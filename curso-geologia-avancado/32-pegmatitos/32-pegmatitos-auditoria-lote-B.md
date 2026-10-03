# Auditoria científica — Módulo 32 (Pegmatitos) — LOTE B: Aulas 10–17

**Status:** relatório de lote (B de 3). A consolidação do módulo está em `32-pegmatitos-auditoria.md`.
**Datas:** Aulas 10–15 corrigidas em 2026-09-24 por uma sessão anterior; relatório escrito, Aulas 10–15 reverificadas e Aulas 16–17 auditadas em 2026-09-28.
**Modo:** audit-and-fix · **Profundidade:** full
**Escopo:** `32-pegmatitos-aula-10` a `32-pegmatitos-aula-17`.
**Material derivado:** o módulo 32 ainda não tem questionário nem flashcards; não houve propagação para esses arquivos nem baralho importado no Anki.
**Veredito do lote:** **Aprovado com correções.** Todos os 🔴/🟠/🟡 corrigidos. Os 🔵 e ⚪ foram reescritos com a incerteza explícita no texto; nenhum fica pendente.

## Nota sobre a história deste lote (importante para a rastreabilidade)

Uma sessão de 2026-09-24 auditou e corrigiu as Aulas 10 a 15 e anotou os achados no rodapé de cada aula (`[CORRIGIDO na auditoria 2026-09-24, achado Bnn-n ...]`, bloco `auditoria:` apontando para este arquivo), mas foi interrompida antes de escrever este relatório e antes de tocar nas Aulas 16–17. Nesta passagem (2026-09-28):

1. os achados B10–B15 foram **reconstituídos a partir das anotações dos rodapés**. As severidades desses achados foram atribuídas nesta passagem, pelo conteúdo da correção registrada, porque a sessão original não as gravou. Não há evidência de IDs perdidos com correção relevante: os números ausentes na sequência (B10-1, B11-5, B11-7, B12-3, B14-1) não aparecem em nenhum rodapé nem no texto, e não foram contados;
2. as Aulas 10–15 foram **relidas por inteiro** para conferir se as correções estavam no texto. Estavam. A releitura encontrou dois problemas novos (B12-10, B15-6);
3. as Aulas 16 e 17 foram auditadas do zero.

## Resumo por severidade

| Severidade | Qtde | Corrigidos | Abertos |
|---|---|---|---|
| 🔴 Erro | 7 | 7 | 0 |
| 🟠 Impreciso | 36 | 36 | 0 |
| 🟡 Desatualizado | 3 | 3 | 0 |
| 🔵 Sem fonte | 6 | 6 (confirmados, reescritos com ressalva ou retirados) | 0 |
| ⚪ Controverso | 2 | 2 (reescritos mostrando as posições) | 0 |
| **Total** | **54** | | |

### Inversões de sentido perigosas (prioridade para questionário e flashcards)

1. **B17-1:** a Suíte Borrachudos (~1,7 Ga; pegmatito Ponte da Raiz 1675 ± 5 Ma) aparecia como **mesoproterozoica** em cinco passagens da Aula 17. É **paleoproterozoica (estateriana)**: pela carta da ICS, o Paleoproterozoico vai até 1600 Ma.
2. **B14-4:** o cinturão de estanho-espodumênio de Kings Mountain estava como **arqueano**. É **mississippiano** (~340–351 Ma).
3. **B14-7:** Spruce Pine estava associado à colisão África–América do Norte (orogenia alleghaniana, carbonífero-permiana). Os granitoides têm 377–404 Ma (Devoniano, orogenia acadiana/neoacadiana).
4. **B15-3:** Manono estava num "cráton do Congo". Fica no **Cinturão Kibara**, orogênico; a mineralização tem 940 ± 5 Ma.
5. **B12-8:** Bikita era dada como mina **exaurida**. Está em operação, com expansões comissionadas em 2023.
6. **B12-1:** Tanco "aflorava" em Bernic Lake. É um corpo sub-horizontal **quase cego**, ~60 m sob o lago.
7. **B11-6:** Spruce Pine era citado como fonte de berílio. Não é: a fonte de referência de Be é a bertrandita de Spor Mountain (vulcânica), e o exemplo de berilo de pegmatito passou a ser Black Hills.
8. **B12-6:** Tanco e Bikita estavam em subtipos diferentes. Os dois são **subtipo petalita**; em Tanco a petalita virou espodumênio + quartzo (SQUI).

