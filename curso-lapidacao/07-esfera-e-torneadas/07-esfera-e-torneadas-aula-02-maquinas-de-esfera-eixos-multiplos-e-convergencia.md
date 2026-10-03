# Aula 02: Máquinas de esfera — copos rotativos, eixos cruzados e o princípio de convergência

**ID:** lapidacao-m07-a02
**Módulo:** [[07-esfera-e-torneadas-modulo|Módulo 07]] — Esfera e formas torneadas
**Duração estimada:** ~27 min
**Objetivo:** descrever o princípio das máquinas de esfera e justificar por que a convergência descrita na aula 01 exige eixos de contato múltiplos, não um único desbaste.
**Pré-requisito:** [[07-esfera-e-torneadas-aula-01-por-que-a-esfera-converge-do-cubo-ao-poliedro-a-esfera|aula 01]] deste módulo (a convergência geométrica e a exigência de centro único); [[03-maquinas-da-bancada-modulo|módulo 03]] deste curso (esmeril e drums de expansão — a lógica de superfície abrasiva rotativa que já produz curva).

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **copo de esfera** (*sphere cup*) | anel abrasivo com uma calha côncava usinada na borda, que abraça parte da peça enquanto gira; o contato é uma coroa circular, não um ponto. |
| **cabeçote** | o conjunto motor + eixo + copo que gira e, por **mola**, pressiona o copo contra a peça, avançando à medida que material sai. |
| **eixo cruzado** | disposição em que dois ou mais eixos de rotação não são paralelos nem coincidentes, de modo que cada um varre a peça numa direção diferente. |
| **preforma de esfera** (*sphere blank*) | peça já reduzida na serra ao sólido de muitas faces da aula 01, ponto de partida para a máquina de esfera. |
| **polo (de um eixo de trabalho)** | um dos dois pontos em que o eixo de rotação fura a superfície da peça; fica parado em relação ao copo e não é varrido pela coroa abrasiva. |
| **diâmetro-alvo** | o diâmetro final pretendido para a esfera, atingido quando o operador interrompe o desbaste — não fixado pela máquina. |
| **faixa de trabalho do copo** | o intervalo de diâmetros de esfera que um dado tamanho de copo consegue produzir. |

## Antes de começar, você precisa saber

- Da [[07-esfera-e-torneadas-aula-01-por-que-a-esfera-converge-do-cubo-ao-poliedro-a-esfera|aula 01]] deste módulo: a convergência à esfera exige que cada etapa de remoção de material seja referenciada ao **mesmo centro**; um centro deslocado produz uma forma assimétrica que não se corrige depois.
- Do [[03-maquinas-da-bancada-modulo|módulo 03]] deste curso: o esmeril e os drums de expansão já produzem superfície curva porque a peça é levada contra uma roda ou cinta que gira num único eixo — mas isso produz uma curva **numa direção só** por vez, como no cabochão.
- Da [[07-esfera-e-torneadas-aula-01-por-que-a-esfera-converge-do-cubo-ao-poliedro-a-esfera|aula 01]]: a peça não chega à máquina como bruto, e sim como a **preforma de esfera**, cortada na serra, de muitas faces pequenas.
- Não é preciso saber ainda os defeitos que a heterogeneidade do material impõe a esse processo — é a aula 03.

## Ao final você vai conseguir

- `lapidacao-m07-oa02` — Descrever o princípio das máquinas de esfera e justificar a necessidade de eixos múltiplos.

## Conteúdo

### Por que um eixo só não converge

O esmeril do [[03-maquinas-da-bancada-modulo|módulo 03]] gera curva porque a peça se move contra uma roda que gira em torno de **um** eixo fixo. Isso funciona perfeitamente para a cúpula do cabochão, porque a cúpula só precisa de curvatura boa **naquela direção de varredura** — o operador decide a curva pela mão, passe a passe, e o resultado é aceito se ficar suave ao olho e ao gabarito de altura.

A esfera não pode ser produzida assim, mesmo em princípio. Uma peça que gira em torno de **um** eixo fixo só pode virar um **sólido de revolução em torno daquele eixo** — e qual sólido, quem decide é o perfil da ferramenta, não a peça: contra uma roda de borda reta sai um cilindro; contra uma calha curva sai um perfil curvo (é assim que a aula 04 produzirá um ovo). O que o eixo único **não** consegue, com ferramenta nenhuma, são os dois pontos onde ele fura a superfície da peça: eles ficam parados no próprio eixo, sem varredura, e nunca entram na zona de trabalho. Todo sólido de revolução tem **dois polos**; a esfera é justamente a forma que não admite polo privilegiado. Por isso a peça precisa de, no mínimo, dois eixos de contato não paralelos: o que é polo para um cai na zona ativa do outro.

