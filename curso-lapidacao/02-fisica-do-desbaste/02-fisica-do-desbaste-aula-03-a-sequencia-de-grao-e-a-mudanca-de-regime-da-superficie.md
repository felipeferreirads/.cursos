# Aula 03: A sequência de grão — de 60 a 100.000 e além, e onde a superfície muda de regime

**ID:** lapidacao-m02-a03
**Módulo:** [[02-fisica-do-desbaste-modulo|Módulo 02]] — Física do desbaste
**Duração estimada:** ~25 min
**Objetivo:** ordenar uma sequência de grão típica, do desbaste ao polimento, e justificar a razão de cada salto entre etapas.
**Pré-requisito:** [[02-fisica-do-desbaste-aula-02-dano-subsuperficial-e-a-logica-de-apagar-o-grao-anterior|Aula 02]] — dano subsuperficial e a lógica de apagar o grão anterior.

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **mesh** | aberturas por polegada de uma peneira — mais aberturas, partícula menor. |
| **ANSI/CAMI** | sistema norte-americano de numeração de grão, norma B74.18. |
| **FEPA (prefixo "P")** | sistema europeu de numeração de grão, escala própria. |
| **mícron (µm)** | um milionésimo de metro — mede partículas finas demais para peneira. |
| **superfície especular** | lisa o bastante para refletir a luz como um espelho. |
| **superfície difusa (fosca)** | irregular o bastante para espalhar a luz em todas as direções. |

## Antes de começar, você precisa saber

- A [[02-fisica-do-desbaste-aula-01-como-um-abrasivo-remove-materia-dureza-diferencial-e-microfratura|Aula 01]] estabeleceu a abrasão por dureza diferencial: material mais duro risca e arranca fragmentos do mais mole.
- A [[02-fisica-do-desbaste-aula-02-dano-subsuperficial-e-a-logica-de-apagar-o-grao-anterior|Aula 02]] mostrou que cada grão deixa dano subsuperficial, e que a etapa seguinte só avança quando remove essa camada inteira. Esta aula aplica essa lógica à sequência de grão e mostra onde ela termina.

## Ao final você vai conseguir

- `lapidacao-m02-oa03` — Ordenar uma sequência de grão típica, do desbaste ao polimento, e justificar a razão de cada salto entre etapas.

## Conteúdo

### Como um grão ganha um número

Imagine duas peneiras de cozinha, uma de furos largos para caldo grosso, outra de tela fina para farinha: quanto mais fina a tela, mais aberturas cabem numa polegada. É essa contagem que dá nome ao **mesh**: aberturas por polegada linear da peneira usada para separar partículas de abrasivo.

Daí a inversão que confunde todo iniciante: **número de mesh maior significa partícula menor**. O mesh mede a peneira, não a partícula — ela só é inferida por ter passado por ali.

### Os sistemas de numeração não são intercambiáveis

Existe mais de um sistema de numeração de grão, e os números **não** significam a mesma coisa entre eles. O norte-americano **ANSI/CAMI** (norma B74.18) e o europeu **FEPA**, com prefixo "P" (P220, P600), divergem pouco no grão grosso e cada vez mais no fino, onde a lapidação passa mais tempo: "600 CAMI" e "P600" não são a mesma partícula — o P600 é maior. Um número de grão só vira informação útil junto com o sistema.

### Por que o mícron é a medida inequívoca

O **mícron** (um milionésimo de metro) é a única medida que não depende de convenção. O pó de diamante é vendido das duas formas — por número de grão e por mícron —, e é o valor em mícrons que desfaz a ambiguidade. Um fio de cabelo tem entre 50 e 100 mícrons; o grão de polimento final é centenas de vezes menor.

A literatura de facetamento descreve uma sequência típica de diamante, em mícrons aproximados: cerca de 70 → 30 → 15 → 6 → 3 → 1 → 0,5 → 0,25 µm, do desbaste ao polimento final (Vargas & Vargas; United States Faceters Guild; International Gem Society) — faixas de referência, não números fechados.

### Dois sistemas, o mesmo número, partículas diferentes

O quadro separa a referência ANSI/CAMI, típica do carbeto de silício, da convenção comercial do pó de diamante, que a norma B74.18 não cobre. Repare no marco 1200: o mesmo número vale ~6,5 µm num sistema e ~15 µm no outro.

| Grão e sistema | Regime aproximado | Partícula aproximada |
|---|---|---|
| 60 CAMI | desbaste grosso | da ordem de 250–270 µm |
| 220 CAMI | desbaste fino / transição | da ordem de 66 µm |
| 600 CAMI | lixamento fino | da ordem de 15 µm |
| 1200 CAMI | lixamento muito fino | da ordem de 6,5 µm |
| 600 diamante | desbaste fino | da ordem de 30 µm |
| 1200 diamante | lixamento e pré-polimento | da ordem de 15 µm |
| 3000 diamante | pré-polimento | da ordem de 6 a 7 µm |
| 8000 diamante | pré-polimento fino | da ordem de 3 µm |
| 14000 diamante | polimento inicial | da ordem de 1 µm |
| 50000 diamante | polimento | da ordem de 0,5 µm |
| 100000 diamante | polimento fino | da ordem de 0,25 µm |

