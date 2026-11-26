"""Cálculos de progresso e desempenho.

O progresso não é armazenado: é calculado na hora a partir das tentativas
(Modelagem - Parte I, modelo conceitual), para evitar dados redundantes.
"""

from django.db.models import Count, Q, QuerySet


def percentual(acertos: int, total: int) -> int:
    """Percentual de acerto, arredondado; zero quando não há tentativas."""
    return round(100 * acertos / total) if total else 0


def resumir(tentativas: QuerySet) -> dict:
    """Acertos, erros e percentual por conteúdo e no total (RF006)."""
    linhas = (
        tentativas.values(
            "exercicio__conteudo__nome",
            "exercicio__conteudo__slug",
            "exercicio__conteudo__ordem",
        )
        .annotate(total=Count("pk"), acertos=Count("pk", filter=Q(correta=True)))
        .order_by("exercicio__conteudo__ordem")
    )
    conteudos = [
        {
            "nome": linha["exercicio__conteudo__nome"],
            "slug": linha["exercicio__conteudo__slug"],
            "acertos": linha["acertos"],
            "erros": linha["total"] - linha["acertos"],
            "total": linha["total"],
            "percentual": percentual(linha["acertos"], linha["total"]),
        }
        for linha in linhas
    ]
    acertos = sum(c["acertos"] for c in conteudos)
    total = sum(c["total"] for c in conteudos)
    return {
        "conteudos": conteudos,
        "acertos": acertos,
        "erros": total - acertos,
        "total": total,
        "percentual": percentual(acertos, total),
    }


def erros_frequentes(tentativas: QuerySet, limite: int = 3) -> list[dict]:
    """Erros comuns mais cometidos, do mais frequente para o menos frequente."""
    return list(
        tentativas.filter(erro_comum__isnull=False)
        .values(
            "erro_comum__resposta_errada",
            "erro_comum__explicacao",
            "exercicio__enunciado",
        )
        .annotate(vezes=Count("pk"))
        .order_by("-vezes", "erro_comum__pk")[:limite]
    )


def conteudos_com_mais_erros(tentativas: QuerySet, limite: int = 3) -> list[dict]:
    """Conteúdos com mais respostas erradas, para o professor priorizar (UC4)."""
    return list(
        tentativas.filter(correta=False)
        .values("exercicio__conteudo__nome")
        .annotate(erros=Count("pk"))
        .order_by("-erros", "exercicio__conteudo__ordem")[:limite]
    )
