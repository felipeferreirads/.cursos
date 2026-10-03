# Auditoria científica — Módulo 03: Tempo geológico e geocronologia

**Data:** 2026-08-16
**Modo:** `audit-and-fix` (dentro do fluxo do curso)
**Tipo:** **reauditoria** do texto reescrito na repartida do zero. A auditoria anterior valia para as 5 aulas antigas e está arquivada em `_arquivo-nivel-antigo/03-tempo-geologico-geocronologia-auditoria-nivel-antigo.md`.
**Escopo:** as 7 aulas reescritas, auditadas em conjunto, mais checagem cruzada contra os módulos 00, 01 e 02.
**Veredito:** ✅ **aprovado** — 0 🔴, 2 🟠 (corrigidos), 0 🟡, 2 🔵 (resolvidos), 1 🔵 herdado (deferido).

## Saldo por severidade

| Severidade | Contagem | Situação |
|---|---|---|
| 🔴 erro factual | 0 | — |
| 🟠 impreciso | 2 | ambos corrigidos |
| 🟡 desatualizado | 0 | — |
| 🔵 sem fonte | 2 | resolvidos na própria auditoria (versão da carta ICS declarada) |
| 🔵 controverso herdado | 1 | `M03-F02`, mantido deferido |
| ⚪ observação | 0 | — |

**Gate liberado:** sem 🔴 ou 🟠 em aberto, o questionário e o baralho de flashcards do módulo estão autorizados a ser reconciliados.

Base da auditoria: **52 alegações auditáveis** declaradas pelas próprias aulas (a01: 5 · a02: 5 · a03: 8 · a04: 8 · a05: 9 · a06: 10 · a07: 7). Este é o módulo com maior densidade numérica do curso, e foi auditado com a carta da ICS aberta ao lado.

## Achados

### 🟠 1. Régua de 100 metros posiciona as primeiras florestas no metro errado

**claim_id:** `GEO-M03-A07-REGUA-004` · **finding_id:** `M03-F03`
**Tipo:** `erro_factual` (aritmético, dentro de recurso didático)
**Onde:** `03-tempo-geologico-geocronologia-aula-07-tempo-rocha-e-magnitude.md` — tabela do corredor de 100 m
**Estava escrito:** "| metro ~94 | primeiras florestas |"
**Problema:** na régua declarada pela própria aula (100 m = 4,54 Ga, logo 1 m ≈ 45,4 Ma), o metro 94 corresponde a cerca de **272 Ma** — Permiano, não Devoniano. As primeiras florestas são do Devoniano Médio, com idade de referência de ~385 Ma (Gilboa, estado de Nova York), o que cai no **metro ~91,5**. O erro era interno: a linha contradizia a régua definida três parágrafos acima, e ficava fora de ordem em relação à linha seguinte (metro ~94,5 para a extinção do fim do Paleozoico, 252 Ma).
**Correção aplicada:** "| metro ~91,5 | primeiras florestas |"
**Fonte:** literatura sobre as florestas devonianas de Gilboa (~385 Ma) + cálculo aritmético sobre a régua declarada · **Nível:** revisada por pares
**Confiança:** confirmado
**Verificação adicional:** **todas as outras nove linhas da tabela foram recalculadas uma a uma** e estão corretas — metro ~12 (rochas mais antigas, 4,0 Ga → 11,9), metro 88 (base do Cambriano, 538,8 Ma → 88,1), metro ~94,5 (extinção do fim do Paleozoico, 251,9 Ma → 94,4), metro ~98,5 (K-Pg, 66,0 Ma → 98,5), últimos 7 cm (*Homo*, ~3 Ma → 6,6 cm), último milímetro (~45 ka).
**Desfecho:** ✅ corrigido

### 🟠 2. Duração do período Jurássico subestimada

**claim_id:** `GEO-M03-A07-DURACAO-JURASSICO-006` · **finding_id:** `M03-F04`
**Tipo:** `erro_factual`
**Onde:** `03-tempo-geologico-geocronologia-aula-07-tempo-rocha-e-magnitude.md` — frase de abertura da seção "Duas coisas com o mesmo nome"
**Estava escrito:** *"O Jurássico durou cerca de 55 milhões de anos."*
**Problema:** pela carta da ICS, o Jurássico vai de **201,4 Ma a 143,1 Ma**, o que dá **58,3 milhões de anos**. "Cerca de 55" erra por mais de 3 Ma e, o que é pior no nível iniciante, **arredonda para o lado errado**: sugere um período mais curto que o Devoniano, quando os dois são praticamente iguais em duração — e a mesma aula usa o Devoniano com "cerca de 60" no exemplo trabalhado. O aluno atento veria uma diferença que não existe.
**Correção aplicada:** *"O Jurássico durou quase 60 milhões de anos."*
**Fonte:** ICS, carta cronoestratigráfica internacional **v2024/12** · **Nível:** normativa
**Confiança:** confirmado
**Verificação adicional:** a duração do Devoniano citada no exemplo trabalhado ("cerca de 60 milhões de anos") foi conferida — 419,2 a 358,9 Ma = 60,3 Ma. **Correta**, mantida.
**Desfecho:** ✅ corrigido

### 🔵 3 e 4. Versão da carta ICS não declarada

