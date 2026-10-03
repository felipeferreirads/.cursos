# Aula 01: Como se enxerga o interior da Terra — ondas sísmicas e descontinuidades

**ID:** geologia-gemologia-m02-a01
**Módulo:** [[02-sistema-terra-tectonica-modulo|Módulo 02 — Sistema Terra: estrutura interna e tectônica de placas]]
**Duração estimada:** ~30 min
**Objetivo:** entender o método pelo qual a estrutura interna da Terra foi descoberta — como ondas sísmicas, sem ninguém jamais ter descido lá, revelam o que existe a milhares de quilômetros de profundidade.
**Pré-requisito:** Módulo 01, Aula 03 (divisão química × mecânica da Terra, diferenciação planetária, a Moho como limite sísmico).

## Ao final você vai conseguir

- [OA-01a] Explicar por que o interior da Terra exige um método indireto, e por que a sismologia cumpre esse papel.
- [OA-01b] Distinguir ondas de corpo (P e S) de ondas de superfície, e explicar por que a onda S não atravessa líquido.
- [OA-01c] Reconstruir, como raciocínio e não como lista de nomes, como Mohorovičić, Gutenberg e Lehmann inferiram os limites internos da Terra a partir de dados sísmicos.
- [OA-01d] Diferenciar a zona de sombra da onda S (prova de núcleo externo líquido) da zona de sombra da onda P (efeito de refração, não de bloqueio).

## Conteúdo

### O problema: um planeta que não se pode abrir

A aula anterior já apresentou as camadas da Terra — crosta, manto, núcleo; litosfera, astenosfera, mesosfera, núcleos externo e interno. O que não foi respondido ainda é a pergunta mais óbvia: **como se sabe disso**, se ninguém jamais chegou lá?

O comparativo deixa o problema claro. O furo mais profundo já perfurado pela humanidade é o **Kola Superdeep Borehole** (SG-3), no norte da Rússia, que atingiu cerca de **12.262 metros** de profundidade após quase duas décadas de perfuração. É um feito de engenharia notável — e, diante do **raio médio da Terra, de 6.371 km**, esse furo mal arranha a crosta continental. Em proporção, é como furar um alfinete na casca de uma maçã e afirmar que se sabe o que tem no caroço.

Existem amostras diretas parciais, e vale registrar quais são, porque elas vão reaparecer no curso:

- **Xenólitos mantélicos** trazidos à superfície por certos magmas (como os kimberlitos), fragmentos de manto arrancados em erupções violentas e rápidas o bastante para não reequilibrar quimicamente no caminho.
- **Ofiolitos**, fatias de crosta oceânica e manto superior empurradas sobre continentes por processos tectônicos, hoje expostas em cadeias de montanha.
- **Meteoritos**, especialmente os ferrosos — como visto na aula anterior, a melhor amostra física do material que compõe o núcleo terrestre, mesmo vindo de um corpo-pai diferente da Terra.

Essas amostras são preciosas, mas são pontuais e superficiais diante da escala do problema: elas não dizem nada sobre a *geometria* do interior — onde ficam os limites, que espessura tem cada camada, se as fronteiras são nítidas ou graduais. Para isso, é preciso um método que enxergue através de milhares de quilômetros de rocha sem perfurar nada. Esse método é a **sismologia**: ela funciona como um tomógrafo planetário, usando a energia liberada por terremotos (e por explosões controladas, em escala menor) para "iluminar" o interior da Terra a partir de fora.

### Ondas sísmicas: como a energia de um terremoto viaja

Quando uma falha rompe e libera energia elástica acumulada, essa energia se propaga em várias formas de onda, cada uma com velocidade e comportamento próprios. Entender essas diferenças é o alicerce de tudo que vem a seguir.

**Ondas de corpo** — viajam pelo interior do planeta, atravessando o volume da Terra:

- **Onda P (primária, compressional ou longitudinal)** — é a mais rápida de todas, por isso chega primeiro a qualquer estação sísmica (daí o nome "primária"). A partícula do meio vibra na mesma direção em que a onda se propaga, como uma sanfona sendo comprimida e esticada. Justamente por ser um mecanismo de compressão, a onda P se propaga em **sólido, líquido e gás** — qualquer meio resiste a ser comprimido.
- **Onda S (secundária ou cisalhante)** — mais lenta que a P (por isso chega em segundo lugar), com a partícula vibrando perpendicularmente à direção de propagação, como uma corda balançada. O ponto crucial: a onda S depende de o meio resistir a **cisalhamento** (a deformação de "torção" lateral). **Líquidos não resistem a cisalhamento** — é essa a definição física de líquido, na prática: ele escoa em vez de voltar à forma. Por isso a onda S **não se propaga em líquido**. Esse único fato, como logo se verá, é a evidência mais forte que existe sobre o estado físico do núcleo externo.

