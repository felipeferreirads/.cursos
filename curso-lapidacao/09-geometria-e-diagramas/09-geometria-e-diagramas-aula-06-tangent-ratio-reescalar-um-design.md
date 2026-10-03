# Aula 06: Tangent ratio — reescalar um design para outro índice de refração

**ID:** lapidacao-m09-a06
**Módulo:** [[09-geometria-e-diagramas-modulo|Módulo 09]] — Geometria da máquina e leitura de diagramas de lapidação
**Duração estimada:** ~28 min
**Objetivo:** aplicar a fórmula do tangent ratio para converter um design entre índices de refração e declarar os limites do método.
**Pré-requisito:** [[09-geometria-e-diagramas-aula-03-anatomia-de-um-diagrama-de-lapidacao|Aula 03]] deste módulo (a tabela de um diagrama, com o ângulo e os índices de cada fileira); [[08-optica-do-facetado-aula-02-angulos-alvo-por-indice-de-refracao|Aula 02 do módulo 08]] deste curso (ângulos-alvo publicados por material, não por fórmula única). Módulo 01 do curso de Gemologia (índice de refração), citado por nome.

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **tangente** | numa relação entre um ângulo e os lados de um triângulo retângulo, a razão entre o cateto oposto e o cateto adjacente a esse ângulo; cresce de 0 a infinito conforme o ângulo vai de 0° a 90°, e não cresce de forma linear. |
| **tangent ratio** | a razão entre a tangente de um ângulo de referência convertido e a tangente do mesmo ângulo de referência no design original; usada para reescalar todos os outros ângulos do design. |
| **faceta de referência** | a faceta escolhida para ancorar a conversão — em geral a main do pavilhão, cujo novo ângulo-alvo já é conhecido. |
| **vista em planta (planview)** | o contorno da pedra visto de cima — a mesma **vista de topo** da aula 03, aqui pelo nome que a literatura de conversão usa; o tangent ratio muda a inclinação das facetas sem alterar esse contorno. |
| **reescalar** | ajustar todos os ângulos de um design de forma proporcional, mantendo a mesma vista em planta. |

## Antes de começar, você precisa saber

- Da [[09-geometria-e-diagramas-aula-03-anatomia-de-um-diagrama-de-lapidacao|Aula 03]] deste módulo: a tabela de um diagrama traz o ângulo e os índices de cada fileira — a profundidade não vem tabelada; a vista de topo mostra a posição angular (índice) de cada faceta, e a vista lateral mostra a inclinação (ângulo).
- Da [[08-optica-do-facetado-aula-02-angulos-alvo-por-indice-de-refracao|Aula 02 do módulo 08]]: os ângulos-alvo publicados vêm **por material**, não de uma fórmula única — quartzo 42°, berilo 43°, coríndon 42°, entre outros — e a margem sobre o ângulo crítico cresce com o índice de refração.
- Não é preciso saber trigonometria além do que esta aula reativa a seguir.

## Ao final você vai conseguir

- `lapidacao-m09-oa06` — Aplicar a fórmula do tangent ratio para converter um design entre índices de refração e declarar os limites do método.

## Conteúdo

### O problema: um design bom, um material diferente

Um design de talhe publicado — com todas as suas facetas, ângulos e índices já resolvidos e testados — representa muito trabalho: alguém escolheu a simetria, ajustou cada fileira, verificou que os meetpoints fecham. Quando esse mesmo desenho precisa ser cortado noutro material, de índice de refração diferente, refazer tudo do zero desperdiçaria esse trabalho. A aula 02 do módulo 08 já mostrou que o ângulo-alvo certo muda de material para material — não por uma fórmula simples, mas por valores publicados individualmente. A pergunta desta aula é: existe um jeito de pegar um design pronto, feito para um material, e **reescalá-lo** inteiro para outro, sem recalcular faceta por faceta a partir do zero?

A resposta da literatura de facetamento é sim, e o método se chama **tangent ratio**.

### Reativando a tangente

