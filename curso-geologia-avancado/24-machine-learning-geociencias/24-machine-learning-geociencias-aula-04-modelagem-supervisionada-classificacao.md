# Aula 04: Modelagem supervisionada — classificação: regressão logística e floresta aleatória

**ID:** geologia-avancado-m24-a04
**Módulo:** [[24-machine-learning-geociencias-modulo|Módulo 24 — Fundamentos e aplicações de machine learning em geociências]]
**Duração estimada:** ~17 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** ajustar os dois modelos de classificação do módulo — regressão logística e floresta aleatória — para prever se uma amostra é geoquimicamente anômala, e ler o resultado numa matriz de confusão, percebendo por que aqui o modelo mais flexível vence, ao contrário do que aconteceu na regressão da Aula 03.
**Ao final você vai conseguir:** explicar por que a classificação linear é feita por regressão **logística** e não por regressão linear; treinar `LogisticRegression` e `RandomForestClassifier` no scikit-learn; ler as quatro células de uma matriz de confusão; e explicar, a partir de um resultado concreto, por que a fronteira de decisão deste problema favorece um método que particiona o espaço em regiões em vez de traçar um único plano.
**Pré-requisito:** [[24-machine-learning-geociencias-aula-03-modelagem-supervisionada-regressao|Aula 03 — Modelagem supervisionada: regressão]] (esta aula é a **Parte 2** do par: usa a mesma tabela `geoquimica.csv` e os mesmos dois algoritmos, agora sobre um rótulo categórico; a leitura de importância de variável e a ressalva sobre o viés de cardinalidade foram estabelecidas ali).

> [!note] Esta aula é a **Parte 2** de um par. A [[24-machine-learning-geociencias-aula-03-modelagem-supervisionada-regressao|Aula 03 — Parte 1]] cobre a tarefa de **regressão** (prever um número: o teor de ouro) com os mesmos dois algoritmos, e fecha com a krigagem do Módulo 20 como parente da regressão linear. As duas aulas juntas cobrem a metade supervisionada do objetivo `oa03`; estude-as em sequência.

## Conteúdo

### Classificação: prever uma categoria

O mesmo par de algoritmos da Aula 03 — um modelo linear e uma floresta aleatória — se aplica à tarefa de classificação, prevendo `anomalo` (1 = geoquimicamente anômala, 0 = background). A versão linear de classificação **não** é a regressão linear (que prevê qualquer número real, sem limite, e portanto responderia coisas como "esta amostra é 1,7 anômala"), e sim a **regressão logística**: em vez de prever diretamente 0 ou 1, ela prevê a **probabilidade** de a amostra pertencer à classe 1, passando a combinação linear das variáveis por uma função logística (sigmoide) que a comprime para o intervalo (0, 1):

$$P(y=1 \mid x) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x_1 + \dots + \beta_p x_p)}}$$

Uma amostra é classificada como 1 quando essa probabilidade excede um limiar (0,5 por padrão no scikit-learn). Note o que continua igual e o que muda em relação à Parte 1: a **combinação linear** $\beta_0 + \beta_1 x_1 + \dots$ é exatamente a mesma da regressão linear, com os mesmos coeficientes a estimar; o que se acrescenta é a sigmoide por cima dela, e é ela que transforma uma previsão de número ilimitado numa previsão de probabilidade.

O bloco abaixo é autocontido — reabre a tabela e refaz a partição, agora **estratificada** pelo rótulo (`stratify=y2`, Aula 02), para que as duas classes apareçam no teste na mesma proporção em que aparecem no conjunto inteiro:

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv("geoquimica.csv")
df["As_ppm"] = df["As_ppm"].fillna(df["As_ppm"].median())
df_enc = pd.get_dummies(df, columns=["litologia"], drop_first=True)
feat_cols = ["dist_falha_m", "cota_m", "Cu_ppm", "As_ppm", "Zn_ppm", "litologia_xisto"]

X, y2 = df_enc[feat_cols], df_enc["anomalo"]
X_train2, X_test2, y_train2, y_test2 = train_test_split(
    X, y2, test_size=0.25, random_state=42, stratify=y2
)

logit = LogisticRegression(max_iter=2000).fit(X_train2, y_train2)
pred_logit = logit.predict(X_test2)
print("acuracia (logistica):", round(accuracy_score(y_test2, pred_logit), 3))
print(confusion_matrix(y_test2, pred_logit))

