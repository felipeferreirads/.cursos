# Auditoria científica: Módulo 01 — Gemologia geral e identificação

**Auditado em:** 2026-08-24 · **passagem adicional em 2026-08-27** (alegações novas das aulas 01–06 — ver seção própria mais abaixo)
**Material:** `01-gemologia-geral/` — 22 aulas (01–06 preservadas da versão anterior e depois aprofundadas em 2026-08-25, 07–21 novas, 22 reescrita a partir da antiga aula 11)
**Modo:** audit-and-fix
**Profundidade:** full
**Escopo (rodada de 2026-08-24):** propriedades numéricas (densidade relativa, índice de refração, dispersão, dureza), nomenclatura (jade, opala, turquesa, lápis-lazúli, turmalina Paraíba), mecanismos ópticos (fluorescência, asterismo, chatoyance, difração, mudança de cor), classificações GIA (grau de lapidação, fluorescência), instrumentação de laboratório, geologia das gemas, províncias brasileiras e instrumentos de mercado (Kimberley, Rapaport, LMHC); consistência entre as aulas do módulo
**Veredito final:** Aprovado (rodada de 2026-08-24) · **Aprovado com correções** (passagem de 2026-08-27: 🟠 1 · 🟡 1, ambas corrigidas)

> [!info] Histórico
> Esta auditoria substitui a de 2026-08-19, feita sobre o módulo de 11 aulas. Os achados daquela rodada estavam todos encerrados. As aulas 01–06 foram reauditadas nesta passagem e permanecem corretas; os claim_ids `GEM-NOM-001/002`, `GEM-COR-001`, `GEM-ID-001`, `GEM-INST-001/002` e `GEM-FLUXO-001` seguem válidos e não foram reciclados. Os claim_ids das aulas migradas (`GEM-DIA-*`, `GEM-COLOR-CLASS-001`, `GEM-TRT-001/002`) passam a ser auditados nos módulos 02 e 03, com o mesmo ID.

## Resumo

🔴 0 erros · 🟠 5 imprecisões · 🟡 0 desatualizados · 🔵 0 sem fonte · ⚪ 0 controversos. Verificadas e corretas: 34 alegações.

Todos os cinco achados 🟠 foram corrigidos nesta mesma rodada, antes da geração do questionário e do baralho. Nenhum achado permanece aberto.

## Achados

### 🟠 1. A proporção de diamantes naturais que fluorescem estava arredondada para cima

**claim_id:** `GEM-UV-002`
**Tipo:** impreciso (valor fora da faixa publicada)
**Onde:** aula 08 · "O que a fluorescência ajuda a ver" e Recap
**Estava escrito:** "Cerca de um terço dos diamantes naturais fluoresce sob onda longa"
**Problema:** "um terço" (33%) fica no topo da faixa publicada pelo GIA e apresenta como valor central o que é o extremo superior. Faltavam ainda duas qualificações relevantes para o aluno: a esmagadora predominância do azul e a fração pequena que atinge intensidade capaz de afetar aparência.
**Correção aplicada:** "Entre cerca de **25% e 35%** dos diamantes naturais submetidos a graduação apresentam alguma fluorescência sob onda longa, e mais de 95% dessas reações são **azuis** [...] Dos diamantes que fluorescem, apenas cerca de 10% chegam às intensidades média, forte ou muito forte".
**Fonte:** GIA, *Understanding Diamond Fluorescence* e *Dispelling Myths: The Truth About Diamond Fluorescence* (estudo com mais de 26.000 diamantes graduados); GIA, *Gems & Gemology*, Summer 2021, "Measurement and Characterization of the Effects of Blue Fluorescence on Diamond Appearance" · **Nível:** normativa (laboratório emissor da escala)
**Confiança:** confirmado
**Também aparece em:** flashcards e questionário do módulo — gerados **depois** desta correção, já com o valor certo.

### 🟠 2. Densidade relativa da turquesa com limite inferior fora da faixa GIA

