import runpy
from pathlib import Path

CONFIGURACAO = runpy.run_path(
    str(Path(__file__).resolve().parent.parent / "gunicorn.conf.py")
)

# Tempo que o Podman e o Docker esperam, depois do SIGTERM, antes de forçar a parada
TEMPO_DE_PARADA_DO_CONTAINER = 10


class TestConfiguracaoDoGunicorn:
    def test_usa_threads_para_nao_travar_em_conexoes_ociosas(self):
        assert CONFIGURACAO["worker_class"] == "gthread"
        assert CONFIGURACAO["threads"] > 1

    def test_para_antes_do_container_forcar_a_parada(self):
        assert CONFIGURACAO["graceful_timeout"] < TEMPO_DE_PARADA_DO_CONTAINER
