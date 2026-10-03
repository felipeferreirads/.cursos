# Auditoria científica — Módulo 08: Geotecnia ambiental

**Módulo:** [[08-geotecnia-ambiental-modulo|Módulo 08 — Geotecnia ambiental]]
**Escopo:** 6 aulas (geologia-avancado-m08-a01 a a06), 43 alegações auditáveis extraídas dos blocos de metadados de cada aula (7+7+7+7+8+7). Uma alegação nova (`GEOAMB-M08-A02-PIPING-008`) foi criada durante a auditoria para uma afirmação do corpo da Aula 02 que não estava coberta por nenhum `claim_id` — total final: 44.
**Modo:** `audit-and-fix`. Todos os achados 🔴, 🟠 e 🟡 foram corrigidos no texto das aulas, nos recaps, nas listas de fontes e nos blocos de metadados antes da geração do questionário e do baralho.
**Método:** verificação de cada `claim_id` contra a literatura padrão de geotecnia ambiental (Sharma & Reddy, 2004; Daniel, 1993; Rowe, Quigley, Brachman & Booker, 2004; Boscov, 2008; Qian, Koerner & Gray, 2002; Vick, 1990; Blight, 2010; Jefferies & Been, 2016; Mitchell & Soga, 2005; NRC, 1994) e contra o texto das normas, dos diplomas legais e das publicações primárias citadas (ASTM D5084, D6270, D6766; ABNT NBR 10004, 10005, 10006, 10157, 13896, 8419, 15115, 15116; Leis 12.305/2010, 12.334/2010, 12.725/2012, 14.026/2020, 14.066/2020; Decreto 10.936/2022; Resoluções ANM 4/2019 e 95/2022; CONAMA 420/2009; GISTM 2020; Varnes 1978; Wischmeier & Smith 1978; Sherard et al. 1976; Hungr, Leroueil & Picarelli 2014; Giroud & Bonaparte 1989; Sowers 1973; Schroeder et al. 1994; Albright, Benson & Waugh 2010; Morgenstern et al. 2016; Robertson et al. 2019; Robertson 2010; Javandel & Tsang 1986; Grubb 1993; Kjeldsen et al. 2002; Christensen et al. 2001), **com recálculo independente de todos os seis exemplos trabalhados** e verificação cruzada com os Módulos 03, 06 e 07.
**Data:** 2026-08-29

## Resumo do veredito

| Severidade | Contagem |
|---|---|
| 🔴 Erro | 1 (corrigido antes da publicação) |
| 🟠 Impreciso | 5 (corrigidos antes da publicação) |
| 🟡 Desatualizado/a matizar | 8 (corrigidos antes da publicação) |
| 🔵 Controverso (área com debate legítimo) | 1 |
| ⚪ Sem fonte direta verificável (mas plausível/consensual) | 3 |

**Veredito geral: aprovado.** Houve **um achado vermelho** — um erro de formulação física no exemplo trabalhado da Aula 05, que produzia fatores de segurança errados por um fator próximo de 1,9 e contradizia a formulação de talude infinito já estabelecida e auditada no Módulo 07 e reutilizada na Aula 02 deste mesmo módulo. Ele foi **corrigido no texto e no bloco de metadados**, junto com os cinco 🟠 e os oito 🟡. **Nenhum achado vermelho, laranja ou amarelo permanece em aberto**, e o gate de qualidade do plugin está satisfeito. Não há `open_findings`: nenhum achado exigiu decisão do usuário. Três pontos de envelhecimento previsível (legislação de resíduos, legislação de barragens, edição vigente das NBR 15115/15116) ficam registrados como `maintenance_flags`, no mesmo padrão adotado no Módulo 07.

---

## Achados

### 🔴 [GEOAMB-M08-A05-EXEMPLO-008] — Peso submerso usado no esforço motriz de um talude percolado

**Aula:** 05. **Claim relacionado:** exemplo trabalhado de comparação entre `FS` drenado e `FS` pós-liquefação.

**Achado:** o enunciado declara "lençol na superfície" — isto é, um talude **percolado**, com fluxo, na face de jusante de uma barragem —, mas a resolução calculava a tensão cisalhante motriz como `τ = σ'v0·tan β`, ou seja, com o **peso submerso**. Essa é a formulação de um talude **totalmente submerso sob água parada**, condição fisicamente distinta e inaplicável à face de jusante de uma barragem de rejeito. O texto ainda trazia a grafia "talque infinito".

No modelo de talude infinito com percolação paralela — o mesmo que o Módulo 07, Aula 03, estabelece e que a **Aula 02 deste próprio módulo aplica corretamente** — o esforço motriz usa o peso **total** e apenas a tensão normal efetiva usa o peso submerso:

- `τ = γsat·z·sen β·cos β`
- `σ'n = (γsat − γw)·z·cos²β`

Recálculo independente com os dados do enunciado (`γsat = 20 kN/m³`, `z = 15 m`, `β = 12°`, `γw = 9,81 kN/m³`, `φ' = 33°`, `su(liq)/σ'v0 = 0,10`):

| Grandeza | Valor publicado | Valor correto |
|---|---|---|
| `τ` motriz | 32,5 kPa | **61,0 kPa** |
| `σ'v0` | 152,9 kPa | 152,9 kPa (correto) |
| `σ'n` | 146,2 kPa | 146,2 kPa (correto) |
| `τf` drenada | 94,9 kPa | 95,0 kPa (correto) |
| `FS` drenado | 2,9 | **1,56** |
| `FS` pós-liquefação | 0,47 | **0,25** |

O erro está inteiramente no denominador. A razão `τf/su(liq) ≈ 6,2` — o coração pedagógico do exemplo — não muda; mas os dois `FS` publicados eram maiores que os corretos por um fator de 1,88, e a interpretação chamava `FS = 2,9` de "folga confortável". O valor correto, `1,56`, é **rasante ao critério regulamentar de 1,5**, o que torna a lição consideravelmente mais forte: a estrutura **passa** na verificação drenada exigida por norma e ainda assim tem `FS = 0,25` na condição não drenada.

