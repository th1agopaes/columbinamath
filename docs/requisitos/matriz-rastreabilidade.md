# Matriz de rastreabilidade - ColumbinaMath

A matriz liga cada requisito ao caso de uso, à história de usuário, às issues e à evidência de que ele foi atendido. Ela responde a duas perguntas: "onde este requisito foi implementado e testado?" e "por que este código existe?".

A matriz é atualizada no mesmo Pull Request de cada item concluído. Situação em 25/11/2026.

Documentos relacionados:

- [Requisitos](requisitos.md)
- [Especificação dos casos de uso](especificacao-casos-de-uso.md)
- [Product Backlog](../scrum/product-backlog.md)

## Requisitos funcionais

| Requisito | Caso de uso | Histórias | Issues | Evidência | Situação |
|---|---|---|---|---|---|
| RF001 - Manter usuários | - | US07 | #22, #24, #43 | `TestCadastro`, `TestEntrarESair`, `TestUsuario`; painel administrativo | Atendido |
| RF002 - Manter conteúdos | UC3 | - | #6 | Painel administrativo (`conteudos/admin.py`) e fixtures | Atendido |
| RF003 - Manter exercícios | UC3 | - | #6, #44 | Painel administrativo; `TestPainelDoExercicio` | Atendido |
| RF004 - Manter tipos de erro comum | UC3 | - | #6 | `TestValidacaoDoErroComum` | Atendido |
| RF005 - Resolver exercício | UC1 | US03, US08 | #6, #30, #44 | `TestNormalizarResposta`, `TestVerificarResposta`, `TestIdentificarErro`, `TestPaginas`, `TestTeoriaEResolucao`, `TestRegistroDaTentativa` | Atendido |
| RF006 - Acompanhar progresso | UC2 | US09 | #45 | `TestCalculoDoProgresso`, `TestPaginaMeuProgresso` | Atendido |
| RF007 - Vincular aluno a professor | UC4 | US10 | #62 | `TestTurma`, `TestPaginasDoProfessor`, `TestPaginasDoAluno` | Atendido |
| RF008 - Acompanhar desempenho da turma | UC4 | US11 | #63 | `TestDesempenho`, `TestPaginaDaTurma` | Atendido |
| RF009 - Consultar conteúdos e explicações | UC1 | US01, US02, US04, US05 | #6, #8, #30, #9 | `TestPaginas`, `TestTeoriaEResolucao`, `TestTrilha` | Atendido |
| RF010 - Disponibilizar conteúdos por API REST | - | - | #55 | `TestConteudos`, `TestExercicios` (app `api`) | Atendido |

## Requisitos não funcionais

| Requisito | Caso de uso | Histórias | Issues | Evidência | Situação |
|---|---|---|---|---|---|
| RNF001 - Tempo de resposta | UC1 | US03 | #6, #48 | Correção no servidor em uma requisição; medição prevista na #48 | Parcial |
| RNF002 - Segurança de senhas | - | US07 | #22, #43 | `TestCadastro::test_guarda_a_senha_so_com_hash` | Atendido |
| RNF003 - Privacidade (LGPD) | - | US07, US10 | #43, #62 | `TestCadastro::test_pede_so_nome_email_e_senha` | Atendido |
| RNF004 - Responsividade | UC1 | US01, US02, US03 | #6 | Teste manual em computador e celular (Definition of Done) | Atendido |
| RNF005 - Portabilidade | - | - | #46 | Execução documentada no README, prevista na #46 | Planejado |

## Testes por app

Os testes ficam em `backend/<app>/tests.py`, e as fixtures compartilhadas, em `backend/conftest.py`.

| App | Classes de teste | Requisitos | Testes |
|---|---|---|---|
| `conteudos` | `TestNormalizarResposta`, `TestVerificarResposta`, `TestIdentificarErro`, `TestValidacaoDoErroComum`, `TestPaginas`, `TestTeoriaEResolucao`, `TestTrilha`, `TestPainelDoExercicio` | RF003, RF004, RF005 e RF009 | 25 |
| `usuarios` | `TestCadastro`, `TestEntrarESair`, `TestUsuario` | RF001, RNF002 e RNF003 | 15 |
| `progresso` | `TestRegistroDaTentativa`, `TestPainel`, `TestCalculoDoProgresso`, `TestPaginaMeuProgresso` | RF005 e RF006 | 17 |
| `turmas` | `TestTurma`, `TestPaginasDoProfessor`, `TestPaginasDoAluno`, `TestDesempenho`, `TestPaginaDaTurma` | RF007 e RF008 | 25 |
| `api` | `TestConteudos`, `TestExercicios` | RF010 | 8 |

**Total:** 90 testes, com 99% de cobertura de código (mínimo exigido no CI: 90%).

## O que a matriz mostra

- **Sem teste automatizado próprio:** RF002 e parte do RF003. O cadastro usa o painel administrativo do Django, que já é testado pelo próprio framework.
- **Sem evidência registrada:** RNF001. Falta a medição do tempo de resposta (#48).
- **Aguardando implementação:** RNF005 (#46).
- **História fora da sprint:** a US06 (#10, Could) melhora a apresentação das expressões, está ligada ao RF009 e continua no Product Backlog.
- **Itens sem requisito:** as issues de processo e infraestrutura (planejamento, CI, documentação, diagramas e a pasta `frontend/`) não atendem a um requisito do produto. Elas estão descritas nos documentos das sprints.
