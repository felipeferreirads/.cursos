# Aula 04: Cominuição: britagem, moagem e índices de moabilidade

**ID:** geologia-avancado-m09-a04
**Módulo:** [[09-geometalurgia-modulo|Módulo 09 — Geometalurgia]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** descrever os estágios de britagem e de moagem e o circuito fechado com classificação por hidrociclone, comparar as leis de cominuição de Rittinger, Kick e Bond, definir o Work Index e o ensaio de moabilidade de Bond, situar os testes de baixa massa para dimensionamento de moinhos SAG (SPI, SMC/DWi, JK drop-weight) e calcular a energia específica de moagem com a equação de Bond.

**Pré-requisito:** nenhum módulo deste curso. Da Aula 01: cominuição como maior consumidora de energia da planta, moabilidade. Da Aula 03: o alvo de P80 e a dependência da energia com `1/√P80`.

## Antes de começar, você precisa saber

- Que a **moabilidade** de uma rocha determina a energia por tonelada e a capacidade (toneladas por hora) de uma planta de moagem de potência instalada fixa (Aula 01).
- Que o **P80** é a abertura de malha pela qual passam 80 % da massa de um material, e que a recuperação melhora com um P80 menor, ao custo de mais energia (Aula 03).
- Que potência é energia por unidade de tempo; a **energia específica** de moagem, em kWh por tonelada, é a potência do moinho dividida pela vazão mássica de sólidos.

## Conteúdo

### Cominuição: por que domina o custo

**Cominuição** é a redução de tamanho por fragmentação. Numa planta de flotação, ela costuma responder por 30 a 50 % — às vezes mais — do consumo de energia elétrica; em escala global, a cominuição de minérios consome alguns pontos percentuais de toda a eletricidade gerada. A eficiência termodinâmica é baixíssima: a fração da energia aplicada que se converte em superfície nova fica abaixo de 1 a 2 %; o restante vira calor, som e deformação.

A **razão de redução** de um equipamento é o tamanho de alimentação dividido pelo tamanho de produto (na prática, `F80/P80`). Cada equipamento opera bem numa faixa de razão de redução; forçar muita redução num único passo custa energia desproporcional.

### Britagem

A britagem trabalha **a seco**, sobre o material como sólido:

- **Primária** — britador giratório ou de mandíbulas; recebe o ROM (*run-of-mine*, blocos de até cerca de 1 m) e reduz a ~150–200 mm. Razão de redução de 3 a 6.
- **Secundária e terciária** — britadores cônicos e de rolos; de ~150 mm a ~10–25 mm.
- **HPGR** (*high-pressure grinding rolls*) — britagem por compressão de um leito de partículas; mais eficiente em energia que a britagem convencional e o moinho, e induz microfissuras que melhoram a moagem e a lixiviação subsequentes. Comum hoje em minérios duros.

### Moagem

A moagem trabalha **a úmido**, com o minério em polpa, em moinhos tubulares rotativos que carregam corpos moedores:

- **Moinho de bolas** — corpos moedores são bolas de aço; produz o material fino, com P80 de dezenas a ~150 µm.
- **Moinho SAG** (semiautógeno) — o próprio minério grosso serve de corpo moedor, complementado por 4 a 15 % de bolas de aço; recebe apenas minério de britagem primária, o que elimina os estágios secundário e terciário de britagem. Circuitos SAB (SAG seguido de moinho de bolas) e SABC (com britagem dos seixos críticos, os *pebbles*).
- **Moinho autógeno (AG)** — só minério, sem bolas.
- **Moinhos verticais** (torre, Vertimill, IsaMill) — para remoagem fina e ultrafina.

### Circuito fechado com classificação

O moinho de bolas opera em **circuito fechado** com um **hidrociclone**: a descarga do moinho é classificada; o *underflow* (fração grossa) retorna ao moinho para nova moagem, e o *overflow* (fração fina, já no P80 alvo) segue para a concentração. A **carga circulante** — razão entre a massa que recircula e a alimentação nova — fica tipicamente entre 200 e 350 %. O circuito fechado retira a partícula assim que ela atinge o tamanho, evitando sobremoagem, e aumenta a capacidade em relação ao moinho isolado.

### As três leis de cominuição

As três "leis" são casos particulares de `dE = −C · dx / xⁿ`, integrados entre o tamanho de alimentação e o de produto:

- **von Rittinger (1867)** — `n = 2`: energia proporcional à área superficial nova criada, ou seja a `(1/d_produto − 1/d_alimentação)`. Ajusta-se melhor à moagem fina.
- **Kick (1885)** — `n = 1`: energia proporcional à razão de redução, `ln(F/P)`. Ajusta-se melhor à britagem grossa.
- **Bond (1952)** — `n = 1,5`: caso intermediário, que o próprio Bond batizou de **"terceira teoria da cominuição"** justamente por contar as de von Rittinger e Kick como a primeira e a segunda. Na forma integrada e com as constantes de Bond:

  `W = 10 · Wi · (1/√P80 − 1/√F80)`

  com `W` em kWh/t, `P80` e `F80` em micrômetros, e `Wi` o Work Index em kWh/t. É a equação usada para dimensionar moinhos na faixa convencional: `F80` de milímetros e `P80` de cerca de **50 a algumas centenas de micrômetros**. Abaixo de ~50 µm — moagem fina e remoagem — ela deixa de valer e subestima a energia.

### Work Index e ensaio de moabilidade de Bond

O **Work Index (Wi)** é a energia, em kWh/t, para reduzir o material de tamanho teoricamente infinito a 80 % passante em 100 µm. A forma da equação decorre disso: quando `F80 → ∞` e `P80 = 100 µm`, `W = 10·Wi·(1/10) = Wi`.

O Wi é determinado pelo **ensaio de moabilidade de Bond** (*Bond ball mill grindability test*): um moinho padronizado de 305 × 305 mm, com carga de bolas especificada, operado em **ciclo fechado** (*locked-cycle*) que simula um circuito com 250 % de carga circulante até a moabilidade (gramas de novo passante por revolução) estabilizar. Consome da ordem de 10 kg de material britado abaixo de 3,35 mm e várias horas de trabalho — é laborioso, o que limita quantas amostras de um programa recebem o ensaio. Há ensaios análogos para moinho de barras e, para britagem, o *impact work index*.

**Valores típicos de Wi (kWh/t), pelas compilações derivadas das tabelas de Bond:**

| Faixa | Ordem de grandeza | Exemplos |
|---|---|---|
| Moles | ~5–10 | barita (~6), gipsita (~7), calcário mais brando |
| Intermediários | ~11–16 | quartzito (~11), dolomito (~12), carvão (~12), calcário (~11–14), **muitos minérios sulfetados de Cu (~12–15)**, quartzo (~15) |
| Duros | ~16–20 | granito (~16), itabirito/taconita (~16), xisto (~17), basalto (~19), gabro (~19–20) |
| Muito duros e tenazes | ~20–25 | diorito (~23) e outras rochas ígneas de trama entrelaçada e alta tenacidade |

Três advertências que valem mais que a tabela:

1. **O Wi é resultado de um ensaio sobre uma amostra específica**, não uma constante da litologia. Duas amostras do mesmo granito, de alterações diferentes, dão Wi diferentes — e é justamente essa variabilidade que a geometalurgia existe para mapear.
2. **As compilações publicadas divergem entre si**, em parte porque as tabelas originais de Bond estão em kWh por tonelada curta e nem toda reprodução converte para a base métrica. Confira a base de massa antes de usar um valor tabelado.
3. Use a tabela para **julgar a plausibilidade** de um resultado de ensaio, nunca para substituí-lo em dimensionamento.

### Testes de baixa massa para o moinho SAG

O moinho SAG quebra por **impacto de alta energia**, um mecanismo que o Wi de Bond não descreve. Os testes que caracterizam essa quebra e exigem menos amostra:

- **JK Drop-Weight Test (DWT)** — mede os parâmetros `A` e `b` da relação entre energia de impacto específica e fração de finos gerada; usa ~75 kg em várias frações de tamanho.
- **SMC Test** (Morrell) — versão de baixo custo e baixa massa do DWT, feita numa única fração de tamanho (inclusive fragmentos de testemunho); entrega o índice **DWi** (kWh/m³) e os parâmetros de queda de peso a partir de poucos quilos. Tornou-se o teste padrão dos programas geometalúrgicos.
- **SPI (SAG Power Index)** — tempo, em minutos, para moer uma amostra padrão a P80 1,7 mm num moinho de laboratório; ~2 kg.

Na prática combinam-se um teste de impacto (SMC/DWi ou DWT) e o Bond ball mill Wi para dimensionar o circuito SAG + bolas, por metodologias como a de Morrell e a SAGDesign.

## Exemplo trabalhado

**Situação:** um circuito recebe minério britado com `F80 = 9 000 µm` e deve entregar `P80 = 106 µm`. O ensaio de Bond deu `Wi = 15,0 kWh/t`.

**(a) Energia específica de moagem.**
`1/√106 = 0,097129`  ;  `1/√9000 = 0,010541`
`W = 10 × 15,0 × (0,097129 − 0,010541) = 150 × 0,086588 = 13,0 kWh/t`

**(b) Se o alvo de P80 baixar para 75 µm** (para ganhar liberação, Aula 03):
`1/√75 = 0,115470`
`W = 150 × (0,115470 − 0,010541) = 150 × 0,104929 = 15,7 kWh/t`
Aumento: `(15,7 − 13,0) / 13,0 = +21 %` de energia para 29 % mais fino.

**(c) Custo anual do incremento** — planta de 12 Mt/ano, energia a US$ 0,09/kWh:
`ΔW = 2,7 kWh/t`  →  `2,7 × 12 000 000 = 3,24 × 10⁷ kWh/ano`
`Custo ≈ 3,24 × 10⁷ × 0,09 ≈ US$ 2,9 milhões/ano` só de eletricidade de moagem, fora o desgaste de bolas e de revestimento e a perda de capacidade.

**(d) Se o minério for mais duro** (`Wi = 19,0`), para o mesmo `P80 = 106 µm`:
`W = 10 × 19,0 × 0,086588 = 16,5 kWh/t`
A uma potência instalada fixa, a planta que moía 12 Mt/ano do minério de Wi 15 processa apenas `12 × 13,0 / 16,5 ≈ 9,5 Mt/ano` do minério de Wi 19 — a capacidade cai ~21 % sem que nada mude no circuito.

**Interpretação:** os itens (b) e (d) são as duas faces da moabilidade num modelo geometalúrgico. Baixar o P80 é uma decisão de projeto que custa energia e dinheiro; encontrar um domínio mais duro é um fato do depósito que **rouba toneladas por ano** da planta. Ambos precisam estar no modelo de blocos como energia específica e como capacidade — não como um número único de "consumo de moagem".

## Erros comuns

- **Tratar o Wi como constante tabelada da rocha** — é resultado de um ensaio específico e varia dentro do depósito.
- **Aplicar a equação de Bond fora da faixa em que ela vale** — britagem muito grossa pede Kick; **moagem fina e remoagem abaixo de ~50 µm** já saem da faixa de Bond, que aí **subestima** a energia, e pedem Rittinger, a equação de Charles ou um gráfico de assinatura energética (*signature plot*) levantado no próprio moinho fino.
- **Dimensionar um moinho SAG a partir do Wi de Bond** — a quebra por impacto exige DWT, SMC/DWi ou SPI.
- **Ignorar a carga circulante e a classificação** — o desempenho do circuito fechado não é o do moinho isolado.
- **Confundir razão de redução com eficiência** — muita redução num só passo custa energia desproporcional.
- **Somar energia por trechos de tamanho** como se `F80 → P80` fosse aditivo, em vez de usar a forma `1/√x`.

## O que não concluir

- **Que reduzir o P80 é "ajuste fino"** — a energia cresce com `1/√P80` e arrasta custo, capacidade e geração de lama.
- **Que um Wi baixo significa planta barata** — capacidade, abrasividade (desgaste) e a resposta ao impacto no SAG contam junto.
- **Que HPGR ou moagem mais fina sempre compensam** — dependem de dureza, umidade, do ganho em liberação e em lixiviação, e do preço do metal.
- **Que o ensaio de Bond está superado** — segue sendo a referência para o moinho de bolas e a âncora de calibração dos testes de baixa massa.

## Recap relâmpago

- **Cominuição** (britagem a seco em estágios; moagem a úmido em moinhos SAG e de bolas) domina o consumo de energia da planta e tem eficiência termodinâmica de poucos por cento.
- O moinho de bolas opera em **circuito fechado com hidrociclone**, com **carga circulante** de 200–350 %, para evitar sobremoagem e ganhar capacidade.
- **von Rittinger, 1867** (energia ∝ área nova; moagem fina), **Kick, 1885** (energia ∝ `ln` da razão de redução; britagem grossa) e **Bond, 1952** (intermediária, a "terceira teoria") são as leis de cominuição; a de Bond, `W = 10·Wi·(1/√P80 − 1/√F80)`, é a usada na faixa convencional — de `F80` de milímetros a `P80` de ~50 µm para cima. Abaixo disso ela subestima a energia.
- O **Work Index** é a energia para moer de tamanho infinito a 80 % passante 100 µm; sai do **ensaio de moabilidade de Bond** (moinho 305 × 305 mm, ciclo fechado a 250 % de carga circulante, ~10 kg abaixo de 3,35 mm) — laborioso, poucas amostras. Valores típicos vão de ~6 kWh/t (barita) a ~23 kWh/t (diorito), com a maioria dos minérios sulfetados de Cu entre 12 e 15 — faixas para julgar plausibilidade, nunca para substituir o ensaio.
- Para o moinho **SAG** usam-se **DWT, SMC/DWi e SPI**, que exigem poucos quilos e cabem num programa geometalúrgico de centenas de amostras.
- No exemplo, baixar o P80 de 106 para 75 µm custa +21 % de energia (~US$ 2,9 milhões/ano numa planta de 12 Mt); um minério de Wi 19 em vez de 15 reduz a capacidade da planta em ~21 %.

## Próxima aula

[[09-geometalurgia-aula-05-concentracao-e-recuperacao|Aula 05 — Concentração: gravítica, magnética, flotação e lixiviação; recuperação metalúrgica]]

## Anterior

[[09-geometalurgia-aula-03-textura-e-liberacao|Aula 03 — Textura, tamanho de grão e liberação mineral: curvas de liberação]]

## Fontes

- Bond, F. C. (1952), "The third theory of comminution", *Transactions AIME (Mining Engineering)*, 193, p. 484–494.
- Bond, F. C. (1961), "Crushing and grinding calculations", *British Chemical Engineering*, 6(6), p. 378–385, e 6(8), p. 543–548.
- Napier-Munn, T. J., Morrell, S., Morrison, R. D. & Kojovic, T. (1996), *Mineral Comminution Circuits: Their Operation and Optimisation*, JKMRC, cap. 1–5 e 9.
- Wills, B. A. & Finch, J. A. (2016), *Wills' Mineral Processing Technology*, 8ª ed., Butterworth-Heinemann, cap. 5–9.
- Morrell, S. (2004), "Predicting the specific energy of autogenous and semi-autogenous mills from small diameter drill core samples", *Minerals Engineering*, 17(3), p. 447–451.
- Starkey, J. & Dobby, G. (1996), "Application of the MinnovEX SAG Power Index at five Canadian SAG plants", *Proc. International Autogenous and Semiautogenous Grinding Technology (SAG 1996)*, Vancouver.
- Doll, A. G. (2022), "Fine grinding, a refresher", *Procemin-GEOMET* / SAGMILLING.COM — limites de validade da equação de Bond na moagem fina e o gráfico de assinatura energética.

<!--
nivel: avancado
palavras_corpo: ~1900
mapa_objetivo_secao:
  geologia-avancado-m09-oa03: "Cominuição: por que domina o custo" + "Britagem" + "Moagem" + "Circuito fechado com classificação" + "As três leis de cominuição" + "Work Index e ensaio de moabilidade de Bond" + "Testes de baixa massa para o moinho SAG" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOMET-M09-A04-ENERGIA-001
    claim: "A cominuição costuma responder por 30 a 50 % do consumo de energia elétrica de uma planta de flotação e por alguns pontos percentuais da eletricidade global; a fração da energia aplicada convertida em superfície nova é inferior a 1–2 %, dissipando-se o restante como calor, som e deformação."
    risk: fato
    source: "Napier-Munn et al. 1996, cap. 1; Wills & Finch 2016, cap. 5"
  - claim_id: GEOMET-M09-A04-ESTAGIOS-002
    claim: "A britagem opera a seco em estágios (primária: giratório ou mandíbulas, ROM a ~150–200 mm, razão de redução 3–6; secundária/terciária: cônicos e rolos, a ~10–25 mm), com HPGR como opção de britagem por leito de partículas que induz microfissuras; a moagem opera a úmido em moinhos de bolas (produto fino) e SAG (semiautógeno, minério grosso como corpo moedor mais 4–15 % de bolas), em circuitos SAB/SABC."
    risk: fato
    source: "Wills & Finch 2016, cap. 6–8; Napier-Munn et al. 1996, cap. 2–3"
  - claim_id: GEOMET-M09-A04-CIRCUITO-003
    claim: "O moinho de bolas opera em circuito fechado com hidrociclone, que retorna o underflow grosso ao moinho e envia o overflow fino à concentração, com carga circulante tipicamente de 200 a 350 %, evitando sobremoagem e aumentando a capacidade em relação ao moinho isolado."
    risk: fato
    source: "Wills & Finch 2016, cap. 7 e 9; Napier-Munn et al. 1996, cap. 5"
  - claim_id: GEOMET-M09-A04-LEIS-004
    claim: "As leis de cominuição são casos de dE = −C·dx/xⁿ: von Rittinger 1867 (n = 2, energia ∝ área nova, melhor para moagem fina), Kick 1885 (n = 1, energia ∝ ln da razão de redução, melhor para britagem grossa) e Bond 1952, a 'terceira teoria' assim chamada por contar Rittinger e Kick como a primeira e a segunda (n = 1,5, intermediária); a equação de Bond é W = 10·Wi·(1/√P80 − 1/√F80), com W em kWh/t e tamanhos em micrômetros. Sua faixa de validade vai de F80 de milímetros a P80 de cerca de 50 a algumas centenas de micrômetros; abaixo de ~50 µm (moagem fina e remoagem) ela subestima a energia, e usam-se Rittinger, a equação de Charles ou um gráfico de assinatura energética."
    risk: fato
    source: "Bond 1952; Bond 1961; Wills & Finch 2016, cap. 5; literatura de moagem fina (signature plot / Doll, 'Fine grinding, a refresher')"
  - claim_id: GEOMET-M09-A04-WI-005
    claim: "O Work Index é a energia (kWh/t) para reduzir o material de tamanho infinito a 80 % passante em 100 µm; é determinado pelo ensaio de moabilidade de Bond, num moinho padrão de 305 × 305 mm operado em ciclo fechado simulando 250 % de carga circulante, consumindo ~10 kg de material britado abaixo de 3,35 mm."
    risk: fato
    source: "Bond 1952; Bond 1961; Wills & Finch 2016, cap. 5; Napier-Munn et al. 1996, cap. 4"
  - claim_id: GEOMET-M09-A04-WI-VALORES-006
    claim: "Valores típicos de Work Index de moinho de bolas (kWh/t, base métrica), pelas compilações derivadas das tabelas de Bond: moles ~5–10 (barita ~6, gipsita ~7); intermediários ~11–16 (quartzito ~11, dolomito ~12, carvão ~12, calcário ~11–14, minérios sulfetados de Cu ~12–15, quartzo ~15); duros ~16–20 (granito ~16, itabirito/taconita ~16, xisto ~17, basalto ~19, gabro ~19–20); muito duros e tenazes ~20–25 (diorito ~23, e outras rochas ígneas de trama entrelaçada e alta tenacidade). São faixas indicativas para julgar a plausibilidade de um ensaio, não constantes de projeto: o Wi é resultado de um ensaio sobre uma amostra específica, e as compilações publicadas divergem entre si em parte porque as tabelas originais de Bond estão em kWh por tonelada curta e nem toda reprodução converte para a base métrica."
    risk: fato
    source: "Bond 1961 (tabelas de work index) e compilações derivadas; Wills & Finch 2016, cap. 5; Napier-Munn et al. 1996, cap. 4"
  - claim_id: GEOMET-M09-A04-SAG-TESTES-007
    claim: "O dimensionamento de moinhos SAG usa testes de quebra por impacto de menor massa que o ensaio de Bond: o JK Drop-Weight Test (parâmetros A e b, ~75 kg), o SMC Test (índice DWi, poucos quilos, inclusive testemunho) e o SPI (tempo para moer a P80 1,7 mm, ~2 kg), combinados na prática com o Bond ball mill Wi."
    risk: fato
    source: "Napier-Munn et al. 1996, cap. 4; Morrell 2004; Starkey & Dobby 1996"
  - claim_id: GEOMET-M09-A04-EXEMPLO-008
    claim: "Para F80 = 9 000 µm, P80 = 106 µm e Wi = 15,0 kWh/t: W = 150 × (0,097129 − 0,010541) = 13,0 kWh/t. Baixando P80 para 75 µm: W = 15,7 kWh/t (+21 %). Numa planta de 12 Mt/ano a US$ 0,09/kWh, o incremento de 2,7 kWh/t custa ~US$ 2,9 milhões/ano. Com Wi = 19,0 para P80 = 106 µm, W = 16,5 kWh/t, e a capacidade a potência fixa cai de 12 para ~9,5 Mt/ano (−21 %)."
    risk: calculo
    source: "Equação de Bond (Bond 1961); aritmética de energia específica e capacidade"
-->
