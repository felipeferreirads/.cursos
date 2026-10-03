# Aula 02: Variáveis regionalizadas, função aleatória e estacionariedade

**ID:** geologia-avancado-m20-a02
**Módulo:** [[20-geoestatistica-modulo|Módulo 20 — Introdução à geoestatística]]
**Duração estimada:** ~22 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** apresentar o conceito que separa a geoestatística da estatística clássica trabalhada na Aula 01 — a variável regionalizada, tratada como uma realização de uma função aleatória — e as hipóteses de estacionariedade, sobretudo a hipótese intrínseca, que tornam possível inferir estatística espacial a partir de uma única realização geológica.
**Ao final você vai conseguir:** explicar por que uma variável regionalizada é tratada simultaneamente como aleatória (localmente) e estruturada (regionalmente), e o que isso significa formalmente; explicar por que a existência de uma única realização torna as hipóteses de estacionariedade indispensáveis, e não um detalhe técnico; distinguir estacionariedade de segunda ordem da hipótese intrínseca dizendo com precisão onde está a folga entre as duas; e reconhecer, diante de um conjunto de dados, qual das duas hipóteses se sustenta — ou se o que existe é uma deriva, que nenhuma das duas acomoda.
**Pré-requisito:** [[20-geoestatistica-aula-01-preparacao-dados-estatistica-descritiva|Aula 01 — Preparação de dados e estatística descritiva]] (as medidas de variância desenvolvidas ali são retomadas aqui sob uma lente espacial).

> [!note] Esta aula é a **Parte 1** de um par. Ela estabelece o modelo probabilístico (variável regionalizada, função aleatória, estacionariedade). A [[20-geoestatistica-aula-03-suporte-relacao-de-krige-anisotropia|Aula 03 — Parte 2]] trata das duas consequências práticas desse modelo: o efeito de suporte e a anisotropia. O par foi dividido porque a Parte 1 é inteiramente abstrata e precisa de espaço próprio; estude as duas em sequência.

## Conteúdo

### O paradoxo da variável regionalizada

A Aula 01 tratou o conjunto de teores como uma amostra estatística comum: uma coleção de números, sem levar em conta onde cada um estava localizado. Mas um teor de ouro medido a 5 m de outro teor de ouro não é independente dele da mesma forma que duas jogadas de dado são independentes uma da outra — rochas próximas tendem a se parecer mais entre si do que rochas distantes, porque compartilham a mesma história geológica de formação. Ao mesmo tempo, essa semelhança não é uma função matemática exata: dois pontos a 5 m de distância no mesmo corpo mineralizado quase sempre têm teores parecidos, mas não idênticos — há uma componente de variação que parece genuinamente errática, ligada a heterogeneidades de escala menor do que a amostragem consegue resolver.

Georges Matheron, ao formalizar a geoestatística nos anos 1960 a partir do trabalho pioneiro de Danie Krige na mineração sul-africana, chamou esse duplo comportamento de **variável regionalizada**: uma variável numérica distribuída no espaço que tem, simultaneamente, um **aspecto aleatório** (a variação de pequena escala, aparentemente errática, entre pontos muito próximos) e um **aspecto estruturado** (a tendência de valores próximos serem parecidos, que se degrada com a distância). Nenhum dos dois aspectos sozinho descreve o fenômeno: tratar o teor como puramente aleatório (a estatística clássica da Aula 01, ignorando a posição) descarta a informação de que amostras vizinhas se parecem; tratar o teor como puramente determinístico (uma função matemática exata da posição) ignora a variabilidade real que nenhum modelo geológico, por mais detalhado, consegue prever ponto a ponto.

### A função aleatória: tratar o desconhecido como uma família de possibilidades

A ferramenta formal que a geoestatística usa para capturar esse duplo caráter é a **função aleatória** (ou campo aleatório). A ideia é tratar o valor da variável em cada posição $x$ do espaço, $Z(x)$, não como um número fixo, mas como uma **variável aleatória** — um valor que poderia, em princípio, ter sido diferente, extraído de uma distribuição de probabilidade. O conjunto de todas essas variáveis aleatórias, uma para cada posição $x$ do domínio de interesse, $\{Z(x), x \in D\}$, é a função aleatória. O valor observado de fato em cada furo de sondagem — o número que está na planilha — é chamado de **realização**: um resultado particular, entre infinitas possibilidades teóricas, do processo aleatório subjacente.

