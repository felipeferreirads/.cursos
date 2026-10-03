# Questionário final cumulativo — Módulo 05: Mecânica de rochas

**Módulo:** [[05-mecanica-de-rochas-modulo|Módulo 05 — Mecânica de rochas]]
**Cobertura:** Aulas 01 a 07 (módulo completo).
**Objetivos avaliados:** geologia-avancado-m05-oa01, oa02, oa03, oa04 (todos)

---

### 1. Múltipla escolha (oa01)
Num plano principal (onde atua uma tensão principal), a tensão cisalhante é:

a) Máxima
b) Igual à tensão normal média
c) Zero, por definição
d) Sempre negativa (tração)

<details><summary>Ver resposta</summary>

**Resposta: c** (Aula 01)
</details>

---

### 2. Verdadeiro ou Falso (oa01)
"O módulo de Young estático, obtido por ensaio de compressão, é tipicamente maior que o módulo dinâmico, obtido por velocidade de onda sônica."

<details><summary>Ver resposta</summary>

**Falso.** É o oposto: o módulo dinâmico é sistematicamente maior, porque a rocha responde de forma mais rígida a uma solicitação de altíssima frequência do que a uma solicitação estática, que dá tempo para microfissuras se fecharem e se propagarem (Aula 02).
</details>

---

### 3. Aplicação (cálculo, oa01)
Um estado de tensão tem σx = 35 MPa, σy = 25 MPa e τxy = 12 MPa. Calcule σ1, σ3 e a tensão cisalhante máxima.

<details><summary>Ver resolução</summary>

C = (35+25)/2 = 30 MPa.

R = √[((35−25)/2)² + 12²] = √[5² + 12²] = √(25+144) = √169 = 13 MPa.

σ1 = 30+13 = 43 MPa. σ3 = 30−13 = 17 MPa. τmáx = R = 13 MPa.

(Mesmo método da Aula 01.)
</details>

---

### 4. Múltipla escolha (oa02)
No critério de Hoek-Brown para **rocha intacta** (não maciço fraturado), os parâmetros s e mb assumem, respectivamente:

a) s = 0 e mb = 0
b) s = 1 e mb = mi
c) s = mi e mb = 1
d) Ambos dependem apenas do GSI, nunca da litologia

<details><summary>Ver resposta</summary>

**Resposta: b** (Aula 03, retomado na Aula 06)
</details>

---

### 5. Dissertativa curta (oa02)
Compare, em até cinco linhas, por que o critério de Griffith e o critério de Mohr-Coulomb divergem na previsão da resistência à tração de uma rocha.

<details><summary>Ver resposta comentada</summary>

**Resposta esperada:** Mohr-Coulomb é uma reta calibrada para o regime de compressão por atrito ao longo de um plano de cisalhamento; extrapolada para tração, prevê uma resistência maior, em módulo, do que a real. Griffith parte de um modelo físico diferente — propagação de microfissuras pré-existentes sob concentração de tensão de tração na ponta da fissura —, adequado ao mecanismo real de ruptura em tração, e prevê uma relação parabólica entre σ1 e σ3, com razão teórica compressão/tração de 8 (tipicamente excedida na prática) (Aula 03).
</details>

---

### 6. Aplicação (cálculo, oa02)
A 600 m de profundidade, com densidade média de 2.600 kg/m³, um ensaio de fraturamento hidráulico registra shut-in de 10,5 MPa. Calcule σv e K = σh/σv.

<details><summary>Ver resolução</summary>

σv = 2.600×9,81×600 ≈ 1,531×10⁷ Pa ≈ 15,3 MPa.

K = 10,5/15,3 ≈ 0,69.

(Mesmo método da Aula 05.)
</details>

---

### 7. Verdadeiro ou Falso (oa03)
"Uma descontinuidade muito rugosa (JRC alto) sempre tem resistência ao cisalhamento maior que uma descontinuidade lisa, em qualquer nível de tensão normal."

<details><summary>Ver resposta</summary>

**Falso.** Em tensões normais muito altas, as asperezas de qualquer rugosidade tendem a ser cisalhadas em vez de contornadas, e o ângulo de atrito efetivo converge para φb — a diferença de resistência entre uma junta lisa e uma rugosa é mais relevante justamente em tensões normais baixas (Aula 04).
</details>

---

### 8. Múltipla escolha (oa03)
Qual das quatro classificações geomecânicas do módulo é a única que se converte diretamente nos parâmetros mb, s e a do critério de Hoek-Brown generalizado?

