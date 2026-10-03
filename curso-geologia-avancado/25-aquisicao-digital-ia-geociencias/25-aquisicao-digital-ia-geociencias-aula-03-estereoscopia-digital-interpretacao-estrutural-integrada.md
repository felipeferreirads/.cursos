# Aula 03: Estereoscopia digital por anaglifos e interpretação estrutural integrada com MDT, sensoriamento remoto e aerogeofísica

**ID:** geologia-avancado-m25-a03
**Módulo:** [[25-aquisicao-digital-ia-geociencias-modulo|Módulo 25 — Aquisição de dados digitais e inteligência artificial em geociências]]
**Duração estimada:** ~29 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** interpretar estruturas geológicas de forma hierárquica (do lineamento regional ao elemento estrutural), usando a visão estereoscópica por anaglifo e integrando modelo digital de terreno (MDT), imagens de sensoriamento remoto e aerogeofísica, com critérios explícitos de confiança e sem cair nas armadilhas de iluminação e de exagero vertical.
**Ao final você vai conseguir:** explicar como um anaglifo produz a percepção de relevo e o que o exagero vertical faz com o mergulho aparente; organizar uma interpretação em quatro níveis hierárquicos; calcular a atitude de um contato geológico a partir de três pontos lidos no MDT; e calcular a orientação média de lineamentos com o tratamento correto de dados axiais.
**Pré-requisito:** [[25-aquisicao-digital-ia-geociencias-aula-02-tipos-organizacao-dados-geologicos|Aula 02]] (aerogeofísica como grid, e não como ponto), [[14-sensoriamento-remoto-modulo|Módulo 14]] e [[16-aerogeofisica-modulo|Módulo 16]]. Assume-se a notação de direção de mergulho e mergulho e o tratamento vetorial de orientações por **polos** (a normal ao plano), vistos na [[25-aquisicao-digital-ia-geociencias-aula-01-aquisicao-digital-campo-ferramentas-imagens-croquis|Aula 01]].

## Conteúdo

### Ver em relevo o que a tela mostra achatado

O olho humano percebe profundidade porque cada olho vê a cena de um ponto ligeiramente diferente, e o cérebro interpreta a diferença como distância. A fotogrametria e a fotointerpretação clássicas exploram isso com **pares estereoscópicos**: duas fotos aéreas do mesmo terreno, tiradas de posições diferentes ao longo da linha de voo, com sobreposição, de modo que cada olho veja uma delas. A diferença de posição de um mesmo objeto nas duas imagens é a **paralaxe**, e ela é proporcional à altura do objeto em relação ao datum: o topo de uma serra se desloca mais entre as imagens do que o fundo do vale.

O **anaglifo** é a versão que dispensa aparelho: as duas imagens são coloridas em cores complementares (em geral vermelho para uma e ciano para a outra) e sobrepostas numa única imagem. Com óculos de lentes vermelha e ciana, cada lente deixa passar só a imagem de sua cor, cada olho vê uma, e o relevo emerge. A vantagem geológica é prática: qualquer tela e uma lente de papel bastam para examinar a topografia em três dimensões.

A estereoscopia **digital** amplia o alcance porque o par estéreo pode ser construído a partir do modelo digital de terreno: cada pixel de uma imagem (uma ortoimagem de satélite, um hillshade, uma composição de bandas) é deslocado lateralmente em proporção à sua altitude, uma vez para cada olho, e as duas imagens deslocadas formam o anaglifo. Assim se obtém relevo para uma cena que nunca foi fotografada em estéreo, e pode-se **drapejar** sobre o relevo a geologia, a geofísica ou a geoquímica.

Duas propriedades do anaglifo pedem cuidado, e ambas afetam a interpretação estrutural:

- **Exagero vertical.** A estereoscopia faz o terreno parecer mais íngreme do que é, e o mergulho aparente das camadas ficar mais forte. Não é um efeito opcional que aparece só quando alguém mexe na paralaxe: num modelo estéreo a escala vertical raramente iguala a horizontal, e o quanto ela é exagerada depende da **geometria do par** — sobretudo da razão entre a distância que separa os dois pontos de vista e a altura de observação (a *razão base-altura*), além da distância focal e da sobreposição — e, no anaglifo construído a partir de um MDT, do fator de deslocamento escolhido. Consequência: **não se lê o valor do mergulho num anaglifo**. Ele serve para reconhecer **geometria** (direção das camadas, forma de dobras, deslocamento de contatos, relação de corte entre estruturas) e para estimar o sentido do mergulho, não para medir ângulos; os ângulos vêm do campo (Aula 01) ou da geometria calculada sobre o MDT (exemplo trabalhado 1).
- **Inversão de relevo (pseudoscopia).** Se as duas imagens forem trocadas entre os olhos, vales viram cristas. Uma verificação simples: confirmar com a rede de drenagem, que deve correr nos vales.