**Correção aplicada:** ✅ exemplo trabalhado reescrito com a formulação correta e com a origem do modelo declarada (Módulo 07, Aula 03); enunciado passou a dizer "lençol na superfície **com fluxo paralelo ao talude**"; typo "talque" corrigido; interpretação reescrita em torno do novo par (1,56 · 0,25) e do fato de a estrutura passar na norma; acrescentado item em "Erros comuns" nomeando explicitamente a confusão entre talude submerso e talude percolado e quantificando o efeito (fator ≈ `γsat/γsub`); `claim` `GEOAMB-M08-A05-EXEMPLO-008` reescrito com todos os valores corretos e com a fonte trocada para a formulação do Módulo 07.
**Confiança:** alta.

---

### 🟠 [GEOAMB-M08-A06-CAPTURA-007] — Largura da zona de captura: assintótica confundida com a largura na linha do poço

**Aula:** 06. **Claim relacionado:** dimensionamento da zona de captura de um poço de bombeamento.

**Achado:** após calcular corretamente `W_∞ = Q/(b·q) = 187,5 m`, o texto registrava "Meia-largura na linha do poço: `W_máx/2 ≈ 94 m` **de cada lado**" — enunciado duplamente incorreto. Pela função de corrente `ψ = U·y − (Q/2π)·θ` (Javandel & Tsang, 1986), a envoltória de captura **afunila** em direção ao poço:

- muito a montante (θ → π): `y = ± Q/(2·b·q) = ± 93,8 m`, total 187,5 m;
- na linha transversal do poço (θ = π/2): `y = ± Q/(4·b·q) = ± 46,9 m`, total **93,8 m** — metade da assintótica.

Os 93,8 m são a **meia-largura assintótica**, não a meia-largura na linha do poço. A consequência não é cosmética: a pluma tem 120 m de largura, e junto ao poço o envelope só tem 93,8 m — **menos que a pluma**. O passo 4 concluía "um poço bem posicionado é geometricamente suficiente" com base apenas no número assintótico, e a ressalva qualitativa que se seguia ("desde que locado de modo que a pluma inteira caia dentro do envelope") não dava ao aluno o número que decide a questão.

**Correção aplicada:** ✅ Passo 2 reescrito distinguindo `W_∞ = Q/(b·q) = 187,5 m (±93,8 m)` de `W_0 = Q/(2·b·q) = 93,8 m (±46,9 m)`, com o afunilamento nomeado; Passo 4 reescrito para explicitar que o envelope só atinge 120 m de largura a cerca de 30 m a montante do poço (verificado: `2y = Qθ/(π·b·q) = 120 m` em `θ = 2,011 rad`, `x ≈ −28,3 m`), e que é por isso — e não só por redundância operacional — que se adota uma linha de 2–3 poços; recap e `claim` atualizados com as duas larguras e a condição de locação.
**Confiança:** alta.

---

### 🟠 [GEOAMB-M08-A04-EXEMPLO-007] — Ordem de grandeza da fuga por liner composto superestimada e internamente contraditória

**Aula:** 04. **Claim relacionado:** efeito da geomembrana sobre a fuga pelo liner.

**Achado:** a parte (c) do exemplo afirmava que a fuga por um liner composto fica "da ordem de **dezenas** de litros por hectare por dia — duas a três ordens de grandeza abaixo dos ~950 m³/ano da CCL isolada". As duas metades da frase se contradizem. Os 950 m³/ano sobre 4 ha equivalem a 651 L/ha·dia; duas a três ordens de grandeza abaixo disso são **0,65 a 6,5 L/ha·dia** — unidades, não dezenas.

O recálculo independente pelas expressões empíricas de Giroud & Bonaparte (1989) confirma as unidades. Para contato bom, `Q = 0,21·a^0,1·h^0,9·k^0,74` (SI), com `a = 1 cm² = 1×10⁻⁴ m²`, `h = 0,30 m`, `k = 5×10⁻¹⁰ m/s`:

`Q = 0,21 × 0,398 × 0,338 × 1,31×10⁻⁷ = 3,7×10⁻⁹ m³/s` por furo = **0,32 L/dia por furo**.

Com a densidade usual de defeitos após bom controle de qualidade (poucos por hectare), isso dá ordem de **0,3 a 3 L/ha·dia**, ou ~1 a 7 m³/ano sobre os 4 ha. "Dezenas" superestima em cerca de uma ordem de grandeza.

**Correção aplicada:** ✅ parte (c) reescrita com o cálculo explícito de Giroud & Bonaparte (0,3 L/dia por furo), a ordem correta ("poucos litros por hectare por dia — unidades, não dezenas") e a conversão para a mesma base dos 950 m³/ano, tornando a afirmação de "duas a três ordens de grandeza" verificável pelo aluno; `claim` atualizado com os valores e com a hipótese de cálculo declarada.
**Confiança:** alta.

---

### 🟠 [GEOAMB-M08-A01-COMPAT-QUIMICA-004] — ASTM D6766 apresentada como o ensaio de compatibilidade de liners em geral

**Aula:** 01. **Claim relacionado:** ensaio de compatibilidade química do liner.

**Achado:** a norma existe e o título citado está correto, mas seu **escopo é específico de geocompostos bentoníticos (GCL)**. O texto — no corpo, na tabela de propriedades e no recap — a apresentava como *o* ensaio de compatibilidade do projeto de liner, inclusive no contexto de camada de argila compactada (CCL), que é o material discutido em todo o resto da aula e do exemplo trabalhado. Para CCL, a verificação de compatibilidade é feita permeando o corpo de prova com o lixiviado da obra em permeâmetro de parede flexível, pelo procedimento da **ASTM D5084**. Um aluno que saísse da aula especificando D6766 para um liner de argila estaria citando norma de escopo errado — o mesmo tipo de defeito que o achado 🟠 do Módulo 06 registrou na atribuição do martelo do SPT.

**Correção aplicada:** ✅ corpo, tabela de propriedades, recap, lista de fontes e `claim` passaram a separar as duas normas por material (D6766 → GCL; D5084 → CCL); ASTM D5084 acrescentada à lista de fontes com o título completo.
**Confiança:** alta.

---

### 🟠 [GEOAMB-M08-A03-PNRS-VOLATIL-003] — Citação legal incorreta: "Lei 14.026/2020, art. 11-B"

**Aula:** 03. **Claim relacionado:** prazos de erradicação de lixões (claim marcado `risk: desatualizavel`).

