# Aula 03: Exponenciais e logaritmos — a matemática da meia-vida e das escalas logarítmicas

**ID:** geologia-m28-a03
**Módulo:** [[28-matematica-geociencias-modulo|Módulo 28 — Matemática para geociências]]
**Duração estimada:** ~30 min
**Nível:** ensino médio completo, sem geologia prévia (contrato `ensino-medio-sem-geologia-v1`)
**Objetivo:** interpretar funções exponenciais e logarítmicas e aplicá-las à meia-vida e às escalas logarítmicas (pH, magnitude, phi).

> [!info] Esta aula entrega uma conta que o curso deixou pendente de propósito O [[03-tempo-geologico-geocronologia-aula-04-meia-vida|Módulo 03, aula 04]] ensina meia-vida **contando divisões pela metade** (1, 2, 3 meias-vidas…) e avisa explicitamente: "razões que não são meias-vidas inteiras exigem logaritmo, ferramenta que este curso ainda não ensinou" (regra LC-06). Esta aula entrega essa ferramenta. Ela **não repete** a explicação qualitativa do que é meia-vida — isso já foi ensinado — e assume que você já sabe o que significa "razão pai/filho" e "sistema fechado".

## Antes de começar, você precisa saber

- O que é **meia-vida**, **razão pai/filho** e **sistema fechado** — [[03-tempo-geologico-geocronologia-aula-04-meia-vida|Módulo 03, aula 04]] (exigido).
- A escala de **pH** — [[26-quimica-geociencias-aula-03-solucoes-concentracao-ph|Módulo 26, aula 03]] (recomendado; não repetida aqui).
- Ler potências de dez — [[00-partida-do-zero-aula-03-ordens-de-grandeza|Módulo 00, aula 03]].

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **Função exponencial** | Uma função em que a variável aparece no **expoente**; cresce (ou decresce) por um fator fixo a cada intervalo igual, não por uma quantidade fixa. |
| **Função logarítmica** | A função **inversa** da exponencial: responde "a que expoente eu preciso elevar essa base para obter este número?". |
| **Base** | O número fixo que é elevado ao expoente numa exponencial, ou o número de referência de um logaritmo. |
| **Constante de decaimento (λ)** | Um número fixo, próprio de cada isótopo radioativo, que mede a rapidez do decaimento — quanto maior λ, mais rápido a quantidade de pai diminui. |
| **Escala logarítmica** | Uma escala numérica em que cada unidade representa um **fator multiplicativo** fixo (geralmente ×10), não uma soma fixa — usada quando os valores de interesse cobrem uma faixa enorme. |

## Conteúdo

### A exponencial: quando a variável está no expoente

Uma função comum, como a distância percorrida a velocidade constante, cresce por uma **quantidade fixa** a cada intervalo de tempo igual — é uma função linear. Uma **função exponencial** é diferente: ela cresce (ou decresce) por um **fator multiplicativo fixo** a cada intervalo igual, porque a variável (geralmente o tempo) aparece no **expoente**. É exatamente o comportamento que a aula sobre meia-vida já descreveu com palavras: "a fração que decai por ano é constante; a quantidade absoluta diminui sempre" — essa é a assinatura de uma exponencial decrescente (decaimento exponencial).

A forma matemática do decaimento radioativo é:

$$N(t) = N_0 \cdot e^{-\lambda t}$$

onde *N(t)* é a quantidade de átomos-pai restante no tempo *t*, *N₀* é a quantidade inicial, *e* é a base dos logaritmos naturais (uma constante, aproximadamente 2,718, tão fixa quanto π), e **λ** (lambda) é a **constante de decaimento**, própria de cada isótopo — o equivalente matemático da "meia- vida" já conhecida, só que expressa como taxa em vez de como tempo. As duas formas se relacionam por:

$$\lambda = \frac{\ln(2)}{T_{1/2}}$$

onde *T½* é a meia-vida e ln(2) é o logaritmo natural de 2 (uma constante, ≈ 0,693). Quanto menor a meia-vida, maior λ, mais rápido o decaimento — consistente com a tabela de meias-vidas já vista no Módulo 03.

### O logaritmo: a pergunta inversa da exponencial

