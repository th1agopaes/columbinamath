# Especificação dos casos de uso - ColumbinaMath

Este documento descreve os quatro casos de uso do ColumbinaMath. Eles vêm da Modelagem - Parte I (14/10/2026) e foram atualizados para refletir o que foi implementado. As diferenças estão indicadas em cada caso de uso.

Documento relacionado: [Requisitos](requisitos.md).

## Visão geral

| Caso de uso | Ator principal | Requisitos | Prioridade | Situação |
|---|---|---|---|---|
| UC1 - Resolver Exercício | Aluno | RF005 | Alta | Parcial |
| UC2 - Acompanhar Progresso | Aluno | RF006 | Média | Planejado |
| UC3 - Cadastrar Exercício | Administrador | RF003 e RF004 | Alta | Atendido |
| UC4 - Acompanhar Desempenho da Turma | Professor | RF007 e RF008 | Baixa | Fora da entrega |

## UC1 - Resolver Exercício

| Campo | Descrição |
|---|---|
| Contexto de uso | O aluno escolhe um conteúdo, responde exercícios e recebe correção imediata com explicação direcionada ao erro. |
| Escopo | Sistema ColumbinaMath |
| Requisito relacionado | RF005 |
| Condições prévias | Aluno autenticado; existe ao menos um exercício cadastrado no conteúdo. |
| Condição final com sucesso | A resposta é corrigida, o feedback é exibido e a tentativa é registrada. |
| Condição final com falha | A tentativa não é registrada e nenhum feedback é exibido. |
| Ator principal | Aluno |
| Gatilho | O aluno seleciona um conteúdo para praticar. |

**Cenário principal de sucesso:**

1. O aluno seleciona um conteúdo na trilha.
2. O sistema exibe a explicação do conteúdo e a lista de exercícios.
3. O aluno seleciona um exercício.
4. O sistema exibe o enunciado e as alternativas: a resposta correta e os erros comuns, em ordem alfabética.
5. O aluno seleciona uma alternativa e envia a resposta.
6. O sistema compara a resposta com a resposta correta, no servidor.
7. O sistema exibe a mensagem de acerto, a alternativa correta e a resolução passo a passo.
8. O sistema registra a tentativa (aluno, exercício, resposta, resultado, data e hora).
9. O aluno solicita o próximo exercício.
10. O sistema retorna ao passo 4, com o exercício seguinte.

**Extensões:**

- **5a. Nenhuma alternativa selecionada:** o sistema informa que é preciso selecionar uma alternativa e retorna ao passo 5. Nenhuma tentativa é registrada.
- **5b. A resposta enviada não é uma alternativa do exercício:** o sistema recusa a resposta e retorna ao passo 5. Nenhuma tentativa é registrada.
- **7a. Resposta incorreta:** o sistema exibe a explicação do erro comum correspondente, a alternativa correta e a resolução passo a passo. O erro comum fica associado à tentativa, e o fluxo segue para o passo 8.
- **9a. O aluno escolhe tentar novamente:** o sistema retorna ao passo 4, com o mesmo exercício. A nova resposta gera outra tentativa.
- **9b. Não há mais exercícios no conteúdo:** o sistema oferece a volta à trilha.

**Informação do projeto:** prioridade alta; tempo de resposta de até 2 segundos (RNF001); canal web, em computadores e celulares (RNF004).

