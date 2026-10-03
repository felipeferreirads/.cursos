# Questionário — Módulo 08: Óptica do talhe facetado

**Módulo:** [[08-optica-do-facetado-modulo|Módulo 08]] — Óptica do talhe facetado
**Cobre:** aulas 01–06 (módulo completo, 6 aulas) · **Total:** 18 questões
**Objetivo:** integrar a óptica do talhe facetado — a aplicação do ângulo crítico e da reflexão interna total ao pavilhão; a leitura da tabela de ângulo crítico calculado e pavilhão publicado por material, sua base física de piso que desce e teto que não desce, e seus limites; a distinção de brilho, dispersão e cintilação por mecanismo; o compromisso entre desempenho óptico e rendimento em peso e os três lugares do projeto onde ele se decide; o segundo compromisso, na mesma variável de profundidade de pavilhão, entre saturação de cor e material escuro ou claro; e o que a modelagem por ray tracing mede, de fato, e o que suas métricas não capturam — cobrando princípio, geometria, causa-efeito e limite, nunca operação de bancada.

**Objetivos cobertos (IDs):** `lapidacao-m08-oa01`, `lapidacao-m08-oa02`, `lapidacao-m08-oa03`, `lapidacao-m08-oa04`, `lapidacao-m08-oa05`, `lapidacao-m08-oa06`.

> [!warning] Nível teórico
> Nenhuma questão deste questionário avalia competência de bancada ou destreza manual — não se pergunta "como ajustar o batente de ângulo", "como operar a facetadora", "como instalar o GemCad" nem "o que você faria na bancada". Todas avaliam princípio, geometria, causa-efeito, ordem de grandeza, escopo e limite, conforme a regra dura do curso (ver [[_contexto|_contexto.md]]). Pré-requisito externo, citado só por nome: módulo 01 do curso de Gemologia (índice de refração, ângulo crítico, reflexão interna total, saturação de cor).

> [!warning] Proibição herdada da revisão didática do módulo
> Nenhuma questão sobre `oa02` tem a forma "dada a faixa de índice X, qual o ângulo-alvo?". Essa formulação puniria exatamente o erro que a auditoria científica derrubou — a tabela **não** funciona por faixa de índice determinando um valor; o ângulo de pavilhão é publicado **por material**, e a faixa só organiza a leitura. A cobrança legítima é: ler as duas colunas (crítica calculada × publicada), explicar a base física piso-com-teto, e a MARGEM sobre o crítico — que **cresce** com o índice, não encolhe.

## Matriz de avaliação

| Objetivo | Explicar/Reconhecer | Aplicar/Prever | Analisar/Distinguir |
|---|---|---|---|
| oa01 — aplicar ângulo crítico e RIT ao pavilhão | Q01, Q02 | Q03 | Q01 |
| oa02 — ler a tabela, base física, limites | Q04, Q06 | Q06 | Q05 |
| oa03 — distinguir brilho, dispersão, cintilação por mecanismo | Q07 | Q09 | Q07, Q08 |
| oa04 — compromisso brilho × rendimento, onde se decide | Q10, Q11 | Q12 | Q12 |
| oa05 — saturação de cor × profundidade de pavilhão | Q13 | Q13, Q15 | Q14, Q15 |
| oa06 — o que o ray tracing mede e o que não captura | Q16, Q17 | Q18 | Q16, Q18 |

## Questões

**1. (Múltipla escolha) — lapidacao-m08-q01.** Um pavilhão de granada (índice de refração ≈ 1,74) é cortado, por erro de ajuste, com ângulo de pavilhão de 55° — bem acima do valor publicado para o material. Sobre o que acontece com a luz nessa faceta, qual afirmação está correta? *(Objetivo: `lapidacao-m08-oa01`)*

- a) A reflexão interna total falha logo na primeira faceta do pavilhão, porque 55° fica abaixo do ângulo crítico da granada, e a luz escapa por absorção progressiva a cada ricocheteio interno.
- b) A reflexão interna total se cumpre na **primeira** faceta do pavilhão (55° está bem acima do crítico), mas o raio refletido chega à faceta **oposta** com ângulo de incidência **abaixo** do crítico e escapa pelo fundo nessa segunda faceta — sem perda por absorção, já que a RIT devolve 100% da energia enquanto se cumpre. O efeito visível é a extinção (*nailhead*).
- c) A reflexão interna total se cumpre em todas as facetas do pavilhão sem exceção, porque qualquer ângulo acima do crítico garante retorno de luz útil ao observador — a pedra fica mais brilhante do que o normal.
- d) Não há como prever o resultado sem rodar um software de ray tracing; a relação entre ângulo de pavilhão e retorno de luz não é calculável por princípio.

**2. (Verdadeiro ou falso — justifique) — lapidacao-m08-q02.** "O ângulo relevante para decidir se uma faceta de pavilhão cumpre a reflexão interna total é o ângulo entre o raio de luz e o **plano da própria faceta** — quanto mais 'de raspão' a luz bate na faceta, maior esse ângulo, e mais fácil a RIT se cumprir." *(Objetivo: `lapidacao-m08-oa01`)*

**3. (Aplicação) — lapidacao-m08-q03.** Um topázio (índice de refração ≈ 1,62) é cortado com ângulo de pavilhão de 32°. (a) Calcule o ângulo crítico do topázio, usando θc = arcsin(1/n). (b) Compare 32° com esse valor e diga se a reflexão interna total se cumpre nessa faceta. (c) Descreva o que um observador veria olhando pela mesa, e nomeie o defeito. (d) Sem citar um valor exato de correção, diga em que **direção** o ângulo de pavilhão precisaria mudar para resolver o problema, e por quê essa direção resolve. *(Objetivo: `lapidacao-m08-oa01`)*

