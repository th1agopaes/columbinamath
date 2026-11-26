from django.urls import path

from . import views

app_name = "turmas"

urlpatterns = [
    path("turmas/", views.lista_turmas, name="lista"),
    path("turmas/nova/", views.criar_turma, name="criar"),
    path("turmas/entrar/", views.entrar_turma, name="entrar"),
    path("turmas/<int:pk>/", views.detalhe_turma, name="detalhe"),
    path(
        "turmas/<int:pk>/alunos/<int:aluno_pk>/",
        views.progresso_do_aluno,
        name="aluno",
    ),
]
