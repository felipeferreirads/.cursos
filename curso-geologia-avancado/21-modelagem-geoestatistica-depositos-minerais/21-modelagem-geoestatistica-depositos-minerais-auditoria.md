# Auditoria científica — Módulo 21: Modelagem geoestatística de depósitos minerais

**Data do levantamento:** 2026-09-18 · **Correções aplicadas em:** 2026-09-18
**Modo:** `audit-and-fix` · **Profundidade:** `full`
**Escopo:** as 5 aulas do módulo, auditadas em conjunto, mais o hub do módulo

> **Nota posterior, acrescentada em 2026-09-19 pela revisão didática — nenhum achado deste relatório foi alterado, reaberto ou renumerado.**
> A revisão didática dividiu a **Aula 03** (achado `DID-M21-A03-CARGA-001`), e o módulo passou de 5 para 6 aulas. Onde este relatório diz:
> · **a03** → hoje é o **par a03 + a04**. Ficaram na **nova a03**: variograma experimental indicador, modelos autorizados × não autorizados (com a separação dos dois sintomas do 🔴 1) e mediana indicadora × *full IK* (🟠 5). Ficaram na **nova a04**: sistema de krigagem indicadora (🟠 8, SIK × OIK), violações de relação de ordem e o exemplo trabalhado aritmético (🟠 6 e 🟠 7).
> · **a04** (krigagem log-normal, achados ⚪ 9, 🟡 11, 🟡 13, 🟡 14) → hoje é a **a05**.
> · **a05** (wireframes, achado 🟠 4) → hoje é a **a06**.
> Os `claim_id` **não** foram renumerados: os prefixos `A03`, `A04` e `A05` designam a numeração em que cada alegação foi emitida. Ver `21-modelagem-geoestatistica-depositos-minerais-revisao-didatica.md`.
**Veredito:** **aprovado — gate liberado.** 0 achados vermelhos e 0 laranjas em aberto; os 15 achados corrigíveis (1 vermelho, 7 laranjas, 7 amarelos) foram corrigidos cirurgicamente, e o único achado branco foi tratado com reescrita que expõe as duas posições da literatura. **Questionário e flashcards liberados**, observadas as restrições ao fim deste relatório.

> **Segunda passagem — 2026-09-19 (pós-divisão didática).** Dois pontos encaminhados pela revisão didática foram auditados e resolvidos, acrescentando **1 achado vermelho (🔴 16)** e **1 amarelo (🟡 17)** a este relatório, ambos **corrigidos na mesma passagem**. O total do módulo passa a **17 achados numerados**. O gate **continua liberado** (0 vermelhos e 0 laranjas em aberto). Ver **"Correções pós-divisão"** ao fim. Um registro azul da primeira passagem (**B12**) foi **superado** pelo 🔴 16 — não foi apagado nem renumerado.

## Contagem por severidade

| Severidade | Contagem | Situação |
|---|---|---|
| 🔴 Vermelho (afirmação factualmente falsa) | **1** | **corrigido** |
| 🟠 Laranja (impreciso, inconsistência interna, certeza indevida, omissão que gera erro) | **7** | **corrigidos** |
| 🟡 Amarelo (atribuição de fonte errada, valor apresentado incorretamente) | **7** | **corrigidos** |
| 🔵 Azul (verificado e correto — registro de que foi checado) | **19** | sem alteração (são registros de verificação bem-sucedida) |
| ⚪ Branco (questão aberta na literatura) | **1** | **tratado** — texto reescrito mostrando as posições; não bloqueia o gate |

> **Nota sobre as contagens:** os números da coluna "Contagem" são os do levantamento original e não mudam — um achado não se apaga ao ser corrigido, ele muda de situação.

**Alegações rastreadas:** as 24 `alegacoes_auditaveis` declaradas pelas aulas (5 na a01, 5 na a02, 7 na a03, 5 na a04, 5 na a05) foram verificadas uma a uma; a auditoria levantou mais 3, chegando a **27 alegações rastreadas**. As 3 novas foram gravadas nos blocos de metadados das aulas: `GEOMOD-M21-A02-OKSEMHIPOTESEDISTRIBUCIONAL-006`, `GEOMOD-M21-A03-PATAMARF-008`, `GEOMOD-M21-A03-SIKVSOIK-009`.

**Exemplos trabalhados:** os cinco foram examinados; **dois pedem aritmética (a03 e a04) e os dois foram refeitos número por número**. O da a04 fecha em todos os passos (só o percentual de comparação estava sobre a base errada — 🟡 14). O da a03 **não fechava como impresso**: a razão de pesos exibida não decorre dos valores de variograma exibidos, e o patamar declarado contradizia o $F(z_c)$ declarado ao lado dele (🟠 6 e 🟠 7). Os três exemplos não numéricos (a01 validação de base, a02 tabela de indicadoras, a05 bissetriz e circuncírculo) foram conferidos e estão corretos.

---

## Padrão dominante

**A ATRIBUIÇÃO CAUSAL ERRADA — um sintoma verdadeiro ligado à causa errada.** Este módulo repete a assinatura diagnosticada no M20 ("a versão mnemônica de uma afirmação certa"), mas num registro novo: aqui não é a definição que está trocada, é a **seta de causalidade**. Os três achados mais caros do módulo têm exatamente essa forma:

1. **"Probabilidade fora de [0,1] é sintoma de variograma não autorizado"** (🔴 1). É a versão que circula. Não é verdade: a causa dominante são os **pesos negativos** do efeito de tela, que ocorrem com modelos perfeitamente autorizados. O que aponta especificamente para modelo não autorizado é a **variância de krigagem negativa** — e só ela. A aula ensinava um procedimento de diagnóstico que manda o aluno olhar para o lugar errado.
2. **"A krigagem ordinária depende implicitamente de a distribuição não ser assimétrica"** (🟠 2). Não depende: a dedução do sistema não assume distribuição alguma. O que a assimetria ataca é **robustez** e **otimalidade**, não a validade.
3. **"Delaunay maximiza o menor ângulo de cada triângulo"** (🟠 4). O teorema é sobre a **triangulação inteira**, não triângulo a triângulo — a diferença some numa leitura rápida e reaparece na hora de justificar por que a malha é boa.

Os três compartilham a propriedade que os torna caros: a versão errada é mais simples de enunciar, e por isso é a que sobrevive. Num questionário, os três são distratores perfeitos — ver `avisos ao gerador` ao fim.

**O segundo padrão é o velho conhecido: atribuição de fonte.** Os 7 amarelos são todos disso, **quinta reincidência consecutiva** (4 no M17, 6 no M18, 7 no M19, 8 no M20, 7 aqui). E desta vez o defeito é sistemático de um jeito novo: **as citações de capítulo do Isaaks & Srivastava e do Goovaerts estão deslocadas de uma unidade**, de forma consistente, em todas as cinco aulas — o que sugere que o gerador está inferindo o número do capítulo em vez de conferi-lo. A verificação recomendada nas auditorias do M18, M19 e M20 continua sem ser implementada.

---

## Achados

### 🔴 1. Estimativa de probabilidade fora de [0,1] atribuída a variograma não autorizado

**claim_id:** `GEOMOD-M21-A03-SINTOMAMODELONAOAUTORIZADO-003`
**Tipo:** erro factual (atribuição causal falsa)
**Onde:** a03 · seção "Modelos autorizados versus não autorizados"; propagado para o Recap relâmpago e para o próprio bloco de alegações auditáveis
**Está escrito:** "o sistema de krigagem pode produzir **variâncias de krigagem negativas** (um absurdo matemático, já que variância nunca é negativa) ou, o problema mais visível no resultado final, **estimativas de probabilidade fora do intervalo $[0,1]$** — uma probabilidade estimada de $-0{,}03$ ou $1{,}12$ não tem interpretação possível, e é sintoma direto de um variograma mal ajustado, não de um erro de cálculo do sistema em si."
**Problema:** a primeira metade está certa e a segunda inverte a causa. **Variância de krigagem negativa** é, de fato, o sintoma de um modelo não autorizado (não condicionalmente definido positivo) — nesse ponto a aula acerta. Mas **estimativas de indicadora fora de $[0,1]$ não são diagnóstico de modelo não autorizado**: elas aparecem rotineiramente com modelos esféricos, exponenciais e gaussianos perfeitamente autorizados. A causa dominante é banal e bem documentada: a krigagem atribui **pesos negativos** a amostras escondidas atrás de amostras mais próximas — o efeito de tela já visto no M20 —, e um peso negativo aplicado a um dado que só vale 0 ou 1 empurra a soma ponderada para fora do intervalo. As outras causas listadas na literatura são da mesma natureza prática: variogramas incompatíveis entre limiares, plano de krigagem mal dimensionado e escassez de dados informativos nos limiares extremos. Nenhuma delas é "variograma não autorizado".
**Por que é vermelho e não laranja:** não é um exagero de grau, é uma **instrução de diagnóstico invertida**. Um aluno que encontrasse $1{,}12$ numa krigagem indicadora sairia desta aula convencido de que precisa refazer o ajuste do variograma, quando o que precisa examinar é a configuração de vizinhança e os pesos. E é matéria de primeira linha para questionário: "o que causa probabilidade fora de [0,1] na IK?" é exatamente o tipo de item que um gerador produziria, e o gabarito sairia errado.
**Correção aplicada:** o parágrafo foi partido em dois. O primeiro mantém a variância negativa como o sintoma específico do modelo não autorizado; o segundo, novo, separa explicitamente o outro sintoma, nomeia os pesos negativos como causa dominante, lista as demais causas e fecha com a regra de diagnóstico ("variância negativa aponta para o modelo; probabilidade fora de [0,1] aponta para os pesos e para a vizinhança"), remetendo ao tratamento de relação de ordem mais adiante na própria aula. O Recap e a alegação auditável foram realinhados; a alegação carrega nota de revisão datada.
**Fonte:** C. V. Deutsch, *An Overview of Multiple Indicator Kriging*, Geostatistics Lessons ("negative probabilities or probabilities greater than 1 may appear because of the weights applied by the kriging or if the variograms for each threshold are not compatible") · Mizuno & Deutsch, *Sequential Indicator Simulation*, Geostatistics Lessons ("kriging can lead to negative weights applied to data screened behind closer samples… this could lead to negative indicator estimates") · Datamine Studio RM, documentação de *Grade Estimation Kriging* · Journel & Huijbregts (1978), *Mining Geostatistics*, caps. II–III (variância negativa e modelo não autorizado) · **Nível:** referência de implementação / tratado de referência · consultado em 2026-09-18
**Confiança:** confirmado
**Também aparece em:** nenhum outro arquivo do curso — verificado contra o M20 (pré-requisito declarado) e contra o M42, que ainda não tem aulas escritas.
**Desfecho:** **corrigido**

