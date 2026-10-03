# Revisão didática — Módulo 23: Introdução à modelagem numérica geodinâmica

**Revisado em:** 2026-09-19 · **Modo:** `review-and-fix`
**Material:** as 7 aulas do módulo (agora 9), o hub do módulo
**Executada depois da** [[23-modelagem-numerica-geodinamica-auditoria|auditoria científica]] do mesmo dia, sobre o material já corrigido — como a ordem da cadeia exige.

> [!success] **Veredito: BEM ENSINADO COM RESSALVAS**
> O módulo ensina bem o que se propõe: a progressão é sólida, as remissões internas são densas e (com uma exceção que a auditoria já pegou) corretas, e cada aula tem exemplo trabalhado com conferência à mão. Os defeitos encontrados são de **dois tipos só**, e os dois são consequência do mesmo fato: o módulo tentou caber em sete aulas um conteúdo de nove.

## Resumo

🔴 1 bloqueia · 🟠 5 prejudicam · 🟡 2 atrito · 🔵 1 sugestão

**Todos os 🔴 e 🟠 foram resolvidos.** Os dois 🟡 também. O 🔵 fica registrado como oportunidade.

**Carga, antes e depois:**

| | antes | depois |
|---|---|---|
| Aulas | 7 | **9** |
| Aulas acima do teto de 30 min | **2** (a03 com 31,2; a04 com 30,8) | **0** |
| Faixa de duração | 21,6 a 31,2 min | **23 a 29 min** |
| Duração total do módulo | ~194 min | ~239 min |
| Objetivos declarados sem cobertura | **1** (`oa01`, metade "gráfica") | 0 |

A métrica é a mesma usada na revisão didática do Módulo 22 deste curso (~84 palavras/min sobre o corpo da aula), para que as decisões sejam comparáveis entre módulos.

---

## O diagnóstico em uma frase

> [!warning] **Duas aulas estavam fazendo dois trabalhos cada, e a auditoria científica — corretamente — empurrou as duas para fora do teto.**
> A antiga Aula 03 empilhava *a física do meio contínuo* (continuidade, Stokes) sobre *a representação numérica do contínuo* (malhas, escalonamento, lagrangiano/euleriano). A antiga Aula 04 empilhava *a formulação física do calor* sobre *os esquemas numéricos que a resolvem*. São pares de conteúdo que **se usam** mas não **se constroem** — e essa é exatamente a assinatura de uma aula que deveria ser duas.
>
> Nas duas, a segunda metade não participava do exemplo trabalhado. Esse foi o sintoma que fechou o diagnóstico: uma aula cujo exemplo só exercita metade do que ela ensina está declarando, sem querer, onde fica o seu corte.
>
> A auditoria científica do mesmo dia acrescentou precisão a ambas (o tensor de taxa de deformação, o princípio do máximo, o comportamento de `np.gradient`) — precisão que o módulo precisava e que esta revisão não desfez em nada. O efeito colateral foi empurrar as duas aulas de "no limite" para "acima do limite". A divisão é a forma de ficar com as duas coisas.

---

## Achados

### 🔴 1. A Aula 01 promete Matplotlib e não entrega uma linha de Matplotlib

**claim_id:** `DID-M23-A01-OBJETIVO-001`
**Tipo:** objetivo declarado não coberto
**Onde:** Aula 01 · cabeçalho ("Ao final você vai conseguir"), seção "Matplotlib: visualizar o resultado", os dois exemplos trabalhados
**Escopo:** correção local

**Problema:** a aula declara, entre seus resultados esperados, "produzir um gráfico de linha e um mapa de cores com Matplotlib". Ela **descreve** `plt.plot`, `plt.imshow` e `plt.contourf` em prosa, e argumenta bem por que um gráfico bem rotulado é instrumento de conferência e não enfeite. E então: **nenhum dos dois exemplos trabalhados contém uma linha de Matplotlib.** Os dois importam apenas NumPy e terminam em `print`.