### As fontes de MDT e de imagens

Os modelos de elevação livres mais usados incluem o SRTM (missão da NASA, resolução de cerca de 30 m para a maior parte do globo), o Copernicus DEM GLO-30 (da ESA, 30 m), o ALOS World 3D / AW3D30 (da JAXA, 30 m) e, no Brasil, o TOPODATA do INPE, que refina os dados SRTM. Confirme as versões e as resoluções vigentes nos portais oficiais.

Uma armadilha muito comum merece nome: o produto que circula como "**ALOS PALSAR de 12,5 m**" (os pacotes de correção radiométrica de terreno do Alaska Satellite Facility) tem **espaçamento de pixel** de 12,5 m, mas o modelo de elevação que vem com ele foi **reamostrado a partir de fontes de 30 m** (SRTM 30 m, NED) — e o próprio ASF avisa, na documentação do produto, que esse arquivo serve para conferir o processamento e **não deve ser usado no lugar de um modelo de elevação comum**. Espaçamento de pixel não é resolução: reamostrar 30 m para 12,5 m não cria informação, só células menores. Para interpretação estrutural a diferença é decisiva, porque é a resolução real que decide o que aparece.

A **resolução limita o que se enxerga**: uma estrutura com largura menor que a célula não aparece. E há uma distinção de nome que vale fixar: um **modelo digital de superfície (MDS)** registra o topo do que existe — copa da vegetação e edificações incluídas —, enquanto um **modelo digital de terreno (MDT)** pretende entregar o solo nu. O SRTM, o Copernicus GLO-30 e o AW3D30 são, a rigor, **MDS**: em terreno florestado medem a copa, o que embaça o relevo estrutural exatamente onde a mata é densa. Na prática, portais e literatura usam "MDT" de modo frouxo para qualquer grade de altitude, e esta aula acompanha o uso corrente; mas quando o alvo é geometria de camada sob mata, confira qual dos dois você tem em mãos.

### A armadilha da iluminação

Ao gerar um relevo sombreado (*hillshade*) para interpretar, você escolhe o azimute do sol. Duas consequências. Primeiro, o convencional é iluminar do quadrante noroeste (azimute 315°), porque o olho humano lê melhor o relevo com a luz vindo do alto e da esquerda; com a luz vindo do lado oposto, pode ocorrer inversão de relevo percebida. Segundo, e mais grave para o estruturalista: **feições lineares perpendiculares à direção da iluminação são realçadas, e as paralelas ficam quase invisíveis**. Uma interpretação de lineamentos feita com um único azimute de sol mostra um viés de orientação que é do sol, e não do terreno. A prática defensável é interpretar com **vários azimutes** (por exemplo, quatro: 0°, 45°, 90°, 135°) e comparar.

### Interpretação hierárquica: quatro níveis

A palavra-chave do objetivo é **hierárquica**: a interpretação estrutural parte do geral e desce ao particular, e cada nível responde a uma pergunta diferente, com um dado diferente.

| Nível | Pergunta | Dados que dominam | Produto |
|---|---|---|---|
| 1. Lineamentos regionais | Que alinhamentos existem em escala regional? | MDT em pequena escala, aeromagnetometria, imagens de satélite | mapa de lineamentos e rosa de direções |
| 2. Domínios estruturais | Onde o padrão estrutural muda? | textura de relevo/drenagem, magnetometria (padrão de anomalias), gamaespectrometria | polígonos de domínios |
| 3. Elementos estruturais | Quais traços de foliação, charneiras e falhas, e como se relacionam? | anaglifo, imagem de detalhe, derivadas magnéticas | traços interpretados, relações de corte |
| 4. Verificação | O que o campo confirma? | medidas em afloramento (Aula 01) | atitudes, cinemática, calibração |

