# Aula 04: Zonas e a lei de Weiss

**ID:** mineralogia-m05-a04
**Módulo:** [[05-miller-e-projecao-modulo|Módulo 05 — Eixos cristalográficos, índices de Miller e projeção estereográfica]]
**Duração estimada:** ~28 min
**Nível:** ensino médio, sem geologia prévia (contrato `ensino-medio-sem-geologia-v1`)
**Objetivo:** reconhecer uma zona de faces, calcular o eixo de zona de duas faces, verificar se uma face pertence a uma zona e achar a face comum a duas zonas.
**Pré-requisito:** [[05-miller-e-projecao-aula-03-direcoes-uvw-e-o-sistema-hexagonal-de-miller-bravais-hkil|Aula 03]] (direções [uvw] e conversão de quatro para três índices).

## Vocabulário desta aula

| Termo | O que quer dizer |
|---|---|
| **zona** | conjunto de faces cujas arestas de interseção são todas paralelas a uma mesma direção. |
| **eixo de zona** | essa direção comum, escrita [uvw]. |
| **faces tautozonais** | faces que pertencem à mesma zona. |
| **lei das zonas (de Weiss)** | a condição hu + kv + lw = 0, que diz se a face (hkl) pertence à zona [uvw]. |
| **regra da adição** | se duas faces estão numa zona, a face cujos índices são a soma dos delas também está, entre as duas. |

## Antes de começar, você precisa saber

- Faces (hkl) e direções [uvw], e como passar (hkil) para (hkl): [[05-miller-e-projecao-aula-03-direcoes-uvw-e-o-sistema-hexagonal-de-miller-bravais-hkil|aula 03]].
- **Matemática reativada:** multiplicar e somar inteiros com sinal: (−1)·(−1) = 1; 2·0 = 0; 1·(−1) + 1·1 = 0.

## Ao final você vai conseguir

- `mineralogia-m05-oa03` — Aplicar a lei das zonas (Weiss) para determinar o eixo de zona de duas faces e verificar se uma face pertence a uma zona.

## Conteúdo

### O que é uma zona

Pegue um prisma qualquer, como o de um cristal de turmalina ou de zircão. Todas as faces do prisma se encontram em arestas **verticais**, paralelas umas às outras e ao comprimento do cristal. Essas faces formam uma **zona**, e a direção comum das arestas é o **eixo de zona**. Num prisma tetragonal ou hexagonal, o eixo de zona é c: [001].

![Figura 4 — faces da zona [001]](05-miller-e-projecao-fig-04-zona-001.svg)

*Figura 4. Prisma tetragonal com as formas {100} e {110}, em corte e de lado. O que observar: todas as oito faces do prisma têm o terceiro índice 0 e todas as arestas entre elas são paralelas a c; elas são tautozonais, com eixo de zona [001].*

Zonas não se limitam a prismas. Qualquer par de faces não paralelas se cruza numa aresta (real ou prolongada), e a direção dessa aresta define uma zona à qual pertencem as duas faces e, em geral, muitas outras. Um cristal com muitas faces é uma rede de zonas cruzadas, e reconhecê-las é a principal ferramenta para indexar faces sem medir tudo.

### A lei das zonas

A face (hkl) pertence à zona de eixo [uvw] **se, e somente se**:

**h·u + k·v + l·w = 0**

De onde vem isso? Na aula 02, a face (hkl) corta os eixos em 1/h, 1/k, 1/l. Um ponto de coordenadas (x, y, z), em unidades de a, b, c, está nesse plano quando hx + ky + lz = 1 (substitua os três interceptos e confira). O plano paralelo que passa pelo centro é hx + ky + lz = 0. Uma direção [uvw] "cabe" dentro da face, isto é, é paralela a ela, quando o ponto (u, v, w) está nesse plano: hu + kv + lw = 0. A face contém a direção; logo, as arestas dela com outras faces que também contêm [uvw] são paralelas a [uvw].

Se a dedução pesar, guarde a regra: é ela que se usa. Como a conta usa só coordenadas ao longo dos eixos, **ela vale em qualquer sistema**, inclusive no monoclínico e no triclínico, com eixos oblíquos. No hexagonal, use (hkl) e [UVW] com três índices (aula 03).

Exemplo rápido: (210) pertence a [001]? 2·0 + 1·0 + 0·1 = 0. Sim: toda face com l = 0 é paralela a c.