Isso é o defeito mais grave que uma aula de ferramenta pode ter, e é por isso que é 🔴 e não 🟠. O objetivo é **performativo** — "produzir um gráfico" —, e ninguém aprende a produzir um gráfico lendo a descrição de uma função. Um aluno que siga a aula inteira chega ao fim sem ter visto uma figura ser feita, e as oito aulas seguintes vão pedir exatamente isso a cada campo calculado. Some-se que este é o único objetivo do módulo (`oa01`) que menciona a palavra "gráficas": metade de um objetivo de aprendizagem do módulo não era ensinada em lugar nenhum.

A auditoria científica já havia pego a metade factual disto — o hub afirmava que havia código Matplotlib nos exemplos trabalhados, o que era falso (achado 14 da auditoria) — e encaminhou a lacuna pedagógica para cá.

**Correção aplicada:** o código Matplotlib entrou **nos dois blocos de código que já existiam**, junto dos dados que ele plota, em vez de virar um terceiro exemplo. Essa escolha é deliberada: um gráfico pertence ao lado do array que ele desenha, e criar um exemplo separado teria acrescentado carga sem acrescentar aprendizado.

- **Exemplo 1** ganhou quatro linhas que desenham a geoterma, com `invert_yaxis()` — e um parágrafo explicando por que *essa linha específica* importa: uma geoterma se lê com a profundidade crescendo para baixo, e esquecê-la produz uma figura que parece certa e está de cabeça para baixo.
- **Exemplo 2** ganhou cinco linhas que exibem o campo `F = X − Z` como mapa de cores com barra de escala rotulada, e um parágrafo que faz o aluno **prever os extremos antes de rodar** (máximo 3 no canto superior direito, mínimo −2 no inferior esquerdo) — fechando com a regra que o módulo inteiro vai usar: *quando o gráfico contradiz a previsão, o erro está no código.*
- Recap atualizado com os dois hábitos operacionais (inverter o eixo de profundidade; sempre rotular a barra de cor) e com a regra da previsão.

**Sobre as alegações novas:** a sintaxe foi conferida contra a documentação oficial do Matplotlib (parâmetro `origin` de `imshow`, parâmetro `label` de `colorbar`). O código **não pôde ser executado** — Matplotlib não está instalado no ambiente de verificação, ao contrário do NumPy. Duas alegações novas (`GEODIN-M23-A01-MATPLOTLIB-API-006`, `GEODIN-M23-A01-EXEMPLO-MAPA-007`) foram registradas e sinalizadas ao auditor.

---

### 🟠 2. A antiga Aula 04 (calor) empilhava formulação física e solução numérica

**claim_id:** `DID-M23-A04-CARGA-001`
**Tipo:** sobrecarga cognitiva / dois modos de pensar numa aula só
**Onde:** antiga Aula 04, inteira
**Escopo:** **exige dividir a aula**
**Resolvido por:** divisão em **Aula 05** + **Aula 06**

**Problema:** 2.587 palavras após as correções da auditoria, ~31 min reais contra **30 declarados — já no teto do plugin antes mesmo da auditoria**. Quinze conceitos novos, e nenhum deles decorativo: lei de Fourier, condutividade térmica, conservação de energia, difusão, produção, advecção, difusividade térmica, malha espaço-tempo, diferença progressiva no tempo, FTCS, o número r, von Neumann, princípio do máximo, BTCS, matriz tridiagonal, algoritmo de Thomas. **Todos operacionais** — o aluno tem de *fazer conta* com cada um, não apenas reconhecê-lo.

O corte era visível a olho nu: das quatro seções, a primeira é a única que **não** fala de discretização, e as outras três não acrescentam nada à física. E o exemplo trabalhado — o pulso de temperatura com r = 0,25 e r = 1,0 — é inteiramente sobre o esquema explícito, ou seja, **não exercitava a primeira seção**.

