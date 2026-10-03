# Aula 04: Descontinuidades: geometria, resistência ao cisalhamento e permeabilidade do maciço

**ID:** geologia-avancado-m05-a04
**Módulo:** [[05-mecanica-de-rochas-modulo|Módulo 05 — Mecânica de rochas]]
**Duração estimada:** ~28 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** descrever e quantificar os parâmetros geométricos de uma descontinuidade, aplicar o critério de resistência ao cisalhamento de Barton-Bandis e explicar como as descontinuidades controlam a permeabilidade equivalente do maciço rochoso.
**Pré-requisito:** critérios de ruptura da rocha intacta e o papel do confinamento na resistência (Aula 03); condutividade hidráulica e lei de Darcy (Módulo 01, Aula 02).

## Antes de começar, você precisa saber

- Resistência ao cisalhamento como função da tensão normal (τ = f(σn)) — a mesma lógica do critério de Mohr-Coulomb (Aula 03), agora aplicada não à rocha intacta, mas ao plano de uma descontinuidade.
- Lei de Darcy e condutividade hidráulica K, do Módulo 01, Aula 02 — a permeabilidade de um meio fraturado será tratada como uma extensão desse conceito.

## Conteúdo

### Por que a descontinuidade, e não a rocha intacta, costuma governar o comportamento do maciço

Um **maciço rochoso** raramente se comporta como a rocha intacta ensaiada em laboratório (Aula 02): está cortado por **descontinuidades** — planos de fraqueza mecânica de origem estrutural (juntas, falhas, planos de acamamento, foliação, contatos litológicos) —, e é ao longo desses planos, não através da matriz rochosa, que a maior parte da deformação, do deslizamento e da percolação de água efetivamente ocorre. Um bloco de rocha intacta entre descontinuidades pode ter UCS de 150 MPa; se as descontinuidades que o delimitam têm baixa resistência ao cisalhamento e estão desfavoravelmente orientadas em relação a uma escavação, é o comportamento delas — não da rocha intacta — que determina se o maciço é estável.

> [!important] "Resistência da rocha" e "resistência do maciço" são coisas diferentes
> Um erro conceitual recorrente é reportar a UCS de um testemunho intacto como se fosse "a resistência da rocha" no sentido relevante para engenharia. A resistência relevante para projeto — de um talude, de uma escavação subterrânea, de uma fundação — é a **resistência do maciço**, que depende tanto da matriz rochosa quanto, de forma frequentemente dominante, da geometria e da resistência das descontinuidades que o atravessam. Esse é o motivo pelo qual as classificações geomecânicas da Aula 06 (RMR, Q, GSI) existem: para capturar esse efeito combinado de forma sistemática.

### Parâmetros geométricos de uma descontinuidade

A caracterização de uma descontinuidade segue um conjunto padronizado de parâmetros, consolidado pelos métodos sugeridos da ISRM (1978) e amplamente adotado em mapeamento geotécnico de campo:

- **Orientação:** direção de mergulho (*dip direction*) e mergulho (*dip*) do plano — o parâmetro isolado mais importante para análise de estabilidade (Aula 07), porque determina se a descontinuidade é cinematicamente favorável ou desfavorável a um deslizamento em relação a uma face de talude ou escavação específica.
- **Espaçamento:** distância perpendicular entre descontinuidades sucessivas de um mesmo conjunto (família) — controla diretamente o tamanho médio dos blocos de rocha intacta delimitados pelas descontinuidades: espaçamentos menores produzem blocos menores e um maciço com comportamento mecânico mais próximo de um meio granular equivalente do que de um sólido contínuo com poucas fraturas.
- **Persistência:** extensão ou continuidade areal de uma descontinuidade — uma junta pouco persistente (poucos metros) tem menor influência na resistência do maciço em escala de talude do que uma falha persistente por centenas de metros, mesmo que ambas tenham a mesma resistência ao cisalhamento local.
- **Rugosidade:** irregularidade da superfície do plano em escalas que vão do ondulamento em grande escala (metros) até a aspereza microscópica — quantificada, na prática de engenharia, pelo **JRC** (*Joint Roughness Coefficient*, Barton, 1973), um índice de 0 (plano liso) a 20 (muito rugoso), estimado por comparação visual com perfis-padrão publicados ou medido diretamente com um perfilômetro.
- **Abertura e preenchimento:** distância entre as paredes da descontinuidade e a natureza do material que eventualmente as preenche (argila, calcita, brecha, ou vazio) — ambos alteram drasticamente tanto a resistência ao cisalhamento (um preenchimento argiloso pode reduzi-la a valores próximos aos de um solo mole) quanto a condutividade hidráulica ao longo do plano.
- **Resistência da parede (JCS):** resistência à compressão da rocha imediatamente adjacente às paredes da descontinuidade (*Joint Wall Compressive Strength*), frequentemente reduzida em relação à rocha intacta sã por alteração ao longo do plano — mede-se por martelo de Schmidt ou por point load (Aula 02) diretamente na parede.
- **Número de famílias e tamanho de bloco:** o número de conjuntos de descontinuidades com orientação sistemática que atravessam o maciço (tipicamente de 1 a 4, mais um conjunto aleatório) determina, junto com o espaçamento, o tamanho e a forma dos blocos individuais — um maciço com três famílias ortogonais bem definidas e espaçamento regular produz blocos aproximadamente cúbicos, enquanto poucas famílias muito espaçadas produzem blocos tabulares grandes.

