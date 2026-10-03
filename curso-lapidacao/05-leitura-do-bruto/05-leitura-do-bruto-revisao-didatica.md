# Revisão didática: Módulo 05 — Leitura e orientação do bruto

**Revisado em:** 2026-09-03 · **Modo:** `review-and-fix`
**Material:** as 6 aulas do módulo 05, em conjunto · contrato `ensino-medio-com-gemologia-v1`
**Rodou depois de:** `05-leitura-do-bruto-auditoria.md` (2026-09-03) — auditoria fechada, `open_findings` vazio
**Veredito:** ✅ **Bem ensinado com ressalvas** — o único achado bloqueante foi resolvido; nada encaminhado ao orquestrador.

> [!note] Sobre este arquivo
> Os módulos 01–04 **não** têm arquivo de revisão didática: o registro deles vive só no bloco `didactic_review` do `course-state.yaml`. Este módulo é o primeiro a ganhar um relatório em disco, a pedido do orquestrador. O bloco do estado foi preenchido no mesmo formato dos módulos anteriores, então nada se perdeu para quem lê só o `course-state.yaml`.

## Resumo

🔴 **1** bloqueia · 🟠 **2** prejudicam · 🟡 **4** atrito · 🔵 **2** sugestões

Todos os 🔴, 🟠 e 🟡 foram corrigidos. As duas 🔵 foram avaliadas e **não** aplicadas, com justificativa.

**Carga por aula** (conceitos novos independentes · exemplos · duração declarada):

| Aula | Conceitos novos | Exemplos | Duração | Carga |
|---|---|---|---|---|
| a01 | 3 (janela · imersão · iluminação) | 1 trabalhado, 4 passos | ~25 min | adequada |
| a02 | 3 (inclusão · fratura · clivagem) | 1 trabalhado, 4 recortes | ~25 min | adequada |
| a03 | 2 (orientação × caminho da luz · talhe × mistura) + 4 padrões | 1 trabalhado | ~25 min | adequada |
| a04 | 3 (pleocroísmo · eixo óptico · tilt de compromisso) | 1 trabalhado, 5 passos | ~28 min | **no limite** |
| a05 | 3 (rendimento · fórmula de estimativa · beleza × peso) | 1 trabalhado, 3 opções | ~27 min | adequada |
| a06 | 2 (janelamento · extinção) + 5 causas | 2 trabalhados | ~28 min | **no limite** |

Nenhuma aula precisa ser dividida. As duas "no limite" (a04 e a06) sustentam a carga porque em ambas os conceitos novos são **contrastivos** — pleocroísmo contra zonação, janela contra extinção —, e contraste reduz carga em vez de somá-la. Nenhuma aula foi encaminhada ao `gerador-de-curso-modular` para divisão.

**Progressão do módulo:** limpa. A cadeia a01 (ver) → a02/a03/a04 (traduzir em restrição) → a05 (precificar) → a06 (prever o defeito) é estritamente crescente, cada aula declara o que a anterior entregou, e nenhuma usa um resultado de aula posterior. Os quatro "Não é preciso saber…" de cada abertura fecham a fronteira corretamente. **Nenhum salto de pré-requisito.**

---

## Achados

### 🔴 1. `raio ordinário` e `raio extraordinário` sustentam a aula inteira e nunca foram definidos

