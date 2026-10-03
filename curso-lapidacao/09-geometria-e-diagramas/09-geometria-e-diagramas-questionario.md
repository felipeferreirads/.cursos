# Questionário — Módulo 09: Geometria da máquina e leitura de diagramas de lapidação

**Módulo:** [[09-geometria-e-diagramas-modulo|Módulo 09]] — Geometria da máquina e leitura de diagramas de lapidação
**Cobre:** aulas 01–06 (módulo completo, 6 aulas) · **Total:** 18 questões
**Objetivo:** integrar a geometria da máquina e a leitura de diagramas — o que o número de dentes do índice determina (e não determina) na simetria possível de um talhe; as três coordenadas de uma faceta e o ajuste da máquina que fixa cada uma; a leitura das duas vistas e da tabela de um diagrama e a extração da sequência de corte; a lógica do meetpoint faceting e o que ela de fato faz com o erro que se acumula; o diagnóstico de qual das três coordenadas está fora quando um encontro não fecha; e a conversão de um design por tangent ratio, com os limites do método — cobrando princípio, geometria, causa-efeito e limite, nunca operação de bancada.

**Objetivos cobertos (IDs):** `lapidacao-m09-oa01`, `lapidacao-m09-oa02`, `lapidacao-m09-oa03`, `lapidacao-m09-oa04`, `lapidacao-m09-oa05`, `lapidacao-m09-oa06`.

> [!warning] Nível teórico
> Nenhuma questão deste questionário avalia competência de bancada ou destreza manual — não se pergunta "como trocar a roda de índice", "como ajustar o batente ou o cheater", "como cortar até o meetpoint" nem "o que você faria na facetadora". Todas avaliam princípio, geometria, causa-efeito, ordem de grandeza, escopo e limite, conforme a regra dura do curso (ver [[_contexto|_contexto.md]]). Pré-requisito externo, citado só por nome: módulo 01 do curso de Gemologia (índice de refração — grandeza óptica homônima da roda de índice, e que não deve ser confundida com ela).

> [!warning] Proibições herdadas da auditoria e da revisão didática do módulo
> As seis travas registradas no relatório da revisão didática valem para este questionário e nenhuma questão as viola:
> 1. `oa01` — toda questão de simetria 7-fold declara o escopo "entre os cinco jogos estudados"; fora deles, o 84 também carrega o fator 7 (e alcança 14-fold). A primazia do 96 é de **notação**, não de amplitude de cobertura (72 e 84 empatam, 120 supera).
> 2. `oa04` — nenhuma questão trata "o meetpoint elimina o erro cumulativo" como verdadeiro. O erro **se acumula**; a técnica dá visibilidade e controle sobre **onde** o acúmulo é absorvido (faceta ajustável, de ângulo mais raso, deixada por último).
> 3. `oa05` — nenhuma questão aceita "desvio de fileira inteira ⇒ ângulo". Ângulo **e** altura são ambos ajustes de fileira; o que os separa é a **inclinação** (certa → altura do mastro; errada → batente de ângulo), não a escala do desvio.
> 4. `oa03` — nenhuma questão cobra "main antes das auxiliares" como regra. O cobrável: a ordem de grande escala (pavilhão → cinta → coroa → mesa), o princípio dos **pontos** de referência a estabelecer, a leitura de índices intercalados como padrão main/break, e a controvérsia declarada (LC-08).
> 5. `oa06` — nenhuma questão trata o tangent ratio como um método que "se degrada com o grande espalhamento angular". Quem se degrada é o **atalho** de somar graus fixos; a razão de tangentes preserva a vista em planta por construção.
> 6. `oa02` — nenhuma questão diz "o diagrama tem três colunas" nem "duas facetas de mesmo ângulo e índice se distinguem pela altura". A tabela traz ângulo e índice; a profundidade vem do ponto de encontro. Ângulo e índice dão a **orientação** do plano; a altura, a **posição** dele.

## Matriz de avaliação

| Objetivo | Explicar/Reconhecer | Aplicar/Prever | Analisar/Distinguir |
|---|---|---|---|
| oa01 — o que o nº de dentes determina na simetria | Q01 | Q03 | Q02, Q03 |
| oa02 — as três coordenadas e o ajuste que fixa cada uma | Q04 | Q06 | Q05, Q06 |
| oa03 — ler as vistas e a tabela, extrair a sequência | Q07 | Q09 | Q08, Q09 |
| oa04 — a lógica do meetpoint e o erro acumulado | Q10 | Q12 | Q11, Q12 |
| oa05 — diagnosticar qual coordenada está fora | Q13 | Q15 | Q14, Q15 |
| oa06 — aplicar o tangent ratio e declarar os limites | Q16 | Q18 | Q17, Q18 |

## Questões

**1. (Múltipla escolha) — lapidacao-m09-q01.** Sobre o que o número de dentes de um jogo de índice determina, qual afirmação está correta? *(Objetivo: `lapidacao-m09-oa01`)*

- a) Um jogo com mais dentes corta ângulos mais precisos: um jogo de 96 permite um controle de inclinação mais fino que um de 32.
- b) Uma simetria N-fold só é alcançável se N for divisor do número de dentes, porque a roda só trava em posições de dente inteiro; e o número de dentes não toca no ângulo nem na altura da faceta, que vêm de outros ajustes.
- c) O jogo de 96 é adotado como padrão porque cobre mais simetrias do que qualquer outro jogo do catálogo corrente.
- d) Com o cheater, qualquer jogo alcança qualquer simetria, porque ele desloca a pedra por frações de dente e preenche as posições que faltam.

**2. (Verdadeiro ou falso — justifique) — lapidacao-m09-q02.** "Para quem já tem o jogo de 96, o jogo de 80 é dispensável: como o 96 é o mais versátil dos cinco jogos estudados, ele cobre todas as simetrias que o 80 cobre." *(Objetivo: `lapidacao-m09-oa01`)*

