# Flashcards — Módulo 17: Geologia estrutural e deformação

**Módulo:** [[17-geologia-estrutural-modulo|Módulo 17]]
**Total:** 85 cards — 52 Basic + 33 Cloze
**Faixa de IDs:** `geologia-m17-fb001`–`B052` · `geologia-m17-fc001`–`C033`
**Status:** auditado — correções da auditoria científica de 2026-08-18 já propagadas (cards `B020`, `B031`, `B040`, `B046`, `C011`, `C019`, `C025`, `C030`). O card `geologia-m17-fb052` (sentido do V em dobra com caimento) foi acrescentado depois, fechando a lacuna de memorização apontada pela mesma auditoria; os cards `B049`, `B050` e `B051` tiveram o campo `aula` corrigido de `a06` para `a07` para refletir a divisão da antiga aula 06 em Parte 1 (aula 06 — atitude, regra do V, dobras em mapa) e Parte 2 (aula 07 — traço de falha, seção geológica, mergulho aparente). Ver [[17-geologia-estrutural-auditoria|relatório de auditoria]].
**Gerado em:** 2026-08-18, junto com as aulas e o questionário final.

## Arquivos para importar

| Arquivo | Tipo de nota no Anki | Campos |
|---|---|---|
| `17-geologia-estrutural-flashcards-basic.csv` | Basic | id, frente, verso, tags, aula, objetivo |
| `17-geologia-estrutural-flashcards-cloze.csv` | Cloze | id, texto, tags, aula, objetivo |

> [!tip] Importação no Anki Importe os dois **separadamente**. Marque "Campos separados por vírgula", ative "Permitir HTML nos campos" e mapeie `id` como primeiro campo. As tags são hierárquicas (`geologia::m17::dobras`).

## Distribuição

| Aula | Objetivo | Basic | Cloze | Total |
|---|---|---|---|---|
| a01 — Tensão e deformação | `oa01` | 8 | 5 | 13 |
| a02 — Comportamento rúptil e dúctil | `oa02` | 8 | 5 | 13 |
| a03 — Dobras: anatomia e classificação | `oa03` | 9 | 6 | 15 |
| a04 — Falhas: anatomia e classificação | `oa04` | 9 | 6 | 15 |
| a05 — Zonas de cisalhamento | `oa04` | 9 | 6 | 15 |
| a06 — Lendo o mapa, Parte 1 (atitude e padrões de afloramento) | `oa05` | 6 | 3 | 9 |
| a07 — Lendo o mapa, Parte 2 (falhas em mapa e seção geológica) | `oa05` | 3 | 2 | 5 |

Cobertura: os **cinco** objetivos do módulo têm card (oa04 cobre aulas 04 e 05, refletindo que o objetivo do módulo agrega falhas e zonas de cisalhamento; oa05 cobre aulas 06 e 07, as duas partes em que a antiga aula 06 foi dividida em 2026-08-18). Nenhum objetivo descoberto, nenhum card órfão.

## Critérios aplicados

- **Cards atômicos.** Cada card cobre um único fato ou relação — nunca duas perguntas empacotadas numa carta só.
- **Terminologia alinhada à aula.** Os termos usados nos cards (stress, strain, charneira, bloco de teto, milonito, mergulho aparente etc.) são exatamente os definidos no bloco "Vocabulário desta aula" de cada aula, sem sinônimo não introduzido.
- **Sem conteúdo deferido.** Nenhum card cobra álgebra de tensores, mecanismos microscópicos exatos de deformação cristalina, projeção estereográfica ou métodos avançados de construção de seção — tudo isso é deferido explicitamente pelas próprias aulas para cursos avançados de mecânica das rochas ou microtectônica.
- **Casos de confusão comum, cobrados de propósito.** Stress × strain (B001/B002/C001), anticlinal/sinclinal por idade × forma (B022/C012), bloco de teto × bloco de muro (B027/B028/C017), milonito × brecha de falha (B038/C024) — são os pares que as aulas nomeiam explicitamente como "erro comum", e por isso entraram no baralho.

## Migração no Anki

Este é o **primeiro baralho** do módulo 17. Não há card antigo a suspender ou apagar — importe os dois CSVs num deck limpo.

> [!warning] Se você já importou este baralho antes de 2026-08-18 Oito cards tiveram o verso corrigido pela auditoria científica (`B020`, `B031`, `B040`, `B046`, `C011`, `C019`, `C025`, `C030`). Reimportar o CSV **não** necessariamente sobrescreve cards já existentes no Anki: confira esses IDs manualmente, ou remova-os antes de reimportar. Um card com verso errado já em revisão não some sozinho. Depois dessa data, o card `geologia-m17-fb052` (sentido do V em dobra com caimento) foi acrescentado — é card novo, basta importar normalmente. Os campos `aula` de `B049`, `B050`, `B051`, `C032` e `C033` também foram atualizados de `a06` para `a07`; isso não muda frente/verso, então não afeta a revisão em andamento, só a tag de origem.
