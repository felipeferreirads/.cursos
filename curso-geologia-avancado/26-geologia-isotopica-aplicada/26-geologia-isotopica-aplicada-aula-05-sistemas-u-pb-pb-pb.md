# Aula 05: Sistemas U-Pb e Pb-Pb — diagramas concórdia, discórdia, idades modelo de Pb e interpretação geológica

**ID:** geologia-avancado-m26-a05
**Módulo:** [[26-geologia-isotopica-aplicada-modulo|Módulo 26 — Geologia isotópica aplicada]]
**Duração estimada:** ~28 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** entender como dois sistemas de decaimento independentes, operando em paralelo a partir de dois isótopos de urânio, permitem construir o diagrama concórdia — uma ferramenta que não apenas data, mas também diagnostica perda de chumbo sem descartar a amostra — e calcular uma idade Pb-Pb, que dispensa até a medida de urânio.
**Ao final você vai conseguir:** calcular uma idade concordante a partir de uma razão ²⁰⁶Pb*/²³⁸U medida; explicar o que representam os interceptos superior e inferior de uma linha de discórdia no diagrama concórdia; calcular uma idade Pb-Pb a partir de uma razão ²⁰⁷Pb*/²⁰⁶Pb*; e justificar por que o zircão é o mineral mais usado neste sistema.
**Pré-requisito:** [[26-geologia-isotopica-aplicada-aula-01-radioatividade-lei-decaimento-geocronologia-espectrometria-massa|Aula 01]] (a equação geral da idade, aplicada aqui duas vezes em paralelo, e a temperatura de bloqueio), [[26-geologia-isotopica-aplicada-aula-02-metodos-k-ar-ar-ar|Aula 02]] (a premissa de filho inicial desprezível, que aqui reaparece por outro mecanismo químico, e a fragilidade de uma medida isolada) e [[26-geologia-isotopica-aplicada-aula-03-sistema-rb-sr|Aulas 03]]–[[26-geologia-isotopica-aplicada-aula-04-metodo-sm-nd|04]] (a técnica da isócrona, que ajuda a situar por que o U-Pb, com dois relógios simultâneos, é estruturalmente diferente).

## Conteúdo

### Dois relógios no mesmo mineral

O urânio natural tem dois isótopos radioativos de meia-vida longa relevantes para geocronologia — ²³⁸U e ²³⁵U — e cada um decai, por uma longa cadeia de decaimentos intermediários de vida curta (que atingem equilíbrio secular e, para fins de datação, podem ser tratados como se o decaimento fosse de um único passo efetivo), para um isótopo de chumbo diferente:

$${}^{238}\text{U} \rightarrow {}^{206}\text{Pb} \qquad (\lambda_{238} = 1{,}55125\times10^{-10}\ \text{ano}^{-1})$$
$${}^{235}\text{U} \rightarrow {}^{207}\text{Pb} \qquad (\lambda_{235} = 9{,}8485\times10^{-10}\ \text{ano}^{-1})$$

Esses dois valores de constante de decaimento — determinados por Jaffey et al. (1971) e adotados como convenção pela IUGS — são notavelmente estáveis na literatura desde então, ao contrário do ⁴⁰K (Aula 02) e, em menor grau, do ⁸⁷Rb (Aula 03): é um dos poucos pares de constantes de decaimento em geocronologia sem controvérsia relevante de recalibração nas últimas décadas, o que torna o sistema U-Pb um dos mais confiáveis do arsenal isotópico para trabalho de altíssima precisão. Um terceiro radionuclídeo de vida longa produz chumbo do mesmo modo, mas ele **não** é um isótopo de urânio: o ²³²Th, isótopo de tório, decai para ²⁰⁸Pb e constitui um sistema adicional (Th-Pb), pouco usado isoladamente mas relevante em minerais ricos em Th, como a monazita.

Como os dois decaimentos de urânio ocorrem **simultaneamente no mesmo mineral**, a partir do mesmo instante de cristalização, um único grão que se comportou como sistema fechado produz **dois** relógios independentes que devem concordar: a idade calculada a partir de ²⁰⁶Pb*/²³⁸U deve ser igual à idade calculada a partir de ²⁰⁷Pb*/²³⁵U. Essa redundância interna — nenhum outro sistema do módulo a tem de forma tão direta — é o que torna o U-Pb capaz de se autotestar.

### O diagrama concórdia

Aplicando a equação geral da idade da Aula 01 a cada um dos dois decaimentos, e assumindo que o mineral não incorporou chumbo comum (não radiogênico) na sua formação — uma premissa razoável para o zircão, discutida adiante —, tem-se:

$$\frac{{}^{206}\text{Pb}^{*}}{{}^{238}\text{U}} = e^{\lambda_{238}t}-1 \qquad \frac{{}^{207}\text{Pb}^{*}}{{}^{235}\text{U}} = e^{\lambda_{235}t}-1$$

