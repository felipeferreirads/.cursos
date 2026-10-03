# Auditoria científica — Módulo 09: Geometria da máquina e leitura de diagramas de lapidação

> [!info] Curso de **Teoria da lapidação** · módulo 09 de 14 · modo **`audit-and-fix`** · profundidade **full** · auditado em **2026-09-06** · **corrigido em 2026-09-06**

**Veredito final: APROVADO — os 13 achados estão fechados.**
*(Veredito da auditoria, antes da correção: **reprovado**.)*

| Severidade | Achados | Desfecho |
|---|---|---|
| 🔴 Erro | **4** | 4 corrigidos |
| 🟠 Impreciso | **7** | 7 corrigidos |
| 🟡 Desatualizado | 0 | — |
| 🔵 Sem fonte | **1** | 1 reescrito com a alegação verificável no lugar da não verificada |
| ⚪ Controverso | **1** | 1 declarado como controvérsia (LC-08 do módulo) |
| **Total** | **13** | **0 em aberto** |
| ✅ Verificado e correto | **21** alegações | 4 delas tocadas por propagação — ver abaixo |

**Gate do curso: LIBERADO.** Nenhum 🔴 ou 🟠 em aberto. Pipeline dos módulos 06+: aulas → auditoria → **correção (concluída)** → **revisão didática** → questionário(s). O questionário **não** deve ser gerado antes da revisão didática. Flashcards seguem dispensados (decisão de 2026-09-04).

**Concentração do dano.** Diferente do módulo 08, onde 3 dos 4 🔴 estavam numa aula só, aqui o dano está **espalhado**: um 🔴 em cada uma das aulas 02, 03, 05 e 06. As aulas 01 e 04 saíram com 🟠 e não com erro estrutural. Os dois pontos que o redator autodeclarou como suspeitos (a fórmula do tangent ratio na a06; os divisores dos jogos de índice na a01) **passaram na verificação numérica** — a fórmula é literalmente a da USFG e o exemplo numérico bate à quarta casa decimal; os divisores estão aritmeticamente certos. O erro estava ao lado deles, na **interpretação** do limite do método e na **atribuição** das fontes.

**Palavras de corpo (LC-02), antes → depois da correção:**
a01 1505 → **1588** · a02 1327 → **1523** · a03 1478 → **1594** · a04 1359 → **1484** · a05 1268 → **1599** · a06 1292 → **1589**.
As seis entraram e saíram sob o teto de ~1.600. A a03 e a a06 precisaram de corte de redundância própria para financiar as correções (método dos módulos 04 a 08); o detalhe de cada corte está na seção "Cortes de compensação". Os rodapés YAML das seis aulas foram atualizados com os novos valores — **`course-state.yaml` ainda declara os antigos e precisa ser realinhado pelo orquestrador.**

**Verificação.** Toda alegação foi conferida contra fonte na web em **2026-09-06**, nada de memória. O exemplo numérico do tangent ratio foi além: recalculado de forma independente, e os três valores publicados pela USFG (45,3348° / 46,9371° / 70,0307°) foram reproduzidos exatamente.

---

## Como ler este relatório depois da correção

Cada achado mantém o texto original da auditoria — o trecho literal citado é o que **estava escrito antes**, não o que está no arquivo agora. Ao fim de cada achado há uma linha **Desfecho** com o que foi efetivamente aplicado.

### O padrão dominante deste módulo: a fonte diz o contrário do que a aula atribui a ela

Três dos quatro 🔴 e dois dos 🟠 têm a mesma forma, e vale nomeá-la porque é a assinatura de erro deste módulo:

> A aula cita uma fonte real, existente e apropriada — e afirma, em nome dela, algo que ela **não diz**, ou que ela diz **ao contrário**.

- 🔴 1 (a06): a USFG diz que o **atalho** de somar graus fixos se degrada com o espalhamento angular; a aula atribuiu a degradação ao **método**.
- 🔴 4 (a03): a USFG *Sequencing Facets* enuncia um princípio sobre a ordem dos **pontos**; a aula lhe atribuiu uma regra sobre a ordem das **fileiras** que a página não contém e que duas outras fontes de referência contradizem.
- 🟠 8 (a01): a citação "*The 77 is 7 and 11 only*" foi atribuída à página *Which Index Gear?* da International Faceting Academy, que **não menciona o jogo de 77 em lugar nenhum**.
- 🟠 11 (a05): overcut e undercut foram atribuídos ao dicionário da USFG, que **não tem esses verbetes**.
- 🟠 6 (a02): o GemCad foi dito especificar a faceta por "altura"; o parâmetro do software é a **center-to-facet distance**.

É a mesma família do `TAB-ALVO-FAIXA-001` e do `RAY-FONTE-USFG-001` do módulo 08. A recomendação para o módulo 10 está na última seção.

### Decisões de julgamento, em resumo

| Achado | Decisão | Por quê |
|---|---|---|
| 🔵 12 `IDX-MAQUINA-PADRAO-001` | **Substituir** a alegação não verificável pela verificável, não removê-la em silêncio | "O 96 acompanha a maioria das máquinas novas" não foi confirmado por fonte nenhuma. Mas a razão real da primazia do 96 **é** documentada e é mais forte: a maioria esmagadora dos diagramas publicados é escrita em notação de 96. A aula ganha, não perde. Precedente do 🔵 `ANG-EX-QUARTZO-001` do módulo 08 (requalificar, não inventar). |
| ⚪ 13 `DIA-SEQ-INICIO-001` | **Declarar** como pergunta aberta, na a03 | Divergência real e documentada entre fontes do mesmo nível sobre qual fileira é cortada primeiro dentro de uma seção. É o LC-08 do módulo, e nasce dentro da reescrita que o 🔴 4 já exigia — custo marginal de três linhas. |

**Uma declaração LC-08, não duas.** O critério fixado nos módulos 06–08 é a **genuinidade**, não a contagem. Esta passa: é divergência documentada entre fontes de referência, no coração do `oa03`. Nenhuma segunda candidata deste módulo passou no mesmo critério — a divergência sobre "qual é o jogo de índice padrão" (🟠 7) não é disputa sobre um fato, é diferença de catálogo entre fabricantes, e foi resolvida por escopo em vez de encenada como controvérsia.

**Nenhum `claim_id` foi renomeado ou reciclado.** Os 32 identificadores originais permanecem com o mesmo nome; três foram criados. Os **34** `claim_id` do módulo foram cruzados por regex contra `^[A-Z]{2,4}-[A-Z0-9]+-[A-Z0-9]+-[0-9]{3}$`: **todos com exatamente 4 segmentos**, nenhum com 5. O bug recorrente do curso não se repetiu.

---

## Achados 🔴 — erro

### 🔴 1. A ressalva sobre o espalhamento angular do tangent ratio está invertida: a fonte acusa o atalho, a aula acusa o método

