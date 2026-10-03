# Aula 01: Modelagem geológica 3D — definições, usos, vantagens e limitações; softwares comerciais e livres

**ID:** geologia-avancado-m22-a01
**Módulo:** [[22-modelagem-geologica-3d-modulo|Módulo 22 — Modelagem geológica 3D]]
**Duração estimada:** ~27 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** definir o que é um modelo geológico tridimensional, situar seus principais usos na indústria e na pesquisa, apresentar a distinção de alto nível entre modelagem **explícita** e **implícita** (que a Aula 02 vai aprofundar em algoritmo), discutir vantagens e limitações da modelagem 3D frente à interpretação em seções 2D, e mapear o panorama de softwares comerciais e livres usados na área.
**Ao final você vai conseguir:** definir o que caracteriza um modelo geológico 3D (em oposição a um mapa ou a uma seção); listar pelo menos três domínios de aplicação em que a modelagem 3D é usada; diferenciar, em termos gerais, a lógica de um fluxo de trabalho explícito da de um fluxo implícito; enumerar vantagens e limitações centrais da modelagem 3D; e identificar os principais softwares comerciais e livres do mercado e o tipo de fluxo de trabalho que cada um privilegia.
**Pré-requisito:** [[21-modelagem-geoestatistica-depositos-minerais/21-modelagem-geoestatistica-depositos-minerais-modulo|Módulo 21]] (modelo de blocos, wireframes construídos por seção e triangulação de Delaunay — a base explícita que esta aula generaliza) e [[19-geofisica-exploracao-mineral/19-geofisica-exploracao-mineral-modulo|Módulo 19]] (os métodos e a lógica de inversão geofísica que entrarão como atributo do modelo nas Aulas 03 e 05).

## Conteúdo

### O que é um modelo geológico 3D

Um **modelo geológico tridimensional** é uma representação digital do subsolo — ou de um volume de rocha delimitado — em que cada unidade geológica de interesse (uma litologia, um domínio de alteração, um corpo mineralizado, uma falha) é representada como um objeto geométrico com posição, forma e volume no espaço tridimensional, e não apenas como um traço numa seção vertical ou um polígono num mapa. A diferença central em relação à cartografia geológica tradicional é que um mapa 2D e uma seção vertical são **projeções** de um objeto 3D sobre um plano — cada uma delas descarta a informação da terceira dimensão, deixando ao leitor a tarefa de reconstruir mentalmente a geometria completa a partir de fatias. O modelo 3D existe justamente para eliminar essa reconstrução mental: o volume é construído uma vez, no computador, e qualquer seção, planta ou vista pode ser extraída dele sob demanda, sempre consistente com o mesmo volume subjacente.

Essa mudança parece técnica, mas tem uma consequência prática importante: um modelo 3D é **testável por operações geométricas** que um conjunto de seções desenhadas à mão não permite de forma direta — calcular o volume (e, com uma função de teor associada, o tonelagem) de um corpo, testar se dois domínios se cruzam ou se tocam, calcular a distância de um ponto qualquer à superfície mais próxima, ou simular uma escavação e ver exatamente que litologias ela intercepta. A Aula 06 do Módulo 21 já introduziu a peça central dessa lógica — o **wireframe**, um sólido fechado construído a partir de seções interpretadas — como a forma mais tradicional de representar um domínio geológico em 3D. Este módulo generaliza essa ideia: em vez de um único fluxo de trabalho (seções → triangulação → sólido), existem hoje duas famílias inteiras de abordagens, com filosofias de construção muito diferentes, que esta aula introduz e a Aula 02 detalha.

### Para que serve um modelo geológico 3D

A construção de modelos 3D deixou de ser uma ferramenta de nicho e hoje atravessa praticamente toda a cadeia de aplicações da geologia aplicada:

- **Exploração e avaliação de recursos minerais** — o uso mais desenvolvido neste curso (Módulo 21): domínios geológicos como suporte para a estimativa de teores, cálculo de volume e tonelagem, e planejamento de sondagem (identificar onde a geometria do modelo está menos restringida por dados e merece um furo adicional).
- **Geologia do petróleo** — modelos de reservatório em 3D, construídos a partir de sísmica de reflexão e de perfis de poço, para simular o comportamento de fluidos e planejar a locação de poços.
- **Geotecnia e engenharia geológica** — modelos de subsuperfície urbana ou de taludes, integrando sondagens geotécnicas, para prever comportamento de fundações, túneis e encostas.
- **Hidrogeologia** — modelos de aquíferos, delimitando unidades hidroestratigráficas (camadas aquíferas e aquitardos) como base geométrica para simulações de fluxo subterrâneo.
- **Levantamentos geológicos nacionais e cartografia 3D regional** — vários serviços geológicos (por exemplo, o BRGM na França e a Geological Survey of Canada) mantêm ou já mantiveram programas de modelagem 3D em escala regional a nacional, produzindo o que se chama de mapa geológico 3D — um produto cartográfico que substitui o mapa 2D tradicional por um volume consultável.
- **Pesquisa em geologia estrutural e tectônica** — reconstrução 3D de sistemas de falhas e de dobras complexas, para testar hipóteses cinemáticas que são difíceis de visualizar apenas em seção.

O fio comum entre esses usos é que todos partem de dados esparsos e heterogêneos (furos, seções, levantamentos geofísicos, mapas de superfície) e precisam de uma geometria contínua e consistente no volume inteiro para responder perguntas quantitativas — volume, conectividade, trajetória de fluido — que dado esparso, por si, não responde.

### Modelagem explícita e modelagem implícita: a distinção de alto nível

Toda construção de modelo 3D resolve o mesmo problema — transformar dados esparsos numa superfície contínua que separa um domínio geológico do outro — mas existem, hoje, duas filosofias amplamente diferentes de resolvê-lo:

**Modelagem explícita** é o fluxo de trabalho em que o geólogo desenha diretamente a geometria: interpreta seções, digitaliza contatos como *strings* — o nome que os softwares de mineração dão a uma polilinha desenhada sobre uma seção, isto é, a sequência de pontos que traça um contato naquele corte —, e o software conecta essas *strings* numa superfície triangulada — exatamente o processo descrito na Aula 06 do Módulo 21 (interpretação de seção, triangulação de Delaunay, construção de wireframe). A geometria final é, no sentido literal, um desenho do geólogo, apoiado por ferramentas de triangulação automática entre as seções interpretadas.

**Modelagem implícita** é o fluxo de trabalho em que o geólogo não desenha a superfície diretamente: fornece ao software os dados brutos (pontos de contato interceptados por furos, medidas de atitude estrutural como direção e mergulho) e um algoritmo de interpolação matemática calcula automaticamente uma superfície que honra esses dados, segundo regras geoestatísticas ou geométricas explícitas. A Aula 02 detalha o algoritmo mais usado (o método do campo potencial, que tem uma ligação direta com a geoestatística do Módulo 20) e como ele se compara a alternativas.

Uma forma útil de guardar a diferença, ainda que aproximada: a modelagem explícita trata a geometria como **produto da interpretação manual do geólogo, auxiliada por ferramentas de desenho**; a modelagem implícita trata a geometria como **produto de um cálculo matemático sobre os dados, guiado pelas escolhas do geólogo nos parâmetros do algoritmo, não no traço da linha**. Nenhuma das duas elimina o julgamento geológico — ele só entra em pontos diferentes do fluxo de trabalho, e essa diferença de "onde o julgamento entra" é o fio condutor da Aula 02.

### Vantagens e limitações da modelagem 3D

Independentemente da abordagem escolhida, migrar de um conjunto de seções 2D para um modelo 3D unificado traz ganhos e custos que valem a pena enumerar antes de entrar no detalhe técnico das próximas aulas.

