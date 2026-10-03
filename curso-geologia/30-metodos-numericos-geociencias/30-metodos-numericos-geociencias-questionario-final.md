# Questionário — Módulo 30: Métodos numéricos para geociências (Final)

**Cobre:** aulas 01–05 (módulo inteiro) · **Objetivo:** testar erro e condicionamento, sistemas lineares, zeros de funções, interpolação e ajuste, e integração numérica e EDOs — com peso em aplicação a casos geológicos.

> [!note] Numeração das questões de `oa05` (sobrevive à divisão da aula 05)
> A revisão didática recomenda dividir a aula 05 em **05a — integração numérica** (trapézio, Simpson) e **05b — EDOs** (Euler, Runge-Kutta), com o objetivo `geologia-m30-oa05` desmembrado em `oa05a` e `oa05b`. Este questionário já trata os dois como blocos separados: as questões **12 e 13** avaliam `oa05a` (integração) e as questões **14 e 15** avaliam `oa05b` (EDOs). Se a aula 05 for dividida, nenhuma questão precisa ser renumerada — só o rótulo de objetivo de cada bloco passa a apontar para `oa05a` / `oa05b`. A integração numérica recebe um item de aplicação próprio (questão 13), já que a aula 05 não traz exemplo trabalhado para ela.

## Questões

**1. (Múltipla escolha)** Um programa calcula sen(x) somando apenas os três primeiros termos da série de Taylor da função, e guarda cada termo em ponto flutuante de precisão dupla. Os erros presentes no resultado são:
- a) só erro de arredondamento, porque o computador tem precisão finita
- b) só erro de truncamento, porque a série foi interrompida
- c) erro de truncamento (parar a série em três termos) e erro de arredondamento (guardar cada termo com dígitos finitos), que são independentes e se somam
- d) nenhum erro, porque três termos da série de Taylor bastam para qualquer x
- e) erro de propagação apenas, que não tem relação com truncamento nem com arredondamento

**2. (V/F — justifique)** "Refazer um cálculo mal condicionado com o dobro de casas decimais elimina o efeito do mau condicionamento."

**3. (Aplicação)** Um perfil de temperatura em poço registra 60,2 °C a 1.000 m e 60,5 °C a 1.010 m, cada leitura com incerteza de ±0,1 °C. (a) Calcule o gradiente geotérmico aparente em °C/km. (b) Estime o erro relativo desse gradiente, propagando a incerteza das duas leituras no pior caso. (c) Diga o que muda se as mesmas temperaturas forem medidas a 1.000 m e 1.500 m, e como esse problema se chama.

**4. (Múltipla escolha)** Sobre a eliminação de Gauss:
- a) é um método iterativo que parte de um palpite e o refina até convergir
- b) é um método direto: escalona o sistema até a forma triangular e resolve por substituição regressiva; um pivô muito pequeno amplifica erro de arredondamento nas etapas seguintes
- c) só funciona para sistemas com dominância diagonal
- d) o pivotamento parcial altera a solução exata do sistema para reduzir o erro
- e) tem custo que cresce linearmente com o número de incógnitas

**5. (V/F — justifique)** "Se um sistema linear não tem dominância diagonal, o método de Gauss-Seidel com certeza vai divergir."

**6. (Aplicação)** Considere o sistema:

```
10x + 2y +  z = 13
 x + 8y + 2z = 11
2x +  y + 6z =  9
```

Verifique se ele é estritamente diagonal dominante e diga o que isso permite concluir sobre a convergência de Gauss-Seidel. Para o sistema do exemplo trabalhado da aula 02 (balanço de massa de três fontes), Gauss-Seidel divergia — explique em uma frase por que a conclusão é diferente aqui.

**7. (Múltipla escolha)** Bisseção e Newton-Raphson para achar um zero de f(x):
- a) a bisseção pode divergir se o intervalo inicial for mal escolhido
- b) Newton-Raphson sempre converge, desde que a função seja contínua
- c) a bisseção sempre converge se o intervalo inicial contém uma mudança de sinal, mas é lenta (convergência linear); Newton-Raphson é mais rápido (quadrática), porém pode divergir com palpite ruim ou derivada próxima de zero
- d) os dois métodos exigem calcular a derivada da função a cada passo
- e) Newton-Raphson corta o intervalo ao meio a cada repetição

