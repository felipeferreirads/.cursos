# Aula 04: Tipos, tamanhos e geometrias de depósitos minerais e a estratégia de modelagem

**ID:** geologia-avancado-m22-a04
**Módulo:** [[22-modelagem-geologica-3d-modulo|Módulo 22 — Modelagem geológica 3D]]
**Duração estimada:** ~27 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** relacionar os principais tipos de depósito mineral — e a geometria característica de cada um — à estratégia de modelagem 3D mais apropriada, mostrando que o critério de decisão não é a classe genética do depósito, mas a natureza física do limite entre mineralização e encaixante.
**Ao final você vai conseguir:** descrever a geometria típica de quatro famílias de depósito mineral (tabular estreita, disseminada/stockwork, controlada por estratigrafia, maciça/pipe); distinguir **estratiforme** de **estratabound** e alocar corretamente os exemplos clássicos de cada um; relacionar cada geometria à escolha entre modelagem predominantemente explícita, implícita ou híbrida, e ao espaçamento de dado exigido; e justificar por que o mesmo algoritmo de modelagem pode produzir resultados de qualidade muito diferente dependendo do tipo de depósito ao qual é aplicado.
**Pré-requisito:** Aulas 01–03 deste módulo (fluxos explícito e implícito, atributos geológicos e geofísicos).

> **Esta é a Parte 1 de um par.** Aqui a pergunta é **"que geometria este depósito tem, e que fluxo de trabalho ela favorece?"**. A [[22-modelagem-geologica-3d-aula-05-modelo-3d-teste-interpretacao-metalogenetica|Aula 05]] faz a pergunta seguinte, que é de outra natureza: **"o modelo, uma vez construído, sustenta ou derruba a hipótese sobre como este depósito se formou?"**. A primeira é uma decisão de método; a segunda é um uso do modelo como instrumento de teste científico.

## Conteúdo

### Por que a geometria do depósito dita a estratégia de modelagem

As Aulas 01 e 02 apresentaram a distinção explícito/implícito como uma escolha genérica, dependente de prazo, equipe e disponibilidade de dado estrutural. Mas existe um segundo eixo de decisão, tão importante quanto esses fatores operacionais: o **tipo genético do depósito mineral** determina uma geometria característica — e certas geometrias se prestam muito melhor a um fluxo de trabalho do que a outro, independentemente de quão bem a equipe execute qualquer um dos dois. Esta aula percorre quatro famílias geométricas amplas, cada uma associada a classes de depósito reconhecidas pela geologia econômica, e discute a estratégia de modelagem que cada uma favorece.

Guarde desde já a pergunta que vai reaparecer ao fim de cada família, porque é ela que organiza a aula inteira: **o limite entre minério e encaixante é uma superfície física real, ou é uma convenção de teor de corte?** A resposta muda o algoritmo.

### Depósitos vetoriais e tabulares estreitos: veios e zonas de cisalhamento mineralizadas

Depósitos hospedados em **veios** (preenchimento de fratura por precipitação hidrotermal) e em **zonas de cisalhamento mineralizadas** — típicos de depósitos de ouro orogênico (*orogenic gold*) — têm geometria caracteristicamente **tabular estreita e alongada**, com espessura de poucos metros a poucas dezenas de metros, mas continuidade que pode se estender por centenas de metros a poucos quilômetros ao longo do rumo e do mergulho, frequentemente com sinuosidade e variação local de espessura ("inchamentos e estrangulamentos" ao longo do corpo) controlada pela estrutura hospedeira.

Essa geometria favorece fortemente a **modelagem explícita**, pela mesma razão já discutida no exemplo trabalhado da Aula 01: um corpo estreito e sinuoso, cuja continuidade é controlada por um elemento estrutural específico (a própria zona de cisalhamento ou a fratura), se beneficia do julgamento geológico caso a caso do geólogo — que conhece o controle estrutural — mais do que de uma interpolação automática genérica, que tende a suavizar a sinuosidade real do corpo. O espaçamento de furos costuma ser relativamente apertado ao longo do rumo (para capturar a variação de espessura), com seções verticais perpendiculares à direção do veio.

*Limite entre minério e encaixante:* **superfície física real** (a parede do veio).

### Depósitos disseminados e em stockwork: pórfiros

