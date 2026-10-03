# Auditoria científica — Módulo 28: Matemática para geociências

**Modo:** `audit-and-fix` · **Profundidade:** `full`
**Data:** 2026-08-19
**Escopo:** as 4 aulas do módulo, auditadas em conjunto (aulas 01–04), incluindo
consistência interna entre elas e consistência com o restante do curso — em particular, checagem explícita contra [[03-tempo-geologico-geocronologia-aula-04-meia-vida|03-tempo-geologico-geocronologia-aula-04-meia-vida.md]] (valores e vocabulário de meia-vida) e [[17-geologia-estrutural-aula-06-mapas-e-secoes-estruturais-parte-1-atitude-e-padroes-de-afloramento|17-geologia-estrutural-aula-06]] (definições de direção/mergulho), pedida explicitamente pelo escopo desta rodada. **Veredito: Aprovado.** 0 achados 🔴, 0 achados 🟠, 0 achados 🟡, 0 achados 🔵, 0 achados ⚪.

## Metodologia

Leitura das 4 aulas em conjunto, listagem de todas as alegações verificáveis (definições, fórmulas matemáticas, valores numéricos e exemplos calculados), recálculo independente de todos os exemplos trabalhados (aritmética verificada passo a passo), e verificação por `web_search` dos pontos de maior risco: a fórmula de mergulho aparente/verdadeiro (trigonometria estrutural), a lei do decaimento radioativo e a relação λ = ln(2)/T½, os fatores de amplitude e energia da escala de magnitude sísmica, e a definição da escala phi de tamanho de grão sedimentar. Checagem cruzada específica de que nenhuma aula deste módulo contradiz valores ou definições já fixados nos Módulos 03 e 18.