### O copo, a coroa de contato e a correção mútua

A solução de oficina descrita por Sinkankas e adotada pelas máquinas comerciais usa **copos abrasivos** — anéis com uma calha côncava usinada na borda, montados em cabeçotes que apontam para a peça a partir de direções diferentes e a **pressionam por mola**. Cada copo toca a peça ao longo de uma coroa circular, não de um ponto. Enquanto o cabeçote gira, essa coroa varre a peça e rebaixa qualquer região que se projete para fora do raio que a calha impõe naquela direção.

O mecanismo de correção mútua é o que faz esse arranjo convergir, e não só desbastar: se a peça, num instante, estiver mais "oval" que "esférica" ao longo do eixo do copo A, o copo B — apontando de outra direção — encontra ali material sobrando e o remove primeiro, porque o excesso aparece como contato mais forte contra a calha de B. A única forma que satisfaz **todos** os copos ao mesmo tempo, com pressão igual, é a esfera. A convergência da aula 01 é realizada na máquina como um **equilíbrio dinâmico entre os copos**, cada um vetando o excesso que o outro deixaria passar.

### Por que máquinas comerciais usam três cabeçotes

Duas cabeças já convergem para uma esfera, mas deixam um ponto fraco: assim que a peça se acomoda girando em torno do eixo que liga os dois copos, os dois **polos** desse eixo ficam dentro da boca dos copos e nunca passam pela coroa abrasiva — a região que não é varrida não é desbastada. Máquinas de duas cabeças (os modelos comerciais existem, para peças pequenas e grandes) resolvem isso pelo **tempo**: o operador reassenta a peça entre passagens, trocando qual par de polos fica exposto.

A configuração comercial de referência é a de **três cabeçotes**, oferecida pelos principais fabricantes de equipamento de lapidaria: os três copos, com molas independentes, apontam a peça de três direções que não se alinham entre si, de modo que o polo de um cai na zona ativa de outro. A peça gira de forma irregular, toda a superfície passa pela abrasão e o reassentamento manual deixa de ser necessário. O ganho do terceiro cabeçote não é velocidade — é **uniformidade de convergência**, o mesmo requisito de centro único da aula 01, agora resolvido no espaço em vez de no tempo.

### Da peça bruta ao diâmetro-alvo

A peça de partida (o *sphere blank*) já chega da serra como a preforma de muitas faces da aula 01, reduzindo o volume que a máquina de copos precisa remover — abrasão por copo é lenta comparada ao esmeril, porque o contato é distribuído e a pressão por área é baixa.

O que o copo fixa **não é** o diâmetro final. Os cabeçotes avançam por mola à medida que material sai, e a esfera **encolhe continuamente** enquanto a máquina roda: o processo não estaciona sozinho num raio. Cada tamanho de copo atende a uma **faixa** de diâmetros — um copo de 25 mm, por exemplo, trabalha esferas de cerca de 25 a 35 mm (catálogos de fabricante, acesso 2026-09-04) —, e é o operador quem interrompe o desbaste no diâmetro pretendido, medido com paquímetro. Trocar de copo muda a **faixa** de trabalho; dentro da faixa, o diâmetro-alvo é uma decisão de **quando parar**.

## Exemplo trabalhado

**Uma preforma de ônix, saída de um cubo de 30 mm de aresta, vai virar uma esfera de 25 mm de diâmetro. (Repare no teto geométrico: de um cubo de 30 mm não sai esfera maior que 30 mm — o cubo é o limite superior do diâmetro.)**

**Se a máquina tivesse um eixo só:** a peça converge para o sólido de revolução daquele eixo — a calha decide qual perfil —, mas os dois polos ficam parados dentro da boca do copo, não são varridos e não são desbastados. Nunca vira esfera, por mais que a máquina rode.

**Com dois cabeçotes:** cada copo rebaixa o que se projeta na sua direção, e a peça arredonda — até se acomodar girando em torno do eixo que liga os dois copos, quando os polos desse eixo param de ser varridos. O operador reassenta a peça algumas vezes, expondo polos diferentes, para compensar.

**Com três cabeçotes:** as três direções não se alinham, a peça gira de forma irregular e o polo de um copo cai na zona ativa de outro. Toda a superfície é abradida sem reassentamento manual.

**Onde a máquina para:** em ponto nenhum, por conta própria. Os cabeçotes avançam por mola e a esfera encolhe; quem determina os 25 mm é o operador, com paquímetro. O copo escolhido só precisa ter os 25 mm dentro da sua faixa de trabalho.

## Erros comuns