rfc = RandomForestClassifier(n_estimators=300, random_state=42).fit(X_train2, y_train2)
pred_rfc = rfc.predict(X_test2)
print("acuracia (floresta):", round(accuracy_score(y_test2, pred_rfc), 3))
print(confusion_matrix(y_test2, pred_rfc))
print(dict(zip(feat_cols, np.round(rfc.feature_importances_, 3))))
```

**Saída esperada:** regressão logística acerta **86,7%** das 15 amostras de teste (13 de 15), com matriz de confusão `[[4, 1], [1, 9]]` — 4 background corretamente identificados, 1 background classificado como anômalo (**falso positivo**), 1 anômalo classificado como background (**falso negativo**), 9 anômalos corretamente identificados. A floresta aleatória de classificação acerta **93,3%** (14 de 15), com matriz `[[5, 0], [1, 9]]` — zero falsos positivos aqui, e a mesma única confusão persistente (1 falso negativo). A matriz de confusão e o vocabulário de falso positivo/negativo são **formalizados na Aula 06**, junto com as métricas que se calculam a partir dela; por ora basta ler as quatro células como quatro contagens.

**Por que aqui o modelo mais flexível venceu.** Ao contrário da regressão da Parte 1, a floresta supera o modelo linear nesta tarefa. A razão está na **fronteira de decisão** do problema: `anomalo` foi definido, na construção deste exemplo (Aula 02), por um limiar rígido de cobre (180 ppm) mais 12% de ruído de rótulo. Uma fronteira desse tipo — um corte abrupto em uma variável — não é uma reta suave no espaço das variáveis, e um método que particiona o espaço em regiões retangulares (como a árvore de decisão) tem uma vantagem estrutural sobre um método que só pode traçar um único plano de separação (a regressão logística). Vale guardar o par de resultados das duas partes lado a lado, porque ele desmonta as duas generalizações fáceis: na **regressão**, o modelo simples ganhou; na **classificação**, sobre exatamente os mesmos dados, o modelo flexível ganhou. Não existe "o melhor algoritmo" — existe o algoritmo que se ajusta à forma do problema.

A importância de variável da floresta classificadora reforça a leitura: `Cu_ppm` (0,349) e `dist_falha_m` (0,261) dominam — coerente com `anomalo` ter sido definido, por construção, diretamente a partir do cobre —, e `litologia_xisto` (0,025) e `cota_m` (0,086) contribuem pouco. Aqui aparece, com números, a inversão que a Aula 03 anunciou: a cota, irrelevante por construção, fica **acima** da litologia, que é uma variável geológica real. Não leia isso como "a elevação informa mais que a rocha encaixante"; é o **viés de cardinalidade** da importância por impureza, que favorece a variável contínua sobre a binária.

## Exemplo trabalhado

**Situação:** você precisa recomendar um dos dois classificadores para triagem de amostras numa campanha de prospecção. As duas acurácias — 0,867 e 0,933 — apontam para a floresta. Antes de fechar a recomendação, leia as **duas matrizes de confusão lado a lado** e diga o que o número único esconde.

| | Logística `[[4, 1], [1, 9]]` | Floresta `[[5, 0], [1, 9]]` |
|---|---|---|
| Background acertado (TN) | 4 | 5 |
| Background previsto como anômalo (FP) | **1** | **0** |
| Anômalo previsto como background (FN) | **1** | **1** |
| Anômalo acertado (TP) | 9 | 9 |
| Erros totais | 2 de 15 | 1 de 15 |
| Acurácia | 13/15 = 0,867 | 14/15 = 0,933 |

**Resolução.** A diferença entre 0,867 e 0,933 é **um único erro** — e não um erro qualquer. Repare que os dois modelos deixam passar a **mesma quantidade de anômalas**: 1 falso negativo cada. Toda a vantagem da floresta está no falso positivo que a logística comete e ela não.

Isso importa porque os dois tipos de erro **não custam a mesma coisa** numa campanha real. O falso negativo é um alvo geoquímico perdido — uma amostra anômala arquivada como background, e possivelmente uma mineralização que ninguém volta a investigar. O falso positivo é dinheiro gasto: uma amostra estéril que entra na lista de prioridades e consome um furo de sondagem. Qual dos dois é mais grave depende do orçamento e do estágio da campanha, não do algoritmo — e é uma decisão do geólogo, não do modelo.

A conclusão prática, então, é mais fraca do que "a floresta é melhor": **a floresta é melhor em acurácia, e as duas são iguais no erro que mais dói numa exploração** (deixar passar anômala). Uma acurácia única somou dois erros de naturezas diferentes e devolveu um número em que essa diferença desapareceu — exatamente a limitação que a Aula 06 vai atacar, apresentando métricas que olham cada tipo de erro separadamente, em vez de misturá-los numa fração só.

## Recap relâmpago

- **Regressão logística** é o análogo linear da classificação: aplica uma **sigmoide** à mesma combinação linear da regressão linear, devolvendo uma **probabilidade** em (0, 1) em vez de um número ilimitado; o scikit-learn classifica como positiva toda amostra com probabilidade acima de **0,5** por padrão.
- A partição de classificação é **estratificada** (`stratify=y2`, Aula 02), para que a proporção entre anômalas e background do conjunto inteiro se preserve no treino e no teste.
- A **matriz de confusão** `[[TN, FP], [FN, TP]]` é a leitura mínima de um classificador: quatro contagens, não uma. Nesta partição, a logística dá `[[4, 1], [1, 9]]` (acurácia 0,867) e a floresta `[[5, 0], [1, 9]]` (acurácia 0,933).
- **A floresta venceu aqui, e perdeu na regressão da Parte 1**, sobre exatamente os mesmos dados. A explicação é a forma da fronteira de decisão: um limiar rígido de cobre com ruído de rótulo favorece quem particiona o espaço em regiões, não quem traça um plano. Nenhum algoritmo é melhor em abstrato.
- A `feature_importances_` da floresta classificadora confirma `Cu_ppm` como dominante — e exibe, com números, o **viés de cardinalidade** anunciado na Aula 03: `cota_m` (0,086), que é ruído por construção, fica acima de `litologia_xisto` (0,025), que é informação geológica real.
- Uma **acurácia única esconde a natureza dos erros**: as duas matrizes desta aula têm o mesmo número de falsos negativos, e é só no falso positivo que elas diferem. Em exploração, falso negativo (alvo perdido) e falso positivo (furo gasto em estéril) custam coisas diferentes.

## Próxima aula

[[24-machine-learning-geociencias-aula-05-modelagem-nao-supervisionada-agrupamento-reducao-dimensionalidade|Aula 05 — Modelagem não supervisionada: agrupamento e redução de dimensionalidade]] — usa as mesmas variáveis geoquímicas, agora **sem nenhum rótulo**, para descobrir estrutura nos dados por conta própria, e compara o resultado com a classificação desta aula.

## Fontes

- Regressão logística como o análogo linear de classificação, função sigmoide e limiar de decisão: Hastie, T., Tibshirani, R. & Friedman, J., *The Elements of Statistical Learning*, 2ª ed. (2009), Springer, cap. 4; Géron, A., *Hands-On Machine Learning with Scikit-Learn, Keras and TensorFlow*, 3ª ed. (2022), O'Reilly, cap. 4.
- Florestas aleatórias em classificação (voto majoritário, subamostragem aleatória de variáveis, importância de variável): Breiman, L. (2001), "Random Forests", *Machine Learning*, 45(1), 5-32, DOI 10.1023/A:1010933404324; Hastie, Tibshirani & Friedman, cap. 15.
- API do scikit-learn para `LogisticRegression`, `RandomForestClassifier`, `confusion_matrix` e `feature_importances_`, e o viés da importância por impureza a favor de variáveis de alta cardinalidade: documentação oficial scikit-learn (scikit-learn.org), versão 1.9.

<!--
nivel: avancado
palavras_corpo: 1341
mapa_objetivo_secao:
  geologia-avancado-m24-oa03: "Classificação: prever uma categoria" + "Exemplo trabalhado"

origem: "Aula criada em 2026-09-21 pela revisao didatica, como Parte 2 da divisao da antiga Aula 03 (achado DID-M24-A03-CARGA-001). O corte foi tarefa de REGRESSAO (Parte 1, Aula 03) contra tarefa de CLASSIFICACAO (Parte 2, esta aula). A secao 'Classificacao: prever uma categoria' e o bloco de codigo vieram da antiga Aula 03 e foram PRESERVADOS palavra por palavra, com tres acrescimos: (i) um preambulo de codigo que torna a aula autocontida (leitura do CSV, imputacao, codificacao e particao estratificada, no mesmo padrao autocontido da ultima aula do modulo); (ii) duas frases de ponte com a Parte 1 (o que a sigmoide acrescenta a combinacao linear, e o par de resultados contrario entre as duas tarefas); (iii) um exemplo trabalhado NOVO e um Recap NOVO. Os claim_id herdados NAO foram renumerados: os prefixos A03 designam a numeracao em que a alegacao foi emitida.

alegacoes_auditaveis:
  - claim_id: MLGEO-M24-A03-CLASSIFICACAO-RESULTADO-003
    claim: "Para a tarefa de classificacao (alvo anomalo, mesma particao estratificada da Aula 02), LogisticRegression(max_iter=2000) obtem acuracia 0.867 (13 de 15 amostras de teste) com matriz de confusao [[4,1],[1,9]] (formato [[TN,FP],[FN,TP]]); RandomForestClassifier(n_estimators=300, random_state=42) obtem acuracia 0.933 (14 de 15) com matriz de confusao [[5,0],[1,9]], com importancias de variavel dist_falha_m=0.261, cota_m=0.086, Cu_ppm=0.349, As_ppm=0.161, Zn_ppm=0.118, litologia_xisto=0.025 - a floresta supera o modelo linear nesta tarefa, ao contrario do que ocorreu na regressao de Au_ppb (Aula 03)."
    risk: calculo
    source: "Execucao direta do codigo apresentado na aula (scikit-learn 1.9.1). CONFIRMADO POR EXECUCAO em 2026-09-20 na antiga Aula 03 e REVERIFICADO em 2026-09-21 sobre o bloco autocontido desta aula: valores reproduzidos digito a digito, incluindo as duas matrizes de confusao completas e as seis importancias de variavel. Alegacao herdada da antiga Aula 03 pela divisao didatica; claim_id preservado sem renumeracao."
  - claim_id: MLGEO-M24-A03-REGRESSAO-LOGISTICA-CONCEITO-005
    claim: "A regressao logistica modela a probabilidade de uma observacao pertencer a classe positiva aplicando a funcao sigmoide (logistica) a uma combinacao linear das variaveis explicativas, P(y=1|x) = 1/(1+exp(-(b0+b1x1+...+bpxp))), comprimindo o resultado para o intervalo aberto (0,1); por padrao, o scikit-learn classifica como positiva toda observacao com probabilidade prevista acima de 0.5."
    risk: fato
    source: "Hastie, T., Tibshirani, R. & Friedman, J., The Elements of Statistical Learning, 2a ed. (2009), Springer, cap. 4; documentacao oficial scikit-learn, classe LogisticRegression (scikit-learn.org), versao 1.9. Alegacao herdada da antiga Aula 03 pela divisao didatica; claim_id preservado sem renumeracao."
  - claim_id: MLGEO-M24-A04-EXEMPLO-MATRIZES-LADO-A-LADO-001
    claim: "Comparando as duas matrizes de confusao desta aula celula por celula: a logistica tem TN=4, FP=1, FN=1, TP=9 (2 erros em 15, acuracia 13/15=0.867) e a floresta tem TN=5, FP=0, FN=1, TP=9 (1 erro em 15, acuracia 14/15=0.933). Os dois modelos tem o MESMO numero de falsos negativos (1), e toda a diferenca de acuracia entre eles esta no unico falso positivo que a logistica comete e a floresta nao. Logo, a diferenca 0.867 contra 0.933 nao corresponde a nenhuma vantagem da floresta no erro de deixar passar uma amostra anomala."
    risk: calculo
    source: "Aritmetica direta sobre as duas matrizes de confusao ja confirmadas por execucao (ver claim MLGEO-M24-A03-CLASSIFICACAO-RESULTADO-003): 13/15=0.8667 e 14/15=0.9333; contagem de celulas conferida a mao. Alegacao NOVA, nascida do exemplo trabalhado criado pela divisao didatica de 2026-09-21, e verificada na mesma passagem - NAO fica pendente de auditoria. Deliberadamente NAO usa precisao, revocacao nem F1, que sao definidas so na Aula 06: o exemplo trabalha apenas com contagens de celula e acuracia, ja disponiveis nesta altura do modulo."
-->
