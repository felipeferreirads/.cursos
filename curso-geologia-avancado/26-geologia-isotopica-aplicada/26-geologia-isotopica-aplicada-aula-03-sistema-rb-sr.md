# Aula 03: Sistema Rb-Sr — construção de diagramas isocrônicos e isótopos de Sr em petrogênese

**ID:** geologia-avancado-m26-a03
**Módulo:** [[26-geologia-isotopica-aplicada-modulo|Módulo 26 — Geologia isotópica aplicada]]
**Duração estimada:** ~28 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** resolver o problema do filho inicial não desprezível — que o método K-Ar contorna pela química do argônio, mas que o Rb-Sr não pode contornar da mesma forma — pela técnica da isócrona, e interpretar a razão inicial de estrôncio como traçador de fonte em petrogênese.
**Ao final você vai conseguir:** escrever a equação da isócrona Rb-Sr e explicar o significado geométrico de sua inclinação e de seu intercepto; calcular uma idade isocrônica a partir de dados de múltiplos minerais ou múltiplas rochas cogenéticas; e interpretar um valor de razão inicial ⁸⁷Sr/⁸⁶Sr em termos de fonte mantélica versus contaminação crustal.
**Pré-requisito:** [[26-geologia-isotopica-aplicada-aula-01-radioatividade-lei-decaimento-geocronologia-espectrometria-massa|Aula 01]] (equação geral da idade) e [[26-geologia-isotopica-aplicada-aula-02-metodos-k-ar-ar-ar|Aula 02]] (a ideia de que um sistema isotópico real raramente começa com filho zero).

## Conteúdo

### O problema que o K-Ar escapou e o Rb-Sr não escapa

No método K-Ar (Aula 02), a premissa de filho inicial desprezível se sustenta numa propriedade química conveniente: o argônio é um gás nobre, e um magma que está subindo e resfriando perde o argônio que contém antes de qualquer mineral cristalizar, de modo que ⁴⁰Ar inicial em um mineral ígneo recém-formado é, na prática, próximo de zero. O rubídio e o estrôncio não têm essa sorte. O ⁸⁷Rb decai por emissão beta negativa para **⁸⁷Sr**, mas o estrôncio é um elemento litófilo comum, que entra facilmente na estrutura cristalina de minerais como plagioclásio, apatita, biotita e K-feldspato **desde a cristalização** — e o estrôncio que entra já vem com sua própria mistura natural de isótopos, incluindo uma quantidade de ⁸⁷Sr que **não é** radiogênica, mas sim herdada da fonte do magma. Não há como, medindo um único mineral, separar quanto do ⁸⁷Sr presente é filho radiogênico acumulado desde a cristalização e quanto já estava lá desde o início. A equação geral da idade da Aula 01, sozinha, não resolve esse sistema — é preciso uma segunda ideia: a **isócrona**.

### Construindo a equação da isócrona

O estrôncio tem quatro isótopos estáveis naturais: ⁸⁴Sr, ⁸⁶Sr, ⁸⁷Sr e ⁸⁸Sr. Destes, ⁸⁶Sr não é produzido por nenhum decaimento radioativo relevante em escala geológica — funciona como uma referência estável, invariável, contra a qual se normalizam as razões medidas (a mesma lógica de normalizar uma medida bruta por um denominador não radiogênico aparece nos outros sistemas do módulo). Definindo P = ⁸⁷Rb, D* = ⁸⁷Sr radiogênico acumulado e usando ⁸⁶Sr como normalizador, a lei do decaimento da Aula 01, aplicada a uma **rocha ou mineral que preservou seu conteúdo original de ⁸⁷Sr** (D₀, o filho inicial, em vez de zero), dá:

$$\left(\frac{{}^{87}\text{Sr}}{{}^{86}\text{Sr}}\right)_{\text{hoje}} = \left(\frac{{}^{87}\text{Sr}}{{}^{86}\text{Sr}}\right)_{\text{inicial}} + \left(\frac{{}^{87}\text{Rb}}{{}^{86}\text{Sr}}\right)_{\text{hoje}}\left(e^{\lambda t}-1\right)$$