**claim_id:** `TGR-LIMITE-ESPALHA-001`
**Tipo:** erro factual (inversão da fonte) + inconsistência interna
**Onde:** aula 06 · "Erros comuns" (3º marcador) · "Recap relâmpago" (5º marcador) · rodapé de alegações

**Está escrito:**
> "**Aplicar o método a um espalhamento muito grande de ângulos.** Quanto maior a diferença entre o ângulo mais raso e o mais íngreme do design, mais **a conversão** se afasta de uma vista de topo preservada; a literatura recomenda cautela para designs com grande variação angular."
>
> e, no Recap: "O método perde precisão quanto maior o espalhamento de ângulos do design."

**Problema:** a fonte declarada diz exatamente o oposto, e a aula contradiz a si mesma.

**(a) A fonte acusa o atalho, não o método.** O artigo da USFG citado é literal:

> "as the spread between the lowest and highest pavilion or crown angles increases as is typical with more complex designs, **the practice of adding a constant difference to the angles** breaks down and the results diverge from a tangent ratio conversion. This can cause noticeable deviations in the planview and may also have ramifications for meet points."

O que se degrada com o espalhamento é a **aproximação por soma de graus fixos**, e o que ela produz de ruim são desvios em relação à conversão correta. A conversão pelo tangent ratio é o **padrão-ouro** contra o qual o atalho é medido, não a vítima.

**(b) O tangent ratio preserva a vista em planta por construção, não por aproximação.** O próprio dicionário da USFG define o método como o que traduz um conjunto de ângulos noutro "**while holding the plan view constant**", e o artigo é explícito quanto ao mecanismo: "the height of a facet divided by its base is the tangent of that facet's angle. When you change all the angles… by the tangent-ratio formula, you are changing only the height of each facet in relation to its base; **the base of each facet remains the same**". Escalar todas as tangentes por uma constante é uma dilatação vertical uniforme — uma transformação que, por definição, não toca a projeção horizontal. Não há espalhamento angular que a degrade.

**(c) A aula já se contradizia.** O 1º marcador de "Erros comuns" dizia, corretamente, que somar graus fixos "não é o mesmo que aplicar a tangent ratio… essa aproximação só é aceitável para variações pequenas de ângulo". O 3º marcador afirmava que o problema era do tangent ratio. Os dois não podem estar certos.

**Gravidade.** Este é o `oa06` inteiro. O aluno sairia acreditando que o método central da aula é frágil justamente onde ele é exato, e — pior — desconfiando dele nos designs complexos, que são precisamente onde o atalho é inaceitável e o tangent ratio é obrigatório.

**Fonte:** United States Faceters Guild, *Gemstone Design Conversion Using the Tangent Ratio Method*, usfacetersguild.org — consultada em 2026-09-06 · USFG, *dicionário de facetamento*, verbete **Tangent Ratio** — consultada em 2026-09-06.
**Nível:** normativa (guilda de referência do domínio) · **Confiança:** confirmado.

**Desfecho: CORRIGIDO.** O marcador de "Erros comuns" foi reescrito para nomear o atalho como o culpado e o método como o padrão; o Recap idem; e foi acrescentado, na seção "O que o método garante", um parágrafo que estabelece a preservação da vista em planta **por construção** e situa a soma de graus fixos como aproximação dela, com a citação do dicionário. A alegação no rodapé foi reescrita e marcada como `INVERSAO CORRIGIDA`.

---

### 🔴 2. Um desvio uniforme numa fileira inteira é atribuído ao ângulo — mas a altura do mastro também é um ajuste de fileira

**claim_id:** `DGN-SINT-FILEIRA-001`
**Tipo:** erro factual + inconsistência interna
**Onde:** aula 05 · "Sintoma 3" · tabela "Organizando o diagnóstico" · "Erros comuns" · "Recap relâmpago" · exemplo trabalhado (Passo 2)

**Está escrito:**
> "Quando não é uma faceta isolada, mas uma **fileira inteira** que apresenta o mesmo desvio — **todas mais curtas, todas mais longas**, ou todo o brilho da fileira visivelmente diferente da vizinha —, … O culpado é o **batente de ângulo** … **Índice e altura não explicariam um padrão que afeta a fileira inteira do mesmo jeito — eles são ajustes por faceta ou por pequeno grupo, não por fileira completa.**"

**Problema:** a premissa que sustenta o diagnóstico é falsa. **A altura do mastro não é um ajuste por faceta — é um ajuste por fileira**, exatamente como o batente de ângulo. O procedimento documentado é inequívoco:

> "When you finish cutting all around the rough **at the same mast height**, lower the mast height a little and repeat this procedure." (The Gemology Project / Geosciences LibreTexts)

Ou seja: trava-se o ângulo, fixa-se a altura, corta-se a fileira inteira girando **só o índice**, e só depois a altura desce para a fileira seguinte. Um erro de altura, portanto, sai **uniforme na fileira inteira** — e o sintoma que ele produz é precisamente "todas mais curtas, todas mais longas", que a aula listou como evidência de erro de ângulo.

**A aula contradiz a si mesma no espaço de dois parágrafos.** O "Sintoma 2", imediatamente acima, ensina — corretamente, e citando o módulo 03 — que faceta **curta ou longa** com o ângulo certo é sintoma de **altura**. O "Sintoma 3" toma o mesmo sintoma, multiplica-o por uma fileira, e conclui **ângulo**. A escala do desvio não muda a sua natureza.

**O erro foi introduzido aqui, não herdado.** O módulo 03, aula 05 (já auditado e aprovado), descreve o *Diagnóstico 3* com cuidado: "*Uma fileira inteira ficou com **brilho diferente** da vizinha… é a fileira toda com a **inclinação** errada. Ajuste: batente de ângulo.*" Ele fala de **inclinação**, e nunca de "todas mais curtas ou mais longas". Foi a aula 05 do módulo 09 que alargou o sintoma para incluir o caso que pertence à altura.

**Gravidade.** É o `oa05` inteiro — o objetivo é justamente *diagnosticar qual das três coordenadas está fora*. Uma árvore de decisão que manda mexer no batente quando o problema é a altura do mastro é pior que nenhuma árvore: ela produz um segundo erro (a fileira inteira reinclinada) em cima do primeiro.

**Fonte:** The Gemology Project, verbete *Faceting*, gemologyproject.com · Geosciences LibreTexts 17.2 *Faceting*, geo.libretexts.org — ambas consultadas em 2026-09-06 · curso de lapidação, módulo 03 aula 05 (texto original preservado).
**Nível:** base de referência + consistência interna do curso · **Confiança:** confirmado.

