# Aula 05: Tratamento e interpretação de dados: diagramas de Piper, Stiff e Schoeller e o modelo hidrogeoquímico conceitual

**ID:** geologia-avancado-m02-a05
**Módulo:** [[02-hidrogeoquimica-modulo|Módulo 02 — Hidrogeoquímica]]
**Duração estimada:** ~29 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** interpretar diagramas de Piper, Stiff e Schoeller para classificar a fácies hidroquímica de uma água e construir, a partir de um conjunto de amostras, o modelo hidrogeoquímico conceitual de um sistema aquífero.

## Antes de começar, você precisa saber

- Unidades meq/L e balanço iônico (Aula 01).
- Processos de mineralização e a sequência de Chebotarev (Aula 02).
- Sistemas de fluxo local/intermediário/regional (Módulo 01, Aula 03).

## Conteúdo

### Fácies hidroquímica: dando nome à composição

Antes de qualquer diagrama, o primeiro passo interpretativo é nomear a **fácies hidroquímica** de uma amostra: os dois íons dominantes (um cátion, um ânion) em base de meq/L, na ordem de abundância. Por convenção, dominante significa responder por mais de 50% da soma de cátions (ou de ânions) em meq/L; quando nenhum íon isolado ultrapassa 50%, a água é classificada como **mista** entre os dois maiores constituintes (ex.: "mista cálcio-magnesiana bicarbonatada"). Exemplos de nomenclatura: água **bicarbonatada cálcica** (Ca²⁺ e HCO₃⁻ dominantes — típica de recarga recente em terreno carbonático ou silicático pouco evoluído), água **cloretada sódica** (Na⁺ e Cl⁻ dominantes — típica de água muito evoluída, evaporítica ou afetada por intrusão salina).

Essa nomenclatura já resume boa parte da história da água (Aula 02), mas os diagramas a seguir permitem comparar dezenas de amostras simultaneamente e revelar padrões espaciais e evolutivos que a nomenclatura isolada não mostra.

### O diagrama de Piper: classificação e agrupamento de fácies

O **diagrama de Piper** (Piper, 1944) é o gráfico mais usado em hidrogeoquímica para classificar e comparar múltiplas amostras de uma vez. Sua construção:

- Dois **triângulos** nas bases: um para cátions (vértices Ca²⁺, Mg²⁺, Na⁺+K⁺, cada eixo em % de meq/L do total de cátions) e um para ânions (vértices HCO₃⁻+CO₃²⁻, SO₄²⁻, Cl⁻, em % de meq/L do total de ânions).
- Um **losango central** (diamante), onde a posição de cada amostra combina sua projeção dos dois triângulos, mostrando simultaneamente o caráter catiônico e aniônico.

A posição de uma amostra no diamante permite ler diretamente sua fácies combinada: o canto superior corresponde a águas com predominância de Ca²⁺+Mg²⁺ e Cl⁻+SO₄²⁻ (águas evoluídas ricas em sulfato/cloreto de cálcio-magnésio — comum em contribuição de gipsita/dolomita); o canto inferior, a águas alcalinas bicarbonatadas sódicas (Na⁺ e HCO₃⁻ dominantes — típicas de troca iônica, Aula 02, ou de hidrólise avançada de silicatos sódicos); os cantos laterais correspondem às fácies mais simples (cálcio-bicarbonatada de um lado, sódio-clorídrica do outro).

> [!important] O maior poder do Piper é comparar, não medir
> Um diagrama de Piper com dezenas de amostras de um mesmo aquífero revela imediatamente se as amostras formam um **agrupamento único** (aquífero homogêneo, um único processo dominante) ou **múltiplos agrupamentos** (diferentes fontes de água, diferentes zonas do sistema de fluxo, ou mistura entre águas de origens distintas) — um padrão de dispersão ao longo de uma linha reta no diamante, em particular, é a assinatura clássica de **mistura binária** entre dois extremos composicionais (Aula 02 e Módulo 03 retomam mistura como processo em contaminação).

### O diagrama de Stiff: a "impressão digital" espacializável

