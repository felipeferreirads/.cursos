# Aula 02: Decaimento radioativo e datação radiométrica

**ID:** geologia-gemologia-m03-a02
**Módulo:** [[03-tempo-geologico-geocronologia-modulo|Módulo 03 — Tempo geológico e geocronologia]]
**Duração estimada:** ~30 min
**Objetivo:** entender o relógio físico embutido em átomos instáveis — por que o decaimento radioativo é previsível mesmo sendo aleatório em cada átomo individual — e aprender a calcular uma idade numérica a partir dele.
**Pré-requisito:** [[03-tempo-geologico-geocronologia-aula-01-datacao-relativa-e-discordancias|Aula 01]] (datação relativa; a ordem que a datação absoluta vai agora calibrar em números).

## Ao final você vai conseguir

- [OA-02a] Explicar o mecanismo do decaimento radioativo e por que ele é estatisticamente previsível em escala populacional apesar de ser aleatório em cada átomo.
- [OA-02b] Definir meia-vida e constante de decaimento, e aplicar a equação de decaimento para calcular uma idade a partir de uma razão pai/filha.
- [OA-02c] Identificar os principais sistemas isotópicos usados em geocronologia (U-Pb, K-Ar/Ar-Ar, Rb-Sr, Sm-Nd, C-14) e o intervalo de idades e materiais para os quais cada um é adequado.
- [OA-02d] Explicar o conceito de temperatura de fechamento e por que uma "idade radiométrica" data um evento específico do mineral, não necessariamente a idade da rocha inteira.

## Conteúdo

### Por que o núcleo atômico funciona como relógio

Alguns isótopos — versões de um elemento com número diferente de nêutrons no núcleo — são **instáveis**: o núcleo tem excesso de energia e, em algum momento, se reorganiza espontaneamente para um estado mais estável, emitindo partículas e/ou radiação nesse processo. Esse fenômeno é o **decaimento radioativo**, e o isótopo original é chamado de **isótopo-pai**; o produto resultante, de **isótopo-filho**.

O ponto que torna esse fenômeno útil como relógio é sutil e vale isolar: **para um único átomo, é impossível prever quando ele vai decair** — o processo é governado pela mecânica quântica e é fundamentalmente probabilístico, sem "gatilho" externo (não depende de temperatura, pressão ou reações químicas, ao contrário de quase todo processo geológico usado para datação relativa). Mas, para uma **população muito grande de átomos** do mesmo isótopo — e uma amostra mineral typical contém números da ordem de 10²⁰ átomos ou mais — a estatística se torna extremamente previsível: **uma fração fixa e constante da população decai por unidade de tempo**, sempre a mesma fração, não importa quantos átomos já decaíram antes. Essa é a analogia útil: não é possível prever quando um grão de pipoca específico vai estourar, mas se metade de uma panela sempre estoura em exatamente 90 segundos, esse tempo fixo (a meia-vida) permite calcular há quanto tempo o fogo foi aceso, mesmo sem ter cronometrado o início.

### Meia-vida, constante de decaimento e a equação

A **meia-vida** (t₁/₂) é o tempo necessário para que **metade** dos átomos-pai de uma amostra decaia para átomo-filho. É uma propriedade fixa de cada isótopo — não muda com temperatura, pressão, estado químico ou qualquer condição ambiental (diferença crucial frente a processos como decomposição orgânica ou reações químicas comuns, que aceleram ou desaceleram com a temperatura).

Matematicamente, o decaimento radioativo segue uma **lei exponencial**:

N(t) = N₀ · e^(−λt)

onde N₀ é o número de átomos-pai no início, N(t) é o número de átomos-pai remanescentes depois de um tempo t, e **λ** (lambda) é a **constante de decaimento** — a probabilidade de decaimento por átomo por unidade de tempo, uma constante própria de cada isótopo. Meia-vida e constante de decaimento se relacionam por:

t₁/₂ = ln(2) / λ ≈ 0,693 / λ

Para efeitos de datação, a forma mais útil da equação reescreve o número de átomos-filho acumulados (D, de *daughter*) em função da razão pai/filha medida hoje:

t = (1/λ) · ln(1 + D/N)