**Tipo:** termo central usado antes de definido (LC-01)
**Onde:** a04 · "Dicroísmo, tricroísmo e o eixo óptico"; "O eixo óptico é central"; "Exemplo trabalhado", passo 1; "Erros comuns", bullet 3; "Recap relâmpago"
**Problema:** os dois termos aparecem seis vezes, e a decisão central da aula — orientar a mesa perpendicular ao eixo óptico *porque* ali só se vê a cor ordinária — é inteiramente construída sobre eles. Na primeira ocorrência vêm entre aspas de citação ("a cor do 'raio ordinário' e a do 'raio extraordinário'"), o que **sinaliza** que são termos técnicos e ao mesmo tempo **deixa de explicá-los**. A tabela de vocabulário tinha nove entradas e nenhuma era essa; o bloco "Antes de começar" cita do curso de Gemologia "pleocroísmo, eixo óptico e birrefringência", que não cobrem os dois raios. Resultado: quem chega ao passo 1 do exemplo trabalhado — "vê-se um azul-violeta puro e saturado — o raio ordinário" — não tem como saber o que acabou de ler, e é exatamente aí que o exemplo vira mecânico em vez de compreendido.
**Correção aplicada:** entrada nova na tabela de vocabulário (que passou a ter dez, o teto de LC-03): "as duas 'metades' em que um cristal anisotrópico separa a luz que o atravessa, cada uma vibrando num plano e cada uma com a sua cor. Termos do curso de Gemologia, usados aqui para nomear qual cor se vê por qual direção." A glosa é a descrição gemológica corrente e está alinhada a `PLE-CLASSE-NUM-001`, já auditada — nenhum fato novo foi introduzido.
**Escopo:** correção local · **custo de LC-02: zero** (a tabela de vocabulário fica fora da régua de `palavras_corpo`).

### 🟠 2. A analogia do celofane ensina mistura subtrativa, que é o oposto do pleocroísmo

**Tipo:** analogia que ensina modelo mental errado
**Onde:** a04 · "A folha de celofane que muda de cor" (abertura da aula)
**Problema:** *encaminhado pela auditoria* (item 1 de `handed_to_didactic_review`). "Olhe através de duas folhas de celofane sobrepostas, uma azul e uma amarela: verde" descreve **dois filtros empilhados somando absorção** — um fenômeno de camadas. O pleocroísmo é absorção dependente da **direção de vibração** num material **único e homogêneo**: não há nada empilhado, e a própria aula insiste nisso três linhas adiante ("a mesma pedra, o mesmo pedaço, sem nenhuma zona"). Analogia é memorável por construção, então o modelo errado gruda: o aluno que a carregar vai prever que girar a pedra **mistura** as cores progressivamente, quando o comportamento é o inverso — cada direção entrega **uma** cor, e é a mistura que aparece só nas direções intermediárias. É também o modelo que atrapalha a a03, onde mistura óptica de fato existe e tem outra causa. LC-04 exige analogia antes do termo, não uma analogia que precise ser desfeita depois.
**Correção aplicada:** a analogia foi **mantida** — ela entrega bem a intuição de partida ("a luz pode sair de uma cor diferente da que entrou") e substituí-la exigiria fabricar conteúdo factual que não passou pelo auditor. O que faltava era a **marca de quebra**, e ela foi acrescentada logo depois do exemplo da iolita: "**E é aqui que a analogia quebra:** no cristal não há duas folhas empilhadas somando cor. Há **uma** só, e o que muda a cor é a direção do olhar."
**Escopo:** correção local · custo de 24 palavras, financiado por corte de redundância no "Recap relâmpago" da mesma aula (ver "Custo em palavras").

### 🟠 3. A síntese final da a06 perdeu o mapeamento dado → defeito

**Tipo:** recap/síntese que não sintetiza — regressão introduzida pela própria auditoria
**Onde:** a06 · "Prever, não remediar"
**Problema:** a auditoria de 2026-09-03 comprimiu esta seção para financiar as correções de `EXT-CONSERTO-CAUSA-001` e `EXT-CINCO-CAUSAS-001`, e cortou os parênteses que ligavam cada dado do bruto ao defeito que ele prevê. O que sobrou — "profundidade disponível × índice, índice do material, saturação vista na imersão, estilo e contorno pretendidos" — é uma lista de **entradas sem saídas**. Só que a função desta seção é justamente ser a tabela de conversão da aula: depois de cinco causas apresentadas uma a uma, é aqui que o leitor monta o procedimento de previsão. Sem as setas, a seção deixa de ensinar e vira um índice. O julgamento da auditoria (de que o Recap repetia o mapeamento) estava certo quanto à duplicação e errado quanto a qual dos dois deveria sobreviver: o corpo é onde se aprende, o recap é onde se consolida.
**Correção aplicada:** as setas foram restauradas no corpo — "cada dado aponta um defeito: profundidade disponível × índice → janela ou extinção de proporção; índice do material → teto de brilho baixo; saturação vista na imersão → extinção química; estilo e contorno pretendidos → extinção de talhe e de contorno" — e o bullet 5 do "Recap relâmpago" foi enxugado para a forma destilada que cabe a um recap: "cada dado da leitura aponta um defeito — profundidade × índice, índice, saturação, estilo, contorno". A duplicação desaparece nos dois sentidos.
**Escopo:** correção local · saldo praticamente neutro em palavras.

