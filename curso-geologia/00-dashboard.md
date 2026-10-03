---
type: dashboard
curso: Geologia — do essencial ao avançado
---

# Dashboard — Geologia — do essencial ao avançado

## Estudo

- [[00-progresso-do-aluno.md|Marcar aulas assistidas]]
- [[_curso|Ver currículo completo e módulos]]
- [[_contexto|Ver regras e contexto do curso]]

> [!info] Como usar Marque as caixas na página **Progresso do aluno** depois de assistir a uma aula ou concluir uma avaliação. A página mantém o seu avanço pessoal separado do estado de produção do curso.

## Trilhas de estudo

| Trecho | Ordem | Status |
| --- | --- | --- |
| Módulos | 00 → 01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09 → 10 → 11 → 12 → 13 → 14 → 15 → 16 → 17 → 18 → 19 → 20 → 21 → 22 → 23 → 24 → 25 → **29** | 20 e 29 pendentes; os demais ✅ |
| Trilha de apoio (opcional) | 26 → 27 → 28 → 30 | ✅ |

## Produção por IA

| Conteúdo | Situação |
| --- | --- |
| Aulas publicadas localmente | 141 declaradas no estado — **subcontagem conhecida**, ver nota abaixo |
| Aulas planejadas | 196 no campo `estimated_lessons`; 200 somando `planned` módulo a módulo |
| Módulos do currículo | 31 |
| Módulos pendentes de conteúdo | 29 (Recursos energéticos) — mais as aulas 07–10 do módulo 20 |
| Fonte de verdade | [[course-state.yaml\|course-state.yaml]] |

> [!warning] Duas divergências de contagem, anteriores a esta rodada e ainda não resolvidas
> **Aulas escritas.** As aulas dos módulos 21 a 25 existem em disco, mas seus itens no `course-state.yaml` não declaram `status: completed` — por isso a contagem automática devolve 141 quando o número real é da ordem de 169. É a mesma inconsistência que o `validate_state.py` acusa como `lesson.count`. Corrigir isso é reparo de bookkeeping, fora do escopo de planejamento.
> **Aulas planejadas.** A soma de `planned` dá 200, contra 196 no campo `estimated_lessons`. As 4 de diferença são slots reservados nos módulos 17 (8 planejadas, 7 itens), 18 (7/6) e 19 (8/6), à espera da **decisão adiada de 2026-08-19**: se `geologia-m17-oa01` e `geologia-m19-oa01` ganham aula própria ou passam a apontar para as aulas 03 e 06 do módulo 27 (Física). Enquanto a decisão não sai, os dois números continuam legitimamente diferentes.

> [!warning] Não regerar estas duas páginas com `build_student_dashboard.py`
> O script só emite linha para aula que já tem arquivo em disco (`if not file: continue`). As 4 aulas novas do módulo 20, as 4 do módulo 29 e as 5 do módulo 30 sumiriam do Progresso do aluno, que é exatamente o que esta rodada precisava acrescentar. Por isso as entradas foram inseridas **à mão** em 2026-08-29, preservando intactas as marcas de progresso do aluno. O script continua seguro depois que as aulas existirem em disco.

> [!note] Planejamento de 2026-08-28/29 — conteúdo ainda não escrito
> Três lacunas contra a grade obrigatória do IGc-USP foram fechadas **em nível de plano**: topografia instrumental (PTR0201) nas aulas 07–10 do módulo 20, o módulo 29 (Recursos energéticos, GAA0301) e o módulo 30 (Métodos numéricos, MAP0125). As 13 aulas aparecem no Progresso do aluno marcadas como *pendentes de geração*. O questionário e o baralho do módulo 20 cobrem hoje só as aulas 01–06 e terão de ser **estendidos**. Ordem de produção quando aprovada: módulo 30 primeiro (destrava o módulo 23 do curso avançado), depois as aulas 07–10 do M20, depois o módulo 29.

## Módulos com aulas disponíveis

