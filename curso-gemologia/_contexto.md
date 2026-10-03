# Contexto — Curso de Gemologia

Preferências e decisões duradouras sobre como este curso é ensinado. Não é estado de progresso — isso vive em `course-state.yaml`.

## Origem: este curso nasceu de uma separação (2026-08-25)

Este curso **não foi escrito do zero**. Até 2026-08-25 a gemologia era uma área temática dentro do curso `curso-geologia-gemologia`, ocupando os módulos **06** (Gemologia geral e identificação), **30** (Diamantes) e **31** (Gemas coradas, pérolas e gemas orgânicas, apenas planejado).

A área cresceu para três módulos e cerca de 57 aulas, com bibliografia própria (GIA, Gem-A, CIBJO, LMHC), público próprio e sequência de estudo própria. Mantê-la dentro do curso de geologia distorcia a numeração — módulos 06, 30 e 31, com 23 módulos de geologia no meio — e poluía o dashboard do aluno. A decisão foi separar em dois cursos independentes:

| Curso | O que ficou |
|---|---|
| `curso-geologia` | os 29 módulos de geociências, renumerados em sequência contínua |
| `curso-gemologia` (este) | os três módulos de gemologia, renumerados 01, 02 e 03 |

## A decisão de renumerar tudo, e o que ela custou

> [!warning] Leia isto antes de estranhar que os IDs mudaram
> Em **2026-08-25** todos os identificadores deste curso mudaram. A decisão foi tomada de forma explícita e consciente pelo usuário, com o custo conhecido de antemão. Este bloco existe para que ninguém, no futuro, procure uma corrupção de dados onde houve uma escolha.

**O que mudou:**

| Antes | Depois |
|---|---|
| `curso-geologia-gemologia/06-gemologia/` | `curso-gemologia/01-gemologia-geral/` |
| `curso-geologia-gemologia/30-gemologia-diamantes/` | `curso-gemologia/02-diamantes/` |
| `curso-geologia-gemologia/31-gemologia-coradas-perolas/` | `curso-gemologia/03-gemas-coradas-perolas/`, dividido em 2026-08-26 em `03-gemas-coradas/` e `04-perolas/` (ver abaixo) |
| `geologia-gemologia-m06-oa01` · `-a01` · `-fb001` · `-fc001` | `gemologia-m01-oa01` · `-a01` · `-fb001` · `-fc001` |
| `geologia-gemologia-m30-*` | `gemologia-m02-*` |
| Deck Anki `Geologia e Gemologia::M06` | Deck Anki `Gemologia::M01` |
| Tags `geologia::gemologia::*` | Tags `gemologia::identificacao::*` |
| `course_id: geologia-gemologia` | `course_id: gemologia` |

**Custo aceito nº 1 — o histórico do Anki.** Como o ID de cada card mudou, o Anki trata os cards importados a partir desta versão como **novos**. Os 1.459 cards já revisados perdem o histórico de repetição espaçada acumulado. Não há como evitar isso mantendo IDs legíveis e coerentes com a nova numeração, e a alternativa — carregar para sempre um prefixo `geologia-gemologia-m06` num curso que não se chama assim e num módulo que não é o 06 — foi julgada pior. **Recomendação prática:** apague os decks antigos `Geologia e Gemologia::M06` e `::M30` no Anki antes de importar os CSVs novos, ou você terá dois baralhos com o mesmo conteúdo.

**Custo aceito nº 2 — o `page_map` do Notion.** O mapa arquivo→página do curso antigo apontava para caminhos que não existem mais. Ele **não** foi transportado para cá: este curso começa sem `notion_sync`, e a primeira publicação vai **criar páginas novas** em vez de atualizar as antigas. As páginas antigas continuam existindo sob a árvore do curso de Geologia no Notion e precisam ser movidas ou apagadas **à mão** pelo usuário. Os `page_id` estão registrados abaixo para que nada se perca.

### Páginas do Notion órfãs (a reconciliar à mão)

Todas estavam sob `Curso: Geologia e Gemologia — do essencial ao avançado`.

