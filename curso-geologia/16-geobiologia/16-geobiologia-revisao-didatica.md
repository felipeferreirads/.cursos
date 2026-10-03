# Revisão didática: Módulo 16 — Geobiologia

**Revisado em:** 2026-08-18  ·  **Modo:** `review-and-fix`
**Material:** cinco aulas, hub, questionário final e baralho do módulo `16-geobiologia/`
**Veredito:** **Bem ensinado com ressalvas**

## Resumo

🔴 0 bloqueiam · 🟠 4 prejudicam · 🟡 6 atrito · 🔵 1 sugestão

**Carga estimada:** conceitos novos: 5–12 por aula (acima da faixa dos módulos vizinhos) · pré-requisitos reativados: ciclos geoquímicos, tempo geológico, estruturas sedimentares, rochas sedimentares · exemplos trabalhados: 1 por aula · duração estimada: 28–36 min por aula.

**Corpo por aula (teto LC-02 = 1.600 palavras), após as correções desta revisão:**

| Aula | Palavras de corpo | LC-02 |
|---|---:|---|
| 01 — Coevolução | 1.300 | conforme |
| 02 — Estromatólitos | 1.389 | conforme |
| 03 — Ciclos biogeoquímicos | 1.537 | conforme, no limite |
| 04 — Biomineralização | 1.355 | conforme |
| 05 — Origem da vida e astrobiologia | 1.850 | **excede em ~16%** |

Para comparação: as aulas dos módulos 07, 15 e 16 ficam entre 420 e 760 palavras de corpo. O módulo 16 opera num registro consistentemente mais denso que o restante do curso já revisado — é a raiz da maioria dos achados abaixo. Não é defeito de escrita: é uma escolha de nível que precisa ser decidida explicitamente pelo orquestrador, porque o módulo 17 (já escrito, ainda não revisado) segue o mesmo padrão.

## Achados

### 🟠 1. Aula 05 excede o teto de palavras e empacota dois assuntos distintos
**Tipo:** sobrecarga cognitiva / violação de LC-02
**Onde:** `16-geobiologia-aula-05-origem-vida-astrobiologia.md`, seção Conteúdo
**Problema:** A aula ensina duas coisas independentes — (a) origem da vida na Terra, com LUCA, serpentinização, mundo de RNA e duas controvérsias abertas; (b) astrobiologia, com zona habitável, zonas subsuperficiais, três alvos do sistema solar, missão Europa Clipper, catálogo de biomarcadores e o caso ALH84001. Cada metade tem massa de aula inteira. A declaração de "~29 min" no cabeçalho subestima o tempo real, e LC-02 é explícito quanto ao remédio: "o que não cabe vira Parte 1 / Parte 2, ou é deferido — nunca é comprimido".
**Correção sugerida:** dividir em `aula-05a — Origem da vida na Terra` (LUCA, hidrotermalismo/serpentinização, mundo de RNA) e `aula-05b — Astrobiologia e critérios de biogenicidade fora da Terra` (zona habitável, alvos, biomarcadores, ALH84001). O OA-05 já é composto ("descrever as hipóteses sobre a origem da vida **e** explicar como os métodos são aplicados na busca por vida") e se separa em dois objetivos sem reescrita.
**Escopo:** exige dividir a aula — decisão do `gerador-de-curso-modular`. **Não aplicada nesta revisão.**

### 🟠 2. Aula 03 ensina quatro ciclos biogeoquímicos numa única aula
**Tipo:** excesso de conceitos novos
**Onde:** `16-geobiologia-aula-03-ciclos-biogeoquimicos.md`, seção Conteúdo
**Problema:** A aula introduz, em sequência, redox, fixação, respiração anaeróbica, nitrogenase e suas três variantes, os ciclos do C, S, N e O, MIF-S, nitrificação, desnitrificação, anammox, o oxigênio como eixo de acoplamento e os eventos de anoxia oceânica. São doze ideias independentes onde o padrão do curso é três a quatro. O texto está bem organizado — cada elemento tem seu subtítulo em negrito, o que salva a legibilidade e é a razão de este achado não ser 🔴 — mas quem lê pela primeira vez não tem onde consolidar antes de receber o próximo ciclo.
**Correção sugerida:** dividir em Parte 1 (carbono e enxofre, os dois ciclos com registro mineral direto) e Parte 2 (nitrogênio e oxigênio, mais o acoplamento entre os quatro). O exemplo do lago anóxico serve como fechamento da Parte 2 sem alteração.
**Escopo:** exige dividir a aula — decisão do `gerador-de-curso-modular`. **Não aplicada nesta revisão.**

