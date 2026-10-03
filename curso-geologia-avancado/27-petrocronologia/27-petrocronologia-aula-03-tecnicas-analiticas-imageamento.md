# Aula 03: Técnicas analíticas e de imageamento — LA-ICP-MS, SIMS, TIMS, microssonda eletrônica (EPMA) e MEV

**ID:** geologia-avancado-m27-a03
**Módulo:** [[27-petrocronologia-modulo|Módulo 27 — Introdução à petrocronologia]]
**Duração estimada:** ~29 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** selecionar a técnica analítica adequada a um problema petrocronológico, reconhecendo a resolução espacial, a precisão e as limitações de cada uma.
**Ao final você vai conseguir:** comparar LA-ICP-MS, SIMS, TIMS e EPMA quanto a resolução espacial, precisão típica e natureza destrutiva ou não da análise; explicar o papel do MEV (imageamento por elétrons retroespalhados e catodoluminescência) como etapa que precede a escolha do ponto de análise; e decidir, diante de um cristal zonado real, qual técnica melhor resolve o problema.
**Pré-requisito:** [[27-petrocronologia-aula-02-sistemas-isotopicos-minerais-dataveis|Aula 02]] (quais minerais e sistemas isotópicos estão em jogo).

## Conteúdo

### Por que a técnica de medição é, em si, uma decisão petrocronológica

Na Aula 01, você viu que datar um grão inteiro por dissolução total pode misturar domínios de idades diferentes num número sem sentido geológico. A solução — análise **in situ**, dentro de um domínio específico do cristal — depende inteiramente da técnica analítica ter resolução espacial suficiente para "acertar" aquele domínio sem contaminar o sinal com o domínio vizinho. Por isso, nesta aula, a pergunta não é apenas "qual técnica é mais precisa", e sim "qual técnica resolve espacialmente o domínio que a textura (Aula 01) já me disse que preciso datar". As cinco técnicas discutidas aqui não competem entre si de forma absoluta: elas ocupam posições diferentes num compromisso entre resolução espacial, precisão analítica e caráter destrutivo da análise, e a escolha certa depende do problema.

### LA-ICP-MS: rapidez e volume de dados, ao custo de resolução espacial

A **espectrometria de massa com plasma indutivamente acoplado por ablação a laser** (LA-ICP-MS, do inglês *laser ablation inductively coupled plasma mass spectrometry*) usa um feixe de laser para vaporizar uma pequena porção da superfície polida do mineral; o material vaporizado é carregado por um gás de arraste até um plasma de argônio, que o ioniza, e os íons resultantes são separados por massa num espectrômetro. A grande vantagem prática é a velocidade: uma análise individual leva segundos a poucos minutos, permitindo datar dezenas a centenas de grãos numa única sessão — decisivo, por exemplo, em estudos de proveniência com zircões detríticos, ou quando se precisa de estatística populacional robusta sobre muitos grãos.

O preço dessa velocidade é a resolução espacial: crateras típicas de LA-ICP-MS variam de cerca de 10 a 40-50 μm de diâmetro, com profundidades de análise da ordem de dezenas de micrômetros (protocolos de alta resolução espacial chegam a operar com spots de 10-16 μm, mas normalmente sacrificando parte da precisão e da relação sinal-ruído). Isso significa que, num cristal com domínios muito finos — bordas metamórficas de poucos micrômetros de espessura, por exemplo —, o feixe de laser pode atravessar mais de um domínio ao mesmo tempo, misturando sinal de dois eventos numa única análise, exatamente o problema que a análise in situ deveria evitar. A precisão típica em idades individuais U-Pb por LA-ICP-MS gira em torno de 1-2% (2σ), suficiente para a maioria dos problemas petrocronológicos, mas inferior à de TIMS ou, em geral, à de SIMS. Uma variante importante para a petrocronologia é o **LASS** (*laser ablation split-stream*), em que o material ablacionado por um único pulso de laser é dividido e enviado simultaneamente a dois espectrômetros — um medindo a razão isotópica U-Pb, outro medindo elementos-traço (como Y e terras-raras pesados) no mesmo volume de material, no mesmo instante (Kylander-Clark, Hacker & Cottle, 2013). Essa simultaneidade é o que torna possível amarrar, ponto a ponto, uma idade a uma composição — o núcleo do método petrocronológico apresentado na Aula 01, agora com instrumentação dedicada.

