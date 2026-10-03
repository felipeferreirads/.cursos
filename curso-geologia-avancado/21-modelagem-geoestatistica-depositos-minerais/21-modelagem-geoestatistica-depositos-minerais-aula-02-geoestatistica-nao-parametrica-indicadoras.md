# Aula 02: Geoestatística não paramétrica: variáveis contínuas, categóricas, booleanas e indicadoras

**ID:** geologia-avancado-m21-a02
**Módulo:** [[21-modelagem-geoestatistica-depositos-minerais-modulo|Módulo 21 — Modelagem geoestatística de depósitos minerais]]
**Duração estimada:** ~27 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** apresentar a transformação indicadora como a ferramenta central da geoestatística não paramétrica, mostrando por que ela dispensa hipóteses sobre a distribuição da variável e como se aplica a variáveis contínuas, categóricas e booleanas.
**Ao final você vai conseguir:** explicar o que a assimetria forte de fato compromete na krigagem ordinária de teores brutos (Módulo 20) — e o que ela **não** compromete —, e o que "não paramétrico" resolve nisso; definir a transformação indicadora para um limiar dado e calculá-la para um pequeno conjunto de dados; distinguir o uso da indicadora em variáveis contínuas (múltiplos limiares de teor), categóricas (domínio geológico) e booleanas (presença/ausência já binária); e descrever, em termos gerais, o que é um variograma indicador e por que se calcula um por limiar.
**Pré-requisito:** Aula 01 deste módulo (base de dados validada, modelo de blocos) e Módulo 20 completo, em especial a Aula 04 (variografia) e a Aula 05 (krigagem ordinária).

## Conteúdo

### O limite da krigagem ordinária de teores brutos

A krigagem ordinária do Módulo 20 estima o valor esperado de um bloco como combinação linear ponderada dos teores vizinhos — e, sozinha, ela responde bem a uma única pergunta: qual é o valor médio esperado? Ela não responde, ao menos não diretamente, a perguntas do tipo "qual é a probabilidade de este bloco ter teor acima do teor de corte econômico?" ou "qual é a incerteza sobre essa probabilidade, dado o padrão de amostragem local?". Essas perguntas de **decisão sob incerteza** — decidir se um bloco vai para a pilha de minério ou para o estéril, por exemplo — são exatamente o tipo de pergunta que domina a avaliação de recursos minerais, e a krigagem ordinária de teores brutos não foi desenhada para respondê-las diretamente.

Há um segundo problema, mais técnico — e aqui convém ser exato, porque circula uma versão errada dele. A dedução do sistema de krigagem ordinária **não assume distribuição alguma**: sob estacionariedade, a krigagem ordinária é o melhor estimador **linear** não viesado seja qual for a forma da distribuição, e normalidade nunca foi requisito para usá-la. O que a assimetria forte compromete é outra coisa, em duas frentes: a **robustez** — o variograma experimental e a própria estimativa ficam reféns de um punhado de valores muito altos — e a **otimalidade** — um estimador linear só coincide com a esperança condicional (que é o estimador ótimo, não só o melhor entre os lineares) sob a hipótese multigaussiana; longe dela, há informação na distribuição que a linearidade simplesmente deixa na mesa. Depósitos minerais frequentemente têm distribuições de teor fortemente **assimétricas** (positivamente enviesadas, com poucos valores muito altos puxando a cauda) — um padrão já visto no Módulo 20 como motivo para capear valores extremos de alto teor antes da composição. Um único variograma, calculado sobre a variável bruta, tende a ser dominado por essa cauda e pode descrever mal a continuidade espacial da maior parte dos dados (os valores baixos e médios, que formam o grosso da massa de minério).

A **geoestatística não paramétrica** responde às duas questões ao mesmo tempo, com uma única ferramenta: transformar a variável contínua original numa (ou várias) variável(is) **binária(s)**, cuja distribuição é, por construção, sempre a mesma — não importa a forma da distribuição original — e cujo valor esperado, estimado por krigagem, *é* diretamente uma probabilidade.

### A transformação indicadora

