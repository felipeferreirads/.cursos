# Questionário final cumulativo — Módulo 24: Fundamentos e aplicações de machine learning em geociências

**Módulo:** [[24-machine-learning-geociencias-modulo|Módulo 24 — Fundamentos e aplicações de machine learning em geociências]]
**Cobertura:** o módulo inteiro — Aulas 01 a 07 (IA e dados geológicos; fluxo de trabalho em Python; regressão; classificação; modelagem não supervisionada; avaliação, sobreajuste e validação; deep learning, estudos de caso e comunicação de resultados).
**Recorte:** integração. O final cumulativo pesa aplicação e conexões entre aulas: a lição do módulo — nenhum número único de desempenho, nenhuma medida de importância e nenhum algoritmo é confiável sozinho — só aparece atravessando as três parciais. Há três questões de integração explícita (q32, q37 e q40).
**Objetivos avaliados:** `geologia-avancado-m24-oa01`, `geologia-avancado-m24-oa02`, `geologia-avancado-m24-oa03`, `geologia-avancado-m24-oa04`
**Pontuação total:** 100 pontos · o gabarito fica oculto; responda antes de abrir.

---

### 30. Múltipla escolha — `geologia-avancado-m24-q30` · oa01+oa03 · 6 pts

Uma mineradora tem 1.200 análises multielementares de rocha, sem nenhuma classe litológica atribuída, e quer sugerir domínios geoquímicos candidatos. Qual abordagem é a mais adequada?

- a) Treinar uma floresta aleatória de classificação, que aprende as classes sozinha a partir das variáveis
- b) Padronizar as variáveis e aplicar K-means, escolhendo $k$ pelo método do cotovelo, tratando o resultado como ferramenta exploratória e não como substituto do julgamento geológico de campo
- c) Ajustar uma regressão linear múltipla do cobre contra os demais elementos
- d) Treinar um MLP com as variáveis brutas, sem padronização, para acelerar o treinamento

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Não há rótulo, logo o problema é de aprendizado **não supervisionado** e a tarefa é de agrupamento. Como K-means usa distância, a padronização é indispensável (sem ela o elemento de maior escala domina); o cotovelo orienta a escolha de $k$. Na prática profissional, domínios são definidos predominantemente por critério geológico (contatos, zonas de alteração) e só secundariamente checados estatisticamente; o agrupamento serve para sugerir domínios candidatos ou verificar se um domínio definido geologicamente é também estatisticamente coerente. "a" exige rótulo que não existe. "c" é regressão, tarefa distinta. "d" acumula dois erros: uma rede treinada com rótulo não resolve o problema sem rótulo, e a falta de padronização prejudica muito redes neurais.
</details>

---

### 31. Verdadeiro ou Falso (justifique) — `geologia-avancado-m24-q31` · oa02+oa04 · 8 pts

"Como a floresta de classificação obteve 0,933 de acurácia na partição da Aula 02, esse é o desempenho que se deve esperar do modelo em amostras novas."

<details>
<summary>Ver resposta</summary>

**Falso.**

Uma única partição é produto de um sorteio (a Aula 02 fixou `random_state=42`, o que a torna reproduzível, não representativa). A validação cruzada de 5 folds da Aula 06 deu média de **0,867** com desvio-padrão de **0,041**, e o 0,933 é maior do que o de qualquer fold (o melhor foi 0,917): a partição calhou de ser favorável. Além disso, com 15 amostras de teste, um único erro muda a acurácia em mais de 6 pontos percentuais (14/15 contra 13/15). O número a comunicar é a média com sua variação, não o melhor resultado de uma divisão.
</details>

---

### 32. Integração / aplicação — `geologia-avancado-m24-q32` · oa01+oa02+oa04 · 10 pts

Um colega tem 500 amostras de sondagem com coordenadas x/y e reporta acurácia de 0,95 com uma floresta avaliada por `KFold(shuffle=True)`. Você refaz a validação com blocos geográficos (`GroupKFold`, um identificador de bloco por região) e obtém 0,78 (valores hipotéticos). (a) Explique a diferença. (b) Qual dos dois números é mais confiável para prever o desempenho numa área nova, e por quê? (c) Que desafio dos dados geológicos (Aula 01) está em jogo?

