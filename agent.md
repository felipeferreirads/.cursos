# Contexto do Projeto: Curso de Geologia & Gemologia

> Arquivo de contexto para agentes de IA. Leia isto antes de tocar em qualquer arquivo do curso.
> Última atualização: 2026-08-19

---

## 1. O que é este projeto

Um curso autodidata completo de Geologia e Gemologia, gerado e mantido por IA, organizado em 34 módulos (00–33) sob `curso-geologia-gemologia/`. O conteúdo é produzido com apoio de transcrições de vídeos e grades curriculares de referência, usando o plugin `estudo-geociencias` (instalado a partir de `FFS-PluginStudy/`).

**Regra de ouro:** não escreva aulas, questionários, fichas ou flashcards manualmente por conta própria — use as skills do plugin `estudo-geociencias` listadas na seção 4. Elas já encapsulam o formato, o estado do curso e as convenções esperadas.

---

## 2. Onde olhar primeiro (nesta ordem)

1. `curso-geologia-gemologia/course-state.yaml` — fonte da verdade do estado atual (o que existe, o que falta, o que está pendente de auditoria).
2. `curso-geologia-gemologia/00-dashboard.md` — painel de progresso legível por humano.
3. `curso-geologia-gemologia/_relatorio-lacunas-transcricoes.md` — o que falta transcrever/cobrir.
4. `curso-geologia-gemologia/_auditoria-transversal.md` — achados de correção científica ainda pendentes entre módulos.

Nunca assuma o estado do curso pela estrutura de pastas sozinha — `course-state.yaml` pode divergir do disco (por isso existe o validador estrutural, seção 4).

---

## 3. Estrutura de diretórios

### 3.1 Curso principal
`curso-geologia-gemologia/` — 34 módulos numerados `NN-tema-descritivo`:

`00-partida-do-zero`, `01-fundamentos-e-metodo`, `02-sistema-terra-tectonica`, `03-tempo-geologico-geocronologia`, `04-cristalografia-quimica-minerais`, `05-mineralogia-identificacao-optica`, `06-gemologia`, `07-rochas-igneas`, `08-rochas-sedimentares`, `09-rochas-metamorficas`, `10-geoquimica`, `11-vulcanologia`, `12-intemperismo-solos-geomorfologia`, `13-glaciologia`, `14-sedimentologia-ambientes`, `15-estratigrafia-correlacao`, `16-paleontologia-historia-vida`, `17-geobiologia`, `18-geologia-estrutural`, `19-tectonica-global-geodinamica`, `20-geofisica-metodos`, `21-metodos-campo-mapeamento`, `22-recursos-minerais-economica`, `23-geologia-do-petroleo`, `24-oceanografia-geologica`, `25-geologia-planetaria`, `26-geologia-do-brasil`, `27-geologia-ambiental-hidrogeologia`, `28-geologia-de-engenharia`, `29-geometalurgia`, `30-engenharia-de-petroleo`, `31-quimica-geociencias`, `32-fisica-geociencias`, `33-matematica-geociencias`.

Cada módulo é dividido internamente em **aulas** (≤30 min de estudo cada; assuntos maiores viram Parte 1, Parte 2...). Avaliação (questionário) e memorização (flashcards) vivem no nível do **módulo**, não da aula.

**Arquivos de controle na raiz do curso:**
| Arquivo | Conteúdo |
|---|---|
| `course-state.yaml` | Estado principal — sempre consultar antes de agir |
| `course-state.pre-repair.yaml` | Backup pré-reparo, só para diagnóstico |
| `00-dashboard.md` | Painel de progresso geral |
| `00-progresso-do-aluno.md` | Progresso detalhado do aluno |
| `_contexto.md` | Contexto geral do curso |
| `_curso.md` | Estrutura do curso |
| `_auditoria-transversal.md` | Achados de auditoria científica entre módulos |
| `_relatorio-lacunas-transcricoes.md` | Lacunas de transcrição/cobertura |

### 3.2 Plugin de geração (`FFS-PluginStudy/`)
Fonte do plugin `estudo-geociencias`, que expõe as skills da seção 4. Contém `agents/`, `skills/`, `templates/`, `schemas/`, `scripts/`, `prompts/`, `references/`, `evals/`, `tests/`, além de `AGENTS.md`, `CLAUDE.md`, `README.md`, `ROADMAP.md`, `BACKLOG-AREAS-ADIADAS.md`, `HANDOFF.md`.

**Repositório:** https://github.com/felipeferreirads/FFS-PluginStudy (em `.cursos` a pasta `FFS-PluginStudy/` é um submódulo/ponteiro e pode estar vazia; se estiver, clone o repositório acima antes de usar as skills).

**E-mail noreply do GitHub (autoria de commits):** `300224651+felipeferreirads@users.noreply.github.com` (conta `felipeferreirads`). Use-o como e-mail de autor nos commits para não expor o e-mail pessoal.

