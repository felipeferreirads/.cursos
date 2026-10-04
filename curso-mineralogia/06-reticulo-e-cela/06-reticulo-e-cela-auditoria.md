# Auditoria científica: Módulo 06 — Retículo cristalino, cela unitária e redes de Bravais

**Auditado em:** 2026-10-04
**Material:** `curso-mineralogia/06-reticulo-e-cela/` — as 4 aulas (`06-reticulo-e-cela-aula-01` a `-aula-04`) e as figuras 1 a 6; cruzamento com os módulos 04 e 05
**Modo:** audit-and-fix
**Profundidade:** full, com recálculo de todos os volumes, densidades e Z (Python) e conferência dos parâmetros de cela e grupos espaciais citados
**Escopo:** as alegações dos rodapés `alegacoes_auditaveis` e as afirmações de risco do corpo: definição de retículo, motivo e estrutura; teste da vizinhança (colmeia de grafita, tabuleiro); pesos de compartilhamento; vetores de centragem; cela primitiva do retículo F; os 14 retículos, seus símbolos e as razões das combinações ausentes; datas de Frankenheim e Bravais; um exemplo mineral por retículo (grupo espacial); hP × hR e trigonal × romboédrico; fórmulas de volume; densidades calculadas e medidas; cela romboédrica × hexagonal da calcita. Questionário e baralho ainda não existiam.
**Veredito:** Requer correção → **correções aplicadas; estado final: Aprovado** (nenhum achado aberto)

## Resumo

🔴 0 erros · 🟠 0 imprecisões · 🟡 4 imprecisões menores (uma delas no módulo 04) · 🔵 0 sem fonte · ⚪ 0 controversos
Verificadas e corretas: 28 alegações dos rodapés (31 no total; ver o manifesto `.json`) e todas as contas.

O núcleo formal passou sem erro: a lista dos 14 (1 + 2 + 4 + 2 + 2 + 3), os símbolos, as razões de colapso (tC = tP, tF = tI, mI = mC) e de quebra de simetria (sem cC nem hC), os vetores de centragem, as fórmulas de volume e de densidade, e todos os números. Os achados são de formulação.

**Contas conferidas (Python, 2026-10-04; Nₐ = 6,022 140 76 × 10²³ mol⁻¹, massas atômicas IUPAC abreviadas):**

| O quê | Resultado | Referência | Onde |
|---|---|---|---|
| Halita: V = 5,6404³; ρ (Z = 4, M = 58,44) | 179,44 Å³; 2,163 g/cm³ | HoM: D(calc.) 2,165, D(meas.) 2,168 | aula 04 |
| Quartzo: V = 0,866·4,9133²·5,4053; ρ (Z = 3) | 113,00 Å³; 2,649 | HoM: D(meas.) 2,65 | aula 04 |
| Calcita (hex.): V; ρ (Z = 6, M = 100,09) | 367,85 Å³; 2,711 | HoM: D(meas.) 2,7102, D(calc.) 2,711 | aula 04 |
| Calcita (romb. primitiva): a_r = √(3a² + c²)/3; α; V | 6,375 Å; 46,08°; 122,62 Å³ (= V_hex/3) | — | aula 04 |
| Fluorita: Z = 3,18·0,6022·163,00/78,07 | 4,00 | HoM: a = 5,4626, D(calc.) 3,180 | aula 04 |
| Diopsídio: M; V = abc·sen β; ρ (Z = 4); V e ρ sem sen β | 216,55; 438,6 Å³; 3,28; 455,4 Å³ e 3,16 | HoM (por busca): a = 9,746, b = 8,899, c = 5,251, β = 105,63° | aula 04 |
| Retículo F: ângulo entre os vetores primitivos (0, ½, ½) etc.; volume | 60,00°; a³/4 | — | aula 02 |
| Halita: posições de Na e Cl; contagem | 4 + 4 | Fm3̄m, Z = 4 | aula 02 |

