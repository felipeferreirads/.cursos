# Revisão didática — Módulo 17: Geofísica marinha e de bacias sedimentares

**Data:** 2026-09-10
**Modo:** `review-and-fix` (melhorias aplicadas)
**Escopo:** as 5 aulas do módulo, mais o hub
**Veredito:** **bem ensinado com ressalvas** — 9 achados, 8 corrigidos e 1 encaminhado ao orquestrador. Nenhum salto de pré-requisito, nenhuma analogia que ensine modelo mental errado, nenhum objetivo de aprendizagem sem seção que o ensine.

## Resumo

🔴 0 bloqueiam · 🟠 3 prejudicam · 🟡 6 atrito · 🔵 3 sugestões

**Carga estimada do módulo:** 5 aulas · ~11.200 palavras de corpo · 4 objetivos de aprendizagem · 3 exemplos trabalhados numéricos e 2 interpretativos. A distribuição é desigual: a a03 e a a05 ficam confortavelmente em 30 min; a a01 e a a02 são densas em nomenclatura mas leves em raciocínio novo; **a a04 estoura**, e é o único achado que esta skill não pode resolver sozinha.

## O que o módulo já fazia bem, antes da revisão

Registrar isto importa tanto quanto listar defeitos — é o padrão que as próximas aulas devem imitar.

1. **Cada aula declara de que aula anterior depende e por quê, em prosa.** A a05 é o melhor exemplo: ela não só lista as Aulas 01-04 como pré-requisito, mas diz o que vai fazer com cada uma ("integra a classificação de bacias e os estágios tectonossedimentares com os métodos sísmicos e de campos potenciais num único exercício de avaliação").
2. **O módulo declara honestamente onde é revisão e onde é conteúdo novo.** A a01 abre dizendo que boa parte dela retoma o Módulo 10 de forma condensada, e o hub repete isso nos "Pontos de dificuldade". Material autodidata quase nunca faz isso, e o efeito é o leitor saber onde acelerar e onde parar.
3. **A a02 traz um quadro dedicado a uma controvérsia real, com a advertência sobre mudança de escala de tempo.** Ensinar que 125 Ma "na base do Aptiano" hoje é Barremiano é ensinar *como a literatura envelhece* — uma competência transferível, não um fato.
4. **Os três exemplos trabalhados numéricos usam números que o corpo da aula já justificou**, e nenhum deles para no resultado: os três voltam ao argumento central. O da a03 é exemplar, porque a pergunta (b) força o aluno a validar o resultado contra o contexto geológico, em vez de aceitar o número.
5. **A a05 fecha o módulo inteiro numa seção `## Encerramento do módulo`**, no mesmo nível hierárquico do exemplo trabalhado — a posição certa, e a mesma correção que o Módulo 16 precisou receber na revisão anterior. O padrão pegou.
6. **Densidade conceitual apropriada em quatro das cinco aulas.** Nenhuma delas, exceto a a04, introduz mais de quatro conceitos genuinamente novos.

---

## Achados

### 🟠 DID-M17-A01-OBJETIVOVISUAL-001 — A aula promete uma competência visual que ela não tem como ensinar
**Tipo:** objetivo não coberto (parcialmente) · **Onde:** a01, cabeçalho "Ao final você vai conseguir" · **Escopo:** correção local.

**Estava escrito:** *"reconhecer os estilos estruturais extensionais típicos de riftes (falhas normais, blocos basculados, meio-grabens) **numa seção sísmica ou num mapa estrutural**"*.

**Problema:** a a01 não contém uma única seção sísmica, um único mapa estrutural, nem qualquer figura. O exemplo trabalhado descreve as geometrias **em palavras** — e descreve bem. A competência que a aula efetivamente ensina é atribuir uma sequência ao estilo estrutural a partir de uma **descrição** de geometria e relação com falhamento; a leitura direta de uma seção sísmica é o que a a03 torna possível, duas aulas adiante. Do ponto de vista de quem lê pela primeira vez, isso produz uma falha silenciosa: o leitor termina a aula, não se sente capaz de ler uma seção sísmica, e conclui que não aprendeu — quando na verdade aprendeu exatamente o que a aula ensinou, e a promessa é que estava errada.

Repare que a a02, ao lado, formula o mesmo tipo de promessa **corretamente**: "posicionar qualquer sequência sedimentar da margem brasileira num dos quatro estágios **a partir de sua litologia, geometria e relação com falhamento**". O defeito é local à a01, não do módulo.

