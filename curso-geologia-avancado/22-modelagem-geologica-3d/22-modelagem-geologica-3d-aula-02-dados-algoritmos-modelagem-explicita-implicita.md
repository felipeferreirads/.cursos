# Aula 02: Dados e algoritmos — integração de superfície (2D) e subsuperfície (3D); modelagem explícita versus implícita

**ID:** geologia-avancado-m22-a02
**Módulo:** [[22-modelagem-geologica-3d-modulo|Módulo 22 — Modelagem geológica 3D]]
**Duração estimada:** ~29 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** detalhar que tipos de dado alimentam um modelo geológico 3D — de superfície (2D) e de subsuperfície (3D) — como esses dados se integram num mesmo modelo, e como os algoritmos de modelagem explícita e implícita usam esses dados de formas fundamentalmente diferentes, com foco no método do campo potencial que sustenta a maioria dos softwares implícitos modernos.
**Ao final você vai conseguir:** classificar um dado de entrada de modelagem 3D como de superfície ou de subsuperfície e explicar como cada um entra no modelo; descrever o fluxo de trabalho explícito de ponta a ponta; explicar o princípio do método do campo potencial usado na modelagem implícita, incluindo o papel dos dados de interface e dos dados de orientação; e comparar as duas abordagens em termos de robustez a dado esparso, velocidade de atualização e risco de artefato geométrico.
**Pré-requisito:** Aula 01 deste módulo (definições gerais de modelagem explícita e implícita) e Módulo 20 (variografia, covariância espacial e krigagem). **Atenção a um degrau de pré-requisito:** o método do campo potencial desta aula se apoia em **cokrigagem**, que o Módulo 20 declara explicitamente fora do seu escopo — por isso a seção "A ligação com a geoestatística" define abaixo o que dela é preciso saber, sem supor que você já a tenha estudado.

## Conteúdo

### Dados de superfície (2D) e de subsuperfície (3D)

Um modelo geológico 3D raramente nasce de uma única fonte de dado: ele integra informação de **superfície**, bidimensional por natureza, e informação de **subsuperfície**, intrinsecamente tridimensional, dentro de um único volume consistente.

**Dados de superfície (2D):**
- **Mapas geológicos** — a distribuição de litologias e de contatos observados em afloramento, geralmente já vetorizados como polígonos e linhas num sistema de informação geográfica.
- **Modelo digital de elevação (MDE/DEM)** — a topografia, que funciona como o limite superior obrigatório de qualquer modelo (nenhuma unidade geológica pode existir acima da superfície do terreno, exceto no caso deliberado de reconstruções paleogeográficas).
- **Lineamentos estruturais interpretados** de sensoriamento remoto ou de mapas aeromagnéticos e radiométricos (Módulo 16) — indicam a provável posição em planta de falhas e contatos que não afloram continuamente.

**Dados de subsuperfície (3D):**
- **Furos de sondagem** — o dado mais direto de subsuperfície: cada furo fornece, ao longo de sua trajetória 3D, os pontos exatos onde o furo atravessou um contato geológico (dado de **interface**), e, quando o testemunho é orientado, a atitude (direção e mergulho) da estrutura interceptada naquele ponto (dado de **orientação**).
- **Seções interpretadas** — como na Aula 06 do Módulo 21, *strings* digitalizadas que já representam a interpretação de um contato ao longo de um corte vertical; funcionam tanto como insumo de um fluxo explícito quanto como restrição adicional (*constraint*) num fluxo implícito.
- **Modelos de inversão geofísica** — grades 3D de propriedade física (densidade, susceptibilidade magnética, resistividade elétrica), produzidas pelos métodos e pelo processo de inversão do Módulo 19; a Aula 03 deste módulo detalha como essa informação entra especificamente como atributo do modelo.

A integração desses dados num único modelo exige que todos compartilhem o mesmo sistema de coordenadas e o mesmo referencial vertical (datum), e que o topo do modelo seja "colado" à topografia — um cuidado simples, mas cuja ausência é uma fonte comum de erro grosseiro (unidades geológicas "flutuando" acima do terreno real, ou o contrário: contatos cortando a superfície de forma fisicamente impossível).

### O fluxo de trabalho explícito, revisitado

A modelagem explícita, já descrita em linhas gerais na Aula 06 do Módulo 21 e na Aula 01 deste módulo, segue um fluxo de quatro etapas centrado no julgamento visual do geólogo sobre cada seção:

1. **Seleção e orientação das seções** — decidir onde cortar o volume (seções verticais paralelas, seções em leque, ou plantas em bancada), tipicamente perpendiculares à direção principal de continuidade geológica esperada.
2. **Interpretação e digitalização** — para cada seção, o geólogo projeta os furos e traça manualmente as *strings* de contato, guiado pelo modelo conceitual da geologia local.
3. **Triangulação entre seções** — o software conecta as *strings* de seções sucessivas por triangulação (tipicamente derivada da triangulação de Delaunay, Módulo 21 Aula 06), gerando a superfície contínua entre os cortes.
4. **Fechamento e validação topológica** — como já visto, garantindo um sólido fechado sem auto-interseções.

O ponto central deste fluxo, que a Aula 01 já adiantou, é que a geometria entre as seções interpretadas é **interpolada geometricamente pela triangulação**, mas a **decisão sobre onde o contato está** é inteiramente do geólogo em cada seção — o algoritmo só conecta pontos já escolhidos por julgamento humano. Isso torna o fluxo explícito altamente controlável (o geólogo vê e aprova cada traço), mas também o torna **caro em tempo** e **difícil de atualizar**: um furo novo, fora do plano de seções original, obriga a reinterpretar (ou pelo menos revisar) as seções vizinhas antes de retriangular.

### O fluxo de trabalho implícito: o método do campo potencial

A alternativa dominante na modelagem implícita moderna resolve o mesmo problema — encontrar a superfície que separa dois domínios geológicos — sem que o geólogo desenhe a superfície diretamente. O método mais difundido, introduzido por Lajaunie, Courrioux e Manuel (1997) e formalizado no fluxo de trabalho do software GeoModeller por Calcagno et al. (2008), é conhecido como **método do campo potencial** (*potential-field method*):

**A ideia central.** Em vez de desenhar contatos, o geólogo fornece dois tipos de dado de entrada — exatamente os dois tipos já descritos acima como dados de furo:
- **Pontos de interface** — localizações 3D onde se sabe que um contato geológico passa (por exemplo, onde um furo cruzou o topo de uma unidade).
- **Dados de orientação** — a atitude (vetor normal ao contato, derivado de direção e mergulho) medida num afloramento ou num testemunho orientado, em qualquer ponto do volume, não apenas sobre o próprio contato.

O algoritmo então interpola um **campo escalar contínuo** (o "potencial") sobre todo o volume 3D, com duas condições simultâneas: (1) o campo deve assumir o **mesmo valor** em todos os pontos de interface fornecidos para um dado contato (ou seja, o contato é uma **isosuperfície** — uma superfície de valor constante — desse campo); e (2) o **gradiente** do campo (a direção de variação mais rápida) deve ser paralelo ao vetor normal medido em cada dado de orientação fornecido. A superfície geológica final é simplesmente a isosuperfície do campo potencial correspondente ao valor da interface.

**A ligação com a geoestatística.** O cálculo desse campo escalar não é arbitrário: Lajaunie et al. (1997) mostraram que o problema pode ser resolvido de forma matematicamente equivalente a uma **cokrigagem universal**. O adjetivo "universal" tem aqui o mesmo sentido que o Módulo 20 (Aula 02) já registrou ao falar de **krigagem universal**: a variável estimada não é estacionária, carrega uma **deriva** (*drift*) — uma tendência sistemática de fundo —, e o sistema resolve essa tendência junto com a interpolação, em vez de supor média constante. No caso do campo potencial isso não é um refinamento opcional: o potencial é uma variável abstrata cujo valor absoluto não tem significado, só os seus incrementos têm, e é precisamente essa indeterminação que a formulação universal acomoda.

Antes de seguir, a definição que o Módulo 20 não deu: **cokrigagem** é a generalização da krigagem para o caso em que duas ou mais variáveis correlacionadas são estimadas em conjunto. A krigagem do Módulo 20 estima um valor num ponto a partir de amostras *da mesma variável*, pesando-as por um modelo de covariância (ou variograma). A cokrigagem faz o mesmo, mas admite que amostras de uma *segunda* variável, correlacionada com a primeira, também entrem na conta e recebam peso — o que exige, além da covariância de cada variável consigo mesma, uma **covariância cruzada** que descreva como as duas variam juntas no espaço. O ganho é justamente o de aproveitar dado que a krigagem simples teria de descartar por ser "de outra variável".

