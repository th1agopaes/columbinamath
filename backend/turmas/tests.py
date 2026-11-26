import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains, assertRedirects

from conftest import SENHA
from progresso.models import Tentativa
from usuarios.models import Aluno, Professor, Usuario

from .models import ALFABETO_DO_CODIGO, TAMANHO_DO_CODIGO, Turma


@pytest.fixture
def turma(professor):
    return Professor.objects.get(pk=professor.pk).criar_turma("1º ano A")


class TestTurma:
    def test_criar_turma_gera_codigo_de_acesso(self, turma, professor):
        assert turma.professor == professor
        assert len(turma.codigo_acesso) == TAMANHO_DO_CODIGO
        assert set(turma.codigo_acesso) <= set(ALFABETO_DO_CODIGO)

    def test_codigos_sao_unicos(self, professor):
        professor = Professor.objects.get(pk=professor.pk)
        codigos = {professor.criar_turma(f"Turma {n}").codigo_acesso for n in range(20)}
        assert len(codigos) == 20

    def test_codigo_nao_muda_ao_salvar_de_novo(self, turma):
        codigo = turma.codigo_acesso
        turma.nome = "1º ano B"
        turma.save()
        assert Turma.objects.get(pk=turma.pk).codigo_acesso == codigo

    def test_aluno_entra_com_codigo_sem_diferenciar_maiusculas(self, turma, aluno):
        aluno = Aluno.objects.get(pk=aluno.pk)
        assert aluno.entrar_turma(f"  {turma.codigo_acesso.lower()} ") is True
        assert turma.possui_aluno(aluno)

    def test_codigo_inexistente_nao_entra(self, turma, aluno):
        aluno = Aluno.objects.get(pk=aluno.pk)
        assert aluno.entrar_turma("ZZZZZZ") is False
        assert not turma.possui_aluno(aluno)

    def test_texto_da_turma(self, turma):
        assert str(turma) == f"1º ano A ({turma.codigo_acesso})"


class TestPaginasDoProfessor:
    def test_cria_turma_e_mostra_o_codigo(self, client, professor):
        client.force_login(professor)
        resposta = client.post(
            reverse("turmas:criar"), {"nome": "1º ano A"}, follow=True
        )
        turma = Turma.objects.get()
        assertContains(resposta, f"Passe o código {turma.codigo_acesso}")
        assertContains(resposta, "1º ano A")

    def test_formulario_de_criar_turma(self, client, professor):
        client.force_login(professor)
        assertContains(client.get(reverse("turmas:criar")), "Nome da turma")

    def test_lista_so_as_turmas_do_professor(self, client, professor, turma):
        outro = Professor.objects.create_user(
            username="rita@exemplo.com", email="rita@exemplo.com", password=SENHA
        )
        outro.criar_turma("Turma da Rita")
        client.force_login(professor)
        resposta = client.get(reverse("turmas:lista"))
        assertContains(resposta, "1º ano A")
        assert "Turma da Rita" not in resposta.content.decode()

    def test_aluno_nao_cria_turma(self, cliente_aluno):
        assert cliente_aluno.get(reverse("turmas:criar")).status_code == 403


class TestPaginasDoAluno:
    def test_entra_na_turma_pelo_codigo(self, cliente_aluno, aluno, turma):
        resposta = cliente_aluno.post(
            reverse("turmas:entrar"),
            {"codigo_acesso": turma.codigo_acesso},
            follow=True,
        )
        assertContains(resposta, "Você entrou na turma.")
        assertContains(resposta, "1º ano A")
        assert turma.possui_aluno(aluno)

    def test_codigo_errado_mostra_aviso(self, cliente_aluno, turma):
        resposta = cliente_aluno.post(
            reverse("turmas:entrar"), {"codigo_acesso": "ZZZZZZ"}, follow=True
        )
        assertContains(resposta, "Código não encontrado.")

    def test_professor_nao_usa_codigo(self, client, professor):
        client.force_login(professor)
        resposta = client.post(reverse("turmas:entrar"), {"codigo_acesso": "ABCDEF"})
        assert resposta.status_code == 403

    def test_turmas_exige_login(self, client, db):
        url = reverse("turmas:lista")
        assertRedirects(client.get(url), f"{reverse('usuarios:entrar')}?next={url}")

    def test_administrador_nao_tem_pagina_de_turmas(self, client, db):
        admin = Usuario.objects.create_superuser(
            username="admin", email="admin@exemplo.com", password=SENHA
        )
        client.force_login(admin)
        assert client.get(reverse("turmas:lista")).status_code == 403

    def test_menu_mostra_turmas(self, cliente_aluno):
        assertContains(cliente_aluno.get(reverse("conteudos:lista")), "Turmas")