**4. (Múltipla escolha) — lapidacao-m08-q04.** Sobre a tabela de ângulo crítico calculado e pavilhão publicado apresentada na aula 02, qual afirmação está correta? *(Objetivo: `lapidacao-m08-oa02`)*

- a) As duas colunas têm a mesma origem: o ângulo de pavilhão publicado é obtido aplicando a fórmula do ângulo crítico a cada material — basta calcular θc para saber o ângulo-alvo.
- b) A coluna de ângulo crítico é **calculada** por θc = arcsin(1/n); a coluna de pavilhão principal é **publicada material a material** pela literatura do ofício, não deduzida da primeira — e a própria United States Faceters Guild adverte que não existe conjunto universal de ângulos ("*no magic bullet or universal set of angles*").
- c) A faixa de índice de refração determina sozinha o ângulo-alvo: basta saber em que faixa um material cai para conhecer seu pavilhão recomendado, independentemente de qual material específico é.
- d) O ângulo de pavilhão publicado decresce estritamente à medida que o índice de refração cresce, acompanhando de perto a queda do ângulo crítico.

**5. (Verdadeiro ou falso — justifique) — lapidacao-m08-q05.** "Como o ângulo crítico cai quando o índice de refração sobe, a margem entre o ângulo-alvo publicado e o ângulo crítico do material **também diminui** para materiais de índice mais alto — afinal, esses materiais já têm ângulo crítico baixo, então precisam de menos folga." *(Objetivo: `lapidacao-m08-oa02`)*

**6. (Dissertativa curta) — lapidacao-m08-q06.** Explique a "base física" da tabela de ângulos-alvo — o piso que desce e o teto que não desce. (a) O que é o **piso**, e por que ele decresce com o índice de refração? (b) O que é o **teto**, e por que ele **não** decresce com o índice? (c) Qual a consequência disso sobre a forma da coluna de pavilhão publicado (quase plana entre 39° e 43°) e sobre a margem sobre o crítico? *(Objetivo: `lapidacao-m08-oa02`)*

**7. (Múltipla escolha) — lapidacao-m08-q07.** Um talhe degrau (poucas facetas grandes e paralelas) e um talhe brilhante redondo (muitas facetas pequenas) são cortados do mesmo material, de dispersão moderadamente alta. Qual associação está correta? *(Objetivo: `lapidacao-m08-oa03`)*

- a) *Brilliance*, no dicionário da United States Faceters Guild, é sinônimo exato de *brightness*: os dois termos descrevem apenas o retorno de luz branca, sem incluir dispersão nem cintilação.
- b) O degrau, com facetas grandes, tende a mostrar mais *brightness* (retorno de luz branca em blocos largos) e menos fogo perceptível (as cores se recombinam antes de sair da faceta); o brilhante, com facetas pequenas e numerosas, fragmenta o retorno mas separa melhor as cores e produz cintilação mais densa.
- c) Mais facetas sempre aumentam os três efeitos ao mesmo tempo, sem limite algum — por isso o brilhante é objetivamente superior ao degrau em qualquer material.
- d) A cintilação depende só do número de facetas, não de movimento: uma pedra parada sob luz fixa já mostra cintilação plena.

**8. (Verdadeiro ou falso — justifique) — lapidacao-m08-q08.** "Reduzir o tamanho das facetas sempre aumenta o fogo percebido, sem limite algum — quanto menores e mais numerosas as facetas, mais intensa fica a dispersão visível." *(Objetivo: `lapidacao-m08-oa03`)*

**9. (Aplicação) — lapidacao-m08-q09.** Uma turmalina de dispersão baixa (comparável à do quartzo) é candidata a dois projetos: (A) talhe degrau, com poucas facetas grandes; (B) talhe brilhante, com muitas facetas pequenas. (a) Compare o brilho (*brightness*) esperado nos dois projetos. (b) Compare o fogo esperado nos dois — e explique por que, neste material específico, a diferença de fogo entre A e B é menos dramática do que seria num material de dispersão alta como o zircão. (c) Qual dos dois projetos tende a mostrar cintilação mais densa, e por quê? *(Objetivo: `lapidacao-m08-oa03`)*

**10. (Múltipla escolha) — lapidacao-m08-q10.** Sobre pavilhão raso (mais raso que o ângulo-alvo publicado) e rendimento, qual afirmação está correta? *(Objetivo: `lapidacao-m08-oa04`)*

- a) Pavilhão raso é sempre uma escolha cautelosa e conservadora, que nunca aumenta o peso final da pedra — é puramente um erro de projeto a evitar.
- b) **Com o contorno da cinta fixo**, pavilhão raso não retém peso; mas soltando o contorno, o pavilhão raso permite um **diâmetro maior** a partir do mesmo bruto — é a manobra de retenção/ganho de peso mais comum do ofício, e também a origem mais frequente de pedras janeladas.
- c) Pavilhão raso nunca aproxima o regime de janelamento; esse defeito só ocorre com pavilhão fundo demais.
- d) A profundidade de pavilhão é a única variável de projeto que afeta o rendimento; culaça e contorno não têm efeito algum sobre o peso final.

**11. (Verdadeiro ou falso — justifique) — lapidacao-m08-q11.** "A presença de uma culaça (pequena faceta plana na base do pavilhão, no lugar do *meetpoint*) é sempre sinal de corte malfeito, porque interrompe a reflexão interna total contínua do resto do pavilhão." *(Objetivo: `lapidacao-m08-oa04`)*