### 3.3 `GradeCurricular/`
Grades universitárias de referência. Atualmente: `Geologia-USP/` (`Obrigatoria/`, `Optativa Livre/`, `grade.json`) — a referência principal para escopo curricular. Há um script reutilizável em `_ferramentas/` para extrair grade+ementas de qualquer curso da USP (ver memória `reference_usp_grade_scraper`).

### 3.4 `Transcricoes/`
Transcrições de vídeos usadas como matéria-prima de conteúdo, por canal:
`EN-CrashCourseGeology/`, `EN-Geology101-Willsey/`, `EN-ProfessorDaveExplains/`, `Geologia-Geomorfologia-Ricardo-Marcilio/` (PT), `PT-EarthAndSpaceSciencesX/` (PT), `Sistema-Terra-USP/` (PT).
Scripts: `_extract.py`, `_extract2.py`, `_retry_slow*.py`. Logs: `*_log.txt`. Mapeamento transcrição→módulo: `mapa-transcricoes-modulos.md`.

### 3.5 Outros
`.obsidian/` (vault Obsidian — o `.md` local já É o vault, não precisa publicar nele), `.course-tools/`, `.ffs-deps/`, `_ferramentas/`.

---

## 4. Qual skill usar para cada pedido

O plugin `estudo-geociencias` já cobre praticamente todo fluxo de trabalho. Mapeamento direto pedido → skill:

| O usuário pede... | Skill |
|---|---|
| Montar/retomar um curso completo em módulos | `gerador-de-curso-modular` |
| Planejar/estruturar o currículo antes de gerar conteúdo | `planejador-curricular` |
| Uma aula avulsa (≤30 min) sobre um tema | `gerador-de-aula` |
| Questionário/quiz/simulado de um módulo | `gerador-de-questionarios` |
| Flashcards/baralho de revisão de um módulo | `gerador-de-flashcards` |
| Ficha de mineral, rocha, fóssil, formação geológica, meteorito, tempo geológico | `ficha-de-*` correspondente |
| Comparar dois conceitos/materiais | `comparador-geocientifico` |
| Identificar espécime por foto | `identificador-de-especime` |
| Chave de identificação | `gerador-de-chave-de-identificacao` |
| Glossário | `gerador-de-glossario` |
| Exercícios/roteiro de campo | `gerador-de-praticas` |
| Catalogar exemplar físico da coleção | `catalogador-de-colecao` |
| Verificar correção científica ("tem erro?", "audita") | `auditor-cientifico` (modos `audit` / `audit-and-fix` / `cross-course`) |
| Verificar qualidade pedagógica ("está confuso?") | `revisor-didatico` (modos `review` / `review-and-fix`) |
| Validar integridade estrutural (arquivos, links, estado) | `validador-estrutural-do-curso` |
| Aula falada / modo tutor por voz | `tutor-de-voz` (modos `briefing` / `sessao` / `colheita`) |
| Publicar ou sincronizar com Notion | `publicador-notion` (modos `push` / `pull` / `sync` / `status`) |

Regra de sequência: `planejador-curricular` decide a estrutura → `gerador-de-aula`/`gerador-de-curso-modular` escreve conteúdo → `auditor-cientifico` e `revisor-didatico` revisam → `validador-estrutural-do-curso` confere integridade → `publicador-notion` publica. Não pule a validação estrutural antes de dar um módulo por concluído ou exportar.

---

## 5. Convenções de nomenclatura

- Módulos: `NN-tema-descritivo` (ex.: `06-gemologia`)
- Arquivos de controle: prefixo `_` (ex.: `_contexto.md`)
- Estado: `course-state.yaml`
- Logs: `<script>_log.txt`
- Scripts Python: prefixo `_` (ex.: `_extract.py`)

---

## 6. Caminhos absolutos

- Curso: `C:\Users\Feliperiano\Documents\.Cursos\curso-geologia-gemologia`
- Plugin: `C:\Users\Feliperiano\Documents\.Cursos\FFS-PluginStudy`
- Grades: `C:\Users\Feliperiano\Documents\.Cursos\GradeCurricular`
- Transcrições: `C:\Users\Feliperiano\Documents\.Cursos\Transcricoes`
- Ferramentas: `C:\Users\Feliperiano\Documents\.Cursos\_ferramentas`

---

## 7. Notas operacionais para agentes

- Sempre leia `course-state.yaml` antes de gerar ou alterar conteúdo — ele pode divergir da estrutura em disco.
- A grade da USP (`GradeCurricular/Geologia-USP/grade.json`) é a referência curricular principal; use-a para checar escopo e ordem de pré-requisitos.
- Nunca escreva aulas/fichas/questionários fora das skills do plugin — elas mantêm formato, estado e convenções consistentes entre módulos.
- Depois de qualquer geração em lote, rode `validador-estrutural-do-curso` antes de considerar o trabalho concluído.
- `auditor-cientifico` verifica se está *correto*; `revisor-didatico` verifica se está *bem ensinado*. São checagens independentes — rode as duas quando o pedido for "revisar" sem qualificação.

---

*Atualize este arquivo sempre que a estrutura de diretórios, o número de módulos ou o mapeamento de skills mudar de forma significativa.*
