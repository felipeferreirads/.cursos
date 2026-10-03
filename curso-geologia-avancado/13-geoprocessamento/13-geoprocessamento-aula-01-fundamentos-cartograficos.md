# Aula 01: Fundamentos cartográficos: geoide, datum, sistemas de coordenadas, projeções e escala

**ID:** geologia-avancado-m13-a01
**Módulo:** [[13-geoprocessamento-modulo|Módulo 13 — Geoprocessamento]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** explicar por que a Terra não cabe num plano sem distorção, e como geoide, datum, sistema de coordenadas e projeção resolvem esse problema em cadeia — até a escolha do sistema de referência de um projeto de geoprocessamento.
**Ao final você vai conseguir:** distinguir elipsoide de geoide e explicar o que um datum fixa; converter entre coordenadas geográficas e planas (UTM); escolher a projeção e o datum adequados a um projeto brasileiro de geociências; e calcular a escala de um mapa a partir de uma distância medida em campo.
**Pré-requisito:** nenhum específico deste curso — esta aula assume apenas noções gerais de geometria e de mapas topográficos, comuns a qualquer formação em geociências.

## Conteúdo

### Por que a cartografia é o alicerce do geoprocessamento

Este módulo abre uma área nova do curso — Métodos quantitativos e geoinformação — e o primeiro problema que qualquer projeto de geoprocessamento enfrenta não é de software, é de geodésia: como representar uma superfície curva, irregular e tridimensional (a Terra) num plano bidimensional (a tela ou o papel) sem que a distorção invalide as medidas que serão feitas em cima dele. Todo erro cometido aqui — um datum errado, uma projeção inadequada — se propaga silenciosamente por todo o projeto: o software sobrepõe as camadas sem reclamar, o mapa parece correto, e só um deslocamento de dezenas a centenas de metros entre uma camada e outra revela o problema, geralmente tarde demais. Por isso esta aula é a fundação do módulo inteiro: as seis aulas seguintes assumem que você sabe, ao abrir qualquer base de dados espacial, perguntar "em que sistema de referência isso está?" antes de perguntar qualquer outra coisa.

### Elipsoide e geoide: dois modelos para uma Terra irregular

A Terra não é uma esfera nem um elipsoide perfeito — é uma superfície irregular, com massa distribuída de forma não uniforme, que a geodésia aproxima por dois modelos complementares.

O **elipsoide de referência** é uma figura geométrica regular (um elipsoide de revolução, achatado nos polos) que aproxima a forma geral da Terra e serve de superfície matemática de cálculo — é sobre ele que se definem as coordenadas geográficas (latitude e longitude). Diferentes elipsoides foram ajustados ao longo do tempo, alguns por regiões (como o antigo Hayford/Internacional 1924, usado no Brasil pelo SAD69) e outros de abrangência global, calculados a partir de dados de satélite (como o **GRS80**, adotado pelo sistema geodésico brasileiro atual, e o **WGS84**, usado pelo GPS).

O **geoide**, por sua vez, é a superfície equipotencial do campo de gravidade terrestre que mais se aproxima do nível médio dos mares — uma superfície irregular, "ondulada", porque a gravidade varia com a distribuição de massa (mais densa sob uma cadeia de montanhas ou uma bacia sedimentar profunda, por exemplo). O geoide é o que define fisicamente "altitude": quando se diz que um ponto está a 850 m de altitude, essa altitude é medida a partir do geoide (altitude ortométrica), não do elipsoide. A diferença entre as duas superfícies em cada ponto é a **ondulação geoidal** (N), que pode ser positiva ou negativa e varia por dezenas de metros ao longo de um território de dimensão continental: no modelo oficial brasileiro MAPGEO2015 (IBGE/EPUSP), as isolinhas de ondulação geoidal são traçadas de 5 em 5 m ao longo de uma faixa da ordem de -30 m a +30 m, conforme a região. Não é, portanto, uma correção desprezível: ignorá-la inviabiliza qualquer levantamento altimétrico, sobretudo ao combinar altitude de GPS/GNSS (que mede em relação ao elipsoide, altitude geométrica *h*) com altitude de referência de nível (ortométrica, *H*) — as duas se relacionam, em boa aproximação, por *h* = *H* + *N*.

```
Elipsoide vs. geoide (corte esquemático, exagero vertical)

              geoide (ondulado, segue a gravidade)
         ___╱‾‾╲___________________╱‾╲______
        ╱                                    ╲
───────╱──────────────────────────────────────╲─────── elipsoide (liso, matemático)
                    N = ondulação geoidal
                    (altitude elipsoidal - altitude ortométrica)
```
A legenda a reter: o elipsoide é a superfície de cálculo de coordenadas horizontais; o geoide é a referência física de altitude — e a diferença entre eles (N) precisa ser somada ou subtraída ao converter entre os dois tipos de altitude.

### Datum: o que fixa o modelo à Terra real

Um elipsoide sozinho é só uma forma abstrata — ele precisa ser posicionado e orientado em relação à Terra real para virar utilizável. Essa amarração é o **datum geodésico**: um conjunto que define o elipsoide de referência, seu ponto de origem (ou, nos data modernos, geocêntricos) e sua orientação, permitindo calcular coordenadas concretas de qualquer ponto.

Existem dois tipos historicamente relevantes no Brasil. Os **data clássicos**, ajustados topograficamente a um ponto de origem específico sobre o território (como o **SAD69** — South American Datum 1969, com origem no vértice Chuá, em Minas Gerais, e elipsoide de referência UGGI-67/GRS67, de semieixo maior 6.378.160 m; não confundir com o datum brasileiro anterior, o **Córrego Alegre**, esse sim assentado no elipsoide Internacional de Hayford, 1924), eram calculados sem apoio de satélite e por isso têm precisão limitada e não são geocêntricos. Os **data geocêntricos modernos**, calculados por técnicas de posicionamento por satélite e centrados no centro de massa da Terra, são hoje o padrão: o **SIRGAS2000** (Sistema de Referência Geocêntrico para as Américas, elipsoide GRS80), adotado oficialmente no Brasil em 2005 (Resolução IBGE/PR nº 1/2005) e, encerrado o período de transição de dez anos em 25 de fevereiro de 2015 (Resolução IBGE/PR nº 1/2015), único sistema de referência válido no Sistema Geodésico Brasileiro e no Sistema Cartográfico Nacional desde então; e o **WGS84** (World Geodetic System 1984), usado internacionalmente pelo GPS. SIRGAS2000 e WGS84 têm definição praticamente coincidente — tanto que não há parâmetros oficiais de transformação publicados entre eles —, mas não são intercambiáveis quando se busca precisão: o SIRGAS2000 é um referencial **estático**, com coordenadas congeladas na época de referência 2000,4, enquanto o WGS84 acompanha o ITRF, que é **dinâmico**. Como a placa Sul-Americana desloca o território brasileiro a pouco mais de 1 cm por ano para noroeste, a diferença entre as duas realizações cresce continuamente desde 2000 e hoje já é da ordem de decímetros (abaixo de 0,5 m). Um projeto de precisão precisa, portanto, declarar não apenas qual dos dois está usando, mas em que época as coordenadas estão referidas.

São quatro nomes num parágrafo só, e vale consolidá-los antes de seguir — é esta tabela, não o parágrafo, que você quer ter na cabeça ao abrir um arquivo de origem desconhecida:

| Datum | Elipsoide | Geocêntrico? | Situação no Brasil |
|---|---|---|---|
| Córrego Alegre | Internacional de Hayford, 1924 | não (topocêntrico) | histórico — em uso de ~1950 a ~1970 |
| SAD69 | UGGI-67 / GRS67 | não (topocêntrico, origem no vértice Chuá, MG) | legado — base de boa parte do acervo cartográfico antigo |
| SIRGAS2000 | GRS80 | sim | único válido no SGB/SCN desde 25/02/2015; estático, época 2000,4 |
| WGS84 | WGS84 (praticamente igual ao GRS80) | sim | referencial do GPS; dinâmico, acompanha o ITRF |

O ponto prático mais importante desta seção: **dois pontos com as mesmas coordenadas numéricas, mas datum diferente, não são o mesmo ponto no terreno**. A diferença entre SAD69 e SIRGAS2000, por exemplo, é da ordem de 60 a 70 m na maior parte do território brasileiro — deslocamento pequeno o bastante para passar despercebido numa inspeção visual do mapa, e grande o bastante para invalidar a delimitação de uma área de pesquisa mineral, o cruzamento de um poço com uma seção sísmica, ou a locação de um afloramento em campo.

### Sistemas de coordenadas: geográficas e planas (projetadas)

Com o datum fixado, um ponto na superfície pode ser localizado de duas formas. As **coordenadas geográficas** (latitude e longitude, expressas em graus, minutos e segundos ou em graus decimais) localizam o ponto diretamente sobre a superfície curva do elipsoide — são o sistema "nativo" da geodésia, mas inconvenientes para medir distâncias e áreas diretamente, porque o comprimento de um grau de longitude muda com a latitude.

As **coordenadas planas** (ou projetadas), como as coordenadas UTM (Universal Transversa de Mercator), resultam de projetar matematicamente a superfície curva sobre um plano, permitindo trabalhar com distâncias e áreas em metros, de forma direta, como numa planta cartesiana comum. O sistema UTM divide o globo em 60 fusos de 6° de longitude cada, cada um com sua própria origem local de coordenadas — o **falso leste** e o **falso norte** são constantes somadas a essas coordenadas justamente para que nenhum ponto do fuso caia com valor negativo. O Brasil, por sua extensão em longitude, atravessa vários fusos (do 18 ao 25, aproximadamente) — um projeto que abrange mais de um fuso exige decidir se usa UTM (com cuidado nas bordas de fuso) ou uma projeção alternativa, como a Cônica Conforme de Lambert, mais adequada a áreas alongadas em longitude.

### Projeções cartográficas: a distorção inevitável e como escolhê-la

Toda projeção cartográfica — a passagem matemática da superfície curva do elipsoide para um plano — introduz distorção em pelo menos uma das três propriedades geométricas: forma (conformidade), área (equivalência) ou distância (equidistância); nenhuma projeção preserva as três ao mesmo tempo, teorema geométrico conhecido desde Gauss. A escolha da projeção, portanto, é sempre um compromisso guiado pelo uso do mapa:

- **Projeções conformes** (preservam ângulos e forma local, como a UTM, baseada na Transversa de Mercator) são a escolha padrão para mapeamento topográfico e geológico de detalhe, onde a forma correta das feições importa mais que a área exata.
- **Projeções equivalentes** (preservam área, como a Albers) são preferíveis para análises que comparam áreas entre regiões — por exemplo, mapas de densidade mineral ou de uso do solo em escala regional a continental.
- **Projeções equidistantes** preservam distâncias a partir de um ponto ou ao longo de linhas específicas, úteis em mapas de navegação ou de alcance.

No Brasil, a prática consolidada para geociências é usar **UTM/SIRGAS2000** para trabalhos em escala local a regional dentro de um único fuso, e projeções cônicas (como Policônica ou Lambert) para mapas de abrangência nacional que atravessam muitos fusos, onde a distorção do UTM nas bordas se tornaria inaceitável.

### Escala: a razão entre mapa e terreno

A **escala cartográfica** é a razão entre uma distância medida no mapa e a distância real correspondente no terreno, expressa como fração (1:50.000, lida "um para cinquenta mil") — significando que 1 unidade de medida no mapa corresponde a 50.000 dessa mesma unidade no terreno. Escalas **grandes** (frações com denominador pequeno, como 1:1.000) mostram mais detalhe numa área menor — típicas de mapeamento de detalhe, plantas de mina, cadastro urbano; escalas **pequenas** (denominador grande, como 1:1.000.000) mostram menos detalhe numa área maior — típicas de mapas geológicos regionais ou nacionais. A escala determina diretamente a **resolução espacial** aceitável dos dados de entrada de um projeto de SIG: não faz sentido produzir um mapa em escala 1:25.000 a partir de uma base cadastrada apenas em 1:250.000, porque a precisão posicional da base original simplesmente não sustenta o detalhe implícito na escala maior — um princípio que retorna, com outra roupagem, quando o Módulo tratar de resolução de modelos digitais de elevação (Aula 06).

## Exemplo trabalhado

**Situação:** um geólogo está planejando um levantamento de campo numa área localizada majoritariamente no fuso UTM 23S (SIRGAS2000), no estado de Minas Gerais. Ele recebe do cliente um shapefile de propriedade antigo, com coordenadas em SAD69, fuso 23S, e precisa sobrepor essa camada à sua base atual em SIRGAS2000 para checar se o polígono da propriedade coincide com os limites observados em campo. Além disso, ele quer expressar a escala de trabalho: no mapa impresso, 4 cm correspondem a 1 km no terreno. Qual é a escala do mapa, e por que a sobreposição direta das duas camadas (sem reprojeção) é um erro?

**Resolução:**

*Parte 1 — cálculo da escala.* A escala é a razão distância no mapa : distância no terreno, com as duas medidas na mesma unidade. Convertendo 1 km para centímetros: 1 km = 100.000 cm. A razão é:

Escala = distância no mapa / distância no terreno = 4 cm / 100.000 cm = 1 / 25.000

O mapa está na escala **1:25.000** — cada 1 cm no papel representa 25.000 cm (250 m) no terreno, escala típica de mapeamento geológico de semidetalhe.

*Parte 2 — o erro de sobrepor SAD69 e SIRGAS2000 sem reprojeção.* SAD69 e SIRGAS2000 são data distintos, com origens e elipsoides diferentes (SAD69: elipsoide UGGI-67/GRS67, origem topocêntrica no vértice Chuá; SIRGAS2000: elipsoide GRS80, geocêntrico). Um ponto com as mesmas coordenadas numéricas UTM nos dois sistemas corresponde, no terreno real, a dois locais fisicamente diferentes, deslocados tipicamente 60 a 70 m em Minas Gerais (a direção e a magnitude exatas do deslocamento variam regionalmente e são tabeladas pelo IBGE). Se o geólogo simplesmente carregar o shapefile antigo e a base atual no mesmo projeto sem reprojetar um deles para o mesmo datum, o software os desenhará sobrepostos sem qualquer aviso — a distorção é silenciosa — mas o polígono da propriedade aparecerá deslocado dezenas de metros do que está realmente em campo. Em escala 1:25.000, um deslocamento de 65 m corresponde a 2,6 mm no mapa impresso: pequeno o bastante para não saltar aos olhos, grande o bastante para colocar erroneamente um afloramento dentro ou fora do polígono de propriedade. A solução correta é reprojetar (transformar de datum) a camada mais antiga para SIRGAS2000 antes de qualquer análise conjunta, usando os parâmetros de transformação publicados pelo IBGE — nunca assumir que "mesma UTM, mesmo fuso" significa "mesmo lugar".

## Erros comuns

- **Confundir altitude do GPS (elipsoidal) com altitude ortométrica de nível.** As duas diferem pela ondulação geoidal N, que no Brasil chega a dezenas de metros — usar uma pela outra sem somar/subtrair N produz erro de altimetria, não de posição.
- **Achar que "mesma UTM, mesmo fuso" garante "mesmo lugar".** É exatamente o erro do exemplo trabalhado: coordenadas numericamente iguais em datum diferente descrevem pontos físicos deslocados dezenas a centenas de metros, e o software sobrepõe as camadas sem avisar.
- **Tratar SIRGAS2000 e WGS84 como perfeitamente intercambiáveis por não haver parâmetros oficiais de transformação entre eles.** A ausência de parâmetros reflete a proximidade de definição, não a identidade — como um é estático e o outro dinâmico, a divergência cresce com o tempo e já soma décimos de metro.
- **Escolher a projeção pelo software padrão em vez de pelo uso do mapa.** UTM é conforme e ótima para forma local, mas distorce área — usá-la para comparar áreas entre regiões distantes (em vez de uma equivalente como Albers) introduz erro sistemático que a "aparência correta" do mapa esconde.

## O que não concluir

- **Que um datum mais moderno é sempre "mais certo" no sentido absoluto.** SAD69 não está errado — é topocêntrico e de precisão mais baixa por não ter apoio de satélite, mas segue sendo o sistema de origem de boa parte do acervo cartográfico histórico, que precisa ser reprojetado, não descartado.
- **Que escala grande é "melhor" que escala pequena.** Escala grande mostra mais detalhe numa área menor; a escala certa depende do propósito do mapa e da resolução real dos dados de entrada — usar escala maior que a base sustenta cria falsa precisão, não mais qualidade.
- **Que a ondulação geoidal é um erro de medição a corrigir uma vez e esquecer.** É uma propriedade física real e variável regionalmente (documentada ponto a ponto no MAPGEO2015); ignorá-la sistematicamente, não só uma vez, é o que compromete um levantamento altimétrico.

## Recap relâmpago

- O elipsoide é o modelo geométrico regular usado para calcular coordenadas horizontais; o geoide é a superfície física de referência de altitude, ondulada porque segue a gravidade; a diferença entre os dois é a ondulação geoidal (N), que no Brasil vai de cerca de -30 m a +30 m conforme a região (MAPGEO2015) e liga as altitudes geométrica e ortométrica por *h* = *H* + *N*.
- O datum amarra o elipsoide à Terra real; data clássicos (Córrego Alegre, com elipsoide de Hayford 1924; SAD69, com elipsoide UGGI-67/GRS67) são topocêntricos e não geocêntricos, enquanto data modernos (SIRGAS2000, WGS84) são geocêntricos e calculados por satélite — o SIRGAS2000 foi adotado em 2005 e é o único datum válido no Brasil desde o fim do período de transição, em 25/02/2015.
- Coordenadas com o mesmo valor numérico em datum diferente representam locais físicos diferentes — a diferença SAD69/SIRGAS2000 é da ordem de 60-70 m no Brasil, deslocamento silencioso e potencialmente crítico.
- Coordenadas geográficas (lat/long) localizam pontos sobre a superfície curva; coordenadas projetadas (UTM) resultam de uma projeção para o plano, permitindo medir distância e área diretamente em metros.
- Toda projeção distorce forma, área ou distância — nenhuma preserva as três; a escolha (conforme, equivalente, equidistante) depende do uso do mapa. UTM/SIRGAS2000 é o padrão brasileiro para trabalho local a regional dentro de um fuso.
- Escala é a razão distância no mapa : distância no terreno (mesma unidade); ela também limita o detalhe que os dados de entrada de um projeto de SIG podem sustentar de forma confiável.

## Próxima aula

[[13-geoprocessamento-aula-02-ambiente-sig-estruturas-vetorial-e-matricial|Aula 02 — Ambiente SIG, estruturas vetorial e matricial e organização de bases de dados espaciais]]

## Fontes

- IBGE, Resolução do Presidente nº 1/2005, de 25/02/2005 (adoção do SIRGAS2000 e período de transição de dez anos) e Resolução do Presidente nº 1/2015, de 25/02/2015 (término do período de transição; SIRGAS2000 como único sistema de referência do SGB e do SCN).
- IBGE/EPUSP (2015), *MAPGEO2015 — Modelo de Ondulação Geoidal do Brasil*, cartograma e documentação técnica (faixa de valores de N no território brasileiro).
- Snyder, J. P. (1987), *Map Projections — A Working Manual*, USGS Professional Paper 1395, cap. 1-4 (fundamentos de projeção, UTM).
- IOGP (2023), *EPSG Geodetic Parameter Dataset*, registros SAD69 (EPSG:4618, elipsoide GRS 1967 modificado / UGGI-67), Córrego Alegre (elipsoide Internacional 1924) e SIRGAS2000 (EPSG:4674, elipsoide GRS80).

<!--
nivel: avancado
palavras_corpo: 2390  # recontado apos auditoria + revisao didatica (2026-09-08)
mapa_objetivo_secao:
  geologia-avancado-m13-oa01: "Por que a cartografia é o alicerce do geoprocessamento" + "Elipsoide e geoide: dois modelos para uma Terra irregular" + "Datum: o que fixa o modelo à Terra real" + "Sistemas de coordenadas: geográficas e planas (projetadas)" + "Projeções cartográficas: a distorção inevitável e como escolhê-la" + "Escala: a razão entre mapa e terreno" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOPROC-M13-A01-ELIPGEOIDE-001
    claim: "O elipsoide de referência é uma superfície geométrica regular usada para cálculo de coordenadas horizontais; o geoide é a superfície equipotencial do campo de gravidade que mais se aproxima do nível médio dos mares e serve de referência para altitude ortométrica; a diferença entre as duas superfícies em um ponto é a ondulação geoidal (N), relacionada às altitudes por h = H + N. No Brasil, o modelo oficial MAPGEO2015 representa valores de N positivos e negativos, numa faixa da ordem de -30 m a +30 m conforme a região."
    risk: fato
    source: "Snyder 1987, Map Projections, cap. 1; IBGE/EPUSP 2015, MAPGEO2015 — Modelo de Ondulação Geoidal do Brasil (cartograma, isolinhas de 5 em 5 m)"
    audit_note: "Corrigido na auditoria do Módulo 13 (achado GEOPROC-M13-A01-ONDULACAO-007): a versão original afirmava faixa de -5 m a -10 m, muito abaixo da amplitude real e com sinal único."
  - claim_id: GEOPROC-M13-A01-DATUM-002
    claim: "SAD69 (South American Datum 1969) é um datum clássico, topocêntrico, não geocêntrico, com origem no vértice Chuá (MG) e elipsoide de referência UGGI-67/GRS67 (semieixo maior 6.378.160 m) — o elipsoide Internacional de Hayford 1924 é o do datum brasileiro anterior, Córrego Alegre; SIRGAS2000 é um datum geocêntrico moderno com elipsoide GRS80, adotado no Brasil em 2005 (Res. IBGE/PR 1/2005) e único válido desde o fim do período de transição em 25/02/2015 (Res. IBGE/PR 1/2015); WGS84 é o datum geocêntrico usado internacionalmente pelo GPS, de definição praticamente coincidente com a do SIRGAS2000, mas dinâmico (acompanha o ITRF) contra o SIRGAS2000 estático na época 2000,4 — divergência hoje da ordem de decímetros, abaixo de 0,5 m, pelo deslocamento de pouco mais de 1 cm/ano da placa Sul-Americana."
    risk: fato
    source: "IBGE, Res. PR 1/2005 e 1/2015; IOGP EPSG Geodetic Parameter Dataset (EPSG:4618 SAD69, EPSG:4674 SIRGAS2000); IBGE, Projeto Mudança do Referencial Geodésico (velocidade da placa Sul-Americana)"
    audit_note: "Corrigido na auditoria do Módulo 13 (achados GEOPROC-M13-A01-DATUM-002 [vermelho, elipsoide do SAD69], GEOPROC-M13-A01-SIRGASWGS-008 e GEOPROC-M13-A01-OFICIALIZACAO-009)."
  - claim_id: GEOPROC-M13-A01-DESLOC-003
    claim: "A diferença de coordenadas entre SAD69 e SIRGAS2000 no território brasileiro é da ordem de 60 a 70 metros na maior parte do território, variando regionalmente."
    risk: aproximacao
    source: "IBGE, parâmetros de transformação SAD69-SIRGAS2000 (ordem de grandeza consolidada na literatura geodésica brasileira); valor exato depende da região e deve ser consultado nos parâmetros oficiais do IBGE para uso de precisão"
  - claim_id: GEOPROC-M13-A01-UTM-004
    claim: "O sistema UTM divide o globo em 60 fusos de 6 graus de longitude cada; o território brasileiro se estende aproximadamente entre os fusos 18 e 25."
    risk: fato
    source: "Snyder 1987, Map Projections, cap. 4 (Transversa de Mercator/UTM)"
  - claim_id: GEOPROC-M13-A01-PROJECAO-005
    claim: "Nenhuma projeção cartográfica preserva simultaneamente forma, área e distância; projeções são classificadas como conformes (preservam forma/ângulos, ex. UTM), equivalentes (preservam área, ex. Albers) ou equidistantes (preservam distância a partir de um ponto ou ao longo de linhas específicas)."
    risk: fato
    source: "Snyder 1987, Map Projections, cap. 1-3"
  - claim_id: GEOPROC-M13-A01-ESCALA-006
    claim: "Escala cartográfica é a razão entre a distância medida no mapa e a distância real correspondente no terreno, expressas na mesma unidade; escalas grandes (denominador pequeno) mostram mais detalhe em área menor, escalas pequenas (denominador grande) mostram menos detalhe em área maior."
    risk: fato
    source: "Convenção cartográfica padrão, consistente com Snyder 1987 e normas de cartografia sistemática (ET-ADGV / especificações técnicas de cartografia do Brasil)"
-->