**Ondas de superfície** — geradas quando a energia das ondas de corpo chega à superfície e se propaga apenas ao longo dela, sem penetrar fundo:

- **Onda Rayleigh** — combina movimento vertical e horizontal, um rolamento elíptico parecido com uma onda do mar.
- **Onda Love** — puramente horizontal, perpendicular à direção de propagação.

Ambas viajam mais devagar que as ondas de corpo, mas carregam mais energia por unidade de área na superfície — por isso são, em geral, as mais destrutivas num terremoto sentido por pessoas. Para o propósito desta aula, porém, o protagonismo é das ondas de corpo: são elas que atravessam o interior e por isso são elas que revelam a estrutura profunda.

A velocidade de cada onda de corpo não é arbitrária — depende de duas propriedades físicas do material que ela atravessa: a **incompressibilidade** (o módulo K, quanto o material resiste a mudar de volume sob pressão) e a **rigidez** (o módulo μ, quanto resiste a mudar de forma, isto é, a cisalhamento) e a densidade (ρ). Em termos simplificados:

- V_P depende de K, μ e ρ juntos.
- V_S depende só de μ e ρ.

É por isso que a onda S, dependendo exclusivamente da rigidez, simplesmente deixa de existir onde μ = 0 — que é a definição de um líquido ideal. Guarde essa relação: ela é o motivo técnico por trás de toda a lógica das zonas de sombra, adiante.

### Como a onda entrega a informação: refração, reflexão e o nome das fases

Uma onda sísmica não viaja em linha reta indiferente ao que atravessa. Duas coisas acontecem:

1. **Reflexão e refração em interfaces.** Quando a onda encontra uma superfície onde a velocidade sísmica muda abruptamente (uma **descontinuidade**), parte da energia reflete de volta e parte refrata — atravessa, mas mudando de direção. O ângulo de refração obedece à mesma lógica da óptica, a **lei de Snell**: o raio se dobra em direção à camada mais lenta e se afasta da normal na mais rápida (ou o inverso, dependendo do sentido). É exatamente esse dobramento e essa reflexão parcial que permitem detectar uma descontinuidade sem vê-la: ela aparece como uma chegada extra de energia numa estação sismográfica, num tempo que não seria esperado se o meio fosse uniforme.
2. **Curvatura por gradiente contínuo de velocidade.** Mesmo onde não há uma interface abrupta, a velocidade sísmica cresce gradualmente com a profundidade (pressão crescente, em geral, endurece o material). Isso curva os raios sísmicos suavemente, sempre na direção da camada mais rápida — o mesmo princípio físico que faz a luz se curvar numa miragem sobre asfalto quente.

Sismólogos batizam cada trajeto possível de uma onda com um código de letras — a **nomenclatura de fases**. Não é necessário memorizar o sistema inteiro; para acompanhar o resto da aula, bastam poucos exemplos, sempre lidos como uma sequência de trechos da viagem:

- **P** e **S** — a onda direta, do foco à estação, sem refletir em nada.
- **PP** — uma onda P que refletiu uma vez na superfície da Terra no meio do caminho.
- **PcP** — uma onda P que refletiu na fronteira manto–núcleo (o "c" é de *core*) e voltou.
- **PKP** — uma onda P que entrou no núcleo (K, de *Kern*, núcleo em alemão), atravessou-o e saiu de novo como P.
- **PKIKP** — uma onda P que atravessou o núcleo externo, entrou no núcleo interno (o segundo "I", de *inner*) como onda P, e retornou pelo mesmo caminho.
- **PKiKP** — uma onda P refletida na superfície do núcleo interno (o "i" minúsculo indica reflexão nessa fronteira), sem penetrá-lo.

Cada letra é um segmento de trajetória documentado. O motivo de essa notação existir é prático: cada fase chega numa estação em um tempo previsível *se* o modelo de camadas estiver certo. Quando a chegada observada bate com a prevista, o modelo se sustenta; quando não bate, o modelo precisa mudar. Foi assim, e não por adivinhação, que o interior da Terra foi mapeado.

