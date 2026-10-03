# Auditoria científica — Módulo 02: Física do desbaste

> [!info] Curso de **Teoria da lapidação** · módulo 02 · modo **audit-and-fix** · profundidade **full**
> Executada em **2026-09-01** · Material auditado: as 5 aulas do módulo 02 · **Veredito: Aprovado com correções aplicadas**

## Escopo

Auditadas as 5 aulas do módulo 02, em conjunto (para pegar contradições entre aulas), a partir das **42 alegações auditáveis** declaradas nos rodapés e das afirmações adicionais não declaradas pelos autores.

Hierarquia de fontes aplicada, conforme instrução do curso: **Vargas & Vargas**, **Wykoff**, **United States Faceters Guild** e **Sinkankas** para valores lapidários; **International Gem Society** e **geology.com** para dados gemológicos e de granulometria; normas **ANSI/CAMI B74.18** e **FEPA-P** para numeração de grão; literatura de física de superfícies para mecanismos de polimento. **Trevor Hannam** (`_fontes/`) tratado apenas como corroboração secundária, nunca como fonte de valor — e o `_fontes/` não foi auditado, por ser material de entrada.

## Resumo

| Severidade | Achados | Corrigidos |
|---|---|---|
| 🔴 Erro | 2 | 2 |
| 🟠 Impreciso | 5 | 5 |
| 🟡 Desatualizado | 0 | — |
| 🔵 Sem fonte | 0 | — |
| ⚪ Controverso | 0 | — |
| **Total** | **7** | **7** |

**Achados 🔴/🟠 em aberto: 0.** O gate para questionário e flashcards está liberado.

---

## Achados

### 🔴 1. Óxido de crômio declarado mais mole que o quartzo

**claim_id:** `ABR-POL-MOLE-001`
**Tipo:** erro factual
**Onde:** aula 01 · seção "Os abrasivos e polidores reais na escala" (e repetido no "Recap relâmpago" e em "O que não concluir")
**Está escrito:** "Já os polidores — óxido de crômio, de estanho e de cério — são **mais moles que o quartzo** (Mohs 7), anomalia que a aula 04 resolve"
**Problema:** falso para o óxido de crômio. O Cr₂O₃ tem dureza da ordem de **8 a 8,5 em Mohs** — bem acima do quartzo. A generalização criava um erro caro: o paradoxo pedagógico do módulo (polidor mole vencendo gema dura) é real para cério e estanho, mas **não** para o crômio, e afirmá-lo do crômio inverteria a conclusão do aluno na aula 04.
**Correção aplicada:** o trecho passou a distinguir os dois casos — cério (~6) e estanho (~6 a 7) não superam o quartzo; crômio fica em 8 a 8,5, acima dele. Novo `claim_id` `ABR-POL-CROM-001` criado para o dado do crômio.
**Fonte:** dados de dureza de Cr₂O₃ / eskolaita (literatura de materiais); corroborado por fornecedores lapidários de green rouge · **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** aula 04 (lista de polidores) — verificada, não afirma dureza, nenhuma correção necessária.
**Desfecho:** **Corrigido**

---

### 🔴 2. Tabela de grão da aula 03 deslocada e em contradição com o texto da própria aula

