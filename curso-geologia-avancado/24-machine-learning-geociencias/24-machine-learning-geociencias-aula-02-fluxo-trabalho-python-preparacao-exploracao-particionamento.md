# Aula 02: Fluxo de trabalho em Python — objetivo, coleta, preparação, análise exploratória e particionamento dos dados

**ID:** geologia-avancado-m24-a02
**Módulo:** [[24-machine-learning-geociencias-modulo|Módulo 24 — Fundamentos e aplicações de machine learning em geociências]]
**Duração estimada:** ~29 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** executar, em Python, as cinco primeiras etapas de qualquer projeto de aprendizado de máquina — definir o problema, coletar os dados, prepará-los, explorá-los estatisticamente e particioná-los em treino e teste — sobre um conjunto de dados geoquímicos que vai ser reaproveitado pelas Aulas 03 a 07.
**Ao final você vai conseguir:** carregar uma tabela de dados com pandas e diagnosticar seu formato, tipos e valores ausentes; tratar valores ausentes de forma justificada; construir uma matriz de correlação e interpretá-la; converter uma variável categórica em variável numérica; e particionar os dados em treino e teste com `train_test_split`, incluindo a decisão de estratificar — e por que uma divisão aleatória ingênua é arriscada quando os dados têm estrutura espacial.
**Pré-requisito:** [[24-machine-learning-geociencias-aula-01-inteligencia-artificial-geociencias-ramos-aprendizado-dados|Aula 01 — Inteligência artificial em geociências]] (a distinção entre aprendizado supervisionado/não supervisionado e os desafios de autocorrelação espacial e escassez de rótulos, discutidos ali em teoria, viram código nesta aula). Pressupõe a base de Python/NumPy/Matplotlib do [[23-modelagem-numerica-geodinamica/23-modelagem-numerica-geodinamica-aula-01-python-jupyter-numpy-matplotlib|Módulo 23, Aula 01]].

## Conteúdo

### As cinco primeiras etapas de um projeto de aprendizado de máquina

Um projeto de aprendizado de máquina não começa escolhendo um algoritmo — começa com uma sequência de decisões que, se malfeitas, nenhum algoritmo consegue compensar depois. As cinco primeiras, que esta aula percorre em ordem sobre um único conjunto de dados, são: **(1) definição do problema** — que pergunta exatamente está sendo respondida, e com que tipo de aprendizado (Aula 01); **(2) coleta** — de onde os dados vêm e em que formato chegam; **(3) preparação** — limpeza, tratamento de valores ausentes, codificação de variáveis categóricas; **(4) análise exploratória** (*exploratory data analysis*, EDA) — entender a distribuição e as relações entre variáveis antes de ajustar qualquer modelo; e **(5) particionamento** — separar uma fração dos dados que o modelo nunca vê durante o treino, reservada exclusivamente para medir o desempenho no final (Aulas 03, 04, 06 e 07 usam essa mesma divisão).

### 1. Definição do problema

O conjunto de dados desta aula simula uma campanha de amostragem geoquímica de solo em prospecção de cobre-ouro: 60 amostras, cada uma com a distância medida até uma estrutura (falha) associada à mineralização, a litologia de caixa, a cota topográfica, e os teores de cobre (Cu), arsênio (As) e zinco (Zn, em ppm) — elementos pathfinder comuns em sistemas epitermais e pórfiros —, além do teor de ouro (Au, em ppb) e um rótulo binário `anomalo` (1 = geoquimicamente anômala, 0 = background), definido operacionalmente como Cu acima de um limiar de 180 ppm, com uma pequena fração de rótulos invertidos para simular incerteza analítica e de campo. **Os dados são sintéticos**, gerados para fins didáticos com um padrão espacial deliberadamente realista (teor decaindo com a distância à estrutura, mais ruído), não uma campanha real — mas o fluxo de código abaixo é idêntico ao que se aplicaria a uma tabela de laboratório de verdade. Duas perguntas guiam o restante do módulo sobre este mesmo conjunto: **quanto ouro esperar numa amostra nova, dados os outros elementos** (regressão, Aula 03) e **esta amostra é geoquimicamente anômala ou não** (classificação, Aula 04).