### SIMS: volume amostrado muito menor, ao custo de tempo e acesso

A **espectrometria de massa de íons secundários** (SIMS, *secondary ion mass spectrometry*), na variante de alta resolução conhecida por instrumentos como o SHRIMP (*Sensitive High Resolution Ion MicroProbe*) e por sondas iônicas CAMECA, bombardeia a superfície do mineral com um feixe primário de íons (geralmente O⁻ ou Cs⁺) e coleta os íons secundários ejetados da própria amostra, separando-os por massa. A vantagem central sobre o LA-ICP-MS é o volume amostrado, muito menor: um pit típico de SHRIMP tem profundidade da ordem de 1-3 μm (contra profundidades de crateras de dezenas de micrômetros em LA-ICP-MS para tempos de análise comparáveis), o que reduz muito o risco de o feixe atravessar, em profundidade, um domínio que não se vê na superfície. Atenção ao que isso **não** significa: lateralmente, o pit do SIMS tem **~15-25 μm de diâmetro**, a mesma ordem de grandeza de um spot de LA-ICP-MS. Numa seção polida, uma borda de poucos micrômetros de largura não cabe num spot de SIMS tanto quanto não cabe num de laser; para bordas assim, a saída é o **perfil em profundidade** — montar o grão sem polir, com a face externa do cristal para cima, e deixar o feixe atravessar a borda de fora para dentro, registrando a mudança de idade à medida que o pit se aprofunda. A precisão típica também tende a ser melhor que a do LA-ICP-MS convencional. Em troca, o SIMS é mais lento por análise, exige laboratórios especializados com menor disponibilidade (o número de instrumentos SHRIMP e sondas CAMECA de alta resolução no mundo é bem menor que o de sistemas LA-ICP-MS), e o custo por análise é maior — o que limita, na prática, o número de pontos que um estudo consegue medir.

### TIMS: a maior precisão, ao custo de resolução espacial e de ser destrutivo

A **espectrometria de massa por ionização térmica** (TIMS, *thermal ionization mass spectrometry*) segue uma lógica completamente diferente das duas anteriores: em vez de analisar o mineral no lugar (in situ), o grão (ou um fragmento dele) é fisicamente dissolvido em ácido, o urânio e o chumbo são quimicamente separados e purificados, e a solução resultante é depositada sobre um filamento que, aquecido, ioniza os átomos para a medição. É um processo trabalhoso e totalmente destrutivo da porção de amostra usada, mas produz a maior precisão analítica disponível para idades U-Pb — a variante **ID-TIMS** (*isotope dilution*, com um traçador isotópico artificial adicionado à solução) combinada com o pré-tratamento de **abrasão química** (CA-ID-TIMS, de Mattinson, 2005, que aquece o grão entre 800-1100 °C por ~48 h para recozer o dano de radiação da estrutura cristalina e depois o submete a dissolução parcial em etapas, removendo domínios danificados que perderiam Pb) rotineiramente atinge precisões de 0,1% ou melhores — de dez a vinte vezes mais precisa que uma análise individual de LA-ICP-MS.

O custo dessa precisão é duplo: primeiro, a resolução espacial é baixa ou inexistente no sentido em que SIMS e LA-ICP-MS a entendem — mesmo quando se seleciona um fragmento pequeno de um cristal (microperfuração), não se consegue isolar um domínio de poucos micrômetros dentro de uma zona de crescimento sem dissolver junto material adjacente; segundo, a análise consome (destrói) o material, então não há possibilidade de reanalisar o mesmo ponto depois com outra técnica. Por isso, na prática petrocronológica, o TIMS costuma ser reservado para perguntas em que a máxima precisão da idade é mais importante que a resolução espacial fina — por exemplo, datar com altíssima precisão um evento já bem caracterizado texturalmente por outras técnicas, ou calibrar padrões de referência usados depois em análises in situ mais rápidas.

