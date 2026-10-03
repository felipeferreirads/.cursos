# Aula 02: Vetores — módulo, direção e sentido; somar forças e representar atitudes

**ID:** geologia-m28-a02
**Módulo:** [[28-matematica-geociencias-modulo|Módulo 28 — Matemática para geociências]]
**Duração estimada:** ~30 min
**Nível:** ensino médio completo, sem geologia prévia (contrato `ensino-medio-sem-geologia-v1`)
**Objetivo:** representar e decompor vetores e usá-los para somar forças e descrever atitudes de planos e linhas.

> [!info] Esta aula formaliza uma ferramenta que o curso já usou sem nomear O [[27-fisica-geociencias-aula-02-forca-massa-leis-de-newton|Módulo 27, aula 02]] decompôs o peso de um bloco num talude em duas partes sem chamá-las formalmente de "componentes de um vetor"; o [[27-fisica-geociencias-aula-03-pressao-e-tensao|Módulo 27, aula 03]] descreveu tensão variando com a direção sem formalizar o objeto matemático por trás. Os grupos de simetria cristalina (Módulos 04 e 05) também descrevem orientação no espaço sem nomear vetores. Esta aula formaliza o que essas três frentes já pressupunham.

## Antes de começar, você precisa saber

- Força e as leis de Newton — [[27-fisica-geociencias-aula-02-forca-massa-leis-de-newton|Módulo 27, aula 02]] (recomendado).
- Seno, cosseno e tangente — [[28-matematica-geociencias-aula-01-trigonometria-em-campo|aula 01 deste módulo]] (recomendado).

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **Escalar** | Uma grandeza completamente descrita por um número (e uma unidade): massa, temperatura, distância percorrida. |
| **Vetor** | Uma grandeza que precisa de um número **e** uma direção **e** um sentido para ser completamente descrita: deslocamento, força, velocidade. |
| **Módulo (de um vetor)** | O "tamanho" do vetor — quão grande é a grandeza, sem informação de direção. |
| **Componente** | A parte de um vetor projetada sobre uma direção de referência (por exemplo, "eixo x" ou "ao longo da encosta"). |
| **Vetor resultante** | O vetor único que representa o efeito combinado de dois ou mais vetores somados. |
| **Decomposição vetorial** | Reescrever um vetor como a soma de duas (ou mais) componentes perpendiculares entre si. |

## Conteúdo

### Escalar e vetor: quando um número basta, e quando não basta

Diga a alguém "eu andei 5 km" e a frase está completa: um número e uma unidade — **km** — dizem tudo o que há para dizer sobre uma grandeza **escalar**. Agora diga "eu andei 5 km" sem dizer para onde: se a pessoa quer saber onde você está agora em relação ao ponto de partida, a frase é inútil. Faltam a **direção** (norte-sul? leste-oeste?) e o **sentido** (para o norte ou para o sul?). Grandezas que só ficam completas com número, direção e sentido juntos são chamadas de **vetores**. Deslocamento, força, velocidade e campo (gravitacional, magnético) são vetores; massa, tempo, temperatura e distância percorrida são escalares.

Um vetor é desenhado como uma seta: o comprimento da seta representa o **módulo** (o "tamanho", como os 5 km do exemplo), e a orientação da seta representa direção e sentido juntos.

### Decompor um vetor: separar o efeito em duas direções úteis

Um único vetor pode ser reescrito, sem perder informação nenhuma, como a soma de duas **componentes** perpendiculares entre si — uma escolha de "eixos" convenientes para o problema em questão. É exatamente o que a aula sobre Newton fez, sem nomear: o peso de um bloco num talude (um vetor apontando sempre para baixo, na vertical) foi separado em uma componente **paralela** à encosta (a que puxa o bloco ladeira abaixo) e uma componente **perpendicular** a ela (a que empurra o bloco contra a superfície). As duas componentes, somadas de volta, reconstituem exatamente o peso original — a decomposição não cria nem destrói nada, só reorganiza a mesma informação de um jeito mais útil para o problema.

> [!tip] Uma analogia Pense em empurrar um carrinho de supermercado na diagonal. Parte da sua força faz o carrinho **andar para a frente**; parte faz o carrinho ir **para o lado**. Você aplica uma única força, mas o efeito dela se reparte em duas direções diferentes ao mesmo tempo — é exatamente essa repartição que a decomposição vetorial calcula, usando seno e cosseno do ângulo entre a força e a direção escolhida.

Se um vetor de módulo *F* faz um ângulo θ com uma direção de referência, suas componentes ao longo dela e perpendicular a ela são:

- componente ao longo da referência = *F* × cos(θ)
- componente perpendicular à referência = *F* × sen(θ)