---

### 🟠 2. Krigagem ordinária descrita como dependente de a distribuição não ser assimétrica

**claim_id:** `GEOMOD-M21-A02-OKSEMHIPOTESEDISTRIBUCIONAL-006` (alegação nova)
**Tipo:** certeza indevida / confusão de escopo
**Onde:** a02 · linha "Ao final você vai conseguir" e seção "O limite da krigagem ordinária de teores brutos"; propagado para o Recap
**Está escrito:** "a krigagem ordinária é um estimador que minimiza variância do erro assumindo, implicitamente, que a relação entre valores vizinhos é bem descrita por uma estrutura de covariância única (o variograma) — o que funciona bem quando a distribuição da variável é razoavelmente simétrica e sem caudas extremas" (e, no objetivo, "depende implicitamente de a distribuição não ser demasiado assimétrica").
**Problema:** a dedução do sistema de krigagem **não faz nenhuma hipótese distribucional**. Sob estacionariedade, a krigagem ordinária é o melhor estimador *linear* não viesado qualquer que seja a forma da distribuição; normalidade nunca foi requisito. Dizer que ela "depende" de simetria transforma uma perda de desempenho em uma condição de validade — e é justamente a confusão que a aula precisaria desfazer, não reforçar, porque ela é a porta de entrada para o mal-entendido de que "é preciso normalizar antes de krigar". O que a assimetria de fato compromete são duas coisas distintas e ambas nomeáveis: a **robustez** (variograma experimental e estimativa ficam sensíveis a poucos valores muito altos) e a **otimalidade** (um estimador linear só coincide com a esperança condicional sob a hipótese multigaussiana — e é aí que mora o ganho potencial dos métodos não lineares, que é o assunto do módulo).
**Correção aplicada:** primeira frase da seção reescrita, nomeando explicitamente as duas frentes e marcando que a KO não assume distribuição. O restante do parágrafo (assimetria de depósitos, variograma dominado pela cauda) foi preservado intacto, porque estava certo. Objetivo e Recap realinhados. Alegação nova criada.
**Fonte:** Chilès & Delfiner (2012), *Geostatistics: Modeling Spatial Uncertainty*, 2ª ed., Wiley · consenso da literatura, resumido em discussões técnicas sobre requisitos da krigagem: "the derivation of the kriging equations does not depend on any distribution assumptions… normality is not a requirement for kriging", e "if the random function is multivariate Gaussian then the simple kriging estimator is the same as the conditional expectation" · **Nível:** tratado de referência
**Confiança:** confirmado
**Desfecho:** **corrigido**

---

### 🟠 3. "Balanced tangential" agrupado com o método tangencial cru

**claim_id:** `GEOMOD-M21-A01-DESURVEY-001`
**Tipo:** impreciso (dois métodos distintos tratados como um)
**Onde:** a01 · seção "As tabelas de uma base de dados de furos de sonda"
**Está escrito:** "(o método do segmento reto, *balanced tangential* ou mais simples ainda, subestima sistematicamente a curvatura real do furo)"
**Problema:** o parêntese junta num mesmo balde dois métodos cuja diferença de exatidão é justamente o ponto. O **tangencial simples** (*tangential*) assume que o furo mantém a direção da última estação medida até a estação seguinte, o que produz saltos bruscos de direção e os maiores erros de toda a família — a literatura de perfuração direcional recomenda abandoná-lo. O **tangencial balanceado** (*balanced tangential*) faz o oposto: pondera igualmente as direções das duas estações e **alcança exatidão comparável à da mínima curvatura**. Colocá-lo do lado errado ensina a descartar um método que é aceitável. A formulação "subestima sistematicamente a curvatura" também não é a caracterização usual do erro do método tangencial, que é um desvio de posição na direção da estação inferior.
**Correção aplicada:** parêntese substituído por duas frases que separam os dois métodos, com a caracterização correta de cada um. A alegação `-001` foi reescrita e carrega nota de revisão. Acrescentada a PetroWiki às Fontes da aula.
**Fonte:** PetroWiki (SPE), *Calculation methods for directional survey* ("the five most commonly used methods are: tangential, balanced tangential, average angle, curvature radius, and minimum curvature (most accurate)"; "large errors are seen in the tangential method… the tangential method is inaccurate and should be abandoned completely"; "the balanced-tangential method gives accuracy comparable to the minimum-curvature method") · Seequent, *Borehole Desurveying Options* · **Nível:** referência técnica de indústria · consultado em 2026-09-18
**Confiança:** confirmado
**Desfecho:** **corrigido**

---

### 🟠 4. Delaunay descrita como maximizando o menor ângulo de cada triângulo

**claim_id:** `GEOMOD-M21-A05-CIRCUNCIRCULOVAZIO-003`
**Tipo:** impreciso (enunciado de teorema deslocado de escopo) + omissão que gera erro
**Onde:** a05 · seção "Triangulação de Delaunay: a estrutura por trás do polígono"; propagado para o Recap
**Está escrito:** "a triangulação de Delaunay é a que **maximiza o menor ângulo** de cada triângulo" e, antes, "a propriedade matemática que define — e caracteriza unicamente — a triangulação de Delaunay".
**Problema:** dois pontos. (a) O teorema é **sobre a triangulação, não sobre cada triângulo**: entre todas as triangulações do mesmo conjunto, a de Delaunay é a que maximiza o **menor ângulo da malha inteira** (e, no enunciado forte, é a que maximiza lexicograficamente o vetor de todos os ângulos ordenados do mais agudo ao menos agudo). Não é verdade que cada triângulo individual tenha, na triangulação de Delaunay, o melhor ângulo mínimo que ele poderia ter. (b) "Caracteriza unicamente" omite a condição de **posição geral**: a triangulação de Delaunay é única só quando não há quatro pontos cocirculares — e quatro pontos cocirculares é exatamente o que acontece numa malha de sondagem quadrada regular, que é o caso mais comum do domínio desta aula. A omissão importa porque o exemplo trabalhado da própria aula argumenta a partir da unicidade.
**Correção aplicada:** o enunciado foi corrigido para "menor ângulo da triangulação", com o enunciado lexicográfico entre parênteses e uma frase explícita sobre o que a propriedade **não** diz. Acrescentado o parágrafo sobre posição geral e o caso cocircular, com o gancho da malha de sondagem quadrada. Recap e alegação `-003` realinhados; Fontes agora citam também o cap. 7 (Voronoi) de de Berg et al.
**Fonte:** de Berg, Cheong, van Kreveld & Overmars (2008), *Computational Geometry: Algorithms and Applications*, 3ª ed., cap. 9 · notas de curso CMSC 754 (Univ. of Maryland), *Delaunay Triangulations* ("among all the triangulations of a point set, a Delaunay triangulation maximizes the minimum angle in the triangulation") · Shewchuk, *Two-dimensional Delaunay triangulations*, cap. 2 (maximização lexicográfica do vetor de ângulos) · **Nível:** tratado de referência / teorema clássico · consultado em 2026-09-18
**Confiança:** confirmado
**Desfecho:** **corrigido**

---

### 🟠 5. Mediana indicadora: omitido que os pesos não dependem do limiar

**claim_id:** `GEOMOD-M21-A03-MEDIANAINDICADORA-004`
**Tipo:** omissão que gera erro
**Onde:** a03 · seção "Duas abordagens: mediana indicadora versus krigagem indicadora completa"; propagado para a seção "Violações de relação de ordem" e para o Recap
**Está escrito:** "Esse variograma único, reescalado ao patamar apropriado de cada limiar, é então usado no sistema de krigagem para todos os cortes. A vantagem é o custo de modelagem muito menor (um variograma, não vários)" — e, mais adiante, "mesmo na abordagem da mediana indicadora, o sistema é resolvido limiar a limiar".
**Problema:** a aula descreve a economia de modelagem e perde a economia que é o próprio motivo de a técnica existir. Como o patamar entra no sistema de krigagem apenas como fator de escala comum aos dois lados das equações, **os pesos de krigagem deixam de depender do limiar**: resolve-se **um único sistema por bloco** e os mesmos $\lambda_i$ são reaproveitados em todos os cortes, mudando só os dados 0/1 que eles ponderam. A frase "o sistema é resolvido limiar a limiar" diz o contrário disso e é a parte que gera erro: um aluno sai achando que a mediana indicadora economiza só o ajuste de variograma, quando ela reduz também o custo computacional da estimativa em um fator igual ao número de limiares. Também é a informação que torna a técnica reconhecível numa prova.
**Correção aplicada:** acrescentada a consequência (pesos independentes do limiar; um sistema por bloco) na seção da mediana indicadora, com a razão pela qual isso ocorre; corrigida a frase da seção de relação de ordem para "os pesos são os mesmos para todos os cortes, a estimativa muda porque os dados de entrada mudam"; Recap e alegação `-004` realinhados. Acrescentada a lição de Deutsch às Fontes.
**Fonte:** C. V. Deutsch, *An Overview of Multiple Indicator Kriging*, Geostatistics Lessons ("this so-called Median IK approach is very fast, since the kriging weights do not depend on the cut-off being considered"; "necessitates the solution of only one kriging system per block") · Geovariances, *Recoverable resources estimation: Indicator Kriging or Uniform Conditioning?* · **Nível:** referência de implementação · consultado em 2026-09-18
**Confiança:** confirmado
**Desfecho:** **corrigido**

