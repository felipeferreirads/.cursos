# Aula 03: Aerogravimetria e gradiometria

**ID:** geologia-avancado-m16-a03
**Módulo:** [[16-aerogeofisica-modulo|Módulo 16 — Introdução à aerogeofísica]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** explicar por que medir gravidade a bordo de uma aeronave é fundamentalmente mais difícil que medi-la em terra, e como a gradiometria de gravidade contorna parte dessa dificuldade ao medir derivadas espaciais do campo em vez do campo em si.
**Ao final você vai conseguir:** explicar por que o movimento da aeronave, não a variação temporal externa, é o principal desafio da aerogravimetria; nomear e converter entre as unidades de gravimetria (mGal) e de gradiometria (Eötvös); e explicar por que a gradiometria alcança maior resolução espacial de alvos rasos e pequenos do que a gravimetria convencional.
**Pré-requisito:** [[16-aerogeofisica-aula-02-aeromagnetometria-fundamentos-correcoes-reducoes-realces|Aula 02]] — a lógica de separar sinal geológico de ruído de aquisição se mantém, mas aqui o ruído dominante muda de natureza: em vez de um campo externo variável no tempo (a diurna magnética), o desafio principal é o próprio movimento da plataforma. Pressupõe também [[15-petrofisica/15-petrofisica-aula-02-densidade-propriedades-elasticas-velocidades-sismicas|Módulo 15, Aula 02]] — densidade como a propriedade física que a gravimetria explora.

## Conteúdo

### Por que gravidade a bordo de uma aeronave é um problema difícil

A gravimetria terrestre mede diferenças de campo gravitacional da ordem de frações de miligal entre estações fixas e estacionárias — o instrumento fica parado, isolado de vibração, durante a medida. Colocar o mesmo tipo de instrumento a bordo de uma aeronave em movimento introduz um problema de ordem de grandeza completamente diferente: qualquer aceleração da própria aeronave — mudança de velocidade, guinada, turbulência, e até a aceleração centrípeta associada ao simples fato de a aeronave seguir a curvatura da Terra numa trajetória aproximadamente horizontal — se soma ao sinal gravitacional que se quer medir, e essas acelerações espúrias são tipicamente muitas ordens de grandeza maiores que a anomalia geológica de interesse. Enquanto na aeromagnetometria o desafio principal é uma variação de campo externo relativamente lenta e previsível (a diurna), na aerogravimetria o desafio principal é o **próprio movimento da plataforma**, muito mais rápido e muito mais difícil de modelar.

Dois elementos tornam a medida viável. Primeiro, o gravímetro é montado sobre uma **plataforma estabilizada** (giroscopicamente estabilizada ou, em sistemas mais recentes, com estabilização assistida por sistema inercial), que mantém o eixo sensível do instrumento o mais próximo possível da vertical local independentemente da atitude da aeronave, reduzindo a contaminação por acelerações horizontais. Segundo, e decisivo, as acelerações verticais residuais da própria aeronave — o componente que mais diretamente contamina a medida de gravidade — são calculadas independentemente a partir do **posicionamento GNSS de alta precisão** (a posição da aeronave, registrada muitas vezes por segundo, permite calcular sua aceleração vertical por dupla derivação da trajetória) e subtraídas do sinal bruto do gravímetro. É essa combinação de plataforma estabilizada com correção GNSS da trajetória que separa a aerogravimetria moderna (viável desde que a tecnologia de posicionamento por satélite atingiu precisão suficiente) da gravimetria aérea muito mais limitada de décadas anteriores.

### A correção de Eötvös: gravidade aparente do próprio movimento

Além das acelerações verticais já discutidas, existe um efeito sistemático e bem definido chamado **efeito Eötvös**: uma aeronave voando com componente de velocidade para leste soma-se à velocidade de rotação da Terra, aumentando a aceleração centrífuga aparente naquele ponto e reduzindo a gravidade medida; voando para oeste, o efeito se inverte. Esse efeito depende da velocidade e do rumo (heading) da aeronave e é calculável com precisão a partir da trajetória registrada por GNSS — a **correção de Eötvös** subtrai (ou soma) esse valor calculado do dado bruto, de forma análoga a como a correção de latitude, em gravimetria terrestre, remove o efeito previsível da forma elipsoidal da Terra e de sua rotação sobre a gravidade medida em cada latitude. Sem essa correção, dois voos sobre o mesmo ponto em direções opostas registrariam valores de gravidade sistematicamente diferentes, mesmo sem nenhuma diferença geológica real.

Depois de aplicadas as correções de movimento (plataforma estabilizada, aceleração vertical por GNSS, Eötvös), a aerogravimetria segue a mesma lógica de reduções da gravimetria terrestre — correção de ar-livre (compensando a altura da medida acima do datum de referência) e, quando aplicável, correção Bouguer (compensando a massa de rocha entre o terreno e o datum) — para produzir a anomalia gravimétrica de interesse geológico. Com uma diferença que não existe em terra: entre o sensor e o terreno há **ar**, não rocha, de modo que a redução Bouguer aerotransportada precisa separar a lâmina de ar sobrevoada da massa rochosa efetivamente presente, e o modelo digital de terreno passa a ser insumo obrigatório do processamento, não um refinamento opcional.

### Gradiometria: medir a variação do campo, não o campo

A **gradiometria de gravidade** (gravity gradiometry) não mede a gravidade diretamente: mede a **taxa de variação espacial** da gravidade — o gradiente do campo gravitacional, um tensor de segunda ordem cujas componentes descrevem como cada componente da gravidade varia em cada direção do espaço. Na prática de exploração, a componente mais frequentemente destacada é o gradiente vertical da gravidade vertical, mas sistemas de tensor completo (Full Tensor Gradiometry, FTG) medem várias componentes do tensor simultaneamente, o que permite reconstruir a direção mais provável da fonte causadora de uma anomalia — uma informação que a gravimetria escalar simples não fornece diretamente.

A vantagem central da gradiometria sobre a gravimetria convencional em plataforma aérea é que ela é, por construção, muito menos sensível ao movimento de baixa frequência da aeronave: como o instrumento mede uma **diferença** entre acelerômetros próximos entre si (ou a variação espacial numa distância curta), acelerações que afetam igualmente todo o instrumento — como boa parte do ruído de manobra da aeronave — se cancelam na subtração, sobrando principalmente o sinal de variação espacial real do campo. Isso torna a gradiometria capaz de resolver alvos rasos e pequenos com uma nitidez que a gravimetria escalar aérea, dominada por ruído de baixa frequência do movimento, dificilmente alcança — ao custo de um instrumento mecanicamente mais complexo (tipicamente baseado em acelerômetros rotativos, como no sistema Falcon, desenvolvido originalmente pela BHP, ou no Air-FTG, de tecnologia originalmente militar adaptada à exploração civil) e de exigir voo mais baixo e linhas mais próximas, porque o próprio gradiente cai com a distância à fonte mais rapidamente do que a gravidade em si — um corpo geológico que ainda produziria um sinal gravimétrico mensurável a certa altura pode já estar abaixo do limiar de detecção do gradiômetro na mesma altura, o que reforça a lógica de altura de voo baixa vista na Aula 01 e explica por que a gradiometria costuma ser reservada a levantamentos de detalhe, não de reconhecimento regional.

### Unidades: miligal e Eötvös

A gravimetria usa como unidade prática o **miligal** (mGal), definido como 10⁻⁵ m/s² (um milésimo de centésimo da aceleração da gravidade padrão, que é de cerca de 980.000 mGal ao nível do mar) — anomalias gravimétricas de interesse geológico tipicamente variam de frações de miligal a algumas dezenas de miligal, dependendo do contraste de densidade e do tamanho e profundidade do corpo.

A gradiometria usa o **Eötvös** (Eo ou E), definido como 10⁻⁹ por segundo ao quadrado (s⁻²) — uma unidade de gradiente de aceleração, portanto de dimensão diferente da do próprio mGal. A relação prática entre as duas é: **1 Eötvös equivale a 0,1 mGal por quilômetro** de distância horizontal — ou seja, um gradiente de 1 Eo significa que a gravidade muda 0,1 mGal a cada quilômetro percorrido na direção daquele gradiente. Sistemas comerciais de gradiometria aérea operam hoje com precisão da ordem de poucos a algumas dezenas de Eötvös: o sistema Falcon, por exemplo, tem erro documentado da ordem de ±5,6 Eötvös (numa filtragem de comprimento de onda de 300 m) para o gradiente vertical, e o Air-FTG opera com precisão operacional da ordem de 10 Eötvös (em médias de dez segundos) — valores que dão a régua de quão pequeno precisa ser o contraste de densidade e quão raso o corpo para ser detectável por gradiometria em condições reais de campo.

## Exemplo trabalhado

**Situação:** um levantamento de gradiometria de gravidade aérea (sistema tipo Falcon) sobre uma área com suspeita de corpo denso raso (possível intrusão máfica sob cobertura sedimentar) registra, ao longo de um trecho de 400 m de uma mesma linha de voo, um **gradiente horizontal de gravidade na direção da linha** (a componente ∂g_z/∂x do tensor) aproximadamente constante e igual a 18 Eötvös.

**Pergunta:** (a) converta esse gradiente para a variação de gravidade equivalente, em miligal, ao longo dessa distância; (b) avalie se esse sinal está acima do limiar de ruído documentado do sistema Falcon (±5,6 Eötvös).

**Resolução:**

**Passo 1 — converter Eötvös em mGal/km.** Usando a equivalência 1 Eo = 0,1 mGal/km:

18 Eo × 0,1 mGal/km por Eo = **1,8 mGal/km**

**Passo 2 — aplicar à distância real percorrida.** Como o gradiente declarado é o da direção em que se caminha (ao longo da linha), a variação de gravidade acumulada é o gradiente vezes a distância percorrida nessa mesma direção — 400 m = 0,4 km:

Δg = 1,8 mGal/km × 0,4 km = **0,72 mGal**

Repare no cuidado que o Passo 2 exige e que é fonte frequente de erro: **só se pode multiplicar um gradiente por uma distância se ambos apontarem na mesma direção**. Um gradiente *vertical* (G_DD = ∂g_z/∂z, a componente que os gradiômetros comerciais mais divulgam) não descreve como a gravidade varia ao longo de uma linha de voo horizontal — descreve como ela variaria se a aeronave subisse ou descesse. Trocar uma componente do tensor por outra na hora de converter em mGal é um erro dimensionalmente invisível, porque a conta "fecha" de qualquer jeito, e por isso mesmo passa despercebido.

**Passo 3 — avaliar o sinal contra o ruído do sistema.** O gradiente medido (18 Eo) é mais de três vezes maior que o erro documentado do sistema Falcon nessas condições (±5,6 Eo) — ou seja, o sinal está claramente acima do nível de ruído instrumental esperado, o que dá confiança de que a anomalia reflete um contraste de densidade real no subsolo, e não apenas ruído de medida. (O número ±5,6 Eo é especificado para a componente G_DD; aqui ele é usado como régua de ordem de grandeza do desempenho do sistema, que é como se faz em avaliação preliminar de alvo — a comparação rigorosa exigiria o nível de ruído da componente efetivamente usada, com o mesmo filtro de comprimento de onda.)

**Interpretação:** uma variação de gravidade de 0,72 mGal ao longo de 400 m é um sinal modesto para gravimetria convencional isolada — em muitos levantamentos gravimétricos terrestres ou aéreos escalares, esse valor estaria próximo do limite de resolução prática, especialmente sob ruído residual de movimento da aeronave. É exatamente esse tipo de alvo — raso, pequeno, de contraste moderado — que a gradiometria é desenhada para resolver melhor do que a gravimetria escalar: ao medir a variação espacial diretamente, e por essa variação cancelar boa parte do ruído de baixa frequência do movimento da aeronave, o gradiômetro entrega um sinal utilizável onde um gravímetro escalar aéreo convencional, na mesma altura de voo, provavelmente não conseguiria separar o sinal geológico do ruído residual de manobra.

## Erros comuns

- **Multiplicar um gradiente vertical por uma distância horizontal percorrida.** O próprio exemplo trabalhado nomeia isso como erro dimensionalmente invisível: só se pode converter gradiente em variação de gravidade se ambos apontarem na mesma direção — trocar a componente do tensor "fecha a conta" sem avisar que está errada.
- **Comparar dois voos em direções opostas sem aplicar a correção de Eötvös.** Sem ela, os dois registrariam gravidade sistematicamente diferente no mesmo ponto por razão puramente cinemática (rumo leste soma-se à rotação da Terra, oeste subtrai) — um efeito que pode ser confundido com variação geológica real.
- **Aplicar a redução Bouguer aerotransportada como se fosse a terrestre, sem separar a lâmina de ar sobrevoada.** Entre o sensor e o terreno há ar, não rocha — o modelo digital de terreno é insumo obrigatório do processamento aerogravimétrico, não refinamento opcional.
- **Interpretar uma anomalia de gradiente sem checar o nível de ruído documentado do sistema.** Como o exemplo trabalhado demonstra, um sinal de 18 Eo só é confiável depois de confirmado acima do erro instrumental (±5,6 Eo do Falcon) — sem essa checagem, ruído e sinal geológico ficam indistinguíveis.

## O que não concluir

- **Que gradiometria é sempre superior à gravimetria escalar.** Ela resolve melhor alvos rasos e pequenos justamente por cancelar ruído de movimento, mas exige voo mais baixo e linhas mais próximas — inadequada para reconhecimento regional, onde a gravimetria convencional continua sendo a ferramenta certa.
- **Que a plataforma estabilizada, sozinha, resolve o problema do movimento da aeronave.** Ela reduz a contaminação por acelerações horizontais; a aceleração vertical residual ainda precisa ser calculada e removida via GNSS de alta precisão — são duas soluções complementares, não uma substituindo a outra.
- **Que 1 Eötvös e 1 mGal são grandezas comparáveis diretamente.** São dimensionalmente diferentes (aceleração vs. gradiente de aceleração); a equivalência 1 Eo = 0,1 mGal/km só vale quando aplicada corretamente a uma distância na mesma direção do gradiente.

## Recap relâmpago

- Na aerogravimetria, o desafio dominante não é um campo externo variável no tempo (como a diurna magnética) — é o próprio movimento da aeronave, cujas acelerações são tipicamente muito maiores que a anomalia geológica de interesse.
- Duas soluções tornam a medida viável: uma plataforma estabilizada mantém o eixo sensível do gravímetro próximo da vertical local, e o posicionamento GNSS de alta precisão permite calcular e remover a aceleração vertical residual da trajetória da aeronave.
- A correção de Eötvös remove o efeito sistemático da velocidade e do rumo da aeronave sobre a gravidade aparente (voar para leste soma-se à rotação da Terra e reduz a gravidade medida; para oeste, o efeito se inverte) — sem ela, voos em direções opostas sobre o mesmo ponto dariam valores diferentes por razão puramente cinemática, não geológica.
- A gradiometria mede a variação espacial (o gradiente) da gravidade, não a gravidade em si; por cancelar boa parte do ruído de baixa frequência do movimento da aeronave na própria subtração entre sensores próximos, alcança melhor resolução de alvos rasos e pequenos do que a gravimetria escalar aérea — ao custo de exigir voo mais baixo e linhas mais próximas, já que o gradiente cai com a distância à fonte mais rapidamente que a própria gravidade.
- Gravimetria usa o miligal (mGal = 10⁻⁵ m/s²); gradiometria usa o Eötvös (Eo = 10⁻⁹ s⁻²), com a equivalência prática de 1 Eo = 0,1 mGal/km. Sistemas comerciais (Falcon, Air-FTG) operam hoje com precisão da ordem de poucos a poucas dezenas de Eötvös.
- Uma anomalia de gradiente precisa ser avaliada contra o nível de ruído documentado do sistema (ex.: ±5,6 Eo para o Falcon em certas condições de filtragem) antes de ser interpretada como sinal geológico real.

## Próxima aula

[[16-aerogeofisica-aula-04-aerogamaespectrometria-canais-k-eu-eth-mapas-ternarios|Aula 04 — Aerogamaespectrometria: canais K, eU e eTh, processamento e mapas ternários]] — muda de novo o campo físico medido, de gravidade para radioatividade natural, e muda também a profundidade de investigação: em vez de estruturas em profundidade, o sinal vem apenas dos primeiros centímetros do terreno.

## Fontes

- Telford, W. M., Geldart, L. P. & Sheriff, R. E. (1990), *Applied Geophysics*, 2ª ed., Cambridge University Press, cap. 2 (correção de Eötvös, correções de ar-livre e Bouguer, unidades de gravimetria).
- Dransfield, M. & Lee, J. B. (2004) e literatura técnica associada ao sistema FALCON (BHP Billiton / Fugro), "The FALCON Airborne Gravity Gradiometer Survey Systems" (precisão documentada do gradiente vertical, ordem de ±5,6 Eötvös a 300 m de comprimento de onda).
- Geological Survey of Western Australia / Kauring AGG Test Site, comparações de precisão de sistemas de gradiometria aérea (Falcon e Air-FTG).
- Bell Geospace, documentação técnica do sistema Air-FTG (precisão operacional da ordem de 10 Eötvös em médias de dez segundos).
- Nabighian, M. N. et al. (2005), "Historical development of the gravity method in exploration", *Geophysics*, 70(6) (fundamentos e evolução da gravimetria e gradiometria aéreas).

<!--
nivel: avancado
palavras_corpo: 2016
mapa_objetivo_secao:
  geologia-avancado-m16-oa02: "Por que gravidade a bordo de uma aeronave é um problema difícil" + "A correção de Eötvös: gravidade aparente do próprio movimento" + "Gradiometria: medir a variação do campo, não o campo" + "Unidades: miligal e Eötvös" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: AEROGEOFIS-M16-A03-DESAFIO-001
    claim: "O principal desafio da aerogravimetria é o movimento da própria aeronave (acelerações de manobra e turbulência), tipicamente ordens de grandeza maiores que a anomalia geológica de interesse, ao contrário da aeromagnetometria, cujo principal desafio é a variação temporal externa (diurna). A viabilidade da aerogravimetria moderna depende de plataforma giroscopicamente estabilizada combinada a posicionamento GNSS de alta precisão para calcular e remover a aceleração vertical residual da trajetória."
    risk: aproximacao
    source: "Telford, Geldart & Sheriff 1990, Applied Geophysics, cap. 2 (fundamentos de gravimetria em plataforma móvel); ga.gov.au/bigobj/GA16642.pdf, General principles of airborne gravity gradiometers (papel do GNSS e da estabilização na aerogravimetria/gradiometria modernas)."
  - claim_id: AEROGEOFIS-M16-A03-EOTVOS-002
    claim: "O efeito Eötvös é a variação sistemática da gravidade aparente medida a bordo de uma plataforma em movimento, causada pela composição da velocidade da plataforma com a rotação da Terra: voar para leste soma-se à rotação terrestre e reduz a gravidade aparente medida; voar para oeste tem efeito oposto. A correção de Eötvös remove esse efeito a partir da velocidade e do rumo da trajetória, calculados por GNSS."
    risk: fato
    source: "Telford, Geldart & Sheriff 1990, Applied Geophysics, cap. 2, seção sobre a correção de Eötvös em gravimetria em plataforma móvel (terrestre, marítima e aérea)."
  - claim_id: AEROGEOFIS-M16-A03-GRADIOMETRIA-003
    claim: "A gradiometria de gravidade mede a taxa de variação espacial (gradiente) do campo gravitacional em vez do campo em si; sistemas de tensor completo (Full Tensor Gradiometry, FTG) medem várias componentes do tensor gravitacional simultaneamente. Por medir uma diferença entre sensores próximos, a gradiometria cancela grande parte do ruído de baixa frequência do movimento da aeronave, alcançando melhor resolução de alvos rasos e pequenos do que a gravimetria escalar aérea, à custa de exigir voo mais baixo e linhas mais próximas, já que o gradiente decai com a distância à fonte mais rapidamente que a gravidade."
    risk: fato
    source: "ga.gov.au/bigobj/GA16642.pdf, General principles of airborne gravity gradiometers; xcaliburmp.com/technology/airborne-gravity-gradiometry (princípios de FTG e vantagem de resolução da gradiometria); geoexpro.com, Gradiometry: The new standard."
  - claim_id: AEROGEOFIS-M16-A03-UNIDADES-004
    claim: "O miligal (mGal) equivale a 10^-5 m/s^2 e é a unidade prática de gravimetria; o Eötvös (Eo) equivale a 10^-9 s^-2 e é a unidade de gradiente de gravidade, com a equivalência prática de 1 Eo = 0,1 mGal/km. A conversão foi reverificada por cálculo direto: 0,1 mGal/km = 10^-6 m/s^2 dividido por 10^3 m = 10^-9 s^-2. CONDIÇÃO DE USO: um gradiente só pode ser multiplicado por uma distância para dar uma variação de gravidade se ambos apontarem na MESMA direção — o gradiente vertical G_DD (a componente mais divulgada pelos sistemas comerciais) não descreve a variação de g ao longo de uma linha de voo horizontal, que é governada pela componente horizontal do tensor."
    risk: fato
    source: "Definições padrão de unidades geofísicas (Telford, Geldart & Sheriff 1990, cap. 2); ga.gov.au/bigobj/GA16642.pdf, General principles of airborne gravity gradiometers, que declara explicitamente 1 Eo = 0,1 mGal/km. CORREÇÃO LARANJA da auditoria de 2026-09-09: o exemplo trabalhado original declarava um 'gradiente vertical de gravidade de 18 Eötvös' e o multiplicava por 400 m medidos NA HORIZONTAL ao longo da linha de voo — a aritmética fechava (1,8 mGal/km x 0,4 km = 0,72 mGal), mas a componente do tensor invocada não é a que produz aquela variação."
  - claim_id: AEROGEOFIS-M16-A03-PRECISAO-005
    claim: "O sistema FALCON de gradiometria aérea tem erro documentado da ordem de ±5,6 Eötvös para o gradiente vertical GDD, numa filtragem de comprimento de onda de 300 m (com análises de repetição sugerindo erros de gravidade vertical gD da ordem de ±0,10-0,18 mGal); o sistema Air-FTG opera com precisão operacional da ordem de 10 Eötvös em médias de dez segundos."
    risk: aproximacao
    source: "Dransfield & Lee, The FALCON airborne gravity gradiometer survey systems (ResearchGate 327069609); comparação Falcon/Air-FTG no Kokong Test Block, Botswana; documentação técnica do sistema Air-FTG (ResearchGate 286352496). Valores de precisão variam por configuração de filtro e por levantamento específico, citados aqui como ordem de grandeza representativa."
-->
