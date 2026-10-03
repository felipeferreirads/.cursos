# Revisão didática — Módulo 19: Geofísica aplicada na exploração mineral

**Data:** 2026-09-13
**Modo:** `review-and-fix` (melhorias aplicadas)
**Escopo:** as 6 aulas do módulo, mais o hub. **Não há questionário nem baralho** — a cadeia rodou na ordem correta aqui, ao contrário do Módulo 18, de modo que a linha "alinhamento aula-avaliação" da tabela de cobertura volta a ser verificável apenas como consistência interna aula↔objetivo declarado.
**Veredito:** **bem ensinado com ressalvas** — 23 achados, 22 corrigidos e 1 encaminhado ao usuário. Nenhum salto de pré-requisito não sinalizado ao fim desta passagem, nenhum termo central indefinido, nenhum objetivo de módulo sem seção que o ensine, nenhum exemplo trabalhado com salto lógico.

## Resumo

🔴 0 bloqueiam · 🟠 7 prejudicam · 🟡 12 atrito · 🔵 4 sugestões

**Carga estimada do módulo:** 6 aulas · **13.090 palavras de corpo reais** (2.017 / 2.480 / 2.239 / 2.287 / 2.070 / 1.997) · 4 objetivos de aprendizagem para 6 aulas (`oa03` coberto por a03+a04, `oa04` por a05+a06) · 6 exemplos trabalhados, **todos interpretativos ou de classificação** — nenhum pede aritmética, o que a auditoria já havia registrado.

A distribuição é a mais desigual dos três últimos módulos, e o desvio tem uma causa identificável: **os seis blocos `palavras_corpo` declarados pelas aulas estavam todos desatualizados, e o da a02 em 39%** (declarava 1.690 contra 2.352 reais antes desta passagem). A a02 é a aula mais pesada do módulo por margem clara e é o único achado que esta skill não resolve sozinha.

## A ordem da cadeia, e o que ela muda nesta revisão

Este módulo teve a auditoria científica concluída em 2026-09-13, modo `audit-and-fix`, veredito **aprovado**, e **nenhum material derivado existe** — sem questionário, sem flashcards. É a ordem normal da cadeia neste curso, e ela facilita esta passagem em dois pontos e a dificulta num terceiro:

1. **Nenhuma correção didática teve custo de propagação.** Nenhum arquivo fora das seis aulas e do hub precisou ser tocado, e nenhuma das 22 correções aplicadas exigiria sincronização se questionário e baralho já existissem — todas são quebra de parágrafo, lista, tabela, glosa, ressalva de método, aviso de cabeçalho ou acerto de contagem.
2. **Uma decisão que no Módulo 18 era cara aqui é barata.** O achado 🟠 `-004` (carga da a02) chega a esta revisão sem nenhum material derivado para arrastar: se o usuário optar por dividir a aula, o custo é renumerar arquivos e ajustar hub e estado, e mais nada. No M18 a mesma decisão arrastava questionário, dois baralhos e cinco arquivos. **É a hora mais barata possível de decidir**, e por isso o achado é encaminhado com as duas opções vivas, e não com uma recomendação fechada disfarçada de pergunta.
3. **Alinhamento aula-avaliação não é verificável nesta passagem**, como no Módulo 17. O que se verificou em lugar disso foi a consistência interna: cada "Ao final você vai conseguir" contra o que a aula de fato ensina, e cada seção contra o objetivo do módulo a que o `mapa_objetivo_secao` a atribui. **Três desalinhamentos foram encontrados aí** (`-005`, `-011`, `-017`), todos no sentido de o cabeçalho prometer de menos ou de mais em relação ao corpo, e todos corrigidos. Isso é exatamente o material que o gerador de questionário vai ler como enunciado de objetivo, de modo que corrigi-los agora é o que impede um desalinhamento futuro.

**Nenhuma correção da auditoria de 2026-09-13 foi desfeita, diluída ou reformulada.** A correção vermelha (polaridade potássica/fílica na a02) e as sete correções de atribuição de fonte foram reverificadas literalmente depois de cada edição — ver a seção de verificação mecânica ao fim. Onde um achado didático incidia sobre trecho **criado** pela auditoria — e são quatro: `-001`, `-002`, `-003` e `-008` —, a intervenção foi exclusivamente de forma, e o texto auditado está inteiro dentro da nova forma.

## O que o módulo já fazia bem, antes da revisão

1. **O fio condutor é declarado na primeira aula, cumprido e fechado na última.** A a01 anuncia que o módulo vai desenvolver o compromisso resolução × profundidade "método a método nas próximas cinco aulas"; a a04 o invoca nominalmente duas vezes ("o mesmo mecanismo de atenuação dependente de frequência introduzido na Aula 01, aqui levado ao extremo"); a a06 fecha com "o módulo fecha exatamente onde começou, com o sistema mineral como o quadro conceitual que dá sentido a todo o dado geofísico coletado". Módulo metodológico que não vira seis capítulos soltos é raro.
2. **A a05 é a melhor aula do módulo pelos dois critérios, o factual e o didático.** A auditoria a aprovou inteira; ela é também a única cuja progressão é estritamente construtiva — problema direto, problema inverso, por que é não único, o que fazer a respeito, o que isso custa, como ancorar. Cada seção usa só o que a anterior entregou. É o padrão que as outras cinco deveriam imitar.
3. **O exemplo trabalhado da a05 ensina uma distinção que material didático quase sempre borra:** que "matematicamente igualmente válido" e "melhor embasado para decidir" são coisas diferentes. A conclusão diz com todas as letras que a Equipe B decide melhor **sem** que seu modelo seja "mais verdadeiro" num sentido matemático absoluto. Isso é competência transferível, não conteúdo de geofísica.
4. **A a03 constrói o diagnóstico em vez de enunciá-lo.** As quatro seções montam, uma de cada vez, exatamente as peças de que o exemplo trabalhado vai precisar: os dois mecanismos de condução, onde a resistividade falha, o que a IP acrescenta, e só então a combinação. Quando o exemplo chega com as Zonas A/B/C, o leitor já tem tudo. A auditoria chamou esse material de "o melhor material de avaliação do módulo" pelo critério factual; ele é bem construído também pelo critério pedagógico.
5. **A a01 ensina o limite econômico do método, não só o físico.** "Rodar um levantamento de eletrorresistividade terrestre de detalhe sobre uma província inteira não é apenas caro — é desperdício de resolução que a pergunta daquela escala não precisa." Um módulo de geofísica aplicada que separa "o método consegue" de "o método vale a pena" está ensinando exploração, não só instrumentação.
6. **A a06 nomeia o viés de amostragem de exploração com precisão incomum.** Tratar "não confirmado" como "geologicamente desfavorável" penaliza justamente a fronteira menos estudada — a formulação está correta no sentido (a auditoria verificou o sentido explicitamente) e é a que mais frequentemente aparece invertida em material de divulgação.

---

## Achados