### Resistência ao cisalhamento de uma descontinuidade: o critério de Barton-Bandis

A resistência ao cisalhamento ao longo de uma descontinuidade não segue simplesmente o critério de Mohr-Coulomb da rocha intacta — a rugosidade do plano contribui com uma componente adicional de resistência, chamada **dilatância por rugosidade**: ao deslizar, as asperezas de uma superfície rugosa forçam as duas paredes a se afastarem uma da outra (a superfície precisa "subir" sobre as saliências da outra), consumindo energia extra. O modelo pioneiro de **Patton (1966)** captura isso com um critério bilinear simplificado: em baixas tensões normais, τ = σn·tan(φb + i), onde φb é o ângulo de atrito básico (da superfície lisa) e i é o ângulo de inclinação médio das asperezas; em tensões normais mais altas, as asperezas são progressivamente cisalhadas (em vez de contornadas), e o comportamento tende ao de uma superfície lisa (τ = σn·tan φb), sem o termo de dilatância.

O critério de **Barton-Bandis**, desenvolvido a partir de Barton (1973) e refinado por Barton & Choubey (1977) e Barton & Bandis (1990), generaliza essa ideia numa única expressão empírica contínua, sem a descontinuidade abrupta do modelo bilinear de Patton:

τ = σn · tan[φb + JRC · log10(JCS/σn)]

onde φb é o ângulo de atrito residual/básico, JRC é o coeficiente de rugosidade (0–20) e JCS é a resistência à compressão da parede. O termo JRC·log10(JCS/σn) representa a contribuição adicional de resistência por dilatância, que **diminui** à medida que a tensão normal σn aumenta (o log de um número que se aproxima de 1 tende a zero) — refletindo fisicamente que, sob confinamento alto, as asperezas são cisalhadas em vez de sobrepujadas, e o efeito de dilatância desaparece.

> [!tip] O critério de Barton-Bandis dá o ângulo de atrito efetivo de pico, não uma constante fixa
> Ao contrário de φ em Mohr-Coulomb (tratado como um único número), o ângulo de atrito efetivo de pico de uma descontinuidade pelo critério de Barton-Bandis, φb + JRC·log10(JCS/σn), **varia com a própria tensão normal aplicada** — é maior em tensões baixas (perto da superfície, em taludes rasos) e converge para φb em tensões altas (descontinuidades profundas, muito confinadas). Aplicar um único valor de "ângulo de atrito da descontinuidade" a toda a faixa de profundidade de um talude, sem recalcular pelo critério em cada nível de tensão normal relevante, é uma simplificação que pode superestimar a segurança em profundidade e subestimá-la perto da superfície.

### Permeabilidade do maciço rochoso: fluxo controlado por fraturas

Rocha intacta sã e pouco porosa costuma ter condutividade hidráulica intrínseca desprezível (Módulo 01, Aula 01) — na prática, quase toda a água que se move através de um maciço rochoso fraturado o faz através da rede de descontinuidades, não através da matriz. O fluxo dentro de uma única fratura, sob a idealização de duas paredes planas e paralelas separadas por uma abertura hidráulica **e**, segue a **lei cúbica** (*cubic law*), derivada da solução de fluxo laminar entre placas paralelas (equação de Navier-Stokes simplificada):

Q ∝ e³ · (dh/dl)

ou seja, a vazão através de uma fratura é proporcional ao **cubo** da abertura — uma dependência muito mais forte que a relação linear de Darcy em meio poroso granular. Uma consequência prática direta: pequenas variações na abertura efetiva de uma fratura (por exemplo, seu fechamento parcial sob tensão de confinamento crescente, ou sua abertura por dissolução ao longo do tempo, em rochas carbonáticas) produzem variações desproporcionalmente grandes na vazão transmitida — dobrar a abertura multiplica a vazão por oito.

