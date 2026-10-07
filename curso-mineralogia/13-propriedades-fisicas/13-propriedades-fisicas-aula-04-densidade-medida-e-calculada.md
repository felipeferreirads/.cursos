# Aula 04: Densidade — medida e calculada

**ID:** mineralogia-m13-a04
**Módulo:** [[13-propriedades-fisicas-modulo|Módulo 13 — Propriedades físicas e identificação macroscópica]]
**Duração estimada:** ~28 min
**Nível:** ensino médio, sem geologia prévia (contrato `ensino-medio-sem-geologia-v1`)
**Objetivo:** medir a densidade relativa de um espécime pesando-o no ar e na água, estimar a incerteza do resultado, e compará-lo à densidade calculada pela cela unitária para interpretar a diferença.
**Pré-requisito:** [[06-reticulo-e-cela-aula-04-conteudo-da-cela-z-volume-e-densidade-calculada|módulo 06, aula 04]] (densidade calculada ρ = Z·M / (0,6022·V)) e [[09-substituicao-e-formula-aula-03-solucao-solida-miscibilidade-e-isomorfismo|módulo 09, aula 03]] (solução sólida).

## Vocabulário desta aula

| Termo | O que quer dizer |
|---|---|
| **densidade (ρ)** | massa por volume, em g/cm³. |
| **densidade relativa (gravidade específica, G)** | razão entre a densidade da amostra e a da água; é um número sem unidade, e vale quase o mesmo número da densidade em g/cm³. |
| **empuxo** | força para cima que um líquido exerce sobre um corpo mergulhado nele; é igual ao peso do líquido deslocado (princípio de Arquimedes). |
| **balança hidrostática** | arranjo que pesa a amostra no ar e suspensa na água. |
| **densidade calculada** | a que sai da cela unitária e da fórmula (módulo 06), de um cristal ideal. |
| **porosidade** | fração de vazios (poros, fissuras) dentro do espécime. |

## Antes de começar, você precisa saber

- Calcular a densidade pela cela: ρ = Z·M / (0,6022·V), com V em Å³ (módulo 06, aula 04).
- Que a substituição iônica muda a composição, e com ela a massa e o volume da cela (módulo 09).
- **Matemática reativada:** "diferença de pesagens" é uma subtração; a incerteza de um quociente cresce quando o denominador é pequeno (a diferença entre duas pesagens próximas).

## Ao final você vai conseguir

- `mineralogia-m13-oa04` — Estimar a densidade relativa de uma amostra e compará-la à densidade calculada.

## Conteúdo

### Por que a densidade é uma boa propriedade

Das propriedades físicas, a densidade é a mais **quantitativa**: mede-se com balança, sem danificar o espécime. Cada espécie tem um valor típico, que vem da composição (átomos pesados deixam o mineral denso) e do empacotamento (arcabouços abertos o deixam leve; módulo 11, aula 04). Ordens de grandeza, em g/cm³ (valores de literatura, aproximados):

| Faixa | Minerais |
|---|---|
| leves, abaixo de ~2,7 | gipsita ~2,3; halita ~2,2; quartzo 2,65 |
| médios, de ~2,7 a ~3,5 | calcita ~2,71; fluorita ~3,18; diamante ~3,52; forsterita ~3,28 |
| altos, de ~3,5 a ~5 | barita ~4,5; fayalita ~4,4 |
| muito altos, acima de ~5 | pirita ~5,0; magnetita ~5,2; hematita ~5,3; galena ~7,6; ouro nativo ~19 |

É o que a mão "sente": uma amostra de galena parece pesada para o tamanho, e uma de gipsita, leve. Esse **teste de peso** é um primeiro filtro (estimativa) e depois se mede.

### Densidade e densidade relativa

A **densidade relativa G** é a razão entre a densidade do mineral e a da água. A água a 4 °C vale 1,000 g/cm³, e a 20 °C, 0,9982: a diferença é de 0,2%, e em medidas de espécime costuma se ignorar. Na prática, G e ρ (em g/cm³) coincidem nos três primeiros algarismos, e é por isso que as fichas escrevem "densidade 2,65".

### Pesar no ar e na água

Pelo princípio de Arquimedes, um corpo mergulhado "perde" peso igual ao peso da água que desloca. Se W_ar é a massa lida com o espécime no prato e W_água a massa lida com o espécime suspenso por um fio e totalmente imerso, a perda é o peso da água deslocada, e o volume do espécime é essa perda dividida pela densidade da água:

**G = W_ar / (W_ar − W_água)**

O denominador é o "peso de água de mesmo volume". A medida em quatro passos: (1) pese seco, no ar; (2) pendure no fio, imerso, sem tocar paredes nem fundo; (3) retire as **bolhas** aderidas (uma gota de detergente ajuda); (4) calcule.

**Fontes de erro.** (1) Bolhas aderidas: reduzem W_água, o que dá G menor. (2) Espécime poroso ou fissurado: a água entra, e o resultado muda com o tempo. (3) Espécime impuro ou com inclusões: a medida é da mistura, não do mineral. (4) **Amostra pequena:** a diferença W_ar − W_água fica pequena, e um erro de 0,1 g pesa muito (veja o exemplo). Para uma pedra de poucos gramas, usa-se balança de miligrama (balança de joalheiro). (5) Minerais solúveis em água (halita) ou que se alteram não se medem assim; o líquido é outro (aula 08).

Há ainda o **picnômetro** (frasco de volume conhecido) para pó, e os **líquidos densos** (por exemplo, soluções de politungstato de sódio, de uso laboratorial) para separar minerais por densidade. Líquidos densos mais antigos (bromofórmio, iodeto de metileno) são tóxicos: não se improvisam fora do laboratório.

### Densidade calculada e densidade medida

A densidade calculada (módulo 06) é a de um cristal **ideal**: fórmula exata, sem poros, sem inclusões, sem defeitos. A medida é a de um espécime real. Comparar as duas é diagnóstico:

| Se a medida é... | Pense em |
|---|---|
| **igual à calculada** (em ~1%) | espécime puro e denso; fórmula e cela corretas |
| **menor** | poros ou fissuras; inclusões leves; **metamictização** (a perda da ordem do zircão e de outros minerais com U e Th, que expande o volume; módulo 10, aula 04) |
| **maior** | inclusões pesadas (óxidos, sulfetos); substituição por átomo mais pesado |

Quando a composição do espécime difere da da fórmula ideal, a **solução sólida** muda ρ. É assim que se usa a densidade para estimar a composição de uma série contínua, como a da olivina, de forsterita (Mg₂SiO₄, ρ ≈ 3,28) a faialita (Fe₂SiO₄, ρ ≈ 4,39).

## Exemplo trabalhado

**Problema.** (a) Um espécime de 47,7 g no ar e 32,7 g suspenso na água. Calcule G, com a incerteza se cada pesagem tem ±0,1 g, e diga que minerais da tabela são compatíveis. (b) Um grão de olivina com densidade medida de 3,60 g/cm³: estime a composição (o **volume molar**, volume ocupado por um mol, é M/ρ: o da forsterita é 140,69/3,275 = 42,96 cm³/mol; o da faialita, 203,77/4,39 = 46,42 cm³/mol). (c) A fluorita tem Z = 4, M = 78,07 g/mol e V = 163,0 Å³. Compare a densidade calculada com a medida de 3,18.

**(a)** W_ar − W_água = 47,7 − 32,7 = 15,0 g; G = 47,7 / 15,0 = **3,18**. Com ±0,1 em cada pesagem, os valores extremos são (47,6) / (47,6 − 32,8) = 3,22 e (47,8) / (47,8 − 32,6) = 3,14: **G = 3,18 ± 0,04**. Na tabela, a fluorita (3,18) é compatível, e o diamante (3,52) e a calcita (2,71) estão fora; mas, fora da tabela, a **apatita** (cerca de 3,2) também é compatível. A densidade reduz as hipóteses, não confirma uma delas (aula 09).

**(b)** Admitindo que os volumes molares se somam (aproximação de solução ideal), a fração x de faialita sai de ρ = M / V. Passar de Mg₂SiO₄ a Fe₂SiO₄ soma 203,77 − 140,69 = 63,08 g/mol à massa e 46,42 − 42,96 = 3,46 cm³/mol ao volume; com uma fração x de faialita, M = 140,69 + 63,08x e V = 42,96 + 3,46x. Então 3,60 = (140,69 + 63,08x) / (42,96 + 3,46x); multiplicando em cruz, 154,66 + 12,46x = 140,69 + 63,08x, e x = 13,97 / 50,62 ≈ **0,28**, isto é, **cerca de Fo72Fa28**. Uma interpolação linear direta da densidade daria 0,29; as duas são próximas. O resultado é um **estimado**: erros de 0,02 g/cm³ na medida levam a alguns pontos percentuais de erro na composição, e inclusões ou poros o deslocam mais.