**12. (Aplicação) — lapidacao-m08-q12.** Um bruto de espinélio irregular e caro está sendo avaliado para dois projetos: (A) redondo de precisão, com pavilhão exatamente no valor-alvo publicado e contorno centrado, descartando boa parte do bruto; (B) contorno livre acompanhando a silhueta do bruto, com pavilhão ligeiramente raso nas extremidades mais estreitas para não furar a superfície do material. (a) Em qual dos três lugares do compromisso — profundidade de pavilhão, culaça ou contorno — cada rota mexe primeiro? (b) Dado que o espinélio deste bruto é raro e caro, qual rota o valor do material tende a favorecer, e por quê? (c) Alguém do comércio chama o projeto B de "corte nativo". Essa descrição está correta pelo critério real de definição do termo, ou é um uso impróprio? Justifique. *(Objetivo: `lapidacao-m08-oa04`)*

**13. (Múltipla escolha) — lapidacao-m08-q13.** Duas ametistas do mesmo lote de bruto, mesmo índice de refração, mas uma de cor roxo muito intensa (quase opaca em pedaços grandes) e outra de tonalidade lilás muito pálida, vão receber ajuste de profundidade de pavilhão em relação ao valor-alvo óptico puro da aula 02. Qual afirmação está correta? *(Objetivo: `lapidacao-m08-oa05`)*

- a) As duas devem receber exatamente o mesmo ajuste, porque têm o mesmo índice de refração e a tabela da aula 02 não distingue saturação de cor.
- b) A ametista intensa pede pavilhão **mais fundo**, para intensificar ainda mais a cor já forte; a pálida pede pavilhão **mais raso**, para não perder a pouca cor que tem.
- c) A ametista intensa pede pavilhão **mais raso** que o valor-alvo, para encurtar o caminho óptico e evitar que o centro fique escuro demais; a pálida pede pavilhão **mais fundo**, para alongar o caminho e acumular mais cor visível.
- d) O ajuste de profundidade por saturação de cor é decidido pela própria tabela de ângulos-alvo da aula 02, sem necessidade de examinar o material.

**14. (Verdadeiro ou falso — justifique) — lapidacao-m08-q14.** "Duas gemas do mesmo índice de refração recebem sempre a **mesma direção** de ajuste de profundidade de pavilhão por cor, porque o índice de refração já determina o valor-alvo da tabela da aula 02, e o ajuste de cor só refina esse mesmo valor." *(Objetivo: `lapidacao-m08-oa05`)*

**15. (Aplicação) — lapidacao-m08-q15.** Uma safira apresenta zonação: uma faixa de azul intenso próxima de um dos lados do cristal, e o restante do material quase incolor. O lapidário já decidiu, pela leitura do bruto, orientar a mesa para que a faixa azul fique bem posicionada no caminho da luz. Só agora decide a profundidade de pavilhão. (a) Por que a decisão de orientação precisa vir **antes** da decisão de profundidade, e não depois? (b) Se o pavilhão for aprofundado sem essa orientação prévia já feita, o que pode dar errado? (c) Supondo a orientação já feita e a faixa bem posicionada, o material dessa faixa azul é de cor cheia ou de cor fraca — e que direção de ajuste (mais raso ou mais fundo) isso sugere? *(Objetivo: `lapidacao-m08-oa05`)*

**16. (Múltipla escolha) — lapidacao-m08-q16.** Um desenho recebe uma métrica de brilho muito alta no GemRay, mas o lapidário sabe que o bruto real tem zonação de cor visível. Por que a métrica alta pode não representar bem o resultado final? *(Objetivo: `lapidacao-m08-oa06`)*

- a) Porque o GemRay ignora completamente a cor: ele só calcula reflexão de luz branca, sem levar em conta absorção nem dispersão.
- b) Porque o GemRay modela absorção por caminho óptico e dispersão (traça vermelho, verde e azul separadamente), mas sobre uma **cor única atribuída pelo operador** — a zonação real do bruto, com suas variações internas de saturação, fica fora do modelo.
- c) Porque métricas de brilho simuladas não têm relação alguma com o comportamento óptico real da pedra — são apenas números de marketing do software.
- d) Porque o GemRay só funciona para materiais incolores; qualquer material colorido invalida a simulação inteira.

**17. (Dissertativa curta) — lapidacao-m08-q17.** (a) Distinga GemCad de GemRay — o que cada um faz, e por que GemRay não é um "módulo" do GemCad. (b) Nomeie as **três lacunas reais** do ray tracing apontadas na aula 06 (não a lacuna falsa de "o software ignora a cor"). (c) Por que a aula 06 fecha o módulo em vez de abri-lo — o que ela faz que nenhuma aula anterior fazia? *(Objetivo: `lapidacao-m08-oa06`)*

**18. (Aplicação) — lapidacao-m08-q18.** Um desenho de brilhante oval para uma turmalina (índice ≈ 1,62) recebe, no GemRay, uma métrica de brilho excelente e uma prévia de imagem com fogo visível nas bordas. O bruto real dessa turmalina tem uma leve variação de tom entre o núcleo (mais escuro) e a borda (mais claro), e uma inclusão fina próxima da cinta, invisível na imagem simulada. (a) O que a métrica alta **garante** sobre a geometria do desenho? (b) Se a variação núcleo–borda for informada ao software como uma única cor, a simulação a captura? E se for zonação real, não uniforme, o que fica de fora? (c) O que a inclusão revela sobre um limite do ray tracing **diferente** do limite de cor? (d) A ferramenta pode decidir, sozinha, se esse desenho é esteticamente melhor do que um alternativo que trocasse parte do brilho por mais fogo? Justifique. *(Objetivo: `lapidacao-m08-oa06`)*

---

## Gabarito comentado

<details><summary>Ver respostas</summary>