**Vantagens:**
- **Consistência geométrica garantida** — qualquer seção extraída do modelo é, por construção, compatível com todas as outras, o que elimina o problema clássico de seções desenhadas independentemente que não batem exatamente nas interseções.
- **Quantificação direta** — volume, tonelagem, área de contato entre domínios e distância a superfícies são cálculos diretos sobre o modelo, não estimativas aproximadas feitas à mão a partir de seções.
- **Atualização e propagação de novos dados** — um furo de sondagem novo pode, em princípio, ser incorporado ao modelo e as superfícies recalculadas, algo que é lento e trabalhoso de fazer manualmente em um conjunto grande de seções (mais fácil em fluxos implícitos, como a Aula 02 discute).
- **Comunicação e visualização** — um modelo 3D navegável comunica geometria de forma mais intuitiva a públicos não especialistas (investidores, engenheiros, órgãos reguladores) do que uma pilha de seções 2D.

**Limitações:**
- **Custo de dado e de tempo** — um modelo 3D confiável exige volume de dado (furos, seções, atitudes estruturais) proporcional à complexidade geológica; em áreas de dado esparso, o modelo preenche os vazios por interpolação (explícita ou implícita), e a qualidade dessa interpolação é tão boa quanto a densidade e a distribuição dos dados que a alimentam, nunca melhor.
- **Falsa sensação de certeza** — uma superfície suave e bem renderizada tem aparência de precisão que pode não corresponder à incerteza real da interpretação, sobretudo em zonas de baixa densidade de dado; a Aula 05 deste módulo trata desse problema diretamente, com o vocabulário de incerteza.
- **Custo computacional e de treinamento** — softwares de modelagem 3D exigem hardware, licenças e treinamento especializado, um investimento maior do que interpretar seções manualmente com ferramentas simples.
- **Complexidade de manutenção de versão** — um modelo em constante atualização, compartilhado por uma equipe, exige controle de versão e de proveniência de dado, uma disciplina que o desenho manual de seções não impõe da mesma forma.

### Panorama de softwares comerciais e livres

O ecossistema de softwares de modelagem geológica 3D combina pacotes comerciais consolidados na indústria de mineração e de petróleo com um conjunto crescente de ferramentas livres e de código aberto, sobretudo nascidas em ambiente acadêmico:

**Comerciais orientados à mineração:**
- **Leapfrog** (Seequent, hoje parte da Bentley Systems, que adquiriu a Seequent em 2021) — um dos pacotes mais usados para modelagem **implícita** na indústria mineral, construído sobre interpolação por funções de base radial.
- **Datamine Studio RM** (Datamine Software) — pacote britânico tradicional de longa data na indústria de mineração, com fluxos explícitos e implícitos.
- **Micromine** (Micromine, Austrália) — pacote amplamente usado em exploração e planejamento de mina, com módulos de modelagem explícita e implícita.
- **Vulcan** (Maptek, Austrália) — um dos pacotes mais antigos do setor, historicamente forte em modelagem explícita por seção e em planejamento de mina.

**Comerciais orientados a estrutural/petróleo:**
- **SKUA-GOCAD** (hoje comercializado como **Aspen SKUA**, da AspenTech — a Emerson adquiriu a Paradigm em 2019 e, em maio de 2022, transferiu seu negócio de *Geological Simulation Software* para a AspenTech, onde o produto integra a suíte Subsurface Science & Engineering; GOCAD nasceu como projeto acadêmico de Jean-Laurent Mallet e seu grupo na Ecole Nationale Supérieure de Géologie, em Nancy, na França, iniciado em 1989) — histórico marco em modelagem implícita de superfícies complexas (a técnica de interpolação suave discreta que ele populariza está na origem de vários algoritmos implícitos usados hoje).
- **Move** (Petroleum Experts, que adquiriu o software originalmente desenvolvido pela Midland Valley Exploration) — voltado a geologia estrutural, restauração de seções e modelagem de falhas.
- **Petrel** (SLB, antiga Schlumberger) — plataforma dominante de modelagem de reservatório na indústria de petróleo, com forte integração de dado sísmico.

