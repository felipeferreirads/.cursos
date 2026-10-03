# Aula 05: Modelagem não supervisionada — agrupamento e redução de dimensionalidade

**ID:** geologia-avancado-m24-a05
**Módulo:** [[24-machine-learning-geociencias-modulo|Módulo 24 — Fundamentos e aplicações de machine learning em geociências]]
**Duração estimada:** ~28 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** aplicar agrupamento (K-means) e redução de dimensionalidade (PCA) aos dados geoquímicos da Aula 02, sem usar o rótulo `anomalo`, e comparar o resultado descoberto pelo algoritmo com a classificação supervisionada da Aula 04 e com a lógica de domínios da geoestatística do Módulo 20.
**Ao final você vai conseguir:** padronizar variáveis antes de um algoritmo baseado em distância; ajustar K-means, escolher o número de grupos pelo método do cotovelo e interpretar os grupos resultantes; ajustar uma Análise de Componentes Principais (PCA), interpretar a variância explicada e os *loadings*; e explicar por que grupos descobertos sem rótulo não precisam coincidir com uma classificação definida por um limiar humano.
**Pré-requisito:** [[24-machine-learning-geociencias-aula-04-modelagem-supervisionada-classificacao|Aula 04 — Modelagem supervisionada: classificação]] (usa as mesmas variáveis geoquímicas, agora sem o rótulo `anomalo`, que só reaparece ao final para comparação). [[20-geoestatistica/20-geoestatistica-modulo|Módulo 20]] para a ideia de domínio geológico.

## Conteúdo

### Por que padronizar antes de agrupar

Agrupamento e redução de dimensionalidade, ao contrário dos modelos supervisionados das Aulas 03 e 04, não recebem nenhum rótulo — o algoritmo só enxerga as variáveis explicativas e precisa decidir, sozinho, o que é "parecido" e o que não é. A maioria dos métodos usados aqui mede semelhança por **distância** (geralmente euclidiana) no espaço das variáveis, e essa distância é sensível à **escala** de cada uma: neste conjunto de dados, `Cu_ppm` varia de 5 a mais de 1.200, enquanto `As_ppm` varia de 0,5 a cerca de 28 — sem correção, a distância entre duas amostras seria dominada quase inteiramente pela diferença em cobre, e o arsênio praticamente não pesaria, não porque seja menos importante geologicamente, mas só porque sua escala numérica é menor. A correção padrão é a **padronização** (*standardization*): subtrair a média e dividir pelo desvio-padrão de cada variável, deixando todas com média 0 e desvio-padrão 1.

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("geoquimica.csv")
df["As_ppm"] = df["As_ppm"].fillna(df["As_ppm"].median())

feat = ["Cu_ppm", "As_ppm", "Zn_ppm"]
X = df[feat].values
Xs = StandardScaler().fit_transform(X)

print("media apos padronizacao:", np.round(Xs.mean(axis=0), 4))
print("desvio apos padronizacao:", np.round(Xs.std(axis=0), 4))
```

**Saída esperada:** média `[0, 0, 0]` (numericamente `[-0., -0., -0.]`, um artefato de arredondamento de ponto flutuante) e desvio-padrão `[1, 1, 1]` para as três colunas — confirmando que a padronização funcionou como esperado. Este passo usa só os três elementos geoquímicos (Cu, As, Zn), não a distância à falha nem a litologia: o objetivo aqui é encontrar **fácies geoquímicas** — agrupamentos de amostras quimicamente parecidas —, uma pergunta diferente da que orientou as Aulas 03 e 04.

### K-means: agrupar por proximidade

O **K-means** é o algoritmo de agrupamento mais usado por sua simplicidade: dado um número de grupos $k$ escolhido de antemão, ele posiciona $k$ **centróides** (pontos representativos) no espaço das variáveis e itera dois passos até convergir — (1) atribui cada amostra ao centróide mais próximo, e (2) recalcula cada centróide como a média das amostras atualmente atribuídas a ele. O algoritmo minimiza a **inércia**: a soma, sobre todas as amostras, da distância euclidiana ao quadrado entre cada amostra e o centróide do seu grupo — quanto menor a inércia, mais compactos (internamente parecidos) são os grupos resultantes.

```python
from sklearn.cluster import KMeans