onde D é a quantidade de isótopo-filho radiogênico (produzido pelo decaimento, não presente originalmente) e N é a quantidade de isótopo-pai remanescente, ambos medidos na amostra hoje por espectrometria de massa. Repare que a idade não exige saber quantos átomos-pai existiam no início — só a razão *atual* entre o que sobrou e o que se acumulou, o que é medível diretamente.

Uma consequência prática importante: depois de **uma** meia-vida, resta 50% do isótopo-pai original; depois de **duas**, resta 25%; depois de **dez**, resta menos de 0,1%. Isso significa que cada sistema isotópico tem uma **janela útil de idades**: um isótopo de meia-vida muito curta esgota o pai rápido demais para datar rochas antigas (o sinal desaparece no ruído de medição); um isótopo de meia-vida muito longa produz pouquíssimo filho em rochas jovens para ser medido com precisão. É por isso que a geocronologia usa **sistemas isotópicos diferentes para faixas de idade diferentes** — não existe um único cronômetro universal.

### Os principais sistemas isotópicos

- **Urânio-chumbo (U-Pb).** Dois decaimentos paralelos e independentes no mesmo mineral: ²³⁸U decai para ²⁰⁶Pb (meia-vida ≈ 4,47 bilhões de anos) e ²³⁵U decai para ²⁰⁷Pb (meia-vida ≈ 704 milhões de anos). Aplicado classicamente ao mineral **zircão** (ZrSiO₄), que incorpora urânio na sua estrutura cristalina ao se formar mas **rejeita chumbo** — de modo que praticamente todo o chumbo encontrado num zircão é radiogênico, sem "chumbo comum" herdado para complicar a conta. O zircão também é notavelmente resistente ao intemperismo e ao metamorfismo, o que preserva a idade original mesmo em rochas que passaram por eventos geológicos posteriores. Por ter dois relógios independentes no mesmo cristal, o método permite um teste interno de consistência (o diagrama concórdia-discórdia, mencionado adiante). É o método mais usado para datar rochas ígneas e metamórficas antigas, incluindo os zircões mais velhos já encontrados na Terra, com idades próximas de 4,4 bilhões de anos.
- **Potássio-argônio (K-Ar) e argônio-argônio (⁴⁰Ar/³⁹Ar).** ⁴⁰K decai para ⁴⁰Ar (meia-vida ≈ 1,25 bilhão de anos), aplicável a minerais ricos em potássio (micas, feldspato potássico, hornblenda) e a rochas vulcânicas inteiras (whole-rock). O método clássico K-Ar mede potássio e argônio separadamente, o que introduz incerteza se a amostra não for homogênea; a variante moderna **⁴⁰Ar/³⁹Ar** irradia a amostra com nêutrons para converter uma fração do ³⁹K em ³⁹Ar, permitindo medir a razão ⁴⁰Ar/³⁹Ar num único espectrômetro e, com aquecimento em etapas (*step-heating*), obter um espectro de idades que revela se a amostra sofreu perda parcial de argônio depois de sua formação. Cobre desde o Quaternário até o Precambriano.
- **Rubídio-estrôncio (Rb-Sr).** ⁸⁷Rb decai para ⁸⁷Sr (meia-vida ≈ 48,8 bilhões de anos — muito longa, por isso mais útil em rochas antigas). Aplicado sobretudo pelo **método da isócrona**: em vez de datar um único mineral, mede-se a razão ⁸⁷Rb/⁸⁶Sr e ⁸⁷Sr/⁸⁶Sr em vários minerais coexistentes de uma mesma rocha (que cristalizaram ao mesmo tempo, a partir do mesmo magma, com a mesma razão inicial de estrôncio, mas com proporções diferentes de rubídio incorporado em cada mineral). Plotados num gráfico, esses pontos se alinham numa reta — a **isócrona** — cuja inclinação dá diretamente a idade, e cujo intercepto no eixo Y dá a razão isotópica inicial de estrôncio (informação sobre a fonte do magma). A vantagem do método de isócrona, generalizável a outros sistemas, é que ele não exige assumir a composição inicial de filho — o próprio conjunto de pontos revela isso.
- **Samário-neodímio (Sm-Nd).** ¹⁴⁷Sm decai para ¹⁴³Nd (meia-vida ≈ 106 bilhões de anos), também tratado principalmente por isócrona, com a vantagem de que samário e neodímio são ambos elementos terras-raras quimicamente muito similares, o que torna o sistema mais resistente a perturbação por alteração ou metamorfismo posterior do que Rb-Sr (rubídio e estrôncio são quimicamente bem diferentes entre si, e mais móveis em fluidos). Muito usado para investigar a evolução química do manto e da crosta ao longo do tempo geológico profundo.
- **Carbono-14 (¹⁴C).** Caso à parte: meia-vida de apenas **5.730 anos**, o que o torna útil somente para os últimos ~50.000-60.000 anos (depois disso, resta pai radiogênico de menos para medir com confiança). Diferente dos demais, o ¹⁴C não é primordial — é produzido continuamente na atmosfera superior pela interação de raios cósmicos com nitrogênio, incorporado por organismos vivos via fotossíntese e cadeia alimentar enquanto estão vivos (mantendo uma razão ¹⁴C/¹²C em equilíbrio com a atmosfera), e passa a decair sem reposição a partir da morte do organismo. Por isso data **material orgânico** (carvão, madeira, ossos, conchas), não minerais ou rochas — é a ferramenta padrão da arqueologia e da geologia do Quaternário recente, não da escala de tempo profundo que domina o resto deste módulo.