Essa é a **equação da isócrona**: uma equação linear em duas variáveis medidas hoje — ⁸⁷Sr/⁸⁶Sr (eixo y) e ⁸⁷Rb/⁸⁶Sr (eixo x) — com inclinação (e^λt − 1) e intercepto no eixo y igual a (⁸⁷Sr/⁸⁶Sr)_inicial. A chave conceitual é que essa equação não vale para uma única amostra isolada: ela vale para um **conjunto de amostras cogenéticas** — minerais separados de uma mesma rocha, ou rochas distintas de uma mesma suíte ígnea, ou fácies distintas de um mesmo corpo — que compartilham a mesma idade t e a mesma razão inicial (⁸⁷Sr/⁸⁶Sr)_inicial no momento da cristalização, mas que têm razões Rb/Sr **diferentes** (porque minerais diferentes incorporam rubídio e estrôncio em proporções diferentes: uma mica rica em K é rica em Rb e pobre em Sr, um plagioclásio cálcico é o oposto).

**Por que a técnica funciona.** Cada amostra do conjunto, plotada num gráfico ⁸⁷Rb/⁸⁶Sr (x) contra ⁸⁷Sr/⁸⁶Sr (y), cai sobre uma **reta**, porque todas compartilham o mesmo t e a mesma razão inicial — apenas a razão Rb/Sr de cada uma difere, o que as espalha ao longo do eixo x com posições y correspondentes previstas pela mesma equação linear. Ajustando uma reta de regressão a esse conjunto de pontos, obtém-se simultaneamente **dois** resultados que uma medida isolada jamais poderia entregar: a **inclinação**, da qual se extrai t (a idade, resolvendo e^λt − 1 = inclinação), e o **intercepto**, que é a própria razão inicial de estrôncio — um dado petrogenético valioso por si, discutido na próxima seção.

### Uma pausa antes de interpretar: qual λ usar, e por que a pergunta tem resposta

Antes de passar do cálculo para a interpretação petrogenética, uma pausa necessária — porque o exemplo trabalhado do fim desta aula precisa escolher um valor de λ, e a escolha não é indiferente.

O ⁸⁷Rb decai por emissão beta negativa com uma constante de decaimento cujo valor mais recente, recomendado pela força-tarefa conjunta IUPAC-IUGS "Isótopos em Geociências" em sua avaliação de 2015, é λ = (1,3972 ± 0,0045) × 10⁻¹¹ ano⁻¹, correspondendo a uma meia-vida de (49,61 ± 0,16) bilhões de anos. Esse valor é sensivelmente diferente do valor convencional mais antigo, de Steiger & Jäger (1977), de λ = 1,42 × 10⁻¹¹ ano⁻¹ (meia-vida próxima de 48,8 Ga) — uma diferença de cerca de 1,6%, pequena, mas não desprezível para trabalho de alta precisão, e o motivo pelo qual muitos problemas didáticos e boa parte da literatura mais antiga ainda usam o valor de 1977. Este exemplo é uma boa ilustração de um ponto geral do módulo: constantes de decaimento não são números gravados em pedra desde a descoberta da radioatividade — são valores medidos, com incerteza, refinados por gerações de metrologia nuclear, e **qual valor um trabalho publicado usa afeta, na segunda ou terceira casa decimal, a idade que ele relata**. Esta aula usa o valor clássico de Steiger & Jäger (1,42 × 10⁻¹¹ ano⁻¹) no exemplo numérico a seguir, por ser o mais comumente encontrado em problemas de geocronologia introdutória e intermediária, mas um trabalho de pesquisa atual deve declarar e, preferencialmente, usar a recomendação IUPAC-IUGS de 2015.

### A razão inicial de estrôncio como traçador de fonte

O valor do intercepto de uma isócrona — a razão (⁸⁷Sr/⁸⁶Sr)_inicial — não é só um subproduto do cálculo de idade: é, em si, um dos traçadores petrogenéticos mais usados em geologia ígnea, porque registra a composição isotópica do **reservatório de onde o magma se originou**, no momento da cristalização. A lógica é a seguinte:

- O manto terrestre tem, em média, uma razão Rb/Sr **baixa** (o rubídio é um elemento fortemente incompatível, que se concentra preferencialmente na crosta durante a diferenciação do planeta, deixando o manto empobrecido nele em relação ao estrôncio). Um reservatório com Rb/Sr baixo acumula ⁸⁷Sr radiogênico muito devagar ao longo do tempo geológico, de modo que magmas derivados diretamente do manto (basaltos de dorsal meso-oceânica, muitos basaltos de intraplaca) cristalizam com razões (⁸⁷Sr/⁸⁶Sr)_inicial **baixas**, tipicamente entre cerca de 0,702 e 0,706, dependendo do reservatório mantélico específico (manto empobrecido versus manto enriquecido).
- A crosta continental, ao contrário, acumulou Rb/Sr alto ao longo de bilhões de anos (o rubídio se concentra em rochas félsicas e em minerais de argila durante intemperismo e diferenciação crustal), de modo que rochas crustais antigas desenvolvem razões ⁸⁷Sr/⁸⁶Sr progressivamente **mais altas** com o tempo — muitas vezes bem acima de 0,710, podendo passar de 0,720 ou mais em terrenos continentais muito antigos e ricos em Rb.

