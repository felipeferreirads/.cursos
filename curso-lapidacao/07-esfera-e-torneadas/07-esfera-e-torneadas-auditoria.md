# Auditoria científica — Módulo 07: Esfera e formas torneadas

**Curso:** Teoria da lapidação — do desbaste ao projeto óptico (`lapidacao`)
**Módulo:** 07 — Esfera e formas torneadas (área IV. Talhes de superfície curva)
**Escopo:** as 4 aulas do módulo (`07-esfera-e-torneadas-aula-01` … `-aula-04`). Questionário **não existe** quando esta auditoria roda — é o efeito pretendido do gate. Baralho de flashcards **não se aplica**: dispensado neste curso a partir do módulo 06.
**Modo:** `audit-and-fix` · **Profundidade:** `full`
**Data:** 2026-09-04
**Auditor:** geo-arquiteto (Opus)
**Contrato de nível:** `ensino-medio-com-gemologia-v1`

---

## Resumo

| Severidade | Alegações afetadas | Blocos narrados abaixo |
|---|---|---|
| 🔴 Vermelho (erro factual / inconsistência interna) | 5 | 4 |
| 🟠 Laranja (impreciso / mecanismo errado / falso universal) | 7 | 6 |
| 🟡 Amarelo (imprecisão menor, termo, aritmética) | 4 | 4 |
| 🔵 Azul (sem fonte — afirmação removida) | 1 | 1 |
| ⚪ Branco (controvérsia real, declarada) | 1 | 1 |
| ✅ Verificado sem achado | 9 | — |

**Total: 18 achados sobre 18 alegações.** As duas colunas diferem em dois pontos, ambos por agrupamento narrativo: `MAQ-RAIO-ALVO-001` e `MAQ-COPO-CASADO-001` são o **mesmo erro** em dois lugares e saem juntas no 🔴 1; e `TOR-GOTA-BRIOL-001` (🟠) foi corrigida dentro do 🔴 4, porque é a mesma reescrita de critério. O manifesto `.json` lista as 18 separadamente, uma por `claim_id`.

**Total de alegações auditáveis no rodapé das aulas:** 20 antes da auditoria → **22** depois (20 herdadas − 1 removida por achado 🔵 + 3 criadas).
**Achados em aberto ao final:** nenhum. **Gate liberado.**

**`palavras_corpo` antes → depois:** a01 **1604→1592** · a02 1570→**1589** · a03 1587→**1590** · a04 1589→**1594**. As quatro sob o teto de ~1600 de LC-02 — e a a01, que entrou **acima** do teto, saiu conforme.

Este é o módulo mais corrigido do curso até aqui em proporção: **4 🔴 em 20 alegações**. A razão é identificável e vale registrar: as quatro aulas foram escritas a partir de um raciocínio geométrico correto e generalizado por conta própria para o maquinário e para a taxonomia, sem checagem contra fabricante ou contra a definição corrente dos termos. O raciocínio geométrico passou quase inteiro; o que dele foi **extrapolado** é o que falhou.

---

## Verificações estruturais

**Formato de `claim_id`.** As 20 alegações herdadas do redator casam com `^[A-Z]{2,4}-[A-Z0-9]+-[A-Z0-9]+-[0-9]{3}$` — **nenhum resíduo de 5 segmentos**. O padrão limpo do módulo 06 se manteve; os escorregões dos módulos 04 e 05 não voltaram. As 3 alegações criadas nesta auditoria — `ESF-PREF-SERRA-001` (a01), `DEF-BAND-DUREZA-001` (a03) e `TOR-GOTA-BRIOL-001` (a04) — seguem o mesmo formato. Verificado por regex sobre os quatro arquivos, antes e depois das correções: 22 alegações, 22 conformes.

**Competência de bancada.** Varredura específica por afirmação, sugestão ou avaliação de destreza manual: **um achado, corrigido**. A a03 dizia "Passe o dedo" no exemplo trabalhado — imperativo dirigido ao leitor. O conteúdo é um **teste de diagnóstico** sobre peça pronta, do mesmo tipo já aceito nos módulos 05 e 06 ("localizar o eixo c sob luz pontual"), mas a **forma** imperativa é a que a regra dura proíbe; trocada por construção impessoal ("Ao tato, porém, a superfície é lisa"). Fora isso, nenhum achado: as quatro aulas usam construção impessoal, os quatro verbos de objetivo são de conhecimento observável (explicar, descrever, prever, relacionar) e as quatro trazem em "O que não concluir" a exclusão explícita (como a máquina realiza a convergência; pressão e velocidade de rotação; como reparar undercut; como se opera o copiador de perfil). O texto **acrescentado** por esta auditoria descreve geometria, mecanismo de máquina e critério de diagnóstico — nunca operação.

**Pré-requisito cross-curso.** O curso de Gemologia é citado **por nome** na a03 (dureza de Mohs da turquesa), nunca por wikilink. Nenhuma violação. A correção do 🟠 5 acrescentou uma segunda menção, também por nome.

**LC-08 (controvérsia declarada).** O módulo entrou com **zero** ocorrências. A auditoria instalou **uma**, na a03, como pergunta aberta e sem arbitrar o debate — ver ⚪ 1. Mesmo desfecho do módulo 06, e pela mesma via: a controvérsia não foi fabricada, foi encontrada.

---

## 🔴 Vermelho 1 — a02 · o diâmetro final dado como fixado pela máquina

**Onde:** `07-esfera-e-torneadas-aula-02`, seção "Da peça bruta ao raio-alvo", exemplo trabalhado, Erros comuns, Recap, Vocabulário. Alegações `MAQ-RAIO-ALVO-001` e `MAQ-COPO-CASADO-001`.

