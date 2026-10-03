# Aula 14: Relações de fases binárias dos tectossilicatos — eutético, peritético, solução sólida completa e ponto de mínimo

**ID:** geologia-avancado-m40-a14
**Módulo:** [[40-mineralogia-dos-tectossilicatos-modulo|Módulo 40 — Mineralogia dos tectossilicatos]]
**Duração estimada:** ~30 min
**Nível:** avançado (graduação plena / pós-graduação em geologia)
**Objetivo:** ler os quatro tipos de diagrama binário T–X que governam a cristalização dos tectossilicatos, aplicar a regra das fases para saber quantos graus de liberdade o sistema tem em cada ponto, e explicar com eles feições que você já viu em lâmina — intercrescimento granofírico, leucita corroída, plagioclásio zonado, dois feldspatos numa mesma rocha.

## Antes de começar, você precisa saber

- Da [[40-mineralogia-dos-tectossilicatos-aula-02-grupo-da-silica-polimorfos-e-diagrama-p-t|aula 02]]: o diagrama P–T dos polimorfos de SiO₂ (Figura 2 do guia) e as inversões deslocativas.
- Da [[40-mineralogia-dos-tectossilicatos-aula-07-solvus-e-exsolucao-pertitas|aula 07]]: o **solvus** dos feldspatos alcalinos e o mecanismo de exsolução — esta aula acrescenta o que acontece **acima** do solidus.
- Da [[40-mineralogia-dos-tectossilicatos-aula-10-teor-de-anortita-e-zonamento|aula 10]]: zonamento normal, inverso e oscilatório em plagioclásio.
- Da [[40-mineralogia-dos-tectossilicatos-aula-13-formulas-estruturais|aula 13]]: como sair de uma análise química para An–Ab–Or.
- Da [[40-mineralogia-dos-tectossilicatos-aula-11-feldspatoides|aula 11]]: a reação KAlSi₂O₆ + SiO₂ → KAlSi₃O₈ e a barreira da saturação em sílica.

## Conteúdo

### O vocabulário mínimo

Um **diagrama de fase** é a representação gráfica dos campos de estabilidade — em geral admitida como **estável** — de fases minerais ou sintéticas, em função de parâmetros termodinâmicos fundamentais (P, T, composição).

- **Sistema:** qualquer parte do universo, dela individualizada para um objetivo específico de estudo ou experimentação.
- **Fase:** qualquer parte desse sistema individualizável por uma **composição química ou estado físico particular e característico**.
- **Número de componentes:** o número de composições químicas distintas necessárias para descrever **todas** as fases presentes.

Assim, o diagrama P–T dos polimorfos de sílica é **unário** (um componente, SiO₂), enquanto os solvus dos feldspatos alcalinos e dos plagioclásios são **binários** (componentes Ab–Or e Ab–An).

Os parâmetros de estado se dividem em **extensivos** — proporcionais à extensão do sistema, portanto aditivos: volume, massa, número de moléculas, energia — e **intensivos** — independentes da extensão e não aditivos: pressão litostática, de fluidos, de gases, e temperatura. Razões entre extensivos podem ser intensivas: massa e volume são extensivos, mas a **densidade** é intensiva.

### A regra das fases

Sistemas em **equilíbrio heterogêneo** — multifásicos, com o potencial químico de cada constituinte igual em todas as fases — obedecem à **regra das fases de Gibbs**: os graus de liberdade (**F**), ou variância, equivalem à diferença entre o número de variáveis independentes e o número de equações de estado. Em termos de componentes (**C**) e fases (**P**):

$$F + P = C + 2$$

No diagrama unário da sílica:

| Situação | P | F | Nome |
|---|:---:|:---:|---|
| Ponto dentro do campo da **coesita** | 1 | **2** | divariante |
| Sobre a linha coesita / quartzo-α | 2 | **1** | univariante |
| **Ponto triplo** coesita + quartzo-α + quartzo-β | 3 | **0** | invariante |

Traduzindo: no campo divariante você pode variar P e T de modo independente sem mudar o número de fases. Sobre a linha univariante, fixada uma variável a outra fica automaticamente definida — sair da linha faz uma das fases desaparecer. No ponto invariante, qualquer alteração de P ou T elimina uma ou duas das três fases.

> [!important] A forma que vamos usar de fato
> Todos os diagramas desta aula são **seções isobáricas** T–X: P é constante. Com um parâmetro intensivo fixado, o número de equações de estado cai de 1 e a regra passa a
> $$F + P = C + 1$$
> Esqueça isso e você vai calcular variância errada em todos os pontos singulares. Os diagramas discutidos aqui representam pressões litostáticas ou de fluidos **relativamente baixas, 1–2 kbar**.

Na prática, a maioria das paragêneses das rochas segue um caso particular, a **regra das fases mineralógicas (de Goldschmidt)**: como as paragêneses naturais são estáveis dentro de **intervalos** de P e T, e não em valores específicos, teremos quase sempre F = 2 e portanto **P = C** — o número de fases tende a igualar o número de componentes.

