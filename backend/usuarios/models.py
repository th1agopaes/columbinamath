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

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        # Quem administra o sistema pelo terminal recebe o perfil de administrador.
        extra_fields.setdefault("tipo", TipoUsuario.ADMIN)
        return super().create_superuser(username, email, password, **extra_fields)


class AlunoManager(UsuarioManager):
    """Só os usuários do tipo aluno."""

    def get_queryset(self):
        return super().get_queryset().filter(tipo=TipoUsuario.ALUNO)


class ProfessorManager(UsuarioManager):
    """Só os usuários do tipo professor."""

    def get_queryset(self):
        return super().get_queryset().filter(tipo=TipoUsuario.PROFESSOR)


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


class Aluno(Usuario):
    """Perfil de aluno (subclasse do diagrama de classes).

    Modelo proxy: usa a mesma tabela do Usuario, filtrada pelo campo tipo, e
    acrescenta o comportamento do aluno. A decisão está no ADR 0003.
    """

    objects = AlunoManager()

    class Meta:
        proxy = True
        verbose_name = "aluno"
        verbose_name_plural = "alunos"

    def save(self, *args, **kwargs):
        self.tipo = TipoUsuario.ALUNO
        super().save(*args, **kwargs)

    def calcular_progresso(self) -> dict:
        """Acertos, erros e percentual por conteúdo e os erros mais frequentes (RF006)."""
        from progresso import calculos  # import local: progresso depende de usuarios

        progresso = calculos.resumir(self.tentativas.all())
        progresso["erros_frequentes"] = calculos.erros_frequentes(self.tentativas.all())
        return progresso

    def entrar_turma(self, codigo_acesso: str) -> bool:
        """Entra na turma do código informado; devolve False se o código não existe."""
        from turmas.models import Turma  # import local: turmas depende de usuarios

        codigo = codigo_acesso.strip().upper()
        turma = Turma.objects.filter(codigo_acesso=codigo).first()
        if turma is None:
            return False
        turma.adicionar_aluno(self)
        return True


class Professor(Usuario):
    """Perfil de professor (subclasse do diagrama de classes), também proxy."""

    objects = ProfessorManager()

    class Meta:
        proxy = True
        verbose_name = "professor"
        verbose_name_plural = "professores"

    def save(self, *args, **kwargs):
        self.tipo = TipoUsuario.PROFESSOR
        super().save(*args, **kwargs)

    def criar_turma(self, nome: str):
        """Cria uma turma com código de acesso gerado automaticamente (RF007)."""
        return self.turmas_criadas.create(nome=nome)