Antes da fórmula, uma pausa de matemática. Num triângulo retângulo, a **tangente** de um dos ângulos (que não o ângulo reto) é a razão entre o cateto oposto a esse ângulo e o cateto adjacente a ele. É uma função que cresce conforme o ângulo cresce, mas **não de forma linear**: perto de 0°, a tangente cresce devagar; perto de 90°, ela dispara — a tangente de 89° já é dezenas de vezes maior que a de 45°, e a de 90° não existe (tende a infinito). Essa curvatura é o motivo pelo qual **somar um número fixo de graus a todos os ângulos de um design não é o mesmo que reescalá-lo corretamente** — um mesmo incremento de graus representa uma mudança de inclinação bem diferente perto de 20° e perto de 70°.

### A ideia central: preservar a vista em planta, mudar só a inclinação

A aula 03 separou a vista de topo (posição angular — índice) da vista lateral (inclinação — ângulo). O tangent ratio atua **só** na vista lateral: ele reescala os ângulos de todas as facetas — mudando o quanto elas são deitadas ou em pé, e por consequência a altura de cada uma — enquanto mantém a vista de topo, e portanto o contorno e a simetria do talhe, exatamente como estavam. Índice não muda; ângulo e altura mudam juntos, proporcionalmente.

Para que essa proporção seja consistente entre facetas de ângulos diferentes, a conversão precisa ser feita **pela razão das tangentes**, não pela diferença simples de graus — é essa razão que o nome do método declara.

### A fórmula

Escolhe-se uma **faceta de referência** — em geral a main do pavilhão, cujo novo ângulo-alvo já é conhecido pela tabela de ângulos-alvo (aula 02 do módulo 08). Calcula-se a razão entre a tangente do novo ângulo dessa referência e a tangente do ângulo antigo dela — a **tangent ratio**, um único número, constante para a conversão inteira. Depois, aplica-se essa mesma razão a cada outro ângulo **da mesma seção**:

$$\text{ângulo}_{\text{novo}} = \arctan\left[\tan(\text{ângulo}_{\text{antigo}}) \times \frac{\tan(\text{ângulo}_{\text{ref, novo}})}{\tan(\text{ângulo}_{\text{ref, antigo}})}\right]$$

Em palavras: pega-se a tangente do ângulo antigo de uma faceta qualquer, multiplica-se pela razão constante calculada na referência, e converte-se o resultado de volta a um ângulo pelo arco-tangente. A mesma razão constante — calculada uma única vez, a partir da faceta de referência — é reaplicada às demais facetas.

Uma ressalva de escopo que a fonte faz e que é fácil perder: a conversão normalmente é feita **em separado para o pavilhão e para a coroa**, cada seção com a sua faceta de referência e a sua razão. Nada na matemática impede usar uma razão só para as duas; o que acontece na prática é que raramente se quer mexer nas duas na mesma medida.

### O que o método garante, e por que só a proporção das tangentes funciona

Facetas a 0° (paralelas à cinta, como a mesa) e a 90° (perpendiculares a ela) não mudam pelo método — suas tangentes são, respectivamente, zero e indefinida, e a razão não as desloca. Para os ângulos intermediários, a proporção das tangentes é exatamente o que preserva a vista de topo: como a inclinação de uma faceta e sua extensão horizontal no contorno estão ligadas pela tangente do ângulo, escalar as tangentes na mesma proporção escala a altura de cada faceta sem mexer em sua posição no contorno. Dito de outro jeito: a altura de uma faceta dividida pela sua base **é** a tangente do ângulo dela — a razão muda só essa altura, e a base de cada faceta permanece a mesma.

Esse é o ponto que separa o método do atalho que costuma ser confundido com ele: **a razão de tangentes preserva a vista em planta por construção, e não por aproximação** — o dicionário do ofício define o tangent ratio exatamente como o que traduz um conjunto de ângulos noutro *mantendo a vista em planta constante*. Somar um número fixo de graus a todos os ângulos é uma **aproximação** disso: boa enquanto os ângulos do design estiverem próximos uns dos outros, e cada vez pior conforme eles se espalham.

## Exemplo trabalhado

**Um design de pavilhão em quartzo (IR ≈ 1,54) tem uma faceta de referência (main) a 39° e uma faceta auxiliar a 42,3°. O talhe precisa ser reescalado para um ângulo-alvo de main de 42° — o valor publicado que a aula 02 do módulo 08 já registrou.**

