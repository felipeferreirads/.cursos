# Aula 03: Textura, tamanho de grão e liberação mineral: curvas de liberação

**ID:** geologia-avancado-m09-a03
**Módulo:** [[09-geometalurgia-modulo|Módulo 09 — Geometalurgia]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** definir liberação mineral e grau de liberação, relacioná-los ao tamanho de grão do mineral e ao tamanho de partícula após a moagem, distinguir liberação por fratura não preferencial de liberação por descolamento, e ler a curva de liberação e a curva teor-recuperação para escolher o alvo de moagem P80.

**Pré-requisito:** nenhum módulo deste curso. Da Aula 01: recuperação, o papel da textura. Da Aula 02: associação mineral, distribuição de tamanho de grão e grau de liberação medidos por análise modal automatizada.

## Antes de começar, você precisa saber

- Que um concentrador separa eficientemente apenas partículas **liberadas** — constituídas por um só mineral (Aula 01).
- Que a análise modal automatizada mede o **grau de liberação** de um mineral por classe de tamanho de partícula, e a **associação** — de quem o mineral está encostado (Aula 02).
- Que o produto de uma moagem tem uma distribuição de tamanhos de partícula, e não um tamanho único.

## Conteúdo

### Partícula liberada e grau de liberação

Uma **partícula liberada** é aquela em que um só mineral ocupa mais que um limiar da sua área ou volume — na prática, adota-se ≥ 90 % ou ≥ 95 %. Abaixo do limiar, a partícula é **mista** ou **travada** (*locked*): o mineral-alvo continua fisicamente preso à ganga.

Duas advertências sobre esse número. Primeiro, **o limiar é uma convenção**, não uma propriedade: um mesmo produto de moagem tem graus de liberação diferentes a 90 % e a 95 %, e comparar valores de laboratórios distintos sem conferir o limiar é comparar coisas diferentes. Segundo, existem **duas definições** de liberação: por *composição* (quanto do volume da partícula é o mineral-alvo) e por *superfície exposta* (quanto da superfície da partícula é o mineral-alvo). A flotação, que age na superfície, responde à segunda; a separação gravítica e a magnética, que agem na massa, respondem à primeira. Salvo aviso, "grau de liberação" é o de composição.

O **grau de liberação** de um mineral é a fração da sua massa total que está presente em partículas liberadas desse mineral. Varia de 0 a 100 % e é medido por classe de tamanho. É a estatística do conjunto — distinta da pergunta binária "esta partícula está liberada?".

### Tamanho de grão e tamanho de partícula

A regra geral: **para liberar um mineral, é preciso moer a rocha até um tamanho de partícula igual ou menor que o tamanho de grão desse mineral na rocha**.

- Minério de **disseminação grossa** (grãos de 0,1 a 1 mm) libera com moagem moderada.
- Minério de **disseminação fina** (grãos < 50 µm), com **microinclusões** ou com **exsolução** (por exemplo, lamelas de pentlandita em pirrotita) exige moagem fina a ultrafina.
- Uma **inclusão** de um mineral dentro de outro só libera se a partícula ficar menor que a própria inclusão — o que muitas vezes é economicamente inviável.

O tamanho de grão é uma herança geológica: da granulação da rocha ígnea ou metamórfica, do grau de recristalização, dos episódios de exsolução no resfriamento, da lixiviação e da precipitação secundária no intemperismo. É por isso que a textura, e não o teor, governa a moagem necessária.

### Fratura não preferencial e descolamento

Como a rocha quebra determina quanta energia a liberação custa.

**Fratura não preferencial** (aleatória, transgranular): a trinca atravessa os grãos sem "enxergar" os contornos entre minerais. É o comportamento da maioria dos minérios silicáticos e sulfetados. A consequência prática é dura: a liberação só cresce com a redução drástica de tamanho, obrigando à **sobremoagem** (moer mais fino que o estritamente necessário) e gerando **lamas** — partículas ultrafinas problemáticas.

**Descolamento** ou **liberação preferencial** (intergranular): a fratura segue os contornos de grão ou uma fase frágil ou clivável — mica, borda de sulfeto, franja de alteração argilosa. Ocorre em parte dos minérios (alguns minérios de ferro intemperizados, pegmatitos, minérios de matriz argilosa) e é explorada por técnicas como a fragmentação por pulsos de alta tensão e a moagem seletiva. Quando existe, a liberação custa muito menos energia.

### Curvas de liberação e curva teor-recuperação

A **curva de liberação** mostra o grau de liberação do mineral-alvo em função do tamanho de partícula (ou do P80 do produto de moagem). É monótona crescente, com **assíntota abaixo de 100 %** — sempre restam travamento fino e inclusões.

Com os pontos do exemplo trabalhado desta aula:

```
grau de
liberação
   100% |- - - - - - - - - - - - - - - - -   assíntota (< 100 %)
        |                              94 o
    90% |                     86 o
        |
    80% |
        |             71 o
    70% |
        |
    60% |
        |     52 o
    50% +-----+---------+----------+---------+
            150        106         75        45      P80 (µm)
        <-- mais grosso                 mais fino -->
```

Leia o **formato**, não os pontos: a curva sobe depressa no início e **achata** no fim. Os primeiros 20 pontos de liberação custam pouca energia; os últimos, muita — e é esse achatamento que cria o ótimo econômico da seção seguinte.

A partir dela e da associação, projeta-se a recuperação atingível: as partículas liberadas recuperam com a eficiência do concentrador — nos modelos de projeto adota-se tipicamente 95–97 % para um sulfeto bem condicionado, hipótese de modelagem e não constante medida; as partículas mistas recuperam **parcialmente**, e quanto — depende da fração de mineral-alvo exposta na superfície da partícula e da rota. A flotação recupera mistas que tenham mineral-alvo exposto; a separação gravítica e a magnética respondem à densidade ou à susceptibilidade **média** da partícula mista.

A **curva teor-recuperação** relaciona, para um dado minério e uma dada moagem, o teor do concentrado e a recuperação: são inversamente relacionados. Move-se **ao longo** de uma curva por tempo de flotação, dosagem de reagente e número de estágios de limpeza. Muda-se **de** curva moendo mais fino (mais liberação) ou processando outro minério. A liberação desloca a curva inteira: minério mais liberado dá mais recuperação a qualquer teor de concentrado.

```
teor do
concentrado
    30% |   o
        |     o                    o = minério tal como moído
    28% |       o                  x = o mesmo minério, moído mais fino
        | x       o
    26% |   x        o
        |     x          o
    24% |        x            o
        |            x             o
    22% +----+----+----+----+----+----+
            75   80   85   90   95  100     recuperação (%)
```

Duas leituras distintas, e confundi-las é o erro clássico: **andar sobre a curva** (reagente, tempo, estágios de limpeza) apenas troca teor por recuperação — não há ganho líquido. **Trocar de curva** (moer mais fino, liberar mais) desloca a linha inteira para fora e melhora as duas coisas ao mesmo tempo. Só a segunda é ganho real, e ela custa energia.

### O alvo de moagem P80

O **P80** é a abertura de malha pela qual passam 80 % da massa do produto de moagem — o descritor padrão de finura. Escolher o P80 é um compromisso:

- Mais fino → mais liberação e mais recuperação.
- Mas a energia de moagem cresce de forma acentuada — pela equação de Bond (Aula 04), aproximadamente com `1/√P80` —, o custo sobe e a capacidade da planta cai.
- E a fração de **lamas ultrafinas** (< 10–20 µm) aumenta: lamas flotam mal, arrastam ganga por entranhamento mecânico na espuma, e dificultam o espessamento e a filtragem.

Existe, portanto, um **P80 de ótimo econômico**: aquele em que o valor do metal marginal recuperado iguala o custo marginal de energia mais as perdas por lama. Um minério cuja recuperação só melhoraria moendo abaixo desse ponto é dito **limitado por liberação** (*liberation-limited*).

## Exemplo trabalhado

**Situação:** minério de cobre, mineral-alvo calcopirita, tamanho de grão médio 70 µm. A análise modal automatizada em quatro produtos de moagem dá o grau de liberação da calcopirita, e a equação de Bond (Wi = 14 kWh/t, F80 = 12 000 µm) dá a energia de moagem:

| P80 do produto | Grau de liberação da calcopirita | Energia de moagem |
|---|---|---|
| 150 µm | 52 % | 10,2 kWh/t |
| 106 µm | 71 % | 12,3 kWh/t |
| 75 µm | 86 % | 14,9 kWh/t |
| 45 µm | 94 % | 19,6 kWh/t |

Estime a recuperação em cada P80, adotando
`R = (grau de liberação × 0,96) + [(1 − grau de liberação) × 0,35]`,
em que 0,96 é a recuperação das partículas liberadas e 0,35 a recuperação média das partículas mistas por flotação.

**Resolução:**

`P80 150 µm: R = 0,52 × 0,96 + 0,48 × 0,35 = 0,499 + 0,168 = 0,667 → 66,7 %`
`P80 106 µm: R = 0,71 × 0,96 + 0,29 × 0,35 = 0,6816 + 0,1015 = 0,7831 → 78,3 %`
`P80  75 µm: R = 0,86 × 0,96 + 0,14 × 0,35 = 0,826 + 0,049 = 0,875 → 87,5 %`
`P80  45 µm: R = 0,94 × 0,96 + 0,06 × 0,35 = 0,902 + 0,021 = 0,923 → 92,3 %`

Ganho de recuperação por incremento de finura, contra o custo de energia:
`150 → 106 µm: +11,6 pontos por +2,1 kWh/t  (≈ 5,5 pontos por kWh/t)`
`106 →  75 µm:  +9,2 pontos por +2,6 kWh/t  (≈ 3,5 pontos por kWh/t)`
` 75 →  45 µm:  +4,8 pontos por +4,7 kWh/t  (≈ 1,0 ponto  por kWh/t)`

**Interpretação:** o retorno em recuperação cai e o custo de energia sobe a cada passo. Entre 150 e 75 µm, cada kWh/t adicional compra vários pontos de recuperação; entre 75 e 45 µm, compra cerca de um ponto, e ainda aumenta a fração ultrafina — quanto, depende da inclinação da distribuição granulométrica, e não se lê do P80 sozinho. Com o preço do cobre e o custo de energia da operação, o ótimo econômico deste minério fica perto de P80 75–90 µm — e é a curva de liberação, não o teor, que aponta esse valor. Outro domínio do mesmo depósito, com calcopirita de grão mais fino, teria outra curva e outro ótimo.

Duas ressalvas sobre os números da tabela, ambas na mesma direção — a de tornar a estimativa **otimista**:

- Os graus de liberação vêm de seções polidas e carregam o **viés estereológico** da Aula 02: a medida 2D superestima a liberação real. A recuperação calculada aqui é, portanto, um limite superior.
- A energia do último ponto (`P80 45 µm`) está no limite inferior de validade da equação de Bond (Aula 04), que subestima a energia na moagem fina. Os 19,6 kWh/t são indicativos; um dimensionamento real usaria um ensaio de moagem fina.

## Erros comuns

- **Confundir tamanho de partícula com tamanho de grão** — moer para 75 µm não libera um mineral de grão de 20 µm.
- **Supor que moer mais fino sempre melhora o resultado econômico** — ignora a energia (`1/√P80`) e as lamas.
- **Assumir descolamento quando o minério frature de forma não preferencial** — superestima a liberação a uma dada moagem.
- **Ler o grau de liberação como se fosse a recuperação** — partículas mistas ainda contribuem em parte, partículas liberadas nem sempre a 100 %.
- **Ignorar a assíntota** — a liberação nunca chega a 100 %; inclusões e travamento fino permanecem.
- **Tratar a curva teor-recuperação como algo a vencer só com reagente** — o teto é da liberação e da mineralogia.

## O que não concluir

- **Que existe um P80 universal** — cada minério, e cada domínio geometalúrgico, tem o seu, ditado pelo tamanho de grão e pela textura.
- **Que liberação alta garante recuperação alta** — ainda dependem da química de superfície, dos reagentes e da operação (Aula 05). E, sobretudo, o teto de liberação **compõe-se** com o teto de partição da Aula 02, não o substitui: um minério com 88 % do cobre em sulfetos e 94 % de liberação a P80 45 µm não recupera 94 %, porque os 12 % em crisocola e óxidos continuam invisíveis à flotação em qualquer finura. Os dois tetos multiplicam-se; o menor deles é sempre o que manda.
- **Que a curva de liberação de um minério vale para outro domínio do mesmo depósito** — ela precisa ser medida onde a textura muda.
- **Que sobremoer é sempre erro** — para inclusões finas pode ser a única via, aceito o custo.

## Recap relâmpago

- **Partícula liberada:** ≥ ~90 % (ou ≥ 95 %) de um só mineral — o limiar é convenção, e há duas definições, por composição e por superfície exposta; a flotação responde à segunda. **Grau de liberação** de um mineral: fração da sua massa em partículas liberadas, medida por classe de tamanho — e **superestimada** pela medida em seção 2D (Aula 02).
- Para liberar, é preciso moer até um tamanho de partícula ≤ ao tamanho de grão do mineral na rocha; **inclusões** só liberam abaixo do próprio tamanho.
- **Fratura não preferencial** (transgranular, a regra) exige redução drástica de tamanho e gera sobremoagem e lamas; **descolamento** (intergranular, alguns minérios e técnicas) libera com muito menos energia.
- A **curva de liberação** (liberação × P80) sobe depressa e depois **achata** — os últimos pontos de liberação são os caros. A **curva teor-recuperação** é inversa, e há duas leituras que não se confundem: **andar sobre a curva** (reagente, tempo, limpeza) só troca teor por recuperação; **trocar de curva** (moer mais fino, liberar mais) desloca a linha inteira e melhora as duas — é o único ganho real, e custa energia.
- O **alvo de P80** é um ótimo econômico: a energia de moagem cresce com `1/√P80` e as lamas ultrafinas pioram a flotação e o desaguamento. No exemplo, o retorno em recuperação por kWh/t cai de ~5,5 para ~1,0 ponto entre 150 e 45 µm.

## Próxima aula

[[09-geometalurgia-aula-04-cominuicao-e-moabilidade|Aula 04 — Cominuição: britagem, moagem e índices de moabilidade]]

## Anterior

[[09-geometalurgia-aula-02-mineralogia-de-processo|Aula 02 — Caracterização de minério e ganga: mineralogia de processo e análise modal automatizada]]

## Fontes

- Wills, B. A. & Finch, J. A. (2016), *Wills' Mineral Processing Technology*, 8ª ed., Butterworth-Heinemann, cap. 1, 7 e 12.
- Gu, Y. (2003), "Automated scanning electron microscope based mineral liberation analysis", *Journal of Minerals & Materials Characterization & Engineering*, 2(1), p. 33–41.
- Gay, S. L. & Morrison, R. D. (2006), "Using two-dimensional sectional distributions to infer three-dimensional volumetric distributions — validation using tomography", *Particle & Particle Systems Characterization*, 23(3–4), p. 246–253.
- King, R. P. (2012), *Modeling and Simulation of Mineral Processing Systems*, 2ª ed. (ed. Schneider, C. L. & King, E. A.), SME, cap. 2 (liberação mineral).
- Petruk, W. (2000), *Applied Mineralogy in the Mining Industry*, Elsevier, cap. 6 e 9.
- Mariano, R. A., Evans, C. L. & Manlapig, E. (2016), "Definition of random and non-random breakage in mineral liberation — a review", *Minerals Engineering*, 94, p. 51–60.

<!--
nivel: avancado
palavras_corpo: ~1900
mapa_objetivo_secao:
  geologia-avancado-m09-oa02: "Partícula liberada e grau de liberação" + "Tamanho de grão e tamanho de partícula" + "Fratura não preferencial e descolamento" + "Curvas de liberação e curva teor-recuperação" + "O alvo de moagem P80" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOMET-M09-A03-LIBERACAO-001
    claim: "Uma partícula é considerada liberada quando um único mineral ocupa mais que um limiar (na prática 90 % ou 95 %) de sua área ou volume; o grau de liberação de um mineral é a fração de sua massa total presente em partículas liberadas, medido por classe de tamanho. O limiar é convenção de laboratório, não propriedade do material, e há duas definições distintas — liberação por composição (volume) e liberação por superfície exposta —, sendo a segunda a relevante para a flotação e a primeira para as separações gravítica e magnética. Valores medidos em seção 2D são superestimados pelo viés estereológico (Aula 02)."
    risk: fato
    source: "Wills & Finch 2016, cap. 12; Gu 2003; King 2012, cap. 2; Gay & Morrison 2006"
  - claim_id: GEOMET-M09-A03-GRAO-PARTICULA-002
    claim: "Liberar um mineral requer moer a rocha até um tamanho de partícula igual ou menor que o tamanho de grão desse mineral; inclusões de um mineral em outro só liberam se a partícula ficar menor que a própria inclusão; o tamanho de grão é herdado da história geológica (granulação, recristalização, exsolução, intemperismo)."
    risk: fato
    source: "Wills & Finch 2016, cap. 1 e 12; Petruk 2000, cap. 6"
  - claim_id: GEOMET-M09-A03-FRATURA-003
    claim: "Na maioria dos minérios silicáticos e sulfetados a fratura é não preferencial (transgranular), de modo que a liberação só cresce com redução drástica de tamanho, gerando sobremoagem e lamas; a liberação por descolamento (fratura intergranular ou por fase frágil) ocorre em parte dos minérios e é mais eficiente em energia."
    risk: fato
    source: "Mariano, Evans & Manlapig 2016; Wills & Finch 2016, cap. 7 e 12"
  - claim_id: GEOMET-M09-A03-CURVAS-004
    claim: "A curva de liberação (grau de liberação × P80) é crescente, côncava (sobe depressa e achata) e com assíntota abaixo de 100 %; a curva teor-recuperação relaciona inversamente o teor do concentrado e a recuperação — move-se ao longo dela por tempo, dosagem e estágios de limpeza, o que apenas troca teor por recuperação, e muda-se de curva moendo mais fino ou trocando de minério; maior liberação desloca toda a curva para fora, melhorando teor e recuperação simultaneamente."
    risk: fato
    source: "Wills & Finch 2016, cap. 12; King 2012, cap. 2"
  - claim_id: GEOMET-M09-A03-P80-005
    claim: "O P80 é a abertura de malha pela qual passam 80 % da massa do produto de moagem; escolhê-lo é um compromisso, pois moer mais fino aumenta liberação e recuperação mas eleva a energia de moagem (aproximadamente com 1/√P80), reduz a capacidade da planta e aumenta a fração de lamas ultrafinas (< 10–20 µm), que flotam mal e dificultam espessamento e filtragem."
    risk: fato
    source: "Wills & Finch 2016, cap. 7, 9 e 12; Napier-Munn et al. 1996, cap. 5"
  - claim_id: GEOMET-M09-A03-EXEMPLO-006
    claim: "Para calcopirita de grão médio 70 µm com liberação de 52 %, 71 %, 86 % e 94 % a P80 de 150, 106, 75 e 45 µm, e R = (liberação × 0,96) + (não liberada × 0,35): a recuperação estimada é 66,7 %, 78,3 %, 87,5 % e 92,3 %; o ganho por incremento de finura cai de ~5,5 para ~1,0 ponto de recuperação por kWh/t adicional entre 150 e 45 µm. As energias por Bond (Wi = 14 kWh/t, F80 = 12 000 µm) são 10,2, 12,3, 14,9 e 19,6 kWh/t; o ponto de 45 µm está no limite inferior de validade da equação de Bond e a energia ali é indicativa. Os graus de liberação, medidos em seção 2D, são superestimados pelo viés estereológico, de modo que a recuperação calculada é um limite superior."
    risk: calculo
    source: "Aritmética do modelo de recuperação por liberação; energia por Bond (Bond 1961; Wi = 14, F80 = 12 000 µm); Gay & Morrison 2006 quanto ao viés estereológico"
-->
