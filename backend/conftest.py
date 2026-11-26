"""Fixtures compartilhadas pelos testes de todos os apps."""

import pytest

from conteudos.models import Conteudo, ErroComum, Exercicio
from usuarios.models import Usuario

SENHA = "trilha-de-sinais-2026"


@pytest.fixture
def aluno(db):
    """Estudante com conta criada."""
    return Usuario.objects.create_user(
        username="ana@exemplo.com",
        email="ana@exemplo.com",
        password=SENHA,
        first_name="Ana",
    )


@pytest.fixture
def cliente_aluno(client, aluno):
    """Navegador com a aluna Ana conectada."""
    client.force_login(aluno)
    return client


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
