# Questionário parcial 2 — Módulo 24: Fundamentos e aplicações de machine learning em geociências

**Módulo:** [[24-machine-learning-geociencias-modulo|Módulo 24 — Fundamentos e aplicações de machine learning em geociências]]
**Cobertura:** Aulas 03 a 05 — regressão (linear múltipla, floresta aleatória, krigagem como parente); classificação (regressão logística, floresta, matriz de confusão); modelagem não supervisionada (padronização, K-means, método do cotovelo, PCA).
**Recorte:** os algoritmos. A parcial 2 testa se você sabe ler o que cada modelo devolve (coeficientes, importâncias, matrizes, inércias, variância explicada) e por que nenhum algoritmo é melhor em abstrato.
**Objetivos avaliados:** `geologia-avancado-m24-oa03` (integral — a03, a04 e a05)
**Pontuação total:** 100 pontos · o gabarito fica oculto; responda antes de abrir.

---

### 9. Múltipla escolha — `geologia-avancado-m24-q09` · oa03 · 8 pts

Na regressão linear múltipla do teor de ouro, o coeficiente de `As_ppm` (0,6881) é cerca de 34 vezes maior que o de `Cu_ppm` (0,0202). Qual é a causa direta dessa diferença?

- a) O arsênio informa 34 vezes mais sobre o ouro do que o cobre
- b) A multicolinearidade entre Cu, As e Zn, que é a causa direta da desproporção entre os dois coeficientes
- c) Um coeficiente de regressão não padronizada carrega a unidade da sua variável, e o arsênio varia numa faixa muito mais estreita (desvio-padrão de 7,7 ppm contra 330,5 ppm do cobre)
- d) A floresta aleatória superestima o arsênio e contamina o modelo linear

<details>
<summary>Ver resposta</summary>

**Resposta: c**

O coeficiente responde "quanto muda o ouro por **uma unidade** daquela variável", e uma unidade significa coisas muito diferentes em escalas diferentes: o desvio-padrão do cobre é cerca de 43 vezes o do arsênio, e a razão dos coeficientes (~34) segue essa desproporção de escala. Multiplicando cada coeficiente pelo desvio-padrão da respectiva variável, a ordem se inverte e as três ficam próximas (Zn 7,05; Cu 6,66; As 5,33). "a" é justamente a leitura ingênua a evitar. "b" é um distrator plausível — a multicolinearidade existe e dificulta ler cada coeficiente isoladamente, mas **não** é a causa direta desta desproporção, que é escala. "d" mistura dois modelos independentes.
</details>

---

### 10. Verdadeiro ou Falso (justifique) — `geologia-avancado-m24-q10` · oa03 · 8 pts

"No modelo linear padronizado, `dist_falha_m` tem efeito baixo (0,58), no mesmo patamar da variável irrelevante `cota_m` (−0,59). Logo, a distância à falha não tem relação com o teor de ouro."

<details>
<summary>Ver resposta</summary>

**Falso.**

Um coeficiente parcial pequeno significa "acrescenta pouco às demais variáveis já no modelo", não "não tem relação com o alvo". A EDA mostrou correlação de r = −0,90 entre a distância à falha e o cobre; o cobre, já dentro do modelo, absorveu quase toda a informação que a distância carregava. A `cota_m`, ao contrário, tem correlação quase nula com tudo — é ruído por construção. Dois números parecidos, dois motivos completamente diferentes.
</details>

---

### 11. Múltipla escolha — `geologia-avancado-m24-q11` · oa03 · 8 pts

Na floresta aleatória de **classificação**, a importância por **redução de impureza** (`feature_importances_`) dá 0,086 para `cota_m`, que é puro ruído por construção, e 0,025 para `litologia_xisto`, que carrega informação geológica real. Como interpretar?

