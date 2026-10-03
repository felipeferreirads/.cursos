# Questionário parcial 2 — Módulo 23: Introdução à modelagem numérica geodinâmica

**Módulo:** [[23-modelagem-numerica-geodinamica-modulo|Módulo 23 — Introdução à modelagem numérica geodinâmica]]
**Cobertura:** Aulas 03 a 06 — mecânica do contínuo (continuidade e Stokes), malhas e descrições lagrangiana/euleriana, lei de Fourier e conservação de calor, e a solução numérica da equação do calor (esquemas explícito e implícito).
**Recorte:** as duas EDPs centrais do módulo — movimento (Stokes) e calor — junto com as escolhas de representação numérica (malha, descrição) e a primeira solução numérica completa do módulo (FTCS/BTCS).
**Objetivos avaliados:** `geologia-avancado-m23-oa02` (integral — a03, a04, a06), `geologia-avancado-m23-oa03` (início — a05)
**Pontuação total:** 100 pontos · o gabarito fica oculto; responda antes de abrir.

---

### 1. Múltipla escolha — `geologia-avancado-m23-q09` · oa02 · 8 pts

A forma simplificada do termo viscoso de Stokes, η∇²**v**, pode ser usada com segurança em:

- a) qualquer modelo de manto, porque a viscosidade do manto é sempre aproximadamente constante
- b) apenas quando a viscosidade η é constante no domínio (e o fluxo é incompressível); um modelo em que η varia por ordens de grandeza — o caso típico em geodinâmica — exige a forma completa, div[η(∇**v** + (∇**v**)ᵀ)]
- c) apenas em modelos tridimensionais, nunca em modelos 2D
- d) nunca — a forma simplificada está sempre incorreta, mesmo com viscosidade constante

<details>
<summary>Ver resposta</summary>

**Resposta: b**

O tensor simétrico completo dentro do divergente, (∇**v** + (∇**v**)ᵀ), só se reduz à forma simplificada η∇²**v** no caso particular em que η é **constante** e o fluxo é incompressível. Em geodinâmica, η varia no espaço por ordens de grandeza junto com a temperatura (como a Aula 08 detalha) — é justamente para mostrar isso que o módulo existe. Usar a forma simplificada num modelo de viscosidade variável é uma das fontes clássicas de implementação errada da equação de Stokes. "a" está errada porque a premissa (viscosidade aproximadamente constante no manto) é falsa. "c" e "d" não têm base: a restrição é sobre a variabilidade de η, não sobre a dimensão do modelo, e a forma simplificada é correta quando η de fato é constante.
</details>

---

### 2. Verdadeiro ou Falso (justifique) — `geologia-avancado-m23-q10` · oa02 · 8 pts

"O campo de velocidade vx = x, vz = −z do exemplo trabalhado da Aula 03 representa um cisalhamento simples, o mesmo regime cinemático associado a uma zona de falha transcorrente."

<details>
<summary>Ver resposta</summary>

**Falso.**

O campo vx = x, vz = −z é um **cisalhamento puro** (*pure shear*): deformação coaxial, em que o material se estica em x na mesma taxa em que se comprime em z, sem nenhuma componente rotacional. Cisalhamento **simples** é um regime distinto — deformação não coaxial, com rotação, tipicamente associada a zonas de cisalhamento transcorrente. A Aula 03 é explícita em não nomear os dois juntos: são regimes contrastados na geologia estrutural, e confundi-los é um erro comum de vocabulário.
</details>

---

### 3. Aplicação / leitura de código — `geologia-avancado-m23-q11` · oa02 · 9 pts

No exemplo trabalhado da Aula 03, `dvx_dx = np.gradient(vx, x, axis=1)` é usado para aproximar ∂vx/∂x sobre uma malha 5×5. Nas duas **bordas** do eixo x (primeira e última coluna), `np.gradient` usa diferença central ou diferença de um lado só? Qual a ordem de precisão nessas bordas, por padrão?

<details>
<summary>Ver resposta</summary>

Nas bordas, `np.gradient` usa **diferença de um lado só** (progressiva na primeira borda, regressiva na última) — não a diferença central, que exige um vizinho de cada lado e por isso não pode ser aplicada onde falta um deles. Por padrão (`edge_order=1`), essa diferença de um lado só é de **primeira** ordem de precisão, menos precisa que a diferença central de segunda ordem usada no interior da malha. No exemplo específico da aula, isso não produz erro visível porque vx e vz são funções lineares (e uma diferença de primeira ordem também é exata para uma função linear) — mas, para um campo não linear, as bordas seriam a parte menos precisa do resultado, razão pela qual, num modelo real, é sempre nelas que mora a condição de contorno, não uma derivada estimada de improviso.
</details>

---

### 4. Dissertativa curta — `geologia-avancado-m23-q12` · oa02 · 8 pts

Explique o mecanismo pelo qual uma malha **colocalizada** (pressão e velocidade no mesmo nó) permite que um padrão de pressão espúrio em xadrez passe despercebido, e por que a malha **escalonada** resolve esse problema.

<details>
<summary>Ver resposta</summary>

