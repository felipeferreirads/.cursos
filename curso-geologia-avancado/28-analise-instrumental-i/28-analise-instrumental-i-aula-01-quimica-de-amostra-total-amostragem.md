# Aula 01: Química de amostra total — amostragem, representatividade e contaminação

**ID:** geologia-avancado-m28-a01
**Módulo:** [[28-analise-instrumental-i-modulo|Módulo 28 — Análise instrumental I]]
**Duração estimada:** ~25 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** entender por que a qualidade de uma análise química de rocha depende, antes de qualquer instrumento, de uma estratégia de amostragem que controle heterogeneidade e contaminação.
**Ao final você vai conseguir:** explicar por que "amostra representativa" é um conceito estatístico e não intuitivo; estimar, pela regra do cubo do diâmetro, quanto cresce a massa mínima de amostra quando o tamanho de partícula relevante aumenta; e listar as principais fontes de contaminação numa cadeia de amostragem e reduzi-las na prática.
**Pré-requisito:** nenhum dentro deste curso. Assume-se noção de estatística básica de graduação (média, desvio-padrão, variância) e familiaridade com litologias e texturas de rochas ígneas e sedimentares.

## Conteúdo

### Por que "amostra representativa" não é óbvio

Quando um geólogo de campo coleta um bloco de 2 kg de um afloramento granítico para "saber a composição química da rocha", ele está implicitamente assumindo que esse bloco representa um corpo rochoso que pode ter centenas de metros cúbicos, com variações modais, texturais e de tamanho de grão que o olho não capta inteiramente. A pergunta que a **química de amostra total** (*whole-rock geochemistry*) precisa responder antes de qualquer análise instrumental é: essa amostra, na massa e na forma em que chega ao laboratório, tem alta probabilidade estatística de refletir a composição média do corpo que ela pretende representar?

Essa pergunta não é retórica. Ela tem uma resposta quantitativa, formalizada pela **teoria da amostragem** desenvolvida pelo engenheiro francês Pierre Gy a partir da década de 1950 para minérios e materiais particulados, e sistematizada em livros de referência como Pitard (1993), *Pierre Gy's Sampling Theory and Sampling Practice*, 2ª ed., CRC Press. A ideia central de Gy é que todo material particulado ou heterogêneo carrega um **erro fundamental de amostragem** (*fundamental sampling error*, FSE) que depende da heterogeneidade intrínseca do material — não é um erro do analista, é um limite estatístico da própria amostra, e existe mesmo antes de qualquer instrumento entrar em cena.

### Heterogeneidade de constituição e massa mínima de amostra

A heterogeneidade que mais importa em geoquímica de rocha total é a **heterogeneidade de constituição**: partículas diferentes (grãos minerais diferentes) têm composições químicas diferentes, e a proporção de cada mineral na porção coletada varia com o tamanho do fragmento amostrado em relação ao tamanho de grão da rocha. Um granito de granulação grossa, com megacristais de K-feldspato de 3 cm, exige uma massa de amostra muito maior para representar bem a proporção modal de K-feldspato do que um basalto afanítico de grão submilimétrico — porque a chance de um fragmento pequeno cair sobre um megacristal (ou sobre nenhum) introduz uma variância muito maior na composição medida.

Gy formalizou essa relação numa equação que estima a variância relativa do erro fundamental de amostragem em função da massa da amostra, do tamanho máximo de partícula, da densidade e de um conjunto de fatores de forma, liberação e composição mineral (fator de heterogeneidade). Na prática de laboratório de geoquímica, essa formalização se traduz numa regra prática amplamente citada, que decorre diretamente do termo de diâmetro de partícula ao cubo (d³) da fórmula de Gy e que, em mineração, aparece como a "linha de segurança" dos nomogramas de amostragem: a massa mínima de amostra necessária para manter um erro relativo aceitável cresce aproximadamente com o **cubo do diâmetro máximo de partícula** — dobrar o tamanho de grão relevante da rocha (ou do fragmento de britagem) multiplica por cerca de oito a massa mínima exigida para o mesmo erro relativo. É por isso que protocolos de amostragem de minério para elementos que ocorrem em grãos raros e grandes (como o ouro nativo em veios de quartzo, o caso clássico do chamado "efeito pepita", *nugget effect*) exigem massas de amostra ordens de grandeza maiores do que protocolos para um elemento maior distribuído homogeneamente na rede cristalina de um mineral formador de rocha comum, como o Fe em olivina de um basalto.

