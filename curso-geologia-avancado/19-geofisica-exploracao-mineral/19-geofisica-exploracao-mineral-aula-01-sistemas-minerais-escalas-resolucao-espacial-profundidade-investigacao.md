# Aula 01: Geofísica na exploração mineral — sistemas minerais, escalas de trabalho e o paradoxo resolução × profundidade

**ID:** geologia-avancado-m19-a01
**Módulo:** [[19-geofisica-exploracao-mineral-modulo|Módulo 19 — Geofísica aplicada na exploração mineral]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** situar a geofísica de exploração mineral dentro do paradigma de **sistemas minerais** — a ideia de que um depósito é o produto final observável de processos que operam em escalas muito maiores do que o próprio depósito — e apresentar o compromisso fundamental entre resolução espacial e profundidade de investigação que governa a escolha de método em cada escala de trabalho.
**Ao final você vai conseguir:** explicar o que um "sistema mineral" é e por que ele se descreve em quatro componentes (fonte, transporte, deposição, preservação); classificar um levantamento geofísico pela escala de trabalho a que ele serve — província, distrito/camp, alvo ou depósito — e relacionar essa escala ao tipo de decisão exploratória que ela informa; e justificar, com base na física da propagação de sinal, por que nenhum método geofísico entrega ao mesmo tempo altíssima resolução espacial e grande profundidade de investigação.
**Pré-requisito:** [[15-petrofisica/15-petrofisica-modulo|Módulo 15 — Introdução à petrofísica]] (as propriedades físicas — densidade, susceptibilidade magnética, resistividade elétrica — que os métodos desta aula em diante vão medir) e [[14-sensoriamento-remoto/14-sensoriamento-remoto-modulo|Módulo 14 — Sensoriamento remoto]] (a lógica de resolução espacial versus cobertura, usada aqui como **analogia** para o par resolução-profundidade — o resultado prático coincide, mas o mecanismo físico é outro, e a aula diz onde a analogia para).

## Conteúdo

### Por que "encontrar minério" não começa cavando

Um depósito mineral economicamente viável é um evento raro: é o resultado de vários processos geológicos independentes que precisam ter acontecido, na sequência certa, no lugar certo, e depois terem sobrevivido à erosão e à deformação subsequentes. A indústria de exploração mineral organiza esse raciocínio no que se chama, desde os anos 1990, de **paradigma de sistemas minerais** (*mineral systems*) — uma mudança de foco em relação ao antigo "modelo de depósito", que descrevia a geometria e a mineralogia de um tipo de jazida já formada, sem necessariamente explicar por que ela se formou ali e não a dez quilômetros dali.

Um sistema mineral se descreve por quatro componentes que precisam coexistir:

- **Fonte** — de onde vieram os metais e os fluidos que os transportaram (uma intrusão magmática, uma bacia sedimentar com fluidos de bacia, o manto).
- **Transporte** — o caminho estrutural que canalizou o fluido mineralizante (falhas profundas, zonas de cisalhamento, contatos litológicos permeáveis) — a arquitetura tectônica de grande escala funciona literalmente como um encanamento.
- **Deposição** — o mecanismo físico-químico que forçou o metal a precipitar num local específico (queda de pressão, mistura de fluidos, reação com uma rocha reativa, ebulição).
- **Preservação** — a razão pela qual esse depósito, uma vez formado, não foi depois erodido, metamorfizado a ponto de destruir a mineralização, ou soterrado a profundidades inacessíveis.

A força do paradigma é que ele desloca a pergunta de "que tipo de depósito é este?" para "que combinação de fonte, caminho, armadilha e preservação eu preciso encontrar evidência de, nesta província, para que um depósito pudesse ter se formado aqui?" — e cada um desses quatro componentes deixa uma assinatura física (densidade, magnetismo, condutividade, radioatividade) que a geofísica pode, em princípio, detectar em escalas diferentes.

### As quatro escalas de trabalho, e o que cada uma decide

A exploração mineral moderna organiza o trabalho em escalas geográficas aninhadas, e a escolha do método geofísico (e do seu custo) depende diretamente de em qual escala a pergunta está sendo feita:

- **Escala de província** (centenas a milhares de km): a pergunta é "esta região tem a arquitetura tectônica certa para hospedar sistemas minerais de um tipo específico?" — por exemplo, existe uma sutura crustal profunda, um cráton com margem reativada, um cinturão de rochas verdes arqueano. Os dados geofísicos aqui vêm quase sempre de levantamentos regionais pré-existentes (gravimetria e magnetometria de cobertura nacional, dados de satélite), não de campanhas dedicadas — o custo por km² é baixíssimo porque o dado já existe ou é compartilhado por muitos usuários.
- **Escala de distrito ou "camp"** (dezenas de km): a pergunta é "onde, dentro desta província favorável, estão os corredores estruturais e os focos de alteração hidrotermal que concentram o sistema mineral?" — aqui entram levantamentos aerogeofísicos dedicados (magnetometria e gamaespectrometria aéreas de alta resolução, como no Módulo 16), com linhas de voo espaçadas tipicamente entre 100 e 400 m.
- **Escala de alvo** (poucos km a centenas de m): a pergunta é "esta anomalia específica, vista à distância, é um alvo perfurável?" — entram os métodos terrestres de maior resolução e maior custo por km² (eletrorresistividade, polarização induzida, eletromagnéticos terrestres), cobrindo áreas muito menores com muito mais detalhe.
- **Escala de depósito** (dezenas a poucas centenas de m, e profundidade): a pergunta já não é mais "existe um alvo aqui?", mas "qual é a geometria 3D do corpo mineralizado, e como ele se conecta aos furos de sondagem já feitos?" — aqui a geofísica de poço e a geofísica terrestre de detalhe (IP e eletromagnético de alta densidade de estações) trabalham lado a lado com a própria sondagem, e a petrofísica de testemunho (Módulo 15) calibra a interpretação.

O ponto central desta seção é que **cada escala filtra que tipo de método faz sentido economicamente**: rodar um levantamento de eletrorresistividade terrestre de detalhe sobre uma província inteira de milhares de km² não é apenas caro — é desperdício de resolução que a pergunta daquela escala não precisa. E o inverso também vale: tentar decidir onde perfurar um alvo específico a partir apenas de gravimetria regional de estações espaçadas a 5 km é pedir a um dado grosseiro uma resposta fina que ele fisicamente não contém.

### O paradoxo resolução × profundidade

Todo método geofísico enfrenta uma tensão física entre dois desempenhos que o explorador gostaria de ter ao mesmo tempo: **resolução espacial** (a capacidade de distinguir dois corpos próximos, ou de definir com precisão o contorno de um corpo) e **profundidade de investigação** (até que profundidade o método ainda consegue detectar um alvo com contraste físico razoável). Na prática, aumentar um dos dois quase sempre custa o outro, por duas razões físicas distintas que se repetem em métodos diferentes:

**Primeira razão — atenuação e difusão do sinal.** Em métodos que dependem da propagação de um campo através da Terra (eletromagnéticos, radar de penetração no solo), o sinal se atenua com a distância percorrida, e a atenuação é mais forte em frequências mais altas. Um sinal de alta frequência carrega mais detalhe (comprimentos de onda curtos resolvem estruturas pequenas), mas é absorvido antes de alcançar profundidade; um sinal de baixa frequência penetra mais fundo, mas seu comprimento de onda longo borra estruturas pequenas — a informação sobre um corpo de poucos metros simplesmente não sobrevive à viagem. É **análogo** — não idêntico — ao compromisso já visto no sensoriamento remoto (Módulo 14), onde as quatro resoluções competem por um orçamento fixo de energia e de dado do sensor, e melhorar a resolução espacial custa faixa de imageamento (cobertura) e número de bandas. Lá a limitação é de **orçamento de fótons e de telemetria**; aqui é de **atenuação física do sinal no meio atravessado** — o resultado prático (não se maximizam duas qualidades ao mesmo tempo) é o mesmo, mas o mecanismo não é.

**Segunda razão — geometria da fonte e do receptor.** Em métodos de campo potencial (gravimetria, magnetometria) e em métodos elétricos com eletrodos fixos em superfície, a resolução com que se separa dois corpos próximos depende do espaçamento entre os pontos de medida (estações, eletrodos) em relação à profundidade do alvo: um corpo a 500 m de profundidade produz uma anomalia de superfície tão suave e alargada que estações espaçadas a 50 m de distância uma da outra não ganham resolução real sobre ele — a anomalia já "se espalhou" antes de chegar à superfície. Uma analogia ajuda, desde que se saiba onde ela quebra: é como fotografar um objeto muito distante através de ar quente e trêmulo. A partir de certa distância, trocar a câmera por outra de mais megapixels não devolve nenhum detalhe, porque o borrão já está no sinal que chega ao sensor, não no sensor. Adensar estações sobre um alvo profundo tem o mesmo destino. **Onde a analogia quebra:** o borrão da fotografia é acidente atmosférico, que um dia melhor elimina; o alargamento da anomalia é consequência necessária da física de campo potencial, e nenhuma condição de campo o elimina.

A consequência prática, que este módulo vai desenvolver método a método nas próximas cinco aulas, é que **não existe "o melhor método geofísico"** — existe o método cujo compromisso entre resolução e profundidade combina com a escala de trabalho e com a profundidade esperada do alvo. Um levantamento aerogeofísico de reconhecimento, voando a 80-120 m de altura com linhas espaçadas a várias centenas de metros, é desenhado para mapear estruturas de escala de distrito a até alguns quilômetros de profundidade — ele nunca vai resolver um corpo tabular de 20 m de espessura a 50 m de profundidade com o detalhe que uma malha terrestre de eletrorresistividade, com eletrodos a cada 10-25 m, resolve. E essa malha terrestre, por sua vez, não teria custo nem cobertura viáveis para mapear uma província inteira.

## Exemplo trabalhado

**Situação:** uma empresa de exploração está avaliando três decisões numa mesma região: (1) decidir se vale a pena adquirir os direitos minerários de um bloco de 8.000 km² num cráton pouco explorado, com base em mapas geológicos de escala 1:250.000 e um levantamento gravimétrico regional já publicado (estações a cada 5-10 km); (2) dentro desse bloco, priorizar 3 de 12 corredores estruturais de 5-15 km de extensão para um levantamento aerogeofísico dedicado; (3) sobre o corredor de maior prioridade, decidir a posição exata de dois furos de sondagem de 400 m de profundidade cada, orçados em conjunto em várias centenas de milhares de dólares.

**Pergunta:** para cada decisão, qual escala de trabalho está em jogo, e o levantamento gravimétrico regional (estações a 5-10 km) é suficiente para embasá-la?

**Resolução:**

**Decisão 1** (aquisição do bloco de 8.000 km²) é uma decisão de **escala de província**. O levantamento gravimétrico regional, mesmo com estações espaçadas a vários quilômetros, é adequado a essa escala: a pergunta não é "onde exatamente está o corpo mineralizado", mas "esta região tem a arquitetura de primeira ordem — bacias, altos estruturais, contatos crustais — compatível com sistemas minerais de interesse". Um dado grosseiro, mas de cobertura completa, responde a essa pergunta melhor do que um dado fino e caro que só cobriria uma fração da área no mesmo orçamento.

**Decisão 2** (priorizar 3 de 12 corredores de 5-15 km) é uma decisão de **escala de distrito**. Aqui o levantamento gravimétrico regional já não é suficiente — suas estações a 5-10 km de distância uma da outra são maiores do que a própria extensão de vários dos corredores candidatos, então ele não tem resolução para diferenciá-los. É exatamente a escala para a qual se justifica um levantamento aerogeofísico dedicado (magnetometria e gamaespectrometria de alta resolução, Aula 02), com linhas de voo de algumas centenas de metros de espaçamento — caro demais para o bloco inteiro de 8.000 km², mas plenamente justificável para os 12 corredores já pré-selecionados pela escala de província.

**Decisão 3** (posicionar dois furos de sondagem de 400 m sobre o corredor prioritário) é uma decisão de **escala de alvo/depósito**. Nem o dado gravimétrico regional nem o levantamento aerogeofísico de distrito têm resolução espacial suficiente para posicionar um furo com a precisão de dezenas de metros que o orçamento da sondagem exige — a decisão típica aqui vem de eletrorresistividade e IP terrestres de detalhe (Aula 03) ou de métodos eletromagnéticos terrestres (Aula 04), com estações espaçadas a poucas dezenas de metros, complementados pela petrofísica de furos vizinhos já perfurados.

**Conclusão:** as três decisões formam a cascata de afunilamento típica da exploração mineral moderna — de milhares de km² a uma dezena de corredores, e destes a dois pontos de perfuração —, e cada afunilamento troca cobertura por resolução, exigindo um método geofísico diferente. Usar o dado errado numa escala — fino demais e caro numa província, grosseiro demais para posicionar um furo — não é apenas ineficiência: é, respectivamente, desperdício de orçamento e risco real de furar ao lado do alvo.

## Recap relâmpago

- Um **sistema mineral** é descrito por quatro componentes que precisam coexistir para formar um depósito: **fonte**, **transporte** (caminho estrutural), **deposição** (mecanismo de precipitação) e **preservação** — o paradigma desloca a pergunta de "que depósito é este?" para "que evidência de fonte-caminho-armadilha-preservação existe nesta área?".
- A exploração mineral trabalha em **escalas aninhadas** — província (centenas a milhares de km), distrito/camp (dezenas de km), alvo (km a centenas de m) e depósito (dezenas a centenas de m, e profundidade) — e cada escala usa métodos geofísicos de custo e resolução crescentes à medida que a área de interesse encolhe.
- Existe um **paradoxo físico entre resolução espacial e profundidade de investigação**: sinais de alta frequência (ou estações densamente espaçadas) resolvem mais detalhe mas se atenuam antes de atingir grande profundidade; sinais de baixa frequência (ou estações espaçadas) atingem mais fundo mas borram estruturas pequenas.
- Não existe "o melhor método geofísico" em abstrato — existe o método cujo compromisso resolução×profundidade combina com a escala da pergunta exploratória sendo feita.
- Aplicar um método fino demais numa escala grande é desperdício de orçamento; aplicar um método grosseiro demais numa escala pequena é risco real de decisão errada (por exemplo, de posicionamento de um furo de sondagem).

## Próxima aula

[[19-geofisica-exploracao-mineral-aula-02-gravimetria-magnetometria-sistemas-minerais|Aula 02 — Gravimetria e magnetometria na caracterização de sistemas minerais]] — os dois primeiros métodos de campo potencial mais usados em escala de província e distrito, e a que componente física de cada tipo de sistema mineral cada um responde.

## Fontes

- Wyborn, L. A. I., Heinrich, C. A. & Jaques, A. L. (1994), "Australian Proterozoic mineral systems: essential ingredients and mappable criteria", em *Proceedings of the AusIMM Annual Conference*, Darwin, 109-115 (origem do conceito de sistema mineral aplicado à exploração australiana, desenvolvido na então AGSO).
- McCuaig, T. C. & Hronsky, J. M. A. (2014), "The mineral system concept: the key to exploration targeting", em *Society of Economic Geologists Special Publication* 18, 153-175 (formalização dos quatro componentes fonte-transporte-deposição-preservação e sua aplicação a escalas aninhadas de exploração).
- Hronsky, J. M. A. & Groves, D. I. (2008), "Science of targeting: definition, strategies, targeting and performance measurement", *Australian Journal of Earth Sciences*, 55(1), 3-12, DOI 10.1080/08120090701581356 (a lógica de afunilamento em escalas de província a depósito).

<!--
nivel: avancado
palavras_corpo: 2010
mapa_objetivo_secao:
  geologia-avancado-m19-oa01: "Por que 'encontrar minério' não começa cavando" + "As quatro escalas de trabalho, e o que cada uma decide" + "O paradoxo resolução × profundidade" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOMIN-M19-A01-SISTEMAMINERAL-001
    claim: "O paradigma de sistemas minerais (mineral systems) descreve um depósito mineral como o produto de quatro componentes que precisam coexistir: fonte (dos metais e fluidos), transporte (caminho estrutural), deposição (mecanismo físico-químico de precipitação) e preservação (sobrevivência do depósito à erosão/metamorfismo/soterramento subsequentes). O conceito foi introduzido por Wyborn, Heinrich & Jaques (1994) para a exploração australiana e formalizado por McCuaig & Hronsky (2014) como estruturado em escalas aninhadas de trabalho."
    risk: fato
    source: "Wyborn, Heinrich & Jaques (1994), 'Australian Proterozoic mineral systems: essential ingredients and mappable criteria', Proceedings of the AusIMM Annual Conference, Darwin, 109-115; McCuaig & Hronsky (2014), SEG Special Publication 18, 153-175; Hronsky & Groves (2008), Australian Journal of Earth Sciences, 55(1), 3-12. CORREÇÃO AMARELA da auditoria de 2026-09-13 (AUD-M19-A01-WYBORN-011 e AUD-M19-A01-HRONSKYGROVES-010): o título e o veículo de Wyborn et al. e o periódico de Hronsky & Groves estavam trocados."
  - claim_id: GEOMIN-M19-A01-ESCALAS-002
    claim: "A exploração mineral organiza o trabalho em escalas aninhadas de província (centenas a milhares de km), distrito/camp (dezenas de km), alvo (poucos km a centenas de m) e depósito (dezenas a centenas de m), com o custo e a resolução dos métodos geofísicos empregados aumentando à medida que a escala de trabalho encolhe — levantamentos aerogeofísicos dedicados tipicamente com linhas de voo espaçadas entre 100 e 400 m em escala de distrito, e levantamentos terrestres de detalhe (eletrorresistividade, IP) com estações espaçadas em dezenas de metros em escala de alvo/depósito."
    risk: aproximacao
    source: "Prática consolidada da indústria de exploração mineral (descrição de fluxo de trabalho por escala), consistente com McCuaig & Hronsky (2014) e com os parâmetros de aquisição típicos descritos no Módulo 16 (aerogeofísica) deste curso. Os espaçamentos de linha de voo e de eletrodo são apresentados como faixas típicas da prática, não como norma fixa — variam por orçamento, alvo e sistema de aquisição usado."
  - claim_id: GEOMIN-M19-A01-RESOLUCAOPROFUNDIDADE-003
    claim: "Métodos geofísicos enfrentam um compromisso físico entre resolução espacial e profundidade de investigação por duas razões distintas: (1) em métodos que propagam um campo pela Terra, sinais de alta frequência resolvem mais detalhe mas se atenuam mais rapidamente com a distância percorrida, limitando a profundidade alcançável; (2) em métodos de campo potencial e elétricos com eletrodos fixos, a resolução com que se separam corpos próximos é limitada pelo espaçamento entre estações/eletrodos em relação à profundidade do alvo, porque a anomalia de um corpo profundo já chega à superfície alargada e suavizada."
    risk: fato
    source: "Princípio físico consolidado da teoria de propagação eletromagnética e de campos potenciais em geofísica aplicada (ver, por exemplo, Telford, Geldart & Sheriff (1990), Applied Geophysics, 2nd ed., Cambridge University Press, capítulos sobre métodos elétricos, eletromagnéticos e de campo potencial). RESSALVA DA AUDITORIA de 2026-09-13 (AUD-M19-A01-M14ANALOGIA-016): o paralelo com o Módulo 14 é ANÁLOGO, não idêntico — lá o compromisso entre as quatro resoluções nasce de um orçamento fixo de energia e de telemetria do sensor; aqui nasce da atenuação do sinal no meio atravessado. O resultado prático coincide; o mecanismo não."
-->
