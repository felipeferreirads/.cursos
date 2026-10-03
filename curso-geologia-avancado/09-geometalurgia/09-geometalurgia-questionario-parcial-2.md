# Questionário parcial 2 — Módulo 09: Geometalurgia

**Módulo:** [[09-geometalurgia-modulo|Módulo 09 — Geometalurgia]]
**Cobertura:** Aulas 04 a 06 — cominuição e índices de moabilidade; rotas de concentração e balanço metalúrgico; domínios geometalúrgicos e modelagem da variabilidade.
**Recorte:** o que se faz com este minério, e como se modela — dimensionamento e valor.
**Objetivos avaliados:** `geologia-avancado-m09-oa03` (integral), `geologia-avancado-m09-oa04` (integral)
**Pontuação total:** 100 pontos · o gabarito fica oculto; responda antes de abrir.

**Nota sobre a Aula 05:** as questões desta parcial **não** distribuem peso igual entre as cinco famílias de assunto da aula (gravítica, magnética, flotação, lixiviação, balanço metalúrgico). Flotação e balanço de dois produtos — o que o resto do curso mais consome — recebem mais peso; gravítica e magnética entram apenas como reconhecimento.

---

### 1. Múltipla escolha — `geologia-avancado-m09-q10` · oa03 · 10 pts
Um engenheiro precisa estimar a energia de moagem fina de um concentrado, reduzindo-o de `P80 = 30 µm` para `P80 = 12 µm`. A equação de Bond, calibrada para a faixa convencional (`F80` de milímetros a `P80` de ~50 µm ou mais), é aplicável diretamente a este caso?

- a) Sim, Bond vale para qualquer faixa de tamanho, bastando ajustar o Work Index
- b) Não; abaixo de ~50 µm a equação de Bond subestima a energia, e usam-se alternativas como von Rittinger, a equação de Charles, ou um gráfico de assinatura energética levantado no próprio moinho fino
- c) Não; nesse caso deve-se usar a lei de Kick, própria da britagem grossa
- d) Sim, desde que se troquem `F80` e `P80` de lugar na fórmula

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A equação de Bond, `n = 1,5`, é calibrada para a faixa que vai de `F80` de milímetros a `P80` de cerca de 50 µm para cima. Abaixo disso — moagem fina e remoagem, exatamente o caso de 30 para 12 µm — ela **subestima** a energia, e a literatura recorre a von Rittinger (`n = 2`, mais aderente à moagem fina), à equação de Charles, ou a um gráfico de assinatura energética levantado no próprio equipamento. Kick (`n = 1`) é a lei da britagem grossa, o extremo oposto do caso descrito, o que elimina "c"; "a" e "d" ignoram que cada lei tem faixa de validade própria.
</details>

---

### 2. Aplicação (cálculo) — `geologia-avancado-m09-q11` · oa03 · 15 pts
Um circuito recebe minério britado com `F80 = 7 500 µm` e deve entregar `P80 = 125 µm`. O ensaio de Bond deu `Wi = 13,5 kWh/t`.

(a) Calcule a energia específica de moagem. (b) Se o alvo de `P80` baixar para 90 µm (para ganhar liberação), recalcule a energia e o aumento percentual. (c) Numa planta de 10 Mt/ano, com energia a US$ 0,08/kWh, calcule o custo anual adicional do item (b).

<details>
<summary>Ver resolução</summary>

`1/√125 = 0,089443`  ·  `1/√7 500 = 0,011547`  ·  `1/√90 = 0,105409`

**(a)** `W = 10 × 13,5 × (0,089443 − 0,011547) = 135 × 0,077896 = 10,52 kWh/t`

**(b)** `W = 135 × (0,105409 − 0,011547) = 135 × 0,093862 = 12,67 kWh/t`
Aumento: `(12,67 − 10,52) / 10,52 ≈ 20,5 %`

**(c)** `ΔW = 12,67 − 10,52 = 2,15 kWh/t`
`2,15 × 10 000 000 = 21 500 000 kWh/ano`
`Custo ≈ 21 500 000 × 0,08 ≈ US$ 1,72 milhão/ano`, só de eletricidade de moagem, fora desgaste de bolas e revestimento e perda de capacidade.
</details>