### As três descobertas que fixaram os grandes limites

**Mohorovičić, 1909 — o limite crosta–manto.** Andrija Mohorovičić, sismólogo croata, estudou o sismo de Pokupsko, próximo a Zagreb, em outubro de 1909. Ao examinar os sismogramas de estações a diferentes distâncias do epicentro, notou algo que não deveria acontecer se a Terra fosse um meio uniforme: em certas estações, **chegavam dois trens de onda P** — um mais lento, que veio direto por uma camada superficial, e um mais rápido, que claramente tinha viajado por um caminho mais profundo e mais veloz antes de retornar à superfície. A única explicação consistente era a existência de uma camada abaixo, onde a onda P viaja mais rápido — ou seja, uma **descontinuidade de velocidade** logo abaixo da crosta. Esse é o raciocínio, não apenas o nome: uma dupla chegada de onda é a assinatura de uma interface de velocidade. Essa interface hoje se chama **descontinuidade de Mohorovičić**, a Moho — o mesmo limite crosta–manto já apresentado na aula anterior, agora com o método que o revelou.

**Gutenberg, 1913 — o limite manto–núcleo.** Beno Gutenberg refinou análises anteriores (incluindo a de R. D. Oldham, que já suspeitava de um núcleo distinto por volta de 1906) e determinou, com boa precisão para a época, a profundidade da fronteira manto–núcleo em torno de **2.900 km**. O raciocínio partiu, de novo, de padrões anômalos nos tempos de chegada: a existência de uma zona onde certas ondas simplesmente não chegam onde deveriam (a zona de sombra, detalhada a seguir) só se explica por uma queda brusca de velocidade numa profundidade específica — e essa profundidade é o limite manto–núcleo.

**Inge Lehmann, 1936 — o núcleo interno.** A dinamarquesa Inge Lehmann observou algo que o modelo de "núcleo único e líquido" não explicava: dentro da própria zona de sombra da onda P (região onde, pelo modelo então aceito, nenhuma onda P deveria chegar), instrumentos ainda registravam chegadas de energia, fracas mas reais. A explicação que ela propôs — e que se sustentou — foi que existe uma **segunda descontinuidade dentro do núcleo**, mais interna, onde a onda refrata de novo e consegue escapar da zona de sombra. Essa descontinuidade interna é o limite entre núcleo externo e **núcleo interno**. A confirmação definitiva de que esse núcleo interno é **sólido** veio depois, consolidada por décadas de trabalho subsequente com fases como PKiKP (reflexão na superfície do núcleo interno) e PKIKP (transmissão através dele) — fases cuja existência e cujo comportamento só fazem sentido se ali houver um sólido.

Repare no padrão comum às três descobertas: nenhuma delas foi "olhar para dentro da Terra". Todas foram inferência à melhor explicação (o método da Aula 02 do Módulo 01) aplicada a uma anomalia nos tempos e nos trajetos de ondas sísmicas.

### As zonas de sombra: a evidência mais direta que existe

Se um terremoto ocorre em um ponto da Terra, e se espalham estações sismográficas por todo o globo, a que distâncias angulares do epicentro (medidas em graus ao longo da superfície, de 0° a 180°) cada tipo de onda deveria, em princípio, ser detectada?

**A zona de sombra da onda S.** Além de aproximadamente **103°** de distância epicentral, a onda S direta simplesmente desaparece dos sismogramas — em toda a região que vai de ~103° até o lado oposto do planeta (180°). Como visto acima, a onda S não se propaga em líquido. A única explicação para essa ausência total, e não parcial, é que o **núcleo externo é líquido**: qualquer trajeto de onda S que precisasse atravessar essa camada é bloqueado ali, e nunca chega ao outro lado. Esta é a evidência clássica e mais citada para o estado físico do núcleo externo — vale registrar que ela é uma prova de ausência de propagação, não de "algo que a barra".

