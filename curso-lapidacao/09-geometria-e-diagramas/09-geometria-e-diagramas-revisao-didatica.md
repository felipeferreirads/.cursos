# Revisão didática — Módulo 09: Geometria da máquina e leitura de diagramas de lapidação

**Revisado em:** 2026-09-06 · **Modo:** `review-and-fix`
**Material:** `09-geometria-e-diagramas/` — as 6 aulas e o hub do módulo
**Contrato:** `ensino-medio-com-gemologia-v1` (LC-01 a LC-08)
**Veredito:** **Bem ensinado com ressalvas** — nenhum achado bloqueava o aprendizado; quatro prejudicavam. Todos os 10 achados foram corrigidos nesta passagem.

## Resumo

🔴 0 bloqueiam · 🟠 4 prejudicam · 🟡 5 atrito · 🔵 1 sugestão · **0 em aberto**

| Carga | a01 | a02 | a03 | a04 | a05 | a06 |
|---|---|---|---|---|---|---|
| Conceitos novos independentes | 3 | 3 | 4 | 3 | 3 | 3 |
| Pré-requisitos reativados | 2 | 3 | 3 | 2 | 3 | 2 |
| Exemplos trabalhados | 1 | 1 | 1 | 1 | 1 | 1 |
| Duração declarada | 22 min | 24 min | 26 min | 24 min | 24 min | 28 min |
| `palavras_corpo` (teto ~1600) | 1588 | 1598 | 1598 | 1554 | 1600 | 1594 |

Nenhuma aula excede 4 conceitos novos; nenhuma precisou ser dividida. A a03 é a mais carregada (quatro peças — vista de topo, vista lateral, tabela, sequência) e é também a única com 26 min declarados fora da a06; fica no limite, mas as quatro peças são partes de um único artefato, não quatro ideias independentes, e a analogia da planta da casa amarra as três primeiras. Não é caso de divisão.

## O contexto desta revisão: o módulo saiu de uma auditoria pesada

A auditoria científica (`audit-and-fix`, 2026-09-06) fechou com 13 achados sobre 34 alegações — 4🔴 + 7🟠 + 1🔵 + 1⚪, nenhum em aberto. **Quatro aulas tiveram mudança de tese**: a02 (planos paralelos), a03 (a sequência de corte e as definições de *tier* e *main*), a04 (o meetpoint **não** elimina erro cumulativo) e a05 (desvio de fileira inteira é da altura, não do ângulo). O padrão do módulo 08 — a tese muda no corpo e o **entorno** da aula continua ensinando a versão refutada — foi, por isso, o eixo desta revisão.

A auditoria já havia feito a sua própria varredura de resíduo e corrigido um título de seção na a04. **Esta revisão encontrou mais três resíduos que aquela varredura não pegou** (achados 🟠 2, 🟡 6 e 🟡 10 abaixo), porque a busca da auditoria foi por regex sobre as formulações refutadas literais, e os três resíduos sobreviventes usam **outras palavras** para a mesma tese refutada.

---

## Achados 🟠 — prejudicam

### 🟠 1. A a02 fica com uma contradição aparente entre "três coordenadas" e "duas já localizam a faceta"

**Tipo:** modelo mental instável · objetivo central enfraquecido — **resíduo de refutação (a02)**
**Onde:** a02, seções "Altura — a profundidade e o alcance" e "As três juntas".
**Problema:** o 🔴 3 da auditoria substituiu a tese antiga ("duas facetas de mesmo ângulo e índice em alturas diferentes") pela correta ("são planos paralelos; a altura dimensiona, não localiza"). A correção está certa, mas deixou o leitor com duas frases que se contradizem sem mediação: a abertura diz "um plano que precisa de posição **e** de orientação... **dois números não bastam**", e três parágrafos depois lê-se "ângulo e índice, juntos, **já localizam** a faceta na pedra". Quem lê sozinho, sem professor, conclui que a terceira coordenada é supérflua — que é exatamente o oposto do `lapidacao-m09-oa02`. Havia ainda um resíduo literal: o lead-in da lista prometia que mudar uma coordenada "produz **uma faceta diferente**", enquanto o terceiro item da própria lista diz "**a mesma faceta**, maior ou menor".
**Correção aplicada:** mapeamento explícito, usando o "posição e orientação" que a própria abertura já enuncia — ângulo e índice dão a **orientação** do plano, a altura dá a **posição** dele; por isso ângulo e índice bastam para dizer *qual* faceta é aquela e não bastam para descrever *o plano*. E o lead-in passou a "produz um **resultado** diferente e previsível". Nenhum fato novo: a distinção orientação/posição já estava no primeiro parágrafo da aula e na definição de *center-to-facet distance* que a aula cita.
**Escopo:** correção local.

