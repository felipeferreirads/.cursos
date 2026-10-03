# Auditoria científica: Módulo 29 — Recursos energéticos

**Auditado em:** 2026-08-29
**Material:** `29-recursos-energeticos/` — quatro aulas
**Modo:** audit (Fase 1) → **audit-and-fix** (Fase 2, após autorização do usuário — ver "Correções aplicadas" no fim)
**Profundidade:** full
**Escopo verificado com prioridade:** participação das fontes na matriz energética global e brasileira; dados de capacidade e geração nuclear e geotérmica; tecnologias de armazenamento; status da transição energética. Por serem números que mudam de ano para ano, cada alegação quantitativa foi checada contra fonte **datada** (IRENA, IEA, IAEA, IBGE/EPE) e a data da fonte está registrada em cada linha.
**Veredito final: Aprovado** — 0 🔴, 0 🟠, 1 🟡, corrigido em 2026-08-29. Nenhum achado em aberto.

## Resumo

🔴 0 erros · 🟠 0 imprecisões · 🟡 1 desatualizado · 🔵 0 sem fonte · ⚪ 0 controversos. Verificadas e corretas: 14 alegações.

**Uma observação que muda a leitura deste relatório.** A preocupação que motivou esta auditoria — "os números da matriz energética mudam com frequência e precisam de fonte datada" — em grande parte não se materializou, e por uma razão deliberada: **as quatro aulas quase não citam percentuais**. Elas ensinam a *estrutura* da matriz (unidades, oferta e demanda, primária vs. final, capacidade instalada vs. energia gerada, hierarquia de emissão) e descrevem as participações de forma qualitativa e comparativa ("majoritariamente fóssil", "bem acima da média mundial", "uma pequena fração nuclear"). Essa escolha torna o módulo notavelmente **durável**: não há uma safra de percentuais de 2024 esperando para envelhecer.

O preço dessa escolha aparece num único ponto — e é exatamente ali que está o achado: onde a aula 04 arrisca uma afirmação de superlativo ("a de maior capacidade instalada entre as fontes renováveis"), o mundo mudou embaixo dela.

## Achados

### 🟡 1. A hidrelétrica deixou de ser a renovável de maior capacidade instalada no mundo — a solar assumiu esse posto em 2023

**claim_id:** `ENE-M29A04-HIDROCAP-001`
**Tipo:** desatualização
**Onde:** `29-recursos-energeticos-aula-04-renovaveis-transicao-energetica-e-clima.md` · "Hidrelétrica: a renovável mais madura, com um limite geográfico claro"
**Está escrito:** "a tecnologia renovável mais madura e, historicamente, a de maior **capacidade instalada** entre as fontes renováveis em escala mundial"

**Problema:** a solar fotovoltaica ultrapassou a hidrelétrica em capacidade instalada global **em 2023**, três anos antes de esta aula ser escrita, e a distância desde então só aumentou. Pelos dados da IRENA de março de 2026, referentes ao fim de 2025:

| Fonte | Capacidade instalada (fim de 2025) |
|---|---|
| Solar | **2.392 GW** |
| Hidrelétrica renovável | 1.296 GW |
| Eólica | 1.291 GW |

A palavra "historicamente" atenua, mas não salva a frase: a aula está descrevendo o presente da matriz energética, num módulo cujo objetivo declarado (`geologia-m29-oa01`) é justamente ler e comparar a matriz **atual**. Um aluno lê "é a de maior capacidade instalada", não "já foi".

**O que continua verdadeiro, e é o que a frase deveria dizer:** a hidrelétrica ainda é a maior fonte renovável de **eletricidade gerada** — cerca de 14% da geração elétrica global em 2025, à frente de eólica e solar, porque seu fator de capacidade é muito mais alto (a própria aula 01 ensina exatamente essa distinção). A IEA projeta que a solar ultrapasse a hidrelétrica também em geração por volta de 2029, e a eólica por volta de 2030. Também permanecem corretos os outros dois atributos afirmados: é a renovável mais **madura**, e é **despachável**.

A ironia pedagógica vale registro: a aula 01 dedica uma seção inteira a "Capacidade instalada não é energia gerada: o erro mais comum ao comparar fontes", e a aula 04 tropeça precisamente nessa distinção — usando capacidade instalada onde geração seria o indicador correto e ainda verdadeiro.

