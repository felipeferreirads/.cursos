# Auditoria científica — Módulo 32 (Pegmatitos) — LOTE C: Aulas 18–26

**Status:** relatório de lote (C de 3). A consolidação do módulo está em `32-pegmatitos-auditoria.md`.
**Data:** 2026-09-28
**Modo:** audit-and-fix · **Profundidade:** full
**Escopo:** `32-pegmatitos-aula-18` a `32-pegmatitos-aula-26`.
**Material derivado:** o módulo ainda não tem questionário nem flashcards; nada a propagar e nenhum baralho no Anki.
**Veredito do lote:** **Aprovado com correções.** Todos os 🔴/🟠/🟡 corrigidos; 🔵 e ⚪ reescritos com a incerteza explícita. Nenhuma pendência.

**Padrão dominante do lote:** os erros graves estavam em frases de ligação e síntese que soavam seguras e não constavam da lista de alegações de risco — a etimologia inventada de LCT a partir da elbaíta, o autor inventado da elbaíta, a família de Volyn, a posição tectônica de Shigar, a confusão idade × duração, a classificação reserva × recurso de Xuxa. Os estudos de caso gemológicos (Aulas 18, 21–24) concentraram a maior parte, onde a literatura revisada por pares é mais rala e o redator se apoiou em fontes de divulgação.

## Resumo por severidade

| Severidade | Qtde | Corrigidos | Abertos |
|---|---|---|---|
| 🔴 Erro | 8 | 8 | 0 |
| 🟠 Impreciso | 27 | 27 | 0 |
| 🟡 Desatualizado | 6 | 6 | 0 |
| 🔵 Sem fonte | 5 | 5 (confirmados, reescritos com ressalva ou retirados) | 0 |
| ⚪ Controverso | 3 | 3 (reescritos mostrando as posições) | 0 |
| **Total** | **49** | | |

### Inversões de sentido perigosas (prioridade para questionário e flashcards)

1. **C23-1:** a elbaíta "deu nome à própria família geoquímica" LCT. **Falso:** LCT = lítio-césio-tântalo (Černý 1991a). A frase aparecia duas vezes.
2. **C23-2:** a elbaíta teria sido "descrita em 1913 pelo mineralogista italiano Ettore Panebianco". O nome é de **Vernadsky** (1913; Schaller descreveu no mesmo ano); o pegmatito Rosina é a localidade do **neótipo** (Bosi et al. 2025), não a localidade-tipo original.
3. **C24-1:** Volyn estava como família **LCT**. É **NYF**, pegmatito miarolítico ligado a um complexo anorogênico AMCG (granito tipo A, rapakivi).
4. **C21-1:** os pegmatitos de Shigar e Braldu (Dassu) estavam "no próprio maciço Nanga Parbat-Haramosh" (placa indiana). Ficam na placa **asiática**, no Complexo Metamórfico do Caracórum (ortognaisse de Dassu).
5. **C21-3:** "pegmatitos tão jovens teriam tido pouco tempo geológico para desenvolver zonamento e cavidades". Confunde **idade** com **duração da cristalização** — o erro que as Aulas 09 e 10 ensinam a evitar.
6. **C19-1:** Xuxa (11,8 Mt a 1,55% Li₂O) estava como **recurso**; é **reserva** provada e provável. O exemplo trabalhado comparava reservas com recurso sem notar — o erro de categoria que a Aula 11 ensina a evitar.
7. **C18-1:** "corpos de **classe** complexa a albita-espodumênio" como os gemíferos. Complexo e albita-espodumênio são **tipos**; e o tipo albita-espodumênio (corpos pouco zonados, como Cachoeira e Kings Mountain) é justamente o que **não** produz bolsões de gema.
8. **C23-5:** a mina Himalaya teria produzido "dezenas de milhas de toneladas" de turmalina, contra ~125 t no mesmo texto.

---

## Achados por aula

Formato compacto: **ID** `claim_id` · severidade · natureza · o que estava escrito → correção · fonte (confiança) · desfecho.

### Aula 18 — Distritos gemíferos de Minas Gerais