## Verificado e correto

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `GEO-M28-A01-TRIG-BASICA-001` | Seno, cosseno e tangente de um ângulo agudo são razões fixas entre os lados de um triângulo retângulo, dependentes apenas do ângulo | Trigonometria plana básica, ensino médio | Confirmado |
| `GEO-M28-A01-MERGULHO-DEF-002` | Mergulho verdadeiro = ângulo de inclinação máxima, medido perpendicular à direção (strike); mergulho aparente = ângulo em qualquer outro corte, ≤ mergulho verdadeiro | Rowland, Duebendorfer & Schiefelbein 2007; Davis, Reynolds & Kluth 2012 — consistente com a definição de direção/mergulho já usada em [[17-geologia-estrutural-aula-06-mapas-e-secoes-estruturais-parte-1-atitude-e-padroes-de-afloramento|17-geologia-estrutural-aula-06]] | Confirmado — sem contradição com o Módulo 17 |
| `GEO-M28-A01-FORMULA-APARENTE-003` | tan(mergulho aparente) = tan(mergulho verdadeiro) × sen(α), α = ângulo entre o corte e a direção da camada | Confirmado por busca web: stevedutch.net (Structural Geology, "Find the Apparent Dip of a Plane"); Rowland, Duebendorfer & Schiefelbein 2007; USGS Techniques and Methods 7-C28 ("An Apparent Dip Calculator for Spreadsheets") | Confirmado — fórmula e exemplo numérico de referência batem com o cálculo apresentado na aula (recalculado independentemente: 36° para mergulho verdadeiro 40° e α = 60°) |
| `GEO-M28-A01-ESPESSURA-004` | Em terreno plano, corte perpendicular à direção: t = w × sen(mergulho verdadeiro) | Compton 1985, *Geology in the Field*; geometria descritiva padrão de mapeamento | Confirmado |
| `GEO-M28-A02-ESCALAR-VETOR-001` | Escalar = número + unidade; vetor = número (módulo) + direção + sentido | Física geral básica; álgebra vetorial elementar | Confirmado |
| `GEO-M28-A02-DECOMPOSICAO-002` | Componente ao longo de uma direção = F·cos(θ); componente perpendicular = F·sen(θ) | Física geral básica — mesma convenção já usada (sem nomear) em [[27-fisica-geociencias-aula-02-forca-massa-leis-de-newton|27-fisica-geociencias-aula-02]] | Confirmado — recalculado de forma independente (500 N a 25°: 211 N e 453 N) |
| `GEO-M28-A02-SOMA-VETORIAL-003` | Soma de vetores não é soma aritmética simples de módulos; para vetores perpendiculares, o resultante vem do teorema de Pitágoras | Álgebra vetorial elementar; geometria | Confirmado — recalculado (√(211² + 453²) ≈ 500 N, reconstitui o vetor original) |
| `GEO-M28-A02-ORIENTACAO-VETOR-004` | Direção/mergulho de um plano pode ser representado por um vetor unitário na orientação do polo (perpendicular ao plano) | Rowland, Duebendorfer & Schiefelbein 2007, capítulo de projeção estereográfica | Confirmado — apresentado como interpretação/formalização, não como fato isolado, condizente com o registro `risk: interpretacao` já atribuído na aula |
| `GEO-M28-A03-DECAIMENTO-FORMULA-001` | N(t) = N₀ · e^(−λt) | Física nuclear consolidada; Faure & Mensing 2005 | Confirmado |
| `GEO-M28-A03-LAMBDA-MEIA-VIDA-002` | λ = ln(2) / T½ | Física nuclear consolidada; Faure & Mensing 2005 | Confirmado — recalculado (T½ = 1,25 Ga → λ ≈ 0,554/Ga) |
| `GEO-M28-A03-LOGARITMO-DEF-003` | log_b(x) = y ⟺ b^y = x | Matemática elementar | Confirmado |
| `GEO-M28-A03-FORMULA-IDADE-004` | t = −(1/λ)·ln(N/N₀), válida para qualquer razão N/N₀ | Álgebra elementar aplicada à lei do decaimento | Confirmado — recalculado (37% restante, K-40, T½ = 1,25 Ga → t ≈ 1,79 Ga, dentro do intervalo plausível entre 1 e 2 meias-vidas) |
| `GEO-M28-A03-MAGNITUDE-ESCALA-005` | ~10× amplitude e ~31,6× energia por unidade de magnitude sísmica; ~1.000× energia para 2 unidades | Confirmado por busca web: USGS — "each whole number increase in magnitude represents a tenfold increase in measured amplitude; each whole number step corresponds to release of about 31 times more energy" ([USGS FAQ — Moment magnitude, Richter scale](https://www.usgs.gov/faqs/moment-magnitude-richter-scale-what-are-different-magnitude-scales-and-why-are-there-so-many); [USGS — magnitude](https://pubs.usgs.gov/gip/earthq3/magnitude.html)) | Confirmado — recalculado (31,6² ≈ 1.000; 10² = 100) |
| `GEO-M28-A03-PHI-DEF-006` | φ = −log₂(diâmetro em mm) | Confirmado por busca web: definição padrão Krumbein (1934/1938), φ = −log₂(D/D₀), D₀ = 1 mm ([Springer, Phi Scale](https://link.springer.com/rwe/10.1007/978-94-017-8801-4_277); [Geosciences LibreTexts, Grain Size](https://geo.libretexts.org/Courses/SUNY_Potsdam/Sedimentary_Geology:_Rocks_Environments_and_Stratigraphy/03:_Describing_Sediment_and_Sedimentary_Rocks/3.01:_Grain_Size)) | Confirmado |
| `GEO-M28-A04-MEDIA-MEDIANA-001` | Média = soma/quantidade, sensível a extremos; mediana = valor central, resistente a extremos | Estatística descritiva elementar | Confirmado — recalculado no exemplo (média 246,2 Ma; mediana 244 Ma) |
| `GEO-M28-A04-DESVIO-PADRAO-002` | Desvio-padrão = raiz da variância (média dos quadrados dos desvios) | Estatística descritiva elementar | Confirmado |
| `GEO-M28-A04-INCERTEZA-DESVIO-003` | "±" reportado tipicamente corresponde ao desvio-padrão ou a um múltiplo declarado dele | Prática padrão de reporte de incerteza; Faure & Mensing 2005 | Confirmado |
| `GEO-M28-A04-COMPARAR-FAIXAS-004` | Compatibilidade estatística entre medidas exige comparar faixas (valor ± incerteza), não só valores centrais | Princípio padrão de comparação de medidas com incerteza; Dickin 2005 | Confirmado |
| `GEO-M28-A04-PRECISAO-NAO-EXATIDAO-005` | Desvio-padrão pequeno indica precisão, não garante exatidão | Retomada de [[27-fisica-geociencias-aula-01-grandezas-unidades-e-medida|27-fisica-geociencias-aula-01]]; metrologia | Confirmado — sem contradição com o Módulo 27 |

## Consistência interna e transversal verificada

- **Consistência com o Módulo 03 (meia-vida):** a aula 03 usa a mesma meia-vida de referência do potássio-40 (~1,25 Ga) já usada em [[03-tempo-geologico-geocronologia-aula-04-meia-vida|03-tempo-geologico-geocronologia-aula-04-meia-vida.md]], o mesmo vocabulário (razão pai/filho, sistema fechado) sem redefini-lo, e entrega exatamente a lacuna que aquela aula deixou explicitamente em aberto ("razões que não são meias-vidas inteiras exigem logaritmo, ferramenta que este curso ainda não ensinou"). Nenhuma contradição de valor ou de conceito encontrada.
- **Consistência com o Módulo 17 (mergulho/direção):** a aula 01 usa as mesmas definições de direção (strike) e mergulho (dip) já fixadas em [[17-geologia-estrutural-aula-06-mapas-e-secoes-estruturais-parte-1-atitude-e-padroes-de-afloramento|17-geologia-estrutural-aula-06]], sem alterar nomenclatura, e trata a regra do V (qualitativa naquela aula) como complementar, não como redundante — a aula 01 deste módulo é explícita sobre isso na seção "Por que isso importa além do exemplo do V". Nenhuma contradição encontrada.
- **Consistência com o Módulo 27 (grandezas, forças, incerteza):** a aula 02 formaliza com o vocabulário de vetores a decomposição de peso num talude já apresentada, sem nomear vetores, em [[27-fisica-geociencias-aula-02-forca-massa-leis-de-newton|27-fisica-geociencias-aula-02]] — mesmo ângulo, mesma lógica de decomposição, sem alterar convenção. A aula 04 formaliza o cálculo de incerteza a partir de medidas repetidas, que [[27-fisica-geociencias-aula-01-grandezas-unidades-e-medida|27-fisica-geociencias-aula-01]] introduziu apenas conceitualmente (precisão vs. exatidão), reutilizando a mesma distinção sem contradizê-la.
- **Consistência com o Módulo 26 (pH):** a aula 03 cita a escala de pH como exemplo de escala logarítmica sem repetir a explicação já dada em [[26-quimica-geociencias-aula-03-solucoes-concentracao-ph|26-quimica-geociencias-aula-03]], apenas remetendo a ela — consistente com a política de não duplicar conteúdo entre módulos da trilha de apoio.
- Todos os exemplos trabalhados (aulas 01 a 04) foram recalculados de forma independente; nenhuma discrepância aritmética encontrada (ver detalhes na coluna "Confiança" da tabela acima).
- Nenhuma aula deste módulo redefine vocabulário matemático ou geológico já usado em aulas anteriores do curso de forma divergente — checado por leitura cruzada.

## Correções aplicadas

Nenhuma. Nenhum achado 🔴/🟠/🟡/🔵/⚪ — nada a corrigir nesta rodada.

**Pendências:** nenhuma. O módulo está liberado para gerar o questionário final.