**Livres e de código aberto:**
- **GemPy** — biblioteca Python de modelagem implícita de código aberto, desenvolvida pelo grupo de Geociência Computacional e Engenharia de Reservatórios da RWTH Aachen (Alemanha), publicada por de la Varga, Schaaf e Wellmann (2019); implementa o método do campo potencial que a Aula 02 detalha, com a vantagem adicional de permitir inversão probabilística dos parâmetros do modelo.
- **Loop3D** — plataforma de código aberto para modelagem geológica implícita probabilística, desenvolvida por um consórcio internacional (incluindo a Monash University e parceiros australianos), com foco em automatizar a construção de modelos a partir de mapas geológicos e dados estruturais digitais.
- **SGeMS** (*Stanford Geostatistical Modeling Software*) — ferramenta de código aberto da Universidade de Stanford, voltada primariamente à simulação geoestatística (o tipo de interpolação de grade discutido nos Módulos 20 e 21), usada como componente de fluxos de modelagem de teor mais do que como modelador de superfícies geológicas completo.

A escolha entre essas ferramentas raramente é puramente técnica: pacotes comerciais de mineração dominam por integração com o resto do fluxo de trabalho de recursos (o mesmo pacote frequentemente cobre a geoestatística dos Módulos 20–21), enquanto ferramentas livres ganham espaço em pesquisa acadêmica e em fluxos que exigem reprodutibilidade total do código e acesso ao algoritmo, algo que um pacote comercial fechado não oferece.

## Exemplo trabalhado

**Situação:** uma empresa de exploração mineral tem um depósito parcialmente perfurado (40 furos de sondagem, geometria em veio estreito e sinuoso) e precisa decidir, com uma equipe pequena e um prazo curto, se constrói o modelo geológico do corpo mineralizado por um fluxo explícito (seções interpretadas manualmente e trianguladas, como na Aula 06 do Módulo 21) ou por um fluxo implícito (interpolação automática a partir dos furos).

**Pergunta:** cite um argumento a favor de cada abordagem para este caso específico, e explique por que a decisão não é puramente uma questão de "qual método é melhor em geral".

**Resolução:** a favor do fluxo **explícito**: um veio estreito e sinuoso é exatamente o tipo de geometria em que o julgamento geológico fino sobre a continuidade do contato entre furos vizinhos — guiado pelo controle estrutural conhecido do veio — tende a superar uma interpolação automática genérica, que pode suavizar demais uma geometria propositalmente irregular; o geólogo que já interpretou veios similares tem informação (o modelo conceitual do controle estrutural) que não está explicitamente nos dados brutos dos furos. A favor do fluxo **implícito**: com uma equipe pequena e prazo curto, digitalizar e triangular manualmente 40 furos em várias seções é trabalho intensivo, e qualquer furo de sondagem futuro exigiria repetir boa parte do trabalho manual; um fluxo implícito incorpora os 40 furos automaticamente e pode ser atualizado em minutos quando novos furos chegarem, ao custo de exigir que o geólogo confie nos parâmetros do algoritmo para capturar a sinuosidade do veio (algo que pode exigir atitudes estruturais adicionais como dado de entrada, não só os furos).

A decisão não é puramente técnica porque depende de fatores que não estão na geometria do depósito em si: prazo disponível, tamanho e experiência da equipe, frequência esperada de atualização do modelo com dado novo, e a disponibilidade de dado estrutural (atitudes) que um fluxo implícito de qualidade normalmente exige além dos furos. É comum, na prática, que as duas abordagens sejam combinadas — um esqueleto implícito ajustado depois por seções explícitas em zonas críticas — o que a Aula 02 volta a mencionar ao comparar as duas famílias de algoritmo em mais detalhe.

## Recap relâmpago