### 🟠 DID-M19-A02-MAGNETOPARAGRAFO-001 — O parágrafo de magnetometria fundiu cinco assuntos, e a remanência, que é objetivo declarado, virou a cauda de um parágrafo sobre pórfiro
**Tipo:** densidade irregular / estrutura escondida · **Onde:** a02, seção "Magnetometria", terceiro parágrafo · **Escopo:** correção local.

**Problema:** um único parágrafo carregava, em sequência: por que halos de alteração são o que a magnetometria detecta; o halo de pirrotita monoclínica em VMS; a regra de sinal de três termos do zoneamento de pórfiro; a armadilha do canal K; e a interpretação sob remanência. Cinco movimentos conceituais, dos quais **dois são conteúdo central declarado no cabeçalho da aula**.

O custo específico é o destino da **remanência**. Ela é metade do título da seção ("magnetização induzida e o problema da remanência") e um dos três resultados prometidos no "Ao final você vai conseguir". Ela aparecia na última frase de um parágrafo sobre zoneamento de pórfiro, aberta por "A interpretação, porém, exige cuidado com a remanência" — uma subordinada, no lugar de mais baixa visibilidade do parágrafo. Um leitor que pare de ler esse parágrafo no meio (e ele convida a isso) perde um objetivo declarado inteiro.

Este achado foi **agravado pela auditoria, sem culpa dela**, e foi exatamente previsto por ela: o achado 🔴 `AUD-M19-A02-PORFIROMAGNETITA-001` inseriu a regra de sinal de três termos, necessária e correta, dentro de um parágrafo que já estava saturado. É o mesmo padrão de `DID-M18-A04-FORCASPARAGRAFO-003` e de `DID-M17-A04-PARAGRAFOMURO-007`: corrigir o fato tornou a forma pior. As `out_of_scope_observations` da auditoria mandam olhar este parágrafo primeiro, e estavam certas.

**Correção aplicada:** dividido em três parágrafos, **sem acrescentar nem remover conteúdo**: (i) os halos de alteração em geral, com o caso VMS; (ii) a regra de sinal do pórfiro, aberta pela frase auditada "E o sentido dessa troca não é arbitrário" e reformatada como **lista de três termos** — potássica acrescenta / fílica destrói / propilítica preserva ou repõe —, seguida da armadilha do canal K, agora destacada em negrito e marcada como "a discriminação de maior valor desta aula"; (iii) a **remanência em parágrafo próprio**, aberto por "Falta a segunda metade anunciada no título desta seção", o que devolve ao tema a posição que o título e o cabeçalho já lhe prometiam. As formulações auditadas estão preservadas palavra por palavra.

### 🟠 DID-M19-A02-SUSCEPTIBILIDADE-002 — A régua de susceptibilidade e a hierarquia de minerais magnéticos num bloco só, com os três degraus escondidos em prosa corrida
**Tipo:** densidade irregular / notação acumulada sem consolidação · **Onde:** a02, seção "Magnetometria", segundo parágrafo · **Escopo:** correção local.

**Problema:** o parágrafo entregava, corrido, a adimensionalidade no SI, a amplitude de mais de cinco ordens de grandeza, os três degraus da escala com seus tipos de rocha, o teto mineral, a amarração ao módulo, a dominância da magnetita, a ordem titanomagnetitas/maghemita/pirrotita monoclínica, o qualificador de fase, o contraste antiferromagnético da hexagonal e a dependência de campo da monoclínica.

O dano não é o comprimento — é que o conteúdo é **uma régua numérica**, e régua em prosa corrida não se consulta. Os três degraus (10⁻⁶-10⁻⁵ / 10⁻³-10⁻² / 10⁻¹ a ~1) são o instrumento que o aluno leva para ler um mapa aeromagnético, e enterrá-los entre vírgulas, num parágrafo que continua por mais seis afirmações, é a forma menos utilizável possível de apresentá-los. Como no `-001`, o bloco foi **engrossado pela auditoria**: as correções 🟠 `...SUSCEPTIBILIDADE-005` (teto de 10⁻² para a ordem da unidade) e 🟠 `...PIRROTITA-006` (fase e ordem) entraram ambas aqui.

**Correção aplicada:** dividido em três parágrafos com funções distintas: (i) a amplitude, com **os três degraus em lista**, abertos por uma frase que diz para que serve a régua ("é com ela que se lê qualquer mapa aeromagnético"); (ii) o teto mineral (~5 SI) e a amarração ao módulo, com "os alvos deste módulo vivem no topo da escala, não em 10⁻²" agora em negrito e em posição de fecho; (iii) a hierarquia de minerais, aberta por "Quem ocupa esse topo é uma hierarquia curta de minerais", com o qualificador de fase e a ordem do Módulo 15 intactos. Nenhum valor alterado.

### 🟠 DID-M19-A02-DENSIDADESPROSA-003 — Seis densidades minerais em prosa corrida, e a distinção mineral × corpo de minério diluída na mesma frase
**Tipo:** densidade irregular / distinção central em posição de baixa visibilidade · **Onde:** a02, seção "Gravimetria", primeiro parágrafo · **Escopo:** correção local.

**Problema:** o parágrafo de abertura da aula mais densa do módulo carregava **seis densidades minerais em sequência**, seguidas da densidade do corpo de minério, de duas densidades de rocha encaixante e do contraste resultante — dez números numa frase e meia.

E a estrutura escondida ali não é uma lista de números: são **duas réguas diferentes**, e a auditoria gastou um achado 🟠 (`...DENSIDADESULFETO-004`) justamente sobre confundi-las. A correção entrou com a oração "Um corpo de minério real, porém, nunca é mineral puro", que é exata e ocupava menos de uma linha no meio do bloco. A distinção que a auditoria considerou cara o bastante para custar um laranja estava, na forma, menos visível que qualquer dos números individuais.

**Correção aplicada:** dividido em quatro parágrafos: (i) o que a gravimetria mede e o sinal da anomalia; (ii) a abertura "Aqui há **duas réguas de densidade diferentes, e confundi-las é um erro caro**", seguida da **régua mineral em lista de seis itens** — com a galena preservada como "o extremo da lista"; (iii) a **régua do corpo de minério**, em parágrafo próprio, nomeada como "a que o gravímetro de fato lê" e com glosa de **ganga** acrescentada em aposto; (iv) o contraste e a consequência para VMS e IOCG. Nenhum valor alterado; a palavra "ganga" ganhou a única glosa nova do bloco.

### 🟠 DID-M19-A02-CARGA-004 — A Aula 02 é 24% maior que a mediana do módulo e a mais densa em fatos numéricos; avaliar divisão
**Tipo:** excesso de conceitos novos / duração declarada irreal · **Onde:** a02, aula inteira · **Escopo:** **não corrigido — encaminhado ao usuário.**

