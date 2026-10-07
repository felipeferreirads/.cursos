# Revisão didática: Módulo 14 — Óptica física para mineralogia: luz, refração, polarização e interferência

**Revisado em:** 2026-10-07  ·  **Modo:** review-and-fix
**Material:** `curso-mineralogia/14-optica-fisica/` — as 8 aulas e as figuras 1 a 8, depois da auditoria científica aprovada ([[14-optica-fisica-auditoria|relatório]]); o relatório de auditoria foi lido antes, e nenhuma das 10 correções foi revertida (ε da calcita como índice da vibração **paralela** a c; coríndon 0,008 a 0,009; O e E coerentes só com luz já polarizada; brilho metálico fora da reflexão parcial; nG − nB; I = I₁ cos²θ com I₁ = I₀/2; eixos ópticos como normais às seções circulares; classe m sem eixo 2; refratômetro limitado pelo líquido; data de Cauchy em disputa)
**Contrato de nível:** `ensino-medio-sem-geologia-v1` (LC-01 a LC-08; o LC-09 não se aplica a este módulo)
**Veredito:** Bem ensinado com ressalvas → **🟠 e 🟡 corrigidos; 🔵 abertos, não bloqueantes**

## Resumo

🔴 0 bloqueiam · 🟠 5 prejudicam · 🟡 13 atrito · 🔵 4 sugestões

**Carga estimada por aula** (contagem de `gerador-de-aula`; palavras de corpo de "Conteúdo" até o fim do recap, mesmo critério dos módulos 12 e 13, depois das correções):

| Arquivo | ID | Conceitos novos | Pré-requisitos reativados | Exemplos | Visuais | Duração |
|---|---|---|---|---|---|---|
| aula 01 | `a01` | 3 (onda e v = λf; luz como onda EM transversal; espectro) + λ no meio | 2 (notação científica; escala atômica) | 1 (2 itens) | 1 figura | ~25 min (~1.416) |
| aula 02 | `a02` | 3 (n = c/v; leis da reflexão e de Snell; placa de faces paralelas) | 2 (seno, reativado; λ no meio) | 1 (3 itens) | 1 figura + 1 tabela | ~28 min (~1.356) |
| aula 03 | `a03` | 3 (ângulo crítico; reflexão total × parcial; refratômetro) | 1 (Snell) | 1 (3 itens) | 1 figura + 1 tabela | ~22 min (~1.331) |
| aula 04 | `a06` | 4 (dispersão normal e sua causa; Cauchy; linhas de referência e dispersão gemológica; prisma) | 2 (Snell; espectro) | 1 (3 itens) | 1 figura | ~24 min (~1.429) |
| aula 05 | `a04` | 3 (luz natural × polarizada; polarizador de absorção; Malus) + três filtros | 2 (cosseno e decomposição, reativados; I ∝ A²) | 1 (5 itens) | 1 figura | ~26 min (~1.565) |
| aula 06 | `a07` | 4 (polarização por reflexão e Brewster; dupla refração O/E; eixo óptico e uniaxial; birrefringência e sinal) | 3 (tangente, reativada; eixo c; Snell) | 1 (3 itens) | 1 figura + 1 tabela | ~26 min (~1.449) |
| aula 07 | `a05` | 4 (superposição e fase; coerência; retardo Γ e ordem m; cores de interferência) + aviso de extinção | 3 (λ; n; dupla refração) | 1 (3 itens) | 1 figura | ~26 min (~1.607) |
| aula 08 | `a08` | 4 (princípio de Neumann; indicatriz; isotrópico/uniaxial/biaxial pela simetria; retardo por direção) | 3 (sistemas e eixos, módulo 04; ω/ε; Γ) | 1 (3 itens + aragonita) | 1 figura + 1 tabela | ~28 min (~1.638) |

As aulas 07 e 08 ficam no teto (~1.607 e ~1.638, até 2% acima de ~1.600, dentro da margem aceita no módulo 13, ~1.645); ver o 🟡 12, que explica por que **não** foram divididas.

## Achados

### 🟠 1. Aula 05: a analogia do terceiro filtro dizia que o mineral "reorienta" a vibração e, por isso, sempre acende