---

### 🟠 6. Inconsistência interna no exemplo da a03: patamar 0,22 declarado como F(1−F) com F ≈ 0,30

**claim_id:** `GEOMOD-M21-A03-PATAMARF-008` (alegação nova)
**Tipo:** inconsistência interna
**Onde:** a03 · Exemplo trabalhado, enunciado
**Está escrito:** "patamar $C=0{,}22$ (a variância máxima teórica da indicadora nesse limiar, $F(z_c)[1-F(z_c)]$, com $F(z_c)\approx 0{,}30$)"
**Problema:** dois defeitos numa frase. (a) $0{,}30 \times 0{,}70 = 0{,}21$, não $0{,}22$. Para que $F(1-F)=0{,}22$ seria preciso $F \approx 0{,}327$ (ou o complementar, $0{,}673$). O enunciado do exemplo contradiz a si mesmo em duas casas decimais, e é justamente o tipo de detalhe que um aluno atento refaz. (b) "variância **máxima teórica** da indicadora nesse limiar" está incorreto: $F(1-F)$ **é** a variância naquele limiar, não um máximo — o máximo, $0{,}25$, ocorre só no limiar da mediana, e a própria aula usa esse fato duas seções antes para justificar a escolha da mediana como variograma de referência. Chamar $0{,}22$ de máximo desfaz o argumento.
**Correção aplicada:** $F(z_c)\approx 0{,}30$ passou a $F(z_c)\approx 0{,}33$ (edição mínima, que preserva todos os valores de variograma e toda a aritmética subsequente); removido o qualificador "máxima teórica". Alegação nova criada, registrando a variância da Bernoulli e o valor de máximo.
**Fonte:** variância de uma variável de Bernoulli, $p(1-p)$; conferido por cálculo direto na auditoria · **Nível:** resultado padrão de probabilidade
**Confiança:** confirmado
**Desfecho:** **corrigido**

---

### 🟠 7. Aritmética do exemplo da a03 não reproduzível a partir dos números impressos

**claim_id:** `GEOMOD-M21-A03-EXEMPLONUMERICO-007`
**Tipo:** inconsistência interna (exemplo trabalhado)
**Onde:** a03 · Exemplo trabalhado, resolução
**Está escrito:** "$\gamma_I(25)=0{,}100$; $\gamma_I(35)=0{,}135$; $\gamma_I(50)=0{,}179$… Subtraindo a primeira da segunda: $0{,}135\lambda_1 - 0{,}135\lambda_2 = 0{,}079 \implies \lambda_1-\lambda_2 \approx 0{,}589$. Combinando com $\lambda_1+\lambda_2=1$: $\lambda_1 \approx 0{,}795$ e $\lambda_2 \approx 0{,}205$."
**Problema:** o passo não fecha. Com os valores de variograma **como impressos**, $0{,}079 / 0{,}135 = 0{,}585$, não $0{,}589$ — e daí $\lambda_1 = 0{,}793$, não $0{,}795$. O resultado final $0{,}795$ está certo, mas só contra os valores **exatos** do modelo esférico ($\gamma(25)=0{,}099768$, $\gamma(35)=0{,}135164$, $\gamma(50)=0{,}179395$), que o texto não mostra. Ou seja: o aluno que refizer a conta com os números que a aula lhe deu chega a um resultado diferente do que a aula afirma, sem ter como saber qual está certo. Isso é pior do que um erro de resultado, porque destrói a confiança no exemplo inteiro — e este é um dos dois exemplos numéricos do módulo.
**Correção aplicada:** os valores de variograma passaram a quatro casas ($0{,}0998$; $0{,}1352$; $0{,}1794$), que é a precisão mínima que faz a cadeia fechar: $0{,}0796/0{,}1352 = 0{,}589$, $\lambda_1 = 0{,}794$, $\lambda_2 = 0{,}206$, $\mu = 0{,}072$, $i^*(x_0) = 0{,}794$. Todas as ocorrências subsequentes ($79{,}5\%$ → $79{,}4\%$; $20{,}5\%$ → $20{,}6\%$; o peso citado na leitura do resultado) foram propagadas. Alegação `-007` reescrita com os valores exatos registrados.
**Fonte:** cálculo direto refeito na auditoria a partir de $\gamma(h)=C[1{,}5(h/a)-0{,}5(h/a)^3]$ com $C=0{,}22$, $a=80$ · **Nível:** verificação aritmética
**Confiança:** confirmado
**Desfecho:** **corrigido**

---

### 🟠 8. "A OIK é preferida na prática" apresentado como consenso

**claim_id:** `GEOMOD-M21-A03-SIKVSOIK-009` (alegação nova)
**Tipo:** certeza indevida
**Onde:** a03 · seção "O sistema de krigagem indicadora"
**Está escrito:** "A OIK é preferida na prática pela mesma razão que a krigagem ordinária de teores é preferida à simples: não exige assumir conhecida, a priori, uma proporção global única válida em toda a área, o que raramente é realista quando o depósito tem domínios geológicos distintos."
**Problema:** a justificativa dada está certa, a conclusão não se sustenta como consenso. A literatura de implementação trata a escolha como **decisão de estacionariedade com trade-off explícito**, não como preferência estabelecida — e há um motivo forte do outro lado, que a aula omite e que se conecta diretamente ao 🔴 1 desta mesma auditoria: na OIK, a restrição $\sum\lambda_i=1$ faz com que **a média global não receba peso nenhum**, de modo que a extrapolação se apoia só na vizinhança local e admite pesos negativos — o que torna a OIK **mais propensa a estimativas fora de $[0,1]$**. A SIK ancora a extrapolação na proporção global declusterizada e, por isso, produz menos violações de relação de ordem. Boa parte do software e da literatura de implementação de krigagem indicadora usa a versão simples exatamente por esse motivo. Apresentar a OIK como a escolha da prática é escolher um lado de uma questão em aberto, e escolher o lado que contradiz a correção do achado vermelho.
**Correção aplicada:** parágrafo reescrito como trade-off, com as duas posições e suas razões, e com a conexão explícita entre pesos negativos da OIK e estimativas fora de $[0,1]$. Alegação nova criada, marcada `risk: controverso`.
**Fonte:** Mizuno & Deutsch, *Sequential Indicator Simulation*, Geostatistics Lessons ("the best kriging option will depend on the stationarity decision"; "stationary simple kriging estimates the probability… based on the conditioning data and a declustered global mean value, while in ordinary kriging, the sum of the weights is constrained to one so that the global mean receives no weight") · C. V. Deutsch, *An Overview of Multiple Indicator Kriging*, Geostatistics Lessons · Goovaerts (1997), cap. 7 · **Nível:** referência de implementação / tratado de referência · consultado em 2026-09-18
**Confiança:** confirmado
**Desfecho:** **corrigido**

---

### ⚪ 9. Krigagem log-normal ordinária — a controvérsia existe, mas não é onde a aula diz

**claim_id:** `GEOMOD-M21-A04-KRIGAGEMOLN-004`
**Tipo:** controvérsia (mal localizada) + atribuição de fonte
**Onde:** a04 · seção "Krigagem log-normal baseada em krigagem ordinária (correção aproximada)"; propagado para o objetivo, para o Recap e para a alegação
**Está escrito:** "A prática consolidada (seguindo Rendu, 1979) usa uma correção **aproximada**… Vale registrar com clareza que esta é uma correção **aproximada e heurística**, não uma identidade derivada com o mesmo rigor da versão baseada em krigagem simples — diferentes fontes da literatura de geoestatística aplicada apresentam variações da fórmula."
**Contexto:** esta alegação foi marcada pelo redator como `risk: controverso` com um pedido explícito de checagem cruzada contra a fonte primária antes de ser tratada como definitiva. A checagem foi feita e **inverteu o diagnóstico**.

**Resultado da verificação — três conclusões separadas:**

1. **A fórmula está correta e não é objeto de divergência.** $Z^*_{OK}(x_0) = \exp[Y^*_{OK}(x_0) + \sigma^2_{OK}(x_0)/2 - \psi_{OK}]$ é a forma padrão, reproduzida sem variação nos tratados de referência e na documentação de software de estimativa de recursos. Não há aqui erro a corrigir, e a afirmação de que "diferentes fontes apresentam variações da fórmula" **não se sustenta** — não encontrei nenhuma fonte com uma variante. O termo $-\mu$ tampouco é um remendo: ele é o preço, no espaço logarítmico, de a média ser desconhecida, e é exatamente por isso que ele não aparece na versão de krigagem simples.
2. **A atribuição primária está trocada** (é o componente 🟡 deste achado, contabilizado como 🟡 13). A derivação canônica é de **Journel (1980)**, *The lognormal approach to predicting local distributions of selective mining unit grades*, *Mathematical Geology* 12(4), 285–303, e é assim que os tratados a creditam ("derived by Journel (1980) and presented in Webster and Oliver (2007)"). **Rendu (1979)** é um artigo real, com a paginação citada corretamente pela aula (*J. Int. Assoc. Math. Geol.* 11(4), 407–422), e trata o mesmo problema de estimativa normal e log-normal — é referência anterior legítima, mas não é a fonte da fórmula com o multiplicador de Lagrange.
3. **A controvérsia genuína existe e está em outro lugar.** Dois pontos abertos, ambos com literatura revisada por pares:
   - **Roth (1998)**, *Is lognormal kriging suitable for local estimation?*, *Mathematical Geology* 30(8), 999–1009: o estimador respeita as propriedades de não viés **sobre o campo inteiro**, mas **localmente** apresenta comportamento "neither expected nor intuitive". O título é a pergunta e a resposta não é "sim".
   - **Yamamoto (2007)**, *On unbiased backtransform of lognormal kriging estimates*, *Computational Geosciences* 11(3), 219–234: as estimativas retransformadas **permanecem viesadas** porque o termo de não viés depende **inteiramente** do modelo de variograma ajustado; propõe um fator corretivo alternativo ancorado na média amostral.

