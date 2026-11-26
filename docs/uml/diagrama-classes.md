# Diagrama de classes e modelo de dados - ColumbinaMath

Este documento mostra o modelo do sistema como ele foi implementado: o diagrama de classes (visão orientada a objetos) e o DER (visão do banco de dados). O diagrama de classes da modelagem original está na [Modelagem - Parte II](../requisitos/modelagem/modelagem-parte-2.pdf).

## Diagrama de classes

```mermaid
classDiagram
    direction TB

    class TipoUsuario {
        <<enumeration>>
        ALUNO
        PROFESSOR
        ADMIN
    }

    class NivelDificuldade {
        <<enumeration>>
        FACIL
        MEDIO
        DIFICIL
    }

    class Usuario {
        +str first_name
        +str email
        +str password
        +TipoUsuario tipo
        +bool is_active
        +datetime date_joined
        +desativar() void
    }

    class Aluno {
        <<proxy>>
        +calcular_progresso() dict
        +entrar_turma(codigo_acesso) bool
    }

    class Professor {
        <<proxy>>
        +criar_turma(nome) Turma
    }

    class Turma {
        +str nome
        +str codigo_acesso
        +datetime data_criacao
        +gerar_codigo_acesso()$ str
        +adicionar_aluno(aluno) void
        +possui_aluno(aluno) bool
        +calcular_desempenho() dict
    }

    class Conteudo {
        +str nome
        +str slug
        +str descricao
        +int ordem
        +str introducao
        +listar()$ QuerySet
        +proximo_exercicio(aluno) Exercicio
    }

    class Secao {
        +int ordem
        +str titulo
        +str explicacao
        +str exemplo
        +str passos
        +str resultado
        +str prova_real
    }

    class Exercicio {
        +str enunciado
        +str resposta_correta
        +NivelDificuldade nivel
        +str resolucao
        +verificar_resposta(resposta) bool
        +identificar_erro(resposta) ErroComum
        +alternativas() list
    }

    class ErroComum {
        +str resposta_errada
        +str explicacao
        +buscar(exercicio, resposta)$ ErroComum
    }

    class Tentativa {
        +str resposta_dada
        +bool correta
        +datetime data_hora
        +registrar(aluno, exercicio, resposta)$ Tentativa
        +filtrar(aluno, conteudo)$ QuerySet
    }

    Usuario <|-- Aluno
    Usuario <|-- Professor
    Usuario ..> TipoUsuario
    Exercicio ..> NivelDificuldade
    Professor "1" --> "0..*" Turma : cria
    Turma "0..*" -- "0..*" Aluno : participa
    Conteudo "1" *-- "0..*" Secao : explica
    Conteudo "1" *-- "0..*" Exercicio : possui
    Exercicio "1" *-- "0..*" ErroComum : prevê
    Aluno "1" --> "0..*" Tentativa : realiza
    Exercicio "1" --> "0..*" Tentativa : recebe
    ErroComum "0..1" --> "0..*" Tentativa : identificado em
```

### Como ler

- **Herança** (seta com triângulo): `Aluno` e `Professor` são tipos de `Usuario`.
- **Composição** (losango cheio): a parte não existe sem o todo. Ao excluir um conteúdo, seus exercícios e seções também são excluídos.
- **Associação** (seta simples) com multiplicidade: um aluno realiza de 0 a muitas tentativas (`0..*`); uma tentativa errada pode ter um erro comum (`0..1`).
- **Métodos sublinhados** (marcados com `$`) são de classe: funcionam sem um objeto, como `Turma.gerar_codigo_acesso()`.

### Diferenças em relação à Modelagem - Parte II