<details>
<summary>Ver resposta</summary>

(a) Amostras de sondagem vizinhas são autocorrelacionadas (quase-duplicatas espaciais). No `KFold` com embaralhamento, vizinhas caem em folds diferentes; o modelo é "lembrado" de amostras que já viu no treino e o teste deixa de ser dado genuinamente novo — a informação vaza e o desempenho medido é artificialmente otimista. Com blocos geográficos, nenhum bloco de teste contém vizinhos imediatos do treino, e a queda de 0,95 para 0,78 é a medida do vazamento.

(b) O **0,78**, porque reproduz a situação real de uso — prever numa região sem vizinhos no treino. O 0,95 responde a uma pergunta diferente (interpolar entre vizinhos).

(c) A **autocorrelação espacial** que viola a premissa i.i.d. (Aula 01, com o variograma do Módulo 20 como pano de fundo); a solução foi antecipada na Aula 02 e detalhada na Aula 06, com `GroupKFold` por blocos. Vale acrescentar que a amostragem preferencial (furos onde já havia indício) é um fator adicional que enviesa ainda mais o quanto o modelo sabe sobre onde não se olhou.
</details>

---

### 33. Múltipla escolha — `geologia-avancado-m24-q33` · oa03 · 6 pts

Qual afirmação compara corretamente a regressão linear múltipla da Aula 03 com a krigagem ordinária do Módulo 20?

- a) Ambas usam atributos químicos medidos na própria amostra como variáveis explicativas; só o algoritmo de ajuste difere
- b) Ambas são combinações lineares ponderadas ajustadas a dados; na regressão, as variáveis explicativas são atributos medidos na própria amostra e a posição espacial é ignorada; na krigagem, o que pesa é a posição espacial relativa das vizinhas, com pesos vindos do variograma
- c) A krigagem exige rótulos categóricos, e a regressão linear, coordenadas espaciais
- d) A regressão linear usa o variograma para ponderar as amostras, e a krigagem usa mínimos quadrados ordinários

<details>
<summary>Ver resposta</summary>

**Resposta: b**

As duas pertencem à família dos mínimos quadrados (a krigagem, à dos generalizados, GLS — não confundir com GLM), mas respondem perguntas diferentes: a regressão prevê o ouro **a partir de outras propriedades químicas** da mesma amostra, e duas amostras próximas ou distantes com os mesmos teores contam do mesmo jeito; a krigagem prevê um valor **a partir de valores vizinhos no espaço**, sem nenhuma variável explicativa além da posição. "a", "c" e "d" atribuem a cada método o que é do outro.
</details>

---

### 34. Aplicação / cálculo — `geologia-avancado-m24-q34` · oa03+oa04 · 8 pts

Nas três primeiras amostras do teste de regressão, os valores observados de Au são 7,87; 19,26 e 9,89 ppb, e a regressão linear prevê 5,28; 8,86 e 24,15 ppb. (a) Calcule o MAE e o RMSE dessas três amostras. (b) Compare com o MAE de 5,128 e o RMSE de 6,759 das 15 amostras. (c) O que isso mostra sobre avaliar um modelo com poucas amostras?

<details>
<summary>Ver resposta</summary>

(a) Erros absolutos: 2,59; 10,40; 14,26. **MAE** = (2,59 + 10,40 + 14,26)/3 = 27,25/3 ≈ **9,08 ppb**. Erros ao quadrado: 6,71; 108,16; 203,35, soma ≈ 318,22; média ≈ 106,07; **RMSE** = √106,07 ≈ **10,30 ppb**.

(b) Ambos são bem maiores que os valores das 15 amostras (5,128 e 6,759), e o RMSE segue acima do MAE (a diferença é maior aqui, porque a terceira amostra, com previsão de 24,15 para um valor real de 9,89, é um erro grande que o quadrado amplifica).