**A zona de sombra da onda P — e o erro que ela convida a cometer.** Entre aproximadamente **103° e 143°** de distância epicentral, a onda P direta também praticamente desaparece. Mas atenção: a causa aqui **não é bloqueio**, é **refração**. A onda P se propaga em líquido — ela consegue entrar no núcleo externo perfeitamente. O que acontece é que, ao cruzar o limite manto–núcleo, a velocidade da onda P **cai abruptamente** (o núcleo externo líquido conduz a onda P mais devagar que a base do manto rochoso). Por Snell, essa queda de velocidade dobra o raio de forma tão acentuada que ele é desviado para uma faixa de ângulos que simplesmente pula a região entre 103° e 143° — como um raio de luz entrando na água em ângulo raso, que se dobra para dentro. A onda P não some: ela é redirecionada, e reaparece além de 143°, chegando atrasada e com trajeto alterado (as fases PKP, PKIKP mencionadas antes). Distinguir essas duas zonas de sombra — uma por ausência real de propagação, outra por geometria de refração — é o ponto mais importante tecnicamente desta aula, e volta na seção de erros comuns.

### O que mais a sismologia revela: descontinuidades menores

Além dos três grandes limites (Moho, manto–núcleo, núcleo interno–externo), a sismologia resolve estruturas mais sutis:

- **Zona de baixa velocidade (LVZ)** — uma faixa no manto superior, próxima à base da litosfera, onde as velocidades sísmicas caem ligeiramente. Interpreta-se como uma região próxima do ponto de fusão parcial da rocha, mais dúctil — coerente com o que a Aula 03 do Módulo 01 já descreveu como a astenosfera fluindo por *creep* em estado sólido.
- **LAB (fronteira litosfera–astenosfera)** — o limite mecânico, não composicional, entre a placa rígida e o manto dúctil abaixo dela. É detectado por sismologia porque a rigidez muda ali, ainda que a composição da rocha possa ser essencialmente a mesma dos dois lados.
- **Descontinuidades de ~410 km e ~660 km** — dois saltos de velocidade dentro do manto, hoje interpretados não como mudanças de composição química, mas como **transições de fase** do mesmo material: sob pressão crescente, a olivina (mineral dominante do manto superior) se reorganiza cristalograficamente em **wadsleyita** perto de 410 km, depois em **ringwoodita** mais profundo, e por volta de 660 km se decompõe em **bridgmanita** (o mineral mais abundante da Terra, quimicamente um silicato de magnésio e ferro em estrutura de perovskita) mais **ferropericlásio**. A transição em 660 km é **endotérmica** (absorve calor) — o que significa que ela resiste à passagem de material através dela, um detalhe relevante para entender por que placas subductadas por vezes "empacam" naquela profundidade, tema que volta no módulo de tectônica.
- **Camada D″** — uma região heterogênea e ainda debatida na base do manto, logo acima do limite com o núcleo externo, onde as propriedades sísmicas mudam de forma complexa e lateralmente variável.

### Tomografia sísmica: do modelo em camadas ao modelo em volume

Tudo descrito até aqui — Moho, limite manto–núcleo, zonas de sombra, descontinuidades de 410 e 660 km — compõe um **modelo unidimensional**: a velocidade sísmica em função apenas da profundidade, como se a Terra fosse perfeitamente esférica e homogênea em cada camada. O modelo de referência mais usado desse tipo é o **PREM** (*Preliminary Reference Earth Model*), publicado em 1981, que resume décadas de dados sísmicos globais numa única curva de velocidade por profundidade.

Mas a Terra real tem variação lateral: uma placa fria afundando é mais rápida sismicamente que o manto ao redor, na mesma profundidade; uma pluma quente é mais lenta. A **tomografia sísmica** explora exatamente essa variação: usando milhares de terremotos e milhares de estações, e medindo minúsculos desvios no tempo de chegada de cada raio em relação ao previsto pelo modelo 1-D, é possível resolver, por inversão matemática, um **modelo tridimensional** de anomalias de velocidade dentro da Terra. É assim que se produzem as imagens, hoje familiares em livros didáticos, de placas subductadas ("slabs" frios) afundando no manto, ou de grandes anomalias de baixa velocidade perto da base do manto sob a África e o Pacífico.

É essencial não superinterpretar essas imagens. Tomografia é uma **inversão** — um problema matemático de reconstrução a partir de dados indiretos e incompletos, análogo (mas não idêntico) a uma tomografia médica. A resolução não é uniforme: é boa onde há muitos terremotos e muitas estações cruzando o volume (por exemplo, sob zonas de subducção densamente monitoradas) e é pobre onde a cobertura de raios é escassa (grandes áreas oceânicas, certas profundidades). Uma anomalia de velocidade também não diz, sozinha, se a causa é temperatura, composição ou a presença de um pouco de fundido — essa interpretação exige informação adicional.