**1. Resposta: b).** É o mecanismo corrigido pela auditoria científica: um pavilhão fundo demais cumpre a reflexão interna total na **primeira** faceta (55° está bem acima do crítico da granada, ≈33,9°–35,3° conforme a variedade), mas entrega o raio à faceta oposta com ângulo **abaixo** do crítico, e ele escapa pelo fundo nessa segunda faceta. A perda **não é por absorção** — a RIT devolve 100% da energia enquanto se cumpre, e numa pedra sem cor forte a absorção ao longo do trajeto é desprezível. O efeito visível é a extinção, o *nailhead* do ofício. **a)** é o erro que a auditoria corrigiu: atribuía a extinção a absorção progressiva, contradizendo a própria definição de RIT. **c)** ignora que "acima do crítico" garante RIT **naquele ponto**, não que a faceta seguinte cumpra a mesma condição. **d)** falso — o princípio é calculável sem software; o ray tracing (aula 06) refina, não substitui, o raciocínio geométrico.

**2. Falso.** Todo ângulo óptico relevante — incidência, crítico, pavilhão — é medido a partir da **normal** à superfície (a perpendicular a ela), nunca do plano da própria faceta. A afirmação também erra na direção: o ângulo em relação ao plano da faceta é o **complemento** do ângulo em relação à normal (somam 90°). Se a luz bate "de raspão" na faceta, o ângulo contra o **plano** é grande, mas o ângulo contra a **normal** — o que decide a RIT — é **pequeno**, o que **dificulta**, não facilita, a reflexão interna total. É o erro de estreia mais comum nomeado na aula 01.

**3.** Resposta esperada.
- **(a)** θc = arcsin(1/1,62) = arcsin(0,617) ≈ **38,1°**.
- **(b)** 32° é **menor** que 38,1°: a reflexão interna total **não se cumpre** nessa faceta.
- **(c)** O observador vê, pela mesa, uma área central sem retorno de luz — a faceta parou de funcionar como espelho e passou a se comportar como janela de vidro comum, deixando ver o que está atrás da pedra. É o **janelamento**.
- **(d)** O ângulo de pavilhão precisa **aumentar** — subir para acima do ângulo crítico, com margem —, porque é isso que restabelece a condição de RIT (ângulo de incidência acima do crítico) para o mesmo raio.
- **Pontuação:** completa calcula θc corretamente, identifica a falha de RIT, nomeia o janelamento e dá a direção certa da correção com a justificativa geométrica; parcial acerta o cálculo e o defeito mas erra ou omite a direção da correção.

**4. Resposta: b).** As duas colunas têm origens diferentes: a de ângulo crítico é **calculada** (θc = arcsin(1/n)); a de pavilhão principal é **publicada material a material** pelo International Gem Society, e não é deduzida da primeira — é exatamente por isso que berilo (IR ≈1,57) recebe pavilhão mais fundo que quartzo (IR≈1,54) apesar do índice maior. A United States Faceters Guild reforça isso publicando seu próprio conjunto para IR 1,54 com a ressalva de que não existe conjunto universal. **a)** é o erro que a auditoria corrigiu — supor que o alvo é deduzido do crítico. **c)** é a forma proibida: a faixa **organiza** a leitura, não determina o valor; o valor vem do material. **d)** descreve a queda do crítico, não do alvo publicado, que é quase plano.

**5. Falso.** É exatamente o oposto: a margem sobre o crítico **cresce** com o índice de refração. O exemplo trabalhado da aula 02 mostra quartzo (θc≈40,5°, pavilhão 42°, margem 1,5°) e coríndon/safira (θc≈34,4°, pavilhão também 42°, margem 7,6°) — dois materiais cujo crítico difere em mais de 6°, recebendo o **mesmo** ângulo de pavilhão. Isso acontece porque o ângulo publicado fica travado pelo **teto** (a exigência de saída pela coroa), que não cai com o índice, enquanto só o **piso** (o crítico) cai — toda a queda do piso vira margem extra.

**6.** Resposta esperada.
- **(a) O piso** é o ângulo crítico, θc = arcsin(1/n): decresce quando o índice de refração cresce, porque um material que desvia mais a luz também a "prende" com mais facilidade, exigindo um ângulo de incidência menor para cumprir RIT.
- **(b) O teto** é a exigência de que a luz, depois de refletir no pavilhão, **saia pela coroa** na direção do observador — não basta cumprir RIT, o raio ainda precisa sair no lugar certo. Essa é uma restrição de geometria de saída que o ângulo crítico, sozinho, não expressa, e ela **não cai** com o índice de refração — é a mesma exigência de saída pela coroa para qualquer material.
- **(c)** O ângulo publicado fica espremido entre um piso que desce e um teto que não desce: por isso a coluna de pavilhão fica quase **plana** (39°–43°) mesmo com o crítico variando de ≈44° a ≈24°, e a **margem** sobre o crítico **cresce** com o índice — quanto mais baixo o piso, mais distância até o teto que não se move.
- **Pontuação:** completa nomeia piso e teto com o mecanismo de cada um, e liga isso à forma plana da tabela e ao crescimento da margem; parcial descreve um dos dois limites sem articular a consequência sobre a forma da tabela.

**7. Resposta: b).** É a lógica de mecanismo separado da aula 03: o degrau, com poucas facetas grandes, devolve blocos largos de luz branca (alto *brightness*), mas cada faceta grande recombina as cores dispersas antes de sair, deixando o fogo pouco visível; o brilhante, com facetas pequenas e numerosas, fragmenta o retorno bruto mas isola melhor os feixes de cor e produz um padrão de cintilação mais denso. **a)** inverte a nomenclatura da própria USFG: *brilliance* é o termo **guarda-chuva** (inclui *brightness* e frequentemente *color spread* ou *scintillation*), não sinônimo isolado de *brightness*. **c)** ignora que mais facetas fragmentam o brilho bruto, e que há um limite de resolução do olho para o fogo (Q08). **d)** contradiz a definição: cintilação **depende de movimento** — da pedra, da luz ou do observador.