**Por que ⚪ branco e não 🔴/🟠:** a aula não afirma nada falso sobre a matemática — ela subestima o status da fórmula e localiza a divergência no lugar errado. Corrigir "aproximada e heurística" para "padrão" é uma correção de caracterização, e a divergência que a aula queria sinalizar **realmente existe**, só que em outro eixo. Tratado conforme a política de achado branco: nenhum lado foi escolhido, as duas posições foram expostas com suas razões.
**Correção aplicada:** a seção foi reescrita. A fórmula passou de $\approx$ para $=$, com a atribuição a Journel (1980) e a nota sobre o papel de Rendu (1979). Acrescentado um bloco curto com as duas divergências reais (Roth 1998, Yamamoto 2007) e a consequência prática para quem usa a técnica (sensibilidade ao modelo de variograma; o relatório precisa reportar o ajuste). O aviso sobre esquecer o termo de correção — que continua verdadeiro em qualquer das posições — foi preservado. Objetivo, Recap, Fontes e alegação realinhados; a alegação segue marcada `risk: controverso` e carrega nota de revisão explicando a inversão do diagnóstico.
**Fonte:** Journel (1980), *Math. Geology* 12(4), 285–303 · Webster & Oliver (2007), *Geostatistics for Environmental Scientists*, 2ª ed., Wiley · Rendu (1979), *J. Int. Assoc. Math. Geol.* 11(4), 407–422 · Roth (1998), *Math. Geology* 30(8), 999–1009 · Yamamoto (2007), *Computational Geosciences* 11(3), 219–234 · Datamine Studio RM, *Grade Estimation Kriging* · **Nível:** revisada por pares / tratado de referência · consultado em 2026-09-18
**Confiança:** confirmado (fórmula e atribuição); em disputa, por natureza (adequação a estimativa local e magnitude do viés residual)
**Desfecho:** **tratado** — texto reescrito mostrando as posições. **Não bloqueia o gate.**

---

### 🟡 10 a 13. Atribuição de capítulo deslocada — Isaaks & Srivastava e Goovaerts

**claim_ids afetados:** `GEOMOD-M21-A02-DEFINICAOINDICADORA-001`, `-002`, `-003`, `-004`, `-005`; `GEOMOD-M21-A03-VARIOGRAMAINDICADOR-001`, `-003`, `-004`, `-005`, `-006`; `GEOMOD-M21-A04-ORIGEMLOGNORMAL-001`, `-002`; listas de Fontes das aulas 02, 03 e 04
**Tipo:** atribuição de fonte
**Problema:** quatro deslocamentos consistentes, todos de uma unidade, todos na mesma direção:

| # | Está escrito | Correto | Ancoragem |
|---|---|---|---|
| 🟡 10 | Isaaks & Srivastava (1989), **cap. 19** — krigagem indicadora, relações de ordem | **cap. 18, *Estimating a Distribution*** | o cap. 19 é *Change of Support* |
| 🟡 11 | Isaaks & Srivastava (1989), **cap. 17** — "transformações e estimativa não linear" (a04) | o **cap. 17 é *Cokriging*** | confirmado diretamente: "Chapter 17 of this book is titled 'Cokriging'" |
| 🟡 12 | Goovaerts (1997), **cap. 6** — indicadoras, ccdf, mediana indicadora | **cap. 7, *Assessment of Local Uncertainty*** | o cap. 6 é *Local Estimation: Accounting for Secondary Information* (cokrigagem) |
| 🟡 13 | Rendu (1979) como fonte da fórmula de krigagem log-normal ordinária | **Journel (1980)**, *Math. Geology* 12(4), 285–303 | ver ⚪ 9, item 2 |

**Correção aplicada:** todas as citações foram corrigidas no corpo, nas listas de Fontes e nos campos `source` dos blocos de alegações, **citando o capítulo pelo título além do número** — assim a referência continua localizável mesmo que a numeração varie entre tiragens. Acrescentadas às Fontes da a04 as obras que de fato sustentam o conteúdo (Journel 1980, Webster & Oliver 2007, Roth 1998, Yamamoto 2007).
**Fonte:** índice de *An Introduction to Applied Geostatistics* (Isaaks & Srivastava, 1989), ancorado na confirmação direta de que o cap. 17 é *Cokriging*, com a sequência *Cokriging* (17) → *Estimating a Distribution* (18) → *Change of Support* (19) → *Assessing Uncertainty* (20) → *Final Thoughts* (21) · índice de *Geostatistics for Natural Resources Evaluation* (Goovaerts, 1997): 6 *Local Estimation: Accounting for Secondary Information*, 7 *Assessment of Local Uncertainty*, 8 *Assessment of Spatial Uncertainty* · **Nível:** base de referência bibliográfica · consultado em 2026-09-18
**Confiança:** confirmado para o cap. 17 = *Cokriging* e para os capítulos do Goovaerts; **provável** para os números exatos 18 e 19 do Isaaks & Srivastava — motivo pelo qual as citações corrigidas trazem o **título** do capítulo, que é a parte verificada.
**Desfecho:** **corrigidos**

---

### 🟡 14. Percentual de comparação da a04 calculado sobre a base errada

**claim_id:** `GEOMOD-M21-A04-EXEMPLONUMERICO-005`
**Tipo:** valor apresentado incorretamente
**Onde:** a04 · Exemplo trabalhado, "Leitura dos resultados"
**Está escrito:** "a diferença entre a retransformação ingênua ($1{,}87$ g/t) e a estimativa log-normal corrigida ($2{,}04$ g/t) é de quase $0{,}17$ g/t — cerca de 9% do valor final"
**Problema:** a aritmética do exemplo fecha em todos os passos ($Y^* = 0{,}62627$; $\exp(Y^*) = 1{,}8706$; $\exp(0{,}71277) = 2{,}0396$; diferença $0{,}1690$) — só o percentual está sobre a base errada. $0{,}1690/2{,}0396 = 8{,}3\%$ do **valor final corrigido**; os $9{,}0\%$ são em relação à **retransformação ingênua** ($0{,}1690/1{,}8706$). A aula nomeia a base como "valor final" e dá o número da outra base.
**Correção aplicada:** "cerca de 9% do valor final" → "cerca de 8% do valor corrigido, ou 9% da retransformação ingênua", nomeando as duas bases. Alegação `-005` ampliada com os dois percentuais e a aritmética exata registrada.
**Fonte:** cálculo direto refeito na auditoria · **Nível:** verificação aritmética
**Confiança:** confirmado
**Desfecho:** **corrigido**

---

### 🟡 15. Regra de tamanho de bloco apresentada sem a ressalva de método

**claim_id:** `GEOMOD-M21-A01-TAMANHOBLOCO-004`
**Tipo:** omissão que gera erro (leve) + superlativo sem base
**Onde:** a01 · seção "O modelo de blocos: revisão e o que muda a partir daqui"; propagado para o Recap
**Está escrito:** "A regra prática **mais citada** ancora o tamanho do bloco na malha de sondagem: um tamanho de bloco horizontal entre um quarto e a metade do espaçamento médio entre furos…"
**Problema:** a faixa está **correta** e foi confirmada (é a regra do *SME Mining Engineering Handbook*: "the block size should be one-half to one-fourth the average drillhole spacing"). O problema é de enquadramento: "a mais citada" é um superlativo não verificável, e a aula apresenta a regra como se fosse o critério de decisão. A prática atual a trata como **ponto de partida**, confirmado por análise quantitativa da vizinhança de krigagem (QKNA), que julga o tamanho escolhido por eficiência de krigagem e inclinação da regressão. Sem essa ressalva, a aula contradiz por omissão a recomendação de QKNA que a auditoria do M20 já havia introduzido no curso.
**Correção aplicada:** "mais citada" → "consolidada"; acrescentada uma frase sobre QKNA ao fim do item, e a ressalva no Recap. Alegação `-004` ampliada, com o SME Mining Engineering Handbook acrescentado como fonte da faixa. Acrescentada a lição de QKNA às Fontes da aula.
**Fonte:** *SME Mining Engineering Handbook* (regra de 1/4 a 1/2 do espaçamento médio de sondagem) · Deutsch & Deutsch, *Quantitative Kriging Neighbourhood Analysis*, Geostatistics Lessons · Geovariances, *Which block size for mineral resource estimation* · **Nível:** manual normativo de indústria / referência de implementação · consultado em 2026-09-18
**Confiança:** confirmado
**Desfecho:** **corrigido**

---

## Verificado e correto

Dezenove alegações e construções foram checadas e passaram sem reparo. Registradas para que uma auditoria futura saiba o que já foi olhado:

