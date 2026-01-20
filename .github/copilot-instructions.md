# Descrição do Projeto

Este projeto é um site educacional para compartilhar tarefas de casa e exercícios de programação com estudantes. Os estudantes podem navegar, visualizar e baixar tarefas diretamente do portal.

## Estrutura do Projeto

- [`assignments/`](../assignments/) Cada tarefa de casa é armazenada em sua própria subpasta com uma estrutura consistente.
- [`templates/`](../templates/) Templates reutilizáveis para novo conteúdo
- [`assets/`](../assets/) Contém os recursos do site incluindo CSS, JavaScript, imagens e arquivos de configuração
- [`index.html`](../index.html) A página principal do site que serve como um portal estático para navegar e visualizar tarefas. O conteúdo é configurável através do arquivo [`config.json`](../config.json) para gerar dinamicamente listas e detalhes de tarefas.

## Diretrizes do Projeto

- Manter estilo consistente em todas as páginas
- Manter nomes de arquivos e pastas descritivos e organizados

## Padrões de Commit

Utilizamos o padrão "Conventional Commits" neste projeto para manter um histórico de commits claro e consistente. O formato geral recomendado é:

```
<type>(scope?): <description>
```

Tipos comuns e exemplos:

- `feat: adicionar página de tarefas`
- `fix: corrigir carregamento das assignments`
- `docs: atualizar README com instruções`
- `refactor: refatorar script.js para modularização`
- `perf: melhorar desempenho do carregamento`
- `test: adicionar testes unitários`
- `chore: atualizar dependências`

Exemplos com escopo e breaking change:

- `feat(auth): adicionar login via OAuth`
- `feat!: alterar assinatura da função loadAssignments()` (BREAKING CHANGE: mudança incompatível na API)

Para mudanças incompatíveis, inclua `BREAKING CHANGE: descrição` no corpo do commit.

## Padrões Educacionais

Ao gerar conteúdo para este projeto:

- **Focado em aprendizado**: Todo conteúdo deve ser projetado com objetivos de aprendizado claros e níveis de dificuldade apropriados
- **Amigável para estudantes**: Use linguagem clara e encorajadora que motiva os estudantes

