from django.conf import settings
from django.db import models

from conteudos.models import ErroComum, Exercicio


class Tentativa(models.Model):
    """Registro de cada resposta do aluno (RF005); é a base do progresso (RF006)."""

    aluno = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tentativas",
        verbose_name="aluno",
    )
    exercicio = models.ForeignKey(
        Exercicio,
        on_delete=models.CASCADE,
        related_name="tentativas",
        verbose_name="exercício",
    )
    # Opcional (0..1): só as respostas erradas previstas têm erro comum.
    erro_comum = models.ForeignKey(
        ErroComum,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tentativas",
        verbose_name="erro comum",
    )
    resposta_dada = models.CharField("resposta dada", max_length=50)
    correta = models.BooleanField("correta")
    data_hora = models.DateTimeField("data e hora", auto_now_add=True)

    class Meta:
        ordering = ["-data_hora"]
        verbose_name = "tentativa"
        verbose_name_plural = "tentativas"

    def __str__(self):
        resultado = "acerto" if self.correta else "erro"
        return f"{self.aluno} · {self.exercicio} · {resultado}"

    @classmethod
    def registrar(cls, aluno, exercicio: Exercicio, resposta: str) -> Tentativa:
        """Corrige a resposta e grava a tentativa, com o erro comum quando houver."""
        correta = exercicio.verificar_resposta(resposta)
        return cls.objects.create(
            aluno=aluno,
            exercicio=exercicio,
            resposta_dada=resposta,
            correta=correta,
            erro_comum=None if correta else exercicio.identificar_erro(resposta),
        )

    @classmethod
    def filtrar(cls, aluno, conteudo=None) -> models.QuerySet:
        """Tentativas de um aluno, opcionalmente só de um conteúdo."""
        tentativas = cls.objects.filter(aluno=aluno)
        if conteudo is not None:
            tentativas = tentativas.filter(exercicio__conteudo=conteudo)
        return tentativas
