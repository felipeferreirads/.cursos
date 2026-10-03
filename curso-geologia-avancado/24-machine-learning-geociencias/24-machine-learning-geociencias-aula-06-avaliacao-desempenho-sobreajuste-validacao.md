# Aula 06: Medidas de avaliação de desempenho, sobreajuste e validação

**ID:** geologia-avancado-m24-a06
**Módulo:** [[24-machine-learning-geociencias-modulo|Módulo 24 — Fundamentos e aplicações de machine learning em geociências]]
**Duração estimada:** ~29 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** formalizar as métricas de avaliação de regressão e classificação já usadas informalmente nas Aulas 03 e 04, diagnosticar sobreajuste comparando desempenho em treino e teste, e validar um modelo com validação cruzada k-fold — a contrapartida, em aprendizado de máquina, da validação cruzada *leave-one-out* já vista para krigagem no Módulo 20.
**Ao final você vai conseguir:** ler uma matriz de confusão e calcular acurácia, precisão, revocação e F1 a partir dela; explicar por que acurácia é enganosa sob classes desbalanceadas; reconhecer sobreajuste comparando desempenho em treino e teste à medida que a complexidade do modelo aumenta; e executar e interpretar uma validação cruzada k-fold com `cross_val_score`.
**Pré-requisito:** [[24-machine-learning-geociencias-aula-03-modelagem-supervisionada-regressao|Aula 03]], [[24-machine-learning-geociencias-aula-04-modelagem-supervisionada-classificacao|Aula 04]] e [[24-machine-learning-geociencias-aula-05-modelagem-nao-supervisionada-agrupamento-reducao-dimensionalidade|Aula 05]] (as métricas MAE/RMSE/R² e acurácia já apareceram ali sem definição formal; esta aula fecha essa lacuna). [[20-geoestatistica/20-geoestatistica-aula-05-krigagem-simples-ordinaria|Módulo 20, Aula 05]] para a validação cruzada *leave-one-out* da krigagem.

## Conteúdo

### Métricas de regressão: revisitando MAE, RMSE e R²

A Aula 03 já usou três métricas de regressão sem defini-las com rigor — esta seção fecha essa lacuna antes de avançar para classificação. Dado um conjunto de valores observados $y_i$ e previstos $\hat y_i$ no conjunto de teste:

O **erro absoluto médio** (*mean absolute error*, MAE) é a média dos erros em valor absoluto: $\text{MAE} = \frac{1}{n}\sum_i |y_i - \hat y_i|$ — está na mesma unidade do rótulo (ppb de ouro, neste módulo) e é diretamente interpretável como "em média, a previsão erra por tantas unidades".

A **raiz do erro quadrático médio** (*root mean squared error*, RMSE) eleva cada erro ao quadrado antes de tirar a média e depois extrai a raiz: $\text{RMSE} = \sqrt{\frac{1}{n}\sum_i (y_i - \hat y_i)^2}$. Elevar ao quadrado penaliza erros grandes desproporcionalmente mais do que erros pequenos — por isso o RMSE é sempre maior ou igual ao MAE para o mesmo conjunto de previsões, e a diferença entre os dois cresce quando há alguns erros muito maiores que os demais (a Aula 03 observou exatamente isso: RMSE = 6,759 contra MAE = 5,128 para a regressão linear, uma diferença de 1,6 ppb sinalizando que pelo menos algumas previsões erraram bem mais do que a média).

O **coeficiente de determinação** ($R^2$) compara o erro do modelo com o erro de um modelo trivial que sempre prevê a média de $y$: $R^2 = 1 - \frac{\sum_i (y_i-\hat y_i)^2}{\sum_i (y_i - \bar y)^2}$. $R^2=1$ significa previsão perfeita; $R^2=0$ significa que o modelo não é melhor do que prever a média para toda amostra; $R^2$ negativo (que vai aparecer na Aula 07) significa que o modelo é **pior** do que essa previsão trivial — um sinal inequívoco de modelo malajustado.

### Métricas de classificação: a matriz de confusão

Para classificação, o ponto de partida é a **matriz de confusão**: uma tabela que cruza a classe prevista com a classe real. Para duas classes (aqui, `anomalo` = 1 e `background` = 0), ela tem quatro células.