### Como ler um diagrama T–X

Três convenções resolvem quase tudo:

1. **Liquidus** separa o campo só-fundido (L) do campo L + cristais. **Solidus** separa L + cristais do campo só-sólido. Acima do liquidus, só fusão; abaixo do solidus, só matéria sólida.
2. Sólidos e fusões em equilíbrio estável estão também em **equilíbrio térmico**: suas posições sobre solidus e liquidus estão sempre sobre a mesma **isoterma**, paralela ao eixo composicional. Basta traçar a horizontal na temperatura de interesse e ler as interseções.
3. A **regra da balança** (segmentos proporcionais) dá as proporções relativas: num campo bifásico, a proporção de cada fase é o segmento **oposto** dividido pelo segmento total.

Nossa estratégia de leitura será sempre a mesma — a mesma da aula 07: **partir de uma composição inicial X e baixar a temperatura**, perguntando a cada passo quais fases existem e qual a composição de cada uma.

> [!note] Por que as temperaturas de fusão caem nas misturas
> Adicionar SiO₂ a NaAlSi₃O₈ abaixa progressivamente a temperatura de fusão e de cristalização — e vice-versa. É consequência de princípios termodinâmicos básicos, e é o que faz as duas curvas de liquidus descerem em sentidos opostos até se interceptarem.
> Pela **equação de Clapeyron**, acréscimos de pressão litostática elevam proporcionalmente as temperaturas de fusão. A adição de **H₂O** faz o oposto — mas por outro motivo: você está **adicionando um terceiro componente**, não apenas mudando P.

### VII.1 · Eutético simples: NaAlSi₃O₈–SiO₂

O binário mais simples: duas fases puras, **totalmente imiscíveis**. Três campos — L; L + C (L + albita, L + tridimita); e C (albita + tridimita).

Descendo a partir de uma composição X rica em sílica:

1. Em **T₁** a projeção de X cruza o liquidus e começa a cristalizar **cristobalita**.
2. Em **T_I** a cristobalita se transforma em **tridimita**, o polimorfo estável abaixo dessa isoterma.
3. À medida que T cai, o fundido **se empobrece em SiO₂** (consumida pela tridimita) e caminha sobre o liquidus. Em T₂ a composição do fundido é L₂; pela regra da balança, a proporção em peso de tridimita é PL₂/L₂T₂ e a de fundido, PT₂/L₂T₂.
4. Em **T_E** começa a cristalizar **albita**, que se junta à tridimita. Aqui coexistem fundido L_E + tridimita + albita: **C = 2, P = 3, logo F = 0**. A composição do fundido e as proporções relativas de albita e tridimita **permanecem fixas até a cristalização se completar**, e a temperatura não cai enquanto houver fundido.

No ponto eutético **E**, a composição do fundido L_E é **exatamente igual à composição global dos cristais que se formam**. A reação

$$L_E \;\rightarrow\; \mathrm{Ab}_{(c)} + \mathrm{Td}_{(c)} \qquad (T = \text{constante})$$

é uma **reação de cristalização eutética**, também dita **congruente**. Esgotado o fundido, a temperatura volta a cair e, em equilíbrio, a tridimita converte-se a quartzo-β e este a quartzo-α ao cruzar a isoterma de **573 °C**.

**Duas generalizações:**

1. **Qualquer** composição intermediária entre SiO₂ e NaAlSi₃O₈ termina obrigatoriamente a cristalização no eutético.
2. A **ordem** em que as fases cristalizam depende **exclusivamente da composição inicial** — a partir do lado albítico, a albita é que vem primeiro.

**Em desequilíbrio**, com resfriamento rápido, podem sobreviver cristobalita metaestável junto com tridimita, ou cristobalita + tridimita + quartzo-α abaixo de 573 °C. Abaixo de **270 °C** a cristobalita-β inverte diretamente para cristobalita-α; abaixo de **130 °C**, a tridimita-β passa a tridimita-α.

> [!tip] O retorno a algo que você já viu
> Os intercrescimentos **(micro)granofíricos** entre feldspato alcalino ou plagioclásio sódico e quartzo da [[40-mineralogia-dos-tectossilicatos-aula-09-feldspatos-ao-microscopio-e-intercrescimentos|aula 09]] são, em sua grande maioria, **cristalização eutética da fração residual** de magmas graníticos. A textura é o registro direto de F = 0: duas fases crescendo simultaneamente, em proporção fixa, a temperatura constante.

### VII.2 · Peritético simples: KAlSi₂O₆–SiO₂

A diferença em relação ao caso anterior: existe uma **fase adicional de composição fixa, intermediária** entre os extremos — o KAlSi₃O₈, formado pela reação leucita + sílica que você viu na aula 11. No eixo em % em peso de SiO₂, a leucita está em **55,1 %** e o feldspato potássico em **64,8 %** — valores estequiométricos exatos, calculáveis das fórmulas (KAlSi₂O₆: 2 × 60,08 / 218,25 = 55,06 %; KAlSi₃O₈: 3 × 60,08 / 278,33 = 64,76 %). O guia lê ~54,5 e ~65,5 do eixo da Figura 19, que é esquemática; use os valores estequiométricos.

