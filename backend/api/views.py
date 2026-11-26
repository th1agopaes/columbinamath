from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from conteudos.models import Conteudo, Exercicio

from .serializers import (
    ConteudoDetalheSerializer,
    ConteudoSerializer,
    ExercicioSerializer,
)


class ConteudoViewSet(viewsets.ReadOnlyModelViewSet):
    """Trilha de conteúdos (RF010): GET /api/conteudos/ e /api/conteudos/<slug>/."""

    permission_classes = [AllowAny]
    lookup_field = "slug"

    def get_queryset(self):
        return Conteudo.listar()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ConteudoDetalheSerializer
        return ConteudoSerializer


class ExercicioViewSet(viewsets.ReadOnlyModelViewSet):
    """Exercícios com as alternativas, sem a resposta correta (RF010)."""

    permission_classes = [AllowAny]
    serializer_class = ExercicioSerializer

    def get_queryset(self):
        queryset = Exercicio.objects.select_related("conteudo").prefetch_related(
            "erros_comuns"
        )
        conteudo = self.request.query_params.get("conteudo")
        if conteudo:
            queryset = queryset.filter(conteudo__slug=conteudo)
        return queryset.order_by("conteudo__ordem", "pk")
