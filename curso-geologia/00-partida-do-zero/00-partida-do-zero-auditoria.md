# Auditoria científica — Módulo 00: Partida do zero

**Data:** 2026-08-16
**Modo:** `audit-and-fix` (dentro do fluxo do curso)
**Escopo:** as 6 aulas do módulo, auditadas em conjunto, mais checagem cruzada contra os módulos 01, 02 e 03.
**Veredito:** ✅ **aprovado** — 0 🔴, 2 🟠 (corrigidos), 0 🟡, 2 🔵 (resolvidos na própria auditoria), 1 ⚪.

Auditoria de primeira passagem: o módulo foi criado em 2026-08-16 na repartida do zero e nunca havia sido auditado.

## Saldo por severidade

| Severidade       | Contagem | Situação                                        |
| ---------------- | -------- | ----------------------------------------------- |
| 🔴 erro factual  | 0        | —                                               |
| 🟠 impreciso     | 2        | ambos corrigidos                                |
| 🟡 desatualizado | 0        | —                                               |
| 🔵 sem fonte     | 2        | ambos resolvidos com fonte na própria auditoria |
| ⚪ controverso    | 1        | tratado no texto como questão em aberto (LC-08) |

**Gate liberado:** sem 🔴 ou 🟠 em aberto, o questionário e o baralho de flashcards do módulo estão autorizados.

Base da auditoria: **46 alegações auditáveis** declaradas pelas próprias aulas (a01: 8 · a02: 7 · a03: 8 · a04: 9 · a05: 9 · a06: 5), mais a verificação de consistência numérica contra os módulos 01, 02 e 03.

## Achados

### 🟠 1. Espessura da crosta continental divergente entre módulos

**claim_id:** `GEO-M00-A04-ESPESSURAS-002` · **finding_id:** `XC-F01` (achado transversal)
**Tipo:** `inconsistencia_interna`
**Onde:** `00-partida-do-zero-aula-04-terra-por-dentro.md` — tabela de espessuras e recap
**Estava escrito:** "Crosta continental | ~30 a 40 km (mais sob montanhas)"
**Problema:** o mesmo fato aparece como **30 a 50 km** em `01-fundamentos-e-metodo-aula-05` e em `02-sistema-terra-tectonica-aula-02`, e como **30 a 40 km** aqui e em `02-sistema-terra-tectonica-aula-04`. Duas aulas do curso contradiziam as outras duas. O USGS dá 30–50 km para regiões continentais estáveis, e a compilação de Mooney registra mais de 90% das determinações entre 24 e 56 km — ou seja, a faixa mais larga é a sustentada.
**Correção aplicada:** "~30 a 50 km (mais sob montanhas)", na tabela e no recap.
**Fonte:** USGS, *This Dynamic Earth* e compilações de espessura crustal · **Nível:** normativa
**Confiança:** confirmado
**Também aparecia em:** `02-sistema-terra-tectonica-aula-04-modelo-em-camadas.md` (corrigido no mesmo passe)
**Desfecho:** ✅ corrigido

### 🟠 2. Régua de tempo: espessura atribuída à história escrita

**claim_id:** `GEO-M00-A03-REGUA-006` · **finding_id:** `M00-F01`
**Tipo:** `erro_factual` (aritmético, em recurso didático)
**Onde:** `00-partida-do-zero-aula-03-ordens-de-grandeza.md` — bloco da régua de 4,54 m
**Estava escrito:** "Toda a história escrita cabe em **três milésimos de milímetro**"
**Problema:** na régua declarada pela própria aula, 1 mm = 1 Ma. Três milésimos de milímetro correspondem, portanto, a 3.000 anos. A história escrita é convencionalmente contada a partir de cerca de 5.000 anos atrás, o que dá 0,005 mm.
**Correção aplicada:** "cinco milésimos de milímetro".
**Fonte:** cálculo aritmético direto sobre a régua declarada no próprio texto · **Nível:** verificável pelo leitor
**Confiança:** confirmado
**Desfecho:** ✅ corrigido

### 🔵 3. Referência de Chamberlin incompleta