| # | Aula | Alegação verificada | Fonte |
|---|---|---|---|
| B1 | a01 | Estrutura relacional de quatro tabelas (collar, survey, assay, litologia) ligadas pelo hole ID, com quebras de profundidade possivelmente distintas entre assay e litologia | Sinclair & Blackwell (2002) cap. 3; Rossi & Deutsch (2014) cap. 3 |
| B2 | a01 | Mínima curvatura como método padrão de desaggregação, ajustando arco circular entre estações | PetroWiki, *Calculation methods for directional survey* |
| B3 | a01 | QA/QC com os três tipos de amostra de controle: duplicatas (precisão), padrões certificados (exatidão/viés), brancos (contaminação) | Rossi & Deutsch (2014) cap. 3 |
| B4 | a01 | Sub-blocking como refinamento local nas bordas de domínio, preservando a regularidade do modelo no interior | Rossi & Deutsch (2014) cap. 5 |
| B5 | a01 | **Exemplo trabalhado (não numérico):** sobreposição 43,5–44,0 m entre dois intervalos de assay; intervalo 45,5–48,0 m excedendo a profundidade final de 46,0 m; survey de estação única. Os três diagnósticos e as três ações (voltar ao boletim primário) estão corretos | Sinclair & Blackwell (2002) cap. 3 |
| B6 | a02 | $E[I(x;z_c)] = F(z_c)$ como consequência direta da esperança de uma Bernoulli — não é aproximação | Journel (1983); Isaaks & Srivastava (1989) cap. 18 |
| B7 | a02 | Convenção de sinal ($\le$ vs. $>$) varia entre autores e precisa ser consistente | Journel (1983) |
| B8 | a02 | Faixa típica de 5 a 15 limiares, escolhidos em percentis/decis da distribuição global | Deutsch, *MIK Overview*; Goovaerts (1997) cap. 7 |
| B9 | a02 | Indicadora categórica: pertença a categoria $k$, sem ordem nem limiar; krigá-la dá probabilidade de domínio | Goovaerts (1997) cap. 7 |
| B10 | a02 | Variável booleana já é a própria indicadora, sem transformação | Goovaerts (1997) cap. 7 |
| B11 | a02 | **Exemplo trabalhado:** tabela de indicadoras para $z_c=0{,}50$ e $z_c=1{,}80$ sobre os cinco teores dados; médias $1/5=0{,}20$ e $4/5=0{,}80$. Conferido linha a linha | verificação aritmética |
| B12 | a03 | ~~Variograma indicador como **proporção de pares discordantes** naquela distância — leitura direta de $[i(x)-i(x+h)]^2 \in \{0,1\}$~~ · **⚠️ SUPERADO em 2026-09-19 pelo achado 🔴 16 (erro de fator 2): $\hat\gamma_I(h)$ é a *metade* dessa proporção.** Registro preservado para histórico; não usar como verificação válida. | Isaaks & Srivastava (1989) cap. 18; Journel (1983) |
| B13 | a03 | Patamar do variograma indicador igual a $F(z_c)[1-F(z_c)]$ sob estacionariedade; máximo $0{,}25$ na mediana | variância de Bernoulli |
| B14 | a03 | Modelos autorizados: esférico, exponencial, gaussiano, pepita, potência, e somas com pesos positivos; variância de krigagem negativa como sintoma de modelo não autorizado | Journel & Huijbregts (1978) caps. II–III |
| B15 | a03 | Correção de relação de ordem: reset para o limite mais próximo fora de $[0,1]$ e média entre correção ascendente e descendente; violações mais frequentes nos limiares extremos por escassez de dados | Deutsch & Journel (1998), GSLIB; Deutsch, *MIK Overview* |
| B16 | a04 | Origem multiplicativa da log-normalidade (TCL aplicado ao produto); diagnóstico por histograma/gráfico de probabilidade do logaritmo | Journel & Huijbregts (1978); Sinclair & Blackwell (2002) cap. 9 |
| B17 | a04 | Viés de Jensen: $\exp$ é convexa, $E[\exp(Y)] \ge \exp(E[Y])$; $E[Z]=\exp(\mu_Y+\sigma_Y^2/2)$; fator $\exp(\sigma_Y^2/2)>1$ | resultado padrão de probabilidade |
| B18 | a04 | Forma exata sob multigaussianidade: $Z^*_{SLN}=\exp[Y^*_{SK}+\sigma^2_{SK}/2]$, sem termo de Lagrange | Journel (1980); Webster & Oliver (2007) |
| B19 | a05 | Voronoi/Delaunay como estruturas duais; bissetriz perpendicular como fronteira de influência; teste de inclusão por paridade de cruzamentos de semirreta; domínio rígido × suave como decisão geológica. **Exemplo trabalhado (a):** $AB$ de $(0,0)$ a $(40,0)$, bissetriz $x=20$ — conferido | de Berg et al. (2008) caps. 7 e 9; Rossi & Deutsch (2014) cap. 4 |

Também verificados e corretos: o método poligonal como anterior à difusão da krigagem na indústria e hoje usado sobretudo como checagem independente; o fluxo de quatro etapas de construção de wireframe (strings → triangulação entre seções → *end caps* → validação topológica) e a exigência de sólido fechado para cálculo de volume e teste de inclusão; a dependência do variograma indicador em relação ao limiar e a leitura geológica dela (alto teor mais localizado, alcance menor).

---

## Verificação transversal

Verificação explícita contra o **M20 (geoestatística)**, pré-requisito declarado, com atenção às **três decisões terminológicas que a auditoria do M20 registrou como obrigatórias de herdar** pelo M21:

1. **"Valor extremo de alto teor" ≠ "teor de corte".** ✅ Respeitado. O módulo usa "teor de corte" exclusivamente para *cutoff* (9 ocorrências) e **nenhuma** ocorrência de "valor de corte". A a02 já dizia "valores extremos de alto teor"; a a04 dizia só "valores extremos" e foi alinhada na auditoria.
2. **A hipótese intrínseca não acomoda deriva.** ✅ Sem risco: o módulo não menciona deriva, hipótese intrínseca nem krigagem universal em nenhuma aula. Nada a contradizer.
3. **A relação de Krige é identidade exata dentro de um domínio $D$.** ✅ Sem risco: o módulo não a invoca.

Verificação adicional contra o **M22 (modelagem geológica 3D)**, que ainda não tem aulas escritas e para o qual a a05 faz um ponteiro declarado (modelagem implícita, interpolação de superfícies, integração com inversão geofísica) — o ponteiro está corretamente marcado como fora do escopo deste módulo, não como conteúdo.

**Nenhuma contradição encontrada.** O M21 reutiliza um conjunto de valores numéricos do exemplo de krigagem ordinária do M20 (a04: $\lambda_1=0{,}8125$, $\lambda_2=0{,}1875$, $\mu=0{,}330$, $\sigma^2_{OK}=0{,}833$) — os quatro foram conferidos contra o registro do M20 e **batem**.

**Ponto de atenção registrado para adiante, não tratado como achado:** o **M42 (exploração mineral e avaliação de recursos)** ainda não tem aulas escritas e vai reencontrar quatro decisões deste módulo, que precisam ser herdadas sem divergência — (a) probabilidade fora de $[0,1]$ na IK é problema de **pesos e vizinhança**, não de variograma não autorizado; (b) SIK × OIK é **trade-off de estacionariedade**, não preferência; (c) a fórmula de krigagem log-normal ordinária é de **Journel (1980)** e é padrão, com a controvérsia em Roth (1998) e Yamamoto (2007); (d) a regra de 1/4–1/2 para tamanho de bloco é **ponto de partida**, confirmado por QKNA.

---

## Correções aplicadas

**Aplicadas em:** 2026-09-18

| claim_id | Sev. | Desfecho | Arquivos alterados |
|---|---|---|---|
| `GEOMOD-M21-A03-SINTOMAMODELONAOAUTORIZADO-003` | 🔴 | Corrigido | aula-03 (corpo, recap, alegação) |
| `GEOMOD-M21-A02-OKSEMHIPOTESEDISTRIBUCIONAL-006` | 🟠 | Corrigido | aula-02 (objetivo, corpo, recap, alegação nova) |
| `GEOMOD-M21-A01-DESURVEY-001` | 🟠 | Corrigido | aula-01 (corpo, Fontes, alegação) |
| `GEOMOD-M21-A05-CIRCUNCIRCULOVAZIO-003` | 🟠 | Corrigido | aula-05 (corpo, recap, Fontes, alegação) |
| `GEOMOD-M21-A03-MEDIANAINDICADORA-004` | 🟠 | Corrigido | aula-03 (corpo em duas seções, recap, Fontes, alegação) |
| `GEOMOD-M21-A03-PATAMARF-008` | 🟠 | Corrigido | aula-03 (exemplo trabalhado, alegação nova) |
| `GEOMOD-M21-A03-EXEMPLONUMERICO-007` | 🟠 | Corrigido | aula-03 (exemplo trabalhado inteiro, alegação) |
| `GEOMOD-M21-A03-SIKVSOIK-009` | 🟠 | Corrigido | aula-03 (corpo, alegação nova) |
| `GEOMOD-M21-A04-KRIGAGEMOLN-004` | ⚪ | **Tratado** (posições expostas) | aula-04 (objetivo, corpo, recap, Fontes, alegação) |
| `GEOMOD-M21-FONTES-ISAAKS-CAP19-010` | 🟡 | Corrigido | aulas 02, 03 (Fontes e 10 campos `source`) |
| `GEOMOD-M21-FONTES-ISAAKS-CAP17-011` | 🟡 | Corrigido | aula-04 (Fontes, alegações `-001`, `-002`) |
| `GEOMOD-M21-FONTES-GOOVAERTS-CAP6-012` | 🟡 | Corrigido | aulas 02, 03, 04 (Fontes e 6 campos `source`) |
| `GEOMOD-M21-FONTES-RENDU-JOURNEL-013` | 🟡 | Corrigido | aula-04 (corpo, Fontes, alegações `-002`, `-003`, `-004`) |
| `GEOMOD-M21-A04-EXEMPLONUMERICO-005` | 🟡 | Corrigido | aula-04 (exemplo trabalhado, alegação) |
| `GEOMOD-M21-A01-TAMANHOBLOCO-004` | 🟡 | Corrigido | aula-01 (corpo, recap, Fontes, alegação) |

