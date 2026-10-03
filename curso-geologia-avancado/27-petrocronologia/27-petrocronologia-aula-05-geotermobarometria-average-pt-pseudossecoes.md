# Aula 05: Fundamentos de petrologia metamórfica (Parte 2) — geotermobarometria convencional, average P-T e pseudosseções

**ID:** geologia-avancado-m27-a05
**Módulo:** [[27-petrocronologia-modulo|Módulo 27 — Introdução à petrocronologia]]
**Duração estimada:** ~15 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** apresentar as ferramentas convencionais e modernas de geotermobarometria que atribuem valores numéricos de P e T aos estágios de crescimento lidos nas texturas e no zoneamento (Parte 1).
**Ao final você vai conseguir:** aplicar, em termos conceituais, um termômetro de troca Fe-Mg e o barômetro GASP a um par mineral coexistente; explicar por que o par isolado dá um ponto, e não um caminho; e dizer o que average P-T e pseudosseções resolvem em relação ao par isolado, e que hipóteses elas exigem.
**Pré-requisito:** [[27-petrocronologia-aula-04-petrologia-metamorfica-texturas-pt|Aula 04 — Parte 1]] (microdomínios, zoneamento de Mn, trajetórias P-T e a granada zonada do exemplo, que esta aula retoma) e [[27-petrocronologia-aula-03-tecnicas-analiticas-imageamento|Aula 03]] (a EPMA, que mede as composições usadas aqui).

> [!note] Esta aula é a **Parte 2** de um par. As Aulas 04 e 05 eram uma aula só até a revisão didática de 2026-09-22, que a dividiu por sobrecarga (seis blocos de conceitos independentes em ~30 min). Estude-as em sequência: a Parte 1 lê a rocha em termos **relativos** (qual estágio veio antes de qual); esta Parte 2 põe **números** de P e T nesses estágios.

## Conteúdo

### De onde paramos: um caminho com forma, mas sem números

A Parte 1 terminou com uma granada zonada cuja textura e cujo zoneamento de Mn contam uma história em ordem — núcleo antes da borda, crescimento prógrado contínuo — mas sem um único número de pressão ou de temperatura. Sabemos que o caminho subiu; não sabemos de onde a quanto. Esta aula apresenta as ferramentas que fazem essa conversão, de um microdomínio identificado por textura e composição para um ponto (ou um campo estreito) no diagrama P-T.

### Geotermobarometria convencional: colocando números no caminho

A **geotermobarometria** converte associações minerais em valores numéricos de pressão e temperatura, usando o equilíbrio termodinâmico entre fases coexistentes. Dois tipos clássicos de reação servem de base:

- **Termômetros de troca de Fe-Mg**: baseiam-se em reações de troca catiônica entre dois minerais coexistentes que trocam ferro e magnésio entre si sem mudar as demais proporções de fase — o par granada-biotita é o exemplo mais usado em metapelitos, calibrado experimentalmente por Ferry & Spear (1978) a partir de reações entre biotita e granada a pressão constante de 0,207 GPa (2,07 kbar) e temperaturas de até 800 °C, e refinado por trabalhos posteriores. A lógica física é que a partição de Fe e Mg entre os dois minerais depende da temperatura: em temperaturas mais altas, a distribuição de Fe e Mg entre granada e biotita se aproxima mais de uma distribuição aleatória; em temperaturas mais baixas, a partição se torna mais desigual, favorecendo um dos dois minerais. Medindo a razão Fe/Mg em ambos os minerais coexistentes (por EPMA, a mesma técnica da Aula 03), calcula-se uma temperatura.
- **Barômetros baseados em reações de volume molar**: dependem de reações em que o volume molar total dos produtos difere significativamente do volume molar dos reagentes, tornando o equilíbrio sensível à pressão. O exemplo clássico em metapelitos é o barômetro **GASP** (*garnet-aluminosilicate-plagioclase-quartz*, formalizado por Ghent, 1976, e calibrado termodinamicamente por Newton & Haselton, 1981), baseado no equilíbrio entre granada + Al₂SiO₅ (cianita, andaluzita ou silimanita) + quartzo de um lado e plagioclásio anortítico do outro — uma reação em que a diferença de volume molar entre os dois lados é grande o suficiente para tornar o equilíbrio um bom indicador de pressão.