**Achado:** o dispositivo citado não é o correto. O **art. 11-B** foi inserido pela Lei 14.026/2020 na **Lei 11.445/2007** (marco do saneamento) e trata de comprovação de capacidade econômico-financeira dos prestadores — nada a ver com resíduos sólidos. O escalonamento dos prazos de erradicação de lixões vem do **art. 11 da Lei 14.026/2020**, que deu nova redação ao **art. 54 da própria Lei 12.305/2010**. Num claim que a própria aula sinaliza como volátil e que instrui o aluno a reconfirmar o texto vigente, a citação errada é especialmente danosa: ela manda o leitor procurar no lugar errado.

**Correção aplicada:** ✅ callout de advertência, lista de fontes e `claim` corrigidos para "art. 11 da Lei 14.026/2020, que deu nova redação ao art. 54 da Lei 12.305/2010", com o escalonamento explicitado (2 de agosto de 2021 para capitais e municípios de região metropolitana, até 2 de agosto de 2024 para municípios com menos de 50 mil habitantes).
**Confiança:** alta.

---

### 🟠 [GEOAMB-M08-A06-RESIDUOS-006] — Referência bibliográfica inconsistente e não verificável

**Aula:** 06. **Claim relacionado:** uso de cinza volante em solo-cimento.

**Achado:** a lista de fontes trazia a entrada `"Javadi, S. & Ghavami, K. / Consoli, N. C. et al. (2001), 'Effect of fly ash and cure conditions on the strength of soil–cement', JGGE"`. A barra separando dois conjuntos de autores distintos indica hesitação do redator, e a referência, como escrita, não corresponde a uma publicação identificável: não é citável nem verificável. Referência não verificável em material de nível de especialização é defeito de auditoria mesmo quando a afirmação que ela sustenta é correta — e a afirmação (cinza volante como pozolana em estabilização de solo) é correta e está amplamente coberta por Edil (2005) e por Sharma & Reddy (2004, cap. 17).

**Correção aplicada:** ✅ entrada removida em vez de substituída por outra que eu não pudesse verificar com confiança alta. A alegação passa a se apoiar em Edil (2005) e Sharma & Reddy (2004, cap. 17), ambas verificadas. Acrescentada a **ASTM D6270** (*Standard Practice for Use of Scrap Tires in Civil Engineering Applications*), que é a fonte primária correta para o limite de espessura de camada de agregado de pneu contra aquecimento interno — afirmação que antes não tinha fonte própria.
**Recomendação ao usuário:** se quiser uma referência primária brasileira específica para cinza volante em solo-cimento, o grupo de Consoli (UFRGS) publicou sobre misturas solo–cinza volante–cal na JGGE em 2001; não a inseri porque não pude confirmar título e paginação com confiança alta.
**Confiança:** alta quanto ao defeito; a decisão de remover em vez de substituir é deliberada.

---

### 🟡 [GEOAMB-M08-A02-VARNES-005] — "Complexo" atribuído à atualização de Hungr et al. (2014), que o abandonou

**Aula:** 02. **Claim relacionado:** classificação de movimentos gravitacionais de massa.

**Achado:** o texto apresentava a tabela como "o sistema de Varnes (1978), **atualizado por** Hungr, Leroueil & Picarelli (2014)" e incluía a linha "Complexo". A revisão de 2014 justamente **descartou** a classe "complexo": ela detalha os tipos em 32 classes, subdivide o eixo de material (rocha; solo separado em argila/silte e areia/pedregulho/detrito) e recomenda descrever o movimento composto pela **sequência** de tipos observada, em vez de rotulá-lo com uma categoria genérica. Apresentar a lista de Varnes como se fosse a lista atualizada é impreciso num curso de especialização, e o aluno que citasse "classe complexo, Hungr et al. 2014" estaria errado.

**Correção aplicada:** ✅ a atribuição da tabela passou a ser exclusivamente de Varnes (1978); acrescentado callout curto explicando o que a revisão de 2014 mudou e registrando que a linha "Complexo" é de 1978; recap e `claim` atualizados.
**Confiança:** alta.

---

### 🟡 [GEOAMB-M08-A02-PIPING-008] — "Mecanismo de falha mais comum" superestima, e diverge da calibração do Módulo 06

**Aula:** 02. **Claim:** alegação criada nesta auditoria (não havia `claim_id` cobrindo a afirmação).

**Achado:** o texto afirmava que o piping "é o mecanismo de falha **mais comum** de barragens de terra pequenas e de maciços de aterro". Os levantamentos estatísticos de acidentes em barragens de aterro (Foster, Fell & Spannagle, 2000) colocam erosão interna e galgamento como as **duas** causas dominantes, com participações comparáveis e ordem que varia conforme o recorte da amostra — não há base para eleger uma delas como "a mais comum" sem qualificar o conjunto de dados. O ponto tem agravante de consistência interna: o Módulo 06, já auditado, calibrou a mesma afirmação como "causa histórica **frequente** de ruptura de barragens de terra", e a Aula 02 a escalou sem base nova.

**Correção aplicada:** ✅ redação alterada para "uma das duas causas históricas dominantes de ruptura de barragens de terra — ao lado do galgamento —, responde por parcela comparável do total nos levantamentos de acidentes"; acrescentado item de recap; criada a alegação `GEOAMB-M08-A02-PIPING-008` com Foster, Fell & Spannagle (2000) como fonte, e essa referência acrescentada à lista de fontes da aula.
**Confiança:** alta.

---

### 🟡 [GEOAMB-M08-A02-BACKCALC-007] — "Cerca de cinco vezes o tolerável" usa só o extremo favorável da faixa declarada na mesma frase

**Aula:** 02. **Claim relacionado:** exemplo trabalhado, parte (a), USLE.

**Achado:** o cálculo em si está correto — recálculo independente confirma `A = 6500 × 0,035 × 2,1 × 0,12 × 1,0 = 57,3 t·ha⁻¹·ano⁻¹`, e a variante com `C = 0,004` dá `1,91 t·ha⁻¹·ano⁻¹`. O defeito está na leitura: o parágrafo declara a tolerância como "tipicamente entre 4 e 12 t·ha⁻¹·ano⁻¹" e conclui, na frase seguinte, que a encosta perde "cerca de **cinco vezes** o tolerável". Cinco vezes só se obtém dividindo por 12, o extremo superior da faixa; dividindo por 4 o resultado é catorze vezes. A conclusão citava o número mais favorável de uma faixa que ela mesma acabara de abrir, o que num laudo seria uma escolha indefensável.

