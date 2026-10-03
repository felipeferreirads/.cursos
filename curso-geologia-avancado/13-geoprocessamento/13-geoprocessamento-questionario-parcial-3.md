# Questionário parcial 3 — Módulo 13: Geoprocessamento

**Módulo:** [[13-geoprocessamento-modulo|Módulo 13 — Geoprocessamento]]
**Cobertura:** Aulas 06 e 07 — modelos digitais de elevação (MDT/MDS, declividade, hipsometria, análise hidrológica D8, lineamentos) e layout cartográfico normatizado/projeto integrado.
**Recorte:** os produtos derivados de MDE e a entrega final — o que se extrai de uma superfície contínua de elevação, e como o projeto inteiro do módulo chega a um mapa entregável e auditável.
**Objetivos avaliados:** `geologia-avancado-m13-oa04` (integral — a06 + a07)
**Pontuação total:** 100 pontos · o gabarito fica oculto; responda antes de abrir.

---

### 1. Múltipla escolha — `geologia-avancado-m13-q20` · oa04 · 10 pts

Um projeto precisa calcular declividade e delinear a rede de drenagem de uma bacia coberta por floresta densa. Deve usar um MDT ou um MDS, e por quê?

- a) MDS, porque inclui mais informação (topo da vegetação também é dado útil)
- b) MDT, porque representa a elevação do terreno "nu"; um MDS usado sem correção incorporaria o topo da copa das árvores como se fosse relevo real, distorcendo declividade e direção de fluxo
- c) Tanto faz, porque a diferença entre MDT e MDS é desprezível em qualquer tipo de cobertura vegetal
- d) MDS, porque é sempre o produto de maior resolução espacial disponível

<details>
<summary>Ver resposta</summary>

**Resposta: b**

O **MDT** (Modelo Digital de Terreno) representa a elevação da superfície do terreno excluindo vegetação e edificações; o **MDS** (Modelo Digital de Superfície) representa a elevação do topo de tudo o que existe sobre o terreno, incluindo a copa das árvores. Para análise morfométrica e hidrológica — declividade, direção de fluxo, rede de drenagem — o produto correto é o MDT: um MDS usado sem correção trataria o topo da vegetação como se fosse relevo real, distorcendo toda a análise derivada. A diferença MDS − MDT, aliás, é o próprio método usado para estimar altura de vegetação, não um dado a descartar — mas não é o insumo da análise de relevo. "a", "c" e "d" ignoram esse critério funcional.
</details>

---

### 2. Verdadeiro ou Falso (justifique) — `geologia-avancado-m13-q21` · oa04 · 10 pts

"A liberação da versão de 30 m do SRTM para áreas fora dos Estados Unidos, ocorrida entre 2014 e 2015, representa um refinamento do dado — a missão original, de 2000, havia adquirido apenas a resolução de 90 m."

<details>
<summary>Ver resposta</summary>

**Falso.**

A missão SRTM, voada em **fevereiro de 2000**, já adquiriu dados com espaçamento de **1 segundo de arco (~30 m)** para quase todo o globo entre 60°N e 56°S — não houve novo levantamento nem refinamento em 2014-2015. O que mudou foi a **política de distribuição**: por restrição de acesso, fora dos EUA só a versão reamostrada para 3 segundos de arco (~90 m) foi publicada por mais de uma década; a liberação global da resolução de 1 segundo de arco começou em **setembro de 2014** (América do Sul em novembro de 2014) e se completou em 2015. Tratar essa mudança como "refinamento do dado" é um erro registrado pela auditoria científica deste módulo — o dado de 30 m sempre existiu desde a aquisição, só não estava publicamente disponível fora dos EUA.
</details>

---

### 3. Aplicação (cálculo) — `geologia-avancado-m13-q22` · oa04 · 15 pts

Um analista aplica um limiar de acumulação de fluxo de 800 células para delinear a rede de drenagem derivada de um MDE. Calcule a área de drenagem contribuinte mínima representada por esse limiar (a) usando um MDE de resolução 12,5 m e (b) usando um MDE de resolução 30 m, para a mesma bacia. (c) Um colega compara a densidade de drenagem obtida nos dois MDEs usando o mesmo limiar de 800 células e conclui que o MDE de 30 m produziu uma rede "mais grosseira, mas hidrologicamente equivalente". O que está errado nessa conclusão?

<details>
<summary>Ver resolução</summary>

**(a)** Célula de 12,5 × 12,5 m = 156,25 m². Área mínima = 800 × 156,25 = 125.000 m² = **0,125 km² (12,5 ha)**.

**(b)** Célula de 30 × 30 m = 900 m². Área mínima = 800 × 900 = 720.000 m² = **0,72 km² (72 ha)**.