Dado um limiar (também chamado de **corte** ou *cutoff*) $z_c$, a **transformação indicadora** de uma variável contínua $Z$ num ponto $x$ é definida como:

$$I(x; z_c) = \begin{cases} 1 & \text{se } z(x) \le z_c \\ 0 & \text{se } z(x) > z_c \end{cases}$$

(a convenção do sinal — $\le$ versus $>$ — varia entre autores; o que importa é usar a mesma convenção de forma consistente do início ao fim do exercício.) O resultado é uma variável que só assume dois valores, 0 ou 1, para cada amostra, em cada limiar escolhido. A propriedade central que torna essa transformação útil é: **o valor esperado da indicadora, $E[I(x;z_c)]$, é exatamente a probabilidade de o valor de $Z$ em $x$ ser menor ou igual a $z_c$** — ou seja, é o valor da função de distribuição acumulada de $Z$ avaliada em $z_c$, $F(z_c)$. Essa não é uma aproximação: é uma consequência direta da definição de valor esperado de uma variável de Bernoulli. É esse fato que conecta a krigagem (que estima valores esperados) à estimativa de probabilidades: **krigar a indicadora estima a probabilidade acumulada**, não o teor.

Na prática, uma única indicadora e um único limiar respondem a uma pergunta binária ("este bloco está abaixo ou acima do teor de corte?"). Para descrever a distribuição inteira de um bloco — não só um ponto de corte — usa-se um **conjunto de limiares** (tipicamente entre 5 e 15, escolhidos nos percentis da distribuição global dos dados: decis, por exemplo), cada um gerando sua própria variável indicadora e, na Aula 03, seu próprio variograma. O conjunto de estimativas de $F(z_c)$ nesses vários limiares reconstrói, ponto a ponto, uma aproximação discreta da **função de distribuição acumulada local** (*local ccdf*, distribuição condicional aos dados vizinhos) — a peça central da geoestatística não paramétrica, montada ponto a ponto na Aula 04.

### Variáveis contínuas, categóricas e booleanas: três usos da mesma ferramenta

A transformação indicadora não se restringe a teores; ela se aplica a três tipos de variável de forma distinta, e é importante não confundir os três:

**Variável contínua** (teor de um elemento, densidade, espessura de um corpo): esse é o caso descrito acima — vários limiares ao longo do intervalo de valores possíveis, cada um definindo uma indicadora diferente. É o caso que motiva o uso de múltiplos limiares e a reconstrução de uma distribuição local completa.

**Variável categórica** (litologia, tipo de alteração, domínio geológico/estrutural): aqui a variável já não é ordenada num eixo contínuo — "granito" não é "maior" ou "menor" que "xisto". A indicadora, nesse caso, marca a **pertença a uma categoria específica**: $I(x; \text{categoria } k) = 1$ se a amostra em $x$ pertence à categoria $k$, e $0$ caso contrário — uma indicadora por categoria, sem noção de limiar ou ordem. Krigar essa indicadora estima a **probabilidade local de pertencer àquela categoria** — por exemplo, a probabilidade de um bloco não amostrado estar dentro do domínio de minério oxidado versus sulfetado. Essa é, de fato, uma das aplicações mais diretas da krigagem de indicadoras em modelagem de depósitos: gerar mapas de probabilidade de domínio geológico a partir de furos onde a litologia foi logada categoricamente.

**Variável booleana** (presença/ausência de mineralização visível, presença de uma estrutura, um teste sim/não): essa variável já nasce como 0 ou 1 — não precisa de transformação, porque ela **é** a própria indicadora. Krigar uma variável booleana diretamente já produz uma estimativa de probabilidade, pelo mesmo argumento do valor esperado de uma Bernoulli. O ponto prático de distinguir esse caso dos outros dois é só terminológico: não existe "limiar" a escolher, porque a variável já é binária por definição do fenômeno observado, não por uma transformação aplicada pelo geólogo.

Os três casos compartilham a mesma matemática de estimativa (uma krigagem de uma variável 0/1, cujo resultado é interpretado como probabilidade), mas diferem na origem da variável 0/1: **corte de um contínuo** (variável contínua), **pertença** (categórica) ou **observação direta** (booleana).

