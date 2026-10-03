# Aula 01: Inteligência artificial em geociências — ramos, tipos de aprendizado, fontes e desafios dos dados geológicos

**ID:** geologia-avancado-m24-a01
**Módulo:** [[24-machine-learning-geociencias-modulo|Módulo 24 — Fundamentos e aplicações de machine learning em geociências]]
**Duração estimada:** ~27 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** situar o aprendizado de máquina dentro do campo mais amplo da inteligência artificial, distinguir os tipos de aprendizado (supervisionado, não supervisionado, por reforço) e identificar de onde vêm os dados geológicos e por que eles desafiam as premissas que a maioria dos algoritmos de aprendizado de máquina assume.
**Ao final você vai conseguir:** posicionar IA, aprendizado de máquina e aprendizado profundo como campos aninhados; distinguir aprendizado supervisionado de não supervisionado a partir da presença ou ausência de rótulo; listar as principais fontes de dados geológicos digitais; e explicar por que autocorrelação espacial, desbalanceamento de classes e escassez de rótulos são desafios recorrentes — não peculiaridades deste curso — na aplicação de aprendizado de máquina a problemas geológicos.
**Pré-requisito:** [[20-geoestatistica/20-geoestatistica-modulo|Módulo 20 — Introdução à geoestatística]] (a ideia de variável regionalizada e de amostras espacialmente correlacionadas, vista ali para a krigagem, reaparece aqui como o motivo central pelo qual dados geológicos violam a premissa de independência que o aprendizado de máquina clássico assume).

## Conteúdo

### Inteligência artificial, aprendizado de máquina e aprendizado profundo: três círculos aninhados

**Inteligência artificial (IA)** é o campo mais amplo: qualquer sistema computacional que executa tarefas normalmente associadas à cognição humana — reconhecer um padrão, tomar uma decisão, planejar uma rota. Historicamente, a IA incluiu abordagens que não aprendem com dado nenhum: um **sistema especialista** dos anos 1980, por exemplo, codifica manualmente um conjunto de regras "se-então" escritas por um geólogo (se o mineral risca o vidro e tem clivagem em duas direções a 90°, sugerir feldspato) — funciona, mas não melhora sozinho com mais exemplos, porque não há aprendizado envolvido, só regras fixas.

**Aprendizado de máquina (*machine learning*, ML)** é o subcampo da IA em que o sistema constrói sua própria regra de decisão a partir de dados, em vez de receber a regra pronta: em vez de um geólogo escrever "se dureza > 6 e clivagem ausente, então provavelmente quartzo", um algoritmo de ML recebe centenas de exemplos rotulados (medidas de dureza, clivagem, brilho, cada um com o mineral já identificado) e **infere** por conta própria o padrão que separa quartzo de outros minerais. É esse deslocamento — de "escrever a regra" para "aprender a regra a partir de exemplos" — que define o campo, e é o fio condutor deste módulo inteiro.

**Aprendizado profundo (*deep learning*, DL)**, tema da Aula 07, é um subcampo do aprendizado de máquina que usa **redes neurais artificiais** com várias camadas processando a informação em sequência, cada camada aprendendo uma representação progressivamente mais abstrata dos dados brutos — da textura de pixel de uma imagem de testemunho de sondagem até o conceito de "zona de alteração hidrotermal", sem que ninguém tenha programado manualmente o que é "textura de alteração". A relação entre os três campos é estritamente de inclusão: todo aprendizado profundo é aprendizado de máquina, todo aprendizado de máquina é inteligência artificial, mas a IA contém muito mais do que só ML (sistemas de regras, busca em grafos, lógica simbólica), e o ML contém muito mais do que só DL (regressão linear, árvores de decisão, e os métodos das Aulas 03 a 06 deste módulo, nenhum deles uma rede neural).

### Os três tipos de aprendizado

O critério que separa os principais tipos de aprendizado de máquina é simples de enunciar e decisivo na prática: **os dados de treino trazem o resultado certo anotado, ou não?**

