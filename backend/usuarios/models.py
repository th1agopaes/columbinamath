from django.contrib.auth.models import AbstractUser
from django.db import models


class TipoUsuario(models.TextChoices):
    """Perfis de acesso (enumeração TipoUsuario do diagrama de classes)."""

    ALUNO = "aluno", "Aluno"
    PROFESSOR = "professor", "Professor"
    ADMIN = "administrador", "Administrador"


class Usuario(AbstractUser):
    """Usuário do ColumbinaMath.

    Herda de AbstractUser os dados de acesso (nome, e-mail, senha com hash e situação) e acrescenta o tipo de perfil.
    """

    email = models.EmailField("endereço de e-mail", unique=True)
    tipo = models.CharField(
        "tipo",
        max_length=20,
        choices=TipoUsuario.choices,
        default=TipoUsuario.ALUNO,
    )

    class Meta:
        verbose_name = "usuário"
        verbose_name_plural = "usuários"

    def __str__(self):
        return self.get_full_name() or self.username
