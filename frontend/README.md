# Front-end do ColumbinaMath

Camada de apresentação da aplicação: o que o estudante vê no navegador.

As páginas são renderizadas no servidor pelo Django (*server-side rendering*): a cada requisição, o Django preenche os templates com os dados e devolve o HTML pronto. Não há uma aplicação JavaScript separada. A decisão está no [ADR 0002](../docs/arquitetura/adr/0002-camada-de-apresentacao-na-pasta-frontend.md).

## Estrutura

```text
frontend/
├── templates/
│   ├── base.html       # layout comum: cabeçalho, navegação e rodapé
│   └── conteudos/      # trilha, explicação e exercício
└── static/
    └── css/
        └── estilo.css  # estilo próprio, com modo claro e escuro
```

Cada app do Django tem a sua subpasta em `templates/`, com o mesmo nome do app.

## Tecnologias

- HTML com a linguagem de templates do Django.
- CSS próprio, sem framework, com variáveis para o modo claro e o modo escuro.
- Layout responsivo, para computador e celular (RNF004).