### 🟡 4. Dois termos de fora usados na a01 sem constar da abertura

**Tipo:** LC-01 / LC-03 — pré-requisito não declarado
**Onde:** a01 · "A janela de inspeção" (`pré-polimento`); "O que a leitura decide", item 1 (`birrefringente`)
**Problema:** **(a)** "levada a um pré-polimento rápido" é a primeira aparição do termo no módulo; ele vem do módulo 02 e não estava nem no vocabulário nem em "Antes de começar". É agravante que a definição da janela **depende** dele: sem saber o que o pré-polimento faz, não se entende por que uma face desbastada passa a deixar ver o interior. **(b)** "em pedra colorida e birrefringente" usa uma propriedade do curso de Gemologia que a linha de pré-requisitos da a01 não lista — ela cita índice de refração, ângulo crítico, reflexão interna total e pleocroísmo, e para. A a04 lista birrefringência corretamente; a a01, que a usa antes, não.
**Correção aplicada:** dois acréscimos ao bloco "Antes de começar": birrefringência entrou na linha do curso de Gemologia com uma glosa de meia linha ("a propriedade de um cristal desdobrar a luz que o atravessa"), e um bullet novo remete ao módulo 02 explicando o pré-polimento como o lixamento fino que antecede o polimento e já deixa a superfície transparente o bastante para se enxergar através dela — que é exatamente o que a janela precisa.
**Escopo:** correção local · **custo de LC-02: zero** ("Antes de começar" fica fora da régua).

### 🟡 5. Um termo do vocabulário da a02 nunca aparece no corpo, e outro é definido por um termo não ensinado

**Tipo:** vocabulário órfão + definição que usa termo não definido
**Onde:** a02 · tabela de vocabulário (`subsuperficial`, `partição`) e "Fraturas — a inclusão que pode crescer"
**Problema:** **(a)** `subsuperficial` está declarado no vocabulário e **não ocorre uma única vez** no corpo. O conceito está lá — "fratura interna rasa — dentro do alcance do acabamento" — mas com outras palavras, então o leitor decora um termo que a aula não usa e não reconhece o termo quando o encontrar depois (ele volta no módulo 02 e no 14). Vocabulário órfão é o sintoma clássico de uma tabela escrita antes do corpo. **(b)** `partição` é definida como "ligada a geminação ou tensão" — e `geminação` é um termo de cristalografia que este curso declara **fora de escopo** e não ensina em lugar nenhum. Definir um termo do vocabulário por outro termo desconhecido é definição circular na prática.
**Correção aplicada:** **(a)** o termo declarado passou a ser **usado**, em vez de removido do vocabulário: "**Fratura interna rasa**, **subsuperficial** — dentro do alcance do acabamento". Custo de duas palavras, e a aula ganha a ancoragem que faltava. **(b)** glosa mínima acrescentada na própria célula da tabela: "**geminação** — dois cristais do mesmo mineral crescidos colados, em orientações espelhadas". Nenhum fato novo: é a definição corrente, e a aula continua sem ensinar cristalografia.
**Escopo:** correção local · custo de duas palavras na régua.

### 🟡 6. Vocabulário órfão na a03, enquanto o termo que a auditoria instalou ficou sem entrada

