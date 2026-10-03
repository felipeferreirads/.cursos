# Questionário parcial 1 — Módulo 09: Geometalurgia

**Módulo:** [[09-geometalurgia-modulo|Módulo 09 — Geometalurgia]]
**Cobertura:** Aulas 01 a 03 — vocabulário e programa geometalúrgico; caracterização de minério e ganga (partição do metal e mineralogia de processo); textura, tamanho de grão e liberação mineral.
**Recorte:** o que este minério é — diagnóstico da variabilidade metalúrgica, antes de qualquer decisão de circuito.
**Objetivos avaliados:** `geologia-avancado-m09-oa01` (integral), `geologia-avancado-m09-oa02` (integral)
**Pontuação total:** 100 pontos · o gabarito fica oculto; responda antes de abrir.

---

### 1. Múltipla escolha — `geologia-avancado-m09-q01` · oa01 · 10 pts
Duas plantas processam minérios com o mesmo teor de alimentação (1,00 % Cu), mas uma entrega recuperação de 92 % e a outra, de 65 %. O que esse contraste demonstra?

- a) A recuperação é proporcional ao teor de alimentação, e a diferença só pode vir de erro de amostragem
- b) A recuperação depende de como o metal está distribuído entre os minerais e de como esses minerais estão arranjados na rocha — não da quantidade de metal presente
- c) A razão de concentração (`F/C`) determina sozinha a recuperação de qualquer minério
- d) Duas plantas com o mesmo teor de alimentação sempre têm a mesma razão de enriquecimento (`c/f`)

<details>
<summary>Ver resposta</summary>

**Resposta: b**

É o ponto de virada conceitual da Aula 01: recuperação e teor são grandezas independentes. A recuperação responde a mineralogia (em que mineral o metal está) e a textura (como esses minerais estão arranjados e liberam), não à quantidade de metal presente na rocha. A alternativa "a" comete exatamente o erro que a aula nomeia como recorrente em quem vem da geologia; "c" confunde uma grandeza (razão de concentração, toneladas por tonelada de concentrado) com a variável que ela não determina sozinha; "d" está errada porque `c/f` depende do teor do concentrado obtido, que também varia entre minérios de mesmo teor de alimentação.
</details>

---

### 2. Verdadeiro ou Falso (justifique) — `geologia-avancado-m09-q02` · oa01 · 10 pts
"Teor é uma variável primária e recuperação é uma variável proxy, porque o teor é a grandeza mais barata e mais disponível para alimentar o modelo de blocos."

<details>
<summary>Ver resposta</summary>

**Falso.**

A afirmação inverte as duas categorias. **Teor é a proxy**: barato, medido em praticamente todos os furos, presente em toda a base de dados de sondagem. **Recuperação é a variável primária**: cara de medir (exige teste metalúrgico, que é destrutivo e compete pelo testemunho), e por isso existe em poucos pontos do depósito. A lógica da modelagem geometalúrgica (Aula 06) é justamente construir uma relação entre a proxy densa e barata (teor, entre outras) e a primária esparsa e cara (recuperação), e propagar essa relação a todos os blocos — o oposto do que a frase propõe.
</details>

---

### 3. Aplicação (cálculo) — `geologia-avancado-m09-q03` · oa01 · 15 pts
Dois blocos de um pórfiro de cobre têm o mesmo teor de alimentação, `f = 1,20 % Cu`, e a mesma tonelagem, `8 000 t`. No **bloco C** (sulfeto primário) a recuperação de bancada é `R_C = 88 %` e o concentrado sai a `26 % Cu`. No **bloco D** (zona de transição) a recuperação é `R_D = 58 %` e o concentrado sai a `22 % Cu`. O preço pago é `US$ 9 000 / t` de Cu contido no concentrado.

Calcule: (a) o cobre recuperável e a receita bruta de cada bloco; (b) a razão de concentração (`F/C`) e a razão de enriquecimento (`c/f`) do bloco C; (c) a diferença absoluta e percentual de receita entre os dois blocos.

