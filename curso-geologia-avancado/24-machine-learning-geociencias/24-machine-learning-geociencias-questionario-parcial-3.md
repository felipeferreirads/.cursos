# Questionário parcial 3 — Módulo 24: Fundamentos e aplicações de machine learning em geociências

**Módulo:** [[24-machine-learning-geociencias-modulo|Módulo 24 — Fundamentos e aplicações de machine learning em geociências]]
**Cobertura:** Aulas 06 a 07 — métricas de regressão e de classificação, sobreajuste, validação cruzada k-fold; redes neurais (perceptron multicamadas), estudos de caso, importância por permutação, comunicação de resultados com suas limitações.
**Recorte:** a avaliação e a honestidade sobre o resultado. A parcial 3 testa se você sabe medir um modelo com a métrica certa, diagnosticar sobreajuste, desconfiar de um número único e comunicar o que o modelo não permite concluir.
**Objetivos avaliados:** `geologia-avancado-m24-oa04` (integral — a06 e a07)
**Pontuação total:** 100 pontos · o gabarito fica oculto; responda antes de abrir.

---

### 20. Múltipla escolha — `geologia-avancado-m24-q20` · oa04 · 6 pts

A regressão linear da Aula 03 tem MAE = 5,128 ppb e RMSE = 6,759 ppb no teste. O que a diferença entre as duas métricas indica?

- a) Que houve erro de cálculo, pois as duas métricas deveriam coincidir
- b) Que o RMSE é sempre maior ou igual ao MAE, porque eleva os erros ao quadrado e penaliza os grandes; uma diferença de cerca de 1,6 ppb sinaliza que algumas previsões erraram bem mais do que a média
- c) Que o modelo é excelente, pois RMSE menor que MAE é o sinal de bom ajuste
- d) Que o modelo está sobreajustado, pois RMSE mede o erro no treino e MAE mede o erro no teste

<details>
<summary>Ver resposta</summary>

**Resposta: b**

MAE é a média dos erros em valor absoluto e está na unidade do rótulo; RMSE eleva cada erro ao quadrado antes da média e extrai a raiz, o que penaliza desproporcionalmente os erros grandes. Por isso RMSE ≥ MAE sempre, e a distância entre eles cresce quando há alguns erros muito maiores que os demais. "a" e "c" ignoram essa desigualdade. "d" confunde métrica com conjunto: ambas são calculadas sobre o mesmo conjunto de teste; o diagnóstico de sobreajuste compara treino com teste, não RMSE com MAE.
</details>

---

### 21. Múltipla escolha — `geologia-avancado-m24-q21` · oa04 · 6 pts

Um modelo de regressão tem R² = −0,1208 no conjunto de teste. Como interpretar?

- a) O modelo explica 12% da variação do alvo, com sinal invertido por convenção
- b) O modelo erra menos do que prever a média do alvo para toda amostra, mas só um pouco
- c) O modelo é pior do que a previsão trivial de sempre prever a média do alvo — um sinal inequívoco de modelo malajustado
- d) O R² não pode ser negativo; houve erro na avaliação

<details>
<summary>Ver resposta</summary>

**Resposta: c**

$R^2 = 1 - \frac{\sum (y_i-\hat y_i)^2}{\sum (y_i-\bar y)^2}$ compara o erro do modelo com o do modelo trivial que sempre prevê a média: 1 é perfeito, 0 é igual à média, e **negativo** é pior que a média. É perfeitamente possível em teste — foi exatamente o que aconteceu com a rede neural de regressão da Aula 07. "a" e "b" leem o sinal ao contrário; "d" é falso.
</details>

---

### 22. Aplicação / cálculo — `geologia-avancado-m24-q22` · oa04 · 12 pts

Um classificador de amostras anômalas produz, em 100 amostras de teste, a matriz `[[TN, FP], [FN, TP]] = [[70, 10], [5, 15]]`, com "anômala" como classe positiva. Calcule acurácia, precisão, revocação e F1, e diga qual das duas métricas de classe (precisão ou revocação) é mais preocupante e por quê.