**Tipo:** analogia que ensina modelo mental errado
**Onde:** aula 05 · "O experimento dos três polarizadores"; Recap relâmpago
**Problema:** o texto fechava com "um mineral entre polarizadores cruzados pode fazer passar luz porque **reorienta** (decompõe em duas direções) a vibração", e o recap repetia "reorientar a vibração faz a luz passar, o princípio do microscópio de polarização". O filtro do meio entrega **uma** vibração linear, a 45°, e sempre deixa passar luz; o mineral entrega **duas**, com atraso, e pode deixar passar nada (Γ = mλ na aula 07; posições de extinção no módulo 15). Quem leva o modelo do filtro para o microscópio espera que todo mineral anisotrópico acenda sempre, e não entende a extinção. O recap é o trecho de onde sai o baralho.
**Correção aplicada:** a comparação ganhou o ponto em que quebra: "o filtro entrega **uma** vibração, a 45°, e sempre deixa passar luz; o mineral entrega **duas**, uma atrasada em relação à outra, e quanto passa depende desse atraso (aula 07) e da posição do cristal entre os filtros (módulo 15). Pode passar muita luz, pouca ou nenhuma." O recap passou a distinguir os dois caminhos ("Um mineral anisotrópico também pode 'acender' entre filtros cruzados, mas por outro caminho: divide a vibração em duas, e quanto passa depende do atraso entre elas").
**Escopo:** correção local. **Alegação nova registrada** (`OPT-POL-DIDAT-001`, "pendente").

### 🟠 2. Aula 06: "uniaxial" e "eixo c" usados antes de definidos

**Tipo:** salto de pré-requisito / termo usado antes de definido (LC-01)
**Onde:** aula 06 · Vocabulário; "Dupla refração"; "Eixo óptico, birrefringência e sinal óptico"
**Problema:** a aula define o raio O e o raio E "num cristal uniaxial (aula 08)" e descreve a calcita pelo "eixo c", mas uniaxial só é definido duas aulas depois, e o eixo c vem do módulo 05, que o cabeçalho do módulo não declara. O próprio vocabulário definia eixo óptico "num cristal uniaxial", em círculo. A aula 06 é a mais densa do módulo e a que mais depende desses dois termos.
**Correção aplicada:** termo **cristal uniaxial** no vocabulário ("cristal anisotrópico com uma só direção em que a luz não se divide, o eixo óptico; nele, o eixo óptico coincide com o eixo c. A aula 08 mostra quais sistemas cristalinos são uniaxiais"), antes de "eixo óptico"; em "Antes de começar", o eixo c reativado com wikilink para o [[05-miller-e-projecao-aula-01-eixos-cristalograficos-e-parametros-de-cela-por-sistema|módulo 05, aula 01]].
**Escopo:** correção local. **Alegação nova registrada** (`OPT-DUPLA-DIDAT-001`, "pendente").

### 🟠 3. Aula 07: o recap só ensinava a regra "Δ = mλ reforça", sem a inversão do microscópio

**Tipo:** recap que omite o ponto central (risco para o baralho e para o módulo 15)
**Onde:** aula 07 · Recap relâmpago; "Um aviso sobre a condição de extinção"
**Problema:** o corpo avisa, corretamente, que entre polarizadores cruzados com o cristal a 45° a regra se inverte (Γ = mλ escuro; (m + ½)λ máximo), mas o recap só trazia a regra das ondas paralelas, e o aviso fechava com "aqui basta guardar a condição para duas ondas na mesma direção". O exemplo (c) da própria aula já usa a regra invertida ("o vermelho seria quase extinto"). Um aluno que revisa pelo recap, ou um card gerado dele, chega ao módulo 15 com a regra trocada. São duas regras opostas sobre o mesmo símbolo: é o ponto de maior risco de confusão do módulo.
**Correção aplicada:** recap com a condição explícita ("Ondas coerentes de mesmo λ, **vibrando na mesma direção**...") e uma linha nova: "Atenção: entre polarizadores cruzados, com o cristal a 45° deles (módulo 15), a regra se inverte: Γ = mλ dá escuro e Γ = (m + ½)λ dá o máximo." O fecho do aviso passou a "guarde por ora que as duas regras existem e valem em situações diferentes". Para não passar do teto, saiu do corpo uma frase que repetia a remissão ao módulo 15.
**Escopo:** correção local. **Alegação registrada** (`OPT-INT-DIDAT-001`, "pendente"; a condição em si já foi verificada em `OPT-INT-EXTINCAO-001`).

### 🟠 4. Aula 08: "direção" ora é a de vibração, ora a de propagação, e "a direção c tem índice ε"

**Tipo:** ambiguidade que ensina modelo errado
**Onde:** aula 08 · "O princípio"; "Os três casos, pela simetria" (uniaxial); Erros comuns
**Problema:** o vocabulário e a indicatriz falam em direção de **vibração**, mas o parágrafo do uniaxial dizia "A direção c é diferente, e seu índice é ε" e, na frase seguinte, "ao longo dele [c] a luz vê só ω". Lido sem cuidado, "a direção c tem índice ε" e "a luz ao longo de c vê ω" se contradizem; e é exatamente essa troca (vibração × propagação) que produziu o erro 🔴 6 da auditoria na calcita. Sem a distinção explícita, o aluno não tem como reconciliar a aula 06 (índice do raio E "conforme a direção de propagação") com a aula 08 (índice "para cada direção de vibração").
**Correção aplicada:** frase de alerta na definição da indicatriz ("daqui em diante, 'direção' é aquela em que **E** vibra, não aquela em que a luz caminha; como a luz é transversal (aula 01), a que caminha numa direção só vibra, e só 'sente' índices, nas direções perpendiculares a ela"); o uniaxial reescrito ("A **vibração** ao longo de c é diferente, e seu índice é ε; só a luz que caminha perpendicular a c pode vibrar ao longo de c e encontrar ε [...] a luz que caminha ao longo dele só vibra no plano perpendicular a c, vê só ω"); erro comum novo ("Achar que a direção c 'tem índice ε' para qualquer luz").
**Escopo:** correção local. **Alegação nova registrada** (`OPT-ANI-DIDAT-001`, "pendente").

