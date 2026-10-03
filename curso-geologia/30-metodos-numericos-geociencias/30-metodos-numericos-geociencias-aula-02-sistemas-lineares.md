# Aula 02: Sistemas de equações lineares — eliminação de Gauss, Gauss-Seidel e matrizes mal condicionadas

**ID:** geologia-m30-a02
**Módulo:** [[30-metodos-numericos-geociencias-modulo|Módulo 30 — Métodos numéricos para geociências]]
**Duração estimada:** ~30 min
**Nível:** ensino médio completo, sem geologia prévia (contrato `ensino-medio-sem-geologia-v1`)
**Objetivo:** resolver sistemas de equações lineares por eliminação de Gauss e por Gauss-Seidel, e diagnosticar quando o método iterativo converge.

> [!info] Esta aula retoma o condicionamento da aula anterior A [[30-metodos-numericos-geociencias-aula-01-erro-numerico|aula 01]] mostrou que um problema pode amplificar erro de entrada mesmo sem nenhum erro de conta. Sistemas lineares são o primeiro lugar onde isso aparece em escala: um sistema "quase impossível de resolver" não por estar mal escrito, mas por estar mal condicionado.

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **Sistema linear** | Um conjunto de equações onde cada incógnita aparece apenas multiplicada por um número (nunca elevada a potência, nem dentro de seno/log), e cuja solução é o conjunto de valores que satisfaz todas as equações ao mesmo tempo. |
| **Pivô** | O coeficiente usado, em cada etapa da eliminação de Gauss, para zerar os coeficientes abaixo dele numa mesma coluna. |
| **Eliminação de Gauss** | Método **direto**: transforma o sistema, por etapas, numa forma triangular (onde cada equação tem menos incógnitas que a anterior) e depois resolve de trás para frente. |
| **Substituição regressiva** | A etapa final da eliminação de Gauss: resolver a última equação (uma incógnita), substituir na penúltima, e assim sucessivamente até a primeira. |
| **Método iterativo** | Método que parte de um palpite inicial e o refina, repetição após repetição, até o resultado parar de mudar de forma significativa — nunca dá a resposta exata "de uma vez", mas se aproxima dela. |
| **Gauss-Seidel** | Um método iterativo específico para sistemas lineares: em cada repetição, recalcula cada incógnita usando os valores mais recentes já disponíveis das outras. |
| **Dominância diagonal** | Uma condição sobre os coeficientes do sistema (o coeficiente da diagonal de cada equação é maior, em valor absoluto, que a soma dos demais coeficientes daquela equação) que **garante** a convergência de Gauss-Seidel. |
| **Matriz mal condicionada** | Um sistema em que pequenas mudanças nos coeficientes ou nos termos independentes produzem mudanças grandes e desproporcionais na solução — quase sempre porque as equações são quase redundantes entre si (quase paralelas). |

## Antes de começar, você precisa saber

- **Condicionamento** e propagação de erro — [[30-metodos-numericos-geociencias-aula-01-erro-numerico|Módulo 30, aula 01]] (exigido).
- Noção de vetor e de sistema de duas ou três incógnitas (ensino médio) é suficiente; esta aula reativa o resto.

## Ao final você vai conseguir

- [geologia-m30-oa02] Resolver sistemas de equações lineares por eliminação de Gauss e por Gauss-Seidel e diagnosticar quando o método iterativo converge.

## Conteúdo

### Onde sistemas lineares aparecem em geociências

Sistemas lineares nascem sempre que várias grandezas desconhecidas estão amarradas por várias relações simultâneas. Em geoquímica, o caso clássico é o **balanço de massa de mistura de fontes**: conhecidas a composição química da mistura final e a de cada área-fonte, as frações de cada fonte no sedimento saem de um sistema linear — uma equação por elemento usado como traçador, uma incógnita por fonte. Em geofísica, a **inversão de dados** (estimar a densidade de várias camadas do subsolo a partir de medidas de gravidade na superfície) recai, depois de linearizada, num sistema com uma equação por medida e uma incógnita por camada. Inversões realistas têm centenas ou milhares de incógnitas e exigem métodos além do que esta aula introduz.

### Eliminação de Gauss: resolver de forma direta

A **eliminação de Gauss** resolve um sistema em duas etapas. Na primeira, **escalonamento**, usa-se a primeira equação para eliminar a primeira incógnita de todas as equações abaixo dela (subtraindo múltiplos apropriados de uma equação das outras), depois a segunda equação — já sem a primeira incógnita — para eliminar a segunda das que vêm abaixo, e assim por diante, até sobrar uma equação com uma única incógnita. Na segunda etapa, **substituição regressiva**, resolve-se essa última equação, leva-se o valor à penúltima, resolve-se essa, e sobe-se até a primeira.