**8. (Aplicação)** Uma equação geoquímica de equilíbrio se reduz a achar a raiz positiva de f(x) = x² − 10. Partindo de x₀ = 3, faça **um** passo de Newton-Raphson (lembre que f'(x) = 2x) e compare com o valor verdadeiro √10 ≈ 3,1623. Em que situação, para outra função, esse mesmo passo poderia jogar a estimativa para longe da raiz?

**9. (Múltipla escolha)** O fenômeno de Runge descreve:
- a) o erro de arredondamento que se acumula ao somar muitos termos pequenos
- b) a oscilação crescente e fisicamente implausível de um polinômio interpolador de grau alto **entre** os pontos de dados, apesar de ele passar exatamente por cada ponto
- c) a divergência de Newton-Raphson perto de um ponto de inflexão
- d) a perda de dígitos ao subtrair dois números próximos
- e) a instabilidade de Gauss-Seidel em sistemas quase singulares

**10. (Dissertativa curta)** Explique a diferença entre **interpolar** um conjunto de dados e **ajustá-lo por mínimos quadrados**. Para dados de campo com ruído de medição, qual das duas abordagens é preferível e por quê? Cite um uso geológico do ajuste por mínimos quadrados.

**11. (Aplicação)** Dois furos de sondagem, separados por 400 m em linha reta, registram o topo de uma camada de folhelho a 210 m de profundidade (furo A) e a 250 m (furo B). Estime, por interpolação linear, a profundidade do topo dessa camada num ponto a 100 m do furo A, na linha entre os dois. Que suposição essa estimativa embute?

**12. (Múltipla escolha — `oa05a`, integração numérica)** Sobre a regra do trapézio e a regra de Simpson:
- a) as duas têm a mesma ordem de erro; a escolha é indiferente
- b) a regra do trapézio aproxima a curva por retas entre pontos consecutivos (erro de 2ª ordem no passo); a de Simpson aproxima por parábolas a cada par de intervalos (erro de 4ª ordem), exigindo número par de intervalos
- c) a regra de Simpson exige número ímpar de intervalos
- d) a regra do trapézio é sempre mais precisa que a de Simpson para curvas suaves
- e) nenhuma das duas serve quando só há pontos discretos, sem fórmula da função

**13. (Aplicação — `oa05a`, integração numérica)** A taxa de subsidência de uma bacia foi estimada em quatro instantes:

| tempo (Ma) | 0 | 2 | 4 | 6 |
|---|---|---|---|---|
| taxa (m/Ma) | 100 | 80 | 60 | 40 |

Use a regra do trapézio (com os quatro pontos, passo de 2 Ma) para estimar a subsidência total acumulada entre 0 e 6 Ma. Mostre a soma dos trapézios.

**14. (Múltipla escolha — `oa05b`, EDOs)** Sobre os métodos de Euler e Runge-Kutta clássico de 4ª ordem (RK4) para resolver uma EDO:
- a) Euler é de 4ª ordem e RK4 de 1ª ordem
- b) Euler usa a taxa de variação só no início do passo (1ª ordem: erro global proporcional ao passo); RK4 combina várias avaliações da taxa dentro do passo (4ª ordem: erro proporcional à 4ª potência do passo), ao custo de mais cálculo por passo
- c) RK4 elimina o erro numérico, entregando o valor exato
- d) os dois métodos exigem a solução analítica da EDO para funcionar
- e) Euler é mais preciso que RK4 para o mesmo tamanho de passo

**15. (Aplicação — `oa05b`, EDOs)** Um corpo pequeno resfria segundo dT/dt = −0,1 (T − 20), com T em °C e t em minutos (lei de resfriamento de Newton, ambiente a 20 °C). Partindo de T₀ = 100 °C, faça **dois** passos do método de Euler com passo h = 5 min e estime T(10 min). A solução exata é T(t) = 20 + 80·e^(−0,1t), com T(10) ≈ 49,4 °C. O Euler subestimou ou superestimou, e o que reduziria esse erro?

---

## Gabarito comentado

<details><summary>Ver respostas</summary>

**1.** Resposta: **c)**. Truncamento = parar um processo exato (a série infinita) numa versão finita; existiria mesmo com aritmética perfeita. Arredondamento = representar cada termo com dígitos finitos em ponto flutuante. São fontes independentes e se somam no resultado. (a) e (b) capturam só metade; (d) é falso (três termos só bastam para x pequeno); (e) propagação é como os erros já existentes se espalham pelas operações, não uma terceira fonte que exclua as outras duas.

**2.** **Falso.** Mais casas decimais reduzem o erro de **arredondamento**, mas o mau condicionamento é uma propriedade do **problema**: ele amplifica a incerteza da **entrada** (dados de medição), e nenhuma precisão extra no cálculo aritmético conserta isso. O remédio é mudar o problema — medir em pontos mais espaçados, obter dados mais independentes, reformular.

