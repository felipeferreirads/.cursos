# Auditoria científica: Módulo 11 — Arquitetura dos silicatos

**Auditado em:** 2026-10-06
**Material:** `curso-mineralogia/11-estrutura-dos-silicatos/` — as 5 aulas (`-aula-01` a `-aula-05`) e as figuras 1 a 3; cruzamento com o módulo 01 (aulas 03 a 06), o módulo 02 (aulas 04 e 05), o módulo 05 (aula 01), o módulo 06 (aula 04), o módulo 08 (aulas 01, 02, 04, 05 e 06), o módulo 09 (aulas 01, 02 e 05) e o módulo 10 (aula 01); coerência com os hubs dos módulos 33 a 36 (ainda não escritos)
**Modo:** audit-and-fix
**Profundidade:** full, com recálculo em Python de todas as razões Si:O e (Si + Al IV):O, das cargas das sete unidades silicáticas e de 29 fórmulas-exemplo, da média de 2,5 vértices da cadeia dupla, das somas de forças de ligação (Si–O–Si, Si–O–Al, Al–O–Al), da geometria do tetraedro e dos ângulos de clivagem {110} a partir das celas do diopsídio e da tremolita
**Escopo:** as 36 alegações dos rodapés e as afirmações de risco do corpo: tetraedro SiO₄ (distâncias, ângulo, carga); segunda e terceira regras de Pauling aplicadas à polimerização; ângulo Si–O–Si; notação Qⁿ; as seis classes, suas unidades, cargas e razões; fórmulas e coordenações dos exemplos; Al tetraédrico × octaédrico; cátions de compensação; regra de Loewenstein; classificação com Al nos tetraedros; clivagem, hábito, densidade e série de Bowen; mapa Nickel-Strunz × módulos 33–36; parâmetros de Liebau. Questionário e baralho ainda não existiam.
**Veredito:** Requer correção (menor) → **correções aplicadas; estado final: Aprovado** (nenhum achado aberto)

## Resumo

🔴 0 erros · 🟠 0 imprecisões · 🟡 3 imprecisões menores · 🔵 0 sem fonte · ⚪ 0 controversos
Verificadas e corretas: 33 alegações dos rodapés (36 no total; ver o manifesto `.json`) e todas as contas.

As razões Si:O pedidas para cada subclasse (SiO₄⁴⁻, Si₂O₇⁶⁻, Si₃O₉⁶⁻ e Si₆O₁₈¹²⁻, SiO₃²⁻ ou Si₂O₆⁴⁻, Si₄O₁₁⁶⁻, Si₂O₅²⁻, SiO₂) foram todas recalculadas e conferem. Os três achados são generalizações que ficavam falsas como escritas.

**Contas conferidas (Python, 2026-10-06):**

| O quê | Resultado | Onde |
|---|---|---|
| O por Si = 4 − n/2, n = 0 a 4 | 4; 3,5; 3; 2,5; 2 | a02 |
| SiO₄; Si₂O₇; Si₃O₉; Si₆O₁₈; SiO₃; Si₂O₆; Si₄O₁₁; Si₂O₅; Si₄O₁₀; SiO₂ | cargas −4; −6; −6; −12; −2; −4; −6; −2; −4; 0 · razões 1:4; 2:7; 1:3; 1:3; 1:3; 1:3; 4:11; 2:5; 2:5; 1:2 | a01, a02, figura 2 |
| Cadeia dupla: (2 × 2 + 2 × 3)/4; O em Si₄O₁₁ = 6 não compartilhados + 5 pontes | 2,5; 11 | a02 |
| Cargas de 29 fórmulas (forsterita, zircão, piropo, cianita, titanita, hemimorfita, lawsonita, åkermanita, benitoíta, berilo, diopsídio, enstatita, jadeíta, wollastonita, tremolita, talco, pirofilita, caulinita, crisotila, muscovita, flogopita, quartzo, ortoclásio, albita, anortita, leucita, nefelina, epidoto, sodalita) | todas 0 | a02, a03, a05 |
| (Si + Al IV):O: muscovita, flogopita; ortoclásio, anortita, leucita, nefelina, sodalita | 2:5; 1:2 | a03, a05 |
| Forças no O ponte: Si–O–Si; Si–O–Al; Al–O–Al | 2; 1,75; 1,5 | a03 |
| (Al₃Si)O₈ | carga −3 | a03 |
| Aresta O–O = 1,61 × √(8/3); ângulo tetraédrico | 2,629 Å; 109,47° | a01, figura 1 |
| Ângulo {110} = 2·arctan(a·senβ/b): diopsídio (9,746; 8,899; 105,63°); tremolita (9,863; 18,048; 104,8°/104,95°) | 93,0°/87,0°; 55,7°/124,3° (55,6° com 104,95°) | a04, figura 3 |