(c) Uma métrica calculada sobre poucas amostras é **instável**: nas mesmas três amostras, a floresta teve MAE de 8,34 — melhor que a regressão linear (9,08) —, o inverso da ordem nas 15 amostras (5,778 contra 5,128). Três amostras não são base confiável para julgar um modelo; é para isso que o conjunto de teste completo existe, e é por isso que a validação cruzada e o desvio entre folds importam.
</details>

---

### 35. Aplicação / cálculo — `geologia-avancado-m24-q35` · oa03+oa04 · 8 pts

Para as matrizes de teste da Aula 04, com "anômala" como classe positiva — logística `[[4, 1], [1, 9]]` e floresta `[[5, 0], [1, 9]]` —, calcule precisão, revocação e F1 de cada uma. Numa triagem em que o erro mais caro é deixar passar uma amostra anômala, a floresta é melhor?

<details>
<summary>Ver resposta</summary>

**Logística:** precisão = 9/(9+1) = 0,900; revocação = 9/(9+1) = 0,900; F1 = 0,900.

**Floresta:** precisão = 9/(9+0) = **1,000**; revocação = 9/(9+1) = **0,900**; F1 = 2·(1,0·0,9)/(1,0+0,9) ≈ **0,947**.

A revocação é **igual** (0,900 nos dois): o falso negativo (1) é o mesmo. A vantagem da floresta está inteiramente na precisão (nenhum falso positivo). Portanto, se o erro mais caro é deixar passar anômala, a floresta **não** é melhor nesse critério; ela é melhor em não gastar furos com estéril. E como o teste tem só 15 amostras e a floresta cai para 0,867 ± 0,041 na validação cruzada, nenhuma dessas diferenças deve ser lida como definitiva.
</details>

---

### 36. Múltipla escolha — `geologia-avancado-m24-q36` · oa03+oa04 · 6 pts

O MLP de classificação (65 parâmetros) teve acurácia de treino 1,000 e de teste 0,867, um gap de 13,3 pontos percentuais; o MLP de regressão (257 parâmetros) teve R² de treino 0,9991 e de teste −0,1208. Ambos com 45 amostras de treino. Qual é a melhor explicação para o sobreajuste ser muito mais severo no segundo?

- a) Regressão é intrinsecamente mais difícil que classificação para qualquer algoritmo
- b) A razão entre parâmetros e amostras de treino é muito mais desfavorável na rede de regressão (257/45, mais de 5 por amostra, contra 65/45, cerca de 1,4), e não há informação nos dados para restringir tantos graus de liberdade
- c) A rede de regressão foi treinada sem padronização
- d) Redes neurais só sobreajustam em regressão

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A contagem de parâmetros ($6\times16+16+16\times8+8+8\times1+1 = 257$, contra $6\times8+8+8\times1+1 = 65$) para as mesmas 45 amostras explica a diferença de gravidade: o de classificação memoriza, mas não colapsa; o de regressão memoriza e generaliza pior que a média. "a" e "d" são generalizações sem base — o que mudou foi a razão parâmetros/amostras, não a natureza da tarefa. "c" é falso: a rede de regressão **foi** treinada com variáveis padronizadas.
</details>

---

### 37. Integração — `geologia-avancado-m24-q37` · oa03+oa04 · 8 pts

Um relatório do módulo afirma: "O MLP de regressão foi o pior dos seis modelos treinados, e a floresta de classificação, com 0,933, foi o melhor dos seis." Avalie a afirmação e reformule o que é defensável.

<details>
<summary>Ver resposta</summary>

A afirmação **não é defensável**, porque os seis modelos não são ordenáveis num ranking único: os três de regressão são avaliados por R²/MAE e os três de classificação por acurácia/F1, métricas incomensuráveis entre tarefas diferentes (R² compara o erro com o de prever a média de um alvo contínuo; acurácia é fração de acertos de classe).