<details>
<summary>Ver resolução</summary>

Cobre contido em cada bloco: `m_Cu = 8 000 × 0,0120 = 96,0 t Cu`

**Bloco C:**
`Cu recuperado = 96,0 × 0,88 = 84,48 t`
`Receita = 84,48 × 9 000 = US$ 760 320`
`Massa de concentrado = 84,48 / 0,26 = 324,9 t`
`F/C = 8 000 / 324,9 ≈ 24,6`  ·  `c/f = 26 / 1,20 ≈ 21,7`

**Bloco D:**
`Cu recuperado = 96,0 × 0,58 = 55,68 t`
`Receita = 55,68 × 9 000 = US$ 501 120`
`Massa de concentrado = 55,68 / 0,22 ≈ 253,1 t`

**Diferença:** `84,48 − 55,68 = 28,80 t Cu`; `760 320 − 501 120 = US$ 259 200`, uma diferença de `259 200 / 760 320 ≈ 34 %` na receita — apesar de teor e tonelagem idênticos nos dois blocos. Se o plano de lavra sequenciar o bloco D (transição) para o início da vida da mina, essa perda incide justamente nos anos que mais pesam no valor presente.
</details>

---

### 4. Múltipla escolha — `geologia-avancado-m09-q04` · oa01 · 10 pts
Qual das afirmações abaixo explica corretamente por que a **partição do metal** (*deportment*) é a primeira pergunta que a mineralogia de processo precisa responder?

- a) Porque ela determina o preço de venda do minério antes de qualquer teste metalúrgico
- b) Porque cada mineral portador do metal tem uma rota própria de recuperação, e a fração do metal presa em minerais que a rota não consegue separar fixa um teto de recuperação antes de qualquer questão de circuito, reagente ou moagem
- c) Porque a partição substitui a necessidade de moer o minério
- d) Porque só minerais opacos podem conter metal de interesse econômico

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A partição diz em que minerais o metal está — e cada mineral portador tem uma rota (flotação de sulfetos, lixiviação ácida, etc.) e uma recuperação próprias dessa rota. Isso fixa um teto **antes** de qualquer discussão de liberação, reagente ou circuito: nenhum ajuste de flotação recupera metal que está num mineral que a flotação não alcança. "a" confunde partição com precificação; "c" inverte a relação entre mineralogia e cominuição; "d" é falso — minerais não opacos (óxidos, silicatos, carbonatos de metal) também são portadores.
</details>

---

### 5. Aplicação (cálculo) — `geologia-avancado-m09-q05` · oa01 · 15 pts
A análise modal automatizada de um minério de cobre dá:

| Mineral | Massa (%) | Cu no mineral (%) |
|---|---|---|
| Bornita (Cu₅FeS₄) | 1,00 | 63,3 (estequiométrico) |
| Calcopirita (CuFeS₂) | 1,00 | 34,6 (estequiométrico) |
| Malaquita (carbonato de Cu) | 0,20 | 57,5 (medido nesta amostra) |
| Cu em óxidos de Fe (limonita cuprífera) | — | contribui 0,020 % Cu ao total |

Calcule: (a) o teor de cobre do minério; (b) a partição do cobre entre os quatro portadores; (c) a fração do cobre em sulfetos flotáveis e a recuperação máxima teórica por flotação, supondo que a flotação recupera 95 % do cobre que está em sulfetos; (d) que proxy barata, medida em todos os furos, poderia sinalizar a fração de cobre que a flotação de sulfetos não alcança.

<details>
<summary>Ver resolução</summary>

Cobre aportado por cada mineral:
`Bornita: 1,00 × 0,633 = 0,633 %`
`Calcopirita: 1,00 × 0,346 = 0,346 %`
`Malaquita: 0,20 × 0,575 = 0,115 %`
`Óxidos de Fe: 0,020 %`
`Cu total = 0,633 + 0,346 + 0,115 + 0,020 = 1,114 % Cu`