É essa máquina que o campo potencial usa, entre duas variáveis — o próprio potencial (observado apenas de forma relativa, nos pontos de interface) e o seu gradiente (observado diretamente, nos dados de orientação) —, com o detalhe conveniente de que aqui as duas variáveis não são medidas independentes: uma é a derivada da outra, e a covariância cruzada decorre da covariância do potencial em vez de precisar ser modelada à parte. A modelagem implícita por campo potencial é, no fundo, uma aplicação da mesma máquina geoestatística já usada para interpolar teor, agora aplicada a uma variável geométrica abstrata (o potencial) em vez de a um teor.

**Alternativas ao campo potencial.** Duas outras famílias de algoritmo implícito são amplamente usadas, sobretudo na indústria mineral:
- **Interpolação por funções de base radial (RBF)** — descrita por Cowan, Beatson, Ross et al. (2003) e na base de softwares como o Leapfrog (Aula 01); em vez de resolver um sistema de cokrigagem geoestatística, ajusta uma combinação de funções radiais centradas nos pontos de dado para produzir uma superfície implícita que honra os pontos de interface e as orientações, com formulação matemática diferente do campo potencial mas objetivo equivalente.
- **Interpolação suave discreta (DSI)**, popularizada pelo GOCAD (Mallet, 1992, Aula 01), que resolve a geometria por minimização de uma energia de suavidade sobre uma malha discreta, em vez de por um campo contínuo analítico.

Métodos mais recentes estendem o campo potencial para tratar explicitamente **dobras e deformação superposta** — Laurent et al. (2016) constroem um referencial de dobra (*fold frame*) a partir da superfície axial e do eixo da dobra, descrevendo a geometria dobrada por ângulos de rotação em vez de deixá-la emergir da interpolação —, um problema que a formulação original de 1997 não resolvia bem sozinha. O tratamento de **falhas** segue um caminho distinto, já presente em Calcagno et al. (2008) e sistematizado em Caumon et al. (2009): é o assunto da Aula 03.

### Comparando as duas abordagens

Com o algoritmo do campo potencial em mãos, a comparação entre explícito e implícito, introduzida em termos gerais na Aula 01, pode ser precisada:

- **Robustez a dado esparso.** Em zonas de dado esparso, o fluxo explícito exige que o geólogo **preencha o vazio com julgamento geológico explícito** (uma decisão consciente e documentável, ainda que subjetiva); o fluxo implícito preenche o mesmo vazio **automaticamente**, segundo o comportamento matemático do algoritmo de interpolação (por exemplo, o campo potencial tende a gerar superfícies suaves e sem singularidades onde não há dado para restringi-lo). O risco específico do fluxo implícito — antecipado no hub deste módulo — é que essa suavidade automática **parece** uma interpretação geológica confiável mesmo quando não há dado nenhum sustentando aquele trecho específico da superfície.
- **Velocidade de atualização.** Um furo novo é incorporado a um modelo implícito recalculando o campo potencial (minutos a poucas horas, dependendo do tamanho do modelo); o mesmo furo, num fluxo explícito, pode exigir a revisão manual de várias seções vizinhas.
- **Controle e auditabilidade.** No fluxo explícito, cada traço de contato é uma decisão visível e revisável linha por linha; no fluxo implícito, a "decisão" está distribuída nos parâmetros do algoritmo (o alcance e a forma da função de covariância ou da função radial, o peso relativo dado a pontos de interface versus dados de orientação) — parâmetros que exigem outro tipo de expertise (geoestatística ou interpolação numérica) para auditar com o mesmo rigor.
- **Geometrias complexas e descontínuas.** Dobras muito apertadas, superposição de eventos de deformação e redes de falha complexas historicamente favoreceram o fluxo explícito, porque o geólogo pode aplicar julgamento estrutural caso a caso; os métodos implícitos mais recentes (RBF avançado, campo potencial estendido para dobras superpostas) reduziram essa vantagem, mas não a eliminaram por completo em cenários estruturalmente muito complexos.

Na prática profissional, a maioria dos projetos combina as duas abordagens: um esqueleto implícito rápido para a primeira versão do modelo e para atualização contínua com dado novo, revisado e ajustado manualmente (explicitamente) em zonas críticas onde o geólogo tem razão para desconfiar da interpolação automática — geralmente exatamente as zonas de dado mais esparso, onde a diferença entre as duas filosofias mais importa.

## Exemplo trabalhado

**Situação:** um geólogo está construindo o modelo implícito de um contato litológico usando o método do campo potencial. Ele fornece ao software três pontos de interface ao longo do contato (interceptados por três furos diferentes) e, separadamente, duas medidas de atitude estrutural (direção/mergulho) obtidas de afloramentos próximos, mas que não estão exatamente sobre o contato.