**Aprendizado supervisionado** parte de exemplos com **rótulo** conhecido — um valor ou uma categoria que o algoritmo deve aprender a prever a partir das demais variáveis (as **feições**, ou *features*). Se o rótulo é um número contínuo (o teor de ouro em ppb de uma amostra, a porosidade de uma rocha-reservatório), a tarefa é de **regressão**. Se o rótulo é uma categoria (esta amostra é minério ou estéril; esta rocha é granito, gnaisse ou xisto), a tarefa é de **classificação**. As Aulas 03 e 04 tratam de um caso cada, porque a lógica de ajuste é a mesma — só muda o que está sendo previsto.

**Aprendizado não supervisionado** parte de dados **sem rótulo** nenhum: o algoritmo não sabe de antemão em que grupo cada amostra deveria cair, e a tarefa é descobrir estrutura escondida nos próprios dados — agrupar amostras geoquimicamente parecidas sem que ninguém tenha dito quantos grupos existem (**agrupamento**, ou *clustering*), ou resumir muitas variáveis correlacionadas num número menor de combinações que capturam a maior parte da variação (**redução de dimensionalidade**). A Aula 05 cobre os dois.

**Aprendizado por reforço** é o terceiro tipo, mencionado aqui por completude mas fora do escopo operacional deste módulo: um agente aprende por tentativa e erro, recebendo uma recompensa ou penalidade a cada ação tomada num ambiente, sem que nenhum exemplo rotulado lhe diga a ação certa de antemão — o paradigma por trás de sistemas que jogam Go ou controlam robôs. Aplicações geocientíficas existem (otimização de sequenciamento de lavra, por exemplo), mas usam uma maquinaria distinta da que este módulo constrói; os fluxos de trabalho das Aulas 02 a 07 são todos de aprendizado supervisionado ou não supervisionado.

Um quarto rótulo aparece com frequência na literatura aplicada e vale registrar: o **aprendizado semi-supervisionado**, que mistura um pequeno conjunto de dados rotulados com um conjunto grande de dados não rotulados — relevante em geociências precisamente porque rotular uma amostra geológica costuma exigir ensaio de laboratório caro (uma seção fina, uma análise química, uma datação isotópica), enquanto dados não rotulados (um levantamento aerogeofísico inteiro, por exemplo) são comparativamente baratos de coletar.

### De onde vêm os dados geológicos

Um projeto de aprendizado de máquina em geociências tipicamente combina dados de fontes heterogêneas, cada uma com sua própria resolução espacial, custo de aquisição e tipo de ruído:

- **Furos de sondagem**: testemunhos e amostras de calha com ensaios químicos, logs litológicos e geotécnicos — a fonte mais direta de dados "verdade de campo" (*ground truth*), mas também a mais cara por ponto amostrado, o que limita fortemente o tamanho dos conjuntos de dados rotulados (retomado na Aula 02, e já visto sob outro ângulo no Módulo 20 como o insumo bruto da krigagem).
- **Geofísica** (aerogeofísica, sísmica, geofísica terrestre): campos de magnetometria, gamaespectrometria, gravimetria ou seções sísmicas cobrem áreas extensas de forma relativamente barata por unidade de área, mas medem uma propriedade física indireta (densidade, suscetibilidade magnética), não a litologia ou o teor diretamente — os Módulos 15 a 19 deste curso tratam dessas técnicas em detalhe.
- **Sensoriamento remoto**: imagens multiespectrais e hiperespectrais de satélite ou aerotransportadas, usadas para mapear alteração hidrotermal, litologia superficial e estruturas — tema do Módulo 14 e retomado no Módulo 25 sob a ótica de aquisição digital.
- **Petrografia e mineralogia digital**: imagens de seção fina, MEV (microscopia eletrônica de varredura) e QEMSCAN/MLA, cada vez mais processadas por visão computacional em vez de contagem manual de pontos.
- **Bancos de dados públicos e literatura**: catálogos geocronológicos, bases isotópicas, mapas geológicos digitalizados e compilações regionais — volumosos, mas de qualidade e metadados heterogêneos entre fontes.