- a) A elevação informa mais sobre anomalia geoquímica do que a rocha encaixante
- b) É o viés de cardinalidade da importância por impureza, que favorece variáveis contínuas (muitos valores distintos) sobre binárias ou de poucas categorias; o resultado não prova que a cota importe mais que a litologia
- c) A litologia não tem nenhuma relação com o alvo, e a floresta acertou ao ignorá-la
- d) A floresta foi mal treinada; com mais árvores a cota teria importância zero

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A importância por impureza é documentadamente enviesada a favor de variáveis de alta cardinalidade (numéricas contínuas) e contra binárias ou categóricas de poucas categorias. Como `cota_m` é contínua e `litologia_xisto` é binária, a inversão é o viés em ação — não uma descoberta geológica. "a" e "c" tomam o número pelo valor de face. "d" é um distrator sem base: o viés não some com mais árvores. Repare que a pergunta nomeia o método (impureza): a mesma pergunta por outro método (permutação, coeficiente padronizado) pode ter resposta diferente.
</details>

---

### 12. Múltipla escolha — `geologia-avancado-m24-q12` · oa03 · 6 pts

A krigagem ordinária do Módulo 20 pertence formalmente a qual família em relação à regressão linear desta aula?

- a) Modelos lineares generalizados (GLM), a mesma família da regressão logística
- b) Mínimos quadrados generalizados (GLS): a generalização da regressão para resíduos correlacionados segundo uma estrutura de covariância conhecida, que na krigagem é o variograma
- c) Florestas aleatórias, porque combina muitos vizinhos por média
- d) Aprendizado não supervisionado, porque não usa rótulo

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A krigagem é o melhor estimador linear não-viesado (BLUE) e, formalmente, um caso de **GLS**. "a" é o falso amigo a evitar: GLS (mínimos quadrados **generalizados**) não é o mesmo que GLM (modelo linear **generalizado**), esta segunda sendo a família a que pertence a regressão logística. "c" e "d" não descrevem a krigagem: ela é uma combinação linear ponderada com pesos vindos do variograma e usa os valores observados nos vizinhos como dado, não é agrupamento.
</details>

---

### 13. Aplicação / cálculo — `geologia-avancado-m24-q13` · oa03 · 8 pts

Numa regressão logística, a combinação linear das variáveis dá z = +2 para uma amostra A e z = −2 para uma amostra B. (a) Calcule a probabilidade prevista P(y=1) de cada uma pela função sigmoide (use e² ≈ 7,39). (b) Qual a classe prevista com o limiar padrão? (c) Por que não se usa uma regressão linear comum para classificar?

<details>
<summary>Ver resposta</summary>

(a) $P = 1/(1+e^{-z})$.

- Amostra A: $1/(1+e^{-2}) = 1/(1+0{,}135) \approx$ **0,88**.
- Amostra B: $1/(1+e^{2}) = 1/(1+7{,}39) \approx$ **0,12**.

(b) O scikit-learn classifica como 1 quando a probabilidade excede **0,5**: A é classe 1 (anômala); B é classe 0 (background).

(c) A regressão linear prevê qualquer número real, sem limite — responderia coisas como "esta amostra é 1,7 anômala". A sigmoide comprime a mesma combinação linear para o intervalo (0, 1), transformando-a numa probabilidade. A combinação linear é a mesma da regressão linear; o que se acrescenta é a sigmoide por cima.
</details>

---

### 14. Aplicação — `geologia-avancado-m24-q14` · oa03 · 10 pts

As matrizes de confusão de teste (formato `[[TN, FP], [FN, TP]]`, 15 amostras) são: regressão logística `[[4, 1], [1, 9]]` e floresta `[[5, 0], [1, 9]]`. Um colega conclui: "a floresta (acurácia 0,933) é melhor que a logística (0,867), inclusive em não deixar passar amostras anômalas". Avalie a conclusão.

<details>
<summary>Ver resposta</summary>

A conclusão é **parcialmente errada**. As acurácias estão corretas (14/15 = 0,933 contra 13/15 = 0,867), mas a diferença é **um único erro**, e ele está no lugar errado para sustentar a frase do colega: os dois modelos têm o **mesmo número de falsos negativos (1)** — deixam passar exatamente a mesma quantidade de amostras anômalas. Toda a vantagem da floresta está no falso positivo que a logística comete (1) e a floresta não (0).

Os dois erros não custam o mesmo numa campanha: o falso negativo é um alvo perdido; o falso positivo é um furo gasto em estéril. Qual pesa mais é decisão do geólogo (orçamento, estágio), não do algoritmo. A afirmação defensável é: a floresta é melhor em acurácia e as duas são iguais no erro de deixar passar anômala. É a limitação de uma acurácia única, que a Aula 06 ataca com métricas que olham cada tipo de erro separadamente.
</details>