**claim_id:** `GEM-TUR-001`
**Tipo:** impreciso (valor fora da faixa aceita)
**Onde:** aula 16 · "Turquesa" e Recap
**Estava escrito:** "densidade relativa entre 2,3 e 2,9"; "Índice de refração de ponto próximo de 1,61"
**Problema:** o GIA publica DR 2,76 com tolerância +0,14 / −0,36, isto é, de 2,40 a 2,90. O limite inferior de 2,3 é mais baixo que o publicado. O índice de refração é uma faixa (1,610–1,650), não um valor único.
**Correção aplicada:** "densidade relativa de referência 2,76, com variação de cerca de 2,40 a 2,90 [...] Índice de refração de ponto entre 1,61 e 1,65."
**Fonte:** GIA Gem Encyclopedia — Turquoise, *gem overview* · **Nível:** base de referência normativa
**Confiança:** confirmado
**Também aparece em:** nenhum outro arquivo do curso.

### 🟠 3. O grau de lapidação GIA foi descrito de forma vaga

**claim_id:** `GEM-PROP-003`
**Tipo:** omissão que gera erro
**Onde:** aula 12 · "As proporções do brilhante redondo"
**Estava escrito:** "ele avalia o resultado visual, mais o acabamento, mais a durabilidade do desenho"
**Problema:** a formulação sugeria três componentes vagos. O sistema GIA é explícito: **sete** componentes, divididos entre aparência e execução. Sem essa lista, o aluno não consegue ler um relatório nem entender por que uma pedra com proporções dentro da faixa pode não receber Excelente.
**Correção aplicada:** "o sistema avalia **sete componentes** — três de aparência (brilho, fogo e cintilação) e quatro de projeto e execução (razão de peso, durabilidade, polimento e simetria)". Precisado também que o grau se aplica ao brilhante redondo **padrão** na faixa D–Z.
**Fonte:** GIA 4Cs, *Diamond Cut — Understanding the Cut Scale*; GIA, *Cut Grading System Charts and Booklets* · **Nível:** normativa
**Confiança:** confirmado
**Também aparece em:** módulo 02, aula 09 (lapidação do diamante) — gerada depois, já com a formulação correta.

### 🟠 4. Faixa de densidade do coríndon truncada no limite superior

**claim_id:** `GEM-DR-005`
**Tipo:** impreciso
**Onde:** aula 07 · tabela "Faixas de referência"
**Estava escrito:** "Coríndon | 3,95–4,05"
**Problema:** o valor de referência GIA para coríndon é 4,00 com tolerância +0,10 / −0,05, ou seja, até 4,10. A tabela cortava a faixa em 4,05 e podia levar o aluno a considerar incompatível uma leitura legítima de 4,08.
**Correção aplicada:** "Coríndon | 3,95–4,10 (referência 4,00)".
**Fonte:** GIA Gem Encyclopedia — Corundum/Sapphire, *gem overview*; Mindat · **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** aula 09, tabela de simulantes (safira incolor, DR 4,00) — consistente, sem alteração necessária.

### 🟠 5. Aparente contradição entre as duas tabelas de densidade do zircão

**claim_id:** `GEM-SIM-004`
**Tipo:** inconsistência interna
**Onde:** aula 07 (tabela de referência: zircão 3,90–4,73) e aula 09 (tabela de simulantes: zircão incolor 4,6–4,7)
**Problema:** as duas faixas são corretas, mas descrevem coisas diferentes — a primeira cobre o zircão inteiro, incluindo o material metamíctico, danificado por radiação, de densidade baixa; a segunda descreve o zircão de "tipo alto", que é o usado como simulante. Sem essa distinção declarada, o material se contradiz aos olhos do aluno.
**Correção aplicada:** a linha da aula 09 passou a dizer "Zircão incolor (tipo alto)", e o exemplo trabalhado ganhou a explicação da diferença entre zircão de tipo alto e metamíctico, com referência explícita à tabela da aula 07.
**Fonte:** GIA Gem Encyclopedia — Zircon; Mindat — zircão e metamictização · **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** nenhum outro arquivo.

