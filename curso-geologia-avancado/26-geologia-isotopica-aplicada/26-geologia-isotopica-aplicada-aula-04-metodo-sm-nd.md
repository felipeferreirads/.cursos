# Aula 04: Método Sm-Nd — idades isocrônicas e idades modelo, notação εNd e isótopos de Nd em petrogênese

**ID:** geologia-avancado-m26-a04
**Módulo:** [[26-geologia-isotopica-aplicada-modulo|Módulo 26 — Geologia isotópica aplicada]]
**Duração estimada:** ~25 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** aplicar a técnica da isócrona (Aula 03) ao par samário-neodímio, e introduzir dois recursos que o sistema Sm-Nd tornou padrão em petrogênese: a notação εNd, que expressa desvios muito pequenos da composição condrítica de referência, e a idade-modelo, que estima quando um magma se separou de um reservatório mantélico sem precisar de uma isócrona de múltiplos pontos.
**Ao final você vai conseguir:** calcular uma idade isocrônica Sm-Nd; converter uma razão ¹⁴³Nd/¹⁴⁴Nd medida em um valor εNd(t) usando o reservatório condrítico uniforme (CHUR) como referência; explicar o que uma idade-modelo (T_DM) estima e por que ela difere conceitualmente de uma idade isocrônica; e interpretar valores positivos e negativos de εNd em termos de fonte mantélica empobrecida versus fonte enriquecida ou crustal.
**Pré-requisito:** [[26-geologia-isotopica-aplicada-aula-03-sistema-rb-sr|Aula 03]] (técnica da isócrona, razão inicial como traçador de fonte — o raciocínio de fundo se repete aqui, com outro par isotópico e uma notação diferente).

## Conteúdo

### Por que o samário e o neodímio se comportam melhor que o rubídio e o estrôncio

O samário (Sm) e o neodímio (Nd) são dois elementos terras-raras leves (lantanídeos) vizinhos na tabela periódica, com raios iônicos e comportamento geoquímico muito parecidos entre si — ambos são elementos incompatíveis, mas de incompatibilidade moderada, e ambos entram preferencialmente na estrutura de minerais como apatita, granada, anfibólio e nos próprios silicatos formadores de rocha em proporções relativamente estáveis. Essa semelhança geoquímica tem uma consequência importante para a geocronologia: a razão Sm/Nd de uma rocha varia **pouco** durante processos como intemperismo, metamorfismo de baixo a médio grau e alteração hidrotermal, ao contrário da razão Rb/Sr, que é facilmente perturbada porque o rubídio (um elemento alcalino grande e muito incompatível) e o estrôncio (alcalino-terroso) reagem de forma bem diferente a fluidos aquosos. Por isso, o sistema Sm-Nd é considerado, de modo geral, mais **robusto** contra alteração secundária que o Rb-Sr — uma vantagem prática relevante ao datar rochas metamórficas ou hidrotermalmente alteradas, embora nenhum dos dois sistemas seja imune a perturbação em condições suficientemente extremas.

### A isócrona Sm-Nd

O ¹⁴⁷Sm decai por emissão de partícula alfa para **¹⁴³Nd**, com uma constante de decaimento recomendada pela força-tarefa conjunta IUPAC-IUGS em sua avaliação mais recente (2020) de λ = (6,524 ± 0,024) × 10⁻¹² ano⁻¹, correspondendo a uma meia-vida de (106,25 ± 0,38) bilhões de anos — cerca de duas vezes mais longa que a do ⁸⁷Rb (49,61 Ga, Aula 03), o que faz do Sm-Nd um sistema especialmente adequado para datar eventos muito antigos (rochas arqueanas e mesmo meteoritos, usados para datar a formação do sistema solar), mas menos sensível, em termos de acúmulo mensurável de filho radiogênico, para rochas muito jovens. Usando ¹⁴⁴Nd (estável, não radiogênico) como isótopo normalizador — o análogo, neste sistema, ao papel que o ⁸⁶Sr desempenha no Rb-Sr —, a equação da isócrona Sm-Nd tem exatamente a mesma forma da equação de Rb-Sr da Aula 03:

$$\left(\frac{{}^{143}\text{Nd}}{{}^{144}\text{Nd}}\right)_{\text{hoje}} = \left(\frac{{}^{143}\text{Nd}}{{}^{144}\text{Nd}}\right)_{\text{inicial}} + \left(\frac{{}^{147}\text{Sm}}{{}^{144}\text{Nd}}\right)_{\text{hoje}}\left(e^{\lambda t}-1\right)$$

