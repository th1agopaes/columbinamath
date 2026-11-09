import pytest
from django.core.exceptions import ValidationError
from django.urls import reverse
from pytest_django.asserts import assertContains, assertNotContains

from .models import (
    Conteudo,
    ErroComum,
    Exercicio,
    Secao,
    normalizar_resposta,
    separar_linhas,
)


@pytest.fixture
def exercicio(db):
    """Exercício "247 + 185" salvo no banco, com um erro comum cadastrado."""
    conteudo = Conteudo.objects.create(
        nome="Operações básicas",
        slug="operacoes-basicas",
        descricao="As quatro operações.",
        ordem=1,
    )
    exercicio = Exercicio.objects.create(
        conteudo=conteudo,
        enunciado="Quanto é 247 + 185?",
        resposta_correta="432",
    )
    ErroComum.objects.create(
        exercicio=exercicio,
        resposta_errada="422",
        explicacao="Você esqueceu o vai um das unidades.",
    )
    return exercicio


class TestNormalizarResposta:
    def test_remove_espacos(self):
        assert normalizar_resposta(" 4 32 ") == "432"

    def test_troca_o_menos_tipografico_pelo_do_teclado(self):
        assert normalizar_resposta("\u22128") == "-8"


class TestVerificarResposta:
    def test_aceita_a_resposta_correta(self, exercicio):
        assert exercicio.verificar_resposta("432") is True

    def test_recusa_a_resposta_errada(self, exercicio):
        assert exercicio.verificar_resposta("422") is False

    def test_ignora_espacos(self, exercicio):
        assert exercicio.verificar_resposta(" 432 ") is True


class TestIdentificarErro:
    def test_encontra_o_erro_comum(self, exercicio):
        erro = exercicio.identificar_erro("422")
        assert erro is not None
        assert erro.resposta_errada == "422"

    def test_retorna_none_para_erro_nao_previsto(self, exercicio):
        assert exercicio.identificar_erro("999") is None


class TestValidacaoDoErroComum:
    def test_recusa_erro_igual_a_resposta_correta(self, exercicio):
        erro = ErroComum(exercicio=exercicio, resposta_errada=" 432", explicacao="x")
        with pytest.raises(ValidationError):
            erro.clean()

    def test_valida_mesmo_com_o_exercicio_ainda_nao_salvo(self):
        # Cenário do painel: exercício e erros comuns são cadastrados juntos.
        novo = Exercicio(enunciado="Quanto é 2 + 2?", resposta_correta="4")
        erro = ErroComum(exercicio=novo, resposta_errada="4", explicacao="x")
        with pytest.raises(ValidationError):
            erro.clean()

    def test_aceita_erro_diferente_da_resposta_correta(self, exercicio):
        erro = ErroComum(exercicio=exercicio, resposta_errada="322", explicacao="x")
        erro.clean()  # não deve levantar exceção


@pytest.fixture
def url_exercicio(exercicio):
    return reverse("conteudos:exercicio", args=[exercicio.conteudo.slug, exercicio.pk])


class TestPaginas:
    def test_lista_mostra_os_conteudos(self, client, exercicio):
        resposta = client.get(reverse("conteudos:lista"))
        assertContains(resposta, "Operações básicas")

    def test_lista_segue_a_ordem_da_trilha(self, client, exercicio):
        Conteudo.objects.create(nome="Frações", slug="fracoes", descricao="-", ordem=2)
        html = client.get(reverse("conteudos:lista")).content.decode()
        assert html.index("Operações básicas") < html.index("Frações")

    def test_conteudo_inexistente_retorna_404(self, client, db):
        resposta = client.get(reverse("conteudos:detalhe", args=["nao-existe"]))
        assert resposta.status_code == 404

    def test_resposta_correta_mostra_acerto(self, client, url_exercicio):
        resposta = client.post(url_exercicio, {"resposta": "432"})
        assertContains(resposta, "Resposta correta")

    def test_erro_comum_mostra_a_explicacao(self, client, url_exercicio):
        resposta = client.post(url_exercicio, {"resposta": "422"})
        assertContains(resposta, "Você esqueceu o vai um das unidades.")

    def test_recusa_alternativa_que_nao_existe(self, client, url_exercicio):
        resposta = client.post(url_exercicio, {"resposta": "999"})
        assertNotContains(resposta, "Resposta correta")
        assertNotContains(resposta, "Resposta incorreta")


class TestTeoriaEResolucao:
    def test_separar_linhas_ignora_linhas_vazias(self):
        assert separar_linhas("Passo 1\n\n  Passo 2  \n") == ["Passo 1", "Passo 2"]

    def test_detalhe_mostra_a_explicacao_e_o_exemplo(self, client, exercicio):
        Secao.objects.create(
            conteudo=exercicio.conteudo,
            ordem=1,
            titulo="Adição",
            explicacao="Adicionar é juntar quantidades.",
            exemplo="158 + 276",
            passos="Unidades: 8 + 6 = 14.\nDezenas: 5 + 7 + 1 = 13.",
            resultado="158 + 276 = 434",
        )
        url = reverse("conteudos:detalhe", args=[exercicio.conteudo.slug])
        resposta = client.get(url)
        assertContains(resposta, "Adicionar é juntar quantidades.")
        assertContains(resposta, "<li>Dezenas: 5 + 7 + 1 = 13.</li>", html=True)

    def test_resultado_mostra_a_resolucao_mesmo_no_acerto(
        self, client, exercicio, url_exercicio
    ):
        exercicio.resolucao = "Unidades: 7 + 5 = 12.\nResultado: 432."
        exercicio.save()
        resposta = client.post(url_exercicio, {"resposta": "432"})
        assertContains(resposta, "Alternativa correta")
        assertContains(resposta, "<li>Resultado: 432.</li>", html=True)
