---
type: dashboard
curso: Geologia Avançada — Especializações além da graduação
---

# Dashboard — Geologia Avançada — Especializações além da graduação

## Estudo

- [[00-progresso-do-aluno.md|Marcar aulas assistidas (198 aulas disponíveis)]]
- [[_curso|Ver currículo completo e módulos]]
- [[_contexto|Ver regras e contexto do curso]]

> [!info] Como usar Marque as caixas na página **Progresso do aluno** depois de assistir a uma aula ou concluir uma avaliação. A página mantém o seu avanço pessoal separado do estado de produção do curso.

## Trilhas de estudo

| Trecho | Ordem | Status |
| --- | --- | --- |
| IX. Especializações aplicadas | 01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09 → 10 → 11 → 12 | 01–12 concluídos; área IX completa |
| X. Métodos quantitativos e geoinformação | 13 → 14 → 15 → 16 → 17 → 18 → 19 → 20 → 21 → 22 → **42** → 23 → 24 → 25 | 13–25 concluídos (últimos: 23 em 2026-09-20, 24 em 2026-09-21, 25 em 2026-09-21); 42 pendente |
| XI. Geoquímica isotópica e petrogênese avançada | 26 → 27 → 28 → 29 → 30 → 31 → 32 → 33 → 34 → 35 → 36 → 37 | 26–36 concluídos (26 em 2026-09-22, 27-31 em 2026-09-23/24, 32 em 2026-09-28, 33–35 em 2026-09-29, 36 em 2026-09-30); 37 pendente |
| XII. Síntese estrutural e integração | 38 → 39 → 40 → 41 | 40 concluído; 38, 39 e 41 pendentes |

## Produção por IA

| Conteúdo | Situação |
| --- | --- |
| Aulas publicadas localmente | 252 (soma direta de `lessons.completed` nos 37 módulos com `status: completed`, verificada via `course-state.yaml` em 2026-09-30) |
| Aulas planejadas | 283 |
| Módulos do currículo | 42 |
| Módulos concluídos | 37 / 42 (módulos 01–36 e 40) |
| Áreas temáticas | 4 |
| Questionários gerados | 416 (adição: módulo 36: questionário único = 17 q) |
| Baralhos de flashcards gerados | 36 / 42 — 2.785 cards totais (adição: módulo 36: 48 cards, densidade 12 cards/aula) |
| Auditorias científicas concluídas | 26 / 42 — todas aprovadas, 0 achados 🔴/🟠 em aberto |
| Revisões didáticas concluídas | 26 / 42 — todas aprovadas |
| Fonte de verdade | `course-state.yaml` |

> [!note] Planejamento de 2026-08-28/29 — módulo 42 criado, conteúdo ainda não escrito
> O **módulo 42 — Exploração mineral e avaliação de recursos** (área X, 8 aulas) fechou a última lacuna de disciplina obrigatória do IGc-USP sem cobertura (GAA0405 + GAA0404). Está **só planejado**: as 8 aulas aparecem no Progresso do aluno marcadas como *pendentes de geração*. Recebeu o número 42 para não renumerar nenhum módulo existente; na listagem aparece na sua posição de estudo, logo após o 22.
>
> Duas restrições de ordem que o grafo formal não declara: **estudar o 42 antes do 41** (capstone), e **gerar o módulo 30 do curso base antes do módulo 23** daqui, que pressupõe cálculo numérico. A fila de produção continua no módulo 13.

> [!warning] Não regerar estas duas páginas com `build_student_dashboard.py`
> O script descarta toda aula que ainda não tem arquivo em disco — as 8 aulas do módulo 42 e as de todos os outros módulos pendentes sumiriam do Progresso do aluno (cerca de 216 linhas), e as quatro áreas temáticas colapsariam numa lista única. As métricas curadas desta página (questionários, baralhos, auditorias, revisões) também não são derivadas pelo script. As entradas do módulo 42 foram inseridas **à mão** em 2026-08-29 por esse motivo.
>
> **Atualização de 2026-09-11:** o enum `status: complete` → `completed` foi corrigido em todo o `course-state.yaml` (193 ocorrências), então esse desvio específico não existe mais. O número de aulas escritas nesta página (113, atualizado nesta mesma data) continua sendo mantido à mão pelo motivo acima — o script ainda descartaria os módulos pendentes.

