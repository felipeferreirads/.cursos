# Aula 03: Operações de simetria II — rotoinversão e combinação de elementos

**ID:** mineralogia-m04-a03
**Módulo:** [[04-simetria-e-morfologia-modulo|Módulo 04 — Simetria e morfologia cristalina: operações, classes e sistemas]]
**Duração estimada:** ~30-32 min (com ponto de pausa)
**Nível:** ensino médio, sem geologia prévia (contrato `ensino-medio-sem-geologia-v1`)
**Objetivo:** reconhecer eixos de rotoinversão (1̄, 2̄, 3̄, 4̄, 6̄), saber quais deles equivalem a combinações de elementos já conhecidos, e aplicar as regras de combinação que fazem os elementos de simetria aparecerem juntos.
**Pré-requisito:** [[04-simetria-e-morfologia-aula-02-operacoes-de-simetria-i-rotacao-reflexao-e-inversao|Aula 02]] (rotação, espelho e centro).

## Vocabulário desta aula

| Termo | O que quer dizer |
|---|---|
| **rotoinversão** | operação composta: girar 360°/n em torno de um eixo e, em seguida, inverter pelo centro. |
| **eixo de rotoinversão (n̄)** | eixo em torno do qual a rotoinversão deixa o cristal indistinguível; lê-se "n barra". |
| **eixo próprio / impróprio** | o de rotação pura (próprio) não troca a "mão" do objeto; o de rotoinversão (impróprio) troca. |
| **n/m** | notação para um eixo de ordem n com um espelho perpendicular a ele (lê-se "n sobre m"). |
| **disfenoide** | sólido de quatro faces triangulares em que pares de faces de cima e de baixo se cruzam, como um tetraedro "achatado" ou "esticado". |

## Antes de começar, você precisa saber

- Eixos de rotação 1, 2, 3, 4, 6; espelho (m); centro (1̄); o teste "cada face cai sobre uma equivalente": [[04-simetria-e-morfologia-aula-02-operacoes-de-simetria-i-rotacao-reflexao-e-inversao|aula 02]].
- Que o centro leva (*x*, *y*, *z*) a (−*x*, −*y*, −*z*).

## Ao final você vai conseguir

- `mineralogia-m04-oa02` — Identificar operações e elementos de simetria (rotação, reflexão, inversão, rotoinversão) num cristal ou modelo. *(Esta aula completa o objetivo com a rotoinversão e as regras de combinação.)*

## Conteúdo

### Girar e inverter

