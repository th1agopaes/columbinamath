from functools import wraps

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


def perfil_obrigatorio(tipo):
    """Exige login e um perfil específico; outro perfil recebe 403 (acesso negado)."""

    def decorador(view):
        @wraps(view)
        @login_required
        def view_protegida(request, *args, **kwargs):
            if request.user.tipo != tipo:
                raise PermissionDenied
            return view(request, *args, **kwargs)

        return view_protegida

    return decorador