### Temperatura de fechamento: o que a idade realmente data

Um ponto conceitual que costuma escapar numa primeira leitura: uma "idade radiométrica" não data necessariamente "a rocha". Ela data o momento em que um **mineral específico** se tornou um sistema fechado para aquele isótopo-filho — ou seja, o momento em que o filho radiogênico parou de escapar por difusão e passou a se acumular de forma retida na estrutura cristalina. Esse momento é chamado de **temperatura de fechamento** (*closure temperature*) daquele sistema isotópico naquele mineral: acima dela, o filho se difunde para fora do cristal tão rápido quanto se forma (o "relógio" fica com o ponteiro travado em zero); abaixo dela, a difusão é lenta o bastante para o filho se acumular e o relógio começar a contar.

Sistemas diferentes — e até o mesmo sistema em minerais diferentes — têm temperaturas de fechamento distintas: o U-Pb em zircão tem temperatura de fechamento muito alta (frequentemente acima de 800-900 °C, próxima da temperatura de cristalização magmática, por isso costuma datar a cristalização original), enquanto o K-Ar/Ar-Ar em mica tem temperatura de fechamento bem mais baixa e varia entre espécies de mica: cerca de **300-330 °C na biotita** e **350-425 °C na muscovita** (a hornblenda, um anfibólio também usado no método, fecha numa temperatura ainda mais alta, em torno de 500 °C). Isso significa que, numa mesma rocha metamórfica que esfriou lentamente depois de um evento de metamorfismo em alta temperatura, diferentes minerais podem registrar idades **diferentes e todas corretas** — cada uma marcando o momento em que aquele mineral específico esfriou abaixo da sua própria temperatura de fechamento. Esse conjunto de idades, interpretado em conjunto, permite reconstruir não só *quando* um evento ocorreu, mas a **taxa de resfriamento** subsequente da rocha — uma técnica chamada **termocronologia**.

### Verificando a confiabilidade: o diagrama concórdia-discórdia

Como o U-Pb tem dois relógios independentes no mesmo mineral (via ²³⁸U e via ²³⁵U), é possível testar se um zircão se comportou como sistema fechado desde sua formação. A **curva concórdia** é o lugar geométrico de todas as combinações de razões ²⁰⁶Pb/²³⁸U e ²⁰⁷Pb/²³⁵U que dariam a **mesma idade** pelos dois métodos — ou seja, o comportamento esperado de um sistema perfeitamente fechado. Se um conjunto de análises de zircões da mesma rocha cai exatamente sobre a curva concórdia, ambas as idades concordam e a confiança na idade é alta. Se os pontos caem **fora** da curva, alinhados numa reta que a intercepta em dois pontos (uma **discórdia**), isso é evidência de **perda de chumbo** em algum momento posterior à cristalização (tipicamente por um evento metamórfico ou de alteração) — e, notavelmente, a própria reta discórdia ainda contém informação recuperável: os dois pontos de intercepto com a concórdia costumam registrar a idade de cristalização original (intercepto superior) e a idade do evento de perturbação (intercepto inferior).

