import pytest
from django.urls import reverse

from conteudos.models import Conteudo, ErroComum, Exercicio


@pytest.fixture
def api(client):
    """Cliente HTTP que pede JSON, como um aplicativo consumindo a API."""
    client.defaults["HTTP_ACCEPT"] = "application/json"
    return client


class TestConteudos:
    def test_lista_a_trilha_na_ordem(self, api, exercicio):
        Conteudo.objects.create(nome="Frações", slug="fracoes", descricao="-", ordem=2)
        dados = api.get(reverse("api:conteudo-list")).json()
        assert [c["slug"] for c in dados] == ["operacoes-basicas", "fracoes"]
        assert dados[0]["total_exercicios"] == 1
        assert dados[1]["total_exercicios"] == 0

    def test_detalhe_pelo_slug_com_os_exercicios(self, api, exercicio):
        url = reverse("api:conteudo-detail", args=["operacoes-basicas"])
        dados = api.get(url).json()
        assert dados["nome"] == "Operações básicas"
        assert dados["exercicios"] == [
            {"id": exercicio.pk, "enunciado": "Quanto é 247 + 185?", "nivel": "facil"}
        ]

    def test_conteudo_inexistente_retorna_404(self, api, db):
        url = reverse("api:conteudo-detail", args=["nao-existe"])
        assert api.get(url).status_code == 404


class TestExercicios:
    def test_mostra_as_alternativas_sem_a_resposta_correta(self, api, exercicio):
        dados = api.get(reverse("api:exercicio-detail", args=[exercicio.pk])).json()
        assert dados["alternativas"] == ["422", "432"]
        assert dados["conteudo"] == "operacoes-basicas"
        assert "resposta_correta" not in dados
        assert "resolucao" not in dados

    def test_filtra_por_conteudo(self, api, exercicio):
        outro = Conteudo.objects.create(
            nome="Regra de sinais", slug="regra-de-sinais", descricao="-", ordem=2
        )
        sinais = Exercicio.objects.create(
            conteudo=outro, enunciado="(-3) x (-4)?", resposta_correta="12"
        )
        ErroComum.objects.create(
            exercicio=sinais, resposta_errada="-12", explicacao="x"
        )
        url = reverse("api:exercicio-list") + "?conteudo=regra-de-sinais"
        assert [e["id"] for e in api.get(url).json()] == [sinais.pk]

    def test_api_e_somente_leitura(self, api, exercicio):
        url = reverse("api:exercicio-list")
        resposta = api.post(url, {"enunciado": "x"}, content_type="application/json")
        assert resposta.status_code == 405

    def test_raiz_lista_os_recursos(self, api, db):
        dados = api.get(reverse("api:api-root")).json()
        assert set(dados) == {"conteudos", "exercicios"}

    def test_interface_navegavel_no_navegador(self, client, exercicio):
        resposta = client.get(reverse("api:conteudo-list"), HTTP_ACCEPT="text/html")
        assert resposta.status_code == 200
        assert "text/html" in resposta["Content-Type"]
