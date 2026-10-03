# Aula 01: Caracterização e classificação dos solos: granulometria, limites de Atterberg, SUCS e AASHTO

**ID:** geologia-avancado-m06-a01
**Módulo:** [[06-elementos-de-geomecanica-modulo|Módulo 06 — Elementos de geomecânica]]
**Duração estimada:** ~28 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** determinar a distribuição granulométrica e os limites de Atterberg de um solo e classificá-lo pelos sistemas SUCS (USCS) e AASHTO.
**Pré-requisito:** noções de intemperismo e formação de solos residuais e transportados (curso base); nenhum conceito do Módulo 05 é usado diretamente aqui — o Módulo 05 funciona como pré-requisito curricular (mecânica de rochas como contraponto conceitual à mecânica dos solos), não como base direta.

## Antes de começar, você precisa saber

- Que solo, em geotecnia, é qualquer material inconsolidado formado por partículas minerais (e eventualmente orgânicas) com vazios entre elas, preenchidos por ar e/ou água — em oposição à rocha, um agregado coeso de minerais.
- Frações granulométricas qualitativas (pedregulho, areia, silte, argila) como já usadas em descrição de campo.

## Conteúdo

### Por que classificar solos: da descrição à previsão de comportamento

Duas amostras que parecem semelhantes a olho nu — ambas "terra marrom-clara" — podem se comportar de modo radicalmente diferente sob carga: uma drena rápido e ganha resistência com a compactação, a outra retém água, incha e perde resistência ao ser remoldada. Um **sistema de classificação de solos** existe para substituir essa ambiguidade por uma sigla reprodutível (por exemplo, "CL" ou "SW") que já carrega, embutida, uma previsão qualitativa de comportamento — permeabilidade relativa, compressibilidade, aptidão como material de aterro. Os dois sistemas usados neste módulo, o **SUCS** (Sistema Unificado de Classificação de Solos, do inglês *USCS — Unified Soil Classification System*) e o **AASHTO** (American Association of State Highway and Transportation Officials), partem dos mesmos dois ensaios de base — granulometria e limites de Atterberg — mas os combinam com lógicas diferentes, porque nasceram para propósitos diferentes: o SUCS para engenharia geotécnica geral, o AASHTO para pavimentação rodoviária.

### Análise granulométrica: peneiramento e sedimentação

A **distribuição granulométrica** descreve a proporção, em massa, de partículas em cada faixa de tamanho. Para a fração grossa (partículas retidas na peneira nº 200, abertura 0,075 mm), usa-se **peneiramento**: uma série de peneiras de abertura decrescente (por exemplo, 4,75 mm — peneira nº 4 — até 0,075 mm) é agitada mecanicamente, e a massa retida em cada peneira dá a porcentagem passante acumulada. Para a fração fina (silte e argila, que passam na peneira nº 200), o peneiramento não funciona — as partículas são finas demais para separar mecanicamente — e usa-se **sedimentação** (ensaio do densímetro), baseada na lei de Stokes: partículas maiores sedimentam mais rápido numa suspensão em repouso, e a densidade da suspensão medida ao longo do tempo permite inferir a distribuição de tamanhos abaixo de 0,075 mm.

O resultado é plotado como uma **curva granulométrica** (porcentagem passante acumulada, em escala logarítmica de diâmetro, no eixo x). Duas leituras diretas da curva resumem sua forma:

- **Coeficiente de uniformidade:** Cu = D60/D10, onde D60 e D10 são os diâmetros abaixo dos quais passam 60% e 10% da massa, respectivamente. Cu alto (curva "esticada", partículas de tamanhos muito variados) indica solo **bem graduado**; Cu próximo de 1 (curva íngreme, partículas de tamanho parecido) indica solo **mal graduado** (uniforme).
- **Coeficiente de curvatura:** Cc = (D30)² / (D10 · D60). Usado junto com Cu para verificar se a curva tem uma forma suave e contínua (sem um salto abrupto que indicaria ausência de uma faixa intermediária de tamanhos, um solo "descontínuo" apesar de ter Cu alto).

> [!important] "Bem graduado" não é o mesmo que "boa qualidade"
> Um solo bem graduado (Cu alto, curva contínua) tende a compactar-se com maior densidade e menor índice de vazios — as partículas menores preenchem os vazios entre as maiores — o que geralmente favorece resistência e reduz permeabilidade. Mas "bem graduado" é uma descrição da forma da curva, não um veredito de qualidade absoluta: um material bem graduado de partículas fracas (por exemplo, um solo residual com grãos alteráveis) pode ser inferior, para uma dada aplicação, a um material uniforme de grãos duros e limpos.

