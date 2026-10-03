# Auditoria científica — Módulo 27: Introdução à petrocronologia

**Curso:** geologia-avancado
**Módulo:** 27 — `27-petrocronologia` (6 aulas)
**Modo:** `audit-and-fix` · **Profundidade:** `full`
**Passagens:** 1 (2026-09-22). Uma sessão anterior começou esta auditoria e foi cortada por limite de sessão **antes de gravar qualquer coisa em disco** (nenhum relatório, `course-state.yaml` byte-idêntico ao backup `course-state.yaml.bak-20260922-pre-m27-audit`, aulas idênticas às da redação). Nada foi recuperado dela; esta passagem começou do zero e numera os achados a partir de 1.
**Veredito:** **Aprovado após correções** — 2 vermelhos, 10 laranjas, 1 amarelo e 1 azul levantados; todos os vermelhos, laranjas e amarelos corrigidos; o azul foi resolvido por remoção do dado não verificável. Nada em aberto.

> [!warning] Numeração das aulas neste relatório
> Este relatório usa a numeração **da auditoria** (6 aulas). Depois dela, no mesmo dia, a revisão didática dividiu a Aula 04 em **Aula 04 (Parte 1)** e **Aula 05 (Parte 2 — geotermobarometria)** e renumerou as antigas Aulas 05 e 06 para **06 e 07**. Onde este relatório diz "Aula 05" (minerais acessórios), leia Aula 06; onde diz "Aula 06" (granada e integração), leia Aula 07; o achado 🔵 7 (Ferry & Spear) está hoje no arquivo da Aula 05. Os `claim_id` não mudaram — são âncoras estáveis. Ver [[27-petrocronologia-revisao-didatica|relatório da revisão didática]].

---

## Resumo por severidade

| Severidade | Levantados | Corrigidos | Em aberto |
|---|---|---|---|
| 🔴 Erro | 2 | 2 | **0** |
| 🟠 Impreciso | 10 | 10 | **0** |
| 🟡 Desatualizado / metadado | 1 | 1 | **0** |
| 🔵 Sem fonte | 1 | 1 (removido o dado não verificável) | **0** |
| ⚪ Controverso | 0 | — | 0 |
| **Total** | **14** | **14** | **0** |

Gate de qualidade: **liberado** para questionário e flashcards (0 vermelhos e 0 laranjas em aberto). O módulo **não** foi fechado nesta etapa.

---

## Nota de método

A redação declarou 41 alegações auditáveis e marcou com `INCERTEZA DECLARADA` sobretudo **paginação de referências**. O padrão observado nos módulos 25 e 26 se repetiu, e com mais força:

- **Das 16 paginações marcadas como incertas, 14 estavam certas** e 2 erradas — as duas de Pollington & Baxter, que não tinham só a paginação errada: ano, revista e volume estavam trocados entre as duas publicações (🟠 12). As 14 corretas: Hoskin & Schaltegger 2003 (27-62), Corfu et al. 2003 (469-500), Cherniak et al. 2004 (829-840), Copeland et al. 1988 (760-763), Cherniak 1993 (177-194), Ganguly & Tirone 1999 (131-140), Suzuki et al. 1994 (391-405), Ghent 1976 (710-714), Powell & Holland 1994 (120-133), Connolly 2005 (524-541), Hollister 1966 (1647-1651), England & Thompson 1984 (894-928), Foster et al. 2002 (183-207, seis autores), Watson et al. 2006 (413-433). Todas as marcas foram retiradas.
- **Os dois vermelhos estavam em trechos que a redação deu como verificados ou nem sinalizou.** O 🔴 8 (coeficientes de partição zircão/granada lidos ao contrário) está numa alegação marcada `VERIFICADO por busca` — a busca achou o número certo e a leitura inverteu o sentido. O 🔴 1 (protólito ígneo de um metapelito) é uma contradição de definição num exemplo que a redação classificou como "hipotético", categoria que não costuma ser conferida.
- **Três referências marcadas VERIFICADO estavam erradas**: o título de Rubatto (2002) (🟡 2) e as duas publicações de Pollington & Baxter, marcadas ao mesmo tempo VERIFICADO (conteúdo) e INCERTEZA (paginação), com anos, revistas, volumes e páginas trocados entre si (🟠 12). "VERIFICADO" no rodapé de uma aula não dispensa conferência.

Ferramentas: metadados bibliográficos conferidos na API do Crossref (título, revista, volume, páginas, ano, autores, DOI) para 33 referências; resumos e textos primários lidos quando acessíveis (Rubatto & Hermann 2007, texto integral; Mezger et al. 1992, resumo; SHRIMP-RG Stanford, página técnica); o restante por busca com fonte identificada.

---

## Achados

### 🔴 1. Exemplo da Aula 01: "protólito ígneo" de um metapelito