### Eixo de zona de duas faces

Para achar a direção comum a duas faces (h₁k₁l₁) e (h₂k₂l₂), use a **regra da cruz**. Escreva os índices duas vezes, um embaixo do outro, risque a primeira e a última coluna, e multiplique em cruz:

```text
   h₁  │ k₁   l₁   h₁   k₁ │  l₁
   h₂  │ k₂   l₂   h₂   k₂ │  l₂

   u = k₁·l₂ − l₁·k₂
   v = l₁·h₂ − h₁·l₂
   w = h₁·k₂ − k₁·h₂
```

Trocar a ordem das duas faces troca todos os sinais: [uvw] e [ūv̄w̄] são a mesma reta, em sentidos opostos, e nomeiam a mesma zona.

### Face comum a duas zonas

A mesma regra, aplicada a dois eixos de zona [u₁v₁w₁] e [u₂v₂w₂], dá os índices (hkl) da face (possível) que pertence às duas zonas. É assim que os cristalógrafos indexavam faces pequenas: uma face que trunca duas arestas conhecidas está na interseção das duas zonas, e os índices saem sem medir ângulo nenhum.

### A regra da adição

Se (h₁k₁l₁) e (h₂k₂l₂) estão na mesma zona, então (h₁+h₂, k₁+k₂, l₁+l₂) também está, e fica **entre** as duas. Na zona [001] de um cubo, (100) + (010) = (110), a face do dodecaedro que trunca a aresta vertical do cubo. E (100) + (110) = (210), entre (100) e (110). A regra explica por que faces pequenas aparecem como "chanfros" de arestas.

> [!question] Pare e explique
> Pela lei das zonas, por que toda face (hk0) pertence à zona [001], em qualquer sistema? O que isso diz sobre as faces de um prisma?

## Exemplo trabalhado

**Problema.** Num cristal cúbico aparecem as faces (100), (111) e (011). (a) Ache o eixo da zona que contém (100) e (111). (b) Verifique se (011) e (110) estão nessa zona. (c) Mostre que (111) fica entre (100) e (011). (d) Ache a face comum a essa zona e à zona [001].

**Passo 1. Eixo de zona de (100) e (111).** Regra da cruz com h₁k₁l₁ = 1 0 0 e h₂k₂l₂ = 1 1 1:
u = 0·1 − 0·1 = 0; v = 0·1 − 1·1 = −1; w = 1·1 − 0·1 = 1 → **[01̄1]**.

**Passo 2. (011) está na zona?** 0·0 + 1·(−1) + 1·1 = **0**. Sim.
**(110) está na zona?** 1·0 + 1·(−1) + 0·1 = **−1**. Não.

**Passo 3. Regra da adição.** (100) + (011) = (111). Logo, nessa zona, (111) fica entre (100) e (011).

**Passo 4. Face comum a [01̄1] e [001].** Regra da cruz com 0 1̄ 1 e 0 0 1:
h = (−1)·1 − 1·0 = −1; k = 1·0 − 0·1 = 0; l = 0·0 − (−1)·0 = 0 → (1̄00), ou seja, o par de faces paralelas **(100)/(1̄00)**. Conferência: (100) está em [001] (1·0 + 0 + 0 = 0) e em [01̄1] (0 + 0 + 0 = 0).

**Passo 5. O mesmo no quartzo.** Converta r (101̄1) → (101) e z (011̄1) → (011). Eixo de zona: u = 0·1 − 1·1 = −1; v = 1·0 − 1·1 = −1; w = 1·1 − 0·0 = 1 → **[1̄1̄1]**. A face de prisma (11̄00) → (11̄0): 1·(−1) + (−1)·(−1) + 0·1 = 0, está na zona; a face (101̄0) → (100): 1·(−1) = −1, não está. A aula 06 vai ver essa zona desenhada.

**Método geral:** converta para três índices; eixo de zona pela regra da cruz; pertença pela soma hu + kv + lw; face comum pela regra da cruz aplicada aos eixos.

## Erros comuns

- **Somar os índices em vez de multiplicar e somar.** A lei é h·u + k·v + l·w, termo a termo; (110) e [11̄0] não "somam zero" por terem 1 e −1 em algum lugar, e sim porque 1·1 + 1·(−1) + 0·0 = 0.
- **Usar quatro índices de face com três de direção.** Misturar (hkil) com [UVW] dá conta errada; converta tudo para três índices.
- **Trocar a ordem na regra da cruz e achar que deu outra zona.** O resultado com sinais trocados é a mesma zona.
- **Esquecer que a regra da adição vale só dentro da zona.** Somar índices de faces de zonas diferentes não produz face nenhuma em especial.

