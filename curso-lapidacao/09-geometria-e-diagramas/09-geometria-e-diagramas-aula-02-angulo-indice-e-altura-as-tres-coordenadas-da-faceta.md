# Aula 02: Ângulo, índice e altura — as três coordenadas de uma faceta

**ID:** lapidacao-m09-a02
**Módulo:** [[09-geometria-e-diagramas-modulo|Módulo 09]] — Geometria da máquina e leitura de diagramas de lapidação
**Duração estimada:** ~24 min
**Objetivo:** descrever as três coordenadas que definem uma faceta e identificar qual ajuste da máquina fixa cada uma.
**Pré-requisito:** [[09-geometria-e-diagramas-aula-01-o-sistema-de-indice-32-64-77-80-96-dentes|Aula 01]] deste módulo (o índice como roda dentada e a regra de simetria); [[03-maquinas-da-bancada-aula-05-anatomia-do-ajuste-batente-de-angulo-altura-do-mastro-e-o-cheater|Aula 05 do módulo 03]] deste curso (batente de ângulo, altura do mastro e as duas famílias de ajuste). Nenhum pré-requisito específico do curso de Gemologia.

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **coordenada** | um dos números independentes necessários para fixar completamente a posição de algo — aqui, de uma faceta. |
| **ângulo** | a inclinação da faceta em relação ao plano da cinta, fixada pelo batente de ângulo. |
| **índice** | a posição rotacional da faceta ao redor do eixo da pedra, fixada pela roda dentada — sempre a roda, nunca o índice de refração. |
| **altura** | a posição do conjunto braço-cabeçote ao longo do mastro, que fixa a profundidade e o alcance do corte. |
| **tier (fileira)** | um grupo de facetas na mesma altura ao redor da pedra — na prática, cortadas com o mesmo ângulo e a mesma altura do mastro, cada uma num índice diferente. |
| **independência de coordenada** | a propriedade de um sistema em que mudar uma coordenada não altera as outras. |

## Antes de começar, você precisa saber

- Da [[09-geometria-e-diagramas-aula-01-o-sistema-de-indice-32-64-77-80-96-dentes|Aula 01]] deste módulo: **índice** é sempre a roda dentada da facetadora, e a simetria de um talhe depende de quais números dividem o total de dentes.
- Da [[03-maquinas-da-bancada-aula-05-anatomia-do-ajuste-batente-de-angulo-altura-do-mastro-e-o-cheater|Aula 05 do módulo 03]]: os ajustes da facetadora se dividem em duas famílias — **batente de ângulo + altura do mastro** definem a faceta no plano radial (inclinação e profundidade); **índice + cheater** definem sua posição na volta (simetria). Esta aula nomeia as três grandezas que essas famílias produzem juntas.
- Não é preciso saber ainda como essas três grandezas aparecem organizadas numa tabela de diagrama — é a aula 03.

## Ao final você vai conseguir

- `lapidacao-m09-oa02` — Descrever as três coordenadas que definem uma faceta e identificar qual ajuste da máquina fixa cada uma.

## Conteúdo

### Por que uma faceta precisa de três números

Pense numa escada em caracol. Para marcar um degrau específico e voltar a ele depois, três informações bastam: em que **andar** ele fica, em que **direção** da escada ele aponta, e o quanto ele está **inclinado**. Falta qualquer uma das três e o degrau não está determinado — ele podia ser outro, no mesmo andar mas noutra direção, ou na mesma direção mas noutro andar.

Uma faceta plana, gerada pela facetadora, é exatamente esse tipo de objeto: um plano que precisa de posição **e** de orientação para estar completamente especificado. Dois números não bastam. É por isso que o módulo 08 já usava, de passagem, os nomes que esta aula desenvolve: o **GemCad** — o software mais citado para desenhar diagramas — especifica cada faceta por **ângulo, índice e uma distância do centro da pedra ao plano da faceta**, que é a forma que a terceira coordenada assume dentro do software. Na máquina, quem realiza essa terceira coordenada é a **altura do mastro**, e é por esse nome que este curso a trata.

### Ângulo — a inclinação

O **ângulo** é a grandeza que a Aula 05 do módulo 03 já nomeou: a inclinação da faceta em relação ao plano da cinta, fixada pelo **batente de ângulo**. Uma faceta a 42° e outra a 20° têm inclinações diferentes — uma mais deitada, outra mais em pé — mesmo que estejam exatamente na mesma posição da volta ao redor da pedra. O ângulo, sozinho, não diz **onde** na volta a faceta fica nem **quão fundo** o corte avança; ele só diz o quanto o plano está deitado.

