# Flashcards — Módulo 24: Machine Learning em Geociências

## Fundamentos de IA e Aprendizado

| Frente | Verso |
|--------|-------|
| Qual é a relação de inclusão entre Inteligência Artificial, Aprendizado de Máquina e Aprendizado Profundo? | IA ⊃ ML ⊃ DL. Aprendizado de máquina é o subcampo da IA em que o sistema infere a regra de decisão a partir de dados. Aprendizado profundo é o subcampo de ML que usa redes neurais de múltiplas camadas. |
| Qual é o critério central que distingue aprendizado supervisionado de não supervisionado? | A presença ou ausência de rótulo nos dados de treino. Supervisionado usa dados rotulados; não supervisionado usa dados sem rótulo. |
| Defina regressão no contexto de aprendizado supervisionado. | Regressão é a tarefa supervisionada em que o rótulo é numérico contínuo. Objetivo: prever um número a partir de variáveis explicativas. |
| Defina classificação no contexto de aprendizado supervisionado. | Classificação é a tarefa supervisionada em que o rótulo é uma categoria. Objetivo: prever uma classe a partir de variáveis explicativas. |

## Dados Geológicos e Desafios

| Frente | Verso |
|--------|-------|
| Quais são as três principais fontes de dados geológicos em projetos de aprendizado de máquina? | (1) Furos de sondagem (testemunhos, amostras, ensaios químicos), (2) Geofísica (magnetometria, sísmica), (3) Sensoriamento remoto (imagens multiespectrais, hiperespectrais), além de petrografia digital e bancos de dados públicos. |
| Por que dados geológicos violam a premissa i.i.d. (independência e distribuição idêntica)? | Três razões principais: (1) autocorrelação espacial (amostras próximas se parecem), (2) escassez de rótulos (ensaios caros produzem conjuntos pequenos), (3) classes desbalanceadas (a classe rara é a de interesse econômico). |
| O que é autocorrelação espacial e por que é um problema para aprendizado de máquina? | Amostras próximas espacialmente tendem a se parecer. Ao particionar aleatoriamente em treino/teste, vizinhos podem cair em conjuntos diferentes, vazando informação do treino para o teste e inflando a performance. |
| Qual é a solução para o problema de vazamento espacial ao particionar dados? | Validação cruzada em blocos (spatial blocking): particionar por blocos geográficos em vez de por sorteio amostra a amostra, garantindo que vizinhos fiquem no mesmo conjunto. |

## Preparação e Padronização

| Frente | Verso |
|--------|-------|
| Qual é o objetivo da padronização (StandardScaler) antes de algoritmos baseados em distância? | Transformar todas as variáveis para média 0 e desvio-padrão 1, eliminando o efeito de escala. Sem isso, variáveis de escala grande dominam a distância euclidiana. |
| Por que a padronização é ainda mais crítica para redes neurais do que para K-means? | Redes neurais usam descida de gradiente para ajustar pesos, e o gradiente é sensível à escala das variáveis de entrada. Sem padronização, variáveis de escala grande dominam o gradiente inicial. |

## K-Means e Agrupamento

| Frente | Verso |
|--------|-------|
| Descreva os dois passos principais do algoritmo K-means. | (1) Atribuição: cada amostra é atribuída ao centróide mais próximo. (2) Atualização: cada centróide é recalculado como a média das amostras atualmente atribuídas a ele. O processo itera até convergência. |
| O que é inércia no contexto de K-means? | Inércia é a soma das distâncias euclidianas ao quadrado de cada amostra até o centróide do seu grupo. K-means minimiza essa quantidade. |
| O que é o método do cotovelo (elbow method) para escolher o número de grupos em K-means? | Executar K-means para vários valores de k e plotar a inércia versus k. O cotovelo é o ponto onde a queda de inércia desacelera visivelmente, sinalizando que grupos adicionais compram pouca melhoria. |
| Por que agrupamento não supervisionado não precisa coincidir com uma classificação definida por um limiar? | Agrupamento responde à pergunta 'que estrutura existe nos dados'; classificação supervisionada responde 'os dados confirmam a categoria que defini?'. São duas perguntas diferentes com potencialmente respostas diferentes. |
| Qual é a diferença conceitual entre K-means e domínios geoestatísticos? | K-means parte da estrutura estatística multivariada dos dados analíticos. Domínios geoestatísticos partem do critério geológico de campo, com verificação estatística secundária. Convergem quando geologia se expressa na geoquímica. |

## PCA

| Frente | Verso |
|--------|-------|
| O que é Análise de Componentes Principais (PCA)? | PCA transforma um conjunto de variáveis correlacionadas em um novo conjunto de variáveis não correlacionadas (componentes principais), ordenados pela variância que capturam. |
| O que são loadings em PCA? | Loadings são os pesos que indicam como cada componente principal combina as variáveis originais. Uma linha de loadings por componente, uma coluna por variável original. |

## Regressão Linear