**Problema:** a a02 tem **2.480 palavras de corpo** contra uma mediana de ~2.150 nas outras cinco, e declarava "~30 min" apoiada num `palavras_corpo` de 1.690 que estava 39% abaixo do real. Mais relevante que o tamanho é a **densidade de fatos numéricos consultáveis**: seis densidades minerais, duas densidades de rocha encaixante, um contraste, três degraus de susceptibilidade, um teto mineral, três picos de energia, três janelas de energia com dois intervalos mortos e uma profundidade de penetração. É a única aula do módulo que funciona também como tabela de referência, e tabela de referência não se lê em trinta minutos — se consulta.

A auditoria previu este achado em duas linhas das `out_of_scope_observations` ("vale conferir se a a02 ainda cabe nos ~30 min declarados"). A resposta é **não**: realisticamente ~40 min, e mais se o leitor tentar fixar os números.

**Por que não corrigi:** sobrecarga não se conserta com mais explicação, e dividir uma aula é decisão do orquestrador — isso não mudou desde o M17 e o M18. As três correções de forma aplicadas acima (`-001`, `-002`, `-003`) **não reduzem a carga; dão fôlego** e tornam os números consultáveis, que é o máximo que esta skill faz.

**Encaminhamento ao usuário** — duas opções, e desta vez **sem recomendação fechada**, porque o custo relativo mudou em relação ao M18:

1. **Aceitar a aula como está e corrigir a duração declarada** de "~30 min" para "~40 min" no cabeçalho da a02 e no hub. Custo: duas linhas. Não deixei isso aplicado porque a escolha depende da opção 2 — corrigir a duração de uma aula que será dividida seria trabalho perdido.
2. **Dividir a a02** em duas: **campos potenciais** (gravimetria + magnetometria) e **gamaespectrometria**, renumerando a03-a06 para a04-a07 e passando o módulo a 7 aulas, com `oa02` coberto em conjunto pelas duas — nenhum objetivo novo criado, exatamente a forma da divisão do M18.

**O que pesa em cada lado, para a decisão ser informada:**

- **A favor de dividir:** o custo é o mais baixo que jamais será. Não existe questionário nem baralho, então a divisão arrasta apenas os arquivos das aulas, o hub e o `course-state.yaml` — nada de remapear faixas de cards, blocos de questionário ou gabaritos. No M18, esta mesma decisão arrastava cinco arquivos e material em revisão no Anki; aqui arrasta três e nada em revisão.
- **Contra dividir, e é o argumento mais forte:** **o exemplo trabalhado da a02 não sobrevive ao corte.** Ele lê um alvo de pórfiro cruzando magnetometria **com** gamaespectrometria, e a discriminação de maior valor do módulo inteiro — que o canal K não separa potássica de fílica, e que quem separa é o sinal magnético — **só existe na interseção dos dois métodos**. Separar a gamaespectrometria numa aula própria deixaria o exemplo órfão numa das duas metades e desmontaria o ponto que a auditoria nomeia como o achado de maior valor pedagógico do módulo (`generator_warnings`, item 3). Uma divisão que preservasse o exemplo teria de mover a gamaespectrometria inteira junto com ele, o que reconstitui a aula atual sob outro nome.
- **Efeito colateral em terceiro lugar:** a recomendação preliminar da auditoria de **3 parciais + 1 cumulativo**, com fronteiras a01 / a02 / a03+a04 / a05+a06, pressupõe 6 aulas. Dividir a a02 muda a primeira fronteira e o gerador de questionários precisa ser avisado (🔵 S3).

**Se a decisão for não dividir, a ação é a opção 1** — e ela não pode ser esquecida, porque "~30 min" numa aula de ~40 é o dano concreto deste achado para quem planeja o estudo.

### 🟠 DID-M19-A04-OBJETIVOTDEM-005 — O objetivo declarado da a04 ficou sendo o único lugar da aula que ainda ensina a versão que a auditoria corrigiu
**Tipo:** desalinhamento cabeçalho–corpo / certeza indevida sobrevivente · **Onde:** a04, "Ao final você vai conseguir" · **Escopo:** correção local.

**Estava escrito:** *"explicar por que o domínio do tempo tende a alcançar maior profundidade de investigação"* — sem qualificador.

**Problema:** a auditoria gastou o achado 🟠 `AUD-M19-A04-CHENTDEM-008` precisamente para restringir essa afirmação. Depois dela, o corpo diz "comparando sistemas aéreos de **bobina rebocada**, que é a comparação justa" e dedica um parágrafo inteiro a explicar que em fonte aterrada a profundidade vem da geometria da fonte e vale **nos dois domínios**. O recap ganhou um bullet novo com a mesma separação. O cabeçalho não foi tocado, e ficou sendo **o único ponto do arquivo que ainda enuncia a versão irrestrita** — em negrito, na primeira tela, que é onde o leitor forma a expectativa do que vai aprender.

O agravante é de propagação futura: é o "Ao final você vai conseguir" que o gerador de questionários lê como enunciado do que cobrar. Um item gerado a partir deste cabeçalho nasceria com o gabarito que a auditoria acabou de desfazer — o mesmo risco que custou vermelho a este módulo, chegando por outra porta.

**Correção aplicada:** o resultado passou a "explicar por que o domínio do tempo tende a alcançar maior profundidade de investigação **entre sistemas aéreos de bobina rebocada** — e por que essa vantagem não vale para arranjos de fonte aterrada, em que a profundidade vem da geometria da fonte e não do domínio". O cabeçalho agora promete o que o corpo corrigido entrega, incluindo a ressalva.

### 🟠 DID-M19-A04-EXEMPLOBOBINA-006 — O exemplo trabalhado compara três plataformas diferentes logo depois de a aula dizer qual é a comparação justa
**Tipo:** salto no exemplo trabalhado / exemplo que contraria a regra recém-ensinada · **Onde:** a04, Exemplo trabalhado, Resolução · **Escopo:** correção local.

**Problema:** a seção anterior acabara de ensinar, por correção da auditoria, que a comparação TDEM × FDEM só é legítima **entre sistemas aéreos de bobina rebocada**, e que profundidade também se compra por geometria de fonte. O exemplo imediatamente seguinte põe lado a lado um **FDEM terrestre de bobina fixa**, um **TDEM aéreo** e um **GPR terrestre** — três plataformas diferentes — e conclui pelo TDEM, fechando com "o mesmo paradoxo resolução × profundidade sendo resolvido, aqui, pela escolha do domínio de aquisição (tempo versus frequência)".

O exemplo **não está errado**: ele decide pelas profundidades de investigação **declaradas de cada sistema específico**, que a própria situação fornece (100 m, várias centenas de metros, poucos metros), e só invoca o domínio para explicar a robustez à cobertura condutora — o que é legítimo. Mas ele não diz isso em lugar nenhum. Do ponto de vista de quem lê pela primeira vez, o efeito é de contradição: a aula ensinou uma restrição e o exemplo parece ignorá-la uma página depois. O leitor atento suspeita da regra; o desatento conclui que a restrição era retórica e a esquece — e a restrição é justamente o que a auditoria pagou um laranja para instalar.