**Correção aplicada:** a promessa foi reformulada para o que a aula entrega, com remissão explícita a onde a leitura sísmica é adquirida: "atribuir uma sequência sedimentar ao estilo estrutural extensional que a controla (…) a partir da descrição de sua geometria e de sua relação com o falhamento — a leitura direta dessas mesmas geometrias numa seção sísmica é o que a Aula 03 acrescenta". *Horst* e *rollover* foram acrescentados à lista, porque a aula os ensina e a promessa os omitia.

### 🟠 DID-M17-A01-CONVITEAPULAR-002 — A aula autoriza o leitor a pular justamente a seção de maior risco
**Tipo:** estrutura / sinalização enganosa · **Onde:** a01, fim da seção "O que este módulo assume e o que ele acrescenta" · **Escopo:** correção local.

**Estava escrito:** *"Se você concluiu o Módulo 10 recentemente, sinta-se à vontade para ler esta seção rapidamente e ir direto ao Exemplo trabalhado."*

**Problema:** o convite não distingue entre as seções, e o que fica **entre** aquele parágrafo e o exemplo trabalhado inclui a seção de estilos estruturais extensionais — que contém o parágrafo sobre *rollover* e arrasto reverso. Esse parágrafo é, por documentação do próprio curso, o ponto mais lembrado ao contrário de todo o bloco: a auditoria do Módulo 10 teve de corrigir exatamente essa geometria invertida (achado 🔴 6 daquele módulo), e a auditoria deste módulo verificou o parágrafo linha a linha justamente por isso. Dizer a um leitor que já estudou M10 que ele pode pular é dizê-lo precisamente a quem tem a versão invertida armazenada na memória e nenhuma razão para suspeitar dela.

Esse é o caso em que a redundância deliberada vale mais que a economia: quem já sabe é quem mais precisa reler.

**Correção aplicada:** o convite passou a ser seletivo — libera a leitura acelerada dos mecanismos de subsidência e do contexto de placas, e **retém explicitamente** a seção de estilos estruturais: "Não pule, porém, a seção sobre estilos estruturais extensionais: o parágrafo sobre o *rollover* anticlinal trata de uma geometria que é rotineiramente lembrada ao contrário — inclusive por quem já a estudou — e que volta como trapa estrutural na Aula 05. Se você for ler uma só coisa desta aula com atenção, que seja aquele parágrafo."

### 🟠 DID-M17-A04-CARGA-003 — A Aula 04 excede o orçamento de 30 minutos, e a correção é dividir
**Tipo:** excesso de conceitos novos / duração · **Onde:** a04, aula inteira · **Escopo:** **exige dividir a aula — decisão do `gerador-de-curso-modular`, não corrigida aqui.**

**Problema:** a a04 é a aula mais longa do módulo (~2.350 palavras declaradas, o maior arquivo dos cinco) e carrega cinco blocos conceituais genuinamente novos, não quatro:

1. gravimetria a bordo de plataforma em movimento (estabilização, ruído de casco) e correção de Eötvös marinha;
2. correção de Bouguer **marinha** e o par ar-livre/Bouguer com sua tabela;
3. assinatura gravimétrica dos elementos de uma margem divergente (COB, sal, depocentros);
4. anomalias magnéticas lineares da crosta oceânica e datação por correlação com a escala de polaridade;
5. fluxo de calor, modelo GDH1 com suas duas equações, idade de selamento, e a ponte para maturação térmica.

Os blocos 1-3 e o bloco 5 não compartilham quase nada: um é campo potencial gravitacional com suas correções de aquisição, o outro é estrutura térmica da litosfera com um modelo próprio e uma família de números próprios. O leitor que chega ao fluxo de calor já gastou o orçamento de atenção em três cadeias de correção gravimétrica. A auditoria científica, ao acrescentar as equações do GDH1 e a tabela de réguas térmicas — necessárias para consertar três achados amarelos —, tornou a aula mais **correta** e um pouco mais **longa**, o que agrava este achado em vez de aliviá-lo.

**Por que não corrigi aqui:** a regra desta skill é que sobrecarga cognitiva não se conserta com mais explicação, e que dividir uma aula é decisão do orquestrador. Também há um custo real: dividir a a04 renumera a a05 e mexe no hub, no `course-state.yaml` e nos mapas de objetivo.

