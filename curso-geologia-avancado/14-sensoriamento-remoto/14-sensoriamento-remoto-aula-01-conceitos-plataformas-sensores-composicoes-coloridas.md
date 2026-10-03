# Aula 01: Conceitos, plataformas e sensores; resoluções espacial, espectral, temporal e radiométrica; composições coloridas

**ID:** geologia-avancado-m14-a01
**Módulo:** [[14-sensoriamento-remoto-modulo|Módulo 14 — Sensoriamento remoto]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** apresentar o vocabulário e o mapa mental do sensoriamento remoto — o que é uma plataforma, o que é um sensor, os quatro tipos de resolução que definem se uma imagem serve a um problema geológico, e como combinar bandas em composições coloridas interpretáveis.
**Ao final você vai conseguir:** distinguir sensores passivos de ativos e plataformas orbitais de aerotransportadas; explicar as quatro resoluções (espacial, espectral, temporal, radiométrica) e o compromisso entre elas; escolher uma composição colorida adequada a um objetivo de interpretação geológica; e ler a ficha técnica de um sensor óptico real (Landsat 8/9, Sentinel-2) sem se perder na quantidade de números.
**Pré-requisito:** nenhum específico deste módulo — pressupõe apenas o SIG e os conceitos de dado matricial (raster) vistos no Módulo 13 (Aula 02), sobre os quais o sensoriamento remoto se apoia diretamente: toda imagem de satélite é, estruturalmente, um raster com uma ou mais bandas.
**Aviso de sequência, deliberado:** esta aula vem **antes** da física, e não depois. Ela vai usar vocabulário espectral — banda, visível, infravermelho próximo, infravermelho de ondas curtas (SWIR), termal, micro-ondas — como se fosse rótulo de ficha técnica, sem explicar de onde ele vem; quem constrói essa física é a Aula 02, e quem explica por que cada material responde diferente em cada faixa é a Aula 03. A escolha é proposital: é mais fácil entender por que a física importa depois de já ter visto para que servem os números que ela produz. Se em algum momento desta aula você sentir que está aceitando um termo sem entendê-lo, está tudo certo — anote e siga; as duas aulas seguintes fecham exatamente essa lacuna.

## Conteúdo

### O que é sensoriamento remoto, e por que ele abre uma nova área do curso

**Sensoriamento remoto** é a ciência de obter informação sobre um objeto ou uma área sem contato físico direto com ele — na prática, medindo a energia eletromagnética que esse objeto emite, reflete ou espalha, captada por um sensor a distância. O Módulo 13 tratou de como organizar, processar e entregar dados espaciais já existentes; este módulo trata de como esses dados de origem — sobretudo as imagens — são gerados e interpretados fisicamente, e como extrair deles informação geológica: litologia, estruturas, alteração hidrotermal, cobertura vegetal como indicador indireto de substrato, geomorfologia, risco geológico.

Dois pares de conceitos organizam tudo o que vem depois: **plataforma** e **sensor**, de um lado; **sensor passivo** e **sensor ativo**, do outro.

A **plataforma** é o veículo que carrega o sensor: um satélite em órbita, uma aeronave tripulada, um VANT (veículo aéreo não tripulado, o "drone"), ou até um suporte terrestre fixo. A escolha de plataforma determina, antes de qualquer outra coisa, a altitude de operação — e a altitude, por sua vez, condiciona a área coberta por imagem (a **faixa de imageamento**, ou *swath*) e, em boa parte dos casos, a resolução espacial alcançável. Satélites orbitam a centenas ou milhares de quilômetros de altitude e cobrem grandes áreas com resolução moderada a fina; aeronaves voam a alguns quilômetros e cobrem áreas menores com resolução mais fina; VANTs voam a dezenas a poucas centenas de metros e alcançam resolução centimétrica sobre áreas pequenas.

O **sensor** é o instrumento que efetivamente mede a energia eletromagnética. Aqui entra a segunda distinção, mais importante para interpretar qualquer produto: um sensor **passivo** mede a energia que já existe no ambiente — luz solar refletida pelos alvos (a faixa mais comum, do óptico ao infravermelho de ondas curtas) ou energia térmica emitida naturalmente pelos próprios alvos (infravermelho termal). Um sensor **ativo**, ao contrário, emite sua própria energia (um pulso de micro-ondas ou de laser) em direção ao alvo e mede o que retorna — o radar (SAR) e o LiDAR são os dois exemplos centrais, e ambos serão o assunto das Aulas 06 e 07 deste módulo. A diferença tem uma consequência prática enorme: sensores passivos na faixa óptica dependem de luz solar e, portanto, não operam à noite nem enxergam bem sob nuvens espessas; sensores ativos de micro-ondas carregam sua própria fonte de energia e atravessam nuvens, operando de dia ou de noite — uma vantagem decisiva em regiões tropicais de cobertura de nuvens persistente, boa parte do território brasileiro incluída.

### Órbitas: por que a maioria dos satélites de recursos naturais é heliossíncrona

A imensa maioria dos satélites ópticos usados em geologia (Landsat, Sentinel-2, os satélites CBERS sino-brasileiros) opera em **órbita heliossíncrona** (também chamada síncrona ao Sol): uma órbita quase polar, de baixa altitude (tipicamente 700-800 km), ajustada de modo que o satélite sempre cruze um dado ponto da superfície aproximadamente no mesmo horário solar local — por exemplo, o Landsat 8/9 cruza o Equador por volta das 10h da manhã, horário local, em toda passagem. Isso mantém o ângulo de iluminação solar razoavelmente consistente entre imagens de datas diferentes, o que é essencial para comparar cenas ao longo do tempo sem que a variação de sombra distorça a análise.

Uma órbita alternativa, usada por satélites meteorológicos, é a **geoestacionária**: a cerca de 36.000 km de altitude, sobre o Equador, com velocidade orbital igual à rotação da Terra, de forma que o satélite parece "parado" sobre o mesmo ponto — cobertura contínua da mesma área, mas com resolução espacial muito mais grosseira, por isso pouco usada em geologia de detalhe e mais associada a monitoramento atmosférico e de grandes eventos.

### As quatro resoluções: o vocabulário que decide se uma imagem serve ao problema

Toda ficha técnica de sensor gira em torno de quatro tipos de resolução, e confundi-los é o erro mais comum de quem está começando em sensoriamento remoto — vale fixar bem esta seção antes de seguir.

**Resolução espacial** é o tamanho do menor elemento de terreno que o sensor consegue distinguir como uma unidade separada — na prática, o tamanho do pixel no terreno (o *IFOV*, campo de visão instantâneo, projetado na superfície). Uma imagem com resolução espacial de 30 m (como as bandas multiespectrais do Landsat) tem cada pixel representando um quadrado de 30 × 30 m no terreno; uma imagem de 10 m (Sentinel-2, bandas principais) resolve detalhe substancialmente maior. Resolução espacial mais fina custa caro em dois sentidos: tecnicamente (ótica maior, mais dados por cena) e em termos de área coberta por imagem, que tende a diminuir.

**Resolução espectral** é o número, a largura e a posição das bandas que o sensor registra ao longo do espectro eletromagnético. Um sensor **multiespectral** (Landsat, com 11 bandas; Sentinel-2, com 13) mede em algumas dezenas de bandas relativamente largas; um sensor **hiperespectral** mede em centenas de bandas estreitas e contíguas, o suficiente para reconstruir uma curva espectral quase contínua de cada pixel — capacidade que se aproxima da espectroscopia de laboratório e permite, em princípio, identificar minerais específicos por sua assinatura espectral fina (assunto que retorna na Aula 03). Quanto mais estreitas e numerosas as bandas, maior a resolução espectral — e maior também o volume de dado e a complexidade de processamento.

**Resolução temporal** é o intervalo de tempo entre duas passagens do mesmo sensor sobre o mesmo ponto da superfície — o **tempo de revisita**. O Landsat 8 e o Landsat 9 revisitam o mesmo ponto a cada 16 dias cada um, mas como operam defasados um em relação ao outro, a constelação conjunta entrega uma imagem a cada 8 dias, em média, sobre a mesma área. O Sentinel-2 opera como uma constelação de **dois satélites em serviço simultâneo**, defasados 180° na mesma órbita, com revisita combinada de cerca de 5 dias no Equador. Resolução temporal alta é indispensável para monitorar fenômenos que mudam rápido — deslizamentos, inundações, desmatamento, deformação de superfície (Aula 06) — e menos crítica para litologia, que não muda em escala humana de tempo.

**Resolução radiométrica** é o número de níveis distintos de intensidade que o sensor consegue registrar para cada pixel, expresso em bits — 8 bits equivalem a 256 níveis de cinza possíveis por banda, 12 bits (padrão do Landsat 8/9 e do Sentinel-2 atuais) equivalem a 4.096 níveis. Mais bits significa mais sensibilidade a variações sutis de brilho — a diferença entre dois materiais muito parecidos em reflectância pode só aparecer numa radiometria fina o bastante para separá-los.

O ponto que amarra as quatro resoluções: elas competem por um orçamento fixo de dado e de energia do sensor, e melhorar uma quase sempre custa alguma coisa nas outras três — um sensor de resolução espacial muito fina tende a ter faixa de imageamento menor (o que prejudica a resolução temporal, porque revisita menos área por órbita) e frequentemente menos bandas (resolução espectral mais pobre). Escolher um sensor para um projeto geológico é, na prática, decidir qual dessas quatro trocar por qual — nunca existe o sensor que maximiza as quatro ao mesmo tempo.

### Plataformas e sensores de referência em geologia

Vale ter no radar (com perdão do trocadilho) os sensores ópticos mais usados em geologia, por sua disponibilidade gratuita e continuidade histórica:

| Sensor | Órbita/plataforma | Resolução espacial (bandas principais) | Bandas | Revisita |
|---|---|---|---|---|
| Landsat 8/9 (OLI/TIRS) | heliossíncrona, ~705 km | 30 m (multiespectral), 15 m (pancromática), 100 m (termal) | 11 (incl. 2 termais) | 16 dias cada (~8 dias combinado) |
| Sentinel-2 (MSI) | heliossíncrona, ~786 km | 10 m, 20 m e 60 m conforme a banda | 13 | ~5 dias combinado (par nominal 2B+2C desde 2025; 2A em campanha de extensão) |
| ASTER (a bordo do Terra) | heliossíncrona, ~705 km | 15 m (VNIR), 30 m (SWIR), 90 m (TIR) | 14 (destaque: 6 bandas SWIR e 5 termais) | não há revisita sistemática — as cenas são adquiridas por solicitação |

**Nota sobre a identidade dos satélites Sentinel-2.** O que é estável é o *arranjo* — dois satélites em serviço, defasados 180°, revisita de 5 dias. Quem ocupa esses dois lugares muda, e vale saber qual satélite gerou a cena que você baixou:

| Satélite | Situação |
|---|---|
| 2A | fora da operação nominal desde **21/01/2025**, quando o 2C assumiu seu lugar; desde março de 2025 opera numa **campanha de extensão**, defasado 36° do 2B |
| 2B | em operação nominal (será sucedido pelo 2D) |
| 2C | em operação nominal desde 21/01/2025 |

A campanha de extensão do 2A tem uma consequência prática que interessa diretamente a quem trabalha no Brasil: ela adensa a revisita sobre a Europa, a África tropical e a **América do Sul** — justamente as regiões mais penalizadas por cobertura de nuvens.

Três siglas da tabela, que a Aula 02 vai localizar no espectro e a Aula 03 vai explicar: **VNIR** é visível mais infravermelho próximo, **SWIR** é o infravermelho de ondas curtas, e **TIR** é o infravermelho termal. Por ora basta reter que são faixas sucessivas de comprimento de onda, cada vez mais longo, e que um mesmo sensor pode registrar as três em resoluções espaciais diferentes — como o ASTER faz.

O ASTER merece nota à parte: apesar de ter encerrado a aquisição de novas bandas SWIR em 2008 (degradação do detector), seu arquivo histórico continua sendo referência em geologia mineral, justamente pela combinação rara de múltiplas bandas SWIR (sensíveis a minerais de alteração hidrotermal) e bandas termais — capacidade que nem Landsat nem Sentinel-2 replicam completamente.

### Composições coloridas: como transformar bandas em imagem interpretável

O olho humano enxerga apenas três cores primárias (vermelho, verde e azul — RGB), mas um sensor multiespectral registra dezenas de bandas, muitas fora do visível. Uma **composição colorida** resolve essa diferença atribuindo três bandas quaisquer do sensor aos três canais RGB de exibição de um monitor — permitindo "ver" informação que o olho humano jamais capta diretamente, como o infravermelho próximo.

A **composição em cor verdadeira** (*true color*) atribui banda vermelha ao canal R, banda verde ao canal G e banda azul ao canal B — reproduzindo a aparência que a cena teria a olho nu. É intuitiva, mas pouco poderosa para geologia, porque rochas e solos tendem a variar pouco em cor visível e a informação mais diagnóstica costuma estar fora do visível.

A **composição em falsa cor** atribui a um ou mais canais RGB bandas fora da faixa correspondente — a mais clássica em sensoriamento remoto é a falsa cor "padrão" (infravermelho próximo no canal R, vermelho no canal G, verde no canal B), que realça vegetação saudável em tons de vermelho vivo (porque vegetação reflete fortemente no infravermelho próximo — mecanismo detalhado na Aula 03) e água em tons escuros a pretos (porque água absorve fortemente o infravermelho próximo). Para geologia especificamente, o que se busca é levar o **infravermelho de ondas curtas (SWIR)** para dentro da composição, porque é lá que estão as feições de absorção diagnósticas de argilominerais, óxidos e sulfatos (assunto que a Aula 03 desenvolve com as curvas espectrais específicas). O Landsat 8/9 tem apenas **duas** bandas SWIR (a 6, SWIR 1, e a 7, SWIR 2), de modo que nenhuma composição pode ocupar os três canais com SWIR — o padrão é usar as duas mais uma terceira banda de contraste: **7-6-2** (SWIR 2, SWIR 1, azul), a combinação convencionalmente rotulada de "geologia", e **7-6-4** (SWIR 2, SWIR 1, vermelho), rotulada de "infravermelho de ondas curtas", ambas boas para discriminar litologia, solo exposto e zonas de alteração. Convém registrar que esses rótulos são convenção de mercado e de software, não norma: fontes diferentes nomeiam combinações diferentes, e o que importa é saber quais bandas entraram em cada canal, não decorar um apelido.

Não existe uma composição "certa" universal — a escolha depende do que se quer realçar. Um geólogo interpretando estrutura regional pode preferir uma composição que maximize contraste topográfico e de drenagem; um geólogo de exploração mineral, uma composição voltada a alteração hidrotermal; um pedólogo, uma composição sensível a umidade e matéria orgânica do solo. A habilidade central desta aula, mais do que decorar uma combinação específica, é entender o princípio: cada composição é uma escolha deliberada de qual informação espectral se torna visível ao olho humano, e qual fica escondida.

## Exemplo trabalhado

**Situação:** uma equipe de exploração mineral recebe uma cena Landsat 9 (11 bandas, 30 m de resolução espacial nas bandas multiespectrais, 12 bits de radiometria) cobrindo uma área de 185 × 180 km no norte de Minas Gerais, e precisa decidir: (a) essa imagem serve para mapear alteração hidrotermal associada a um alvo de ouro orogênico de ~200 m de extensão? (b) que composição colorida melhor realça esse alvo? (c) quanto tempo, em média, até a próxima imagem livre de nuvens da mesma área?

**Resolução:**

*Parte (a) — resolução espacial adequada ao alvo.* A resolução espacial do Landsat (30 m) define o menor objeto que aparece como uma unidade distinta na imagem — na prática, para um alvo ser reconhecível com alguma confiança (não apenas teoricamente detectável), ele precisa se estender por vários pixels contíguos, uma regra empírica comum sendo ao menos 3-5 pixels no menor eixo. Um alvo de 200 m de extensão corresponde a cerca de 6-7 pixels de 30 m — no limite inferior do que é razoavelmente mapeável nessa resolução, mas ainda possível, sobretudo se o contraste espectral entre a zona alterada e a rocha encaixante for forte. Um alvo de 60 m (2 pixels) já seria inviável nessa resolução — exigiria uma imagem de resolução mais fina (Sentinel-2 nas bandas de 10-20 m, ou dados aerotransportados/VANT de resolução métrica a centimétrica).

*Parte (b) — composição adequada.* Para alteração hidrotermal (argilominerais, óxidos de ferro, sulfatos — minerais com feições de absorção diagnósticas no SWIR, conforme a Aula 03 vai detalhar), a composição recomendada leva as duas bandas SWIR do Landsat 8/9 para os canais R e G: bandas 7 (SWIR 2, 2,11-2,29 µm), 6 (SWIR 1, 1,57-1,65 µm) e 4 (vermelho, 0,64-0,67 µm) atribuídas a R-G-B — a composição 7-6-4 apresentada acima, ou sua irmã 7-6-2, que troca o vermelho pelo azul no terceiro canal que tende a separar zonas de argilização e oxidação da vegetação e da rocha fresca por contraste de cor. Uma composição em cor verdadeira (bandas 4-3-2) seria pouco útil aqui, porque a maior parte do contraste diagnóstico de alteração está fora do visível.

*Parte (c) — resolução temporal.* Como a constelação Landsat 8+9 revisita a mesma área a cada 8 dias em média (16 dias cada satélite, defasados), a próxima imagem "bruta" está a, no máximo, 8 dias. Mas a pergunta prática de campo não é "quando passa o satélite" e sim "quando passa o satélite **sem nuvem cobrindo o alvo**": em regiões de cobertura de nuvens frequente (boa parte do território brasileiro em época chuvosa), o intervalo real entre duas imagens utilizáveis pode ser de várias semanas a poucos meses — motivo pelo qual, para monitoramento contínuo em áreas de nuvem persistente, sensores ativos de micro-ondas (radar, Aula 06), que atravessam nuvens, são preferíveis a sensores ópticos passivos.

## Erros comuns

- **Achar que existe um sensor que maximiza as quatro resoluções ao mesmo tempo.** Elas competem por um orçamento fixo de dado e energia — melhorar uma quase sempre custa nas outras três. Escolher sensor é decidir qual trocar por qual, nunca "ter tudo".
- **Julgar se um alvo é mapeável só pela resolução espacial nominal, sem contar pixels sobre a extensão real do alvo.** Como o exemplo trabalhado mostra, um alvo de 200 m em pixels de 30 m já está no limite inferior (6-7 pixels); um de 60 m simplesmente não é mapeável nessa resolução, por melhor que seja o contraste espectral.
- **Confundir tempo de revisita do satélite com tempo até a próxima imagem utilizável.** Em áreas de nuvens frequentes, a imagem "bruta" chega no prazo nominal, mas a imagem sem nuvem sobre o alvo pode demorar semanas a meses — é por isso que radar (que atravessa nuvens) entra em cena para monitoramento contínuo.
- **Tratar os rótulos de composição colorida ("geologia", "infravermelho de ondas curtas") como padrão universal.** São convenção de mercado e de software, não norma — fontes diferentes nomeiam combinações diferentes; o que importa é saber quais bandas entraram em cada canal, não decorar o apelido.

## O que não concluir

- **Que composição em cor verdadeira é "a composição correta" por reproduzir a aparência real.** Para geologia é geralmente a menos útil: rochas e solos variam pouco em cor visível, e a informação diagnóstica mais forte está fora do visível (SWIR), onde a cor verdadeira nem olha.
- **Que resolução espectral mais alta (hiperespectral) é sempre a escolha certa.** Mais bandas estreitas significam mais volume de dado e complexidade de processamento — a resposta certa depende do problema, não é hierarquia de qualidade.
- **Que a identidade dos satélites Sentinel-2 (2A, 2B, 2C) é fixa.** O que é estável é o arranjo (dois satélites, revisita de 5 dias); quem ocupa essas posições muda — a aula registra explicitamente a substituição do 2A pelo 2C em 2025, e vale checar qual satélite gerou a cena antes de assumir parâmetros antigos.

## Recap relâmpago

- Sensoriamento remoto obtém informação sobre um alvo sem contato físico, medindo energia eletromagnética; plataforma é o veículo (satélite, aeronave, VANT), sensor é o instrumento de medição.
- Sensor passivo mede energia existente (luz solar refletida, calor emitido); sensor ativo emite sua própria energia e mede o retorno (radar, LiDAR) — e por isso opera de dia ou de noite e atravessa nuvens, diferença crucial em regiões tropicais.
- A maioria dos satélites de recursos naturais (Landsat, Sentinel-2) usa órbita heliossíncrona de baixa altitude, cruzando cada ponto sempre no mesmo horário solar local, para manter iluminação comparável entre datas.
- Quatro resoluções definem se uma imagem serve a um problema: espacial (tamanho do pixel no terreno), espectral (número/largura/posição das bandas), temporal (intervalo de revisita) e radiométrica (níveis de intensidade distinguíveis, em bits) — e melhorar uma tende a custar nas outras três.
- Landsat 8/9 (30 m, 11 bandas, ~8 dias combinado) e Sentinel-2 (10-60 m conforme a banda, 13 bandas, ~5 dias combinado com dois satélites em serviço — par nominal 2B+2C desde janeiro de 2025, com o 2A em campanha de extensão que adensa a revisita sobre a América do Sul) são os sensores ópticos gratuitos de referência; ASTER contribui bandas SWIR e termais raras noutros sensores, apesar de seu arquivo SWIR ser anterior a 2008.
- Uma composição colorida atribui três bandas quaisquer aos canais R-G-B de exibição — cor verdadeira reproduz a aparência a olho nu, falsa cor (como infravermelho-vermelho-verde, ou as combinações 7-6-2 e 7-6-4 do Landsat 8/9 para exploração mineral, que levam as duas únicas bandas SWIR do sensor mais uma terceira de contraste) revela informação espectral fora do alcance da visão humana; a escolha depende do que se quer realçar, não existe uma composição universalmente "certa".

## Próxima aula

[[14-sensoriamento-remoto-aula-02-fundamentos-fisicos-radiacao-eletromagnetica-espectro-atmosfera|Aula 02 — Fundamentos físicos: radiação eletromagnética, espectro e interação com a atmosfera]] — esta aula usou o espectro eletromagnético e a ideia de banda sem formalizar a física por trás; a próxima constrói essa base, necessária para entender por que cada alvo reflete de forma diferente em cada faixa (assunto da Aula 03).

## Fontes

- NASA/USGS, *Landsat 8 Data Users Handbook* e *Landsat 9 Data Users Handbook* (especificações de banda, resolução espacial, radiométrica e temporal do OLI/TIRS).
- ESA, *Sentinel-2 User Handbook* e SentiWiki/Copernicus (especificações de banda e resolução do MSI, revisita combinada 2A+2B).
- NASA/METI, *ASTER User Handbook* (bandas VNIR/SWIR/TIR, histórico de degradação do detector SWIR em 2008).
- Jensen, J. R. (2016), *Introductory Digital Image Processing: A Remote Sensing Perspective*, 4ª ed., Pearson, cap. 1-2 (conceitos de plataforma, sensor, resoluções, composições coloridas).
- Sabins, F. F. & Ellis, J. M. (2020), *Remote Sensing: Principles, Interpretation, and Applications*, 4ª ed., Waveland Press, cap. 1-3.

<!--
nivel: avancado
palavras_corpo: 2788
mapa_objetivo_secao:
  geologia-avancado-m14-oa02: "O que é sensoriamento remoto, e por que ele abre uma nova área do curso" + "Órbitas: por que a maioria dos satélites de recursos naturais é heliossíncrona" + "As quatro resoluções: o vocabulário que decide se uma imagem serve ao problema" + "Plataformas e sensores de referência em geologia" + "Composições coloridas: como transformar bandas em imagem interpretável" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: SENSREM-M14-A01-PASSIVOATIVO-001
    claim: "Sensor passivo mede energia eletromagnética existente no ambiente (luz solar refletida ou energia térmica emitida pelo alvo); sensor ativo emite sua própria energia (micro-ondas ou laser) e mede o retorno — exemplos centrais: radar (SAR) e LiDAR. Sensores ativos de micro-ondas atravessam nuvens e operam independentemente de luz solar."
    risk: fato
    source: "Jensen 2016, Introductory Digital Image Processing, cap. 1; Sabins & Ellis 2020, Remote Sensing, cap. 1"
  - claim_id: SENSREM-M14-A01-ORBITA-002
    claim: "Landsat 8/9 e Sentinel-2 operam em órbita heliossíncrona de baixa altitude (~700-800 km), cruzando cada ponto da superfície aproximadamente no mesmo horário solar local em toda passagem; órbitas geoestacionárias (~36.000 km, sobre o Equador) mantêm cobertura contínua da mesma área com resolução espacial muito mais grosseira."
    risk: fato
    source: "NASA/USGS Landsat 8/9 Data Users Handbook; ESA Sentinel-2 User Handbook"
  - claim_id: SENSREM-M14-A01-LANDSAT-003
    claim: "Landsat 8 e Landsat 9 (sensores OLI/TIRS) têm 11 bandas (incluindo 2 termais), resolução espacial de 30 m nas bandas multiespectrais, 15 m na pancromática e 100 m nas bandas termais, radiometria de 12 bits, e revisita individual de 16 dias cada, resultando em revisita combinada de aproximadamente 8 dias sobre a mesma área."
    risk: fato
    source: "NASA/USGS, Landsat 8 Data Users Handbook e Landsat 9 Data Users Handbook"
  - claim_id: SENSREM-M14-A01-SENTINEL-004
    claim: "Sentinel-2 (sensor MSI) tem 13 bandas espectrais em três resoluções espaciais conforme a banda (10 m, 20 m e 60 m), e revisita combinada de dois satélites em serviço simultâneo, defasados 180°, de aproximadamente 5 dias no Equador. O par nominal já não é 2A+2B: o Sentinel-2C substituiu o Sentinel-2A em operação nominal em 21 de janeiro de 2025 (par atual 2B+2C, com o 2D previsto para suceder o 2B), e o 2A segue desde março de 2025 numa campanha de extensão, defasado 36° do 2B, que aumenta a frequência de revisita sobre a Europa, a África tropical e a América do Sul."
    risk: fato
    source: "SentiWiki/Copernicus, S2 Mission (data da substituição 2C/2A e configuração da campanha de extensão); ESA Sentinel-2 User Handbook. Atualizado na auditoria do Modulo 14 (claim SENSREM-M14-A01-SENTINEL2C-008): a redacao anterior descrevia a constelação como 2A+2B, correto ate janeiro de 2025."
  - claim_id: SENSREM-M14-A01-ASTER-005
    claim: "O sensor ASTER, a bordo do satélite Terra, opera em 14 bandas (VNIR 15 m, SWIR 30 m, TIR 90 m) e encerrou a aquisição de novas bandas SWIR em 2008 por degradação do detector, mas seu arquivo histórico permanece referência em geologia mineral pela combinação de múltiplas bandas SWIR e termais."
    risk: fato
    source: "NASA/METI, ASTER User Handbook"
  - claim_id: SENSREM-M14-A01-COMPOSICAO-006
    claim: "O Landsat 8/9 (OLI) tem apenas DUAS bandas SWIR (banda 6, SWIR 1, e banda 7, SWIR 2), de modo que nenhuma composição colorida pode ocupar os tres canais RGB com bandas SWIR. As composições de falsa cor usadas em exploração mineral levam as duas bandas SWIR mais uma terceira banda de contraste: 7-6-2 (rotulada convencionalmente 'geologia') e 7-6-4 (rotulada 'infravermelho de ondas curtas'), ambas para realçar zonas de alteração hidrotermal (argilominerais, óxidos, sulfatos), cujas feições de absorção diagnósticas estão na faixa SWIR."
    risk: aproximacao
    source: "NASA/USGS, Landsat 8 Data Users Handbook (o OLI possui exatamente duas bandas SWIR); Sabins & Ellis 2020, Remote Sensing, cap. 3 e 6 (composições de exploração mineral); rótulos de combinação (geologia = 7-6-2, SWIR = 7-6-4, agricultura = 6-5-2, natural com remoção atmosférica = 7-5-3) são convenção de mercado e de software, NAO norma, e variam por fonte. Corrigido na auditoria do Modulo 14 (claim SENSREM-M14-A01-COMPOSICAO-005): a redacao anterior afirmava SWIR 'nos tres canais' — fisicamente impossível com o OLI — e listava 7-5-3 e 6-5-2 como as composições geológicas, divergindo do proprio exemplo trabalhado da aula, que usa 7-6-4."
-->
