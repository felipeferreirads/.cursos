# Aula 04: Condutividade elétrica das rochas e a relação integrada entre as propriedades físicas

**ID:** geologia-avancado-m15-a04
**Módulo:** [[15-petrofisica-modulo|Módulo 15 — Introdução à petrofísica]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** aplicar a lei de Archie para relacionar condutividade (ou resistividade) elétrica, porosidade e saturação de água numa rocha, e integrar as propriedades físicas vistas no módulo no conjunto de contrastes que a geofísica aplicada explora.
**Ao final você vai conseguir:** explicar por que a maioria dos minerais formadores de rocha é isolante e por que, mesmo assim, rochas conduzem eletricidade; aplicar a lei de Archie para calcular saturação de água a partir de resistividade medida; explicar o papel do fator de formação e dos expoentes de cimentação e de saturação; e montar o quadro-síntese que liga cada propriedade física estudada neste módulo ao método geofísico que a explora.
**Pré-requisito:** [[15-petrofisica-aula-01-meios-porosos-porosidade-permeabilidade-controles-geologicos|Aula 01]] para a primeira metade (porosidade e permeabilidade reaparecem como os controles centrais da condutividade elétrica de uma rocha porosa) — mas a **segunda metade desta aula, que integra o módulo, depende das Aulas 02 e 03 por inteiro**: a tabela de fechamento cruza densidade e velocidade sísmica (Aula 02) com magnetismo e radioatividade (Aula 03). Esta é a única aula do módulo que reativa todas as anteriores; não pule direto para ela.

## Conteúdo

### Por que uma rocha conduz eletricidade, se seus minerais não conduzem

Ao contrário do magnetismo e da radioatividade, cuja fonte é mineral, a condutividade elétrica da grande maioria das rochas sedimentares comuns **não vem da matriz mineral**. Quartzo, calcita, feldspato e a maioria dos silicatos são isolantes elétricos (condutividade extremamente baixa, ou, de forma equivalente, resistividade extremamente alta) — um grão de quartzo seco praticamente não conduz corrente elétrica. O que conduz, na esmagadora maioria das rochas sedimentares porosas, é a **água que preenche os poros**, e especificamente os **íons dissolvidos** nela (sódio, cloreto, cálcio, entre outros, provenientes da salinidade da água de formação). Uma rocha porosa e permeável, saturada com salmoura, conduz corrente eletrolítica através da rede de poros interconectados — o mesmo caminho que, na Aula 01, foi identificado como responsável pelo fluxo de fluido.

Essa origem elétrica explica a ligação direta entre esta aula e a primeira do módulo: a condutividade elétrica de uma rocha porosa depende essencialmente de três coisas — **quanta água há** (porosidade e saturação), **quão bem conectada** está essa água (a mesma geometria de poro e garganta que controla a permeabilidade) e **quão salgada** (condutiva) é essa água. Rochas ígneas e metamórficas cristalinas, com porosidade primária próxima de zero, são tipicamente muito resistivas (pouco condutoras), exceto ao longo de zonas de fratura saturadas ou de minerais condutores específicos, como sulfetos metálicos maciços ou grafita — casos em que a condução deixa de ser eletrolítica (pelo fluido) e passa a ser eletrônica (pelo próprio mineral), um mecanismo à parte que a eletrorresistividade e a polarização induzida, tratadas em módulos de geofísica adiante, exploram especificamente.

Existe uma exceção importante à regra "só o fluido conduz": rochas ricas em **argila** conduzem corrente elétrica também pela superfície dos próprios argilominerais (a chamada **condutividade de superfície**, associada à dupla camada elétrica na interface entre o argilomineral carregado e a água adjacente), um efeito adicional que a lei de Archie clássica, apresentada a seguir, não contempla — e que exige correções específicas (como o modelo de Waxman-Smits) em rochas argilosas, mencionadas aqui apenas para que a limitação fique registrada, sem desenvolvê-las nesta aula introdutória.

### A lei de Archie: a relação central da petrofísica de reservatório

Em 1942, o engenheiro Gus Archie publicou uma relação empírica, obtida a partir de medições em arenitos limpos (sem argila significativa), que se tornou a equação mais usada da petrofísica de poço e permanece o ponto de partida de praticamente qualquer interpretação quantitativa de resistividade até hoje. A lei de Archie tem duas partes.

A primeira relaciona a resistividade de uma rocha **100% saturada de água** (R₀) à resistividade da própria água de formação (Rw) através do **fator de formação** (F):

F = R₀ / Rw = a / φ^m

onde φ é a porosidade, **a** é uma constante empírica e **m** é o **expoente de cimentação**. Aqui mora a primeira armadilha: **a e m não são dois botões independentes**. Eles vêm em pares calibrados sobre um mesmo conjunto de amostras, e trocar um sem o outro produz um fator de formação simplesmente errado, não uma média prudente. A forma dita "de Archie" usa a = 1 com m entre 1,8 e 2,0; a **fórmula de Humble** (Winsauer et al., 1952) usa a = 0,62 **acompanhado de m = 2,15**, e a variante para areias inconsolidadas usa a = 0,65, também com m = 2,15. Combinar o a de um par com o m de outro — por exemplo a = 0,62 com m = 2 — é um erro comum e silencioso, porque o resultado continua parecendo plausível.

Voltando ao significado de **m**, ele é o **expoente de cimentação** — que, apesar do nome, reflete não só a cimentação diagenética, mas de forma mais geral a **tortuosidade** do caminho que a corrente elétrica precisa percorrer através da rede de poros: quanto mais tortuoso e mal conectado o caminho, maior m, e maior a resistividade para uma dada porosidade. Para arenitos limpos, m situa-se tipicamente entre 1,8 e 2,0, estendendo-se a cerca de 2,2 em arenitos consolidados em geral (a faixa que o Módulo 12 usa); rochas com poros mais tortuosos ou fraturados podem ter m mais alto ou mais baixo, respectivamente, e o valor apropriado costuma ser calibrado com medições de laboratório em amostras de testemunho, não simplesmente assumido.

A segunda parte relaciona a resistividade real da rocha (Rt), quando ela não está 100% saturada de água mas contém também hidrocarboneto (óleo ou gás, ambos isolantes elétricos, ao contrário da água salgada), à saturação de água (Sw, a fração do espaço poroso ocupada por água) através do **expoente de saturação** (n):

Rt / R₀ = 1 / Sw^n → Sw = (a × Rw / (φ^m × Rt))^(1/n) = (F × Rw / Rt)^(1/n)

O expoente n costuma ser tomado como 2 na ausência de calibração específica, e essa aproximação é razoável **enquanto a rocha for molhável por água** (*water-wet*) — que é a condição em que Archie mediu. **Molhabilidade** é a preferência da superfície mineral por um dos fluidos presentes: numa rocha *water-wet*, a água adere à parede do poro e o óleo fica no meio do espaço poroso; numa rocha *oil-wet*, é o contrário. A distinção parece detalhe de laboratório e não é — ela decide por onde a corrente elétrica consegue passar. A faixa deixa de ser estreita assim que a molhabilidade muda, e essa é a segunda armadilha da equação: medidas clássicas em testemunho (Sweeney & Jennings) dão n ≈ 1,6 em rocha molhável por água, ≈ 1,9 em molhabilidade neutra e ≈ **8** em rocha molhável por óleo (*oil-wet*), com valores acima de 10 em testemunhos uniformemente oil-wet a baixa saturação de salmoura. A razão física é direta e vale memorizar: numa rocha water-wet a água permanece como um **filme contínuo** na parede do poro e continua conduzindo mesmo quando há pouca água; numa rocha oil-wet ela se rompe em **gotas desconectadas**, e a condução despenca. Como boa parte dos carbonatos é de molhabilidade mista ou oil-wet, herdar n = 2 num reservatório carbonático não é uma imprecisão pequena — e erra para o lado perigoso, como o exemplo trabalhado a seguir vai quantificar. O ponto físico por trás da equação é intuitivo: como hidrocarboneto não conduz, substituir água por óleo ou gás no espaço poroso obriga a corrente elétrica a percorrer um caminho mais tortuoso através da água remanescente — e isso **aumenta** a resistividade medida (Rt) em relação à resistividade totalmente saturada de água (R₀). É exatamente essa elevação de resistividade, medida por uma ferramenta de perfilagem elétrica ou de indução descida no poço, que permite inferir a presença de hidrocarboneto sem nunca ver a rocha diretamente — a lógica central por trás da avaliação de formações em toda a indústria de petróleo desde a década de 1940.

### Integrando as propriedades físicas do módulo

Este módulo caracterizou sete propriedades físicas — porosidade, permeabilidade, densidade, propriedades elásticas (Vp/Vs), magnetismo, radioatividade e, agora, condutividade elétrica — não como uma lista solta, mas como a base de contraste que cada método geofísico principal explora. Vale fechar o módulo amarrando essa correspondência de forma explícita, porque é ela que justifica por que o curso segue, no Módulo 16, para a aerogeofísica:

| Propriedade física | O que a controla | Método geofísico que a explora |
|---|---|---|
| Densidade bulk | Composição mineral, porosidade, fluido de poro | Gravimetria (contraste de densidade entre corpos) |
| Magnetização total (induzida + remanente) | Teor de magnetita e de titanomagnetita — **não** de ilmenita, que é paramagnética em condições geológicas | Magnetometria (contraste de magnetização; a parcela remanente pode dominar a induzida, e a razão entre as duas — de Koenigsberger — é o que diz qual delas manda) |
| Radioatividade natural (K, U, Th) | Minerais-fonte de K, U e Th na rocha ou no solo residual | Gamaespectrometria (radiação emitida pela superfície, penetração de poucos cm a dm) |
| Velocidade sísmica (Vp, Vs) | Densidade, módulos elásticos, porosidade, fluido de poro | Sísmica de **reflexão** (contraste de impedância acústica = densidade × velocidade) e de **refração** (contraste de **velocidade** apenas — a refração crítica obedece à lei de Snell e é insensível à densidade) |
| Condutividade/resistividade elétrica | Porosidade, saturação e salinidade da água de poro, teor de argila | Eletrorresistividade, indução eletromagnética, polarização induzida |
| Permeabilidade | Tamanho de garganta de poro, conectividade | Não medida remotamente por geofísica de superfície; inferida indiretamente a partir de porosidade, litologia e testes de poço |

Uma observação amarra a tabela inteira, e vale dizê-la com a precisão que a própria tabela permite. **Três** dos cinco métodos listados — gravimetria, sísmica e eletrorresistividade/eletromagnetismo — dependem, em algum grau, da **mesma variável subjacente**: quanto poro existe e o que o preenche. Cada um a enxerga através de um mecanismo físico diferente e, por isso, com uma sensibilidade diferente a fatores de confusão. Os outros dois — magnetometria e gamaespectrometria — são **cegos** a essa variável por construção, e é exatamente essa cegueira que os torna complementares aos três primeiros, e não redundantes: o método que ignora a porosidade é o que resolve a ambiguidade do método que não a ignora. A gravimetria, por exemplo, não distingue diretamente se uma anomalia de densidade vem de mudança de litologia ou de mudança de porosidade; a magnetometria é cega a tudo que não seja magnetita e titanomagnetita, inclusive a mudanças de porosidade ou fluido; a gamaespectrometria só enxerga a superfície exposta ou solo residual raso, sendo cega a qualquer coisa em profundidade; e a resistividade sozinha não distingue rocha porosa com água doce de rocha menos porosa com água salgada, porque os dois efeitos podem produzir a mesma resistividade aparente — a ambiguidade citada no hub deste módulo como a "raiz da ambiguidade que aparece em todos os módulos de geofísica seguintes". É exatamente por essa razão que a prática da geofísica aplicada raramente confia num único método isolado: cada contraste físico resolve parte da ambiguidade que os outros deixam em aberto, e é esse raciocínio de integração multimétodo — não um método específico — que o Módulo 16 (aerogeofísica) começa a colocar em prática.

## Exemplo trabalhado

**Situação:** um arenito-reservatório tem porosidade φ = 22% (0,22), medida por perfil de densidade-nêutron. A água de formação da bacia tem resistividade Rw = 0,08 ohm·m a temperatura de formação. Uma ferramenta de resistividade profunda mede, na zona de interesse, Rt = 12 ohm·m. Assuma a = 1, m = 2 e n = 2 (valores-padrão de Archie para arenito limpo, na ausência de calibração de testemunho específica desta bacia).

**Pergunta:** calcule o fator de formação F, a resistividade da rocha 100% saturada de água R₀, e a saturação de água Sw da zona. A zona é candidata a reservatório de hidrocarboneto?

**Resolução:**

Fator de formação: F = a / φ^m = 1 / (0,22)² = 1 / 0,0484 ≈ **20,7**

Resistividade 100% saturada de água: R₀ = F × Rw = 20,7 × 0,08 ≈ **1,66 ohm·m**

Saturação de água: Sw = (F × Rw / Rt)^(1/n) = (20,7 × 0,08 / 12)^(1/2) = (1,656 / 12)^(1/2) = (0,138)^(1/2) ≈ **0,371 → 37,1%**

**Interpretação:** a resistividade medida (Rt = 12 ohm·m) é cerca de sete vezes maior que a resistividade que a mesma rocha teria se estivesse 100% saturada de água (R₀ ≈ 1,66 ohm·m) — um contraste grande demais para ser explicado por variação de porosidade ou de salinidade da água sozinhas, e coerente com uma saturação de água relativamente baixa (37%), o que implica uma **saturação de hidrocarboneto de 1 − Sw ≈ 63%**. Essa é exatamente a lógica de decisão que orienta a avaliação de formação em um poço exploratório: uma zona porosa com resistividade muito acima de R₀ é candidata a reservatório de óleo ou gás, e o valor de Sw calculado por Archie é o primeiro número que entra no cálculo do volume de hidrocarboneto in situ — ainda que, na prática de campo, sempre sujeito a calibração de a, m e n específica da formação e a correções (como a de argilosidade, mencionada na seção anterior) que uma rocha real, argilosa, exigiria e que este exemplo, deliberadamente, manteve de fora por tratar de um arenito limpo. Vale notar de passagem que, em arenito limpo, as duas porosidades da Aula 01 — total e efetiva — praticamente coincidem, e é por isso que Archie funciona aqui sem precisar qualificar de qual delas se trata; em rocha argilosa elas divergem, e escolher entre uma e outra passa a ser parte da correção de argilosidade.

**Quanto custa herdar n = 2 quando ele não vale.** Refaça a última conta trocando apenas o expoente de saturação, mantendo tudo o mais: com n = 2, Sw = 0,138^(1/2) = **37%**. Se a rocha fosse oil-wet, com n = 8, o mesmo dado de resistividade daria Sw = 0,138^(1/8) = **78%** — mais que o dobro, e a zona deixaria de ser candidata a reservatório. Repare na direção do erro: assumir n = 2 numa rocha oil-wet **subestima** a saturação de água e, portanto, **superestima** o hidrocarboneto. É o pior sentido possível para se errar numa decisão de perfurar, e é o motivo pelo qual n é calibrado em testemunho, não herdado de livro-texto.

## Erros comuns

- **Combinar a constante a de um par calibrado com o m de outro** (por exemplo a = 0,62 de Humble com m = 2 de Archie). A aula é explícita: a e m não são botões independentes — vêm calibrados juntos, e misturá-los produz um fator de formação errado que ainda assim parece plausível.
- **Herdar n = 2 sem verificar a molhabilidade da rocha.** Como o próprio exemplo trabalhado quantifica, presumir n = 2 numa rocha oil-wet (onde n real seria ~8) subestima drasticamente Sw e superestima o hidrocarboneto — o erro é na direção mais perigosa possível para uma decisão de perfurar.
- **Aplicar Archie clássica sem correção em rocha argilosa.** A condutividade de superfície dos argilominerais não é capturada pela equação original — ignorá-la em rochas com fração de argila relevante exige o modelo de Waxman-Smits, não a fórmula simples.
- **Interpretar resistividade alta como só hidrocarboneto, sem considerar salinidade da água.** A própria tabela de integração destaca essa ambiguidade: rocha porosa com água doce e rocha menos porosa com água salgada podem produzir a mesma resistividade aparente — é por isso que nenhum método geofísico isolado resolve essa questão sozinho.

## O que não concluir

- **Que m = "expoente de cimentação" mede só cimentação diagenética.** Reflete, de forma mais geral, a tortuosidade do caminho poroso — pode ser alto por fratura, baixo por conectividade excelente, sem qualquer relação direta com quanto cimento existe.
- **Que magnetometria e gamaespectrometria são métodos "incompletos" por serem cegos à porosidade.** É exatamente essa cegueira que os torna complementares aos métodos sensíveis a poro/fluido (gravimetria, sísmica, resistividade) — cada método resolve parte da ambiguidade que os outros deixam em aberto.
- **Que sísmica de reflexão e de refração exploram o mesmo contraste físico.** Reflexão depende de impedância acústica (densidade × velocidade); refração crítica depende só de velocidade, sendo insensível à densidade — confundir os dois leva a esperar o contraste errado de cada método.

## Recap relâmpago

- A maioria dos minerais formadores de rocha é eletricamente isolante; a condutividade de uma rocha porosa sedimentar comum vem, na prática, da água salgada (eletrólito) que preenche os poros interconectados — o mesmo caminho que controla a permeabilidade.
- Rochas cristalinas intactas são tipicamente muito resistivas, exceto ao longo de fraturas saturadas ou na presença de minerais condutores eletrônicos como sulfetos maciços e grafita — um mecanismo de condução diferente do eletrolítico.
- Argilominerais introduzem condutividade de superfície adicional, não capturada pela lei de Archie clássica, que exige correções específicas (Waxman-Smits) em rochas argilosas.
- Lei de Archie: fator de formação F = a/φ^m (m, expoente de cimentação/tortuosidade, tipicamente 1,8-2,0 em arenito limpo) relaciona R₀ (resistividade 100% saturada de água) a Rw (resistividade da água de formação); Sw = (F × Rw / Rt)^(1/n) (n, expoente de saturação) dá a saturação de água a partir da resistividade real medida (Rt).
- As duas armadilhas dos parâmetros de Archie: (1) **a e m vêm em pares calibrados** e nunca devem ser combinados entre si — a = 1 com m ≈ 1,8-2,0, ou Humble com a = 0,62 **e** m = 2,15; (2) **n ≈ 2 só vale em rocha molhável por água** — cai para ~1,6 em water-wet estrito, ~1,9 em molhabilidade neutra e sobe para ~8 (ou mais) em rocha oil-wet, porque o filme contínuo de água se rompe em gotas desconectadas. Herdar n = 2 numa rocha oil-wet subestima Sw e superestima o hidrocarboneto — erro na direção perigosa.
- Como hidrocarboneto não conduz, Rt maior que R₀ indica saturação de água menor que 100% — a base da avaliação quantitativa de formação por resistividade em poços de petróleo desde a década de 1940.
- As sete propriedades físicas do módulo (porosidade, permeabilidade, densidade, elasticidade sísmica, magnetismo, radioatividade e condutividade elétrica) correspondem cada uma a um método geofísico principal (gravimetria, magnetometria, gamaespectrometria, sísmica, eletrorresistividade/eletromagnetismo). Três desses métodos — gravimetria, sísmica e resistividade — compartilham a mesma ambiguidade de fundo: porosidade e fluido de poro afetando o sinal de formas que um único método não consegue separar sozinho. Os outros dois — magnetometria e gamaespectrometria — são cegos a essa variável, e é essa cegueira que os torna complementares; resolver a ambiguidade por integração multimétodo é o fio condutor dos módulos de geofísica que seguem.
- Reflexão e refração sísmicas não exploram o mesmo contraste: a **reflexão** depende do contraste de **impedância acústica** (densidade × velocidade), enquanto a **refração** crítica depende apenas do contraste de **velocidade**, sendo insensível à densidade.

## Próxima aula

Este é o fim do Módulo 15. O [[16-aerogeofisica/16-aerogeofisica-modulo|Módulo 16 — Introdução à aerogeofísica]] retoma diretamente a tabela de correspondências desta aula, tratando de como os contrastes de densidade, susceptibilidade magnética e radioatividade natural aqui caracterizados são efetivamente medidos, processados e interpretados a partir de levantamentos aerotransportados.

## Fontes

- Archie, G. E. (1942), "The Electrical Resistivity Log as an Aid in Determining Some Reservoir Characteristics", *Transactions of the AIME*, 146(1), 54-62 (publicação original da lei de Archie, definição de F, m e n).
- Winsauer, W. O., Shearin, H. M., Masson, P. H. & Williams, M. (1952), "Resistivity of brine-saturated sands in relation to pore geometry", *AAPG Bulletin*, 36(2) (fórmula de Humble: a = 0,62 com m = 2,15).
- Anderson, W. G. (1986), "Wettability Literature Survey — Part 3: The Effects of Wettability on the Electrical Properties of Porous Media", *Journal of Petroleum Technology*, 38(12), 1371-1378 (dependência do expoente de saturação n em relação à molhabilidade; dados de Sweeney & Jennings).
- Schön, J. H. (2015), *Physical Properties of Rocks: Fundamentals and Principles of Petrophysics*, 2ª ed., Elsevier, cap. 7-8 (condutividade elétrica de rochas, origem eletrolítica, condutividade de superfície de argilas, lei de Archie).
- Ellis, D. V. & Singer, J. M. (2007), *Well Logging for Earth Scientists*, 2ª ed., Springer, cap. 4 e 8 (avaliação de formação, resistividade, saturação de água, correção de argilosidade e modelo de Waxman-Smits).
- Telford, W. M., Geldart, L. P. & Sheriff, R. E. (1990), *Applied Geophysics*, 2ª ed., Cambridge University Press, cap. 1 e 8 (visão de conjunto das propriedades físicas exploradas por cada método geofísico).

<!--
nivel: avancado
palavras_corpo: 2367
mapa_objetivo_secao:
  geologia-avancado-m15-oa04: "Por que uma rocha conduz eletricidade, se seus minerais não conduzem" + "A lei de Archie: a relação central da petrofísica de reservatório" + "Integrando as quatro propriedades físicas do módulo" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: PETROFIS-M15-A04-ORIGEMCONDUTIVIDADE-001
    claim: "A maioria dos minerais formadores de rocha (quartzo, calcita, feldspato, silicatos comuns) é eletricamente isolante; a condutividade elétrica da maioria das rochas sedimentares porosas vem da água salgada (eletrólito, íons dissolvidos) que preenche os poros interconectados. Rochas cristalinas intactas sao tipicamente muito resistivas, exceto em fraturas saturadas ou na presença de minerais condutores eletrônicos (sulfetos maciços, grafita)."
    risk: fato
    source: "Schön 2015, Physical Properties of Rocks, cap. 7; Telford, Geldart & Sheriff 1990, Applied Geophysics, cap. 8"
  - claim_id: PETROFIS-M15-A04-CONDUTIVIDADESUPERFICIE-002
    claim: "Argilominerais introduzem condutividade elétrica de superfície adicional (associada à dupla camada elétrica na interface argilomineral-água), efeito não contemplado pela lei de Archie clássica e que exige correções especificas como o modelo de Waxman-Smits em rochas argilosas."
    risk: fato
    source: "Schön 2015, Physical Properties of Rocks, cap. 7-8; Ellis & Singer 2007, Well Logging for Earth Scientists, cap. 4 (modelo de Waxman-Smits para correção de argilosidade)"
  - claim_id: PETROFIS-M15-A04-ARCHIE-003
    claim: "Lei de Archie (Archie, 1942): fator de formação F = R0/Rw = a/phi^m; saturação de água Sw = (a x Rw / (phi^m x Rt))^(1/n) = (F x Rw/Rt)^(1/n). O expoente de cimentação/tortuosidade m fica tipicamente entre 1,8 e 2,0 em arenito limpo, sobe em poro tortuoso e cai em rocha fraturada."
    risk: fato
    source: "Archie 1942, Transactions of the AIME 146(1):54-62, publicação original; Ellis & Singer 2007, Well Logging for Earth Scientists, cap. 4"
  - claim_id: PETROFIS-M15-A04-ARCHIEAM-006
    claim: "a e m NÃO são parâmetros independentes: vêm em pares calibrados sobre um mesmo conjunto de amostras. Forma 'de Archie': a=1 com m entre 1,8 e 2,0. Fórmula de Humble (Winsauer et al., 1952): a=0,62 COM m=2,15. Variante para areias inconsolidadas: a=0,65, também com m=2,15. Combinar o a de um par com o m de outro (p.ex. a=0,62 com m=2) produz fator de formação errado."
    risk: fato
    source: "Winsauer et al. 1952 (fórmula de Humble); SEG Wiki, Dictionary: Archie's formulas; Ellis & Singer 2007, cap. 4. CORREÇÃO LARANJA da auditoria de 2026-09-08: a redação original apresentava a e m como escolhas independentes, listando 'a = 0,62 ou 0,65' sem o m=2,15 que os acompanha."
  - claim_id: PETROFIS-M15-A04-ARCHIEN-007
    claim: "O expoente de saturação n vale aproximadamente 2 apenas em rocha molhável por água (water-wet), condição em que Archie mediu. Medidas de Sweeney & Jennings dão n aprox. 1,6 (water-wet), aprox. 1,9 (molhabilidade neutra) e aprox. 8 (oil-wet), com n acima de 10 em testemunhos uniformemente oil-wet a baixa saturação de salmoura. Mecanismo: em rocha water-wet a água forma filme contínuo na parede do poro e segue conduzindo; em rocha oil-wet ela se rompe em gotas desconectadas. Consequência quantificada com os dados do próprio exemplo trabalhado: F x Rw/Rt = 0,138 dá Sw = 37% com n=2 e Sw = 78% com n=8 - assumir n=2 numa rocha oil-wet subestima Sw e superestima o hidrocarboneto."
    risk: fato
    source: "Sweeney & Jennings, dados de molhabilidade vs. expoente de saturação; Anderson, Wettability Literature Survey Part 3: Effects of Wettability on Electrical Properties of Porous Media, JPT 38(12):1371; Ellis & Singer 2007, cap. 4. CORREÇÃO LARANJA da auditoria de 2026-09-08: a redação original afirmava que n 'varia numa faixa relativamente estreita (2 +/- 0,5)', falso para a classe de rochas de molhabilidade mista ou oil-wet que o próprio módulo discute."
  - claim_id: PETROFIS-M15-A04-REFRACAO-008
    claim: "Sísmica de reflexão e de refração não exploram o mesmo contraste: a amplitude da reflexão é governada pelo contraste de IMPEDÂNCIA ACÚSTICA (R = (rho2.V2 - rho1.V1)/(rho2.V2 + rho1.V1)), enquanto a refração crítica obedece à lei de Snell e depende apenas do contraste de VELOCIDADE, sendo insensível à densidade."
    risk: fato
    source: "Telford, Geldart & Sheriff 1990, Applied Geophysics, cap. 4; US EPA, Seismic Reflection (definição do coeficiente de reflexão). CORREÇÃO LARANJA da auditoria de 2026-09-08: a tabela de integração agrupava 'sísmica de reflexão e refração' sob 'contraste de impedância acústica', atribuindo à refração um mecanismo que não é o dela."
  - claim_id: PETROFIS-M15-A04-HIDROCARBONETO-004
    claim: "Hidrocarboneto (óleo e gás) é eletricamente isolante; substituir água por hidrocarboneto no espaço poroso aumenta a resistividade medida (Rt) em relação à resistividade 100% saturada de água (R0), permitindo inferir presença de hidrocarboneto e calcular saturação de água por resistividade — base da avaliação de formação em poços de petróleo desde a década de 1940."
    risk: fato
    source: "Archie 1942, Transactions of the AIME 146(1); Ellis & Singer 2007, Well Logging for Earth Scientists, cap. 4 e 8"
  - claim_id: PETROFIS-M15-A04-INTEGRACAO-005
    claim: "Cada método geofísico principal explora um contraste físico distinto: gravimetria (densidade bulk), magnetometria (magnetização total = induzida + remanente, controlada por magnetita e titanomagnetita, NÃO por ilmenita), gamaespectrometria (radioatividade natural K-U-Th, penetração de poucos cm a dm), sísmica de reflexão (impedância acústica) e de refração (velocidade), e eletrorresistividade/eletromagnetismo/polarização induzida (condutividade elétrica). A permeabilidade não é medida diretamente por geofísica de superfície, apenas inferida indiretamente. TRÊS dos cinco métodos (gravimetria, sísmica, resistividade) dependem da mesma variável subjacente - porosidade e fluido de poro; os outros DOIS (magnetometria, gamaespectrometria) são cegos a ela por construção, e é essa cegueira que os torna complementares."
    risk: aproximacao
    source: "Telford, Geldart & Sheriff 1990, Applied Geophysics, cap. 1 (visão de conjunto de métodos geofísicos e a propriedade física que cada um explora); Clark 1997 (magnetização total e razão de Koenigsberger). Correções da auditoria de 2026-09-08: propagação do achado vermelho da ilmenita (Aula 03), separação de reflexão e refração, inclusão da magnetização remanente, e substituição de 'quase todo método' por contagem explícita de três contra dois."
-->
