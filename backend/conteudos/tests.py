import pytest
from django.core.exceptions import ValidationError

from .models import Conteudo, ErroComum, Exercicio, normalizar_resposta


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
