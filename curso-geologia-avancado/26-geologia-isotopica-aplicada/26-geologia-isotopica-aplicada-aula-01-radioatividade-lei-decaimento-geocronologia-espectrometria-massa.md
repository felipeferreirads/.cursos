# Aula 01: Radioatividade, lei do decaimento e geocronologia; espectrometria de massa de isótopos tradicionais e não tradicionais

**ID:** geologia-avancado-m26-a01
**Módulo:** [[26-geologia-isotopica-aplicada-modulo|Módulo 26 — Geologia isotópica aplicada]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** explicar a lei do decaimento radioativo e deduzir dela a equação da idade que sustenta toda a geocronologia isotópica, e entender o princípio físico com que um espectrômetro de massa mede razões isotópicas — tanto para os isótopos radiogênicos "tradicionais" (Sr, Nd, Pb, Os, Hf) quanto para os isótopos estáveis "não tradicionais" de elementos de transição e metaloides (Fe, Cu, Zn, Mg, Mo, entre outros).
**Ao final você vai conseguir:** escrever e aplicar a lei do decaimento radioativo e a equação geral da idade isotópica; converter entre constante de decaimento e meia-vida; explicar por que um sistema isotópico precisa ser fechado para datar um evento; descrever o princípio de separação por massa/carga de um espectrômetro de massa (TIMS e MC-ICP-MS); e distinguir, em uma frase, o que torna um isótopo "tradicional" (radiogênico) de um "não tradicional" (estável, de massa variável).
**Pré-requisito:** nenhum dentro deste curso. Ajuda ter familiaridade básica com notação exponencial e logaritmo natural, e com a tabela periódica (número atômico, número de massa, isótopo).

## Conteúdo

### Por que datar uma rocha é contar átomos

Toda a geocronologia isotópica descansa sobre um fato experimental muito bem estabelecido: um núcleo atômico instável (um **radionuclídeo pai**, ou nuclídeo-pai) se transforma espontaneamente em outro núcleo (o **nuclídeo-filho**, ou produto radiogênico) numa taxa que não depende de temperatura, pressão, estado químico ou de qualquer processo geológico — só do tempo decorrido e da identidade do próprio núcleo. Se você souber quantos átomos-filho radiogênicos se acumularam a partir de quantos átomos-pai, e souber a taxa de conversão, você calcula há quanto tempo esse acúmulo começou. Datar uma rocha, na prática, é **contar átomos** de duas populações (pai remanescente e filho acumulado) com uma precisão de partes por milhão a bilhão, e essa contagem é o que a espectrometria de massa faz.

### A lei do decaimento radioativo

O decaimento de um radionuclídeo é um processo estatístico: em qualquer intervalo de tempo pequeno, cada átomo-pai tem a mesma probabilidade de decair, independente da idade do átomo (um núcleo não "envelhece" — essa é a diferença fundamental entre decaimento nuclear e qualquer processo biológico ou mecânico). Essa probabilidade por unidade de tempo é a **constante de decaimento**, representada por λ (lambda), com unidade de "por ano" (ano⁻¹). Para uma população de N átomos-pai no instante t, a taxa de decaimento é proporcional à própria população:

$$\frac{dN}{dt} = -\lambda N$$

Integrando essa equação diferencial entre o instante inicial (t = 0, quando havia N₀ átomos-pai) e um instante t qualquer, obtém-se a **lei do decaimento radioativo**:

$$N = N_0\, e^{-\lambda t}$$

Essa é a mesma forma matemática de qualquer processo de decaimento exponencial (resfriamento de Newton, descarga de um capacitor), e vale para qualquer radionuclídeo isolado — a diferença entre um sistema e outro está inteiramente no valor de λ, que é uma propriedade nuclear medida em laboratório, não algo que varia com o ambiente geológico.

### Meia-vida: a forma mais intuitiva de expressar λ

A **meia-vida** (t₁/₂) é o tempo necessário para que metade de uma população de átomos-pai decaia. Fazendo N = N₀/2 na lei do decaimento:

$$\frac{N_0}{2} = N_0\, e^{-\lambda t_{1/2}} \quad\Rightarrow\quad t_{1/2} = \frac{\ln 2}{\lambda} \approx \frac{0{,}6931}{\lambda}$$

Meia-vida e constante de decaimento carregam exatamente a mesma informação — são só duas formas de expressar a mesma taxa. A literatura de geocronologia cita as duas de forma intercambiável, e é comum uma tabela dar λ e outra dar t₁/₂ para o mesmo sistema; saber converter entre as duas evita o erro comum de tratá-las como duas propriedades diferentes que precisariam, cada uma, ser medida separadamente.

**Conferindo com um caso real:** para o ⁴⁰K (potássio-40), sistema da Aula 02, o valor de constante de decaimento total recomendado por Steiger & Jäger (1977) — a convenção adotada pela IUGS (União Internacional de Ciências Geológicas) e ainda hoje a mais citada em cursos e em boa parte da literatura, embora existam refinamentos mais recentes discutidos na Aula 02 — é λ = 5,543 × 10⁻¹⁰ ano⁻¹. A meia-vida correspondente é

$$t_{1/2} = \frac{0{,}6931}{5{,}543\times10^{-10}} \approx 1{,}25\times10^{9}\ \text{anos} = 1{,}25\ \text{Ga}$$

que é exatamente o valor de 1,25 bilhão de anos citado em qualquer manual de geocronologia para o ⁴⁰K. A conta é só a definição de meia-vida aplicada ao número tabelado.

### Da lei do decaimento à equação da idade

O que se mede em laboratório não é diretamente N₀ (a quantidade original de átomos-pai, que ninguém observou), mas sim **quanto pai sobrou hoje** (P, a quantidade atual de átomos-pai) e **quanto filho radiogênico se acumulou** (D*, o asterisco indicando que é especificamente a fração do filho que veio do decaimento, e não a que já existia no mineral quando ele se formou). Como cada átomo-pai que decaiu virou exatamente um átomo-filho radiogênico (em um sistema de decaimento simples, de um passo), a quantidade original de pai era N₀ = P + D*. Substituindo na lei do decaimento (com N = P no instante atual) e isolando t, chega-se à **equação geral da idade isotópica**:

$$t = \frac{1}{\lambda}\ln\!\left(1 + \frac{D^{*}}{P}\right)$$

Essa equação é o coração de todo o módulo: os cinco sistemas radiogênicos das Aulas 02 a 05 (K-Ar/Ar-Ar, Rb-Sr, Sm-Nd, U-Pb e Pb-Pb) são, no fundo, variações desta mesma equação, com λ e a definição de D* e P específicas de cada par pai-filho, mais a complicação adicional — tratada aula a aula — de como isolar o D* que é **de fato radiogênico** de um D* que já estava presente no mineral quando ele se formou (o "filho inicial", que a técnica da isócrona existe justamente para resolver).

### As quatro premissas que fazem a idade significar algo

A equação da idade só devolve um número geologicamente útil se quatro condições, nenhuma delas garantida automaticamente pela física do decaimento, forem satisfeitas:

1. **O sistema precisa estar fechado.** Nem pai nem filho podem ter entrado ou saído do mineral desde o evento que se quer datar (cristalização, recristalização metamórfica, resfriamento abaixo de uma temperatura de bloqueio). A **temperatura de bloqueio** — termo que reaparece nas Aulas 02 e 05 e que vale fixar já aqui — é a temperatura abaixo da qual a difusão do isótopo-filho para fora da rede cristalina fica lenta demais para importar em escala geológica: acima dela, o filho escapa à medida que é produzido e o relógio não acumula nada; abaixo dela, o mineral retém o que produz e o relógio começa a contar. Cada par mineral–sistema isotópico tem a sua, e é daí que vem a frase que atravessa o módulo inteiro: uma idade isotópica data, a rigor, o **fechamento** do sistema, que nem sempre é o mesmo instante que a cristalização da rocha. Perda de argônio por difusão térmica (Aula 02), perda de chumbo por dano radioativo em zircão (Aula 05) e troca de estrôncio por fluido hidrotermal (Aula 03) são formas concretas de violação desta premissa, e cada aula do módulo trata de como reconhecer e, quando possível, contornar essa violação.
2. **A quantidade inicial de filho precisa ser conhecida ou determinável.** Em alguns sistemas ela é desprezível por construção do método (o argônio, um gás nobre, escapa do magma antes da cristalização, de modo que ⁴⁰Ar inicial em um mineral ígneo recém-formado é próximo de zero); em outros, ela não é desprezível e precisa ser resolvida — é o problema central que a técnica da isócrona ataca (Aulas 03 a 05).
3. **A constante de decaimento precisa ser conhecida com precisão e ser, de fato, constante.** Decaimento radioativo por emissão alfa, beta ou captura eletrônica não é sensível a temperatura, pressão ou ligação química nas condições da crosta e do manto terrestres — ao contrário do que ocorre, por exemplo, com decaimento por conversão interna em condições atômicas extremas de laboratório, que não tem relevância geológica. As constantes de decaimento usadas em geocronologia vêm de décadas de medição física de laboratório e de calibração cruzada entre sistemas, e são objeto de recomendações formais e periódicas de comissões conjuntas da IUPAC (União Internacional de Química Pura e Aplicada) e da IUGS — um processo que segue ativo, como a Aula 02 mostra para o ⁴⁰K.
4. **A razão isotópica precisa ser medida com exatidão e precisão suficientes.** Isso é tarefa da espectrometria de massa, tratada a seguir.

### Como um espectrômetro de massa separa e conta isótopos

Um espectrômetro de massa não "vê" um átomo — ele separa partículas carregadas por sua razão massa/carga (m/z) usando campos elétricos e magnéticos, e conta quantas chegam a cada posição de um detector. O princípio, comum a todos os desenhos usados em geocronologia, tem três etapas:

1. **Ionização.** A amostra, previamente separada quimicamente do elemento de interesse (por exemplo, o estrôncio isolado de uma amostra de rocha por cromatografia de troca iônica), precisa virar um feixe de íons. Dois métodos dominam a geocronologia de isótopos radiogênicos: a **ionização térmica** (TIMS, sigla em inglês de *thermal ionization mass spectrometry*), em que a amostra é depositada sobre um filamento de metal refratário (tântalo ou rênio) e aquecida no vácuo até ionizar termicamente; e o **plasma indutivamente acoplado** (ICP-MS), em que a amostra em solução é nebulizada e injetada em um plasma de argônio a cerca de 6.000–10.000 K, ionizando praticamente qualquer elemento.
2. **Aceleração e separação por massa.** Os íons são acelerados por um campo elétrico e entram em um campo magnético; a força magnética curva a trajetória de cada íon com um raio proporcional à raiz quadrada de m/z — íons mais leves (numa mesma carga) curvam mais, íons mais pesados curvam menos. O resultado é um leque de feixes, cada um correspondendo a uma massa isotópica diferente, fisicamente separados no espaço na saída do ímã.
3. **Detecção e contagem.** Um **coletor** (uma copa de Faraday, que mede corrente elétrica, ou um multiplicador de elétrons, mais sensível e usado para feixes fracos) posicionado em cada trajetória conta a intensidade do feixe correspondente. Instrumentos **multicoletores** (o "MC" de MC-ICP-MS e o equivalente em TIMS multicoletor) têm várias copas fixas ou móveis, permitindo medir várias massas isotópicas **ao mesmo tempo**, o que cancela boa parte da instabilidade temporal do próprio feixe de íons e é o que torna possível a precisão de partes por 10⁵–10⁶ que a geocronologia moderna exige.

A escolha entre TIMS e MC-ICP-MS depende do elemento e do sistema: TIMS ainda domina para Rb-Sr (mede razões de Sr) e Sm-Nd (razões de Nd) em muitos laboratórios pela sua altíssima precisão em razões isotópicas de massa média, enquanto MC-ICP-MS ganhou espaço para Pb (que ioniza mal termicamente sem tratamento especial) e é praticamente obrigatório para os isótopos não tradicionais desta aula, porque ioniza eficientemente elementos que a ionização térmica trata mal (Fe, Cu, Zn, Mo).

### Isótopos "tradicionais" e "não tradicionais": uma distinção de mecanismo, não de tabela periódica

O módulo usa duas expressões que valem a pena fixar logo no início, porque orientam a leitura das Aulas 02 a 06:

- **Isótopos tradicionais** são os isótopos **radiogênicos** — aqueles cuja razão isotópica muda ao longo do tempo geológico **porque um deles é o produto do decaimento de um radionuclídeo-pai**. É o caso de ⁴⁰Ar (filho do ⁴⁰K), ⁸⁷Sr (filho do ⁸⁷Rb), ¹⁴³Nd (filho do ¹⁴⁷Sm), ²⁰⁶Pb/²⁰⁷Pb/²⁰⁸Pb (filhos de ²³⁸U/²³⁵U/²³²Th) e ¹⁸⁷Os (filho do ¹⁸⁷Re, sistema não coberto neste módulo). A variação da razão isotópica nesses sistemas mede diretamente **tempo decorrido**, pela equação da idade desta aula.
- **Isótopos não tradicionais** (também chamados, na literatura, de isótopos "metálicos" ou "de metal de transição", embora a categoria inclua também metaloides como Si) são isótopos **estáveis** de elementos como Fe, Cu, Zn, Mg, Ca, Mo, Li, Cr, Se, Tl e Hg, cuja razão isotópica varia **não por decaimento radioativo, mas por fracionamento dependente de massa**: processos físico-químicos (mudança de estado de oxidação, precipitação mineral, processos biológicos, difusão) discriminam levemente entre isótopos mais leves e mais pesados do mesmo elemento, porque a massa afeta a energia de ligação e a velocidade de reação. Esse fracionamento não mede tempo — mede **processo**: condição redox, temperatura, via metabólica, fonte de contaminação. A Aula 06 desenvolve essas aplicações em detalhe.

A separação analítica entre as duas categorias ficou historicamente amarrada à separação instrumental: isótopos tradicionais, com diferenças de massa relativa grandes (a diferença entre ⁸⁷Sr e ⁸⁶Sr já é cerca de 1,2% da massa), eram mensuráveis com a resolução de TIMS de gerações anteriores; isótopos não tradicionais, com diferenças de massa relativa muito menores (a diferença entre ⁵⁶Fe e ⁵⁴Fe é de cerca de 3,6%, mas o efeito de fracionamento a ser resolvido é de frações de por mil), só se tornaram rotineiramente mensuráveis com o MC-ICP-MS de alta resolução a partir do final dos anos 1990 e ao longo dos anos 2000 — o motivo pelo qual a geoquímica de isótopos não tradicionais é um campo consideravelmente mais recente que a geocronologia radiogênica clássica, que remonta às primeiras décadas do século XX.

## Exemplo trabalhado: da lei do decaimento à idade de um mineral hipotético

**Situação.** Um mineral hipotético cristalizou incorporando apenas o isótopo-pai de um sistema radioativo fictício "X", sem nenhum isótopo-filho inicial (D₀ = 0 — uma simplificação deliberada para isolar o raciocínio matemático da equação da idade, antes de os sistemas reais das próximas aulas introduzirem a complicação do filho inicial). A constante de decaimento desse sistema hipotético é λ = 5,00 × 10⁻¹⁰ ano⁻¹. Uma análise moderna do mineral mede uma razão filho radiogênico/pai remanescente de D*/P = 0,250. Qual é a idade de cristalização?

**Resolução.** Aplicando diretamente a equação geral da idade:

$$t = \frac{1}{\lambda}\ln\!\left(1+\frac{D^{*}}{P}\right) = \frac{1}{5{,}00\times10^{-10}}\ln(1{,}250)$$

Calculando o logaritmo natural: ln(1,250) ≈ 0,22314. Então:

$$t = \frac{0{,}22314}{5{,}00\times10^{-10}} \approx 4{,}463\times10^{8}\ \text{anos} \approx 446{,}3\ \text{milhões de anos}$$

**Verificação de sanidade.** Vale conferir se o resultado é fisicamente razoável antes de aceitá-lo: a meia-vida deste sistema hipotético é t₁/₂ = ln2/λ = 0,6931/5,00×10⁻¹⁰ ≈ 1,386 × 10⁹ anos. Uma idade de 446 milhões de anos é cerca de um terço dessa meia-vida — ou seja, esperamos que uma fração ainda pequena do pai original tenha decaído, e de fato D*/P = 0,25 significa que, para cada átomo-pai remanescente, há um quarto de átomo-filho acumulado: uma conversão parcial, coerente com uma idade bem menor que a meia-vida. Esse tipo de checagem cruzada — a idade calculada é consistente com a fração de decaimento observada e com a meia-vida do sistema? — é um hábito que vale carregar para os cálculos de K-Ar, Rb-Sr, Sm-Nd e U-Pb das próximas quatro aulas, onde o mesmo raciocínio se aplica com D*/P substituído por razões isotópicas reais.

## Recap relâmpago

- O decaimento radioativo segue N = N₀e^(−λt); a meia-vida t₁/₂ = ln2/λ é só outra forma de expressar a constante de decaimento λ, e as duas aparecem de forma intercambiável na literatura.
- A equação geral da idade isotópica, t = (1/λ)ln(1 + D*/P), deriva diretamente da lei do decaimento assumindo que cada átomo-pai perdido virou um átomo-filho radiogênico (D*).
- Uma idade isotópica só é geologicamente significativa se quatro premissas se sustentam: sistema fechado, filho inicial conhecido ou determinável, constante de decaimento bem calibrada e razão isotópica medida com exatidão — as próximas quatro aulas mostram, sistema a sistema, onde cada premissa costuma falhar e como contorná-la.
- Um sistema se fecha quando o mineral esfria abaixo da sua **temperatura de bloqueio**, abaixo da qual o isótopo-filho para de escapar por difusão. É por isso que uma idade isotópica data, a rigor, um **fechamento** — e não necessariamente a cristalização da rocha, distinção que reaparece nas Aulas 02 e 05 e que é o ponto de dificuldade central do módulo.
- Um espectrômetro de massa separa isótopos por razão massa/carga usando ionização (térmica, no TIMS, ou por plasma, no ICP-MS), aceleração num campo magnético e detecção multicoletora — o mesmo princípio físico serve tanto para isótopos radiogênicos quanto para isótopos estáveis não tradicionais.
- **Isótopos tradicionais** (Sr, Nd, Pb, Os) são radiogênicos: sua razão isotópica varia com o **tempo**, pela lei do decaimento. **Isótopos não tradicionais** (Fe, Cu, Zn, Mg, Mo etc.) são estáveis: sua razão isotópica varia por **fracionamento dependente de massa**, e mede processo físico-químico ou biológico, não tempo — tema da Aula 06.

## Próxima aula

[[26-geologia-isotopica-aplicada-aula-02-metodos-k-ar-ar-ar|Aula 02 — Métodos K-Ar e ⁴⁰Ar-³⁹Ar]]: o primeiro sistema radiogênico do módulo em detalhe, incluindo o decaimento ramificado do ⁴⁰K, o cálculo de idades K-Ar convencionais, e como a técnica ⁴⁰Ar/³⁹Ar resolve, por irradiação de nêutrons e aquecimento escalonado, boa parte das fragilidades do método clássico.

## Fontes

- Faure, G. & Mensing, T. M. (2005), *Isotopes: Principles and Applications*, 3ª ed., Wiley — capítulos 1 e 2 (lei do decaimento radioativo, dedução da equação geral da idade).
- Dickin, A. P. (2005), *Radiogenic Isotope Geology*, 2ª ed., Cambridge University Press — capítulo 1 (fundamentos de decaimento radioativo e instrumentação de espectrometria de massa).
- Steiger, R. H. & Jäger, E. (1977), "Subcommission on geochronology: convention on the use of decay constants in geo- and cosmochronology", *Earth and Planetary Science Letters*, 36(3), 359-362 — valor convencional de λ para o ⁴⁰K citado no exemplo de conversão meia-vida/constante de decaimento.
- Albarède, F. (2004), "The stable isotope geochemistry of copper and zinc", *Reviews in Mineralogy and Geochemistry*, 55(1), 409-427 (doi 10.2138/gsrmg.55.1.409) — capítulo do volume 55 da série, intitulado *Geochemistry of Non-Traditional Stable Isotopes* (Mineralogical Society of America, 2004), o primeiro volume da série dedicado ao tema e, em si, um marco da consolidação do campo. CONFERIDO na auditoria (2026-09-21): autor, ano, título, série, volume, fascículo, paginação e DOI todos confirmados.
- Steiger, R. H. & Jäger, E. (1977) — ver a Aula 02 para os valores parciais λβ e λε do ⁴⁰K, confirmados na auditoria (2026-09-21) contra a referência original.

<!--
nivel: avancado
palavras_corpo: 2563
palavras_corpo_metodo: "contagem de tokens separados por espaco do corpo entre '## Conteudo' e '## Fontes', INCLUINDO blocos LaTeX e tabelas. Metodo declarado a partir de 2026-09-22 para que passagens futuras comparem o mesmo numero; contagens anteriores a esta data usavam convencao nao declarada e sao ligeiramente menores."
duracao_estimada_min: 30

NOTA DE REVISAO DIDATICA (2026-09-22, revisor-didatico, modo review-and-fix):
  ACHADO LARANJA DID-5 CORRIGIDO - 'temperatura de bloqueio' usada sem definicao. O termo aparecia
  aqui (premissa 1) e de novo na Aula 02 ('o ultimo resfriamento abaixo da temperatura de bloqueio
  do argonio para aquele mineral'), em NENHUMA das duas com definicao, e em nenhuma outra aula do
  modulo. E um conceito central: e ele que explica por que uma idade isotopica data um fechamento e
  nao uma cristalizacao - que e, palavra por palavra, o 'ponto de dificuldade' declarado no hub do
  modulo. Corrigido com uma definicao na primeira ocorrencia (aqui), mais um bullet no recap.
  A definicao acrescentada - temperatura abaixo da qual a difusao do isotopo-filho para fora da
  rede cristalina fica lenta demais para importar em escala geologica; acima dela o filho escapa a
  medida que e produzido, abaixo dela o mineral retem - NAO e fato novo no modulo: e exatamente o
  mecanismo que a Aula 02 ja descreve em detalhe ao tratar de perda de argonio por difusao termica
  e de espectros de aquecimento escalonado (claim ISOGEO-M26-A02-ESPECTRO-PLATO-007, auditado), e
  que a Aula 05 descreve para a perda de chumbo. A revisao apenas nomeou e definiu, no lugar certo,
  o conceito que o modulo ja usava. Nenhum valor numerico de temperatura de bloqueio foi publicado.
  DURACAO: esta aula passou de ~28,4 para ~30,5 min pelo metodo de contagem acima, ou seja, ficou
  no teto de 30 min do plugin - e o acrescimo desta revisao responde por boa parte disso. NAO foi
  dividida, porque o conteudo e um arco unico (lei do decaimento -> equacao da idade -> premissas
  -> como se mede), e porque dividir uma aula de fundamentos separa a deducao da sua aplicacao.
  Registrado como achado amarelo DID-7 para que uma passagem futura NAO acrescente mais texto aqui
  sem cortar equivalente.

mapa_objetivo_secao:
  geologia-avancado-m26-oa01: "A lei do decaimento radioativo" + "Meia-vida: a forma mais intuitiva de expressar λ" + "Da lei do decaimento à equação da idade" + "As quatro premissas que fazem a idade significar algo" + "Como um espectrômetro de massa separa e conta isótopos" + "Isótopos tradicionais e não tradicionais: uma distinção de mecanismo, não de tabela periódica" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: ISOGEO-M26-A01-LEI-DECAIMENTO-001
    claim: "O decaimento radioativo segue dN/dt = -lambda*N, integrando para N = N0*e^(-lambda*t); a meia-vida t(1/2) = ln(2)/lambda e a equacao geral da idade isotopica de um sistema de decaimento simples e t = (1/lambda)*ln(1 + D*/P), onde D* e o filho radiogenico acumulado e P e o pai remanescente."
    risk: fato
    source: "Dedução matemática padrão a partir da equação diferencial de decaimento de primeira ordem; forma apresentada em qualquer texto-base de geocronologia, e.g. Faure & Mensing (2005), Isotopes: Principles and Applications, 3a ed., Wiley, cap. 1-2; Dickin, A. P. (2005), Radiogenic Isotope Geology, 2a ed., Cambridge University Press, cap. 1."
  - claim_id: ISOGEO-M26-A01-K40-LAMBDA-STEIGER-JAGER-002
    claim: "A constante de decaimento total do 40K recomendada por Steiger & Jager (1977), convencao adotada pela IUGS e ainda amplamente citada, e lambda = 5,543 x 10^-10 /ano, correspondendo a uma meia-vida de aproximadamente 1,25 bilhao de anos (1,25 Ga)."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-21): resultado de busca confirma 'The recommended value of the total decay constant lambda for 40K decay from Steiger and Jager (1977) is 5.543 x 10^-10 per year, equivalent to a half-life of 1.25 Byr', citando Steiger, R.H. & Jager, E. (1977), Earth and Planetary Science Letters, 36(3), 359-362. Existem refinamentos mais recentes (p.ex. Min et al., valor proximo a 5,463x10^-10/ano) discutidos na Aula 02; nao ha consenso unico substituindo Steiger & Jager na pratica corrente, por isso a aula sinaliza explicitamente a existencia de valores alternativos."
  - claim_id: ISOGEO-M26-A01-ESPECTROMETRIA-PRINCIPIO-003
    claim: "Um espectrometro de massa separa ions por razao massa/carga (m/z) por meio de ionizacao (termica, no TIMS, sobre filamento de Ta ou Re; ou por plasma de argonio a ~6000-10000 K, no ICP-MS), aceleracao por campo eletrico e deflexao por campo magnetico (raio de curvatura proporcional a raiz quadrada de m/z), com deteccao por copos de Faraday (corrente) ou multiplicadores de eletrons (feixes fracos); instrumentos multicoletores medem varias massas simultaneamente, reduzindo o efeito de instabilidade temporal do feixe."
    risk: fato
    source: "Principio fisico padrao de espectrometria de massa por setor magnetico, descrito em Dickin, A. P. (2005), Radiogenic Isotope Geology, 2a ed., Cambridge University Press, cap. 1 (instrumentacao). Conhecimento consolidado de instrumentacao analitica; nao verificado contra fonte primaria especifica nesta redacao - risco baixo por ser descricao de principio fisico estabelecido, nao de valor numerico controverso."
  - claim_id: ISOGEO-M26-A01-TRADICIONAL-NAO-TRADICIONAL-004
    claim: "Isotopos 'tradicionais' (Sr, Nd, Pb, Os, Hf) sao radiogenicos: a razao isotopica varia com o tempo por decaimento de um nuclideo-pai. Isotopos 'nao tradicionais' (Fe, Cu, Zn, Mg, Ca, Mo, Li, Cr, Se, Tl, Hg, entre outros) sao estaveis e variam por fracionamento dependente de massa (discriminacao fisico-quimica entre isotopos leves e pesados por processos como mudanca de estado de oxidacao, precipitacao mineral e processos bioquimicos), nao por decaimento; a geoquimica de isotopos nao tradicionais e um campo mais recente, viabilizado pelo MC-ICP-MS de alta resolucao a partir do final dos anos 1990/anos 2000."
    risk: fato
    source: "Terminologia e distincao conceitual padrao da literatura de geoquimica isotopica (ver p.ex. capitulos introdutorios de Reviews in Mineralogy and Geochemistry sobre isotopos nao tradicionais). Ano de popularizacao do MC-ICP-MS para isotopos nao tradicionais (final dos anos 1990 a anos 2000) e conhecimento consolidado de historia da tecnica, nao verificado contra fonte primaria unica nesta redacao.
    CONFIRMADO PELA AUDITORIA (2026-09-21) por evidencia bibliografica direta, sem correcao necessaria: o volume 55 da serie Reviews in Mineralogy and Geochemistry, intitulado 'Geochemistry of Non-Traditional Stable Isotopes' (Mineralogical Society of America), foi publicado em 2004 e e o PRIMEIRO volume da serie dedicado ao tema - uma serie de revisao so dedica um volume a um campo depois que ele tem corpo de literatura suficiente, o que datar a consolidacao do campo 'a partir do final dos anos 1990 e ao longo dos anos 2000' sustenta com folga. Referencia verificada do capitulo citado: Albarede, F. (2004), 'The stable isotope geochemistry of copper and zinc', RiMG 55(1), 409-427, doi 10.2138/gsrmg.55.1.409 (autor, ano, titulo, volume, fasciculo, paginacao e DOI todos conferidos). A aula usa 'a partir de' e 'ao longo de', nao uma data pontual, de modo que nao ha numero exato a corrigir. INCERTEZA DECLARADA RESOLVIDA.
    VERIFICACOES NUMERICAS COMPLEMENTARES da auditoria nesta aula: diferenca de massa relativa 87Sr-86Sr = 1/86 = 1,16% (aula diz 'cerca de 1,2%', correto); 56Fe-54Fe = 2/55 = 3,64% (aula diz 'cerca de 3,6%', correto). Abundancias isotopicas do potassio citadas na Aula 02 (39K 93,26%, 41K 6,73%, 40K 0,0117%) somam 100,0017% por arredondamento dos valores tabelados (93,2581 / 6,7302 / 0,0117), sem erro."
  - claim_id: ISOGEO-M26-A01-EXEMPLO-IDADE-HIPOTETICA-005
    claim: "Para um sistema hipotetico com lambda = 5,00x10^-10/ano e D*/P = 0,250 medido, a equacao t=(1/lambda)ln(1+D*/P) da t = ln(1,250)/5,00x10^-10 = 0,22314/5,00x10^-10 = 4,463x10^8 anos (=446,3 milhoes de anos); a meia-vida desse sistema e ln(2)/lambda = 1,386x10^9 anos."
    risk: calculo
    source: "Aritmetica direta a partir da equacao apresentada; ln(1,25)=0,223144 e ln(2)=0,693147 sao valores matematicos padrao. Dados de entrada (lambda, D*/P) sao hipoteticos, criados para este exemplo pedagogico, e nao correspondem a um sistema isotopico real. RECALCULADO E CONFIRMADO PELA AUDITORIA (2026-09-21, execucao em Python): ln(1,25)=0,22314355; t=446.287.103 anos = 446,3 Ma; meia-vida do sistema hipotetico = ln(2)/5,00e-10 = 1,3863e9 anos = 1,386 Ga. Os tres numeros publicados reproduzem. Conversao meia-vida do 40K tambem reconferida: 0,6931/5,543e-10 = 1,2504e9 anos = 1,25 Ga, consistente com o valor tabelado citado. Nenhum erro aritmetico nesta aula."
-->