---

### 15. Dissertativa — `geologia-avancado-m24-q15` · oa03 · 14 pts

Sobre exatamente os mesmos dados, na regressão de `Au_ppb` o modelo linear (R² = 0,7879; MAE = 5,128) superou a floresta (R² = 0,7331; MAE = 5,778), e na classificação de `anomalo` a floresta (acurácia 0,933) superou a regressão logística (0,867). Explique por que a ordem entre os dois algoritmos se inverte quando a tarefa muda, e qual a lição para a escolha de modelos.

<details>
<summary>Ver resposta</summary>

Uma boa resposta cobre:

- **Regressão:** a relação entre teor de elemento pathfinder e ouro é, neste exemplo, aproximadamente linear por construção; com apenas 45 amostras de treino, o modelo simples (seis coeficientes e um intercepto) tem menos com que errar, enquanto a floresta, de muito mais capacidade, tende a captar ruído do treino em vez de sinal generalizável — primeiro sinal do sobreajuste que a Aula 06 formaliza.
- **Classificação:** o rótulo `anomalo` foi definido por um **limiar rígido de cobre** (180 ppm) mais 12% de ruído de rótulo. Um corte abrupto numa variável não é uma reta suave no espaço das variáveis; um método que particiona o espaço em regiões (árvores) tem vantagem estrutural sobre um que só traça um único plano (logística).
- **Lição:** não existe "o melhor algoritmo" em abstrato; existe o que se ajusta à forma do problema e ao volume de dados. Comparar candidatos no conjunto de teste é a única forma confiável de saber. E o resultado não é universal: florestas costumam superar o modelo linear quando a relação é genuinamente não linear ou há interações complexas.
</details>

---

### 16. Múltipla escolha — `geologia-avancado-m24-q16` · oa03 · 6 pts

Por que padronizar as variáveis (`StandardScaler`) antes de rodar K-means nos teores de Cu, As e Zn?

- a) Para que o algoritmo receba o rótulo `anomalo` de forma numérica
- b) Porque a distância euclidiana seria dominada pela variável de maior escala numérica (Cu, de 5 a mais de 1.200 ppm), e o arsênio (de 0,5 a cerca de 28 ppm) praticamente não pesaria, sem que isso reflita importância geológica
- c) Porque K-means só aceita variáveis com média zero e desvio-padrão 1 por restrição da linguagem Python
- d) Para aumentar a inércia e tornar o método do cotovelo mais nítido

<details>
<summary>Ver resposta</summary>

**Resposta: b**

K-means mede semelhança por distância no espaço das variáveis; sem padronização, a diferença em cobre dominaria a distância e o arsênio quase não contaria — só por causa da escala numérica. Padronizar (subtrair a média e dividir pelo desvio-padrão) deixa todas com média 0 e desvio-padrão 1. "a" está errada porque K-means **não usa rótulo**. "c" inventa uma restrição técnica. "d" está errada: a padronização não serve para alterar a inércia, e sim para tornar as variáveis comparáveis.
</details>

---

### 17. Aplicação / cálculo — `geologia-avancado-m24-q17` · oa03 · 12 pts

Para K-means com $k = 1$ a $6$ sobre as três variáveis padronizadas (n = 60), as inércias são: 180,0; 55,75; 31,9; 22,38; 18,28; 16,35. (a) Calcule a queda percentual de $k=1$ para $k=2$ e de $k=2$ para $k=3$. (b) Que $k$ o método do cotovelo indica e por que não escolher $k=6$, o de menor inércia? (c) Por que a inércia com $k=1$ vale exatamente 180?

<details>
<summary>Ver resposta</summary>

(a) $(180{,}0 - 55{,}75)/180{,}0 \approx$ **69%** de $k=1$ para $k=2$; $(55{,}75 - 31{,}9)/55{,}75 \approx$ **43%** de $k=2$ para $k=3$ (e cerca de 30% de $k=3$ para $k=4$).

