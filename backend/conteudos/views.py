from django.db.models import Count
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET, require_http_methods

from .forms import RespostaForm
from .models import Conteudo, Exercicio


@require_GET
def lista_conteudos(request):
    """Trilha de conteúdos, na ordem de estudo."""
    # Consultas com contagem (GROUP BY) ignoram o Meta.ordering: ordenamos aqui.
    conteudos = Conteudo.objects.annotate(
        total_exercicios=Count("exercicios")
    ).order_by("ordem")
    return render(request, "conteudos/lista.html", {"conteudos": conteudos})


@require_GET
def detalhe_conteudo(request, slug):
    """Exercícios de um conteúdo."""
    conteudo = get_object_or_404(Conteudo, slug=slug)
    contexto = {"conteudo": conteudo, "exercicios": conteudo.exercicios.order_by("pk")}
    return render(request, "conteudos/detalhe.html", contexto)


@require_http_methods(["GET", "POST"])
def resolver_exercicio(request, slug, pk):
    """Mostra o exercício e corrige a resposta no servidor (RF005)."""
    exercicio = get_object_or_404(Exercicio, pk=pk, conteudo__slug=slug)
    exercicios = exercicio.conteudo.exercicios.order_by("pk")
    resultado = None

    if request.method == "POST":
        form = RespostaForm(request.POST, exercicio=exercicio)
        if form.is_valid():
            resposta = form.cleaned_data["resposta"]
            acertou = exercicio.verificar_resposta(resposta)
            resultado = {
                "acertou": acertou,
                "erro": None if acertou else exercicio.identificar_erro(resposta),
            }
    else:
        form = RespostaForm(exercicio=exercicio)

    contexto = {
        "conteudo": exercicio.conteudo,
        "exercicio": exercicio,
        "form": form,
        "resultado": resultado,
        "posicao": exercicios.filter(pk__lte=exercicio.pk).count(),
        "total": exercicios.count(),
        "proximo": exercicios.filter(pk__gt=exercicio.pk).first(),
    }
    return render(request, "conteudos/exercicio.html", contexto)