**Tipo:** vocabulário órfão + termo novo sem definição na tabela
**Onde:** a03 · tabela de vocabulário
**Problema:** dois defeitos que se cancelam. `contraste de cor` ("quanto uma zona se destaca da vizinha aos olhos") está no vocabulário e **não aparece no corpo** — mesmo padrão da a02. Ao mesmo tempo, a correção 🔴 1 da auditoria instalou no corpo o par **faixa deitada × faixa de pé**, que passou a carregar a distinção mais importante da aula (é ela que decide se a cor sai uniforme ou dividida) e aparece agora em quatro lugares — corpo, exemplo trabalhado, "Erros comuns" e "Recap relâmpago" — glosada só na primeira ocorrência, no meio de um parágrafo denso. A tabela já tinha dez entradas, o teto de LC-03, então acrescentar sem trocar quebraria o contrato.
**Correção aplicada:** troca de uma pela outra. `contraste de cor` saiu; entrou "**faixa deitada** × **faixa de pé** — uma faixa de cor está *deitada* quando o plano dela é paralelo ao da mesa e ao da cinta, e *de pé* quando é perpendicular a eles, atravessando a pedra de lado a lado. É a distinção que decide se a cor sai uniforme ou dividida." A tabela continua com dez entradas e passa a definir o que a aula de fato usa.
**Escopo:** correção local · **custo de LC-02: zero**.

### 🟡 7. `preformado` e `cintilação` usados na a05 sem apoio

**Tipo:** LC-01 / LC-03 — termo técnico usado antes de definido
**Onde:** a05 · "Quanto se perde, tipicamente" e "Recap relâmpago" (`quase preformado`); "A escolha que sempre aparece" (`cintilação pobre`)
**Problema:** **(a)** "um bruto já quase preformado" entrou no texto pela correção 🟠 6 da auditoria e trouxe consigo um termo do módulo 03, aula 03, que a a05 não declarava. É o mesmo defeito que a revisão didática do módulo 04 pegou na aula 03 daquele módulo, e a definição correta de preforma — contorno **e** volume, não só contorno — foi ela própria produto de uma correção de auditoria (`PRE-FORMA-DEF-001`), o que torna a remissão ainda mais necessária. **(b)** "paga em óptica: janelamento, extinção, brilho apagado, **cintilação pobre**" usa um termo que só será ensinado no módulo 08 e que a a06 — a aula que a frase remete — não cobre. É a única palavra da lista que o leitor não pode desempacotar.
**Correção aplicada:** **(a)** bullet novo em "Antes de começar" com wikilink para a aula certa do módulo 03 e a glosa alinhada ao texto já auditado, mais a explicação do que "quase preformado" significa num bruto natural. **(b)** `cintilação pobre` foi **removida** da enumeração, que ficou "**janelamento**, **extinção** e brilho apagado (aula 06)" — os três termos que a a06 de fato ensina. A promessa da frase e o conteúdo da aula seguinte passam a coincidir.
**Escopo:** correção local · o item (a) tem custo zero na régua; o (b) economiza duas palavras.

---

## Sugestões avaliadas e não aplicadas

### 🔵 8. A a05 usa dois exemplos numéricos diferentes para a mesma ideia, a vinte linhas de distância

**Onde:** a05 · "A escolha que sempre aparece" (mini-exemplo inline: "opção A: ~1,1 ct, ângulos corretos, sem janela; opção B: ~1,5 ct, pavilhão 3° raso, janela pequena no centro") contra o "Exemplo trabalhado" logo abaixo, que usa a turmalina com 2,3 / 4,2 / 5,5 ct.
**Avaliação:** há um custo real — o leitor encontra dois pares de números para a mesma decisão e pode tentar reconciliá-los. Mas o mini-exemplo é um **molde de formulação**, não um caso: ele mostra o *formato* em que o compromisso deve ser escrito, e é justamente por ser genérico que funciona como molde. Amarrá-lo à turmalina o transformaria numa antecipação do exemplo trabalhado e roubaria o efeito de "agora faça isso com o seu bruto". **Não alterado.**

### 🔵 9. A seção "A regra que junta tudo" da a03 ficou mais enxuta que as demais

**Onde:** a03 · "A regra que junta tudo"
**Avaliação:** *encaminhado pela auditoria* (item 2 de `handed_to_didactic_review`). A correção 🔴 1 obrigou a reescrever o parágrafo de orientação e, para pagar as palavras dentro de LC-02, esta seção perdeu as enumerações concretas ("faixa, setor, núcleo, parti-color"; "brilhante se há zonação a esconder, degrau só com cor uniforme…"). Reli a versão atual: os **três passos** do procedimento continuam íntegros e na ordem certa, e cada uma das enumerações removidas sobrevive literalmente no "Recap relâmpago", duas telas abaixo. A seção cumpre a função de fecho; o que ela perdeu foi redundância, não conteúdo. Restaurar exigiria cortar em outro lugar da a03 sem ganho líquido. **Não alterado** — e o contraste com o achado 🟠 3 é deliberado: lá o corpo tinha perdido o **mecanismo**, aqui perdeu só os **exemplos** do mecanismo.