**Passo 1 — a tangent ratio, a partir da referência.** $\tan(39°) \approx 0{,}8098$. $\tan(42°) \approx 0{,}9004$. Razão: $0{,}9004 \div 0{,}8098 \approx 1{,}1119$. Esse número — 1,1119 — é a constante que será aplicada a **todas** as demais facetas do design.

**Passo 2 — converter a faceta auxiliar.** $\tan(42{,}3°) \approx 0{,}9099$. Multiplicando pela razão: $0{,}9099 \times 1{,}1119 \approx 1{,}0118$. O novo ângulo é $\arctan(1{,}0118) \approx 45{,}33°$.

**Passo 3 — checar a não linearidade.** A referência subiu 3° (de 39° para 42°); a faceta auxiliar subiu cerca de 3,03° (de 42,3° para 45,33°) — quase o mesmo, mas não exatamente, porque a razão de tangentes, e não uma soma fixa de graus, é o que rege a conversão. Numa faceta bem mais íngreme do mesmo design a diferença salta: a mesma razão leva 68° a 70,03° — um deslocamento de 2,03°, não de 3°.

**Passo 4 — a lição do exemplo.** Uma única razão, calculada a partir de uma faceta de referência, reescala o design inteiro — mas o resultado não é "somar 3° em tudo": é a proporção das tangentes que preserva a vista de topo, e ela desloca cada ângulo por uma quantidade de graus ligeiramente diferente conforme sua posição na curva não linear da tangente.

## Erros comuns

- **Somar a mesma diferença de graus a todos os ângulos.** Não é o mesmo que aplicar a tangent ratio — a tangente não é linear, e essa aproximação só é aceitável para variações pequenas de ângulo.
- **Achar que o método muda o índice ou o contorno do talhe.** O tangent ratio atua só na inclinação (e, por consequência, na altura); a vista de topo — e a simetria que ela declara — permanece a mesma.
- **Achar que é o tangent ratio que se degrada num design de grande espalhamento angular.** É o contrário. A conversão pela razão de tangentes preserva a vista em planta **por construção**, qualquer que seja o espalhamento. Quem se degrada é o **atalho** de somar um número fixo de graus a todos os ângulos: quanto maior a diferença entre o ângulo mais raso e o mais íngreme do design — o que é típico dos designs mais complexos —, mais esse atalho se afasta da conversão correta, e é ele que produz desvios visíveis na vista em planta e problemas nos pontos de encontro.
- **Esquecer que a razão vem de uma faceta de referência específica.** Trocar a referência — usar uma faceta diferente para calcular a razão — muda o resultado de toda a conversão.

## O que não concluir

- Não concluir de onde vem o novo ângulo-alvo da faceta de referência — ele ainda vem da tabela de ângulos-alvo por material, tema da aula 02 do módulo 08, não de um cálculo do tangent ratio.
- Não concluir que o tangent ratio substitui a modelagem por ray tracing (aula 06 do módulo 08) como verificação final de um design reescalado — ele é um atalho geométrico, não uma simulação óptica completa.
- Não concluir como aplicar essa conversão na prática, numa facetadora real — competência de bancada, fora do escopo teórico deste curso.

## Recap relâmpago

- O **tangent ratio** reescala um design de talhe inteiro para outro índice de refração sem recalcular cada faceta do zero, mantendo a vista de topo (contorno e simetria) e mudando só a inclinação.
- A **tangente** cresce de forma **não linear** com o ângulo — por isso somar graus fixos não substitui a razão de tangentes.
- Fórmula: $\text{ângulo}_{\text{novo}} = \arctan\left[\tan(\text{ângulo}_{\text{antigo}}) \times \dfrac{\tan(\text{ângulo}_{\text{ref, novo}})}{\tan(\text{ângulo}_{\text{ref, antigo}})}\right]$ — a razão vem de uma faceta de referência (em geral a main do pavilhão) e é reaplicada às demais facetas **da mesma seção**; pavilhão e coroa são normalmente convertidos em separado.
- Facetas a 0° e a 90° não mudam pelo método; o novo ângulo da referência ainda vem da tabela de ângulos-alvo por material, não de uma fórmula.
- O que perde precisão com um grande espalhamento de ângulos **não é o tangent ratio** — é o atalho de somar graus fixos, que diverge dele e aí sim deforma a vista em planta e os pontos de encontro. A conversão pela razão de tangentes preserva a vista em planta por construção. E o método não substitui a verificação por ray tracing.