**Encaminhamento ao `gerador-de-curso-modular`:** avaliar a divisão da a04 em duas — **"Gravimetria e magnetometria marinhas em margens divergentes"** (blocos 1-4, com o exemplo trabalhado atual, que é inteiramente de campos potenciais) e **"Fluxo de calor e a estrutura térmica de uma margem divergente"** (bloco 5, que já tem material próprio suficiente: GDH1, as duas equações, a tabela de réguas, o selamento hidrotermal, e a ligação com a subsidência térmica da a01-a02 e com a maturação da a05). O corte é limpo: o exemplo trabalhado atual trata as três zonas crustais por critério magnético e gravimétrico e só usa o fluxo de calor no parágrafo final, que migraria inteiro.

**Mitigação aplicada enquanto a decisão não vem:** a seção de fluxo de calor, que era um único parágrafo-muro, foi quebrada em quatro blocos com um destaque para as equações e uma tabela de valores de referência — ver DID-M17-A04-PARAGRAFOMURO-006. Isso não reduz a carga, mas dá pontos de parada.

### 🟡 DID-M17-A01-PREREQ-004 — Pré-requisito declarado não é o que a aula realmente usa
**Tipo:** pré-requisito declarado mas não usado · **Onde:** a01, cabeçalho · **Escopo:** correção local.

O cabeçalho declarava como pré-requisito o Módulo 15 (petrofísica), afirmando que "esta aula assume que você já sabe como densidade, velocidade sísmica e demais propriedades físicas das rochas variam com litologia e compactação". A a01 invoca o M15 **uma vez**, de passagem, numa remissão sobre compactação. O antecedente conceitual real da aula é o **Módulo 10** — de onde vêm os quatro mecanismos de subsidência, todo o vocabulário muro/teto, meio-graben, graben, horst e *rollover* —, e o M10 aparecia apenas como menção opcional no fim do parágrafo. O leitor que lê o cabeçalho literalmente vai revisar a coisa errada antes de começar.

**Correção aplicada:** o cabeçalho passou a nomear o M10 como antecedente conceitual direto e o M15 como pré-requisito formal do módulo, "acionado mais adiante, nas Aulas 03 e 04, quando densidade, velocidade sísmica e compactação voltam como as propriedades que a geofísica de fato mede" — o que também é verdade e agora está no lugar certo. Acrescentada a garantia de autossuficiência: cada termo estrutural é redefinido no ponto em que aparece, de modo que quem não cursou o M10 consegue acompanhar. Isso foi verificado termo a termo e é verdade.

### 🟡 DID-M17-A03-PREREQ-005 — Falta a ponte para o Módulo 11, que é o antecedente do método
**Tipo:** pré-requisito não declarado (sem salto) · **Onde:** a03, cabeçalho · **Escopo:** correção local.

A a03 usa "impedância acústica" na primeira frase da primeira seção, sem definição, e trata a cobertura CDP como algo que o leitor reconhece ("é o mesmo princípio de CDP usado na sísmica terrestre"). **Não é um salto de pré-requisito:** impedância acústica é ensinada no M15 a02 — declarado — e no M11 a01, e o princípio do CDP é explicado inline com suficiência. Mas o **Módulo 11 (Sismoestratigrafia)**, que é o antecedente direto do método sísmico de reflexão nesta progressão, não é mencionado em lugar nenhum da aula. Em um módulo cuja melhor virtude é declarar de onde vem cada coisa, esse é um silêncio destoante — e custa ao leitor a informação de *o que exatamente é novo aqui*.

**Correção aplicada:** o cabeçalho passou a nomear os dois antecedentes e o que cada um entrega, e a dizer explicitamente o que a aula acrescenta a eles: "como essas ondas são geradas, propagadas e registradas quando fonte e receptores estão em movimento sobre 2 km de água, e o que a coluna d'água faz com o sinal". Impedância acústica foi nomeada no cabeçalho como termo herdado do M15, com a definição entre parênteses (produto densidade × velocidade), de modo que quem não lembra não trava na primeira frase.

### 🟡 DID-M17-A03-STREAMER-006 — Definição circular de "grupo" e "canal"
**Tipo:** definição circular / termo não explicado · **Onde:** a03, seção "Streamers" · **Escopo:** correção local.

**Estava escrito:** *"cada um contendo centenas a milhares de hidrofones agrupados em **grupos** regularmente espaçados ao longo de **canais individuais**"*.