**Fontes acrescentadas ao módulo** (não estavam em nenhuma aula e sustentam correções): Journel (1980), *Math. Geology* 12(4), 285–303; Webster & Oliver (2007), *Geostatistics for Environmental Scientists*, 2ª ed., Wiley; Roth (1998), *Math. Geology* 30(8), 999–1009; Yamamoto (2007), *Computational Geosciences* 11(3), 219–234; PetroWiki (SPE), *Calculation methods for directional survey*; Deutsch & Deutsch, *Quantitative Kriging Neighbourhood Analysis*, Geostatistics Lessons; Deutsch, *An Overview of Multiple Indicator Kriging*, Geostatistics Lessons; Chilès & Delfiner (2012), Wiley; *SME Mining Engineering Handbook*.

**Pendências:** nenhuma. **0 vermelhos e 0 laranjas em aberto.** O achado ⚪ 9 está tratado (não pendente): a política do plugin para controvérsia é expor as posições, não escolher lado, e foi o que se fez.

**Material derivado:** o módulo **não tinha** questionário, baralho de flashcards nem glossário quando as correções foram aplicadas. Não há nada a propagar e **nenhum card no Anki a corrigir à mão**. Em particular, a inversão causal do achado vermelho e o exemplo aritmético não reproduzível da a03 não chegaram a virar gabarito.

---

## Gate de avaliação

**Status: LIBERADO** para `gerador-de-questionarios` e `gerador-de-flashcards`, em 2026-09-18.

0 achados vermelhos e 0 laranjas em aberto. O único achado branco está tratado com as duas posições expostas, e não bloqueia — mas impõe uma restrição de formulação, abaixo.

### Restrições para a avaliação

1. **Não cobrar a krigagem log-normal ordinária como se houvesse uma única resposta sobre sua adequação.** A **fórmula** é cobrável como fato ($Z^*_{OLN}=\exp[Y^*_{OK}+\sigma^2_{OK}/2-\mu]$, Journel 1980). A **adequação a estimativa local** não é: se for cobrada, tem de ser como questão de discussão, reconhecendo Roth (1998) e Yamamoto (2007).
2. **Não cobrar "OIK ou SIK, qual é a melhor?" com gabarito fechado.** Cobrar o *trade-off* (estacionariedade × propensão a estimativas fora de $[0,1]$).
3. **O número de limiares (5 a 15) é faixa de prática, não valor a memorizar.** Cobrar o critério (percentis/decis da distribuição global; mais limiares nos trechos de decisão), não o número.
4. **A faixa 1/4–1/2 para tamanho de bloco é ponto de partida.** Cobrar o critério e a existência da confirmação quantitativa (QKNA), nunca a faixa como fórmula.
5. **Não cobrar modelagem implícita, inversão geofísica nem simulação sequencial** — os três aparecem no módulo só como ponteiros declarados fora do escopo (a05 → M22).
6. **Os valores do exemplo da a04 vêm do M20** e já estavam auditados lá; se forem reutilizados numa questão, usar exatamente $\lambda_1=0{,}8125$, $\lambda_2=0{,}1875$, $\mu=0{,}330$, $\sigma^2_{OK}=0{,}833$.

### Avisos ao gerador de questionários e de flashcards

Quinze pontos mudaram nesta auditoria. **Gerar item a partir da versão anterior das aulas produz gabarito errado.** Os de maior valor:

1. **O par de discriminação mais valioso do módulo é "variância de krigagem negativa" × "probabilidade fora de [0,1]".** O primeiro aponta para o **modelo de variograma** (não autorizado); o segundo aponta para os **pesos negativos e a vizinhança**, e ocorre com modelos perfeitamente autorizados. "Probabilidade fora de [0,1] indica variograma não autorizado" é o **distrator perfeito**, porque é exatamente o que a aula dizia antes e o que o senso comum sugere. **Não gerar card nem gabarito que faça essa equivalência** — foi este o erro vermelho corrigido.
2. **Segundo par de alto valor: o que a assimetria compromete na krigagem ordinária.** Não a validade nem a dedução (que não assume distribuição); compromete **robustez** e **otimalidade**. O distrator natural é "a KO exige distribuição aproximadamente normal" — falso, e muito difundido.
3. **Terceiro: o teorema de Delaunay é sobre a triangulação, não sobre cada triângulo.** Excelente para verdadeiro/falso. Distrator: "cada triângulo de Delaunay tem o maior ângulo mínimo possível".
4. **Quarto: o ganho real da mediana indicadora.** Não é só um variograma em vez de vários — é que **os pesos não dependem do limiar**, logo **um sistema de krigagem por bloco**. Item de aplicação de alto valor.
5. **Não gerar item que descreva a fórmula de krigagem log-normal ordinária como "heurística" ou "aproximada"** — era o que a aula dizia e não se sustenta. Ela é padrão e atribuída a Journel (1980).
6. **Não gerar item que atribua a fórmula log-normal OK a Rendu (1979)** como fonte primária.
7. **Atenção ao sinal do termo de Lagrange:** a versão de krigagem **simples** é $\exp[Y^*_{SK}+\sigma^2_{SK}/2]$, **sem** $\mu$; a de krigagem **ordinária** subtrai $\mu$. Trocar as duas é o erro prático que a aula identifica como de maior risco de viés silencioso — ótimo material para questão de aplicação.
8. **Os dois exemplos aritméticos estão conferidos e são base segura.** Valores canônicos, pós-correção: a03 — esférico $C=0{,}22$, $a=80$ m, $\gamma(25)=0{,}0998$, $\gamma(35)=0{,}1352$, $\gamma(50)=0{,}1794$, $\lambda_1=0{,}794$, $\lambda_2=0{,}206$, $\mu=0{,}072$, $i^*=0{,}794$; a04 — $Y^*=0{,}6263$, ingênua $1{,}871$ g/t, corrigida $2{,}04$ g/t.
9. **A variância da indicadora é $F(1-F)$, máxima ($0{,}25$) só na mediana.** Não chamar o patamar de um limiar qualquer de "variância máxima".
10. **Terminologia herdada do M20, obrigatória:** **valor extremo de alto teor** para *high-grade outlier*; **teor de corte** reservado ao *cutoff*. As duas coisas aparecem juntas neste módulo (capeamento na a02/a04, limiar na a02/a03) e confundi-las num item seria reintroduzir um erro já corrigido no curso.
11. **Delaunay é única só em posição geral.** Numa malha de sondagem quadrada há quatro pontos cocirculares e a unicidade falha — bom item de aplicação com gancho geológico.
12. **O tangencial simples e o tangencial balanceado não são a mesma coisa**: o primeiro deve ser abandonado, o segundo tem exatidão comparável à da mínima curvatura.

### Recomendação de formato do questionário

**Questionário único, sem parciais.** Registrada em detalhe no hub do módulo; resumo aqui: o módulo tem **5 aulas**, dentro do limiar de ~5–6 do plugin abaixo do qual não se dividem parciais, e a estrutura reforça a decisão — **duas cadeias curtas que convergem** (a01 → a02 → a03 → a04, a cadeia de estimativa; a01 → a05, a cadeia geométrica), com a a05 explicitamente dependente das quatro anteriores para o passo de integração. Partir em parciais cortaria a convergência, que é onde estão as questões de maior valor. Comparação com os vizinhos: M20 (4 aulas) e M17 (6 aulas) usaram questionário único; M19 (7 aulas) usou 3 parciais + final.

> **Revisão após a etapa didática:** se a revisão didática dividir a a03 ou a a04 em Parte 1/Parte 2, o módulo vai a 6 aulas — ainda **dentro** do limiar, e a recomendação **não muda**, porque uma divisão de aula longa não cria um corte conceitual novo, só reparte um existente.

---

## Observações fora de escopo (para o `revisor-didatico`)

1. **a03 é a aula mais pesada do módulo e ficou mais pesada com esta auditoria.** Ela já declarava 30 min (o teto do plugin) antes das correções, e o achado 🔴 1 e o 🟠 8 acrescentaram dois blocos densos à mesma aula: a separação dos dois sintomas e o trade-off SIK × OIK. A estimativa pós-auditoria é de **~2440 palavras**, bem acima do que as outras aulas do módulo carregam. **O conteúdo está certo; a forma pede intervenção.** É a primeira aula a olhar, e a candidata mais forte à divisão em Parte 1 / Parte 2 pela convenção dos módulos 17, 19 e 20 — com um corte natural já visível: variograma indicador e modelagem (autorizado/não autorizado, full IK × median IK) numa parte, sistema de krigagem e relações de ordem na outra.
2. **a04 também cresceu**, de ~2120 para ~2350 palavras, por conta do bloco de controvérsia do ⚪ 9. Vale checar se a seção "Krigagem log-normal baseada em krigagem ordinária" não virou o ponto mais denso da aula, acumulando fórmula, atribuição histórica e duas divergências de literatura num só fôlego.
3. **a01 tem sequência de leitura estranha na abertura.** Ela declara como pré-requisito o M20 inteiro e depois gasta a primeira seção argumentando por que a base de dados vem antes da geoestatística — um argumento que o aluno já deveria ter aceito para ter chegado até aqui. Vale checar se não é redundância.
4. **Termos técnicos usados antes de definidos.** A a01 usa "composição por bancada" e "teor de corte" antes de qualquer definição neste módulo (ambos vêm do M20, mas a a01 não sinaliza isso); a a02 menciona "*local ccdf*" como "a peça central" três vezes antes de a a03 mostrar o que é. São *forward references* declaradas, não erros — cabe ao revisor julgar se o aluno consegue seguir.
5. **A a05 muda de natureza no meio do módulo.** As aulas 01–04 são quantitativas e a a05 é geométrica e qualitativa (interpretação de seção, julgamento geológico). A própria aula sinaliza a mudança, mas vale checar se a transição está suficientemente preparada — a a04 termina anunciando a a05 em uma linha.
6. **Alinhamento objetivo ↔ conteúdo:** o `oa02` é mapeado por duas aulas (a02 inteira + três seções da a03) e o `oa03` por duas (duas seções da a03 + a a04 inteira). Não é erro, mas significa que **nenhum objetivo tem correspondência 1:1 com uma aula** neste módulo — diferente do M20. Se a a03 for dividida, o mapeamento pode ficar mais limpo, com `oa02` na Parte 1 e `oa03` na Parte 2.

