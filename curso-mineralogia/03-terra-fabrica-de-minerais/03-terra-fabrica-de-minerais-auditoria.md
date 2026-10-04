# Auditoria científica: Módulo 03 — A Terra como fábrica de minerais

**Auditado em:** 2026-10-04
**Material:** `curso-mineralogia/03-terra-fabrica-de-minerais/` — as 4 aulas (`03-terra-fabrica-de-minerais-aula-01` a `-aula-04`)
**Modo:** audit-and-fix
**Profundidade:** full
**Escopo:** as 51 alegações dos rodapés `alegacoes_auditaveis`, mais as afirmações de risco do corpo (profundidades e pressões das descontinuidades, composições médias, gradientes, ponto triplo do Al₂SiO₅, solubilidades, ponto crítico da água, sequência evaporítica, datas históricas). Questionário e baralho ainda não existiam.
**Veredito:** Requer correção → **correções aplicadas; estado final: Aprovado** (nenhum achado aberto)

## Resumo

🔴 0 erros · 🟠 2 imprecisões · 🟡 5 desatualizados/imprecisões menores · 🔵 0 sem fonte · ⚪ 0 controversos
Verificadas e corretas: 44 alegações (41 confirmadas, 3 prováveis); mais 3 da revisão didática na segunda passagem (47 no total).

Os pontos de maior risco passaram: as profundidades do PREM (Moho, 410, 520, 660, ~2.890 e ~5.150 km), as pressões das transições (13-14 e 23-24 GPa), a mineralogia do manto inferior (75/17/8 % em volume, Sun et al., 2016), as datas de aprovação da bridgmanita (2014) e da davemaoíta (2021), o ponto crítico da água (IAPWS-95), o ponto triplo do Al₂SiO₅ como faixa entre Holdaway (1971) e Pattison (1992), e as contas do exemplo trabalhado da aula 03. Os problemas foram de escopo (composição média da crosta continental, déficit de densidade do núcleo) e de mecanismo simplificado demais (solubilidade retrógrada da calcita).

> [!note] Limite da verificação nesta sessão
> A verificação usou busca na web (resumos e páginas institucionais) cruzada com as referências bibliográficas completas. Não houve acesso ao texto integral de Rudnick & Gao (2003), Warren (2016) nem Winter (2010); os números deles foram conferidos por fontes secundárias concordantes. Recomenda-se, numa sessão com acesso, conferir as frações da sequência de Usiglio em Warren (2016).

## Achados

### 🟠 1. Crosta continental "com composição de granodiorito"

**claim_id:** `TER-CRO-CONT-001`
**Tipo:** confusão de escopo
**Onde:** aula 01 · tabela de camadas e "A crosta: a única camada que tocamos"
**Está escrito:** "composição média próxima à de um granodiorito (~60% de SiO₂)"
**Problema:** os 60,6% de SiO₂ de Rudnick & Gao (2003) são a média da crosta **inteira**, de composição andesítica (intermediária). Granodiorito (~63-68% SiO₂) descreve a crosta **superior**. O texto juntava o número de uma com o nome da outra.
**Correção aplicada:** "~60% de SiO₂ em massa, intermediária entre a do basalto (~50%) e a do granito (~70%); a parte de cima é mais rica em sílica, próxima de um granodiorito"; tabela ajustada para "composição média intermediária (~60% de SiO₂), mais granítica no topo".
**Fonte:** Rudnick, R. L. & Gao, S. (2003), *Treatise on Geochemistry* 3, 1–64  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** só na aula 01.

### 🟠 2. Solubilidade retrógrada da calcita atribuída só à perda de CO₂

