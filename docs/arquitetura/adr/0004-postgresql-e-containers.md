# ADR 0004: Executar em containers, com PostgreSQL, Gunicorn e WhiteNoise

- **Status:** Aceito
- **Data:** 2026-11-26
- **Autor:** Thiago Paes de Barros Costa

## Contexto

Até a Sprint 3, o ColumbinaMath rodava só com o servidor de desenvolvimento do Django (`runserver`) e o SQLite. O conteúdo de Programação Web inclui containers e banco de dados, e a apresentação de Engenharia de Software pede a forma de build e execução. O professor também precisa executar o projeto ao clonar o repositório, sem instalar Python nem um banco de dados.

## Decisão

- **Containers:** a aplicação e o banco rodam em dois containers, descritos no `docker-compose.yml` e iniciados pelo `build.sh`. O script usa o Podman e, na falta dele, o Docker. As imagens usam nomes completos (`docker.io/library/...`), que o Podman exige.
- **Banco de dados:** PostgreSQL 18 no container `db`, com os dados em um volume. O SQLite continua no desenvolvimento local: o Django usa o PostgreSQL só quando a variável `POSTGRES_HOST` está definida, e o compose a define apenas para o container da aplicação.
- **Servidor de aplicação:** Gunicorn, no lugar do `runserver`, que não é feito para produção.
- **Arquivos estáticos:** WhiteNoise, que serve o CSS direto do Gunicorn, sem um servidor web na frente.
- **Imagem:** `python:3.14-slim` com o uv, dependências instaladas pelo `uv.lock` sem as de desenvolvimento, `collectstatic` no build e um usuário sem privilégios de administrador. As migrações rodam ao iniciar o container (`entrypoint.sh`).

## Alternativas consideradas

- **Só SQLite também no container.**
  Descartada: o SQLite é um arquivo local, pouco adequado a vários processos do Gunicorn, e o PostgreSQL é o banco relacional usado no mercado com o Django.
- **Nginx na frente do Gunicorn para os estáticos.**
  Descartada: seria um terceiro container para servir um único arquivo CSS. O WhiteNoise resolve dentro da aplicação.
- **Kubernetes.**
  Descartada: um compose com dois serviços atende à demonstração e à avaliação, sem a complexidade de um cluster.

## Consequências

### Positivas

- O projeto roda com um comando (`./build.sh`), igual em qualquer máquina com Podman ou Docker.
- O mesmo código roda com SQLite no desenvolvimento e com PostgreSQL no container, e os testes passam nos dois bancos.

### Negativas

- O container do banco recebe o mesmo `backend/.env` da aplicação, inclusive variáveis que não usa.
- O build depende do acesso ao Docker Hub e ao GitHub Container Registry para baixar as imagens base.
