# Aula 05: Integração numérica e equações diferenciais ordinárias — trapézio, Simpson, Euler e Runge-Kutta

**ID:** geologia-m30-a05
**Módulo:** [[30-metodos-numericos-geociencias-modulo|Módulo 30 — Métodos numéricos para geociências]]
**Duração estimada:** ~30 min
**Nível:** ensino médio completo, sem geologia prévia (contrato `ensino-medio-sem-geologia-v1`)
**Objetivo:** calcular integrais numéricas pelas regras do trapézio e de Simpson, e resolver equações diferenciais ordinárias por Euler e Runge-Kutta, estimando o erro de cada método.

> [!info] A última peça do módulo — e o que ela destrava As quatro aulas anteriores deram as ferramentas para lidar com erro, sistemas, raízes e ajuste de dados. Esta fecha o módulo com as duas operações que faltavam: somar áreas (integração) e projetar como uma grandeza muda ao longo do tempo (equações diferenciais). É exatamente esse par de ferramentas — junto com diferenças finitas, vista na [[30-metodos-numericos-geociencias-aula-04-interpolacao-e-ajuste|aula 04]] — que o Módulo 23 do curso avançado (modelagem numérica geodinâmica) pressupõe.

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **Integral (numérica)** | A área sob uma curva entre dois pontos, calculada a partir de valores conhecidos da função em pontos discretos, sem precisar de uma expressão analítica dela. |
| **Regra do trapézio** | Método de integração numérica que aproxima a área sob a curva, entre cada par de pontos consecutivos, pela área de um trapézio. |
| **Regra de Simpson** | Método de integração numérica que aproxima a curva, a cada par de intervalos, por uma parábola em vez de uma reta — mais precisa que o trapézio para curvas suaves. |
| **Equação diferencial ordinária (EDO)** | Uma equação que relaciona uma grandeza à sua própria taxa de variação (derivada) — descreve como algo muda ao longo do tempo (ou de outra variável), em vez de dar seu valor diretamente. |
| **Método de Euler** | Método mais simples para resolver uma EDO numericamente: avança em passos pequenos, usando a taxa de variação conhecida no início de cada passo para projetar o valor seguinte. |
| **Runge-Kutta (RK4, clássico de 4ª ordem)** | Método que resolve uma EDO combinando várias estimativas da taxa de variação dentro de cada passo (não só no início), produzindo uma projeção muito mais precisa para o mesmo tamanho de passo que Euler. |
| **Ordem de um método** | Uma medida de quão rápido o erro de um método numérico diminui conforme o passo (ou o espaçamento) diminui — quanto maior a ordem, mais rápido o erro cai ao refinar o passo. |

## Antes de começar, você precisa saber

- **Diferenças finitas** — [[30-metodos-numericos-geociencias-aula-04-interpolacao-e-ajuste|Módulo 30, aula 04]] (recomendado).
- **Função exponencial e a matemática da meia-vida** — [[28-matematica-geociencias-aula-03-exponenciais-e-logaritmos|Módulo 28, aula 03]] (recomendado, usado no exemplo trabalhado).

## Ao final você vai conseguir

- [geologia-m30-oa05] Calcular integrais numéricas pelas regras do trapézio e de Simpson e resolver equações diferenciais ordinárias por Euler e Runge-Kutta, estimando o erro de cada método.

## Conteúdo

### Integração numérica: somar área quando só há pontos, não fórmula

Muitos dados geológicos vêm como uma série de pontos discretos — uma taxa de subsidência de uma bacia sedimentar medida em alguns intervalos de tempo, uma taxa de produção de um poço amostrada mês a mês — e o que interessa não é o valor pontual, mas o **acumulado**: a subsidência total ao longo de um intervalo, ou o volume total produzido. Esse acumulado é uma **integral** — a área sob a curva que liga os pontos — e, sem uma fórmula fechada para a curva, ela precisa ser aproximada numericamente a partir dos próprios pontos.