A **rotoinversão** de ordem *n* é feita em dois tempos: gira-se a face 360°/*n* em torno do eixo e, em seguida, inverte-se pelo centro do cristal. O resultado tem de cair sobre uma face equivalente. Repetindo a operação até voltar ao início, obtém-se o conjunto de faces gerado pelo eixo n̄.

O ponto que trava os alunos é que **o centro sozinho não precisa ser um elemento de simetria do cristal**: ele é só o ponto de passagem da operação composta. Num eixo 4̄, nem o giro de 90° sozinho nem a inversão sozinha deixam o cristal igual; só a combinação dos dois.

### Os cinco eixos de rotoinversão, um a um

Como só existem rotações de ordem 1, 2, 3, 4 e 6, só existem cinco rotoinversões. Três delas não são novidade:

| Eixo | O que faz | Equivale a | Observação |
|---|---|---|---|
| **1̄** | gira 360° (nada) e inverte | **centro de inversão** | é por isso que o centro se escreve 1̄ |
| **2̄** | gira 180° e inverte | **espelho perpendicular ao eixo** (m) | na prática, escreve-se m |
| **3̄** | gira 120° e inverte | **eixo 3 + centro** | gera 6 faces, em dois grupos de 3 alternados em cima e embaixo |
| **4̄** | gira 90° e inverte | **operação nova**: contém um eixo 2 na mesma direção, mas nem eixo 4 nem centro | gera 4 faces, 2 em cima e 2 embaixo, cruzadas: um disfenoide |
| **6̄** | gira 60° e inverte | **eixo 3 com espelho perpendicular** (3/m) | gera 6 faces, 3 em cima e as mesmas 3 refletidas embaixo |

Duas equivalências merecem ser verificadas no papel, porque viram ferramentas:

- **2̄ = m.** Uma face no alto, à direita, girada 180° vai para o alto, à esquerda; invertida pelo centro, vai para baixo, à direita, exatamente onde o reflexo da face original num espelho horizontal a colocaria.
- **6̄ = 3/m.** Seis passos de 60° com inversão alternam entre o hemisfério de cima e o de baixo; o resultado é um conjunto de 3 faces em cima, a 120° umas das outras, cada uma com seu reflexo exato embaixo.

O **4̄** é a única rotoinversão que não se reduz a elementos anteriores. Ele aparece nos cristais em forma de **disfenoide**: duas faces em cima, formando uma aresta horizontal, e duas embaixo, formando outra aresta horizontal girada de 90° em relação à de cima. É o hábito típico da calcopirita, um sulfeto de cobre e ferro. Gire esse sólido 90° em torno do eixo vertical: ele **não** coincide consigo mesmo. Agora inverta pelo centro: coincide. E um giro de 180° também funciona; por isso todo eixo 4̄ contém um eixo 2.

*Figura sugerida: um disfenoide tetragonal visto de lado e de cima, com a sequência de quatro posições de uma face (gira 90° → inverte → gira 90° → inverte). O que observar: a face alterna entre cima e embaixo, e as arestas de cima e de baixo ficam cruzadas.*

> [!question] Pare e explique
> Um cristal com eixo 3̄ tem centro de simetria. Um cristal com eixo 4̄ não tem. Use a tabela para explicar a diferença.

Os eixos 1, 2, 3, 4 e 6 são **próprios**: não trocam a "mão" do objeto. Os eixos 1̄, 2̄ (= m), 3̄, 4̄ e 6̄ são **impróprios**: trocam. Isso completa a regra da aula 02: um cristal é quiral (existe em versão direita e esquerda) quando **não tem nenhum elemento impróprio**, ou seja, nem centro, nem espelho, nem 3̄, 4̄ ou 6̄.

### Os elementos não andam sozinhos: regras de combinação

> [!tip] Ponto de pausa
> Se a rotoinversão pesou, pare aqui e retome numa segunda sessão. As regras abaixo só usam o que já foi visto.

Se um cristal tem dois elementos de simetria, aplicar um depois do outro também é uma operação de simetria. Isso faz certos elementos **gerarem** outros. Quatro regras resolvem quase todos os casos:

1. **Eixo de ordem par + espelho perpendicular ⇒ centro.** Um eixo 2 com um espelho perpendicular a ele obriga a existência de um centro no cruzamento. Vale também em qualquer combinação de dois: eixo par + centro ⇒ espelho perpendicular; espelho + centro ⇒ eixo 2 perpendicular ao espelho. Notação: **2/m, 4/m, 6/m**.
2. **Dois espelhos que se cruzam ⇒ eixo de rotação na linha de cruzamento**, com giro igual ao dobro do ângulo entre eles. Dois espelhos a 90° geram um eixo 2; a 60°, um eixo 3; a 45°, um eixo 4; a 30°, um eixo 6.
3. **Eixo de ordem n + um espelho que o contém ⇒ n espelhos** contendo o eixo (o eixo "copia" o espelho a cada giro). Um eixo 4 com um espelho vertical tem 4 espelhos verticais (dois pares, a 45° um do outro).
4. **Eixo de ordem n + um eixo 2 perpendicular ⇒ n eixos 2 perpendiculares.** Um eixo 3 com um eixo 2 perpendicular tem 3 eixos 2 perpendiculares a 120°.

Essas regras explicam por que a lista do cubo (aula 02) é tão longa: bastam poucos elementos de partida, e o resto é consequência. Explicam também por que não existem combinações arbitrárias: a maioria das misturas de elementos gera outros até fechar um conjunto coerente. Esses conjuntos fechados são as **classes de simetria** da aula 04.

## Exemplo trabalhado

**Problema.** Um cristal tem um eixo de ordem 4 vertical e um plano de simetria vertical que contém esse eixo. Nenhum outro elemento foi observado ainda. Que outros elementos ele **tem de** ter? Há centro?

**Passo 1. Regra 3 (eixo + espelho que o contém).** O eixo 4 gira o espelho de 90° em 90°: aparecem espelhos a 0°, 90°, 180° e 270°. Como um espelho a 180° é o mesmo plano que o de 0°, sobram **2 espelhos** a 90° entre si.

**Passo 2. Regra 2 (dois espelhos que se cruzam).** Dois espelhos verticais a 90° geram um eixo 2 vertical, que já está contido no eixo 4. Nada novo.

**Passo 3. Os espelhos diagonais.** A regra 2 lida ao contrário também vale: um eixo 4 é o que dois espelhos a 45° geram. Compondo o giro de 90° com a reflexão num dos espelhos, obtém-se a reflexão num plano a 45° dele. Resultado: mais **2 espelhos diagonais**. Total: **4 espelhos verticais**.

**Passo 4. Centro?** Nenhum espelho é perpendicular ao eixo 4, e nenhuma regra obriga um centro. Sem mais informação, **não há centro**. Lista: A₄ 4P. Na notação da aula 04, isso será **4mm**.

**Passo 5. Teste de coerência.** Um cristal assim tem a ponta de cima diferente da de baixo, como uma pirâmide de base quadrada. Isso bate com a falta de centro e de espelho horizontal.

**Método geral:** liste os elementos observados, aplique as regras de combinação até nada novo aparecer e só então afirme a presença ou a ausência de centro.

## Erros comuns

- **Achar que um eixo 4̄ implica um centro**, porque a operação "passa pelo centro". É a confusão mais frequente da aula: o centro é ponto de passagem da operação composta, não elemento do cristal.
- **Contar 2̄ como elemento à parte.** Ele é o espelho perpendicular; contar os dois é contar duas vezes a mesma coisa.
- **Parar na lista observada.** Elementos observados implicam outros; um cristal com eixo 2 e espelho perpendicular tem centro, mesmo que você não o tenha procurado.
- **Esquecer que espelhos "copiados" a 180° coincidem.** Um eixo 4 multiplica um espelho por 2 pares (4 espelhos), não por 4 pares.

## O que não concluir

- Que todo cristal sem centro seja quiral. Um cristal com 4̄ ou com espelho não tem centro e não é quiral.
- Que a regra 1 valha para eixos de ordem ímpar. Um eixo 3 com espelho perpendicular não gera centro: é 3/m = 6̄.
- Que as regras gerem simetria "a mais" no cristal real. Elas dizem o que **tem de** estar lá se os elementos de partida estiverem; se o elemento gerado não existir, um dos elementos de partida foi mal identificado.

## Recap relâmpago

- Rotoinversão = girar 360°/n e inverter; cinco eixos: 1̄, 2̄, 3̄, 4̄, 6̄.
- 1̄ = centro; 2̄ = m; 3̄ = 3 + centro; 6̄ = 3/m; 4̄ é operação própria nova (contém 2, sem 4 e sem centro).
- Elementos impróprios (centro, m, 3̄, 4̄, 6̄) trocam a "mão"; sem nenhum deles, o cristal é quiral.
- Eixo par + espelho perpendicular ⇒ centro (n/m).
- Dois espelhos a θ ⇒ eixo de giro 2θ; eixo n + espelho ou eixo 2 ⇒ n espelhos ou n eixos 2.

## Próxima aula

Em [[04-simetria-e-morfologia-aula-04-os-32-grupos-pontuais-e-a-notacao-de-hermann-mauguin-parte-1-deducao|Aula 04 — Os 32 grupos pontuais, Parte 1]], as regras de combinação fecham-se em exatamente 32 conjuntos possíveis, e você aprende a escrevê-los no símbolo de Hermann-Mauguin.

## Fontes consultadas

- Klein, C. & Dutrow, B., *Manual of Mineral Science*, 23ª ed., Wiley (rotoinversão; combinações de elementos de simetria).
- Nesse, W. D., *Introduction to Mineralogy*, Oxford University Press (eixos de rotoinversão; teoremas de combinação).
- *International Tables for Crystallography*, vol. A, IUCr (operações próprias e impróprias; equivalências 1̄ = centro, 2̄ = m, 6̄ = 3/m).
- Mindat, "Chalcopyrite" (classe 4̄2m; hábito disfenoidal), consultado em 2026-10-04.

<!--
nivel: ensino-medio-sem-geologia-v1
palavras_corpo: 1458
cobertura:
  mineralogia-m04-oa02: [Conteúdo, Exemplo trabalhado]
alegacoes_auditaveis:
  - claim_id: CRI-ROT-EQUIV-001
    claim: "1-barra = centro; 2-barra = espelho perpendicular; 3-barra = eixo 3 + centro; 6-barra = 3/m; 4-barra e operacao nova que contem eixo 2, sem eixo 4 e sem centro."
    risk: conceito
    source: "International Tables vol. A; Klein & Dutrow"
    audit: "verificado em 2026-10-04"
  - claim_id: CRI-ROT-FACES-001
    claim: "3-barra gera 6 faces (3 em cima, 3 embaixo alternadas); 4-barra gera 4 faces em disfenoide; 6-barra gera 6 faces (3 em cima refletidas embaixo)."
    risk: numero
    source: "Klein & Dutrow"
    audit: "verificado em 2026-10-04"
  - claim_id: CRI-ROT-CALCOP-001
    claim: "A calcopirita tem habito tipico disfenoidal (classe 4-barra 2m)."
    risk: fato
    source: "Mindat; Klein & Dutrow"
    audit: "verificado em 2026-10-04"
  - claim_id: CRI-ROT-QUIRAL-001
    claim: "Um cristal e quiral quando nao tem nenhum elemento improprio (centro, m, 3-barra, 4-barra, 6-barra)."
    risk: conceito
    source: "International Tables vol. A"
    audit: "verificado em 2026-10-04"
  - claim_id: CRI-COMB-REGRAS-001
    claim: "Eixo par + espelho perpendicular => centro (e quaisquer dois implicam o terceiro); dois espelhos a theta => eixo de giro 2 theta; eixo n + espelho que o contem => n espelhos; eixo n + eixo 2 perpendicular => n eixos 2."
    risk: conceito
    source: "Klein & Dutrow; Nesse"
    audit: "verificado em 2026-10-04"
  - claim_id: CRI-COMB-EXEMPLO-001
    claim: "Eixo 4 + um espelho vertical gera 4 espelhos verticais (dois pares a 45 graus), sem centro: classe 4mm."
    risk: conceito
    source: "deducao; International Tables vol. A"
    audit: "verificado em 2026-10-04"
  - claim_id: CRI-COMB-IMPAR-001
    claim: "Eixo 3 com espelho perpendicular nao gera centro: e 3/m = 6-barra."
    risk: conceito
    source: "International Tables vol. A"
    audit: "verificado em 2026-10-04"
-->
