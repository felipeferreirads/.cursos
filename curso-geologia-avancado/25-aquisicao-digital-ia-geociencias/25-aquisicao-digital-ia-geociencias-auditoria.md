# Auditoria científica — Módulo 25: Aquisição de dados digitais e inteligência artificial em geociências

**Curso:** geologia-avancado
**Módulo:** 25 — `aquisicao-digital-ia-geociencias` (5 aulas)
**Modo:** `audit-and-fix` · **Profundidade:** `full`
**Passagens:** 2 (2026-09-21, ambas)
**Veredito:** **Aprovado** — 0 achados vermelhos, laranjas ou amarelos em aberto

---

## Nota de método: por que este relatório tem duas passagens e um achado perdido

A **passagem 1** (2026-09-21) auditou as Aulas 01 a 04, aplicou as correções e gravou as verificações nos blocos `alegacoes_auditaveis` das aulas, mas **terminou por limite de sessão antes de escrever este relatório, o manifesto `.json` e o bloco `audit` no `course-state.yaml`**. Isso é exatamente o que aconteceu no Módulo 24, e o procedimento aqui é o mesmo: reconstruir o que deixou rastro, declarar o que não deixou, e **não reciclar a numeração**.

O que foi recuperado dos metadados das aulas, em disco, antes de qualquer edição desta passagem:

| Evidência em disco | O que provou |
|---|---|
| `course-state.yaml` com mtime **anterior** aos das cinco aulas | a passagem 1 editou as aulas e **nunca** gravou o estado |
| ausência de `-auditoria.md` e `-auditoria.json` | nenhum relatório foi produzido |
| marcas `ACHADO VERMELHO 1`, `LARANJA 3`, `LARANJA 4`, `LARANJA 5`, `LARANJA 6`, `AMARELO 7` nos blocos de metadados | seis achados numerados sobreviveram, com fonte e correção descritas |
| nenhuma marca com o número **2** | **o achado 2 não é reconstruível** |
| `INCERTEZA DECLARADA` ainda presente só na Aula 05 | a Aula 05 **não foi auditada** na passagem 1 |

**Achado 2: declarado perdido.** Não há como saber que alegação ele tratava nem se a correção foi aplicada. Ele não é reaberto, não é renumerado e não é substituído: fica registrado como lacuna. A **passagem 2 começa em 8**, para que as marcas já gravadas nas aulas continuem apontando para o que apontam.

**Escopo da passagem 2:** a Aula 05 integralmente (7 alegações, nunca verificadas) mais as quatro alegações das Aulas 01 a 04 que a passagem 1 deixou sem verificação (`A01-SENSORES-ORIENTACAO-001`, `A03-ANAGLIFO-PARALAXE-001`, `A03-EXAGERO-VERTICAL-002`, `A04-REPOSITORIOS-006`). Os seis achados da passagem 1 **não foram reabertos nem reavaliados**, e as seis correções seguem aplicadas.

---

## Resumo por severidade

| Severidade | Levantados | Corrigidos | Em aberto |
|---|---|---|---|
| 🔴 Erro | 1 | 1 | **0** |
| 🟠 Impreciso | 7 | 7 | **0** |
| 🟡 Desatualizado | 3 | 3 | **0** |
| 🔵 Sem fonte | 0 | — | **0** |
| ⚪ Controverso | 0 | — | **0** |
| **Perdido (passagem 1)** | 1 | ? | declarado |

Achados numerados: **13**, sendo **1 perdido**. Alegações declaradas pelo redator: 34. Alegações levantadas pela auditoria: **9** (2 na passagem 1, 7 na passagem 2). Alegações rastreadas: **43** (6 na Aula 01, 7 na 02, 13 na 03, 8 na 04, 9 na 05). Sem auditar: 0.

---

## Achados recuperados da passagem 1 (1 a 7)

Reconstruídos das marcas nos metadados das aulas. As correções já estão em disco.

