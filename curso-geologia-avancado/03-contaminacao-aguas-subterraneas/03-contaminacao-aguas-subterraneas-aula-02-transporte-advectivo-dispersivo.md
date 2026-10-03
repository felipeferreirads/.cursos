# Aula 02: Transporte de solutos em subsuperfície: advecção e dispersão hidrodinâmica

**ID:** geologia-avancado-m03-a02
**Módulo:** [[03-contaminacao-aguas-subterraneas-modulo|Módulo 03 — Contaminação dos recursos hídricos subterrâneos]]
**Duração estimada:** ~29 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** calcular a velocidade de transporte advectivo de um soluto e explicar como a dispersão hidrodinâmica espalha uma pluma de contaminação além do que a advecção sozinha preveria.
**Pré-requisito:** conceito de fonte contaminante e carga (Aula 01); Lei de Darcy e velocidade de fluxo subterrâneo (Módulo 01).

## Antes de começar, você precisa saber

- A Lei de Darcy e a distinção entre condutividade hidráulica (K), gradiente hidráulico (i) e porosidade (n), do Módulo 01.
- O conceito de fonte contaminante e carga contaminante (Aula 01).

## Conteúdo

### Advecção: o soluto viaja com a água

O **transporte advectivo** é o movimento de um soluto dissolvido junto com o fluxo da água subterrânea, na mesma direção e, em princípio, na mesma velocidade da água. É o processo dominante de transporte na maioria dos aquíferos: se não houvesse mais nenhum outro processo atuando, uma pluma de contaminante se moveria como um bloco compacto, à velocidade da água, sem se espalhar nem se diluir.

A velocidade relevante para o transporte não é a velocidade de Darcy (v_D = K×i, o fluxo por área total da seção, incluindo os grãos sólidos), mas a **velocidade linear média** (também chamada velocidade intersticial ou de poro), que é a velocidade real com que a água — e o soluto nela dissolvido — se move através dos vazios interconectados:

**v_x = (K × i) / n_e**

onde n_e é a **porosidade efetiva** (a fração do volume total ocupada por poros interconectados que efetivamente conduzem água, geralmente menor que a porosidade total em rochas com poros isolados ou em argilas com água fortemente adsorvida — Módulo 01).

> [!important] Por que dividir por n_e, e não por n total
> A velocidade de Darcy descreve uma vazão distribuída sobre toda a área da seção transversal, como se a água ocupasse 100% do espaço. Mas a água só flui pelos poros interconectados — dividir por n_e "concentra" essa mesma vazão apenas no espaço onde ela de fato ocorre, dando a velocidade real com que uma partícula de água (e o soluto que carrega) avança. Usar a porosidade total em vez da efetiva subestima a velocidade real em meios com porosidade não conectada significativa (rochas vulcânicas vesiculares, por exemplo).

Com a velocidade linear média, o tempo de trânsito advectivo entre a fonte e um ponto a jusante, a uma distância L, é simplesmente t = L / v_x — a base de qualquer estimativa preliminar de "quando" um contaminante deve chegar a um poço de captação ou a um corpo d'água receptor.

### Dispersão hidrodinâmica: por que a pluma real é maior do que a advecção prevê

Na prática, uma pluma de contaminante nunca se comporta como o bloco compacto que a advecção pura preveria — ela se espalha, dilui-se nas bordas e desenvolve uma frente que avança gradualmente, não abruptamente. Esse espalhamento adicional é a **dispersão hidrodinâmica**, soma de dois mecanismos físicos distintos (Freeze & Cherry, 1979; Fetter, 1999):

**Dispersão mecânica:** resulta da heterogeneidade da trajetória da água em escala de poro e de meio poroso — a água não viaja em linhas retas paralelas com velocidade uniforme. Três causas se combinam:
- Dentro de um mesmo poro, a água no centro do canal viaja mais rápido que a água próxima às paredes dos grãos (atrito).
- Poros de diâmetros diferentes conduzem água em velocidades diferentes — poros maiores, mais rápido.
- A trajetória da água contorna os grãos sólidos, alongando o caminho percorrido em relação à distância em linha reta.

