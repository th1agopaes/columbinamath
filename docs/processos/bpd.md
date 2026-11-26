# Processos de negócio (BPD) - ColumbinaMath

Os diagramas de processo de negócio (BPD, *Business Process Diagram*) mostram, passo a passo, como o trabalho acontece entre as pessoas e o sistema. Cada raia é um participante; o processo começa no evento de início (círculo) e termina no evento de fim (círculo duplo).

O Mermaid não tem a notação BPMN completa. Os diagramas usam um fluxograma com as mesmas convenções: raias, eventos de início e fim, tarefas e decisões (losangos).

## Processo 1: estudar um conteúdo e praticar

Processo principal do produto (UC1 e UC2): o aluno estuda, responde e acompanha o próprio progresso.

```mermaid
flowchart LR
    subgraph aluno["Aluno"]
        direction TB
        inicio(("Início"))
        escolher["Escolher um conteúdo<br/>na trilha"]
        estudar["Ler a explicação e<br/>os exemplos resolvidos"]
        conectado{"Está conectado?"}
        entrar["Criar conta ou entrar"]
        responder["Escolher uma alternativa<br/>e enviar"]
        ler["Ler o feedback<br/>e a resolução"]
        continuar{"Tentar de novo<br/>ou seguir?"}
        verProgresso["Consultar<br/>Meu progresso"]
        fim((("Fim")))
    end

    subgraph sistema["ColumbinaMath"]
        direction TB
        corrigir["Corrigir a resposta<br/>no servidor"]
        acertou{"Acertou?"}
        explicarErro["Mostrar a explicação<br/>do erro comum"]
        parabenizar["Mostrar a mensagem<br/>de acerto"]
        registrar["Registrar a tentativa"]
        calcular["Calcular acertos, erros<br/>e percentual por conteúdo"]
    end

    inicio --> escolher --> estudar --> conectado
    conectado -- "não" --> entrar --> responder
    conectado -- "sim" --> responder
    responder --> corrigir --> acertou
    acertou -- "não" --> explicarErro --> registrar
    acertou -- "sim" --> parabenizar --> registrar
    registrar --> ler --> continuar
    continuar -- "tentar de novo ou<br/>próximo exercício" --> responder
    continuar -- "conteúdo concluído" --> verProgresso --> calcular --> fim
```

## Processo 2: acompanhar uma turma

Processo do professor (UC4): ele cria a turma, os alunos entram com o código, e ele acompanha o desempenho.

```mermaid
flowchart LR
    subgraph professor["Professor"]
        direction TB
        inicio(("Início"))
        criar["Criar a turma"]
        passar["Passar o código<br/>aos alunos"]
        abrir["Abrir a página<br/>da turma"]
        analisar["Analisar quem precisa de ajuda<br/>e os conteúdos com mais erros"]
        detalhar{"Ver um aluno<br/>em detalhe?"}
        fim((("Fim")))
    end

    subgraph alunos["Aluno"]
        direction TB
        informar["Informar o código<br/>na página Turmas"]
        praticar["Resolver exercícios<br/>(processo 1)"]
    end

    subgraph sistema["ColumbinaMath"]
        direction TB
        gerar["Gerar o código<br/>de acesso único"]
        validar{"Código existe?"}
        avisar["Avisar que o código<br/>não foi encontrado"]
        vincular["Vincular o aluno<br/>à turma"]
        desempenho["Calcular o desempenho<br/>de cada aluno"]
        progresso["Mostrar o progresso<br/>individual do aluno"]
    end

    inicio --> criar --> gerar --> passar --> informar --> validar
    validar -- "não" --> avisar --> informar
    validar -- "sim" --> vincular --> praticar
    praticar --> abrir --> desempenho --> analisar --> detalhar
    detalhar -- "sim" --> progresso --> analisar
    detalhar -- "não" --> fim
```

## Relação com os casos de uso

| Processo | Casos de uso | Requisitos |
|---|---|---|
| 1. Estudar um conteúdo e praticar | UC1 - Resolver Exercício e UC2 - Acompanhar Progresso | RF001, RF005, RF006 e RF009 |
| 2. Acompanhar uma turma | UC4 - Acompanhar Desempenho da Turma | RF007 e RF008 |
