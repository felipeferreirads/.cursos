# Questionário parcial 1 — Módulo 11: Sismoestratigrafia

**Módulo:** [[11-sismoestratigrafia-modulo|Módulo 11 — Sismoestratigrafia]]
**Cobertura:** Aulas 01 a 03 — fundamentos do método sísmico (impedância, coeficiente de reflexão, aquisição, processamento, resolução), amarração poço-sísmica e o refletor como linha de tempo, com os quatro padrões de terminação de refletores.
**Recorte:** o dado e o refletor individual — o que a sísmica mede, como nasce e é processada, o que resolve, como o poço calibra, e o que uma única terminação de refletor significa. A segunda metade do oa02 (superfícies-chave SB e MFS) fica para a parcial 2, que é onde a Aula 05 as ensina.
**Objetivos avaliados:** `geologia-avancado-m11-oa01` (integral, a01+a02), `geologia-avancado-m11-oa02` (parcial — terminação de refletores, a03)
**Pontuação total:** 100 pontos · o gabarito fica oculto; responda antes de abrir.

---

### 1. Múltipla escolha — `geologia-avancado-m11-q01` · oa01 · 10 pts

Qual das afirmações abaixo descreve corretamente o **limite de Widess (1973)**?

- a) É o critério de separação visual entre topo e base de uma camada, em torno de λ/4, também chamado de espessura de sintonia
- b) É o limiar, em torno de λ/8, abaixo do qual a forma da onda composta estabiliza (aproximando-se da derivada do pulso da fonte) e só a amplitude continua variando, de forma aproximadamente proporcional à espessura
- c) É outro nome para a espessura de sintonia (*tuning thickness*), o mesmo conceito do critério de Rayleigh, só que atribuído a outro autor
- d) É o valor de resolução vertical usado, na prática, quando um intérprete diz "a resolução vertical deste dado é X metros"

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Widess (1973) propôs o limiar de **λ/8**, onde a forma de onda do refletor composto já estabilizou e apenas a amplitude segue informando (aproximadamente) a espessura da camada — é o que permite estimar espessuras muito finas por inversão, mas sem geometria de topo/base separável. As alternativas "a", "c" e "d" descrevem, na verdade, o **critério de Rayleigh** (espessura de sintonia, λ/4) — o número usado no dia a dia como "resolução vertical" e o mais comumente (e erroneamente) atribuído a Widess em material didático. Confundir os dois limiares é o erro mais recorrente do assunto, inclusive na literatura de divulgação.
</details>

---

### 2. Verdadeiro ou Falso (justifique) — `geologia-avancado-m11-q02` · oa01 · 10 pts

"O coeficiente de reflexão RC = (Z₂−Z₁)/(Z₂+Z₁) dá diretamente a fração da **energia** sísmica incidente que retorna refletida numa interface."

<details>
<summary>Ver resposta</summary>

**Falso.**

RC é uma razão de **amplitudes**, não de energias. A fração da energia incidente que retorna refletida é **RC²**. Um RC de 0,1, por exemplo, devolve 10% da amplitude, mas apenas 1% da energia. A distinção importa porque RC é a grandeza que entra diretamente na construção do sismograma sintético (Aula 02) e em qualquer leitura quantitativa de amplitude — tratá-la como fração de energia superestima por um fator quadrático a energia efetivamente refletida.
</details>

---

### 3. Aplicação (cálculo) — `geologia-avancado-m11-q03` · oa01 · 15 pts

Um intervalo reservatório tem velocidade de 2.500 m/s, e a frequência dominante do levantamento sísmico nessa profundidade é 25 Hz.

Calcule: (a) o comprimento de onda dominante λ; (b) os dois limiares de resolução vertical (critério de Rayleigh e limite de Widess); (c) um reservatório de **15 m** de espessura consegue ser visto como dois refletores distintos (topo e base)? Sua forma de onda já estabilizou no regime de Widess? Justifique com os dois números calculados.

<details>
<summary>Ver resolução</summary>

**(a)** λ = V/f = 2.500/25 = **100 m**

**(b)** Critério de Rayleigh (espessura de sintonia, λ/4) = 100/4 = **25 m**. Limite de Widess (λ/8) = 100/8 = **12,5 m**.