### 🟠 5. Aula 08: o argumento central do objetivo pulava um passo

**Tipo:** salto lógico no raciocínio que sustenta o objetivo (`oa06`)
**Onde:** aula 08 · "O princípio"; "Os três casos" (uniaxial)
**Problema:** "Girar de 90°, 60° ou 120° em torno de c troca entre si direções do plano perpendicular a c: **todas as direções nesse plano têm o mesmo índice**." Um giro de 90° iguala quatro direções, não todas; a conclusão não decorria do que estava escrito, e o aluno atento fica sem saber por que o tetragonal não tem quatro índices no plano. O exemplo do princípio ("um cristal pouco simétrico pode ter n quase isotrópico") também não ilustrava a ideia de a propriedade ter **mais** simetria que o cristal.
**Correção aplicada:** o passo que faltava, com o objeto que a aula já tinha apresentado (a indicatriz): "Girar de 90°, 60° ou 120° em torno de c tem de deixar igual o corte da indicatriz pelo plano perpendicular a c; uma elipse só volta a si mesma com giro de 180°, então esse corte é um círculo, e todas as direções nesse plano têm o mesmo índice, ω." O exemplo do princípio passou a ser o quartzo ("só tem eixo 3, mas seu índice é o mesmo em todas as direções do plano perpendicular a c"), que é justamente o caso em que a propriedade é mais simétrica que o cristal.
**Escopo:** correção local. Alegação em `OPT-ANI-DIDAT-001` ("pendente").

### 🟡 1. Aula 01: a analogia da corda não dizia onde quebra, e um erro comum contradizia a aula

**Tipo:** analogia sem limite declarado (LC-04)
**Onde:** aula 01 · Erros comuns
**Problema:** o erro comum dizia que o eixo vertical da figura "não é um eixo no espaço", enquanto o corpo ensina que E aponta numa direção do espaço, perpendicular ao raio. O que a corda engana é outra coisa: na luz nada material sobe e desce, e o raio não serpenteia.
**Correção aplicada:** "**Levar a analogia da corda longe demais.** Na luz nada material sobe e desce, e o raio não serpenteia: segue em linha reta. A altura da curva na Figura 1 representa o valor do campo elétrico **E** (que aponta numa direção perpendicular ao raio), não um deslocamento no espaço." Alegação `OPT-LUZ-DIDAT-001` ("pendente").

### 🟡 2. Aula 01: amplitude, remissões e um número sem origem

**Onde:** aula 01 · Vocabulário; Antes de começar; Exemplo trabalhado
**Correção aplicada:** amplitude "define a intensidade" → "a intensidade cresce com o quadrado dela (aula 05)", coerente com a aula 05 e a 07; "(módulos 06 e 08)" → wikilinks para os hubs ([[06-reticulo-e-cela-modulo|módulo 06]], [[08-empacotamento-e-coordenacao-modulo|módulo 08]]), como pede o LC-03; os "65%" da verificação ganharam a origem "(1,94/3,00 ≈ 0,65)".

### 🟡 3. Aula 02: ω, ε e "isotrópico" sem definição na primeira ocorrência

**Tipo:** termo usado antes de definido (LC-01)
**Onde:** aula 02 · tabela de índices; parágrafo seguinte
**Correção aplicada:** "(dois valores, chamados ômega e épsilon: aulas 06 a 08)"; "ele não é **isotrópico** (isto é, não tem as mesmas propriedades ópticas em todas as direções)". Alegação `OPT-REF-DIDAT-001` ("pendente").

### 🟡 4. Aula 03: termos sem glosa e remissão errada

**Onde:** aula 03 · "Ângulos críticos"; "Aplicação"; O que não concluir
**Correção aplicada:** "mesa (a faceta grande e plana do topo)"; "moissanita (carbeto de silício, usado como imitação de diamante)"; "é um aplicativo direto" → "é uma aplicação direta"; o brilho de face polida remetia à "aula 06", mas a reflexão parcial é ensinada na própria aula 03 → "(seção 'Reflexão parcial' acima e módulo 13)". Alegação `OPT-TOT-DIDAT-001` ("pendente").

