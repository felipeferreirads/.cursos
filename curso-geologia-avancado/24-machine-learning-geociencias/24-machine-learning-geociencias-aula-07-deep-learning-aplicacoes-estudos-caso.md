# Aula 07: Deep learning e aplicações — redes neurais, estudos de caso com dados reais, interpretação e comunicação dos resultados

**ID:** geologia-avancado-m24-a07
**Módulo:** [[24-machine-learning-geociencias-modulo|Módulo 24 — Fundamentos e aplicações de machine learning em geociências]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** apresentar a rede neural artificial como o modelo central do aprendizado profundo, treinar uma rede simples (perceptron multicamadas) para classificação e para regressão sobre os dados deste módulo, e fechar o módulo mostrando — com um resultado concreto de sobreajuste severo — como interpretar e comunicar as limitações de um modelo, não só o seu desempenho.
**Ao final você vai conseguir:** descrever a arquitetura mínima de uma rede neural (camadas, pesos, função de ativação) e por que a padronização de variáveis é ainda mais crítica para redes neurais do que foi para K-means; treinar um `MLPClassifier`/`MLPRegressor` no scikit-learn; comparar a contagem de parâmetros de uma rede com o tamanho do conjunto de treino para antecipar risco de sobreajuste; usar importância por permutação para interpretar um modelo que não expõe coeficientes nem `feature_importances_`; e redigir uma comunicação de resultado que declare explicitamente as limitações do modelo, não só a métrica de desempenho.
**Pré-requisito:** [[24-machine-learning-geociencias-aula-06-avaliacao-desempenho-sobreajuste-validacao|Aula 06 — Avaliação de desempenho, sobreajuste e validação]] (o diagnóstico de sobreajuste construído ali é aplicado diretamente ao resultado desta aula).

## Conteúdo

### O que é uma rede neural artificial

Uma **rede neural artificial** organiza o cálculo em **camadas** de unidades simples chamadas **neurônios**: a **camada de entrada** recebe as variáveis explicativas (aqui, as mesmas seis variáveis geoquímicas e estruturais das Aulas 02 a 06); uma ou mais **camadas ocultas** (*hidden layers*) transformam essa entrada progressivamente; e a **camada de saída** produz a previsão (uma probabilidade, para classificação; um número, para regressão). Cada neurônio de uma camada oculta calcula uma combinação linear das saídas da camada anterior — pesos multiplicando cada entrada, mais um termo de viés (*bias*), exatamente como o $\beta_0 + \beta_1 x_1 + \dots$ da regressão linear da Aula 03 — e então aplica uma **função de ativação não linear** a esse resultado antes de repassá-lo adiante. A função de ativação é o ingrediente que faz a rede ser mais do que uma sequência de regressões lineares empilhadas (que, sem ela, colapsaria algebricamente numa única regressão linear, não importa quantas camadas); a mais usada hoje em camadas ocultas é a **ReLU** (*rectified linear unit*, $f(x)=\max(0,x)$), simples e eficiente de treinar. Os pesos de todas as camadas são ajustados por **retropropagação do erro** (*backpropagation*) combinada com um algoritmo de descida de gradiente estocástica: a rede faz uma previsão, mede o erro em relação ao rótulo verdadeiro, e propaga esse erro de volta pelas camadas ajustando cada peso na direção que mais reduz o erro — repetindo esse ciclo por muitas iterações sobre o conjunto de treino.

O modelo mais simples dessa família — e o único praticado nesta aula — é o **perceptron multicamadas** (*multilayer perceptron*, MLP): uma rede totalmente conectada (cada neurônio de uma camada se conecta a todos os da camada seguinte), sem a estrutura especializada de outras arquiteturas de aprendizado profundo mais avançadas, como as **redes neurais convolucionais** (especializadas em imagem — mencionadas na Aula 01 como a ferramenta natural para classificar fotografias de testemunho) ou as **redes recorrentes** (especializadas em sequências, como um log de sondagem ao longo da profundidade). O MLP já é suficiente para ilustrar o comportamento central que esta aula quer demonstrar: como redes neurais se comportam diante de dados tabulares pequenos, o cenário mais comum em projetos geológicos reais.

### Por que a padronização importa ainda mais aqui

A Aula 05 já exigiu padronização para K-means, por causa da distância euclidiana. Para redes neurais, a padronização é ainda mais decisiva, por um motivo adicional: o algoritmo de descida de gradiente que ajusta os pesos é sensível à **escala** das variáveis de entrada — sem padronização, uma variável de escala grande (`Cu_ppm`, na casa das centenas) domina o gradiente inicial e pode fazer o treinamento convergir mal ou lentamente, mesmo que a variável não seja mais informativa do que outra de escala pequena (`As_ppm`, na casa das unidades).

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("geoquimica.csv")
df["As_ppm"] = df["As_ppm"].fillna(df["As_ppm"].median())
df_enc = pd.get_dummies(df, columns=["litologia"], drop_first=True)
feat_cols = ["dist_falha_m", "cota_m", "Cu_ppm", "As_ppm", "Zn_ppm", "litologia_xisto"]
X, y = df_enc[feat_cols], df_enc["anomalo"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

mlp_sem = MLPClassifier(hidden_layer_sizes=(8,), max_iter=3000, random_state=42).fit(X_train, y_train)
print("SEM padronizacao, acuracia teste:", round(accuracy_score(y_test, mlp_sem.predict(X_test)), 3))

scaler = StandardScaler().fit(X_train)
Xtr_s, Xte_s = scaler.transform(X_train), scaler.transform(X_test)
mlp = MLPClassifier(hidden_layer_sizes=(8,), activation="relu", max_iter=3000, random_state=42).fit(Xtr_s, y_train)
print("COM padronizacao, acuracia teste:", round(accuracy_score(y_test, mlp.predict(Xte_s)), 3))
```

**Saída esperada:** **0,333** de acurácia sem padronização — pior do que simplesmente chutar a classe majoritária (que daria 0,667, pois 10 das 15 amostras de teste são anômalas) — contra **0,867** com padronização. A diferença não é sutil: é o intervalo entre um modelo inutilizável e um modelo competitivo com os das Aulas 03, 04 e 06. `hidden_layer_sizes=(8,)` define uma única camada oculta com 8 neurônios; `activation="relu"` fixa a função de ativação já descrita; `max_iter=3000` limita o número de iterações do treinamento.

### Estudo de caso 1: classificação — desempenho competitivo, mas não superior

```python
from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=300, random_state=42).fit(X_train, y_train)
print("RandomForest, acuracia teste:", round(accuracy_score(y_test, rfc.predict(X_test)), 3))
print("MLP, acuracia treino:", round(accuracy_score(y_train, mlp.predict(Xtr_s)), 3))
```

**Saída esperada:** a floresta aleatória (já vista nas Aulas 04 e 06) alcança **0,933** de acurácia de teste, contra **0,867** do MLP — o MLP fica *atrás* do método mais simples, embora não por muito. A acurácia de **treino** do MLP é **1,000**: a rede memoriza perfeitamente as 45 amostras de treino, um gap de 13,3 pontos percentuais para o teste — sobreajuste real, mas moderado, na escala da Aula 06 (compare com o salto de quase 47 pontos da árvore profunda). A contagem de parâmetros ajuda a entender por quê: uma rede com 6 entradas, 8 neurônios ocultos e 1 saída tem $6\times8 + 8 + 8\times1 + 1 = 65$ parâmetros ajustáveis (pesos e vieses de cada camada) — bem mais do que os 7 parâmetros da regressão logística da Aula 04 (6 coeficientes + 1 intercepto), mas ainda da mesma ordem de grandeza que as 45 amostras de treino, o suficiente para memorizar mas não tão desproporcional a ponto de colapsar completamente no teste.

### Estudo de caso 2: regressão — quando mais capacidade piora o resultado

O segundo estudo de caso usa uma rede um pouco maior — duas camadas ocultas, de 16 e 8 neurônios — para prever `Au_ppb`, repetindo a tarefa de regressão da Aula 03:

```python
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression

y_reg = df_enc["Au_ppb"]
Xtr3, Xte3, ytr3, yte3 = train_test_split(X, y_reg, test_size=0.25, random_state=42)
scaler2 = StandardScaler().fit(Xtr3)
Xtr3_s, Xte3_s = scaler2.transform(Xtr3), scaler2.transform(Xte3)

mlp_reg = MLPRegressor(hidden_layer_sizes=(16, 8), max_iter=5000, random_state=42).fit(Xtr3_s, ytr3)
pred_test = mlp_reg.predict(Xte3_s)
pred_train = mlp_reg.predict(Xtr3_s)

print("MLP - R2 treino:", round(r2_score(ytr3, pred_train), 4), "| R2 teste:", round(r2_score(yte3, pred_test), 4))
print("MLP - MAE teste:", round(mean_absolute_error(yte3, pred_test), 3))

lr = LinearRegression().fit(Xtr3, ytr3)
print("Regressao linear (Aula 03) - R2 teste:", round(r2_score(yte3, lr.predict(Xte3)), 4))
```

**Saída esperada — o resultado central desta aula:** **R² de treino = 0,9991** (a rede praticamente decora as 45 amostras de treino) contra **R² de teste = −0,1208** — **negativo**, ou seja, pior do que simplesmente prever a média de `Au_ppb` para toda amostra de teste (Aula 06: R² negativo é o sintoma mais inequívoco de modelo malajustado que existe). O MAE de teste sobe para **12,716 ppb**, mais que o dobro do MAE de 5,128 ppb obtido pela regressão linear da Aula 03 **sobre a mesma tarefa**. Por que a discrepância é tão mais severa aqui do que na classificação: a rede de regressão, com duas camadas ocultas (16 e 8 neurônios), tem $6\times16+16+16\times8+8+8\times1+1 = 257$ parâmetros ajustáveis — para apenas **45 amostras de treino**, isto é, mais de 5 parâmetros por amostra. Não há informação suficiente nos dados para restringir 257 graus de liberdade de forma confiável. E a rede **não converge**: o treinamento termina por esgotar o limite de 5.000 iterações, e o scikit-learn imprime um `ConvergenceWarning` junto com os números acima — um aviso adicional, na própria saída, de que o ajuste está no limite. Ela para numa solução que reproduz o treino quase exatamente e generaliza mal. **Esta é a mesma lição da Aula 03 — "o modelo mais sofisticado não é automaticamente o melhor" — levada ao extremo**: entre os seis modelos treinados neste módulo (regressão linear, floresta de regressão, regressão logística, floresta de classificação, MLP de classificação, MLP de regressão), o de maior capacidade nominal (a rede de regressão, com 257 parâmetros) produziu o pior resultado **entre os três modelos de regressão** — e o único R² negativo de todo o módulo —, exatamente onde a razão parâmetros/amostras foi mais desfavorável. (Não existe ranking único dos seis: R² e acurácia medem coisas diferentes, e comparar regressão com classificação por "quem foi melhor" não é operação definida.)

### Interpretação: importância por permutação

Um MLP não expõe coeficientes (como a regressão) nem `feature_importances_` (como a floresta): os pesos internos, espalhados por camadas e neurônios, não têm leitura direta em termos de "quanto a variável X pesa". A **importância por permutação** (*permutation importance*) contorna isso de forma agnóstica ao modelo: embaralha os valores de uma variável por vez, mantendo as demais intactas, e mede o quanto o desempenho do modelo já treinado piora — queda grande indica dependência forte daquela variável.

```python
from sklearn.inspection import permutation_importance

result = permutation_importance(mlp, Xte_s, y_test, n_repeats=30, random_state=42, scoring="accuracy")
print(dict(zip(feat_cols, np.round(result.importances_mean, 3))))
```

**Saída esperada:** `Cu_ppm = 0,216` (a mais importante, coerente com a definição do rótulo `anomalo` a partir do cobre), `litologia_xisto = 0,104`, `As_ppm = 0,067`, `Zn_ppm = 0,047`, `cota_m = 0,027` e `dist_falha_m = −0,002` (praticamente nula, e o valor levemente negativo é ruído estatístico do processo de embaralhamento repetido, não um efeito real). O padrão qualitativo — `Cu_ppm` dominando, a variável geograficamente irrelevante (`cota_m`) entre as mais baixas — é consistente com o que a importância de variável das florestas (Aulas 03 e 04) já havia mostrado, ainda que os valores numéricos não sejam diretamente comparáveis entre os dois métodos (a importância de permutação mede queda de acurácia; `feature_importances_` da floresta mede outra quantidade, a redução de impureza nas divisões).

Há, porém, uma **divergência** que ensina mais do que a semelhança: `dist_falha_m`, a segunda mais importante nas duas florestas (0,240 na Aula 03; 0,261 na Aula 04), aqui é praticamente nula — e isso **não** significa que a distância à falha seja irrelevante. A causa é uma limitação documentada da técnica: quando duas variáveis são correlacionadas — e a distância à falha correlaciona r = −0,90 com o cobre (Aula 02) —, embaralhar uma delas não derruba o desempenho, porque o modelo recupera a mesma informação pela outra, e a permutação reporta valor baixo para **ambas**. É o coeficiente parcial pequeno da Aula 03 outra vez: "acrescenta pouco ao que as outras já dizem" não é "não tem relação com o alvo". Cada método tem o seu ponto cego — a impureza favorece variáveis contínuas sobre binárias, a permutação dilui as correlacionadas —, e é por isso que interpretar um modelo com uma única medida de importância é arriscado.

### Comunicar resultados com suas limitações

O objetivo geral deste módulo — "escolher o algoritmo, avaliar o desempenho e comunicar os resultados com suas limitações" — chega ao seu ponto mais concreto neste último estudo de caso: um relatório que reportasse apenas "MLP: MAE de X ppb" sem mencionar o R² negativo no teste, o tamanho da amostra ou a razão entre parâmetros e amostras estaria omitindo exatamente a informação que determina se o resultado é confiável. Uma comunicação adequada a um tomador de decisão (um geólogo sênior, um gerente de exploração) declara, no mínimo: **(1)** o modelo escolhido e por que — aqui, um MLP foi testado por completude pedagógica, não porque o problema exigisse uma rede neural; **(2)** o tamanho do conjunto usado (60 amostras, 45 de treino) e por que isso limita a complexidade recomendável; **(3)** a métrica no **teste**, nunca só no treino, com sua incerteza (o desvio-padrão de 0,041 da validação cruzada da Aula 06 é o tipo de informação que deve acompanhar qualquer número único); e **(4)** para que decisões o modelo é — e não é — adequado: um R² negativo em teste, como o do MLP de regressão desta aula, **veta** o uso do modelo para orientar sondagem adicional, e dizer isso é parte do trabalho tanto quanto treinar o modelo.

## Exemplo trabalhado

**Situação:** com os seis modelos treinados ao longo do módulo (Aulas 03, 04 e 07) sobre o mesmo conjunto de dados, monte uma tabela-resumo de desempenho de teste e decida qual recomendar para cada tarefa.

| Tarefa | Modelo | Métrica de teste | Fonte |
|---|---|---|---|
| Regressão (Au) | Regressão linear | R² = 0,7879, MAE = 5,128 | Aula 03 |
| Regressão (Au) | Floresta aleatória | R² = 0,7331, MAE = 5,778 | Aula 03 |
| Regressão (Au) | MLP (16, 8) | R² = −0,1208, MAE = 12,716 | Aula 07 |
| Classificação (anomalo) | Regressão logística | Acurácia = 0,867, F1 = 0,900 | Aulas 04 e 06 |
| Classificação (anomalo) | Floresta aleatória | Acurácia = 0,933 | Aula 04 |
| Classificação (anomalo) | MLP (8) | Acurácia = 0,867 | Aula 07 |

**Decisão e justificativa.** Para regressão, a **regressão linear** vence com folga — melhor R² e menor MAE entre os três, e além disso o modelo mais simples de explicar e de auditar, uma vantagem adicional que a tabela sozinha não captura, mas que pesa na recomendação prática. O MLP de regressão deveria ser **descartado** para esta tarefa, não porque redes neurais sejam ruins em geral, mas porque este conjunto de dados específico (45 amostras de treino) não sustenta um modelo de 257 parâmetros — a mesma tarefa, com milhares de amostras rotuladas, poderia favorecer a rede. Para classificação, a **floresta aleatória** tem a melhor acurácia (0,933), mas a Aula 04 já mostrou que essa vantagem é um único falso positivo, e a Aula 06, que ela não sobrevive à validação cruzada: antes de recomendar, faltam precisão/revocação por classe e k-fold. Uma tabela assim — desempenho no teste, vários modelos, mesma partição, limitação amostral declarada — é a síntese que fecha um projeto real, e encerra o arco que a Aula 02 abriu ao definir o problema.

## Recap relâmpago

- Uma **rede neural artificial** empilha camadas de neurônios que combinam entradas linearmente e aplicam uma **função de ativação não linear** (ReLU, a mais comum); os pesos são ajustados por **retropropagação** e descida de gradiente. O **perceptron multicamadas (MLP)** é a arquitetura mais simples dessa família; redes convolucionais (imagem) e recorrentes (sequência) são especializações fora do escopo deste módulo.
- A **padronização é ainda mais crítica para redes neurais** do que para K-means: sem ela, a acurácia do MLP de classificação caiu de 0,867 para 0,333 — pior do que prever a classe majoritária.
- Neste módulo, **nenhum dos dois MLPs superou os métodos mais simples**: o de classificação (0,867) perdeu para a floresta (0,933); o de regressão (R² = −0,12) foi pior que a regressão linear (R² = 0,79) e pior até do que prever a média — o resultado mais claro de sobreajuste de todo o módulo, produzido pela razão desfavorável entre parâmetros (257) e amostras de treino (45).
- **Importância por permutação** interpreta um modelo de caixa-preta (como o MLP, sem coeficientes nem `feature_importances_`) embaralhando cada variável e medindo a queda de desempenho — aqui, confirmou `Cu_ppm` como a variável dominante, coerente com as demais aulas. Mas ela **dilui variáveis correlacionadas**: `dist_falha_m` sai praticamente nula, apesar de ser a segunda mais importante nas florestas, porque o cobre carrega a mesma informação. Nenhuma medida de importância é neutra — a de impureza favorece variáveis contínuas, a de permutação penaliza as correlacionadas.
- **Comunicar um resultado de ML exige declarar suas limitações**, não só a métrica: o algoritmo escolhido e por quê, o tamanho da amostra, o desempenho no teste com sua incerteza, e para que decisões o modelo é ou não adequado — um R² negativo em teste é um veto, não um detalhe técnico a ser omitido.

## Fontes

- Arquitetura do perceptron multicamadas, funções de ativação (ReLU) e retropropagação: Goodfellow, I., Bengio, Y. & Courville, A., *Deep Learning* (2016), MIT Press, caps. 6 e 6.5 (retropropagação); Géron, A., *Hands-On Machine Learning with Scikit-Learn, Keras and TensorFlow*, 3ª ed. (2022), O'Reilly, caps. 10-11.
- Panorama de aprendizado profundo aplicado a geociências sólidas, incluindo o alerta sobre tamanho de conjuntos de dados rotulados: Bergen, K. J., Johnson, P. A., de Hoop, M. V. & Beroza, G. C. (2019), "Machine learning for data-driven discovery in solid Earth geoscience", *Science*, 363(6433), eaau0323, DOI 10.1126/science.aau0323.
- Razão entre número de parâmetros e tamanho da amostra como fator de risco de sobreajuste: Hastie, T., Tibshirani, R. & Friedman, J., *The Elements of Statistical Learning*, 2ª ed. (2009), Springer, caps. 2.9 e 11.
- Importância por permutação como método de interpretação agnóstico ao modelo: Breiman, L. (2001), "Random Forests", *Machine Learning*, 45(1), 5-32, DOI 10.1023/A:1010933404324 (origem do método); documentação oficial scikit-learn, módulo `sklearn.inspection.permutation_importance` (scikit-learn.org), versão 1.9.
- API scikit-learn para `MLPClassifier` e `MLPRegressor`, incluindo `hidden_layer_sizes`, `activation` e critérios de convergência (`max_iter`): documentação oficial scikit-learn (scikit-learn.org), versão 1.9.

<!--
nivel: avancado
palavras_corpo: 2514
mapa_objetivo_secao:
  geologia-avancado-m24-oa04: "O que é uma rede neural artificial" + "Por que a padronização importa ainda mais aqui" + "Estudo de caso 1: classificação — desempenho competitivo, mas não superior" + "Estudo de caso 2: regressão — quando mais capacidade piora o resultado" + "Interpretação: importância por permutação" + "Comunicar resultados com suas limitações" + "Exemplo trabalhado"
  geologia-avancado-m24-oa03: "O que é uma rede neural artificial" + "Estudo de caso 1: classificação — desempenho competitivo, mas não superior" + "Estudo de caso 2: regressão — quando mais capacidade piora o resultado"

alegacoes_auditaveis:
  - claim_id: MLGEO-M24-A06-REDE-NEURAL-CONCEITO-001
    claim: "Uma rede neural artificial (perceptron multicamadas) organiza o calculo em camada de entrada, uma ou mais camadas ocultas e camada de saida; cada neuronio calcula uma combinacao linear das saidas da camada anterior mais um termo de vies, seguida de uma funcao de ativacao nao linear (a ReLU, f(x)=max(0,x), e a mais comum em camadas ocultas); sem a nao linearidade da funcao de ativacao, uma sequencia de camadas lineares colapsaria algebricamente em uma unica transformacao linear equivalente. Os pesos sao ajustados por retropropagacao do erro combinada com descida de gradiente estocastica."
    risk: fato
    source: "Goodfellow, I., Bengio, Y. & Courville, A., Deep Learning (2016), MIT Press, caps. 6 e 6.5; Geron, A., Hands-On Machine Learning with Scikit-Learn, Keras and TensorFlow, 3a ed. (2022), O'Reilly, caps. 10-11."
  - claim_id: MLGEO-M24-A06-PADRONIZACAO-RESULTADO-002
    claim: "Treinando MLPClassifier(hidden_layer_sizes=(8,), max_iter=3000, random_state=42) sobre o conjunto de dados da aula (mesma particao da Aula 02/03) sem padronizacao previa das variaveis, a acuracia no teste e 0.333 - pior do que prever a classe majoritaria para toda amostra (que daria 0.667, pois 10 das 15 amostras de teste sao anomalas); com StandardScaler ajustado no treino e aplicado a treino e teste, a mesma arquitetura (agora com activation='relu' explicito) atinge acuracia de teste 0.867."
    risk: calculo
    source: "Execucao direta do codigo apresentado na aula (scikit-learn 1.9.1). CONFIRMADO POR EXECUCAO em 2026-09-20: acuracia sem padronizacao = 0.333, com padronizacao = 0.867, reproduzidas digito a digito; proporcao de anomalos no teste (10/15=0.667) ja confirmada na Aula 02/03."
  - claim_id: MLGEO-M24-A06-CLASSIFICACAO-COMPARACAO-003
    claim: "Sobre o mesmo conjunto de teste, RandomForestClassifier(n_estimators=300, random_state=42) obtem acuracia 0.933 (ja relatada na Aula 04), superando o MLPClassifier padronizado (0.867, ver claim 002); o MLP de classificacao obtem acuracia de treino 1.000, um gap de 0.133 em relacao ao teste. A rede tem 6 entradas, 1 camada oculta de 8 neuronios e 1 saida, totalizando 6*8+8+8*1+1=65 parametros ajustaveis (pesos e vieses), contra 45 amostras de treino."
    risk: calculo
    source: "Execucao direta do codigo apresentado na aula (scikit-learn 1.9.1). CONFIRMADO POR EXECUCAO em 2026-09-20: acuracia de treino do MLP = 1.000, contagem de parametros verificada somando o tamanho de mlp.coefs_ (formas (6,8) e (8,1)) e mlp.intercepts_ (formas (8,) e (1,)) = 65."
  - claim_id: MLGEO-M24-A06-REGRESSAO-SOBREAJUSTE-004
    claim: "Treinando MLPRegressor(hidden_layer_sizes=(16,8), max_iter=5000, random_state=42) sobre a tarefa de regressao de Au_ppb desta aula (mesma particao nao estratificada de 45 treino/15 teste usada na Aula 03), o modelo obtem R2 de treino 0.9991 e R2 de teste -0.1208 (negativo, indicando desempenho pior que prever a media do alvo para toda amostra de teste), com MAE de teste 12.716 ppb - mais do que o dobro do MAE de 5.128 ppb da regressao linear (Aula 03) na mesma tarefa. O treinamento atinge o limite de 5000 iteracoes sem convergencia total (ConvergenceWarning emitido pelo scikit-learn). A rede tem 6 entradas, camadas ocultas de 16 e 8 neuronios e 1 saida, totalizando 6*16+16+16*8+8+8*1+1=257 parametros ajustaveis, para 45 amostras de treino - mais de 5 parametros por amostra."
    risk: calculo
    source: "Execucao direta do codigo apresentado na aula (scikit-learn 1.9.1). CONFIRMADO POR EXECUCAO em 2026-09-20: R2 treino=0.9991, R2 teste=-0.1208, MAE teste=12.716, ConvergenceWarning emitido ao atingir max_iter=5000, contagem de parametros = 257 verificada somando mlp_reg.coefs_ e mlp_reg.intercepts_."
  - claim_id: MLGEO-M24-A06-PERMUTATION-IMPORTANCE-005
    claim: "A importancia por permutacao calculada sobre o MLPClassifier padronizado desta aula (n_repeats=30, random_state=42, scoring='accuracy', avaliada no conjunto de teste) da os valores aproximados Cu_ppm=0.216, litologia_xisto=0.104, As_ppm=0.067, Zn_ppm=0.047, cota_m=0.027 e dist_falha_m=-0.002 (proximo de zero, consistente com ausencia de efeito real, e o sinal negativo sendo ruido estatistico do processo de embaralhamento). A tecnica de importancia por permutacao mede a queda de desempenho do modelo quando os valores de uma variavel sao embaralhados aleatoriamente, mantendo as demais intactas, e e aplicavel a qualquer modelo treinado, ao contrario de feature_importances_ (especifico de modelos baseados em arvore) ou de coeficientes (especificos de modelos lineares)."
    risk: calculo
    source: "Execucao direta de sklearn.inspection.permutation_importance sobre o MLPClassifier desta aula (scikit-learn 1.9.1). CONFIRMADO POR EXECUCAO em 2026-09-20: importances_mean reproduzido digito a digito (arredondado a 3 casas) para as seis variaveis."
  - claim_id: MLGEO-M24-A06-RESUMO-SEIS-MODELOS-006
    claim: "Resumindo o desempenho de teste dos seis modelos treinados no modulo sobre o mesmo conjunto de dados: regressao de Au_ppb - regressao linear R2=0.7879/MAE=5.128 (Aula 03), floresta aleatoria R2=0.7331/MAE=5.778 (Aula 03), MLP(16,8) R2=-0.1208/MAE=12.716 (Aula 07); classificacao de anomalo - regressao logistica acuracia=0.867/F1=0.900 (Aulas 04 e 06), floresta aleatoria acuracia=0.933 (Aula 04), MLP(8) acuracia=0.867 (Aula 07). Em ambas as tarefas, o metodo de maior capacidade nominal nao produziu o melhor resultado: na regressao, o MLP teve o pior desempenho ENTRE OS TRES MODELOS DE REGRESSAO (e o unico R2 negativo do modulo), coincidindo com a razao mais desfavoravel entre parametros ajustaveis (257) e amostras de treino (45). Os seis modelos NAO sao ordenaveis num ranking unico: R2 (regressao) e acuracia (classificacao) nao sao metricas comensuraveis."
    risk: calculo
    source: "Compilacao direta dos resultados ja individualmente confirmados por execucao nas Aulas 03, 04, 06 e 07 deste modulo (ver claims MLGEO-M24-A03-REGRESSAO-LINEAR-RESULTADO-001, MLGEO-M24-A03-RANDOMFOREST-REGRESSAO-RESULTADO-002, MLGEO-M24-A03-CLASSIFICACAO-RESULTADO-003, MLGEO-M24-A05-MATRIZ-CONFUSAO-METRICAS-002, MLGEO-M24-A06-CLASSIFICACAO-COMPARACAO-003 e MLGEO-M24-A06-REGRESSAO-SOBREAJUSTE-004). ACHADO 14 DA AUDITORIA de 2026-09-21 restringiu o escopo da comparacao (ver MLGEO-M24-A06-COMPARACAO-METRICAS-009)."
  - claim_id: MLGEO-M24-A06-CONVERGENCIA-007
    claim: "O MLPRegressor(hidden_layer_sizes=(16,8), max_iter=5000, random_state=42) desta aula NAO converge: o treinamento termina por esgotar o limite de 5000 iteracoes (n_iter_ = 5000) e o scikit-learn emite um ConvergenceWarning, que aparece na saida junto com os resultados. Dizer que 'a rede converge' e incorreto; o correto e que ela para no limite de iteracoes, numa solucao que reproduz o treino quase exatamente (R2 de treino 0.9991) e generaliza mal (R2 de teste -0.1208). Os dois MLPClassifier da aula, por contraste, convergem antes do limite (n_iter_ = 2514 contra max_iter=3000) e nao emitem aviso."
    risk: calculo
    source: "Execucao direta do codigo da aula com captura explicita de avisos (scikit-learn 1.9.1). CONFIRMADO POR EXECUCAO em 2026-09-21: mlp_reg.n_iter_ = 5000 com ConvergenceWarning emitido; mlp.n_iter_ = 2514 sem aviso. ACHADO 12 DA AUDITORIA de 2026-09-21 (o corpo da aula dizia 'a rede converge' e a propria frase seguinte reconhecia o limite de iteracoes atingido - contradicao interna; a saida esperada tambem nao mencionava o aviso que o leitor vai ver na tela)."
  - claim_id: MLGEO-M24-A06-PERMUTACAO-CORRELACAO-008
    claim: "A importancia por permutacao DILUI a importancia de variaveis correlacionadas: quando duas variaveis sao correlacionadas e uma delas e embaralhada, o modelo continua tendo acesso a mesma informacao pela outra, e a tecnica reporta valor baixo para AMBAS, ainda que as duas sejam informativas. E isso, e nao irrelevancia, que explica dist_falha_m aparecer com importancia por permutacao praticamente nula (-0.002) no MLP desta aula, sendo que ela e a segunda variavel mais importante na floresta de regressao (0.240, Aula 03) e na de classificacao (0.261, Aula 04): dist_falha_m correlaciona r=-0.90 com Cu_ppm (Aula 02). Portanto a semelhanca entre os dois metodos de importancia e parcial, e a divergencia em dist_falha_m e esperada, nao anomala."
    risk: fato
    source: "Documentacao oficial scikit-learn, '5.2. Permutation feature importance', secao 'Misleading values on strongly correlated features' (scikit-learn.org/stable/modules/permutation_importance.html), versao 1.9.1, consultada em 2026-09-21: 'When two features are correlated and one of the features is permuted, the model still has access to the latter through its correlated feature. This results in a lower reported importance value for both features, though they might actually be important.' Valores -0.002, 0.240, 0.261 e r=-0.90 confirmados por execucao. ACHADO 13 DA AUDITORIA de 2026-09-21 (a aula declarava o padrao 'consistente' com a floresta e omitia a divergencia mais visivel e sua causa)."
  - claim_id: MLGEO-M24-A06-COMPARACAO-METRICAS-009
    claim: "Os seis modelos treinados no modulo nao podem ser ordenados num ranking unico de desempenho, porque os tres de regressao sao avaliados por R2/MAE e os tres de classificacao por acuracia/F1 - metricas incomensuraveis entre tarefas diferentes. A afirmacao defensavel e que o MLP de regressao foi o pior ENTRE OS TRES MODELOS DE REGRESSAO e o unico com R2 negativo em todo o modulo, nao que foi 'o pior dos seis'."
    risk: fato
    source: "Consequencia direta da definicao das metricas (Aula 06 deste modulo: R2 compara o erro do modelo com o de prever a media do alvo continuo; acuracia e fracao de acertos de classe) - nao ha transformacao que ponha as duas na mesma escala comparavel. ACHADO 14 DA AUDITORIA de 2026-09-21 (confusao de escopo na comparacao entre os seis modelos, corrigida no corpo da aula e no claim -RESUMO-SEIS-MODELOS-006)."
-->
