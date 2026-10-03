# Flashcards — Módulo 19: Geofísica: métodos e imageamento da Terra

**Módulo:** [[19-geofisica-metodos-modulo|Módulo 19]]
**Total:** 96 cards — 60 Basic + 36 Cloze
**Faixa de IDs:** `geologia-m19-fb001`–`fb060` · `geologia-m19-fc001`–`fc036`
**Gerado em:** 2026-08-18, a partir das seis aulas do módulo.

> [!info] Primeira geração O módulo 19 nunca teve baralho. Importe os dois CSVs em deck limpo. Este baralho foi gerado **antes** da auditoria científica; a auditoria foi concluída em 2026-08-18 ([[19-geofisica-metodos-auditoria|relatório]]) e três cards foram corrigidos: `fb008` (magnitude mede o tamanho do terremoto na fonte, não a energia) e `fb020` + `fc012` (identificação histórica do Moho). Se você já importou o baralho antes desta data, corrija ou apague esses três cards à mão: reimportar o CSV não sobrescreve com segurança cards já em revisão no Anki. A revisão didática do módulo segue pendente.

## Arquivos para importar

| Arquivo | Tipo de nota no Anki | Campos |
|---|---|---|
| `19-geofisica-metodos-flashcards-basic.csv` | Basic | id, frente, verso, tags, objetivo, aula, dificuldade, fonte |
| `19-geofisica-metodos-flashcards-cloze.csv` | Cloze | id, texto, extra, tags, objetivo, aula, dificuldade, fonte |

> [!tip] Importação no Anki Importe os dois **separadamente**. Separador `;`, encoding UTF-8 sem BOM. Marque "Permitir HTML nos campos" e mapeie `id` como primeiro campo (oculto). As tags são hierárquicas (`geologia::geofisica::sismologia`). Todas as lacunas Cloze usam a sintaxe numerada `{{cN::texto}}`.

## Distribuição

| Aula | Objetivo | Basic | Cloze | Total |
|---|---|---:|---:|---|
| a01 — Sismologia e ondas sísmicas | `oa01` | 10 | 6 | 16 |
| a02 — Sísmica de reflexão e refração | `oa02` | 10 | 6 | 16 |
| a03 — Gravimetria | `oa03` | 10 | 5 | 15 |
| a04 — Magnetometria | `oa03` | 10 | 6 | 16 |
| a05 — Métodos elétricos, EM e geotérmicos | `oa04` | 10 | 6 | 16 |
| a06 — Perfilagem de poços e integração | `oa05` | 10 | 7 | 17 |

Cobertura: os cinco objetivos do módulo têm cards, com `oa03` recebendo o dobro de cards Basic (20) porque cobre duas aulas inteiras (gravimetria e magnetometria) — o mesmo critério aplicado no questionário final do módulo. Nos Cloze a distribuição não é exatamente 6 por aula: `oa03` soma 11 (5 da a03 + 6 da a04) e a a06 tem 7.

## Critérios aplicados

- **Cards atômicos, um fato por card.** Nenhum card exige lembrar duas definições ao mesmo tempo, exceto onde a distinção em si é o conteúdo (ex.: `fb001`, P × S; `fc031`, GR alto × baixo).
- **A não unicidade dos métodos potenciais tem cards próprios.** `fb029`, `fb030`, `fb039`, `fc017` e `fc023` existem porque é a ideia mais fácil de esquecer e a mais citada erroneamente como se anomalia isolada fosse prova — o mesmo ponto que o questionário final do módulo testa pesadamente.
- **Valores numéricos aparecem em ordem de grandeza, não como constante fechada.** Temperatura de Curie (~580 °C), gradiente geotérmico (~25–30 °C/km), fator de energia por grau Mw (~32×) e densidade padrão da Bouguer (~2,67 g/cm³) são consistentemente marcados com "cerca de"/"aproximadamente".
- **A integração de métodos, tema de fechamento da aula 06, tem cards que apontam de volta para os métodos anteriores** (`fb060`, `fc036`), reforçando que nenhuma técnica do módulo é lida como autossuficiente.

## Amostra (tabela de conferência)

| ID | Frente | Verso |
|---|---|---|
| fb001 | Diferença de propagação entre onda P e onda S | P atravessa qualquer meio; S só atravessa sólidos |
| fb010 | O que é a zona de sombra sísmica e o que revelou | Faixa sem S além de ~103°; revelou núcleo externo líquido |
| fb022 | O que indica uma anomalia gravimétrica positiva | Excesso de massa/densidade em profundidade |
| fb029 | O que é a não unicidade dos métodos potenciais | Mesma anomalia pode vir de infinitas combinações de forma/profundidade/contraste |
| fb033 | Mineral que domina a resposta magnética das rochas | Magnetita, mesmo em pequena proporção |
| fb041 | O que controla a resistividade de rocha porosa | Água nos poros e sua salinidade |
| fb058 | O que é um sismograma sintético | Sismograma artificial de sônico+densidade, para amarrar sísmica ao poço |

*(Tabela parcial. Os 96 cards estão nos CSVs.)*

## Navegação

[[19-geofisica-metodos-modulo|← Hub do módulo]] · [[19-geofisica-metodos-questionario-final|← Questionário]]

<!--
last_id_basic: 60
last_id_cloze: 36
gerado_em: "2026-08-18"
tipo: primeira_geracao
nivel: geologia-avancado-v1
pendencias: revisão didática do módulo ainda não realizada
auditoria_cientifica: concluída em 2026-08-18; cards corrigidos fb008, fb020, fc012
-->