### Limites de Atterberg: os estados de consistência de um solo fino

Para a fração fina (silte e argila), o comportamento mecânico depende fortemente do teor de umidade — o mesmo material pode se comportar como um líquido viscoso, uma massa plástica moldável, um sólido que ainda se deforma sem trincar, ou um sólido rígido, dependendo de quanta água contém. Os **limites de Atterberg**, propostos pelo agrônomo sueco Albert Atterberg e padronizados por Arthur Casagrande, definem os teores de umidade nas transições entre esses estados:

- **Limite de liquidez (LL):** teor de umidade (%, em relação à massa seca) na transição entre o estado líquido e o plástico. Determinado pelo ensaio da concha de Casagrande (número de golpes para fechar um sulco padronizado) ou pelo cone de penetração.
- **Limite de plasticidade (LP):** teor de umidade na transição entre o estado plástico e o semissólido, determinado como a umidade na qual um cilindro de solo rolado à mão de 3 mm de diâmetro começa a fissurar.
- **Limite de contração (LC):** teor de umidade abaixo do qual uma redução adicional de água não provoca mais redução de volume do solo (o solo atinge sua densidade seca máxima por secagem).

A diferença entre os dois primeiros — o **índice de plasticidade**, IP = LL − LP — mede a amplitude do intervalo de umidade em que o solo se comporta como um material plástico moldável. Um IP alto (argilas plásticas) indica um material que tolera grande variação de umidade permanecendo trabalhável, mas também tipicamente mais compressível e mais sensível a variações de umidade em serviço (expansão e contração); um IP baixo ou nulo (siltes não plásticos) indica um material que passa rapidamente do estado líquido ao quebradiço, com pouca margem plástica.

### A carta de plasticidade e a linha A

Casagrande organizou os resultados de LL e IP de milhares de solos num gráfico — a **carta de plasticidade** — com LL no eixo horizontal e IP no eixo vertical, e observou que os pontos se organizam em agrupamentos separáveis por uma linha empírica, a **linha A**:

IP = 0,73 (LL − 20)

Solos que caem **acima** da linha A (IP relativamente alto para seu LL) são predominantemente **argilas** (comportamento coesivo, plástico); solos que caem **abaixo** dela são predominantemente **siltes** ou **solos orgânicos** (comportamento com menor coesão intrínseca e maior influência da fração de silte). Uma segunda linha, a **linha U** (IP = 0,9(LL−8)), marca o limite superior prático observado empiricamente — poucos solos naturais caem acima dela, e um ponto ali costuma indicar erro de ensaio. O próprio valor de LL, dividido no limiar convencional de 50%, separa solos de **baixa compressibilidade** (LL < 50, sufixo "L") de **alta compressibilidade** (LL ≥ 50, sufixo "H").

### O Sistema Unificado de Classificação de Solos (SUCS/USCS)

O SUCS classifica o solo em três etapas sucessivas:

1. **Fração dominante:** se mais de 50% da massa é retida na peneira nº 200, o solo é de **granulação grossa** (símbolo principal G — pedregulho, ou S — areia, conforme a peneira nº 4 separe a fração predominante). Se mais de 50% passa na peneira nº 200, o solo é de **granulação fina** (símbolo principal M — silte, C — argila, ou O — orgânico).
2. **Para solos grossos**, o segundo símbolo distingue graduação e finos associados: W (bem graduado, *well graded*) ou P (mal graduado, *poorly graded*) quando os finos são menos de 5%; M ou C quando os finos excedem 12% (o comportamento passa a ser controlado pela fração fina); e uma dupla classificação (por exemplo, SW-SM) na faixa intermediária de 5–12% de finos.
3. **Para solos finos**, o segundo símbolo vem diretamente da posição na carta de plasticidade em relação à linha A e ao limiar LL=50: CL (argila de baixa plasticidade), CH (argila de alta plasticidade), ML (silte de baixa compressibilidade), MH (silte de alta compressibilidade), OL/OH para solos orgânicos.

> [!warning] Os critérios numéricos do SUCS têm limiares fixos, não são "aproximadamente"
> Os limiares de 50% (grosso vs. fino), 5% e 12% de finos, e a equação exata da linha A não são recomendações estéticas — são os critérios normativos do sistema (ASTM D2487). Um solo com 51% passante na nº 200 já muda de família (grosso→fino); um ponto a menos de 1% de IP da linha A pode mudar CL para ML. A classificação correta depende de aplicar os limiares como definidos, não de arredondar por "estar perto".