Essa construção resolve um problema conceitual real: o depósito mineral que existe fisicamente no subsolo é único — não existem "depósitos paralelos" dos quais se poderia tirar múltiplas amostras independentes para estimar uma distribuição de probabilidade, como se faz ao jogar um dado várias vezes. Existe **uma única realização** da variável regionalizada, e a partir dela a geoestatística precisa inferir os parâmetros (média, variância, estrutura espacial) da função aleatória que, hipoteticamente, a gerou. Essa é a razão pela qual a etapa seguinte — as hipóteses de estacionariedade — não é um detalhe técnico secundário: sem alguma forma de estacionariedade, seria matematicamente impossível estimar qualquer coisa a partir de uma única realização, porque não haveria repetição suficiente de nenhum padrão para se inferir uma estatística confiável.

### Estacionariedade: por que repetir no espaço substitui repetir no tempo

Em estatística clássica, confiamos em uma média porque a calculamos sobre muitas repetições independentes do mesmo experimento. Na geoestatística, a "repetição" vem de outro lugar: assume-se que, embora exista uma única realização, o comportamento estatístico da variável se repete de forma consistente ao longo do domínio espacial — de modo que diferentes pares de pontos, situados em lugares diferentes mas com a mesma distância e direção relativa entre si, podem ser tratados como repetições comparáveis do mesmo fenômeno. Essa suposição é o que se chama de **estacionariedade**, e existem dois níveis principais, do mais forte ao mais fraco:

**Estacionariedade de segunda ordem** exige duas condições: (1) a esperança (média) de $Z(x)$ é constante em todo o domínio, $E[Z(x)] = m$, não dependendo de $x$; e (2) a covariância entre dois pontos, $Cov[Z(x), Z(x+h)]$, depende apenas do vetor de separação $h$ (distância e direção entre os dois pontos), não das posições absolutas $x$ e $x+h$. Sob essa hipótese, existe uma função de covariância $C(h)$ bem definida e finita para todo $h$, inclusive $h=0$ (que é, por definição, a variância da variável).

**Hipótese intrínseca** é mais fraca, e por isso mais amplamente aplicável: em vez de exigir uma covariância finita bem definida, ela exige apenas que os **incrementos** $Z(x+h) - Z(x)$ tenham média zero e variância finita, dependente apenas de $h$:

$$E[Z(x+h) - Z(x)] = 0 \qquad \text{Var}[Z(x+h)-Z(x)] = 2\gamma(h)$$

A função $\gamma(h)$ é o **variograma**, formalmente definido aqui e desenvolvido em profundidade na Aula 04. A hipótese intrínseca é estritamente mais fraca do que a estacionariedade de segunda ordem — toda função com covariância de segunda ordem também satisfaz a hipótese intrínseca, mas o inverso não é verdadeiro.

#### Onde exatamente está a folga entre as duas hipóteses

Este é o ponto em que a literatura aplicada frequentemente escorrega, e vale ir devagar, porque é dele que sai o exemplo trabalhado desta aula.

Repare primeiro no que as duas hipóteses têm **em comum**. A hipótese intrínseca **também** impõe média constante: a condição $E[Z(x+h)-Z(x)]=0$ é precisamente a afirmação de que o valor esperado não muda de um ponto para outro. Nesse quesito as duas exigem o mesmo.

A diferença está na **segunda** exigência da estacionariedade de segunda ordem, e é uma só: a hipótese intrínseca **não requer que a variância a priori seja finita**. Existem fenômenos cuja variabilidade continua a crescer indefinidamente com a distância — o variograma sobe sem nunca atingir um patamar (modelos linear e de potência, comportamento tipo movimento browniano) — e para eles a covariância $C(h)$ simplesmente não existe, porque $C(0)=\sigma^2$ é infinita. A hipótese intrínseca continua valendo nesses casos, e o variograma continua definido e modelável, enquanto a estacionariedade de segunda ordem falha. É essa, e apenas essa, a razão formal pela qual a geoestatística de recursos minerais adota a hipótese intrínseca como base de trabalho padrão.

**Guarde a distinção nesta forma curta:** as duas hipóteses pedem média constante; só a de segunda ordem pede também variância finita.

#### E a deriva? Nenhuma das duas a acomoda

Uma **deriva** (*drift*) é uma tendência sistemática de aumento ou diminuição do teor médio numa direção — comum em depósitos com zoneamento geoquímico. É natural supor que a hipótese intrínseca, sendo a mais frouxa, dê conta dela. **Não dá.** A deriva **viola** a hipótese intrínseca, pela condição que as duas hipóteses compartilham: se a média muda com a posição, os incrementos deixam de ter esperança zero.