A cristalização de uma composição X começa em T_c com **leucita**; o fundido migra sobre o liquidus rumo a composições mais ricas em sílica. Ao atingir **T_P**, no ponto **P**, o excesso de sílica torna a leucita **instável**, e ela **reage com a fusão** para formar feldspato potássico, a temperatura constante (novamente P = 3, C = 2 ⇒ **F = 0**):

$$\mathrm{leucita} + L_P \;\rightarrow\; \mathrm{feldspato\ potássico}$$

Esta é uma **reação peritética, incongruente**: um sólido previamente formado reage com o fundido para gerar **outro sólido, composicionalmente distinto**. Convertida toda a leucita, se sobrar fundido a cristalização prossegue com feldspato potássico até o **eutético**, onde a tridimita se junta.

**Quatro desfechos, conforme a composição inicial:**

| Composição inicial X | Resultado final |
|---|---|
| Entre leucita e Kfs (**insaturada**) | leucita + feldspato potássico |
| Exatamente KAlSi₃O₈ (**saturada**) | só feldspato potássico |
| Entre Kfs e a projeção do peritético | feldspato potássico + alguma tridimita |
| Entre o eutético e SiO₂ | cristobalita/tridimita primeiro, depois eutético |

A conclusão maior: **leucita e quartzo não podem coexistir em equilíbrio estável**.

> [!warning] O sistema sódico é diferente — e é por isso que a leucita corroída existe
> As relações entre nefelina e SiO₂ são dadas por **dois binários eutéticos unidos pelo membro albítico**: um insaturado (NaAlSiO₄–NaAlSi₃O₈) e um saturado (NaAlSi₃O₈–SiO₂). A **albita é um máximo termal — uma barreira térmica**. Como a cristalização implica queda de temperatura, **não é possível passar de um lado para o outro**.
> No sistema potássico, ao contrário, o peritético permite que uma fusão insaturada gere feldspato potássico e, em certas circunstâncias, chegue a frações residuais **saturadas**. Por isso o guia observa que situação similar **não** é possível no sistema NaAlSiO₄–SiO₂.

**Em desequilíbrio**, a reação peritética pode não se completar — por cinética (faltou tempo) ou por **impossibilidade física**: o feldspato potássico formado às expensas da leucita precipita **sobre ela**, usando-a como germe, e cria um **manto (armadura)** que isola o núcleo de leucita do fundido. Alternativamente, a leucita pode ter sido **fisicamente extraída** do sistema. Daí ser teoricamente possível encontrar **restos corroídos de leucita preservados dentro de cristais de feldspato potássico** em algumas rochas sieníticas.

> [!tip] Ponto de pausa sugerido
> Esta é a aula mais longa do módulo (~30 min cheios, quatro sistemas binários). Os dois primeiros — eutético e peritético — formam um bloco fechado: ambos tratam de fases **imiscíveis** e ambos terminam com F = 0 num ponto fixo. Se você está estudando de uma vez, **pare aqui**. Os dois sistemas seguintes mudam de assunto: passam a tratar de **soluções sólidas**, e a comparação que interessa é com o que você acabou de ver, não dentro deles.

### VII.3 · Solução sólida completa: NaAlSi₃O₈–CaAl₂Si₂O₈

Aqui os componentes são **perfeitamente miscíveis** pela substituição acoplada NaSi ⇄ CaAl. Qualquer composto intermediário é uma fase possível e **única** para dada temperatura. Não há eutético: as temperaturas de cristalização das intermediárias ficam **entre** as dos membros finais.

Descendo a partir de X: em T_c precipitam cristais de composição **C_ss** (ss = solução sólida). Com a queda de T, a composição do fundido caminha sobre o liquidus e a dos cristais caminha, mais ou menos em paralelo, sobre o solidus. **Os cristais previamente formados se reequilibram continuamente com o fundido**, de modo que, a qualquer temperatura, **todos os cristais têm a mesma composição** — porque liquidus e solidus em equilíbrio estão sob a mesma isoterma.

Em T₁, sólidos C₁ss coexistem com fundido L₁, e a regra da balança dá:

$$C_{1ss}(\%) = 100 \times \frac{L_1X_1}{L_1C_{1ss}} \qquad L_1(\%) = 100 \times \frac{X_1C_{1ss}}{L_1C_{1ss}}$$

A cristalização termina quando a composição do **último sólido C_Fss coincide com a composição inicial X** — que é o teste de fechamento do balanço de massa.

**Em desequilíbrio**, quando a velocidade de cristalização supera a velocidade de reequilíbrio, o resultado é **zonamento composicional normal**: do núcleo para a borda, composições progressivamente mais ricas em **Ab**. Nesses casos os últimos sólidos **não** têm a composição do sistema inicial. Variações progressivas ou flutuantes dos parâmetros intensivos (P litostática, de fluidos) alteram a forma das curvas e as temperaturas, e podem gerar zonamentos **inversos** (núcleos mais albíticos) e **oscilatórios**.