### O sistema AASHTO e o índice de grupo

O sistema **AASHTO** (adotado para subleitos rodoviários) também parte da granulometria e dos limites de Atterberg, mas organiza os solos em sete grupos principais, A-1 a A-7, ordenados do material granular de melhor desempenho como subleito (A-1) ao solo fino mais problemático (A-7), com subgrupos que refinam a graduação e a plasticidade dentro de cada grupo. Diferente do SUCS, o AASHTO calcula um **índice de grupo (GI)**, um número inteiro não negativo que resume, numa única escala, o quanto um solo fino se afasta do comportamento ideal de subleito:

GI = (F200 − 35)[0,2 + 0,005(LL − 40)] + 0,01(F200 − 15)(IP − 10)

onde F200 é a porcentagem passante na peneira nº 200. Cada termo entre colchetes é truncado em zero se resultar negativo (um valor de LL ou IP abaixo do limiar de referência não *reduz* o GI, apenas deixa de aumentá-lo), e o GI final também é truncado em zero e arredondado ao inteiro mais próximo. Quanto maior o GI, pior o desempenho esperado como subleito — um GI de 0 indica material excelente a bom, GI acima de 20 indica material muito pobre.

## Exemplo trabalhado

**Situação:** um solo tem 8% retido na peneira nº 4, 30% retido entre a peneira nº 4 e a nº 200, e 62% passante na peneira nº 200 (F200 = 62%). O ensaio de Atterberg no material passante na peneira nº 40 deu LL = 45% e LP = 22%. Classifique pelo SUCS e calcule o índice de grupo AASHTO.

**Resolução (SUCS):**

Passante na nº 200 = 62% > 50% → solo de **granulação fina**.

IP = LL − LP = 45 − 22 = 23.

Linha A no ponto LL=45: IP_A = 0,73(45−20) = 0,73×25 = 18,25. Como IP do solo (23) > IP_A (18,25), o ponto cai **acima** da linha A → família argila (C).

LL = 45% < 50 → sufixo de baixa compressibilidade (L).

**Classificação SUCS: CL** (argila inorgânica de baixa a média plasticidade).

**Resolução (AASHTO — índice de grupo):**

F200 = 62%.

Primeiro termo: (F200−35)[0,2+0,005(LL−40)] = (62−35)[0,2+0,005(45−40)] = 27×[0,2+0,025] = 27×0,225 = 6,075.

Segundo termo: 0,01(F200−15)(IP−10) = 0,01×(62−15)×(23−10) = 0,01×47×13 = 6,11.

GI = 6,075 + 6,11 = 12,185 → **GI ≈ 12** (arredondado).

**Interpretação:** um solo CL com GI≈12 é consistente com o grupo AASHTO A-7-6 (argila com LL e IP relativamente altos para subleito) — um material fino de plasticidade moderada, esperado como subleito de qualidade regular a pobre, exigindo tratamento (estabilização, drenagem) numa aplicação rodoviária, apesar de ser um solo perfeitamente utilizável, com os cuidados certos, em outras aplicações geotécnicas.

## Erros comuns

- **Aplicar os limites de Atterberg à amostra total**, sem lembrar que o ensaio é feito apenas na fração que passa na peneira nº 40 (0,425 mm) — a presença de pedregulho e areia grossa na amostra bruta não entra no cálculo de LL e LP.
- **Confundir "bem graduado" com "resistente" ou "de boa qualidade"** — a graduação descreve a forma da curva granulométrica, não a resistência dos grãos individuais nem a adequação a um uso específico.
- **Usar o valor de IP negativo (LP > LL) sem tratamento**, quando na prática isso indica solo não plástico (IP relatado como "NP", não como um número negativo) — situação comum em siltes e areias finas com pouca fração argilosa.
- **Truncar incorretamente os termos do índice de grupo AASHTO**, esquecendo que cada termo entre colchetes deve ser zerado (não deixado negativo) antes de somar, e que o próprio GI final não pode ser negativo.

## O que não concluir

