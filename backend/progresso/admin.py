from django.contrib import admin

from .models import Tentativa


@admin.register(Tentativa)
class TentativaAdmin(admin.ModelAdmin):
    """Consulta das tentativas. Somente leitura: elas são o histórico do aluno."""

    list_display = ("data_hora", "aluno", "exercicio", "resposta_dada", "correta")
    list_filter = ("correta", "exercicio__conteudo")
    search_fields = ("aluno__email", "aluno__first_name")
    date_hierarchy = "data_hora"

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