### 🔴 1. As duas fontes de comparação celular × bússola foram creditadas com a mesma conclusão, quando divergem

**claim_id:** `DIGGEO-M25-A01-PRECISAO-CELULAR-VS-BRUNTON-002`
**Tipo:** erro factual · **Onde:** Aula 01 · "Como o celular mede uma orientação"
**Problema:** a redação atribuía a Allmendinger, Siron & Scott (2017) **e** a Novakova & Pavlis (2017) a conclusão de precisão "comparável à bússola", com a incerteza dominada pelo procedimento "mais do que pelo sensor" — o **oposto** do que Novakova & Pavlis concluem.
**Fonte:** Novakova & Pavlis (2017), *J. Struct. Geol.* 97, 93-103 (resumo e Conclusions lidos em PDF: discrepâncias "in some cases higher than 80 deg"; "dip direction measurements were found less accurate than dip measurements"; "the source of the problem was instability in the magnetic sensor"); Allmendinger, Siron & Scott (2017), *J. Struct. Geol.* 102, 98-112, DOI 10.1016/j.jsg.2017.07.011.
**Desfecho:** **corrigido** na passagem 1 — a divergência entre as fontes passou a ser o próprio conteúdo da seção.

### 🟠 3. GeoSciML e EarthResourceML tratados como tendo o mesmo estatuto

**claim_id:** `DIGGEO-M25-A04-GEOSCIML-005`
**Tipo:** impreciso / confusão de escopo · **Onde:** Aula 04 · "Padrões de interoperabilidade"
**Problema:** a redação punha o GeoSciML "no âmbito do OGC" e os dois "alinhados ao OGC". O GeoSciML **é** padrão OGC (v4.1, 2017, OGC 16-008r1); o EarthResourceML **não é** — é padrão da CGI/IUGS assentado sobre OGC/ISO.
**Fonte:** OGC 16-008r1 (docs.ogc.org/is/16-008/16-008r1.html); CGI/IUGS, página do EarthResourceML.
**Desfecho:** **corrigido** na passagem 1.

### 🟠 4. "ALOS PALSAR de 12,5 m" listado como fonte de MDT de 12,5 m

**claim_id:** `DIGGEO-M25-A03-MDT-FONTES-006`
**Tipo:** omissão que gera erro · **Onde:** Aula 03 · "As fontes de MDT e de imagens"
**Problema:** o produto tem **espaçamento de pixel** de 12,5 m e modelo de elevação **reamostrado de fontes de 30 m** — listá-lo ao lado de produtos de 30 m, numa aula cujo argumento é que "a resolução limita o que se enxerga", tornava a afirmação enganosa como escrita.
**Fonte:** Alaska Satellite Facility, docs.asf.alaska.edu/datasets/palsar e ASF RTC product guide.
**Desfecho:** **corrigido** na passagem 1 — AW3D30 no lugar, e a armadilha nomeada.

### 🟠 5. "MDT é, em geral, um modelo de superfície"

**claim_id:** `DIGGEO-M25-A03-MDS-VS-MDT-009` *(alegação criada pela auditoria)*
**Tipo:** inconsistência interna · **Onde:** Aula 03 · "As fontes de MDT e de imagens"
**Problema:** contradição nos próprios termos, confundindo MDS e MDT justamente onde o aluno precisa distingui-los.
**Desfecho:** **corrigido** na passagem 1 — as duas siglas definidas e o uso frouxo corrente declarado.

### 🟠 6. Definição de lineamento estreitada para "origem presumivelmente estrutural"

**claim_id:** `DIGGEO-M25-A03-LINEAMENTO-DEFINICAO-004`
**Tipo:** erro de definição · **Onde:** Aula 03 · "Interpretação hierárquica"
**Problema:** O'Leary, Friedman & Pohn (1976) dizem "presumably reflects a subsurface phenomenon", não origem estrutural; a versão estreitada contradizia a ressalva seguinte da própria aula.
**Fonte:** O'Leary, Friedman & Pohn (1976), *GSA Bulletin* 87(10), 1463-1469.
**Desfecho:** **corrigido** na passagem 1, com "simples ou composta" restituído.