**8. Falso.** A relação entre número de facetas e fogo percebido **não é monotônica**: abaixo de um certo tamanho de faceta, cada flash colorido fica pequeno demais para o olho resolver como cor, e aumentar ainda mais o número de facetas passa a **reduzir** o fogo percebido em vez de aumentá-lo. Que esse ponto de retorno decrescente existe é aceito no ofício; **onde** exatamente ele fica é objeto de divergência real na literatura de talhe — a aula 03 declara isso como pergunta em aberto, sem arbitrar o debate (não é uma questão com resposta numérica fechada).

**9.** Resposta esperada.
- **(a) Brilho:** o projeto A (degrau) tende a mostrar *brightness* mais "sólido" — blocos largos de luz branca devolvidos de uma vez pelas facetas grandes. O projeto B (brilhante) também devolve bastante luz, mas fragmentada em pontos menores.
- **(b) Fogo:** como a turmalina deste caso tem dispersão baixa (semelhante ao quartzo), o fogo fisicamente existe nos dois projetos, mas é sutil em ambos — a diferença entre A e B é real (o brilhante separa mais os feixes) porém pouco dramática, porque não há muita dispersão física para revelar. Num material de dispersão alta como o zircão, a mesma comparação produziria uma diferença de fogo muito mais perceptível entre degrau e brilhante — é a dispersão do material, não só o corte, que determina o quanto há para revelar.
- **(c) Cintilação:** o projeto B (brilhante), por ter mais facetas pequenas, produz mais pontos de troca de estado por unidade de movimento — padrão mais denso e "vivo". O degrau, com poucas facetas grandes, cintila mais raramente e de forma mais ampla.
- **Pontuação:** completa compara os três efeitos nos dois projetos e explica corretamente por que a dispersão baixa do material amortece (sem eliminar) a diferença de fogo entre os cortes; parcial compara os efeitos mas trata "dispersão baixa" como "sem fogo nenhum" ou ignora o papel do material na magnitude da diferença.

**10. Resposta: b).** Com o contorno fixo, pavilhão raso de fato não ganha peso — mas essa condição raramente vale para bruto tabular ou achatado: soltando o contorno, o pavilhão raso permite um diâmetro maior a partir do mesmo material, sendo a manobra de rendimento mais comum do ofício e, ao mesmo tempo, a origem mais frequente de pedras janeladas. **a)** é o erro corrigido pela auditoria — tratar pavilhão raso como sempre conservador, ignorando a manobra de diâmetro. **c)** contradiz a aula 01: pavilhão raso é justamente o mecanismo geométrico do janelamento. **d)** ignora culaça e contorno, os outros dois lugares do compromisso descritos na aula 04.

**11. Falso.** A culaça é uma escolha **deliberada** de durabilidade, não sinal de corte malfeito. O desenho ideal do pavilhão termina num único ponto (o *meetpoint*), que é frágil e vulnerável a lascamento; a culaça o substitui por uma pequena faceta plana, trocando uma fração muito pequena e previsível de desempenho óptico por resistência a impacto — e evitando um retrabalho que, se o *meetpoint* lascar, custaria mais peso do que a própria culaça.

**12.** Resposta esperada.
- **(a)** A rota A mexe primeiro em **profundidade de pavilhão** (mantém o valor-alvo publicado) e em **contorno** (redondo centrado, descartando bruto). A rota B mexe primeiro em **contorno** (livre, seguindo a silhueta) e, como consequência, em **profundidade de pavilhão** (mais raso nas pontas para não furar o bruto).
- **(b)** Bruto raro e caro empurra na direção da **retenção de peso** — cada quilate perdido pesa mais na conta final — o que favorece a rota B, mesmo custando desempenho óptico localizado nas extremidades.
- **(c)** A descrição está **incorreta** pelo critério real do termo: "corte nativo" designa, em primeiro lugar, a pedra facetada **no país de origem, à mão e a olho**, por métodos tradicionais — é um critério de **origem e método**, do qual a retenção de peso é consequência típica, não a definição. O projeto B, descrito apenas como "contorno livre priorizando rendimento", não diz nada sobre onde ou como foi cortado; chamá-lo de "corte nativo" só porque prioriza peso é usar o termo pelo resultado, não pelo critério que o define — o mesmo uso impróprio que a aula 04 registra como disputado no comércio.
- **Pontuação:** completa localiza corretamente os dois lugares mexidos por cada rota, liga o valor/raridade do material à rota B, e recusa "corte nativo" pelo critério de origem/método; parcial localiza as rotas mas aceita "corte nativo" apenas pelo resultado de peso.

**13. Resposta: c).** É a lógica do caminho óptico da aula 05: caminho mais longo = mais absorção = cor mais forte. A ametista intensa, quase opaca em pedaços grandes, já satura com pouco caminho; um pavilhão no valor-alvo ou mais fundo aumentaria a absorção além do ponto de saturação perceptual, escurecendo o centro — a prescrição é pavilhão **mais raso**. A pálida precisa do oposto: caminho mais longo para que a absorção acumulada produza cor visível — pavilhão **mais fundo**. **a)** ignora que a saturação de origem, não o índice de refração, decide a direção do ajuste. **b)** e **d)** invertem a lógica: aprofundar o material já escuro pioraria o escurecimento, e a tabela da aula 02 não sabe nada sobre saturação de cor.