### Por que dados geológicos desafiam as premissas do aprendizado de máquina

A maioria dos algoritmos de aprendizado de máquina — incluindo praticamente todos os usados neste módulo — foi desenvolvida sob uma premissa estatística confortável: as amostras de treino são **independentes e identicamente distribuídas** (i.i.d.), isto é, cada amostra é extraída aleatoriamente da mesma distribuição, sem relação com as demais. Dados geológicos violam essa premissa de forma sistemática, por pelo menos três razões que vão reaparecer ao longo do módulo:

**Autocorrelação espacial.** Duas amostras de furos de sondagem próximas entre si tendem a se parecer mais do que duas amostras distantes — é exatamente a ideia de **variável regionalizada** e de **continuidade espacial** que o Módulo 20 formalizou por meio do variograma. Isso tem uma consequência direta e traiçoeira para o aprendizado de máquina: se um conjunto de dados é dividido aleatoriamente em treino e teste (a prática padrão, coberta na Aula 02) e duas amostras vizinhas — quase-duplicatas espaciais uma da outra — caem uma no treino e outra no teste, o modelo não está sendo testado em dado genuinamente novo: parte da informação "vazou" do treino para o teste através da proximidade espacial, e a métrica de desempenho medida no teste fica artificialmente otimista. A Aula 02 volta a este ponto na hora de particionar os dados, e a Aula 06 o retoma ao discutir validação.

**Escassez e custo de rótulos.** Como cada rótulo confiável em geociências normalmente vem de um ensaio caro (análise química, datação, laminação e descrição petrográfica), os conjuntos de dados rotulados costumam ser pequenos — dezenas a poucas centenas de amostras é comum, ordens de grandeza abaixo dos milhões de exemplos rotineiros em aplicações de ML de imagem ou texto. Modelos com muitos parâmetros (em especial redes neurais profundas, Aula 07) sofrem mais com essa escassez, porque têm capacidade de memorizar o pequeno conjunto de treino em vez de generalizar — o fenômeno de **sobreajuste** (*overfitting*) que a Aula 06 formaliza e mede.

**Classes desbalanceadas.** Em problemas de classificação geológica de interesse econômico ou ambiental — depósito mineral contra rocha estéril, zona de risco geotécnico contra zona estável — a classe de interesse é tipicamente rara: a maior parte de qualquer área é estéril, e só uma fração pequena hospeda mineralização. Um classificador que simplesmente prevê "estéril" para toda amostra pode alcançar 90% ou mais de acurácia global sem identificar um único depósito real — a acurácia, sozinha, é uma métrica enganosa nesse cenário, e a Aula 06 apresenta as métricas (precisão, revocação, F1) desenhadas especificamente para não se deixar enganar por esse desbalanceamento.

Um quarto ponto, mais sutil e que a Aula 02 detalha na prática: a amostragem geológica raramente é aleatória no sentido estatístico. Furos de sondagem se concentram onde já há indício de mineralização — um **viés de amostragem preferencial** que, se ignorado, faz o modelo aprender menos sobre onde não olhar do que sobre onde já se sabia olhar.

## Exemplo trabalhado

**Situação:** um geólogo de exploração tem três tarefas diferentes pela frente e precisa decidir, para cada uma, que tipo de aprendizado de máquina se aplica.

**Tarefa A.** A empresa tem 80 amostras de solo com teores de Cu, As e Zn medidos em laboratório, e quer prever o teor de Au (ouro, em ppb) — não medido em todas as amostras por causa do custo do ensaio — a partir dos elementos já disponíveis.

