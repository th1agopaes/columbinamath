import secrets

from django.conf import settings
from django.db import models

from usuarios.models import TipoUsuario

# Sem letras e números que se confundem (O e 0, I e 1), para o código ser ditado em sala.
ALFABETO_DO_CODIGO = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
TAMANHO_DO_CODIGO = 6


class Turma(models.Model):
    """Grupo de alunos de um professor, com código de acesso (RF007)."""

    nome = models.CharField("nome", max_length=100)
    codigo_acesso = models.CharField(
        "código de acesso",
        max_length=TAMANHO_DO_CODIGO,
        unique=True,
        editable=False,
    )
    professor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="turmas_criadas",
        limit_choices_to={"tipo": TipoUsuario.PROFESSOR},
        verbose_name="professor",
    )
    alunos = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="turmas",
        blank=True,
        limit_choices_to={"tipo": TipoUsuario.ALUNO},
        verbose_name="alunos",
    )
    data_criacao = models.DateTimeField("data de criação", auto_now_add=True)

    class Meta:
        ordering = ["-data_criacao"]
        verbose_name = "turma"
        verbose_name_plural = "turmas"

    def __str__(self):
        return f"{self.nome} ({self.codigo_acesso})"

    def save(self, *args, **kwargs):
        if not self.codigo_acesso:
            self.codigo_acesso = self.gerar_codigo_acesso()
        super().save(*args, **kwargs)

    @staticmethod
    def gerar_codigo_acesso() -> str:
        """Gera um código aleatório que ainda não pertence a nenhuma turma."""
        while True:
            codigo = "".join(
                secrets.choice(ALFABETO_DO_CODIGO) for _ in range(TAMANHO_DO_CODIGO)
            )
            if not Turma.objects.filter(codigo_acesso=codigo).exists():
                return codigo

    def adicionar_aluno(self, aluno) -> None:
        self.alunos.add(aluno)

    def possui_aluno(self, aluno) -> bool:
        return self.alunos.filter(pk=aluno.pk).exists()
