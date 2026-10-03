# Questionário parcial 2 — Módulo 26: Geologia isotópica aplicada

**Módulo:** [[26-geologia-isotopica-aplicada-modulo|Módulo 26 — Geologia isotópica aplicada]]
**Cobertura:** Aulas 04 e 05 — o sistema Sm-Nd (isócrona, notação εNd, idade-modelo T_DM) e os sistemas U-Pb e Pb-Pb (diagrama concórdia, discórdia, idade Pb-Pb, o zircão).
**Recorte:** os dois sistemas de interpretação mais densa do módulo. A parcial 2 testa se você sabe calcular uma idade isocrônica Sm-Nd e converter uma razão medida em εNd(t), distinguir idade-modelo de idade de cristalização, calcular uma idade concordante e uma idade Pb-Pb, e interpretar um padrão de discordância.
**Objetivos avaliados:** `geologia-avancado-m26-oa02` (sistemas Sm-Nd e U-Pb/Pb-Pb), `geologia-avancado-m26-oa03` (εNd e discordância U-Pb como traçadores)
**Pontuação total:** 100 pontos · o gabarito fica oculto; responda antes de abrir.

---

### 11. Múltipla escolha — `geologia-avancado-m26-q11` · oa02 · 8 pts

Por que o sistema Sm-Nd é considerado, de modo geral, mais robusto contra alteração secundária do que o sistema Rb-Sr?

- a) Porque o ¹⁴⁷Sm tem meia-vida muito mais curta que o ⁸⁷Rb, e sistemas de meia-vida curta são sempre menos sensíveis a alteração
- b) Porque Sm e Nd são terras-raras leves quimicamente muito parecidos entre si, o que faz a razão Sm/Nd de uma rocha variar pouco durante intemperismo, metamorfismo de baixo a médio grau e alteração hidrotermal — ao contrário de Rb e Sr, que reagem de forma bem diferente a fluidos aquosos
- c) Porque o Sm-Nd não depende de uma técnica de isócrona, dispensando amostras cogenéticas
- d) Porque o neodímio, ao contrário do estrôncio, é um gás nobre e não entra na estrutura cristalina dos minerais

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Sm e Nd têm raios iônicos e comportamento geoquímico muito semelhantes, ambos elementos incompatíveis de incompatibilidade moderada — por isso a razão Sm/Nd de uma rocha resiste bem a processos que perturbariam a razão Rb/Sr (o rubídio, alcalino grande e muito incompatível, e o estrôncio, alcalino-terroso, reagem de forma bem diferente a fluidos aquosos). "a" é falso: a meia-vida do ¹⁴⁷Sm (106,25 Ga) é cerca de **duas vezes mais longa**, não mais curta, que a do ⁸⁷Rb (49,61 Ga) — e meia-vida não determina robustez química a alteração. "c" é falso: o Sm-Nd usa a mesma técnica de isócrona do Rb-Sr, com amostras cogenéticas. "d" é falso e absurdo quimicamente: Nd é um lantanídeo, não um gás nobre.
</details>

---

### 12. Aplicação / cálculo — `geologia-avancado-m26-q12` · oa02 · 14 pts

Três frações minerais de uma rocha (dados hipotéticos, diferentes do exemplo da aula) produziram uma isócrona Sm-Nd com inclinação 0,0009000 e intercepto (¹⁴³Nd/¹⁴⁴Nd)_inicial = 0,511950. Usando λ = 6,524 × 10⁻¹² ano⁻¹ (IUPAC-IUGS, 2020) e os valores de CHUR de DePaolo & Wasserburg (1976) — (¹⁴³Nd/¹⁴⁴Nd)_CHUR,0 = 0,512638 e (¹⁴⁷Sm/¹⁴⁴Nd)_CHUR = 0,1967 —, calcule (a) a idade da rocha e (b) o εNd(t) no momento da cristalização.

<details>
<summary>Ver resposta</summary>

**(a) Idade.** e^(λt) − 1 = 0,0009000 ⟹ λt = ln(1,0009) ≈ 0,00089960

t = 0,00089960/6,524×10⁻¹² ≈ 1,3787×10⁸ anos ≈ **137,9 milhões de anos**

**(b) εNd(t).** Primeiro, a razão do CHUR no momento t:

(¹⁴³Nd/¹⁴⁴Nd)_CHUR,t = 0,512638 − 0,1967 × 0,0009000 = 0,512638 − 0,00017703 ≈ 0,512461