### 🟠 3. Cauda longa de termos de geociências usados sem definição na primeira ocorrência
**Tipo:** termo técnico usado antes de definido / violação de LC-01
**Onde:** as cinco aulas
**Problema:** Ao contrário dos módulos anteriores, cujos vocabulários cobriam quase todo o jargão empregado, aqui o bloco "Vocabulário desta aula" define cinco termos centrais e o corpo do texto usa outros dez ou mais sem gloss algum: *detrítico*, *MIF-S* (nomeado mas não desdobrado), *bentônico*, *autigênico*, *eutrofizado*, *testa*, *ressurgência*, *metazoário*, *ultramáfico*, *procarionte*. Cada um sozinho é atrito; juntos produzem a sensação de leitura em que o estudante entende o parágrafo pela forma, não pelo conteúdo. *Metazoário* é o mais grave dos dez, porque sustenta a frase central sobre a revolução esquelética do Ediacarano-Cambriano.
**Correção sugerida:** aposto curto em linguagem comum na primeira ocorrência, sem expandir o escopo.
**Escopo:** correção local. **Aplicada** — ver a lista em "Correções aplicadas".

### 🟠 4. A questão 7 do questionário cobra uma distinção que nenhuma aula ensina
**Tipo:** desalinhamento aula–avaliação
**Onde:** `16-geobiologia-questionario.md`, Q7 (V/F com justificativa, OA-03, 3 pts)
**Problema:** A afirmação a julgar conjuga um fato correto (a nitrogenase é a única via biológica conhecida) com uma tese filosófica sobre causalidade ("e sua evolução foi, portanto, a **causa última** da fixação de nitrogênio"). O gabarito exige que o estudante separe "ferramenta" de "causa" e reconheça pressão seletiva como co-causa — uma distinção que a Aula 03 não faz em momento nenhum, nem no corpo, nem em "Erros comuns", nem em "O que não concluir". Na prática a questão testa sofisticação argumentativa prévia, não o que o módulo ensinou. O gabarito, que abre com "Verdadeiro — em parte" e termina reformulando a própria afirmação, confirma o problema: quando a resposta certa exige reescrever o enunciado, o enunciado é que está mal calibrado.
**Correção sugerida:** ou reformular Q7 para cobrar o que a aula ensina de fato (por exemplo, por que ~3,2 Ga é limite mínimo do registro e não data de origem da enzima — ponto que a aula trabalha explicitamente em "O que não concluir"), ou acrescentar à Aula 03 uma frase que distinga a enzima como ferramenta da pressão seletiva como causa.
**Escopo:** correção no questionário — **fora da jurisdição desta skill**. Encaminhado ao `gerador-de-questionarios`. **Não aplicada.**

### 🟡 5. A Aula 04 depende da Aula 02 sem declará-la
**Tipo:** pré-requisito não declarado
**Onde:** `16-geobiologia-aula-04-...`, cabeçalho e bloco "Antes de começar"
**Problema:** O cabeçalho declara Aula 03 e M07. Mas a definição de biomineralização induzida — metade do OA-04 — é ancorada em "como discutido a propósito de estromatólitos na Aula 02", e o exemplo trabalhado inteiro opõe laminação estromatolítica a grainstone bioclástico. Quem voltou direto da Aula 03 não tem como detectar que precisa da 02.
**Escopo:** correção local. **Aplicada.**