O **diagrama concórdia** (também chamado diagrama de Wetherill, em homenagem a George W. Wetherill, que o propôs em 1956) plota ²⁰⁶Pb*/²³⁸U no eixo y contra ²⁰⁷Pb*/²³⁵U no eixo x. Para cada valor de t, as duas equações acima geram um par de coordenadas — variando t continuamente de zero até a idade da Terra, esse par de coordenadas traça uma curva, a **curva concórdia**, que não é uma reta (por causa da diferença entre λ238 e λ235), mas uma curva suavemente côncava, com marcações de idade ao longo dela.

Se um grão de zircão se comportou como sistema perfeitamente fechado desde a cristalização, o ponto correspondente às suas duas razões medidas cai **sobre** a curva concórdia — diz-se que a análise é **concordante**, e a idade lida diretamente na curva é confiável tanto pelo relógio ²³⁸U-²⁰⁶Pb quanto pelo ²³⁵U-²⁰⁷Pb, que necessariamente concordam nesse ponto. É essa concordância mútua, e não a confiança em um único par pai-filho, que dá ao U-Pb concordante um grau de confiabilidade que nenhum sistema isocrônico isolado da Aula 03 ou 04 pode oferecer por si só.

### Discórdia: quando o sistema não ficou fechado, mas a informação não se perde

Zircões reais frequentemente perdem uma fração do chumbo acumulado — por dano à estrutura cristalina causado pela própria radiação alfa emitida durante o decaimento (metamictização), por recristalização parcial durante metamorfismo, ou por lixiviação hidrotermal — sem perder urânio na mesma proporção (o chumbo, com raio iônico e valência diferentes dos do urânio, se comporta de modo distinto na rede cristalina danificada). Quando isso acontece, o ponto medido cai **abaixo** da curva concórdia (ambas as razões Pb*/U diminuem, mas não necessariamente na mesma proporção) — a análise é **discordante**.

A observação empírica central que sustenta a interpretação de dados discordantes é que, quando **vários** grãos (ou vários domínios do mesmo grão, analisados por microssonda ou LA-ICP-MS em pontos distintos) de uma mesma população, todos originalmente cristalizados na mesma idade e todos tendo perdido chumbo em algum evento posterior comum (mas em graus variáveis, dependendo de quanto dano cada grão acumulou), esses pontos discordantes tendem a cair sobre uma **reta** — chamada **discórdia** — que intercepta a curva concórdia em **dois** pontos:

- o **intercepto superior**, que corresponde à idade de cristalização original do zircão (t₁, o evento ígneo ou metamórfico que formou o mineral);
- o **intercepto inferior**, que corresponde à idade do evento que causou a perda de chumbo (t₂, um metamorfismo posterior, ou, em muitos casos práticos, um intercepto inferior próximo de zero, indicando perda de chumbo recente, relacionada ao intemperismo ou à preparação da amostra, sem significado de um evento geológico distinto).

A prática moderna, principalmente com dados de LA-ICP-MS obtidos em muitos grãos de uma mesma amostra, ajusta essa reta de discórdia por regressão sobre um conjunto de pontos (frequentemente dezenas a centenas de análises pontuais numa população de zircões detríticos ou magmáticos), usando software especializado — o mais citado é o Isoplot, desenvolvido por Kenneth Ludwig — que reporta os dois interceptos com suas incertezas. A lição estrutural aqui é que perda parcial de chumbo, ao contrário de uma medida K-Ar de mineral único (Aula 02), **não inutiliza o dado**: o padrão de discordância, lido corretamente através de várias análises, ainda recupera a idade de cristalização original, no intercepto superior.

### O que faz do zircão o mineral preferido do sistema U-Pb

Três propriedades, combinadas, explicam por que o zircão (ZrSiO₄) é, disparadamente, o mineral mais usado em geocronologia U-Pb, à frente de outros minerais acessórios ricos em urânio como monazita, titanita e badeleíta:

- **Incorpora urânio prontamente, mas rejeita chumbo.** O urânio substitui o zircônio na estrutura cristalina do zircão em quantidades apreciáveis (dezenas a milhares de partes por milhão), enquanto o chumbo, com raio iônico e valência incompatíveis com o sítio do zircônio, é fortemente excluído durante a cristalização — de modo que o chumbo comum inicial em um zircão recém-formado é, na prática, próximo de zero, e praticamente todo o chumbo presente hoje é radiogênico. Essa é a mesma lógica de "filho inicial desprezível" do argônio na Aula 02, mas por um mecanismo químico diferente (exclusão estrutural, não volatilidade).
- **É quimicamente e mecanicamente muito resistente.** O zircão resiste a intemperismo, transporte sedimentar e a boa parte de eventos metamórficos de grau baixo a médio sem perder sua composição química original — o que permite que zircões detríticos em uma rocha sedimentar preservem a idade de cristalização de sua rocha-fonte, muitas vezes bilhões de anos mais velha que a deposição do próprio sedimento, um recurso central em análise de proveniência (tema retomado no contexto de bancos de dados geológicos do Módulo 25).
- **Cresce em zonas, registrando eventos sucessivos.** Muitos zircões crescem em zonamento composicional (visível por catodoluminescência), com um núcleo ígneo original sobrecrescido por bordas metamórficas de idade mais jovem, formadas em eventos posteriores. Técnicas de datação *in situ* de alta resolução espacial, como SIMS (espectrometria de massa de íons secundários) e LA-ICP-MS (ablação a laser acoplada a ICP-MS), permitem datar núcleo e borda separadamente no mesmo grão — o tema central da petrocronologia, desenvolvido no Módulo 27 deste curso.