**(c)** ρ_calc = 4 × 78,07 / (0,6022 × 163,0) = **3,18 g/cm³**, igual à medida: espécime puro e denso.

**Método geral:** (1) pese no ar; (2) pese suspenso em água, sem bolhas; (3) G = W_ar / (W_ar − W_água); (4) propague a incerteza das pesagens; (5) compare com valores de espécies e com a densidade calculada, e interprete a diferença (poros, inclusões, solução sólida).

## Erros comuns

- **Esquecer as bolhas.** Dão G menor que o real.
- **Medir um agregado como se fosse um cristal.** O resultado é o da mistura de minerais e vazios.
- **Ignorar o tamanho do espécime.** Em amostra pequena, o erro de pesagem domina.
- **Usar o fio mergulhado sem descontar.** Em medidas de precisão, o fio entra na pesagem; ele precisa ficar o mesmo nas duas.
- **Considerar densidade e dureza correlacionadas.** O diamante (3,5) é mais duro que a galena (7,6).

## O que não concluir

- Que uma única medida de densidade identifique a espécie. Várias espécies caem na mesma faixa (apatita e fluorita; quartzo e calcedônia).
- Que a diferença entre medida e calculada seja "erro de medida". Muitas vezes é informação sobre o espécime.
- Que a densidade estimada pela solução ideal seja exata.

## Recap relâmpago

- Densidade é massa por volume; densidade relativa G é a razão com a da água (G e ρ em g/cm³ têm praticamente o mesmo número: diferem cerca de 0,2% com a água a 20 °C).
- Balança hidrostática: G = W_ar / (W_ar − W_água); cuidado com bolhas, poros, inclusões e amostras pequenas.
- Densidade calculada (cela): ρ = Z·M / (0,6022·V); comparar medida e calculada diagnostica poros, inclusões, metamictização e solução sólida.
- Na olivina, a densidade (3,28 a 4,39) permite estimar Fo/Fa; é uma estimativa.
- Densidade filtra hipóteses; não confirma.

## Próxima aula

Em [[13-propriedades-fisicas-aula-05-brilho-diafaneidade-cor-e-traco-parte-1-brilho-e-diafaneidade|Aula 05 — Brilho, diafaneidade, cor e traço, Parte 1: brilho e diafaneidade]], as propriedades ópticas macroscópicas: como a luz sai do mineral.

## Fontes consultadas

- Klein & Dutrow, *Manual of Mineral Science*, 23ª ed. (densidade, gravidade específica, método hidrostático).
- Densidades da tabela: *Handbook of Mineralogy*, D(meas.), verbetes lidos na auditoria de 2026-10-07: gipsita 2,317; halita 2,168; quartzo 2,65; calcita 2,7102; fluorita 3,175–3,184; forsterita 3,275; diamante 3,511 (calc. 3,515); faialita 4,392; barita 4,50; pirita 5,018; magnetita 5,175; hematita 5,26; galena 7,58; ouro 19,3 (o ouro nativo com prata fica abaixo disso).
- Densidade da água a 20 °C (0,9982 g/cm³): valor padrão. Cálculos de (a), (b) e (c) refeitos em Python em 2026-10-07 (G = 3,18; extremos 3,14 e 3,22; x = 0,276; ρ_calc = 3,181) e de novo na auditoria (com faialita 4,392 em vez de 4,39, x = 0,275; mesma resposta, Fo72Fa28).
- Toxicidade de bromofórmio e iodeto de metileno, e politungstato de sódio como alternativa de baixa toxicidade: orientação usual de laboratório de separação mineral.

<!--
nivel: ensino-medio-sem-geologia-v1
palavras_corpo: 1275
cobertura:
  mineralogia-m13-oa04: [Conteúdo, Exemplo trabalhado]