<details>
<summary>Ver resposta</summary>

- **Acurácia** = (TP + TN)/total = (15 + 70)/100 = **0,85**.
- **Precisão** = TP/(TP + FP) = 15/(15 + 10) = **0,60**: das amostras previstas como anômalas, só 60% realmente são.
- **Revocação** = TP/(TP + FN) = 15/(15 + 5) = **0,75**: das anômalas reais, 75% foram capturadas.
- **F1** = 2·(0,60·0,75)/(0,60 + 0,75) = 0,90/1,35 ≈ **0,667**, a média harmônica, que penaliza o desequilíbrio entre as duas.

A acurácia de 0,85 parece alta e esconde que a classe positiva é a rara (20 de 100) e que 40% do que o modelo aponta como anômalo é alarme falso (10 de 25 previsões positivas). Qual das duas é mais preocupante depende do custo dos erros: se deixar passar um alvo (falso negativo) é o que mais dói, a revocação de 0,75 é a preocupação; se cada furo em estéril (falso positivo) consome orçamento, é a precisão de 0,60. É uma decisão do geólogo, não do algoritmo.
</details>

---

### 23. Aplicação — `geologia-avancado-m24-q23` · oa04 · 10 pts

Um colega apresenta um classificador de instabilidade de encostas com 96% de acurácia. Você pede a matriz: nas 250 encostas de teste, 10 são instáveis e 240 são estáveis, e o modelo previu "estável" para todas. Reconstrua a matriz, calcule a revocação e a precisão da classe instável e diga se o modelo deve ser aprovado para triagem.

<details>
<summary>Ver resposta</summary>

Matriz (classe positiva = instável): TN = 240, FP = 0, FN = 10, TP = 0. Acurácia = 240/250 = **0,96**, confirmando o número reportado.

Revocação da classe instável = TP/(TP + FN) = 0/10 = **0**: nenhuma encosta instável real é identificada. Precisão = 0/0, **indefinida**, porque o modelo nunca fez uma previsão positiva; o F1 da classe é 0.

**O modelo não deve ser aprovado.** Sob classes desbalanceadas (4% de instáveis), um modelo que só prevê a classe majoritária alcança acurácia alta com revocação zero na classe que interessa — o cenário mais perigoso em geociências, onde a classe rara costuma ser a economicamente ou ambientalmente relevante. Antes de qualquer aprovação, é preciso reportar revocação e F1 da classe instável e, dado o desbalanceamento, considerar reponderação de classes, reamostragem ou limiar de decisão diferente de 0,5.
</details>

---

### 24. Aplicação — `geologia-avancado-m24-q24` · oa04 · 12 pts

Uma árvore de decisão foi treinada com profundidades diferentes sobre 45 amostras de treino e avaliada em 15 de teste:

| max_depth | acurácia de treino | acurácia de teste |
|---|---|---|
| 1 | 0,911 | 0,933 |
| 2 | 0,911 | 0,933 |
| 3 | 1,000 | 0,533 |
| 5 | 1,000 | 0,533 |
| sem limite | 1,000 | 0,533 |

(a) A partir de qual profundidade há sobreajuste, e qual o tamanho do gap? (b) Por que profundidades 3, 5 e "sem limite" dão resultados idênticos? (c) Por que a linha de profundidade 1 (teste acima do treino) não indica problema?

<details>
<summary>Ver resposta</summary>

(a) A partir de `max_depth=3`: o treino salta para 1,000 (a árvore memoriza as 45 amostras, inclusive o ruído de rótulo de 12% da Aula 02) e o teste despenca para 0,533 — gap de **0,467**, quase 47 pontos percentuais. O sintoma característico de sobreajuste é desempenho excelente no treino e visivelmente pior no teste.