### 🟠 2. A a03 define "fileira" de duas formas contraditórias na mesma aula — e a do corpo é a refutada

**Tipo:** definição inconsistente — **resíduo de refutação (a03)**
**Onde:** a03, seção "A vista lateral: o perfil e as fileiras".
**Problema:** o 🟠 10 da auditoria corrigiu a definição de *tier* para "grupo de facetas **na mesma altura** ao redor da pedra — na prática, mesmo ângulo e mesma altura do mastro". O verbete de vocabulário e o recap foram corrigidos; **a linha do corpo não**, e continuava definindo fileira como "um grupo de facetas com o mesmo ângulo". Não é um detalhe: a a05 inteira depende de o leitor entender que **ângulo e altura são ambos ajustes de fileira** (é a tese do 🔴 2 da auditoria). Um leitor que chega à a05 com "fileira = mesmo ângulo" na cabeça não tem como aceitar o Sintoma 3.
**Correção aplicada:** a linha do corpo alinhada ao verbete — "o grupo de facetas na mesma altura ao redor da pedra, cortadas com o mesmo ângulo".
**Escopo:** correção local.

### 🟠 3. A a03 é uma aula sobre ler um artefato visual e não mostra nem pede o artefato

**Tipo:** abstração sem apoio concreto · descumprimento de item do contexto do curso
**Onde:** a03, seção "A tabela".
**Problema:** o `_contexto.md` lista três pontos em que "ilustração é essencial e a aula deve pedi-la explicitamente", e dois deles são deste módulo: "as três coordenadas da faceta **e o diagrama de lapidação** (m09 a02 e a03)". A a02 traz seu bloco `> **Ilustração pedida**`; **a a03 não trazia nenhum**. É a aula mais visual do curso — o objetivo `lapidacao-m09-oa03` é literalmente ler vista de topo, vista lateral e tabela — e o leitor tinha de reconstruir mentalmente as três peças a partir de prosa.
**Correção aplicada:** bloco `> **Ilustração pedida — um diagrama de lapidação completo.**` com as três peças e a seta ligando cada linha da tabela à fileira que ela descreve, no mesmo formato da a02.
**Escopo:** correção local.

### 🟠 4. O exemplo trabalhado da a06 demonstra o contrário da tese da aula

**Tipo:** exemplo insuficiente — o caso escolhido não discrimina
**Onde:** a06, "Exemplo trabalhado", Passo 3.
**Problema:** a tese central da aula é que **somar graus fixos não é reescalar** (a não linearidade da tangente, LC-06). O exemplo converte 39°→42° na referência e 42,3°→45,33° na auxiliar: deslocamentos de 3° e 3,03°. A diferença é de **três centésimos de grau**. O leitor honesto conclui o oposto do que a aula quer: "então somar 3° em tudo dá no mesmo". A aula percebia o problema e o remendava com uma promessa vaga — "numa faceta de ângulo bem mais alto... produziria um deslocamento visivelmente diferente" — sem nunca mostrar o número que fecharia o argumento.
**Correção aplicada:** o par 68° → 70,03° entrou no lugar da promessa vaga: deslocamento de **2,03°, não 3°**. É o mesmo exemplo da USFG que a aula já cita em "Fontes consultadas" e que a auditoria recalculou de forma independente (70,0307°) — **não é fato novo**, é um dado já verificado que estava fora do corpo da aula.
**Escopo:** correção local.

---