**Continuidade de código.** Os blocos desta aula reaproveitam o ambiente das **Aulas 03 e 04**, com os nomes de lá: `X` (as seis variáveis) e `y` (o alvo de **regressão**, `Au_ppb`) vêm da Aula 03; `y2` (o alvo de **classificação**, `anomalo`), a partição **estratificada** `X_train2`/`X_test2`/`y_train2`/`y_test2` e as previsões `pred_logit` (regressão logística) vêm da Aula 04. Rode as duas antes, na mesma sessão — usar por engano os nomes da partição de regressão (`y_train`, `y_test`, `pred`) nas tarefas de classificação abaixo não dá número errado, dá erro: o scikit-learn recusa um alvo contínuo num classificador (`ValueError: Unknown label type: continuous`).

```python
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test2, pred_logit)
print(cm)
```

**Saída esperada**, para a regressão logística da Aula 04: `[[4, 1], [1, 9]]`. A convenção do scikit-learn organiza a matriz como `[[TN, FP], [FN, TP]]`: **TN** (verdadeiro negativo) = background corretamente previsto como background (4 amostras); **FP** (falso positivo) = background previsto incorretamente como anômalo (1 amostra); **FN** (falso negativo) = anômalo previsto incorretamente como background (1 amostra); **TP** (verdadeiro positivo) = anômalo corretamente previsto como anômalo (9 amostras). Todas as demais métricas de classificação desta aula se calculam a partir dessas quatro contagens.

**Acurácia**, a métrica mais intuitiva, é a fração de previsões corretas: $\text{acc} = \frac{TP+TN}{TP+TN+FP+FN} = \frac{9+4}{15} = 0{,}867$ — bate com o valor já usado na Aula 04. Mas a acurácia trata os dois tipos de erro (falso positivo e falso negativo) como igualmente custosos, e mistura numa única fração o desempenho nas duas classes, escondendo desequilíbrios — o problema central que a Aula 01 já havia anunciado ao discutir classes desbalanceadas.

**Precisão** (*precision*) responde: das amostras que o modelo previu como anômalas, quantas realmente são? $\text{precisão} = \frac{TP}{TP+FP} = \frac{9}{9+1} = 0{,}900$. **Revocação** (*recall*, também chamada sensibilidade) responde a pergunta complementar: das amostras que realmente são anômalas, quantas o modelo capturou? $\text{revocação} = \frac{TP}{TP+FN} = \frac{9}{9+1} = 0{,}900$ (coincidem neste exemplo porque FP = FN = 1, mas em geral são diferentes). O **F1-score** resume as duas numa única métrica, pela média harmônica (que penaliza mais um desequilíbrio entre as duas do que a média aritmética faria): $F1 = 2 \cdot \frac{\text{precisão}\cdot\text{revocação}}{\text{precisão}+\text{revocação}} = 0{,}900$.

```python
from sklearn.metrics import classification_report
print(classification_report(y_test2, pred_logit, digits=3))
```

**Saída esperada:** o relatório completo confirma precisão = 0,900, revocação = 0,900 e F1 = 0,900 para a classe 1 (anômalo, 10 amostras de suporte no teste), e precisão = 0,800, revocação = 0,800 e F1 = 0,800 para a classe 0 (background, 5 amostras de suporte) — a acurácia global (0,867, no meio das duas) esconde que o modelo é visivelmente mais confiável identificando anomalias do que confirmando background, uma distinção que só aparece quando as métricas são olhadas por classe.

**Por que a acurácia sozinha engana sob desbalanceamento.** É o cenário que a Aula 01 anunciou, e o exemplo trabalhado desta aula o percorre com números. O que importa retê-lo agora é o motivo pelo qual precisão, revocação e F1 são indispensáveis em geociências: a classe de interesse econômico ou de risco costuma ser a **rara**, e é sobre ela que a revocação (não deixar passar um depósito real, ou uma zona de risco geotécnico real) e a precisão (não gerar alarme falso demais para justificar o custo de investigação) precisam ser avaliadas separadamente da acurácia global.

### Sobreajuste: quando o modelo decora em vez de aprender