## Exemplo trabalhado

**Problema.** Uma estação sismográfica registra a chegada da onda P e, alguns segundos depois, a chegada da onda S do mesmo terremoto. A diferença de tempo entre as duas chegadas é **Δt(S−P) = 40 segundos**. Assumindo, para o manto superior raso, velocidades aproximadas de **V_P ≈ 8 km/s** e **V_S ≈ 4,5 km/s**, a que distância epicentral está essa estação? E por que uma única estação não basta para localizar o terremoto?

*Passo 1 — montar a equação.* As duas ondas partem juntas, no mesmo instante, do foco. Cada uma leva um tempo diferente para percorrer a mesma distância *d* até a estação:

- Tempo da onda P: t_P = d / V_P
- Tempo da onda S: t_S = d / V_S

A diferença observada é: Δt = t_S − t_P = d/V_S − d/V_P = d · (1/V_S − 1/V_P)

*Passo 2 — calcular o fator.*

1/V_S = 1 / 4,5 = 0,2222 s/km
1/V_P = 1 / 8 = 0,1250 s/km
1/V_S − 1/V_P = 0,2222 − 0,1250 = 0,0972 s/km

*Passo 3 — isolar e calcular a distância.*

d = Δt / 0,0972 = 40 / 0,0972 ≈ **411 km**

Conferindo: t_P = 411 / 8 ≈ 51,4 s; t_S = 411 / 4,5 ≈ 91,3 s; diferença = 91,3 − 51,4 ≈ 39,9 s ≈ 40 s. A conta fecha.

*Passo 4 — por que uma estação só dá um círculo, não um ponto.* O cálculo acima informa **a distância** entre a estação e o foco — não a direção. Isso define um **círculo** de raio 411 km ao redor da estação (na superfície, para um foco raso), sobre o qual o epicentro pode estar em qualquer ponto. Uma segunda estação, com seu próprio Δt(S−P), define um segundo círculo, e a interseção dos dois já reduz as possibilidades a no máximo dois pontos. Uma **terceira estação**, com um terceiro círculo, resolve a ambiguidade e fecha o ponto — esse é o procedimento de **triangulação** (mais precisamente, trilateração, já que o que se mede são distâncias, não ângulos) usado na prática para localizar terremotos.

*Passo 5 — por que epicentro antes de hipocentro.* O procedimento acima, com Δt(S−P) e trilateração em três ou mais estações, localiza primeiro o **epicentro** — a projeção na superfície do ponto onde o sismo se originou — porque a geometria mais simples (distância medida ao longo da superfície) resolve diretamente essa posição horizontal. Encontrar o **hipocentro** (o foco real, em profundidade) exige informação adicional: tipicamente, o formato preciso das curvas de tempo de percurso em função da profundidade, o uso de múltiplas fases sísmicas, ou redes de estações densas o bastante para restringir a componente vertical. Por isso a profundidade de um terremoto costuma ter incerteza maior do que sua posição epicentral, e por isso a prática usual — e o que sismólogos fazem primeiro — é ancorar o epicentro e refinar o hipocentro depois, com mais dados.

## Erros comuns

- **Achar que a zona de sombra da onda P é bloqueio, igual à da onda S.** É sedutor porque as duas "zonas de sombra" têm o mesmo nome e o mesmo sintoma — ondas que somem dos sismogramas numa faixa de distâncias — então a mente generaliza a mesma causa para as duas. Mas a causa é oposta: a onda S some porque **não pode existir** no líquido; a onda P some porque é **desviada geometricamente** por refração ao entrar num meio mais lento. A onda P nunca deixou de se propagar — ela só não chega naquela faixa específica de ângulos.
- **Concluir que "a onda S não passa" prova que o núcleo inteiro é líquido.** É sedutor porque a evidência da onda S é tão limpa e categórica que parece justificar uma conclusão igualmente categórica. Mas a onda S ausente prova apenas que existe líquido *em algum lugar do caminho* — no caso, o **núcleo externo**. A existência do núcleo interno sólido foi estabelecida por uma linha de evidência diferente e posterior (Lehmann, 1936, e as fases PKiKP/PKIKP), não pela ausência da onda S.
- **Confundir magnitude do terremoto com o que a onda revela sobre a estrutura interna.** É sedutor porque magnitude é o número mais divulgado sobre um terremoto, e por isso a mente tende a tratá-lo como a variável relevante em qualquer discussão sísmica. Mas magnitude mede a **energia liberada na fonte** — é uma propriedade do evento, não do meio que a onda atravessa depois. O que revela a estrutura interna são os **tempos de chegada, as trajetórias e as amplitudes relativas** das fases em diferentes estações, algo que se mede tanto num sismo grande quanto num pequeno, desde que haja instrumentação suficiente.
- **Tratar um mapa de tomografia sísmica como uma fotografia direta do interior.** É sedutor porque a imagem final se parece com um corte de tecido em exame médico, com cores nítidas e contornos definidos, e essa familiaridade visual sugere um retrato fiel. Mas é o resultado de uma **inversão matemática** sobre dados esparsos e desigualmente distribuídos: a resolução varia por região e profundidade, e uma anomalia colorida não distingue, por si só, entre causa térmica, composicional ou a presença de fundido parcial.

