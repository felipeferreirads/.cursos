# Aula 04: O variograma — cálculo experimental e modelagem teórica

**ID:** geologia-avancado-m20-a04
**Módulo:** [[20-geoestatistica-modulo|Módulo 20 — Introdução à geoestatística]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** ensinar a calcular o variograma experimental a partir de dados amostrais, interpretar seus três elementos estruturais — efeito pepita, patamar e alcance —, e ajustar a ele um modelo teórico permissível, incluindo o tratamento da anisotropia introduzida na Aula 03.
**Ao final você vai conseguir:** descrever o procedimento de cálculo do variograma experimental (pares, lags, tolerâncias); interpretar efeito pepita, patamar e alcance num gráfico de variograma e relacionar cada um a uma causa geológica ou amostral; escolher entre os modelos esférico, exponencial e gaussiano com base no comportamento do variograma perto da origem e na forma como ele se aproxima do patamar; e reconhecer um variograma direcional como evidência de anisotropia.
**Pré-requisito:** [[20-geoestatistica-aula-02-variaveis-regionalizadas-funcao-aleatoria-estacionariedade|Aula 02 — Variáveis regionalizadas, função aleatória e estacionariedade]] (o variograma $\gamma(h)$ foi definido ali, sob a hipótese intrínseca, como a variância dos incrementos $Z(x+h)-Z(x)$; esta aula transforma essa definição em ferramenta calculável e ajustável) e [[20-geoestatistica-aula-03-suporte-relacao-de-krige-anisotropia|Aula 03 — Suporte, relação de Krige e anisotropia]] (a anisotropia é apresentada ali em termos conceituais; aqui ela vira procedimento, e $\bar\gamma(v,v)$, prometida ali, passa a ser calculável a partir do modelo ajustado aqui).

## Conteúdo

### Do conceito ao gráfico: o variograma experimental

A Aula 02 definiu o variograma teórico como $2\gamma(h) = \text{Var}[Z(x+h)-Z(x)]$ sob a hipótese intrínseca. Na prática, não se conhece a função aleatória $Z(x)$ — apenas um conjunto finito de dados amostrados em posições fixas. O **variograma experimental** é o estimador que a geoestatística usa para aproximar $\gamma(h)$ a partir desses dados:

$$\hat{\gamma}(h) = \frac{1}{2N(h)}\sum_{i=1}^{N(h)} [z(x_i+h) - z(x_i)]^2$$

Em palavras: para uma distância e direção fixas $h$, percorre-se o conjunto de dados procurando todos os **pares de pontos** separados aproximadamente por esse vetor $h$; calcula-se a diferença ao quadrado entre os valores de cada par; e faz-se a média dessas diferenças ao quadrado, dividida por dois. $N(h)$ é o número de pares encontrados para aquele $h$. Repetindo esse cálculo para uma sequência de distâncias crescentes (chamadas de **lags**: $h$, $2h$, $3h$, ...), obtém-se uma sequência de valores $\hat{\gamma}(h)$ que, plotada contra a distância, é o **gráfico do variograma experimental**.

Na prática, os dados raramente estão separados por distâncias exatamente iguais a um múltiplo de $h$ — sobretudo em duas ou três dimensões, onde amostras estão espalhadas de forma irregular. Por isso o cálculo usa **tolerâncias**: uma tolerância de distância (por exemplo, "pares entre 45 e 55 m" para representar o lag de 50 m) e, quando o variograma é calculado numa direção específica, uma **tolerância angular** (por exemplo, "pares cuja direção está a até 22,5° do azimute de referência"), agrupando num mesmo lag todos os pares que caem dentro dessa janela de distância e direção. Escolher tolerâncias muito estreitas produz um variograma calculado sobre poucos pares (ruidoso, $N(h)$ pequeno); tolerâncias muito largas misturam distâncias e direções diferentes, borrando a estrutura real. Esse ajuste — junto com o número e o espaçamento dos lags — é a parte mais artesanal do cálculo do variograma experimental, e normalmente exige algumas iterações antes de produzir um gráfico interpretável.

### Os três elementos estruturais do variograma

Um variograma bem comportado — calculado sobre um número razoável de pares em cada lag, para um fenômeno que satisfaz a hipótese intrínseca — tem uma forma característica: cresce a partir da origem, desacelera o crescimento e eventualmente se estabiliza num platô. Essa forma é descrita por três parâmetros que resumem a estrutura de continuidade espacial:

- **Efeito pepita (nugget effect, $C_0$)** — o valor (não nulo, na prática) do variograma extrapolado para $h=0$. Formalmente, pela própria definição, $\gamma(0)=0$: um ponto comparado consigo mesmo tem diferença zero. Mas ao extrapolar o comportamento do variograma experimental de volta até a origem, a partir dos lags mais curtos disponíveis, a curva quase sempre não passa por zero — ela intercepta o eixo vertical num valor positivo. Esse "salto" na origem é o efeito pepita, e representa duas fontes de variabilidade que o cálculo não consegue separar sem informação adicional: (1) a **variabilidade genuína de escala muito pequena** — heterogeneidade real da mineralização em distâncias menores do que o espaçamento mínimo de amostragem, que existe fisicamente mas está abaixo da resolução dos dados; e (2) o **erro de amostragem e análise** — erro de coleta, preparação e análise laboratorial, que introduz ruído mesmo quando duas amostras coincidentes (duplicatas) são comparadas. O nome vem da mineração de ouro, onde uma pepita isolada, capturada ou perdida por uma amostra e não pela vizinha imediata, ilustra fisicamente essa descontinuidade de curtíssimo alcance.
- **Patamar (sill, $C_0+C_1$)** — o valor no qual o variograma se estabiliza, formando um platô, para distâncias grandes o suficiente. Sob estacionariedade de segunda ordem, o patamar é igual à variância a priori do conjunto de dados ($\sigma^2$, a mesma variância calculada na Aula 01/02): a partir da distância na qual o variograma atinge o patamar, os valores comparados já não guardam relação espacial alguma entre si — comparar dois pontos muito distantes é estatisticamente equivalente a comparar dois pontos aleatórios quaisquer do conjunto, e a variância dessa comparação converge para a variância total dos dados.
- **Alcance (range, $a$)** — a distância na qual o variograma atinge (ou da qual se aproxima assintoticamente) o patamar. É a medida direta de **continuidade espacial**: além do alcance, duas amostras não carregam informação uma sobre a outra (pela definição do próprio patamar); dentro do alcance, quanto mais perto duas amostras estão uma da outra, mais parecidas elas tendem a ser. O alcance é o parâmetro que, na Aula 05, define até que distância uma amostra pode legitimamente contribuir para a estimativa de um ponto não amostrado.

A razão entre o efeito pepita e o patamar total, $C_0/(C_0+C_1)$, expressa em porcentagem, é usada informalmente como um índice da qualidade da continuidade espacial de um depósito: quanto menor essa razão, mais a variabilidade observada é explicada por estrutura espacial (e menos por ruído/erro), e mais confiável é a interpolação por krigagem.

### Modelos teóricos: por que o variograma experimental precisa ser substituído por uma curva

O variograma experimental, calculado ponto a ponto para cada lag, não pode ser usado diretamente dentro do sistema de equações de krigagem (Aula 05) — porque esse sistema exige o valor de $\gamma(h)$ para **qualquer** distância $h$ entre pares de pontos e blocos envolvidos na estimativa, não apenas para os lags discretos calculados experimentalmente, e exige que a função seja **matematicamente permissível** (tecnicamente, que a matriz de covariâncias associada seja definida não negativa), condição que o variograma experimental bruto, ponto a ponto, não garante. A solução é ajustar aos pontos experimentais um **modelo teórico** contínuo, escolhido de uma família restrita de funções que satisfazem essa condição de permissibilidade. Os três modelos mais usados em geoestatística de recursos minerais são:

- **Modelo esférico** — cresce quase linearmente perto da origem e atinge o patamar exatamente no alcance $a$, com uma leve curvatura de aproximação. É o modelo mais comumente usado em depósitos minerais porque seu comportamento próximo à origem (aproximadamente linear) é consistente com fenômenos naturais de continuidade moderada, e por ter um alcance finito bem definido (útil diretamente como raio de busca na krigagem).
- **Modelo exponencial** — também tem comportamento **linear** na origem, mas com inclinação inicial mais acentuada do que a do esférico (para um mesmo alcance, o dobro), e se aproxima do patamar de forma assintótica, sem nunca atingi-lo exatamente (na prática, define-se um **alcance prático** como a distância na qual o modelo atinge 95% do patamar). É apropriado para fenômenos com continuidade de curto alcance e maior variabilidade de pequena escala.
- **Modelo gaussiano** — tem comportamento **parabólico** (tangente horizontal) muito próximo à origem, refletindo um fenômeno extremamente contínuo e suave em pequena escala — os pontos mais próximos são quase idênticos. Também atinge o patamar assintoticamente, com o mesmo critério de alcance prático a 95%. É usado com cautela em recursos minerais, porque esse comportamento suave demais perto da origem pode gerar sistemas de krigagem numericamente instáveis (sobretudo com efeito pepita nulo); costuma ser mais apropriado para fenômenos de origem física suave (por exemplo, superfícies topográficas ou variáveis climáticas) do que para teores de metais, que raramente são tão suaves em pequena escala.

O comportamento do modelo **muito próximo à origem** é o critério que separa duas famílias, e é preciso ser exato sobre o que ele decide e o que não decide. Ele separa o **gaussiano** — único dos três com comportamento parabólico, tangente horizontal em $h=0$ — dos outros dois, que são ambos **lineares na origem**. Ou seja: o comportamento na origem **não** distingue esférico de exponencial, e apresentá-lo assim é um equívoco comum. Entre esses dois, o que decide é (i) a **inclinação inicial relativa**, mais acentuada no exponencial, e sobretudo (ii) a **forma da aproximação ao patamar**: o esférico chega a ele numa distância finita, com uma quebra nítida de inclinação, enquanto o exponencial se aproxima assintoticamente, achatando-se de forma gradual e continuando a subir levemente muito além do alcance prático. Um variograma experimental que sobe e depois "trava" num platô bem definido favorece o esférico; um que sobe rápido nos primeiros lags e depois se arrasta lentamente em direção ao patamar favorece o exponencial.

Vale consolidar os três modelos numa tabela, porque é por estas três colunas que a escolha se faz na prática — e é esta tabela que você deve conseguir reconstruir de memória:

| Modelo | Comportamento na origem | Como chega ao patamar | Quando usar / cautela |
|---|---|---|---|
| **Esférico** | linear | atinge o patamar **numa distância finita** ($h=a$), com quebra nítida de inclinação | o mais comum em teores de metais; alcance finito serve direto como referência de raio de busca |
| **Exponencial** | linear, mas com inclinação inicial mais acentuada (o dobro, para o mesmo alcance) | **assintótico** — nunca atinge; usa-se o alcance prático a 95% do patamar | continuidade de curto alcance, maior variabilidade de pequena escala |
| **Gaussiano** | **parabólico** (tangente horizontal) — o único dos três | assintótico, alcance prático a 95% | fenômenos muito suaves (topografia, variáveis climáticas); **cautela** em teores: pode gerar krigagem numericamente instável, sobretudo com pepita nulo |

Lendo a tabela pelas colunas: a **primeira** separa o gaussiano dos outros dois; a **segunda** separa o esférico dos outros dois. Não existe coluna que separe esférico de exponencial pela origem — é o erro que a seção acima desfez.

O ajuste — escolha do modelo e dos valores de $C_0$, $C_1$ e $a$ — é feito visualmente ou por mínimos quadrados ponderados, sempre calibrado pelo julgamento do geólogo/geoestatístico sobre o que é geologicamente plausível para aquele tipo de depósito, não apenas pelo ajuste puramente estatístico aos pontos experimentais.

### Anisotropia no variograma: variogramas direcionais

A Aula 03 definiu anisotropia geométrica e zonal em termos conceituais; a variografia é onde essas definições viram procedimento. Em vez de calcular um único variograma "omnidirecional" (usando todos os pares, em qualquer direção), calcula-se um **variograma direcional** para cada uma de várias direções de referência (tipicamente a cada 22,5° ou 30°, cobrindo 180°, já que a direção $h$ e $-h$ são equivalentes por definição), cada um com sua própria tolerância angular. Se os variogramas direcionais tiverem alcances diferentes mas o mesmo patamar, a anisotropia é **geométrica**, e a prática padrão é ajustar uma **elipse (2D) ou elipsoide (3D) de anisotropia**, cujos três eixos correspondem às três direções principais de continuidade (direção de maior alcance, direção de menor alcance no plano perpendicular, e a terceira ortogonal a ambas) — essa elipse é então usada para transformar as distâncias de forma que um único modelo de variograma, aplicado às distâncias "esticadas" pela elipse, sirva para todas as direções simultaneamente. Se, em vez disso, os patamares direcionais forem diferentes entre si, a anisotropia é **zonal**, situação que normalmente exige a soma de duas ou mais estruturas de variograma com orientações e patamares distintos (um modelo aninhado), refletindo a coexistência de fontes de variabilidade em escalas geológicas diferentes — por exemplo, variabilidade de curto alcance dentro de um estrato e variabilidade adicional entre estratos, na direção perpendicular ao acamamento.

## Exemplo trabalhado

**Situação:** um geoestatístico calcula o variograma experimental omnidirecional de um conjunto de compositas de cobre (Cu, %) ao longo de um corpo mineralizado, usando lags de 20 m, e obtém os seguintes pares (distância; $\hat{\gamma}(h)$; número de pares $N(h)$):

| Lag (m) | $\hat{\gamma}(h)$ | $N(h)$ |
|---|---|---|
| 20 | 0,18 | 145 |
| 40 | 0,32 | 210 |
| 60 | 0,44 | 198 |
| 80 | 0,52 | 175 |
| 100 | 0,58 | 140 |
| 120 | 0,60 | 98 |
| 140 | 0,59 | 52 |
| 160 | 0,61 | 21 |

A variância a priori do conjunto de dados (calculada como na Aula 01) é $\sigma^2 = 0,60$ (%)².

**Pergunta:** identifique o efeito pepita aproximado, o patamar e o alcance a partir desses pontos experimentais; avalie se o patamar é consistente com a variância a priori; e diga qual modelo teórico (esférico ou exponencial) é mais apropriado, com base na forma como a curva se aproxima do patamar e na inclinação dos primeiros lags.

**Resolução:**

**Efeito pepita:** extrapolando a curva de volta para $h=0$ a partir dos dois primeiros pontos (20 m: 0,18; 40 m: 0,32) — o crescimento entre eles é de 0,14 em 20 m — o intercepto aproximado em $h=0$ fica em torno de 0,04 a 0,06 (%)², um efeito pepita moderado, não desprezível, mas pequeno frente ao patamar.

**Patamar:** os valores se estabilizam a partir de aproximadamente 120 m ($\hat{\gamma}\approx0,60$), com pequenas flutuações depois disso (140 m: 0,59; 160 m: 0,61) atribuíveis ao número decrescente de pares disponíveis ($N(h)$ caindo de 98 para 21) — quanto menos pares, mais ruidosa e menos confiável é a estimativa naquele lag, e por isso os lags mais distantes recebem menos peso na hora de ajustar o modelo. O patamar estimado, cerca de 0,60 (%)², **é consistente com a variância a priori** de 0,60 (%)² — exatamente o comportamento esperado sob estacionariedade de segunda ordem, e um bom sinal de que a hipótese de estacionariedade adotada é razoável para este conjunto de dados.

**Alcance:** a distância na qual a curva atinge o patamar é de aproximadamente 120 m.

**Escolha do modelo:** primeiro, o descarte do gaussiano — a curva sobe de forma aproximadamente **linear** desde os primeiros lags (0,18 aos 20 m, 0,32 aos 40 m: praticamente o dobro), sem a tangente horizontal e a curvatura para cima que caracterizariam um comportamento parabólico na origem. Restam esférico e exponencial, e aqui o critério decisivo é a **aproximação ao patamar**: os valores sobem de forma quase regular até ~120 m e então **travam** (0,60; 0,59; 0,61), uma quebra nítida de inclinação numa distância finita — assinatura do esférico. Um exponencial com o mesmo alcance prático de 120 m subiria bem mais depressa nos primeiros lags (previria $\gamma(20)\approx0,27$ contra os 0,18 observados) e continuaria subindo suavemente além dos 120 m, em vez de achatar. O **modelo esférico** é, portanto, a escolha mais apropriada: $C_0\approx0,05$; $C_1\approx0,55$; $a\approx120$ m. Conferindo o ajuste, esse modelo prevê $\gamma(20)=0,19$; $\gamma(40)=0,32$; $\gamma(60)=0,43$; $\gamma(80)=0,52$; $\gamma(100)=0,58$ — praticamente os valores observados.

## Recap relâmpago

- O **variograma experimental** $\hat{\gamma}(h) = \frac{1}{2N(h)}\sum[z(x_i+h)-z(x_i)]^2$ estima a continuidade espacial a partir de pares de dados agrupados por classes de distância (**lags**) e, quando direcional, por **tolerância angular**; tolerâncias mal escolhidas produzem um variograma ruidoso (estreitas demais) ou borrado (largas demais).
- Os três elementos estruturais: **efeito pepita** ($C_0$, variabilidade de escala muito pequena + erro de amostragem/análise, não separáveis sem dado adicional); **patamar** ($C_0+C_1$, igual à variância a priori sob estacionariedade de segunda ordem); **alcance** ($a$, a distância além da qual duas amostras não carregam informação espacial uma sobre a outra).
- Modelos teóricos permissíveis substituem o variograma experimental bruto para uso na krigagem: **esférico** (linear na origem, atinge o patamar numa distância finita com quebra nítida; o mais comum em teores), **exponencial** (também linear na origem, mas com inclinação inicial mais acentuada, e aproximação assintótica ao patamar), **gaussiano** (o único parabólico na origem, usado com cautela por gerar instabilidade numérica). O comportamento na origem separa o gaussiano dos outros dois — **não** separa esférico de exponencial; entre esses, o critério é a forma da aproximação ao patamar.
- **Anisotropia geométrica** (mesmo patamar, alcance variável por direção) modela-se por uma elipse/elipsoide de anisotropia; **anisotropia zonal** (patamar também variável por direção) exige modelos aninhados de duas ou mais estruturas.

## Próxima aula

[[20-geoestatistica-aula-05-krigagem-simples-ordinaria|Aula 05 — Krigagem simples e ordinária]] — como o modelo de variograma ajustado nesta aula entra num sistema de equações lineares que pondera as amostras vizinhas para estimar valores em pontos e blocos não amostrados, e como validar essa estimativa.

## Anterior

[[20-geoestatistica-aula-03-suporte-relacao-de-krige-anisotropia|Aula 03 — Suporte, relação de Krige e anisotropia]].

## Fontes

- Isaaks, E. H. & Srivastava, R. M. (1989), *An Introduction to Applied Geostatistics*, Oxford University Press, capítulo 7 (continuidade espacial do conjunto amostral: cálculo do variograma experimental, lags e tolerâncias, variogramas direcionais) e capítulo 16 (modelagem do variograma amostral: modelos permissíveis, comportamento na origem, estruturas aninhadas e anisotropia).
- Journel, A. G. & Huijbregts, C. J. (1978), *Mining Geostatistics*, Academic Press, capítulo III (formalização matemática do variograma e condições de permissibilidade dos modelos teóricos).
- Clark, I. (1979), *Practical Geostatistics*, Applied Science Publishers, capítulo 2 (procedimento prático de cálculo de variograma experimental, escolha de lags e tolerâncias).

<!--
nivel: avancado
palavras_corpo: 2560
mapa_objetivo_secao:
  geologia-avancado-m20-oa03: "Do conceito ao gráfico: o variograma experimental" + "Os três elementos estruturais do variograma" + "Modelos teóricos: por que o variograma experimental precisa ser substituído por uma curva" + "Anisotropia no variograma: variogramas direcionais" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOEST-M20-A03-VARIOGRAMAEXPERIMENTAL-001
    claim: "O variograma experimental é calculado como gamma-chapéu(h) = (1/2N(h)) * soma dos quadrados das diferenças [z(xi+h)-z(xi)] entre todos os pares de pontos separados aproximadamente pelo vetor h, agrupados em classes de distância (lags) e, para variogramas direcionais, dentro de uma tolerância angular em torno de um azimute de referência; tolerâncias muito estreitas reduzem o número de pares por lag (aumentando o ruído), tolerâncias muito largas misturam distâncias/direções distintas (borrando a estrutura)."
    risk: fato
    source: "Isaaks & Srivastava (1989), An Introduction to Applied Geostatistics, Oxford University Press, capítulo 7 (definição e procedimento de cálculo do variograma experimental, lags, tolerâncias de distância e angular); Clark (1979), Practical Geostatistics, capítulo 2 (prática de escolha de lags e tolerâncias)."
  - claim_id: GEOEST-M20-A03-ELEMENTOSESTRUTURAIS-002
    claim: "O variograma tem três elementos estruturais: efeito pepita (C0, o valor não nulo ao qual a curva experimental é extrapolada em h=0, combinando variabilidade genuína de escala muito pequena e erro de amostragem/análise, não separáveis sem informação adicional como duplicatas); patamar (C0+C1, o valor de estabilização do variograma, igual à variância a priori dos dados sob estacionariedade de segunda ordem); e alcance (a, a distância na qual o variograma atinge o patamar, além da qual duas amostras não carregam informação espacial mútua)."
    risk: fato
    source: "Journel & Huijbregts (1978), Mining Geostatistics, Academic Press, capítulo III; Isaaks & Srivastava (1989), capítulos 7 e 16. Terminologia padrão consolidada na literatura de geoestatística (nugget effect, sill, range)."
  - claim_id: GEOEST-M20-A03-MODELOSTEORICOS-003
    claim: "Os modelos teóricos de variograma mais usados em geoestatística de recursos minerais são o esférico (comportamento LINEAR próximo à origem, atinge o patamar exatamente no alcance finito a, com quebra nítida de inclinação), o exponencial (TAMBÉM linear na origem, mas com inclinação inicial mais acentuada — o dobro da do esférico para um mesmo alcance —, com aproximação assintótica ao patamar sem nunca atingi-lo exatamente, usando-se um 'alcance prático' onde atinge ~95% do patamar) e o gaussiano (o ÚNICO dos três com comportamento parabólico/tangente horizontal muito próximo à origem, associado a fenômenos extremamente contínuos em pequena escala, também assintótico ao patamar com alcance prático a 95%, usado com cautela por poder gerar instabilidade numérica no sistema de krigagem, sobretudo com efeito pepita nulo). O comportamento muito próximo à origem separa o gaussiano dos outros dois, mas NÃO distingue esférico de exponencial — entre esses, o critério é a forma de aproximação ao patamar (finita e com quebra nítida no esférico; assintótica e gradual no exponencial) e a inclinação inicial relativa."
    risk: fato
    source: "Isaaks & Srivastava (1989), An Introduction to Applied Geostatistics, capítulo 16 (modelos teóricos permissíveis, condição de matriz de covariância definida não negativa, comportamento na origem e aproximação ao patamar como critérios de escolha); Journel & Huijbregts (1978), capítulo III; documentação técnica de software de variografia (Seequent Leapfrog/Geothermal, Maptek Vulcan, SAS PROC VARIOGRAM), que consigna explicitamente a linearidade na origem tanto do esférico quanto do exponencial e o alcance prático a 95% para exponencial e gaussiano. [claim corrigido na auditoria de 2026-09-18 — a versão anterior atribuía ao comportamento na origem a distinção esférico/exponencial]"
  - claim_id: GEOEST-M20-A03-ANISOTROPIADIRECIONAL-004
    claim: "Variogramas direcionais calculados para múltiplas direções de referência (tipicamente cobrindo 180°, dado que h e -h são equivalentes) revelam anisotropia geométrica quando os alcances diferem entre direções mas o patamar é o mesmo (modelada por uma elipse/elipsoide de anisotropia que transforma as distâncias) e anisotropia zonal quando o próprio patamar difere entre direções (tipicamente modelada pela soma de duas ou mais estruturas de variograma com orientações distintas, um modelo aninhado)."
    risk: fato
    source: "Isaaks & Srivastava (1989), An Introduction to Applied Geostatistics, capítulo 7 (procedimento de cálculo de variogramas direcionais) e capítulo 16 (ajuste de elipse/elipsoide de anisotropia geométrica; modelos aninhados para anisotropia zonal)."
  - claim_id: GEOEST-M20-A03-RAZAOEFEITOPEPITA-005
    claim: "A razão entre efeito pepita e patamar total (C0/(C0+C1)), expressa em porcentagem, é usada informalmente como índice da qualidade da continuidade espacial de um depósito: quanto menor essa razão, mais a variabilidade observada é explicada por estrutura espacial (versus ruído/erro), e mais confiável tende a ser a interpolação por krigagem."
    risk: aproximacao
    source: "Prática informal consolidada na literatura aplicada de geoestatística de recursos minerais (ver Isaaks & Srivastava 1989, caps. 7 e 16; Clark 1979, cap. 2). Apresentada como heurística de interpretação, não como critério estatístico formal com limiares universais; faixas de referência publicadas (p.ex. Cambardella et al. 1994: <25% forte, 25-75% moderada, >75% fraca dependência espacial) variam entre autores e domínios de aplicação."
  - claim_id: GEOEST-M20-A03-AJUSTEEXEMPLO-006
    claim: "No exemplo trabalhado desta aula, o modelo esférico com C0=0,05, C1=0,55 e a=120 m reproduz os pontos experimentais observados: prevê gamma(20)=0,19; gamma(40)=0,32; gamma(60)=0,43; gamma(80)=0,52; gamma(100)=0,58, contra os valores observados 0,18; 0,32; 0,44; 0,52; 0,58. Um modelo exponencial com o mesmo alcance prático de 120 m preveria gamma(20) = 0,05+0,55(1-e^-0,5) = 0,27, muito acima dos 0,18 observados — o que descarta o exponencial para este conjunto."
    risk: fato
    source: "Cálculo direto a partir das fórmulas padrão do modelo esférico, gamma(h)=C0+C1[1,5(h/a)-0,5(h/a)^3] para h<=a, e do exponencial, gamma(h)=C0+C1[1-exp(-3h/a_pratico)] (Isaaks & Srivastava 1989, cap. 16; Journel & Huijbregts 1978, cap. III). Verificado numericamente na auditoria de 2026-09-18."
-->
