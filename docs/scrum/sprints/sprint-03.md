# Sprint 03 - ColumbinaMath

## Datas

- Início: 10/11/2026.
- Planejamento: 16/11/2026.
- Replanejamentos: 16/11/2026 e 25/11/2026.
- Entrega de Programação Web: 26/11/2026 (código do projeto, pelo link do repositório).
- Entrega de Engenharia de Software: 07/12/2026, pelo SUAP (vídeo da apresentação final).
- Sprint Review: 07/12/2026.

## Contexto

Esta é a última sprint do projeto. O mesmo produto é avaliado em três disciplinas, com datas próximas, e a mais cedo delas define o ritmo da sprint: 01/12 no planejamento e 26/11 depois do replanejamento de 25/11.

A Sprint 2 entregou a trilha em Django com Operações básicas e Regra de sinais, de uso anônimo. Nesta sprint, o produto passa a ter conta de estudante, registro de tentativas e progresso, conforme os requisitos RF001, RF005 e RF006 da modelagem do sistema. O projeto também recebe verificação automática, execução por container e a documentação de engenharia usada na apresentação final.

Ações da [retrospectiva da Sprint 2](sprint-02.md#retrospectiva) aplicadas neste planejamento:

- O CI no GitHub Actions é o primeiro item da sprint.
- Todos os itens têm estimativa, incluindo os técnicos e os de documentação.
- O trabalho é diário, conferido no `git log` toda sexta-feira.

## Meta da Sprint

Entregar a versão 1.0 do ColumbinaMath: o estudante cria uma conta, resolve exercícios com as tentativas registradas e acompanha o próprio progresso, em um projeto verificado automaticamente a cada mudança, executável por container e documentado para a apresentação final.

## Replanejamento de 16/11

No mesmo dia do planejamento, o escopo técnico foi revisto. O conteúdo programático de Programação Web inclui containers, banco de dados e serviços REST, e os critérios da entrega ainda não foram confirmados pelo professor. Por prudência, PostgreSQL, API REST e containers passam a ser tratados como exigidos.

A meta da sprint não muda. O que muda é o Sprint Backlog:

- A #46 (containers com PostgreSQL) passa de Should para Must.
- Entra a #55 (API REST), Must, com 3 SP. Ela é feita de 02 a 04/12, depois do vídeo de Engenharia de Software, porque só é avaliada em Programação Web.
- Os itens Must passam de 27 para 35 SP, e o total da sprint, de 37 para 40 SP.
- O plano de contingência foi refeito: PostgreSQL e containers deixam de ser cortes possíveis.

## Replanejamento de 25/11

As datas de duas entregas mudaram: Programação Web foi antecipada para 26/11 e Engenharia de Software passou para 07/12, no mesmo dia da Sprint Review. De 17 a 24/11 não houve avanço no projeto.

A entrega de Programação Web avalia o código contra a modelagem do sistema (Partes I e II), que inclui o caso de uso 4 (turmas e desempenho da turma). Por isso:

- Entram a US10 (#62) e a US11 (#63), Must, com 3 SP cada. RF007 e RF008 deixam de ser Won't.
- Entra a #61 (1 SP): a camada de apresentação passa para a pasta `frontend/`, em resposta à avaliação de Engenharia de Software ([ADR 0002](../../arquitetura/adr/0002-camada-de-apresentacao-na-pasta-frontend.md)).
- US07, US08 e US09 foram concluídas em 25/11, junto com a US10, a US11 e a #61.
- Containers com PostgreSQL (#46) e API REST (#55) continuam Must, com prazo em 07/12. Se ficarem prontas até 26/11, entram também na entrega de Programação Web.
- A meta da sprint continua a mesma, agora com o professor acompanhando as turmas.

## Capacidade

- Velocidade medida: 10 SP na Sprint 1 e 14 SP na Sprint 2.
- Os itens Must desta sprint somam 35 SP, duas vezes e meia a maior velocidade medida.
- Situação em 16/11: 4 SP concluídos (#41 e #7). Restam 28 SP até 01/12 e 3 SP (API REST) de 02 a 04/12.
- Situação em 25/11: 24 de 47 SP concluídos. Restam 18 SP Must até 07/12.
- Por que o plano foi mantido: as datas das três disciplinas são fixas; os 14 SP da Sprint 2 foram entregues em 4 dias de trabalho e não contavam os 8 itens técnicos sem estimativa; de 17 a 30/11 são 14 dias de trabalho, o que pede uma média de 2 SP por dia.
- O risco aumentou com o replanejamento. Ele é reconhecido e tratado pelos marcos e pelo plano de contingência abaixo.

## Itens selecionados

| Ordem | Issue | Item | MoSCoW | Estimativa | Resultado |
|---|---|---|---|---|---|
| 1 | #41 | Planejar a Sprint 3 e atualizar o Product Backlog | Must | 2 SP | Concluído |
| 2 | #7 | Verificar a aplicação no GitHub Actions (CI) | Must | 2 SP | Concluído |
| 3 | #42 | Registrar requisitos, casos de uso e priorização | Must | 2 SP | Concluído |
| 4 | #43 | US07 - Criar conta e entrar | Must | 5 SP | Concluído |
| 5 | #44 | US08 - Registrar tentativas | Must | 3 SP | Concluído |
| 6 | #45 | US09 - Acompanhar o progresso | Must | 3 SP | Concluído |
| 7 | #61 | Separar a camada de apresentação na pasta `frontend/` | Must | 1 SP | Concluído |
| 8 | #62 | US10 - Criar turma e entrar com código | Must | 3 SP | Concluído |
| 9 | #63 | US11 - Acompanhar o desempenho da turma | Must | 3 SP | Concluído |
| 10 | #46 | Executar a aplicação em containers com PostgreSQL | Must | 5 SP | Concluído |
| 11 | #47 | Diagramas de casos de uso, classes, arquitetura e BPD | Must | 3 SP | Concluído |
| 12 | #48 | Métricas do projeto e ADRs pendentes | Must | 2 SP | |
| 13 | #49 | Apresentação final: slides, vídeo e versão 1.0 | Must | 5 SP | |
| 14 | #55 | Expor conteúdos e exercícios por API REST | Must | 3 SP | Concluído |
| 15 | #9 | US05 - Ordem das operações | Should | 5 SP | |

**Total:** 47 SP (42 SP Must e 5 SP Should). Concluídos até 26/11: 35 SP.

## Marcos

| Data | Marco |
|---|---|
| 18/11 | Requisitos registrados em `docs/requisitos/` (cumprido em 16/11) |
| 26/11 | Entrega de Programação Web: modelagem inteira implementada (UC1 a UC4) |
| 30/11 | Containers com PostgreSQL e API REST |
| 03/12 | Diagramas, métricas e ADRs; congelamento do código (code freeze) |
| 07/12 | Vídeo entregue em Engenharia de Software e Sprint Review 3 |

## Sprint Backlog

### #7 - CI no GitHub Actions

A issue foi reescrita: fica só a verificação automática. A publicação online saiu da sprint.

- [x] Criar o workflow com os hooks do pre-commit e os testes com cobertura.
- [x] Executar o workflow nos Pull Requests e na `main`.
- [x] Adicionar o selo do CI ao README.
- [x] Configurar o Dependabot.

### #42 - Requisitos e casos de uso

- [x] Registrar os requisitos funcionais e não funcionais com a priorização MoSCoW, incluindo os itens Won't.
- [x] Registrar os casos de uso descritivos.
- [x] Montar a matriz de rastreabilidade (requisito, história, issue e teste).
- [x] Adicionar ao repositório os documentos de modelagem (Partes I e II).

### #43 - US07 Criar conta e entrar

- [x] Criar a página de cadastro de estudante (nome, e-mail e senha).
- [x] Permitir entrar e sair, com login por e-mail.
- [x] Mostrar na navegação se o estudante está conectado.
- [x] Testar o cadastro, o login e o logout.

### #44 - US08 Registrar tentativas

- [x] Criar o modelo Tentativa, conforme o diagrama de classes.
- [x] Registrar uma tentativa a cada resposta enviada.
- [x] Exigir login para responder; a explicação continua aberta a todos.
- [x] Testar o registro da tentativa.

### #45 - US09 Acompanhar o progresso

- [x] Calcular acertos, erros e percentual por conteúdo a partir das tentativas.
- [x] Criar a página "Meu progresso", com o resumo por conteúdo e os erros comuns mais frequentes.
- [x] Orientar o estudante que ainda não tem tentativas.
- [x] Testar o cálculo do progresso.

### #61 - Camada de apresentação na pasta `frontend/`

- [x] Mover os templates e o CSS para `frontend/`.
- [x] Apontar as configurações do Django para a nova pasta.
- [x] Registrar a decisão no ADR 0002.

### #62 - US10 Criar turma e entrar com código

- [x] Criar o modelo Turma, conforme o diagrama de classes.
- [x] Permitir que o professor crie a turma e receba o código de acesso.
- [x] Permitir que o aluno entre na turma com o código.
- [x] Testar a criação, o código e a entrada na turma.

### #63 - US11 Acompanhar o desempenho da turma

- [x] Calcular o desempenho de cada aluno e os conteúdos com mais erros.
- [x] Criar a página da turma e a do progresso individual do aluno.
- [x] Negar o acesso a turmas de outros professores e a alunos de outra turma.
- [x] Testar o cálculo e o controle de acesso.

### #46 - Containers com PostgreSQL

- [x] Escrever o `backend/Dockerfile` com Gunicorn.
- [x] Escrever o `docker-compose.yml` com a aplicação e o PostgreSQL.
- [x] Escrever o `build.sh` para construir e iniciar os containers.
- [x] Documentar a execução no README e registrar o ADR do banco de dados.

### #47 - Diagramas

- [x] Diagrama de casos de uso.
- [x] Diagrama de classes atualizado com o que foi implementado.
- [x] Diagrama de arquitetura (modelo C4: contexto e containers).
- [x] BPD do processo de resolver um exercício.

### #48 - Métricas e ADRs

- [ ] Registrar as horas por fase da engenharia de software.
- [ ] Registrar linhas de código, commits, Pull Requests, issues, testes e cobertura.
- [ ] Registrar os ADRs pendentes: monólito em vez de microsserviços e tabela única para os tipos de usuário.
- [ ] Preencher ou remover os arquivos vazios de `docs/`.

### #49 - Apresentação final

- [ ] Montar os slides a partir da estrutura indicada pelo professor.
- [ ] Ensaiar e gravar o vídeo (cerca de 30 minutos).
- [ ] Adicionar ao README o link do vídeo e a licença; criar a tag `v1.0.0`.
- [ ] Migrar o registro da Sprint 1 do repositório v1.

### #55 - API REST

Antecipada para 26/11, para entrar na entrega de Programação Web.

- [x] Adicionar o Django REST Framework ao projeto.
- [x] Expor conteúdos e exercícios em JSON, somente para leitura e sem a resposta correta.
- [x] Testar os endpoints.
- [x] Documentar a API no README.

### #9 - US05 Ordem das operações

Último item da ordem: só começa depois da entrega de Programação Web.

- [ ] Preparar a explicação e conferir os exemplos resolvidos.
- [ ] Elaborar os exercícios com alternativas baseadas em erros comuns.
- [ ] Conferir a correção matemática de exemplos, alternativas e resoluções.
- [ ] Disponibilizar o conteúdo na trilha.

## Fora da Sprint

- US06 - Notação matemática (#10): continua no Product Backlog.
- Publicação online da aplicação: a demonstração usa a execução local ou por container.
- Monitoramento com Prometheus e Grafana, microsserviços e servidor de front-end separado: não são exigidos; a decisão será registrada em ADR e em trabalhos futuros.

## Definition of Done

Um item será considerado "Pronto" quando:

- Atender aos critérios de aceitação da issue.
- Passar nos hooks do pre-commit e nos testes, localmente e no GitHub Actions.
- Tiver sido testado manualmente em computador e celular, quando alterar a interface.
- Estiver integrado à `main` por Pull Request vinculado à issue.
- Tiver a documentação relacionada atualizada.

## Riscos

- Os itens Must (42 SP) estão muito acima da velocidade medida (10 e 14 SP).
- Duas entregas no mesmo dia (07/12), depois da entrega antecipada de Programação Web (26/11).
- O enunciado de Programação Web pede só o código do projeto. PostgreSQL, API REST e containers continuam Must por causa do conteúdo programático da disciplina e da apresentação de Engenharia de Software.
- GitHub Actions, containers, PostgreSQL, autenticação e Django REST Framework são tecnologias novas no projeto. Antes de cada um desses itens, a viabilidade é verificada na documentação oficial, para não repetir o problema da #7 na Sprint 2.

**Plano de contingência**, aplicado se um marco atrasar mais de um dia, nesta ordem:

1. US05 (#9) volta ao Product Backlog.
2. A US09 (#45) entrega só o resumo por conteúdo, sem os erros comuns mais frequentes.
3. A API REST (#55) é reduzida a um único recurso somente para leitura (a lista de conteúdos).
4. Os diagramas (#47) e as métricas (#48) são feitos em paralelo com os slides.