**Desfecho: CORRIGIDO.** O "Sintoma 3" foi reescrito e retitulado para "**uma fileira inteira desviada, e por que ela tem duas causas**", abrindo com o fato mecânico (duas coordenadas são reguladas por fileira) e desdobrando-se em duas leituras: fileira uniformemente curta ou longa com inclinação certa → **altura do mastro**; fileira com a inclinação errada → **ângulo**. A tabela de diagnóstico ganhou uma quinta linha e teve a quarta requalificada. O Passo 2 do exemplo trabalhado foi reescrito para descartar o ângulo **pela inclinação** e não pela escala do desvio. Foi acrescentado um marcador em "Erros comuns" contra o atalho "afeta a fileira inteira, logo é ângulo", e o Recap foi refeito. A alegação `DGN-TABELA-RESUMO-001` foi realinhada.

---

### 🔴 3. Duas facetas com o mesmo ângulo e o mesmo índice, em alturas diferentes, não existem — e o exemplo trabalhado inteiro se apoiava nelas

**claim_id:** `COO-INDEPEND-EIXO-001` (com `COO-INDICE-DEF-001` e `COO-ALTURA-DEF-001` afetados)
**Tipo:** erro factual (geometria) + inconsistência interna
**Onde:** aula 02 · "Altura — a profundidade e o alcance" · "As três juntas" (2º marcador) · **exemplo trabalhado, integralmente** · "Recap relâmpago" · rodapé de alegações

**Está escrito:**
> "Duas facetas podem ter o mesmo ângulo e o mesmo índice — a mesma inclinação, a mesma direção — e ainda assim serem cortes diferentes, um mais raso e outro mais profundo, porque a altura difere."
>
> "- Mesmo ângulo e índice, altura diferente → … facetas em camadas na mesma linha radial, **como um main e um break vizinhos na mesma direção**."
>
> e o exemplo trabalhado: "*Faceta A — ângulo 43°, índice 8, altura 6,0 mm. Faceta B — ângulo 43°, índice 8, altura 5,2 mm*", concluído com "*é o padrão de um main (mais raso) seguido por um break mais fundo exatamente na mesma direção*".

**Problema:** essas duas facetas não podem coexistir numa pedra. Ângulo e índice fixam a **orientação do plano**; dois planos com a mesma orientação são **paralelos**. Num sólido convexo, cortar o segundo plano mais fundo que o primeiro simplesmente **consome** o primeiro: sobra uma faceta só, a mais profunda. Não há como olhar para uma pedra e ver duas facetas paralelas no mesmo índice.

A fonte é explícita quanto ao ponto: o ângulo e o índice, juntos, "**uniquely locate each facet on the stone's surface**" — cortar mais fundo no mesmo ângulo e índice "will indeed make the facet larger without changing its position or **creating distinct parallel facets**".

**E o exemplo escolhido é o pior possível.** Uma main e uma break vizinhas **não** se distinguem por altura: distinguem-se por **ângulo**. A própria aula 03 deste módulo, dois arquivos adiante, apresenta a tabela canônica com **main a 42° e break a 46°** e comenta a diferença de quatro graus. A aula 02 e a aula 03 ensinavam coisas incompatíveis sobre o mesmo par de fileiras.

**Gravidade.** O `oa02` é "descrever as três coordenadas". O modelo mental que a aula instalava — três coordenadas que geram facetas distintas de forma simétrica entre si — é falso, e é o modelo do qual a a03 (leitura da tabela) e a a05 (diagnóstico) dependem. A verdade é assimétrica e mais útil: **ângulo e índice localizam a faceta; a altura a dimensiona.**

**Fonte:** Sky Jems, *Faceting Diagram*, skyjems.ca — consultada em 2026-09-06 · Robert W. Strickland, *GemCad for Windows — User's Guide* (a faceta como plano definido por ângulo, índice e *center-to-facet distance*) · geometria direta de planos paralelos num sólido convexo · curso de lapidação, módulo 09 aula 03 (tabela main 42° / break 46°).
**Nível:** base de referência + derivação geométrica · **Confiança:** confirmado.

**Desfecho: CORRIGIDO.** A frase da seção "Altura" foi substituída por uma advertência explícita (os dois planos são paralelos, o mais fundo consome o mais raso). O marcador de "As três juntas" foi reescrito, reordenado (o caso do ângulo passou à frente) e passou a dizer que fileiras vizinhas se distinguem **por ângulo, nunca por altura**. O **exemplo trabalhado foi refeito por completo**: agora compara A(43°, índice 8) com B(43°, índice 32) — cópia simétrica — e com C(39°, índice 8) — outra fileira na mesma direção, e reserva o Passo 3 para mostrar o que a altura *não* faz. O Recap foi refeito. As alegações `COO-INDICE-DEF-001` e `COO-INDEPEND-EIXO-001` foram reescritas, com `COO-INDEPEND-EIXO-001` promovida de `risk: interpretacao` para `risk: mecanismo`.

---

### 🔴 4. "Main antes das fileiras auxiliares" é apresentada como a regra do ofício, atribuída a uma fonte que não a enuncia e contradita por duas outras

**claim_id:** `DIA-SEQ-ORDEM-001` (com `PTO-SEQ-DEPENDE-001` afetado na a04)
**Tipo:** erro factual + atribuição de fonte falsa + certeza indevida
**Onde:** aula 03 · "A sequência: em que ordem a tabela é percorrida" · vocabulário (verbete *main*) · exemplo trabalhado (Passo 4) · "Erros comuns" · "Recap relâmpago" — **propagado** para a aula 04 ("Antes de começar", "Onde a sequência da aula 03 se encaixa", Recap)

**Está escrito:**
> "Dentro de cada seção, a fileira main — a maior, **a que estabelece o contorno geral** — costuma vir antes das fileiras auxiliares (break, star)"
>
> e, na a04: "não é um costume arbitrário: **é exatamente a ordem que o meetpoint exige**."

**Problema:** três problemas encadeados.

**(a) A fonte citada não diz isso.** O artigo *Sequencing Facets* da USFG enuncia um princípio sobre **pontos**, não sobre fileiras:

> "the sequencing of facets is determined by **the order in which points on the stone must be made**, and the two most common starting places were either **a culet point or a set of girdle points**"

E o que ele recomenda deixar por último é o oposto do que a aula deduziu: as facetas **ajustáveis, de ângulo mais raso**, para absorver o erro acumulado — "if you can let your accumulation of small errors end up on a step facet, you can often save yourself the necessity of cheating". No pavilhão, a faceta de ângulo mais raso é justamente a **main**.

**(b) Duas fontes de referência descrevem a ordem inversa.** The Gemology Project dá, para a coroa: *break* (47°) → *main* (42°) → *star* (27°) → mesa. O Geosciences LibreTexts dá, para o pavilhão: facetas *break* primeiro, depois as mains. A regra da aula falha em ambas.

**(c) "A main estabelece o contorno geral" é falso em qualquer das ordens.** Quem estabelece o contorno — a linha da cinta — são as facetas de cinta / *break*. As mains do pavilhão estabelecem o **ponto de culaça**. A aula trocou as funções.