**Pergunta:** (a) que condição matemática o campo potencial calculado precisa satisfazer nos três pontos de interface? (b) as duas medidas de atitude, mesmo não estando sobre o contato, são úteis para o cálculo — por quê, e que condição elas impõem ao campo?

**Resolução:**

**(a)** O campo potencial precisa assumir o **mesmo valor numérico** (o valor associado a esse contato específico) nos três pontos de interface — essa é justamente a definição de uma isosuperfície do campo: o contato modelado é o lugar geométrico onde o campo tem aquele valor constante. Não é necessário que os três pontos estejam próximos entre si nem alinhados de forma simples; o algoritmo de cokrigagem calcula o campo em todo o volume de forma que essa igualdade de valor seja satisfeita exatamente (ou aproximadamente, dependendo do tratamento de erro de dado) nos três pontos, e a isosuperfície correspondente passa, por construção, por todos eles.

**(b)** As medidas de atitude são úteis mesmo fora do contato porque elas não restringem o **valor** do campo potencial naquele ponto, mas sim a **direção do seu gradiente** — e essa é uma informação sobre o comportamento local do campo, válida em qualquer ponto do volume, não apenas sobre a própria superfície de interesse. Fisicamente, um dado de orientação diz "a rocha, aqui, está inclinada nesta direção", e o algoritmo usa essa informação para orientar corretamente a inclinação da isosuperfície interpolada nas vizinhanças daquele ponto, mesmo que o ponto medido não esteja sobre o contato modelado especificamente. É esse mecanismo — usar orientação medida em qualquer lugar do volume para restringir a forma do campo em todo o volume, não só no ponto medido — que permite ao método do campo potencial produzir superfícies com mergulho e curvatura geologicamente plausíveis mesmo em regiões sem pontos de interface diretos, generalizando a informação estrutural regional de um jeito que o método das áreas de influência puramente geométrico (Módulo 21, Aula 06) não tem como fazer.

## Recap relâmpago

- **Dados de superfície (2D)** — mapas geológicos, MDE/topografia, lineamentos interpretados — definem o contexto e o limite superior do modelo; **dados de subsuperfície (3D)** — furos (pontos de interface e de orientação), seções interpretadas, grades de inversão geofísica — restringem sua geometria interna; todos precisam compartilhar sistema de coordenadas e datum.
- O **fluxo explícito** segue seleção de seções → interpretação/digitalização manual de contatos → triangulação entre seções → validação topológica; o julgamento geológico entra em cada traço, o que o torna controlável mas caro em tempo e lento de atualizar.
- O **método do campo potencial** (Lajaunie et al. 1997; Calcagno et al. 2008) interpola um campo escalar contínuo tal que os contatos observados são isosuperfícies desse campo (mesmo valor nos pontos de interface) e o gradiente do campo casa com as atitudes estruturais medidas (dados de orientação) — matematicamente equivalente a uma **cokrigagem universal** entre o potencial e seu gradiente. **Cokrigagem** é a krigagem generalizada a duas ou mais variáveis correlacionadas estimadas em conjunto, com uma covariância cruzada além da covariância de cada uma — a extensão natural da krigagem do Módulo 20, que a tratava como fora de escopo.
- Alternativas implícitas incluem interpolação por **funções de base radial (RBF)** (base do Leapfrog) e **interpolação suave discreta (DSI)** (base do GOCAD), com formulações matemáticas diferentes mas objetivo equivalente.
- Comparando as abordagens: implícito ganha em velocidade de atualização e cobre dado esparso automaticamente (com o risco de suavizar demais onde não há dado real), explícito ganha em auditabilidade e controle direto do geólogo sobre cada traço — na prática, a maioria dos projetos combina as duas, usando o explícito para revisar zonas críticas de dado esparso.

## Anterior

[[22-modelagem-geologica-3d-aula-01-definicoes-usos-vantagens-limitacoes-softwares|Aula 01 — Modelagem geológica 3D: definições, usos, vantagens e limitações; softwares comerciais e livres]].

## Próxima aula

[[22-modelagem-geologica-3d-aula-03-atributos-geologicos-geofisicos-inversao|Aula 03 — Atributos geológicos, estruturais, geoquímicos e geofísicos no modelo; modelos geofísicos de inversão e modelos geológicos]] — como os dados discutidos aqui (sobretudo as grades de inversão geofísica) entram como atributos populando o modelo, e como se avalia a coerência entre o modelo geológico e o modelo geofísico.