O resultado líquido é que moléculas de soluto partindo juntas da fonte chegam a tempos ligeiramente diferentes a um mesmo ponto a jusante, espalhando a frente de concentração.

**Difusão molecular:** o movimento aleatório de moléculas por agitação térmica (movimento browniano), que ocorre mesmo sem fluxo de água algum, das regiões de maior para as de menor concentração (lei de Fick). Em aquíferos com velocidade de fluxo apreciável, a difusão molecular costuma ser desprezível frente à dispersão mecânica; ela se torna relevante apenas em meios de baixíssima condutividade hidráulica (argilas compactas, aquitardos), onde o fluxo advectivo é muito lento.

> [!note] Dispersão mecânica e difusão molecular são somadas, não escolhidas
> O **coeficiente de dispersão hidrodinâmica** (D) usado nas equações de transporte é a soma do coeficiente de dispersão mecânica com o coeficiente de difusão molecular. Em quase todos os aquíferos de interesse prático (areia, cascalho, rocha fraturada com fluxo ativo), a dispersão mecânica domina amplamente essa soma — a difusão molecular só ganha peso relativo em meios praticamente estagnados.

### Dispersividade: longitudinal e transversal

A magnitude da dispersão mecânica é descrita pela **dispersividade** (α), uma propriedade do meio poroso com dimensão de comprimento, que relaciona o coeficiente de dispersão à velocidade de fluxo:

D_mecânica = α × v_x

A dispersividade não é isotrópica: o espalhamento é maior na direção do fluxo do que perpendicular a ele, porque as variações de velocidade que geram a dispersão mecânica atuam mais fortemente ao longo da trajetória do que através dela. Por isso se distinguem:

- **Dispersividade longitudinal (α_L):** na direção do fluxo — controla o alongamento da pluma ao longo do eixo de transporte.
- **Dispersividade transversal (α_T):** perpendicular ao fluxo (horizontal e vertical) — controla o alargamento lateral e o espessamento vertical da pluma. É tipicamente 5 a 20 vezes menor que a longitudinal (Gelhar et al., 1992, síntese de dados de campo).

Um aspecto contraintuitivo, bem documentado empiricamente, é que a dispersividade **aumenta com a escala da observação**: valores medidos em ensaios de laboratório (centímetros) são ordens de grandeza menores que valores retrocalculados de plumas reais em campo (centenas de metros a quilômetros), porque em escala de campo a dispersão observada incorpora heterogeneidades de condutividade hidráulica em múltiplas escalas (camadas, lentes, fraturas) que um ensaio de laboratório, num único tipo de meio homogêneo, não captura. Esse é o chamado **efeito de escala da dispersividade**, e é a razão pela qual dispersividade de laboratório não deve ser usada diretamente para modelar uma pluma de campo sem calibração.

### A equação de advecção-dispersão

Combinando os dois processos, o transporte unidimensional de um soluto conservativo (que não sofre retardação nem degradação — conceitos da Aula 03) numa direção x é descrito pela **equação de advecção-dispersão (ADE)**:

∂C/∂t = D_L × ∂²C/∂x² − v_x × ∂C/∂x

onde o primeiro termo à direita representa o espalhamento por dispersão (proporcional à curvatura do perfil de concentração) e o segundo, o deslocamento por advecção (proporcional ao gradiente de concentração ao longo de x).

Para uma fonte contínua de concentração constante C₀, injetada num meio inicialmente limpo, a solução analítica clássica (Ogata & Banks, 1961) para a concentração num ponto x, no tempo t, é:

**C(x,t)/C₀ = ½ [erfc((x − v_x t) / (2√(D_L t)))]**

onde erfc é a função erro complementar. Essa solução não precisa ser memorizada para o nível desta aula — o que importa reter é sua forma qualitativa: ela descreve uma frente de concentração que não é um degrau abrupto (como a advecção pura preveria), mas uma curva em "S" suavizada, centrada aproximadamente na posição advectiva (x = v_x t) e alargada pela dispersão, com a suavização mais pronunciada quanto maior D_L em relação a v_x.