### VII.4 · Solução sólida parcial com ponto de mínimo: NaAlSi₃O₈–KAlSi₃O₈

Ab e Or são apenas **parcialmente miscíveis** nos ambientes geológicos comuns. Os mecanismos de cristalização são similares aos do caso anterior — e a parte **subsólida** deste diagrama, com o solvus, é exatamente o que você estudou na aula 07.

O traço típico é o **ponto de mínimo M**. Quando um fundido qualquer alcança M — composição L_m —, **todo o fundido restante cristaliza como uma fase única C_ss, de composição igual à do fundido**, a temperatura constante.

> [!important] Mínimo × eutético: parecidos onde não importa, opostos onde importa
> **Semelhança:** nos dois, a composição global dos sólidos iguala a do liquidus, e a temperatura fica fixa até o fundido acabar.
> **Diferença decisiva:** no mínimo cristaliza **um único sólido**, uma solução sólida; no eutético cristalizam **duas fases não miscíveis entre si**, simultaneamente.

Valem aqui as mesmas observações sobre zonamento, com um detalhe elegante: para composições **à esquerda de M** (mais albíticas), o zonamento normal enriquece progressivamente a borda em **molécula de ortoclásio**; para as **à direita de M** (mais potássicas), a evolução é para composições progressivamente mais **albíticas**. As bordas convergem para M, venham de onde vierem.

**O efeito da água.** Introduzir H₂O abaixa as temperaturas de fusão e cristalização: liquidus e solidus **descem**. Mas a curva de **solvus não desce junto**. Para P(H₂O) da ordem de **2,5 kbar ou mais**, o solidus intercepta o solvus e **o ponto de mínimo se converte num ponto eutético** — passando a permitir a cristalização **simultânea de dois feldspatos**, um albítico e outro potássico.

Depois da cristalização primária a partir do liquidus, outras fases feldspáticas ainda podem surgir por **exsolução em estado sólido** — as pertitas da aula 07.

## Exemplo trabalhado

**Situação.** Retome o feldspato alcalino **F1** da aula 13, cuja composição calculamos como **An₁,₇Ab₆₇,₈Or₃₀,₅** (molar). Imagine uma fusão homogênea com essa composição. Represente-a no diagrama Ab–Or e descreva a cristalização em equilíbrio estável.

**Passo 1 — a conversão que quase todo mundo esquece.** O diagrama Ab–Or é traçado em **percentagens em peso**, mas o cálculo da aula 13 entregou **proporções moleculares**. É preciso converter.

Desprezando o An (1,7 %), normalizamos ao binário: Ab 68,96 e Or 31,04 **mol %**. Com PM(Ab) = 262,22 e PM(Or) = 278,33 g/mol:

| Componente | mol % | × PM | massa relativa | **% em peso** |
|---|---:|---:|---:|---:|
| Ab | 68,96 | 262,22 | 18 083 | **67,7** |
| Or | 31,04 | 278,33 | 8 639 | **32,3** |
| | | | 26 722 | 100,0 |

**Ab₆₇,₇Or₃₂,₃ em peso.** O deslocamento é de ~1,3 ponto, porque o Or é mais pesado que o Ab. Pequeno aqui — mas é sistemático, e num sistema com pesos moleculares mais díspares seria fatal.

**Passo 2 — a cristalização.** Nas condições da Figura 21 (P < 2 kbar), F1 plota **muito próximo do ponto de mínimo M**, em composições intermediárias do sistema. A leitura tem duas partes:

*Se X cai exatamente sobre M:* toda a fusão cristaliza a **temperatura constante** como uma **fase única** de feldspato alcalino, de composição igual à do fundido — sem intervalo de cristalização e sem zonamento. É o caso-limite.

*Se X cai ligeiramente do lado albítico:* a cristalização começa no liquidus com um (feldspato-Na)ss mais sódico que X; fundido e sólidos caminham sobre liquidus e solidus rumo a M, e o **zonamento normal** enriquece as bordas em molécula de **ortoclásio**. A cristalização se completa quando o último sólido atinge a composição X.

**Passo 3 — a história subsólida, que é onde a rocha guarda a informação.** Cristalizado um feldspato alcalino homogêneo de ~Ab₆₈Or₃₂, o resfriamento o leva para dentro do **solvus** (aula 07). A partir daí, o destino depende só da taxa de resfriamento:

- **Resfriamento muito rápido** (vulcânico): a difusão não acompanha; preserva-se um feldspato **homogêneo e desordenado** — sanidina/anortoclásio, opticamente limpo, com o solvus atravessado sem exsolução visível, no máximo criptopertita.
- **Resfriamento lento** (plutônico): a fase homogênea se desmistura, gerando **pertita** — hospedeiro potássico com lamelas albíticas — e o feldspato potássico ordena progressivamente rumo a microclínio, com geminação em grade.

