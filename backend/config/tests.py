import runpy
from pathlib import Path
from types import SimpleNamespace

from django.urls import reverse
from prometheus_client import REGISTRY

CONFIGURACAO = runpy.run_path(
    str(Path(__file__).resolve().parent.parent / "gunicorn.conf.py")
)

# Tempo que o Podman e o Docker esperam, depois do SIGTERM, antes de forçar a parada
TEMPO_DE_PARADA_DO_CONTAINER = 10


def amostra(nome, **rotulos):
    """Valor atual de uma métrica no registro do Prometheus (0 se ainda não existe)."""
    return REGISTRY.get_sample_value(nome, rotulos) or 0


class TestConfiguracaoDoGunicorn:
    def test_usa_threads_para_nao_travar_em_conexoes_ociosas(self):
        assert CONFIGURACAO["worker_class"] == "gthread"
        assert CONFIGURACAO["threads"] > 1

    def test_para_antes_do_container_forcar_a_parada(self):
        assert CONFIGURACAO["graceful_timeout"] < TEMPO_DE_PARADA_DO_CONTAINER

    def test_abre_a_porta_de_metricas_so_quando_configurada(self, monkeypatch):
        portas = []
        gancho = CONFIGURACAO["post_worker_init"]
        monkeypatch.setitem(gancho.__globals__, "start_http_server", portas.append)

        # Imita o worker do Gunicorn: o gancho só usa worker.log.info
        worker = SimpleNamespace(log=SimpleNamespace(info=lambda *args: None))

        monkeypatch.delenv("METRICAS_PORTA", raising=False)
        gancho(worker)
        monkeypatch.setenv("METRICAS_PORTA", "9100")
        gancho(worker)
        assert portas == [9100]


class TestMetricasHttp:
    def test_conta_a_requisicao_pela_view(self, client, db):
        rotulos = {"metodo": "GET", "view": "conteudos:lista", "status": "200"}
        antes = amostra("columbinamath_requisicoes_total", **rotulos)
        client.get(reverse("conteudos:lista"))
        assert amostra("columbinamath_requisicoes_total", **rotulos) == antes + 1

    def test_mede_o_tempo_de_resposta(self, client, db):
        rotulos = {"metodo": "GET", "view": "conteudos:lista"}
        antes = amostra("columbinamath_tempo_resposta_segundos_count", **rotulos)
        client.get(reverse("conteudos:lista"))
        depois = amostra("columbinamath_tempo_resposta_segundos_count", **rotulos)
        assert depois == antes + 1
        # A faixa de 2 s (limite do RNF001) existe no histograma
        assert (
            amostra("columbinamath_tempo_resposta_segundos_bucket", le="2.0", **rotulos)
            >= 1
        )

    def test_enderecos_inexistentes_usam_um_rotulo_so(self, client, db):
        rotulos = {"metodo": "GET", "view": "nao_encontrada", "status": "404"}
        antes = amostra("columbinamath_requisicoes_total", **rotulos)
        client.get("/um-endereco-qualquer/")
        client.get("/outro-endereco/")
        assert amostra("columbinamath_requisicoes_total", **rotulos) == antes + 2