### Por que se calcula um variograma por limiar (prévia da Aula 03)

Uma consequência importante — e um ponto onde a intuição vinda da krigagem ordinária do Módulo 20 pode enganar — é que **cada limiar tem, em princípio, seu próprio variograma indicador**, e esses variogramas podem ter alcances e formas diferentes entre si. Isso faz sentido geologicamente: a continuidade espacial de "estar acima do teor de corte de minério de alto teor" pode ser bem menor (feições de alto teor tendem a ser mais localizadas, associadas a estruturas específicas) do que a continuidade espacial de "estar acima de um teor de corte muito baixo, perto do teor médio do depósito" (que descreve, essencialmente, os limites do próprio corpo mineralizado, tipicamente mais contínuos). Essa dependência do variograma em relação ao limiar é o que a Aula 03 vai formalizar e usar — por ora, o ponto a reter é que a transformação indicadora não é só um truque estatístico: ela expõe uma informação geológica (como a continuidade espacial muda com o teor) que um único variograma de teores brutos, no Módulo 20, não conseguia separar.

## Exemplo trabalhado

**Situação:** cinco amostras de um furo de sondagem têm os seguintes teores de cobre (Cu, %): $z_1=0,25$; $z_2=0,80$; $z_3=1,50$; $z_4=0,60$; $z_5=2,10$.

**Pergunta:** calcule a transformação indicadora dessas cinco amostras para dois limiares — o teor de corte econômico $z_c=0,50\%$ e um limiar mais alto, $z_c=1,80\%$ — e interprete o que cada conjunto de indicadoras estima.

**Resolução:**

Usando a convenção $I(x;z_c)=1$ se $z(x)\le z_c$, $0$ caso contrário:

| Amostra | $z$ (%) | $I(z_c=0,50)$ | $I(z_c=1,80)$ |
|---|---|---|---|
| 1 | 0,25 | 1 | 1 |
| 2 | 0,80 | 0 | 1 |
| 3 | 1,50 | 0 | 1 |
| 4 | 0,60 | 0 | 1 |
| 5 | 2,10 | 0 | 0 |

Para o limiar $z_c=0,50\%$: apenas a amostra 1 (0,25%) está abaixo do corte; a média amostral das indicadoras é $1/5=0,20$ — uma estimativa (não ponderada espacialmente, apenas descritiva) de que 20% das amostras do furo estão abaixo do teor de corte econômico, ou seja, 80% estão em minério de teor igual ou superior ao corte.

Para o limiar $z_c=1,80\%$: quatro das cinco amostras (todas exceto a amostra 5, com 2,10%) estão abaixo desse limiar; a média amostral das indicadoras é $4/5=0,80$.

**Leitura dos resultados:** o mesmo conjunto de cinco teores gera duas variáveis indicadoras completamente diferentes, dependendo do limiar escolhido — e, embora este exemplo use só a média amostral simples (sem ponderação espacial), o mesmo princípio vale para a krigagem indicadora da Aula 04: uma krigagem no limiar $0,50\%$ estima a probabilidade local de estar abaixo do teor de corte econômico; uma krigagem no limiar $1,80\%$ estima a probabilidade local de estar abaixo de um teor bem mais alto — duas perguntas diferentes, cada uma respondida por sua própria variável indicadora e, na prática, por seu próprio variograma.

## Recap relâmpago

- A krigagem ordinária de teores brutos (Módulo 20) estima um valor esperado, não uma probabilidade. Sua dedução **não** assume distribuição alguma — ela é o melhor estimador *linear* não viesado sob estacionariedade —, mas sob assimetria forte perde **robustez** (refém de poucos valores altos) e **otimalidade** (só sob multigaussianidade um estimador linear iguala a esperança condicional). A **geoestatística não paramétrica** responde às duas limitações transformando a variável numa (ou várias) variável(is) binária(s).
- A **transformação indicadora** $I(x;z_c)=1$ se $z(x)\le z_c$, $0$ caso contrário, tem a propriedade central de que seu valor esperado é a **probabilidade acumulada** $F(z_c)$ — krigar a indicadora estima uma probabilidade, não um teor.
- Usa-se um **conjunto de limiares** (não um só) para reconstruir, ponto a ponto, uma aproximação da distribuição de probabilidade local completa (função de distribuição acumulada local, *local ccdf*) — a peça que a Aula 04 monta.
- A mesma ferramenta serve para três tipos de variável: **contínua** (indicadora por limiar de teor), **categórica** (indicadora de pertença a um domínio/litologia, sem noção de ordem), e **booleana** (a variável já é a própria indicadora, sem transformação).
- Cada limiar pode ter seu **próprio variograma indicador**, com alcance e forma diferentes — essa dependência do variograma em relação ao limiar carrega informação geológica real (a continuidade espacial de alto teor costuma ser menor do que a do corpo mineralizado como um todo) e é o assunto da Aula 03.