- Um **modelo geológico 3D** representa unidades geológicas como objetos com volume no espaço, permitindo cálculos diretos (volume, interseção, distância) que seções 2D isoladas não permitem sem reconstrução mental.
- A modelagem 3D é usada em exploração e recursos minerais, geologia do petróleo, geotecnia, hidrogeologia, cartografia geológica regional e pesquisa estrutural — o fio comum é transformar dado esparso em geometria contínua e consistente.
- **Modelagem explícita** é o geólogo desenhando a geometria diretamente (seções interpretadas → triangulação → wireframe, como na Aula 06 do Módulo 21); **modelagem implícita** é um algoritmo de interpolação calculando a superfície a partir dos dados brutos e das escolhas de parâmetro do geólogo — a Aula 02 detalha o algoritmo.
- A modelagem 3D ganha em consistência geométrica, quantificação direta e atualização de dado, mas custa em volume de dado exigido, risco de falsa certeza visual, custo computacional/de treinamento e disciplina de controle de versão.
- O mercado de software se divide entre pacotes comerciais orientados à mineração (Leapfrog, Datamine, Micromine, Vulcan), pacotes orientados a estrutural/petróleo (SKUA-GOCAD, Move, Petrel) e ferramentas livres de origem acadêmica (GemPy, Loop3D, SGeMS) — a escolha combina critério técnico com integração ao resto do fluxo de trabalho da equipe.

## Próxima aula

[[22-modelagem-geologica-3d-aula-02-dados-algoritmos-modelagem-explicita-implicita|Aula 02 — Dados e algoritmos: integração de superfície (2D) e subsuperfície (3D); modelagem explícita versus implícita]] — o detalhe algorítmico da distinção introduzida aqui, incluindo o método do campo potencial que conecta a modelagem implícita à geoestatística já estudada nos Módulos 20 e 21.

## Fontes

- Caumon, G., Collon-Drouaillet, P., Le Carlier de Veslud, C., Viseur, S. & Sausse, J. (2009), "Surface-Based 3D Modeling of Geological Structures", *Mathematical Geosciences*, 41(8), 927-945 (panorama de abordagens explícitas e implícitas de modelagem geológica 3D).
- Wellmann, F. & Caumon, G. (2018), "3-D Structural geological models: Concepts, methods, and uncertainties", *Advances in Geophysics*, 59, 1-121 (visão geral de usos, fluxos de trabalho e limitações da modelagem geológica 3D).
- de la Varga, M., Schaaf, A. & Wellmann, F. (2019), "GemPy 1.0: open-source stochastic geological modeling and inversion", *Geoscientific Model Development*, 12(1), 1-32, DOI 10.5194/gmd-12-1-2019 (GemPy como ferramenta livre de modelagem implícita).
- Bentley Systems (2021), comunicado de conclusão da aquisição da Seequent, 17 de junho de 2021 (histórico corporativo de Leapfrog); AspenTech (2022), comunicado de conclusão da transação com a Emerson, 16 de maio de 2022, que transferiu à AspenTech o negócio de *Geological Simulation Software* da Emerson, incluindo o SKUA-GOCAD.
- Mallet, J.-L. (1992), "GOCAD: a computer aided design program for geological applications", em Turner, A. K. (ed.), *Three-Dimensional Modeling with Geoscientific Information Systems*, NATO ASI Series C 354, Kluwer, 123-141 (origem acadêmica do GOCAD na Ecole Nationale Supérieure de Géologie de Nancy; o método de interpolação suave discreta em si é formulado em Mallet, J.-L. (1989), "Discrete smooth interpolation", *ACM Transactions on Graphics*, 8(2), 121-144).

