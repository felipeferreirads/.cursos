# Auditoria científica — Módulo 02: Sistema Terra: estrutura interna e tectônica de placas

**Data:** 2026-08-15
**Modo:** `audit-and-fix`
**Escopo:** as 6 aulas do módulo, auditadas em conjunto (o que também checa contradições entre elas).
**Veredito:** ✅ **aprovado** — 0 🔴, 1 🟠 (corrigido), 2 🟡 (corrigidos), 4 🔵 (registrados como ressalvas não bloqueantes).

## Saldo por severidade

| Severidade | Contagem | Situação |
|---|---|---|
| 🔴 erro factual | 0 | — |
| 🟠 impreciso / desatualizado | 1 | corrigido |
| 🟡 sem fonte / merece qualificação | 2 | corrigidos |
| 🔵 controverso / decisão pendente | 4 | registrados, tratados no texto com incerteza explícita |
| ⚪ observação | 2 | registrado |

**Gate liberado:** sem 🔴 ou 🟠 em aberto, o questionário e o baralho de flashcards do módulo estão autorizados.

Base da auditoria: 108 alegações auditáveis declaradas pelas próprias aulas (A01: 15 · A02: 23 · A03: 28 · A04: 16 · A05: 16 · A06: 15), mais a checagem cruzada de consistência entre aulas e com o módulo 01.

## Achados

### 🟠 M02-F01 — Taxa de espalhamento da Elevação do Pacífico Leste inconsistente entre duas aulas
**Aulas:** 03 e 04 · **claim_ids:** `GEO-M02-A03-TAXAESPALHAMENTO-028`, `GEO-M02-A04-DORSAL-RAPIDA-006`
**Problema:** a Aula 03 atribuía à Elevação do Pacífico Leste uma **meia-taxa de 8–9 cm/ano**, o que implica abertura total de 16–18 cm/ano. A Aula 04, no mesmo módulo, dava a **taxa total como "até cerca de 15 cm/ano"**. As duas afirmações não podem ser ambas verdadeiras, e a da Aula 03 estava acima da faixa usualmente citada. Agravante didático: a própria Aula 03 dedica um passo do exemplo trabalhado a alertar contra confundir meia-taxa com taxa total — e então tropeçava exatamente nisso.
**Fonte:** taxas de espalhamento de referência — dorsais lentas (Mesoatlântica) com abertura total de 2–5 cm/ano; a Elevação do Pacífico Leste, nos segmentos mais rápidos, com abertura total de até cerca de 15 cm/ano, ou seja, meia-taxa de até ~7,5 cm/ano.
**Correção aplicada:** a Aula 03 passou a dizer meia-taxa de 1–2,5 cm/ano (total 2–5) para dorsais lentas e cerca de 7–7,5 cm/ano de meia-taxa (total até ~15) para dorsais rápidas, com remissão explícita à Aula 04 e à equivalência entre as duas formas de expressar a taxa. O bloco de alegações auditáveis da Aula 03 foi atualizado junto.
**Status:** ✅ fechado.

### 🟡 M02-F02 — Atribuição a Ortelius (1596) apresentada sem procedência
**Aula:** 03 · **claim_id:** `GEO-M02-A03-ORTELIUS-001`
**Problema:** o texto afirmava, sem qualificação, que Abraham Ortelius comentou o encaixe dos continentes em 1596 no *Thesaurus Geographicus*. A atribuição é real, mas não é um dado que circulou continuamente na geologia: ela foi resgatada e trazida à atenção moderna em 1994, por um estudo do classicista James Romm. Apresentá-la como fato corrente omite que se trata de uma redescoberta filológica relativamente recente.
**Correção aplicada:** acrescentada a procedência no texto ("atribuição que só foi trazida à atenção da comunidade geológica moderna em 1994, por um estudo do classicista James Romm").
**Status:** ✅ fechado.