## Módulos

**IX. Especializações aplicadas**

- [[01-hidrogeologia-recursos-hidricos/01-hidrogeologia-recursos-hidricos-modulo|01 — Hidrogeologia e recursos hídricos]] · **7/7 aulas** · auditoria ✅ · revisão didática ✅ · 3 questionários · 56 flashcards
- [[02-hidrogeoquimica/02-hidrogeoquimica-modulo|02 — Hidrogeoquímica]] · **5/5 aulas** · auditoria ✅ · revisão didática ✅ · 1 questionário · 50 flashcards
- [[03-contaminacao-aguas-subterraneas/03-contaminacao-aguas-subterraneas-modulo|03 — Contaminação dos recursos hídricos subterrâneos]] · **5/5 aulas** · auditoria ✅ · revisão didática ✅ · 1 questionário · 50 flashcards
- [[04-exploracao-gestao-aguas-subterraneas/04-exploracao-gestao-aguas-subterraneas-modulo|04 — Exploração, explotação e gestão dos recursos hídricos subterrâneos]] · **4/4 aulas** · auditoria ✅ · revisão didática ✅ · 1 questionário · 44 flashcards
- [[05-mecanica-de-rochas/05-mecanica-de-rochas-modulo|05 — Mecânica de rochas]] · **7/7 aulas** · auditoria ✅ · revisão didática ✅ · 3 questionários · 60 flashcards
- [[06-elementos-de-geomecanica/06-elementos-de-geomecanica-modulo|06 — Elementos de geomecânica]] · **6/6 aulas** · auditoria ✅ · revisão didática ✅ · 3 questionários · 56 flashcards
- [[07-mapeamento-geotecnico/07-mapeamento-geotecnico-modulo|07 — Metodologia de mapeamento geotécnico]] · **4/4 aulas** · auditoria ✅ · revisão didática ✅ · 1 questionário · 44 flashcards
- [[08-geotecnia-ambiental/08-geotecnia-ambiental-modulo|08 — Geotecnia ambiental]] · **6/6 aulas** · auditoria ✅ · revisão didática ✅ · 3 questionários · 54 flashcards
- [[09-geometalurgia/09-geometalurgia-modulo|09 — Geometalurgia]] · **6/6 aulas** · auditoria ✅ · revisão didática ✅ · 3 questionários · 95 flashcards
- [[10-tectonica-de-bacias-sedimentares/10-tectonica-de-bacias-sedimentares-modulo|10 — Tectônica de bacias sedimentares]] · **5/5 aulas** · auditoria ✅ · revisão didática ✅ · 1 questionário · 110 flashcards
- [[11-sismoestratigrafia/11-sismoestratigrafia-modulo|11 — Sismoestratigrafia]] · **6/6 aulas** · auditoria ✅ · revisão didática ✅ · 3 questionários · 132 flashcards
- [[12-engenharia-de-petroleo/12-engenharia-de-petroleo-modulo|12 — Engenharia de petróleo]] · **5/5 aulas** · auditoria ✅ · revisão didática ✅ · 1 questionário · 239 flashcards

**X. Métodos quantitativos e geoinformação**

