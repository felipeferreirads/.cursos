# Aula 03: Critérios de ruptura aplicáveis às rochas: Mohr-Coulomb, Griffith e Hoek-Brown

**ID:** geologia-avancado-m05-a03
**Módulo:** [[05-mecanica-de-rochas-modulo|Módulo 05 — Mecânica de rochas]]
**Duração estimada:** ~29 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** aplicar os critérios de ruptura de Mohr-Coulomb, Griffith e Hoek-Brown para prever a resistência de uma rocha sob um dado estado de tensão, e reconhecer o domínio de validade e as limitações de cada um.
**Pré-requisito:** círculo de Mohr e tensões principais (Aula 01); envelope de ruptura obtido por ensaio triaxial e resistência à tração (Aula 02).

## Antes de começar, você precisa saber

- O círculo de Mohr representa o par (σ, τ) de qualquer plano; um critério de ruptura é uma curva no mesmo diagrama (σ, τ) que separa estados de tensão estáveis de estados que causam ruptura (Aula 01).
- O envelope de ruptura é construído empiricamente a partir de ensaios triaxiais em diferentes confinamentos, e a resistência à tração é obtida pelo ensaio brasileiro (Aula 02).

## Conteúdo

### O que é um critério de ruptura e como ele se conecta ao círculo de Mohr

Um **critério de ruptura** é uma função matemática que estabelece a combinação de tensões (normal e cisalhante, ou tensões principais) na qual um material rompe. Representado no diagrama (σ, τ), um critério de ruptura é uma curva — o **envelope de ruptura** — tal que qualquer círculo de Mohr **tangente** a essa curva representa um estado de tensão na iminência da ruptura; um círculo que não alcança a curva representa um estado estável; e um círculo que a ultrapassaria seria fisicamente inalcançável, porque a ruptura já teria ocorrido antes.

Essa é a ponte direta entre a Aula 01 (o círculo de Mohr descreve o estado de tensão) e esta aula (o critério de ruptura decide se aquele estado é seguro): dado um envelope de ruptura já calibrado para uma rocha, basta desenhar o círculo de Mohr do estado de tensão de interesse e verificar se ele toca, cruza ou fica abaixo da curva.

### Mohr-Coulomb: o critério linear clássico

O critério de **Mohr-Coulomb** postula que a ruptura por cisalhamento ocorre quando a tensão cisalhante num plano atinge um valor que depende linearmente da tensão normal naquele mesmo plano:

τ = c + σn · tan φ

onde **c** é a **coesão** (resistência ao cisalhamento na ausência de tensão normal — um parâmetro do material, não necessariamente com significado físico microscópico direto, mas útil como parâmetro de ajuste) e **φ** é o **ângulo de atrito interno** (a taxa de aumento da resistência ao cisalhamento com o aumento do confinamento normal). Reescrito em termos de tensões principais, o critério equivale a uma reta no espaço (σ1, σ3):

σ1 = σc + σ3 · tan²(45° + φ/2)

onde σc é a resistência à compressão uniaxial (σ3 = 0) prevista pelo critério.

Mohr-Coulomb é amplamente usado por sua simplicidade — dois parâmetros, ajuste direto a partir de ensaios triaxiais em poucos níveis de confinamento — e por ser o critério padrão em mecânica dos solos (retomado no Módulo 06). Em mecânica das rochas, porém, tem uma limitação bem documentada: o envelope de ruptura real de rochas, obtido experimentalmente, é **côncavo em relação ao eixo σ** (a resistência ao cisalhamento cresce cada vez mais devagar à medida que o confinamento aumenta), enquanto Mohr-Coulomb, sendo uma reta, superestima sistematicamente a resistência em confinamentos altos e pode subestimá-la em confinamentos baixos, dependendo de onde os dados foram ajustados.

> [!warning] Mohr-Coulomb extrapolado para tração dá um resultado fisicamente errado
> A reta de Mohr-Coulomb, extrapolada para σ3 negativo (tração), cruza o eixo σ num valor de resistência à tração maior, em módulo, do que a resistência à tração real medida por ensaio brasileiro — porque a rocha rompe por um mecanismo de propagação de fissuras em tração (Griffith, a seguir), não pelo mesmo mecanismo de cisalhamento por atrito que governa a compressão. Por isso, aplicações práticas de Mohr-Coulomb em rocha frequentemente impõem um "corte de tração" (*tension cutoff*) arbitrário, truncando a reta antes que ela alcance valores de tração irreais.

### Griffith: ruptura a partir da propagação de microfissuras