---

## Achados por aula

Formato compacto: **ID** `claim_id` · severidade · natureza · o que estava escrito → correção · fonte (confiança) · desfecho.

### Aula 10 — Debate das taxas de cristalização

**B10-2** `PEG-M32-A10-MODELOS-TERMICOS-001` · 🟠 · certeza_indevida — "dias a poucos anos" aparecia como resultado. Passou a resultado de modelo condutivo (Webber et al. 1999: ~5 dias no dique Himalaya a ~9 anos no Stewart, 650 → <550 °C), tratado como limite superior. Fonte: Webber et al. (1999), *Am. Mineral.* 84:708-717; valor do Stewart conferido em Phelps et al. (2020) (confirmado). **Corrigido.**

**B10-3** `PEG-M32-A10-PHELPS-2020-002` · 🟠 · impreciso — elementos e método. Correção: Al, Li e Ge em quartzo miarolítico, Ti como termômetro; camadas-limite de 10–100 µm; volume 11, artigo 4986. Fonte: Phelps, Lee & Morton (2020), *Nat. Commun.* 11:4986, texto integral PMC7536386 (confirmado). **Corrigido.**

**B10-4** `PEG-M32-A10-PHELPS-2020-002` · 🟠 · omissao_que_gera_erro — cristais métricos "em dias" sem a condição. Acrescentado "**se** as taxas se sustentarem" e que o material é quartzo de cavidade miarolítica, estágio tardio, não o corpo inteiro. **Corrigido.**

**B10-5** `PEG-M32-A10-POPOV-2023-003` · 🟠 · omissao_que_gera_erro — acrescentado que diferenças entre geocronômetros de temperaturas de fechamento distintas medem resfriamento (Aula 09); o argumento de Popov depende de domínios texturalmente controlados, datados de preferência pelo mesmo sistema. **Corrigido.**

**B10-6** `PEG-M32-A10-RECONCILIACAO-004` · ⚪ · certeza_indevida — a reconciliação aparecia atribuída à "literatura". Passou a síntese declarada do curso, ancorada no termo "episódios" do título de Phelps et al., com a limitação do lado cinético (a taxa depende do modelo de partição adotado). **Reescrito.**

**B10-7** `PEG-M32-A10-POPOV-2023-003` · 🟠 · impreciso — "Popov não descarta" passou a "não fecha a questão no sentido oposto". Fonte: Popov (2023), *Geosciences* 13(10):297 (confirmado). **Corrigido.**

### Aula 11 — Recursos minerais e "classe mundial"

**B11-1** `PEG-M32-A11-TA-NB-SN-002` · 🟡 · desatualizacao — nomes IMA columbita-(Fe), columbita-(Mn), tantalita-(Fe), tantalita-(Mn), com os antigos entre parênteses (coerente com A04-6). **Corrigido.**

**B11-2** `PEG-M32-A11-TA-NB-SN-002` · 🟠 · impreciso — "pegmatitos NYF como fonte secundária de Nb via pirocloro e fergusonita". O Nb de pegmatitos é sobretudo coproduto do Ta em concentrados de columbita-tantalita de pegmatitos LCT. **Corrigido.**

**B11-3** `PEG-M32-A11-TA-NB-SN-002` · 🟠 · impreciso — Sn de pegmatitos como "fonte histórica importante" passou a fonte secundária; Greenbushes começou pelo estanho em 1888; o TSB deve o nome à co-ocorrência. Fonte: Partington (2018), AusIMM Monograph 32. **Corrigido.**

**B11-4** `PEG-M32-A11-CS-BE-003` · 🟠 · inconsistencia_interna — fórmula da polucita alinhada à Aula 04 (·2H₂O). **Corrigido.**