A **regra do trapézio** é a aproximação mais simples: entre cada par de pontos consecutivos, a área sob a curva é aproximada pela área do trapézio formado pelos dois valores da função e a base no eixo horizontal. Somando a área de todos os trapézios ao longo do intervalo, chega-se a uma estimativa da integral total. O erro dessa aproximação vem de tratar como reta um trecho de curva que, na realidade, pode ser curvo — quanto mais pontos (trapézios mais estreitos), menor esse erro.

A **regra de Simpson** melhora essa ideia: em vez de ligar os pontos por retas, ajusta uma **parábola** a cada par de intervalos (exigindo, por isso, um número par de intervalos no total) — uma parábola acompanha a curvatura de uma função suave muito melhor que uma reta, reduzindo o erro de forma substancial para o mesmo número de pontos. Em termos de ordem: o erro do trapézio cai proporcionalmente ao quadrado do tamanho do passo (dobrar o número de pontos reduz o erro a cerca de um quarto); o erro de Simpson cai proporcionalmente à quarta potência do passo (dobrar o número de pontos reduz o erro a cerca de um dezesseis avos) — para funções suaves, Simpson tipicamente entrega muito mais precisão com o mesmo esforço de amostragem.

### Equações diferenciais ordinárias: descrever como algo muda

Uma **equação diferencial ordinária (EDO)** não dá o valor de uma grandeza diretamente — dá a **taxa de variação** dela, geralmente em função do próprio valor atual (e às vezes do tempo). O exemplo mais familiar deste curso é o **decaimento radioativo**: a taxa de variação do número de átomos radioativos, a cada instante, é proporcional ao número de átomos ainda presentes (dN/dt = −λN, onde λ é a constante de decaimento) — quanto mais átomos restam, mais decaem por unidade de tempo, e a quantidade vai diminuindo cada vez mais devagar em termos absolutos. Esse caso específico tem solução analítica exata (a função exponencial vista no [[28-matematica-geociencias-aula-03-exponenciais-e-logaritmos|Módulo 28, aula 03]]), o que o torna ideal para **testar e comparar** métodos numéricos contra uma resposta certa conhecida — exatamente o que o exemplo trabalhado desta aula faz. Outro caso clássico e mais simples ainda é o resfriamento de um corpo pequeno em contato com um ambiente de temperatura constante (lei de resfriamento de Newton): a taxa de queda de temperatura é proporcional à diferença entre a temperatura do corpo e a do ambiente — um modelo simplificado (de parâmetro concentrado, sem variação espacial dentro do corpo), diferente da equação de difusão de calor completa que descreve como o calor se propaga dentro de um corpo extenso e que exige métodos mais avançados (fora do escopo desta aula).

### Método de Euler: o passo mais simples

O **método de Euler** resolve uma EDO numericamente da forma mais direta possível: partindo de um valor inicial conhecido, calcula a taxa de variação **naquele ponto de partida**, e usa essa taxa para projetar o valor no próximo instante, um passo de tamanho fixo à frente — como se a taxa de variação permanecesse constante durante todo o passo (o que raramente é verdade). Repete-se o processo, usando sempre o valor mais recente calculado como novo ponto de partida.

> [!tip] Uma analogia É como dirigir um carro olhando só o velocímetro no instante em que você começa a andar, e manter essa mesma velocidade "de memória" por um trecho inteiro antes de olhar de novo — se a velocidade real mudou durante o trecho (freou numa curva, acelerou depois), sua estimativa de quanto andou fica cada vez mais torta, principalmente se o trecho entre uma olhada e a próxima for longo.

O erro do método de Euler vem exatamente disso: assumir que a taxa de variação, medida só no início do passo, vale para o passo inteiro. Passos menores reduzem esse erro, mas custam mais passos (mais cálculo) para cobrir o mesmo intervalo total — e o erro acumulado, ao longo de muitos passos, cresce proporcionalmente ao tamanho do passo (método de **primeira ordem**).

### Runge-Kutta: várias olhadas por passo