A 500 °C, as composições das duas fases coexistentes se leem diretamente nos dois ramos do solvus na isoterma correspondente, e suas **proporções relativas** saem da regra da balança, com X entre elas.

**A lição de conjunto.** A **composição** do feldspato foi decidida acima do solidus, pelo liquidus e pelo ponto de mínimo. A **microestrutura e o estado estrutural** foram decididos abaixo, pelo solvus e pela taxa de resfriamento. São duas histórias independentes gravadas no mesmo cristal — e ler uma no lugar da outra é o erro central deste módulo inteiro.

## Erros comuns

- **Usar F + P = C + 2 numa seção isobárica.** Com P fixa, é **C + 1**. Todo ponto singular (eutético, peritético, mínimo) tem F = 0 com P = 3 e C = 2 — e a conta só fecha na forma correta.
- **Plotar proporções molares num diagrama em % em peso.** O eixo de composição dos diagramas T–X clássicos é **em peso**. Converta antes.
- **Chamar o ponto de mínimo de eutético.** No mínimo cristaliza **uma** solução sólida; no eutético, **duas fases imiscíveis**.
- **Achar que o eutético só vale para a composição eutética.** Toda composição intermediária **termina** no eutético; o que muda é a **ordem** de cristalização.
- **Tratar a reação peritética como se fosse eutética.** Ela é **incongruente**: consome um sólido para produzir outro, distinto.
- **Supor que a barreira térmica da albita vale também para o sistema potássico.** Não vale — o peritético do sistema K é justamente o que permite atravessar de insaturado para saturado.
- **Ler o diagrama como receita determinística.** Quase toda feição realmente vista em lâmina — zonamento, leucita mantelada, cristobalita metaestável — existe porque o equilíbrio **não** foi atingido.
- **Achar que adicionar H₂O é "só baixar a temperatura".** H₂O é um **componente a mais**; e ela desloca liquidus e solidus **sem** deslocar o solvus, o que muda a topologia do diagrama.

## O que não concluir

- **Que P = C (Goldschmidt) é uma lei.** É um caso particular muito frequente, decorrente de as paragêneses naturais serem estáveis em **intervalos** de P–T. Não substitui a regra de Gibbs.
- **Que estes diagramas descrevem magmas reais.** São sistemas de **dois componentes**, obtidos por experimentação com limitações severas. Magmas têm muitos componentes, voláteis e histórias de mistura. Os binários dão o **esqueleto do raciocínio**, não a resposta numérica.
- **Que "não pode coexistir em equilíbrio estável" significa "nunca coexiste".** Leucita e quartzo, ou fóide e quartzo, podem ser encontrados juntos — e quando isso ocorre, é **informação**: registra desequilíbrio, blindagem, mistura de magmas ou xenocristal.
- **Que as coordenadas exatas de E, P e M são universais.** Elas dependem de P, de P(H₂O) e da presença de outros componentes. Acima de ~2,5 kbar de P(H₂O), o próprio **mínimo M vira eutético** — a topologia muda. As figuras do guia são esquemáticas.
- **Que o zonamento prova resfriamento rápido em termos absolutos.** Prova que a **cristalização** superou o **reequilíbrio**; a taxa absoluta depende também da difusividade, da composição e da presença de fluidos.

## Recap relâmpago

- **Sistema** = parte do universo isolada para estudo; **fase** = parte individualizável por composição ou estado físico; **componentes** = n° de composições químicas para descrever todas as fases. Sílica P–T = unário; solvus Ab–Or e Ab–An = binários.
- Parâmetros **extensivos** (aditivos: volume, massa, energia) × **intensivos** (P, T); razões de extensivos podem ser intensivas (densidade).
- **Gibbs:** F + P = C + 2. Unário da sílica: campo = divariante (F=2); linha = univariante (F=1); ponto triplo = invariante (F=0). **Seção isobárica: F + P = C + 1.** **Goldschmidt:** paragêneses naturais têm quase sempre F = 2 ⇒ **P = C**.
- **Leitura:** liquidus separa L de L+C; solidus separa L+C de C; equilíbrio ⇒ mesma **isoterma**; proporções pela **regra da balança**. Misturar dois componentes **abaixa** as temperaturas de fusão. Clapeyron: mais P litostática ⇒ mais T; H₂O ⇒ menos T (é um terceiro componente).
- **Eutético (Ab–SiO₂):** fases puras imiscíveis. Em E, C=2, P=3 ⇒ **F=0**: L_E, composição e proporções fixas, T constante. Reação **congruente** L_E → Ab + Td. Toda composição intermediária **termina em E**; só a **ordem** depende de X. ⇒ **textura granofírica**.
- **Peritético (Lc–SiO₂):** fase intermediária de composição fixa (Kfs, **64,8 %** SiO₂ em peso; leucita **55,1 %** — valores estequiométricos). Em P: **leucita + L → Kfs**, reação **incongruente**, F = 0. **Leucita e quartzo não coexistem em equilíbrio estável.** Em desequilíbrio, **leucita corroída mantelada por Kfs**. No sistema sódico, a **albita é barreira térmica** e a travessia é impossível.
- **Solução sólida completa (Ab–An):** miscibilidade total por NaSi ⇄ CaAl; sem eutético; cristais **se reequilibram** e são todos iguais a cada T; fim quando C_Fss = X. Em desequilíbrio ⇒ **zonamento normal** (bordas mais Ab); variações de P ⇒ zonamento **inverso** e **oscilatório**.
- **Solução sólida parcial com mínimo (Ab–Or):** em **M**, todo o fundido cristaliza como **fase única** de composição = à do fundido, a T constante. Difere do eutético por cristalizar **um** sólido, não dois imiscíveis. Zonamento normal converge para M dos dois lados. **P(H₂O) ≥ ~2,5 kbar: solidus corta o solvus e M vira eutético ⇒ dois feldspatos.**
- **Conversão obrigatória:** o eixo é **% em peso**; An–Ab–Or sai **molar**. F1 = Ab₆₉Or₃₁ molar ⇒ **Ab₆₇,₇Or₃₂,₃ em peso**.
- **Composição** decide-se acima do solidus; **microestrutura e estado estrutural**, abaixo dele, pelo solvus e pela taxa de resfriamento.