**3. (Aplicação / análise) — lapidacao-m09-q03.** Um projetista quer cortar um talhe de simetria 7-fold e tem à mão os cinco jogos estudados nesta aula: 32, 64, 77, 80 e 96 dentes. (a) Qual jogo serve, e por quê — cite o fator primo decisivo. (b) Um colega afirma: "então o jogo de 77 é a única roda no mundo capaz de simetria 7-fold". Explique por que essa afirmação extrapola o escopo da aula. (c) Por que nenhuma combinação de 32, 64, 80 ou 96 alcança 7-fold? *(Objetivo: `lapidacao-m09-oa01`)*

**4. (Múltipla escolha) — lapidacao-m09-q04.** Qual afirmação descreve corretamente as três coordenadas de uma faceta e o ajuste da máquina que fixa cada uma? *(Objetivo: `lapidacao-m09-oa02`)*

- a) Ângulo (batente de ângulo), índice (roda dentada) e altura (altura do mastro); ângulo e índice juntos dão a **orientação** do plano da faceta, e a altura dá a **posição** dele — a que distância do centro da pedra o plano passa.
- b) Ângulo (batente), índice (cheater) e altura (roda dentada) — as três famílias de ajuste, cada uma numa parte diferente da facetadora.
- c) As três coordenadas são lidas diretamente das três colunas centrais da tabela do diagrama, uma coluna por coordenada.
- d) Ângulo, índice e altura; duas facetas de mesmo ângulo e mesmo índice, cortadas a alturas diferentes, ficam empilhadas na pedra como duas facetas paralelas distintas.

**5. (Verdadeiro ou falso — justifique) — lapidacao-m09-q05.** "Como ângulo e índice já dizem qual faceta do desenho é aquela, a altura do mastro é uma coordenada redundante: um diagrama poderia especificar qualquer talhe completo usando só ângulo e índice." *(Objetivo: `lapidacao-m09-oa02`)*

**6. (Aplicação / distinção) — lapidacao-m09-q06.** Um diagrama de pavilhão, num jogo de 96 dentes, traz três facetas: **A** — ângulo 43°, índice 8; **B** — ângulo 43°, índice 32; **C** — ângulo 39°, índice 8. (a) Qual é a relação entre A e B, e o que muda entre elas? (b) Qual é a relação entre A e C, e que par de fileiras vizinhas essa relação ilustra? (c) Um estudante propõe que exista ainda uma faceta **D** — ângulo 43°, índice 8, cortada mais fundo que A — coexistindo com A na mesma pedra. O que há de errado nessa proposta? *(Objetivo: `lapidacao-m09-oa02`)*

**7. (Múltipla escolha) — lapidacao-m09-q07.** Sobre a leitura das partes de um diagrama de lapidação, qual afirmação está correta? *(Objetivo: `lapidacao-m09-oa03`)*

- a) A vista de topo carrega a simetria do talhe (o número de posições que ela desenha precisa ser divisor do número de dentes do jogo); a vista lateral mostra a inclinação das fileiras; a tabela dá o ângulo e os índices de cada fileira.
- b) "Main" é a fileira com mais facetas de uma seção — a mais numerosa —, e é por isso que ela é cortada primeiro.
- c) Dentro de uma seção, a sequência de corte é sempre a main, depois a break, depois a star, porque é a main que estabelece o contorno geral da pedra.
- d) A tabela traz uma coluna de profundidade (ou altura) para cada fileira, ao lado das colunas de ângulo e de índice.

**8. (Verdadeiro ou falso — justifique) — lapidacao-m09-q08.** "A ordem em que as fileiras de uma seção são cortadas é fixada pela regra do ofício de que a main vem antes das auxiliares, porque é a main que estabelece o contorno geral da pedra." *(Objetivo: `lapidacao-m09-oa03`)*

**9. (Aplicação / análise) — lapidacao-m09-q09.** Um diagrama simplificado de pavilhão, jogo de 96, traz duas linhas: **Linha 1** — ângulo 42°, índices 0/8/16/24/32/40/48/56/64/72/80/88, "main"; **Linha 2** — ângulo 46°, índices 4/12/20/28/36/44/52/60/68/76/84/92, "break". (a) Que simetria o talhe tem, e como a tabela mostra isso? (b) O que a relação entre os dois conjuntos de índices indica sobre as duas fileiras? (c) A main está listada primeiro — o que se **pode** e o que **não se pode** concluir sobre a ordem de corte a partir disso? (d) Por que a break aparece mais perto da cinta na vista lateral? *(Objetivo: `lapidacao-m09-oa03`)*

**10. (Múltipla escolha) — lapidacao-m09-q10.** Por que o meetpoint faceting obtém precisão sem medir a profundidade de cada corte? *(Objetivo: `lapidacao-m09-oa04`)*

- a) Porque o diagrama fornece a profundidade exata de cada faceta numa coluna da tabela, o que torna a medição na pedra desnecessária.
- b) Porque cada faceta é cortada até **encontrar** facetas vizinhas já cortadas, num ponto ou numa linha compartilhada — uma condição visível —, em vez de até uma profundidade medida; "duas facetas fazem uma linha, três facetas fazem um ponto".
- c) Porque cada encontro correto "reseta" a referência para o corte seguinte, de modo que o erro nunca se acumula ao longo da cadeia.
- d) Porque o cheater ajusta a profundidade do corte de forma contínua até o ponto de encontro fechar.

**11. (Verdadeiro ou falso — justifique) — lapidacao-m09-q11.** "A vantagem do meetpoint faceting é eliminar o erro cumulativo: como cada faceta nova é cortada contra a anterior, o pequeno desvio de cada corte é zerado no encontro seguinte e não se propaga pela pedra." *(Objetivo: `lapidacao-m09-oa04`)*