Um magma que assimilou material crustal durante sua ascensão (um processo petrológico comum chamado **contaminação crustal** ou, no jargão da petrologia ígnea, AFC — *assimilation and fractional crystallization*) carrega essa assinatura crustal para sua razão inicial de estrôncio, deslocando-a para valores mais altos que os de um magma mantélico puro da mesma região. Por isso, comparar a razão inicial de ⁸⁷Sr/⁸⁶Sr de diferentes corpos ígneos de uma mesma província magmática é uma das ferramentas mais diretas para testar hipóteses de contaminação crustal versus fonte mantélica homogênea — um raciocínio que reaparece, com outro isótopo e outra notação, na discussão de εNd da Aula 04.

### Cuidado com o que uma isócrona bem ajustada não garante

Uma reta bem ajustada num diagrama Rb-Sr é uma condição necessária, mas não suficiente, para uma idade confiável. Duas armadilhas merecem menção:

- **Isócrona de mistura.** Se as amostras analisadas não são, na verdade, cogenéticas com uma única razão inicial comum, mas sim uma mistura em proporções variáveis de dois reservatórios distintos (por exemplo, um magma que se misturou com material crustal em graus diferentes ao longo de uma sequência de amostragem), os pontos também caem sobre uma reta — mas essa reta não tem significado de idade nenhum: é uma **linha de mistura de dois componentes**, e sua "inclinação" não corresponde a e^λt − 1 de coisa alguma. Distinguir uma isócrona verdadeira de uma linha de mistura exige evidência independente (petrográfica, geoquímica de elementos traço, ou um segundo sistema isotópico que deveria mostrar a mesma idade se a isócrona for real).
- **Rehomogeneização metamórfica.** Um evento metamórfico suficientemente intenso pode redistribuir estrôncio entre os minerais de uma rocha sem removê-lo do sistema como um todo — a chamada isócrona de rocha total ainda pode registrar a idade ígnea original mesmo que as isócronas internas de minerais individuais da mesma rocha tenham sido "reiniciadas" pelo metamorfismo e registrem, em vez disso, a idade do evento metamórfico. Essa é, de fato, uma ferramenta deliberada: comparar a isócrona de rocha total com a isócrona de minerais separados da mesma rocha pode, em conjunto, revelar tanto a idade ígnea quanto a idade de um evento metamórfico posterior.

## Exemplo trabalhado: construindo e resolvendo uma isócrona Rb-Sr

**Situação.** Quatro frações minerais separadas de um mesmo corpo granítico (dados hipotéticos, construídos para este exemplo) foram analisadas para Rb-Sr, com os seguintes resultados:

| Fração | ⁸⁷Rb/⁸⁶Sr | ⁸⁷Sr/⁸⁶Sr |
|---|---|---|
| A (plagioclásio) | 0,20 | 0,70800 |
| B (rocha total) | 0,80 | 0,70920 |
| C (K-feldspato) | 1,50 | 0,71070 |
| D (biotita) | 3,00 | 0,71370 |

Qual é a idade de cristalização do corpo granítico, e qual é sua razão inicial de estrôncio? Use λ = 1,42 × 10⁻¹¹ ano⁻¹ (Steiger & Jäger, 1977).

**Resolução — verificando a linearidade.** Antes de ajustar a reta, vale conferir se os pontos são, de fato, aproximadamente colineares, calculando a inclinação entre pares sucessivos:

- A→B: (0,70920 − 0,70800)/(0,80 − 0,20) = 0,00120/0,60 = 0,00200
- B→C: (0,71070 − 0,70920)/(1,50 − 0,80) = 0,00150/0,70 ≈ 0,00214
- C→D: (0,71370 − 0,71070)/(3,00 − 1,50) = 0,00300/1,50 = 0,00200

As três inclinações parciais são consistentes entre si (em torno de 0,0020, com uma pequena dispersão esperada de qualquer dado real), confirmando que os quatro pontos são compatíveis com uma única reta.