### 🟡 7. Pré-requisito creditado à Aula 01 que a Aula 01 não tem

**claim_id:** `DIGGEO-M25-A03-PREREQ-ESTEREOGRAMA-010` *(alegação criada pela auditoria)*
**Tipo:** atribuição interna incorreta · **Onde:** Aula 03 · cabeçalho
**Problema:** o cabeçalho assumia "leitura de estereogramas vista na Aula 01"; a Aula 01 ensina notação de direção de mergulho/mergulho e média vetorial por polos, e **não** apresenta estereograma nenhum.
**Desfecho:** **corrigido** na passagem 1.

### ⛔ 2. Perdido

Aplicado na passagem 1 sem deixar marca. Severidade, aula, alegação e desfecho **desconhecidos**. Não reconstruível. Fica declarado, não disfarçado.

---

## Achados novos da passagem 2 (8 a 13)

### 🟠 8. A independência do sinal analítico em relação à direção de magnetização vale em 2D, não em dados em grade

**claim_id:** `DIGGEO-M25-A03-SINAL-ANALITICO-3D-011`
**Tipo:** confusão de escopo + certeza indevida · **Onde:** Aula 03 · "Integrar as três fontes: a lógica da coincidência"
**Está escrito:** "em baixas latitudes magnéticas (como no norte do Brasil), a redução ao polo é numericamente instável, e o sinal analítico, que independe da direção de magnetização, é preferido."
**Problema:** a independência é propriedade do sinal analítico **bidimensional** de Nabighian (1972). Li (2006) demonstrou que, no caso **tridimensional** — que é o caso de qualquer grade aerogeofísica —, a amplitude do sinal analítico **depende** da direção do campo ambiente e da direção de magnetização. A aula afirma a propriedade sem qualificação e exatamente no contexto em que o resíduo mais aparece (baixa latitude magnética, magnetização remanente): a recomendação prática continua certa, a justificativa não. A passagem 1 aceitou esta frase como "conhecimento consolidado de geofísica de campos potenciais" sem verificá-la.
**Correção aplicada:** a preferência pelo sinal analítico é mantida; acrescentada a distinção 2D/3D com a fonte, e a ressalva de que ele **reduz, mas não elimina** a dependência.
**Fonte:** Li, X. (2006), "Understanding 3D analytic signal amplitude", *Geophysics* 71(2), L13-L16, DOI 10.1190/1.2184367. · **Nível:** revisada por pares (SEG) · **Confiança:** confirmado
**Também aparece em:** nenhum outro arquivo do módulo.

### 🟠 9. INSPIRE descrito como tendo adotado GeoSciML e EarthResourceML como padrões obrigatórios

**claim_id:** `DIGGEO-M25-A04-INSPIRE-OBRIGATORIO-007`
**Tipo:** impreciso / confusão de escopo · **Onde:** Aula 04 · "Padrões de interoperabilidade"
**Está escrito:** "a diretiva europeia INSPIRE os adotou como padrões obrigatórios de troca de dados geológicos e de recursos minerais."
**Problema:** o que é vinculante na União Europeia são as **especificações de dados do próprio INSPIRE** (temas Geology e Mineral Resources), cujo modelo de dados é *baseado em* GeoSciML e EarthResourceML — não os padrões da CGI em si. E parte dos esquemas derivados fica **declaradamente fora** das regras de implementação: a própria especificação registra que esquemas adicionais, como a `MineralResourcesExtension`, "are not included in the Implementing Rules". O erro é o mesmo do achado 3, uma frase adiante: achatar estatuto de padrão. A passagem 1 verificou este ponto contra a **página do próprio padrão na CGI** — a fonte interessada, não a normativa.
**Correção aplicada:** trocado "adotou como padrões obrigatórios" por "baseou neles as suas especificações de dados", com a distinção explicitada.
**Fonte:** INSPIRE, D2.8.III.21 *Data Specification on Mineral Resources — Technical Guidelines* (inspire-mif.github.io/technical-guidelines/data/mr/dataspecification_mr.html) e *Data Specification on Geology*; BGS, página EU INSPIRE Directive. · **Nível:** normativa · **Confiança:** confirmado