**O que dizia.**
> O raio-alvo é fixado pela abertura entre os copos, não escolhido durante o processo: a peça converge até o ponto em que toca todos os copos ao mesmo tempo com a mesma pressão, e a partir daí a máquina só remove material igualmente de toda a superfície (o polimento), **sem mudar mais o raio**.
> […] copos abrasivos — discos ou anéis com uma calha côncava semicircular usinada na borda, **cujo raio de calha é exatamente o raio-alvo da esfera**.

**Por que é erro.** Não é assim que uma máquina de esfera funciona, e o erro é estrutural, não de detalhe.

1. **Os cabeçotes são de mola e avançam.** As fichas técnicas dos fabricantes descrevem cabeçotes **independentes, com mola e ajustáveis por manípulo**, justamente para acompanhar a peça enquanto ela encolhe. Não há "abertura fixa" que estacione o processo: a esfera diminui continuamente enquanto a máquina roda.
2. **O copo não tem o raio da esfera.** Cada tamanho de copo cobre uma **faixa** de diâmetros. O guia de seleção da Highland Park é explícito: copo de 1 pol (25 mm) → esferas de 1 a 1,4 pol (25 a 35,5 mm); copo de 2 pol (50,5 mm) → esferas de 2 a 2,6 pol (50,5 a 66 mm). O copo é maior que a esfera que produz, e produz várias.
3. **Quem determina o diâmetro é o operador**, interrompendo o desbaste — o que o texto negava explicitamente ("não algo ajustado durante").

Como estava, a afirmação produziria distrator invertido num questionário ("o que fixa o diâmetro da esfera?") e, pior, ancoraria a aula 04 no lugar errado: se o copo fixasse o raio, o copiador de perfil da a04 não teria de existir.

**Correção aplicada.** A seção foi retitulada "Da peça bruta ao **diâmetro-alvo**" e reescrita em dois blocos: (i) a preforma que chega da serra; (ii) o que o copo fixa e o que não fixa — cabeçote com mola, esfera encolhendo, faixa de trabalho por tamanho de copo com o número de catálogo, e o operador como quem para. A definição de copo foi reescrita (anel com calha, cabeçote com mola, contato em **coroa**, e a esfera como a única forma que satisfaz todos os copos com pressão igual). Vocabulário reindexado: `raio-alvo` → `diâmetro-alvo`, entradas novas `cabeçote`, `polo (de um eixo de trabalho)` e `faixa de trabalho do copo`; `par de copos casados` e `assento de máquina de esfera` removidas por terem virado supérfluas. Exemplo trabalhado ganhou o bloco "Onde a máquina para". Erros comuns e Recap alinhados.

**Fontes.** Highland Park Lapidary — guia de seleção de tamanho de copo (acesso 2026-09-04). Covington Engineering — máquinas de esfera pequena, grande e de três cabeças; cabeçotes com mola, independentes, ajustáveis por manípulo; faixa de 2,5 a 10 pol na máquina de três cabeças. Kingsley North e Arrowhead Lapidary Supply — mesma configuração.

**Confiança:** confirmado (três fontes de fabricante convergentes, com números).

---

## 🔴 Vermelho 2 — a02 · "um eixo só produz um cilindro", que contradiz a própria aula 04

**Onde:** `07-esfera-e-torneadas-aula-02`, seção "Por que um eixo só não converge", exemplo trabalhado, Erros comuns, Recap. Alegação `MAQ-EIXO-CIL-001`.

**O que dizia.**
> Se uma peça girasse contra um único eixo abrasivo, o resultado seria um **cilindro** ou um **disco** — a rotação em torno de um eixo fixo produz curvatura na direção perpendicular a esse eixo, mas deixa **reto** qualquer perfil medido ao longo do próprio eixo.

**Por que é erro.** É falso em geral, e é **contradito pela aula 04 do mesmo módulo**. Um eixo fixo produz o sólido de revolução daquele eixo, e qual sólido quem decide é o **perfil da ferramenta**: contra uma borda reta sai cilindro; contra uma calha curva sai perfil curvo. A a04 descreve exatamente isso — o copiador de perfil produzindo um ovo em torno de um eixo único. Um aluno que decorasse a frase da a02 concluiria que o ovo da a04 é impossível.

O que de fato falta a um eixo único é outra coisa, e é geométrica: os **dois pontos onde o eixo fura a superfície** ficam parados em relação à ferramenta e nunca são varridos. Todo sólido de revolução tem dois polos; a esfera é a forma que não admite polo privilegiado. Esse é o argumento correto, e ele é mais forte que o antigo, porque encadeia diretamente com o 🟠 3 (os polos fracos da máquina de duas cabeças) em vez de deixá-lo solto.

**Correção aplicada.** Parágrafo reescrito em torno do argumento dos polos, com a ressalva explícita de que a calha decide o perfil "(é assim que a aula 04 produzirá um ovo)". Exemplo trabalhado, um bullet novo em Erros comuns ("Achar que o eixo único obriga a um cilindro") e Recap alinhados. A a04 recebeu o fecho recíproco: "lá, um eixo fixo era insuficiente **para a esfera**; aqui, é exatamente o que se quer, porque o alvo tem polos".

**Confiança:** confirmado (geometria elementar de sólidos de revolução; a existência do copiador de perfil está na própria bibliografia da aula 04).

---

## 🔴 Vermelho 3 — a03 · "a ágata tem dureza uniforme, logo não socava"

**Onde:** `07-esfera-e-torneadas-aula-03`, seção "Bandeamento — um problema de orientação, não de dureza", exemplo trabalhado (Esfera B), Erros comuns, Recap. Alegação `DEF-BAND-ORIENT-001`.