## Exemplo trabalhado

**Problema.** Uma amostra de rocha ígnea contém um mineral que incorpora ⁴⁰K em sua estrutura, sem argônio inicial (situação idealizada, para simplificar o cálculo). Medições de espectrometria de massa mostram que **12,5%** do ⁴⁰K original ainda está presente como isótopo-pai (o restante decaiu para ⁴⁰Ar). A meia-vida do ⁴⁰K é de aproximadamente **1,25 bilhão de anos**. Qual é a idade da amostra?

*Passo 1 — traduzir "12,5% restante" em número de meias-vidas.* Se 100% é o ponto de partida, depois de uma meia-vida resta 50%; depois de duas, 25%; depois de três, 12,5%. Então já se sabe, por inspeção, que se passaram **3 meias-vidas**, sem precisar da fórmula logarítmica completa — este é o atalho útil sempre que a fração restante é uma potência exata de 1/2.

*Passo 2 — calcular a idade.* Idade = 3 × t₁/₂ = 3 × 1,25 bilhão de anos = **3,75 bilhões de anos**.

*Passo 3 — verificar pela equação geral (mesmo resultado, caminho formal).* N/N₀ = 0,125. t = −(1/λ) · ln(N/N₀), com λ = ln(2)/t₁/₂ = 0,693/1,25 Ga ≈ 0,5545 Ga⁻¹. t = −(1/0,5545) · ln(0,125) = −(1,804) × (−2,079) ≈ **3,75 bilhões de anos**. Os dois caminhos batem, como deveriam.

*Passo 4 — por que essa idade é a da cristalização do mineral, não necessariamente da "rocha" em sentido amplo.* Como discutido, o resultado data o momento em que esse mineral específico se fechou para a difusão de argônio — coerente com sua temperatura de fechamento. Se essa mesma rocha tivesse sofrido um evento metamórfico posterior forte o bastante para reabrir o sistema (ultrapassando a temperatura de fechamento de novo), o "relógio" teria sido zerado naquele momento, e a idade calculada refletiria o evento metamórfico, não a cristalização ígnea original — motivo pelo qual, na prática, geocronólogos frequentemente datam **vários minerais com temperaturas de fechamento diferentes** na mesma amostra, para reconstruir a história completa e não só um único ponto dela.

## Erros comuns

- **Achar que decaimento radioativo é imprevisível porque é probabilístico.** É sedutor porque "probabilístico" soa como sinônimo de "incerto" ou "não confiável". Mas a imprevisibilidade existe apenas no nível de um átomo individual; numa população de bilhões de átomos, a lei dos grandes números torna a fração decaída por unidade de tempo extremamente previsível e constante — é exatamente essa regularidade estatística, não uma regularidade determinística átomo a átomo, que sustenta o método.
- **Achar que meia-vida muda com temperatura, pressão ou reações químicas.** É sedutor porque quase todo outro "relógio" natural (decomposição orgânica, reações químicas, taxas biológicas) de fato acelera com o calor. Mas o decaimento radioativo é um processo do **núcleo atômico**, isolado por muitas ordens de grandeza de energia das condições químicas e físicas do ambiente geológico — pressões e temperaturas de crosta e manto não alteram mensuravelmente a constante de decaimento.
- **Confundir a idade radiométrica de um mineral com a idade de "toda a rocha".** É sedutor porque se fala casualmente em "idade da rocha" como se fosse um número único. Mas, como visto na seção de temperatura de fechamento, diferentes minerais na mesma rocha podem registrar diferentes eventos (cristalização, metamorfismo, resfriamento) — a interpretação correta sempre depende de saber *qual sistema, em qual mineral*, foi datado, e qual evento sua temperatura de fechamento efetivamente registra.
- **Achar que "12,5% restante" significa, sem mais, 87,5% de idade decorrida em relação à meia-vida.** É sedutor por causa da subtração ingênua 100% − 12,5%. Mas a relação entre fração restante e tempo é **exponencial**, não linear — só funciona o atalho de "número de meias-vidas" quando a fração restante é exatamente uma potência de 1/2; qualquer outra fração exige a fórmula logarítmica completa.