**C18-1** `PEG-M32-A18-CONTROLES-GEMA-006` · 🔴 · confusao_de_escopo + inconsistencia_interna — "normalmente em corpos de classe complexa a albita-espodumênio, segundo Černý & Ercit (2005)". Correção: tipo complexo (ex.: subtipo elbaíta) da classe de elementos raros, ou classe miarolítica; não o tipo albita-espodumênio (contradizia as Aulas 14 e 19 e o próprio texto sobre o Grupo Cachoeira). Fonte: Černý & Ercit (2005), *Can. Mineral.* 43:2005-2026 (confirmado no lote A). **Corrigido.**

**C18-2** `PEG-M32-A18-JONAS-GOLCONDA-002` · 🟠 · impreciso — Santa Rosa posta "no mesmo eixo Conselheiro Pena–São José da Safira". Fica ~36 km a sudoeste de Itambacuri, na região de Teófilo Otoni. Jonas fica na encosta de Itatiaia, perto de Conselheiro Pena (bolsão de rubelita de 1978). Fonte: Proctor (1985), *Gems & Gemology* 21(2), texto integral lido (confirmado). **Corrigido.**

**C18-4** `PEG-M32-A18-IPE-009` (novo) · 🟠 · certeza_indevida — Ipê (467 ± 5 Ma) como "a idade de cristalização mais provável para boa parte dos corpos gemíferos deste eixo". É a idade de um corpo num único geocronômetro. **Corrigido.**

**C18-5** `PEG-M32-A18-SAPUCAIA-0025` · 🟠 · impreciso — Sapucaia "no distrito pegmatítico de Aimorés" e "localidade-tipo de dez minerais, incluindo cinco espécies novas" (contraditório). Correção: distrito de Conselheiro Pena; localidade-tipo de cinco fosfatos descritos por Lindberg e colaboradores do USGS nos anos 1950 (barbosalita, faheyíta, frondelita, moraesita, tavorita); lavrada por muscovita e berilo. Fonte: *Am. Mineral.* 40:952 (1955); Mindat; *Braz. J. Geol.* (2015) (confirmado). **Corrigido.**

**C18-6** `PEG-M32-A18-BRAZILIANITA-008` (novo) · 🟠 · omissao_que_gera_erro — a aula tratava a Sapucaia como "referência mundial de fosfatos **gemológicos**", mas a Sapucaia é referência de mineralogia de fosfatos; o fosfato gemológico do distrito é a **brazilianita** (Córrego Frio, Linópolis, descrita em 1945). Fonte: Pough & Henderson (1945), *Am. Mineral.* (consolidado; provável quanto à citação exata). **Corrigido.**

**C18-7** `PEG-M32-A18-PRINCESA-005` · 🟡 · desatualizacao — "Princesa Brasileira, o maior topázio lapidado do mundo". Foi a maior gema lapidada quando cortada (1977); hoje é superada pelo El-Dorado (~31.000 ct, 1984) e pelo American Golden Topaz (22.892,5 ct), ambos de Minas Gerais. Fonte: Smithsonian (confirmado). **Corrigido.**

**C18-8** `PEG-M32-A18-CONTROLES-GEMA-006` · 🟠 · impreciso (terminologia) — "a composição elbaíta, a variedade que produz as cores gema": elbaíta é espécie; "série schorl-dravita" para a turmalina precoce de pegmatito passou a "schorl, com componente dravita variável". **Corrigido.**

Verificado e acrescentado: Golconda I (1908, mica), II (1935) e III (bolsão de ~900 kg de turmalina verde em 1961), a noroeste de Governador Valadares (Proctor 1985); Cruzeiro com gema desde 1914 e mica desde a Primeira Guerra; Ponto do Marambaia = classe de elementos raros, tipo berilo sem Ta-Nb (Ferreira, Fonseca & Pires 2005). A seção sobre as Golcondas atende também ao achado didático D-B01.

### Aula 19 — Lítio do Vale do Jequitinhonha