A exponencial responde "quanto sobra depois de um certo tempo?". O **logaritmo** responde a pergunta oposta: "quanto tempo passou, para sobrar uma certa fração?" Formalmente, o logaritmo de um número *x* numa base *b* é o expoente ao qual *b* precisa ser elevado para dar *x*:

$$\log_b(x) = y \iff b^y = x$$

> [!tip] Uma analogia A exponencial é como perguntar "se eu dobrar uma folha de papel 5 vezes, quantas camadas ela tem?" (resposta: 2⁵ = 32). O logaritmo é a pergunta ao contrário: "eu tenho 32 camadas de papel; quantas vezes ele foi dobrado?" (resposta: log₂(32) = 5, porque 2⁵ = 32). Uma pergunta desfaz a outra — exponenciação e logaritmação são operações inversas, do mesmo jeito que soma e subtração, ou multiplicação e divisão.

Isolando o tempo na fórmula do decaimento (N(t) = N₀·e^(−λt)), obtém-se:

$$t = -\frac{1}{\lambda} \ln\left(\frac{N}{N_0}\right)$$

Essa é exatamente a fórmula geral que o Módulo 03 avisou que ficaria pendente: ela funciona para **qualquer** razão pai/filho — 12,5%, 37%, 8,2% — não só para frações que são potências exatas de 1/2.

### Escalas logarítmicas: quando o intervalo de interesse é gigantesco

Muitas grandezas em geociências cobrem uma faixa tão ampla — de milésimos a milhões, ou mais — que representá-las numa escala comum (linear) seria inútil: os valores pequenos ficariam todos amontoados perto de zero. A solução é uma **escala logarítmica**: cada unidade da escala representa não uma soma fixa, mas um **fator multiplicativo fixo**, geralmente 10 vezes. Três escalas logarítmicas já apareceram ou aparecerão neste curso:

- **pH** ([[26-quimica-geociencias-aula-03-solucoes-concentracao-ph|Módulo 26, aula 03]]) — mede a concentração de íons H⁺ numa escala logarítmica de base 10; cada unidade de pH representa uma concentração de H⁺ dez vezes maior ou menor.
- **Magnitude de terremoto** (escala de momento sísmico, que substituiu a escala Richter original na prática moderna) — cada unidade inteira de magnitude corresponde a cerca de **10 vezes** mais amplitude de abalo registrada no sismógrafo, e a cerca de **31,6 vezes** (10^1,5) mais energia liberada. Duas unidades de magnitude, portanto, já representam cerca de **1.000 vezes** mais energia — não 2 vezes.
- **Escala phi (φ)** de tamanho de grão sedimentar — usada para classificar sedimentos de argila a matacão — é definida como φ = −log₂(diâmetro em mm); cada unidade de phi representa uma **duplicação** (ou uma redução à metade) do diâmetro do grão, o que comprime uma faixa de tamanhos que vai de frações de milímetro a metros numa escala numérica administrável.

O padrão comum às três: sempre que uma grandeza física varia por muitas ordens de grandeza, uma escala logarítmica comprime essa variação em números pequenos e manejáveis — ao custo de que uma diferença "pequena" na escala (uma unidade de pH, de magnitude, de phi) já representa uma diferença **grande** na grandeza física original.

## Exemplo trabalhado

**Situação 1 — completando o exemplo que o Módulo 03 deixou em aberto.** Um mineral vulcânico é analisado e mede-se que restam **37%** do potássio-40 original (uma razão que não é potência exata de 1/2). A meia-vida do potássio-40 é de cerca de 1,25 Ga (bilhões de anos). Qual a idade?

**Passo 1 — calcular λ a partir da meia-vida.** λ = ln(2) / T½ = 0,693 / 1,25 Ga ≈ 0,554 por Ga.

**Passo 2 — aplicar a fórmula do tempo.** t = −(1/λ) × ln(N/N₀) = −(1/0,554) × ln(0,37).

**Passo 3 — calcular o logaritmo natural de 0,37.** ln(0,37) ≈ −0,994 (negativo, porque 0,37 é menor que 1 — o logaritmo de uma fração menor que 1 é sempre negativo).

**Passo 4 — substituir e simplificar os sinais.** t = −(1/0,554) × (−0,994) = (0,994/0,554) ≈ **1,79 Ga**.