**O que dizia.**
> A ágata bandada quase sempre tem dureza essencialmente **uniforme** de banda a banda […]. Se a dureza é uniforme, o mecanismo de undercut da seção anterior **não se aplica**: as bandas não afundam umas em relação às outras, porque o abrasivo remove todas na mesma taxa.

**Por que é erro.** Duas razões, e a segunda é interna.

1. **É falso.** O socavamento entre bandas de ágata é um problema **corrente e documentado** da oficina: as bandas variam em grau de cristalização, em porosidade e na proporção entre as fases de sílica, e a literatura de lapidaria discute abertamente como contê-lo — escolha de polidor (óxido de alumínio tipo Linde A é citado justamente para material que socava), escolha de suporte, cuidado no acabamento. A aula transformava uma tendência ("as bandas costumam ser parecidas") numa impossibilidade ("o mecanismo não se aplica").
2. **Contradizia o próprio título e o próprio vocabulário da aula.** O título é "undercut, **banda dura** e a orientação do padrão da ágata", e a tabela de vocabulário define "banda dura / banda mole" como camada "mais ou menos resistente à abrasão que as camadas vizinhas", exemplificando **com a ágata**. O corpo negava o que o título e o vocabulário afirmavam.

O dano potencial era grande porque este é o objetivo `oa03` inteiro, e porque a distinção entre os dois defeitos — que é excelente e sobrevive intacta — estava apoiada numa premissa falsa: a aula separava undercut de bandeamento **pelo material** ("é ágata, logo não é undercut"), quando o critério certo é **pelo relevo**.

**Correção aplicada.** A seção foi retitulada "**Bandeamento — dois defeitos diferentes com o mesmo nome**" e reorganizada em dois blocos explícitos: (i) **undercut entre bandas**, com o mecanismo, a variação real entre bandas e a marca observável (relevo físico); (ii) **bandeamento fora de centro**, o defeito geométrico, sem relevo, ligado à leitura do bruto do módulo 05. A seção seguinte foi retitulada "**O critério de diagnóstico é o relevo, não o material**" e reescrita para enunciar o critério na forma que o orquestrador pediu: *depressão física com o entorno no raio correto = undercut; padrão deslocado sobre superfície lisa = orientação*, com a ressalva de que **os dois podem coexistir na mesma peça**. O exemplo trabalhado ganhou o fecho "o que separou os dois casos não foi o material — foi o relevo. Com relevo no limite das bandas, a esfera B seria undercut de ágata". Erros comuns ganhou o erro nas **duas** direções ("tratar todo defeito de esfera bandada como undercut — ou achar que ágata nunca socava"). Vocabulário ganhou `bandeamento fora de centro` e teve `heterogeneidade de dureza` reindexada para `heterogeneidade de resistência à abrasão`, que é o que o mecanismo realmente mede.

**Fontes.** Lapidary Journal / Rock & Gem e literatura corrente de oficina sobre polimento de ágata (acesso 2026-09-04) — socavamento entre bandas como problema corrente e a escolha de polidor para contê-lo; discussões técnicas de lapidaria sobre material que socava no polimento final.

**Confiança:** confirmado para a existência do efeito; a **causa** é ⚪ 1.

---

## 🔴 Vermelho 4 — a04 · o critério de "forma torneada" excluía os dois exemplos que a própria aula dava

**Onde:** `07-esfera-e-torneadas-aula-04`, vocabulário, seção "O que continua igual, e o que muda", seção "Ovo, obelisco e gota", seção "A fronteira com a escultura livre", exemplo trabalhado, Erros comuns, Recap. Alegações `TOR-DEF-REVOL-001`, `TOR-PROP-OBEL-001`, `TOR-DIST-ESCULT-001`.

**O que dizia.**
> toda forma torneada é um **sólido de revolução**, e **qualquer seção perpendicular ao eixo é um círculo perfeito**
> […] o corpo […] costuma ser canelado ou levemente facetado ao longo do eixo, uma **variação que não quebra a simetria rotacional** porque as canaletas se repetem identicamente ao redor do eixo
> […] **gota** (*briolette* ou *teardrop*) | forma torneada com uma extremidade arredondada e a outra afunilada

**Por que é erro.** A aula enuncia um critério forte e depois admite na categoria duas formas que o violam, declarando que não o violam.

1. **Canaletas repetidas quebram, sim, a simetrização contínua.** Um corpo canelado tem simetria **cíclica** (coincide consigo mesmo a cada 1/n de volta), não contínua. Suas seções perpendiculares não são círculos. Dizer que a repetição "não quebra a simetria rotacional" confunde os dois tipos de simetria.
2. **O obelisco não é um sólido de revolução, e nem pretende ser.** A forma que dá nome ao termo é de **seção quadrada** com pirâmide no topo; a versão ornamental de lapidaria é tipicamente de quatro ou seis lados. Uma aula que exige seção circular expulsa da família a forma que ela mesma pôs no título.
3. **A briolette é, por definição, facetada.** As definições correntes convergem: pera alongada, aproximadamente simétrica em torno do eixo principal, **coberta de facetas angulares** e **sem cinta**. Igualá-la à gota lisa como se fossem a mesma coisa, e chamar as duas de sólido de revolução, é erro de nomenclatura sobre erro de geometria.

Isto importa porque `oa04` é exatamente "distinguir da escultura livre": o critério é o objeto da aula, e estava quebrado.

**Correção aplicada.** Instalada a distinção que resolve os três casos de uma vez, numa seção nova, "**Duas exigências diferentes: seção circular e eixo único**":

