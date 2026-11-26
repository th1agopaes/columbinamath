"""Configuração do Gunicorn no container. O Gunicorn lê este arquivo sozinho,
porque ele fica na pasta em que o servidor é iniciado (WORKDIR da imagem).

Por que o worker gthread: o worker padrão (sync) atende uma conexão por vez.
Quando o navegador abre uma conexão e não envia nada (a pré-conexão do Chrome),
o worker fica preso nela até o timeout. A página demora e, ao parar o container,
o Gunicorn espera até 30 s, mais que os 10 s que o Podman dá antes de forçar a
parada. O gthread atende cada conexão numa thread e não fica preso (ADR 0004).
"""

import os

from prometheus_client import start_http_server

bind = "0.0.0.0:8000"

# Um processo com várias threads atende a escala do projeto com pouca memória.
# Com um só processo, as métricas do Prometheus ficam num único lugar (ADR 0005).
worker_class = "gthread"
workers = 1
threads = 8

# Uma requisição que passa de 30 s é encerrada.
timeout = 30
# Ao receber o sinal de parada (SIGTERM), espera no máximo 5 s pelas requisições
# em andamento, abaixo dos 10 s que o Podman e o Docker esperam.
graceful_timeout = 5

# Log de acesso na saída padrão, para aparecer no "podman compose logs".
accesslog = "-"


def post_worker_init(worker):
    """Abre a porta das métricas para o Prometheus quando METRICAS_PORTA existe.

    A porta é interna da rede dos containers: o docker-compose.yml não a publica
    no computador, então as métricas não ficam expostas como uma página do site.
    """
    porta = os.environ.get("METRICAS_PORTA")
    if porta:
        start_http_server(int(porta))
        worker.log.info("Métricas do Prometheus na porta %s", porta)