O método de **Runge-Kutta clássico de quarta ordem (RK4)** ataca o mesmo problema de outro jeito: em vez de usar a taxa de variação só no início do passo, calcula-a em **vários pontos** dentro do mesmo passo (no início, em dois pontos intermediários estimados, e no fim) e combina essas várias estimativas numa média ponderada, que representa muito melhor o comportamento real da taxa de variação ao longo de todo o passo. O resultado é um método de **quarta ordem**: o erro cai proporcionalmente à quarta potência do tamanho do passo — reduzir o passo pela metade reduz o erro a cerca de um dezesseis avos, contra a redução de apenas metade que o mesmo corte de passo daria no método de Euler.

Essa diferença de ordem tem uma consequência prática direta: RK4 costuma entregar muito mais precisão do que Euler usando o **mesmo** tamanho de passo (ao custo de mais cálculo por passo, já que avalia a taxa de variação quatro vezes em vez de uma) — e, para muitos problemas, um RK4 com passos grandes ainda supera um Euler com passos bem menores, para o mesmo esforço computacional total.

### O que fica para depois: sistemas e equações de difusão espacial

Esta aula tratou de uma única grandeza variando com uma única variável (o tempo, tipicamente). Modelar como o **calor se difunde dentro** de um corpo (por exemplo, como a temperatura evolui em profundidade e ao longo do tempo numa intrusão ígnea resfriando, ou a evolução da geoterma numa litosfera) exige uma **equação diferencial parcial** — variação em mais de uma dimensão ao mesmo tempo (espaço e tempo) — tratada por generalizações das diferenças finitas (aula 04) combinadas com os métodos desta aula, mas com uma camada adicional de complexidade (malhas espaciais, esquemas explícitos e implícitos) que este módulo não cobre. É exatamente esse tratamento mais completo que o módulo 23 do curso avançado (modelagem numérica geodinâmica) assume como já conhecido — e é por isso que este módulo 30 é citado, no seu próprio hub, como pré-requisito de fato daquele módulo.

## Exemplo trabalhado

**Situação — decaimento radioativo, Euler contra a solução exata.** Uma amostra tem N₀ = 1.000 átomos de um isótopo com constante de decaimento λ = 0,1 por unidade de tempo (dN/dt = −0,1N). Estimar N depois de duas unidades de tempo, usando Euler com passo de 1 unidade, e comparar com a solução exata.

**Passo 1 — primeiro passo de Euler.** Taxa em t=0: dN/dt = −0,1 × 1.000 = −100. Projeção para t=1: N(1) ≈ 1.000 + (−100) × 1 = **900**.

**Passo 2 — segundo passo de Euler.** Taxa em t=1 (usando o valor já projetado): dN/dt = −0,1 × 900 = −90. Projeção para t=2: N(2) ≈ 900 + (−90) × 1 = **810**.

**Passo 3 — solução exata.** Como dN/dt = −λN tem solução exata N(t) = N₀ × e^(−λt) ([[28-matematica-geociencias-aula-03-exponenciais-e-logaritmos|Módulo 28, aula 03]]): N(2) = 1.000 × e^(−0,2) ≈ 1.000 × 0,8187 ≈ **818,7**.

**Passo 4 — comparar o erro.** Euler deu 810; o valor exato é ≈818,7 — um erro de cerca de 8,7 átomos, ou aproximadamente 1,1% do valor verdadeiro, acumulado em apenas dois passos com um passo relativamente grande. Usando passos menores (por exemplo, 0,5 em vez de 1, com quatro passos ao todo), o erro do Euler cairia, mas não desapareceria — o método continua de primeira ordem.

**O que Runge-Kutta faria diferente:** aplicando RK4 com o mesmo passo de 1 unidade, o resultado ficaria muito mais próximo de 818,7 já nesses dois passos, porque o método usa a curvatura da taxa de variação dentro de cada passo, não só seu valor no início — a mesma lógica qualitativa do exemplo do carro: RK4 "olha o velocímetro" várias vezes dentro do mesmo trecho, em vez de uma só.

## Erros comuns

