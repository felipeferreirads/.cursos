# Revisão didática: Módulo 11 — Arquitetura dos silicatos

**Revisado em:** 2026-10-06  ·  **Modo:** review-and-fix
**Material:** `curso-mineralogia/11-estrutura-dos-silicatos/` — aulas 01 a 05 e figuras 1 a 3, depois da auditoria científica
**Veredito:** Bem ensinado com ressalvas → **ressalvas 🟡 corrigidas**

## Resumo

🔴 0 bloqueiam · 🟠 0 prejudicam · 🟡 5 atrito · 🔵 3 sugestões

**Carga estimada por aula** (contagem de `gerador-de-aula`; palavras de corpo depois das correções):

| Aula | Conceitos novos | Pré-requisitos reativados | Exemplos | Visuais | Duração |
|---|---|---|---|---|---|
| 01 | 3 (geometria do tetraedro; O ponte × não ponte pela regra 2; Qⁿ) + regra 3 retomada | 4 | 1 (4 itens) | 1 figura + 1 tabela | ~27 min (~1.320) |
| 02 | 2 (regra O/Si = 4 − n/2; seis classes) + leitura da fórmula | 2 | 1 (5 itens) | 1 figura + 1 tabela | ~30 min (~1.090) |
| 03 | 3 (carga e compensação; Al IV × Al VI; Loewenstein) | 3 | 1 (4 itens) | 2 tabelas | ~28 min (~1.280) |
| 04 | 3 (clivagem por classe e vigas em I; densidade × polimerização; Bowen) | 3 | 1 (3 itens, com trigonometria) | 1 figura + 2 tabelas | ~30 min (~1.230) |
| 05 | 2 (mapa Nickel-Strunz × módulos; parâmetros de Liebau) | 3 | 1 (6 itens) | 1 tabela | ~25 min (~1.070) |

Todas abaixo do teto de ~1.600 palavras. A carga da aula 02 está na tabela e no exemplo, não no texto; a da aula 04, na conta dos ângulos.

## Achados

### 🟡 1. Qⁿ escrito de dois jeitos

**Onde:** aula 01 · figura 1 e tabela
**Problema:** o texto usa Q⁰…Q⁴ e a figura, Q0…Q4 (por limitação de renderização de sobrescritos no SVG). O aluno pode achar que são notações diferentes.
**Correção aplicada:** legenda da figura: "(Na figura, Q⁰ a Q⁴ aparecem escritos Q0 a Q4.)"

### 🟡 2. "Topologia" sem remissão

**Onde:** aula 02 · As seis classes
**Correção aplicada:** "(quem está ligado a quem, módulo 10, aula 01)".

### 🟡 3. "Piroxenoide" usado antes da definição

**Onde:** aula 02 · Exemplo trabalhado (d)
**Problema:** a definição só vem na aula 05.
**Correção aplicada:** "(um piroxenoide, isto é, um silicato de cadeia simples que não é piroxênio; aula 05 e módulo 34)".

### 🟡 4. "Intercamada" sem definição

**Onde:** aula 03 · Erros comuns
**Correção aplicada:** "o espaço entre as lâminas (micas)", termo já usado no corpo da aula.

### 🟡 5. "Sítio A" sem apoio

**Onde:** aula 04 · Ino (acrescentado pela auditoria)
**Correção aplicada:** "o sítio A, muitas vezes vazio" com remissão ao módulo 09, onde ele aparece no vetor da edenita.

### 🔵 6. Modelo físico

**Sugestão:** montar tetraedros de papel (ou com bolas e varetas) e ligá-los pelos vértices em par, anel, cadeia e folha. Vale mais que qualquer figura para sentir por que a razão Si:O cai. Fica como sugestão de prática (skill `gerador-de-praticas`, se o usuário pedir).
**Desfecho:** aberto, não bloqueante.

### 🔵 7. Lista de treino de classificação

**Sugestão:** uma lista de 20 fórmulas para classificar (com e sem Al tetraédrico, com OH, H₂O e O extras). O questionário cobre parte disso; uma prática dedicada reforçaria o método.
**Desfecho:** aberto, não bloqueante.

### 🔵 8. Imagens reais de clivagem

**Sugestão:** fotos de seções basais de piroxênio e de anfibólio ao microscópio, com as clivagens a ~87° e ~56°, ajudariam a aula 04. Ficam para o módulo 34, que trata da identificação em lâmina.
**Desfecho:** registrado para o módulo 34.

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo | Avaliado em |
|---|---|---|---|
| `mineralogia-m11-oa01` — tetraedro e polimerização por vértices | a01 | sim (forsterita, quartzo, Si₂O₇) | (questionário a gerar) |
| `mineralogia-m11-oa02` — classificar pela razão Si:O | a02, a05 | sim (hemimorfita, tremolita, caulinita, wollastonita, cianita; piropo, lawsonita, jadeíta, flogopita, sodalita) | (questionário a gerar) |
| `mineralogia-m11-oa03` — Al↔Si e compensação | a03 | sim (albita, anortita, muscovita, leucita, (Al₃Si)O₈) | (questionário a gerar) |
| `mineralogia-m11-oa04` — propriedades a partir da polimerização | a04, a05 | sim (ângulos {110}; densidades) | (questionário a gerar) |

Nenhum objetivo descoberto; nenhuma seção órfã.

## O que está bem feito (manter)

- Uma conta só (O por Si = 4 − n/2) gera todas as razões, em vez de uma tabela para decorar; a cadeia dupla, que é o ponto difícil previsto no hub, ganha a conta explícita da média 2,5.
- A segunda regra de Pauling do módulo 08 é usada para explicar **por que** os silicatos polimerizam e os carbonatos não, e de novo para a regra de Loewenstein (1,5 no O entre dois Al): o mesmo instrumento resolve duas perguntas.
- A aula 03 ensina a desconfiar da fórmula: leucita, nefelina e anortita "parecem" outra classe até o Al tetraédrico ser contado.
- Os ângulos de clivagem de 87° e 56° saem de uma conta com as celas reais (uma delas já usada no módulo 05), não de decoreba; a figura 3 está na escala das celas.
- A aula 05 cumpre o ponto de dificuldade do hub (não antecipar a sistemática): dá o mapa, um exemplo por classe e a pergunta de partida, e remete o resto aos módulos 33–36.

## Correções aplicadas

| # | Severidade | Desfecho | Arquivos |
|---|---|---|---|
| 1 | 🟡 | Corrigido | aula-01 |
| 2, 3 | 🟡 | Corrigido | aula-02 |
| 4 | 🟡 | Corrigido | aula-03 |
| 5 | 🟡 | Corrigido | aula-04 |
| 6-8 | 🔵 | 6 e 7 abertos; 8 registrado para o módulo 34 | — |

As mudanças da revisão foram conferidas pelo `auditor-cientifico` (seção "Segunda passagem" da auditoria do módulo).
