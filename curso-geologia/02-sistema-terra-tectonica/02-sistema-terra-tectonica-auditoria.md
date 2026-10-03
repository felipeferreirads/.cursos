# Auditoria científica — Módulo 02: Sistema Terra, estrutura interna e tectônica de placas

**Data:** 2026-08-16
**Modo:** `audit-and-fix` (dentro do fluxo do curso)
**Tipo:** **reauditoria** do texto reescrito na repartida do zero. A auditoria de 2026-08-15 valia para as 6 aulas antigas e está arquivada em `_arquivo-nivel-antigo/02-sistema-terra-tectonica-auditoria-nivel-antigo.md`.
**Escopo:** as 9 aulas reescritas, auditadas em conjunto, mais checagem cruzada contra os módulos 00, 01 e 03.
**Veredito:** ✅ **aprovado** — 0 🔴, 1 🟠 (corrigido), 0 🟡, 4 🔵 herdados (deferidos, não bloqueantes).

## Saldo por severidade

| Severidade | Contagem | Situação |
|---|---|---|
| 🔴 erro factual | 0 | — |
| 🟠 impreciso | 1 | corrigido |
| 🟡 desatualizado | 0 | — |
| 🔵 controverso | 4 | **herdados**; deferidos a M09, M10, M18, M19, M24 |
| ⚪ observação | 0 | — |

**Gate liberado:** sem 🔴 ou 🟠 em aberto, o questionário e o baralho de flashcards do módulo estão autorizados a ser reconciliados.

Base da auditoria: **60 alegações auditáveis** declaradas pelas próprias aulas (a01: 3 · a02: 6 · a03: 6 · a04: 7 · a05: 5 · a06: 7 · a07: 8 · a08: 8 · a09: 10) — o maior conjunto do curso até aqui.

## Achados

### 🟠 1. Espessura da crosta continental divergente entre aulas do próprio curso

**claim_id:** `GEO-M02-A04-ESPESSURA-CROSTA` · **finding_id:** `XC-F01` (achado transversal)
**Tipo:** `inconsistencia_interna`
**Onde:** `02-sistema-terra-tectonica-aula-04-modelo-em-camadas.md` — lista de profundidades da Moho
**Estava escrito:** "Sob os continentes: **algumas dezenas de quilômetros** — da ordem de 30 a 40 km."
**Problema:** a **aula 02 deste mesmo módulo** dizia "da ordem de 30 a 50 km", e o M01-a05 também. Duas aulas do módulo 02 se contradiziam entre si — exatamente a classe de defeito que a prática de auditar as aulas **em conjunto** existe para pegar, e a segunda vez que ela pega algo assim neste módulo (a primeira foi `M02-F01`, sobre a taxa de espalhamento). O USGS sustenta 30–50 km para regiões continentais estáveis.
**Correção aplicada:** "da ordem de 30 a 50 km". A linha seguinte, sobre orógenos passando de 60 km, ficou intacta e continua coerente.
**Fonte:** USGS · **Nível:** normativa
**Confiança:** confirmado
**Também aparecia em:** `00-partida-do-zero-aula-04-terra-por-dentro.md` (corrigido no mesmo passe)
**Desfecho:** ✅ corrigido

## Achados herdados (🔵 deferidos)

Os quatro são controvérsias reais de literatura, concentradas no motor da tectônica e no manto profundo. Nesta rodada verificou-se que **as aulas reescritas tratam todas as quatro como questão em aberto**, em uma frase, conforme a regra LC-08 — o que era o comportamento exigido. Nenhuma precisou de edição.

| finding_id | Questão | Como o texto trata | Retomar em |
|---|---|---|---|
| 🔵 `M02-F04` | Geometria da convecção do manto: camada única × estratificada em 660 km | `a09` declara explicitamente o debate | M18, M19 |
| 🔵 `M02-F05` | Origem das plumas mantélicas e fixidez dos pontos quentes | `a08` (Islândia) e `a09` declaram o debate | M10, M18, M24 |
| 🔵 `M02-F06` | Balanço quantitativo entre slab pull, ridge push e basal drag | `a09` dá o slab pull como "geralmente considerado" o maior, sem fechar o balanço | M18, M19 |
| 🔵 `M02-F07` | Natureza das LLSVPs e elementos leves do núcleo externo | `a03`, `a04` e `a09` declaram o debate | M09, M19 |

Sobre `M02-F07`, uma nota de consistência: `a03` e `a04` afirmam, com formulações diferentes mas equivalentes, que o núcleo é menos denso que ferro puro nas condições esperadas, implicando elementos leves de identidade debatida. **O M00-a04 foi conferido contra as duas e não fecha a questão** — diz apenas "ferro, com níquel e uma parcela de elementos mais leves". Consistente.

## Verificado e correto