**Correção aplicada:** uma nota de método abrindo a resolução, antes de qualquer item — declarando que os três candidatos não são sistemas comparáveis de bobina rebocada, que a comparação abaixo usa a **profundidade de investigação declarada de cada sistema específico**, que é o dado que a situação fornece, e que o domínio só é invocado no fim, para explicar o comportamento diante da cobertura condutora. Nenhum fato novo: os três valores declarados já estavam no enunciado da situação. A conduta que a resolução já adotava passou a ser explicitada, em vez de apenas executada — mesma forma de `DID-M18-A04-ORDEMEXEMPLO-015`.

### 🟠 DID-M19-A06-MLVOCABULARIO-007 — A Aula 06 usa vocabulário de aprendizado de máquina que o curso só ensina cinco módulos adiante, sem declarar isso
**Tipo:** salto de pré-requisito não declarado · **Onde:** a06, cabeçalho e seção "Abordagens orientadas por dados" · **Escopo:** correção local.

**Problema:** a a06 usa, sem glosa e como se fossem conhecidos, **floresta aleatória**, **árvores de decisão**, **máquinas de vetores de suporte**, **redes neurais**, **aprendizado supervisionado** e **desbalanceamento de classes**. O cabeçalho declara como pré-requisito apenas "todas as aulas anteriores deste módulo". Nenhuma delas ensina qualquer um desses termos, e **o curso só os ensina no Módulo 24 — cinco módulos adiante**.

Este é o defeito mais fatal do catálogo desta skill quando não sinalizado, e o dano no leitor autodidata é específico: ele não tem como saber se aquilo é (a) algo que ele deveria ter aprendido e não aprendeu, (b) algo que a aula vai explicar mais adiante, ou (c) algo que ele pode atravessar sem entender. Na dúvida, ou ele para e vai estudar florestas aleatórias por fora — gastando horas fora do orçamento da aula —, ou segue com a sensação de estar perdendo o fio. **As duas condutas são caras, e a segunda é pior**, porque a aula de fato não exige nenhum desses algoritmos: todo o raciocínio dela é sobre o que **qualquer** algoritmo supervisionado faz com 6 positivos e uma camada de 8% de cobertura, e isso ela ensina do zero e muito bem.

Note que este é o inverso exato de `DID-M18-A02-POROSIDADE-008` e `DID-M17-A01-PREREQ-004`: lá o cabeçalho declarava pré-requisito que a aula não usava; aqui a aula usa vocabulário que o cabeçalho não declara. Nos dois casos o custo é o mesmo — orçamento de atenção gasto no lugar errado.

**Correção aplicada:** uma linha nova de cabeçalho, "Aviso sobre o vocabulário de aprendizado de máquina", dizendo com todas as letras que a aula **não** pressupõe conhecimento desses algoritmos, que **não é aqui que eles se aprendem**, que quem os ensina é o Módulo 24 (com wikilink), que os nomes aparecem apenas como rótulos de famílias de algoritmo, e que o que importa na aula — o que qualquer um deles faz com um conjunto de treinamento pequeno e enviesado — ela ensina do zero. Converte um salto de pré-requisito em instrução de leitura acionável, sem ensinar o pré-requisito no meio da aula (que é como uma aula de 30 min vira uma de 50).

---

### 🟡 DID-M19-A03-LIMIARES-008 — Os dois limiares de linearidade da IP estavam escritos de forma que se lê como contradição
**Tipo:** formulação que ensina o oposto do pretendido · **Onde:** a03, seção "Polarização induzida", terceiro parágrafo · **Escopo:** correção local.

**Estava escrito:** *"aproximadamente linear até cerca de **20%** do volume de rocha — acima disso, e em texturas maciças ou de veio, a relação deixa de ser linear (nessas texturas a cargabilidade cresce de forma não linear já abaixo de **~30%** de volume)"*.

**Problema:** a frase diz "deixa de ser linear **acima** de 20%" e, quatro palavras depois, "não linear já **abaixo** de ~30%". Lidas em sequência, as duas se contradizem, e o leitor não tem como saber qual vale. A causa é que **são dois limiares de duas texturas diferentes**, fundidos numa única oração com um parêntese: 20% é o teto do regime linear no **disseminado**; 30% é a marca abaixo da qual o crescimento **já é** não linear em **veio/maciço** — ou seja, na segunda textura a linearidade nem chega a ser o regime esperado. Escrito assim, parece um único limiar que muda de valor.

O custo é preciso: o `assessment_gate` da auditoria manda cobrar "a existência da não linearidade **e a distinção entre as texturas**, não o número como se fosse exato" (restrição (a)). A distinção entre as texturas era justamente a coisa que a forma anterior tornava ilegível.

**Correção aplicada:** os dois regimes separados em **lista de dois itens**, cada um nomeando sua textura, abertos por uma frase que anuncia que a resposta depende da textura e "são duas texturas com dois comportamentos distintos, que não se devem confundir". Acrescentado um fecho que diz o que se leva dali — "o que se leva daqui não é o número, é a distinção: a leitura 'cargabilidade proporcional a teor' só vale no regime disseminado e de baixo volume" —, que é a formulação da própria ressalva auditada. A ressalva de "ordem de grandeza, não constante física" está preservada literal, e o bloco de fatores petrofísicos passou a parágrafo próprio. Nenhum número alterado.

### 🟡 DID-M19-A03-QUADRANTES-009 — O melhor material de avaliação do módulo estava em prosa corrida
**Tipo:** estrutura escondida pela forma · **Onde:** a03, seção "Por que combinar os dois métodos é mais diagnóstico" · **Escopo:** correção local.

**Problema:** a seção apresenta três combinações mutuamente excludentes de resistividade × cargabilidade, cada uma com sua causa provável e sua consequência para a decisão de sondagem, dentro de **um único parágrafo**. É uma tabela de três linhas e quatro colunas escrita como texto seguido — o formato menos utilizável possível para um conteúdo cuja função é **discriminar entre casos**, e cujo uso imediato é o exemplo trabalhado que vem na página seguinte com exatamente essas três zonas. A auditoria chama este material de "o melhor material de avaliação do módulo" e o registra como o único dos três pares de sinal oposto que não precisou de nenhuma correção factual. Ele merecia forma melhor.

**Correção aplicada:** a prosa foi **mantida intacta** — ela argumenta, e o argumento tem valor —, e recebeu logo abaixo uma **tabela de consolidação** com as três combinações que o texto enuncia: resistividade, cargabilidade, causa mais provável, prioridade de sondagem. A tabela é aberta por uma instrução de estudo ("é esta tabela que o exemplo trabalhado a seguir executa, e vale relê-la antes dele"). **Nenhuma linha inventada:** o quarto quadrante (alta resistividade + baixa cargabilidade) não consta da tabela porque o texto não o enuncia — ver 🔵 S1.