**Correção proposta:** "a tecnologia renovável mais madura e, ainda hoje, a que mais **gera eletricidade** entre as fontes renováveis em escala mundial — cerca de 14% da geração elétrica global (IEA, 2025) — embora a solar fotovoltaica já a tenha ultrapassado em **capacidade instalada** desde 2023 (IRENA), diferença que se explica pelo fator de capacidade muito mais alto da hidrelétrica, como visto na Aula 01."
**Fonte:** [IRENA, *Renewable capacity highlights*, 31 de março de 2026](https://www.irena.org/-/media/Files/IRENA/Agency/Publication/2026/Mar/IRENA_DAT_RE_capacity_highlights_2026.pdf) (fim de 2025: solar 2.392 GW, hidrelétrica 1.296 GW, eólica 1.291 GW); [IRENA/Balkan Green Energy News, *Global solar power capacity surpasses hydropower in 2023*](https://balkangreenenergynews.com/irena-global-solar-power-capacity-surpasses-hydropower-in-2023/); [IEA, *Renewables 2025 — Renewable electricity*](https://www.iea.org/reports/renewables-2025/renewable-electricity) (hidrelétrica ainda a maior fonte renovável de geração, ~14%; solar deve ultrapassá-la em geração por volta de 2029) · **Nível:** base de referência (IRENA e IEA são as agências de referência para estatística de capacidade e geração) · **Versão:** IRENA, dados de fim de 2025, publicados em março de 2026; IEA *Renewables 2025*
**Confiança:** confirmado
**Também aparece em:** nenhum arquivo derivado — o módulo 29 ainda não tem questionário nem flashcards. **É por isso que este achado deve ser fechado antes da geração da avaliação:** "hidrelétrica é a renovável de maior capacidade instalada" é exatamente o tipo de afirmação que vira flashcard e passa a ser revisada ativamente já errada.

## Verificado e correto

Cada linha abaixo foi checada contra fonte datada e passou.

| claim_id | Aula | Alegação | Fonte (com data) | Confiança |
|---|---|---|---|---|
| `ENE-M29A01-TEPEJ-002` | 01 | tep e EJ são unidades de balanço energético; o BEN brasileiro usa tep, a IEA usa EJ | EPE/MME, BEN; IEA, *World Energy Balances* | confirmado |
| `ENE-M29A01-PRIMFINAL-003` | 01 | Energia primária é sempre maior que a final, porque toda conversão envolve perdas | termodinâmica e contabilidade energética padrão (IEA) | confirmado |
| `ENE-M29A01-MATRIZBR-004` | 01 | A matriz **elétrica** brasileira é majoritariamente renovável (puxada pela hidrelétrica) enquanto a matriz **energética total** permanece significativamente fóssil por causa dos transportes | EPE/MME, BEN (série histórica) | confirmado |
| `ENE-M29A01-FATORCAP-005` | 01 | Fator de capacidade é alto e estável para hidrelétrica e nuclear, baixo e variável para eólica e solar | conceito padrão de planejamento energético (IEA/EPE) | confirmado |
| `ENE-M29A01-EXEMPLOFC-006` | 01 | Fatores de capacidade de ~35% (eólica) e ~90% (nuclear) como ordens de grandeza típicas | EIA/Statista, médias dos EUA em 2024: eólica 34%, nuclear 92,3% | confirmado (ver ressalva abaixo) |
| `ENE-M29A02-RANKCARVAO-007` | 02 | Rank do carvão (linhito → sub-betuminoso → betuminoso → antracito) reflete carbonificação e poder calorífico crescentes | classificação padrão (USGS; petrologia sedimentar) | confirmado |
| `ENE-M29A02-EMISSAO-008` | 02 | Emissão de CO₂ por unidade de energia na ordem carvão > petróleo > gás natural, por causa da razão C/H de cada combustível | IEA/EIA, fatores de emissão por combustível; química da combustão | confirmado |
| `ENE-M29A02-GNL-009` | 02 | GNL é gás natural resfriado a cerca de −162 °C, permitindo transporte marítimo sem gasoduto | [US DOE, *LNG Basics*](https://www.energy.gov/hgeo/articles/lng-basics); indústria de GNL (redução de volume ~600×) | confirmado |
| `ENE-M29A02-RP-010` | 02 | A relação R/P do petróleo manteve-se historicamente estável apesar do consumo contínuo, por reavaliação de reservas | séries históricas de reservas provadas (EI/BP *Statistical Review*; IEA) | confirmado |
| `ENE-M29A03-URANIO235-011` | 03 | O urânio natural tem ~0,7% de ²³⁵U e ~99,3% de ²³⁸U, proporção praticamente constante em qualquer depósito | [World Nuclear Association, *Uranium Enrichment*](https://world-nuclear.org/information-library/nuclear-fuel-cycle/conversion-enrichment-and-fabrication/uranium-enrichment); [CDC, U-235/U-238](https://www.cdc.gov/radiation-emergencies/hcp/isotopes/uranium-235-238.html) | confirmado |
| `ENE-M29A03-ENRIQUECIMENTO-012` | 03 | O enriquecimento eleva o ²³⁵U a poucos por cento para reatores de água leve, o tipo mais comum no mundo | World Nuclear Association; IAEA | confirmado |
| `ENE-M29A03-CICLOABERTO-013` | 03 | O ciclo aberto (sem reprocessamento) é o mais adotado, inclusive pelo Brasil | [World Nuclear Association, *Nuclear Power in Brazil*](https://world-nuclear.org/information-library/country-profiles/countries-a-f/brazil) (o Brasil não planeja reprocessar; combustível usado armazenado em Angra); IAEA (a maioria dos Estados-membros não reprocessa) | confirmado |
| `ENE-M29A03-GRADIENTE-014` | 03 | Gradiente geotérmico tipicamente da ordem de 25–30 °C/km | [Britannica, *Geothermal gradient*](https://www.britannica.com/science/geothermal-gradient); literatura geofísica padrão (25–30 °C/km na crosta continental fora de limites de placa) | confirmado |
| `ENE-M29A04-PUMPEDHYDRO-015` | 04 | O armazenamento por bombeamento é a tecnologia de armazenamento de maior capacidade instalada no mundo | [IHA, *World Hydropower Outlook* — bombeamento ultrapassa 200 GW, >94% da capacidade de armazenamento de longa duração](https://www.hydropower.org/news/year-of-the-water-battery-global-pumped-storage-capacity-surpasses-200-gw); [IEA](https://www.iea.org/articles/how-rapidly-will-the-global-electricity-storage-market-grow-by-2026) (PSH ~3× as baterias em 2026, embora as baterias cresçam muito mais rápido) | confirmado |

### Ressalva sobre os fatores de capacidade do exemplo trabalhado (não é achado)

Os valores usados na aula 01 (~35% eólica, ~90% nuclear) conferem com as **médias dos Estados Unidos** em 2024 (34% e 92,3%). As médias **mundiais** são mais baixas — nuclear em torno de 80% e eólica onshore mais perto de 25–30%. Isso **não** é um achado, porque a aula declara explicitamente que são "valores típicos de ordem de grandeza para essas fontes, sujeitos a variação conforme o parque e o país", e porque a conclusão do exemplo (o fator de capacidade da nuclear é muito maior que o da eólica) vale sob qualquer um dos dois conjuntos. Registrado apenas para que uma revisão futura saiba de onde vieram os números, caso queira atribuí-los.

## Consistência interna do módulo

- A distinção **matriz elétrica × matriz energética total** é definida na aula 01 e usada de forma consistente nas aulas 02 e 04.
- A hierarquia de emissão carvão > petróleo > gás é estabelecida na aula 02 e reutilizada sem divergência na aula 04.
- A lógica reservatório + selo do Módulo 22 é aplicada ao CCS na aula 04 de forma coerente com o que aquele módulo ensina.
- O gradiente geotérmico da aula 03 (25–30 °C/km) não conflita com nenhum valor de outros módulos.
- **A única tensão interna encontrada** é a registrada no achado 1: a aula 04 usa capacidade instalada onde a aula 01 ensina que geração é o indicador correto para comparar fontes.

## Observações não factuais (fora de escopo desta auditoria)

- O objetivo `geologia-m29-oa01` promete "ler e comparar a matriz energética global e a brasileira", mas nenhuma das aulas apresenta uma composição concreta — nem percentuais, nem uma tabela de exemplo. O aluno aprende o vocabulário e o método sem nunca ver uma matriz preenchida. Isso é uma decisão de projeto defensável (durabilidade) e **não é um erro factual**, mas é uma lacuna de alinhamento entre objetivo e conteúdo que cabe ao `revisor-didatico` avaliar. Se ele recomendar incluir números, a recomendação desta auditoria é que venham sempre com ano e fonte explícitos no corpo do texto, no formato "(EPE/BEN 2025)" — nunca soltos.
- Erro de digitação na aula 01: "dois traços **specíficos**" → "específicos". Não é achado factual.

---

## Correções aplicadas

**Aplicadas em:** 2026-08-29 (modo `audit-and-fix`, autorizado pelo usuário após a entrega da Fase 1)

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `ENE-M29A04-HIDROCAP-001` | 🟡 | **Corrigido** | aula 04 |

**O que mudou:** a frase de abertura da seção sobre hidrelétrica passou a afirmar o que continua verdadeiro — que ela é a renovável que mais **gera eletricidade** no mundo (~14% da geração global, IEA 2025) — e a registrar explicitamente que **já não** é a de maior capacidade instalada, posto que a solar fotovoltaica assumiu em 2023 (IRENA). Em vez de apenas remover a afirmação envelhecida, a correção amarra o contraste à distinção entre capacidade instalada e energia gerada que a Aula 01 do próprio módulo ensina, e explica a diferença pelo fator de capacidade. O achado, que nasceu de a aula 04 tropeçar na lição da aula 01, virou uma aplicação dela.

Mantida sem alteração a segunda metade do parágrafo (limitações geográficas e socioambientais da hidrelétrica), que estava correta, e o recap relâmpago, que não repetia a alegação de capacidade instalada.

**Propagação:** nenhuma necessária — o módulo 29 ainda não tem questionário nem flashcards. Conferido que nenhuma outra passagem das quatro aulas repetia a alegação. A única outra afirmação de "maior capacidade instalada" no módulo é a do armazenamento por bombeamento (`ENE-M29A04-PUMPEDHYDRO-015`), que foi verificada e **está correta** (>200 GW, ~3× as baterias).

**Pendências:** nenhuma. **Gate científico liberado:** 0 achados em aberto de qualquer severidade.