> [!warning] O centro da pluma se move pela advecção; a forma da frente é definida pela dispersão
> Um erro comum é achar que "mais dispersão" significa "a pluma chega mais rápido". Não: a posição central da frente ainda avança na velocidade advectiva v_x. A dispersão apenas alarga a distribuição em torno desse centro — por isso uma pequena fração da massa do soluto chega **antes** do tempo puramente advectivo (a "cauda dianteira" da curva em S), o que é justamente o motivo de monitoramento de poços a jusante começar antes do tempo de trânsito advectivo calculado ingenuamente.

## Exemplo trabalhado

**Situação:** um aquífero arenoso tem condutividade hidráulica K = 8 m/dia, gradiente hidráulico i = 0,004 (m/m) e porosidade efetiva n_e = 0,25. Uma fonte contínua de contaminante está a 120 m a montante de um poço de monitoramento, na direção do fluxo. Estime a velocidade linear média e o tempo de trânsito advectivo até o poço.

**Cálculo:**

Velocidade de Darcy: v_D = K × i = 8 m/dia × 0,004 = 0,032 m/dia

Velocidade linear média: v_x = v_D / n_e = 0,032 / 0,25 = 0,128 m/dia

Tempo de trânsito advectivo: t = L / v_x = 120 m / 0,128 m/dia ≈ 938 dias ≈ 2,6 anos

**Interpretação:** essa é a estimativa do tempo em que o **centro** da frente de concentração (C/C₀ = 0,5 na solução de Ogata-Banks) alcançaria o poço, assumindo transporte puramente advectivo-dispersivo, sem retardação nem degradação (Aula 03 mostra como esses processos alteram — em geral retardam — essa estimativa). Por causa da dispersão longitudinal, uma fração pequena, porém detectável, do contaminante deve chegar ao poço **antes** dos 2,6 anos calculados — por isso um programa de monitoramento bem projetado não espera o tempo de trânsito advectivo completo para começar a amostrar, e sim inicia com folga de segurança.

## Erros comuns

- **Usar a velocidade de Darcy (v_D) diretamente como velocidade de transporte do contaminante**, sem dividir pela porosidade efetiva — subestima grosseiramente a velocidade real de avanço.
- **Confundir porosidade efetiva com porosidade total**, especialmente em meios com porosidade não conectada (algumas rochas vulcânicas, sedimentos com matriz argilosa) — usar a porosidade total superestima n_e e, portanto, subestima v_x.
- **Achar que dispersão maior significa chegada mais rápida da pluma.** A dispersão alarga a distribuição em torno do centro advectivo; não acelera o centro da pluma.
- **Aplicar a dispersividade medida em laboratório diretamente a uma pluma de campo**, ignorando o efeito de escala — subestima substancialmente o espalhamento real observado em campo.
- **Tratar α_L e α_T como iguais.** A dispersividade transversal é tipicamente uma fração pequena (1/5 a 1/20) da longitudinal; tratá-las como iguais superestima o espalhamento lateral e vertical da pluma.

## O que não concluir

- **Que a equação de Ogata-Banks descreve qualquer contaminante em qualquer aquífero.** Ela assume um soluto conservativo (sem sorção nem degradação), meio homogêneo e fonte de concentração constante — condições raramente satisfeitas de forma exata em campo; serve como aproximação de primeira ordem e como base conceitual para os modelos mais completos da Aula 03.
- **Que um contaminante "não detectado" num poço antes do tempo de trânsito advectivo calculado prova que a pluma não está migrando.** A curva em S da solução de Ogata-Banks tem cauda; concentrações muito baixas na frente de avanço podem estar abaixo do limite de detecção sem que isso signifique ausência de migração.

## Recap relâmpago