**Correção aplicada:** ✅ redação alterada para "de **cinco a catorze vezes** o tolerável", com a razão explicitada (a faixa, e não um múltiplo único, é o que se declara) e a origem da faixa nomeada (profundidade e taxa de formação do solo).
**Confiança:** alta.

---

### 🟡 [GEOAMB-M08-A02-ERODIBILIDADE-002] — Fonte citada não sustenta a parte litológica da alegação

**Aula:** 02. **Claim relacionado:** erodibilidade de solos.

**Achado:** a alegação tem duas metades com bases distintas. A primeira — erodibilidade máxima em texturas siltosas e areia fina, de baixa coesão e baixo teor de matéria orgânica — é exatamente o que o nomograma do fator `K` da USLE modela, e Wischmeier & Smith (1978) e Renard et al. (1997) a sustentam. A segunda — alta erodibilidade de **solos residuais de granito e de arenito** — não decorre do fator `K`: é resultado da literatura brasileira de geologia de engenharia e de conservação do solo, e não está nas duas fontes citadas. A alegação é verdadeira; a atribuição de fonte é que estava incorreta.

**Correção aplicada:** ✅ campo `source` do claim reescrito separando o que cada fonte sustenta, com a ressalva explícita de que "a parte litológica da alegação não decorre do fator K da USLE"; acrescentadas à lista de fontes da aula Salomão (1998, in *Geologia de Engenharia*, ABGE) e Bertoni & Lombardi Neto (2012, *Conservação do Solo*).
**Confiança:** alta quanto ao defeito de atribuição; alta quanto ao conteúdo da alegação.

---

### 🟡 [GEOAMB-M08-A03-SELECAO-004] — Restrição a aeródromos atribuída à NBR 13896

**Aula:** 03. **Claim relacionado:** critérios de seleção de área da NBR 13896.

**Achado:** a lista de critérios de seleção incluía "distâncias mínimas a corpos d'água superficiais, a núcleos habitacionais, a poços de abastecimento, **e a aeródromos**", toda ela apresentada como "seguindo a NBR 13896", e o `claim` repetia a atribuição. A restrição relativa a aeródromos não é critério de norma técnica de aterro: é regra de **segurança aérea**, hoje na Lei 12.725/2012 (que instituiu a Área de Segurança Aeroportuária e vedou atividades de atração de fauna no seu entorno), sucedendo a Resolução CONAMA 4/1995. A própria aula reconhece a natureza da restrição em "Erros comuns" ("é critério de segurança aérea, não ambiental"), o que torna a atribuição à NBR uma inconsistência interna. Registro de confiança: não pude confirmar com confiança alta o texto integral da NBR 13896:1997, mas a base legal correta da restrição a aeródromos é independente dela, e a correção aplicada é válida em qualquer hipótese.

**Correção aplicada:** ✅ o item de distâncias mínimas foi partido em dois, com a restrição a aeródromos destacada, sua base legal nomeada (Lei 12.725/2012, sucedendo a CONAMA 4/1995) e a advertência explícita de que não é critério da NBR 13896; item de "Erros comuns" reforçado ("ou procurá-la na NBR 13896"); `claim` e lista de fontes atualizados.
**Confiança:** alta quanto à base legal da restrição; média-alta quanto ao conteúdo literal da NBR 13896.

---

### 🟡 [GEOAMB-M08-A05-LIQUEFACAO-005] — "Deflagrada sem sismo" aplicado a Fundão sem a ressalva do próprio painel

**Aula:** 05. **Claim relacionado:** mecanismo de liquefação estática em Fundão e Feijão I.

**Achado:** a aula define liquefação estática como "deflagrada **sem sismo**" e, no mesmo bloco, afirma que foi o mecanismo identificado nos painéis de Fundão e de Feijão I. A definição está correta e os dois casos são de liquefação estática, mas a formulação categórica omite um fato registrado pelo próprio painel de Fundão: **três pequenos eventos sísmicos cerca de 90 minutos antes do colapso**, que o painel considerou possíveis **aceleradores** de um processo já em curso — não a causa. A causa fundamental identificada foi a perda de confinamento por extrusão lateral da lama depositada fora do limite de projeto, levando o rejeito arenoso saturado a deformação por extensão e à liquefação de fluxo. Feijão I, ao contrário, não teve gatilho externo algum. Um aluno que memorizasse "Fundão = sem sismo, ponto final" ficaria vulnerável ao primeiro texto que mencionasse os tremores.

**Correção aplicada:** ✅ definição ajustada para "deflagrada **sem necessidade de sismo**"; acrescentado callout curto registrando os três eventos sísmicos de Fundão, o papel de acelerador e não de causa, a causa fundamental identificada, o contraste com Feijão I (sem gatilho externo) e a lição generalizável (quando o material já está no limiar, o gatilho pode ser desprezível); `claim` atualizado com a ressalva de precisão explícita.
**Confiança:** alta.

---

### 🟡 [GEOAMB-M08-A01-TRANSITO-007 · GEOAMB-M08-A03-PLUMA-006] — Notação do fator de retardação divergente do Módulo 03

**Aulas:** 01 e 03. **Claim relacionado:** pré-requisito de retardação herdado do Módulo 03.

**Achado:** verificação cruzada solicitada. O Módulo 03, já auditado, define e usa de forma consistente `R = 1 + (ρ_b/n_e)·K_d`, com `ρ_b` a massa específica aparente do meio poroso e `n_e` a porosidade efetiva — notação que reaparece idêntica na aula, no questionário, nos flashcards e no relatório de auditoria daquele módulo. As Aulas 01 e 03 do Módulo 08 escreviam `R = 1 + ρd·Kd/n`, na seção "Antes de começar", isto é, exatamente no ponto em que o texto se apresenta como retomada literal do que foi ensinado. Duas divergências: `ρd` (massa específica seca) por `ρ_b`, e sobretudo **`n` (porosidade total) por `n_e` (porosidade efetiva)** — que não são a mesma grandeza. O valor numérico do exemplo não é afetado (o exemplo usa `R = 3` como dado), mas a inconsistência de notação num bloco de retomada é o tipo de atrito que faz o aluno duvidar se está diante da mesma fórmula.

**Correção aplicada:** ✅ as duas ocorrências harmonizadas com o Módulo 03 (`R = 1 + (ρ_b/n_e)·K_d`), com o significado dos símbolos explicitado na Aula 01.
**Confiança:** alta.

---