| claim_id | O que foi verificado | Resultado |
|---|---|---|
| `GEO-M02-A02-PERFURACAO` | Perfuração mais profunda >12 km, menos de 0,2% do raio — **conferido contra M00-a04**; 12,26/6.371 = 0,19% | consistente e aritmeticamente correto ✔ |
| `GEO-M02-A02-ESPESSURAS` | Crosta oceânica ~5-10 km, continental ~30-50 km | confirmado ✔ — foi a **referência que resolveu `XC-F01`** |
| `GEO-M02-A03-ZONA-SOMBRA` | Zona de sombra das ondas P entre ~105° e ~140° de distância epicentral | confirmado ✔ |
| `GEO-M02-A04-MANTO-VOLUME` | Manto como mais de 80% do volume da Terra (valor de referência ~84%) | confirmado ✔ — **consistente com o "maior parte do volume" de M00-a04** |
| `GEO-M02-A04-CROSTA-OCEANICA-7KM` | Crosta oceânica da ordem de 7 km | confirmado ✔ — dentro da faixa 5-10 km usada nas demais aulas |
| `GEO-M02-A04-IDADE-CROSTA` | Crosta oceânica não passa de ~200 Ma; continental atinge bilhões — **conferida contra M01-a05 e M02-a07** | os três consistentes ✔ |
| `GEO-M02-A05-LITOSFERA` | Litosfera continental da ordem de 100 km, "bem mais que isso sob os núcleos continentais antigos" | confirmado ✔ — a ressalva cobre os crátons, cuja litosfera passa de 200 km |
| `GEO-M02-A06-PANGEIA` | Pangeia reunida há cerca de 250 Ma, denominação de Wegener | confirmado ✔ |
| `GEO-M02-A07-SIMETRIA-IDADES` | Idade da crosta oceânica cresce simetricamente a partir da cadeia meso-oceânica | confirmado ✔ |
| `GEO-M02-A07-TAXAS` | Taxas de expansão da ordem de centímetros por ano | confirmado ✔ — **a adoção de ordem de grandeza aqui é o que fechou definitivamente o antigo achado `M02-F01`** |
| `GEO-M02-A07-INVERSOES` | Campo magnético inverte em intervalos irregulares, de dezenas de milhares a milhões de anos | confirmado ✔ |
| `GEO-M02-A01-*` | Aula-ponte de ondas: propagação, reflexão, refração, mudança de meio | confirmado ✔ — sem conteúdo geológico a auditar |

## Nota sobre o achado `M02-F01` (auditoria anterior)

O achado que a auditoria de 2026-08-15 corrigiu — taxa de espalhamento da Elevação do Pacífico Leste inconsistente entre duas aulas — **não pode mais reaparecer**: a repartida substituiu o valor pontual por ordem de grandeza (regra LC-05), o que elimina a classe de erro em vez de corrigir a instância. Registrado como fechado em definitivo.

## Correções aplicadas

**Aplicadas em:** 2026-08-16

| claim_id / finding | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `XC-F01` / `GEO-M02-A04-ESPESSURA-CROSTA` | 🟠 | Corrigido | `02-sistema-terra-tectonica-aula-04-modelo-em-camadas.md` |
| `M02-F04` | 🔵 | Mantido deferido (M18, M19) | — |
| `M02-F05` | 🔵 | Mantido deferido (M10, M18, M24) | — |
| `M02-F06` | 🔵 | Mantido deferido (M18, M19) | — |
| `M02-F07` | 🔵 | Mantido deferido (M09, M19) | — |
| `M02-F01` | 🟠 | Fechado em definitivo pela regra LC-05 | — |

**Propagação:** o questionário e os três arquivos de baralho foram varridos em busca de item que cobrasse a espessura da crosta continental. Um item cobra o valor diretamente:

| Item | Onde | Diz | Situação |
|---|---|---|---|
| `geologia-m02-fb013` | `02-sistema-terra-tectonica-flashcards-basic.csv` | "Crosta continental típica: 30–50 km, chegando a ~70 km sob cinturões orogênicos" | ✅ **já correto** — nenhuma edição necessária |
| `geologia-m02-fb011` / `geologia-m02-fc007` | basic e cloze | crosta oceânica "~7 km (faixa 5–10 km)" | ✅ já correto |

O baralho havia sido gerado a partir da aula 02, que estava do lado certo da divergência. **Nenhum arquivo derivado precisou de edição por causa de `XC-F01`** — a inconsistência vivia só entre duas aulas, e o material derivado nunca a herdou. O `needs_review` do questionário e do baralho permanece por motivo **curricular** (magnitude sísmica e anomalias magnéticas deferidas ao M19; vulcanologia ao M10), não factual.

**Pendências:** os quatro 🔵 herdados, todos com módulo de destino definido.