## Achados 🟡 — atrito

### 🟡 5. A resposta operacional do `oa03` some do recap da a03

**Tipo:** recap que não recapitula
**Onde:** a03, "Recap relâmpago" e "Erros comuns".
**Problema:** depois do 🔴 4 da auditoria (não há regra fixa de main antes das auxiliares), o que sobrou como resposta prática ao objetivo — "a ordem das linhas na tabela geralmente **é** a ordem de corte proposta pelo autor" — ficou como parágrafo isolado no fim da seção, e não aparecia no recap. Quem estuda pelo recap saía com a controvérsia e sem a regra de leitura.
**Correção aplicada:** a frase entrou no marcador de sequência do recap; e o marcador correspondente de "Erros comuns" foi condensado para não triplicar a informação.
**Escopo:** correção local.

### 🟡 6. "Cada faceta amassaria uma margem de erro" — a palavra errada trava a frase que monta o problema da a04

**Tipo:** prolixidade/erro de redação em ponto de carga
**Onde:** a04, primeiro parágrafo de "O problema que a técnica resolve".
**Problema:** "amassar" não tem leitura possível ali; a frase é a que estabelece **por que** a técnica existe. Um tropeço lexical no parágrafo de motivação custa desproporcionalmente caro.
**Correção aplicada:** "carregaria".
**Escopo:** correção local.

### 🟡 7. Dois dos seis verbetes do vocabulário da a05 nunca aparecem na aula

**Tipo:** vocabulário desalinhado (LC-01/LC-03)
**Onde:** a05, "Vocabulário desta aula".
**Problema:** a tabela definia "desvio na circunferência" e "desvio radial" — dois termos que **não ocorrem uma única vez** no corpo. Os termos que a aula de fato usa o tempo todo, e dos quais a árvore de diagnóstico depende, são "**posição na volta**" e "**plano radial**", que não estavam no vocabulário. O leitor decora dois rótulos mortos e chega à árvore com os dois vivos indefinidos.
**Correção aplicada:** os dois verbetes trocados pelos termos realmente usados, cada um já com o sintoma que lhe corresponde. Custo zero de `palavras_corpo` (o vocabulário fica fora da régua LC-02).
**Escopo:** correção local.

### 🟡 8. A a05 resvala em instrução de bancada no Passo 3

**Tipo:** proximidade da regra dura do curso
**Onde:** a05, "Exemplo trabalhado", Passo 3.
**Problema:** "**A correção indicada.** Ajustar a altura do mastro para essa faceta, aprofundando o corte até ela alcançar o vértice" espelha a formulação que o `_contexto.md` proíbe nominalmente ("Ajuste o cheater até o meetpoint fechar"). Não é violação consumada — o `oa05` é diagnóstico e nomear a coordenada corretiva faz parte dele, como faz a coluna "Ajuste que corrige" da tabela —, mas a frase lida como ordem de bancada e não como conclusão de diagnóstico.
**Correção aplicada:** reformulado para identificação de coordenada: "A coordenada a corrigir é a **altura do mastro**: é ela que leva o corte ao vértice onde as outras duas já estão."
**Escopo:** correção local.

### 🟡 9. "Vista em planta" e "vista de topo" usadas como sinônimos sem aviso, e um anglicismo no vocabulário da a06

**Tipo:** vocabulário acumulado sem consolidação
**Onde:** a06, "Vocabulário desta aula".
**Problema:** a a03 ensina "vista de topo (*plan view*)"; a a06 introduz "vista em planta" como se fosse coisa nova e depois alterna entre os dois nomes dentro da mesma seção, sem nunca dizer que são a mesma vista. E o verbete saía como "**facet** de referência" enquanto o corpo usa "faceta de referência".
**Correção aplicada:** o verbete agora declara a identidade com a vista de topo da a03 e explica por que o outro nome aparece (é o nome que a literatura de conversão usa); "facet" → "faceta". Custo zero de `palavras_corpo`.
**Escopo:** correção local.

### 🟡 10. O hub e o cabeçalho da a06 ainda descreviam a tabela do diagrama como tendo coluna de altura