O que é defensável são as comparações **dentro** de cada tarefa: na **regressão**, regressão linear (R² = 0,7879; MAE = 5,128) > floresta (0,7331; 5,778) > MLP (−0,1208; 12,716), e o MLP é o pior **entre os três de regressão** e o único com R² negativo em todo o módulo; na **classificação**, floresta (0,933) > regressão logística (0,867) = MLP (0,867), com a ressalva de que a diferença da floresta é um único falso positivo e não sobrevive à validação cruzada (0,867 ± 0,041). O fio comum, este sim comparável entre as tarefas, é que o modelo de maior capacidade nominal não produziu o melhor resultado em nenhuma das duas.
</details>

---

### 38. Aplicação / cálculo — `geologia-avancado-m24-q38` · oa04 · 8 pts

Para um novo conjunto de 100 amostras de treino, você propõe um MLP com 8 variáveis de entrada, duas camadas ocultas (20 e 10 neurônios) e 1 saída. (a) Calcule o número de parâmetros. (b) Qual a razão parâmetros/amostras e o que ela antecipa? (c) Que diagnóstico rodar e o que fazer se ele indicar problema?

<details>
<summary>Ver resposta</summary>

(a) $8\times20 + 20 + 20\times10 + 10 + 10\times1 + 1 = 160 + 20 + 200 + 10 + 10 + 1 =$ **401** parâmetros (pesos e vieses).

(b) 401/100 ≈ **4 parâmetros por amostra** — uma razão desfavorável, próxima do regime que, no módulo, levou a rede de 257 parâmetros com 45 amostras (mais de 5 por amostra) ao R² negativo em teste. Antecipa alto risco de sobreajuste.

(c) Comparar o desempenho no **treino** com o do **teste** (o gap grande é o sintoma) e, de preferência, validar por k-fold, reportando média e desvio. Se houver sobreajuste, reduzir a capacidade (menos camadas/neurônios), e comparar sempre contra um modelo simples de referência (regressão linear ou logística): se o modelo simples empata ou vence, ele deve ser o recomendado. Lembre de padronizar as entradas antes de treinar.
</details>

---

### 39. Múltipla escolha — `geologia-avancado-m24-q39` · oa03+oa04 · 6 pts

Um relatório diz apenas: "A variável mais importante para o ouro é `Cu_ppm`." Qual é a crítica correta?

- a) Está correto: o cobre é a variável mais importante em todos os modelos do módulo
- b) A afirmação é incompleta porque não diz **por qual método**: no modelo linear padronizado, `Zn_ppm` tem o maior efeito (7,05, contra 6,66 do cobre); pela impureza da floresta de regressão o maior é `Zn_ppm` (0,272); só pela impureza da floresta de classificação (0,349) e pela permutação do MLP (0,216) o cobre lidera; cada medida tem seu viés
- c) Está errada porque o cobre não tem nenhuma importância em nenhum modelo
- d) Só pode ser avaliada por `feature_importances_`, pois é a única medida válida

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A resposta a "qual a variável mais importante" muda com o método (e com a tarefa: regressão do ouro versus classificação de `anomalo`, cujo rótulo foi construído a partir do cobre). Cada medida tem ponto cego próprio: a importância por impureza favorece variáveis contínuas sobre binárias (a cota irrelevante supera a litologia real na floresta de classificação), e a permutação dilui as correlacionadas (a distância à falha aparece nula, −0,002, no MLP, mesmo com 0,261 na floresta). Coeficientes não padronizados nem sequer são comparáveis entre variáveis. "a" e "d" ignoram tudo isso; "c" é um exagero sem base.
</details>

---

### 40. Integração (Aulas 01–07) — `geologia-avancado-m24-q40` · oa01+oa02+oa03+oa04 · 10 pts

Ao longo do módulo, um número único de desempenho enganou de pelo menos três maneiras diferentes. Descreva **três** situações (citando o número envolvido em cada uma) e o que cada uma exigiu do analista.

<details>
<summary>Ver resposta</summary>

Qualquer três das seguintes (todas verificadas no módulo):

