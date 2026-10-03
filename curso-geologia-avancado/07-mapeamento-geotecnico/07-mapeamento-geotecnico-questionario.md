# Questionário — Módulo 07: Metodologia de mapeamento geotécnico

**Módulo:** [[07-mapeamento-geotecnico-modulo|Módulo 07 — Metodologia de mapeamento geotécnico]]
**Cobertura:** Aulas 01 a 04 — módulo completo. Questionário cumulativo único (módulo com 4 aulas, abaixo do limiar de parciais).
**Objetivos avaliados:** geologia-avancado-m07-oa01, geologia-avancado-m07-oa02, geologia-avancado-m07-oa03, geologia-avancado-m07-oa04

---

### 1. Múltipla escolha
A diferença essencial entre um mapa geológico e uma carta geotécnica está:

a) Na escala de trabalho, sempre maior na carta geotécnica
b) No critério de agrupamento das unidades — origem e idade no mapa geológico, comportamento frente ao uso na carta geotécnica
c) No uso de cores e simbologia padronizada
d) Na presença de dados de subsuperfície, ausentes no mapa geológico

<details>
<summary>Ver resposta</summary>

**Resposta: b**

O mapa geológico agrupa por origem e idade; a carta geotécnica agrupa por comportamento frente à solicitação de interesse. Os dois critérios frequentemente não coincidem: um granito são e o mesmo granito com manto de alteração espesso formam **uma** unidade geológica e **duas** unidades geotécnicas, enquanto solos residuais de litologias distintas podem convergir para uma única unidade geotécnica. A alternativa "a" confunde uma tendência com o critério definidor (Aula 01).
</details>

---

### 2. Verdadeiro ou Falso
"Uma carta geotécnica levantada em 1:50.000 pode ser ampliada para 1:5.000 e usada para decidir a implantação de uma edificação, desde que a ampliação seja feita digitalmente e sem perda de resolução gráfica."

<details>
<summary>Ver resposta</summary>

**Falso.**

A escala não é atributo de apresentação, e sim do **levantamento**: ela fixa a menor área representável e a densidade de investigação empregada. Uma carta pode ser generalizada para escala menor sem perda de validade, mas jamais ampliada — a informação de detalhe simplesmente não foi levantada. A ampliação, digital ou não, cria uma aparência de precisão que os dados não sustentam. É o mesmo erro que, em ambiente SIG, se comete ao reamostrar um raster para células menores (Aulas 01 e 04).
</details>

---

### 3. Dissertativa curta
Uma encosta muito íngreme, com colúvio espesso sobre contato basal desfavorável, situa-se numa área de mata preservada, sem qualquer ocupação e sem nada a jusante no alcance de uma eventual corrida. Classifique essa situação quanto a suscetibilidade e quanto a risco, e justifique.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:** a **suscetibilidade é alta** — a predisposição do terreno ao processo é dada por suas características físicas (declividade, material coluvionar, contato basal desfavorável), e essas características estão todas presentes. O **risco é nulo**, porque risco exige elementos expostos e vulneráveis: sem ocupação e sem nada a jusante no alcance, não há o que perder, e Risco = Perigo × Exposição × Vulnerabilidade se anula quando a exposição é zero (Aula 03).

**Comentário:** este é o caso que torna a distinção operacional, e não terminológica. A área não é candidata a obra de contenção nem a remoção — não há ninguém a remover —, mas **é** candidata prioritária a restrição de uso no zoneamento, justamente para que o risco permaneça nulo. Suscetibilidade orienta planejamento; risco orienta intervenção sobre situações concretas com pessoas dentro.
</details>

---

### 4. Múltipla escolha
Uma carta clinográfica derivada de MDE SRTM de 30 m indica declividade de 28% num trecho de encosta. Em relação ao limiar de 30% da Lei 6.766/1979, pode-se afirmar que:

a) O trecho está abaixo do limiar, e o parcelamento não encontra essa restrição
b) O trecho está acima do limiar, pois o SRTM superestima declividades
c) Não é possível concluir, pois o SRTM subestima sistematicamente as declividades altas
d) A questão é irrelevante, pois a Lei 6.766/1979 não trata de declividade

<details>
<summary>Ver resposta</summary>

**Resposta: c**

