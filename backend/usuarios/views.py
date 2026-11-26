from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_http_methods

from .forms import CadastroForm, EntrarForm


class EntrarView(LoginView):
    """Login por e-mail (RF001). Quem já está conectado volta para a trilha."""

    form_class = EntrarForm
    template_name = "usuarios/entrar.html"
    redirect_authenticated_user = True


@require_http_methods(["GET", "POST"])
def cadastrar(request):
    """Cria a conta de estudante e já entra com ela (US07)."""
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)

    proximo = request.POST.get("next") or request.GET.get("next", "")
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario, backend="django.contrib.auth.backends.ModelBackend")
            # Só redireciona para endereços do próprio site (evita open redirect).
            if url_has_allowed_host_and_scheme(
                proximo, allowed_hosts={request.get_host()}
            ):
                return redirect(proximo)
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = CadastroForm()

    return render(request, "usuarios/cadastro.html", {"form": form, "next": proximo})