**O que sobrevive.** A convenção de **grande escala** (pavilhão → cinta → coroa → mesa) está correta e confirmada, e o princípio "cada fileira é cortada contra facetas que já existem" está correto e é o que a a04 realmente precisa. O que não sobrevive é a regra de ordem interna e a atribuição.

**Gravidade.** É o `oa03` ("extrair do diagrama a sequência de corte") e vaza para o `oa04`, onde é apresentada como necessidade lógica do meetpoint — elevando uma convenção contestada ao estatuto de teorema.

**Fonte:** United States Faceters Guild, *Sequencing Facets*, usfacetersguild.org — consultada em 2026-09-06 · The Gemology Project, verbete *Faceting* · Geosciences LibreTexts 17.2 *Faceting* · GemologyOnline.com, *Preform vs Meetpoint faceting* — todas consultadas em 2026-09-06.
**Nível:** normativa (USFG) + base de referência · **Confiança:** confirmado.

**Desfecho: CORRIGIDO.** A seção de sequência da a03 foi reescrita: a convenção de grande escala permanece, e a regra interna foi substituída pelo princípio da USFG (a ordem é a dos pontos a estabelecer), pelas duas partidas correntes, pela declaração de controvérsia (⚪ 13) e pela doutrina das facetas ajustáveis por último. O verbete *main* e o Passo 4 do exemplo foram refeitos; um marcador novo entrou em "Erros comuns" e o Recap foi refeito. Na a04, foram corrigidos o "Antes de começar", a seção "Onde a sequência da aula 03 se encaixa" e o Recap, com a alegação `PTO-SEQ-DEPENDE-001` reescrita e remetendo a `DIA-SEQ-INICIO-001`.

---

## Achados 🟠 — impreciso

### 🟠 5. "O meetpoint evita erro cumulativo" — a fonte citada diz que o erro se acumula e ensina onde enterrá-lo

**claim_id:** `PTO-ERRO-LOCAL-001`
**Tipo:** erro factual contra a fonte citada · omissão que gera erro
**Onde:** aula 04 · **título de seção** · "Por que isso evita medir profundidade…" · "Erros comuns" (3º marcador) · "Recap relâmpago" · exemplo trabalhado (Passo 2)

**Está escrito:**
> "o erro não se acumula progressivamente… cada corte 'reseta' a referência para o próximo, em vez de herdar o erro de todos os anteriores"
>
> e, em "Erros comuns", a afirmação era ensinada como correção de uma concepção errada: "**Supor que o erro se acumula…** É o oposto: cada encontro correto 'reseta' a referência."

**Problema:** o artigo da USFG que a aula cita trata a acumulação de erro como um **fato a ser administrado**, não como um problema que o meetpoint dissolve:

> "Whenever you chain around the stone, look for a point at or near the end of the chain where you can make an adjustment which will **bury any accumulated errors**."
>
> "if you can let your **accumulation of small errors** end up on a step facet, you can often save yourself the necessity of cheating."

E a comunidade é explícita quanto à causa: nenhuma máquina é perfeitamente repetível — "the errors build up in one place, build down in another, and occasionally a miracle occurs and the errors cancel each other out".

A aula não só afirmava o contrário: afirmava-o **em "Erros comuns"**, isto é, marcava a verdade como sendo o erro a evitar. O aluno que já soubesse a coisa certa seria corrigido para a errada.

**O que sobrevive, e é o ponto real.** A vantagem do meetpoint não é imunidade ao acúmulo — é **visibilidade** (o desvio aparece no encontro em que se manifesta) e **controle sobre onde o acúmulo vai parar** (a cadeia é planejada para terminar numa faceta ajustável). Isso é mais interessante que a versão falsa, e conecta-se diretamente à doutrina das facetas de ângulo mais raso deixadas por último, que o 🔴 4 trouxe para a a03.

**Fonte:** United States Faceters Guild, *Sequencing Facets* · GemologyOnline.com, *Meetpoint Madness* — ambas consultadas em 2026-09-06.
**Nível:** normativa + fórum especializado (para a formulação coloquial) · **Confiança:** confirmado.

**Desfecho: CORRIGIDO.** A segunda metade da seção foi reescrita com um parágrafo que desfaz explicitamente o otimismo ("Aqui cabe desfazer um otimismo fácil"), afirma que o erro se acumula, e reposiciona a vantagem como visibilidade + controle sobre onde o acúmulo é absorvido. O marcador de "Erros comuns" foi invertido para "**Achar que o meetpoint elimina o erro acumulado**". O Recap foi refeito. O Passo 2 do exemplo trabalhado foi requalificado ("isso não prova que a causa nasceu ali"). **E o título da seção foi corrigido** — ver "Resíduo de refutação" abaixo.

---

### 🟠 6. O terceiro parâmetro do GemCad não é "altura", e um diagrama impresso não tabela três coordenadas por faceta

**claim_id:** `COO-TRES-EIXO-001` (com `DIA-TRES-PECAS-001` afetada na a03)
**Tipo:** nomenclatura imprecisa + inconsistência interna (pré-refutação da a04)
**Onde:** aula 02 · "Por que uma faceta precisa de três números" · "As três juntas" · "Recap relâmpago" · "Fontes consultadas" — e aula 03, "A tabela: onde as coordenadas viram números" e Recap

**Está escrito:**
> "o **GemCad** … especifica cada faceta por **índice, ângulo e altura**"; nas fontes, "(mast angle, index, elevation/height)"
>
> e, no Recap: "É essa independência de três eixos que permite a um diagrama de lapidação especificar qualquer faceta com só três números, um por coordenada — cada faceta, uma linha da tabela."
>
> e, na a03: "traz **três colunas centrais**: ângulo, índice … e, quando necessário, altura."

**Problema:** dois pontos.

**(a) Nomenclatura.** O parâmetro do GemCad é a **center-to-facet distance** — "the distance from the plane of the facet to the origin (0,0,0) at the center of the stone, measured perpendicular to the plane of the facet". Não é uma altura, e não é medida ao longo do mastro. *Mast angle* e *index* são termos reais das tabelas; "elevation/height" não é o nome do terceiro parâmetro.

**(b) O ponto sério: a a02 pré-refutava a a04.** Se o diagrama entregasse a profundidade de cada faceta como um número tabelado, o meetpoint faceting não teria razão de existir — e a a04, duas aulas adiante, ensina exatamente que "não se corta até uma profundidade medida, corta-se até um ponto de encontro". As tabelas publicadas dão **ângulo e índice**; a terceira coordenada é fixada na pedra, pelo encontro. A a02 instalava uma expectativa que a a04 precisava desfazer sem nunca reconhecer que a estava desfazendo.

**Fonte:** Robert W. Strickland, *GemCad for Windows — User's Guide* · Sky Jems, *Faceting Diagram* ("together, these two parameters uniquely locate each facet on the stone's surface") — consultadas em 2026-09-06.
**Nível:** base de referência (documentação do próprio software) · **Confiança:** confirmado.