## Próxima aula

Aula 03 — Variograma indicador: cálculo, modelos autorizados e escolha da abordagem. Com a transformação indicadora definida, a próxima aula formaliza como calcular e modelar o variograma de cada indicadora e como escolher, com evidência, entre ajustar um variograma por limiar (*full IK*) e usar um único variograma de referência (*median IK*).

Ela abre um **par de aulas**: a Aula 04 completa o assunto resolvendo o sistema de krigagem indicadora, combinando as estimativas de vários limiares numa distribuição local e tratando o problema prático das **violações de relação de ordem**, mencionado no ponto de dificuldade do módulo.

## Fontes

- Journel, A. G. (1983), "Nonparametric estimation of spatial distributions", *Mathematical Geology*, 15(3), 445–468 — artigo fundador da abordagem de krigagem de indicadoras.
- Isaaks, E. H. & Srivastava, R. M. (1989), *An Introduction to Applied Geostatistics*, Oxford University Press, capítulo 18, *Estimating a Distribution* (geoestatística não paramétrica: transformação indicadora, propriedade do valor esperado como probabilidade acumulada).
- Goovaerts, P. (1997), *Geostatistics for Natural Resources Evaluation*, Oxford University Press, capítulo 7, *Assessment of Local Uncertainty* (modelagem não paramétrica da incerteza local: indicadoras contínuas e categóricas).
- Sinclair, A. J. & Blackwell, G. H. (2002), *Applied Mineral Inventory Estimation*, Cambridge University Press, capítulo 8 (aplicação de indicadoras a domínios geológicos categóricos em depósitos minerais).