@pytest.fixture
def turma_com_alunos(turma, aluno, exercicio):
    """Turma com Ana (1 acerto e 1 erro) e Caio (sem respostas)."""
    caio = Aluno.objects.create_user(
        username="caio@exemplo.com",
        email="caio@exemplo.com",
        password=SENHA,
        first_name="Caio",
    )
    turma.adicionar_aluno(aluno)
    turma.adicionar_aluno(caio)
    Tentativa.registrar(aluno, exercicio, "422")
    Tentativa.registrar(aluno, exercicio, "432")
    return turma


class TestDesempenho:
    def test_resume_cada_aluno_e_os_conteudos_com_mais_erros(self, turma_com_alunos):
        desempenho = turma_com_alunos.calcular_desempenho()
        ana, caio = desempenho["alunos"]
        assert (ana["aluno"].first_name, ana["acertos"], ana["erros"]) == ("Ana", 1, 1)
        assert ana["percentual"] == 50
        assert (caio["total"], caio["percentual"]) == (0, 0)
        assert desempenho["conteudos_com_mais_erros"] == [
            {"exercicio__conteudo__nome": "Operações básicas", "erros": 1}
        ]

    def test_ignora_tentativas_de_quem_nao_esta_na_turma(self, turma, aluno, exercicio):
        Tentativa.registrar(aluno, exercicio, "422")
        desempenho = turma.calcular_desempenho()
        assert desempenho["alunos"] == []
        assert desempenho["conteudos_com_mais_erros"] == []


class TestPaginaDaTurma:
    def test_mostra_alunos_e_conteudos_com_mais_erros(
        self, client, professor, turma_com_alunos
    ):
        client.force_login(professor)
        resposta = client.get(turma_com_alunos.get_absolute_url())
        assertContains(resposta, "Ana")
        assertContains(resposta, "Caio")
        assertContains(resposta, "Operações básicas: 1 erro")

    def test_turma_vazia_mostra_o_codigo(self, client, professor, turma):
        client.force_login(professor)
        resposta = client.get(turma.get_absolute_url())
        assertContains(resposta, "Nenhum aluno entrou na turma ainda")
        assertContains(resposta, turma.codigo_acesso)

    def test_professor_nao_ve_turma_de_outro(self, client, turma):
        outro = Professor.objects.create_user(
            username="rita@exemplo.com", email="rita@exemplo.com", password=SENHA
        )
        client.force_login(outro)
        assert client.get(turma.get_absolute_url()).status_code == 404

    def test_aluno_nao_ve_desempenho_da_turma(self, cliente_aluno, turma):
        assert cliente_aluno.get(turma.get_absolute_url()).status_code == 403

    def test_professor_ve_o_progresso_de_um_aluno(
        self, client, professor, aluno, turma_com_alunos
    ):
        client.force_login(professor)
        url = reverse("turmas:aluno", args=[turma_com_alunos.pk, aluno.pk])
        resposta = client.get(url)
        assertContains(resposta, "Progresso de Ana")
        assertContains(resposta, "Você esqueceu o vai um das unidades.")

    def test_aluno_sem_respostas_tem_aviso_proprio(
        self, client, professor, turma_com_alunos
    ):
        client.force_login(professor)
        caio = Aluno.objects.get(first_name="Caio")
        url = reverse("turmas:aluno", args=[turma_com_alunos.pk, caio.pk])
        assertContains(client.get(url), "Caio ainda não resolveu exercícios.")

    def test_nega_aluno_de_outra_turma(self, client, professor, turma):
        """Extensão 6a do UC4."""
        de_fora = Aluno.objects.create_user(
            username="davi@exemplo.com", email="davi@exemplo.com", password=SENHA
        )
        client.force_login(professor)
        url = reverse("turmas:aluno", args=[turma.pk, de_fora.pk])
        assert client.get(url).status_code == 403
