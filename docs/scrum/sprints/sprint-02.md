# Sprint 02 - ColumbinaMath

## Datas

- Início: 10/10/2026.
- Sprint Review: 09/11/2026.

## Contexto

A Sprint 1 foi desenvolvida no repositório [columbinamath-v1](https://github.com/th1agopaes/columbinamath-v1), com React e JavaScript. Nesta sprint, o projeto passa a usar um novo repositório, organizado com práticas de engenharia de software: TypeScript, documentação em `docs/`, issues, Pull Requests e quadro no GitHub Projects.

Ação da retrospectiva da Sprint 1 aplicada: o planejamento da Sprint 2 foi realizado antes do início da implementação.

## Meta da Sprint

Disponibilizar online, na nova arquitetura, a trilha inicial de matemática básíca com Operações básicas, Regra de sinais e Ordem das operações, mantendo o feedback por erro comum e a documentação do produto atualizada.

## Itens selecionados

| Ordem | Issue | Item | MoSCoW | Estimativa |
|---|---|---|---|---|
| 1 | #3 | Planejar a Sprint 2 | Must | 1 SP |
| 2 | #4 | Migrar e atualizar a visão do produto | Must | 1 SP |
| 3 | #5 | Migrar e atualizar o product backlog | Must | 2 SP |
| 4 | #6 | Migrar percurso de Operações básicas para TypeScript | Must | 5 SP |
| 5 | #7 | Publicar automaticamente no GitHub Pages | Must | 2 SP |
| 6 | #8 | US04 - Regra de sinais | Must | 5 SP |
| 7 | #9 | US05 - Ordem das operações | Should | 5 SP |
| 8 | #10 | US06 - Notação matemática nas expressões | Could | 3 SP |

**Total:** 24 SP.

## Recorte de conteúdo

- Regra de sinais: adição, subtração, multiplicação e divisão com números inteiros; divisões exatas; um exemplo e um exercício por operação.
- Ordem das operações: parênteses, multiplicação e divisão, adição e subtração; operações de mesma prioridade da esquerda para a direita.
- Potências ficam fora desta sprint, pois têm conteúdo próprio na trilha.

## Sprint Backlog

### #4 - Visão do produto
- [ ] Migrar a visão do v1 para `docs/produto/visao.md`.
- [ ] Atualizar categoria e benefícios com a trilha atual.
- [ ] Adicionar link para o repositório da Sprint 1.

### #5 - Product Backlog
- [ ] Migrar US01 a US03 como concluídas.
- [ ] Adicionar US04 a US06 com critérios de aceitação.
- [ ] Revisar MoSCoW, ordem e estimativas.

### #6 - Migração para TypeScript
- [ ] Remover arquivos do template do Vite.
- [ ] Definir os tipos de conteúdo, exemplo, exercício e alternativa.
- [ ] Migrar os dados (`conteudos.ts)`.
- [ ] Migrar componentes e páginas, com React Router.
- [ ] Migrar identidade visual (modo claro e escuro).
- [ ] Verificar o mesmo comportamento do v1.

### #7 - Deploy
- [ ] Criar o workflow de verificação e publicação no GitHub Actions.
- [ ] Configurar o GitHub Pages e o fallback de rotas.
- [ ] Adicionar o link do site no README.

### #8 - US04 Regra de sinais
- [ ] Preparar a explicação e conferir os exemplos resolvidos.
- [ ] Elaborar os exercícios com alternativas baseadas em erros comuns.
- [ ] Conferir a correção matemática de exemplos, alternativas e resoluções.
- [ ] Disponibilizar o conteúdo na trilha.

### #9 - US05 Ordem das operações
- [ ] Preparar a explicação e conferir os exemplos resolvidos.
- [ ] Elaborar os exercícios com alternativas baseadas em erros comuns.
- [ ] Conferir a correção matemática de exemplos, alternativas e resoluções.
- [ ] Disponibilizar o conteúdo na trilha.

### #10 - US06 Notação matemática
- [ ] Adicionar a biblioteca de renderização de fórmulas (KaTeX).
- [ ] Criar componente de expressão com exibição do texto original em caso de erro.
- [ ] Aplicar a notação nos conteúdos disponíveis.
- [ ] Verificar legibilidade em celular, computador e nos modos claro e escuro.

## Definition of Done

Um item será considerado "Pronto" quando:

- Atender aos critérios de aceitação da issue.
- Passar no lint e no build, localmente e no GitHub Actions.
- Tiver sido testado manualmente em computador e celular.
- Estiver integrado à `main` por Pull Requst vinculado à issue.
- Tiver a documentação relacionada atualizada.

## Riscos

- A capacidade planejada (24 SP) é maior que a entregue na Sprint 1 (10 SP)
- Plano de contingência: se o prazo apertar, US06 (Could) e depois US05 (Should) voltam para o Product Backlog, sem comprometer a Meta da Sprint.