**(c)** O reservatório de 15 m está **abaixo** do critério de Rayleigh (25 m) — logo, **não** é separável como dois refletores distintos de topo e base; produz um único refletor composto. Mas 15 m está **acima** do limite de Widess (12,5 m) — logo, sua forma de onda **ainda não estabilizou completamente**: está na zona de transição entre o pico de amplitude de sintonia (que ocorre em 25 m) e o regime puramente amplitude-proporcional de Widess (abaixo de 12,5 m). Conclusão: o reservatório não tem separação visual de topo e base, e também não está no regime "puro" de camada fina de Widess — está numa faixa intermediária onde a amplitude do refletor composto já variou de seu máximo de sintonia, mas a forma de onda ainda carrega alguma dependência de espessura além da simples proporcionalidade de amplitude.
</details>

---

### 4. Múltipla escolha — `geologia-avancado-m11-q04` · oa01 · 10 pts

Segundo Yilmaz (2001), qual é a ordem correta da cadeia de processamento sísmico convencional?

- a) Correção de NMO e empilhamento → deconvolução → migração
- b) Deconvolução → correção de NMO e empilhamento → migração
- c) Migração → deconvolução → correção de NMO e empilhamento
- d) Deconvolução → migração → correção de NMO e empilhamento

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A deconvolução (compressão do pulso da fonte, melhora de resolução vertical) é aplicada **antes** do empilhamento, sobre os traços individuais; só depois vem a correção de NMO e o empilhamento; a migração, que reposiciona geometricamente os refletores, é a última etapa da tríade. Inverter essa ordem — como em "a" — é um erro comum, porque cada etapa opera sobre um eixo diferente do dado (tempo, afastamento, espaço) e pressupõe a anterior já aplicada.
</details>

---

### 5. Dissertativa curta — `geologia-avancado-m11-q05` · oa01 · 10 pts

Explique por que o sismograma sintético, construído a partir de dados de poço, é comparável ao traço sísmico real — mesmo a série de coeficientes de reflexão do poço tendo uma resolução muito maior que a da sísmica. Qual etapa da construção do sintético reconcilia as duas escalas, e por quê?

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:**

A série de RC calculada a partir do perfil de impedância do poço tem a resolução centimétrica do próprio poço — ela registraria centenas de picos onde a sísmica mostra um punhado de refletores. O que reconcilia as duas escalas é a **convolução com a wavelet** do levantamento sísmico: como a wavelet tem banda de frequências limitada (a mesma banda do dado sísmico), convolucioná-la com a série de RC funciona como um filtro passa-banda, que degrada de propósito a resolução do poço até a resolução da sísmica. O sintético resultante não é "o poço", é "o poço visto com os olhos da sísmica" — por isso é comparável ao traço real, e por isso a amarração informa o que existe dentro de um refletor composto sem tornar isso visível diretamente na seção.
</details>

---

### 6. Verdadeiro ou Falso (justifique) — `geologia-avancado-m11-q06` · oa01 · 10 pts

"Um desajuste de amarração poço-sísmica que cresce progressivamente com a profundidade é mais provavelmente causado por uma anomalia litológica pontual (como gás na formação) do que por um erro sistemático de velocidade."

<details>
<summary>Ver resposta</summary>

**Falso.**

É o oposto: uma anomalia litológica pontual (gás, anisotropia local) produz um desajuste **concentrado** num intervalo específico, não uma deriva que cresce continuamente com a profundidade. Um desvio que cresce progressivamente é assinatura de um **erro sistemático e acumulativo**, tipicamente de velocidade — por exemplo, um sônico rodado em más condições de furo, sofrendo "salto de ciclo", que registra tempos de trânsito artificialmente altos (velocidade subestimada) e atrasa o sintético em relação ao dado real de forma cumulativa. O sinal do desvio é diagnóstico: velocidade subestimada sempre atrasa o sintético (TWT maior), nunca o adianta.
</details>

---

### 7. Aplicação (cálculo) — `geologia-avancado-m11-q07` · oa01 · 15 pts

Uma interface separa uma camada superior de impedância Z₁ = 6,0 × 10⁶ kg/(m²·s) de uma camada inferior de impedância Z₂ = 8,0 × 10⁶ kg/(m²·s).

Calcule: (a) o coeficiente de reflexão RC; (b) a fração de amplitude e a fração de energia que retornam refletidas; (c) interprete o resultado: esse é um refletor forte ou fraco, e o que acontece com a maior parte da energia incidente?

<details>
<summary>Ver resolução</summary>

**(a)** `RC = (Z₂ − Z₁)/(Z₂ + Z₁) = (8,0 − 6,0)/(8,0 + 6,0) = 2,0/14,0 ≈ 0,143`