**12. (Aplicação / análise) — lapidacao-m09-q12.** Três facetas de pavilhão são planejadas para se encontrar num único vértice na culaça. Depois de cortadas, duas se tocam com perfeição e a terceira deixa uma linha fina entre ela e as outras. (a) Por que não é preciso instrumento nenhum para saber que houve erro? (b) O desvio se manifesta na terceira faceta — pode-se concluir que a causa está nela? Justifique. (c) Um outro talhe é entregue com **todos** os meetpoints fechados com perfeição, mas foi cortado com o ângulo de pavilhão 3° mais raso que o especificado no diagrama. Isso é possível? O que esse caso revela sobre o que a técnica garante e o que não garante? *(Objetivo: `lapidacao-m09-oa04`)*

**13. (Múltipla escolha) — lapidacao-m09-q13.** Uma faceta isolada chega à profundidade certa — aponta na direção do vértice esperado, sem sobrar nem faltar corte — mas está **girada** em relação às vizinhas, por um desvio menor que um dente. Qual coordenada está fora, e qual ajuste corresponde a ela? *(Objetivo: `lapidacao-m09-oa05`)*

- a) A altura do mastro — a faceta terminou antes ou depois do ponto planejado.
- b) O índice, no ajuste fino — o cheater, que desloca a pedra por uma fração de passo de dente; um desvio de um dente inteiro, esse sim, se corrige recolocando a pedra no dente certo, não no cheater.
- c) O batente de ângulo — a inclinação da faceta ficou diferente da planejada.
- d) Qualquer uma das três, de forma indistinguível sem medir a faceta com instrumento.

**14. (Verdadeiro ou falso — justifique) — lapidacao-m09-q14.** "Undercut e overcut são erros simétricos: um é a faceta que ficou curta, o outro a que ficou longa, e ambos se corrigem movendo a altura do mastro em direções opostas." *(Objetivo: `lapidacao-m09-oa05`)*

**15. (Aplicação / distinção) — lapidacao-m09-q15.** Duas pedras chegam com uma **fileira inteira** de pavilhão desviada. **Pedra X:** todas as facetas da fileira terminam curtas, na mesma medida, mas a inclinação parece a planejada e o brilho combina com o da fileira vizinha. **Pedra Y:** as facetas da fileira têm brilho e proporção visivelmente destoando da fileira vizinha, e subir ou descer o mastro não alinha os encontros. (a) Diagnostique cada pedra — qual coordenada está fora? (b) Um estudante conclui: "as duas são erro de ângulo, porque o índice não afeta uma fileira inteira do mesmo jeito". Onde ele acerta e onde erra? (c) Por que o índice, de fato, não explica um padrão de fileira inteira? *(Objetivo: `lapidacao-m09-oa05`)*

**16. (Múltipla escolha) — lapidacao-m09-q16.** Qual afirmação descreve corretamente o que o tangent ratio faz? *(Objetivo: `lapidacao-m09-oa06`)*

- a) Reescala o design mudando o índice e o contorno (a vista de topo) para que ele caiba nas proporções do novo material.
- b) Reescala os ângulos das facetas — e, por consequência, as alturas — pela razão entre a tangente do novo ângulo de uma faceta de referência e a tangente do ângulo antigo dela, preservando a vista de topo (contorno e simetria); pavilhão e coroa são normalmente convertidos em separado.
- c) Reescala o design com precisão exata só quando os ângulos estão próximos uns dos outros; quanto maior o espalhamento angular, mais o método se afasta de uma vista em planta preservada.
- d) Equivale a somar a cada ângulo do design a diferença, em graus, entre o novo ângulo-alvo e o antigo da faceta de referência.

**17. (Verdadeiro ou falso — justifique) — lapidacao-m09-q17.** "O tangent ratio perde precisão em designs de grande espalhamento angular: quanto maior a diferença entre o ângulo mais raso e o mais íngreme do design, mais a conversão se afasta de uma vista em planta preservada, com desvios visíveis no contorno e nos pontos de encontro." *(Objetivo: `lapidacao-m09-oa06`)*

**18. (Aplicação) — lapidacao-m09-q18.** Um design de pavilhão em quartzo tem a main de referência a 39°, a ser reescalada para o ângulo-alvo publicado de 42°. Dados: tan(39°) ≈ 0,8098; tan(42°) ≈ 0,9004; tan(42,3°) ≈ 0,9099; arctan(1,0118) ≈ 45,33°. (a) Calcule a tangent ratio. (b) Aplique-a a uma faceta auxiliar de 42,3° e dê o novo ângulo dela. (c) A referência subiu 3° (de 39° para 42°). De quanto subiu a auxiliar, e por que não é exatamente 3°? (d) A aula afirma que, no mesmo design, uma faceta a 68° convertida pela **mesma** razão se desloca só ~2,03°, não 3°. Explique por que o mesmo fator multiplicativo desloca menos graus num ângulo mais íngreme, e o que isso demonstra sobre a prática de somar graus fixos. *(Objetivo: `lapidacao-m09-oa06`)*

---

## Gabarito comentado

<details><summary>Ver respostas</summary>

**1. Resposta: b).** É a regra central da aula 01: simetria N-fold exige que N divida o número de dentes, porque a roda só trava em posições de dente inteiro — é aritmética, não convenção. E o número de dentes não determina ângulo nem altura, que vêm do batente e da altura do mastro (outra família de ajuste, separada no módulo 03). **a)** é o erro comum apontado na aula: mais dentes = mais posições rotacionais, não mais precisão de ângulo. **c)** é a formulação que a auditoria corrigiu: o 96 cobre 11 simetrias, mas o 72 e o 84 cobrem 11 também e o 120 cobre mais (14); a razão real da primazia do 96 é a **notação** — a grande maioria dos diagramas publicados é escrita em notação de 96. **d)** o cheater corrige uma fração de dente num diagnóstico de erro; ele não cria as posições de dente inteiro de que a simetria depende.

