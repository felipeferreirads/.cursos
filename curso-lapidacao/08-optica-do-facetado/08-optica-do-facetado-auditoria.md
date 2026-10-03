# Auditoria científica — Módulo 08: Óptica do talhe facetado

> [!info] Curso de **Teoria da lapidação** · módulo 08 de 14 · modo **`audit-and-fix`** · profundidade **full** · auditado em **2026-09-04** · **corrigido em 2026-09-04**

**Veredito final: APROVADO — os 16 achados estão fechados.**
*(Veredito da auditoria, antes da correção: reprovado.)*

| Severidade | Achados | Desfecho |
|---|---|---|
| 🔴 Erro | **4** | 4 corrigidos |
| 🟠 Impreciso | **8** | 8 corrigidos |
| 🟡 Desatualizado | 0 | — |
| 🔵 Sem fonte | **2** | 1 reatribuído, 1 requalificado |
| ⚪ Controverso | **2** | 2 declarados como controvérsia (os primeiros LC-08 do módulo) |
| **Total** | **16** | **0 em aberto** |
| ✅ Verificado e correto | **23** alegações | 3 delas tocadas por propagação — ver abaixo |

**Gate do curso: LIBERADO.** Nenhum 🔴 ou 🟠 em aberto. Pipeline dos módulos 06+: aulas → auditoria → **correção (concluída)** → **revisão didática** → questionário(s). O questionário **não** deve ser gerado antes da revisão didática. Flashcards seguem dispensados (decisão de 2026-09-04).

**Concentração do dano:** 3 dos 4 🔴 estavam na **aula 02**, e o quarto na **aula 06**, vazando para a aula 05. As aulas 01, 03 e 04 saíram com achados 🟠 pontuais e nenhum erro estrutural.

**Palavras de corpo (LC-02), antes → depois da correção:** a01 1589 → **1576** · a02 1566 → **1543** · a03 1597 → **1592** · a04 1615 → **1605** · a05 1612 → **1599** · a06 1624 → **1602**. Cada acréscimo foi financiado por corte de redundância da própria aula, o método dos módulos 04 a 07; as seis entraram e saíram sob o teto.

---

## Como ler este relatório depois da correção

Cada achado abaixo mantém o texto original da auditoria — o trecho literal citado é o que **estava escrito antes**, não o que está no arquivo agora. Ao fim de cada achado foi acrescentada uma linha **Desfecho** dizendo o que foi efetivamente aplicado. Os quatro achados que exigiram julgamento (2 🔵 e 2 ⚪) trazem a decisão e a justificativa por extenso, e as mesmas notas estão no campo `decision_note` do manifesto `.json`.

### Decisões de julgamento, em resumo

| Achado | Decisão | Por quê |
|---|---|---|
| 🔵 13 `RAY-FONTE-USFG-001` | **Reatribuir** a fonte, não remover a alegação | O conteúdo está correto e tem fonte própria; o que estava quebrado era a rota de verificação. Difere do 🔵 do módulo 07, que foi **removido** porque ali nenhuma fonte sustentava o conteúdo. |
| 🔵 14 `ANG-EX-QUARTZO-001` | **Requalificar** o número, não removê-lo nem trocá-lo | O resto do exemplo está confirmado contra a USFG. O 2,5° passa a ser declarado como a leitura aritmética do exemplo (43 − 40,5), com a formulação da fonte ("vários graus") ao lado. Precedente do módulo 07: não inventar valor novo. |
| ⚪ 15 `BRI-PROJ-COMPR-001` | **Declarar** como pergunta aberta, na aula 03 | Divergência real na literatura de talhe. Prosa com abertura "Pergunta em aberto:", a convenção fixada na revisão didática do módulo 07. |
| ⚪ 16 `FAC-REN-NATIVO-001` | **Declarar** como ponto em aberto, na aula 04 | Idem, e entra dentro da reescrita que o 🟠 11 já exigia, a custo de três linhas. |

**Sobre haver duas declarações LC-08 e não uma.** Os módulos 06 e 07 instalaram **uma** cada, e registraram que "uma basta". O critério real daquelas decisões, porém, não era a contagem: era a **genuinidade** — a segunda candidata do módulo 07 foi descartada por ser decisão de eficiência de oficina, não divergência sobre um fato, e portanto encenação num curso teórico. As duas deste módulo passam nesse critério: ambas são divergências documentadas entre fontes, cada uma no coração do objetivo da sua aula. O módulo entrou com **zero** declarações de controvérsia nas seis aulas e sai com duas, nas duas aulas em que havia disputa real.

**Sobre o `claim_id` da aula 01 — `ANG-` mantido.** O `_contexto.md` dá `FAC-ANG-CRIT-001` numa lista de **cinco exemplos de formato** (ao lado de `CAB-DOM-CURV-001`, `ABR-GRAO-SEQ-001`, `DOP-TRAN-RISK-001`, `TRT-EST-RESIN-001`), nenhum dos quais existe como `claim_id` real em aula alguma do curso — é exemplar de formato, não registro de atribuição. Renomear quebraria a regra dura de 4 segmentos em quatro dos seis identificadores (`ANG-EXTIN-CAUSA-001` viraria `FAC-ANG-EXTIN-CAUSA-001`, com **cinco**), ou exigiria reinventar os seis com perda de informação no nome. Não há colisão: `ANG-` foi cruzado por regex contra todos os `claim_id` dos módulos 01–07 e não aparece como primeiro segmento em nenhum. E o próprio redator já usou prefixo composto onde ele resolve um problema real — `FAC-REN-` na aula 04, para não colidir com os `REN-` do módulo 05. **Divergência registrada como aceitável**, não como pendência.

---

## Achados 🔴 — erro

### 🔴 1. A tabela de ângulos-alvo por faixa de índice não corresponde aos valores publicados, e a atribuição de fonte é falsa

**claim_id:** `TAB-ALVO-FAIXA-001`
**Tipo:** erro factual + atribuição de fonte falsa
**Onde:** aula 02 · "A tabela — valores de referência por faixa"; repetida no "Recap relâmpago"

**Está escrito:** as seis faixas com alvo de pavilhão ≈45°–46° (IR 1,43–1,46), ≈42°–43° (1,50–1,55), ≈40°–41° (1,56–1,65), ≈39°–40° (1,66–1,75), **≈38°–40° (coríndon)**, ≈40,75° (diamante) — declaradas como "os valores de referência correntes na literatura de facetamento amador", com fonte "United States Faceters Guild — tabela de ângulo crítico e ângulos de pavilhão recomendados por índice de refração para o brilhante redondo".

**Problema:** dois problemas independentes, ambos graves.

**(a) Os valores estão errados, e a estrutura decrescente da tabela não existe na literatura.** A tabela publicada pelo International Gem Society para ângulo de pavilhão principal por material dá: quartzo 42°, **berilo 43°**, turmalina 42°, topázio 41°, peridoto 42°, espinélio 41°, **coríndon/safira 42°**, zircão 41°, granada 39°–41°. Os valores reais são praticamente **planos** na faixa 40°–43° para toda a gama de gema comum, e o berilo (IR 1,57) recebe um pavilhão *mais fundo* que o quartzo (IR 1,54) — o oposto da tendência que a aula ensina. O erro individual mais grave é o **coríndon: a aula manda 38°–40°, a literatura manda 42°**, uma diferença de 2° a 4° num valor que a aula apresenta como referência de projeto.

**(b) A USFG não publica essa tabela e diz explicitamente o contrário.** A página *Refractive Index and Critical Angle* da USFG traz apenas uma tabela de índices de refração — sem coluna de ângulo crítico e sem coluna de ângulo-alvo — e remete a Sinkankas, *Gemstone & Mineral Data Book*, para os ângulos recomendados, sem reproduzi-los. O artigo *Choosing the Best Angles for Your SRB*, da mesma USFG, fecha com: **"There simply is no magic bullet or universal set of angles"** — e publica um único conjunto, para IR 1,54 (pavilhão mains 43,00°, breaks 41,00°; coroa mains 32,00°, breaks 28,00°, stars 13,00°). A tabela de seis faixas da aula 02 não tem origem localizável em nenhuma das fontes declaradas.

**Correção proposta:** substituir a tabela de seis faixas por (i) o conjunto de ângulos da USFG para IR 1,54, declarado como tal; (ii) uma lista de ângulos de pavilhão principais por material da tabela do IGS; e (iii) a constatação — que é a lição realmente defensável e mais interessante — de que **os ângulos publicados são quase planos em 40°–43° apesar de o ângulo crítico variar de ~44° a ~24°**, porque o que trava o pavilhão por cima não é a reflexão interna total, e sim a exigência de a luz sair pela coroa. Reescrever a fonte como "IGS, tabela de propriedades para facetamento; USFG, *Choosing the Best Angles for Your SRB* (conjunto para IR 1,54)". Manter o diamante como linha à parte, com fonte Tolkowsky.