O **diagrama de Stiff** (Stiff, 1951) representa uma única amostra como um polígono: três ou quatro eixos horizontais paralelos, cada um indo de um cátion (Ca²⁺, Mg²⁺, Na⁺+K⁺) à esquerda a um ânion correspondente (HCO₃⁻, SO₄²⁻, Cl⁻) à direita, em escala de meq/L, conectando os pontos extremos em um polígono cuja **forma** (não só o tamanho) é a assinatura visual da composição.

A vantagem central do diagrama de Stiff sobre o Piper é que ele é **compacto o suficiente para ser plotado diretamente sobre um mapa**, em cada ponto de amostragem — permitindo visualizar simultaneamente a distribuição espacial e a evolução da composição ao longo do sistema de fluxo, algo que o Piper (que precisa de um gráfico separado) não faz diretamente. Amostras com formas semelhantes de polígono, próximas espacialmente, sugerem a mesma origem/processo; mudanças progressivas de forma ao longo de uma linha de fluxo (do menor para o maior polígono, ou de uma forma para outra) visualizam a evolução hidroquímica regional (Chebotarev, Aula 02) diretamente no mapa.

### O diagrama de Schoeller: comparando várias amostras, vários parâmetros, uma escala logarítmica

O **diagrama de Schoeller** (também chamado semilogarítmico, Schoeller, 1962) organiza cada constituinte maior (e o TDS, opcionalmente) num eixo vertical logarítmico próprio, um ao lado do outro; cada amostra é representada por uma linha poligonal conectando seu valor em cada eixo.

A escala logarítmica é essencial porque os constituintes maiores variam em ordens de grandeza diferentes entre si (Ca²⁺ em dezenas de mg/L, Cl⁻ podendo ir de poucos a milhares) — numa escala linear, os constituintes minoritários ficariam ilegíveis. O Schoeller é o diagrama de escolha quando o objetivo é comparar **muitas amostras simultaneamente em todos os constituintes maiores ao mesmo tempo** (ao contrário do Piper, que exige agregar Na⁺+K⁺ e converte tudo em porcentagem, perdendo a informação de concentração absoluta): duas águas podem ter a mesma fácies percentual no Piper mas TDS absoluto muito diferente — só o Schoeller (ou a leitura direta dos dados) revela essa diferença.

| Diagrama | Mostra bem | Não mostra |
|---|---|---|
| Piper | Fácies relativa (%), agrupamento/mistura entre muitas amostras | Concentração absoluta, TDS |
| Stiff | Forma espacializável no mapa, comparação visual rápida ponto a ponto | Detalhe fino de constituintes menores |
| Schoeller | Concentração absoluta de cada constituinte maior, comparação multiamostra | Fácies percentual direta (exige leitura relativa entre eixos) |

> [!note] Os três diagramas respondem perguntas diferentes — não competem entre si
> Uma interpretação hidrogeoquímica completa tipicamente usa os três em conjunto: Piper para classificar fácies e detectar agrupamentos/mistura, Stiff para mapear a distribuição espacial, Schoeller para comparar magnitudes absolutas entre poços ou ao longo do tempo (mesmo poço, campanhas diferentes).

### Do diagrama ao modelo hidrogeoquímico conceitual

O **modelo hidrogeoquímico conceitual** integra os diagramas com o entendimento hidráulico já construído no Módulo 01 (mapas potenciométricos, sistemas de fluxo de Tóth) para produzir uma narrativa coerente e testável: de onde vem a água, que processos ela sofreu, e por qual caminho. Os passos típicos:

1. **Classificar a fácies** de cada amostra (nomenclatura + Piper).
2. **Mapear a distribuição espacial** das fácies (Stiff sobre o mapa potenciométrico) e verificar se a variação espacial é consistente com a direção de fluxo já conhecida (recarga → descarga).
3. **Testar a hipótese de evolução ao longo do fluxo** (sequência de Chebotarev, Aula 02) comparando fácies e TDS entre poços de montante e de jusante hidráulico — usando Schoeller para verificar se o aumento de TDS é gradual (evolução por interação água-rocha) ou abrupto (mistura com outra fonte, possível contaminação).
4. **Identificar anomalias** que não se encaixam na progressão esperada — um poço "fora da curva" é a pista mais valiosa de um processo adicional (troca iônica localizada, intrusão de água de outra unidade, contaminação — Módulo 03) e deve ser investigado, não descartado como ruído.
5. **Confrontar com o balanço iônico** (Aula 01) de cada amostra usada — um modelo conceitual construído sobre análises com balanço ruim é tão confiável quanto os dados que o sustentam.