**2. Falso.** O jogo de 96 é 2⁵ × 3: ele não tem o fator 5. As simetrias 5-fold e 10-fold só são alcançáveis, **entre os cinco jogos estudados**, pelo jogo de 80 (2⁴ × 5). Na verdade o 96 deixa **dois** buracos entre os cinco: o fator 5 (preenchido pelo 80) e o fator 7 (preenchido pelo 77). "Mais versátil dos cinco" não é o mesmo que "cobre tudo que os outros cobrem".

**3.** Resposta esperada.
- **(a)** O jogo de **77** (= 7 × 11): é o único dos cinco que carrega o fator primo **7**, e simetria 7-fold exige que 7 divida o número de dentes.
- **(b)** A afirmação extrapola porque a aula recorta **cinco** jogos de um catálogo corrente de **oito** (32, 64, 72, 77, 80, 84, 96, 120). Fora dos cinco, o jogo de **84** (= 2² × 3 × 7) também carrega o fator 7 — e ainda alcança 14-fold, que o 77 não alcança. O correto é "o 77 é a única fonte de 7-fold **entre os cinco desta aula**".
- **(c)** Porque 7 é primo e não se compõe de 2, 3 ou 5: 32 e 64 são potências de 2 puras; 80 = 2⁴ × 5; 96 = 2⁵ × 3. Nenhum tem 7 entre seus divisores, então 96/7, 80/7, 64/7 e 32/7 não são inteiros e a roda não trava nas posições exigidas.
- **Pontuação:** completa nomeia o 77 e o fator 7, explica a extrapolação pelo par catálogo-de-oito / recorte-de-cinco e cita o 84 (com o detalhe do 14-fold), e justifica (c) pela primalidade do 7; parcial acerta o 77 mas trata "único no mundo" como correto, ou não identifica o 84 como a alternativa fora da lista.

**4. Resposta: a).** As três coordenadas e seus ajustes: ângulo ↔ batente de ângulo, índice ↔ roda dentada, altura ↔ altura do mastro. A formulação que a revisão didática fixou: ângulo e índice dão a **orientação** do plano (para onde ele aponta — e por isso bastam para dizer *qual* faceta do desenho é aquela), e a altura dá a **posição** do plano (a que distância do centro da pedra ele passa). **b)** erra os ajustes: o cheater é ajuste fino de índice, não a coordenada índice em si, e a altura não vem da roda dentada. **c)** é a proibição da trava 6: o diagrama impresso tabela normalmente **duas** coordenadas (ângulo e índice); a profundidade não é lida de uma coluna, é fixada na pedra pelo ponto de encontro. **d)** é o erro geométrico que a auditoria derrubou: mesmo ângulo e mesmo índice = mesma orientação = planos **paralelos**; num sólido convexo o corte mais fundo consome o mais raso, e sobra uma faceta só.

**5. Falso.** Ângulo e índice dão a **orientação** do plano — bastam para dizer *qual* faceta do desenho é aquela —, mas não a **posição** dele: sem a altura, o plano não tem a que distância do centro da pedra passar, e o corte não sabe até onde avançar. A altura **dimensiona** a faceta que o ângulo e o índice localizaram; não é redundante. O que é verdade — e não deve ser confundido com a afirmação — é que o diagrama **impresso** costuma tabelar só ângulo e índice: a terceira coordenada não é dispensada, é fixada na pedra pelo ponto de encontro (meetpoint faceting, aula 04).

**6.** Resposta esperada.
- **(a)** A e B têm o mesmo ângulo (43°) e índices diferentes (8 e 32): só o índice muda, então **B é uma cópia simétrica de A**, a mesma faceta repetida noutra posição da volta (deslocada 24 dentes num jogo de 96).
- **(b)** A e C têm o mesmo índice (8) e ângulos diferentes (43° e 39°): só o ângulo muda, então C tem **outra inclinação no mesmo ponto da volta** — A e C pertencem a fileiras diferentes empilhadas na mesma direção radial. É **assim, por ângulo**, que uma main e uma break vizinhas se distinguem — nunca por altura.
- **(c)** D teria o mesmo ângulo e o mesmo índice de A, logo a **mesma orientação** — os dois planos seriam **paralelos**. Num sólido convexo, cortar D mais fundo que A simplesmente **consome** A: sobra uma faceta só, a mais profunda. Não é possível ver duas facetas paralelas no mesmo índice; a altura dimensiona a faceta, não cria uma nova.
- **Pontuação:** completa classifica os três pares (cópia simétrica; fileiras vizinhas distintas por ângulo; planos paralelos que não coexistem) e nomeia a distinção main/break por ângulo; parcial acerta A–B e A–C mas aceita a faceta D, ou atribui a distinção de fileiras vizinhas à altura.

**7. Resposta: a).** As três peças e o que cada uma carrega: vista de topo → contorno e posição angular, onde a simetria aparece (o número de posições precisa ser divisor do número de dentes do jogo); vista lateral → a inclinação das fileiras; tabela → ângulo e índices de cada fileira. **b)** é o erro corrigido na auditoria: "main" diz **tamanho** (as facetas grandes que atravessam a seção, da cinta à culaça ou da cinta à mesa), não quantidade — num brilhante redondo há 8 mains de pavilhão contra 16 facetas de cinta. **c)** é a proibição da trava 4: não há regra fixa de main antes de auxiliares, e não é a main que estabelece o contorno (isso são as facetas de cinta/break). **d)** trava 6: a tabela não tem coluna de profundidade.