### A idade Pb-Pb: um relógio que dispensa a medida de urânio

Um terceiro tipo de idade neste sistema não usa diretamente a razão de nenhum isótopo de chumbo com urânio, mas sim a razão entre os **dois isótopos radiogênicos de chumbo entre si**: ²⁰⁷Pb*/²⁰⁶Pb*. Dividindo a equação de ²⁰⁷Pb* pela de ²⁰⁶Pb* (ambas da seção do diagrama concórdia acima) e introduzindo a razão isotópica natural do urânio, ²³⁸U/²³⁵U — hoje adotada, para minerais terrestres, no valor de referência 137,818 (Hiess et al., 2012, que revisou o valor mais antigo de 137,88, mostrado não ser universalmente constante entre reservatórios terrestres, mas adotado como valor de consenso prático da comunidade de geocronologia U-Pb) —, obtém-se a **equação da idade Pb-Pb**:

$$\frac{{}^{207}\text{Pb}^{*}}{{}^{206}\text{Pb}^{*}} = \frac{1}{137{,}818}\cdot\frac{e^{\lambda_{235}t}-1}{e^{\lambda_{238}t}-1}$$

Essa equação é **transcendental** em t (não há forma fechada para isolar t algebricamente); na prática, resolve-se por iteração numérica ou por software especializado — mas o princípio conceitual é direto o bastante para um exemplo trabalhado a seguir, resolvido por tentativa. A vantagem estrutural da idade Pb-Pb é que ela usa **apenas razões isotópicas de chumbo**, dispensando qualquer medida de urânio — útil, por exemplo, para minerais que perderam urânio de forma significativa (mas preservaram a razão entre os dois isótopos de chumbo acumulados antes da perda), ou para amostras de chumbo comum em depósitos minerais, onde a idade Pb-Pb do minério é estimada a partir da composição de chumbo herdada de uma fonte crustal ou mantélica sem que o urânio original precise ser conhecido — a base do modelo de evolução do chumbo terrestre de Holmes-Houtermans, usado, entre outras aplicações, para estimar a idade de formação de depósitos de sulfetos metálicos a partir da composição isotópica de chumbo da galena.

## Exemplo trabalhado 1: idade concordante

**Situação.** Um grão de zircão foi analisado por ID-TIMS (diluição isotópica por ionização térmica, o método de mais alta precisão disponível) e mostrou uma razão ²⁰⁶Pb*/²³⁸U = 0,5000 (valor hipotético, escolhido para simplificar a aritmética do exemplo). A análise é concordante (a razão ²⁰⁷Pb*/²³⁵U medida coincide, dentro do erro, com o valor previsto pela curva concórdia para a mesma idade). Qual é a idade do zircão?

**Resolução.** Usando a equação de ²³⁸U-²⁰⁶Pb:

$$t = \frac{1}{\lambda_{238}}\ln(1+0{,}5000) = \frac{\ln(1{,}5000)}{1{,}55125\times10^{-10}}$$

Calculando: ln(1,5000) ≈ 0,405465. Então:

$$t = \frac{0{,}405465}{1{,}55125\times10^{-10}} \approx 2{,}6138\times10^{9}\ \text{anos} \approx 2613{,}8\ \text{milhões de anos}$$

**Conferência com o segundo relógio.** Para essa mesma idade, a equação de ²³⁵U-²⁰⁷Pb prevê:

$$\frac{{}^{207}\text{Pb}^{*}}{{}^{235}\text{U}} = e^{\lambda_{235}t}-1 = e^{(9{,}8485\times10^{-10})(2{,}6138\times10^{9})}-1 \approx e^{2{,}574}-1 \approx 12{,}12$$

Uma razão ²⁰⁷Pb*/²³⁵U de aproximadamente 12,12 é a que se esperaria, no diagrama concórdia, exatamente no mesmo ponto de idade 2613,8 Ma que o relógio ²³⁸U-²⁰⁶Pb devolveu — a concordância entre os dois valores (que numa análise real seria testada contra a razão efetivamente medida, não apenas prevista, como neste exemplo simplificado) é o que classificaria esta análise como concordante e confiável. Uma idade de aproximadamente 2,61 Ga situa este zircão hipotético no Neoarqueano.

