# Requisitos - ColumbinaMath

Este documento registra os requisitos do ColumbinaMath, a prioridade de cada um e a situação na entrega final (Sprint 3).

Os requisitos RF001 a RF008 e RNF001 a RNF004 vêm do Documento de Visão da Modelagem - Parte I (versão 1.1, de 14/10/2026), feita na disciplina de Programação Web. Os demais foram acrescentados durante o projeto e estão identificados.

Documentos relacionados:

- [Especificação dos casos de uso](especificacao-casos-de-uso.md)
- [Product Backlog](../scrum/product-backlog.md)
- [Sprint 3](../scrum/sprints/sprint-03.md)

## Histórico de revisão

| Data | Versão | Descrição |
|---|---|---|
| 07/10/2026 | 1.0 | Versão inicial, no Documento de Visão. |
| 14/10/2026 | 1.1 | Modelo conceitual sem atributos, conforme orientação do professor. |
| 16/11/2026 | 1.2 | Requisitos trazidos para o repositório, com prioridade e situação. RF009, RF010 e RNF005 acrescentados. |

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
| RF001 | Manter usuários | Cadastrar, autenticar (login e logout), editar e desativar contas de aluno, professor e administrador. | Must | Parcial |
| RF002 | Manter conteúdos | O administrador cadastra os conteúdos e seus níveis de dificuldade. | Must | Atendido |
| RF003 | Manter exercícios | O administrador cadastra exercícios vinculados a um conteúdo, com enunciado, resposta correta e nível. | Must | Atendido |
| RF004 | Manter tipos de erro comum | O administrador cadastra erros comuns por exercício, cada um com a resposta errada esperada e uma explicação. | Must | Atendido |
| RF005 | Resolver exercício | O aluno responde e o sistema corrige na hora. Se a resposta errada corresponder a um erro comum (RF004), exibe a explicação direcionada. Cada tentativa é registrada. | Must | Parcial |
| RF006 | Acompanhar progresso | Exibe ao aluno os acertos e erros por conteúdo, com base nas tentativas do RF005. | Must | Planejado |
| RF007 | Vincular aluno a professor | O professor cria uma turma e gera um código de acesso, que o aluno usa para entrar nela. | Won't | Fora da entrega |
| RF008 | Acompanhar desempenho da turma | O professor visualiza o progresso (RF006) dos alunos da sua turma. | Won't | Fora da entrega |
| RF009 | Consultar conteúdos e explicações | O estudante visualiza a trilha de conteúdos e consulta a explicação de cada um, com exemplos resolvidos. | Must | Atendido |
| RF010 | Disponibilizar conteúdos por API REST | Um cliente HTTP consulta conteúdos e exercícios em JSON, somente para leitura e sem a resposta correta. | Must | Planejado |

### Detalhes por requisito

- **RF001:** o modelo `Usuario` existe, com e-mail único e o tipo de perfil. As contas são criadas, editadas e desativadas pelo administrador no painel do Django. O cadastro feito pelo próprio estudante e o login por e-mail entram com a US07 (#43). Editar ou desativar a própria conta pela aplicação: Won't.
- **RF002, RF003 e RF004:** atendidos pelo painel administrativo do Django. Os erros comuns são cadastrados dentro do exercício, e o sistema recusa um erro comum igual à resposta correta. O nível de dificuldade fica no exercício. O conteúdo inicial é carregado por fixtures.
- **RF005:** a correção imediata e a explicação do erro comum foram entregues na US03. O registro de cada tentativa entra com a US08 (#44).
- **RF006:** entra com a US09 (#45), com o resumo por conteúdo e os erros comuns mais frequentes. O detalhamento das tentativas de um conteúdo (passos 5 e 6 do caso de uso 2): Won't.
- **RF007 e RF008:** as turmas ficam para uma versão futura. A decisão está registrada na [Sprint 3](../scrum/sprints/sprint-03.md#fora-da-sprint).
- **RF009:** acrescentado em 16/11/2026. O comportamento existe desde a Sprint 1 (US01 e US02) e foi ampliado na US04, mas não tinha requisito próprio no Documento de Visão.
- **RF010:** acrescentado em 16/11/2026, no replanejamento da Sprint 3. Entra com a #55.

## Requisitos não funcionais

| ID | Requisito | Descrição | MoSCoW | Situação |
|---|---|---|---|---|
| RNF001 | Tempo de resposta | O feedback de um exercício não pode exceder 2 segundos. | Must | Parcial |
| RNF002 | Segurança de senhas | Senhas armazenadas apenas com hash (recurso nativo do Django), nunca em texto puro. | Must | Atendido |
| RNF003 | Privacidade (LGPD) | Coletar apenas os dados necessários, já que parte dos usuários pode ser menor de idade. | Must | Planejado |
| RNF004 | Responsividade | A interface deve funcionar em computadores e celulares. | Must | Atendido |
| RNF005 | Portabilidade | A aplicação executa em containers, com PostgreSQL, a partir de um único comando. | Must | Planejado |

### Detalhes por requisito

- **RNF001:** a correção acontece no servidor, em uma única requisição. Falta registrar uma medição do tempo de resposta, prevista nas métricas do projeto (#48).
- **RNF002:** o modelo `Usuario` herda do `AbstractUser` do Django, que guarda a senha apenas com hash. A US07 (#43) acrescenta um teste automatizado.
- **RNF003:** o cadastro da US07 (#43) pede só nome, e-mail e senha.
- **RNF004:** a interface usa CSS próprio com largura fluida. O teste manual em computador e celular faz parte da Definition of Done.
- **RNF005:** acrescentado em 16/11/2026, no replanejamento da Sprint 3. Entra com a #46.

## Restrições

- Desenvolvido em Python com o framework Django (padrão MVT), conforme o [ADR 0001](../arquitetura/adr/0001-troca-de-stack-para-django.md).
- Banco de dados relacional: SQLite no desenvolvimento e PostgreSQL na execução por container (#46).
- Projeto em dupla, com prazos definidos pelo calendário acadêmico 2026-2.

## Fora do escopo do produto

- Videoaulas.
- Chat ou comunicação em tempo real entre usuários.
- Emissão de certificados.
- Conteúdos além da matemática básica.

## Mudanças em relação à Modelagem - Parte I

- **Questão em aberto "O aluno poderá tentar o mesmo exercício mais de uma vez?":** sim. Cada resposta gera uma nova tentativa (US08).
- **Questão em aberto "Respostas equivalentes (ex.: 1/2 e 0,5) serão aceitas?":** deixou de se aplicar. Os exercícios são de múltipla escolha: as alternativas são a resposta correta e os erros comuns.
- **Requisitos acrescentados:** RF009, RF010 e RNF005.