**Tipo:** **resíduo de refutação (a06 e hub)** — pré-requisito declarado em desacordo com o que a aula-fonte ensina
**Onde:** hub `09-geometria-e-diagramas-modulo.md`, linha de pré-requisito do módulo 08; a06, linha **Pré-requisito** e "Antes de começar".
**Problema:** o 🟠 6 da auditoria estabeleceu que um diagrama impresso tabela **dois** parâmetros (ângulo e índice) e que a profundidade é fixada na pedra pelo ponto de encontro, não lida de uma coluna. A correção entrou na a02 e na a03 — mas três lugares continuavam ensinando a versão refutada: o hub ("especificação de talhe (ângulo, índice, altura)"), o cabeçalho da a06 ("a tabela de um diagrama, com ângulo, índice e altura por fileira") e o "Antes de começar" da a06 ("um diagrama especifica cada fileira por ângulo, índice e altura"). Os dois últimos são especialmente danosos porque se apresentam ao leitor como **o resumo do que a a03 ensinou** — e dizem o contrário do que ela ensina. A varredura da auditoria não os pegou porque procurava a expressão "três colunas", e estes usam outra formulação.
**Correção aplicada:** os três alinhados a "o ângulo e os índices de cada fileira", com o "Antes de começar" da a06 acrescentando "— a profundidade não vem tabelada". O item 2 das "Pendências de propagação" da auditoria fica assim resolvido.
**Escopo:** correção local. A pendência **cross-course** (item 3 da auditoria: `RAY-MODEL-MEDE-001` e a resposta (a) do questionário do módulo 08) **continua aberta e fora do escopo desta revisão** — módulo fechado, não reaberto.

---

## Achado 🔵 — sugestão

### 🔵 11. A a01 ficou com oito jogos de índice em circulação e cinco tabelados

**Tipo:** carga de números após a correção de escopo — **não é defeito, é aviso para o questionário**
**Onde:** a01, "Por que cinco rodas, e não uma só" e "Erros comuns".
**Observação:** os 🟠 7 e 🟠 8 da auditoria obrigaram a aula a admitir os oito jogos do catálogo (32, 64, 72, 77, 80, 84, 96, 120) enquanto a tabela de divisores trabalha com cinco. A aula faz o escopo direito toda vez ("**entre os cinco**", "fora deles, o 84"), e por isso não há achado. Mas o leitor termina com dois conjuntos na cabeça, e o exemplo trabalhado ainda destaca em negrito "**um único jogo, entre os cinco, cobre essa simetria: o 77**".
**Nenhuma alteração feita.** Fica o aviso para a etapa seguinte, na seção abaixo.

---

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo trabalhado | Recap cobre | Avaliado em |
|---|---|---|---|---|
| `lapidacao-m09-oa01` | a01, "A regra central" + "Os jogos correntes" | sim (8-fold × 7-fold) | sim | pendente |
| `lapidacao-m09-oa02` | a02, as três seções de coordenada + "As três juntas" | sim (facetas A/B/C) | sim | pendente |
| `lapidacao-m09-oa03` | a03, as quatro seções de anatomia | sim (duas linhas de pavilhão) | sim (após 🟡 5) | pendente |
| `lapidacao-m09-oa04` | a04, "A ideia central" + "Por que isso evita medir" | sim (três facetas na culaça) | sim | pendente |
| `lapidacao-m09-oa05` | a05, os três sintomas + a árvore | sim (continuação da a04) | sim | pendente |
| `lapidacao-m09-oa06` | a06, "A fórmula" + "O que o método garante" | sim (quartzo 39°→42°) | sim | pendente |

**Seis objetivos, seis aulas, um para um.** Nenhum objetivo órfão, nenhuma seção órfã, nenhum objetivo formulado com verbo não verificável — os seis usam explicar, descrever, ler, diagnosticar e aplicar. O `oa05` ("diagnosticar") e o `oa06` ("aplicar") são os dois de nível cognitivo mais alto e são também os dois com exemplo trabalhado mais forte, o que está na ordem certa.

## Progressão e pré-requisitos