### EPMA: resolução espacial extrema, ao custo de precisão por ponto

A **microssonda eletrônica** (EPMA, *electron probe microanalyzer*) não mede razões isotópicas — mede concentrações elementares (com espectrometria de comprimento de onda, WDS) com precisão e exatidão muito altas, e em spots muito pequenos, tipicamente de 1-2 μm de diâmetro (chegando a menos de 1 μm em instrumentos modernos). Aplicada à monazita, essa capacidade deu origem a um método de datação inteiramente diferente dos anteriores, chamado **datação química de monazita** (Suzuki, Adachi & Kajizuka, 1994; Montel et al., 1996): como a monazita é extremamente rica em tório e urânio, o chumbo radiogênico se acumula rápido o bastante para ser medido diretamente em concentração (não em razão isotópica) já em rochas de dezenas de milhões de anos. Assumindo que o chumbo comum (não radiogênico) incorporado na cristalização é desprezível — hipótese que precisa ser verificada, não presumida —, é possível calcular uma idade a partir de apenas três concentrações medidas (Th, U, Pb) num único ponto, sem espectrômetro de massa algum.

A vantagem decisiva é a resolução espacial: como o spot de EPMA é cerca de dez vezes menor que um spot típico de SIMS e várias vezes menor que um de LA-ICP-MS, ele consegue mapear zoneamento composicional finíssimo dentro de um único cristal de monazita — domínios que nenhuma das outras três técnicas conseguiria isolar sem misturar sinal. O preço é a precisão por análise individual: uma idade química de monazita costuma ter incerteza da ordem de algumas dezenas de milhões de anos por ponto (tipicamente da ordem de ±30-50 Ma em rochas de algumas centenas de milhões de anos, aumentando proporcionalmente em rochas mais antigas), bem inferior à precisão relativa de LA-ICP-MS, SIMS ou TIMS. Na prática, o método é mais poderoso quando usado para **mapear** dezenas a centenas de pontos dentro de um único domínio composicional e depois combinar esses pontos estatisticamente (uma "idade de população", com incerteza agregada bem menor que a de qualquer ponto isolado) — não para produzir uma única idade de alta precisão. Essa lógica de mapeamento de idade por domínio composicional é retomada na Aula 06, quando o foco passa a ser a própria monazita como cronômetro.

### MEV: a etapa que decide onde analisar, não uma técnica de datação

O **microscópio eletrônico de varredura** (MEV, ou SEM, *scanning electron microscope*) não produz idades — produz as imagens que, na prática, decidem onde as quatro técnicas anteriores devem apontar o feixe. Duas modalidades de imageamento são centrais para a petrocronologia:

- **Elétrons retroespalhados (BSE, *backscattered electrons*)**: o contraste de brilho numa imagem BSE reflete o número atômico médio do material — regiões mais claras têm elementos mais pesados. Em minerais como monazita, titanita e granada, esse contraste revela zoneamento composicional (por exemplo, variação de Th ou de terras-raras) que orienta diretamente a escolha dos pontos de análise.
- **Catodoluminescência (CL, *cathodoluminescence*)**: o bombardeio de elétrons excita luminescência no cristal, sensível a defeitos estruturais e a certos elementos-traço (como terras-raras) — é a técnica-padrão para revelar o zoneamento oscilatório de zircão magmático e as bordas metamórficas sem zoneamento discutidas na Aula 01 (Corfu et al., 2003). Sem uma imagem CL prévia, escolher onde apontar um feixe de SIMS ou LA-ICP-MS num zircão zonado é, na prática, um chute às cegas quanto a que domínio de crescimento está sendo amostrado.

