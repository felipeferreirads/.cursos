# Aula 01: Meios porosos — porosidade, permeabilidade e seus controles geológicos

**ID:** geologia-avancado-m15-a01
**Módulo:** [[15-petrofisica-modulo|Módulo 15 — Introdução à petrofísica]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** definir porosidade e permeabilidade com rigor operacional, distinguir porosidade total de porosidade efetiva e explicar por que uma rocha porosa nem sempre é permeável.
**Ao final você vai conseguir:** calcular porosidade a partir de volumes de grão e de poro; distinguir porosidade total de porosidade efetiva e explicar quando essa diferença muda uma decisão de campo; situar valores típicos de porosidade e permeabilidade por litologia; e explicar, com base na geometria do poro, por que permeabilidade e porosidade não são a mesma grandeza nem variam sempre juntas.
**Pré-requisito:** nenhum específico deste módulo — pressupõe o vocabulário básico de textura sedimentar (seleção, arredondamento, empacotamento de grãos) e de diagênese (cimentação, compactação) do curso base de geologia.

## Conteúdo

### Por que a petrofísica abre esta área do curso

Este módulo muda de registro em relação aos anteriores: até aqui o curso tratou de água subterrânea, geomecânica, bacias, geoprocessamento e sensoriamento remoto como blocos relativamente independentes. A **petrofísica** — o estudo das propriedades físicas de rochas e minerais e de como essas propriedades se relacionam entre si — é o que amarra tudo isso à geofísica que vem a seguir (Módulos 16 a 19): todo método geofísico funciona porque duas rochas diferentes respondem de forma mensuravelmente diferente a algum campo físico, e é a petrofísica que diz **por que** essa diferença existe e **quanto** ela vale. Esta primeira aula trata da propriedade mais intuitiva e, ao mesmo tempo, mais mal-compreendida do grupo: a porosidade — e da propriedade que dela mais frequentemente se confunde, a permeabilidade.

### Porosidade: definição e o que ela não diz sozinha

**Porosidade** (símbolo usual φ, phi) é a fração do volume de uma rocha que corresponde a espaço vazio (poros), em relação ao volume total da rocha:

φ = V_poros / V_total

Expressa-se como fração (0 a 1) ou como percentual (0% a teoricamente próximo de 100%, embora rochas reais raramente superem 40-50%). É importante fixar que porosidade é uma razão de **volumes**, não de massa, e que ela nada diz, por si só, sobre o **tamanho, a forma ou a conectividade** dos poros — três atributos que, como a seção seguinte mostra, são decisivos para saber se aquele espaço vazio serve para alguma coisa.

Existem duas famílias principais de porosidade quanto à origem:

- **Porosidade primária** (ou deposicional): existe desde a formação da rocha, criada pelo espaço entre grãos durante a deposição (sedimentos clásticos) ou pela estrutura de crescimento do material (recifes de coral, por exemplo).
- **Porosidade secundária**: criada depois da rocha formada, por processos como dissolução (cavidades de dissolução em calcários — a porosidade cárstica é o caso extremo), fraturamento (porosidade de fratura, importante em rochas ígneas e metamórficas que praticamente não têm porosidade primária) ou dolomitização (a substituição mol a mol de calcita por dolomita reduz o volume do sólido em cerca de 13% — mas ver a ressalva logo abaixo).

**Ressalva sobre a dolomitização.** O número é estequiometria confirmada: dois mols de calcita ocupam cerca de 73,9 cm³ e um mol de dolomita ocupa cerca de 64,3 cm³, uma redução de aproximadamente 13% no volume do sólido. O que **não** é consenso é a conclusão de que daí resulte porosidade nova. O modelo mol a mol (Weyl, 1960), que produz esse ganho, exige um sistema aberto que importe Mg e exporte Ca do sistema; o modelo alternativo, de substituição volume a volume acompanhada de cimentação (Lucia), prevê **redução** de porosidade; e há autores que tratam os "13% de porosidade" como artefato de uma hipótese de trabalho que a rocha real raramente satisfaz. Guarde o número como estequiometria e a consequência porosa como hipótese condicional ao sistema geoquímico — não como regra.

### Porosidade total versus porosidade efetiva: a distinção que derruba estimativas de fluxo

A **porosidade total** conta todo o espaço vazio da rocha, incluindo poros isolados que não se conectam a nenhum outro poro. A **porosidade efetiva** conta apenas o espaço vazio que está **interconectado** e, portanto, disponível para o fluido se mover através da rocha. A diferença entre as duas é a **porosidade não efetiva** (ou isolada) — poros fechados, cavidades vesiculares isoladas em rochas vulcânicas, ou poros conectados apenas por gargantas tão estreitas que, na prática, não conduzem fluido em escala de tempo geológica relevante.

Essa distinção importa porque **porosidade alta não implica permeabilidade alta**: uma rocha vulcânica vesicular pode ter porosidade total de 20-30% e ser, na prática, quase impermeável, se as vesículas forem isoladas entre si pela matriz vítrea. Argilas e folhelhos ilustram o caso oposto e mais contraintuitivo: podem ter porosidade total muito alta (às vezes 40% ou mais em depósitos rasos, recém-depositados) e, ainda assim, permeabilidade extremamente baixa, porque os poros são minúsculos e mal conectados — o assunto da próxima seção explica por quê.

**Uma ressalva de vocabulário que volta a importar na Aula 04.** "Porosidade efetiva" tem **duas definições vivas e incompatíveis** em petrofísica, e confundi-las é um erro caro. A definição usada acima é a da análise de testemunho: porosidade efetiva = porosidade total menos a porosidade isolada, isto é, o espaço **interconectado**. Mas na interpretação de perfis de poço — o mundo em que a Aula 04 vai entrar — "porosidade efetiva" convencionalmente significa outra coisa: porosidade total menos a **água ligada à argila** (*clay-bound water*), que é imóvel e portanto inútil, ainda que esteja fisicamente conectada. Em arenito limpo as duas definições dão praticamente o mesmo número e ninguém se machuca; em folhelho e em arenito argiloso elas divergem muito, e a porosidade efetiva de testemunho seco fica **maior** que a de perfil, próxima do que o perfil chama de porosidade total. Sempre pergunte de qual das duas se está falando antes de comparar dois números de porosidade efetiva.

### Controles geológicos da porosidade: textura, compactação e diagênese

Em rochas sedimentares clásticas, quatro fatores geológicos controlam a porosidade primária:

**Seleção (sorting).** Um sedimento bem selecionado (grãos de tamanho parecido) empacota com mais espaço vazio entre os grãos do que um sedimento mal selecionado, no qual grãos menores preenchem o espaço entre os grãos maiores. Areias eólicas e de praia, tipicamente bem selecionadas, tendem a porosidades primárias mais altas do que depósitos fluviais ou de leque aluvial, comumente mal selecionados.

**Arredondamento e esfericidade dos grãos** afetam o modo de empacotamento — grãos angulares tendem a criar mais espaço vazio irregular entre si do que grãos bem arredondados, embora esse efeito seja secundário frente à seleção.

**Empacotamento (packing).** Um empacotamento cúbico teórico de esferas idênticas produz cerca de 47,6% de porosidade; um empacotamento romboédrico (o mais compacto possível para esferas iguais) produz cerca de 26%. Sedimentos reais ficam nessa faixa antes da compactação, e a compactação por soterramento — o peso da coluna de sedimentos sobrejacente reorganizando e comprimindo os grãos — reduz a porosidade progressivamente com a profundidade.

**Diagênese**, sobretudo a **cimentação**: minerais precipitados nos poros a partir da água intersticial (cimento de quartzo, calcita, ou argila autigênica) ocupam espaço que antes era poro, reduzindo porosidade — às vezes drasticamente, a ponto de uma areia originalmente porosa se tornar um arenito com porosidade quase nula (arenito "silicificado" ou "calcificado"). A diagênese também pode operar no sentido inverso: a **dissolução** de grãos ou de cimento por água subterrânea ácida cria porosidade secundária, comum em calcários (porosidade de dissolução, vugular e cárstica) e, em menor grau, em arenitos com grãos de feldspato ou fragmentos líticos instáveis.

Em rochas ígneas e metamórficas cristalinas (granito, gnaisse, basalto maciço), a porosidade primária intergranular é essencialmente nula — os cristais crescem entrelaçados, sem espaço vazio residual. Toda porosidade relevante nessas rochas é **secundária**, criada por fraturamento (porosidade de fratura) ou, em rochas vulcânicas, por vesículas de gás aprisionadas na lava em resfriamento (porosidade vesicular, que pode ser alta em volume mas mal conectada).

### Valores típicos de porosidade por litologia

Como referência de ordem de grandeza — valores reais variam amplamente com a diagênese e a profundidade de soterramento —, arenitos não consolidados a pouco consolidados situam-se tipicamente entre 25% e 35% de porosidade, caindo para a faixa de 5% a 25% em arenitos consolidados e cimentados de subsuperfície; calcários e dolomitos cobrem a faixa mais ampla de todas as rochas comuns, de próximo de 0% em calcários densamente recristalizados a mais de 30-40% em calcários vugulares, oolíticos ou cársticos; folhelhos podem superar 40% de porosidade total logo abaixo do fundo do mar e cair para menos de 10% a poucos quilômetros de profundidade, à medida que a compactação expulsa a água intersticial; e rochas ígneas e metamórficas intactas (sem fratura) ficam tipicamente abaixo de 1-2%, podendo chegar a vários pontos percentuais apenas em zonas de fraturamento denso ou de alteração hidrotermal.

### Permeabilidade: o que ela mede e por que não é a mesma coisa que porosidade

**Permeabilidade** (símbolo k) é a capacidade de um meio poroso de transmitir fluido através dele — não quanto espaço vazio existe, mas quão facilmente um fluido consegue atravessar esse espaço. A unidade tradicional é o **darcy** (ou, mais comumente em rochas de baixa a média permeabilidade, o **millidarcy**, mD, um milésimo de darcy), definida a partir da lei de Darcy para fluxo laminar em meio poroso: a vazão através de uma amostra é proporcional à permeabilidade, à área da seção transversal e ao gradiente de pressão, e inversamente proporcional à viscosidade do fluido.

A permeabilidade depende, sobretudo, de três coisas que a porosidade sozinha não descreve: o **tamanho das gargantas de poro** (a abertura mais estreita ao longo do caminho de conexão entre dois poros — o gargalo que controla o fluxo, não o tamanho médio do poro em si), a **conectividade** da rede de poros, e a presença de **argila ou material fino** obstruindo as gargantas. Isso explica a aparente contradição levantada na seção anterior: um folhelho pode ter porosidade total de 30-40% e permeabilidade da ordem de nanodarcys (bilionésimos de darcy) — muitas ordens de grandeza abaixo de um arenito — porque seus poros, embora numerosos, são extremamente pequenos, tortuosos e frequentemente desconectados pela orientação plana dos minerais de argila.

Vale desenhar isso, porque é a passagem que o hub deste módulo declara como sua armadilha central e ela é irredutivelmente **geométrica** — prosa é o pior meio possível para descrevê-la:

```
CORPO DE PORO (volume)  ×  GARGANTA DE PORO (abertura mais estreita)

(A) ARENITO LIMPO — poros grandes, gargantas largas
      ___       ___       ___
     (   )=====(   )=====(   )      φ = 20%   k = 500 mD
      ---   ^   ---   ^   ---
            |         |
         gargantas largas  -> fluxo fácil

(B) ARENITO CIMENTADO — mesmos poros, gargantas fechadas por cimento
      ___       ___       ___
     (   )|    |(   )|   |(   )     φ = 18%   k = 0,1 mD
      ---  cimento    ---
         gargantas obstruídas -> quase sem fluxo
         (a porosidade quase não mudou; a permeabilidade caiu 5.000x)

(C) FOLHELHO — porosidade ALTA, poros minúsculos e tortuosos
     .·.·.·.·.·.·.·.·.·.·.·.·.       φ = 35%   k = 0,00001 mD
     ·.·.·.·.·.·.·.·.·.·.·.·.·
         muito espaço, nenhum caminho

(D) BASALTO VESICULAR — vesículas isoladas na matriz vítrea
      (O)   (O)   (O)   (O)         φ = 25%   k ~ 0
         sem conexão nenhuma entre elas
```

Leia a figura pela **coluna da direita**, não pela esquerda: de (A) para (B) a porosidade cai 2 pontos e a permeabilidade cai por um fator de milhares; de (A) para (C) a porosidade quase **dobra** e a permeabilidade despenca oito ordens de grandeza. É o desenho inteiro do argumento desta aula — a porosidade conta o espaço, a permeabilidade conta o **caminho**, e nada obriga os dois a andarem juntos. (Os valores são ilustrativos, dentro das faixas por litologia dadas nesta aula.)

Como ordem de grandeza, arenitos-reservatório de boa qualidade situam-se tipicamente entre dezenas e milhares de millidarcys, podendo superar 1 darcy em arenitos não consolidados e muito limpos; calcários e dolomitos variam enormemente conforme o grau de fraturamento e dissolução, de poucos millidarcys em matriz intacta a valores efetivamente muito altos ao longo de condutos cársticos ou fraturas abertas; folhelhos não fraturados situam-se tipicamente entre 10⁻³ e 10⁻⁶ mD (da ordem de microdarcys a nanodarcys); e granitos e outras rochas cristalinas intactas ficam tipicamente abaixo de 10⁻³ mD, valor que pode saltar várias ordens de grandeza ao longo de um plano de fratura aberto — um lembrete de que, em rocha cristalina, a permeabilidade é essencialmente uma propriedade da fratura, não da matriz.

### A relação (frágil) entre porosidade e permeabilidade

Dentro de uma mesma litologia e sob controle textural razoavelmente uniforme, porosidade e permeabilidade costumam crescer juntas — mais espaço poroso tende a vir acompanhado de gargantas maiores. Relações empíricas como a de Kozeny-Carman formalizam essa tendência, relacionando permeabilidade a porosidade, à área superficial específica dos grãos e a um fator de forma do poro. Mas a relação **não é universal nem transferível entre litologias**: comparar a porosidade de um folhelho com a de um arenito e esperar que a permeabilidade siga a mesma proporção é o erro mais comum de quem está começando em petrofísica — o controle decisivo é o tamanho da garganta de poro, não o volume poroso total, e isso é exatamente o que distingue as duas propriedades desta aula.

## Exemplo trabalhado

**Situação:** uma amostra cilíndrica de arenito, coletada em testemunho de sondagem, tem volume total de 50 cm³. Em laboratório, mede-se que o volume ocupado pelos grãos sólidos (volume de matriz) é de 38 cm³, e que, ao saturar a amostra com salmoura sob vácuo, apenas 9 cm³ de fluido efetivamente entram nos poros interconectados (o restante do espaço vazio corresponde a poros isolados, obtidos **por diferença**: nenhuma técnica de injeção os alcança diretamente — a porosimetria de mercúrio e a saturação por líquido, por definição, só entram no espaço **conectado**, e é a picnometria de hélio, medindo o volume de grãos, que fecha a conta da porosidade total).

**Pergunta:** calcule a porosidade total e a porosidade efetiva da amostra, e discuta o que a diferença entre as duas sugere sobre a rocha.

**Resolução:**

Volume de poros totais = Volume total − Volume de grãos = 50 cm³ − 38 cm³ = 12 cm³

Porosidade total: φ_total = V_poros_total / V_total = 12 / 50 = 0,24 → **24%**

Porosidade efetiva: φ_efetiva = V_poros_conectados / V_total = 9 / 50 = 0,18 → **18%**

Porosidade não efetiva (isolada): 24% − 18% = **6%**

**Discussão:** os 6 pontos percentuais de porosidade isolada (25% de toda a porosidade da amostra) não participam do fluxo de fluido e, portanto, não devem entrar em qualquer cálculo de permeabilidade, de volume de fluido recuperável ou de capacidade de armazenamento efetiva de um aquífero ou reservatório. Um relatório que reportasse "24% de porosidade" sem qualificar qual das duas está sendo citada superestimaria em 33% (18% → 24% é um aumento relativo de 33%) a capacidade real de a rocha entregar fluido — a diferença entre "quanto espaço vazio existe" e "quanto desse espaço serve para alguma coisa" é exatamente a lição desta aula, e ela se paga em decisões de campo, não só em prova.

## Erros comuns

- **Reportar "porosidade" sem especificar total ou efetiva.** Como o exemplo trabalhado mostra, a diferença entre as duas (24% vs. 18%) é uma superestimativa relativa de 33% na capacidade de entregar fluido — um número solto sem qualificação é ambíguo o bastante para distorcer uma decisão de campo.
- **Comparar "porosidade efetiva" de um relatório de testemunho com a de um perfil de poço como se fossem a mesma grandeza.** A aula avisa: são duas definições vivas e incompatíveis (espaço interconectado vs. total menos água ligada à argila) — coincidem em arenito limpo, mas divergem muito em folhelho e arenito argiloso.
- **Assumir que a relação porosidade-permeabilidade (Kozeny-Carman) vale entre litologias diferentes.** A relação empírica funciona dentro de uma mesma litologia sob controle textural uniforme; comparar um folhelho com um arenito esperando permeabilidade proporcional à porosidade é o erro mais citado por quem começa em petrofísica.
- **Tratar os "13% de redução de volume" da dolomitização como prova automática de ganho de porosidade.** A estequiometria é sólida; a consequência porosa depende do sistema ser aberto ao Mg/Ca — a aula é explícita que isso é hipótese condicional, não regra.

## O que não concluir

- **Que porosidade alta sempre significa boa rocha-reservatório.** Folhelhos e basalto vesicular desmentem isso diretamente — o que importa é a porosidade efetiva combinada com permeabilidade, não a porosidade total isolada.
- **Que picnometria de hélio e saturação por líquido medem a mesma coisa por caminhos diferentes.** Só a picnometria de hélio alcança o espaço isolado (via volume de grãos); a saturação por líquido e a porosimetria de mercúrio só entram no espaço conectado — a porosidade isolada só existe na conta por diferença entre as duas medidas.
- **Que rocha cristalina intacta (granito, gnaisse) não pode ser um reservatório ou aquífero produtivo.** Não pela matriz — mas a permeabilidade de fratura pode saltar várias ordens de grandeza acima da matriz intacta, tornando essas rochas produtivas ao longo de planos de fratura específicos.

## Recap relâmpago

- Porosidade (φ) é a razão entre volume de poros e volume total da rocha; não diz nada, sozinha, sobre tamanho, forma ou conectividade dos poros.
- Porosidade total inclui poros isolados; porosidade efetiva conta só o espaço interconectado, disponível ao fluxo — a diferença entre as duas pode ser grande e muda diretamente qualquer estimativa de volume de fluido recuperável. Cuidado com o termo: em interpretação de perfil de poço, "porosidade efetiva" significa porosidade total menos a água ligada à argila, definição diferente da de testemunho e que só coincide com ela em rocha limpa.
- Porosidade isolada não é medida diretamente por nenhuma técnica de injeção — mercúrio e saturação por líquido só entram no espaço conectado; a porosidade isolada sai por diferença, contra a porosidade total obtida por picnometria de hélio.
- Porosidade primária vem da deposição (controlada por seleção, arredondamento e empacotamento dos grãos); porosidade secundária vem de processos pós-deposicionais — dissolução, fraturamento, dolomitização — e domina em rochas cristalinas, onde a porosidade primária é essencialmente nula. Na dolomitização, os ~13% de redução de volume do sólido são estequiometria segura, mas o ganho de porosidade daí decorrente é disputado na literatura e depende do sistema ser aberto ao Ca.
- Cimentação diagenética reduz porosidade ocupando espaço poroso; dissolução a aumenta — os dois processos podem atuar na mesma rocha em momentos diferentes de sua história.
- Permeabilidade (k, em darcy ou millidarcy) mede a facilidade de um fluido atravessar a rocha, e depende do tamanho das gargantas de poro e da conectividade da rede — não do volume poroso total.
- Porosidade alta não implica permeabilidade alta: folhelhos podem ter porosidade total maior que arenitos e, ainda assim, permeabilidade muitas ordens de grandeza menor, por causa do tamanho minúsculo e da má conectividade de seus poros; em rocha cristalina, a permeabilidade é essencialmente uma propriedade da fratura, não da matriz.

## Próxima aula

[[15-petrofisica-aula-02-densidade-propriedades-elasticas-velocidades-sismicas|Aula 02 — Densidade, propriedades elásticas e propagação de ondas sísmicas]] — a porosidade volta a aparecer aqui como um dos principais controles da densidade e da velocidade sísmica de uma rocha, junto com a composição mineral e o fluido que ocupa os poros.

## Fontes

- Schön, J. H. (2015), *Physical Properties of Rocks: Fundamentals and Principles of Petrophysics*, 2ª ed., Elsevier, cap. 2-3 (definições de porosidade total/efetiva, controles geológicos, faixas típicas por litologia).
- Tiab, D. & Donaldson, E. C. (2015), *Petrophysics: Theory and Practice of Measuring Reservoir Rock and Fluid Transport Properties*, 4ª ed., Gulf Professional Publishing, cap. 2-4 (porosidade, permeabilidade, lei de Darcy, relação Kozeny-Carman).
- Ellis, D. V. & Singer, J. M. (2007), *Well Logging for Earth Scientists*, 2ª ed., Springer, cap. 1 (faixas de porosidade e permeabilidade por litologia em contexto de perfilagem).
- Telford, W. M., Geldart, L. P. & Sheriff, R. E. (1990), *Applied Geophysics*, 2ª ed., Cambridge University Press, cap. 1 (propriedades físicas de rochas, ordens de grandeza de permeabilidade).
- Weyl, P. K. (1960), "Porosity through dolomitization: conservation-of-mass requirements", *Journal of Sedimentary Petrology*, 30(1), 85-90 (modelo mol a mol e o cálculo dos ~13%).
- Machel, H. G. (2004), "Concepts and models of dolomitization: a critical reappraisal", *Geological Society, London, Special Publications*, 235, 7-63 (reavaliação crítica; por que a criação de porosidade é condicional e não automática).
- Schlumberger *Energy Glossary*, verbete "effective porosity" (as duas definições concorrentes do termo em análise de testemunho e em interpretação de perfil).

<!--
nivel: avancado
palavras_corpo: 2503
mapa_objetivo_secao:
  geologia-avancado-m15-oa01: "Por que a petrofísica abre esta área do curso" + "Porosidade: definição e o que ela não diz sozinha" + "Porosidade total versus porosidade efetiva: a distinção que derruba estimativas de fluxo" + "Controles geológicos da porosidade: textura, compactação e diagênese" + "Valores típicos de porosidade por litologia" + "Permeabilidade: o que ela mede e por que não é a mesma coisa que porosidade" + "A relação (frágil) entre porosidade e permeabilidade" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: PETROFIS-M15-A01-DEFPOROSIDADE-001
    claim: "Porosidade (phi) é definida como a razão entre o volume de poros e o volume total da rocha, expressa como fração ou percentual; distingue-se porosidade primária (deposicional) de secundária (dissolução, fraturamento, dolomitização) e porosidade total de porosidade efetiva (apenas o espaço interconectado disponível ao fluxo)."
    risk: fato
    source: "Schön 2015, Physical Properties of Rocks, cap. 2; Tiab & Donaldson 2015, Petrophysics, cap. 2"
  - claim_id: PETROFIS-M15-A01-EMPACOTAMENTO-002
    claim: "Empacotamento cúbico de esferas idênticas produz cerca de 47,6% de porosidade teórica; empacotamento romboédrico (o mais compacto possível para esferas iguais) produz cerca de 26%."
    risk: fato
    source: "Tiab & Donaldson 2015, Petrophysics, cap. 2 (geometria de empacotamento de esferas). Verificado por cálculo direto: 1 - pi/6 = 0,4764 (cúbico) e 1 - pi/(3*raiz2) = 0,2595 (romboédrico)."
  - claim_id: PETROFIS-M15-A01-DOLOMITIZACAO-006
    claim: "A substituição mol a mol de calcita por dolomita reduz o volume do sólido em cerca de 13% (2 x 36,9 cm3/mol de calcita contra 64,3 cm3/mol de dolomita). CONTROVERSO: se dessa redução resulta porosidade nova é matéria em disputa aberta - o modelo mol a mol de Weyl (1960) prevê ganho de porosidade e exige sistema aberto que importe Mg e exporte Ca; o modelo volume a volume com cimentação (Lucia) prevê perda. A aula registra as duas posições sem escolher lado."
    risk: controverso
    source: "Weyl 1960, J. Sedimentary Petrology 30(1):85-90; Machel 2004, Geol. Soc. London Spec. Publ. 235:7-63 (reavaliação crítica). Achado branco da auditoria de 2026-09-08 - politica de achado controverso: registrar a divergencia, nao arbitrar."
  - claim_id: PETROFIS-M15-A01-POROSIDADEEFETIVA-007
    claim: "O termo 'porosidade efetiva' tem duas definições concorrentes e ativas: em análise de testemunho, porosidade total menos a porosidade isolada (espaço interconectado); em interpretação de perfil de poço, porosidade total menos a água ligada à argila (clay-bound water). Coincidem em rocha limpa e divergem muito em rocha argilosa, com a definição de testemunho dando o valor maior."
    risk: fato
    source: "Schlumberger Energy Glossary, verbete 'effective porosity'; Cuddy, 'Should petrophysics calculate total or effective porosity?', AFES 2021. Ressalva acrescentada pela auditoria de 2026-09-08 (achado laranja PETROFIS-M15-A01-POROSIDADEEFETIVA-007): a omissão tornava a definição falsa como escrita para o contexto de perfilagem em que a Aula 04 entra."
  - claim_id: PETROFIS-M15-A01-POROSIMETRIA-008
    claim: "A porosidade isolada não é medida diretamente por técnicas de injeção: a porosimetria de mercúrio e a saturação por líquido só acessam o espaço poroso CONECTADO. A porosidade isolada é obtida por diferença entre a porosidade total (via picnometria de hélio, que mede volume de grãos) e a porosidade conectada."
    risk: fato
    source: "Anton Paar, Mercury Intrusion Porosimetry Basics; ACS Energy & Fuels 2024/2025 (comparações He-picnometria vs. MIP em folhelhos). Correção da auditoria de 2026-09-08 (achado laranja): o exemplo trabalhado atribuía à porosimetria de mercúrio exatamente o que ela não consegue fazer."
  - claim_id: PETROFIS-M15-A01-FAIXASPOROSIDADE-003
    claim: "Ordens de grandeza típicas de porosidade: arenitos não consolidados 25-35%, arenitos consolidados de subsuperfície 5-25%; calcários/dolomitos de próximo de 0% a mais de 30-40% (vugular/cárstico); folhelhos de mais de 40% (raso, recém-depositado) a menos de 10% (poucos km de profundidade); rochas ígneas/metamórficas intactas tipicamente abaixo de 1-2%."
    risk: aproximacao
    source: "Schön 2015, Physical Properties of Rocks, cap. 2, tabelas de porosidade por litologia; Ellis & Singer 2007, Well Logging for Earth Scientists, cap. 1. Faixas amplas e deliberadamente aproximadas, dada a grande variabilidade real por diagênese e soterramento."
  - claim_id: PETROFIS-M15-A01-DEFPERMEABILIDADE-004
    claim: "Permeabilidade (k) mede a capacidade de um meio poroso transmitir fluido, definida pela lei de Darcy; a unidade tradicional é o darcy, mais comumente usada como millidarcy (mD, um milésimo de darcy) em rochas de baixa a média permeabilidade. Depende do tamanho das gargantas de poro, da conectividade da rede porosa e da presença de material fino/argila, não do volume poroso total."
    risk: fato
    source: "Tiab & Donaldson 2015, Petrophysics, cap. 3-4; Telford, Geldart & Sheriff 1990, Applied Geophysics, cap. 1"
  - claim_id: PETROFIS-M15-A01-FAIXASPERMEABILIDADE-005
    claim: "Ordens de grandeza típicas de permeabilidade: arenitos-reservatório de boa qualidade, dezenas a milhares de mD (podendo superar 1 darcy em areias não consolidadas limpas); folhelhos não fraturados tipicamente 10^-3 a 10^-6 mD (microdarcy a nanodarcy); granitos e rochas cristalinas intactas tipicamente abaixo de 10^-3 mD, com aumento de várias ordens de grandeza ao longo de fraturas abertas; calcários/dolomitos com permeabilidade de matriz baixa mas muito variável conforme fraturamento e dissolução."
    risk: aproximacao
    source: "Schön 2015, Physical Properties of Rocks, cap. 3, tabelas de permeabilidade por litologia; Tiab & Donaldson 2015, cap. 4. Faixas amplas por natureza — a permeabilidade varia mais ordens de grandeza que qualquer outra propriedade petrofísica comum."
-->