### 🟡 [GEOAMB-M08-A06-RESIDUOS-006] — NBR 15115 e NBR 15116 citadas com edição de 2004, posteriormente revisada

**Aula:** 06. **Claim relacionado:** RCD reciclado como agregado.

**Achado:** as duas normas de agregados reciclados de RCD estão citadas como `:2004`. Ambas foram objeto de revisão posterior, com alteração inclusive de título e escopo. Não pude confirmar a edição vigente com confiança alta a partir das fontes disponíveis nesta auditoria, e não invento desfecho: registro a incerteza em vez de trocar o ano por outro que eu não possa verificar.

**Correção aplicada:** ✅ citações **desversionadas** no corpo e na lista de fontes, com a instrução explícita "edições originais de 2004, posteriormente revisadas — **confirmar a edição vigente antes de citar**"; `claim` atualizado com a mesma ressalva. Também registrado como `maintenance_flag` do módulo. A afirmação técnica sustentada pelas normas (RCD reciclado como agregado para base, sub-base e aterro; variabilidade e contaminação por gesso e matéria orgânica como pontos de controle) não depende da edição e permanece correta.
**Confiança:** alta quanto ao fato de haver revisão posterior; **baixa** quanto ao ano e ao título da edição vigente — motivo do registro em vez de correção.

---

### 🔵 [GEOAMB-M08-A05-SU-LIQ-006] — O estatuto da razão de resistência liquefeita `su(liq)/σ'v0`

**Aula:** 05. **Claim:** "a resistência não cai a zero: desaba para um patamar não drenado baixo e aproximadamente constante, tipicamente 5 a 12 % da tensão efetiva vertical para rejeito fofo".

**Achado:** há debate técnico legítimo e ativo em torno de dois pontos desta afirmação. Primeiro, o **valor**: a faixa 0,05–0,12 é uma convenção de projeto derivada de retroanálises de rupturas e de correlações com o CPT (Robertson, 2010), e não uma constante do material; a escola de estado crítico (Jefferies & Been, 2016) sustenta que a resistência liquefeita é função do **parâmetro de estado** e da trajetória de tensões, de modo que uma faixa única por tipo de material é uma simplificação de engenharia, útil mas não fundamental. Segundo, a **constância**: se `su(liq)` é de fato aproximadamente constante durante o fluxo, ou se depende da velocidade de deformação e da geometria do escoamento, permanece em aberto — e é justamente essa dependência que controla o *runout*, cuja previsão continua sendo um dos problemas menos resolvidos da área. O texto da aula não toma partido dogmático: apresenta a faixa qualificada como "tipicamente", atribui a ela explicitamente o papel de governar o *runout*, e trata o próprio valor `0,10` do exemplo como "estimada por ensaios", isto é, como parâmetro de sítio e não como constante universal.

**Correção proposta:** nenhuma. O tratamento já é adequado, e a ressalva de que a razão vem de ensaios está no ponto exato onde o aluno estaria mais exposto a tomá-la como propriedade fixa.
**Confiança:** alta.

---

### ⚪ [GEOAMB-M08-A04-RECALQUE-005] — Faixa de recalque total de aterro de RSU

**Aula:** 04. **Claim:** "o recalque total de longo prazo de um aterro de RSU atinge tipicamente 15 a 30 % da altura".

**Achado:** a faixa é consistente com Sowers (1973) e com a literatura de projeto de aterros, e a afirmação qualitativamente central — que a parcela de biodegradação **remove massa** e por isso distingue o recalque de aterro do recalque de solo — é sólida e bem sustentada. Ressalva de baixo impacto: compilações posteriores registram valores acima de 30 %, chegando a cerca de 40 %, para resíduo de alto teor orgânico e baixa compactação inicial, de modo que o limite superior deve ser lido como típico e não como teto. O texto já apresenta os números como faixa típica ("chega a 15–30 %"), sem tratá-los como limite físico.

**Correção proposta:** nenhuma obrigatória.
**Confiança:** média-alta.

---

### ⚪ [GEOAMB-M08-A05-DESCARACT-007] — Origem regulatória da proibição do alteamento a montante

**Aula:** 05. **Claim:** proibição do método a montante e obrigação de descaracterização.

**Achado:** a alegação estava correta quanto ao conteúdo e ao instrumento vigente, mas atribuía a inovação exclusivamente à Lei 14.066/2020. A proibição e os prazos de descaracterização apareceram primeiro na **Resolução ANM nº 4/2019**, editada semanas após Brumadinho, e só depois foram elevados a lei. Não é erro — a lei é o instrumento vigente e é o que se cita num parecer —, mas o encadeamento importa para entender por que a resposta regulatória foi tão rápida e por que a norma infralegal precede a legal neste tema.

**Correção aplicada:** ✅ enriquecimento de baixo risco — callout de advertência, lista de fontes e `claim` passaram a registrar a Resolução ANM 4/2019 como origem, com a Lei 14.066/2020 como elevação a lei.
**Confiança:** alta.

---

### ⚪ [GEOAMB-M08-A03-NBR10004-001] — "Padrões de potabilidade" como critério da Classe II B

**Aula:** 03. **Claim:** definição de resíduo Classe II B (inerte).

**Achado:** a NBR 10004:2004 define o resíduo inerte pelo resultado do ensaio de solubilização (NBR 10006) confrontado com os limites do seu próprio anexo, que **derivam** dos padrões de potabilidade mas não são atualizados automaticamente junto com a portaria de potabilidade vigente do Ministério da Saúde. A formulação da aula ("não liberam constituintes acima dos padrões de potabilidade") é o atalho consagrado na prática e transmite corretamente o conceito, mas um aluno que fosse aplicar o critério deve consultar o anexo da norma, não a portaria de potabilidade.

**Correção proposta:** nenhuma. O atalho é padrão na literatura da área e a aula já remete o ensaio à norma.
**Confiança:** média-alta.

---

## Verificação independente dos exemplos trabalhados

Todos os seis exemplos foram recalculados do zero, sem reutilizar os resultados publicados.