> [!note] Limite da verificação nesta sessão
> Como nos módulos anteriores, o acesso direto a *Handbook of Mineralogy*, Mindat e RRUFF estava bloqueado pelo proxy; tudo foi conferido por busca. **Não conferido na fonte primária:** o β exato da tremolita no *Handbook of Mineralogy* (a busca deu a e b do HoM e β = 104,95° do Mindat; o ângulo de clivagem muda menos de 0,2° entre 104,8° e 104,95°); as densidades de talco, ortoclásio e albita (usadas como faixas arredondadas); o texto original de Liebau (1985), conferido por resumos que o citam.

## Achados

### 🟡 1. "O único cátion abundante que cabe no tetraedro"

**claim_id:** `CRQ-ALSI-CARGA-001`  ·  **Tipo:** confusão de escopo  ·  **Onde:** aula 03 · Uma carga a mais
**Está escrito:** "O Al³⁺ é o único cátion abundante que cabe bem no tetraedro além do Si⁴⁺."
**Problema:** o Fe³⁺, que é abundante, também ocupa tetraedros em alguns minerais (por exemplo, a tetraferriflogopita, KMg₃(Fe³⁺Si₃O₁₀)(OH,F)₂). "Único" é falso como escrito.
**Correção aplicada:** "O Al³⁺ é, de longe, o cátion que mais ocupa tetraedros no lugar do Si⁴⁺ (o Fe³⁺ também pode fazê-lo, mas em muito menos minerais, como certas micas ricas em ferro)."
**Fonte:** Mindat; Webmineral (tetraferriflogopita), por busca  ·  **Confiança:** confirmado

### 🟡 2. "O asbesto" e os sítios entre as vigas

**claim_id:** `CRQ-PROP-INO-001`  ·  **Onde:** aula 04 · Ino: cadeias, prismas e duas clivagens
**Problema:** "alguns anfibólios formam fibras, o asbesto" sugere que todo asbesto é anfibólio, quando a crisotila (uma serpentina, filossilicato) é outro asbesto; e, no anfibólio, além do M4, o sítio A também fica entre as vigas.
**Correção aplicada:** "alguns anfibólios crescem em fibras, que estão entre os minerais chamados de asbesto; a crisotila, uma serpentina, é outro deles"; "M2 no piroxênio; M4 e o sítio A no anfibólio".  ·  **Confiança:** confirmado (Klein & Dutrow)

### 🟡 3. Subdivisões de Nickel-Strunz incompletas

**claim_id:** `CRQ-MAPA-STRUNZ-001`  ·  **Onde:** aula 05 · O mapa
**Problema:** a lista 9.A–9.G foi dada como completa; a classe 9 tem também 9.H (silicatos não classificados) e 9.J (germanatos).
**Correção aplicada:** "além de 9.H (silicatos não classificados) e 9.J (germanatos, os análogos com germânio)".
**Fonte:** Mindat, *Strunz-mindat (2025) Classification*  ·  **Confiança:** confirmado

## Verificado e correto (seleção)

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `CRQ-SIL-TETRA-001` | Si–O ~1,61–1,62 Å; O–Si–O 109,5°; O–O ~2,63 Å; SiO₄ −4 | Shannon (1976); cálculo | confirmado |
| `CRQ-SIL-SIOSI-001` | Si–O–Si de ~120° a 180°; ~144° no quartzo | Gibbs et al.; busca | confirmado |
| `CRQ-SIL-QN-001` | Qⁿ = nº de O ponte; Engelhardt (1975), Lippmaa (1980) | busca | confirmado |
| `CRQ-POLIM-CLASSES-001` | unidades, cargas e razões das seis classes | cálculo; Klein & Dutrow | confirmado |
| `CRQ-ALSI-LOEW-001` | Loewenstein (1954), *Am. Mineral.* 39, 92–96; Al:Si ≤ 1 com alternância | busca | confirmado |
| `CRQ-ALSI-CLASSIF-001` | leucita, nefelina, anortita = tecto; jadeíta (Al VI) = ino | Mindat; Morimoto (1988) | confirmado |
| `CRQ-PROP-ANGULO-001` | {110} 93,0°/87,0° (diopsídio) e 55,7°/124,3° (tremolita) | cálculo; HoM; Mindat | confirmado |
| `CRQ-PROP-BOWEN-001` | série descontínua acompanha a polimerização; plagioclásio em paralelo | Britannica; Earle | confirmado |
| `CRQ-MAPA-LIEBAU-001` | dimensionalidade, multiplicidade, periodicidade (2, 3, 5) | Liebau (1985); *Mineral. Mag.*; LibreTexts | confirmado |
| `CRQ-MAPA-QUARTZO-001` | quartzo: tecto (Dana 75.1.3.1), óxido (Strunz 4.DA.05) | módulo 02, aula 05 | confirmado |

## Consistência interna e com o resto do curso

