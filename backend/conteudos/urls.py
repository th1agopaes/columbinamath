from django.urls import path

from . import views

app_name = "conteudos"

urlpatterns = [
    path("", views.lista_conteudos, name="lista"),
    path("conteudos/<slug:slug>/", views.detalhe_conteudo, name="detalhe"),
    path(
        "conteudos/<slug:slug>/exercicios/<int:pk>/",
        views.resolver_exercicio,
        name="exercicio",
    ),
]