O tratamento da deriva é outro, e tem dois caminhos:

- **Quase-estacionariedade** — o caminho usual na prática mineira. Assume-se que a média é constante apenas dentro de uma vizinhança de busca pequena o suficiente, e estima-se ponto a ponto com uma **vizinhança móvel**. É exatamente o que a krigagem ordinária faz, e é por isso que ela é a forma dominante na indústria (Aula 05).
- **Modelagem explícita da deriva** — o caminho formal, para deriva marcada e sistemática: **krigagem universal** (*universal kriging*, ou krigagem com modelo de tendência) e **funções aleatórias intrínsecas de ordem $k$** (IRF-$k$). Ambas ficam fora do escopo deste módulo introdutório; ficam registradas para que você saiba que existem e como se chamam.

## Exemplo trabalhado

**Situação:** você recebe três conjuntos de dados de furos de sondagem, de três depósitos diferentes, e precisa decidir, para cada um, qual hipótese de estacionariedade pode assumir antes de seguir para a variografia. O que se sabe de cada um:

| Conjunto | O que os dados mostram |
|---|---|
| **A** — pórfiro de Cu | O variograma experimental sobe e se estabiliza num platô, e esse platô coincide com a variância a priori do conjunto. Não há tendência sistemática do teor médio em nenhuma direção do depósito. |
| **B** — depósito laterítico de Ni | O variograma experimental sobe de forma persistente até a maior distância calculada, sem sinal de platô; um modelo linear ajusta bem os pontos. O teor médio das compositas não muda sistematicamente de um lado a outro da área. |
| **C** — veio epitermal de Au | O teor médio das compositas cresce de forma regular e monotônica de sudoeste para nordeste ao longo de todo o corpo, acompanhando o zoneamento geoquímico mapeado. |

**Pergunta:** para cada conjunto, diga (a) se a estacionariedade de segunda ordem se sustenta; (b) se a hipótese intrínseca se sustenta; e (c) o que fazer em seguida.

**Resolução:**

**Conjunto A — as duas hipóteses se sustentam.** O platô bem definido significa que a variância a priori é finita, e coincidir com ela é o comportamento esperado sob estacionariedade de segunda ordem. Sem tendência direcional, a média é constante. Satisfeitas as duas condições da hipótese mais forte, e como segunda ordem implica intrínseca, a mais fraca também vale. **Em seguida:** modelar o variograma normalmente; pode-se trabalhar indiferentemente com $\gamma(h)$ ou com $C(h)$, porque a covariância existe.

**Conjunto B — só a hipótese intrínseca se sustenta.** Um variograma que sobe sem patamar é precisamente o caso de **variância a priori não finita**: se $\sigma^2$ fosse finita, o variograma teria de estabilizar nela. Logo $C(0)$ não existe, a função de covariância não está definida, e a estacionariedade de segunda ordem **falha**. Mas a média é constante (sem tendência sistemática), então os incrementos têm esperança zero e sua variância depende só de $h$ — a hipótese intrínseca **vale**. **Em seguida:** modelar o variograma com um modelo sem patamar (linear ou de potência) e trabalhar **só** com $\gamma(h)$: qualquer passo que exija $C(h)$ é inválido aqui. É exatamente o caso que justifica a hipótese intrínseca existir.

**Conjunto C — nenhuma das duas se sustenta no domínio inteiro.** A tendência monotônica de SW para NE é uma **deriva**: a média depende da posição. Isso derruba a condição que as duas hipóteses compartilham — os incrementos $Z(x+h)-Z(x)$ não têm mais esperança zero quando $h$ aponta na direção da deriva. Note que **não adianta recorrer à hipótese intrínseca**, porque não é a exigência de variância finita que está sendo violada aqui. **Em seguida:** ou assumir **quase-estacionariedade**, restringindo a estimativa a vizinhanças móveis pequenas o bastante para que a deriva seja desprezível dentro de cada uma — o que a krigagem ordinária faz por construção (Aula 05) —, ou modelar a deriva explicitamente por krigagem universal / IRF-$k$, fora do escopo deste módulo.

**O que o exercício treina:** o erro mais comum aqui é responder "intrínseca" para o Conjunto C, por raciocinar que a hipótese mais fraca aceita mais coisas. Ela aceita mais coisas numa direção específica — variância não limitada — e em nenhuma outra. B e C falham por motivos **diferentes**, e é essa distinção que separa quem entendeu a hierarquia de quem a memorizou.

## Recap relâmpago