- [[13-geoprocessamento/13-geoprocessamento-modulo|13 — Geoprocessamento]] · **7/7 aulas** · auditoria ✅ · revisão didática ✅ · questionário ✅ (38 q) · flashcards ✅ (78)
- [[14-sensoriamento-remoto/14-sensoriamento-remoto-modulo|14 — Sensoriamento remoto]] · **7/7 aulas** · auditoria ✅ · revisão didática ✅ · questionário ✅ (39 q) · flashcards ✅ (96)
- [[15-petrofisica/15-petrofisica-modulo|15 — Introdução à petrofísica]] · **4/4 aulas** · auditoria ✅ · revisão didática ✅ · questionário ✅ (16 q) · flashcards ✅ (95)
- [[16-aerogeofisica/16-aerogeofisica-modulo|16 — Introdução à aerogeofísica]] · **5/5 aulas** · auditoria ✅ · revisão didática ✅ · questionário ✅ (18 q) · flashcards ✅ (104)
- [[17-geofisica-marinha-bacias-sedimentares/17-geofisica-marinha-bacias-sedimentares-modulo|17 — Geofísica marinha e de bacias sedimentares]] · **6/6 aulas** · auditoria ✅ · revisão didática ✅ · questionário ✅ (20 q) · flashcards ✅ (56)
- [[18-geofisica-america-do-sul/18-geofisica-america-do-sul-modulo|18 — Geofísica da América do Sul]] · **5/5 aulas** · auditoria ✅ · revisão didática ✅ · questionário ✅ (18 q) · flashcards ✅ (68)
- [[19-geofisica-exploracao-mineral/19-geofisica-exploracao-mineral-modulo|19 — Geofísica aplicada na exploração mineral]] · **7/7 aulas** · auditoria ✅ · revisão didática ✅ · questionário ✅ (47 q) · flashcards ✅ (50)
- [[20-geoestatistica/20-geoestatistica-modulo|20 — Introdução à geoestatística]] · **5/5 aulas** · auditoria ✅ · revisão didática ✅ · questionário ✅ (20 q) · flashcards ✅ (45)
- [[21-modelagem-geoestatistica-depositos-minerais/21-modelagem-geoestatistica-depositos-minerais-modulo|21 — Modelagem geoestatística de depósitos minerais]] · **6/6 aulas** · auditoria ✅ · revisão didática ✅ · questionário ✅ (19 q) · flashcards ✅ (30)
- [[22-modelagem-geologica-3d/22-modelagem-geologica-3d-modulo|22 — Modelagem geológica 3D]] · **6/6 aulas** · auditoria ✅ · revisão didática ✅ · questionário ✅ (15 q) · flashcards ✅ (56)
- [[42-exploracao-mineral-avaliacao-de-recursos/42-exploracao-mineral-avaliacao-de-recursos-modulo|42 — Exploração mineral e avaliação de recursos]] · 0/8 aulas · **estudar antes do 41**
- [[23-modelagem-numerica-geodinamica/23-modelagem-numerica-geodinamica-modulo|23 — Introdução à modelagem numérica geodinâmica]] · **9/9 aulas** · auditoria ✅ · revisão didática ✅ · questionário ✅ (41 q) · flashcards ✅ (87)
- [[24-machine-learning-geociencias/24-machine-learning-geociencias-modulo|24 — Fundamentos e aplicações de machine learning em geociências]] · **7/7 aulas** · auditoria ✅ · revisão didática ✅ · questionário ✅ (3 parciais+final, 42 q) · flashcards ✅ (56)
- [[25-aquisicao-digital-ia-geociencias/25-aquisicao-digital-ia-geociencias-modulo|25 — Aquisição de dados digitais e inteligência artificial em geociências]] · **5/5 aulas** · auditoria ✅ · revisão didática ✅ · questionário ✅ (15 q) · flashcards ✅ (45)

**XI. Geoquímica isotópica e petrogênese avançada**