**Conferência de plausibilidade:** restar 37% é mais que os 25% de duas meias-vidas completas e menos que os 50% de uma meia-vida completa — então a idade deveria ficar **entre** 1 meia-vida (1,25 Ga) e 2 meias-vidas (2,5 Ga). 1,79 Ga está exatamente nesse intervalo. Confere.

**Situação 2 — magnitude sísmica.** Um terremoto de magnitude 7 é comparado a um de magnitude 5. Quantas vezes mais energia o de magnitude 7 libera?

**Cálculo:** a diferença de magnitude é ΔM = 2. O fator de energia por unidade de magnitude é cerca de 31,6× (10^1,5); para duas unidades, o fator se multiplica: 31,6 × 31,6 ≈ 1.000, ou diretamente 10^(1,5 × 2) = 10³ = **1.000 vezes mais energia**. Note que a amplitude registrada no sismógrafo segue outro fator: 10² = **100 vezes maior**, não 1.000 — amplitude e energia crescem em taxas diferentes ao longo da escala, e confundir as duas é o erro mais comum do tópico.

## Erros comuns

- **Tratar o decaimento exponencial como linear.** Já era o erro número um da aula de meia-vida; aqui ele reaparece na forma de achar que "37% restante" significa "37% do tempo total decorrido" — não significa, porque a relação entre fração restante e tempo é logarítmica, não linear.
- **Esquecer o sinal negativo na fórmula do tempo.** ln de uma fração menor que 1 é sempre negativo; multiplicado pelo −1/λ da fórmula, o resultado final para *t* é positivo — sumir com um dos dois sinais dá idade negativa, um resultado fisicamente sem sentido que deveria soar o alarme.
- **Confundir o fator de amplitude com o fator de energia numa escala de magnitude.** Para cada unidade de magnitude, a amplitude aumenta ~10× mas a energia aumenta ~31,6×; para duas unidades, 100× em amplitude contra 1.000× em energia — são grandezas físicas diferentes crescendo a taxas diferentes na mesma escala.
- **Achar que uma unidade de pH, magnitude ou phi representa uma diferença "pequena".** Cada unidade dessas escalas representa um fator multiplicativo (geralmente 10× ou 2×) na grandeza física real — pequeno na escala, grande na realidade que ela mede.

## O que não concluir

- **Que esta aula ensina isócronas, regressão linear em dados isotópicos, ou propagação de incerteza em datação.** Esse tratamento mais completo, incluindo o caso em que há filho inicial presente na amostra, é o conteúdo avançado de geocronologia isotópica, fora do escopo desta aula introdutória de matemática.
- **Que a escala de magnitude sísmica usada hoje é idêntica à escala Richter original de 1935.** A prática moderna usa majoritariamente a escala de magnitude de momento (Mw), calibrada para concordar aproximadamente com a Richter na faixa intermediária, mas mais robusta para terremotos grandes — o comportamento logarítmico descrito aqui vale para ambas.

## Recap relâmpago

- **Função exponencial**: a variável está no expoente; cresce/decresce por fator multiplicativo fixo a cada intervalo igual — é o que rege o decaimento radioativo, N(t) = N₀·e^(−λt).
- **λ (constante de decaimento)** e **meia-vida** se relacionam por λ = ln(2)/T½.
- **Logaritmo** é a operação inversa da exponencial: log_b(x) = y ⟺ b^y = x.
- A fórmula geral da idade radiométrica, t = −(1/λ)·ln(N/N₀), funciona para **qualquer** razão pai/filho, não só potências exatas de 1/2 — é a ferramenta que o Módulo 03 deixou pendente.
- **Escalas logarítmicas** (pH, magnitude sísmica, phi) comprimem faixas enormes de variação; cada unidade da escala é um **fator multiplicativo**, não uma soma — amplitude e energia sísmica, em particular, crescem a taxas diferentes (10× e ~31,6× por unidade de magnitude).

## Próxima aula

[[28-matematica-geociencias-aula-04-estatistica-descritiva|Aula 04 — Estatística descritiva: média, dispersão, histograma e leitura de incerteza]]

## Anterior

[[28-matematica-geociencias-aula-02-vetores|Aula 02 — Vetores]]

## Fontes