Um conjunto de amostras cogenéticas (minerais separados de uma rocha, ou rochas de uma mesma suíte) com razões Sm/Nd diferentes, mas mesma idade e mesma razão inicial, cai sobre uma reta num diagrama ¹⁴⁷Sm/¹⁴⁴Nd vs. ¹⁴³Nd/¹⁴⁴Nd; a inclinação dá a idade, o intercepto dá a razão inicial. A leitura geométrica, o procedimento de ajuste e as duas armadilhas discutidas na Aula 03 (isócrona de mistura, rehomogeneização metamórfica) se aplicam igualmente aqui — a diferença entre os dois sistemas está inteiramente na física nuclear (λ diferente) e na química dos elementos envolvidos (Sm-Nd mais resistente à perturbação secundária).

### O reservatório condrítico uniforme (CHUR) e a notação εNd

Como a razão Sm/Nd varia pouco entre reservatórios geológicos diferentes (ao contrário da razão Rb/Sr, que varia por ordens de grandeza entre manto e crosta), a razão ¹⁴³Nd/¹⁴⁴Nd também varia pouco de um reservatório para outro — as diferenças interessantes aparecem na quarta ou quinta casa decimal da razão bruta, o que tornaria qualquer tabela de valores absolutos difícil de ler e comparar. A solução adotada pela comunidade, proposta por DePaolo & Wasserburg (1976), foi definir um valor de referência — o **reservatório condrítico uniforme**, CHUR (do inglês *Chondritic Uniform Reservoir*) — que representa a composição média do material rochoso do Sistema Solar a partir do qual a Terra se formou, estimada a partir de meteoritos condríticos. O CHUR tem, por definição, uma razão ¹⁴⁷Sm/¹⁴⁴Nd de aproximadamente 0,1967 (valor original de DePaolo & Wasserburg, 1976; refinamentos posteriores com medidas de maior precisão em condritos não equilibrados sugerem um valor ligeiramente menor, próximo de 0,1960) e uma razão ¹⁴³Nd/¹⁴⁴Nd presente de aproximadamente 0,512638.

A partir do CHUR, define-se a notação **εNd** (épsilon-Nd), que expressa o desvio da razão ¹⁴³Nd/¹⁴⁴Nd de uma amostra em relação ao CHUR, em partes por 10.000:

$$\varepsilon_{Nd} = \left[\frac{\left({}^{143}\text{Nd}/{}^{144}\text{Nd}\right)_{\text{amostra}}}{\left({}^{143}\text{Nd}/{}^{144}\text{Nd}\right)_{\text{CHUR}}} - 1\right] \times 10^{4}$$

Um valor de εNd = 0 significa que a amostra tem exatamente a composição isotópica que o manto teria se tivesse evoluído desde a formação da Terra com a mesma razão Sm/Nd do material condrítico médio — ou seja, sem nunca ter passado por um evento de fracionamento de terras-raras (como a extração de um magma, que separa Sm de Nd de forma sistemática). Um εNd **positivo** indica uma fonte com razão Sm/Nd historicamente **mais alta** que a condrítica — o **manto empobrecido** (depleted mantle, DM), que perdeu componentes incompatíveis (Nd é mais incompatível que Sm, então extrair magma do manto ao longo do tempo geológico empobrece o manto residual em Nd relativamente a Sm, elevando Sm/Nd e, com ele, a taxa de acúmulo de ¹⁴³Nd radiogênico). Um εNd **negativo** indica uma fonte com Sm/Nd historicamente mais baixa que a condrítica — tipicamente **crosta continental antiga**, que concentra elementos incompatíveis como o Nd durante sua formação por fusão parcial do manto, empobrecendo-se relativamente em Sm.

**Uma advertência de notação, antes que ela pegue você de surpresa no exemplo.** A fórmula acima compara a amostra com o CHUR **de hoje**, e é assim que se calcula o εNd de uma rocha recente. Mas a pergunta petrogenética quase sempre é outra: que assinatura a fonte tinha **no momento em que a rocha cristalizou**? Para responder isso escreve-se **εNd(t)**, com o (t) indicando que os dois termos da razão — o da amostra e o do CHUR — são avaliados naquele instante, não hoje. O do CHUR precisa ser recalculado para trás, porque o CHUR também acumula ¹⁴³Nd ao longo do tempo; o exemplo trabalhado faz essa conta passo a passo. Guarde a distinção: εNd sem argumento é hoje, εNd(t) é na idade da rocha, e é quase sempre o segundo que se publica.

