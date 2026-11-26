from django.urls import reverse
from pytest_django.asserts import assertContains, assertRedirects

from conftest import SENHA

from .forms import CadastroForm
from .models import TipoUsuario, Usuario


def dados_cadastro(**extras):
    dados = {
        "first_name": "Bruno",
        "email": "bruno@exemplo.com",
        "password1": SENHA,
        "password2": SENHA,
    }
    dados.update(extras)
    return dados


class TestCadastro:
    def test_pede_so_nome_email_e_senha(self):
        """RNF003: nenhum outro dado pessoal é pedido."""
        campos = set(CadastroForm().fields)
        assert campos == {"first_name", "email", "password1", "password2"}

    def test_cria_aluno_e_ja_entra(self, client, db):
        resposta = client.post(reverse("usuarios:cadastro"), dados_cadastro())
        assertRedirects(resposta, reverse("conteudos:lista"))
        usuario = Usuario.objects.get(email="bruno@exemplo.com")
        assert usuario.tipo == TipoUsuario.ALUNO
        assert int(client.session["_auth_user_id"]) == usuario.pk

    def test_guarda_a_senha_so_com_hash(self, client, db):
        """RNF002: a senha nunca fica em texto puro."""
        client.post(reverse("usuarios:cadastro"), dados_cadastro())
        usuario = Usuario.objects.get(email="bruno@exemplo.com")
        assert usuario.password != SENHA
        assert usuario.check_password(SENHA)

    def test_recusa_email_repetido_mesmo_com_maiusculas(self, client, aluno):
        resposta = client.post(
            reverse("usuarios:cadastro"), dados_cadastro(email="ANA@exemplo.com")
        )
        assertContains(resposta, "Já existe uma conta com este e-mail.")
        assert Usuario.objects.count() == 1

    def test_volta_para_a_pagina_pedida(self, client, db):
        destino = reverse("conteudos:lista") + "?origem=cadastro"
        resposta = client.post(
            reverse("usuarios:cadastro"), dados_cadastro(next=destino)
        )
        assertRedirects(resposta, destino)

    def test_ignora_destino_de_outro_site(self, client, db):
        resposta = client.post(
            reverse("usuarios:cadastro"),
            dados_cadastro(next="https://site-malicioso.com/"),
        )
        assertRedirects(resposta, reverse("conteudos:lista"))

    def test_quem_ja_entrou_volta_para_a_trilha(self, client, aluno):
        client.force_login(aluno)
        resposta = client.get(reverse("usuarios:cadastro"))
        assertRedirects(resposta, reverse("conteudos:lista"))


class TestEntrarESair:
    def test_entra_com_email_sem_diferenciar_maiusculas(self, client, aluno):
        resposta = client.post(
            reverse("usuarios:entrar"),
            {"username": "Ana@Exemplo.com", "password": SENHA},
        )
        assertRedirects(resposta, reverse("conteudos:lista"))

    def test_senha_errada_nao_diz_qual_campo_errou(self, client, aluno):
        resposta = client.post(
            reverse("usuarios:entrar"),
            {"username": "ana@exemplo.com", "password": "senha-errada"},
        )
        assert resposta.status_code == 200
        assert "_auth_user_id" not in client.session
        assertContains(resposta, "E-mail ou senha incorretos.")

    def test_navegacao_mostra_quem_esta_conectado(self, client, aluno):
        client.force_login(aluno)
        resposta = client.get(reverse("conteudos:lista"))
        assertContains(resposta, "Olá, Ana")
        assertContains(resposta, "Sair")

    def test_navegacao_oferece_entrar_e_criar_conta(self, client, db):
        resposta = client.get(reverse("conteudos:lista"))
        assertContains(resposta, "Entrar")
        assertContains(resposta, "Criar conta")

    def test_sair_encerra_a_sessao(self, client, aluno):
        client.force_login(aluno)
        resposta = client.post(reverse("usuarios:sair"))
        assertRedirects(resposta, reverse("conteudos:lista"))
        assert "_auth_user_id" not in client.session


class TestUsuario:
    def test_desativar_impede_o_login(self, client, aluno):
        aluno.desativar()
        assert client.login(email="ana@exemplo.com", password=SENHA) is False

    def test_texto_do_usuario_e_o_nome(self, aluno):
        assert str(aluno) == "Ana"
