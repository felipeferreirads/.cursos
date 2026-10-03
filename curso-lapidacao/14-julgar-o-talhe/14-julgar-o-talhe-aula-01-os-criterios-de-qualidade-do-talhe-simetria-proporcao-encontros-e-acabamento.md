# Aula 01: Os critérios de qualidade do talhe — simetria, proporção, encontro de facetas e acabamento

**ID:** lapidacao-m14-a01
**Módulo:** [[14-julgar-o-talhe-modulo|Módulo 14]] — Julgar um talhe pronto
**Duração estimada:** ~29 min
**Objetivo:** enumerar os critérios de qualidade de talhe — simetria, proporção, encontro de facetas, acabamento de polimento — e explicar o que cada um mede.
**Pré-requisito:** [[06-cabochao-aula-04-cinta-e-base-onde-o-cabochao-mais-se-estraga|Módulo 06, aula 04]] deste curso (contorno e cinta como interface mecânica); [[07-esfera-e-torneadas-aula-01-por-que-a-esfera-converge-do-cubo-ao-poliedro-a-esfera|Módulo 07, aula 01]] deste curso (a esfera como convergência de simetria); [[09-geometria-e-diagramas-aula-04-meetpoint-faceting-a-logica-do-ponto-de-encontro|Módulo 09, aula 04]] deste curso (a lógica do ponto de encontro); [[10-familias-de-talhe-aula-01-o-talhe-brilhante-facetas-triangulares-e-a-linhagem-do-brilhante-redondo|Módulo 10, aula 01]] deste curso (simetria de rotação do contorno redondo); [[12-fancy-cutting-aula-04-talhe-de-precisao-e-talhes-opticos-simetria-extrema-e-padrao-de-reflexao|Módulo 12, aula 04]] deste curso (simetria extrema do talhe de precisão).

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **simetria de rotação** (*n-fold*) | a pedra parece igual a si mesma depois de girada de uma fração de volta; *n* é quantas vezes isso acontece numa volta completa. |
| **simetria de reflexão** (bilateral) | a metade de um lado do contorno é a imagem espelhada da metade do outro lado, em torno de um eixo. |
| **proporção** | a relação entre as dimensões da pedra — altura, largura, profundidade de pavilhão — expressa como razão ou porcentagem, não como valor absoluto. |
| **encontro de facetas** | o critério de que facetas vizinhas planejadas para se tocar num ponto realmente se toquem ali, sem sobra visível. |
| **meetpoint** | o ponto único onde três ou mais facetas se encontram quando a execução fecha certo. |
| **meetline** | a linha fina (ou pequeno triângulo) que sobra no lugar do meetpoint quando a execução escorrega. |
| **acabamento de polimento** | o estado da superfície já polida — lisa, sem risco, sem resíduo — como critério observável por si, distinto da forma por baixo dela. |

## Antes de começar, você precisa saber

- Do [[10-familias-de-talhe-aula-01-o-talhe-brilhante-facetas-triangulares-e-a-linhagem-do-brilhante-redondo|módulo 10, aula 01]]: o contorno redondo tem simetria de rotação alta, e essa simetria é a razão por trás do arranjo brilhante.
- Do [[09-geometria-e-diagramas-aula-04-meetpoint-faceting-a-logica-do-ponto-de-encontro|módulo 09, aula 04]]: um meetpoint fechado é uma condição visível. E da [[09-geometria-e-diagramas-aula-05-quando-o-meetpoint-nao-fecha-cheater-e-diagnostico|aula 05 do mesmo módulo]]: o encontro que não fecha tem sintomas diferentes conforme a coordenada fora.
- Do [[06-cabochao-aula-04-cinta-e-base-onde-o-cabochao-mais-se-estraga|módulo 06, aula 04]]: contorno, cinta e base são a interface mecânica do cabochão, e um defeito ali se propaga para o resto da pedra.
- Do [[07-esfera-e-torneadas-aula-01-por-que-a-esfera-converge-do-cubo-ao-poliedro-a-esfera|módulo 07, aula 01]]: a esfera é o limite de simetria que um sólido de revolução alcança quando todo raio é igual.

## Ao final você vai conseguir

- `lapidacao-m14-oa01` — Enumerar os critérios de qualidade de talhe — simetria, proporção, encontro de facetas, acabamento de polimento — e explicar o que cada um mede.