**claim_id:** `PETROCRON-M27-A01-EXEMPLO-NUCLEO-BORDA-004`
**Tipo:** inconsistência interna (erro de definição)
**Onde:** Aula 01 · Exemplo trabalhado (Situação e Leitura petrocronológica); ecoado no bloco de metadados
**Está escrito:** "Uma amostra de **metapelito** de alto grau contém zircões com núcleos [...] 550 Ma provavelmente data a **cristalização do protólito ígneo da rocha**"
**Problema:** metapelito é, por definição, rocha metamórfica de protólito **pelítico (sedimentar)**. Núcleos de zircão com zoneamento oscilatório num metapelito são grãos **detríticos**: datam a cristalização da rocha ígnea-fonte e dão uma idade máxima de deposição, não a "cristalização do protólito ígneo da rocha". A conclusão do exemplo ("protólito ígneo aos 550 Ma") é falsa para a rocha descrita. A lógica didática (núcleo magmático × borda metamórfica) está certa; só a litologia contradiz a conclusão.
**Correção aplicada:** a amostra passa a ser um **ortognaisse** de alto grau (gnaisse de protólito granítico), em que a leitura "núcleo = cristalização do protólito ígneo" é correta. Menor edição possível: a conclusão, o par de idades e a Aula 05 (que retoma este zircão) ficam intactos.
**Fonte:** definição de metapelito e interpretação de núcleos detríticos — Corfu et al. (2003), *Atlas of Zircon Textures*, RiMG 53, 469-500, doi:10.2113/0530469 · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 05, Exemplo trabalhado ("Retomando o zircão do exemplo da Aula 01") — não cita a litologia, continua coerente sem edição.

### 🟡 2. Título de Rubatto (2002) citado errado

**claim_id:** `PETROCRON-M27-A01-RUBATTO-TITULO-006` (novo)
**Tipo:** erro de metadado bibliográfico
**Onde:** Aula 01 · Fontes; Aula 05 · Fontes
**Está escrito:** "Zircon trace element geochemistry: **distribution coefficients** and the link between U-Pb ages and metamorphism" (marcado VERIFICADO)
**Problema:** o título publicado é "Zircon trace element geochemistry: **partitioning with garnet** and the link between U-Pb ages and metamorphism". A variante "distribution coefficients" circula em listas de referências (inclusive em Rubatto & Hermann 2007), o que explica o engano, mas não é o registro da editora. Revista, volume, páginas e ano estavam certos.
**Correção aplicada:** título corrigido nas duas aulas, com a variante mencionada entre parênteses para quem a encontrar em outra bibliografia.
**Fonte:** Crossref, doi:10.1016/S0009-2541(01)00355-2, consultado 2026-09-22 · **Nível:** base de indexação
**Confiança:** confirmado

### 🟠 3. "Lutécio em concentrações mais altas que em qualquer outra fase da rocha"

**claim_id:** `PETROCRON-M27-A02-LU-CONCENTRACAO-GRANADA-009` (novo)
**Tipo:** imprecisão (generalização falsa como escrita)
**Onde:** Aula 02 · "Sm-Nd e Lu-Hf: a granada como cronômetro", bullet Lu-Hf
**Está escrito:** "entrando em concentrações desproporcionalmente mais altas que em **qualquer outra fase** da rocha"
**Problema:** vale para os minerais **formadores de rocha**, não para "qualquer fase". O zircão tem concentrações de HREE (Lu incluído) **maiores** que as da granada — Rubatto & Hermann (2007): "Zircon contains significantly more heavy-REE than garnet" a 800-850 °C. A granada domina o **orçamento** de Lu da rocha pela abundância modal, não por ter a maior concentração. É a mesma confusão que gerou o 🔴 8, e deixá-la aqui faria a Aula 02 preparar o erro da Aula 05. A ressalva também é o motivo físico do subtítulo de Scherer et al. (2000) ("effects of trace mineral inclusions"): inclusões de zircão estragam isócronas Lu-Hf de granada porque são ricas em Hf.
**Correção aplicada:** "que em qualquer outro mineral formador de rocha" + uma frase dizendo que só acessórios como zircão e xenotima têm concentrações ainda maiores, em quantidade modal ínfima, e que por isso inclusões de zircão contaminam a isócrona.
**Fonte:** Rubatto & Hermann (2007), *Chemical Geology* 241, 38-61, doi:10.1016/j.chemgeo.2007.01.027 (resumo e texto integral lidos) · **Nível:** revisada por pares
**Confiança:** confirmado

### 🟠 4. Obras citadas no corpo e ausentes das Fontes; uma nota de verificação apontando para a aula errada