Havia ainda um defeito de compressão dentro da primeira seção: os três termos da equação do calor (difusão, produção, advecção) eram definidos dentro de **um único parágrafo corrido**, que no mesmo fôlego ainda introduzia a difusividade térmica e a advertência sobre κ e λ acrescentada pela auditoria. A distinção difusão × advecção — que é a que os alunos mais confundem — recebia meia frase.

**Correção aplicada — divisão:**

- **Aula 05 — "Calor: lei de Fourier, conservação de calor, produção e advecção"** (1.944 palavras, ~23 min). Recebeu a seção física, com os três termos **promovidos a parágrafos próprios**, cada um com sua leitura física: a difusão ganhou a explicação da curvatura ("um ponto mais frio que a média dos vizinhos recebe calor dos dois lados"), e a distinção difusão × advecção virou uma frase destacada. A difusividade κ ganhou seção própria, e a advertência sobre κ ≠ λ — a correção 🔴 da auditoria — virou **callout**, ficando mais visível do que estava.
- **Aula 06 — "Solução numérica da equação do calor: FTCS e BTCS"** (2.310 palavras, ~28 min). Recebeu a discretização espaço-tempo, os dois esquemas e o **exemplo trabalhado original, preservado palavra por palavra**. A condição de estabilidade ganhou **seção própria** — "A condição de estabilidade, e o que significa 'impossível'" —, que é onde a correção 🟠 3 da auditoria (princípio do máximo) pôde finalmente ser desenvolvida em vez de espremida.

**Correção aplicada — exemplo novo para a Aula 05.** A Parte 1 ficou sem exemplo, e ganhou um construído para ser **autoconsistente com o módulo**: calcula κ = k/(ρCp) a partir de três propriedades de rocha crustal e o fluxo condutivo pela lei de Fourier. Os parâmetros foram escolhidos de modo que os **resultados** reproduzam valores que a auditoria já verificou em outras aulas — κ = 1×10⁻⁶ m²/s (o mesmo da Aula 07, item azul B24) e q = 54 mW/m², dentro da faixa 40-70 mW/m² da Aula 07 (B25). O ganho pedagógico é que o κ que a Aula 06 e a Aula 07 usam deixa de ser um número caído do céu. A segunda situação é classificatória e **não tem valor numérico nenhum**: dados três cenários geológicos, dizer qual termo domina. Uma alegação nova (`GEODIN-M23-A04-EXEMPLO-PROPRIEDADES-008`) foi registrada e sinalizada ao auditor — é a única das quatro novas que envolve valores medidos.

---

### 🟠 3. A antiga Aula 03 empilhava a física do contínuo e sua representação numérica

**claim_id:** `DID-M23-A03-CARGA-002`
**Tipo:** sobrecarga cognitiva / dois modos de pensar numa aula só
**Onde:** antiga Aula 03, inteira
**Escopo:** **exige dividir a aula**
**Resolvido por:** divisão em **Aula 03** + **Aula 04**

**Problema:** 2.622 palavras após as correções da auditoria, ~31 min reais contra 29 declarados — **a aula mais pesada do módulo**. Catorze conceitos novos: meio contínuo, continuidade, divergente, incompressibilidade, Boussinesq, solenoidal, Navier-Stokes, Reynolds, Stokes, tensor de taxa de deformação, malha estruturada, não estruturada, escalonada, lagrangiano, euleriano, particle-in-cell.

Como na Aula 04, o corte estava declarado pela própria estrutura: a quarta seção **usa** as equações das três primeiras mas não contribui para construí-las, e **não participa do exemplo trabalhado** (o teste de divergente, que é inteiramente sobre a equação da continuidade).

E havia compressão severa: essa quarta seção era **uma única seção de quatro parágrafos** em que três famílias de malha, a patologia da pressão colocalizada, duas descrições de movimento e o método de partículas em célula estavam empilhados. O primeiro parágrafo sozinho era um período de mais de cem palavras com três definições dentro — malha estruturada, não estruturada e escalonada, todas numa frase.