### 🟡 5. Aula 04: A e B de Cauchy sem o passo, e o teste em 589 nm feito duas vezes

**Tipo:** salto no cálculo + redundância
**Onde:** aula 04 · "Uma fórmula empírica"; Exemplo trabalhado (c)
**Problema:** o corpo dava A = 2,3798 e B = 1,314 × 10⁴ nm² "com dois pontos", sem dizer como, e em seguida fazia o teste em 589 nm, repetido palavra por palavra no exemplo (c).
**Correção aplicada:** no corpo, o passo ("subtraindo as duas equações, A desaparece, e B = (2,4354 − 2,4076) / (1/486² − 1/687²) ≈ 1,314 × 10⁴ nm²; depois, A = 2,4354 − B/486² ≈ 2,3798"; conferido em Python: 13 144,3 e 2,37975) e o teste remetido ao exemplo (c). Também: "goniômetro de prisma (o goniômetro, do módulo 04, mede ângulos; este mede os do prisma e do raio desviado)"; "três vezes maior" → "mais de três vezes a do diamante" (0,156/0,044 = 3,5). Alegação `OPT-DIS-DIDAT-001` ("pendente").

### 🟡 6. Figura 4: a curva extrapolava contra o próprio texto, passava do eixo e tinha rótulos sobrepostos

**Tipo:** visual que contradiz o texto + anotação da auditoria
**Onde:** `14-optica-fisica-fig-04-dispersao.svg`
**Problema:** a curva de Cauchy, ajustada a 486 e 687 nm, era desenhada contínua de 420 a 700 nm, enquanto o exemplo (c) ensina que a fórmula serve "para interpolar dentro da faixa 486–687 nm, mas não para extrapolar"; entre 420 e ~433 nm passava acima do topo do eixo (n > 2,45). Além disso, o rótulo do eixo x (y = 418) e a primeira nota (y = 425) se sobrepunham.
**Correção aplicada:** curva contínua de 486 a 687 nm e **tracejada** de 436 a 486 e de 687 a 700 nm (fica dentro do eixo: ponto mais alto em y = 96, topo em 90); nota "Tracejado: extrapolação"; legenda da aula atualizada; tela de 470 para 500 px e notas em y = 452 e 474. Pontos, escala, barras e o cabeçalho corrigido na auditoria ("nG − nB, intervalo B–G") inalterados.

### 🟡 7. Aula 05: uma conferência que confundia quem conferia

**Onde:** aula 05 · Exemplo trabalhado, Conferência; Recap
**Problema:** "a soma (b) + (c) não precisa dar 50" — mas dá exatamente 50 (37,5 + 12,5), e quem soma fica sem saber se errou.
**Correção aplicada:** "E (b) + (c) dá exatamente 50, não por acaso: cos 60° = sen 30°, e cos²θ + sen²θ = 1, ou seja, as componentes paralela e perpendicular a um eixo somam a intensidade inteira." No recap, "absorve a componente de E num sentido" → "numa direção" (sentido e direção são coisas diferentes na física do ensino médio).

### 🟡 8. Aula 06: a explicação de Brewster parava no meio, e dois erros de redação

**Onde:** aula 06 · "Polarização por reflexão"; "Dupla refração"; "Eixo óptico"
**Problema:** a aula dava o mecanismo ("uma carga que oscila ao longo de uma direção não irradia nessa mesma direção") e, separadamente, o fato de refletido e refratado formarem 90°, sem ligar um ao outro; o aluno não via por que o ângulo de Brewster é especial.
**Correção aplicada:** "e é isso que liga a lei à explicação acima: a componente paralela ao plano de incidência faz as cargas do meio refletor oscilarem perpendicularmente ao raio refratado, isto é, exatamente na direção em que o refletido teria de sair, e nessa direção elas não irradiam." Também "Por que o cristal se divide em duas?" → "Por que a luz se divide em duas?" e "o opala" → "a opala" (anotação da auditoria). Alegação `OPT-DUPLA-DIDAT-001` ("pendente").

### 🟡 9. Aula 07: radiano sem reativação, um "meio λ" que era "quase meio" e um erro comum mal nomeado

**Onde:** aula 07 · "Somar ondas"; Exemplo (a); Erros comuns
**Correção aplicada:** "(em radianos: 2π rad = 360°, um ciclo inteiro por comprimento de onda)" (LC-06); exemplo (a), m = 0,46: "fica meio λ atrás, quase em oposição" → "fica quase meio λ atrás, perto da oposição de fase"; o erro comum "Usar uma só espessura para dois raios", que descrevia o procedimento **certo** (os dois raios atravessam a mesma espessura), passou a "**Somar os caminhos em vez de subtrair.**"; notação uniformizada (2A·|cos(πΔ/λ)|, como em cos²(πΔ/λ)); saiu do corpo a frase "uma lâmina fina de mineral muito birrefringente e uma espessa..." que o "O que não concluir" repete.

