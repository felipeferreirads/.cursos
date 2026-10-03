# Aula 07: Estabilidade de taludes rochosos e escavações a céu aberto e subterrâneas

**ID:** geologia-avancado-m05-a07
**Módulo:** [[05-mecanica-de-rochas-modulo|Módulo 05 — Mecânica de rochas]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** identificar os modos de ruptura cinematicamente possíveis num talude rochoso a partir da orientação das descontinuidades, calcular o fator de segurança de uma ruptura planar simples, e descrever como uma escavação subterrânea redistribui as tensões ao seu redor e como essa redistribuição orienta o dimensionamento do suporte.
**Pré-requisito:** orientação e resistência ao cisalhamento de descontinuidades, incluindo Barton-Bandis (Aula 04); tensões in situ como estado de tensão de fundo antes da escavação (Aula 05); classificações geomecânicas RMR, Q e SMR (Aula 06).

## Antes de começar, você precisa saber

- Direção de mergulho e mergulho de um plano, e a noção de que a orientação relativa entre uma descontinuidade e uma face de talude determina se um deslizamento é geometricamente possível (Aula 04).
- Resistência ao cisalhamento de uma descontinuidade como função da tensão normal (critério de Barton-Bandis, Aula 04) e classificação SMR como índice de triagem de estabilidade de taludes (Aula 06).

## Conteúdo

### Análise cinemática: a orientação decide se a ruptura é geometricamente possível

Antes de calcular qualquer fator de segurança, a primeira pergunta em estabilidade de taludes rochosos é puramente geométrica: **a orientação das descontinuidades presentes permite, em princípio, algum modo de ruptura por deslizamento nessa face de talude específica?** Essa verificação — a **análise cinemática**, tradicionalmente feita com projeção estereográfica (redes de Schmidt ou Wulff) — precede a análise de forças, porque um plano de descontinuidade que mergulha na direção **oposta** à face do talude, por exemplo, não pode gerar deslizamento nessa face, não importa quão fraca seja sua resistência ao cisalhamento. Os quatro modos clássicos de ruptura em talude rochoso, cada um com sua condição cinemática de viabilidade:

- **Ruptura planar:** deslizamento ao longo de um único plano de descontinuidade que mergulha na mesma direção geral da face do talude (dentro de um envelope angular, tipicamente ±20°), com mergulho **menor** que o mergulho da face (para a descontinuidade aflorar na face) e **maior** que o ângulo de atrito da descontinuidade (para que exista uma força motriz líquida).
- **Ruptura em cunha:** deslizamento ao longo da linha de interseção de duas descontinuidades de famílias distintas, que juntas formam uma cunha destacável — viável cinematicamente quando a linha de interseção mergulha na direção geral da face e com mergulho menor que o da face, mas maior que o ângulo de atrito mobilizado ao longo das duas superfícies.
- **Tombamento (toppling):** ocorre quando descontinuidades íngremes mergulham para **dentro** do maciço, no sentido contrário ao da face do talude — colunas ou lâminas de rocha delimitadas por essas descontinuidades tombam para fora por flexão (*flexural toppling*, em rocha estratificada fina) ou como blocos rígidos que giram apoiados numa base (*block toppling*).
- **Ruptura circular (ou "rotacional"):** não controlada por uma descontinuidade discreta, mas por uma superfície de ruptura que atravessa a massa como um todo — típica de maciços muito fraturados, intensamente intemperizados, ou de solo residual, onde o comportamento se aproxima do de um material homogêneo equivalente (a mesma lógica de análise usada em mecânica dos solos, retomada no Módulo 06); analisada por métodos de equilíbrio limite de fatias, não pela geometria de blocos discretos.

> [!important] A pergunta cinemática vem antes da pergunta sobre resistência
> Um erro conceitual recorrente é calcular diretamente um fator de segurança para um modo de ruptura que a orientação geométrica torna inviável — por exemplo, testar ruptura planar numa descontinuidade que mergulha para dentro do maciço. A sequência correta é sempre: primeiro, a projeção estereográfica (ou o teste de Markland, uma verificação simplificada equivalente) determina **quais** modos são cinematicamente possíveis para aquela combinação específica de orientações; só então o cálculo de forças é aplicado ao(s) modo(s) viável(is).

### Fator de segurança de uma ruptura planar simples

Para o caso mais simples — ruptura planar, sem água na trinca de tração, considerando apenas o peso próprio do bloco deslizante —, o fator de segurança (FS) é a razão entre a força resistente (resistência ao cisalhamento mobilizável ao longo do plano) e a força motriz (componente do peso que atua no sentido do deslizamento):

FS = (c·A + N·tan φ) / T

onde A é a área da superfície de deslizamento, N é a componente da força peso normal ao plano de ruptura, T é a componente do peso paralela ao plano (a força motriz), e c e φ são os parâmetros de resistência da descontinuidade (obtidos, idealmente, do critério de Barton-Bandis calculado para a tensão normal real do problema, Aula 04, não de uma tabela genérica). Para um bloco de peso W sobre um plano que mergulha a um ângulo ψp:

N = W·cos ψp        T = W·sen ψp

Quando presente, a **água numa trinca de tração** na crista do talude e ao longo do plano de ruptura reduz o fator de segurança por dois mecanismos simultâneos: a pressão de água na própria trinca de tração empurra o bloco na direção do deslizamento (uma força motriz adicional, V), e a subpressão de água ao longo do plano de ruptura (U) reduz a tensão normal efetiva e, portanto, a componente friccional da resistência (retomando o princípio de tensão efetiva, análogo ao usado em hidrogeologia — Módulo 01 — mas aqui aplicado ao plano de uma descontinuidade em vez de a um meio poroso contínuo):

FS = [c·A + (W·cos ψp − U − V·sen ψp)·tan φ] / (W·sen ψp + V·cos ψp)

> [!warning] Água é, na prática, o fator mais controlável e um dos mais decisivos
> Diferente da geometria e da resistência intrínseca da descontinuidade — em grande parte fixadas pela geologia local —, a pressão de água numa trinca de tração pode ser reduzida por drenagem (drenos sub-horizontais, por exemplo), oferecendo uma das intervenções de engenharia mais custo-efetivas para elevar o fator de segurança de um talude marginalmente instável, sem alterar a geometria de escavação nem instalar suporte estrutural pesado.

### Ruptura em cunha e tombamento: extensões do mesmo princípio

A **ruptura em cunha** aplica a mesma lógica de forças da ruptura planar, mas projetada sobre a linha de interseção de dois planos em vez de um único plano — o cálculo é mais elaborado (a resultante do peso precisa ser decomposta nas componentes normais a cada uma das duas superfícies, cada uma com sua própria resistência ao cisalhamento), e por isso é tradicionalmente resolvido com ábacos padronizados (Hoek & Bray, 1981) ou software específico, em vez de uma fórmula fechada única — mas o princípio (força resistente sobre força motriz, agora numa geometria tridimensional) é o mesmo da ruptura planar.

O **tombamento** não é bem descrito por uma análise de equilíbrio de forças de deslizamento simples, porque o modo de falha é rotacional, não translacional — a condição analisada é se o momento do peso próprio em torno da base de apoio de cada coluna ou bloco supera o momento resistente (que depende da largura da base do bloco e do atrito nas juntas basais). Métodos de equilíbrio limite específicos para tombamento (por exemplo, o método de Goodman & Bray, 1976) tratam a coluna como uma sequência de blocos que podem escorregar entre si e tombar individualmente, propagando o efeito de um bloco para o seguinte.

### Escavações subterrâneas: redistribuição de tensão ao redor de uma abertura

Ao escavar uma abertura subterrânea (túnel, galeria, câmara), o maciço ao redor precisa redistribuir a tensão que antes passava através do volume agora vazio — a tensão in situ de fundo (Aula 05) é concentrada nas paredes da escavação. Para o caso idealizado de uma abertura circular num meio elástico contínuo sob um campo de tensão biaxial remoto (σv vertical, σh horizontal), as **equações de Kirsch** (solução analítica clássica de elasticidade, 1898) descrevem a tensão tangencial na parede da escavação em função da posição angular θ e da razão K = σh/σv:

- No teto e no piso da escavação (θ = 90°/270°, medido a partir da horizontal): a tensão tangencial é 3σh − σv = (3K−1)·σv — se K for baixo (campo dominado pela tensão vertical), essa tensão pode ser baixa ou até negativa (tração, quando K < 1/3), um dos motivos pelos quais tetos de escavação sob baixo confinamento horizontal são propensos a desplacamento e queda de blocos; se K for alto, a tensão no teto e no piso cresce e pode se aproximar da resistência à compressão da rocha.
- Nas paredes laterais (θ = 0°/180°): a tensão tangencial é 3σv − σh = (3−K)·σv — concentrando a maior compressão exatamente quando K é baixo (campo dominado pela tensão vertical), com risco de dano por compressão elevada nesse regime (incluindo, em profundidade e sob rocha resistente e frágil, o fenômeno de *rock burst*, já introduzido pelo fator SRF do sistema Q na Aula 06, cujo risco cresce com o nível absoluto de tensão, não apenas com K).

Esse resultado — que a concentração de tensão ao redor de uma abertura depende diretamente de K — conecta diretamente a Aula 05 (medição de K in situ) ao dimensionamento da escavação: uma mesma geometria de túnel pode ser segura sob um campo de tensão e problemática sob outro, dependendo exclusivamente da razão de tensões medida antes de escavar.

> [!tip] O princípio de convergência-confinamento formaliza a interação suporte-maciço ao longo do tempo
> À medida que a face de escavação avança para além de um dado ponto do túnel, a tensão ali se redistribui progressivamente (não instantaneamente) e o maciço converge (se deforma para dentro da abertura) até estabilizar ou romper. O método de **convergência-confinamento**, usado no dimensionamento conceitual de suporte (associado à filosofia do NATM — *New Austrian Tunnelling Method*), representa essa interação como duas curvas que se cruzam: a curva característica do maciço (quanto ele converge para cada nível de pressão de confinamento remanescente) e a curva de reação do suporte (quanta pressão o suporte oferece para cada deslocamento que já ocorreu antes de sua instalação) — instalar o suporte cedo demais sobrecarrega-o com toda a convergência ainda por vir; instalar tarde demais permite deformação excessiva ou ruptura antes que o suporte atue.

### Suporte de escavações: reforço, sustentação e o papel das classificações geomecânicas

O suporte de uma escavação subterrânea combina, em geral, duas estratégias complementares: **reforço** (tirantes/chumbadores ancorados na própria rocha, que mobilizam a resistência do maciço ao redor da abertura, prendendo blocos individuais entre si e criando um efeito de arco autoportante) e **sustentação** (concreto projetado, cambotas metálicas, revestimento — elementos estruturais que aplicam uma pressão de confinamento externa à superfície escavada). As classificações geomecânicas da Aula 06 (RMR e, sobretudo, Q, via o ábaco de dimensão equivalente De e o fator ESR) fornecem a orientação preliminar de qual combinação e intensidade de suporte é tipicamente necessária para uma dada qualidade de maciço e um dado vão de escavação — uma estimativa de triagem, refinada, em projetos de maior porte, por análise numérica ou por monitoramento de convergência durante a própria execução da obra.

## Exemplo trabalhado

**Situação:** um talude rochoso tem 25 m de altura, com uma descontinuidade planar que aflora na face, mergulhando a ψp = 35°. O peso do bloco potencialmente instável é W = 4.500 kN, a área da superfície de deslizamento é A = 180 m², a coesão da descontinuidade é c = 20 kPa e o ângulo de atrito é φ = 32° (já calculado pelo critério de Barton-Bandis para a tensão normal relevante deste bloco, Aula 04). Não há água na trinca de tração (U=V=0). Calcule o fator de segurança.

**Resolução:**

N = W·cos ψp = 4.500×cos 35° ≈ 4.500×0,8192 ≈ 3.686 kN.

T = W·sen ψp = 4.500×sen 35° ≈ 4.500×0,5736 ≈ 2.581 kN.

Força resistente = c·A + N·tan φ = 20×180 + 3.686×tan 32° = 3.600 + 3.686×0,6249 ≈ 3.600 + 2.304 ≈ 5.904 kN.

FS = 5.904 / 2.581 ≈ 2,29.

**Interpretação:** um FS de 2,29, sem consideração de água, indica uma margem de segurança confortável nas condições atuais — mas a Aula 07 já deixou claro que essa mesma descontinuidade, se preenchida com água numa estação chuvosa, teria sua tensão normal efetiva reduzida e receberia uma força motriz adicional (V), ambos reduzindo o FS calculado. Um projeto responsável não reportaria apenas o FS na condição seca mais favorável, mas recalcularia o cenário com o nível de água na trinca de tração correspondente ao evento de projeto (por exemplo, uma chuva de período de retorno definido pelo regulamento aplicável), e só então decidiria se o talude, nessa condição mais desfavorável plausível, ainda atende ao FS mínimo exigido pelo projeto.

## Erros comuns

- **Calcular um fator de segurança de ruptura planar ou em cunha sem antes confirmar, por análise cinemática, que a orientação das descontinuidades torna esse modo de ruptura geometricamente possível** — um número de FS sem sentido físico se a geometria não permite o deslizamento analisado.
- **Ignorar a presença ou o cenário futuro de água em trincas de tração**, calculando o FS apenas na condição seca mais favorável, sem considerar o cenário de projeto relevante (evento de chuva de referência, elevação do lençol freático).
- **Aplicar a análise de equilíbrio de forças de ruptura planar/em cunha a um caso de tombamento**, quando o modo correto de falha é rotacional, exigindo um método de equilíbrio de momentos específico (Goodman & Bray, 1976), não uma simples razão força resistente/motriz.
- **Assumir que uma escavação circular sob campo de tensão isotrópico (K=1) representa bem qualquer geometria e razão de tensão real** — as equações de Kirsch mostram que a concentração de tensão ao redor de uma abertura depende fortemente de K e da forma da abertura; extrapolar sem ajustar para o K real medido (Aula 05) pode subestimar seriamente a tensão de pico no teto ou nas paredes.

## O que não concluir

- **Que um fator de segurança alto na condição atual garante estabilidade permanente do talude.** Taludes evoluem: intemperismo progressivo reduz φ e c ao longo do tempo, eventos de chuva extremos elevam pressões de água episodicamente, e vibração de desmonte ou tráfego pode induzir deslocamentos incrementais — um FS calculado hoje descreve a condição hoje, não uma garantia perpétua sem monitoramento.
- **Que o suporte de uma escavação subterrânea existe para "segurar o peso da rocha" como uma estrutura que sustenta uma carga externa.** Na filosofia moderna de suporte (refletida no método de convergência-confinamento e no conceito de reforço), o objetivo primário é **mobilizar e preservar a resistência inerente do próprio maciço** ao redor da abertura — o suporte trabalha em conjunto com o maciço, não em vez dele, e um suporte rígido instalado cedo demais pode, contraintuitivamente, atrair mais carga e falhar antes de um suporte mais flexível instalado no momento certo do processo de convergência.

## Recap relâmpago

- A análise cinemática (projeção estereográfica) determina quais modos de ruptura (planar, em cunha, tombamento) são geometricamente possíveis para uma dada combinação de orientação de descontinuidades e face de talude, e deve preceder qualquer cálculo de fator de segurança.
- O fator de segurança de uma ruptura planar simples é a razão entre a resistência ao cisalhamento mobilizável (c·A + N·tanφ) e a força motriz (T = W·senψp), reduzido pela presença de água numa trinca de tração, que aumenta a força motriz e reduz a tensão normal efetiva simultaneamente.
- Ruptura em cunha estende a mesma lógica a duas superfícies de interseção, resolvida por ábacos ou software; tombamento é um modo rotacional distinto, analisado por equilíbrio de momentos entre blocos, não pela mesma razão força resistente/motriz.
- As equações de Kirsch mostram que a redistribuição de tensão ao redor de uma escavação circular depende diretamente da razão K=σh/σv medida in situ (Aula 05) — sob K baixo, o teto e o piso arriscam entrar em tração e desplacar, enquanto as paredes laterais concentram a maior compressão (e o risco de rock burst); sob K alto, esse padrão se inverte, concentrando mais tensão no teto e no piso.
- O suporte de escavações combina reforço (mobiliza a resistência do próprio maciço) e sustentação (aplica confinamento externo), dimensionado preliminarmente pelas classificações RMR/Q (Aula 06) e refinado pelo princípio de convergência-confinamento, que trata o momento de instalação do suporte como uma variável crítica de projeto.

## Próxima aula

Última aula do módulo. Avaliação: [[05-mecanica-de-rochas-questionario-parcial-2|Questionário parcial 2]] (aulas 05–07) e [[05-mecanica-de-rochas-questionario-final|Questionário final cumulativo]] (aulas 01–07). Próximo módulo: [[06-elementos-de-geomecanica/06-elementos-de-geomecanica-modulo|Módulo 06 — Elementos de geomecânica]].

## Anterior

[[05-mecanica-de-rochas-aula-06-classificacoes-geomecanicas-rmr-q-gsi-smr|Aula 06 — Classificações geomecânicas de maciços rochosos: RMR, Q, GSI e SMR]]

## Fontes

- Análise cinemática de taludes rochosos (projeção estereográfica, teste de Markland) e fórmula de fator de segurança para ruptura planar com água em trinca de tração: Hoek, E. & Bray, J. W. (1981), *Rock Slope Engineering*, 3ª ed., Institution of Mining and Metallurgy, cap. 5–9.
- Método de equilíbrio limite para tombamento de blocos: Goodman, R. E. & Bray, J. W. (1976), "Toppling of rock slopes", *Proceedings of the Specialty Conference on Rock Engineering for Foundations and Slopes*, ASCE.
- Equações de Kirsch para concentração de tensão ao redor de abertura circular: Kirsch, G. (1898), "Die Theorie der Elastizität und die Bedürfnisse der Festigkeitslehre", *Zeitschrift des Vereines Deutscher Ingenieure*, 42; reproduzido em Jaeger, Cook & Zimmerman (2007), *Fundamentals of Rock Mechanics*, 4ª ed., Blackwell, cap. 5.
- Método de convergência-confinamento e princípios de suporte de escavações subterrâneas: Hoek, E., Kaiser, P. K. & Bawden, W. F. (1995), *Support of Underground Excavations in Hard Rock*, Balkema, cap. 8.

<!--
nivel: avancado
palavras_corpo: ~2150

mapa_objetivo_secao:
  geologia-avancado-m05-oa04: "Análise cinemática: a orientação decide se a ruptura é geometricamente possível" + "Fator de segurança de uma ruptura planar simples" + "Ruptura em cunha e tombamento: extensões do mesmo princípio" + "Escavações subterrâneas: redistribuição de tensão ao redor de uma abertura" + "Suporte de escavações: reforço, sustentação e o papel das classificações geomecânicas" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: MECROCHA-M05-A07-CINEMATICA-001
    claim: "A análise cinemática de estabilidade de taludes rochosos (por projeção estereográfica) determina se ruptura planar, em cunha ou tombamento são geometricamente possíveis a partir da orientação relativa entre as descontinuidades e a face do talude, devendo preceder qualquer cálculo de fator de segurança."
    risk: fato
    source: "Hoek & Bray 1981, cap. 5-9"
  - claim_id: MECROCHA-M05-A07-FSPLANAR-002
    claim: "O fator de segurança de uma ruptura planar simples com água em trinca de tração é dado por FS=[c·A+(W·cosψp−U−V·senψp)·tanφ]/(W·senψp+V·cosψp), onde U é a subpressão ao longo do plano de ruptura e V é a força da água na trinca de tração."
    risk: fato
    source: "Hoek & Bray 1981, cap. 6"
  - claim_id: MECROCHA-M05-A07-KIRSCH-003
    claim: "As equações de Kirsch (1898) para uma abertura circular num meio elástico sob campo de tensão biaxial mostram que a tensão tangencial no teto/piso é 3σh−σv=(3K−1)σv e nas paredes laterais é 3σv−σh=(3−K)σv, onde K=σh/σv, de modo que a concentração de tensão ao redor da abertura depende diretamente da razão K e se inverte entre teto/piso e paredes conforme K seja baixo ou alto."
    risk: fato
    source: "Kirsch 1898; Jaeger, Cook & Zimmerman 2007, cap. 5"
  - claim_id: MECROCHA-M05-A07-CONVCONF-004
    claim: "O método de convergência-confinamento representa a interação suporte-maciço ao redor de uma escavação subterrânea pelo cruzamento entre a curva característica do maciço (convergência versus pressão de confinamento remanescente) e a curva de reação do suporte, sendo o momento de instalação do suporte uma variável crítica de projeto."
    risk: fato
    source: "Hoek, Kaiser & Bawden 1995, cap. 8"
-->
