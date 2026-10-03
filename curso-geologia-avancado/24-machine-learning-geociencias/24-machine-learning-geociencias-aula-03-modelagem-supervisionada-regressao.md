# Aula 03: Modelagem supervisionada — regressão: linear, floresta aleatória e a krigagem como parente

**ID:** geologia-avancado-m24-a03
**Módulo:** [[24-machine-learning-geociencias-modulo|Módulo 24 — Fundamentos e aplicações de machine learning em geociências]]
**Duração estimada:** ~28 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** ajustar e comparar dois modelos de regressão — regressão linear múltipla e floresta aleatória — para prever o teor de ouro sobre o conjunto de dados preparado na Aula 02, aprender a ler (e a não ler) os coeficientes e a importância de variável, e situar a krigagem do Módulo 20 como um parente conceitual da regressão linear.
**Ao final você vai conseguir:** treinar e usar `LinearRegression` e `RandomForestRegressor` no scikit-learn; interpretar os coeficientes de um modelo linear na escala certa e reconhecer o viés da importância de variável de uma floresta; explicar por que a krigagem ordinária pertence, formalmente, à família dos mínimos quadrados generalizados (GLS) — e por que isso não é a mesma coisa que modelo linear generalizado (GLM); e reconhecer, num resultado concreto, quando um modelo mais simples (linear) supera um modelo mais flexível (floresta aleatória) e por quê.
**Pré-requisito:** [[24-machine-learning-geociencias-aula-02-fluxo-trabalho-python-preparacao-exploracao-particionamento|Aula 02 — Fluxo de trabalho em Python]] (usa a mesma tabela `geoquimica.csv`, já preparada e codificada, e a mesma partição treino/teste). [[20-geoestatistica/20-geoestatistica-aula-05-krigagem-simples-ordinaria|Módulo 20, Aula 05 — Krigagem simples e ordinária]] para a comparação com regressão.

> [!note] Esta aula é a **Parte 1** de um par. Ela cobre a tarefa de **regressão** — prever um número — com os dois algoritmos do módulo, e fecha situando a krigagem do Módulo 20 em relação à regressão linear. A [[24-machine-learning-geociencias-aula-04-modelagem-supervisionada-classificacao|Aula 04 — Parte 2]] aplica **os mesmos dois algoritmos** à tarefa de **classificação** — prever uma categoria — e mostra que a ordem entre eles se inverte. O par foi dividido porque as duas tarefas, juntas, passavam de 34 minutos; estude as duas em sequência.

## Conteúdo

### Regressão: prever um número contínuo

A Aula 01 definiu regressão como a tarefa supervisionada em que o rótulo é numérico contínuo. Aqui o rótulo é o teor de ouro (`Au_ppb`), e as variáveis explicativas (*features*) são distância à falha, cota, Cu, As, Zn e a litologia codificada — a mesma tabela preparada na Aula 02.

O modelo mais simples é a **regressão linear múltipla**, que estende a regressão linear simples do Módulo 20 (Aula 01, correlação e regressão de duas variáveis) para várias variáveis explicativas ao mesmo tempo:

$$\hat{y} = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_p x_p$$

onde $\hat y$ é o valor previsto, $\beta_0$ o intercepto, e cada $\beta_i$ o **coeficiente** associado à variável $x_i$ — o quanto $\hat y$ muda, em média, para um aumento de uma unidade em $x_i$, mantendo as demais variáveis constantes. Os coeficientes são ajustados (o "aprendizado") minimizando a soma dos quadrados dos resíduos entre valor previsto e valor observado no conjunto de treino — o **método dos mínimos quadrados**, o mesmo princípio da regressão linear simples do Módulo 20, agora generalizado para várias variáveis.

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("geoquimica.csv")
df["As_ppm"] = df["As_ppm"].fillna(df["As_ppm"].median())
df_enc = pd.get_dummies(df, columns=["litologia"], drop_first=True)
feat_cols = ["dist_falha_m", "cota_m", "Cu_ppm", "As_ppm", "Zn_ppm", "litologia_xisto"]

