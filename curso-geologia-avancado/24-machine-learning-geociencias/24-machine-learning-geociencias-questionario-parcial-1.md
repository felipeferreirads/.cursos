# Questionário parcial 1 — Módulo 24: Fundamentos e aplicações de machine learning em geociências

**Módulo:** [[24-machine-learning-geociencias-modulo|Módulo 24 — Fundamentos e aplicações de machine learning em geociências]]
**Cobertura:** Aulas 01 a 02 — IA, aprendizado de máquina e aprendizado profundo; tipos de aprendizado; fontes e desafios dos dados geológicos; fluxo de trabalho em Python (definição do problema, coleta, preparação, análise exploratória, particionamento).
**Recorte:** o problema e os dados — antes de qualquer algoritmo. A parcial 1 testa se você sabe situar a técnica, reconhecer por que dados geológicos são difíceis e preparar e particionar uma tabela sem contaminar a avaliação.
**Objetivos avaliados:** `geologia-avancado-m24-oa01` (integral — a01), `geologia-avancado-m24-oa02` (integral — a02)
**Pontuação total:** 100 pontos · o gabarito fica oculto; responda antes de abrir.

---

### 1. Múltipla escolha — `geologia-avancado-m24-q01` · oa01 · 12 pts

Qual afirmação descreve corretamente a relação entre inteligência artificial (IA), aprendizado de máquina (ML) e aprendizado profundo (DL)?

- a) O aprendizado profundo é o campo mais amplo, e contém o aprendizado de máquina e a inteligência artificial como casos particulares
- b) A IA contém o ML, que contém o DL; um sistema especialista com regras "se-então" escritas por um geólogo é IA, mas não é aprendizado de máquina
- c) IA e ML são sinônimos; só o aprendizado profundo é capaz de aprender regras a partir de dados
- d) Um sistema especialista é aprendizado de máquina, porque melhora sozinho quando recebe mais exemplos

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A relação é de inclusão estrita: todo DL é ML, todo ML é IA, mas a IA contém mais do que ML (sistemas de regras, busca, lógica simbólica) e o ML contém mais do que DL (regressão linear, árvores, florestas, K-means — nenhum deles rede neural). O que define o ML é o deslocamento de "receber a regra pronta" para "inferir a regra a partir de dados"; o sistema especialista codifica regras fixas e não melhora com mais exemplos, por isso é IA sem ser ML. "a" inverte a hierarquia. "c" confunde os campos e atribui só ao DL algo que todo ML faz. "d" erra exatamente o critério: regra escrita à mão não aprende.
</details>

---

### 2. Aplicação — `geologia-avancado-m24-q02` · oa01 · 12 pts

Uma equipe de exploração tem três demandas. Para cada uma, diga (i) o tipo de aprendizado e (ii) a tarefa, justificando pela presença ou ausência de rótulo.

- **A.** 120 testemunhos com porosidade medida em laboratório; prever a porosidade de testemunhos novos a partir de perfis geofísicos.
- **B.** 800 amostras de sedimento de corrente com geoquímica multielementar completa, sem nenhuma classe atribuída; descobrir se existem populações geoquímicas distintas.
- **C.** 400 seções finas já classificadas por um petrógrafo como "alterada" ou "fresca"; treinar um sistema que classifique seções novas.

<details>
<summary>Ver resposta</summary>

**A.** Aprendizado **supervisionado**, tarefa de **regressão**: existe rótulo e ele é um número contínuo (porosidade).

**B.** Aprendizado **não supervisionado**, tarefa de **agrupamento** (*clustering*): nenhuma amostra chega com etiqueta de grupo, e o objetivo é justamente descobrir estrutura nos próprios dados.

**C.** Aprendizado **supervisionado**, tarefa de **classificação**: cada seção já traz um rótulo categórico atribuído por especialista. Por serem imagens, é também candidata natural a aprendizado profundo (redes convolucionais), mas a decisão sobre o tipo de aprendizado vem só da presença do rótulo, não da natureza da entrada.

