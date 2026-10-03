# Aula 04: Processamento digital de imagens I: realces, operações aritméticas e filtros de convolução

**ID:** geologia-avancado-m14-a04
**Módulo:** [[14-sensoriamento-remoto-modulo|Módulo 14 — Sensoriamento remoto]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** apresentar as operações digitais fundamentais que transformam uma imagem bruta de satélite em produto interpretável — correção prévia, realce de contraste, operações aritméticas entre bandas (razões e índices espectrais) e filtragem espacial por convolução.
**Ao final você vai conseguir:** explicar a diferença entre correção radiométrica/atmosférica e realce; aplicar e interpretar um alongamento de contraste; calcular e justificar uma razão de bandas ou um índice espectral (NDVI, NDWI) a partir de valores de reflectância; e escolher um filtro de convolução adequado a um objetivo de realce (passa-baixa, passa-alta, detecção de borda).
**Pré-requisito:** [[14-sensoriamento-remoto-aula-03-comportamento-espectral-agua-solos-minerais-rochas-vegetacao-geobotanica|Aula 03]] — as operações desta aula fazem sentido pleno quando já se sabe por que a curva espectral de cada alvo se comporta como se comporta.

## Conteúdo

### O que é processamento digital de imagens, e onde ele começa

**Processamento digital de imagens** (PDI) é o conjunto de operações matemáticas aplicadas ao dado numérico de uma imagem — cada pixel de cada banda é apenas um número, um **nível de cinza** ou **valor digital** (DN, *digital number*), tipicamente entre 0 e um valor máximo definido pela resolução radiométrica do sensor (a Aula 01 já introduziu essa ideia: 4.096 níveis possíveis, 0-4095, num sensor de 12 bits) — e é sobre esses números, não sobre a "imagem" no sentido fotográfico, que todo o processamento opera.

Antes de qualquer realce interpretativo, uma imagem passa por **pré-processamento**, cujo objetivo não é tornar a imagem mais bonita, mas corrigir distorções sistemáticas introduzidas pelo próprio sistema de aquisição — e vale nomear as três correções mais relevantes, ainda que o detalhamento operacional de cada uma fuja do escopo desta aula. A **correção radiométrica** ajusta o valor digital bruto de cada pixel para compensar diferenças de calibração entre detectores do sensor (cada sensor tem múltiplos detectores físicos, ligeiramente diferentes entre si) e converte, por fim, o número digital em uma grandeza física com significado — radiância no topo da atmosfera. A **correção atmosférica**, consequência direta do que a Aula 02 explicou sobre espalhamento e absorção, remove a contribuição da própria atmosfera (o *path radiance*) para recuperar uma estimativa da reflectância de superfície — sem essa correção, comparar duas imagens de datas diferentes (com condições atmosféricas distintas) introduz erro sistemático em qualquer análise quantitativa, incluindo os índices espectrais que esta aula vai apresentar. A **correção geométrica** (ortorretificação) ajusta distorções de posição causadas pela geometria de aquisição (ângulo de visada, relevo do terreno) e amarra a imagem a um sistema de coordenadas de referência — o mesmo tipo de cuidado com datum e projeção visto no Módulo 13, agora aplicado à origem, não à entrega, do dado espacial. Só depois dessas três correções a imagem está pronta para os realces e análises que seguem.

### Realce de contraste: alongamento de histograma

Uma imagem de satélite bruta, mesmo já corrigida radiometricamente, costuma ocupar apenas uma fração estreita da faixa total de valores digitais disponíveis — o **histograma** (a distribuição de frequência dos valores digitais de uma banda) concentra-se num intervalo estreito, produzindo uma imagem de baixo contraste visual, mesmo que a informação esteja presente nos números. O **alongamento de contraste** (*contrast stretch*) redistribui esses valores por toda a faixa disponível de exibição (0-255, no padrão de exibição de 8 bits de qualquer monitor, independentemente da radiometria original do sensor), tornando diferenças sutis entre pixels visualmente perceptíveis sem alterar a informação relativa entre eles.

O **alongamento linear** mapeia o intervalo mínimo-máximo (ou um intervalo definido por percentual, para não deixar poucos pixels extremos "esticarem" todo o resto) diretamente para 0-255, de forma proporcional — é o mais simples e o mais usado por padrão. O **alongamento por equalização de histograma** redistribui os valores de forma que o histograma resultante seja aproximadamente uniforme (cada nível de saída recebe aproximadamente o mesmo número de pixels), maximizando o contraste onde há mais pixels concentrados — útil quando a informação relevante está concentrada numa faixa estreita e específica de valores, à custa de distorcer a relação visual entre partes muito claras e muito escuras da imagem. É importante frisar o que o realce de contraste **não** faz: ele não adiciona informação nova, apenas torna mais visível a informação que já estava presente nos valores digitais — a decisão de qual tipo de alongamento usar depende do que se quer tornar mais evidente ao olho, não muda o dado subjacente usado em análises quantitativas posteriores.

### Operações aritméticas entre bandas: razões e índices espectrais

Enquanto o realce de contraste opera dentro de uma única banda, as **operações aritméticas entre bandas** combinam dois ou mais canais espectrais pixel a pixel, usando as quatro operações básicas (soma, subtração, multiplicação, divisão) para gerar uma banda derivada nova, frequentemente mais diagnóstica do que qualquer banda original isolada.

A **razão de bandas** (divisão de uma banda por outra, pixel a pixel) tem uma propriedade valiosa: ela cancela, em boa medida, o efeito de fatores que afetam todas as bandas de forma multiplicativa e aproximadamente uniforme — sombra topográfica e diferenças de iluminação solar entre encostas de exposição diferente sendo os exemplos mais relevantes em terrenos montanhosos. Se um pixel em sombra recebe metade da iluminação de um pixel equivalente ao sol, todas as suas bandas caem proporcionalmente — mas a **razão** entre duas bandas desse mesmo pixel permanece praticamente igual à razão do pixel ensolarado, porque o fator de escala se cancela na divisão. É por isso que razões de bandas (como as combinações SWIR mencionadas na Aula 01 para alteração hidrotermal) são preferidas a bandas brutas para mapear composição em terreno de relevo acidentado.

O **índice espectral** é uma razão de bandas normalizada, formulada especificamente para realçar um alvo ou fenômeno de interesse — e os dois mais usados em sensoriamento remoto, ambos derivados diretamente das curvas espectrais vistas na Aula 03, merecem fórmula explícita.

O **NDVI** (Normalized Difference Vegetation Index, índice de vegetação por diferença normalizada) explora o contraste entre a alta reflectância da vegetação sadia no infravermelho próximo e sua baixa reflectância no vermelho (absorção por clorofila):

NDVI = (NIR − Vermelho) / (NIR + Vermelho)

O resultado varia entre −1 e +1: vegetação densa e vigorosa produz valores tipicamente entre 0,6 e 0,9 (NIR muito maior que vermelho); solo exposto e rocha ficam próximos de 0 (reflectância parecida nas duas bandas); água produz valores negativos (NIR menor que vermelho, o oposto do padrão terrestre, consequência direta da forte absorção de água no infravermelho próximo vista na Aula 03). O NDVI é usado tanto para mapear vegetação diretamente quanto, de forma indireta, para geobotânica (Aula 03) — variações locais e anômalas de NDVI, num contexto de vegetação de resto homogênea, podem sinalizar estresse hídrico ou por metais.

O **NDWI** (Normalized Difference Water Index) tem formulação análoga, adaptada ao contraste espectral da água:

NDWI = (Verde − NIR) / (Verde + NIR)

Explorando o mesmo princípio da Aula 03 — água reflete relativamente bem no verde e absorve fortemente no infravermelho próximo — o NDWI produz valores altos e positivos para água, e valores baixos ou negativos para vegetação e solo, o inverso do padrão do NDVI, o que o torna um delineador de corpos d'água mais robusto do que uma banda isolada, pela mesma razão de cancelamento de efeitos de iluminação que vale para qualquer razão de bandas.

Uma armadilha de nomenclatura que vale conhecer antes de ler qualquer artigo da área: **existem dois índices diferentes chamados NDWI**, propostos no mesmo ano e para finalidades distintas. O de McFeeters (1996), acima, usa verde e NIR e mede **superfície de água aberta**. O de Gao (1996) usa NIR e SWIR — NDWI = (NIR − SWIR)/(NIR + SWIR) — e mede o **teor de água líquida dentro da folha**, explorando justamente a absorção da água foliar no SWIR vista na Aula 03; é um índice de vegetação, não de corpos d'água. Há ainda o **MNDWI** de Xu (2006), que troca o NIR pelo SWIR na fórmula de McFeeters — (Verde − SWIR)/(Verde + SWIR) — e costuma delinear água melhor que o original em área urbana. Ao encontrar "NDWI" num texto, verifique sempre quais bandas entraram na fórmula antes de supor o que ele mede.

### Filtragem espacial por convolução: realçando padrões, não composição

Enquanto as operações aritméticas combinam bandas diferentes no mesmo pixel, a **filtragem espacial** opera dentro de uma única banda, combinando o valor de cada pixel com os valores de seus vizinhos — o objetivo não é mais realçar composição espectral, e sim padrões espaciais: textura, bordas, feições lineares.

O mecanismo padrão é a **convolução**: uma pequena matriz de pesos (o **kernel**, tipicamente 3×3 ou 5×5 pixels) percorre a imagem pixel a pixel, e em cada posição multiplica o valor de cada pixel sob o kernel pelo peso correspondente, somando o resultado para gerar o novo valor do pixel central na imagem de saída. A escolha dos pesos do kernel determina completamente o que o filtro faz.

Um **filtro passa-baixa** (ou de suavização) usa pesos que calculam essencialmente uma média (ponderada ou simples) da vizinhança — o efeito é suavizar a imagem, atenuando ruído de alta frequência (variação pixel a pixel abrupta e aleatória) à custa de perder nitidez de detalhe fino; o kernel mais simples é uma média aritmética uniforme (todos os pesos iguais, somando 1), e variações gaussianas dão mais peso ao pixel central, suavizando com menos perda de nitidez.

Um **filtro passa-alta** (ou de realce de nitidez) faz o oposto: realça diferenças abruptas entre um pixel e sua vizinhança, tornando bordas e detalhes finos mais evidentes, à custa de amplificar também o ruído — obtido tipicamente subtraindo uma versão suavizada da imagem original (realçando o que a suavização removeu) ou por um kernel com peso central alto positivo e pesos negativos na vizinhança, de forma que a soma dos pesos seja próxima de 1.

Os **filtros de detecção de borda** (ou de realce direcional) são um caso especializado de passa-alta, desenhados para destacar especificamente transições abruptas de valor numa direção preferencial ou em todas as direções — os kernels de Sobel e de Prewitt, por exemplo, calculam o gradiente da imagem em direções horizontal e vertical separadamente, e sua combinação produz uma imagem de magnitude de borda. Em geologia, filtros de detecção de borda são a ferramenta padrão para realçar **lineamentos** — traços retilíneos ou levemente curvos na imagem que podem corresponder a falhas, fraturas, contatos litológicos ou drenagem estruturalmente controlada — mas, exatamente como a Aula 06 do Módulo 13 já advertiu sobre lineamentos extraídos de modelo digital de elevação, um lineamento realçado por filtro é **hipótese de controle estrutural, não confirmação**: o mesmo filtro realça igualmente bordas de origem não estrutural (limites de uso do solo, estradas, bordas de nuvem residual, artefatos de mosaico entre cenas), e só a checagem de campo — ou a integração com outros dados independentes, como os produtos ativos das Aulas 06 e 07 — separa lineamento geológico real de artefato.

## Exemplo trabalhado

**Situação:** um analista recebe uma cena Sentinel-2 já corrigida atmosfericamente (valores de reflectância de superfície, escala 0-1) sobre uma área com uma encosta parcialmente em sombra. Para um pixel de vegetação ao sol, a banda B4 (vermelho, ~665 nm) tem reflectância 0,05 e a banda B8 (NIR, ~842 nm) tem reflectância 0,45. Para um pixel de vegetação equivalente, mas em sombra parcial (recebendo aproximadamente 60% da iluminação do pixel ao sol), as duas bandas caem proporcionalmente: B4 = 0,03 e B8 = 0,27. Calcule o NDVI dos dois pixels e mostre por que a razão (índice) é mais robusta à sombra do que comparar diretamente os valores brutos de uma única banda.

**Resolução:**

*Pixel ao sol:*
NDVI = (0,45 − 0,05) / (0,45 + 0,05) = 0,40 / 0,50 = **0,80**

*Pixel em sombra:*
NDVI = (0,27 − 0,03) / (0,27 + 0,03) = 0,24 / 0,30 = **0,80**

Os dois pixels produzem exatamente o mesmo NDVI (0,80), apesar de os valores brutos de reflectância diferirem em 40% entre eles (0,45 vs. 0,27 no NIR, uma queda que, olhada isoladamente na banda B8, sugeriria — erradamente — uma diferença real de vigor de vegetação entre os dois pontos). Isso acontece porque a sombra reduziu ambas as bandas pelo mesmo fator multiplicativo (0,6), e esse fator se cancela algebricamente na razão: (0,6×NIR − 0,6×Vermelho) / (0,6×NIR + 0,6×Vermelho) = 0,6×(NIR−Vermelho) / [0,6×(NIR+Vermelho)] = (NIR−Vermelho)/(NIR+Vermelho), o mesmo NDVI de antes. Este é exatamente o mecanismo descrito na seção sobre razões de bandas: um analista que decidisse comparar vigor de vegetação usando apenas a banda B8 bruta concluiria, incorretamente, que a vegetação em sombra está em pior estado — quando na verdade a diferença observada é inteiramente um artefato de iluminação, não de composição ou saúde da planta. É essa robustez a variações de iluminação, e não apenas a interpretabilidade da fórmula, que faz de índices normalizados a ferramenta padrão para análise quantitativa de vegetação em terreno de relevo variado — como praticamente todo terreno geológico de interesse.

## Erros comuns

- **Comparar bandas brutas entre pixels ao sol e em sombra e concluir sobre vigor de vegetação.** É exatamente o erro que o exemplo trabalhado evita: a queda de 40% na banda NIR isolada sugeriria diferença real de saúde da planta, quando é inteiramente artefato de iluminação — a razão (NDVI) cancela esse efeito, a banda isolada não.
- **Usar "NDWI" sem checar quais bandas a fórmula usa.** A aula nomeia três índices homônimos ou quase (McFeeters: verde/NIR, corpos d'água; Gao: NIR/SWIR, água na folha; MNDWI de Xu: verde/SWIR) — supor qual é sem checar a fórmula pode levar a interpretar um índice de vegetação como se fosse de corpo d'água.
- **Aplicar realce de contraste antes da correção atmosférica e radiométrica.** Realce só torna mais visível o que já está nos números — se o número ainda carrega viés sistemático (path radiance, descalibração entre detectores), o realce só destaca o viés, não corrige nada.
- **Interpretar um lineamento realçado por filtro de borda (Sobel, Prewitt) como falha confirmada.** O mesmo filtro realça igualmente estradas, limites de uso do solo e bordas de mosaico entre cenas — é hipótese estrutural até checagem de campo, o mesmo princípio já visto para lineamentos de MDE no Módulo 13.

## O que não concluir

- **Que alongamento de contraste (linear ou por equalização) muda a informação quantitativa do dado.** Ele só redistribui a exibição visual — qualquer análise quantitativa (NDVI, razão de bandas) deve ser feita sobre os valores originais, não sobre a versão realçada para visualização.
- **Que filtro passa-alta é "melhor" que passa-baixa por realçar mais detalhe.** Passa-alta amplifica ruído junto com a borda real — a escolha depende do que se busca (suavizar ruído vs. realçar transição), não existe filtro superior em abstrato.
- **Que uma razão de bandas resolve qualquer problema de iluminação.** Ela cancela efeitos **multiplicativos** e aproximadamente uniformes entre bandas (como a sombra do exemplo); não corrige, por si só, diferenças não multiplicativas ou erros de calibração entre detectores — para isso a correção radiométrica prévia continua sendo necessária.

## Recap relâmpago

- PDI opera sobre valores digitais (DN) de cada pixel; pré-processamento (correção radiométrica, atmosférica e geométrica) precisa preceder qualquer realce ou análise quantitativa, sob pena de comparar imagens com viés sistemático embutido.
- Alongamento de contraste redistribui os valores digitais pela faixa de exibição para tornar diferenças sutis visíveis, sem adicionar informação nova ao dado — linear é o padrão simples, equalização de histograma maximiza contraste onde há mais pixels concentrados.
- Razões de bandas cancelam, algebricamente, efeitos multiplicativos comuns a todas as bandas (sombra, diferença de iluminação entre encostas), o que as torna mais robustas que bandas brutas para mapear composição em terreno acidentado.
- NDVI = (NIR−Vermelho)/(NIR+Vermelho) realça vegetação (valores altos e positivos) e diferencia de água (valores negativos) e solo/rocha (valores próximos de zero); NDWI de McFeeters (1996) = (Verde−NIR)/(Verde+NIR) realça água de forma análoga — mas cuidado com a homonímia: o NDWI de Gao (1996) é (NIR−SWIR)/(NIR+SWIR) e mede água **na folha**, não corpos d'água, e o MNDWI de Xu (2006) é (Verde−SWIR)/(Verde+SWIR); confira sempre as bandas antes de supor o que um "NDWI" mede.
- Filtros de convolução operam dentro de uma banda combinando um pixel com sua vizinhança via um kernel: passa-baixa suaviza (atenua ruído, perde nitidez), passa-alta realça bordas e detalhe (amplifica ruído), filtros de detecção de borda (Sobel, Prewitt) são a ferramenta padrão para realçar lineamentos.
- Um lineamento realçado por filtro de borda é hipótese de controle estrutural, não confirmação — o mesmo filtro realça igualmente artefatos não geológicos (uso do solo, estradas, bordas de mosaico), e só checagem de campo ou integração com outros dados separa uma coisa da outra.

## Próxima aula

[[14-sensoriamento-remoto-aula-05-pdi-ii-transformacoes-multivariadas-classificacao|Aula 05 — Processamento digital de imagens II: transformações multivariadas e classificação supervisionada e não supervisionada]] — esta aula tratou cada banda (ou par de bandas) isoladamente; a próxima trata todas as bandas em conjunto, com técnicas que reduzem redundância e classificam automaticamente cada pixel numa categoria.

## Fontes

- Jensen, J. R. (2016), *Introductory Digital Image Processing: A Remote Sensing Perspective*, 4ª ed., Pearson, cap. 4-5 e 7 (pré-processamento, realce de contraste, filtragem espacial, operações aritméticas).
- Lillesand, T. M., Kiefer, R. W. & Chipman, J. W. (2015), *Remote Sensing and Image Interpretation*, 7ª ed., Wiley, cap. 7 (índices de vegetação e de água, razões de banda).
- Rouse, J. W. et al. (1973), "Monitoring vegetation systems in the Great Plains with ERTS", *NASA SP-351* (formulação original do NDVI).
- McFeeters, S. K. (1996), "The use of the Normalized Difference Water Index (NDWI) in the delineation of open water features", *International Journal of Remote Sensing*, 17(7), p. 1425-1432 (formulação do NDWI usada nesta aula, verde e NIR, para corpos d'água).
- Gao, B.-C. (1996), "NDWI — A normalized difference water index for remote sensing of vegetation liquid water from space", *Remote Sensing of Environment*, 58(3) (o outro NDWI, NIR e SWIR, para água na folha — homônimo do anterior).
- Xu, H. (2006), "Modification of normalised difference water index (NDWI) to enhance open water features in remotely sensed imagery", *International Journal of Remote Sensing*, 27(14) (MNDWI, verde e SWIR).
- Gonzalez, R. C. & Woods, R. E. (2018), *Digital Image Processing*, 4ª ed., Pearson, cap. 3 (fundamentos de convolução e filtragem espacial, kernels de Sobel/Prewitt).

<!--
nivel: avancado
palavras_corpo: 2265
mapa_objetivo_secao:
  geologia-avancado-m14-oa03: "O que é processamento digital de imagens, e onde ele começa" + "Realce de contraste: alongamento de histograma" + "Operações aritméticas entre bandas: razões e índices espectrais" + "Filtragem espacial por convolução: realçando padrões, não composição" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: SENSREM-M14-A04-PREPROC-001
    claim: "Correção radiométrica ajusta o valor digital bruto para compensar diferenças de calibração entre detectores e converte DN em radiância; correção atmosférica remove a contribuição do path radiance para estimar reflectância de superfície; correção geométrica (ortorretificação) ajusta distorções de posição causadas pela geometria de aquisição e relevo, amarrando a imagem a um sistema de coordenadas de referência."
    risk: fato
    source: "Jensen 2016, Introductory Digital Image Processing, cap. 4 (pré-processamento radiométrico, atmosférico e geométrico)"
  - claim_id: SENSREM-M14-A04-NDVI-002
    claim: "NDVI = (NIR - Vermelho) / (NIR + Vermelho), formulado por Rouse et al. (1973); varia entre -1 e +1, com vegetação densa tipicamente entre 0,6 e 0,9, solo/rocha próximos de 0, e água com valores negativos."
    risk: fato
    source: "Rouse et al. 1973, NASA SP-351; Jensen 2016, cap. 7; faixas típicas de valor consolidadas na literatura de sensoriamento remoto de vegetação"
  - claim_id: SENSREM-M14-A04-NDWI-003
    claim: "NDWI = (Verde - NIR) / (Verde + NIR), formulado por McFeeters (1996) para delineamento de corpos d'água abertos; produz valores altos e positivos para água e valores baixos ou negativos para vegetação e solo. HOMONIMIA REGISTRADA: existe um segundo índice também chamado NDWI, de Gao (1996), definido como (NIR - SWIR)/(NIR + SWIR), que mede teor de água líquida na folha e é um índice de vegetação, não de corpos d'água; e o MNDWI de Xu (2006), (Verde - SWIR)/(Verde + SWIR), variante do de McFeeters que costuma delinear água melhor em área urbana."
    risk: fato
    source: "McFeeters 1996, International Journal of Remote Sensing 17(7):1425-1432; Gao 1996, Remote Sensing of Environment 58(3):257-266; Xu 2006, International Journal of Remote Sensing 27(14):3025-3033. Ambiguidade de nomenclatura registrada na auditoria do Modulo 14 (claim SENSREM-M14-A04-NDWIHOMONIMO-011); a atribuição original da aula a McFeeters já estava correta — o que faltava era a advertência."
  - claim_id: SENSREM-M14-A04-RAZAOCANCELA-004
    claim: "Numa razão de bandas, um fator multiplicativo uniforme aplicado a ambas as bandas (como a redução proporcional de reflectância causada por sombra topográfica) se cancela algebricamente no resultado da razão, tornando índices normalizados como NDVI mais robustos a variações de iluminação do que a comparação direta de valores de uma única banda."
    risk: fato
    source: "Consequência algébrica direta da definição de razão de bandas; Lillesand, Kiefer & Chipman 2015, cap. 7"
  - claim_id: SENSREM-M14-A04-FILTROS-005
    claim: "Filtros de convolução passa-baixa suavizam a imagem (atenuam ruído, reduzem nitidez) por meio de kernels que calculam média ponderada da vizinhança; filtros passa-alta realçam bordas e detalhe fino (amplificam ruído); os kernels de Sobel e Prewitt são filtros de detecção de borda que calculam o gradiente da imagem em direções horizontal e vertical, usados para realçar lineamentos geológicos como hipótese, não confirmação, de estrutura."
    risk: fato
    source: "Gonzalez & Woods 2018, Digital Image Processing, cap. 3; Jensen 2016, cap. 5 (filtragem espacial e detecção de borda em sensoriamento remoto geológico)"
-->