---

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo | Recap cobre |
|---|---|---|---|
| `lapidacao-m05-oa01` — descrever a leitura e listar as decisões que ela precede | a01 · "A janela", "A imersão", "A iluminação", "O que a leitura decide" | sim — água-marinha, 4 passos | sim, e as cinco decisões aparecem nomeadas |
| `lapidacao-m05-oa02` — prever como inclusão, fratura e clivagem restringem o talhe | a02 · as três seções homônimas + o callout achado × propriedade | sim — kunzita, pena + clivagem combinadas | sim |
| `lapidacao-m05-oa03` — explicar a zonação sob orientações e talhes | a03 · "Onde a cor mora", "A orientação da mesa…", "A família de talhe…" | sim — safira de Montana | sim |
| `lapidacao-m05-oa04` — determinar a orientação de um bruto pleocroico e justificar o custo | a04 · "Qual cor se quer…", "O custo em rendimento", "A decisão incommensurável" | sim — safira do Sri Lanka, 5 passos | sim |
| `lapidacao-m05-oa05` — estimar o rendimento e formular o compromisso beleza × peso | a05 · "Quanto se perde", "Estimar o peso antes de cortar", "A escolha que sempre aparece" | sim — turmalina, 3 opções comparadas | sim |
| `lapidacao-m05-oa06` — prever janelamento e extinção e distinguir as causas | a06 · "Janelamento — uma causa", "Extinção — cinco causas", quadro `[!note]` | sim — dois casos (turmalina, ametista) | sim |

**Nenhum objetivo não coberto. Nenhum conteúdo órfão** — toda seção substancial das seis aulas serve ao objetivo declarado da sua aula. Cada objetivo é coberto por conteúdo **e** por exemplo **e** por recap, que é o padrão que os módulos 03 e 04 estabeleceram.

**Verbos:** os seis são de conhecimento observável (descrever, prever, explicar, determinar, estimar, prever). Nenhum "entender", "conhecer" ou "saber". Nenhum verbo de execução.

**Alinhamento aula–avaliação:** **não verificável nesta etapa** — o questionário e o baralho do módulo 05 ainda não existem. Fica registrado para o `gerador-de-questionarios`: a matriz precisa cobrir os seis objetivos e, em particular, cobrar da a06 a **distinção** janela × extinção e a **atribuição de causa**, que são o par mais fácil de avaliar mal (uma questão que peça "a causa da extinção" no singular reintroduz exatamente o erro que a aula combate no bullet 2 de "Erros comuns").

---

## Custo em palavras

Nenhuma aula estourou o teto de ~1.600 de LC-02. As correções que acrescentavam texto foram financiadas dentro da própria aula:

- **a04** — o marcador de quebra da analogia (+24) foi pago pelo "Recap relâmpago", que a auditoria já apontara como o mais redundante dos seis do módulo: caíram "e esta aula não se aplica a eles" (repetido em "Erros comuns"), a segunda metade do bullet do eixo óptico (repetida no bullet do procedimento) e "muitos cristais uniaxiais crescem alongados no eixo óptico" (repetido no corpo duas seções antes). A aula saiu de 1600 — exatamente no teto, situação que a auditoria sinalizou como risco — para **1594**, com folga recuperada.
- **a06** — a restauração das setas (+20) foi paga pelo bullet 5 do Recap (−18) e por "A confusão entre as duas é" → "Confundi-las é" (−6).
- **a01, a03** — custo zero na régua: as três correções caíram em "Antes de começar" e na tabela de vocabulário, ambas fora da contagem.
- **a02** — +2 palavras (o termo `subsuperficial` usado no corpo); a glosa de `geminação` caiu na tabela, fora da régua.
- **a05** — −2 palavras (`cintilação pobre` removida); o bullet de pré-requisito caiu fora da régua.

