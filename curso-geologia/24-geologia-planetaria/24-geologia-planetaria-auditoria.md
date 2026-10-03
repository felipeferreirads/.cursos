# Auditoria científica — Módulo 24: Geologia planetária

**Modo:** audit-and-fix (dentro do pipeline do curso)
**Escopo:** as 5 aulas do módulo, auditadas em conjunto
**Data:** 2026-08-18
**Veredito: Aprovado, 0 achados**

## Achados

Nenhum achado 🔴, 🟠 ou 🟡. O módulo passou limpo na primeira auditoria.

## Verificado e correto

| claim_id | Aula | Alegação | Fonte | Confiança |
|---|---|---|---|---|
| `GEO-M24-A01-NEBULAR-001` | 01 | Sistema solar formado há ~4,6 Ga por colapso gravitacional de nebulosa, achatando-se em disco | NASA, Formation of the Solar System | confirmado |
| `GEO-M24-A01-LINHA-GELO-002` | 01 | Linha de gelo explica distribuição de planetas rochosos (próximos) vs. gigantes gasosos/gelados (distantes) | modelo padrão de formação planetária (NASA) | confirmado |
| `GEO-M24-A01-DIFERENCIACAO-003` | 01 | Diferenciação planetária é separação gravitacional metal/silicato num corpo (parcialmente) fundido | geoquímica/petrologia padrão (Goldschmidt, Módulo 09) | confirmado |
| `GEO-M24-A01-LHB-004` | 01 | Bombardeio pesado tardio (~3,8-4,1 Ga) é hipótese debatida, não consenso fechado | literatura de ciência planetária sobre o debate do LHB | confirmado (tratado corretamente como controvérsia, LC-08) |
| `GEO-M24-A02-CONDRITO-001` | 02 | Condritos preservam côndrulos, nunca fundiram, usados como referência da composição da nebulosa | NASA; Natural History Museum, classificação de meteoritos | confirmado |
| `GEO-M24-A02-ACONDRITO-METALICO-002` | 02 | Acondritos/metálicos/siderólitos vêm de corpos-mãe diferenciados, representando crosta-manto/núcleo/transição | classificação padrão de meteoritos | confirmado |
| `GEO-M24-A03-ESCAVACAO-001` | 03 | Impactos a dezenas de km/s escavam por onda de choque; cratera final ~10-20x o diâmetro do projétil | NASA; Melosh, Impact Cratering | confirmado |
| `GEO-M24-A03-SIMPLES-COMPLEXA-002` | 03 | Transição simples/complexa depende de gravidade e material; na Lua ~15-20 km, na Terra diâmetros bem menores | busca dedicada (AGU/JGR Planets, Krüger 2018; Chandnani 2019): transição lunar ~20 km, terrestre ~2-4 km conforme litologia | confirmado — valores da aula (15-20 km Lua; "bem menores" Terra) são consistentes com os valores medidos na literatura (Lua ~20 km; Terra ~2-4 km) |
| `GEO-M24-A03-CONTAGEM-CRATERAS-003` | 03 | Contagem de crateras dá idade relativa; conversão para absoluta exige calibração radiométrica (robusta só para a Lua, amostras Apollo) | Lunar and Planetary Institute; cronologia planetária padrão | confirmado |
| `GEO-M24-A04-RAZAO-SUP-VOL-001` | 04 | Corpos pequenos têm maior razão superfície/volume, perdem calor mais rápido, cessam atividade geológica antes | princípio físico padrão de resfriamento planetário | confirmado |
| `GEO-M24-A04-VENUS-ESTAGNANTE-002` | 04 | Vênus não tem tectônica de placas móvel reconhecida (stagnant lid); motivo da divergência com a Terra não é consenso fechado | ciência planetária comparativa (NASA) | confirmado — tratado corretamente como questão em aberto (LC-08) |
| `GEO-M24-A04-AQUECIMENTO-MARE-003` | 04 | Aquecimento de maré sustenta oceanos internos e criovulcanismo em luas geladas (Encélado, Europa, Io) | NASA/JPL | confirmado |
| — (verificação adicional não listada no rodapé da aula) | 04 | Vulcanismo dos mares lunares durou até cerca de 1-3 Ga atrás, conforme a região | busca dedicada: pico 3,9-3,1 Ga, amostras Chang'e-5/6 confirmam basalto até ~2,0-2,8 Ga, análise de crateras sugere possível extensão a ~1,2 Ga | confirmado — faixa "1 a 3 bilhões de anos" da aula está de acordo com a ordem de grandeza da literatura mais recente (Chang'e-5/6), correta sob LC-05 |
| `GEO-M24-A05-HABITABILIDADE-001` | 05 | Habitabilidade avaliada por múltiplos critérios geológicos, não só água líquida | NASA Astrobiology | confirmado |
| `GEO-M24-A05-BIOMARCADOR-002` | 05 | Metodologia padrão exige descartar explicações abióticas antes de aceitar biomarcador | NASA Astrobiology; literatura sobre falsos positivos de biosignature | confirmado |
| `GEO-M24-A05-JEZERO-003` | 05 | Cratera Jezero selecionada como sítio de pouso da Perseverance por evidência de leito de lago com delta antigo | NASA/JPL, missão Mars 2020 | confirmado |

## Consistência interna do módulo

- A diferenciação planetária ensinada na Aula 01 é reutilizada de forma coerente nas Aulas 02 (classificação de meteoritos por estágio de diferenciação do corpo-mãe) e 04 (comparação entre corpos rochosos).
- A contagem de crateras, ensinada na Aula 03, é aplicada de forma consistente na Aula 04 (idade relativa dos mares lunares vs. terras altas) e referenciada corretamente na Aula 01 (limite metodológico da datação do bombardeio pesado tardio).
- Nenhum valor numérico (idades, diâmetros de transição de cratera, faixas de vulcanismo lunar) se repete de forma divergente entre as aulas.
- As duas pendências de controvérsia herdadas de auditorias anteriores do curso e marcadas para retomada neste módulo em `_contexto.md` — **M01-F03** (origem da Lua por impacto gigante) e **M02-F05** (plumas mantélicas/pontos quentes) — foram avaliadas: a origem da Lua por impacto gigante é mencionada de passagem na Aula 01 ("o impacto que teria formado a Lua"), consistente com o tratamento como hipótese amplamente aceita mas não observada diretamente, sem reabrir o debate técnico (adequado ao nível da aula); o tema de plumas mantélicas/pontos quentes (M02-F05) não tem conexão direta com nenhum dos cinco objetivos de aprendizagem deste módulo (formação do sistema solar, meteoritos, cratereamento, comparação de corpos rochosos, astrobiologia) e não foi forçado para dentro do texto — permanece como pendência para os módulos que já o retomam (M10, M18), conforme `_contexto.md`.

## Observação fora de escopo (não é achado factual)

Nenhuma observação didática relevante nesta rodada.

## Correções aplicadas

**Aplicadas em:** 2026-08-18

Nenhuma correção necessária.

**Pendências:** nenhuma.
