# Auditoria científica — Módulo 03: Tempo geológico e geocronologia

**Data:** 2026-08-16
**Modo:** `audit-and-fix` (dentro do fluxo do curso)
**Escopo:** as 5 aulas do módulo, auditadas em conjunto (o que também checa contradições entre elas).
**Veredito:** ✅ **aprovado** — 0 🔴, 1 🟠 (corrigido), 0 🟡, 1 🔵 (registrado como ressalva não bloqueante).

## Saldo por severidade

| Severidade | Contagem | Situação |
|---|---|---|
| 🔴 erro factual | 0 | — |
| 🟠 impreciso / desatualizado | 1 | corrigido |
| 🟡 sem fonte / merece qualificação | 0 | — |
| 🔵 controverso / decisão pendente | 1 | registrado, já tratado no texto com ressalva |
| ⚪ observação | 0 | — |

**Gate liberado:** sem 🔴 ou 🟠 em aberto, o questionário e o baralho de flashcards do módulo estão autorizados.

Base da auditoria: 19 alegações auditáveis declaradas pelas próprias aulas (A01: 4 · A02: 6 · A03: 6 · A04: 3), mais a checagem cruzada de consistência entre aulas e com os módulos 01 e 02.

## Achados

### 🟠 M03-F01 — Faixa de temperatura de fechamento do K-Ar em "mica" genérica demais
**Aula:** 02 · **claim_id:** `GEO-M03-A02-FECHAMENTO-005`
**Problema:** o texto original dava uma única faixa de 300-350 °C para "K-Ar em mica", tratando o mineral como um bloco homogêneo. Na literatura de termocronologia, biotita e muscovita têm temperaturas de fechamento sensivelmente diferentes — biotita em torno de 300-330 °C, muscovita bem mais alta, 350-425 °C. A faixa original cobria a biotita mas ficava abaixo do valor real da muscovita, o que teria produzido uma leitura errada se o exemplo trabalhado ou um flashcard futuro citasse "K-Ar em muscovita fecha a ~340 °C".
**Fonte:** conceito de temperatura de fechamento (Dodson, 1973); valores de referência consolidados em termocronologia — biotita ~300-330 °C, muscovita ~350-425 °C, hornblenda (Ar-Ar, para contraste) ~500 °C.
**Correção aplicada:** o texto da Aula 02 (seção "Temperatura de fechamento: o que a idade realmente data") passou a diferenciar biotita, muscovita e hornblenda com faixas próprias, em vez de uma única faixa para "mica". O bloco de alegações auditáveis da Aula 02 foi atualizado com a nova faixa e uma nota explícita do que motivou a correção.
**Status:** ✅ fechado. `content_hash` da Aula 02 atualizado em `course-state.yaml` (de `7a4615a7a6f28ff2` para `7ad49191fd30cce4`).

### 🔵 M03-F02 — Temperatura de fechamento do U-Pb em zircão dada como faixa aproximada
**Aula:** 02 · **claim_id:** `GEO-M03-A02-FECHAMENTO-005`
**Situação:** o texto cita "acima de 800-900 °C" para o fechamento do sistema U-Pb em zircão. A literatura não converge num único número: zircão tem difusão de Pb extremamente lenta, e vários autores tratam esse sistema como praticamente sem temperatura de fechamento útil abaixo da temperatura de cristalização/anatexia (valores citados vão de ~900 °C a próximo do solidus, dependendo do tamanho de grão e da taxa de resfriamento assumidos).
**Tratamento:** o próprio texto já qualifica o valor como aproximado e o bloco de alegações já traz `confianca: media`, coerente com a natureza pouco padronizada desse número específico na literatura.
**Status:** 🔵 aberto por natureza — não bloqueia o módulo. Fica registrado para o caso de uma futura ficha de mineral sobre zircão (fora do escopo deste curso modular) precisar de um valor mais fechado.

## Verificações que passaram