### Índice — a posição na volta

O **índice** é a coordenada que a Aula 01 deste módulo tratou: a posição rotacional, travada pela roda dentada num dente específico. Duas facetas podem ter exatamente o mesmo ângulo e a mesma altura e ainda assim serem facetas diferentes, porque cada uma ocupa um ponto distinto da volta — é assim que um talhe com simetria 8-fold repete o mesmo grupo de facetas oito vezes, cada cópia num índice diferente, todas com o mesmo ângulo. O índice, sozinho, não diz **quão inclinada** a faceta é nem **quão fundo** o corte avança; ele só diz em que direção da volta ela aponta.

### Altura — a profundidade e o alcance

A terceira coordenada é a **altura do mastro**, também já nomeada na Aula 05 do módulo 03: a posição de todo o conjunto braço-cabeçote ao longo da coluna vertical. Com o batente travado no mesmo ângulo, subir ou descer o mastro não muda a inclinação da faceta — muda **até onde** o corte avança, ou seja, o tamanho da faceta e onde sua borda cai dentro do contorno da pedra. Cuidado com uma armadilha aqui: uma mesma faceta cortada a duas alturas diferentes, com o mesmo ângulo e o mesmo índice, **não** vira duas facetas. Os dois planos são paralelos, e o corte mais profundo consome o mais raso que estava na frente dele — sobra uma faceta só, a mais funda. Ângulo e índice, juntos, já localizam a faceta na pedra; a altura decide **quanto** dela existe.

### As três juntas, e por que nenhuma substitui as outras duas

Uma faceta plana está completamente especificada quando as três coordenadas estão fixadas: **ângulo** (quão inclinada), **índice** (em que direção da volta) e **altura** (quão profunda). Vale reconciliar aqui as duas metades da abertura: **ângulo e índice dão a orientação** do plano — para onde ele aponta —, e **a altura dá a posição** dele — a que distância do centro da pedra esse plano passa. É por isso que ângulo e índice bastam para dizer *qual* faceta do desenho é aquela, e ainda assim não bastam para descrever *o plano*: sem a altura, ele não tem onde ficar. Mudar qualquer uma das três sozinha, mantendo as outras duas, produz um resultado diferente e previsível:

- Mesmo ângulo e altura, índice diferente → a mesma faceta repetida noutra posição da volta (uma cópia simétrica).
- Mesmo índice e altura, ângulo diferente → outra inclinação no mesmo ponto da volta. É **assim** — por ângulo — que fileiras vizinhas se distinguem: uma main e uma break empilhadas na mesma direção radial têm ângulos diferentes, não alturas diferentes.
- Mesmo ângulo e índice, altura diferente → **a mesma faceta**, maior ou menor. O plano não se move; só avança mais para dentro da pedra.

É essa independência que confirma a Aula 05 do módulo 03: batente e altura vivem numa família (o plano radial), índice numa outra (a posição na volta), e é exatamente por não se sobreporem que um diagrama de lapidação consegue especificar centenas de facetas com pouquíssimas colunas de números — uma linha por fileira, com ângulo e índice fazendo o grosso do trabalho.

> **Ilustração pedida — as três coordenadas sobre a pedra.** Um corte de perfil da pedra mostrando: (a) uma seta de inclinação rotulada "ângulo", saindo do plano da cinta; (b) um arco ao redor do eixo vertical, dividido em posições numeradas, rotulado "índice"; (c) uma régua vertical ao longo do eixo, rotulada "altura", com duas marcas mostrando profundidades diferentes no mesmo ângulo e índice.

## Exemplo trabalhado

**Um talhe simples tem três facetas do pavilhão especificadas assim, num jogo de 96 dentes: Faceta A — ângulo 43°, índice 8. Faceta B — ângulo 43°, índice 32. Faceta C — ângulo 39°, índice 8. O que muda em cada par, e onde entra a altura?**

**Passo 1 — comparar A e B.** Ângulo: igual (43° nas duas). Índice: diferente (8 contra 32). Como só o índice muda, B é a **mesma faceta repetida noutra posição da volta** — uma cópia simétrica de A, deslocada 24 dentes ao redor da pedra.

**Passo 2 — comparar A e C.** Índice: igual (8 nas duas). Ângulo: diferente (43° contra 39°). Como só o ângulo muda, C tem outra inclinação **no mesmo ponto da volta**: ela e A pertencem a fileiras diferentes, empilhadas na mesma direção radial. É por aqui — pelo ângulo — que uma main e uma break vizinhas se distinguem.

