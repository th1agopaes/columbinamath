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
- [x] Centralizar os dados dos conteúdos em um único arquivo (`src/data/conteudos.js`).
- [x] Reorganizar a listagem como trilha de pré-requisitos, com os assuntos sem material marcados como "Em breve".

### US02 - Acessar uma explicação

- [x] Preparar a explicação das quatro operações.
- [x] Elaborar e conferir um exemplo resolvido por operação.
- [x] Adicionar Operações básicas à listagem e criar sua página.
- [x] Exibir a explicação e os exemplos na página.
- [x] Permitir retornar à listagem de conteúdos.

### US03 - Resolver exercícios e receber correção explicada

- [x] Elaborar quatro exercícios de múltipla escolha, cada um com exatamente uma alternativa correta.
- [x] Preparar e conferir a resolução explicada de cada exercício.
- [x] Criar o acesso aos exercícios a partir da explicação.
- [x] Permitir selecionar uma alternativa por exercício e enviar a resposta.
- [x] Orientar o estudante quando tentar enviar sem selecionar uma alternativa, sem considerar isso um erro matemático.
- [x] Apresentar acerto ou erro, alternativa correta e resolução explicada após o envio.
- [x] Permitir retornar à explicação do conteúdo.

### Navegação e apresentação

- [x] Adicionar acesso à lista de conteúdos na página inicial.
- [x] Distinguir conteúdos disponíveis para estudo dos assuntos ainda sem material.
- [x] Verificar legibilidade e uso em telas de celular e computador.

### Verificação da entrega

- [x] Conferir os critérios de aceitação da US02 e da US03.
- [x] Testar respostas corretas, incorretas e envios sem alternativa selecionada.
- [x] Verificar o percurso completo de navegação e os caminhos de volta.
- [x] Conferir a correção matemática dos exemplos, alternativas e resoluções.
- [x] Verificar o tratamento de identificador de conteúdo inexistente.
- [x] Executar as verificações de lint e build e corrigir problemas encontrados.
- [x] Versionar as alterações e disponibilizá-las no GitHub.
- [x] Atualizar os itens concluídos e o roteiro da demonstração conforme o resultado real.

### Melhorias técnicas incluídas

- [x] Remover arquivos e estilos que sobraram do template do Vite.
- [x] Adicionar cabeçalho de navegação em todas as páginas.
- [x] Adicionar página 404 para endereços inexistentes.
- [x] Ajustar título e idioma da página (`pt-BR`).
- [x] Aplicar identidade visual com suporte a modo claro e escuro.

## Definition of Done

Um item será considerado "Pronto" quando:

- Atender aos critérios de aceitação da User Story.
- Estiver funcionando sem erros conhecidos que impeçam seu uso principal.
- A navegação relacionada à funcionalidade tiver sido testada manualmente.
- O código estiver versionado no Git.
- O código estiver disponível no repositório do GitHub.

## Incremento produzido

Primeira versão utilizável do ColumbinaMath, com um percurso completo de estudo em **Operações básicas**:

- Página inicial com explicação do funcionamento e acesso aos conteúdos.
- Listagem dos conteúdos organizada como trilha de pré-requisitos (1 disponível e 6 "Em breve").
- Explicação das quatro operações, com vocabulário, um exemplo resolvido passo a passo por operação e prova real.
- Quatro exercícios de múltipla escolha, um por operação.
- Correção imediata, com alternativa correta e resolução explicada.
- **Feedback por erro comum:** cada alternativa errada corresponde a um erro típico (por exemplo, esquecer o "vai um" ou o zero no quociente) e o feedback explica aquele erro específico.
- Orientação ao tentar enviar sem selecionar alternativa.
- Caminhos de volta entre exercícios, explicação e listagem.
- Página 404 para conteúdos e endereços inexistentes.
- Layout responsivo (celular e computador) com modo claro e escuro.

## Itens concluídos

- US01 - Visualizar conteúdos.
- US02 - Acessar uma explicação.
- US03 - Resolver exercícios e receber correção explicada.

## Mudanças em relação ao planejamento

- Os assuntos Porcentagem, Juros e Notação científica foram mantidos, mas agora aparecem como "Em breve" no fim da trilha, porque dependem de operações básicas, sinais, ordem das operações e frações.
- Foi incluído o feedback por erro comum, como hipótese de diferencial do produto a ser validada com estudantes.

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

Todas as etapas do roteiro foram concluídas e verificadas manualmente no computador e no celular.

### Próximos passos propostos (entrada para a Sprint 2)

- Publicar a aplicação (deploy) para acesso por link.
- Criar os conteúdos de Regra de sinais e Ordem das operações.
- Exibir fórmulas com KaTeX.
- Conversar com estudantes do Ensino Médio para validar dificuldades e o feedback por erro comum.

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