**Correção aplicada — divisão:**

- **Aula 03 — "Mecânica do contínuo: a equação da continuidade e a equação de Stokes"** (2.401 palavras, ~29 min). Ficou com as três primeiras seções e o exemplo trabalhado original, **palavra por palavra**, inclusive as quatro correções da auditoria que o tocavam. Ganhou dois esclarecimentos que a aula original deixava implícitos: a **condição de validade** da hipótese do contínuo enunciada como regra ("a escala do fenômeno supera largamente a escala do grão — abaixo disso, estas equações não servem") e o desfazimento do nó aparente da aproximação de Boussinesq (ela não diz que ρ é constante; diz que sua variação é desprezível no balanço de massa e decisiva no de forças).
- **Aula 04 — "Malhas e descrições lagrangiana e euleriana"** (2.036 palavras, ~24 min). Os quatro blocos que estavam empilhados viraram **quatro seções**, cada uma com espaço para ser explicada. O maior ganho está na malha escalonada: a aula original afirmava que ela "evita um problema numérico clássico de oscilação espúria da pressão" — uma afirmação correta e completamente opaca. Agora o **mecanismo** está dito: numa malha colocalizada, a diferença central do gradiente de pressão pula o vizinho imediato, de modo que uma oscilação de nó em nó não produz gradiente nenhum no cálculo e o solver a aceita como legítima. A analogia do bote no rio foi preservada e ganhou **onde ela quebra** — no rio o bote é distinto da água; no modelo, o "bote" é a própria rocha.

**Correção aplicada — exemplo novo para a Aula 04.** Duas situações. A primeira é aritmética verificável (as coordenadas escalonadas, e a regra de que *n* nós dão *n−1* centros de célula — a origem de metade dos erros de índice em código de malha escalonada). A segunda é classificatória, sem valor numérico: três problemas geodinâmicos, escolher malha e descrição. Duas alegações novas registradas e sinalizadas ao auditor.

---

### 🟠 4. O pré-requisito de Python não aparece onde o aluno planeja o estudo

**claim_id:** `DID-M23-M23-PREREQPYTHON-003`
**Tipo:** pré-requisito não declarado no lugar certo
**Onde:** hub do módulo · seção "Pré-requisitos"
**Escopo:** correção local

**Problema:** a Aula 01 declara, honestamente, no seu cabeçalho: "Pressupõe familiaridade mínima com sintaxe Python (variáveis, funções, listas) — se você nunca programou em Python, vale uma introdução rápida à linguagem antes desta aula, fora do escopo deste curso."

O hub, porém, diz apenas "Nenhum [pré-requisito] dentro deste curso" e um aviso longo sobre o Módulo 30 do curso base. **Saber programar não aparece.** E o hub é justamente onde o aluno decide quando vai começar o módulo e o que precisa providenciar antes — descobrir que precisa aprender uma linguagem de programação já dentro da Aula 01 é descobrir tarde. Este é, além disso, o **único módulo do curso** com essa dependência, o que torna a omissão mais custosa, não menos: não há como o aluno inferi-la do padrão dos outros módulos.

**Correção aplicada:** callout próprio no hub, na seção de pré-requisitos, ao lado do aviso do Módulo 30, com a distinção explícita entre o que a Aula 01 ensina (NumPy e Matplotlib) e o que ela pressupõe (a linguagem), e com o motivo de estar duplicado ali ("registrado aqui, e não só lá, porque é no hub que se planeja o estudo").

---

### 🟠 5. Durações declaradas calculadas com réguas diferentes

**claim_id:** `DID-M23-M23-DURACOES-004`
**Tipo:** estimativa de carga não confiável
**Onde:** cabeçalho das 7 aulas originais
**Escopo:** correção local (todas as aulas)

