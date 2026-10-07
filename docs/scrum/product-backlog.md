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

## Visão geral das histórias

| Ordem | ID | História | Épico | MoSCoW | Estimativa | Status |
|---|---|---|---|---|---|---|
| - | US01 | Visualizar conteúdos | EP01 | Must | 2 SP | Concluído |
| - | US02 | Acessar uma explicação | EP01 | Must | 3 SP | Concluído |
| - | US03 | Resolver exercícios e receber correção explicada | EP02 | Must | 5 SP | Concluído |

US01, US02 e US03 foram concluídas na Sprint 1. Os próximos itens serão detalhados no planejamento da Sprint 2.

## Itens do Product Backlog

### US01 - Visualizar conteúdos

**User Story:**  
Como estudante, quero visualizar os conteúdos disponíveis para identificar os assuntos que posso estudar e reforçar.

**Épico:** EP01 — Revisão dos fundamentos   
**MoSCoW:** Must    
**Estimativa:** 2 SP    
**Status:** Concluído

**Critérios de aceitação:**
- Ao acessar a área de conteúdos, o estudante consegue visualizar os conteúdos disponíveis.
- Cada conteúdo apresenta um título que identifica o assunto abordado.
- O estudante consegue selecionar um dos conteúdos disponíveis.
- Ao selecionar um conteúdo, o estudante é direcionado para a página correspondente.

### US02 - Acessar uma explicação

**User Story:**
Como estudante, quero acessar uma explicação com exemplo resolvido sobre um conteúdo para compreender seus conceitos antes de praticá-los.

**Épico:** EP01 - Revisão dos fundamentos  
**MoSCoW:** Must  
**Estimativa:** 3 SP     
**Status:** Concluído

**Critérios de aceitação:**

- Ao acessar um conteúdo disponibilizado para estudo, o estudante visualiza seu título e a explicação correspondente.
- A explicação contém pelo menos um exemplo resolvido, com as etapas do cálculo e sua justificativa.
- O estudante consegue retornar à listagem de conteúdos.

### US03 - Resolver exercícios e receber correção explicada

**User Story:**
Como estudante, quero responder a exercícios de múltipla escolha e consultar a correção explicada para verificar minha compreensão e entender a resolução.

**Épico:** EP02 - Prática com correção explicada  
**MoSCoW:** Must  
**Estimativa:** 5 SP     
**Status:** Concluído

**Critérios de aceitação:**

- A partir da explicação de um conteúdo, o estudante consegue acessar os exercícios correspondentes.
- Cada exercício apresenta um enunciado e alternativas com exatamente uma resposta correta.
- O estudante consegue selecionar somente uma alternativa por exercício e enviar sua resposta.
- Se tentar enviar sem selecionar uma alternativa, recebe uma orientação para selecionar uma resposta, sem que isso seja considerado um erro matemático.
- Após o envio, o sistema informa imediatamente se a resposta está correta ou incorreta.
- Tanto no acerto quanto no erro, o sistema apresenta a alternativa correta e uma resolução explicada.
- O estudante consegue retornar à explicação do conteúdo.