## Verificado e correto

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `GEM-NOM-001` | Esmeralda é variedade de berilo; ametista é variedade de quartzo | Mindat; IMA-CNMNC | confirmado |
| `GEM-NOM-002` | "Jade" designa nefrita, jadeíta e, sob critérios definidos, onfacita verde | CIBJO Gemmological Laboratories Blue Book 2024; GIA Jade | confirmado |
| `GEM-COR-001` | No coríndon, Cr³⁺ associa-se a rosa/vermelho e o par Fe²⁺–Ti⁴⁺ a azul | GIA, G&G Spring 2020, corundum chromophores | confirmado |
| `GEM-ID-001` | Refratômetro, polariscópio, dicroscópio e espectroscópio integram o conjunto padrão GIA | GIA Gem Identification | confirmado |
| `GEM-INST-001` | Refratômetro com líquido de contato e polariscópio no equipamento básico | GIA Gem Identification | confirmado |
| `GEM-INST-002` | Dicroscópio, lupa 10×, espectroscópio e microscópio no equipamento de identificação | GIA Gem Identification | confirmado |
| `GEM-FLUXO-001` | Testes padrão como base, com testes avançados conforme necessário | GIA, Analysis of Gemstones (2024) | confirmado |
| `GEM-DR-001` | Densidade relativa é razão adimensional entre a massa do material e a de igual volume de água | GIA; Gem-A | confirmado |
| `GEM-DR-002` | DR = P(ar) ÷ [P(ar) − P(água)] | princípio de Arquimedes; GIA Gem Identification | confirmado |
| `GEM-DR-003` | Bromofórmio ≈ 2,89; di-iodometano ≈ 3,32; solução de Clerici ≈ 4,15 | densidades tabeladas dos reagentes (CHBr₃ 2,89; CH₂I₂ 3,325 g/cm³); literatura gemológica | confirmado |
| `GEM-DR-004` | A solução de Clerici contém sais de tálio, é altamente tóxica e caiu em desuso | fichas de segurança de compostos de tálio; Gem-A | confirmado |
| `GEM-DR-006` | Diamante 3,52; topázio 3,49–3,57; quartzo 2,65; berilo 2,67–2,90; opala 1,98–2,25; âmbar 1,05–1,09 | GIA Gem Encyclopedia | confirmado |
| `GEM-UV-001` | Onda longa ≈ 365 nm; onda curta ≈ 254 nm | GIA Gem Identification; especificação de lâmpadas de mercúrio | confirmado |
| `GEM-UV-003` | GIA registra fluorescência em cinco níveis, como identificação e não como qualidade | GIA, Diamond Fluorescence | confirmado |
| `GEM-UV-004` | Sintéticos de fusão em chama mostram luminescência de aspecto giz sob onda curta | GIA Gem Identification | confirmado |
| `GEM-UV-005` | Fluorescência vermelha no rubi vem do cromo e é atenuada por ferro | GIA, G&G corundum chromophores | confirmado |
| `GEM-COND-001` | O diamante tem a maior condutividade térmica entre materiais maciços à temperatura ambiente | GIA; física de materiais | confirmado |
| `GEM-COND-002` | Moissanita aciona o testador térmico, o que motivou o teste de condutividade elétrica | GIA, G&G Summer 1997, Synthetic moissanite | confirmado |
| `GEM-COND-003` | Diamante tipo IIb contém boro, é semicondutor e pode ser lido como moissanita | GIA, diamond type classification | confirmado |
| `GEM-SIM-001` | RI: diamante 2,417; moissanita 2,648–2,691; CZ 2,15–2,18; YAG 1,833; GGG 1,970 | GIA Gem Encyclopedia; literatura de simulantes | confirmado |
| `GEM-SIM-002` | Dispersão: diamante 0,044; moissanita 0,104; CZ ≈0,060; YAG 0,028; GGG 0,045 | GIA; literatura de simulantes | confirmado |
| `GEM-SIM-003` | Moissanita tem birrefringência ≈0,043 e duplica facetas; diamante é isotrópico | GIA, G&G Summer 1997 | confirmado |
| `GEM-SIM-005` | CZ tem DR 5,6–6,0; GGG tem DR 7,05; YAG tem DR ≈4,55 | literatura de simulantes sintéticos | confirmado |
| `GEM-LAB-001` | Tipos Ia/Ib/IIa/IIb são determinados por FTIR, pela agregação do nitrogênio | GIA, Laboratory-Grown Diamond Identification | confirmado |
| `GEM-LAB-002` | Preenchimentos orgânicos produzem bandas em ~2800–3000 cm⁻¹ | GIA; literatura de FTIR aplicada a jadeíta e esmeralda | confirmado |
| `GEM-LAB-003` | A linha em 415 nm (centro N3) é indício de diamante natural | GIA, G&G; ZPL do N3 em 415 nm | confirmado |
| `GEM-LAB-004` | PL é medida a frio; a feição em ~737 nm associada ao silício indica CVD | GIA, Laboratory-Grown Diamond Identification | confirmado |
| `GEM-LAB-005` | LA-ICP-MS mede traços em ppm/ppb, sustenta origem e deixa microcrateras | GIA, Analysis of Gemstones (2024) | confirmado |
| `GEM-CUT-001` | Partes: mesa, coroa, cintura, pavilhão e cúlete | GIA, Anatomy of a diamond | confirmado |
| `GEM-CUT-002` | Brilhante redondo padrão: 57 facetas, 58 com cúlete facetado | GIA, Diamond Cut | confirmado |
| `GEM-PROP-001` | Ângulo crítico: diamante ≈24,4°; coríndon ≈34,6°; quartzo ≈40,4° | cálculo arcsen(1/n) sobre índices GIA | confirmado |
| `GEM-PROP-002` | Brilhante redondo: mesa 53–58%; coroa 34–35°; pavilhão 40,6–41,0°; profundidade 59–62,5% | GIA, Diamond Cut; G&G Fall 2004, cut grading | confirmado |
| `GEM-FEN-002` | Asterismo de seis raios no coríndon vem de rutilo em três direções a 120° | GIA, Sapphire quality factors | confirmado |
| `GEM-FEN-007/008` | Jogo de cores por difração em esferas de sílica; 150 nm para violeta/azul, ~350 nm para vermelho | Jones, Sanders & Segnit, *Nature* 204 (1964); GIA Opal quality factors | confirmado |
| `GEM-FEN-009/010` | Mudança de cor depende da fonte; pleocroísmo depende da direção | GIA, Alexandrite quality factors; GIA Gem Identification | confirmado |
| `GEM-JADE-001/002/003` | Duas espécies sob um nome; Damour 1863; RI e DR de nefrita e jadeíta; nefrita não é espécie IMA | GIA Jade; IMA-CNMNC; Mindat | confirmado |
| `GEM-JADE-004/005/006` | Sistema A/B/C; FTIR em 2800–3000 cm⁻¹; linha 437 nm e banda ~650 nm | GIA, "What is B jade?"; literatura de jadeíta | confirmado |
| `GEM-OPA-001/002/003` | Opala: RI 1,37–1,47; DR 1,98–2,25; hidrofânica etíope; opala de fogo é cor de corpo | GIA Opal quality factors; G&G sobre opala etíope | confirmado |
| `GEM-LAP-001` | Lápis-lazúli é rocha (lazurita + calcita + pirita); Sar-e-Sang é a fonte histórica | GIA Lapis lazuli; Mindat | confirmado |
| `GEM-MAL-001` | Malaquita: dureza 3,5–4; DR 3,6–4,0; reage a ácidos | Mindat; GIA | confirmado |
| `GEM-DUR-001/002/003/004/005` | Três componentes de durabilidade; Mohs ordinal; clivagem octaédrica do diamante; lista de proibições de ultrassom; quartzo na poeira | GIA, Gemstone durability; GIA, Gem care and cleaning | confirmado |
| `GEM-MET-001/002/003/004/005` | Teores de ouro; regulação Inmetro; densidades Pt 21,4 / Au 19,3 / Ag 10,5; ródio; prata 925 | CIBJO Precious Metals Blue Book; Inmetro; Mindat | confirmado |
| `GEM-GEO-001…006` | Pegmatitos e elementos incompatíveis; transporte por kimberlito e basalto alcalino; esmeralda de xisto; rubi em mármore; jadeíta em subducção; placers | GIA, Where do gems come from?; G&G, Emerald deposits classification | confirmado |
| `GEM-BR-002/003` | Turmalina Paraíba: Mina da Batalha, elbaíta cuprífera, mercado ~1990; hoje nome de variedade independente de origem | GIA, G&G Fall 2008, Paraíba-type copper-bearing tourmaline; LMHC Information Sheet | confirmado |
| `GEM-BR-004` | Topázio imperial de Ouro Preto, sem equivalente conhecido em outra localidade | CPRM/SGB; GIA Gem Encyclopedia | confirmado |
| `GEM-BR-005` | Ametista do Sul (RS) é o maior distrito produtor de ametista do mundo, em geodos da Formação Serra Geral | IBRAM; literatura geológica sobre gemas do RS; CPRM/SGB | confirmado |
| `GEM-BR-006` | Ringwoodita natural identificada em inclusão de diamante superprofundo de Juína (MT) | Pearson et al., *Nature* 507 (2014) | confirmado |
| `GEM-BR-007` | Dom Pedro, de material de Pedra Azul (MG), é a maior água-marinha lapidada do mundo | Smithsonian NMNH | confirmado |
| `GEM-MKT-001/002/004` | Kimberley em vigor desde 2003, só bruto; definição restrita a movimentos rebeldes; Rapaport semanal desde 1978 | Kimberley Process; Rapaport | confirmado |
| `GEM-MKT-003` | As tentativas de ampliar a definição de diamante de conflito fracassaram em ciclos sucessivos, pela regra do consenso | Kimberley Process Civil Society Coalition; cobertura dos plenários 2023–2026 | confirmado |
| `GEM-REPORT-001/002/003` | Serviços de relatório GIA; LMHC harmoniza terminologia; "nenhum tratamento detectado" declara o limite do exame | GIA Colored Stone Reports; LMHC; CIBJO Blue Book 2024 | confirmado |
| `GEM-ORIGIN-001` | O GIA descreve país de origem como opinião de especialista | GIA, Country of origin and expert opinion | confirmado |