**Resolução — ajustando a reta.** Na prática profissional, a reta de uma isócrona se ajusta com um algoritmo que pondera cada ponto pelos seus erros analíticos — o mais usado na literatura é o de York (1968). Como este exemplo não traz barras de erro, o ajuste se reduz aos mínimos quadrados simples, que dá para acompanhar com calculadora na mão. Com x = ⁸⁷Rb/⁸⁶Sr e y = ⁸⁷Sr/⁸⁶Sr, as médias dos quatro pontos são x̄ = 1,375 e ȳ = 0,71040, e a reta depende de apenas duas somas:

$$S_{xx} = \sum(x_i-\bar{x})^2 = 4{,}3675 \qquad S_{xy} = \sum(x_i-\bar{x})(y_i-\bar{y}) = 0{,}008910$$

A inclinação é o quociente das duas, e o intercepto sai de impor que a reta passe pelo centro do conjunto (x̄, ȳ):

$$b = \frac{S_{xy}}{S_{xx}} = \frac{0{,}008910}{4{,}3675} \approx 0{,}002040 \qquad a = \bar{y} - b\,\bar{x} = 0{,}71040 - 0{,}002040\times1{,}375 \approx 0{,}70759$$

Note que a inclinação da reta de melhor ajuste **não** é a média aritmética das três inclinações parciais, que daria ≈0,00205: a regressão pondera cada ponto pela sua distância ao centro do conjunto, e os pontos extremos (A e D, os mais afastados em x) puxam a reta mais que os intermediários. A diferença entre as duas contas é pequena aqui, mas o hábito de nunca substituir um ajuste por uma média de inclinações parciais é o que evita que ela deixe de ser pequena em um conjunto pior distribuído.

**Resolução — idade.** A inclinação da isócrona é e^λt − 1:

$$e^{\lambda t} - 1 = 0{,}002040 \quad\Rightarrow\quad \lambda t = \ln(1{,}002040)$$

Calculando: ln(1,002040) ≈ 0,002038. Então:

$$t = \frac{0{,}002038}{1{,}42\times10^{-11}} \approx 1{,}435\times10^{8}\ \text{anos} \approx 143{,}5\ \text{milhões de anos}$$

**Resolução — razão inicial.** O intercepto da isócrona, 0,70759, é diretamente a razão (⁸⁷Sr/⁸⁶Sr)_inicial do granito no momento da cristalização.

**Interpretação.** O corpo granítico cristalizou há aproximadamente 143,5 milhões de anos — ou seja, no Jurássico Superior terminal (Titoniano), imediatamente acima do limite Jurássico-Cretáceo, hoje posicionado pela ICS em 143,1 ± 0,6 Ma. Repare que a incerteza analítica de uma isócrona real (tipicamente de 1 a 2%, aqui ±1,5 a ±3 Ma) é da mesma ordem da distância deste resultado ao limite: uma idade isotópica próxima de uma fronteira cronoestratigráfica raramente decide, por si só, de que lado dela o evento caiu. Sua razão inicial de 0,70759 é intermediária: mais alta que a faixa tipicamente mantélica (0,702–0,706), sugerindo que o magma que originou este granito não veio de uma fonte mantélica não contaminada, mas envolveu contribuição crustal significativa — seja por fusão parcial de crosta continental pré-existente, seja por assimilação de material crustal durante a ascensão do magma. Esse é exatamente o tipo de leitura petrogenética que só a técnica da isócrona, e não uma medida isolada de um único mineral, permite fazer.

## Recap relâmpago

- O rubídio e o estrôncio, ao contrário do argônio, entram normalmente na estrutura cristalina desde a cristalização; o ⁸⁷Sr inicial não é desprezível, e resolver a idade exige a **técnica da isócrona**, não a equação simples da idade da Aula 01.
- A equação da isócrona, (⁸⁷Sr/⁸⁶Sr)_hoje = (⁸⁷Sr/⁸⁶Sr)_inicial + (⁸⁷Rb/⁸⁶Sr)_hoje(e^λt − 1), é linear num diagrama ⁸⁷Rb/⁸⁶Sr vs. ⁸⁷Sr/⁸⁶Sr para um conjunto de amostras cogenéticas (mesma idade, mesma razão inicial, Rb/Sr diferente); a inclinação dá a idade e o intercepto dá a razão inicial.
- A constante de decaimento do ⁸⁷Rb tem valor clássico (Steiger & Jäger, 1977: 1,42 × 10⁻¹¹ ano⁻¹) e valor recomendado mais recente (IUPAC-IUGS, 2015: 1,3972 × 10⁻¹¹ ano⁻¹), diferindo cerca de 1,6% — outro lembrete de que a escolha de constante afeta o resultado publicado.
- A razão inicial ⁸⁷Sr/⁸⁶Sr é um traçador de fonte: valores baixos (≈0,702–0,706) indicam derivação de um reservatório mantélico com Rb/Sr historicamente baixo; valores mais altos indicam envolvimento de crosta continental (Rb/Sr alto, acumulado por bilhões de anos), por fusão parcial de crosta ou por contaminação de um magma mantélico durante a ascensão.
- Uma reta bem ajustada não é garantia automática de idade válida: pode ser uma **linha de mistura** de dois reservatórios sem significado temporal, e um evento metamórfico pode reiniciar isócronas minerais individuais preservando, ainda assim, a isócrona de rocha total.