- **Advecção:** o soluto se move com a água, à velocidade linear média **v_x = (K × i) / n_e** — não à velocidade de Darcy.
- **Dispersão hidrodinâmica = dispersão mecânica (heterogeneidade da trajetória em escala de poro) + difusão molecular** (geralmente desprezível fora de meios de baixíssima condutividade).
- **Dispersividade (α)** relaciona o coeficiente de dispersão à velocidade (D = α × v_x); é maior na direção longitudinal que na transversal, e aumenta com a escala de observação (efeito de escala) — dispersividade de laboratório subestima a de campo.
- A **equação de advecção-dispersão** (solução de Ogata-Banks para fonte contínua) produz uma frente em forma de S, centrada na posição advectiva e alargada pela dispersão — parte da massa chega antes do tempo puramente advectivo.

## Próxima aula

[[03-contaminacao-aguas-subterraneas-aula-03-retardacao-e-atenuacao|Aula 03 — Retardação e atenuação: sorção, biodegradação e atenuação natural monitorada]]

## Anterior

[[03-contaminacao-aguas-subterraneas-aula-01-conceito-de-contaminacao-e-fontes|Aula 01 — Conceito de contaminação e fontes: atividades humanas geradoras e carga contaminante]]

## Fontes

- Velocidade linear média e porosidade efetiva: Freeze, R. A. & Cherry, J. A. (1979), *Groundwater*, Prentice-Hall, cap. 2 e 9.
- Dispersão mecânica, difusão molecular e dispersividade: Fetter, C. W. (1999), *Contaminant Hydrogeology*, 2ª ed., Prentice Hall, cap. 2.
- Efeito de escala da dispersividade e razão α_L/α_T: Gelhar, L. W., Welty, C. & Rehfeldt, K. R. (1992), "A critical review of data on field-scale dispersion in aquifers", *Water Resources Research*, 28(7), 1955–1974.
- Solução analítica de fonte contínua: Ogata, A. & Banks, R. B. (1961), "A solution of the differential equation of longitudinal dispersion in porous media", USGS Professional Paper 411-A.

<!--
nivel: avancado
palavras_corpo: ~1900

mapa_objetivo_secao:
  geologia-avancado-m03-oa02: "Advecção: o soluto viaja com a água" + "Dispersão hidrodinâmica: por que a pluma real é maior do que a advecção prevê" + "Dispersividade: longitudinal e transversal" + "A equação de advecção-dispersão" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: CONTAM-M03-A02-VLINEAR-001
    claim: "A velocidade linear média (velocidade intersticial) é vx = (K x i) / ne, onde ne é a porosidade efetiva; é a velocidade relevante para o transporte de soluto, distinta da velocidade de Darcy."
    risk: fato
    source: "Freeze & Cherry 1979, cap. 2 e 9"
  - claim_id: CONTAM-M03-A02-DISPERSAO-002
    claim: "A dispersão hidrodinâmica é a soma da dispersão mecânica (heterogeneidade de trajetória em escala de poro) e da difusão molecular (movimento browniano); a difusão molecular é geralmente desprezível frente à dispersão mecânica exceto em meios de condutividade hidráulica muito baixa."
    risk: fato
    source: "Fetter 1999, cap. 2; Freeze & Cherry 1979, cap. 9"
  - claim_id: CONTAM-M03-A02-DISPERSIVIDADE-003
    claim: "A dispersividade transversal é tipicamente 5 a 20 vezes menor que a longitudinal, e a dispersividade aumenta com a escala de observação (efeito de escala), com valores de laboratório sistematicamente menores que valores retrocalculados de plumas de campo."
    risk: fato
    source: "Gelhar, Welty & Rehfeldt 1992, Water Resources Research 28(7)"
  - claim_id: CONTAM-M03-A02-OGATABANKS-004
    claim: "A solução analítica de Ogata-Banks (1961) para transporte 1D de soluto conservativo com fonte contínua de concentração constante é C(x,t)/C0 = 1/2 erfc((x - vx*t)/(2*sqrt(DL*t)))."
    risk: fato
    source: "Ogata & Banks 1961, USGS Professional Paper 411-A"
-->