### A razão entre etapas

Por que não pular direto de um grão grosso para um fino? A [[02-fisica-do-desbaste-aula-02-dano-subsuperficial-e-a-logica-de-apagar-o-grao-anterior|Aula 02]] já respondeu em princípio: cada etapa apaga o dano da anterior, e uma partícula muito menor demora demais para isso. A regra prática é reduzir a partícula por um fator moderado — da ordem de duas a três vezes — a cada etapa; um salto maior é ineficiente, não só arriscado.

### Onde a superfície muda de regime

A superfície passa por três regimes conceitualmente distintos, não apenas "mais fino, mais fino":

1. **Desbaste**, ou **preformação** — dar ao bruto a forma aproximada da peça. Remove-se volume; a superfície é irrelevante, pois será refeita adiante.
2. **Lixamento e pré-polimento.** A geometria já está definida; o trabalho passa a remover o dano da etapa anterior. A superfície fica mais lisa, mas ainda **difusa**, porque suas irregularidades ainda são grandes demais para a luz.
3. **Polimento.** A remoção de matéria cai a quase nada; deixa de ser "tirar material" e passa a ser "gerar superfície opticamente especular" — a fronteira entre 2 e 3 é o ponto de virada da aula.

### O critério óptico da virada

Por que a virada acontece exatamente ali? A luz viaja como onda, e o **comprimento de onda** é o tamanho dessa ondulação: 0,4 a 0,7 µm na luz visível. Uma onda ignora o que é menor que ela — a maré passa sobre uma pedra sem se desmanchar. Daí o critério: a superfície espalha a luz enquanto suas irregularidades são maiores que essa escala, e a reflete de forma organizada quando caem abaixo dela. É o argumento físico por trás de onde a sequência termina: a rugosidade fica menor que a própria luz que a revelaria.

### E além

Se o critério é a rugosidade cair abaixo do comprimento de onda, por que não parar no grão mais fino? Porque, passado certo ponto, o mecanismo deixa de ser só abrasão de partícula contra mineral.

Controvérsia sem resposta única: onde termina o pré-polimento e começa o polimento não tem definição consensual — parte da literatura trata o "pré-polimento" como polimento num regime mais grosso, não como etapa distinta.

## Exemplo trabalhado

Uma peça está em grão 600 de diamante, partícula da ordem de 30 µm. Dois caminhos: (a) 600 → 1200 → 3000 → 8000; ou (b) pular direto de 600 para 8000. Em (b), o 8000 trabalha com partículas da ordem de 3 µm — pequenas demais para arrancar rápido o dano de dezenas de mícrons deixado pelo 600: a razão entre as partículas é de cerca de dez vezes, muito além da faixa de 2× a 3×, e o tempo para apagar esse dano cresce de forma desproporcional. Em (a), cada etapa reduz o dano a uma escala que a seguinte apaga em tempo razoável — e o caminho percorre os três regimes: 600 é desbaste; 1200 e 3000 são pré-polimento, superfície lisa mas difusa; só perto de 50000 ela vira especular.

## Erros comuns

- **Citar um número de grão sem o sistema.** "600" é ambíguo entre 600 CAMI, P600 FEPA e 600 de diamante.
- **Achar que "mais grão" sempre é mais fino.** Só vale dentro do mesmo sistema.
- **Achar a mudança de regime proporcional ao número de grão.** É fronteira conceitual, não rampa contínua.
- **Achar que pular etapas é só "mais arriscado".** O problema central é ineficiência.

## O que não concluir

- Que os valores em mícrons sejam exatos, ou que a sequência de oito etapas seja a única correta — são aproximações típicas da literatura.
- Que o mecanismo do polimento já foi explicado — esta aula só situa onde a superfície muda de regime.
- Que ANSI/CAMI, FEPA "P" e a convenção do diamante convertem entre si por fórmula simples.

## Recap relâmpago

- Mesh conta aberturas por polegada: número maior é partícula menor.
- ANSI/CAMI e FEPA "P" divergem mais no grão fino; um número só faz sentido com o sistema declarado.
- O mícron é a medida inequívoca: "1200" vale ~6,5 µm em CAMI e ~15 µm na convenção do diamante.
- Reduzir a partícula por um fator moderado (2× a 3×) a cada etapa evita saltos ineficientes.
- A superfície atravessa três regimes — desbaste, pré-polimento, polimento — que mudam de objetivo, não só de grão.
- A virada para polimento é critério óptico: rugosidade abaixo do comprimento de onda da luz (0,4–0,7 µm).

## Próxima aula

Na [[02-fisica-do-desbaste-aula-04-polimento-microabrasao-acao-quimico-mecanica-e-a-camada-de-beilby|Aula 04 — Polimento não é desbaste fino]], o gancho desta aula se resolve.

## Fontes consultadas