**Problema:** as durações declaradas não eram comparáveis entre si. A Aula 01 declarava 28 min para 1.812 palavras (≈ 65 palavras/min); a antiga Aula 07 declarava 30 min para 2.287 (≈ 76 palavras/min). Uma variação de **17%** na régua, dentro do mesmo módulo.

Isso não é pedantismo de contagem: a duração declarada é a única informação que o aluno autodidata tem para planejar uma sessão de estudo, e se ela é calculada de formas diferentes de aula para aula, ela não serve para comparar nem para somar. Um aluno que reserva "uma hora para as aulas 01 e 02" está tomando uma decisão com base num número que não significa a mesma coisa nas duas.

**Correção aplicada:** as nove aulas foram redimensionadas com **a mesma régua** — ~84 palavras/min sobre o corpo, a métrica já usada na revisão didática do Módulo 22 deste curso, para que as estimativas sejam comparáveis **entre módulos** também. O campo `palavras_corpo` de cada aula foi corrigido para a contagem real (vários estavam defasados, alguns por mais de 300 palavras). O módulo passa a declarar **239 min ≈ 4 h**.

| Aula | Palavras | Antes | Depois |
|---|---|---|---|
| 01 | 2.173 | 28 | **26** |
| 02 | 2.152 | 29 | **26** |
| 03 | 2.401 | (29, pré-divisão) | **29** |
| 04 | 2.036 | — | **24** |
| 05 | 1.944 | (30, pré-divisão) | **23** |
| 06 | 2.310 | — | **28** |
| 07 | 2.362 | 29 | **28** |
| 08 | 2.342 | 29 | **28** |
| 09 | 2.283 | 30 | **27** |

---

### 🟠 6. O parágrafo mais denso do módulo ficou mais denso com a auditoria

**claim_id:** `DID-M23-A05-DENSIDADE-006`
**Tipo:** densidade irregular
**Onde:** Aula 07 (antiga 05) · seção "Litosfera continental", parágrafo da relação de Lachenbruch
**Escopo:** correção local

**Problema:** um parágrafo de cerca de 300 palavras encadeando, sem respiro: a relação dq/dz = A(z), as **duas** convenções de sinal (descendente e ascendente), a conclusão física, o modelo exponencial A(z) = A₀e^(−z/hr), a espessura de escala hr, a origem em Lachenbruch (1970) e a integração final até q₀ = q_r + A₀·hr. Sete movimentos distintos.

A correção 🟠 4 da auditoria científica — necessária e bem-feita — inseriu ali as duas convenções de sinal, que antes não existiam. O texto ficou **mais correto e menos legível**, e essa é uma consequência previsível de corrigir sem reestruturar; é para isso que a revisão didática vem depois.

Havia ainda uma lacuna: **hr era nomeada em negrito como "espessura de escala" e nunca definida.** O aluno sabia que era importante e não sabia o que era.

**Correção aplicada:** o parágrafo foi quebrado em **dois passos rotulados** — "Passo 1: o fluxo de calor acumula a produção que está acima dele" (onde a correção da auditoria está integral, palavra por palavra) e "Passo 2: dar uma forma a A(z) e integrar" —, com a forma exponencial promovida a fórmula destacada. A conclusão que importa daqui para a frente ficou em negrito, isolada. E hr ganhou sua definição: a profundidade em que a produção cai a 1/e do valor de superfície — que não é fato novo, é leitura direta da exponencial que já estava ali.

---

### 🟡 7. O título da Aula 02 promete mais do que a aula faz

**claim_id:** `DID-M23-A02-TITULO-005`
**Tipo:** título que não corresponde
**Onde:** Aula 02 · título e abertura
**Escopo:** correção local

**Problema:** o título é "Álgebra linear, cálculo e equações diferenciais parciais". A aula ensina EDO × EDP e diferenças finitas para a segunda derivada. **Álgebra linear** aparece apenas na última seção, como o *destino* para onde a discretização leva, com a solução explicitamente delegada ao Módulo 30 e à Aula 06. **Cálculo** não é ensinado em lugar nenhum — é pressuposto.