**8. Falso.** Dois erros. Primeiro: **não existe essa regra fixa**. A literatura enuncia um princípio sobre a ordem dos **pontos** que precisam ser estabelecidos — as duas partidas correntes são um ponto de culaça ou um conjunto de pontos de cinta —, e fontes de referência do mesmo nível descrevem as duas ordens (mains primeiro; ou facetas de cinta primeiro). É controvérsia declarada (LC-08): a escolha pertence ao design. Segundo: quem estabelece o **contorno** — a linha da cinta — são as facetas de cinta / break; as mains do pavilhão estabelecem o **ponto de culaça**. O que é estável e cobrável: a ordem de grande escala pavilhão → cinta → coroa → mesa, e o princípio de que cada fileira é cortada **contra** facetas que já existem.

**9.** Resposta esperada.
- **(a)** Simetria **12-fold**: cada linha tem 12 índices, espaçados de 8 em 8 dentes num jogo de 96 (96 ÷ 8 = 12); a vista de topo mostraria 12 raios iguais.
- **(b)** Os índices da Linha 2 (4, 12, 20…) caem exatamente **entre** os da Linha 1 (0, 8, 16…) — **intercalados**, não sobrepostos. É o padrão típico de uma fileira main e uma fileira break vizinhas: cada break preenche o intervalo angular entre duas mains consecutivas.
- **(c)** **Pode-se** concluir que a ordem das linhas costuma ser a sequência de corte proposta pelo autor, e que cada fileira é cortada contra a anterior (invertê-las tiraria de uma fileira a referência contra a qual ela fecha). **Não se pode** concluir que "main antes de break" seja regra do ofício: outro autor partiria dos pontos de cinta e inverteria as duas — qual é a padrão é questão em aberto.
- **(d)** A break está a 46°, mais **inclinada** (mais em pé) que a main a 42°; facetas de pavilhão mais inclinadas caem mais perto da cinta na vista lateral.
- **Pontuação:** completa deriva a simetria pelo cálculo, identifica os índices intercalados como padrão main/break, separa o que a ordem das linhas permite e não permite concluir (sem cair em "main antes de break"), e liga a posição da break ao seu ângulo maior; parcial acerta a simetria e o padrão intercalado mas afirma "main antes de break" como regra, ou erra a relação ângulo-posição na vista lateral.

**10. Resposta: b).** A lógica central da aula 04: em vez de "até que profundidade cortar", a pergunta é "até que ponto de encontro cortar" — a faceta é levada a encontrar vizinhas já cortadas num ponto ou numa linha compartilhada, e o encontro (ou a linha fina que sobra, ou a faceta que passou) é uma condição **visível**, que dispensa instrumento. "Duas facetas fazem uma linha, três facetas fazem um ponto." **a)** trava 6: o diagrama não tabela profundidade. **c)** é a proibição da trava 2: o erro **não** é zerado a cada encontro — ele se acumula; essa era, inclusive, a versão que a auditoria encontrou marcada erradamente como "erro comum" na aula. **d)** o cheater é ajuste fino de índice, não de profundidade.

**11. Falso.** Nenhuma máquina é perfeitamente repetível, e a literatura do ofício descreve o contrário: ao encadear facetas ao redor da pedra, os pequenos erros **se somam** num ponto e se cancelam noutro. O meetpoint **não** elimina o acúmulo. O que a técnica dá é (a) **visibilidade** — o desvio aparece no encontro em que se manifesta, e não diluído pela pedra inteira — e (b) **controle sobre onde o acúmulo vai parar**: a cadeia é planejada para terminar numa faceta ajustável, de ângulo mais raso, deixada por último justamente para absorver o erro. Um encontro que falha diz **onde olhar**, não necessariamente onde a causa nasceu.

**12.** Resposta esperada.
- **(a)** O ponto de encontro é uma condição visível: ou as facetas se tocam exatamente, ou sobra uma linha fina, ou uma passa da outra. A linha fina **é** o indicador de que o meetpoint não fechou — nenhum instrumento é necessário.
- **(b)** Não necessariamente. Como duas das três facetas se encontram bem, o desvio se manifesta na terceira — mas o erro pode ter vindo se somando pela cadeia e só ter estourado neste encontro. O meetpoint aponta **onde olhar**, não onde a causa nasceu.
- **(c)** Sim, é possível. O meetpoint faceting garante **consistência geométrica interna** — que facetas planejadas para se encontrar de fato se encontrem —, mas **não** garante que o ângulo ou a proporção estejam corretos: essas grandezas vêm das coordenadas do diagrama (ângulo, índice, altura), lidas e aplicadas corretamente, independentemente de os encontros fecharem. Um talhe pode ter todos os pontos fechados e ainda ter sido cortado com o ângulo errado.
- **Pontuação:** completa explica o encontro como condição visível, nega que o local do sintoma prove o local da causa, e distingue consistência interna (garantida) de correção da especificação (não garantida); parcial acerta (a) e (b) mas conclui que meetpoints fechados garantem o ângulo certo.

**13. Resposta: b).** Faceta na profundidade certa mas **girada** → o desvio é de **posição na volta**, não do plano radial. Desvio menor que um dente → ajuste fino de índice, que é o **cheater** (desloca a pedra por uma fração de passo de dente). Um desvio de um dente inteiro ou mais seria erro de **índice** propriamente, corrigido recolocando a pedra no dente certo — o cheater corrige frações, não dentes completos. **a)** altura produz faceta curta ou longa na direção certa, não girada. **c)** o batente de ângulo muda a inclinação, não a posição na volta. **d)** o próprio padrão do desvio (girado, na profundidade certa, menos de um dente) já identifica a coordenada — não é preciso medir.

**14. Falso.** Undercut e overcut **não** são simétricos. Um **undercut** (faceta curta, parou antes do encontro) é recuperável: falta corte, e o corte que falta ainda pode ser feito. Um **overcut** (faceta longa, passou do ponto) **não tem volta** — material removido não retorna, e recuperar o encontro obriga a refazer as facetas vizinhas numa profundidade nova. É essa assimetria — o overcut é irreversível — que o torna o erro caro. (Observação de vocabulário: "undercut" aparece neste curso em outros dois sentidos — o sub-corte da serra fina, módulo 03 aula 01, e a depressão por resistência diferencial à abrasão, módulo 07 aula 03 —; aqui vale só o de profundidade de faceta.)