## Correções aplicadas

**Aplicadas em:** 2026-08-24

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `GEM-UV-002` | 🟠 | Corrigido | 01-gemologia-geral-aula-09-fluorescencia-uv-onda-longa-e-onda-curta.md |
| `GEM-TUR-001` | 🟠 | Corrigido | 01-gemologia-geral-aula-17-opala-turquesa-lapis-lazuli-e-outros-opacos.md |
| `GEM-PROP-003` | 🟠 | Corrigido | 01-gemologia-geral-aula-13-proporcoes-desempenho-optico-e-defeitos-de-lapidacao.md |
| `GEM-DR-005` | 🟠 | Corrigido | 01-gemologia-geral-aula-08-densidade-relativa-e-liquidos-pesados.md |
| `GEM-SIM-004` | 🟠 | Corrigido | 01-gemologia-geral-aula-10-condutividade-termica-eletrica-e-simulantes.md |

**Pendências:** nenhuma. Como o questionário e o baralho deste módulo foram regerados **depois** desta auditoria, não houve propagação para material derivado com valores antigos.

---

## Passagem adicional — 2026-08-27: alegações novas das aulas 01–06

**Modo:** audit-and-fix · **Profundidade:** full
**Escopo:** as alegações acrescentadas às aulas 01–06 no aprofundamento de 2026-08-25 (`GEM-NOM-003`–`009`, `GEM-COR-002`–`009`, `GEM-DIAG-001`–`008`, `GEM-OPT-001`–`009`, `GEM-OBS-001`–`008`, `GEM-FLUXO-002`–`006`), que não existiam na auditoria de 2026-08-24 — pendência 2 do `_contexto.md`.
**Método:** revisão contra Gem-A *Gemmology Foundation*, GIA *Gem Encyclopedia*, Mindat e IMA-CNMNC, com buscas web dirigidas em 2026-08-27 (faixa de IR do grupo das granadas; IR/DR de berilo, espinélio e moissanita; sinal óptico de coríndon/berilo/quartzo; citação do mecanismo de cor da opala).
**Veredito:** **Aprovado com correções**