**claim_id:** `PETROCRON-M27-A02-FONTES-AUSENTES-010` (novo)
**Tipo:** imprecisão bibliográfica (omissão)
**Onde:** Aula 02 · corpo (monazita, titanita, Sm-Nd) e Fontes; Aula 05 · corpo (zircão) e Fontes
**Está escrito:** Aula 02 cita no corpo Parrish (1990), Kohn & Corrie (2011) e "Mezger et al., 1992 estabeleceram valores de referência", e nenhum dos três está nas Fontes. Aula 05 cita "Rubatto & Hermann, trabalhos experimentais posteriores" sem referência, e a entrada de Zack et al. (2004) nas Fontes diz "já confirmado na Aula 02", mas a Aula 02 não cita Zack et al.
**Problema:** citação no corpo sem entrada na bibliografia não é rastreável (mesmo padrão do achado 🟠 10 do módulo 25). No caso de Mezger et al. (1992), a atribuição ficava vaga ("valores de referência") numa frase que apresenta uma faixa de 600-750 °C; o que o artigo de fato estima é **ca. 600 ± 30 °C** para granadas de 0,1-5 cm em terrenos de resfriamento lento — o limite inferior da faixa, não a faixa inteira.
**Correção aplicada:** Parrish (1990), Mezger, Essene & Halliday (1992) e Kohn & Corrie (2011) acrescentados às Fontes da Aula 02; frase de Sm-Nd reescrita atribuindo a Mezger et al. o valor que eles publicaram (~600 ± 30 °C) e a Ganguly & Tirone a dependência de tamanho de grão e taxa de resfriamento. Rubatto & Hermann (2007) acrescentado às Fontes da Aula 05 e nomeado no corpo; nota "já confirmado na Aula 02" substituída pela conferência real.
**Fonte:** Crossref — Parrish 1990, *Can. J. Earth Sci.* 27, 1431-1450, doi:10.1139/e90-152; Mezger et al. 1992, *EPSL* 113, 397-409, doi:10.1016/0012-821X(92)90141-H (resumo lido: "ca. 600 ± 30 °C"); Kohn & Corrie 2011, *EPSL* 311, 136-143, doi:10.1016/j.epsl.2011.09.008; Rubatto & Hermann 2007, doi:10.1016/j.chemgeo.2007.01.027 · **Nível:** revisada por pares / base de indexação
**Confiança:** confirmado

### 🟠 5. Exemplo da Aula 02: muscovita num granulito lida como idade de resfriamento

**claim_id:** `PETROCRON-M27-A02-EXEMPLO-CINCO-IDADES-008`
**Tipo:** confusão de escopo (paragênese implausível num exemplo)
**Onde:** Aula 02 · Exemplo trabalhado (Situação, Leitura, Conclusão)
**Está escrito:** "Um **granulito** de alto grau foi datado por [...] **muscovita** Rb-Sr, 560 ± 10 Ma [...] com fechamento em torno de 450-500 °C"
**Problema:** a muscovita não é estável na fácies granulito: reage com quartzo (Ms + Qz → Kfs + Sil + H₂O ou fundido) antes dela, e a associação sillimanita + K-feldspato marca justamente essa passagem. Muscovita num granulito é **retrógrada**, cresceu abaixo do pico — e uma mica que cresce abaixo da sua temperatura de fechamento data o **crescimento**, não a passagem por 450-500 °C no resfriamento. A leitura que o exemplo ensina ("fecha a sequência de resfriamento") é falsa para essa rocha.
**Correção aplicada:** a mica do exemplo passa a ser **biotita** Rb-Sr (a biotita persiste em muitos granulitos), com a temperatura de fechamento que a própria aula dá para ela (~300-350 °C). Idade (560 Ma), intervalo (60 Ma) e a lógica de encadeamento ficam intactos; ajustadas as três menções no exemplo e o metadado.
**Fonte:** Dyck, Waters, St-Onge & Searle (2020), "Muscovite dehydration melting: reaction mechanisms, microstructures, and implications for anatexis", *J. Metamorphic Geol.* 38, 29-52, doi:10.1111/jmg.12511 · **Nível:** revisada por pares
**Confiança:** confirmado

### 🟠 6. SIMS: resolução em profundidade apresentada como resolução lateral

**claim_id:** `PETROCRON-M27-A03-SIMS-VS-LAICPMS-002`
**Tipo:** imprecisão que induz conclusão errada
**Onde:** Aula 03 · seção SIMS; Exemplo trabalhado, Problema 2; Recap
**Está escrito:** "A vantagem central sobre o LA-ICP-MS é a resolução espacial: um pit típico de SHRIMP tem profundidade da ordem de 1-3 μm [...] permitindo atingir domínios estreitos" e, no Problema 2, SIMS para atingir "borda metamórfica fina de poucos micrômetros"
**Problema:** o pit do SHRIMP tem **~2 μm de profundidade**, mas **~15-25 μm de diâmetro** — lateralmente, a mesma ordem de grandeza do LA-ICP-MS. Numa seção polida, uma borda de poucos micrômetros de largura **não** cabe num spot de SIMS. A vantagem real é o volume amostrado muito menor (e, portanto, a resolução em profundidade); bordas de poucos micrômetros são datadas por **perfil em profundidade**, fazendo o feixe atravessar a borda a partir da face externa de um grão não polido. Como escrito, o aluno sai achando que SIMS resolve lateralmente o que o LA-ICP-MS não resolve.
**Correção aplicada:** seção SIMS explicita diâmetro × profundidade; Problema 2 passa a descrever o perfil em profundidade no grão não seccionado; recap ajustado.
**Fonte:** Stanford-USGS SHRIMP-RG Lab, "Zircon U-Th-Pb and U-Th ages and trace element analyses" (pits "~15 to 25 microns" de diâmetro e "~2 microns" de profundidade; perfil em profundidade de bordas em faces não polidas), consultado 2026-09-22, https://shrimprg.stanford.edu/zircon-u-th-pb-and-u-th-ages-and-trace-element-analyses · **Nível:** base de referência (laboratório operador)
**Confiança:** confirmado

