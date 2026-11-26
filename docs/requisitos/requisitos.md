# Requisitos - ColumbinaMath

Este documento registra os requisitos do ColumbinaMath, a prioridade de cada um e a situação na entrega final (Sprint 3).

Os requisitos RF001 a RF008 e RNF001 a RNF004 vêm do Documento de Visão da Modelagem - Parte I (versão 1.1, de 14/10/2026), feita na disciplina de Programação Web. Os demais foram acrescentados durante o projeto e estão identificados.

Documentos relacionados:

- [Especificação dos casos de uso](especificacao-casos-de-uso.md)
- [Matriz de rastreabilidade](matriz-rastreabilidade.md)
- [Product Backlog](../scrum/product-backlog.md)
- [Sprint 3](../scrum/sprints/sprint-03.md)
- [Modelagem - Parte I](modelagem/modelagem-parte-1.pdf): cenário, documento de visão, modelo conceitual e casos de uso.
- [Modelagem - Parte II](modelagem/modelagem-parte-2.pdf): diagramas de sequência e diagrama de classes.

## Histórico de revisão

| Data | Versão | Descrição |
|---|---|---|
| 07/10/2026 | 1.0 | Versão inicial, no Documento de Visão. |
| 14/10/2026 | 1.1 | Modelo conceitual sem atributos, conforme orientação do professor. |
| 16/11/2026 | 1.2 | Requisitos trazidos para o repositório, com prioridade e situação. RF009, RF010 e RNF005 acrescentados. |
| 25/11/2026 | 1.3 | RF007 e RF008 passam de Won't para Must. Situação atualizada após a implementação da modelagem inteira. |

## Como ler

**Prioridade (MoSCoW)**, em relação à entrega final do projeto:

- **Must have:** indispensável para a entrega.
- **Should have:** importante, mas pode ser adiado sem inviabilizar a entrega.
- **Could have:** desejável, caso haja capacidade.
- **Won't have this time:** fora desta entrega.

**Situação:**

- **Atendido:** implementado e integrado à `main`.
- **Parcial:** uma parte está implementada; o restante tem issue aberta.
- **Planejado:** ainda não implementado; tem issue na Sprint 3.
- **Fora da entrega:** não será implementado nesta versão.

## Requisitos funcionais

| ID | Requisito | Descrição | MoSCoW | Situação |
|---|---|---|---|---|
| RF001 | Manter usuários | Cadastrar, autenticar (login e logout), editar e desativar contas de aluno, professor e administrador. | Must | Atendido |
| RF002 | Manter conteúdos | O administrador cadastra os conteúdos e seus níveis de dificuldade. | Must | Atendido |
| RF003 | Manter exercícios | O administrador cadastra exercícios vinculados a um conteúdo, com enunciado, resposta correta e nível. | Must | Atendido |
| RF004 | Manter tipos de erro comum | O administrador cadastra erros comuns por exercício, cada um com a resposta errada esperada e uma explicação. | Must | Atendido |
| RF005 | Resolver exercício | O aluno responde e o sistema corrige na hora. Se a resposta errada corresponder a um erro comum (RF004), exibe a explicação direcionada. Cada tentativa é registrada. | Must | Atendido |
| RF006 | Acompanhar progresso | Exibe ao aluno os acertos e erros por conteúdo, com base nas tentativas do RF005. | Must | Atendido |
| RF007 | Vincular aluno a professor | O professor cria uma turma e gera um código de acesso, que o aluno usa para entrar nela. | Must | Atendido |
| RF008 | Acompanhar desempenho da turma | O professor visualiza o progresso (RF006) dos alunos da sua turma. | Must | Atendido |
| RF009 | Consultar conteúdos e explicações | O estudante visualiza a trilha de conteúdos e consulta a explicação de cada um, com exemplos resolvidos. | Must | Atendido |
| RF010 | Disponibilizar conteúdos por API REST | Um cliente HTTP consulta conteúdos e exercícios em JSON, somente para leitura e sem a resposta correta. | Must | Atendido |

### Detalhes por requisito