O par termômetro + barômetro, aplicado à mesma associação mineral (tipicamente granada-biotita para T e granada-Al₂SiO₅-plagioclásio-quartzo para P, quando as quatro fases coexistem), fornece um ponto P-T único — mas apenas um ponto, referente ao momento em que aquela associação específica estava em equilíbrio químico. Para reconstruir um caminho inteiro, é preciso repetir esse exercício em vários microdomínios de composição diferente dentro do mesmo cristal zonado (por exemplo, núcleo e borda de uma granada), associando cada composição a um estágio do caminho.

### Além do par isolado: average P-T e pseudosseções

A abordagem de um único termômetro mais um único barômetro, embora historicamente importante e ainda amplamente usada, tem uma limitação: cada reação calibrada isoladamente carrega sua própria incerteza, e escolher arbitrariamente qual par de reações usar (há dezenas de termômetros e barômetros calibrados na literatura) pode introduzir inconsistência entre estimativas feitas com pares diferentes. Duas abordagens mais modernas tentam resolver isso:

- **Average P-T** (também chamada de termobarometria "ótima" ou multi-equilíbrio, implementada no software THERMOCALC de Powell & Holland): em vez de escolher uma única reação de troca e uma única reação de volume molar, o método usa **todas** as reações independentes possíveis entre as fases presentes simultaneamente, ponderando cada uma pela sua incerteza termodinâmica, e calcula um único par P-T (com elipse de incerteza) que melhor satisfaz o conjunto inteiro de equilíbrios — reduzindo a dependência do resultado à escolha arbitrária de qual par de reações privilegiar.
- **Pseudosseções** (calculadas por softwares como THERMOCALC, Perple_X — Connolly, 2005 — ou Theriak-Domino — de Capitani & Petrakakis, 2010): em vez de calcular um ponto P-T a partir de uma composição mineral já medida, o método calcula, a partir da composição **total** (em bloco) da rocha, quais associações minerais e quais composições de cada mineral são estáveis em cada ponto de um diagrama P-T inteiro. Comparando as composições previstas pela pseudosseção com as composições realmente medidas num domínio específico do cristal (núcleo, borda), é possível posicionar aquele domínio num campo estreito do diagrama P-T — uma abordagem que hoje é considerada mais robusta que o par isolado de termômetro e barômetro, embora dependa criticamente da composição total medida (bulk) estar correta e de o sistema ter atingido equilíbrio químico local, hipóteses que nem sempre se sustentam em rochas zonadas de crescimento prolongado.

Essas ferramentas — geotermobarometria convencional e pseudosseções — são o que converte um microdomínio identificado por textura e composição (como na Parte 1) num ponto ou num campo estreito de pressão e temperatura, que a Aula 07 vai finalmente conectar a uma idade numérica, fechando o ciclo textura → reação → P-T → idade que abriu a Parte 1.

## Exemplo trabalhado: pondo números na granada zonada da Parte 1

**Situação (retomada da Aula 04).** A mesma granada de metapelito: núcleo com Mn alto e foliação interna discordante da externa, zona intermediária com Mn decrescente, borda com Mn baixo contornada pela foliação externa. A Parte 1 já leu nela um crescimento prógrado contínuo, com o núcleo anterior à borda.

**Leitura P-T.** Aplicando o par granada-biotita (termômetro de Ferry & Spear, 1978) e GASP (barômetro de Ghent, 1976; Newton & Haselton, 1981) separadamente à composição do núcleo, da zona intermediária e da borda — usando, em cada caso, a biotita e o plagioclásio em contato textural com aquele domínio específico da granada —, obtêm-se pontos P-T distintos: o núcleo registra uma condição de temperatura mais baixa, o intervalo intermediário e a borda registram condições sucessivamente mais quentes, traçando um segmento prógrado do caminho P-T. Se a pressão também sobe entre núcleo e borda de forma proporcionalmente mais rápida que a temperatura, esse segmento é consistente com a porção inicial de um caminho horário — a assinatura de espessamento crustal discutida na Parte 1.

**O que falta.** Essa reconstrução dá a **forma** do caminho e os valores de P e T de cada estágio, mas não diz **quando**, em anos, cada estágio ocorreu, nem quanto tempo o cristal levou para crescer do núcleo à borda. É exatamente essa lacuna — P-T sem tempo — que a petrocronologia, com as ferramentas isotópicas in situ das Aulas 02 e 03, aplicadas aos próprios microdomínios já caracterizados aqui, vai preencher nas Aulas 06 e 07.

## Recap relâmpago

