# Aula 01: Tensão e deformação em rochas: estado de tensão, tensões principais e círculo de Mohr

**ID:** geologia-avancado-m05-a01
**Módulo:** [[05-mecanica-de-rochas-modulo|Módulo 05 — Mecânica de rochas]]
**Duração estimada:** ~28 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** definir o estado de tensão e de deformação num ponto do maciço rochoso, determinar tensões principais a partir de componentes num sistema de eixos arbitrário e construir e interpretar o círculo de Mohr em 2D e 3D.
**Pré-requisito:** álgebra vetorial e trigonometria básicas; nenhum conceito específico do Módulo 01 é usado diretamente nesta aula — o Módulo 01 funciona aqui como pré-requisito curricular (fundamentos de geologia aplicada), não como base conceitual direta.

## Antes de começar, você precisa saber

- O que é uma força distribuída sobre uma área (pressão/tensão como força por unidade de área) e a diferença entre um escalar, um vetor e um tensor de segunda ordem, em nível intuitivo.
- Trigonometria: seno, cosseno e a identidade do ângulo duplo (cos 2θ, sen 2θ), usadas diretamente na dedução do círculo de Mohr.

## Conteúdo

### O que é tensão num ponto de um maciço rochoso

Tensão é a intensidade da força interna que um corpo transmite através de um plano imaginário em seu interior, por unidade de área. Num ponto qualquer de uma rocha submetida a um carregamento (peso das rochas sobrejacentes, forças tectônicas, escavação nas proximidades), a tensão não é um número único: depende da **orientação do plano** através do qual você "corta" o corpo para medi-la. Por isso, o estado de tensão completo num ponto é descrito por um **tensor**, não por um escalar nem por um vetor simples.

Em três dimensões, o tensor de tensões tem nove componentes, organizadas numa matriz 3×3, mas a simetria do tensor (τxy = τyx, τyz = τzy, τxz = τzx, uma consequência do equilíbrio de momentos num elemento infinitesimal) reduz o número de componentes independentes a seis: três **tensões normais** (σx, σy, σz — perpendiculares às faces de um cubo elementar orientado segundo os eixos x, y, z) e três **tensões cisalhantes** (τxy, τyz, τxz — paralelas às faces).

> [!important] Convenção de sinais em mecânica das rochas
> Diferente da convenção usual da mecânica dos sólidos e da engenharia estrutural (onde tração é positiva), a mecânica das rochas e a mecânica dos solos adotam **compressão positiva**. A escolha é prática: no maciço rochoso e no solo, o estado de tensão de interesse é quase sempre compressivo (peso de rocha sobrejacente, confinamento), e tratar esse caso comum como positivo simplifica a notação. Um sinal negativo, nessa convenção, indica tração — situação real, mas normalmente restrita a zonas muito específicas (topo de uma escavação em abóbada mal dimensionada, borda de uma descontinuidade aberta).

### Tensões principais: os planos onde não há cisalhamento

Para qualquer estado de tensão num ponto, existe um sistema de três eixos ortogonais entre si — únicos, a menos de casos degenerados de simetria — sobre cujos planos perpendiculares a tensão cisalhante é nula. As tensões normais que atuam nesses planos são as **tensões principais**, denotadas σ1 ≥ σ2 ≥ σ3 (tensão principal maior, intermediária e menor, respeitando a convenção de compressão positiva). Encontrar as tensões principais é, matematicamente, encontrar os autovalores do tensor de tensões; os autovalores correspondentes definem as **direções principais**.

Essa redução é o que torna o estado de tensão tratável na prática: em vez de lidar com seis componentes arbitrárias, basta conhecer três números (σ1, σ2, σ3) e a orientação dos três eixos principais para reconstruir a tensão em qualquer plano que passe pelo ponto. Em geologia estrutural e em mecânica das rochas aplicada, é comum simplificar ainda mais, tratando o problema em duas dimensões (um plano vertical contendo a direção de maior interesse, por exemplo perpendicular a um talude ou a uma galeria) — o que reduz o problema a duas tensões principais, σ1 e σ3, no plano analisado.

### O círculo de Mohr em 2D: construção e leitura

O **círculo de Mohr** é uma construção gráfica que representa todos os pares possíveis de tensão normal (σ) e tensão cisalhante (τ) que atuam nos planos que passam por um ponto, para um estado de tensão bidimensional. Dado um estado de tensão conhecido em dois eixos ortogonais x e y (σx, σy, τxy), a tensão normal e cisalhante num plano cuja normal faz um ângulo θ com o eixo x é:

σθ = (σx + σy)/2 + (σx − σy)/2 · cos 2θ + τxy · sen 2θ

τθ = −(σx − σy)/2 · sen 2θ + τxy · cos 2θ

Essas duas equações são, geometricamente, a equação paramétrica de uma circunferência no plano (σ, τ), com:

- **Centro:** C = (σx + σy)/2, sobre o eixo σ (τ = 0).
- **Raio:** R = √[((σx − σy)/2)² + τxy²]

As tensões principais são os pontos onde o círculo cruza o eixo σ (τ = 0): σ1 = C + R e σ3 = C − R. A tensão cisalhante máxima possível em qualquer plano, τmáx = R = (σ1 − σ3)/2, ocorre no topo e na base do círculo — ou seja, em planos a 45° das direções principais, nunca nas próprias direções principais (onde, por definição, o cisalhamento é zero).

> [!warning] O ângulo no círculo de Mohr é o dobro do ângulo físico
> Um plano físico girado de um ângulo θ em relação ao eixo x corresponde, no círculo de Mohr, a um giro de 2θ a partir do ponto (σx, τxy). Esquecer esse fator 2 é o erro de leitura mais comum ao usar o círculo pela primeira vez — um plano a 30° no maciço aparece a 60° no gráfico.

O valor prático do círculo de Mohr não é apenas visualizar — é permitir, com régua e compasso ou algebricamente, obter rapidamente: (1) as tensões principais a partir de tensões medidas em eixos arbitrários; (2) a tensão normal e cisalhante em qualquer plano de interesse (por exemplo, o plano de uma descontinuidade com orientação conhecida); e (3) — como será usado já na Aula 03 — a comparação direta entre o estado de tensão e um critério de ruptura, também representável no mesmo diagrama (σ, τ).

### Extensão ao espaço: o diagrama de Mohr em 3D

Em três dimensões, com três tensões principais σ1 ≥ σ2 ≥ σ3, o estado de tensão em planos de orientação arbitrária não cai sobre uma única circunferência, mas numa região do plano (σ, τ) limitada por **três círculos de Mohr**, construídos par a par a partir das três tensões principais:

- Círculo maior: diâmetro σ1 − σ3 (o par de tensões principais extremas).
- Círculo intermediário: diâmetro σ1 − σ2.
- Círculo menor: diâmetro σ2 − σ3.

Os três círculos são tangentes dois a dois no eixo σ (nos pontos σ1, σ2 e σ3) e a combinação (σ, τ) de qualquer plano de orientação arbitrária no espaço cai necessariamente dentro da área sombreada entre o círculo maior e os dois menores — nunca fora dela e nunca dentro dos dois círculos menores. Essa construção mostra visualmente um resultado importante: a tensão cisalhante máxima absoluta em qualquer plano que passe pelo ponto é sempre τmáx = (σ1 − σ3)/2 — a tensão intermediária σ2 não altera esse valor máximo, embora influencie a forma da região de tensões possíveis e, como será visto na Aula 03, tenha um papel debatido nos critérios de ruptura.

### Deformação: a resposta do material ao estado de tensão

**Deformação** (*strain*) descreve a mudança relativa de forma e volume de um corpo submetido a tensão — deslocamentos relativos entre pontos internos, normalizados pela distância original, de modo a serem uma grandeza adimensional (ou expressa em %, ou microdeformações, με = 10⁻⁶). Assim como a tensão, a deformação num ponto também é um tensor de segunda ordem, com componentes normais (εx, εy, εz — alongamento ou encurtamento relativo ao longo de cada eixo) e cisalhantes (γxy, γyz, γxz — distorção angular), e também admite direções principais e um círculo de Mohr análogo ao de tensão, com a mesma regra do ângulo duplo.

Para um material **elástico linear e isótropo** — a idealização de primeira aproximação para rocha intacta em baixos níveis de tensão, antes de aproximar-se da ruptura — tensão e deformação relacionam-se pela lei de Hooke generalizada, caracterizada por apenas duas constantes elásticas independentes: o **módulo de Young (E)**, que relaciona tensão e deformação axial num ensaio uniaxial, e o **coeficiente de Poisson (ν)**, que relaciona a deformação lateral (expansão) à deformação axial (encurtamento) sob compressão uniaxial. Essas duas constantes — e os ensaios de laboratório que as medem — são o tema central da Aula 02; aqui, o essencial é reconhecer que o círculo de Mohr de tensão e o círculo de Mohr de deformação descrevem o mesmo fenômeno físico observado de duas maneiras (causa e resposta), e que ambos compartilham a mesma lógica geométrica de construção.