- **Aula 01 — trânsito advectivo por CCL.** `i = (0,30+0,90)/0,90 = 1,3333`; `q = 1×10⁻⁹ × 1,3333 = 1,333×10⁻⁹ m/s`; base anual `1,333×10⁻⁹ × 3,156×10⁷ = 0,0421 m/ano ≈ 42 mm/ano`; `v = q/n = 3,175×10⁻⁹ m/s`; `t = 0,90/3,175×10⁻⁹ = 2,835×10⁸ s = 8,98 ≈ 9,0 anos`; `t_soluto = 3 × 9,0 = 27 anos`. **Confere.** ✅ (A constante `3,156×10⁷ s/ano` é o ano juliano de 365,25 dias — arredondamento legítimo, diferença de 0,08 % em relação ao ano de 365 dias; sem impacto.)
- **Aula 02, parte (a) — USLE.** `A = 6500 × 0,035 × 2,1 × 0,12 × 1,0`; `227,5 × 2,1 = 477,75`; `× 0,12 = 57,33 t·ha⁻¹·ano⁻¹`. Variante florestal: `477,75 × 0,004 = 1,91`. **Confere.** ✅ Ver achado 🟡 quanto à leitura do múltiplo da tolerância.
- **Aula 02, parte (b) — retroanálise por talude infinito.** `β = 22°`: `cos β = 0,92718`, `cos²β = 0,85967`, `sen β = 0,37461`. `τ = 19 × 3 × 0,37461 × 0,92718 = 57 × 0,34733 = 19,80 kPa`; `σn = 57 × 0,85967 = 49,00 kPa`; `u = 9,81 × 3 × 0,85967 = 25,30 kPa`; `σ'n = 23,70 kPa`; `tan 32° = 0,62487` → `23,70 × 0,62487 = 14,81 kPa`; `c' = 19,80 − 14,81 = 4,99 ≈ 5,0 kPa`. **Confere**, e usa corretamente o peso **total** no esforço motriz — a formulação que a Aula 05 contrariava. ✅
- **Aula 03 — matriz de decisão ponderada.** Pesos somam 1,00. Sítio A: `0,60+0,50+0,80+0,75+0,40 = 3,05`. Sítio B: `1,20+1,25+0,60+0,45+0,20 = 3,70`. Critérios de proteção do aquífero: `0,30+0,25 = 0,55`. **Confere.** ✅
- **Aula 04 — balanço hídrico e fuga.** `ES = 260 mm/ano`; `L = 1300 − 260 − 620 = 420 mm/ano`; `V = 0,420 × 40 000 = 16 800 m³/ano`; `÷365 = 46,0 m³/dia`. Fuga pela CCL: `i = 0,90/0,60 = 1,50`; `q = 7,5×10⁻¹⁰ m/s`; `× 3,156×10⁷ = 0,02367 m/ano = 23,7 mm/ano`; `× 40 000 = 947 ≈ 950 m³/ano`. **Confere.** ✅ Ver achado 🟠 quanto à ordem de grandeza da fuga do liner composto na parte (c).
- **Aula 05 — `FS` drenado × pós-liquefação.** **Não conferia** — ver achado 🔴. Valores corretos, verificados: `τ = 61,0 kPa`, `σ'v0 = 152,9 kPa`, `σ'n = 146,2 kPa`, `τf = 95,0 kPa`, `FS_drenado = 1,56`, `su(liq) = 15,3 kPa`, `FS_liq = 0,25`. ⚠️ **corrigido**
- **Aula 06 — zona de captura.** `q = 20 × 0,004 = 0,08 m/dia`; `v = 0,32 m/dia`; `W_∞ = 150/0,8 = 187,5 m`; `x_L = 150/(2π × 0,8) = 150/5,0265 = 29,84 m`. Fórmulas e aritmética **conferem**. ✅ Ver achado 🟠 quanto à largura na linha do poço, verificada independentemente pela função de corrente: `W_0 = Q/(2·b·q) = 93,8 m`.

## Verificação de normas, diplomas legais e referências

- **ASTM D6766** — designação e título corretos; escopo restrito a GCL. Ver achado 🟠. ✅
- **ASTM D5084** (permeâmetro de parede flexível) — acrescentada como norma correta para compatibilidade de CCL. ✅
- **ASTM D6270** (uso de pneus em obras civis) — acrescentada como fonte primária do limite de espessura de camada de agregado de pneu. ✅
- **ABNT NBR 10004:2004** (classificação), **10005:2004** (lixiviação), **10006:2004** (solubilização) — designações, anos e escopos conferem; as três classes (I, II A, II B) e o enquadramento do RSU como II A conferem. ✅
- **ABNT NBR 13896:1997** (aterros de resíduos não perigosos) e **NBR 10157:1987** (aterros de resíduos perigosos) — designações, anos e títulos conferem; escopo de cada uma corresponde ao uso que a aula faz. ✅ Ver achado 🟡 quanto à atribuição da restrição a aeródromos.
- **ABNT NBR 8419:1992** (apresentação de projetos de aterros sanitários de RSU) — confere. ✅
- **ABNT NBR 15115 e 15116** — existência e escopo conferem; ano de edição desatualizado. Ver achado 🟡. ⚠️
- **Lei 12.305/2010** (PNRS) — hierarquia do art. 9º reproduzida na ordem correta e completa; responsabilidade compartilhada, logística reversa (art. 33) e planos nos três níveis federativos conferem; a distinção legal entre "resíduo" e "rejeito", central na aula, confere. ✅
- **Decreto 10.936/2022** — data (12 de janeiro de 2022) e efeito (regulamenta a PNRS, substituindo o Decreto 7.404/2010) conferem. ✅
- **Lei 14.026/2020** — data confere; dispositivo citado estava errado. Ver achado 🟠. ⚠️
- **Lei 12.725/2012** (fauna nas imediações de aeródromos / ASA) — acrescentada como base legal correta da restrição a aeródromos. ✅
- **Lei 12.334/2010** (PNSB), **Lei 14.066/2020**, **Resolução ANM 4/2019**, **Resolução ANM 95/2022**, **Portaria DNPM 70.389/2017** — o encadeamento descrito (proibição do método a montante e descaracterização introduzidas pela ANM 4/2019, elevadas a lei pela 14.066/2020; regras consolidadas pela ANM 95/2022, antes dispersas, entre elas a Portaria 70.389/2017) confere. ✅
- **CONAMA 420/2009** — designação e objeto conferem; acrescentada a alteração pela Resolução 460/2013. ✅
- **GISTM (2020, ICMM/UNEP/PRI)** — designação, ano e autoria conferem. ✅
- **Varnes (1978)**, TRB Special Report 176, p. 11–33 — confere. ✅ **Hungr, Leroueil & Picarelli (2014)**, *Landslides* 11(2):167–194 — confere; ver achado 🟡 quanto ao que a revisão mudou.
- **Wischmeier & Smith (1978)** AH-537 e **Renard et al. (1997)** AH-703 — conferem; estrutura `A = R·K·LS·C·P` e a ressalva sobre SDR (perda em vertente ≠ produção de sedimento de bacia) conferem. ✅
- **Sherard et al. (1976)**, JGED-ASCE 102(GT1):69–85 — confere; a caracterização dos solos dispersivos (Na trocável alto, defloculação sem velocidade de fluxo, não detectáveis por granulometria e Atterberg, pinhole/crumb/dupla hidrometria) confere. ✅
- **Giroud & Bonaparte (1989)**, *Geotextiles and Geomembranes* 8(2):71–111 (Part II, composite liners) — confere. ✅
- **Sowers (1973)**, 8th ICSMFE, v.2:207–210 — confere. **Schroeder et al. (1994)**, HELP v3, EPA/600/R-94/168b — confere. **Albright, Benson & Waugh (2010)**, ASCE Press — confere. ✅
- **Morgenstern et al. (2016)** e **Robertson et al. (2019)** — painéis, autoria e conclusões conferem; ver achado 🟡 quanto à ressalva sísmica de Fundão. ✅
- **Robertson (2010)**, JGGE 136(6):842–853 — confere. **Jefferies & Been (2016)**, 2ª ed. CRC — confere. **Vick (1990)**, **Blight (2010)** — conferem. ✅
- **NRC (1994)**, *Alternatives for Ground Water Cleanup* — confere, e sustenta corretamente *tailing* e *rebound*. **USEPA (1998)** EPA/600/R-98/125 e **Gavaskar (1999)** JHM 68(1–2):41–71 — conferem. ✅
- **Javandel & Tsang (1986)** e **Grubb (1993)** — conferem como fontes da solução analítica de zona de captura. ✅
- **Kjeldsen et al. (2002)** CREST 32(4):297–336 e **Christensen et al. (2001)** *Applied Geochemistry* 16(7–8):659–718 — conferem; a evolução acidogênica → metanogênica e o papel da amônia como controlador do alcance de longo prazo da pluma conferem. ✅
- **Benson, Zhai & Wang (1994)** JGE-ASCE 120(2):366–387 — confere; sustenta o alvo de `K` e o efeito da umidade de moldagem. ✅
- Referência não verificável na Aula 06 — removida. Ver achado 🟠. ⚠️