**claim_id:** `GEO-M03-A06-BASE-FANEROZOICO-004`, `GEO-M03-A06-ERAS-006`, `GEO-M03-A07-DURACAO-JURASSICO-006` · **finding_id:** `M03-F05`
**Tipo:** `evidencia_insuficiente`
**Onde:** blocos de alegações das aulas 06 e 07 — três marcadores `CITAR VERSÃO`
**Resolução:** todos os valores foram conferidos contra a **carta ICS v2024/12** e a versão foi registrada nos blocos:

| Valor na aula | Carta ICS v2024/12 | Situação |
|---|---|---|
| Base do Fanerozoico "por volta de 540 Ma" | 538,8 ± 0,6 Ma (GSSP de Fortune Head, Terra Nova, primeira ocorrência de *Trichophycus pedum*) | ✔ correto em ordem de grandeza |
| Paleozoico ~540 a ~250 Ma | 538,8 a 251,9 Ma | ✔ correto |
| Mesozoico ~250 a ~66 Ma | 251,9 a 66,0 Ma | ✔ correto |
| Cenozoico ~66 Ma ao presente | 66,0 Ma | ✔ correto |
| Duração do Jurássico | 201,4 a 143,1 Ma | ✗ — ver achado 2 |

**Desfecho:** ✅ resolvido — nenhum valor além do Jurássico precisou mudar; versão da fonte agora registrada

## Achado herdado (🔵 deferido)

### 🔵 `M03-F02`

Mantido conforme registrado no relatório anterior e em `_contexto.md`. Não é defeito do texto reescrito.
**Desfecho:** ✅ mantido deferido

## Verificado e correto

| claim_id | O que foi verificado | Resultado |
|---|---|---|
| `GEO-M03-A04-MEIAS-VIDAS` | C-14 ~5,7 ka · U-235 ~700 Ma · K-40 ~1,25 Ga · U-238 ~4,5 Ga · Rb-87 ~49 Ga | **todas as cinco confirmadas** ✔ (valores de referência 5.700 a · 703,8 Ma · 1,248 Ga · 4,468 Ga · 49,6 Ga) |
| `GEO-M03-A04-FRACOES` | 50% · 25% · 12,5% · 6,25% · 3,125% após 1 a 5 meias-vidas | recalculado ✔ |
| `GEO-M03-A04-IDADE-TERRA` / `A05` | 4,54 Ga — **conferida contra M00-a03 e M01-a04** | os quatro consistentes ✔ |
| `GEO-M03-A05-ROCHA-MAIS-ANTIGA` | Disputa declarada explicitamente | ✔ — **atende ao deferimento de `M01-F02` para este módulo** |
| `GEO-M03-A06-PROPORCAO-PRECAMBRIANO-005` | 88% do tempo geológico | recalculado ✔ — (4.540 − 538,8)/4.540 = 88,1%; **consistente com "mais de 80%" de M01-a06** |
| `GEO-M03-A06-KPG-REVISAO` | Idade do limite K-Pg revisada de ~65 para ~66 Ma **sem redefinição do GSSP** | confirmado ✔ — é justamente o exemplo que sustenta a distinção GSSP × idade numérica |
| `GEO-M03-A06-GSSP-DEF-007` | GSSP define o limite por ponto físico, independente da estimativa numérica | ICS ✔ |
| `GEO-M03-A06-GSSA-008` | Fronteiras do Pré-cambriano definidas por idade acordada (GSSA), não por seção | ICS ✔ |
| `GEO-M03-A07-DUPLA-HIERARQUIA-001` | Éon/eonotema, era/eratema, período/sistema, época/série, idade/andar | ICS ✔ |
| `GEO-M03-A07-ADJETIVOS-002` | Inferior/superior para rocha; antigo/recente para tempo | convenção estratigráfica ✔ |
| `GEO-M03-A01-*` | Princípios de datação relativa — **conferidos contra M00-a05 e M01-a03** | os três consistentes ✔ |
| `GEO-M03-A03-*` | Aula-ponte de átomos e isótopos: próton, nêutron, número atômico, isótopo, decaimento | confirmado ✔ |

## Correções aplicadas

**Aplicadas em:** 2026-08-16

| claim_id / finding | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `M03-F03` / `GEO-M03-A07-REGUA-004` | 🟠 | Corrigido | `03-tempo-geologico-geocronologia-aula-07-tempo-rocha-e-magnitude.md` |
| `M03-F04` / `GEO-M03-A07-DURACAO-JURASSICO-006` | 🟠 | Corrigido | `03-tempo-geologico-geocronologia-aula-07-tempo-rocha-e-magnitude.md` |
| `M03-F05` / `GEO-M03-A06-*` | 🔵 | Resolvido (versão da carta declarada) | `03-tempo-geologico-geocronologia-aula-06-escala-do-tempo-e-gssp.md`, `...-aula-07-...md` |
| `M03-F02` | 🔵 | Mantido deferido | — |

**Propagação:** o questionário e os três arquivos de baralho foram varridos em busca dos dois fatos corrigidos.

- **Duração do Jurássico:** o único item que menciona o Jurássico é `geologia-m03-fb037` (basic e índice `.md`), que cobra a distinção sistema × período — **não cobra duração**. Nenhuma edição necessária.
- **Primeiras florestas / régua de 100 m:** **nenhum item** do questionário ou do baralho menciona florestas ou a régua. Nenhuma edição necessária.

O `needs_review` do questionário e do baralho permanece por motivo **curricular** (itens de cálculo de isócrona excedem o nível do módulo; cards de concórdia/discórdia migram para o M09), não factual.

**Pendências:** `M03-F02`, mantido deferido.