(b) Com apenas 45 amostras e seis variáveis, a árvore já atinge acurácia de treino perfeita numa profundidade baixa; aumentar mais a profundidade não muda nada, porque simplesmente não há mais nó para dividir de forma útil.

(c) Teste ligeiramente acima do treino (0,933 contra 0,911) é plausível numa amostra pequena de 15 amostras e não é o padrão de memorização: o modelo simples não decorou o treino. O diagnóstico é sempre comparar treino com teste, nunca julgar só pelo treino — e um modelo simples demais erraria em ambos por igual (subajuste).
</details>

---

### 25. Múltipla escolha — `geologia-avancado-m24-q25` · oa04 · 10 pts

A floresta de classificação obteve 0,933 na divisão única treino/teste. Uma validação cruzada k-fold (5 folds, todas as 60 amostras) deu acurácias de 0,917; 0,917; 0,833; 0,833; 0,833 (média 0,867; desvio-padrão 0,041). Qual conclusão é a mais adequada?

- a) A validação cruzada está errada, porque o resultado da divisão única é o oficial
- b) A partição única foi favorável ao modelo (0,933 supera até o melhor fold); o desempenho esperado é melhor descrito por 0,867 com desvio de 0,041, e o desvio quantifica quanto o resultado varia conforme o subconjunto usado como teste
- c) O modelo melhorou com a validação cruzada, porque foi treinado cinco vezes
- d) O desvio-padrão de 0,041 mostra que o modelo é instável demais para ser usado em qualquer cenário

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Numa divisão única, o resultado depende de um sorteio; aqui 0,933 é maior que o de qualquer um dos cinco folds (o melhor foi 0,917), o que indica partição favorável. A validação cruzada gira qual quinto fica de fora, usa mais dados no total e entrega uma média **e** um desvio — e o desvio é a informação nova: sem ele, um número único dá falsa sensação de precisão. O mesmo vale para a regressão: MAE de 5,128 na divisão única contra 6,846 ppb na validação cruzada. "a" inverte a lógica. "c" atribui melhora a um procedimento que só mede. "d" exagera: 0,041 é uma faixa de variação a comunicar, não um veto. A *leave-one-out* do Módulo 20 é o caso extremo de k-fold em que k é igual ao número de amostras.
</details>

---

### 26. Verdadeiro ou Falso (justifique) — `geologia-avancado-m24-q26` · oa04 · 6 pts

"Na Aula 07, o MLP de classificação sem padronização obteve 0,333 de acurácia no teste, que tem 10 anômalas em 15 amostras. Isso é só um pouco abaixo do acaso, e padronizar as variáveis seria um refinamento opcional para redes neurais."

<details>
<summary>Ver resposta</summary>

**Falso.**

Prever a classe majoritária para toda amostra daria 10/15 = **0,667**; os 0,333 são **pior** do que esse chute, não "um pouco abaixo do acaso". E a padronização não é opcional: a descida de gradiente que ajusta os pesos é sensível à escala das entradas — uma variável de escala grande (Cu, na casa das centenas) domina o gradiente inicial e o treinamento converge mal. Com padronização, a mesma arquitetura sobe para 0,867: a diferença entre um modelo inutilizável e um competitivo. É a mesma razão de padronizar antes do K-means, com um motivo adicional.
</details>

---

### 27. Aplicação / cálculo — `geologia-avancado-m24-q27` · oa04 · 14 pts

No estudo de caso de regressão, a rede (16, 8) teve R² de treino = 0,9991 e de teste = −0,1208, MAE de teste 12,716 ppb (contra 5,128 da regressão linear), com 257 parâmetros para 45 amostras de treino. (a) Diagnostique. (b) Conte os parâmetros de uma rede para outro conjunto com 6 entradas, uma camada oculta de 10 neurônios e 1 saída, e compare com as mesmas 45 amostras. (c) O que você recomendaria?

<details>
<summary>Ver resposta</summary>