**Desfecho: CORRIGIDO.** Na a02, a menção ao GemCad passou a nomear a *center-to-facet distance* e a explicar que a altura do mastro é como a **máquina** realiza essa coordenada; o Recap passou a dizer que o diagrama tabela normalmente **dois** dos três, remetendo à a04; a linha de fontes foi refeita com a definição literal. Na a03, "três colunas centrais" virou "duas colunas centrais" com a ressalva sobre a profundidade, e o Recap acompanhou. A alegação `DIA-TRES-PECAS-001` foi reescrita.

---

### 🟠 7. "Os cinco jogos mais citados" e "de longe a maior cobertura" não se sustentam; e a razão da primazia do 96 é outra

**claim_id:** `IDX-JOGO-CORRENTE-001`
**Tipo:** confusão de escopo + certeza indevida
**Onde:** aula 01 · "Os jogos correntes e o que cada um libera" · "Por que cinco rodas, e não uma só" · "Erros comuns" (4º marcador)

**Está escrito:**
> "Os **cinco mais citados** são 32, 64, 77, 80 e 96 dentes."
>
> "O 96 é o mais versátil da lista — cobre onze simetrias diferentes, **de longe a maior cobertura**, e é por isso que a literatura o cita como o jogo padrão."

**Problema:** três imprecisões.

**(a) O catálogo corrente tem oito jogos, não cinco.** A Ultra Tec lista 32 – 64 – **72** – 77 – 80 – **84** – 96 – **120**. Os três ausentes da aula não são obscuros: a International Faceting Academy recomenda começar por 96 e 120 e declara seu próprio kit como "96, 120, 72, and 84" — sem o 77. E, entre os cinco da aula, o 80 é descrito na literatura como "rarely encountered" e o 77 como servindo designs "pretty rare".

**(b) "De longe a maior cobertura" é falso.** O 96 cobre 11 simetrias — e o **72 e o 84 cobrem 11 também**, enquanto o **120 cobre mais** (14, pela contagem da mesma fonte). Não há folga, muito menos "de longe".

**(c) A razão real da primazia do 96 é mais forte que a alegada.** Não é a amplitude de cobertura: é a **notação**. "The overwhelming majority of published facet diagrams are written to 96-index notation" — o 96 é a língua franca do ofício, e é por isso que se compra um.

**Restrição de escopo.** O `oa01` fixa exatamente estes cinco jogos, e o objetivo não pode ser alterado por uma auditoria. A correção é de **enquadramento**: apresentá-los como o recorte que a aula usa dentro de um catálogo maior, e não como "os mais citados".

**Fonte:** ULTRA TEC Faceting, catálogo de *Index Gears* · International Faceting Academy, *Which Index Gear?* · Sky Jems, *96 Index: The Standard Indexing Gear in Faceting* · GemologyOnline.com, *Index Gears* — todas consultadas em 2026-09-06.
**Nível:** fabricante + escola especializada + base de referência · **Confiança:** confirmado.

**Desfecho: CORRIGIDO.** O parágrafo de abertura passou a declarar o catálogo de oito e a explicitar que a aula trabalha com cinco deles, escolhidos por exporem os fatores primos que decidem a simetria. A seção "Por que cinco rodas" foi reescrita: 96 "o mais versátil **dos cinco**", empate com 72 e 84 declarado, 120 acima, e a razão real (notação) posta como a explicação de fundo. O 4º marcador de "Erros comuns" foi refeito. Fontes acrescentadas com as citações literais.

---

### 🟠 8. "Quem quiser 7-fold precisa do 77" é falso fora dos cinco jogos — e a citação de apoio foi atribuída a uma página que não menciona o 77

**claim_id:** `IDX-DIVISOR-TAB-001`
**Tipo:** confusão de escopo + atribuição de fonte falsa + inconsistência interna
**Onde:** aula 01 · "Por que cinco rodas, e não uma só" · exemplo trabalhado (lição final) · rodapé de alegações

**Está escrito:**
> "quem quiser cortar um talhe de simetria 7-fold **precisa do 77**, porque nenhuma combinação de 2, 3 ou 5 alcança 7"
>
> "ele preenche **o único buraco** que o 96 deixa"
>
> e, no rodapé, a fonte: "corroborado por International Faceting Academy, *Which Index Gear?* ('**The 77 is 7 and 11 only**'…)"

**Problema:**

**(a) O 84 também carrega o fator 7** — 84 = 2² × 3 × 7 — e a própria International Faceting Academy escreve que "**only the 84 will let you do 7-fold or 14-fold symmetry**". O 84 dá inclusive a simetria **14-fold**, que o 77 não alcança. Um usuário de fórum relata ter recarregado um design de 77 no GemCad e visto que ele "mapped perfectly at 84".

**(b) A citação atribuída não está na página citada.** A página *Which Index Gear?* da International Faceting Academy **não menciona o jogo de 77 em lugar nenhum**. A formulação "the 77 is 7 and 11 only" circula na comunidade (GemologyOnline), não naquele artigo. É o mesmo defeito do `RAY-FONTE-USFG-001` do módulo 08: conteúdo defensável, rota de verificação quebrada.

**(c) "O único buraco que o 96 deixa" contradiz a própria aula.** Dois parágrafos acima, a aula ensina que o 80 é "a única forma de chegar a 5 e 10-fold", porque o 96 **não tem o fator 5**. O 96 deixa dois buracos entre os cinco, não um.

**O que passou.** A **tabela de divisores em si está aritmeticamente correta** — 32 {2,4,8,16,32}, 64 {2,4,8,16,32,64}, 77 {7,11,77}, 80 {2,4,5,8,10,16,20,40,80}, 96 {2,3,4,6,8,12,16,24,32,48,96} — conferida por cálculo direto, assim como o exemplo trabalhado (8-fold em quatro dos cinco; 7-fold só no 77, e ali corretamente escopado como "entre os cinco").

**Fonte:** International Faceting Academy, *Which Index Gear?* · GemologyOnline.com, *Index Gears* — consultadas em 2026-09-06 · cálculo direto de divisores.
**Nível:** escola especializada + fórum (para a formulação) · **Confiança:** confirmado.

**Desfecho: CORRIGIDO.** A frase da seção passou a escopar "entre os cinco desta aula" e a nomear o 84 (com o fator 7 e a simetria 14-fold) como a alternativa fora da lista. A lição final do exemplo passou a falar em "um dos **dois** buracos que o 96 deixa entre os cinco", nomeando o fator 5 / jogo 80 como o outro. A alegação no rodapé ganhou um bloco `RESSALVA DE ESCOPO` e a fonte foi corrigida, com a nota explícita de que a página da IFA não menciona o 77.

---

