from django import forms

from .models import TAMANHO_DO_CODIGO


class CriarTurmaForm(forms.Form):
    nome = forms.CharField(label="Nome da turma", max_length=100)


class EntrarTurmaForm(forms.Form):
    codigo_acesso = forms.CharField(
        label="Código de acesso",
        min_length=TAMANHO_DO_CODIGO,
        max_length=TAMANHO_DO_CODIGO,
        widget=forms.TextInput(attrs={"autocomplete": "off", "spellcheck": "false"}),
    )