O termo **lineamento** tem definição precisa: feição linear mapeável, **simples ou composta**, de uma superfície, cujas partes se alinham numa relação retilínea ou levemente curva e que difere dos padrões das feições adjacentes, e que **presumivelmente expressa um fenômeno de subsuperfície** (O'Leary, Friedman & Pohn, 1976). Note o que a definição **não** diz: ela não afirma origem estrutural. "Fenômeno de subsuperfície" é deliberadamente mais largo — cabe contato litológico, dique, zona alterada. Ressalva essencial, portanto: **um lineamento é uma hipótese, não uma falha**. Rios seguem falhas, mas também seguem contatos litológicos, diques, fraturas de alívio e simples divisores.

### Integrar as três fontes: a lógica da coincidência

Cada fonte responde a uma propriedade diferente, e por isso a coincidência entre elas é informação:

- O **MDT** mostra a **expressão topográfica**: cristas, vales, ressaltos de erosão diferencial. É controlado pela resistência das rochas à erosão e pela drenagem.
- O **sensoriamento remoto** (bandas ópticas, radar) mostra a **cobertura da superfície**: vegetação, solo, umidade, alteração hidrotermal; contribui com o padrão de drenagem e com contrastes de cor/textura.
- A **aerogeofísica** mostra a **propriedade física em subsuperfície rasa**: a magnetometria, o contraste de suscetibilidade magnética; a gamaespectrometria, o teor de K, eTh e eU nos primeiros decímetros do solo. Para realçar bordas e feições lineares nos dados magnéticos usam-se filtros de derivada — os principais estão na nota abaixo.

> [!note] Os filtros magnéticos, e uma ressalva que quase todo mundo repete errado
> Os realces de borda mais usados em dados magnéticos são a **primeira derivada vertical**, o **sinal analítico** (Nabighian, 1972) e a **inclinação do sinal** (*tilt derivative*, Miller & Singh, 1994). O cálculo deles é dos [[16-aerogeofisica-modulo|Módulos 16]] e [[19-geofisica-exploracao-mineral-modulo|19]]; aqui você só precisa saber o que esperar de cada um e uma ressalva.
> Em baixas latitudes magnéticas (como no norte do Brasil), a redução ao polo é numericamente instável, e o sinal analítico costuma ser preferido. A justificativa que se ouve para isso, porém, é mais estreita do que se costuma dizer: a independência do sinal analítico em relação à direção de magnetização é propriedade do caso **bidimensional** tratado por Nabighian (1972). Para dados em **grade**, isto é, no caso tridimensional de qualquer levantamento aerogeofísico, a amplitude do sinal analítico **depende** da direção do campo ambiente e da direção de magnetização (Li, 2006). Ele **reduz**, não elimina, a dependência — e o resíduo aparece justamente em baixa latitude magnética e com magnetização remanente, que é o cenário em que ele foi escolhido. Guarde como ressalva a arquivar: a escolha prática continua certa, o argumento de sempre é que está pela metade.

Regra de confiança: um lineamento que aparece **só no relevo** pode ser drenagem ou litologia; um que aparece **só na magnetometria** pode ser um dique ou uma variação litológica; um que **coincide** no relevo, na magnetometria e em um deslocamento de contatos tem uma probabilidade muito maior de ser uma zona de falha ou de cisalhamento. Por isso convém que cada traço interpretado receba, no banco (Aula 02), um campo de **confiança** (alta, média, baixa) e outro de **fontes que o sustentam**. Isso é o equivalente, para dados interpretados, do campo "tipo de medida" da Aula 01.

Um contraste importante entre as fontes: o MDT e as imagens mostram a **superfície**, e a aerogeofísica **integra volume** (a magnetometria, em particular, responde a corpos em profundidade). Um lineamento magnético que não tem qualquer expressão topográfica não é um "erro": pode ser uma estrutura sob cobertura.

## Exemplo trabalhado 1: atitude de um contato a partir do MDT (problema dos três pontos)

**Situação.** Sobre a imagem e o MDT você traça um contato geológico planar (por exemplo, a base de uma camada de quartzito) e lê as coordenadas (leste, norte, cota, em metros) de três pontos do mesmo contato: **P1 (1000; 2000; 820)**, **P2 (1400; 2300; 760)**, **P3 (900; 2600; 700)**. Quais são o mergulho e a direção de mergulho do contato?

**Resolução.** Três pontos não colineares definem um plano. Obtêm-se dois vetores no plano, P1→P2 e P1→P3, e o produto vetorial deles dá a normal (o polo) do plano; a normal, orientada para cima, fornece o mergulho (o ângulo com a vertical) e a direção de mergulho (a direção horizontal oposta à projeção da normal).

```python
import numpy as np

pts = np.array([[1000.0, 2000.0, 820.0],
                [1400.0, 2300.0, 760.0],
                [ 900.0, 2600.0, 700.0]])
v1, v2 = pts[1] - pts[0], pts[2] - pts[0]
n = np.cross(v1, v2)
if n[2] < 0: n = -n                              # normal para cima
n /= np.linalg.norm(n)
dip = np.degrees(np.arccos(n[2]))
dd = np.degrees(np.arctan2(-n[0], -n[1])) % 360   # direção de mergulho
strike = (dd - 90) % 360                          # regra da mão direita
print("dip=%.1f  dip_direction=%.1f  strike(RHR)=%.1f" % (dip, dd, strike))
```

**Saída obtida:** `dip = 11,3°`, `direção de mergulho = 180,0°` e direção (rumo) pela regra da mão direita de `90,0°`. À mão: v1 = (400, 300, −60), v2 = (−100, 600, −120), produto vetorial = (0, 54.000, 270.000); a razão entre a componente horizontal e a vertical da normal, 54.000/270.000 = 0,2, dá arctan(0,2) = 11,3°, e a componente horizontal da normal aponta para o norte, logo o plano mergulha para o sul (180°).

**Interpretação.** O contato mergulha suavemente (11°) para o sul. Duas ressalvas de método: (i) o resultado só vale se os três pontos pertencem realmente ao **mesmo contato planar**, e a leitura de cota sobre MDT tem incerteza (em MDT de 30 m, alguns metros de erro vertical num intervalo de 60 a 120 m de desnível já mudam o mergulho em alguns graus); (ii) para mergulhos pequenos, como este, o erro relativo do mergulho é grande, o que é a razão de o valor calculado ser hipótese a confirmar no campo (nível 4).

## Exemplo trabalhado 2: orientação média de lineamentos (dados axiais)

**Situação.** Você interpretou dez lineamentos e mediu seus azimutes: 32, 41, 28, 205, 36, 47, 215, 30, 38 e 52 graus. Qual a direção média?

**Armadilha.** A média aritmética dá 72,4° e é **errada**: lineamentos são **dados axiais**, sem sentido (uma linha de azimute 205° é a mesma linha de 25°). Somar 205 e 215 com 32 e 41 mistura duas "voltas" do círculo.

**Solução.** Dobra-se o ângulo (a linha de 25° e a de 205° passam a valer 50° e 410° = 50°, ficando iguais), somam-se os vetores unitários e desdobra-se o resultado:

```python
az = np.array([32, 41, 28, 205, 36, 47, 215, 30, 38, 52])
theta = np.radians(2 * az)
C, S = np.cos(theta).sum(), np.sin(theta).sum()
media = (np.degrees(np.arctan2(S, C)) / 2) % 180
R = np.hypot(C, S) / len(az)
print("media axial: %.1f graus  |  R = %.3f" % (media, R))
```

**Saída obtida:** média axial de **36,3°** com **R = 0,961** (R próximo de 1 = lineamentos muito concentrados), contra os **72,4° da média ingênua**, um erro de 36°. A direção dominante é NE (cerca de N36E). Como o azimute de 205° equivale a 25° e o de 215° a 35°, todos os dez lineamentos ficam entre 25° e 52°: o enxame é coeso, e a média correta cai no meio dele, enquanto a média ingênua cai fora de todos os lineamentos.

**O que isso não prova.** Uma direção média coesa não garante origem estrutural comum, e pode refletir o viés de iluminação da seção anterior, se a interpretação foi feita com um único azimute de sol. A checagem é repetir a interpretação com outro azimute e comparar as rosas de direção.

## Recap relâmpago

- O **anaglifo** sobrepõe duas imagens em cores complementares; a **paralaxe** proporcional à altitude cria o relevo; pode ser construído a partir de um MDT.
- O anaglifo **exagera o relevo**: use-o para geometria e relações de corte, **não para ler mergulho**. Troca de imagens gera **inversão de relevo**.
- Ilumine com **vários azimutes**: lineamentos perpendiculares ao sol são realçados e os paralelos somem.
- **Espaçamento de pixel não é resolução** (o "ALOS PALSAR de 12,5 m" é reamostrado de 30 m), e **MDS não é MDT**: SRTM, Copernicus GLO-30 e AW3D30 medem a copa da vegetação, não o solo nu.
- A interpretação é **hierárquica**: lineamentos regionais, domínios, elementos estruturais, verificação de campo.
- **Lineamento é hipótese.** Confiança maior quando **MDT, sensoriamento e aerogeofísica coincidem**; registre no banco a confiança e as fontes de cada traço.
- Atitude de contato pelos **três pontos** (produto vetorial); direção de lineamentos é dado **axial**: use o **ângulo dobrado**.

## Próxima aula

[[25-aquisicao-digital-ia-geociencias-aula-04-bancos-dados-big-data-fair-reprodutibilidade|Aula 04 — Bancos de dados e Big Data em geociências]]: com dados de campo (Aula 01), dados analíticos (Aula 02) e interpretações (esta aula) em mãos, é hora de organizá-los num banco que outras pessoas, e você mesmo daqui a dois anos, consigam reencontrar e reutilizar.

## Fontes

- O'Leary, D. W., Friedman, J. D. & Pohn, H. A. (1976), "Lineament, linear, lineation: some proposed new standards for old terms", *Geological Society of America Bulletin*, 87(10), 1463-1469.
- Nabighian, M. N. (1972), "The analytic signal of two-dimensional magnetic bodies with polygonal cross-section: its properties and use for automated anomaly interpretation", *Geophysics*, 37(3), 507-517.
- Miller, H. G. & Singh, V. (1994), "Potential field tilt: a new concept for location of potential field sources", *Journal of Applied Geophysics*, 32, 213-217.
- Li, X. (2006), "Understanding 3D analytic signal amplitude", *Geophysics*, 71(2), L13-L16, DOI 10.1190/1.2184367: a amplitude do sinal analítico em três dimensões **não** é independente da direção de magnetização, ao contrário do caso bidimensional.
- Lillesand, T. M., Kiefer, R. W. & Chipman, J. W. (2015), *Remote Sensing and Image Interpretation*, 7ª ed., Wiley, ISBN 9781118343289: capítulos de fotogrametria e visão estereoscópica.
- Portais dos modelos de elevação: NASA/USGS (SRTM), ESA (Copernicus DEM GLO-30), JAXA (ALOS World 3D / AW3D30), INPE (TOPODATA), para versões e resoluções vigentes.
- Alaska Satellite Facility, *ALOS PALSAR Radiometric Terrain Correction — product guide* e *ALOS PALSAR Products* (docs.asf.alaska.edu/datasets/palsar): o modelo de elevação dos produtos de alta resolução é reamostrado de fontes de 30 m para o espaçamento de 12,5 m e não substitui um modelo de elevação regular.

<!--
nivel: avancado
palavras_corpo: 2443
mapa_objetivo_secao:
  geologia-avancado-m25-oa03: "Ver em relevo" + "As fontes de MDT" + "A armadilha da iluminação" + "Interpretação hierárquica" + "Integrar as três fontes" + "Exemplo trabalhado 1" + "Exemplo trabalhado 2"

alegacoes_auditaveis:
  - claim_id: DIGGEO-M25-A03-ANAGLIFO-PARALAXE-001
    claim: "Um anaglifo sobrepoe duas imagens em cores complementares (vermelho/ciano); a paralaxe entre as imagens e proporcional a altura do objeto em relacao ao datum; o par pode ser construido deslocando pixels de uma imagem em proporcao a altitude do MDT; a troca das imagens entre os olhos produz inversao de relevo (pseudoscopia)."
    risk: fato
    source: "VERIFICADO na auditoria de 2026-09-21 (passagem 2), item azul B14: Lillesand, T. M., Kiefer, R. W. & Chipman, J. W. (2015), Remote Sensing and Image Interpretation, 7a ed., Wiley, ISBN 9781118343289, capitulos de fotogrametria e visao estereoscopica. A proporcionalidade entre paralaxe e altura e EXATA no anaglifo construido por deslocamento de pixels a partir de um MDT (que e o caso que a aula constroi) e aproximada no par fotografico classico. ACHADO AMARELO 12 DA AUDITORIA: a edicao, que a lista de Fontes mandava 'conferir', ficou fixada na 7a (2015) - ver claim -LILLESAND-EDICAO-013."
  - claim_id: DIGGEO-M25-A03-EXAGERO-VERTICAL-002
    claim: "A visao estereoscopica exagera verticalmente o relevo, fazendo o mergulho aparente parecer maior; por isso o mergulho nao deve ser lido em anaglifo, que serve para geometria e relacoes de corte. O exagero e INTRINSECO a geometria do par estereo (razao base-altura, distancia focal, sobreposicao), nao um efeito opcional do ajuste de paralaxe."
    risk: fato
    source: "VERIFICADO na auditoria de 2026-09-21 (passagem 2): razao base-altura como determinante do exagero vertical no estereomodelo - Esri GIS Dictionary, verbete 'base-height ratio'; Photogrammetric Engineering (ASPRS), 'Vertical exaggeration in stereoscopic models' e 'Some factors causing vertical exaggeration and slope distortion', set. 1953; Lillesand, Kiefer & Chipman (2015), cap. de fotogrametria - a escala vertical do estereomodelo raramente iguala a horizontal e em geral a excede. NENHUM FATOR NUMERICO DE EXAGERO E AFIRMADO, em continuidade com a decisao do redator. Ver ACHADO LARANJA 11 (claim -EXAGERO-INTRINSECO-012)."
  - claim_id: DIGGEO-M25-A03-ILUMINACAO-VIES-003
    claim: "Em relevo sombreado, feicoes lineares perpendiculares a direcao de iluminacao sao realcadas e as paralelas atenuadas, o que introduz vies de orientacao na interpretacao de lineamentos com um unico azimute de sol; convencionalmente iluminacao a 315 graus; recomenda-se usar varios azimutes."
    risk: fato
    source: "VERIFICADO na auditoria de 2026-09-21. Convencao de 315 graus: documentacao oficial do ArcGIS Pro, 'How Hillshade works' (azimute padrao 315, altitude 45) e GDAL (gdal_raster_hillshade). Vies de iluminacao: literatura de extracao automatica de lineamentos - feicoes alongadas cuja direcao coincide com a direcao da luz ficam pouco visiveis ou invisiveis, e a pratica estabelecida e combinar varios azimutes (Multi-Hillshade Hierarchic Clustering; hillshade multidirecional, cuja implementacao GDAL/Imhof combina 225, 270, 315 e 360 graus). A aula sugere quatro azimutes como exemplo; o numero e didatico, nao normativo."
  - claim_id: DIGGEO-M25-A03-LINEAMENTO-DEFINICAO-004
    claim: "Lineamento e feicao linear mapeavel, simples ou composta, de uma superficie, cujas partes se alinham numa relacao retilinea ou levemente curva, que difere dos padroes das feicoes adjacentes e que presumivelmente expressa um FENOMENO DE SUBSUPERFICIE - a definicao nao afirma origem estrutural."
    risk: fato
    source: "VERIFICADO na auditoria de 2026-09-21: O'Leary, D. W., Friedman, J. D. & Pohn, H. A. (1976), 'Lineament, linear, lineation: some proposed new standards for old terms', GSA Bulletin 87(10), 1463-1469 (volume, numero e paginas conferem). Definicao como circula na literatura: 'a mappable, simple or composite linear feature of a surface, whose parts align in straight or slightly curving relationship and which differs distinctly from the pattern of adjacent features and presumably reflects a subsurface phenomenon'. ACHADO LARANJA 6 DA AUDITORIA de 2026-09-21: a redacao original trocava 'fenomeno de subsuperficie' por 'origem presumivelmente estrutural', estreitando a definicao e contradizendo a propria ressalva seguinte da aula (rios seguem tambem contatos litologicos, diques e fraturas de alivio). Corrigido, com os termos 'simples ou composta' restituidos."
  - claim_id: DIGGEO-M25-A03-DERIVADAS-MAGNETICAS-005
    claim: "Primeira derivada vertical, sinal analitico (Nabighian 1972) e inclinacao do sinal/tilt derivative (Miller & Singh 1994) sao filtros usados para realcar bordas e feicoes lineares em dados magneticos; em baixas latitudes magneticas a reducao ao polo e instavel e o sinal analitico, que nao depende da direcao de magnetizacao, e preferido."
    risk: fato
    source: "REFERENCIAS VERIFICADAS na auditoria de 2026-09-21: Nabighian, M. N. (1972), 'The analytic signal of two-dimensional magnetic bodies with polygonal cross-section: its properties and use for automated anomaly interpretation', Geophysics 37(3), 507-517, DOI 10.1190/1.1440276 (volume, numero e paginas conferem; o artigo define a funcao analitica cuja parte real e a derivada horizontal e a imaginaria a derivada vertical do perfil, sendo esta a transformada de Hilbert daquela). Miller, H. G. & Singh, V. (1994), 'Potential field tilt - a new concept for location of potential field sources', J. Appl. Geophys. 32, 213-217, DOI 10.1016/0926-9851(94)90022-1 (confere; o tilt e definido pela razao entre a primeira derivada vertical e o gradiente horizontal, positivo sobre a fonte e negativo fora, e o artigo o compara ao sinal analitico e a outras medidas de deteccao de borda). A independencia do sinal analitico em relacao a direcao de magnetizacao e a instabilidade da reducao ao polo em baixas latitudes magneticas seguem como conhecimento consolidado de geofisica de campos potenciais, coerente com os dois artigos e com os Modulos 16 e 19 do curso."
  - claim_id: DIGGEO-M25-A03-MDT-FONTES-006
    claim: "SRTM (~30 m, NASA), Copernicus DEM GLO-30 (ESA, 30 m), ALOS World 3D / AW3D30 (JAXA, 30 m) e TOPODATA (INPE, refinamento do SRTM) sao fontes livres de modelo de elevacao. O produto distribuido como 'ALOS PALSAR de 12,5 m' (pacotes RTC do Alaska Satellite Facility) tem ESPACAMENTO DE PIXEL de 12,5 m, mas seu modelo de elevacao e reamostrado de fontes de 30 m (SRTM 30 m, NED): espacamento de pixel nao e resolucao."
    risk: fato
    source: "VERIFICADO na auditoria de 2026-09-21: documentacao do Alaska Satellite Facility (docs.asf.alaska.edu/datasets/palsar; ASF RTC product guide v1.2; ALOS PALSAR RTC User Guide, NASA Earthdata) - 'high resolution RTC products from medium resolution DEMs are upsampled from the 30-m version to 12.5 m', produtos hi-res com pixel de 12,5 m gerados de NED13 (alta) e SRTM 30 m / NED1 / NED2 (media), e advertencia explicita de que o DEM empacotado 'should not be used in place of a regular DEM' porque a correcao geoidal altera os valores de altitude. ACHADO LARANJA 4 DA AUDITORIA de 2026-09-21: a redacao original listava 'ALOS PALSAR em resolucao de cerca de 12,5 m' como fonte livre de MDT ao lado de produtos de 30 m, numa aula cujo proprio argumento e que 'a resolucao limita o que se enxerga' - a omissao tornava a afirmacao enganosa como escrita. Corrigido, com AW3D30 (o produto JAXA legitimo de 30 m) no lugar e a armadilha nomeada."
  - claim_id: DIGGEO-M25-A03-MDS-VS-MDT-009
    claim: "Modelo digital de superficie (MDS) registra o topo do que existe, inclusive copa de vegetacao e edificacoes; modelo digital de terreno (MDT) pretende entregar o solo nu. SRTM, Copernicus GLO-30 e AW3D30 sao, a rigor, MDS, e em terreno florestado medem a copa."
    risk: fato
    source: "Distincao terminologica padrao em geoprocessamento e sensoriamento remoto (DSM vs DTM/DEM), coerente com os Modulos 13 e 14 do curso; os tres produtos citados derivam de radar interferometrico ou estereoscopia optica que registram a primeira superficie refletora. ACHADO LARANJA 5 DA AUDITORIA de 2026-09-21: a redacao original dizia 'MDT e, em geral, um modelo de superficie', que e contradicao nos proprios termos e confundia as duas siglas justamente onde o aluno precisa distingui-las. Corrigido definindo as duas e declarando que a aula acompanha o uso frouxo corrente de 'MDT' para qualquer grade de altitude."
  - claim_id: DIGGEO-M25-A03-PREREQ-ESTEREOGRAMA-010
    claim: "O pre-requisito que esta aula toma da Aula 01 e a notacao de direcao de mergulho e mergulho e o tratamento vetorial de orientacoes por polos - NAO a leitura de estereogramas."
    risk: fato
    source: "Verificacao direta contra o arquivo do proprio curso, 25-...-aula-01-....md, em 2026-09-21: a Aula 01 ensina notacao de dip direction/dip e a media vetorial por polos (Exemplo trabalhado 2), e NAO apresenta, desenha nem ensina a ler estereograma nenhum. ACHADO AMARELO 7 DA AUDITORIA de 2026-09-21: o cabecalho dizia 'Assume-se a leitura de estereogramas de mergulho e direcao de mergulho vista na Aula 01', creditando a aula anterior um conteudo que ela nao tem. Corrigido para o que a Aula 01 de fato entrega. Este e o quarto modulo consecutivo (22, 23, 24, 25) em que a citacao interna ao proprio curso e ponto de falha - ver dominant_pattern no course-state.yaml."
  - claim_id: DIGGEO-M25-A03-TRES-PONTOS-007
    claim: "Para P1 (1000;2000;820), P2 (1400;2300;760), P3 (900;2600;700): v1=(400,300,-60), v2=(-100,600,-120), produto vetorial=(0,54000,270000), dip=arctan(54000/270000)=11.3 graus, direcao de mergulho 180 graus, direcao (RHR) 90 graus."
    risk: calculo
    source: "Aritmetica direta e execucao do codigo (Python, NumPy), 2026-09-21."
  - claim_id: DIGGEO-M25-A03-MEDIA-AXIAL-008
    claim: "Para os azimutes 32,41,28,205,36,47,215,30,38,52 a media axial pelo angulo dobrado e 36.3 graus com R=0.961, enquanto a media aritmetica ingenua (72.4 graus) e errada por tratar dados axiais como direcionais."
    risk: calculo
    source: "Execucao direta do codigo (Python, NumPy), 2026-09-21. REEXECUTADO e reproduzido digito a digito na auditoria de 2026-09-21 (passagem 2), item azul B17."
  - claim_id: DIGGEO-M25-A03-SINAL-ANALITICO-3D-011
    claim: "A independencia do sinal analitico em relacao a direcao de magnetizacao vale no caso BIDIMENSIONAL (Nabighian 1972); para dados em grade, isto e, no caso TRIDIMENSIONAL de um levantamento aerogeofisico, a amplitude do sinal analitico DEPENDE da direcao do campo ambiente e da direcao de magnetizacao (Li 2006). O sinal analitico reduz, mas nao elimina, essa dependencia, e o residuo aparece justamente em baixa latitude magnetica e com magnetizacao remanente."
    risk: fato
    source: "VERIFICADO na auditoria de 2026-09-21 (passagem 2): Li, X. (2006), 'Understanding 3D analytic signal amplitude', Geophysics 71(2), L13-L16, DOI 10.1190/1.2184367 - demonstra que a amplitude do sinal analitico NAO e independente da direcao do campo ambiente nem da direcao de magnetizacao no caso 3D geral, ao contrario do caso 2D. Ver tambem 'Reducing the dependence of the analytic signal amplitude of aeromagnetic data on the source vector direction' (Geophysics, DOI 10.1190/geo2013-0319.1) e a literatura de interpretacao de campo total em baixas latitudes magneticas. ACHADO LARANJA 8 DA AUDITORIA de 2026-09-21: a redacao original afirmava, sem qualificacao e exatamente no contexto de baixa latitude magnetica, que o sinal analitico 'independe da direcao de magnetizacao'. A PASSAGEM 1 DESTA AUDITORIA ACEITOU essa frase como 'conhecimento consolidado de geofisica de campos potenciais' sem verifica-la (ver claim -DERIVADAS-MAGNETICAS-005): a propriedade 2D apresentada como geral e o erro. Corrigido com a distincao 2D/3D e a ressalva de que a preferencia pratica continua valida."
  - claim_id: DIGGEO-M25-A03-EXAGERO-INTRINSECO-012
    claim: "O exagero vertical do modelo estereoscopico e propriedade intrinseca da geometria do par (razao base-altura, distancia focal, sobreposicao) e, no anaglifo derivado de MDT, do fator de deslocamento escolhido - NAO um efeito que so aparece quando a paralaxe e ajustada para realcar o relevo."
    risk: fato
    source: "VERIFICADO na auditoria de 2026-09-21 (passagem 2), mesmas fontes do claim -EXAGERO-VERTICAL-002. ACHADO LARANJA 11 DA AUDITORIA de 2026-09-21: a redacao original punha o exagero entre parenteses como condicional ('sobretudo com a paralaxe ajustada para realcar o relevo'), o que ensina que um anaglifo 'nao ajustado' entregaria mergulho confiavel - contradizendo a instrucao correta que a propria aula da duas linhas abaixo. Corrigido nomeando o mecanismo, sem afirmar fator numerico."
  - claim_id: DIGGEO-M25-A03-LILLESAND-EDICAO-013
    claim: "A referencia de Lillesand, Kiefer & Chipman usada na aula e a 7a edicao (2015), Wiley, ISBN 9781118343289."
    risk: fato
    source: "VERIFICADO na auditoria de 2026-09-21 (passagem 2): Wiley, pagina da 7a edicao (ISBN 9781118343289); registros de catalogo concordantes. ACHADO AMARELO 12 DA AUDITORIA de 2026-09-21: a lista de Fontes publicava a instrucao editorial 'Wiley; conferir a edicao', isto e, uma nota do redator para a auditoria exposta ao aluno como se fosse parte da referencia - nao citavel, e sinaliza incerteza onde nao havia. Corrigido com edicao, ano e ISBN."
-->
