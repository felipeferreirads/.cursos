# Questionário final cumulativo — Módulo 23: Introdução à modelagem numérica geodinâmica

**Módulo:** [[23-modelagem-numerica-geodinamica-modulo|Módulo 23 — Introdução à modelagem numérica geodinâmica]]
**Cobertura:** Módulo inteiro — Aulas 01 a 09. Peso maior em aplicação e em conexões entre aulas, incluindo pelo menos uma questão que cruza os três blocos (01-02 / 03-06 / 07-09).
**Objetivos avaliados:** `geologia-avancado-m23-oa01`, `geologia-avancado-m23-oa02`, `geologia-avancado-m23-oa03`, `geologia-avancado-m23-oa04` (todos, de forma integrada)
**Pontuação total:** 100 pontos · o gabarito fica oculto; responda antes de abrir.

---

### 1. Aplicação / leitura de código — `geologia-avancado-m23-q32` · oa01 · 6 pts

```python
import numpy as np
z = np.linspace(0, 10, 6)   # profundidade, km
T = 5 + 10 * z               # geoterma linear ilustrativa
print(T)
```

Qual é o array `T` resultante? Confira à mão o valor em z = 6 km.

<details>
<summary>Ver resposta</summary>

`z = np.linspace(0, 10, 6)` gera 6 pontos igualmente espaçados de 0 a 10: `[0, 2, 4, 6, 8, 10]`.

`T = 5 + 10*z` = `[5, 25, 45, 65, 85, 105]`.

Conferindo em z=6: T = 5 + 10×6 = 5 + 60 = **65** — bate com o quarto elemento do array (índice 3).
</details>

---

### 2. Múltipla escolha — `geologia-avancado-m23-q33` · oa02 · 7 pts

Considere dN/dt = −λN (decaimento radioativo) e ∂T/∂t = κ∂²T/∂z² (difusão de calor). Assinale a alternativa correta:

- a) Ambas são EDPs, porque λ e κ têm o mesmo papel matemático nas duas equações
- b) A primeira é uma EDO (uma única variável independente, o tempo); a segunda é uma EDP (duas variáveis independentes, tempo e espaço). λ e κ não são a mesma grandeza — nem em significado físico, nem em unidade (λ: 1/tempo; κ: área/tempo)
- c) A primeira é uma EDP e a segunda uma EDO, porque o decaimento depende implicitamente da posição da amostra medida
- d) λ e κ são interconversíveis por um fator de escala universal, já que governam fenômenos de decaimento/espalhamento

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A distinção EDO/EDP é pelo **número de variáveis independentes**: uma só (o decaimento, no tempo) versus duas ou mais simultâneas (a difusão, tempo e espaço). λ e κ, apesar de aparecerem em posições sintaticamente parecidas ("a constante que multiplica..."), governam fenômenos matemáticos distintos e têm unidades diferentes — confundi-las é o erro mais perigoso identificado na auditoria científica deste módulo.
</details>

---

### 3. Aplicação — `geologia-avancado-m23-q34` · oa02 · 7 pts

Um código de modelagem de manto usa uma viscosidade η que varia por três ordens de grandeza entre o núcleo de uma pluma quente e o manto circundante mais frio. Qual forma do termo viscoso da equação de Stokes deve ser implementada, e por quê?

<details>
<summary>Ver resposta</summary>

A forma **completa**, div[η(∇**v** + (∇**v**)ᵀ)], deve ser implementada — não a forma simplificada η∇²**v**. Esta última só é matematicamente equivalente à completa quando η é **constante** (e o fluxo é incompressível); com η variando por ordens de grandeza, como no cenário descrito, usar a forma simplificada produziria um resultado fisicamente incorreto. É exatamente o caso que o módulo inteiro existe para tratar: viscosidade que varia por ordens de grandeza é a regra, não a exceção, em geodinâmica.
</details>

---

### 4. Verdadeiro ou Falso (justifique) — `geologia-avancado-m23-q35` · oa02 · 6 pts

"Numa malha colocalizada, a discretização por diferença central do gradiente de pressão usa o nó imediatamente vizinho de cada lado, o que permite detectar e penalizar qualquer oscilação de pressão de nó em nó."

<details>
<summary>Ver resposta</summary>

**Falso.**

