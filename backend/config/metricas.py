"""Métricas HTTP da aplicação no formato do Prometheus (ADR 0005).

O Prometheus lê estas métricas pela porta METRICAS_PORTA, aberta pelo
gunicorn.conf.py, e o Grafana as mostra em painéis.
"""

import time

from prometheus_client import Counter, Histogram

REQUISICOES = Counter(
    "columbinamath_requisicoes",
    "Requisições HTTP atendidas, por método, página e código de status.",
    ["metodo", "view", "status"],
)

TEMPO_DE_RESPOSTA = Histogram(
    "columbinamath_tempo_resposta_segundos",
    "Tempo para responder a uma requisição, em segundos (RNF001: até 2 s).",
    ["metodo", "view"],
    # Faixas de tempo; a de 2 s corresponde ao limite do RNF001
    buckets=(0.05, 0.1, 0.25, 0.5, 1.0, 2.0, 5.0),
)

# Endereços que não existem ficam num único rótulo, para que URLs aleatórias
# não criem uma série nova no Prometheus a cada acesso.
VIEW_NAO_ENCONTRADA = "nao_encontrada"


class MetricasMiddleware:
    """Conta cada requisição e mede o tempo de resposta.

    Fica depois do WhiteNoise na lista de middlewares: os arquivos estáticos
    são servidos antes de chegar aqui e não entram nas métricas.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        inicio = time.perf_counter()
        resposta = self.get_response(request)
        duracao = time.perf_counter() - inicio

        rota = getattr(request, "resolver_match", None)
        view = rota.view_name if rota else VIEW_NAO_ENCONTRADA
        REQUISICOES.labels(request.method, view, resposta.status_code).inc()
        TEMPO_DE_RESPOSTA.labels(request.method, view).observe(duracao)
        return resposta
