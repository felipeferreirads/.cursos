# Questionário parcial 1 — Módulo 23: Introdução à modelagem numérica geodinâmica

**Módulo:** [[23-modelagem-numerica-geodinamica-modulo|Módulo 23 — Introdução à modelagem numérica geodinâmica]]
**Cobertura:** Aulas 01 a 02 — Python/NumPy/Matplotlib para geodinâmica computacional; equações diferenciais ordinárias e parciais; solução analítica versus numérica; método das diferenças finitas (diferença central de segunda ordem para a segunda derivada).
**Recorte:** a ferramenta (Python vetorizado, aula 01) e a linguagem matemática que ela vai resolver (EDO/EDP, diferenças finitas, aula 02) — antes de qualquer física de geodinâmica propriamente dita, que começa na parcial 2.
**Objetivos avaliados:** `geologia-avancado-m23-oa01` (integral — a01), `geologia-avancado-m23-oa02` (parcial — início em a02, completado nas parciais seguintes)
**Pontuação total:** 100 pontos · o gabarito fica oculto; responda antes de abrir.

---

### 1. Múltipla escolha — `geologia-avancado-m23-q01` · oa01 · 12 pts

Um aluno tem dois arrays NumPy de 10.000 elementos cada, `a` e `b`, e quer somá-los elemento a elemento. Qual a forma correta e por que ela é preferível a um laço `for` percorrendo os índices um a um?

- a) `for i in range(len(a)): c[i] = a[i] + b[i]` — é a única forma que o NumPy aceita para arrays grandes
- b) `c = a + b` — o NumPy aplica a soma de forma vetorizada, delegando a execução a rotinas compiladas, o que é muito mais rápido que um laço interpretado em Python puro para arrays grandes
- c) `c = list(a) + list(b)` — converter para lista e concatenar produz a soma elemento a elemento
- d) É indiferente: NumPy internamente sempre executa um laço `for`, então não há ganho de desempenho em nenhuma das formas

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A vetorização é exatamente isso: aplicar a operação aritmética a todos os elementos de uma vez, sem laço `for` explícito no código Python, com a execução delegada a rotinas compiladas (em C) por baixo dos panos — mais legível e muito mais rápida que um laço interpretado, uma diferença que se torna decisiva em malhas de milhares a milhões de pontos. "a" descreve exatamente o que a vetorização evita. "c" está errada porque `+` entre listas Python as **concatena** (produz uma lista de 20.000 elementos), não soma seus valores — é justamente o defeito que o array do NumPy corrige. "d" é falsa: o ganho de desempenho da vetorização é real e mensurável, não uma ilusão de sintaxe.
</details>

---

### 2. Aplicação / leitura de código — `geologia-avancado-m23-q02` · oa01 · 12 pts

Considere o código:

```python
import numpy as np

x = np.linspace(0, 4, 5)   # 0, 1, 2, 3, 4
z = np.linspace(0, 2, 3)   # 0, 1, 2
X, Z = np.meshgrid(x, z)
F = X + Z
```

Qual é o `shape` de `X` (e de `F`)? E qual o valor de `F` na posição de índice `[1, 2]` (linha 1, coluna 2, contando a partir de zero)?

<details>
<summary>Ver resposta</summary>

**`shape` = `(3, 5)`** — 3 linhas (uma por valor de `z`, que tem 3 pontos) e 5 colunas (uma por valor de `x`, que tem 5 pontos), porque `meshgrid` replica cada array 1D ao longo da outra dimensão, com a convenção (número de pontos do segundo array, número de pontos do primeiro).

Na posição `[1, 2]`: linha 1 corresponde a `z = 1` (o segundo valor de `z = [0, 1, 2]`); coluna 2 corresponde a `x = 2` (o terceiro valor de `x = [0, 1, 2, 3, 4]`). Logo `F[1, 2] = x + z = 2 + 1 = 3`.
</details>

---

### 3. Verdadeiro ou Falso (justifique) — `geologia-avancado-m23-q03` · oa01 · 12 pts

"Ao plotar uma geoterma com `plt.plot(T, z)`, não é necessário chamar `plt.gca().invert_yaxis()`, porque o Matplotlib reconhece automaticamente que `z` representa profundidade e inverte o eixo sozinho."

<details>
<summary>Ver resposta</summary>

**Falso.**

O Matplotlib não tem noção nenhuma do significado físico dos dados que recebe — ele não "sabe" que o array passado como eixo y representa profundidade. Por padrão, o eixo vertical cresce de baixo para cima, como em qualquer gráfico cartesiano comum. Se o gráfico é de uma geoterma, em que se espera que a profundidade cresça **para baixo**, é preciso inverter o eixo explicitamente com `invert_yaxis()`. Esquecer essa linha produz uma figura que parece plausível à primeira vista, mas está de cabeça para baixo — exatamente o alerta que a Aula 01 destaca como o primeiro exemplo concreto de que "o gráfico é o instrumento de conferência, e um gráfico mal rotulado não confere nada".
</details>

---

### 4. Múltipla escolha — `geologia-avancado-m23-q04` · oa02 · 12 pts

O decaimento radioativo, dN/dt = −λN, e a equação do calor, ∂T/∂t = κ ∂²T/∂z², diferem fundamentalmente porque:

- a) o decaimento é uma EDP e a equação do calor é uma EDO
- b) o decaimento envolve derivada em relação a uma única variável independente (o tempo) — é uma EDO; a equação do calor envolve derivadas parciais em relação a duas variáveis independentes simultâneas (tempo e espaço) — é uma EDP
- c) as duas são EDPs, porque ambas descrevem taxas de variação de uma grandeza física
- d) a diferença é apenas de notação (d versus ∂), sem nenhuma implicação sobre o tipo de equação

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Uma equação diferencial **ordinária** (EDO) envolve derivadas em relação a uma única variável independente — no decaimento radioativo, só o tempo. Uma equação diferencial **parcial** (EDP) envolve derivadas parciais em relação a duas ou mais variáveis independentes ao mesmo tempo — na equação do calor, tempo **e** espaço (daí o uso do símbolo ∂, "derivada parcial", em vez de d). "a" inverte a classificação. "c" ignora a definição: o decaimento não tem nenhuma derivada espacial. "d" está errada porque a notação não é arbitrária — ela reflete exatamente essa diferença estrutural entre as duas equações.
</details>

---

### 5. Aplicação / cálculo — `geologia-avancado-m23-q05` · oa02 · 14 pts

Tome a função-teste T(z) = 3z² + 2z, cuja segunda derivada exata é constante: d²T/dz² = 6. Discretize z de 0 a 8 em 5 nós igualmente espaçados (Δz = 2: z = 0, 2, 4, 6, 8) e calcule, pela fórmula de diferença central de segunda ordem, a segunda derivada aproximada no nó i = 2 (z = 4). Compare com o valor exato.

<details>
<summary>Ver resposta</summary>

Valores de T nos 5 nós: T(0) = 0; T(2) = 3(4) + 4 = 16; T(4) = 3(16) + 8 = 56; T(6) = 3(36) + 12 = 120; T(8) = 3(64) + 16 = 208.

No nó i = 2 (z = 4), os vizinhos são T[1] = 16 (z=2) e T[3] = 120 (z=6):

d²T/dz² ≈ (T[3] − 2·T[2] + T[1]) / Δz² = (120 − 2×56 + 16) / 2² = (120 − 112 + 16) / 4 = 24 / 4 = **6**

O resultado bate exatamente com o valor exato (6), sem nenhum erro — coerente com a propriedade vista na Aula 02: a fórmula de diferença central de segunda ordem é **exata** para qualquer polinômio até grau três, e T(z) = 3z² + 2z é de grau dois.
</details>

---

### 6. Dissertativa curta — `geologia-avancado-m23-q06` · oa02 · 12 pts

Em que condições um problema geodinâmico admite solução analítica (fórmula fechada), e por que a maioria dos problemas reais não admite? Dê um exemplo de cada caso.

<details>
<summary>Ver resposta</summary>

Uma boa resposta cobre: solução analítica existe apenas para um conjunto restrito de EDPs com geometria simples, condições de contorno simples e coeficientes constantes (ex.: a solução exponencial do decaimento radioativo, N(t)=N₀e^(−λt), ou — como a Aula 07 mostra — a geoterma de resfriamento de semi-espaço em regime simplificado). Esses casos servem sobretudo como **referência** para testar métodos numéricos. Assim que qualquer ingrediente realista entra — produção de calor variável com a profundidade, condutividade térmica que muda entre camadas, geometria irregular, reologia não linear dependente exponencialmente da própria temperatura calculada —, a fórmula fechada deixa de existir, e a solução numérica passa a ser a única saída. Essa é a situação **normal**, não a exceção, em geodinâmica quantitativa — e é o motivo de o módulo inteiro existir.
</details>

---

### 7. Verdadeiro ou Falso (justifique) — `geologia-avancado-m23-q07` · oa02 · 14 pts

"A fórmula de diferença central para a segunda derivada tem a mesma ordem de precisão que a fórmula de diferença central para a primeira derivada — ambas de segunda ordem —, então, para as duas, reduzir Δz pela metade reduz o erro de truncamento pela metade."

<details>
<summary>Ver resposta</summary>

**Falso** na segunda parte, embora a primeira esteja correta.

É verdade que ambas as fórmulas de diferença central (para a primeira e para a segunda derivada) são de **segunda ordem** de precisão — erro de truncamento proporcional a Δz². Mas "segunda ordem" significa que o erro escala com **Δz²**, não com Δz: reduzir Δz pela metade reduz o erro por um fator de (1/2)² = 1/4, não por um fator de 1/2. Confundir "ordem de precisão" com "fator de redução linear do erro" é um erro comum de leitura — a ordem descreve o **expoente** de Δz no termo de erro, não uma proporcionalidade direta.
</details>

---

### 8. Integração (Aulas 01–02) — `geologia-avancado-m23-q08` · oa01+oa02 · 12 pts

Explique por que a malha construída com `np.linspace`/`np.meshgrid` na Aula 01 (vetorização) é exatamente o tipo de estrutura sobre a qual a Aula 02 aplica a fórmula de diferença central — ou seja, por que "vetorizar" e "discretizar um domínio numa malha" se encaixam naturalmente, em vez de serem dois assuntos desconectados.

<details>
<summary>Ver resposta</summary>

Uma boa resposta observa que a discretização por diferenças finitas **cria** deliberadamente um conjunto de pontos (nós) igualmente espaçados — exatamente o que `np.linspace` produz. Uma vez que o domínio vira um array de nós, aplicar a fórmula de diferença central em todos os nós de uma vez (por exemplo, `(T[2:] - 2*T[1:-1] + T[:-2]) / dz**2`, como no exemplo trabalhado da Aula 02) é uma operação vetorizada: soma, subtração e divisão aplicadas a fatias inteiras do array, sem laço `for` explícito percorrendo nó por nó. A malha da Aula 01 não é um exemplo isolado de sintaxe NumPy — é a mesma estrutura de dados que sustenta toda a discretização espacial do restante do módulo, e a vetorização é o que torna essa discretização eficiente de calcular em código.
</details>

---

**Total: 100 pontos.**