### 2. Coleta

Em um projeto real, a coleta é `pd.read_csv("geoquimica.csv")` sobre um arquivo exportado do laboratório. Para que esta aula seja autocontida e reprodutível sem depender de um arquivo externo, o bloco abaixo gera a mesma tabela — rode-o uma vez para obter `geoquimica.csv`, que as Aulas 03 a 07 vão reabrir com `pd.read_csv`.

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(7)   # semente fixa: mesma tabela a cada execucao
n = 60

dist_falha = rng.uniform(5, 500, n)                     # m
litologia = rng.choice(["xisto", "granito"], size=n, p=[0.6, 0.4])
lito_xisto = (litologia == "xisto").astype(int)

Cu_ppm = 15 + 1200*np.exp(-dist_falha/150) + 25*lito_xisto + rng.normal(0, 60, n)
Cu_ppm = np.clip(Cu_ppm, 5, None)
As_ppm = np.clip(2 + 0.02*Cu_ppm + rng.normal(0, 4, n), 0.5, None)
Zn_ppm = np.clip(30 + 0.35*Cu_ppm + 20*lito_xisto + rng.normal(0, 35, n), 10, None)
cota_m = rng.uniform(800, 1400, n)                      # feicao IRRELEVANTE, de proposito
Au_ppb = np.clip(1 + 0.045*Cu_ppm + 0.5*As_ppm - 0.003*dist_falha + rng.normal(0, 9, n), 0.1, None)

base = (Cu_ppm > 180).astype(int)
flip = rng.random(n) < 0.12                              # 12%: ruido de rotulo
anomalo = np.where(flip, 1 - base, base)

