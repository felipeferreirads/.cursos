# Questionário parcial 1 — Módulo 05: Mecânica de rochas

**Módulo:** [[05-mecanica-de-rochas-modulo|Módulo 05 — Mecânica de rochas]]
**Cobertura:** Aulas 01 a 04 — tensão e círculo de Mohr, propriedades físicas e comportamento reológico, critérios de ruptura, descontinuidades.
**Objetivos avaliados:** geologia-avancado-m05-oa01, geologia-avancado-m05-oa02 (parcial), geologia-avancado-m05-oa03 (parcial)

---

### 1. Múltipla escolha
Um ponto de um maciço rochoso tem σx = 60 MPa, σy = 20 MPa e τxy = 0 MPa (eixos x e y já coincidindo com direções principais). A tensão cisalhante máxima nesse ponto é:

a) 0 MPa, porque não há cisalhamento nos eixos medidos
b) 20 MPa
c) 40 MPa
d) 80 MPa

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Como τxy = 0, os eixos x e y já são as direções principais: σ1 = 60 MPa, σ3 = 20 MPa. A tensão cisalhante máxima é τmáx = (σ1−σ3)/2 = (60−20)/2 = 20 MPa, ocorrendo a 45° das direções principais — nunca nos próprios eixos principais, onde o cisalhamento é zero por definição (Aula 01).
</details>

---

### 2. Verdadeiro ou Falso
"Em mecânica das rochas, a convenção usual trata tração como tensão positiva, da mesma forma que a mecânica dos sólidos clássica."

<details>
<summary>Ver resposta</summary>

**Falso.**

A mecânica das rochas (e a mecânica dos solos) adota convencionalmente **compressão positiva**, o oposto da convenção de tração positiva da mecânica dos sólidos clássica — uma escolha prática, já que o estado de tensão de interesse em rocha é predominantemente compressivo (Aula 01).
</details>

---

### 3. Dissertativa curta
Explique, em até quatro linhas, o que é dilatância numa curva tensão-deformação de compressão uniaxial e em que fase da curva ela aparece.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:** dilatância é o aumento líquido de volume do corpo de prova apesar da compressão contínua, causado pela abertura e propagação de microfissuras que mais que compensa a compactação dos poros. Aparece na fase de propagação instável de fissuras, próximo do pico de resistência (tipicamente 80–95% da UCS) (Aula 02).

**Comentário:** a dilatância pré-pico em laboratório é o mesmo fenômeno físico que causa dano progressivo e afrouxamento do maciço ao redor de uma escavação subterrânea, retomado na Aula 07.
</details>

---

### 4. Aplicação (cálculo)
Um estado de tensão num ponto tem σx = 50 MPa, σy = 10 MPa e τxy = 15 MPa. Calcule as tensões principais σ1 e σ3.

<details>
<summary>Ver resolução</summary>

Centro: C = (50+10)/2 = 30 MPa.

Raio: R = √[((50−10)/2)² + 15²] = √[20² + 15²] = √(400+225) = √625 = 25 MPa.

σ1 = C+R = 30+25 = 55 MPa. σ3 = C−R = 30−25 = 5 MPa.

(Aula 01 — mesmo método do exemplo trabalhado da aula, com valores diferentes.)
</details>

---

### 5. Múltipla escolha
O critério de Griffith original, para o caso 2D, prevê uma razão teórica entre resistência à compressão uniaxial e resistência à tração de:

a) 2
b) 8
c) 20
d) A mesma razão que Mohr-Coulomb, sempre

<details>
<summary>Ver resposta</summary>

**Resposta: b**

O critério de Griffith original prevê uma razão teórica de 8:1 entre compressão e tração — valor tipicamente excedido pelas rochas reais, o que motivou versões modificadas do critério (Aula 03).
</details>

---

### 6. Verdadeiro ou Falso
"A reta de Mohr-Coulomb, extrapolada sem correção para tensões de confinamento negativas (tração), prevê corretamente a resistência à tração real da rocha, medida por ensaio brasileiro."

<details>
<summary>Ver resposta</summary>

**Falso.**

A extrapolação da reta de Mohr-Coulomb para tração dá um valor de resistência à tração maior, em módulo, do que o valor real medido — a ruptura em tração ocorre por um mecanismo físico diferente (propagação de microfissuras, descrito por Griffith), não pelo mesmo mecanismo de atrito por cisalhamento que governa a compressão. Por isso, aplicações práticas impõem um corte de tração (Aula 03).
</details>

---

### 7. Múltipla escolha
Segundo o critério de Barton-Bandis, o ângulo de atrito efetivo de pico de uma descontinuidade rugosa, φb + JRC·log10(JCS/σn):

a) É constante, independente da tensão normal aplicada
b) Aumenta com o aumento da tensão normal
c) Diminui com o aumento da tensão normal, convergindo para φb em altas tensões
d) Só se aplica a descontinuidades sem preenchimento

<details>
<summary>Ver resposta</summary>

**Resposta: c**

O termo de rugosidade JRC·log10(JCS/σn) diminui à medida que σn aumenta (o argumento do logaritmo se aproxima de 1), refletindo que sob confinamento alto as asperezas são cisalhadas em vez de contornadas — o ângulo efetivo converge para φb (Aula 04).
</details>

---

### 8. Dissertativa curta
Um bloco de rocha intacta entre descontinuidades tem UCS de 150 MPa em laboratório. Explique por que essa informação sozinha não é suficiente para concluir que o maciço rochoso do qual esse bloco faz parte é estável para uma dada escavação.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:** a resistência do maciço depende não apenas da resistência da rocha intacta, mas também da geometria (orientação, espaçamento, persistência) e da resistência ao cisalhamento das descontinuidades que atravessam o maciço. Se as descontinuidades tiverem baixa resistência ao cisalhamento e estiverem desfavoravelmente orientadas em relação à escavação, é o comportamento delas — não da rocha intacta — que determina a estabilidade, mesmo com UCS alta (Aula 04).

**Comentário:** essa distinção entre "resistência da rocha" e "resistência do maciço" é o eixo conceitual retomado nas classificações geomecânicas (Aula 06) e na análise de estabilidade (Aula 07).
</details>

---

### Gabarito resumido

| Questão | Resposta |
|---|---|
| 1 | b |
| 2 | Falso |
| 3 | ver comentário |
| 4 | σ1 = 55 MPa; σ3 = 5 MPa |
| 5 | b |
| 6 | Falso |
| 7 | c |
| 8 | ver comentário |