`palavras_corpo` pós-revisão: **a01 1591 · a02 1593 · a03 1592 · a04 1594 · a05 1596 · a06 1597**. Rodapés YAML das seis aulas ressincronizados; `content_hash` recalculado e gravado no `course-state.yaml`.

**Nenhum texto instalado pela auditoria de 2026-09-03 foi cortado.** As passagens de `ZON-FAIXA-MESA-001`, `ZON-ORIENT-PATH-001`, `PLE-REN-CUSTO-001`, `PLE-CRESC-EIXO-001`, `PLE-EXEM-SAFIRA-001`, `PLE-ORIENT-PROC-001`, `INC-CLIV-KUNZ-001`, `REN-FORMULA-PESO-001`, `REN-FAIXA-TIP-001`, `REN-RECUT-PERDA-001`, `REN-ESTIM-PROC-001`, `BRU-IMER-IDX-001`, `BRU-AQUA-ORIENT-001`, `EXT-CINCO-CAUSAS-001` e `EXT-CONSERTO-CAUSA-001` seguem íntegras — conferido uma a uma. A única alteração que tocou texto da auditoria foi o achado 🟠 3, que **restaurou** conteúdo que a compressão da auditoria havia removido, sem mexer no que ela instalou.

---

## O que está bem feito

Vale preservar nas próximas revisões:

- **O par contrastivo como motor de duas aulas.** A a04 abre distinguindo pleocroísmo de zonação e a a06 abre distinguindo janela de extinção. Nos dois casos a distinção vem **antes** do conteúdo, não depois, e nos dois casos ela é reforçada em "Erros comuns" com o erro específico de confundi-los. É a melhor decisão estrutural do módulo e é o que permite que as duas aulas mais carregadas caibam em 30 minutos.
- **A homonímia sinalizada.** "Janela de inspeção" (ferramenta, a01) e "janelamento" (defeito, a06) são a mesma palavra com sentidos opostos, e a a06 avisa disso no bloco "Antes de começar", antes de a colisão acontecer. Poucos materiais autodidatas fazem isso.
- **Os blocos "Não é preciso saber…".** As seis aberturas fecham explicitamente a fronteira do que ainda não foi ensinado. Num módulo em que as restrições se acumulam aula a aula sobre a mesma decisão (a orientação da mesa), esse fechamento é o que impede o leitor de achar que perdeu algo.
- **A restrição que se acumula sobre uma única escolha.** A a02 restringe a mesa pela clivagem, a a03 pela zonação, a a04 pelo pleocroísmo — e cada aula **declara** que está somando à anterior ("A cor entra como uma **segunda** restrição sobre a mesma escolha"). Isso é sequenciamento de currículo funcionando dentro de um módulo.
- **O exemplo trabalhado da a05 com três opções comparadas.** Comparar A, B e C com a mesma fórmula e o mesmo bruto ensina o método muito melhor que um único cálculo correto, e a decisão final justificada pelo destino da pedra fecha o objetivo sem virar opinião.
- **A a02.** É a aula mais bem construída do módulo: a analogia do marceneiro (nó/rachadura/veio) mapeia os três conceitos um a um, o callout "achado × propriedade" nomeia a discriminação que o leitor mais erra, e o exemplo da kunzita faz as duas restrições colidirem em vez de tratá-las em paralelo. Só precisou de duas correções, ambas de vocabulário.

## Não executado, por escopo

- **Questionário e flashcards** — não existem ainda; o gate da auditoria está liberado e eles são as etapas 3 e 4.
- **Módulo não marcado como concluído** — `modules[05].status` permanece `pending`, e só fecha depois dos flashcards.
- **`validador-estrutural-do-curso` não rodado.**
- **`_curso.md` não reconciliado** — etapa da `geo-operacional`.
- **Hub `05-leitura-do-bruto-modulo.md`** — a tabela "Estado do módulo" e o callout de auditoria pendente foram atualizados nesta etapa, porque passaram a afirmar algo falso ("a auditoria científica ainda não rodou"). As contagens de palavras por aula do hub também foram ressincronizadas. Nenhuma outra parte do hub foi tocada.
