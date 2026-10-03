# Questionário parcial 3 — Módulo 23: Introdução à modelagem numérica geodinâmica

**Módulo:** [[23-modelagem-numerica-geodinamica-modulo|Módulo 23 — Introdução à modelagem numérica geodinâmica]]
**Cobertura:** Aulas 07 a 09 — calor na litosfera oceânica (resfriamento de semi-espaço) e continental (relação de Lachenbruch); reologia das rochas (elástico, viscoso, frágil, fluência por difusão e deslocamento, viscosidade efetiva); extensão e colisão continental, forças de placa e cunhas orogênicas.
**Recorte:** a aplicação da física de calor (Aulas 05-06) e da mecânica do contínuo (Aulas 03-04) a casos geológicos completos — geotermas, reologia dependente de temperatura, e a síntese final em cenários tectônicos de extensão e colisão.
**Objetivos avaliados:** `geologia-avancado-m23-oa03` (integral — a07), `geologia-avancado-m23-oa04` (integral — a08, a09)
**Pontuação total:** 100 pontos · o gabarito fica oculto; responda antes de abrir.

---

### 1. Aplicação / cálculo — `geologia-avancado-m23-q21` · oa03 · 10 pts

Pelo modelo de resfriamento de semi-espaço, calcule a temperatura a 20 km de profundidade numa litosfera oceânica de 40 Ma, usando T_m = 1.300 °C e κ = 1 × 10⁻⁶ m²/s.

<details>
<summary>Ver resposta</summary>

t = 40 × 10⁶ anos × 31.557.600 s/ano ≈ 1,2623 × 10¹⁵ s.

κt = 10⁻⁶ × 1,2623 × 10¹⁵ = 1,2623 × 10⁹ m². √(κt) ≈ 35.522 m. 2√(κt) ≈ 71.045 m.

η = z / (2√(κt)) = 20.000 / 71.045 ≈ **0,282**.

Interpolando a função erro entre erf(0,25) ≈ 0,2763 e erf(0,30) ≈ 0,3286: erf(0,282) ≈ 0,2763 + (0,282−0,25)/0,05 × (0,3286−0,2763) ≈ 0,2763 + 0,64×0,0523 ≈ **0,309**.

T = T_m × erf(η) = 1.300 × 0,309 ≈ **402 °C** a 20 km de profundidade, aos 40 Ma. (Pequenas diferenças na segunda casa decimal são esperadas por arredondamento da interpolação manual da função erro.)
</details>

---

### 2. Aplicação / cálculo — `geologia-avancado-m23-q22` · oa03 · 10 pts

Uma província continental tem produção radiogênica de superfície A₀ = 3,0 µW/m³, espessura de escala hr = 8 km, e fluxo de calor reduzido q_r = 25 mW/m². Calcule o fluxo de calor superficial esperado pela relação de Lachenbruch.

<details>
<summary>Ver resposta</summary>

q₀ = q_r + A₀ · hr = 25 mW/m² + (3,0 µW/m³ × 8.000 m)

3,0 µW/m³ × 8.000 m = 24.000 µW/m² = 24 mW/m² (dividindo por 1.000 para converter µW em mW).

q₀ = 25 + 24 = **49 mW/m²**.
</details>

---

### 3. Verdadeiro ou Falso (justifique) — `geologia-avancado-m23-q23` · oa03 · 8 pts

"O ajuste do modelo de resfriamento de semi-espaço a dados observados de batimetria e fluxo de calor oceânicos permanece bom para litosfera de qualquer idade, sem limite superior."

<details>
<summary>Ver resposta</summary>

**Falso.**

O ajuste em √idade se comporta bem apenas até aproximadamente **70-80 Ma**. Além dessa idade, os dados observados de batimetria e fluxo de calor se **achatam** (*flattening*) em relação à previsão do modelo de semi-espaço puro — um desvio que motivou refinamentos como o modelo de placa (Parsons & Sclater, 1977) e sua atualização GDH1 (Stein & Stein, 1992), que impõem um limite de espessura à litosfera (mantida por calor de baixo) em vez de deixá-la esfriar indefinidamente.
</details>

---

### 4. Dissertativa curta — `geologia-avancado-m23-q24` · oa03 · 9 pts

Compare os controles que governam a geoterma da litosfera oceânica e da litosfera continental estável. Por que uma litosfera continental antiga (cráton) é, em geral, mais fria a uma dada profundidade do que a litosfera oceânica jovem?

<details>
<summary>Ver resposta</summary>