### 🟠 9. Uma única razão para "o design inteiro" — pavilhão e coroa são convertidos em separado

**claim_id:** `TGR-METODO-DEF-001`
**Tipo:** omissão que gera erro
**Onde:** aula 06 · "A fórmula" · "Recap relâmpago" · rodapé de alegações

**Está escrito:**
> "aplica-se essa mesma razão a cada outro ângulo **do design**" · "é reaplicada a **todas as demais facetas do design**" · "reescala um design de talhe **inteiro**"

**Problema:** a fonte é explícita quanto ao escopo da conversão, e o escopo é a **seção**, não o design:

> "If you do want to lower or raise the crown angles, that normally gets done as a **separate and independent conversion** from the pavilion angles."
>
> "in the circumstance where you wanted to convert both a crown and pavilion using the same tangent ratio there is no mathematical reason you can't calculate them together. However, **in practice this circumstance is usually not the case**."

E a formulação da regra de preservação é, ela própria, por seção: "all of the angles on a **pavilion or crown** must be scaled proportionately in order to preserve its original planview". Um aluno que aplicasse a razão do pavilhão à coroa estaria fazendo algo matematicamente possível mas que o ofício quase nunca quer — e perderia a razão pela qual o método é usado na prática (rebaixar a coroa por falta de material sem mexer no pavilhão já cortado).

**Fonte:** United States Faceters Guild, *Gemstone Design Conversion Using the Tangent Ratio Method* — consultada em 2026-09-06.
**Nível:** normativa · **Confiança:** confirmado.

**Desfecho: CORRIGIDO.** A fórmula passou a dizer "a cada outro ângulo **da mesma seção**", e foi acrescentado um parágrafo de ressalva de escopo declarando a conversão separada de pavilhão e coroa e registrando que nada na matemática o impede — só a prática. O Recap acompanhou. A alegação ganhou um bloco `RESSALVA DE ESCOPO` com as três citações literais.

---

### 🟠 10. *Tier* não é "mesmo ângulo" e *main* não é "a mais numerosa" — as duas definições contra o dicionário normativo

**claim_id:** `DIA-FILEIRA-NOME-001` (com o vocabulário da a02 afetado)
**Tipo:** nomenclatura imprecisa
**Onde:** aula 03 · vocabulário (*fileira*, *main*) · "A vista lateral" · "Erros comuns" · "Recap" — e aula 02, vocabulário (*tier*)

**Está escrito:**
> "**tier (fileira)** — um grupo de facetas que compartilham o **mesmo ângulo**"
>
> "**main** — a fileira de facetas **maiores e mais numerosas**"

**Problema:** o dicionário da USFG define as duas de outro jeito.

- **Tier:** "a group of facets **at the same elevation** around the stone. It may be made up of one or more sets of facets." A definição é por **elevação**, não por ângulo. Na prática, uma fileira compartilha o ângulo *e* a altura do mastro — e essa segunda metade não é um detalhe: é exatamente o fato mecânico que o 🔴 2 precisou para corrigir o diagnóstico da a05.
- **Main Facets:** "a set of **large** facets which extend from Girdle to Table on the Crown, or from Girdle to Culet on the Pavilion." São as **grandes** e as que **atravessam a seção** — e são tipicamente as **menos** numerosas: num brilhante redondo, oito mains de pavilhão contra dezesseis facetas de cinta.

**Fonte:** United States Faceters Guild, *dicionário de facetamento*, verbetes *Tier* e *Main Facets* — consultada em 2026-09-06 · contagem do brilhante redondo padrão.
**Nível:** normativa · **Confiança:** confirmado.

**Desfecho: CORRIGIDO.** Os verbetes de vocabulário das aulas 02 e 03 foram refeitos segundo o dicionário. A seção "A vista lateral" da a03 passou a definir a main pela travessia da seção e a registrar a contagem 8 × 16 do brilhante redondo. "Erros comuns" e Recap acompanharam. A alegação foi reescrita com as duas definições literais e a nota de que o dicionário **não** define main como a fileira mais numerosa.

---

### 🟠 11. Overcut e undercut: atribuição falsa, assimetria omitida, e um terceiro sentido de "undercut" no curso sem aviso

**claim_id:** `DGN-OVERCUT-VOCAB-001` — **novo**
**Tipo:** atribuição de fonte falsa + omissão que gera erro + colisão de terminologia interna
**Onde:** aula 05 · vocabulário · "Erros comuns" (3º marcador) · "Fontes consultadas"

**Está escrito:**
> Fontes: "United States Faceters Guild, *dicionário de facetamento* — **vocabulário de overcut e undercut** como desvios de profundidade em relação ao meetpoint planejado."
>
> "Undercut (curto) e overcut (passou do ponto) pedem ajustes de altura **em direções opostas**."

**Problema:** três pontos.

**(a) O dicionário da USFG não tem esses verbetes.** Foram procurados diretamente: *overcut* e *undercut* estão **ausentes**. Os termos são reais e correntes no ofício, mas não vêm dessa fonte.

**(b) Os dois não são simétricos, e tratá-los como simétricos é o erro caro.** A prática é clara: "**if you overcut, you need to recut all the facets you've cut before it.** In contrast, **if you undercut, you can go back and finish it up**." Um undercut é falta de corte, e o corte que falta ainda pode ser feito. Um overcut é irreversível — material removido não volta —, e recuperar o encontro obriga a refazer as facetas vizinhas numa profundidade nova. Apresentá-los como "ajustes de altura em direções opostas" sugere uma reversibilidade que não existe num deles.

**(c) É o terceiro sentido de "undercut" neste curso, e nenhum aviso foi dado.** O módulo 03, aula 01, define **sub-corte (undercut)** como o rasgo fora do plano por flexão da lâmina fina; o módulo 07, aula 03, define **undercut** como a depressão por resistência diferencial à abrasão — e essa aula foi objeto de um achado próprio na auditoria do módulo 07. Introduzir um terceiro sentido sem declarar a colisão é exatamente o tipo de armadilha que o LC-01 existe para evitar, e que a própria a01 deste módulo trata com cuidado exemplar no caso de "índice".

**Fonte:** United States Faceters Guild, *dicionário de facetamento* (verbetes ausentes, verificado) · GemologyOnline.com, *Meetpoint Madness* — consultadas em 2026-09-06 · curso de lapidação, módulo 03 aula 01 e módulo 07 aula 03.
**Nível:** normativa (para a ausência) + fórum especializado (para o uso) · **Confiança:** confirmado.

**Desfecho: CORRIGIDO.** O verbete de vocabulário ganhou uma advertência explícita nomeando os outros dois sentidos e seus módulos. O 3º marcador de "Erros comuns" foi substituído por "**Tratar undercut e overcut como simétricos**", com a assimetria explicada. A linha de fontes foi refeita: o dicionário da USFG passou a ser citado pelos verbetes que **tem** (*cheater*, *index gear*, *meetpoint*, *tier*), com a nota de que não traz overcut nem undercut, e a GemologyOnline entrou como fonte do uso e da assimetria. Alegação nova `DGN-OVERCUT-VOCAB-001` criada.