## Conteúdo

### Avaliar sem ter feito

Um crítico gastronômico não precisa saber cozinhar o prato para dizer se ele saiu bem: prova, olha o corte da carne, mede o ponto do molho contra um padrão que aprendeu a reconhecer. O curso inteiro, até aqui, ensinou a **fazer** — como cada família de talhe é projetada e por que cada etapa existe. Este módulo muda de posição: a pedra já está pronta, o processo é invisível, e a única coisa disponível para julgar é o resultado. Julgar um talhe pronto não exige saber lapidar; exige saber **o que olhar**. Quatro critérios cobrem a maior parte do que se vê: simetria, proporção, encontro de facetas e acabamento de polimento. Cada um mede algo diferente, e nenhum sozinho decide a qualidade da pedra.

### Simetria — dois tipos, e nem toda família usa os dois

A simetria tem duas formas distintas neste curso, já vistas em separado. A **simetria de rotação** (*n-fold*) é a que o [[09-geometria-e-diagramas-aula-01-o-sistema-de-indice-32-64-77-80-96-dentes|módulo 09]] ligou aos divisores do jogo de índice: a pedra parece igual a si mesma depois de girar 1/*n* de volta. O brilhante redondo do [[10-familias-de-talhe-aula-01-o-talhe-brilhante-facetas-triangulares-e-a-linhagem-do-brilhante-redondo|módulo 10]] tem *n* = 8 — oito setores repetidos a cada 45° —, e não o *n* mais alto que o jogo de índice permitiria; o talhe de precisão do [[12-fancy-cutting-aula-04-talhe-de-precisao-e-talhes-opticos-simetria-extrema-e-padrao-de-reflexao|módulo 12]] leva essa mesma simetria a uma tolerância de execução muito mais apertada. A **simetria de reflexão** (bilateral) é outra coisa: metade do contorno espelha a outra em torno de um eixo — o critério que julga uma pêra, uma marquise ou um coração, contornos que não têm simetria de rotação alta mas devem ter os dois lados equivalentes.

Nem toda família usa as duas. A esfera do [[07-esfera-e-torneadas-aula-01-por-que-a-esfera-converge-do-cubo-ao-poliedro-a-esfera|módulo 07]] é o caso-limite: simetria de rotação em qualquer eixo que passe pelo centro, ao mesmo tempo. O cabochão de contorno oval usa só a reflexão — não tem sentido perguntar seu *n-fold*, porque não repete por rotação. Julgar a simetria errada para a família é o primeiro erro que este critério convida a cometer.

### Proporção — razão, não valor absoluto

Proporção mede a relação entre partes da pedra, sempre como razão ou porcentagem — nunca um milímetro isolado. No cabochão, é a razão de cúpula (altura da cúpula sobre a **menor** dimensão do contorno) que o [[06-cabochao-aula-03-geometria-da-cupula-altura-curvatura-luz-engaste|módulo 06, aula 03]] tratou como o que decide se a luz atravessa ou reflete. No facetado, é a profundidade total como porcentagem do diâmetro e o ângulo de pavilhão em relação ao índice de refração, ambos do [[08-optica-do-facetado-modulo|módulo 08]]. Numa esfera ou num ovo, proporção é a razão entre os dois eixos — 1:1 na esfera perfeita, maior que 1 no ovo, e o [[07-esfera-e-torneadas-aula-04-ovos-obeliscos-e-formas-torneadas|módulo 07, aula 04]] fixou faixas de referência para cada forma.

Proporção erra em dois sentidos, e os dois têm nome no curso: fundo ou raso demais para o índice do material produz janela ou extinção ([[05-leitura-do-bruto-aula-06-janelamento-e-extincao|módulo 05, aula 06]]); e proporção alterada para reter peso — cinta grossa, pavilhão fundo, quilha deslocada — é o assunto do [[10-familias-de-talhe-aula-05-onde-o-peso-se-esconde|módulo 10, aula 05]]. Julgar a proporção, aqui, é comparar o que se vê contra a faixa de referência da família — não contra um número memorizado sem contexto.

### Encontro de facetas — o critério exclusivo do talhe facetado

Cabochão, esfera e forma torneada não têm facetas planas encontrando-se em vértices; o critério de **encontro** simplesmente não se aplica a eles. Ele nasce no facetado, onde o [[09-geometria-e-diagramas-aula-04-meetpoint-faceting-a-logica-do-ponto-de-encontro|módulo 09]] descreveu o **meetpoint**: três ou mais facetas planejadas para se tocar num único ponto. Quando a execução fecha, o vértice é limpo. Quando não fecha, sobra uma **meetline** — linha fina ou pequeno triângulo, nomeada assim no [[12-fancy-cutting-aula-04-talhe-de-precisao-e-talhes-opticos-simetria-extrema-e-padrao-de-reflexao|módulo 12, aula 04]] — e o padrão de reflexão da pedra perde nitidez ali, mesmo que o ângulo geral esteja correto.

O rigor exigido varia por estilo. Um brilhante comercial tolera uma meetline pequena sem que ela pese muito no julgamento; um talhe de precisão a trata como falha grave, porque o estilo inteiro se define pela tolerância apertada do encontro — é o ponto central do módulo 12. Julgar encontro de facetas é, portanto, perguntar não só "os vértices fecham?", mas "quanto rigor este estilo específico promete?".

### Acabamento de polimento — a superfície por si

O quarto critério não é sobre forma: é sobre a **superfície** que a forma recebeu. Uma pedra com proporção e simetria perfeitas ainda pode ter um acabamento ruim — risco visível, ponto fosco, resíduo. O acabamento resulta da etapa final da cadeia física do [[02-fisica-do-desbaste-aula-04-polimento-microabrasao-acao-quimico-mecanica-e-a-camada-de-beilby|módulo 02, aula 04]]: um polidor bem escolhido, aplicado sobre uma superfície que já passou por toda a sequência de grão sem saltar etapa, produz uma superfície lisa e especular. Um acabamento imperfeito é o sinal visível de que algo faltou ou saiu errado nessa cadeia — antecipando o raciocínio da aula 03 deste módulo, que liga cada defeito de acabamento a uma etapa específica do processo.

### Os quatro critérios por família

| Critério | Cabochão | Esfera / torneada | Facetado |
|---|---|---|---|
| Simetria de reflexão | sim (contorno) | não se aplica (rotação plena) | sim (contornos de fantasia) |
| Simetria de rotação | só se contorno regular | sim, em qualquer eixo | sim (*n-fold* do jogo de índice) |
| Proporção | razão de cúpula | razão entre eixos | profundidade % diâmetro, ângulos |
| Encontro de facetas | não se aplica | não se aplica | sim |
| Acabamento de polimento | sim | sim | sim |

Acabamento é o único critério universal — vale para toda família. Os outros três se aplicam de formas diferentes, ou não se aplicam, conforme a geometria que a pedra pronta apresenta.

## Exemplo trabalhado

**Uma pedra oval facetada, contorno alongado, chega para avaliação.**

1. **Simetria.** O contorno oval não tem simetria de rotação alta (não é redondo), mas deve ter simetria de **reflexão** nos dois eixos — metade espelhando a outra ao longo do comprimento e da largura. Medida: as duas metades coincidem ao dobrar mentalmente o contorno ao meio? Se um lado é visivelmente mais largo, a simetria falha.
2. **Proporção.** Profundidade total como porcentagem do diâmetro maior — compara-se contra a faixa que o [[08-optica-do-facetado-modulo|módulo 08]] associou ao índice de refração do material. Fora da faixa, para mais ou para menos, aponta para janela, extinção ou retenção de peso.
3. **Encontro de facetas.** Nos vértices do pavilhão, procura-se meetline: alguma linha fina ou pequeno triângulo em vez de um ponto limpo? Presente ou ausente, e em quantos vértices.
4. **Acabamento.** A superfície de cada faceta, sob luz rasante: lisa e especular, ou com risco, ponto fosco, resíduo de cera de dop.

**Conclusão do exemplo:** os quatro critérios são independentes — a pedra pode passar em três e falhar só no quarto (por exemplo, simetria e proporção corretas, mas com uma meetline num vértice e acabamento perfeito). É por isso que julgar exige checar os quatro, não parar no primeiro que parece bom.

## Erros comuns

- **Cobrar encontro de facetas de um cabochão ou de uma esfera.** O critério não existe onde não há facetas planas se encontrando em vértice.
- **Confundir simetria de rotação com simetria de reflexão.** São propriedades diferentes; um contorno pode ter uma sem a outra (a pêra tem reflexão, não rotação alta).
- **Julgar proporção por um valor absoluto memorizado.** Proporção é razão; o valor de referência muda com o índice de refração do material e com a família de talhe.
- **Achar que acabamento perfeito compensa proporção ruim.** São critérios independentes; nenhum anula o outro no julgamento.
- **Aplicar o mesmo rigor de encontro de facetas a qualquer estilo.** O talhe de precisão exige tolerância muito mais apertada que um brilhante comercial.

## O que não concluir

- Não concluir o catálogo completo de defeitos — janela, extinção, quilha deslocada, cinta ondulada, faceta extra, arranhão de polimento, undercut — é a aula 02 deste módulo.
- Não concluir, a partir de um defeito visível, qual etapa do processo o produziu — é o diagnóstico reverso da aula 03.
- Não concluir se vale a pena recortar uma pedra com defeito — é a aula 04.
- Não concluir como medir cada critério com instrumento de bancada (goniômetro, proporcioscópio) — competência de bancada, fora do nível teórico deste curso.

## Recap relâmpago

- Julgar um talhe pronto exige saber **o que olhar**, não saber lapidar: quatro critérios cobrem a maior parte do que se vê.
- **Simetria** tem duas formas: **rotação** (*n-fold*, limitada pelos divisores do jogo de índice) e **reflexão** (bilateral, em torno de um eixo). Nem toda família usa as duas — a esfera só tem rotação plena, o cabochão oval só tem reflexão.
- **Proporção** é sempre razão ou porcentagem — altura de cúpula sobre a menor dimensão do contorno, profundidade sobre diâmetro —, comparada contra uma faixa de referência que muda com a família e com o índice de refração do material.
- **Encontro de facetas** só existe no talhe facetado: o **meetpoint** fechado é a condição correta; a **meetline** é o defeito. O rigor exigido varia — talhe de precisão tolera muito menos do que um brilhante comercial.
- **Acabamento de polimento** é o único critério universal, presente em toda família, e resulta da etapa final da cadeia física de desbaste e polimento.
- Os quatro critérios são **independentes**: uma pedra pode passar em três e falhar só no quarto.

## Próxima aula

Na [[14-julgar-o-talhe-aula-02-o-catalogo-de-defeitos-o-que-se-ve-na-pedra-pronta|Aula 02 — O catálogo de defeitos]], os quatro critérios desta aula viram uma lista nomeada de falhas específicas — janela, extinção, quilha deslocada, cinta ondulada, faceta extra, arranhão de polimento, undercut — cada uma como a violação visível de um dos critérios aqui estabelecidos.

## Fontes consultadas

- Gemological Institute of America — sistema de avaliação de corte do brilhante redondo: **polimento (*polish*)** e **simetria** são dois dos sete componentes avaliados (brilho, fogo, cintilação, razão de peso, durabilidade, polimento, simetria); as **proporções** entram como a base medida a partir da qual os demais componentes são calculados, e não como uma categoria graduada à parte. Consultada em 2026-09-07.
- United States Faceters Guild, dicionário de facetamento — verbetes *meet* ("a term used in judging how well facets come to a point") e *meetpoint*, ambos presentes e verificados em 2026-09-07: o rigor de encontro como critério de execução.
- International Gem Society, *Diamond Cut Quality: Ultimate Guide* — proporção expressa em **porcentagem** (mesa entre 52% e 62% da largura; altura de coroa entre 12,5% e 17% da profundidade total), nunca em valor absoluto. Consultada em 2026-09-07. Esse guia **não** trata de simetria de contorno de fantasia — declara apenas que talhes fancy usam parâmetros mais frouxos e subjetivos.
- International Gem Society, *How to Grade Fancy Cut Diamonds* — razão comprimento:largura e erros de simetria como categorias de julgamento de contornos de fantasia. Consultada em 2026-09-07.
- [[09-geometria-e-diagramas-modulo|Módulo 09]], [[10-familias-de-talhe-modulo|módulo 10]], [[12-fancy-cutting-modulo|módulo 12]] e [[02-fisica-do-desbaste-modulo|módulo 02]] deste curso — simetria de rotação e jogo de índice, proporção e retenção de peso, meetpoint e meetline, acabamento como resultado da cadeia física de polimento.

<!--
nivel: ensino-medio-com-gemologia-v1
palavras_corpo: 1581
cobertura:
  lapidacao-m14-oa01: [Conteúdo, "Exemplo trabalhado", "Erros comuns", "O que não concluir", "Recap relâmpago"]
alegacoes_auditaveis:
  - claim_id: JUL-CRIT-QUAT-001
    claim: "Quatro critérios cobrem a maior parte do julgamento de um talhe pronto: simetria, proporção, encontro de facetas e acabamento de polimento. Cada um mede uma propriedade diferente e independente das outras — uma pedra pode passar em três critérios e falhar só no quarto."
    risk: definicao
    source: "Gemological Institute of America, sistema de cut grading do brilhante redondo — polimento e simetria entre os sete componentes avaliados; as proporcoes sao a base medida, nao uma categoria graduada a parte (verificado 2026-09-07). United States Faceters Guild, dicionario de facetamento, verbetes meet e meetpoint (presentes, verificados 2026-09-07)"
  - claim_id: JUL-SIM-DOIS-001
    claim: "Simetria de talhe tem duas formas distintas: simetria de rotação (n-fold), em que a pedra parece igual a si mesma após girar 1/n de volta, limitada pelos divisores do jogo de índice da facetadora (módulo 09 deste curso); e simetria de reflexão (bilateral), em que uma metade do contorno espelha a outra em torno de um eixo. Nem toda família de talhe usa as duas: a esfera tem simetria de rotação em qualquer eixo que passe pelo centro, e um cabochão de contorno oval usa só a reflexão, sem simetria de rotação alta."
    risk: definicao
    source: "curso de lapidacao, módulo 09 aula 01 (jogo de índice e divisores), módulo 07 aula 01 (esfera como limite de simetria) e módulo 10 aula 01 (o brilhante redondo tem oito setores repetidos a cada 45 graus); International Gem Society, How to Grade Fancy Cut Diamonds (simetria e razao comprimento:largura em contornos de fantasia; verificado 2026-09-07 — o guia Diamond Cut Quality NAO cobre esse ponto)"
  - claim_id: JUL-PROP-RAZAO-001
    claim: "Proporção, como critério de julgamento de talhe, é sempre expressa como razão ou porcentagem entre dimensões da pedra — nunca como um valor absoluto isolado —, e a faixa de referência contra a qual ela é comparada muda com a família de talhe e, no facetado, com o índice de refração do material."
    risk: definicao
    source: "curso de lapidacao, módulo 06 aula 03 (razão de cúpula), módulo 08 (profundidade % diâmetro e ângulo de pavilhão por índice), módulo 07 aula 04 (razão entre eixos em ovo e obelisco)"
  - claim_id: JUL-ENC-EXCL-001
    claim: "O critério de encontro de facetas só se aplica ao talhe facetado, porque cabochão, esfera e forma torneada não têm facetas planas se encontrando em vértices. No facetado, o meetpoint fechado (vértice limpo onde três ou mais facetas planejadas para se tocar de fato se tocam) é a condição correta; quando a execução escorrega, sobra uma meetline (linha fina ou pequeno triângulo). O rigor exigido varia por estilo: um talhe de precisão exige tolerância de encontro muito mais apertada que um brilhante comercial, porque o estilo se define por essa tolerância."
    risk: definicao
    source: "curso de lapidacao, módulo 09 aula 04 (lógica do meetpoint) e módulo 12 aula 04 (meetline e tolerância do talhe de precisão)"
  - claim_id: JUL-ACAB-UNIV-001
    claim: "O acabamento de polimento é o único dos quatro critérios de julgamento universal a toda família de talhe, e resulta da etapa final da cadeia física de desbaste e polimento — uma superfície que passou por toda a sequência de grão sem saltar etapa, seguida de um polidor bem escolhido para o material, produz acabamento liso e especular; um acabamento imperfeito é sinal visível de falha nessa cadeia."
    risk: consistencia interna
    source: "curso de lapidacao, módulo 02 aula 04 (mecanismo de polimento) e módulo 04 aula 03 (contaminação de grão e risco residual)"
-->