---

### 3. Verdadeiro ou Falso (justifique) — `geologia-avancado-m09-q12` · oa03 · 8 pts
"O Work Index de uma rocha é uma constante litológica — duas amostras de granito sempre terão o mesmo Wi — e um moinho SAG pode ser dimensionado inteiramente a partir do Wi de Bond do minério."

<details>
<summary>Ver resposta</summary>

**Falso, em dois pontos.**

Primeiro, o Wi é **resultado de um ensaio sobre uma amostra específica**, não uma constante da litologia: duas amostras do mesmo granito, com alterações diferentes, dão Wi diferentes — e é exatamente essa variabilidade que a geometalurgia existe para mapear. Segundo, o moinho SAG quebra por **impacto de alta energia**, mecanismo que o Wi de Bond (ensaio de moagem por atrito/impacto de baixa energia em moinho de bolas) não descreve; o dimensionamento do SAG exige testes de impacto de baixa massa (JK Drop-Weight Test, SMC/DWi, SPI), combinados na prática com o Bond ball mill Wi.
</details>

---

### 4. Múltipla escolha — `geologia-avancado-m09-q13` · oa03 · 6 pts
Um minério tem critério de concentração `CC = 1,40` para a separação de um mineral pesado. Segundo a regra prática de Taggart, essa separação por via gravítica é:

- a) Fácil, viável até granulometria fina de ~75 µm
- b) Viável, mas exige controle de finos, até ~150 µm
- c) Difícil, viável só em fragmentos grossos, até ~6,35 mm, tipicamente em pré-concentração
- d) Comercialmente inviável em qualquer tamanho de partícula

<details>
<summary>Ver resposta</summary>

**Resposta: c**

`CC = 1,40` cai na faixa `1,25–1,50`, à qual corresponde separação viável só até ~6,35 mm — material grosso, tipicamente em pré-concentração. "a" e "b" correspondem a faixas de `CC` mais altas (`> 2,5` e `1,75–2,50`, respectivamente); "d" corresponde a `CC < 1,25`. O `CC` nunca se lê sozinho — é sempre o par `CC`/tamanho mínimo de partícula que decide a viabilidade.
</details>

---

### 5. Múltipla escolha — `geologia-avancado-m09-q14` · oa03 · 6 pts
Um concentrador quer remover magnetita (fortemente magnética, a rigor ferrimagnética) de um rejeito antes de descartá-lo. Qual tecnologia de separação magnética é adequada, e por quê?

- a) WHIMS/HGMS de 1–2 T, porque magnetita é apenas fracamente paramagnética
- b) LIMS de baixa intensidade (~0,1–0,4 T), porque magnetita é fortemente magnética e responde a campos baixos
- c) Nenhuma separação magnética funciona em minerais ferrimagnéticos
- d) É necessária flotação, pois magnetita não responde a campo magnético

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Magnetita e pirrotita monoclínica são os minerais fortemente magnéticos de referência — a literatura de processamento os chama de "ferromagnéticos" em sentido amplo, embora, a rigor, sejam ferrimagnéticos. Por serem fortemente magnéticos, respondem a campos baixos, e por isso são separados por **LIMS** (baixa intensidade). **WHIMS/HGMS** (alta intensidade e alto gradiente) é reservado a minerais paramagnéticos fracos (hematita, ilmenita, wolframita, monazita, granada). "c" e "d" ignoram a própria premissa do enunciado.
</details>

---

### 6. Múltipla escolha — `geologia-avancado-m09-q15` · oa03 · 10 pts
Numa flotação de sulfetos de cobre-zinco, deseja-se recuperar a calcopirita e **deprimir a esfalerita** nesta etapa, mesmo com o coletor xantato presente (que adsorve em ambos os sulfetos). Que reagente cumpre essa função, e como ele age?

