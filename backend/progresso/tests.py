import pytest
from django.contrib.admin.sites import site
from django.urls import reverse
from pytest_django.asserts import assertRedirects

from conteudos.models import Exercicio

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