- **Usar a regra de Simpson com um número ímpar de intervalos.** Simpson exige pares de intervalos (uma parábola cobre dois intervalos de cada vez); um número ímpar de intervalos não se encaixa nesse esquema sem ajuste.
- **Usar passos grandes no método de Euler e confiar no resultado sem comparar com uma solução conhecida ou com um passo menor.** Como no exemplo trabalhado, o erro de Euler pode ser pequeno em porcentagem mas ainda assim significativo, e cresce mais rápido quanto maior o passo.
- **Achar que Runge-Kutta "elimina" o erro.** RK4 reduz o erro drasticamente para o mesmo passo, mas ainda é uma aproximação — nenhum método numérico (exceto em casos triviais) entrega o valor exato.
- **Aplicar Euler ou Runge-Kutta a uma equação de difusão espacial (calor se propagando dentro de um corpo) como se fosse uma EDO simples.** Isso exige tratar também a variação no espaço — uma equação diferencial **parcial**, fora do escopo desta aula.

## O que não concluir

- **Que esta aula ensina a resolver sistemas de várias EDOs acopladas, ou equações diferenciais parciais (como a equação de difusão de calor usada para modelar o resfriamento de uma intrusão ígnea de forma espacialmente completa).** Esses são os assuntos que o Módulo 23 do curso avançado (modelagem numérica geodinâmica) trata, e que este módulo apenas prepara o terreno para estudar.
- **Que a regra de Simpson é sempre superior à do trapézio na prática.** Para curvas com quebras abruptas, ruído forte, ou poucos pontos irregularmente espaçados, a suposição de uma parábola suave que Simpson faz pode não se sustentar tão bem quanto para curvas geológicas tipicamente graduais.

## Recap relâmpago

- **Regra do trapézio**: aproxima a área sob a curva por trapézios; erro cai com o quadrado do refinamento do passo (2ª ordem).
- **Regra de Simpson**: aproxima a curva por parábolas a cada dois intervalos; erro cai com a quarta potência do refinamento do passo (4ª ordem) — mais precisa para curvas suaves, exige número par de intervalos.
- **EDO** relaciona uma grandeza à sua taxa de variação; o decaimento radioativo (dN/dt = −λN) tem solução exata conhecida, o que o torna um bom caso de teste para validar métodos numéricos.
- **Método de Euler**: usa a taxa de variação só no início de cada passo — simples, mas erro de primeira ordem (cai proporcionalmente ao passo).
- **Runge-Kutta (RK4)**: combina várias estimativas da taxa de variação dentro do mesmo passo — muito mais preciso (4ª ordem) para o mesmo tamanho de passo, ao custo de mais cálculo por passo.
- Este módulo tratou de uma variável (tempo); difusão espacial (equações diferenciais **parciais**, como a do calor numa intrusão) é o próximo patamar, tratado no Módulo 23 do curso avançado.

## Próxima aula

Nenhuma — última aula do módulo. Ver [[30-metodos-numericos-geociencias-modulo|Módulo 30]] para o questionário e os flashcards (gerados em etapa seguinte).

## Anterior

[[30-metodos-numericos-geociencias-aula-04-interpolacao-e-ajuste|Aula 04 — Interpolação e ajuste]]

## Fontes

- Regra do trapézio, regra de Simpson e ordem de erro de integração numérica: Chapra, S. C. & Canale, R. P., *Numerical Methods for Engineers*, 7ª ed., McGraw-Hill, capítulos sobre integração numérica (Newton-Cotes).
- Método de Euler, Runge-Kutta clássico de 4ª ordem e ordem de convergência: Chapra & Canale, *Numerical Methods for Engineers*, 7ª ed., capítulos sobre solução numérica de EDOs; Burden, R. L. & Faires, J. D., *Numerical Analysis*, 9ª ed., Cengage.
- Decaimento radioativo como EDO com solução analítica exata: retomada de [[28-matematica-geociencias-aula-03-exponenciais-e-logaritmos|Módulo 28, aula 03]].
- Equações diferenciais parciais em modelagem térmica de intrusões e da litosfera, como o próximo patamar do assunto: Turcotte, D. L. & Schubert, G., *Geodynamics*, 3ª ed., Cambridge University Press, capítulos sobre condução de calor.