| Arquivo antigo | `page_id` | Papel |
|---|---|---|
| `06-gemologia/06-gemologia-modulo.md` | `3a7e3d393096813c9130c81cb4dccaf2` | hub do módulo |
| `06-gemologia/…-aula-01-o-que-e-gema-especie-variedade-nome-comercial.md` | `3c0e3d39309681d2a137e79d34c2050a` | aula |
| `06-gemologia/…-aula-02-origem-da-cor-nas-gemas.md` | `3c0e3d393096813f9978c51e1dc56a54` | aula |
| `06-gemologia/…-aula-03-propriedades-diagnosticas-gemologicas.md` | `3c0e3d39309681a2af37d381e967075c` | aula |
| `06-gemologia/…-aula-04-refratometro-e-polariscopio.md` | `3c0e3d393096810695f5fb9aa7970f1e` | aula |
| `06-gemologia/…-aula-05-dicroscopio-espectroscopio-lupa-microscopio.md` | `3c0e3d39309681e68fbbee1e3b7021b1` | aula |
| `06-gemologia/…-aula-06-fluxo-de-identificacao-gemologica.md` | `3c0e3d39309681f6b91cf6ca992c5a0a` | aula |
| `06-gemologia/…-aula-22-proveniencia-laudos-e-fatores-de-valor.md` | `3c0e3d393096813d8b6bd8360ef5e2f4` | aula |
| `06-gemologia/06-gemologia-auditoria.md` | `3c0e3d393096812b8a49d55fb8df103e` | auditoria |
| `06-gemologia/06-gemologia-revisao-didatica.md` | `3c0e3d393096815ea96ed5081d2d30f1` | revisão didática |
| `06-gemologia/06-gemologia-questionario-parcial-1.md` | `3c0e3d3930968140908ff6a19f30cc3f` | avaliação |
| `06-gemologia/06-gemologia-questionario-parcial-2.md` | `3c0e3d39309681668d4cd5be9970752e` | avaliação |
| `06-gemologia/06-gemologia-questionario-final.md` | `3c0e3d3930968101931edd3703d57bc2` | avaliação |
| `06-gemologia/06-gemologia-flashcards.md` | `3c0e3d3930968185a7cfe7a56ea7c283` | flashcards |

O módulo 30 (Diamantes) nunca chegou a ser publicado e não tem páginas órfãs.

## Perfil e nível

- **Partida:** ensino médio completo, **mais** mineralogia e cristalografia de nível de graduação, que este curso **não** ensina.
- **Chegada:** avançado / especialista — cobertura equivalente ao núcleo do programa Graduate Gemologist do GIA.
- Aplicação prática: não declarada; formação ampla e completa.

## Pré-requisito externo (cross-curso)

O pré-requisito real do módulo 01 **não está neste curso**. Ele vive no curso irmão de Geologia:

| Pré-requisito | Onde | O que este curso assume |
|---|---|---|
| Cristalografia e química dos minerais | `curso-geologia`, módulo **04** | espécie mineral, ligação química, sistemas cristalinos, simetria, estruturas dos silicatos |
| Mineralogia, identificação e óptica | `curso-geologia`, módulo **05** | propriedades físicas diagnósticas, dureza Mohs, clivagem, como a luz atravessa um cristal |

> **Regra:** essa dependência é referenciada **por nome**, nunca por wikilink. Um wikilink apontando para fora do curso quebra no Obsidian e é reportado como link morto pelo `validador-estrutural-do-curso`. A dependência está registrada de forma estruturada em `course-state.yaml` no campo `external_prerequisites` do módulo 01 — que o schema atual não conhece, e por isso ficou registrada aqui.
>
> Os números 04 e 05 do curso de Geologia **não mudaram** na renumeração de 2026-08-25 (só os módulos 07 em diante foram deslocados), então as referências continuam válidas.

## Contrato de nível (`ensino-medio-sem-geologia-v1`, herdado)

Vale para toda aula deste curso, herdado do curso de origem:

1. **LC-01 — Nenhum termo sem definição** na primeira aparição, em linguagem comum.
2. **LC-02 — Teto de ~1.600 palavras** de corpo por aula. O que não cabe vira Parte 1 / Parte 2, ou é deferido — nunca é comprimido.
3. **LC-03 — Abertura padronizada:** "Vocabulário desta aula" (5 a 10 termos) e "Antes de começar, você precisa saber", com os links das aulas exigidas.
4. **LC-04 — Analogia antes do termo.**
5. **LC-05 — Ordem de grandeza, não precisão de laboratório.** A exceção são datas de decisões normativas e valores de referência tabelados (índices de refração, densidades, comprimentos de onda), que têm valor único e são o objeto de estudo.
6. **LC-06 — Matemática reativada antes do uso.**
7. **LC-07 — "Erros comuns", "O que não concluir" e "Recap relâmpago" obrigatórios.**
8. **LC-08 — Controvérsia em uma frase**, declarada como pergunta aberta, sem arbitrar o debate.

Acrescente-se a convenção estrutural adotada no módulo 01 a partir de 2026-08-24 e estendida a todo o curso: bloco **"Ao final você vai conseguir"** com o **ID completo** do objetivo (nunca `OA-0N`), e rodapé em comentário HTML com `nivel`, `palavras_corpo`, `cobertura` e `alegacoes_auditaveis` em YAML.

## Pipeline de qualidade

Ordem obrigatória, por módulo: **aulas → auditoria científica → correção → questionário(s) → flashcards → revisão didática.**

Gate: nenhum questionário ou baralho é gerado para um módulo com achado 🔴 ou 🟠 em aberto na auditoria.

## Escopo dos três módulos

- **01 — Gemologia geral e identificação** (22 aulas, completo): fundamentos e nomenclatura, origem da cor, propriedades diagnósticas, instrumentos de bancada, camada espectroscópica de laboratório, anatomia e lapidação, fenômenos ópticos, materiais opacos, durabilidade, metais e montagem, geologia das gemas, províncias brasileiras, mercado, proveniência e laudos.
- **02 — Diamantes** (15 aulas, completo): o diamante como mineral, origem geológica e superprofunda, tipos Ia/Ib/IIa/IIb, os quatro fatores de qualidade em profundidade, cor fancy, fluorescência e valor, simulantes, crescimento HPHT e CVD, DiamondView e fotoluminescência, triagem, tratamentos e laudos.
- **03 — Gemas coradas, pérolas e gemas orgânicas** (20 aulas planejadas, **a construir**): graduação de cor no sistema GIA (matiz, tom, saturação, GemSet); fatores de valor de gema corada; tipos de pureza por espécie; espécies coradas uma a uma (coríndon, berilo, turmalina, granadas, espinélio, topázio, peridoto, quartzo e calcedônia, e as demais frequentes), cada uma com identificação, tratamento e valor; o mapa dos tratamentos e a regra de divulgação; as rotas de síntese e suas assinaturas; imitações e materiais compostos; pérolas em cobertura completa (biologia, natural × cultivada, akoya, South Sea, Tahiti e água doce, nucleação, os sete fatores de valor do GIA, ensaios e tratamentos); e gemas orgânicas (âmbar × copal, coral, marfim com nota CITES, azeviche, madrepérola).

## Fora do escopo (e por quê)

- **Geologia geral.** É o curso irmão. Este curso assume mineralogia e cristalografia e não as reensina.
- **Joalheria, ourivesaria e engaste como ofício.** A aula 18 do módulo 01 trata de metais e montagem **pelo que eles fazem ao exame gemológico** — não como técnica de bancada de joalheiro.
- **Avaliação de valor de mercado.** O curso ensina a separar identificação de avaliação, e para de propósito na fronteira.

## Preferências de ensino

- Destino: Obsidian. Aulas de no máximo 30 minutos; assuntos grandes divididos em partes.
- Progressão sem usar conceito antes de ensiná-lo, verificável por LC-01 e LC-03.
- Nenhum card ou questão pode afirmar competência de bancada: exame escrito avalia princípio, escopo e limite, nunca destreza manual.

## IDs aposentados, jamais recicláveis

Herdados da reabertura do módulo 06 em 2026-08-24, quando diamantes e gemas coradas saíram dele:

- **Objetivos do módulo 01:** `oa07`, `oa08` (migraram para o módulo 02); `oa09`, `oa10` (migraram para o módulo 03).
- **Flashcards do módulo 01:** `fb019`–`fb030` e `fc013`–`fc020`.
- **Questões do módulo 01:** `q11`–`q33`.