O fluxo de trabalho padrão da petrocronologia moderna segue, quase sempre, esta ordem: primeiro, imageamento por MEV (BSE e/ou CL) do grão inteiro, para mapear os domínios texturais; depois, seleção dos pontos de interesse com base nessa imagem; só então, a análise isotópica ou química propriamente dita, pela técnica escolhida conforme a resolução espacial e a precisão que o problema exige.

### As cinco técnicas lado a lado

Os números das seções acima, num só lugar:

| Técnica | O que mede | Resolução lateral | Profundidade amostrada | Precisão típica | In situ? |
|---|---|---|---|---|---|
| LA-ICP-MS (e LASS) | razões isotópicas; no LASS, também elementos-traço no mesmo volume | ~10-50 μm (10-16 μm em alta resolução) | dezenas de μm | ~1-2% (2σ) por idade U-Pb | sim |
| SIMS (SHRIMP, CAMECA) | razões isotópicas | ~15-25 μm | ~1-3 μm (perfil em profundidade para bordas finas) | em geral melhor que LA-ICP-MS | sim |
| CA-ID-TIMS | razões isotópicas, após dissolução química | nenhuma no sentido in situ (grão ou fragmento) | — | ~0,1% ou melhor | não: destrói a porção analisada |
| EPMA (datação química de monazita) | concentrações de Th, U e Pb | ~1-2 μm (menos de 1 μm nos instrumentos modernos) | — | ±30-50 Ma por ponto em rochas de centenas de Ma | sim |
| MEV (BSE, CL) | imagens de contraste composicional e de luminescência | — | — | não data | sim (etapa prévia) |

## Exemplo trabalhado: escolhendo a técnica certa para três problemas diferentes

**Problema 1 — datar, com a máxima precisão possível, um único evento de cristalização magmática já bem caracterizado por dados de campo e petrográficos, para calibrar a escala de tempo geológico de uma sequência vulcânica.** Aqui a resolução espacial fina não é o gargalo — o evento já está bem delimitado texturalmente. A escolha recai sobre **CA-ID-TIMS**, que entrega a maior precisão absoluta (tipicamente 0,1% ou melhor), ao custo de menos grãos analisados e de consumir o material.

**Problema 2 — reconstruir a história completa de um zircão metamórfico multi-domínio (núcleo herdado, sobrecrescimento magmático, borda metamórfica fina de poucos micrômetros) de uma mesma amostra, preservando os grãos para reanálise.** Aqui a resolução espacial é o gargalo decisivo, e a análise não pode ser destrutiva do grão inteiro. O fluxo começa com **imageamento CL por MEV** para mapear os domínios, seguido de **SIMS** para atingir cada domínio individualmente sem misturar sinal: spots na seção polida para o núcleo herdado e o sobrecrescimento magmático, que são largos o bastante para um pit de ~15-25 μm, e **perfil em profundidade por SIMS** num grão irmão montado sem polir para a borda de poucos micrômetros, que nenhum spot lateral resolveria (se a borda fosse larga o suficiente, LA-ICP-MS de alta resolução espacial também serviria).

**Problema 3 — mapear como a idade de crescimento de uma monazita varia ponto a ponto dentro de um zoneamento composicional complexo (múltiplos domínios de poucos micrômetros, ligados a diferentes reações metamórficas), produzindo um "mapa de idade" de todo o cristal.** Aqui o número de pontos necessários (dezenas a centenas) e a resolução espacial extrema tornam **EPMA** (datação química de monazita) a única escolha prática — SIMS e LA-ICP-MS simplesmente não têm resolução espacial suficiente para mapear domínios dessa escala em número tão grande de pontos, e TIMS nem sequer é uma opção espacialmente resolvida.

Nenhuma das três respostas é "a melhor técnica" em absoluto — cada uma é a melhor resposta para o par específico entre a pergunta geológica e a limitação física da técnica.

## Recap relâmpago