Uma boa resposta cobre: numa malha colocalizada, a diferença central do gradiente de pressão num nó usa os dois nós **alternados** (i+1 e i−1), pulando o vizinho imediato. Um campo de pressão que oscila de nó em nó — alto, baixo, alto, baixo — tem, nos nós alternados usados pela fórmula, sempre o mesmo valor; a diferença entre eles dá zero, então essa oscilação **não produz gradiente nenhum** no cálculo e não é penalizada — o solver aceita esse padrão em xadrez como solução estacionária legítima, embora não tenha nada de físico. A malha escalonada resolve isso pondo a pressão no centro da célula e cada componente de velocidade no meio da face correspondente: o gradiente de pressão entre dois centros vizinhos passa a cair exatamente sobre o ponto de velocidade entre eles, um estêncil **compacto** entre vizinhos diretos, de modo que nenhuma oscilação de nó em nó escapa ao cálculo.
</details>

---

### 5. Aplicação / cálculo — `geologia-avancado-m23-q13` · oa02 · 9 pts

Para uma malha 1D de 8 nós, x = np.linspace(0, 7, 8) (Δx = 1), quantos centros de célula escalonados existem? Quais são os dois primeiros valores de `x_meio`?

<details>
<summary>Ver resposta</summary>

Uma malha de **n nós tem n−1 centros de célula**: 8 nós → **7 centros**.

x = [0, 1, 2, 3, 4, 5, 6, 7]. `x_meio = 0.5*(x[:-1] + x[1:])` = [0,5; 1,5; 2,5; 3,5; 4,5; 5,5; 6,5]. Os dois primeiros valores são **0,5 e 1,5**.
</details>

---

### 6. Múltipla escolha — `geologia-avancado-m23-q14` · oa02 · 8 pts

Um modelo precisa rastrear o caminho pressão-temperatura-tempo de uma porção específica de crosta durante uma colisão continental, mas resolver o campo de velocidade e pressão sobre uma malha que não se distorça mesmo com deformação acumulada grande. Qual arranjo atende às duas exigências?

- a) Malha puramente lagrangiana, colada ao material
- b) Malha euleriana fixa para resolver velocidade e pressão, com marcadores lagrangianos que se movem através dela carregando a história da porção de crosta — o método de partículas em célula
- c) Malha não estruturada, sem marcadores
- d) Duas malhas eulerianas independentes, uma para pressão e outra para temperatura

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Essa é exatamente a combinação descrita na Aula 04: a malha **euleriana fixa** nunca se distorce, o que a torna viável para deformação acumulada grande (uma malha lagrangiana pura ficaria irremediavelmente torcida); os **marcadores lagrangianos** carregam consigo a história de composição e temperatura de uma porção específica de material, que é exatamente o que a pergunta pede. "a" falha na primeira exigência (a malha se distorceria). "c" resolveria geometria irregular, não é o critério aqui, e sem marcadores não rastreia história de material. "d" não corresponde a nenhum arranjo descrito na aula.
</details>

---

### 7. Verdadeiro ou Falso (justifique) — `geologia-avancado-m23-q15` · oa03 · 8 pts

"A difusividade térmica κ é a mesma constante que aparece no decaimento radioativo, dN/dt = −κN, já que ambos os fenômenos descrevem processos que decaem ou se espalham com uma escala de tempo característica."

<details>
<summary>Ver resposta</summary>

**Falso.**

κ (difusividade térmica) e λ (constante de decaimento radioativo) são constantes de fenômenos matematicamente distintos. O decaimento radioativo, dN/dt = −λN, é uma **EDO de primeira ordem no tempo**, sem nenhuma derivada espacial, com solução exponencial fechada. A difusão de calor, ∂T/∂t = κ∂²T/∂z², é uma **EDP de segunda ordem no espaço** (e primeira no tempo). Apesar de ambas as constantes governarem "quão rápido algo muda", elas não são a mesma grandeza, não têm a mesma unidade (λ tem unidade de 1/tempo; κ tem unidade de área/tempo, m²/s) e não entram na mesma forma de equação — é exatamente a distinção EDO/EDP construída na Aula 02, aplicada aqui pela primeira vez a um caso concreto.
</details>

---

### 8. Aplicação / cálculo — `geologia-avancado-m23-q16` · oa03 · 9 pts

Uma rocha crustal tem k = 3,0 W/(m·K), ρ = 2.900 kg/m³, Cp = 900 J/(kg·K), com gradiente geotérmico medido de 25 °C/km. Calcule (a) a difusividade térmica κ e (b) o fluxo de calor condutivo.

<details>
<summary>Ver resposta</summary>

**(a)** ρCp = 2.900 × 900 = 2.610.000 J/(m³·K) = 2,61 × 10⁶ J/(m³·K).

κ = k / (ρCp) = 3,0 / (2,61 × 10⁶) ≈ **1,15 × 10⁻⁶ m²/s**.

**(b)** Gradiente em unidades SI: 25 °C/km = 0,025 K/m.

q = k × (dT/dz) = 3,0 × 0,025 = **0,075 W/m² = 75 mW/m²**.
</details>