> [!warning] O modelo conceitual é uma hipótese de trabalho, não uma prova
> Diagramas hidroquímicos mostram *padrões consistentes* com uma hipótese de origem e evolução — não a demonstram de forma unívoca. Duas hipóteses diferentes (por exemplo, evolução por interação água-rocha ao longo do fluxo vs. mistura de dois aquíferos distintos) podem produzir padrões espaciais parecidos num Piper ou Stiff. Confirmação mais forte exige integrar litologia real da área atravessada, dados isotópicos (fora do escopo deste módulo) ou datação de idade da água, quando disponíveis.

## Exemplo trabalhado

**Situação:** cinco poços ao longo de uma linha de fluxo regional (do poço 1, na recarga, ao poço 5, na descarga) mostram, no diagrama de Piper, uma progressão suave do canto cálcio-bicarbonatado (poço 1) até o canto sódio-clorídrico (poço 5), formando uma trajetória curva e contínua no diamante. O Schoeller mostra aumento progressivo e gradual de TDS de 220 para 1.850 mg/L ao longo da mesma sequência. Interprete.

**Raciocínio:** a progressão suave e contínua no Piper, acompanhada de aumento gradual (não abrupto) de TDS no Schoeller, é consistente com **evolução hidroquímica ao longo do sistema de fluxo regional** (sequência de Chebotarev, Aula 02) — não com mistura binária entre duas fontes distintas, que produziria tipicamente uma trajetória retilínea entre dois extremos fixos no diamante, com possíveis saltos de composição em vez de gradiente contínuo. **A lição:** a *forma* da trajetória no Piper (curva suave vs. reta entre extremos) e o *padrão* do Schoeller (gradual vs. abrupto) são, juntos, o principal critério visual para distinguir evolução progressiva de mistura simples — nenhum dos dois diagramas isoladamente seria conclusivo.

## Erros comuns

- **Usar só o Piper e ignorar a concentração absoluta.** Duas amostras podem ter fácies percentual idêntica no Piper com TDS de 100 mg/L e de 3.000 mg/L — informação que só o Schoeller (ou os dados brutos) revela.
- **Interpretar um agrupamento único no Piper como prova de que só existe um processo geoquímico atuando.** Processos diferentes podem, por coincidência, convergir para fácies percentuais semelhantes.
- **Descartar o poço anômalo do conjunto de dados** em vez de investigá-lo como pista de um processo adicional.
- **Construir o modelo conceitual usando amostras com balanço iônico fora da faixa aceitável** sem sinalizar essa limitação.

## O que não concluir

- **Que uma trajetória retilínea no Piper prova mistura entre exatamente duas fontes.** É consistente com mistura binária, mas outros processos (por coincidência geométrica) também podem produzir alinhamentos aparentes com poucas amostras — mais pontos ao longo da linha fortalecem a hipótese, mas não a provam de forma definitiva sem apoio isotópico ou hidráulico independente.
- **Que o modelo hidrogeoquímico conceitual substitui o modelo hidráulico do Módulo 01.** Os dois são complementares: o modelo hidráulico define de onde a água vem e para onde vai; o modelo hidrogeoquímico testa e enriquece essa história com a composição química — nenhum dos dois é completo sem o outro.

## Recap relâmpago

- Fácies hidroquímica nomeia os dois íons dominantes (>50% de meq/L); "mista" quando nenhum íon isolado supera 50%.
- **Piper**: dois triângulos (cátions, ânions) + diamante central — melhor para classificar fácies e detectar agrupamento/mistura entre muitas amostras (em %, sem concentração absoluta).
- **Stiff**: polígono por amostra, compacto o suficiente para plotar no mapa — melhor para visualizar distribuição espacial e evolução ao longo do fluxo.
- **Schoeller**: eixos logarítmicos paralelos por constituinte — melhor para comparar concentrações absolutas entre muitas amostras.
- O modelo hidrogeoquímico conceitual integra os três diagramas com o modelo hidráulico (Módulo 01) numa narrativa testável, nunca uma prova definitiva isolada; poços anômalos são pista, não ruído a descartar.