Da divisão da aula 13 em 2026-08-27: **nenhum**. Nenhum ID de aula, objetivo, questão ou card foi aposentado ou reciclado — `gemologia-m03-oa17` é ID **novo**, e os IDs de aula deslocados (`a15`, `a16`, `a17`) apenas passaram a designar aulas que já existiam.

Herdados da divisão do módulo 03 em 2026-08-26:

- **Flashcards do módulo 03:** `fb201`–`fb265` e `fc059`–`fc074` (os cards migraram para o módulo 04 e foram reindexados lá).
- **Questões do módulo 03:** `q33`–`q44` (o parcial 3 virou o questionário do módulo 04) e `q58`–`q61` (o bloco biológico do cumulativo migrou junto).

Próximo ID livre: módulo 01 → `fb196` / `fc078`; módulo 02 → `fb176` / `fc051`; módulo 03 → `fb275` / `fc077` e **`oa22`** para objetivo; módulo 04 → `fb066` / `fc017`.

## A divisão do módulo 03 (2026-08-26)

> [!warning] Segunda mudança de identificadores, e a última prevista
> Em **2026-08-26** o módulo `03-gemas-coradas-perolas`, de 21 aulas, foi dividido em dois. Como no episódio de 2026-08-25, a decisão foi explícita do usuário e o custo é conhecido. Este bloco existe para que ninguém procure uma corrupção de dados onde houve uma escolha.

**Por que dividir.** O módulo reunia dois regimes de exame incompatíveis. No material mineral, o eixo é refratômetro, birrefringência, caráter óptico e densidade. No material biológico — pérola, âmbar, coral, marfim, madrepérola — esses instrumentos quase não servem, e o exame passa a ser densidade, toque, cheiro, solvente, fluorescência e lupa. Além disso, com 21 aulas o módulo era maior que os outros dois somados por bloco temático. A fronteira entre a aula 16 e a aula 17 já era o corte natural, e o questionário parcial 3 já cobria exatamente as cinco aulas biológicas — a estrutura pedia a divisão antes de alguém propô-la.

**O que mudou:**

| Antes | Depois |
|---|---|
| `03-gemas-coradas-perolas/` (21 aulas) | `03-gemas-coradas/` (aulas 01–16) e `04-perolas/` (ex-aulas 17–21, renumeradas 01–05) |
| `gemologia-m03-a17` … `-a21` | `gemologia-m04-a01` … `-a05` |
| `gemologia-m03-oa17` … `-oa21` | `gemologia-m04-oa01` … `-oa05` |
| `gemologia-m03-fb201`–`fb265` · `fc059`–`fc074` | `gemologia-m04-fb001`–`fb065` · `fc001`–`fc016` |
| `gemologia-m03-q33`–`q44` (parcial 3) e `q58`–`q61` (bloco D do cumulativo) | `gemologia-m04-q01`–`q12` e `q13`–`q16` |
| Deck Anki `Gemologia::M03 Gemas coradas, pérolas e gemas orgânicas` | Decks `Gemologia::M03 Gemas coradas` e `Gemologia::M04 Pérolas e gemas orgânicas` |

**Custo aceito — o histórico do Anki, de novo, mas só de uma parte.** Os **258 cards** que ficaram no módulo 03 (`fb001`–`fb200`, `fc001`–`fc058`) mantiveram os IDs, porque a numeração era contígua por aula: eles preservam o histórico de repetição espaçada. Os **81 cards** que mudaram de módulo foram reindexados e o Anki vai tratá-los como novos. **Recomendação prática:** ao reimportar, apague no Anki apenas as notas com ID `gemologia-m03-fb201` a `fb265` e `fc059` a `fc074`, ou você ficará com 81 duplicatas.

**O que NÃO mudou.** Nenhum texto de aula foi reescrito — só as referências internas de numeração ("a aula 18" virou "a aula 02", os wikilinks para as aulas minerais passaram a declarar o módulo de origem). Nenhum achado de auditoria, controvérsia, alegação verificada, nota deferida, questão, rubrica ou card foi criado, alterado ou descartado: os relatórios foram **particionados** pelo arquivo de origem de cada item.