**claim_id:** `TER-FLU-RETRO-001`
**Tipo:** certeza indevida (mecanismo)
**Onde:** aula 04 · A molécula que desmonta cristais
**Está escrito:** "dissolve-se menos em água quente do que em água fria, porque o CO₂, que torna a água ácida, escapa da água quente"
**Problema:** a calcita tem solubilidade retrógrada mesmo com a pressão de CO₂ fixada; a menor solubilidade do CO₂ em água quente reforça o efeito em sistema aberto, mas não é a causa única. "Porque" apresentava uma das causas como a explicação.
**Correção aplicada:** "Parte do motivo é que o CO₂, que acidifica a água e ajuda a dissolver a calcita, é menos solúvel em água quente."
**Fonte:** Klein & Dutrow, *Manual of Mineral Science*, 23ª ed.; Plummer & Busenberg (1982), *Geochimica et Cosmochimica Acta* 46, 1011–1040  ·  **Nível:** livro-texto / revisada por pares
**Confiança:** confirmado
**Também aparece em:** exemplo trabalhado da aula 04 (anidrita), sem a mesma explicação; nada a corrigir ali.

### 🟡 3. Idade da crosta oceânica mais antiga

**claim_id:** `TER-CRO-OCEAN-001`  ·  **Onde:** aula 01
**Problema:** ~180 Ma vale para o assoalho dos oceanos atuais (Pacífico ocidental); há propostas de crosta oceânica mais antiga preservada no Mediterrâneo oriental.
**Correção aplicada:** "a mais antiga ainda no fundo dos oceanos atuais tem cerca de 180 milhões de anos".  ·  **Confiança:** confirmado

### 🟡 4. Como Lehmann deduziu o núcleo interno

**claim_id:** `TER-NUC-HIST-001`  ·  **Onde:** aula 01
**Problema:** "por ondas P refletidas" simplifica de forma imprecisa; o argumento de Lehmann (1936) foram chegadas de ondas P dentro da zona de sombra prevista.
**Correção aplicada:** "por ondas P que chegavam onde o modelo previa 'sombra'".  ·  **Confiança:** confirmado

### 🟡 5. Déficit de densidade do núcleo

**claim_id:** `TER-NUC-COMP-001`  ·  **Onde:** aula 01
**Problema:** o déficit de ~10% em relação ao ferro puro é do núcleo **externo**; o do interno é de poucos por cento.
**Correção aplicada:** "O núcleo externo é ~10% menos denso que ferro puro nas mesmas condições (o interno, alguns %)".  ·  **Confiança:** confirmado

### 🟡 6. Descoberta da coesita crustal atribuída só a Chopin

**claim_id:** `TER-PT-COESITA-001`  ·  **Onde:** aula 03
**Problema:** Chopin (1984, Alpes, Dora Maira) e Smith (1984, *Nature* 310, Noruega) publicaram no mesmo ano.
**Correção aplicada:** "(e, no mesmo ano, David Smith, na Noruega)".  ·  **Confiança:** confirmado

### 🟡 7. Solubilidade do quartzo em alta temperatura

**claim_id:** `TER-FLU-QTZSOL-001`  ·  **Onde:** aula 04
**Problema:** "milhares de mg" a "algumas centenas de graus e alguns kbar" exagera a faixa baixa: a ~400 °C e 1 kbar a solubilidade é da ordem de mil mg/kg; milhares exigem condições mais quentes (Manning, 1994).
**Correção aplicada:** "centenas a milhares de mg".  ·  **Confiança:** provável