## Próxima aula

Última aula do Módulo 02. O módulo segue para o [[02-hidrogeoquimica-questionario|questionário]] e o [[02-hidrogeoquimica-flashcards|baralho de flashcards]]. Próximo módulo do curso: [[03-contaminacao-aguas-subterraneas/03-contaminacao-aguas-subterraneas-modulo|Módulo 03 — Contaminação dos recursos hídricos subterrâneos]], que usa diretamente o modelo hidrogeoquímico conceitual construído aqui para detectar composições anômalas indicativas de contaminação.

## Anterior

[[02-hidrogeoquimica-aula-04-amostragem-e-controle-de-qualidade|Aula 04 — Amostragem representativa, métodos analíticos, limites de detecção e padrões de qualidade]]

## Fontes

- Nomenclatura de fácies hidroquímica: Custodio, E. & Llamas, M. R. (1983), *Hidrología Subterránea*, Omega, cap. 13; Freeze, R. A. & Cherry, J. A. (1979), *Groundwater*, Prentice-Hall, cap. 7.
- Diagrama de Piper: Piper, A. M. (1944), "A graphic procedure in the geochemical interpretation of water-analyses", *Transactions, American Geophysical Union*, 25(6), 914–928.
- Diagrama de Stiff: Stiff, H. A. (1951), "The interpretation of chemical water analysis by means of patterns", *Journal of Petroleum Technology*, 3(10), 15–17.
- Diagrama de Schoeller: Schoeller, H. (1962), *Les eaux souterraines*, Masson, Paris.
- Integração ao modelo hidrogeoquímico conceitual: Appelo, C. A. J. & Postma, D. (2005), *Geochemical Processes and Applications*, 2ª ed., Balkema, cap. 8.

<!--
nivel: avancado
palavras_corpo: ~1900

mapa_objetivo_secao:
  geologia-avancado-m02-oa04: "Fácies hidroquímica: dando nome à composição" + "O diagrama de Piper: classificação e agrupamento de fácies" + "O diagrama de Stiff: a impressão digital espacializável" + "O diagrama de Schoeller: comparando várias amostras, vários parâmetros, uma escala logarítmica" + "Do diagrama ao modelo hidrogeoquímico conceitual" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: HIDROGEOQ-M02-A05-FACIES-001
    claim: "Fácies hidroquímica é nomeada pelos íons (um cátion, um ânion) que respondem por mais de 50% da soma de cátions ou ânions em meq/L; quando nenhum íon isolado supera 50%, a água é classificada como mista."
    risk: fato
    source: "Custodio & Llamas 1983, cap. 13; Freeze & Cherry 1979, cap. 7"
  - claim_id: HIDROGEOQ-M02-A05-PIPER-002
    claim: "O diagrama de Piper (1944) usa dois triângulos (cátions: Ca2+, Mg2+, Na++K+; ânions: HCO3-+CO3(2-), SO4(2-), Cl-, em % de meq/L) e um losango central que combina as duas projeções para classificar fácies hidroquímicas e detectar padrões de mistura entre amostras."
    risk: fato
    source: "Piper 1944, Transactions AGU 25(6)"
  - claim_id: HIDROGEOQ-M02-A05-STIFF-003
    claim: "O diagrama de Stiff (1951) representa uma amostra como um polígono em eixos horizontais paralelos de cátions e ânions em meq/L, sendo compacto o suficiente para ser plotado diretamente sobre um mapa em cada ponto de amostragem."
    risk: fato
    source: "Stiff 1951, Journal of Petroleum Technology 3(10)"
  - claim_id: HIDROGEOQ-M02-A05-SCHOELLER-004
    claim: "O diagrama de Schoeller (1962) usa eixos verticais logarítmicos paralelos, um por constituinte maior, permitindo comparar concentrações absolutas de várias amostras simultaneamente apesar das diferenças de ordem de grandeza entre constituintes."
    risk: fato
    source: "Schoeller 1962, Les eaux souterraines"
-->