## Exemplo trabalhado

**Situação:** um afloramento rochoso próximo a uma futura escavação é instrumentado, e a análise indica, num plano vertical de interesse, σx = 40 MPa, σy = 15 MPa e τxy = 10 MPa (eixo x horizontal, y vertical). Determine as tensões principais σ1 e σ3, a orientação do plano principal maior em relação ao eixo x, e a tensão cisalhante máxima nesse plano.

**Resolução:**

Centro do círculo: C = (σx + σy)/2 = (40 + 15)/2 = 27,5 MPa.

Raio: R = √[((σx − σy)/2)² + τxy²] = √[((40−15)/2)² + 10²] = √[12,5² + 10²] = √(156,25 + 100) = √256,25 ≈ 16,0 MPa.

Tensões principais: σ1 = C + R ≈ 27,5 + 16,0 = 43,5 MPa; σ3 = C − R ≈ 27,5 − 16,0 = 11,5 MPa.

Orientação: tan 2θp = 2τxy / (σx − σy) = 2×10 / (40−15) = 20/25 = 0,8 → 2θp ≈ 38,7° → θp ≈ 19,3° (ângulo, medido a partir do eixo x, da direção de σ1).

Tensão cisalhante máxima: τmáx = R ≈ 16,0 MPa, atuando em planos a 45° da direção principal (ou seja, a θp + 45° ≈ 64,3° do eixo x).

**Interpretação:** a tensão principal maior (43,5 MPa) não está alinhada com nenhum dos eixos de medição originais (x ou y) — está a apenas 19,3° do eixo x, mas isso já é suficiente para que a leitura direta de σx como "a maior tensão" fosse um erro de quase 3,5 MPa. Esse desalinhamento entre eixos de medição de campo e direções principais reais é a norma, não a exceção, e é exatamente por isso que o círculo de Mohr — e não a leitura direta dos componentes medidos — é a ferramenta correta para obter σ1 e σ3.

## Erros comuns

- **Ler a maior tensão medida diretamente como σ1**, ignorando que as tensões principais só coincidem com os eixos de medição quando, por coincidência, τxy = 0 nesses eixos.
- **Esquecer o fator 2 na relação entre o ângulo físico do plano e o ângulo no círculo de Mohr**, invertendo ou duplicando incorretamente a orientação da direção principal.
- **Tratar o círculo de Mohr 3D como um único círculo**, ignorando σ2 e concluindo — corretamente por coincidência, mas por raciocínio errado — que qualquer plano cai sobre "o" círculo, quando na verdade cai na região entre os três círculos, salvo para os planos particulares que contêm uma das direções principais.
- **Confundir a convenção de sinais** ao importar fórmulas de um livro de mecânica dos sólidos clássica (tração positiva) sem adaptar para a convenção de compressão positiva usual em mecânica das rochas, invertendo os sinais de toda a análise.

## O que não concluir

- **Que a tensão cisalhante máxima ocorre no mesmo plano que a tensão normal máxima.** São planos diferentes: a tensão normal máxima (σ1) ocorre num plano principal, onde o cisalhamento é zero por definição; a tensão cisalhante máxima ocorre num plano a 45° das direções principais, onde a tensão normal é a média (σ1+σ3)/2, nem máxima nem mínima.
- **Que o comportamento elástico linear (lei de Hooke) descreve a rocha em qualquer nível de tensão.** É uma boa aproximação para tensões moderadas, abaixo do limiar de dano; próximo da ruptura, o comportamento se torna não linear — tema retomado nas Aulas 02 e 03.

## Recap relâmpago

