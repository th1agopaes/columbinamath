# ADR 0003: Representar os perfis de usuário em uma tabela única, com modelos proxy

- **Status:** Aceito
- **Data:** 2026-11-25
- **Autor:** Thiago Paes de Barros Costa

## Contexto

O diagrama de classes (Modelagem - Parte II) tem a superclasse `Usuario` e três subclasses: `Aluno`, `Professor` e `Administrador`. Cada subclasse tem métodos próprios, como `Aluno.calcular_progresso()`, `Aluno.entrar_turma()` e `Professor.criar_turma()`.

No Django, uma herança entre modelos pode virar tabelas diferentes, e o modelo de usuário personalizado precisava ser definido antes da primeira migração (05/11).

## Decisão

Os três perfis ficam em uma única tabela, a do modelo `Usuario`, que herda de `AbstractUser` e tem o campo `tipo` (enumeração `TipoUsuario`).

`Aluno` e `Professor` são **modelos proxy**: classes do Python que usam a mesma tabela do `Usuario`, com um gerenciador que filtra pelo `tipo` e os métodos do diagrama de classes. `Administrador` não tem métodos próprios no diagrama, então é só um valor do campo `tipo`.

Correspondência com o diagrama de classes:

| Diagrama | Implementação |
|---|---|
| `Usuario.nome`, `email`, `senha`, `ativo`, `data_cadastro` | `first_name`, `email` (único), `password` (com hash), `is_active` e `date_joined`, herdados do `AbstractUser` |
| `Usuario.autenticar(email, senha)` | Login por e-mail (`USERNAME_FIELD = "email"`) |
| `Usuario.desativar()` | `Usuario.desativar()` |
| `Aluno` e `Professor` | Modelos proxy `Aluno` e `Professor` |
| `Aluno.serie` | Não implementado: dado pessoal desnecessário (RNF003, LGPD) |

As páginas de cada perfil são protegidas pelo decorador `perfil_obrigatorio`, que responde com acesso negado (HTTP 403) a outro perfil.

## Alternativas consideradas

- **Uma tabela por perfil (herança multitabela).**
  Descartada: cada consulta de aluno precisaria de uma junção com a tabela de usuários, e um usuário teria duas linhas para manter em sincronia.
- **Um modelo de perfil separado, ligado ao usuário por `OneToOneField`.**
  Descartada: os perfis não têm atributos próprios que justifiquem outra tabela.
- **Só o campo `tipo`, sem modelos proxy.**
  Descartada: os métodos de aluno e de professor ficariam todos no `Usuario`, longe do diagrama de classes.

## Consequências

### Positivas

- Uma tabela simples, sem junções, e o diagrama de classes continua reconhecível no código.
- Os métodos de cada perfil ficam na classe do perfil, como no diagrama.

### Negativas

- O `request.user` é sempre um `Usuario`. Para usar os métodos do perfil, a view busca o mesmo registro pela classe proxy (`Aluno.objects.get(pk=...)`).
- Salvar um objeto pela classe proxy força o `tipo` daquele perfil.