Não é erro, e por isso é 🟡: os dois termos estão no título porque são os pré-requisitos que a aula reativa. Mas um aluno que chega esperando revisão de álgebra linear não a encontra, e demora a entender que não vai encontrar.

**Correção aplicada:** callout de abertura explicitando o que o título promete e o que a aula faz — quais partes são pré-requisito reativado, de onde vêm (Módulo 30, aulas 01, 02 e 04), qual é o conteúdo genuinamente novo, e onde a álgebra linear é efetivamente exercida (Aula 06). **O título e o nome do arquivo não foram alterados** de propósito: renomear quebraria os wikilinks e o registro em `course-state.yaml` por um ganho que uma nota de três linhas entrega igual.

---

### 🟡 8. Duas frases quebradas

**claim_id:** `DID-M23-A01-FRASE-007` e `DID-M23-A07-CONCORDANCIA-008`
**Tipo:** redação
**Escopo:** correção local

Ambas já registradas pela auditoria científica como observações fora de escopo, e encaminhadas para cá.

- Aula 01, seção "Por que geodinâmica precisa de modelagem numérica": *"É exatamente esse é o fio condutor deste módulo"* — verbo duplicado. → "É esse o fio condutor deste módulo".
- Aula 09 (antiga 07), primeira seção: *"a coluna afinada é mais leve, e a superfície subsidem quase instantaneamente"* → "subside".

---

### 🔵 9. O módulo não tem uma figura, num assunto que é visual por natureza

**claim_id:** `DID-M23-M23-VISUAL-009`
**Tipo:** sugestão
**Escopo:** fora do escopo desta revisão — registrado para decisão do usuário

**Observação:** depois da correção do 🔴 1, o aluno produz figuras rodando o código — o que é melhor do que ver figuras prontas, e resolve o objetivo. Mas três conceitos do módulo permanecem difíceis de segurar só com prosa, e são exatamente aqueles em que uma figura carrega mais informação que um parágrafo:

1. **A malha escalonada** (Aula 04). O arranjo "pressão no centro, velocidade no meio das faces" é uma configuração geométrica, e o texto gasta um parágrafo descrevendo o que um diagrama de uma célula resolveria instantaneamente.
2. **O padrão em xadrez da pressão colocalizada** (Aula 04). O mecanismo agora está explicado, mas o padrão é literalmente visual.
3. **O envelope de resistência da litosfera** (Aula 08). É um gráfico — resistência por profundidade, com a quebra frágil-dúctil — descrito em palavras.

Não foi corrigido porque produzir esses visuais está fora do que esta skill faz, e improvisá-los em ASCII ou em descrição textual seria pior que a ausência. Fica como decisão do usuário: os dois primeiros seriam bons candidatos a um trecho de código Matplotlib adicional na Aula 04, aproveitando que o aluno já sabe plotar depois da Aula 01 corrigida.

---

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo trabalhado | Situação |
|---|---|---|---|
| `oa01` — programar em Python operações numéricas **e gráficas** com NumPy e Matplotlib | Aula 01 (as quatro seções) | **sim** — dois exemplos, agora com NumPy **e** Matplotlib | ✅ **resolvido** — a metade "gráfica" não era coberta (achado 🔴 1) |
| `oa02` — resolver EDPs por métodos explícitos e implícitos; explicar continuidade e Navier-Stokes | Aulas 02, 03, 04, 06 | sim, nas quatro | ✅ coberto, e agora com uma aula por sub-tarefa |
| `oa03` — calcular geotermas e fluxo de calor oceânico e continental, interpretar controles | Aulas 05 e 07 | sim, nas duas | ✅ coberto — a Aula 05 passou a ter exemplo próprio, que antes não existia para a metade física |
| `oa04` — explicar a reologia e aplicá-la a extensão e colisão | Aulas 08 e 09 | sim, nas duas | ✅ coberto |