| Frente | Verso |
|--------|-------|
| Defina regressão linear múltipla. | Modelo: ŷ = β₀ + β₁x₁ + β₂x₂ + ... + βₚxₚ. Estima coeficientes minimizando a soma dos quadrados dos resíduos no conjunto de treino (método dos mínimos quadrados). |
| Por que os coeficientes brutos de uma regressão linear não padronizada não são comparáveis como medida de importância? | Porque cada coeficiente carrega a unidade da sua variável. Coeficiente grande não significa variável importante; pode significar apenas que a variável varia em escala pequena. |
| Como corrigir os coeficientes de regressão para comparação honesta de importância? | Multiplicar cada coeficiente pelo desvio-padrão da sua variável no treino (equivalente a reajustar o modelo sobre variáveis padronizadas). |
| O que é multicolinearidade e qual é seu efeito em regressão linear? | Multicolinearidade é quando variáveis explicativas correlacionam fortemente entre si. Torna difícil separar qual variável merece o crédito pela variação do alvo; os coeficientes parciais ficam instáveis. |

## Florestas Aleatórias

| Frente | Verso |
|--------|-------|
| Descreva uma floresta aleatória (random forest). | Combina muitas árvores de decisão, cada uma treinada em uma amostra aleatória (bootstrap) dos dados e considerando um subconjunto aleatório de variáveis a cada divisão. A previsão final é a média (regressão) ou voto majoritário (classificação) das árvores. |
| O que é feature_importances_ em florestas aleatórias? | Medida de importância de variável baseada na redução média de impureza (ou inércia) que cada variável proporciona nas divisões de todas as árvores. |
| Qual é o viés documentado da importância por impureza (feature_importances_) em florestas? | Enviesada A FAVOR de variáveis de alta cardinalidade (contínuas, muitos valores distintos) e CONTRA variáveis binárias ou categóricas com poucas categorias. |
| Por que a regressão linear superou a floresta aleatória na regressão de ouro (Au) neste módulo? | Porque com apenas 45 amostras de treino, a floresta (com 300 árvores, muitos parâmetros) sofre sobreajuste. A regressão linear, com forma funcional restrita (7 parâmetros), generaliza melhor em amostra pequena. |

## Regressão e Geoestatística

| Frente | Verso |
|--------|-------|
| Descreva a relação formal entre krigagem ordinária e regressão linear. | Ambas estimam uma combinação linear ponderada ajustada a partir de uma estrutura de covariância nos dados. Kriegagem pertence à família dos Mínimos Quadrados Generalizados (GLS), não é regressão linear ordinária. |
| Qual é a diferença entre GLS (Mínimos Quadrados Generalizados) e GLM (Modelo Linear Generalizado)? | GLS generaliza regressão linear para resíduos correlacionados. GLM é a família a que pertence a regressão logística. Não são a mesma coisa. |

## Regressão Logística

| Frente | Verso |
|--------|-------|
| O que é regressão logística e por que não usamos regressão linear comum para classificação? | Regressão logística modela P(y=1\|x) = 1/(1+exp(-(β₀+β₁x₁+...))). A sigmoide comprime a saída para (0,1). Regressão linear comum pode prever valores fora [0,1], não representando probabilidade. |
| Qual é a função de ativação sigmoide e qual é seu papel na regressão logística? | Função sigmoide: σ(z) = 1/(1+e^(-z)). Converte uma combinação linear ilimitada em uma probabilidade no intervalo (0,1), comprimindo o resultado. |
| Qual é o limiar de decisão padrão em regressão logística no scikit-learn? | 0,5. Amostras com probabilidade prevista acima de 0,5 são classificadas como positivas; abaixo de 0,5, como negativas. |

## Matriz de Confusão e Métricas

| Frente | Verso |
|--------|-------|
| Descreva a matriz de confusão em formato padrão do scikit-learn para classificação binária. | [[TN, FP], [FN, TP]]. TN = verdadeiro negativo, FP = falso positivo, FN = falso negativo, TP = verdadeiro positivo. |
| Defina acurácia em classificação e cite seu problema principal. | Acurácia = (TP+TN)/(TP+TN+FP+FN). Problema: trata falsos positivos e negativos como igualmente custosos, e esconde desequilíbrios em classes desbalanceadas. |
| Defina precisão (precision) em classificação. | Precisão = TP/(TP+FP). Responde: das amostras que o modelo previu como positivas, quantas realmente são? |
| Defina revocação (recall) ou sensibilidade em classificação. | Revocação = TP/(TP+FN). Responde: das amostras que realmente são positivas, quantas o modelo capturou? |
| Defina F1-score. | F1 = 2·(precisão·revocação)/(precisão+revocação). Média harmônica de precisão e revocação, penalizando desbalanceamento entre as duas. |
| Por que acurácia sozinha engana em classes desbalanceadas? | Um modelo que sempre prevê a classe majoritária pode ter acurácia alta mas revocação zero na classe rara, cenário perigoso em geociências onde a classe rara é economicamente/ambientalmente relevante. |

## Sobreajuste e Validação