## Verificação de conteúdo técnico não coberto por claim específico

- **Alvo `K ≤ 1×10⁻⁹ m/s`** para CCL e GCL (equivalente a 1×10⁻⁷ cm/s dos regulamentos USEPA Subtitle D): confere, e o texto o apresenta corretamente como alvo de projeto e não como impermeabilidade. ✅
- **Compactação no ramo úmido** produzindo estrutura dispersa e `K` uma a duas ordens abaixo do ramo seco, com o mínimo de `K` não coincidindo com a densidade seca máxima: confere (Mitchell & Soga, 2005, cap. 6; Benson et al., 1994), e é usado de forma consistente com o Módulo 06, Aula 02. ✅
- **Espessura de CCL 0,6–1,0 m** e **geomembrana de PEAD 1,5–2,0 mm**: dentro das faixas usuais de projeto e dos mínimos regulatórios. ✅
- **Carga de lixiviado ≤ 0,30 m sobre o liner** como exigência regulatória (40 CFR 258 e 264): confere. ✅
- **Liner duplo com camada de detecção de vazamento** para resíduos perigosos: confere. ✅
- **Ganho do liner composto vindo da interação** (a GM corta o fluxo pela área intacta; a CCL confina o vazamento sob cada furo) e não da soma de resistências em série: confere com Giroud & Bonaparte (1989) e Rowe et al. (2004); é conceitualmente correto e bem colocado em "Erros comuns". ✅
- **Balanço hídrico `L = P − ES − AET − ΔS`** e o HELP como ferramenta de referência com roteamento camada a camada e passo diário: confere. ✅
- **Cobertura evapotranspirativa** dependente de `ET > P`, adequada a clima árido e semiárido e falha em clima úmido: confere com Albright, Benson & Waugh (2010) e com o ACAP. A advertência de que a escolha é climática antes de ser geotécnica é correta e bem posicionada. ✅
- **Biogás ≈ 50 % CH₄**, gás de efeito estufa e risco de explosão por migração lateral: confere (faixa usual 45–60 %). ✅
- **Rejeito × estéril** e segregação hidráulica em praia arenosa e lama: conferem com Vick (1990). ✅
- **Métodos de alteamento** (montante, jusante, linha de centro) e a atribuição do método de montante a Fundão e a Feijão I: conferem com os dois relatórios de painel. ✅
- **Espessado, pasta e filtrado** em ordem crescente de desaguamento, com o filtrado compactado como aterro convencional: conferem. ✅
- **`FS ≥ 1,5` drenado de longo prazo e `FS ≥ 1,3` não drenado**, com exigências por classe de risco na regulamentação da ANM: conferem, e são consistentes com os valores dados na Aula 02 para taludes permanentes. ✅
- **Monitoramento priorizando poropressão**, com inclinômetros, marcos superficiais, medidores de vazão de dreno e InSAR: confere; a afirmação de que a poropressão precede a ruptura e o deslocamento visível já é tarde é correta e é a lição operacional central do bloco. ✅
- **Descaracterização** como reconformação para que a estrutura deixe de ser barragem: confere. ✅
- **Restauração / recuperação / reabilitação** e o PRAD como instrumento da meta de recuperação: conferem. ✅
- **Mapa das técnicas de remediação** (contenção × tratamento, in situ × ex situ, fonte × pluma) e as nove técnicas tabeladas: conferem quanto a meio, alvo e mecanismo. A regra de seleção por contaminante — VOC → SVE e air sparging; clorados dissolvidos → PRB de ferro zero-valente e biorremediação anaeróbia; metais → S/E e fitoextração, **nunca** oxidação ou volatilização; DNAPL livre → remoção de fonte antes de tratar pluma — confere e é o ponto tecnicamente mais denso da Aula 06. ✅
- **Back-diffusion** derrotando injeção e extração em meio heterogêneo de baixa permeabilidade, e sua relação com *tailing* e *rebound*: confere com NRC (1994). ✅
- **Escória de aciaria exigindo cura contra expansão por hidratação de CaO/MgO livres** e **agregado de pneu com espessura limitada contra combustão interna exotérmica**: conferem. ✅