df = pd.DataFrame({
    "amostra_id": [f"S{str(i+1).zfill(2)}" for i in range(n)],
    "dist_falha_m": np.round(dist_falha, 1), "litologia": litologia,
    "cota_m": np.round(cota_m, 1), "Cu_ppm": np.round(Cu_ppm, 1),
    "As_ppm": np.round(As_ppm, 2), "Zn_ppm": np.round(Zn_ppm, 1),
    "Au_ppb": np.round(Au_ppb, 2), "anomalo": anomalo,
})
df.loc[[5, 22, 41], "As_ppm"] = np.nan   # falhas de leitura de laboratorio, realistas
df.to_csv("geoquimica.csv", index=False)
print(df.shape)
```

**Saída esperada:** `(60, 9)` — 60 amostras, 9 colunas. Note a coluna `cota_m` (elevação): ela entra no conjunto de propósito, sem nenhuma relação real com a mineralização, para servir de teste de sanidade nas Aulas 03, 04 e 07 — um modelo bem ajustado deve aprender a **não** dar peso a ela.

### 3. Preparação: tipos, valores ausentes e codificação

O primeiro diagnóstico depois de carregar qualquer tabela é entender o que cada coluna contém e onde faltam dados:

```python
df = pd.read_csv("geoquimica.csv")
print(df.dtypes)
print(df.isna().sum())
```

**Saída esperada:** as colunas numéricas aparecem como `float64` (ou `int64` para `anomalo`) e `litologia`/`amostra_id` como texto; `df.isna().sum()` mostra `As_ppm    3` e zero para todas as demais — as três amostras (índices 5, 22 e 41) em que a leitura de arsênio falhou no laboratório, um cenário comum: nem sempre todo ensaio é concluído para toda amostra.

Há duas saídas padrão para valores ausentes: **descartar** a linha (`df.dropna()`), que perde informação sobre as demais colunas daquela amostra e só se justifica quando poucas linhas são afetadas e a variável é central; ou **imputar** um valor — o mais simples e mais comum em conjuntos pequenos é preencher com a **mediana** da coluna, por ser robusta a valores extremos (ao contrário da média):

```python
mediana_As = df["As_ppm"].median()
df["As_ppm"] = df["As_ppm"].fillna(mediana_As)
print(round(mediana_As, 2), df.isna().sum().sum())
```

**Saída esperada:** mediana de `7.82` (ppm), e `0` valores ausentes no total depois do preenchimento. Vale registrar a limitação: preencher com a mediana **atenua artificialmente** a variância daquela coluna e ignora qualquer relação entre `As_ppm` e as demais variáveis (uma amostra de Cu alto tende a ter As mais alto, Módulo 20 chamaria isso de correlação positiva) — para três valores ausentes em sessenta amostras o efeito é pequeno, mas a técnica não escala bem para uma fração grande de dados faltantes, caso em que métodos de imputação mais sofisticados (por regressão ou por vizinho mais próximo) seriam preferíveis.

A segunda tarefa de preparação é **codificar variáveis categóricas**: a maioria dos algoritmos de aprendizado de máquina espera entrada puramente numérica, e `litologia` (texto: "xisto"/"granito") precisa virar número antes de entrar em qualquer modelo. Com apenas duas categorias, a **codificação one-hot** (`pd.get_dummies`) cria uma única coluna binária:

```python
df_enc = pd.get_dummies(df, columns=["litologia"], drop_first=True)
print(df_enc[["litologia_xisto"]].head(3))
```

**Saída esperada:** uma nova coluna `litologia_xisto` substitui a coluna de texto `litologia`, exibindo `True` quando a amostra é xisto e `False` quando é granito — o `get_dummies` do pandas devolve as colunas indicadoras em **dtype booleano** por padrão (passe `dtype=int` se quiser literalmente 1 e 0 na tela), e o scikit-learn as consome como 1 e 0 sem nenhuma conversão adicional, de modo que a escolha do dtype não muda nenhum resultado das Aulas 03 a 07. `drop_first=True` evita criar uma coluna redundante para a segunda categoria, já implícita quando a primeira é `False` — com mais de duas categorias, o mesmo `get_dummies` criaria uma coluna binária por categoria menos uma.

### 4. Análise exploratória: descrever antes de modelar

Ajustar um modelo sobre dados que ninguém olhou primeiro é como interpretar um variograma sem ter olhado o histograma dos dados brutos (Módulo 20, Aula 01) — o risco de um erro grosseiro passar despercebido é alto. `df.describe()` resume cada coluna numérica por contagem, média, desvio-padrão e quartis:

```python
print(df.describe().round(2))
```

**Saída esperada (colunas selecionadas):** `Cu_ppm` varia de 5,0 a 1.202,4 ppm (média 365,4, mediana 271,1 — a média bem acima da mediana já denuncia uma distribuição assimétrica à direita, comum em dados geoquímicos, onde poucas amostras muito enriquecidas puxam a média para cima); `Au_ppb` vai de 0,1 a 73,5 (média 20,8); `anomalo` tem média 0,65 — ou seja, 65% das 60 amostras estão rotuladas como anômalas, uma proporção próxima o bastante de 50/50 para não caracterizar desbalanceamento severo (o oposto do cenário descrito na Aula 01, guardado de propósito para a Aula 06).

A matriz de correlação (`df.corr()`, a mesma ideia de coeficiente de correlação de Pearson do Módulo 20, Aula 01) mostra como as variáveis numéricas se relacionam par a par:

```python
cols = ["dist_falha_m", "cota_m", "Cu_ppm", "As_ppm", "Zn_ppm", "Au_ppb"]
print(df[cols].corr().round(2))
```

**Saída esperada:** `Cu_ppm` e `Zn_ppm` correlacionam fortemente entre si (r = 0,95) e ambos correlacionam negativamente com `dist_falha_m` (r = −0,90 e −0,85) — esperado, já que o teor decai com a distância à estrutura mineralizante por construção deste exemplo. `Au_ppb` correlaciona positivamente com Cu, As e Zn (r entre 0,85 e 0,89) — os três elementos carregam informação real sobre o ouro. E `cota_m`, a variável irrelevante inserida de propósito, não correlaciona com nada (|r| ≤ 0,10 com todas as demais) — o comportamento esperado de uma variável sem relação geológica real com a mineralização, e o primeiro sinal de que ela deveria pesar pouco em qualquer modelo ajustado nas próximas aulas.

Um gráfico complementa a tabela: um histograma de `Cu_ppm` (`plt.hist(df["Cu_ppm"], bins=12)`) tornaria visível a assimetria à direita que a comparação média/mediana já sugeriu, e um `plt.scatter(df["Cu_ppm"], df["Au_ppb"])` mostraria a relação positiva e aproximadamente linear entre os dois elementos citada acima. O **histograma** é o mesmo instrumento que o Módulo 20, Aula 01, já usava — ao lado do boxplot — para descrever dados de furo de sondagem antes da geoestatística; o **gráfico de dispersão** é novo aqui: lá a relação entre duas variáveis entrava por via algébrica, como coeficiente de correlação e reta de regressão, sem a nuvem de pontos.

### 5. Particionamento: treino e teste, e o perigo da divisão aleatória ingênua

A etapa final antes de qualquer modelo (Aulas 03 a 07) é reservar uma fração dos dados — tipicamente 20% a 30% — que o modelo **nunca vê durante o ajuste**, usada só no final para medir o desempenho em dado genuinamente novo. `train_test_split` do scikit-learn faz essa divisão:

```python
from sklearn.model_selection import train_test_split