1. **Amostra de avaliação pequena (Aula 03).** MAE de 9,08 ppb nas três primeiras amostras contra 5,128 ppb nas 15 do teste; e a ordem entre floresta e regressão linear se inverte (8,34 contra 9,08 em três amostras; 5,778 contra 5,128 em quinze). Exige base de avaliação adequada e cautela com métricas de poucas amostras.
2. **Acurácia mistura tipos de erro (Aulas 04 e 06).** Acurácias de 0,867 e 0,933 diferem por um único falso positivo, com o mesmo falso negativo; e um classificador de encostas com 96% de acurácia pode ter revocação zero na classe instável. Exige ler a matriz de confusão e reportar precisão, revocação e F1 por classe.
3. **Divisão única favorável (Aula 06).** Acurácia de 0,933 na divisão única contra 0,867 ± 0,041 na validação cruzada; MAE de 5,128 contra 6,846 ppb. Exige validação cruzada e reportar a variação entre folds.
4. **Desempenho só no treino (Aulas 06 e 07).** Acurácia de treino 1,000 da árvore profunda (teste 0,533) e R² de treino 0,9991 da rede (teste −0,1208). Exige comparar treino com teste.
5. **Partição aleatória em dado espacial (Aulas 01, 02 e 06).** Desempenho otimista por vazamento entre vizinhos. Exige blocagem espacial (`GroupKFold`).

O fio comum: nenhum número único, nenhuma divisão única e nenhuma medida única de importância é suficiente para confiar num modelo.
</details>

---

### 41. Aplicação / decisão — `geologia-avancado-m24-q41` · oa03+oa04 · 10 pts

Numa campanha nova, você tem 80 amostras rotuladas de Au (60 de treino, 20 de teste) e obtém, no teste (valores hipotéticos): regressão linear R² = 0,74; floresta de regressão R² = 0,71; MLP (32, 16) com R² de treino = 0,99 e de teste = −0,30. (a) Qual modelo recomendar? (b) Redija, em quatro pontos, o que a comunicação ao gerente deve conter. (c) Faz sentido dizer que "o MLP é pior do que a floresta de classificação que já usamos para o rótulo anômalo"?

<details>
<summary>Ver resposta</summary>

(a) A **regressão linear**: melhor R² no teste entre os três e a mais simples de explicar e auditar. O MLP deve ser descartado nesta tarefa: R² de treino de 0,99 com R² de teste negativo é o retrato do sobreajuste severo (modelo pior do que prever a média), com muito mais parâmetros do que a amostra sustenta. A diferença entre linear (0,74) e floresta (0,71) é pequena e, com 20 amostras de teste, não deve ser tratada como definitiva; convém validar por k-fold.

(b) (1) o modelo escolhido e por quê (e que o MLP foi testado e descartado); (2) o tamanho do conjunto (80 amostras, 60 de treino) e como isso limita a complexidade; (3) a métrica **no teste**, com sua incerteza (média e desvio de uma validação cruzada); (4) para que decisões o modelo serve e para quais não — e que o R² negativo do MLP **veta** seu uso para orientar sondagem.

(c) Não: comparar um modelo de regressão (R²) com um de classificação (acurácia) não é operação definida; só se compara dentro da mesma tarefa e com a mesma métrica.
</details>

---

### 42. Verdadeiro ou Falso (justifique) — `geologia-avancado-m24-q42` · oa03+oa04 · 6 pts

"A padronização das variáveis só é necessária para o K-means, porque só ele usa distância; PCA e redes neurais dispensam esse passo."

<details>
<summary>Ver resposta</summary>

**Falso.**

O K-means precisa dela porque usa distância euclidiana: a variável de maior escala numérica dominaria os grupos. Mas a padronização também foi aplicada ao **PCA** do módulo (sobre Cu, As e Zn padronizados, o que torna os componentes comparáveis por variância em vez de dominados pela escala) e é **ainda mais crítica para redes neurais**, porque a descida de gradiente é sensível à escala das entradas: o MLP de classificação teve 0,333 de acurácia sem padronização (pior que prever a classe majoritária, 0,667) e 0,867 com ela. A regra prática: quando o algoritmo é sensível à escala das variáveis (distância, gradiente, variância) e a escala numérica não reflete a importância geológica — o que em dados geoquímicos é a regra —, padronize.
</details>

---

**Total: 100 pontos.**