**Problema:** a frase usa três termos técnicos — grupo, canal, e implicitamente traço — sem dizer o que nenhum deles é, e a construção "agrupados em grupos … ao longo de canais" é circular. O leitor de primeira viagem não consegue extrair a ideia central, que é simples e importante: **os hidrofones não são lidos um a um**. É exatamente essa ideia que explica por que um streamer com milhares de hidrofones produz algumas centenas de traços, e por que existe um limite de resolução lateral associado ao comprimento do grupo — que a seção seguinte, sobre offset e CDP, já pressupõe.

**Correção aplicada:** parágrafo reescrito para expor a cadeia hidrofone → grupo → canal → traço, dizendo que é o centro do grupo que define a posição do receptor na geometria e que é o comprimento do grupo que estabelece a menor feição lateral amostrável. Nenhum fato novo foi introduzido: são as mesmas entidades que a redação anterior já nomeava, agora com a relação entre elas explícita.

### 🟡 DID-M17-A04-PARAGRAFOMURO-007 — A seção de fluxo de calor era um único parágrafo-muro
**Tipo:** densidade irregular · **Onde:** a04, "Fluxo de calor: o relógio térmico da margem divergente" · **Escopo:** correção local.

A seção condensava, num só parágrafo: a definição de fluxo de calor e sua unidade; o mecanismo de resfriamento da litosfera oceânica; o modelo GDH1 e o que ele substituiu; a lei de semiespaço; a circulação hidrotermal e a idade de selamento; o patamar assintótico; e **seis** valores numéricos de referência de domínios diferentes (oceânico jovem, oceânico antigo, cratônico arqueano, cratônico proterozoico, média continental, média oceânica). Seis números de categorias distintas correndo dentro de um parágrafo, separados por vírgulas e parênteses, é o formato em que eles menos se fixam e mais se confundem entre si.

**Correção aplicada:** a seção foi dividida em quatro blocos (definição e mecanismo → o modelo e suas equações → as duas idades que se confundem → os valores de referência), com as equações do GDH1 em destaque e os seis números convertidos numa **tabela de réguas de ordem de grandeza**, seguida de uma frase que diz como lê-la e qual é o padrão que ela revela. Nenhum conteúdo foi acrescentado nem removido — só reorganizado. (As equações e a correção do valor de 60 Ma vieram da auditoria científica, não desta revisão.)

### 🟡 DID-M17-A02-RECAPBULLET-008 — O primeiro bullet do recap deixou de ser um recap
**Tipo:** recap que não recapitula · **Onde:** a02, "Recap relâmpago" · **Escopo:** correção local.

O bullet de abertura carregava, numa só frase: os quatro estágios, suas idades numéricas, a ressalva sobre Chang et al., a diacronia norte-sul, a versão da carta ICS e a advertência sobre literatura anterior a 2021. Um recap existe para ser relido em trinta segundos antes de uma prova; um bullet de seis linhas não é relido, é pulado. O problema piorou com as correções da auditoria científica, que legitimamente acrescentaram a ressalva de escopo.

**Correção aplicada:** dividido em dois bullets com funções distintas — um para a **sequência** dos quatro estágios (limpo de números) e outro, intitulado "As idades, e a armadilha de escopo que elas escondem", para toda a camada numérica. Os dois juntos dizem exatamente o que o bullet único dizia, e cada um cabe num fôlego.

### 🟡 DID-M17-A05-LISTAESCONDIDA-009 — Uma lista de quatro itens escrita como parágrafo único
**Tipo:** estrutura · **Onde:** a05, "Da geofísica à decisão exploratória" · **Escopo:** correção local.

A seção enumerava quatro métodos e o papel de cada um na decisão exploratória, encadeados por ponto e vírgula num parágrafo de doze linhas. O conteúdo é uma lista paralela de quatro itens — método → contribuição — e a forma de parágrafo esconde esse paralelismo, que é justamente o que a seção quer ensinar. Esta é a seção de síntese que amarra as Aulas 03 e 04 à avaliação de recursos; se há um lugar do módulo em que a estrutura deve saltar aos olhos, é este.

**Correção aplicada:** convertida em lista de quatro itens, cada um encabeçado pelo método e pela **pergunta exploratória que ele responde** (*onde estão reservatório, selo e trapa? / até onde vai a bacia e onde está o sal que a sísmica não enxerga? / a geradora chegou a gerar, e quando? / dá para perfurar aqui em segurança?*). O texto de cada item é o mesmo da redação anterior; a pergunta em itálico é o único acréscimo, e é reformulação do que o próprio item já dizia.

### 🟡 DID-M17-A02-HALOCINESE-010 — "Halocinese" usado sem glosa
**Tipo:** termo técnico usado antes de definido · **Onde:** a02, "Segmentação lateral" · **Escopo:** correção local.