- Função exponencial, logaritmo e suas propriedades: matemática do ensino médio / cálculo introdutório.
- Lei do decaimento radioativo N(t) = N₀e^(−λt) e relação λ = ln(2)/T½: física nuclear consolidada; G. Faure & T. M. Mensing (2005), *Isotopes: Principles and Applications*, 3ª ed., Wiley, capítulo 1.
- Escala de magnitude de momento sísmico e fatores de amplitude/energia por unidade: U.S. Geological Survey (USGS), *Earthquake Magnitude, Energy Release, and Shaking Intensity* (página de referência pública do USGS).
- Escala phi de tamanho de grão: Krumbein, W. C. (1934), definição original da escala; Boggs, S., *Principles of Sedimentology and Stratigraphy*, capítulo de textura sedimentar.

<!--
nivel: ensino-medio-sem-geologia-v1
palavras_corpo: ~1560
bridge_lesson: true

mapa_objetivo_secao:
  OA-03: "A exponencial: quando a variável está no expoente" + "O logaritmo: a pergunta inversa da exponencial" + "Escalas logarítmicas: quando o intervalo de interesse é gigantesco" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEO-M28-A03-DECAIMENTO-FORMULA-001
    claim: "A lei do decaimento radioativo é N(t) = N0 · e^(-λt), onde N0 é a quantidade inicial de átomos-pai, λ é a constante de decaimento própria do isótopo e t é o tempo decorrido."
    risk: fato
    source: "física nuclear consolidada; Faure & Mensing 2005, Isotopes: Principles and Applications, cap. 1"
  - claim_id: GEO-M28-A03-LAMBDA-MEIA-VIDA-002
    claim: "A constante de decaimento λ relaciona-se com a meia-vida T½ por λ = ln(2)/T½."
    risk: fato
    source: "física nuclear consolidada; Faure & Mensing 2005, Isotopes: Principles and Applications, cap. 1"
  - claim_id: GEO-M28-A03-LOGARITMO-DEF-003
    claim: "O logaritmo é a operação inversa da exponenciação: log_b(x) = y se e somente se b^y = x."
    risk: fato
    source: "matemática elementar; definição padrão de logaritmo"
  - claim_id: GEO-M28-A03-FORMULA-IDADE-004
    claim: "Isolando t na lei do decaimento, obtém-se t = -(1/λ)·ln(N/N0), válida para qualquer razão N/N0 entre 0 e 1, não apenas para potências inteiras de 1/2."
    risk: fato
    source: "álgebra elementar aplicada à lei do decaimento radioativo"
  - claim_id: GEO-M28-A03-MAGNITUDE-ESCALA-005
    claim: "Na escala de magnitude sísmica (Richter/magnitude de momento), cada unidade inteira corresponde a um aumento de aproximadamente 10 vezes na amplitude do abalo registrada no sismógrafo e de aproximadamente 31,6 vezes (10^1,5) na energia liberada; uma diferença de duas unidades de magnitude corresponde a aproximadamente 1.000 vezes mais energia."
    risk: numero
    source: "U.S. Geological Survey, Earthquake Magnitude, Energy Release, and Shaking Intensity (referência pública consolidada)"
  - claim_id: GEO-M28-A03-PHI-DEF-006
    claim: "A escala phi (φ) de tamanho de grão sedimentar é definida como φ = -log2(diâmetro em milímetros), de modo que cada unidade de phi corresponde a uma duplicação ou redução à metade do diâmetro do grão."
    risk: fato
    source: "Krumbein 1934 (definição original); Boggs, Principles of Sedimentology and Stratigraphy"

nota_trilha_apoio: >-
  Aula 3 de 4 do módulo 28 (trilha de apoio, opcional, não bloqueante), criada em
  2026-08-19. Entrega diretamente a lacuna deixada em aberto por
  03-tempo-geologico-geocronologia-aula-04-meia-vida (nota "Sobre a matemática":
  razões que não são meias-vidas inteiras exigem logaritmo). Não repete a
  explicação qualitativa de meia-vida, razão pai/filho ou sistema fechado —
  pressupõe esse conteúdo e formaliza apenas a matemática. Também cobre a escala
  phi, citada no objetivo geologia-m28-oa03, com relevância direta para
  o futuro módulo de sedimentologia (M13).
-->