### 🔵 7. Limite inferior de temperatura dos experimentos de Ferry & Spear (1978)

**claim_id:** `PETROCRON-M27-A04-GRT-BT-THERMOMETER-005`
**Tipo:** evidência insuficiente
**Onde:** Aula 04 · Geotermobarometria convencional; Fontes; metadados
**Está escrito:** "a pressão constante (0,207 GPa) e temperaturas entre **500** e 800 °C"
**Problema:** a pressão (2,07 kbar = 0,207 GPa) e o limite superior (800 °C) são consistentes em todas as fontes. O limite **inferior** não: fontes secundárias dão 500 °C (Wikipedia), 550 °C (citação do resumo) e 600 °C (Wu & Cheng 2006, *Lithos* 89, 1-23, para as corridas bem fechadas). O resumo original é fechado pela editora e não pôde ser lido. Não é central para a aula.
**Correção aplicada:** removido o limite inferior não verificável: "a pressão constante de 0,207 GPa (2,07 kbar) e temperaturas de até 800 °C". Nenhum valor inventado.
**Fonte:** Crossref doi:10.1007/BF00372150 (bibliografia confirmada); divergência entre as secundárias registrada no manifesto · **Nível:** base de indexação
**Confiança:** não verificado (limite inferior) · confirmado (pressão, limite superior, bibliografia)

### 🔴 8. Coeficientes de partição zircão/granada lidos ao contrário

**claim_id:** `PETROCRON-M27-A05-PARTICAO-VALORES-NUMERICOS-003` (também afeta `-COMPETICAO-Y-HREE-001` e `-ZIRCAO-HREE-PADRAO-002`)
**Tipo:** erro factual
**Onde:** Aula 05 · "O fio condutor", "Zircão: Th/U, Y/HREE e a assinatura da granada", Recap, Fontes, metadados
**Está escrito:** "coeficientes de partição de HREE tipicamente maiores que 1 **em favor da granada** (valores da ordem de ~0,7-2,3 para Gd, crescendo para ~6-24 para Lu)"; no recap, "coeficientes de partição de HREE muito maiores que 1 **a seu favor**"; e, na abertura, zircão e monazita aceitam Y e HREE "em **concentrações menores**"
**Problema:** os valores 0,7-2,3 (Gd) a 6,3-24 (Lu) são **D(zircão/granada)**: acima de 1 significa que o **zircão** é mais rico em HREE que a granada. Rubatto & Hermann (2007), no próprio parágrafo de onde saem os números: "partitioning increasingly in favour of zircon across the HREE". O texto inverte o sentido e usa o número invertido como "confirmação quantitativa" de por que a granada vence a competição. Além disso, o D cai para ~1 em temperaturas ultra-altas (1,3-0,6 em granulitos UHT; D_Lu de 12 a 800 °C para 1,4 a 1000 °C, experimental), coisa que o texto não diz. O **mecanismo** que a aula ensina (a granada empobrece o reservatório e o zircão cogenético sai com HREE achatado) está certo, mas a causa é outra: a granada domina o orçamento de HREE da rocha pela **abundância modal** (porcentagens de volume contra centésimos de porcento de zircão), e não por ter coeficiente maior. Esse erro iria direto para um card de flashcard ("D > 1 a favor da granada").
**Correção aplicada:** reescritas a frase dos coeficientes (sentido correto, dependência da temperatura, causa modal), a frase de abertura ("concentrações menores" → concentrações altas em quantidade modal ínfima), o bullet do recap e os três claims de metadados. A entrada de Fontes que dizia "a favor da granada" foi corrigida e atribuída ao artigo certo. Refinamento aplicado no fim da mesma passagem: como a faixa do Gd (0,7-2,3) inclui valores abaixo de 1, o texto diz que os coeficientes "favorecem o zircão: ficam perto de 1 no Gd e crescem para bem acima de 1 no Lu", em vez de "maiores que 1" para toda a série.
**Fonte:** Rubatto & Hermann (2007), *Chemical Geology* 241, 38-61, doi:10.1016/j.chemgeo.2007.01.027 — resumo ("Zircon contains significantly more heavy-REE than garnet at temperatures of 800–850 °C. Zircon/garnet partition coefficients of heavy-REE decrease with increasing temperature...") e seção 1 (síntese 0,7-2,3 / 6,3-24 e UHT 1,3-0,6); Taylor et al. (2015), *J. Metamorphic Geol.* 33, 231-248, doi:10.1111/jmg.12118 · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 02 (🟠 3, mesma raiz); hub do módulo, "Pontos de dificuldade" (formulação neutra, não precisou de edição).

