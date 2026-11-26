from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = "api"

roteador = DefaultRouter()
roteador.register("conteudos", views.ConteudoViewSet, basename="conteudo")
roteador.register("exercicios", views.ExercicioViewSet, basename="exercicio")

urlpatterns = [
    path("api/", include(roteador.urls)),
]