**15.** Resposta esperada.
- **(a)** **Pedra X** → **altura do mastro** daquela fileira: a altura é fixada uma vez por fileira e mantida enquanto todas as facetas dela são cortadas ao redor da pedra, então um erro de altura sai **uniforme na fileira inteira** — é o sintoma de faceta curta promovido de uma faceta para a fileira, com a inclinação preservada. **Pedra Y** → **batente de ângulo**: a fileira foi cortada com a inclinação errada (brilho e proporção destoando), e isso não se conserta subindo ou descendo o mastro.
- **(b)** Ele **acerta** que o índice não explica um padrão de fileira inteira. **Erra** ao concluir "ângulo" para as duas: ângulo **e** altura são **ambos** ajustes de fileira. O que separa os dois casos é a **inclinação** — certa → altura; errada → ângulo —, não a escala do desvio.
- **(c)** O índice é escolhido **faceta a faceta**; um erro de índice desloca uma faceta, não todas do mesmo jeito.
- **Pontuação:** completa diagnostica X como altura e Y como ângulo, corrige o estudante pela distinção inclinação-certa / inclinação-errada (não pela escala), e explica por que o índice não gera padrão de fileira; parcial diagnostica as duas como ângulo, ou acerta o diagnóstico mas justifica pelo tamanho do desvio em vez da inclinação.

**16. Resposta: b).** O tangent ratio reescala os ângulos (e, por consequência, as alturas) pela razão entre a tangente do novo ângulo de uma faceta de referência e a tangente do ângulo antigo dela — uma constante para a conversão inteira —, mantendo a vista de topo (contorno e simetria) intacta; o índice não muda. Pavilhão e coroa são normalmente convertidos **em separado**, cada seção com sua referência e sua razão. **a)** o método não toca no índice nem no contorno. **c)** é a proibição da trava 5 — inversão: quem se degrada com o espalhamento angular é o **atalho** de somar graus fixos, não o método. **d)** essa é exatamente a descrição do atalho não linear, que **não** é o tangent ratio.

**17. Falso.** É a inversão que a auditoria corrigiu. A conversão pela razão de tangentes preserva a vista em planta **por construção** — o dicionário do ofício define o tangent ratio como o que traduz um conjunto de ângulos noutro "mantendo a vista em planta constante" —, qualquer que seja o espalhamento angular. Quem se degrada com o espalhamento é o **atalho** de somar um número fixo de graus a todos os ângulos: quanto maior a diferença entre o ângulo mais raso e o mais íngreme do design (típico dos designs complexos), mais esse atalho diverge da conversão correta, e é ele que produz desvios visíveis na vista em planta e problemas nos pontos de encontro. (Facetas a 0° e a 90° não mudam pelo método — tangentes zero e indefinida.)

**18.** Resposta esperada.
- **(a)** Tangent ratio = tan(42°) ÷ tan(39°) = 0,9004 ÷ 0,8098 ≈ **1,1119**.
- **(b)** tan(42,3°) × 1,1119 = 0,9099 × 1,1119 ≈ 1,0118; o novo ângulo é arctan(1,0118) ≈ **45,33°**.
- **(c)** A auxiliar subiu ~**3,03°** (de 42,3° para 45,33°). Não é exatamente 3° porque a conversão é regida pela **razão das tangentes**, não por uma soma fixa de graus, e a tangente não é uma função linear do ângulo.
- **(d)** Perto de 90° a tangente cresce muito depressa; assim, multiplicar a tangente por 1,1119 corresponde a um acréscimo **menor em graus** num ângulo íngreme do que o mesmo fator produziria perto de 40°. Por isso a mesma razão leva 68° a apenas ~70,03° (deslocamento de ~2,03°, não 3°). Isso demonstra que **somar um número fixo de graus a todos os ângulos** (o atalho) diverge da conversão correta — tanto mais quanto maior o espalhamento angular do design.
- **Pontuação:** completa calcula a razão (1,1119), aplica corretamente à auxiliar (45,33°), quantifica o deslocamento (~3,03°) e o atribui à não linearidade da tangente, e explica (d) pela curvatura da tangente perto de 90° com a conclusão sobre o atalho; parcial acerta os cálculos mas atribui a diferença a "erro de arredondamento", ou não conecta (d) à falha de somar graus fixos.

</details>

## Cobertura

- **Decisão: questionário único.** O módulo tem **6 aulas** — no limiar de ~5–6 que a skill usa para considerar questionários parciais. Optou-se por **um** questionário, seguindo o padrão fixado nos módulos 07 e 08 (também de 4 e 6 aulas, questionário único): as seis aulas formam uma cadeia estritamente sequencial e um único artefato conceitual — o que a máquina controla (a01, a02) → como o projeto é comunicado (a03) → como o corte alcança o projeto (a04) → como o erro é diagnosticado (a05) → como o projeto é transportado para outro material (a06) —, sem dois sub-blocos que se sustentem como parciais independentes. 18 questões, 3 por objetivo, com peso de aplicação/análise nas questões finais de cada objetivo, cumprem a recuperação integrada. Nenhum questionário parcial nem final cumulativo.
- **Objetivos cobertos: 6 de 6, cada um com 3 questões** — matriz **sem célula vazia**:
  - `lapidacao-m09-oa01` — Q01, Q02, Q03
  - `lapidacao-m09-oa02` — Q04, Q05, Q06
  - `lapidacao-m09-oa03` — Q07, Q08, Q09
  - `lapidacao-m09-oa04` — Q10, Q11, Q12
  - `lapidacao-m09-oa05` — Q13, Q14, Q15
  - `lapidacao-m09-oa06` — Q16, Q17, Q18