**Por que o prefixo é `04-perolas` e não algo mais amplo.** Foi pedido explícito do usuário. A pérola é o material central do módulo — três das cinco aulas —, mas o módulo cobre **todas as gemas de origem biológica** do curso, e as duas últimas aulas não tratam de pérola nenhuma. O hub, o índice do baralho e o relatório de auditoria declaram isso na abertura para que o nome não estreite a expectativa.

## A divisão da aula 13 do módulo 03 (2026-08-27)

> [!warning] Terceira mudança de numeração, e a menor delas
> Em **2026-08-27** a aula 13 do módulo 03 foi dividida em duas, e as aulas seguintes foram deslocadas. Ao contrário dos episódios de 2026-08-25 e 2026-08-26, **esta divisão não custou nenhum histórico do Anki** — leia o porquê abaixo antes de supor o contrário por analogia com as anteriores.

**Por que dividir.** A [[03-gemas-coradas/03-gemas-coradas-revisao-didatica|revisão didática do módulo 03]] registrou o achado 🟠 3: a aula 13 carregava **quatro espécies sem parentesco mineralógico** — zircão, tanzanita, espodumênio e iolita —, cada uma com sua tabela completa de propriedades, e o zircão com **duas**. Eram 34 linhas de tabela e cinco conjuntos de números, contra dois nas aulas vizinhas, e era a aula com mais cards do módulo (18). A moldura narrativa das "quatro fragilidades" ajudava, mas moldura não reduz carga. A própria revisão já indicava o corte e observava que o texto **já estava seccionado por espécie** — a divisão não exigia conteúdo novo.

**O que mudou:**

| Antes | Depois |
|---|---|
| `…aula-13-zircao-tanzanita-espodumenio-e-iolita.md` (quatro espécies) | `…aula-13-quatro-fragilidades-parte-1-zircao-e-tanzanita.md` e `…aula-14-quatro-fragilidades-parte-2-espodumenio-e-iolita.md` |
| `gemologia-m03-a14` · `-a15` · `-a16` | `gemologia-m03-a15` · `-a16` · `-a17` |
| `gemologia-m03-oa13` (quatro espécies) | `gemologia-m03-oa13` (zircão e tanzanita) **+** `gemologia-m03-oa17` (espodumênio e iolita, **ID novo**) |
| `oa14` · `oa15` · `oa16` nas aulas 14, 15 e 16 | os **mesmos** `oa14` · `oa15` · `oa16`, agora nas aulas 15, 16 e 17 |
| Módulo 03 com 16 aulas · curso com 58 | Módulo 03 com **17** aulas · curso com **59** |

**Por que o objetivo novo é `oa17`, e não `oa14`.** Deslocar `oa14`–`oa16` para abrir espaço no meio da sequência obrigaria a aposentar três IDs já referenciados por questões dos três questionários, por 35 cards e por quatro arquivos do módulo 04. O objetivo novo recebeu, em vez disso, o **próximo ID livre**. O preço é que a lista de objetivos do módulo deixa de estar em ordem numérica — ela está em **ordem de aula**, e tanto o hub quanto o `course-state.yaml` dizem isso de forma explícita, para que ninguém leia a ordem como erro. **Nenhum ID de objetivo foi reciclado**, e a regra de um objetivo por aula continua valendo: 17 objetivos para 17 aulas.

**Custo que NÃO foi pago — o histórico do Anki.** Nenhum ID de card mudou. Os cards de espodumênio e iolita (`fb162`–`fb165` e `fc049`) trocaram apenas os campos `aula`, `objetivo` e `tags`; os cards das antigas aulas 14, 15 e 16 apenas passaram a apontar para 15, 16 e 17. Isso foi possível porque **a numeração já era contígua por aula e o prefixo de módulo não mudou** — exatamente a razão pela qual, em 2026-08-26, os 258 cards que ficaram no módulo 03 também preservaram o histórico. **Recomendação prática:** reimporte os dois CSVs normalmente, com "atualizar notas existentes quando o primeiro campo coincide". O Anki atualiza etiqueta e campos e **mantém o agendamento**. Não apague nada desta vez.

