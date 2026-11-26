import pytest
from django.contrib.admin.sites import site
from django.urls import reverse, reverse_lazy
from pytest_django.asserts import assertContains, assertRedirects

from conftest import SENHA
from conteudos.models import Conteudo, ErroComum, Exercicio
from usuarios.models import Aluno

from .models import Tentativa


@pytest.fixture
def url_exercicio(exercicio):
    return reverse("conteudos:exercicio", args=[exercicio.conteudo.slug, exercicio.pk])


class TestRegistroDaTentativa:
    def test_responder_exige_login(self, client, url_exercicio):
        resposta = client.get(url_exercicio)
        assertRedirects(resposta, f"{reverse('usuarios:entrar')}?next={url_exercicio}")

    def test_acerto_gera_tentativa_correta(self, cliente_aluno, aluno, url_exercicio):
        cliente_aluno.post(url_exercicio, {"resposta": "432"})
        tentativa = Tentativa.objects.get()
        assert tentativa.aluno == aluno
        assert tentativa.resposta_dada == "432"
        assert tentativa.correta is True
        assert tentativa.erro_comum is None
        assert tentativa.data_hora is not None

    def test_erro_comum_fica_associado(self, cliente_aluno, exercicio, url_exercicio):
        cliente_aluno.post(url_exercicio, {"resposta": "422"})
        tentativa = Tentativa.objects.get()
        assert tentativa.correta is False
        assert tentativa.erro_comum == exercicio.erros_comuns.get()

    def test_envio_sem_alternativa_nao_gera_tentativa(
        self, cliente_aluno, url_exercicio
    ):
        cliente_aluno.post(url_exercicio, {})
        assert not Tentativa.objects.exists()

    def test_cada_resposta_gera_nova_tentativa(self, cliente_aluno, url_exercicio):
        cliente_aluno.post(url_exercicio, {"resposta": "422"})
        cliente_aluno.post(url_exercicio, {"resposta": "432"})
        assert Tentativa.objects.count() == 2

    def test_filtrar_por_conteudo(self, aluno, exercicio):
        Tentativa.registrar(aluno, exercicio, "432")
        outro = Exercicio.objects.create(
            conteudo=exercicio.conteudo, enunciado="2 + 2?", resposta_correta="4"
        )
        Tentativa.registrar(aluno, outro, "4")
        assert Tentativa.filtrar(aluno).count() == 2
        assert Tentativa.filtrar(aluno, exercicio.conteudo).count() == 2

    def test_texto_da_tentativa(self, aluno, exercicio):
        tentativa = Tentativa.registrar(aluno, exercicio, "422")
        assert str(tentativa) == "Ana · Quanto é 247 + 185? · erro"


class TestPainel:
    def test_tentativas_sao_somente_leitura(self, rf):
        admin_tentativa = site._registry[Tentativa]
        requisicao = rf.get("/")
        assert admin_tentativa.has_add_permission(requisicao) is False
        assert admin_tentativa.has_change_permission(requisicao) is False


@pytest.fixture
def segundo_conteudo(exercicio):
    """Conteúdo "Regra de sinais", depois de Operações básicas na trilha."""
    conteudo = Conteudo.objects.create(
        nome="Regra de sinais", slug="regra-de-sinais", descricao="-", ordem=2
    )
    outro = Exercicio.objects.create(
        conteudo=conteudo, enunciado="Quanto é (-3) x (-4)?", resposta_correta="12"
    )
    ErroComum.objects.create(
        exercicio=outro, resposta_errada="-12", explicacao="Menos com menos dá mais."
    )
    return outro


class TestCalculoDoProgresso:
    def test_resume_por_conteudo_na_ordem_da_trilha(
        self, aluno, exercicio, segundo_conteudo
    ):
        Tentativa.registrar(aluno, segundo_conteudo, "-12")
        Tentativa.registrar(aluno, exercicio, "422")
        Tentativa.registrar(aluno, exercicio, "432")
        progresso = Aluno.objects.get(pk=aluno.pk).calcular_progresso()

        operacoes, sinais = progresso["conteudos"]
        assert operacoes["nome"] == "Operações básicas"
        assert (operacoes["acertos"], operacoes["erros"]) == (1, 1)
        assert operacoes["percentual"] == 50
        assert (sinais["acertos"], sinais["erros"], sinais["percentual"]) == (0, 1, 0)
        assert (progresso["acertos"], progresso["total"]) == (1, 3)
        assert progresso["percentual"] == 33

    def test_erros_mais_frequentes_primeiro(self, aluno, exercicio, segundo_conteudo):
        Tentativa.registrar(aluno, exercicio, "422")
        Tentativa.registrar(aluno, segundo_conteudo, "-12")
        Tentativa.registrar(aluno, segundo_conteudo, "-12")
        erros = Aluno.objects.get(pk=aluno.pk).calcular_progresso()["erros_frequentes"]
        assert [e["erro_comum__resposta_errada"] for e in erros] == ["-12", "422"]
        assert erros[0]["vezes"] == 2

    def test_sem_tentativas_tudo_zerado(self, aluno):
        progresso = Aluno.objects.get(pk=aluno.pk).calcular_progresso()
        assert progresso["total"] == 0
        assert progresso["percentual"] == 0
        assert progresso["conteudos"] == []

    def test_cada_aluno_conta_so_as_proprias_tentativas(self, aluno, exercicio):
        colega = Aluno.objects.create_user(
            username="caio@exemplo.com", email="caio@exemplo.com", password=SENHA
        )
        Tentativa.registrar(colega, exercicio, "422")
        assert Aluno.objects.get(pk=aluno.pk).calcular_progresso()["total"] == 0


class TestPaginaMeuProgresso:
    url = reverse_lazy("progresso:meu")

    def test_exige_login(self, client, db):
        resposta = client.get(self.url)
        assertRedirects(resposta, f"{reverse('usuarios:entrar')}?next={self.url}")

    def test_orienta_quem_ainda_nao_respondeu(self, cliente_aluno):
        assertContains(cliente_aluno.get(self.url), "Comece pela trilha")

    def test_mostra_o_resumo_e_os_erros(self, cliente_aluno, aluno, exercicio):
        Tentativa.registrar(aluno, exercicio, "422")
        resposta = cliente_aluno.get(self.url)
        assertContains(resposta, "Operações básicas")
        assertContains(resposta, "0%")
        assertContains(resposta, "Você esqueceu o vai um das unidades.")

    def test_outro_perfil_recebe_acesso_negado(self, client, professor):
        client.force_login(professor)
        resposta = client.get(self.url)
        assert resposta.status_code == 403
        assertContains(resposta, "Acesso negado", status_code=403)

    def test_menu_mostra_meu_progresso_para_aluno(self, cliente_aluno, db):
        assertContains(cliente_aluno.get(reverse("conteudos:lista")), "Meu progresso")
