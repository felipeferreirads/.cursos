# Aula 04: Interpolação e ajuste — interpolação polinomial, diferenças finitas e mínimos quadrados

**ID:** geologia-m30-a04
**Módulo:** [[30-metodos-numericos-geociencias-modulo|Módulo 30 — Métodos numéricos para geociências]]
**Duração estimada:** ~30 min
**Nível:** ensino médio completo, sem geologia prévia (contrato `ensino-medio-sem-geologia-v1`)
**Objetivo:** interpolar e ajustar dados geológicos por interpolação polinomial, diferenças finitas e mínimos quadrados, reconhecendo os limites da extrapolação.

> [!info] O ponto mais caro do módulo Interpolar e ajustar **parecem** a mesma tarefa — "passar uma curva pelos pontos" — mas resolvem perguntas diferentes. Confundir as duas é o erro mais citado no planejamento deste módulo: interpolação **passa exatamente** pelos dados; ajuste por mínimos quadrados **aproxima** os dados, aceitando não passar exatamente por nenhum ponto, em troca de uma curva mais simples e mais confiável fora do ruído de medição.

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **Interpolação** | Estimar o valor de uma grandeza num ponto **entre** dados já conhecidos, usando uma função que passa exatamente por todos os pontos conhecidos. |
| **Extrapolação** | Estimar o valor de uma grandeza **além** do intervalo coberto pelos dados conhecidos — sempre mais arriscada que interpolar. |
| **Interpolação polinomial** | Interpolação feita ajustando um único polinômio que passa exatamente por todos os pontos dados. |
| **Fenômeno de Runge** | Oscilações grandes e artificiais que aparecem entre os pontos quando se usa um polinômio interpolador de grau muito alto — o polinômio passa exatamente pelos pontos, mas "balança" descontroladamente entre eles. |
| **Diferenças finitas** | Fórmulas que estimam a derivada (taxa de variação) de uma função a partir de valores conhecidos em pontos discretos, sem precisar de uma expressão analítica da função. |
| **Mínimos quadrados** | Método de ajuste que escolhe os parâmetros de uma curva (por exemplo, os coeficientes de uma reta) minimizando a soma dos quadrados das diferenças entre a curva e cada dado — sem exigir que a curva passe exatamente por nenhum ponto. |
| **Resíduo** | A diferença entre um dado observado e o valor previsto pela curva ajustada naquele ponto. |

## Antes de começar, você precisa saber

- **Condicionamento e propagação de erro** — [[30-metodos-numericos-geociencias-aula-01-erro-numerico|Módulo 30, aula 01]] (recomendado).
- **Média, desvio-padrão e a ideia de dispersão de dados** — [[28-matematica-geociencias-aula-04-estatistica-descritiva|Módulo 28, aula 04]] (recomendado).

## Ao final você vai conseguir

- [geologia-m30-oa04] Interpolar e ajustar dados geológicos por interpolação polinomial, diferenças finitas e mínimos quadrados, reconhecendo os limites da extrapolação.

## Conteúdo

### Interpolação: estimar entre pontos conhecidos

O caso mais simples de **interpolação** — linear, entre dois pontos — está por trás de uma tarefa corriqueira em geociências: estimar o topo de uma camada, ou uma propriedade de perfil de poço (porosidade, densidade), num ponto **entre** dois furos de sondagem já medidos. Se dois furos registram o topo de uma camada a profundidades diferentes, a interpolação linear estima esse topo em qualquer ponto entre eles assumindo variação proporcional à distância — uma reta ligando os dois valores conhecidos.

Quando há mais de dois pontos, a **interpolação polinomial** generaliza a ideia: em vez de uma reta entre dois pontos, ajusta-se um único polinômio (de grau maior, quando há mais pontos) que passa exatamente por **todos** eles. Isso parece sempre vantajoso — mais pontos, mais informação, curva mais "fiel" — mas tem um limite sério.

### O fenômeno de Runge: por que grau mais alto nem sempre ajuda

Seria natural supor que, quanto mais pontos e maior o grau do polinômio interpolador, melhor a estimativa entre eles. Na prática, polinômios de grau alto **oscilam** de forma cada vez mais violenta entre os pontos, sobretudo perto das bordas do intervalo — o **fenômeno de Runge**. O polinômio continua passando exatamente pelos pontos fornecidos, garantido por construção, mas os valores que produz **entre** eles podem ser fisicamente absurdos: uma porosidade acima de 100% ou negativa entre dois furos que registraram valores perfeitamente razoáveis.