**B11-6** `PEG-M32-A11-CS-BE-003` · 🔴 · erro_factual — Spruce Pine citado como fonte de berilo/Be. Substituído por Black Hills, e acrescentado que boa parte do Be mundial vem da bertrandita de Spor Mountain (Utah), não pegmatítica. Tanco com ~3/4 do minério de polucita mundial nos anos 1990 confirmado (Černý, Ercit & Vanstone 1996). **Corrigido.**

**B11-8** `PEG-M32-A11-VOCABULARIO-ECONOMICO-004`, `...-EXEMPLO-007` · 🟠 · impreciso — reserva exige recurso indicado/medido e ao menos estudo de pré-viabilidade; uma PEA não sustenta reserva (e pode usar inferido). "Estudo de viabilidade preliminar" do exemplo passou a PEA. Fonte: NI 43-101 e CIM Definition Standards (confirmado). **Corrigido.**

**B11-9** `PEG-M32-A11-CLASSE-MUNDIAL-005` · 🟠 · impreciso — "os 12 depósitos das Aulas 12–16 combinam esses fatores" passou a "classe mundial, arquétipos científicos ou as duas coisas" (Black Hills e Koktokay valem mais como referência científica; Spruce Pine, por um mineral industrial). **Corrigido.**

**B11-10** `PEG-M32-A11-CRITICIDADE-006` · 🟠 · impreciso — listas de minerais críticos datadas: USGS 2025 inclui Li, Ta, Nb, Cs, Rb, Be e Sn; UE 2023 inclui Li, Ta, Nb, Be (e feldspato), não Cs nem Sn. Fonte: USGS Final 2025 List (Federal Register, 7/11/2025); Critical Raw Materials Act 2023 (confirmado). **Corrigido.**

### Aula 12 — Tanco e Bikita

**B12-1** `PEG-M32-A12-TANCO-CONTEXTO-001` · 🔴 · erro_factual — "Tanco aflora em Bernic Lake". É um corpo sub-horizontal bilobado, ~60 m sob o lago, praticamente cego (só uma mancha da zona 5 "aflora"), em metagabro. Fonte: Černý, Ercit & Vanstone (1996), guia A3 GAC-MAC (lido). **Corrigido.**

**B12-2** `PEG-M32-A12-TANCO-IDADE-002` · 🟠 · impreciso — "2,64–2,67 Ga" passou a 2641 ± 3 Ma (U-Pb em tantalita). Fonte: Camacho et al. (2012), *Can. Mineral.* 50(6):1775-1792 (confirmado). **Corrigido.**

**B12-4** `PEG-M32-A12-TANCO-ZONAMENTO-003` · 🟠 · impreciso — mineralogia do Ta: tantalita-(Mn), grupos da wodginita e da microlita, ferrotapiolita e cassiterita, nas zonas (3) e (6); wodginita e microlita em boa parte substituições tardias. Fonte: Van Lichtervelde et al. (2007), *Econ. Geol.* 102(2):257-276 (confirmado no Crossref). **Corrigido.**

**B12-5** `PEG-M32-A12-TANCO-ZONAMENTO-003` · 🟠 · impreciso — Li primário sobretudo em petalita (cristais até 13 m) convertida em SQUI; retirada a afirmação de Li "na estrutura da polucita". **Corrigido.**

**B12-6** `PEG-M32-A12-COMPARACAO-008` · 🟠 · impreciso (classificação) — os dois são tipo complexo, **subtipo petalita**; a diferença está na fase de Li explotada, não no subtipo. **Corrigido.**

**B12-7** `PEG-M32-A12-TANCO-PRODUCAO-004` · 🟠 · impreciso — "décadas de produção contínua" passou a: início em 1969 (Ta), suspensão no fim de 1982, produção alternada; Sinomine desde 2019, espodumênio retomado em dezembro de 2021. **Corrigido.**

**B12-8** `PEG-M32-A12-BIKITA-PRODUCAO-007` · 🔴 · erro_factual — "depósito exaurido". Em operação; Sinomine (2022), plantas de espodumênio e petalita em 2023. **Corrigido.**

**B12-9** `PEG-M32-A12-BIKITA-CONTEXTO-IDADE-005` · 🟠 · impreciso — "contemporâneos dentro da incerteza": Bikita (2616–2625 Ma) é ~20–25 Ma mais jovem que Tanco. **Corrigido.**