**(c)** A conclusão do colega está errada porque o **mesmo número de células não representa a mesma área de contribuição** nos dois MDEs — a área mínima no MDE de 30 m (0,72 km²) é quase **6 vezes maior** que no MDE de 12,5 m (0,125 km²). Não se trata de "mesma rede, resolução mais grosseira": o limiar de 800 células, aplicado ao MDE de 30 m, está exigindo uma bacia de contribuição bem maior antes de classificar uma célula como canal — a rede resultante não é apenas visualmente mais grosseira, é **hidrologicamente diferente**, porque omite canais reais que teriam sido capturados no MDE mais fino. A comparação correta exige expressar o limiar em área real (km² ou ha), não em número de células, antes de comparar redes derivadas de MDEs de resolução diferente.
</details>

---

### 4. Dissertativa curta — `geologia-avancado-m13-q23` · oa04 · 10 pts

Uma bacia hidrográfica tem curva hipsométrica claramente convexa (área concentrada nas altitudes relativas mais elevadas). O que essa forma indica sobre o estágio evolutivo geomorfológico da bacia, e o que se esperaria observar numa bacia com curva côncava, no extremo oposto?

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:**

Uma curva hipsométrica **convexa** — com a maior parte da área da bacia concentrada nas altitudes relativas mais elevadas — é característica de uma bacia **geomorfologicamente jovem**, ainda dominada por processos de **incisão vertical ativa**, com pouco tempo de erosão acumulada: grande parte do relevo original ainda está "alto", pouco rebaixado.

No extremo oposto, uma curva **côncava** (área concentrada nas altitudes relativas mais baixas) é característica de uma bacia **madura ou senil**, onde grande parte do relevo original já foi rebaixado por erosão prolongada ao longo do tempo geológico. Entre as duas, uma curva sigmoidal (em S) indica um estágio intermediário de equilíbrio. A classificação transforma uma propriedade puramente geométrica extraída do MDE (a distribuição estatística de altitudes normalizada por área) num indicador interpretável do processo geomorfológico responsável por esculpir aquela paisagem — os trabalhos clássicos de Strahler sobre geomorfologia quantitativa.
</details>

---

### 5. Múltipla escolha — `geologia-avancado-m13-q24` · oa04 · 10 pts

No algoritmo D8 de direção de fluxo, cada célula do MDE recebe:

- a) Múltiplas direções de escoamento, proporcionais à declividade em cada uma das oito direções vizinhas
- b) Uma única direção de escoamento, escolhida entre as oito células vizinhas (quatro ortogonais e quatro diagonais), correspondente à maior declividade descendente a partir daquela célula
- c) Uma direção fixa, sempre a mesma para todas as células do MDE, definida pela orientação geral da bacia
- d) Nenhuma direção — o D8 calcula apenas a acumulação de fluxo, não a direção

<details>
<summary>Ver resposta</summary>

**Resposta: b**

O **D8** (*eight-direction*) atribui a cada célula uma **única** direção de escoamento, escolhida entre as oito células vizinhas, correspondente à direção de **maior declividade descendente**. É sobre essa direção de fluxo, célula a célula, que se calcula depois a acumulação de fluxo (número de células a montante cujo fluxo converge para cada célula) — "d" inverte a ordem lógica da cadeia. "a" descreve um algoritmo diferente (de múltiplas direções, como o MFD, não o D8 clássico); "c" ignora que a direção é calculada célula a célula, não fixa para toda a bacia.
</details>

---

### 6. Verdadeiro ou Falso (justifique) — `geologia-avancado-m13-q25` · oa04 · 10 pts

"Um alinhamento retilíneo de vales, identificado por inspeção visual de um hillshade derivado de MDE, confirma a existência de uma falha ou zona de fratura no local."

<details>
<summary>Ver resposta</summary>

**Falso.**

Um lineamento identificado por geoprocessamento é uma **hipótese** de controle estrutural, não uma confirmação. O mesmo alinhamento retilíneo de vales pode resultar de uma zona de fraqueza estrutural real, mas também de um **artefato do próprio processamento** (a direção de iluminação escolhida no hillshade favorece certas orientações e disfarça outras — um viés conhecido do método), de um **controle litológico não estrutural** (um contato entre rochas de resistência diferente à erosão, sem falha alguma) ou de uma **feição antrópica** (estrada, linha de transmissão, canal retificado). A verificação de campo — checar se há de fato uma zona de falha, fratura ou cisalhamento no local — é etapa obrigatória antes de qualquer interpretação estrutural ser dada como estabelecida, nunca opcional.
</details>

---

### 7. Múltipla escolha — `geologia-avancado-m13-q26` · oa04 · 10 pts

Qual das especificações técnicas brasileiras homologadas pela CONCAR trata especificamente de simbologia e representação em layout cartográfico — a mais próxima do tema desta aula?

- a) ET-EDGV (Estruturação de Dados Geoespaciais Vetoriais)
- b) ET-ADGV (Aquisição de Dados Geoespaciais Vetoriais)
- c) ET-RDG (Representação de Dados Geoespaciais)
- d) NBR 13133:1994