- **Módulo 01:** Si–O ~45% iônica, forte e direcional (aula 04); Si–O ≈ 1,62 Å (aula 06); talco com lâminas neutras e van der Waals, moscovita com K⁺, durezas 1 e 2–2,5, quartzo 7 (aulas 04 e 05) — reaproveitados sem mudança; a aula 04 daqui retoma explicitamente o "plano de ligação mais fraca" da aula 05 de lá.
- **Módulo 02:** abundâncias (O ~47% da massa; silicatos ~92%; feldspatos > 50%), titanita como nesossilicato e quartzo 4.DA.05 / Dana 75.1.3.1 — mesmos valores e mesma leitura.
- **Módulo 05/06:** cela do diopsídio (a = 9,746; b = 8,899; β = 105,63°) e densidade do quartzo 2,65 — idênticas.
- **Módulo 08:** raios de Shannon (Si IV 0,26; Al IV 0,39; Al VI 0,535), s = carga/NC, mesodésmico, só vértices (Si–Si 1,86/1,07/3,06 Å), taumasita, estishovita — idênticos.
- **Módulo 09:** Al↔Si com 50% de diferença de raio; vetor CaAlNa₋₁Si₋₁; regra de distribuição "Si, depois Al até completar T" (aula 05); sítios M1 e M2 do piroxênio — coerentes.
- **Módulo 10:** Al₂SiO₅ com metade do Al octaédrico; cianita como nesossilicato com O extra — coerentes com a aula 03 e o exemplo (e) da aula 02.
- **Módulos 33–36 (hubs):** os grupos da tabela da aula 05 são exatamente os planejados em cada hub; nenhuma espécie foi atribuída a um módulo diferente; nenhum conteúdo de sistemática foi antecipado além de fórmula, classe e propriedade-assinatura. A aula 04 cita os ângulos de clivagem de piroxênios e anfibólios, objetivo do módulo 34 (oa01, oa04), apenas como consequência da arquitetura, sem nomenclatura de sítios além de M2, M4 e A.

## Correções aplicadas

**Aplicadas em:** 2026-10-06

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `CRQ-ALSI-CARGA-001` | 🟡 | Corrigido | aula-03 |
| `CRQ-PROP-INO-001` | 🟡 | Corrigido | aula-04 |
| `CRQ-MAPA-STRUNZ-001` | 🟡 | Corrigido | aula-05 |

Também foram atualizados: os rodapés `alegacoes_auditaveis` das aulas (campo `audit:`), o hub do módulo e o `course-state.yaml` (bloco `audit` do 11).

**Pendências:** nenhuma. Não há questionário nem baralho a propagar (ainda não existiam).

## Segunda passagem (depois da revisão didática)

**Em:** 2026-10-06. A revisão didática acrescentou cinco trechos, conferidos aqui:

- **aula 01:** nota de que Q0–Q4 na figura equivalem a Q⁰–Q⁴ — notação, sem fato novo.
- **aula 02:** "topologia (quem está ligado a quem)" e "piroxenoide, isto é, um silicato de cadeia simples que não é piroxênio" — definições coerentes com o módulo 10 (aula 01) e com a aula 05 daqui (periodicidade 3 da wollastonita).
- **aula 03:** "o espaço entre as lâminas" no lugar de "intercamada" — mesma afirmação.
- **aula 04:** "o sítio A, muitas vezes vazio" — coerente com o módulo 09, aula 02 (sítio A do anfibólio normalmente vazio, que recebe Na no vetor da edenita; Hawthorne et al., 2012).

**Pendências:** nenhuma.

## Terceira passagem: checagem científica do questionário e do baralho

**Em:** 2026-10-06, antes de marcar o módulo como concluído.

**Questionário final (15 questões, 37 pontos).** Cada gabarito foi refeito contra as aulas corrigidas, e as contas foram recalculadas em Python: cargas de AlSi₃O₈ (−1) e Al₂Si₂O₈ (−2); cargas zero de almandina, åkermanita, enstatita, pirofilita e benitoíta; 2·arctan(9,5/27) = 38,8° (suplemento 141,2°). A matriz soma 7 + 9 + 9 + 12 = 37. Nenhum distrator é defensável como correto (na Q2, um anel de 4 teria Si₄O₁₂, não Si₄O₁₁; na Q5, a compensação do Al não exige K). **Dados fora das aulas**, declarados no registro de geração: as fórmulas de almandina, åkermanita e pirofilita, dadas no enunciado, e a cela **hipotética** de uma cadeia tripla na Q15 (a). Resultado: 0 🔴, 0 🟠.

**Baralho (57 Basic + 8 Cloze).** Cada card foi rastreado até a frase da aula de origem; as razões e cargas foram recalculadas antes de virar card; as três correções da auditoria aparecem só na versão corrigida. Cinco cards Basic que repetiam o fato de um Cloze foram retirados antes de receber ID definitivo. Resultado: 0 🔴, 0 🟠. `validate_flashcards.py`: 0 erros, 0 avisos.

**Pendências:** nenhuma.