## Próxima aula

Encerra o módulo 09. O módulo 10 — Famílias de talhe facetado — retoma o vocabulário de fileira, main e break desta anatomia de diagrama para caracterizar brilhante, degrau e misto pelo arranjo geométrico de suas facetas.

## Fontes consultadas

- United States Faceters Guild, *Gemstone Design Conversion Using the Tangent Ratio Method* — a fórmula literal ("angle xnew = tan⁻¹{tan(angle xoriginal) * [(tan(angle refnew) / tan(angle reforiginal)]}"); o exemplo numérico completo (referência 39° → 42°; 42,3° → 45,3348°; 43,9° → 46,9371°; 68° → 70,0307°), reconferido por cálculo direto nesta auditoria; a regra "all of the angles on a pavilion or crown must be scaled proportionately in order to preserve its original planview"; a ressalva de que a coroa "normally gets done as a separate and independent conversion from the pavilion angles"; a nota de que facetas a 0° e 90° "remain at 0° or 90° and do not need to be converted"; e — decisivo — a advertência de que o que se degrada com o espalhamento angular é **o atalho**, não o método: "as the spread between the lowest and highest pavilion or crown angles increases… **the practice of adding a constant difference to the angles** breaks down and the results diverge from a tangent ratio conversion. This can cause noticeable deviations in the planview and may also have ramifications for meet points". Consultada em 2026-09-06.
- United States Faceters Guild, *dicionário de facetamento* — definição de tangent ratio como a razão entre a tangente de um ângulo e a tangente de um segundo ângulo, usada para traduzir um conjunto de ângulos noutro mantendo a vista em planta.
- International Gem Society, *Tangent Ratioing* — corroboração do método e de seu uso na conversão de designs entre materiais de índice de refração diferente. Consultada em 2026-09-06.
- [[08-optica-do-facetado-aula-02-angulos-alvo-por-indice-de-refracao|módulo 08, aula 02]] deste curso — os ângulos-alvo por material usados como referência de conversão, reativados nesta aula.

<!--
nivel: ensino-medio-com-gemologia-v1
palavras_corpo: 1594
cobertura:
  lapidacao-m09-oa06: [Conteúdo, "Exemplo trabalhado", "Erros comuns", "Recap relâmpago"]
