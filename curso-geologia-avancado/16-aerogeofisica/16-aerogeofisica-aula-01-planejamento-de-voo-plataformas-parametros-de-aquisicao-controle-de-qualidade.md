# Aula 01: Por que voar — plataformas, planejamento de voo, parâmetros de aquisição e controle de qualidade

**ID:** geologia-avancado-m16-a01
**Módulo:** [[16-aerogeofisica-modulo|Módulo 16 — Introdução à aerogeofísica]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** definir os parâmetros que estruturam um aerolevantamento geofísico (plataforma, altura de voo, espaçamento e direção das linhas) e avaliar o controle de qualidade que garante que os dados brutos são confiáveis antes de qualquer processamento.
**Ao final você vai conseguir:** escolher a plataforma (avião, helicóptero ou VANT) mais adequada a um objetivo de levantamento; dimensionar altura de voo e espaçamento de linhas a partir da distância sensor-fonte (altura de voo + profundidade do topo do alvo) e do tamanho do alvo geológico; explicar por que a orientação das linhas de voo importa; e identificar os procedimentos de controle de qualidade que separam um levantamento confiável de um inutilizável.
**Pré-requisito:** [[15-petrofisica/15-petrofisica-modulo|Módulo 15 — Introdução à petrofísica]] — esta aula assume que você já sabe de onde vêm os contrastes físicos (densidade, magnetismo, radioatividade, condutividade) que a aerogeofísica mede; aqui a pergunta muda de "por que a rocha responde assim" para "como desenhar um voo que capture essa resposta com confiança".

## Conteúdo

### Por que voar em vez de caminhar

Um levantamento geofísico terrestre percorre o terreno a pé ou de veículo, estação por estação, com controle fino sobre a posição de cada medida — mas cobre poucos quilômetros quadrados por dia e não alcança áreas de relevo acidentado, cobertas por vegetação densa, alagadas ou simplesmente vastas demais. A aerogeofísica troca esse controle fino por **velocidade e cobertura**: uma aeronave percorre em um dia o que uma equipe terrestre levaria meses para cobrir, adquirindo dados de forma contínua e homogênea ao longo de milhares de quilômetros de linha, sobre qualquer tipo de terreno, sem depender de acesso rodoviário ou autorização de entrada em cada propriedade. O preço dessa vantagem é que o sensor fica a dezenas ou centenas de metros da fonte do sinal geológico — e, como se verá ao longo deste módulo, essa distância domina quase toda a física de como se planeja e processa um aerolevantamento.

Essa troca de escala não é gratuita: aerolevantamentos são o método de primeira escolha para reconhecimento regional e exploração mineral e de hidrocarbonetos em áreas extensas, exatamente onde o custo por quilômetro quadrado de um levantamento terrestre equivalente seria proibitivo. Depois de identificado um alvo por via aérea, o refinamento fino costuma voltar ao terreno — a aerogeofísica raramente substitui por completo a geofísica terrestre, ela **direciona** onde aplicá-la.

### Três plataformas, três compromissos

**Avião de asa fixa.** É a plataforma de maior velocidade de cruzeiro (tipicamente da ordem de 250-280 km/h) e maior autonomia, o que o torna econômico para levantamentos regionais de grande área — milhares a dezenas de milhares de quilômetros de linha. Sua limitação é a incapacidade de reduzir a velocidade ou de manobrar em curvas fechadas, o que exige terreno relativamente suave para manter altura de voo baixa e constante acima do solo — o **drapeamento** do relevo, isto é, subir e descer acompanhando a topografia para preservar a mesma distância ao terreno, em vez de voar num plano horizontal fixo — e torna o avião menos adequado a serras íngremes ou a áreas urbanizadas com obstáculos.

**Helicóptero.** Voa mais devagar (da ordem de 100-140 km/h) e consegue manter altura de voo mais baixa e mais constante sobre relevo acidentado, além de fazer curvas de raio menor entre linhas — vantagens diretas para exploração mineral de detalhe, onde a resolução espacial de alvos pequenos e rasos depende de voar baixo e com linhas próximas. O custo operacional por hora é maior que o do avião, e a autonomia é menor, o que o torna a escolha típica de levantamentos de área menor e alta resolução, não de reconhecimento regional.

**VANT (veículo aéreo não tripulado, drone).** É a plataforma mais recente do trio e ocupa o nicho de áreas pequenas (dezenas a poucas centenas de km²) que exigem resolução extrema: por voar ainda mais baixo e mais devagar que o helicóptero, com linhas mais próximas, produz o mapa de maior detalhe espacial dos três — ao custo de autonomia de voo limitada pela bateria (tipicamente dezenas de minutos por bateria, exigindo múltiplos voos e trocas), carga útil (payload) restrita, que limita o tipo de sensor embarcado, e uma regulamentação de espaço aéreo ainda em consolidação em muitos países. VANTs magnéticos são hoje o uso mais maduro da plataforma; sensores mais pesados (gravímetros, espectrômetros gama de cristal grande) ainda dependem majoritariamente de avião e helicóptero, embora essa fronteira venha se movendo.

A escolha entre as três não é sobre qual é "melhor", mas sobre qual **compromisso entre área, resolução e custo** o problema geológico exige. Vale ver os três lado a lado antes de seguir, porque as linhas da tabela não são características soltas: elas se encadeiam, e é o encadeamento que fecha o argumento.

| | **Avião de asa fixa** | **Helicóptero** | **VANT (drone)** |
|---|---|---|---|
| Velocidade típica | ≈250-280 km/h | ≈100-140 km/h | mais lento que o helicóptero |
| Autonomia | maior de todas | intermediária | dezenas de minutos por bateria |
| Altura de voo praticável | maior; barométrica constante é comum | baixa e drapeada (dezenas de m) | a mais baixa das três |
| Espaçamento de linha viável | centenas de m a km | 50-200 m | o mais fechado dos três |
| Área típica | milhares a dezenas de milhares de km de linha | área menor, alta resolução | dezenas a poucas centenas de km² |
| Carga útil | qualquer sensor | qualquer sensor | restrita (magnetômetro é o uso maduro) |
| Vocação | reconhecimento regional | exploração mineral de detalhe | detalhe extremo em área pequena |

Lendo a tabela de cima para baixo, o padrão é um só: **velocidade e autonomia se pagam em resolução, e resolução se paga em área coberta** — não existe uma plataforma que ganhe nas três. Por isso a decisão vem do problema geológico e não do catálogo: reconhecimento regional de uma bacia sedimentar pede avião; um alvo de poucos km² de sulfeto maciço vulcanogênico sob relevo acidentado pede helicóptero; um afloramento ou uma cava de mina que precisa de mapa magnético centimétrico pede VANT.

### Altura de voo: o parâmetro que domina o sinal

Todo campo físico medido à distância decai com a distância à fonte — o campo magnético e o campo gravitacional de um corpo geológico caem, em primeira aproximação, com uma potência da distância (o dipolo magnético cai com o cubo da distância e a massa pontual gravitacional cai com o quadrado da distância, ambos mais rápido do que uma simples proporção linear). Isso faz da **altura de voo** o parâmetro isolado mais determinante de quanto sinal geológico chega ao sensor: voar mais alto suaviza e atenua as anomalias de fontes rasas e pequenas, e nenhum processamento posterior recupera de volta esse sinal perdido na aquisição — um realce pode tornar mais visível o que já está no dado, mas não pode inventar o que a distância já apagou.

Por isso a altura de voo é escolhida em função do alvo: levantamentos de reconhecimento regional, cujo objetivo é mapear estruturas profundas e de grande escala, tipicamente voam mais alto (a aviação de asa fixa frequentemente mantém altura constante de referência barométrica em vez de drapeamento fino do relevo, na faixa de uma centena a algumas centenas de metros); levantamentos de detalhe para exploração mineral, cujo alvo costuma ser raso e de pequenas dimensões, voam **drapeados** (acompanhando o relevo com altura constante acima do solo, medida por altímetro a laser ou radar) e o mais baixo que a segurança operacional permitir — em helicóptero, frequentemente na faixa de algumas dezenas de metros para magnetometria de alta resolução, e ainda mais baixo para gamaespectrometria, cujo sinal (visto na Aula 04) vem apenas dos primeiros centímetros do solo e se atenua fortemente com a altura.

### Espaçamento e direção das linhas

Um aerolevantamento não cobre a área de forma contínua: ele adquire dados ao longo de **linhas de voo** paralelas, espaçadas entre si, e o espaço entre linhas é a segunda decisão de projeto mais determinante depois da altura de voo. A lógica é análoga à de qualquer amostragem espacial: se as linhas estiverem espaçadas muito além do tamanho do alvo, o levantamento pode simplesmente passar ao lado dele sem nunca cruzá-lo, ou cruzá-lo de forma tão parcial que a anomalia fica irreconhecível na malha final.

A regra prática consagrada na literatura dimensiona o espaçamento de linha em função da **distância entre o sensor e a fonte** — que não é a profundidade do alvo sozinha, e sim a soma da altura de voo com a profundidade do topo do corpo. O critério de referência vem da análise de aliasing de Reid (1980), até hoje o ponto de partida do projeto de levantamento: Reid mostrou que a fração da potência do sinal que é aliasada por uma malha de espaçamento Δx sobre fontes a uma distância média *h* do sensor decai como exp(−2π·*h*/Δx), de modo que um espaçamento de até cerca de **duas vezes a distância sensor-fonte** deixa apenas alguns por cento da potência aliasada — daí a regra de bolso de Δx ≤ 2*h*, com a prática operacional corrente situando-se na faixa de 2 a 2,5 vezes essa distância. Duas leituras desse número importam. Primeira: ele é um **teto**, não uma meta — espaçar menos só melhora a amostragem, ao custo de horas de voo. Segunda: o erro de projeto mais comum é usar apenas a profundidade do topo do corpo no lugar da distância sensor-fonte, esquecendo que o sensor já parte de dezenas ou centenas de metros acima do solo — num levantamento alto, essa omissão faz o intérprete acreditar que a malha resolve mais do que de fato resolve. Alvos mais rasos e mais estreitos exigem malhas proporcionalmente mais fechadas. Na prática de exploração mineral, isso se traduz tipicamente em espaçamentos de 50 a 200 m para alvos rasos e de detalhe, enquanto levantamentos de reconhecimento regional — cujo objetivo é mapear grandes estruturas crustais, não corpos individuais — usam espaçamentos de centenas de metros a alguns quilômetros, historicamente até 1.600 m (1 milha) em levantamentos regionais mais antigos.

A **direção das linhas** também é uma decisão deliberada, não uma conveniência operacional: o ideal é orientar as linhas de voo **perpendiculares à direção estrutural predominante** esperada na área (foliação, acamamento, zonas de cisalhamento, contatos litológicos), porque uma linha perpendicular a uma estrutura linear a atravessa e a registra como uma anomalia nítida, enquanto uma linha paralela à mesma estrutura pode percorrê-la inteira sem nunca cruzá-la, tornando-a invisível no levantamento independentemente de quão forte seja o contraste físico. Perpendicularmente às linhas de voo principais, adiciona-se um conjunto esparso de **linhas de controle** (tie lines), tipicamente espaçadas em um múltiplo do espaçamento das linhas principais (da ordem de 5 a 10 vezes), cuja função não é mapear diretamente, mas fornecer os pontos de cruzamento usados no nivelamento dos dados, discutido a seguir.

### Controle de qualidade: dos sensores ao produto final

Um aerolevantamento gera milhões de medidas, e a maior parte delas nunca é olhada individualmente por um intérprete — o controle de qualidade é o que garante que essa massa de dados brutos é confiável antes de qualquer mapa ser produzido. Os procedimentos centrais são:

**Testes de calibração pré-voo.** Antes do levantamento, verifica-se a resposta dos sensores contra padrões conhecidos (por exemplo, pastilhas de calibração de concentração radiométrica certificada, no caso da gamaespectrometria) e testa-se o **erro de rumo** (heading error) do magnetômetro voando um padrão em forma de oito sobre um ponto fixo, o que revela se a magnetização da própria aeronave contamina a leitura de forma dependente da direção de voo — um efeito que precisa ser modelado e removido, ou minimizado posicionando o sensor magnético o mais longe possível da fuselagem (tipicamente rebocado atrás da aeronave num "bird" ou fixado na ponta de uma longarina).

**Estação-base simultânea.** Durante todo o voo, uma estação terrestre fixa registra continuamente o mesmo campo físico que a aeronave mede (tipicamente o campo magnético total, para a correção de variação diurna tratada na Aula 02) — sem essa referência simultânea em terra, é impossível separar a variação temporal do campo (que afeta toda a área do levantamento por igual, ao longo do dia) da variação espacial devida à geologia (que é o que se quer mapear).

**Repetição de linhas e nivelamento em cruzamentos.** Uma fração das linhas é voada mais de uma vez em dias ou condições diferentes, e a diferença entre as repetições estabelece o **nível de ruído** do levantamento — um número que acompanha o produto final e diz ao intérprete o quanto de detalhe no mapa é sinal geológico real e o quanto é ruído instrumental. Nos cruzamentos entre linhas principais e linhas de controle, exige-se que a mesma grandeza física, medida por dois voos diferentes no mesmo ponto do espaço, produza o mesmo valor dentro de uma tolerância predefinida; divergências sistemáticas nesses cruzamentos alimentam o processo de **nivelamento** (leveling), que ajusta cada linha para eliminar deslocamentos artificiais entre linhas adjacentes antes de gerar a grade final.

**Posicionamento.** A posição de cada medida ao longo da linha depende de GNSS (frequentemente com correção diferencial, para erro posicional da ordem de poucos metros ou menos) e a altura acima do terreno de um altímetro a laser ou radar; um atraso de tempo entre a leitura do sensor geofísico e a leitura de posição (o **lag**, causado pelo tempo de resposta do sensor e pela distância física entre sensor e antena de GPS quando o sensor é rebocado) desloca sistematicamente a anomalia ao longo da linha se não for corrigido, e esse deslocamento é maior quanto maior a velocidade da aeronave — mais um motivo pelo qual helicópteros, mais lentos, favorecem a resolução de detalhe.

Só depois de aprovado nesses testes o dado bruto segue para as correções específicas de cada método — o assunto das quatro aulas seguintes deste módulo.

## Exemplo trabalhado

**Situação:** uma empresa de exploração mineral quer planejar um levantamento aeromagnético e aerogamaespectrométrico sobre uma área de 400 km² onde mapeamento geológico prévio sugere um corpo mineralizado tabular com topo esperado a cerca de 150 m de profundidade e extensão lateral mínima de 300 m, associado a uma zona de cisalhamento de direção geral N30°E. A área tem relevo moderado, sem rios largos nem áreas urbanizadas.

**Pergunta:** defina a plataforma, a altura de voo aproximada, o espaçamento e a direção das linhas principais, e o espaçamento das linhas de controle.

**Resolução:**

**Plataforma:** a área é de tamanho moderado (400 km², compatível com um levantamento de detalhe, não regional) e exige alta resolução para um alvo raso e relativamente pequeno (300 m de extensão). O relevo moderado ainda permite avião de asa fixa em muitos casos, mas a exigência de resolução para um alvo dessa profundidade favorece **helicóptero**, que voa mais baixo e mais devagar, reduzindo o lag de posicionamento e permitindo um drapeamento mais fiel do relevo.

**Altura de voo:** para gamaespectrometria (sensível apenas aos primeiros centímetros de solo, Aula 04) e magnetometria de detalhe sobre alvo raso, a prioridade é voar o mais baixo que a segurança permitir — uma altura drapeada da ordem de 60-80 m é uma escolha típica de levantamento de detalhe em helicóptero, equilibrando resolução com segurança sobre relevo moderado.

**Espaçamento das linhas principais:** a distância sensor-fonte não são os 150 m de profundidade do topo, e sim a soma da altura de voo com essa profundidade: 60-80 m + 150 m ≈ **210 a 230 m**. Pelo critério de Reid, o teto de espaçamento sem aliasing relevante fica em cerca de duas vezes esse valor, ou seja, **≈420 a 460 m**. Como aqui o objetivo é delinear a geometria do corpo, e não apenas detectá-lo, escolhe-se bem abaixo do teto: um espaçamento de **150 a 200 m** coloca duas a três linhas sobre um alvo de 300 m de extensão lateral, o que permite mapear a forma da anomalia em vez de apenas registrar sua existência.

**Direção das linhas principais:** a zona de cisalhamento tem direção N30°E; as linhas de voo devem ser **perpendiculares** a essa direção, portanto orientadas aproximadamente N60°O (ou, na convenção de rumo de voo, aproximadamente 300°/120°) — cruzando a estrutura de frente em vez de correrem paralelas a ela.

**Linhas de controle:** perpendiculares às linhas principais (portanto, aproximadamente paralelas à direção estrutural, N30°E) e espaçadas em um múltiplo maior — usando o fator prático de 5 a 10 vezes o espaçamento principal, um espaçamento de linha de controle de **1.000 a 1.500 m** fornece cruzamentos suficientes para o nivelamento sem multiplicar desnecessariamente o tempo de voo, já que a função dessas linhas é de controle, não de mapeamento direto do alvo.

**Conclusão:** o mesmo alvo geológico, se fosse mapeado por um levantamento regional genérico de reconhecimento (linhas de 800-1.600 m, direção arbitrária, altura de centenas de metros), muito provavelmente não apareceria no mapa — não por falta de contraste físico, mas porque o desenho do voo nunca lhe daria a chance de ser detectado. Os parâmetros de aquisição não são detalhe técnico posterior à decisão geológica: eles **são** a decisão geológica, traduzida em números antes de a aeronave decolar.

## Erros comuns

- **Dimensionar o espaçamento de linha só pela profundidade do topo do corpo.** A distância que importa para o critério de Reid é sensor-fonte (altura de voo + profundidade) — esquecer a altura de voo faz o intérprete acreditar que a malha resolve mais do que de fato resolve, exatamente o erro de projeto mais comum citado na aula.
- **Voar linhas paralelas à direção estrutural predominante.** Uma linha paralela a uma zona de cisalhamento pode percorrê-la inteira sem nunca cruzá-la, tornando-a invisível no levantamento por melhor que seja o contraste físico — a orientação perpendicular é decisão deliberada, não conveniência operacional.
- **Escolher espaçamento de linha rente ao teto do critério de Reid quando o objetivo é delinear a geometria do alvo, não só detectá-lo.** Como o exemplo trabalhado mostra, o teto (2× a distância sensor-fonte) garante detecção; mapear a forma de um corpo de 300 m exige ficar bem abaixo dele, com 2-3 linhas cruzando o alvo.
- **Escolher plataforma pelo catálogo (a "melhor" em abstrato) em vez de pelo compromisso que o problema exige.** Avião, helicóptero e VANT trocam velocidade/autonomia por resolução/área — não existe uma que vença nas três, a decisão vem do alvo geológico.

## O que não concluir

- **Que voar mais baixo sempre é a escolha certa.** É a escolha certa para alvo raso e pequeno; reconhecimento regional de estruturas profundas e grandes usa alturas maiores deliberadamente — a altura de voo é escolhida em função do alvo, não minimizada por padrão.
- **Que o teste do "oito" ou a estação-base são formalidades pré-voo dispensáveis quando o cronograma aperta.** Sem o teste de erro de rumo, a magnetização da própria aeronave contamina a leitura de forma dependente da direção; sem a estação-base simultânea, é impossível separar variação temporal do campo da variação espacial que se quer mapear — nenhum processamento posterior repara a ausência desses dois controles.
- **Que aerogeofísica substitui completamente o levantamento terrestre.** Ela direciona onde aplicar geofísica terrestre de detalhe depois — raramente é a etapa final da investigação, é a etapa que reduz a área de busca.

## Recap relâmpago

- Aerogeofísica troca o controle fino do levantamento terrestre por velocidade e cobertura, direcionando onde depois aplicar métodos terrestres de detalhe — raramente a substitui por completo.
- Avião de asa fixa: mais rápido (≈250-280 km/h) e de maior autonomia, ideal para reconhecimento regional de grande área. Helicóptero: mais lento (≈100-140 km/h), voa mais baixo e drapeia melhor o relevo, ideal para exploração mineral de detalhe. VANT: menor área e maior resolução dos três, limitado por autonomia de bateria e carga útil, hoje mais maduro em magnetometria.
- A altura de voo é o parâmetro isolado mais determinante do sinal captado — nenhum processamento recupera depois o sinal de fonte rasa perdido por voar alto demais. Levantamentos regionais voam mais alto (dezenas a centenas de metros, por vezes com altura barométrica constante); levantamentos de detalhe voam drapeados e baixos (dezenas de metros em helicóptero).
- O espaçamento de linha se dimensiona pela **distância sensor-fonte** (altura de voo + profundidade do topo do corpo), não pela profundidade sozinha: o critério de Reid (1980), cuja fração de potência aliasada decai como exp(−2π·h/Δx), põe o teto sem aliasing relevante em cerca de 2 vezes essa distância (prática corrente entre 2 e 2,5 vezes), e quem quer delinear geometria, não só detectar, escolhe bem abaixo do teto. Exploração mineral de detalhe tipicamente usa 50-200 m; reconhecimento regional usa centenas de metros a poucos quilômetros.
- As linhas de voo devem ser perpendiculares à direção estrutural predominante esperada, para que cruzem — em vez de correrem paralelas a — feições lineares; linhas de controle (tie lines), perpendiculares às principais e mais espaçadas (≈5-10× o espaçamento principal), servem ao nivelamento nos cruzamentos, não ao mapeamento direto.
- Controle de qualidade cobre calibração pré-voo (incluindo o teste de erro de rumo em oito), estação-base simultânea em terra (essencial para separar variação temporal de variação espacial), repetição de linhas e nivelamento em cruzamentos (que estabelecem o nível de ruído do levantamento) e correção de posicionamento (GNSS, altímetro, lag sensor-GPS).

## Próxima aula

[[16-aerogeofisica-aula-02-aeromagnetometria-fundamentos-correcoes-reducoes-realces|Aula 02 — Aeromagnetometria: fundamentos, correções, reduções e realces de mapas magnéticos]] — como o sinal magnético bruto, adquirido segundo os parâmetros desta aula, é transformado em mapa interpretável: da remoção do campo de referência (IGRF) e da variação diurna até os realces (derivadas, sinal analítico, redução ao polo) que tornam visíveis os contatos e estruturas que a magnetometria explora.

## Fontes

- Reeves, C. (2005), *Aeromagnetic Surveys: Principles, Practice and Interpretation*, Geosoft (parâmetros de projeto de levantamento: altura de voo, direção de linhas, controle de qualidade, testes de erro de rumo, estações-base).
- Reid, A. B. (1980), "Aeromagnetic survey design", *Geophysics*, 45(5), 973-976 (critério de aliasing: fração de potência aliasada F = exp(−2π·h/Δx), donde o teto prático de espaçamento de linha de ≈2 vezes a distância sensor-fonte).
- Saltus, R. W., Chulliat, A. & Blakely, R. J. (2026), "Evaluation of aliasing in aeromagnetic surveys — update to Reid 1980 analysis", *Earth and Space Science*, 13, e2025EA004336 (reavaliação do critério de Reid: a análise segue válida para anomalias de curto comprimento de onda, mas o projeto moderno de levantamento deve considerar fatores adicionais que não existiam em 1980).
- Telford, W. M., Geldart, L. P. & Sheriff, R. E. (1990), *Applied Geophysics*, 2ª ed., Cambridge University Press, cap. 6 (fundamentos de plataformas e aquisição aerogeofísica).
- Nabighian, M. N. et al. (2005), "The historical development of the magnetic method in exploration", *Geophysics*, 70(6) (evolução de plataformas e parâmetros de aquisição aeromagnética).
- U.S. Geological Survey, Open-File Report 00-0027 (levantamento aeromagnético do Mt. Rainier) e USGS OFR 2004-1293 (parâmetros de aquisição de levantamentos históricos e modernos: alturas de voo, incluindo o padrão de 305 m / 1.000 pés, e espaçamentos de linha regionais vs. de detalhe).
- sphengineering.com, "How to Plan Drone Magnetic Surveys" (parâmetros e limitações operacionais de VANT em magnetometria).

<!--
nivel: avancado
palavras_corpo: 3067
mapa_objetivo_secao:
  geologia-avancado-m16-oa01: "Por que voar em vez de caminhar" + "Três plataformas, três compromissos" + "Altura de voo: o parâmetro que domina o sinal" + "Espaçamento e direção das linhas" + "Controle de qualidade: dos sensores ao produto final" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: AEROGEOFIS-M16-A01-PLATAFORMAS-001
    claim: "Avião de asa fixa tem velocidade de cruzeiro tipicamente da ordem de 250-280 km/h e maior autonomia, favorecendo levantamentos regionais de grande área; helicóptero voa mais devagar (ordem de 100-140 km/h), mantém altura mais baixa e constante sobre relevo acidentado e faz curvas de raio menor, favorecendo exploração mineral de detalhe, a custo operacional por hora maior e menor autonomia."
    risk: aproximacao
    source: "Reeves 2005, Aeromagnetic Surveys: Principles, Practice and Interpretation; Telford, Geldart & Sheriff 1990, Applied Geophysics, cap. 6. Faixas de velocidade são aproximadas e variam por modelo de aeronave."
  - claim_id: AEROGEOFIS-M16-A01-VANT-002
    claim: "VANTs (drones) ocupam o nicho de áreas pequenas exigindo resolução extrema, voando mais baixo e devagar que helicóptero, com autonomia limitada por bateria (tipicamente dezenas de minutos por voo) e carga útil restrita; magnetometria é hoje o uso mais maduro da plataforma, com sensores mais pesados (gravímetro, espectrômetro gama) ainda dependendo majoritariamente de avião/helicóptero."
    risk: aproximacao
    source: "sphengineering.com, How to Plan Drone Magnetic Surveys: Flight Planning, Sensors and UgCS Setup; jouav.com, Drone Magnetic Survey for Mineral Exploration in Gansu. Estado da técnica em evolução, generalização razoável mas não universal."
  - claim_id: AEROGEOFIS-M16-A01-ALTURA-003
    claim: "A altura de voo é o parâmetro isolado mais determinante do sinal captado, pois campos magnético e gravitacional decaem com a distância à fonte, e nenhum processamento posterior recupera sinal de fonte rasa perdido por voar alto demais. Levantamentos regionais de asa fixa historicamente mantêm alturas de referência da ordem de uma centena a algumas centenas de metros (nominalmente até 305 m / 1.000 pés em levantamentos de reconhecimento mais antigos); levantamentos de detalhe em helicóptero voam drapeados, tipicamente na faixa de algumas dezenas de metros (ordem de 60-80 m)."
    risk: aproximacao
    source: "Reeves 2005; ScienceDirect Topics, Aeromagnetic Survey overview; USGS OFR 2004-1293 e OFR-00-0027 (alturas de voo de levantamentos históricos e modernos, incluindo o padrão de 305 m / 1.000 pés e alturas de detalhe abaixo de 350 m)."
  - claim_id: AEROGEOFIS-M16-A01-ESPACAMENTO-004
    claim: "O espaçamento de linha se dimensiona pela DISTÂNCIA SENSOR-FONTE (altura de voo + profundidade do topo do corpo), não pela profundidade do alvo isolada. Pelo critério de aliasing de Reid (1980), a fração de potência aliasada decai como F = exp(-2*pi*h/dx), de modo que dx = 2h deixa apenas alguns por cento da potência aliasada — daí o teto prático de espaçamento de até cerca de 2 vezes a distância sensor-fonte, com a prática operacional corrente entre 2 e 2,5 vezes. Na prática, exploração mineral de detalhe usa espaçamentos de 50-200 m; reconhecimento regional usa de centenas de metros a poucos quilômetros, historicamente até 1.600 m (1 milha) com altura nominal de 305 m."
    risk: fato
    source: "Reid, A. B. (1980), Aeromagnetic survey design, Geophysics 45(5):973-976 (fórmula de fração aliasada e regra dx <= 2h); Saltus, Chulliat & Blakely (2026), Evaluation of aliasing in aeromagnetic surveys — update to Reid 1980 analysis, Earth and Space Science 13, e2025EA004336 (o critério de Reid segue válido para curto comprimento de onda, com fatores adicionais no projeto moderno); Reeves 2005; USGS OFR 00-0027 e OFR 2004-1293 (faixas típicas de espaçamento regional vs. detalhe, incluindo o padrão histórico de 1.600 m / 305 m). CORREÇÃO LARANJA da auditoria de 2026-09-09: a redação original desta alegação dizia 'da ordem de 1 a 2 vezes a PROFUNDIDADE esperada do topo do alvo', omitindo a altura de voo — exatamente o erro de projeto que o corpo da aula denuncia; a alegação contradizia o próprio texto da aula."
  - claim_id: AEROGEOFIS-M16-A01-DIRECAO-005
    claim: "Linhas de voo devem ser orientadas perpendicularmente à direção estrutural predominante esperada, para maximizar a chance de cruzar feições lineares em vez de correr paralelas a elas; linhas de controle (tie lines) são voadas perpendicularmente às linhas principais e mais espaçadas (ordem de 5 a 10 vezes o espaçamento principal), servindo ao nivelamento nos pontos de cruzamento."
    risk: fato
    source: "Reeves 2005; Telford, Geldart & Sheriff 1990, cap. 6 (orientação de linhas de voo e função das tie lines no nivelamento)."
  - claim_id: AEROGEOFIS-M16-A01-QC-006
    claim: "Controle de qualidade de aerolevantamento inclui: calibração pré-voo com padrões conhecidos e teste de erro de rumo (voo em oito) para revelar magnetização da aeronave; estação-base terrestre simultânea, necessária para separar variação temporal do campo de variação espacial devida à geologia; repetição de linhas e nivelamento em cruzamentos entre linhas principais e de controle, que estabelecem o nível de ruído do levantamento; correção de posicionamento por GNSS e altímetro, com atenção ao lag entre sensor geofísico e antena de GPS, mais crítico em maior velocidade de aeronave."
    risk: fato
    source: "Reeves 2005, Aeromagnetic Surveys: Principles, Practice and Interpretation, cap. sobre controle de qualidade e nivelamento; Telford, Geldart & Sheriff 1990, cap. 6; Nabighian et al. 2005, Geophysics 70(6) (evolução dos procedimentos de QC em levantamentos aeromagnéticos)."
-->
