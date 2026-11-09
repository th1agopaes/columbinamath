from django.contrib import admin

from .models import Conteudo, ErroComum, Exercicio, Secao


class SecaoInline(admin.StackedInline):
    """Seções da explicação, editadas dentro do conteúdo (composição)."""

    model = Secao
    extra = 0


@admin.register(Conteudo)
class ConteudoAdmin(admin.ModelAdmin):
    list_display = ("ordem", "nome", "slug")
    list_display_links = ("nome",)
    prepopulated_fields = {"slug": ("nome",)}
    inlines = [SecaoInline]


class ErroComumInline(admin.TabularInline):
    """Erros comuns editados dentro do exercício (composição)."""

    model = ErroComum
    extra = 1


@admin.register(Exercicio)
class ExercicioAdmin(admin.ModelAdmin):
    list_display = ("enunciado", "conteudo", "nivel", "resposta_correta")
    list_filter = ("conteudo", "nivel")
    search_fields = ("enunciado",)
    inlines = [ErroComumInline]