**claim_id:** `SEQ-TAB-MARCOS-001`
**Tipo:** erro factual + inconsistência interna
**Onde:** aula 03 · seção "Uma tabela de marcos, com o sistema declarado" (e propagado ao "Exemplo trabalhado")
**Está escrito (tabela original):** 1200 → "3–6 µm"; 3000 → "1–2 µm"; 8000–14000 → "0,5–1 µm"; 50000 → "0,25 µm"; 100000 → "abaixo de 0,25 µm"
**Problema:** duplo. **(a)** Todo o bloco de diamante estava deslocado em cerca de uma etapa: na convenção lapidária, 1200 ≈ 15 µm, 3000 ≈ 6–7 µm, 8000 ≈ 3 µm, 14000 ≈ 1 µm, 50000 ≈ 0,5 µm, 100000 ≈ 0,25 µm. **(b)** A tabela **contradizia o texto da própria aula**, que dava a sequência correta ("60 → 30 → 14–15 → 6 → 3 → 1 → 0,5 → 0,25 µm") três parágrafos acima. Havia ainda uma terceira inconsistência: o texto afirmava que "os valores até 1200 seguem a referência ANSI/CAMI" enquanto a tabela rotulava a linha 1200 como "convenção diamante".
**Correção aplicada:** tabela reconstruída em **dois blocos declarados** — referência ANSI/CAMI (60 ≈ 250–270 µm, 220 ≈ 66 µm, 600 ≈ 15 µm, 1200 ≈ 6,5 µm) e convenção comercial do pó de diamante (600 ≈ 30, 1200 ≈ 15, 3000 ≈ 6–7, 8000 ≈ 3, 14000 ≈ 1, 50000 ≈ 0,5, 100000 ≈ 0,25 µm). A colisão do marco 1200 (≈6,5 µm em CAMI × ≈15 µm em diamante) virou **exemplo explícito da própria tese da aula** — o mesmo número designando partículas diferentes. Novo `claim_id` `SEQ-COLIS-1200-001` criado para esse dado.
**Fonte:** International Gem Society, *Gem Cutting Abrasives in Grit, Mesh, and Microns*; ANSI/CAMI B74.18 · **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** "Exemplo trabalhado" da aula 03, que afirmava "o 3000 trabalha com partículas de 1 a 2 µm" — **corrigido junto**, e o exemplo inteiro foi reancorado na convenção do diamante (600 → 1200 → 3000 → 8000) para não misturar sistemas. Recap e "Erros comuns" atualizados.
**Desfecho:** **Corrigido**

---

### 🟠 3. Faixas de dureza anisotrópica da cianita subestimadas nos dois extremos

**claim_id:** `ABR-ANIS-DIR-001`
**Tipo:** valor fora da faixa aceita
**Onde:** aula 01 · seção "Dureza diferencial dentro da mesma pedra"
**Está escrito:** "da ordem de 4 a 5 ao longo do cristal a 6 a 7 na direção perpendicular"
**Problema:** os valores canônicos são **4,5–5 paralelo ao comprimento** e **6,5–7 na direção transversal**. Ambos os extremos estavam meio ponto baixos.
**Correção aplicada:** valores substituídos por 4,5–5 e 6,5–7; a atribuição de direção, que já estava correta, foi preservada e explicitada no `claim`.
**Fonte:** geology.com, *Kyanite Mineral* · **Nível:** base de referência
**Confiança:** confirmado
**Desfecho:** **Corrigido**

---

### 🟠 4. "O diamante é medido em mícrons, não em mesh" — certeza indevida

**claim_id:** `SEQ-DIAM-MICR-001`
**Tipo:** certeza indevida / confusão de escopo
**Onde:** aula 03 · seção "Por que o diamante é medido em mícrons"
**Está escrito:** "a literatura lapidária especifica o diamante pelo tamanho da partícula, em mícrons, **em vez de** mesh"
**Problema:** falso como exclusão. O pó de diamante é comercializado **das duas formas** — por número de grão (3000, 50000, 100000) e por mícron. A formulação exclusiva também contradizia a própria tabela da aula, que usa números de grão de diamante.
**Correção aplicada:** afirmação reformulada para o que é verdadeiro e mais forte pedagogicamente — o diamante é vendido nas duas formas, e o **mícron é a medida inequívoca** porque não depende de convenção. Título da seção alterado para "Por que o mícron é a medida inequívoca".
**Fonte:** International Gem Society, *Gem Cutting Abrasives in Grit, Mesh, and Microns* · **Nível:** base de referência
**Confiança:** confirmado
**Desfecho:** **Corrigido**

---

### 🟠 5. Linha "600 CAMI" com faixa larga demais