**Situação:** os passos 1 a 7 e 9 a 10 foram entregues na US03. A exigência de login e o registro da tentativa (passo 8) entram com a US08 (#44).

**Diferenças em relação à Modelagem - Parte I:**

- Os exercícios são de múltipla escolha. Na modelagem, o aluno digitava a resposta.
- O aluno escolhe o exercício na lista do conteúdo. Na modelagem, o sistema escolhia o exercício de acordo com o nível.
- A alternativa correta e a resolução aparecem no acerto e no erro.
- Toda alternativa errada é um erro comum cadastrado. Por isso, a extensão "resposta incorreta sem erro comum correspondente" deixou de existir.
- As duas questões em aberto foram resolvidas e estão registradas nos [Requisitos](requisitos.md#mudanças-em-relação-à-modelagem---parte-i).

## UC2 - Acompanhar Progresso

| Campo | Descrição |
|---|---|
| Contexto de uso | O aluno consulta seus acertos e erros por conteúdo para saber onde precisa praticar mais. |
| Escopo | Sistema ColumbinaMath |
| Requisito relacionado | RF006 |
| Condições prévias | Aluno autenticado. |
| Condição final com sucesso | O progresso por conteúdo é exibido. |
| Condição final com falha | O progresso não é exibido. |
| Ator principal | Aluno |
| Gatilho | O aluno acessa a opção "Meu progresso". |

**Cenário principal de sucesso:**

1. O aluno acessa "Meu progresso".
2. O sistema busca as tentativas do aluno.
3. O sistema calcula acertos, erros e percentual de acerto por conteúdo.
4. O sistema exibe o resumo por conteúdo e os erros comuns mais frequentes.

**Extensões:**

- **2a. O aluno ainda não possui tentativas:** o sistema informa que não há dados e sugere resolver exercícios (UC1).

**Informação do projeto:** prioridade média; caso de uso relacionado: Resolver Exercício (UC1). O progresso é calculado a partir das tentativas e não é armazenado. Cada aluno vê apenas o próprio progresso.

**Situação:** planejado para a US09 (#45).

**Diferenças em relação à Modelagem - Parte I:**

- O detalhamento das tentativas de um conteúdo (passos 5 e 6 da modelagem) fica fora desta entrega.

## UC3 - Cadastrar Exercício

| Campo | Descrição |
|---|---|
| Contexto de uso | O administrador cadastra um novo exercício em um conteúdo, com seus erros comuns. |
| Escopo | Sistema ColumbinaMath |
| Requisitos relacionados | RF003 e RF004 |
| Condições prévias | Administrador autenticado; o conteúdo já está cadastrado (RF002). |
| Condição final com sucesso | O exercício e seus erros comuns estão registrados. |
| Condição final com falha | Nenhum dado é gravado. |
| Ator principal | Administrador |
| Gatilho | O administrador solicita cadastrar exercício. |

**Cenário principal de sucesso:**

1. O administrador solicita cadastrar exercício.
2. O sistema exibe o formulário com a lista de conteúdos.
3. O administrador informa conteúdo, enunciado, resposta correta e nível. A resolução passo a passo é opcional.
4. O sistema valida os campos obrigatórios.
5. O administrador informa um ou mais erros comuns (resposta errada e explicação).
6. O sistema valida os erros comuns.
7. O administrador confirma o cadastro.
8. O sistema grava o exercício e os erros comuns e exibe a mensagem de sucesso.

**Extensões:**

- **4a. Campos obrigatórios não preenchidos:** o sistema destaca os campos e retorna ao passo 3.
- **5a. O administrador não informa erros comuns:** o exercício é gravado sem erros comuns.
- **6a. Resposta errada do erro comum igual à resposta correta:** o sistema informa a inconsistência e retorna ao passo 5.
- **6b. Dois erros comuns com a mesma resposta errada:** o sistema informa a repetição e retorna ao passo 5.

**Informação do projeto:** prioridade alta.

**Situação:** atendido pelo painel administrativo do Django. No painel, as validações dos passos 4 e 6 acontecem juntas, quando o administrador confirma o cadastro.

**Diferenças em relação à Modelagem - Parte I:**

- A resolução passo a passo foi acrescentada ao cadastro.
- A extensão 6b foi acrescentada.
- Como os exercícios são de múltipla escolha, um exercício sem erros comuns (extensão 5a) teria só a alternativa correta. Todo exercício publicado tem erros comuns.

## UC4 - Acompanhar Desempenho da Turma

Fora desta entrega (Won't have this time). O caso de uso fica registrado como referência para uma versão futura, sem alterações em relação à Modelagem - Parte I.

| Campo | Descrição |
|---|---|
| Contexto de uso | O professor consulta o progresso dos alunos vinculados à sua turma. |
| Escopo | Sistema ColumbinaMath |
| Requisitos relacionados | RF007 e RF008 |
| Condições prévias | Professor autenticado; possui ao menos uma turma criada. |
| Condição final com sucesso | O desempenho da turma é exibido. |
| Condição final com falha | O desempenho não é exibido. |
| Ator principal | Professor |
| Gatilho | O professor acessa "Minhas turmas". |

**Cenário principal de sucesso:**

1. O professor acessa "Minhas turmas".
2. O sistema lista as turmas do professor.
3. O professor seleciona uma turma.
4. O sistema calcula o desempenho por conteúdo de cada aluno da turma.
5. O sistema exibe o resumo da turma e os conteúdos com mais erros.
6. O professor seleciona um aluno.
7. O sistema exibe o progresso individual do aluno (UC2).

**Extensões:**

- **2a. O professor não possui turmas:** o sistema oferece a opção de criar turma e gerar o código de acesso (RF007).
- **4a. A turma não possui alunos:** o sistema informa que não há alunos e exibe o código de acesso da turma.
- **6a. O professor tenta ver um aluno de outra turma:** o sistema nega o acesso (somente alunos vinculados).

**Informação do projeto:** prioridade baixa (funcionalidade opcional); caso de uso subordinado: Acompanhar Progresso (UC2).