**(b)** Fração de **amplitude** refletida ≈ **14,3%** (o próprio RC). Fração de **energia** refletida = RC² ≈ 0,143² ≈ **2,04%**.

**(c)** É um refletor de amplitude moderada a fraca — um RC de 0,14 é um contraste real, mas está longe dos contrastes fortes (RC > 0,3, por exemplo água-gás ou topo de sal) que geram os refletores mais brilhantes de uma seção. Cerca de **98% da energia incidente continua se propagando para baixo**, disponível para iluminar (e refletir em) interfaces mais profundas — é por isso que um único contraste forte e raso pode "roubar" energia da iluminação de alvos mais profundos, um efeito relevante no planejamento de levantamentos em bacias com corpos de sal ou anidrita rasos.
</details>

---

### 8. Múltipla escolha — `geologia-avancado-m11-q08` · oa02 · 10 pts

O que distingue **onlap** de **downlap**, segundo a definição correta de *baselap*?

- a) A inclinação absoluta da extremidade da camada — se a ponta está muito inclinada, é downlap; se está pouco inclinada, é onlap
- b) Qual das duas superfícies — o refletor ou a superfície de base contra a qual ele termina — mergulha mais: se a superfície de base mergulha mais que o refletor, é onlap; se o refletor mergulha mais que a superfície de base, é downlap
- c) A cor ou a amplitude do refletor na seção sísmica
- d) A profundidade absoluta em que a terminação ocorre — onlap é sempre raso, downlap é sempre profundo

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Onlap e downlap são os dois padrões de *baselap* (terminação contra a superfície de base), e o critério que os separa é a inclinação **relativa** entre o refletor e a superfície de base — não a inclinação absoluta da ponta da camada. Esse critério é o que sobrevive mesmo em clinoformas obliquas paralelas, cujo mergulho é constante até a base (um caso em que definir pela inclinação absoluta da extremidade falharia). "a" é o erro clássico de definição por inclinação absoluta; "c" e "d" não são critérios geométricos válidos.
</details>

---

### 9. Dissertativa curta — `geologia-avancado-m11-q09` · oa02 · 10 pts

Explique a diferença conceitual entre **toplap** e **truncamento erosivo**, e por que confundir os dois leva a um erro de interpretação sobre a história de uma bacia.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:**

**Toplap:** refletores terminam mergulho acima contra uma superfície suprajacente de baixo ângulo, sem evidência de erosão — a terminação registra ausência de deposição continuada (*sedimentary bypass*) acima de um certo nível, não remoção de material já depositado.

**Truncamento erosivo:** refletores são cortados abruptamente por uma superfície suprajacente, com evidência de que material foi de fato removido (erosão subaérea ou submarina).

**O erro de confundi-los:** toplap implica que a sedimentação simplesmente não avançou além daquele ponto — não há registro perdido, apenas não formado. Truncamento implica que **havia** registro sedimentar ali e ele foi removido. Interpretar um truncamento como toplap subestima a magnitude do hiato temporal e da erosão associada (pode esconder uma discordância regional importante, como a discordância de ruptura do Módulo 10); interpretar um toplap como truncamento superestima a erosão e pode levar a inferir uma queda de nível relativo do mar mais severa do que realmente ocorreu.
</details>

---

## Gabarito resumido

| Questão | ID | Resposta |
|---|---|---|
| 1 | q01 | b (Widess = λ/8; λ/4 é Rayleigh/sintonia) |
| 2 | q02 | Falso (RC é razão de amplitudes; energia = RC²) |
| 3 | q03 | λ = 100 m; Rayleigh = 25 m; Widess = 12,5 m; 15 m está abaixo de Rayleigh (não separável) e acima de Widess (forma de onda ainda não estabilizada) |
| 4 | q04 | b (deconvolução → NMO/empilhamento → migração) |
| 5 | q05 | ver comentário (convolução com a wavelet filtra o poço até a resolução da sísmica) |
| 6 | q06 | Falso (deriva crescente = erro sistemático de velocidade; anomalia pontual = desajuste localizado) |
| 7 | q07 | RC ≈ 0,143; amplitude ≈ 14,3%; energia ≈ 2,04%; refletor moderado, ~98% da energia segue em profundidade |
| 8 | q08 | b (inclinação relativa entre refletor e superfície de base, não a absoluta) |
| 9 | q09 | ver comentário (toplap = bypass sem remoção; truncamento = remoção comprovada de material) |
