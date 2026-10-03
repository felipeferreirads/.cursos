# Aula 05: Processamento digital de imagens II: transformações multivariadas e classificação supervisionada e não supervisionada

**ID:** geologia-avancado-m14-a05
**Módulo:** [[14-sensoriamento-remoto-modulo|Módulo 14 — Sensoriamento remoto]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** apresentar as técnicas que tratam todas as bandas de uma imagem em conjunto — a Análise de Componentes Principais como redutora de redundância espectral, e a classificação de imagens (supervisionada e não supervisionada) como o processo de converter pixels em categorias temáticas.
**Ao final você vai conseguir:** explicar o que a Análise de Componentes Principais faz com um conjunto de bandas correlacionadas e por que isso ajuda a realçar informação geológica; distinguir classificação supervisionada de não supervisionada e escolher qual usar conforme o conhecimento prévio disponível; e interpretar uma matriz de confusão para avaliar a acurácia de uma classificação.
**Pré-requisito:** [[14-sensoriamento-remoto-aula-04-pdi-i-realces-operacoes-aritmeticas-filtros|Aula 04]] — pressupõe os conceitos de valor digital, histograma e razão de bandas já estabelecidos.

## Conteúdo

### Por que tratar as bandas em conjunto, e não uma a uma

A Aula 04 tratou cada banda (ou par de bandas, nas razões) isoladamente. Mas um sensor multiespectral como o Landsat entrega 11 bandas simultâneas do mesmo pixel — e essas bandas, por medirem o mesmo alvo físico em faixas espectrais próximas, tendem a estar fortemente **correlacionadas** entre si: um pixel de solo exposto, por exemplo, tende a ser relativamente claro em quase todas as bandas do visível ao SWIR, porque a maior parte da variação de brilho entre pixels vem de um fator comum — iluminação, albedo geral do material, umidade — que afeta várias bandas ao mesmo tempo, e não da diferença espectral fina entre elas. Essa redundância tem dois custos práticos: desperdiça capacidade de armazenamento e processamento (várias bandas carregando informação parecida) e, pior, esconde a informação realmente diferenciadora — a variação sutil entre bandas — atrás da variação dominante e comum a todas. As técnicas desta aula respondem a dois problemas distintos gerados por essa situação: como comprimir e realçar a informação não redundante (Análise de Componentes Principais) e como transformar toda essa informação combinada em categorias temáticas úteis a um mapa (classificação).

### Análise de Componentes Principais: reorganizando a informação por importância

A **Análise de Componentes Principais** (ACP, ou PCA na sigla em inglês) é uma transformação matemática que converte um conjunto de bandas originais, correlacionadas entre si, num novo conjunto de bandas — as **componentes principais** — que são estatisticamente não correlacionadas (ortogonais) e ordenadas por quanto da variância total do conjunto de dados original cada uma explica.

A mecânica, em termos conceituais (sem entrar no cálculo de autovalores e autovetores da matriz de covariância, que foge do escopo desta aula): a **primeira componente principal** (PC1) é construída de forma a capturar a maior fração possível da variância total presente em todas as bandas originais — na prática, para a maioria das imagens ópticas de sensoriamento remoto, essa primeira componente costuma corresponder aproximadamente ao "brilho geral" da cena, porque é exatamente esse fator comum de iluminação/albedo, mencionado na seção anterior, que domina a variância compartilhada entre bandas. A **segunda componente** (PC2) captura a maior fração possível da variância **restante**, sob a restrição adicional de ser estatisticamente não correlacionada com a PC1 — e assim por diante, cada componente subsequente explicando cada vez menos variância total.

O valor prático para geologia está justamente nas componentes **posteriores** à primeira: como a PC1 absorve o fator dominante de brilho/iluminação (frequentemente pouco diagnóstico de composição), as componentes de ordem mais alta (PC2, PC3, às vezes PC4) costumam concentrar justamente as diferenças espectrais mais sutis entre materiais — exatamente o tipo de informação que interessa para diferenciar litologias ou realçar alteração hidrotermal, que a Aula 03 mostrou depender de feições de absorção estreitas, um sinal fraco frente à variação dominante de brilho. Uma técnica derivada e muito usada em exploração mineral é a **ACP seletiva** (ou *feature-oriented PCA*, ACP orientada a feição): em vez de rodar a transformação sobre todas as bandas do sensor, seleciona-se deliberadamente um subconjunto pequeno de bandas (por exemplo, apenas as bandas SWIR que contêm as feições diagnósticas de um argilomineral específico, como visto na Aula 03) antes de aplicar a ACP — isso concentra a transformação exatamente onde a informação mineral relevante está, produzindo uma componente que realça esse mineral especificamente, de forma muito mais direcionada do que uma ACP sobre todas as bandas do sensor de uma vez.

Vale registrar uma ressalva importante sobre interpretação: **qual componente captura qual informação não é fixo nem previsível de antemão** — depende inteiramente da cena específica (cobertura de vegetação, tipos de solo e rocha presentes, condições de iluminação daquela data) e precisa ser verificado caso a caso, tipicamente examinando a "carga" (o peso) de cada banda original em cada componente resultante, e não simplesmente assumido a partir de exemplos de outros trabalhos.

### Classificação de imagens: de valor digital a categoria temática

**Classificação de imagens** é o processo de atribuir a cada pixel de uma imagem multiespectral (ou às suas componentes principais, ou a um conjunto de índices derivados) uma categoria discreta de interesse — tipos de cobertura da terra, classes litológicas, classes de uso do solo — com base no seu comportamento espectral em todas as bandas usadas como entrada. O resultado é um mapa temático: uma imagem onde cada pixel não representa mais um brilho contínuo, e sim um rótulo de classe.

O espaço conceitual em que a classificação opera é o **espaço de atributos espectrais** (ou espaço de *features*): cada pixel, com seus valores em N bandas, é um ponto num espaço N-dimensional, e pixels de materiais espectralmente parecidos tendem a se agrupar (formar "nuvens" ou *clusters*) nesse espaço. Toda técnica de classificação, no fundo, é um método de particionar esse espaço N-dimensional em regiões, cada uma associada a uma classe.

**Classificação não supervisionada** não usa nenhum conhecimento prévio sobre as classes — o algoritmo agrupa os pixels automaticamente, com base apenas na similaridade espectral entre eles, em um número de agrupamentos (*clusters*) definido a priori pelo analista (por exemplo, "encontre 10 agrupamentos nesta cena"). O algoritmo mais comum, **K-means**, funciona de forma iterativa: começa com K centros de agrupamento posicionados (aleatoriamente ou por alguma heurística inicial), atribui cada pixel ao centro mais próximo no espaço de atributos, recalcula cada centro como a média dos pixels a ele atribuídos, e repete esse ciclo até que as atribuições estabilizem (deixem de mudar significativamente entre iterações sucessivas). O resultado é um mapa de agrupamentos espectrais — mas, e este é o ponto crucial, **os agrupamentos não vêm rotulados com nome de classe geológica nenhuma**: cabe ao analista, depois de rodar o algoritmo, examinar cada agrupamento (por sua localização, sua assinatura espectral média, seu contexto no terreno, eventualmente confirmação de campo) e decidir a que classe temática real (por exemplo, "afloramento de granito", "solo residual", "vegetação de cerrado") cada agrupamento corresponde — um processo chamado de rotulação pós-classificação. A classificação não supervisionada é útil quando não se tem amostras de treinamento confiáveis disponíveis, ou como etapa exploratória inicial para entender a variabilidade espectral de uma área pouco conhecida.

**Classificação supervisionada**, ao contrário, começa com conhecimento prévio: o analista define **áreas de treinamento** (*training samples*, também chamadas de amostras de referência) — polígonos ou pontos na imagem cuja classe verdadeira já é conhecida, por trabalho de campo, mapas geológicos existentes, ou interpretação visual confiável — e o algoritmo aprende, a partir da assinatura espectral dessas áreas conhecidas, a regra de decisão que separa uma classe de outra no espaço de atributos, aplicando depois essa regra a todos os demais pixels da imagem. Entre os classificadores supervisionados clássicos, o de **Máxima Verossimilhança** (*Maximum Likelihood*) modela estatisticamente a distribuição espectral de cada classe (tipicamente assumindo distribuição normal multivariada, estimada a partir das amostras de treinamento) e atribui cada pixel novo à classe cuja distribuição estatística torna aquele valor observado mais provável — um método clássico, bem estabelecido, mas sensível à qualidade e à representatividade das amostras de treinamento, e à validade da suposição de normalidade. Classificadores mais modernos, como **Máquinas de Vetores de Suporte** (SVM) e classificadores baseados em **árvores de decisão e florestas aleatórias** (*Random Forest*), fazem menos suposições sobre a distribuição estatística dos dados e frequentemente superam a Máxima Verossimilhança em cenas complexas — sem, no entanto, eliminar a dependência fundamental de boas amostras de treinamento, que continua sendo o fator que mais determina a qualidade do resultado final, em qualquer dos métodos. Esse é um tema que reaparece com mais profundidade adiante no curso, no módulo de aprendizado de máquina aplicado a geociências.

### Avaliando a qualidade de uma classificação: a matriz de confusão

Uma classificação — supervisionada ou não — sempre erra em algum grau: pixels de uma classe são inevitavelmente rotulados como outra, seja por ambiguidade espectral genuína entre materiais parecidos (dois tipos de solo com composição próxima, por exemplo), seja por mistura espectral dentro de um único pixel (um pixel de borda entre duas classes, cujo valor médio não representa bem nenhuma das duas — o chamado problema do **pixel misto**, mais grave quanto mais grosseira a resolução espacial em relação ao tamanho dos objetos mapeados). Avaliar objetivamente esse erro é indispensável antes de usar o resultado para qualquer decisão prática.

A ferramenta padrão é a **matriz de confusão** (também chamada matriz de erro): uma tabela que cruza a classe atribuída pelo classificador (nas linhas ou colunas, por convenção) com a classe verdadeira, verificada de forma independente por um conjunto de **amostras de validação** (distintas das amostras de treinamento usadas para construir o classificador — usar as mesmas amostras para treinar e validar infla artificialmente a acurácia aparente, um erro metodológico grave e recorrente). Da matriz de confusão derivam-se métricas-padrão: a **acurácia global** (proporção total de pixels de validação corretamente classificados, soma da diagonal da matriz dividida pelo total), a **acurácia do produtor** (para uma classe específica, a proporção dos pixels verdadeiramente daquela classe que foram corretamente identificados como tal — mede omissão) e a **acurácia do usuário** (para uma classe específica, a proporção dos pixels que o classificador rotulou como daquela classe que realmente são daquela classe — mede inclusão indevida, ou comissão). O coeficiente **Kappa**, derivado também da matriz de confusão, ajusta a acurácia global descontando a concordância que ocorreria apenas por acaso — uma classificação com muitas classes e proporções desiguais entre elas pode ter acurácia global aparentemente alta apenas por acertar bem a classe mais numerosa, e o Kappa se propõe a penalizar esse efeito.

Sobre o Kappa, porém, é preciso registrar que **a área está dividida**, e um leitor que encontre só um dos lados vai interpretar mal metade dos artigos que ler. De um lado, a referência-padrão de avaliação de acurácia temática (Congalton & Green) segue ensinando e recomendando o Kappa, e ele continua sendo reportado em cerca de metade da literatura recente. De outro, um conjunto influente de trabalhos argumenta que ele deveria ser abandonado: Pontius & Millones (2011, no artigo de título deliberadamente provocativo *Death to Kappa*) sustentam que a linha de base de "acaso" que o Kappa usa é arbitrária e pouco informativa, e propõem substituí-lo por duas medidas mais diretamente interpretáveis — **desacordo de quantidade** e **desacordo de alocação** —, e Foody (2020) argumenta que o Kappa é inadequado especificamente para *comparar* a acurácia de mapas temáticos diferentes. Não há consenso fechado. A postura defensável na prática é: reporte sempre a matriz de confusão completa e as acurácias de produtor e usuário por classe (que ninguém disputa), e trate o Kappa como número de contexto, não como o veredito sobre a qualidade do mapa.

## Exemplo trabalhado

**Situação:** um projeto de mapeamento litológico produz uma classificação supervisionada de três classes (granito, xisto, cobertura de solo/vegetação) sobre uma cena com 300 pixels de validação independentes, coletados em campo após a classificação. A matriz de confusão resultante é:

| Verdadeiro \ Classificado | Granito | Xisto | Solo/veg. | Total verdadeiro |
|---|---|---|---|---|
| Granito | 80 | 15 | 5 | 100 |
| Xisto | 10 | 70 | 20 | 100 |
| Solo/veg. | 5 | 5 | 90 | 100 |
| Total classificado | 95 | 90 | 115 | 300 |

Calcule a acurácia global, a acurácia do produtor e do usuário para a classe Xisto, e interprete o que esses números dizem sobre a confiabilidade prática do mapa.

**Resolução:**

*Acurácia global* = soma da diagonal (pixels corretamente classificados em cada classe) / total de pixels de validação = (80 + 70 + 90) / 300 = 240 / 300 = **80%**. Globalmente, 8 em cada 10 pixels de validação foram classificados corretamente.

*Acurácia do produtor, classe Xisto* = pixels verdadeiramente Xisto corretamente classificados como Xisto / total de pixels verdadeiramente Xisto = 70 / 100 = **70%**. Isso significa que, de todo o xisto real presente em campo, o classificador só identificou corretamente 70% — os outros 30% (10 confundidos com granito, 20 confundidos com solo/vegetação) foram **omitidos** da classe xisto no mapa final, um problema de **omissão**.

*Acurácia do usuário, classe Xisto* = pixels verdadeiramente Xisto entre os classificados como Xisto / total de pixels classificados como Xisto = 70 / 90 = **77,8%**. Isso significa que, de todo pixel que o mapa rotula como "xisto", só 77,8% realmente é xisto em campo — os outros 22,2% (15 pixels na verdade de granito, 5 de solo/vegetação) foram **incluídos indevidamente** na classe xisto, um problema de **comissão**, distinto do anterior.

*Interpretação prática:* a acurácia global de 80% pode parecer satisfatória isoladamente, mas esconde uma fraqueza específica e importante — a classe xisto tem tanto omissão (30%) quanto comissão (22,2%) consideráveis, bem piores do que granito e solo/vegetação (que têm acurácias mais altas, verificáveis pelo mesmo cálculo). Um geólogo que confiasse apenas na acurácia global concluiria "o mapa está bom"; olhando a matriz de confusão completa, a conclusão correta e mais útil é: "o mapa é confiável para diferenciar granito e cobertura de solo/vegetação, mas o contorno da unidade de xisto precisa de verificação de campo adicional antes de ser usado para qualquer decisão — sobretudo nas bordas de contato com granito, onde a confusão entre as duas classes é mais provável". É exatamente esse tipo de leitura granular, classe por classe, que a matriz de confusão fornece e que a acurácia global, sozinha, esconde.

## Erros comuns

- **Assumir que a PC2 (ou qualquer componente) sempre representa a mesma informação de uma cena para outra.** A própria aula avisa: qual componente captura o quê depende da cena específica e precisa ser verificado caso a caso, examinando as cargas de banda — nunca herdado de outro trabalho sem checagem.
- **Confiar só na acurácia global para julgar um mapa temático.** Como o exemplo trabalhado mostra, 80% de acurácia global esconde uma classe (xisto) com 30% de omissão e 22,2% de comissão — a leitura correta exige a matriz de confusão completa, classe por classe.
- **Validar uma classificação com as mesmas amostras usadas para treiná-la.** A aula chama isso de erro metodológico grave e recorrente — infla artificialmente a acurácia aparente porque o classificador está sendo testado exatamente onde já "viu a resposta".
- **Tratar o coeficiente Kappa como veredito definitivo sobre a qualidade de um mapa.** A área está genuinamente dividida (Congalton & Green o mantêm; Pontius & Millones e Foody defendem abandoná-lo) — a postura defensável é reportar a matriz completa e tratar o Kappa como número de contexto, não conclusão.

## O que não concluir

- **Que classificação não supervisionada dispensa conhecimento de campo.** Ela dispensa amostras de treinamento prévias, mas a rotulação pós-classificação — decidir que agrupamento espectral corresponde a qual classe geológica real — ainda exige esse conhecimento, só que depois de rodar o algoritmo, não antes.
- **Que um classificador mais moderno (SVM, Random Forest) elimina a dependência de boas amostras de treinamento.** Reduz suposições sobre distribuição estatística dos dados, mas a qualidade das amostras continua sendo o fator que mais determina o resultado final, em qualquer método.
- **Que pixel misto é um problema que desaparece com mais bandas ou melhor algoritmo.** É uma limitação da resolução espacial em relação ao tamanho dos objetos mapeados — só resolução espacial mais fina (ou aceitar a mistura como parte da interpretação) resolve, não a escolha de classificador.

## Recap relâmpago

- Bandas de um sensor multiespectral são frequentemente correlacionadas entre si (um fator comum de brilho/iluminação domina a variância compartilhada), o que motiva técnicas que tratam todas as bandas em conjunto, em vez de uma a uma.
- A Análise de Componentes Principais (ACP) reorganiza bandas correlacionadas em componentes não correlacionadas e ordenadas por variância explicada; a PC1 tipicamente captura brilho geral, enquanto componentes de ordem mais alta (PC2, PC3) costumam concentrar diferenças espectrais sutis mais úteis para diferenciar litologia ou alteração — mas qual componente captura o quê precisa ser verificado caso a caso, não é fixo.
- ACP seletiva (aplicada só a um subconjunto de bandas relevantes a um mineral-alvo) concentra a transformação onde a informação diagnóstica está, sendo mais direcionada que uma ACP sobre todas as bandas do sensor.
- Classificação não supervisionada (K-means) agrupa pixels por similaridade espectral sem conhecimento prévio de classe, exigindo rotulação pós-classificação; classificação supervisionada (Máxima Verossimilhança, SVM, Random Forest) usa amostras de treinamento com classe conhecida para aprender a regra de decisão — a qualidade das amostras de treinamento determina, em qualquer método, a qualidade do resultado.
- A matriz de confusão cruza classe atribuída com classe verdadeira (verificada por amostras de validação independentes das de treinamento) e permite calcular acurácia global, acurácia do produtor (mede omissão) e acurácia do usuário (mede comissão) por classe; o coeficiente Kappa ajusta a acurácia global descontando concordância ao acaso — mas é objeto de divergência real na área (Congalton & Green o mantêm; Pontius & Millones 2011 e Foody 2020 defendem abandoná-lo em favor de desacordo de quantidade e de alocação), e não deve ser tratado como o veredito único sobre um mapa.
- Acurácia global alta pode esconder desempenho ruim numa classe específica — a leitura completa da matriz de confusão, classe por classe, é o que determina se um mapa temático é confiável o bastante para uma decisão prática.

## Próxima aula

[[14-sensoriamento-remoto-aula-06-sensoriamento-remoto-ativo-radar-sar-insar-lidar|Aula 06 — Sensoriamento remoto ativo: Radar/SAR, InSAR e LiDAR]] — até aqui o módulo tratou exclusivamente de sensores passivos ópticos; a próxima aula muda de mecanismo físico inteiramente, entrando nos sensores ativos que emitem sua própria energia.

## Fontes

- Richards, J. A. (2022), *Remote Sensing Digital Image Analysis*, 6ª ed., Springer, cap. 6 e 8 (Análise de Componentes Principais, classificação supervisionada e não supervisionada).
- Jensen, J. R. (2016), *Introductory Digital Image Processing: A Remote Sensing Perspective*, 4ª ed., Pearson, cap. 8-9 (ACP, K-means, Máxima Verossimilhança, avaliação de acurácia).
- Congalton, R. G. & Green, K. (2019), *Assessing the Accuracy of Remotely Sensed Data: Principles and Practices*, 3ª ed., CRC Press (matriz de confusão, acurácia do produtor/usuário, coeficiente Kappa — referência padrão da área, e o lado que mantém o Kappa).
- Pontius Jr., R. G. & Millones, M. (2011), "Death to Kappa: birth of quantity disagreement and allocation disagreement for accuracy assessment", *International Journal of Remote Sensing*, 32(15), p. 4407-4429 (o lado que defende abandonar o Kappa).
- Foody, G. M. (2020), "Explaining the unsuitability of the kappa coefficient in the assessment and comparison of the accuracy of thematic maps obtained by image classification", *Remote Sensing of Environment*, 239 (crítica dirigida ao uso comparativo do Kappa).
- Loughlin, W. P. (1991), "Principal component analysis for alteration mapping", *Photogrammetric Engineering and Remote Sensing*, 57(9) (ACP seletiva/orientada a feição, aplicação em exploração mineral).

<!--
nivel: avancado
palavras_corpo: 2483
mapa_objetivo_secao:
  geologia-avancado-m14-oa03: "Por que tratar as bandas em conjunto, e não uma a uma" + "Análise de Componentes Principais: reorganizando a informação por importância" + "Classificação de imagens: de valor digital a categoria temática" + "Avaliando a qualidade de uma classificação: a matriz de confusão" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: SENSREM-M14-A05-ACP-001
    claim: "A Análise de Componentes Principais transforma um conjunto de bandas correlacionadas em componentes principais estatisticamente não correlacionadas (ortogonais) e ordenadas por fração de variância total explicada; em imagens ópticas de sensoriamento remoto, a primeira componente (PC1) tipicamente captura o fator dominante de brilho geral/iluminação, enquanto componentes de ordem mais alta tendem a concentrar diferenças espectrais mais sutis entre materiais."
    risk: aproximacao
    source: "Richards 2022, Remote Sensing Digital Image Analysis, cap. 6; Jensen 2016, Introductory Digital Image Processing, cap. 8 — o comportamento de PC1 como 'brilho geral' é um padrão comum, não garantido em toda cena, por isso classificado como aproximação"
  - claim_id: SENSREM-M14-A05-ACPSELETIVA-002
    claim: "ACP seletiva (feature-oriented PCA), aplicada a um subconjunto deliberadamente escolhido de bandas contendo feições diagnósticas de um mineral-alvo, é usada em exploração mineral para realçar esse mineral de forma mais direcionada do que uma ACP aplicada a todas as bandas do sensor."
    risk: aproximacao
    source: "Loughlin 1991, Photogrammetric Engineering and Remote Sensing 57(9); prática consolidada de processamento de imagem para exploração mineral"
  - claim_id: SENSREM-M14-A05-KMEANS-003
    claim: "Classificação não supervisionada por K-means agrupa pixels iterativamente por similaridade espectral em um número K de agrupamentos definido a priori, sem rótulo de classe conhecido; a atribuição de nome de classe temática a cada agrupamento (rotulação) ocorre em etapa posterior, pelo analista."
    risk: fato
    source: "Richards 2022, Remote Sensing Digital Image Analysis, cap. 8; Jensen 2016, cap. 9"
  - claim_id: SENSREM-M14-A05-MAXVEROSS-004
    claim: "O classificador de Máxima Verossimilhança modela estatisticamente a distribuição espectral de cada classe (tipicamente assumindo normalidade multivariada) a partir de amostras de treinamento, e atribui cada pixel à classe de maior probabilidade estatística; classificadores como SVM e Random Forest fazem menos suposições sobre a distribuição dos dados e frequentemente superam a Máxima Verossimilhança em cenas complexas, mas ambos dependem criticamente da qualidade das amostras de treinamento."
    risk: fato
    source: "Richards 2022, Remote Sensing Digital Image Analysis, cap. 8; literatura consolidada de classificação supervisionada em sensoriamento remoto"
  - claim_id: SENSREM-M14-A05-MATRIZCONFUSAO-005
    claim: "A matriz de confusão cruza a classe atribuída por um classificador com a classe verdadeira, verificada por amostras de validação independentes das amostras de treinamento; dela derivam-se acurácia global (diagonal sobre total), acurácia do produtor (mede omissão, por classe), acurácia do usuário (mede comissão, por classe) e o coeficiente Kappa, que ajusta a acurácia global descontando a concordância esperada ao acaso. O USO DO KAPPA É OBJETO DE DIVERGENCIA REAL E ATIVA NA AREA: Congalton & Green (2019) o mantêm como métrica padrão, enquanto Pontius & Millones (2011) defendem abandoná-lo em favor de desacordo de quantidade e desacordo de alocação, e Foody (2020) argumenta sua inadequação para comparar acurácias de mapas distintos. A matriz completa e as acurácias de produtor e usuário por classe não são disputadas por nenhum dos lados."
    risk: controverso
    source: "Congalton & Green 2019, Assessing the Accuracy of Remotely Sensed Data, cap. 4-5; Pontius Jr. & Millones 2011, International Journal of Remote Sensing 32(15):4407-4429; Foody 2020, Remote Sensing of Environment 239. Divergencia registrada na auditoria do Modulo 14 (claim SENSREM-M14-A05-KAPPA-010); nenhum lado foi escolhido, conforme a politica para achados controversos."
-->