**Passo 3 — onde entra a altura.** Nenhuma das três fica determinada só por esses dois números: cada uma ainda precisa saber **até onde** avançar. Mas repare no que a altura *não* faz. Se a Faceta A fosse cortada a 43° no índice 8 em duas alturas diferentes, não sairiam duas facetas — sairia **uma só**, a mais profunda, porque os dois planos são paralelos e o corte mais fundo consome o mais raso. A altura não cria faceta nova; ela dimensiona a que o ângulo e o índice já localizaram.

**Passo 4 — a lição do exemplo.** Ângulo e índice **localizam** a faceta na pedra; a altura **dimensiona** o corte. As três são necessárias, e cada uma responde a uma pergunta diferente — é essa divisão de trabalho que a aula 03 vai encontrar organizada nas colunas de um diagrama.

## Erros comuns

- **Achar que duas coordenadas bastam.** Ângulo e altura sem índice não dizem em que direção da volta a faceta fica; índice e ângulo sem altura não dizem quão fundo o corte avança. As três são necessárias.
- **Confundir altura com ângulo.** Já é o erro mais comum apontado na Aula 05 do módulo 03: mudar a altura, com o batente travado, não muda a inclinação — só a profundidade e o alcance do corte.
- **Ler um número de índice sem saber o jogo de dentes.** "Índice 8" só tem sentido dentro de uma roda específica — 8 num jogo de 96 é uma posição bem diferente de 8 num jogo de 32.
- **Achar que a coordenada "índice" desta aula é o índice de refração.** É a roda dentada, como a Aula 01 já isolou.

## O que não concluir

- Não concluir como as três coordenadas aparecem organizadas numa tabela real de diagrama de lapidação, com colunas e fileiras — é a aula 03.
- Não concluir a lógica do meetpoint nem por que cortar até um ponto de encontro dispensa medir a altura diretamente — é a aula 04.
- Não concluir como diagnosticar qual das três coordenadas está errada quando um ponto de encontro não fecha — é a aula 05.
- Não concluir nada sobre como regular fisicamente batente, índice ou altura numa facetadora real — competência de bancada, fora do escopo teórico deste curso.

## Recap relâmpago

- Uma faceta plana é um plano que precisa de posição e orientação: três coordenadas independentes a definem completamente.
- **Ângulo** ↔ inclinação em relação à cinta (batente de ângulo). **Índice** ↔ posição rotacional ao redor do eixo da pedra (roda dentada). **Altura** ↔ profundidade e alcance do corte (altura do mastro).
- As três são independentes: mudar uma sozinha, mantendo as outras duas, produz um resultado previsível — outra posição na volta (índice), outra inclinação no mesmo lugar (ângulo), ou **a mesma faceta em outro tamanho** (altura). Duas facetas não se distinguem só pela altura: dois planos paralelos no mesmo ângulo e no mesmo índice não coexistem, o mais fundo consome o mais raso.
- É essa independência de três eixos que fecha a especificação de uma faceta. Um diagrama impresso, porém, costuma tabelar só **dois** deles — ângulo e índice; a terceira coordenada não é lida de uma coluna, é fixada na pedra pelo ponto de encontro, e é disso que trata a aula 04.
- O nome "índice" desta coordenada continua sendo sempre a roda dentada, nunca o índice de refração.

## Próxima aula

Na [[09-geometria-e-diagramas-aula-03-anatomia-de-um-diagrama-de-lapidacao|Aula 03 — Anatomia de um diagrama de lapidação]], as três coordenadas desta aula reaparecem organizadas numa tabela real, ao lado das vistas de topo e lateral que mostram o contorno e o perfil do talhe.

## Fontes consultadas

- [[08-optica-do-facetado-aula-06-modelagem-optica-ray-tracing-e-os-limites-da-metrica|módulo 08, aula 06]] deste curso — a especificação de cada faceta por índice, ângulo e altura no GemCad, reativada nesta aula.
- [[03-maquinas-da-bancada-aula-05-anatomia-do-ajuste-batente-de-angulo-altura-do-mastro-e-o-cheater|módulo 03, aula 05]] deste curso — a definição de ângulo (batente) e altura (mastro) e as duas famílias de ajuste, reativadas nesta aula.
- United States Faceters Guild, *dicionário de facetamento* — ângulo, índice e altura como as grandezas especificadas num diagrama de lapidação.
- Robert W. Strickland, *GemCad for Windows — User's Guide* — a especificação de faceta por ângulo (*mast angle*), número de índice e **center-to-facet distance**, "the distance from the plane of the facet to the origin (0,0,0) at the center of the stone, measured perpendicular to the plane of the facet". Consultada em 2026-09-06. O parâmetro do software é essa distância, não uma "altura"; a altura do mastro é como a máquina a realiza.
- Sky Jems, *Faceting Diagram* — a estrutura de um diagrama e a nota de que o ângulo e o índice, juntos, "uniquely locate each facet on the stone's surface". Consultada em 2026-09-06.
- United States Faceters Guild, *dicionário de facetamento* — verbete *Tier*: "a group of facets at the same elevation around the stone". Consultada em 2026-09-06.
- Vargas & Vargas, *Faceting for Amateurs* — a prática de especificar cada faceta pelas três coordenadas.