### 🟡 DID-M19-A02-OBJETIVOPORFIRO-011 — O ponto de maior valor da a02 depois da auditoria não estava entre os resultados declarados
**Tipo:** conteúdo central sem objetivo declarado que o anuncie · **Onde:** a02, "Ao final você vai conseguir" · **Escopo:** correção local.

**Problema:** o cabeçalho da a02 prometia três resultados — propriedades medidas e contrastes típicos; induzida × remanente; profundidade da gamaespectrometria. Depois da auditoria, a aula ganhou um quarto conteúdo que é, pelo julgamento da própria auditoria, **o mais valioso do módulo**: a regra de sinal potássica/fílica e a armadilha do canal K. Ele é a espinha do exemplo trabalhado, ocupa um bullet inteiro do recap e é o item 1 e o item 3 dos `generator_warnings`. E não estava anunciado em lugar nenhum do cabeçalho.

É o inverso do "objetivo não coberto": aqui a seção existe e é boa, e falta o objetivo. O leitor que usa o cabeçalho para decidir onde prestar atenção — que é para isso que ele existe — é orientado a passar batido justamente pelo trecho de maior retorno.

**Correção aplicada:** quarto resultado acrescentado ao cabeçalho — "aplicar a regra de sinal do zoneamento de um pórfiro (qual alteração acrescenta e qual destrói magnetita) e explicar por que o canal de potássio sozinho não separa as duas". Nenhum fato novo; é a promessa do que a aula já entrega.

### 🟡 DID-M19-A01-CAMERA-012 — A analogia da câmera estava truncada e sugeria o oposto do que o parágrafo argumenta
**Tipo:** analogia que ensina modelo mental errado · **Onde:** a01, seção "O paradoxo resolução × profundidade", segunda razão · **Escopo:** correção local.

**Estava escrito:** *"É o análogo geofísico de tentar fotografar um objeto distante com uma câmera de altíssima resolução: a resolução do sensor deixa de ser o fator limitante muito antes da distância física ao objeto."*

**Problema:** dois defeitos somados. O primeiro é de redação — a oração final não fecha: "deixa de ser o fator limitante muito antes da distância física ao objeto" compara um fator a uma distância e não se resolve em nenhuma leitura. O segundo é pior e é do tipo mais insidioso que esta skill persegue: o parágrafo acabara de argumentar que **adensar estações não compra resolução** sobre um alvo profundo, porque a anomalia já chega alargada à superfície. A analogia, como escrita, dirige a atenção para a "distância física ao objeto" como o problema — e distância é justamente o que, na leitura ingênua, *se pode reduzir*. O leitor sai com o modelo de que o limite é circunstancial e contornável, quando o parágrafo inteiro existe para dizer que ele é necessário.

Analogia truncada é pior que analogia ausente, porque é o que fica na memória. E esta aula já traz um exemplo de como fazer certo: a analogia com o Módulo 14, no parágrafo anterior, foi reescrita pela auditoria dizendo explicitamente onde ela para ("o resultado prático é o mesmo, mas o mecanismo não").

**Correção aplicada:** reformulada para dizer o que o parágrafo diz — fotografar um objeto distante **através de ar quente e trêmulo**, onde trocar a câmera por outra de mais megapixels não devolve detalhe nenhum "porque o borrão já está no sinal que chega ao sensor, não no sensor", com a amarração explícita ("adensar estações sobre um alvo profundo tem o mesmo destino"). E, seguindo a forma da correção vizinha da auditoria, a analogia agora **diz onde quebra**: o borrão atmosférico é acidente que um dia melhor elimina; o alargamento da anomalia é consequência necessária da física de campo potencial, e nenhuma condição de campo o elimina. Nenhum fato novo — é a reformulação do que as duas frases anteriores do parágrafo já estabelecem.

### 🟡 DID-M19-A01-M14CABECALHO-013 — O cabeçalho da a01 ainda dizia "retomada aqui" depois de a auditoria rebaixar a identidade a analogia
**Tipo:** desalinhamento cabeçalho–corpo · **Onde:** a01, linha de pré-requisito · **Escopo:** correção local.

O achado 🟡 `AUD-M19-A01-M14ANALOGIA-016` corrigiu o corpo de "exatamente o mesmo compromisso" para "**análogo** — não idêntico", nomeando os dois mecanismos lado a lado. O cabeçalho continuava dizendo que a lógica do Módulo 14 é "**retomada aqui** para o par resolução-profundidade" — e "retomar" afirma continuidade do mesmo conteúdo, que é precisamente o grau de identidade que a auditoria desfez. Mesma família do achado `-005`: a correção factual não subiu até o cabeçalho.

**Correção aplicada:** "usada aqui como **analogia** para o par resolução-profundidade — o resultado prático coincide, mas o mecanismo físico é outro, e a aula diz onde a analogia para". Alinha o cabeçalho ao corpo auditado e prepara o leitor para a ressalva que vai encontrar.

### 🟡 DID-M19-A04-GREENFIELD-014 — "Greenfield" é o único termo de negócio do módulo que entra sem glosa, e ele carrega a conclusão sobre o GPR
**Tipo:** termo técnico usado antes de definido · **Onde:** a04, seção "GPR", último parágrafo, e recap · **Escopo:** correção local.

O termo aparece duas vezes e nunca é explicado, num módulo que glosa consistentemente seus termos na primeira ocorrência — "camp", "eddy currents", "percolação elétrica", "problema mal-posto", "stockwork" (agora). E ele não é decorativo: a frase inteira que define o papel do GPR no fluxo de trabalho depende dele. Um leitor que leia "greenfield" como genérico de "exploração" conclui que o GPR não serve para exploração, quando a aula diz algo bem mais específico e mais útil — que ele não serve para *achar* o depósito, e serve muito bem para caracterizar a cobertura sobre um alvo já localizado.

**Correção aplicada:** glosa em aposto na primeira ocorrência — "em área sem descoberta prévia, onde ainda se procura o depósito em vez de detalhar um já conhecido". Meia linha, e é a definição do termo, não uma afirmação nova sobre o GPR.

### 🟡 DID-M19-A06-COBERTURAPARCIAL-015 — O exemplo trabalhado cobra um viés que o corpo nunca ensinou, e o recap o recapitula
**Tipo:** exemplo que exige conceito não ensinado / recap que recapitula o que não está no corpo · **Onde:** a06, seção "O problema dos positivos raros", exemplo trabalhado e recap · **Escopo:** correção local.

**Problema:** o corpo da a06 ensina dois riscos, e os ensina bem: **sobreajuste** e **viés de amostragem de exploração**. O exemplo trabalhado então apresenta um terceiro, sem aviso: a camada de IP que cobre **8%** da área e, entrando no modelo como se fosse completa, ensina o algoritmo a associar "ausência de dado" a "ausência de depósito". A resolução o trata como se fosse o viés de amostragem já ensinado — e ele é parente próximo, mas não é o mesmo: um vive no **rótulo** (o que se sabe sobre a área), o outro na **entrada** (que camadas existem sobre a área).