Depois, εNd(t) usando o intercepto da isócrona (razão inicial da rocha, 0,511950) e a razão do CHUR no mesmo instante (0,512461):

εNd(t) = [(0,511950/0,512461) − 1] × 10⁴ ≈ [0,999003 − 1] × 10⁴ ≈ **−10,0**

Um εNd(t) negativo indica fonte com razão Sm/Nd historicamente mais baixa que a condrítica — tipicamente crosta continental antiga, ou fonte mantélica contaminada — em vez de manto empobrecido não contaminado, que produziria εNd positivo.
</details>

---

### 13. Verdadeiro ou Falso (justifique) — `geologia-avancado-m26-q13` · oa02 · 8 pts

"A idade-modelo T_DM de uma rocha ígnea é sempre igual à sua idade isocrônica de cristalização, porque as duas medem exatamente o mesmo evento geológico."

<details>
<summary>Ver resposta</summary>

**Falso.**

As duas são conceitualmente distintas. A idade isocrônica registra um evento específico de cristalização (ou de fechamento do sistema), obtida ajustando uma reta a um conjunto de amostras cogenéticas. A idade-modelo T_DM estima **quando o material que forma a rocha se separou quimicamente do manto** (um evento de extração de magma, ou de diferenciação crustal) — projetando a evolução da razão ¹⁴³Nd/¹⁴⁴Nd da amostra para trás no tempo até cruzar a curva de evolução do manto empobrecido. Para uma rocha ígnea recém-extraída diretamente do manto, as duas idades podem coincidir aproximadamente; mas para uma rocha formada por refusão de crosta continental antiga (material que já havia se separado do manto muito antes), T_DM registra a idade antiga de extração crustal, enquanto a idade isocrônica registra o evento de cristalização recente — podem ser muito diferentes. É por isso que T_DM continua interpretável até em rochas sedimentares, que não têm "idade de cristalização" no sentido ígneo.
</details>

---

### 14. Dissertativa curta — `geologia-avancado-m26-q14` · oa03 · 10 pts

Explique o que a notação εNd representa, por que o CHUR foi escolhido como referência, e o que significa um valor positivo versus um valor negativo.

<details>
<summary>Ver resposta</summary>

Uma boa resposta cobre:

- εNd expressa o desvio da razão ¹⁴³Nd/¹⁴⁴Nd de uma amostra em relação ao CHUR (reservatório condrítico uniforme), em partes por 10.000 — uma escala adotada porque as diferenças interessantes entre reservatórios aparecem só na quarta ou quinta casa decimal da razão bruta, difícil de ler e comparar diretamente.
- O CHUR, proposto por DePaolo & Wasserburg (1976), representa a composição média do material rochoso do Sistema Solar, estimada a partir de meteoritos condríticos — um valor de referência único e estável contra o qual comparar qualquer amostra terrestre.
- εNd = 0 significa que a amostra evoluiu desde a formação da Terra com a mesma razão Sm/Nd do material condrítico médio, sem nunca ter passado por um evento de fracionamento de terras-raras.
- εNd **positivo** indica fonte com Sm/Nd historicamente mais alta que a condrítica — o manto empobrecido (Nd é mais incompatível que Sm, logo extração de magma ao longo do tempo eleva a razão Sm/Nd do manto residual). εNd **negativo** indica fonte com Sm/Nd historicamente mais baixa — tipicamente crosta continental antiga, que concentra Nd incompatível durante sua formação por fusão parcial do manto.
</details>

---

### 15. Múltipla escolha — `geologia-avancado-m26-q15` · oa02 · 8 pts

Por que o sistema U-Pb consegue se "autotestar" de um jeito que nenhum sistema isocrônico isolado (Rb-Sr ou Sm-Nd) consegue por si só?