### 🟠 10. Três obras creditadas no corpo da Aula 05 estão ausentes da lista de Fontes

**claim_id:** `DIGGEO-M25-A05-FONTES-AUSENTES-008`
**Tipo:** omissão que gera erro · **Onde:** Aula 05 · "O papel do modelo metalogenético" e "Fontes"
**Está escrito:** "decomposição introduzida por Wyborn, Heinrich & Jaques (1994) e refinada por Knox-Robinson & Wyborn (1997) e Hronsky & Groves (2008)."
**Problema:** as três obras são creditadas com autor e ano no texto e **não aparecem** na seção Fontes, que lista oito outras referências. Num módulo cuja Aula 04 ensina proveniência, licença e identificador persistente, uma citação que o aluno não consegue seguir é defeito material, não descuido de forma. As três atribuições, verificadas, estão **corretas** — o que faltava era poder conferi-las.
**Correção aplicada:** as três referências acrescentadas à seção Fontes, com veículo, volume, páginas e DOI onde existe.
**Fontes verificadas:**
- Wyborn, L. A. I., Heinrich, C. A. & Jaques, A. L. (1994), "Australian Proterozoic mineral systems: essential ingredients and mappable criteria", *AusIMM Annual Conference*, 109-115 — definição confirmada: "mobilising ore components from a source, transporting and accumulating them in more concentrated form and then preserving them throughout the subsequent geological history", que é a decomposição fonte–transporte–armadilha–preservação que a aula usa. *Ressalva de fonte:* a literatura cita o volume com dois locais de conferência (Darwin no acervo da AusIMM, Melbourne em citações secundárias); a página da AusIMM é a referência adotada.
- Knox-Robinson, C. M. & Wyborn, L. A. I. (1997), "Towards a holistic exploration strategy: using Geographic Information Systems as a tool to enhance exploration", *Australian Journal of Earth Sciences* 44(4), 453-463, DOI 10.1080/08120099708728326.
- Hronsky, J. M. A. & Groves, D. I. (2008), "Science of targeting: definition, strategies, targeting and performance measurement", *Australian Journal of Earth Sciences* 55(1), 3-12, DOI 10.1080/08120090701581356.
**Confiança:** confirmado (veículo, volume e páginas conferidos para as duas últimas; a primeira é ata de conferência, sem DOI)

### 🟠 11. Exagero vertical apresentado como condicional ao ajuste de paralaxe

**claim_id:** `DIGGEO-M25-A03-EXAGERO-INTRINSECO-012`
**Tipo:** omissão que gera erro · **Onde:** Aula 03 · "Ver em relevo o que a tela mostra achatado"
**Está escrito:** "A estereoscopia (sobretudo com a paralaxe ajustada para realçar o relevo) faz o terreno parecer mais íngreme do que é."
**Problema:** o parêntese ensina que o exagero é um efeito opcional, que aparece quando alguém mexe na paralaxe. Não é: num modelo estéreo a escala vertical raramente iguala a horizontal, e o exagero é consequência da **geometria do par** — da razão base-altura (distância entre os pontos de vista sobre a altura de observação), da distância focal e da sobreposição. Um aluno que leia o parêntese pode concluir que um anaglifo "não ajustado" entrega mergulho confiável, o que contradiz a instrução correta que a própria aula dá duas linhas abaixo.
**Correção aplicada:** o exagero é declarado intrínseco e o mecanismo nomeado (razão base-altura, e o fator de deslocamento no anaglifo derivado de MDT). **Nenhum fator numérico de exagero é afirmado**, em continuidade com a decisão do redator.
**Fonte:** razão base-altura e sua relação com exagero vertical: Esri GIS Dictionary, "base-height ratio"; *Photogrammetric Engineering* (ASPRS), "Vertical exaggeration in stereoscopic models" e "Some factors causing vertical exaggeration and slope distortion" (set. 1953); Lillesand, Kiefer & Chipman (2015), cap. de fotogrametria. · **Nível:** base de referência + revisada por pares · **Confiança:** confirmado