### 🟡 6. O hub do módulo subdeclara os pré-requisitos
**Tipo:** pré-requisito não declarado
**Onde:** `16-geobiologia-modulo.md`, seção Pré-requisitos
**Problema:** O hub lista M09 e M15, mas as aulas exigem também M13 (aula 02), M07 (aula 04) e M03 (aula 05). Quem planeja o estudo pelo hub não vê três dos cinco pré-requisitos reais.
**Escopo:** correção local. **Aplicada.**

### 🟡 7. O centro de gravidade da avaliação está na aula mais especulativa
**Tipo:** desalinhamento de ênfase entre ensino e avaliação
**Onde:** `16-geobiologia-questionario.md` (matriz) e baralho
**Problema:** OA-05 recebe 16 dos 48 pontos do questionário (33%, quatro questões, incluindo as duas de maior valor) e 10 dos 29 cards Basic (34%) — mais que o dobro de OA-01 e OA-02, que valem 7 pontos cada. OA-05 é justamente o objetivo mais aberto do módulo, com duas pendências ⚪ de auditoria em curso (`GEOBIO-LUCA-THERMO-001`, `GEOBIO-LHB-001`). O peso avaliativo está no que menos se pode fixar como conhecimento estável, enquanto a coevolução geosfera-biosfera — o conceito que dá nome e sentido ao módulo — vale 15%.
**Correção sugerida:** rebalancear para aproximar os cinco objetivos, ou justificar o desequilíbrio explicitamente na matriz.
**Escopo:** questionário e baralho — **fora da jurisdição desta skill.** **Não aplicada.**

### 🟡 8. Cards não atômicos e cards que dependem do número da aula
**Tipo:** desalinhamento aula–flashcards
**Onde:** `16-geobiologia-flashcards-basic.csv`
**Problema:** Dois defeitos distintos. (a) O índice do baralho declara atomicidade como critério de qualidade, mas `fb004` (positiva **e** negativa), `fb006`, `fb008` ("cite três critérios"), `fb017` ("cite três famílias") e `fb025` ("cite dois corpos") pedem múltiplas respostas num card só — em repetição espaçada isso produz acerto parcial constante, que é o pior sinal possível para o algoritmo de agendamento. (b) `fb002` ("...conforme a Aula 01") e `fb026` ("...cite um exemplo do registro terrestre da Aula 05") referenciam a numeração da aula na frente do card; meses depois, fora do contexto do curso, a pergunta deixa de ser respondível.
**Escopo:** baralho — **fora da jurisdição desta skill.** Encaminhado ao `gerador-de-flashcards`. **Não aplicada.**

### 🟡 9. A controvérsia da Aula 05 entra com detalhe de debate, não como pergunta em aberto
**Tipo:** carga cognitiva / tensão com LC-08
**Onde:** `16-geobiologia-aula-05-...`, seção Conteúdo, parágrafos sobre LUCA e girase reversa
**Problema:** LC-08 prevê que, no nível de entrada, a controvérsia apareça como pergunta em aberto declarada, sem o detalhe do debate. Os dois parágrafos sobre a termofilia do LUCA e sobre o bombardeamento pesado tardio fazem o contrário: reconstroem quem argumenta o quê, com ressalvas encadeadas ("os próprios autores ressalvam... apontam no mesmo genoma... admitem tanto... há ainda análises que concluem o oposto"). Isso é rigor, e veio da auditoria — os achados ⚪ abertos exigem essa honestidade. Mas rigor entregue como cadeia de ressalvas é, para quem lê pela primeira vez, indistinguível de ruído.
**Observação importante:** este achado **não deve ser resolvido cortando as ressalvas** — elas são o registro auditado de duas divergências reais da literatura. A saída correta é estrutural: com a divisão proposta no achado 1, a Parte 1 ganha espaço para enunciar cada controvérsia em uma frase no corpo e alojar o detalhe do debate em "O que não concluir", que é onde o leitor já espera encontrar limites de interpretação.
**Escopo:** resolve-se junto com a divisão da aula. **Não aplicada.**