O critério que separa os tipos é a pergunta única da Aula 01: os dados de treino trazem o resultado certo anotado, ou não? Dentro do supervisionado, o que distingue regressão de classificação é a natureza do rótulo (contínuo ou categórico).
</details>

---

### 3. Verdadeiro ou Falso (justifique) — `geologia-avancado-m24-q03` · oa01 · 10 pts

"Como rótulos geológicos costumam vir de ensaios caros (análise química, datação, seção fina), os conjuntos rotulados são pequenos; isso é uma vantagem para modelos com muitos parâmetros, como redes neurais profundas, que aprendem melhor quando há poucos dados."

<details>
<summary>Ver resposta</summary>

**Falso.**

A primeira parte está correta: dezenas a poucas centenas de amostras rotuladas é comum, ordens de grandeza abaixo dos milhões de exemplos típicos de aplicações de imagem ou texto. Mas a consequência é o inverso da afirmada: modelos com muitos parâmetros e poucos dados de treino têm capacidade de **memorizar** o conjunto em vez de generalizar — é o sobreajuste. Escassez de rótulos penaliza justamente os modelos de alta capacidade; a Aula 07 mostra o caso extremo, com 257 parâmetros para 45 amostras de treino.
</details>

---

### 4. Dissertativa curta — `geologia-avancado-m24-q04` · oa01 · 14 pts

Explique por que a **autocorrelação espacial** dos dados geológicos viola uma premissa central do aprendizado de máquina clássico e qual é a consequência concreta para a medida de desempenho quando o conjunto é dividido em treino e teste por sorteio de amostras. Relacione com o Módulo 20.

<details>
<summary>Ver resposta</summary>

Uma boa resposta cobre:

- A premissa violada é a de amostras **independentes e identicamente distribuídas** (i.i.d.). Amostras geológicas próximas se parecem mais do que amostras distantes — é a ideia de variável regionalizada e de continuidade espacial que o Módulo 20 formalizou por meio do variograma.
- Consequência: num sorteio aleatório, é comum duas amostras vizinhas (quase-duplicatas espaciais) caírem uma no treino e outra no teste. O teste deixa de ser dado genuinamente novo; a informação "vazou" do treino para o teste pela proximidade, e o desempenho medido fica **artificialmente otimista**.
- Correção (retomada nas Aulas 02 e 06): validação/particionamento por **blocos espaciais**, de modo que nenhum bloco de teste contenha vizinhos imediatos do treino.

Bônus aceitável: mencionar que a amostragem preferencial (furos concentrados onde já há indício) é um quarto desafio, que faz o modelo aprender mais sobre onde já se olhava do que sobre onde não se olhou.
</details>

---

### 5. Múltipla escolha — `geologia-avancado-m24-q05` · oa02 · 12 pts

Numa tabela de 60 amostras, a coluna `As_ppm` tem 3 valores ausentes (falhas de leitura do laboratório). Qual decisão é a mais defensável, e qual é sua limitação?

- a) Preencher com a média da coluna, porque a média é mais robusta a valores extremos do que a mediana
- b) Preencher com a mediana da coluna, que é robusta a valores extremos; a limitação é que atenua artificialmente a variância da coluna e ignora a relação do arsênio com as demais variáveis, problema que cresce com a fração de dados ausentes
- c) Descartar sempre a linha inteira, porque imputar nunca é aceitável em dados geológicos
- d) Preencher com zero, porque leitura ausente significa teor nulo

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Com apenas 3 de 60 valores ausentes, imputar pela mediana é o padrão simples e razoável: a mediana é robusta a valores extremos (ao contrário da média, o que derruba "a"), e descartar as linhas perderia a informação das demais colunas daquelas amostras. A limitação é real: a imputação por valor único atenua a variância e ignora que uma amostra de Cu alto tende a ter As alto; com muitos ausentes seriam preferíveis métodos que usam as outras variáveis (regressão, vizinho mais próximo). "c" é rígido demais — descartar só se justifica com poucas linhas afetadas **e** variável central. "d" é errado fisicamente: falha de leitura não é teor zero.
</details>

