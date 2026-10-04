# Flashcards — Módulo 06: Retículo cristalino, cela unitária e redes de Bravais

**Módulo:** [[06-reticulo-e-cela-modulo|Módulo 06 — Retículo cristalino, cela unitária e redes de Bravais]]
**Total:** 70 cards — 58 Basic + 12 Cloze
**Faixa de IDs:** `mineralogia-m06-fb001`–`fb058` · `mineralogia-m06-fc001`–`fc012`
**Auditoria:** aprovada em 2026-10-04, sem achados 🔴/🟠 em aberto — gate liberado.
**Didática:** revisão concluída em 2026-10-04
**Questionário:** gerado em 2026-10-04 (final cumulativo; 14 questões, 4 objetivos cobertos)
**Gerado em:** 2026-10-04, contra as aulas já auditadas e revisadas do módulo.

> [!info] Primeira geração
> Não há baralho prévio deste módulo. Todos os IDs são novos. Importe os dois CSVs num deck limpo.

## Arquivos para importar

| Arquivo | Tipo de nota no Anki | Campos |
|---|---|---|
| `06-reticulo-e-cela-flashcards-basic.csv` | Basic | id, frente, verso, tags, objetivo, aula, dificuldade, fonte |
| `06-reticulo-e-cela-flashcards-cloze.csv` | Cloze | id, texto, extra, tags, objetivo, aula, dificuldade, fonte |

> [!tip] Importação no Anki
> Importe os dois **separadamente**. Marque "Campos separados por ponto-e-vírgula" e mapeie `id` como primeiro campo. As tags são hierárquicas (`mineralogia::m06::...`).

## Distribuição

| Aula | Objetivo | Basic | Cloze | Total |
|---|---|---|---|---|
| a01 — Motivo, retículo e estrutura | `oa01` | 13 | 2 | 15 |
| a02 — Cela primitiva e convencional | `oa04` | 13 | 3 | 16 |
| a03 — Os 14 retículos de Bravais | `oa02` | 18 | 3 | 21 |
| a04 — Conteúdo da cela: Z, volume, densidade | `oa03` | 14 | 4 | 18 |

**Cobertura:** os quatro objetivos do módulo têm card. Nenhum card órfão.

## Critérios aplicados

- **Cada card é rastreável a uma frase das aulas auditadas** (`06-reticulo-e-cela-auditoria.md`); nenhum retículo, grupo espacial, Z ou densidade foi acrescentado fora delas.
- **Um exemplo mineral por retículo só quando a aula o discute** (halita, zircão, granadas, pirita, quartzo, calcita, berilo e apatita); a tabela de exemplos da aula 03 é de consulta.
- **Parâmetros de cela com decimais não viram card**; os números decorados são os inteiros (Z, pontos por cela, pesos) e os resultados que as aulas destacam (halita ≈ 2,16 g/cm³; calcita α ≈ 46°).
- **Cloze com no máximo 3 lacunas e sem chaves dentro das lacunas.**
- **Nenhum card depende de figura.**

## Cards Basic