- Uma **variável regionalizada** tem duplo caráter: aleatório em pequena escala, estruturado em escala regional. Formaliza-se tratando o valor em cada posição como uma **função aleatória** $Z(x)$, da qual os dados observados são uma **única realização** — e é justamente por existir só uma realização que as hipóteses de estacionariedade são indispensáveis.
- **Estacionariedade de segunda ordem:** média constante **e** covariância $C(h)$ finita e bem definida (logo, variância a priori finita).
- **Hipótese intrínseca:** média constante (via incrementos de esperança zero) e $\text{Var}[Z(x+h)-Z(x)] = 2\gamma(h)$, definindo o **variograma**. É estritamente mais fraca, e a folga é **uma só**: dispensa variância a priori finita, admitindo variogramas sem patamar. Segunda ordem implica intrínseca; a recíproca é falsa.
- **Deriva não é acomodada por nenhuma das duas**, porque viola a média constante que as duas exigem. Trata-se por **quase-estacionariedade em vizinhança móvel** (o que a krigagem ordinária faz) ou por **krigagem universal / IRF-$k$**, fora do escopo aqui.

## Próxima aula

[[20-geoestatistica-aula-03-suporte-relacao-de-krige-anisotropia|Aula 03 — Suporte, relação de Krige e anisotropia]] (Parte 2 deste par) — as duas consequências práticas do modelo estabelecido aqui: por que a variância observada depende do tamanho da amostra, e por que a continuidade espacial quase nunca é a mesma em todas as direções.

## Fontes

- Matheron, G. (1963), "Principles of geostatistics", *Economic Geology*, 58(8), 1246-1266, DOI 10.2113/gsecongeo.58.8.1246 (artigo fundador, definição de variável regionalizada e função aleatória).
- Journel, A. G. & Huijbregts, C. J. (1978), *Mining Geostatistics*, Academic Press, capítulo II (teoria das variáveis regionalizadas: formalização da hipótese intrínseca e sua relação com a estacionariedade de segunda ordem).
- Isaaks, E. H. & Srivastava, R. M. (1989), *An Introduction to Applied Geostatistics*, Oxford University Press, capítulo 9 (modelos de função aleatória, realização, estacionariedade).
- Chilès, J.-P. & Delfiner, P. (2012), *Geostatistics: Modeling Spatial Uncertainty*, 2ª ed., Wiley, capítulos 1 e 2 (hierarquia das hipóteses de estacionariedade; distinção entre variância não limitada e deriva; funções aleatórias intrínsecas de ordem k).

<!--
nivel: avancado
palavras_corpo: 1960
mapa_objetivo_secao:
  geologia-avancado-m20-oa02: "O paradoxo da variável regionalizada" + "A função aleatória: tratar o desconhecido como uma família de possibilidades" + "Estacionariedade: por que repetir no espaço substitui repetir no tempo" + "Onde exatamente está a folga entre as duas hipóteses" + "E a deriva? Nenhuma das duas a acomoda" + "Exemplo trabalhado"

divisao_de_aula: 'Esta aula e a PARTE 1 da antiga Aula 02 unica (Variaveis regionalizadas e a hipotese intrinseca, 2.505 palavras de corpo, ~32 min reais, 16 conceitos novos abstratos sem nenhum apoio concreto ate o exemplo final), dividida em 2026-09-18 pela revisao didatica (achado DID-M20-A02-CARGA-001), seguindo a convencao dos Modulos 17 e 19 deste curso. A PARTE 2 e a Aula 03 (suporte, relacao de Krige e anisotropia). CORTE ESCOLHIDO: entre o modelo probabilistico (esta aula) e suas duas consequencias praticas (Parte 2). E o unico corte do material que nao parte nenhum raciocinio ao meio - as secoes "O suporte" e "Continuidade e anisotropia" USAM o modelo estabelecido aqui, mas nao o constroem. NENHUMA correcao da auditoria cientifica de 2026-09-18 foi desfeita na divisao: as tres correcoes que tocavam esta metade (a folga das hipoteses, a nao acomodacao da deriva, e a alegacao -002 reescrita) estao INTEGRALMENTE preservadas e, com o espaco da divisao, ganharam subsecao propria e um exemplo trabalhado que as exercita.'