<!--
nivel: ensino-medio-com-gemologia-v1
palavras_corpo: 1598
cobertura:
  lapidacao-m09-oa02: [Conteúdo, "Exemplo trabalhado", "Erros comuns", "Recap relâmpago"]
alegacoes_auditaveis:
  - claim_id: COO-TRES-EIXO-001
    claim: "Uma faceta plana gerada pela facetadora e um plano que precisa de posicao e orientacao simultaneamente, e por isso fica completamente especificada por tres coordenadas independentes: angulo (inclinacao), indice (posicao rotacional na volta) e altura (profundidade/alcance do corte). No GemCad, a terceira coordenada aparece como center-to-facet distance — a distancia do plano da faceta ate a origem no centro da pedra, medida perpendicularmente ao plano —, e nao como uma 'altura'; a altura do mastro e como a maquina realiza essa coordenada. RESSALVA: um diagrama impresso normalmente tabela apenas duas delas (angulo e indice); a terceira nao e lida de uma coluna, e fixada na pedra pelo ponto de encontro (ver aula 04 deste modulo)."
    risk: mecanismo
    source: "Robert W. Strickland, GemCad for Windows User's Guide (center-to-facet distance); Sky Jems, Faceting Diagram ('together, these two parameters uniquely locate each facet on the stone's surface'); curso de lapidacao, modulo 08 aula 06. Verificado em 2026-09-06."
  - claim_id: COO-ANGULO-DEF-001
    claim: "O angulo de uma faceta e sua inclinacao em relacao ao plano da cinta, fixada pelo batente de angulo; ele nao determina, sozinho, em que posicao da volta a faceta fica nem quao fundo o corte avanca."
    risk: consistencia interna
    source: "curso de lapidacao, modulo 03 aula 05 (definicao de angulo/batente, ja auditada)"
  - claim_id: COO-INDICE-DEF-001
    claim: "O indice de uma faceta e sua posicao rotacional ao redor do eixo da pedra, travada pela roda dentada; ele nao determina, sozinho, a inclinacao nem a profundidade da faceta. Duas facetas com o mesmo indice e ANGULOS diferentes formam camadas na mesma direcao radial (por exemplo, uma main e uma break vizinhas): fileiras vizinhas se distinguem por angulo, nunca por altura."
    risk: mecanismo
    source: "curso de lapidacao, modulo 09 aula 01 (definicao de indice) e modulo 03 aula 05 (indice como familia de posicao na volta); modulo 09 aula 03 (tabela com main a 42 graus e break a 46 graus, angulos distintos); United States Faceters Guild, dicionario de facetamento. Verificado em 2026-09-06."
  - claim_id: COO-ALTURA-DEF-001
    claim: "A altura do mastro fixa a profundidade e o alcance do corte; com o batente de angulo travado, mudar a altura mantem a inclinacao da faceta e muda apenas o tamanho da faceta e onde sua borda cai no contorno da pedra."
    risk: consistencia interna
    source: "curso de lapidacao, modulo 03 aula 05 (definicao de altura do mastro, ja auditada)"
  - claim_id: COO-INDEPEND-EIXO-001
    claim: "As tres coordenadas de uma faceta sao independentes entre si: mudar apenas o indice produz uma copia simetrica da faceta noutra posicao da volta; mudar apenas o angulo produz outra inclinacao no mesmo ponto da volta (e assim, por angulo, que fileiras vizinhas como main e break se distinguem); mudar apenas a altura NAO produz uma segunda faceta — produz a MESMA faceta em outro tamanho, porque os dois planos sao paralelos e o corte mais fundo consome o mais raso. Angulo e indice, juntos, localizam a faceta; a altura a dimensiona."
    risk: mecanismo
    source: "Sky Jems, Faceting Diagram ('together, these two parameters uniquely locate each facet on the stone's surface'); geometria direta de planos paralelos num solido convexo; curso de lapidacao, modulo 03 aula 05 (duas familias de ajuste) e modulo 09 aula 01 (regra do indice). Verificado em 2026-09-06."
-->