figuras: []
alegacoes_auditaveis:
  - claim_id: PRF-DENS-FAIXAS-001
    claim: "Densidades tipicas (g/cm3): gipsita ~2,3; halita ~2,2; quartzo 2,65; calcita ~2,71; forsterita ~3,28; fluorita ~3,18; diamante ~3,52; barita ~4,5; faialita ~4,4; pirita ~5,0; magnetita ~5,2; hematita ~5,3; galena ~7,6; ouro nativo ~19."
    risk: numero
    source: "Handbook of Mineralogy; Klein & Dutrow (conferido na auditoria de 2026-10-07)"
    audit: "verificado em 2026-10-07 (HoM D(meas.); galena corrigida para ~7,6 pelo achado 9)"
  - claim_id: PRF-DENS-HIDRO-001
    claim: "Balanca hidrostatica: G = W_ar / (W_ar - W_agua); fontes de erro: bolhas (G menor), porosidade, inclusoes, amostra pequena; agua 0,9982 g/cm3 a 20 C."
    risk: conceito
    source: "Klein & Dutrow; Arquimedes"
    audit: "verificado em 2026-10-07 (Arquimedes; agua 0,9982 a 20 C)"
  - claim_id: PRF-DENS-EXEMPLO-001
    claim: "Exemplo: 47,7 g no ar e 32,7 g na agua: G = 3,18; com +-0,1 g em cada pesagem, 3,14 a 3,22; fluorita e apatita compativeis, diamante e calcita fora."
    risk: numero
    source: "calculo em Python (2026-10-07); caso hipotetico"
    audit: "verificado em 2026-10-07 (Python: 3,180; 3,145; 3,216)"
  - claim_id: PRF-DENS-OLIVINA-001
    claim: "Olivina de densidade 3,60: x(Fa) ~0,28 (Fo72Fa28) por volumes molares aditivos (Fo 140,69/3,275 = 42,96; Fa 203,77/4,39 = 46,42 cm3/mol); interpolacao linear da densidade da 0,29."
    risk: numero
    source: "calculo em Python (2026-10-07); caso hipotetico; aproximacao de solucao ideal"
    audit: "verificado em 2026-10-07 (Python: x = 0,276 com Fa 4,39 e 0,275 com HoM 4,392; linear 0,291; aproximacao de volumes aditivos declarada no texto)"
  - claim_id: PRF-DENS-CALC-001
    claim: "Fluorita Z=4, M=78,07, V=163,0: rho calculada 3,18, igual a medida."
    risk: numero
    source: "modulo 06 aula 04; calculo em Python"
    audit: "verificado em 2026-10-07 (Python: 3,182; a = 5,4626 da V = 163,0)"
  - claim_id: PRF-DENS-METAMICT-001
    claim: "Densidade medida menor que a calculada pode indicar poros, inclusoes leves ou metamictizacao (expansao de volume em minerais com U e Th); maior, inclusoes pesadas ou substituicao por atomo mais pesado."
    risk: conceito
    source: "modulo 10 aula 04"
    audit: "verificado em 2026-10-07 (modulo 10 aula 04; HoM zircon)"
  - claim_id: PRF-DENS-LIQUIDOS-001
    claim: "Liquidos densos: politungstato de sodio de uso laboratorial; bromoformio e iodeto de metileno toxicos."
    risk: seguranca
    source: "orientacao usual de laboratorio (conferido na auditoria de 2026-10-07)"
    audit: "verificado em 2026-10-07 (orientacao de laboratorio de separacao mineral; provavel)"
  - claim_id: PRF-DENS-RECAP-001
    claim: "G e rho em g/cm3 tem praticamente o mesmo numero (diferenca ~0,2% com agua a 20 C), nao so a mesma ordem de grandeza."
    risk: conceito
    source: "agua 0,9982 g/cm3 a 20 C"
    audit: "corrigido em 2026-10-07 (achado 8)"
  - claim_id: PRF-DENS-GALENA-001
    claim: "Galena: densidade ~7,6 (HoM D(meas.) 7,58)."
    risk: numero
    source: "Handbook of Mineralogy, galena"
    audit: "corrigido em 2026-10-07 (achado 9)"
  - claim_id: PRF-DENS-DIDAT-001
    claim: "Acrescentado na revisao didatica: no exemplo (b), 42,96 e 46,42 cm3/mol sao volumes molares (M/rho), e nao 'densidade molar'; passos explicitos: 63,08 = 203,77 - 140,69 e 3,46 = 46,42 - 42,96; 3,60 x 42,96 = 154,66 e 3,60 x 3,46 = 12,46; x = 13,97 / 50,62 = 0,276."
    risk: numero
    source: "aritmetica do proprio exemplo (conferida a mao em 2026-10-07)"
    audit: "verificado em 2026-10-07, segunda passagem (Python: 42,959; 46,417; 63,08; 3,458; 154,656; 12,456; 13,97/50,62 = 0,2760; x exato 0,2758; linear 0,2915; apatita HoM 3,1-3,25)"
-->