## O que não concluir

- Que existe um único método radiométrico "universal" que serve para qualquer rocha e qualquer idade. Cada sistema isotópico tem uma janela útil de idades e um conjunto de minerais/materiais aos quais se aplica — a escolha do método depende do tipo de rocha, da idade aproximada esperada e da pergunta específica (idade de cristalização, de metamorfismo, de resfriamento).
- Que uma única idade radiométrica, isolada, é automaticamente confiável sem verificação. A prática padrão envolve múltiplas análises (vários grãos ou pontos de zircão, por exemplo), testes internos de consistência (como o diagrama concórdia-discórdia) e, frequentemente, comparação com outros sistemas isotópicos independentes antes de aceitar uma idade como robusta.
- Que temperatura de fechamento é um valor fixo e universal para cada sistema isotópico. Na realidade, ela depende também do tamanho do grão mineral (grãos maiores retêm o filho por mais tempo, à mesma temperatura, porque o caminho de difusão até a borda do cristal é mais longo) e da taxa de resfriamento — por isso valores de temperatura de fechamento citados na literatura são aproximações típicas, não constantes absolutas.
- Que o método Rb-Sr ou Sm-Nd por isócrona elimina toda incerteza sobre composição inicial. O método evita ter que *assumir* uma razão inicial arbitrária, mas ainda depende da premissa de que todos os minerais analisados cristalizaram ao mesmo tempo, a partir de um reservatório homogêneo, e permaneceram sistemas fechados depois — premissas que podem falhar e que a própria dispersão dos pontos em torno da reta ajuda a diagnosticar.

## Recap relâmpago

- **Decaimento radioativo:** aleatório por átomo, mas estatisticamente previsível numa população grande — a base do relógio isotópico.
- **Meia-vida (t₁/₂)** e **constante de decaimento (λ)**: t₁/₂ = 0,693/λ. Idade: t = (1/λ)·ln(1 + D/N), calculável a partir da razão pai/filha medida hoje.
- Principais sistemas: **U-Pb** (zircão, meia-vidas de 704 Ma e 4,47 Ga, ideal para rochas antigas), **K-Ar/Ar-Ar** (micas, feldspato, meia-vida 1,25 Ga), **Rb-Sr** e **Sm-Nd** (isócronas, meia-vidas muito longas, rochas antigas), **C-14** (matéria orgânica, só até ~50-60 mil anos, meia-vida de 5.730 anos).
- **Temperatura de fechamento:** o momento em que um mineral específico se torna sistema fechado para o isótopo-filho — a idade data esse evento, não necessariamente "a rocha inteira"; minerais diferentes podem dar idades diferentes e igualmente corretas (termocronologia).
- **Diagrama concórdia-discórdia:** usa os dois decaimentos independentes do U-Pb para testar se o sistema permaneceu fechado; desvios (discórdia) revelam perda de chumbo por eventos posteriores.

## Próxima aula

[[03-tempo-geologico-geocronologia-aula-03-carta-cronoestratigrafica-e-gssp|Aula 03 — A carta cronoestratigráfica da ICS e o conceito de GSSP]], que mostra como milhares de idades relativas e radiométricas, combinadas, viraram a escala do tempo geológico oficial e internacionalmente ratificada.

## Fontes

