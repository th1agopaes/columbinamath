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
    """Erros comuns editados dentro do exercício (composição).

    Pelo menos um é obrigatório: as alternativas do exercício são a resposta
    correta e os erros comuns, então sem eles haveria uma única alternativa.
    """

    model = ErroComum
    extra = 1
    min_num = 1
    validate_min = True


@admin.register(Exercicio)
class ExercicioAdmin(admin.ModelAdmin):
    list_display = ("enunciado", "conteudo", "nivel", "resposta_correta")
    list_filter = ("conteudo", "nivel")
    search_fields = ("enunciado",)
    inlines = [ErroComumInline]