**14. Falso.** A direção do ajuste de profundidade por cor depende da **saturação de origem** do material (cor cheia × cor fraca), não do índice de refração. Duas gemas de índice idêntico podem ter saturações opostas e, portanto, receber ajustes em **direções opostas** — é exatamente a estrutura do exemplo das duas granadas na aula 05 (mesma faixa de índice, mesma tabela, dois ajustes de profundidade em sentidos contrários). O índice de refração decide o valor-alvo **óptico puro** da aula 02; a leitura de saturação do bruto (módulo 05) decide para que lado desse valor o projeto se desloca.

**15.** Resposta esperada.
- **(a)** A profundidade de pavilhão alonga o caminho óptico através de **todas** as zonas de cor que o raio atravessa, não só da zona mais próxima da mesa. A orientação de mesa decide **onde** a cor boa fica no caminho da luz; a profundidade decide **quanto** caminho esse trajeto tem. Decidir profundidade antes de orientação arrisca intensificar a intensidade certa na **zona errada**.
- **(b)** Se o pavilhão for aprofundado sem a orientação prévia, o caminho mais longo pode intensificar tanto a faixa azul desejada quanto uma zona indesejada (a região quase incolor, ou uma eventual zona de fundo) se a mesa não tiver isolado bem uma da outra primeiro — o ajuste "certo" na variável errada.
- **(c)** A faixa de azul intenso, que já mostra cor forte mesmo em caminho curto, é material de **cor cheia**; isso sugere um pavilhão **mais raso** que o valor-alvo óptico puro, para não escurecer o centro além do ponto de saturação perceptual.
- **Pontuação:** completa explica a ordem onde/quanto com o mecanismo de todas as zonas atravessadas, prevê o risco de intensificar a zona errada, e classifica a faixa como cor cheia com o ajuste correspondente; parcial afirma a ordem de decisão sem o mecanismo, ou erra a classificação da faixa.

**16. Resposta: b).** O GemRay modela absorção por caminho óptico e dispersão (traçado separado de vermelho, verde e azul) — ele **não ignora** cor. A lacuna real é que ele usa uma **cor única atribuída pelo operador**: zonação, pleocroísmo e variação de saturação dentro da peça ficam fora do modelo. Uma safira zonada é lida como safira de cor média uniforme — o escurecimento por profundidade aparece na simulação, a faixa não. **a)** é a afirmação **falsa** que a auditoria científica derrubou (era a espinha da aula 06 antes da correção) — um distrator deliberadamente sedutor para quem leu uma versão desatualizada do assunto. **c)** e **d)** exageram o limite real a ponto de negar capacidades documentadas da ferramenta.

**17.** Resposta esperada.
- **(a)** **GemCad** especifica a geometria do diagrama de lapidação — ângulo, índice de posição e altura de cada faceta — e verifica o encontro de facetas (*meetpoint*). **GemRay** é um programa **autônomo**, do mesmo autor (Robert W. Strickland), distribuído separadamente, que abre os arquivos do GemCad e simula o comportamento óptico dessa geometria. Não é "módulo" do GemCad porque roda como programa independente, não como uma função embutida do primeiro — o GemCad trata da forma, o GemRay trata da aparência.
- **(b) As três lacunas reais:** (1) **cor uniforme, não real** — o modelo usa uma cor única atribuída pelo operador; zonação, pleocroísmo e variação de saturação ficam fora. (2) **textura e qualidade do material real** — o modelo idealizado assume ausência de inclusões, fraturas e variação de polimento, que um bruto real quase nunca tem. (3) **preferência estética** — a métrica agrega tudo num único número, mas quanto de brilho vale quanto de fogo, ou se a cintilação densa é preferível à ampla, é julgamento de gosto que a ferramenta não decide.
- **(c)** Porque ela **reúne** o que cada aula anterior tratou de forma isolada ou aproximada (princípio na a01, tabela na a02, os três efeitos na a03, os dois compromissos nas a04/a05) num cálculo específico faceta por faceta — e porque só depois de conhecer princípios, valores de referência e compromissos qualitativos é que faz sentido apresentar a ferramenta que os quantifica com precisão, junto com os limites do que ela não resolve.
- **Pontuação:** completa distingue os dois programas pela função e autonomia, nomeia as três lacunas reais sem citar a lacuna falsa, e explica a posição de fechamento pela integração dos conteúdos anteriores; parcial nomeia duas das três lacunas ou confunde GemRay com módulo do GemCad.

**18.** Resposta esperada.
- **(a)** A métrica alta garante que a **geometria**, faceta por faceta, devolve eficientemente a luz simulada dentro do ângulo de observação do software — a reflexão interna total está bem resolvida para esse desenho específico, um resultado mais fino do que a tabela da aula 02 sozinha confirmaria.
- **(b)** Se a variação núcleo–borda for informada como uma **única** cor, a simulação não a captura — o modelo trabalha com o valor atribuído, uniforme. Se for tratada como **zonação real** (não uniforme), o que fica de fora é justamente a distribuição espacial da cor dentro da peça: o GemRay modela absorção por caminho óptico sobre uma cor atribuída pelo operador, não sobre a variação real ponto a ponto do material.
- **(c)** A inclusão revela o limite do **modelo idealizado**: o software assume uma pedra sem inclusões, sem fraturas e sem variação de polimento entre facetas. Uma inclusão real espalha e absorve luz de formas que o modelo não representa — é uma lacuna de **textura e qualidade do material**, independente de qualquer questão de cor.
- **(d)** Não. A métrica agrega o comportamento simulado num único número, mas a escolha entre mais brilho ou mais fogo é uma ponderação estética — quanto de um vale quanto do outro — que a ferramenta não resolve; ela pode dizer que um desenho devolve mais luz simulada que outro, não que ele é a escolha certa.
- **Pontuação:** completa distingue os três limites (cor uniforme, textura do material, preferência estética) aplicando cada um corretamente ao caso da turmalina; parcial identifica um ou dois dos limites, ou trata a inclusão como problema de cor em vez de textura do material.