- a) Espumante, que estabiliza a espuma e por isso reforça a coleta seletiva
- b) Cianeto, que deprime a esfalerita ao complexar o zinco superficial e tornar sua superfície hidrofílica, mantendo a calcopirita livre para o xantato
- c) Sulfato de cobre, que ativa a esfalerita, tornando-a ainda mais flotável junto com a calcopirita
- d) Cal, que deprime exclusivamente a calcopirita, deixando a esfalerita flotar sozinha

<details>
<summary>Ver resposta</summary>

**Resposta: b**

O cianeto é o depressor clássico de esfalerita e de pirita: complexa o zinco (ou o ferro) na superfície do mineral, tornando-a hidrofílica e incapaz de responder ao coletor, mesmo na presença do xantato. O espumante ("a") não atua na seletividade mineral, só na estabilidade da espuma — confundir as duas funções é erro comum listado na Aula 05. O sulfato de cobre ("c") é o **ativador** clássico da esfalerita (efeito oposto ao pedido). A cal ("d") deprime pirita, não calcopirita, e a Aula 05 justamente cita cal deprimindo pirita como exemplo de modificador.
</details>

---

### 7. Aplicação (cálculo) — `geologia-avancado-m09-q16` · oa03 · 15 pts
Uma usina de flotação de cobre amostra as três correntes: alimentação `f = 0,95 % Cu`, concentrado `c = 26,0 % Cu`, rejeito `t = 0,065 % Cu`.

(a) Calcule a recuperação pela fórmula de dois produtos. (b) Calcule a razão de concentração e a razão de enriquecimento. (c) Verifique o balanço numa base de 1 000 t de alimentação. (d) Se um ajuste baixasse o rejeito para `t = 0,045 % Cu`, qual seria a nova recuperação, e quantas toneladas adicionais de Cu seriam recuperadas por 1 000 t de minério?

<details>
<summary>Ver resolução</summary>

**(a)** `R = [c(f − t)] / [f(c − t)] = [26,0 × (0,95 − 0,065)] / [0,95 × (26,0 − 0,065)]`
`R = (26,0 × 0,885) / (0,95 × 25,935) = 23,01 / 24,64 = 0,934 → 93,4 %`

**(b)** `K = F/C = (c − t)/(f − t) = 25,935 / 0,885 = 29,3`
`c/f = 26,0 / 0,95 = 27,4`

**(c)** Base 1 000 t: `Cu alimentado = 1 000 × 0,0095 = 9,5 t`
`Massa de concentrado = 1 000 / 29,3 = 34,1 t → Cu = 34,1 × 0,26 = 8,87 t`
`Massa de rejeito = 965,9 t → Cu = 965,9 × 0,00065 = 0,63 t`
`Soma: 8,87 + 0,63 = 9,50 t` (fecha)

**(d)** `R_novo = [26,0 × (0,95 − 0,045)] / [0,95 × (26,0 − 0,045)] = (26,0 × 0,905) / (0,95 × 25,955) = 23,53 / 24,66 = 0,954 → 95,4 %`
Ganho: `95,4 − 93,4 = 2,0 pontos`. Cobre adicional: `9,5 × 0,020 ≈ 0,19 t Cu` por 1 000 t de minério (≈ 190 kg).
</details>

---

### 8. Dissertativa curta — `geologia-avancado-m09-q17` · oa03 · 8 pts
Duas plantas processam o mesmo minério de cobre, moído ao mesmo `P80`. A planta X opera com mais tempo de flotação e menos estágios de limpeza; a planta Y opera com mais estágios de limpeza e menos tempo. Explique, usando a distinção entre "andar sobre a curva" e "trocar de curva", por que nenhuma das duas obteve um ganho real sobre a outra, e o que precisaria mudar para haver ganho real.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:** X e Y estão apenas **andando sobre a mesma curva** teor-recuperação, em direções opostas — X trocou teor por mais recuperação (mais tempo, menos limpeza), Y trocou recuperação por mais teor (mais limpeza, menos tempo). Como a moagem (e portanto a liberação) é a mesma para as duas, a curva subjacente é a mesma, e nenhuma das duas obtém ganho líquido: uma ganha o que a outra perde. Para haver ganho real, seria preciso **trocar de curva** — moer mais fino (mais liberação) ou processar outro minério —, o que desloca toda a curva teor-recuperação para fora e melhora as duas grandezas simultaneamente, ao custo de mais energia.
</details>