### 🟡 M02-F03 — Limite manto–núcleo: pendência herdada do módulo 01
**Aulas:** 01 e 02 · **claim_ids:** `GEO-M02-A01-GUTENBERG-006`, `GEO-M02-A02-CMB-013`
**Problema:** o módulo 01 deixou registrado o achado 🔵 **M01-F04**, que pedia maior precisão sobre a profundidade do limite manto–núcleo (o M01 usava "cerca de 2.900 km"). Era necessário verificar se o módulo 02 resolveria ou repetiria a imprecisão.
**Verificação:** resolvido corretamente e sem contradizer o módulo 01. A Aula 01 usa 2.900 km **no contexto histórico correto** — é o valor que Gutenberg determinou em 1913 — e registra em nota que o valor moderno é ~2.891 km. A Aula 02 adota explicitamente o valor do **PREM (2.891 km)** e declara que o número depende do modelo sísmico adotado, fazendo o mesmo com 410 km, 660 km e o limite núcleo externo/interno (~5.150 km).
**Status:** ✅ fechado quanto ao módulo 02. O achado **M01-F04 permanece deferido ao módulo 20** (geofísica) para o tratamento de precisão plena, conforme `_contexto.md`.

### 🔵 M02-F04 — Geometria da convecção do manto
**Aula:** 05 · **claim_id:** `GEO-M02-A05-660KM-GEOMETRIA-005`
**Situação:** convecção em manto inteiro × convecção estratificada em duas camadas separadas pela descontinuidade de 660 km. A tomografia sísmica mostra lajes frias atravessando os 660 km e alcançando a base do manto em várias regiões, o que sustenta a circulação de manto inteiro como quadro dominante — mas a transição de 660 km é endotérmica e oferece resistência real, com lajes que estagnam ali temporariamente. Não é uma questão fechada.
**Tratamento:** a aula apresenta explicitamente como conhecimento em evolução, não como fato consolidado. Adequado.
**Status:** 🔵 aberto por natureza. Retomar nos módulos **19** (tectônica global e geodinâmica) e **20** (geofísica).

### 🔵 M02-F05 — Origem e fixidez das plumas mantélicas e dos pontos quentes
**Aula:** 05 · **claim_ids:** `GEO-M02-A05-PLUMAS-ORIGEM-012`, `GEO-M02-A05-HOTSPOT-FIXIDEZ-013`, `GEO-M02-A05-DOBRA-HEC-011`
**Situação:** duas controvérsias reais e distintas. (a) A origem das plumas — profunda, no limite manto–núcleo, contra explicações rasas ligadas a fraturas litosféricas e heterogeneidade do manto superior (linha cética associada a G. R. Foulger). (b) A fixidez dos pontos quentes — há evidência de movimento relativo entre eles, o que afeta diretamente a leitura da dobra da cadeia Havaí–Imperador (~47 Ma): mudança do movimento da placa ou deriva do próprio hotspot.
**Tratamento:** a aula marca as duas frentes como debate ativo e, no exemplo trabalhado, apresenta as duas leituras concorrentes da dobra **sem eleger uma como verdade estabelecida**. Adequado.
**Status:** 🔵 aberto por natureza. Retomar nos módulos **11** (vulcanologia), **19** (geodinâmica) e **25** (geologia planetária, para o paralelo com vulcanismo de outros corpos).

### 🔵 M02-F06 — Balanço quantitativo das forças motoras e razão de Urey
**Aula:** 05 · **claim_ids:** `GEO-M02-A05-SLABPULL-DOMINANTE-006`, `GEO-M02-A05-RAZAOUREY-015`, `GEO-M02-A05-RAYLEIGH-003`, `GEO-M02-A05-VISCOSIDADE-004`
**Situação:** que o slab pull seja a força dominante é bem sustentado, inclusive pela evidência cinemática forte (placas com grande fração de borda subductante se movem muito mais rápido — Forsyth & Uyeda, 1975). O que **não** está fechado é o balanço quantitativo exato entre slab pull, ridge push, basal drag e sucção, que depende de parâmetros reológicos incertos. A razão de Urey (~0,3–0,5) é declaradamente mal restringida, e o número de Rayleigh e a viscosidade do manto são ordens de grandeza, não constantes medidas.
**Tratamento:** a aula distingue com rigor o que é medido, o que é modelado e o que é disputado; a razão de Urey vem com `confianca: baixa` no próprio bloco de alegações. Adequado.
**Status:** 🔵 aberto por natureza. Retomar nos módulos **19** e **20**.

