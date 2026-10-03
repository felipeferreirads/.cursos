# Questionário parcial 2 — Módulo 01: Hidrogeologia e recursos hídricos

**Módulo:** [[01-hidrogeologia-recursos-hidricos-modulo|Módulo 01 — Hidrogeologia e recursos hídricos]]
**Cobertura:** Aulas 05 a 07 — testes de bombeamento e de aquífero, gestão quantitativa, águas subterrâneas e mudanças climáticas.
**Objetivos avaliados:** geologia-avancado-m01-oa03 (parcial), geologia-avancado-m01-oa04

---

### 1. Múltipla escolha
Num teste de bombeamento interpretado pelo método de Cooper-Jacob, um achatamento da inclinação do gráfico s versus log(t) depois de algum tempo sugere:

a) Um limite impermeável próximo (barreira de fluxo)
b) Uma fonte adicional de água entrando no sistema (recarga induzida)
c) Que o teste foi mal executado e deve ser descartado
d) Que o aquífero é homogêneo e infinito, confirmando as hipóteses de Theis

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Achatamento (Δs por ciclo logarítmico menor) indica que uma fonte adicional está alimentando o sistema — um rio conectado ou drenança de um aquífero vizinho mais transmissivo. O padrão oposto (aumento de inclinação) indicaria um limite impermeável (Aula 05).
</details>

---

### 2. Verdadeiro ou Falso
"Num teste de degraus de vazão (step-drawdown), o coeficiente C (perda de carga não linear) reflete propriedades do aquífero, enquanto o coeficiente B reflete a qualidade construtiva do poço."

<details>
<summary>Ver resposta</summary>

**Falso — está invertido.**

B (perda de carga linear com Q) reflete propriedades do aquífero (a mesma física de Theis/Cooper-Jacob); C (perda de carga não linear, proporcional a Q²) reflete a qualidade construtiva do poço — turbulência no filtro, no pré-filtro e na tubulação, associada a colmatação ou projeto inadequado (Aula 05).
</details>

---

### 3. Aplicação (cálculo)
Um teste de bombeamento com Q = 2.000 m³/dia produz, no método de Cooper-Jacob, uma reta com inclinação Δs = 0,45 m por ciclo logarítmico. Calcule a transmissividade T.

<details>
<summary>Ver resolução</summary>

T = 2,3Q / (4π·Δs) = (2,3 × 2.000) / (4π × 0,45) = 4.600 / 5,655 ≈ 813 m²/dia.

(Mesma fórmula do exemplo trabalhado da Aula 05, aplicada a valores diferentes.)
</details>

---

### 4. Dissertativa curta
Um gestor argumenta que um aquífero está sendo explorado de forma sustentável porque a extração total anual é menor que a recarga média anual estimada (critério de "vazão segura"). Explique por que esse critério, isoladamente, pode ser insuficiente.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:** o critério de vazão segura ignora que (1) a extração pode induzir aumento de recarga ou redução de descarga natural, de modo que a "recarga natural" não é uma constante independente do próprio bombeamento (princípio da captura); e (2) mesmo uma extração formalmente dentro do balanço de massa pode causar impactos inaceitáveis — redução de vazão de base abaixo de limiar ecológico, secamento de nascentes, intrusão salina — muito antes de esgotar o balanço (Aula 06, crítica de Sophocleous 2000).

**Comentário:** o conceito moderno de vazão sustentável substitui o critério puramente quantitativo por um critério de impacto tolerável, que envolve escolha técnica e social, não só cálculo de balanço de massa.
</details>

---

### 5. Aplicação (cálculo)
Um aquífero costeiro tem nível freático a 2,2 m acima do nível do mar. Pela relação de Ghyben-Herzberg, estime a profundidade da interface água doce-água salgada abaixo do nível do mar.

<details>
<summary>Ver resolução</summary>

z ≈ 40 × h = 40 × 2,2 = 88 m abaixo do nível do mar.

(Fórmula e fator de aproximação da Aula 06 — z = h·[ρf/(ρs−ρf)] ≈ 40h.)
</details>

---

### 6. Múltipla escolha
Segundo a Constituição Federal brasileira, o domínio das águas subterrâneas é:

a) Sempre da União, independentemente do Estado
b) Sempre dos Estados
c) Municipal, delegado pela União
d) Depende do domínio do rio superficial sobrejacente

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Diferentemente das águas superficiais (que podem ser de domínio da União ou dos Estados conforme o corpo hídrico), as águas subterrâneas são, pela Constituição Federal de 1988 (art. 26, I), sempre de domínio estadual — o que torna a outorga de água subterrânea, na prática brasileira, majoritariamente uma competência dos órgãos gestores estaduais (Aula 06).
</details>

---

### 7. Verdadeiro ou Falso
"Um aquífero fóssil, como o Sistema Aquífero da Núbia, pode ser explorado indefinidamente como recurso renovável, desde que a extração seja bem planejada."

<details>
<summary>Ver resposta</summary>

**Falso.**

Um aquífero fóssil tem recarga atual desprezível em escala de tempo humana — extraí-lo é minerar um estoque finito, não usar um recurso renovável. Um planejamento adequado deve reconhecer o horizonte de exaustão calculável, tratando-o como uma mina, não como fonte perene (Aula 07).
</details>

---

### 8. Dissertativa curta
Explique por que a subsidência do terreno causada pela superexplotação de um aquífero confinado em sedimentos argilosos é considerada, na prática, irreversível.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:** a subsidência resulta da compactação inelástica da matriz sedimentar fina (argila/silte) quando a tensão efetiva aumenta além de um limite histórico nunca antes atingido. Essa compactação envolve rearranjo permanente dos grãos argilosos; mesmo que o nível piezométrico se restabeleça depois (reduzindo a tensão efetiva de volta), o arranjo dos grãos não se desfaz, então o terreno não recupera a elevação perdida (Aula 07).

**Comentário:** casos históricos como o Valle de Mexico e o Valle Central da Califórnia ilustram subsidências acumuladas de vários metros ao longo de décadas de bombeamento intensivo.
</details>

---

### Gabarito resumido

| Questão | Resposta |
|---|---|
| 1 | b |
| 2 | Falso (invertido) |
| 3 | T ≈ 813 m²/dia |
| 4 | ver comentário |
| 5 | z ≈ 88 m |
| 6 | b |
| 7 | Falso |
| 8 | ver comentário |