(a) **Sobreajuste severo**: a rede praticamente decora o treino (R² ≈ 1) e generaliza pior do que prever a média (R² de teste negativo), com MAE de teste mais que o dobro do da regressão linear na mesma tarefa. O treinamento ainda esgotou o limite de 5.000 iterações e emitiu `ConvergenceWarning`: a rede para no limite, numa solução que reproduz o treino e generaliza mal.

(b) Parâmetros = pesos + vieses de cada camada: $6\times10 + 10 + 10\times1 + 1 = 60 + 10 + 10 + 1 =$ **81** parâmetros; para 45 amostras, cerca de 1,8 parâmetro por amostra (contra mais de 5 por amostra na rede de 257). Ainda é muito para 45 amostras, embora bem menos desfavorável.

(c) Para esta tarefa, descartar a rede e ficar com a regressão linear (melhor R² e menor MAE entre os três de regressão, e o modelo mais simples de explicar e auditar). Não porque redes neurais sejam ruins em geral, mas porque 45 amostras não sustentam centenas de graus de liberdade; com milhares de amostras rotuladas a conclusão poderia mudar.
</details>

---

### 28. Múltipla escolha — `geologia-avancado-m24-q28` · oa04 · 8 pts

No MLP de classificação, a **importância por permutação** dá `dist_falha_m = −0,002`, enquanto a **importância por impureza** da floresta de classificação dá 0,261 para a mesma variável. Como interpretar a divergência?

- a) A distância à falha é irrelevante, e a floresta foi enganada
- b) A permutação dilui variáveis correlacionadas: `dist_falha_m` tem r = −0,90 com o cobre, então embaralhá-la não derruba o desempenho porque o modelo recupera a informação pelo cobre; o valor baixo não significa ausência de relação com o alvo
- c) O valor negativo prova que a distância à falha prejudica o modelo
- d) As duas medidas deveriam coincidir numericamente; a divergência indica erro de código

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A importância por permutação mede a queda de desempenho quando uma variável é embaralhada; se outra variável correlacionada carrega a mesma informação, a queda é pequena para **ambas**, embora as duas sejam informativas. O sinal levemente negativo é ruído do embaralhamento repetido, não um efeito real ("c"). "d" está errada: as duas medidas medem grandezas diferentes (queda de acurácia versus redução de impureza) e não são numericamente comparáveis. Nenhuma medida de importância é neutra: a de impureza favorece variáveis contínuas sobre binárias; a de permutação dilui as correlacionadas. Interpretar um modelo com uma única medida é arriscado.
</details>

---

### 29. Dissertativa — `geologia-avancado-m24-q29` · oa04 · 16 pts

Você precisa reportar ao gerente de exploração o resultado do MLP de regressão da Aula 07 (R² de treino 0,9991; R² de teste −0,1208; 60 amostras no total). Liste os elementos que a comunicação deve declarar, além da métrica, e diga qual recomendação decorre do resultado.

<details>
<summary>Ver resposta</summary>

Uma comunicação adequada declara, no mínimo:

1. **O modelo escolhido e por quê** — aqui o MLP foi testado por completude pedagógica, não porque o problema exigisse uma rede neural.
2. **O tamanho do conjunto** (60 amostras, 45 de treino) e por que isso limita a complexidade recomendável (257 parâmetros para 45 amostras).
3. **A métrica no teste, nunca só no treino, com sua incerteza** — o R² de treino de 0,9991 sozinho seria enganoso; o tipo de informação que deve acompanhar um número único é o desvio-padrão entre folds da validação cruzada (0,041 no exemplo da Aula 06).
4. **Para que decisões o modelo é ou não adequado.** Um R² negativo em teste **veta** o uso do modelo para orientar sondagem adicional; a recomendação é usar a regressão linear (R² 0,79) e descartar a rede para esta tarefa.

Reportar apenas "MLP: MAE de X ppb" omitiria exatamente a informação que determina se o resultado é confiável. Dizer que o modelo não deve ser usado faz parte do trabalho tanto quanto treiná-lo.
</details>

---

**Total: 100 pontos.**