### 🟠 9. "Granada consumida por reação retrógrada, por exemplo durante fusão parcial"

**claim_id:** `PETROCRON-M27-A05-QUEBRA-GRANADA-FUSAO-010` (novo)
**Tipo:** imprecisão (mecanismo)
**Onde:** Aula 05 · "O fio condutor"
**Está escrito:** "quando a granada é consumida por uma reação retrógrada (por exemplo, **durante fusão parcial** ou descompressão)"
**Problema:** a fusão parcial de metapelitos por desidratação da biotita é **prógrada** e **produz** granada peritética (Bt + Sil + Pl + Qz → Grt + Kfs + fundido). A granada é consumida na **retrogressão**: quando o fundido cristaliza e reage de volta com o resíduo, ou na descompressão (por exemplo, formando cordierita). Como escrito, o exemplo inverte o papel da fusão, justo o contexto (migmatitos) em que a petrocronologia de zircão e monazita mais se aplica.
**Correção aplicada:** "(por exemplo, na descompressão, ou quando o fundido de uma rocha parcialmente fundida cristaliza e reage de volta com a granada — a fusão parcial em si, na subida de temperatura, tende a **produzir** granada)".
**Fonte:** Le Breton & Thompson (1988), "Fluid-absent (dehydration) melting of biotite in metapelites in the early stages of crustal anatexis", *Contrib. Mineral. Petrol.* 99, 226-237, doi:10.1007/BF00371463; Pyle & Spear (2003), *American Mineralogist* 88, 338-351, doi:10.2138/am-2003-2-311 (monazita 4 formada "during melt crystallization and consumption of garnet and cordierite") · **Nível:** revisada por pares
**Confiança:** confirmado

### 🟠 10. Monazita "antes" do crescimento da granada com Y baixo

**claim_id:** `PETROCRON-M27-A05-MONAZITA-Y-PRE-GRANADA-011` (novo)
**Tipo:** imprecisão
**Onde:** Aula 05 · "Monazita: zoneamento de ítrio"; Recap
**Está escrito:** "domínios de monazita que crescem **antes** ou durante o crescimento da granada tendem a Y relativamente baixo"; recap: "baixo durante/antes do crescimento da granada"
**Problema:** a monazita **pré-granada** tende a Y **alto**: antes de a granada nuclear, o Y da rocha está disponível, e a monazita frequentemente coexiste com xenotima (que tampona o Y). O Y cai na monazita que cresce **durante** o crescimento da granada, e volta a subir na que cresce **depois** da quebra da granada. A sequência correta é alto → baixo → alto, não baixo → baixo → alto; o texto como estava faria o aluno classificar errado uma monazita pré-granada.
**Correção aplicada:** "domínios que crescem **durante** o crescimento da granada tendem a Y relativamente baixo; domínios **anteriores** à granada (em geral em equilíbrio com xenotima) e **posteriores** à sua quebra tendem a Y alto"; recap ajustado.
**Fonte:** Pyle, Spear, Rudnick & McDonough (2001), *J. Petrology* 42, 2083-2107, doi:10.1093/petrology/42.11.2083, via Schulz (2021), "Monazite microstructures and their interpretation in petrochronology", *Frontiers in Earth Science* 9:668566, doi:10.3389/feart.2021.668566 ("a pre-garnet grown matrix monazite should have elevated Y contents") · **Nível:** revisada por pares
**Confiança:** confirmado

### 🟠 11. Isócrona de granada inteira como "média ponderada por massa"

**claim_id:** `PETROCRON-M27-A06-GRANADA-MEDIA-PONDERADA-001`
**Tipo:** imprecisão (contradiz a seção seguinte da mesma aula)
**Onde:** Aula 06 · "O problema da idade 'borrada'"; metadados
**Está escrito:** "mede uma média ponderada **por massa** de todo o intervalo de crescimento"
**Problema:** a idade de granada inteira é ponderada pela **quantidade do elemento-pai** em cada zona (Sm para Sm-Nd, Lu para Lu-Hf), não só pela massa. É exatamente por isso que a mesma aula, duas seções depois, explica que Lu-Hf se enviesa para o núcleo — o que seria impossível se a ponderação fosse só por massa.
**Correção aplicada:** "uma média ponderada pela massa de cada zona **e** pelo seu teor do elemento-pai (Sm no Sm-Nd, Lu no Lu-Hf)".
**Fonte:** Baxter & Scherer (2013), *Elements* 9, 433-438, doi:10.2113/gselements.9.6.433; Smit, Scherer & Mezger (2013), *EPSL* 381, 222-233, doi:10.1016/j.epsl.2013.08.046 ("average ages of all growth zones weighted by their respective Lu and Sm contents") · **Nível:** revisada por pares
**Confiança:** confirmado

### 🟠 12. Pollington & Baxter: anos, revistas, volumes e páginas trocados