Para fins de modelagem regional (onde não é viável simular cada fratura individualmente), o maciço fraturado é frequentemente tratado como um **meio poroso equivalente**, com uma condutividade hidráulica equivalente estimada a partir da densidade, orientação e abertura média das famílias de fraturas — uma simplificação válida em escala suficientemente grande (muitas fraturas por volume representativo), mas que pode falhar em escala local, onde o fluxo real concentra-se de forma muito heterógena em um pequeno número de fraturas mais abertas e mais conectadas (os chamados canais preferenciais de fluxo).

## Exemplo trabalhado

**Situação:** uma família de juntas num talude tem JRC = 12, JCS = 80 MPa e ângulo de atrito básico φb = 30°. Calcule o ângulo de atrito efetivo de pico previsto por Barton-Bandis para duas profundidades distintas: uma tensão normal de 0,2 MPa (perto da superfície) e uma de 4 MPa (mais profunda).

**Resolução:**

Em σn = 0,2 MPa: JCS/σn = 80/0,2 = 400. log10(400) ≈ 2,60. Componente de rugosidade = JRC × 2,60 = 12×2,60 = 31,2°. Ângulo efetivo = 30° + 31,2° = 61,2°.

Em σn = 4 MPa: JCS/σn = 80/4 = 20. log10(20) ≈ 1,30. Componente de rugosidade = 12×1,30 = 15,6°. Ângulo efetivo = 30° + 15,6° = 45,6°.

**Interpretação:** o ângulo de atrito efetivo de pico quase triplica em contribuição de rugosidade entre as duas profundidades (31,2° contra 15,6°) e o total cai de 61,2° para 45,6° — uma diferença substancial para qualquer análise de estabilidade de talude (Aula 07). Adotar, por simplicidade, um único valor médio de ângulo de atrito para toda a altura de um talude alto arrisca superestimar a resistência mobilizável nos níveis mais profundos (onde ela é, na realidade, mais próxima de φb) e subestimá-la perto da crista — mas o erro de maior consequência prática costuma ser o primeiro, porque é nos níveis mais profundos que a massa potencialmente instável é maior.

## Erros comuns

- **Ignorar completamente as descontinuidades e dimensionar uma escavação ou talude só com base na resistência da rocha intacta** — subestima grosseiramente o risco quando as descontinuidades estão desfavoravelmente orientadas, mesmo numa rocha intacta muito resistente.
- **Aplicar um único ângulo de atrito de descontinuidade (tirado de tabela genérica) sem considerar JRC, JCS e a tensão normal real do problema** — o critério de Barton-Bandis existe justamente porque esse ângulo não é uma constante do material, mas depende do estado de tensão local.
- **Confundir persistência com espaçamento** — uma descontinuidade pode ser muito persistente (centenas de metros de extensão) mas fazer parte de uma família com espaçamento grande (poucas descontinuidades por volume), ou vice-versa; são parâmetros geometricamente independentes.
- **Tratar a permeabilidade de um maciço fraturado como constante ao longo da vida útil de uma obra**, ignorando que o fechamento de fraturas por aumento de tensão de confinamento (por exemplo, ao redor de uma escavação profunda) pode reduzir drasticamente a condutividade hidráulica local, pela dependência cúbica da lei cúbica.

## O que não concluir

- **Que uma descontinuidade lisa (JRC baixo) é sempre menos resistente que uma rugosa.** Em tensões normais muito altas, onde as asperezas de qualquer rugosidade tendem a ser cisalhadas, a diferença de resistência entre uma junta lisa e uma rugosa se reduz — o efeito da rugosidade é mais relevante justamente nas tensões normais mais baixas.
- **Que o tratamento de meio poroso equivalente é válido em qualquer escala de análise.** É uma simplificação apropriada para fluxo regional através de um volume com muitas fraturas, mas pode falhar seriamente para prever fluxo através de uma única galeria ou poço, onde um pequeno número de fraturas conectadas pode dominar o comportamento observado.

## Recap relâmpago