**C19-1** `PEG-M32-A19-XUXA-004` · 🔴 · erro_factual + inconsistencia_interna — "O recurso do depósito Xuxa foi estimado, em junho de 2021, em 11,8 Mt a 1,55% Li₂O". É **reserva** provada e provável; Barreiro (21,8 Mt a 1,37%, fev/2022) também. O exemplo trabalhado chamava os três números (Xuxa, Barreiro, Colina) de "números de recurso" e os comparava. Exemplo reescrito com a categoria como primeiro passo; acrescentada tabela com categoria e data. Fonte: Mining Technology; miningdataonline; Sigma Lithium (confirmado). **Corrigido.**

**C19-2** `PEG-M32-A19-CACHOEIRA-001` · 🟡 · desatualizacao — "a CBL detém historicamente a totalidade das reservas oficiais" (no recap, no presente). Passou a "por décadas deteve; deixou de valer na década de 2010". **Corrigido.**

**C19-3** `PEG-M32-A19-CACHOEIRA-001` · 🔵 · evidencia_insuficiente — petalita como mineral-minério da própria mina da Cachoeira não confirmada; o argumento espodumênio × petalita foi reescrito para o distrito de Araçuaí-Itinga. **Corrigido com ressalva.**

**C19-4** `PEG-M32-A19-COLINA-007` · 🟠 · impreciso — "Latin Resources, adquirida pela Pilbara Minerals em 2024" passou a "aquisição anunciada em 2024". **Corrigido.**

Propagado de B17-2: G4 ~535–500 Ma (três ocorrências).

### Aula 20 — Volta Grande e Borborema

**C20-1** `PEG-M32-A20-VOLTAGRANDE-002` · 🟡 · desatualizacao — "greenstone belt arqueano do vale do Rio das Mortes". A literatura antiga o chama de arqueano; os trabalhos recentes do Cinturão Mineiro tratam as sucessões de Rio das Mortes e Nazareno como paleoproterozoicas (metamorfismo a ~2,19 e ~2,13–2,10 Ga). Fonte: *Geoscience Frontiers* (2021), "U-Pb provenance fingerprints of metavolcanic-sedimentary successions of the Mineiro belt" (provável). **Corrigido, com as duas leituras.**

**C20-2** `PEG-M32-A20-VOLTAGRANDE-002` · 🔵 · evidencia_insuficiente — a relação com o Granitoide Ritápolis estava marcada como "carece de geocronologia direta dos pegmatitos". Há: pegmatitos que cortam os anfibolitos do Rio das Mortes deram U-Pb em zircão de 2121 ± 9 e 2121 ± 28 Ma, idênticas à do metagranito Ritápolis. Contemporaneidade sustentada; filiação estrita segue inferência. **Resolvido.**

**C20-3** `PEG-M32-A20-SJDR-CONTEXTO-001` · 🟠 · impreciso — "mais de 1,5 bilhão de anos mais antiga do que G1–G5": 2121 − ~630 Ma ≈ 1,49 Ga. "Cerca de 1,5 bilhão". **Corrigido.**

**C20-4** `PEG-M32-A20-VOLTAGRANDE-OPERACAO-006` (novo) · 🟡 · desatualizacao — "A mina Volta Grande foi historicamente lavrada". Lavrada desde 1945 e em operação (AMG Mineração), com espodumênio recuperado desde 2018. Fonte: Mindat; *Mineral. Mag.* (2025) (confirmado). **Corrigido.**

**C20-6** `PEG-M32-A20-PARAIBA-005` · 🟠 · omissao_que_gera_erro — "Paraíba" tratado como uso "em alguns contextos comerciais" para turmalina cuprífera de outras origens. Pela harmonização dos laboratórios (LMHC), "Paraíba" é nome de **variedade** (turmalina azul-verde colorida por Cu-Mn), independente da procedência. Fonte: LMHC Information Sheet (consolidado). **Corrigido.**

(O ID C20-5 foi reclassificado como achado didático — remissão cruzada errada — e não é contado aqui.)

### Aula 21 — Paquistão, Gilgit-Baltistão