## O que não concluir

- Que a sismologia dá uma resolução uniforme do interior da Terra. A cobertura de raios sísmicos depende de onde ocorrem terremotos e onde existem estações — por isso regiões com sismicidade e monitoramento densos (bordas de placas convergentes, por exemplo) são bem mais resolvidas do que grandes áreas oceânicas ou certas profundidades específicas.
- Que o PREM e outros modelos 1-D descrevem a Terra real ponto a ponto. Eles são **médias globais** — úteis como referência e como primeira aproximação, mas a Terra real tem variação lateral considerável em cada profundidade, que é exatamente o que a tomografia tenta capturar.
- Que as descontinuidades de 410 e 660 km marcam mudança de composição química do manto. A interpretação corrente é de **transição de fase** — o mesmo material (essencialmente olivina e seus polimorfos de alta pressão) reorganizando sua estrutura cristalina sob pressão crescente, não uma nova rocha entrando em cena. Isso segue sendo estudado; variações regionais na profundidade exata dessas descontinuidades são discutidas na literatura como indício de temperatura ou composição um pouco distintas localmente.
- Que a camada D″, na base do manto, tem uma natureza bem estabelecida e consensual. Ela é sismicamente complexa e heterogênea, e sua origem — se está ligada a acumulação de material subductado, a uma transição de fase adicional em minerais como a pós-perovskita, ou a outra causa — segue em discussão ativa na pesquisa atual.
- Que localizar um epicentro com poucas estações dá uma posição exata e sem incerteza. Mesmo com trilateração bem-sucedida, os valores de velocidade usados (como os V_P e V_S aproximados do exemplo) são simplificações de um meio que varia lateralmente; localizações reais de agências sismológicas trazem elipses de incerteza, não pontos exatos.

## Recap relâmpago

- O interior da Terra é inacessível a perfuração direta: o furo mais profundo (Kola SG-3, ~12.262 m) mal arranha os 6.371 km de raio médio. A sismologia funciona como tomógrafo indireto.
- **Onda P** (compressional, mais rápida, passa por sólido/líquido/gás) e **onda S** (cisalhante, mais lenta, **não passa por líquido**) são as ondas de corpo; **Rayleigh** e **Love** são as ondas de superfície, mais lentas e mais destrutivas.
- Reflexão, refração (lei de Snell) e curvatura por gradiente de velocidade são o que permite inferir descontinuidades a partir de tempos de chegada anômalos.
- **Mohorovičić (1909)** inferiu a Moho a partir de dupla chegada de onda P; **Gutenberg (1913)** fixou o limite manto–núcleo (~2.900 km); **Lehmann (1936)** inferiu o núcleo interno a partir de chegadas anômalas dentro da zona de sombra de P.
- **Zona de sombra da onda S** (além de ~103°): prova que o **núcleo externo é líquido**. **Zona de sombra da onda P** (~103° a ~143°): efeito de **refração**, não de bloqueio — a onda P entra no líquido, só é desviada.
- Descontinuidades adicionais: LVZ e LAB no manto superior; **~410 km** (olivina → wadsleyita) e **~660 km** (ringwoodita → bridgmanita + ferropericlásio, transição endotérmica); camada **D″** na base do manto.
- O **PREM** (1981) é o modelo de referência 1-D; a **tomografia sísmica** produz modelos 3-D por inversão, com resolução desigual — não é uma fotografia.
- Localizar um sismo usa Δt(S−P) por estação para achar a distância, e **três estações** (trilateração) para achar o **epicentro**; o **hipocentro** (profundidade) exige informação adicional.

