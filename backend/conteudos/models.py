from django.db import models


class NivelDificuldade(models.TextChoices):
    """Níveis de dificuldade (enumeração, NivelDificuldade do diagrama de classes)."""

    FACIL = "facil", "Fácil"
    MEDIO = "medio", "Médio"
    DIFICIL = "dificil", "Difícil"


class Conteudo(models.Model):
    """Tema de matemática básica, na ordem da trilha de estudo."""

    nome = models.CharField("nome", max_length=100)
    slug = models.SlugField("slug", unique=True)
    descricao = models.CharField("descrição", max_length=200)
    ordem = models.PositiveSmallIntegerField("ordem")

    class Meta:
        ordering = ["ordem"]
        verbose_name = "conteúdo"
        verbose_name_plural = "conteúdos"

    def __str__(self):
        return self.nome


class Exercicio(models.Model):
    """Exercício de um conteúdo. Composição: não existe sem o conteúdo."""

    conteudo = models.ForeignKey(
        Conteudo,
        on_delete=models.CASCADE,
        related_name="exercicios",
        verbose_name="conteúdo",
    )
    enunciado = models.TextField("enunciado")
    resposta_correta = models.CharField("resposta correta", max_length=50)
    nivel = models.CharField(
        "nível",
        max_length=10,
        choices=NivelDificuldade.choices,
        default=NivelDificuldade.FACIL,
    )

    class Meta:
        verbose_name = "exercício"
        verbose_name_plural = "exercícios"

    def __str__(self):
        return self.enunciado


class ErroComum(models.Model):
    """Resposta errada esperada e a explicação mostrada como feedback."""

    exercicio = models.ForeignKey(
        Exercicio,
        on_delete=models.CASCADE,
        related_name="erros_comuns",
        verbose_name="exercício",
    )
    resposta_errada = models.CharField("resposta errada", max_length=50)
    explicacao = models.TextField("explicação")

    class Meta:
        verbose_name = "erro comum"
        verbose_name_plural = "erros comuns"
        constraints = [
            models.UniqueConstraint(
                fields=["exercicio", "resposta_errada"],
                name="erro_comum_unico_por_exercicio",
            ),
        ]

    def __str__(self):
        return self.resposta_errada
