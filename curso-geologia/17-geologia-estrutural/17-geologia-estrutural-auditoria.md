# Auditoria científica: Módulo 17 — Geologia estrutural e deformação

**Auditado em:** 2026-08-18
**Material:** `17-geologia-estrutural/` — seis aulas, questionário final e os três arquivos de flashcards
**Modo:** audit-and-fix
**Profundidade:** full
**Escopo:** stress e strain, regimes rúptil e dúctil, anatomia e classificação de dobras e falhas, zonas de cisalhamento e indicadores cinemáticos, leitura de mapas e seções estruturais; consistência entre aulas e entre aula, questionário e baralho
**Reverificado em:** 2026-08-18 (segunda passada independente: os sete achados originais foram reconferidos contra fonte e no texto dos arquivos; um achado novo foi encontrado no questionário)
**Veredito final:** Aprovado com ressalva (todos os achados corrigidos; nenhum aberto)

## Resumo

🔴 1 erro · 🟠 6 imprecisões · 🟡 0 desatualizados · 🔵 0 sem fonte · ⚪ 1 controverso Verificadas e corretas: 21 alegações.

## Achados

### 🔴 1. O padrão em V de uma dobra com caimento foi apresentado com um único sentido

**claim_id:** `EST-M17-PLUNGE-VDIR-001`
**Tipo:** erro factual
**Onde:** aula 03 · "Classificação pelo caimento do eixo" e recap · aula 06 · "Como dobras aparecem em mapa: a regra do V" e recap
**Está escrito:** "Esse tipo de dobra produz, num mapa geológico, um padrão característico em forma de 'V' ou ferradura apontando na direção do caimento" (aula 03) e "com a ponta do V apontando na direção do caimento do eixo" (aula 06).
**Problema:** a regra vale apenas para **anticlinais e antiformes**. Num **sinclinal ou sinforme com caimento** o padrão se inverte: a estrutura **se abre** na direção do caimento, e a ponta do V aponta no sentido **oposto**. Como a afirmação está escrita de forma geral para "dobras com caimento", ela é falsa em metade dos casos — e é exatamente o tipo de erro que faz o aluno inverter a leitura de um mapa. Agrava-se por a aula 06 apresentar o padrão como "esse mesmo princípio" da regra do V para camadas, que é um fenômeno geométrico distinto.
**Correção proposta:** separar os dois sentidos explicitamente (anticlinal/antiforme → V na direção do caimento; sinclinal/sinforme → V no sentido oposto) e desfazer a fusão com a regra do V de camadas.
**Fonte:** *Basics — Geologic Structures*, Wenatchee Valley College, [commons.wvc.edu](https://commons.wvc.edu/rdawes/Basics/structures.html), consultado em 2026-08-18; *Outcrop Patterns*, University of Oregon, [pages.uoregon.edu](https://pages.uoregon.edu/millerm/Srpatterns.html); *Overview of Folds, Faults, and Unconformities*, BCcampus Lab Manual for Earth Science (2021) · **Nível:** base de referência (convergente com Fossen 2016, cap. 11)
**Confiança:** confirmado
**Também aparece em:** nenhum flashcard e nenhuma questão cobravam o sentido do V em dobra com caimento — a correção ficou contida nas aulas 03 e 06.

### 🟠 2. A regra do V foi ensinada com uma única exceção, e falta justamente a que inverte o sentido

**claim_id:** `EST-M17-VRULE-EXCEPT-002`
**Tipo:** omissão que gera erro
**Onde:** aula 06 · vocabulário, "Como dobras aparecem em mapa", exemplo trabalhado, erros comuns e recap
**Está escrito:** "o 'V' aponta na direção em que a camada mergulha (a exceção ocorre quando o mergulho da camada é exatamente igual, e no mesmo sentido, à declividade do vale — uma situação mais rara)."
**Problema:** a regra do V tem três exceções, não uma. Faltam (a) a camada **vertical**, que não forma V, e sobretudo (b) a camada que mergulha **vale abaixo com ângulo menor que a declividade do vale**, em que o V **se forma apontando no sentido contrário ao mergulho**. Essa última não é uma curiosidade: é o caso em que aplicar a regra como ensinada produz a resposta exatamente invertida. Falta também o critério prático que separa os casos — a cota da ponta do V em relação às bordas do traço.
**Correção proposta:** enumerar as três exceções e acrescentar a checagem de cota (ponta do V mais baixa que as bordas → mergulho no sentido do V; mais alta → sentido contrário).
**Fonte:** *The Rule of Vs in geological mapping*, Geological Digressions, [geological-digressions.com](https://www.geological-digressions.com/the-rule-of-vs-in-geological-mapping/), consultado em 2026-08-18; *9.3 Estimating Dip Direction from a Geological Map*, A Practical Guide to Introductory Geology (Open Education Alberta, 2021) · **Nível:** base de referência (convergente com Rowland et al. 2007, cap. 2)
**Confiança:** confirmado
**Também aparece em:** questionário — enunciado e gabarito de **A4**, gabarito de **D3**; flashcards — `geologia-m17-fb046` e `geologia-m17-fc030`.

### 🟠 3. "Eixo da dobra" foi definido como a linha que é, na verdade, a charneira

**claim_id:** `EST-M17-FOLDAXIS-DEF-003`
**Tipo:** imprecisão de nomenclatura
**Onde:** aula 03 · vocabulário, "Anatomia de uma dobra", erros comuns e recap
**Está escrito:** "**Eixo da dobra** — a linha formada pela interseção entre o plano axial e a superfície dobrada específica que você está observando."
**Problema:** essa interseção é a **charneira** daquela superfície — que a própria aula já define duas linhas acima, criando dois nomes para a mesma coisa sem dizê-lo. O eixo da dobra, no uso corrente da geologia estrutural, é a **linha reta que, deslocada paralelamente a si mesma, gera a forma da dobra**, e só é definido em dobras **cilíndricas** (charneira retilínea); dobras de charneira curva não têm eixo único e são tratadas como sucessão de trechos cilíndricos. A definição dada apaga essa restrição, que é justamente o que torna o conceito útil em análise estereográfica.
**Correção proposta:** definir eixo como a linha geradora, paralela à charneira, válida em dobras cilíndricas, mantendo o contraste com o plano axial que a aula já faz bem.
**Fonte:** *Folds*, em Waldron & Snyder, *Geological Structures: a Practical Introduction*, [geo.libretexts.org](https://geo.libretexts.org/Bookshelves/Geology/Geological_Structures_-_A_Practical_Introduction_(Waldron_and_Snyder)/01:_Topics/1.05:_Folds), consultado em 2026-08-18; ETH Zürich, *Folds — basic geometrical definitions*, [files.ethz.ch](https://www.files.ethz.ch/structuralgeology/JPB/files/English/8folds.pdf) · **Nível:** base de referência (convergente com Fossen 2016, cap. 11)
**Confiança:** confirmado
**Também aparece em:** questionário — gabarito de **V2**; flashcards — `geologia-m17-fb020` e `geologia-m17-fc011`. A resposta de V2 continua "Falso"; só a justificativa mudou.

### 🟠 4. Porfiroclasto delta descrito como tendo caudas curvadas "do jeito oposto"

**claim_id:** `EST-M17-DELTA-CLAST-004`
**Tipo:** imprecisão que induz a conclusão errada
**Onde:** aula 05 · "Como saber para que lado a zona de cisalhamento se moveu"
**Está escrito:** "formas em 'sigma' (σ, com caudas que se curvam de um jeito) ou 'delta' (δ, com caudas que se curvam do jeito oposto e cruzam o plano central do grão)."
**Problema:** "se curvam do jeito oposto" sugere que σ e δ apontariam **sentidos de cisalhamento opostos** — e é justamente o erro que um aluno cometeria diante de uma lâmina. Os dois tipos indicam o **mesmo** sentido; o que os distingue é a geometria das caudas em relação a uma linha de referência traçada pelo centro do grão, paralela à foliação: no tipo σ as linhas medianas das caudas ficam de lados opostos dessa linha **sem cruzá-la**; no tipo δ as caudas envolvem o grão e **cruzam** a linha. O que lê o sentido é o degrau (*stair-stepping*) das caudas, não o lado para o qual elas "curvam".
**Correção proposta:** substituir a descrição por uma que use a linha de referência e declarar explicitamente que os dois tipos indicam o mesmo sentido.
**Fonte:** Passchier, C. W. & Simpson, C. (1986), "Porphyroclast systems as kinematic indicators", *Journal of Structural Geology*, [tekphys.geo.uni-mainz.de](https://www.tekphys.geo.uni-mainz.de/publications_PDF/12-PasschierSimpson86.pdf), consultado em 2026-08-18; *Ductile shear sense indicators*, Structure Database · **Nível:** revisada por pares (base original da distinção σ/δ, retomada em Passchier & Trouw 2005, cap. 7)
**Confiança:** confirmado
**Também aparece em:** flashcards — `geologia-m17-fb040` e `geologia-m17-fc025`.

### 🟠 5. Zona de cisalhamento apresentada como "resultado de falhas profundas", contradizendo os erros comuns da mesma aula

**claim_id:** `EST-M17-SHEARZONE-ORIGIN-005`
**Tipo:** inconsistência interna
**Onde:** aula 05 · "A mesma ideia de deslocamento, respondida de outro jeito" (fecho da analogia)
**Está escrito:** "Zonas de cisalhamento são, na prática, o resultado de falhas profundas cuja deformação, em vez de se concentrar numa única superfície, se espalha por uma faixa de rocha inteira."
**Problema:** a zona de cisalhamento dúctil não é *produzida por* uma falha; falha rúptil e zona de cisalhamento dúctil são os dois extremos de um **contínuo** de estruturas que acomodam deslocamento, e a mesma estrutura tectônica muda de caráter com a profundidade. Além de inverter a relação causal, a frase contradiz frontalmente o bullet de "erros comuns" da própria aula, que adverte contra tratar zona de cisalhamento como "uma falha muito larga" — o material afirma as duas coisas sem que o aluno tenha como saber qual vale.
**Correção proposta:** reescrever no enquadramento de contínuo, preservando a analogia do gelo e da massa que já funcionava.
**Fonte:** Fossen, H. & Cavalcante, G. C. G. (2017), "Shear zones — A review", *Earth-Science Reviews*; *Shear Zones*, em Waldron & Snyder, *Geological Structures: a Practical Introduction*, [pressbooks.openeducationalberta.ca](https://pressbooks.openeducationalberta.ca/introductorystructuralgeology/chapter/m-shear-zones/), consultado em 2026-08-18 · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** nenhum arquivo derivado — o card `geologia-m17-fb035` e o gabarito de **D2(a)** já usavam o enquadramento correto.

### 🟠 6. O deslocamento dos cavalgamentos foi limitado a "dezenas de quilômetros"

**claim_id:** `EST-M17-THRUST-DISP-006`
**Tipo:** imprecisão de magnitude
**Onde:** aula 04 · "Falha reversa e de cavalgamento: quando o teto sobe"
**Está escrito:** "empurrando rochas mais antigas por cima de rochas mais jovens ao longo de distâncias que podem chegar a dezenas de quilômetros."
**Problema:** o teto de "dezenas de quilômetros" subestima em uma ordem de grandeza justamente os exemplos que a frase acabou de citar. O Main Central Thrust, no Himalaia, tem deslocamento mínimo estimado em ~116 km numa seção balanceada no Nepal central, e o encurtamento total do cinturão himalaiano é da ordem de centenas de quilômetros. A frase não é falsa como afirmação de possibilidade, mas ensina uma escala errada para o fenômeno.
**Correção proposta:** dar a faixa real (de poucos quilômetros a mais de uma centena nos maiores) e ancorar com o exemplo do Main Central Thrust.
**Fonte:** DeCelles et al., seções balanceadas do Himalaia central (síntese em *Main Central Thrust*, com deslocamento mínimo de 116 km na seção do rio Budhi-Gandaki), consultado em 2026-08-18; Wiesmayr & Grasemann (2002), *Tectonics*, encurtamento total do cinturão de dobras e cavalgamentos · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** recap da aula 04. Nenhum flashcard ou questão cobrava a magnitude.

### ⚪ 7. O corte de 30° para cavalgamento foi apresentado como definição fechada

**claim_id:** `EST-M17-THRUST-ANGLE-007`
**Tipo:** controvérsia apresentada como consenso
**Onde:** aula 04 · vocabulário, "Falha reversa e de cavalgamento", erros comuns e recap
**Está escrito:** "**Falha de cavalgamento (thrust)** | Uma falha reversa de baixo ângulo (tipicamente menos de ~30°)".
**Problema:** o limite numérico não é uniforme entre fontes do mesmo nível. Boa parte da literatura estrutural usa **<30°**, enquanto o *Glossary of Geology* (AGI), o uso corrente do USGS e a Britannica definem cavalgamento como falha reversa com mergulho de **45° ou menos**. O material adota um dos dois sem sinalizar que existe o outro, e o aluno que encontrar a definição de 45° numa fonte oficial vai concluir que a aula está errada.
**Correção proposta:** manter 30° como convenção do módulo, declarando que parte das referências usa 45° ou menos e que o consensual é o caráter de baixo ângulo, não o número de corte.
**Fonte:** Neuendorf, Mehl & Jackson (eds.), *Glossary of Geology*, AGI — verbete "thrust fault" (dip 45° ou menos); *Thrust fault*, Encyclopædia Britannica, [britannica.com](https://www.britannica.com/science/thrust-fault), consultado em 2026-08-18; contraposto a Fossen 2016, cap. 9, e Davis, Reynolds & Kluth 2012, cap. 8 (<30°) · **Nível:** base de referência versus base de referência — divergência real
**Confiança:** em disputa
**Também aparece em:** questionário — enunciado e gabarito de **9**; flashcards — `geologia-m17-fb031` e `geologia-m17-fc019`. A questão 9 continua válida: nenhum distrator virou resposta correta, porque a alternativa certa é o **termo**, não o ângulo.

### 🟠 8. A matriz de cobertura do questionário aponta para cinco questões que não existem, e a contagem declarada não bate com o conteúdo

**claim_id:** `EST-M17-QUIZ-COVERAGE-029`
**Tipo:** inconsistência interna
**Onde:** questionário final · cabeçalho e "Matriz de cobertura"
**Está escrito:** "**Questões:** 19 · **Pontuação total:** 44 pontos", "**Nota de corte sugerida:** 31/44 (70%)" e as linhas de matriz "`oa04` (parte 2 [...]) | 11, 12, V4, D2(a) | 6" e "`oa05` [...] | 13, 14, 15, A4, D2(b), D3 | 9".
**Problema:** a Parte I termina na questão **10** — as questões **11, 12, 13, 14 e 15** citadas pela matriz não existem no arquivo, e o gabarito comentado também só cobre de 1 a 10. O conteúdo real são **21 questões somando 39 pontos** (14 na Parte I + 4 na Parte II + 8 na Parte III + 13 na Parte IV), não 19 questões e 44 pontos. Como consequência, a nota de corte 31/44 é calculada sobre um total inexistente, e a linha de níveis cognitivos (8+8+3 = 19) descreve um questionário diferente do que está no arquivo. A matriz também atribuía **D2(b)** ao `oa05`, quando o subitem trata de zona de cisalhamento (`oa04` parte 2). Não é erro científico: é o material contradizendo a si mesmo, e o efeito prático é o aluno se autoavaliar contra um denominador errado.
**Correção proposta:** reconciliar cabeçalho, nota de corte e matriz com o conteúdo efetivamente presente, reatribuir D2(b) ao objetivo correto e registrar a lacuna de cobertura em vez de inventar as cinco questões ausentes.
**Fonte:** o próprio material — contagem direta dos itens e dos pesos declarados no questionário, conferida contra o gabarito comentado · **Nível:** verificação interna
**Confiança:** confirmado
**Também aparece em:** hub do módulo (`17-geologia-estrutural-modulo.md`), que repetia "19 questões, 44 pontos".

## Verificado e correto

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `EST-M17-STRESS-DEF-008` | Stress é força por área, medido em Pa/MPa; strain é adimensional. | Fossen 2016, cap. 2; van der Pluijm & Marshak 2004, cap. 3 | confirmado |
| `EST-M17-TENSOR-009` | O estado de stress num ponto é um tensor com três tensões principais perpendiculares, ordenadas σ1 ≥ σ2 ≥ σ3. | Fossen 2016, cap. 2 | confirmado |
| `EST-M17-STRESS-TYPES-010` | Compressivo encurta, distensivo alonga, cisalhante desliza paralelo ao plano de contato. | Davis, Reynolds & Kluth 2012, cap. 2 | confirmado |
| `EST-M17-ELASTIC-PERM-011` | Deformação elástica é reversível (ondas sísmicas); a permanente é a que fica registrada. | Fossen 2016, cap. 2 | confirmado |
| `EST-M17-STRAIN-EXAMPLE-012` | 500 m → 400 m corresponde a 20% de encurtamento (strain 0,2). | aritmética verificada contra a definição de strain longitudinal | confirmado |
| `EST-M17-BD-FACTORS-013` | Temperatura, pressão confinante, taxa de deformação e composição/fluidos controlam o regime; T e Pc altas e taxa lenta favorecem dúctil. | Fossen 2016, cap. 7 | confirmado |
| `EST-M17-BDT-DEPTH-014` | A transição rúptil-dúctil na crosta continental fica em torno de 10–15 km e ~300 °C, controlada pelo quartzo, e varia com o geotermo. | Axen (2024), *G-cubed*, transição rúptil-plástica a ~250–350 °C e ~10–20 km em crosta quartzosa; Hirth & Tullis (1994), *JGR* | confirmado |
| `EST-M17-QTZ-FSP-015` | O quartzo passa a fluir dutilmente em temperatura bem menor que o feldspato. | Hirth & Tullis (1994); Axen (2024) | confirmado |
| `EST-M17-JOINT-FAULT-016` | Junta é fratura sem deslocamento perceptível; falha é fratura com deslocamento. | Fossen 2016, cap. 9 | confirmado |
| `EST-M17-HW-FW-017` | Bloco de teto fica acima do plano inclinado, bloco de muro abaixo; a terminologia vem da mineração subterrânea. | Fossen 2016, cap. 9 | confirmado |
| `EST-M17-NORMAL-DIP-018` | Falha normal desce o teto, associa-se a distensão e mergulha tipicamente entre 45° e 70°. | distribuição observada de mergulhos de falhas normais (~40–70°, moda 51–57°); mecânica clássica prevê 60–65° | confirmado |
| `EST-M17-STRIKESLIP-019` | Transcorrente tem deslocamento horizontal paralelo à direção; dextral/sinistral pelo movimento aparente do bloco oposto, visto de cima. | Fossen 2016, cap. 9 | confirmado |
| `EST-M17-ANDERSON-020` | Anderson (1905), *Trans. Edinburgh Geol. Soc.* v. 8, p. 387, prevê ~60° para normais, ~30° para cavalgamentos e plano subvertical para transcorrentes. | Healy et al. (eds.), *Stress, faulting, fracturing and seismicity: the legacy of Ernest Masson Anderson*, GSL Special Publications 367 (2012) | confirmado |
| `EST-M17-ANTI-SYN-021` | Anticlinal tem as camadas mais antigas no núcleo e sinclinal as mais jovens; o critério é idade, não forma. | van der Pluijm & Marshak 2004, cap. 11 | confirmado |
| `EST-M17-ANTIFORM-022` | Antiforme/sinforme descrevem só a forma, usados quando a idade relativa é desconhecida ou não se aplica. | van der Pluijm & Marshak 2004, cap. 11 | confirmado |
| `EST-M17-OVERTURN-RECUMB-023` | Tombada tem um flanco invertido; recumbente tem plano axial aproximadamente horizontal. | Davis, Reynolds & Kluth 2012, cap. 6 | confirmado |
| `EST-M17-MYLONITE-024` | Milonito se forma por recristalização dinâmica em fluxo dúctil, ao contrário da brecha/cataclasito, de fragmentação rúptil. | Passchier & Trouw 2005, cap. 6 | confirmado |
| `EST-M17-SC-FABRIC-025` | Na fábrica S-C, S vem de *schistosité* (foliação contínua) e C de *cisaillement* (bandas mais paralelas à zona), e o ângulo entre elas dá o sentido. | Berthé, Choukroune & Jégouzo (1979); Passchier & Trouw 2005, cap. 7 | confirmado |
| `EST-M17-STRIKE-DIP-026` | Direção é a interseção da superfície com um plano horizontal; mergulho é a inclinação máxima, medida perpendicular à direção. Uma direção N30°E aponta 30° a leste do norte. | Rowland, Duebendorfer & Schiefelbein 2007, cap. 2 | confirmado |
| `EST-M17-APPARENT-DIP-027` | O mergulho aparente é sempre menor ou igual ao mergulho real. | Fossen 2016, cap. 3 | confirmado |
| `EST-M17-MAP-SYMBOLS-028` | Falha normal recebe hachuras/ticks no lado que desceu; cavalgamento recebe dentes de serra no lado do bloco de teto (upper plate). | FGDC, *Digital Cartographic Standard for Geologic Map Symbolization*, [ngmdb.usgs.gov](https://ngmdb.usgs.gov/fgdc_gds/geolsymstd/fgdc-geolsym-all.pdf), seção 2 | confirmado |

## Observações não factuais

- O baralho não tem card algum sobre o sentido do V em dobras com caimento — o ponto corrigido no achado 🔴 1 ficou sem cobertura de memorização. Não foi criado card novo aqui: criar cobertura é tarefa do `gerador-de-flashcards`, não da auditoria. Fica registrado para a próxima passada do baralho.
- A aula 06 fundia, sob "esse mesmo princípio", dois fenômenos geométricos distintos (regra do V de camadas e nariz de dobra com caimento). A fusão foi desfeita como parte do achado 🔴 1; se restar dificuldade de leitura no trecho, é assunto do `revisor-didatico`.
- Nenhuma contradição entre aulas foi encontrada além do achado 🟠 5, que era interno à aula 05.

---

## Correções aplicadas

**Aplicadas em:** 2026-08-18

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `EST-M17-PLUNGE-VDIR-001` | 🔴 | Corrigido | aula 03, aula 06 |
| `EST-M17-VRULE-EXCEPT-002` | 🟠 | Corrigido | aula 06, questionário final, flashcards-basic.csv, flashcards-cloze.csv |
| `EST-M17-FOLDAXIS-DEF-003` | 🟠 | Corrigido | aula 03, questionário final, flashcards-basic.csv, flashcards-cloze.csv |
| `EST-M17-DELTA-CLAST-004` | 🟠 | Corrigido | aula 05, flashcards-basic.csv, flashcards-cloze.csv |
| `EST-M17-SHEARZONE-ORIGIN-005` | 🟠 | Corrigido | aula 05 |
| `EST-M17-THRUST-DISP-006` | 🟠 | Corrigido | aula 04 |
| `EST-M17-THRUST-ANGLE-007` | ⚪ | Corrigido com ressalva (divergência declarada, nenhum lado escolhido) | aula 04, questionário final, flashcards-basic.csv, flashcards-cloze.csv |
| `EST-M17-QUIZ-COVERAGE-029` | 🟠 | Corrigido (metadados reconciliados com o conteúdo real; questões ausentes **não** inventadas) | questionário final, `17-geologia-estrutural-modulo.md` |

**Arquivos tocados nesta fase:** as seis aulas com achado (03, 04, 05, 06 — as aulas 01 e 02 passaram limpas), `17-geologia-estrutural-questionario-final.md`, `17-geologia-estrutural-flashcards.md`, `17-geologia-estrutural-flashcards-basic.csv`, `17-geologia-estrutural-flashcards-cloze.csv` e o hub `17-geologia-estrutural-modulo.md`.

**Cards com verso alterado:** `geologia-m17-fb020`, `geologia-m17-fb031`, `geologia-m17-fb040`, `geologia-m17-fb046`, `geologia-m17-fc011`, `geologia-m17-fc019`, `geologia-m17-fc025`, `geologia-m17-fc030`. Se o baralho já foi importado no Anki, reimportar o CSV **não** garante sobrescrever esses cards — confira ou remova esses IDs à mão antes de reimportar.

**Questões afetadas:** enunciado e gabarito de **A4**, gabarito de **D3**, gabarito de **V2** e gabarito de **9**. Nenhuma questão foi invalidada: em nenhum caso um distrator virou resposta correta, e nenhuma alternativa de múltipla escolha precisou mudar.

**Pendências:** nenhuma no plano factual. Gate científico liberado: 0 achados vermelhos ou laranja abertos.

Duas tarefas ficam encaminhadas a outras skills, e **nenhuma delas bloqueia o gate**:

1. **Lacuna de cobertura no questionário** (do achado 🟠 8) — `oa04` parte 2 e `oa05` não têm nenhuma questão de múltipla escolha, e a matriz original supunha cinco questões (11 a 15) que nunca existiram no arquivo. Escrever essas questões é tarefa do `gerador-de-questionarios`; a auditoria não cria item de avaliação novo, do mesmo modo que não cria flashcard.
2. **Cobertura de memorização do achado 🔴 1** — o baralho segue sem card sobre o sentido do V em dobras com caimento, conforme já registrado nas observações.

O `course-state.yaml` **não** foi atualizado por esta execução — a consolidação do bloco de auditoria do módulo 17, junto com os módulos 18 e 20, ficou reservada para a coordenação em paralelo.

## Reverificação de 2026-08-18

Segunda passada independente sobre o módulo já corrigido, para confirmar que as correções da primeira passada foram de fato aplicadas e estão certas:

- **Os sete achados originais foram reconferidos no texto dos arquivos** — todos presentes e aplicados, nas aulas 03, 04, 05 e 06 e nos derivados. A execução foi idempotente: nenhuma reedição foi necessária.
- **Quatro correções foram reconferidas contra fonte**, e todas se sustentam: o sentido do V em dobra com caimento (anticlinal fecha na direção do caimento, sinclinal abre); a geometria σ/δ pela linha de referência com ambos indicando o mesmo sentido; o deslocamento mínimo de ~116 km do Main Central Thrust; e a divergência real 30° × 45° na definição de cavalgamento.
- **O critério de cota introduzido no achado 🟠 2 foi validado**: a ponta do V em cota mais alta que as bordas identifica a camada que mergulha vale abaixo mais suavemente que a declividade do vale (V contrário ao mergulho); em cota mais baixa, o V aponta a favor do mergulho. Confere com a formulação de referência da regra.
- **As aulas 01 e 02 seguem limpas**, e os 84 cards dos três arquivos de flashcards batem entre si e com as aulas corrigidas.
- **Um achado novo** (🟠 8) foi encontrado no questionário, fora do alcance da primeira passada, que olhou o conteúdo científico e não a contabilidade interna do instrumento de avaliação.