**claim_id:** `PETROCRON-M27-A06-POLLINGTON-BIBLIO-006` (novo)
**Tipo:** erro de metadado bibliográfico (referência irrecuperável como citada)
**Onde:** Aula 06 · Fontes (as duas entradas); corpo ("Pollington & Baxter (2010, 2011)")
**Está escrito:** "Pollington & Baxter (**2010**), 'High precision microsampling...', ***Chemical Geology*, 281**, 270-282" e "Pollington & Baxter (**2011**), 'High resolution Sm-Nd garnet geochronology reveals...', ***EPSL*, 305, 579-590**" (ambas marcadas VERIFICADO)
**Problema:** o artigo de **resultados** (12 zonas, 7,55 ± 0,52 Ma, dois pulsos) é **2010**, *EPSL* **293, 63-71**; o artigo de **método** (microamostragem) é **2011**, *Chemical Geology* **281, 270-282**. Os anos estavam trocados, e o volume/páginas do EPSL (305, 579-590) não correspondem ao artigo. Na aula, o resultado de 7,55 Ma ficava atribuído implicitamente a 2011.
**Correção aplicada:** as duas entradas reescritas com os metadados do Crossref, com DOI; o corpo passa a dizer "Pollington & Baxter (2011, método; 2010, aplicação)" e atribui o resultado à publicação de 2010. Os fatos (12 zonas, 7,55 ± 0,52 Ma a 2 DP, dois pulsos, Tauern Window) conferem com o resumo e ficaram como estavam.
**Fonte:** Crossref — doi:10.1016/j.epsl.2010.02.019 e doi:10.1016/j.chemgeo.2010.12.014, consultados 2026-09-22 · **Nível:** base de indexação
**Confiança:** confirmado

### 🟠 13. Lu-Hf in situ com "resolução espacial comparável à do LA-ICP-MS" de U-Pb

**claim_id:** `PETROCRON-M27-A06-LUHF-INSITU-007` (novo)
**Tipo:** imprecisão; resolve também uma pendência 🔵 da redação (citação primária não identificada)
**Onde:** Aula 06 · "Lu-Hf versus Sm-Nd"; Fontes
**Está escrito:** "datação in situ de Lu-Hf por LA-ICP-MS/MS [...] permite medir múltiplos pontos dentro do mesmo cristal com resolução espacial **comparável à do LA-ICP-MS discutido na Aula 03**"
**Problema:** a Aula 03 dá spots de ~10-50 μm para U-Pb. Na granada, Lu e sobretudo Hf estão em concentrações baixas, e os protocolos publicados usam spots de **~50-150 μm**, com incertezas de isócrona de alguns porcento (3,5-10% em Wu et al. 2023), bem piores que as de TIMS em frações microamostradas. A técnica evita a dissolução e amarra a análise à textura, mas não tem a resolução espacial de um U-Pb em zircão.
**Correção aplicada:** frase reescrita (spots tipicamente de dezenas a ~150 μm, precisão de alguns porcento; complementar, não substituto, da microamostragem); a citação primária entra nas Fontes: Simpson et al. (2021).
**Fonte:** Simpson et al. (2021), "In-situ Lu–Hf geochronology of garnet, apatite and xenotime by LA ICP MS/MS", *Chemical Geology* 577, 120299, doi:10.1016/j.chemgeo.2021.120299; Wu et al. (2023), "In situ Lu–Hf geochronology with LA-ICP-MS/MS analysis", *J. Anal. At. Spectrom.* 38, 1285-1300, doi:10.1039/D2JA00407K (spots de 50-150 μm; incertezas de 3,5-10%) · **Nível:** revisada por pares
**Confiança:** confirmado

### 🟠 14. Exemplo da Aula 06: zonas Sm-Nd lidas como idades de crescimento numa rocha que passou de ~680 °C

**claim_id:** `PETROCRON-M27-A06-EXEMPLO-INTEGRACAO-005`
**Tipo:** omissão que gera erro
**Onde:** Aula 06 · Exemplo trabalhado, Leitura integrada
**Está escrito:** as três zonas Sm-Nd (480, 472, 465 Ma) são lidas como idades de crescimento e dão "duração total de crescimento da granada de [...] 15 milhões de anos", numa rocha cujo pico, pelo próprio exemplo, ficou "certamente acima de ~680 °C", seguido de resfriamento lento (35 Ma)
**Problema:** a Aula 02 do mesmo módulo dá para o Sm-Nd em granada um fechamento de ~600-750 °C, e Mezger et al. (1992) mostram que, em terrenos de resfriamento lento acima de ~600 °C, granadas de até alguns centímetros dão idades de **resfriamento**, não de crescimento. O perfil zonado de Pollington & Baxter vem de uma rocha de fácies anfibolito. Ler zonas Sm-Nd como crescimento numa rocha acima de ~680 °C, sem checar se a difusão de Nd as reequilibrou, é exatamente a leitura sem crítica que o módulo condena, e o exemplo a ensina como correta.
**Correção aplicada:** acrescentada uma frase de ressalva na leitura: tratar as três zonas como idades de crescimento pressupõe que o pico não reequilibrou o Nd por difusão, o que precisa ser checado contra tamanho de grão, temperatura de pico e taxa de resfriamento (Aula 02); se o reequilíbrio tiver acontecido, as zonas registram resfriamento e a "duração de 15 Ma" deixa de valer. Nenhum número alterado.
**Fonte:** Mezger, Essene & Halliday (1992), *EPSL* 113, 397-409 (resumo lido); Baxter & Scherer (2013), *Elements* 9, 433-438 · **Nível:** revisada por pares
**Confiança:** confirmado

