from django.contrib import admin

from .models import Turma


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ("nome", "codigo_acesso", "professor", "data_criacao")
    list_filter = ("professor",)
    search_fields = ("nome", "codigo_acesso")
    readonly_fields = ("codigo_acesso", "data_criacao")
    filter_horizontal = ("alunos",)