<details>
<summary>Ver resposta</summary>

**Resposta: c**

A **ET-RDG** (Representação de Dados Geoespaciais), publicada pela DSG (Diretoria de Serviço Geográfico do Exército) e homologada pela CONCAR, é a especificação pertinente a simbologia e layout. As outras duas siglas de nome parecido tratam de outra coisa: a **ET-EDGV** trata de **estruturação** de dados vetoriais (esquema de atributos, não simbologia), e a **ET-ADGV** trata de **aquisição** de dados vetoriais — confundir "estruturação" com "aquisição" nessas duas siglas foi um erro corrigido pela auditoria científica deste módulo. A **NBR 13133** trata de execução de levantamento topográfico, e sua edição vigente é a de **2021** (que cancelou e substituiu a de 1994), não simbologia de layout.
</details>

---

### 8. Aplicação — `geologia-avancado-m13-q27` · oa04 · 15 pts

Um mapa final combina um raster de declividade (0° a 90°, dado contínuo) com um polígono vetorial de unidades litológicas (categórico, sem ordem). (a) Que tipo de paleta de cores é adequado para cada camada, e por quê? (b) Se o mapa de declividade precisar destacar especificamente as áreas acima de um limiar regulatório de 30° (acima do qual uma norma de uso do solo proíbe construção), que ajuste de paleta e de classificação melhora a comunicação desse limite específico, em vez de uma paleta sequencial genérica?

<details>
<summary>Ver resolução</summary>

**(a)** O raster de **declividade** é um dado **ordenado**, variando ao longo de um único eixo de magnitude (0° a 90°) — pede uma **paleta sequencial** (progressão de uma cor clara a escura, ou de uma cor a outra). O polígono de **unidades litológicas** é um dado **categórico**, sem relação de ordem entre as classes — pede uma **paleta qualitativa** (cores distintas, sem hierarquia, ainda que a convenção cartográfica geológica siga uma tradição de cor por período/sistema).

**(b)** Uma paleta sequencial genérica só mostra gradiente de magnitude, sem destacar o ponto de corte regulatório. A comunicação melhora com uma **paleta divergente**, centrada exatamente no limiar de **30°**, ou — mais diretamente ainda — com uma **classificação com um limite de classe fixado no valor regulatório** (30°), mesmo que isso produza classes de tamanho numérico desigual: o que importa para o leitor do mapa é a posição de cada área em relação ao limite legal de uso do solo, não uma divisão estatisticamente "equilibrada" (como quantil ou intervalo igual) da distribuição de declividades.
</details>

---

### 9. Dissertativa curta — `geologia-avancado-m13-q28` · oa04 · 10 pts

Por que a escala gráfica é preferível à escala numérica isolada num mapa técnico que será impresso e potencialmente redimensionado num relatório?

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:**

A **escala gráfica** (uma barra com subdivisões representando distâncias reais) permanece **geometricamente correta** mesmo que o mapa seja ampliado ou reduzido na reprodução, porque a barra é redimensionada **proporcionalmente** junto com o resto do mapa. A **escala numérica isolada** (por exemplo, "1:50.000") não tem essa propriedade: se o arquivo do mapa for redimensionado ao ser encaixado num relatório — uma prática comum e muitas vezes despercebida na diagramação final — o valor numérico declarado deixa de corresponder à relação real entre distância no mapa e no terreno, invalidando silenciosamente essa informação sem que nada no próprio mapa avise o leitor. Por isso um layout técnico bem-feito inclui ambas, mas trata a escala gráfica como a informação que continua confiável em qualquer cenário de reprodução.
</details>

---

## Gabarito resumido

| Questão | ID | Resposta |
|---|---|---|
| 1 | q20 | b (MDT; MDS incorporaria vegetação como relevo) |
| 2 | q21 | Falso (30 m adquirido desde 2000; o que mudou em 2014-2015 foi a liberação/distribuição) |
| 3 | q22 | 0,125 km² a 12,5 m; 0,72 km² a 30 m; mesmo limiar em células ≠ mesma área — comparação exige converter para área real |
| 4 | q23 | ver comentário (convexa = jovem/incisão ativa; côncava = madura/senil) |
| 5 | q24 | b (uma única direção, maior declividade descendente, entre 8 vizinhas) |
| 6 | q25 | Falso (lineamento é hipótese de controle estrutural, exige verificação de campo) |
| 7 | q26 | c (ET-RDG; ET-EDGV = estruturação, ET-ADGV = aquisição) |
| 8 | q27 | declividade = sequencial; litologia = qualitativa; destacar 30° com paleta divergente ou classe fixada no limiar regulatório |
| 9 | q28 | ver comentário (escala gráfica se redimensiona proporcionalmente; numérica isolada perde correção ao redimensionar) |