| ID | Frente | Verso | Aula | Objetivo |
|---|---|---|---|---|
| `mineralogia-m06-fb001` | O que é o motivo (ou base) de uma estrutura cristalina? | O grupo de átomos que se repete; uma cópia dele fica em cada ponto do retículo. | a01 | `oa01` |
| `mineralogia-m06-fb002` | O que é um retículo cristalino? | O conjunto infinito de pontos equivalentes por translação, todos com a mesma vizinhança na mesma orientação; é abstração, não átomos. | a01 | `oa01` |
| `mineralogia-m06-fb003` | Qual é a relação entre estrutura, retículo e motivo? | Estrutura = retículo + motivo: uma cópia do motivo em cada ponto do retículo. | a01 | `oa01` |
| `mineralogia-m06-fb004` | Onde se põe o ponto do retículo dentro do motivo? | Em qualquer lugar, desde que seja o mesmo lugar em todas as cópias; mudar a escolha só desloca a grade. | a01 | `oa01` |
| `mineralogia-m06-fb005` | Qual é o teste prático para saber se um conjunto de pontos é um retículo? | Todo ponto tem de ter exatamente a mesma vizinhança, na mesma orientação. | a01 | `oa01` |
| `mineralogia-m06-fb006` | Como se escreve um ponto qualquer de um retículo tridimensional a partir dos vetores de translação? | n₁·t₁ + n₂·t₂ + n₃·t₃, com n₁, n₂, n₃ inteiros. | a01 | `oa01` |
| `mineralogia-m06-fb007` | O que são, fisicamente, os parâmetros a, b, c, α, β, γ? | Os comprimentos dos três vetores de translação do retículo e os ângulos entre eles. | a01 | `oa01` |
| `mineralogia-m06-fb008` | Em que a translação difere das operações de simetria do módulo 04? | Ela desloca o cristal inteiro e não deixa nenhum ponto fixo. | a01 | `oa01` |
| `mineralogia-m06-fb009` | Por que a forma externa de um cristal não revela o seu retículo? | As translações são de alguns ångströms; a forma mostra só a classe (rotações e reflexões). O retículo se vê por difração. | a01 | `oa01` |
| `mineralogia-m06-fb010` | Por que os vértices de uma camada de grafita (colmeia) não formam um retículo? | Metade dos vértices tem as ligações orientadas de um jeito e metade de outro: as vizinhanças diferem. | a01 | `oa01` |
| `mineralogia-m06-fb011` | Quantos carbonos tem o motivo de uma camada de grafita? | Dois (o retículo é hexagonal, com um ponto a cada par de átomos). | a01 | `oa01` |
| `mineralogia-m06-fb012` | Num tabuleiro de xadrez de dois tipos de átomo (casas de lado d), qual é o retículo? | Quadrado, girado 45°, de lado d·√2, com motivo de uma casa preta + uma branca. | a01 | `oa01` |
| `mineralogia-m06-fb013` | Qual é o motivo da halita? | Um Na e um Cl. | a01 | `oa01` |
| `mineralogia-m06-fb014` | O que é uma cela unitária? | Um paralelepípedo de arestas iguais a translações do retículo que, repetido por translação, preenche o espaço sem lacunas nem sobreposições. | a02 | `oa04` |
| `mineralogia-m06-fb015` | O que é uma cela primitiva? | Uma cela com exatamente um ponto do retículo; é a de menor volume. | a02 | `oa04` |
| `mineralogia-m06-fb016` | O que é a cela convencional? | A menor cela entre as que têm arestas ao longo das direções de simetria do retículo; pode ter 1, 2, 3 ou 4 pontos. | a02 | `oa04` |
| `mineralogia-m06-fb017` | Por que a cela convencional é preferida à primitiva? | Porque a primitiva pode esconder a simetria do retículo; a convencional a mostra. | a02 | `oa04` |
| `mineralogia-m06-fb018` | Por que um ponto do retículo situado num vértice vale só 1/8 para a cela? | Porque o vértice é compartilhado por 8 celas vizinhas. | a02 | `oa04` |
| `mineralogia-m06-fb019` | Por que uma cela I tem o dobro do volume da cela primitiva do mesmo retículo? | Porque contém 2 pontos do retículo (vértices + centro), e cada ponto ocupa o volume de uma primitiva. | a02 | `oa04` |
| `mineralogia-m06-fb020` | Que cela primitiva tem o retículo cúbico de faces centradas, e por que ela não é usada? | Um romboedro com ângulos de 60° entre as arestas e 1/4 do volume do cubo; ele esconde a simetria cúbica. | a02 | `oa04` |
| `mineralogia-m06-fb021` | Que vetor de centragem define a cela C? | (½, ½, 0): um ponto extra no centro da face ab. | a02 | `oa04` |
| `mineralogia-m06-fb022` | De onde vem a letra I da centragem de corpo? | Do alemão innenzentriert (centrado por dentro). | a02 | `oa04` |
| `mineralogia-m06-fb023` | O que significam as coordenadas fracionárias (x, y, z) de um ponto da cela? | Frações de a, b e c a partir do vértice de origem. | a02 | `oa04` |
| `mineralogia-m06-fb024` | Por que (1, ½, 0) e (0, ½, 0) indicam o mesmo ponto do retículo? | Porque diferem de uma translação inteira (a); por isso as coordenadas se escrevem entre 0 e 1. | a02 | `oa04` |
| `mineralogia-m06-fb025` | Quais são as posições dos Na na cela convencional da halita? | (0, 0, 0), (½, ½, 0), (½, 0, ½) e (0, ½, ½). | a02 | `oa04` |
| `mineralogia-m06-fb026` | Quantos Na e quantos Cl há na cela convencional da halita? | 4 e 4. | a02 | `oa04` |
| `mineralogia-m06-fb027` | Quantos retículos de Bravais existem em três dimensões? | 14. | a03 | `oa02` |
| `mineralogia-m06-fb028` | Quem mostrou que os retículos são 14, e quem tinha contado 15? | Auguste Bravais (trabalho de 1848, publicado em 1850); Moritz Frankenheim tinha contado 15 em 1842. | a03 | `oa02` |
| `mineralogia-m06-fb029` | No símbolo de um retículo, como cF, o que indica cada letra? | A primeira, a família (a, m, o, t, h, c); a segunda, a centragem (P, C, I, F, R). | a03 | `oa02` |
| `mineralogia-m06-fb030` | Que letra designa a família triclínica no símbolo do retículo, e por quê? | a, de anórtico. | a03 | `oa02` |
| `mineralogia-m06-fb031` | Quais são os retículos de Bravais do sistema ortorrômbico? | oP, oC, oI e oF (os quatro). | a03 | `oa02` |
| `mineralogia-m06-fb032` | Quais são os retículos de Bravais do sistema monoclínico? | mP e mC. | a03 | `oa02` |
| `mineralogia-m06-fb033` | Por que não existe retículo tetragonal C? | Centrar a base dá um retículo de quadrados menores (lado a/√2, girado 45°) que já é tetragonal primitivo. | a03 | `oa02` |
| `mineralogia-m06-fb034` | A que retículo equivale um 'tetragonal F'? | Ao tetragonal I (tI). | a03 | `oa02` |
| `mineralogia-m06-fb035` | Por que não existe retículo cúbico C? | Centrar só um par de faces torna uma direção diferente das outras e destrói os quatro eixos 3; o retículo deixaria de ser cúbico. | a03 | `oa02` |
| `mineralogia-m06-fb036` | Por que o ortorrômbico admite as quatro centragens? | Cada uma preserva os três eixos 2 e nenhuma pode ser redescrita como uma cela ortorrômbica menor. | a03 | `oa02` |
| `mineralogia-m06-fb037` | Onde se lê o tipo de centragem de um mineral na sua ficha? | Na primeira letra do símbolo do grupo espacial (ex.: I4₁/amd → I). | a03 | `oa02` |
| `mineralogia-m06-fb038` | Qual é o retículo de Bravais do zircão (I4₁/amd)? | tI. | a03 | `oa02` |
| `mineralogia-m06-fb039` | Qual é o retículo de Bravais da halita (Fm3̄m)? | cF. | a03 | `oa02` |
| `mineralogia-m06-fb040` | Qual é o retículo de Bravais das granadas (Ia3̄d)? | cI. | a03 | `oa02` |
| `mineralogia-m06-fb041` | Qual é o retículo de Bravais da pirita (Pa3̄)? | cP. | a03 | `oa02` |
| `mineralogia-m06-fb042` | Quais são os dois retículos da família hexagonal? | hP e hR. | a03 | `oa02` |
| `mineralogia-m06-fb043` | Um cristal trigonal tem sempre retículo romboédrico? | Não: o quartzo é trigonal com retículo hP; a calcita e o coríndon são trigonais com retículo hR. | a03 | `oa02` |
| `mineralogia-m06-fb044` | Que retículo têm os cristais hexagonais, como o berilo e a apatita? | Sempre hP. | a03 | `oa02` |
| `mineralogia-m06-fb045` | O que é Z? | O número de unidades de fórmula contidas na cela convencional. | a04 | `oa03` |
| `mineralogia-m06-fb046` | Qual é o Z da halita na cela convencional? | 4. | a04 | `oa03` |
| `mineralogia-m06-fb047` | Qual é o Z do quartzo? | 3. | a04 | `oa03` |
| `mineralogia-m06-fb048` | Qual é a fórmula do volume de uma cela monoclínica? | V = a·b·c·sen β. | a04 | `oa03` |
| `mineralogia-m06-fb049` | Qual é a fórmula do volume de uma cela hexagonal? | V = (√3/2)·a²·c ≈ 0,866·a²·c. | a04 | `oa03` |
| `mineralogia-m06-fb050` | Qual é a fórmula prática da densidade calculada, com V em Å³? | ρ (g/cm³) = Z·M / (0,6022 · V). | a04 | `oa03` |
| `mineralogia-m06-fb051` | De onde vem o fator 0,6022 na fórmula da densidade? | Da constante de Avogadro (6,022 × 10²³) multiplicada por 10⁻²⁴ (1 Å³ = 10⁻²⁴ cm³). | a04 | `oa03` |
| `mineralogia-m06-fb052` | Como se acha Z a partir da densidade medida? | Z = ρ · 0,6022 · V / M; o resultado tem de sair perto de um inteiro. | a04 | `oa03` |
| `mineralogia-m06-fb053` | Por que a densidade medida de uma amostra pode diferir da calculada? | A amostra real tem substituições na fórmula, vacâncias, defeitos, inclusões e fissuras; a calculada é a do cristal ideal. | a04 | `oa03` |
| `mineralogia-m06-fb054` | Qual é a densidade calculada da halita? | ≈ 2,16 g/cm³ (medida: 2,168). | a04 | `oa03` |
| `mineralogia-m06-fb055` | Quantos pontos do retículo tem a cela hexagonal de um retículo romboédrico (hR)? | 3: os vértices e os pontos (⅔, ⅓, ⅓) e (⅓, ⅔, ⅔). | a04 | `oa03` |
| `mineralogia-m06-fb056` | Qual é o Z da calcita na cela hexagonal e na cela romboédrica primitiva? | 6 na hexagonal; 2 na romboédrica (um terço do volume). | a04 | `oa03` |
| `mineralogia-m06-fb057` | Se Z muda quando se troca de cela, por que a densidade calculada não muda? | Porque o volume muda na mesma proporção que Z. | a04 | `oa03` |
| `mineralogia-m06-fb058` | O romboedro de clivagem da calcita é a sua cela primitiva? | Não: a cela primitiva tem α ≈ 46°; o romboedro de clivagem tem ângulos entre faces de cerca de 75° e 105°. | a04 | `oa03` |