**B12-10** `PEG-M32-A12-BIKITA-PRODUCAO-007` · 🟠 · impreciso (novo, 2026-09-28) — "capacidade da ordem de 300 mil t anuais de cada concentrado". São ~300 kt/ano de concentrado de espodumênio e ~480 kt/ano de petalita (dados da empresa). Fonte: Mining Technology, "Sinomine completes upgrades at Zimbabwe lithium mine"; Newsday Zimbabwe (provável). **Corrigido.**

### Aula 13 — Greenbushes e Pilgangoora

**B13-1** `PEG-M32-A13-GREENBUSHES-CONTEXTO-001`, `...-CONTROLE-ESTRUTURAL-007` · 🔵 · evidencia_insuficiente (pendência adiada da Aula 08, lote A) — controle por zona de cisalhamento **confirmado**: Greenbushes na zona Donnybrook–Bridgetown (~150 km), alojado durante D2 (Partington et al. 1995, *Econ. Geol.* 90(3):616-635); Pilgangoora em zonas de cisalhamento D4b (*Econ. Geol.* 120(5):1113-1139, 2025). **Resolvido.**

**B13-2** `PEG-M32-A13-GREENBUSHES-IDADE-002` · ⚪ · controversia — 2527 ± 2 Ma (Partington et al. 1995) × 2631 ± 4 Ma (zircão, capítulo AusIMM); Smithies et al. (2025) registram "várias idades neoarqueanas". Mantido em aberto, com a ressalva do zircão metamítico (Aula 09). **Reescrito com as posições.**

**B13-3** `PEG-M32-A13-GREENBUSHES-PARENTAL-003` · 🔵 · evidencia_insuficiente (pendência A01-5 do lote A) — não há parental demonstrado: granitoides datados na zona de cisalhamento ~90 Ma mais antigos; suíte mais jovem aparentemente sincrônica (Partington); pegmatitos gigantes "não precisam ter granitos parentais óbvios" (Partington 2018); proposta de Smithies et al. (2025), *Commun. Earth Environ.* 6:630. Coerente com a formulação cautelosa da Aula 01. **Resolvido.**

**B13-4** `PEG-M32-A13-GREENBUSHES-RECURSO-004` · 🟡 · desatualizacao — reserva de 86,4 Mt a 2,35% Li₂O era número antigo. Substituída por recurso ~447 Mt a 1,5% e reserva ~179 Mt a 1,9% Li₂O (JORC, 31/12/2023). Fonte: IGO, ASX 19/02/2024. **Corrigido (número antigo mantido como exemplo de desatualização).**

**B13-5** `PEG-M32-A13-GREENBUSHES-RECURSO-004` · 🟠 · impreciso — Ta como "fração relevante do recurso mundial" passou a histórico (grande produtor até o colapso de 2002, hoje subproduto); zonamento em camadas, não concêntrico. **Corrigido.**

**B13-6** `PEG-M32-A13-PILGANGOORA-CONTEXTO-IDADE-005` · 🟠 · impreciso (atribuição) — 2879 Ma era atribuída a "modelo do USGS". É Kinny (2000), Pb-Pb SHRIMP em columbita-tantalita, 2879 ± 5 Ma. **Corrigido.**

**B13-7** `PEG-M32-A13-PILGANGOORA-CONTEXTO-IDADE-005` · 🟠 · omissao — acrescentado 2845 ± 4 Ma em tantalita (ASEG 2019), ~15 Ma mais jovem que um plúton Split Rock próximo: há candidato a parental, mas a filiação não está demonstrada. **Corrigido.**

**B13-8** `PEG-M32-A13-PILGANGOORA-MINERALOGIA-RECURSO-006` · 🔵 · evidencia_insuficiente — 446 Mt a 1,28% Li₂O confirmado como posição de 31/03/2025 (anúncio de 11/06/2025); subtotal medido+indicado não confirmado e a comparação "assembleia mais diversa que Greenbushes" sem fonte foram **retirados**.

### Aula 14 — Black Hills, Kings Mountain, Spruce Pine