</details>

## Cobertura

- **Decisão: questionário único.** O módulo tem 6 aulas — no limiar de "~5–6 aulas" da skill. As seis formam **um bloco temático coeso e sequencial**: o princípio (a01) → os valores publicados e sua base física (a02) → os três efeitos que esses valores servem (a03) → o que eles custam em peso (a04) → o que eles custam em cor (a04→a05, mesma variável) → o que a ferramenta calcula e o que não calcula (a06, que fecha reunindo as cinco anteriores). Não há dois sub-blocos que se sustentem como parciais independentes — a a06 depende explicitamente de todas as cinco anteriores, o que tornaria qualquer corte em "parcial 1 / parcial 2" artificial. Os módulos 03, 04, 05 e 06 deste curso, todos com 6 aulas, usaram questionário único pela mesma razão de coesão; segue-se o critério da skill (coesão temática), não o número cru de aulas. Um único questionário de 18 questões, com peso reforçado em aplicação/distinção nos pontos mais sutis do módulo (oa02 e oa05), cumpre o papel de recuperação integrada. Nenhum questionário parcial nem final cumulativo.
- **Objetivos cobertos: 6 de 6, cada um com 3 questões** (mínimo do curso é 2; os módulos recentes fazem 3) — matriz **sem célula vazia**:
  - `lapidacao-m08-oa01` — Q01, Q02, Q03
  - `lapidacao-m08-oa02` — Q04, Q05, Q06
  - `lapidacao-m08-oa03` — Q07, Q08, Q09
  - `lapidacao-m08-oa04` — Q10, Q11, Q12
  - `lapidacao-m08-oa05` — Q13, Q14, Q15
  - `lapidacao-m08-oa06` — Q16, Q17, Q18
- **Distribuição por tipo (18 questões):** 6 múltipla escolha (Q01, Q04, Q07, Q10, Q13, Q16); 5 verdadeiro/falso com justificativa (Q02, Q05, Q08, Q11, Q14); 2 dissertativa curta (Q06, Q17); 5 de aplicação sobre caso novo, não trabalhado nas aulas (Q03, Q09, Q12, Q15, Q18) — os casos usam materiais diferentes dos exemplos das aulas (granada, topázio, turmalina, espinélio, safira zonada), nunca reciclando o exato caso trabalhado.
- **Calibração cognitiva:** os OA de "analisar" (oa03, oa04, oa05) recebem cada um pelo menos uma questão de comparação real entre duas alternativas sobre o mesmo material ou bruto fixo — oa03 com turmalina em degrau × brilhante isolando o efeito da dispersão baixa do material (Q09); oa04 com as duas rotas de projeto do espinélio e a recusa do rótulo "corte nativo" pelo critério errado (Q12); oa05 com a ordem de decisão orientação-antes-de-profundidade na safira zonada (Q15). O OA de "explicar" com maior densidade conceitual (oa02) recebe a questão dissertativa mais longa do questionário (Q06, piso-com-teto). O OA de fechamento (oa06) recebe a questão de aplicação mais longa (Q18), articulando os três limites reais do ray tracing sobre um único caso.
- **Distratores e afirmações-isca ancorados nas regras que a auditoria científica corrigiu ou inverteu** (armadilhas didáticas naturais, listadas no achado 6 da revisão didática):
  - **extinção como absorção** — Q01(a): o mecanismo correto é escape na segunda faceta, RIT sem perda.
  - **ângulo medido contra o plano da faceta** — Q02: o ângulo relevante é sempre contra a normal.
  - **alvo deduzido do crítico / faixa determina o valor** — Q04(a) e Q04(c): o pavilhão publicado é por material, não derivado da fórmula nem da faixa.
  - **margem que encolhe com o índice** — Q05: a margem cresce (quartzo 1,5°, safira 7,6°).
  - **coríndon 38°–40°** substituído pelo valor correto (42°) em toda referência do questionário — nenhuma questão reproduz o erro antigo, mesmo como distrator.
  - ***brilliance* como sinônimo de *brightness*** — Q07(a): *brilliance* é o guarda-chuva da USFG.
  - **fogo sem limite de resolução** — Q08: existe um ponto de retorno decrescente, sem valor fixado (não cobrado como número).
  - **pavilhão raso como só cautela** — Q10(a): é a manobra de rendimento mais comum, e a origem mais comum do janelamento.
  - **culaça como defeito** — Q11: é escolha deliberada de durabilidade.
  - **corte nativo como sinônimo neutro de "reter peso"** — Q12(c): o critério real é origem e método.
  - **ajuste de cor decidido pelo índice** — Q13(a) e Q14: a direção depende da saturação de origem, não do índice.
  - **GemRay ignora cor** — Q16(a): a lacuna real é a uniformidade da cor, não a ausência dela.
  - **GemRay como módulo do GemCad** — Q17(a): são dois programas autônomos do mesmo autor.
  - **margem numérica de 2,5° da a01 tratada como valor de projeto** — não aparece em nenhuma questão nem gabarito como número a decorar; onde a margem é cobrada (Q05, Q06), é pelo raciocínio, não por um valor fixo.