**Custo aceito — o baralho desequilibrado.** A nova aula 14 ficou com **5 cards** (4 Basic + 1 Cloze), contra 13 a 17 nas demais aulas do módulo, porque a repartição **não podia criar card**: criar card é criar afirmação, e a regra desta operação era não introduzir fato novo. Ampliar esse conjunto é tarefa do `gerador-de-flashcards`, e está registrada como pendência não bloqueante em `course-state.yaml`.

**O que NÃO mudou.** Nenhum texto de espécie foi reescrito: as quatro seções, as cinco tabelas de propriedades, os "erros comuns", o "o que não concluir" e as **12 alegações auditáveis** foram **redistribuídos** por espécie, não refeitos — sete alegações na parte 1 (`ZIR-*`, `TAN-*`) e cinco na parte 2 (`ESD-*`, `IOL-*`). Nenhum achado de auditoria, controvérsia ou nota deferida foi criado, alterado ou descartado: foram apenas reapontados para o arquivo certo. **Nenhum ID de questão foi reindexado** — a Q9 do parcial 2 continua no `oa13` e a Q10 passou ao `oa17`, na mesma ordem e com a mesma pontuação total.

**A única prosa nova.** A parte 2 herdou o exemplo trabalhado original (iolita × tanzanita × quartzo). A parte 1 precisava de um próprio, porque a convenção do curso exige exemplo trabalhado por objetivo — e ele foi montado **exclusivamente** com valores já verificados na auditoria (`ZIR-EST-001`, `ZIR-EST-002`, `ZIR-TRAT-001`, `TAN-EST-001`), recombinados num fluxo de bancada. Nenhuma alegação auditável nova foi registrada, e por isso a auditoria do módulo não precisou ser reaberta.

## Decisões (registro por data)