---

### 9. Múltipla escolha — `geologia-avancado-m09-q18` · oa04 · 10 pts
Um mesmo corpo de granito, são numa porção e cloritizado noutra, mói e flota de forma diferente nas duas porções, embora ambas sejam mapeadas como a mesma litologia. Isso ilustra que:

- a) O domínio geológico é sempre também um domínio geometalúrgico
- b) O domínio geometalúrgico deve ser validado pela resposta metalúrgica medida, e não presumido do mapa geológico — a mesma litologia pode ter respostas diferentes
- c) A cloritização não afeta a moabilidade nem a flotação
- d) Apenas a mineralogia de minério, nunca a de ganga ou a alteração, define um domínio geometalúrgico

<details>
<summary>Ver resposta</summary>

**Resposta: b**

O domínio geometalúrgico é um volume que responde de forma homogênea no processo (recuperação, moabilidade, resposta a reagentes), definido cruzando controles geológicos com resposta metalúrgica **medida**. O domínio geológico **não** é automaticamente um domínio geometalúrgico: o próprio exemplo do granito são/cloritizado, citado na Aula 06, mostra a mesma litologia com duas respostas — o que elimina "a" e "c". A alteração hidrotermal (cloritização) é um dos controles geológicos cruzados na definição do domínio, ao lado da litologia e da mineralogia de ganga, o que elimina "d".
</details>

---

### 10. Aplicação (dissertativa) — `geologia-avancado-m09-q19` · oa04 · 12 pts
Um plano de blendagem propõe misturar, na proporção 50/50 em massa, um minério de Work Index `13,0 kWh/t` com outro de Work Index `21,0 kWh/t`. Um engenheiro júnior estima o Wi da blenda pela média ponderada simples: `(13,0 + 21,0) / 2 = 17,0 kWh/t`. Explique por que essa estimativa é inadequada, o que tende a acontecer de fato com a moabilidade da blenda, e por que a recuperação de uma blenda de dois minérios de mineralogia distinta também não deve ser estimada por média ponderada.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:**

- **Work Index não é aditivo.** A média ponderada simples pressupõe que os dois minérios se comportem de forma independente e proporcional à sua massa — o que não ocorre. O componente mais duro (Wi 21,0) resiste mais à quebra, permanece mais tempo no circuito e a energia se distribui de forma não linear entre os dois. A moabilidade real da blenda tende a ser **pior** (mais próxima do minério mais duro) do que os 17,0 kWh/t da média simples sugerem, e o quanto depende da proporção e da granulometria de cada componente.
- **Recuperação também não é aditiva.** Minerais de ganga de um minério (talco, argila, minerais solúveis) podem contaminar a química de flotação do outro; um minério pode consumir o reagente que faltaria ao outro; a cinética muda. A recuperação de uma blenda pode ficar **abaixo** da média ponderada das recuperações isoladas dos dois minérios.
- **Consequência prática:** nem Wi nem recuperação devem ser krigados diretamente, como se fossem aditivos — o teor é a única das três grandezas para a qual a média ponderada (e a krigagem, que é linear) vale.
</details>

---

## Gabarito resumido

| Questão | ID | Resposta |
|---|---|---|
| 1 | q10 | b |
| 2 | q11 | (a) 10,52 kWh/t; (b) 12,67 kWh/t, +20,5 %; (c) ≈ US$ 1,72 milhão/ano |
| 3 | q12 | Falso (Wi é resultado de ensaio específico; SAG exige DWT/SMC/SPI) |
| 4 | q13 | c |
| 5 | q14 | b |
| 6 | q15 | b |
| 7 | q16 | (a) R ≈ 93,4 %; (b) K ≈ 29,3, c/f ≈ 27,4; (d) R ≈ 95,4 %, +0,19 t Cu/1000 t |
| 8 | q17 | ver comentário (mesma curva; sem ganho líquido; trocar de curva exige moer mais fino) |
| 9 | q18 | b |
| 10 | q19 | ver comentário (Wi e recuperação não aditivos; blenda pior que a média) |