Para a rotina de rocha total em geoquímica ígnea e metamórfica — o alvo principal deste módulo — a implicação prática mais imediata não é tanto calcular a fórmula de Gy explicitamente (isso é mais comum em geoquímica exploratória e controle de qualidade de minério), mas internalizar o princípio: **quanto mais grossa e mais heterogênea a rocha, maior a massa de campo necessária e mais crítica é a etapa de homogeneização em laboratório**, tratada na Aula 02.

### Representatividade ao longo da cadeia, não só na coleta

Um erro comum é pensar que a representatividade se resolve inteiramente no campo. Na verdade, a amostra passa por uma **cadeia de subamostragem**: do afloramento para o bloco de mão, do bloco de mão para o material britado, do britado para o pulverizado, do pó para a alíquota pesada para o forno ou para a digestão ácida. Cada etapa de redução de massa é, ela mesma, uma nova operação de amostragem, sujeita ao mesmo princípio de Gy — e cada uma introduz seu próprio incremento de erro, que se propaga e se soma (em quadratura, quando os erros são independentes) ao longo da cadeia. Um protocolo de amostragem mal desenhado em qualquer elo — por exemplo, retirar sempre a "colherada de cima" de um saco de pó sem homogeneizar, o que favorece partículas mais finas que se acumulam no topo por segregação granulométrica — introduz um viés sistemático que nenhuma precisão instrumental (Aula 06) consegue corrigir depois.

Rollinson (1993), em *Using Geochemical Data: Evaluation, Presentation, Interpretation* (Longman), sintetiza esse ponto para geólogos: a interpretação petrogenética de um diagrama de elementos-traço só é tão boa quanto a amostra que a alimenta. A teoria de Gy separa aqui duas coisas que convém não confundir. O **erro fundamental de amostragem** é **aleatório**: sua média é praticamente nula e ele aparece como dispersão entre amostras replicadas (em elementos concentrados em grãos raros, com distribuição assimétrica, em que a maioria das amostras pequenas subestima o teor). Já os erros de **amostragem incorreta** — segregação, delimitação ou extração malfeitas, como a "colherada de cima" — introduzem **viés sistemático**, deslocando toda uma população de dados na mesma direção. O ponto comum, e o que importa na prática, é que **nenhum dos dois aparece na réplica instrumental**: repetir a leitura da mesma solução não revela nem a dispersão nem o viés da amostragem, só réplicas da própria etapa de amostragem o fazem.

### Contaminação: onde ela entra e como controlar

Além da representatividade estatística, a segunda ameaça à qualidade de uma amostra de rocha total é a **contaminação** introduzida pelo próprio processo de preparação. As fontes mais documentadas na literatura de preparação de amostras geoquímicas (ver Potts, 1987, *A Handbook of Silicate Rock Analysis*, Blackie/Chapman & Hall, capítulo de preparação de amostra) incluem:

- **Contaminação por equipamento de britagem e moagem**: britadores de mandíbula de aço ao carbono e moinhos de bola ou de disco podem introduzir Fe, Cr, Co, Ni, Mn e W (este último especialmente de moinhos de carboneto de tungstênio) em concentrações relevantes para análise de elementos-traço, mesmo que insignificantes para elementos maiores. É por isso que laboratórios especializados em elementos-traço evitam moinhos de aço quando o objetivo inclui Cr, Ni ou Co, preferindo ágata, alumina ou carboneto de tungstênio conforme o elemento de interesse — e reportam a especificação do equipamento usado, prática de transparência analítica.
- **Contaminação cruzada entre amostras**: partículas residuais de uma amostra anterior alojadas em juntas do britador, no disco do moinho ou na parede do almofariz. O controle padrão é o uso de uma alíquota de material de "lavagem" (geralmente quartzo puro ou uma porção da própria amostra seguinte, descartada) processada e descartada entre amostras.
- **Contaminação ambiental**: poeira de laboratório, umidade, e reagentes de pureza insuficiente introduzidos nas etapas seguintes de digestão (Aula 02).

O controle de qualidade contra contaminação não é apenas processual — ele é **verificável empiricamente**, e essa verificação é o elo direto com o restante do módulo: material de referência certificado (MRC, discutido na Aula 02), brancos de procedimento e réplicas processadas do início ao fim da cadeia (não só reinjetadas no instrumento) são a forma padrão de detectar contaminação introduzida pela preparação, antes mesmo de qualquer consideração sobre o instrumento analítico em si.

## Exemplo trabalhado: escolhendo a massa de amostra para um pórfiro cuprífero vs. um basalto afanítico