**C21-1** `PEG-M32-A21-CONTEXTO-001`, `PEG-M32-A21-SHIGAR-KARAKORAM-006` (novo) · 🔴 · erro_factual — "Os pegmatitos gemíferos de Gilgit-Baltistão — nos vales de Shigar, Braldu, Haramosh e Stak — estão encaixados majoritariamente nas rochas ... do próprio maciço Nanga Parbat-Haramosh". Shigar e Braldu (Dassu) intrudem o ortognaisse de Dassu e o Complexo Metamórfico do Caracórum (placa asiática), como parte do Batólito Axial do Caracórum; só Haramosh e Stak Nala (e Dache, Khaltaro, Shegus) estão no NPHM (placa indiana). Os leucogranitos de Shigar (~11–3 Ma) vêm da fusão do gnaisse de Dassu. Fonte: Awais et al. (2022), *Geological Journal*; "Gems and gem-bearing pegmatites of the Shigar valley"; *Gondwana Research* (2026) (confirmado). Tabela Shigar × NPHM × rubi acrescentada. **Corrigido.**

**C21-2** `PEG-M32-A21-IDADE-002` · 🟠 · omissao_que_gera_erro — Ar-Ar em muscovita de 9,13 ± 0,04 Ma apresentado como idade do pegmatito. É idade de resfriamento, mínima para a cristalização (Aula 09). **Corrigido.**

**C21-3** `PEG-M32-A21-IDADE-DURACAO-007` (novo) · 🔴 · erro conceitual — "Pegmatitos tão jovens normalmente teriam tido pouco tempo geológico para desenvolver zonamento e cavidades bem formadas". Idade absoluta não é duração de cristalização. Reescrito: a juventude só reduz o tempo de exposição a deformação e alteração posteriores. **Corrigido.**

**C21-4** `PEG-M32-A21-CONTEXTO-001` · 🟠 · inconsistencia_interna — "lá [no Brasil], os pegmatitos eram arqueanos a paleoproterozoicos (Aulas 12-13, 17, 20)". O Brasil do bloco anterior vai do Paleoproterozoico ao Cambriano (Araçuaí e Borborema), e as Aulas 12–13 não são do Brasil. **Corrigido.**

**C21-5** `PEG-M32-A21-MINERALOGIA-003` · 🟡 · desatualizacao — "schorlita" → schorl (nome IMA). **Corrigido.**

**C21-6** `PEG-M32-A21-MINERALOGIA-003` · 🔵 · evidencia_insuficiente — "água-marinha ... dos vales de Shigar, Hunza e Braldu": Hunza sem fonte como produtor de água-marinha pegmatítica. **Retirado.**

**C21-7** `PEG-M32-A21-RUBI-NAO-PEGMATITO-005` · ⚪ · certeza_indevida — "mármores dolomíticos", "metamorfismo regional e metassomatismo de contato" e "a literatura especializada é explícita: pegmatitos estão ausentes". Garnier et al. (2008), *Ore Geol. Rev.* 34:169-191: mármores de séries carbonáticas de plataforma; Al e Cr das impurezas; sais evaporíticos como fundentes; depósitos **espacialmente relacionados a intrusões graníticas**, mas sem papel genético do granito. Reescrito sem "contato" e sem a certeza absoluta. **Reescrito.**

**C21-8** `PEG-M32-A21-CONTEXTO-001` · 🟠 · impreciso — "um pegmatito que já era 'recente' ... quando os primeiros hominídeos bípedes ainda nem existiam": só vale para o de 9,13 Ma; os de 7–0,7 Ma convivem com hominídeos. **Retirado.**

**C21-9** `PEG-M32-A21-CONTEXTO-001` · 🟠 · impreciso — "dezenas de milhões de anos" (os corpos têm ~11 a 0,7 Ma) e "do arqueano de Tanco ao paleoproterozoico de Volta Grande ... mais de 2,5 bilhões de anos" (esse intervalo tem ~0,5 Ga). Corrigido para "poucos milhões a ~10 Ma" e "de Pilgangoora (~2,88 Ga) a Koktokay e Jiajika (Triássico-Jurássico)". **Corrigido.**