- **Declarações de LC-08 (controvérsia) não cobradas como se tivessem resposta fechada:** nem o limite de resolução do olho para o fogo (a03, tocado em Q08 apenas como "existe, sem valor fixo") nem a disputa sobre o termo "corte nativo" (a04, tocado em Q12 apenas como recusa de um uso impróprio, não como definição fechada de vencedor do debate) recebem gabarito que arbitre a controvérsia.
- **Nível teórico preservado:** nenhuma questão pede ou avalia destreza de bancada — não se pergunta como ajustar o batente de ângulo, como operar a facetadora, como instalar ou rodar GemCad/GemRay, nem "o que você faria" na máquina. Todas cobram princípio, geometria, causa-efeito, ordem de grandeza, escopo e limite. GemCad e GemRay aparecem só como objeto de **consciência de ferramenta** (Q16, Q17, Q18), nunca como tutorial.
- **Avisos da revisão didática atendidos** (bloco `modules[08].didactic_review.desalinhamento_aula_avaliacao`, 9 itens):
  1. **Proibição da forma "dada a faixa de índice X, qual o ângulo-alvo?"** — nenhuma questão de `oa02` (Q04, Q05, Q06) tem essa forma; Q04 cobra a distinção entre as duas colunas, Q05 cobra a margem, Q06 cobra a base física.
  2. **Questão sobre a MARGEM, não sobre o alvo** — Q05 (V/F sobre a margem encolher) e Q06(c) (consequência do piso-com-teto sobre a margem) cobrem exatamente o resultado mais contraintuitivo do módulo.
  3. **Caso de `oa05` em que a direção não é dedutível da tabela da a02** — Q13 e Q15 usam materiais de mesmo índice com saturações opostas (ou tratam a saturação como a variável decisiva), na estrutura do exemplo das duas granadas.
  4. **`oa06` não cobra "o ray tracing não modela cor" em nenhuma forma** — Q16(a) usa exatamente essa afirmação como distrator errado e sedutor, nunca como gabarito.
  5. **`oa04` trata pavilhão raso como manobra de rendimento, não erro conservador** — Q10(b) é o gabarito; Q10(a) é o distrator que reintroduziria o erro.
  6. **Armadilhas legítimas da auditoria como distratores** — listadas acima; nenhuma delas aparece como resposta correta em lugar algum do questionário.
  7. **Margem de 2,5° da a01 não cobrada como valor de projeto** — confirmado acima.
  8. **Declarações de LC-08 sem resposta fechada** — confirmado acima.
  9. **Nível teórico sem nenhuma pergunta de ajuste, medição ou operação de facetadora/software** — confirmado acima; varredura sem achado.

<!--
nivel: ensino-medio-com-gemologia-v1
questoes: 18
decisao_quantidade: 'questionario unico — 6 aulas no limiar de ~5-6 da skill, bloco tematico coeso e sequencial (principio -> valores e base fisica -> tres efeitos -> custo em peso -> custo em cor, mesma variavel -> o que a ferramenta calcula e nao calcula, a06 dependente de todas as cinco anteriores) sem sub-blocos independentes; mesmo criterio e mesma escolha dos modulos 03, 04, 05 e 06 (6 aulas, questionario unico)'
cobertura:
  lapidacao-m08-oa01: [lapidacao-m08-q01, lapidacao-m08-q02, lapidacao-m08-q03]
  lapidacao-m08-oa02: [lapidacao-m08-q04, lapidacao-m08-q05, lapidacao-m08-q06]
  lapidacao-m08-oa03: [lapidacao-m08-q07, lapidacao-m08-q08, lapidacao-m08-q09]
  lapidacao-m08-oa04: [lapidacao-m08-q10, lapidacao-m08-q11, lapidacao-m08-q12]
  lapidacao-m08-oa05: [lapidacao-m08-q13, lapidacao-m08-q14, lapidacao-m08-q15]
  lapidacao-m08-oa06: [lapidacao-m08-q16, lapidacao-m08-q17, lapidacao-m08-q18]
tipo_distribuicao: '6 multipla escolha (q01,q04,q07,q10,q13,q16); 5 verdadeiro/falso com justificativa (q02,q05,q08,q11,q14); 2 dissertativa curta (q06,q17); 5 aplicacao sobre caso novo (q03,q09,q12,q15,q18)'
celulas_vazias: 0
regras_invertidas_como_distratores: 'extincao como absorcao (q01); angulo contra o plano da faceta em vez da normal (q02); alvo deduzido do critico ou da faixa (q04); margem que encolhe com o indice (q05); coríndon 38-40 graus nunca reproduzido; brilliance como sinonimo de brightness (q07); fogo sem limite de resolucao (q08); pavilhao raso so como cautela (q10); culaca como defeito (q11); corte nativo como sinonimo neutro de reter peso (q12); ajuste de cor decidido pelo indice em vez da saturacao (q13,q14); GemRay ignora cor (q16); GemRay como modulo do GemCad (q17)'
avisos_revisao_didatica_atendidos: 'os nove itens de modules[08].didactic_review.desalinhamento_aula_avaliacao estao atendidos: (1) nenhuma questao de oa02 na forma proibida faixa->alvo; (2) q05 e q06c cobram a margem crescente; (3) q13/q15 usam caso em que a direcao do ajuste nao sai da tabela da a02; (4) q16a usa "GemRay ignora cor" so como distrator errado, nunca gabarito; (5) q10b trata pavilhao raso como manobra de rendimento; (6) armadilhas da auditoria como distratores em q01/q02/q04/q05/q07/q08/q10/q11/q12/q13/q16/q17; (7) margem de 2,5 graus da a01 nao cobrada como numero de projeto; (8) declaracoes de LC-08 (limite de resolucao do fogo, disputa de corte nativo) sem resposta fechada; (9) varredura de competencia de bancada sem achado'
-->
