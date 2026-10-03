# CONCLUÍDO: lacunas curriculares dos cursos de geologia vs. grade USP

**Criado:** 2026-08-29 (versão original) · **Encerrado:** 2026-08-29
**Estado: TAREFA CONCLUÍDA — não reabrir.** As quatro lacunas de disciplina obrigatória estão
planejadas. Nada aqui está pendente de execução.

> **Aviso sobre a versão anterior deste arquivo.** Ele dizia "planejamento não iniciado" e
> descrevia a tarefa como por fazer. Isso estava **errado**: o texto foi escrito *antes* da
> sessão de 2026-08-28, que executou o planejamento inteiro, e nunca foi atualizado depois
> dela. A sessão de 2026-08-29 acreditou nele, reabriu a tarefa e quase recriou módulos que
> já existiam. A fonte de verdade é sempre o `course-state.yaml` de cada curso, nunca um
> arquivo de retomada solto na raiz.

## O que foi feito, e onde está registrado

Quatro disciplinas **obrigatórias** do IGc-USP não tinham cobertura. Todas as quatro foram
fechadas **em nível de plano** — módulos e aulas existem como entradas `status: pending`,
nenhum conteúdo foi escrito, nada foi publicado no Notion.

| # | Lacuna | Disciplina USP | Curso | Módulo | Aulas pendentes | Data |
|---|--------|----------------|-------|--------|-----------------|------|
| 1 | Métodos numéricos | MAP0125 | `curso-geologia` | **30** (novo, trilha de apoio) | 5 | 2026-08-28 |
| 2 | Topografia geológica | PTR0201 | `curso-geologia` | **20** (expandido, 6 → 10 aulas) | 4 (aulas 07–10) | 2026-08-28 |
| 3 | Recursos energéticos | GAA0301 | `curso-geologia` | **29** (novo, área VII) | 4 | 2026-08-28 |
| 4 | Exploração e avaliação de recursos minerais | GAA0405 + GAA0404 | `curso-geologia-avancado` | **42** (novo, área X) | 8 | 2026-08-28 |

Registro completo: decisões de **2026-08-28** e **2026-08-29** nos dois `course-state.yaml`,
mais as seções correspondentes em cada `_contexto.md` e `_curso.md`.

Nenhum módulo foi renumerado em nenhuma das duas datas. Os módulos novos entraram no fim da
numeração (29, 30 no base; 42 no avançado) exatamente para não propagar ids.

## O que a sessão de 2026-08-29 acrescentou

- **Pré-requisito cruzado declarado dos dois lados.** O módulo 30 do curso base é
  pré-requisito de fato do módulo 23 do curso avançado (modelagem numérica geodinâmica).
  Só o curso base dizia isso. Agora o avançado também declara, no campo
  `cross_course_prerequisites` do módulo 23 e num aviso no hub. Mesmo tratamento dado ao
  módulo 42, que pressupõe o módulo 21 do curso base.
- **Campo novo no schema do plugin.** `cross_course_prerequisites` foi adicionado a
  `FFS-PluginStudy/schemas/course-state.schema.json` (definição `module`), porque
  `prerequisites` só aceita ids do próprio curso e o validador rejeita id estrangeiro.
  É documental: não entra no grafo nem na ordenação topológica.
- **Status explícito das optativas em limbo**, nos dois `_contexto.md`. Todas **adiadas**,
  nenhuma cortada — cortar é decisão de escopo do usuário.
- **Links quebrados repontados**: `../curso-geologia-gemologia/` → `../curso-geologia/`
  no `_curso.md` e no `_contexto.md` do curso avançado, quebrados desde 2026-08-25.

## O que continua pendente de DECISÃO DO USUÁRIO (nada a executar)

Registrado por extenso nos `_contexto.md`. Nenhum conteúdo deve ser gerado para estes temas
enquanto o usuário não decidir.

- **`curso-geologia`** — GMG0201 Geoconservação e Geoética · GAA0393 Geologia do Quaternário
  (+ GAA0291 Palinologia) · GAA0425 Pedologia Aplicada · GAA0311 Geoquímica Orgânica
  (+ GAA0202 Geoquímica Ambiental e Forense) · GAA0289 Terrenos Cársticos.
- **`curso-geologia-avancado`** — GAA0342 Petrografia e Diagênese de Rochas Sedimentares ·
  GMG0333 Introdução ao Magnetismo de Rocha.

Cortadas, com substituto declarado: PCC2110 · 4300270 · 4300357 · QFL0404 · BIO0103 ·
GMG0401 · GAA0304 · 0440335 · 0440500.

## Próximo passo real (quando o usuário aprovar a geração)

1. **`curso-geologia` módulo 30** (Métodos numéricos) — primeiro, porque destrava o módulo 23
   do curso avançado.
2. **`curso-geologia` M20 aulas 07–10** — e, depois de auditadas, **estender** o questionário
   e o baralho do M20, que hoje cobrem só as aulas 01–06 e os objetivos `oa01`–`oa06`.
3. **`curso-geologia` módulo 29** (Recursos energéticos).
4. **`curso-geologia-avancado`**: a fila de produção segue no **módulo 08** (Geotecnia
   ambiental); o módulo 42 entra quando a área X chegar, e deve ser estudado antes do 41.

## Pendências não relacionadas, ainda abertas

- Dashboards (`00-dashboard.md`, `00-progresso-do-aluno.md`) dos dois cursos não listam os
  módulos novos (29, 30, 42) nem as aulas 07–10 do M20. Regerar com
  `build_student_dashboard.py` — atenção à preservação das caixas já marcadas pelo aluno.
- Decisão adiada de 2026-08-19 no curso base: M17 e M19 ganham aula própria para
  `geologia-m17-oa01` / `geologia-m19-oa01`, ou apontam para as aulas 03 e 06 do M27?
- Auditoria cross-course dos módulos 20–25 contra 00–19 não rodou.
- Revisão didática pendente para vários módulos (20–25 e trilha de apoio).
- Páginas órfãs no Notion (módulos removidos + gemologia) para apagar à mão.
- Ruído pré-existente nos validadores, anterior a estas sessões e não causado por elas:
  manifestos de auditoria fora do schema, `status: complete` em vez de `completed` no curso
  avançado, CSVs de flashcards com vírgula em vez de ponto e vírgula, wikilinks para `.csv`,
  contagens `lessons.completed` divergentes.