### 🟡 12. Instrução editorial não resolvida publicada na lista de Fontes

**claim_id:** `DIGGEO-M25-A03-LILLESAND-EDICAO-013`
**Tipo:** evidência insuficiente, agora resolvida · **Onde:** Aula 03 · "Fontes"
**Está escrito:** "Lillesand, T. M., Kiefer, R. W. & Chipman, J. W., *Remote Sensing and Image Interpretation* (Wiley; **conferir a edição**)"
**Problema:** o "conferir a edição" é uma nota do redator para a auditoria que foi publicada como se fosse parte da referência. Além de não ser citável, sinaliza ao aluno que a fonte é incerta quando ela não é.
**Correção aplicada:** edição fixada.
**Fonte:** Lillesand, T. M., Kiefer, R. W. & Chipman, J. W. (2015), *Remote Sensing and Image Interpretation*, 7ª ed., Wiley, ISBN 9781118343289. · **Confiança:** confirmado

### 🟡 13. GEOROC descrito como base de rochas ígneas apenas

**claim_id:** `DIGGEO-M25-A04-GEOROC-ESCOPO-008`
**Tipo:** desatualização de escopo · **Onde:** Aula 04 · "Dados abertos: onde buscar e como citar"
**Está escrito:** "o GEOROC (rochas ígneas)"
**Problema:** o GEOROC reúne análises de rochas e minerais **ígneos e metamórficos**, e desde 2021 deixou o Max Planck de Mainz e passou a ser curado pelo projeto DIGIS na Universidade de Göttingen (georoc.eu, GEOROC 2.0), com pipeline de dados para o EarthChem. Numa aula que ensina a citar fonte com versão, a etiqueta de escopo incompleta e a instituição implícita desatualizada são o tipo de detalhe que a própria aula manda conferir.
**Correção aplicada:** escopo completado e curadoria atual nomeada.
**Fonte:** georoc.eu; DIGIS/GZG, Universidade de Göttingen; re3data.org/repository/r3d100011206. · **Confiança:** confirmado

---

## Verificado e correto (achados azuis)

O que a passagem 2 abriu e **não** precisou alterar.