**3.** (a) Gradiente = (60,5 − 60,2) / (1.010 − 1.000) = 0,3 °C / 10 m = 0,03 °C/m = **30 °C/km**. (b) O numerador (0,3 °C) é uma diferença de duas leituras, cada uma com ±0,1 °C; no pior caso (uma lida para cima, a outra para baixo) a incerteza do numerador é ±0,2 °C — ou seja, um erro relativo de cerca de **±67%** no gradiente, antes de qualquer outra fonte de incerteza. (c) Com as leituras a 1.000 m e 1.500 m, o mesmo ±0,1 °C por leitura é uma fração muito menor do denominador (agora 500 m), e o gradiente fica muito mais confiável — nada no cálculo mudou, só o espaçamento. O problema é o **mau condicionamento** (dividir por um denominador pequeno, próximo de zero), o mesmo da aula 01.

**4.** Resposta: **b)**. Eliminação de Gauss é direta (escalonamento + substituição regressiva). Pivô pequeno → dividir por número perto de zero → amplifica arredondamento; daí o pivotamento parcial, que **não** altera a solução exata (d é falsa). (a) descreve um método iterativo; (c) dominância diagonal é assunto de Gauss-Seidel, não de Gauss; (e) o custo cresce com o cubo do número de incógnitas.

**5.** **Falso.** A dominância diagonal é condição **suficiente**, não **necessária**: quando presente, garante a convergência; quando ausente, nada se pode concluir só a partir disso — alguns sistemas sem dominância diagonal convergem mesmo assim. A ausência da condição obriga a checar a convergência de outra forma (por exemplo, observando se os valores param de mudar), não permite afirmar que vai divergir.

**6.** Linha 1: |10| = 10 > |2| + |1| = 3 ✓. Linha 2: |8| = 8 > |1| + |2| = 3 ✓. Linha 3: |6| = 6 > |2| + |1| = 3 ✓. O sistema é **estritamente diagonal dominante**, o que **garante** a convergência de Gauss-Seidel a partir de qualquer palpite inicial. No exemplo da aula 02, ao isolar cada incógnita, a equação do traçador Y tinha coeficiente 0,10 na sua própria incógnita contra 1,00 nas outras — o oposto de dominância diagonal, e por larga margem, e o método divergia. Aqui cada incógnita depende sobretudo de si mesma (coeficiente diagonal grande), então a condição suficiente é satisfeita.

**7.** Resposta: **c)**. Bisseção: converge sempre que o intervalo inicial contém mudança de sinal (não diverge), mas é lenta (linear). Newton-Raphson: rápido (quadrático), mas pode divergir com palpite distante, derivada ≈ 0 (tangente quase horizontal) ou função irregular. (a) a bisseção não "diverge" — no máximo não acha raiz se não há mudança de sinal no intervalo; (b) Newton-Raphson não converge sempre; (d) só Newton-Raphson usa derivada; (e) quem corta o intervalo ao meio é a bisseção.

**8.** f(3) = 9 − 10 = −1; f'(3) = 2·3 = 6; x₁ = 3 − (−1)/6 = 3 + 0,1667 = **3,1667**. Comparado a √10 ≈ 3,1623, o erro é ~0,004 — já muito bom num único passo. O mesmo passo poderia afastar a estimativa da raiz se, no ponto de partida, a **derivada fosse próxima de zero** (a tangente quase horizontal cruza o eixo x muito longe), ou se o palpite inicial estivesse longe demais da raiz, ou perto de um ponto de inflexão / de várias raízes próximas.

**9.** Resposta: **b)**. Runge = polinômio interpolador de grau alto oscilando de forma crescente entre os pontos (pior perto das bordas), produzindo valores absurdos (porosidade negativa, acima de 100%) mesmo passando exatamente por cada dado. A prática usual para evitá-lo é interpolar por trechos de grau baixo (linear, splines). (d) é cancelamento catastrófico; (c) e (e) são outros fenômenos; (a) não é Runge.

**10.** Interpolar = construir uma função que passa **exatamente** por todos os pontos dados e usá-la para estimar valores **entre** eles. Ajustar por mínimos quadrados = escolher os parâmetros de uma curva (a inclinação e o intercepto de uma reta, por exemplo) que **minimizam a soma dos quadrados dos resíduos**, **sem** exigir passagem exata por nenhum ponto. Para dados de campo com ruído, o ajuste por mínimos quadrados é preferível: forçar a curva a passar por cada ponto (interpolação) reproduz também o ruído de medição, não só a tendência real; o ajuste captura a tendência e tolera a dispersão. Uso geológico: ajuste da **isócrona** em geocronologia — a inclinação da reta ajustada às razões isotópicas de vários minerais de uma rocha liga-se à idade (via a constante de decaimento), e o intercepto dá a composição isotópica inicial do isótopo filho.