**claim_id:** `SEQ-TAB-MARCOS-001` (mesmo achado, linha distinta)
**Tipo:** valor impreciso
**Onde:** aula 03 · tabela
**Está escrito:** "600 (CAMI) → da ordem de 10–16 µm"
**Problema:** o valor mediano de CAMI 600 é da ordem de **14,5 a 16 µm**; o extremo inferior de 10 µm não é sustentado. Igualmente, "60 CAMI → 250 µm" e "220 CAMI → 60 µm" estavam levemente baixos (valores de referência: ~268 e ~66 µm).
**Correção aplicada:** linhas ajustadas para ~15 µm, ~250–270 µm e ~66 µm respectivamente.
**Fonte:** ANSI/CAMI B74.18 (tabelas de granulometria) · **Nível:** normativa
**Confiança:** confirmado
**Desfecho:** **Corrigido**

---

### 🟠 6. Teoria química do polimento atribuída a Cook em paralelo falso com Hooke e Beilby

**claim_id:** `POL-QUIM-HIDR-001`
**Tipo:** omissão que gera erro
**Onde:** aula 04 · "Mecanismo 3 — ação químico-mecânica"
**Está escrito:** "linha da literatura de polimento de vidro **associada ao estudo de Cook**"
**Problema:** a aula nomeia **Hooke** como autor do mecanismo 1 e **Beilby** como autor do mecanismo 2; nomear apenas Cook no mecanismo 3 cria o paralelo implícito — e falso — de que Cook o originou. A teoria química foi formulada por **Preston e Grebenshchikov**; Cook (1990) é a síntese moderna de referência, não a origem.
**Correção aplicada:** crédito corrigido para "proposta por Preston e Grebenshchikov e desenvolvida no estudo de Cook". Fontes consultadas e `claim` atualizados.
**Fonte:** literatura histórica de polimento de vidro (revisão das três teorias: abrasão — Hooke/Newton/Rayleigh; escoamento — Beilby; química — Preston/Grebenshchikov) · **Nível:** revisada por pares
**Confiança:** confirmado
**Desfecho:** **Corrigido**

---

### 🟠 7. Clivagem atribuída à apatita como mecanismo de dano térmico

**claim_id:** `CAL-APAT-FRAG-001` (novo)
**Tipo:** erro de mecanismo
**Onde:** aula 05 · seção "Gemas termicamente sensíveis e por quê"
**Está escrito:** "**Fluorita** e **apatita**: dureza baixa somada a clivagem."
**Problema:** a apatita tem clivagem **fraca a indistinta** — não é ela o mecanismo. A vulnerabilidade real da apatita vem de ser um material **quebradiço** com **sensibilidade alta a calor e a choque**. Agrupá-la com a fluorita (que sim tem clivagem octaédrica perfeita) ensinava o mecanismo errado, exatamente o que a própria aula adverte em "Erros comuns" ao dizer que cada gema é sensível por mecanismo próprio.
**Correção aplicada:** as duas separadas, cada uma com seu mecanismo real. Novo `claim_id` criado.
**Fonte:** International Gem Society, *Apatite Faceting Information*; geology.com, *Apatite* · **Nível:** base de referência
**Confiança:** confirmado
**Desfecho:** **Corrigido**

---

## Verificado e correto

Alegações checadas contra fonte que **passaram sem correção** — registradas para que a auditoria seja refazível:

| Alegação | Veredito | Fonte |
|---|---|---|
| Mohs é ordinal, não linear; o salto 9→10 é ordens de grandeza maior que entre minerais moles | ✅ confirmado | escalas Knoop comparadas (talco ~1, gipsita ~32, coríndon ~2000, diamante ~7000) |
| Coríndon ~2.000–2.100 Knoop; diamante ~7.000–8.000 Knoop | ✅ dentro das faixas citadas na literatura (variam com o plano cristalográfico e a fonte, ressalva já presente no texto) | tabelas de dureza Knoop |
| Carbeto de silício ~9,5 Mohs; alumina ~9 | ✅ confirmado | literatura de abrasivos |
| Óxido de cério ~6 Mohs, abaixo do quartzo (7) — o paradoxo central do módulo | ✅ confirmado | literatura de polimento de silicatos |
| Diamante só é cortado por diamante | ✅ confirmado | Sinkankas |
| Regime frágil e remoção por coalescência de microfraturas em gemas | ✅ confirmado | literatura de usinagem de materiais frágeis |
| Profundidade de dano subsuperficial escala com o tamanho do grão, "da ordem de algumas vezes" | ✅ confirmado, e adequadamente hedgeado como ordem de grandeza | literatura de fabricação óptica |
| P600 (FEPA) é partícula maior que 600 (CAMI); os sistemas divergem mais no fino | ✅ confirmado (P600 ≈ 25,8 µm × CAMI 600 ≈ 14,5 µm) | ANSI/CAMI B74.18 e FEPA-P |
| Superfície vira especular quando a rugosidade cai abaixo do comprimento de onda visível (0,4–0,7 µm) | ✅ confirmado como ordem de grandeza | óptica geral |
| Microabrasão atribuída a Robert Hooke (1665) | ✅ confirmado — Hooke argumentou que o polidor apenas corta sulcos muito finos | literatura histórica de polimento |
| Camada de Beilby: hipótese de George Beilby, início do séc. XX, existência ainda disputada | ✅ confirmado; o mecanismo do polimento segue explicitamente não resolvido na literatura | física de superfícies |
| Opala (desidratação), tanzanita e kunzita (clivagem), esmeralda (inclusão fluida), peridoto (choque térmico), topázio e feldspato (clivagem) | ✅ confirmados, cada um com o mecanismo correto | GIA / literatura gemológica |
| Sílica cristalina livre no corte a seco e risco de silicose | ✅ confirmado | saúde ocupacional |
| Refrigerante com três funções (calor, swarf, poeira) | ✅ confirmado | Sinkankas; Vargas & Vargas |

## Contradições entre aulas

Verificadas explicitamente, já que as 5 aulas foram escritas em paralelo:

- **Cério × quartzo** — aulas 01 e 04 concordam após a correção do achado 1 (~6 contra 7).
- **Sequência de grão** — a contradição interna da aula 03 (achado 2) era o único caso; resolvida.
- **Dano subsuperficial** — aulas 02, 03 e 05 usam o conceito de forma consistente.
- **Fronteiras de escopo** — nenhuma aula invade o território da outra; os deferimentos para os módulos 03 e 04 são coerentes entre si.

## Observação fora do escopo da auditoria

Registrada em uma linha, sem misturar com os achados factuais: a correção do achado 2 aumentou a aula 03 (tabela com mais linhas). Prosa redundante foi enxugada para compensar e os rodapés `palavras_corpo` foram todos ressincronizados com a contagem real. O ajuste fino do teto de LC-02 cabe à revisão didática, não a esta auditoria.

## Correções aplicadas

**Aplicadas em:** 2026-09-01

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `ABR-POL-MOLE-001` + `ABR-POL-CROM-001` (novo) | 🔴 | Corrigido | aula-01 |
| `SEQ-TAB-MARCOS-001` + `SEQ-COLIS-1200-001` (novo) | 🔴 | Corrigido | aula-03 |
| `ABR-ANIS-DIR-001` | 🟠 | Corrigido | aula-01 |
| `SEQ-DIAM-MICR-001` | 🟠 | Corrigido | aula-03 |
| `SEQ-TAB-MARCOS-001` (linhas CAMI) | 🟠 | Corrigido | aula-03 |
| `POL-QUIM-HIDR-001` | 🟠 | Corrigido | aula-04 |
| `CAL-APAT-FRAG-001` (novo) | 🟠 | Corrigido | aula-05 |

**Material derivado:** nenhum questionário e nenhum baralho de flashcards existiam no momento da auditoria — a ordem do pipeline foi respeitada, então **não houve propagação a fazer**. Nenhum baralho foi importado no Anki para este módulo, portanto não há card já em revisão a corrigir à mão.

**Pendências:** nenhuma. Todos os 7 achados foram corrigidos na mesma passada.
