# Sprint 03 - ColumbinaMath

## Datas

- Início: 10/11/2026.
- Planejamento: 16/11/2026.
- Entrega de Engenharia de Software: 01/12/2026 (vídeo da apresentação final).
- Entrega de Programação Web: prevista para 05/12/2026.
- Sprint Review: 07/12/2026.

## Contexto

Esta é a última sprint do projeto. O mesmo produto é avaliado em três disciplinas, com três datas próximas, e a mais cedo delas (01/12) define o ritmo da sprint.

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

## Capacidade

- Velocidade medida: 10 SP na Sprint 1 e 14 SP na Sprint 2.
- Os itens Must desta sprint somam 35 SP, duas vezes e meia a maior velocidade medida.
- Situação em 16/11: 4 SP concluídos (#41 e #7). Restam 28 SP até 01/12 e 3 SP (API REST) de 02 a 04/12.
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
| 6 | #45 | US09 - Acompanhar o progresso | Must | 3 SP | |
| 7 | #46 | Executar a aplicação em containers com PostgreSQL | Must | 5 SP | |
| 8 | #47 | Diagramas de casos de uso, classes, arquitetura e BPD | Must | 3 SP | |
| 9 | #48 | Métricas do projeto e ADRs pendentes | Must | 2 SP | |
| 10 | #49 | Apresentação final: slides, vídeo e versão 1.0 | Must | 5 SP | |
| 11 | #55 | Expor conteúdos e exercícios por API REST | Must | 3 SP | |
| 12 | #9 | US05 - Ordem das operações | Should | 5 SP | |

**Total:** 40 SP (35 SP Must e 5 SP Should).

## Marcos

| Data | Marco |
|---|---|
| 18/11 | CI ativo e requisitos registrados em `docs/requisitos/` |
| 23/11 | Conta, tentativas e progresso funcionando |
| 25/11 | Aplicação executando por container com PostgreSQL |
| 27/11 | Diagramas e métricas prontos; congelamento do código (code freeze) |
| 01/12 | Vídeo entregue em Engenharia de Software |
| 04/12 | API REST disponível |
| 05/12 | Entrega de Programação Web |
| 07/12 | Sprint Review 3 |

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

- [ ] Calcular acertos, erros e percentual por conteúdo a partir das tentativas.
- [ ] Criar a página "Meu progresso", com o resumo por conteúdo e os erros comuns mais frequentes.
- [ ] Orientar o estudante que ainda não tem tentativas.
- [ ] Testar o cálculo do progresso.

### #46 - Containers com PostgreSQL

- [ ] Escrever o `backend/Dockerfile` com Gunicorn.
- [ ] Escrever o `docker-compose.yml` com a aplicação e o PostgreSQL.
- [ ] Escrever o `build.sh` para construir e iniciar os containers.
- [ ] Documentar a execução no README e registrar o ADR do banco de dados.

### #47 - Diagramas

- [ ] Diagrama de casos de uso.
- [ ] Diagrama de classes atualizado com o que foi implementado.
- [ ] Diagrama de arquitetura (modelo C4: contexto e containers).
- [ ] BPD do processo de resolver um exercício.

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

Feita de 02 a 04/12, depois da entrega de Engenharia de Software. Como chega depois da tag `v1.0.0`, é publicada como versão `v1.1.0`.

- [ ] Adicionar o Django REST Framework ao projeto.
- [ ] Expor conteúdos e exercícios em JSON, somente para leitura e sem a resposta correta.
- [ ] Testar os endpoints.
- [ ] Documentar a API no README.

### #9 - US05 Ordem das operações

Último item da ordem: só começa depois da entrega de 01/12.

- [ ] Preparar a explicação e conferir os exemplos resolvidos.
- [ ] Elaborar os exercícios com alternativas baseadas em erros comuns.
- [ ] Conferir a correção matemática de exemplos, alternativas e resoluções.
- [ ] Disponibilizar o conteúdo na trilha.

## Fora da Sprint

- US06 - Notação matemática (#10): continua no Product Backlog.
- Turmas e desempenho da turma (RF007 e RF008): Won't have this time.
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

- Os itens Must (35 SP) estão muito acima da velocidade medida (10 e 14 SP).
- Três entregas em sete dias (01/12, 05/12 e 07/12).
- Os critérios da entrega de Programação Web ainda não foram confirmados. Se o professor dispensar PostgreSQL, API REST ou containers, o item dispensado volta a ser Should.
- GitHub Actions, containers, PostgreSQL, autenticação e Django REST Framework são tecnologias novas no projeto. Antes de cada um desses itens, a viabilidade é verificada na documentação oficial, para não repetir o problema da #7 na Sprint 2.

**Plano de contingência**, aplicado se um marco atrasar mais de um dia, nesta ordem:

1. US05 (#9) volta ao Product Backlog.
2. A US09 (#45) entrega só o resumo por conteúdo, sem os erros comuns mais frequentes.
3. A API REST (#55) é reduzida a um único recurso somente para leitura (a lista de conteúdos).
4. Os diagramas (#47) e as métricas (#48) passam para 28 e 29/11, em paralelo com os slides.
