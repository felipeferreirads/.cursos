# Aula 03: Métodos sísmicos marinhos — propagação de ondas, aquisição, sonar e batimetria

**ID:** geologia-avancado-m17-a03
**Módulo:** [[17-geofisica-marinha-bacias-sedimentares-modulo|Módulo 17 — Geofísica marinha e de bacias sedimentares]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** explicar os princípios físicos de propagação de ondas sísmicas na coluna d'água e no subsolo marinho, os fundamentos de aquisição sísmica marinha por reflexão, e os princípios de sonar e batimetria multifeixe usados para mapear o assoalho oceânico.
**Ao final você vai conseguir:** calcular o tempo de trânsito de uma onda sísmica na coluna d'água e reconhecer múltiplas de fundo em uma seção sísmica; descrever a geometria de aquisição sísmica marinha (fonte, streamer, offset, cobertura CDP) e por que ela difere da aquisição terrestre; e distinguir sonar de varredura lateral, ecobatímetro de feixe único e sonar multifeixe pela resolução e cobertura que cada um oferece.
**Pré-requisito:** [[15-petrofisica/15-petrofisica-modulo|Módulo 15 — Introdução à petrofísica]] (Aula 02 — densidade, propriedades elásticas e velocidades sísmicas), de onde vêm a velocidade sísmica e a **impedância acústica** (produto densidade × velocidade) usadas aqui sem redefinição; e, como antecedente do método em si, o [[11-sismoestratigrafia/11-sismoestratigrafia-modulo|Módulo 11 — Sismoestratigrafia]] (Aulas 01-02: fundamentos do método sísmico, refletores e resolução). O que esta aula acrescenta a esses dois é específico: **como** essas ondas são geradas, propagadas e registradas quando fonte e receptores estão em movimento sobre 2 km de água, e o que a coluna d'água faz com o sinal.

## Conteúdo

### A coluna d'água como uma camada sísmica a mais

Do ponto de vista da física de propagação de ondas, o oceano não é um obstáculo à sísmica — é simplesmente mais uma camada, com sua própria velocidade sísmica, que a onda atravessa antes de alcançar o fundo do mar. A velocidade do som na água do mar depende de temperatura, salinidade e pressão, mas para fins de processamento sísmico regional adota-se um valor de referência da ordem de **1.500 m/s** (nos oceanos, o valor real varia aproximadamente entre 1.450 e 1.570 m/s conforme temperatura, salinidade e pressão; a maior parte da coluna d'água oceânica fica entre 1.450 e 1.550 m/s, e os valores mais altos aparecem em água superficial quente e salina) — um valor cerca de duas a três vezes menor que a velocidade sísmica típica de rochas sedimentares consolidadas, o que faz da interface água-sedimento um dos contrastes de impedância acústica mais fortes de toda a seção sísmica marinha, gerando uma reflexão de amplitude tipicamente alta e por vezes causando fortes múltiplas (energia que ricocheteia entre a superfície do mar e o fundo oceânico mais de uma vez antes de retornar ao receptor).

Essa lâmina d'água precisa ser tratada explicitamente no processamento: o tempo de trânsito de ida e volta através da coluna d'água (o tempo até a primeira reflexão do fundo do mar) é, sozinho, uma medida direta de profundidade — a mesma equação que fundamenta a batimetria por eco, tratada mais adiante nesta aula — e qualquer erro na velocidade da água adotada se propaga como erro sistemático de profundidade em toda a seção processada.

### Fonte sísmica marinha: canhões de ar (air guns)

Ao contrário da sísmica terrestre, que frequentemente usa explosivos ou vibradores mecânicos (vibroseis) como fonte, a sísmica de reflexão marinha usa predominantemente **canhões de ar (air guns)**: câmaras que armazenam ar comprimido a alta pressão e o liberam abruptamente na água, gerando uma bolha de gás em expansão e colapso rápido que produz um pulso de pressão sísmico. Um arranjo (array) de vários canhões de ar de volumes diferentes, disparados simultaneamente, é a configuração padrão de um levantamento comercial — o desenho do arranjo busca reforçar construtivamente o pulso principal e suprimir, por interferência destrutiva, as oscilações secundárias da bolha (o efeito "bubble pulse") que, se não controladas, geram ruído repetitivo na seção processada.

Os canhões de ar são rebocados a poucos metros abaixo da superfície, atrás do navio, e disparados em intervalos regulares de distância (não de tempo) enquanto a embarcação avança — o chamado **ponto de tiro** (shot point), cuja distância entre disparos sucessivos define, junto com a geometria dos receptores, a densidade de amostragem da linha sísmica.

### Streamers: os receptores que substituem os geofones

A sísmica terrestre grava o retorno das ondas com geofones fixados no solo; a sísmica marinha usa **hidrofones**, sensores de pressão (não de velocidade de partícula, como os geofones) que respondem a variações de pressão na água causadas pela onda sísmica que retorna. Esses hidrofones são organizados ao longo de longos cabos rebocados atrás do navio — os **streamers** — cada um contendo centenas a milhares de hidrofones. Eles não são lidos um a um: os hidrofones são somados eletricamente em **grupos** regularmente espaçados ao longo do cabo, e cada grupo alimenta **um canal de registro**, produzindo **um traço sísmico**. É o centro do grupo que define a posição do "receptor" na geometria do levantamento, e é o comprimento do grupo que estabelece a menor feição lateral que aquele streamer consegue amostrar. O cabo inteiro é mantido a uma profundidade constante (tipicamente alguns metros abaixo da superfície) por dispositivos de controle de profundidade (*birds*).

Um levantamento 3D moderno reboca não um único streamer, mas um arranjo de **múltiplos streamers paralelos**, espaçados lateralmente entre si por dezenas a poucas centenas de metros e mantidos nessa geometria por defletores e por um sistema de posicionamento acústico contínuo — porque, ao contrário de um receptor terrestre fixo por um piquete, um streamer se move e deforma com correntes marinhas, ventos e a manobra do navio, exigindo posicionamento ativo em tempo real para que cada traço sísmico registrado seja corretamente atribuído a uma posição no espaço.

### Geometria de aquisição: offset, cobertura CDP e o papel do afastamento fonte-receptor

O princípio da cobertura múltipla (multiplicidade, ou fold) — registrar o mesmo ponto de reflexão em subsuperfície a partir de várias combinações de fonte e receptor com afastamentos (offsets) diferentes, e depois somar esses traços no processamento (empilhamento, ou stacking) para reforçar o sinal coerente e atenuar o ruído aleatório — é o mesmo princípio de CDP (common depth point / common midpoint) usado na sísmica terrestre, mas a geometria marinha o realiza de forma contínua e sistemática: como fonte e receptores estão ambos em movimento constante junto com o navio, cada disparo gera automaticamente uma família de afastamentos crescentes ao longo do streamer, e a sobreposição de tiros sucessivos preenche a cobertura CDP de forma naturalmente densa, sem a necessidade de posicionar geofones individualmente como em terra.

O **offset mínimo** (distância entre a fonte e o hidrofone mais próximo) e o **offset máximo** (distância ao hidrofone mais distante, definido pelo comprimento do streamer, que pode chegar a vários quilômetros) controlam, respectivamente, a capacidade de imagear estruturas muito rasas e a capacidade de resolver a velocidade sísmica em profundidade por meio da variação do tempo de trânsito com o afastamento (move-out) — um afastamento máximo maior melhora a resolução de velocidade, mas aumenta o custo e a complexidade logística do levantamento.

### Sonar: varredura lateral e mapeamento da textura do fundo

Enquanto a sísmica de reflexão busca imagear a estrutura abaixo do fundo do mar, o **sonar de varredura lateral** (side-scan sonar) tem um objetivo diferente: mapear a textura e a morfologia da própria superfície do assoalho oceânico, a partir da intensidade (não do tempo de trânsito) do retorno acústico de um pulso de alta frequência emitido lateralmente a partir de um transdutor rebocado próximo ao fundo. Superfícies rugosas, afloramentos rochosos, dunas de areia, escarpas e objetos no fundo retroespalham o som com intensidade maior que superfícies lisas e lamosas, produzindo um mosaico de imagem acústica análogo, em princípio, a uma fotografia aérea — mas de reflectividade acústica, não de luz refletida. O sonar de varredura lateral é a ferramenta de escolha para reconhecimento geológico do fundo marinho (identificação de afloramentos, feições de fundo, dutos e infraestrutura submarina), mas não fornece diretamente profundidade absoluta com a mesma precisão geométrica que a batimetria.

### Batimetria: do ecobatímetro de feixe único ao sonar multifeixe

A **batimetria** mede a profundidade da coluna d'água pelo mesmo princípio físico do tempo de trânsito de ida e volta usado no fundo da seção sísmica: um pulso acústico é emitido verticalmente, reflete no fundo do mar, e a profundidade é calculada a partir do tempo decorrido e da velocidade do som na água (profundidade = velocidade × tempo de trânsito ÷ 2). O **ecobatímetro de feixe único** (single-beam echo sounder) mede a profundidade ao longo de um único ponto diretamente abaixo do navio a cada pulso, produzindo um perfil de profundidade ao longo da rota — suficiente para navegação, mas insuficiente para mapear a morfologia tridimensional completa do fundo entre linhas de levantamento.

O **sonar multifeixe** (multibeam echo sounder) resolve essa limitação emitindo, a cada pulso, um leque de múltiplos feixes acústicos angulados (tipicamente dezenas a centenas de feixes simultâneos), cada um medindo o tempo de trânsito de forma independente — o que produz, a cada passagem do navio, uma faixa (swath) de profundidades cobrindo uma largura lateral proporcional à profundidade da água (tipicamente da ordem de várias vezes a lâmina d'água local), em vez de um único ponto. Levantamentos multifeixe modernos, com linhas de navegação espaçadas para garantir sobreposição entre faixas adjacentes, produzem modelos digitais de elevação do assoalho oceânico com cobertura total (100%) da área — a base cartográfica sobre a qual se sobrepõe toda a interpretação sísmica, gravimétrica e magnética discutida nas aulas seguintes deste módulo, e a ferramenta central para identificar feições morfológicas de fundo relevantes à geologia de bacias, como escarpas de falha, cânions submarinos, montes vulcânicos submarinos e a própria borda da plataforma continental.

### Da coluna d'água ao alvo geológico: por que a ordem importa

As três ferramentas desta aula — sísmica de reflexão, sonar e batimetria — não competem entre si: elas se complementam numa sequência lógica de levantamento. A batimetria multifeixe e o sonar de varredura lateral tipicamente vêm primeiro, estabelecendo a morfologia do fundo e identificando riscos geotécnicos e feições rasas de interesse (elemento indispensável antes de qualquer perfuração); a sísmica de reflexão, discutida em maior profundidade quanto a seus fundamentos físicos nesta aula, é o método que penetra abaixo do fundo do mar e imageia a arquitetura estratigráfica e estrutural completa da bacia — pré-rifte, rifte, sag, sal, margem divergente — descrita na Aula 02.

## Exemplo trabalhado

**Situação:** um navio sísmico registra, num levantamento na Bacia de Santos, um tempo de trânsito de ida e volta de **2,80 segundos** até a primeira reflexão forte e contínua identificada como o fundo do mar. A velocidade do som na água do mar local, medida por perfilagem de velocidade (sound velocity profile), é de **1.500 m/s**.

**Pergunta:** (a) calcule a profundidade da lâmina d'água nesse ponto; (b) sabendo que a lâmina d'água em parte da área do pré-sal de Santos ultrapassa 2.000 m, avalie se o resultado é consistente com essa região da bacia; (c) explique por que uma múltipla de fundo apareceria, na seção sísmica, em torno de 5,60 s.

**Resolução:**

**(a) Profundidade da lâmina d'água.** A relação entre tempo de trânsito de ida e volta, velocidade e profundidade é:

profundidade = velocidade × (tempo de trânsito ÷ 2)

profundidade = 1.500 m/s × (2,80 s ÷ 2) = 1.500 × 1,40 = **2.100 m**

**(b) Consistência com a região do pré-sal de Santos.** Uma profundidade de 2.100 m está dentro da faixa de lâmina d'água ultraprofunda reportada para parte da área do pré-sal da Bacia de Santos (que ultrapassa 2.000 m em diversos campos) — um resultado plausível e consistente com essa porção da bacia, e não com áreas de plataforma continental rasa, onde a lâmina d'água seria de dezenas a poucas centenas de metros.

**(c) A múltipla de fundo.** Uma múltipla de fundo do mar ocorre quando o pulso sísmico reflete no fundo do mar, retorna à superfície, reflete novamente na interface água-ar (um refletor quase perfeito, dado o forte contraste de impedância), desce de novo, e reflete uma segunda vez no fundo do mar antes de finalmente ser registrado pelo streamer — um percurso de ida e volta pela coluna d'água **duas vezes** em vez de uma. O tempo de trânsito dessa múltipla é, portanto, aproximadamente o dobro do tempo do fundo do mar primário: 2 × 2,80 s = **5,60 s** — exatamente o valor do enunciado. Isso ilustra por que a lâmina d'água profunda típica da margem brasileira exige atenção redobrada ao processamento de remoção de múltiplas: quanto mais profunda a água, mais tarde no registro (em tempo) a múltipla de fundo aparece, podendo mascarar reflexões geológicas reais de horizontes profundos, como o topo do sal ou o embasamento, quando esses coincidem em tempo de trânsito com a múltipla.

## Erros comuns

- **Confundir uma múltipla de fundo com um refletor geológico profundo real.** Como o exemplo trabalhado calcula, a múltipla aparece a aproximadamente o dobro do tempo de trânsito primário — em água ultraprofunda (pré-sal de Santos), ela pode coincidir em tempo com o topo do sal ou o embasamento, mascarando sinal geológico real se não identificada.
- **Usar sonar de varredura lateral esperando profundidade absoluta precisa.** Ele mede intensidade de retorno (textura/reflectividade), não tempo de trânsito com a mesma precisão geométrica da batimetria — são instrumentos com propósitos diferentes, não substitutos um do outro.
- **Adotar a velocidade do som na água como constante única (1.500 m/s) em qualquer cálculo de precisão.** É um valor de referência; a velocidade real varia entre ~1.450 e 1.570 m/s conforme temperatura, salinidade e pressão — qualquer erro nessa velocidade se propaga como erro sistemático de profundidade em toda a seção processada.
- **Tratar ecobatímetro de feixe único como equivalente ao multifeixe para mapear morfologia 3D do fundo.** O feixe único produz um perfil ao longo da rota, insuficiente para morfologia completa entre linhas — só o multifeixe, com seu leque de feixes por pulso, entrega cobertura total (100%) da área.

## O que não concluir

- **Que offset máximo maior é sempre melhor sem custo.** Melhora a resolução de velocidade em profundidade, mas aumenta custo e complexidade logística — a escolha do comprimento do streamer é um compromisso, não uma maximização livre.
- **Que sísmica, sonar e batimetria competem pela mesma função.** Se complementam numa sequência lógica: batimetria e sonar primeiro (morfologia do fundo, riscos rasos), sísmica de reflexão depois (arquitetura abaixo do fundo) — nenhum substitui o papel do outro.
- **Que a geometria de aquisição marinha (CDP contínuo, streamers múltiplos) dispensa posicionamento cuidadoso por ser "automática".** Um streamer se move e deforma com correntes e vento — exige posicionamento acústico ativo em tempo real, ao contrário de um geofone terrestre fixo por piquete.

## Recap relâmpago

- A coluna d'água é uma camada sísmica com velocidade de referência de ~1.500 m/s (faixa oceânica de ~1.450 a 1.570 m/s conforme temperatura, salinidade e pressão), cerca de duas a três vezes menor que a de rochas sedimentares consolidadas — o forte contraste de impedância na interface água-sedimento gera reflexões de alta amplitude e múltiplas de fundo, que precisam ser tratadas explicitamente no processamento.
- A fonte sísmica marinha padrão é o arranjo de canhões de ar (air guns), que geram um pulso de pressão pela expansão-colapso de uma bolha de ar comprimido; os receptores são hidrofones (sensores de pressão) organizados em streamers rebocados, mantidos em profundidade constante e posicionados ativamente em tempo real.
- A geometria de aquisição marinha gera cobertura CDP de forma contínua e naturalmente densa, com offset mínimo e máximo controlando, respectivamente, a resolução de estruturas rasas e a resolução de velocidade em profundidade.
- Sonar de varredura lateral mapeia a textura/reflectividade do fundo (não a profundidade absoluta com precisão geométrica); ecobatímetro de feixe único mede profundidade ao longo de um perfil sob o navio; sonar multifeixe emite um leque de feixes por pulso, cobrindo uma faixa lateral e produzindo modelos batimétricos de cobertura total — a base cartográfica de todo o restante da interpretação geofísica do módulo.
- Profundidade = velocidade × (tempo de trânsito de ida e volta ÷ 2); uma múltipla de fundo do mar aparece em tempo aproximadamente igual ao dobro do tempo de trânsito primário do fundo — mais crítica quanto mais profunda a lâmina d'água, como nas áreas ultraprofundas do pré-sal de Santos.

## Próxima aula

[[17-geofisica-marinha-bacias-sedimentares-aula-04-gravimetria-magnetometria-campos-potenciais|Aula 04 — Gravimetria e magnetometria marinhas em margens divergentes]] — como os campos potenciais (gravidade e magnetismo), medidos a partir da superfície do mar, complementam a imagem sísmica desta aula com informação sobre densidade e magnetização da bacia; a estrutura térmica profunda vem na Aula 05, em seguida.

## Anterior

[[17-geofisica-marinha-bacias-sedimentares-aula-02-margem-atlantica-brasileira-pre-rifte-rifte-sag-divergente|Aula 02 — A margem atlântica brasileira: estágios pré-rifte, rifte, sag e divergente; estilos estruturais extensionais]]

## Fontes

- Kearey, P., Brooks, M. & Hill, I. (2002), *An Introduction to Geophysical Exploration*, 3ª ed., Blackwell Science, cap. 4 (sísmica de reflexão marinha: fontes, streamers, geometria de aquisição, múltiplas).
- Sheriff, R. E. & Geldart, L. P. (1995), *Exploration Seismology*, 2ª ed., Cambridge University Press (fundamentos de aquisição sísmica marinha e processamento de múltiplas).
- National Oceanic and Atmospheric Administration (NOAA), "Multibeam Bathymetry" e "Side Scan Sonar" (nauticalcharts.noaa.gov) (princípios de sonar multifeixe e sonar de varredura lateral).
- Mayer, L. et al. (2018), "The Nippon Foundation—GEBCO Seabed 2030 Project: The Quest to See the World's Oceans Completely Mapped", *Geosciences*, 8(2), 63 (contexto de cobertura batimétrica multifeixe global).
- National Physical Laboratory (NPL), "Technical Guides — Speed of Sound in Sea-Water" (equações e valores de referência da velocidade do som na água do mar em função de temperatura, salinidade, pressão e latitude).
- Discovery of Sound in the Sea (DOSITS), "Tutorial: Speed of Sound" (faixa oceânica de ~1.450 a 1.570 m/s e as taxas de variação com temperatura, salinidade e pressão).

<!--
nivel: avancado
palavras_corpo: 2150
mapa_objetivo_secao:
  geologia-avancado-m17-oa03: "A coluna d'água como uma camada sísmica a mais" + "Fonte sísmica marinha: canhões de ar (air guns)" + "Streamers: os receptores que substituem os geofones" + "Geometria de aquisição: offset, cobertura CDP e o papel do afastamento fonte-receptor" + "Sonar: varredura lateral e mapeamento da textura do fundo" + "Batimetria: do ecobatímetro de feixe único ao sonar multifeixe" + "Da coluna d'água ao alvo geológico" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOFISMAR-M17-A03-VELOCIDADE-001
    claim: "A velocidade do som na água do mar usada como referência em processamento sísmico marinho é da ordem de 1.500 m/s; nos oceanos o valor real varia aproximadamente entre 1.450 e 1.570 m/s conforme temperatura, salinidade e pressão (a maior parte da coluna fica entre 1.450 e 1.550 m/s; os valores mais altos ocorrem em água superficial quente e salina) — valor cerca de duas a três vezes menor que a velocidade sísmica típica de rochas sedimentares consolidadas."
    risk: fato
    source: "National Physical Laboratory (NPL), Technical Guides — Speed of Sound in Sea-Water; Discovery of Sound in the Sea (DOSITS), tutorial de velocidade do som; Kearey, Brooks & Hill (2002), An Introduction to Geophysical Exploration, 3ª ed., cap. 4. CORRIGIDO na auditoria (AUD-M17-A03-VELOCIDADEFAIXA-012): o teto da faixa estava em 1.550 m/s; a faixa oceânica correntemente citada vai até ~1.570 m/s."
  - claim_id: GEOFISMAR-M17-A03-AQUISICAO-002
    claim: "A sísmica de reflexão marinha usa predominantemente arranjos de canhões de ar (air guns) como fonte, gerando pulso de pressão por expansão-colapso de bolha de ar comprimido, e hidrofones (sensores de pressão) organizados em streamers rebocados como receptores, em contraste com geofones (sensores de velocidade de partícula) fixados no solo usados na sísmica terrestre. A geometria de aquisição marinha gera cobertura CDP (common depth point) de forma contínua, com offset mínimo e máximo do streamer controlando, respectivamente, resolução de estruturas rasas e resolução de velocidade em profundidade."
    risk: fato
    source: "Sheriff & Geldart (1995), Exploration Seismology, 2ª ed.; Kearey, Brooks & Hill (2002), cap. 4."
  - claim_id: GEOFISMAR-M17-A03-SONAR-003
    claim: "Sonar de varredura lateral (side-scan sonar) mapeia a reflectividade/textura da superfície do assoalho oceânico a partir da intensidade do retorno acústico, sem fornecer diretamente profundidade absoluta com precisão geométrica; ecobatímetro de feixe único mede profundidade ao longo de um único ponto sob o navio; sonar multifeixe (multibeam) emite um leque de dezenas a centenas de feixes por pulso, cobrindo uma faixa lateral proporcional à profundidade da água e produzindo cobertura batimétrica total da área levantada."
    risk: fato
    source: "NOAA, Multibeam Bathymetry e Side Scan Sonar (nauticalcharts.noaa.gov); Mayer et al. (2018), The Nippon Foundation—GEBCO Seabed 2030 Project, Geosciences 8(2)."
  - claim_id: GEOFISMAR-M17-A03-EXEMPLO-004
    claim: "A relação profundidade = velocidade × (tempo de trânsito de ida e volta ÷ 2) é o princípio físico básico de conversão tempo-profundidade tanto em sísmica de reflexão (fundo do mar como primeiro refletor) quanto em batimetria por eco; uma múltipla de fundo do mar ocorre em tempo de trânsito aproximadamente igual ao dobro do tempo de trânsito primário do fundo, por percorrer a coluna d'água duas vezes antes de ser registrada."
    risk: fato
    source: "Sheriff & Geldart (1995), Exploration Seismology, princípios de conversão tempo-profundidade e múltiplas de curto período; valores de lâmina d'água ultraprofunda do pré-sal de Santos (superior a 2.000 m) consistentes com Moreira et al. (2007), Boletim de Geociências da Petrobras 15(2)."
-->