Depósitos do tipo **pórfiro** (cobre porfirítico, molibdênio porfirítico, muitas vezes com ouro associado) têm geometria fundamentalmente diferente: a mineralização não ocupa uma estrutura discreta, mas se distribui de forma **disseminada** e em **stockwork** (uma malha densa de vênulas de quartzo mineralizadas, cada uma individualmente sem continuidade própria) dentro de um grande volume de rocha alterada hidrotermalmente, tipicamente em torno de um corpo intrusivo. A forma do corpo de minério acompanha, em primeiro lugar, a forma da intrusão hospedeira: como Sillitoe (2010) observa, *stocks* cilíndricos tendem a hospedar corpos de minério cilíndricos, e os *stocks* e enxames de diques que organizam esses sistemas são **verticalmente alongados**, com mais de 3 km de extensão vertical. Em planta, o corpo é aproximadamente equidimensional, com dimensões de centenas de metros a poucos quilômetros de diâmetro; em seção, o que se vê com frequência é um **casco de minério** em forma de sino ou de taça invertida, encapando um núcleo interno de teor mais baixo. O erro a evitar é ler "aproximadamente equidimensional em planta" como "equidimensional em três dimensões": o alongamento vertical é justamente o que torna o modelo 3D necessário, e é o que aparece no exemplo trabalhado adiante (600 m de diâmetro contra 1.000 m de profundidade).

Essa geometria favorece a **modelagem implícita**, porque o limite econômico do corpo não é definido por um contato litológico nítido, mas por um **envelope de teor** (a superfície que separa rocha acima do teor de corte da rocha abaixo dele) — um limite que, por definição, é gradual e não corresponde a nenhuma superfície geológica discreta que um geólogo possa traçar diretamente em seção. A modelagem por teor (frequentemente chamada de modelagem por **domínio de teor** ou por **superfície de alteração**, usando os halos de alteração hidrotermal característicos de pórfiros como domínio geométrico auxiliar) se beneficia diretamente da interpolação automática sobre a grade densa de furos verticais/subverticais tipicamente usada nesse tipo de depósito.

**Uma ressalva sobre o zoneamento de alteração, porque ela muda o que se modela.** O modelo que circula mais — herdado de Lowell e Guilbert (1970) — descreve halos **concêntricos em planta**: potássica no núcleo, depois fílica, argílica e propilítica em direção às bordas. Sillitoe (2010), a síntese de referência hoje, descreve o zoneamento de outra forma: a sequência principal é **empilhada verticalmente**, de baixo para cima — sódico-cálcica, potássica, clorita-sericita, sericítica e argílica avançada —, e a **propilítica** é **distal e profunda**, enquanto a argílica avançada forma um *lithocap* raso que pode passar de 1 km de espessura. Em sistemas telescopados, os tipos rasos se sobrepõem aos profundos. A diferença é prática, não acadêmica: quem monta domínios de alteração assumindo anéis concêntricos em planta vai interpolar superfícies com a orientação errada num sistema cujo zoneamento real é sobretudo vertical.

*Limite entre minério e encaixante:* **convenção de teor de corte**, sem superfície física correspondente.

### Depósitos estratiformes e estratabound: sedimentares e vulcanogênicos

Dois termos que este curso usa com sentidos distintos, e que convém não trocar. **Estratiforme** significa concordante com o acamamento — o corpo mineralizado é, ele próprio, uma camada. É o caso de muitos depósitos sedimentares de cobre (Kupferschiefer, Cinturão do Cobre da Zâmbia). **Estratabound** significa confinado a uma unidade estratigráfica específica, sem que o corpo precise ser concordante dentro dela. Os depósitos de chumbo-zinco tipo **Mississippi Valley (MVT)** são o exemplo clássico da segunda categoria e **não** da primeira: são estratabound em escala de distrito, mas em escala de depósito são tipicamente **discordantes**, hospedados em brechas de colapso, cavidades de dissolução e corpos que cortam dezenas de metros da sucessão carbonática. Os sulfetos maciços vulcanogênicos (**VMS**) também são estratabound: a lente maciça é aproximadamente concordante, mas a zona de *stockwork* alimentadora que a sustenta por baixo é francamente discordante.

O que une essas classes, apesar da diferença, é que a geometria é controlada primariamente pela **estratigrafia** — o corpo mineralizado se aloja em uma ou mais camadas ou horizontes dentro de uma sequência sedimentar ou vulcano-sedimentar, e é a geometria dessa sequência que dá o arcabouço do modelo.