- **RF001:** o estudante cria a própria conta e entra com e-mail e senha (US07, #43). As contas de professor e de administrador são criadas pelo administrador, e qualquer conta é editada ou desativada no painel do Django (`Usuario.desativar()` preserva o histórico). Editar ou desativar a própria conta pela aplicação: Won't.
- **RF002, RF003 e RF004:** atendidos pelo painel administrativo do Django. Os erros comuns são cadastrados dentro do exercício, e o sistema recusa um erro comum igual à resposta correta. O nível de dificuldade fica no exercício. O conteúdo inicial é carregado por fixtures.
- **RF005:** a correção imediata e a explicação do erro comum foram entregues na US03. O registro de cada tentativa (`Tentativa`, com o erro comum quando houver) e a exigência de login para responder foram entregues na US08 (#44).
- **RF006:** página "Meu progresso" (US09, #45), com o resumo por conteúdo e os erros comuns mais frequentes, calculados a partir das tentativas (`Aluno.calcular_progresso()`). O detalhamento das tentativas de um conteúdo (passos 5 e 6 do caso de uso 2): Won't.
- **RF007:** o professor cria a turma e recebe um código de 6 caracteres; o aluno entra com o código (US10, #62). Eram Won't até o [replanejamento de 25/11](../scrum/sprints/sprint-03.md#replanejamento-de-2511).
- **RF008:** a página da turma mostra o desempenho de cada aluno e os conteúdos com mais erros, e o professor abre o progresso individual de cada aluno da turma (US11, #63).
- **RF009:** acrescentado em 16/11/2026. O comportamento existe desde a Sprint 1 (US01 e US02) e foi ampliado na US04, mas não tinha requisito próprio no Documento de Visão.
- **RF010:** acrescentado em 16/11/2026, no replanejamento da Sprint 3. Atendido pela #55: API REST somente leitura em `/api/`, com o Django REST Framework.

## Requisitos não funcionais

| ID | Requisito | Descrição | MoSCoW | Situação |
|---|---|---|---|---|
| RNF001 | Tempo de resposta | O feedback de um exercício não pode exceder 2 segundos. | Must | Parcial |
| RNF002 | Segurança de senhas | Senhas armazenadas apenas com hash (recurso nativo do Django), nunca em texto puro. | Must | Atendido |
| RNF003 | Privacidade (LGPD) | Coletar apenas os dados necessários, já que parte dos usuários pode ser menor de idade. | Must | Atendido |
| RNF004 | Responsividade | A interface deve funcionar em computadores e celulares. | Must | Atendido |
| RNF005 | Portabilidade | A aplicação executa em containers, com PostgreSQL, a partir de um único comando. | Must | Atendido |

### Detalhes por requisito

- **RNF001:** a correção acontece no servidor, em uma única requisição. Falta registrar uma medição do tempo de resposta, prevista nas métricas do projeto (#48).
- **RNF002:** o modelo `Usuario` herda do `AbstractUser` do Django, que guarda a senha apenas com hash. Um teste automatizado da US07 confere que a senha gravada não é o texto digitado.
- **RNF003:** o cadastro pede só nome, e-mail e senha, conferido por teste automatizado. O atributo `serie` do Aluno, previsto no diagrama de classes, não foi implementado pelo mesmo motivo.
- **RNF004:** a interface usa CSS próprio com largura fluida. O teste manual em computador e celular faz parte da Definition of Done.
- **RNF005:** acrescentado em 16/11/2026, no replanejamento da Sprint 3. Atendido pela #46: `./build.sh` inicia a aplicação e o PostgreSQL em containers ([ADR 0004](../arquitetura/adr/0004-postgresql-e-containers.md)).

## Restrições

- Desenvolvido em Python com o framework Django (padrão MVT), conforme o [ADR 0001](../arquitetura/adr/0001-troca-de-stack-para-django.md).
- Banco de dados relacional: SQLite no desenvolvimento e PostgreSQL na execução por container.
- Projeto em dupla em Engenharia de Software e Extensão I, e individual em Programação Web, com prazos definidos pelo calendário acadêmico 2026-2.

## Fora do escopo do produto

- Videoaulas.
- Chat ou comunicação em tempo real entre usuários.
- Emissão de certificados.
- Conteúdos além da matemática básica.

## Mudanças em relação à Modelagem - Parte I

- **Questão em aberto "O aluno poderá tentar o mesmo exercício mais de uma vez?":** sim. Cada resposta gera uma nova tentativa (US08).
- **Questão em aberto "Respostas equivalentes (ex.: 1/2 e 0,5) serão aceitas?":** deixou de se aplicar. Os exercícios são de múltipla escolha: as alternativas são a resposta correta e os erros comuns.
- **Requisitos acrescentados:** RF009, RF010 e RNF005.