**B14-2** `PEG-M32-A14-BLACKHILLS-ZONAMENTO-002` · 🟠 · impreciso — Black Hills como "o berço" da nomenclatura. Cameron et al. (1949) sintetizaram ~68 homens-ano em vários distritos (Nova Inglaterra, Sudeste, Dakota do Sul, Idaho, Montana, Wyoming, Colorado, Novo México). **Corrigido.**

**B14-3** `PEG-M32-A14-BLACKHILLS-BENS-003` · 🟠 · impreciso — cristal de Etta: 14,3 × 0,8 m (Rickwood 1981, *Am. Mineral.* 66:885-907), com os relatos históricos de 42–47 pés; relevância atual reescrita como histórica/didática. **Corrigido.**

**B14-4** `PEG-M32-A14-KINGSMOUNTAIN-CONTEXTO-004` · 🔴 · erro_factual — idade "arqueana". Mississippiana (Rb-Sr ~340–351 Ma); o cinturão coincide com a zona de cisalhamento de Kings Mountain. **Corrigido.**

**B14-5** `PEG-M32-A14-KINGSMOUNTAIN-CONTEXTO-004` · 🟠 · certeza_indevida — Cherryville como "fonte fértil mais provável" passou a filiação debatida (anatexia comum × fracionamento); acrescentado o tipo albita-espodumênio. Fonte: GSA Connects 2022; *Econ. Geol.* 120(3) 2025. **Corrigido.**

**B14-6** `PEG-M32-A14-KINGSMOUNTAIN-MINERALOGIA-005` · 🟡 · desatualizacao — status da mina: fechada; reabertura da Albemarle em projeto (US$ 90 milhões do DoD, 2023; operação prevista para o fim de 2026, sujeita a licenças). **Corrigido.**

**B14-7** `PEG-M32-A14-SPRUCEPINE-FORMACAO-006` · 🔴 · erro_factual — "~380 Ma, colisão entre a placa africana e a norte-americana". U-Pb em zircão 377–404 Ma, orogenia acadiana/neoacadiana; a colisão África–América do Norte é alleghaniana, posterior. Fonte: Swanson & Veal (2010), *J. Geosci.* 55:27-42 (lido). **Corrigido.**

**B14-8** `PEG-M32-A14-SPRUCEPINE-FORMACAO-006` · 🟠 · certeza_indevida — "resfriamento lento em ambiente seco" apresentado como causa da pureza. É divulgação comercial sem apoio e em contraste com a literatura (cristalização a 20–30 km em magmas possivelmente ricos em água); "<10 ppm" é após beneficiamento. A causa da pureza segue sem explicação estabelecida. **Corrigido.**

**B14-9** `PEG-M32-A14-SPRUCEPINE-APLICACAO-007` · 🟠 · certeza_indevida — "~80% do HPQ mundial (BloombergNEF)" passou a estimativa de ~70–90% (Construction Physics). **Corrigido.**

### Aula 15 — Baía de James, Manono, Barroso-Alvão

**B15-1** `PEG-M32-A15-CV5-RECURSO-002` · 🟠 · omissao_que_gera_erro — o recurso de 2023 (109,2 Mt a 1,42% Li₂O) era **todo inferido**; atualizado com o consolidado CV5+CV13 de 20/06/2025 (108,0 Mt indicado + 33,4 Mt inferido) e a reserva provável de 84,3 Mt a 1,26% (2025). Fonte: GlobeNewswire 30/07/2023; PMET Resources (confirmado). **Corrigido.**

**B15-2** `PEG-M32-A15-CV5-MINERALOGIA-003` · 🟠 · impreciso — Whabouchi não é "relacionado" a CV5 (outro depósito, a centenas de km); petalita em CV5 e o subtipo "complexo, espodumênio" não confirmados, retirados. **Corrigido.**

**B15-3** `PEG-M32-A15-MANONO-CONTEXTO-004` · 🔴 · erro_factual — "rochas cratônicas do cráton do Congo". Manono está no Cinturão Kibara; pegmatitos ligados aos granitos do grupo E; U-Pb Nb-Ta 940 ± 5 Ma, Ar-Ar em muscovita ~934–939 Ma. Fonte: Dewaele et al. (2016), *Ore Geol. Rev.* 72:373-390 (confirmado). **Corrigido.**