---

### 6. Aplicação / cálculo — `geologia-avancado-m24-q06` · oa02 · 14 pts

Uma tabela de 200 amostras tem 50 rotuladas como anômalas (25%) e 150 como background. Você usa `train_test_split(X, y, test_size=0.30, random_state=1, stratify=y)`.

(a) Quantas amostras vão para treino e quantas para teste? (b) Quantas anômalas e quantas background você espera em cada conjunto? (c) Para que serve o `stratify=y`? (d) Por que o mesmo argumento não resolve o problema de um alvo contínuo como `Au_ppb`?

<details>
<summary>Ver resposta</summary>

(a) Teste = 30% de 200 = **60**; treino = **140**.

(b) A estratificação preserva a proporção de 25%/75%: teste com **15 anômalas e 45 background**; treino com **35 anômalas e 105 background**.

(c) Sem `stratify`, o sorteio de linhas é independente e, em conjuntos pequenos, pode concentrar por azar uma classe num dos lados, deixando o teste artificialmente fácil ou difícil. `random_state` fixa a semente e torna a divisão reproduzível.

(d) `stratify` só se aplica a **rótulos categóricos**: não há como forçar duas fatias de uma variável numérica a terem a mesma média por sorteio de linhas inteiras. Na Aula 02, a divisão de `Au_ppb` deixou o teste com média de cerca de 27,1 ppb contra 18,7 ppb no treino (~45% mais alta) — um lembrete de conferir esse deslocamento antes de julgar um erro de previsão em conjuntos pequenos.
</details>

---

### 7. Verdadeiro ou Falso (justifique) — `geologia-avancado-m24-q07` · oa02 · 10 pts

"Na análise exploratória do conjunto da Aula 02, `Cu_ppm` tem média de 365,4 ppm e mediana de 271,1 ppm. Como os dois valores são da mesma ordem de grandeza, a distribuição do cobre é simétrica."

<details>
<summary>Ver resposta</summary>

**Falso.**

Comparar média e mediana é um diagnóstico rápido de assimetria: numa distribuição simétrica os dois coincidem. Aqui a média está bem acima da mediana (365,4 contra 271,1), o que denuncia assimetria **à direita** — poucas amostras muito enriquecidas (o máximo é 1.202,4 ppm) puxam a média para cima, padrão comum em dados geoquímicos. Ser "da mesma ordem de grandeza" não é critério de simetria. Um histograma (`plt.hist`) tornaria a cauda visível.
</details>

---

### 8. Integração (Aulas 01–02) — `geologia-avancado-m24-q08` · oa01+oa02 · 16 pts

A Aula 01 adverte que particionamento aleatório vaza informação em dados espaciais; a Aula 02, porém, usa `train_test_split` com sorteio simples e o declara adequado. (a) Por que isso não é contradição? (b) Um colega tem 500 amostras de solo com coordenadas x/y e propõe o mesmo `train_test_split` aleatório. O que você diria, e o que você trocaria?

<details>
<summary>Ver resposta</summary>

(a) Porque o conjunto da Aula 02 **não carrega coordenadas espaciais** e é sintético, gerado com ruído independente; não há vizinhança a violar, então o sorteio simples é adequado a ele "tal como construído". A advertência da Aula 01 vale para conjuntos reais com posição espacial conhecida, e a própria Aula 02 diz isso.

(b) Um conjunto real com posição espacial conhecida tem amostras vizinhas autocorrelacionadas (quase-duplicatas espaciais). O sorteio simples as separaria entre treino e teste, e o desempenho medido ficaria artificialmente otimista. A troca é por um particionamento/validação em **blocos geográficos**, por exemplo `GroupKFold` do scikit-learn com um identificador de bloco espacial (recomendação retomada na Aula 06), garantindo que nenhum bloco de teste contenha vizinhos imediatos de um bloco de treino. Fora isso, a sequência de etapas (definir, coletar, preparar, explorar, particionar) e a estratificação por rótulo continuam valendo.
</details>

---

**Total: 100 pontos.**