feat_cols = ["dist_falha_m", "cota_m", "Cu_ppm", "As_ppm", "Zn_ppm", "litologia_xisto"]
X = df_enc[feat_cols]
y = df_enc["anomalo"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
print(X_train.shape, X_test.shape)
print(y_train.value_counts())
print(y_test.value_counts())
```

**Saída esperada:** `(45, 6) (15, 6)` — 45 amostras de treino, 15 de teste (25% de 60), a divisão exata pedida por `test_size=0.25`. `y_train.value_counts()` dá 29 anômalas e 16 background no treino; `y_test.value_counts()` dá 10 anômalas e 5 background no teste — em ambos os conjuntos a proporção de classes fica próxima da proporção original (65%/35%), porque o argumento `stratify=y` **força** essa preservação: sem ele, uma divisão puramente aleatória poderia, por azar, concentrar quase todas as amostras anômalas no treino e deixar o teste artificialmente fácil ou difícil. `random_state=42` fixa a semente do sorteio — qualquer pessoa que rode este código obtém exatamente a mesma divisão, o que torna o resultado reproduzível e comparável entre as Aulas 03, 06 e 07, que reaproveitam esta mesma partição.

**O aviso da Aula 01, em código.** `train_test_split` sorteia linhas **independentemente umas das outras** — a suposição i.i.d. que a maioria dos algoritmos assume. Se este conjunto de dados tivesse coordenadas geográficas e duas amostras vizinhas (a poucos metros uma da outra, quase-duplicatas espaciais por causa da continuidade geoquímica que o Módulo 20 formaliza como variograma) caíssem uma no treino e outra no teste, o desempenho medido no teste ficaria artificialmente otimista — o modelo estaria, na prática, sendo "lembrado" de uma amostra que viu no treino, não genuinamente testado em dado novo. Este conjunto de dados não carrega coordenadas x/y explícitas, então o `train_test_split` aleatório acima é adequado a ele tal como construído; mas a advertência vale para qualquer conjunto real com posição espacial conhecida, e a solução — **validação cruzada espacial**, particionando por blocos geográficos em vez de por sorteio amostra a amostra — é retomada em nível de recomendação na Aula 06, quando as métricas de validação estiverem definidas.

## Exemplo trabalhado

**Situação:** antes de prosseguir para a Aula 03, confirme que a preparação está completa e que o particionamento preserva a proporção de classes também para a variável de **regressão** (`Au_ppb`), que não tem classes para estratificar.

```python
X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(
    X, df_enc["Au_ppb"], test_size=0.25, random_state=42
)
print(X_train_r.shape, X_test_r.shape)
print(round(y_train_r.mean(), 2), round(y_test_r.mean(), 2))
```

**Saída esperada:** `(45, 6) (15, 6)`, com médias de `Au_ppb` de aproximadamente 18,7 ppb no treino e 27,1 ppb no teste — a média do teste é cerca de 45% mais alta que a do treino (27,06/18,74 = 1,44), porque `stratify` não se aplica a uma variável contínua (só a rótulos categóricos): não há como forçar duas fatias de uma variável numérica a terem exatamente a mesma média por sorteio de linhas inteiras, e com apenas 60 amostras uma divisão aleatória pode facilmente concentrar por acaso algumas amostras de teor alto num dos dois lados. É um bom lembrete prático: em conjuntos pequenos vale sempre conferir esse tipo de desbalanceamento residual antes de confiar no resultado de um modelo de regressão — se o conjunto de teste, por sorteio, ficou com uma média bem mais alta que o treino, um erro de previsão que pareça grande em valor absoluto (Aula 06 formaliza essa medida) pode refletir esse deslocamento, não necessariamente um modelo ruim. É exatamente o hábito de "prever/checar antes de confiar no resultado" que o Módulo 23 já havia estabelecido para gráficos, agora aplicado a uma tabela de números.

## Recap relâmpago

- As cinco primeiras etapas de um projeto de ML: **definição do problema** (que pergunta, que tipo de aprendizado), **coleta**, **preparação**, **análise exploratória** e **particionamento** — nesta ordem, porque cada uma depende da anterior.
- **Valores ausentes**: descartar (`dropna`) perde informação e só se justifica com poucas linhas afetadas; imputar pela **mediana** (`fillna`) é o padrão simples para poucos valores ausentes, mas atenua a variância e ignora correlações entre colunas.
- **Variáveis categóricas** precisam virar numéricas antes de entrar num modelo — `pd.get_dummies` faz a **codificação one-hot**.
- `df.describe()` e `df.corr()` resumem distribuição e relações entre variáveis antes de qualquer ajuste — comparar média e mediana denuncia assimetria; uma variável irrelevante deliberadamente incluída (`cota_m`) serve de teste de sanidade porque não deveria correlacionar com nada.
- `train_test_split(..., stratify=y, random_state=...)` reserva uma fração dos dados (aqui 25%) exclusivamente para avaliação final, preservando a proporção de classes quando `stratify` é usado; a semente fixa (`random_state`) garante reprodutibilidade.
- **Uma divisão aleatória ingênua vaza informação quando os dados têm estrutura espacial**: amostras vizinhas quase-duplicatas caindo em conjuntos diferentes inflam artificialmente o desempenho medido — a validação cruzada espacial (blocos geográficos) é a correção, retomada na Aula 06.

## Próxima aula

[[24-machine-learning-geociencias-aula-03-modelagem-supervisionada-regressao|Aula 03 — Modelagem supervisionada: regressão]] — usa exatamente esta tabela preparada e esta mesma partição treino/teste para ajustar os primeiros modelos do módulo.

## Fontes

- pandas como biblioteca padrão de manipulação de dados tabulares em Python, incluindo tratamento de valores ausentes (`isna`, `fillna`, `dropna`) e codificação categórica (`get_dummies`): McKinney, W. (2010), "Data Structures for Statistical Computing in Python", *Proceedings of the 9th Python in Science Conference*, 56-61; documentação oficial pandas (pandas.pydata.org), versão 3.0.
- scikit-learn como biblioteca padrão de aprendizado de máquina em Python, incluindo `train_test_split` e o parâmetro `stratify`: Pedregosa, F. et al. (2011), "Scikit-learn: Machine Learning in Python", *Journal of Machine Learning Research*, 12, 2825-2830; documentação oficial scikit-learn (scikit-learn.org), versão 1.9.
- Imputação de valores ausentes pela mediana como método simples e robusto a outliers, e suas limitações (atenuação de variância, ignorância de correlação entre variáveis): Hastie, T., Tibshirani, R. & Friedman, J., *The Elements of Statistical Learning*, 2ª ed. (2009), Springer, cap. 9.6.
- Risco de vazamento de informação por particionamento aleatório de dados com estrutura espacial, e a validação cruzada em blocos como correção: Roberts, D. R. et al. (2017), "Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure", *Ecography*, 40(8), 913-929, DOI 10.1111/ecog.02881.

<!--
nivel: avancado
palavras_corpo: 2330
mapa_objetivo_secao:
  geologia-avancado-m24-oa02: "As cinco primeiras etapas de um projeto de aprendizado de máquina" + "1. Definição do problema" + "2. Coleta" + "3. Preparação: tipos, valores ausentes e codificação" + "4. Análise exploratória: descrever antes de modelar" + "5. Particionamento: treino e teste, e o perigo da divisão aleatória ingênua" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: MLGEO-M24-A02-DATASET-SHAPE-001
    claim: "O conjunto de dados sintetico gerado pelo codigo da aula (seed=7, n=60) tem forma (60, 9) apos a construcao, com 3 valores ausentes na coluna As_ppm (indices 5, 22 e 41) e zero valores ausentes em todas as demais colunas."
    risk: calculo
    source: "Execucao direta do codigo apresentado na aula (Python 3.13.2, NumPy 2.5.1, pandas 3.0.3). CONFIRMADO POR EXECUCAO em 2026-09-20: df.shape = (60, 9); df.isna().sum() = {As_ppm: 3, demais colunas: 0}."
  - claim_id: MLGEO-M24-A02-MEDIANA-DESCRIBE-002
    claim: "Apos a geracao do conjunto de dados, a mediana de As_ppm (antes da imputacao) e 7.82 ppm; apos fillna com essa mediana, o total de valores ausentes no DataFrame e 0. describe() do conjunto mostra Cu_ppm com minimo 5.0, maximo 1202.4, media 365.37 e mediana (50%) 271.05 ppm; Au_ppb com minimo 0.1, maximo 73.48, media 20.82 ppb; e anomalo com media 0.65 (65% das 60 amostras rotuladas como anomalas)."
    risk: calculo
    source: "Execucao direta do codigo apresentado na aula. CONFIRMADO POR EXECUCAO em 2026-09-20 (pandas 3.0.3): valores batem digito a digito com os relatados no texto."
  - claim_id: MLGEO-M24-A02-CORRELACAO-003
    claim: "Na matriz de correlacao de Pearson do conjunto de dados da aula, Cu_ppm e Zn_ppm correlacionam com r=0.95; Cu_ppm e dist_falha_m com r=-0.90; Zn_ppm e dist_falha_m com r=-0.85; Au_ppb correlaciona com Cu_ppm (r=0.89), As_ppm (r=0.85) e Zn_ppm (r=0.89); e cota_m (variavel irrelevante incluida deliberadamente) nao correlaciona com nenhuma outra variavel numerica do conjunto, com todos os coeficientes de correlacao envolvendo cota_m tendo modulo menor ou igual a 0.10."
    risk: calculo
    source: "Execucao direta de df[cols].corr() sobre o conjunto de dados da aula. CONFIRMADO POR EXECUCAO em 2026-09-20 (pandas 3.0.3, NumPy 2.5.1): matriz de correlacao reproduzida digito a digito (arredondada a duas casas) conforme relatado no texto."
  - claim_id: MLGEO-M24-A02-PARTICIONAMENTO-004
    claim: "train_test_split(X, y, test_size=0.25, random_state=42, stratify=y) sobre o conjunto de dados da aula (60 amostras, y=anomalo com 39 casos positivos e 21 negativos) produz X_train com forma (45,6) e X_test com forma (15,6), com y_train contendo 29 casos positivos e 16 negativos e y_test contendo 10 positivos e 5 negativos - preservando a proporcao aproximada de 65%/35% da variavel original em ambos os subconjuntos gracas ao argumento stratify. Sem esse argumento, train_test_split sorteia linhas de forma independente entre si (premissa i.i.d.), o que pode concentrar desproporcionalmente uma classe em um dos subconjuntos por acaso, especialmente em conjuntos de dados pequenos."
    risk: calculo
    source: "Execucao direta do codigo apresentado na aula (scikit-learn 1.9.1). CONFIRMADO POR EXECUCAO em 2026-09-20: X_train.shape=(45,6), X_test.shape=(15,6), y_train.value_counts()={1:29,0:16}, y_test.value_counts()={1:10,0:5}."
  - claim_id: MLGEO-M24-A02-PARTICIONAMENTO-REGRESSAO-005
    claim: "Para o mesmo conjunto de dados, train_test_split(X, Au_ppb, test_size=0.25, random_state=42) sem estratificacao produz X_train e X_test com formas (45,6) e (15,6), com media de Au_ppb de aproximadamente 18.7 ppb no treino e 27.1 ppb no teste - a media do teste sendo cerca de 45% mais alta que a do treino (27.06/18.74 = 1.444), porque o argumento stratify do scikit-learn se aplica apenas a variaveis categoricas, nao a variaveis numericas continuas, e com apenas 60 amostras o sorteio aleatorio pode concentrar por acaso amostras de teor mais alto em um dos dois subconjuntos."
    risk: calculo
    source: "Execucao direta do codigo apresentado na aula (scikit-learn 1.9.1). CONFIRMADO POR EXECUCAO em 2026-09-20: y_train_r.mean() = 18.74, y_test_r.mean() = 27.06, batendo com os valores relatados no texto (arredondados a uma casa decimal)."
  - claim_id: MLGEO-M24-A02-IMPUTACAO-LIMITACOES-006
    claim: "Imputar valores ausentes pela mediana da coluna e um metodo simples e robusto a valores extremos (ao contrario da media), mas atenua artificialmente a variancia da coluna imputada e ignora qualquer correlacao entre a variavel com dados ausentes e as demais variaveis do conjunto; a limitacao se torna mais severa quanto maior a fracao de dados ausentes na coluna."
    risk: fato
    source: "Hastie, T., Tibshirani, R. & Friedman, J., The Elements of Statistical Learning, 2a ed. (2009), Springer, secao 9.6 (tratamento de valores ausentes)."
  - claim_id: MLGEO-M24-A02-GETDUMMIES-DTYPE-007
    claim: "pd.get_dummies devolve as colunas indicadoras em dtype booleano por padrao (o parametro dtype tem valor padrao bool), de modo que print(df_enc[['litologia_xisto']].head(3)) exibe True/False e nao 1/0; passar dtype=int produz as colunas como inteiros. A escolha do dtype nao altera nenhum resultado numerico dos modelos, porque o scikit-learn consome colunas booleanas como 1 e 0."
    risk: calculo
    source: "Documentacao oficial pandas, funcao pandas.get_dummies (pandas.pydata.org), versao 3.0: parametro 'dtype: dtype, default bool'. CONFIRMADO POR EXECUCAO em 2026-09-20 (pandas 3.0.3): a saida impressa das tres primeiras linhas e False/False/False. ACHADO 3 DA AUDITORIA de 2026-09-20 (a aula declarava 1/0 como saida)."
  - claim_id: MLGEO-M24-A02-ATRIBUICAO-M20-GRAFICOS-008
    claim: "Os instrumentos graficos efetivamente usados pelo Modulo 20, Aula 01 (Preparacao de dados e estatistica descritiva) deste curso sao o HISTOGRAMA e o BOXPLOT. Aquela aula NAO usa grafico de dispersao (nem a expressao aparece nela): a relacao entre duas variaveis e tratada algebricamente, por coeficiente de correlacao de Pearson e reta de regressao linear simples. Logo, o par 'histograma + grafico de dispersao' NAO pode ser atribuido ao Modulo 20; o histograma pode, a dispersao e introduzida nesta aula."
    risk: fato
    source: "Verificacao direta contra o arquivo do proprio curso 20-geoestatistica/20-geoestatistica-aula-01-preparacao-dados-estatistica-descritiva.md em 2026-09-21: secao 'Histograma, boxplot e o problema dos valores extremos' e secao 'Estatistica bivariada: correlacao e regressao'; busca textual por 'dispersao'/'scatter' no arquivo retorna somente 'medidas de dispersao' (no sentido de espalhamento estatistico), nunca um grafico. ACHADO 16 DA AUDITORIA de 2026-09-21 (a aula atribuia ao Modulo 20 um par de instrumentos graficos que ele nao usa; no mesmo trecho havia o anglicismo 'used' por 'usado', corrigido junto)."
-->