a) RMR
b) Q
c) GSI
d) SMR

<details><summary>Ver resposta</summary>

**Resposta: c** (Aula 06)
</details>

---

### 9. Aplicação (cálculo, oa03)
Um maciço tem: UCS = 120 MPa (12 pontos), RQD = 85% (17 pontos), espaçamento de 0,6 m (15 pontos), condição de descontinuidades boa, ligeiramente rugosa e sã (25 pontos), maciço seco (15 pontos). Calcule o RMR básico e classifique o maciço.

<details><summary>Ver resolução</summary>

RMR = 12+17+15+25+15 = 84.

**Classificação: Classe I (RMR 81–100), maciço muito bom.**

(Mesmo método da Aula 06.)
</details>

---

### 10. Aplicação (cálculo, oa04)
Um talude tem um bloco com peso W = 3.200 kN sobre um plano de ruptura planar com mergulho ψp = 30°, área A = 150 m², coesão c = 15 kPa e ângulo de atrito φ = 34°. Sem água na trinca de tração, calcule o fator de segurança.

<details><summary>Ver resolução</summary>

N = W·cosψp = 3.200×cos30° ≈ 3.200×0,8660 ≈ 2.771 kN.

T = W·senψp = 3.200×sen30° = 3.200×0,5 = 1.600 kN.

Resistência = c·A + N·tanφ = 15×150 + 2.771×tan34° = 2.250 + 2.771×0,6745 ≈ 2.250 + 1.869 ≈ 4.119 kN.

FS = 4.119/1.600 ≈ 2,57.

(Mesmo método do exemplo trabalhado da Aula 07.)
</details>

---

### 11. Verdadeiro ou Falso (oa04)
"Segundo as equações de Kirsch, para uma abertura circular sob campo de tensão biaxial com K = σh/σv < 1 (campo dominado pela tensão vertical), as paredes laterais concentram tensão tangencial maior que o teto e o piso, podendo o teto e o piso inclusive entrar em tração se K for suficientemente baixo (K < 1/3)."

<details><summary>Ver resposta</summary>

**Verdadeiro.**

Nas paredes, a tensão tangencial é 3σv−σh = (3−K)·σv; no teto/piso, é 3σh−σv = (3K−1)·σv. A diferença (paredes − teto/piso) é (4−4K)·σv, positiva sempre que K<1 — ou seja, com confinamento horizontal relativamente baixo, as paredes concentram tensão tangencial maior que o teto e o piso. Além disso, (3K−1)·σv é negativo (tração) quando K<1/3, explicando por que tetos de escavação sob baixo confinamento horizontal são propensos a desplacamento e queda de blocos (Aula 07).
</details>

---

### 12. Dissertativa curta (oa04)
Explique, em até cinco linhas, por que instalar o suporte de uma escavação subterrânea "o mais rápido possível e o mais rígido possível" não é necessariamente a estratégia mais segura, à luz do método de convergência-confinamento.

<details><summary>Ver resposta comentada</summary>

**Resposta esperada:** o método de convergência-confinamento mostra que o maciço converge progressivamente à medida que a tensão se redistribui após a escavação, e que a interação suporte-maciço depende do ponto dessa curva de convergência em que o suporte é instalado. Um suporte muito rígido instalado cedo demais, antes de o maciço ter dissipado parte da energia por deformação controlada, é sobrecarregado por toda a convergência ainda por vir e pode atrair carga excessiva e falhar; o objetivo é permitir alguma convergência controlada antes de confinar, mobilizando a própria resistência do maciço, em vez de tentar impedir toda deformação desde o primeiro instante (Aula 07).
</details>

---

### Gabarito resumido

| Questão | Resposta |
|---|---|
| 1 | c |
| 2 | Falso |
| 3 | σ1 = 43 MPa; σ3 = 17 MPa; τmáx = 13 MPa |
| 4 | b |
| 5 | ver comentário |
| 6 | σv ≈ 15,3 MPa; K ≈ 0,69 |
| 7 | Falso |
| 8 | c |
| 9 | RMR = 84 (Classe I) |
| 10 | FS ≈ 2,57 |
| 11 | Falso |
| 12 | ver comentário |

## Cobertura de objetivos confirmada
- geologia-avancado-m05-oa01 — questões 1, 2, 3
- geologia-avancado-m05-oa02 — questões 4, 5, 6
- geologia-avancado-m05-oa03 — questões 7, 8, 9
- geologia-avancado-m05-oa04 — questões 10, 11, 12