<!--
nivel: ensino-medio-sem-geologia-v1
palavras_corpo: 1882
bridge_lesson: true

mapa_objetivo_secao:
  geologia-m30-oa05: "Integração numérica: somar área quando só há pontos, não fórmula" + "Equações diferenciais ordinárias: descrever como algo muda" + "Método de Euler: o passo mais simples" + "Runge-Kutta: várias olhadas por passo" + "O que fica para depois: sistemas e equações de difusão espacial" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEO-M30-A05-TRAPEZIO-SIMPSON-001
    claim: "A regra do trapézio aproxima a integral definida de uma função por meio de trapézios entre pontos consecutivos, com erro global proporcional ao quadrado do tamanho do passo (2ª ordem); a regra de Simpson aproxima a função por parábolas a cada par de intervalos (exigindo número par de intervalos), com erro global proporcional à quarta potência do tamanho do passo (4ª ordem)."
    risk: fato
    source: "Chapra & Canale, Numerical Methods for Engineers, 7ª ed., cap. sobre fórmulas de integração de Newton-Cotes"
  - claim_id: GEO-M30-A05-DECAIMENTO-EDO-002
    claim: "O decaimento radioativo é modelado pela equação diferencial ordinária dN/dt = −λN, cuja solução analítica exata é N(t) = N0 × e^(−λt), sendo por isso um caso de teste útil para comparar métodos numéricos de solução de EDOs contra uma resposta conhecida."
    risk: fato
    source: "física nuclear elementar; Faure & Mensing, Isotopes: Principles and Applications, 3ª ed.; retomada de 28-matematica-geociencias-aula-03"
  - claim_id: GEO-M30-A05-EULER-003
    claim: "O método de Euler resolve uma EDO numericamente avançando em passos discretos, usando a derivada (taxa de variação) calculada no início de cada passo para projetar o valor seguinte; é um método de primeira ordem, com erro global proporcional ao tamanho do passo."
    risk: fato
    source: "Chapra & Canale, Numerical Methods for Engineers, 7ª ed., cap. sobre métodos de passo único para EDOs; Burden & Faires, Numerical Analysis, 9ª ed."
  - claim_id: GEO-M30-A05-RUNGE-KUTTA-004
    claim: "O método de Runge-Kutta clássico de quarta ordem (RK4) combina quatro avaliações da derivada em pontos distintos dentro de cada passo (numa média ponderada) para estimar o próximo valor, sendo um método de quarta ordem, com erro global proporcional à quarta potência do tamanho do passo — consideravelmente mais preciso que o método de Euler para o mesmo tamanho de passo."
    risk: fato
    source: "Chapra & Canale, Numerical Methods for Engineers, 7ª ed., cap. sobre métodos de Runge-Kutta; Burden & Faires, Numerical Analysis, 9ª ed."
  - claim_id: GEO-M30-A05-DIFUSAO-CALOR-005
    claim: "Modelar a propagação espacial de calor dentro de um corpo (por exemplo, o resfriamento de uma intrusão ígnea ou a evolução da geoterma litosférica ao longo da profundidade e do tempo) requer uma equação diferencial parcial (variação simultânea no espaço e no tempo), tratada numericamente por generalizações de diferenças finitas combinadas com esquemas de integração no tempo, distinta em complexidade de uma equação diferencial ordinária de uma única variável."
    risk: fato
    source: "Turcotte, D. L. & Schubert, G., Geodynamics, 3ª ed., Cambridge University Press, cap. sobre condução de calor na litosfera"

nota_trilha_apoio: >-
  Aula 5 de 5 e última do módulo 30 (trilha de apoio, opcional, não bloqueante),
  criada em 2026-08-29. Fecha o módulo validando Euler contra a solução exata
  do decaimento radioativo (já visto qualitativamente no Módulo 28, aula 03) e
  aponta explicitamente, na seção final de conteúdo, a lacuna que o módulo 23
  do curso `curso-geologia-avancado` (modelagem numérica geodinâmica) cobre em
  seguida — EDPs de difusão de calor — sem tentar ensiná-la aqui.
-->