<!--
nivel: avancado
palavras_corpo: 1790
mapa_objetivo_secao:
  geologia-avancado-m21-oa02: "O limite da krigagem ordinária de teores brutos" + "A transformação indicadora" + "Variáveis contínuas, categóricas e booleanas: três usos da mesma ferramenta" + "Por que se calcula um variograma por limiar (prévia da Aula 03)" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOMOD-M21-A02-DEFINICAOINDICADORA-001
    claim: "A transformação indicadora de uma variável contínua Z num limiar z_c é definida como I(x;z_c)=1 se z(x)<=z_c e 0 caso contrário (convenção de sinal podendo ser invertida por autor, desde que aplicada consistentemente); seu valor esperado E[I(x;z_c)] é, por definição de valor esperado de uma variável de Bernoulli, exatamente a probabilidade acumulada F(z_c) = P(Z(x)<=z_c) — logo, krigar a indicadora estima uma probabilidade acumulada, não o teor em si."
    risk: fato
    source: "Journel, A. G. (1983), 'Nonparametric estimation of spatial distributions', Mathematical Geology, 15(3), 445-468; Isaaks & Srivastava (1989), An Introduction to Applied Geostatistics, Oxford University Press, capítulo 18 (Estimating a Distribution)."
  - claim_id: GEOMOD-M21-A02-MULTIPLOSLIMIARES-002
    claim: "Para reconstruir uma aproximação discreta da função de distribuição acumulada local (ccdf local, condicional aos dados vizinhos) de uma variável contínua, usa-se um conjunto de múltiplos limiares (tipicamente entre 5 e 15, com escolha usual nos percentis/decis da distribuição global dos dados), cada um gerando sua própria variável indicadora."
    risk: fato
    source: "Isaaks & Srivastava (1989), capítulo 18 (Estimating a Distribution) (reconstrução da ccdf local a partir de múltiplos limiares indicadores); Goovaerts (1997), Geostatistics for Natural Resources Evaluation, Oxford University Press, capítulo 7 (Assessment of Local Uncertainty)."
  - claim_id: GEOMOD-M21-A02-VARIAVELCATEGORICA-003
    claim: "Para uma variável categórica (ex.: litologia, domínio geológico), a indicadora marca pertença a uma categoria específica k, I(x;categoria k)=1 se a amostra pertence à categoria k e 0 caso contrário, sem noção de ordem ou limiar entre categorias; krigar essa indicadora estima a probabilidade local de pertencer àquela categoria, permitindo gerar mapas de probabilidade de domínio geológico a partir de logs categóricos de furos de sondagem."
    risk: fato
    source: "Goovaerts (1997), Geostatistics for Natural Resources Evaluation, capítulo 7 (Assessment of Local Uncertainty) (indicadoras categóricas); Sinclair & Blackwell (2002), Applied Mineral Inventory Estimation, Cambridge University Press, capítulo 8 (aplicação a domínios geológicos em mineração)."
  - claim_id: GEOMOD-M21-A02-VARIAVELBOOLEANA-004
    claim: "Uma variável booleana (ex.: presença/ausência de mineralização visível, de uma estrutura) já é, por definição do fenômeno observado, uma variável 0/1, sem necessidade de transformação por limiar; krigá-la diretamente já produz uma estimativa de probabilidade local, pelo mesmo argumento de valor esperado de uma variável de Bernoulli aplicado às indicadoras contínuas e categóricas."
    risk: fato
    source: "Goovaerts (1997), Geostatistics for Natural Resources Evaluation, capítulo 7 (Assessment of Local Uncertainty); Isaaks & Srivastava (1989), capítulo 18 (Estimating a Distribution)."
  - claim_id: GEOMOD-M21-A02-VARIOGRAMAPORLIMIAR-005
    claim: "Cada limiar de uma variável contínua pode, em princípio, ter um variograma indicador diferente (alcance e forma podem variar com o limiar) — um padrão de interesse geológico direto, já que limiares de teor mais alto (mineralização de alto teor, tipicamente mais localizada/estrutural) tendem a apresentar alcances menores do que limiares baixos, próximos ao teor médio do depósito, que aproximam os limites do próprio corpo mineralizado."
    risk: fato
    source: "Journel, A. G. (1983), Mathematical Geology, 15(3); Isaaks & Srivastava (1989), capítulo 18 (Estimating a Distribution) (variação do variograma indicador com o limiar, 'efeito de destriagem'/sill relativo)."
  - claim_id: GEOMOD-M21-A02-OKSEMHIPOTESEDISTRIBUCIONAL-006
    claim: "A deducao do sistema de krigagem ordinaria nao assume distribuicao alguma: sob estacionariedade, a KO e o melhor estimador LINEAR nao viesado qualquer que seja a forma da distribuicao, e normalidade nunca foi requisito. O que a assimetria forte compromete sao (i) a robustez — variograma experimental e estimativa ficam sensiveis a poucos valores muito altos — e (ii) a otimalidade — um estimador linear so coincide com a esperanca condicional (estimador otimo) sob a hipotese multigaussiana."
    risk: fato
    source: "Chilès & Delfiner (2012), Geostatistics: Modeling Spatial Uncertainty, 2ª ed., Wiley, cap. 3 (a krigagem como BLUE, sem hipótese distribucional); Goovaerts (1997), capítulo 7 (Assessment of Local Uncertainty) (multigaussianidade e esperança condicional); Journel & Huijbregts (1978), Mining Geostatistics, capítulo V."
    revisao: "2026-09-18 — alegação nova, criada pela auditoria (🟠 2). A versão anterior da aula afirmava que a krigagem ordinária 'depende implicitamente de a distribuição não ser demasiado assimétrica', o que é a versão mnemônica errada de uma afirmação certa: a KO não assume distribuição, o que a assimetria ataca é robustez e otimalidade."
-->