**Partição:**
`Bornita: 0,633 / 1,114 = 56,8 %`
`Calcopirita: 0,346 / 1,114 = 31,1 %`
`Malaquita: 0,115 / 1,114 = 10,3 %`
`Óxidos de Fe: 0,020 / 1,114 = 1,8 %`

Cobre em sulfetos flotáveis (bornita + calcopirita) = `56,8 + 31,1 = 87,9 %` do cobre total.

Recuperação máxima teórica por flotação: `R_máx = 0,879 × 0,95 = 0,835 → 83,5 %`

**Interpretação:** como no exemplo da Aula 02, o teto de recuperação por flotação já está fixado pela partição, antes de qualquer discussão de liberação, reagente ou circuito. A malaquita (carbonato) e os óxidos de ferro (12,1 % do cobre total) são invisíveis à flotação de sulfetos em qualquer finura de moagem.

**(d)** Assim como a crisocola no exemplo da Aula 02, a malaquita é solúvel em ácido; a **razão entre cobre solúvel em ácido fraco e cobre total**, medida em todos os furos, é a proxy barata capaz de sinalizar, propagada ao modelo de blocos, onde a flotação sozinha deixa metal para trás.
</details>

---

### 6. Verdadeiro ou Falso (justifique) — `geologia-avancado-m09-q06` · oa01 · 10 pts
"A medida de liberação em seção polida bidimensional superestima a liberação real, porque o corte de uma partícula mista pode atravessar apenas uma das fases, produzindo um resultado indistinguível do corte de uma partícula genuinamente liberada."

<details>
<summary>Ver resposta</summary>

**Verdadeiro.**

É o viés estereológico da análise modal automatizada. O corte 2D de uma partícula liberada **nunca** aparece como mista — mas o corte de uma partícula mista **pode** atravessar só uma das fases e sair indistinguível de uma liberada. O viés é, portanto, de **mão única**: a seção polida superestima sistematicamente a liberação (e subestima o travamento) tridimensional. É uma propriedade do instrumento de medida, presente sempre que se usa seção 2D — não depende de erro do analista. Métodos de correção estereológica (King; Gay & Morrison, 2006) atenuam o viés, e a microtomografia de raios X o elimina, ambos a custo maior.
</details>

---

### 7. Múltipla escolha — `geologia-avancado-m09-q07` · oa02 · 10 pts
Um mineral tem grão médio de 40 µm, mas parte dele ocorre em **inclusões de apenas 5 µm** dentro de outro mineral. Moer o minério a um `P80` de 40 µm é suficiente para:

- a) Liberar todo o mineral, inclusive as inclusões de 5 µm
- b) Liberar a maior parte dos grãos de 40 µm, mas não as inclusões de 5 µm, que só se liberam se a partícula ficar menor que a própria inclusão
- c) Liberar apenas as inclusões, e não os grãos de 40 µm
- d) Não liberar nada, pois a moagem deve sempre ser mais grossa que o tamanho de grão

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A regra geral: para liberar um mineral é preciso moer a rocha até um tamanho de partícula igual ou menor que o tamanho de grão desse mineral. Os grãos de 40 µm liberam-se com um `P80` de 40 µm; as inclusões de 5 µm, não — elas só liberam se a partícula ficar menor que a própria inclusão, o que muitas vezes é economicamente inviável. "d" inverte a regra; "c" e "a" ignoram que os dois tamanhos de grão exigem finuras diferentes de moagem.
</details>

---

### 8. Dissertativa curta — `geologia-avancado-m09-q08` · oa02 · 10 pts
Explique a diferença entre **fratura não preferencial** (transgranular) e **descolamento** (liberação preferencial, intergranular), e explique por que assumir que um minério fratura por descolamento, quando na verdade fratura de forma não preferencial, leva a **superestimar** a liberação esperada a uma dada moagem.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada — três pontos:**