A cadeia interna é limpa e **cada aula declara e usa o que declara**: a02 usa a01 (índice) e o módulo 03 a05 (batente, mastro); a03 usa a02 e o módulo 08 a06; a04 usa a03 e a02; a05 usa a04 e o módulo 03 a05; a06 usa a03 e o módulo 08 a02. Nenhum pré-requisito declarado ficou sem uso — o sintoma clássico de aula que mudou e cabeçalho que não —, exceto o corrigido no 🟡 10.

Nenhum **salto de pré-requisito** encontrado. Os dois pontos de risco previstos no hub foram tratados na origem: a ambiguidade "índice × índice de refração" é isolada logo no primeiro parágrafo da a01 e reafirmada no vocabulário e no recap da a02 (a auditoria elogiou essa disciplina); e a tangente é reativada antes da fórmula na a06, cumprindo LC-06.

**Pré-requisito externo:** o `curso-gemologia` é citado **só por nome** na a06 ("Módulo 01 do curso de Gemologia (índice de refração)"). Nenhum wikilink para fora do curso em nenhuma das seis aulas — regra dura respeitada.

## Varredura de competência de bancada

**Nenhum achado consumado; um resvalo corrigido (🟡 8).** As seis aulas trazem em "O que não concluir" a exclusão explícita da operação de máquina, e os seis verbos de objetivo são de conhecimento observável. Não há uma única ocorrência de "você vai conseguir lapidar/polir/operar" nem de imperativo de bancada. A a05 é a aula de maior risco estrutural — ela **nomeia ajustes corretivos** —, e resolve isso pela coluna "Ajuste que corrige" da árvore de diagnóstico, que descreve a relação sintoma→coordenada em vez de instruir a mão. Só o Passo 3 do exemplo escapava do registro, e foi reformulado.

## Régua LC-02 e integridade

| Aula | `palavras_corpo` antes | depois | Cortes de compensação |
|---|---|---|---|
| a01 | 1588 | **1588** | — (não alterada) |
| a02 | 1523 | **1598** | nenhum necessário (folga de 77) |
| a03 | 1594 | **1598** | sim — ver abaixo |
| a04 | 1486 (declarava 1484) | **1554** | nenhum necessário |
| a05 | 1599 | **1600** | reformulação word-neutral |
| a06 | 1589 | **1594** | a promessa vaga do Passo 3 trocada pelo dado concreto |

A a03 foi a única a exigir cortes de verdade (o bloco de ilustração custa ~45 palavras). O método é o dos módulos 04 a 08 — **financiar o acréscimo com redundância da própria aula**, nunca comprimindo a correção: saiu "o perfil mostra num relance quantas fileiras a coroa e o pavilhão têm" (redundante com a própria seção); a paráfrase da linha 1 da tabela foi condensada; saiu a terceira remissão consecutiva à a04 na mesma seção; e o marcador "ordem das linhas é arbitrária" de "Erros comuns" foi condensado por passar a duplicar o recap. **Nenhuma correção didática foi encurtada para caber.**

`content_hash` recalculado (SHA256) e `palavras_corpo` regravado nos rodapés das cinco aulas alteradas e no `course-state.yaml`. As 34 alegações auditáveis foram cruzadas por regex após as edições: **todas com 4 segmentos, nenhuma duplicata** — nenhuma edição desta revisão tocou em bloco de alegação.

## O que está bem feito, e precisa ser preservado

- **A disciplina do termo "índice".** A a01 abre isolando as duas grandezas homônimas, o vocabulário da a02 repete a advertência dentro do próprio verbete, "Erros comuns" a repete nas duas aulas e o recap da a02 fecha com ela. É redundância **deliberada** num ponto difícil — exatamente o uso legítimo de repetição em material autodidata — e não deve ser podada em revisão futura por parecer repetitiva.
- **A a05 como aula de diagnóstico.** A estrutura sintoma → coordenada → ajuste, com a árvore em tabela e um exemplo que **continua** o exemplo da a04 em vez de inventar um caso novo, é o melhor pedaço de ensino do módulo. A continuidade entre as duas aulas faz o leitor sentir que o diagnóstico resolve um problema que ele já viu, e não um problema de livro.
- **O tratamento honesto do "o que a técnica não promete" (a04) e do "o que a escolha do índice não determina" (a01).** Seções que dizem o que o conceito **não** faz são raras e valiosas; nas duas aulas elas previnem exatamente a generalização indevida que o leitor faria sozinho.
- **A controvérsia da a03 (LC-08) declarada como pergunta aberta.** "Qual delas é a padrão é questão em aberto: fontes do mesmo nível descrevem as duas, e a escolha pertence ao design" — declarada em uma frase, sem arbitrar, exatamente como o contrato pede.