## Próxima aula

[[26-geologia-isotopica-aplicada-aula-04-metodo-sm-nd|Aula 04 — Método Sm-Nd]]: um segundo sistema isocrônico, agora entre dois elementos terras-raras que fracionam menos entre si que Rb e Sr, com a notação εNd e o conceito de idade-modelo em relação ao manto empobrecido.

## Fontes

- Faure, G. & Mensing, T. M. (2005), *Isotopes: Principles and Applications*, 3ª ed., Wiley — capítulo 8 (sistema Rb-Sr, técnica da isócrona, razão inicial de estrôncio em petrogênese).
- Dickin, A. P. (2005), *Radiogenic Isotope Geology*, 2ª ed., Cambridge University Press — capítulo 3 (sistema Rb-Sr, incluindo isócronas de mistura e rehomogeneização metamórfica).
- Villa, I. M., De Bièvre, P., Holden, N. E. & Renne, P. R. (2015), "IUPAC-IUGS recommendation on the half life of ⁸⁷Rb", *Geochimica et Cosmochimica Acta*, 164, 382-385 (doi 10.1016/j.gca.2015.05.025) — "(49.61 ± 0.16) Ga for the half life of 87Rb, corresponding to a decay constant λ87 = (1.3972 ± 0.0045) × 10⁻¹¹ a⁻¹". CONFERIDO na auditoria (2026-09-21): lista de autores, volume e paginação confirmados.
- Steiger, R. H. & Jäger, E. (1977), "Subcommission on geochronology: convention on the use of decay constants in geo- and cosmochronology", *Earth and Planetary Science Letters*, 36(3), 359-362 — valor convencional λ = 1,42 × 10⁻¹¹ ano⁻¹ para o ⁸⁷Rb, usado no exemplo numérico desta aula. CONFERIDO na auditoria (2026-09-21).
- York, D. (1968), "Least squares fitting of a straight line with correlated errors", *Earth and Planetary Science Letters*, 5, 320-324 — algoritmo de regressão ponderada pelo erro analítico, padrão para ajuste de isócronas. CONFERIDO na auditoria (2026-09-21): o ano de publicação é **1968** (EPSL vol. 5, fascículo de dezembro de 1968), embora grande parte da literatura de geocronologia cite este trabalho como "York, 1969".
- International Commission on Stratigraphy, *International Chronostratigraphic Chart* — limite Jurássico-Cretáceo (base do Berriasiano) em 143,1 ± 0,6 Ma, usado na interpretação do exemplo trabalhado. Consultado na auditoria (2026-09-21).

<!--
nivel: avancado
palavras_corpo: 2323
palavras_corpo_metodo: "tokens separados por espaco entre '## Conteudo' e '## Fontes', incluindo LaTeX e tabelas (metodo declarado em 2026-09-22)."
duracao_estimada_min: 28

