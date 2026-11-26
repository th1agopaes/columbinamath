from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class TipoUsuario(models.TextChoices):
    """Perfis de acesso (enumeração TipoUsuario do diagrama de classes)."""

    ALUNO = "aluno", "Aluno"
    PROFESSOR = "professor", "Professor"
    ADMIN = "administrador", "Administrador"


class UsuarioManager(UserManager):
    """Gerenciador de usuários com login por e-mail, sem diferenciar maiúsculas."""

    def get_by_natural_key(self, username):
        # O Django chama este método no login, passando o valor do USERNAME_FIELD.
        return self.get(**{f"{self.model.USERNAME_FIELD}__iexact": username})


class Usuario(AbstractUser):
    """Usuário do ColumbinaMath.

    Herda de AbstractUser os dados de acesso (nome, e-mail, senha com hash e situação) e acrescenta o tipo de perfil.
    O login é feito pelo e-mail, como no método autenticar(email, senha) do diagrama de classes.
    """

    email = models.EmailField("endereço de e-mail", unique=True)
    tipo = models.CharField(
        "tipo",
        max_length=20,
        choices=TipoUsuario.choices,
        default=TipoUsuario.ALUNO,
    )

    objects = UsuarioManager()

    # O e-mail identifica o usuário no login; o username continua existindo
    # porque o AbstractUser e o painel administrativo dependem dele.
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "usuário"
        verbose_name_plural = "usuários"

    def __str__(self):
        return self.get_full_name() or self.email

    def desativar(self):
        """Desativa a conta sem apagar o histórico (RF001)."""
        self.is_active = False
        self.save(update_fields=["is_active"])