**Tarefa B.** A mesma empresa tem 300 amostras de rocha com composição geoquímica multielementar completa, sem nenhuma classificação litológica atribuída, e quer identificar se existem agrupamentos geoquimicamente distintos que possam corresponder a diferentes unidades ou fácies de alteração.

**Tarefa C.** Um banco de 500 fotografias de testemunho de sondagem já rotuladas manualmente por um geólogo sênior como "mineralizado" ou "estéril" está disponível, e a empresa quer treinar um sistema que classifique automaticamente novas fotos.

**Resolução.**

Tarefa A: o rótulo (Au, um número contínuo) existe para pelo menos parte dos dados, e o objetivo é prevê-lo a partir de outras variáveis — **aprendizado supervisionado, tarefa de regressão** (retomada com um caso muito parecido na Aula 03).

Tarefa B: não há rótulo nenhum — nenhuma amostra chega com uma etiqueta de "grupo" ou "fácies" pré-definida, e o objetivo é justamente descobrir se agrupamentos existem — **aprendizado não supervisionado, tarefa de agrupamento** (a Aula 05 desenvolve esse exato cenário, com dados geoquímicos multielementares).

Tarefa C: cada foto já vem com um rótulo categórico atribuído por um especialista (mineralizado/estéril), e o objetivo é aprender a prever esse rótulo em fotos novas — **aprendizado supervisionado, tarefa de classificação**. Dado o volume de imagens e a natureza visual do problema, essa tarefa é também uma boa candidata a **aprendizado profundo** (Aula 07): redes neurais convolucionais são a arquitetura clássica para classificação de imagem e seguem sendo a escolha padrão quando o conjunto de imagens rotuladas é pequeno — o regime típico em geociências —, ainda que, desde o início da década de 2020, os *vision transformers* tenham assumido a liderança nos grandes referenciais de classificação de imagem, onde há dados de treino em escala suficiente para sustentá-los. Em qualquer dos dois casos o contraste com as Tarefas A e B se mantém: dados tabulares (poucas colunas numéricas) costumam funcionar tão bem ou melhor com os métodos mais simples das Aulas 03 a 05 — um ponto que a Aula 07 discute explicitamente ao comparar desempenho.

## Recap relâmpago

- **IA ⊃ aprendizado de máquina (ML) ⊃ aprendizado profundo (DL)**: três campos aninhados, não sinônimos. ML é o subcampo em que o sistema aprende a regra de decisão a partir de dados, em vez de recebê-la pronta; DL é o subcampo de ML que usa redes neurais de várias camadas.
- Os dois tipos de aprendizado que este módulo cobre operacionalmente: **supervisionado** (dados com rótulo conhecido — regressão para rótulo contínuo na Aula 03, classificação para rótulo categórico na Aula 04) e **não supervisionado** (dados sem rótulo — agrupamento e redução de dimensionalidade, Aula 05). Aprendizado por reforço e semi-supervisionado existem e foram situados, mas ficam fora do escopo operacional.
- Dados geológicos vêm de fontes heterogêneas — sondagem, geofísica, sensoriamento remoto, petrografia digital, bancos públicos — cada uma com sua resolução, custo e tipo de ruído próprios.
- Três desafios recorrentes violam a premissa de independência que a maioria dos algoritmos assume: **autocorrelação espacial** (amostras vizinhas se parecem, e um particionamento aleatório ingênuo vaza informação do treino para o teste), **escassez de rótulos** (ensaios caros produzem conjuntos de dados pequenos, favorecendo sobreajuste) e **classes desbalanceadas** (a classe de interesse econômico costuma ser rara, tornando a acurácia global uma métrica enganosa). Um quarto ponto — a amostragem preferencial em áreas de interesse — soma-se aos três.

## Próxima aula

[[24-machine-learning-geociencias-aula-02-fluxo-trabalho-python-preparacao-exploracao-particionamento|Aula 02 — Fluxo de trabalho em Python: objetivo, coleta, preparação, análise exploratória e particionamento dos dados]] — onde as advertências desta aula sobre particionamento e amostragem preferencial se tornam decisões concretas de código sobre um conjunto de dados geoquímicos.