<!--
nivel: avancado
palavras_corpo: 2050
mapa_objetivo_secao:
  geologia-avancado-m22-oa01: "O que é um modelo geológico 3D" + "Modelagem explícita e modelagem implícita: a distinção de alto nível" + "Vantagens e limitações da modelagem 3D" + "Panorama de softwares comerciais e livres" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOMOD3D-M22-A01-EXPLICITAIMPLICITA-001
    claim: "Modelagem explicita e o fluxo de trabalho em que o geologo desenha diretamente a geometria (secoes interpretadas, digitalizadas como strings e trianguladas em wireframe); modelagem implicita e o fluxo em que um algoritmo de interpolacao matematica calcula automaticamente a superficie a partir de dados brutos (pontos de contato e atitudes estruturais), segundo regras geoestatisticas ou geometricas explicitas."
    risk: fato
    source: "Caumon, Collon-Drouaillet, Le Carlier de Veslud, Viseur & Sausse (2009), 'Surface-Based 3D Modeling of Geological Structures', Mathematical Geosciences, 41(8), 927-945; Wellmann & Caumon (2018), 'Advances in Geophysics', 59, 1-121."
  - claim_id: GEOMOD3D-M22-A01-SOFTWARESMINERACAO-002
    claim: "Leapfrog (Seequent, adquirida pela Bentley Systems em 2021) e um dos pacotes mais usados para modelagem implicita na industria mineral, construido sobre interpolacao por funcoes de base radial; Datamine Studio RM (Datamine Software, Reino Unido), Micromine (Australia) e Vulcan (Maptek, Australia) sao outros pacotes comerciais tradicionais de modelagem geologica/mina, com fluxos explicitos e implicitos."
    risk: fato
    source: "Bentley Systems (2021), comunicado oficial de aquisicao da Seequent; Cowan, Beatson, Ross et al. (2003), 'Practical implicit geological modelling', 5th International Mining Geology Conference (base RBF do Leapfrog); materiais institucionais publicos da Datamine, Micromine e Maptek sobre historico e escopo dos respectivos produtos."
  - claim_id: GEOMOD3D-M22-A01-GOCADORIGEM-003
    claim: "O GOCAD nasceu como projeto academico de Jean-Laurent Mallet e seu grupo na Ecole Nationale Superieure de Geologie, em Nancy, na Franca, iniciado em 1989, e populariza uma tecnica de interpolacao suave discreta (Discrete Smooth Interpolation) que esta na origem de varios algoritmos de modelagem implicita usados posteriormente na industria."
    risk: fato
    source: "Mallet, J.-L. (1992), 'GOCAD: A Computer Aided Design Program for Geological Applications', em Turner, A. K. (ed.), Three-Dimensional Modeling with Geoscientific Information Systems, NATO ASI Series vol. 354, Kluwer/Springer Dordrecht, 123-141; Mallet, J.-L. (1989), 'Discrete smooth interpolation', ACM Transactions on Graphics, 8(2), 121-144; pagina institucional do RING Team (Universite de Lorraine) sobre a fundacao do projeto Gocad em 1989."
  - claim_id: GEOMOD3D-M22-A01-SKUAVENDOR-005
    claim: "O SKUA-GOCAD e hoje comercializado como Aspen SKUA pela AspenTech, dentro da suite Subsurface Science & Engineering: a Emerson adquiriu a Paradigm em 2019 e, na conclusao da transacao com a AspenTech em 16 de maio de 2022, transferiu a esta o seu negocio de Geological Simulation Software, do qual o produto faz parte."
    risk: fato
    source: "AspenTech (2022), comunicado 'AspenTech Completes Emerson Transaction', 16 de maio de 2022 (inclusao dos negocios OSI e Geological Simulation Software da Emerson na AspenTech); pagina de produto Aspen SKUA da AspenTech."
  - claim_id: GEOMOD3D-M22-A01-FERRAMENTASLIVRES-004
    claim: "GemPy e uma biblioteca Python de codigo aberto para modelagem geologica implicita, desenvolvida pelo grupo de Geociencia Computacional e Engenharia de Reservatorios da RWTH Aachen (Alemanha) e publicada por de la Varga, Schaaf e Wellmann (2019); Loop3D e uma plataforma de codigo aberto para modelagem implicita probabilistica desenvolvida por um consorcio internacional incluindo a Monash University; SGeMS e um software livre da Universidade de Stanford voltado primariamente a simulacao geoestatistica, mais do que a modelagem completa de superficies geologicas."
    risk: fato
    source: "de la Varga, Schaaf & Wellmann (2019), 'GemPy 1.0: open-source stochastic geological modeling and inversion', Geoscientific Model Development, 12(1), 1-32, DOI 10.5194/gmd-12-1-2019; documentacao publica do projeto Loop3D (consorcio Loop); Remy, N., Boucher, A. & Wu, J. (2009), Applied Geostatistics with SGeMS, Cambridge University Press."
-->
