# Sprint 01 - ColumbinaMath

## Datas

- Sprint Review: 07/10/2026.

## Situação inicial

O projeto ainda não estava estruturado. Houve uma tentativa inicial de desenvolver uma aplicação em Django, mas a ideia não foi continuada. Não havia Product Backlog, Sprint Backlog ou definição formal da Sprint.

## Meta da Sprint

Estruturar a proposta do ColumbinaMath e disponibilizar um primeiro percurso de aprendizagem sobre operações básicas, permitindo ao estudante acessar explicações e exemplos, responder a exercícios de múltipla escolha e consultar a correção explicada.

## Itens selecionados

- US01 - Visualizar conteúdos.
- US02 - Acessar uma explicação.
- US03 - Resolver exercícios e receber correção explicada.

## Recorte de conteúdo

- Adição, subtração, multiplicação e divisão com números naturais.
- Um exemplo resolvido por operação.
- Quatro exercícios de múltipla escolha, um por operação.
- Divisões exatas, com divisor diferente de zero.
- Subtrações com resultado não negativo.
- Números negativos, frações e expressões com várias operações ficam para entregas posteriores.

## Sprint Backlog

### US01 - Visualizar conteúdos

- [x] Criar a estrutura inicial da aplicação frontend.
- [x] Criar a página inicial.
- [x] Criar a área de conteúdos.
- [x] Adicionar os títulos dos assuntos iniciais:
  - Porcentagem.
  - Juros simples e compostos.
  - Potências de 10 e notação científica.
- [x] Criar as páginas iniciais com o título de cada assunto.
- [x] Implementar a navegação entre a lista de conteúdos e suas respectivas páginas.
- [x] Verificar o funcionamento dessa navegação.

### US02 - Acessar uma explicação

- [ ] Preparar a explicação das quatro operações.
- [ ] Elaborar e conferir um exemplo resolvido por operação.
- [ ] Adicionar Operações básicas à listagem e criar sua página.
- [ ] Exibir a explicação e os exemplos na página.
- [ ] Permitir retornar à listagem de conteúdos.

### US03 - Resolver exercícios e receber correção explicada

- [ ] Elaborar quatro exercícios de múltipla escolha, cada um com exatamente uma alternativa correta.
- [ ] Preparar e conferir a resolução explicada de cada exercício.
- [ ] Criar o acesso aos exercícios a partir da explicação.
- [ ] Permitir selecionar uma alternativa por exercício e enviar a resposta.
- [ ] Orientar o estudante quando tentar enviar sem selecionar uma alternativa, sem considerar isso um erro matemático.
- [ ] Apresentar acerto ou erro, alternativa correta e resolução explicada após o envio.
- [ ] Permitir retornar à explicação do conteúdo.

### Navegação e apresentação

- [ ] Adicionar acesso à lista de conteúdos na página inicial.
- [ ] Distinguir conteúdos disponíveis para estudo dos assuntos ainda sem material.
- [ ] Verificar legibilidade e uso em telas de celular e computador.

### Verificação da entrega

- [ ] Conferir os critérios de aceitação da US02 e da US03.
- [ ] Testar respostas corretas, incorretas e envios sem alternativa selecionada.
- [ ] Verificar o percurso completo de navegação e os caminhos de volta.
- [ ] Conferir a correção matemática dos exemplos, alternativas e resoluções.
- [ ] Verificar o tratamento de identificador de conteúdo inexistente.
- [ ] Executar as verificações de lint e build e corrigir problemas encontrados.
- [ ] Versionar as alterações e disponibilizá-las no GitHub.
- [ ] Atualizar os itens concluídos e o roteiro da demonstração conforme o resultado real.

## Definition of Done

Um item será considerado "Pronto" quando:

- Atender aos critérios de aceitação da User Story.
- Estiver funcionando sem erros conhecidos que impeçam seu uso principal.
- A navegação relacionada à funcionalidade tiver sido testada manualmente.
- O código estiver versionado no Git.
- O código estiver disponível no repositório do GitHub.

## Incremento produzido

Até o momento, foi produzida uma primeira versão navegável do frontend do ColumbinaMath, contendo:

- Página inicial.
- Área de conteúdos.
- Listagem dos três assuntos iniciais.
- Navegação entre a listagem e as páginas correspondentes.
- Identificação do conteúdo pela URL.
- Exibição do título de cada assunto.
- Tratamento para identificadores de conteúdo inexistentes.

As explicações, os exemplos resolvidos e os exercícios ainda não estão implementados. Esta seção será atualizada conforme as funcionalidades forem concluídas e verificadas.

## Itens concluídos

- US01 - Visualizar conteúdos.

## Itens não concluídos

- US02 - Acessar uma explicação: não iniciado.
- US03 - Resolver exercícios e receber correção explicada: não iniciado.
- As tarefas complementares pendentes estão indicadas no Sprint Backlog.

## Dificuldades encontradas

- Definição tardia do tema e do escopo do projeto.
- Ausência de planejamento formal da Sprint no início do período.
- Falta inicial de Product Backlog e Sprint Backlog.
- Pouca familiaridade com React, React Router e organização de um projeto frontend.
- Necessidade de configurar o ambiente de desenvolvimento no WSL antes de iniciar a implementação.

## Sprint Review

### Demonstração planejada

- Apresentar a página inicial e acessar a lista de conteúdos.
- Abrir o conteúdo de operações básicas.
- Consultar a explicação e os exemplos resolvidos.
- Responder a exercícios e visualizar a correção explicada.
- Demonstrar os caminhos de volta e o tratamento de conteúdo inexistente.

O roteiro será ajustado antes da Review para demonstrar somente as funcionalidades concluídas e verificadas.

## Retrospectiva

Observações registradas até o momento, a revisar ao finalizar a entrega.

### O que funcionou bem

- A definição do problema, público-alvo e objetivo tornou o projeto mais claro.
- A criação do Product Backlog ajudou a organizar as funcionalidades.
- A divisão da US01 em tarefas menores facilitou a implementação.
- O uso de Git e GitHub permitiu registrar a evolução do projeto.

### O que precisa melhorar

- Planejar a Sprint antes do início do desenvolvimento.
- Definir a Meta da Sprint e o Sprint Backlog com antecedência.
- Manter uma rotina de acompanhamento do progresso ao longo da Sprint.
- Evitar deixar decisões importantes para os últimos dias.

### Ação para a próxima Sprint

- Realizar o planejamento da Sprint 2 antes de iniciar a implementação e acompanhar as tarefas durante toda a Sprint.