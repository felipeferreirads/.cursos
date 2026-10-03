# Auditoria científica: Módulo 19 — Geofísica: métodos e imageamento da Terra

**Auditado em:** 2026-08-18
**Material:** `19-geofisica-metodos/` — seis aulas, questionário final e baralho de flashcards (`.md`, `-basic.csv`, `-cloze.csv`)
**Modo:** audit-and-fix
**Profundidade:** full
**Escopo:** sismologia e ondas sísmicas, sísmica de reflexão e refração, gravimetria, magnetometria, métodos elétricos/EM/geotérmicos, perfilagem de poços e integração; consistência entre aulas e entre aulas e material derivado
**Veredito da Fase 1:** Requer correção
**Veredito após a Fase 2:** Aprovado (todos os achados corrigidos; nenhum 🔴/🟠/⚪ aberto)

## Resumo da Fase 1

🔴 1 erro · 🟠 10 imprecisões · 🟡 0 desatualizados · 🔵 1 sem fonte · ⚪ 1 controverso Verificadas e corretas: 18 alegações de risco.

O módulo é sólido no essencial: os mecanismos físicos centrais (não unicidade, contraste de impedância, refração crítica, condução iônica, limite de Curie, amarração poço-sísmica) estão corretos, e os números de maior risco — 103°/142° da zona de sombra, 32× de energia por grau de magnitude, 580 °C da magnetita, 2,67 g/cm³ da correção Bouguer, 25–30 °C/km do gradiente geotérmico — passaram na verificação. Os achados se concentram em três lugares previsíveis: **atribuições históricas comprimidas**, **um mineral nomeado no lugar do certo**, e **tabelas de controle do questionário e do baralho que não batem com o próprio conteúdo que descrevem**.

## Achados

### 🔴 1. Minerais formadores de rocha descritos como "isolantes elétricos muito pobres"