1. **Fratura não preferencial:** a trinca atravessa os grãos sem "enxergar" os contornos entre minerais — comportamento da maioria dos minérios silicáticos e sulfetados. A liberação só cresce com redução drástica de tamanho, obrigando à sobremoagem e gerando lamas.
2. **Descolamento:** a fratura segue os contornos de grão ou uma fase frágil/clivável (mica, borda de sulfeto, franja de alteração argilosa). Ocorre em parte dos minérios e libera com muito menos energia.
3. **O erro de modelagem:** se o analista assume descolamento onde na verdade há fratura não preferencial, ele projeta que a liberação sobe rapidamente com pouca moagem — quando, de fato, sobe devagar e exige moagem muito mais fina. O resultado é uma estimativa de liberação (e de recuperação) otimista a um dado `P80`, que o circuito real não entrega.

**Comentário:** este é um erro de escolha do modelador sobre o mecanismo de quebra — distinto do viés estereológico da medida em seção polida (Aula 02), que é uma propriedade do instrumento e vale sempre, independentemente da hipótese de fratura adotada.
</details>

---

### 9. Aplicação (cálculo) — `geologia-avancado-m09-q09` · oa02 · 10 pts
Mineral-alvo galena, grão médio 90 µm. A análise modal automatizada em quatro produtos de moagem dá o grau de liberação:

| `P80` do produto | Grau de liberação |
|---|---|
| 180 µm | 48 % |
| 125 µm | 68 % |
| 90 µm | 83 % |
| 53 µm | 93 % |

Estime a recuperação em cada `P80`, adotando `R = (grau de liberação × 0,95) + [(1 − grau de liberação) × 0,30]`, em que 0,95 é a recuperação das partículas liberadas e 0,30 a recuperação média das mistas. Identifique em que faixa de `P80` o ganho de recuperação por passo é maior, e comente por que os graus de liberação usados aqui são, eles próprios, um limite superior.

<details>
<summary>Ver resolução</summary>

`P80 180 µm: R = 0,48 × 0,95 + 0,52 × 0,30 = 0,456 + 0,156 = 0,612 → 61,2 %`
`P80 125 µm: R = 0,68 × 0,95 + 0,32 × 0,30 = 0,646 + 0,096 = 0,742 → 74,2 %`
`P80  90 µm: R = 0,83 × 0,95 + 0,17 × 0,30 = 0,7885 + 0,051 = 0,8395 → 84,0 %`
`P80  53 µm: R = 0,93 × 0,95 + 0,07 × 0,30 = 0,8835 + 0,021 = 0,9045 → 90,5 %`

Ganho por passo: `180→125: +13,0 pontos`; `125→90: +9,8 pontos`; `90→53: +6,5 pontos`. O maior ganho está no primeiro passo (180→125 µm); o retorno cai a cada redução adicional de tamanho, o mesmo padrão de achatamento da curva de liberação visto na Aula 03.

**Sobre o limite superior:** os graus de liberação desta tabela vêm de seções polidas 2D e carregam o viés estereológico — a medida superestima a liberação real. As recuperações calculadas aqui são, portanto, um teto otimista; a planta real, com liberação 3D verdadeira menor, tende a entregar recuperações abaixo destes valores.
</details>

---

## Gabarito resumido

| Questão | ID | Resposta |
|---|---|---|
| 1 | q01 | b |
| 2 | q02 | Falso (teor é proxy, recuperação é primária — invertido na afirmação) |
| 3 | q03 | Cu recuperado 84,48 t (C) e 55,68 t (D); receita US$ 760 320 e US$ 501 120; F/C ≈ 24,6; c/f ≈ 21,7; diferença ≈ 34 % |
| 4 | q04 | b |
| 5 | q05 | Cu total 1,114 %; partição 56,8/31,1/10,3/1,8 %; sulfetos 87,9 %; R_máx 83,5 %; proxy = razão de cobre solúvel em ácido |
| 6 | q06 | Verdadeiro (viés de mão única; seção 2D superestima liberação) |
| 7 | q07 | b |
| 8 | q08 | ver comentário (fratura não preferencial × descolamento; erro de modelagem superestima liberação) |
| 9 | q09 | R = 61,2 / 74,2 / 84,0 / 90,5 %; maior ganho no primeiro passo; valores são teto otimista (viés estereológico) |