- **sólido de revolução estrito** — toda seção perpendicular é círculo, a peça coincide consigo mesma sob **qualquer** ângulo. Esfera, ovo liso, gota lisa.
- **forma de eixo único** — existe um eixo que organiza a peça e todo detalhe ou é de revolução em torno dele ou se repete em torno dele um número inteiro de vezes. Inclui os anteriores **mais** obelisco poligonal, obelisco canelado e briolette facetada. **É esta a família de talhe do módulo**, e a inclusão foi fixada numa fórmula memorável: **estrito ⊂ eixo único**.

A "fronteira com a escultura livre" foi reescrita como um **teste de duas perguntas em ordem** — (1) a peça se repete em torno de alguma linha, contínua ou por ângulo fixo? "não" = escultura livre, e a segunda pergunta nem se coloca; (2) a repetição é contínua? "sim" = revolução estrita, "não" = obelisco e briolette. O exemplo trabalhado passou a rodar as duas perguntas em cada uma das três peças, e o obelisco do exemplo foi explicitado como de **seção quadrada** (as seções são quadrados que encolhem de ~18 mm a quase zero, não círculos). Vocabulário refeito: entradas novas `sólido de revolução estrito`, `forma de eixo único` (com a glosa de que é o que o curso chama de *forma torneada*) e `briolette`; `obelisco` e `gota` reescritas. Erros comuns e Recap alinhados; alegação nova `TOR-GOTA-BRIOL-001`.

**Fontes.** Britannica, verbete *briolette*; Antique Jewelry University, *Briolette Cut*; literatura gemológica corrente (acesso 2026-09-04) — pera alongada coberta de facetas angulares, sem cinta. *American Scientist*, "Moving Obelisks" (acesso 2026-09-04) — obelisco de seção quadrada. Teoria elementar de simetria rotacional (contínua × cíclica).

**Confiança:** confirmado.

---

## 🟠 Laranja 1 — a01 · o ponto mais distante de um poliedro dado como o meio da aresta

**Onde:** `07-esfera-e-torneadas-aula-01`, seção "Do cubo ao poliedro", exemplo trabalhado (passos 2 e 3), Recap. Alegação `ESF-CONV-POLI-001`.

**O que dizia.** "O cuboctaedro […] ainda tem pontos mais distantes do centro (**o meio de cada aresta**) e pontos mais próximos (o centro de cada face). O próximo corte trunca essas novas arestas."

**Por que é impreciso.** Num sólido convexo de faces planas, o ponto mais distante de qualquer ponto interior é sempre um **vértice**, nunca o meio de uma aresta. No cuboctaedro tirado de um cubo de 30 mm de aresta, os vértices estão a $15\sqrt2 \approx 21{,}2$ mm e os meios de aresta a ~18,4 mm. A frase inverte o objeto do corte justamente na aula cuja mecânica inteira é "corte o ponto mais distante" — e o texto se salvava por acidente, porque os vértices do cuboctaedro **são** os meios de aresta do cubo (leitura que o exemplo trabalhado sugeria e a seção de conteúdo não).

**Correção aplicada.** Seção retitulada "a lógica do corte de **vértice**"; frase reescrita com o princípio explícito ("os **vértices**, que num sólido de faces planas são sempre os pontos extremos"); passos 2 e 3 do exemplo reescritos, com o passo 3 declarando a identidade que resolve a ambiguidade: "corte dos 12 vértices do cuboctaedro, que são exatamente os 12 meios de aresta do cubo original — é o mesmo cortar-as-arestas da preforma de serra". Recap e vocabulário (`convergência geométrica`) alinhados.

---

## 🟠 Laranja 2 — a01 · a física do teste de rolamento invertida

**Onde:** `07-esfera-e-torneadas-aula-01`, exemplo trabalhado, Recap. Alegação `ESF-TEST-ROLA-001`.

**O que dizia.** "uma esfera com erro de centro tem um eixo 'preferido' e para sempre voltando à mesma orientação, porque **o lado mais pesado (ou mais largo) busca o ponto mais baixo**."

**Por que é impreciso.** O parêntese está de cabeça para baixo. Um corpo de densidade uniforme repousa na orientação que **minimiza a altura do centro de massa acima do plano**, e essa altura é a distância do centro ao plano tangente no ponto de contato — mínima onde o **raio é menor**. Uma peça fora de redondo assenta, portanto, sobre as regiões de raio **menor**, deixando o eixo mais longo **deitado**: é o ovo deitado, não o ovo em pé. Só o "lado mais pesado" (densidade heterogênea) desce, e essa é uma causa **diferente** da que a aula está discutindo, que é erro de geometria.

Somava-se a isso uma atribuição de fonte que a auditoria não conseguiu sustentar: o "teste de rolamento" era creditado a *Lapidary Journal / Rock & Gem* como verificação de qualidade de oficina, e a verificação documentada é outra — **diâmetro com paquímetro em várias direções**, comparando o maior com o menor valor.

**Correção aplicada.** Mecanismo corrigido e ancorado ("assenta sobre as regiões de **menor** raio, deixando o eixo mais longo deitado, como um ovo deitado"); o parêntese de densidade removido; o rolamento rebaixado ao que ele é — "o indício grosseiro que antecede a medida" — e a medição de oficina instalada no lugar. Alegação reescrita com fonte de mecânica elementar em vez de atribuição de revista. Recap alinhado.

---

## 🟠 Laranja 3 — a02 · os polos fracos explicados por velocidade linear

**Onde:** `07-esfera-e-torneadas-aula-02`, seção "Por que máquinas comerciais usam mais de dois eixos", exemplo trabalhado, Recap. Alegação `MAQ-POLO-FRACO-001`.