km2 = KMeans(n_clusters=2, random_state=42, n_init=10).fit(Xs)
print("inercia k=2:", round(km2.inertia_, 2))
print("tamanho dos grupos:", np.bincount(km2.labels_))

df["cluster"] = km2.labels_
print(df.groupby("cluster")[feat].mean().round(1))
```

**Saída esperada:** inércia de **55,75** para $k=2$, com grupos de tamanho **45 e 15** amostras. A média de cada elemento por grupo revela o que o algoritmo encontrou sozinho, sem qualquer rótulo: o grupo de 45 amostras tem Cu médio de **208,6 ppm**, As de **6,2 ppm** e Zn de **107,2 ppm** — um perfil geoquímico de **background**; o grupo de 15 amostras tem Cu médio de **835,6 ppm**, As de **19,6 ppm** e Zn de **346,1 ppm** — um perfil claramente mais enriquecido, um domínio **anômalo**. O K-means recuperou, sem nenhum rótulo, uma separação qualitativamente parecida com a que a Aula 04 aprendeu a prever, a partir do limiar arbitrário de cobre (180 ppm) fixado na Aula 02 — mas não é a mesma partição, como a seção seguinte mostra.

**Escolher $k$: o método do cotovelo.** Nada, no algoritmo em si, diz qual é o número "certo" de grupos — é um parâmetro que precisa ser escolhido. O **método do cotovelo** (*elbow method*) ajusta o K-means para vários valores de $k$ e observa como a inércia cai:

```python
inercias = []
for k in range(1, 7):
    km = KMeans(n_clusters=k, random_state=42, n_init=10).fit(Xs)
    inercias.append(round(km.inertia_, 2))
print(inercias)
```

**Saída esperada:** `[180.0, 55.75, 31.9, 22.38, 18.28, 16.35]` para $k = 1$ a $6$. A inércia sempre cai quando $k$ aumenta (mais grupos, cada um menor e mais compacto — no limite, $k$ igual ao número de amostras dá inércia zero, cada amostra sendo seu próprio grupo, o que não é útil), então a escolha não é "o $k$ de menor inércia" — seria sempre o maior testado. É procurar o **cotovelo**: o ponto onde a queda da inércia desacelera visivelmente, sinalizando que grupos adicionais compram cada vez menos compactação por grupo a mais. Aqui, a queda de $k=1$ para $k=2$ é a maior de todas (de 180,0 para 55,75, uma redução de 69%), e as quedas seguintes (para $k=3$: mais 43%; para $k=4$: mais 30%) diminuem progressivamente — o cotovelo mais nítido está em $k=2$, coerente com a estrutura geológica esperada deste exemplo (background versus anômalo).

### Agrupamento não é classificação: comparando com o rótulo

O K-means encontrou seus dois grupos sem nunca ver `anomalo`. Comparar os dois, agora, revela até onde a semelhança vai:

```python
print(pd.crosstab(df["cluster"], df["anomalo"]))
```

**Saída esperada:**

```
anomalo    0   1
cluster
0         20  25
1          1  14
```

O cluster 1 (o grupo enriquecido, 15 amostras) é quase inteiramente composto por amostras rotuladas `anomalo=1` (14 de 15) — o algoritmo isolou corretamente o núcleo mais enriquecido. Mas o cluster 0 (45 amostras) é uma mistura: 20 amostras background e **25 amostras rotuladas anômalas** — mais da metade do total de amostras anômalas do conjunto (39, pela Aula 02) caem no cluster "background". Isso não é um defeito do K-means: é a consequência direta de o rótulo `anomalo` ter sido definido por um **limiar único e arbitrário** (Cu > 180 ppm, com 12% de ruído de rótulo, Aula 02), enquanto o K-means organiza os dados pela sua estrutura geométrica natural em três dimensões (Cu, As, Zn simultaneamente) — e essa estrutura natural, aqui, tem uma transição mais gradual do que um único corte abrupto em uma variável reproduziria. A lição generaliza: **um algoritmo não supervisionado responde "que estrutura existe nos dados", não "os dados confirmam a categoria que eu já tinha em mente"** — as duas perguntas podem ter respostas parecidas, mas raramente idênticas, e tratar os grupos de um K-means como se fossem automaticamente a classificação de interesse é um erro de interpretação comum.

### PCA: redução de dimensionalidade

A **Análise de Componentes Principais** (PCA) resolve um problema diferente: em vez de agrupar amostras, ela reescreve um conjunto de variáveis correlacionadas (aqui, Cu, As e Zn, com correlações de 0,82 a 0,95 entre si, já vistas na Aula 02) como um novo conjunto de variáveis não correlacionadas — os **componentes principais** —, ordenados por quanta variação original cada um capta. O primeiro componente principal (PC1) é a combinação linear das variáveis originais que captura a maior variância possível; o segundo (PC2) é a combinação linear, ortogonal à primeira, que captura a maior variância restante; e assim por diante.

```python
from sklearn.decomposition import PCA