### 🟡 10. Aula 08: seções circulares sem explicação e um pré-requisito que desfazia a auditoria

**Onde:** aula 08 · biaxial; Antes de começar
**Problema:** (i) "as duas direções perpendiculares às duas seções circulares do elipsoide" (texto corrigido pela auditoria, achado 9) usava "seção circular" sem dizer o que é, e sem dizer por que a luz não se divide ali; (ii) o "Antes de começar" resumia o monoclínico como "um eixo binário" e o ortorrômbico como "três eixos binários", o que contradiz o módulo 04 ("um único eixo 2 ou 2̄") e o achado 10 da auditoria (a classe m não tem eixo 2).
**Correção aplicada:** (i) "Seção é o corte do elipsoide por um plano que passa pelo centro: quase todas são elipses, só duas são círculos. A luz que caminha perpendicular a um desses círculos vibra dentro dele e vê um índice só." (o texto da auditoria ficou intacto); (ii) "no ortorrômbico, três direções perpendiculares com eixo 2 ou 2̄; no monoclínico, uma só direção com eixo 2 ou 2̄ (o 2̄ equivale a um plano de simetria)". Alegação `OPT-ANI-DIDAT-001` ("pendente").

### 🟡 11. Figuras 2, 3, 6, 7 e 8: vírgula decimal, legenda encostada, rótulos cortados ou sobrepostos

**Tipo:** visual (anotações da auditoria e duas colisões encontradas nesta revisão)
**Onde:** figuras 2, 3, 6, 7, 8; gerador `figs14.py` (cópia anterior preservada como `figs14.pre_revdid.py` no scratchpad)
**Correção aplicada:** ângulos com vírgula decimal (fig. 2: "θ₂ = 29,7°"; fig. 3: "θc = 40,4°" no título e no raio rasante, "sai para o ar a 40,7°"; fig. 6: "56,3°" e "33,7°"); fig. 7: tela de 560 para 590 px e legenda inferior de y = 548 para y = 578 (a terceira soma desce até y ≈ 554); fig. 6: o rótulo "incidente (luz natural)", que começava fora da tela (x ≈ −21), passou a duas linhas, como "refletido (polarizado)"; fig. 8: o rótulo "ε (paralelo ao eixo c)" se sobrepunha ao subtítulo "tetragonal, hexagonal, trigonal", e os três desenhos desceram 20 px (com as linhas de índices de y = 330 para 352). Nenhum valor nem geometria mudou: as coordenadas que a auditoria conferiu continuam válidas nas figs. 2, 3, 5 e 6 (Brewster) e, nas figs. 4 e 8, valem com o deslocamento indicado. As oito figuras foram regeneradas do gerador, com as correções da auditoria (cabeçalho da fig. 4 e título da fig. 5) mantidas; XML validado e sobreposição de textos checada por script.

### 🟡 12. Aulas 07 e 08: carga no teto; enxugadas, não divididas

**Tipo:** carga cognitiva no limite (LC-02)
**Onde:** aulas 07 e 08, inteiras
**Problema:** a aula 07 entrou com 1.608 palavras e a 08 com 1.597; as correções 🟠 3, 4 e 5 e 🟡 9 e 10 somariam cerca de 40 (07) e 120 (08).
**Correção aplicada:** enxugadas sem tirar conteúdo de ensino: na 07, saíram duas frases que repetiam a remissão ao módulo 15 e o "O que não concluir"; na 08, os itens de "Cuidados", "Erros comuns" e "O que não concluir" que diziam a mesma coisa duas ou três vezes (isotrópico × amorfo; classe óptica × sistema exato; índices variam com a composição, já na aula 02; amostra da tabela) foram fundidos ou retirados, o "Método geral" perdeu um passo que repetia o recap e a comparação final ficou mais curta. Ficaram 1.607 e 1.638.
**Por que não dividir:** o módulo já tem 8 aulas, o teto de 3 a 8 do `_contexto.md`, e as duas aulas já são Partes 1 e 2 de uma aula do planejamento; uma terceira divisão quebraria `oa05` ou `oa06` ao meio sem fronteira natural (na 08, a classificação e o retardo por direção usam a mesma indicatriz). Se o aluno relatar que a aula 08 passou de 30 min, a fronteira menos ruim seria "princípio e três casos" × "retardo por direção e cuidados", decisão do orquestrador.
**Escopo:** correção local (dividir não foi necessário).

### 🟡 13. Contagem de palavras, durações e notação do hub

