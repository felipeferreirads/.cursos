# Auditoria científica — Módulo 01: Fundamentos e método das geociências

**Data:** 2026-08-16
**Modo:** `audit-and-fix` (dentro do fluxo do curso)
**Tipo:** **reauditoria** do texto reescrito na repartida do zero. A auditoria de 2026-07-21 valia para as 4 aulas antigas e está arquivada em `_arquivo-nivel-antigo/01-fundamentos-e-metodo-auditoria-nivel-antigo.md`.
**Escopo:** as 6 aulas reescritas, auditadas em conjunto, mais checagem cruzada contra os módulos 00, 02 e 03.
**Veredito:** ✅ **aprovado** — 0 🔴, 0 🟠, 0 🟡, 0 🔵 novos, 3 🔵 herdados (deferidos, não bloqueantes).

## Saldo por severidade

| Severidade | Contagem | Situação |
|---|---|---|
| 🔴 erro factual | 0 | — |
| 🟠 impreciso | 0 | — |
| 🟡 desatualizado | 0 | — |
| 🔵 sem fonte / controverso | 3 | **herdados** da auditoria anterior; deferidos a módulos posteriores |
| ⚪ observação | 1 | observação estrutural, não factual |

**Gate liberado:** sem 🔴 ou 🟠 em aberto, o questionário e o baralho de flashcards do módulo estão autorizados a ser reconciliados.

Base da auditoria: **31 alegações auditáveis** declaradas pelas próprias aulas (a01: 4 · a02: 5 · a03: 3 · a04: 7 · a05: 6 · a06: 6), mais verificação de consistência numérica contra os módulos 00, 02 e 03.

## Por que a reauditoria não achou nada novo

Vale registrar, porque é um resultado e não uma omissão. Três razões:

1. **A regra LC-05 eliminou uma classe inteira de achado.** Ao trocar precisão de laboratório por ordem de grandeza, o texto deixou de afirmar valores que envelhecem. Foi exatamente o mecanismo previsto quando a regra foi adotada.
2. **O conteúdo mais arriscado foi deferido.** A regra de Goldschmidt saiu para o M09 e a isócrona de Patterson para o M03. Eram os pontos de maior densidade factual da versão antiga.
3. **O único achado 🟠 do módulo nesta rodada nasceu fora dele** — a divergência de espessura da crosta continental (`XC-F01`), em que **este módulo estava do lado correto** (30 a 50 km) e os módulos 00 e 02 é que foram harmonizados com ele.

## Achados herdados (🔵 deferidos)

Nenhum é defeito do texto: são controvérsias reais de literatura, tratadas no material como questão em aberto conforme a regra LC-08. Permanecem abertos por decisão de projeto, para serem retomados onde o nível permita arbitrá-los.

### 🔵 M01-F02 — Qual é a rocha mais antiga preservada

**Situação:** disputa entre o gnaisse de Acasta (Canadá) e a faixa de Nuvvuagittuq (Quebec), esta última com idade dependente do sistema isotópico adotado.
**Como o texto trata:** a aula 04 dá o gnaisse de Acasta em ~4,0 Ga sem declarar primazia absoluta. O M00-a03 e o M03-a05 usam ordem de grandeza pelo mesmo motivo. **Nenhuma das três aulas arbitra a disputa** — verificado nesta rodada.
**Retomar em:** M03 (feito — o M03-a05 declara explicitamente a disputa) e **M25** (crátons).
**Desfecho:** ✅ mantido deferido

### 🔵 M01-F03 — Origem da Lua por impacto gigante

**Situação:** o modelo de impacto gigante é dominante, mas os parâmetros do impactor e a assinatura isotópica seguem em debate.
**Como o texto trata:** a aula 04 apresenta como "modelo dominante, com parâmetros em debate". Correto sob LC-08.
**Retomar em:** **M24** (geologia planetária).
**Desfecho:** ✅ mantido deferido

### 🔵 M01-F04 — Precisão de espessura crustal e do limite manto-núcleo

**Situação:** o achado original apontava faixas de referência tratadas como valores fechados.
**Avaliação nesta rodada:** **neutralizado no nível iniciante pela regra LC-05.** O texto reescrito usa faixas e ordens de grandeza. A precisão plena segue deferida ao **M19**.
**Nota:** a harmonização de `XC-F01` reforçou este ponto — as quatro aulas do curso que citam espessura crustal agora dizem a mesma coisa.
**Desfecho:** ✅ mantido deferido, com escopo reduzido

## Verificado e correto