pca = PCA().fit(Xs)
print("variancia explicada:", np.round(pca.explained_variance_ratio_, 4))
print("acumulada:", np.round(np.cumsum(pca.explained_variance_ratio_), 4))
print("loadings:\n", np.round(pca.components_, 3))
```

**Saída esperada:** variância explicada de **92,03%** pelo PC1, **6,63%** pelo PC2 e apenas **1,33%** pelo PC3 — os três somam 100%, porque com três variáveis de entrada há no máximo três componentes principais, e juntos eles recuperam toda a variância original. Os dois primeiros componentes já somam **98,67%** da variância — praticamente toda a informação das três variáveis originais cabe em duas dimensões, uma consequência direta da forte correlação entre Cu, As e Zn: quando variáveis são muito correlacionadas, elas carregam informação redundante, e o PCA identifica e remove essa redundância. Os **loadings** (a matriz `components_`, uma linha por componente, uma coluna por variável original) dizem *como* cada componente combina as variáveis: o PC1 tem pesos aproximadamente iguais e positivos em Cu, As e Zn (0,591; 0,561; 0,580) — na prática, o PC1 se comporta como uma **média ponderada geral de enriquecimento geoquímico**, um "índice de anomalia" que os três elementos compartilham. O PC2 (pesos −0,255; 0,812; −0,525) contrasta principalmente o arsênio com o cobre e o zinco — uma segunda dimensão de variação, bem menos importante (6,6% da variância) mas potencialmente informativa sobre amostras com razões elementares atípicas (arsênio alto sem cobre/zinco proporcionalmente altos, por exemplo).

```python
pca2 = PCA(n_components=2).fit(Xs)
Xp = pca2.transform(Xs)
print("variancia com 2 componentes:", round(pca2.explained_variance_ratio_.sum(), 4))
print(np.round(Xp[:5], 3))
```

**Saída esperada:** as duas primeiras amostras projetadas em (PC1, PC2) são aproximadamente `(−1,271; 0,224)` e `(−1,708; −0,102)` — ambas com PC1 bem negativo, coerente com serem amostras de baixo teor (PC1 alto e positivo indicaria enriquecimento, pela direção dos pesos calculados acima). Reduzir de 3 para 2 dimensões preserva 98,67% da variância original — na prática, quase nenhuma informação é perdida, e o ganho é poder visualizar as 60 amostras num único gráfico de dispersão bidimensional (PC1 no eixo x, PC2 no eixo y) em vez de precisar de um gráfico tridimensional, com o cluster K-means da seção anterior sobreposto por cor para verificar visualmente a separação encontrada.

### Domínios geoestatísticos e agrupamento: a mesma pergunta, ferramentas diferentes

O Módulo 20 não tratou explicitamente de agrupamento, mas a prática de geoestatística que ele introduziu depende de uma etapa anterior à krigagem que este raciocínio ilumina: a **definição de domínios** — subdividir um depósito em regiões com comportamento estatístico distinto (médias e variogramas diferentes) antes de estimar cada uma separadamente, porque misturar domínios geologicamente diferentes numa única krigagem viola a estacionariedade que a Aula 02 do Módulo 20 exige. Na prática de mercado, domínios são definidos predominantemente por **critério geológico** (contatos litológicos, zonas de alteração mapeadas em campo) e só secundariamente checados estatisticamente; o agrupamento por K-means desta aula inverte a ênfase — parte puramente da estrutura estatística multivariada dos dados analíticos, sem nenhuma informação geológica de campo incorporada diretamente. As duas abordagens **convergem quando a estrutura geológica real se expressa claramente na geoquímica** (como neste exemplo, onde o cluster K-means recuperou um domínio enriquecido coerente) e **divergem quando não se expressa** — um contato litológico abrupto pode não corresponder a nenhuma descontinuidade geoquímica visível, e uma zonação geoquímica gradual pode não respeitar nenhum contato mapeado. Na prática profissional, agrupamento não supervisionado serve bem como **ferramenta exploratória** para sugerir domínios candidatos ou verificar se um domínio definido geologicamente é também estatisticamente coerente — não como substituto do julgamento geológico de campo.

## Exemplo trabalhado

**Situação:** confirme manualmente, para $k=2$, que a divisão do cluster 1 (15 amostras, Cu médio 835,6 ppm) produz uma inércia consistente com o valor reportado, e compare os tamanhos de grupo com o corte por limiar da Aula 02.

**Verificação de consistência:** o cluster 1 tem 15 amostras — exatamente o mesmo número de amostras cuja combinação de Cu, As e Zn padronizados as coloca mais distantes da massa principal de dados, e a inércia total do agrupamento (55,75) é bem menor do que a inércia com $k=1$ (180,0, que é simplesmente a soma das distâncias ao quadrado de todas as 60 amostras ao centróide único do conjunto inteiro). Esse 180,0 não é um número arbitrário: para variáveis padronizadas, cada uma das $p$ colunas contribui com variância 1 por amostra, então a inércia com $k=1$ vale exatamente $n \times p = 60 \times 3 = 180$. Ou seja, ela é **$n$ vezes** a variância total multivariada — que aqui é 3, não 180. A queda de 180,0 para 55,75 é uma redução de 69%, o maior salto de toda a sequência de $k$ testada, confirmando $k=2$ como a escolha do cotovelo já identificada.

**Comparação com o limiar da Aula 02:** o rótulo `anomalo` da Aula 02 marca 39 das 60 amostras como anômalas (65%). Cuidado para não atribuir esse 39 ao limiar sozinho: o limiar puro de Cu > 180 ppm seleciona **36** amostras, e o ruído de rótulo de 12% troca 5 delas (4 de background para anômala, 1 no sentido inverso), fechando em 36 − 1 + 4 = 39. O K-means, sem ver esse limiar, isolou um grupo bem menor e mais concentrado (15 amostras, 25%) como o núcleo geoquimicamente mais enriquecido. A diferença não é um erro de nenhum dos dois métodos — são duas definições diferentes de "anômalo": o limiar da Aula 02 é uma regra simples sobre uma única variável (deliberadamente, para servir de rótulo de treino a um classificador), enquanto o K-means encontra uma partição que respeita a estrutura conjunta de três variáveis simultaneamente. Um projeto real de exploração se beneficiaria de examinar os dois: onde os dois concordam (as 14 amostras do cluster 1 que também são `anomalo=1`), a evidência é mais forte; onde divergem (as 25 amostras `anomalo=1` fora do cluster 1), vale investigar se são zonas de transição, ruído de rótulo, ou uma mineralização de caráter geoquímico distinto que um limiar único de cobre não capturaria.

## Recap relâmpago

- Algoritmos baseados em distância (K-means, e a maioria dos métodos não supervisionados) exigem **padronização** prévia das variáveis (`StandardScaler`) — sem ela, a variável de maior escala numérica domina a distância, distorcendo os grupos.
- **K-means** particiona os dados em $k$ grupos minimizando a **inércia** (soma das distâncias ao quadrado de cada amostra ao centróide do seu grupo); $k$ é escolhido pelo **método do cotovelo**, observando onde a queda de inércia desacelera — neste exemplo, $k=2$.
- Os grupos descobertos por agrupamento **não precisam coincidir** com uma classificação supervisionada definida por um limiar — respondem a perguntas diferentes (estrutura natural dos dados versus categoria pré-definida), e a comparação entre os dois é informativa, não um teste de "acerto ou erro".
- **PCA** substitui variáveis correlacionadas por **componentes principais** não correlacionados, ordenados pela variância que capturam; os **loadings** dizem como cada componente combina as variáveis originais. Neste exemplo, PC1 (92% da variância) funciona como um índice geral de enriquecimento geoquímico.
- Agrupamento não supervisionado e **domínios geoestatísticos** (Módulo 20) respondem a uma pergunta semelhante — que regiões dos dados formam grupos coerentes — mas por caminhos diferentes: um parte da estrutura estatística multivariada, o outro do critério geológico de campo; convergem quando a geologia se expressa claramente na geoquímica e divergem quando não.

## Próxima aula

[[24-machine-learning-geociencias-aula-06-avaliacao-desempenho-sobreajuste-validacao|Aula 06 — Medidas de avaliação de desempenho, sobreajuste e validação]] — formaliza as métricas (MAE, RMSE, R², acurácia, precisão, revocação, F1) já usadas informalmente nas Aulas 03 e 04, e mostra como diagnosticar sobreajuste com validação cruzada.

## Fontes

- K-means como algoritmo de agrupamento por minimização de inércia, e o método do cotovelo para escolha do número de grupos: Hastie, T., Tibshirani, R. & Friedman, J., *The Elements of Statistical Learning*, 2ª ed. (2009), Springer, cap. 14.3; documentação oficial scikit-learn, classe `KMeans` e módulo `sklearn.cluster` (scikit-learn.org), versão 1.9.
- Análise de Componentes Principais (PCA): variância explicada, componentes ortogonais e *loadings*: Jolliffe, I. T., *Principal Component Analysis*, 2ª ed. (2002), Springer; documentação oficial scikit-learn, classe `PCA` (scikit-learn.org), versão 1.9.
- Necessidade de padronização de variáveis antes de métodos baseados em distância euclidiana: Géron, A., *Hands-On Machine Learning with Scikit-Learn, Keras and TensorFlow*, 3ª ed. (2022), O'Reilly, cap. 2 e 9.
- Definição de domínios geoestatísticos por critério geológico antes da estimativa, e a exigência de estacionariedade dentro de cada domínio: retomando [[20-geoestatistica/20-geoestatistica-aula-02-variaveis-regionalizadas-funcao-aleatoria-estacionariedade|Módulo 20, Aula 02]] deste curso; Rossi, M. E. & Deutsch, C. V., *Mineral Resource Estimation* (2014), Springer, cap. 4 (definição de domínios de estimativa).

<!--
nivel: avancado
palavras_corpo: 2319
mapa_objetivo_secao:
  geologia-avancado-m24-oa03: "Por que padronizar antes de agrupar" + "K-means: agrupar por proximidade" + "Agrupamento não é classificação: comparando com o rótulo" + "PCA: redução de dimensionalidade" + "Domínios geoestatísticos e agrupamento: a mesma pergunta, ferramentas diferentes" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: MLGEO-M24-A04-PADRONIZACAO-001
    claim: "Aplicando StandardScaler as tres colunas Cu_ppm, As_ppm, Zn_ppm do conjunto de dados da aula (com As_ppm ja imputado pela mediana), o resultado tem media 0 e desvio-padrao 1 em cada coluna (a media e numericamente -0. por arredondamento de ponto flutuante, nao exatamente zero, mas equivalente a zero dentro da precisao de maquina)."
    risk: calculo
    source: "Execucao direta do codigo apresentado na aula (scikit-learn 1.9.1, NumPy 2.5.1). CONFIRMADO POR EXECUCAO em 2026-09-20: media = [-0.,-0.,-0.], desvio = [1.,1.,1.] apos arredondamento a 4 casas."
  - claim_id: MLGEO-M24-A04-KMEANS-K2-002
    claim: "KMeans(n_clusters=2, random_state=42, n_init=10) sobre as tres variaveis geoquimicas padronizadas do conjunto de dados da aula produz inercia 55.75, com grupos de tamanho 45 e 15 amostras; o grupo de 45 tem media Cu_ppm=208.6, As_ppm=6.2, Zn_ppm=107.2 e o grupo de 15 tem media Cu_ppm=835.6, As_ppm=19.6, Zn_ppm=346.1."
    risk: calculo
    source: "Execucao direta do codigo apresentado na aula (scikit-learn 1.9.1). CONFIRMADO POR EXECUCAO em 2026-09-20: inertia_=55.75 (arredondado 2 casas), bincount(labels)=[45,15], medias por grupo batendo digito a digito."
  - claim_id: MLGEO-M24-A04-COTOVELO-003
    claim: "Para o mesmo conjunto padronizado, a inercia do KMeans (n_init=10, random_state=42) para k=1 a 6 e, respectivamente, 180.0, 55.75, 31.9, 22.38, 18.28 e 16.35; a maior queda relativa ocorre de k=1 para k=2 (reducao de aproximadamente 69%), com quedas subsequentes progressivamente menores (k=2 para k=3: aproximadamente 43%; k=3 para k=4: aproximadamente 30%), identificando k=2 como o cotovelo da sequencia."
    risk: calculo
    source: "Execucao direta do codigo apresentado na aula (scikit-learn 1.9.1). CONFIRMADO POR EXECUCAO em 2026-09-20: lista de inercias reproduzida digito a digito; percentuais de queda calculados a partir dela: (180.0-55.75)/180.0=0.6903 (~69%), (55.75-31.9)/55.75=0.4278 (~43%), (31.9-22.38)/31.9=0.2985 (~30%)."
  - claim_id: MLGEO-M24-A04-CROSSTAB-004
    claim: "Cruzando o cluster do KMeans (k=2) com o rotulo anomalo do conjunto de dados da aula (39 amostras anomalas, 21 background, no total de 60), o cluster 0 (45 amostras) contem 20 background e 25 anomalas, e o cluster 1 (15 amostras) contem 1 background e 14 anomalas - ou seja, 25 das 39 amostras rotuladas anomalas (mais da metade) caem no cluster que a media geoquimica caracteriza como background."
    risk: calculo
    source: "Execucao direta de pd.crosstab sobre os resultados do KMeans e o rotulo anomalo do conjunto de dados da aula. CONFIRMADO POR EXECUCAO em 2026-09-20: crosstab reproduzida digito a digito (cluster0: {0:20,1:25}; cluster1: {0:1,1:14})."
  - claim_id: MLGEO-M24-A04-PCA-VARIANCIA-005
    claim: "PCA() ajustado as tres variaveis geoquimicas padronizadas do conjunto de dados da aula produz variancia explicada de 0.9203 (92.03%) pelo primeiro componente, 0.0663 (6.63%) pelo segundo e 0.0133 (1.33%) pelo terceiro, somando 1.0 (os tres juntos recuperam toda a variancia, pois ha exatamente tres variaveis de entrada); os dois primeiros componentes somam 0.9867 (98.67%) da variancia total. Os loadings do primeiro componente sao aproximadamente 0.591 (Cu_ppm), 0.561 (As_ppm) e 0.580 (Zn_ppm), pesos positivos e de magnitude semelhante nas tres variaveis; os loadings do segundo componente sao aproximadamente -0.255 (Cu_ppm), 0.812 (As_ppm) e -0.525 (Zn_ppm)."
    risk: calculo
    source: "Execucao direta do codigo apresentado na aula (scikit-learn 1.9.1). CONFIRMADO POR EXECUCAO em 2026-09-20: explained_variance_ratio_ = [0.9203, 0.0663, 0.0133] (soma exata 1.0 dentro da precisao de ponto flutuante); components_ reproduzidos digito a digito (arredondados a 3 casas)."
  - claim_id: MLGEO-M24-A04-KMEANS-ALGORITMO-006
    claim: "O algoritmo K-means, dado um numero de grupos k escolhido a priori, itera dois passos ate convergencia: atribuicao de cada amostra ao centroide mais proximo (por distancia euclidiana) e recalculo de cada centroide como a media das amostras atualmente atribuidas a ele, minimizando a inercia (soma das distancias euclidianas ao quadrado entre cada amostra e o centroide do seu grupo)."
    risk: fato
    source: "Hastie, T., Tibshirani, R. & Friedman, J., The Elements of Statistical Learning, 2a ed. (2009), Springer, secao 14.3.6."
  - claim_id: MLGEO-M24-A04-DOMINIOS-GEOESTATISTICOS-007
    claim: "Na pratica profissional de estimativa de recursos minerais, a definicao de dominios de estimativa (subregioes com comportamento estatistico distinto, cada uma tratada separadamente por variografia e krigagem) e predominantemente conduzida por criterio geologico (contatos litologicos, zonas de alteracao mapeadas em campo), com verificacao estatistica secundaria, ao contrario de um agrupamento nao supervisionado puramente estatistico como o K-means, que parte exclusivamente da estrutura multivariada dos dados analiticos sem incorporar diretamente informacao geologica de campo."
    risk: fato
    source: "Rossi, M. E. & Deutsch, C. V., Mineral Resource Estimation (2014), Springer, cap. 4 (definicao de dominios de estimativa)."
  - claim_id: MLGEO-M24-A04-INERCIA-K1-008
    claim: "A inercia do KMeans com k=1 (180.0 neste conjunto) e a soma das distancias euclidianas ao quadrado de todas as amostras ao centroide unico do conjunto. Para variaveis padronizadas ela vale exatamente n*p (60 amostras x 3 variaveis = 180), porque cada variavel padronizada contribui com variancia 1 por amostra - ou seja, a inercia com k=1 e n VEZES a variancia total multivariada (que aqui vale 3), e NAO igual a ela."
    risk: calculo
    source: "Definicao de inercia em sklearn.cluster.KMeans (documentacao oficial scikit-learn, versao 1.9) combinada com a identidade soma_i ||x_i - media||^2 = n * soma_j var(x_j); StandardScaler usa variancia populacional (ddof=0), o que torna a identidade exata. CONFIRMADO POR EXECUCAO em 2026-09-20: km1.inertia_ = 180.0 exatamente, para n=60 e p=3. ACHADO 2 DA AUDITORIA de 2026-09-20 (a aula dizia que a inercia era 'equivalente a variancia total multivariada', o que erra por um fator n=60)."
  - claim_id: MLGEO-M24-A04-LIMIAR-CONTAGEM-009
    claim: "No conjunto de dados do modulo, o limiar puro de Cu > 180 ppm seleciona 36 das 60 amostras; o rotulo anomalo efetivamente usado marca 39 das 60 (65%) porque o gerador da Aula 02 aplica 12% de ruido de rotulo, que trocou 5 rotulos (4 de background para anomala e 1 de anomala para background), fechando em 36 - 1 + 4 = 39. As duas contagens nao devem ser confundidas: 39 e a contagem do rotulo, nao a do limiar."
    risk: calculo
    source: "Execucao direta do gerador de dados da Aula 02 (NumPy 2.5.1, semente 7). CONFIRMADO POR EXECUCAO em 2026-09-20: (Cu_ppm > 180).sum() = 36; flip.sum() = 5, com 4 no sentido 0->1 e 1 no sentido 1->0; anomalo.sum() = 39. ACHADO 5 DA AUDITORIA de 2026-09-20 (a aula atribuia os 39 ao limiar sozinho)."
-->