alegacoes_auditaveis:
  - claim_id: TGR-TAN-NAOLIN-001
    claim: "A tangente de um angulo, num triangulo retangulo, e a razao entre o cateto oposto e o cateto adjacente a esse angulo; ela cresce de 0 a infinito conforme o angulo vai de 0 a 90 graus, de forma NAO linear — cresce devagar perto de 0 grau e dispara perto de 90 graus. Por isso somar um numero fixo de graus a todos os angulos de um design nao equivale a reescala-lo pela razao de tangentes."
    risk: fato tecnico
    source: "United States Faceters Guild, dicionario de facetamento (tangent ratio) e Gemstone Design Conversion Using the Tangent Ratio Method ('the tangent function is not linear')"
  - claim_id: TGR-METODO-DEF-001
    claim: "O tangent ratio e o metodo de reescalar um design de talhe inteiro entre indices de refracao diferentes preservando a vista em planta (indice/contorno) e mudando so a inclinacao (angulo) e, por consequencia, a altura de cada faceta. A conversao usa uma faceta de referencia (tipicamente a main do pavilhao) cujo novo angulo-alvo ja e conhecido; a razao entre a tangente do novo angulo da referencia e a tangente do angulo antigo dela e calculada uma unica vez e reaplicada as demais facetas DA MESMA SECAO. RESSALVA DE ESCOPO: a conversao e normalmente feita em separado para o pavilhao e para a coroa, cada um com a sua faceta de referencia e a sua razao; nada na matematica impede uma razao unica para os dois, mas na pratica raramente se quer altera-los na mesma medida."
    risk: mecanismo
    source: "United States Faceters Guild, Gemstone Design Conversion Using the Tangent Ratio Method ('all of the angles on a pavilion or crown must be scaled proportionately in order to preserve its original planview'; 'if you do want to lower or raise the crown angles, that normally gets done as a separate and independent conversion from the pavilion angles'; 'there is no mathematical reason you can't calculate them together. However, in practice this circumstance is usually not the case'); International Gem Society, Tangent Ratioing. Verificado em 2026-09-06."
  - claim_id: TGR-FORMULA-DEF-001
    claim: "A formula do tangent ratio e: angulo_novo = arctan[tan(angulo_antigo) x (tan(angulo_ref_novo) / tan(angulo_ref_antigo))], onde a razao tan(angulo_ref_novo)/tan(angulo_ref_antigo) e constante para toda a conversao de um mesmo design."
    risk: dado numerico
    source: "United States Faceters Guild, Gemstone Design Conversion Using the Tangent Ratio Method (formula literal: 'angle xnew = tan-1{tan(angle xoriginal) * [(tan(angle refnew) / tan(angle reforiginal)]}')"
  - claim_id: TGR-EX-NUMERICO-001
    claim: "Exemplo numerico de conversao (quartzo, referencia de main de 39 para 42 graus): tan(39)=0,8098; tan(42)=0,9004; razao=0,9004/0,8098=1,1119. Para uma faceta auxiliar de 42,3 graus: tan(42,3)=0,9099; 0,9099 x 1,1119=1,0118; arctan(1,0118)=45,33 graus. CONFERIDO por calculo direto nesta auditoria: 45,3348 graus, coincidindo com o valor publicado pela fonte."
    risk: dado numerico
    source: "United States Faceters Guild, Gemstone Design Conversion Using the Tangent Ratio Method (exemplo numerico completo: 42,3 -> 45,3348; 43,9 -> 46,9371; 68 -> 70,0307); recalculo independente em 2026-09-06, resultados identicos."
  - claim_id: TGR-LIMITE-EXTREMOS-001
    claim: "Facetas a 0 grau (paralelas a cinta) e a 90 graus (perpendiculares a ela) permanecem inalteradas pelo tangent ratio, porque suas tangentes sao, respectivamente, zero e indefinida (tendendo a infinito), o que a razao constante nao altera de forma significativa."
    risk: consistencia interna
    source: "United States Faceters Guild, Gemstone Design Conversion Using the Tangent Ratio Method (comportamento nos extremos da funcao tangente)"
  - claim_id: TGR-LIMITE-ESPALHA-001
    claim: "INVERSAO CORRIGIDA. O que se degrada com o aumento do espalhamento angular de um design NAO e a conversao pelo tangent ratio — e o ATALHO de somar um numero fixo de graus a todos os angulos. A conversao pela razao de tangentes preserva a vista em planta POR CONSTRUCAO (o dicionario da USFG define o tangent ratio como o que traduz um conjunto de angulos noutro 'while holding the plan view constant'), qualquer que seja o espalhamento. Quanto maior a diferenca entre o angulo mais raso e o mais ingreme — tipico dos designs mais complexos —, mais a soma de graus fixos diverge da conversao correta, e e ESSA divergencia que causa desvios perceptiveis na vista em planta e problemas nos pontos de encontro."
    risk: causa-efeito
    source: "United States Faceters Guild, Gemstone Design Conversion Using the Tangent Ratio Method: 'as the spread between the lowest and highest pavilion or crown angles increases as is typical with more complex designs, THE PRACTICE OF ADDING A CONSTANT DIFFERENCE TO THE ANGLES breaks down and the results diverge from a tangent ratio conversion. This can cause noticeable deviations in the planview and may also have ramifications for meet points.'; USFG, dicionario de facetamento, verbete Tangent Ratio: 'used for translating one set of angles to another while holding the plan view constant'. Verificado em 2026-09-06."
-->