---

## Verificado e correto

**Bibliografia — 33 itens conferidos no Crossref (título, revista, volume, páginas, ano, autores):** Engi, Lanari & Kohn 2017 (RiMG 83, 1-12) · Kohn, Engi & Lanari eds. 2017 (RiMG 83) · Hoskin & Schaltegger 2003 · Corfu et al. 2003 · Dodson 1973 · Cherniak & Watson 2001 · Cherniak et al. 2004 · Copeland et al. 1988 · Cherniak 1993 · Cherniak 2000 · Chamberlain & Bowring 2001 · Scherer et al. 2000 · Ganguly & Tirone 1999 · Kylander-Clark et al. 2013 · Mattinson 2005 · Suzuki et al. 1994 · Montel et al. 1996 · Williams et al. 2007 · Ferry & Spear 1978 · Ghent 1976 (GeoScienceWorld) · Newton & Haselton 1981 · Powell & Holland 1994 (GeoScienceWorld) · Connolly 2005 · de Capitani & Petrakakis 2010 · Hollister 1966 · England & Thompson 1984 · Foster et al. 2002 (6 autores: Foster, Gibson, Parrish, Horstwood, Fraser, Tindle) · Hayden et al. 2008 · Zack et al. 2004 · Watson et al. 2006 · Baxter & Scherer 2013 · Spear & Pyle 2002 · Rubatto 2002 (título: 🟡 2). **Errados: 3** (Rubatto 2002, título; Pollington & Baxter 2010 e 2011, anos/revistas/volumes/páginas trocados).

**Valores numéricos conferidos e corretos como publicados:**

| Aula | Alegação | Situação · fonte |
|---|---|---|
| 01 | Th/U ~0,1 como fronteira indicativa; magmático tipicamente >0,5 com exceções | ✅ Hoskin & Schaltegger 2003; Rubatto 2002 |
| 02 | Zircão sem reabertura difusiva de Pb abaixo de ~900 °C | ✅ Cherniak & Watson 2001 |
| 02 | Monazita: 720-750 °C (campo), >900 °C para grãos de 10 μm a 10 °C/Ma (experimental) | ✅ Copeland et al. 1988; Cherniak et al. 2004 |
| 02 | Rutilo ~600-640 °C | ✅ Cherniak 2000 (~600 °C para grãos de ~100 μm), confirmado em rochas por Vry & Baker 2006, GCA 70, 1807-1820 |
| 02 | Apatita ~450-550 °C | ✅ Chamberlain & Bowring 2001 (~450 °C) |
| 02 | Rb-Sr biotita ~300-350 °C, muscovita ~450-500 °C | ✅ valores clássicos (~300 e ~500 °C, Jäger 1967; Purdy & Jäger 1976) |
| 02 | Lu-Hf em granada com fechamento ≥ Sm-Nd | ✅ Scherer et al. 2000 |
| 03 | CA-ID-TIMS: recozimento 800-1100 °C ~48 h; precisão ≤0,1% | ✅ Mattinson 2005 |
| 03 | EPMA 1-2 μm; ±30-50 Ma por ponto | ✅ Montel et al. 1996; Williams et al. 2007 |
| 03 | LA-ICP-MS 10-50 μm, 1-2% (2σ) | ✅ aproximação de referência, declarada como tal |
| 04 | GASP: 3 An = Grs + 2 Al₂SiO₅ + Qz | ✅ Ghent 1976 |
| 04 | Ferry & Spear: 0,207 GPa, até 800 °C | ✅ (limite inferior: 🔵 7) |
| 05 | Zr-em-titanita: 800-1000 °C, 1-2,4 GPa, tampão zircão+quartzo+rutilo, log-linear Zr-P-1/T | ✅ Hayden et al. 2008 |
| 05 | Zr-em-rutilo: 31 rochas, 430-1100 °C, 30-8400 ppm | ✅ Zack et al. 2004 |
| 06 | 12 zonas, 7,55 ± 0,52 Ma (2 DP), dois pulsos, Tauern Window | ✅ Pollington & Baxter 2010 (resumo) |

**Mecanismos e princípios conferidos:** zoneamento de Mn em sino por fracionamento de Rayleigh (Hollister 1966); caminhos horário/anti-horário (England & Thompson 1984); debate das granadas "rotacionadas" (Bell 1985, *J. Metamorphic Geol.* 3, 109-118, que a redação só descreveu, agora com referência); dissolução-reprecipitação em monazita (Williams et al. 2007; Schulz 2021); viés de Lu-Hf para o núcleo (Baxter & Scherer 2013; Smit et al. 2013).

