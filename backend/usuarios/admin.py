from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    """Painel de usuários reaproveitando o UserAdmin, com o campo tipo."""

    fieldsets = UserAdmin.fieldsets + (("ColumbinaMath", {"fields": ("tipo",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("ColumbinaMath", {"fields": ("email", "tipo")}),
    )
    list_display = ("username", "email", "first_name", "tipo", "is_staff")
    list_filter = UserAdmin.list_filter + ("tipo",)