Essa geometria favorece um fluxo **híbrido**: a estratigrafia regional (as superfícies limitantes da unidade hospedeira) costuma ser modelada de forma implícita, a partir dos mesmos dados de contato de furo e de atitude usados em qualquer sequência estratigráfica; mas a variação interna de espessura e de teor dentro dessa unidade hospedeira (por exemplo, o espessamento local de um horizonte de sulfeto maciço vulcanogênico numa bacia sin-vulcânica) costuma exigir revisão explícita local, porque reflete controle paleogeográfico (topografia do fundo marinho na época da deposição) que um algoritmo de interpolação genérico não tem como inferir sem dado estrutural adicional específico daquela geometria paleoambiental.

*Limite entre minério e encaixante:* **superfície física real** no arcabouço (os contatos da unidade hospedeira), mas **gradual** na variação interna de teor — daí o fluxo híbrido.

### Depósitos maciços e em pipe: magmáticos e de brecha

Um quarto grupo geométrico compreende corpos aproximadamente **equidimensionais** ou em **pipe** (chaminé subvertical). Entram aqui os depósitos magmáticos de **níquel-cobre-EGP** (elementos do grupo da platina) de **conduto** — hospedados em condutos magmáticos, os chamados *chonolitos*, ou em diques em lâmina, como Noril'sk, Voisey's Bay e Jinchuan — e os depósitos **de contato basal**, alojados em embaiamentos e calhas na base de intrusões máficas-ultramáficas. Entram também os depósitos de brecha hidrotermal ou de diatrema, incluindo, num extremo bem diferente de composição, as chaminés kimberlíticas diamantíferas. A geometria em pipe tem continuidade vertical pronunciada e seção transversal relativamente compacta, muitas vezes com contatos abruptos e bem definidos entre o corpo mineralizado e o encaixante.

**O que não entra aqui, apesar de também ser "Ni-Cu-EGP magmático":** os depósitos de **recife** (*reef*) de EGP das intrusões acamadadas — Merensky e UG2 no Bushveld, J-M no Stillwater — têm geometria oposta à desta família. São corpos **estratiformes**, com espessura de centímetros a poucos metros, rastreáveis lateralmente por dezenas a centenas de quilômetros ao longo da intrusão. Pertencem, do ponto de vista da estratégia de modelagem, à família estratiforme da seção anterior, e são modelados como superfícies estratigráficas, não como sólidos compactos. A classe genética "magmática" não determina a geometria sozinha; o mecanismo de alojamento (conduto, contato basal ou recife) é que determina.

Contatos abruptos e bem definidos — ao contrário do envelope de teor gradual do pórfiro — favorecem novamente a **modelagem explícita** de alta qualidade (o contato é fisicamente nítido e vale a pena o geólogo traçá-lo com cuidado), mas a geometria compacta e regular do pipe também se presta bem à modelagem implícita quando o volume de furos é grande o suficiente, porque o contato nítido produz um sinal forte (contraste de valor de interface bem definido) para o algoritmo de interpolação — ao contrário do pórfiro, em que o "contato" é uma convenção de teor de corte, não uma superfície física real.

*Limite entre minério e encaixante:* **superfície física real e abrupta.**

### Síntese: geometria como critério de decisão

A tabela conceitual que emerge das quatro famílias é a seguinte relação entre geometria e estratégia dominante — sempre lembrando, como a Aula 01 já ressalvou, que a prática real frequentemente combina as duas abordagens:

| Geometria | Exemplos de tipo de depósito | Limite minério/encaixante | Estratégia favorecida |
|---|---|---|---|
| Tabular estreita e sinuosa, controle estrutural discreto | Veios de ouro orogênico, zonas de cisalhamento mineralizadas | Físico e nítido | Explícita |
| Equidimensional em planta mas verticalmente alongada, envelope de teor gradual | Pórfiros de Cu-Mo(-Au) | Convenção de teor de corte | Implícita (domínio de teor/alteração) |
| Controlada por estratigrafia (estratiforme ou estratabound), com variação paleoambiental interna | VMS, Cu sedimentar, Pb-Zn tipo Mississippi Valley, recifes de EGP de intrusões acamadadas | Físico no arcabouço, gradual no interior | Híbrida (estratigrafia implícita, detalhe interno explícito) |
| Equidimensional a pipe, contatos abruptos | Ni-Cu-EGP de conduto e de contato basal, brecha/diatrema, kimberlito | Físico e abrupto | Explícita ou implícita de alta qualidade, conforme densidade de furo |

