# ColumbinaMath

Plataforma web de apoio à revisão e prática de matemática básica para estudantes do Ensino Médio.

## Sobre o projeto

O ColumbinaMath é um projeto desenvolvido na disciplina de Extensão I do Bacharelado em Engenharia da Computação do IFMT.

A proposta é oferecer um ambiente simples para revisão de conteúdos fundamentais de matemática, com explicações, exercícios e feedback sobre as respostas.

## Público-alvo

Estudantes do Ensino Médio que desejam revisar ou fortalecer seus conhecimentos fundamentais de matemática.

## Funcionalidades atuais

- Página inicial com acesso aos conteúdos.
- Listagem dos conteúdos em trilha de pré-requisitos.
- Explicação com exemplos resolvidos passo a passo e prova real.
- Exercícios de múltipla escolha com correção imediata e resolução explicada.
- Feedback por erro comum: cada alternativa errada explica o erro típico que leva a ela.
- Página 404 para endereços inexistentes.
- Layout responsivo com modo claro e escuro.

## Conteúdos

| Ordem | Conteúdo | Situação |
|---|---|---|
| 1 | Operações básicas | Disponível |
| 2 | Regra de sinais | Em breve |
| 3 | Ordem das operações | Em breve |
| 4 | Frações | Em breve |
| 5 | Porcentagem | Em breve |
| 6 | Potências de 10 e notação científica | Em breve |
| 7 | Juros simples e compostos | Em breve |

## Tecnologias

- React
- JavaScript
- Vite
- React Router
- Git
- GitHub

## Estrutura do projeto

```text
columbinamath/
├── docs/
│   ├── product/            # visão do produto
│   └── scrum/              # backlog e sprints
├── frontend/
│   └── src/
│       ├── components/     # partes reutilizáveis (cabeçalho, exercício)
│       ├── data/           # conteúdos, exemplos e exercícios
│       └── pages/          # páginas (início, conteúdos, exercícios, 404)
└── README.md
```

## Como rodar localmente

Pré-requisito: [Node.js](https://nodejs.org/) instalado.

```bash
cd frontend
npm install     # baixa as dependências (só na primeira vez)
npm run dev     # abre o servidor de desenvolvimento em http://localhost:5173
```

## Onde editar os conteúdos

Todos os conteúdos, exemplos e exercícios ficam em `frontend/src/data/conteudos.js`.
