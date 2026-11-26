from django.urls import path

from . import views

app_name = "turmas"

urlpatterns = [
    path("turmas/", views.lista_turmas, name="lista"),
    path("turmas/nova/", views.criar_turma, name="criar"),
    path("turmas/entrar/", views.entrar_turma, name="entrar"),
]