O critério que atravessa as quatro linhas não é "qual algoritmo é melhor", mas **a natureza física do limite entre mineralização e encaixante**: um limite estrutural discreto favorece o traço manual guiado por julgamento estrutural; um limite definido por teor de corte (sem superfície física correspondente) favorece a interpolação automática de uma grade contínua de valores.

Repare que a coluna do limite prevê a coluna da estratégia melhor do que a classe genética prevê: dois depósitos "magmáticos" podem cair em linhas diferentes da tabela, e dois depósitos de classes genéticas distintas (um veio e um pipe de brecha) caem na mesma linha porque compartilham o tipo de limite. É isso que significa dizer que a geometria, e não a gênese, dita a estratégia.

## Exemplo trabalhado

**Situação:** uma empresa de exploração tem dois alvos na mesma região: Alvo A, um veio de ouro orogênico com 25 furos de sondagem definindo uma espessura média de 3 m e continuidade ao longo de 800 m de rumo; Alvo B, um pórfiro de cobre com 60 furos verticais definindo um envelope de teor aproximadamente cônico de 600 m de diâmetro na superfície, afunilando a 1.000 m de profundidade.

**Pergunta:** para cada alvo, qual estratégia de modelagem (explícita, implícita, ou híbrida) é mais indicada, e que atributo geométrico de cada depósito justifica a escolha?

**Resolução:** para o **Alvo A** (veio de ouro orogênico), a estratégia mais indicada é a **explícita**, dominante ou pelo menos como revisão obrigatória de qualquer esqueleto implícito inicial: a espessura estreita (3 m) e o controle estrutural discreto de um veio significam que o contato mineralização-encaixante é uma superfície física real, e a continuidade sinuosa ao longo de 800 m de rumo é exatamente o tipo de geometria que se beneficia do julgamento geológico seção a seção, como discutido na seção sobre depósitos vetoriais acima — uma interpolação implícita genérica correria o risco de suavizar variações reais de espessura e de posição que o geólogo, guiado pelo controle estrutural conhecido, capturaria com mais fidelidade.

Para o **Alvo B** (pórfiro de cobre), a estratégia mais indicada é a **implícita**, com o domínio definido por envelope de teor de corte (e, complementarmente, por halos de alteração hidrotermal): o limite do corpo mineralizável não corresponde a nenhum contato litológico físico nítido, mas a uma convenção de teor de corte aplicada sobre uma distribuição gradual — exatamente a situação em que a interpolação automática de uma grade de teor (ou de um campo potencial calculado sobre a variável de teor transformada) é mais apropriada do que tentar traçar manualmente, seção a seção, um "contato" que fisicamente não existe como superfície discreta. A densidade de 60 furos verticais também favorece um algoritmo de interpolação bem restringido, algo que 25 furos ao longo de um veio linear estreito não oferecem da mesma forma para um volume de 600 m de diâmetro que desce até 1.000 m — equidimensional em planta, mas verticalmente alongado, como a seção sobre pórfiros ressalvou.

Note que a justificativa, nos dois casos, passou pela **coluna do limite** da tabela de síntese, e não pela classe genética do depósito — é esse o hábito de raciocínio que a aula quer instalar.

## Recap relâmpago