> [!note] Limite da verificação nesta sessão
> Como no módulo 05, o acesso direto aos sites de referência estava bloqueado; parâmetros, densidades e grupos espaciais foram conferidos por busca (resultados que citam as fichas em PDF do *Handbook of Mineralogy*), e os grupos espaciais já conferidos na auditoria do módulo 04 foram reaproveitados (cianita, diopsídio, forsterita, aragonita, hemimorfita, rutilo, zircão, quartzo, berilo, calcita, coríndon, pirita, granadas, halita, fluorita, diamante). Epídoto P2₁/m, cordierita Cccm e enxofre Fddd foram conferidos por busca nesta sessão. As datas de Frankenheim (1842) e Bravais (1848, publicado em 1850) vieram de busca, com remissão ao *IUCr Newsletter* 27(1). A escolha do diopsídio, e não do ortoclásio, para o exemplo monoclínico decorre do achado 🟠 6 da auditoria do módulo 05 (c do ortoclásio não confirmado).

## Achados

### 🟡 1. "Calculada e medida concordam na segunda casa decimal"

**claim_id:** `CRI-ZDE-CALCMED-001`  ·  **Tipo:** certeza indevida  ·  **Onde:** aula 04 · Calculada × medida
**Problema:** generalização sem fonte; há espécies comuns em que a diferença passa de alguns centésimos (substituições, defeitos).
**Correção aplicada:** "As duas costumam ficar próximas (diferenças de alguns centésimos são comuns); quando divergem muito, é a amostra que tem algo a contar."  ·  **Confiança:** confirmado (pares D(meas.)/D(calc.) do HoM).

### 🟡 2. Remissão que prometia o que a aula de destino não tem

**claim_id:** `CRI-ZDE-CLIVCALC-001`  ·  **Tipo:** inconsistência interna  ·  **Onde:** aula 04 · Uma cela romboédrica, uma cela hexagonal
**Problema:** "o romboedro de clivagem, com seus ângulos de cerca de 75° e 105°, é outra coisa (módulo 05, aula 03)" — a aula 03 do módulo 05 dá os **índices** da clivagem ({101̄4} / {101̄1}), não os ângulos. Os ângulos (74,9° e 105,1°) foram calculados na auditoria do módulo 05.
**Correção aplicada:** "o romboedro de clivagem, com ângulos entre faces de cerca de 75° e 105°, é outra coisa (os índices dessa clivagem estão no módulo 05, aula 03)."  ·  **Confiança:** confirmado (cálculo: 74,94° com a cela do HoM).

### 🟡 3. Justificativa incompleta para as quatro centragens do ortorrômbico

**claim_id:** `CRI-BRA-QUEBRA-001`  ·  **Tipo:** omissão  ·  **Onde:** aula 03 · Por que não 7 × 5
**Está escrito:** "seus três eixos já são diferentes, e nenhuma centragem tem como quebrar uma simetria que obrigue igualdade."
**Problema:** a aula dá **duas** razões para combinações ausentes (colapso numa cela menor do mesmo sistema; quebra de simetria) e justificava o ortorrômbico só pela segunda.
**Correção aplicada:** "cada centragem preserva os três eixos 2 (nenhuma quebra a simetria) e nenhuma pode ser redescrita como uma cela ortorrômbica menor (nenhuma colapsa)."  ·  **Fonte:** *International Tables*, vol. A  ·  **Confiança:** confirmado.

### 🟡 4. (cross-module, módulo 04) "Cela unitária: a menor unidade que se repete"

**claim_id:** `CRI-EST-CELA-001`
**Tipo:** imprecisão (definição que contradiz a aula 02 deste módulo)
**Onde:** módulo 04, aula 01 · "O tijolo de Haüy..."; baralho do módulo 04, card `mineralogia-m04-fb011`
**Está escrito:** "a **cela unitária** (módulo 06): a menor unidade que, repetida por translação, reconstrói o cristal."
**Problema:** a menor é a cela **primitiva**; a cela convencional, que é a usada nas fichas, pode ter 2, 3 ou 4 vezes esse volume (aula 02 deste módulo). O card `fb011` repetia a frase e estava sendo memorizado.
**Correção aplicada:** "a unidade que, repetida por translação, reconstrói o cristal (a menor delas é a cela primitiva)", na aula 01 do módulo 04, em `04-simetria-e-morfologia-flashcards-basic.csv` e em `04-simetria-e-morfologia-flashcards.md` (o ID `fb011` foi mantido; histórico do baralho anotado). Rodapé da aula ganhou o `claim_id`; o `content_hash` e `palavras_corpo` da aula foram atualizados no `course-state.yaml`; a auditoria do módulo 04 ganhou uma seção "Correção posterior".
**Fonte:** IUCr, *Online Dictionary of Crystallography* ("Unit cell", "Primitive cell")  ·  **Confiança:** confirmado
**Aviso:** se o baralho do módulo 04 já foi importado no Anki, o card `fb011` precisa ser corrigido à mão.