- [[26-geologia-isotopica-aplicada/26-geologia-isotopica-aplicada-modulo|26 — Geologia isotópica aplicada]] · **7/7 aulas** · auditoria ✅ (1🔵 em aberto, não bloqueante) · revisão didática ✅ (1🔴 em aberto, não bloqueante — paleoclimatologia sem cobertura) · questionário ✅ (2 parciais+final, 32 q) · flashcards ✅ (100)
- [[27-petrocronologia/27-petrocronologia-modulo|27 — Introdução à petrocronologia]] · **7/7 aulas** · auditoria ✅ · revisão didática ✅ · questionário ✅ (2 parciais+final, 32 q) · flashcards ✅ (88)
- [[28-analise-instrumental-i/28-analise-instrumental-i-modulo|28 — Análise instrumental I]] · **6/6 aulas** · auditoria ✅ · revisão didática ✅ · questionário ✅ (17 q) · flashcards ✅ (62)
- [[29-granitos-no-ciclo-de-wilson/29-granitos-no-ciclo-de-wilson-modulo|29 — Granitos no ciclo de Wilson]] · **6/6 aulas** · auditoria ✅ · revisão didática ✅ · questionário ✅ (18 q) · flashcards ✅ (31) · **CONCLUÍDO**
- [[30-kimberlitos-carbonatitos/30-kimberlitos-carbonatitos-modulo|30 — Petrologia de kimberlitos e carbonatitos e mineralizações associadas]] · **6/6 aulas** · auditoria ✅ · revisão didática ✅ · questionário ✅ (19 q) · flashcards ✅ (50) · **CONCLUÍDO**
- [[31-rochas-igneas-alcalinas/31-rochas-igneas-alcalinas-modulo|31 — Rochas ígneas alcalinas: petrologia e mineralizações]] · **7/7 aulas** · auditoria ✅ · revisão didática ✅ · questionário ✅ (3: 2 parciais + 1 final, 31 q) · flashcards ✅ (53) · **CONCLUÍDO**
- [[32-pegmatitos/32-pegmatitos-modulo|32 — Pegmatitos: da gênese à exploração]] · **26/26 aulas** · auditoria ✅ · revisão didática ✅ · questionário ✅ (5 parciais + final, 120 q) · flashcards ✅ (61) · **CONCLUÍDO**
- [[33-intrusoes-acamadadas/33-intrusoes-acamadadas-modulo|33 — Petrologia de intrusões acamadadas e processos ígneos de mineralização]] · **8/8 aulas** · auditoria ✅ · revisão didática ✅ · questionário ✅ (2 parciais+final, 43 q) · flashcards ✅ (81) · **CONCLUÍDO**
- [[34-sistemas-hidrotermais-metalogenese/34-sistemas-hidrotermais-metalogenese-modulo|34 — Sistemas hidrotermais e metalogênese]] · **10/10 aulas** · auditoria ✅ · revisão didática ✅ · questionário ✅ (2 parciais+final, 43 q) · flashcards ✅ (100 cards)
- [[35-vulcanismo-mineralizacoes-associadas/35-vulcanismo-mineralizacoes-associadas-modulo|35 — Vulcanismo e mineralizações associadas]] · **6/6 aulas** · auditoria ✅ · revisão didática ✅ · questionário ✅ (único, 20 q) · flashcards ✅ (61 cards)
- [[36-microscopia-de-minerios/36-microscopia-de-minerios-modulo|36 — Microscopia de minérios]] · **4/4 aulas** · auditoria ✅ · revisão didática ✅ · questionário ✅ (único, 17 q) · flashcards ✅ (48 cards)
- [[37-petrografia-de-minerio/37-petrografia-de-minerio-modulo|37 — Petrografia de minério]] · 0/6 aulas

**XII. Síntese estrutural e integração**

- [[38-geologia-estrutural-quantitativa/38-geologia-estrutural-quantitativa-modulo|38 — Geologia estrutural quantitativa]] · 0/5 aulas
- [[39-analise-textural-de-rochas/39-analise-textural-de-rochas-modulo|39 — Análise textural de rochas: técnicas e aplicações]] · 0/8 aulas
- [[40-mineralogia-dos-tectossilicatos/40-mineralogia-dos-tectossilicatos-modulo|40 — Mineralogia dos tectossilicatos: cristaloquímica, óptica e relações de fases]] · **14/14 aulas** · auditoria ✅ · revisão didática ✅ · 3 questionários · 96 flashcards
- [[41-estudos-integrados-projetos-em-geologia-aplicada/41-estudos-integrados-projetos-em-geologia-aplicada-modulo|41 — Estudos integrados: projetos em geologia aplicada]] · 0/4 aulas
