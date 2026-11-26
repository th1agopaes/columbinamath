"""Métrica de negócio: respostas dos alunos, por resultado (ADR 0005)."""

from prometheus_client import Counter

TENTATIVAS = Counter(
    "columbinamath_tentativas",
    "Respostas enviadas pelos alunos, por resultado (acerto ou erro).",
    ["resultado"],
)