## Cards Cloze

| ID | Texto | Extra | Aula | Objetivo |
|---|---|---|---|---|
| `mineralogia-m06-fc001` | Estrutura cristalina = {{c1::retículo}} + {{c2::motivo}}. | O retículo diz como se repete; o motivo, o que se repete. | a01 | `oa01` |
| `mineralogia-m06-fc002` | A restrição cristalográfica (só eixos 1, 2, 3, 4 e 6) é exigência da periodicidade por {{c1::translação}}. |  | a01 | `oa01` |
| `mineralogia-m06-fc003` | Pesos de compartilhamento numa cela: vértice {{c1::1/8}}; aresta {{c2::1/4}}; face {{c3::1/2}}. | Ponto interior vale 1. | a02 | `oa04` |
| `mineralogia-m06-fc004` | Uma cela P tem {{c1::1}} ponto do retículo; uma cela I ou C, {{c2::2}}; uma cela F, {{c3::4}}. |  | a02 | `oa04` |
| `mineralogia-m06-fc005` | O ponto de centragem de uma cela I fica em ({{c1::½, ½, ½}}). |  | a02 | `oa04` |
| `mineralogia-m06-fc006` | A família triclínica tem {{c1::1}} retículo de Bravais; a monoclínica, {{c2::2}}; a ortorrômbica, {{c3::4}}. |  | a03 | `oa02` |
| `mineralogia-m06-fc007` | A família tetragonal tem {{c1::2}} retículos de Bravais; a hexagonal, {{c2::2}}; a cúbica, {{c3::3}}. | Total: 1 + 2 + 4 + 2 + 2 + 3 = 14. | a03 | `oa02` |
| `mineralogia-m06-fc008` | O quartzo tem retículo {{c1::hP}}; a calcita, retículo {{c2::hR}}. | Ambos são trigonais. | a03 | `oa02` |
| `mineralogia-m06-fc009` | Volume da cela: cúbica {{c1::a³}}; tetragonal {{c2::a²·c}}; ortorrômbica {{c3::a·b·c}}. | Monoclínica: a·b·c·sen β. | a04 | `oa03` |
| `mineralogia-m06-fc010` | A densidade calculada é ρ = {{c1::Z·M}} / (Nₐ·V). | Com V em Å³: ρ = Z·M/(0,6022·V). | a04 | `oa03` |
| `mineralogia-m06-fc011` | Na fórmula da densidade, Z e V têm de ser da {{c1::mesma}} cela. | Misturar Z da convencional com V da primitiva erra por 2, 3 ou 4 vezes. | a04 | `oa03` |
| `mineralogia-m06-fc012` | A cela primitiva romboédrica da calcita tem α ≈ {{c1::46}}°. | Não é o romboedro de clivagem. | a04 | `oa03` |

## Navegação

[[06-reticulo-e-cela-modulo|← Hub do módulo]] · [[06-reticulo-e-cela-questionario-final|Questionário final]] · [[06-reticulo-e-cela-auditoria|Auditoria do módulo]]

## Histórico

- 2026-10-04 — primeira geração (fb001–fb058, fc001–fc012).
- 2026-10-04 — **checagem científica do baralho, antes de fechar o módulo.** Cada card foi conferido contra a frase da aula auditada de onde vem; contagens, centragens e densidades recalculadas (mesmos valores do registro de contas da auditoria). Resultado: 0 🔴, 0 🟠. Antes de receber ID definitivo, o rascunho foi ajustado: três cards de peso de compartilhamento e de pontos por cela, apontados pelo `validate_flashcards.py` como quase-duplicatas e já cobertos por cloze, foram retirados; os que ficaram foram reescritos como perguntas de "por quê".
- 2026-10-04 — `validate_flashcards.py`: 0 erros, 0 avisos (Basic e Cloze).
