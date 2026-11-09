from django.core.exceptions import ValidationError
from django.db import models

SINAL_DE_MENOS = "\u2212"  # "U+2212", o sinal de menos tipográfico


def normalizar_resposta(resposta: str) -> str:
    """Padroniza uma resposta para comparação: sem espaços e com o menos do teclado."""
    return "".join(resposta.split()).replace(SINAL_DE_MENOS, "-")


UM_POR_LINHA = "Escreva um passo por linha."


def separar_linhas(texto: str) -> list[str]:
    """Transforma um texto com um passo por linha em uma lista, sem linhas vazias."""
    return [linha.strip() for linha in texto.splitlines() if linha.strip()]


class NivelDificuldade(models.TextChoices):
    """Níveis de dificuldade (enumeração NivelDificuldade do diagrama de classes)."""

    FACIL = "facil", "Fácil"
    MEDIO = "medio", "Médio"
    DIFICIL = "dificil", "Difícil"


class Conteudo(models.Model):
    """Tema de matemática básica, na ordem da trilha de estudo."""

    nome = models.CharField("nome", max_length=100)
    slug = models.SlugField("slug", unique=True)
    descricao = models.CharField("descrição", max_length=200)
    ordem = models.PositiveSmallIntegerField("ordem")
    introducao = models.TextField("introdução", blank=True)

    class Meta:
        ordering = ["ordem"]
        verbose_name = "conteúdo"
        verbose_name_plural = "conteúdos"

    def __str__(self):
        return self.nome


class Secao(models.Model):
    """Parte da explicação de um conteúdo, com um exemplo resolvido (US02)."""

    conteudo = models.ForeignKey(
        Conteudo,
        on_delete=models.CASCADE,
        related_name="secoes",
        verbose_name="conteúdo",
    )
    ordem = models.PositiveSmallIntegerField("ordem")
    titulo = models.CharField("título", max_length=100)
    explicacao = models.TextField("explicação")
    exemplo = models.CharField("exemplo", max_length=100, blank=True)
    passos = models.TextField("passos do exemplo", blank=True, help_text=UM_POR_LINHA)
    resultado = models.CharField("resultado", max_length=100, blank=True)
    prova_real = models.CharField("prova real", max_length=100, blank=True)

    class Meta:
        ordering = ["ordem"]
        verbose_name = "seção"
        verbose_name_plural = "seções"

    def __str__(self):
        return self.titulo

    def lista_de_passos(self) -> list[str]:
        return separar_linhas(self.passos)


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
    resolucao = models.TextField("resolução", blank=True, help_text=UM_POR_LINHA)

    class Meta:
        verbose_name = "exercício"
        verbose_name_plural = "exercícios"

    def __str__(self):
        return self.enunciado

    def verificar_resposta(self, resposta: str) -> bool:
        """Diz se a resposta do aluno está correta (RF005)."""
        return normalizar_resposta(resposta) == normalizar_resposta(
            self.resposta_correta
        )

    def identificar_erro(self, resposta: str) -> ErroComum | None:
        """Procura o erro comum que corresponde à resposta errada (RF005)."""
        return ErroComum.buscar(self, resposta)

    def passos_da_resolucao(self) -> list[str]:
        return separar_linhas(self.resolucao)


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

    def clean(self):
        """Extensão 6a do caso de uso 3: o erro não pode ser a resposta correta."""
        super().clean()
        exercicio = getattr(self, "exercicio", None)
        if exercicio is None:
            return
        if normalizar_resposta(self.resposta_errada) == normalizar_resposta(
            exercicio.resposta_correta
        ):
            mensagem = "O erro comum não pode ser igual à resposta correta."
            raise ValidationError({"resposta_errada": mensagem})

    @classmethod
    def buscar(cls, exercicio: Exercicio, resposta: str) -> ErroComum | None:
        """Devolve o erro comum do exercício que corresponde à resposta, se houver."""
        alvo = normalizar_resposta(resposta)
        for erro in exercicio.erros_comuns.all():
            if normalizar_resposta(erro.resposta_errada) == alvo:
                return erro
        return None