**O que dizia.** "os polos […] recebem menos abrasão relativa que o 'equador' […] **porque a velocidade linear da superfície abrasiva contra a peça é menor perto do centro de rotação**."

**Por que é impreciso.** O fenômeno existe; o mecanismo dado não é o dele. O copo abrade por uma **coroa** de raio fixo — todos os pontos de contato têm praticamente a mesma velocidade linear, não há gradiente do centro para a borda como haveria num disco plano. A causa é geométrica: quando a peça se acomoda girando em torno do eixo que liga os dois copos, os polos desse eixo ficam **dentro da boca do copo** e simplesmente não passam pela coroa abrasiva. Região não varrida, não desbastada.

A diferença não é acadêmica: com o mecanismo errado, o remédio ("reassentar a peça") vira arbitrário, e o argumento do terceiro cabeçote perde a razão de ser.

**Correção aplicada.** Mecanismo reescrito nas quatro ocorrências; vocabulário ganhou a entrada `polo (de um eixo de trabalho)`, que agora é o mesmo conceito usado no 🔴 2 — o que amarra as duas seções da aula num argumento só.

---

## 🟠 Laranja 4 — a02 · "máquinas comerciais usam de 3 a 6 copos"

**Onde:** `07-esfera-e-torneadas-aula-02`, seção "Por que máquinas comerciais usam mais de dois eixos", exemplo trabalhado, "O que não concluir", Recap. Alegação `MAQ-NUM-COPOS-001`.

**Por que é impreciso.** O levantamento de catálogo não sustenta a faixa. As configurações comerciais correntes são de **duas** e de **três** cabeças: Covington Engineering modelo de três cabeças, mais os modelos de duas cabeças para peça pequena e grande; Highland Park, três cabeças; Kingsley North e Arrowhead, o mesmo. Nenhuma máquina de 4, 5 ou 6 copos apareceu. Além disso, o texto descartava a configuração de duas cabeças como "de oficina mais simples", quando ela é um produto comercial corrente.

**Correção aplicada.** A faixa "3 a 6" foi substituída pela descrição real — duas e três cabeças, com **três como o arranjo comercial de referência** —, e a seção foi retitulada "Por que máquinas comerciais usam **três cabeçotes**". A frase que tratava a máquina de duas cabeças como improvisada foi corrigida ("os modelos comerciais existem, para peças pequenas e grandes"). O argumento pedagógico não mudou: dois resolvem no **tempo**, três resolvem no **espaço**, e o ganho é uniformidade, não velocidade.

---

## 🟠 Laranja 5 — a03 · a direção da dureza da matriz da turquesa dada como fixa

**Onde:** `07-esfera-e-torneadas-aula-03`, seção "Undercut", exemplo trabalhado (Esfera A), Recap. Alegação `UND-MAT-EXEMPLO-001`.

**O que dizia.** "turquesa com **matriz mole** entremeada de veio mais duro" e, no exemplo, "a matriz é **mais mole** que a turquesa maciça ao redor".

**Por que é impreciso.** A turquesa tem dureza 5 a 6 de Mohs e a matriz que a atravessa **varia**: limonita é mais mole que a turquesa e socava; chert e quartzo são mais duros, e nesse caso quem recua é a **própria turquesa**, deixando o veio de matriz saliente. A aula fixava uma das duas direções como se fosse a única, o que ensina o defeito como uma lista de materiais em vez de uma comparação — exatamente o hábito que o 🔴 3 também combate.

**Correção aplicada.** Parágrafo novo com a regra na forma correta ("o mecanismo diz **quem** afunda — o menos resistente —, não qual dos dois materiais é ele"), os dois casos da turquesa nomeados, e o pré-requisito do curso de Gemologia reativado por nome para a dureza. A Esfera A do exemplo foi especificada como **matriz limonítica** e ganhou o parêntese do caso invertido. Erros comuns ganhou o bullet "Decorar qual material afunda".

---

## 🟠 Laranja 6 — a04 · a proporção do obelisco sem faixa e sem tradição declarada

**Onde:** `07-esfera-e-torneadas-aula-04`, seção "Ovo, obelisco e gota", exemplo trabalhado, "O que não concluir", Recap. Alegação `TOR-PROP-OBEL-001`.

**O que dizia.** "razão altura:largura tipicamente **4:1 ou mais**, valor de referência da mesma literatura".

**Por que é impreciso.** "4:1 ou mais" é aberto para cima e não corresponde a nenhuma das duas tradições que a palavra "obelisco" carrega. O obelisco **arquitetônico** — o que dá nome à forma — é bem mais esbelto: a razão altura:largura vai de cerca de 6:1 a 12,5:1, com metade dos exemplares entre 9:1 e 11:1 e média em torno de 9,4:1; a descrição clássica dá "nove, nove e meia, às vezes dez vezes a espessura". O obelisco **ornamental de lapidaria** é bem mais atarracado, correntemente entre 3:1 e 5:1. Um valor único aberto para cima cobre as duas e não descreve nenhuma, violando LC-05 (faixa **e** fonte).

**Correção aplicada.** As duas faixas foram declaradas separadamente, com a tradição de cada uma nomeada, e a confusão entre elas foi promovida a erro comum ("é erro de **escopo**, não de número"). O exemplo trabalhado passou a situar seus 4,4:1 explicitamente: "na faixa ornamental (3:1 a 5:1), longe da arquitetônica (6:1 a 12:1)".

---

## 🟡 Amarelo 1 — a01 · "o desvio máximo cai para poucos milímetros"