## Fontes

- Panorama do aprendizado de máquina aplicado a geociências sólidas, incluindo os desafios específicos de dados geológicos (autocorrelação espacial, escassez de rótulos, heterogeneidade de fonte): Bergen, K. J., Johnson, P. A., de Hoop, M. V. & Beroza, G. C. (2019), "Machine learning for data-driven discovery in solid Earth geoscience", *Science*, 363(6433), eaau0323, DOI 10.1126/science.aau0323.
- Taxonomia padrão de aprendizado supervisionado, não supervisionado e por reforço, e a relação de inclusão entre IA, aprendizado de máquina e aprendizado profundo: Goodfellow, I., Bengio, Y. & Courville, A., *Deep Learning* (2016), MIT Press, cap. 1; Géron, A., *Hands-On Machine Learning with Scikit-Learn, Keras and TensorFlow*, 3ª ed. (2022), O'Reilly, cap. 1.
- Posição atual das redes convolucionais frente aos *vision transformers* em classificação de imagem — ViT liderando os referenciais de larga escala, CNN mantendo vantagem em conjuntos pequenos: Dosovitskiy, A. et al. (2021), "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale", *ICLR*, arXiv:2010.11929.
- Risco de vazamento de informação em validação cruzada e particionamento de dados com estrutura espacial, temporal ou hierárquica: Roberts, D. R. et al. (2017), "Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure", *Ecography*, 40(8), 913-929, DOI 10.1111/ecog.02881.