## Verificado e correto

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `TER-INT-KOLA-001` | Kola ~12 km; raio 6.371 km | registros do poço SG-3; IUGG | confirmado |
| `TER-INT-ONDAS-001` | P em sólido e líquido; S só em sólido; sombra S revela núcleo líquido | PREM | confirmado |
| `TER-INT-CAMADAS-001` | Profundidades das camadas | PREM (Dziewonski & Anderson, 1981) | confirmado |
| `TER-CRO-MASSA-001` | Crosta <1%, manto ~67%, núcleo ~32% da massa | PREM | confirmado |
| `TER-CRO-ZIRCAO-001` | Zircão de Jack Hills ~4,4 Ga | Wilde et al. (2001), *Nature* 409 | confirmado |
| `TER-MOHO-1909-001` | Moho, 1909; Vp ~6-7 → ~8 km/s | história da sismologia; PREM | confirmado |
| `TER-MAN-PIROLITO-001` | SiO₂ ~45, MgO ~38, FeO ~8; ~60% de olivina | McDonough & Sun (1995) | confirmado |
| `TER-MAN-ALFASE-001` | Plagioclásio → espinélio (~30 km) → granada (~60-80 km) | Klein & Dutrow | confirmado |
| `TER-MAN-TRANSICAO-001` | 410 (13-14 GPa), 520, 660 km (23-24 GPa) | Klein & Dutrow; literatura de alta pressão | confirmado |
| `TER-MAN-INFERIOR-001` | 75/17/8 % em volume; bridgmanita provavelmente o mineral mais abundante | Sun et al. (2016), *JGR* | confirmado |
| `TER-MAN-BRIDGM-001` | Bridgmanita 2014 (Tenham); davemaoíta 2021 (inclusão em diamante) | Tschauner et al. (2014, 2021), *Science* | confirmado |
| `TER-MAN-AMORFIZA-001` | Bridgmanita amorfiza na descompressão | Tschauner et al. (2014) | confirmado |
| `TER-LIT-ESPESS-001` | Litosfera ~100 km (oceano) a ~200 km (cráton) | livros-texto | provável (crátons podem passar de 200 km) |
| `TER-CIC-HUTTON-001` | Ciclo das rochas remonta a Hutton (1785/1788) | Hutton (1788) | confirmado |
| `TER-IGN-TEXTURA-001` | Fanerítica, afanítica, vítrea, porfirítica | Winter | confirmado |
| `TER-IGN-PARES-001` | Granito/riolito; gabro/basalto | Le Maitre (2002) | confirmado |
| `TER-IGN-MINERAIS-001` | Minerais de magmas basálticos e graníticos | Winter | confirmado |
| `TER-SED-CAULIN-001` | Feldspato → caulinita; quartzo resiste | Klein & Dutrow | confirmado |
| `TER-SED-DIAGEN-001` | Compactação e cimentação; clásticas e químicas | sedimentologia | confirmado |
| `TER-MET-FOLIA-001` | Foliação; ardósia → xisto → gnaisse; mármore, quartzito, hornfels | Winter | confirmado |
| `TER-MET-MINERAIS-001` | Argila → mica → granada, estaurolita | Winter | confirmado |
| `TER-CIC-FAIXAS-001` | Faixas de T por família | Winter (ordem de grandeza) | confirmado |
| `TER-PT-RHOGH-001` | ~27 MPa/km; 1 GPa ≈ 30-37 km | cálculo | confirmado |
| `TER-PT-CALOR-001` | Calor residual + U, Th, K | Turcotte & Schubert | confirmado |
| `TER-PT-GRAD-001` | ~25-30 °C/km; ~1.300 °C na base da litosfera | Turcotte & Schubert | confirmado |
| `TER-PT-REGIMES-001` | 5-10, 20-30, ≥40 °C/km | Winter | confirmado |
| `TER-PT-AL2SIO5-001` | Ponto triplo ~0,4-0,45 GPa, 500-550 °C | Holdaway (1971); Pattison (1992) | confirmado |
| `TER-PT-SUBDUC-001` | Xisto azul (glaucofânio, lawsonita); eclogito (granada + onfacita) | Winter | confirmado |
| `TER-PT-ARCO-001` | Água abaixa o solidus do manto acima da placa | Winter | confirmado |
| `TER-PT-COLISAO-001` | Crosta espessada até ~60-70 km | tectônica | confirmado |
| `TER-PT-CONTATO-001` | Andaluzita e cordierita em hornfels | Winter | confirmado |
| `TER-PT-DIAMANTE-001` | Diamante a partir de ~140-150 km (~4,5 GPa) sob crátons | Kennedy & Kennedy (1976) | confirmado |
| `TER-PT-FUSAO-001` | Descompressão, água, aquecimento | Winter | confirmado |
| `TER-PT-PLACAS-001` | Alguns cm/ano | GPS | confirmado |
| `TER-PT-EXEMPLO-001` | 0,55 GPa; 1,76 GPa; 515 °C; 495 °C | recálculo | confirmado |
| `TER-FLU-POLAR-001` | Água polar hidrata íons | química geral | confirmado |
| `TER-FLU-COMPLEXO-001` | Complexos de Cl⁻ e HS⁻ | Robb | confirmado |
| `TER-FLU-FONTES-001` | Cinco fontes de água; magmas graníticos com vários % de H₂O | Robb; Winter | confirmado |
| `TER-FLU-CRITICO-001` | 373,946 °C; 22,064 MPa | IAPWS-95 | confirmado |
| `TER-FLU-EVAP-001` | Carbonatos → gipsita (~1/5) → halita (~1/10) → sais de K-Mg | Warren (2016) | provável |
| `TER-FLU-FUMAROLA-001` | 350-400 °C; sulfetos; anidrita por aquecimento | Tivey (2007) | confirmado |
| `TER-FLU-EBULICAO-001` | Ebulição separa CO₂ e H₂S e precipita Au | Robb | confirmado |
| `TER-FLU-QTZSINT-001` | Crescimento hidrotermal em autoclave | Klein & Dutrow | confirmado |
| `TER-FLU-GEODO-001` | Ametista em geodos de basalto; fendas alpinas | Mindat; Klein & Dutrow | confirmado |