O valor é calculável e vale ~6 mm, não "poucos". Para um cubo de 30 mm de aresta: vértice a $15\sqrt3 \approx 26$ mm e face a 15 mm, desvio ~11 mm; no cuboctaedro, vértice a $15\sqrt2 \approx 21$ mm e face quadrada a 15 mm, desvio ~6 mm. Os dois pares de números foram instalados no corpo e no passo 2 do exemplo, o que de quebra deu ao aluno a verificação numérica de que a convergência realmente reduz o desvio — que a aula afirmava sem mostrar.

---

## 🟡 Amarelo 2 — a01 e a02 · o corte discreto tratado como ficção pedagógica

A a01 dizia que "o corte de aresta é o modelo pedagógico […] **não uma descrição do maquinário**", e a a02 descrevia a peça de partida como "desbastada perto de um cubo ou de um cilindro curto". As duas subestimam a prática: a preforma de esfera é feita **na serra**, por corte discreto, indo de cubo → corte dos 8 vértices → corte das 12 arestas, e chegando a um sólido de dezenas de faces pequenas antes de qualquer máquina de copos. Ou seja, o "modelo pedagógico" da a01 é literalmente a etapa real anterior à da a02, e as duas aulas se tratavam como se fossem alternativas.

**Correção aplicada.** Parágrafo novo na a01 instalando a preforma de serra como etapa real, com a fronteira nítida entre os dois regimes (corte plano discreto na serra; abrasão contínua na máquina); alegação nova **`ESF-PREF-SERRA-001`**. O bullet de Erros comuns da a01 foi reescrito de "confundir o modelo com o processo" para "**confundir as duas etapas**". A a02 ganhou uma linha em "Antes de começar" e teve a descrição da peça de partida corrigida; vocabulário da a01 ganhou `preforma de esfera` e o da a02 teve `saibro / cilindro pré-formado` renomeado para a mesma entrada (ver 🟡 3).

**Fonte.** Highland Park Lapidary, *How to Make a Stone Sphere: A Step-by-Step Guide* (acesso 2026-09-04) — cubo, corte dos cantos e corte dos cantos resultantes.

---

## 🟡 Amarelo 3 — a02 · "saibro" como tradução de *sphere blank*

A entrada de vocabulário era "**saibro** / cilindro pré-formado (*sphere blank*)". *Saibro*, em português, é solo arenoso ou cascalho de alteração — não tem relação com peça pré-formada, e é termo de geologia de campo que colide com o vocabulário do curso irmão. Renomeada para **`preforma de esfera` (*sphere blank*)**, que é a mesma entrada agora usada na a01, alinhando as duas aulas.

---

## 🟡 Amarelo 4 — a02 · "esfera de 25 mm de raio" a partir de um cubo de 30 mm

No exemplo trabalhado: "**Uma peça de ônix cúbica de 30 mm de aresta vai virar uma esfera de 25 mm de raio de calha**". Uma esfera de 25 mm de raio tem 50 mm de diâmetro e não cabe num cubo de 30 mm — o cubo é o teto do diâmetro. Erro de raio por diâmetro, repetido em três pontos do exemplo. Corrigido para **25 mm de diâmetro**, e a restrição foi promovida a conteúdo, entre parênteses, porque ensina de graça o limite geométrico da preforma: "de um cubo de 30 mm não sai esfera maior que 30 mm".

---

## 🔵 Azul 1 — a01 · a tolerância de esfericidade e o gabarito de anel calibrado (removidos)

**Onde:** `07-esfera-e-torneadas-aula-01`, seção "Do cubo ao poliedro", Recap, "O que não concluir". Alegação `ESF-TOL-FAIXA-001` — **removida**.

**O que dizia.** "tipicamente algumas **centésimas de milímetro** de desvio de raio numa esfera de 20 a 30 mm, para uma esfera de qualidade de guilda avaliada por **gabarito de anel calibrado (ring gauge)**".

**Por que é 🔵.** Nenhuma das duas metades se confirmou. A busca por critério de tolerância de esfericidade em lapidaria não devolveu fonte do ofício: o material sobre *ring gauge* que existe é de **metrologia industrial** (calibrador passa/não-passa para eixos e furos), não de bancada de lapidaria, e transplantar o termo para cá é criar um procedimento que a fonte não descreve. O número em centésimos de milímetro não apareceu em fonte alguma. O que **está** documentado é o método simples: medir o diâmetro com paquímetro em **várias direções** e comparar o maior com o menor.

**Tratamento (regra da skill para 🔵: não inventar a correção).** A afirmação foi **removida** do corpo e do Recap, e a alegação foi retirada do rodapé em vez de ser reescrita com número novo. No lugar entrou o método verificável, e "O que não concluir" ganhou um bullet declarando a lacuna de forma explícita: *"Não concluir qual é a tolerância de esfericidade aceita numa esfera de qualidade — número de oficina que a literatura consultada não fixa de forma verificável; o que se pode afirmar é o método."* Nenhum número foi substituído por outro número.

---

## ⚪ Branco 1 — a03 · por que uma banda de ágata socava (controvérsia declarada, LC-08)

Achado colhido durante a correção do 🔴 3. As fontes de oficina **convergem** sobre o efeito — bandas de ágata socavam, e o remédio é polidor e suporte — e **divergem** sobre a causa: uma leitura atribui a diferença real de dureza entre fases de sílica, outra a dureza praticamente igual com diferença de porosidade e de tomada de polimento. As duas hipóteses preveem exatamente o mesmo relevo observável, o que explica por que a divergência sobrevive.