**Módulos**
- [[00-partida-do-zero/00-partida-do-zero-modulo|00 — Nivelamento opcional: kit de sobrevivência geológica]] · 6/6 aulas
- [[01-fundamentos-e-metodo/01-fundamentos-e-metodo-modulo|01 — Fundamentos e método das geociências]] · 6/6 aulas
- [[02-sistema-terra-tectonica/02-sistema-terra-tectonica-modulo|02 — Sistema Terra: estrutura interna e tectônica de placas]] · 9/9 aulas
- [[03-tempo-geologico-geocronologia/03-tempo-geologico-geocronologia-modulo|03 — Tempo geológico e geocronologia]] · 7/7 aulas
- [[04-cristalografia-quimica-minerais/04-cristalografia-quimica-minerais-modulo|04 — Química dos minerais e cristalografia]] · 0/7 aulas
- [[05-mineralogia-identificacao-optica/05-mineralogia-identificacao-optica-modulo|05 — Mineralogia: propriedades, identificação e óptica]] · 0/7 aulas
- [[06-rochas-igneas/06-rochas-igneas-modulo|06 — Rochas ígneas e magmatismo]] · 8/8 aulas
- [[07-rochas-sedimentares/07-rochas-sedimentares-modulo|07 — Rochas sedimentares]] · 7/7 aulas
- [[08-rochas-metamorficas/08-rochas-metamorficas-modulo|08 — Rochas metamórficas]] · 6/6 aulas
- [[09-geoquimica/09-geoquimica-modulo|09 — Geoquímica]] · 8/8 aulas
- [[10-vulcanologia/10-vulcanologia-modulo|10 — Vulcanologia]] · 6/6 aulas
- [[11-intemperismo-solos-geomorfologia/11-intemperismo-solos-geomorfologia-modulo|11 — Intemperismo, solos e geomorfologia]] · 7/7 aulas
- [[12-glaciologia/12-glaciologia-modulo|12 — Glaciologia]] · 5/5 aulas
- [[13-sedimentologia-ambientes/13-sedimentologia-ambientes-modulo|13 — Sedimentologia e ambientes deposicionais]] · 6/6 aulas
- [[14-estratigrafia-correlacao/14-estratigrafia-correlacao-modulo|14 — Estratigrafia e correlação]] · 6/6 aulas
- [[15-paleontologia-historia-vida/15-paleontologia-historia-vida-modulo|15 — Paleontologia e história da vida]] · 7/7 aulas
- [[16-geobiologia/16-geobiologia-modulo|16 — Geobiologia]] · 7/7 aulas
- [[17-geologia-estrutural/17-geologia-estrutural-modulo|17 — Geologia estrutural e deformação]] · 7/8 aulas
- [[18-tectonica-global-geodinamica/18-tectonica-global-geodinamica-modulo|18 — Tectônica global e geodinâmica]] · 6/7 aulas
- [[19-geofisica-metodos/19-geofisica-metodos-modulo|19 — Geofísica: métodos e imageamento da Terra]] · 6/8 aulas
- [[20-metodos-campo-mapeamento/20-metodos-campo-mapeamento-modulo|20 — Métodos de campo e mapeamento geológico]] · 6/10 aulas · aulas 07–10 (topografia instrumental) pendentes
- [[21-recursos-minerais-economica/21-recursos-minerais-economica-modulo|21 — Recursos minerais e geologia econômica]] · 0/6 aulas
- [[22-geologia-do-petroleo/22-geologia-do-petroleo-modulo|22 — Geologia do petróleo]] · 0/5 aulas
- [[23-oceanografia-geologica/23-oceanografia-geologica-modulo|23 — Oceanografia geológica (geologia marinha)]] · 0/5 aulas
- [[24-geologia-planetaria/24-geologia-planetaria-modulo|24 — Geologia planetária]] · 0/5 aulas
- [[25-geologia-do-brasil/25-geologia-do-brasil-modulo|25 — Geologia do Brasil]] · 0/7 aulas
- [[29-recursos-energeticos/29-recursos-energeticos-modulo|29 — Recursos energéticos]] · 0/4 aulas · pendente
- [[26-quimica-geociencias/26-quimica-geociencias-modulo|26 — Química para geociências: reações, soluções e equilíbrio]] · 5/5 aulas
- [[27-fisica-geociencias/27-fisica-geociencias-modulo|27 — Física para geociências: grandezas, forças e energia]] · 6/6 aulas
- [[28-matematica-geociencias/28-matematica-geociencias-modulo|28 — Matemática para geociências: vetores, trigonometria, funções e estatística]] · 4/4 aulas
- [[30-metodos-numericos-geociencias/30-metodos-numericos-geociencias-modulo|30 — Métodos numéricos para geociências: erro, sistemas lineares, interpolação e integração]] · 5/5 aulas · **pré-requisito do módulo 23 do curso avançado**