- **Achar que "girar bastante" contra um copo só produz uma esfera.** Um eixo fixo produz um sólido de revolução daquele eixo, com dois polos que não são varridos — falta a segunda direção de trabalho.
- **Achar que o eixo único obriga a um cilindro.** Quem decide o perfil é a calha da ferramenta, não o número de eixos: com um gabarito de perfil, um eixo único produz um ovo (aula 04). O que ele não produz é uma esfera.
- **Achar que o copo fixa o diâmetro final.** Os cabeçotes avançam por mola e a esfera encolhe até o operador parar; o copo define a **faixa** de diâmetros em que trabalha, não o valor de chegada.
- **Achar que mais cabeçotes aumentam a velocidade de desbaste.** O ganho é a uniformidade da convergência (elimina os polos não varridos), não a rapidez com que material é removido.
- **Ignorar a pré-formação.** Levar um cubo bruto direto à máquina de copos exige que eles removam um volume grande com contato distribuído e pressão baixa — muito mais lento do que reduzir o volume antes na serra e no esmeril do módulo 03.

## O que não concluir

- Não concluir a pressão ou a velocidade de rotação ideais para operar uma máquina de esfera — competência de bancada, fora do nível deste curso.
- Não concluir os defeitos que a heterogeneidade do material (dureza diferencial, bandeamento) impõe a esse processo de convergência — é a aula 03.
- Não concluir como as formas torneadas não-esféricas (ovo, obelisco) usam um princípio de eixo diferente, de eixo único fixo em vez de múltiplos eixos cruzados — é a aula 04.
- Não tomar o diâmetro do exemplo (25 mm) nem a faixa de copo citada (25 a 35 mm para um copo de 25 mm) como especificação: são um caso e um número de catálogo, para mostrar que **existe** faixa, não para decorar.

## Recap relâmpago

- Um eixo fixo, por mais tempo que trabalhe, só produz o **sólido de revolução daquele eixo** — o perfil quem decide é a calha da ferramenta —, e deixa **dois polos** parados no eixo, nunca varridos. Esfera exige no mínimo **dois eixos de contato não paralelos**.
- O **copo de esfera** é um anel com calha côncava, montado num cabeçote que o pressiona por **mola** contra a peça e o faz girar; o contato é uma **coroa**, não um ponto, e rebaixa o que se projeta para fora do raio da calha naquela direção.
- A forma que satisfaz **todos** os copos ao mesmo tempo, com pressão igual, é a esfera: é esse equilíbrio dinâmico que realiza fisicamente a exigência de centro único da aula 01.
- Duas cabeças deixam os polos do eixo que as liga dentro da boca dos copos, sem abrasão; resolve-se no **tempo**, reassentando a peça. **Três cabeçotes** — o arranjo comercial de referência — resolvem no **espaço**: o polo de um cai na zona ativa de outro.
- O ganho do terceiro cabeçote é **uniformidade de convergência**, não velocidade de desbaste.
- O copo **não fixa** o diâmetro final: ele define uma **faixa** de diâmetros de trabalho, a esfera encolhe continuamente enquanto a máquina roda, e quem para o processo no diâmetro-alvo é o operador, medindo com paquímetro.
- A pré-formação (a preforma de muitas faces da aula 01, feita na serra) poupa tempo, porque a abrasão por copo é lenta.

## Próxima aula

Na [[07-esfera-e-torneadas-aula-03-materiais-e-defeitos-undercut-e-bandeamento|Aula 03 — Materiais e defeitos da esfera]]: mesmo com a máquina convergindo corretamente para um centro único, o próprio material pode impedir uma esfera perfeita — resistência diferencial à abrasão produzindo undercut, e o padrão de bandas fora de centro produzindo um defeito distinto, que não deixa relevo nenhum. O critério que separa os dois é o relevo, não o material.

## Fontes consultadas

- Sinkankas, *Gem Cutting: A Lapidary's Manual* — o capítulo de esfera e conta: o princípio do copo, eixos cruzados e a convergência por contato múltiplo.
- Catálogos e fichas técnicas de fabricantes de equipamento de lapidaria — Covington Engineering (máquinas de duas e de três cabeças), Highland Park Lapidary, Kingsley North, Arrowhead Lapidary Supply (acesso 2026-09-04): cabeçotes com mola e ajuste independente; tabela de tamanho de copo × faixa de diâmetro de esfera.
- William Holland School of Lapidary Arts e a taxonomia de disciplinas das guildas norte-americanas — esfera como disciplina própria.
- Lapidary Journal / Rock & Gem — configuração de máquinas de esfera de bancada e a prática de reassentar a peça em máquinas de duas cabeças.

<!--
nivel: ensino-medio-com-gemologia-v1
palavras_corpo: 1590
cobertura:
  lapidacao-m07-oa02: [Conteúdo, "Exemplo trabalhado", "Erros comuns", "O que não concluir", "Recap relâmpago"]