| # | Alegação | Fonte consultada | Resultado |
|---|---|---|---|
| B1 | `A05-CRACKNELL-READING-004` — Cracknell & Reading (2014): cinco algoritmos, floresta aleatória como boa primeira escolha, influência da distribuição espacial do treino, "informação espacial explícita" como termo dos autores | *Computers & Geosciences* 63, 22-33, DOI 10.1016/j.cageo.2013.10.008 | **Confirmado integralmente.** Os cinco algoritmos são Naive Bayes, k-NN, florestas aleatórias, SVM e redes neurais. A floresta aleatória melhora ainda mais a vantagem relativa **à medida que o treino fica espacialmente mais disperso**. O uso de informação espacial explícita "generates accurate lithology predictions but should be used in conjunction with geophysical data in order to generate geologically plausible predictions" — o que **sustenta** a afirmação da aula de que incluir coordenadas melhorou o mapeamento litológico, com a nuance de que sozinhas dão acurácia sem plausibilidade geológica. A `INCERTEZA DECLARADA` do redator é retirada. |
| B2 | `A05-SISTEMA-MINERALIZADOR-005` — os quatro passos de tradução de McCuaig, Beresford & Hronsky (2010) | *Ore Geology Reviews* 38, 128-138, DOI 10.1016/j.oregeorev.2010.05.008 | **Confirmado.** O processo de quatro passos é exatamente "(1) critical processes of the mineral system, (2) constituent processes, (3) targeting elements reflected in geology, (4) targeting criteria used to detect the targeting elements" — a descrição da aula é fiel. O artigo ilustra com Ni-Cu-EGP em komatiito e ouro orogênico, e trata as quatro fontes de incerteza da cadeia. A atribuição da **decomposição por componentes** a Wyborn et al. (1994), e do **processo de tradução** a McCuaig et al. (2010), está corretamente separada no corpo da aula. |
| B3 | `A05-LITERATURA-PROSPECTIVIDADE-006` — Carranza & Laborte (2015), *C&G* 74, 60-70 | DOI 10.1016/j.cageo.2014.10.004 | **Confirmado**, inclusive o conteúdo: floresta aleatória com **menos de 20** locais de treino (12 prospectos de pórfiro de Cu em Abra) e ganho de acurácia por imputação de valores ausentes. |
| B4 | idem — Xiong & Zuo (2016), *C&G* 86, 75-82 | dblp; índices | **Confirmado**, autocodificador profundo por erro de reconstrução. |
| B5 | idem — Zuo (2017), *Natural Resources Research* 26, 457-464 | DOI 10.1007/s11053-017-9345-4 | **Confirmado**, revisão de métodos de aprendizado de máquina para anomalias geoquímicas. |
| B6 | idem — Yousefi & Carranza (2015), *C&G* 79, 69-81 | ADS 2015CG.....79...69Y | **Confirmado**, gráfico predição-área. |
| B7 | idem — Carranza (2008), *Handbook of Exploration and Environmental Geochemistry* vol. 11, Elsevier | ISBN 978-0-444-51325-0, 368 pp. | **Confirmado**, incluindo a caracterização como referência de GIS aplicado a prospectividade. A `INCERTEZA DECLARADA` do redator sobre estas cinco referências é retirada. |
| B8 | `A05-PESOS-EVIDENCIA-001` + Bonham-Carter, Agterberg & Wright (1989) | GSC Paper 89-9, em *Statistical Applications in the Earth Sciences* (eds. Agterberg & Bonham-Carter) | **Referência confirmada.** Aritmética **reexecutada e reproduzida dígito a dígito**: P(B\|D)=0,600; P(B\|¬D)=0,1918; razão 3,128; W⁺=+1,140; W⁻=−0,703; C=1,844; chances 0,0638 e 0,0101, probabilidades 6,000% e 1,000%, coincidindo com 12/200 e 8/800. O uso de "chance" para *odds* e a conversão para probabilidade estão corretos. |
| B9 | `A05-VALIDACAO-ESPACIAL-002` — AUC 0,920 (aleatória) × 0,686 (blocos) | execução do código da aula | **Reproduzido exatamente** em Python 3.13.2, NumPy 2.5.1, scikit-learn 1.9.1: prevalência 180/1200 (15%), 16 blocos, AUC 0,920 e 0,686. |
| B10 | `A05-VAZAMENTO-ESPACIAL-003` — vazamento por partição aleatória e correção por blocos | Roberts et al. (2017), *Ecography* 40(8), 913-929, DOI 10.1111/ecog.02881 | **Confirmado**, e a alegação de que é "a mesma fonte da Aula 01 do Módulo 24" foi verificada **no próprio arquivo**: a Aula 01 do Módulo 24 cita essa referência com volume, páginas e DOI idênticos. |
| B11 | Três citações internas da Aula 05 ao Módulo 24 | arquivos do Módulo 24 em disco | **Todas as três conferem.** (i) "classificação binária extremamente desbalanceada, como na Aula 06 do Módulo 24" — a Aula 06 do M24 é de fato a que formaliza desbalanceamento, com o exemplo das 200 encostas (4% instáveis, acurácia 0,96, revocação 0). (ii) "o roteiro de comunicação da Aula 07 do Módulo 24" — a Aula 07 tem a seção "Comunicar resultados com suas limitações", com os quatro itens. (iii) a ressalva sobre importância por impureza e por permutação corresponde a dois achados já corrigidos na auditoria do M24. **O `dominant_pattern` dos Módulos 22, 23 e 24 — a citação interna como ponto de falha — NÃO se repetiu na Aula 05.** Repetiu-se apenas na Aula 03 (achado 7, passagem 1). |
| B12 | `A01-SENSORES-ORIENTACAO-001` — acelerômetro dá o mergulho, magnetômetro dá a direção, leitura magnética exige declinação, magnetômetro perturbado por magnetita e aço | Allmendinger, Siron & Scott (2017), *J. Struct. Geol.* 102, 98-112 (ADS 2017JSG...102...98A); Novakova & Pavlis (2017) | **Confirmado.** O resumo de Allmendinger et al. sustenta tanto o mecanismo quanto o enquadramento da aula: os autores registram explicitamente que "recent work has called into question the reliability of sensors on Android devices", que é a divergência que a aula ensina. A `INCERTEZA DECLARADA` do redator é retirada. |
| B13 | `A05-NEGATIVOS-VIES-007` — inexistência de negativos verdadeiros, viés de amostragem, leitura como ordenação relativa | Carranza (2008); Zuo (2017); literatura de prospectividade | **Mantido como julgamento metodológico consolidado, não promovido a fato.** Verificar uma alegação não muda a natureza dela: isto é princípio de método, não medida nem classificação formal. Mesmo critério aplicado nos Módulos 22 e 23. |
| B14 | `A03-ANAGLIFO-PARALAXE-001` — anaglifo em cores complementares, paralaxe proporcional à altura, construção por deslocamento de pixels segundo o MDT, pseudoscopia por troca das imagens | Lillesand, Kiefer & Chipman (2015), 7ª ed., caps. de fotogrametria e visão estereoscópica; literatura de fotogrametria | **Confirmado.** A proporcionalidade é exata no anaglifo construído por deslocamento a partir de um MDT, e aproximada no par fotográfico clássico — a aula constrói o caso digital, em que ela vale. Ver achado 12 para a edição. |
| B15 | `A02-COMPOSICIONAL-004` — nota da Aula 02 sobre as matrizes de correlação do Módulo 24 usarem elementos-traço em ppm | arquivo da Aula 02 do Módulo 24 | **Confere.** As variáveis são Cu, Zn e As em ppm (mais Au em ppb e duas variáveis não composicionais). O argumento de que o efeito de fechamento é menor aí que nos elementos maiores está correto. |
| B16 | `A04-REPOSITORIOS-006` — GeoSGB, USGS, Geoscience Australia, EarthChem/PetDB, Macrostrat, PBDB, Zenodo, CC BY 4.0 | portais e re3data | **Confirmado**, com uma correção de escopo no GEOROC (achado 13). O EarthChem de fato agrega PetDB e outras bases, com busca combinada sobre seis bases geoquímicas. |
| B17 | Exemplos numéricos das Aulas 01, 02 e 03 | reexecução | **Todos reproduzidos dígito a dígito.** Aula 01: \|R\|/n=0,9979, dd=93,9°, mergulho=41,5°, desvios 2,0/2,5/5,3/3,5/4,3. Aula 02: médias 13,00 / 11,75 / 10,50 ppb e razão 1,238. Aula 03: produto vetorial (0; 54.000; 270.000), mergulho 11,3°, dd 180,0°, direção RHR 90,0°; média axial 36,3° com R=0,961 contra 72,4° da média ingênua. |