### 🔵 M02-F07 — Manto profundo: natureza das LLSVPs e elementos leves do núcleo
**Aula:** 02 · **claim_ids:** `GEO-M02-A02-LLSVP-012`, `GEO-M02-A02-ELEMENTOS-LEVES-014`, `GEO-M02-A02-POSPEROVSKITA-011`, `GEO-M02-A01-DDOISLINHAS-015`
**Situação:** a **observação** tomográfica das duas grandes províncias de baixa velocidade de cisalhamento (sob a África e sob o Pacífico) é robusta e replicada; a **interpretação** (anomalia térmica, reservatório quimicamente distinto, pilha de crosta oceânica antiga subductada, ou combinação) segue em debate. Do mesmo modo, o déficit de densidade do núcleo externo é um dado sólido, mas *quais* elementos leves (S, O, Si, C, H) o explicam e em que proporção é uma das perguntas mais abertas da geofísica profunda. A natureza da camada D″ acompanha o mesmo estatuto.
**Tratamento:** as Aulas 01 e 02 separam explicitamente observação de interpretação em todos esses pontos, e a Aula 02 dedica um item de "O que não concluir" a cada um. Adequado — e é justamente o padrão de honestidade que o curso pede.
**Status:** 🔵 aberto por natureza. Retomar nos módulos **10** (geoquímica, para os elementos leves) e **20** (geofísica).

### ⚪ M02-F08 — Magnitudes dos sismos brasileiros são valores de catálogo
**Aula:** 06 · **claim_ids:** `GEO-M02-A06-JOAO-CAMARA-011`, `GEO-M02-A06-MATO-GROSSO-1955-012`
**Observação:** João Câmara (RN, 1986) e o evento de Mato Grosso (1955) são citados com magnitude "da ordem de" 5 e 6, respectivamente, e já vêm marcados com `confianca: media` por serem valores de catálogo antigos que variam entre fontes e entre escalas de magnitude. O texto não os apresenta como medidas precisas, e o ponto didático que eles sustentam — que a sismicidade intraplaca brasileira é **baixa, mas não nula** — não depende do valor exato. Sem ação. Precisão maior é assunto do módulo **26** (Geologia do Brasil).

### ⚪ M02-F09 — Vocabulário de metadados varia entre as aulas
**Aulas:** todas
**Observação:** o campo `risk:` dos blocos de alegações usa `numero | mecanismo | classificacao | historico | controverso` nas Aulas 01–05, e introduz `data` e `nomenclatura` nas Aulas 03 e 06. Os rótulos locais de objetivo também variam de forma (`OA-01a…d`, `OA-01…05`, `OA-03a…d`, `OA-05a…e`). Nada disso afeta o conteúdo científico nem o mapeamento para os objetivos do módulo, que é feito em `course-state.yaml` pelos ids canônicos `geologia-gemologia-m02-oa01…oa05`. Sem ação neste módulo; vale padronizar o vocabulário quando a convenção do plugin for revisada.

## Verificações que passaram