Uma boa resposta cobre: a geoterma **oceânica** é controlada essencialmente por um único parâmetro — a **idade** da crosta —, num processo puramente condutivo e transiente (∂T/∂t ≠ 0): a placa "esquece" progressivamente a temperatura de formação na cordilheira. A geoterma **continental** antiga, em contraste, atinge um regime **estável** (∂T/∂t ≈ 0), em que a equação de calor se reduz a uma EDO no espaço, controlada pela **produção radiogênica** crustal e pelo **fluxo de calor de base**, praticamente independente de quando a crosta se formou. O cráton é mais frio não porque seja "mais velho no sentido de mais tempo esfriando" (ele já relaxou termicamente há muito tempo), mas porque sua geoterma de equilíbrio reflete um balanço de fontes de calor tipicamente menor (fluxo de base e produção radiogênica mais modestos) do que o calor "represado" numa litosfera oceânica jovem logo após sua formação na crista.
</details>

---

### 5. Múltipla escolha — `geologia-avancado-m23-q25` · oa04 · 9 pts

No jargão de modelagem geodinâmica, o termo "plástico" (como em "critério plástico friccional" ou modelo de Mohr-Coulomb) se refere a:

- a) sinônimo direto de ruptura frágil — os dois termos são intercambiáveis na literatura de modelagem
- b) o nome do **modelo numérico** friccional (Mohr-Coulomb ou Drucker-Prager) usado para **representar** comportamento frágil em códigos de meio contínuo, que não pode abrir uma fratura discreta — não é o processo físico de ruptura em si
- c) um quarto regime reológico distinto de elástico, viscoso e frágil
- d) o regime que domina exclusivamente em escalas de tempo geológicas longas

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Ruptura é **frágil** (*brittle*); deformação plástica, na mecânica dos materiais, é permanente e **contínua**, sem perda de coesão — o oposto conceitual de uma ruptura. Os dois termos aparecem juntos na literatura de modelagem geodinâmica por uma razão prática: um meio contínuo, por construção, não sabe abrir uma fratura discreta, então os códigos representam o comportamento frágil por um critério de escoamento **plástico** de atrito (Mohr-Coulomb ou Drucker-Prager), que limita a tensão suportada em função da pressão. É uma representação numérica do frágil, não uma afirmação de que romper seja plástico. "a" é exatamente a confusão que a Aula 08 alerta para evitar. "c" está errada: são apenas três regimes físicos (elástico, viscoso, frágil); "plástico" nomeia o modelo, não um quarto regime. "d" descreve mais o regime viscoso do que o frágil.
</details>

---

### 6. Múltipla escolha — `geologia-avancado-m23-q26` · oa04 · 8 pts

A energia de ativação Q = 540 kJ/mol usada no exemplo trabalhado da Aula 08 para fluência por deslocamento em olivino seco é atribuída a:

- a) Hirth & Kohlstedt (2003)
- b) Karato & Wu (1993)
- c) Ranalli (1995)
- d) Turcotte & Schubert (2014)

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Q = 540 kJ/mol vem de **Karato & Wu (1993)**, "Rheology of the upper mantle: A synthesis", *Science*. É um valor dentro da faixa de calibrações publicadas para esse mecanismo (aproximadamente 430 a 560 kJ/mol) — mas não é o mesmo número que **Hirth & Kohlstedt (2003)** relatam para o mesmo mecanismo (530 ± 4 kJ/mol, opção "a"): são calibrações experimentais distintas, e atribuir 540 kJ/mol a Hirth & Kohlstedt seria uma citação incorreta, mesmo os dois valores estando próximos.
</details>

---

### 7. Aplicação / cálculo — `geologia-avancado-m23-q27` · oa04 · 12 pts

Usando a mesma lei de Arrhenius do exemplo da Aula 08 (Q = 540 kJ/mol, R = 8,314 J/(mol·K)), mas agora para T₁ = 1.200 K e T₂ = 1.250 K (a mesma diferença de 50 K do exemplo original, porém em temperaturas absolutas mais altas), calcule a razão η_eff(T₁)/η_eff(T₂). O resultado é maior, menor ou igual à razão de ≈22 obtida no exemplo original (T₁=1000 K, T₂=1050 K)? O que isso revela sobre a sensibilidade do fator de Arrhenius?

<details>
<summary>Ver resposta</summary>

Q/R = 540.000 / 8,314 ≈ 64.950,7.

Q/(R·T₁) = 64.950,7 / 1.200 ≈ 54,13. Q/(R·T₂) = 64.950,7 / 1.250 ≈ 51,96.

Diferença dos expoentes: 54,13 − 51,96 ≈ **2,165**.

Razão = exp(2,165) ≈ **8,7**.

O resultado é **menor** que a razão ≈22 do exemplo original, embora a diferença absoluta de temperatura (ΔT=50 K) seja a mesma. Isso revela que a sensibilidade do fator de Arrhenius, exp(Q/RT), **não depende apenas de ΔT** — depende da temperatura absoluta em que essa diferença ocorre: em temperaturas mais altas (1.200-1.250 K, típicas de manto mais profundo), o mesmo ΔT produz uma variação relativa menor de viscosidade do que em temperaturas mais baixas (1.000-1.050 K, típicas de litosfera mais rasa ou mais fria). Ainda assim, ≈8,7× é uma variação substancial para apenas 50 K de diferença — o ponto pedagógico central da Aula 08 permanece: pequenos erros no campo térmico produzem erros grandes na viscosidade calculada.
</details>