## Fontes

- Lajaunie, C., Courrioux, G. & Manuel, L. (1997), "Foliation fields and 3D cartography in geology: principles of a method based on potential interpolation", *Mathematical Geology*, 29(4), 571-584 (formulação original do método do campo potencial).
- Calcagno, P., Chilès, J. P., Courrioux, G. & Guillen, A. (2008), "Geological modelling from field data and geological knowledge: Part I. Modelling method coupling 3D potential-field interpolation and geological rules", *Physics of the Earth and Planetary Interiors*, 171(1-4), 147-157 (formalização do método no fluxo de trabalho do GeoModeller, sua equivalência com cokrigagem e o tratamento de falhas como descontinuidades inseridas no campo potencial).
- Cowan, E. J., Beatson, R. K., Ross, H. J. et al. (2003), "Practical implicit geological modelling", *5th International Mining Geology Conference*, Bendigo, 89-99 (interpolação por funções de base radial aplicada à modelagem geológica de mina).
- Laurent, G., Ailleres, L., Grose, L., Caumon, G., Jessell, M. & Armit, R. (2016), "Implicit modeling of folds and overprinting deformation", *Earth and Planetary Science Letters*, 456, 26-38 (extensão do campo potencial a dobras e deformação superposta, por meio de um referencial de dobra construído sobre a superfície axial e o eixo da dobra — o artigo **não** trata de redes de falha).
- Caumon, G., Collon-Drouaillet, P., Le Carlier de Veslud, C., Viseur, S. & Sausse, J. (2009), "Surface-Based 3D Modeling of Geological Structures", *Mathematical Geosciences*, 41(8), 927-945 (panorama das estratégias de modelagem de descontinuidades estruturais, retomado na Aula 03).
- Mallet, J.-L. (1992), "GOCAD: A Computer Aided Design Program for Geological Applications", em Turner, A. K. (ed.), *Three-Dimensional Modeling with Geoscientific Information Systems*, NATO ASI Series vol. 354, Kluwer/Springer Dordrecht, 123-141 (interpolação suave discreta; formulação original do método em Mallet, J.-L. (1989), "Discrete smooth interpolation", *ACM Transactions on Graphics*, 8(2), 121-144).

