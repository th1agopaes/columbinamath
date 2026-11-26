from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET, require_http_methods

from progresso.models import Tentativa

from .forms import RespostaForm
from .models import Conteudo, Exercicio


@require_GET
def lista_conteudos(request):
    """Trilha de conteúdos, na ordem de estudo."""
    return render(request, "conteudos/lista.html", {"conteudos": Conteudo.listar()})


@require_GET
def detalhe_conteudo(request, slug):
    """Explicação e exercícios de um conteúdo. A explicação é aberta a todos."""
    conteudo = get_object_or_404(Conteudo, slug=slug)
    contexto = {"conteudo": conteudo, "exercicios": conteudo.exercicios.order_by("pk")}
    if request.user.is_authenticated:
        acertados = request.user.tentativas.filter(
            correta=True, exercicio__conteudo=conteudo
        ).values_list("exercicio", flat=True)
        contexto["acertados"] = set(acertados)
        contexto["proximo"] = conteudo.proximo_exercicio(request.user)
    return render(request, "conteudos/detalhe.html", contexto)


@login_required
@require_http_methods(["GET", "POST"])
def resolver_exercicio(request, slug, pk):
    """Corrige a resposta no servidor e registra a tentativa (UC1, RF005)."""
    exercicio = get_object_or_404(Exercicio, pk=pk, conteudo__slug=slug)
    exercicios = exercicio.conteudo.exercicios.order_by("pk")
    tentativa = None

    if request.method == "POST":
        form = RespostaForm(request.POST, exercicio=exercicio)
        if form.is_valid():
            tentativa = Tentativa.registrar(
                request.user, exercicio, form.cleaned_data["resposta"]
            )
    else:
        form = RespostaForm(exercicio=exercicio)

    contexto = {
        "conteudo": exercicio.conteudo,
        "exercicio": exercicio,
        "form": form,
        "tentativa": tentativa,
        "posicao": exercicios.filter(pk__lte=exercicio.pk).count(),
        "total": exercicios.count(),
        "proximo": exercicios.filter(pk__gt=exercicio.pk).first(),
    }
    return render(request, "conteudos/exercicio.html", contexto)
