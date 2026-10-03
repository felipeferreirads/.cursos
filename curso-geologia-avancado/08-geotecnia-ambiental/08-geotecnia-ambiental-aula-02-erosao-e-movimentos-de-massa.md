# Aula 02: Condicionantes geológico-geotécnicos de processos erosivos e movimentos gravitacionais de massa

**ID:** geologia-avancado-m08-a02
**Módulo:** [[08-geotecnia-ambiental-modulo|Módulo 08 — Geotecnia ambiental]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** identificar os condicionantes geológicos e geotécnicos que controlam a erosão hídrica (laminar, ravinamento, voçorocamento, piping) e os movimentos gravitacionais de massa, estimar a perda de solo pela USLE/RUSLE, classificar movimentos pelo sistema de Varnes e aplicar a retroanálise para calibrar parâmetros de resistência.

**Pré-requisito:** resistência ao cisalhamento em tensões efetivas, `τf = c' + σ'n·tan φ'` ([[06-elementos-de-geomecanica/06-elementos-de-geomecanica-aula-06-resistencia-ao-cisalhamento-e-prospeccao-geotecnica|Módulo 06, Aula 06]]); efeito da poropressão sobre `σ'` ([[06-elementos-de-geomecanica/06-elementos-de-geomecanica-aula-03-tensoes-totais-efetivas-neutras-k0|Módulo 06, Aula 03]]); modelo de talude infinito e a cadeia suscetibilidade–perigo–risco ([[07-mapeamento-geotecnico/07-mapeamento-geotecnico-aula-03-cartas-derivadas-aptidao-suscetibilidade-risco|Módulo 07, Aula 03]]).

## Antes de começar, você precisa saber

- O modelo de talude infinito, `FS = [c' + (γ·z·cos²β − u)·tan φ'] / (γ·z·sen β·cos β)`, e que a chuva desestabiliza a encosta elevando `u` e reduzindo `σ'n`, não adicionando peso (Módulo 07, Aula 03).
- A distinção entre **suscetibilidade** (predisposição do terreno, atemporal) e **risco** (com exposição e vulnerabilidade) — uma encosta suscetível e desocupada tem risco nulo (Módulo 07, Aula 03).

## Conteúdo

### Erosão hídrica: da laminar ao voçorocamento

A erosão hídrica evolui numa sequência de formas de energia crescente:

- **Erosão laminar** (*sheet erosion*): remoção difusa de uma lâmina fina de solo pelo escoamento não concentrado e pelo salpico da gota de chuva. É a mais insidiosa porque quase não deixa marca até que o horizonte superficial se esgote.
- **Sulcos** (*rills*): microcanais de poucos centímetros, ainda apagáveis pelo preparo do solo.
- **Ravinas** (*gullies*): canais de dezenas de centímetros a metros, incisos até o horizonte C, já não apagáveis por aração.
- **Voçorocas** (*voçorocamento*): feições de grande porte que atingem o lençol freático. A partir daí, o **fluxo de água subterrânea nas paredes e no fundo** passa a comandar a evolução por erosão interna e solapamento, e a voçoroca cresce mesmo sem chuva. É o estágio mais difícil e caro de estabilizar.

O condicionante geotécnico central é a **erodibilidade**, a suscetibilidade intrínseca do solo ao destacamento e ao transporte de partículas. Ela é máxima em solos de textura siltosa e areia fina, com baixa coesão, pouca matéria orgânica e estrutura fraca; e em **solos residuais de rochas graníticas e de arenitos**, onde a fração silte-areia fina domina. Argila bem estruturada e areia grossa resistem — a primeira por coesão, a segunda por peso da partícula.

### Piping e solos dispersivos

O **piping** (erosão interna, ou entubamento) é o carreamento de partículas pelo fluxo dentro do maciço, formando dutos que progridem de jusante para montante até criar um caminho passante. É uma das duas causas históricas dominantes de ruptura de barragens de terra — ao lado do galgamento —, responde por parcela comparável do total nos levantamentos de acidentes, e opera também em maciços de aterro, no fundo de voçorocas e em taludes de corte com surgência.

Uma classe de solo é especialmente vulnerável: os **solos dispersivos**, argilas com alta proporção de sódio trocável (elevada PST / SAR) cujas partículas se defloculam espontaneamente em contato com água de baixa salinidade, sem necessidade de velocidade de fluxo. Não são identificados pelos ensaios de granulometria e Atterberg convencionais; exigem ensaios específicos — **pinhole test** (Sherard et al., 1976), **crumb test**, ensaio de dupla hidrometria e química do extrato de saturação. Aterros e diques construídos com solo dispersivo sem tratamento (adição de cal, filtros bem graduados) rompem por piping poucos anos após a construção.

### Quantificar a perda de solo: USLE e RUSLE

A **Equação Universal de Perda de Solo** estima a perda média anual de solo **em vertente** como o produto de cinco fatores:

`A = R · K · LS · C · P`

- `R` — **erosividade da chuva**: energia cinética × intensidade máxima em 30 min, integrada no ano. É o que o clima impõe. Em regiões tropicais úmidas brasileiras fica tipicamente entre 5 000 e 12 000 (unidades métricas).
- `K` — **erodibilidade do solo**: perda por unidade de `R` numa parcela-padrão. É a propriedade discutida acima, estimada por nomograma a partir de textura, matéria orgânica, estrutura e permeabilidade. Cuidado com a colisão de símbolo: aqui `K` **não** é condutividade hidráulica.
- `LS` — **fator topográfico**: comprimento e declividade da rampa, combinados. É a geometria da encosta.
- `C` — **uso e manejo da cobertura**: razão entre a perda sob a cobertura real e a perda em solo descoberto. Vai de ~1,0 (solo nu) a ~0,004 (floresta).
- `P` — **práticas conservacionistas**: terraceamento, plantio em nível, cordões vegetados. Vale 1,0 quando não há prática alguma.

A **RUSLE** mantém a estrutura e reformula os fatores com base empírica mais ampla. Note a divisão de trabalho: `R` e `LS` são dados do sítio, praticamente não manipuláveis; `K` muda muito lentamente; **`C` e `P` são as alavancas de intervenção** — e `C` é a de maior efeito, como o exemplo trabalhado mostra.

### Movimentos gravitacionais de massa: a classificação de Varnes

O sistema de Varnes (1978) classifica os movimentos por **tipo de movimento** × **tipo de material** (rocha, detrito, solo/terra):

| Tipo de movimento | Descrição | Exemplos |
|---|---|---|
| Queda (*fall*) | Destacamento livre de blocos de face íngreme | Queda de blocos rochosos |
| Tombamento (*topple*) | Rotação de coluna à frente do seu centro de gravidade | Tombamento de lajes verticalizadas |
| Escorregamento (*slide*) | Deslocamento sobre superfície de ruptura definida — **rotacional** (superfície curva, maciço homogêneo) ou **translacional/planar** (superfície plana, controle estrutural ou de contato) | Rotacional em aterro; translacional raso em colúvio sobre rocha |
| Expansão lateral (*spread*) | Fraturamento e extensão de massa rígida sobre camada que se liquefaz ou flui | Solos sensíveis, rejeitos |
| Fluxo (*flow*) | Movimento com deformação interna contínua, sem superfície de ruptura discreta | Corrida de detritos (*debris flow*), corrida de lama |
| Complexo | Combinação sequencial de dois ou mais | Escorregamento que evolui para corrida |

> [!note] O que a atualização de 2014 mudou
> Hungr, Leroueil & Picarelli (2014) detalharam os tipos em 32 classes e subdividiram o eixo de material (rocha; solo em argila/silte e areia/pedregulho/detrito). Nessa revisão a classe **"complexo" foi abandonada**: descreve-se a **sequência** observada ("escorregamento rotacional que evolui para corrida de detritos") em vez de um rótulo genérico. A linha "Complexo" da tabela é, portanto, de Varnes (1978).

Para a geotecnia ambiental, dois casos são recorrentes: o **escorregamento translacional raso** deflagrado por chuva em encostas de ocupação irregular, e as **corridas de detritos** canalizadas, que transportam o material a grandes distâncias e atingem áreas fora da encosta de origem. A expansão lateral em material que se liquefaz é o elo com a Aula 05 (rejeitos).

### Deflagração por poropressão e retroanálise

A maioria dos escorregamentos rasos em clima tropical é deflagrada pela **elevação da poropressão** durante ou logo após chuvas intensas ou prolongadas, pelo mecanismo já visto no Módulo 07: `u` sobe, `σ'n` cai, a parcela friccional `σ'n·tan φ'` da resistência despenca, e `FS` cruza 1. Cortes de talude para autoconstrução, lançamento de água servida e de lixo, e remoção da vegetação aceleram o processo.

A **retroanálise** (*back-analysis*) inverte o raciocínio do cálculo de estabilidade: dado um escorregamento que **efetivamente ocorreu**, sabe-se que `FS = 1` no instante da ruptura. Fixando a geometria observada e o regime de poropressão estimado para aquele momento, resolve-se a equação de equilíbrio para os parâmetros de resistência mobilizados (`c'`, `φ'`). É a forma mais confiável de obter parâmetros operacionais de projeto para o restante de uma encosta ou para encostas geologicamente análogas, porque incorpora automaticamente efeitos de escala, de estrutura relíquia e de fissuras que o ensaio de laboratório em corpo de prova pequeno não captura.

### Fator de segurança de projeto

Não existe um `FS` único: ele depende da confiança nos parâmetros, das consequências da ruptura e da condição analisada. Referências correntes para taludes permanentes: `FS ≥ 1,5` para condição drenada de longo prazo com boa investigação; `FS ≥ 1,3` para fim de construção (não drenada) ou carregamento transitório; valores maiores quando há população exposta a jusante. Abordagens probabilísticas substituem o `FS` determinístico pela probabilidade de ruptura, mais transparente quando a incerteza dos parâmetros é grande.

## Exemplo trabalhado

**Situação:** duas partes.
**(a)** Estime a perda de solo anual, pela USLE, de uma encosta de pastagem degradada: `R = 6500` (erosividade), `K = 0,035` (erodibilidade — não confundir com condutividade hidráulica), `LS = 2,1` (topográfico), `C = 0,12` (pastagem degradada), `P = 1,0` (sem práticas conservacionistas), em unidades métricas usuais.
**(b)** Um escorregamento translacional raso ocorreu numa encosta vizinha, em colúvio de `z = 3,0 m`, `β = 22°`, `γsat = 19 kN/m³`, com o lençol na superfície e fluxo paralelo à encosta no instante da ruptura. Ensaios independentes indicam `φ' = 32°`. Estime o `c'` mobilizado na ruptura. Use `γw = 9,81 kN/m³`.

**Resolução — parte (a):**
`A = R·K·LS·C·P = 6500 × 0,035 × 2,1 × 0,12 × 1,0`
`A = 227,5 × 2,1 × 0,12 = 57,3 t·ha⁻¹·ano⁻¹`

A tolerância de perda de solo fica tipicamente entre 4 e 12 t·ha⁻¹·ano⁻¹, conforme a profundidade e a taxa de formação do solo. A encosta perde, portanto, de **cinco a catorze vezes** o tolerável — é essa faixa, e não um múltiplo único, que se declara. Trocar `C = 0,12` (pastagem degradada) por `C ≈ 0,004` (floresta) levaria `A` a ~1,9 t·ha⁻¹·ano⁻¹ — a cobertura vegetal é o fator sobre o qual a intervenção tem maior efeito.

**Resolução — parte (b):**
Termos geométricos (β = 22°): `cos β = 0,9272`, `cos²β = 0,8597`, `sen β = 0,3746`.

Tensão cisalhante motriz na superfície de ruptura:
`τ = γ·z·sen β·cos β = 19 × 3 × 0,3746 × 0,9272 = 57 × 0,3474 = 19,80 kPa`

Tensão normal total: `γ·z·cos²β = 57 × 0,8597 = 49,00 kPa`
Poropressão: `u = γw·z·cos²β = 9,81 × 3 × 0,8597 = 25,30 kPa`
Tensão normal efetiva: `σ'n = 49,00 − 25,30 = 23,70 kPa`

Na ruptura, `FS = 1` → `τ = c' + σ'n·tan φ'`:
`19,80 = c' + 23,70 × tan 32° = c' + 23,70 × 0,6249 = c' + 14,81`
`c' = 4,99 ≈ 5,0 kPa`

**Interpretação:** a retroanálise fixa o par (`c' = 5 kPa`, `φ' = 32°`) como a combinação de resistência compatível com a ruptura observada, sob a poropressão máxima. Esse par — e não o valor de um ensaio triaxial de laboratório — é o que deve alimentar o cálculo de estabilidade das encostas geologicamente equivalentes do entorno e o projeto de contenção. Note quanto o resultado depende da hipótese de poropressão: se o lençol estivesse a 0,5 m de profundidade em vez de na superfície, `u` cairia e o `c'` inferido seria menor, mostrando por que a reconstituição das condições hidrológicas do dia da ruptura é a parte mais delicada da retroanálise.

## Erros comuns

- **Estabilizar uma voçoroca só na superfície**, ignorando que, uma vez atingido o lençol, é o fluxo subterrâneo que comanda a evolução por solapamento das paredes.
- **Aceitar solo em aterro ou dique sem ensaio de dispersividade** — o pinhole test não é substituível por granulometria e Atterberg.
- **Usar a USLE para prever a produção de sedimento de uma bacia.** A USLE estima perda bruta em vertente; o aporte ao curso d'água exige a razão de aporte de sedimentos (*SDR*), sempre menor que 1.
- **Fazer retroanálise com dois parâmetros livres (`c'` e `φ'`) e uma só equação**, obtendo infinitas soluções. Fixa-se um (em geral `φ'`, por ensaio ou por tipo de solo) e resolve-se para o outro.
- **Aplicar o modelo de talude infinito a ruptura rotacional profunda** — ele descreve apenas rupturas planares rasas paralelas à encosta (Módulo 07).
- **Confundir a classe de material com o tipo de movimento** na classificação de Varnes: são dois eixos independentes.

## O que não concluir

- **Que `FS > 1,5` garante estabilidade.** O `FS` só é tão bom quanto os parâmetros e a hipótese de poropressão que o alimentam; encostas com `FS` calculado alto rompem quando a poropressão excede a assumida ou quando há um plano de fraqueza não mapeado.
- **Que erosão e movimento de massa são processos separados.** Voçorocas destabilizam taludes ao pé; escorregamentos expõem solo à erosão acelerada. Na prática atuam encadeados.
- **Que a retroanálise fornece "os" parâmetros verdadeiros do solo.** Fornece o par de resistência **operacional** para aquela geometria e aquele modelo — que já é o que interessa para o projeto, mas não é uma propriedade de laboratório.

## Recap relâmpago

- A erosão hídrica evolui de laminar → sulcos → ravinas → voçorocas; ao atingir o lençol, o fluxo subterrâneo comanda o crescimento da voçoroca por solapamento.
- Erodibilidade é máxima em siltes e areia fina de baixa coesão e em solos residuais de granito e arenito; solos dispersivos (Na trocável alto) defloculam sem velocidade de fluxo e exigem pinhole test.
- Piping (erosão interna) é uma das duas causas dominantes de ruptura de barragens de terra, ao lado do galgamento.
- A USLE/RUSLE estima a perda de solo em vertente: `A = R·K·LS·C·P` — erosividade da chuva, erodibilidade do solo, fator topográfico, cobertura e manejo, práticas conservacionistas. `R` e `LS` são dados do sítio; `C` e `P` são as alavancas de intervenção, e `C` é a de maior efeito.
- Varnes (1978) classifica movimentos por tipo (queda, tombamento, escorregamento rotacional/translacional, expansão lateral, fluxo, complexo) × material (rocha, detrito, solo); a atualização de Hungr, Leroueil & Picarelli (2014) detalhou os tipos em 32 classes, subdividiu o eixo de material e **abandonou a classe "complexo"** em favor de descrever a sequência de movimentos.
- A maioria dos escorregamentos rasos tropicais é deflagrada por elevação de poropressão; a **retroanálise** (assumindo `FS = 1` na ruptura) calibra os parâmetros de resistência operacionais.
- O `FS` de projeto não é único: ~1,5 (drenado, longo prazo), ~1,3 (fim de construção), maior com população exposta.

## Próxima aula

[[08-geotecnia-ambiental-aula-03-residuos-solidos-e-selecao-de-areas|Aula 03 — Resíduos sólidos e seleção de áreas de disposição: Política Nacional de Resíduos Sólidos e plumas de contaminação]]

## Anterior

[[08-geotecnia-ambiental-aula-01-conceitos-e-propriedades-geotecnicas|Aula 01 — Geotecnia ambiental: conceitos, abrangência e propriedades geotécnicas relevantes]]

## Fontes

- Varnes, D. J. (1978), "Slope movement types and processes", in *Landslides: Analysis and Control*, TRB Special Report 176, National Academy of Sciences, p. 11–33.
- Hungr, O., Leroueil, S. & Picarelli, L. (2014), "The Varnes classification of landslide types, an update", *Landslides*, 11(2), p. 167–194.
- Wischmeier, W. H. & Smith, D. D. (1978), *Predicting Rainfall Erosion Losses — A Guide to Conservation Planning*, USDA Agriculture Handbook 537.
- Renard, K. G., Foster, G. R., Weesies, G. A., McCool, D. K. & Yoder, D. C. (1997), *Predicting Soil Erosion by Water: A Guide to Conservation Planning with the Revised Universal Soil Loss Equation (RUSLE)*, USDA Agriculture Handbook 703.
- Sherard, J. L., Dunnigan, L. P., Decker, R. S. & Steele, E. F. (1976), "Pinhole test for identifying dispersive soils", *Journal of the Geotechnical Engineering Division, ASCE*, 102(GT1), p. 69–85.
- Fell, R., Corominas, J., Bonnard, C. et al. (2008), "Guidelines for landslide susceptibility, hazard and risk zoning for land use planning", *Engineering Geology*, 102(3–4), p. 85–98.
- Augusto Filho, O. & Virgili, J. C. (1998), "Estabilidade de taludes", in Oliveira & Brito (eds.), *Geologia de Engenharia*, ABGE, São Paulo, cap. 15.
- Salomão, F. X. T. (1998), "Controle e prevenção dos processos erosivos", in Oliveira & Brito (eds.), *Geologia de Engenharia*, ABGE, São Paulo, cap. 13 (erodibilidade de solos residuais brasileiros).
- Bertoni, J. & Lombardi Neto, F. (2012), *Conservação do Solo*, 8ª ed., Ícone, São Paulo (fator K e tolerância de perda de solo em condições brasileiras).
- Foster, M., Fell, R. & Spannagle, M. (2000), "The statistics of embankment dam failures and accidents", *Canadian Geotechnical Journal*, 37(5), p. 1000–1024 (participação relativa de erosão interna e galgamento).

<!--
nivel: avancado
palavras_corpo: ~2060
# Ressalva registrada na revisão didática (DID-M08-A02-EXTENSAO): acima do teto de ~1900.
# O excedente é a seção "Quantificar a perda de solo: USLE e RUSLE", acrescentada na revisão
# para fechar um objetivo declarado que nenhuma seção ensinava (DID-M08-A02-USLE-001).

mapa_objetivo_secao:
  geologia-avancado-m08-oa02: "Erosão hídrica: da laminar ao voçorocamento" + "Piping e solos dispersivos" + "Quantificar a perda de solo: USLE e RUSLE" + "Movimentos gravitacionais de massa: a classificação de Varnes" + "Deflagração por poropressão e retroanálise" + "Fator de segurança de projeto" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOAMB-M08-A02-EROSAO-SEQ-001
    claim: "A erosão hídrica evolui de laminar para sulcos, ravinas e voçorocas por energia crescente do escoamento; ao atingir o lençol freático, a voçoroca passa a evoluir por erosão interna e solapamento comandados pelo fluxo de água subterrânea, podendo crescer sem chuva."
    risk: fato
    source: "Augusto Filho & Virgili 1998; IPT/ABGE Geologia de Engenharia, cap. de processos erosivos"
  - claim_id: GEOAMB-M08-A02-ERODIBILIDADE-002
    claim: "A erodibilidade do solo é máxima em texturas siltosas e areia fina de baixa coesão e baixo teor de matéria orgânica, e em solos residuais de rochas graníticas e de arenitos; argila bem estruturada e areia grossa são mais resistentes."
    risk: fato
    source: "Wischmeier & Smith 1978 e Renard et al. 1997 (nomograma do fator K: textura, matéria orgânica, estrutura, permeabilidade); Salomão 1998 e Bertoni & Lombardi Neto 2012 (erodibilidade de solos residuais de granito e de arenito no Brasil — a parte litológica da alegação não decorre do fator K da USLE)"
  - claim_id: GEOAMB-M08-A02-DISPERSIVOS-003
    claim: "Solos dispersivos são argilas com alta proporção de sódio trocável que defloculam em água de baixa salinidade sem necessidade de velocidade de fluxo, não são identificados por granulometria e limites de Atterberg, e exigem ensaios específicos como o pinhole test, o crumb test e a dupla hidrometria."
    risk: fato
    source: "Sherard et al. 1976"
  - claim_id: GEOAMB-M08-A02-PIPING-008
    claim: "O piping (erosão interna) é o carreamento de partículas pelo fluxo dentro do maciço, com dutos que progridem de jusante para montante; é uma das duas causas dominantes de ruptura de barragens de terra, ao lado do galgamento, com participação comparável nos levantamentos estatísticos de acidentes."
    risk: fato
    source: "Foster, Fell & Spannagle 2000, Canadian Geotechnical Journal 37(5); Terzaghi, Peck & Mesri 1996, cap. 4 (Módulo 06, Aula 04)"
  - claim_id: GEOAMB-M08-A02-USLE-004
    claim: "A Equação Universal de Perda de Solo estima a perda média anual de solo em vertente como A = R·K·LS·C·P; ela estima perda bruta na vertente, não a produção de sedimento de uma bacia, que requer a razão de aporte de sedimentos."
    risk: fato
    source: "Wischmeier & Smith 1978; Renard et al. 1997"
  - claim_id: GEOAMB-M08-A02-VARNES-005
    claim: "A classificação de Varnes (1978) organiza os movimentos gravitacionais de massa por tipo de movimento (queda, tombamento, escorregamento rotacional ou translacional, expansão lateral, fluxo, complexo) cruzado com o tipo de material (rocha, detrito, solo/terra). A atualização de Hungr, Leroueil & Picarelli (2014) detalhou os tipos em 32 classes, subdividiu o eixo de material (rocha; solo em argila/silte e areia/pedregulho/detrito) e ABANDONOU a classe 'complexo', recomendando descrever o movimento composto pela sequência de tipos observada."
    risk: fato
    source: "Varnes 1978; Hungr, Leroueil & Picarelli 2014, Landslides 11(2)"
  - claim_id: GEOAMB-M08-A02-RETROANALISE-006
    claim: "Na retroanálise de um escorregamento, assume-se FS = 1 no instante da ruptura e resolve-se a equação de equilíbrio, com a geometria observada e a poropressão estimada para aquele momento, para os parâmetros de resistência mobilizados; fixa-se um parâmetro (em geral φ') e resolve-se para o outro, pois há uma equação e dois incógnitos."
    risk: fato
    source: "Duncan, Wright & Brandon 2014, Soil Strength and Slope Stability, cap. 12; Augusto Filho & Virgili 1998"
  - claim_id: GEOAMB-M08-A02-BACKCALC-007
    claim: "Para z = 3,0 m, β = 22°, γsat = 19 kN/m³, lençol na superfície com fluxo paralelo (u = γw·z·cos²β = 25,3 kPa) e φ' = 32°, a retroanálise pelo modelo de talude infinito fornece c' mobilizado ≈ 5,0 kPa; e a USLE com R = 6500, K = 0,035, LS = 2,1, C = 0,12, P = 1,0 fornece A ≈ 57 t·ha⁻¹·ano⁻¹."
    risk: calculo
    source: "Cálculo pelo modelo de talude infinito (Módulo 07, Aula 03) e pela USLE"
-->