A diferença central do gradiente num nó *i* usa os nós **alternados** (i+1 e i−1) — ela **pula** o vizinho imediato. Um campo de pressão que oscila de nó em nó (alto, baixo, alto, baixo) tem, nos dois nós alternados usados pela fórmula, exatamente o mesmo valor, de modo que a diferença dá zero: a oscilação **não** produz gradiente algum no cálculo e, portanto, **não** é penalizada — o solver a aceita como solução legítima, o padrão espúrio em xadrez. É justamente esse defeito que a malha escalonada resolve.
</details>

---

### 5. Aplicação / cálculo — `geologia-avancado-m23-q36` · oa02+oa03 · 9 pts

Para uma malha 1D com κ = 1 × 10⁻⁶ m²/s (valor típico de rocha crustal, visto nas Aulas 05 e 07) e Δz = 1 km = 1.000 m, calcule o passo de tempo máximo Δt permitido pela condição de estabilidade do esquema explícito. Expresse o resultado em anos.

<details>
<summary>Ver resposta</summary>

A condição de estabilidade exige r = κΔt/Δz² ≤ 1/2, logo Δt_max = 0,5 × Δz² / κ.

Δz² = (1.000)² = 1 × 10⁶ m². Δt_max = 0,5 × 1×10⁶ / 1×10⁻⁶ = 0,5 × 10¹² = **5 × 10¹¹ s**.

Convertendo para anos (1 ano ≈ 3,15576 × 10⁷ s): Δt_max ≈ 5×10¹¹ / 3,15576×10⁷ ≈ **1,58 × 10⁴ anos** (≈ 15.800 anos).

Esse número é pequeno comparado às escalas de tempo geodinâmicas de milhões de anos que o módulo trata — um passo de tempo explícito de ~16 mil anos exigiria dezenas de milhares de passos para simular apenas 1 milhão de anos de evolução geológica, o que ilustra na prática por que o esquema implícito (Aula 06), sem essa restrição, é frequentemente preferido em modelos de longa duração, apesar do custo maior por passo.
</details>

---

### 6. Verdadeiro ou Falso (justifique) — `geologia-avancado-m23-q37` · oa02 · 7 pts

Um aluno programa o esquema explícito e observa, após alguns passos, valores de temperatura oscilando violentamente, alguns deles negativos. Ele conclui: "o esquema está instável porque os valores ficaram negativos." A justificativa dada por ele está correta?

<details>
<summary>Ver resposta</summary>

**A conclusão (instabilidade) está correta, mas a justificativa (valores negativos) não é o critério válido.**

O critério correto é a violação do **princípio do máximo**: a solução da equação da difusão sem produção deve permanecer, em qualquer instante, dentro do intervalo entre o menor e o maior valor presentes na condição inicial e nas condições de contorno. Um valor negativo em Celsius não é, por si só, impossível (uma geoterma sob gelo pode começar negativa); o que denuncia a instabilidade é o valor ter **escapado** desse intervalo, qualquer que seja o sinal. Se o aluno tivesse condições iniciais e de contorno já negativas, valores negativos dentro do intervalo permitido não indicariam problema nenhum — é a violação do intervalo, e não o sinal, que é o critério.
</details>

---

### 7. Múltipla escolha — `geologia-avancado-m23-q38` · oa04 · 6 pts

A reologia dúctil da crosta continental superior é frequentemente aproximada pela lei de fluência de qual mineral, e a do manto superior por qual outro?

- a) Ambas por olivina — o mesmo mineral domina crosta e manto
- b) Crosta: quartzo (mais fraco, flui em temperaturas relativamente baixas); manto: olivina (mais resistente, exige temperaturas mais altas)
- c) Crosta: feldspato; manto: piroxênio
- d) Crosta: mica; manto: granada

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A crosta continental superior tem seu comportamento dúctil frequentemente aproximado pela lei de fluência do **quartzo**; a crosta inferior e o manto superior são governados por leis de fluência de minerais máficos e do **olivino**, respectivamente — muito mais resistentes, exigindo temperaturas mais altas para fluir na mesma taxa. Essa diferença, combinada com a geoterma, produz a estrutura de resistência em camadas ("envelope de resistência") da litosfera continental.
</details>

---

### 8. Dissertativa curta — `geologia-avancado-m23-q39` · oa03+oa04 · 9 pts

Explique por que um orógeno colisional tende a **aquecer antes de esfriar** após o espessamento crustal, e como esse aquecimento retroalimenta a reologia da crosta profunda (conectando as Aulas 08 e 09).