**Situação.** Um geólogo precisa decidir a massa de amostra de campo para dois materiais: (a) um basalto afanítico de grão fino (tamanho de grão médio ~0,5 mm), homogêneo a olho nu, para análise de elementos maiores e traço de rocha total; e (b) um pórfiro cuprífero com fenocristais de plagioclásio de até 8 mm e veios de quartzo-sulfeto centimétricos, para análise de Cu e Au visando um estudo de recursos.

**Raciocínio.** Para o basalto, o tamanho de grão pequeno e a distribuição relativamente homogênea dos minerais formadores de rocha (plagioclásio, piroxênio, óxidos de Fe-Ti finamente dispersos) significam que mesmo uma amostra de 1 a 2 kg reduzida a um fragmento representativo de algumas centenas de gramas para o laboratório tem erro fundamental de amostragem pequeno para elementos maiores e para a maioria dos traços — a heterogeneidade de constituição é baixa porque nenhum mineral está concentrado em partículas grandes e raras.

Para o pórfiro cuprífero, dois fatores pioram a heterogeneidade: o tamanho de partícula relevante é maior (fenocristais de 8 mm, mas sobretudo os veios de sulfeto, que podem ter espessura de centímetros e concentrar quase todo o Cu e Au da rocha em um volume pequeno e descontínuo), e a distribuição do elemento de interesse é fortemente desigual — a maior parte do cobre e praticamente todo o ouro estão em sulfetos que ocupam uma fração pequena do volume da rocha. Esse é exatamente o cenário em que a equação de Gy prevê que a massa mínima necessária cresce de forma acentuada: uma amostra de 1 a 2 kg, adequada para o basalto, seria estatisticamente inadequada para Au num pórfiro com efeito pepita, podendo tanto superestimar (se o fragmento capturar um grão rico) quanto subestimar (se não capturar nenhum) o teor real do corpo. Protocolos de exploração para Au tipicamente exigem amostras de vários quilos a dezenas de quilos, ou compostagem de múltiplos incrementos ao longo de um intervalo, exatamente para reduzir esse erro a um nível aceitável — e mesmo assim reportam duplicatas de campo como controle de qualidade padrão.

**Ordem de grandeza pela regra do cubo.** Só o termo d³, com os demais fatores da fórmula de Gy mantidos fixos, já dá a escala do problema. O tamanho de partícula relevante passa de ~0,5 mm (basalto) para ~8 mm (fenocristais do pórfiro): 16 vezes maior. A massa mínima cresce com o cubo dessa razão, 16³ ≈ 4100 vezes. O número não é uma previsão de massa — os outros fatores mudam de uma rocha para a outra, e no caso do Au a concentração do elemento em poucos grãos pesa tanto quanto o tamanho —, mas mostra por que a massa que basta para o basalto não chega nem perto de bastar para o pórfiro. O mesmo raciocínio vale ao contrário, e é a razão de britar e pulverizar antes de subamostrar: reduzir o tamanho de partícula à metade divide por oito a massa mínima de cada etapa seguinte da cadeia.

**Conclusão prática.** A massa de amostra não é uma convenção fixa de laboratório — é uma decisão que depende do tamanho de grão relevante, da distribuição do elemento de interesse e do nível de erro relativo tolerável para a decisão geológica ou econômica em jogo. Definir essa massa **antes** da coleta de campo é parte do planejamento analítico, não um detalhe operacional de laboratório.

## Recap relâmpago

- A química de amostra total depende, antes de qualquer instrumento, de uma amostra estatisticamente representativa do corpo rochoso — problema formalizado pela teoria de amostragem de Pierre Gy (ver Pitard, 1993).
- A heterogeneidade de constituição (composição diferente entre partículas) faz a massa mínima de amostra necessária crescer aproximadamente com o cubo do tamanho máximo de partícula relevante: rochas grossas ou com o elemento de interesse concentrado em grãos raros (efeito pepita) exigem amostras muito maiores.
- A representatividade se decide ao longo de toda a cadeia de subamostragem (campo → britagem → pulverização → alíquota), não só na coleta de campo; cada etapa de redução de massa é, ela mesma, uma operação de amostragem sujeita ao mesmo princípio.
- O erro fundamental de amostragem é aleatório (dispersão entre amostras replicadas); a amostragem incorreta (segregação, "colherada de cima") introduz viés sistemático. Nenhum dos dois aparece na réplica instrumental, e nenhuma precisão instrumental corrige um viés introduzido antes do instrumento.
- Contaminação de preparação (britadores e moinhos de aço introduzindo Fe, Cr, Ni, Co, W; contaminação cruzada; poeira e reagentes) é controlada por escolha de equipamento adequado ao elemento de interesse, material de lavagem entre amostras, e verificada empiricamente por brancos, réplicas e materiais de referência certificados.