### 🟡 10. A Aula 03 só oferece âncora concreta no exemplo trabalhado
**Tipo:** abstração antes do concreto / LC-04
**Onde:** `16-geobiologia-aula-03-...`, seção Conteúdo
**Problema:** A aula tem uma âncora sensorial excelente — o cheiro de ovo podre do H₂S — mas ela aparece só no exemplo trabalhado, depois de mil palavras de reações redox. As outras quatro aulas trazem a analogia cedo e ela funciona bem ("pias químicas" e "termostato" na 01, "andaime" e as falésias de Dover na 04, "eletrodo natural" na 05). A 03 é a aula mais abstrata do módulo e a única sem essa ponte no começo.
**Correção sugerida:** antecipar o H₂S do fundo de lago como abertura da seção do enxofre. **Não aplicada nesta revisão** porque mover o gancho para dentro de uma aula que já está no limite de LC-02 é decisão que faz mais sentido junto com a divisão do achado 2.

### 🔵 11. Um diagrama de retroalimentação ajudaria a Aula 01
**Onde:** `16-geobiologia-aula-01-...`, parágrafo da Grande Oxidação
**Sugestão:** o ciclo já está escrito em prosa como cadeia ("vida produz O₂ → O₂ se acumula depois de saturar as pias → oxidação muda rochas e atmosfera → mudança climática reconfigura o ambiente da vida"). É o conceito-mãe do módulo inteiro e o único que se beneficiaria mais de ser visto do que lido. Um diagrama circular simples, sem número novo algum, o fixaria de uma vez.

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo | Avaliado em |
|---|---|---|---|
| `geologia-m16-oa01` | Aula 01, Conteúdo (GOE e ciclo carbonato-silicato) | sim (BIFs) | Q1, Q2 · fb001–fb004 |
| `geologia-m16-oa02` | Aula 02, Conteúdo (mecanismo e critérios de biogenicidade) | sim (domo do Proterozoico) | Q3, Q4 · fb005–fb009 |
| `geologia-m16-oa03` | Aula 03, Conteúdo (quatro ciclos e acoplamento) | sim (lago estratificado) | Q5, Q6, Q7 · fb010–fb014 |
| `geologia-m16-oa04` | Aula 04, Conteúdo (induzida × controlada, três famílias) | sim (duas amostras carbonáticas) | Q8, Q9, Q10 · fb015–fb019 |
| `geologia-m16-oa05` | Aula 05, Conteúdo (origem da vida e astrobiologia) | sim (pluma de Encélado) | Q11–Q14 · fb020–fb029 |

Nenhum objetivo ficou sem ensino, sem exemplo ou sem avaliação, e nenhuma seção substancial é órfã de objetivo. Todos os cinco objetivos são formulados com verbo verificável (explicar, descrever, distinguir, situar) — nenhum usa "entender" ou "conhecer". O problema de alinhamento não é de cobertura, é de proporção (achado 7) e de calibragem de uma questão (achado 4).

## Verificação do contrato de nível (`ensino-medio-sem-geologia-v1`)

| Regra | Resultado |
|---|---|
| LC-01 — nenhum termo sem definição | **Ressalva** — dez termos sem gloss na primeira ocorrência (achado 3); corrigidos localmente. |
| LC-02 — teto de 1.600 palavras | **Não conforme na aula 05** (1.850). As outras quatro estão conformes; a 03 está no limite. |
| LC-03 — abertura padronizada | Conforme: cinco termos de vocabulário e bloco de pré-requisitos nas cinco aulas. Ressalva de conteúdo no achado 5, corrigida. |
| LC-04 — analogia antes do termo | Conforme nas aulas 01, 02, 04 e 05. Ressalva na 03 (achado 10). |
| LC-05 — ordem de grandeza | Conforme: as idades aparecem como faixas ("~2,4–2,3 Ga", "~550–539 Ma"), não como valores pontuais falsamente precisos. |
| LC-06 — matemática reativada | Conforme: não há derivação nem notação matemática. |
| LC-07 — três blocos obrigatórios | Conforme: "Erros comuns", "O que não concluir" e "Recap relâmpago" presentes nas cinco aulas, e os recaps destilam em vez de repetir. |
| LC-08 — controvérsia em uma frase | **Ressalva na aula 05** (achado 9), por tensão legítima com o rigor exigido pela auditoria. |

