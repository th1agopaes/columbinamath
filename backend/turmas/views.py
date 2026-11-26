from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET, require_http_methods, require_POST

from usuarios.models import Aluno, Professor, TipoUsuario
from usuarios.permissoes import perfil_obrigatorio

from .forms import CriarTurmaForm, EntrarTurmaForm


@require_GET
@login_required
def lista_turmas(request):
    """Turmas do usuário: as que o professor criou ou as que o aluno participa."""
    if request.user.tipo == TipoUsuario.PROFESSOR:
        turmas = request.user.turmas_criadas.all()
        return render(request, "turmas/professor_lista.html", {"turmas": turmas})
    if request.user.tipo == TipoUsuario.ALUNO:
        contexto = {"turmas": request.user.turmas.all(), "form": EntrarTurmaForm()}
        return render(request, "turmas/aluno_lista.html", contexto)
    raise PermissionDenied


@require_http_methods(["GET", "POST"])
@perfil_obrigatorio(TipoUsuario.PROFESSOR)
def criar_turma(request):
    """O professor cria a turma e recebe o código para passar aos alunos (RF007)."""
    form = CriarTurmaForm(request.POST or None)
    if form.is_valid():
        professor = get_object_or_404(Professor, pk=request.user.pk)
        turma = professor.criar_turma(form.cleaned_data["nome"])
        messages.success(
            request, f"Turma criada. Passe o código {turma.codigo_acesso} aos alunos."
        )
        return redirect("turmas:lista")
    return render(request, "turmas/criar.html", {"form": form})


@require_POST
@perfil_obrigatorio(TipoUsuario.ALUNO)
def entrar_turma(request):
    """O aluno entra em uma turma com o código de acesso (RF007)."""
    form = EntrarTurmaForm(request.POST)
    aluno = get_object_or_404(Aluno, pk=request.user.pk)
    if form.is_valid() and aluno.entrar_turma(form.cleaned_data["codigo_acesso"]):
        messages.success(request, "Pronto! Você entrou na turma.")
    else:
        messages.error(request, "Código não encontrado. Confira com o seu professor.")
    return redirect("turmas:lista")