- A pergunta que organiza a aula inteira é **"o limite entre minério e encaixante é uma superfície física real ou uma convenção de teor de corte?"** — ela prevê a estratégia de modelagem melhor do que a classe genética do depósito prevê.
- Depósitos **vetoriais e tabulares estreitos** (veios de ouro orogênico, zonas de cisalhamento mineralizadas) têm geometria sinuosa com controle estrutural discreto e limite físico nítido, favorecendo a **modelagem explícita**.
- Depósitos **disseminados e em stockwork** (pórfiros de Cu-Mo-Au) acompanham a forma da intrusão hospedeira: equidimensionais em planta mas **verticalmente alongados**, limitados por um envelope de teor de corte gradual (não uma superfície física discreta), o que favorece a **modelagem implícita** por domínio de teor ou de alteração. O zoneamento de alteração que serve de domínio auxiliar é, segundo Sillitoe (2010), **sobretudo vertical** (sódico-cálcica, potássica, clorita-sericita, sericítica, argílica avançada de baixo para cima, com propilítica distal), não o anel concêntrico em planta do modelo clássico de Lowell e Guilbert (1970).
- Depósitos **controlados pela estratigrafia** favorecem um fluxo **híbrido** (estratigrafia regional implícita, detalhe paleoambiental interno revisado explicitamente) — e aqui cabe distinguir **estratiforme** (o corpo é uma camada: Cu sedimentar, recifes de EGP como o Merensky e o J-M) de **estratabound** (confinado a uma unidade, mas discordante dentro dela: MVT, hospedado em brechas de colapso e dissolução; VMS, com sua zona de *stockwork* alimentadora discordante).
- Depósitos **maciços e em pipe** (Ni-Cu-EGP **de conduto e de contato basal**, brecha/diatrema, kimberlito) têm contatos abruptos e bem definidos, aceitando bem tanto modelagem explícita de alta qualidade quanto implícita, dependendo da densidade de furo disponível. Note que a classe genética não fixa a geometria: Ni-Cu-EGP de conduto é pipe, Ni-Cu-EGP de recife é estratiforme.

## Anterior

[[22-modelagem-geologica-3d-aula-03-atributos-geologicos-geofisicos-inversao|Aula 03 — Atributos geológicos, estruturais, geoquímicos e geofísicos no modelo; modelos geofísicos de inversão e modelos geológicos]].

## Próxima aula

[[22-modelagem-geologica-3d-aula-05-modelo-3d-teste-interpretacao-metalogenetica|Aula 05 — O modelo 3D como ferramenta de teste da interpretação metalogenética]] — a Parte 2 deste par: com a geometria já construída pela estratégia escolhida aqui, como usar o modelo para testar a hipótese sobre a formação do depósito e para gerar alvos novos.

## Fontes

- Robb, L. (2005), *Introduction to Ore-Forming Processes*, Blackwell Publishing, capítulos sobre depósitos orogênicos de ouro, pórfiros de cobre, VMS e depósitos magmáticos de Ni-Cu-EGP (geometrias características de cada classe genética).
- Sillitoe, R. H. (2010), "Porphyry copper systems", *Economic Geology*, 105(1), 3-41 (forma do corpo de minério controlada pela forma do *stock* hospedeiro, alongamento vertical >3 km do sistema, zoneamento de alteração empilhado verticalmente — sódico-cálcica, potássica, clorita-sericita, sericítica, argílica avançada, com propilítica distal — *lithocap* argílico avançado e telescopagem).
- Lowell, J. D. & Guilbert, J. M. (1970), "Lateral and vertical alteration-mineralization zoning in porphyry ore deposits", *Economic Geology*, 65(4), 373-408 (o modelo clássico de halos coaxiais potássica → fílica → argílica → propilítica, apresentado aqui como o modelo histórico que Sillitoe 2010 reformula, não como a descrição vigente).
- Groves, D. I., Goldfarb, R. J., Gebre-Mariam, M., Hagemann, S. G. & Robert, F. (1998), "Orogenic gold deposits: A proposed classification in the context of their crustal distribution and relationship to other gold deposit types", *Ore Geology Reviews*, 13(1-5), 7-27 (geometria vetorial/tabular e controle estrutural de veios de ouro orogênico).
- Leach, D. L. & Sangster, D. F. (1993), "Mississippi Valley-type lead-zinc deposits", em Kirkham, R. V. et al. (eds.), *Mineral Deposit Modeling*, Geological Association of Canada Special Paper 40, 289-314 (caráter estratabound em escala de distrito e discordante em escala de depósito; hospedeiro em brechas de colapso e cavidades de dissolução).
- Naldrett, A. J. (2004), *Magmatic Sulfide Deposits: Geology, Geochemistry and Exploration*, Springer (distinção geométrica entre depósitos de Ni-Cu-EGP de conduto/contato basal e depósitos de recife estratiformes de intrusões acamadadas).