## Próxima aula

Fim do módulo. Siga para a [[40-mineralogia-dos-tectossilicatos-questionario-parcial-2|avaliação]] — o [[40-mineralogia-dos-tectossilicatos-questionario-final|questionário final]] traz, na Parte D, o roteiro de bancada ao microscópio derivado da Parte B do guia.

Módulo seguinte: [[41-estudos-integrados-projetos-em-geologia-aplicada/41-estudos-integrados-projetos-em-geologia-aplicada-modulo|Módulo 41 — Estudos integrados: projetos em geologia aplicada]]

## Anterior

[[40-mineralogia-dos-tectossilicatos-aula-13-formulas-estruturais|Aula 13 — Cálculo de fórmulas estruturais de tectossilicatos e proporções An–Ab–Or]]

## Fontes

- Definições de diagrama de fase, sistema, fase e número de componentes; parâmetros extensivos e intensivos; regra das fases de Gibbs (F + P = C + 2) e sua aplicação ao diagrama unário da sílica (divariante, univariante, ponto triplo); regra das fases mineralógicas de Goldschmidt (P = C); a forma isobárica F + P = C + 1; a ressalva de que os diagramas representam 1–2 kbar; liquidus, solidus, isotermas e regra da balança; equação de Clapeyron e efeito da adição de H₂O; e os quatro sistemas binários (VII.1 a VII.4) com todas as suas conclusões: Vlach, S. R. F., *A Classe dos Tectossilicatos: Guia Geral da Teoria e Exercício*, IGc-USP, Série Didática USP, item VII e Figuras 18 a 21.
- Sistema NaAlSi₃O₈–SiO₂ (Figura 18) e sistema NaAlSi₃O₈–KAlSi₃O₈ (Figura 21): Tuttle, O. F. & Bowen, N. L. (1958), *Origin of Granite in the Light of Experimental Studies in the System NaAlSi₃O₈–KAlSi₃O₈–SiO₂–H₂O*, GSA Memoir 74 — fonte das figuras segundo o guia.
- Sistema KAlSi₂O₆–SiO₂ (Figura 19): Schairer & Bowen (1955), *in* Deer, Howie & Zussman (1992), conforme creditado no guia.
- Sistema NaAlSi₃O₈–CaAl₂Si₂O₈ (Figura 20): Bowen (1913), *in* Deer, Howie & Zussman (1992), conforme creditado no guia.
- Temperaturas de inversão dos polimorfos de sílica (573 °C, 270 °C, 130 °C) citadas conforme o guia; ver a discussão de valores na [[40-mineralogia-dos-tectossilicatos-aula-02-grupo-da-silica-polimorfos-e-diagrama-p-t|aula 02]] e o achado correspondente no [[40-mineralogia-dos-tectossilicatos-auditoria|relatório de auditoria]].
- Composição F1 usada no exemplo trabalhado: Tabela 2 do guia (item IX.2); fórmula estrutural e conversão molar → peso calculadas nas aulas 13 e 14. O exercício de cristalizar F1 na Figura 21 é o do item IX.3 do guia.

<!--
nivel: avancado
palavras_corpo: ~2560

mapa_objetivo_secao:
  geologia-avancado-m40-oa06: "O vocabulário mínimo" + "A regra das fases" + "Como ler um diagrama T-X" + "VII.1 Eutético simples" + "VII.2 Peritético simples" + "VII.3 Solução sólida completa" + "VII.4 Solução sólida parcial com ponto de mínimo" + "Exemplo trabalhado"
  geologia-avancado-m40-oa04: "VII.4 Solução sólida parcial com ponto de mínimo" + "Exemplo trabalhado" (passo 3, história subsólida e solvus)
  geologia-avancado-m40-oa01: "VII.2 Peritético simples" (barreira da saturação em sílica, fóide x quartzo)