- O comportamento mecânico e hidráulico de um maciço rochoso é, na maior parte dos casos práticos, governado pelas descontinuidades, não pela rocha intacta entre elas — daí a distinção entre "resistência da rocha" e "resistência do maciço".
- Os parâmetros geométricos padronizados de uma descontinuidade (ISRM, 1978) são orientação, espaçamento, persistência, rugosidade (JRC), abertura/preenchimento, resistência da parede (JCS) e número de famílias — cada um com efeito distinto sobre a resistência e a permeabilidade.
- O critério de Barton-Bandis, τ = σn·tan[φb + JRC·log10(JCS/σn)], descreve a resistência ao cisalhamento de uma descontinuidade rugosa como um ângulo de atrito efetivo que decresce com o aumento da tensão normal, convergindo para φb em altas tensões.
- O fluxo através de uma fratura individual segue a lei cúbica (Q ∝ e³), fazendo a permeabilidade do maciço muito mais sensível a pequenas mudanças de abertura do que a permeabilidade de um meio poroso granular equivalente.

## Próxima aula

[[05-mecanica-de-rochas-aula-05-tensoes-in-situ-metodos-de-determinacao|Aula 05 — Tensões in situ: origem e métodos de determinação (overcoring, fraturamento hidráulico, macacos planos)]]

## Anterior

[[05-mecanica-de-rochas-aula-03-criterios-de-ruptura-mohr-coulomb-griffith-hoek-brown|Aula 03 — Critérios de ruptura aplicáveis às rochas: Mohr-Coulomb, Griffith e Hoek-Brown]]

## Fontes

- Parâmetros geométricos padronizados de descontinuidades: ISRM (International Society for Rock Mechanics) (1978), "Suggested methods for the quantitative description of discontinuities in rock masses", *International Journal of Rock Mechanics and Mining Sciences*, 15(6).
- Critério de resistência ao cisalhamento bilinear de Patton: Patton, F. D. (1966), "Multiple modes of shear failure in rock", *Proceedings of the 1st Congress of ISRM*, Lisboa.
- Coeficiente de rugosidade JRC e critério de Barton-Bandis: Barton, N. (1973), "Review of a new shear strength criterion for rock joints", *Engineering Geology*, 7(4); Barton, N. & Choubey, V. (1977), "The shear strength of rock joints in theory and practice", *Rock Mechanics*, 10(1-2); Barton, N. & Bandis, S. (1990).
- Lei cúbica de fluxo em fraturas e permeabilidade equivalente de maciço fraturado: Goodman, R. E. (1989), *Introduction to Rock Mechanics*, 2ª ed., Wiley, cap. 6.

<!--
nivel: avancado
palavras_corpo: ~1900

mapa_objetivo_secao:
  geologia-avancado-m05-oa03: "Por que a descontinuidade, e não a rocha intacta, costuma governar o comportamento do maciço" + "Parâmetros geométricos de uma descontinuidade" + "Resistência ao cisalhamento de uma descontinuidade: o critério de Barton-Bandis" + "Permeabilidade do maciço rochoso: fluxo controlado por fraturas" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: MECROCHA-M05-A04-PARAMETROS-001
    claim: "Os parâmetros geométricos padronizados para descrição quantitativa de descontinuidades rochosas — orientação, espaçamento, persistência, rugosidade, abertura, preenchimento, resistência da parede e número de famílias — foram consolidados pela ISRM em 1978."
    risk: fato
    source: "ISRM 1978"
  - claim_id: MECROCHA-M05-A04-PATTON-002
    claim: "O modelo de Patton (1966) descreve a resistência ao cisalhamento de uma descontinuidade rugosa por um critério bilinear: τ=σn·tan(φb+i) em baixa tensão normal (dilatância por rugosidade), tendendo a τ=σn·tanφb em alta tensão normal, quando as asperezas passam a ser cisalhadas."
    risk: fato
    source: "Patton 1966"
  - claim_id: MECROCHA-M05-A04-BARTONBANDIS-003
    claim: "O critério de Barton-Bandis, τ=σn·tan[φb+JRC·log10(JCS/σn)], descreve a resistência ao cisalhamento de uma descontinuidade em função da tensão normal, do coeficiente de rugosidade JRC e da resistência da parede JCS, com a contribuição de rugosidade decrescendo à medida que a tensão normal aumenta."
    risk: fato
    source: "Barton 1973; Barton & Choubey 1977; Barton & Bandis 1990"
  - claim_id: MECROCHA-M05-A04-LEICUBICA-004
    claim: "O fluxo laminar através de uma fratura idealizada como duas placas planas e paralelas é proporcional ao cubo da abertura hidráulica da fratura (lei cúbica), tornando a permeabilidade de um maciço fraturado muito sensível a pequenas variações de abertura."
    risk: fato
    source: "Goodman 1989, cap. 6; solução clássica de fluxo laminar entre placas paralelas (Navier-Stokes)"
-->
