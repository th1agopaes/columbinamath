from rest_framework import serializers

from conteudos.models import Conteudo, Exercicio


class ExercicioResumoSerializer(serializers.ModelSerializer):
    """Exercício dentro do conteúdo: só o necessário para listar."""

    class Meta:
        model = Exercicio
        fields = ["id", "enunciado", "nivel"]


class ConteudoSerializer(serializers.ModelSerializer):
    total_exercicios = serializers.IntegerField(read_only=True)

    class Meta:
        model = Conteudo
        fields = ["slug", "nome", "descricao", "ordem", "total_exercicios"]


class ConteudoDetalheSerializer(serializers.ModelSerializer):
    exercicios = serializers.SerializerMethodField()

    class Meta:
        model = Conteudo
        fields = ["slug", "nome", "descricao", "ordem", "introducao", "exercicios"]

    def get_exercicios(self, conteudo) -> list[dict]:
        exercicios = conteudo.exercicios.order_by("pk")
        return ExercicioResumoSerializer(exercicios, many=True).data


class ExercicioSerializer(serializers.ModelSerializer):
    """Exercício com as alternativas, sem dizer qual é a correta.

    As alternativas são as mesmas da página do exercício: a resposta correta e
    os erros comuns, em ordem alfabética. A correção continua no servidor.
    """

    conteudo = serializers.SlugRelatedField(slug_field="slug", read_only=True)
    alternativas = serializers.SerializerMethodField()

    class Meta:
        model = Exercicio
        fields = ["id", "conteudo", "enunciado", "nivel", "alternativas"]

    def get_alternativas(self, exercicio) -> list[str]:
        return exercicio.alternativas()