O sintoma que confirma o diagnóstico está no recap: o quarto bullet ("A camada de evidência mais rica em dado não é necessariamente a mais confiável para treinamento regional se sua cobertura for parcial") **recapitula algo que não está no corpo** — só no exemplo. Um recap existe para destilar o que o corpo ensinou; quando ele traz conteúdo que o corpo não tem, o defeito não é dele, é da lacuna que ele está cobrindo.

**Correção aplicada:** um parágrafo novo ao fim da seção "O problema dos positivos raros", nomeando o **viés de cobertura das próprias camadas de evidência** como parente do viés de amostragem de exploração — "o mesmo raciocínio, deslocado do rótulo para a entrada" —, anunciando que o exemplo trabalhado vai cobrá-lo, e fechando com o que unifica os dois: "em ambos, uma decisão de **onde se foi olhar** entra no modelo disfarçada de fato geológico". **Nenhum conteúdo factual novo:** a afirmação já estava no exemplo trabalhado e no recap, e só faltava no corpo. O exemplo deixou de testar o que a aula não ensinou, e o quarto bullet do recap passou a recapitular de fato.

### 🟡 DID-M19-A06-NAVEGACAO-016 — A última aula do módulo não tinha a seção de retorno que as últimas aulas dos Módulos 17 e 18 têm
**Tipo:** convenção de navegação quebrada na única aula sem "Próxima aula" · **Onde:** a06, entre o recap e as Fontes · **Escopo:** correção local.

As cinco primeiras aulas do módulo fecham com "## Próxima aula" e um wikilink. A a06, por ser a última, não tem — e passava direto do recap para as Fontes, deixando o leitor num beco: nenhum link adiante, nenhum link de volta, nenhuma indicação de que o módulo acabou ali por desenho e não por arquivo truncado. As últimas aulas dos Módulos 17 (a06) e 18 (a05) resolvem isso com uma seção **"## Anterior"** e o backlink da aula precedente; a do M17 acrescenta ainda um "## Encerramento do módulo".

**Correção aplicada:** seção "## Anterior" acrescentada na posição em que os Módulos 17 e 18 a colocam, com o backlink da a05, mais uma linha declarando que esta é a última aula do módulo e oferecendo o retorno ao hub. Nenhum conteúdo; o fecho conceitual do módulo já existia e é bom (último bullet do recap).

### 🟡 DID-M19-A05-OBJETIVO3D-017 — A quinta seção da a05 não correspondia a nenhum resultado declarado no cabeçalho
**Tipo:** conteúdo órfão em relação aos objetivos da aula · **Onde:** a05, "Ao final você vai conseguir" e seção "Modelos 3D" · **Escopo:** correção local.

O cabeçalho da a05 prometia três resultados: direto × inverso e a não unicidade; regularização e estrutura mínima; o caso concreto da petrofísica. A **quinta seção de conteúdo — "Modelos 3D: da inversão 1D e 2D ao volume completo" — não serve a nenhum dos três.** Ela serve ao objetivo do **módulo** (`oa04`, "explicar os fundamentos, as vantagens e as limitações da inversão geofísica"), de modo que não é conteúdo órfão em sentido estrito, e o `mapa_objetivo_secao` está correto. Mas é órfã em relação aos resultados que a própria aula declarou, e ela carrega um ponto que merece ser prometido: que aumentar a dimensão do modelo **não** resolve a ambiguidade.

**Correção aplicada:** quarto resultado acrescentado — "situar a inversão 3D em relação à 1D e à 2D, explicando por que aumentar a dimensão do modelo não elimina a ambiguidade". Nenhum fato novo; é a promessa do que a seção já entrega.

### 🟡 DID-M19-A05-PARAGRAFO3D-018 — A seção de modelos 3D era uma única frase de nove linhas
**Tipo:** densidade irregular / ausência de pausa · **Onde:** a05, seção "Modelos 3D", parágrafo único · **Escopo:** correção local.

A seção inteira era **um parágrafo com duas frases**, a segunda delas com nove linhas, dois parênteses de remissão a outros módulos e três movimentos conceituais encadeados por travessão: que a 3D não elimina a ambiguidade; que ela permite inversão conjunta e restrição por modelo geológico prévio; e que isso é a mesma regularização sob outra forma. É o fecho da melhor aula do módulo, e o leitor chega nele já com cinco seções de carga.

O ponto enterrado ali importa: **"passar de 2D para 3D não resolve a ambiguidade"** contraria a expectativa natural de qualquer leitor (mais dimensões, mais informação) e é exatamente o tipo de correção de intuição que material didático precisa marcar, não sussurrar no meio de uma frase longa.

**Correção aplicada:** dividida em dois parágrafos, **sem acrescentar nem remover conteúdo**: (i) a evolução histórica 1D → 2D → 3D e os códigos; (ii) um parágrafo próprio aberto por "Aqui vale desfazer uma expectativa natural: **passar de 2D para 3D não resolve a ambiguidade**", seguido do que a 3D de fato ganha e do fecho que reduz tudo a regularização. A frase auditada sobre reduzir o espaço de modelos a um subconjunto geologicamente plausível está preservada.

### 🟡 DID-M19-A03-STOCKWORK-010 — "Stockwork" aparece só dentro do exemplo trabalhado, sem glosa
**Tipo:** termo técnico usado antes de definido · **Onde:** a03, Exemplo trabalhado, Zona C · **Escopo:** correção local.

O termo entra uma única vez, na resolução da zona que o exemplo elege como prioritária, e nunca foi apresentado — nem nesta aula, nem nas duas anteriores do módulo. Está ali como parte da justificativa da conclusão ("sulfeto mais concentrado, possivelmente com textura de veio ou stockwork denso"), de modo que o leitor precisa avaliar um argumento cujo termo ele não recebeu. Mesmo defeito de `DID-M18-A03-SUBPLACAGEM-013`, e num módulo que glosa todos os seus outros termos.

**Correção aplicada:** glosa em aposto — "uma malha densa de veios finos entrecruzados, em vez de grãos isolados na matriz". A formulação em contraste ("em vez de") é deliberada: é a oposição com o disseminado que faz o termo trabalhar no argumento da Zona C.

### 🟡 DID-M19-PALAVRAS-019 — Os seis blocos `palavras_corpo` estavam desatualizados, o da a02 em 39%
**Tipo:** metadado que desinforma quem planeja o estudo · **Onde:** bloco de metadados das seis aulas · **Escopo:** correção local.

| Aula | Declarado | Real (antes) | Real (após esta revisão) |
|---|---|---|---|
| a01 | 1.780 | 1.951 | **2.017** |
| a02 | 1.690 | 2.352 | **2.480** |
| a03 | 1.750 | 2.016 | **2.240** |
| a04 | 1.720 | 2.174 | **2.287** |
| a05 | 1.780 | 2.050 | **2.070** |
| a06 | 1.780 | 1.882 | **1.997** |

