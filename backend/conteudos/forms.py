from django import forms


class RespostaForm(forms.Form):
    """Alternativas do exercício: a resposta correta e os erros comuns."""

    resposta = forms.ChoiceField(
        label="Escolha a sua resposta",
        widget=forms.RadioSelect,
        error_messages={"required": "Selecione uma alternativa antes de enviar."},
    )

    def __init__(self, *args, exercicio, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["resposta"].choices = [(a, a) for a in exercicio.alternativas()]
