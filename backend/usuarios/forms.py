from django import forms
from django.contrib.auth.forms import AuthenticationForm, BaseUserCreationForm

from .models import TipoUsuario, Usuario


class CadastroForm(BaseUserCreationForm):
    """Cadastro de estudante: só nome, e-mail e senha (RNF003, LGPD)."""

    class Meta:
        model = Usuario
        fields = ("first_name", "email")
        labels = {"first_name": "Nome", "email": "E-mail"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].required = True

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if Usuario.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Já existe uma conta com este e-mail.")
        return email

    def save(self, commit=True):
        usuario = super().save(commit=False)
        # O username é obrigatório no AbstractUser; usamos o próprio e-mail.
        usuario.username = usuario.email
        usuario.tipo = TipoUsuario.ALUNO
        if commit:
            usuario.save()
        return usuario


class EntrarForm(AuthenticationForm):
    """Login por e-mail e senha."""

    # A mensagem não diz qual dos dois campos está errado (US07).
    error_messages = {
        **AuthenticationForm.error_messages,
        "invalid_login": "E-mail ou senha incorretos. Confira e tente de novo.",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "E-mail"
        self.fields["username"].widget = forms.EmailInput(
            attrs={"autofocus": True, "autocomplete": "email"}
        )