## Próxima aula

[[28-analise-instrumental-i-aula-02-preparacao-de-amostras-metodos-classicos|Aula 02 — Preparação de amostras e métodos analíticos clássicos]]: como o material coletado e amostrado segundo os princípios desta aula é efetivamente reduzido, homogeneizado e transformado (por fusão ou digestão ácida) numa forma que os instrumentos das aulas seguintes podem medir.

## Fontes

- Pitard, F. F. (1993), *Pierre Gy's Sampling Theory and Sampling Practice: Heterogeneity, Sampling Correctness, and Statistical Process Control*, 2ª ed., CRC Press. VERIFICADO por busca nesta redação (2026-09-23): título, autor, editora e ano confirmados (Amazon, AbeBooks, Google Books, WorldCat).
- Potts, P. J. (1987), *A Handbook of Silicate Rock Analysis*, Blackie & Son (EUA: Chapman & Hall). VERIFICADO por busca nesta redação (2026-09-23): editora, ano e 622 páginas confirmados (Cambridge Core, resenhas em *Clay Minerals* e *Mineralogical Magazine*, American Mineralogist).
- Rollinson, H. (1993), *Using Geochemical Data: Evaluation, Presentation, Interpretation*, Longman. Referência padrão de graduação/pós-graduação em interpretação de dados geoquímicos; título, autor, editora e ano conferidos na auditoria (2026-09-23).
- Minnitt, R. C. A., Rice, P. M. & Spangenberg, C. (2007), "Part 1: Understanding the components of the fundamental sampling error: a key to good sampling practice", *Journal of the Southern African Institute of Mining and Metallurgy*, 107(8), 505-511 — decomposição do erro total de amostragem de Gy em componentes aleatórios (entre eles o erro fundamental) e componentes de viés (amostragem incorreta). Acrescentada pela auditoria (2026-09-23).

<!--
nivel: avancado
palavras_corpo: 2075
recontagem_didatica: "Recontado por script na revisao didatica de 2026-09-23, depois da ultima edicao, a ~84 palavras/min (achado DID-M28-DURACOES-DECLARADAS-006). Valor declarado antes: 1720."
palavras_corpo_metodo: "tokens separados por espaco entre '## Conteudo' e '## Fontes', incluindo tabelas, seguindo a convencao do modulo 26/27."
duracao_estimada_min: 25