**Onde:** campo `palavras_corpo` das oito aulas e do `course-state.yaml`; "Duração estimada" das aulas 05 e 08; hub, "Pontos de dificuldade previstos"
**Correção aplicada:** recontado depois das correções (de "Conteúdo" até o fim do recap): 1.416 · 1.356 · 1.331 · 1.429 · 1.565 · 1.449 · 1.607 · 1.638. Duração da aula 05 de ~24 para ~26 min e da 08 de ~26 para ~28 min. O hub chamava o retardo de "Δ = d·(n₂ − n₁)"; as aulas usam Δ para a diferença de caminho geral e Γ para o retardo da lâmina, e o hub passou a "Γ = d·(n₂ − n₁)".

### 🔵 1. Questionário: o que pesar e o que não cobrar

**Sugestão para o `gerador-de-questionarios`:** ver a seção "Orientações para o questionário" abaixo.
**Desfecho:** aberto, não bloqueante.

### 🔵 2. IDs × ordem de leitura

**Sugestão:** a ordem de leitura dos arquivos é a01, a02, a03, a06, a04, a07, a05, a08 (as Partes 2 receberam ID novo). Questionário e baralho devem citar a aula pelo **ID** e pelo número do arquivo juntos ("aula 04, `a06`"), para não induzir a procurar a "aula 06" errada.
**Desfecho:** aberto, não bloqueante.

### 🔵 3. Pré-requisitos do módulo no estado

**Sugestão (para o orquestrador, não editado):** o `course-state.yaml` declara só o módulo 04 como pré-requisito, mas as aulas usam também o eixo c (módulo 05, agora com wikilink na aula 06), a escala atômica (módulos 06 e 08) e o brilho e a lâmina de 30 µm (módulo 13). Todos são núcleo e vêm antes na ordem numérica; acrescentar '05' e '13' a `prerequisites` seria decisão curricular, não desta revisão.
**Desfecho:** aberto, encaminhado.

### 🔵 4. Uma figura para as direções de vibração de O e E

**Sugestão:** a aula 06 descreve em palavras que O vibra perpendicular ao plano que contém o eixo óptico e o raio e E vibra nele; a figura 6 mostra só as trajetórias. Um esquema da seção principal com as duas vibrações marcadas (pontos para O, traços para E) ajudaria, e prepararia a indicatriz do módulo 16. Não foi desenhado aqui por exigir conteúdo geométrico novo que precisaria passar pelo auditor.
**Desfecho:** aberto, não bloqueante.

## Relação com o módulo 15 (remetido só por nome)

O módulo 14 promete ao 15, sem desenvolver, quatro coisas; o redator do 15 deve retomá-las com estes nomes, e o 14 não deve ser cobrado nelas além do que está dito:

1. **Linha de Becke** (aula 02, "Dois casos extremos"; aula 04, bordas coloridas pela dispersão): só o princípio (n₁ = n₂ apaga a interface). O 15 tem `oa02` para isso.
2. **Inversão da regra de interferência entre polarizadores cruzados** (aula 07, aviso e recap): Γ = mλ escuro, (m + ½)λ máximo, com o cristal a 45°. O 14 dá a regra e a razão em uma frase ("as duas vibrações voltam a compor a mesma vibração que entrou"); a dedução e a dependência com a posição do cristal (extinção, `oa05` do 15) são do 15.
3. **Por que o polarizador fica abaixo da lâmina** (aula 07, coerência; aula 05, microscópio): o 14 dá a razão (luz natural não gera O e E coerentes). O 15 pode partir dela.
4. **Carta de Michel-Lévy** (aula 07, "módulos 15 e 16"): o 14 dá Γ = d·Δn e a origem das cores; a leitura da carta (`oa04` do 15) é do 15. O exemplo da aula 07 (quartzo 270 nm a 30 µm) é o número que o 15 deve reencontrar na carta.

Nada do módulo 14 contradiz o plano do módulo 15 no hub (7 aulas planejadas, nenhuma escrita).

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo | Avaliado em |
|---|---|---|---|
| `mineralogia-m14-oa01` — luz como onda EM; λ, f, v; espectro | aula 01 (`a01`) | sim (f da luz de sódio; λ no quartzo, 381 nm) | (questionário a gerar) |
| `mineralogia-m14-oa02` — Snell, n, ângulo crítico, reflexão total | aulas 02 e 03 (`a02`, `a03`) | sim (ar → diamante e quartzo a 50°; θc 59,7° na água; 55° e 70°) | (questionário a gerar) |
| `mineralogia-m14-oa03` — dispersão e como se mede | aula 04 (`a06`) | sim (prisma 1,498; 0,0278 × 0,044; Cauchy em 589 nm) | (questionário a gerar) |
| `mineralogia-m14-oa04` — polarização por absorção, reflexão e dupla refração | aulas 05 e 06 (`a04`, `a07`) | sim (Malus 50/37,5/12,5/0 e três filtros; Brewster na água; raio O na calcita; sinal e birrefringência do coríndon) | (questionário a gerar) |
| `mineralogia-m14-oa05` — retardo e interferência | aula 07 (`a05`) | sim (Γ e m do quartzo e da calcita a 30 µm; três cores na calcita) | (questionário a gerar) |
| `mineralogia-m14-oa06` — isotropia/anisotropia × simetria | aula 08 (`a08`) | sim (classificar três materiais; retardo máximo; aragonita) | (questionário a gerar) |