### Aula 22 — Afeganistão

**C22-1** `PEG-M32-A22-IDADE-002`, `PEG-M32-A22-LAGHMAN-OLIGOCENO-007` (novo) · 🟠 · omissao — idade "qualitativa (mesozoico-cenozoica)". Os campos da zona do Nuristão se associam aos granitos de duas micas **oligocênicos** do Complexo Granitoide de Laghman (fase mais jovem, considerada fértil); datação direta dos pegmatitos segue escassa. Fonte: *Russian Journal of Earth Sciences* (dois artigos sobre o Complexo de Laghman, resumos); Rossovskiy (1981) (confirmado). **Corrigido.**

**C22-2** `PEG-M32-A22-CINTURAO-001` · 🟠 · impreciso — "Jalalabad" como província: é a capital de Nangarhar. **Corrigido.**

**C22-3** `PEG-M32-A22-JEGDALEK-006` · 🟠 · impreciso — Jegdalek "ao sul de Cabul". Fica ~60 km a **leste** de Cabul (distrito de Surobi/Sarobi), na borda sul do maciço do Nuristão. Fonte: Mindat/Gemdat (confirmado). **Corrigido.**

**C22-4** `PEG-M32-A22-JEGDALEK-006` · ⚪ · certeza_indevida — mesma formulação absoluta de C21-7 ("literatura explícita: pegmatitos ausentes") e "mármore dolomítico". Reescrito conforme Garnier et al. (2008). **Reescrito.**

**C22-5** `PEG-M32-A22-PAPROK-003` · 🔵 · evidencia_insuficiente — "encaixados em ardósia do Triássico Superior" vem de fonte de localidade (EarthWonders), sem literatura revisada. Mantido e atribuído. **Corrigido com ressalva.**

### Aula 23 — Madagascar, Elba, San Diego

**C23-1** `PEG-M32-A23-ELBA-003` · 🔴 · erro_factual — "A elbaíta ... popularizou o próprio nome do mineral que hoje serve de referência para toda a família geoquímica dos pegmatitos LCT" e "localidade-tipo de um mineral que deu nome à própria família geoquímica". LCT é sigla de Li-Cs-Ta (Černý 1991a). Substituído, com alerta explícito. **Corrigido.**

**C23-2** `PEG-M32-A23-ELBA-003` · 🔴 · erro_factual (atribuição) — "descrita formalmente em 1913 pelo mineralogista italiano Ettore Panebianco". Nome dado por Vernadsky (1913), com descrição de Schaller (1913); não há Panebianco na história da espécie. Fonte: Bosi et al. (2025), *Eur. J. Mineral.* 37:505-516, lido (confirmado). **Corrigido.**

**C23-3** `PEG-M32-A23-ELBA-003` · 🟠 · impreciso — pegmatito Rosina "localidade-tipo" e "cerca de 100 m ao sul" de San Piero. É a localidade do **neótipo** (2025), a algumas centenas de metros ao sul, na borda leste do plúton. **Corrigido.**

**C23-4** `PEG-M32-A23-ELBA-003` · 🟠 · impreciso — Monte Capanne "~7–8 Ma" e "plúton pós-colisional/anorogênico". Monzogranito de ~7 Ma da Província Magmática Toscana, ligado à extensão pós-colisional do Apenino Setentrional; "anorogênico" retirado (consolidado; provável quanto ao valor exato). **Corrigido** (também na tabela da Aula 24).

**C23-5** `PEG-M32-A23-SANDIEGO-004` · 🔴 · inconsistencia_interna — "dezenas de milhas [sic] de toneladas de turmalina" contra ~125 t no mesmo texto. "Da ordem de uma centena de toneladas". **Corrigido.**

**C23-6** `PEG-M32-A23-ANJANABONOINA-002` · 🟠 · impreciso (atribuição) — caráter híbrido LCT-NYF "segundo a classificação de Simmons". É a família **mista** de Černý & Ercit (2005); Madagascar discutido por Martin & De Vito (2005), *Can. Mineral.* 43:2027-2048 (confirmado no Crossref). **Corrigido.**