### Somar vetores: o efeito combinado de duas grandezas

Quando duas forças (ou dois deslocamentos, ou dois campos) atuam ao mesmo tempo, o efeito combinado é dado pela **soma vetorial**, que não é uma soma simples de números — precisa levar direção e sentido em conta. Duas formas práticas de somar:

- **Graficamente:** encostar a cauda do segundo vetor na ponta do primeiro (método "ponta a ponta"); o vetor resultante vai da cauda do primeiro até a ponta do segundo.
- **Por componentes:** decompor cada vetor em componentes ao longo dos mesmos dois eixos de referência, somar as componentes de mesma direção separadamente, e recompor o resultado.

Um caso especial vale destacar: se dois vetores têm a **mesma** direção e sentido, a soma é simples — os módulos se somam diretamente. Se têm a mesma direção e sentidos **opostos**, a soma é a diferença dos módulos, no sentido do maior. É só quando as direções são diferentes que a decomposição em componentes se torna necessária.

### Vetores para descrever orientação: da atitude estrutural aos eixos cristalinos

Vetores não servem só para forças — também descrevem **orientação no espaço**, sem magnitude física associada. A direção e o mergulho de um plano geológico (vistos na [[28-matematica-geociencias-aula-01-trigonometria-em-campo|aula 01]]) podem ser representados por um vetor de módulo fixo (geralmente 1, um "vetor unitário") apontando na orientação do **polo** desse plano — perpendicular a ele. Da mesma forma, os eixos cristalográficos que organizam a simetria de um cristal (Módulos 04 e 05) são, matematicamente, um conjunto de vetores de referência que definem as direções privilegiadas da estrutura atômica. Em nenhum dos dois casos os módulos anteriores chamaram esses objetos de "vetores" — mas é exatamente essa a ferramenta matemática usada por trás, e reconhecê-la ajuda a enxergar o que direção/mergulho e eixos cristalinos têm em comum: ambos descrevem orientação, não força.

## Exemplo trabalhado

**Situação:** um bloco de rocha de peso 500 N (newtons) repousa sobre um talude inclinado 25° em relação à horizontal — a mesma situação de princípio da [[27-fisica-geociencias-aula-02-forca-massa-leis-de-newton|aula 02 do Módulo 27]], agora resolvida com o vocabulário formal de vetores.

**Pergunta 1: qual a componente do peso paralela à encosta (a que tende a puxar o bloco ladeira abaixo)?**

O peso é um vetor vertical de módulo 500 N. O ângulo entre o peso (vertical) e a direção perpendicular à encosta é igual ao ângulo do talude, 25° — resultado de geometria de ângulos complementares. A componente paralela à encosta é: 500 × sen(25°) ≈ 500 × 0,423 ≈ **211 N**.

**Pergunta 2: qual a componente perpendicular à encosta (a que pressiona o bloco contra a superfície)?**

Componente perpendicular = 500 × cos(25°) ≈ 500 × 0,906 ≈ **453 N**.

**Pergunta 3: as duas componentes, somadas de volta, devem reconstituir o peso original. Isso se confirma?**

Sim — mas a soma correta de componentes perpendiculares não é a soma aritmética simples (211 + 453 = 664, que não bate com 500); é a soma vetorial usando o teorema de Pitágoras, já que as duas componentes formam um triângulo retângulo com o vetor original como hipotenusa: √(211² + 453²) = √(44.521 + 205.209) = √249.730 ≈ **500 N**. Confere.

**A lição:** decompor um vetor em duas componentes perpendiculares e depois somá-las de volta **não** é uma soma aritmética direta — é uma soma que respeita a geometria, e o teorema de Pitágoras é a ferramenta que confirma que a decomposição foi bem feita.

## Erros comuns

- **Somar módulos de vetores diretamente, ignorando a direção.** Só funciona quando os vetores têm exatamente a mesma direção; em qualquer outro caso, a soma exige decomposição em componentes ou o teorema de Pitágoras (para vetores perpendiculares).
- **Confundir escalar com vetor.** Massa é escalar; peso (a força da gravidade sobre a massa) é vetor — tratados como sinônimos no dia a dia, são grandezas fisicamente diferentes.
- **Trocar seno por cosseno na decomposição.** A componente **ao longo** da direção de referência usa cosseno do ângulo entre o vetor e essa direção; a componente **perpendicular** usa seno do mesmo ângulo — inverter os dois é o erro mais comum do tópico.
- **Achar que decompor um vetor "perde" parte da grandeza original.** A decomposição é reversível: somando as componentes de volta (com Pitágoras, se forem perpendiculares), o vetor original é recuperado por inteiro.

