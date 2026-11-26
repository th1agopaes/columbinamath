from django.urls import path

from . import views

app_name = "progresso"

urlpatterns = [
    path("progresso/", views.meu_progresso, name="meu"),
]