## Exemplo trabalhado 2: idade Pb-Pb por iteração

**Situação.** Uma amostra de chumbo (por exemplo, galena de um depósito de sulfetos, ou um zircão do qual só se conseguiu medir a composição de chumbo com confiança) tem uma razão radiogênica ²⁰⁷Pb*/²⁰⁶Pb* = 0,1800 (valor hipotético, já corrigido para chumbo comum). Usando ²³⁸U/²³⁵U = 137,818 (Hiess et al., 2012), qual é a idade Pb-Pb?

**Resolução.** A equação a resolver é:

$$0{,}1800 = \frac{1}{137{,}818}\cdot\frac{e^{\lambda_{235}t}-1}{e^{\lambda_{238}t}-1} \quad\Rightarrow\quad \frac{e^{\lambda_{235}t}-1}{e^{\lambda_{238}t}-1} = 0{,}1800 \times 137{,}818 \approx 24{,}807$$

Como não há solução algébrica direta, testa-se valores de t por tentativa. Vale fazer **uma** tentativa por extenso, porque as outras são a mesma conta com outro número e, sem ver uma inteira, o resto do exemplo vira uma lista de resultados que você não tem como conferir. Tomando t = 2,70 × 10⁹ anos:

$$\lambda_{235}t = 9{,}8485\times10^{-10}\times2{,}70\times10^{9} = 2{,}6591 \quad\Rightarrow\quad e^{2{,}6591}-1 \approx 13{,}283$$
$$\lambda_{238}t = 1{,}55125\times10^{-10}\times2{,}70\times10^{9} = 0{,}41884 \quad\Rightarrow\quad e^{0{,}41884}-1 \approx 0{,}52019$$
$$\frac{13{,}283}{0{,}52019} \approx 25{,}54$$

Esses 25,54 estão **acima** do alvo de 24,807, então 2,70 Ga é velho demais — a razão ²⁰⁷Pb*/²⁰⁶Pb* cresce monotonicamente com a idade, porque o ²³⁵U, de meia-vida muito mais curta, se esgotou mais cedo e deixou o ²⁰⁷Pb* acumulado mais cedo também. Repetindo a mesma conta para t = 2,60 × 10⁹ anos obtém-se 24,04 (baixo demais), o que encaixota a resposta entre 2,60 e 2,70 Ga. Refinando dentro desse intervalo, para t = 2,652 × 10⁹ anos o lado esquerdo dá aproximadamente 24,81 — muito próximo do alvo de 24,807. Portanto:

$$t \approx 2{,}652\times10^{9}\ \text{anos} \approx 2652\ \text{Ma} \approx 2{,}65\ \text{Ga}$$

**Interpretação.** A idade Pb-Pb de aproximadamente 2,65 Ga foi obtida **sem uma única medida de urânio** — apenas da razão entre dois isótopos radiogênicos de chumbo e do valor de referência ²³⁸U/²³⁵U. Esse tipo de cálculo, na prática profissional, é feito por software (que resolve a equação transcendental numericamente com muito mais casas decimais de precisão do que a tentativa manual aqui), mas o princípio — testar valores de t até que a razão prevista bata com a medida — é exatamente o que o software automatiza.

## Recap relâmpago

- O urânio tem dois isótopos radioativos relevantes, ²³⁸U (para ²⁰⁶Pb, λ = 1,55125×10⁻¹⁰/ano) e ²³⁵U (para ²⁰⁷Pb, λ = 9,8485×10⁻¹⁰/ano) — dois relógios independentes no mesmo mineral, com constantes de decaimento estabelecidas por Jaffey et al. (1971) e sem controvérsia relevante de recalibração.
- O **diagrama concórdia** plota ²⁰⁶Pb*/²³⁸U contra ²⁰⁷Pb*/²³⁵U; um ponto sobre a curva concórdia é uma análise **concordante**, confirmada por dois relógios independentes; um ponto abaixo da curva é **discordante**, tipicamente por perda de chumbo.
- Uma reta de **discórdia** ajustada a vários pontos discordantes de uma mesma população intercepta a concórdia em dois pontos: o intercepto superior dá a idade de cristalização original, o intercepto inferior dá a idade do evento de perda de chumbo (ou zero, se a perda foi recente e sem evento geológico distinto).
- O zircão domina a geocronologia U-Pb porque incorpora urânio e rejeita chumbo estruturalmente (filho inicial desprezível), resiste a intemperismo e metamorfismo (preservando idades em grãos detríticos) e cresce em zonas que registram eventos sucessivos, datáveis separadamente por SIMS ou LA-ICP-MS.
- A **idade Pb-Pb**, calculada só a partir da razão ²⁰⁷Pb*/²⁰⁶Pb* e do valor de referência ²³⁸U/²³⁵U = 137,818 (Hiess et al., 2012), dispensa a medida de urânio — útil para minerais ou minérios que perderam urânio, mas preservaram a razão entre os dois chumbos radiogênicos acumulados.

