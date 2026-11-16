# Matriz de rastreabilidade - ColumbinaMath

A matriz liga cada requisito ao caso de uso, à história de usuário, às issues e à evidência de que ele foi atendido. Ela responde a duas perguntas: "onde este requisito foi implementado e testado?" e "por que este código existe?".

A matriz é atualizada no mesmo Pull Request de cada item concluído. Situação em 16/11/2026.

Documentos relacionados:

- [Requisitos](requisitos.md)
- [Especificação dos casos de uso](especificacao-casos-de-uso.md)
- [Product Backlog](../scrum/product-backlog.md)

## Requisitos funcionais

| Requisito | Caso de uso | Histórias | Issues | Evidência | Situação |
|---|---|---|---|---|---|
| RF001 - Manter usuários | - | US07 | #22, #24, #43 | Modelo `Usuario` e painel administrativo; testes previstos na US07 | Parcial |
| RF002 - Manter conteúdos | UC3 | - | #6 | Painel administrativo (`conteudos/admin.py`) e fixtures | Atendido |
| RF003 - Manter exercícios | UC3 | - | #6 | Painel administrativo (`conteudos/admin.py`) e fixtures | Atendido |
| RF004 - Manter tipos de erro comum | UC3 | - | #6 | `TestValidacaoDoErroComum` | Atendido |
| RF005 - Resolver exercício | UC1 | US03, US08 | #6, #30, #44 | `TestNormalizarResposta`, `TestVerificarResposta`, `TestIdentificarErro`, `TestPaginas` e `TestTeoriaEResolucao`; registro da tentativa previsto na US08 | Parcial |
| RF006 - Acompanhar progresso | UC2 | US09 | #45 | Testes previstos na US09 | Planejado |
| RF007 - Vincular aluno a professor | UC4 | - | - | - | Fora da entrega |
| RF008 - Acompanhar desempenho da turma | UC4 | - | - | - | Fora da entrega |
| RF009 - Consultar conteúdos e explicações | UC1 | US01, US02, US04, US05 | #6, #8, #30, #9 | `TestPaginas` e `TestTeoriaEResolucao` | Atendido |
| RF010 - Disponibilizar conteúdos por API REST | - | - | #55 | Testes previstos na #55 | Planejado |

## Requisitos não funcionais

| Requisito | Caso de uso | Histórias | Issues | Evidência | Situação |
|---|---|---|---|---|---|
| RNF001 - Tempo de resposta | UC1 | US03 | #6, #48 | Correção no servidor em uma requisição; medição prevista na #48 | Parcial |
| RNF002 - Segurança de senhas | - | US07 | #22, #43 | `Usuario` herda de `AbstractUser`; teste previsto na US07 | Atendido |
| RNF003 - Privacidade (LGPD) | - | US07 | #43 | Teste previsto na US07 | Planejado |
| RNF004 - Responsividade | UC1 | US01, US02, US03 | #6 | Teste manual em computador e celular (Definition of Done) | Atendido |
| RNF005 - Portabilidade | - | - | #46 | Execução documentada no README, prevista na #46 | Planejado |

## Testes por requisito

Os testes ficam em `backend/conteudos/tests.py`.

| Requisito | Classe de teste | Testes |
|---|---|---|
| RF004 | `TestValidacaoDoErroComum` | 3 |
| RF005 | `TestNormalizarResposta` | 2 |
| RF005 | `TestVerificarResposta` | 3 |
| RF005 | `TestIdentificarErro` | 2 |
| RF005 | `TestPaginas` (resposta correta, erro comum e alternativa inexistente) | 3 |
| RF005 | `TestTeoriaEResolucao` (resolução no acerto) | 1 |
| RF009 | `TestPaginas` (lista, ordem da trilha e conteúdo inexistente) | 3 |
| RF009 | `TestTeoriaEResolucao` (explicação e exemplo) | 1 |
| RF005 e RF009 | `TestTeoriaEResolucao` (separação das linhas) | 1 |

**Total:** 19 testes.

## O que a matriz mostra

- **Sem teste automatizado próprio:** RF002 e RF003. O cadastro usa o painel administrativo do Django, que já é testado pelo próprio framework.
- **Sem evidência registrada:** RNF001. Falta a medição do tempo de resposta (#48).
- **Aguardando implementação:** RF001 (cadastro e login), RF006, RF010, RNF003 e RNF005, todos com issue na Sprint 3.
- **História fora da sprint:** a US06 (#10, Could) melhora a apresentação das expressões, está ligada ao RF009 e continua no Product Backlog.
- **Itens sem requisito:** as issues de processo e infraestrutura (planejamento, CI, documentação e diagramas) não atendem a um requisito do produto. Elas estão descritas nos documentos das sprints.