---

### 9. Múltipla escolha — `geologia-avancado-m23-q17` · oa03 · 8 pts

Uma pluma mantélica quente ascende através do manto circundante, carregando consigo sua própria temperatura elevada. Qual termo da equação de conservação de calor domina esse processo?

- a) Difusão, porque calor está atravessando rocha
- b) Produção, porque a pluma gera calor internamente
- c) Advecção, porque é a própria rocha (a pluma) que se move, transportando fisicamente sua temperatura
- d) Nenhum dos três — o processo não é descrito pela equação de conservação de calor

<details>
<summary>Ver resposta</summary>

**Resposta: c**

Advecção é exatamente isso: calor sendo fisicamente transportado pelo movimento do material. Numa pluma ascendente, a rocha (ou o magma) se move, levando sua temperatura consigo — o mesmo mecanismo citado na Aula 05 para uma placa subductando ou magma subindo por um conduto. "a" descreve o caso oposto: difusão é calor atravessando rocha **parada**. "b" seria aplicável a decaimento radioativo interno, não ao transporte por movimento de material. "d" está incorreta — advecção é um dos três termos da própria equação de conservação de calor.
</details>

---

### 10. Aplicação / cálculo — `geologia-avancado-m23-q18` · oa02 · 9 pts

Uma malha 1D de 5 nós (z = 0,1,2,3,4; Δz=1) tem extremidades fixas em T=0 e condição inicial T = [0, 0, 50, 0, 0]. Aplique um passo do esquema explícito com κ = 0,4 e Δt = 0,5 (sem produção de calor). Primeiro verifique se r ≤ 1/2, depois calcule T_novo nos três nós interiores.

<details>
<summary>Ver resposta</summary>

r = κΔt/Δz² = 0,4 × 0,5 / 1² = **0,2** — dentro do limite de estabilidade r ≤ 0,5. Esquema estável.

Aplicando T_novo[i] = T[i] + r·(T[i+1] − 2T[i] + T[i−1]):

- i=1: T[0]=0, T[1]=0, T[2]=50 → T_novo[1] = 0 + 0,2×(50 − 0 + 0) = **10**
- i=2: T[1]=0, T[2]=50, T[3]=0 → T_novo[2] = 50 + 0,2×(0 − 100 + 0) = 50 − 20 = **30**
- i=3: T[2]=50, T[3]=0, T[4]=0 → T_novo[3] = 0 + 0,2×(0 − 0 + 50) = **10**

T_novo = [0, 10, 30, 10, 0]. Conferindo a conservação de energia: soma antes = 0+0+50+0+0 = 50; soma depois = 0+10+30+10+0 = 50 — igual, como esperado sem produção nem perda pelos contornos.
</details>

---

### 11. Verdadeiro ou Falso (justifique) — `geologia-avancado-m23-q19` · oa02 · 8 pts

"Se, ao simular numericamente a equação da difusão sem produção de calor, um nó da malha apresentar temperatura negativa em graus Celsius, isso já é prova de que o esquema numérico é instável."

<details>
<summary>Ver resposta</summary>

**Falso.**

Uma temperatura negativa em Celsius não é, por si só, sinal de instabilidade — é fisicamente banal (uma geoterma sob uma camada de gelo, por exemplo, começa negativa). O critério correto de instabilidade é a **violação do princípio do máximo**: a equação da difusão sem produção garante que a solução em qualquer instante posterior permanece **dentro** do intervalo entre o menor e o maior valor presentes na condição inicial e nas condições de contorno. Um valor que escapa desse intervalo — para cima ou para baixo — é matematicamente impossível para a equação sendo resolvida, e é isso, não o sinal do número, que denuncia a instabilidade numérica.
</details>

---

### 12. Integração (Aulas 03–06) — `geologia-avancado-m23-q20` · oa02+oa03 · 8 pts

O exemplo trabalhado da Aula 03 verifica ∇·**v** ≈ 0 como checagem de consistência de um campo de velocidade; o critério de instabilidade da Aula 06 verifica se a solução da equação do calor respeita o princípio do máximo. O que essas duas checagens têm em comum, do ponto de vista do trabalho de quem constrói um modelo geodinâmico?

<details>
<summary>Ver resposta</summary>

Uma boa resposta identifica que ambas são **testes de consistência interna**, aplicáveis antes mesmo de examinar se os resultados fazem sentido físico específico do problema: em ambos os casos, existe uma propriedade matemática que a solução **precisa** satisfazer — incompressibilidade (∇·**v** ≈ 0) para o campo de velocidade, ou o intervalo definido pelo princípio do máximo para o campo de temperatura — e essa propriedade é barata de verificar computacionalmente (um cálculo direto sobre o resultado já obtido). Se a checagem falha, o erro está quase certamente na formulação ou na discretização do código — não em algum efeito geológico exótico —, e é exatamente esse hábito de "verificar a saúde numérica do modelo antes de interpretar a física" que os dois exemplos trabalhados, de aulas diferentes, ensinam da mesma forma.
</details>

---

**Total: 100 pontos.**
