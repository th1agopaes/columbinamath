from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET

from usuarios.models import Aluno, TipoUsuario
from usuarios.permissoes import perfil_obrigatorio


@require_GET
@perfil_obrigatorio(TipoUsuario.ALUNO)
def meu_progresso(request):
    """Página "Meu progresso" (UC2): cada aluno vê só o próprio progresso."""
    aluno = get_object_or_404(Aluno, pk=request.user.pk)
    contexto = {
        "aluno": aluno,
        "progresso": aluno.calcular_progresso(),
        "titulo": "Meu progresso",
    }
    return render(request, "progresso/progresso.html", contexto)
