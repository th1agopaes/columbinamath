# ADR 0002: Separar a camada de apresentação na pasta `frontend/`

- **Status:** Aceito
- **Data:** 2026-11-25
- **Autor:** Thiago Paes de Barros Costa

## Contexto

O ColumbinaMath usa o Django no padrão MVT (Model, View, Template), com as páginas montadas no servidor ([ADR 0001](0001-troca-de-stack-para-django.md)). Os templates e o CSS ficavam espalhados dentro de `backend/`: o layout base em `backend/templates/`, as páginas de cada app em `backend/<app>/templates/` e o CSS em `backend/static/`.

Nessa organização, a camada de apresentação não aparece na estrutura do repositório. Na avaliação de Engenharia de Software, foi perguntado onde estava o front-end do projeto.

## Decisão

Toda a camada de apresentação fica na pasta `frontend/`, na raiz do repositório:

- `frontend/templates/`: o layout base e as páginas de cada app, em uma subpasta por app.
- `frontend/static/`: CSS e demais arquivos estáticos.

O `backend/config/settings.py` aponta o `TEMPLATES["DIRS"]` e o `STATICFILES_DIRS` para essas pastas. A renderização continua no servidor: o Django recebe a requisição, consulta os modelos e devolve o HTML pronto ao navegador.

## Alternativas consideradas

- **Manter os templates dentro de cada app (padrão do Django).**
  Descartada: é a convenção do framework, mas esconde a camada de apresentação, que é avaliada separadamente.
- **Criar um front-end separado (React ou similar) consumindo uma API.**
  Descartada: exigiria duas stacks e duas bases de código, o problema que motivou o ADR 0001, e não cabe no prazo da entrega final.

## Consequências

### Positivas

- A separação entre apresentação (`frontend/`) e regras de negócio e dados (`backend/`) fica visível na raiz do repositório.
- Quem trabalha só na interface encontra todos os arquivos em um lugar.
- Nenhuma mudança de arquitetura, de rotas ou de comportamento.

### Negativas

- Foge da convenção de templates por app, e quem conhece Django precisa ler este ADR para saber onde estão as páginas.
- O `backend/` depende de uma pasta irmã: a imagem de container precisa copiar as duas.