| Frente | Verso |
|--------|-------|
| Defina sobreajuste (overfitting). | Sobreajuste ocorre quando um modelo se ajusta tão de perto ao ruído do conjunto de treino que perde capacidade de generalizar para dado novo. Sintoma: desempenho excelente em treino, pior em teste. |
| Qual é a razão parâmetros/amostras como fator de risco de sobreajuste? | Razão alta entre parâmetros ajustáveis e amostras de treino favorece sobreajuste. Ex: 257 parâmetros para 45 amostras (>5 por amostra) é risco alto. |
| Como diagnosticar sobreajuste na prática? | Comparar desempenho em treino com desempenho em teste. Gap grande (treino 1,0 e teste 0,5) é sintoma claro de sobreajuste. Nunca julgar modelo pelo desempenho no treino. |
| O que é validação cruzada k-fold? | Dividir dados em k partes (folds), treinar k vezes deixando cada parte de fora como teste, alternando qual parte fica de fora. Desempenho é resumido pela média e desvio-padrão das k métricas. |
| Qual é a relação entre leave-one-out e k-fold? | Leave-one-out é um caso especial de k-fold em que k = número total de amostras. Cada amostra é testada uma única vez. |
| Por que o desvio-padrão de validação cruzada é tão importante quanto a média? | Desvio-padrão quantifica quanto o desempenho varia entre folds. Uma única métrica sem essa variação dá falsa sensação de precisão. |

## Métricas de Regressão

| Frente | Verso |
|--------|-------|
| Defina MAE (Mean Absolute Error) em regressão. | MAE = (1/n)·Σ\|yᵢ - ŷᵢ\|. Erro médio absoluto em mesma unidade que o rótulo. Diretamente interpretável como 'previsão erra por X unidades em média'. |
| Defina RMSE (Root Mean Squared Error) em regressão. | RMSE = √[(1/n)·Σ(yᵢ - ŷᵢ)²]. Elevar ao quadrado penaliza erros grandes; RMSE ≥ MAE sempre. Diferença entre MAE e RMSE sinaliza presença de erros grandes. |
| Defina R² (coeficiente de determinação). | R² = 1 - Σ(yᵢ-ŷᵢ)²/Σ(yᵢ-ȳ)². Compara erro do modelo com erro de prever a média. R²=1 (perfeito), R²=0 (igual à média), R²<0 (pior que média). |
| O que significa R² negativo e por que é um sinal claro de modelo malajustado? | R²<0 significa que o modelo prevê pior do que simplesmente prever a média de y para toda amostra. É o sintoma mais inequívoco de modelo inadequado. |

## Redes Neurais

| Frente | Verso |
|--------|-------|
| O que é uma rede neural artificial? | Organiza cálculo em camadas: entrada, uma ou mais camadas ocultas, e saída. Cada neurônio faz combinação linear das saidas da camada anterior + viés, passa por função de ativação não linear, repassa adiante. |
| Por que a função de ativação é essencial em redes neurais? | Sem não linearidade, camadas lineares empilhadas colapsariam algebricamente em uma única regressão linear. A não linearidade (ReLU, sigmoide) permite expressividade de formas funcionais complexas. |
| O que é ReLU (Rectified Linear Unit)? | ReLU(x) = max(0, x). Função de ativação mais usada em camadas ocultas de redes neurais modernas. Simples e eficiente de treinar. |
| Descreva o processo de retropropagação (backpropagation) em redes neurais. | Rede faz previsão, mede erro em relação ao rótulo verdadeiro, propaga esse erro de volta pelas camadas, ajustando cada peso na direção que mais reduz o erro. Repetido por muitas iterações. |
| Quantos parâmetros tem um MLP com 6 entradas, 8 neurônios ocultos e 1 saída? | 6×8 + 8 (camada oculta) + 8×1 + 1 (camada saida) = 65 parâmetros. Coeficientes e vieses combinados. |
| Por que o MLP de regressão teve R² negativo neste módulo? | Porque tinha 257 parâmetros para 45 amostras de treino (>5 por amostra). Não havia informação suficiente para restringir esses graus de liberdade; a rede memorizou o treino e generalizou mal. |

## Interpretação de Modelos

| Frente | Verso |
|--------|-------|
| O que é importância por permutação (permutation importance)? | Embaralhar os valores de uma variável por vez, manter demais intactas, medir queda de desempenho do modelo já treinado. Queda grande indica dependência forte daquela variável. Agnóstica ao modelo (funciona com qualquer). |
| Qual é a limitação da importância por permutação com variáveis correlacionadas? | Quando duas variáveis correlacionam, embaralhar uma delas não derruba o desempenho porque o modelo recupera a mesma informação pela outra. Ambas saem com importância baixa apesar de informativas. |

## Comunicação de Resultados

| Frente | Verso |
|--------|-------|
| Como comunicar resultados de aprendizado de máquina adequadamente? | Declarar: (1) algoritmo escolhido e por quê, (2) tamanho da amostra e suas limitações, (3) métrica no teste com sua incerteza (desvio-padrão), (4) para que decisões o modelo é/não é adequado. |
| Qual é a regra de ouro para escolher entre algoritmos simples e complexos em geociências? | Em conjuntos pequenos (típico em geociências), o algoritmo mais sofisticado não é automaticamente melhor. Comparar candidatos no teste é o único jeito confiável de saber qual funciona melhor no problema concreto. |
