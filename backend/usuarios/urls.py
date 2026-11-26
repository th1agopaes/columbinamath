from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views

app_name = "usuarios"

urlpatterns = [
    path("conta/entrar/", views.EntrarView.as_view(), name="entrar"),
    path("conta/sair/", LogoutView.as_view(), name="sair"),
    path("conta/cadastro/", views.cadastrar, name="cadastro"),
]