| Alegação | Resultado |
|---|---|
| Steno (1669), *Dissertationis prodromus*: superposição, horizontalidade original, continuidade lateral | ✅ confirmado |
| William Smith, mapa geológico da Inglaterra e País de Gales de 1815, baseado em sucessão faunística | ✅ confirmado — não foi o primeiro mapa geológico do mundo, mas o primeiro de grande escala e detalhe nessa região; a aula não afirma "o primeiro do mundo", só "o primeiro mapa geológico nacional de grande escala", o que está correto |
| Quatro tipos de discordância (angular, disconformidade, não conformidade, paraconformidade) | ✅ classificação padrão, confirmado |
| Siccar Point, discordância angular observada por Hutton em 1788 | ✅ confirmado (a aula não afirma um valor específico de hiato em anos, então não há conflito com os ~65 Ma citados por algumas fontes para aquele hiato específico) |
| Meias-vidas: ²³⁸U→²⁰⁶Pb ~4,47 Ga (valor de referência ~4,468 Ga); ²³⁵U→²⁰⁷Pb ~704 Ma (referência ~703,8 Ma); ⁴⁰K→⁴⁰Ar ~1,25 Ga (referência ~1,248 Ga); ⁸⁷Rb→⁸⁷Sr ~48,8 Ga; ¹⁴⁷Sm→¹⁴³Nd ~106 Ga; ¹⁴C ~5.730 anos | ✅ todos confirmados dentro do arredondamento usado |
| Equação de decaimento t = (1/λ)·ln(1+D/N) e t₁/₂ = ln(2)/λ | ✅ correto, física nuclear padrão |
| Zircão incorpora U mas rejeita Pb; zircões terrestres mais antigos ~4,4 Ga | ✅ confirmado |
| ¹⁴C produzido na atmosfera superior por raios cósmicos + N; limite útil de datação ~50.000-60.000 anos | ✅ confirmado |
| Diagrama concórdia-discórdia — dois decaimentos independentes do U-Pb testam consistência interna; discórdia revela perda de Pb | ✅ correto |
| Exemplo trabalhado da Aula 02 (12,5% de ⁴⁰K restante = 3 meias-vidas = 3,75 Ga) | ✅ aritmética confere pelos dois caminhos (atalho de potência de 1/2 e fórmula logarítmica completa) |
| Hierarquia Éon > Era > Período > Época > Idade; quatro éons (Hadeano, Arqueano, Proterozoico, Fanerozoico); três eras do Fanerozoico | ✅ confirmado, ICS |
| Início do Fanerozoico / base do Cambriano em 538,8 Ma | ✅ confirmado — valor vigente na carta ICS consultada |
| GSSP da base do Cambriano em Fortune Head, Terra Nova, Canadá, escolhido em 1992, marcado pela primeira ocorrência do icnofóssil *Trichophycus pedum* | ✅ confirmado (a aula não menciona o icnofóssil especificamente, o que é uma simplificação aceitável para o nível da aula, não um erro) |
| GSSP da fronteira K-Pg (base do Andar Daniano) em El Kef, Tunísia, ratificado em 1991, marcado pela camada de argila com anomalia de irídio, idade ~66 Ma | ✅ confirmado |
| Fronteira Arqueano-Proterozoico fixada por GSSA em exatamente 2.500 Ma, sem GSSP associado | ✅ confirmado — a Subcomissão de Estratigrafia do Precambriano recomendou essa convenção numérica precisamente pela dificuldade de correlação física em rochas precambrianas, coerente com a explicação dada na aula |
| Pares cronoestratigráficos/geocronológicos (Eonotema/Éon, Eratema/Era, Sistema/Período, Série/Época, Andar/Idade) | ✅ nomenclatura padrão confirmada |
| Idade da Terra ≈ 4,54 ± 0,05 Ga, via U-Pb em meteoritos condríticos | ✅ confirmado, incluindo a margem de incerteza |
| Idade do Universo ≈ 13,8 Ga | ✅ confirmado (valor Planck ~13,797 Ga, dentro do arredondamento "≈13,8" usado na aula) |
| Exemplo trabalhado da Aula 05 (conversão do calendário cósmico: início do Fanerozoico ≈18 de novembro; fronteira K-Pg ≈26 de dezembro) | ✅ aritmética confere a partir dos valores de referência já verificados (538,8 Ma e 66 Ma sobre 4,54 Ga / 365 dias) |
| Percentual do Precambriano (~88% da história da Terra) | ✅ aritmética confere (538,8 / 4.540 ≈ 11,9% de Fanerozoico → ~88,1% de Precambriano) |

## Consistência entre as aulas e com os módulos anteriores

- **Datação relativa (A01) → datação absoluta (A02)** — a A02 abre explicitamente retomando a A01 ("a ordem que a datação absoluta vai agora calibrar em números"), sem reintroduzir nem contradizer nenhum princípio já estabelecido. ✅
- **A02 → A03** — a A03 usa a datação radiométrica da A02 exatamente como ferramenta de calibração da carta, sem inflar sua função (a carta não é "definida" pelos números, como a própria A03 enfatiza). ✅
- **A03 → A04** — a distinção cronoestratigrafia/geocronologia, insinuada de passagem na A03 ("o Sistema Jurássico é o corpo de rocha... o Período Jurássico é o próprio intervalo de tempo"), é formalizada sem contradição na A04. ✅
- **Valor de 538,8 Ma** — usado de forma consistente na A03 e na A04, e reutilizado corretamente no cálculo da A05. Nenhuma divergência entre aulas. ✅
- **GSSP vs. GSSA** — a distinção é introduzida na A03 e reaproveitada corretamente na A04 (unidades geocronométricas) sem contradição. ✅
- **Relação com o Módulo 01** — a A05 (tempo profundo, Hutton) não repete nem contradiz o conteúdo de tempo profundo já mencionado de passagem no Módulo 01; aprofunda com o método (Siccar Point) e os números (datação radiométrica) que o Módulo 01 ainda não tinha disponíveis. ✅
- **Relação com o Módulo 02** — nenhuma menção a limite manto-núcleo, Moho ou outros marcos do M02 é repetida aqui de forma divergente; os dois módulos não compartilham alegações numéricas sobrepostas. ✅
- **Remissões a módulos futuros** — todas corretas: bioestratigrafia e fósseis-guia → Módulo 15; unidades litoestratigráficas → Módulo 15; geocronologia do manto/crosta via Sm-Nd e Rb-Sr → Módulo 10 (geoquímica); glaciações precambrianas → Módulo 13; Grande Evento de Oxidação → Módulo 17 (geobiologia). Nenhuma aula promete um assunto ao módulo errado. ✅

## Registro para o estado

```yaml
audit:
  status: approved
  red: 0
  orange: 1
  yellow: 0
  blue: 1
  open_findings: []
  deferred_findings: ["M03-F02"]
  audited_at: "2026-08-16"
```

O único 🔵 (M03-F02) é uma ressalva de imprecisão de literatura sobre a temperatura de fechamento do zircão — já tratada com incerteza explícita no texto e sem impacto no restante do módulo. Não bloqueia a geração do questionário nem do baralho de flashcards.