---

## Achado 🔵 — sem fonte

### 🔵 12. "O 96 acompanha a maioria das máquinas novas" não foi confirmado por fonte nenhuma

**claim_id:** `IDX-MAQUINA-PADRAO-001` — **novo**
**Tipo:** evidência insuficiente
**Onde:** aula 01 · "Por que cinco rodas, e não uma só"

**Está escrito:** "é por isso que a literatura o cita como **o jogo padrão da maioria das máquinas novas**."

**Problema:** a afirmação é específica, verificável e não foi confirmada. As fontes consultadas sustentam que o 96 é **o jogo padrão do ofício** — mas por notação de diagrama, não por política de fábrica —, e os fabricantes vendem jogos de índice como **acessórios avulsos** (Ultra Tec, Facetron, Graves), o que torna "acompanha a máquina" uma alegação sobre configuração comercial que nenhuma fonte consultada faz. Não é acusação de falsidade: é sinalização de que a rota de verificação não existe.

**Nível:** — · **Confiança:** não verificado.

**Desfecho: REESCRITO — a alegação não verificável deu lugar à verificável.** Não foi inventada substituição nem removida em silêncio: a frase passou a atribuir a primazia do 96 à razão que **é** documentada ("the overwhelming majority of published facet diagrams are written to 96-index notation"), que é mais forte e mais útil para o aluno que a alegação original. A alegação `IDX-JOGO-CORRENTE-001` incorporou essa formulação e a nota de que a razão de fundo **não** é a amplitude de cobertura. Segue o precedente do 🔵 `ANG-EX-QUARTZO-001` do módulo 08: requalificar em vez de inventar.

---

## Achado ⚪ — controverso

### ⚪ 13. Qual fileira é cortada primeiro dentro de uma seção — divergência real entre fontes do mesmo nível

**claim_id:** `DIA-SEQ-INICIO-001` — **novo**
**Tipo:** controvérsia
**Onde:** aula 03 · "A sequência: em que ordem a tabela é percorrida"

**A divergência:**

| Fonte | Ordem descrita |
|---|---|
| Tradição do *meetpoint faceting* (Long & Steele; GemologyOnline) | Mains do pavilhão primeiro, cortadas até um ponto central; facetas de cinta depois, vindo encontrá-las |
| The Gemology Project | Coroa: *break* 47° → *main* 42° → *star* 27° → mesa — **break antes da main** |
| Geosciences LibreTexts 17.2 | Pavilhão: facetas *break* primeiro, depois as mains |
| USFG, *Sequencing Facets* | Não arbitra: "the two most common starting places were either a culet point or a set of girdle points" |

Não é um caso de uma fonte estar errada. É uma escolha de projeto que depende de qual ponto de referência o design precisa fixar primeiro, e a fonte mais autorizada do domínio trata explicitamente as duas partidas como igualmente correntes.

**Desfecho: DECLARADO COMO CONTROVÉRSIA (LC-08).** A aula 03 passou a apresentar as duas sequências lado a lado e a declarar, em uma frase e sem arbitrar: "*Qual delas é a padrão é questão em aberto: fontes do mesmo nível descrevem as duas, e a escolha pertence ao design.*" A a04 foi alinhada ("qualquer que seja a partida escolhida pelo design"). É a única declaração LC-08 do módulo.

---

## Resíduo de refutação — a varredura pós-correção

O módulo 08 firmou a lição de que corrigir a tese de uma aula não basta: vocabulário, "Antes de começar", **títulos de seção**, exemplos e "Próxima aula" de outras aulas podem continuar ensinando a versão refutada. A varredura foi feita por regex sobre as seis aulas, procurando as formulações refutadas ("mais numerosas", "contorno geral", "reseta", "três colunas", "main antes", "desvio sistemático", "perde precisão", "precisa do 77", "mais citados", "maior cobertura").

**Um resíduo encontrado e corrigido:**

| Onde | Resíduo | Correção |
|---|---|---|
| a04, título de seção | `### Por que isso evita medir profundidade — e por que evita erro cumulativo` — o título **prometia** a tese que o corpo da seção, já corrigido pelo 🟠 5, passara a refutar | `### Por que isso evita medir profundidade — e o que faz com o erro acumulado` |

**Verificado e limpo:** o verbete "erro cumulativo" do vocabulário da a04 ("um pequeno desvio de corte que se soma ao longo de várias facetas sucessivas") é uma definição neutra e **fica correta** sob a nova tese — não foi tocado. Os blocos "Antes de começar" das aulas 04 e 05, os quatro blocos "Próxima aula" e o "O que não concluir" das seis aulas foram lidos e não repetiam nenhuma tese refutada, exceto o "Antes de começar" da a04 já corrigido pelo 🔴 4.

---

## Cortes de compensação (LC-02)

As correções acrescentaram texto e três aulas estouraram o teto de ~1.600 antes do ajuste (a01 chegou a 1618, a03 a 1789, a06 a 1628). O método é o dos módulos 04 a 08: **financiar o acréscimo com redundância da própria aula**, nunca comprimindo a correção.

| Aula | Cortes feitos |
|---|---|
| a01 | Reativação do módulo 03 encurtada; a frase "mais dentes não é mais preciso em ângulo" fundida com a anterior (já constava idêntica em "Erros comuns" e no Recap) |
| a03 | Analogia da planta da casa condensada; a frase "um talhe simples pode ter só duas ou três fileiras" removida (referia-se ao exemplo da a02, que o 🔴 3 substituiu); a repetição do cálculo 96 ÷ 8 = 12 removida do corpo (permanece no exemplo trabalhado); marcador "Ler a tabela sem checar o jogo de índice declarado" removido de "Erros comuns" (duplicata literal do 3º marcador da a02) |
| a06 | Explicação altura/base condensada; a ponte "guarde a distinção, porque a próxima seção depende dela" removida; exemplificação da conversão separada de coroa e pavilhão encurtada |

Nenhuma correção foi encurtada para caber. Todas as seis aulas terminaram sob o teto.

---

## Verificado e correto — as 21 alegações que passaram

As de maior risco, com o que foi conferido:

| claim_id | Aula | O que foi verificado |
|---|---|---|
| `TGR-FORMULA-DEF-001` | a06 | **A fórmula bate literalmente** com a da USFG: `angle xnew = tan⁻¹{tan(angle xoriginal) * [(tan(angle refnew) / tan(angle reforiginal)]}`. Autossuspeita do redator: infundada. |
| `TGR-EX-NUMERICO-001` | a06 | **Recalculado de forma independente.** tan(39°)=0,8098; tan(42°)=0,9004; razão 1,1119; tan(42,3°)=0,9099; arctan(1,0118)=**45,3348°**. Coincide com o publicado pela USFG (45,3348402…), assim como 43,9°→46,9371° e 68°→70,0307°. Autossuspeita do redator: infundada. |
| `IDX-REGRA-DIVISOR-001` | a01 | A regra "simetria M-fold exige que M divida N" está correta e a derivação da aula é válida. Confirmada pela IFA ("the symmetry of a design depends on which numbers divide evenly into the available number of teeth"). |
| `IDX-DIVISOR-TAB-001` (tabela) | a01 | **Os cinco conjuntos de divisores estão aritmeticamente corretos**, conferidos por cálculo. Só o escopo e a atribuição falharam (🟠 8). Autossuspeita do redator sobre os números: infundada. |
| `TGR-LIMITE-EXTREMOS-001` | a06 | Confirmado literalmente: "original facet angles specified at 0° or 90° (tables and girdles) remain at 0° or 90° and do not need to be converted". |
| `TGR-TAN-NAOLIN-001` | a06 | A não linearidade da tangente e sua consequência estão certas, e a fonte a declara. |
| `PTO-DEF-TECNICA-001` | a04 | Quase literal ao uso corrente: "with meetpoint designs, **you aren't cutting to a particular depth, you're cutting to hit the meetpoint**". |
| `PTO-FRASE-PONTO-001` | a04 | Confirmada literalmente na USFG: "**three facets make a point and two facets make a line**". |
| `PTO-PARTIDA-REQ-001` | a04 | Confirmada: "meetpoint designs require that they must have a **starting point which is accurate** and from which all of the other facets can be derived". |
| `DGN-SINT-GIRO-001` | a05 | O cheater como ajuste fino de índice confere com o dicionário da USFG ("a bearing angle adjustment which allows 'indexing' between teeth") e com The Gemology Project ("an index micro-adjuster called a cheater"). A distinção fração-de-dente × dente-inteiro é sólida. |
| `DGN-SINT-ALTURA-001` | a05 | Confere: "the mast height controls how much to cut off"; e o módulo 03 a05 já registrava a altura como responsável por faceta curta ou longa. |
| `IDX-DUPLO-SENT-001` | a01 | A separação entre índice de refração e *index gear* está certa e é tratada com rigor exemplar — o modelo que faltou ao verbete de *undercut* da a05. |
| `IDX-NAO-ANGULO-001` | a01 | Confere com o módulo 03 a05 e com a definição de *index gear* da USFG. |
| `DIA-VISTA-TOPO-001` | a03 | A vista de topo como portadora da simetria e a exigência de divisibilidade conferem. |
| `DIA-EX-INTERCALADO-001` | a03 | Índices intercalados como padrão de main/break confere; e o par 42°/46° do exemplo é geometricamente coerente (a break, mais íngreme, encosta na cinta). |
| `PTO-LIMITE-GARANTIA-001` | a04 | Correto e importante: o meetpoint garante consistência interna, não a correção da especificação. |
| `COO-ANGULO-DEF-001` | a02 | Confere com o dicionário da USFG: "used alone, 'angle' refers to the angle which a facet makes with the **Girdle Plane**". |
| `DGN-ARVORE-BASE-001` | a05 | A pergunta de partida (plano radial × posição na volta) é herdada do módulo 03 a05, já auditado, e permanece válida — só o ramo do "Sintoma 3" precisou de conserto. |

**Quatro tocadas por propagação, sem mudança de conteúdo:** `COO-ALTURA-DEF-001` (a02, alinhada ao 🔴 3), `DIA-TRES-PECAS-001` (a03, ao 🟠 6), `PTO-SEQ-DEPENDE-001` (a04, ao 🔴 4), `DGN-TABELA-RESUMO-001` (a05, ao 🔴 2).

---

## Propagação

**Material derivado:** o módulo **não tem questionário nem baralho de flashcards** — o questionário só entra depois da revisão didática, pelo pipeline dos módulos 06+, e os flashcards seguem dispensados desde 2026-09-04. **Nenhum material derivado foi contaminado**, que é exatamente o que o gate existe para garantir.

**Arquivos alterados:** as seis aulas. Nada mais foi tocado.

### Pendências de propagação para o orquestrador

Três itens que esta auditoria **deliberadamente não tocou**, por estarem fora do seu escopo:

1. **`course-state.yaml`** — os seis `palavras_corpo` e os seis `content_hash` do módulo 09 estão desatualizados; e o bloco `audit` do módulo precisa passar de `{status: pending}` para aprovado, com as contagens deste relatório e `open_findings` vazio.
2. **Hub `09-geometria-e-diagramas-modulo.md`** — a linha 24 descreve o diagrama de lapidação como "especificação de talhe (**índice, ângulo, altura**)". É a formulação que o 🟠 6 corrigiu na a02. Ajuste de uma linha.
3. **Módulo 08 (fechado) — nomenclatura do GemCad.** A alegação `RAY-MODEL-MEDE-001`, na aula 06 do módulo 08, e a resposta (a) da questão correspondente no questionário do módulo 08 descrevem o GemCad como especificando "ângulo, índice e **altura** de cada faceta". É a mesma imprecisão do 🟠 6, com **severidade 🟠 e raio pequeno**: "altura" é uma glosa aceitável em linguagem comum, e o módulo 09 agora carrega a versão precisa. **Não foi corrigido** para não reabrir um módulo aprovado à revelia do orquestrador — mas fica registrado como candidato à próxima auditoria `cross-course`.

---

## Recomendação para o módulo 10

**Verificar a atribuição de fonte antes de verificar o conteúdo.** Cinco dos treze achados deste módulo — e dois dos quatro 🔴 — não são erros de fato, são erros de **procedência**: a afirmação foi para o texto acompanhada do nome de uma fonte real e apropriada que, aberta, dizia outra coisa ou não dizia nada. É o terceiro módulo consecutivo com essa assinatura (`TAB-ALVO-FAIXA-001` e `RAY-FONTE-USFG-001` no 08). Nos casos mais graves — o 🔴 1 e o 🔴 4 — a fonte não era omissa: era **contrária**, e o texto a citou como se a confirmasse.

A verificação barata que teria pego quatro dos cinco: para cada linha de "Fontes consultadas" que carrega uma citação entre aspas ou uma alegação específica, **abrir a URL e localizar a frase**. O módulo 10 (famílias de talhe) trabalhará com linhagem histórica do brilhante redondo, com Tolkowsky e com o duplo sentido de "talhe misto" — território onde a atribuição errada é ainda mais fácil de cometer e mais difícil de detectar depois.

---

*Auditoria conduzida em `audit-and-fix`, profundidade `full`, sobre as seis aulas em conjunto. Toda verificação feita por busca na web em 2026-09-06; nenhuma alegação foi avaliada de memória. Manifesto estruturado em `09-geometria-e-diagramas-auditoria.json`.*