X = df_enc[feat_cols]
y = df_enc["Au_ppb"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

lr = LinearRegression().fit(X_train, y_train)
pred = lr.predict(X_test)

print(dict(zip(feat_cols, np.round(lr.coef_, 4))))
print("intercepto:", round(lr.intercept_, 4))
print("MAE:", round(mean_absolute_error(y_test, pred), 3))
print("RMSE:", round(mean_squared_error(y_test, pred)**0.5, 3))
print("R2:", round(r2_score(y_test, pred), 4))
```

**Saída esperada:** coeficientes aproximados `dist_falha_m = 0,0039`, `cota_m = −0,0033`, `Cu_ppm = 0,0202`, `As_ppm = 0,6881`, `Zn_ppm = 0,0561`, `litologia_xisto = 2,0303`, intercepto `−1,3053`. **MAE = 5,128**, **RMSE = 6,759**, **R² = 0,7879** (as três métricas são formalizadas na Aula 06; por ora, leia R² = 0,79 como "o modelo explica cerca de 79% da variação do ouro no conjunto de teste" — abaixo de 1,0 porque nenhuma previsão é perfeita, acima de 0 porque o modelo é bem melhor do que simplesmente prever a média para toda amostra). **Como (não) ler estes coeficientes.** A tentação imediata diante dessa lista é ordenar as variáveis por magnitude do coeficiente e chamar isso de importância. Ela precisa ser resistida, porque **um coeficiente de regressão não padronizada carrega a unidade da sua variável**: ele responde "quanto muda o ouro por *uma unidade* daquela variável", e uma unidade significa coisas muito diferentes em colunas de escalas diferentes. O coeficiente de `As_ppm` (0,6881) é 34 vezes maior que o de `Cu_ppm` (0,0202) não porque o arsênio informe 34 vezes mais sobre o ouro, mas porque o arsênio varia numa faixa 43 vezes mais estreita (desvio-padrão de 7,7 ppm no treino, contra 330,5 ppm do cobre — desvios **populacionais**, divisor $n$, que é a convenção do `StandardScaler`; `pandas.std()` usa o divisor $n-1$ e devolve 7,8 e 334,3, e a equivalência com o modelo padronizado, afirmada no parágrafo seguinte, só é exata na convenção populacional).

A comparação só fica honesta depois de pôr todas as variáveis na mesma escala — multiplicando cada coeficiente pelo desvio-padrão da sua variável, o que equivale a reajustar o modelo sobre variáveis padronizadas (`StandardScaler`, Aula 05). Feito isso, a ordem se inverte: `Zn_ppm` (7,05), `Cu_ppm` (6,66) e `As_ppm` (5,33) ficam próximos entre si e bem à frente de `litologia_xisto` (1,01), `cota_m` (−0,59) e `dist_falha_m` (0,58).

Duas leituras se seguem, ambas ecoando a Aula 02. Primeiro, o **teste de sanidade de `cota_m` funciona — mas só na escala certa**: o efeito padronizado da cota (−0,59) é uma ordem de grandeza menor que o dos três elementos, coerente com sua correlação quase nula já vista na EDA, o sinal de que o modelo não está inventando relação onde não há. Note que, nessa escala, `dist_falha_m` (0,58) cai no mesmo patamar baixo — e não porque a distância à falha seja irrelevante (a EDA mostrou r = −0,90 com o cobre), e sim porque o cobre, já dentro do modelo, absorveu quase toda a informação que a distância carregava. Um coeficiente parcial pequeno quer dizer "acrescenta pouco às demais variáveis", não "não tem relação com o alvo".

Segundo, essa redundância tem nome: a **multicolinearidade** identificada na Aula 02. Cu, As e Zn correlacionam fortemente entre si (r ≥ 0,82), então o modelo linear tem dificuldade em separar exatamente qual dos três "merece" o crédito pela variação do ouro, e reparte os coeficientes de um jeito que pode variar bastante com pequenas mudanças nos dados. Somadas as duas coisas — escala e multicolinearidade —, a conclusão prática é firme: os coeficientes individuais, nesse regime, devem ser lidos com cautela; a previsão conjunta (R² = 0,79) é mais confiável do que a interpretação isolada de qualquer coeficiente.

### Regressão com floresta aleatória: um modelo não linear

Uma **árvore de decisão** de regressão particiona o espaço das variáveis em regiões retangulares, sucessivamente, escolhendo a cada divisão a variável e o limiar que mais reduzem a dispersão do rótulo dentro de cada região resultante — ao contrário da regressão linear, não assume nenhuma forma funcional específica (linear, quadrática) entre variáveis e rótulo. Uma **floresta aleatória** (*random forest*) treina muitas árvores de decisão, cada uma sobre uma amostra aleatória (com reposição) dos dados de treino e um subconjunto aleatório de variáveis a cada divisão, e faz a previsão final pela **média** das previsões de todas as árvores — o "aleatório" reduz a variância que uma única árvore, ajustada a fundo, tende a ter.

```python
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(n_estimators=300, random_state=42).fit(X_train, y_train)
pred_rf = rf.predict(X_test)

print("MAE:", round(mean_absolute_error(y_test, pred_rf), 3))
print("RMSE:", round(mean_squared_error(y_test, pred_rf)**0.5, 3))
print("R2:", round(r2_score(y_test, pred_rf), 4))
print(dict(zip(feat_cols, np.round(rf.feature_importances_, 3))))
```

**Saída esperada:** **MAE = 5,778**, **RMSE = 7,582**, **R² = 0,7331** — pior do que a regressão linear nas três métricas. `n_estimators=300` fixa 300 árvores na floresta; `feature_importances_` retorna a **importância de variável**, uma medida (baseada na redução média de dispersão que cada variável proporciona nas divisões de todas as árvores) de quanto cada *feature* contribuiu para as previsões: `dist_falha_m = 0,240`, `cota_m = 0,025`, `Cu_ppm = 0,224`, `As_ppm = 0,234`, `Zn_ppm = 0,272`, `litologia_xisto = 0,006` — de novo, `cota_m` (a variável irrelevante) recebe a segunda menor importância, e a de menor importância de todas é justamente `litologia_xisto`, quase zero, sugerindo que a informação de litologia já está capturada indiretamente pelos teores geoquímicos correlacionados a ela. Essa última leitura, porém, precisa de uma ressalva que vale para toda `feature_importances_` de árvore: a importância por **redução de impureza** é documentadamente **enviesada a favor de variáveis de alta cardinalidade** (numéricas contínuas, com muitos valores distintos) e **contra** variáveis binárias ou categóricas de poucas categorias. Parte do valor quase nulo de `litologia_xisto`, que é binária, vem desse viés — não só da redundância com os teores. A prova está na floresta de classificação da Aula 04, onde `cota_m`, que é puro ruído por construção, recebe importância **maior** (0,086) do que `litologia_xisto` (0,025), que carrega informação geológica real. Para uma medida sem esse viés, e aplicável a qualquer modelo, a Aula 07 usa a **importância por permutação**.

**Por que o modelo mais simples venceu aqui.** Este não é um resultado universal — florestas aleatórias costumam superar a regressão linear quando a relação entre variáveis e rótulo é genuinamente não linear ou quando há interações complexas entre variáveis. Mas com **apenas 45 amostras de treino**, um modelo com muito mais capacidade de ajuste (uma floresta de 300 árvores, cada uma podendo se ramificar profundamente) tem menos dados por parâmetro efetivo para estimar de forma estável, e tende a captar ruído específico do conjunto de treino em vez de sinal genuinamente generalizável — um primeiro sinal do que a Aula 06 vai chamar de **sobreajuste**. A regressão linear, com uma forma funcional muito mais restrita (seis coeficientes e um intercepto, e a relação subjacente entre teor de elemento pathfinder e ouro sendo de fato aproximadamente linear neste exemplo, por construção), tem menos com que "errar" nessa amostra pequena. A lição prática — não a teórica — é: **o modelo mais sofisticado não é automaticamente o melhor**; a escolha depende dos dados disponíveis, e comparar candidatos no conjunto de teste, como feito aqui, é o único jeito confiável de saber qual funciona melhor num problema concreto.

### Krigagem como parente da regressão

O Módulo 20 (Aula 05) apresentou a krigagem ordinária como o **melhor estimador linear não-viesado** (BLUE): uma combinação linear ponderada de amostras vizinhas, $z^*(x_0) = \sum_i \lambda_i z(x_i)$, com os pesos $\lambda_i$ resolvidos a partir do modelo de variograma. Formalmente, a krigagem ordinária pertence à família dos **mínimos quadrados generalizados** (*generalized least squares*, GLS) — a generalização da regressão desta aula para o caso em que os resíduos **não** são independentes entre si, e sim correlacionados segundo uma estrutura de covariância conhecida, que na krigagem é justamente o variograma. (Um falso amigo a evitar: mínimos quadrados **generalizados**, GLS, não é a mesma coisa que modelo linear **generalizado**, GLM — esta segunda é a família a que pertence a regressão logística da Aula 04, a Parte 2 deste par.) Assim como a regressão linear desta aula estima os coeficientes $\beta$ que melhor combinam linearmente as variáveis explicativas para prever o rótulo, a krigagem estima os pesos $\lambda$ que melhor combinam linearmente os valores vizinhos para prever o valor num ponto não amostrado — a diferença central está em **o que faz o papel de variável explicativa**. Na regressão desta aula, as variáveis explicativas são atributos medidos na própria amostra (Cu, As, Zn, distância à falha); na krigagem, a "variável explicativa" é a **posição espacial relativa** de cada amostra vizinha, e os pesos vêm da estrutura de covariância espacial (o variograma), não de uma tabela de atributos. Há uma segunda diferença prática, não só formal: a regressão linear desta aula despreza inteiramente a posição espacial das amostras — duas amostras próximas e duas amostras distantes contam exatamente da mesma forma no ajuste, desde que tenham os mesmos valores de Cu, As, Zn — enquanto a krigagem é construída em torno exatamente dessa posição. É por isso que os dois métodos respondem a perguntas diferentes, mesmo quando ambos são, no fundo, "combinações lineares ponderadas ajustadas a dados": a regressão desta aula prevê o ouro **a partir de outras propriedades químicas** da mesma amostra; a krigagem prevê um valor **a partir de valores vizinhos no espaço**, sem precisar de nenhuma variável explicativa além da posição. A Aula 05 retoma essa distinção ao comparar interpolação geoestatística com agrupamento no espaço de atributos, não no espaço geográfico.

## Exemplo trabalhado

**Situação:** compare, lado a lado, a previsão da regressão linear e da floresta aleatória (regressão de `Au_ppb`) para as três primeiras amostras do conjunto de teste, e verifique manualmente o cálculo do MAE sobre essas três.

**Valores observados nas 3 primeiras amostras do teste (`y_test`):** 7,87; 19,26; 9,89 ppb.
**Previsões da regressão linear:** 5,28; 8,86; 24,15 ppb.
**Previsões da floresta aleatória:** 7,65; 5,75; 21,18 ppb.

**Cálculo manual do erro absoluto de cada amostra (regressão linear):**

$$|7{,}87 - 5{,}28| = 2{,}59 \qquad |19{,}26 - 8{,}86| = 10{,}40 \qquad |9{,}89 - 24{,}15| = 14{,}26$$

**MAE dessas três amostras:** $(2{,}59 + 10{,}40 + 14{,}26)/3 = 27{,}25/3 \approx 9{,}08$ ppb — bem acima do MAE de 5,128 ppb calculado sobre as 15 amostras completas do teste, porque a segunda e a terceira amostra desta pequena sub-amostra de três são justamente onde o modelo mais erra (a terceira, com valor real baixo de 9,89 ppb, recebeu uma previsão de 24,15 — mais que o dobro do valor real).

**A floresta, nas mesmas três amostras:** erros absolutos de $|7{,}87 - 7{,}65| = 0{,}22$, $|19{,}26 - 5{,}75| = 13{,}51$ e $|9{,}89 - 21{,}18| = 11{,}29$, com MAE de $(0{,}22 + 13{,}51 + 11{,}29)/3 = 25{,}02/3 \approx 8{,}34$ ppb. Repare no que acontece: **nestas três amostras a floresta sai melhor** que a regressão linear (8,34 contra 9,08), o **inverso** do que vale nas 15 amostras completas do teste (5,778 contra 5,128, a seção anterior). A ordem entre dois modelos se inverteu ao trocar a base de comparação de 15 amostras para 3. Isso ilustra um ponto que a Aula 06 desenvolve com rigor: **uma métrica calculada sobre poucas amostras é instável** — três amostras não são uma base confiável para julgar um modelo, e é exatamente por isso que o conjunto de teste completo (15 amostras neste módulo, idealmente muito mais num projeto real) existe: para que a métrica final não dependa de quais três amostras, por acaso, caíram na conta.

## Recap relâmpago

- **Regressão linear múltipla** estende a regressão linear simples (Módulo 20) para várias variáveis; os coeficientes vêm de mínimos quadrados e devem ser lidos com cautela quando há **multicolinearidade** entre as variáveis explicativas (aqui, Cu/As/Zn fortemente correlacionados).
- **Floresta aleatória** (regressão ou classificação) combina muitas árvores de decisão treinadas em subamostras aleatórias, sem assumir forma funcional linear; não é automaticamente melhor que um modelo linear — com poucos dados de treino, o modelo mais simples pode generalizar melhor, como neste exemplo de regressão (R² linear 0,79 contra R² floresta 0,73).
- `feature_importances_` (florestas) e os coeficientes (modelos lineares) servem para identificar quais variáveis pesam mais — mas **coeficientes de regressão não padronizada não são comparáveis entre variáveis de escalas diferentes**: antes de ordená-los, multiplique cada um pelo desvio-padrão da sua variável (ou ajuste o modelo sobre variáveis padronizadas). Nessa escala corrigida, a variável irrelevante `cota_m` fica uma ordem de grandeza abaixo dos três elementos geoquímicos na regressão linear, e recebe a segunda menor `feature_importances_` da floresta de regressão — o teste de sanidade útil. (A `feature_importances_` da floresta já é adimensional e não precisa dessa correção de escala — mas tem um viés próprio, a favor de variáveis contínuas e contra binárias, e é por isso que a cota irrelevante supera a litologia real na floresta de classificação da Aula 04.)
- A **krigagem** (Módulo 20) pertence, formalmente, à família dos **mínimos quadrados generalizados** (GLS) — combinação linear ponderada ajustada a dados com resíduos correlacionados —, mas usa a posição espacial relativa como base dos pesos em vez de atributos medidos na amostra, o que a torna uma ferramenta diferente na prática, não intercambiável com a regressão desta aula. Não confunda GLS com **modelo linear generalizado** (GLM), a família da regressão logística (Aula 04).

## Próxima aula

[[24-machine-learning-geociencias-aula-04-modelagem-supervisionada-classificacao|Aula 04 — Modelagem supervisionada: classificação]] — a **Parte 2** deste par: os mesmos dois algoritmos, agora sobre um rótulo categórico, e o resultado que inverte a ordem entre eles.

## Fontes

- Regressão linear múltipla por mínimos quadrados e interpretação de coeficientes: Hastie, T., Tibshirani, R. & Friedman, J., *The Elements of Statistical Learning*, 2ª ed. (2009), Springer, cap. 3; Géron, A., *Hands-On Machine Learning with Scikit-Learn, Keras and TensorFlow*, 3ª ed. (2022), O'Reilly, cap. 4.
- Árvores de decisão e florestas aleatórias (bagging, subamostragem aleatória de variáveis, importância de variável): Breiman, L. (2001), "Random Forests", *Machine Learning*, 45(1), 5-32, DOI 10.1023/A:1010933404324; Hastie, Tibshirani & Friedman, cap. 15.
- API do scikit-learn para os dois modelos usados (`LinearRegression`, `RandomForestRegressor`), para `feature_importances_` e para o viés da importância por impureza a favor de variáveis de alta cardinalidade: documentação oficial scikit-learn (scikit-learn.org), versão 1.9.
- Krigagem como melhor estimador linear não-viesado e sua relação formal com mínimos quadrados generalizados: Cressie, N., *Statistics for Spatial Data*, ed. revisada (1993), Wiley, cap. 3; retomando [[20-geoestatistica/20-geoestatistica-aula-05-krigagem-simples-ordinaria|Módulo 20, Aula 05]] deste curso.

<!--
nivel: avancado
palavras_corpo: 2417
mapa_objetivo_secao:
  geologia-avancado-m24-oa03: "Regressão: prever um número contínuo" + "Regressão com floresta aleatória: um modelo não linear" + "Krigagem como parente da regressão" + "Exemplo trabalhado"

origem: "Aula DIVIDIDA em 2026-09-21 pela revisao didatica (achado DID-M24-A03-CARGA-001): a antiga Aula 03 cobria regressao E classificacao em 2.923 palavras (~34,8 min, acima do teto de 30). O corte foi por TAREFA: esta aula ficou com a regressao (linear, floresta aleatoria, krigagem como parente e o exemplo trabalhado ORIGINAL do MAE manual, preservado palavra por palavra), e a nova Aula 04 ficou com a classificacao. As duas alegacoes de classificacao (MLGEO-M24-A03-CLASSIFICACAO-RESULTADO-003 e MLGEO-M24-A03-REGRESSAO-LOGISTICA-CONCEITO-005) MIGRARAM para a Aula 04 com o claim_id PRESERVADO, sem renumeracao: o prefixo A03 designa a numeracao em que a alegacao foi emitida, nao a aula onde ela hoje mora. Nenhum fato novo foi introduzido nesta aula pela divisao."

alegacoes_auditaveis:
  - claim_id: MLGEO-M24-A03-REGRESSAO-LINEAR-RESULTADO-001
    claim: "Ajustando LinearRegression sobre o conjunto de dados da aula (feat_cols = dist_falha_m, cota_m, Cu_ppm, As_ppm, Zn_ppm, litologia_xisto; alvo Au_ppb; mesma particao treino/teste da Aula 02, random_state=42, test_size=0.25), os coeficientes aproximados sao dist_falha_m=0.0039, cota_m=-0.0033, Cu_ppm=0.0202, As_ppm=0.6881, Zn_ppm=0.0561, litologia_xisto=2.0303, intercepto=-1.3053, com MAE=5.128, RMSE=6.759 e R2=0.7879 no conjunto de teste."
    risk: calculo
    source: "Execucao direta do codigo apresentado na aula (scikit-learn 1.9.1, pandas 3.0.3, NumPy 2.5.1). CONFIRMADO POR EXECUCAO em 2026-09-20: valores reproduzidos digito a digito (coeficientes arredondados a 4 casas, metricas a 3-4 casas)."
  - claim_id: MLGEO-M24-A03-RANDOMFOREST-REGRESSAO-RESULTADO-002
    claim: "Ajustando RandomForestRegressor(n_estimators=300, random_state=42) sobre o mesmo conjunto de treino/teste da regressao linear desta aula, o modelo obtem MAE=5.778, RMSE=7.582 e R2=0.7331 no teste - pior que a regressao linear (R2=0.7879) nas tres metricas - com importancias de variavel dist_falha_m=0.240, cota_m=0.025, Cu_ppm=0.224, As_ppm=0.234, Zn_ppm=0.272, litologia_xisto=0.006."
    risk: calculo
    source: "Execucao direta do codigo apresentado na aula (scikit-learn 1.9.1). CONFIRMADO POR EXECUCAO em 2026-09-20: valores reproduzidos digito a digito."
  - claim_id: MLGEO-M24-A03-RANDOMFOREST-CONCEITO-004
    claim: "Uma floresta aleatoria (random forest) treina multiplas arvores de decisao, cada uma sobre uma amostra bootstrap (com reposicao) dos dados de treino e considerando, a cada divisao de no, apenas um subconjunto aleatorio das variaveis disponiveis, combinando as previsoes individuais por media (regressao) ou voto majoritario (classificacao); esse mecanismo de aleatorizacao dupla (amostragem de linhas e de variaveis) reduz a variancia do estimador combinado em relacao a uma unica arvore de decisao profundamente ajustada."
    risk: fato
    source: "Breiman, L. (2001), 'Random Forests', Machine Learning, 45(1), 5-32, DOI 10.1023/A:1010933404324."
  - claim_id: MLGEO-M24-A03-KRIGAGEM-REGRESSAO-006
    claim: "A krigagem ordinaria, apresentada no Modulo 20 como o melhor estimador linear nao-viesado (combinacao linear ponderada de amostras vizinhas com pesos resolvidos a partir do modelo de variograma), pertence formalmente a familia dos MINIMOS QUADRADOS GENERALIZADOS (generalized least squares, GLS): a generalizacao da regressao linear ordinaria para residuos correlacionados em vez de independentes, sendo a estrutura de correlacao dada, na krigagem, pelo variograma. Ambas estimam uma combinacao linear de valores de entrada ajustada a partir de uma estrutura de covariancia/correlacao nos dados, mas a krigagem usa a posicao espacial relativa das amostras vizinhas como base dos pesos, enquanto a regressao linear classica usa atributos medidos na propria amostra como variaveis explicativas, sem considerar posicao espacial. ATENCAO TERMINOLOGICA: minimos quadrados generalizados (GLS) NAO e o mesmo que modelo linear generalizado (GLM), a familia a que pertence a regressao logistica tambem ensinada nesta aula - a expressao ambigua 'regressao linear generalizada' foi removida do texto por esse motivo."
    risk: fato
    source: "Cressie, N., Statistics for Spatial Data, ed. revisada (1993), Wiley, cap. 3 (krigagem como problema de minimos quadrados generalizados; krigagem ordinaria com media constante desconhecida estimada por GLS); retomando Modulo 20, Aula 05 deste curso (krigagem como BLUE). ACHADO 8 DA AUDITORIA de 2026-09-20 (ambiguidade terminologica GLS x GLM corrigida)."
  - claim_id: MLGEO-M24-A03-EXEMPLO-MAE-MANUAL-007
    claim: "Para as tres primeiras amostras do conjunto de teste de regressao (y_test = 7.87, 19.26, 9.89 ppb; previsoes da regressao linear = 5.28, 8.86, 24.15 ppb), os erros absolutos sao 2.59, 10.40 e 14.26, e o MAE dessas tres amostras e (2.59+10.40+14.26)/3 = 27.25/3 = 9.08 ppb, valor mais alto que o MAE de 5.128 ppb calculado sobre as 15 amostras completas do conjunto de teste."
    risk: calculo
    source: "Calculo aritmetico direto a partir dos valores de y_test e das previsoes da regressao linear desta aula, ja confirmados por execucao (claim MLGEO-M24-A03-REGRESSAO-LINEAR-RESULTADO-001). Conferido manualmente: 7.87-5.28=2.59; 19.26-8.86=10.40; |9.89-24.15|=14.26; soma=27.25; 27.25/3=9.0833."
  - claim_id: MLGEO-M24-A03-COEFICIENTES-ESCALA-008
    claim: "Coeficientes de uma regressao linear ajustada sobre variaveis NAO padronizadas nao sao comparaveis entre si como medida de importancia, porque cada coeficiente carrega a unidade da sua variavel. No modelo desta aula, o coeficiente de As_ppm (0.6881) e 34 vezes maior que o de Cu_ppm (0.0202) porque o desvio-padrao de As_ppm no treino (7.74 ppm) e 43 vezes menor que o de Cu_ppm (330.55 ppm), e nao porque o arsenio seja mais informativo. Multiplicando cada coeficiente pelo desvio-padrao da sua variavel no treino (equivalente a reajustar o modelo sobre variaveis padronizadas), os efeitos padronizados sao Zn_ppm=7.053, Cu_ppm=6.664, As_ppm=5.326, litologia_xisto=1.009, cota_m=-0.585 e dist_falha_m=0.581 - ordem diferente da dos coeficientes brutos. Nessa escala, cota_m continua uma ordem de grandeza abaixo dos tres elementos geoquimicos (o teste de sanidade da variavel irrelevante se sustenta), mas dist_falha_m cai no MESMO patamar baixo (0.581 contra 0.585 da cota) apesar de correlacionar r=-0.90 com o cobre: um coeficiente parcial pequeno indica pouca contribuicao ADICIONAL as demais variaveis ja no modelo, nao ausencia de relacao com o alvo."
    risk: calculo
    source: "Hastie, T., Tibshirani, R. & Friedman, J., The Elements of Statistical Learning, 2a ed. (2009), Springer, cap. 3 (interpretacao de coeficientes de minimos quadrados e o papel da escala das variaveis); Geron, A., Hands-On Machine Learning, 3a ed. (2022), O'Reilly, cap. 4. CONFIRMADO POR EXECUCAO em 2026-09-20 (scikit-learn 1.9.1): desvios-padrao do treino e coeficientes padronizados reproduzidos digito a digito, e verificados de forma independente reajustando LinearRegression sobre StandardScaler().fit_transform(X_train), que devolve exatamente os mesmos valores. ACHADO 1 DA AUDITORIA de 2026-09-20 (a aula atribuia a desproporcao do coeficiente de As a multicolinearidade, quando a causa direta e a escala)."
  - claim_id: MLGEO-M24-A03-MDI-VIES-CARDINALIDADE-009
    claim: "A importancia de variavel por reducao de impureza (feature_importances_ de modelos baseados em arvore) e documentadamente enviesada A FAVOR de variaveis de alta cardinalidade (numericas continuas, com muitos valores distintos) e CONTRA variaveis binarias ou categoricas de poucas categorias. No proprio modulo esse vies fica visivel: na floresta de CLASSIFICACAO, cota_m (variavel de puro ruido, continua) recebe importancia 0.086, MAIOR que litologia_xisto (0.025), que e binaria e carrega informacao geologica real. Logo, a importancia quase nula de litologia_xisto na floresta de regressao (0.006) nao se explica somente pela redundancia com os teores geoquimicos correlacionados - parte dela e o vies de cardinalidade. A importancia por permutacao (Aula 07) nao apresenta esse vies e se aplica a qualquer modelo."
    risk: fato
    source: "Documentacao oficial scikit-learn, '5.2. Permutation feature importance' (scikit-learn.org/stable/modules/permutation_importance.html), versao 1.9.1, consultada em 2026-09-21: as importancias por impureza sao 'strongly biased' e 'favor high cardinality features (typically numerical features) over low cardinality features such as binary features or categorical variables with a small number of possible categories'; 'permutation-based feature importances do not exhibit such a bias'. Valores numericos 0.086 e 0.025 confirmados por execucao (ver claim MLGEO-M24-A03-CLASSIFICACAO-RESULTADO-003). ACHADO 11 DA AUDITORIA de 2026-09-21 (a aula usava feature_importances_ como teste de sanidade sem a ressalva, e explicava a importancia nula da litologia apenas por redundancia geoquimica)."
  - claim_id: MLGEO-M24-A03-EXEMPLO-RF-PREVISOES-010
    claim: "Para as tres primeiras amostras do conjunto de teste de regressao (y_test = 7.87, 19.26, 9.89 ppb), a floresta aleatoria de regressao desta aula preve 7.65, 5.75 e 21.18 ppb, com erros absolutos de 0.22, 13.51 e 11.29 e MAE dessas tres de (0.22+13.51+11.29)/3 = 25.02/3 = 8.34 ppb - MENOR que o MAE de 9.08 ppb da regressao linear nas mesmas tres amostras, e portanto o INVERSO da ordem valida sobre as 15 amostras completas do teste (floresta 5.778 contra linear 5.128). A ordem entre os dois modelos se inverte ao trocar a base de comparacao de 15 para 3 amostras, o que reforca a instabilidade de metrica em amostra pequena que o exemplo se propoe a ilustrar."
    risk: calculo
    source: "Execucao direta do RandomForestRegressor(n_estimators=300, random_state=42) da aula sobre a mesma particao (scikit-learn 1.9.1). CONFIRMADO POR EXECUCAO em 2026-09-21: rf.predict(X_test)[:3] = [7.65, 5.75, 21.18]; aritmetica dos erros conferida a mao. ACHADO 15 DA AUDITORIA de 2026-09-21 (o exemplo anunciava a comparacao lado a lado com a floresta e nao a entregava, dizendo apenas 'conferidas separadamente pelo codigo da aula')."
  - claim_id: MLGEO-M24-A03-DDOF-DESVIO-011
    claim: "Os desvios-padrao de treino citados nesta aula (7.7 ppm para As_ppm e 330.5 ppm para Cu_ppm) sao POPULACIONAIS (divisor n, ddof=0), a convencao do StandardScaler do scikit-learn. O metodo .std() do pandas usa por padrao o divisor n-1 (ddof=1) e devolve 7.83 e 334.28 para as mesmas colunas. A equivalencia afirmada na aula - multiplicar cada coeficiente pelo desvio-padrao da sua variavel EQUIVALE a reajustar o modelo sobre variaveis padronizadas - so e exata na convencao populacional; com ddof=1 os efeitos padronizados saem 1.1% maiores (Zn 7.133, Cu 6.739, As 5.386, litologia 1.020, cota -0.592, dist 0.587) e nao coincidem mais com o ajuste sobre StandardScaler."
    risk: calculo
    source: "Documentacao oficial scikit-learn, classe StandardScaler (variancia populacional) e pandas.DataFrame.std (parametro ddof, default 1), versoes 1.9.1 e 3.0.3. CONFIRMADO POR EXECUCAO em 2026-09-21: ddof=0 devolve As 7.74 / Cu 330.55 e efeitos identicos aos do ajuste padronizado; ddof=1 devolve As 7.83 / Cu 334.28. ACHADO 17 DA AUDITORIA de 2026-09-21 (a aula nao dizia qual convencao usava, e o leitor que reproduzisse com pandas .std() obteria numeros diferentes dos declarados)."
-->
