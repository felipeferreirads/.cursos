# Aula 06: Modelos digitais de elevação: declividade, hipsometria, análise hidrológica e extração de lineamentos

**ID:** geologia-avancado-m13-a06
**Módulo:** [[13-geoprocessamento-modulo|Módulo 13 — Geoprocessamento]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** derivar variáveis morfométricas (declividade, hipsometria) e hidrológicas (direção e acumulação de fluxo, rede de drenagem) a partir de um modelo digital de elevação, e reconhecer lineamentos como feição de interesse geológico extraível desses produtos.
**Ao final você vai conseguir:** explicar a diferença entre MDT e MDS; calcular declividade a partir de um MDE; interpretar uma curva hipsométrica; descrever o algoritmo de direção de fluxo D8 e como ele gera uma rede de drenagem derivada; e explicar como lineamentos são extraídos de um MDE.
**Pré-requisito:** [[13-geoprocessamento-aula-02-ambiente-sig-estruturas-vetorial-e-matricial|Aula 02]]. Esta aula assume domínio do conceito de raster (célula, resolução) — o modelo digital de elevação é o exemplo canônico de dado raster contínuo em geociências, e toda a análise desta aula opera sobre ele célula a célula.

## Conteúdo

### O que é um modelo digital de elevação

Um **modelo digital de elevação (MDE)**, ou DEM (*Digital Elevation Model*), é um raster em que o valor de cada célula representa a altitude do terreno naquela posição — a estrutura de dados matricial (Aula 02) aplicada especificamente à variável elevação. É a partir do MDE que se calculam, por processamento de célula a célula e de vizinhança entre células, praticamente todas as variáveis morfométricas (relativas à forma do relevo) e hidrológicas (relativas ao escoamento da água) que interessam a um projeto de geociências — o objetivo desta aula, que fecha, junto com a Aula 07, o eixo de produtos derivados do módulo.

Uma distinção importante logo de início: um **MDT** (Modelo Digital de Terreno, ou DTM) representa a elevação da superfície do terreno "nu", excluindo vegetação, edificações e outros objetos sobre ele; um **MDS** (Modelo Digital de Superfície, ou DSM) representa a elevação do topo de tudo o que existe naquela posição — incluindo o topo da copa das árvores, o topo de um telhado. A diferença entre os dois pode ser de vários metros em área florestada e é frequentemente o próprio produto de interesse (a **altura da vegetação ou de estruturas**, calculada por subtração MDS − MDT). Para análise morfométrica e hidrológica do relevo — foco desta aula — o MDT é o produto correto: um MDS usado sem correção incorporaria a copa de árvores e telhados de edificações como se fossem parte do relevo real, distorcendo declividade, direção de fluxo e toda a análise hidrológica derivada.

A fonte mais comum de MDE de cobertura global gratuita é o **SRTM** (*Shuttle Radar Topography Mission*), missão de radar interferométrico voada em fevereiro de 2000, que adquiriu dados com espaçamento de 1 segundo de arco (~30 m) para quase todo o globo entre 60°N e 56°S. Vale conhecer a história da distribuição, porque ela ainda confunde: por restrição de política de dados, fora dos Estados Unidos só a versão reamostrada para 3 segundos de arco (~90 m) foi publicada por mais de uma década; a liberação global da resolução de 1 segundo de arco começou em setembro de 2014 e se completou ao longo de 2015 — a América do Sul entrou em novembro de 2014. Não houve, portanto, novo levantamento nem "refinamento" do dado: o que mudou foi o que passou a ser publicado. É por isso que material mais antigo descreve o SRTM como um MDE de 90 m, e por isso convém sempre checar qual versão do produto está em mãos. Modelos de maior resolução e precisão exigem levantamento aerofotogramétrico, LiDAR (temas do Módulo 14, Sensoriamento remoto) ou restituição a partir de curvas de nível de cartas topográficas de escala grande.

### Declividade

A **declividade** (ou inclinação, *slope*) de um ponto do terreno é a taxa de variação da altitude por unidade de distância horizontal naquele ponto, calculada, num MDE, a partir da diferença de altitude entre uma célula e suas células vizinhas imediatas (tipicamente as oito células ao redor, num algoritmo de janela móvel 3×3), e expressa em graus (0° a 90°, ângulo em relação ao plano horizontal) ou em porcentagem (razão entre a variação vertical e a distância horizontal, multiplicada por 100 — uma declividade de 100% corresponde a 45°). A declividade é a variável morfométrica de uso mais direto em geociências aplicadas: entra em modelos de suscetibilidade a movimento de massa (retomando o Módulo 05, Mecânica de rochas, e o Módulo 08, Geotecnia ambiental, agora com uma ferramenta para mapear a variável espacialmente em toda uma bacia, em vez de só no ponto de um talude específico), define restrições de uso do solo, e é insumo direto de modelos hidrológicos, porque controla a velocidade do escoamento superficial.

A qualidade do cálculo de declividade depende diretamente da resolução do MDE de entrada — um MDE de resolução grosseira (célula grande, como os 30 m do SRTM) suaviza rupturas de declive reais que existem no terreno numa escala menor que a célula, produzindo valores de declividade sistematicamente mais baixos que a declividade real de feições estreitas (uma escarpa, um talude de estrada), o mesmo problema de escala/resolução já discutido nas Aulas 01 e 02, agora com consequência direta sobre um produto quantitativo específico.

### Hipsometria e a curva hipsométrica

**Hipsometria** é o estudo da distribuição de altitudes numa área — tipicamente representada visualmente por um **mapa hipsométrico** (um raster de elevação classificado em faixas de altitude, cada faixa com uma cor, seguindo convenções cartográficas padronizadas de baixadas em verde a altitudes elevadas em marrom/branco) e analiticamente por uma **curva hipsométrica**, que representa, para uma bacia hidrográfica, a proporção da área da bacia que está acima de cada altitude relativa, normalizada de 0 a 1 tanto no eixo de altitude quanto no eixo de área.

A forma da curva hipsométrica é interpretada geomorfologicamente como um indicador do estágio evolutivo de uma bacia: uma curva convexa (área concentrada nas altitudes mais elevadas relativas) é característica de uma bacia geomorfologicamente jovem, ainda dominada por processos de incisão vertical ativa e pouco tempo de erosão acumulada; uma curva côncava (área concentrada nas altitudes mais baixas relativas) é característica de uma bacia madura ou senil, onde grande parte do relevo já foi rebaixado por erosão prolongada; uma curva sigmoidal, em forma de S, intermediária entre as duas, é característica de uma bacia em equilíbrio ou estágio maduro intermediário. Essa classificação (associada aos trabalhos clássicos de Strahler sobre geomorfologia quantitativa de bacias) transforma uma propriedade puramente geométrica derivada do MDE — a distribuição estatística de altitudes — num indicador interpretável do processo geomorfológico que esculpiu aquela paisagem.

```
Curvas hipsométricas — três estágios evolutivos (esquemático)

altitude relativa
1,0 ┤ ╲                    ╲___              
    │  ╲  jovem (convexa)      ╲   maduro         senil (côncava)
    │   ╲                       ╲  (sigmoide)     ╲___
    │    ╲___                    ╲___              ╲__
0,0 ┼──────────── área relativa ──────────────────────── 1,0
```
A legenda a reter: a mesma variável (altitude, extraída do MDE) reorganizada como proporção de área acumulada revela o estágio evolutivo do relevo — informação que não está visível olhando o MDE bruto.

### Análise hidrológica: direção e acumulação de fluxo

A análise hidrológica derivada de um MDE segue uma sequência lógica de processamento em etapas. Primeiro, o MDE geralmente precisa de um pré-processamento de **preenchimento de depressões** (*fill sinks*): pequenas depressões espúrias no MDE — muitas vezes artefatos de erro de medição ou de interpolação, não feições reais do terreno — interromperiam o fluxo simulado antes de chegar à drenagem principal, então são preenchidas até o ponto de transbordamento mais próximo antes da análise prosseguir.

Sobre o MDE preenchido, calcula-se a **direção de fluxo** (*flow direction*) de cada célula: o algoritmo mais tradicional e amplamente usado, o **D8** (*eight-direction*), atribui a cada célula uma única direção de escoamento, entre as oito células vizinhas (as quatro ortogonais e as quatro diagonais), escolhendo a direção de maior declividade descendente a partir daquela célula. A partir da direção de fluxo de todas as células, calcula-se a **acumulação de fluxo** (*flow accumulation*): para cada célula, o número de células a montante cujo fluxo, seguindo a cadeia de direções de fluxo célula a célula, converge para aquela célula — um valor que, na prática, representa a área de drenagem contribuinte (em número de células, convertível a área real multiplicando pela área de uma célula) acumulada até aquele ponto.

A **rede de drenagem derivada** é obtida aplicando um limiar (*threshold*) sobre o raster de acumulação de fluxo: células cuja acumulação excede o limiar escolhido são classificadas como parte do canal de drenagem, formando uma rede vetorizável de linhas que reproduz, com boa fidelidade quando o MDE tem resolução e qualidade adequadas, a rede de drenagem real observável em campo ou em imagem de satélite. A escolha do limiar é um parâmetro de julgamento: um limiar baixo gera uma rede de drenagem excessivamente densa e ramificada (incluindo microdrenagens efêmeras irrelevantes para a escala do projeto); um limiar alto omite canais reais de menor ordem. A partir da direção de fluxo é possível também delimitar automaticamente uma **bacia hidrográfica** (*watershed*) — a área de contribuição de todas as células cujo fluxo converge para um ponto de saída (*pour point*) especificado, como a foz de um rio ou a localização de uma barragem — operação que combina, célula a célula, toda a lógica de direção de fluxo descrita nesta seção.

```
Cadeia hidrológica derivada do MDE — cada etapa consome a saída da anterior

  MDE bruto
     │  preenchimento de depressões (fill sinks)
     ▼  remove depressões espúrias que travariam o fluxo simulado
  MDE hidrologicamente consistente
     │  direção de fluxo (D8): uma direção por célula, entre as 8 vizinhas,
     ▼  escolhida pela maior declividade descendente
  raster de DIREÇÃO de fluxo ─────────────────┐
     │  acumulação de fluxo:                   │ o mesmo raster de direção
     ▼  nº de células a montante que convergem │ alimenta as duas saídas
  raster de ACUMULAÇÃO de fluxo                ▼
     │  limiar (threshold):              delimitação de BACIA
     ▼  acumulação > limiar = canal      (tudo que converge para um
  REDE DE DRENAGEM derivada               ponto de saída escolhido)
```
A legenda a reter: são quatro produtos raster encadeados, e só os dois últimos passos envolvem escolha do analista — o limiar da rede de drenagem e o ponto de saída da bacia. Errar o preenchimento ou a direção de fluxo contamina tudo que vem depois, em silêncio.

### Extração de lineamentos

**Lineamentos** são feições lineares ou curvilíneas do relevo (ou de outros produtos derivados, como imagens de sensoriamento remoto, tema aprofundado no Módulo 14) que sugerem, mas não confirmam por si só, um controle estrutural subjacente — falhas, fraturas, zonas de cisalhamento — expresso na topografia por meio de alinhamentos de vales, mudanças abruptas de declividade, ou segmentos retilíneos anômalos na rede de drenagem derivada. A extração de lineamentos a partir de um MDE combina, tipicamente, um produto derivado chamado **relevo sombreado** (*hillshade* — uma simulação de iluminação do relevo a partir de uma direção de luz artificial escolhida, que realça visualmente rupturas de declive e alinhamentos sutis não óbvios no MDE bruto) com a inspeção visual ou semiautomática de padrões retilíneos anômalos na drenagem e no relevo.

O ponto crítico desta seção — e um dos mais importantes de toda a análise morfométrica derivada de MDE em geociências — é que **um lineamento identificado por geoprocessamento é uma hipótese de controle estrutural, não uma confirmação**. Um alinhamento retilíneo de vales pode de fato marcar uma zona de fraqueza estrutural aproveitada pela erosão diferencial (o caso de interesse geológico real), mas também pode resultar de um artefato do próprio processamento (a direção de iluminação escolhida no hillshade favorece certas orientações e disfarça outras — um viés conhecido do método, corrigível gerando hillshades com múltiplas direções de iluminação), de um controle litológico não estrutural (um contato entre rochas de resistência à erosão diferente, sem falha alguma), ou de uma feição antrópica (uma estrada, uma linha de transmissão, um canal de drenagem retificado). A verificação de campo do lineamento identificado remotamente — checar se há de fato uma zona de falha, fratura ou cisalhamento no local, e não apenas uma coincidência geométrica — é etapa obrigatória antes de qualquer interpretação estrutural ser dada como estabelecida, nunca opcional.

## Exemplo trabalhado

**Situação:** um MDE de resolução 12,5 m cobre uma bacia hidrográfica de 45 km². Após preenchimento de depressões, cálculo de direção de fluxo (D8) e acumulação de fluxo, o analista aplica um limiar de 500 células para definir a rede de drenagem derivada. Sabendo que a resolução do MDE é 12,5 m (célula de 12,5 × 12,5 m), qual é a área de drenagem contribuinte mínima (em km²) representada por esse limiar, e por que essa conversão importa na hora de comparar o resultado com a rede de drenagem real observada em campo ou em imagem de satélite?

**Resolução:**

Cada célula do MDE representa uma área de 12,5 m × 12,5 m = 156,25 m². O limiar de 500 células corresponde, portanto, a uma área de drenagem contribuinte mínima de:

Área mínima = 500 células × 156,25 m²/célula = 78.125 m²

Convertendo para km² (1 km² = 1.000.000 m²):

Área mínima = 78.125 / 1.000.000 = 0,078125 km² ≈ **0,078 km² (7,8 ha)**

Isso significa que a rede de drenagem derivada, com esse limiar, só representa como "canal" os pontos do terreno onde a área de contribuição acumulada a montante já atingiu pelo menos 0,078 km². Essa conversão importa porque o número "500 células" sozinho não tem significado hidrológico intuitivo — é apenas uma contagem de células, dependente da resolução do MDE usado. O mesmo limiar de 500 células, aplicado a um MDE de resolução 30 m (célula de 900 m²), corresponderia a uma área mínima de 500 × 900 = 450.000 m² = 0,45 km², quase seis vezes maior. Ou seja: **o mesmo valor numérico de limiar produz redes de drenagem hidrologicamente muito diferentes conforme a resolução do MDE de entrada** — um analista que compare a densidade de drenagem derivada de dois MDEs de resolução diferente, usando o mesmo limiar de células sem converter para área real, estaria comparando duas coisas metodologicamente distintas. A prática correta é sempre expressar (e documentar) o limiar em unidade de área (km² ou ha) de contribuição mínima, não apenas em número de células — permitindo comparação consistente entre MDEs de resolução diferente e uma escolha do limiar orientada pela escala real de drenagem esperada na bacia (informação que pode vir de mapas topográficos existentes ou de inspeção da drenagem visível em imagem de satélite de alta resolução), não por um valor arbitrário de contagem de células.

## Erros comuns

- **Usar MDS (com vegetação/edificações) para análise morfométrica ou hidrológica.** A copa de árvores e telhados não são relevo real — um MDS não corrigido distorce declividade, direção de fluxo e toda a rede de drenagem derivada. O produto correto para essa análise é sempre o MDT.
- **Comparar densidades de drenagem derivadas de MDEs de resolução diferente usando o mesmo limiar em número de células.** O próprio exemplo trabalhado mostra que 500 células significam áreas de contribuição quase seis vezes diferentes entre um MDE de 12,5 m e um de 30 m — o limiar precisa ser expresso em área real para ser comparável.
- **Interpretar um lineamento extraído por geoprocessamento como falha confirmada.** É uma hipótese de controle estrutural até verificação de campo — pode ser artefato de iluminação do hillshade, contato litológico sem falha, ou até uma estrada.
- **Aplicar declividade calculada de um MDE de 30 m a uma decisão que exige a declividade real de uma feição estreita** (uma escarpa, um talude). A resolução grosseira suaviza rupturas de declive reais menores que a célula, subestimando sistematicamente a declividade real.

## O que não concluir

- **Que "quanto menor o limiar, mais realista a rede de drenagem".** Um limiar baixo demais gera microdrenagem efêmera irrelevante para a escala do projeto; a escolha certa depende da escala de drenagem esperada na bacia, não de minimizar o limiar.
- **Que uma curva hipsométrica classifica a idade real (em anos) de uma bacia.** Ela indica estágio evolutivo relativo (jovem, maduro, senil) do ponto de vista geomorfológico — um indicador de processo dominante, não uma data absoluta.
- **Que preencher depressões do MDE é sempre corrigir um erro.** A maioria das depressões pequenas é artefato de medição ou interpolação, mas depressões reais (uma dolina cárstica, uma bacia endorreica genuína) também existem — preencher indiscriminadamente sem esse discernimento remove informação hidrológica real em terrenos cársticos ou áridos.

## Recap relâmpago

- MDT representa a elevação do terreno nu; MDS representa a elevação do topo de tudo sobre ele (vegetação, edificações); análise morfométrica/hidrológica exige o MDT, sob risco de distorção por vegetação ou construções.
- Declividade é calculada, célula a célula, a partir da diferença de altitude entre uma célula e suas vizinhas (janela 3×3); sua qualidade depende diretamente da resolução do MDE de entrada.
- A curva hipsométrica normaliza a distribuição de altitude de uma bacia em proporção de área acumulada; sua forma (convexa, sigmoide, côncava) indica o estágio evolutivo geomorfológico da bacia (jovem, maduro, senil).
- A análise hidrológica segue uma sequência: preenchimento de depressões, direção de fluxo (algoritmo D8, escolhendo a maior declividade descendente entre 8 vizinhos), acumulação de fluxo (célula a montante convergindo), e rede de drenagem derivada por limiar de acumulação.
- O limiar de acumulação de fluxo deve ser expresso em área real (não apenas em número de células), porque o mesmo número de células representa áreas de contribuição muito diferentes conforme a resolução do MDE.
- Lineamentos extraídos de MDE (frequentemente com apoio de hillshade) são hipóteses de controle estrutural, não confirmação — exigem verificação de campo antes de qualquer interpretação estrutural definitiva.

## Próxima aula

[[13-geoprocessamento-aula-07-layout-cartografico-normatizado-e-projeto-integrado|Aula 07 — Layout cartográfico normatizado e projeto integrado de geoprocessamento]]

## Fontes

- Strahler, A. N. (1952), "Hypsometric (Area-Altitude) Analysis of Erosional Topography", *Geological Society of America Bulletin*, 63(11), 1117-1142 (curva hipsométrica e estágios evolutivos).
- O'Callaghan, J. F. & Mark, D. M. (1984), "The extraction of drainage networks from digital elevation data", *Computer Vision, Graphics, and Image Processing*, 28(3), 323-344 (algoritmo D8, direção e acumulação de fluxo).
- Jensen, J. R. (2016), *Introductory Digital Image Processing*, 4ª ed., Pearson, cap. 8 (hillshade, lineamentos, produtos morfométricos derivados de MDE).
- USGS/NASA, *SRTM (Shuttle Radar Topography Mission)*, documentação técnica de referência sobre origem e resolução do produto.

<!--
nivel: avancado
palavras_corpo: 2460  # recontado apos auditoria + revisao didatica (2026-09-08)
mapa_objetivo_secao:
  geologia-avancado-m13-oa04: "O que é um modelo digital de elevação" + "Declividade" + "Hipsometria e a curva hipsométrica" + "Análise hidrológica: direção e acumulação de fluxo" + "Extração de lineamentos" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOPROC-M13-A06-MDTMDS-001
    claim: "MDT (Modelo Digital de Terreno) representa a elevação da superfície do terreno excluindo vegetação e edificações; MDS (Modelo Digital de Superfície) representa a elevação do topo de todos os objetos presentes, incluindo vegetação e construções; a diferença MDS menos MDT é usada para estimar altura de vegetação ou de estruturas."
    risk: fato
    source: "Jensen 2016, Introductory Digital Image Processing, cap. 8; terminologia padrão de sensoriamento remoto/fotogrametria"
  - claim_id: GEOPROC-M13-A06-SRTM-002
    claim: "O SRTM (Shuttle Radar Topography Mission) é uma missão de radar interferométrico voada em fevereiro de 2000, que adquiriu dados com espaçamento de 1 segundo de arco (~30 m) para quase todo o globo entre 60°N e 56°S; fora dos Estados Unidos, porém, apenas a versão de 3 segundos de arco (~90 m) foi publicada até a liberação global de 1 segundo de arco, iniciada em setembro de 2014 (América do Sul em novembro de 2014) e completada em 2015. A diferença entre as versões é de política de distribuição, não de novo levantamento."
    risk: fato
    source: "USGS EROS Archive — SRTM 1 Arc-Second Global; NASA Earthdata, SRTM Version 3.0 global 1 arc second release (setembro de 2014)"
    audit_note: "Corrigido na auditoria do Módulo 13 (achado GEOPROC-M13-A06-SRTM-002, laranja): a versão original descrevia a disponibilidade de 30 m como 'refinamento de cobertura completada em anos posteriores', sugerindo melhoria do dado em vez de liberação de dado já existente."
  - claim_id: GEOPROC-M13-A06-DECLIVIDADE-003
    claim: "A declividade em um MDE é calculada a partir da diferença de altitude entre uma célula central e suas células vizinhas (tipicamente janela móvel 3x3, oito vizinhos), expressa em graus (0-90°) ou em porcentagem (100% equivale a 45°); a qualidade do cálculo depende diretamente da resolução espacial do MDE de entrada."
    risk: fato
    source: "Burrough & McDonnell 1998, Principles of GIS, cap. 8 (análise de superfície); relação percentual-graus é conversão trigonométrica padrão (tan 45° = 1 = 100%)"
  - claim_id: GEOPROC-M13-A06-HIPSOMETRIA-004
    claim: "A curva hipsométrica de Strahler (1952) relaciona a proporção de área de uma bacia acima de cada altitude relativa; curva convexa indica bacia geomorfologicamente jovem, sigmoide indica estágio maduro intermediário, côncava indica bacia madura/senil."
    risk: fato
    source: "Strahler 1952, Hypsometric (Area-Altitude) Analysis of Erosional Topography, GSA Bulletin 63(11)"
  - claim_id: GEOPROC-M13-A06-D8-005
    claim: "O algoritmo D8 (eight-direction flow) atribui a cada célula de um MDE uma única direção de escoamento entre as oito células vizinhas, escolhendo a direção de maior declividade descendente; a acumulação de fluxo resultante representa, para cada célula, o número de células a montante cujo fluxo converge para ela, proporcional à área de drenagem contribuinte."
    risk: fato
    source: "O'Callaghan & Mark 1984, The extraction of drainage networks from digital elevation data, Computer Vision, Graphics, and Image Processing 28(3)"
  - claim_id: GEOPROC-M13-A06-LINEAMENTO-006
    claim: "Lineamentos extraídos de MDE ou de produtos derivados (como hillshade) representam hipóteses de controle estrutural (falha, fratura, zona de cisalhamento) que podem também resultar de artefato do processamento (viés de direção de iluminação do hillshade), controle litológico não estrutural ou feição antrópica, exigindo verificação de campo antes de interpretação estrutural definitiva."
    risk: fato
    source: "Jensen 2016, Introductory Digital Image Processing, cap. 8; prática consolidada de interpretação estrutural remota em geologia estrutural e sensoriamento remoto"
-->