- **[2026-08-24]** Abrir a área temática de gemologia em três módulos em vez de inchar um só. O módulo 06 estava subdimensionado: 11 aulas para todo o programa gemológico, com diamantes e gemas coradas espremidos em duas aulas cada.
- **[2026-08-25]** **Separar** a gemologia em curso independente.
- **[2026-08-25]** **Renumerar tudo e reprefixar todos os IDs**, aceitando a perda do histórico do Anki e o desalinhamento do Notion. Detalhado acima.
- **[2026-08-25]** **Não fundir** nenhuma das aulas 01–06 do módulo 01. Cada uma cobre exatamente um objetivo (`oa01` a `oa06`) e marca um degrau conceitual distinto; fundir obrigaria a aposentar um objetivo ou a criar uma aula com dois centros. O problema era profundidade, não fragmentação.
- **[2026-08-25]** **Aprofundar** as aulas 01–06, que tinham 270–341 palavras contra 876–1.258 das demais, normalizando-as para a convenção atual. Na aula 04, a física (índice de refração, lei de Snell, ângulo crítico, reflexão interna total, luz polarizada) passou a vir **antes** da operação do refratômetro e do polariscópio — o instrumento agora é apresentado como aplicação de uma física já entendida, e não como um procedimento a decorar.
- **[2026-08-25]** Referenciar pré-requisitos do curso de Geologia **por nome**, nunca por wikilink.
- **[2026-08-25]** Gerar o baralho do módulo 02, que não existia: 225 cards ancorados nas alegações já auditadas das 15 aulas.
- **[2026-08-26]** **Dividir o módulo 03** em `03-gemas-coradas` (16 aulas) e `04-perolas` (5 aulas), com o prefixo `perolas` mesmo cobrindo âmbar, coral e marfim. Detalhado acima.
- **[2026-08-27]** **Dividir a aula 13 do módulo 03** em parte 1 (zircão e tanzanita) e parte 2 (espodumênio e iolita), renumerando as aulas 14–16 para 15–17. Resolve o achado 🟠 3 da revisão didática. Detalhado acima.
- **[2026-08-27]** **Dar ao objetivo novo o próximo ID livre (`oa17`)** em vez de deslocar `oa14`–`oa16`. Aceita-se que a lista de objetivos do módulo 03 deixe de estar em ordem numérica — ela passa a estar em ordem de aula, e isso está declarado no hub e no `course-state.yaml`. A alternativa aposentaria três IDs já referenciados por questões, por 35 cards e por quatro arquivos do módulo 04.
- **[2026-08-27]** **Não reindexar nenhum card nem nenhuma questão** na divisão da aula 13. A numeração de card já era contígua por aula e o prefixo de módulo não mudou, então trocar os campos `aula`, `objetivo` e `tags` bastou — e o histórico do Anki fica **preservado**, ao contrário das duas divisões anteriores.
- **[2026-08-28]** **Comprimir a aula 02 do módulo 04 em vez de dividi-la.** Ela ficou com 1.817 palavras ao absorver a madrepérola. Dividir emitiria um objetivo novo e reindexaria questões e cards por causa de ~220 palavras; a aula tinha redundância real (o recap repetia a tabela quase verbatim, o exemplo trabalhado tinha oito passos onde cinco bastam), então o corte saiu de redundância e **nenhum fato foi removido** — as 12 alegações auditáveis do rodapé continuam sustentadas pelo texto. Resultado: **1.588** palavras.
- **[2026-08-28]** **Não reindexar `fb064` e `fb065`** ao movê-los da aula 05 para a aula 02, pelo mesmo motivo aceito na divisão da aula 13 do módulo 03: trocar `aula`, `objetivo`, `tags` e `fonte` **preserva o histórico do Anki**. Custo aceito: a faixa de IDs da aula 02 deixa de ser contígua — `fb013`–`fb024` **e** `fb064`–`fb065`. **Reimporte normalmente, sem apagar nada.**
- **[2026-08-28]** **Registro corrigido: os IDs das alegações de madrepérola são `MPE-EST-001` e `MPE-USO-001`.** As notas de 2026-08-27 no `course-state.yaml` se referiam a elas como "as alegações `PER-MAD-*`". **Esse prefixo nunca existiu** neste curso. Fica o registro para que ninguém procure um par de IDs inexistente.
- **[2026-08-27]** **Normalizar a tabela de correções da auditoria do módulo 02**, cujas células de desfecho diziam "✅ Corrigido" enquanto os módulos 01, 03 e 04 dizem "Corrigido". O `validate_course.py` conta achado 🔴/🟠 fechado procurando exatamente `| 🟠 | Corrigido`, e o emoji extra fazia os quatro achados **já corrigidos** do módulo 02 aparecerem como abertos — um **ERRO** de gate `gate.open_findings` que travava o curso inteiro. Foi um falso positivo de formatação: nenhum fato, severidade ou desfecho mudou, e o `outcome: corrigido` já constava do manifesto JSON. Descoberto ao rodar os validadores depois da divisão da aula 13.
- **[2026-08-28]** **Fechar as duas últimas lacunas de conteúdo aprovadas.** (a) **Casco de tartaruga** entrou como seção da aula 05 do módulo 04 pela **opção (a)** do escopo — seção compacta mais poda de redundância na própria aula, que fica em **1.600 palavras** de corpo, dentro do teto. O **arquivo e o título não mudaram** ("coral e marfim"), pelo mesmo critério aceito quando a madrepérola entrou na aula 02: renomear quebraria wikilinks, questionário e flashcards sem ganho — quem se ampliou foi o **statement do objetivo `oa05`**. Quatro alegações novas `TRT-*`, não auditadas. (b) **Procedências mundiais** viraram as **aulas 20 e 21** do módulo 03 (bloco 5, ao fim), com objetivos novos `oa20` e `oa21`. As **províncias brasileiras não foram reescritas** — ficam na aula 21 do módulo 01, ligadas por wikilink. Módulo 03 com **21 aulas**; curso com **65**.
- **[2026-08-26]** Manter o **questionário único** no módulo 04, sem parciais: cinco aulas ficam abaixo do limiar de seis do plugin. O antigo parcial 3 virou o Bloco A, e as quatro questões biológicas do cumulativo antigo viraram o Bloco B de integração.
- **[2026-08-25]** Descartar `30-gemologia-diamantes/_claims_tmp.json`, arquivo temporário de trabalho da auditoria, que não segue o padrão de nomes do plugin e cujo conteúdo já está consolidado em `02-diamantes-auditoria.json`.

## Pendências abertas