Verificado: Sahatany ~25 km a SW de Antsirabe, ~150 km², >100 pegmatitos LCT dos tipos berilo e complexo, idade pan-africana ~550 Ma (Mindat); Himalaya descoberta em 1898.

### Aula 24 — Volyn, Murzinka, Alto Ligonha

**C24-1** `PEG-M32-A24-VOLYN-001` · 🔴 · erro_factual — Volyn classificado como **LCT** na tabela-síntese e descrito como "fracionamento tardio de um grande granito peraluminoso" no exemplo. É **NYF** (miarolítico; Černý & Ercit 2005), ligado a granito anorogênico do tipo A; pegmatitos de 1760 ± 3 Ma, câmaras formadas por reaquecimento do granito semicristalizado por magma básico e fluidos do maciço gabro-anortosítico. Fonte: Shumlyanskyy et al. (2021), *Eur. J. Mineral.* 33:703 (resumo lido); *Biogeosciences* 19:1795 (2022) (confirmado). **Corrigido.**

**C24-2** `PEG-M32-A24-MURZINKA-002` · ⚪ · controversia — pegmatitos gemíferos "mais jovens, ~230–200 Ma", e "última fase de colisão continental do Triássico ao início do Jurássico". As fontes divergem: Ar-Ar em mica de Mokrusha, Kazennitsa e Semenovskaia dá ~250–254 Ma (contemporâneo do maciço de 248–259 Ma), enquanto Popov et al. (2022), *J. Mining Inst.* 255:337-348, citam 230–200 Ma; a colisão uraliana principal é carbonífero-permiana. Reescrito como caso em aberto. **Reescrito.**

**C24-3** `PEG-M32-A24-ALTOLIGONHA-004` · 🟠 · impreciso — "pertencem à família LCT" (os quatro tipos), "datados por CHIME em torno de 430–450 Ma" e "contemporâneos à intrusão dos granitos". Cronwright (2005): família LCT com algumas afinidades NYF; pegmatitos de 481–440 Ma, **posteriores** aos granitos pan-africanos tardios de ~521–495 Ma; "sodalithic" é o termo regional para pegmatito sódico-litinífero (explicado, para não sugerir sodalita). Fonte: resumo do trabalho, lido no repositório da U. Porto (confirmado). **Corrigido.**

**C24-4** `PEG-M32-A24-ALTOLIGONHA-004` · 🟠 · inconsistencia_interna — "no mesmo padrão de depósito polimetálico com valor agregado gemológico já visto para Volta Grande (Aula 20)". A Aula 20 diz que Volta Grande não tem apelo gemológico. **Corrigido.**

**C24-5** `PEG-M32-A24-SINTESE-005` (novo) · 🟠 · impreciso — "cinco continentes" (são quatro: Ásia, Europa, África, América do Norte); o objetivo falava em "seis províncias" (a tabela tem oito). **Corrigido.**

**C24-6** `PEG-M32-A24-VOLYN-001` · 🟡 · desatualizacao — Volodarsk-Volynski foi renomeada Khoroshiv (2016). **Corrigido, com o nome antigo mantido.**

### Aula 25 — Exploração, GREENPEG, Bird River

**C25-1** `PEG-M32-A25-KRB-002` · 🟠 · analogia que ensina modelo errado — K/Rb em muscovita apresentado como "o mesmo raciocínio de geobarômetro geoquímico já discutido para o par espodumênio-petalita". K/Rb é indicador de **fracionamento**; o par Spd-Pet é indicador de **pressão**. **Corrigido.**

**C25-2** `PEG-M32-A25-GREENPEG-004` · 🟠 · inconsistencia_interna — "três áreas de demonstração ... do ártico costeiro ao temperado florestal, alpino e mediterrâneo". São três: Tysfjord (ártico costeiro), Leinster (temperado florestal), Wolfsberg (alpino), de 20–70 km² cada. Fonte: NHM Oslo, página do projeto; *Econ. Geol.* 120(3) (2025) (confirmado). **Corrigido.**