### Resumo

🔴 0 · 🟠 1 · 🟡 1 · 🔵 0 · ⚪ 0. Verificadas e corretas: **38 alegações**. As duas correções foram aplicadas nesta mesma rodada.

### 🟠 1. A faixa de IR das granadas exclui a andradita e o demantoide

**claim_id:** `GEM-DIAG-004`
**Tipo:** confusão de escopo
**Onde:** aula 03, tabela de valores de referência de materiais isotrópicos; reaparece no exemplo trabalhado da aula 04
**Está escrito:** "| Granadas (grupo) | 1,714–1,830 | — | isotrópico | 3,4–4,3 |"
**Problema:** 1,830 é o máximo da **almandina**, não do grupo. A **andradita** e sua variedade gema **demantoide** — a granada verde mais valorizada — alcançam cerca de **1,88–1,895**. Como escrita, a faixa faria um gemólogo rejeitar uma leitura legítima de demantoide (~1,885) como "não é granada". O limite inferior de densidade (3,4) também está abaixo de qualquer granada de gema (o mínimo real é ~3,5, grossulária).
**Correção aplicada:** faixa de IR → **1,714–1,888** (grupo, do piropo à andradita/demantoide); densidade → **3,5–4,3**. Aplicado na tabela da aula 03, no rodapé de alegações da aula 03 e na frase do exemplo trabalhado da aula 04.
**Fonte:** GIA, *A Proposed New Classification for Gem-Quality Garnets*; Mindat, grupo das granadas; Webster, *Gems*. · **Nível:** base de referência · **Confiança:** confirmado
**Também aparecia em:** `01-gemologia-geral-aula-04-refratometro-e-polariscopio.md`. Nenhum flashcard ou questão cita a faixa de IR das granadas.