O coeficiente usado para eliminar uma coluna, em cada etapa, é o **pivô**. Um detalhe que liga diretamente à aula anterior: se um pivô for um número muito pequeno (perto de zero), dividir por ele amplia qualquer erro de arredondamento já presente nos coeficientes — o mesmo mecanismo de condicionamento visto na aula 01. Por isso, implementações cuidadosas de eliminação de Gauss reordenam as equações a cada etapa para usar, como pivô, o maior coeficiente disponível na coluna (**pivotamento parcial**) — não muda a solução do sistema, só evita amplificar erro numérico ao longo do processo.

### Gauss-Seidel: resolver de forma iterativa

Para sistemas muito grandes — inversão geofísica, ou malhas de simulação de fluxo de água subterrânea com uma equação por célula — a eliminação de Gauss fica cara demais: o número de operações cresce com o **cubo** do número de incógnitas. O **Gauss-Seidel** ataca de outro jeito: reescreve cada equação isolando sua própria incógnita em função das demais, parte de um palpite inicial (todas em zero, por exemplo) e recalcula cada incógnita, uma de cada vez, com os valores mais atualizados das outras — inclusive os já recalculados na mesma repetição. Repete até os valores pararem de mudar de forma significativa.

> [!tip] Uma analogia Pense em três amigos dividindo uma conta de forma que cada um deve pagar de acordo com o que os outros dois pagaram (uma regra circular, não uma divisão simples). Ninguém sabe o valor exato de cara, mas cada um pode chutar um valor inicial e ir ajustando o próprio pagamento com base no que os outros dois anunciaram por último — repetindo esse ajuste algumas rodadas, os três valores convergem para a divisão correta, mesmo que ninguém tenha calculado a resposta final de uma vez.

### Quando Gauss-Seidel converge — e quando não converge

Gauss-Seidel nem sempre converge: em alguns sistemas os valores oscilam cada vez mais longe da solução. Existe uma condição **suficiente** — garante convergência quando satisfeita, mas sua ausência não prova que o método vá falhar — chamada **dominância diagonal**: em cada equação, o coeficiente da própria incógnita daquela equação precisa ser, em valor absoluto, maior que a soma dos valores absolutos dos demais coeficientes dela. Sistemas de balanço de massa e de fluxo, em que cada incógnita depende sobretudo de si mesma e só secundariamente das vizinhas, tendem a satisfazer isso naturalmente — daí Gauss-Seidel ser tão usado em simulação de fluxo subterrâneo, onde cada célula troca água principalmente com as vizinhas imediatas.

### Matrizes mal condicionadas: quando o sistema em si é traiçoeiro

Retomando a aula 01: um sistema linear está **mal condicionado** quando duas ou mais equações são quase redundantes entre si — geometricamente, quando as retas (ou planos) que elas representam são quase paralelas. Aí um pequeno erro nos coeficientes ou nos termos independentes, como um erro de medição na composição de uma fonte, desloca o ponto de interseção — a solução — de forma desproporcional. Não é problema do método: é do próprio sistema, e nem Gauss nem Gauss-Seidel o resolvem. O remédio é obter dados mais independentes entre si, como traçadores que distingam melhor as fontes, não trocar de algoritmo.

## Exemplo trabalhado

**Situação — balanço de massa de três fontes sedimentares.** Um sedimento é mistura de três fontes (A, B, C). Um traçador químico X e um traçador Y, medidos na mistura e em cada fonte, e a condição de que as três frações somam 1, dão o sistema (frações a, b, c):

- 0,20a + 0,50b + 0,80c = 0,45 (traçador X)
- 0,70a + 0,30b + 0,10c = 0,40 (traçador Y)
- a + b + c = 1 (frações somam 100%)

**Passo 1 — eliminar *a*.** O objetivo é o mesmo do escalonamento descrito acima — fazer sumir uma incógnita das demais equações —, mas aqui isso sai mais rápido por substituição do que subtraindo múltiplos de uma equação das outras, porque a terceira equação já tem todos os coeficientes iguais a 1. Substituindo a = 1 − b − c nas duas primeiras, sobram duas equações só em *b* e *c*: 0,20(1−b−c) + 0,50b + 0,80c = 0,45 → 0,30b + 0,60c = 0,25; e 0,70(1−b−c) + 0,30b + 0,10c = 0,40 → −0,40b − 0,60c = −0,30, ou seja, 0,40b + 0,60c = 0,30.

