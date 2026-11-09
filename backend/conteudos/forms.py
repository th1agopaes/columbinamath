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
        alternativas = [exercicio.resposta_correta]
        alternativas += [erro.resposta_errada for erro in exercicio.erros_comuns.all()]
        # Ordem fixa e alfabética: a posição não entrega qual é a correta.
        self.fields["resposta"].choices = [(a, a) for a in sorted(alternativas)]