1. ~~**Construir o módulo 03**~~ — feito em 2026-08-25, e dividido em dois módulos em 2026-08-26.
2. ~~**Auditar as alegações novas das aulas 01–06** do módulo 01.~~ — feito em **2026-08-27** (audit-and-fix, ~40 alegações). Veredito "aprovado com correções": 🟠 1 (`GEM-DIAG-004` — faixa de IR das granadas 1,714–1,830 → 1,714–1,888, que excluía andradita/demantoide) e 🟡 1 (`GEM-COR-006` — mecanismo de cor da opala reatribuído a Sanders, *Colour of Precious Opal*, Nature 204:1151, 1964). Ambas corrigidas e propagadas (aulas 02/03/04 + 4 campos de fonte de flashcards). Detalhe em [[01-gemologia-geral/01-gemologia-geral-auditoria|auditoria do módulo 01]], seção de 2026-08-27.
3. ~~**Ampliar o questionário parcial 1 do módulo 01**, escrito contra a versão curta das aulas 01–06.~~ — feito em **2026-08-27**. Acrescentadas 12 questões (Q78–Q89, +41 pts; parcial passou de 16/52 para 28/93), cobrindo o conteúdo do aprofundamento de 2026-08-25: origem da cor por mecanismo (campo cristalino × transferência de carga, idio/alo/pseudocromático); física óptica da aula 04 (lei de Snell, ângulo crítico, reflexão interna total, birrefringência e sinal óptico no refratômetro); os três requisitos de propriedade diagnóstica e a leitura combinada da tabela IR/DR; e as cinco perguntas do ofício (pedra montada, dupletes, efeito de flash). Matriz, seção "Cobertura" e o bloco `assessment` do módulo 01 em `course-state.yaml` (66 questões / 228 pts) atualizados. IDs `q11`–`q33` continuam aposentados.
4. ~~**Revisão didática do módulo 02**, que nunca foi feita.~~ — feita em **2026-08-27**: veredito "bem ensinado com ressalvas" (0 🔴 · 0 🟠 · 3 🟡 · 4 🔵). Três correções locais aplicadas (a03, a07, a04/a12). Encaminhamento aberto: grafia "rarísssimo" ainda nos questionários parcial 1 (Q8) e final (Q48).
5. **Publicar o curso no Notion** pela primeira vez e reconciliar as páginas órfãs listadas acima.
5-bis. **Passagem de qualidade nas cinco aulas e na seção acrescentadas em 2026-08-28** — aula 16 do módulo 02, aulas 18–21 do módulo 03 e a seção de casco de tartaruga na aula 05 do módulo 04. Nenhuma passou por **auditoria científica** (8 alegações `DIA-CUT-*`, 21 `SFE-/FDS-/DAN-/APA-/FLU-/CIA-/DIO-/SCP-/BRZ-/OUT-*`, 16 `PRO-*` e 4 `TRT-*`), por **revisão didática**, nem está coberta por **questão** ou **flashcard**. É a pendência maior do curso hoje.
6. **Ampliar o baralho da aula 14 do módulo 03**, que ficou com 5 cards na divisão de 2026-08-27 porque a repartição não podia criar card. As demais aulas do módulo têm entre 13 e 17. Não bloqueante.
7. **Regravar os `content_hash` das aulas 02, 03 e 04 do módulo 01 e 03, 04, 05, 07 e 12 do módulo 02**, que divergem dos arquivos em disco desde as correções de 2026-08-27 (audit-and-fix do módulo 01, revisão didática do módulo 02). O desvio foi **detectado**, não corrigido, na divisão da aula 13: recalcular o hash sem reverificar o conteúdo apagaria o único sinal de que aquelas aulas mudaram sem passar pelo estado. Não bloqueante.
8. **Formato de `claim_id`.** O curso usa três segmentos (`GEM-DR-001`, `DIA-EST-004`); o `audit.schema.json` do plugin exige quatro (`^[A-Z]{2,4}-[A-Z0-9]+-[A-Z0-9]+-[0-9]{3}$`). São ~100 alegações no módulo 01 e ~93 no módulo 02, e a divergência é **herdada** do curso de origem. Renomear todas exigiria tocar cada rodapé de aula, os dois relatórios de auditoria e os dois manifestos. Fica registrado como divergência conhecida, não como defeito novo.
