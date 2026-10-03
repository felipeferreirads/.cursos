# Aula 04: Aterros sanitários: liners, barreiras de cobertura, projeto, operação, monitoramento e recalques

**ID:** geologia-avancado-m08-a04
**Módulo:** [[08-geotecnia-ambiental-modulo|Módulo 08 — Geotecnia ambiental]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** descrever o sistema de impermeabilização de fundo e de cobertura de um aterro sanitário, distinguir barreira de cobertura convencional de evapotranspirativa, estimar a geração de lixiviado por balanço hídrico, comparar o vazamento por liner de argila e por liner composto, e explicar os recalques de aterro, incluindo a parcela de longo prazo por biodegradação.

**Pré-requisito:** o tripé hidráulico–mecânico–químico e o alvo `K ≤ 1×10⁻⁹ m/s` ([[08-geotecnia-ambiental-aula-01-conceitos-e-propriedades-geotecnicas|Aula 01]]); pluma de lixiviado e critérios de seleção de área ([[08-geotecnia-ambiental-aula-03-residuos-solidos-e-selecao-de-areas|Aula 03]]); adensamento e compressão secundária `Cα` ([[06-elementos-de-geomecanica/06-elementos-de-geomecanica-aula-05-compressibilidade-adensamento-recalques|Módulo 06, Aula 05]]); lei de Darcy ([[06-elementos-de-geomecanica/06-elementos-de-geomecanica-aula-04-percolacao-em-meios-porosos-e-fissurados|Módulo 06, Aula 04]]).

## Antes de começar, você precisa saber

- Que uma barreira retarda, não anula, o fluxo, e que o `K` de projeto só vale para as condições de moldagem e de fluido em que foi medido — daí o ensaio de compatibilidade com o lixiviado real (Aula 01).
- Que o recalque tem parcela imediata, primária (adensamento) e secundária (`Cα`, *creep* sob `σ'` constante), e que a secundária domina o longo prazo em materiais compressíveis (Módulo 06, Aula 05).

## Conteúdo

### Sistema de impermeabilização de fundo

O objetivo é interceptar o lixiviado e limitar a vazão residual para a subsuperfície. Um sistema moderno é **composto e multicamada**, de baixo para cima:

- **Barreira inferior:** camada de argila compactada (CCL) de 0,6–1,0 m com `K ≤ 1×10⁻⁹ m/s`, ou geocomposto bentonítico (GCL), frequentemente os dois.
- **Geomembrana (GM):** polietileno de alta densidade (PEAD/HDPE) de 1,5–2,0 mm, soldada em painéis. Sobre a CCL, forma o **liner composto** — o arranjo de melhor desempenho, porque a GM elimina o fluxo advectivo pela área intacta e a CCL limita o espalhamento lateral sob qualquer furo da GM.
- **Camada de coleta de lixiviado (LCS):** brita ou geocomposto drenante com rede de drenos, que conduz o lixiviado a um poço de bombeamento e mantém a carga hidráulica sobre o liner baixa (tipicamente ≤ 0,30 m — exigência regulatória).
- **Sistema duplo com detecção de vazamento (LDS):** em aterros de resíduos perigosos, dois liners compostos com uma camada drenante entre eles; qualquer vazão nessa camada intermediária é sinal direto de furo no liner primário.

A **compatibilidade química** (Aula 01) volta aqui: a GM de PEAD é resistente à maioria dos lixiviados, mas hidrocarbonetos podem difundir através dela lentamente, e a CCL sob lixiviado orgânico pode ter o `K` degradado.

### Balanço hídrico e geração de lixiviado

A vazão de lixiviado a tratar é a percolação que atravessa a cobertura (ou a superfície da célula em operação) e alcança a massa de resíduo. Estima-se por **balanço hídrico**:

`L = P − ES − AET − ΔS`

onde `P` é a precipitação, `ES` o deflúvio superficial, `AET` a evapotranspiração real e `ΔS` a variação de armazenamento de água no perfil (nulo em média plurianual). O modelo padrão para essa conta em aterros é o **HELP** (*Hydrologic Evaluation of Landfill Performance*, USEPA), que roteia a água camada a camada — cobertura vegetal, solo de armazenamento, barreira, drenagem — com passo diário. O HELP é a ferramenta de referência para dimensionar a drenagem de lixiviado e para comparar alternativas de cobertura.

### Barreira de cobertura: convencional versus evapotranspirativa

A cobertura final tem três funções: minimizar a infiltração (e, portanto, a geração de lixiviado), conter o biogás e permitir o uso pós-fechamento.

- **Cobertura convencional (resistiva):** replica o liner de fundo — geomembrana e/ou argila compactada de baixo `K`, sob camadas de drenagem e de solo com vegetação. Ela **barra** a água por baixa condutividade. Funciona em qualquer clima, mas é vulnerável à **dessecação e fissuração** da argila e a recalques diferenciais, que abrem caminhos preferenciais.
- **Cobertura evapotranspirativa (*store-and-release*, ou ET cover):** uma camada espessa de solo de granulometria fina, sem barreira de baixo `K`, que **armazena** a água de chuva na sua capacidade de campo e a **devolve** à atmosfera por evapotranspiração da vegetação antes que ela percole. Não barra a água — administra o seu tempo de residência. É mais barata, mais tolerante a recalque (não há camada rígida a fissurar) e frequentemente mais durável, mas **só funciona onde a evapotranspiração potencial supera a precipitação** com folga: climas áridos e semiáridos. Em clima úmido, falha.

> [!important] A escolha da cobertura é climática antes de ser geotécnica
> Uma cobertura evapotranspirativa dimensionada para o semiárido nordestino e transposta para um aterro no Sul do Brasil deixaria passar volume de lixiviado inaceitável, porque o balanço `ET − P` é negativo boa parte do ano. A pergunta inicial não é "qual solo temos", e sim "o clima local permite confiar na evapotranspiração para descartar a chuva".

### Recalques de aterro

A massa de um aterro de RSU recalca de forma pronunciada — o recalque total de longo prazo chega a **15–30 % da altura**. Compõe-se de:

- **Recalque imediato:** rearranjo mecânico dos resíduos sob o peso das camadas sobrejacentes, durante a operação.
- **Adensamento primário:** dissipação de pressões de líquido e gás nos vazios, semanas a meses.
- **Compressão secundária e biodegradação:** *creep* mecânico do arcabouço de resíduo somado à **perda de massa por decomposição** da fração orgânica ao longo de décadas. Essa parcela biológica é o que torna o recalque de aterro qualitativamente diferente do recalque de solo: parte do volume simplesmente **desaparece** convertida em biogás e lixiviado.

As implicações de projeto são diretas: a cobertura deve ser projetada com declividade inicial folgada, para que ela ainda drene depois de anos de recalque diferencial; a geomembrana da cobertura precisa de deformação admissível compatível; e o uso pós-fechamento (parque, estacionamento; nunca edificação convencional) tem de tolerar o assentamento continuado e a exsudação de gás.

### Operação e monitoramento

**Operação:** disposição em células com compactação por rolo pé-de-carneiro, cobertura diária de solo (controle de vetores e de fogo), cobertura intermediária nas frentes inativas, e sistema de drenagem e queima ou aproveitamento do **biogás** (≈ 50 % CH₄), gás de efeito estufa e risco de explosão se migrar lateralmente.

**Monitoramento:** rede de poços a montante (*background*) e a jusante do aterro na direção do fluxo subterrâneo, amostrados periodicamente para indicadores de lixiviado (condutividade elétrica, cloreto, amônia, DQO, metais, compostos orgânicos). Complementam a rede os medidores de nível e de recalque (marcos superficiais), os piezômetros e os poços de gás. O monitoramento continua por décadas após o encerramento — o **período de pós-fechamento** legalmente exigido.

## Exemplo trabalhado

**Situação:** uma célula de 4,0 ha recebe cobertura. Dados climáticos e de projeto: `P = 1300 mm/ano`, deflúvio superficial 20 % de `P`, `AET = 620 mm/ano`, `ΔS ≈ 0`. O liner de fundo é composto: geomembrana de PEAD sobre CCL de 0,60 m com `K = 5×10⁻¹⁰ m/s`; a LCS mantém `hw = 0,30 m` de carga sobre o liner.
Calcule (a) a percolação anual pela cobertura e o volume de lixiviado gerado; (b) a vazão de fuga se a barreira fosse **só a CCL** (Darcy); e comente (c) o efeito da geomembrana.

**Resolução:**

**(a) Balanço hídrico da cobertura.**
`ES = 0,20 × 1300 = 260 mm/ano`
`L = P − ES − AET − ΔS = 1300 − 260 − 620 − 0 = 420 mm/ano`
Sobre 4,0 ha = 40 000 m²:
`V = 0,420 m/ano × 40 000 m² = 16 800 m³/ano ≈ 46 m³/dia`
É essa a vazão que a drenagem de lixiviado e a estação de tratamento precisam comportar.

**(b) Fuga por uma CCL isolada (sem geomembrana).**
`i = (0,60 + 0,30)/0,60 = 1,50`
`q = K·i = 5×10⁻¹⁰ × 1,50 = 7,5×10⁻¹⁰ m/s`
Em base anual: `7,5×10⁻¹⁰ × 3,156×10⁷ ≈ 0,0237 m/ano = 23,7 mm/ano`
Sobre 4,0 ha: `0,0237 × 40 000 ≈ 950 m³/ano`

**(c) Efeito da geomembrana.** Com a GM intacta sobre a CCL, não há fluxo advectivo pela área íntegra: a fuga passa a ocorrer **só através de defeitos** (furos de instalação, tipicamente poucos por hectare). Pelas expressões empíricas de Giroud & Bonaparte (1989), um furo de 1 cm² sob 0,30 m de carga, com bom contato GM–CCL e `K` da argila de 5×10⁻¹⁰ m/s, vaza cerca de 0,3 L/dia; com a densidade usual de defeitos após um bom controle de qualidade, isso dá uma fuga da ordem de **poucos litros por hectare por dia** — unidades, não dezenas. Convertido à mesma base, são ~1 a 7 m³/ano sobre os 4 ha, ou seja, **duas a três ordens de grandeza** abaixo dos ~950 m³/ano da CCL isolada. É a demonstração de por que o liner **composto** supera a soma das duas barreiras usadas em separado: a GM corta o fluxo pela área intacta, e a CCL, abaixo dela, impede que o líquido que passa por um furo se espalhe lateralmente e encontre outros caminhos. Repare também na hierarquia dos números: a fuga pelo liner (na pior hipótese, ~950 m³/ano) é pequena frente aos ~16 800 m³/ano de lixiviado que a drenagem precisa **coletar e tratar** — o gargalo operacional de um aterro bem construído é o tratamento do lixiviado captado, não o vazamento pelo fundo.

## Erros comuns

- **Somar a resistência hidráulica da GM e da CCL como se fossem barreiras independentes em série.** O ganho do liner composto vem da interação (a CCL confina o vazamento sob cada furo da GM), não da soma.
- **Especificar cobertura evapotranspirativa em clima úmido** porque é mais barata e tolerante a recalque — ela depende de `ET > P`.
- **Projetar a cobertura com a declividade final desejada.** Ela precisa de declividade inicial maior, porque o recalque diferencial vai reduzi-la ao longo de décadas.
- **Tratar o recalque de aterro como adensamento de solo.** A parcela de biodegradação remove massa; não há analogia direta com `Cc` e `Cα` de solo, embora `Cα` sirva de ponto de partida.
- **Dimensionar a drenagem de lixiviado sem balanço hídrico** ou com balanço de ano médio quando o crítico é o ano úmido.
- **Encerrar o monitoramento no fim da operação** — o período de pós-fechamento se estende por décadas.

## O que não concluir

- **Que o liner composto elimina o vazamento.** Reduz a taxa a valores muito baixos; não a zera. O monitoramento a jusante existe justamente para detectar a fração que passa.
- **Que aterro encerrado é terreno recuperado para qualquer uso.** Recalque continuado, exsudação de biogás e a integridade da cobertura restringem o uso a atividades leves e reversíveis.
- **Que o HELP fornece a vazão exata de lixiviado.** É um modelo de balanço com parâmetros incertos (curva número, capacidade de campo, índice de área foliar); usa-se com análise de sensibilidade e cenário úmido.

## Recap relâmpago

- O liner de fundo moderno é composto: CCL e/ou GCL (`K ≤ 1×10⁻⁹ m/s`) + geomembrana de PEAD 1,5–2,0 mm + camada de coleta de lixiviado que mantém a carga ≤ 0,30 m; aterros perigosos usam liner duplo com camada de detecção de vazamento.
- O liner composto supera a soma das barreiras: a GM corta o fluxo advectivo pela área intacta, a CCL confina o vazamento sob cada furo.
- A geração de lixiviado vem do balanço hídrico `L = P − ES − AET − ΔS`, calculado camada a camada pelo modelo HELP.
- Cobertura convencional (resistiva) barra a água por baixo `K` e serve em qualquer clima, mas fissura; cobertura evapotranspirativa armazena e devolve a água à atmosfera, é mais barata e tolerante a recalque, mas só funciona onde `ET > P` (semiárido).
- O recalque total de um aterro de RSU chega a 15–30 % da altura, com parcela de longo prazo por **biodegradação** (perda de massa), o que o distingue do recalque de solo; a cobertura precisa de declividade inicial folgada.
- O monitoramento usa poços a montante e a jusante na direção do fluxo, mais marcos de recalque e poços de gás, e continua por décadas no pós-fechamento.

## Próxima aula

[[08-geotecnia-ambiental-aula-05-rejeitos-de-mineracao|Aula 05 — Rejeitos de mineração: características geotécnicas, técnicas de disposição e estruturas de contenção]]

## Anterior

[[08-geotecnia-ambiental-aula-03-residuos-solidos-e-selecao-de-areas|Aula 03 — Resíduos sólidos e seleção de áreas de disposição]]

## Fontes

- Qian, X., Koerner, R. M. & Gray, D. H. (2002), *Geotechnical Aspects of Landfill Design and Construction*, Prentice Hall, cap. 4, 6, 9 e 11.
- Koerner, R. M. (2012), *Designing with Geosynthetics*, 6ª ed., Xlibris, cap. 5 e 6.
- Rowe, R. K., Quigley, R. M., Brachman, R. W. I. & Booker, J. R. (2004), *Barrier Systems for Waste Disposal Facilities*, 2ª ed., Spon Press, cap. 3, 6 e 10.
- Giroud, J. P. & Bonaparte, R. (1989), "Leakage through liners constructed with geomembranes — Part II: composite liners", *Geotextiles and Geomembranes*, 8(2), p. 71–111.
- Schroeder, P. R., Dozier, T. S., Zappi, P. A. et al. (1994), *The Hydrologic Evaluation of Landfill Performance (HELP) Model: Engineering Documentation for Version 3*, USEPA/600/R-94/168b.
- Albright, W. H., Benson, C. H. & Waugh, W. J. (2010), *Water Balance Covers for Waste Containment: Principles and Practice*, ASCE Press.
- Sowers, G. F. (1973), "Settlement of waste disposal fills", *Proceedings of the 8th International Conference on Soil Mechanics and Foundation Engineering*, Moscou, v. 2, p. 207–210.
- ABNT NBR 13896:1997, *Aterros de resíduos não perigosos — Critérios para projeto, implantação e operação*; NBR 8419:1992, *Apresentação de projetos de aterros sanitários de resíduos sólidos urbanos*.

<!--
nivel: avancado
palavras_corpo: ~2010
# Ressalva registrada na revisão didática (DID-M08-A04-EXTENSAO): acima do teto de ~1900,
# mantida por decisão — o excedente está na parte (c) do exemplo trabalhado, que é onde a
# aula demonstra por que o liner composto supera a soma das barreiras.

mapa_objetivo_secao:
  geologia-avancado-m08-oa01: "Sistema de impermeabilização de fundo" + "Barreira de cobertura: convencional versus evapotranspirativa" + "Exemplo trabalhado"
  geologia-avancado-m08-oa03: "Balanço hídrico e geração de lixiviado" + "Recalques de aterro" + "Operação e monitoramento" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOAMB-M08-A04-LINER-COMPOSTO-001
    claim: "O liner composto (geomembrana de PEAD sobre camada de argila compactada) supera o desempenho das duas barreiras usadas isoladamente, porque a geomembrana elimina o fluxo advectivo pela área intacta e a argila subjacente limita o espalhamento lateral do lixiviado sob cada defeito da geomembrana."
    risk: fato
    source: "Giroud & Bonaparte 1989; Rowe et al. 2004, cap. 6; Koerner 2012, cap. 5"
  - claim_id: GEOAMB-M08-A04-LCS-002
    claim: "A camada de coleta de lixiviado conduz o líquido a um poço de bombeamento e mantém a carga hidráulica sobre o liner baixa, tipicamente limitada a 0,30 m por exigência regulatória; aterros de resíduos perigosos usam sistema de liner duplo com camada de detecção de vazamento entre os dois liners."
    risk: fato
    source: "USEPA 40 CFR Part 258 (Subtitle D) e Part 264; Qian, Koerner & Gray 2002, cap. 4"
  - claim_id: GEOAMB-M08-A04-BALANCO-HELP-003
    claim: "A geração de lixiviado é estimada por balanço hídrico L = P − ES − AET − ΔS, sendo o modelo HELP (Hydrologic Evaluation of Landfill Performance, USEPA) a ferramenta de referência para roteá-lo camada a camada com passo diário e dimensionar a drenagem."
    risk: fato
    source: "Schroeder et al. 1994; Qian, Koerner & Gray 2002, cap. 6"
  - claim_id: GEOAMB-M08-A04-ET-COVER-004
    claim: "A barreira de cobertura evapotranspirativa (store-and-release) armazena a água de chuva na capacidade de campo de uma camada espessa de solo fino e a devolve à atmosfera por evapotranspiração, sem camada de baixa condutividade; só é adequada onde a evapotranspiração potencial supera a precipitação, isto é, climas áridos e semiáridos, e falha em clima úmido."
    risk: fato
    source: "Albright, Benson & Waugh 2010; Alternative Cover Assessment Program (ACAP), USEPA"
  - claim_id: GEOAMB-M08-A04-RECALQUE-005
    claim: "O recalque total de longo prazo de um aterro de resíduo sólido urbano atinge tipicamente 15 a 30 % da altura, com parcela de longo prazo governada pela compressão secundária somada à perda de massa por biodegradação da fração orgânica, que remove volume convertendo-o em biogás e lixiviado — o que o distingue qualitativamente do recalque de solo."
    risk: fato
    source: "Sowers 1973; Qian, Koerner & Gray 2002, cap. 11"
  - claim_id: GEOAMB-M08-A04-BIOGAS-006
    claim: "O biogás de aterro de RSU contém cerca de 50 % de metano, é gás de efeito estufa e representa risco de explosão se migrar lateralmente, exigindo sistema de drenagem com queima ou aproveitamento energético."
    risk: fato
    source: "Qian, Koerner & Gray 2002, cap. 10; Tchobanoglous, Theisen & Vigil, Integrated Solid Waste Management"
  - claim_id: GEOAMB-M08-A04-EXEMPLO-007
    claim: "Para P = 1300 mm/ano, ES = 20 % de P, AET = 620 mm/ano e ΔS = 0, a percolação é 420 mm/ano, gerando ~16 800 m³/ano (~46 m³/dia) sobre 4 ha; a fuga por uma CCL isolada de 0,60 m com K = 5×10⁻¹⁰ m/s e carga de 0,30 m é ~24 mm/ano (~950 m³/ano sobre 4 ha), reduzida em duas a três ordens de grandeza pela geomembrana sobreposta — a fuga do liner composto fica na ordem de POUCOS LITROS por hectare por dia (unidades, não dezenas), equivalente a ~1 a 7 m³/ano sobre 4 ha."
    risk: calculo
    source: "Cálculo por balanço hídrico e lei de Darcy; expressões empíricas de Giroud & Bonaparte 1989 (contato bom, furo de 1 cm², h = 0,30 m, k = 5×10⁻¹⁰ m/s → ~0,3 L/dia por furo) para a fuga por defeitos"
-->