**Sobreajuste** (*overfitting*) acontece quando um modelo se ajusta tão de perto ao ruído específico do conjunto de treino que perde capacidade de generalizar para dado novo — o sintoma característico é um desempenho excelente no treino e visivelmente pior no teste. O oposto, **subajuste** (*underfitting*), acontece quando o modelo é simples demais para captar até o padrão real presente nos dados, errando em treino e teste por igual. O diagnóstico prático é sempre o mesmo: **comparar o desempenho no treino com o desempenho no teste**, nunca julgar um modelo só pelo desempenho no treino.

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

for depth in [1, 2, 3, 5, None]:
    tree = DecisionTreeClassifier(max_depth=depth, random_state=42).fit(X_train2, y_train2)
    acc_train = accuracy_score(y_train2, tree.predict(X_train2))
    acc_test = accuracy_score(y_test2, tree.predict(X_test2))
    print(depth, round(acc_train, 3), round(acc_test, 3))
```

**Saída esperada:** para `max_depth=1` e `max_depth=2`, acurácia de treino **0,911** e de teste **0,933** — as duas próximas (teste ligeiramente acima do treino, plausível em amostra pequena, sem sinal de sobreajuste). Mas a partir de `max_depth=3` — e para `max_depth=5` e `max_depth=None` (sem limite de profundidade), os três resultados **idênticos** — a acurácia de treino salta para **1,000** (a árvore memoriza perfeitamente as 45 amostras de treino) enquanto a acurácia de teste **despenca para 0,533** — um `gap` de quase 47 pontos percentuais entre treino e teste, o retrato mais claro possível de sobreajuste: a árvore parou de aprender um padrão geral e passou a decorar particularidades (inclusive o ruído de rótulo de 12% introduzido na Aula 02) do conjunto específico de treino. O fato de profundidade 3, 5 e "sem limite" darem exatamente o mesmo resultado indica que, com apenas 45 amostras e seis variáveis, a árvore já atinge acurácia de treino perfeita numa profundidade relativamente baixa — aumentar ainda mais a profundidade não piora nem melhora, simplesmente não há mais nó para dividir de forma útil.

A lição estrutural, que reaparece com força total na Aula 07: **modelos com muita capacidade de ajuste, combinados com poucos dados de treino, são o cenário clássico de sobreajuste** — e conjuntos de dados geológicos rotulados pequenos (Aula 01) tornam esse risco uma regra, não uma exceção, em projetos reais de aprendizado de máquina aplicado à geologia.

### Validação cruzada: uma estimativa mais robusta do que um único teste

Até aqui, cada modelo foi avaliado numa **única** divisão treino/teste (a da Aula 02) — mas essa única divisão é, ela mesma, produto de um sorteio, e uma partição “de sorte” (fácil demais ou difícil demais) pode distorcer a avaliação, como o exemplo de três amostras da Aula 03 já ilustrou em miniatura. A **validação cruzada k-fold** (*k-fold cross-validation*) generaliza a validação *leave-one-out* já vista para krigagem no Módulo 20 (Aula 05): em vez de deixar de fora uma única amostra por vez, o conjunto de dados inteiro é dividido em $k$ partes (*folds*) de tamanho aproximadamente igual; o modelo é treinado $k$ vezes, cada vez usando $k-1$ partes como treino e a parte restante como teste, alternando qual parte fica de fora; e o desempenho final é resumido pela média (e desvio-padrão) das $k$ métricas obtidas — o *leave-one-out* do Módulo 20 é, na prática, o caso extremo de k-fold em que $k$ é igual ao número de amostras.

```python
from sklearn.model_selection import KFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier

kf = KFold(n_splits=5, shuffle=True, random_state=42)
rfc = RandomForestClassifier(n_estimators=300, random_state=42)
scores = cross_val_score(rfc, X, y2, cv=kf, scoring="accuracy")
print(np.round(scores, 3), round(scores.mean(), 3), round(scores.std(), 3))
```

**Saída esperada:** cinco acurácias, uma por *fold* — **0,917; 0,917; 0,833; 0,833; 0,833** — com média **0,867** e desvio-padrão **0,041**. Note que `cross_val_score` recebe **todo** o conjunto `X, y2` (60 amostras), não apenas o treino: cada rodada gira qual quinto fica de fora, o que é uma forma diferente — e tipicamente mais estável, por usar mais dados no total — de estimar desempenho. A média (0,867) fica **abaixo** da acurácia que a mesma floresta obteve na Aula 04 sobre a divisão única (0,933) — e, mais que isso, aquele 0,933 é maior do que o resultado de **qualquer um** dos cinco *folds* (o melhor deles foi 0,917). Ou seja: a partição da Aula 02 calhou de ser favorável àquele modelo, exatamente o mesmo fenômeno que o exemplo de regressão logo abaixo mostra de forma ainda mais nítida. O desvio-padrão (0,041) é a informação nova e importante: ele quantifica **quanto o desempenho varia** dependendo de qual subconjunto é usado como teste — uma única medida de acurácia, sem essa faixa de variação, dá uma falsa sensação de precisão sobre quão bom o modelo realmente é.

O mesmo mecanismo se aplica a regressão, trocando a métrica — e trocando o alvo, que aqui volta a ser `y` (o `Au_ppb` da Aula 03), não `y2`:

```python
from sklearn.linear_model import LinearRegression
scores_mae = cross_val_score(LinearRegression(), X, y, cv=kf, scoring="neg_mean_absolute_error")
print(np.round(-scores_mae, 3), round(-scores_mae.mean(), 3))
```

**Saída esperada:** MAE por *fold* de **6,235; 6,947; 7,215; 6,304; 7,527**, com média **6,846** ppb — mais alto do que o MAE de 5,128 ppb obtido na Aula 03 sobre a divisão única, um lembrete concreto de que uma única divisão treino/teste pode, por sorteio, favorecer a avaliação (o `scoring` do scikit-learn usa o prefixo `neg_` por convenção interna, porque a API de validação cruzada sempre trata "maior é melhor"; multiplicar por −1, como feito acima, devolve o MAE na sua forma usual). **Aviso de continuidade com a Aula 02**: este `KFold` embaralha as amostras aleatoriamente (`shuffle=True`) antes de dividir em partes — adequado aqui porque este conjunto de dados não carrega coordenadas espaciais explícitas, mas, para um conjunto real com posição geográfica conhecida, a mesma advertência de vazamento espacial da Aula 02 se aplica à validação cruzada tanto quanto ao particionamento único: a correção seria substituir `KFold` por uma validação cruzada em **blocos espaciais** (por exemplo, `GroupKFold` do scikit-learn usando um identificador de bloco geográfico em vez de sorteio amostra a amostra), garantindo que nenhum bloco de teste contenha vizinhos imediatos de um bloco de treino.

## Exemplo trabalhado

**Situação:** um colega de equipe reporta "meu classificador de risco geotécnico teve 96% de acurácia" e propõe usá-lo para triagem automática de encostas. Antes de aprovar, você pede a matriz de confusão: de 200 encostas de teste, 8 são de fato instáveis (classe rara, 4% do total) e 192 são estáveis; o modelo previu "estável" para as 200 encostas.

**Resolução.** Recalculando a acurácia: $\text{acc} = 192/200 = 0{,}96$ — o modelo de fato acerta 96%, confirmando o número reportado, mas a matriz de confusão revela o que a acurácia sozinha esconde: TP = 0 (nenhuma encosta instável foi identificada como tal), FN = 8 (todas as 8 encostas realmente instáveis foram classificadas erradamente como estáveis), TN = 192, FP = 0. A revocação da classe de interesse (instável) é $TP/(TP+FN) = 0/8 = 0$ — o modelo **nunca** identifica uma encosta instável real, apesar da acurácia alta, porque simplesmente prevê a classe majoritária para tudo (o mesmo padrão de degeneração já ilustrado na seção de matriz de confusão acima, agora com números concretos). A precisão da classe instável é indefinida (0/0, porque TP+FP=0 — nenhuma previsão positiva foi feita) e o F1 da classe instável é 0. **Conclusão:** o modelo é inútil para o propósito declarado (triagem de risco) apesar da acurácia alta, e não deveria ser aprovado sem, no mínimo, reportar revocação e F1 da classe instável — e, dado o desbalanceamento severo (4% de instáveis), provavelmente sem técnicas específicas para classes desbalanceadas (reponderação de classes, reamostragem, ou um limiar de decisão diferente de 0,5), nenhuma delas coberta em profundidade neste módulo introdutório, mas necessárias antes de qualquer uso prático de um classificador nesse regime.

## Recap relâmpago

- **MAE**, **RMSE** e **R²** medem erro de regressão em unidades diferentes: MAE é o erro médio absoluto; RMSE penaliza mais os erros grandes (sempre ≥ MAE); R² compara o modelo com a previsão trivial da média (1 = perfeito, 0 = igual à média, negativo = pior que a média).
- A **matriz de confusão** (`[[TN,FP],[FN,TP]]`) é a base de toda métrica de classificação: **acurácia** = acertos totais; **precisão** = dos previstos positivos, quantos são de fato; **revocação** = dos positivos reais, quantos foram capturados; **F1** = média harmônica de precisão e revocação.
- **Acurácia sozinha engana sob classes desbalanceadas** — um modelo que sempre prevê a classe majoritária pode ter acurácia alta e revocação zero na classe de interesse, o cenário mais perigoso em geociências, onde a classe rara costuma ser a economicamente ou ambientalmente relevante.
- **Sobreajuste** é diagnosticado comparando desempenho em treino e teste: um `gap` grande (como o salto de acurácia de teste de 0,933 para 0,533 ao aumentar a profundidade de uma árvore, enquanto o treino vai a 1,000) é o sintoma característico; modelos com muita capacidade e poucos dados de treino são o cenário clássico.
- **Validação cruzada k-fold** generaliza o *leave-one-out* de krigagem (Módulo 20) para aprendizado de máquina: treina e testa $k$ vezes, alternando qual fatia fica de fora, e resume o desempenho por média **e** desvio-padrão — a variação entre *folds* é informação tão importante quanto a média. Para dados com estrutura espacial, `GroupKFold` por blocos geográficos evita o mesmo vazamento de informação já advertido no particionamento simples (Aula 02).

## Próxima aula

[[24-machine-learning-geociencias-aula-07-deep-learning-aplicacoes-estudos-caso|Aula 07 — Deep learning e aplicações: redes neurais, estudos de caso com dados reais, interpretação e comunicação dos resultados]] — usa exatamente o diagnóstico de sobreajuste desta aula para explicar por que uma rede neural, com muita capacidade e poucos dados, pode desempenhar pior do que a regressão linear da Aula 03.

## Fontes

- Definições formais de MAE, RMSE e R² para avaliação de regressão: Hastie, T., Tibshirani, R. & Friedman, J., *The Elements of Statistical Learning*, 2ª ed. (2009), Springer, cap. 7; documentação oficial scikit-learn, módulo `sklearn.metrics` (scikit-learn.org), versão 1.9.
- Matriz de confusão, acurácia, precisão, revocação e F1-score, e o problema de classes desbalanceadas: Géron, A., *Hands-On Machine Learning with Scikit-Learn, Keras and TensorFlow*, 3ª ed. (2022), O'Reilly, cap. 3.
- Sobreajuste e subajuste como o compromisso entre viés e variância (*bias-variance tradeoff*): Hastie, Tibshirani & Friedman, cap. 2.9 e 7.2-7.3.
- Validação cruzada k-fold, sua relação com *leave-one-out*, e `GroupKFold`/blocagem espacial para dados não independentes: documentação oficial scikit-learn, módulo `sklearn.model_selection` (scikit-learn.org), versão 1.9; Roberts, D. R. et al. (2017), "Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure", *Ecography*, 40(8), 913-929, DOI 10.1111/ecog.02881; retomando [[20-geoestatistica/20-geoestatistica-aula-05-krigagem-simples-ordinaria|Módulo 20, Aula 05]] deste curso.

<!--
nivel: avancado
palavras_corpo: 2480
mapa_objetivo_secao:
  geologia-avancado-m24-oa04: "Métricas de regressão: revisitando MAE, RMSE e R²" + "Métricas de classificação: a matriz de confusão" + "Sobreajuste: quando o modelo decora em vez de aprender" + "Validação cruzada: uma estimativa mais robusta do que um único teste" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: MLGEO-M24-A05-METRICAS-FORMULAS-001
    claim: "MAE = media dos erros absolutos (1/n * soma de |y_i - yhat_i|); RMSE = raiz da media dos erros quadraticos (raiz de (1/n * soma de (y_i-yhat_i)^2)), sempre maior ou igual ao MAE para o mesmo conjunto de previsoes; R2 = 1 - (soma dos quadrados dos residuos)/(soma dos quadrados totais em relacao a media de y), valendo 1 para previsao perfeita, 0 quando o modelo equivale a prever a media, e podendo ser negativo quando o modelo e pior que essa previsao trivial."
    risk: fato
    source: "Hastie, T., Tibshirani, R. & Friedman, J., The Elements of Statistical Learning, 2a ed. (2009), Springer, cap. 7; documentacao oficial scikit-learn, funcoes mean_absolute_error, mean_squared_error e r2_score (scikit-learn.org), versao 1.9."
  - claim_id: MLGEO-M24-A05-MATRIZ-CONFUSAO-METRICAS-002
    claim: "Para a regressao logistica da Aula 04 sobre o conjunto de teste desta aula (15 amostras, mesma particao), a matriz de confusao e [[4,1],[1,9]] no formato [[TN,FP],[FN,TP]], dando acuracia=(9+4)/15=0.867, precisao=9/(9+1)=0.900, revocacao=9/(9+1)=0.900 e F1=2*(0.9*0.9)/(0.9+0.9)=0.900; o relatorio de classificacao completo (classification_report) da precisao=0.800, revocacao=0.800 e F1=0.800 para a classe 0 (5 amostras de suporte) e precisao=0.900, revocacao=0.900, F1=0.900 para a classe 1 (10 amostras de suporte)."
    risk: calculo
    source: "Execucao direta do codigo apresentado na aula sobre os mesmos dados e particao da Aula 04 (scikit-learn 1.9.1). CONFIRMADO POR EXECUCAO em 2026-09-20: confusion_matrix, accuracy_score, precision_score, recall_score, f1_score e classification_report reproduzidos digito a digito com os valores relatados no texto."
  - claim_id: MLGEO-M24-A05-SOBREAJUSTE-ARVORE-003
    claim: "Para DecisionTreeClassifier(random_state=42) treinada e testada na mesma particao desta aula (45 treino, 15 teste), a acuracia de treino/teste e, respectivamente, 0.911/0.933 para max_depth=1, 0.911/0.933 para max_depth=2, e 1.000/0.533 para max_depth=3, max_depth=5 e max_depth=None (os tres ultimos identicos entre si) - um salto de gap de -0.022 (teste levemente acima do treino) para +0.467 (treino perfeito, teste bem pior) ao aumentar a profundidade de 2 para 3."
    risk: calculo
    source: "Execucao direta do codigo apresentado na aula (scikit-learn 1.9.1). CONFIRMADO POR EXECUCAO em 2026-09-20: acuracias de treino e teste reproduzidas digito a digito para as cinco profundidades testadas, incluindo a identidade exata entre os resultados de depth=3, depth=5 e depth=None."
  - claim_id: MLGEO-M24-A05-CROSSVAL-CLASSIFICACAO-004
    claim: "cross_val_score(RandomForestClassifier(n_estimators=300, random_state=42), X, y, cv=KFold(n_splits=5, shuffle=True, random_state=42), scoring='accuracy') sobre o conjunto completo de 60 amostras produz as acuracias por fold 0.917, 0.917, 0.833, 0.833, 0.833, com media 0.867 e desvio-padrao 0.041. A acuracia de 0.933 obtida pela mesma floresta na divisao unica da Aula 02/03 e MAIOR que a de qualquer um dos cinco folds (o melhor e 0.917) e fica cerca de 1.6 desvios-padrao acima da media da validacao cruzada, indicando que aquela particao unica foi favoravel ao modelo - o mesmo fenomeno que o exemplo de regressao da secao seguinte mostra (MAE de 5.128 na divisao unica contra 6.846 na validacao cruzada)."
    risk: calculo
    source: "Execucao direta do codigo apresentado na aula (scikit-learn 1.9.1). CONFIRMADO POR EXECUCAO em 2026-09-20: scores por fold, media e desvio-padrao reproduzidos digito a digito (arredondados a 3 casas)."
  - claim_id: MLGEO-M24-A05-CROSSVAL-REGRESSAO-005
    claim: "cross_val_score(LinearRegression(), X, Au_ppb, cv=KFold(n_splits=5, shuffle=True, random_state=42), scoring='neg_mean_absolute_error') sobre o conjunto completo produz MAE por fold de 6.235, 6.947, 7.215, 6.304 e 7.527, com media 6.846 ppb - mais alto que o MAE de 5.128 ppb obtido na Aula 03 sobre a unica divisao treino/teste daquela aula."
    risk: calculo
    source: "Execucao direta do codigo apresentado na aula (scikit-learn 1.9.1). CONFIRMADO POR EXECUCAO em 2026-09-20: MAE por fold e media reproduzidos digito a digito (arredondados a 3 casas)."
  - claim_id: MLGEO-M24-A05-KFOLD-LEAVEONEOUT-006
    claim: "A validacao cruzada leave-one-out (deixar uma amostra de fora por vez, usada para krigagem no Modulo 20) e um caso particular da validacao cruzada k-fold em que o numero de dobras k e igual ao numero total de amostras do conjunto de dados."
    risk: fato
    source: "Documentacao oficial scikit-learn, modulo sklearn.model_selection, comparacao entre KFold e LeaveOneOut (scikit-learn.org), versao 1.9; Hastie, Tibshirani & Friedman, The Elements of Statistical Learning, 2a ed. (2009), Springer, secao 7.10."
  - claim_id: MLGEO-M24-A05-EXEMPLO-ACURACIA-ENGANOSA-007
    claim: "Para um cenario hipotetico de 200 encostas de teste (8 instaveis, 192 estaveis) em que um modelo preve 'estavel' para todas, a acuracia e 192/200=0.96, mas a revocacao da classe instavel e TP/(TP+FN)=0/8=0 (nenhuma encosta instavel real e identificada) e a precisao da classe instavel e indefinida (0/0, pois nenhuma previsao positiva foi feita), demonstrando que uma acuracia alta pode coexistir com revocacao nula na classe de interesse quando ha desbalanceamento severo de classes."
    risk: calculo
    source: "Calculo aritmetico direto a partir dos numeros hipoteticos do cenario apresentado na aula (192/200=0.96; 0/8=0), consistente com a definicao formal de acuracia, precisao e revocacao ja estabelecida nesta aula."
  - claim_id: MLGEO-M24-A05-NAMESPACE-CONTINUIDADE-008
    claim: "Os cinco blocos de codigo desta aula nao redefinem dados nem particoes: eles rodam no ambiente das Aulas 03 e 04 e usam os nomes de lá. As tarefas de CLASSIFICACAO desta aula (matriz de confusao, classification_report, arvores de decisao, validacao cruzada de acuracia) exigem a particao ESTRATIFICADA da Aula 04 (X_train2/X_test2/y_train2/y_test2, alvo y2=anomalo, previsao pred_logit); a validacao cruzada de REGRESSAO exige X e y=Au_ppb. Usar os nomes da particao de regressao (y_train/y_test/pred) nas tarefas de classificacao NAO produz numero errado: produz erro de execucao (ValueError 'continuous is not supported' em confusion_matrix e classification_report; 'Unknown label type: continuous' em DecisionTreeClassifier.fit e em cross_val_score com scoring='accuracy')."
    risk: calculo
    source: "Execucao direta dos cinco blocos da aula sobre o namespace declarado das Aulas 03 e 04 (Python 3.13.2, scikit-learn 1.9.1). CONFIRMADO POR EXECUCAO em 2026-09-21: os quatro blocos de classificacao levantaram ValueError e o quinto levantou NameError ('y_reg' nunca e definido nas Aulas 02 a 05 - so aparece na Aula 07); com os nomes corretos, as cinco saidas declaradas na aula se reproduzem digito a digito. ACHADO 10 DA AUDITORIA de 2026-09-21 (corrigido: nomes ajustados nos cinco blocos e nota de continuidade de codigo acrescentada)."
-->