## Correções aplicadas

Todas locais, sem alegação factual nova e sem alterar o escopo científico aprovado na auditoria de 2026-08-18.

**Aula 01**
- "Hadeano e Arqueano" ganhou reativação com link para M15, aula 06.
- "minerais detríticos" ganhou aposto ("grãos herdados da erosão de rochas mais antigas").
- MIF-S deixou de ser só uma sigla nomeada: o texto agora desdobra o que "fracionamento independente de massa" significa antes de dizer o que ele indica.

**Aula 02**
- "bentônicas" ganhou gloss ("que vivem sobre o fundo").

**Aula 03**
- "autigênico" ganhou gloss ("formado no próprio local de deposição, e não trazido de fora como grão").
- "eutrofizado" ganhou gloss ("com excesso de nutrientes e, por consequência, de matéria orgânica a decompor").

**Aula 04**
- O bloco "Antes de começar" passou a reativar a Aula 02, nomeando a precipitação induzida por tapetes microbianos como o contraponto direto da biomineralização controlada (achado 5).
- "metazoários" ganhou gloss ("animais"), "testas" ganhou gloss ("as carapaças minerais dessas células") e "ressurgência oceânica" ganhou gloss ("subida de águas profundas ricas em nutrientes").

**Aula 05**
- "ultramáficas" e "procariontes" ganharam gloss.
- A frase de fechamento do módulo dizia a mesma coisa duas vezes; foi reduzida de setenta para quarenta palavras, preservando as duas metades do sentido.

**Hub**
- A seção Pré-requisitos passou a listar M03, M07 e M13 como reativados por aulas específicas, além de M09 e M15 (achado 6).

Os glosses acrescentam cerca de 45 palavras distribuídas entre as cinco aulas — mantidos deliberadamente curtos porque a aula 05 já está acima do teto e as aulas 03 e 05 aguardam decisão de divisão.

## O que está bem feito

- **A progressão do módulo é excelente e deveria ser preservada em qualquer divisão.** As cinco aulas encadeiam quatro modos distintos de a vida agir como agente geológico — alterar a química global (01), construir estrutura sedimentar (02), mover elementos entre reservatórios (03), fabricar mineral (04) — e a quinta usa os quatro como método para o caso mais difícil, o da vida que talvez não exista. Cada aula abre retomando explicitamente onde a anterior parou. É raro um módulo em que a ordem das aulas seja, ela própria, um argumento.
- **O critério de biogenicidade é ensinado uma vez e depois cobrado três vezes em contextos novos** — no domo do Proterozoico (02), na magnetita marciana (04) e nos aminoácidos de Encélado (05). É transferência genuína, não repetição: o estudante aplica a mesma régua a uma rocha, a um cristal e a uma molécula, e é assim que se ensina um método em vez de um fato.
- **Os blocos "O que não concluir" são os melhores do curso até aqui.** Cada um freia uma inferência específica que o texto acabou de tornar tentadora — LUCA não é a origem da vida, a idade de Strelley Pool não é a origem da vida, magnetita compatível não é prova, ~3,2 Ga é limite do registro e não data de origem. Todos ensinam o mesmo hábito: separar o limite da evidência do limite do fenômeno.
- **As metáforas escolhidas não ensinam modelo errado.** "Pias químicas", "termostato de longo prazo", "andaime", "eletrodo natural" e "bússola biológica" são todas mecanicamente fiéis ao que descrevem, e nenhuma cria a ilusão de intencionalidade que costuma contaminar textos sobre coevolução.

## Encaminhamentos

| Item | Destino |
|---|---|
| Achados 1, 2 e 9 — divisão das aulas 03 e 05 | `gerador-de-curso-modular` |
| Achados 4 e 7 — recalibrar Q7 e o peso de OA-05 | `gerador-de-questionarios` |
| Achados 7 e 8 — atomicidade, dependência de contexto e balanceamento dos cards | `gerador-de-flashcards` |
| Calibragem de nível do bloco (M16 e M17 operam acima do registro dos módulos 06–15) | decisão do usuário / `planejador-curricular` |