As seis subestimavam, e a soma declarada (10.500) ficava **2.590 palavras abaixo** da real. Parte do desvio é da auditoria, que acrescentou texto sem atualizar os blocos; parte é anterior a ela. O número importa porque é o que qualquer passagem posterior — inclusive a decisão de divisão do achado `-004` — lê para julgar carga: com 1.690 declaradas, a a02 parecia a aula **mais leve** do módulo, quando é a mais pesada por margem clara. Foi essa inversão que quase escondeu o achado `-004`.

**Correção aplicada:** os seis valores sincronizados com a contagem real pós-revisão. Nenhum outro campo do bloco de metadados foi tocado.

---

## Sugestões (não são defeitos)

- **🔵 DID-M19-S1 — O quarto quadrante resistividade × cargabilidade não existe no material, e a tabela nova torna a lacuna visível.** A a03 enuncia três das quatro combinações; falta **alta resistividade + baixa cargabilidade**, que é o caso da rocha estéril, resistiva e sem sulfeto — o "fundo" contra o qual as outras três se destacam. A tabela que esta revisão acrescentou tem três linhas por isso, e a ausência agora fica evidente ao leitor, o que é preferível a escondê-la. **Não a preenchi porque enunciar esse quadrante é conteúdo factual novo**, que não passou pelo auditor — precisamente o que esta skill não faz. É uma linha de tabela e uma oração de corpo, e fecharia o que a auditoria chama de "o melhor material de avaliação do módulo". Recomendo ao orquestrador, com passagem pelo `auditor-cientifico` antes de entrar.
- **🔵 DID-M19-S2 — Se este módulo receber uma única figura, que seja o zoneamento de alteração de pórfiro da a02.** Seis aulas, zero figuras. O candidato é disparado o mais forte do módulo: um esquema em planta com o núcleo potássico magnetítico, o anel fílico de baixo magnético e o halo propilítico externo, com os canais K e Th sobrepostos, resolveria de uma vez o conteúdo que (a) custou o único vermelho da auditoria, (b) é o item 1 e o item 3 dos `generator_warnings`, (c) é a espinha do exemplo trabalhado e (d) é intrinsecamente **espacial** — anéis concêntricos descritos em prosa. As correções `-001` e `-011` fazem o que é possível fazer com texto; uma figura faria mais, com menos. **Fora do escopo desta skill** (produzir conteúdo), registrado para o orquestrador.
- **🔵 DID-M19-S3 — Se a a02 for dividida, a recomendação de formato da auditoria precisa ser revista antes de gerar o questionário.** A inclinação de **3 parciais + 1 cumulativo** registrada em `partials_recommendation_preliminary` assume as fronteiras a01 / a02 / a03+a04 / a05+a06, com seis aulas. Dividir a a02 muda a primeira fronteira e o `oa02` passa a ser coberto por duas aulas. A decisão continua sendo do `gerador-de-questionarios`, mas ela **não pode ser tomada antes** da decisão do achado `-004`.
- **🔵 DID-M19-S4 — Os blocos de metadados em comentário HTML das aulas não fazem parse como YAML, e isso é do curso inteiro, não deste módulo.** O campo `mapa_objetivo_secao` usa a forma `oa01: "seção A" + "seção B"`, que é um escalar entre aspas seguido de mais conteúdo — sintaxe inválida. Verifiquei os **76 blocos de metadados de aula** dos módulos auditados e **os 76 falham igualmente**: é convenção do curso, anterior a este módulo e a esta passagem, e não foi introduzida nem agravada aqui. Registrado apenas para que ninguém a atribua a esta revisão. Pertence ao `validador-estrutural-do-curso` decidir se a convenção muda ou se o schema passa a aceitá-la — junto da observação sobre formato de wikilink que a auditoria do M19 herdou do M18 e que segue pendente.

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo | Avaliado em | Observação |
|---|---|---|---|---|
| `oa01` — selecionar método por escala e alvo; compromisso resolução × profundidade | a01 (integral: 3 seções) | sim (a01, três decisões em cascata de escala) | — *não verificável: sem questionário* | coberto; analogia da câmera refeita (`-012`) e grau de identidade com o M14 alinhado ao corpo auditado (`-013`) |
| `oa02` — interpretar gravimetria, magnetometria e gamaespectrometria como assinatura de sistema mineral | a02 (integral: 3 seções) | sim (a02, zoneamento de pórfiro por magnetometria + gamaespectrometria) | — *não verificável* | coberto; **a regra de sinal do pórfiro passou a constar dos resultados declarados** (`-011`), que era a lacuna mais cara da tabela. Carga acima do orçamento — achado `-004`, em aberto |
| `oa03` — distinguir métodos elétricos dos eletromagnéticos e a que propriedade cada um responde | a03 (4 seções) + a04 (4 seções) | sim, dois (a03, três zonas por resistividade × cargabilidade; a04, três sistemas por profundidade e cobertura condutora) | — *não verificável* | coberto **em conjunto** pelas duas aulas; a restrição de escopo da comparação TDEM × FDEM subiu ao cabeçalho (`-005`) e o exemplo passou a declarar em que base compara (`-006`) |
| `oa04` — fundamentos, vantagens e limitações da inversão e dos modelos de prospectividade | a05 (5 seções) + a06 (4 seções) | sim, dois (a05, dois modelos igualmente válidos; a06, sete camadas e seis positivos) | — *não verificável* | coberto **em conjunto**; a seção de modelos 3D da a05 passou a ter resultado declarado que a anuncie (`-017`) |

**Conteúdo órfão:** nenhum. Todas as seções substantivas das seis aulas estão mapeadas a um objetivo do módulo pelo `mapa_objetivo_secao`, e a verificação contra o enunciado de cada objetivo não encontrou nenhuma seção que sirva à aula mas não ao objetivo — ao contrário do Módulo 18, onde a seção de maré terrestre era esse caso-limite. O único desalinhamento desta família foi interno à a05 (`-017`), entre a seção e os resultados **da própria aula**, não entre a seção e o objetivo do módulo.

**Alinhamento com a avaliação — não verificável nesta passagem**, porque questionário e baralho ainda não existem. O que foi verificado em seu lugar, e é o que pode ser verificado agora: **cada "Ao final você vai conseguir" contra o corpo da respectiva aula**. Três divergências foram encontradas e corrigidas, e as três apontavam na direção que mais custa depois — o cabeçalho da a04 prometia mais do que o corpo corrigido sustenta (`-005`), e os cabeçalhos da a02 e da a05 prometiam menos do que o corpo entrega (`-011`, `-017`). Como é esse campo que o `gerador-de-questionarios` lê como enunciado do cobrável, corrigi-los agora previne o desalinhamento em vez de remediá-lo.

## Propagação a material derivado