| claim_id | O que foi verificado | Resultado |
|---|---|---|
| `GEO-M01-A01-DEF-MINERAL-001` | Definição de mineral — **conferida contra `GEO-M00-A01-DEF-MINERAL-001`** | consistente ✔ |
| `GEO-M01-A01-GEM-NAOMINERAL-002` | Âmbar, pérola, coral, obsidiana — **enunciado idêntico ao de M00-a01** | consistente ✔ |
| `GEO-M01-A01-NUCLEO-EXT-004` | Núcleo externo líquido — **conferido contra M00-a04 e M02-a03/a04** | consistente ✔ |
| `GEO-M01-A02-GOE` | Aumento do oxigênio livre a partir de ~2,4 Ga, não instantâneo | confirmado ✔ |
| `GEO-M01-A03-*` | Princípios de Steno e relações de corte — **conferidos contra M00-a05 e M03-a01** | os três consistentes ✔ |
| `GEO-M01-A04-IDADE-TERRA` | 4,54 Ga — **conferida contra M00-a03, M03-a04, M03-a05** | os quatro consistentes ✔ |
| `GEO-M01-A04-CAI` | Sólidos mais antigos do sistema solar ~4,57 Ga (CAIs) | confirmado ✔ |
| `GEO-M01-A04-JACKHILLS` | Zircões de Jack Hills ~4,4 Ga, materiais terrestres mais antigos conhecidos | confirmado ✔ |
| `GEO-M01-A04-ACASTA` | Gnaisse de Acasta ~4,0 Ga | confirmado ✔ (ver M01-F02) |
| `GEO-M01-A05-ESPESSURAS` | Crosta oceânica ~5-10 km, continental ~30-50 km | confirmado ✔ — **este módulo é a referência que resolveu `XC-F01`** |
| `GEO-M01-A05-CMB` | Limite manto-núcleo ~2.900 km — **conferido contra M00-a04 e M02-a04** | consistente ✔ |
| `GEO-M01-A05-LITOSFERA-OCEANICA` | Litosfera oceânica engrossa com a idade até ~100 km | confirmado ✔ |
| `GEO-M01-A05-IDADE-CROSTA-OCEANICA` | Crosta oceânica raramente passa de ~200 Ma — **conferida contra M02-a04 e M02-a07** | os três consistentes ✔ |
| `GEO-M01-A06-PRECAMBRIANO` | "Mais de 80% do tempo geológico" — **conferido contra o "cerca de 88%" de M03-a06 e M03-a07** | consistente ✔ (88 > 80; enunciados compatíveis) |
| `GEO-M01-A04-VELOCIDADE-PLACA-006` | 5 cm/ano → 5.000 km em 100 Ma | recalculado ✔ — **idêntico ao exemplo (a) de M00-a03** |
| `GEO-M01-A04-DENUDACAO-007` | 0,1 mm/ano → 10 km em 10⁸ anos | recalculado ✔ |
| `GEO-M01-A06-CALENDARIO` | Tabela do ano-calendário comprimido | recurso didático, arredondamento declarado ✔ |

## Observação estrutural (fora do escopo factual)

⚪ Três alegações do arquivo da **aula 06** carregam prefixo `GEO-M01-A04-` (`VELOCIDADE-PLACA-006`, `DENUDACAO-007`, e a de calendário). O conteúdo está correto; o **prefixo do `claim_id` não corresponde ao arquivo em que a alegação vive**. Isso não é erro factual e não foi alterado — `claim_id` não deve ser reciclado nem renumerado, por ser âncora de histórico. Fica registrado para que uma busca futura por "alegações da aula 06" não os perca.

## Correções aplicadas

**Aplicadas em:** 2026-08-16

| claim_id / finding | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| — | — | Nenhuma correção necessária neste módulo | — |
| `M01-F02` | 🔵 | Mantido deferido (M03 ✔, M25 pendente) | — |
| `M01-F03` | 🔵 | Mantido deferido (M24) | — |
| `M01-F04` | 🔵 | Mantido deferido (M19), escopo reduzido por LC-05 | — |

**Propagação:** nenhuma correção de texto, portanto nenhuma propagação factual. O questionário e o baralho seguem marcados `needs_review` por motivo **curricular**, não factual — itens ancorados em conteúdo deferido ao M09. Ver o registro de reconciliação.

**Pendências:** os três 🔵 herdados, todos com módulo de destino definido.

## Passagem de verificação — incorporação de achado (2026-08-19, modo `audit`)

Após a incorporação do achado de lacunas de transcrição (atribuição histórica Hutton/Lyell na aula 02), verificados os 3 claims novos contra fonte normativa. Não houve reabertura da auditoria acima; os achados anteriores seguem válidos.

- `GEO-M01-A02-HUTTON-008` — confirmado (Encyclopedia Britannica; USGS *History of Geology*).
- `GEO-M01-A02-LYELL-1830-009` — confirmado (Encyclopedia Britannica; USGS *History of Geology*).
- `GEO-M01-A02-LYELL-GRADUALISMO-010` — confirmado (distinção clássica entre uniformitarismo metodológico e substantivo; Gould 1965, *Is uniformitarianism necessary?*, *American Journal of Science*).

**Veredito:** dentro do escopo já auditado, sem novo achado. `pending_reaudit` (registrado apenas no rodapé da aula, não em `course-state.yaml`) encerrado.