**B15-4** `PEG-M32-A15-MANONO-RECURSO-005` · 🔵 · evidencia_insuficiente — produção histórica de Sn-Nb-Ta confirmada em termos gerais; datas e volumes não conferidos, declarados como tais no texto. **Corrigido com ressalva.**

**B15-5** `PEG-M32-A15-BARROSO-CONTEXTO-006` · 🟠 · impreciso — 370–290 Ma é o intervalo da orogenia varisca, não a idade dos pegmatitos (tardi-variscos); "milhares" passou a "alguns milhares". **Corrigido.**

**B15-6** `PEG-M32-A15-BARROSO-CLASSIFICACAO-007` · 🟠 · inconsistencia_interna (novo, 2026-09-28) — "subtipos de espodumênio e de petalita — paralelo direto com o par Tanco-Bikita". Depois de B12-6, Tanco e Bikita são do mesmo subtipo (petalita); o paralelo válido é a fase de lítio explotada. **Corrigido.**

### Aula 16 — Koktokay nº 3 e Jiajika

**B16-1** `PEG-M32-A16-KOKTOKAY-CONTEXTO-001` · 🟠 · impreciso — "evolução paleozoica-triássica da margem norte do continente asiático". Correção: o Altai chinês faz parte do Cinturão Orogênico da Ásia Central, orógeno acrescionário do Cambriano ao Carbonífero; os pegmatitos, triássicos a jurássicos, são posteriores à acreção e formaram-se em regime extensional. Fonte: *Frontiers in Earth Science* (2025), "Exhumation of the Koktokay rare-metal pegmatite group" (confirmado). **Corrigido.**

**B16-2** `PEG-M32-A16-KOKTOKAY-CONTEXTO-001` · 🟠 · inconsistencia_interna — a cúpula era 250 × 150 × 250 m no texto e "~250 m em cada dimensão" no recap e no rodapé. As fontes divergem (250 × 250 × 250 e 250 × 150 × 250 m); o texto passou a mostrar as duas e o recap diz só o que é comum (250 m de comprimento e de profundidade). **Corrigido.**

**B16-3** `PEG-M32-A16-KOKTOKAY-ZONAMENTO-002` · 🟠 · certeza_indevida — "quando o sistema tem tempo, espaço e um gradiente químico". Atribuir o zonamento a "tempo" antecipa como fato o que a Aula 10 e a seção de geocronologia da própria aula deixam em aberto. Reescrito. **Corrigido.**

**B16-4** `PEG-M32-A16-KOKTOKAY-GEOCRONOLOGIA-003` · 🔵 · evidencia_insuficiente — "leucogranitos ... peraluminosos (tipo S)": o resumo da fonte (*Gondwana Research* 2022) descreve muscovita-albita granitos com berilo e columbita-tantalita, sem classificar como tipo S. **Retirado.** As idades (224,2 ± 2,7 a 220,7 ± 4,0 Ma; 219,8 ± 1,3 Ma; Ar-Ar 181–177 Ma) foram **confirmadas**, assim como Zhou et al. (2015), *Resource Geology* 65:210-231 (Jurássico Inferior, ~16 Ma de evolução).

**B16-5** `PEG-M32-A16-KOKTOKAY-ZONAMENTO-002` · 🔵 · evidencia_insuficiente — "nove zonas": é a contagem clássica (Zhou et al. 2015); o trabalho de 2025 conta dez. **Corrigido com ressalva.**

**B16-6** `PEG-M32-A16-JIAJIKA-CONTEXTO-004` · 🟠 · impreciso — "deformados durante a evolução do sistema orogênico tibetano". Correção: sequências turbidíticas triássicas deformadas na orogenia indosiniana (Triássico Superior, fechamento do Paleotétis). Síntese regional consolidada (provável). **Corrigido.**

Verificado e correto: Jiajika como maior depósito pegmatítico de Li da China, 498 diques em ~80 km², dois grupos de idade (~213–208 e ~199–192 Ma), granitos de duas micas de 206–223 Ma, veio X03 com ~0,89 Mt de Li₂O (fontes da aula, ScienceDirect/GYIG, sem contradição encontrada).