## Próxima aula

[[26-geologia-isotopica-aplicada-aula-06-isotopos-estaveis-aplicados|Aula 06 — Isótopos estáveis: notação delta, fracionamento, e aplicação a minérios e magmas]]: as duas últimas aulas do módulo deixam o terreno da geocronologia radiogênica e trocam a pergunta — a razão isotópica deixa de medir tempo e passa a medir processo. A Aula 06 monta a máquina (notação δ, fracionamento de equilíbrio e cinético) e a aplica ao enxofre em gênese de depósitos minerais e ao oxigênio em petrogênese; a [[26-geologia-isotopica-aplicada-aula-07-isotopos-estaveis-registro-ambiental|Aula 07]] a aplica ao ambiente — quimioestratigrafia, paleorredox e contaminação.

## Fontes

- Faure, G. & Mensing, T. M. (2005), *Isotopes: Principles and Applications*, 3ª ed., Wiley — capítulos 4 e 5 (sistema U-Pb, diagrama concórdia, discórdia, idade Pb-Pb, modelo Holmes-Houtermans).
- Dickin, A. P. (2005), *Radiogenic Isotope Geology*, 2ª ed., Cambridge University Press — capítulo 6 (U-Pb e Pb-Pb, geocronologia de zircão).
- Jaffey, A. H., Flynn, K. F., Glendenin, L. E., Bentley, W. C. & Essling, A. M. (1971), "Precision measurement of half-lives and specific activities of ²³⁵U and ²³⁸U", *Physical Review C*, 4(5), 1889-1906 — valores convencionais das constantes de decaimento λ238 e λ235, adotados pela IUGS. CONFERIDO na auditoria (2026-09-21): lista de autores, volume, fascículo e paginação confirmados. As meias-vidas medidas no artigo — (4,4683 ± 0,0024) × 10⁹ anos para o ²³⁸U e (7,0381 ± 0,0048) × 10⁸ anos para o ²³⁵U — reproduzem exatamente os λ usados nesta aula: ln2/4,4683×10⁹ = 1,55125 × 10⁻¹⁰ ano⁻¹ e ln2/7,0381×10⁸ = 9,84850 × 10⁻¹⁰ ano⁻¹.
- Wetherill, G. W. (1956), "Discordant uranium-lead ages, I", *Eos, Transactions American Geophysical Union*, 37(3), 320-326 (doi 10.1029/TR037i003p00320) — proposta original do diagrama concórdia. CONFERIDO na auditoria (2026-09-21): título, volume, fascículo e paginação confirmados; o nome atual do periódico é *Eos, Transactions American Geophysical Union*.
- Hiess, J., Condon, D. J., McLean, N. & Noble, S. R. (2012), "²³⁸U/²³⁵U systematics in terrestrial uranium-bearing minerals", *Science*, 335(6076), 1610-1614 — valor de consenso ²³⁸U/²³⁵U = 137,818 ± 0,045, revisando o valor histórico de 137,88. CONFERIDO na auditoria (2026-09-21).
- Ludwig, K. R. (2012), "Isoplot 3.75 — a geochronological toolkit for Microsoft Excel", *Berkeley Geochronology Center Special Publication* n. 5, 75 p. — software de referência para regressão de discórdias e cálculo de idades U-Pb. CONFERIDO na auditoria (2026-09-21): esta é a última versão publicada; a versão 3.00 anterior é *BGC Special Publication* n. 4 (2003).

<!--
nivel: avancado
palavras_corpo: 2325
palavras_corpo_metodo: "tokens separados por espaco entre '## Conteudo' e '## Fontes', incluindo LaTeX e tabelas (metodo declarado em 2026-09-22)."
duracao_estimada_min: 28