- a) Porque o zircão é um mineral mais abundante que a biotita ou o plagioclásio
- b) Porque dois decaimentos independentes (²³⁸U→²⁰⁶Pb e ²³⁵U→²⁰⁷Pb) ocorrem simultaneamente no mesmo mineral desde a cristalização, produzindo dois relógios que devem concordar; se o ponto medido cai sobre a curva concórdia, os dois relógios independentes confirmam a mesma idade
- c) Porque a constante de decaimento do urânio é medida com mais precisão do que qualquer outra constante de decaimento em geocronologia
- d) Porque a técnica da isócrona não é necessária no sistema U-Pb, eliminando a principal fonte de erro dos outros sistemas

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A redundância interna do U-Pb vem de ter dois decaimentos radioativos independentes operando no mesmo mineral a partir do mesmo instante de cristalização: um grão que se comportou como sistema fechado produz uma idade por ²⁰⁶Pb*/²³⁸U e outra por ²⁰⁷Pb*/²³⁵U que devem coincidir. É essa concordância mútua, e não a confiança em um único par pai-filho, que dá ao U-Pb concordante um grau de confiabilidade que nenhum sistema isocrônico isolado da Aula 03 ou 04 oferece por si só. "a" é irrelevante ao autoteste. "c" é uma afirmação sobre precisão, não sobre a estrutura de dupla verificação. "d" é falso — o sistema U-Pb tem, ele mesmo, uma técnica análoga (a discórdia), que não é a mesma coisa que dispensar verificação.
</details>

---

### 16. Aplicação / cálculo — `geologia-avancado-m26-q16` · oa02 · 14 pts

Um grão de zircão analisado por ID-TIMS mostrou uma razão ²⁰⁶Pb*/²³⁸U = 0,4000 (valor hipotético, diferente do exemplo da aula), com análise concordante. Usando λ238 = 1,55125 × 10⁻¹⁰ ano⁻¹:

(a) Calcule a idade concordante. (b) Qual razão ²⁰⁷Pb*/²³⁵U o segundo relógio (λ235 = 9,8485 × 10⁻¹⁰ ano⁻¹) deveria prever para essa mesma idade, confirmando a concordância?

<details>
<summary>Ver resposta</summary>

**(a)** t = (1/λ238)·ln(1 + 0,4000) = ln(1,4000)/1,55125×10⁻¹⁰

ln(1,4000) ≈ 0,336472 ⟹ t ≈ 0,336472/1,55125×10⁻¹⁰ ≈ 2,1697×10⁹ anos ≈ **2169,7 milhões de anos (≈2,17 Ga)**

**(b)** Usando t = 2,1697×10⁹ anos na equação do segundo relógio:

²⁰⁷Pb*/²³⁵U = e^(λ235·t) − 1

λ235·t = 9,8485×10⁻¹⁰ × 2,1697×10⁹ ≈ 2,1368

e^2,1368 − 1 ≈ **7,47**

Uma razão ²⁰⁷Pb*/²³⁵U medida próxima de 7,47 confirmaria a mesma idade pelos dois relógios independentes, classificando a análise como concordante — a mesma lógica do Exemplo trabalhado 1 da Aula 05.
</details>

---

### 17. Verdadeiro ou Falso (justifique) — `geologia-avancado-m26-q17` · oa02 · 8 pts

"A idade Pb-Pb, calculada a partir da razão ²⁰⁷Pb*/²⁰⁶Pb*, precisa de uma medida direta do urânio presente na amostra, assim como a idade concordante convencional precisa."

<details>
<summary>Ver resposta</summary>

**Falso.**

A vantagem estrutural da idade Pb-Pb é exatamente dispensar qualquer medida de urânio. A equação ²⁰⁷Pb*/²⁰⁶Pb* = (1/137,818)·(e^(λ235t)−1)/(e^(λ238t)−1) usa apenas a razão entre os dois isótopos radiogênicos de chumbo entre si e o valor de referência ²³⁸U/²³⁵U = 137,818 (Hiess et al., 2012) — nenhuma medida de urânio entra na conta. Isso torna a idade Pb-Pb útil justamente para minerais ou minérios que perderam urânio de forma significativa, mas preservaram a razão entre os dois chumbos radiogênicos acumulados antes da perda, incluindo aplicações a chumbo comum de depósitos minerais (modelo de Holmes-Houtermans) sem que o urânio original precise ser conhecido.
</details>

---

### 18. Múltipla escolha — `geologia-avancado-m26-q18` · oa03 · 8 pts

Numa reta de discórdia ajustada a vários pontos discordantes de uma mesma população de zircões, o que representam o intercepto superior e o intercepto inferior com a curva concórdia?

- a) O intercepto superior é sempre zero, e o intercepto inferior dá a idade de cristalização
- b) O intercepto superior corresponde à idade de cristalização original do zircão; o intercepto inferior corresponde à idade do evento que causou a perda de chumbo (podendo ser próximo de zero, se a perda foi recente e sem evento geológico distinto)
- c) Os dois interceptos são estatisticamente equivalentes e podem ser trocados sem alterar a interpretação geológica
- d) O intercepto superior dá a idade do evento metamórfico mais recente, e o inferior dá a idade de cristalização, invertendo a leitura do K-Ar