<!--
nivel: avancado
palavras_corpo: 2130
mapa_objetivo_secao:
  geologia-avancado-m22-oa03: "Por que a geometria do depósito dita a estratégia de modelagem" + "Depósitos vetoriais e tabulares estreitos: veios e zonas de cisalhamento mineralizadas" + "Depósitos disseminados e em stockwork: pórfiros" + "Depósitos estratiformes e estratabound: sedimentares e vulcanogênicos" + "Depósitos maciços e em pipe: magmáticos e de brecha" + "Síntese: geometria como critério de decisão" + "Exemplo trabalhado"

nota_divisao_didatica: |
  Esta aula e a Aula 05 resultam da divisao da antiga Aula 04 unica ('Tipos, tamanhos e
  geometrias de depositos minerais e a aplicacao de modelos 3D em metalogenese',
  2.764 palavras / ~33 min apos a auditoria cientifica de 2026-09-19), pela revisao
  didatica de 2026-09-19, achado DID-M22-A04-CARGA-001. O corte separa os dois usos
  distintos do modelo que o objetivo oa03 ja declarava em duas metades: a ESCOLHA DE
  ESTRATEGIA A PARTIR DA GEOMETRIA (esta aula) e o MODELO COMO TESTE DA INTERPRETACAO
  METALOGENETICA (Aula 05). Nenhuma correcao da auditoria cientifica de 2026-09-19 foi
  desfeita, diluida ou reformulada. Os claim_id NAO foram renumerados: o prefixo A04
  designa a numeracao em que cada alegacao foi emitida.