**Tratamento (regra da skill para ⚪: não escolher lado).** Instalado um callout `> [!question] Em aberto` na a03, declarando a divergência como pergunta aberta e nomeando as duas posições, sem arbitrar; um bullet no Recap; alegação nova **`DEF-BAND-DUREZA-001`** com `risk: controversia`. De quebra, isto instala o **único LC-08 do módulo**, que entrou com zero — mesma situação e mesmo desfecho do módulo 06.

---

## Verificado sem achado (amostra do que foi conferido e passou)

- **Geometria do cuboctaedro (a01).** Cubo 6/12/8 → corte dos 8 vértices até a metade das arestas → 14 faces (6 quadradas residuais, 8 triangulares novas), 24 arestas, 12 vértices. Confere, inclusive Euler (12−24+14=2). É a retificação padrão do cubo.
- **Aritmética do passo 1 do exemplo (a01).** Centro→face 15 mm; centro→vértice $15\sqrt3 \approx 26$ mm; desvio ~11 mm. Confere.
- **Propagação do erro de centro (a01, `ESF-CENT-PROP-001`).** O argumento — cada etapa assume o centro anterior, logo o erro se propaga em vez de se diluir — é correto e independente das correções acima. Nada a mudar.
- **Cúpula única × sólido de revolução completo (a01, `ESF-SOL-REVO-001`).** A assimetria de exigência entre cabochão e esfera confere, e o encadeamento com o módulo 06 está correto.
- **Correção mútua entre copos (a02).** O argumento de que a única forma que satisfaz todos os copos com pressão igual é a esfera é correto e sobreviveu inteiro às correções do 🔴 1 e do 🔴 2 — na verdade ficou mais forte, porque deixou de depender do raio da calha.
- **Pré-formação poupa tempo (a02).** Abrasão por copo é lenta por contato distribuído e pressão baixa por área. Confere, e agora encadeia com a preforma de serra da a01.
- **Mecanismo do undercut (a03, `UND-MEC-DIFDUR-001`).** Idêntico ao do módulo 02, com a agravante correta na esfera: a zona mole afunda abaixo do raio em que as vizinhas já pararam, e mais tempo só aprofunda. Confere; a alegação foi só reescrita em vocabulário ("resistência" no lugar de "dureza"), sem mudança de conteúdo.
- **Dois centros e a leitura do bruto (a03, `DEF-BRUTO-CENTRO-001`).** A geometria concêntrica do nódulo de ágata, o não-alinhamento entre centro de crescimento e centro geométrico, e a irreversibilidade da decisão depois da montagem: tudo confere, e é o melhor argumento do módulo.
- **Proporção do ovo (a04, `TOR-PROP-OVO-001`).** 1,3:1 a 1,5:1 confere contra amostragem de dimensões declaradas em peças de oferta corrente (21,0×14,0 cm = 1,5:1; 14,0×10,0 cm = 1,4:1; 1,8×1,3 pol = 1,38:1) e contra a proporção do ovo de ave. A alegação foi só reforçada com essa verificação.
- **Copiador de perfil (a04, `TOR-COPIA-PERFIL-001`).** O princípio — gabarito guiando a distância entre eixo e superfície abrasiva — confere, e a exclusão da operação por competência de bancada está corretamente declarada.

---

## Alegações corrigidas

`MAQ-RAIO-ALVO-001` · `MAQ-COPO-CASADO-001` · `MAQ-EIXO-CIL-001` · `MAQ-POLO-FRACO-001` · `MAQ-NUM-COPOS-001` · `DEF-BAND-ORIENT-001` · `DEF-DIAG-CAUSA-001` · `UND-MAT-EXEMPLO-001` · `UND-MEC-DIFDUR-001` · `ESF-CONV-POLI-001` · `ESF-TEST-ROLA-001` · `TOR-DEF-REVOL-001` · `TOR-PROP-OBEL-001` · `TOR-DIST-ESCULT-001` · `TOR-PROP-OVO-001`

## Alegações criadas

`ESF-PREF-SERRA-001` (a01) · `DEF-BAND-DUREZA-001` (a03) · `TOR-GOTA-BRIOL-001` (a04)

## Alegações removidas

`ESF-TOL-FAIXA-001` (a01) — ver 🔵 1. Removida, não reescrita: não havia fonte para substituir o número.

## Alegações renomeadas

Nenhuma. Todas as 20 herdadas já estavam no formato de 4 segmentos.

---

## Material derivado

**Nenhum.** O módulo 07 não tinha questionário quando esta auditoria rodou — efeito pretendido do gate — e não terá baralho de flashcards, dispensado neste curso a partir do módulo 06. Nada a propagar; o `gerador-de-questionarios` recebe o módulo já limpo.

**Nenhuma outra aula do curso foi tocada.** Buscas por "cilindro", "raio-alvo", "briolette", "obelisco", "undercut" e "banda" nos módulos 01–06 não encontraram repetição dos fatos corrigidos fora do módulo 07. O `undercut` do módulo 02 é o mecanismo genérico e permanece correto; a a03 deste módulo agora o cita com o vocabulário alinhado.

---

## Encaminhado à revisão didática

1. **As quatro aulas foram enxugadas para caber no teto.** As correções acrescentaram material substancial (a seção nova da a04, os dois blocos novos da a03, o argumento dos polos da a02, a preforma de serra da a01) e o orçamento foi financiado por corte de redundância em cada aula. A revisão deve verificar, corte a corte, se algum removeu **conteúdo** em vez de repetição — é o mesmo encargo que a a04 do módulo 06 recebeu e que lá foi verificado sem ação. Pontos a checar: a01 (abertura da seção "Do cubo ao poliedro", fecho da seção de propagação de erro, fecho do exemplo trabalhado); a02 (exemplo trabalhado, comprimido em ~40% depois que o Conteúdo passou a carregar o mecanismo); a03 (seção de abertura e as duas seções finais); a04 (a seção "O que continua igual" foi **fundida** na seção nova, e a "fronteira com a escultura livre" foi cortada quase pela metade).

