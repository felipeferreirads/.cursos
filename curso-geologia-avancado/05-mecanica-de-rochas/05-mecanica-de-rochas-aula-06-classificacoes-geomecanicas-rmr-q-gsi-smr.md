# Aula 06: Classificações geomecânicas de maciços rochosos: RMR, Q, GSI e SMR

**ID:** geologia-avancado-m05-a06
**Módulo:** [[05-mecanica-de-rochas-modulo|Módulo 05 — Mecânica de rochas]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** classificar um maciço rochoso pelos sistemas RMR, Q e GSI, obter parâmetros de resistência do maciço (Hoek-Brown) a partir do GSI, e adaptar a classificação RMR para taludes pelo sistema SMR.
**Pré-requisito:** parâmetros geométricos de descontinuidades — orientação, espaçamento, persistência, rugosidade, abertura, preenchimento, resistência da parede (Aula 04); critério de Hoek-Brown para maciço rochoso, cujos parâmetros mb, s e a dependem do GSI (Aula 03).

## Antes de começar, você precisa saber

- Que os parâmetros de descontinuidade (espaçamento, rugosidade JRC, abertura, preenchimento, resistência da parede JCS) descrevem uma descontinuidade individual ou uma família (Aula 04) — as classificações desta aula agregam esses parâmetros, junto com propriedades da rocha intacta, numa nota única que caracteriza o maciço como um todo.
- Que o critério de Hoek-Brown generalizado depende dos parâmetros mb, s e a (Aula 03), que serão obtidos a partir do GSI nesta aula.

## Conteúdo

### Por que classificar um maciço com um único índice numérico

Um maciço rochoso é descrito por dezenas de parâmetros (resistência da rocha intacta, RQD, espaçamento, orientação, rugosidade, água subterrânea, e mais). Um índice de classificação geomecânica **agrega** esses parâmetros numa nota única, calibrada empiricamente contra o desempenho observado de obras reais (escavações que precisaram ou não de suporte, taludes que romperam ou se mantiveram estáveis) — permitindo comparar maciços de forma padronizada, estimar rapidamente uma faixa de suporte necessário numa fase preliminar de projeto, e alimentar diretamente critérios de ruptura de maciço, como Hoek-Brown (Aula 03), que de outra forma exigiriam ensaios triaxiais completos do maciço fraturado — inviáveis de realizar em escala de campo.

### RMR (Rock Mass Rating): a classificação de Bieniawski

O **RMR**, desenvolvido por Z. T. Bieniawski a partir de 1973 e consolidado na versão de 1989 amplamente usada até hoje, atribui pontos a cinco parâmetros principais, cuja soma dá uma nota de 0 a 100:

1. **Resistência à compressão uniaxial da rocha intacta** (0–15 pontos): quanto maior a UCS (Aula 02), maior a pontuação.
2. **RQD — Rock Quality Designation** (0–20 pontos): a fração, em %, de um testemunho de sondagem composta por pedaços intactos de comprimento ≥ 10 cm, em relação ao comprimento total perfurado — um índice indireto de fraturamento, proposto por Deere (1964), incorporado ao RMR como um dos cinco parâmetros.
3. **Espaçamento das descontinuidades** (0–20 pontos): maior espaçamento (blocos maiores) pontua mais alto.
4. **Condição das descontinuidades** (0–30 pontos, o parâmetro de maior peso): combina persistência, abertura, rugosidade, preenchimento e grau de intemperismo das paredes — o parâmetro mais qualitativo e o que exige mais julgamento de campo experiente.
5. **Condição de água subterrânea** (0–15 pontos): de seco a fluxo abundante sob pressão, penalizando maciços com percolação significativa através das descontinuidades.

A soma bruta desses cinco parâmetros é ajustada por um sexto fator — a **orientação das descontinuidades em relação à obra** —, subtraído da soma (correção que pode chegar a −12 pontos para túneis, mais severa para taludes), refletindo que a mesma descontinuidade pode ser irrelevante ou crítica dependendo apenas de sua orientação relativa à escavação. A nota final classifica o maciço em cinco classes, de **RMR I (81–100, maciço muito bom)** a **RMR V (0–20, maciço muito fraco)**, cada uma associada, nas tabelas originais de Bieniawski, a uma faixa orientativa de tempo de autossustentação (*stand-up time*) e a recomendações preliminares de suporte para túneis.

### O sistema Q de Barton, Lien e Lunde

O **sistema Q** (Barton, Lien & Lunde, 1974), desenvolvido a partir de centenas de casos históricos de túneis escandinavos, calcula um índice de qualidade pela razão de seis parâmetros, agrupados em três pares:

Q = (RQD/Jn) × (Jr/Ja) × (Jw/SRF)

- **RQD/Jn** (tamanho de bloco): RQD já definido acima; Jn é o número de famílias de descontinuidades — a razão estima o tamanho relativo dos blocos.
- **Jr/Ja** (resistência ao cisalhamento entre blocos): Jr é o número de rugosidade da junta (análogo em espírito ao JRC de Barton-Bandis, Aula 04, mas numa escala de classificação categórica); Ja é o número de alteração da junta (penaliza preenchimentos argilosos ou paredes alteradas).
- **Jw/SRF** (efeito do estado de tensão ativo): Jw é o fator de redução por água (penaliza fluxo e pressão de água na escavação); SRF (*Stress Reduction Factor*) penaliza tanto zonas de fraqueza sob baixo confinamento quanto, no outro extremo, rocha competente sob tensão muito alta (risco de *rock burst*, ruptura frágil violenta por liberação de energia elástica armazenada).

O valor de Q varia numa escala logarítmica extremamente ampla, de 0,001 (maciço excepcionalmente fraco) a 1.000 (maciço excepcionalmente bom). O sistema Q é usado diretamente para dimensionar o suporte de uma escavação subterrânea através do conceito de **dimensão equivalente** (De = vão ou altura da escavação dividido pelo **ESR**, *Excavation Support Ratio* — um fator que reflete a tolerância a risco da obra, menor para obras críticas como centrais de energia, maior para túneis de mineração temporários), plotada num ábaco padronizado que relaciona Q e De diretamente à categoria de suporte recomendada (tipo e espessura de concreto projetado, padrão e comprimento de chumbadores).

> [!tip] RMR e Q medem coisas semelhantes por caminhos diferentes, e nenhum é estritamente superior
> Os dois sistemas correlacionam-se empiricamente entre si (relações aproximadas do tipo RMR ≈ 9·ln(Q) + 44 têm sido propostas, mas com dispersão considerável caso a caso) porque capturam, no fundo, o mesmo conjunto de fatores físicos — tamanho de bloco, resistência das descontinuidades, água, estado de tensão. A escolha entre eles em um projeto real costuma refletir a tradição regional/setorial (Q é historicamente mais associado a projetos escandinavos e ao método NATM/NMT de escavação, RMR a uma tradição mais ampla de mineração e engenharia civil) mais do que uma superioridade técnica de um sobre o outro — projetos cuidadosos frequentemente calculam ambos para validação cruzada.

### GSI (Geological Strength Index): a ponte para o critério de Hoek-Brown

O **GSI**, introduzido por Hoek em 1994 e refinado em versões posteriores (Hoek, Marinos & Benissi, 1998; Marinos & Hoek, 2000), foi desenvolvido especificamente para suprir uma lacuna deixada por RMR e Q: nenhum dos dois fornece diretamente os parâmetros necessários para o critério de ruptura de Hoek-Brown do maciço (mb, s, a — Aula 03). O GSI é estimado por um **ábaco qualitativo** que cruza duas dimensões visuais de campo:

- **Estrutura do maciço:** de blocos bem entalhados e pouco perturbados até completamente esmagado/laminado, passando por graus intermediários de blocagem, dobramento e cisalhamento.
- **Condição das superfícies das descontinuidades:** de muito rugosa e sã até muito intemperizada, cisalhada e com preenchimento argiloso espesso.

O valor de GSI, tipicamente entre 10 (maciço muito pobre) e 90 (maciço de excelente qualidade), converte-se diretamente nos parâmetros de Hoek-Brown generalizado por relações empíricas publicadas (Hoek, Carranza-Torres & Corkum, 2002):

mb = mi · exp[(GSI−100)/(28−14D)]

s = exp[(GSI−100)/(9−3D)]

a = 1/2 + (1/6)·[exp(−GSI/15) − exp(−20/3)]

onde D é um fator de perturbação (0 para escavação cuidadosa/mecanizada, até 1 para desmonte a fogo mal controlado ou alívio de tensão por escavação extensa), e mi é o parâmetro litológico da rocha intacta (Aula 03). Diferente de RMR e Q, o GSI é deliberadamente **puramente qualitativo e visual** — não soma pontuações numéricas de parâmetros separados —, uma escolha proposital de Hoek para evitar a dupla contagem de fatores que já estão implicitamente correlacionados entre si (por exemplo, maciços muito fraturados tendem também a ter superfícies mais alteradas).

> [!warning] GSI não deve ser aplicado a maciços com poucas famílias de descontinuidades muito espaçadas
> O GSI pressupõe um maciço suficientemente fraturado para se comportar, em escala da obra, como um meio equivalente aproximadamente isotrópico. Em maciços com uma ou duas famílias dominantes muito espaçadas (poucos blocos grandes controlando o comportamento), a resposta mecânica é fortemente anisotrópica e dominada pela orientação específica das poucas descontinuidades presentes — nesse caso, uma análise de blocos individuais (cinemática de cunhas, Aula 07) é mais apropriada que um índice de maciço equivalente contínuo como o GSI.

### SMR (Slope Mass Rating): RMR adaptado para taludes

O **SMR**, proposto por Manuel Romana em 1985, adapta o RMR (chamado, nesse contexto, RMRb — *basic RMR*, sem a correção de orientação genérica) especificamente para a análise de estabilidade de taludes, substituindo aquela correção genérica por quatro fatores de ajuste calibrados para a geometria específica de um talude rochoso:

SMR = RMRb + (F1 × F2 × F3) + F4

- **F1:** depende do paralelismo entre a direção de mergulho da descontinuidade crítica e a direção de mergulho da face do talude — máximo (F1=1) quando são quase paralelas (condição mais desfavorável para ruptura planar), mínimo (F1≈0,15) quando divergem mais de 30°.
- **F2:** depende do mergulho da descontinuidade (para ruptura planar) — relacionado à probabilidade de a resistência ao cisalhamento mobilizada ser suficiente; para ruptura por tombamento (*toppling*), F2 é fixado em 1,0 por convenção.
- **F3:** compara o mergulho da descontinuidade com o mergulho da face do talude — penaliza fortemente quando a descontinuidade mergulha mais suavemente que a face (situação onde a descontinuidade "aflora" na face, condição necessária para ruptura planar cinematicamente possível).
- **F4:** um ajuste que depende do método de escavação do talude (natural, pré-fissurado/controlado, desmonte a fogo suave, desmonte a fogo comum ou deficiente) — desmonte mal controlado pode danificar e enfraquecer a rocha remanescente, penalizando a nota.

O SMR resultante classifica o talude em cinco classes (de SMR I, muito bom, praticamente estável, a SMR V, muito ruim, com ruptura ativa esperada), cada uma associada a uma recomendação genérica de tratamento (sem suporte, suporte pontual, suporte sistemático, redesenho do talude, ou escavação inviável sem intervenção maior) — a mesma lógica de RMR e Q, mas calibrada para o modo de falha específico de taludes (planar, em cunha ou por tombamento), tema desenvolvido na Aula 07.

## Exemplo trabalhado

**Situação:** um afloramento de gnaisse a ser escavado para uma galeria de mina tem: UCS = 90 MPa (10 pontos no RMR), RQD = 65% (13 pontos), espaçamento médio de 0,4 m (10 pontos), condição de descontinuidades moderadamente rugosas com abertura pequena e leve alteração (20 pontos), e fluxo de água úmido, sem gotejamento livre (7 pontos). Calcule o RMR básico (antes da correção de orientação) e classifique o maciço.

**Resolução:**

RMR básico = 10 + 13 + 10 + 20 + 7 = 60.

**Classificação:** RMR 60 cai na Classe III (RMR 41–60), maciço de qualidade **regular** ("fair rock") — nem bom o suficiente para dispensar suporte sistemático, nem tão fraco a ponto de exigir suporte pesado imediato; a faixa orientativa de tempo de autossustentação para essa classe, em vãos moderados, é da ordem de dias a poucas semanas, exigindo suporte relativamente rápido após a escavação.

**Interpretação:** note que nenhum dos cinco parâmetros individuais, isoladamente, seria alarmante (RQD de 65% e UCS de 90 MPa não soam como "maciço ruim"), mas a combinação — em especial a condição de descontinuidades moderadamente comprometida e o fluxo de água presente — empurra a nota total para a faixa "regular", não "boa". É exatamente esse efeito de agregação, capturando a interação entre parâmetros individualmente não críticos, que justifica o uso de uma classificação composta em vez de decidir com base num único parâmetro isolado.

## Erros comuns

- **Aplicar diretamente os parâmetros de Hoek-Brown para rocha intacta (mi, s=1) a um maciço fraturado**, em vez de calcular mb e s a partir do GSI real do maciço — um erro já sinalizado na Aula 03, mas que reaparece aqui como a causa mais comum de superestimar a resistência do maciço em projeto.
- **Estimar o GSI a partir de fotografias de baixa resolução ou de descrições de sondagem em vez de observação direta e extensa de afloramento ou de parede de escavação** — o GSI é deliberadamente qualitativo e depende de julgamento experiente sobre a estrutura em escala de maciço, não apenas do testemunho de um furo isolado.
- **Usar RMR ou Q calculados para dimensionar suporte de túnel diretamente como um índice de estabilidade de talude**, sem a adaptação SMR — a correção de orientação do RMR genérico não captura corretamente a cinemática específica de ruptura de taludes (planar, cunha, tombamento).
- **Comparar numericamente RMR e Q como se fossem a mesma escala** (por exemplo, tratar "RMR 60" e "Q 6" como equivalentes por alguma regra de conversão fixa e universal) sem reconhecer a dispersão considerável nas correlações empíricas entre os dois sistemas.

## O que não concluir

- **Que uma classificação geomecânica substitui o critério de ruptura ou a análise de estabilidade específica da obra.** RMR, Q, GSI e SMR são ferramentas de **triagem e comunicação padronizada** entre profissionais — orientam decisões preliminares de suporte e apontam para a faixa correta de parâmetros de resistência (via GSI → Hoek-Brown), mas não substituem uma análise de equilíbrio limite ou numérica específica do problema geométrico real (Aula 07).
- **Que uma nota de classificação alta garante ausência de risco local.** Mesmo um maciço com RMR ou Q globalmente favoráveis pode conter uma única descontinuidade crítica, desfavoravelmente orientada, capaz de causar uma ruptura localizada — as classificações descrevem uma tendência média do maciço, não eliminam a necessidade de mapear estruturas individuais críticas.

## Recap relâmpago

- Classificações geomecânicas agregam parâmetros de rocha intacta e de descontinuidades numa nota única, calibrada empiricamente contra o desempenho real de obras — úteis para triagem preliminar, comparação padronizada e, no caso do GSI, para alimentar diretamente o critério de Hoek-Brown do maciço.
- RMR (Bieniawski) soma cinco parâmetros (UCS, RQD, espaçamento, condição de descontinuidades, água) numa escala de 0–100, ajustada por orientação, em cinco classes de I a V.
- Q (Barton, Lien & Lunde) multiplica três razões — tamanho de bloco, resistência entre blocos, efeito do estado de tensão ativo — numa escala logarítmica de 0,001 a 1.000, usada diretamente para dimensionar suporte via dimensão equivalente (De) e ESR.
- GSI (Hoek) é um índice puramente qualitativo e visual (estrutura × condição de superfície), a única classificação desta aula que se converte diretamente nos parâmetros mb, s e a do critério de Hoek-Brown para maciço.
- SMR (Romana) adapta o RMR básico para taludes com quatro fatores de ajuste (F1–F4) que capturam a relação geométrica entre a orientação da descontinuidade crítica e a face do talude, calibrados para os modos de ruptura planar, em cunha e por tombamento.

## Próxima aula

[[05-mecanica-de-rochas-aula-07-estabilidade-de-taludes-e-escavacoes|Aula 07 — Estabilidade de taludes rochosos e escavações a céu aberto e subterrâneas]]

## Anterior

[[05-mecanica-de-rochas-aula-05-tensoes-in-situ-metodos-de-determinacao|Aula 05 — Tensões in situ: origem e métodos de determinação (overcoring, fraturamento hidráulico, macacos planos)]]

## Fontes

- Sistema RMR e tabelas de classificação (1989): Bieniawski, Z. T. (1989), *Engineering Rock Mass Classifications*, Wiley.
- Índice RQD: Deere, D. U. (1964), "Technical description of rock cores for engineering purposes", *Rock Mechanics and Engineering Geology*, 1(1).
- Sistema Q e dimensionamento de suporte por dimensão equivalente: Barton, N., Lien, R. & Lunde, J. (1974), "Engineering classification of rock masses for the design of tunnel support", *Rock Mechanics*, 6(4).
- GSI e relações empíricas com mb, s, a de Hoek-Brown generalizado: Hoek, E. (1994), "Strength of rock and rock masses", *ISRM News Journal*, 2(2); Hoek, E., Carranza-Torres, C. & Corkum, B. (2002), "Hoek-Brown failure criterion — 2002 edition", *Proceedings of NARMS-TAC Conference*, Toronto; Marinos, P. & Hoek, E. (2000), "GSI: a geologically friendly tool for rock mass strength estimation".
- Sistema SMR: Romana, M. (1985), "New adjustment ratings for application of Bieniawski classification to slopes", *Proceedings of the International Symposium on the Role of Rock Mechanics*, Zacatecas.

<!--
nivel: avancado
palavras_corpo: ~2100

mapa_objetivo_secao:
  geologia-avancado-m05-oa03: "Por que classificar um maciço com um único índice numérico" + "RMR (Rock Mass Rating): a classificação de Bieniawski" + "O sistema Q de Barton, Lien e Lunde" + "GSI (Geological Strength Index): a ponte para o critério de Hoek-Brown" + "SMR (Slope Mass Rating): RMR adaptado para taludes" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: MECROCHA-M05-A06-RMR-001
    claim: "O sistema RMR de Bieniawski (versão de 1989) soma pontuações de cinco parâmetros (resistência da rocha intacta, RQD, espaçamento de descontinuidades, condição de descontinuidades e água subterrânea) numa escala de 0 a 100, ajustada por um fator de correção de orientação, resultando em cinco classes de maciço (I a V)."
    risk: fato
    source: "Bieniawski 1989"
  - claim_id: MECROCHA-M05-A06-Q-002
    claim: "O sistema Q de Barton, Lien e Lunde (1974) calcula a qualidade do maciço como Q=(RQD/Jn)×(Jr/Ja)×(Jw/SRF), numa escala logarítmica de aproximadamente 0,001 a 1.000, usada para dimensionar suporte de escavações subterrâneas via dimensão equivalente (De) e o fator ESR."
    risk: fato
    source: "Barton, Lien & Lunde 1974"
  - claim_id: MECROCHA-M05-A06-GSI-003
    claim: "O GSI (Geological Strength Index), introduzido por Hoek em 1994, é um índice qualitativo baseado em estrutura do maciço e condição das superfícies de descontinuidade, convertido em parâmetros mb, s e a do critério de Hoek-Brown generalizado por relações empíricas publicadas por Hoek, Carranza-Torres e Corkum (2002)."
    risk: fato
    source: "Hoek 1994; Hoek, Carranza-Torres & Corkum 2002"
  - claim_id: MECROCHA-M05-A06-SMR-004
    claim: "O SMR (Slope Mass Rating), proposto por Romana em 1985, adapta o RMR básico para taludes somando quatro fatores de ajuste (F1 a F4) calibrados para a relação geométrica entre a descontinuidade crítica e a face do talude, cobrindo os modos de ruptura planar, em cunha e por tombamento."
    risk: fato
    source: "Romana 1985"
-->