Os números de cada técnica estão na tabela "As cinco técnicas lado a lado"; o que levar desta aula é a regra de escolha:

- **Primeiro o MEV.** BSE e catodoluminescência não datam nada, mas mostram os domínios; sem essa etapa, a análise in situ perde o sentido que a Aula 01 lhe deu.
- **Muitos grãos, ou idade e composição no mesmo volume** → LA-ICP-MS (e LASS): rápido, precisão de ~1-2%, resolução moderada.
- **Domínio raso ou borda fina** → SIMS, que amostra um volume muito menor; lateralmente, porém, o spot é da ordem do de laser, e uma borda de poucos micrômetros se data por perfil em profundidade.
- **Máxima precisão num evento já caracterizado** → CA-ID-TIMS, aceitando destruir a porção analisada e abrir mão da resolução espacial.
- **Mapear zoneamento fino, ponto a ponto, na monazita** → EPMA, compensando a baixa precisão de cada ponto com muitos pontos.

## Próxima aula

[[27-petrocronologia-aula-04-petrologia-metamorfica-texturas-pt|Aula 04 — Fundamentos de petrologia metamórfica (Parte 1)]]: texturas, microdomínios e trajetórias P-T (a geotermobarometria vem na Parte 2, Aula 05) — a base petrológica que dá sentido geológico às idades e composições que as técnicas desta aula produzem.

## Fontes