| Modelagem | Implementação | Por quê |
|---|---|---|
| `Aluno`, `Professor` e `Administrador` como subclasses | `Aluno` e `Professor` são modelos proxy da mesma tabela; `Administrador` é um valor de `tipo` | [ADR 0003](../arquitetura/adr/0003-perfis-de-usuario-em-tabela-unica.md) |
| `Usuario.nome`, `senha`, `ativo`, `data_cadastro` | `first_name`, `password` (com hash), `is_active` e `date_joined`, herdados do `AbstractUser` do Django | Recursos prontos e seguros do framework (RNF002) |
| `Usuario.autenticar(email, senha)` | Login do Django com o e-mail como identificador (`USERNAME_FIELD`) | Mesma regra, sem reimplementar a autenticação |
| `Aluno.serie` | Não implementado | Dado pessoal desnecessário (RNF003, LGPD) |
| `Conteudo.proximo_exercicio(aluno)` | Primeiro exercício que o aluno ainda não acertou | Botão "Continuar de onde parei" |
| - | `Secao`, `Exercicio.resolucao` e `Exercicio.alternativas()` | Explicação com exemplos resolvidos e exercícios de múltipla escolha |
| - | `Tentativa.registrar()` | Corrige a resposta e grava a tentativa num só lugar |

## Modelo de dados (DER)

As tabelas abaixo são as criadas pelas migrações do Django, no SQLite e no PostgreSQL. As tabelas internas do Django (sessões, permissões e grupos) foram omitidas.

```mermaid
erDiagram
    usuarios_usuario ||--o{ turmas_turma : "cria (professor)"
    usuarios_usuario ||--o{ turmas_turma_alunos : "participa (aluno)"
    turmas_turma ||--o{ turmas_turma_alunos : "reúne"
    usuarios_usuario ||--o{ progresso_tentativa : "realiza"
    conteudos_conteudo ||--o{ conteudos_secao : "tem"
    conteudos_conteudo ||--o{ conteudos_exercicio : "possui"
    conteudos_exercicio ||--o{ conteudos_errocomum : "prevê"
    conteudos_exercicio ||--o{ progresso_tentativa : "recebe"
    conteudos_errocomum |o--o{ progresso_tentativa : "identificado em"

    usuarios_usuario {
        bigint id PK
        varchar email UK
        varchar username UK
        varchar password
        varchar first_name
        varchar tipo
        boolean is_active
        boolean is_staff
        timestamp date_joined
    }

    turmas_turma {
        bigint id PK
        varchar nome
        varchar codigo_acesso UK
        bigint professor_id FK
        timestamp data_criacao
    }

    turmas_turma_alunos {
        bigint id PK
        bigint turma_id FK
        bigint usuario_id FK
    }

    conteudos_conteudo {
        bigint id PK
        varchar nome
        varchar slug UK
        varchar descricao
        smallint ordem
        text introducao
    }

    conteudos_secao {
        bigint id PK
        bigint conteudo_id FK
        smallint ordem
        varchar titulo
        text explicacao
        varchar exemplo
        text passos
        varchar resultado
        varchar prova_real
    }

    conteudos_exercicio {
        bigint id PK
        bigint conteudo_id FK
        text enunciado
        varchar resposta_correta
        varchar nivel
        text resolucao
    }

    conteudos_errocomum {
        bigint id PK
        bigint exercicio_id FK
        varchar resposta_errada
        text explicacao
    }

    progresso_tentativa {
        bigint id PK
        bigint aluno_id FK
        bigint exercicio_id FK
        bigint erro_comum_id FK "opcional"
        varchar resposta_dada
        boolean correta
        timestamp data_hora
    }
```

### Regras do banco

- `usuarios_usuario.email`, `conteudos_conteudo.slug` e `turmas_turma.codigo_acesso` são únicos.
- Um exercício não pode ter dois erros comuns com a mesma resposta errada (restrição única em `exercicio_id` e `resposta_errada`).
- Excluir um conteúdo exclui suas seções e exercícios; excluir um exercício exclui seus erros comuns e tentativas (`CASCADE`).
- Excluir um erro comum mantém as tentativas, com `erro_comum_id` vazio (`SET NULL`), para não apagar o histórico do aluno.
- O progresso e o desempenho não têm tabela: são calculados a partir de `progresso_tentativa`.