> [!tip] Uma analogia Pense em tentar desenhar, à mão, uma linha suave que passe exatamente por dez pontos espalhados numa folha. Uma linha razoavelmente suave, com poucas curvas, já conecta os dez pontos de forma plausível. Forçar uma única curva "perfeita" (um polinômio) a passar exatamente por todos, sem nenhuma folga, tende a produzir voltas e reviravoltas desnecessárias entre pontos vizinhos — a curva "se contorce" para acertar cada ponto exatamente, em vez de seguir a tendência geral dos dados.

A prática usual para evitar o fenômeno de Runge é não usar um único polinômio de grau muito alto sobre muitos pontos, e sim interpolar por trechos: ligar pontos vizinhos por retas, ou usar trechos suaves (splines), que ficam fora do escopo desta aula.

### Diferenças finitas: estimar a derivada sem fórmula analítica

Muitas vezes, o que se quer de um conjunto de dados não é o valor entre dois pontos, mas a **taxa de variação** — a derivada — nesse ponto. As **diferenças finitas** fazem isso diretamente a partir dos dados discretos, sem precisar de uma expressão matemática da função: a diferença progressiva usa o ponto atual e o seguinte; a diferença regressiva usa o ponto atual e o anterior; a diferença central usa um ponto antes e um depois do ponto de interesse, e costuma ser mais precisa que as outras duas para o mesmo espaçamento entre dados. O gradiente geotérmico, já mencionado na aula 01 como exemplo de cálculo mal condicionado quando os pontos estão muito próximos, é justamente uma diferença finita: a variação de temperatura dividida pela variação de profundidade entre duas (ou mais) medidas de um perfil de temperatura em poço.

### Mínimos quadrados: ajustar sem exigir passagem exata

Dados de campo raramente são exatos — toda medição carrega ruído. Forçar uma curva a passar exatamente por dados ruidosos (interpolação) reproduz também o ruído, não só a tendência real. O **ajuste por mínimos quadrados** resolve isso de outro jeito: em vez de exigir passagem exata, escolhe os parâmetros da curva — a inclinação e o intercepto de uma reta, por exemplo — que **minimizam a soma dos quadrados dos resíduos**. Elevar ao quadrado, em vez de somar as diferenças diretas, evita que resíduos positivos e negativos se cancelem e penaliza mais os desvios maiores.

O exemplo mais direto em geocronologia é o **ajuste de uma isócrona**: várias análises isotópicas de minerais de uma mesma rocha tendem a cair aproximadamente sobre uma reta, se a rocha se formou num único evento e permaneceu um sistema fechado desde então. A **inclinação** dessa reta ajustada por mínimos quadrados liga-se à idade da rocha, via a constante de decaimento do sistema isotópico usado; o **intercepto** informa a composição isotópica inicial do isótopo filho. Nenhuma análise individual precisa cair exatamente sobre a reta — o método aceita, e espera, dispersão em torno dela por erro analítico.

### Interpolação sim, extrapolação com muito mais cautela

Tanto a interpolação quanto o ajuste por mínimos quadrados são confiáveis **dentro** do intervalo coberto pelos dados — é isso que **interpolação** significa por definição. Usar a mesma curva para prever um valor **fora** desse intervalo é **extrapolação**, e o risco é qualitativamente maior: nada garante que o comportamento observado continue além dos dados. Isso é especialmente grave com polinômios de grau alto, que já oscilam dentro do intervalo pelo fenômeno de Runge e disparam para valores extremos logo além dele, e com qualquer ajuste aplicado a fenômenos que mudam de regime — uma taxa de subsidência ajustada aos últimos milhões de anos de uma bacia não deve ser estendida, sem justificativa geológica adicional, a eras em que o regime tectônico podia ser outro.

## Exemplo trabalhado

**Situação 1 — interpolação linear do topo de uma camada.** Dois furos de sondagem, separados por 500 m, registram o topo de uma camada de arenito a 120 m de profundidade (furo A) e a 145 m de profundidade (furo B). Qual a profundidade estimada do topo dessa camada num ponto a 200 m do furo A (na linha reta entre os dois furos)?

**Passo 1.** Fração do caminho percorrido: 200 / 500 = 0,4.

**Passo 2.** Variação total de profundidade entre os furos: 145 − 120 = 25 m.

**Passo 3.** Profundidade estimada: 120 + 0,4 × 25 = 120 + 10 = **130 m**.

**Ressalva:** essa estimativa assume que o topo da camada varia de forma aproximadamente linear entre os dois furos — razoável para uma distância pequena e uma unidade sem falhas conhecidas entre os pontos, mas uma suposição, não um fato medido.