## Consistência cruzada com os Módulos 03, 06 e 07

Verificação explicitamente solicitada. Os conceitos herdados foram conferidos contra a definição original de cada módulo.

| Conceito herdado | Módulo de origem | Uso no Módulo 08 | Situação |
|---|---|---|---|
| Lei de Darcy, condutividade hidráulica | M06 A04 (`v = k·i`) | A01, A04, A06 | ✅ consistente (o Módulo 08 grafa `K` maiúsculo, convenção hidrogeológica; o Módulo 06 usa `k`. Divergência apenas tipográfica, sem ambiguidade em contexto — registrada, sem correção) |
| Compactação, ramo seco × ramo úmido, curva de Proctor | M06 A02 | A01 | ✅ consistente, e corretamente estendido (o Módulo 06 lê a curva para densidade; a A01 a lê para `K` mínimo, e nomeia a inversão de objetivo) |
| Tensão efetiva `σ' = σ − u` | M06 A03 | A02, A05 | ✅ consistente |
| Adensamento e compressão secundária `Cα` | M06 A05 | A04 | ✅ consistente, e a A04 marca corretamente o limite da analogia (a parcela de biodegradação remove massa, o que não tem paralelo em solo) |
| Contração/dilatância, drenado × não drenado, `su` | M06 A06 | A05 | ✅ consistente; a A05 aplica a distinção ao caso extremo do rejeito contrátil sem redefinir os termos |
| Compactação × adensamento (par confundível) | M06 A02/A05 | A01 ("Erros comuns") | ✅ consistente com a distinção estabelecida no M06 |
| Piping, erosão interna, gradiente crítico | M06 A04 | A02 | ⚠️ **divergia** na calibração ("mais comum" × "frequente") — corrigido, ver 🟡 `PIPING-008` |
| Modelo de talude infinito | M07 A03 | A02 ✅ · A05 ⚠️ | A02 usa a formulação exata do M07; **A05 a contrariava** — corrigido, ver 🔴 |
| Suscetibilidade × perigo × risco | M07 A03 | A02 ("Antes de começar") | ✅ consistente |
| Sobreposição ponderada / AHP em SIG | M07 A03 | A03 (seleção de área) | ✅ consistente, e bem explicitado como caso particular de cartografia geotécnica derivada |
| Carga contaminante e fontes | M03 A01 | A03 | ✅ consistente |
| Advecção, dispersão, atenuação | M03 A02/A03 | A01, A03, A06 | ✅ consistente |
| Fator de retardação `R` | M03 A03 | A01, A03 | ⚠️ **notação divergia** (`n` por `n_e`, `ρd` por `ρ_b`) — corrigido, ver 🟡 |
| Vulnerabilidade GOD | M03 A05 | A03 | ✅ consistente |
| LNAPL / DNAPL | M03 A04 | A06 | ✅ consistente |
| Atenuação natural monitorada | M03 A03 | A06 | ✅ consistente, com a mesma exigência de linha de evidências |

Nota de símbolo interna ao módulo: `K` designa condutividade hidráulica nas Aulas 01, 03, 04 e 06 e o **fator de erodibilidade da USLE** na Aula 02. A colisão é herdada das duas literaturas e inevitável; nenhuma aula usa os dois sentidos simultaneamente. Encaminhada à revisão didática como ponto de clareza, não como achado de auditoria.

## Cobertura de objetivos de aprendizagem

| Objetivo | Aulas que cobrem | Verificado |
|---|---|---|
| geologia-avancado-m08-oa01 | a01, a04 | ✅ |
| geologia-avancado-m08-oa02 | a02 | ✅ |
| geologia-avancado-m08-oa03 | a03, a04, a05 | ✅ |
| geologia-avancado-m08-oa04 | a06 | ✅ |

Os quatro objetivos têm cobertura efetiva, e o `mapa_objetivo_secao` de cada aula corresponde ao conteúdo realmente desenvolvido. Nenhum objetivo ficou sem alegações auditáveis correspondentes.

## Pontos de manutenção periódica

Registrados como `maintenance_flags` do módulo no `course-state.yaml`, no mesmo padrão do Módulo 07. Não bloqueiam o gate: são conteúdo correto hoje, que envelhece de forma previsível e já está sinalizado por callout na própria aula.

1. **Legislação de resíduos (Aula 03)** — PNRS, Decreto 10.936/2022, prazos do art. 54 na redação do art. 11 da Lei 14.026/2020, e a restrição a aeródromos da Lei 12.725/2012.
2. **Legislação de barragens de rejeito (Aula 05)** — Lei 12.334/2010 alterada pela 14.066/2020, Resoluções ANM 4/2019 e 95/2022, GISTM 2020.
3. **Edição vigente das NBR 15115 e NBR 15116 (Aula 06)** — o único item com incerteza residual desta auditoria; o texto instrui explicitamente a confirmar antes de citar.

## Recomendação

**Aprovar o módulo para avaliação (questionários) e memorização (flashcards).** O achado 🔴, os cinco 🟠 e os oito 🟡 foram aplicados ao texto das aulas, aos recaps, às listas de fontes e aos blocos de metadados, de modo que **nenhum achado vermelho, laranja ou amarelo permanece em aberto** e não há `open_findings`. O achado 🔵 fica registrado como referência de um debate técnico legítimo (o estatuto da razão de resistência liquefeita), já tratado com a cautela apropriada; os três ⚪ são aproximações e atalhos de linguagem qualificados como tais.

Duas advertências para quem gerar a avaliação:

- **A Aula 05 mudou de números.** Qualquer questão ou flashcard sobre o exemplo de rejeito deve usar `τ = 61,0 kPa`, `FS drenado = 1,56` e `FS pós-liquefação = 0,25` — e o contraste didaticamente mais forte agora é que a estrutura **passa** no critério de 1,5 e ainda assim está liquefeita, não que tenha "folga confortável".
- **A Aula 06 mudou de conclusão qualitativa.** A zona de captura afunila; a largura que decide se um poço basta é a do local da pluma, não a assintótica. Questões que cobrem só `W = Q/(b·q)` perdem exatamente o ponto que a correção introduziu.