### 🟡 2. O mecanismo de cor da opala é atribuído ao artigo errado do par de 1964

**claim_id:** `GEM-COR-006`
**Tipo:** desatualização / imprecisão de citação
**Onde:** aula 02, seção de cor por efeito físico; lista de fontes; rodapé de alegações
**Está escrito:** "O mecanismo foi estabelecido por Jones, Sanders e Segnit em 1964." / fonte: "Jones, Sanders & Segnit, *Structure of Opal*, Nature 204, 990–991 (1964)"
**Problema:** o artigo de Jones, Sanders & Segnit (*Structure of Opal*, Nature 204:990–991) trata do **arranjo de esferas**. O mecanismo de **difração da cor** foi demonstrado num artigo distinto do mesmo volume: **J. V. Sanders, "Colour of Precious Opal", Nature 204:1151–1153 (1964)**. A afirmação e a fonte não estavam erradas quanto ao volume e ao ano, mas atribuíam o mecanismo de cor ao artigo de estrutura.
**Correção aplicada:** corpo e rodapé da aula 02 passam a separar as duas contribuições; a lista de fontes ganhou o artigo de Sanders (1964); os campos de fonte dos flashcards da opala (`fb081`, `fb082`, `fc040`, `flashcards.md`) foram atualizados. O conteúdo de todos os cards já estava correto — só a citação foi ajustada.
**Fonte:** Sanders, *Colour of Precious Opal*, Nature 204, 1151–1153 (1964); Jones, Sanders & Segnit, *Structure of Opal*, Nature 204, 990–991 (1964). · **Nível:** revisada por pares · **Confiança:** confirmado

### Verificado e correto (amostra do que passou)

- **Faixas de IR e DR** de quartzo, berilo, topázio, turmalina, peridoto, coríndon, fluorita, espinélio, CZ, diamante e moissanita — coerentes com Gem-A e GIA.
- **Ângulos críticos** (diamante ~24,4°, coríndon ~34,6°, quartzo ~40,4°) — conferem com arcsen(1/n).
- **Classes ópticas por sistema cristalino** e **sinais ópticos** (coríndon e berilo negativos, quartzo positivo).
- **Lei de Snell**, ângulo crítico e mecanismo do refratômetro de bancada (líquido de di-iodometano com enxofre, n≈1,81).
- **Centros de cor da ametista**, rota ametista→citrino por aquecimento; idiocromático / alocromático / pseudocromático; transferência de carga vs. campo cristalino; faixa visível ~380–780 nm.
- **Nomenclatura IMA** (variedade não é categoria IMA; granada e turmalina são grupos), reserva de "sintético", misnomers (topázio-fumê, diamante Herkimer), recomendação da CIBJO contra "pedra semipreciosa", definição de jade (nefrita / jadeíta / onfacita).
- **ADR** em granada, espinélio, vidro e âmbar; efeito de flash; escopo de laudo; as cinco perguntas do ofício e a origem geográfica como opinião comparativa.

### Correções aplicadas — 2026-08-27

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `GEM-DIAG-004` | 🟠 | Corrigido | aula-03, aula-04 |
| `GEM-COR-006` | 🟡 | Corrigido | aula-02, flashcards-basic.csv, flashcards-cloze.csv, flashcards.md |

**Propagação:** o questionário e o baralho do módulo 01 foram verificados quanto aos dois fatos. Nenhuma questão depende da faixa de IR das granadas nem da autoria do artigo da opala; nenhum verso de flashcard estava errado (só o campo de fonte de quatro cards da opala, ajustado). Se o baralho já foi importado no Anki, a reimportação atualiza apenas o campo de fonte desses quatro cards — nenhum precisa ser refeito à mão.

**Pendências:** nenhuma. A pendência 2 do `_contexto.md` fica encerrada.

## Observação didática (fora do escopo desta auditoria)

O módulo tem 22 aulas e é o maior do curso. A carga por aula respeita o teto de 1.600 palavras do contrato de nível, mas o volume total sugere que a revisão didática confira se os três blocos declarados no hub são de fato pontos naturais de parada. Isso é matéria do `revisor-didatico`, não desta auditoria.