<!--
nivel: avancado
palavras_corpo: 2153
mapa_objetivo_secao:
  geologia-avancado-m24-oa01: "Inteligência artificial, aprendizado de máquina e aprendizado profundo: três círculos aninhados" + "Os três tipos de aprendizado" + "De onde vêm os dados geológicos" + "Por que dados geológicos desafiam as premissas do aprendizado de máquina" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: MLGEO-M24-A01-TAXONOMIA-IA-ML-DL-001
    claim: "Inteligencia artificial, aprendizado de maquina e aprendizado profundo formam uma relacao estrita de inclusao (IA contem ML, que contem DL): aprendizado de maquina e o subcampo da IA em que o sistema infere a regra de decisao a partir de dados em vez de receber uma regra codificada manualmente (como em um sistema especialista baseado em regras), e aprendizado profundo e o subcampo de ML que usa redes neurais artificiais de multiplas camadas para aprender representacoes progressivamente mais abstratas dos dados brutos."
    risk: fato
    source: "Goodfellow, I., Bengio, Y. & Courville, A., Deep Learning (2016), MIT Press, cap. 1; Geron, A., Hands-On Machine Learning with Scikit-Learn, Keras and TensorFlow, 3a ed. (2022), O'Reilly, cap. 1."
  - claim_id: MLGEO-M24-A01-TIPOS-APRENDIZADO-002
    claim: "O criterio central que distingue aprendizado supervisionado de nao supervisionado e a presenca ou ausencia de rotulo nos dados de treino: supervisionado usa dados rotulados para regressao (rotulo continuo) ou classificacao (rotulo categorico); nao supervisionado usa dados sem rotulo para agrupamento (clustering) ou reducao de dimensionalidade; aprendizado por reforco usa um sinal de recompensa obtido por tentativa e erro em vez de exemplos rotulados; aprendizado semi-supervisionado combina um conjunto pequeno de dados rotulados com um conjunto grande de dados nao rotulados."
    risk: fato
    source: "Geron, A., Hands-On Machine Learning with Scikit-Learn, Keras and TensorFlow, 3a ed. (2022), O'Reilly, cap. 1; Hastie, T., Tibshirani, R. & Friedman, J., The Elements of Statistical Learning, 2a ed. (2009), Springer, cap. 1 e 14."
  - claim_id: MLGEO-M24-A01-DESAFIOS-DADOS-GEOLOGICOS-003
    claim: "Dados geologicos tipicamente violam a premissa de amostras independentes e identicamente distribuidas (i.i.d.) que a maioria dos algoritmos classicos de aprendizado de maquina assume, por razoes que incluem autocorrelacao espacial entre amostras proximas, escassez de dados rotulados (por causa do custo de ensaios laboratoriais e de campo) favorecendo sobreajuste em modelos com muitos parametros, classes fortemente desbalanceadas em problemas de interesse economico ou ambiental (tornando a acuracia global uma metrica enganosa), e amostragem preferencial em areas de interesse geologico previo em vez de amostragem aleatoria."
    risk: fato
    source: "Bergen, K. J., Johnson, P. A., de Hoop, M. V. & Beroza, G. C. (2019), 'Machine learning for data-driven discovery in solid Earth geoscience', Science, 363(6433), eaau0323, DOI 10.1126/science.aau0323."
  - claim_id: MLGEO-M24-A01-VALIDACAO-CRUZADA-ESPACIAL-004
    claim: "Quando os dados tem estrutura espacial, temporal, hierarquica ou filogenetica, um particionamento aleatorio ingenuo em treino e teste pode permitir vazamento de informacao entre os dois conjuntos por meio de amostras proximas/relacionadas caindo em conjuntos diferentes, inflando artificialmente o desempenho estimado; estrategias de validacao cruzada com blocos ou agrupamentos que respeitam essa estrutura (por exemplo, blocagem espacial) sao recomendadas para obter uma estimativa de desempenho mais realista."
    risk: fato
    source: "Roberts, D. R. et al. (2017), 'Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure', Ecography, 40(8), 913-929, DOI 10.1111/ecog.02881."
  - claim_id: MLGEO-M24-A01-EXEMPLO-CLASSIFICACAO-TAREFAS-005
    claim: "Um problema de previsao de uma variavel numerica continua (teor de ouro) a partir de outras variaveis medidas e uma tarefa de aprendizado supervisionado de regressao; um problema de descoberta de agrupamentos em dados geoquimicos sem nenhum rotulo previo e uma tarefa de aprendizado nao supervisionado de agrupamento; um problema de previsao de uma categoria (mineralizado/esteril) a partir de dados ja rotulados por um especialista e uma tarefa de aprendizado supervisionado de classificacao, e classificacao de imagem em grande volume e um cenario tipico onde redes neurais profundas (aprendizado profundo) tendem a superar metodos classicos, ao contrario de problemas tabulares com poucas colunas numericas."
    risk: fato
    source: "Geron, A., Hands-On Machine Learning with Scikit-Learn, Keras and TensorFlow, 3a ed. (2022), O'Reilly, cap. 1 e 10 (comparacao de desempenho entre modelos classicos e redes neurais em dados tabulares versus dados de imagem)."
  - claim_id: MLGEO-M24-A01-CNN-VIT-ESTADO-ARTE-006
    claim: "As redes neurais convolucionais (CNN) sao a arquitetura classica de classificacao de imagem e permanecem a escolha padrao quando o conjunto de imagens rotuladas e pequeno, mas desde o inicio da decada de 2020 nao sao mais, sozinhas, o estado da arte: os vision transformers (ViT) lideram os grandes referenciais de classificacao de imagem (ImageNet) quando ha dados de treino em escala suficiente, enquanto CNNs mantem vantagem em conjuntos pequenos e em cenarios de custo computacional restrito."
    risk: fato
    source: "Dosovitskiy, A. et al. (2021), 'An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale', ICLR, arXiv:2010.11929; levantamentos comparativos correntes CNN x ViT em classificacao de imagem (2025-2026), que registram a lideranca dos ViT nos referenciais de larga escala e a vantagem persistente das CNN em conjuntos de dados pequenos. ACHADO 9 DA AUDITORIA de 2026-09-20 (desatualizacao corrigida)."
-->