| Alegação | Resultado |
|---|---|
| Kola SG-3 ~12.262 m; raio médio da Terra 6.371 km | ✅ confirmado |
| Onda P em sólido/líquido/gás; onda S só em meio com rigidez (μ > 0) | ✅ correto e bem fundamentado |
| Zona de sombra de S além de ~103°; de P entre ~103° e ~143° por **refração**, não bloqueio | ✅ correto — e a distinção, que é o ponto técnico central da A01, está bem construída |
| Mohorovičić 1909 (sismo de Pokupsko); Gutenberg 1913; Lehmann 1936 | ✅ confirmado |
| PREM (Dziewonski & Anderson, 1981); CMB 2.891 km; ICB ~5.150 km; núcleo interno ~1.221 km de raio | ✅ confirmado |
| Descontinuidades de 410/660 km como **transição de fase**, não mudança composicional; 660 endotérmica | ✅ correto |
| Bridgmanita — nome IMA aprovado em 2014 (Tschauner et al.), antes "perovskita de silicato" | ✅ confirmado, incluindo a razão (exigência de amostra natural, achada em meteorito chocado) |
| Densidade média da Terra 5,514 g/cm³; fator de momento de inércia ~0,3307 < 0,4 | ✅ confirmado |
| Exemplo A02: manto 84% do volume, núcleo ~16% → densidade do núcleo ~17 g/cm³ | ✅ aritmética confere (0,837 × 3,3 + 0,163 × ρ = 5,514 → ρ ≈ 16,9); e a aula declara corretamente que o valor real é menor (10–13) por simplificar o manto como densidade constante |
| Exemplo A01: Δt(S−P) = 40 s, Vp 8 / Vs 4,5 km/s → ~411 km | ✅ aritmética confere, com verificação reversa no próprio texto |
| Distinção epicentro × hipocentro e necessidade de três estações (trilateração) | ✅ correto, inclusive a ressalva de que "triangulação" é o nome usual mas o método mede distâncias |
| Wegener 1912/1915; Polflucht e marés; objeção de Jeffreys sobre magnitude de força | ✅ confirmado, e tratado como episódio racional, não como teimosia da comunidade |
| Snider-Pellegrini 1858; du Toit 1937; Holmes (convecção, fim dos 1920/início dos 1930); ajuste de Bullard 1965 (500 braças) | ✅ confirmado |
| *Mesosaurus*, *Glossopteris*, *Cynognathus*, *Lystrosaurus*; tilitos permo-carboníferos | ✅ confirmado como conjunto canônico de evidência gondwânica |
| Hess 1962 ("History of Ocean Basins"); Dietz 1961 cunhou *seafloor spreading* | ✅ confirmado |
| Vine & Matthews (Nature, 1963) e Morley (rejeitado) | ✅ confirmado, com o crédito a Morley corretamente registrado |
| Wilson 1965 (transformante); Sykes 1967 (mecanismos focais); McKenzie & Parker 1967; Morgan 1968 | ✅ confirmado |
| Isacks, Oliver & Sykes 1968, JGR v. 73, p. 5855–5899 | ✅ referência bibliográfica confere |
| DSDP / *Glomar Challenger* a partir de 1968; idade do sedimento basal simétrica | ✅ confirmado |
| Brunhes–Matuyama ~0,78 Ma | ✅ confirmado |
| Exemplo A03: 15,6 km ÷ 0,78 Ma = 20 km/Ma = 2,0 cm/ano (meia) → 4,0 cm/ano (total); 200 km ÷ 20 = 10 Ma | ✅ aritmética confere em todos os passos |
| Fossa das Marianas / Challenger Deep ~10.900 m | ✅ confirmado como faixa (~10.900–10.935 m conforme a expedição) |
| Zona de Wadati–Benioff até ~700 km | ✅ confirmado — e **consistente entre as Aulas 04 e 06** |
| Magma de arco por **fusão por adição de fluidos**, não por atrito | ✅ correto, e é a correção didática mais valiosa da A04 |
| Geometria da transformante oceânica (movimento ativo só entre os segmentos de dorsal, sentido oposto ao aparente) | ✅ correto — o ponto contraintuitivo está bem explicado |
| Margem brasileira como margem **passiva**, dentro da Placa Sul-Americana | ✅ correto, e coerentemente reaproveitado na A06 para explicar a baixa sismicidade |
| Exemplo A04: hipocentros 100 km/100 km → 500 km/400 km ⇒ mergulho ≈ 53° | ✅ aritmética confere (arctan 400/300 = 53,13°) |
| Slab pull reforçado pela transição gabro → **eclogita** | ✅ correto |
| "Ridge push" como escorregamento gravitacional / energia potencial gravitacional, não pressão de magma | ✅ correto — corrige um erro muito difundido em material didático |
| Forsyth & Uyeda 1975: placas com borda subductante são mais rápidas | ✅ confirmado como argumento observacional a favor do slab pull |
| Exemplo A05: 2.600 km ÷ 28 Ma ≈ 92,9 km/Ma ≈ 9,3 cm/ano | ✅ aritmética confere; ordem de grandeza compatível com a Placa Pacífica |
| Fluxo de calor global ~46 TW | ✅ dentro da faixa das compilações correntes (~44–47 TW) |
| Momento sísmico M₀ = μ·A·d; Mw; saturação de ML acima de ~6,5–7 | ✅ correto |
| 1 grau de magnitude ≈ 10× amplitude e ≈ 32× energia (10^1,5) | ✅ confere |
| Valdivia 1960 Mw ~9,5; Sumatra 2004 Mw ~9,1; Tohoku 2011 Mw ~9,0 | ✅ confirmado (USGS) |
| Rebote elástico (Reid, a partir do sismo de São Francisco de 1906) | ✅ confirmado |
| Nova Madri 1811–1812 como sismicidade intraplaca | ✅ confirmado |
| Everest 8.849 m (medição conjunta China–Nepal, 2020) | ✅ confirmado (8.848,86 m, arredondado) |
| Subsidência térmica ∝ √idade; planície abissal funda por resfriamento, não erosão | ✅ correto |
| Isostasia (Airy × Pratt) e rebote pós-glacial como demonstração observável | ✅ correto |
| Ausência de previsão determinística de terremotos; alerta precoce ≠ previsão | ✅ correto e responsavelmente tratado — ponto sensível bem resolvido |