exemplo_trabalhado_novo: 'O exemplo trabalhado desta aula foi CRIADO na divisao de 2026-09-18 (a antiga Aula 02 tinha um unico exemplo, sobre a relacao de Krige, que foi preservado palavra por palavra na Parte 2 por ser inteiramente sobre suporte). NAO CONTEM NENHUMA ALEGACAO FACTUAL NOVA: e a aplicacao classificatoria, sem qualquer valor numerico, das afirmacoes ja auditadas em GEOEST-M20-A02-HIPOTESEINTRINSECA-002 - variograma com patamar coincidente com a variancia a priori indica segunda ordem; variograma sem patamar indica variancia a priori nao finita, logo so intrinseca; deriva viola a media constante que as duas hipoteses exigem e se trata por quase-estacionariedade ou krigagem universal / IRF-k. Cada um dos tres casos reproduz uma frase ja presente no corpo, reorganizada em formato situacao-pergunta-resolucao. Nenhuma fonte nova foi consultada para constru-lo. Os nomes de deposito (porfiro de Cu, lateritico de Ni, veio epitermal de Au) sao rotulos de cenario, nao afirmacoes sobre o comportamento tipico dessas classes de deposito. Fica sinalizado para o usuario decidir se quer manda-lo ao auditor-cientifico para checagem pontual, como foi feito nos Modulos 17, 18 e 19.'

alegacoes_auditaveis:
  - claim_id: GEOEST-M20-A02-VARREGIONALIZADA-001
    claim: "A variável regionalizada, conceito formalizado por Georges Matheron a partir do trabalho pioneiro de Danie Krige na mineração sul-africana, é uma variável numérica distribuída no espaço com duplo caráter: aleatório em pequena escala e estruturado (espacialmente correlacionado) em escala regional. Formaliza-se tratando o valor da variável em cada posição como uma função aleatória Z(x), sendo os dados observados uma única realização dessa função aleatória."
    risk: fato
    source: "Matheron, G. (1963), 'Principles of geostatistics', Economic Geology, 58(8), 1246-1266, DOI 10.2113/gsecongeo.58.8.1246. Reconhecimento padrão na literatura de que a geoestatística de Matheron sistematizou o trabalho empírico anterior de D. G. Krige (mineração de ouro sul-africana, década de 1950)."
  - claim_id: GEOEST-M20-A02-HIPOTESEINTRINSECA-002
    claim: "A hipótese intrínseca exige que os incrementos Z(x+h)-Z(x) tenham média zero — o que É uma condição de média constante — e variância finita dependente apenas do vetor de separação h, definindo o variograma 2γ(h) = Var[Z(x+h)-Z(x)]. É estritamente mais fraca que a estacionariedade de segunda ordem (que exige, ADICIONALMENTE, covariância C(h) bem definida e finita para todo h, incluindo C(0)=σ² finita): toda função com covariância de segunda ordem satisfaz a hipótese intrínseca, mas o inverso não é verdadeiro. A folga entre as duas hipóteses está na DISPENSA DE VARIÂNCIA A PRIORI FINITA — a hipótese intrínseca admite fenômenos de variabilidade não limitada, cujo variograma cresce sem atingir patamar (modelos linear e de potência, comportamento browniano), para os quais C(h) não existe. A hipótese intrínseca NÃO acomoda deriva (drift): uma média que varia com a posição viola E[Z(x+h)-Z(x)]=0. Deriva se trata por quase-estacionariedade em vizinhança móvel (krigagem ordinária) ou, formalmente, por krigagem universal / funções aleatórias intrínsecas de ordem k (IRF-k)."
    risk: fato
    source: "Journel & Huijbregts (1978), Mining Geostatistics, Academic Press, capítulo II (definição formal da hipótese intrínseca e sua relação com a estacionariedade de segunda ordem); Isaaks & Srivastava (1989), An Introduction to Applied Geostatistics, capítulo 9 (modelos de função aleatória); Chilès & Delfiner (2012), Geostatistics: Modeling Spatial Uncertainty, 2ª ed., Wiley, caps. 1-2 (hierarquia de hipóteses; IRF-k). [claim reescrito na auditoria de 2026-09-18 — a versão anterior atribuía à hipótese intrínseca a tolerância a deriva, o que é incorreto: a folga é a variância não limitada]"

nota_alegacoes_migradas: 'As alegacoes GEOEST-M20-A02-RELACAOKRIGE-003 e GEOEST-M20-A02-ANISOTROPIA-004 NAO estao mais declaradas aqui: elas acompanharam o texto correspondente para a Aula 03 (Parte 2) na divisao de 2026-09-18. Os claim_id foram DELIBERADAMENTE MANTIDOS com o prefixo A02, que designa a aula pre-divisao, para nao quebrar a rastreabilidade com o manifesto 20-geoestatistica-auditoria.json, que os referencia. Nao renumerar.'
-->
