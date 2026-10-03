# Flashcards — Módulo 20: Métodos de campo e mapeamento geológico

**Módulo:** [[20-metodos-campo-mapeamento-modulo|Módulo 20]]
**Total:** 150 cards — 100 Basic + 50 Cloze
**Faixa de IDs:** `geologia-m20-fb001`–`fb100` · `geologia-m20-fc001`–`fc050`
**Gerado em:** 2026-08-18 (Aulas 01–06, `fb001`–`fb060`/`fc001`–`fc030`), **depois** da auditoria científica; estendido em 2026-08-29 (Aulas 07–10, `fb061`–`fb100`/`fc031`–`fc050`), quando o módulo ganhou as quatro aulas de topografia instrumental. As Aulas 07–10 ainda não passaram por auditoria científica formal.

> [!info] Primeira geração O módulo 20 nunca teve baralho. Importe os dois CSVs em deck limpo. O baralho foi gerado sobre o texto já corrigido pela auditoria ([[20-metodos-campo-mapeamento-auditoria|relatório]]) — os cards de regra dos V (`fb026`–`fb030`, `fc013`–`fc014`) já refletem os quatro casos corrigidos, não a versão original de três casos.

> [!info] Extensão 2026-08-29 Cards `fb061`–`fb100` e `fc031`–`fc050` cobrem as Aulas 07–10 (teoria dos erros/NBR 13133, planimetria/poligonais, altimetria/curvas de nível/áreas e volumes, SIRGAS2000/UTM/GNSS geodésico). Se reimportar o deck no Anki, importe apenas as linhas novas (ou reimporte o CSV inteiro — o Anki atualiza por `id`, sem duplicar).

## Arquivos para importar

| Arquivo | Tipo de nota no Anki | Campos |
|---|---|---|
| `20-metodos-campo-mapeamento-flashcards-basic.csv` | Basic | id, frente, verso, tags, objetivo, aula, dificuldade, fonte |
| `20-metodos-campo-mapeamento-flashcards-cloze.csv` | Cloze | id, texto, extra, tags, objetivo, aula, dificuldade, fonte |

> [!tip] Importação no Anki Importe os dois **separadamente**. Separador `;`, encoding UTF-8 sem BOM. Marque "Permitir HTML nos campos" e mapeie `id` como primeiro campo (oculto). As tags são hierárquicas (`geologia::metodos-campo::...`). Todas as lacunas Cloze usam a sintaxe numerada `{{cN::texto}}`.

## Distribuição

| Aula | Objetivo | Basic | Cloze | Total |
|---|---|---:|---:|---|
| a01 — Observação, registro e amostragem | `oa01` | 10 | 5 | 15 |
| a02 — Bússola de geólogo e atitudes | `oa02` | 10 | 5 | 15 |
| a03 — Mapa geológico e regra dos V | `oa03` | 10 | 5 | 15 |
| a04 — Seção geológica | `oa04` | 10 | 5 | 15 |
| a05 — Coluna estratigráfica | `oa05` | 10 | 5 | 15 |
| a06 — Sensoriamento remoto, GPS e SIG | `oa06` | 10 | 5 | 15 |
| a07 — Teoria dos erros e NBR 13133 | `oa07` | 10 | 5 | 15 |
| a08 — Planimetria, azimutes e poligonais | `oa08` | 10 | 5 | 15 |
| a09 — Altimetria, curvas de nível, áreas e volumes | `oa09` | 10 | 5 | 15 |
| a10 — SIRGAS2000, UTM e GNSS geodésico | `oa10` | 10 | 5 | 15 |

Cobertura uniforme: os dez objetivos do módulo têm exatamente 15 cards cada, refletindo que cada aula do módulo cobre um único objetivo de aprendizagem (mapeamento 1:1 entre aula e `oaNN`).

## Critérios aplicados

- **Cards atômicos, um fato por card.** Listas (ex.: os quatro casos da regra dos V, os elementos de uma entrada de caderneta) foram quebradas em cards individuais em vez de um card com resposta composta.
- **A regra dos V recebeu atenção extra** (`fb026`–`fb030`, `fc013`–`fc014`): é o ponto mais fácil de errar do módulo e o que a auditoria encontrou incompleto na primeira versão da aula — os cards testam especificamente o caso menos intuitivo (mergulho a favor do vale e mais íngreme que ele → V aponta rio abaixo).
- **Distinção espessura aparente × espessura real** recebeu cards próprios (`fb042`, `fb043`, `fb049`, `fc021`), pelo mesmo motivo: é uma armadilha geométrica comum, não um detalhe trivial.
- **Valores numéricos aparecem em ordem de grandeza**, consistente com a regra LC-05 do contrato de nível do curso: precisão de GPS como "alguns metros" / "ordem de centímetros" (`fb056`, `fb057`), nunca como número fechado.

## Amostra (tabela de conferência)

| ID | Frente | Verso |
|---|---|---|
| fb003 | O que é a caderneta de campo? | Documento primário do trabalho geológico, registrado no momento da observação |
| fb013 | O que é o mergulho (dip) de uma camada? | Ângulo de inclinação medido a partir da horizontal, perpendicular à direção |
| fb029 | Único caso da regra dos V em que o contato aponta rio abaixo | Mergulho a favor do vale e mais íngreme que a inclinação do próprio vale |
| fb042 | O que é espessura aparente de uma camada? | Espessura medida em direção não perpendicular à camada; sempre ≥ espessura real |
| fb055 | Como o GPS calcula a posição de um receptor? | Triangulação de sinais de múltiplos satélites |

*(Tabela parcial. Os 90 cards estão nos CSVs.)*

## Navegação

[[20-metodos-campo-mapeamento-modulo|← Hub do módulo]] · [[20-metodos-campo-mapeamento-questionario-final|← Questionário]]

<!--
last_id_basic: 100
last_id_cloze: 50
gerado_em: "2026-08-18"
estendido_em: "2026-08-29"
tipo: extensao_de_modulo
nivel: ensino-medio-sem-geologia-v1
pendencias: revisão didática do módulo ainda não realizada. Auditoria científica das Aulas 07-10 concluída em 2026-08-29 (2 achados, ambos corrigidos); o card fb066 foi atualizado na propagação do achado TOP-M20A07-NBR13133-002.
auditoria_cientifica: Aulas 01-06 concluída em 2026-08-18, 1 achado 🟠 corrigido (GEO-M20-F01, regra dos V); baralho original gerado depois da correção. Aulas 07-10 (topografia instrumental) sem auditoria formal ainda.
-->