**Fonte:** [USFG, *Refractive Index and Critical Angle*](https://usfacetersguild.org/refractive-index-and-critical-angle/) · [USFG, *Choosing the Best Angles for Your SRB*](https://usfacetersguild.org/choosing-the-best-angles-for-your-srb/) · [IGS, *Faceting Made Easy, Part 1: Gemstone Properties*](https://www.gemsociety.org/article/faceting-made-easy-part-1-gemstone-properties/) — consultadas em 2026-09-04
**Nível:** base de referência do ofício · **Confiança:** confirmado
**Também aparece em:** aula 02 "Recap relâmpago"; aula 04 (referências ao "ângulo-alvo da aula 02"); aula 05 ("valor-alvo da aula 02"); aula 06 (exemplo trabalhado). As referências das aulas 04/05 são genéricas e sobrevivem à correção; a da aula 06 não — ver 🟠 12.

> **Desfecho — CORRIGIDO em 2026-09-04.** A tabela de seis faixas foi substituída por uma tabela de quatro colunas: faixa de IR, **ângulo crítico calculado** (declarado como derivado, não copiado), material, e **pavilhão principal publicado pelo IGS, material a material** — quartzo 42°, berilo 43°, turmalina 42°, topázio 41°, peridoto 42°, espinélio 41°, coríndon 42°, zircão 41°, granada 39°–41°, diamante 40,75°. O conjunto da USFG para IR 1,54 (pavilhão *mains* 43,00°, *breaks* 41,00°; coroa *mains* 32,00°, *breaks* 28,00°, *stars* 13,00°) entrou declarado como tal, com a citação literal da advertência de que não existe conjunto universal. A lição do caráter **plano** dos valores em 40°–43° contra um crítico que despenca de 44° a 24° virou o parágrafo de leitura da tabela. Fontes reescritas: IGS, USFG (as duas páginas, com a nota de que a página de *Refractive Index* não publica coluna de ângulo-alvo), Tolkowsky via OctoNus. A entrada de vocabulário de "ângulo-alvo" foi ajustada para dizer que o valor é publicado **por material**, não por faixa.

---

### 🔴 2. Berilo e zircão estão nas faixas de índice erradas

**claim_id:** `TAB-ALVO-FAIXA-002` *(novo — o erro é de exemplo de material, não do valor de ângulo)*
**Tipo:** erro factual
**Onde:** aula 02 · coluna "Exemplo de material" da tabela

**Está escrito:** "1,50 – 1,55 … quartzo, **berilo (extremo baixo)**" e "1,66 – 1,75 … peridoto, espinélio, **zircão (extremo baixo)**".

**Problema:**
- **Berilo não existe na faixa 1,50–1,55.** O índice de refração do berilo é **1,562–1,602** (esmeralda 1,577–1,583; água-marinha 1,567–1,590). Não há berilo em 1,55 nem abaixo. O berilo já aparece — corretamente — na faixa 1,56–1,65 da mesma tabela, de modo que o material está listado duas vezes, uma delas numa faixa fisicamente impossível.
- **Zircão de gema não existe na faixa 1,66–1,75.** O zircão vai de **1,810 a 2,024**; o zircão *high*, que é o de qualidade gema, fica em 1,92–1,98. Só o zircão metamíctico (*low*, danificado por radiação) desce a ~1,75, tocando a borda da faixa — e é justamente o material que menos se faceta. Apresentar o zircão como exemplo desta faixa ensina uma associação errada que o aluno carregará.

**Correção proposta:** remover "berilo (extremo baixo)" da faixa 1,50–1,55, deixando quartzo (e, se quiser um segundo exemplo, calcedônia). Remover "zircão (extremo baixo)" da faixa 1,66–1,75 e substituir por granada piropo (1,72–1,76); mover o zircão para uma faixa alta própria, ou citá-lo apenas com a ressalva "zircão *low*/metamíctico, ~1,75 — o zircão de gema fica em 1,92–1,98".

**Fonte:** [Wikipedia, *Zircon*](https://en.wikipedia.org/wiki/Zircon) (IR 1,810–2,024; distinção high/low) · [Sosna Gems, *Gemstone Refractive Index chart*](https://sosnagems.com/blogs/gemstone-guides/guide-gemstone-refractive-index) (berilo 1,562–1,602; metamíctico ~1,75) — consultadas em 2026-09-04
**Nível:** base de referência · **Confiança:** confirmado
**Também aparece em:** só na aula 02. A aula 03 usa o zircão como exemplo de dispersão, sem citar índice — não é afetada.

> **Desfecho — CORRIGIDO em 2026-09-04.** Berilo saiu da faixa 1,50–1,55 (que ficou com quartzo e calcedônia) e permanece só na 1,56–1,65. O zircão saiu da faixa 1,66–1,75, substituído por granada piropo, e ganhou linha própria em 1,81–2,02. Um parágrafo curto de ressalva de material foi instalado com os valores: berilo 1,562–1,602; zircão 1,810–2,024, *high* de gema em 1,92–1,98, *low* metamíctico descendo a ~1,75. Alegação nova `TAB-ALVO-FAIXA-002` instalada no rodapé.

---

### 🔴 3. A "segunda base física" da tabela conclui o oposto do que o próprio exemplo trabalhado demonstra

**claim_id:** `TAB-BASE-FISICA-001`
**Tipo:** inconsistência interna + certeza indevida
**Onde:** aula 02 · "A base física: por que índice mais alto tolera pavilhão mais raso"; contradita em "Exemplo trabalhado", passos 3 e 4

**Está escrito:** "materiais de índice alto não apenas partem de um piso mais baixo, mas também **toleram uma margem proporcionalmente menor** sobre esse piso — o ângulo-alvo final **cai ainda mais rápido com o índice** do que só o ângulo crítico sozinho preveria."

**Problema:** o exemplo trabalhado da mesma aula, três parágrafos adiante, calcula exatamente o contrário e diz isso em voz alta: "a diferença entre os ângulos críticos (6,1°) é **maior** que a diferença entre os ângulos-alvo (3,5°) … a safira, de índice mais alto, tem **margem absoluta maior**, não menor". O ângulo-alvo cai *mais devagar* que o crítico, não mais rápido. E a margem também é **proporcionalmente** maior para a safira, não menor: quartzo 2,0°/40,5° = 4,9%; safira 4,6°/34,4° = 13,4%. Com os valores corretos do 🔴 1 (quartzo 42°, coríndon 42°) a contradição fica ainda mais forte: margem do quartzo 1,5°, margem do coríndon 7,6°.

O mecanismo físico invocado é real e vale a pena preservar — a refração na mesa de fato confina os raios internos a um cone de meio-ângulo igual a arcsin(1/n), que é **exatamente o ângulo crítico**, e portanto mais estreito quanto maior o índice. O que está errado é a conclusão tirada dele. O mecanismo que de fato governa o limite superior do ângulo de pavilhão, e que a aula omite, é a exigência de que a luz **saia pela coroa** depois da segunda reflexão — é ele que mantém o alvo em 40°–43° para quase todo material, independentemente do índice.

**Correção proposta:** reescrever a seção para: (i) manter o fato elegante de que o cone interno tem meio-ângulo igual ao ângulo crítico; (ii) trocar a conclusão para "por isso o **piso** cai com o índice"; (iii) introduzir o teto — a luz precisa sair pela coroa —, que não cai com o índice; (iv) concluir que o alvo publicado fica quase plano porque está espremido entre um piso que desce e um teto que não desce, e que **é por isso** que a margem sobre o crítico cresce com o índice, como o exemplo trabalhado mostra. Assim o exemplo passa a confirmar a teoria em vez de refutá-la.

**Fonte:** aritmética direta sobre os valores da própria aula (verificada: θc(1,54) = 40,49°; θc(1,77) = 34,40°) · [OctoNus, *The "Diamond Design" by Tolkowsky (1919)*](https://www.octonus.com/projects/diamond-cut-study/the-diamond-design-by-tolkowsky-1919) para a restrição de saída pela coroa — consultadas em 2026-09-04
**Nível:** cálculo direto + fonte histórica primária · **Confiança:** confirmado
**Também aparece em:** aula 02 "Recap relâmpago", segundo marcador, que repete a formulação errada.

> **Desfecho — CORRIGIDO em 2026-09-04.** Seção reescrita e **retitulada** — de "por que índice mais alto tolera pavilhão mais raso" (que afirmava justamente o que o achado derrubou) para **"A base física: um piso que desce e um teto que não desce"**. O cone interno de meio-ângulo igual ao crítico foi preservado como propriedade do **piso**; entrou o **teto** — a luz precisa sair pela coroa depois de refletir, restrição que não cai com o índice; e a conclusão passou a ser que o alvo publicado fica espremido entre os dois, ficando quase plano, com a **margem crescendo** com o índice. O exemplo trabalhado agora **confirma** a seção em vez de contradizê-la. O marcador do Recap foi reescrito na mesma direção.

---

### 🔴 4. GemRay modela cor, absorção por caminho óptico e dispersão — a "lacuna de cor" que a aula 06 apresenta como central é falsa

**claim_id:** `RAY-LIMITE-COR-001` (e, por tabela, `RAY-LIMITE-PERCEP-001`)
**Tipo:** erro factual
**Onde:** aula 06 · "O que essas métricas não capturam", bloco **Cor**; "Recap relâmpago"; **propagado** para a aula 05, "O que não concluir"

**Está escrito (aula 06):** "As ferramentas de ray tracing tradicionalmente usadas em facetamento amador foram construídas para otimizar o comportamento de luz branca num material tipicamente incolor ou de cor não modelada; a absorção seletiva por comprimento de onda que produz a cor de uma gema colorida … não é, em geral, o que essas simulações calculam."
**Está escrito (aula 05):** "a aula 06 declara explicitamente que ferramentas como GemCad e GemRay, na configuração corrente, **não modelam bem absorção de cor**."

**Problema:** o GemRay — que é a ferramenta nomeada — faz exatamente as duas coisas que a aula diz que ele não faz. A documentação do autor descreve que o programa permite **selecionar a cor do material** e que **"quanto mais longe um raio viaja através do material, mais a luz é absorvida"** — isto é, o GemRay implementa precisamente o mecanismo de caminho óptico × absorção que a aula 05 ensina, e que a aula 06 afirma estar fora do alcance dele. Além disso o GemRay **traça os raios vermelho, verde e azul separadamente** e combina os três numa imagem colorida, ou seja, modela dispersão. E gera **animações de basculamento (tilt)**, o que enfraquece também `RAY-LIMITE-PERCEP-001` ("métrica estática", "fotografia congelada").

Este é o achado de maior custo do módulo, porque a lacuna falsa é a **espinha da aula 06**: ela é apresentada como a primeira das "três lacunas" e como a justificativa de a aula fechar o módulo. E porque a aula 05 a repete como fato estabelecido.

**Correção proposta:** trocar a lacuna "cor" por uma lacuna verdadeira e melhor. Duas honestas e verificáveis: (i) o modelo de cor do GemRay usa uma **cor uniforme escolhida pelo operador**, e portanto não representa zonação, pleocroísmo nem variação real de saturação dentro da peça — o que preserva integralmente a lição da aula 05 sobre a ordem "orientação antes de profundidade"; (ii) a métrica agrega em um número uma preferência estética que não é redutível a número. Na aula 05, trocar "não modelam bem absorção de cor" por "modelam absorção com uma cor uniforme atribuída, não com a zonação real do bruto". Reescrever o exemplo trabalhado da aula 06 em conformidade: a simulação *teria* apontado o escurecimento da safira de cor cheia; o que ela não pega é a zonação em faixas.

**Fonte:** [GemCad.com — *GemRay for Windows*](https://www.gemcad.com/gemray.html) e [manual do GemRay, Robert W. Strickland, 2012](https://www.gemcad.com/downloads/gemrayman.pdf) — consultadas em 2026-09-04
**Nível:** documentação do autor da ferramenta (normativa para a alegação) · **Confiança:** confirmado
**Também aparece em:** aula 05 "O que não concluir", 3º marcador (mesma afirmação, propagada); aula 06 "Recap relâmpago", 4º marcador; aula 06 "Erros comuns", 1º marcador.

> **Desfecho — CORRIGIDO em 2026-09-04.** A lacuna falsa foi substituída pelas duas verdadeiras propostas. A seção "O que essas métricas não capturam" agora **abre desfazendo a suposição**: o GemRay escolhe cor de material, traça vermelho, verde e azul em separado (logo, modela dispersão), absorve proporcionalmente ao caminho óptico e gera animações de basculamento. As três lacunas passaram a ser **cor uniforme, não cor real** (zonação, pleocroísmo e variação de saturação fora do modelo), **textura e qualidade do material** e **preferência estética** (a métrica agrega num número uma ordenação de gosto). O exemplo trabalhado foi reescrito: a simulação *teria* apontado o escurecimento por profundidade; o que ela não pega é a zonação em faixas. Na **aula 05**, "não modelam bem absorção de cor" virou a formulação correta — o mecanismo está no alcance do GemRay, mas sobre cor uniforme atribuída, não sobre a zonação real do bruto —, e a linha de "Próxima aula" foi realinhada. `RAY-LIMITE-PERCEP-001` foi realocada junto (ver propagação, ao final).

---

## Achados 🟠 — impreciso

### 🟠 5. A extinção é atribuída a perda por absorção e a reflexão "não perfeitamente eficiente"; a reflexão interna total não tem perda

**claim_id:** `ANG-EXTIN-CAUSA-001`
**Tipo:** erro de mecanismo (confusão de escopo)
**Onde:** aula 01 · "O outro extremo: pavilhão fundo demais"

**Está escrito:** "uma fração crescente da luz é absorvida a cada reflexão (nenhuma superfície real reflete 100,000% de forma perfeitamente eficiente ao longo de múltiplos percursos) ou é redirecionada para fora da abertura angular que o olho do observador ocupa."

**Problema:** a **reflexão interna total não tem perda** — é o único regime de reflexão que devolve a totalidade da energia, e é por isso que a RIT é o fundamento do talhe facetado. Atribuir a extinção à ineficiência da reflexão contradiz o que a própria aula acabou de ensinar duas seções antes ("100% da luz é refletida"). Numa pedra incolor, a absorção ao longo do caminho é desprezível. O mecanismo real do pavilhão fundo demais é **vazamento**: depois da primeira reflexão, o raio atinge a faceta oposta do pavilhão **abaixo** do ângulo crítico e escapa pelo fundo — é o efeito conhecido no ofício como *nailhead*, "quando a pedra é cortada funda demais, a luz sai pelos lados, deixando uma sombra escura no centro". A segunda metade da frase da aula ("redirecionada para fora da abertura angular do observador") está correta e é o segundo mecanismo real.

Detalhe adicional: **"100,000%"** é erro de digitação (deveria ser "100%"), e a passagem inteira sai na correção.

**Correção proposta:** "…o raio, depois da primeira reflexão, atinge a faceta oposta do pavilhão com um ângulo **abaixo** do crítico e escapa pelo fundo — a luz não deixa de ser refletida na primeira faceta, ela se perde na segunda; e a parcela que ainda retorna sai fora da abertura angular que o olho do observador ocupa."
**Fonte:** [USFG, *Refractive Index and Critical Angle*](https://usfacetersguild.org/refractive-index-and-critical-angle/) (exemplo do pavilhão a 50°, "resultados mistos conforme o trajeto do raio") · literatura corrente de talhe sobre *nailhead* — consultadas em 2026-09-04
**Nível:** base de referência do ofício · **Confiança:** confirmado
**Também aparece em:** aula 01 "Erros comuns" (4º marcador) e "Recap relâmpago" (5º marcador) — ambos repetem "perde luz por absorção em múltiplos ricocheteios"; aula 04, `FAC-REN-PROF-001`, repete "caminho óptico mais longo, mais perda por absorção".

> **Desfecho — CORRIGIDO em 2026-09-04.** Passagem reescrita para o mecanismo real: a RIT se cumpre na **primeira** faceta e a luz se perde na **segunda**, que o raio atinge abaixo do crítico, escapando pelo fundo — o *nailhead* do ofício. Foi dito explicitamente que a RIT **não tem perda** e que numa pedra incolor a absorção no caminho é desprezível, o que remove a contradição com a seção anterior da própria aula. O "100,000%" saiu junto. "Erros comuns" ganhou um marcador dedicado ao equívoco, o marcador do Recap foi reescrito, e a propagação para `FAC-REN-PROF-001` na aula 04 foi aplicada no texto e no rodapé.

---

### 🟠 6. O papel da dispersão no ângulo de Tolkowsky está com o sinal invertido

**claim_id:** `TAB-DIAM-EXCE-001`
**Tipo:** causa-efeito invertida
**Onde:** aula 02 · "A tabela — valores de referência por faixa", parágrafo do diamante

**Está escrito:** "o ângulo de pavilhão de referência … não é 'pouco acima de 24°' — é ~40,75°, bem mais alto que o piso mínimo. A razão … **é o compromisso com a dispersão espectral**."

**Problema:** o **valor 40,75° está correto** e a atribuição a Tolkowsky está correta (pavilhão 40°45', coroa 34°30', mesa ~53%) — mas a direção do argumento está invertida. Tolkowsky escreve que a dispersão é o que **impede o ângulo de subir mais**, não o que o levanta acima do crítico: "*although a greater angle would give better reflection, this would not compensate for the loss due to the corresponding reduction in dispersion*". A dispersão é o **teto**, não o motivo de estar acima do piso. O que levanta o pavilhão muito acima de 24,4° é a geometria de saída — a luz precisa refletir duas vezes no pavilhão e **sair pela coroa** em direção ao observador.

Como está, a aula ensina "dispersão empurra o ângulo para cima", e o aluno aplicará esse raciocínio errado a qualquer material de dispersão alta.

**Correção proposta:** "…a razão de estar tão acima do piso é a exigência de que a luz, depois de refletir duas vezes no pavilhão, **saia pela coroa** na direção do observador — uma restrição geométrica que o ângulo crítico sozinho não expressa. A dispersão entra pelo lado oposto: Tolkowsky registra que um ângulo *maior* daria reflexão ainda melhor, mas não compensaria a perda de fogo — isto é, a dispersão é o que **impede o valor de subir**, não o que o levanta."
**Fonte:** [OctoNus, *The "Diamond Design" by Tolkowsky (1919)*](https://www.octonus.com/projects/diamond-cut-study/the-diamond-design-by-tolkowsky-1919) — transcrição da tese original, consultada em 2026-09-04
**Nível:** fonte primária histórica · **Confiança:** confirmado
**Também aparece em:** aula 02 "Erros comuns", 3º marcador ("tem causa física — o compromisso com a dispersão — detalhada na aula 03"); aula 02 "Próxima aula"; aula 02 "Recap relâmpago", 3º marcador.

> **Desfecho — CORRIGIDO em 2026-09-04.** O parágrafo do diamante passou a atribuir o valor alto à **exigência de saída pela coroa**, e a dispersão ao papel de **teto**, com a paráfrase de Tolkowsky (um ângulo maior daria reflexão melhor, mas não compensaria a perda de fogo). O marcador de "Erros comuns" foi trocado por um que ataca diretamente a inversão ("Achar que a dispersão empurra o ângulo do diamante para cima"), e a linha de "Próxima aula" foi reescrita para prometer o *fogo que impede o pavilhão de subir*, em vez da causa invertida.

---

### 🟠 7. GemRay é um programa autônomo do mesmo autor, não "um módulo" do GemCad — e o hedge sobre o nome é desnecessário

**claim_id:** `RAY-FERR-GEMCAD-001`
**Tipo:** imprecisão factual + certeza indevidamente baixa
**Onde:** aula 06 · "O que o ray tracing faz"; "Recap relâmpago"; "Erros comuns"

**Está escrito:** "**O módulo** de traçado de raios frequentemente citado junto a ele … é **conhecido na literatura do ofício como GemRay**"; "o módulo de traçado de raios associado, **referido na literatura como** GemRay"; e, no rodapé, "nomes e atribuição de autoria sujeitos a confirmação na auditoria científica".

**Problema:** três imprecisões numa alegação só. (1) **GemRay não é um módulo do GemCad** — é um programa autônomo, distribuído separadamente, que *abre os arquivos salvos pelo GemCad*. (2) O hedge "referido na literatura como" sugere um nome de tradição oral incerto; GemRay é o nome próprio e documentado do produto, escrito por **Robert W. Strickland** — o mesmo autor do GemCad —, publicado em gemcad.com, com manual do usuário datado de 2012. (3) A divisão de trabalho que a aula descreve está certa e é confirmada pelo autor: o GemCad trata da forma, o GemRay da aparência e do desempenho.

Vale registrar, embora a aula não afirme o contrário: Strickland aposentou-se em 2023 e liberou **GemCad e GemRay gratuitamente**, com o GemRay em código aberto. É informação útil ao nível de "consciência de ferramenta" que a aula declara ter como objetivo.

**Correção proposta:** "O programa companheiro de traçado de raios, do mesmo autor, é o **GemRay**: ele abre os arquivos salvos pelo GemCad e simula o comportamento óptico da geometria já especificada. Os dois cobrem as duas metades do problema — o GemCad trata da forma, o GemRay da aparência." Remover o hedge do rodapé (a confirmação foi feita). Corrigir "Erros comuns", 3º marcador, que diz "o módulo de ray tracing associado".
**Fonte:** [GemCad.com — *GemRay for Windows*](https://www.gemcad.com/gemray.html) · [GemCad.com — *GemCad for Windows*](https://www.gemcad.com/gemcad.html) · [manual do GemRay, Robert W. Strickland, 2012](https://www.gemcad.com/downloads/gemrayman.pdf) — consultadas em 2026-09-04
**Nível:** documentação do autor · **Confiança:** confirmado
**Também aparece em:** aula 06 "Recap relâmpago" (2º marcador) e "Erros comuns" (3º marcador).

> **Desfecho — CORRIGIDO em 2026-09-04.** GemRay passou a ser descrito como **programa autônomo do mesmo autor**, que abre os arquivos salvos pelo GemCad; o hedge "conhecido na literatura do ofício como" saiu, a autoria de **Robert W. Strickland** entrou por nome, e o registro da aposentadoria em 2023 com a liberação gratuita de ambos (GemRay em código aberto) foi acrescentado, como o achado sugeria. O hedge de rodapé "nomes e atribuição de autoria sujeitos a confirmação na auditoria científica" foi **removido**: a confirmação foi feita. "Erros comuns" e "Recap relâmpago" alinhados.

---

### 🟠 8. A coluna "ângulo crítico aproximado" da tabela tem três faixas mal arredondadas

**claim_id:** `TAB-ALVO-FAIXA-003` *(novo — a coluna de ângulo crítico é uma alegação separada da coluna de alvo)*
**Tipo:** dado numérico impreciso
**Onde:** aula 02 · coluna 2 da tabela

**Problema:** valores calculados por θc = arcsin(1/n) sobre os extremos declarados de cada faixa:

| Faixa de IR | Na aula | Correto | Nota |
|---|---|---|---|
| 1,43 – 1,46 | ≈ 44° | **≈ 43° – 44°** | valor único quebra o formato de faixa das outras linhas |
| 1,50 – 1,55 | ≈ 40° – 41° | **≈ 40° – 42°** | θc(1,50) = 41,8°, arredonda para 42, não 41 |
| 1,56 – 1,65 | ≈ 37° – 39° | **≈ 37° – 40°** | θc(1,56) = 39,9°, arredonda para 40, não 39 |
| 1,66 – 1,75 | ≈ 35° – 37° | ≈ 35° – 37° | ✅ correto |
| 1,76 – 1,81 | ≈ 33° – 35° | ≈ 33,5° – 34,6° | ✅ aceitável |
| ≥ 2,40 | ≈ 24° | ≈ 24,4° | ✅ correto |

O erro é pequeno em graus, mas a aula declara (LC-05, exceção deste curso) que os números tabelados **são o objeto de estudo** e vão com valor de referência e fonte — o que eleva o padrão exigido desta coluna especificamente.

**Correção proposta:** substituir pelos valores da coluna "Correto" acima. A coluna é derivada por cálculo, não por fonte externa; declarar como tal.
**Fonte:** cálculo direto de θc = arcsin(1/n), verificado em 2026-09-04 · convenção da fórmula: [USFG, *Refractive Index and Critical Angle*](https://usfacetersguild.org/refractive-index-and-critical-angle/)
**Nível:** cálculo direto · **Confiança:** confirmado

> **Desfecho — CORRIGIDO em 2026-09-04.** Coluna substituída pelos valores recalculados, e a coluna inteira passou a ser **declarada como derivada por cálculo**, não copiada de fonte externa, num parágrafo antes da tabela. Alegação nova `TAB-ALVO-FAIXA-003` instalada no rodapé, com os valores para todos os extremos de faixa.

---

### 🟠 9. "Pavilhão mais raso não gera ganho de peso" contradiz a prática que a própria aula descreve

**claim_id:** `FAC-REN-PROF-001`
**Tipo:** omissão que gera erro + inconsistência interna
**Onde:** aula 04 · "Onde o compromisso é decidido: três lugares do projeto", bloco *Profundidade de pavilhão*

**Está escrito:** "Um pavilhão levemente mais raso que o ângulo-alvo aproxima o janelamento … **em troca de nenhum ganho de peso** — é praticamente sempre uma escolha pior que as outras duas."

**Problema:** a afirmação só vale com o **contorno da cinta fixo**. Com bruto tabular ou achatado — que é o caso comum — o pavilhão raso é justamente o que permite um **diâmetro maior** a partir do mesmo material, e o ganho de peso é real e é a razão pela qual a prática existe. A literatura descreve o corte nativo exatamente assim: "o erro mais comum é cortar uma gema com face grande e pavilhão raso, resultando em janelamento", feito "numa tentativa exagerada de maximizar o peso em quilates". Ou seja, o pavilhão raso é **a** manobra clássica de rendimento — não uma escolha sem ganho.

A própria aula 04 se contradiz duas vezes: sua definição de corte nativo ("talhe feito para reter o máximo de peso, aceitando perda óptica") descreve essa manobra, e sua Rota B do exemplo trabalhado usa ângulo mais raso nas pontas do oval **exatamente para ganhar rendimento**.

**Correção proposta:** "Um pavilhão mais raso que o ângulo-alvo aproxima o janelamento (mesmo mecanismo da aula 01). Com o contorno da cinta fixo ele também não retém peso — mas o bruto tabular ou achatado raramente deixa o contorno fixo: aí o pavilhão raso permite um diâmetro maior a partir do mesmo material, e é essa a manobra de rendimento mais comum do ofício — e a origem mais frequente de pedras janeladas."
**Fonte:** [AJS Gems, *Precision Cut vs. Native Cut Gemstones*](https://www.ajsgem.com/articles/precision-cut-vs.-native-cut-gemstones.html) · [GemSelect, *Native Cut Gemstones*](https://www.gemselect.com/other-info/native-cut-gems.php) — consultadas em 2026-09-04
**Nível:** base de referência do ofício · **Confiança:** confirmado
**Também aparece em:** aula 04 "Recap relâmpago", 2º marcador; aula 04 `FAC-REN-ASSIM-001` ("projeto excessivamente conservador … apenas reduz o peso"), que depende da mesma premissa.

> **Desfecho — CORRIGIDO em 2026-09-04.** O bloco de profundidade de pavilhão foi dividido em dois parágrafos e a afirmação passou a ser condicionada: **com o contorno da cinta fixo** o pavilhão raso não retém peso, mas bruto tabular ou achatado raramente deixa o contorno fixo, e aí o raso permite **diâmetro maior** — a manobra de rendimento mais comum do ofício e a origem mais frequente de pedras janeladas. "Erros comuns" ganhou marcador dedicado. `FAC-REN-ASSIM-001`, que dependia da premissa derrubada, teve os exemplos dos dois lados da assimetria trocados (ver propagação, ao final). Fontes AJS Gems e GemSelect acrescentadas.

---

### 🟠 10. "Brilho" é definido com o sentido que a fonte citada dá a "brightness", não a "brilliance"

**claim_id:** `BRI-MEC-BRILHO-001`
**Tipo:** nomenclatura / confusão de escopo
**Onde:** aula 03 · "Vocabulário desta aula"; "Brilho: retorno bruto de luz branca"

**Está escrito:** "**brilho** (*brilliance*) | a quantidade de luz branca que a pedra devolve ao olho do observador, sob luz parada." Fonte declarada: "United States Faceters Guild — dicionário de facetamento: definições correntes de *brilliance*, *fire* e *scintillation*".

**Problema:** o dicionário da USFG — a fonte que a aula cita — define o contrário: **"Brilliance: a general term used to describe a stone's overall appearance. It always includes Brightness, and often includes Color Spread or Scintillation."** Isto é, para a USFG *brilliance* é o **termo guarda-chuva que contém os três efeitos**, e o nome do retorno de luz branca é **Brightness**. A aula usa a palavra de uma autoridade com o significado de outra — e faz isso na aula cujo propósito declarado é justamente separar os três termos por mecanismo. O aluno que consultar o dicionário citado encontrará a definição oposta.

(O mesmo dicionário define *Fire/Dispersion* de forma compatível com a aula, e observa que "Color Spread" é o termo preferível para desempenho de pedra pronta.)

**Correção proposta:** manter "brilho" como o termo em português (é o uso corrente), mas trocar o parêntese inglês de *brilliance* para ***brightness*** e acrescentar uma linha: "Cuidado com o inglês: no dicionário da USFG, *brilliance* é o termo guarda-chuva para a aparência geral da pedra — inclui *brightness* e frequentemente também *color spread* e *scintillation*. O efeito isolado que esta seção descreve é o *brightness*." Isso reforça o objetivo da aula em vez de enfraquecê-lo.
**Fonte:** [USFG Faceting Dictionary](https://usfacetersguild.org/usfg-faceting-dictionary/) — consultado em 2026-09-04
**Nível:** normativa para a nomenclatura do ofício · **Confiança:** confirmado
**Também aparece em:** aula 03 "Recap relâmpago", 1º marcador; aula 01, verbete "retorno de luz" (compatível, não precisa mudar).

> **Desfecho — CORRIGIDO em 2026-09-04.** O parêntese inglês do verbete passou de *brilliance* para ***brightness***, e a advertência sobre o uso da USFG entrou na própria entrada de vocabulário, onde o aluno a encontra antes de ler a seção. O marcador do Recap foi alinhado. A linha de fontes foi detalhada com a definição literal do dicionário, e o **GIA** foi acrescentado como fonte da definição de cintilação **por movimento** — a adotada pela aula —, atendendo de passagem a ressalva que a própria auditoria levantou sobre `BRI-MEC-CINT-001`.

---

### 🟠 11. "Corte nativo" é definido só pela intenção de projeto; o termo designa primariamente origem e método

**claim_id:** `FAC-REN-CONTORNO-001`
**Tipo:** omissão que gera erro
**Onde:** aula 04 · "Vocabulário desta aula"; "Contorno"; "Recap relâmpago"

**Está escrito:** "**corte nativo** (*native cut*) | talhe feito para reter o máximo de peso, aceitando perda óptica" e "a literatura do ofício distingue o **corte de precisão** … do **corte nativo** (contorno e proporção fixados pelo bruto)".

**Problema:** *native cut* designa, em primeiro lugar, a pedra **facetada no país de origem, à mão e a olho, por métodos tradicionais** — o critério é geográfico e de método, não de filosofia de projeto. A retenção de peso é a **consequência típica** e a conotação, não a definição. A distinção real que a literatura faz é entre corte à mão/a olho no país de origem e corte com facetadora indexada por lapidários de precisão nos EUA e na Europa. Além disso, "muitos cortes nativos são desenhados para maximizar a **cor**" — motivação que a aula não menciona e que é exatamente o assunto da aula 05 seguinte, uma ponte perdida.

Como está, o aluno conclui que "corte nativo" é um par simétrico e neutro de "corte de precisão" no eixo peso × óptica, o que não é o que o termo significa no comércio.

**Correção proposta:** "**corte nativo** (*native cut*) | talhe executado no país de origem da gema, à mão e a olho, por métodos tradicionais — em oposição ao corte com facetadora indexada e desenho publicado. A retenção de peso do bruto é a consequência típica dessa prática, e o motivo pelo qual o termo aparece neste compromisso; parte dos cortes nativos, porém, é orientada para maximizar **cor**, não peso — o compromisso da aula 05."
**Fonte:** [AJS Gems, *Precision Cut vs. Native Cut Gemstones*](https://www.ajsgem.com/articles/precision-cut-vs.-native-cut-gemstones.html) · [GemSelect, *Native Cut Gemstones*](https://www.gemselect.com/other-info/native-cut-gems.php) · [GIA, *Gem Cutting Styles — Definitions*](https://www.gia.edu/gia-news-research-value-factors-gem-cutting-styles-definitions) — consultadas em 2026-09-04
**Nível:** base de referência do ofício + GIA · **Confiança:** confirmado
**Ver também:** ⚪ 16, sobre o termo ser contestado.

> **Desfecho — CORRIGIDO em 2026-09-04.** O verbete de vocabulário foi reescrito com a definição por **origem e método**, deixando a retenção de peso como consequência típica. No corpo, a oposição corte de precisão × corte nativo ganhou parágrafo próprio, com a ressalva explícita de que **não é o par simétrico "óptica × peso" que parece** e com a ponte perdida para a aula 05 (parte dos cortes nativos é orientada para maximizar **cor**). O marcador de "Erros comuns" e o do Recap foram alinhados. Fontes AJS Gems, GemSelect e GIA acrescentadas.

---

### 🟠 12. O exemplo trabalhado da aula 06 usa um ângulo fora da faixa que a aula 02 prescreve para o mesmo índice

**claim_id:** `RAY-EX-SAFIRA-001` *(novo)*
**Tipo:** inconsistência interna
**Onde:** aula 06 · "Exemplo trabalhado"

**Está escrito:** "um pavilhão de **40,5°** num material hipotético de índice de refração **1,76**" — e o exemplo trata essa geometria como bem resolvida, com métrica de brilho alta.

**Problema:** a tabela da aula 02 prescreve **38°–40°** para a faixa 1,76–1,81. Os 40,5° do exemplo caem **fora** dessa faixa, e a aula 06 não sinaliza a discrepância — ao contrário, apresenta a geometria como correta. Um aluno atento conclui que uma das duas aulas está errada.

Resolve-se sozinho quando o 🔴 1 for corrigido (o valor publicado para coríndon é 42°, e 40,5° passa a ser uma escolha um pouco rasa, plausível e explicável) — **mas só se a correção do 🔴 1 for propagada até aqui**. Fica registrado para que a propagação não seja esquecida.

**Correção proposta:** após corrigir a tabela da aula 02, ajustar o exemplo para 42° (o valor de referência do coríndon), ou manter 40,5° e acrescentar meia frase dizendo que é deliberadamente um pouco mais raso que o valor de referência — o que aliás reforça a lição de cor da própria aula.
**Fonte:** consistência interna do módulo + [IGS, *Faceting Made Easy, Part 1*](https://www.gemsociety.org/article/faceting-made-easy-part-1-gemstone-properties/)
**Nível:** consistência interna · **Confiança:** confirmado

> **Desfecho — CORRIGIDO em 2026-09-04, por propagação.** Escolhida a **segunda** das duas opções: os 40,5° foram mantidos e o exemplo ganhou uma **observação de partida** declarando que são deliberadamente um pouco mais rasos que os 42° publicados para o coríndon, escolha coerente com a regra da aula 05 para material de cor cheia. Como o achado previa, a discrepância se dissolveu ao corrigir o 🔴 1 — e explicá-la reforça a lição de cor da própria aula, em vez de apenas silenciar o conflito. Nenhum `claim_id` novo foi instalado: `RAY-EX-SAFIRA-001` é rótulo de achado, não alegação auditável.

---

## Achados 🔵 — sem fonte

### 🔵 13. Três aulas atribuem ao dicionário da USFG verbetes que ele não tem

**claim_id:** `RAY-FONTE-USFG-001` *(novo)*
**Tipo:** evidência insuficiente / atribuição não verificável
**Onde:** aula 03 "Fontes consultadas"; aula 04 "Fontes consultadas"; aula 06 "Fontes consultadas" e rodapé de `RAY-FERR-GEMCAD-001`

**Problema:** o USFG Faceting Dictionary **contém** verbetes para *Brilliance*, *Fire/Dispersion*, *Scintillation*, *Culet* e *Meetpoint* — as citações das aulas 03 e 04 a esses termos são legítimas (com a ressalva do 🟠 10). Ele **não contém** verbetes para **GemCad**, **GemRay**, **extinction**, **window/windowing** nem **native cut**. Portanto:

- aula 06, "United States Faceters Guild — dicionário de facetamento: referências a ferramentas de ray tracing associadas ao desenho de diagramas (GemRay)" → **a fonte não sustenta a alegação**;
- aula 01 e aula 04 apoiam-se em "janelamento" e "extinção" como vocabulário do ofício sem que o dicionário citado os defina (o vocabulário existe na literatura, mas não nessa fonte).

Não é acusação de erro de conteúdo — as ferramentas e os defeitos existem, e o 🟠 7 já traz a fonte correta para o GemRay. É a rastreabilidade que está quebrada: quem for conferir não encontra.

**Correção proposta:** na aula 06, substituir a linha da USFG por "Robert W. Strickland — *GemCad for Windows* e *GemRay for Windows*, gemcad.com (documentação do autor)". Nas aulas 01 e 04, citar para janelamento/extinção uma fonte que de fato os defina, em vez do dicionário.
**Fonte:** [USFG Faceting Dictionary](https://usfacetersguild.org/usfg-faceting-dictionary/) — verificado verbete a verbete em 2026-09-04
**Nível:** normativa (ausência verificada) · **Confiança:** confirmado (a ausência), não verificado (a alegação original)

> **Desfecho — REATRIBUÍDO em 2026-09-04. Decisão de julgamento.**
>
> **A decisão:** reatribuir a fonte, **não** remover a alegação. O precedente disponível é o 🔵 do módulo 07 (`ESF-TOL-FAIXA-001`), que foi **removido** — mas ali nenhuma fonte lapidária sustentava o conteúdo. Aqui o caso é o oposto: o conteúdo está correto e **existe fonte própria para ele**; o que estava quebrado era só a rota de verificação. Remover seria destruir conteúdo válido para consertar uma nota de rodapé.
>
> **O que foi aplicado, aula a aula.** *Aula 06:* a linha do dicionário da USFG foi substituída por Robert W. Strickland — *GemCad for Windows* e *GemRay for Windows*, gemcad.com, mais o manual de 2012 —, documentação do autor, normativa para as capacidades da ferramenta; acrescentada nota explícita de que o dicionário **não contém** verbetes para GemCad nem GemRay. *Aula 01:* a fonte genérica "material técnico" virou a página específica *Refractive Index and Critical Angle*, que é a que de fato publica o caso do quartzo, mais uma linha para a literatura de talhe sobre o *nailhead*, e nota de que o dicionário não define *window/windowing* nem *extinction* — o vocabulário vem da aula 06 do módulo 05. *Aula 04:* mantida a citação do dicionário, que **é** legítima para *Culet* e *Meetpoint* (`FAC-REN-CULACA-001` é quase literal ao verbete *Culet*), com nota de que *native cut* não está no dicionário e vem da literatura comercial agora citada. *Aula 03:* citação do dicionário mantida e detalhada, legítima para *Brilliance*, *Fire* e *Scintillation*.
>
> Nenhum `claim_id` novo instalado: `RAY-FONTE-USFG-001` é rótulo de achado sobre rastreabilidade, não alegação auditável.

---

### 🔵 14. A "margem de ~2,5° acima do crítico" da aula 01 não tem fonte, e fica abaixo do que a USFG recomenda

**claim_id:** `ANG-EX-QUARTZO-001`
**Tipo:** evidência insuficiente
**Onde:** aula 01 · "Exemplo trabalhado", Passo 4; "O que não concluir", 3º marcador

**Está escrito:** "A margem de ~2,5° acima do crítico — não o valor mínimo exato — existe porque nem todo raio entra perfeitamente vertical."

**Problema:** o **restante do exemplo é impecável e está confirmado** — a USFG usa exatamente este caso (quartzo, θc = 40,49°, pavilhão a 35° janela, pavilhão a 43° devolve luz), e o 43° é o valor de pavilhão *mains* que a própria USFG publica para IR 1,54. O que não se confirma é a **margem de 2,5°** como número apresentado. A USFG diz que "muitas autoridades aconselham manter os *pavilion mains* **vários graus** acima do ângulo crítico" e que "muitas autoridades consideram 41° baixo demais para quartzo" — 41° é margem de 0,5°, e 2,5° está na borda inferior do que essas autoridades chamariam suficiente. O número é uma leitura aritmética do exemplo (43 − 40,5), apresentada com peso de regra.

A aula já se protege parcialmente ("Não tomar a margem de ~2,5° do exemplo como regra fixa"), o que rebaixa a severidade — mas o número segue no Passo 4 sem fonte.

**Correção proposta:** trocar "A margem de ~2,5°" por "A margem — aqui, 2,5°, e na literatura descrita apenas como 'vários graus' acima do crítico — existe porque…". Não inventar um valor; usar a formulação qualitativa da fonte.
**Fonte:** [USFG, *Refractive Index and Critical Angle*](https://usfacetersguild.org/refractive-index-and-critical-angle/) · [USFG, *Choosing the Best Angles for Your SRB*](https://usfacetersguild.org/choosing-the-best-angles-for-your-srb/) — consultadas em 2026-09-04
**Nível:** base de referência · **Confiança:** provável (direção), não verificado (o valor 2,5°)

> **Desfecho — REQUALIFICADO em 2026-09-04. Decisão de julgamento.**
>
> **A decisão:** manter o número, requalificando o que ele é — não removê-lo nem trocá-lo por outro. O precedente do módulo 07 é não inventar valor novo e usar a formulação qualitativa da fonte, e é o que foi feito; mas remover o 2,5° deixaria o Passo 4 sem fechar a conta que os Passos 1 a 3 abriram, e o restante do exemplo está **confirmado** contra a USFG (quartzo, θc = 40,49°, pavilhão a 35° janela, a 43° devolve luz — e 43° é o valor que a própria USFG publica para IR 1,54).
>
> **O que foi aplicado:** o Passo 4 passou a dizer "a margem — aqui 2,5°, que é a leitura aritmética deste exemplo (43 − 40,5), e que a literatura do ofício descreve apenas como 'vários graus' acima do crítico, sem fixar um número —". O rodapé de `ANG-EX-QUARTZO-001` registra a mesma distinção e cita as duas páginas da USFG. A proteção que a aula já tinha em "O que não concluir" foi mantida.

---

## Achados ⚪ — controverso

### ⚪ 15. "Mais facetas revelam mais fogo" é apresentado como consenso; a relação é disputada e não é monotônica

**claim_id:** `BRI-PROJ-COMPR-001` (e `BRI-MEC-DISP-001`)
**Tipo:** certeza indevida
**Onde:** aula 03 · "Dispersão"; "Os três juntos"; "Recap relâmpago"

**Está escrito:** "Um material de dispersão alta se beneficia, portanto, de desenhos com **mais facetas, menores e mais numerosas** na coroa e no pavilhão."

**Problema:** a direção geral é defensável e é o senso comum do ofício, mas a relação **não é monotônica** e o ponto é objeto de disputa real na literatura de talhe: abaixo de um certo tamanho angular, cada flash colorido fica pequeno demais para o olho resolver como cor, e o aumento do número de facetas passa a **reduzir** o fogo percebido em vez de aumentá-lo. A aula apresenta como regra sem limite ("mais facetas ajudam a dispersão e a cintilação") o que é uma relação com ótimo interno.

O contrato de nível deste curso torna isso obrigatório: **LC-08 — controvérsia em uma frase, declarada como pergunta aberta, sem arbitrar o debate**. A aula 03 não tem nenhuma declaração de controvérsia.

**Correção proposta:** acrescentar uma frase em "Os três juntos": "Até onde essa troca compensa é questão aberta: abaixo de um certo tamanho de faceta, cada flash colorido fica pequeno demais para o olho resolver como cor, e há divergência na literatura sobre onde exatamente fica esse limite." Não arbitrar.
**Nível:** divergência real entre fontes do ofício · **Confiança:** em disputa

> **Desfecho — DECLARADO COMO CONTROVÉRSIA em 2026-09-04. Decisão de julgamento.**
>
> **A decisão:** instalar, sem arbitrar. É a primeira declaração LC-08 do módulo, que entrou com zero nas seis aulas.
>
> **O que foi aplicado:** parágrafo em "Os três juntos", em **prosa**, com abertura "**Pergunta em aberto:**" — a convenção do curso fixada na revisão didática do módulo 07 (o curso não usa *callout* para controvérsia declarada; *callout* fica reservado a pedido de ilustração). A formulação separa o que é aceito do que está em disputa: afirma que o ponto de retorno decrescente **existe** — abaixo de certo tamanho de faceta o flash colorido fica pequeno demais para o olho resolver como cor — e declara em disputa **onde** ele fica. O marcador de "Erros comuns" foi realinhado de "mais facetas sempre melhora tudo" para a formulação com limite, e um marcador de Recap foi acrescentado.

---

### ⚪ 16. "Corte nativo" é um termo contestado no comércio, e a aula o usa como categoria neutra

**claim_id:** `FAC-REN-NATIVO-001` *(novo)*
**Tipo:** controvérsia / certeza indevida
**Onde:** aula 04 · "Vocabulário"; "Contorno"; "Erros comuns", 3º marcador

**Problema:** a aula trata "corte nativo" como uma categoria técnica neutra e simétrica a "corte de precisão" — e chega a dizer, corretamente na intenção, que "confundir corte nativo com corte malfeito" é erro comum. Mas o próprio termo é **contestado**: parte do comércio o usa de fato como sinônimo pejorativo de "conjunto de defeitos de talhe resultantes de tentativa exagerada de maximizar peso", e parte o rejeita como designação de origem carregada, preferindo "corte de origem". A aula não registra que a disputa existe.

Isto é o mesmo achado do 🟠 11 visto pelo outro lado: lá o problema é a definição incompleta, aqui é a ausência da controvérsia que LC-08 exige.

**Correção proposta:** uma frase, sem arbitrar: "O próprio termo é disputado — parte do comércio o emprega como sinônimo de talhe deficiente, parte o rejeita como designação de origem e prefere 'corte de origem'; este curso o usa no sentido descritivo de método e origem."
**Fonte:** [AJS Gems](https://www.ajsgem.com/articles/precision-cut-vs.-native-cut-gemstones.html) ("o termo é frequentemente usado para se referir a uma série de males de talhe") · [AfricaGems, *What is a Native Cut Gemstone?*](https://www.africagems.com/blog/what-is-a-native-cut-gemstone-a-collectors-guide-to-tradition-vs-precision/) — consultadas em 2026-09-04
**Nível:** uso comercial divergente · **Confiança:** em disputa

> **Desfecho — DECLARADO COMO CONTROVÉRSIA em 2026-09-04. Decisão de julgamento.**
>
> **A decisão:** instalar como **segunda** declaração LC-08 do módulo. Os módulos 06 e 07 registraram que "uma basta", mas o critério real daquelas decisões era a **genuinidade**, não a contagem — a segunda candidata do módulo 07 foi descartada por ser decisão de eficiência de oficina, não divergência sobre um fato. Esta passa no critério: é divergência documentada entre usos comerciais reais, está no coração de `oa04`, e entra **dentro** da reescrita que o 🟠 11 já exigia, a custo de três linhas.
>
> **O que foi aplicado:** parágrafo em prosa, com abertura "**Ponto em aberto:**", registrando os dois lados (parte do comércio usa o termo como sinônimo de talhe deficiente; parte o rejeita como designação de origem e prefere "corte de origem") e declarando que este curso o usa no sentido descritivo de método e origem, sem tomar partido. Alegação nova `FAC-REN-NATIVO-001` instalada no rodapé, com `risk: controversia`. Fontes AJS Gems e AfricaGems acrescentadas.

---

## Verificado e correto

Alegações checadas contra fonte e **aprovadas sem alteração** — inclusive as três que o redator sinalizou como de maior risco e que se confirmaram corretas:

| claim_id | O que foi verificado | Fonte · confiança |
|---|---|---|
| `ANG-CRIT-FORM-001` | θc = arcsin(1/n); quanto maior n, menor θc; propriedade do material | USFG, *Refractive Index and Critical Angle* · confirmado |
| `ANG-NORM-INCID-001` | todo ângulo óptico medido a partir da normal | óptica geométrica / lei de Snell · confirmado |
| `ANG-RIT-PAV-001` | acima do crítico → RIT; abaixo → escape pelo fundo = janelamento | USFG · confirmado |
| `ANG-EX-QUARTZO-001` (o cálculo) | quartzo θc = **40,49°**; 35° janela; 43° restabelece a RIT | **caso idêntico ao publicado pela USFG** · confirmado |
| `ANG-LEQUE-MARG-001` | a mesa e a coroa refratam a luz num leque, não num raio único; a condição precisa valer para o leque | confirmado — e mais forte do que a aula diz: a refração na mesa confina os raios internos a um cone de meio-ângulo **exatamente igual ao ângulo crítico** |
| `TAB-LIMITE-RAY-001` | a tabela assume desenho de referência; contorno e proporção deslocam o ideal; refino exige ray tracing | USFG ("no magic bullet or universal set of angles") · confirmado |
| `TAB-DIAM-EXCE-001` (os valores) | diamante n ≈ 2,417, θc ≈ 24,4°; Tolkowsky pavilhão **40,75°**, coroa 34,5°, mesa ~53% | Tolkowsky 1919 via OctoNus · confirmado (só a *causa* está invertida — 🟠 6) |
| `BRI-MEC-DISP-001` | dispersão = refração diferencial por comprimento de onda; medida pela diferença de IR entre vermelho e violeta; acumula na entrada e na saída, não na RIT | USFG dictionary; gemologia padrão · confirmado |
| `BRI-EX-ZIRCAO-001` | zircão como material de dispersão moderadamente alta (0,039, contra 0,044 do diamante) | dados de dispersão padrão · confirmado |
| `FAC-REN-CULACA-001` | culaça = "pequena faceta paralela ao plano da cinta feita para evitar lascar a ponta da culaça" | **USFG dictionary, verbete *Culet*, definição 1 — quase literal** · confirmado |
| `FAC-REN-ELIPSE-001` | maior círculo inscrito numa elipse tem área b/a da elipse; 1/1,3 = **0,769** | geometria elementar, recalculado · confirmado (ver nota menor abaixo) |
| `FAC-REN-VALOR-001` | o equilíbrio depende de valor por quilate, raridade e mercado; sem resposta geral | AJS Gems; USFG · confirmado |
| **`COR-CAMINHO-OPT-001`** | **caminho óptico maior → mais absorção → cor mais saturada; a profundidade de pavilhão é a variável que mais controla esse caminho** | **confirmado** |
| **`COR-PROF-ESCURO-001`** | **material de cor cheia → pavilhão mais RASO** | **USFG, *Choosing the Best Angles for Your SRB*: "If you have dark rough… keeping the stone shallow so it is not too dark. Use lower crown and/or pavilion angles"** · confirmado |
| **`COR-PROF-CLARO-001`** | **material de cor fraca → pavilhão mais FUNDO** | **USFG, mesma fonte: "if you're cutting clear or pale colored material… Employ higher crown and pavilion angles"** · confirmado |
| `COR-ZONA-ORDEM-001` | zonação: a profundidade alonga o caminho por todas as zonas; orientação precede profundidade | coerente com a fonte da regra de profundidade; sem contra-evidência · provável |
| `RAY-MODEL-MEDE-001` | ray tracing traça raios individuais aplicando reflexão e refração faceta a faceta, e agrega em métricas | documentação do GemRay · confirmado |

---

## Observações menores (não são achados factuais)

- **Aula 01** — "nenhuma superfície real reflete **100,000%**" é erro de digitação (100%). Sai junto na correção do 🟠 5.
- **Aula 04** — "cada **grama** perdida pesa mais na conta final", duas linhas depois de "valor comercial **por quilate**". Gema se pesa em quilates; trocar por "cada quilate perdido".
- **Aula 04** — "descarta … algo da ordem de **20%**": o valor exato é 1 − 0,769 = **23,1%**. "Da ordem de 20%" é defensável, mas "cerca de 23%" é gratuito e mais preciso, e é o que o próprio `FAC-REN-ELIPSE-001` calcula.
- **Formato de `claim_id`** — as **35 alegações do módulo casam com `^[A-Z]{2,4}-[A-Z0-9]+-[A-Z0-9]+-[0-9]{3}$`**, todas com 4 segmentos. Nenhuma tem 5. Os prefixos `ANG-`, `TAB-`, `BRI-`, `COR-`, `RAY-` e `FAC-REN-` **não colidem** com nenhum primeiro segmento em uso nos módulos 01–07; em particular `FAC-REN-` está bem separado dos `REN-` do módulo 05 (`REN-FORMULA-PESO-001`, `REN-FAIXA-TIP-001`, `REN-RECUT-PERDA-001`, `REN-ESTIM-PROC-001`). Os 6 identificadores criados por esta auditoria também foram verificados como livres.
- **Divergência do exemplar** — `_contexto.md` e `_curso.md` dão `FAC-ANG-CRIT-001` como exemplo canônico de `claim_id` para exatamente este assunto; o redator usou o prefixo `ANG-`. Não é colisão nem erro factual, e o formato está correto — fica registrado só para decisão consciente. Assunto do `validador-estrutural-do-curso`, não desta auditoria.
- **Fora de escopo desta skill, para o `revisor-didatico`:** a aula 02 é a que mais sofre com as correções acima — três dos quatro 🔴 estão nela e o conserto do 🔴 3 muda a linha argumentativa da seção "base física". Vale reavaliar a coerência didática da aula 02 inteira depois da correção, não só os trechos tocados.

---

## Propagação para alegações que a auditoria havia aprovado

Três das 23 alegações verificadas e aprovadas foram tocadas pela correção — não porque estivessem erradas, mas porque dependiam de algo que mudou. Registrado aqui para a revisão didática.

- **`TAB-EX-MARGEM-001`** (aula 02) — a aritmética estava certa, mas partia dos valores-alvo incorretos da tabela antiga (42,5° e 39°, margens de 2,0° e 4,6°). Refeita sobre os valores publicados, virou **quartzo 42° contra coríndon 42°** — alvos **idênticos** com críticos separados por 6,1°, margens de 1,5° e 7,6° (3,7% contra 22,1%). A conclusão não mudou: ficou mais forte, e o exemplo agora **confirma** a seção de base física em vez de refutá-la.
- **`RAY-LIMITE-PERCEP-001`** (aula 06) — apoiava-se no caráter **estático** da métrica ("fotografia congelada"), argumento que a própria auditoria enfraqueceu ao documentar que o GemRay gera animações de basculamento. A lacuna foi **realocada** para a agregação estética: a métrica reduz a um número uma ordenação de gosto entre brilho, fogo e cintilação, e essa não é redutível a número. A lacuna sobrevive, com fundamento que se sustenta.
- **`FAC-REN-ASSIM-001`** (aula 04) — dependia da premissa derrubada pelo 🟠 9: listava "pavilhão mais raso" como erro **conservador**, quando o pavilhão raso é justamente a manobra **agressiva** de rendimento. Os exemplos dos dois lados da assimetria foram trocados (conservador: redondo num bruto que não pedia; agressivo: pavilhão empurrado para o raso em busca de diâmetro, ou *meetpoint* sem culaça). A assimetria em si — excesso de rendimento carrega penalidade potencial maior — permanece válida.

Além dessas, **`COR-ZONA-ORDEM-001`** (aula 05) saiu reforçada: a ordem "orientação antes de profundidade" ganhou o argumento correto para o limite do modelo de cor (cor uniforme atribuída, não ausência de cor).

---

## Verificação estrutural pós-correção

- **`claim_id`** — 38 alegações ao final (35 herdadas + 3 criadas: `TAB-ALVO-FAIXA-002`, `TAB-ALVO-FAIXA-003`, `FAC-REN-NATIVO-001`). **Todas** casam com `^[A-Z]{2,4}-[A-Z0-9]+-[A-Z0-9]+-[0-9]{3}$`, todas com **4 segmentos**, verificadas por regex sobre os seis arquivos depois das correções. Nenhuma duplicata dentro do módulo e **nenhuma colisão** com os `claim_id` dos módulos 01–07. Nenhum resíduo de 5 segmentos — o escorregão dos módulos 04 e 05 não voltou.
- **Rótulos de achado que não viraram alegação** — `RAY-EX-SAFIRA-001` e `RAY-FONTE-USFG-001` foram criados por esta auditoria como identificadores de **achado**, não de alegação auditável: o primeiro era inconsistência interna resolvida dentro do exemplo trabalhado, o segundo era rastreabilidade de fonte. Nenhum dos dois existe no rodapé de aula alguma, por decisão consciente.
- **Régua de `palavras_corpo`** — a mesma de `_contexto.md`: de `## Conteúdo` ao fim de `## Recap relâmpago`, inclusive, por `len(texto.split())`. A contagem reproduziu **exatamente** os seis valores declarados antes da correção (1589/1566/1597/1615/1612/1624), o que revalida a régua. Rodapés ressincronizados nas seis aulas.
- **Regra dura de bancada** — nenhum texto acrescentado por esta correção descreve operação de máquina ou destreza manual. O material instalado é geometria, mecanismo óptico, valor publicado com fonte, nomenclatura e declaração de controvérsia.

---

## Método

- **Modo `audit-and-fix`** — auditoria em `audit` (2026-09-04) e correção aplicada no mesmo dia. Os trechos literais citados em cada achado são os da versão **anterior** à correção; a linha **Desfecho** de cada um diz o que ficou no arquivo.
- As 6 aulas foram lidas em conjunto, o que é o que permitiu pegar os achados 🟠 12 (aula 06 × aula 02), 🔴 4 (aula 06 → aula 05) e 🟠 9 (aula 04 contra si mesma).
- Nenhuma verificação foi feita de memória: cada valor numérico, ângulo, faixa de índice, nome de ferramenta e atribuição de fonte foi checado contra fonte consultada em 2026-09-04, listada em cada achado.
- Ângulos críticos recalculados por θc = arcsin(1/n) para todos os extremos de faixa da tabela da aula 02.
- Os `claim_id` foram conferidos por regex contra `^[A-Z]{2,4}-[A-Z0-9]+-[A-Z0-9]+-[0-9]{3}$` e cruzados com todos os `claim_id` dos módulos 01–07.

## Próximo passo

1. ~~**Correção** dos 4 🔴 e 8 🟠~~ — **concluída em 2026-09-04**, junto com os 2 🔵 e os 2 ⚪, cada um destes com decisão registrada acima e no manifesto.
2. **Revisão didática** — é a próxima etapa, e o encargo está detalhado abaixo. Atenção prioritária à **aula 02**, cuja linha argumentativa mudou.
3. **Questionário** — depois da revisão didática, não antes. O gate da auditoria está liberado, mas o pipeline dos módulos 06+ põe a revisão didática entre a correção e a avaliação.

Sem flashcards: dispensados neste curso a partir do módulo 06 (decisão de 2026-09-04).

### Encargo para o `revisor-didatico`

1. **A aula 02 é a prioridade.** Três dos quatro 🔴 estavam nela, e a correção do 🔴 3 mudou a **linha argumentativa inteira** da seção de base física — que agora sustenta um piso que desce contra um teto que não desce, com o exemplo trabalhado confirmando a tese em vez de contradizê-la. Reavaliar a coerência da aula inteira, não só os trechos tocados: ela perdeu 23 palavras líquidas, mas trocou boa parte do corpo.
2. **Possível desalinhamento entre título e conteúdo na aula 02.** O título da aula e o objetivo `lapidacao-m08-oa02` falam em "tabela de ângulos-alvo **por faixa de índice de refração**", enquanto a lição central passou a ser que os valores são publicados **por material** e que a faixa apenas organiza a leitura. A entrada de vocabulário foi ajustada para dizer isso, mas título e objetivo não foram tocados — objetivo de aprendizagem não se altera por auditoria. Julgar se há desalinhamento didático.
3. **Duas declarações LC-08, e não uma.** O módulo entrou com zero e sai com duas (a03 e a04), ambas em prosa, na convenção do módulo 07. Julgar se duas é o número certo para um módulo de seis aulas — a justificativa está no bloco de decisões acima.
4. **As seis aulas foram enxugadas para financiar as correções.** Conferir corte a corte se algum removeu **conteúdo** em vez de repetição, com atenção à a06 (≈283 palavras cortadas) e à a04 (perdeu ~60 líquidas depois de ganhar três blocos novos).
5. **Conferir títulos de seção contra o corpo reescrito.** É a terceira vez que este curso pega título desatualizado por auditoria — módulos 04, 06 e 07, sempre na a02. Nesta correção o título da seção de base física da a02 **já foi trocado** por esse motivo; o título "A tabela — valores de referência por faixa" merece segunda olhada, pela mesma razão do item 2.