alegacoes_auditaveis:
  - claim_id: TECTO-M40-A14-CONCEITOS-001
    claim: "Diagrama de fase e a representacao grafica dos campos de estabilidade em condicoes de equilibrio, em geral admitido como estavel, com base em parametros termodinamicos fundamentais. Sistema e uma parte qualquer do universo dele individualizada para um objetivo de estudo; fase e qualquer parte do sistema individualizavel por composicao quimica ou estado fisico particular e caracteristico; numero de componentes e o numero de composicoes quimicas distintas para descrever todas as fases presentes. O diagrama P-T dos polimorfos de silica e unario; os solvus dos feldspatos alcalinos e dos plagioclasios sao binarios."
    risk: fato
    source: "Vlach, Guia dos Tectossilicatos, item VII"
  - claim_id: TECTO-M40-A14-GIBBS-002
    claim: "A regra das fases de Gibbs estabelece F + P = C + 2. No diagrama unario da silica, um ponto no campo da coesita e divariante (P=1, F=2), a linha coesita/quartzo de baixa e univariante (P=2, F=1) e o ponto triplo coesita + quartzo de baixa + quartzo de alta e invariante (F=0). Em secoes isobaricas do espaco PTX o numero de equacoes de estado diminui de 1 e a regra assume a forma F + P = C + 1."
    risk: fato
    source: "Vlach, Guia dos Tectossilicatos, item VII, equacao VII.1"
  - claim_id: TECTO-M40-A14-GOLDSCHMIDT-003
    claim: "A regra das fases mineralogicas de Goldschmidt estabelece que, como as paragenses minerais naturais sao estaveis dentro de certos intervalos de P e T e nao para valores especificos, tem-se quase sempre F = 2 e portanto P = C, ou seja, o numero de fases sera em geral igual ao numero de componentes."
    risk: fato
    source: "Vlach, Guia dos Tectossilicatos, item VII"
  - claim_id: TECTO-M40-A14-EUTETICO-004
    claim: "No sistema eutetico simples NaAlSi3O8-SiO2, no ponto eutetico E coexistem fundido LE, tridimita e albita, com C = 2 e P = 3, logo F = 0 na secao isobarica; a composicao do fundido e as proporcoes relativas de albita e tridimita permanecem constantes ate a cristalizacao se completar, a temperatura constante. A reacao LE = Ab + Td e uma reacao de cristalizacao eutetica, tambem denominada congruente. A composicao do fundido LE e exatamente igual a composicao global dos cristais que se formam. Quaisquer composicoes intermediarias completam a cristalizacao no ponto eutetico, e a ordem de cristalizacao depende exclusivamente da composicao inicial."
    risk: fato
    source: "Vlach, Guia dos Tectossilicatos, item VII.1 e Figura 18 (modificado de Tuttle & Bowen, 1958)"
  - claim_id: TECTO-M40-A14-GRANOFIRICO-005
    claim: "Os intercrescimentos (micro)granofiricos entre feldspatos alcalinos ou plagioclasios sodicos e quartzo podem ser explicados, em sua grande maioria, por cristalizacao eutetica da fracao residual de magmas de composicao granitica."
    risk: interpretacao
    source: "Vlach, Guia dos Tectossilicatos, item VII.1"
  - claim_id: TECTO-M40-A14-PERITETICO-006
    claim: "No sistema peritetico KAlSi2O6-SiO2 existe uma fase adicional de composicao fixa intermediaria, KAlSi3O8. No ponto peritetico P (P = 3 fases, C = 2, F = 0 em secao isobarica) a leucita previamente formada torna-se instavel e reage com a fusao para formar feldspato potassico a temperatura constante: leucita + LP = feldspato potassico, reacao peritetica incongruente. No eixo em % em peso de SiO2 a leucita situa-se em 55,1 e o feldspato potassico em 64,8, valores estequiometricos exatos. A analise do diagrama demonstra que leucita e quartzo nao podem coexistir em equilibrio estavel."
    risk: numero
    source: "Vlach, Guia dos Tectossilicatos, item VII.2 e Figura 19 (modificado de Schairer & Bowen, 1955, in Deer et al., 1992); percentagens recalculadas por estequiometria nesta auditoria — CORRIGE a leitura ~54,5/~65,5 do eixo esquematico da Figura 19"
  - claim_id: TECTO-M40-A14-BARREIRA-007
    claim: "As relacoes de fase entre nefelina e SiO2 sao definidas por dois sistemas binarios euteticos unidos pelo membro intermediario albitico: um insaturado, NaAlSiO4-NaAlSi3O8, e outro saturado, NaAlSi3O8-SiO2. A composicao albitica e um maximo termal, uma barreira termica, de modo que nao e possivel passar de um lado para o outro durante a cristalizacao, ja que esta implica diminuicao de temperatura. Situacao similar a do sistema potassico, em que o peritetico permite atingir composicoes saturadas a partir de fusoes insaturadas, nao e possivel no sistema NaAlSiO4-SiO2."
    risk: fato
    source: "Vlach, Guia dos Tectossilicatos, item VII.2"
  - claim_id: TECTO-M40-A14-ARMADURA-008
    claim: "Em desequilibrio a reacao peritetica pode nao se completar, por cinetica ou por impossibilidade fisica: o feldspato potassico formado as expensas da leucita precipita sobre ela como substrato e gera um manto ou armadura que inviabiliza o contato entre a leucita e a fusao; alternativamente a leucita pode ter sido fisicamente extraida do sistema. E portanto teoricamente possivel encontrar restos corroidos de leucita preservados em cristais de feldspato potassico em algumas rochas sieniticas."
    risk: interpretacao
    source: "Vlach, Guia dos Tectossilicatos, item VII.2"
  - claim_id: TECTO-M40-A14-SSCOMPLETA-009
    claim: "No sistema NaAlSi3O8-CaAl2Si2O8 os componentes sao perfeitamente misciveis pela substituicao NaSi <-> CaAl e qualquer composto intermediario e uma fase possivel e unica para dada temperatura. Em equilibrio os cristais previamente formados se reequilibram continuamente com o liquidus e, para qualquer temperatura, todos os cristais apresentam a mesma composicao; a cristalizacao se completa quando a composicao do ultimo solido coincide com a composicao inicial do sistema. Em desequilibrio, quando a velocidade de cristalizacao supera a de reequilibrio, forma-se zonamento composicional normal, com composicoes progressivamente mais ricas em Ab do nucleo para a borda; variacoes dos parametros intensivos podem gerar zonamentos invertidos e oscilatorios."
    risk: fato
    source: "Vlach, Guia dos Tectossilicatos, item VII.3 e Figura 20 (modificado de Bowen, 1913, in Deer et al., 1992)"
  - claim_id: TECTO-M40-A14-MINIMO-010
    claim: "No sistema NaAlSi3O8-KAlSi3O8 os componentes sao apenas parcialmente misciveis. O aspecto tipico e a presenca de um ponto de minimo M: quando o fundido chega a Lm, todo o fundido restante cristaliza como fase unica Css de composicao igual a do fundido, sob temperatura constante. Pontos de minimo assemelham-se a euteticos porque a composicao global dos solidos iguala a do liquidus e a temperatura permanece fixa ate a cristalizacao terminar, mas contrastam porque no minimo cristaliza um unico solido, uma solucao solida, enquanto no eutetico cristalizam conjuntamente fases nao misciveis entre si. Composicoes a esquerda de M desenvolvem zonamento normal com enriquecimento em molecula de ortoclasio para as bordas, e composicoes a direita de M evoluem para composicoes mais albiticas."
    risk: fato
    source: "Vlach, Guia dos Tectossilicatos, item VII.4 e Figura 21 (modificado de Tuttle & Bowen, 1958)"
  - claim_id: TECTO-M40-A14-AGUA-011
    claim: "A introducao de H2O abaixa as temperaturas de fusao e cristalizacao, deslocando liquidus e solidus para temperaturas menores, mas nao desloca a curva de solvus. Para pressoes de H2O da ordem de 2,5 kbar ou superiores, o solidus intercepta o solvus e o ponto de minimo se converte em um ponto eutetico, possibilitando a cristalizacao simultanea de dois feldspatos, um albitico e outro potassico."
    risk: numero
    source: "Vlach, Guia dos Tectossilicatos, item VII.4"
  - claim_id: TECTO-M40-A14-CONVERSAO-012
    claim: "O diagrama da Figura 21 representa as fases em percentagens em peso dos componentes Ab e Or, sendo necessario converter os resultados moleculares obtidos no calculo de formula estrutural para os equivalentes em peso antes de aplica-lo. Para a composicao F1 (An1,7Ab67,8Or30,5 molar), normalizada ao binario Ab-Or (Ab 68,96 e Or 31,04 mol %) e com PM(Ab) = 262,22 e PM(Or) = 278,33 g/mol, obtem-se Ab67,7Or32,3 em peso."
    risk: numero
    source: "Instrucao do item IX.3 de Vlach, Guia dos Tectossilicatos; conversao calculada nesta aula"
  - claim_id: TECTO-M40-A14-ESQUEMATICO-013
    claim: "As coordenadas exatas dos pontos eutetico, peritetico e de minimo dependem da pressao, da pressao de H2O e da presenca de outros componentes; as figuras do guia sao esquematicas e representam pressoes litostaticas ou de fluidos relativamente baixas, de 1 a 2 kbar. Sistemas experimentais consideram em geral um numero reduzido de componentes, o que dificulta comparacoes diretas com processos naturais."
    risk: interpretacao
    source: "Vlach, Guia dos Tectossilicatos, item VII (limitacoes experimentais e condicoes dos diagramas)"
-->
