# Aula 02: Métodos K-Ar e ⁴⁰Ar-³⁹Ar — cálculo de idades, perda de argônio e leitura de espectros de aquecimento

**ID:** geologia-avancado-m26-a02
**Módulo:** [[26-geologia-isotopica-aplicada-modulo|Módulo 26 — Geologia isotópica aplicada]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** aplicar o decaimento ramificado do ⁴⁰K à equação da idade K-Ar convencional, e entender como a técnica ⁴⁰Ar/³⁹Ar — por irradiação de nêutrons e aquecimento escalonado — mede a mesma idade com uma defesa embutida contra a principal fragilidade do método clássico, a perda parcial de argônio.
**Ao final você vai conseguir:** calcular uma idade K-Ar convencional a partir de uma razão ⁴⁰Ar*/⁴⁰K medida; explicar o que é o fator J e como ele substitui a medida direta de potássio no método ⁴⁰Ar/³⁹Ar; calcular uma idade ⁴⁰Ar/³⁹Ar a partir de uma razão ⁴⁰Ar*/³⁹ArK e de um padrão de calibração; e ler um espectro de idade por etapas de aquecimento, reconhecendo um platô válido e um padrão de perda de argônio.
**Pré-requisito:** [[26-geologia-isotopica-aplicada-aula-01-radioatividade-lei-decaimento-geocronologia-espectrometria-massa|Aula 01]] (lei do decaimento, equação geral da idade, premissa do sistema fechado).

## Conteúdo

### Por que o potássio é um relógio geológico tão usado

O potássio é um dos oito elementos mais abundantes da crosta terrestre e entra na estrutura cristalina de minerais formadores de rocha comuns — micas (biotita, muscovita), feldspato potássico, anfibólio e argilominerais (illita, glauconita) — o que torna o sistema K-Ar aplicável a uma gama enorme de rochas ígneas, metamórficas e mesmo sedimentares (datação de autigênese de argilominerais). O potássio natural tem três isótopos: ³⁹K (93,26% em abundância) e ⁴¹K (6,73%), ambos estáveis, e ⁴⁰K (0,0117%), o único radioativo dos três — raro em abundância relativa, mas presente em quantidade suficiente, dada a abundância total do potássio na crosta, para produzir argônio radiogênico mensurável mesmo em rochas relativamente jovens.

### O decaimento ramificado do ⁴⁰K

Diferente dos sistemas de decaimento simples da Aula 01, o ⁴⁰K decai por **dois caminhos concorrentes** para dois núcleos-filho diferentes:

- cerca de 89,5% dos átomos de ⁴⁰K decaem por emissão **beta negativa** (β⁻) para **⁴⁰Ca** (cálcio-40);
- os cerca de 10,5% restantes decaem por **captura eletrônica** (o núcleo captura um elétron da camada K do próprio átomo) para **⁴⁰Ar** (argônio-40), um gás nobre.

O ramo para ⁴⁰Ca é geocronologicamente inútil na prática: o cálcio já é abundantíssimo na maioria dos minerais e rochas, de modo que a pequena quantidade de ⁴⁰Ca radiogênico se perde na massa de ⁴⁰Ca comum já presente — não há como separar analiticamente o cálcio "novo" do cálcio original. O ramo para ⁴⁰Ar, ao contrário, é o que sustenta toda a geocronologia K-Ar: como o argônio é um gás nobre quimicamente inerte, ele não entra na estrutura cristalina de um mineral em formação (um magma em erupção libera o argônio que porventura contivesse, e um mineral cristalizando a partir dele começa, em teoria, com ⁴⁰Ar próximo de zero); todo ⁴⁰Ar encontrado hoje aprisionado na rede cristalina de um mineral, portanto, é presumivelmente radiogênico — produzido *in situ* pelo decaimento do ⁴⁰K desde a cristalização.

Cada ramo tem sua própria constante de decaimento parcial: λβ (para ⁴⁰Ca) e λε (para ⁴⁰Ar, incluindo a captura eletrônica e uma fração muito pequena de emissão de pósitron, agrupadas na mesma constante por convenção). A constante de decaimento **total** é a soma dos dois ramos, λ = λβ + λε, e é ela quem entra na lei do decaimento de N (a população de ⁴⁰K, que decai pelos dois caminhos simultaneamente). Pelos valores convencionais de Steiger & Jäger (1977) — a base ainda mais citada, embora não a única em uso, como a seção seguinte discute —, λβ = 4,962 × 10⁻¹⁰ ano⁻¹ e λε = 0,581 × 10⁻¹⁰ ano⁻¹, somando λ = 5,543 × 10⁻¹⁰ ano⁻¹ (o mesmo valor usado no exemplo de conversão de meia-vida da Aula 01). A fração do decaimento total que vai para o argônio — a **razão de ramificação** — é λε/λ = 0,581/5,543 ≈ 0,1048, ou aproximadamente 10,5%: de cada 100 átomos de ⁴⁰K que decaem, cerca de 10 ou 11 produzem ⁴⁰Ar e o restante produz ⁴⁰Ca.

### A equação da idade K-Ar convencional

Como só uma fração λε/λ dos átomos de ⁴⁰K que decaem produz o filho que se mede (⁴⁰Ar), a equação geral da idade da Aula 01 precisa de um fator de correção para essa ramificação. A forma da equação da idade K-Ar convencional é:

$$t = \frac{1}{\lambda}\ln\!\left[\frac{\lambda}{\lambda_\varepsilon}\left(\frac{{}^{40}\text{Ar}^{*}}{{}^{40}\text{K}}\right) + 1\right]$$

onde ⁴⁰Ar* é o argônio radiogênico medido (assumindo sistema fechado e argônio inicial desprezível) e ⁴⁰K é calculado a partir do potássio total medido no mineral (por absorção atômica, fotometria de chama ou ativação de nêutrons) multiplicado pela abundância isotópica natural do ⁴⁰K (0,0117%). O termo λ/λε > 1 amplia a razão medida antes do logaritmo, compensando o fato de que só uma fração do ⁴⁰K decaído produziu o argônio observado.

**A fragilidade estrutural do método.** A equação da idade K-Ar convencional depende de **duas medidas totalmente independentes**, em geral feitas em duas alíquotas separadas da amostra e às vezes até em laboratórios diferentes: o potássio total, medido por um método químico, e o argônio radiogênico, medido por espectrometria de massa de gás nobre. Se o mineral perdeu argônio por aquecimento posterior (metamorfismo, soterramento profundo, intrusão próxima) sem que essa perda deixe qualquer marca visível na medida de potássio, a idade calculada subestima silenciosamente a idade real do evento que se quer datar, e **não há, dentro do próprio dado K-Ar convencional, nenhum sinal interno de que isso aconteceu**. É exatamente essa fragilidade que o método ⁴⁰Ar/³⁹Ar foi desenhado para resolver.

### O truque do ⁴⁰Ar/³⁹Ar: transformar potássio em um isótopo de argônio

A ideia central do método ⁴⁰Ar/³⁹Ar, desenvolvido a partir do final dos anos 1960, é evitar por completo a medida química de potássio, substituindo-a por uma segunda medida de argônio. Isso se consegue irradiando a amostra com um fluxo de nêutrons rápidos em um reator nuclear de pesquisa antes da análise. A irradiação converte uma fração pequena e conhecida do ³⁹K (o isótopo estável mais abundante do potássio) em ³⁹Ar por uma reação nuclear induzida (³⁹K(n,p)³⁹Ar — captura de um nêutron com emissão de um próton). O ³⁹Ar é, ele mesmo, radioativo, mas com meia-vida de centenas de anos — tempo suficiente para medir a amostra em semanas a meses sem perda apreciável, mas descartando a necessidade de qualquer medida química separada de potássio: a quantidade de ³⁹Ar produzida é diretamente proporcional à quantidade de ³⁹K presente (e, portanto, de ⁴⁰K, já que os dois isótopos de potássio ocorrem em proporção fixa na natureza).

O problema é que a "constante de proporcionalidade" entre ³⁹Ar produzido e ³⁹K original depende do fluxo de nêutrons recebido, que varia de posição para posição dentro do reator e não é conhecido a priori com a precisão necessária. A solução é irradiar, junto com as amostras desconhecidas, um **monitor de fluxo** (também chamado de padrão de idade): um mineral (em geral sanidina ou biotita) cuja idade **já é conhecida com alta precisão** por calibração independente. Da razão medida entre ⁴⁰Ar* e ³⁹ArK no próprio monitor e de sua idade conhecida, calcula-se o **fator J** (o parâmetro de irradiação, que absorve toda a dependência do fluxo de nêutrons, da duração da irradiação e da seção de choque da reação nuclear em um único número empírico):

$$J = \frac{e^{\lambda t_{\text{padrão}}} - 1}{\left({}^{40}\text{Ar}^{*}/{}^{39}\text{Ar}_K\right)_{\text{padrão}}}$$

Um dos monitores mais usados mundialmente é a sanidina do Fish Canyon Tuff (sudoeste do Colorado, EUA), com uma idade de referência amplamente adotada — a calibração astronômica de Kuiper et al. (2008), de 28,201 ± 0,046 Ma — embora, como a seção seguinte comenta, essa não seja a única calibração em circulação na literatura. Uma vez determinado J a partir do monitor irradiado na mesma posição (ou em posição próxima e interpolada) que a amostra desconhecida, a idade da amostra vem de:

$$t = \frac{1}{\lambda}\ln\!\left[J\left(\frac{{}^{40}\text{Ar}^{*}}{{}^{39}\text{Ar}_K}\right)_{\text{amostra}} + 1\right]$$

Note a elegância da construção: essa equação tem exatamente a forma da equação geral da idade da Aula 01, com J desempenhando o papel de λ/λε da equação convencional — mas agora **toda a informação sobre potássio vem de uma razão entre dois isótopos de argônio, medidos na mesma alíquota, no mesmo instrumento**, o que elimina o erro sistemático de combinar duas medidas independentes em laboratórios ou métodos diferentes.

### Onde ainda mora a incerteza: a própria calibração do relógio

O método ⁴⁰Ar/³⁹Ar não eliminou toda controvérsia numérica do sistema: a comunidade ainda debate tanto o valor exato da constante de decaimento total do ⁴⁰K (Steiger & Jäger, 1977: 5,543 × 10⁻¹⁰ ano⁻¹; recalibrações posteriores, como a de Min et al., propõem valores próximos de 5,463 × 10⁻¹⁰ ano⁻¹) quanto a idade de referência exata do Fish Canyon Tuff (Kuiper et al., 2008: 28,201 Ma; Renne et al., 2010: 28,305 Ma; Renne et al., 2011, revisando o próprio valor anterior: 28,294 ± 0,036 Ma — uma divergência de cerca de 0,3 a 0,4% em relação a Kuiper). Essa divergência afeta **toda** a escala de tempo ⁴⁰Ar/³⁹Ar sistematicamente e de forma proporcional à idade, com diferenças de poucos milhares de anos no Quaternário, dezenas de milhares no Neogeno e até cerca de 200 mil anos perto do limite Cretáceo-Paleogeno. **Isto não é falha do método, mas lembrete de que toda idade isotópica publicada carrega, implícita, a convenção de calibração usada** — checar qual conjunto de constantes o autor declara é hábito de leitura crítica.

### Lendo um espectro de idade por aquecimento escalonado

A vantagem prática mais usada do método ⁴⁰Ar/³⁹Ar não é apenas dispensar a medida química de potássio — é permitir o **aquecimento escalonado** (*step heating*): em vez de fundir a amostra de uma vez (como no K-Ar convencional, onde só existe uma medida de ⁴⁰Ar* por amostra), a amostra irradiada é aquecida em uma série de etapas de temperatura crescente (a laser ou em forno resistivo), e o gás de argônio liberado em **cada etapa** é analisado separadamente, produzindo uma idade aparente para cada uma.

Se o mineral se comportou como sistema fechado desde a cristalização (ou o último resfriamento abaixo da temperatura de bloqueio do argônio para aquele mineral), as etapas de temperatura intermediária a alta tendem a devolver idades **concordantes** entre si — um **platô de idade**: um conjunto de etapas contíguas, tipicamente exigindo, por convenção da comunidade (ver, por exemplo, McDougall & Harrison, 1999), que cubram pelo menos a metade do ³⁹Ar total liberado e que suas idades individuais se sobreponham dentro do erro de 2σ, sem tendência sistemática crescente ou decrescente entre elas. Quando esse platô existe, a idade do platô (a média ponderada das etapas que o compõem) é interpretada como a idade de fechamento do sistema, com uma confiança adicional que o K-Ar convencional, de medida única, não oferece: **o próprio formato do espectro é um teste de sistema fechado**.

Quando o mineral perdeu argônio de forma parcial e recente (por reaquecimento posterior à cristalização, sem reabertura total do sistema), o padrão típico é um espectro em **forma de U ou de "escada ascendente"**: as etapas de temperatura mais baixa (que liberam o gás retido nos sítios cristalinos mais fracamente ligados, mais suscetíveis à perda por difusão) mostram idades aparentes anomalamente **jovens**, enquanto as etapas de temperatura mais alta (gás retido em sítios estruturais mais robustos, que resistiram à perda) se aproximam progressivamente da idade original de cristalização — às vezes sem nunca formar um platô claro, e às vezes formando um platô parcial nas etapas de temperatura mais alta que ainda permite recuperar uma idade geologicamente útil, mesmo que o restante do espectro esteja comprometido. Essa é a razão prática pela qual o método ⁴⁰Ar/³⁹Ar é preferido sobre o K-Ar convencional em terrenos que sofreram história térmica complexa (múltiplos eventos de metamorfismo ou magmatismo sobrepostos): o espectro inteiro, e não um único número, é o dado.

## Exemplo trabalhado 1: idade K-Ar convencional

**Situação.** Uma amostra de biotita de um dique ígneo tem uma razão medida ⁴⁰Ar*/⁴⁰K = 0,00500 (valor hipotético, construído para este exemplo). Usando os valores convencionais de Steiger & Jäger (1977) — λ = 5,543 × 10⁻¹⁰ ano⁻¹ e λε = 0,581 × 10⁻¹⁰ ano⁻¹ —, qual é a idade K-Ar da biotita?

**Resolução.** Primeiro, o fator de correção pela ramificação:

$$\frac{\lambda}{\lambda_\varepsilon} = \frac{5{,}543\times10^{-10}}{0{,}581\times10^{-10}} \approx 9{,}540$$

Substituindo na equação da idade K-Ar:

$$t = \frac{1}{5{,}543\times10^{-10}}\ln\!\left[9{,}540 \times 0{,}00500 + 1\right] = \frac{1}{5{,}543\times10^{-10}}\ln(1{,}04770)$$

Calculando o logaritmo: ln(1,04770) ≈ 0,046600. Então:

$$t = \frac{0{,}046600}{5{,}543\times10^{-10}} \approx 8{,}41\times10^{7}\ \text{anos} \approx 84{,}1\ \text{milhões de anos}$$

A biotita registraria uma idade K-Ar de aproximadamente 84,1 Ma (Cretáceo Superior) — **desde que** o sistema tenha permanecido fechado e que a medida de potássio total, em uma alíquota separada, corresponda de fato à mesma população mineral analisada para argônio.

## Exemplo trabalhado 2: fator J e idade ⁴⁰Ar/³⁹Ar

**Situação.** Uma sanidina usada como monitor de fluxo de nêutrons, com idade de referência t_padrão = 28,201 Ma (Fish Canyon Tuff, calibração de Kuiper et al., 2008), foi irradiada junto com uma amostra desconhecida e mostrou uma razão medida (⁴⁰Ar*/³⁹ArK)_padrão = 0,0523 (valor hipotético, escolhido apenas para ilustrar o cálculo — não é o valor real medido para o Fish Canyon Tuff, que depende do fluxo de nêutrons específico de cada irradiação). Qual o fator J dessa irradiação, e qual a idade de uma amostra desconhecida irradiada na mesma posição, com razão medida (⁴⁰Ar*/³⁹ArK)_amostra = 0,1200?

**Resolução — fator J.** Convertendo a idade do padrão para anos, t_padrão = 2,8201 × 10⁷ anos. O expoente:

$$\lambda\, t_{\text{padrão}} = 5{,}543\times10^{-10} \times 2{,}8201\times10^{7} \approx 0{,}015633$$

$$e^{0{,}015633} - 1 \approx 0{,}015756$$

$$J = \frac{0{,}015756}{0{,}0523} \approx 0{,}30125$$

**Resolução — idade da amostra.** Substituindo J e a razão medida na equação da idade ⁴⁰Ar/³⁹Ar:

$$t = \frac{1}{5{,}543\times10^{-10}}\ln\!\left[0{,}30125 \times 0{,}1200 + 1\right] = \frac{1}{5{,}543\times10^{-10}}\ln(1{,}036150)$$

Calculando: ln(1,036150) ≈ 0,035512. Então:

$$t = \frac{0{,}035512}{5{,}543\times10^{-10}} \approx 6{,}41\times10^{7}\ \text{anos} \approx 64{,}1\ \text{milhões de anos}$$

**Interpretação.** Note que essa idade foi calculada **sem qualquer medida química de potássio** — toda a informação de "quanto ⁴⁰K havia" está embutida no fator J, calibrado pelo monitor. É essa independência de uma medida química separada, mais a possibilidade de repetir o cálculo etapa a etapa num aquecimento escalonado, que dá ao ⁴⁰Ar/³⁹Ar sua vantagem estrutural sobre o K-Ar convencional do Exemplo 1.

## Recap relâmpago

- O ⁴⁰K decai por dois caminhos concorrentes: ~89,5% por β⁻ para ⁴⁰Ca (geocronologicamente inútil, pois o cálcio radiogênico se perde na massa de cálcio comum) e ~10,5% por captura eletrônica para ⁴⁰Ar (a base do método, porque o argônio é um gás nobre inerte que não entra na estrutura cristalina até ser produzido *in situ*).
- A idade K-Ar convencional, t = (1/λ)ln[(λ/λε)(⁴⁰Ar*/⁴⁰K) + 1], depende de duas medidas independentes (potássio químico e argônio por espectrometria de gás nobre) — sua fragilidade estrutural é que perda parcial de argônio não deixa nenhum sinal interno no dado, e a idade calculada simplesmente subestima em silêncio.
- O método ⁴⁰Ar/³⁹Ar substitui a medida química de potássio por irradiação de nêutrons, que converte uma fração conhecida de ³⁹K em ³⁹Ar; o fator J, calibrado por um monitor de idade conhecida (como a sanidina do Fish Canyon Tuff, ≈28,201 Ma na calibração de Kuiper et al. 2008), absorve a dependência do fluxo de nêutrons.
- Tanto a constante de decaimento do ⁴⁰K quanto a idade de referência dos monitores de irradiação têm calibrações concorrentes na literatura (λ total de 5,543 × 10⁻¹⁰/ano em Steiger & Jäger 1977 contra 5,463 × 10⁻¹⁰/ano em Min et al. 2000; Fish Canyon sanidina de 28,201 Ma em Kuiper et al. 2008 contra 28,294 Ma em Renne et al. 2011 — uma diferença de cerca de 0,3%); toda idade ⁴⁰Ar/³⁹Ar publicada carrega implicitamente a convenção usada, e checar qual foi declarada é hábito de leitura crítica.
- O aquecimento escalonado produz um espectro de idade por etapa de temperatura: um **platô** (etapas contíguas, cobrindo tipicamente ≥50% do ³⁹Ar liberado, com idades concordantes em 2σ) indica sistema fechado; um espectro em **U ou escada ascendente**, com idades jovens nas etapas de baixa temperatura subindo até estabilizar nas de alta temperatura, é a assinatura de perda parcial de argônio por reaquecimento.

## Próxima aula

[[26-geologia-isotopica-aplicada-aula-03-sistema-rb-sr|Aula 03 — Sistema Rb-Sr]]: o primeiro sistema do módulo que resolve o problema do filho inicial não desprezível pela técnica da isócrona, construindo e interpretando o diagrama ⁸⁷Rb/⁸⁶Sr vs. ⁸⁷Sr/⁸⁶Sr, e usando a razão inicial de estrôncio como traçador de fonte em petrogênese.

## Fontes

- Faure, G. & Mensing, T. M. (2005), *Isotopes: Principles and Applications*, 3ª ed., Wiley — capítulo 12 (sistema K-Ar e ⁴⁰Ar/³⁹Ar, decaimento ramificado do ⁴⁰K, equação do fator J).
- McDougall, I. & Harrison, T. M. (1999), *Geochronology and Thermochronology by the ⁴⁰Ar/³⁹Ar Method*, 2ª ed., Oxford University Press — referência padrão para o método ⁴⁰Ar/³⁹Ar, aquecimento escalonado e critérios de platô de idade.
- Steiger, R. H. & Jäger, E. (1977), "Subcommission on geochronology: convention on the use of decay constants in geo- and cosmochronology", *Earth and Planetary Science Letters*, 36(3), 359-362 (doi 10.1016/0012-821X(77)90060-7) — valores convencionais λβ = (4,962 ± 0,009) × 10⁻¹⁰ ano⁻¹, λε = (0,581 ± 0,004) × 10⁻¹⁰ ano⁻¹ e λ total = (5,543 ± 0,010) × 10⁻¹⁰ ano⁻¹ para o ⁴⁰K. CONFERIDO na auditoria (2026-09-21): os três valores e a paginação confirmados.
- Kuiper, K. F. et al. (2008), "Synchronizing rock clocks of Earth history", *Science*, 320(5875), 500-504 — calibração astronômica da sanidina do Fish Canyon Tuff, idade de 28,201 ± 0,046 Ma. CONFERIDO na auditoria (2026-09-21): volume, fascículo e paginação confirmados.
- Renne, P. R., Mundil, R., Balco, G., Min, K. & Ludwig, K. R. (2010), "Joint determination of ⁴⁰K decay constants and ⁴⁰Ar*/⁴⁰K for the Fish Canyon sanidine standard, and improved accuracy for ⁴⁰Ar/³⁹Ar geochronology", *Geochimica et Cosmochimica Acta*, 74(18), 5349-5367 — idade do Fish Canyon sanidine de 28,305 Ma, com λε = (0,5757 ± 0,0016) × 10⁻¹⁰ e λβ = (4,9548 ± 0,0134) × 10⁻¹⁰ ano⁻¹. CONFERIDO na auditoria (2026-09-21).
- Renne, P. R., Balco, G., Ludwig, K. R., Mundil, R. & Min, K. (2011), "Response to the comment by W. H. Schwarz et al. on 'Joint determination of ⁴⁰K decay constants...' by P. R. Renne et al. (2010)", *Geochimica et Cosmochimica Acta*, 75(17), 5097-5100 — revisão do próprio valor de 2010 para idade do Fish Canyon sanidine de 28,294 ± 0,036 Ma, com λε = (0,5755 ± 0,0016) × 10⁻¹⁰ e λβ = (4,9737 ± 0,0093) × 10⁻¹⁰ ano⁻¹ (λ total = 5,5492 × 10⁻¹⁰ ano⁻¹). CONFERIDO na auditoria (2026-09-21): é este o valor de 28,294 Ma citado no texto.
- Min, K., Mundil, R., Renne, P. R. & Ludwig, K. R. (2000), "A test for systematic errors in ⁴⁰Ar/³⁹Ar geochronology through comparison with U/Pb analysis of a 1.1-Ga rhyolite", *Geochimica et Cosmochimica Acta*, 64(1), 73-98 — recalibração da constante de decaimento total do ⁴⁰K em (5,463 ± 0,054) × 10⁻¹⁰ ano⁻¹, correspondendo a meia-vida de 1,269 ± 0,013 Ga. CONFERIDO na auditoria (2026-09-21): autoria, ano, veículo, paginação e valor confirmados.

<!--
nivel: avancado
palavras_corpo: 2467
mapa_objetivo_secao:
  geologia-avancado-m26-oa02: "O decaimento ramificado do 40K" + "A equação da idade K-Ar convencional" + "O truque do 40Ar/39Ar" + "Onde ainda mora a incerteza" + "Lendo um espectro de idade por aquecimento escalonado" + "Exemplo trabalhado 1" + "Exemplo trabalhado 2"

alegacoes_auditaveis:
  - claim_id: ISOGEO-M26-A02-DECAIMENTO-RAMIFICADO-K40-001
    claim: "O 40K decai por dois caminhos concorrentes: aproximadamente 89,5% por emissao beta negativa para 40Ca, e aproximadamente 10,5% por captura eletronica (mais uma fracao muito pequena de emissao de positron, agrupada na mesma constante por convencao) para 40Ar; a constante de decaimento total e a soma das duas constantes parciais, lambda = lambda_beta + lambda_epsilon."
    risk: fato
    source: "Faure & Mensing (2005), Isotopes: Principles and Applications, 3a ed., Wiley, cap. 12. A razao de ramificacao de ~10,5% e derivada dos valores de Steiger & Jager (1977) (lambda_epsilon/lambda_total = 0,581/5,543 = 0,1048); valores alternativos na literatura existem.
    CONFIRMADO PELA AUDITORIA (2026-09-21), sem correcao necessaria no texto: com os valores de Steiger & Jager (1977), verificados como corretos (lambda_epsilon = 0,581e-10, lambda_beta = 4,962e-10), a razao de ramificacao lambda_epsilon/lambda_total = 0,581/5,543 = 0,104817, ou 10,48% - o '~10,5%' e o '89,5%' do corpo da aula estao corretos para a convencao que a aula declara estar usando. Recalibracoes posteriores deslocam esse numero em fracoes de ponto percentual: com os valores de Renne et al. (2011), verificados nesta auditoria (lambda_epsilon = 0,5755e-10, lambda_beta = 4,9737e-10, total 5,5492e-10), a razao cai para 10,37%. A aula ja sinaliza a existencia de calibracoes concorrentes na secao 'Onde ainda mora a incerteza', e o corpo usa 'cerca de' em ambos os percentuais, de modo que a segunda casa decimal nao e afirmada. INCERTEZA DECLARADA RESOLVIDA.
    ATENCAO A UMA CONFUSAO COMUM DE CONVENCAO, verificada na auditoria: parte da literatura reporta para Steiger & Jager uma 'razao de ramificacao' de 0,1171, que e lambda_epsilon/lambda_BETA (0,581/4,962 = 0,11709) e NAO lambda_epsilon/lambda_TOTAL. As duas definicoes circulam com o mesmo nome. A aula usa, corretamente e de forma explicita, a fracao do decaimento total que vai para o argonio ('de cada 100 atomos de 40K que decaem, cerca de 10 ou 11 produzem 40Ar'), que e a razao sobre o total."
  - claim_id: ISOGEO-M26-A02-STEIGER-JAGER-VALORES-PARCIAIS-002
    claim: "Os valores convencionais de Steiger & Jager (1977) para as constantes de decaimento parcial do 40K sao lambda_beta = 4,962x10^-10/ano (para 40Ca) e lambda_epsilon = 0,581x10^-10/ano (para 40Ar), somando lambda_total = 5,543x10^-10/ano."
    risk: fato
    source: "Citado de memoria a partir do artigo classico Steiger, R.H. & Jager, E. (1977), Earth and Planetary Science Letters, 36(3), 359-362, cujo valor total (5,543x10^-10/ano) foi VERIFICADO por busca nesta redacao. CONFIRMADO PELA AUDITORIA (2026-09-21): os valores parciais estao CORRETOS como publicados - lambda_epsilon = (0,581 +/- 0,004) x 10^-10 /ano e lambda_beta = (4,962 +/- 0,009) x 10^-10 /ano, somando lambda_total = (5,543 +/- 0,010) x 10^-10 /ano, adotados por convencao pela Subcomissao de Geocronologia da IUGS a partir de Steiger & Jager (1977); paginacao e DOI (10.1016/0012-821X(77)90060-7) tambem verificados. Soma reconferida por calculo: 4,962e-10 + 0,581e-10 = 5,543e-10 exatamente. A INCERTEZA DECLARADA esta RESOLVIDA sem correcao necessaria."
  - claim_id: ISOGEO-M26-A02-EQUACAO-IDADE-KAR-003
    claim: "A equacao da idade K-Ar convencional e t = (1/lambda)*ln[(lambda/lambda_epsilon)*(40Ar*/40K) + 1], onde 40Ar* e o argonio radiogenico medido e 40K e calculado do potassio total multiplicado pela abundancia isotopica natural do 40K (0,0117%)."
    risk: fato
    source: "Forma padrao da equacao de idade K-Ar, derivada da equacao geral da idade da Aula 01 aplicada ao decaimento ramificado; ver Faure & Mensing (2005), cap. 12, e Dickin, A.P. (2005), Radiogenic Isotope Geology, 2a ed., Cambridge University Press, cap. 10. Abundancia isotopica natural do 40K (0,0117%) e valor padrao de tabelas de isotopos."
  - claim_id: ISOGEO-M26-A02-METODO-AR-AR-FATOR-J-004
    claim: "No metodo 40Ar/39Ar, a amostra e irradiada com neutrons rapidos, convertendo uma fracao conhecida de 39K em 39Ar (reacao 39K(n,p)39Ar); o fator de irradiacao J e calculado a partir de um monitor de idade conhecida irradiado junto, por J = (e^(lambda*t_padrao) - 1) / (40Ar*/39ArK)_padrao, e a idade da amostra desconhecida e t = (1/lambda)*ln[J*(40Ar*/39ArK)_amostra + 1]. O 39Ar produzido e radioativo, mas com meia-vida de centenas de anos, suficiente para nao decair de forma apreciavel durante o periodo tipico entre irradiacao e analise."
    risk: fato
    source: "McDougall, I. & Harrison, T.M. (1999), Geochronology and Thermochronology by the 40Ar/39Ar Method, 2a ed., Oxford University Press - referencia padrao do metodo. Meia-vida do 39Ar: valor tabelado de fisica nuclear, nao verificado contra fonte primaria na redacao.
    ACHADO LARANJA 6 (auditoria 2026-09-21), claim ISOGEO-M26-A02-AR39-MODO-DECAIMENTO-010: esta propria alegacao afirmava que o 39Ar decai 'por captura eletronica'. FALSO: o 39Ar decai por EMISSAO BETA NEGATIVA (beta-) para 39K, com energia de transicao (endpoint) de 565 keV, classificada como decaimento beta- unico de primeira proibicao. A meia-vida esta CORRETA: 269 +/- 3 anos, o que confirma tambem o 'centenas de anos' do corpo da aula. Fontes: Stoenner, Schaeffer & Katcoff (1965), 'Half-lives of Argon-37, Argon-39, and Argon-42', Science 148(3675), 1325-1328; e dados nucleares replicados na literatura de detectores de argonio (endpoint 565 keV, ~1 Bq/kg no argonio atmosferico). NOTA IMPORTANTE DE ESCOPO: o erro estava APENAS neste bloco de metadados de auditoria - o CORPO da aula nunca declarou o modo de decaimento do 39Ar, dizendo somente 'o 39Ar e, ele mesmo, radioativo, mas com meia-vida de centenas de anos', o que esta correto. Nenhuma correcao foi necessaria no texto que o aluno le; a correcao foi feita aqui, no registro. Valor exato agora declarado: 269 +/- 3 anos, por beta-."
  - claim_id: ISOGEO-M26-A02-FISH-CANYON-KUIPER-005
    claim: "A sanidina do Fish Canyon Tuff (sudoeste do Colorado, EUA) e um dos monitores de fluxo de neutrons mais usados mundialmente em 40Ar/39Ar; a calibracao astronomica de Kuiper et al. (2008) atribui a ela uma idade de 28,201 +/- 0,046 Ma."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-21): 'In 2008, Kuiper and others published an astronomically calibrated age of 28.201 +/- 0.046 Ma for the Fish Canyon sanidine (FCs)... Kuiper et al. (2008) performed 40Ar/39Ar cross-calibration experiments with sanidine from tephras in the astronomically tuned Messadit section (Melilla Basin, Morocco) to determine the age of FCs as 28.201 +/- 0.046 Ma (2 sigma).' Publicado em Science."
  - claim_id: ISOGEO-M26-A02-CONTROVERSIA-CALIBRACAO-006
    claim: "Existe divergencia na literatura entre calibracoes concorrentes tanto da constante de decaimento total do 40K (Steiger & Jager 1977: 5,543x10^-10/ano; recalibracoes mais recentes, como Min et al., proximas de 5,463x10^-10/ano) quanto da idade de referencia do Fish Canyon Tuff (calibracao astronomica de Kuiper et al. 2008: 28,201 Ma; calibracao de intercomparacao de sistemas de Renne et al. 2010-2011: valor ligeiramente mais velho, na ordem de 28,3 Ma), com diferencas da ordem de fracoes de percentual que se propagam sistematicamente por toda a escala de tempo 40Ar/39Ar."
    risk: fato
    source: "VERIFICADO parcialmente por busca nesta redacao: resultado de busca confirma explicitamente 'reported K-Ar and 40Ar/39Ar ages for FCTs vary from 27.54 +/- 0.29 Ma to 28.39 +/- 0.19 Ma (2 sigma), a spread of ~3%, with researchers including Renne et al., 2011 among those who have proposed different ages' e que a idade de Kuiper et al. (2008) 'has been challenged by later studies... leading again to a ~1.5% age scattering'. O valor especifico de Min et al. (~5,463x10^-10/ano) para a constante de decaimento foi mencionado em resultado de busca associado a este valor, mas a citacao bibliografica completa (autores, ano, veiculo) nao foi verificada nesta redacao.
    CONFIRMADO PELA AUDITORIA (2026-09-21), com as duas referencias agora completas e o valor verificado: (a) Min, K., Mundil, R., Renne, P.R. & Ludwig, K.R. (2000), 'A test for systematic errors in 40Ar/39Ar geochronology through comparison with U/Pb analysis of a 1.1-Ga rhyolite', Geochimica et Cosmochimica Acta 64(1), 73-98 - lambda total do 40K = (5,463 +/- 0,054) x 10^-10 /ano, meia-vida 1,269 +/- 0,013 Ga; o valor de 5,463 citado na aula esta CORRETO. (b) Renne, P.R., Mundil, R., Balco, G., Min, K. & Ludwig, K.R. (2010), GCA 74(18), 5349-5367, e Renne, P.R., Balco, G., Ludwig, K.R., Mundil, R. & Min, K. (2011), 'Response to the comment by W.H. Schwarz et al....', GCA 75(17), 5097-5100. INCERTEZAS DECLARADAS RESOLVIDAS.
    ACHADO LARANJA 3 (auditoria 2026-09-21), claim ISOGEO-M26-A02-DIVERGENCIA-PERCENTUAL-011: o corpo da aula afirmava que Renne et al. (2010-2011) divergem de Kuiper et al. (2008) 'por cerca de 0,4-0,7%'. IMPRECISO E EXAGERADO. Valores reais: Renne et al. (2011) da 28,294 +/- 0,036 Ma e Renne et al. (2010) dava 28,305 Ma, contra 28,201 +/- 0,046 Ma de Kuiper et al. (2008). Divergencias recalculadas pela auditoria: (28,294-28,201)/28,201 = 0,330% e (28,305-28,201)/28,201 = 0,369%. A faixa correta e 0,3 a 0,4%, nao 0,4 a 0,7%. Corrigido no corpo e no recap, com os tres valores numericos agora explicitados em vez de so a faixa percentual. CORRECAO PROPAGADA: a frase seguinte dizia que a divergencia produz 'diferencas de milhares a dezenas de milhares de anos em eventos do Cenozoico'; 0,33% de 66 Ma sao ~218 mil anos, de modo que a faixa estava subestimada no extremo antigo. Reescrita para 'poucos milhares de anos no Quaternario, dezenas de milhares no Neogeno e ate cerca de 200 mil anos perto do limite Cretaceo-Paleogeno'. NOTA: a dispersao de ~3% mencionada no resultado de busca original (27,54 a 28,39 Ma) e a de TODAS as idades K-Ar e 40Ar/39Ar ja reportadas para o Fish Canyon Tuff ao longo de decadas, nao a divergencia entre as duas calibracoes modernas concorrentes que o texto compara - confundir as duas coisas foi a origem provavel do 0,7%."
  - claim_id: ISOGEO-M26-A02-ESPECTRO-PLATO-007
    claim: "Um plato de idade em um espectro de aquecimento escalonado 40Ar/39Ar e definido, por convencao da comunidade, como um conjunto de etapas contiguas cobrindo tipicamente pelo menos 50% do 39Ar total liberado, com idades individuais concordantes dentro do erro de 2 sigma e sem tendencia sistematica; perda parcial de argonio por reaquecimento produz tipicamente um espectro em forma de U ou 'escada ascendente', com idades jovens nas etapas de baixa temperatura subindo ate estabilizar nas etapas de alta temperatura."
    risk: fato
    source: "McDougall, I. & Harrison, T.M. (1999), Geochronology and Thermochronology by the 40Ar/39Ar Method, 2a ed., Oxford University Press - criterios de plato e interpretacao de espectros de perda de argonio sao conteudo padrao deste livro-texto de referencia do metodo. O criterio numerico exato (>=50% do 39Ar, >=3 etapas contiguas) pode variar ligeiramente entre laboratorios e software de reducao de dados - sinalizado no texto como 'convencao', nao como regra universal fixa."
  - claim_id: ISOGEO-M26-A02-EXEMPLO-KAR-CONVENCIONAL-008
    claim: "Para 40Ar*/40K = 0,00500 medido, com lambda=5,543x10^-10/ano e lambda_epsilon=0,581x10^-10/ano, a equacao da idade K-Ar convencional da lambda/lambda_epsilon=9,541, ln(9,541*0,00500+1)=ln(1,04771)=0,04661, e t=0,04661/5,543x10^-10=8,41x10^7 anos (84,1 milhoes de anos)."
    risk: calculo
    source: "Aritmetica direta a partir da equacao apresentada nesta aula; dado de entrada (40Ar*/40K=0,00500) e hipotetico, construido para este exemplo pedagogico.
    ACHADO LARANJA 7 (auditoria 2026-09-21), claim ISOGEO-M26-A02-ARREDONDAMENTOS-EXEMPLOS-012: os dois exemplos trabalhados desta aula publicavam intermediarios mal arredondados. (a) Exemplo 1: lambda/lambda_epsilon = 5,543/0,581 = 9,54045, que arredonda para 9,540, nao 9,541 como publicado; e o logaritmo ln(1,047702) = 0,046599, nao 0,04661. (b) Exemplo 2: ln(1,036150) = 0,0355119, nao 0,035506 como publicado. Todos recalculados pela auditoria por execucao em Python. IMPACTO NO RESULTADO: nenhum - as idades finais permanecem 84,1 Ma (exato 84,07 Ma) e 64,1 Ma (exato 64,06 Ma) com tres algarismos significativos. O achado foi mantido como laranja e corrigido de todo modo porque um exemplo trabalhado e justamente o material que o aluno reproduz passo a passo: um intermediario que nao fecha faz o aluno duvidar da propria conta. Valores publicados agora: 9,540, ln(1,04770)=0,046600 e ln(1,036150)=0,035512."
  - claim_id: ISOGEO-M26-A02-EXEMPLO-FATOR-J-009
    claim: "Para um padrao com t=28,201 Ma e (40Ar*/39ArK)_padrao=0,0523 (hipotetico), lambda*t_padrao=5,543x10^-10*2,8201x10^7=0,015633, e^0,015633-1=0,015756, J=0,015756/0,0523=0,30125; para uma amostra com (40Ar*/39ArK)=0,1200, t=(1/lambda)*ln(0,30125*0,1200+1)=(1/5,543x10^-10)*ln(1,036150)=0,035506/5,543x10^-10=6,41x10^7 anos (64,1 milhoes de anos)."
    risk: calculo
    source: "Aritmetica direta a partir das equacoes apresentadas nesta aula; a idade do padrao (28,201 Ma) e a de Kuiper et al. (2008), VERIFICADA por busca (ver claim 005), mas a razao (40Ar*/39ArK)_padrao=0,0523 e o valor da amostra (0,1200) sao hipoteticos, escolhidos apenas para ilustrar o calculo e nao correspondem a medidas reais do Fish Canyon Tuff."
-->