Essa é a contrapartida direta, em outro sistema isotópico, do raciocínio de razão inicial de estrôncio da Aula 03: εNd positivo aponta para fonte mantélica empobrecida (análogo a ⁸⁷Sr/⁸⁶Sr baixo), εNd negativo aponta para envolvimento de crosta continental antiga (análogo a ⁸⁷Sr/⁸⁶Sr alto) — e, de fato, é comum ver os dois traçadores usados juntos, num diagrama εNd versus ⁸⁷Sr/⁸⁶Sr inicial, para caracterizar a fonte de uma suíte ígnea com dois sistemas independentes.

### Idade-modelo: uma idade sem isócrona

Nem sempre se tem acesso a múltiplas frações cogenéticas de composição Sm/Nd variável para construir uma isócrona — às vezes há apenas uma amostra de rocha total. Para esses casos, o sistema Sm-Nd oferece um segundo tipo de idade, conceitualmente distinto: a **idade-modelo** (T_DM, de *depleted mantle model age*), que estima **há quanto tempo o material que forma a rocha se separou do manto** (por extração de um magma), assumindo que, antes dessa separação, a razão Sm/Nd do material evoluía junto com a do manto empobrecido, e que, depois da separação, evoluiu com a razão Sm/Nd medida hoje na própria rocha.

A lógica geométrica é a de projetar, para trás no tempo, a evolução da razão ¹⁴³Nd/¹⁴⁴Nd da amostra (usando sua própria razão Sm/Nd medida) até encontrar o ponto em que ela cruzaria a curva de evolução do manto empobrecido — esse ponto de cruzamento é T_DM. A equação correspondente, análoga à equação geral da idade da Aula 01 mas usando o manto empobrecido em vez do CHUR como referência, é:

$$t_{DM} = \frac{1}{\lambda}\ln\left[1 + \frac{\left({}^{143}\text{Nd}/{}^{144}\text{Nd}\right)_{\text{amostra,hoje}} - \left({}^{143}\text{Nd}/{}^{144}\text{Nd}\right)_{DM,\text{hoje}}}{\left({}^{147}\text{Sm}/{}^{144}\text{Nd}\right)_{\text{amostra}} - \left({}^{147}\text{Sm}/{}^{144}\text{Nd}\right)_{DM}}\right]$$

onde os valores de referência do manto empobrecido de hoje — (¹⁴³Nd/¹⁴⁴Nd)_DM e (¹⁴⁷Sm/¹⁴⁴Nd)_DM — vêm de um modelo de evolução do manto empobrecido ao longo do tempo geológico — o mais citado é o de DePaolo (1981), que ajusta uma curva **não linear** a dados de basaltos de dorsal meso-oceânica.

**Esta aula não calcula um T_DM numericamente, e vale dizer por quê.** Fazer a conta exige os dois parâmetros de referência do manto empobrecido de hoje, e eles não são valores universais: dependem de qual modelo de evolução se adota, e aproximá-los por uma reta — que é o atalho didático comum — muda o resultado em dezenas a centenas de milhões de anos justamente nas rochas antigas em que T_DM mais interessa. O que você precisa levar desta seção não é uma aritmética, e sim a **leitura geométrica**: T_DM é o ponto de encontro entre duas curvas de evolução, a da amostra e a do manto empobrecido, projetadas para trás no tempo. Quem entendeu esse encontro sabe ler qualquer T_DM publicado e, sobretudo, sabe perguntar a pergunta certa diante dele — "contra que modelo de manto este número foi calculado?" —, que é a pergunta que decide se dois T_DM de artigos diferentes são comparáveis entre si.

**O que T_DM mede, e o que não mede.** É essencial não confundir idade-modelo com idade isocrônica: T_DM estima quando o **precursor químico** do material se separou do manto (um evento de extração de magma, ou de diferenciação crustal), não necessariamente quando a **rocha que você tem na mão** cristalizou. Uma rocha sedimentar, por exemplo, não tem "idade de cristalização" no sentido ígneo — mas seu T_DM ainda é interpretável, como a idade média (ponderada pela contribuição de cada fonte) de extração crustal do material que a compõe, útil para reconstituir a idade média da crosta continental que forneceu os sedimentos, mesmo que a deposição do próprio sedimento seja muito mais jovem. Essa distinção — idade de um evento específico versus idade média de extração de um precursor químico — é o ponto de dificuldade mais citado sobre o método na literatura, e reaparece, com outra roupagem, na discussão de idade-modelo de chumbo da Aula 05.