**claim_id:** `GFI-M19-RESIST-INSULATOR-001`
**Tipo:** erro factual (inversão de sentido)
**Onde:** aula 05 · "O que faz uma rocha conduzir eletricidade"
**Está escrito:** "minerais formadores de rocha (quartzo, feldspato, calcita) são, em geral, isolantes elétricos muito pobres."
**Problema:** a frase afirma o oposto do que a aula quer ensinar e do que é verdade. Quartzo, feldspato e calcita são **excelentes** isolantes — isto é, condutores muito pobres. Dizer que são "isolantes muito pobres" afirma que isolam mal, ou seja, que conduzem bem, o que contradiz o resto do próprio parágrafo (que atribui toda a condução à água dos poros). Como está, é a afirmação que um aluno pode memorizar invertida.
**Correção aplicada:** "a rocha em si quase não conduz: minerais formadores de rocha (quartzo, feldspato, calcita) são, em geral, excelentes isolantes elétricos — ou seja, condutores muito pobres."
**Fonte:** Burnley, *Resistivity of Earth Materials* (UNLV, notas de curso: "most rock forming minerals are insulators"); US EPA, [Electrical Methods](https://www.epa.gov/environmental-geophysics/electrical-methods); Britannica, *Rock — Electrical properties* · **Nível:** base de referência / revisada por pares
**Confiança:** confirmado
**Também aparece em:** questionário final, comentário do gabarito da Q9 ("mineral sólido comum é isolante pobre") — mesma inversão, corrigida junto.

### 🟠 2. Ilmenita apresentada como mineral fortemente magnético

**claim_id:** `GFI-M19-MAG-ILMENITE-002`
**Tipo:** erro factual de nomenclatura mineral (severidade 🟠: a família de minerais está certa, o membro nomeado não)
**Onde:** aula 04 · "Por que magnetita domina tudo"
**Está escrito:** "minerais fortemente magnéticos — sobretudo a **magnetita** (Fe₃O₄), e em menor grau a ilmenita e a pirrotita."
**Problema:** a ilmenita (FeTiO₃) é **paramagnética à temperatura ambiente** — sua temperatura de Néel fica em torno de −218 °C (40–80 K) —, e portanto praticamente não contribui para a anomalia magnética medida em superfície. Os óxidos de Fe-Ti que de fato importam são as **titanomagnetitas** (série magnetita–ulvoespinélio, com temperatura de Curie de 200 a 580 °C) e as intercrescências hemo-ilmeníticas ferrimagnéticas (composições Ilm 0,5–0,8), além da pirrotita. Nomear justamente o membro paramagnético da série como contribuinte magnético inverte o critério que a aula está tentando ensinar.
**Correção aplicada:** substituída ilmenita por titanomagnetita na lista, mantida a pirrotita, e acrescentada a ressalva explícita de que a ilmenita pura é paramagnética à temperatura ambiente e de que quem responde, nas rochas que a contêm, são as intercrescências e fases ricas em magnetita associadas.
**Fonte:** Haggerty, *Mineralogical constraints on Curie isotherms in deep crustal magnetic anomalies*, GRL 5(2), 1978; McEnroe et al., *Magnetism at Depth*, G³ 19, 2018; Lawson et al., GRL 11(3), 1984 (série ilmenita-hematita) · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** aula 04, bullet de pré-requisito (ajustado para "minerais opacos de Fe-Ti", sem afirmar magnetismo). Nenhum flashcard nem questão citava ilmenita.

### 🟠 3. Moho atribuída a um levantamento de refração com fonte artificial

**claim_id:** `GFI-M19-MOHO-DISCOVERY-003`
**Tipo:** confusão de escopo (histórica)
**Onde:** aula 02 · "Refração: quando a onda corre ao longo da interface" e Recap
**Está escrito:** "inclusive foi o método usado nos primeiros **levantamentos** que definiram a descontinuidade de Mohorovičić" e "A refração histórica foi o método que definiu a descontinuidade de Mohorovičić (Moho)."
**Problema:** o princípio físico está certo — a Moho foi identificada por ondas refratadas criticamente (ondas de cabeça) chegando antes da direta a grandes distâncias. O que está errado é o contexto: Andrija Mohorovičić não realizou levantamento algum. Em 1909 ele analisou os sismogramas de um **terremoto natural** (vale do Kupa/Pokupsko, Croácia, 8 de outubro de 1909), no qual identificou, além de ~200–300 km, um segundo conjunto de chegadas P mais rápidas, deduzindo um salto de velocidade de 5,68 para 7,75 km/s. Como a frase está inserida num capítulo inteiramente dedicado a fontes artificiais controladas, ela ensina que a Moho saiu de um levantamento de exploração — o que não ocorreu; a refração com fonte controlada só passou a mapear a Moho depois.
**Correção aplicada:** reescrito o trecho e o recap para atribuir a identificação a Mohorovičić em 1909, a partir de curvas de tempo-percurso de um terremoto natural, com a ressalva explícita de que não houve fonte artificial e de que os levantamentos controlados vieram depois.
**Fonte:** Mohorovičić (1909/1910); Prodehl & Mooney, *100 years of seismic research on the Moho*, Tectonophysics 609, 2013; Geotech d.o.o. Rijeka, [Discovery of Mohorovičić's discontinuity](https://www.geotech.hr/en/discovery-of-mohorovicics-moho-discontinuity/) · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** flashcard `fb020` e cloze `fc012` (ambos afirmavam "definida a partir de dados de sísmica de refração") e o bloco `alegacoes_auditaveis` da aula 02 — todos corrigidos.

### 🟠 4. Detecção do núcleo interno confundida com demonstração de que ele é sólido

**claim_id:** `GFI-M19-INNERCORE-SOLID-004`
**Tipo:** certeza indevida / omissão que gera erro
**Onde:** aula 01 · "A zona de sombra: como um núcleo líquido aparece num gráfico"
**Está escrito:** "Mais tarde, a detecção de ondas P refratadas de volta a partir de uma superfície ainda mais interna revelou o **núcleo interno sólido**, dentro do núcleo externo líquido."
**Problema:** a aula acabou de ensinar, corretamente, que ondas P atravessam líquidos tão bem quanto sólidos — e logo em seguida usa uma observação feita **só com ondas P** como prova de solidez. Inge Lehmann (1936) detectou o núcleo interno por chegadas P (PKiKP) dentro da zona de sombra; esses dados não podiam estabelecer solidez. Birch (1940) e Bullen (1946) argumentaram a favor dela a partir do contraste de velocidade, e a validação veio com a sensibilidade a cisalhamento e densidade dos **modos normais** de vibração da Terra (Dziewonski & Gilbert, 1971). Deixar como está ensina o aluno a aplicar mal o próprio critério P/S que é o coração da aula.
**Correção aplicada:** separada a detecção (Lehmann, 1936) da solidez, com a ressalva de que ondas P sozinhas não bastariam e a atribuição da validação aos modos normais (Dziewonski & Gilbert, 1971).
**Fonte:** Dziewonski & Gilbert, *Solidity of the inner core of the Earth inferred from normal mode observations*, Nature 234, 1971; *Revisiting Seismological Discoveries of the Inner Core*, SRL 97(1), 2026; APS, [Lehmann concludes Earth has an inner core](https://www.aps.org/apsnews/2023/08/seismologist-lehmann-earth-inner-core) · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** nenhum arquivo derivado — os cards `fb010` e `fc005` só tratam do núcleo **externo** líquido, e estão corretos.

### 🟠 5. Delimitação da zona de sombra datada de "ao redor de 1906"

**claim_id:** `GFI-M19-SHADOW-HISTORY-005`
**Tipo:** erro factual (atribuição histórica)
**Onde:** aula 01 · "A zona de sombra"
**Está escrito:** "Ao redor de 1906, observou-se que estações a certas distâncias angulares do epicentro (aproximadamente entre 103° e 142° de arco […]) não recebiam ondas P diretas."
**Problema:** os **valores angulares estão corretos** e foram verificados (P ausente entre ~103° e ~142°; S ausente além de ~103°), mas não são de 1906. Richard Oldham, em 1906, inferiu a existência de um núcleo a partir de tempos de chegada anômalos, sem delimitar a faixa; a observação e a delimitação da zona de sombra, com a profundidade do limite núcleo-manto, são de Beno Gutenberg, em 1913–1914. O próprio bloco `alegacoes_auditaveis` da aula já listava "Oldham 1906, Gutenberg 1913" — o corpo do texto é que comprimiu os dois num só evento.
**Correção aplicada:** atribuída a inferência do núcleo a Oldham (1906) e a delimitação da zona de sombra a Gutenberg (1913–1914), preservando os valores angulares.
**Fonte:** IRIS/EarthScope, [Seismic Shadow Zones](https://www.iris.edu/hq/inclass/animation/seismic_shadow_zone_basic_introduction); USGS, [Shadow Zone](https://www.usgs.gov/media/videos/shadow-zone) · **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** nenhum arquivo derivado — nem o questionário (Q2) nem os cards (`fb010`, `fc005`) carregam a data.

### 🟠 6. Velocidade da onda P na crosta dada como 5–8 km/s

**claim_id:** `GFI-M19-PVEL-CRUST-006`
**Tipo:** imprecisão numérica
**Onde:** aula 01 · "Dois tipos de onda de corpo, duas físicas diferentes"
**Está escrito:** "é a mais rápida das ondas sísmicas (tipicamente 5–8 km/s na crosta, mais rápida ainda no manto profundo)."
**Problema:** 8 km/s não é valor de crosta, é o valor do manto imediatamente abaixo do Moho (Pn ≈ 8,0–8,1 km/s, faixa 7,6–8,8). A velocidade média global da crosta é ≈ 6,45 km/s, e a crosta superior/média fica em 6,0–6,5 km/s. Absorver 8 km/s dentro da faixa "crosta" apaga exatamente o salto de velocidade que **define** a Moho — o mesmo salto que a aula 02 usa duas aulas depois (5,68 → 7,75 km/s no dado original de Mohorovičić). É um caso em que a imprecisão numérica destrói um conceito posterior.
**Correção aplicada:** "tipicamente em torno de 6 km/s na crosta continental, variando com litologia e profundidade, e saltando para cerca de 8 km/s no manto logo abaixo do Moho, mais rápida ainda em profundidade."
**Fonte:** Christensen & Mooney, *Seismic Velocity Structure and Composition of the Continental Crust: A Global View*, JGR 100(B7), 1995; Mooney, *Seismic Velocity Structure of the Continental Lithosphere* (USGS) · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** nenhum arquivo derivado — nenhum card ou questão cita a faixa de velocidade.

### 🟠 7. "Anomalia Bouguer" definida sem distinguir simples de completa

**claim_id:** `GFI-M19-BOUGUER-COMPLETE-007`
**Tipo:** omissão que gera erro (nomenclatura)
**Onde:** aula 03 · Vocabulário e "Da leitura bruta à anomalia"
**Está escrito:** "Anomalia Bouguer | Anomalia obtida após todas as correções padrão (ar-livre, Bouguer, terreno)."
**Problema:** a definição dada é a da anomalia Bouguer **completa** (ou refinada), apresentada como se fosse a única. A terminologia padrão separa: a **anomalia Bouguer simples** (ou incompleta) para após a correção Bouguer com a aproximação de laje plana infinita, e a **completa** quando se acrescenta a correção de terreno. A diferença entre as duas é o próprio efeito de terreno, que é sempre negativo e nada desprezível em relevo acidentado. Um aluno com essa definição lerá errado qualquer mapa ou artigo rotulado "simple Bouguer anomaly".
**Correção aplicada:** nomeadas as duas variantes no vocabulário e no corpo, indicando em que etapa da redução cada uma se fecha e quando a diferença importa.
**Fonte:** Hinze et al., *New standards for reducing gravity data: The North American gravity database*, Geophysics 70(4), 2005; Holom & Oldow, *Gravity reduction spreadsheet…*, Geosphere 3(2), 2007 · **Nível:** normativa (padrão de redução gravimétrica)
**Confiança:** confirmado
**Também aparece em:** nenhum arquivo derivado — `fb024`, `fb025` e `fc015` descrevem as **correções** (corretamente), não a anomalia final; a Q6 do questionário também pergunta pela correção. Nada a propagar.

### 🟠 8. Magnitude definida como medida da energia liberada

**claim_id:** `GFI-M19-MAG-ENERGY-008`
**Tipo:** imprecisão conceitual
**Onde:** aula 01 · Vocabulário e Recap
**Está escrito:** "Magnitude | Medida instrumental única da energia liberada num terremoto (hoje, tipicamente magnitude de momento, Mw)."
**Problema:** o USGS separa explicitamente as duas grandezas: a magnitude de momento deriva do **momento sísmico** (rigidez × área da falha × deslocamento) e mede o *tamanho* do terremoto, enquanto a energia radiada tem sua própria escala, a magnitude de energia (Me) — "the Energy Magnitude and Moment Magnitude measure two different properties of the earthquake, their values are not the same". Vale notar que o corpo da aula já definia Mw corretamente ("calculada a partir da área da falha rompida, do deslocamento médio e da rigidez"), de modo que a definição do vocabulário contradizia o próprio texto.
**Correção aplicada:** vocabulário e recap passam a definir magnitude como medida única do tamanho do terremoto na fonte, calculada a partir do momento sísmico, com a ressalva de que se relaciona à energia sem ser a mesma grandeza que Me.
**Fonte:** USGS, [Earthquake Magnitude, Energy Release, and Shaking Intensity](https://www.usgs.gov/programs/earthquake-hazards/earthquake-magnitude-energy-release-and-shaking-intensity), consultado em 2026-08-18 · **Nível:** normativa
**Confiança:** confirmado
**Também aparece em:** flashcard `fb008` (corrigido). **Não afeta** a Q3 do questionário nem `fb009`/`fc006`: a regra de ~32× de energia por grau inteiro é ensinada pelo próprio USGS e foi verificada como correta.

### 🟠 9. Q17 e Q18 mapeadas nos objetivos de aprendizagem errados

**claim_id:** `GFI-M19-QUIZ-OBJMAP-009`
**Tipo:** inconsistência interna
**Onde:** questionário final · Matriz de cobertura e tabela de Autodiagnóstico
**Está escrito:** matriz atribuindo `oa03` a "6, 7, 8, 15, 16, 18" e `oa04` a "9, 10, 17".
**Problema:** as duas dissertativas estão trocadas de objetivo. A **Q18** é inteiramente sobre intervalos P-S, trilateração de epicentro e a suposição de velocidade constante — conteúdo da aula 01 (`oa01`), não de métodos potenciais. A **Q17** é sobre interpretação de uma anomalia **aeromagnética** de 150 nT — conteúdo da aula 04 (`oa03`), não de métodos elétricos. O efeito prático é no autodiagnóstico: quem errava a Q18 era mandado revisar gravimetria e magnetometria, e quem errava a Q17 era mandado à aula 05. O próprio questionário se contradizia, porque a caixa de dica ao fim ("Se você errou 15, 16 ou 17 → volte às aulas 03 e 04") já tratava a Q17 como conteúdo de magnetometria.
**Correção aplicada:** Q18 movida para `oa01`/aula 01 e Q17 para `oa03`/aulas 03–04, na matriz e no autodiagnóstico.
**Fonte:** consistência interna do próprio material (enunciados das Q17 e Q18 contra os objetivos declarados no hub do módulo) · **Nível:** interna
**Confiança:** confirmado
**Também aparece em:** só no questionário.

### 🟠 10. Pontuação por objetivo não fecha, e a nota de normalização é falsa

**claim_id:** `GFI-M19-QUIZ-POINTS-010`
**Tipo:** inconsistência interna (numérica)
**Onde:** questionário final · Matriz de cobertura
**Está escrito:** coluna de pontos com 8 / 6 / 12 / 8 / 12 e a nota "Total: 46 pontos possíveis distribuídos pelas 19 questões antes de arredondamento de escala — a tabela 'Pontuação total' acima usa o valor final normalizado a 40."
**Problema:** não existe normalização alguma. A soma real das questões é exatamente 40: Parte I com 12 questões de 1 ponto, Parte II com 4 de 2 pontos (8), Parte III com 6 + 6 + 8 (20). Os 46 da tabela vinham da coluna de pontos por objetivo, que estava simplesmente errada, e a frase sobre "arredondamento de escala" foi construída para justificar a divergência em vez de resolvê-la. Distribuição real, já com o mapeamento corrigido do achado 9: `oa01` 11, `oa02` 4, `oa03` 13, `oa04` 2, `oa05` 10 — soma 40.
**Correção aplicada:** coluna de pontos substituída pelos valores reais, nota de normalização removida e substituída pela decomposição verdadeira (12 + 8 + 20).
**Fonte:** aritmética do próprio questionário · **Nível:** interna
**Confiança:** confirmado
**Também aparece em:** só no questionário.
**Consequência registrada:** com as contas certas, `oa04` (aula 05 inteira — resistividade, ER, IP, EM e geotermia) fica com **2 pontos em duas múltiplas escolhas**, desproporcional ao tamanho da aula. Isso é desenho de avaliação, não erro factual: foi registrado como ressalva no próprio questionário e encaminhado à revisão didática, sem inventar questões novas nesta auditoria.

### 🟠 11. Tabela de distribuição dos flashcards não bate com os CSVs

**claim_id:** `GFI-M19-CARDS-DIST-011`
**Tipo:** inconsistência interna (numérica)
**Onde:** `19-geofisica-metodos-flashcards.md` · tabela "Distribuição" e parágrafo de cobertura
**Está escrito:** 6 cards Cloze para cada uma das seis aulas, e "`oa03` recebendo o dobro de cards (20 Basic + 12 Cloze)".
**Problema:** a contagem real nos CSVs é outra. Os 60 cards Basic estão de fato distribuídos 10 por aula, mas os Cloze não: a03 tem 5 (`fc013`–`fc017`) e a06 tem 7 (`fc030`–`fc036`); as demais têm 6. O total de 36 está certo, mas a tabela descreve uma distribuição que o baralho não tem, e `oa03` soma 11 Cloze, não 12. Uma tabela de conferência que não confere é pior que não ter tabela.
**Correção aplicada:** tabela ajustada para a contagem real (a03 = 5, a06 = 7) e o parágrafo de cobertura corrigido para 20 Basic + 11 Cloze em `oa03`, explicitando que a distribuição Cloze não é uniforme.
**Fonte:** contagem direta em `19-geofisica-metodos-flashcards-cloze.csv` · **Nível:** interna
**Confiança:** confirmado
**Também aparece em:** só no índice do baralho; os CSVs em si estão íntegros.

### 🔵 12. Duas fontes citadas não sustentam o material

**claim_id:** `GFI-M19-CITATION-INTEGRITY-012`
**Tipo:** evidência insuficiente (integridade de citação)
**Onde:** aula 02 · Fontes; aula 05 · Fontes
**Está escrito:** "USGS, [Seismic Reflection and Refraction](https://www.usgs.gov/special-topics/water-science-school)" e "USGS, [Geothermal Gradient](https://www.usgs.gov/faqs/what-geothermal-gradient)".
**Problema:** a primeira URL foi verificada e é a página do **USGS Water Science School** — um portal educativo sobre água (ciclo hidrológico, qualidade da água, água subterrânea), sem qualquer conteúdo sobre sísmica de reflexão ou refração. A segunda retorna **HTTP 404**. Nos dois casos, o leitor que for conferir a afirmação não encontra o que a aula diz que está lá.
**Situação das alegações:** as afirmações em si **não** são erro — os mecanismos de reflexão/refração foram confirmados pelas páginas do SEG Wiki já citadas nas mesmas aulas, e o gradiente de 25–30 °C/km foi confirmado independentemente. O defeito é de verificabilidade, não de fato.
**Correção aplicada (com ressalva):** removida a atribuição falsa ao USGS na aula 02, mantendo a referência a Kearey, Brooks & Hill que já acompanhava a linha; e a URL morta da aula 05 substituída por uma publicação USGS viva e verificada sobre o mesmo dado. Nenhuma alegação nova foi inventada — apenas se retirou uma atribuição demonstravelmente falsa e se apontou para fonte conferida.
**Fonte substituta verificada:** USGS, [Geothermal gradients in the conterminous United States](https://www.usgs.gov/publications/geothermal-gradients-conterminous-united-states) (leste dos EUA ≈ 25 °C/km, oeste ≈ 34 °C/km; ≈ 25 °C/km longe de limites de placa) · **Nível:** normativa
**Confiança:** não verificado (quanto à citação original); confirmado (quanto ao valor do gradiente)
**Também aparece em:** bloco `alegacoes_auditaveis` da aula 05, cuja linha `source` foi atualizada.

### ⚪ 13. Saturação da escala Richter dada como "~7" sem indicar a divergência

**claim_id:** `GFI-M19-RICHTER-SAT-013`
**Tipo:** controvérsia / certeza indevida
**Onde:** aula 01 · "Localizando um epicentro: a corrida P-S"
**Está escrito:** "substituiu a escala Richter original para eventos grandes, porque a Richter satura (perde sensibilidade) acima de magnitude ~7."
**Problema:** o fato de fundo é indiscutível — ML satura e por isso Mw a substituiu para eventos grandes. O número específico é que não é consenso. A página do USGS sobre escalas de magnitude, consultada, **não fixa um limiar**, dizendo apenas que o método "was strictly valid only for certain frequency and distance ranges"; fontes secundárias dão ~6,5; boa parte da literatura didática dá 6,5–7; e o limiar depende de qual escala se discute (ML satura antes de Ms, que satura em torno de 8) e de que definição de saturação se adota. Apresentar "~7" como número fechado esconde essa dispersão.
**Correção aplicada (2026-08-18, por decisão do usuário):** o número único foi substituído por uma faixa com a divergência explícita — "satura em torno de magnitude 6,5–7, conforme a escala e o critério adotados". O texto segue afirmando o fato indiscutível (a saturação em si e a substituição por Mw), sem escolher qual limiar exato prevalece.
**Fonte:** USGS, [Moment magnitude, Richter scale — what are the different magnitude scales…](https://usgs.gov/faqs/moment-magnitude-richter-scale-what-are-different-magnitude-scales-and-why-are-there-so-many), consultado em 2026-08-18 · **Nível:** normativa (silente quanto ao limiar)
**Confiança:** em disputa
**Também aparece em:** nenhum arquivo derivado — nenhum card nem questão cita o limiar de saturação.

## Verificado e correto

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `GFI-M19-OK-PS-PROP-014` | Onda P é longitudinal e atravessa sólido, líquido e gás; onda S é transversal e só se propaga em sólidos. | USGS, *The Science of Earthquakes* (2026) | confirmado |
| `GFI-M19-OK-VSVP-015` | Vs é cerca de 60% de Vp no mesmo meio. | Vp/Vs crustal 1,74–1,83 (Christensen & Mooney 1995) → Vs ≈ 0,55–0,58 Vp | confirmado |
| `GFI-M19-OK-SHADOW-ANG-016` | Zona de sombra: P ausente entre ~103° e ~142°; S ausente além de ~103°. | IRIS/EarthScope; USGS | confirmado |
| `GFI-M19-OK-SHADOW-MECH-017` | A ausência total de S além de ~103° é a evidência de núcleo externo líquido; a de P vem de refração no limite núcleo-manto. | IRIS/EarthScope | confirmado |
| `GFI-M19-OK-ENERGY-32-018` | Cada grau inteiro de magnitude corresponde a cerca de 32× mais energia liberada (e 2 graus, a ~1.000×). | USGS, *Earthquake Magnitude, Energy Release, and Shaking Intensity* | confirmado |
| `GFI-M19-OK-INTENSITY-019` | Intensidade (Mercalli) varia ponto a ponto para um mesmo evento; magnitude é única. | USGS | confirmado |
| `GFI-M19-OK-TRILAT-020` | O intervalo P-S dá distância, não direção; três estações localizam o epicentro por trilateração. | IRIS, *How Do Seismologists Locate an Earthquake?* | confirmado |
| `GFI-M19-OK-IMPEDANCE-021` | Impedância acústica é densidade × velocidade P, e o contraste de impedância é o que gera reflexão. | SEG Wiki, *Seismic reflection method*; Kearey, Brooks & Hill | confirmado |
| `GFI-M19-OK-HEADWAVE-022` | No ângulo crítico a onda viaja ao longo da interface na velocidade da camada inferior e, além do ponto de cruzamento, chega antes da direta. | SEG Wiki, *Seismic refraction method* | confirmado |
| `GFI-M19-OK-TIMEDEPTH-023` | A sísmica bruta é medida em tempo; converter para profundidade exige modelo de velocidade. | SEG Wiki; Schlumberger Oilfield Glossary | confirmado |
| `GFI-M19-OK-BOUGUER-DENS-024` | A correção Bouguer assume tipicamente ~2,67 g/cm³ para crosta continental. | Hinze, *Bouguer reduction density, why 2.67?*, Geophysics 68(5), 2003 | confirmado |
| `GFI-M19-OK-NONUNIQUE-025` | Métodos potenciais sofrem de não unicidade: a mesma anomalia admite infinitas soluções de forma, profundidade e contraste. | SEG Wiki, *Gravity method* | confirmado |
| `GFI-M19-OK-CURIE-580-026` | A temperatura de Curie da magnetita é ~580 °C e define a profundidade de Curie na crosta. | Bouligand et al., JGR 114, 2009; Haggerty, GRL 5(2), 1978 | confirmado |
| `GFI-M19-OK-NT-BACKGROUND-027` | Anomalias magnéticas de interesse são de dezenas a centenas de nT sobre um campo de fundo de dezenas de milhares de nT. | SEG Wiki, *Magnetic method*; IGRF | confirmado |
| `GFI-M19-OK-PORE-FLUID-028` | A resistividade de rocha porosa é controlada pela água dos poros e sua salinidade (condução iônica); minério maciço e grafita conduzem por via eletrônica. | US EPA, *Electrical Methods*; Britannica, *Rock — Electrical properties* | confirmado |
| `GFI-M19-OK-IP-DISSEM-029` | IP é especialmente sensível a minerais metálicos **disseminados**, mesmo com pouco contraste de resistividade. | SEG Wiki, *Induced polarization* | confirmado |
| `GFI-M19-OK-GEOTHERM-030` | Gradiente geotérmico continental médio da ordem de 25–30 °C/km, variando muito com o contexto tectônico. | USGS, *Geothermal gradients in the conterminous United States* | confirmado |
| `GFI-M19-OK-LOGS-031` | GR mede radioatividade natural (K, Th, U) e separa folhelho de rocha limpa; sônico + densidade dão a impedância que gera o sismograma sintético da amarração poço-sísmica. | SEG Wiki, *Well logging*; Schlumberger Oilfield Glossary | confirmado |

## Observações não factuais

- A frase entre parênteses na aula 06 sobre resistividade de poço — "(baixa condutividade/água salina desloca para fora, óleo e gás são muito mais resistivos que água salgada)" — está truncada e de leitura difícil. O conteúdo é correto; a redação é assunto da revisão didática.
- A sub-cobertura de `oa04` no questionário (2 pontos para uma aula inteira), exposta pelo achado 10, é desenho de avaliação e foi encaminhada à revisão didática, não corrigida aqui.

## Fontes normativas e primárias consultadas

- USGS, *Earthquake Magnitude, Energy Release, and Shaking Intensity*, consultado em 2026-08-18 — https://www.usgs.gov/programs/earthquake-hazards/earthquake-magnitude-energy-release-and-shaking-intensity
- USGS, *Moment magnitude, Richter scale — what are the different magnitude scales*, consultado em 2026-08-18
- USGS, *Geothermal gradients in the conterminous United States*, consultado em 2026-08-18
- IRIS/EarthScope Consortium, animações e material didático sobre zonas de sombra e localização de epicentro, consultado em 2026-08-18
- SEG Wiki (Society of Exploration Geophysicists), verbetes *Seismic reflection method*, *Seismic refraction method*, *Gravity method*, *Magnetic method*, *Induced polarization*, *Well logging*
- Christensen & Mooney, *Seismic Velocity Structure and Composition of the Continental Crust*, JGR 100(B7), 1995
- Prodehl & Mooney, *100 years of seismic research on the Moho*, Tectonophysics 609, 2013
- Dziewonski & Gilbert, *Solidity of the inner core of the Earth inferred from normal mode observations*, Nature 234, 1971
- Haggerty, *Mineralogical constraints on Curie isotherms in deep crustal magnetic anomalies*, GRL 5(2), 1978; McEnroe et al., G³ 19, 2018
- Hinze, *Bouguer reduction density, why 2.67?*, Geophysics 68(5), 2003; Hinze et al., Geophysics 70(4), 2005
- US EPA, *Electrical Methods*; Britannica, *Rock — Electrical properties*

---

## Correções aplicadas

**Aplicadas em:** 2026-08-18

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `GFI-M19-RESIST-INSULATOR-001` | 🔴 | Corrigido | aula 05, questionário final (gabarito Q9) |
| `GFI-M19-MAG-ILMENITE-002` | 🟠 | Corrigido | aula 04 |
| `GFI-M19-MOHO-DISCOVERY-003` | 🟠 | Corrigido | aula 02, flashcards-basic.csv (`fb020`), flashcards-cloze.csv (`fc012`) |
| `GFI-M19-INNERCORE-SOLID-004` | 🟠 | Corrigido | aula 01 |
| `GFI-M19-SHADOW-HISTORY-005` | 🟠 | Corrigido | aula 01 |
| `GFI-M19-PVEL-CRUST-006` | 🟠 | Corrigido | aula 01 |
| `GFI-M19-BOUGUER-COMPLETE-007` | 🟠 | Corrigido | aula 03 |
| `GFI-M19-MAG-ENERGY-008` | 🟠 | Corrigido | aula 01, flashcards-basic.csv (`fb008`) |
| `GFI-M19-QUIZ-OBJMAP-009` | 🟠 | Corrigido | questionário final (matriz e autodiagnóstico) |
| `GFI-M19-QUIZ-POINTS-010` | 🟠 | Corrigido | questionário final (matriz) |
| `GFI-M19-CARDS-DIST-011` | 🟠 | Corrigido | flashcards.md |
| `GFI-M19-CITATION-INTEGRITY-012` | 🔵 | Corrigido com ressalva — atribuição falsa removida/substituída, nenhuma alegação inventada | aula 02, aula 05 |
| `GFI-M19-RICHTER-SAT-013` | ⚪ | Corrigido com ressalva — faixa 6,5–7 com divergência explícita, nenhum lado escolhido | aula 01 |

**Pendências:**

1. **`GFI-M19-CITATION-INTEGRITY-012` (🔵) foi tratado com ressalva.** Se a preferência do usuário for não substituir fontes durante a auditoria, a alteração na aula 05 (troca da URL morta pela publicação USGS verificada) pode ser revertida sem afetar nenhuma alegação.
2. **`course-state.yaml`** foi atualizado numa consolidação posterior, junto com os módulos 17 e 19.
3. **Baralho possivelmente já importado no Anki.** Três cards mudaram (`fb008`, `fb020`, `fc012`). Reimportar os CSVs não sobrescreve com segurança cards já em revisão: se o baralho foi importado antes de 2026-08-18, esses três precisam ser corrigidos ou apagados à mão.

**Gate científico:** liberado. 0 achados 🔴 ou 🟠 em aberto — o único achado aberto é ⚪, que por definição não é erro. O módulo está factualmente limpo para seguir para a revisão didática.