## Consistência entre as aulas

Verificado que nenhum termo é definido de duas formas diferentes no módulo, e que a progressão de pré-requisitos não tem salto:

- **litosfera × crosta** — a distinção herdada do M01 é mantida sem escorregão em nenhuma das seis aulas. A A04 explicita que placa é litosfera e que a borda da placa não é a borda do continente. ✅
- **astenosfera** — sempre sólida e dúctil, nunca "magma". A A02 combate a confusão diretamente, e a A05 reforça ao tratar convecção em estado sólido. ✅
- **descontinuidades de 410/660 km** — apresentadas como transição de fase na A01 e na A02, com a mesma interpretação; a A05 usa a resistência da transição de 660 km sem contradizer nada do que foi dito antes. ✅
- **profundidades de referência** — a A01 usa o valor histórico de Gutenberg no contexto histórico e a A02 adota o PREM; a diferença é explicada, não silenciosa. ✅
- **taxas de espalhamento** — havia divergência real entre A03 e A04 (achado M02-F01), **corrigida**; agora as duas aulas usam a mesma faixa e a A03 declara a equivalência entre meia-taxa e taxa total. ✅
- **zona de Wadati–Benioff (~700 km)** — mesmo valor na A04 e na A06. ✅
- **motor da tectônica** — a A04 descreve a geometria dos limites e adia explicitamente o motor para a A05, que por sua vez abre retomando a dívida de mecanismo deixada pela A03. A cadeia A03 → A04 → A05 não usa nenhum conceito antes de instalá-lo. ✅
- **fusão nos arcos** — introduzida na A04 (desidratação da laje) e reutilizada na A06 sem redefinir, com remissão correta aos módulos 07 e 11. ✅
- **margem passiva brasileira** — afirmada na A04 e reaproveitada na A06 para explicar a baixa sismicidade intraplaca. Mesma tese, sem contradição. ✅
- **remissões a módulos futuros** — consistentes e corretas: deformação → 18; orogênese e ciclo de Wilson → 19; geofísica de precisão → 20; magmas e vulcanologia → 07 e 11; geoquímica → 10; Brasil → 26; planetária → 25. Nenhuma aula promete um assunto ao módulo errado. ✅
- **relação com o módulo 01** — o M02 cumpre a promessa feita na A03 do M01 ("esse quadro será desenvolvido no módulo 02") e resolve, no que lhe cabe, a pendência M01-F04. ✅

## Registro para o estado

```yaml
audit:
  status: approved
  red: 0
  orange: 1
  yellow: 2
  blue: 4
  open_findings: []
  deferred_findings: ["M02-F04", "M02-F05", "M02-F06", "M02-F07"]
  audited_at: "2026-08-15"
```

Os quatro 🔵 são **ressalvas de literatura**, não pendências do material — controvérsias reais que o texto já sinaliza como tal, concentradas na Aula 05 (o motor da tectônica) e no manto profundo da Aula 02. Não bloqueiam a geração do questionário nem do baralho, mas ficam registrados para que o questionário **não cobre como fato fechado** nada que dependa deles: nem a geometria da convecção, nem a origem profunda das plumas, nem a fixidez dos hotspots, nem o balanço quantitativo das forças, nem a natureza das LLSVPs ou a composição exata dos elementos leves do núcleo.
