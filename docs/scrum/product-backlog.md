# Product Backlog - ColumbinaMath

## Organização e priorização

Este backlog descreve a evolução do ColumbinaMath.

A classificação MoSCoW considera como referência a primeira versão que permita estudar um conteúdo e praticá-lo com correção explicada.

- **Must have:** indispensável para essa versão.
- **Should have:** importante, mas pode ser adiado sem inviabilizar a versão.
- **Could have:** desejável, caso haja capacidade.
- **Won’t have this time:** fora dessa versão.
- **Ordem:** sequência de prioridade dos itens pendentes; pode ser revista.
- **Story Points:** estimativa relativa de esforço, complexidade e incerteza, utilizando 1, 2, 3, 5 e 8.
- **Status:** Não iniciado, Em andamento ou Concluído.

## Épicos

| ID | Épico | Objetivo |
|---|---|---|
| EP01 | Revisão dos fundamentos | Permitir que o estudante encontre os conteúdos e consulte explicações e exemplos. |
| EP02 | Prática com correção explicada | Permitir que o estudante aplique seus conhecimentos e consulte a resolução após responder. |
| EP03 | Acompanhamento do aprendizado | Permitir que o estudante tenha uma conta, registre suas respostas e acompanhe o próprio progresso. |

## Visão geral das histórias

| Ordem | ID | História | Épico | MoSCoW | Estimativa | Status |
|---|---|---|---|---|---|---|
| - | US01 | Visualizar conteúdos | EP01 | Must | 2 SP | Concluído |
| - | US02 | Acessar uma explicação | EP01 | Must | 3 SP | Concluído |
| - | US03 | Resolver exercícios e receber correção explicada | EP02 | Must | 5 SP | Concluído |
| - | US04 | Estudar e praticar a regra de sinais | EP01, EP02 | Must | 5 SP | Concluído |
| - | US07 | Criar conta e entrar | EP03 | Must | 5 SP | Concluído |
| - | US08 | Registrar tentativas | EP03 | Must | 3 SP | Concluído |
| - | US09 | Acompanhar o progresso | EP03 | Must | 3 SP | Concluído |
| 4 | US05 | Estudar e praticar a ordem das operações | EP01, EP02 | Should | 5 SP | Não iniciado |
| 5 | US06 | Visualizar expressões em notação matemática | EP01 | Could | 3 SP | Não iniciado |

US01, US02 e US03 foram concluídas na Sprint 1 e reimplementadas em Django na Sprint 2 ([ADR 0001](../arquitetura/adr/0001-troca-de-stack-para-django.md)). A US04 foi concluída na Sprint 2.

US07, US08 e US09 entraram no planejamento da [Sprint 3](sprints/sprint-03.md). Elas vêm dos requisitos RF001, RF005 e RF006 da modelagem do sistema e, por isso, passaram à frente da US05 na ordem.

## Itens do Product Backlog

### US01 - Visualizar conteúdos

**User Story:** Como estudante, quero visualizar os conteúdos disponíveis para identificar os assuntos que posso estudar e reforçar.

- **Épico:** EP01 — Revisão dos fundamentos
- **MoSCoW:** Must
- **Estimativa:** 2 SP
- **Status:** Concluído

**Critérios de aceitação:**
- Ao acessar a área de conteúdos, o estudante consegue visualizar os conteúdos disponíveis.
- Cada conteúdo apresenta um título que identifica o assunto abordado.
- O estudante consegue selecionar um dos conteúdos disponíveis.
- Ao selecionar um conteúdo, o estudante é direcionado para a página correspondente.

### US02 - Acessar uma explicação

**User Story:** Como estudante, quero acessar uma explicação com exemplo resolvido sobre um conteúdo para compreender seus conceitos antes de praticá-los.

- **Épico:** EP01 - Revisão dos fundamentos
- **MoSCoW:** Must
- **Estimativa:** 3 SP
- **Status:** Concluído

**Critérios de aceitação:**

- Ao acessar um conteúdo disponibilizado para estudo, o estudante visualiza seu título e a explicação correspondente.
- A explicação contém pelo menos um exemplo resolvido, com as etapas do cálculo e sua justificativa.
- O estudante consegue retornar à listagem de conteúdos.

### US03 - Resolver exercícios e receber correção explicada

**User Story:** Como estudante, quero responder a exercícios de múltipla escolha e consultar a correção explicada para verificar minha compreensão e entender a resolução.

- **Épico:** EP02 - Prática com correção explicada
- **MoSCoW:** Must
- **Estimativa:** 5 SP
- **Status:** Concluído

**Critérios de aceitação:**

- A partir da explicação de um conteúdo, o estudante consegue acessar os exercícios correspondentes.
- Cada exercício apresenta um enunciado e alternativas com exatamente uma resposta correta.
- O estudante consegue selecionar somente uma alternativa por exercício e enviar sua resposta.
- Se tentar enviar sem selecionar uma alternativa, recebe uma orientação para selecionar uma resposta, sem que isso seja considerado um erro matemático.
- Após o envio, o sistema informa imediatamente se a resposta está correta ou incorreta.
- Tanto no acerto quanto no erro, o sistema apresenta a alternativa correta e uma resolução explicada.
- O estudante consegue retornar à explicação do conteúdo.