**11.** Fração do caminho: 100 / 400 = 0,25. Variação total de profundidade entre os furos: 250 − 210 = 40 m. Profundidade estimada: 210 + 0,25 × 40 = 210 + 10 = **220 m**. Suposição embutida: que o topo da camada varia de forma **aproximadamente linear** entre os dois furos — razoável para distância pequena e uma unidade sem falhas conhecidas entre os pontos, mas uma hipótese, não um dado medido.

**12.** Resposta: **b)**. Trapézio: retas entre pontos, erro de 2ª ordem (dobrar o número de pontos reduz o erro a ~1/4). Simpson: parábola a cada dois intervalos → exige número **par** de intervalos, erro de 4ª ordem (dobrar os pontos reduz o erro a ~1/16). (a), (c), (d) e (e) contradizem isso — inclusive (e): as duas regras existem justamente para integrar a partir de pontos discretos.

**13.** Regra do trapézio com passo h = 2 Ma e pontos f = (100, 80, 60, 40):
integral ≈ (h/2) · [f₀ + 2f₁ + 2f₂ + f₃] = (2/2) · [100 + 2·80 + 2·60 + 40] = 1 · [100 + 160 + 120 + 40] = **420 m**.
Conferindo trapézio a trapézio: [(100+80)/2]·2 + [(80+60)/2]·2 + [(60+40)/2]·2 = 180 + 140 + 100 = 420 m. A subsidência acumulada estimada entre 0 e 6 Ma é de cerca de **420 m**.

**14.** Resposta: **b)**. Euler: taxa só no início do passo → 1ª ordem (erro global ∝ passo). RK4: quatro avaliações da taxa por passo, média ponderada → 4ª ordem (erro ∝ passo⁴), muito mais preciso para o mesmo passo, ao custo de ~4× o cálculo por passo. (a) inverte as ordens; (c) nenhum método elimina o erro; (d) o objetivo dos métodos é justamente dispensar a solução analítica; (e) inverte a precisão.

**15.** Passo 1: taxa em t = 0 → dT/dt = −0,1·(100 − 20) = −8 °C/min. T(5) ≈ 100 + (−8)·5 = **60 °C**. Passo 2: taxa em t = 5 → dT/dt = −0,1·(60 − 20) = −4 °C/min. T(10) ≈ 60 + (−4)·5 = **40 °C**. A solução exata é ≈ 49,4 °C, então o Euler **subestimou** T(10) (previu resfriamento rápido demais, porque usou a taxa alta do início de cada passo para o passo inteiro, e a taxa real diminui à medida que T se aproxima de 20 °C). Reduziria o erro: usar um passo menor (mais passos de Euler), ou trocar por um método de ordem mais alta como RK4, que avalia a taxa em vários pontos dentro de cada passo.

</details>

---

<!--
gerado_em: 2026-08-29
skill: gerador-de-questionarios
tipo: final_cumulativo
modulo: 30
aulas_cobertas: [geologia-m30-a01, geologia-m30-a02, geologia-m30-a03, geologia-m30-a04, geologia-m30-a05]
total_questoes: 15
tipos: {multipla_escolha: 7, verdadeiro_falso: 2, dissertativa_curta: 1, aplicacao: 5}
matriz_cobertura:
  geologia-m30-oa01: [1, 2, 3]
  geologia-m30-oa02: [4, 5, 6]
  geologia-m30-oa03: [7, 8]
  geologia-m30-oa04: [9, 10, 11]
  geologia-m30-oa05a: [12, 13]   # integracao numerica (trapezio, Simpson) - inclui item de aplicacao (13)
  geologia-m30-oa05b: [14, 15]   # EDOs (Euler, Runge-Kutta)
restricao_didatica_respeitada: >-
  Achado laranja 1 da revisao didatica (aula 05 empacota dois assuntos, integracao
  sem exemplo trabalhado proprio; divisao 05a/05b recomendada). Integracao numerica
  e EDOs sao tratadas como blocos separados: Q12-Q13 -> oa05a, Q14-Q15 -> oa05b.
  A numeracao das questoes 12-15 sobrevive a divisao da aula 05 sem renumeracao -
  so o rotulo de objetivo de cada bloco passa a apontar para oa05a/oa05b. Integracao
  numerica recebe item de aplicacao proprio (Q13, regra do trapezio sobre taxa de
  subsidencia), suprindo a ausencia de exemplo trabalhado na aula.
observacao: >-
  Enquanto oa05 nao for formalmente desmembrado no course-state, a cobertura de
  oa05 e considerada satisfeita pela uniao dos blocos oa05a + oa05b (Q12-Q15).
gate_cientifico: aprovado
gate_didatico: liberado_com_restricao
-->