---

## Correções pós-divisão

**Segunda passagem:** 2026-09-19 · **Modo:** `audit-and-fix` · **Profundidade:** `full`, escopo restrito
**Disparada por:** `21-modelagem-geoestatistica-depositos-minerais-revisao-didatica.md`, seção "Encaminhado ao `auditor-cientifico`"
**Escopo:** os dois pontos de fato que a revisão didática identificou e deliberadamente não tratou, mais o exemplo trabalhado novo que a divisão criou na a03, mais duas discrepâncias de escrituração.

Nenhum achado da primeira passagem foi reaberto, reauditado, renumerado ou apagado. A numeração dos achados continua de onde parou: o último da primeira passagem é o 🟡 15, e os novos são **🔴 16** e **🟡 17**.

---

### 🔴 16. Erro de fator 2 na leitura verbal do variograma indicador

**claim_id:** `GEOMOD-M21-A03-VARIOGRAMAINDICADOR-001` (reaberto por erro de fator; `claim_id` **preservado**)
**Tipo:** erro factual + inconsistência interna
**Onde:** nova a03 · seção "O variograma experimental indicador" e "Recap relâmpago"
**Registro anterior:** verificado como correto na primeira passagem (azul **B12**, 2026-09-18). **Aquela verificação estava errada** e este achado a supera.

**Está escrito:** "O variograma indicador é, portanto, uma **proporção de pares discordantes** naquela distância: a fração de pares de amostras separadas por $h$ que caem em lados diferentes do limiar $z_c$."

**Problema:** a fórmula impressa **duas linhas acima**, na própria aula, é a do **semi**variograma experimental:

$$\hat\gamma_I(h;z_c) = \frac{1}{2N(h)}\sum_{k=1}^{N(h)}\left[i(x_k;z_c)-i(x_k+h;z_c)\right]^2$$

Como cada termo do somatório vale 0 ou 1, o somatório é exatamente $D(h)$, o **número** de pares discordantes. Logo

$$\hat\gamma_I(h) = \frac{D(h)}{2N(h)} = \frac{1}{2}\cdot\underbrace{\frac{D(h)}{N(h)}}_{\text{proporção de pares discordantes}}$$

O semivariograma indicador é **metade** da proporção de pares discordantes, não a proporção. A proporção é $2\hat\gamma_I(h)$ — isto é, o **variograma** $2\gamma$, e não o semivariograma, que é o objeto que se calcula, se plota, se modela e se usa no sistema de krigagem. **Das duas leituras, a fórmula estava certa e a explicação verbal estava errada.**

**Inconsistência interna que confirma o diagnóstico (decisiva).** A mesma aula afirma, duas linhas adiante, que o patamar vale $F(z_c)[1-F(z_c)]$, com máximo $0{,}25$ na mediana — alegação `GEOMOD-M21-A03-PATAMARF-008`, verificada e correta (B13). As duas afirmações não podem ser ambas verdadeiras: a distâncias grandes, em que as amostras do par são independentes, a probabilidade de um par ser discordante é $P(1,0)+P(0,1) = 2F(1-F)$. Pela leitura verbal antiga, o patamar na mediana teria de ser $2(0{,}5)(0{,}5) = 0{,}5$; pela fórmula, é a metade disso, $0{,}25$ — que é o valor correto e o que a própria aula declara. O fator 2 é exatamente a discrepância.

**Correção aplicada:**
- **Corpo:** a frase passa a dizer que o somatório *conta* os pares discordantes e que, por causa do $\frac{1}{2N(h)}$, $\hat\gamma_I(h)$ é **metade da proporção**, sendo a proporção $2\hat\gamma_I(h)$ — "o variograma $2\gamma$, não o semivariograma que se plota e se modela". A leitura intuitiva ("que fração dos pares muda de lado do corte") foi **preservada**, agora condicionada ao fator ("guardado esse fator 2"): ela é didaticamente valiosa e só precisava da escala certa.
- **Fecho de coerência:** acrescentada, logo após a menção ao patamar, a verificação que amarra as duas afirmações — a distâncias grandes a proporção tende a $2F(z_c)[1-F(z_c)]$ e sua metade é exatamente o patamar; na mediana, metade dos pares distantes é discordante e o patamar vale $0{,}25$, não $0{,}5$.
- **Recap:** primeiro marcador corrigido na mesma formulação.
- **Bloco de alegações:** `claim` de `-001` reescrita com o fator correto e com a checagem de consistência contra `-008`; `source` ampliada com Journel & Huijbregts (1978), cap. II, para a definição do semivariograma com o fator $\tfrac12$; campo `revisao` acrescentado.
- **B12** marcado como superado na tabela "Verificado e correto", sem ser apagado.

**Fonte:** Journel, A. G. & Huijbregts, C. J. (1978), *Mining Geostatistics*, Academic Press, cap. II — definição do semivariograma $\gamma(h)=\tfrac12 E\{[Z(x)-Z(x+h)]^2\}$, com o variograma sendo $2\gamma(h)$ · Deutsch, C. V., *The Sill of the Variogram*, Geostatistics Lessons — fórmula experimental $\hat\gamma(h)=\frac{1}{2N(h)}\sum[Z(u_i)-Z(u_i+h)]^2$, verbatim, consultada em 2026-09-19 · Isaaks & Srivastava (1989), cap. 18 · variância de Bernoulli $F(1-F)$ para o patamar. **Nível:** tratado normativo + referência de implementação
**Confiança:** **confirmado** — a fórmula do semivariograma com $\tfrac{1}{2N(h)}$ é normativa e não está em disputa, e a álgebra é de uma linha. Reforçada por consistência interna independente (o patamar $F(1-F)$).
**Também aparece em:** nenhum outro arquivo. Varredura no curso inteiro por "discordante"/"muda de lado": as únicas ocorrências no sentido geoestatístico eram as duas da a03 (corpo e recap), mais o registro B12 deste relatório e a nota da revisão didática. A ocorrência no M10 (a02) é "discordância" em sentido estratigráfico, sem relação.
**Material derivado:** **nenhum.** O módulo continua sem questionário, sem baralho e sem glossário — o erro não chegou a virar gabarito nem card, e **não há nada a reimportar no Anki**.
**Desfecho:** **corrigido**

> **Por que a primeira passagem não pegou.** B12 verificou a *substância* da alegação — que $[i(x)-i(x+h)]^2\in\{0,1\}$ e que por isso o variograma indicador mede discordância entre pares — e a substância está certa. O que não foi conferido foi a **constante de proporcionalidade**, que a fórmula impressa ao lado já fixava. É um modo de falha a registrar: uma alegação pode estar qualitativamente certa e quantitativamente errada, e a verificação qualitativa passa por cima disso. **Lição de processo:** quando uma alegação verbal traduz uma fórmula impressa, conferir a igualdade termo a termo, não só o sentido — e cruzar com o valor assintótico (aqui, o patamar), que é o teste barato que teria pego o fator 2 na primeira passagem.

---

### 🟡 17. Referência cruzada de numeração errada numa nota de revisão

**claim_id:** `GEOMOD-M21-A01-TAMANHOBLOCO-004` (nota de escrituração; a alegação em si continua correta e corrigida)
**Tipo:** inconsistência interna de escrituração
**Onde:** a01 · bloco `alegacoes_auditaveis`, campo `revisao` da alegação `-004`
**Está escrito:** "2026-09-18 — auditoria 🟡 16: a faixa 1/4–1/2 foi confirmada…"
**Problema:** este relatório numera aquele achado como **🟡 15**, não 🟡 16. Não há e nunca houve um achado 🟡 16 na primeira passagem — a numeração dela termina em 15. Sem efeito sobre o conteúdo científico, mas é exatamente o tipo de ponteiro quebrado que uma auditoria futura segue e não encontra. Agravante superveniente: o número 16 agora **existe** e designa outro achado (o 🔴 16 acima), de modo que a referência errada deixou de ser apenas inútil e passou a apontar para o achado errado.
**Correção aplicada:** "🟡 16" → "🟡 15" no campo `revisao` da alegação `-004` em `…-aula-01-consolidacao-validacao-bases-dados-modelo-blocos.md`. Nenhuma outra alteração naquele arquivo.
**Fonte:** consistência interna deste relatório (achados numerados 1–15 na primeira passagem, sem lacunas).
**Confiança:** confirmado
**Desfecho:** **corrigido**

---

### ✅ Exemplo trabalhado novo da a03 — auditado e aprovado (registro azul **B20**)