Nenhum objetivo descoberto e nenhuma seção órfã. A fórmula de Cauchy e a do prisma (aula 04) são a parte mais periférica de `oa03` ("como ela é medida"), mas servem a ele; o refratômetro (aula 03) serve a `oa02` e a `oa03`.

## Orientações para o questionário

O módulo tem 8 aulas, acima de ~5–6: cabem **2 questionários parciais e 1 final**. Divisão natural: parcial 1 = aulas 01 a 04 (`a01`, `a02`, `a03`, `a06`; `oa01` a `oa03`); parcial 2 = aulas 05 a 08 (`a04`, `a07`, `a05`, `a08`; `oa04` a `oa06`).

**O que pesar mais**
- `oa02`, `oa04` (duas aulas cada) e `oa05`, `oa06` (a ponte para os módulos 15 e 16) devem ter mais itens que `oa01` e `oa03`.
- Cálculo com conferência, sempre com os números das aulas: Snell (ângulo com a normal); θc e o teste "existe ou não raio refratado"; Malus partindo da luz natural (I₀/2 primeiro); Brewster (θB + θ₂ = 90°); Γ = d·Δn e m = Γ/λ com conversão de mm para nm; classificar pelo número de índices e calcular Γ máximo.
- Armadilhas que as aulas ensinam a evitar e que valem como distratores: ângulo medido da superfície; Malus aplicado à luz natural; cos θ em vez de cos²θ; dispersão confundida com birrefringência; isotrópico confundido com isométrico; "uniaxial/biaxial" lido como eixos cristalográficos; somar caminhos em vez de subtrair; "meio denso" lido como densidade.
- Conceitos que o módulo 15 vai cobrar: por que o polarizador fica antes do cristal (coerência); por que vibrações perpendiculares precisam do analisador; por que cada cor tem uma ordem; a existência das duas regras (mesma direção × cruzados), sem cálculo de extinção.
- Os dois pontos que geraram erro na auditoria e modelo errado nesta revisão: ε é o índice da vibração **paralela** a c (calcita: ω 1,658 perpendicular, ε 1,486 paralelo); a luz que caminha ao longo de c vê só ω. Um item de "qual índice vê a luz que caminha em tal direção" é o melhor teste de `oa06`.

**O que não cobrar**
- Valores para decorar: c com nove algarismos, limites do visível (380–750 × 400–700 nm), comprimentos das linhas de Fraunhofer com decimais, a tabela de dispersão gemológica (cobrar só a ordem relativa: esfalerita > diamante > zircão > rubi/safira > quartzo > fluorita), o teto de ~1,81 do refratômetro como número exato, índices de minerais (dar sempre no enunciado).
- A data da fórmula de Cauchy (1830 ou 1836, controvérsia registrada pela auditoria) e a de Malus (1808/1809); Bartholin pode aparecer como contexto, não como resposta.
- A dedução da fórmula do desvio mínimo, os coeficientes A e B de Cauchy (no máximo, usar a fórmula dada) e a extrapolação de Cauchy fora de 486–687 nm.
- O nome e a numeração das leis de Fresnel-Arago (cobrar a ideia: componentes da luz natural não interferem).
- O que é do módulo 15 ou 16: posições e tipos de extinção, carta de Michel-Lévy, sinal dos biaxiais, orientação detalhada da indicatriz no monoclínico e triclínico (no máximo, "um eixo ∥ b no monoclínico, livre no triclínico").
- A birrefringência do coríndon por cruzamento dos extremos do Handbook: se aparecer, só como o erro a reconhecer (0,004 e 0,013 não existem num cristal real).
- As afirmações acrescentadas por esta revisão enquanto estiverem "pendente" (lista abaixo), em especial a glosa da moissanita, o mecanismo de Brewster pelo dipolo e o argumento da elipse no uniaxial: podem ser usadas como explicação no gabarito depois da segunda passagem do auditor, não como objeto de item antes dela.

## O que está bem feito (manter)

