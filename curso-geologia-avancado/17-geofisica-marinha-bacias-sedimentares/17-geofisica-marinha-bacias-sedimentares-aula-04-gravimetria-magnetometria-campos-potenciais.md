# Aula 04: Gravimetria e magnetometria marinhas em margens divergentes

**ID:** geologia-avancado-m17-a04
**Módulo:** [[17-geofisica-marinha-bacias-sedimentares-modulo|Módulo 17 — Geofísica marinha e de bacias sedimentares]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** interpretar mapas gravimétricos e magnéticos de bacias sedimentares e margens continentais, reconhecendo as correções específicas do ambiente marinho e as assinaturas geofísicas dos principais elementos estruturais de uma margem divergente.
**Ao final você vai conseguir:** explicar por que a correção de Bouguer marinha usa o contraste água-rocha em vez da densidade da rocha isolada; reconhecer a anomalia magnética de crosta oceânica como uma sequência de faixas lineares e relacioná-la à idade do assoalho oceânico; e usar o par ar-livre/Bouguer e o padrão de faixas magnéticas para posicionar o limite crosta continental-oceânica de uma margem divergente.
**Pré-requisito:** [[16-aerogeofisica/16-aerogeofisica-modulo|Módulo 16 — Introdução à aerogeofísica]] — esta aula assume que você já domina os fundamentos de gravimetria e magnetometria (unidades mGal e nT, correções de Bouguer e ar-livre, redução ao polo, IGRF) desenvolvidos ali para o contexto aéreo/terrestre; aqui a pergunta é como essas mesmas técnicas se adaptam à plataforma marinha em movimento e à interpretação específica de bacias sedimentares e margens divergentes.

## Conteúdo

### Gravimetria marinha: medir a bordo de uma plataforma em movimento

Os fundamentos físicos da gravimetria — a medida de pequenas variações do campo gravitacional terrestre, causadas por contrastes de densidade em subsuperfície, expressas em miligals (mGal) — são exatamente os mesmos estabelecidos no Módulo 16 para levantamentos aéreos. O que muda no ambiente marinho é o desafio de aquisição: um gravímetro instalado a bordo de um navio está sujeito à aceleração vertical do movimento do casco sobre as ondas (um ruído que pode superar em várias ordens de grandeza o próprio sinal geológico de interesse, medido em miligals), o que exige gravímetros marinhos montados sobre plataformas estabilizadas por giroscópio e sistemas de filtragem que separam a aceleração de manobra do sinal gravitacional real.

Uma correção específica do ambiente em movimento, já introduzida no Módulo 16 para a aerogravimetria, é a **correção de Eötvös**: como a Terra gira, uma plataforma que se move sobre sua superfície tem uma componente de aceleração centrífuga adicional que depende da velocidade e do rumo (azimute) do deslocamento. Como no Módulo 16: mover-se para **leste** soma-se à rotação terrestre e **reduz** a gravidade medida (a correção a somar de volta é positiva); mover-se para **oeste** tem o efeito oposto. O sinal não se inverte de um hemisfério para o outro — o que muda com a latitude é a **magnitude**, que escala com o cosseno da latitude e se anula nos polos.

O que muda entre navio e aeronave é justamente a escala do problema, e vale gravar o contraste: **a correção de Eötvös é uma a duas ordens de grandeza maior no ar do que no mar**. A fórmula padrão, com a velocidade *V* em nós, é *E* = 7,5038 · *V* · cos φ · sen α (+ 0,004154 · *V*², termo de segunda ordem em geral desprezível), em que φ é a latitude e α o azimute do deslocamento. A 45° de latitude e rumo leste, isso dá cerca de **5,3 mGal por nó** — ou seja, algumas **dezenas** de mGal num navio a 5-10 nós de velocidade de levantamento. Numa aeronave a algumas centenas de nós, o mesmo efeito ultrapassa **1 Gal (mais de 1.000 mGal)**: um fator de aproximadamente 30 vezes entre as duas plataformas. Em ambos os casos a correção depende criticamente da qualidade do posicionamento e da velocidade registrados durante o levantamento — mas na aerogravimetria um erro pequeno de velocidade vira um erro grande em mGal, o que é parte de por que a aerogravimetria escalar é mais ruidosa que a gravimetria marinha.

### A correção de Bouguer marinha: por que a água entra na conta

Em terra, a correção de Bouguer remove o efeito gravitacional atrativo da própria massa de rocha entre o ponto de medida e um datum de referência, usando a densidade média da crosta (tipicamente ~2,67 g/cm³). No mar, a lógica se inverte: o gravímetro está no navio, na superfície da água, e abaixo dele há uma coluna de água (densidade ~1,03 g/cm³) seguida do assoalho oceânico e da crosta. A **correção de Bouguer marinha** substitui, no cálculo, essa coluna d'água por uma coluna hipotética de rocha crustal — efetivamente adicionando de volta a massa "que faltaria" se ali houvesse crosta em vez de água — usando não a densidade da rocha isolada, mas o **contraste de densidade entre a água e a rocha** (aproximadamente 2,67 − 1,03 ≈ 1,64 g/cm³), porque é esse contraste, e não a densidade absoluta de nenhum dos dois meios, que determina o efeito gravitacional da substituição.

Como a correção marinha **adiciona** massa (rocha no lugar de água), ela é sempre positiva e frequentemente grande. A consequência é um par de assinaturas que convém memorizar em conjunto, porque elas são espelhadas:

| | Anomalia ar-livre | Anomalia de Bouguer |
|---|---|---|
| Oceano profundo (planície abissal compensada) | próxima de zero | fortemente **positiva** (tipicamente +220 a +330 mGal) |
| Cadeia de montanhas continental (compensada) | próxima de zero | fortemente **negativa** |

Em ambos os casos a anomalia ar-livre é pequena porque o relevo está isostaticamente compensado; é a Bouguer que revela o desvio — positiva no oceano, porque a crosta oceânica é fina e densa, e negativa sob montanhas, porque a raiz crustal é espessa e leve. Não confunda: a anomalia ar-livre em mar aberto **não** equivale à Bouguer. Sobre a mesma planície abissal, as duas diferem por **centenas de mGal** — uma fica perto de zero, a outra chega a +300 mGal.

Na prática de interpretação regional, a **anomalia ar-livre** (sem qualquer correção pela massa entre o ponto de medida e o datum) já é amplamente usada em mapas gravimétricos marinhos regionais, sobretudo porque, em mar aberto, ela tende a refletir bem a topografia do assoalho oceânico e estruturas rasas; a anomalia de Bouguer marinha, por remover esse efeito topográfico, é a ferramenta preferida para investigar contrastes de densidade mais profundos — como a espessura crustal e a posição do limite crosta continental-crosta oceânica, um dos alvos centrais da interpretação gravimétrica de margens divergentes.

### Assinatura gravimétrica dos elementos de uma margem divergente

Retomando a arquitetura tectonossedimentar da Aula 02, cada elemento estrutural de uma margem divergente tem uma assinatura gravimétrica característica: a **crosta oceânica**, mais densa e mais fina que a crosta continental, produz anomalias de Bouguer regionalmente mais positivas (mais altas) que a crosta continental adjacente, e a transição entre as duas — o limite crosta continental-oceânica (COB, continent-ocean boundary) — frequentemente se expressa como um gradiente gravimétrico regional acentuado, uma das ferramentas usadas para posicionar esse limite quando a sísmica de reflexão profunda não o resolve com clareza direta. O **sal aptiano**, por sua baixa densidade (tipicamente ~2,2 g/cm³, sensivelmente menor que os carbonatos e siliciclásticos que o encaixam, tipicamente 2,4-2,7 g/cm³), produz um efeito gravimétrico local negativo (déficit de massa) sobre corpos de sal espessos — um sinal usado, de forma complementar à sísmica, para mapear a distribuição de sal em áreas de imageamento sísmico difícil sob corpos salíferos complexos, um problema conhecido de imageamento sísmico. Depocentros sin-rifte preenchidos por sedimentos de baixa densidade sobre embasamento mais denso também geram anomalias locais negativas, ajudando a delinear a geometria de meio-grabens em mapas gravimétricos regionais.

### Magnetometria marinha e as anomalias lineares da crosta oceânica

A magnetometria marinha compartilha com a aeromagnetometria (Módulo 16) os mesmos fundamentos físicos — magnetização induzida e remanente controlada majoritariamente por minerais ferrimagnéticos como a magnetita, medida em nanotesla (nT) e reduzida ao remover o campo de referência IGRF — mas revela, no ambiente oceânico, um padrão sem equivalente direto em levantamentos terrestres: as **anomalias magnéticas lineares da crosta oceânica**, faixas paralelas e simétricas de polaridade magnética alternada (positiva e negativa) que se estendem paralelas ao eixo de uma dorsal meso-oceânica.

Essas faixas registram as **reversões do campo magnético terrestre**: à medida que nova crosta oceânica se forma continuamente na dorsal e se resfria abaixo do ponto de Curie, ela adquire uma magnetização remanente que registra a polaridade do campo terrestre no momento do resfriamento; como o campo magnético terrestre reverte de polaridade em intervalos irregulares ao longo do tempo geológico, cada nova faixa de crosta formada registra a polaridade vigente naquele momento, produzindo um padrão de faixas simétricas em relação ao eixo da dorsal — a evidência clássica que, na década de 1960, confirmou o espalhamento do assoalho oceânico e sustentou a teoria da tectônica de placas. Para a interpretação de margens divergentes como a brasileira, essas anomalias lineares são a ferramenta padrão para **datar a crosta oceânica** por correlação com a escala de tempo de polaridade geomagnética (comparando o padrão observado a um padrão de referência calibrado por idades radiométricas de outras margens), permitindo estimar independentemente a idade do início do espalhamento oceânico — um dado complementar às idades estratigráficas de breakup discutidas na Aula 02.

Como a crosta continental estirada da margem, ao contrário da crosta oceânica recém-formada na dorsal, não registra esse padrão de faixas lineares simétricas (sua magnetização reflete uma história geológica muito mais antiga e heterogênea), a transição de um padrão magnético heterogêneo e não-linear (crosta continental) para um padrão de faixas lineares e simétricas (crosta oceânica) é também, como no caso gravimétrico, um critério auxiliar para posicionar o limite crosta continental-oceânica.

## Exemplo trabalhado

**Situação:** um levantamento gravimétrico e magnético regional na margem sudeste brasileira mostra: (1) na porção mais próxima ao continente, uma anomalia magnética heterogênea, sem padrão linear reconhecível, sobre uma anomalia de Bouguer relativamente mais baixa (mais negativa); (2) numa faixa de transição estreita, um gradiente gravimétrico acentuado; (3) na porção mais oceânica, um padrão de faixas magnéticas lineares, simétricas e paralelas entre si, sobre uma anomalia de Bouguer regionalmente mais alta (mais positiva) que a porção (1).

**Pergunta:** interprete a natureza crustal de cada uma das três zonas.

**Resolução:**

**Zona 1** (magnetismo heterogêneo sem padrão linear; Bouguer mais baixa): a ausência de faixas magnéticas lineares simétricas, combinada com anomalia de Bouguer relativamente negativa (consistente com crosta mais espessa e menos densa), identifica esta zona como **crosta continental** — neste caso, a porção estirada da margem, próxima ao continente não deformado.

**Zona 2** (gradiente gravimétrico acentuado, estreita): um gradiente gravimétrico regional concentrado numa faixa estreita é a assinatura clássica de uma transição abrupta de espessura e densidade crustal — a zona de transição consistente com o **limite crosta continental-oceânica (COB)**, confirmando com o critério gravimétrico o que o critério magnético (zona 3) também vai indicar.

**Zona 3** (faixas magnéticas lineares simétricas; Bouguer mais alta): o padrão de faixas magnéticas lineares e simétricas é a assinatura diagnóstica de **crosta oceânica**, formada por espalhamento a partir de uma antiga dorsal meso-oceânica e registrando reversões sucessivas do campo magnético terrestre; a anomalia de Bouguer mais alta é consistente com crosta mais fina e mais densa que a crosta continental adjacente.

**Conclusão:** os dois critérios — magnético (faixas lineares vs. padrão heterogêneo) e gravimétrico (gradiente na transição, nível regional em cada domínio) — convergem de forma independente para a mesma interpretação de zoneamento crustal, exatamente o tipo de integração multimétodo que a interpretação de margens divergentes exige. A Aula 05 acrescenta um terceiro critério independente a esse mesmo zoneamento: o fluxo de calor, que decai com a idade da crosta oceânica e permite estimar a distância ao eixo de espalhamento original.

## Erros comuns

- **Tratar anomalia ar-livre e anomalia de Bouguer marinha como equivalentes sobre oceano profundo.** A aula é explícita: sobre a mesma planície abissal compensada, ar-livre fica perto de zero e Bouguer chega a +300 mGal — uma diferença de centenas de mGal que confundir invalida qualquer interpretação de espessura crustal.
- **Aplicar a densidade de contraste da Bouguer terrestre (rocha isolada, ~2,67) em vez do contraste água-rocha (~1,64) no cálculo marinho.** É precisamente o que muda entre os dois ambientes — usar a densidade errada produz uma correção sistematicamente errada, não apenas imprecisa.
- **Ignorar a diferença de ordem de grandeza da correção de Eötvös entre navio e aeronave.** Como a aula quantifica, o efeito é ~30 vezes maior no ar do que no mar — um erro de velocidade que seria desprezível em gravimetria marinha vira erro grande em mGal na aerogravimetria.
- **Buscar anomalias magnéticas lineares simétricas sobre crosta continental estirada.** Como o exemplo trabalhado demonstra, a ausência desse padrão é justamente o critério que identifica a Zona 1 como continental — esperar faixas lineares ali é aplicar um critério ao domínio errado.

## O que não concluir

- **Que o sinal da correção de Eötvös se inverte entre hemisférios.** O que muda com a latitude é a magnitude (escala com cos φ, anulando-se nos polos); o sinal depende do rumo (leste reduz, oeste aumenta a gravidade medida), não do hemisfério.
- **Que o critério gravimétrico e o magnético para o limite crosta continental-oceânica são redundantes.** São critérios independentes que, quando convergem (como no exemplo trabalhado), aumentam a confiança na posição do COB — mas cada um pode falhar isoladamente onde o outro ainda resolve.
- **Que a anomalia negativa de sal aptiano identifica sozinha a presença de sal sem ambiguidade.** É um sinal complementar à sísmica, útil onde o imageamento sísmico sob sal é difícil — mas depocentros sin-rifte de baixa densidade também geram anomalias locais negativas, então a interpretação isolada do sinal gravimétrico pode confundir as duas causas.

## Recap relâmpago

- Gravimetria marinha compartilha os fundamentos da gravimetria aérea (Módulo 16), mas exige plataforma estabilizada por giroscópio (ruído de movimento do navio) e correção de Eötvös pela velocidade/azimute do deslocamento — *E* = 7,5038 · *V*(nós) · cos φ · sen α, isto é ~5,3 mGal por nó a 45° de latitude, ou seja **dezenas** de mGal num navio, contra **mais de 1.000 mGal** numa aeronave a centenas de nós (uma a duas ordens de grandeza de diferença, fator ~30); o sinal depende do rumo (leste reduz a gravidade medida), não do hemisfério.
- A correção de Bouguer marinha substitui a coluna d'água por uma coluna hipotética de rocha, usando o contraste de densidade água-rocha (2,67 − 1,03 ≈ 1,64 g/cm³) em vez da densidade da rocha isolada. Consequência a não trocar: sobre oceano profundo compensado, a anomalia **ar-livre é próxima de zero** e a **Bouguer é fortemente positiva** (+220 a +330 mGal); sob montanhas continentais, ar-livre ~0 e Bouguer fortemente negativa.
- Assinatura gravimétrica de uma margem divergente: crosta oceânica mais densa/fina gera Bouguer regionalmente mais alta que a crosta continental; o limite crosta continental-oceânica (COB) frequentemente aparece como gradiente gravimétrico acentuado; sal aptiano (baixa densidade, ~2,2 g/cm³) gera anomalia local negativa.
- Anomalias magnéticas lineares e simétricas da crosta oceânica registram reversões do campo geomagnético durante o espalhamento do assoalho oceânico a partir de uma dorsal — a evidência clássica da tectônica de placas — e servem para datar a crosta oceânica e localizar o limite crosta continental-oceânica, de forma complementar ao critério gravimétrico.

## Próxima aula

[[17-geofisica-marinha-bacias-sedimentares-aula-05-fluxo-de-calor-estrutura-termica-margem|Aula 05 — Fluxo de calor e a estrutura térmica de uma margem divergente]] — como a mesma litosfera cujo zoneamento crustal esta aula acabou de mapear por gravimetria e magnetometria também registra, no fluxo de calor que emite, um terceiro critério independente de idade e de estrutura térmica.

## Anterior

[[17-geofisica-marinha-bacias-sedimentares-aula-03-metodos-sismicos-marinhos-propagacao-aquisicao-sonar-batimetria|Aula 03 — Métodos sísmicos marinhos: propagação de ondas, aquisição, sonar e batimetria]]

## Fontes

- Telford, W. M., Geldart, L. P. & Sheriff, R. E. (1990), *Applied Geophysics*, 2ª ed., Cambridge University Press, caps. 2 e 4 (gravimetria e magnetometria marinha, correções de Bouguer e Eötvös).
- Kearey, P., Brooks, M. & Hill, I. (2002), *An Introduction to Geophysical Exploration*, 3ª ed., Blackwell Science (gravimetria e magnetometria aplicadas a margens continentais).
- Vine, F. J. & Matthews, D. H. (1963), "Magnetic anomalies over oceanic ridges", *Nature*, 199, 947-949 (artigo clássico das anomalias magnéticas lineares da crosta oceânica e reversões geomagnéticas).
- Harlan, R. B. (1968), "Eotvos corrections for airborne gravimetry", *Journal of Geophysical Research*, 73(14), 4675-4679 (magnitude da correção de Eötvös em velocidades de aeronave).
- Módulo 16 deste curso — Introdução à aerogeofísica (Aulas 02 e 03: fundamentos de magnetometria e gravimetria, correções de Eötvös, redução ao polo, IGRF).

<!--
nivel: avancado
palavras_corpo: 1500
origem: 'Esta aula é a metade "campos potenciais" da antiga Aula 04 (Gravimetria, magnetometria e fluxo de calor), dividida em 2026-09-10 por decisão do orquestrador a partir do achado didático DID-M17-A04-CARGA-003 (revisão didática, não bloqueante). Conteúdo científico integralmente já auditado e corrigido (auditoria de 2026-09-10, ver 17-geofisica-marinha-bacias-sedimentares-auditoria.md) — apenas o parágrafo final do exemplo trabalhado e a conclusão foram ajustados (removida a referência à zona de fluxo de calor, que migrou para a Aula 05 com exemplo próprio) e a seção "Próxima aula" foi redirecionada. NÃO houve alteração de nenhuma frase do conteúdo técnico (Eötvös, Bouguer, assinatura gravimétrica, magnetometria) além da divisão mecânica. NÃO requer nova rodada completa de auditoria de conteúdo.'
mapa_objetivo_secao:
  geologia-avancado-m17-oa04: "Gravimetria marinha: medir a bordo de uma plataforma em movimento" + "A correção de Bouguer marinha: por que a água entra na conta" + "Assinatura gravimétrica dos elementos de uma margem divergente" + "Magnetometria marinha e as anomalias lineares da crosta oceânica" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOFISMAR-M17-A04-EOTVOS-006
    claim: "A correção de Eötvös depende da velocidade e do rumo da plataforma: movimento para leste soma-se à rotação terrestre e reduz a gravidade medida (correção positiva a somar de volta), movimento para oeste tem o efeito oposto; o SINAL não se inverte entre hemisférios, apenas a MAGNITUDE escala com o cosseno da latitude e se anula nos polos. A magnitude difere fortemente entre plataformas: pela fórmula padrão E = 7,5038 · V(nós) · cos(latitude) · sen(azimute) + 0,004154 · V², a 45° de latitude e rumo leste dá cerca de 5,3 mGal por nó, isto é, dezenas de mGal num navio a 5-10 nós, contra mais de 1 Gal (>1.000 mGal) numa aeronave a centenas de nós — um fator de aproximadamente 30 vezes, ou seja UMA A DUAS ordens de grandeza, não uma."
    risk: fato
    source: "Telford, Geldart & Sheriff (1990), Applied Geophysics, 2ª ed., cap. 2; constante 7,5038 conferida contra a implementação de referência do GMT (mgd77list) e contra a entrada 'Eötvös effect' do SEG Wiki; Harlan, R. B. (1968), Eotvos corrections for airborne gravimetry, JGR 73(14), 4675-4679; Módulo 16 deste curso, Aula 03. Herdado sem alteração da auditoria de 2026-09-10 da Aula 04 original (achados AUD-M17-A04-EOTVOSORDEM-004 e AUD-M17-A04-EOTVOSVALOR-009, ambos corrigidos)."
  - claim_id: GEOFISMAR-M17-A04-BOUGUER-001
    claim: "A correção de Bouguer marinha substitui, no cálculo, a coluna d'água abaixo do gravímetro por uma coluna hipotética de rocha crustal, usando o contraste de densidade entre água (~1,03 g/cm³) e rocha crustal (~2,67 g/cm³), isto é, um contraste da ordem de ~1,64 g/cm³, em vez da densidade da rocha isolada como na correção de Bouguer terrestre. Por adicionar massa, a correção marinha é sempre positiva: sobre oceano profundo isostaticamente compensado a anomalia AR-LIVRE é próxima de zero enquanto a anomalia de BOUGUER é fortemente POSITIVA (tipicamente +220 a +330 mGal); sob cadeias continentais compensadas o par é espelhado (ar-livre ~0, Bouguer fortemente negativa)."
    risk: fato
    source: "Telford, Geldart & Sheriff (1990), Applied Geophysics, 2ª ed., cap. 2; literatura de gravimetria de margens rifteadas para a faixa de anomalia de Bouguer sobre crosta oceânica. Herdado sem alteração da auditoria de 2026-09-10 (achado AUD-M17-A04-ARLIVREOPOSTO-010, corrigido)."
  - claim_id: GEOFISMAR-M17-A04-GRAV-MARGEM-002
    claim: "Crosta oceânica, mais densa e mais fina que a crosta continental, produz anomalias de Bouguer regionalmente mais positivas; o limite crosta continental-oceânica frequentemente se expressa como gradiente gravimétrico regional acentuado; sal (densidade tipicamente ~2,2 g/cm³, menor que carbonatos/siliciclásticos encaixantes ~2,4-2,7 g/cm³) produz anomalia gravimétrica local negativa sobre corpos de sal espessos."
    risk: aproximacao
    source: "Telford, Geldart & Sheriff (1990), caps. 2 e 4; valores de densidade de sal e rochas encaixantes consistentes com literatura padrão de petrofísica de evaporitos. Herdado sem alteração da auditoria de 2026-09-10."
  - claim_id: GEOFISMAR-M17-A04-MAGNETO-003
    claim: "Anomalias magnéticas lineares e simétricas da crosta oceânica registram reversões do campo magnético terrestre durante o espalhamento do assoalho oceânico a partir de uma dorsal meso-oceânica, constituindo evidência clássica (Vine & Matthews, 1963) que sustentou a teoria da tectônica de placas; servem para datar a crosta oceânica por correlação com a escala de tempo de polaridade geomagnética e para auxiliar a localização do limite crosta continental-oceânica."
    risk: fato
    source: "Vine, F. J. & Matthews, D. H. (1963), Magnetic anomalies over oceanic ridges, Nature 199. Herdado sem alteração da auditoria de 2026-09-10."
-->