| Arquivo | Alterado? | O quê |
|---|---|---|
| `19-...-questionario.md` | **não existe** | Nada a propagar. As correções `-005`, `-011` e `-017` alteram enunciados de objetivo declarado e, se o questionário já existisse, exigiriam reconferência — não exigem, porque ele será gerado a partir da versão já corrigida. |
| `19-...-flashcards.md` / `.csv` | **não existem** | Nada a propagar, nada a reimportar no Anki. |
| `19-...-auditoria.md` / `.json` | **não** | Nenhum achado desta revisão contradiz, revisa ou reabre achado da auditoria. Os quatro achados que incidiram sobre trecho criado por ela (`-001`, `-002`, `-003`, `-008`) foram exclusivamente de forma. |
| `19-...-modulo.md` (hub) | **sim** | Linha "Revisão didática: pendente" substituída pelo resumo desta passagem, com o achado em aberto nomeado. O `status` do módulo, o `current_module`, o `next_action`, o dashboard, o `_curso.md` e o progresso do aluno **não** foram tocados — o fechamento é etapa do `geo-operacional`. |
| `course-state.yaml` | **sim** | Bloco `didactic_review` do módulo 19 acrescentado entre `audit` e `assessment`, mesma estrutura dos módulos 17 e 18. |

**Advertência para quem gerar o questionário e os flashcards:** os `generator_warnings` da auditoria continuam **integralmente válidos** — nenhum valor numérico, nenhuma polaridade e nenhuma citação foi alterada nesta passagem. Três pontos desta revisão os complementam: (a) a regra de sinal do pórfiro e a armadilha do canal K agora constam do cabeçalho da a02, o que autoriza cobrá-las como objetivo declarado e não apenas como conteúdo de corpo; (b) a distinção entre os limiares de 20% (disseminado) e 30% (veio/maciço) ficou legível, o que torna cobrável a restrição (a) do `assessment_gate` — antes ela era cobrável em teoria e ilegível na prática; (c) o cabeçalho da a04 passou a carregar a restrição de bobina rebocada, de modo que **um item gerado a partir do enunciado do objetivo não nasce mais irrestrito**, que era o risco silencioso mais próximo de reintroduzir o erro que a auditoria desfez.

## Verificação mecânica feita ao fim da passagem

- **Correções da auditoria, reverificadas depois de cada edição.** A correção vermelha está literal na a02 nos cinco pontos em que a auditoria a aplicou: "potássica ... **acrescenta** magnetita ... **alto** magnético", "fílica/sericítica ... **destrutiva de magnetita** ... **baixo** magnético, tipicamente como um anel", a propilítica preservando ou repondo, a armadilha do canal K no corpo, no exemplo trabalhado e no recap, e a alegação `...ZONEAMENTOPORFIRO-004` intacta. As sete correções de atribuição de fonte foram conferidas uma a uma nas listas de Fontes e nas alegações: Hronsky & Groves em *AJES* 55(1), 3-12; Wyborn et al. no AusIMM/Darwin, 109-115; Parasnis **1956**, *Geophysical Prospecting* 4(3), 249-278; *Minerals* 12(5), 583 sob **Prikhodko et al.**; Carranza & Laborte desdobrado nos **dois** artigos; Wu et al. (2022) no lugar da entrada sem título; e a entrada de Chen et al. (2019) com a advertência de escopo ("**não** para uma vantagem do TDEM") preservada palavra por palavra. Os valores auditados também: janelas 1,37-1,57 / 1,66-1,86 / 2,41-2,81 MeV; picos 1,46 / 1,76 / **2,61**; densidades minerais com galena 7,4-7,6 e esfalerita 3,9-4,1; corpo de minério 3,5-4,5; susceptibilidade em mais de cinco ordens com magnetita ~5 SI; **pirrotita monoclínica (Fe₇S₈)** nas três ocorrências magnéticas, com a hexagonal antiferromagnética; calcopirita ~1-10⁴ S/m, pirita 10⁻³-1, pirrotita 10³-10⁵; DIGHEM ~900 Hz-56 kHz e RESOLVE ~400 Hz-140 kHz; teorema da casca de Newton com as três condições. **Nenhuma perda, nenhuma duplicação, nenhuma reformulação.**
- **Estrutura das seis aulas.** Nenhuma seção `###` de conteúdo foi criada, removida ou renomeada em nenhuma das seis aulas. A contagem de seções `##` passou de 5 em cinco aulas e **4 na a06** para **5 nas seis** — a diferença é a seção "## Anterior" acrescentada pelo achado `-016`, que é exatamente o que faltava para a a06 alcançar a estrutura das demais e a das últimas aulas dos Módulos 17 e 18. Os blocos de metadados em comentário HTML estão intactos nos seis arquivos, com o único campo alterado sendo `palavras_corpo` (achado `-019`); os 23 blocos de `alegacoes_auditaveis` seguem com o mesmo `claim_id`, `claim`, `risk` e `source` que a auditoria deixou.
- **`course-state.yaml`.** Backup gravado em `course-state.yaml.bak-20260913-pre-m19-didactic` **antes** de qualquer edição. Parse por `yaml.safe_load` OK depois da escrita. O bloco `didactic_review` do módulo 19 usa a mesma estrutura de campos dos módulos 17 e 18, na mesma posição (entre `audit` e `assessment`), com `status: completed` (nunca `complete`) e uma nota adicional que a ordem correta da cadeia justifica (`chain_order_note`, que aqui registra o **oposto** do que registrava no M18).
- **Wikilinks introduzidos.** Os três links novos foram conferidos contra o disco: `24-machine-learning-geociencias/24-machine-learning-geociencias-modulo` (achado `-007`), `19-geofisica-exploracao-mineral-aula-05-inversao-ambiguidade-regularizacao` e `19-geofisica-exploracao-mineral-modulo` (achado `-016`). Os três resolvem.

## Encaminhamentos ao usuário

1. **Decidir sobre a carga da Aula 02** (achado 🟠 `DID-M19-A02-CARGA-004`) — **o único achado não corrigido**. As duas opções estão detalhadas no achado, com o argumento de cada lado. Em resumo: dividir **nunca será mais barato** do que agora (zero material derivado), mas o **exemplo trabalhado não sobrevive ao corte**, porque a discriminação de maior valor do módulo só existe na interseção entre magnetometria e gamaespectrometria. **Se a decisão for não dividir, corrigir "~30 min" para "~40 min"** no cabeçalho da a02 e no hub — isso não pode ser esquecido, é o dano concreto do achado para quem planeja o estudo.
2. **Não gerar o questionário antes da decisão 1** (🔵 S3). A recomendação de 3 parciais + 1 cumulativo pressupõe 6 aulas e a fronteira a01 / a02.
3. **Avaliar a figura de zoneamento de pórfiro da a02** (🔵 S2). É a intervenção de maior retorno pedagógico disponível neste módulo, e a única que esta revisão não podia fazer.
4. **Avaliar o quarto quadrante da a03** (🔵 S1), lembrando que ele exige passagem pelo `auditor-cientifico` antes de entrar, por ser conteúdo factual novo.