<details>
<summary>Ver resposta</summary>

Uma boa resposta cobre: o espessamento tectônico (empilhamento de nappes, duplicação de crosta) é **rápido demais** para a condução de calor acompanhar — a crosta espessada carrega momentaneamente a distribuição de temperatura que tinha antes do espessamento, agora concentrada num volume menor de área superficial relativa, com a camada radiogênica também duplicada em espessura. O resultado é que a crosta espessada tende a **aquecer** nas primeiras dezenas de milhões de anos, antes de relaxar de volta a um perfil mais estável. Esse aquecimento retroalimenta a reologia porque, como a Aula 08 mostrou, a viscosidade efetiva depende exponencialmente da temperatura via o fator de Arrhenius — o mesmo aquecimento pós-colisional **enfraquece** progressivamente a crosta profunda, facilitando o fluxo dúctil lateral (extrusão de crosta média a inferior aquecida) característico de orógenos colisionais maduros. A cadeia de causa é: espessamento gera calor → calor reduz viscosidade → viscosidade reduzida facilita mais deformação — uma retroalimentação que une os dois módulos (calor e reologia) numa única história física.
</details>

---

### 9. Múltipla escolha — `geologia-avancado-m23-q40` · oa04 · 7 pts

Uma placa oceânica antiga tem uma longa zona de subducção ativa numa de suas bordas, mas não é adjacente a nenhuma cordilheira meso-oceânica de topografia significativa. Qual força tende a dominar o balanço de forças dessa placa?

- a) Ridge-push, porque é sempre a força dominante em qualquer placa
- b) Slab-pull, tipicamente cerca de uma ordem de grandeza maior (~10¹³ N/m) que ridge-push (~10¹² N/m), e o único dos dois motores presentes de forma significativa neste cenário
- c) Nenhuma das duas — sem cordilheira, a placa não se move
- d) As duas forças se cancelam exatamente

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Com uma zona de subducção ativa e sem cordilheira relevante, o **slab-pull** é o motor presente e, além disso, tipicamente o mais forte dos dois em ordem de grandeza (~10¹³ N/m contra ~10¹² N/m do ridge-push). "a" inverte a hierarquia geral. "c" ignora que o slab-pull sozinho já é suficiente para mover uma placa. "d" não tem base nas estimativas de ordem de grandeza discutidas na Aula 09.
</details>

---

### 10. Aplicação / cálculo — `geologia-avancado-m23-q41` · oa04 · 8 pts

Usando τ = 62,8 Ma (mesmo valor de referência da Aula 09), calcule a fração de subsidência térmica atingida em t = τ = 62,8 Ma. Que propriedade geral do decaimento exponencial esse resultado ilustra?

<details>
<summary>Ver resposta</summary>

Em t = τ: fração = 1 − e^(−τ/τ) = 1 − e^(−1) ≈ 1 − 0,3679 ≈ **0,632** (63,2%).

Esse resultado ilustra a propriedade geral de qualquer decaimento (ou relaxamento) exponencial: em um tempo igual à **constante de tempo característica** τ, aproximadamente **63%** da variação total já ocorreu — é a mesma propriedade que aparece no resfriamento de semi-espaço da Aula 07 e em qualquer processo governado por uma forma e^(−t/τ), inclusive fora da geodinâmica (circuitos RC, decaimento populacional, etc.).
</details>

---

### 11. Múltipla escolha — `geologia-avancado-m23-q42` · oa03 · 6 pts

As relações dq_z/dz = A(z) (com z orientado para baixo e q_z o fluxo de Fourier nessa direção) e dq/dz = −A(z) (com q o fluxo ascendente, positivo por convenção) são:

- a) contraditórias — só uma das duas pode estar correta
- b) duas expressões da mesma física, diferindo apenas pela convenção de sinal do eixo/fluxo adotada
- c) aplicáveis a fenômenos físicos diferentes — uma à condução, outra à advecção
- d) válidas apenas em regime transiente, nunca em regime estável

<details>
<summary>Ver resposta</summary>

**Resposta: b**

As duas relações descrevem exatamente o mesmo balanço físico — o fluxo de calor acumulando a produção radiogênica acima de cada nível —, apenas expressas sob convenções de sinal diferentes para a orientação do eixo z e do fluxo. Escolher uma convenção sem declará-la é uma fonte comum de erro de sinal em problemas de aplicação; a Aula 07 é explícita em fixar qual convenção usa antes de aplicar a fórmula.
</details>

