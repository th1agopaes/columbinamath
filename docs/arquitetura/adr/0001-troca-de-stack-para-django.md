# ADR 0001: Trocar a stack Node/React por Pytho/Django

- **Status:** Aceito
- **Data:** 2026-11-04
- **Autor:** Thiago Paes de Barros Costa

## Contexto

A primeira versão do ColumbinaMath foi construída com React, Vite e TypeScript, e a Sprint 1 de extensão I foi entregue nela.

O projeto passou a ser usado em três disciplinas do quinto semestre: Engenharia de Software, Programação Web e Extensão I. Programação Web ensina o framework Django (templates, formulários, banco de dados, regras de negócio no back-end e serviços REST), conteúdo que a stack Node/React não cobre.

Manter duas stacks dobraria o trabalho. Além disso, no v1 as respostas corretas dos exercícios eram enviadas ao navegador, onde podiam ser consultadas pelo estudante.

## Decisão

Adotamos Python com Django como stack única do ColumbinaMath. A interface passa a ser feita com templates do Django (HTML e CSS) gerados no servidor, e a correção dos exercícios passa a acontecer no back-end. Node e React deixam de ser usados neste projeto.

Banco de dados, hospedagem e divisão em serviços serão registrados em ADRs próprios.

## Alternativas consideradas

- **Manter o v1 (Node/React) e criar um projeto Django separado para Programação Web.**
  Descartada: seriam dois projetos para manter, com o dobro do trabalho, sem que o código de um ajudasse o outro.
- **Usar React no front-end e Django apenas como API.**
  Descartada: mantém duas stacks e duas bases de código, e deixa de praticar templates e formulários do Django, conteúdo da Unidade II de Programação Web.

## Consequências

### Positivas

- Uma única stack para aprender e manter, cobrindo as três disciplinas no mesmo repositório.
- As respostas corretas deixam de ser enviadas ao navegador, porque a correção acontece no servidor.
- O Django já traz recursos prontos, como painel administrativo, ORM e autenticação.

### Negativas

- As issues #6 (migração para TypeScript) e #7 (publicação no GitHub Pages) precisam ser reescritas. O GitHub Pages só hospeda sites estáticos e não executa Django.
- A aplicação passa a precisar de um servidor para ficar acessível por link. A hospedagem ainda será decidida.

### O que muda no repositório

- O front-end React e o arquivo `.nvmrc` são removidos.
- O projeto Django é criado em `backend/`.
- Os conteúdos de Operações básicas são migrados de `conteudos.js` (v1) para o banco de dados.