**Situação 2 — ajuste de isócrona por mínimos quadrados (simplificado).** Quatro minerais da mesma rocha fornecem os pares (razão isótopo-pai/filho estável, razão isótopo-filho radiogênico/filho estável): (0,10; 0,705), (0,30; 0,715), (0,50; 0,725) e (0,70; 0,735).

**Passo 1 — observar o padrão.** Os quatro pontos crescem de forma quase perfeitamente linear: a cada 0,20 de aumento no eixo x, o eixo y sobe 0,010.

**Passo 2 — estimar a inclinação.** Pelos dois pontos extremos: (0,735 − 0,705) / (0,70 − 0,10) = 0,030 / 0,60 = 0,05. Aqui os quatro pontos são exatamente colineares, então o ajuste completo por mínimos quadrados devolve exatamente esses mesmos 0,05 — o atalho e o método coincidem. Com dados reais isso não acontece: as análises se dispersam em torno da reta, o atalho de dois pontos passa a depender de *quais* dois pontos foram escolhidos, e é justamente por isso que se usa o ajuste sobre todos eles.

**Passo 3 — interpretar.** Essa inclinação (0,05) é proporcional à idade da rocha, através da constante de decaimento do sistema isotópico usado — o cálculo exato da idade a partir da inclinação foi tratado qualitativamente no [[03-tempo-geologico-geocronologia-modulo|Módulo 03]] e depende do isótopo específico. O intercepto da reta ajustada (o valor de y quando x = 0) informa a razão isotópica inicial do isótopo filho no momento da formação da rocha.

## Erros comuns

- **Usar um polinômio de grau alto sobre muitos pontos, achando que "mais fiel aos dados" é sempre melhor.** O fenômeno de Runge produz oscilações fisicamente absurdas entre os pontos, mesmo passando exatamente por cada um.
- **Extrapolar com a mesma confiança de uma interpolação.** Fora do intervalo dos dados nada garante que o comportamento observado continue, e o risco cresce mais rápido ainda com grau alto.
- **Confundir interpolação com ajuste.** Interpolação exige passar exatamente pelos pontos; mínimos quadrados aceita não passar por nenhum, em troca de uma curva menos sensível ao ruído de cada medição.
- **Calcular um gradiente a partir de pontos muito próximos sem lembrar do condicionamento (aula 01).** O mau condicionamento de dividir por um denominador pequeno se aplica aqui também.

## O que não concluir

- **Que esta aula ensina splines ou geoestatística (krigagem), usadas para interpolar mapas e superfícies a partir de dados espalhados irregularmente.** Splines resolvem a oscilação do fenômeno de Runge trocando um polinômio de grau alto por vários de grau baixo unidos suavemente; krigagem incorpora a estrutura espacial de correlação dos dados. Ambas ficam fora do escopo desta aula.
- **Que o ajuste por mínimos quadrados aqui apresentado cobre regressão múltipla (mais de uma variável independente) ou não linear.** O caso tratado foi o ajuste de uma reta a uma variável — a forma mais simples e mais comum em isócronas, mas não a única aplicação do método.

## Recap relâmpago

- **Interpolação** passa exatamente pelos dados e estima valores **entre** eles; **extrapolação** estima valores **fora** do intervalo dos dados e é sempre mais arriscada.
- **Interpolação polinomial** de grau alto sobre muitos pontos pode oscilar de forma artificial e fisicamente implausível entre os pontos — o **fenômeno de Runge**.
- **Diferenças finitas** estimam a derivada (taxa de variação) a partir de dados discretos; a diferença central costuma ser mais precisa que a progressiva ou a regressiva para o mesmo espaçamento.
- **Mínimos quadrados** ajusta uma curva minimizando a soma dos resíduos ao quadrado, sem exigir passagem exata por nenhum ponto — a base do ajuste de isócronas em geocronologia.
- Sempre distinguir se o valor de interesse está **dentro** do intervalo coberto pelos dados (interpolação, mais segura) ou **fora** dele (extrapolação, sempre mais arriscada).

## Próxima aula

[[30-metodos-numericos-geociencias-aula-05-integracao-e-edos|Aula 05 — Integração numérica e equações diferenciais ordinárias: trapézio, Simpson, Euler e Runge-Kutta]]

## Anterior

[[30-metodos-numericos-geociencias-aula-03-zeros-de-funcoes|Aula 03 — Zeros de funções]]

## Fontes