- **Distribuição por tipo (18 questões):** 6 múltipla escolha (Q01, Q04, Q07, Q10, Q13, Q16); 6 verdadeiro/falso com justificativa (Q02, Q05, Q08, Q11, Q14, Q17); 6 de aplicação/análise sobre caso novo (Q03, Q06, Q09, Q12, Q15, Q18), sendo Q18 de aplicação de fórmula com dados fornecidos (não exige cálculo de tangente de cabeça nem calculadora além do que os dados dão).
- **Calibração cognitiva:** os dois objetivos de nível mais alto — `oa05` (diagnosticar) e `oa06` (aplicar) — recebem a questão de aplicação mais exigente. Q15 apresenta duas fileiras desviadas que **não** se distinguem pela escala do desvio, forçando o critério da inclinação; Q18 exige aplicar a fórmula e interpretar a não linearidade. Os objetivos de nível "explicar/descrever/ler" recebem questão de aplicação que exige justificar mecanismo (Q03, Q06, Q12) ou distinguir o concluível do não concluível (Q09).

### Como cada uma das seis travas da revisão didática foi respeitada

1. **`oa01` — 7-fold só com escopo.** Q03(a) pede o jogo 7-fold **"entre os cinco jogos estudados"** e Q03(b) cobra explicitamente a extrapolação (o 84 fora da lista, com o 14-fold que o 77 não alcança). Q02 usa "os cinco jogos estudados" e o gabarito nomeia os **dois** buracos do 96 (fatores 5 e 7). Q01(c) tem como distrator a versão refutada da primazia do 96 ("cobre mais simetrias que qualquer outro"), corrigida no gabarito para a razão de **notação** (72/84 empatam, 120 supera).
2. **`oa04` — o meetpoint não elimina o erro cumulativo.** Q11 é V/F com a tese refutada como afirmação → **Falso**, e o gabarito reposiciona a vantagem como visibilidade + controle sobre onde o acúmulo é absorvido (faceta ajustável de ângulo mais raso, por último). Q10(c) traz a mesma tese refutada ("cada encontro reseta a referência, o erro nunca se acumula") como distrator. Q12(b) cobra que o local do sintoma não prova o local da causa.
3. **`oa05` — desvio de fileira inteira ≠ ângulo.** Q15 dá duas fileiras inteiras desviadas e exige distingui-las pela **inclinação** (X uniforme e curta com inclinação certa → altura do mastro; Y com inclinação errada → batente). Q15(b) refuta explicitamente o atalho "afeta a fileira inteira, logo é ângulo". Q14 trata a assimetria undercut/overcut (auditoria 🟠 11). Nenhuma questão de `oa05` permite responder pela escala do desvio.
4. **`oa03` — sem "main antes das auxiliares".** Q08 é V/F com essa regra como afirmação → **Falso** (não há regra fixa; controvérsia LC-08; e não é a main que estabelece o contorno). Q07(c) usa a mesma regra como distrator. Q09(c) cobra o que a ordem das linhas **permite** e **não permite** concluir. O cobrável aparece: ordem de grande escala (Q08 gabarito), índices intercalados como padrão main/break (Q09b), princípio dos pontos de referência (Q08 gabarito). Q07(b) e o gabarito de Q07 corrigem "main = mais numerosa" para "main = maiores" (8 × 16 no brilhante redondo).
5. **`oa06` — o tangent ratio não se degrada com o espalhamento.** Q17 é V/F com a inversão como afirmação → **Falso**, gabarito atribuindo a degradação ao **atalho** de somar graus fixos e citando a preservação da vista em planta "por construção". Q16(c) usa a versão invertida como distrator; Q16(d) usa a descrição do atalho como distrator. Q18(d) usa o par **68° → 70,03° (+2,03°)** — o dado que a revisão didática acrescentou ao exemplo — para fechar o argumento da não linearidade.
6. **`oa02` — sem "três colunas" e sem "facetas distinguidas pela altura".** Q04(c) e Q07(d) têm "três colunas / coluna de profundidade" como distrator; o gabarito de Q04 e Q07 e a matriz de travas afirmam que a tabela traz **duas** coordenadas e a profundidade vem do ponto de encontro. Q04(d) e Q06(c) têm "duas facetas de mesmo ângulo e índice empilhadas por altura" como distrator, refutado pela geometria de planos paralelos num sólido convexo. Q04(a) e Q05 usam a formulação corrigida: ângulo e índice = **orientação**; altura = **posição/dimensão**.

### Pontos da auditoria refletidos nos distratores e gabaritos

- **96 padrão por notação, não por cobertura** (🟠 7, 🔵 12) — Q01(c), Q02.
- **77 escopado aos cinco; 84 carrega o fator 7 e o 14-fold** (🟠 8) — Q03.
- **planos paralelos: mesmo ângulo + mesmo índice não coexistem** (🔴 3) — Q04(d), Q06(c).
- **diagrama tabela dois parâmetros; profundidade pelo ponto de encontro** (🟠 6) — Q04(c), Q05, Q07(d).
- **"main antes das auxiliares" não é regra; contorno é da cinta/break** (🔴 4) — Q07(c), Q08.
- **main = maiores, não mais numerosas; tier = mesma altura/mesmo ângulo** (🟠 10) — Q07(b), Q09.
- **sequência: ordem dos pontos, controvérsia LC-08 declarada** (🔴 4, ⚪ 13) — Q08, Q09(c).
- **meetpoint não elimina erro cumulativo; dá visibilidade + controle** (🟠 5) — Q10(c), Q11, Q12(b).
- **meetpoint garante consistência interna, não a correção da especificação** (`PTO-LIMITE-GARANTIA-001`) — Q12(c).
- **desvio de fileira inteira tem duas causas; a inclinação separa** (🔴 2) — Q15.
- **undercut e overcut não são simétricos; overcut irreversível** (🟠 11) — Q14.
- **cheater corrige fração de dente, não dente inteiro, nunca ângulo** (`DGN-SINT-GIRO-001`) — Q13.
- **tangent ratio: o atalho se degrada, não o método; par 68°→70,03°** (🔴 1) — Q16, Q17, Q18.
- **pavilhão e coroa convertidos em separado** (🟠 9) — Q16(b).
- **fórmula e exemplo numérico verificados à quarta casa** (`TGR-FORMULA-DEF-001`, `TGR-EX-NUMERICO-001`) — Q18, com os valores de tangente fornecidos no enunciado.