---

### 8. Dissertativa curta — `geologia-avancado-m23-q28` · oa04 · 8 pts

Diferencie fluência por difusão e fluência por deslocamento em termos da relação entre tensão e taxa de deformação, e diga em que condições cada mecanismo domina.

<details>
<summary>Ver resposta</summary>

Uma boa resposta cobre: **fluência por difusão** tem relação **linear** entre tensão (σ) e taxa de deformação (ε̇) — comportamento Newtoniano, expoente de tensão n=1 —, e domina em tensões **baixas**, temperaturas **altas** e grãos **pequenos** (é o único dos dois mecanismos sensível ao tamanho de grão). **Fluência por deslocamento** tem relação **não linear**: a taxa de deformação escala com σⁿ, com n tipicamente entre 3 e 4 para minerais do manto (olivino ≈ 3,5), o que a torna independente do tamanho de grão e dominante em tensões **mais altas** — dobrar a tensão mais que dobra (multiplica por 2ⁿ) a taxa de deformação, uma sensibilidade muito mais forte que a fluência por difusão.
</details>

---

### 9. Verdadeiro ou Falso (justifique) — `geologia-avancado-m23-q29` · oa04 · 10 pts

"Segundo o exemplo trabalhado da Aula 09, aos 100 Ma após o rifteamento, resta ainda quase 20% da subsidência térmica total por vir."

<details>
<summary>Ver resposta</summary>

**Falso.**

Com τ = 62,8 Ma, a fração de subsidência térmica atingida aos 100 Ma é 1 − e^(−100/62,8) ≈ 1 − 0,2035 ≈ **0,7965** (≈80%). A fração que **ainda resta** é 1 − 0,7965 = **0,2034**, ou seja, **pouco mais de 20%** — não "quase 20%", que sugeriria um valor abaixo de 20%. A diferença de redação importa: "pouco mais de" (20,3%, ligeiramente acima) e "quase" (ligeiramente abaixo) descrevem posições opostas em relação ao limiar de 20%, mesmo estando os dois muito próximos dele.
</details>

---

### 10. Múltipla escolha — `geologia-avancado-m23-q30` · oa04 · 9 pts

Sobre as ordens de grandeza das forças motoras clássicas da tectônica de placas, slab-pull e ridge-push:

- a) slab-pull ≈ 10¹² N/m, ridge-push ≈ 10¹³ N/m — ridge-push é geralmente a força dominante
- b) slab-pull ≈ 10¹³ N/m, ridge-push ≈ 10¹² N/m — slab-pull é, quando presente, geralmente a força dominante, cerca de uma ordem de grandeza maior que ridge-push
- c) as duas forças têm a mesma ordem de grandeza, ≈10¹² N/m
- d) slab-pull e ridge-push são a mesma força vista de dois referenciais diferentes

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Estimativas clássicas de ordem de grandeza (Forsyth & Uyeda, 1975) situam o **slab-pull** — o arrasto gravitacional de uma placa oceânica subductada, mais densa que o manto ao redor por estar mais fria — em torno de **10¹³ N/m**, e o **ridge-push** — o deslizamento gravitacional a partir da topografia elevada da cordilheira meso-oceânica — cerca de uma ordem de grandeza menor, em torno de **10¹² N/m**. Isso torna o slab-pull, quando presente, a força dominante no balanço de forças de uma placa, embora o ridge-push permaneça relevante sobretudo em placas com pouca ou nenhuma subducção ativa em suas bordas. "a" inverte as ordens de grandeza. "c" e "d" não correspondem às estimativas nem à natureza física distinta dos dois mecanismos.
</details>

---

### 11. Dissertativa curta — `geologia-avancado-m23-q31` · oa04 · 7 pts

Explique, em termos gerais, a lógica da teoria da cunha crítica para a geometria de um cinturão de dobramentos e empurrões.

<details>
<summary>Ver resposta</summary>

Uma boa resposta cobre: a teoria da cunha crítica (Davis, Suppe & Dahlen, 1983) trata o material deformado como um material plástico friccional (Coulomb) empurrado sobre uma base de baixa resistência (um descolamento basal) — analogamente a uma pilha de areia empurrada por uma pá de bulldozer. A pilha mantém um ângulo de inclinação (o *taper*, soma do mergulho topográfico com o do descolamento basal) determinado pelo equilíbrio entre a resistência interna do material, a resistência de atrito na base e a inclinação topográfica — um ângulo **crítico** abaixo do qual a cunha se deforma internamente (engrossando) até atingi-lo, e acima do qual avança sem se deformar mais internamente, como um bloco relativamente rígido deslizando sobre a base. É essa mecânica de equilíbrio geométrico-friccional que explica a forma de cunha característica e previsível dos cinturões de empurrões.
</details>

---

**Total: 100 pontos.**