## Exemplo trabalhado: de isócrona a εNd(t)

**Situação.** Três frações minerais de uma mesma rocha máfica (dados hipotéticos) foram analisadas, produzindo uma isócrona Sm-Nd com inclinação 0,0007200 e intercepto (¹⁴³Nd/¹⁴⁴Nd)_inicial = 0,511800. Usando λ = 6,524 × 10⁻¹² ano⁻¹ (IUPAC-IUGS, 2020) e os valores de CHUR de DePaolo & Wasserburg (1976) — (¹⁴³Nd/¹⁴⁴Nd)_CHUR,0 = 0,512638 e (¹⁴⁷Sm/¹⁴⁴Nd)_CHUR = 0,1967 —, calcule a idade da rocha e o valor de εNd no momento da cristalização.

**Resolução — idade.** Da inclinação:

$$e^{\lambda t} - 1 = 0{,}0007200 \quad\Rightarrow\quad \lambda t = \ln(1{,}00072)$$

Calculando: ln(1,00072) ≈ 0,0007197. Então:

$$t = \frac{0{,}0007197}{6{,}524\times10^{-12}} \approx 1{,}1032\times10^{8}\ \text{anos} \approx 110{,}3\ \text{milhões de anos}$$

**Resolução — razão do CHUR no momento da cristalização.** A razão ¹⁴³Nd/¹⁴⁴Nd do CHUR também evolui no tempo, com sua própria (¹⁴⁷Sm/¹⁴⁴Nd)_CHUR constante:

$$\left(\frac{{}^{143}\text{Nd}}{{}^{144}\text{Nd}}\right)_{CHUR,t} = \left(\frac{{}^{143}\text{Nd}}{{}^{144}\text{Nd}}\right)_{CHUR,0} - \left(\frac{{}^{147}\text{Sm}}{{}^{144}\text{Nd}}\right)_{CHUR}\left(e^{\lambda t}-1\right)$$

$$= 0{,}512638 - 0{,}1967 \times 0{,}0007200 \approx 0{,}512638 - 0{,}0001416 = 0{,}512496$$

**Resolução — εNd(t).** Usando a razão inicial da isócrona (0,511800) e a razão do CHUR no mesmo instante (0,512496):

$$\varepsilon_{Nd}(t) = \left[\frac{0{,}511800}{0{,}512496} - 1\right]\times10^{4} = \left[0{,}998642 - 1\right]\times10^{4} \approx -13{,}6$$

**Interpretação.** A rocha cristalizou há aproximadamente 110,3 milhões de anos (Cretáceo Inferior) com εNd(t) ≈ −13,6 — um valor claramente negativo e numericamente expressivo, incompatível com uma fonte de manto empobrecido não contaminado (que, num basalto dessa idade, tipicamente mostraria εNd positivo, entre cerca de +7 e +10 — a média de basaltos de dorsal meso-oceânica atuais fica próxima de +9 a +10). Um εNd(t) tão negativo, para uma rocha máfica, é a assinatura característica de contaminação crustal substancial durante a ascensão do magma, ou de uma fonte mantélica litosférica antiga e enriquecida (metassomatizada por fluidos ou fundidos crustais em algum evento muito anterior à cristalização) — exatamente o tipo de conclusão que o par razão inicial de Sr (Aula 03) mais εNd(t) (esta aula), usados juntos, tornaria mais robusta.

## Recap relâmpago

- Sm e Nd são terras-raras leves quimicamente muito parecidos entre si; sua razão Sm/Nd resiste melhor a alteração secundária que a razão Rb/Sr, tornando o sistema Sm-Nd mais robusto para rochas metamórficas ou alteradas.
- A isócrona Sm-Nd tem a mesma forma matemática da isócrona Rb-Sr (Aula 03): inclinação dá a idade (com λ = 6,524 × 10⁻¹² ano⁻¹, IUPAC-IUGS 2020), intercepto dá a razão inicial ¹⁴³Nd/¹⁴⁴Nd.
- A notação **εNd** expressa o desvio da razão ¹⁴³Nd/¹⁴⁴Nd de uma amostra em relação ao CHUR (reservatório condrítico uniforme, a composição média do Sistema Solar), em partes por 10.000; εNd positivo indica fonte de manto empobrecido, εNd negativo indica envolvimento de crosta continental antiga — o análogo, em outro sistema, da razão inicial de Sr.
- A **idade-modelo** T_DM estima quando o material de uma rocha se separou do manto (por extração de magma), projetando a evolução da razão ¹⁴³Nd/¹⁴⁴Nd da amostra para trás até cruzar a curva de evolução do manto empobrecido — um conceito diferente de idade isocrônica, que registra um evento específico de cristalização.
- Não confunda idade-modelo com idade de cristalização: T_DM é útil até para rochas sem "idade ígnea" própria (sedimentos), como estimativa da idade média de extração crustal do material-fonte.