- Interpolação polinomial e fenômeno de Runge: Chapra, S. C. & Canale, R. P., *Numerical Methods for Engineers*, 7ª ed., McGraw-Hill, capítulo sobre interpolação.
- Diferenças finitas para aproximação de derivadas a partir de dados discretos: Chapra & Canale, *Numerical Methods for Engineers*, 7ª ed., capítulo sobre diferenciação numérica.
- Mínimos quadrados e ajuste de isócronas em geocronologia: Faure, G. & Mensing, T. M., *Isotopes: Principles and Applications*, 3ª ed., Wiley, capítulo sobre o método isócrono; retomada de [[03-tempo-geologico-geocronologia-modulo|Módulo 03]].
- Splines e krigagem como alternativas mais avançadas (mencionadas, não desenvolvidas): Chapra & Canale, *Numerical Methods for Engineers*, 7ª ed.; Isaaks, E. H. & Srivastava, R. M., *An Introduction to Applied Geostatistics*, Oxford University Press.

<!--
nivel: ensino-medio-sem-geologia-v1
palavras_corpo: 1598
bridge_lesson: true

mapa_objetivo_secao:
  geologia-m30-oa04: "Interpolação: estimar entre pontos conhecidos" + "O fenômeno de Runge: por que grau mais alto nem sempre ajuda" + "Diferenças finitas: estimar a derivada sem fórmula analítica" + "Mínimos quadrados: ajustar sem exigir passagem exata" + "Interpolação sim, extrapolação com muito mais cautela" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEO-M30-A04-INTERPOLACAO-DEF-001
    claim: "Interpolação estima o valor de uma função em um ponto dentro do intervalo coberto por dados conhecidos, usando uma função que passa exatamente pelos pontos dados; extrapolação estima valores fora desse intervalo e carrega risco maior de erro, pois não há garantia de que o comportamento observado dentro do intervalo continue além dele."
    risk: fato
    source: "Chapra & Canale, Numerical Methods for Engineers, 7ª ed., cap. sobre interpolação"
  - claim_id: GEO-M30-A04-RUNGE-002
    claim: "O fenômeno de Runge é a tendência de polinômios interpoladores de grau alto oscilarem de forma crescente e não física entre os pontos de dados, especialmente perto das bordas do intervalo, mesmo passando exatamente pelos pontos fornecidos; a prática usual para evitá-lo é usar interpolação por trechos de grau baixo (linear ou splines) em vez de um único polinômio de grau alto."
    risk: fato
    source: "Chapra & Canale, Numerical Methods for Engineers, 7ª ed., cap. sobre interpolação"
  - claim_id: GEO-M30-A04-DIFERENCAS-FINITAS-003
    claim: "As fórmulas de diferenças finitas (progressiva, regressiva e central) estimam a derivada de uma função a partir de valores discretos conhecidos, sem exigir uma expressão analítica da função; para o mesmo espaçamento entre pontos, a diferença central costuma ter erro de truncamento menor que a progressiva ou a regressiva."
    risk: fato
    source: "Chapra & Canale, Numerical Methods for Engineers, 7ª ed., cap. sobre diferenciação numérica"
  - claim_id: GEO-M30-A04-MINIMOS-QUADRADOS-004
    claim: "O método dos mínimos quadrados ajusta os parâmetros de uma curva minimizando a soma dos quadrados dos resíduos (diferenças entre valores observados e previstos), sem exigir que a curva passe exatamente por nenhum ponto observado, sendo apropriado para dados com ruído de medição."
    risk: fato
    source: "Chapra & Canale, Numerical Methods for Engineers, 7ª ed., cap. sobre regressão por mínimos quadrados"
  - claim_id: GEO-M30-A04-ISOCRONA-005
    claim: "No método isócrono de geocronologia, análises de diferentes minerais (ou fases) de uma mesma rocha formada num único evento e que permaneceu um sistema fechado tendem a se alinhar aproximadamente sobre uma reta num diagrama de razões isotópicas; a inclinação dessa reta, ajustada por mínimos quadrados, relaciona-se com a idade da rocha através da constante de decaimento do sistema isotópico usado, e o intercepto indica a composição isotópica inicial do isótopo filho."
    risk: fato
    source: "Faure, G. & Mensing, T. M., Isotopes: Principles and Applications, 3ª ed., Wiley, cap. sobre o método isócrono"

nota_trilha_apoio: >-
  Aula 4 de 5 do módulo 30 (trilha de apoio, opcional, não bloqueante), criada em
  2026-08-29. Distingue explicitamente interpolação de ajuste por mínimos
  quadrados, apontado no hub do módulo como o ponto de maior dificuldade;
  retoma condicionamento (aula 01) na diferença finita do gradiente e amarra
  mínimos quadrados ao método isócrono já visto qualitativamente no Módulo 03.
-->