- Vargas & Vargas, *Faceting for Amateurs*; United States Faceters Guild — sequência de diamante em mícrons.
- Sinkankas, *Gem Cutting: A Lapidary's Manual*; Wykoff, *Beginner's Guide to Faceting*.
- Normas ANSI/CAMI B74.18 e FEPA-P.
- International Gem Society, *Gem Cutting Abrasives in Grit, Mesh, and Microns* — conversão grão↔mícron do pó de diamante.
- Trevor Hannam, *Faceting Made Easy* — corrobora, como fonte amadora, a progressão 1200/3000/50000 mesh.

<!--
nivel: ensino-medio-com-gemologia-v1
palavras_corpo: 1599
cobertura:
  lapidacao-m02-oa03: [Conteúdo, Exemplo trabalhado]
alegacoes_auditaveis:
  - claim_id: SEQ-MESH-NUM-001
    claim: "O numero de mesh e a contagem de aberturas por polegada linear da peneira usada para separar particulas de abrasivo; numero maior de mesh corresponde a particula menor."
    risk: definicao
    source: "ANSI/CAMI B74.18; literatura geral de abrasivos"
  - claim_id: SEQ-CAMI-FEPA-001
    claim: "ANSI/CAMI e FEPA (prefixo P) sao sistemas de numeracao de grao distintos e nao intercambiaveis; a divergencia entre os dois cresce no extremo fino da escala."
    risk: valor
    source: "ANSI/CAMI B74.18; FEPA-P; Vargas & Vargas, Faceting for Amateurs"
  - claim_id: SEQ-P600-CAMI-001
    claim: "P600 FEPA e 600 CAMI nao correspondem a mesma particula; o P600 tende a uma particula maior que o 600 CAMI."
    risk: valor
    source: "FEPA-P; ANSI/CAMI B74.18"
  - claim_id: SEQ-DIAM-MICR-001
    claim: "O po de diamante e vendido tanto por numero de grao quanto por micrometro, e o valor em micrometros e o unico inequivoco, porque a conversao numero-micron depende do sistema de numeracao usado."
    risk: mecanismo
    source: "International Gem Society, Gem Cutting Abrasives in Grit, Mesh and Microns; Vargas & Vargas, Faceting for Amateurs; United States Faceters Guild"
  - claim_id: SEQ-DIAM-SEQ-001
    claim: "Uma sequencia tipica de diamante descrita na literatura de facetamento vai, em micrometros aproximados, de cerca de 70 a 0,25, passando por marcos da ordem de 30, 15, 6, 3, 1 e 0,5."
    risk: valor
    source: "International Gem Society, Gem Cutting Abrasives in Grit, Mesh and Microns; Vargas & Vargas, Faceting for Amateurs; United States Faceters Guild"
  - claim_id: SEQ-TAB-MARCOS-001
    claim: "Na referencia ANSI/CAMI os marcos 60, 220, 600 e 1200 correspondem a cerca de 250 a 270, 66, 15 e 6,5 micrometros; na convencao comercial do po de diamante os marcos 600, 1200, 3000, 8000, 14000, 50000 e 100000 correspondem a cerca de 30, 15, 6 a 7, 3, 1, 0,5 e 0,25 micrometros."
    risk: valor
    source: "ANSI/CAMI B74.18; International Gem Society, Gem Cutting Abrasives in Grit, Mesh and Microns"
  - claim_id: SEQ-COLIS-1200-001
    claim: "O numero de grao 1200 corresponde a cerca de 6,5 micrometros na referencia ANSI/CAMI e a cerca de 15 micrometros na convencao comercial do po de diamante, ou seja, o mesmo numero designa particulas diferentes em sistemas diferentes."
    risk: valor
    source: "ANSI/CAMI B74.18; International Gem Society, Gem Cutting Abrasives in Grit, Mesh and Microns"
  - claim_id: SEQ-RAZAO-RED-001
    claim: "A pratica descrita na literatura lapidaria recomenda reduzir o tamanho de particula por um fator da ordem de duas a tres vezes a cada etapa da sequencia de grao."
    risk: conceitual
    source: "Sinkankas, Gem Cutting: A Lapidary's Manual; Vargas & Vargas, Faceting for Amateurs"
  - claim_id: SEQ-REGIM-LAMB-001
    claim: "Uma superficie passa a refletir a luz de forma especular, em vez de espalha-la de forma difusa, quando suas irregularidades caem abaixo da ordem do comprimento de onda da luz visivel, situado entre aproximadamente 0,4 e 0,7 micrometro."
    risk: mecanismo
    source: "Optica geral (comprimento de onda da luz visivel); Sinkankas, Gem Cutting: A Lapidary's Manual"
  - claim_id: SEQ-HANNAM-COR-001
    claim: "A progressao amadora de po de diamante 1200, 3000 e 50000 mesh mencionada por Trevor Hannam em Faceting Made Easy corrobora, como fonte secundaria, a existencia pratica dessa sequencia na literatura lapidaria de facetamento."
    risk: controverso
    source: "Trevor Hannam, Faceting Made Easy (2000)"
-->