## Recomendações para o questionário (ETAPA 4)

O módulo não tem questionário nem baralho — o gate funcionou. Cinco travas que a avaliação precisa respeitar, todas nascidas das teses **corrigidas** pela auditoria e reforçadas por esta revisão:

1. **Nunca cobrar `oa01` como "quem alcança 7-fold?" sem escopo.** A resposta certa depende do conjunto: entre os cinco jogos da aula, é o 77; no catálogo real, o 84 também (e só ele alcança 14-fold). Toda questão de 7-fold precisa dizer "entre os cinco jogos estudados". Ver 🔵 11.
2. **Nunca cobrar `oa04` como "o meetpoint elimina o erro cumulativo".** A resposta é **não** — ele dá visibilidade e **controle sobre onde o acúmulo termina** (numa faceta de degrau, de ângulo mais raso, deixada por último). A versão contrária foi o 🟠 5 da auditoria e chegou a estar listada como "erro comum" na aula, isto é, a verdade estava marcada como erro a evitar.
3. **Nunca cobrar `oa05` como "desvio de fileira inteira ⇒ ângulo".** É a armadilha do 🔴 2. Ângulo **e** altura são ajustes de fileira; o que separa os dois é a **inclinação**, não a escala do desvio. Uma boa questão de aplicação é justamente pedir ao aluno que distinga os dois casos de fileira.
4. **Nunca cobrar `oa03` como "main antes das auxiliares".** Não há regra fixa dentro de uma seção (🔴 4 e ⚪ 13). O que é cobrável: a ordem de grande escala (pavilhão → cinta → coroa), o princípio dos **pontos** de referência, e a leitura de índices intercalados como padrão main/break.
5. **Nunca cobrar `oa06` como "o tangent ratio se degrada em designs de grande espalhamento angular".** Inversão corrigida no 🔴 1: quem se degrada é o **atalho** de somar graus fixos; a razão de tangentes preserva a vista em planta por construção. O novo par 68°→70,03° do exemplo dá o dado numérico para uma questão de aplicação limpa.

Uma trava adicional, desta revisão: **`oa02` não pode ser cobrado como "o diagrama tem três colunas"** nem como "duas facetas de mesmo ângulo e índice se distinguem pela altura". A tabela traz ângulo e índice; a profundidade vem do ponto de encontro. Ver 🟠 1 e 🟡 10.

## Nota de método para o módulo 10

A auditoria deste módulo recomendou verificar **procedência** antes de conteúdo. Esta revisão acrescenta uma segunda verificação barata, pelo que encontrou: depois de uma correção de tese, **varrer o entorno por paráfrase, não por regex da frase refutada**. A varredura da auditoria era por expressão literal e pegou um resíduo; os três que sobraram (🟠 2, 🟡 10 em dois lugares) diziam a mesma tese refutada com **outras palavras**, e todos os três estavam em zonas de baixa atenção — a linha do corpo que repete o verbete, o cabeçalho de pré-requisito de outra aula, o "Antes de começar" que resume a aula-fonte, e o hub. Os quatro lugares a ler depois de toda mudança de tese: **verbete de vocabulário, "Antes de começar" das aulas a jusante, títulos de seção e o hub do módulo.**

---

**Arquivos alterados nesta revisão:** as aulas 02, 03, 04, 05 e 06 e o hub do módulo. A aula 01 não foi tocada. Nenhum questionário ou baralho existe para propagar.