NOTA DE REVISAO DIDATICA (2026-09-22, revisor-didatico, modo review-and-fix):
  (a) ACHADO LARANJA DID-6 CORRIGIDO - salto no exemplo trabalhado. O exemplo verificava a
  colinearidade calculando tres inclinacoes parciais e, no passo seguinte, anunciava que 'uma
  regressao linear completa devolve uma inclinacao de aproximadamente 0,002040 e um intercepto de
  aproximadamente 0,70759' - dois numeros que o aluno nao tinha como obter nem conferir. Esse e o
  exemplo carro-chefe do modulo, e e precisamente onde a auditoria de 2026-09-21 encontrou o achado
  laranja 2 (a redacao havia publicado uma inclinacao 'estimada por inspecao'): um passo opaco e
  onde um erro se esconde. CORRIGIDO mostrando a conta de minimos quadrados por extenso - medias
  x=1,375 e y=0,71040, Sxx=4,3675, Sxy=0,008910, b=Sxy/Sxx e a=y-b*x. ARITMETICA VERIFICADA POR
  EXECUCAO EM PYTHON nesta revisao: b=0,00204007 e a=0,70759491, que arredondam exatamente para os
  0,002040 e 0,70759 ja publicados e ja auditados; ln(1,00204007)=0,00203799 e t=143,52 Ma,
  consistente com os 143,5 Ma publicados. Nao ha valor novo no texto - so o caminho ate os valores
  que ja estavam la. NOTA PARA A PROXIMA AUDITORIA: o registro do achado laranja 2 (claim
  ISOGEO-M26-A03-EXEMPLO-ISOCRONA-CALCULO-006, abaixo) anota inclinacao 0,0020395; o recalculo
  desta revisao da 0,0020401. A diferenca esta na sexta casa, nao muda nada arredondado a 0,002040
  nem a idade a uma casa decimal, e o valor PUBLICADO na aula esta correto nas duas contas - fica
  so registrado, sem abrir achado.
  Foi acrescentada tambem a observacao de que a inclinacao ajustada nao e a media das parciais
  (que daria 0,00205), que a auditoria ja havia pedido, agora com o numero explicito.
  (b) ACHADO AMARELO DID-8 CORRIGIDO - ordem interna. A secao sobre o valor numerico da constante
  de decaimento do 87Rb ficava encaixada entre a construcao da isocrona e a interpretacao
  petrogenetica, interrompendo o fio sem dizer por que. Ela PRECISA vir antes do exemplo (que
  escolhe um lambda), entao nao foi movida; recebeu titulo e frase de ponte que declaram ao leitor
  que e uma pausa deliberada e para que ela serve.
  (c) ACHADO AMARELO DID-10 CORRIGIDO - grafia 'uma mesma suice ignea' para 'suite ignea'. Erro de
  digitacao apontado pela auditoria de 2026-09-21 como observacao fora do escopo dela.