**Nenhum achado branco.** O módulo é em boa parte metodológico, mas as afirmações que faz são de classificação, atribuição e procedimento, não de posições em disputa. O único ponto com divergência real na literatura — a acurácia de celulares como bússola — já é **ensinado como divergência** pela própria aula, que é o tratamento correto.

---

## Correções aplicadas

**Aplicadas em:** 2026-09-21 (passagem 2; as dos achados 1 e 3 a 7 são da passagem 1)

| claim_id | # | Sev. | Desfecho | Arquivos alterados |
|---|---|---|---|---|
| `DIGGEO-M25-A01-PRECISAO-CELULAR-VS-BRUNTON-002` | 1 | 🔴 | Corrigido (passagem 1) | aula-01 |
| — | 2 | ? | **Perdido — não reconstruível** | desconhecido |
| `DIGGEO-M25-A04-GEOSCIML-005` | 3 | 🟠 | Corrigido (passagem 1) | aula-04 |
| `DIGGEO-M25-A03-MDT-FONTES-006` | 4 | 🟠 | Corrigido (passagem 1) | aula-03 |
| `DIGGEO-M25-A03-MDS-VS-MDT-009` | 5 | 🟠 | Corrigido (passagem 1) | aula-03 |
| `DIGGEO-M25-A03-LINEAMENTO-DEFINICAO-004` | 6 | 🟠 | Corrigido (passagem 1) | aula-03 |
| `DIGGEO-M25-A03-PREREQ-ESTEREOGRAMA-010` | 7 | 🟡 | Corrigido (passagem 1) | aula-03 |
| `DIGGEO-M25-A03-SINAL-ANALITICO-3D-011` | 8 | 🟠 | Corrigido | aula-03 (corpo + Fontes + metadados) |
| `DIGGEO-M25-A04-INSPIRE-OBRIGATORIO-007` | 9 | 🟠 | Corrigido | aula-04 (corpo + metadados) |
| `DIGGEO-M25-A05-FONTES-AUSENTES-008` | 10 | 🟠 | Corrigido | aula-05 (Fontes + metadados) |
| `DIGGEO-M25-A03-EXAGERO-INTRINSECO-012` | 11 | 🟠 | Corrigido | aula-03 (corpo + metadados) |
| `DIGGEO-M25-A03-LILLESAND-EDICAO-013` | 12 | 🟡 | Corrigido | aula-03 (Fontes + metadados) |
| `DIGGEO-M25-A04-GEOROC-ESCOPO-008` | 13 | 🟡 | Corrigido | aula-04 (corpo + metadados) |