**Nota sobre `oa02`:** é o objetivo mais carregado do módulo — quatro aulas o servem. Isso não é defeito: ele contém três tarefas distintas (formular EDP, discretizar, resolver por dois esquemas), e as quatro aulas correspondem a elas. Vale, porém, que o questionário o cubra em mais de um item, o que a recomendação de três parciais já garante (ele atravessa as Parciais 1 e 2).

---

## Formato do questionário — confirmação

A auditoria científica recomendou **3 parciais + 1 final cumulativo**, com blocos 01-02 / 03-04 / 05-07, e registrou a recomendação como robusta a uma eventual divisão de aula.

**Confirmada sem alteração.** As duas divisões caíram **dentro** dos blocos existentes:

| Parcial | Antes | Depois | Fronteira |
|---|---|---|---|
| 1 | 01-02 | **01-02** | inalterada |
| 2 | 03-04 | **03-06** | 03│04 e 05│06 são cortes *internos* ao bloco |
| 3 | 05-07 | **07-09** | inalterada |

As duas descontinuidades conceituais — 02│03 (método → física) e 06│07 (equação genérica → litosfera concreta com números medidos) — são exatamente as mesmas de antes. A divisão não criou fronteira nova, que é precisamente o critério que a auditoria enunciou.

---

## O que está bem feito

Vale registrar, porque precisa ser preservado nas próximas revisões e porque quem escreveu acertou nisto:

- **A densidade de remissões internas é a maior do curso, e elas funcionam.** Cada aula diz de onde vem o que está usando e para onde aquilo vai. O aluno nunca fica sem saber por que está vendo aquilo. (A auditoria encontrou **uma** remissão fabricada em dezenas — taxa muito baixa.)
- **Todo exemplo trabalhado tem conferência à mão antes da saída do código.** Isso é raro e é pedagogicamente caro de fazer. Num módulo computacional, é a diferença entre ensinar a programar e ensinar a copiar: o aluno aprende que o código confirma a conta, não a substitui. A auditoria executou os sete blocos e **nenhuma saída declarada estava errada** — o que só foi verificável porque o autor as declarou explicitamente.
- **O exemplo do caso estável × caso instável (hoje Aula 06) é o melhor do módulo.** Ele mostra o mesmo cálculo com um único parâmetro alterado e deixa o desastre acontecer à vista. É a forma certa de ensinar uma condição de estabilidade — muito melhor que enunciar a desigualdade e pedir que se confie nela.
- **O fio condutor calor → reologia → deformação é explícito e sustentado.** A Aula 08 explica por que a precisão do campo térmico importa, e a Aula 09 colhe as duas coisas. Um módulo quantitativo com essa costura é incomum.
- **A analogia do bote no rio é boa** — concreta, memorável e do tamanho certo. Esta revisão só acrescentou onde ela quebra.

---

## Registro das correções

**Aplicadas em:** 2026-09-19

| # | claim_id | Sev. | Desfecho | Arquivos |
|---|---|---|---|---|
| 1 | `DID-M23-A01-OBJETIVO-001` | 🔴 | Resolvido — Matplotlib acrescentado aos dois exemplos | aula-01 |
| 2 | `DID-M23-A04-CARGA-001` | 🟠 | Resolvido — **divisão** em Aulas 05 + 06 | aula-05 (novo recorte), aula-06 (nova) |
| 3 | `DID-M23-A03-CARGA-002` | 🟠 | Resolvido — **divisão** em Aulas 03 + 04 | aula-03 (novo recorte), aula-04 (nova) |
| 4 | `DID-M23-M23-PREREQPYTHON-003` | 🟠 | Resolvido — callout no hub | modulo.md |
| 5 | `DID-M23-M23-DURACOES-004` | 🟠 | Resolvido — régua única nas 9 aulas | as 9 aulas |
| 6 | `DID-M23-A05-DENSIDADE-006` | 🟠 | Resolvido — parágrafo quebrado em dois passos; hr definida | aula-07 |
| 7 | `DID-M23-A02-TITULO-005` | 🟡 | Resolvido — callout de escopo (título preservado) | aula-02 |
| 8 | `DID-M23-A01-FRASE-007`, `DID-M23-A07-CONCORDANCIA-008` | 🟡 | Resolvidos | aula-01, aula-09 |
| 9 | `DID-M23-M23-VISUAL-009` | 🔵 | **Não corrigido** — fora do escopo, registrado para decisão | — |