### Aula 17 — Província Pegmatítica Oriental e Orógeno Araçuaí

**B17-1** `PEG-M32-A17-GEOCRONOLOGIA-CONTRASTE-004`, `...-FAMILIAS-005` · 🔴 · erro_factual — Suíte Borrachudos e pegmatito Ponte da Raiz (1675 ± 5 Ma) descritos como **mesoproterozoicos** (cinco ocorrências no corpo, no exemplo e no recap). São **paleoproterozoicos (Estateriano)**: o Mesoproterozoico começa em 1600 Ma (carta da ICS). Granito Borrachudos datado em 1729 ± 12 Ma; pegmatitos de Santa Maria de Itabira de idade estateriana. Fonte: *Research, Society and Development* (2023); "The Borrachudos Granitic Suite: Paleo- to Mesoproterozoic A-type Magmatism" (*An. Acad. Bras. Ciênc.*); Geologia USP (2024) (confirmado). **Corrigido.**

**B17-2** `PEG-M32-A17-SUPERSUITES-002` · 🟠 · impreciso — janelas das supersuítes. Correção segundo Pedrosa-Soares et al. (2011), *GSL Spec. Publ.* 350:25-51: G1 630–585 Ma (arco cálcio-alcalino; estava 630–595); G3 ~540–500 Ma, **tardicolisional**, leucogranitos de fusão de G2 (estava "tardi- a pós-colisional, 545–520"); G4 ~535–500 Ma, a supersuíte mais associada aos pegmatitos ricos em Li; estágio pós-colisional G4 + G5 de 530 a 480 Ma. Propagado para a Aula 19 (G4 ~535–500 Ma). **Corrigido.**

**B17-3** `PEG-M32-A17-GEOCRONOLOGIA-CONTRASTE-004` · 🟠 · certeza_indevida — "a idade de ~467 Ma ... sugerindo que a granitogênese pós-colisional fértil da província continuou". É uma única idade em zircão de um único corpo; reescrito como ponto em investigação, com o contraexemplo da monazita concordante de 498 ± 3 Ma (*Econ. Geol.* 120(5):1331-1370, 2025). **Corrigido.**

Verificado e correto: PPOB com ~150.000 km² (confirmado na síntese de 2025); onze distritos (Pedrosa-Soares et al.; mantido com ressalva, divisão varia entre autores); Santa Maria de Itabira como NYF e São José da Safira como LCT (Geologia USP 2024).

---

## Correções aplicadas

**Aplicadas em:** 2026-09-24 (Aulas 10–15) e 2026-09-28 (B12-10, B15-6, Aulas 16–17).

| Aula | Achados | Arquivo |
|---|---|---|
| 10 | B10-2…B10-7 | `32-pegmatitos-aula-10-debate-taxas-de-cristalizacao.md` |
| 11 | B11-1…B11-4, B11-6, B11-8…B11-10 | `32-pegmatitos-aula-11-recursos-minerais-classe-mundial.md` |
| 12 | B12-1, B12-2, B12-4…B12-10 | `32-pegmatitos-aula-12-tanco-bikita.md` |
| 13 | B13-1…B13-8 | `32-pegmatitos-aula-13-greenbushes-pilgangoora.md` |
| 14 | B14-2…B14-9 | `32-pegmatitos-aula-14-black-hills-apalaches.md` |
| 15 | B15-1…B15-6 | `32-pegmatitos-aula-15-nova-fronteira-litio.md` |
| 16 | B16-1…B16-6 | `32-pegmatitos-aula-16-china-koktokay-jiajika.md` |
| 17 | B17-1…B17-3 (+ ressalvas "risk" convertidas, ver revisão didática) | `32-pegmatitos-aula-17-mg1-provincia-oriental-aracuai.md` |
| 19 | propagação de B17-2 | `32-pegmatitos-aula-19-mg3-litio-jequitinhonha.md` |

Nos rodapés, as alegações afetadas receberam a anotação do achado, sem renumerar `claim_id`. O bloco `auditoria:` das Aulas 16–17 passou de `pendente` para 2026-09-28 / lote B.

**Pendências:** nenhuma.