**Passo 2 — eliminar mais uma incógnita.** Subtraindo a primeira equação reduzida da segunda: (0,40b + 0,60c) − (0,30b + 0,60c) = 0,30 − 0,25 → 0,10b = 0,05 → **b = 0,5**.

**Passo 3 — substituição regressiva.** Com b = 0,5, da equação 0,30b + 0,60c = 0,25: 0,15 + 0,60c = 0,25 → c = 0,10/0,60 ≈ **0,167**. Com b e c conhecidos, a = 1 − 0,5 − 0,167 ≈ **0,333**.

**Passo 4 — conferir.** a + b + c ≈ 0,333 + 0,5 + 0,167 = 1,0 ✓. As frações fazem sentido físico: todas entre 0 e 1, nenhuma negativa — um sistema mal condicionado, ou um erro de conta, frequentemente denuncia-se por uma fração negativa ou maior que 1.

**E se tentássemos Gauss-Seidel aqui?** Antes de aplicar, faça o que esta aula manda: cheque a dominância diagonal. Isolando *a* da equação de soma, *b* da equação X e *c* da equação Y, olhe a última — o coeficiente de *c* na equação Y é 0,10, contra 0,70 + 0,30 = 1,00 dos outros dois. É o **oposto** de dominância diagonal, e por larga margem. Aplicando Gauss-Seidel mesmo assim, a partir do palpite a=b=c≈0,33, os valores não se aproximam da solução: na terceira repetição *c* já passa de 67, na quinta passa de 6.500, e daí em diante disparam. O método **diverge**.

Esse é um resultado útil, não um fracasso do exemplo: mostra que a checagem da seção anterior não é formalidade. Gauss-Seidel é a ferramenta certa para sistemas **grandes** — dezenas de fontes e traçadores, ou uma malha de fluxo com milhares de células, onde cada incógnita depende principalmente de si mesma e pouco das vizinhas. Não é a ferramenta certa para *este* sistema de três equações, que a eliminação de Gauss resolve exatamente em quatro passos.

## Erros comuns

- **Aplicar Gauss-Seidel sem checar dominância diagonal e assumir que vai convergir.** Sem essa checagem, o método pode divergir silenciosamente — os valores parecem "quase certos" numa repetição e disparam na seguinte.
- **Ignorar o pivotamento na eliminação de Gauss.** Um pivô pequeno amplia o erro de arredondamento nas etapas seguintes — o condicionamento da aula 01, agora dentro do próprio algoritmo.
- **Aceitar sem investigar uma fração negativa ou maior que 1 num problema de mistura.** Um resultado fisicamente impossível costuma apontar erro nos dados de entrada ou sistema mal condicionado, não um resultado válido "só que estranho".
- **Confundir “o sistema não tem solução única” com “o método falhou”.** Um sistema com equações redundantes ou contraditórias não tem solução única (ou não tem solução nenhuma) independentemente do método usado para tentar resolvê-lo.

## O que não concluir

- **Que esta aula ensina decomposição LU, ou os métodos especializados para sistemas esparsos muito grandes (como gradiente conjugado), usados em inversão geofísica de larga escala.** Ficam para um tratamento mais avançado de álgebra linear numérica.
- **Que dominância diagonal é uma condição necessária para Gauss-Seidel convergir.** É **suficiente** (garante convergência quando presente), mas alguns sistemas sem dominância diagonal convergem de qualquer forma — a ausência da condição não permite concluir, sozinha, que o método vai falhar.

## Recap relâmpago

- **Eliminação de Gauss** é um método direto: escalona o sistema até a forma triangular, depois resolve por substituição regressiva de trás para frente.
- **Pivotamento** (usar o maior coeficiente disponível como pivô) evita amplificar erro de arredondamento durante a eliminação — ligação direta com o condicionamento da aula 01.
- **Gauss-Seidel** é um método iterativo: parte de um palpite e refina cada incógnita usando os valores mais recentes das demais, repetição após repetição, até convergir.
- **Dominância diagonal** garante a convergência de Gauss-Seidel; sua ausência não garante divergência, mas exige checar a convergência de outra forma (por exemplo, observando se o resultado para de mudar).
- Um sistema **mal condicionado** (equações quase redundantes) amplifica erro de entrada na solução, independentemente do método escolhido — o remédio é melhorar os dados, não trocar de algoritmo.