- **Que SUCS e AASHTO vão sempre concordar sobre qual é "o melhor" solo.** Os dois sistemas otimizam para propósitos diferentes: o SUCS descreve comportamento geotécnico geral, o AASHTO prioriza desempenho como subleito rodoviário — um solo classificado como bom em um sistema não é automaticamente equivalente no outro, e a correspondência entre siglas SUCS e grupos AASHTO é aproximada, não uma tabela de conversão exata.
- **Que a classificação por si só substitui o ensaio de resistência ou compressibilidade.** A sigla é uma previsão qualitativa útil para triagem e comunicação entre profissionais, mas o dimensionamento de uma obra real exige os ensaios mecânicos específicos (cisalhamento, adensamento, compactação) tratados nas próximas aulas deste módulo.

## Recap relâmpago

- A granulometria (peneiramento para a fração grossa, sedimentação por lei de Stokes para a fina) e os limites de Atterberg (LL, LP, IP=LL−LP) são os dois ensaios de base de qualquer classificação de solo fino ou misto.
- Cu=D60/D10 e Cc=(D30)²/(D10·D60) descrevem a forma da curva granulométrica (graduação); a linha A da carta de plasticidade, IP=0,73(LL−20), separa argilas (acima) de siltes/orgânicos (abaixo), e LL=50% separa baixa de alta compressibilidade.
- O SUCS classifica primeiro por fração dominante (grosso se >50% retido na nº 200, fino se >50% passante), depois por graduação (grosso) ou posição na carta de plasticidade (fino), resultando em siglas como SW, CL, MH.
- O AASHTO agrupa solos em A-1 a A-7 e resume a adequação como subleito rodoviário num índice de grupo GI — calculado a partir de F200, LL e IP, sempre truncado em zero termo a termo antes de somar.
- Ambos os sistemas são ferramentas de triagem e comunicação; não substituem os ensaios mecânicos (resistência, compressibilidade) que vêm nas aulas seguintes.

## Próxima aula

[[06-elementos-de-geomecanica-aula-02-indices-fisicos-e-compactacao|Aula 02 — Índices físicos de solos e rochas e compactação]]

## Anterior

Primeira aula do módulo. Pressupõe o [[05-mecanica-de-rochas/05-mecanica-de-rochas-modulo|Módulo 05]] concluído (pré-requisito curricular).

## Fontes

- Análise granulométrica, limites de Atterberg e classificação SUCS: ASTM D2487 (*Standard Practice for Classification of Soils for Engineering Purposes — Unified Soil Classification System*); Das, B. M. (2019), *Fundamentos de Engenharia Geotécnica*, 9ª ed., Cengage, cap. 3–4.
- Carta de plasticidade e linha A: Casagrande, A. (1948), "Classification and Identification of Soils", *Transactions of the ASCE*, 113, 901–930.
- Sistema AASHTO e índice de grupo: AASHTO M 145 (*Standard Specification for Classification of Soils and Soil-Aggregate Mixtures for Highway Construction Purposes*).

<!--
nivel: avancado
palavras_corpo: ~1700

mapa_objetivo_secao:
  geologia-avancado-m06-oa01: "Por que classificar solos" + "Análise granulométrica" + "Limites de Atterberg" + "A carta de plasticidade e a linha A" + "O Sistema Unificado de Classificação de Solos (SUCS/USCS)" + "O sistema AASHTO e o índice de grupo" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOMEC-M06-A01-CUCC-001
    claim: "O coeficiente de uniformidade Cu=D60/D10 e o coeficiente de curvatura Cc=(D30)²/(D10·D60) caracterizam a graduação de um solo a partir da curva granulométrica."
    risk: fato
    source: "ASTM D2487; Das 2019, cap. 3"
  - claim_id: GEOMEC-M06-A01-LINHAA-002
    claim: "A linha A da carta de plasticidade de Casagrande é dada por IP=0,73(LL−20), separando argilas (acima) de siltes e solos orgânicos (abaixo)."
    risk: fato
    source: "Casagrande 1948; ASTM D2487"
  - claim_id: GEOMEC-M06-A01-SUCS-003
    claim: "O SUCS classifica um solo como de granulação grossa se mais de 50% da massa é retida na peneira nº 200, e fina se mais de 50% passa; solos finos são subdivididos por posição na carta de plasticidade e pelo limiar LL=50% (baixa/alta compressibilidade)."
    risk: fato
    source: "ASTM D2487"
  - claim_id: GEOMEC-M06-A01-AASHTO-GI-004
    claim: "O índice de grupo AASHTO é GI=(F200−35)[0,2+0,005(LL−40)]+0,01(F200−15)(IP−10), com cada termo entre colchetes e o resultado final truncados em zero quando negativos."
    risk: fato
    source: "AASHTO M 145"
-->