- Termômetros de troca Fe-Mg (granada-biotita, Ferry & Spear 1978) usam a partição de Fe e Mg entre dois minerais, que se aproxima da aleatória quanto mais quente; barômetros de volume molar (GASP, Ghent 1976; Newton & Haselton 1981) usam reações cujo equilíbrio se desloca com a pressão.
- O par termômetro + barômetro dá **um ponto** P-T, o do momento em que aquela associação estava em equilíbrio; um **caminho** exige repetir a conta em vários microdomínios (núcleo, zona intermediária, borda).
- Average P-T (multi-equilíbrio, THERMOCALC) usa todas as reações independentes de uma vez, ponderadas pela incerteza; pseudosseções (THERMOCALC, Perple_X, Theriak-Domino) partem da composição total da rocha e comparam composições previstas e medidas — ambas reduzem a dependência de uma única reação, ao custo de exigir composição total confiável e equilíbrio local.
- Com isto, as três primeiras etapas da ordem textura → reação → P-T → idade estão cobertas; a quarta começa na próxima aula.

## Próxima aula

[[27-petrocronologia-aula-06-minerais-acessorios-zircao-monazita|Aula 06 — Petrocronologia dos minerais acessórios]]: zircão, monazita, titanita, rutilo e apatita — como o zoneamento composicional discutido nas Aulas 04 e 05, aplicado a cada um desses minerais, vira um cronômetro amarrado a reações metamórficas específicas.

## Fontes

- Ferry, J. M. & Spear, F. S. (1978), "Experimental calibration of the partitioning of Fe and Mg between biotite and garnet", *Contributions to Mineralogy and Petrology*, 66, 113-117. doi:10.1007/BF00372150. Título, volume e paginação conferidos no Crossref pela auditoria (2026-09-22); pressão (2,07 kbar) e limite superior (800 °C) consistentes em todas as fontes. O limite inferior de temperatura dos experimentos diverge entre as fontes secundárias (500, 550 ou 600 °C) e não pôde ser conferido no original — por isso a aula não o cita.
- Ghent, E. D. (1976), "Plagioclase-garnet-Al2SiO5-quartz: a potential geobarometer-geothermometer", *American Mineralogist*, 61, 710-714 — formalização original do barômetro GASP. Paginação (61, 710-714) conferida no GeoScienceWorld pela auditoria (2026-09-22).
- Newton, R. C. & Haselton, H. T. (1981), "Thermodynamics of the garnet-plagioclase-Al2SiO5-quartz geobarometer", em Newton, R. C., Navrotsky, A. & Wood, B. J. (eds.), *Thermodynamics of Minerals and Melts*, Springer, 131-147 — calibração termodinâmica do GASP. VERIFICADO por busca nesta redação (2026-09-22): título e atribuição confirmados.
- Powell, R. & Holland, T. J. B. (1994), "Optimal geothermometry and geobarometry", *American Mineralogist*, 79, 120-133 — base do método average P-T implementado no THERMOCALC. Paginação conferida no GeoScienceWorld pela auditoria (2026-09-22); a atribuição do método a Powell & Holland (1994) e sua descrição como termobarometria "ótima" (multi-equilíbrio) foram confirmadas por busca.
- Connolly, J. A. D. (2005), "Computation of phase equilibria by linear programming: a tool for geodynamic modeling and its application to subduction zone decarbonation", *Earth and Planetary Science Letters*, 236, 524-541 — base do software Perple_X para cálculo de pseudosseções. Paginação conferida no Crossref pela auditoria (2026-09-22), doi:10.1016/j.epsl.2005.04.033.
- De Capitani, C. & Petrakakis, K. (2010), "The computation of equilibrium assemblage diagrams with Theriak/Domino software", *American Mineralogist*, 95, 1006-1016 — software Theriak-Domino para cálculo de pseudosseções, citado por busca nesta redação (2026-09-22) como referência padrão junto de THERMOCALC e Perple_X; conferido no Crossref pela auditoria, doi:10.2138/am.2010.3354.

<!--
nivel: avancado
palavras_corpo: 1275
palavras_corpo_metodo: "tokens separados por espaco entre '## Conteudo' e '## Fontes' (split do texto), incluindo o callout de nota fora dessa faixa nao contado; ~84 palavras/min, convencao do modulo 26."
duracao_estimada_min: 15