**Plausibilidade dos exemplos hipotéticos:** Aula 03 (três problemas): coerente após o 🟠 6. Aula 04 (granada zonada): coerente. Aula 05 (zircão HREE): coerente. Aula 06: muscovita num metapelito com pico acima de ~680 °C é plausível só em pressões mais altas (a muscovita some por fusão desidratada perto de ~660 °C a 4,5 kbar, e mais alto com a pressão). Registrado aqui, sem achado: o exemplo não fixa pressão e a leitura continua defensável.

---

## Observações fora do escopo factual (para a revisão didática)

- Aula 04, "Microdomínios composicionais": grafia "equilíbrico" → "equilíbrio"; e "a composição do líquido/fluido" num contexto subsolidus (a granada de metapelito cresce da reação com a matriz, não de um líquido).
- Aula 04, recap: "célula a célula" é expressão sem sentido no contexto (provavelmente "zona a zona").

---

## Correções aplicadas

**Aplicadas em:** 2026-09-22 (mesma passagem)

| # | claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|---|
| 1 | `PETROCRON-M27-A01-EXEMPLO-NUCLEO-BORDA-004` | 🔴 | Corrigido | aula-01 |
| 2 | `PETROCRON-M27-A01-RUBATTO-TITULO-006` | 🟡 | Corrigido | aula-01, aula-05 |
| 3 | `PETROCRON-M27-A02-LU-CONCENTRACAO-GRANADA-009` | 🟠 | Corrigido | aula-02 |
| 4 | `PETROCRON-M27-A02-FONTES-AUSENTES-010` | 🟠 | Corrigido | aula-02, aula-05 |
| 5 | `PETROCRON-M27-A02-EXEMPLO-CINCO-IDADES-008` | 🟠 | Corrigido | aula-02 |
| 6 | `PETROCRON-M27-A03-SIMS-VS-LAICPMS-002` | 🟠 | Corrigido | aula-03 |
| 7 | `PETROCRON-M27-A04-GRT-BT-THERMOMETER-005` | 🔵 | Corrigido com ressalva (dado não verificável removido, nada inventado) | aula-04 |
| 8 | `PETROCRON-M27-A05-PARTICAO-VALORES-NUMERICOS-003` | 🔴 | Corrigido | aula-05 |
| 9 | `PETROCRON-M27-A05-QUEBRA-GRANADA-FUSAO-010` | 🟠 | Corrigido | aula-05 |
| 10 | `PETROCRON-M27-A05-MONAZITA-Y-PRE-GRANADA-011` | 🟠 | Corrigido | aula-05 |
| 11 | `PETROCRON-M27-A06-GRANADA-MEDIA-PONDERADA-001` | 🟠 | Corrigido | aula-06 |
| 12 | `PETROCRON-M27-A06-POLLINGTON-BIBLIO-006` | 🟠 | Corrigido | aula-06 |
| 13 | `PETROCRON-M27-A06-LUHF-INSITU-007` | 🟠 | Corrigido | aula-06 |
| 14 | `PETROCRON-M27-A06-EXEMPLO-INTEGRACAO-005` | 🟠 | Corrigido | aula-06 |

Além das correções, **todas as marcas `INCERTEZA DECLARADA`** das seis aulas foram substituídas pelo resultado da conferência (nas Fontes e nos blocos `alegacoes_auditaveis`), e cada aula ganhou um bloco `auditoria:` no fim dos metadados listando os achados que a tocaram. Toda edição de conteúdo é rastreável a um dos 14 números acima.

**Propagação:** nenhuma externa. O módulo não tem questionário, baralho nem glossário (a auditoria correu antes deles, na ordem certa); **não há card no Anki a corrigir à mão**. O hub (`27-petrocronologia-modulo.md`) repete só formulações neutras (o ponto de dificuldade sobre Y/HREE do zircão respondendo à granada continua correto) e foi atualizado apenas no registro de etapas. Nenhum outro módulo afirma os mesmos fatos com o erro: o módulo 26, que é pré-requisito, trata os sistemas isotópicos sem os coeficientes de partição nem a monazita.

**Pendências:** nenhuma que bloqueie. Três observações fora do escopo factual foram encaminhadas à revisão didática (seção anterior).

**Rastreabilidade (contada em disco, por script, depois das edições):** 41 alegações declaradas na redação (a01 5, a02 8, a03 6, a04 8, a05 9, a06 5) + 7 criadas pela auditoria (A01-RUBATTO-TITULO-006, A02-LU-CONCENTRACAO-GRANADA-009, A02-FONTES-AUSENTES-010, A05-QUEBRA-GRANADA-FUSAO-010, A05-MONAZITA-Y-PRE-GRANADA-011, A06-POLLINGTON-BIBLIO-006, A06-LUHF-INSITU-007) = **48 alegações** nos blocos de metadados, sem `claim_id` duplicado. Por aula agora: a01 6, a02 10, a03 6, a04 8, a05 11, a06 7. Nenhuma alegação ficou sem verificação.