## Consistência interna e com o resto do curso

- **Pressão × profundidade:** "~27 MPa/km" e "1 kbar ≈ 3,5 km" batem com o módulo 01, aula 06 (`QUI-UNID-PRESS-001`); o "1 GPa ≈ 35 km (30-37 km)" bate com o hub ("~1 GPa a ~30-35 km").
- **Espessura da crosta** (5-10 / 30-70 km) igual à do módulo 02, aula 04 (`MIN-ABU-CROSTA-001`).
- **Manto superior × manto todo:** a aula 01 respeita a correção feita no módulo 02 (`MIN-ABU-MANTO-001`): olivina e piroxênios só no manto superior.
- **Remissões:** curso-geologia citado só por nome no hub; nenhuma aula tem wikilink externo.

## Correções aplicadas

**Aplicadas em:** 2026-10-04

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `TER-CRO-CONT-001` | 🟠 | Corrigido | aula-01 |
| `TER-FLU-RETRO-001` | 🟠 | Corrigido | aula-04 |
| `TER-CRO-OCEAN-001` | 🟡 | Corrigido | aula-01 |
| `TER-NUC-HIST-001` | 🟡 | Corrigido | aula-01 |
| `TER-NUC-COMP-001` | 🟡 | Corrigido | aula-01 |
| `TER-PT-COESITA-001` | 🟡 | Corrigido | aula-03 |
| `TER-FLU-QTZSOL-001` | 🟡 | Corrigido | aula-04 |

Também foram atualizados: os rodapés `alegacoes_auditaveis` das 4 aulas (campo `audit:` em cada uma das 51 alegações); o hub do módulo; `course-state.yaml` (bloco `audit`).

## Segunda passagem (depois da revisão didática)

**Em:** 2026-10-04. A revisão didática moveu a seção de litosfera e astenosfera da aula 01 para a aula 03 (com a alegação `TER-LIT-ESPESS-001`, sem mudança de conteúdo) e acrescentou glossas. As três alegações novas foram conferidas:

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `TER-REV-GLOSSAS-001` | condritos, espinélio (óxido de Mg-Al), zircão, orto/clinopiroxênio | Klein & Dutrow | confirmado |
| `TER-REV-GLOSSAS-002` | glaucofânio, lawsonita, onfacita, cordierita; xisto azul e eclogito | Klein & Dutrow; Winter | confirmado |
| `TER-REV-GLOSSAS-003` | pegmatitos, esfalerita (ZnS), estaurolita (silicato de Fe-Al) | Klein & Dutrow | confirmado |

Total final: 54 alegações, 47 verificadas sem mudança e 7 corrigidas.

**Pendências:** nenhuma.

**Aviso de baralho já importado:** não se aplica; questionário e flashcards ainda não existiam.