mapa_objetivo_secao:
  geologia-avancado-m28-oa01: "Por que 'amostra representativa' não é óbvio" + "Heterogeneidade de constituição e massa mínima de amostra" + "Representatividade ao longo da cadeia, não só na coleta" + "Contaminação: onde ela entra e como controlar" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: ANINST-M28-A01-TEORIA-GY-FSE-001
    claim: "A teoria da amostragem de Pierre Gy formaliza um 'erro fundamental de amostragem' (FSE) que depende da heterogeneidade intrinseca do material particulado, sistematizada por Pitard (1993) em livro de referencia de mesmo tema."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-23): Pitard, F.F. (1993), Pierre Gy's Sampling Theory and Sampling Practice, 2a ed., CRC Press, confirmado por multiplas fontes (Amazon, AbeBooks, WorldCat, Google Books)."
  - claim_id: ANINST-M28-A01-MASSA-CUBO-DIAMETRO-002
    claim: "A massa minima de amostra necessaria para um erro relativo aceitavel cresce aproximadamente com o cubo do diametro maximo de particula relevante, de forma que dobrar o tamanho de grao relevante multiplica por cerca de oito a massa minima exigida."
    risk: fato
    source: "Consequencia direta da formula de variancia do erro fundamental de amostragem de Gy, que inclui o termo de diametro de particula elevado ao cubo (d^3) multiplicando o fator de heterogeneidade; relacao classica discutida em Pitard (1993). [AUDITORIA 2026-09-23: a atribuicao original a 'regra de Visman' foi retirada - Visman (1969) e outra formulacao (variancia A/w + B/n), nao a regra do cubo.]"
    incerteza: "o fator multiplicador exato 'cerca de oito' depende dos demais parametros da formula de Gy (fator de forma, fator de liberacao, fator de heterogeneidade de composicao) e e uma aproximacao pedagogica da relacao cubica, nao uma constante universal."
  - claim_id: ANINST-M28-A01-EFEITO-PEPITA-AU-003
    claim: "O 'efeito pepita' (nugget effect) descreve a alta variancia de amostragem de elementos como ouro nativo, que ocorrem concentrados em graos raros e grandes, exigindo amostras de campo maiores (tipicamente de varios kg a dezenas de kg) do que elementos formadores de rede cristalina distribuidos homogeneamente."
    risk: fato
    source: "Termo e fenomeno amplamente documentados na literatura de exploracao mineral e geoestatistica (ja tratado no Modulo 20 deste curso); consistente com a teoria de amostragem de Gy aplicada a Au. Ordem de grandeza de massa ('varios kg a dezenas de kg') e uma generalizacao pedagogica de protocolos de exploracao, nao um numero de norma especifica citada."
  - claim_id: ANINST-M28-A01-FONTES-CONTAMINACAO-004
    claim: "Equipamentos de britagem e moagem de aco ao carbono podem introduzir Fe, Cr, Co, Ni e Mn; moinhos de carboneto de tungstenio podem introduzir W; por isso laboratorios de elementos-traco evitam aco quando o objetivo inclui Cr, Ni ou Co, preferindo agata, alumina ou carboneto de tungstenio conforme o elemento de interesse."
    risk: fato
    source: "Principio padrao de preparacao de amostra em geoquimica analitica, discutido em Potts (1987), A Handbook of Silicate Rock Analysis (Blackie/Chapman & Hall), no capitulo de preparacao de amostra; pratica documentada tambem em manuais de laboratorios comerciais (ALS, SGS, Bureau Veritas) para contaminacao por equipamento de moagem."
  - claim_id: ANINST-M28-A01-EXEMPLO-PORFIRO-BASALTO-005
    claim: "Exemplo pedagogico hipotetico comparando massa de amostra necessaria para um basalto afanitico homogeneo (~0,5 mm) versus um porfiro cuprifero com fenocristais de plagioclasio ate 8 mm e veios de sulfeto centimetricos, concluindo que o porfiro exige massa de amostra muito maior devido a heterogeneidade de constituicao e efeito pepita para Au."
    risk: hipotetico
    source: "Exemplo pedagogico construido especificamente para esta aula, com valores de tamanho de grao plausiveis para as litologias descritas mas nao correspondentes a uma jazida real publicada. A logica quantitativa (heterogeneidade cresce com tamanho de particula e com concentracao desigual do elemento de interesse) segue diretamente a teoria de Gy discutida em Pitard (1993)."
  - claim_id: ANINST-M28-A01-VIES-VS-FSE-006
    claim: "O erro fundamental de amostragem de Gy e aleatorio (media praticamente nula, aparece como dispersao entre amostras replicadas); o vies sistematico vem de amostragem incorreta (segregacao, delimitacao, extracao). Nenhum dos dois e revelado pela replica instrumental."
    risk: fato
    source: "Criado pela auditoria de 2026-09-23 (achado 2). Minnitt, Rice & Spangenberg (2007), J. SAIMM 107(8), 505-511 (texto lido), sobre a decomposicao de Gy (1982) e Pitard (1989)."

auditoria:
  data: 2026-09-23
  modo: audit-and-fix
  relatorio: 28-analise-instrumental-i-auditoria.md
  achados_nesta_aula:
    - "1 (laranja) ANINST-M28-A01-MASSA-CUBO-DIAMETRO-002 - 'regra de Visman' retirada; regra d3 atribuida a Gy - corrigido"
    - "2 (laranja) ANINST-M28-A01-VIES-VS-FSE-006 (novo) - FSE aleatorio x vies de amostragem incorreta - corrigido (corpo e recap)"
  verificados_sem_achado: "001 (Pitard 1993), 003 (efeito pepita), 004 (contaminacao por aco e WC), 005 (exemplo porfiro x basalto)"

revisao_didatica:
  data: 2026-09-23
  modo: review-and-fix
  relatorio: 28-analise-instrumental-i-revisao-didatica.md
  achados_nesta_aula:
    - "DID-M28-A01-CALCULO-MASSA-PROMETIDO-005 (laranja) - 'Ao final' prometia calcular a massa minima e nenhum passo calculava; objetivo reformulado para estimar pela regra do cubo e passo 'Ordem de grandeza pela regra do cubo' acrescentado ao exemplo (so aritmetica: (8/0,5)^3 = 16^3 ~ 4100; metade do tamanho -> massa/8), com a ressalva de que os demais fatores de Gy mudam entre as rochas"
    - "DID-M28-REFERENCIAS-CRUZADAS-007 (amarelo) - precisao instrumental agora remete a Aula 06"
-->