2. **a04 — carga de conceitos.** A aula agora ensina **dois** critérios aninhados onde antes ensinava um, mais um teste de duas perguntas, mais três formas, mais duas tradições de proporção do obelisco. É de longe a aula mais densa do módulo. A revisão deve julgar se a fórmula `estrito ⊂ eixo único` e o teste em duas perguntas bastam como organizador prévio, ou se a aula precisa de um andaime a mais — sabendo que a folga é de 6 palavras e que qualquer acréscimo tem de ser financiado por corte, e **não** pelo texto instalado por esta auditoria.

3. **a02 — o exemplo trabalhado ficou paralelo ao Conteúdo.** Depois das correções, os quatro blocos do exemplo (um eixo, dois cabeçotes, três cabeçotes, onde a máquina para) repetem a estrutura das quatro seções do Conteúdo quase um a um. Está correto e é útil como consolidação, mas a revisão deve julgar se é **exemplo** ou **resumo** — se for resumo, a aula tem um exemplo trabalhado a menos do que declara.

4. **LC-08.** O módulo entrou com zero controvérsias e a auditoria instalou uma (a03, a causa do socavamento entre bandas). Cabe à revisão decidir se basta. Candidata natural para uma segunda, se for julgada necessária: a posição da preforma — quantas faces vale a pena tirar na serra antes de passar à máquina — que apareceu nas fontes com respostas diferentes e não foi desenvolvida por falta de orçamento de palavras.

5. **a03 — o callout `> [!question]` é o primeiro do módulo.** Verificar se a forma de callout do Obsidian é consistente com a usada nos módulos anteriores para controvérsia declarada, e se o bloco não interrompe o fio entre os dois defeitos (ele está posicionado entre o primeiro e o segundo).

6. **Vocabulário reindexado em três das quatro aulas.** a01 foi de 8 para 9 entradas, a02 trocou 4 das 7, a03 foi de 7 para 8, a04 foi de 7 para 9 (o teto de LC-03 é 10). A revisão deve conferir LC-01 nas entradas novas — se cada termo novo está definido na primeira aparição do corpo, e não só na tabela.

---

## Fontes consultadas nesta auditoria

- Sinkankas, *Gem Cutting: A Lapidary's Manual* — capítulo de esfera e conta: convergência, copo, eixos cruzados, formas torneadas, heterogeneidade de material.
- Highland Park Lapidary (acesso 2026-09-04) — *How to Make a Stone Sphere: A Step-by-Step Guide* (preforma: cubo, corte dos cantos, corte dos cantos resultantes); guia de seleção de tamanho de copo (copo de 1 pol → esferas de 1 a 1,4 pol; copo de 2 pol → esferas de 2 a 2,6 pol; copo de 3 pol → 3,4 a 4,1 pol); máquina de três cabeças, rosca 5/8-11 e adaptador NPT 3/4 pol.
- Covington Engineering (acesso 2026-09-04) — máquina de esfera de três cabeças (2,5 a 10 pol; três cabeçotes com mola, independentes, ajustáveis por manípulo); máquina pequena (1/4 a 1 pol) e grande (1-1/4 a 9 pol) de duas cabeças.
- Kingsley North e Arrowhead Lapidary Supply (acesso 2026-09-04) — catálogo de máquinas de esfera; modelo 383 de três cabeças, modelo 381 grande.
- Lapidary Journal / Rock & Gem e literatura corrente de oficina sobre polimento (acesso 2026-09-04) — socavamento entre bandas de ágata como problema corrente; escolha de polidor para material que socava; polimento de turquesa.
- Literatura corrente de lapidaria sobre turquesa (acesso 2026-09-04) — dureza 5 a 6 de Mohs; matriz variável em dureza.
- Britannica, verbete *briolette*; Antique Jewelry University, *Briolette Cut*; literatura gemológica corrente (acesso 2026-09-04) — briolette como pera alongada coberta de facetas angulares, sem cinta, simétrica em torno do eixo principal.
- *American Scientist*, "Moving Obelisks", e a descrição clássica das proporções do obelisco (acesso 2026-09-04) — razão largura:altura de 1:6 a 1:12,5, cerca de metade entre 1:9 e 1:11, média 1:9,4; seção quadrada.
- Levantamento de dimensões declaradas em peças ornamentais de pedra em oferta corrente (acesso 2026-09-04) — ovos entre 1,38:1 e 1,5:1; torres e obeliscos de seção quadrada ou hexagonal.
- Prática corrente de medição de gema e de esfera com paquímetro (acesso 2026-09-04) — diâmetro tomado em várias direções como verificação de simetria.
- Geometria poliedral e teoria de simetria rotacional (contínua × cíclica) — cuboctaedro como retificação do cubo; o vértice como ponto extremo de um sólido convexo de faces planas; mecânica elementar de repouso de corpo rígido.
- William Holland School of Lapidary Arts e a taxonomia de disciplinas das guildas norte-americanas — esfera e torneado como disciplina distinta da escultura.
- GIA — Idar-Oberstein; fronteira entre forma de máquina e escultura livre.
- `_contexto.md` deste curso — contrato `ensino-medio-com-gemologia-v1`, régua de `palavras_corpo`, formato de `claim_id`, regra dura de não-competência-de-bancada, pipeline sem flashcards a partir do módulo 06.