## Verificado e correto (seleção)

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `CRI-RET-DEF-001` | estrutura = retículo + motivo; retículo = pontos de vizinhança idêntica | IUCr *Online Dictionary* | confirmado |
| `CRI-RET-GRAFITA-001` | colmeia não é retículo; hexagonal com 2 C | IUCr; Klein & Dutrow | confirmado |
| `CRI-CEL-PESOS-001` | 1/8, 1/4, 1/2, 1; P 1, I 2, F 4 | Klein & Dutrow | confirmado |
| `CRI-CEL-CENTRAGEM-001` | vetores de centragem C, A, B, I, F | *Int. Tables* A | confirmado |
| `CRI-CEL-FCCPRIM-001` | primitiva do F: romboedro de 60°, ¼ do volume | cálculo | confirmado |
| `CRI-BRA-LISTA-001` | 14 retículos e símbolos | *Int. Tables* A | confirmado |
| `CRI-BRA-HIST-001` | Frankenheim 1842 (15); Bravais 1848/1850 (14) | IUCr Newsletter 27(1); busca | confirmado |
| `CRI-BRA-COLAPSO-001` | tC = tP; tF = tI; mI = mC | *Int. Tables* A | confirmado |
| `CRI-BRA-EXEMPLOS-001` | um mineral por retículo | HoM; auditoria m04; busca | confirmado |
| `CRI-BRA-HEX-001` | hP e hR; quartzo hP, calcita e coríndon hR | *Int. Tables* A | confirmado |
| `CRI-ZDE-FORMULA-001` | ρ = Z·M/(0,6022·V) | SI; cálculo | confirmado |
| `CRI-ZDE-CALCITA-001` | calcita: Z = 6 (hex.) e 2 (romb.); pontos (⅔, ⅓, ⅓), (⅓, ⅔, ⅔) | HoM; *Int. Tables* A | confirmado |

## Consistência interna e com o resto do curso

- **Módulo 04, aula 06:** "sete sistemas reticulares; o quartzo é trigonal com retículo hexagonal" — coerente com a aula 03 (hP × hR).
- **Módulo 04, aula 01:** definição de cela unitária — corrigida (achado 4).
- **Módulo 05, aula 01:** parâmetros de cela como comprimentos e ângulos dos eixos — a aula 01 deste módulo os reinterpreta como as translações; mesmos valores (halita, quartzo, calcita, diopsídio).
- **Módulo 05, aula 03:** clivagem da calcita {101̄4} — a aula 04 distingue a cela (46°) do romboedro de clivagem (~75°/105°), com a remissão corrigida (achado 2).
- **Módulo 01, aula 06:** mol, massa molar, ångström — reaproveitados sem conflito.

## Correções aplicadas

**Aplicadas em:** 2026-10-04

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `CRI-ZDE-CALCMED-001` | 🟡 | Corrigido | aula-04 |
| `CRI-ZDE-CLIVCALC-001` | 🟡 | Corrigido | aula-04 |
| `CRI-BRA-QUEBRA-001` | 🟡 | Corrigido | aula-03 |
| `CRI-EST-CELA-001` | 🟡 | Corrigido (propagado) | m04 aula-01; m04 flashcards-basic.csv e flashcards.md (`fb011`); m04 auditoria |

Também foram atualizados: os rodapés `alegacoes_auditaveis` das aulas (campo `audit:`), o hub do módulo e o `course-state.yaml` (blocos `audit` do 06 e `lessons` do 04).

## Segunda passagem (depois da revisão didática)

**Em:** 2026-10-04. A revisão didática acrescentou a figura 6 (cela da halita com Na e Cl, desenhada a partir das mesmas coordenadas do exemplo), encurtou o exemplo do quartzo da aula 04 (mesmos números) e acrescentou frases de orientação. Nenhum fato novo além da figura; as posições da figura 6 foram conferidas contra o exemplo (Na nos 8 vértices e 6 faces; Cl nas 12 arestas e no centro).

**Pendências:** nenhuma.

**Aviso de baralho já importado:** vale para o card `mineralogia-m04-fb011` do módulo 04 (achado 4).