O critério de **Griffith** (formulado originalmente por A. A. Griffith em 1921 para vidro e estendido à mecânica das rochas por McClintock & Walsh, entre outros) parte de um modelo físico diferente: a rocha contém microfissuras elípticas pré-existentes orientadas aleatoriamente, e a ruptura ocorre quando a concentração de tensão de tração na ponta de uma dessas microfissuras — mesmo sob um campo de tensão macroscopicamente compressivo — atinge a resistência de coesão molecular do material. O resultado matemático (para o critério de Griffith original, 2D) é uma relação **parabólica**, não linear, entre σ1 e σ3:

(σ1 − σ3)² = 8·σt·(σ1 + σ3), válida para σ1 + 3σ3 > 0

onde σt é a resistência à tração uniaxial. Uma previsão notável do critério de Griffith original é que a razão entre a resistência à compressão uniaxial e a resistência à tração deveria ser exatamente 8 — um valor que a maioria das rochas reais excede consideravelmente (razões de 10 a 20, ou mais, são comuns), o que levou a versões **modificadas** do critério (incorporando o fechamento por atrito das faces da microfissura sob compressão, o que reduz a concentração de tensão efetiva) para melhor ajuste aos dados experimentais.

O valor do critério de Griffith não está tanto em seu uso direto de projeto — Hoek-Brown, a seguir, é preferido na prática — mas em fornecer o **fundamento físico** (propagação de microfissuras) para por que o envelope de ruptura real das rochas é côncavo: a mesma micromecânica de fissuras que explica a fragilidade em tração explica também por que o ganho de resistência com o confinamento desacelera em altas pressões, uma vez que o confinamento inibe progressivamente a abertura das fissuras.

### Hoek-Brown: o critério empírico não linear de referência em mecânica das rochas

O critério de **Hoek-Brown**, proposto por Evert Hoek e E. T. Brown em 1980 e revisado em versões sucessivas (1988, 1997, 2002 — esta última incorporando o Índice de Resistência Geológica, GSI, tema da Aula 06), é hoje o critério de ruptura mais usado em projeto de engenharia de rochas, precisamente por combinar uma forma **não linear** (compatível com o comportamento real observado) com uma calibração direta a partir de propriedades relativamente acessíveis. Na forma generalizada (2002), para o maciço rochoso:

σ1' = σ3' + σci · (mb · σ3'/σci + s)^a

onde σ1' e σ3' são as tensões principais efetivas na ruptura, σci é a resistência à compressão uniaxial da rocha intacta, e mb, s e a são parâmetros adimensionais que dependem da qualidade do maciço (via GSI, perturbação por desmonte, e o parâmetro mi característico da litologia — Aula 06 detalha como esses parâmetros são obtidos a partir da classificação GSI). Para a **rocha intacta** (sem influência de descontinuidades), o critério se reduz à forma original de 1980, com s = 1 e mb = mi:

σ1 = σ3 + σci · (mi · σ3/σci + 1)^0,5

O parâmetro **mi** é uma constante empírica característica do tipo litológico (valores tabelados a partir de extensos bancos de dados de ensaios triaxiais — tipicamente baixo, ~4–7, para rochas carbonáticas de granulação fina, e mais alto, ~25–33, para granitos e riolitos), refletindo o quanto a resistência de uma rocha específica responde ao aumento de confinamento.

> [!tip] Por que Hoek-Brown dominou a prática, e Mohr-Coulomb não desapareceu
> Hoek-Brown descreve melhor o comportamento não linear observado experimentalmente e se conecta diretamente às classificações de maciço (Aula 06), tornando-se o critério de referência para projeto em rocha. Mas muitos softwares de análise de estabilidade (inclusive de equilíbrio limite, Aula 07) ainda trabalham nativamente com parâmetros de Mohr-Coulomb (c, φ) — por isso, é prática comum **ajustar** um par equivalente (c, φ) de Mohr-Coulomb, válido apenas na faixa de tensão de interesse do problema específico, a partir do envelope de Hoek-Brown calculado para aquele maciço. Esse par equivalente não deve ser extrapolado para uma faixa de tensão muito diferente daquela em que foi ajustado, sob pena de reintroduzir o erro de linearização que o Hoek-Brown foi criado para evitar.

## Exemplo trabalhado

**Situação:** uma rocha intacta tem σci = 100 MPa e mi = 15 (valor típico de um arenito de granulação média). Calcule, pelo critério de Hoek-Brown original (rocha intacta), a tensão principal maior na ruptura (σ1) para um confinamento de σ3 = 5 MPa, e compare com a previsão de um critério de Mohr-Coulomb ajustado com c = 18 MPa e φ = 35°, calibrado a partir do mesmo par de ensaios.

**Resolução (Hoek-Brown):**

σ1 = σ3 + σci·(mi·σ3/σci + 1)^0,5 = 5 + 100×(15×5/100 + 1)^0,5 = 5 + 100×(0,75+1)^0,5 = 5 + 100×√1,75 ≈ 5 + 100×1,3229 ≈ 5 + 132,3 = 137,3 MPa.

**Resolução (Mohr-Coulomb):**

σ1 = σc + σ3·tan²(45°+φ/2), com σc = 2c·tan(45°+φ/2).

tan(45°+17,5°) = tan(62,5°) ≈ 1,921. tan² ≈ 3,690.

σc = 2×18×1,921 ≈ 69,2 MPa.

σ1 = 69,2 + 5×3,690 ≈ 69,2 + 18,45 ≈ 87,6 MPa.

**Interpretação:** os dois critérios, ajustados a partir dos mesmos dados experimentais (por hipótese, neste exemplo), divergem consideravelmente em σ3 = 5 MPa (137,3 MPa contra 87,6 MPa) porque a reta de Mohr-Coulomb, calibrada para se ajustar bem numa faixa de confinamento mais alta, subestima a resistência em confinamentos baixos, onde o envelope real (curvo, tipo Hoek-Brown) sobe mais rapidamente a partir de σci. Esse tipo de divergência — não um erro de cálculo, mas uma consequência da forma funcional escolhida — é exatamente por que um par (c, φ) de Mohr-Coulomb só deve ser aplicado dentro da faixa de tensão em que foi calibrado.

## Erros comuns

- **Usar um único par (c, φ) de Mohr-Coulomb para toda a faixa de tensão de um problema**, quando o maciço já foi caracterizado por Hoek-Brown numa faixa de tensão mais estreita e específica do problema real (por exemplo, tensões baixas próximas à superfície de um talude raso).
- **Aplicar o critério de Griffith original (razão compressão/tração = 8) como previsão quantitativa direta**, ignorando que a maioria das rochas reais exibe razões maiores, e que versões modificadas do critério existem justamente para corrigir essa discrepância.
- **Confundir os parâmetros de Hoek-Brown para rocha intacta (s=1, mb=mi) com os parâmetros para maciço rochoso (s<1, mb<mi, dependentes do GSI)** — aplicar o critério de rocha intacta a um maciço fraturado superestima grosseiramente sua resistência (tema retomado na Aula 06).
- **Tratar c e φ como propriedades físicas medíveis diretamente**, como se fossem análogas a densidade ou porosidade — são parâmetros de ajuste de um modelo linear a um comportamento real não linear, e seu valor numérico depende da faixa de tensão usada na calibração.

## O que não concluir

- **Que Hoek-Brown é "mais correto" e Mohr-Coulomb deveria ser abandonado.** Mohr-Coulomb permanece amplamente usado — inclusive dentro de análises que partem de um Hoek-Brown calibrado — porque muitas ferramentas de cálculo de equilíbrio limite (Aula 07) e boa parte da mecânica dos solos (Módulo 06) são construídas nativamente sobre esse par de parâmetros; a escolha certa depende da ferramenta e da faixa de tensão do problema, não de um critério ser universalmente "melhor".
- **Que o critério de Griffith prevê corretamente a ruptura em compressão triaxial de qualquer rocha.** Foi desenvolvido primariamente para explicar a ruptura em tração e a razão compressão/tração; seu papel principal hoje é conceitual (explicar por que o envelope real é côncavo), não como ferramenta de dimensionamento direto.

## Recap relâmpago

- Um critério de ruptura é uma curva no diagrama (σ, τ); um círculo de Mohr tangente a essa curva representa um estado de tensão na iminência da ruptura.
- Mohr-Coulomb (τ = c + σn·tanφ) é linear, simples de calibrar, mas superestima a resistência em altos confinamentos e prevê uma resistência à tração irreal se extrapolado sem corte de tração.
- Griffith explica a ruptura pela propagação de microfissuras pré-existentes, prevendo uma relação parabólica entre σ1 e σ3 e uma razão teórica compressão/tração de 8 (na prática, geralmente excedida) — seu valor é sobretudo explicativo do formato côncavo do envelope real.
- Hoek-Brown (σ1' = σ3' + σci·(mb·σ3'/σci + s)^a) é o critério empírico não linear de referência em engenharia de rochas, calibrado a partir de σci, do parâmetro litológico mi e, para maciço rochoso, do GSI (Aula 06); para rocha intacta, reduz-se à forma original de 1980 com s=1 e mb=mi.
- Um par (c, φ) de Mohr-Coulomb pode ser ajustado a partir de um envelope de Hoek-Brown para uso em ferramentas que exigem parâmetros lineares, mas só é válido na faixa de tensão em que foi calibrado.

## Próxima aula

[[05-mecanica-de-rochas-aula-04-descontinuidades-geometria-resistencia-permeabilidade|Aula 04 — Descontinuidades: geometria, resistência ao cisalhamento e permeabilidade do maciço]]

## Anterior

[[05-mecanica-de-rochas-aula-02-propriedades-fisicas-comportamento-reologico|Aula 02 — Propriedades físicas e comportamento reológico das rochas; ensaios de laboratório]]

## Fontes

- Critério de Mohr-Coulomb aplicado a rochas e limitações em altos confinamentos: Jaeger, J. C., Cook, N. G. W. & Zimmerman, R. W. (2007), *Fundamentals of Rock Mechanics*, 4ª ed., Blackwell, cap. 4.
- Critério de Griffith original e modificado, propagação de microfissuras: Jaeger, Cook & Zimmerman (2007), cap. 4; Griffith, A. A. (1921), "The phenomena of rupture and flow in solids", *Philosophical Transactions of the Royal Society A*, 221.
- Critério de Hoek-Brown original, generalizado e parâmetros mi, mb, s, a: Hoek, E. & Brown, E. T. (1980), "Empirical strength criterion for rock masses", *Journal of the Geotechnical Engineering Division*, ASCE, 106(9); Hoek, E., Carranza-Torres, C. & Corkum, B. (2002), "Hoek-Brown failure criterion — 2002 edition", *Proceedings of NARMS-TAC Conference*, Toronto.
- Valores tabelados do parâmetro mi por litologia: Hoek, E. (2007), *Practical Rock Engineering* (nota técnica online do autor), cap. 11; Marinos, P. & Hoek, E. (2000).

<!--
nivel: avancado
palavras_corpo: ~1900

mapa_objetivo_secao:
  geologia-avancado-m05-oa02: "O que é um critério de ruptura e como ele se conecta ao círculo de Mohr" + "Mohr-Coulomb: o critério linear clássico" + "Griffith: ruptura a partir da propagação de microfissuras" + "Hoek-Brown: o critério empírico não linear de referência em mecânica das rochas" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: MECROCHA-M05-A03-MOHRCOULOMB-001
    claim: "O critério de Mohr-Coulomb (τ = c + σn·tanφ) é linear e, aplicado a rochas, superestima sistematicamente a resistência em confinamentos altos porque o envelope de ruptura real das rochas é côncavo em relação ao eixo de tensão normal."
    risk: fato
    source: "Jaeger, Cook & Zimmerman 2007, cap. 4"
  - claim_id: MECROCHA-M05-A03-GRIFFITH-002
    claim: "O critério de Griffith original prevê uma relação parabólica entre σ1 e σ3, com razão teórica entre resistência à compressão uniaxial e resistência à tração igual a 8, valor tipicamente excedido pelas rochas reais, o que motivou versões modificadas do critério."
    risk: fato
    source: "Griffith 1921; Jaeger, Cook & Zimmerman 2007, cap. 4"
  - claim_id: MECROCHA-M05-A03-HOEKBROWN-003
    claim: "O critério de Hoek-Brown generalizado (2002) tem a forma σ1'=σ3'+σci·(mb·σ3'/σci+s)^a, reduzindo-se para rocha intacta à forma original de 1980 com s=1 e mb=mi, onde mi é um parâmetro empírico dependente da litologia."
    risk: fato
    source: "Hoek & Brown 1980; Hoek, Carranza-Torres & Corkum 2002"
  - claim_id: MECROCHA-M05-A03-EQUIVALENCIA-004
    claim: "É prática comum de engenharia ajustar um par equivalente de parâmetros de Mohr-Coulomb (c, φ) a partir de um envelope de Hoek-Brown calculado para uma faixa de tensão específica do problema, sendo esse par válido apenas dentro daquela faixa."
    risk: prática de engenharia
    source: "Hoek, Carranza-Torres & Corkum 2002; prática consolidada de softwares de estabilidade (ex.: RocScience)"
-->