**C25-3** `PEG-M32-A25-GREENPEG-004` · 🟠 · impreciso (tradução) — "magnetômetro de bigode (*nose stinger*)". É um magnetômetro em haste frontal de helicóptero — o primeiro da Europa —, que permite voos a ~50 m do solo. **Corrigido.**

**C25-4** `PEG-M32-A25-BIRDRIVER-005`, `...-HALO-003` · 🔵 · evidencia_insuficiente — o trabalho de Galeschuk & Vanstone era conhecido só por síntese. Conferido: *Exploration 07*, p. 823-839; halos de Li são os mais largos e passam de 100 m em Tanco; litogeoquímica desde meados dos anos 1970; *Enzyme Leach* sobre Tanco e sobre o pegmatito Dibs (enterrado, complexo, subtipo petalita, descoberto em 1997). "Li > Rb > Cs" mantido como tendência geral. **Resolvido.**

### Aula 26 — Lavra, beneficiamento, garimpo

**C26-1** `PEG-M32-A26-BENEFICIAMENTO-002` · 🟠 · impreciso — DMS "para que o espodumênio afunde e a ganga flutue (ou vice-versa, conforme a configuração)". O espodumênio (~3,1–3,2 g/cm³) é sempre o produto afundado contra ganga de ~2,6–2,9 g/cm³. **Corrigido.**

**C26-2** `PEG-M32-A26-FECHAMENTO-007` (novo) · 🟠 · impreciso — "treze estudos de caso de classe mundial em quatro continentes". São treze **aulas** de estudo de caso (12–24), com dezenas de depósitos, em seis continentes. **Corrigido.**

**C26-3** `PEG-M32-A26-REGULACAO-BRASIL-005` · 🟠 · omissao_que_gera_erro — PLG sem base legal nem a condição ambiental. Correção: criada pela Lei nº 7.805/1989, depende de licenciamento ambiental prévio; Estatuto do Garimpeiro (Lei nº 11.685/2008); turmalina, berilo, quartzo, feldspato e mica estão entre os bens garimpáveis (consolidado). **Corrigido.**

Verificado: calcinação α→β a ~1.050–1.100 °C com expansão de ~30% e redução de ~40% na energia de moagem (*Sci. Rep.* 2022, fonte da aula); DMS + flotação como fluxograma padrão.

---

## Correções aplicadas

**Aplicadas em:** 2026-09-28.

| Aula | Achados | Arquivo |
|---|---|---|
| 18 | C18-1, 2, 4, 5, 6, 7, 8 | `32-pegmatitos-aula-18-mg2-distritos-gemiferos.md` |
| 19 | C19-1…C19-4 (+ propagação B17-2) | `32-pegmatitos-aula-19-mg3-litio-jequitinhonha.md` |
| 20 | C20-1…C20-4, C20-6 | `32-pegmatitos-aula-20-volta-grande-borborema.md` |
| 21 | C21-1…C21-9 | `32-pegmatitos-aula-21-paquistao-gilgit-baltistao.md` |
| 22 | C22-1…C22-5 | `32-pegmatitos-aula-22-afeganistao-hindu-kush.md` |
| 23 | C23-1…C23-6 | `32-pegmatitos-aula-23-classicos-miaroliticos-madagascar-elba-san-diego.md` |
| 24 | C24-1…C24-6 (+ propagação C21-1, C22-1, C23-4 na tabela-síntese) | `32-pegmatitos-aula-24-volyn-murzinka-alto-ligonha.md` |
| 25 | C25-1…C25-4 | `32-pegmatitos-aula-25-exploracao-fertilidade-greenpeg-bird-river.md` |
| 26 | C26-1…C26-3 | `32-pegmatitos-aula-26-lavra-beneficiamento-garimpo.md` |

Nos rodapés, as alegações afetadas receberam a anotação do achado, sem renumerar `claim_id`; foram criadas as alegações A18-007/008/009, A20-006, A21-006/007, A22-007, A24-005 e A26-007. O bloco `auditoria:` de cada aula passou de `pendente` para 2026-09-28 / lote C.

**Pendências:** nenhuma.