O exemplo trabalhado da nova a03 foi **criado pela revisão didática** ao dividir a antiga a03 (achado didático `DID-M21-A03-EXEMPLOP1-003`) e **não havia passado pela auditoria**. Foi refeito do zero, pelo mesmo procedimento da primeira passagem.

**(a) Patamares contra $F(z_c)[1-F(z_c)]$** — as três multiplicações, recalculadas independentemente:

| Limiar | $F(z_c)$ | $F(1-F)$ recalculado | Patamar impresso | Confere |
|---|---|---|---|---|
| decil 1 | $0{,}10$ | $0{,}10\times0{,}90 = 0{,}09$ | $0{,}09$ | ✅ |
| mediana | $0{,}50$ | $0{,}50\times0{,}50 = 0{,}25$ | $0{,}25$ | ✅ |
| decil 9 | $0{,}90$ | $0{,}90\times0{,}10 = 0{,}09$ | $0{,}09$ | ✅ |

A simetria invocada ("os decis 1 e 9 têm o mesmo patamar porque $F(1-F)$ é simétrica em torno de $F=0{,}5$") está correta: $F(1-F)$ é uma parábola com concavidade para baixo, simétrica em $F=0{,}5$, e $0{,}10$ e $0{,}90$ são equidistantes dela.

**(b) Alcances e a decisão *median IK* × *full IK*** — afirmações numéricas conferidas uma a uma:

- "alcances de 95 m e 90 m, praticamente iguais" — diferença de 5 m, **5,3%**. ✅ defensável.
- "O decil 9 não: 40 m, **menos da metade** dos outros dois" — $40 < 45$ (metade de 90) e $40 < 47{,}5$ (metade de 95). ✅ verdadeiro para os dois.
- "aplicaria ao decil 9 um alcance **mais que duas vezes maior** do que o medido" — a mediana IK usaria o variograma da mediana, de alcance 90 m; $90/40 = 2{,}25 > 2$. ✅ correto.

A conclusão conceitual — a hipótese da mediana indicadora (forma e alcance relativo constantes entre limiares, só o patamar variando) falha neste conjunto, logo o depósito pede *full IK* ao menos na faixa alta — é aplicação correta de `GEOMOD-M21-A03-MEDIANAINDICADORA-004`. A leitura geológica (alto teor mais localizado, amarrado a estruturas discretas, perdendo continuidade antes do corpo como um todo) reaplica `GEOMOD-M21-A02-VARIOGRAMAPORLIMIAR-005`, já verificada.

**(c) Por que a mediana é o limiar de referência** — $F(1-F)$ é máxima em $F=0{,}5$, onde vale $0{,}25$. ✅ correto (vértice da parábola).

**Verificado e não é achado:** a expressão "o que dá o variograma experimental com **mais pares informativos**" poderia sugerir que o número de pares $N(h)$ muda com o limiar — o que é falso, já que $N(h)$ é fixado pela geometria da malha e é o mesmo em todos os cortes. A leitura correta, porém, é a que o texto explicita no mesmo período ("porque é onde a indicadora tem a **variância máxima** e portanto o sinal mais forte"): o que é máximo na mediana é o número de pares **discordantes**, os únicos que contribuem com termo não nulo ao somatório — no limite de independência, $2F(1-F)$, que vale $0{,}18$ no decil 1 e $0{,}50$ na mediana. Sob essa leitura a afirmação é verdadeira e está glosada nos dois lugares em que aparece (corpo e exemplo). **Não é achado.** Registro a checagem para que uma auditoria futura não a reabra. Nota: a correção do 🔴 16 **reforçou** este ponto, porque agora a aula nomeia explicitamente a proporção de pares discordantes e sua relação com $2\hat\gamma_I(h)$.

**Alegações factuais novas introduzidas pelo exemplo:** **nenhuma.** Cada passo reaplica alegação já rastreada (`-008`, `-004`, `A02-005`), como a revisão didática havia declarado. Os valores da tabela são ilustrativos e o enunciado os declara hipotéticos ("conjunto hipotético, montado para exercitar a leitura"), no mesmo padrão dos demais exemplos do módulo.

**Veredito do exemplo:** **fecha aritmeticamente em todos os passos; nenhuma correção necessária.** Registrado como azul **B20** e anotado no bloco `divisao_didatica` da a03.

Com isso, o módulo passa a ter **três** exemplos trabalhados numéricos conferidos número por número (a03 novo, a04 sistema de krigagem, a05 retransformação log-normal) e três não numéricos conferidos (a01, a02, a06).

---

### Nota de escrituração: a contagem de amarelos da primeira passagem

**Não é achado e o número não foi alterado** — é uma explicação, registrada porque a discrepância já foi notada duas vezes (pelo manifesto e pela revisão didática) e merece fechamento.

O cabeçalho e a tabela de severidade da primeira passagem declaram **7 amarelos**; o relatório enumera **6** `claim_id` amarelos distintos (🟡 10–15). A hipótese que circulava — de que o 7º seria `GEOMOD-M21-FONTES-ISAAKS-CAP19-010` contado duas vezes por ter sido aplicado em **duas** aulas (a02 e a03) — **foi verificada e não se sustenta**, por contraexemplo interno: `GEOMOD-M21-FONTES-GOOVAERTS-CAP6-012` foi aplicado em **três** aulas (a02, a03, a04) e é contado **uma** vez. O relatório não conta achados por aula de aplicação, e portanto não contaria o 010 duas vezes.

A explicação que o próprio relatório sustenta é mais simples e verificável por aritmética: os achados da primeira passagem são numerados de **1 a 15, sem lacunas**, e se distribuem em 🔴 1 (um), 🟠 2–8 (sete), ⚪ 9 (**um**) e 🟡 10–15 (**seis**) — total 15. O cabeçalho, porém, descreve os mesmos 15 como "1 vermelho, 7 laranjas, 7 amarelos" **e** trata o branco como adicional, o que somaria 16. **O achado branco foi absorvido na contagem de amarelos ao redigir o cabeçalho.** O número correto de amarelos distintos da primeira passagem é **6**.

**Decisão:** o número declarado no levantamento (**7**) fica preservado no cabeçalho e na tabela de severidade, conforme a política deste relatório de não reescrever contagens de levantamento; esta nota é o registro da leitura correta. O manifesto `.json` já trazia a discrepância em `summary.summary_note` e o campo `summary.yellow_enumerated_claim_ids: 6` — ambos mantidos, com a hipótese do 010 **substituída** pela explicação confirmada. **Sem efeito sobre o gate:** todos os amarelos, seis ou sete, estão corrigidos e nenhum está em aberto.

---

### Correções aplicadas — segunda passagem

**Aplicadas em:** 2026-09-19

| claim_id | Sev. | Desfecho | Arquivos alterados |
|---|---|---|---|
| `GEOMOD-M21-A03-VARIOGRAMAINDICADOR-001` | 🔴 16 | **Corrigido** | `…-aula-03-variograma-indicador-modelos-autorizados.md` (corpo, recap, alegação `-001`, bloco `divisao_didatica`, `palavras_corpo`); `…-auditoria.md` (B12 marcado como superado) |
| `GEOMOD-M21-A01-TAMANHOBLOCO-004` | 🟡 17 | **Corrigido** | `…-aula-01-consolidacao-validacao-bases-dados-modelo-blocos.md` (campo `revisao` da alegação `-004`) |
| exemplo trabalhado novo da a03 | 🔵 B20 | **Aprovado sem correção** | `…-aula-03-….md` (registro no bloco `divisao_didatica`) |

**Metadado sincronizado:** `palavras_corpo` da a03 de **1.860** para **1.964** (a correção do 🔴 16 acrescentou ~104 palavras entre o corpo e o recap). A aula segue em ~25–26 min, **abaixo do teto de 30 min** — a divisão didática não fica comprometida.

**Pendências:** **nenhuma.** **0 vermelhos e 0 laranjas em aberto.**

**Material derivado:** o módulo continua **sem questionário, sem baralho de flashcards e sem glossário**. Nada a propagar e **nenhum card no Anki a corrigir à mão**. Como na primeira passagem, o erro foi pego antes de virar gabarito — e desta vez por pouco: o 🔴 16 é precisamente o tipo de erro que produziria um valor numérico errado em questão de aplicação.

---

### Gate de avaliação — reconfirmado

**Status: LIBERADO**, reconfirmado em 2026-09-19.

0 achados vermelhos e 0 laranjas em aberto após a segunda passagem. As seis restrições e os doze avisos ao gerador registrados na primeira passagem **continuam todos válidos**, e a segunda passagem acrescenta **dois**:

13. **O variograma indicador é METADE da proporção de pares discordantes.** A proporção é $2\hat\gamma_I(h)$. Este é o erro que o 🔴 16 corrigiu e é um **distrator excelente** — a formulação errada é intuitiva e era o que a aula dizia. **Não gerar item nem card que afirme que $\hat\gamma_I(h)$ *é* a proporção de pares discordantes.** Se a questão pedir número: na mediana, a distâncias grandes, metade dos pares é discordante e o patamar vale $0{,}25$ — jamais $0{,}5$. O cruzamento com o patamar $F(1-F)$ (aviso 9) é a checagem que fecha o item.
14. **O exemplo trabalhado novo da a03 é base segura para questão de aplicação.** Valores canônicos: $F=0{,}10/0{,}50/0{,}90$; patamares $0{,}09/0{,}25/0{,}09$; alcances $95/90/40$ m; razão $90/40=2{,}25$. O item de maior valor é o **(b)** — decidir *median IK* × *full IK* a partir da comparação de alcances, e não pela definição decorada. Gabarito: **full IK**, ao menos na faixa alta de limiares.