Um MDE grosseiro promedia a elevação em células maiores, suavizando o relevo e **subestimando sistematicamente** as declividades altas. O erro não é aleatório — não ocorre para mais e para menos com igual probabilidade em encosta íngreme —, e sua magnitude pode facilmente exceder os 2 pontos percentuais que separam 28% de 30%. Com esse dado, portanto, não se pode afirmar que o trecho está abaixo do limiar. A conclusão exige MDE de resolução compatível com a escala da carta (Aula 02).
</details>

---

### 5. Aplicação (cálculo)
Numa encosta de 25° de inclinação há 2 m de colúvio com γsat = 19 kN/m³, c' = 5 kPa e φ' = 30°, sobre contato basal paralelo à superfície. Calcule o fator de segurança pelo modelo de talude infinito na condição saturada, com fluxo paralelo à encosta e nível d'água na superfície. Use γw = 9,81 kN/m³. (cos 25° = 0,9063; sen 25° = 0,4226)

<details>
<summary>Ver resolução</summary>

cos²25° = 0,8214.

**Força motriz:** γ·z·sen β·cos β = 19 × 2 × 0,4226 × 0,9063 = 38 × 0,3830 = **14,55 kPa**

**Tensão normal total:** γ·z·cos²β = 38 × 0,8214 = **31,21 kPa**

**Poropressão** (fluxo paralelo à encosta, NA na superfície): u = γw·z·cos²β = 9,81 × 2 × 0,8214 = **16,12 kPa**

**Tensão normal efetiva:** σ'n = 31,21 − 16,12 = **15,09 kPa**

**Resistência:** τf = c' + σ'n·tan φ' = 5 + (15,09 × 0,5774) = 5 + 8,72 = **13,72 kPa**

**FS = 13,72 / 14,55 = 0,94**

FS < 1 → a condição saturada é instável. Para comparação, o mesmo talude seco (u = 0) teria resistência de 5 + 18,02 = 23,02 kPa e FS = 1,58. A saturação, sem adicionar peso relevante, derruba o FS de 1,58 para 0,94 — exatamente o mecanismo de escorregamento deflagrado por chuva do Módulo 06, Aula 03 (Aula 03).
</details>

---

### 6. Verdadeiro ou Falso
"Numa carta de suscetibilidade produzida por sobreposição ponderada, uma cicatriz de escorregamento ativa deve ser incluída como mais um fator condicionante, com peso proporcional à sua importância."

<details>
<summary>Ver resposta</summary>

**Falso.**

Uma cicatriz ativa não é fator de **predisposição** — é evidência direta de que o processo **ocorre** naquele local. Incluí-la como parcela de uma soma ponderada a submeteria ao caráter **compensatório** do método: com um peso qualquer, valores baixos nos demais fatores poderiam diluí-la e a célula sairia em classe média. O tratamento correto é uma **regra restritiva aplicada após a agregação**, reclassificando diretamente para a classe máxima de suscetibilidade toda célula com cicatriz ativa e sua zona de influência. A mesma lógica de veto vale para fatores eliminatórios legais (APP) e físicos (cavidade) (Aula 04).
</details>

---

### 7. Aplicação (cálculo e crítica)
Uma sobreposição ponderada usa declividade (peso 0,50), material (0,30) e forma de vertente (0,20), com fatores reclassificados de 1 a 5. Calcule o índice das células A (declividade 5, material 2, forma 2) e B (declividade 3, material 4, forma 4), e comente o resultado.

<details>
<summary>Ver resolução</summary>

**Célula A:** (0,50 × 5) + (0,30 × 2) + (0,20 × 2) = 2,50 + 0,60 + 0,40 = **3,50**

**Célula B:** (0,50 × 3) + (0,30 × 4) + (0,20 × 4) = 1,50 + 1,20 + 0,80 = **3,50**

**Comentário:** as duas células recebem índice **idêntico** e cairão na mesma classe, apesar de descreverem situações fisicamente distintas — A é uma encosta muito íngreme em material e forma favoráveis, B é uma vertente moderada em material desfavorável e forma côncava (que concentra fluxo). Isso é a **compensação** inerente à soma ponderada: o valor extremo de um fator é diluído pelos valores baixos dos demais.

A conclusão metodológica não é que o método esteja errado, mas que ele produz um **ordenamento** do território para priorizar investigação, e não um **diagnóstico** do mecanismo de cada célula. Por isso a carta de suscetibilidade deve sempre ser apresentada acompanhada das cartas básicas, permitindo recuperar *por que* uma célula caiu naquela classe (Aula 04).
</details>

---

### 8. Múltipla escolha
Para detectar movimento lento e contínuo de um talude urbano ao longo de vários anos, o produto de sensoriamento remoto mais adequado é:

a) Imagem óptica Landsat, pela série temporal longa e gratuita
b) LiDAR aerotransportado, pela resolução submétrica
c) Interferometria SAR (InSAR) por série temporal
d) Fotogrametria por VANT, pelo detalhe de feições

<details>
<summary>Ver resposta</summary>

**Resposta: c**

O InSAR mede **deslocamento de superfície** em escala milimétrica a centimétrica ao longo do tempo, sendo o único dos quatro que quantifica movimento acumulado — e funciona bem em área urbana, onde há alvos estáveis. As demais opções mapeiam **geometria** num instante: LiDAR e VANT com excelente detalhe, Landsat com série longa mas resolução insuficiente para movimento lento. Comparar dois levantamentos LiDAR detectaria deslocamento decimétrico ou maior, não milimétrico. Limitação a registrar do InSAR: mede apenas a componente na linha de visada do satélite, e perde coerência em vegetação densa e em movimento rápido (Aula 04).
</details>

---

### 9. Dissertativa curta
Uma carta de aptidão classifica uma gleba como "apta com restrição". Explique por que essa informação, isolada, é insuficiente, e o que a legenda precisaria conter para tornar a carta útil ao gestor.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:** a classe indica que a ocupação é possível mediante exigências, mas não diz **quais** — e sem isso o gestor não sabe se deve exigir projeto de drenagem, contenção, limitação de corte e aterro, densidade máxima ou investigação geotécnica prévia. A legenda precisa associar a cada classe o **fator limitante** que a determinou e a **medida requerida** para superá-lo. Sem isso, a carta gradua sem orientar ação, e a classificação torna-se ainda inauditável, já que não há como verificar por que aquela gleba recebeu aquela classe (Aula 03, com o princípio geral da Aula 01).

**Comentário:** essa exigência é a versão prática do princípio estabelecido na Aula 01 — a carta geotécnica é interpretativa por construção, e por isso o critério de classificação precisa estar explícito na legenda e no memorial. Uma carta sem critério declarado não pode ser revista nem contestada, só refeita.
</details>

---

### 10. Múltipla escolha
Duas camadas vetoriais, uma em SAD-69 e outra em SIRGAS 2000, são sobrepostas num SIG sem qualquer conversão. A consequência esperada é:

a) Nenhuma, pois o SIG reprojeta automaticamente ao sobrepor
b) Deslocamento entre as camadas, podendo alcançar dezenas ou centenas de metros
c) Perda de atributos das feições
d) Erro de topologia nos polígonos

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Datums geodésicos distintos posicionam as mesmas coordenadas em pontos diferentes do terreno, e o deslocamento resultante pode chegar a dezenas ou centenas de metros — o suficiente para colocar uma edificação no polígono errado de uma carta de risco. A conversão exige **transformação de datum**, não mera mudança de rótulo do sistema. No Brasil, todas as camadas devem ser levadas ao SIRGAS 2000, o sistema de referência geodésico oficial, de adoção obrigatória desde 2015. A alternativa "a" descreve um comportamento que alguns softwares oferecem *se configurados para tal*, e cuja suposição acrítica é uma fonte frequente de erro (Aula 04).
</details>

---

### 11. Dissertativa curta
Um município tem uma excelente carta de risco, tecnicamente irretocável, produzida há cinco anos e nunca incorporada ao plano diretor. Avalie a afirmação: "o município reduziu seu risco geológico-geotécnico ao produzir a carta".

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:** a afirmação é falsa. A carta é **diagnóstico**, não intervenção — ela identifica onde o risco está, e a redução efetiva depende de decisão política, recurso, capacidade institucional e continuidade. Uma carta arquivada não alterou nem o perigo, nem a exposição, nem a vulnerabilidade, que são os três fatores do risco. Pior: se a ocupação avançou sobre áreas classificadas como inaptas nesses cinco anos, o risco **aumentou** apesar da existência da carta. O indicador de efetividade não é a qualidade do mapa, e sim a evolução da ocupação nas áreas que ele classificou como inaptas (Aula 04).

**Comentário:** a resposta completa menciona os canais pelos quais a carta produziria efeito — plano diretor e lei de uso e ocupação, licenciamento e aprovação de parcelamento, plano de contingência da defesa civil, e integração a limiares pluviométricos para alerta. É a diferença entre produzir conhecimento e produzir consequência.
</details>

---