### US04 - Estudar e praticar a regra de sinais

**User Story:** Como estudante, quero estudar e praticar a regra de sinais para fazer contas com números negativos sem errar o sinal do resultado.

- **Épico:** EP01 - Revisão dos fundamentos e EP02 - Prática com correção explicada
- **MoSCoW:** Must
- **Estimativa:** 5 SP
- **Status:** Concluído

**Critérios de aceitação:**

- O conteúdo Regra de sinais está disponível na trilha, logo depois de Operações básicas.
- A explicação apresenta a regra para adição, subtração, multiplicação e divisão de números inteiros, com um exemplo resolvido por operação.
- Há um exercício de múltipla escolha por operação, com divisões exatas.
- Cada alternativa errada corresponde a um erro comum e, quando escolhida, exibe a explicação desse erro.
- Após o envio, o sistema apresenta a alternativa correta e a resolução explicada.

### US05 - Estudar e praticar a ordem das operações

**User Story:** Como estudante, quero estudar e praticar a ordem das operações para resolver expressões numéricas na sequência correta.

- **Épico:** EP01 - Revisão dos fundamentos e EP02 - Prática com correção explicada
- **MoSCoW:** Should
- **Estimativa:** 5 SP
- **Status:** Não iniciado

**Critérios de aceitação:**

- O conteúdo Ordem das operações está disponível na trilha, logo depois de Regra de sinais.
- A explicação aborda parênteses, multiplicação e divisão, adição e subtração, e a resolução da esquerda para a direita entre operações de mesma prioridade, com exemplos resolvidos.
- Potências ficam fora deste conteúdo, pois têm conteúdo próprio na trilha.
- Os exercícios seguem o padrão da US03: múltipla escolha, feedback por erro comum e resolução explicada.

### US06 - Visualizar expressões em notação matemática

**User Story:** Como estudante, quero ver as expressões escritas em notação matemática para lê-las como no caderno e nos livros.

- **Épico:** EP01 - Revisão dos fundamentos
- **MoSCoW:** Could
- **Estimativa:** 3 SP
- **Status:** Não iniciado

**Critérios de aceitação:**

- As expressões dos conteúdos disponíveis são exibidas em notação matemática.
- Se a notação não puder ser exibida, o texto original da expressão continua visível.
- A leitura funciona em computador e celular, nos modos claro e escuro.

### US07 - Criar conta e entrar

**User Story:** Como estudante, quero criar uma conta e entrar no ColumbinaMath para que minhas respostas fiquem guardadas no meu nome.

- **Épico:** EP03 - Acompanhamento do aprendizado
- **Requisitos:** RF001, RNF002 e RNF003
- **MoSCoW:** Must
- **Estimativa:** 5 SP
- **Status:** Concluído

**Critérios de aceitação:**

- O estudante cria uma conta informando nome, e-mail e senha; nenhum outro dado pessoal é pedido.
- Não é possível criar duas contas com o mesmo e-mail.
- A senha é guardada apenas com hash, nunca em texto puro.
- O estudante entra com e-mail e senha e consegue sair.
- Com e-mail ou senha incorretos, o sistema avisa do erro sem dizer qual dos dois está errado.
- A navegação mostra se o estudante está conectado.

### US08 - Registrar tentativas

**User Story:** Como estudante, quero que cada resposta que eu enviar fique registrada para acompanhar depois o que acertei e o que errei.

- **Épico:** EP03 - Acompanhamento do aprendizado
- **Requisitos:** RF005
- **MoSCoW:** Must
- **Estimativa:** 3 SP
- **Status:** Concluído

**Critérios de aceitação:**

- Para responder a um exercício, o estudante precisa estar conectado; a explicação do conteúdo continua aberta a todos.
- Cada resposta enviada gera uma tentativa com o estudante, o exercício, a resposta, o resultado e a data e hora.
- Quando a resposta errada corresponde a um erro comum, ele fica associado à tentativa.
- O envio sem alternativa selecionada não gera tentativa.
- O estudante pode responder ao mesmo exercício mais de uma vez, e cada resposta gera uma nova tentativa.

### US09 - Acompanhar o progresso

**User Story:** Como estudante, quero ver meus acertos e erros por conteúdo para saber onde preciso praticar mais.

- **Épico:** EP03 - Acompanhamento do aprendizado
- **Requisitos:** RF006
- **MoSCoW:** Must
- **Estimativa:** 3 SP
- **Status:** Concluído

**Critérios de aceitação:**

- A página "Meu progresso" mostra, para cada conteúdo, os acertos, os erros e o percentual de acerto.
- A página mostra os erros comuns mais frequentes do estudante.
- O progresso é calculado a partir das tentativas, sem ser armazenado.
- Quem ainda não tem tentativas recebe a orientação de resolver exercícios.
- Cada estudante vê apenas o próprio progresso.