O termo aparece uma vez ("sustenta halocinese intensa"), sem definição, num módulo em que todos os demais termos técnicos recebem glosa na primeira ocorrência. O contexto imediato fala de "tectônica salífera" e o leitor provavelmente infere a equivalência, mas inferir não é saber, e o termo reaparece implicitamente na a05 (diápiros, almofadas, falhas de descolamento).

**Correção aplicada:** glosa de meia linha na primeira ocorrência — "o fluxo do sal no estado sólido sob a carga dos sedimentos que o cobrem, que é o que produz diápiros, almofadas e minibacias".

---

## Sugestões (não são defeitos)

- **🔵 DID-M17-HUB-S1 — O objetivo `oa04` acumula duas competências distintas.** "Interpretar mapas gravimétricos, magnéticos e de fluxo de calor de bacias **e** avaliar o potencial de recursos minerais e energéticos associado" são duas coisas, ensinadas em duas aulas diferentes (a04 e a05). Funciona, mas torna a matriz de avaliação ambígua: uma questão sobre trapas e uma questão sobre anomalia de Bouguer marcam o mesmo objetivo. Se a a04 vier a ser dividida (achado 🟠 -003), este é o momento natural para desdobrar `oa04` em dois objetivos e reatribuir. **Não alterado** — mexer nos objetivos declarados é decisão do orquestrador.
- **🔵 DID-M17-A01-S2 — A "Nota de compatibilidade com o Módulo 10" é um acerto raro.** Em vez de esconder que os dois módulos agrupam os mecanismos de subsidência de formas diferentes, a a01 declara a divergência, explica por que ela existe (a fase térmica é destacada porque é o que a a04 vai medir) e garante que nenhum mecanismo entra ou sai. Isso é honestidade epistêmica com custo didático quase zero, e deveria virar padrão sempre que um módulo reagrupar uma classificação já ensinada em outro.
- **🔵 DID-M17-A03-S3 — A seção "Da coluna d'água ao alvo geológico: por que a ordem importa" faz um trabalho que quase nenhum material faz:** explica que batimetria, sonar e sísmica não competem, e em que ordem se usam num levantamento real. É uma seção curta, no fim da aula, e é a que transforma três técnicas soltas numa sequência operacional. Preservar em qualquer reescrita.

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo | Observação |
|---|---|---|---|
| `oa01` — classificar bacias por mecanismo de subsidência e contexto tectônico; estilos estruturais extensionais | a01 (integral) · a02 (aplicação ao Atlântico Sul) | sim (a01, interpretativo) | coberto; promessa do cabeçalho ajustada (achado -001) |
| `oa02` — origem e estágios tectonossedimentares da margem atlântica brasileira | a02 (integral) | sim (a02, interpretativo) | coberto |
| `oa03` — princípios de aquisição e interpretação dos métodos sísmicos marinhos, sonar e batimetria | a03 (integral) | sim (a03, numérico) | coberto |
| `oa04` — interpretar mapas gravimétricos, magnéticos e de fluxo de calor; avaliar potencial de recursos | a04 (campos potenciais e fluxo de calor) · a05 (recursos) | sim (a04 interpretativo; a05 numérico) | coberto, mas o objetivo acumula duas competências — ver sugestão S1 |

**Conteúdo órfão:** nenhum. Todas as seções substantivas das cinco aulas servem a um objetivo declarado.

**Alinhamento com avaliação:** não verificável nesta passagem — o módulo ainda não tem questionário nem baralho. As restrições que a geração deve respeitar estão registradas no relatório de auditoria (notas 1 a 10) e no `course-state.yaml`.

## Encaminhamentos ao orquestrador

1. **Decidir sobre a divisão da Aula 04** (achado 🟠 DID-M17-A04-CARGA-003). É o único achado não corrigido, e o único que exige decisão estrutural. Recomendação: dividir, com o corte entre campos potenciais e estrutura térmica. Se a decisão for **não** dividir, o módulo permanece publicável — a aula fica longa, não incorreta —, mas o hub deveria registrar a a04 como "~40 min" em vez de "~30 min", porque a estimativa atual é otimista e o aluno que planeja o estudo por ela vai se frustrar.
2. **Se a a04 for dividida, desdobrar `oa04` em dois objetivos** (sugestão 🔵 S1) na mesma passagem, aproveitando que hub, `course-state.yaml` e mapas de objetivo já estarão sendo tocados.