- O estado de tensão num ponto é um tensor com seis componentes independentes em 3D (três normais, três cisalhantes); em mecânica das rochas, a convenção usual trata compressão como positiva.
- Tensões principais (σ1 ≥ σ2 ≥ σ3) são as tensões normais nos três planos ortogonais onde a tensão cisalhante é nula — encontradas, em 2D, pelo centro e raio do círculo de Mohr: C = (σx+σy)/2, R = √[((σx−σy)/2)²+τxy²].
- No círculo de Mohr, um giro físico de θ no plano corresponde a um giro de 2θ no diagrama; a tensão cisalhante máxima (τmáx = R) ocorre a 45° das direções principais, não nelas.
- Em 3D, o estado de tensão em qualquer plano cai na região entre três círculos de Mohr construídos a partir de σ1, σ2 e σ3; a tensão cisalhante máxima absoluta é sempre (σ1−σ3)/2.
- Deformação é a resposta do material ao estado de tensão, também descrita por um tensor com lógica geométrica análoga (círculo de Mohr de deformação); a relação entre os dois, no regime elástico linear, depende de apenas duas constantes — módulo de Young e coeficiente de Poisson — tema da Aula 02.

## Próxima aula

[[05-mecanica-de-rochas-aula-02-propriedades-fisicas-comportamento-reologico|Aula 02 — Propriedades físicas e comportamento reológico das rochas; ensaios de laboratório]]

## Anterior

Primeira aula do módulo. Pressupõe o [[01-hidrogeologia-recursos-hidricos/01-hidrogeologia-recursos-hidricos-modulo|Módulo 01]] concluído (pré-requisito curricular).

## Fontes

- Definição do tensor de tensões, tensões principais e construção do círculo de Mohr em 2D e 3D: Jaeger, J. C., Cook, N. G. W. & Zimmerman, R. W. (2007), *Fundamentals of Rock Mechanics*, 4ª ed., Blackwell, cap. 2–3.
- Convenção de sinais (compressão positiva) e aplicação do círculo de Mohr em problemas de engenharia de rochas: Goodman, R. E. (1989), *Introduction to Rock Mechanics*, 2ª ed., Wiley, cap. 3.
- Relação tensão-deformação elástica linear e constantes elásticas: Hoek, E. & Bray, J. W. (1981), *Rock Slope Engineering*, 3ª ed., Institution of Mining and Metallurgy, cap. 4.

<!--
nivel: avancado
palavras_corpo: ~1750

mapa_objetivo_secao:
  geologia-avancado-m05-oa01: "O que é tensão num ponto de um maciço rochoso" + "Tensões principais: os planos onde não há cisalhamento" + "O círculo de Mohr em 2D: construção e leitura" + "Extensão ao espaço: o diagrama de Mohr em 3D" + "Deformação: a resposta do material ao estado de tensão" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: MECROCHA-M05-A01-TENSOR-001
    claim: "O estado de tensão num ponto é descrito por um tensor simétrico de segunda ordem com seis componentes independentes em três dimensões (três normais e três cisalhantes)."
    risk: fato
    source: "Jaeger, Cook & Zimmerman 2007, cap. 2"
  - claim_id: MECROCHA-M05-A01-CONVENCAO-002
    claim: "A mecânica das rochas e a mecânica dos solos adotam convencionalmente compressão como tensão positiva, ao contrário da convenção de tração positiva usual na mecânica dos sólidos clássica."
    risk: convenção
    source: "Goodman 1989, cap. 3; uso consolidado na literatura de mecânica das rochas"
  - claim_id: MECROCHA-M05-A01-MOHR2D-003
    claim: "O círculo de Mohr 2D tem centro C=(σx+σy)/2 e raio R=√[((σx−σy)/2)²+τxy²], com as tensões principais dadas por σ1=C+R e σ3=C−R, e um giro físico de θ no plano correspondendo a um giro de 2θ no diagrama."
    risk: fato
    source: "Jaeger, Cook & Zimmerman 2007, cap. 2"
  - claim_id: MECROCHA-M05-A01-MOHR3D-004
    claim: "Em três dimensões, o estado de tensão em qualquer plano de orientação arbitrária cai na região do plano (σ,τ) delimitada por três círculos de Mohr construídos a partir de σ1, σ2 e σ3, e a tensão cisalhante máxima absoluta é sempre (σ1−σ3)/2, independente de σ2."
    risk: fato
    source: "Jaeger, Cook & Zimmerman 2007, cap. 2-3"
  - claim_id: MECROCHA-M05-A01-ELASTICIDADE-005
    claim: "Para um material elástico linear e isótropo, a relação entre tensão e deformação é totalmente caracterizada por duas constantes elásticas independentes: o módulo de Young e o coeficiente de Poisson."
    risk: fato
    source: "Hoek & Bray 1981, cap. 4"
-->