- Cada aula termina com um "Método geral" numerado e com uma conferência numérica (90° de Brewster, decrescimento de Malus, ordem de grandeza do retardo): o aluno pratica o hábito de conferir, não só de calcular.
- A trigonometria é reativada exatamente onde é usada (seno na 02, cosseno na 05, tangente na 06, radiano na 07), como pede o LC-06.
- As correções da auditoria viraram lição: o coríndon ensina que não se cruzam extremos de amostras diferentes; a coerência de O e E explica a posição do polarizador; o refratômetro mostra que quem limita é o líquido.
- O fio que vai da aula 01 (E empurra cargas; λ ≫ distância entre átomos) à aula 08 (índice por direção de vibração, princípio de Neumann) é contínuo: a anisotropia óptica chega como consequência, não como lista.
- As fronteiras com os módulos 15 e 16 são declaradas em cada ponto em que o assunto continua, sem ensinar o que é deles.

## Correções aplicadas

| # | Severidade | Desfecho | Arquivos |
|---|---|---|---|
| 🟠 1 | 🟠 | Corrigido | aula-05 |
| 🟠 2 | 🟠 | Corrigido | aula-06 |
| 🟠 3 | 🟠 | Corrigido | aula-07 |
| 🟠 4–5 | 🟠 | Corrigido | aula-08 |
| 🟡 1–2 | 🟡 | Corrigido | aula-01 |
| 🟡 3 | 🟡 | Corrigido | aula-02 |
| 🟡 4 | 🟡 | Corrigido | aula-03 |
| 🟡 5–6 | 🟡 | Corrigido | aula-04, fig-04 |
| 🟡 7 | 🟡 | Corrigido | aula-05 |
| 🟡 8 | 🟡 | Corrigido | aula-06 |
| 🟡 9 | 🟡 | Corrigido | aula-07 |
| 🟡 10 | 🟡 | Corrigido | aula-08 |
| 🟡 11 | 🟡 | Corrigido | fig-02, fig-03, fig-06, fig-07, fig-08 (todas regeneradas do `figs14.py`) |
| 🟡 12 | 🟡 | Corrigido (enxugadas, não divididas) | aula-07, aula-08 |
| 🟡 13 | 🟡 | Corrigido | todas as aulas, hub, `course-state.yaml` |
| 🔵 1–4 | 🔵 | 1, 2 e 4 abertos; 3 encaminhado ao orquestrador | — |

Nenhuma aula foi dividida; nenhum ID, arquivo ou link mudou.

**Afirmações factuais acrescentadas ou tocadas pela revisão** (nenhuma das 10 correções da auditoria foi revertida; todas as novas estão nos rodapés com `audit: pendente` para a segunda passagem do `auditor-cientifico`):

| claim_id | Aula | O que foi acrescentado |
|---|---|---|
| `OPT-LUZ-DIDAT-001` | 01 | intensidade ∝ amplitude²; na luz nada material oscila e o raio segue reto; a curva da fig. 1 é o valor de E, perpendicular ao raio |
| `OPT-REF-DIDAT-001` | 02 | isotrópico = mesmas propriedades ópticas em todas as direções; ω e ε chamados ômega e épsilon |
| `OPT-TOT-DIDAT-001` | 03 | mesa = faceta grande e plana do topo; moissanita = carbeto de silício, imitação de diamante; brilho de face polida pela reflexão parcial |
| `OPT-DIS-DIDAT-001` | 04 | B = 0,0278/(1/486² − 1/687²) = 13 144 nm², A = 2,37975 (Python); goniômetro de prisma; esfalerita "mais de três vezes" o diamante (3,5); curva da fig. 4 tracejada fora de 486–687 nm |
| `OPT-POL-DIDAT-001` | 05 | filtro do meio: uma vibração, sempre passa luz; mineral: duas vibrações com atraso, passa conforme o atraso e a posição do cristal, podendo não passar nada; cos²30° + cos²60° = 1 |
| `OPT-DUPLA-DIDAT-001` | 06 | uniaxial: um eixo óptico, coincidente com c; eixo c ao longo do eixo principal no tetragonal, hexagonal e trigonal; Brewster pelo dipolo (cargas oscilam perpendicular ao refratado, na direção do refletido, e não irradiam ao longo de si) |
| `OPT-INT-DIDAT-001` | 07 | 2π rad = 360°; inversão da regra entre polarizadores cruzados no recap (condição já verificada em `OPT-INT-EXTINCAO-001`); quartzo m = 0,46, "quase meio λ" |
| `OPT-ANI-DIDAT-001` | 08 | luz que caminha numa direção só vibra nas perpendiculares; ε é da vibração ∥ c, só encontrada por luz que caminha ⊥ c; só duas seções centrais do elipsoide triaxial são círculos; argumento da elipse (só volta a si com 180°) para o uniaxial; quartzo como propriedade mais simétrica que o cristal; ortorrômbico/monoclínico com "2 ou 2̄" |

**Pendente antes do questionário:** segunda passagem do auditor sobre essas oito alegações (o gate formal só bloqueia achados 🔴/🟠 da auditoria, mas são afirmações que ainda não passaram por ele). Questionário e baralho **não** foram gerados.