**claim_id:** `GEO-M00-A06-CHAMBERLIN-003` · **finding_id:** `M00-F02`
**Tipo:** `evidencia_insuficiente` (fonte declarada como pendente pelo próprio autor)
**Onde:** `00-partida-do-zero-aula-06-observar-descrever-inferir.md` — bloco de alegações e seção Fontes
**Estava escrito:** o bloco trazia o marcador `CONFERIR referência completa na auditoria`.
**Resolução:** referência confirmada e completada — Chamberlin, T. C., "The Method of Multiple Working Hypotheses", *Science*, ns-15(366), p. 92–96, 7 de fevereiro de 1890, DOI 10.1126/science.ns-15.366.92; reeditado no *Journal of Geology*, v. 5, p. 837–848, 1897. A atribuição feita pela aula (autoria, ano e conteúdo do argumento) estava correta.
**Fonte:** Science / AAAS · **Nível:** revisada por pares
**Confiança:** confirmado
**Desfecho:** ✅ resolvido — placeholder removido, referência completa no texto e no bloco

### 🔵 4. Versão da carta ICS não declarada

**claim_id:** `GEO-M00-A03-MARCOS-004` · **finding_id:** `M00-F03`
**Tipo:** `evidencia_insuficiente` (versão de fonte normativa ausente)
**Onde:** `00-partida-do-zero-aula-03-ordens-de-grandeza.md` — bloco de alegações
**Estava escrito:** o bloco trazia o marcador `CONFERIR VERSÃO DA CARTA na reauditoria`.
**Resolução:** valores conferidos contra a **carta cronoestratigráfica internacional da ICS, versão 2024/12**. Base do Cambriano: 538,8 ± 0,6 Ma (a aula usa ~539 Ma) ✔. Limite K-Pg: 66,0 Ma (a aula usa ~66 Ma) ✔. Rochas mais antigas preservadas ~4,0 Ga ✔, mantido em ordem de grandeza por causa do achado aberto M01-F02. Máximo da última glaciação ~20 ka ✔. **Nenhum valor precisou mudar.**
**Fonte:** ICS — stratigraphy.org, carta v2024/12 · **Nível:** normativa
**Confiança:** confirmado
**Desfecho:** ✅ resolvido — versão registrada no bloco

### ⚪ 5. Limite de idade para o uso do termo "fóssil"

**claim_id:** `GEO-M00-A01-FOSSIL-IDADE-008` · **finding_id:** `M00-F04`
**Tipo:** `controversia`
**Onde:** `00-partida-do-zero-aula-01-nomes-no-lugar.md` — seção "Fóssil"
**Situação:** não existe norma formal fixando uma idade mínima para que um resto seja chamado de fóssil. Circulam o limite do Holoceno (~11,7 ka) e o valor de conveniência de 10 ka, e boa parte da literatura simplesmente não fixa limite.
**Avaliação:** **a aula já trata isso corretamente.** Ela diz "alguns milhares de anos", qualifica como convenção, declara que a linha é "convencional e um pouco frouxa" e defere a discussão. É exatamente o comportamento exigido pela regra LC-08.
**Desfecho:** ✅ aceito como está — nenhuma edição necessária

## Verificado e correto

Alegações conferidas contra fonte que **passaram sem alteração** — registradas para que uma auditoria futura saiba o que já foi olhado:

| claim_id | O que foi verificado | Fonte |
|---|---|---|
| `GEO-M00-A01-DEF-MINERAL-001` | Os quatro critérios de espécie mineral, e a ressalva de que há casos de fronteira e revisão por comissão | IMA-CNMNC |
| `GEO-M00-A01-OBSIDIANA-004` | Obsidiana como vidro vulcânico, não mineral, classificada como rocha | IUGS |
| `GEO-M00-A02-*` (7 alegações) | Três famílias por origem; relação granulação × taxa de resfriamento; três vias sedimentares; pares protólito-produto; foliação × acamamento | IUGS; petrologia padrão |
| `GEO-M00-A03-NOTACAO-001` | Regras de potência de dez e notação científica | aritmética, verificável |
| `GEO-M00-A03-IDADE-TERRA-003` | 4,54 Ga — **consistente com M01-a04, M03-a04 e M03-a05** | datação de meteoritos |
| `GEO-M00-A03-SEGUNDOS-005` | 10⁶ s = 11,6 dias; 10⁹ s = 31,7 anos | cálculo direto, refeito |
| `GEO-M00-A03-ESCALA-GRAO-007` | Limite areia/silte em ~0,06 mm | escala de Wentworth (1/16 mm = 0,0625) |
| `GEO-M00-A03-BILHAO-AMBIGUO-008` | Escala curta × escala longa para "bilhão" | uso corrente e histórico |
| `GEO-M00-A04-RAIO-001` | Raio ~6.400 km (referência 6.371 km), em ordem de grandeza por LC-05 | IUGG/USGS |
| `GEO-M00-A04-MANTO-SOLIDO-004` | Manto sólido que flui por convecção; fusão localizada — **consistente com M02-a04 e M02-a05** | consenso geofísico |
| `GEO-M00-A04-POCO-PROFUNDO-008` | ~12 km (Kola, 12.262 m) — **consistente com M02-a02, que dá "menos de 0,2% do raio"; 12,26/6.371 = 0,19%** ✔ | registro público |
| `GEO-M00-A04-TEMP-CENTRO-009` | Alguns milhares de graus, com incerteza declarada — tratamento correto sob LC-08 | física de altas pressões |
| `GEO-M00-A05-*` (9 alegações) | Objeto do mapa geológico; convenções de cor e a ausência de padrão universal; estilos de linha; símbolo de atitude; conversões de escala; exagero vertical | CPRM/SGB; USGS; CGMW |
| `GEO-M00-A05-CORTA-MAIS-NOVO-008` | Relações de corte — **enunciado conferido contra M01-a03 e M03-a01; os três são consistentes** | princípio de Hutton |
| `GEO-M00-A06-*` (5 alegações) | Separação observação/interpretação; cor em superfície fresca; parâmetros de descrição macroscópica | CPRM/SGB; USGS |

## Observação didática (fora do escopo factual)

⚪ Registrada em uma linha, conforme a política da skill: a aula 05 é a única do curso que ensina leitura de mapa geológico antes do módulo 20. Vale conferir, quando o M20 for escrito, que ele **retome** e não **repita** — o risco é o aluno receber a mesma introdução duas vezes.

## Correções aplicadas

**Aplicadas em:** 2026-08-16

| claim_id / finding | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `XC-F01` / `GEO-M00-A04-ESPESSURAS-002` | 🟠 | Corrigido | `00-partida-do-zero-aula-04-terra-por-dentro.md` |
| `M00-F01` / `GEO-M00-A03-REGUA-006` | 🟠 | Corrigido | `00-partida-do-zero-aula-03-ordens-de-grandeza.md` |
| `M00-F02` / `GEO-M00-A06-CHAMBERLIN-003` | 🔵 | Resolvido | `00-partida-do-zero-aula-06-observar-descrever-inferir.md` |
| `M00-F03` / `GEO-M00-A03-MARCOS-004` | 🔵 | Resolvido | `00-partida-do-zero-aula-03-ordens-de-grandeza.md` |
| `M00-F04` / `GEO-M00-A01-FOSSIL-IDADE-008` | ⚪ | Aceito como está | — |

**Propagação:** no momento da auditoria, o módulo 00 ainda **não tinha** questionário nem baralho de flashcards, portanto não houve material derivado a propagar.

> [!note] Adendo de 2026-08-16 — material derivado gerado O questionário final (19 questões, 40 pontos) e o baralho (101 cards) foram gerados **depois** desta auditoria, contra o texto já corrigido. Nenhum dos dois herdou os achados: `XC-F01` (crosta continental 30 a 50 km) e `M00-F01` (história escrita em cinco milésimos de milímetro na régua) aparecem nos dois materiais já na versão corrigida, e são cobrados de propósito. `M00-F04` é cardificado como ausência de norma, não como número. `M01-F02` e `M02-F07`, abertos em outros módulos, não são cobrados por nenhum item.

**Pendências:** nenhuma.

## Nota de 2026-08-25 — separação dos cursos

Quando a gemologia saiu deste curso, o conceito de **gema** foi retirado da aula 01, que passou de seis para quatro conceitos centrais (mineral, rocha, cristal e fóssil). Com ele saíram duas alegações deste relatório:

- `GEO-M00-A01-GEMA-NAOMINERAL-005` — âmbar, pérola, coral e obsidiana como materiais gemológicos não minerais.
- `GEO-M00-A01-CRITERIOS-GEMA-006` — beleza, durabilidade e raridade como critérios de gema.

Os dois números ficam **retirados de circulação** nesta aula e não serão reciclados. A afirmação sobre a obsidiana não ser mineral continua na aula, coberta por `GEO-M00-A01-OBSIDIANA-004`. O conteúdo gemológico vive hoje no curso de Gemologia, módulo 01, aula 01.