<!--
nivel: avancado
palavras_corpo: 2180
mapa_objetivo_secao:
  geologia-avancado-m22-oa01: "O fluxo de trabalho explícito, revisitado" + "O fluxo de trabalho implícito: o método do campo potencial" + "Comparando as duas abordagens" + "Exemplo trabalhado"
  geologia-avancado-m22-oa02: "Dados de superfície (2D) e de subsuperfície (3D)" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOMOD3D-M22-A02-TIPOSDEDADO-001
    claim: "Um modelo geologico 3D integra dados de superficie 2D (mapas geologicos, modelo digital de elevacao/topografia como limite superior obrigatorio, lineamentos estruturais interpretados) e dados de subsuperficie 3D (furos de sondagem, fornecendo pontos de interface e, quando o testemunho e orientado, dados de orientacao/atitude; secoes interpretadas; grades de inversao geofisica), exigindo sistema de coordenadas e datum compartilhados entre todas as fontes."
    risk: fato
    source: "Wellmann & Caumon (2018), 'Advances in Geophysics', 59, 1-121, secoes sobre tipos de dado de entrada em modelagem geologica 3D; Caumon, Collon-Drouaillet, Le Carlier de Veslud, Viseur & Sausse (2009), Mathematical Geosciences, 41(8), 927-945."
  - claim_id: GEOMOD3D-M22-A02-CAMPOPOTENCIAL-002
    claim: "O metodo do campo potencial, introduzido por Lajaunie, Courrioux e Manuel (1997) e formalizado no fluxo de trabalho do software GeoModeller por Calcagno et al. (2008), interpola um campo escalar continuo sobre o volume 3D tal que um contato geologico observado e uma isosuperficie desse campo (mesmo valor em todos os pontos de interface fornecidos) e o gradiente do campo e paralelo ao vetor normal medido em cada dado de orientacao/atitude estrutural fornecido, em qualquer ponto do volume, nao apenas sobre o proprio contato."
    risk: fato
    source: "Lajaunie, Courrioux & Manuel (1997), 'Foliation fields and 3D cartography in geology: principles of a method based on potential interpolation', Mathematical Geology, 29(4), 571-584; Calcagno, Chiles, Courrioux & Guillen (2008), 'Geological modelling from field data and geological knowledge: Part I. Modelling method coupling 3D potential-field interpolation and geological rules', Physics of the Earth and Planetary Interiors, 171(1-4), 147-157."
  - claim_id: GEOMOD3D-M22-A02-EQUIVALENCIACOKRIGAGEM-003
    claim: "Lajaunie, Courrioux e Manuel (1997) mostraram que o calculo do campo potencial e matematicamente equivalente a uma COKRIGAGEM UNIVERSAL entre o potencial (observado de forma relativa nos pontos de interface) e o seu gradiente (observado diretamente nos dados de orientacao), usando um modelo de covariancia que descreve a correlacao espacial do campo com a distancia — a mesma maquina geoestatistica de interpolacao por krigagem/cokrigagem aplicada a uma variavel geometrica abstrata em vez de a um teor. Como uma das variaveis e a derivada da outra, a covariancia cruzada decorre da covariancia do potencial em vez de ser modelada a parte."
    risk: fato
    source: "Lajaunie, Courrioux & Manuel (1997), Mathematical Geology, 29(4), 571-584, secao de formulacao matematica do metodo (cokrigagem universal do potencial e do gradiente); Calcagno et al. (2008), Physics of the Earth and Planetary Interiors, 171(1-4), 147-157."
  - claim_id: GEOMOD3D-M22-A02-PREREQCOKRIGAGEM-005
    claim: "Cokrigagem e a generalizacao da krigagem para o caso em que duas ou mais variaveis correlacionadas sao estimadas em conjunto, exigindo, alem da covariancia (ou variograma) de cada variavel consigo mesma, uma covariancia cruzada que descreva como as duas variam juntas no espaco. O Modulo 20 deste curso declara explicitamente a cokrigagem FORA DO SEU ESCOPO (Aula 01, secao de correlacao e regressao), de modo que esta aula nao pode pressupo-la como pre-requisito ja estudado e a define no proprio texto."
    risk: fato
    source: "Definicao padrao da literatura geoestatistica: Chiles, J.-P. & Delfiner, P. (2012), Geostatistics: Modeling Spatial Uncertainty, 2a ed., Wiley, capitulo 5 (cokriging); Goovaerts, P. (1997), Geostatistics for Natural Resources Evaluation, Oxford University Press, capitulo 6. Inconsistencia interna verificada contra 20-geoestatistica/20-geoestatistica-aula-01-preparacao-dados-estatistica-descritiva.md, que registra a cokrigagem como fora do escopo do Modulo 20."
  - claim_id: GEOMOD3D-M22-A02-ALGORITMOSALTERNATIVOS-004
    claim: "Alem do metodo do campo potencial, duas outras familias de algoritmo de modelagem implicita sao amplamente usadas: interpolacao por funcoes de base radial (RBF), descrita por Cowan, Beatson, Ross et al. (2003) e na base de softwares como o Leapfrog; e interpolacao suave discreta (Discrete Smooth Interpolation, DSI), popularizada pelo GOCAD (Mallet, 1992; formulacao original em Mallet, 1989), que resolve a geometria por minimizacao de uma energia de suavidade sobre uma malha discreta em vez de por um campo continuo analitico. Trabalhos mais recentes (Laurent et al., 2016) estendem o campo potencial para tratar DOBRAS E DEFORMACAO SUPERPOSTA, por meio de um referencial de dobra construido sobre a superficie axial e o eixo da dobra, problema mal resolvido pela formulacao original de 1997; o tratamento de REDES DE FALHA e um problema distinto, tratado por Calcagno et al. (2008) e Caumon et al. (2009), e NAO e objeto de Laurent et al. (2016)."
    risk: fato
    source: "Cowan, Beatson, Ross et al. (2003), 'Practical implicit geological modelling', 5th International Mining Geology Conference, Bendigo, 17-19 nov. 2003, 89-99; Mallet (1992), NATO ASI Series vol. 354, Kluwer/Springer, 123-141, e Mallet (1989), ACM Transactions on Graphics, 8(2), 121-144; Laurent, Ailleres, Grose, Caumon, Jessell & Armit (2016), 'Implicit modeling of folds and overprinting deformation', Earth and Planetary Science Letters, 456, 26-38 (verificado: escopo do artigo e dobras e deformacao superposta, nao redes de falha); Calcagno et al. (2008), PEPI 171(1-4), 147-157; Caumon et al. (2009), Mathematical Geosciences, 41(8), 927-945."
-->