## Próxima aula

[[30-metodos-numericos-geociencias-aula-03-zeros-de-funcoes|Aula 03 — Zeros de funções: bisseção, Newton-Raphson e critérios de parada]]

## Anterior

[[30-metodos-numericos-geociencias-aula-01-erro-numerico|Aula 01 — Erro numérico]]

## Fontes

- Eliminação de Gauss, pivotamento parcial e substituição regressiva: Chapra, S. C. & Canale, R. P., *Numerical Methods for Engineers*, 7ª ed., McGraw-Hill, capítulos sobre eliminação de Gauss.
- Gauss-Seidel e dominância diagonal como condição suficiente de convergência: Chapra & Canale, *Numerical Methods for Engineers*, 7ª ed., capítulo sobre métodos iterativos para sistemas lineares; Burden, R. L. & Faires, J. D., *Numerical Analysis*, 9ª ed., Cengage.
- Balanço de massa de mistura de fontes sedimentares como sistema linear: aplicação padrão de traçadores geoquímicos em proveniência sedimentar (uso didático consolidado em geoquímica de sedimentos).

<!--
nivel: ensino-medio-sem-geologia-v1
palavras_corpo: 1600
bridge_lesson: true

mapa_objetivo_secao:
  geologia-m30-oa02: "Onde sistemas lineares aparecem em geociências" + "Eliminação de Gauss: resolver de forma direta" + "Gauss-Seidel: resolver de forma iterativa" + "Quando Gauss-Seidel converge — e quando não converge" + "Matrizes mal condicionadas: quando o sistema em si é traiçoeiro" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEO-M30-A02-GAUSS-DIRETO-001
    claim: "A eliminação de Gauss resolve sistemas lineares em duas etapas: escalonamento (redução à forma triangular por eliminação sucessiva de incógnitas) seguido de substituição regressiva (resolução da última equação e substituição sucessiva nas anteriores)."
    risk: fato
    source: "Chapra & Canale, Numerical Methods for Engineers, 7ª ed., cap. sobre eliminação de Gauss"
  - claim_id: GEO-M30-A02-PIVOTAMENTO-002
    claim: "O pivotamento parcial (reordenar equações para usar o maior coeficiente disponível como pivô) reduz a amplificação de erro de arredondamento durante a eliminação de Gauss, sem alterar a solução exata do sistema."
    risk: fato
    source: "Chapra & Canale, Numerical Methods for Engineers, 7ª ed.; Burden & Faires, Numerical Analysis, 9ª ed."
  - claim_id: GEO-M30-A02-GAUSS-SEIDEL-003
    claim: "O método de Gauss-Seidel é um método iterativo para sistemas lineares que recalcula cada incógnita usando os valores mais recentes disponíveis das demais (incluindo os já atualizados na mesma iteração), partindo de um palpite inicial e repetindo até convergência."
    risk: fato
    source: "Chapra & Canale, Numerical Methods for Engineers, 7ª ed., cap. sobre métodos iterativos; Burden & Faires, Numerical Analysis, 9ª ed."
  - claim_id: GEO-M30-A02-DOMINANCIA-DIAGONAL-004
    claim: "A dominância diagonal estrita (o coeficiente da diagonal de cada equação maior, em valor absoluto, que a soma dos valores absolutos dos demais coeficientes da mesma equação) é uma condição suficiente, mas não necessária, para a convergência do método de Gauss-Seidel."
    risk: fato
    source: "Burden & Faires, Numerical Analysis, 9ª ed., cap. sobre métodos iterativos para sistemas lineares"
  - claim_id: GEO-M30-A02-CUSTO-COMPUTACIONAL-005
    claim: "O custo computacional da eliminação de Gauss cresce aproximadamente com o cubo do número de incógnitas do sistema, tornando métodos iterativos como Gauss-Seidel preferíveis para sistemas grandes e esparsos, como os que surgem em malhas de simulação de fluxo subterrâneo e em inversão geofísica de larga escala."
    risk: fato
    source: "Chapra & Canale, Numerical Methods for Engineers, 7ª ed., cap. sobre custo computacional de métodos diretos vs. iterativos"

nota_trilha_apoio: >-
  Aula 2 de 5 do módulo 30 (trilha de apoio, opcional, não bloqueante), criada em
  2026-08-29. Retoma o condicionamento da aula 01 aplicado a sistemas lineares
  quase redundantes, e ancora Gauss-Seidel em balanço de massa geoquímico e
  malhas de fluxo subterrâneo/inversão geofísica.
-->