### Nível teórico preservado

Nenhuma questão pede ou avalia destreza de bancada: não se pergunta como trocar a roda de índice, como girar o cheater, com que pressão ou sequência cortar, como levar fisicamente uma faceta ao vértice, nem como operar software de conversão. Os verbos são explicar, descrever, prever, justificar, distinguir, diagnosticar (no sentido de ler o sintoma → coordenada, como a coluna "Ajuste que corrige" da árvore da aula 05) e aplicar uma fórmula. Q13 e Q15 nomeiam a coordenada corretiva porque isso **é** o objetivo `oa05` (identificar qual das três está fora), não uma instrução de mão. Pré-requisito do curso de Gemologia citado só por nome (índice de refração, em Q18 pelo contexto do material).

<!--
nivel: ensino-medio-com-gemologia-v1
questoes: 18
decisao_quantidade: 'questionario unico — 6 aulas no limiar de ~5-6 da skill; padrao dos modulos 07 e 08 (questionario unico); cadeia estritamente sequencial e um unico artefato conceitual (o que a maquina controla -> como o projeto e comunicado -> como o corte alcanca o projeto -> como o erro e diagnosticado -> como o projeto e transportado), sem sub-blocos independentes'
cobertura:
  lapidacao-m09-oa01: [lapidacao-m09-q01, lapidacao-m09-q02, lapidacao-m09-q03]
  lapidacao-m09-oa02: [lapidacao-m09-q04, lapidacao-m09-q05, lapidacao-m09-q06]
  lapidacao-m09-oa03: [lapidacao-m09-q07, lapidacao-m09-q08, lapidacao-m09-q09]
  lapidacao-m09-oa04: [lapidacao-m09-q10, lapidacao-m09-q11, lapidacao-m09-q12]
  lapidacao-m09-oa05: [lapidacao-m09-q13, lapidacao-m09-q14, lapidacao-m09-q15]
  lapidacao-m09-oa06: [lapidacao-m09-q16, lapidacao-m09-q17, lapidacao-m09-q18]
tipo_distribuicao: '6 multipla escolha (q01,q04,q07,q10,q13,q16); 6 verdadeiro/falso com justificativa (q02,q05,q08,q11,q14,q17); 6 aplicacao/analise sobre caso novo (q03,q06,q09,q12,q15,q18), q18 de aplicacao de formula com dados fornecidos'
celulas_vazias: 0
travas_revisao_didatica_respeitadas:
  trava_1_oa01_7fold_escopo: 'q03(a) pede o jogo entre os cinco estudados; q03(b) cobra a extrapolacao (84 fora da lista, 14-fold); q02 escopa aos cinco e nomeia os dois buracos do 96; q01(c) distrator = primazia do 96 por cobertura, corrigida para notacao no gabarito'
  trava_2_oa04_meetpoint_nao_elimina_erro: 'q11 V/F tese refutada = Falso, gabarito reposiciona como visibilidade + controle; q10(c) distrator = cada encontro reseta a referencia; q12(b) local do sintoma nao prova local da causa'
  trava_3_oa05_fileira_inteira_nao_e_angulo: 'q15 duas fileiras desviadas distinguidas pela inclinacao (X->altura do mastro, Y->batente); q15(b) refuta explicitamente o atalho afeta-a-fileira-logo-e-angulo; nenhuma questao de oa05 resolvivel pela escala do desvio'
  trava_4_oa03_sem_main_antes_das_auxiliares: 'q08 V/F essa regra = Falso (nao ha regra fixa; LC-08; contorno e da cinta/break); q07(c) mesmo distrator; q09(c) o que a ordem das linhas permite/nao permite concluir; cobravel presente: ordem grande escala, indices intercalados main/break, principio dos pontos'
  trava_5_oa06_tangent_ratio_nao_se_degrada: 'q17 V/F inversao = Falso, atalho de somar graus fixos como culpado, vista em planta por construcao; q16(c) e q16(d) distratores com a versao invertida e com o atalho; q18(d) usa o par 68->70,03 (+2,03)'
  trava_6_oa02_sem_tres_colunas_sem_altura_distingue: 'q04(c)/q07(d) distrator tres colunas / coluna de profundidade; q04(d)/q06(c) distrator facetas empilhadas por altura (planos paralelos); q04(a)/q05 usam angulo+indice=orientacao, altura=posicao'
auditoria_refletida: 'q01/q02 (96 por notacao, nao por cobertura); q03 (77 escopado, 84 com fator 7); q04/q06 (planos paralelos); q04/q05/q07 (diagrama tabela dois parametros); q07/q08/q09 (main = maiores nao mais numerosas; sequencia por pontos; LC-08); q10/q11/q12 (meetpoint nao elimina erro; consistencia interna nao correcao da especificacao); q13 (cheater fracao de dente); q14 (undercut/overcut assimetricos); q15 (fileira inteira duas causas); q16/q17/q18 (atalho se degrada nao o metodo; pav e coroa separados; formula e exemplo verificados)'
nivel_teorico: 'nenhuma questao avalia destreza de bancada; verbos explicar/descrever/prever/justificar/distinguir/diagnosticar(sintoma->coordenada)/aplicar formula; q13 e q15 nomeiam a coordenada corretiva porque e o proprio oa05; pre-requisito do curso-gemologia citado so por nome'
-->