<details>
<summary>Ver resposta</summary>

**Resposta: b**

O intercepto superior é a idade de cristalização original (t₁, evento ígneo ou metamórfico que formou o mineral); o intercepto inferior é a idade do evento posterior que causou a perda de chumbo (t₂), podendo ser próximo de zero quando a perda foi recente sem um evento geológico distinto associável (por exemplo, perda ligada a intemperismo ou preparação de amostra). "a" está errado: o intercepto superior não é "sempre zero" — é justamente o oposto do inferior próximo de zero em muitos casos práticos. "c" ignora que os dois interceptos representam eventos geológicos distintos e não intercambiáveis. "d" inverte a atribuição.
</details>

---

### 19. Dissertativa — `geologia-avancado-m26-q19` · oa03 · 10 pts

Explique as três propriedades do zircão que o tornam o mineral preferido do sistema U-Pb, e diga por que a terceira delas conecta esta aula ao Módulo 27 deste curso.

<details>
<summary>Ver resposta</summary>

Uma boa resposta cobre as três propriedades da Aula 05:

1. **Incorpora urânio prontamente, mas rejeita chumbo** — o urânio substitui o zircônio na estrutura cristalina em quantidades apreciáveis, enquanto o chumbo, com raio iônico e valência incompatíveis com o sítio do zircônio, é fortemente excluído; o chumbo comum inicial é, na prática, próximo de zero (a mesma lógica de "filho inicial desprezível" do argônio na Aula 02, mas por exclusão estrutural, não volatilidade).
2. **É quimicamente e mecanicamente muito resistente** — resiste a intemperismo, transporte sedimentar e metamorfismo de grau baixo a médio, o que permite que zircões detríticos preservem a idade de cristalização de sua rocha-fonte mesmo em análise de proveniência sedimentar.
3. **Cresce em zonas, registrando eventos sucessivos** — muitos zircões crescem em zonamento composicional (núcleo ígneo original sobrecrescido por bordas metamórficas mais jovens), datável separadamente por SIMS ou LA-ICP-MS.

A terceira propriedade conecta com o Módulo 27: datar núcleo e borda separadamente no mesmo grão é o tema central da **petrocronologia**, que atribui significado petrogenético a essas idades ligando-as a texturas e microdomínios composicionais.
</details>

---

### 20. Integração (Aulas 04–05) — `geologia-avancado-m26-q20` · oa02+oa03 · 12 pts

O método Pb-Pb (Aula 05) e a idade-modelo Sm-Nd T_DM (Aula 04) têm algo em comum: os dois dispensam uma medida direta de um dos elementos originalmente envolvidos no par pai-filho. Compare os dois: (a) o que cada um dispensa medir e o que assume no lugar disso; (b) por que nenhum dos dois é uma "idade de cristalização" no mesmo sentido que uma isócrona.

<details>
<summary>Ver resposta</summary>

**(a)** A idade Pb-Pb dispensa qualquer medida de **urânio**: usa só a razão ²⁰⁷Pb*/²⁰⁶Pb* entre os dois isótopos radiogênicos de chumbo, assumindo o valor de referência ²³⁸U/²³⁵U = 137,818 no lugar de uma medida direta na amostra. A idade-modelo T_DM dispensa a necessidade de **múltiplas frações cogenéticas** para construir uma isócrona: usa uma única amostra de rocha total, assumindo, no lugar disso, um modelo de evolução do manto empobrecido (valores de referência (¹⁴³Nd/¹⁴⁴Nd)_DM e (¹⁴⁷Sm/¹⁴⁴Nd)_DM de hoje, projetados para trás por uma curva de evolução, tipicamente a de DePaolo, 1981).

**(b)** Nenhum dos dois registra um evento específico de cristalização da forma que uma isócrona registra. A idade Pb-Pb, quando aplicada a chumbo comum (por exemplo, galena de um depósito de sulfetos), pode registrar a composição herdada de uma fonte crustal ou mantélica sem corresponder a nenhuma cristalização mineral específica. A idade-modelo T_DM registra quando o **precursor químico** do material se separou do manto (um evento de extração de magma ou diferenciação crustal), não necessariamente quando a rocha que se tem na mão cristalizou — por isso T_DM permanece interpretável até para rochas sedimentares, sem "idade de cristalização" própria, como estimativa da idade média de extração crustal do material-fonte.
</details>

---

**Total: 100 pontos.**