alegacoes_auditaveis:
  - claim_id: GEOMOD3D-M22-A04-GEOMETRIAVEIOS-001
    claim: "Depositos de ouro orogenico e outras mineralizacoes hospedadas em veios ou zonas de cisalhamento tem geometria tipicamente tabular estreita e alongada (espessura de poucos a poucas dezenas de metros, continuidade de centenas de metros a poucos quilometros ao longo do rumo/mergulho), com sinuosidade e variacao local de espessura controladas pela estrutura hospedeira, o que favorece modelagem explicita guiada por julgamento geologico do controle estrutural."
    risk: fato
    source: "Groves, Goldfarb, Gebre-Mariam, Hagemann & Robert (1998), 'Orogenic gold deposits: A proposed classification...', Ore Geology Reviews, 13(1-5), 7-27; Robb (2005), Introduction to Ore-Forming Processes, Blackwell, capítulo sobre depósitos orogênicos de ouro."
  - claim_id: GEOMOD3D-M22-A04-GEOMETRIAPORFIRO-002
    claim: "Depositos porfiriticos de cobre (Cu-Mo-Au) tem mineralizacao disseminada e em stockwork distribuida em torno de uma intrusao, com a forma do corpo de minerio controlada em primeiro lugar pela forma do stock hospedeiro (stocks cilindricos hospedam corpos cilindricos). O sistema e VERTICALMENTE ALONGADO — os stocks e enxames de diques que o organizam excedem 3 km de extensao vertical —, sendo aproximadamente equidimensional em PLANTA (centenas de metros a poucos quilometros de diametro) e nao em tres dimensoes; em secao, o casco de minerio aparece com frequencia em forma de sino ou taca invertida encapando um nucleo de teor mais baixo. O limite economico e definido por um envelope de teor de corte gradual, nao por um contato litologico fisico discreto."
    risk: fato
    source: "Sillitoe, R. H. (2010), 'Porphyry copper systems', Economic Geology, 105(1), 3-41 ('vertically elongate (>3 km) stocks or dike swarms'; 'ore-zone geometries depend mainly on the overall form of the host stock or dike complex, with cylindrical stocks typically hosting cylindrical orebodies')."
  - claim_id: GEOMOD3D-M22-A04-ZONEAMENTOPORFIRO-005
    claim: "O zoneamento de alteracao hidrotermal de sistemas porfiriticos NAO e adequadamente descrito como um conjunto de aneis concentricos em planta (potassica no nucleo, depois filica, argilica e propilitica para fora). Esse e o modelo classico de Lowell e Guilbert (1970), construido sobre San Manuel-Kalamazoo. A sintese de referencia atual (Sillitoe, 2010) descreve a sequencia principal como EMPILHADA VERTICALMENTE, de baixo para cima: sodico-calcica, potassica, clorita-sericita, sericitica e argilica avancada, com a propilitica desenvolvida DISTALMENTE em niveis profundos e a cloritica distalmente em niveis rasos; a argilica avancada forma um lithocap raso que pode exceder 1 km de espessura, e em sistemas telescopados os tipos rasos se sobrepoem aos profundos. A consequencia pratica para modelagem 3D e que dominios de alteracao construidos como aneis concentricos em planta orientam mal as superficies interpoladas."
    risk: fato
    source: "Sillitoe, R. H. (2010), 'Porphyry copper systems', Economic Geology, 105(1), 3-41 (sequencia 'centrally from the bottom upward, several of sodic-calcic, potassic, chlorite-sericite, sericitic, and advanced argillic zones. Chloritic and propylitic alteration develop distally at shallow and deeper levels, respectively'); Lowell, J. D. & Guilbert, J. M. (1970), 'Lateral and vertical alteration-mineralization zoning in porphyry ore deposits', Economic Geology, 65(4), 373-408 (o modelo coaxial classico, citado como referencia historica)."
  - claim_id: GEOMOD3D-M22-A04-GEOMETRIAESTRATIFORME-003
    claim: "ESTRATIFORME significa concordante com o acamamento (o corpo e, ele proprio, uma camada): e o caso de muitos depositos sedimentares de cobre, como o Kupferschiefer e o Cinturao do Cobre da Zambia. ESTRATABOUND significa confinado a uma unidade estratigrafica especifica sem que o corpo precise ser concordante dentro dela. Os depositos de Pb-Zn tipo Mississippi Valley (MVT) sao ESTRATABOUND, NAO estratiformes: sao estratabound em escala de distrito mas DISCORDANTES em escala de deposito, hospedados em brechas de colapso, cavidades de dissolucao e corpos que cortam dezenas de metros da sucessao carbonatica. Os sulfetos maciços vulcanogenicos (VMS) tambem sao estratabound: a lente maciça e aproximadamente concordante, mas a zona de stockwork alimentadora e francamente discordante. As duas classes compartilham o controle primario da geometria pela estratigrafia hospedeira, com variacao interna de espessura frequentemente refletindo controle paleogeografico (topografia do fundo marinho na epoca da deposicao, para VMS)."
    risk: fato
    source: "Leach, D. L. & Sangster, D. F. (1993), 'Mississippi Valley-type lead-zinc deposits', em Kirkham, Sinclair, Thorpe & Duke (eds.), Mineral Deposit Modeling, Geological Association of Canada Special Paper 40, 289-314 ('deposits are discordant on a deposit scale but stratabound on a district scale'; hospedeiro em brechas de dolomito e brechas de colapso); Robb (2005), Introduction to Ore-Forming Processes, Blackwell, capitulos sobre depositos sedimentares de cobre, Pb-Zn tipo MVT e VMS."
  - claim_id: GEOMOD3D-M22-A04-NICUEGPGEOMETRIA-006
    claim: "A classe genetica 'magmatica' nao determina sozinha a geometria de um deposito de Ni-Cu-EGP: o mecanismo de alojamento determina. Depositos de CONDUTO (hospedados em chonolitos ou diques em lamina — Noril'sk, Voisey's Bay, Jinchuan) e de CONTATO BASAL (embaiamentos e calhas na base de intrusoes maficas-ultramaficas) tem geometria equidimensional a pipe, com continuidade vertical pronunciada e contatos abruptos. Ja os depositos de RECIFE (reef) de EGP de intrusoes acamadadas — Merensky e UG2 no Bushveld, J-M no Stillwater — sao ESTRATIFORMES, com espessura de centimetros a poucos metros e continuidade lateral de dezenas a centenas de quilometros ao longo da intrusao, pertencendo a familia estratiforme para efeito de estrategia de modelagem."
    risk: fato
    source: "Naldrett, A. J. (2004), Magmatic Sulfide Deposits: Geology, Geochemistry and Exploration, Springer Berlin Heidelberg, DOI 10.1007/978-3-662-08444-1 (tipologia geometrica dos depositos de sulfeto magmatico); Zientek, M. L. (2012), 'Magmatic ore deposits in layered intrusions — Descriptive model for reef-type PGE and contact-type Cu-Ni-PGE deposits', U.S. Geological Survey Open-File Report 2012-1010 (reef 'laterally persistent along strike... tens to hundreds of kilometers', intervalo mineralizado 'centimeters to meters thick'; J-M reef 1 a 8 m de espessura, rastreado por 40 km)."
-->