## O que não concluir

- **Que esta aula ensina produto escalar, produto vetorial ou o tensor de tensões completo.** Essas ferramentas mais avançadas de álgebra vetorial ficam para quando o curso tratar geofísica quantitativa ou geologia estrutural avançada; esta aula entrega apenas soma, decomposição e módulo de vetores em duas dimensões.
- **Que a representação vetorial de atitude estrutural (direção/mergulho) substitui o símbolo de atitude do mapa geológico.** São a mesma informação em duas linguagens diferentes — o vetor é a formalização matemática, o símbolo é a convenção cartográfica; nenhum substitui o outro na prática de campo.

## Recap relâmpago

- **Escalar** = número + unidade; **vetor** = número (módulo) + direção + sentido.
- Um vetor pode ser **decomposto** em duas componentes perpendiculares: componente ao longo de uma referência = módulo × cos(θ); componente perpendicular = módulo × sen(θ).
- **Somar vetores** respeita direção e sentido — não é soma aritmética simples, exceto quando os vetores têm exatamente a mesma direção.
- Vetores perpendiculares se recompõem pelo **teorema de Pitágoras**.
- Vetores também descrevem **orientação** (direção/mergulho de um plano, eixos cristalográficos), não só força — o que os Módulos 04, 05 e 18 usaram implicitamente sem nomear.

## Próxima aula

[[28-matematica-geociencias-aula-03-exponenciais-e-logaritmos|Aula 03 — Exponenciais e logaritmos: a matemática da meia-vida e das escalas logarítmicas]]

## Anterior

[[28-matematica-geociencias-aula-01-trigonometria-em-campo|Aula 01 — Trigonometria em campo]]

## Fontes

- Grandezas escalares e vetoriais, decomposição e soma de vetores: física geral básica (ex.: Halliday, Resnick & Walker, *Fundamentals of Physics*, capítulo de vetores).
- Aplicação a decomposição de peso em plano inclinado: mesma referência, capítulo de dinâmica.
- Vetor unitário como representação de polo de plano geológico (direção e mergulho): Rowland, Duebendorfer & Schiefelbein (2007), *Structural Analysis and Synthesis*, capítulo de projeção estereográfica (referência conceitual, não desenvolvida nesta aula).

<!--
nivel: ensino-medio-sem-geologia-v1
palavras_corpo: ~1380
bridge_lesson: true

mapa_objetivo_secao:
  OA-02: "Escalar e vetor: quando um número basta, e quando não basta" + "Decompor um vetor: separar o efeito em duas direções úteis" + "Somar vetores: o efeito combinado de duas grandezas" + "Vetores para descrever orientação: da atitude estrutural aos eixos cristalinos" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEO-M28-A02-ESCALAR-VETOR-001
    claim: "Uma grandeza escalar é completamente descrita por um número e uma unidade; uma grandeza vetorial exige adicionalmente direção e sentido para ser completamente descrita."
    risk: fato
    source: "física geral básica; álgebra vetorial elementar"
  - claim_id: GEO-M28-A02-DECOMPOSICAO-002
    claim: "Um vetor de módulo F que faz ângulo θ com uma direção de referência tem componente F·cos(θ) ao longo dessa direção e componente F·sen(θ) perpendicular a ela."
    risk: fato
    source: "trigonometria aplicada a decomposição vetorial; física geral básica"
  - claim_id: GEO-M28-A02-SOMA-VETORIAL-003
    claim: "A soma de vetores não equivale, em geral, à soma aritmética de seus módulos; para vetores perpendiculares, o módulo do vetor resultante é dado pelo teorema de Pitágoras aplicado às componentes."
    risk: fato
    source: "álgebra vetorial elementar; geometria"
  - claim_id: GEO-M28-A02-ORIENTACAO-VETOR-004
    claim: "A atitude de um plano geológico (direção e mergulho) pode ser representada matematicamente por um vetor unitário na orientação do polo do plano (perpendicular a ele), formalização usada em projeção estereográfica."
    risk: interpretacao
    source: "Rowland, Duebendorfer & Schiefelbein 2007, Structural Analysis and Synthesis, cap. de projeção estereográfica"

nota_trilha_apoio: >-
  Aula 2 de 4 do módulo 28 (trilha de apoio, opcional, não bloqueante), criada em
  2026-08-19. Formaliza o vocabulário de vetores que 27-fisica-geociencias-aula-02
  (decomposição de peso num talude) e 27-fisica-geociencias-aula-03 (tensão variando
  com a direção) usaram implicitamente sem nomear, e que os Módulos 04/05
  (simetria e eixos cristalinos) também pressupõem sem formalizar.
-->