**Arquivos renumerados:** antiga a05 → **07**, antiga a06 → **08**, antiga a07 → **09**. IDs (`geologia-avancado-m23-aNN`) e todas as remissões internas atualizados; nenhum wikilink quebrado no módulo, e nenhuma referência às aulas deste módulo a partir de outros módulos do curso.

> [!important] **Os `claim_id` da auditoria NÃO foram renumerados**
> Deliberadamente, seguindo a convenção do Módulo 20 deste curso. Um claim com prefixo `A03` pode hoje estar declarado na Aula 04; um `A04`, na Aula 06. Renumerá-los quebraria a rastreabilidade com `23-modelagem-numerica-geodinamica-auditoria.json`. Cada aula afetada traz a nota `nota_alegacoes_migradas` no seu bloco de metadados, e o relatório da auditoria ganhou um adendo com a tabela de equivalência.

### Nenhuma correção da auditoria científica foi desfeita

Conferido achado a achado. As quatro que mais corriam risco na divisão:

- **🔴 1 `KAPPA-DECAIMENTO-006`** → integral na Aula 05, e **promovido a callout**: ficou mais visível do que estava.
- **🟠 3 `MAXIMOPRINCIPIO-007`** → integral na Aula 06, e **ganhou seção própria**. O formato de aula única não tinha espaço para desenvolvê-lo.
- **🟠 2, 6, 7, 8** (`STOKESVISCOSO`, `ORDEMDIFCENTRAL`, `GRADIENTEBORDA`, `PURESHEAR`) → integrais na Aula 03, palavra por palavra.
- **🟠 4 `SINALFLUXO-008`** → integral na Aula 07, dentro do Passo 1 do parágrafo reestruturado.

### Quatro alegações novas, sinalizadas ao auditor

Nasceram aqui e **não** passaram pela auditoria científica, que é anterior a elas. Nenhuma bloqueia o gate.

| claim_id | Aula | Verificação já feita | O que falta |
|---|---|---|---|
| `GEODIN-M23-A01-MATPLOTLIB-API-006` | 01 | sintaxe contra a documentação oficial do Matplotlib | execução (Matplotlib não instalado no ambiente) |
| `GEODIN-M23-A01-EXEMPLO-MAPA-007` | 01 | aritmética do campo já verificada pela auditoria (B5) | conferência da figura |
| `GEODIN-M23-A03-MALHA-COLOCALIZADA-010` | 04 | ancorada em Gerya (2019) e Patankar (1980) | verificação contra fonte |
| `GEODIN-M23-A03-EXEMPLO-ESCALONADA-011` | 04 | **conferida por execução** | — |
| `GEODIN-M23-A04-EXEMPLO-PROPRIEDADES-008` | 05 | **aritmética conferida por execução**; ambos os resultados coincidem com valores já auditados (B24, B25) | **representatividade dos três parâmetros de entrada** — a de maior prioridade, e a única com valores medidos |

**Pendências:** o 🔵 9 (visuais), que aguarda decisão do usuário, e a passagem pontual do `auditor-cientifico` sobre as cinco alegações novas acima.

**Não foram alterados:** questionário e flashcards — **não existem ainda**. Esta skill não os alteraria de todo modo; desalinhamento com a avaliação é reportado, não corrigido aqui.

---

*Relatório gerado pela skill `revisor-didatico` em modo `review-and-fix`, executada após o `auditor-cientifico` sobre o material já corrigido.*