alegacoes_auditaveis:
  - claim_id: MAQ-EIXO-CIL-001
    claim: "Uma peça presa a um único eixo de rotação fixo só pode virar um sólido de revolução em torno DESSE eixo; qual sólido é decidido pelo perfil da ferramenta (borda reta produz cilindro, calha curva produz perfil curvo — é o princípio do copiador de perfil da aula 04), NÃO pelo número de eixos. O que o eixo único não consegue com ferramenta nenhuma são os dois pontos em que ele fura a superfície da peça (os polos), que ficam parados em relação à ferramenta e não são varridos. Como todo sólido de revolução tem dois polos e a esfera é a forma que não admite polo privilegiado, produzir esfera exige no mínimo dois eixos de contato não paralelos."
    risk: causa-efeito
    source: "Geometria de sólidos de revolução; Sinkankas, Gem Cutting: A Lapidary's Manual — necessidade de contato múltiplo para esfera; catálogos de fabricante de máquina de esfera (acesso 2026-09-04)"
  - claim_id: MAQ-COPO-CASADO-001
    claim: "O copo de esfera é um anel abrasivo com calha côncava usinada na borda, montado num cabeçote que o faz girar e o pressiona por MOLA contra a peça; o contato é uma coroa circular, não um ponto, e rebaixa qualquer região da peça que se projete para fora do raio que a calha impõe naquela direção. Com dois ou mais cabeçotes apontando de direções diferentes, a única forma que satisfaz todos os copos ao mesmo tempo, com pressão igual em todos, é a esfera — e é esse equilíbrio dinâmico que realiza fisicamente a exigência de centro único da aula 01."
    risk: definicao
    source: "Sinkankas, Gem Cutting: A Lapidary's Manual — o princípio do copo para esfera e conta; fichas técnicas de fabricante (Covington Engineering, Highland Park Lapidary, acesso 2026-09-04) — cabeçotes com mola, independentes e ajustáveis"
  - claim_id: MAQ-POLO-FRACO-001
    claim: "Numa máquina de duas cabeças, assim que a peça se acomoda girando em torno do eixo que liga os dois copos, os dois polos desse eixo ficam dentro da boca dos copos e não passam pela coroa abrasiva — a causa da sub-abrasão é GEOMÉTRICA (região não varrida), não um gradiente de velocidade linear da superfície abrasiva. Máquinas de duas cabeças compensam isso no tempo: o operador reassenta a peça durante o processo, expondo polos diferentes."
    risk: causa-efeito
    source: "Geometria de contato copo-peça; Sinkankas, Gem Cutting: A Lapidary's Manual; Lapidary Journal / Rock & Gem — prática de reassentamento em máquinas de duas cabeças"
  - claim_id: MAQ-NUM-COPOS-001
    claim: "As configurações comerciais correntes de máquina de esfera são a de DUAS e a de TRÊS cabeças, sendo a de três cabeças o arranjo de referência oferecido pelos principais fabricantes de equipamento de lapidaria (Covington Engineering modelo de três cabeças, Highland Park, Kingsley North, Arrowhead). Nas máquinas de três cabeças os copos apontam de três direções não alinhadas entre si, de modo que o polo de um copo cai na zona ativa de outro, eliminando estruturalmente a região não varrida sem exigir reassentamento manual. O ganho do terceiro cabeçote é uniformidade de convergência, não velocidade de remoção de material."
    risk: dado numerico
    source: "Catálogos de fabricantes de equipamento de lapidaria — Covington Engineering, Highland Park Lapidary, Kingsley North, Arrowhead Lapidary Supply (acesso 2026-09-04): máquinas de duas e de três cabeças, cabeçotes com mola e independentes"
  - claim_id: MAQ-RAIO-ALVO-001
    claim: "O diâmetro final de uma esfera produzida em máquina de copos NÃO é fixado pela máquina: os cabeçotes avançam por mola à medida que material é removido e a esfera encolhe continuamente enquanto a máquina roda, sem estacionar num raio por conta própria. Cada tamanho de copo atende a uma FAIXA de diâmetros de esfera (um copo de cerca de 25 mm trabalha esferas de cerca de 25 a 35 mm, segundo tabela de fabricante), e é o operador quem interrompe o desbaste no diâmetro pretendido, medido com paquímetro. Trocar de copo muda a faixa de trabalho e a granulometria, não determina o valor de chegada."
    risk: causa-efeito
    source: "Highland Park Lapidary — guia de seleção de tamanho de copo (copo de 1 pol/25 mm para esferas de 1 a 1,4 pol/25 a 35,5 mm; copo de 2 pol/50,5 mm para esferas de 2 a 2,6 pol), acesso 2026-09-04; Covington Engineering — cabeçotes com mola, independentes, ajustáveis por manípulo, faixa de 2,5 a 10 pol na máquina de três cabeças"
-->