## O que não concluir

- Que a face prevista pela regra da cruz exista no cristal. Ela é uma face **possível**; se aparece, depende do crescimento (módulo 25).
- Que zonas existam só onde há arestas reais. A zona é geométrica; vale para arestas prolongadas, entre faces que nem se tocam.
- Que a lei das zonas exija eixos perpendiculares. Ela vale em qualquer sistema, porque usa coordenadas ao longo dos próprios eixos.

## Recap relâmpago

- Zona = faces cujas arestas comuns são paralelas a um eixo de zona [uvw].
- Lei das zonas: (hkl) está em [uvw] se hu + kv + lw = 0; vale em qualquer sistema.
- Eixo de zona de duas faces e face comum a duas zonas: regra da cruz.
- Regra da adição: a soma de duas faces de uma zona é outra face da zona, entre elas.
- No hexagonal, converta para (hkl) e [UVW] antes de calcular.

## Próxima aula

Em [[05-miller-e-projecao-aula-05-a-projecao-estereografica-e-a-rede-de-wulff|Aula 05 — A projeção estereográfica e a rede de Wulff]], cada face vira um ponto num círculo, e cada zona vira uma curva que passa pelos pontos das suas faces.

## Fontes consultadas

- Klein, C. & Dutrow, B., *Manual of Mineral Science*, 23ª ed., Wiley (zonas, eixo de zona, lei de Weiss, regra da cruz).
- IUCr, *Online Dictionary of Crystallography*, verbetes "Zone" e "Zone axis" (consultado em 2026-10-04).
- Contas dos exemplos conferidas em Python (produto vetorial e produto escalar inteiros), em 2026-10-04.

<!--
nivel: ensino-medio-sem-geologia-v1
palavras_corpo: 1253
cobertura:
  mineralogia-m05-oa03: [Conteúdo, Exemplo trabalhado]
figuras:
  - 05-miller-e-projecao-fig-04-zona-001.svg
alegacoes_auditaveis:
  - claim_id: CRI-ZON-DEF-001
    claim: "Zona: faces cujas arestas de intersecao sao paralelas a uma direcao comum, o eixo de zona [uvw]; faces tautozonais."
    risk: conceito
    source: "Klein & Dutrow; IUCr Online Dictionary"
    audit: "verificado em 2026-10-04"
  - claim_id: CRI-ZON-WEISS-001
    claim: "Lei das zonas (Weiss): (hkl) pertence a [uvw] sse hu + kv + lw = 0; vale em qualquer sistema; deducao pelo plano hx + ky + lz = 0."
    risk: conceito
    source: "Klein & Dutrow; International Tables vol. A"
    audit: "verificado em 2026-10-04"
  - claim_id: CRI-ZON-CRUZ-001
    claim: "Eixo de zona de duas faces: u = k1 l2 - l1 k2, v = l1 h2 - h1 l2, w = h1 k2 - k1 h2; a mesma regra aplicada a dois eixos da a face comum."
    risk: conceito
    source: "Klein & Dutrow"
    audit: "verificado em 2026-10-04"
  - claim_id: CRI-ZON-ADICAO-001
    claim: "Regra da adicao: se duas faces estao numa zona, a soma dos indices e face da mesma zona, situada entre elas."
    risk: conceito
    source: "Klein & Dutrow"
    audit: "verificado em 2026-10-04"
  - claim_id: CRI-ZON-EXEMPLO-001
    claim: "(100)x(111) -> [0 -1 1]; (011) na zona, (110) nao; (100)+(011) = (111); face comum a [0-11] e [001] = (100)."
    risk: numero
    source: "calculo conferido em Python"
    audit: "verificado em 2026-10-04"
  - claim_id: CRI-ZON-QUARTZO-001
    claim: "Quartzo: r(101) e z(011) tem eixo de zona [-1 -1 1]; (1-10), i.e. m(1-100), esta na zona; (100), i.e. m(10-10), nao."
    risk: numero
    source: "calculo conferido em Python e no estereograma calculado (figura 8)"
    audit: "verificado em 2026-10-04"
-->
