# Sprint 02 - ColumbinaMath

## Datas

- Início: 10/10/2026.
- Sprint Review: 09/11/2026.

## Contexto

A Sprint 1 foi desenvolvida no repositório [columbinamath-v1](https://github.com/th1agopaes/columbinamath-v1), com React e JavaScript. Nesta sprint, o projeto passa a usar um novo repositório, organizado com práticas de engenharia de software: TypeScript, documentação em `docs/`, issues, Pull Requests e quadro no GitHub Projects.

**Mudança durante a sprint (04/11/2026):** a stack foi trocada de TypeScript/React para Python/Django, para que um único projeto atenda também às disciplinas de Engenharia de Software e Programação Web. A decisão está registrada no [ADR 0001](../../arquitetura/adr/0001-troca-de-stack-para-django.md), e as issues #6 e #7 foram reescritas para a nova stack.

Ação da retrospectiva da Sprint 1 aplicada: o planejamento da Sprint 2 foi realizado antes do início da implementação.

## Meta da Sprint

Disponibilizar online, na nova arquitetura, a trilha inicial de matemática básica com Operações básicas, Regra de sinais e Ordem das operações, mantendo o feedback por erro comum e a documentação do produto atualizada.

## Itens selecionados

| Ordem | Issue | Item | MoSCoW | Estimativa | Resultado |
|---|---|---|---|---|---|
| 1 | #3 | Planejar a Sprint 2 | Must | 1 SP | Concluído |
| 2 | #4 | Migrar e atualizar a visão do produto | Must | 1 SP | Concluído |
| 3 | #5 | Migrar e atualizar o product backlog | Must | 2 SP | Concluído |
| 4 | #6 | Migrar percurso de Operações básicas (reescrito: para Django) | Must | 5 SP | Concluído |
| 5 | #7 | Publicar automaticamente (reescrito: verificar e publicar a aplicação Django) | Must | 2 SP | Voltou ao Product Backlog |
| 6 | #8 | US04 - Regra de sinais | Must | 5 SP | Concluído |
| 7 | #9 | US05 - Ordem das operações | Should | 5 SP | Voltou ao Product Backlog |
| 8 | #10 | US06 - Notação matemática nas expressões | Could | 3 SP | Voltou ao Product Backlog |

**Total:** 24 SP.

## Recorte de conteúdo

- Regra de sinais: adição, subtração, multiplicação e divisão com números inteiros; divisões exatas; um exemplo e um exercício por operação.
- Ordem das operações: parênteses, multiplicação e divisão, adição e subtração; operações de mesma prioridade da esquerda para a direita.
- Potências ficam fora desta sprint, pois têm conteúdo próprio na trilha.

## Sprint Backlog

### #4 - Visão do produto
- [x] Migrar a visão do v1 para `docs/produto/visao.md`.
- [x] Atualizar categoria e benefícios com a trilha atual.
- [x] Adicionar link para o repositório da Sprint 1.

### #5 - Product Backlog
- [x] Migrar US01 a US03 como concluídas.
- [x] Adicionar US04 a US06 com critérios de aceitação.
- [x] Revisar MoSCoW, ordem e estimativas.

### #6 - Migração para Django

Os itens originais (TypeScript) foram substituídos pela migração para Django ([ADR 0001](../../arquitetura/adr/0001-troca-de-stack-para-django.md)).

- [x] Criar os modelos Conteudo, Exercicio e ErroComum, conforme o diagrama de classes.
- [x] Carregar no banco os conteúdos e exercícios do v1.
- [x] Implementar e testar as regras de correção: verificar a resposta e identificar o erro comum.
- [x] Criar as páginas da trilha, do conteúdo e do exercício, com correção no servidor.
- [x] Migrar a identidade visual (modo claro e escuro).
- [x] Restaurar a explicação, os exemplos e a resolução explicada do v1 (#30).

### #7 - Deploy

Voltou ao Product Backlog: o GitHub Pages só hospeda sites estáticos e não executa Django.

- [ ] Criar o workflow de verificação e publicação no GitHub Actions.
- [ ] Configurar o GitHub Pages e o fallback de rotas.
- [ ] Adicionar o link do site no README.

### #8 - US04 Regra de sinais
- [x] Preparar a explicação e conferir os exemplos resolvidos.
- [x] Elaborar os exercícios com alternativas baseadas em erros comuns.
- [x] Conferir a correção matemática de exemplos, alternativas e resoluções.
- [x] Disponibilizar o conteúdo na trilha.

### #9 - US05 Ordem das operações

Voltou ao Product Backlog (plano de contingência).

- [ ] Preparar a explicação e conferir os exemplos resolvidos.
- [ ] Elaborar os exercícios com alternativas baseadas em erros comuns.
- [ ] Conferir a correção matemática de exemplos, alternativas e resoluções.
- [ ] Disponibilizar o conteúdo na trilha.

### #10 - US06 Notação matemática

Voltou ao Product Backlog (plano de contingência).

- [ ] Adicionar a biblioteca de renderização de fórmulas (KaTeX).
- [ ] Criar componente de expressão com exibição do texto original em caso de erro.
- [ ] Aplicar a notação nos conteúdos disponíveis.
- [ ] Verificar legibilidade em celular, computador e nos modos claro e escuro.

## Definition of Done

Um item será considerado "Pronto" quando:

- Atender aos critérios de aceitação da issue.
- Passar no lint e no build, localmente e no GitHub Actions.
- Tiver sido testado manualmente em computador e celular.
- Estiver integrado à `main` por Pull Request vinculado à issue.
- Tiver a documentação relacionada atualizada.

## Riscos

- A capacidade planejada (24 SP) é maior que a entregue na Sprint 1 (10 SP)
- Plano de contingência: se o prazo apertar, US06 (Could) e depois US05 (Should) voltam para o Product Backlog, sem comprometer a Meta da Sprint.

## Itens adicionados durante a Sprint

Itens técnicos criados a partir da troca de stack, sem estimativa em Story Points:

| Issue | Item |
|---|---|
| #12 | Registrar o ADR 0001 (troca de Node/React para Django) |
| #15 | Remover o front-end React e preparar o repositório para Python |
| #17 | Criar o projeto Django com uv |
| #19 | Configurar Ruff e pre-commit |
| #22 e #24 | Criar o modelo de usuário e alinhá-lo ao diagrama de classes |
| #30 | Exibir a teoria e a resolução passo a passo (restaura a US02 e parte da US03) |

## Resultado da Sprint

**Meta:** atingida parcialmente.

- **Atingido:** a trilha na nova arquitetura, com Operações básicas e Regra de sinais, cada uma com explicação, exemplos resolvidos e exercícios com feedback por erro comum e resolução explicada; documentação do produto atualizada.
- **Não atingido:** disponibilizar a aplicação online (#7) e o conteúdo Ordem das operações (#9).

**Story Points:** 14 SP concluídos de 24 SP planejados (#3, #4, #5, #6 e #8). Na Sprint 1, foram 10 SP.

**Qualidade:** 19 testes automatizados (pytest), lint e formatação com Ruff e hooks de pre-commit (Conventional Commits, detecção de segredos e bloqueio de commits na `main`). O item da Definition of Done "no GitHub Actions" não foi cumprido nesta sprint, pois o CI depende da #7.

**Riscos que se concretizaram:**

- A capacidade planejada ficou acima da entregue, como previsto nos riscos.
- A troca de stack no meio da sprint exigiu refazer a migração e adicionou itens técnicos.
- Plano de contingência aplicado: US06 e US05 voltaram ao Product Backlog, assim como a #7.