## Próxima aula

[[02-sistema-terra-tectonica-aula-02-camadas-da-terra-modelo|Aula 02 — O modelo em camadas: da crosta ao núcleo interno]], que converte o método sismológico desta aula no modelo resultante, com as profundidades, espessuras e propriedades físicas de cada camada.

## Fontes

- Ondas sísmicas, fases e nomenclatura — [IRIS/EarthScope, Seismic Waves](https://www.iris.edu/hq/inclass/downloads/seismic_waves), [USGS, Seismic Waves](https://www.usgs.gov/programs/earthquake-hazards/science/seismic-waves)
- Mohorovičić e a descontinuidade de Moho — [Mohorovičić discontinuity (Wikipedia)](https://en.wikipedia.org/wiki/Mohorovi%C4%8Di%C4%87_discontinuity), [Andrija Mohorovičić (Britannica)](https://www.britannica.com/biography/Andrija-Mohorovicic)
- Gutenberg e o limite manto–núcleo — [Core–mantle boundary (Wikipedia)](https://en.wikipedia.org/wiki/Core%E2%80%93mantle_boundary), [Beno Gutenberg (Britannica)](https://www.britannica.com/biography/Beno-Gutenberg)
- Inge Lehmann e o núcleo interno — [Inge Lehmann (Wikipedia)](https://en.wikipedia.org/wiki/Inge_Lehmann), [Earth's Inner Core (USGS)](https://www.usgs.gov/faqs/what-are-earths-layers-and-are-they-solid-or-liquid)
- Zonas de sombra sísmicas — [Seismic Shadow Zone (OpenGeology, Historical Geology)](https://opengeology.org/historicalgeology/), [IRIS, Shadow Zone teaching resources](https://www.iris.edu/hq/inclass)
- Descontinuidades de 410 e 660 km, transições de fase — [Mantle transition zone (Wikipedia)](https://en.wikipedia.org/wiki/Mantle_transition_zone), citado sem link específico: Ringwood, A. E. (mineralogia do manto)
- PREM e tomografia sísmica — [Preliminary reference Earth model (Wikipedia)](https://en.wikipedia.org/wiki/Preliminary_reference_Earth_model) (Dziewonski & Anderson, 1981), [Seismic tomography (Wikipedia)](https://en.wikipedia.org/wiki/Seismic_tomography)
- Kola Superdeep Borehole — [Kola Superdeep Borehole (Wikipedia)](https://en.wikipedia.org/wiki/Kola_Superdeep_Borehole)

<!--
mapa_objetivo_secao:
  OA-01a: "O problema: um planeta que não se pode abrir"
  OA-01b: "Ondas sísmicas: como a energia de um terremoto viaja" + "Como a onda entrega a informação: refração, reflexão e o nome das fases"
  OA-01c: "As três descobertas que fixaram os grandes limites" + "Exemplo trabalhado"
  OA-01d: "As zonas de sombra: a evidência mais direta que existe"

alegacoes_auditaveis:
  - claim_id: GEO-M02-A01-KOLA-001
    claim: "O furo Kola Superdeep Borehole (SG-3) atingiu cerca de 12.262 m de profundidade, o mais profundo já perfurado."
    risk: numero
    source: "Wikipedia/Kola Superdeep Borehole"
    confianca: alta
  - claim_id: GEO-M02-A01-RAIO-TERRA-002
    claim: "O raio médio da Terra é de 6.371 km."
    risk: numero
    source: "valor padrão de referência geodésica"
    confianca: alta
  - claim_id: GEO-M02-A01-ONDAS-003
    claim: "Onda P é compressional e a mais rápida, propaga-se em sólido/líquido/gás; onda S é cisalhante, mais lenta, não se propaga em líquido; ondas Rayleigh e Love são de superfície e mais lentas que as de corpo."
    risk: mecanismo
    source: "sismologia clássica, consolidado"
    confianca: alta
  - claim_id: GEO-M02-A01-MODULOS-004
    claim: "V_P depende de incompressibilidade (K), rigidez (μ) e densidade; V_S depende apenas de rigidez e densidade, anulando-se quando μ = 0 (líquido)."
    risk: mecanismo
    source: "sismologia clássica, consolidado"
    confianca: alta
  - claim_id: GEO-M02-A01-MOHOROVICIC-005
    claim: "Andrija Mohorovičić identificou em 1909, a partir do sismo de Pokupsko próximo a Zagreb (outubro de 1909), a dupla chegada de onda P que revelou a descontinuidade da Moho."
    risk: historico
    source: "Wikipedia/Mohorovičić discontinuity; Britannica"
    confianca: alta
  - claim_id: GEO-M02-A01-GUTENBERG-006
    claim: "Beno Gutenberg determinou em 1913 a profundidade do limite manto-núcleo em torno de 2.900 km (valor moderno ~2.891 km), refinando trabalho anterior de Oldham (~1906)."
    risk: numero
    source: "Wikipedia/Core-mantle boundary; Britannica"
    confianca: alta
    nota: "valor de 2.900 km é aproximação de referência amplamente citada; será detalhado com maior precisão no módulo 20 (geofísica), conforme pendência registrada em _contexto.md (M01-F04)"
  - claim_id: GEO-M02-A01-LEHMANN-007
    claim: "Inge Lehmann propôs em 1936 a existência do núcleo interno, a partir de chegadas anômalas de energia dentro da zona de sombra de onda P."
    risk: historico
    source: "Wikipedia/Inge Lehmann"
    confianca: alta
  - claim_id: GEO-M02-A01-SOMBRA-S-008
    claim: "A zona de sombra da onda S começa em aproximadamente 103° de distância epicentral e se estende até o lado oposto do planeta, evidenciando núcleo externo líquido."
    risk: numero
    source: "sismologia clássica; valor de referência amplamente citado (IRIS/USGS)"
    confianca: alta
  - claim_id: GEO-M02-A01-SOMBRA-P-009
    claim: "A zona de sombra da onda P vai de aproximadamente 103° a 143° de distância epicentral, por efeito de refração na entrada do núcleo, não por bloqueio."
    risk: numero
    source: "sismologia clássica; valor de referência amplamente citado (alguns textos usam ~140°-142°)"
    confianca: media
    nota: "o limite superior exato (140° a 143°) varia ligeiramente entre fontes didáticas; usar como faixa aproximada"
  - claim_id: GEO-M02-A01-DESCONT-410-010
    claim: "A descontinuidade sísmica próxima de 410 km de profundidade corresponde à transição de fase olivina → wadsleyita."
    risk: numero
    source: "Wikipedia/Mantle transition zone; petrologia de alta pressão consolidada"
    confianca: alta
  - claim_id: GEO-M02-A01-DESCONT-660-011
    claim: "A descontinuidade sísmica próxima de 660 km de profundidade corresponde à decomposição da ringwoodita em bridgmanita + ferropericlásio, reação endotérmica."
    risk: numero
    source: "Wikipedia/Mantle transition zone; petrologia de alta pressão consolidada"
    confianca: alta
  - claim_id: GEO-M02-A01-PREM-012
    claim: "O PREM (Preliminary Reference Earth Model) foi publicado em 1981 por Dziewonski e Anderson como modelo de referência 1-D da Terra."
    risk: historico
    source: "Wikipedia/Preliminary reference Earth model"
    confianca: alta
  - claim_id: GEO-M02-A01-EXEMPLO-VELOCIDADES-013
    claim: "Velocidades aproximadas usadas no exemplo trabalhado: V_P ≈ 8 km/s e V_S ≈ 4,5 km/s no manto superior raso."
    risk: numero
    source: "valores de referência didáticos fornecidos como aproximação; variam regionalmente e com profundidade"
    confianca: media
  - claim_id: GEO-M02-A01-EXEMPLO-DISTANCIA-014
    claim: "Com Δt(S-P) = 40 s e as velocidades aproximadas acima, a distância epicentral calculada é de aproximadamente 411 km."
    risk: numero
    source: "cálculo aritmético direto a partir dos valores do próprio exemplo, conferido no passo 3"
    confianca: alta
  - claim_id: GEO-M02-A01-DDOISLINHAS-015
    claim: "A camada D'' na base do manto é sismicamente heterogênea e sua natureza (subducção acumulada, pós-perovskita, ou outra causa) segue em discussão ativa."
    risk: controverso
    source: "apresentado explicitamente como não consensual"
    confianca: media
-->