- Kylander-Clark, A. R. C., Hacker, B. R. & Cottle, J. M. (2013), "Laser-ablation split-stream ICP petrochronology", *Chemical Geology*, 345, 99-112 — método LASS de medição simultânea de idade e composição.
- Corfu, F., Hanchar, J. M., Hoskin, P. W. O. & Kinny, P. (2003), "Atlas of Zircon Textures", Reviews in Mineralogy and Geochemistry, 53, 469-500 — imageamento por catodoluminescência como base para seleção de pontos de análise em zircão.
- Mattinson, J. M. (2005), "Zircon U-Pb chemical abrasion ('CA-TIMS') method: combined annealing and multi-step partial dissolution analysis for improved precision and accuracy of zircon ages", *Chemical Geology*, 220, 47-66. VERIFICADO por busca nesta redação (2026-09-22): título, volume, paginação, temperatura de recozimento (800-1100 °C, ~48 h) e precisão típica (0,1% ou melhor) confirmados (ADS, ScienceDirect).
- Suzuki, K., Adachi, M. & Kajizuka, I. (1994), "Electron microprobe observations of Pb diffusion in metamorphosed detrital monazites", *Earth and Planetary Science Letters*, 128, 391-405 — origem do método de datação química de monazita por microssonda. Paginação conferida no Crossref pela auditoria (2026-09-22), doi:10.1016/0012-821X(94)90158-9.
- Montel, J.-M., Foret, S., Veschambre, M., Nicollet, C. & Provost, A. (1996), "Electron microprobe dating of monazite", *Chemical Geology*, 131, 37-53. VERIFICADO por busca nesta redação (2026-09-22): título, volume, paginação e princípio do método (Pb radiogênico assumindo Pb comum desprezível) confirmados (ScienceDirect, doi 10.1016/0009-2541(96)00024-1).
- Williams, M. L., Jercinovic, M. J. & Hetherington, C. J. (2007), "Microprobe Monazite Geochronology: Understanding Geologic Processes by Integrating Composition and Chronology", *Annual Review of Earth and Planetary Sciences*, 35, 137-175. VERIFICADO por busca nesta redação (2026-09-22): título, volume e paginação confirmados (Annual Reviews, doi 10.1146/annurev.earth.35.031306.140228); resultado de busca também confirma resolução espacial de EPMA (~1-2 μm) e incerteza típica por ponto (dezenas de Ma).
- Resolução espacial comparativa de SHRIMP (pit ~1-3 μm de profundidade) vs. LA-ICP-MS (cratera de dezenas de μm de profundidade, spots de 10-50 μm) e precisão típica de LA-ICP-MS (~1-2%, 2σ): VERIFICADO por busca nesta redação (2026-09-22), com base em múltiplas fontes secundárias consistentes (incluindo comparações publicadas em periódicos revisados por pares); a compilação exata das fontes primárias não foi conferida ponto a ponto, e valores específicos podem variar por laboratório e protocolo — declarado como aproximação de referência, não constante fixa.
- Stanford-USGS SHRIMP-RG Laboratory, "Zircon U-Th-Pb and U-Th ages and trace element analyses" (https://shrimprg.stanford.edu/zircon-u-th-pb-and-u-th-ages-and-trace-element-analyses, consultado 2026-09-22) — pits de ~15-25 μm de diâmetro e ~2 μm de profundidade; perfil em profundidade de bordas metamórficas em faces de cristal não polidas. Acrescentado pela auditoria (2026-09-22).

<!--
nivel: avancado
palavras_corpo: 2456
palavras_corpo_metodo: "tokens separados por espaco entre '## Conteudo' e '## Fontes', seguindo a convencao do modulo 26."
duracao_estimada_min: 29

mapa_objetivo_secao:
  geologia-avancado-m27-oa02: "Por que a tecnica de medicao e, em si, uma decisao petrocronologica" + "LA-ICP-MS" + "SIMS" + "TIMS" + "EPMA" + "MEV" + "As cinco tecnicas lado a lado" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: PETROCRON-M27-A03-LAICPMS-ESPECS-001
    claim: "LA-ICP-MS produz crateras tipicas de ~10-50 micrometros de diametro (protocolos de alta resolucao chegam a 10-16 micrometros), com precisao tipica de idades U-Pb individuais de 1-2% (2sigma); a variante LASS mede simultaneamente idade isotopica e composicao elementar no mesmo volume ablacionado."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-22): resultados confirmam spots de 10-16 micrometros em protocolos de alta resolucao e precisao de ~1% para spots de 15-50 micrometros; Kylander-Clark, Hacker & Cottle (2013), Chemical Geology 345, 99-112, descreve o metodo LASS."
  - claim_id: PETROCRON-M27-A03-SIMS-VS-LAICPMS-002
    claim: "SIMS (SHRIMP) produz pits de profundidade muito menor que LA-ICP-MS para tempos de analise comparaveis (da ordem de 1-3 micrometros contra ~25 micrometros de profundidade), permitindo maior resolucao espacial; em troca, e mais lento por analise e depende de instrumentacao especializada menos disponivel."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-22): resultado de busca cita 'A 35-second laser analysis creates pits approximately 25 micrometers deep compared to a 2.5-micrometer pit in a typical SHRIMP analysis', confirmando resolucao espacial superior do SIMS. ACHADO 6 DA AUDITORIA (2026-09-22, laranja, corrigido): a superioridade e em PROFUNDIDADE/volume, nao lateral - o pit do SHRIMP tem ~15-25 um de diametro (SHRIMP-RG Stanford-USGS), a mesma ordem do LA-ICP-MS, e o texto concluia que SIMS atinge numa secao polida uma borda de poucos micrometros. Secao SIMS, Problema 2 do exemplo e recap reescritos: bordas finas se datam por perfil em profundidade em grao nao polido."
  - claim_id: PETROCRON-M27-A03-CATIMS-PRECISAO-003
    claim: "CA-ID-TIMS (Mattinson 2005) combina recozimento termico (800-1100 C por ~48h) com dissolucao parcial em etapas para remover dominios danificados por radiacao que perderiam Pb, atingindo rotineiramente precisoes de 0,1% ou melhores em idades U-Pb de ziracao - a maior precisao entre as tecnicas desta aula, ao custo de ser destrutiva e sem resolucao espacial fina."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-22): Mattinson (2005), Chemical Geology 220, 47-66, confirma temperatura de recozimento, metodo de dissolucao em etapas e precisao de 0,1% ou melhor."
  - claim_id: PETROCRON-M27-A03-EPMA-MONAZITA-004
    claim: "EPMA tem resolucao espacial de spot tipica de 1-2 micrometros (instrumentos modernos abaixo de 1 micrometro); aplicada a monazita, permite datacao quimica Th-U-Pb total (Suzuki, Adachi & Kajizuka 1994; Montel et al. 1996), assumindo Pb comum desprezivel, com incerteza tipica por ponto da ordem de dezenas de Ma (por exemplo ~30-50 Ma para rochas de centenas de Ma), compensavel mapeando muitos pontos e agregando estatisticamente."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-22): resultado de busca confirma 'high spatial resolution of 1-2 micrometer diameter... beam sizes down below 1 micrometer' e 'final precision on the age for a normal monazite is +/-30-50 Ma for a total counting time of 600s... typical precision is +/-30 Ma for a 300 Ma age and +/-100 Ma for a 3.0 Ga age'; Montel et al. (1996), Chemical Geology 131, 37-53, confirmado por busca quanto a titulo e principio do metodo."
  - claim_id: PETROCRON-M27-A03-MEV-IMAGEAMENTO-005
    claim: "O MEV nao produz idades; imageamento por eletrons retroespalhados (BSE, contraste por numero atomico medio) e por catodoluminescencia (CL, sensivel a defeitos estruturais e certos elementos-traco) revela zoneamento composicional e textural que orienta a escolha dos pontos de analise nas demais tecnicas, sendo a CL o metodo-padrao para revelar zoneamento oscilatorio magmatico e bordas metamorficas em ziracao."
    risk: fato
    source: "Principio consolidado de preparacao analitica em geocronologia in situ, documentado extensivamente em Corfu et al. (2003), Reviews in Mineralogy and Geochemistry 53, 469-500 (Atlas of Zircon Textures)."
  - claim_id: PETROCRON-M27-A03-EXEMPLO-TRES-PROBLEMAS-006
    claim: "Exemplo pedagogico: tres problemas hipoteticos (calibracao de escala de tempo com CA-ID-TIMS; ziracao metamorfico multi-dominio com MEV+SIMS; mapeamento de idade de monazita com EPMA) ilustrando que a escolha de tecnica depende do par entre pergunta geologica e limitacao fisica de cada metodo, nao de uma tecnica ser objetivamente 'melhor' que as outras."
    risk: hipotetico
    source: "Exemplo pedagogico construido especificamente para esta aula a partir dos tradeoffs tecnicos apresentados no corpo do texto, sem corresponder a um estudo de caso publicado especifico. AUDITORIA (2026-09-22): Problema 2 ajustado pelo achado 6 (SIMS por perfil em profundidade para a borda fina; enunciado passou de 'numa unica lamina' para 'de uma mesma amostra')."
auditoria:
  data: 2026-09-22
  achados: "6 (laranja, corrigido)"
  incertezas_declaradas_resolvidas: "paginacao de Suzuki, Adachi & Kajizuka 1994 - correta como citada; Kylander-Clark et al. 2013, Mattinson 2005, Montel et al. 1996, Williams et al. 2007 e Corfu et al. 2003 conferidos no Crossref"
revisao_didatica:
  data: 2026-09-22
  achados:
    - "DID-M27-A03-COMPARACAO-SEM-CONSOLIDACAO-004 (amarelo): o objetivo pede comparar quatro tecnicas em tres eixos e a aula nao tinha nenhum lugar onde a comparacao estivesse inteira; o recap repetia os numeros das secoes. Acrescentada a tabela 'As cinco tecnicas lado a lado' (so numeros ja no texto e ja auditados) e o recap foi reescrito como regra de escolha, sem numeros. Titulo da secao SIMS alinhado a correcao da auditoria (volume amostrado, nao resolucao lateral)."
    - "DID-M27-DURACOES-DECLARADAS-006 (amarelo): ~29,2 min reais (2456 palavras, tabela incluida) contra ~27 declarados."
-->