(b) O cotovelo é o ponto em que a queda desacelera visivelmente: a maior queda é de 1 para 2 e as seguintes diminuem progressivamente — indica **$k=2$**, coerente com a estrutura background versus anômalo. Escolher o $k$ de menor inércia seria sempre escolher o maior $k$ testado: a inércia **sempre** cai quando $k$ aumenta, e no limite ($k$ = número de amostras) chega a zero, com cada amostra como seu próprio grupo, o que não é útil.

(c) Com $k=1$ a inércia é a soma das distâncias ao quadrado de todas as amostras ao centróide único. Para variáveis padronizadas, cada coluna contribui com variância 1 por amostra, então a inércia é $n \times p = 60 \times 3 = 180$. Ou seja, é **$n$ vezes** a variância total multivariada (que aqui vale 3), e não igual a ela.
</details>

---

### 18. Dissertativa — `geologia-avancado-m24-q18` · oa03 · 12 pts

O K-means com $k=2$ separou um grupo de 15 amostras e outro de 45. Cruzando com o rótulo, o grupo 1 (15 amostras) tem 1 background e 14 anômalas; o grupo 0 (45 amostras) tem 20 background e 25 anômalas. (a) O K-means "errou" nas 25 anômalas do grupo 0? (b) Por que o rótulo tem 39 amostras anômalas, e não 36? (c) O que fazer com as amostras em que os dois métodos divergem?

<details>
<summary>Ver resposta</summary>

(a) **Não é erro do K-means.** Um algoritmo não supervisionado responde "que estrutura existe nos dados", não "os dados confirmam a categoria que eu já tinha em mente". O rótulo `anomalo` foi definido por um limiar único e arbitrário de cobre (> 180 ppm) com ruído de rótulo, enquanto o K-means organiza os dados pela estrutura geométrica conjunta de Cu, As e Zn, cuja transição é mais gradual do que um corte abrupto numa variável. As duas respostas se parecem, mas raramente são idênticas; tratar os grupos como a classificação de interesse é erro de interpretação comum.

(b) O limiar puro Cu > 180 ppm seleciona **36** amostras. O ruído de rótulo de 12% trocou 5 rótulos (4 de background para anômala e 1 no sentido inverso), fechando em 36 + 4 − 1 = **39**. Limiar (36) e rótulo (39) não são a mesma contagem.

(c) Onde os dois concordam (as 14 amostras do grupo 1 que também são `anomalo=1`), a evidência é mais forte. Onde divergem (as 25 anômalas fora do grupo 1), vale investigar se são zonas de transição, ruído de rótulo ou uma mineralização de caráter geoquímico distinto que um único limiar de cobre não capturaria.
</details>

---

### 19. Múltipla escolha — `geologia-avancado-m24-q19` · oa03 · 8 pts

Um PCA sobre Cu, As e Zn padronizados dá variância explicada de 92,03% (PC1), 6,63% (PC2) e 1,33% (PC3), com loadings do PC1 de 0,591 (Cu), 0,561 (As) e 0,580 (Zn). Qual leitura está correta?

- a) O PC1 é o cobre, e os outros dois elementos foram descartados pelo algoritmo
- b) O PC1 combina os três elementos com pesos semelhantes e funciona como um índice geral de enriquecimento; dois componentes já somam 98,67% da variância porque Cu, As e Zn são fortemente correlacionados (redundantes)
- c) O PCA precisa do rótulo `anomalo` para ordenar os componentes, e o PC1 é o que melhor separa as classes
- d) Os três componentes somam 100% por coincidência; com mais variáveis, a soma seria menor

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Loadings positivos e de magnitude parecida indicam que o PC1 é uma média ponderada de enriquecimento — um "índice de anomalia" compartilhado pelos três elementos. Como as variáveis têm correlações de 0,82 a 0,95 entre si, carregam informação redundante, e o PCA a remove: duas dimensões preservam 98,67% da variância, o que permite visualizar as 60 amostras num gráfico de dispersão bidimensional. "a" ignora os loadings. "c" erra: PCA é **não supervisionado**, ordena por variância, não por rótulo. "d" erra: com $p$ variáveis existem no máximo $p$ componentes, e juntos sempre recuperam 100% da variância — aqui 3 variáveis, 3 componentes.
</details>

---

**Total: 100 pontos.**