### 12. Verdadeiro ou Falso
"Uma carta de suscetibilidade validada com AUC de 0,88 sobre o mesmo inventário de cicatrizes usado para calibrar o modelo demonstra boa capacidade preditiva."

<details>
<summary>Ver resposta</summary>

**Falso.**

Validar sobre o mesmo inventário do ajuste produz a **curva de sucesso**, que mede o quanto o modelo se ajustou aos dados — não o quanto ele prevê. A capacidade preditiva só é demonstrada pela **curva de predição**, calculada sobre um inventário **independente**, tipicamente uma partição temporal (eventos posteriores) ou espacial. Um AUC alto sobre o próprio conjunto de calibração é compatível inclusive com sobreajuste. Registre-se ainda que o limiar de ~0,8 como "bom" é uma convenção de interpretação, não um critério estatístico de aprovação (Aula 03).
</details>

---

### 13. Aplicação (síntese)
Uma prefeitura dispõe de recurso limitado para reduzir o risco de escorregamento num assentamento consolidado em encosta, classificado em setorização como R3 (risco alto). Liste as quatro alavancas de redução de risco disponíveis, com um exemplo de medida para cada, e comente por que a leitura estritamente geotécnica tende a enxergar apenas uma delas.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada** — de Risco = Perigo × Exposição × Vulnerabilidade decorrem quatro alavancas:

1. **Reduzir o perigo:** obras de contenção, drenagem superficial e profunda, estabilização e retaludamento.
2. **Reduzir a exposição:** remoção das moradias dos setores mais críticos, restrição de uso, e impedimento de novas ocupações (que é a medida de menor custo e maior efeito de longo prazo).
3. **Reduzir a vulnerabilidade:** melhoria construtiva das edificações, regularização, eliminação de lançamento de água servida em talude, capacitação da comunidade e plano de evacuação.
4. **Reduzir a consequência residual:** sistema de alerta antecipado por limiar pluviométrico, plano de contingência, rotas de fuga e pontos de apoio definidos.

**Por que a leitura geotécnica enxerga só a primeira:** porque a formação e o instrumental do geólogo e do engenheiro geotécnico atuam sobre o mecanismo físico do processo, que é o fator "perigo". As outras três são de natureza urbanística, social e institucional. Ocorre que a obra é usualmente a alavanca **mais cara** e nem sempre a mais eficaz por unidade de recurso investido — e, se não houver manutenção permanente, devolve o risco ao patamar anterior, agora com a agravante de uma ocupação consolidada pela falsa sensação de segurança que a obra criou (Aula 04).

**Comentário:** a resposta correta não é escolher uma alavanca, e sim reconhecer que a decisão é de composição e depende de custo, prazo e capacidade institucional — uma decisão de política pública informada pela geotecnia, não determinada por ela.
</details>

---

### 14. Dissertativa curta
Explique por que a cartografia geotécnica separa cartas básicas de cartas derivadas, em vez de produzir diretamente a carta interpretativa final.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:** por **rastreabilidade**. As cartas básicas registram um atributo cada, o mais próximo possível do dado observado; as derivadas as combinam segundo um modelo de comportamento. Se a classificação de uma área for questionada — por um proprietário, por um órgão de controle, ou por uma revisão técnica —, é preciso poder voltar às camadas de origem e verificar **qual atributo** determinou aquela classe. Uma carta interpretativa produzida sem cartas básicas rastreáveis não pode ser revista; só refeita do zero (Aula 02).

**Comentário:** o mesmo princípio reaparece na Aula 04 aplicado ao SIG, onde a carta derivada deve ser resultado de uma operação **declarada e reexecutável** — de modo que a entrada de uma sondagem nova ou a mudança de um peso permita refazer a análise e comparar, em vez de recomeçar. Rastreabilidade e reexecutabilidade são a mesma exigência em dois níveis: dos dados e do procedimento.
</details>

---

### Gabarito resumido

| Questão | Resposta |
|---|---|
| 1 | b |
| 2 | Falso |
| 3 | Suscetibilidade alta, risco nulo (sem exposição) |
| 4 | c |
| 5 | FS = 0,94 (instável) |
| 6 | Falso |
| 7 | Ambas 3,50 — ver comentário sobre compensação |
| 8 | c |
| 9 | ver comentário (nomear fator limitante e medida requerida) |
| 10 | b |
| 11 | Falso — ver comentário |
| 12 | Falso |
| 13 | ver comentário (quatro alavancas) |
| 14 | ver comentário (rastreabilidade) |