mapa_objetivo_secao:
  geologia-avancado-m26-oa02: "Construindo a equação da isócrona" + "O que o valor numérico da constante de decaimento revela" + "Exemplo trabalhado"
  geologia-avancado-m26-oa03: "A razão inicial de estrôncio como traçador de fonte" + "Cuidado com o que uma isócrona bem ajustada não garante" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: ISOGEO-M26-A03-PROBLEMA-FILHO-INICIAL-001
    claim: "Ao contrario do argonio (gas nobre, quimicamente inerte, expelido do magma antes da cristalizacao), o estroncio e um elemento litofilo comum que entra na estrutura cristalina de minerais (plagioclasio, apatita, biotita, K-feldspato) desde a cristalizacao, trazendo consigo isotopos de Sr nao radiogenicos herdados da fonte do magma; por isso o sistema Rb-Sr nao pode assumir filho inicial desprezivel como o K-Ar assume para o argonio."
    risk: fato
    source: "Principio quimico-mineralogico consolidado de geoquimica isotopica; ver Faure & Mensing (2005), Isotopes: Principles and Applications, 3a ed., Wiley, cap. 8, e Dickin, A.P. (2005), Radiogenic Isotope Geology, 2a ed., Cambridge University Press, cap. 3."
  - claim_id: ISOGEO-M26-A03-EQUACAO-ISOCRONA-002
    claim: "A equacao da isocrona Rb-Sr e (87Sr/86Sr)_hoje = (87Sr/86Sr)_inicial + (87Rb/86Sr)_hoje*(e^(lambda*t)-1), linear num diagrama 87Rb/86Sr (x) vs 87Sr/86Sr (y) para um conjunto de amostras cogeneticas que compartilham a mesma idade t e a mesma razao inicial mas tem razoes Rb/Sr diferentes; a inclinacao da reta ajustada e (e^(lambda*t)-1) e o intercepto no eixo y e a razao inicial (87Sr/86Sr)_inicial. 86Sr e usado como isotopo normalizador nao radiogenico."
    risk: fato
    source: "Deducao padrao da tecnica da isocrona, forma apresentada em qualquer texto-base de geocronologia; Faure & Mensing (2005), cap. 8; Dickin (2005), cap. 3."
  - claim_id: ISOGEO-M26-A03-RB87-DECAY-CONSTANT-IUPAC-003
    claim: "A forca-tarefa conjunta IUPAC-IUGS 'Isotopes in Geosciences', em avaliacao de 2015, recomenda um valor de (49,61 +/- 0,16) Ga para a meia-vida do 87Rb, correspondendo a uma constante de decaimento lambda = (1,3972 +/- 0,0045) x 10^-11 /ano; este valor difere de cerca de 1,6% do valor convencional mais antigo de Steiger & Jager (1977), lambda = 1,42x10^-11/ano (meia-vida ~48,8 Ga)."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-21): resultado de busca confirma 'The IUPAC-IUGS joint Task Group Isotopes in Geosciences recommends a value of (49.61 +/- 0.16) Ga for the half life of 87Rb, corresponding to a decay constant lambda87 = (1.3972 +/- 0.0045) x 10-11 a-1', em artigo publicado em Geochimica et Cosmochimica Acta (2015), identificado nos resultados de busca como ScienceDirect S0016703715003208. O calculo de diferenca percentual entre 1,42x10^-11 e 1,3972x10^-11 (~1,6%) e aritmetica direta desta redacao, RECONFERIDA pela auditoria: 1,6318%. Meias-vidas reconferidas: ln(2)/1,3972e-11 = 49,610 Ga e ln(2)/1,42e-11 = 48,813 Ga, ambas consistentes com o texto. CONFIRMADO PELA AUDITORIA (2026-09-21): Villa, I.M., De Bievre, P., Holden, N.E. & Renne, P.R. (2015), 'IUPAC-IUGS recommendation on the half life of 87Rb', Geochimica et Cosmochimica Acta 164, 382-385, doi 10.1016/j.gca.2015.05.025. Lista de autores, volume e paginacao verificados; a INCERTEZA DECLARADA esta RESOLVIDA. Valores parciais de Steiger & Jager (1977) tambem verificados na mesma auditoria (EPSL 36(3), 359-362, doi 10.1016/0012-821X(77)90060-7)."
  - claim_id: ISOGEO-M26-A03-RAZAO-INICIAL-TRACADOR-004
    claim: "O manto terrestre tem razao Rb/Sr media baixa (Rb e elemento fortemente incompativel, concentrado na crosta durante diferenciacao planetaria), de modo que magmas mantelicos (basaltos de dorsal meso-oceanica e muitos basaltos intraplaca) cristalizam com (87Sr/86Sr)_inicial tipicamente entre ~0,702 e 0,706; a crosta continental acumulou Rb/Sr alto ao longo do tempo geologico e desenvolve 87Sr/86Sr progressivamente mais alto, frequentemente acima de 0,710 e podendo exceder 0,720 em terrenos continentais antigos ricos em Rb. Contaminacao crustal de um magma mantelico desloca a razao inicial para valores mais altos que os de uma fonte mantelica pura da mesma regiao."
    risk: fato
    source: "Principio geoquimico consolidado de petrogenese e evolucao crustal, amplamente documentado em Faure & Mensing (2005), cap. 8, e em literatura de petrologia igneia sobre assimilacao e cristalizacao fracionada (AFC). Faixas numericas especificas (0,702-0,706 para manto, >0,710 a >0,720 para crosta antiga) sao ordens de grandeza consolidadas na literatura, mas os limites exatos podem variar por regiao e reservatorio - nao verificado contra uma fonte primaria unica nesta redacao para os limites numericos precisos; risco considerado baixo por serem faixas amplamente replicadas na literatura didatica."
  - claim_id: ISOGEO-M26-A03-ISOCRONA-MISTURA-METAMORFISMO-005
    claim: "Uma reta bem ajustada num diagrama Rb-Sr pode ser uma isocrona verdadeira de idade OU uma linha de mistura de dois reservatorios com composicoes distintas sem significado de idade nenhum; distinguir as duas exige evidencia independente. Um evento metamorfico pode redistribuir estroncio entre minerais de uma rocha (reiniciando isocronas de minerais individuais para a idade do metamorfismo) enquanto a isocrona de rocha total, formada por amostras de composicao global diferente mas nao homogeneizadas entre si, pode preservar a idade ignea original."
    risk: fato
    source: "Principio metodologico padrao de geocronologia Rb-Sr, discutido em Dickin, A.P. (2005), Radiogenic Isotope Geology, 2a ed., Cambridge University Press, cap. 3 (isocronas de mistura e efeitos de metamorfismo). Conhecimento consolidado da area, nao verificado contra pagina especifica nesta redacao."
  - claim_id: ISOGEO-M26-A03-EXEMPLO-ISOCRONA-CALCULO-006
    claim: "Para os quatro pontos hipoteticos (0,20;0,70800), (0,80;0,70920), (1,50;0,71070), (3,00;0,71370), as inclinacoes parciais entre pontos sucessivos sao aproximadamente 0,00200, 0,00214 e 0,00200, e a reta de melhor ajuste tem inclinacao 0,002040 e intercepto 0,70759; com lambda=1,42x10^-11/ano, ln(1,002040)=0,002038 e t=0,002038/1,42x10^-11=1,435x10^8 anos (143,5 milhoes de anos)."
    risk: calculo
    source: "Aritmetica direta a partir dos dados hipoteticos apresentados nesta aula, construidos especificamente para este exemplo pedagogico e nao correspondentes a uma rocha real.
    ACHADO LARANJA 2 (auditoria 2026-09-21), claim ISOGEO-M26-A03-EXEMPLO-ISOCRONA-CALCULO-006 (reaproveitado, mesmo alvo): a redacao publicou inclinacao 0,00201 e idade 141,4 Ma, valores que a propria metadados admitia terem sido 'estimados por inspecao dos quatro pontos'. Esses numeros NAO SAO a reta de melhor ajuste dos dados dados. Regressao por minimos quadrados recalculada pela auditoria (execucao em Python, 2026-09-21): n=4, Sxx=4,3675, Sxy=0,008910, inclinacao = 0,0020395, intercepto = 0,7075957. A INCLINACAO publicada estava errada em 1,5%; o INTERCEPTO publicado (0,70760) estava correto (arredondamento de 0,70759570). Idade correta: ln(1,0020395)=0,00203742, t=0,00203742/1,42e-11 = 1,4348e8 anos = 143,5 Ma. Residuos da reta ajustada: -2,9e-6, -2,7e-5, +4,5e-5, -1,5e-5, colinearidade confirmada. Corpo da aula corrigido para 0,002040 / 0,70759 / 143,5 Ma, e adicionada a nota de que a inclinacao ajustada nao e a media das inclinacoes parciais (a fonte provavel do erro original).
    CONSEQUENCIA GEOLOGICA PROPAGADA: a idade corrigida de 143,5 Ma cai no Jurassico Superior terminal (Titoniano, 149,2-143,1 Ma), NAO no 'Cretaceo Inferior' como a interpretacao original afirmava com base nos 141,4 Ma. Limite Jurassico-Cretaceo (base do Berriasiano) = 143,1 +/- 0,6 Ma pela International Chronostratigraphic Chart da ICS (consultada na auditoria, 2026-09-21; nao ha GSSP definido para a base do Berriasiano). Interpretacao reescrita, com a ressalva de que a incerteza analitica tipica de uma isocrona (1-2%, aqui +/-1,5 a 3 Ma) e da mesma ordem da distancia ao limite. Metodo de regressao ponderada: York, D. (1968) - ver achado amarelo 5 quanto ao ano."
  - claim_id: ISOGEO-M26-A03-YORK-ANO-007
    claim: "O algoritmo padrao de regressao de isocronas ponderada por erros correlacionados em x e y e o de York, publicado em 'Least squares fitting of a straight line with correlated errors', Earth and Planetary Science Letters, vol. 5, p. 320-324, com ano de publicacao 1968 - ainda que grande parte da literatura de geocronologia cite o trabalho como 'York, 1969'."
    risk: fato
    source: "ACHADO AMARELO 5 (auditoria 2026-09-21), levantado pela auditoria a partir da INCERTEZA DECLARADA da redacao, que pedia confirmacao de paginacao. A paginacao (EPSL 5, 320-324) estava CORRETA; o ANO estava errado. Verificado: NASA ADS indexa o artigo como 1968E&PSL...5..320Y e o identificador ScienceDirect e S0012821X68800597, ambos apontando 1968; o fasciculo de dezembro de 1968 do volume 5 da EPSL. Corrigido no corpo ('o mais usado na literatura e o de York, 1968') e na lista de fontes, preservando a mencao a forma 'York, 1969' porque o aluno vai encontrar essa citacao em artigos e manuais e precisa saber que se trata do mesmo trabalho. Nota: nao confundir com York, D. (1969), 'Least squares fitting of a straight line with correlated errors' - nao existe tal segundo artigo; a discrepancia e apenas de datacao do mesmo fasciculo."
-->