divisao_de_aula: "Parte 2 da antiga Aula 04 unica (2517 palavras, ~30,0 min, seis blocos de conceitos independentes e um exemplo). Criada pela revisao didatica de 2026-09-22 (achado DID-M27-A04-SOBRECARGA-SEIS-BLOCOS-002). Herdou, com texto integral e inalterado salvo a grafia 'pseudossecoes' e a referencia de numero de aula, as secoes 'Geotermobarometria convencional' e 'Alem do par isolado', o paragrafo de fechamento 'Essas ferramentas...', o passo 'Leitura P-T' e o passo 'O que falta' do exemplo trabalhado original, e o ultimo bullet do recap (desdobrado em tres). Acrescimos de ligacao sem fato novo: callout, secao de abertura, 'Situacao (retomada)' e o ultimo bullet do recap. Correcao de redacao no passo 'Leitura P-T': 'obtem-se dois pontos P-T' passou a 'pontos P-T distintos' e a zona intermediaria foi nomeada, porque o texto original listava tres dominios depois de anunciar dois."

mapa_objetivo_secao:
  geologia-avancado-m27-oa03: "Geotermobarometria convencional" + "Alem do par isolado" + "Exemplo trabalhado (Leitura P-T)"

alegacoes_auditaveis:
  # Os tres claims abaixo foram levantados quando esta aula e a Aula 04 eram uma so.
  # Mantem o prefixo A04 de proposito: sao identificadores estaveis aos quais o
  # relatorio e o manifesto da auditoria de 2026-09-22 apontam. Ler 'A04' neles como
  # 'levantado quando as Aulas 04 e 05 eram uma so'.
  - claim_id: PETROCRON-M27-A04-GRT-BT-THERMOMETER-005
    claim: "O termometro de troca Fe-Mg granada-biotita foi calibrado experimentalmente por Ferry & Spear (1978) a partir de reacoes entre biotita e granada a pressao constante de 0,207 GPa (2,07 kbar) e temperaturas de ate 800 C; e um dos termometros mais aplicados em petrologia metamorfica, com mais de 1400 citacoes."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-22): confirma titulo, volume/paginacao (Contributions to Mineralogy and Petrology 66, 113-117) e citacao de 'over 1400 citations'. ACHADO 7 DA AUDITORIA (2026-09-22, azul, corrigido por remocao): o limite inferior de temperatura (a redacao dizia 500 C) diverge entre as secundarias - 500 C (Wikipedia), 550 C (citacao do resumo), 600 C (Wu & Cheng 2006, Lithos 89, 1-23) - e o resumo original e fechado pela editora. Removido do texto; pressao e limite superior mantidos."
  - claim_id: PETROCRON-M27-A04-GASP-006
    claim: "O barometro GASP (granada-aluminossilicato-plagioclasio-quartzo) foi formalizado por Ghent (1976) e calibrado termodinamicamente por Newton & Haselton (1981), baseado no equilibrio entre granada+Al2SiO5+quartzo e plagioclasio anortitico, sensivel a pressao pela grande diferenca de volume molar entre os dois lados da reacao."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-22): confirma atribuicao a Ghent (1976) ('Ghent (1976) first devised three GASP barometer formalisms') e a Newton & Haselton (1981) ('Thermodynamics of the Garnet-Plagioclase-Al2SiO5-Quartz Geobarometer'). AUDITORIA (2026-09-22): Ghent 1976 conferido no GeoScienceWorld (61, 710-714); reacao 3 An = Grs + 2 Al2SiO5 + Qz."
  - claim_id: PETROCRON-M27-A04-AVERAGE-PT-PSEUDOSECOES-007
    claim: "O metodo average P-T (Powell & Holland 1994), implementado no THERMOCALC, usa multiplos equilibrios simultaneos ponderados por incerteza termodinamica para calcular um unico par P-T, reduzindo a dependencia de uma escolha arbitraria de par termometro-barometro; pseudossecoes (THERMOCALC, Perple_X de Connolly 2005, Theriak-Domino de de Capitani & Petrakakis 2010) calculam associacoes e composicoes minerais estaveis a partir da composicao total da rocha em todo um diagrama P-T."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-22): confirma atribuicao do average P-T a Powell & Holland (1994) como termobarometria 'otima', e Perple_X (Connolly 2005) e Theriak-Domino (de Capitani & Petrakakis 2010) como softwares padrao de calculo de pseudossecoes usando os mesmos bancos de dados termodinamicos de Holland & Powell. AUDITORIA (2026-09-22): as tres referencias conferidas (Crossref/GeoScienceWorld), paginacao correta."
  # O exemplo trabalhado continua registrado no claim PETROCRON-M27-A04-EXEMPLO-GRANADA-ZONADA-008,
  # que ficou no arquivo da Aula 04 (Parte 1), onde a granada e apresentada.
auditoria:
  data: 2026-09-22
  achados: "7 (azul, corrigido por remocao do dado nao verificavel) - aplicado antes da divisao, no texto que veio para esta aula"
-->