**Propagação:** nenhuma. O módulo **não tem questionário, baralho de flashcards nem glossário** — a auditoria correu antes deles, que é a ordem certa. Não há card já importado no Anki a corrigir à mão. O hub do módulo foi atualizado apenas no registro de etapas; nenhuma das correções toca texto que ele repita.

**Pendências:** nenhuma em aberto. Fica registrado o **achado 2 como perdido**, e a ressalva de fonte do local de conferência de Wyborn et al. (1994).

**Gate:** **liberado** para `gerador-de-questionarios` e `gerador-de-flashcards` — 0 vermelhos e 0 laranjas em aberto.

---

## Observação fora de escopo (não é achado factual)

Uma só, de redação, registrada aqui sem misturar com os achados: na Aula 04, "Regras de **normalização** manda não repetir o mesmo fato" tem erro de concordância. Fica para a revisão didática.

## Padrão dominante desta auditoria

Os dois achados laranjas mais graves da passagem 2 têm a mesma assinatura, e ela é nova no curso: **a passagem 1 verificou afirmações contra a fonte interessada em vez da fonte normativa, ou não as verificou por parecerem consolidadas.** O achado 9 (INSPIRE) foi checado na página promocional do próprio padrão; o achado 8 (sinal analítico) foi dispensado como "conhecimento consolidado de geofísica de campos potenciais" — e é precisamente uma propriedade 2D que a literatura demonstrou não valer em 3D desde 2006. Corolário para os módulos seguintes: **a frase que soa mais consolidada é a que menos foi conferida**, e uma alegação verificada contra quem a promove não está verificada.