## Próxima aula

[[26-geologia-isotopica-aplicada-aula-05-sistemas-u-pb-pb-pb|Aula 05 — Sistemas U-Pb e Pb-Pb]]: dois sistemas de decaimento operando em paralelo a partir de dois isótopos de urânio, o diagrama concórdia que permite reconhecer perda de chumbo sem invalidar a idade, e a idade Pb-Pb, que dispensa até a medida de urânio.

## Fontes

- Faure, G. & Mensing, T. M. (2005), *Isotopes: Principles and Applications*, 3ª ed., Wiley — capítulo 9 (sistema Sm-Nd, isócronas, CHUR e notação εNd).
- DePaolo, D. J. & Wasserburg, G. J. (1976), "Nd isotopic variations and petrogenetic models", *Geophysical Research Letters*, 3(5), 249-252 — definição original do CHUR e da notação εNd. VERIFICADO por busca nesta redação (valores 0,512638 e 0,1967/0,1960 confirmados).
- DePaolo, D. J. (1981), "Neodymium isotopes in the Colorado Front Range and crust-mantle evolution in the Proterozoic", *Nature*, 291, 193-196 — modelo de evolução do manto empobrecido (DM), de curva não linear, que é a referência usual para o cálculo de idade-modelo T_DM. Esta aula ensina a leitura geométrica de T_DM, mas **não** calcula um valor numérico, justamente para não publicar um resultado que dependeria de uma aproximação linear da curva deste modelo. CONFERIDO na auditoria (2026-09-21): volume e paginação corretos.
- Villa, I. M., Holden, N. E., Possolo, A., Hibbert, D. B., Ickert, R. B. & Renne, P. R. (2020), "IUPAC-IUGS recommendation on the half-lives of ¹⁴⁷Sm and ¹⁴⁶Sm", *Geochimica et Cosmochimica Acta*, 285, 70-77 — "(106.25 ± 0.38) Ga for the half-life of 147Sm, and a corresponding decay constant λ147 = (6.524 ± 0.024) × 10⁻¹² a⁻¹". CONFERIDO na auditoria (2026-09-21): lista de autores, volume e paginação confirmados.
- Bouvier, A., Vervoort, J. D. & Patchett, P. J. (2008), "The Lu-Hf and Sm-Nd isotopic composition of CHUR: constraints from unequilibrated chondrites and implications for the bulk composition of terrestrial planets", *Earth and Planetary Science Letters*, 273(1-2), 48-57 — refinamento dos parâmetros do CHUR (¹⁴⁷Sm/¹⁴⁴Nd ≈ 0,1960). CONFERIDO na auditoria (2026-09-21): volume e paginação corretos.

<!--
nivel: avancado
palavras_corpo: 2126
palavras_corpo_metodo: "tokens separados por espaco entre '## Conteudo' e '## Fontes', incluindo LaTeX e tabelas (metodo declarado em 2026-09-22). Este numero nao e comparavel ao 2192 anterior, que usava convencao diferente."
duracao_estimada_min: 25

NOTA DE REVISAO DIDATICA (2026-09-22, revisor-didatico, modo review-and-fix):
  (a) ACHADO LARANJA DID-3 CORRIGIDO - promessa falsa de exemplo. Detalhado no registro do claim
  ISOGEO-M26-A04-IDADE-MODELO-TDM-006, abaixo.
  (b) ACHADO AMARELO DID-11 CORRIGIDO - salto de notacao epsilonNd para epsilonNd(t). O cabecalho
  da aula promete 'converter uma razao 143Nd/144Nd medida em um valor epsilonNd(t)', a secao de
  teoria define epsilonNd SEM argumento (contra o CHUR de hoje), e o (t) so aparecia, sem aviso, ja
  dentro do exemplo trabalhado - onde o aluno descobre de surpresa que precisa recalcular tambem o
  CHUR para tras no tempo. A conta estava correta e o exemplo a explicava, mas tarde: a surpresa
  vem antes da explicacao. CORRIGIDO com um paragrafo de advertencia de notacao ao fim da secao de
  teoria, dizendo o que o (t) significa (os dois termos avaliados na idade da rocha, nao hoje), por
  que o CHUR precisa ser recalculado (ele tambem acumula 143Nd) e que e quase sempre o epsilonNd(t)
  que se publica. Nenhum numero novo; a equacao de evolucao do CHUR continua sendo apresentada no
  exemplo, onde e usada.
  (c) ESTA E A AULA MAIS LEVE DO MODULO (~25 min contra ~30 das aulas 01 e 02). Ha folga deliberada
  aqui - ver a sugestao azul DID-9 no registro do claim 006.