- Decaimento radioativo e geocronologia, princípios gerais — [Radiometric dating (Wikipedia)](https://en.wikipedia.org/wiki/Radiometric_dating), [USGS, Geologic Time: Radiometric Time Scale](https://www.usgs.gov/)
- U-Pb em zircão — [Zircon geochronology (Wikipedia)](https://en.wikipedia.org/wiki/Zircon), [Uranium–lead dating (Wikipedia)](https://en.wikipedia.org/wiki/Uranium%E2%80%93lead_dating)
- K-Ar e ⁴⁰Ar/³⁹Ar — [Potassium–argon dating (Wikipedia)](https://en.wikipedia.org/wiki/Potassium%E2%80%93argon_dating), [Argon–argon dating (Wikipedia)](https://en.wikipedia.org/wiki/Argon%E2%80%93argon_dating)
- Rb-Sr e Sm-Nd, método da isócrona — [Rubidium–strontium dating (Wikipedia)](https://en.wikipedia.org/wiki/Rubidium%E2%80%93strontium_dating), [Samarium–neodymium dating (Wikipedia)](https://en.wikipedia.org/wiki/Samarium%E2%80%93neodymium_dating), [Isochron dating (Wikipedia)](https://en.wikipedia.org/wiki/Isochron_dating)
- Carbono-14 — [Radiocarbon dating (Wikipedia)](https://en.wikipedia.org/wiki/Radiocarbon_dating)
- Temperatura de fechamento e termocronologia — [Closure temperature (Wikipedia)](https://en.wikipedia.org/wiki/Closure_temperature), [Thermochronology (Wikipedia)](https://en.wikipedia.org/wiki/Thermochronology)
- Diagrama concórdia-discórdia — [Concordia diagram (Wikipedia)](https://en.wikipedia.org/wiki/Concordia_diagram)

<!--
mapa_objetivo_secao:
  OA-02a: "Por que o núcleo atômico funciona como relógio"
  OA-02b: "Meia-vida, constante de decaimento e a equação" + "Exemplo trabalhado"
  OA-02c: "Os principais sistemas isotópicos"
  OA-02d: "Temperatura de fechamento: o que a idade realmente data" + "Verificando a confiabilidade: o diagrama concórdia-discórdia"

alegacoes_auditaveis:
  - claim_id: GEO-M03-A02-MEIAVIDAS-001
    claim: "Meias-vidas: 238U -> 206Pb ~4,47 Ga; 235U -> 207Pb ~704 Ma; 40K -> 40Ar ~1,25 Ga; 87Rb -> 87Sr ~48,8 Ga; 147Sm -> 143Nd ~106 Ga; 14C ~5.730 anos."
    risk: numero
    source: "valores padrão de referência em geocronologia; Wikipedia (páginas de cada método)"
    confianca: alta
  - claim_id: GEO-M03-A02-EQUACAO-002
    claim: "A equação de decaimento t = (1/lambda) * ln(1 + D/N) permite calcular idade a partir da razão pai/filha medida hoje, sem necessidade de conhecer N0."
    risk: mecanismo
    source: "física nuclear/geocronologia padrão"
    confianca: alta
  - claim_id: GEO-M03-A02-ZIRCAO-003
    claim: "O zircão incorpora urânio na estrutura cristalina mas rejeita chumbo, tornando praticamente todo o Pb medido radiogênico; zircões terrestres mais antigos têm idades próximas de 4,4 bilhões de anos."
    risk: numero
    source: "Wikipedia/Zircon; geocronologia U-Pb padrão"
    confianca: alta
  - claim_id: GEO-M03-A02-C14-004
    claim: "O carbono-14 é produzido continuamente na atmosfera superior pela interação de raios cósmicos com nitrogênio, e o método é útil até aproximadamente 50.000-60.000 anos."
    risk: numero
    source: "Wikipedia/Radiocarbon dating"
    confianca: alta
  - claim_id: GEO-M03-A02-FECHAMENTO-005
    claim: "Temperatura de fechamento do sistema U-Pb em zircão é tipicamente acima de 800-900 °C; do sistema K-Ar/Ar-Ar em mica, cerca de 300-330 °C na biotita e 350-425 °C na muscovita; hornblenda em torno de 500 °C."
    risk: numero
    source: "termocronologia padrão (conceito de Dodson, 1973); valores aproximados de referência para biotita ~310-330°C, muscovita ~350-425°C, hornblenda ~500°C"
    confianca: media
    nota: "valores de temperatura de fechamento são aproximações típicas citadas na literatura, não constantes universais - dependem de tamanho de grão e taxa de resfriamento, conforme já ressalvado no texto. Corrigido em auditoria M03-F01: faixa original (300-350°C para 'mica' genericamente) era estreita demais para cobrir a muscovita."
  - claim_id: GEO-M03-A02-CONCORDIA-006
    claim: "O diagrama concórdia-discórdia usa os dois decaimentos independentes do sistema U-Pb para testar consistência interna e detectar perda de chumbo por eventos posteriores à cristalização."
    risk: mecanismo
    source: "Wikipedia/Concordia diagram; geocronologia U-Pb padrão"
    confianca: alta
-->