---

### 12. Integração — cruza os três blocos (Aulas 01-02, 03-06, 07-09) — `geologia-avancado-m23-q43` · oa01+oa02+oa04 · 14 pts

Um aluno constrói, com `np.meshgrid` (Aula 01), uma malha espacial para o esquema explícito da equação do calor (Aula 06) e decide **refinar** a malha, reduzindo Δz pela metade, mantendo Δt fixo.

**(a)** O que acontece com r = κΔt/Δz², e qual a consequência prática para a estabilidade do esquema?

**(b)** Suponha que esse refinamento produza um campo de temperatura mais preciso, usado em seguida para calcular a viscosidade efetiva por fluência por deslocamento (Aula 08). Por que um pequeno ganho de precisão térmica pode ter um efeito desproporcional sobre a viscosidade calculada?

<details>
<summary>Ver resposta</summary>

**(a)** Reduzindo Δz pela metade sem alterar Δt, Δz² cai por um fator de 4 — e como r = κΔt/Δz² tem Δz² no denominador, **r quadruplica**. Se o r original já estivesse próximo do limite de estabilidade (r ≤ 1/2), esse refinamento pode empurrar o esquema para além do limite, tornando-o **instável** — um erro comum na prática: refinar a malha espacial sem reduzir Δt proporcionalmente (por um fator de 4, não de 2) para compensar.

**(b)** Porque a viscosidade efetiva depende **exponencialmente** da temperatura, via o fator de Arrhenius exp(Q/RT) (Aula 08) — o próprio exemplo trabalhado daquela aula mostrou que uma diferença de apenas 50 K produz uma razão de viscosidade de ≈22× (pouco mais de uma ordem de grandeza). Um refinamento numérico que melhora a precisão do campo térmico calculado nas Aulas 01/02/06 tem, portanto, um efeito **amplificado**, não proporcional, sobre qualquer grandeza reológica calculada a partir dele — a ferramenta numérica (malha, esquema, estabilidade) e a física reológica não são etapas independentes: a qualidade da primeira se propaga, multiplicada exponencialmente, para a segunda. É exatamente esse encadeamento — de Python vetorizado a discretização estável a reologia sensível — que percorre o módulo inteiro.
</details>

---

### 13. Dissertativa — síntese do módulo — `geologia-avancado-m23-q44` · oa01+oa02+oa03+oa04 · 8 pts

Descreva, em linhas gerais, o fio condutor do Módulo 23, da Aula 01 à Aula 09: como cada peça (Python/NumPy, EDO/EDP e diferenças finitas, equações de Stokes e do calor, malhas, esquemas numéricos, reologia) se encaixa para permitir um modelo geodinâmico quantitativo completo de extensão ou colisão continental.

<details>
<summary>Ver resposta</summary>

Uma boa resposta identifica a cadeia: Python/NumPy/Matplotlib (Aula 01) é a **ferramenta** que sustenta todo o resto; EDO versus EDP e diferenças finitas (Aula 02) são a **linguagem matemática** comum usada para discretizar qualquer equação do módulo; a equação da continuidade e a de Stokes (Aula 03) formulam **o que** governa o movimento do meio contínuo; malhas, malha escalonada e as descrições lagrangiana/euleriana (Aula 04) decidem **como** representar esse contínuo computacionalmente; a lei de Fourier e a equação de conservação de calor (Aula 05) formulam a física térmica; os esquemas explícito e implícito (Aula 06) resolvem essa física **numericamente**, com a condição de estabilidade como restrição central; a litosfera oceânica e continental (Aula 07) aplicam essa solução a geotermas reais, com controles físicos distintos (idade versus produção radiogênica); a reologia (Aula 08) traduz a temperatura calculada em viscosidade, via a lei de Arrhenius, com sensibilidade exponencial; e a extensão/colisão continental (Aula 09) integra tudo — calor, reologia e forças de placa — na análise quantitativa de cenários tectônicos completos. O fio condutor: cada aula entrega um ingrediente, físico ou numérico, que a aula seguinte consome diretamente, culminando numa capacidade de modelagem que nenhuma aula isolada entregaria sozinha.
</details>

---

**Total: 100 pontos.**