NOTA DE REVISAO DIDATICA (2026-09-22, revisor-didatico, modo review-and-fix):
  (a) ACHADO LARANJA DID-6b CORRIGIDO - salto no Exemplo trabalhado 2 (idade Pb-Pb por iteracao).
  O exemplo dizia 'Para t = 2,70e9 anos, o lado esquerdo calcula-se em aproximadamente 25,54' e
  seguia listando mais dois resultados, sem NUNCA mostrar uma tentativa por extenso. O aluno
  recebia tres numeros que nao tinha como reproduzir nem conferir, num exemplo cuja licao e
  justamente o metodo de tentativa - ou seja, o unico passo que importava ensinar era o unico
  omitido. CORRIGIDO expandindo a primeira tentativa (t = 2,70 Ga) em tres linhas: os dois
  expoentes, os dois e^x - 1 e o quociente. ARITMETICA VERIFICADA POR EXECUCAO EM PYTHON nesta
  revisao: lambda235*t = 2,659095 -> e^x - 1 = 13,2834; lambda238*t = 0,4188375 -> e^x - 1 =
  0,520193; quociente = 25,5354, que arredonda para os 25,54 ja publicados e ja auditados. Os
  valores para t = 2,60 Ga (24,0416) e t = 2,652 Ga (24,8054) tambem foram reconferidos e batem
  com o texto. Nenhum resultado novo - so o caminho ate os que ja estavam la.
  Foi acrescentada tambem a razao pela qual 25,54 acima do alvo significa 'velho demais' (a razao
  207Pb*/206Pb* cresce monotonicamente com a idade porque o 235U, de meia-vida mais curta,
  acumulou seu chumbo mais cedo), que o exemplo original deixava implicita e que e o que permite
  ao aluno escolher a direcao da proxima tentativa em vez de chutar. Isso decorre diretamente das
  duas constantes ja publicadas e auditadas na aula (lambda235 >> lambda238).
  (b) ACHADO AMARELO DID-12 CORRIGIDO - pre-requisitos declarados incompletos. O cabecalho
  declarava apenas as Aulas 03 e 04, mas o corpo se apoia explicitamente na Aula 01 ('aplicando a
  equacao geral da idade da Aula 01') e na Aula 02 (duas vezes: 'a mesma logica de filho inicial
  desprezivel do argonio na Aula 02' e 'ao contrario de uma medida K-Ar de mineral unico (Aula
  02)'). Corrigido para declarar as quatro, com a razao de cada uma.
  (c) Bloco 'Proxima aula' reescrito para apontar para as DUAS aulas finais, depois da divisao da
  Aula 06 (achado laranja DID-1); o texto anterior chamava a Aula 06 de 'a ultima aula do modulo'
  e anunciava paleoclimatologia, que nenhuma aula do modulo ensina (achado vermelho DID-2).

mapa_objetivo_secao:
  geologia-avancado-m26-oa02: "Dois relógios no mesmo mineral" + "O diagrama concórdia" + "A idade Pb-Pb" + "Exemplo trabalhado 1" + "Exemplo trabalhado 2"
  geologia-avancado-m26-oa03: "Discórdia: quando o sistema não ficou fechado" + "O que faz do zircão o mineral preferido"

alegacoes_auditaveis:
  - claim_id: ISOGEO-M26-A05-DOIS-DECAIMENTOS-U-001
    claim: "O 238U decai (por cadeia de decaimentos intermediarios de vida curta em equilibrio secular, tratada efetivamente como decaimento de um passo para fins de datacao) para 206Pb com lambda238=1,55125x10^-10/ano; o 235U decai para 207Pb com lambda235=9,8485x10^-10/ano; esses valores foram determinados por Jaffey et al. (1971) e adotados como convencao pela IUGS, sem controversia relevante de recalibracao nas ultimas decadas, ao contrario do 40K e, em menor grau, do 87Rb."
    risk: fato
    source: "Valores de Jaffey et al. (1971) sao convencao padrao amplamente replicada na literatura de geocronologia U-Pb (Faure & Mensing 2005, cap. 4-5; Dickin 2005, cap. 6); a ausencia de controversia relevante de recalibracao (em contraste com 40K e 87Rb, tratados nas Aulas 02 e 03) e observacao consolidada da area, nao verificada contra um levantamento sistematico especifico nesta redacao - risco considerado baixo pela consistencia entre multiplas fontes tercearias consultadas.
    CONFIRMADO PELA AUDITORIA (2026-09-21), com a cadeia numerica fechada ate a fonte primaria: Jaffey, A.H., Flynn, K.F., Glendenin, L.E., Bentley, W.C. & Essling, A.M. (1971), Physical Review C 4(5), 1889-1906, mediram atividade especifica de (746,19 +/- 0,41) desintegracoes/min por mg de 238U e (4798,1 +/- 3,3) por mg de 235U, correspondendo a meias-vidas de (4,4683 +/- 0,0024) x 10^9 anos e (7,0381 +/- 0,0048) x 10^8 anos. Conversao verificada por calculo: ln(2)/4,4683e9 = 1,551255e-10 /ano e ln(2)/7,0381e8 = 9,848499e-10 /ano, que arredondam EXATAMENTE para os 1,55125e-10 e 9,8485e-10 publicados na aula. Autoria completa, volume, fasciculo e paginacao verificados; a INCERTEZA DECLARADA quanto a paginacao esta RESOLVIDA. A literatura tambem descreve estes valores como o 'gold standard' da geocronologia U-Pb, corroborando a afirmacao de estabilidade da aula.
    ACHADO LARANJA 9 (auditoria 2026-09-21), claim ISOGEO-M26-A05-TH232-NAO-E-URANIO-009: o paragrafo abria com 'O uranio natural tem dois isotopos radioativos de meia-vida longa relevantes para geocronologia - 238U e 235U' e, tres linhas depois, dizia 'Um terceiro isotopo, 232Th, decai para 208Pb'. Lido em sequencia, 'um terceiro isotopo' se refere ao uranio, e o texto afirma implicitamente que o 232Th e um isotopo de uranio. FALSO: 232Th e isotopo de torio (Z=90), elemento distinto do uranio (Z=92). Corrigido para 'Um terceiro radionuclideo de vida longa produz chumbo do mesmo modo, mas ele NAO e um isotopo de uranio: o 232Th, isotopo de torio, decai para 208Pb'. Nota: a qualificacao original 'dois isotopos radioativos de MEIA-VIDA LONGA relevantes para geocronologia' esta correta e foi preservada - o uranio natural tem tambem o 234U, radioativo, mas de meia-vida curta (~245 ka) e membro da propria cadeia do 238U."
  - claim_id: ISOGEO-M26-A05-DIAGRAMA-CONCORDIA-002
    claim: "O diagrama concordia (diagrama de Wetherill, proposto por G.W. Wetherill em 1956) plota 206Pb*/238U (eixo y) contra 207Pb*/235U (eixo x); a curva concordia, gerada variando t nas duas equacoes de decaimento, nao e uma reta por causa da diferenca entre lambda238 e lambda235; um ponto medido sobre a curva e uma analise concordante (os dois relogios independentes concordam), um ponto abaixo da curva e discordante (tipicamente por perda de chumbo sem perda proporcional de uranio)."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-21) quanto ao conceito geral: resultado de busca confirma 'The most commonly used concordia diagrams are the Tera-Wasserburg diagram and the Wetherill diagram. The Wetherill diagram measures the 206Pb/238U and 207Pb/235U ratios against each other' e a definicao de pontos discordantes. Atribuicao a Wetherill (1956) e a data exata citadas de memoria. CONFIRMADO PELA AUDITORIA (2026-09-21) sem correcao necessaria: Wetherill, G.W. (1956), 'Discordant uranium-lead ages, I', Eos, Transactions American Geophysical Union 37(3), 320-326, doi 10.1029/TR037i003p00320 - ano, titulo (incluindo o sufixo ', I'), volume, fasciculo e paginacao todos corretos como citados. Unico ajuste: o nome do periodico e hoje indexado como 'Eos, Transactions American Geophysical Union', atualizado na lista de fontes. INCERTEZA DECLARADA RESOLVIDA."
  - claim_id: ISOGEO-M26-A05-DISCORDIA-INTERCEPTOS-003
    claim: "Uma reta de discordia ajustada a varios pontos discordantes de uma mesma populacao (mesma idade de cristalizacao original, perda de chumbo variavel por grao num evento posterior comum) intercepta a curva concordia em dois pontos: o intercepto superior corresponde a idade de cristalizacao original (t1), o intercepto inferior corresponde a idade do evento que causou a perda de chumbo (t2), podendo ser proximo de zero se a perda foi recente sem evento geologico distinto associavel."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-21): resultado de busca confirma 'The upper intercept with concordia represents the original igneous crystallization event at t1, and a lower intercept age represents t2, the time before the present at which Pb loss or overgrowth occurred' e que discordancia e comumente resultado de 'lead loss and/or uranium loss'."
  - claim_id: ISOGEO-M26-A05-ZIRCAO-PROPRIEDADES-004
    claim: "O zircao (ZrSiO4) domina a geocronologia U-Pb porque (1) incorpora uranio substituindo o zirconio na estrutura cristalina em quantidades apreciaveis mas exclui fortemente o chumbo (raio ionico e valencia incompativeis com o sitio do zirconio), tornando o chumbo comum inicial proximo de zero; (2) e quimica e mecanicamente muito resistente a intemperismo, transporte sedimentar e metamorfismo de grau baixo a medio, preservando idades originais em graos detriticos; (3) frequentemente cresce em zonas composicionais (visiveis por catodoluminescencia) que registram eventos sucessivos, dataveis separadamente por SIMS ou LA-ICP-MS."
    risk: fato
    source: "Conhecimento consolidado de geocronologia de zircao, amplamente documentado em Dickin (2005), Radiogenic Isotope Geology, cap. 6, e em literatura de proveniencia sedimentar e petrocronologia. Nao verificado contra fonte primaria unica nesta redacao - risco considerado baixo por ser descricao de propriedades mineralogicas bem estabelecidas e nao controversas."
  - claim_id: ISOGEO-M26-A05-U238-U235-RATIO-HIESS-005
    claim: "A razao natural 238U/235U, historicamente tratada como constante universal de valor 137,88, foi revisada por Hiess et al. (2012) para um valor medio de consenso de 137,818 +/- 0,045 (2 sigma) com base em analises de zircoes, mostrando que a razao varia tanto entre quanto dentro de amostras terrestres; a comunidade de geocronologia U-Pb adotou informalmente o valor de 137,818 como referencia pratica."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-21): resultado de busca confirma 'A value of 137.88 has previously been considered invariant... The U-Pb geochronology community has informally adopted the recommended value of 137.818 +/- 0.045 based on a single data set of 44 zircons by Hiess et al. (2012)', publicado em Science, 335(6076), 1610-1614 (identificado no resultado de busca via DOI science.1215507)."
  - claim_id: ISOGEO-M26-A05-EQUACAO-IDADE-PBPB-006
    claim: "A equacao da idade Pb-Pb, derivada dividindo a equacao de decaimento do 235U-207Pb pela do 238U-206Pb e introduzindo a razao natural 238U/235U, e 207Pb*/206Pb* = (1/137,818)*(e^(lambda235*t)-1)/(e^(lambda238*t)-1); e uma equacao transcendental em t, resolvida na pratica por iteracao numerica ou software especializado (p.ex. Isoplot); permite calcular idade sem nenhuma medida de uranio, util para materiais que perderam uranio mas preservaram a razao entre os dois isotopos radiogenicos de chumbo, incluindo o modelo de evolucao do chumbo terrestre de Holmes-Houtermans aplicado a depositos de sulfetos metalicos."
    risk: fato
    source: "Deducao matematica padrao a partir das duas equacoes de decaimento U-Pb; forma apresentada em Faure & Mensing (2005), cap. 4-5, e Dickin (2005), cap. 6. Atribuicao do modelo de evolucao do chumbo ao par Holmes-Houtermans e conhecimento consolidado de geocronologia de deposito mineral, nao verificado contra fonte primaria nesta redacao - risco considerado baixo por ser atribuicao historica amplamente replicada. Referencia de software agora completa e verificada pela auditoria (2026-09-21): Ludwig, K.R. (2012), 'Isoplot 3.75 - a geochronological toolkit for Microsoft Excel', Berkeley Geochronology Center Special Publication n. 5, 75 p. (a versao 3.00 anterior e a Special Publication n. 4, de 2003). INCERTEZA DECLARADA quanto a versao RESOLVIDA."
  - claim_id: ISOGEO-M26-A05-EXEMPLO1-CONCORDANTE-007
    claim: "Para 206Pb*/238U=0,5000 e lambda238=1,55125x10^-10/ano, t=ln(1,5)/1,55125x10^-10=0,405465/1,55125x10^-10=2,6138x10^9 anos (2613,8 Ma); nessa mesma idade, a equacao de 235U-207Pb preve 207Pb*/235U=e^(lambda235*t)-1=e^2,574-1=aproximadamente 12,12."
    risk: calculo
    source: "Aritmetica direta a partir das equacoes apresentadas nesta aula (verificada por calculo em Python nesta redacao: t=2613796023 anos, expoente lambda235*t=2,5742, razao 207/235=12,12). Dado de entrada (206Pb*/238U=0,5000) e hipotetico, construido para simplificar a aritmetica do exemplo pedagogico."
  - claim_id: ISOGEO-M26-A05-EXEMPLO2-PBPB-ITERACAO-008
    claim: "Para 207Pb*/206Pb*=0,1800 medido e 238U/235U=137,818, a razao alvo (e^(lambda235*t)-1)/(e^(lambda238*t)-1) e 0,1800*137,818=24,807; testando t=2,70x10^9 anos obtem-se ~25,54, testando t=2,60x10^9 anos obtem-se ~24,04, e testando t=2,652x10^9 anos obtem-se ~24,81, proximo do alvo, dando idade Pb-Pb aproximada de 2,652x10^9 anos (2652 Ma, ~2,65 Ga)."
    risk: calculo
    source: "Calculo iterativo verificado nesta redacao por execucao em Python: f(2.6e9)=24,04, f(2.65e9)=24,78, f(2.652e9)=24,805, f(2.66e9)=24,93, f(2.70e9)=25,54, confirmando convergencia proxima de t=2,652x10^9 anos para o alvo 24,807. Dado de entrada (207Pb*/206Pb*=0,1800) e hipotetico, construido para este exemplo pedagogico. REAUDITADO E CONFIRMADO (2026-09-21, execucao independente em Python pela auditoria): alvo 0,1800 x 137,818 = 24,80724; f(2,60e9)=24,0416; f(2,65e9)=24,7755; f(2,652e9)=24,8054; f(2,66e9)=24,9254; f(2,70e9)=25,5354; raiz exata por biseccao = 2.652.124.450 anos = 2652,12 Ma. Todos os cinco valores tabelados e a idade final de 2,652 Ga reproduzem. Exemplo 1 da mesma aula tambem reauditado: ln(1,5)=0,4054651, t=2.613.796.023 anos = 2613,8 Ma, lambda235*t=2,574197, 207Pb*/235U = e^2,574197 - 1 = 12,1208 -> 12,12 publicado. Nenhum erro aritmetico nesta aula."
-->