mapa_objetivo_secao:
  geologia-avancado-m26-oa02: "A isócrona Sm-Nd" + "Exemplo trabalhado"
  geologia-avancado-m26-oa03: "O reservatório condrítico uniforme (CHUR) e a notação εNd" + "Idade-modelo: uma idade sem isócrona" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: ISOGEO-M26-A04-SM-ND-QUIMICA-ROBUSTEZ-001
    claim: "Samario e neodimio sao terras-raras leves quimicamente muito semelhantes entre si (raios ionicos proximos, incompatibilidade moderada similar), o que faz a razao Sm/Nd de uma rocha variar pouco durante intemperismo, metamorfismo de baixo a medio grau e alteracao hidrotermal, tornando o sistema Sm-Nd geralmente mais robusto contra alteracao secundaria que o sistema Rb-Sr, cuja razao Rb/Sr e mais facilmente perturbada por fluidos aquosos."
    risk: fato
    source: "Principio geoquimico consolidado, amplamente documentado em Faure & Mensing (2005), Isotopes: Principles and Applications, 3a ed., Wiley, cap. 9, e em literatura de geoquimica isotopica sobre robustez relativa de sistemas isocronicos frente a alteracao secundaria."
  - claim_id: ISOGEO-M26-A04-SM147-DECAY-CONSTANT-002
    claim: "O 147Sm decai por emissao alfa para 143Nd; a forca-tarefa conjunta IUPAC-IUGS recomenda, em avaliacao de 2020, uma meia-vida de (106,25 +/- 0,38) Ga e constante de decaimento lambda = (6,524 +/- 0,024) x 10^-12 /ano."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-21): resultado de busca confirma 'The IUPAC-IUGS joint Task Group Isotopes in Geosciences recommends a value of (106.25 +/- 0.38) Ga for the half-life of 147Sm, and a corresponding decay constant lambda147 = (6.524 +/- 0.024) x 10-12 a-1', associado a publicacao em Geochimica et Cosmochimica Acta identificada nos resultados de busca (ScienceDirect S0016703720303823, IUPAC-IUGS recommendation on the half-lives of 147Sm). CONFIRMADO PELA AUDITORIA (2026-09-21): Villa, I.M., Holden, N.E., Possolo, A., Hibbert, D.B., Ickert, R.B. & Renne, P.R. (2020), Geochimica et Cosmochimica Acta 285, 70-77, doi 10.1016/j.gca.2020.06.022. Lista de autores, volume e paginacao verificados; a INCERTEZA DECLARADA esta RESOLVIDA. Meia-vida conferida por calculo: ln(2)/6,524e-12 = 106,246 Ga, consistente com 106,25 Ga.
    ACHADO VERMELHO 1 (auditoria 2026-09-21), claim ISOGEO-M26-A04-SM147-RB87-HALFLIFE-RATIO-012: o corpo da aula afirmava que a meia-vida do 147Sm e 'quase sete vezes mais longa que a do 87Rb'. FALSO: 106,25 Ga / 49,61 Ga = 2,14, ou seja CERCA DE DUAS VEZES. Corrigido para 'cerca de duas vezes mais longa que a do 87Rb (49,61 Ga, Aula 03)'. Fontes: Villa et al. (2020), GCA 285, 70-77 (147Sm) e Villa, De Bievre, Holden & Renne (2015), GCA 164, 382-385 (87Rb)."
  - claim_id: ISOGEO-M26-A04-EQUACAO-ISOCRONA-SMND-003
    claim: "A equacao da isocrona Sm-Nd tem a mesma forma da isocrona Rb-Sr: (143Nd/144Nd)_hoje = (143Nd/144Nd)_inicial + (147Sm/144Nd)_hoje*(e^(lambda*t)-1), usando 144Nd como isotopo normalizador nao radiogenico; um conjunto de amostras cogeneticas com razoes Sm/Nd diferentes mas mesma idade e razao inicial cai sobre uma reta neste diagrama."
    risk: fato
    source: "Deducao padrao, analoga a isocrona Rb-Sr da Aula 03; Faure & Mensing (2005), cap. 9; Dickin, A.P. (2005), Radiogenic Isotope Geology, 2a ed., Cambridge University Press, cap. 5."
  - claim_id: ISOGEO-M26-A04-CHUR-DEFINICAO-VALORES-004
    claim: "O CHUR (Chondritic Uniform Reservoir), proposto por DePaolo & Wasserburg (1976), representa a composicao media do material rochoso do Sistema Solar estimada a partir de meteoritos condriticos; tem 147Sm/144Nd(CHUR) de aproximadamente 0,1967 (valor original de 1976) e 143Nd/144Nd(CHUR,hoje) de aproximadamente 0,512638. Refinamentos posteriores com medidas de maior precisao em condritos nao equilibrados sugerem valor ligeiramente menor, proximo de 0,1960, para 147Sm/144Nd."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-21): resultado de busca confirma 'For the present, the value of (143Nd/144Nd)CHUR is 0.512638... the 147Sm/144Nd ratio of the Earth is the same as the chondritic value, 0.1967' e tambem 'average Sm-Nd chondrite compositions of unequilibrated chondrites show 147Sm/144Nd = 0.1960 +/- 4 and 143Nd/144Nd = 0.512630 +/- 11 (2 sigma m)', com referencia a DePaolo & Wasserburg (1976) e a Wikipedia (Chondritic uniform reservoir) como fontes agregadas na busca. Valor refinado de 0,1960 associado a literatura mais recente (p.ex. Bouvier et al. 2008), citado de memoria quanto a atribuicao exata. CONFIRMADO PELA AUDITORIA (2026-09-21): Bouvier, A., Vervoort, J.D. & Patchett, P.J. (2008), 'The Lu-Hf and Sm-Nd isotopic composition of CHUR: constraints from unequilibrated chondrites and implications for the bulk composition of terrestrial planets', Earth and Planetary Science Letters 273(1-2), 48-57 - volume e paginacao verificados; e DePaolo, D.J. & Wasserburg, G.J. (1976), Geophysical Research Letters 3(5), 249-252 (doi 10.1029/GL003i005p00249) - volume, numero e paginacao verificados. INCERTEZA DECLARADA RESOLVIDA."
  - claim_id: ISOGEO-M26-A04-EPSILON-ND-FORMULA-005
    claim: "A notacao epsilon-Nd e definida como epsilonNd = [(143Nd/144Nd)_amostra / (143Nd/144Nd)_CHUR - 1] x 10^4, expressando o desvio da razao isotopica da amostra em relacao ao CHUR em partes por 10.000; epsilonNd positivo indica fonte com Sm/Nd historicamente mais alta que a condritica (manto empobrecido, DM), epsilonNd negativo indica fonte com Sm/Nd historicamente mais baixa (tipicamente crosta continental antiga, enriquecida em Nd incompativel durante fusao parcial do manto)."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-21): resultado de busca confirma 'The Nd isotopic composition is normally converted to an epsilon value defined as epsilonNd = [(143Nd/144Nd)Sample/(143Nd/144Nd)CHUR - 1] x 10^4, where CHUR is the Chondritic Uniform Reservoir'. A interpretacao petrogenetica (positivo=manto empobrecido, negativo=crosta antiga) e conhecimento consolidado de geoquimica isotopica, ver Faure & Mensing (2005), cap. 9."
  - claim_id: ISOGEO-M26-A04-IDADE-MODELO-TDM-006
    claim: "A idade-modelo T_DM (depleted mantle model age) estima quando o material de uma rocha se separou quimicamente do manto (por extracao de magma), projetando a evolucao da razao 143Nd/144Nd da amostra (usando sua propria razao Sm/Nd medida hoje) para tras no tempo ate o ponto em que cruzaria a curva de evolucao do manto empobrecido; e conceitualmente distinta de uma idade isocronica, que registra um evento especifico de cristalizacao, e permanece interpretavel mesmo para rochas sedimentares sem idade ignea propria, como estimativa da idade media de extracao crustal do material-fonte. O modelo de evolucao do manto empobrecido mais citado e o de DePaolo (1981), que usa curva nao linear."
    risk: fato
    source: "Conceito padrao de geoquimica isotopica Sm-Nd, ver DePaolo, D.J. (1981), Nature, 291, 193-196 (CONFIRMADO pela auditoria 2026-09-21: 'Neodymium isotopes in the Colorado Front Range and crust-mantle evolution in the Proterozoic', Nature 291, 193-196, doi 10.1038/291193a0), e Faure & Mensing (2005), cap. 9.
    CORRECAO DE COERENCIA NA REVISAO DIDATICA (2026-09-22), achado laranja DID-3: o texto da aula anunciava que 'esta aula usa, NO EXEMPLO A SEGUIR, uma aproximacao linear simplificada da evolucao do manto empobrecido' - e o exemplo trabalhado da aula NAO calcula T_DM em momento nenhum, nem usa aproximacao linear nenhuma. Ele calcula idade isocronica e epsilonNd(t). A promessa era falsa e deixava a equacao de T_DM publicada sem nenhuma instanciacao, com tres valores de referencia (os do manto empobrecido de hoje) que o aluno nunca via preenchidos. CORRECAO APLICADA: a promessa foi retirada e substituida por um paragrafo que diz explicitamente que a aula NAO calcula T_DM e por que - os parametros de referencia do manto empobrecido nao sao universais, dependem do modelo adotado, e a aproximacao linear muda o resultado em dezenas a centenas de Ma justamente nas rochas antigas em que T_DM interessa - deslocando o que se deve reter para a LEITURA GEOMETRICA (T_DM como encontro de duas curvas de evolucao projetadas para tras) e para a pergunta critica que o aluno deve fazer diante de um T_DM publicado ('contra que modelo de manto?'). Nenhum valor numerico foi acrescentado, e a afirmacao de que a curva de DePaolo (1981) nao e linear ja constava desta alegacao auditada. A entrada de DePaolo (1981) na lista de Fontes foi ajustada na mesma edicao, porque tambem repetia a frase da simplificacao linear.
    OBSERVACAO PARA O REDATOR (sugestao azul DID-9, nao aplicada): esta e a aula mais leve do modulo (~22 min contra ~30 das mais pesadas), e teria folga para um exemplo numerico de T_DM. Escrever um exige declarar valores de referencia do manto empobrecido, o que e conteudo factual novo e, por isso, nao foi feito na revisao didatica."
  - claim_id: ISOGEO-M26-A04-EXEMPLO-ISOCRONA-EPSILON-007
    claim: "Para inclinacao de isocrona 0,0007200 e lambda=6,524x10^-12/ano, ln(1,00072)=0,0007197 e t=0,0007197/6,524x10^-12=1,1032x10^8 anos (110,3 milhoes de anos); com (147Sm/144Nd)CHUR=0,1967 e (143Nd/144Nd)CHUR,0=0,512638, a razao do CHUR no momento t e 0,512638-0,1967*0,0007200=0,512638-0,0001416=0,512496; com intercepto da isocrona (143Nd/144Nd)_inicial=0,511800, epsilonNd(t)=[(0,511800/0,512496)-1]x10^4=[0,998642-1]x10^4=-13,6."
    risk: calculo
    source: "Aritmetica direta a partir das equacoes apresentadas nesta aula; todos os dados de entrada (inclinacao da isocrona 0,0007200, intercepto 0,511800) sao hipoteticos, construidos especificamente para este exemplo pedagogico e nao correspondem a uma rocha real analisada. RECALCULADO E CONFIRMADO PELA AUDITORIA (2026-09-21, execucao em Python): ln(1,00072) = 0,00071974; t = 110,322 Ma; CHUR_t = 0,51249638; epsilonNd(t) = -13,588. Todos os quatro numeros publicados na aula reproduzem exatamente.
    ACHADO LARANJA 8 (auditoria 2026-09-21), claim ISOGEO-M26-A04-EPSILON-DM-BAND-013: a interpretacao do exemplo dizia que um basalto de manto empobrecido nao contaminado desta idade mostraria 'epsilonNd positivo, entre +5 e +10'. O limite inferior e baixo demais para uma fonte estritamente empobrecida: a media de N-MORB atual fica em torno de +9 a +10, e valores proximos de +5 ja indicam fonte levemente enriquecida (tipo E-MORB). Corrigido para 'entre cerca de +7 e +10', com a media de MORB atual (+9 a +10) explicitada. Fonte: compilacoes de composicao do manto empobrecido (DMM) em Workman & Hart (2005), EPSL 231, 53-72, e Salters & Stracke (2004), G3 5, Q05B07; epsilonNd medio de N-MORB proximo de +9,5."
-->
