# Contexto — Curso de Geologia

> [!warning] Leia isto antes de estranhar a numeração e os IDs
> Em **2026-08-25** este curso foi partido em dois. Tudo o que era gemologia saiu daqui e virou o
> curso irmão **`../curso-gemologia`**. Com o buraco aberto, os módulos **07–29 foram renumerados
> para 06–28**, e **todos os identificadores mudaram de prefixo**. A seção "A separação de
> 2026-08-25", logo abaixo, explica o que mudou e o que isso custou.
>
> **Como ler as entradas datadas deste arquivo:** números de módulo dentro de entradas de
> "Decisões (registro por data)" e de notas históricas referem-se à numeração **vigente naquela
> data**. As seções de referência (escopo, trilhas, corte base/avançado, quando estudar cada
> módulo de apoio, pendências) foram atualizadas para a numeração atual.

## A separação de 2026-08-25

A gemologia crescera para uma área temática de três módulos — numerados 06, 30 e 31, com 23
módulos de geologia no meio — com bibliografia própria (GIA, Gem-A, CIBJO), público próprio e
sequência de estudo própria. Manter tudo num curso só distorcia a numeração e o dashboard do aluno.

### O que saiu daqui

| Era | Virou |
|---|---|
| `06-gemologia/` (22 aulas) | `../curso-gemologia/01-gemologia-geral/` |
| `30-gemologia-diamantes/` (15 aulas) | `../curso-gemologia/02-diamantes/` |
| `31-gemologia-coradas-perolas/` (pasta vazia) | `../curso-gemologia/03-gemas-coradas-perolas/` (a construir) |

### A renumeração

Os módulos **00–05 não mudaram de número**. Os módulos **07–29 desceram um**, fechando o buraco
deixado pelo 06:

| Antes | Depois | | Antes | Depois |
|---|---|---|---|---|
| 07 Rochas ígneas | **06** | | 19 Tectônica global | **18** |
| 08 Rochas sedimentares | **07** | | 20 Geofísica | **19** |
| 09 Rochas metamórficas | **08** | | 21 Métodos de campo | **20** |
| 10 Geoquímica | **09** | | 22 Recursos minerais | **21** |
| 11 Vulcanologia | **10** | | 23 Geologia do petróleo | **22** |
| 12 Intemperismo e solos | **11** | | 24 Oceanografia geológica | **23** |
| 13 Glaciologia | **12** | | 25 Geologia planetária | **24** |
| 14 Sedimentologia | **13** | | 26 Geologia do Brasil | **25** |
| 15 Estratigrafia | **14** | | 27 Química (apoio) | **26** |
| 16 Paleontologia | **15** | | 28 Física (apoio) | **27** |
| 17 Geobiologia | **16** | | 29 Matemática (apoio) | **28** |
| 18 Geologia estrutural | **17** | | | |

### A troca de prefixo dos IDs

| Era | Virou |
|---|---|
| `geologia-gemologia-mNN-oaNN` · `-aNN` · `-fbNNN` · `-fcNNN` · `-qNN` | `geologia-mNN-...` |
| `GG-MNN-Bnnn` · `GG-MNN-Cnnn` (módulos 00–04, 18, 27–29) | `geologia-mNN-fbnnn` · `geologia-mNN-fcnnn` |
| `course_id: geologia-gemologia` | `course_id: geologia` |
| Deck Anki `Geologia e Gemologia::MNN` | `Geologia::MNN` |
| Pasta `curso-geologia-gemologia/` | `curso-geologia/` |

A unificação dos dois formatos de ID de flashcard resolveu de quebra um defeito real: `GG-M00-B007`
**nunca passou** no `validate_flashcards.py`, que exige o padrão `<curso>-mNN-fbNNN`. Nove módulos
usavam o formato inválido.

### O custo, aceito de olhos abertos

**Anki.** Como o ID de cada card mudou, o Anki trata os cards importados a partir desta versão como
**novos**: o histórico de repetição espaçada dos cards já revisados não é aproveitado. A decisão foi
do usuário, com o custo conhecido de antemão. **Recomendação prática:** apague os decks antigos
`Geologia e Gemologia::*` antes de importar os CSVs novos, ou você ficará com dois baralhos do
mesmo conteúdo.

**Notion.** O `page_map` (`notion_sync.pages` no `course-state.yaml`) **foi preservado**: o campo
`file` de cada entrada foi reapontado para o caminho novo e o `page_id` ficou intacto. Na prática
isso significa que a próxima sincronização **atualiza** as mesmas páginas em vez de duplicá-las —
melhor do que se esperava quando a decisão foi tomada. O que **não** foi resolvido, e continua como
ação manual do usuário: as 14 páginas do antigo módulo 06 (Gemologia) continuam sob a árvore deste
curso no Notion e precisam ser movidas ou apagadas à mão. Os `page_id` estão listados em
`../curso-gemologia/_contexto.md`. Os títulos das páginas dos módulos renumerados ainda dirão o
número antigo até a primeira republicação.

### O que foi limpo junto

A gemologia tinha vazado para fora dos seus módulos. Foi removida de:

- **M00, aula 01** — "gema" deixou de ser um dos conceitos centrais; a aula passou de seis para
  quatro palavras (mineral, rocha, cristal, fóssil). Saíram a linha do vocabulário, a seção
  inteira, o exemplo (d), três flashcards Basic, um Cloze, duas alegações de auditoria e duas
  questões do questionário.
- **M01, aula 01** — a seção "Onde a gemologia entra" virou "Por que existem subáreas aplicadas
  fora deste mapa", que ensina a mesma lição metodológica sem depender do conteúdo que saiu.
  Duas questões e dois flashcards ajustados.
- **M04** (cristalografia) — as remissões a esmeralda, água-marinha e "módulo 06" viraram
  enquadramento puramente mineralógico. O berilo continua sendo o exemplo do sistema hexagonal.
- **M05** (mineralogia) — a navegação "Próximo: Módulo 06 — Gemologia" passou a apontar para
  Rochas ígneas, com um aviso de que este módulo e o M04 são o pré-requisito do curso irmão.
- **M06** (rochas ígneas, ex-07) — "Anterior: Módulo 06 — Gemologia" passou a apontar para o M05.
- **Decks** dos módulos de vulcanologia e intemperismo, que ainda diziam "Geologia e Gemologia::".

**Não foi tocado**, porque não é contaminação: **sal-gema** (a rocha evaporítica de halita, no
módulo de rochas sedimentares) e a **analogia do ovo cozido** na aula 04 do M00, em que "gema"
é gema de ovo. As fontes do GIA citadas no módulo de rochas ígneas também ficaram: *Gems & Gemology*
é periódico revisado por pares e o artigo citado é sobre petrologia, não sobre gemas.

### Arquivos deliberadamente não renumerados

São instantâneos e artefatos de trabalho, preservados como registro histórico. Os números de módulo
dentro deles referem-se à numeração anterior a 2026-08-25:

`course-state.pre-repair.yaml` · `course-state.yaml.bak-20260824` · `_relatorio-lacunas-transcricoes.md` ·
`_sync_batch_ready.json` · `_sync_modules_00_16.json` · `_sync_status_detailed.json` ·
`_modules_17_26_structure.json` · e a pasta `_arquivo-nivel-antigo/` de cada módulo.

## Perfil e nível
- **Nível de partida: ensino médio completo, sem pressupor domínio prévio de geologia.** Química, física, matemática e biologia escolares podem ser reativadas, mas não tratadas como domínio técnico consolidado. Calibrado em 2026-08-17.
- Nível de chegada: avançado / especialista — cobertura de graduação plena em geociências. **A chegada não foi rebaixada na repartida.** (Até 2026-08-25 esta linha incluía também o núcleo do Graduate Gemologist; isso passou para o curso irmão de Gemologia.)
- Aplicação prática: não declarada; formação ampla e completa.

## Contrato de nível (ensino-medio-sem-geologia-v1)

Vale para toda aula gerada ou revisada a partir de 2026-08-17. A versão canônica, com os IDs das regras, está em `course-state.yaml` sob `level_contract` — é ela que o `revisor-didatico` deve verificar. Em resumo:

1. **LC-01 — Nenhum termo sem definição.** Todo termo técnico é definido em linguagem comum na mesma frase ou na seguinte, na primeira vez que aparece na aula. Termos gerais do ensino médio podem receber apenas uma reativação curta; termos de geociências continuam sempre definidos.
2. **LC-02 — Teto de 1.600 palavras** de corpo por aula. Isso é o que de fato cabe em 30 minutos para quem entra sem geologia e precisa parar para pensar. O que não cabe vira Parte 1 / Parte 2, ou é deferido — nunca é comprimido.
3. **LC-03 — Abertura padronizada:** bloco "Vocabulário desta aula" (5 a 8 termos) e bloco "Antes de começar, você precisa saber", que linka as aulas anteriores exigidas. O aluno tem que poder detectar sozinho que voltou cedo demais.
4. **LC-04 — Analogia antes do termo.** O cotidiano vem primeiro, o nome técnico depois. Não o contrário.
5. **LC-05 — Ordem de grandeza, não precisão de laboratório.** "Cerca de 2.900 km", não "2.891 km". Efeito colateral valioso: elimina de uma vez a classe de achado de auditoria por valor desatualizado ou inconsistente entre aulas — que foi exatamente o defeito M02-F01 encontrado no módulo 02.
6. **LC-06 — Matemática reativada antes do uso.** Exponencial, logaritmo, vetor e tensor só aparecem depois de revisão explícita. As aulas-ponte são nivelamento opcional: podem ser puladas após checagem diagnóstica e ficam como referência.
7. **LC-07 — "Erros comuns", "O que não concluir" e "Recap relâmpago" continuam obrigatórios.** São o que impede que simplificar vire mentir.
8. **LC-08 — Controvérsia em uma frase.** No nível iniciante, a controvérsia de literatura entra como pergunta em aberto declarada, sem o detalhe do debate. O aluno precisa saber que a pergunta existe; não precisa arbitrá-la.

### Política de deferimento
Conteúdo cortado de uma aula na repartida **não é descartado**. Cada corte é registrado no campo `deferred_content` do módulo de origem, com o módulo de destino, e reaparece como objetivo de aprendizagem lá. Simplificar o começo não pode virar buraco no fim.

## Escopo
- Cobertura completa das áreas das geociências, seguindo a taxonomia fornecida pelo usuário: fundamentos, materiais, rochas, geoquímica, vulcanologia, processos de superfície (geomorfologia, pedologia, glaciologia), estratigrafia, paleontologia, geobiologia, estrutural, tectônica/geodinâmica, geofísica, métodos de campo, recursos/econômica, geologia do petróleo, oceanografia, planetologia, geologia do Brasil, e as áreas aplicadas.
- Áreas muito específicas/aplicadas ao final (bloco VIII).
- **Módulo 00** funciona como revisão/nivelamento opcional de vocabulário, escalas, mapas e observação. Não é pré-requisito obrigatório do M01.

## Trilhas de estudo paralelas (curso inteiro, desde 2026-08-18)
O aluno decidiu não estudar o curso em bloco sequencial por área — quer alternar entre frentes diferentes por sessão, respeitando o grafo de pré-requisitos real do `course-state.yaml`. Isso é preferência de **ordem de estudo do aluno**, não muda `prerequisites`, `id` nem pasta de nenhum módulo.

A tentativa inicial (2026-08-18) foi só trilhar o que faltava a partir da Geobiologia. O aluno pediu para estender a trilhas o curso inteiro, desde o módulo 00. Isso expôs um ponto real de currículo: os módulos 01, 03, 04 e 05 são pré-requisito de quase tudo que vem depois (o 05/Mineralogia sozinho condiciona 06, 07, 08, 09, 20 e 28, e indiretamente 17 e 21) — criar "trilhas" ali seria cosmético, não uma escolha real de estudo. A estrutura adotada por isso tem um **tronco comum sequencial** e só abre em trilhas paralelas depois dele.

> **Numeração atualizada em 2026-08-25.** As trilhas abaixo já usam a numeração nova (07–29 → 06–28). A composição das trilhas não mudou; só os números. A antiga trilha 2 começava pela Gemologia, que saiu do curso.

- **Tronco comum** (sequencial, sem paralelismo real, concluído): 00 → 01 → 03 → 04 → 05.
- **Trilha 1 — Vida, superfície e ambiente**: 11 Intemperismo/solos/geomorfologia → 12 Glaciologia → 13 Sedimentologia e ambientes → 14 Estratigrafia e correlação → 15 Paleontologia e história da vida → 16 Geobiologia → 24 Geologia planetária → 23 Oceanografia geológica.
- **Trilha 2 — Materiais, rochas e recursos**: 06 Rochas ígneas → 07 Rochas sedimentares → 08 Rochas metamórficas → 09 Geoquímica → 20 Métodos de campo → 21 Recursos minerais → 25 Geologia do Brasil.
- **Trilha 3 — Terra dinâmica e aplicações**: 02 Sistema Terra → 10 Vulcanologia → 17 Geologia estrutural → 18 Tectônica global → 19 Geofísica → 22 Geologia do petróleo.

As trilhas 1 e 3 terminavam em módulos da antiga área VIII (Geologia ambiental, Engenharia de petróleo, Geologia de engenharia, Geometalurgia), removidos em 2026-08-23 — esses assuntos vivem hoje em `../curso-geologia-avancado/`, que é a continuação natural das três trilhas.

O módulo **02** saiu do tronco comum e virou o primeiro nó da trilha 3: ele só depende do 01, e nada entre os módulos 03–09 depende dele — não precisa ficar no tronco.

Há dependências cruzadas inevitáveis entre trilhas, dado o grafo real do curso — não é defeito da estruturação:
- 11 (trilha 1) precisa do 07 (trilha 2).
- 16 (trilha 1) precisa do 09 (trilha 2).
- 20 (trilha 2) precisa do 14 (trilha 1) e do 17 (trilha 3).
- 21 (trilha 2) precisa do 18 (trilha 3).
- 17 (trilha 3) precisa do 08 (trilha 2).
- 10 e 24 (trilha 3) precisam do 06 e/ou 09 (trilha 2).

Ao gerar a próxima aula por padrão, respeitar esta ordem de trilhas em vez da ordem numérica pura dos módulos, salvo pedido explícito em contrário. `00-dashboard.md` e `00-progresso-do-aluno.md` refletem esta estrutura.

### Trilha de apoio — Ciências para geociências (opcional, desde 2026-08-19)

Quarto braço, **paralelo ao tronco e às trilhas 1–3, e não bloqueante**. Não tem ordem própria dentro do curso: cada módulo é consultado quando o aluno sente falta da base, ou preventivamente antes do módulo de geologia que mais se apoia nele.

- **26 — Química para geociências:** reações, soluções e equilíbrio (5 aulas).
- **27 — Física para geociências:** grandezas, forças e energia (6 aulas).
- **28 — Matemática para geociências:** vetores, trigonometria, funções e estatística (4 aulas).

Total: 15 aulas. Os três módulos têm `prerequisites: []` e `status: completed`, e ficam sob a área `A. Trilha de apoio (opcional): ciências para geociências` — rótulo deliberadamente fora da numeração romana das áreas I–VII, pelo mesmo motivo que o módulo 00 usa `0. Nivelamento opcional`: não é um estágio da progressão, é material de consulta lateral.

> Numeração, duas vezes mexida: estes três módulos eram **31, 32 e 33** até 2026-08-23, quando a antiga área VIII foi removida e eles viraram **27, 28 e 29**; e viraram **26, 27 e 28** em 2026-08-25, com a saída da gemologia. Materiais impressos ou páginas antigas do Notion podem citar qualquer uma das numerações anteriores.

**Quando estudar cada um** (recomendação, não trava):

| Módulo de apoio | Estudar antes de / junto de |
| --- | --- |
| 28 — Matemática, aula 03 (exponenciais e logaritmos) | M03 (meia-vida) |
| 28 — Matemática, aulas 01–02 (trigonometria, vetores) | M17, M20 |
| 28 — Matemática, aula 04 (estatística) | M20, M21 |
| 26 — Química (módulo inteiro) | M09, M11 |
| 26 — Química, aula 03 (soluções e pH) | hidrogeoquímica e contaminação de águas subterrâneas (curso avançado, módulos 02 e 03) |
| 27 — Física, aulas 01–04 (medida, forças, pressão, energia) | M17 |
| 27 — Física, aula 05 (calor) | M06, M08, M10 |
| 27 — Física, aula 06 (campo) | M19 |

O **28 (Matemática)** é o de maior alcance sobre o resto do curso e é o candidato natural a ser estudado primeiro entre os três, ainda que a produção tenha começado pela Química.

## Corte base / avançado (decidido em 2026-08-18)
A base deste curso **fecha no módulo 25** (fim da área VII — "Métodos, recursos e regional"); era o módulo 26 antes da renumeração de 2026-08-25. A área VIII ("Áreas especializadas e aplicadas": 27 Geologia ambiental e hidrogeologia, 28 Geologia de engenharia, 29 Geometalurgia, 30 Engenharia de petróleo) passa a ser tratada como a semente de um **curso avançado separado**, futuro, que os complementará com módulos novos de especialização mais profunda (ex.: geofísica avançada, geologia estrutural quantitativa, geoquímica isotópica avançada) em vez de continuar dentro deste `course-state.yaml`.

Razão do corte: a área VII ainda é conhecimento geral esperado de qualquer geólogo (mapeamento, recursos, geologia regional); a área VIII já é especialização aplicada — o próprio nome da área, definido em 2026-07-20, já sinalizava essa fronteira.

**Execução do corte (2026-08-23).** A área VIII foi **removida deste curso**. Os quatro módulos 27–30 eram esqueletos vazios (só o hub `-modulo.md`, nenhuma aula, `status: pending`) e seus objetivos de aprendizagem já haviam sido reaproveitados e expandidos no curso avançado irmão `../curso-geologia-avancado/`:

| Módulo removido daqui | Onde o conteúdo vive agora (curso avançado) |
| --- | --- |
| 27 — Geologia ambiental e hidrogeologia | 01 Hidrogeologia e recursos hídricos · 02 Hidrogeoquímica · 03 Contaminação de águas subterrâneas · 04 Exploração e gestão de águas subterrâneas |
| 28 — Geologia de engenharia | 05 Mecânica de rochas · 06 Elementos de geomecânica · 07 Mapeamento geotécnico · 08 Geotecnia ambiental |
| 29 — Geometalurgia | 09 Geometalurgia |
| 30 — Engenharia de petróleo | 10 Tectônica de bacias sedimentares · 11 Sismoestratigrafia · 12 Engenharia de petróleo |

Com a remoção, a trilha de apoio (Química, Física, Matemática) foi renumerada de 31–33 para 27–29, e o curso passou a ter 30 módulos (00 a 29). *(Em 2026-08-25 a gemologia saiu também, e o curso passou a ter **29 módulos: 00 a 28**, com a trilha de apoio em 26–28.)*

## Fora do escopo (e por quê)
- **Gemologia inteira.** Saiu deste curso em 2026-08-25 e vive em `../curso-gemologia`. Os módulos 04 e 05 daqui são o pré-requisito de lá, e a dependência é citada por nome, nunca por wikilink — wikilink entre cursos quebra no Obsidian.

### Lacunas da grade da USP conscientemente não implementadas (2026-08-28)
O cruzamento com a grade obrigatória do IGc-USP feito em 2026-08-28 fechou quatro lacunas (ver a decisão daquela data). Estas outras foram examinadas e **deliberadamente não viraram módulo**:

| Disciplina da USP | Por que fica de fora |
| --- | --- |
| PCC2110 — Desenho para Geologia | A parte de *drafting* técnico é habilidade manual de prancheta e de CAD, não conteúdo geológico. A parte que importa (ler e construir seção e mapa) já está nos módulos 20 e 17. |
| 4300270 — Eletricidade e Magnetismo I · 4300357 — Oscilações e Ondas · QFL0404 — Físico-Química IV | Decisão de escopo já registrada: a trilha de apoio ensina física e química **no nível que a geologia usa**, não no nível de um curso de exatas. O que a geofísica (M19) e a geoquímica (M09) precisam de campo, onda e termodinâmica é ensinado dentro dos módulos 27 e 26. |
| BIO0103 — Biologia Evolutiva | Coberta contextualmente nos módulos 15 (Paleontologia e história da vida) e 16 (Geobiologia), onde a evolução aparece amarrada ao registro fóssil em vez de isolada. Um módulo próprio duplicaria. |
| 0440335 — Estágio Supervisionado · 0440500 — Trabalho de Formatura · disciplinas de campo | Não são replicáveis em autoestudo: dependem de orientação institucional, de afloramento real e de banca. Mesmo critério já aplicado no curso avançado. |

### Pendências de decisão em aberto (2026-08-28) — não implementar sem o usuário decidir
Quatro temas ficaram identificados como candidatos legítimos a módulo novo, mas **nenhum foi criado**, porque cada um exige uma decisão de escopo que só o usuário pode tomar:

1. **Geoética e responsabilidade profissional.** Hoje o assunto só aparece de raspão no módulo 41 do curso avançado (uma aula sobre ética, meio ambiente e relacionamento social em projetos de exploração). Decisão pendente: vira aula avulsa no curso base, módulo próprio, ou continua diluída?
2. **Geologia do Quaternário** (GAA0393, optativa). Hoje coberta em pedaços: glaciologia (M12), geomorfologia (M11), estratigrafia (M14). Decisão pendente: o Quaternário merece tratamento próprio — datação por ¹⁴C e OSL, mudanças de nível do mar, registro paleoclimático — ou o recorte atual basta?
3. **Pedologia aplicada** (GAA0425, optativa). Hoje o M11 trata solo como produto do intemperismo, não como objeto de classificação (SiBCS, WRB), de levantamento e de uso. Decisão pendente: aprofundar dentro do M11 ou abrir módulo.
4. **Geoquímica orgânica** (GAA0311, optativa). Hoje só o que o M22 usa para o sistema petrolífero. Decisão pendente: biomarcadores, maturação e proxies paleoambientais justificam módulo próprio?

Registrados aqui para não se perderem entre sessões. Enquanto não houver decisão, **não** gerar conteúdo para eles.

### Status explícito das optativas em limbo (2026-08-29)
A revisão de 2026-08-29 conferiu o fechamento das quatro lacunas obrigatórias e constatou que as optativas acima estavam registradas sem **status declarado** — nem cortadas, nem adiadas, nem planejadas — e que três outras nem apareciam. Todas recebem agora status explícito. O status `adiado` significa **decisão do usuário pendente**: o tema é candidato legítimo, o custo de adiar é zero hoje, e nenhum conteúdo deve ser gerado até que o usuário decida. Nenhuma foi cortada por decisão minha — cortar é decisão de escopo do usuário.

| Disciplina da USP | Status | Onde o assunto encosta hoje | O que a decisão precisa resolver |
| --- | --- | --- | --- |
| GMG0201 — Geoconservação e Geoética | **adiado** | Só de raspão no M41 do curso avançado (ética e relacionamento social em projetos) | Aula avulsa no curso base, módulo próprio, ou continua diluída? |
| GAA0393 — Geologia do Quaternário · GAA0291 — Palinologia de Quaternário | **adiado** | Em pedaços: M12 (glaciologia), M11 (geomorfologia), M14 (estratigrafia), M15 (registro fóssil) | Módulo próprio de Quaternário (¹⁴C, OSL, nível do mar, paleoclima) com a palinologia como uma de suas aulas de proxy, ou o recorte atual basta? A palinologia sozinha não sustenta módulo. |
| GAA0425 — Pedologia Aplicada | **adiado** | M11 trata solo como produto do intemperismo, não como objeto de classificação (SiBCS, WRB), levantamento e uso | Aprofundar dentro do M11 ou abrir módulo próprio? |
| GAA0311 — Geoquímica Orgânica · GAA0202 — Geoquímica Ambiental e Forense | **adiado** | GAA0311: só o que o M22 usa para o sistema petrolífero. GAA0202: a camada analítica encosta no M09 daqui e nos módulos 02, 03 e 28 do curso avançado | São dois temas distintos e o pareamento é de conveniência: biomarcadores/maturação (orgânica) versus rastreamento e forense (ambiental). Decidir cada um por si — e, no caso da GAA0202, decidir se ela pertence a este curso ou ao avançado. |
| GAA0289 — Geologia dos Terrenos Cársticos | **adiado** | Dissolução de carbonatos no M11, ambientes carbonáticos no M13, e o aquífero cárstico encosta nos módulos 01–04 do curso avançado | Carste é um sistema (geomorfologia + hidrogeologia + espeleotema como registro paleoambiental + risco geotécnico) que hoje aparece fatiado em quatro módulos e em dois cursos. Decidir se vira módulo integrador e em qual dos dois cursos. |

### Obrigatórias de campo — status de corte (2026-08-29)
A linha "disciplinas de campo" da tabela de 2026-08-28 fica com os códigos nomeados, para não depender de memória de sessão:

| Disciplina da USP | Status | O mais próximo que existe |
| --- | --- | --- |
| GMG0401 — Mapeamento Geológico · GAA0304 — Mapeamento Geológico de Terrenos Sedimentares (componentes de campo) | **cortado** | M20 deste curso (métodos de campo e mapeamento, agora com topografia instrumental nas aulas 07–10) e M41 do curso avançado (estudos integrados). O que é transmissível está nesses dois; o que depende de afloramento real, de logística e de banca não é replicável em autoestudo. |
| 0440335 — Estágio Supervisionado · 0440500 — Trabalho de Formatura | **cortado** | Mesmo critério: dependem de orientação institucional e de banca. |

## Preferências de ensino
- Destino: Obsidian. Aulas de no máximo 30 min; assuntos grandes divididos em partes.
- Progressão do básico ao avançado, sem usar conceito antes de ensiná-lo. Na repartida essa regra deixou de ser aspiracional e virou verificável (LC-01, LC-03).

## Sincronização com a dashboard no Notion

- **Gatilho obrigatório:** sempre que uma aula for publicada no Notion, atualizar também a dashboard **Central de Estudos** na área `Cursos`.
- **Registro da aula:** localizar a aula pelo módulo e pela ordem no módulo; se ela ainda não existir, criá-la relacionada ao curso **Geologia — do essencial ao avançado** e ao módulo correspondente. Registrar título, duração, caminho/URL de origem quando disponível e o agente responsável. Ao publicar, preencher obrigatoriamente `Link da aula` com a URL da página publicada no Notion: esse é o atalho clicável exibido na view **Próxima aula**.
- **Estado de produção:** definir `Status IA` como `Publicada` apenas depois de a página/aula estar efetivamente publicada no Notion **como subpágina do módulo correspondente em `Curso: Geologia — do essencial ao avançado`**. Na mesma operação, gravar essa URL em `Link da aula` e conferir o atalho `Abrir aula publicada`. Antes disso, usar o estágio real do fluxo (`Planejada`, `Em geração`, `Pronta para revisão` ou `Revisada`).
- **Progresso do aluno é independente:** a sincronização de publicação nunca pode alterar `Status do aluno`, `Data assistida` ou o status de estudo de módulos e cursos. Esses campos pertencem exclusivamente ao aluno.
- **Conferência:** após cada sincronização, confirmar que a aula está relacionada ao curso e ao módulo certos. Os rollups de `Progresso IA` são atualizados automaticamente; não editar seus valores manualmente.

## Sincronização com a dashboard no Obsidian

- A página `00-dashboard.md` é a entrada do aluno no vault; `00-progresso-do-aluno.md` guarda as marcações de aulas assistidas.
- Ao criar uma aula local, incluir seu wikilink no módulo correspondente de `00-progresso-do-aluno.md` e atualizar os totais e a próxima aula em `00-dashboard.md`.
- Nunca substituir uma caixa já marcada pelo aluno (`- [x]`) durante atualizações automáticas; o progresso pessoal continua sendo dado do aluno, não do agente.
- **Desde 2026-08-25:** as duas páginas são **geradas** por `build_student_dashboard.py` a partir do `course-state.yaml`. O script preserva as caixas já marcadas pelo aluno casando pelo **caminho do arquivo linkado**, nunca pelo texto do link — por isso a renumeração de 2026-08-25 foi feita **antes** da regeração, para que os caminhos batessem e nenhuma marca se perdesse. A ordem de apresentação vem do campo `study_tracks` do estado; na ausência dele, cai na ordem numérica dos módulos. *(A regra anterior, de 2026-08-18, mandava inserir seções à mão seguindo a ordem das trilhas; ela foi substituída pela geração automática.)*

## Decisões (registro por data)
- [2026-07-20] Destino Obsidian.
- [2026-07-20] Gemologia como módulo único, movido para logo após a mineralogia (M06).
- [2026-07-20] Cobertura ampliada para a taxonomia do usuário: adicionados Vulcanologia (M11), Glaciologia (M13), Geobiologia (M17), Geologia do petróleo (M23), Geometalurgia (M29), Engenharia de petróleo (M30).
- [2026-07-20] Geodinâmica incorporada à Tectônica global (M19). Sismologia, gravimetria, magnetometria e sísmica dentro de Geofísica (M20).
- [2026-07-20] Áreas muito específicas/aplicadas movidas para o bloco final (VIII).
- [2026-08-15] Correção técnica: IDs dos módulos 08 e 09 estavam sem aspas em `course-state.yaml` — corrigido em todas as 10 ocorrências.
- [2026-08-15] Módulo 02 concluído. A auditoria do M02 corrigiu uma inconsistência numérica real entre duas aulas do próprio módulo (taxa de espalhamento da Elevação do Pacífico Leste, achado M02-F01) — evidência de que auditar as aulas **em conjunto**, e não uma a uma, é o que pega esse tipo de defeito. Manter essa prática.
- **[2026-08-17] Entrada recalibrada para ensino médio completo.** O curso não pressupõe geologia prévia, mas deixa de tratar química, física, matemática e biologia escolares como inexistentes. Nenhuma aula M00–M05 foi reescrita e nenhum conteúdo foi descartado. O M00 e todas as aulas-ponte passam a ser revisão/ nivelamento opcional, pulável mediante checagem dos respectivos objetivos; seguem disponíveis como referência. O M01 deixa de exigir formalmente o M00. Para M06 em diante, futuras redações devem reativar pré-requisitos escolares de modo breve e usar as pontes completas apenas quando o diagnóstico indicar necessidade.
- **[2026-08-16] Repartida do zero.** O usuário determinou que o curso estava pesado demais para quem entende pouco da área. Decisões tomadas:
  - **Decisão histórica, superada em 2026-08-17 quanto ao nível de entrada.** A granularidade, o M00 e as pontes foram preservados; mudou apenas seu papel para revisão/nivelamento opcional.
  - Nível de partida passa de "alguma base" para **zero absoluto**; nível de chegada **inalterado**.
  - Criado o **módulo 00 — Partida do zero** (6 aulas). Numerado 00 de propósito: renumerar os 30 módulos existentes quebraria todos os nomes de pasta, todos os caminhos no estado e todos os wikilinks do vault, por ganho zero.
  - Adotado o **contrato de nível** acima, com IDs verificáveis.
  - Criadas **8 aulas-ponte** (M02, M03, M04 ×2, M05, M10, M16, M18, M20) que ensinam onda, átomo, ligação química, luz, energia, classificação biológica, tensão e campo. Eram os pontos onde o currículo antigo exigia conhecimento que nunca entregou.
  - Volume: 30 → 31 módulos, ~161 → ~205 aulas, ~80–96 h → ~115–130 h. **Nenhum tópico foi removido do curso**; o aumento é de granularidade e de pontes.
  - Pré-requisito do **M04 muda de 02 para 01 + 03**, porque a ponte de átomos e isótopos do M03 passa a ser a base da química do M04. O M10 ganha o 03 como pré-requisito pelo mesmo motivo.
  - Módulos 01, 02 e 03 marcados como `rewriting`. Auditorias passam a `stale`; questionários e baralhos passam a `needs_review`.

- **[2026-08-16] Bloco I fechado.** Módulo 00 escrito (6 aulas novas). Módulos 01, 02 e 03 reauditados sobre o texto reescrito, mais uma auditoria transversal dos quatro. Resultado: **0 achados 🔴**, 4 🟠 encontrados e corrigidos, 4 🔵 de fonte resolvidos. Questionários reconciliados e os três baralhos regenerados.
  - O achado mais importante foi **transversal**, e nenhuma auditoria de módulo isolado o teria visto: a espessura da crosta continental aparecia como **30–40 km** em M00-a04 e M02-a04 e como **30–50 km** em M01-a05 e M02-a02 — inclusive **duas vezes dentro do módulo 02**. Harmonizado para 30–50 km (USGS).
  - É a **segunda vez** que a inconsistência numérica entre aulas é o achado mais grave de uma rodada (a primeira foi M02-F01). Confirma a prática de auditar as aulas **em conjunto**. Manter, e manter também a auditoria transversal por bloco.
  - Os baralhos precisaram ser **regenerados, não corrigidos**: apontavam para estruturas de aula que deixaram de existir, não tinham card algum sobre as aulas-ponte novas, e carregavam dezenas de cards órfãos. Lição para os próximos módulos: **baralho gerado antes de uma reestruturação não sobrevive a ela.**
  - O baralho antigo do M03 usava "disconformidade" e "não conformidade", termos que o texto reescrito não emprega (usa **desconformidade** e **inconformidade**). Divergência de terminologia entre baralho e aula é um defeito silencioso — incluir essa checagem nas próximas auditorias.
  - Atenção na migração para o Anki: **reimportar CSV não apaga card antigo**. Os índices de baralho dos três módulos trazem a lista do que suspender ou apagar.

- **[2026-08-16] Avaliação do módulo 00.** Última pendência do bloco I. Gerados o questionário final (19 questões, 40 pontos) e o baralho (101 cards: 62 Basic + 39 Cloze), ambos **depois** da auditoria e contra o texto já corrigido. O bloco I passa a ter os quatro módulos completos — aulas, auditoria, avaliação e memorização.
  - O M00 é o **primeiro módulo do curso cujo material derivado nasce depois da auditoria**, e não antes. Nos M01–M03 a ordem foi a inversa, e foi exatamente isso que obrigou à reconciliação dos questionários e à regeneração dos baralhos. A ordem correta — auditar, corrigir, só então avaliar e cardificar — deve valer do M04 em diante.
  - Nenhuma migração de Anki a fazer no M00: o baralho é de primeira geração, sem IDs antigos a aposentar. Importar os dois CSVs em deck limpo.
  - Os dois achados 🟠 corrigidos viraram **item de cobrança** em vez de risco: o questionário cobra a régua corrigida (`M00-F01`) e a espessura harmonizada (`XC-F01`), e o baralho repete os dois valores certos. Prática a repetir: onde a auditoria corrigiu, o material derivado deve testar a versão corrigida.

- **[2026-08-16] Módulo 04 concluído.** As 7 aulas (2 pontes de química + 5 de cristalografia/mineralogia) foram auditadas **em conjunto**, contra fontes normativas (Klein & Dutrow, *Manual of Mineral Science*; Nesse, *Introduction to Mineralogy*; IUCr, *International Tables for Crystallography*; Mindat.org), seguindo a prática consolidada desde o módulo 02. Resultado: **53 alegações verificadas, 0 achados 🔴/🟠/🟡/🔵/⚪** — o primeiro módulo do curso, desde a repartida, a sair limpo na primeira auditoria.
  - O ponto de maior risco checado por busca web foi a classificação do quartzo como **trigonal** (não hexagonal). Fontes de divulgação geral frequentemente simplificam o quartzo como "hexagonal" pelo hábito externo; a aula 05 já trata essa confusão de propósito, explicando que o critério decisivo é a ordem real do eixo de rotação (3, não 6). Confirmado correto contra Klein & Dutrow e busca cruzada — não foi achado, foi a aula antecipando o erro mais comum da literatura de divulgação.
  - Hipótese de por que o módulo saiu limpo: cada aula já nasceu com o bloco `alegacoes_auditaveis` e fontes citadas desde a redação (prática que vem sendo reforçada desde o M00), e o domínio (cristalografia/mineralogia descritiva básica) é estável na literatura, sem fronteira de pesquisa em disputa — ao contrário de tectônica de placas ou geocronologia, que já geraram achados 🔵/⚪.
  - Questionário (20 questões, 46 pontos) e baralho (99 cards: 60 Basic + 39 Cloze) gerados **depois** da auditoria, contra o texto já verificado — mantendo a ordem correta adotada desde o M00 (auditar → corrigir → só então avaliar e cardificar), que evita a reconciliação forçada que os módulos 01-03 precisaram.
  - Primeiro baralho do módulo 04: sem migração de Anki a fazer, importar limpo.

- **[2026-08-18] Reestruturação do roadmap de estudo em trilhas paralelas, e corte base/avançado definido.** O aluno achou o curso pesado demais para estudar uma área inteira por vez e pediu para alternar entre frentes. Ver seções "Trilhas de estudo paralelas" e "Corte base / avançado" acima para o detalhe. Nenhum módulo foi renumerado, movido ou teve pré-requisito alterado — é só ordem de estudo preferida pelo aluno sobre o grafo já existente.
- **[2026-08-18] Trilhas estendidas para o curso inteiro (tronco + 3 trilhas).** A reestruturação acima só cobria os módulos que faltavam a partir do 17. O aluno pediu para aplicar trilhas desde o módulo 00. Como os módulos 01, 03, 04 e 05 são pré-requisito de quase tudo no curso, criar trilhas ali seria cosmético — a decisão foi manter um tronco comum sequencial (00→01→03→04→05) e só abrir em 3 trilhas paralelas depois dele (o módulo 02 saiu do tronco e foi para a trilha 3, por não ser pré-requisito de nada entre 03 e 10). `00-dashboard.md` e `00-progresso-do-aluno.md` foram reordenados fisicamente (seções por tronco/trilha em vez de ordem numérica), preservando todas as caixas já marcadas pelo aluno. Nenhum arquivo de aula foi movido — é só a ordem de apresentação nessas duas páginas.

- **[2026-08-18] Módulo 17 (Geobiologia) finalizado — e o primeiro módulo do curso em que a revisão didática, e não a auditoria, foi o que mudou a estrutura do material.** A auditoria científica já havia aprovado o módulo; foi a revisão didática que apontou que duas aulas estavam acima da carga que o contrato de nível suporta. Aplicadas as quatro recomendações que a revisão deixara explicitamente em aberto por exigirem outras skills:
  - **Aula 05 dividida** em `05a — Origem da vida na Terra` e `05b — Astrobiologia e critérios de biogenicidade`. A 05 tinha 1.850 palavras de corpo, ~16% acima do teto LC-02, e empacotava dois assuntos com massa de aula inteira cada.
  - **Aula 03 dividida** em `03a — carbono e enxofre` (os dois ciclos com registro mineral direto) e `03b — nitrogênio, oxigênio e o acoplamento`. A âncora sensorial do H₂S (cheiro de ovo podre) foi antecipada para abrir o ciclo do enxofre, em vez de só aparecer no exemplo trabalhado, mil palavras depois (LC-04).
  - **Questionário reescrito:** a antiga Q7 cobrava uma distinção causal ("causa última") que nenhuma aula ensinava — substituída por uma questão sobre por que ~3,2 Ga é limite mínimo do registro e não data de origem da nitrogenase, ponto que a aula trabalha explicitamente. O peso de OA-05 caiu de 33% para 23% da nota, e nenhum objetivo ficou fora da faixa 19–23%.
  - **Baralho corrigido:** cinco cards não atômicos quebrados em cards separados (`fb030`–`fb037`), e dois cards que citavam o número da aula na frente reformulados.
  - **Lição a repetir:** as duas controvérsias ⚪ abertas (`GEOBIO-LUCA-THERMO-001`, `GEOBIO-LHB-001`) não foram simplificadas para caber em LC-08 — foram **reposicionadas**. A pergunta em aberto entra em uma frase no corpo, e a cadeia de ressalvas auditada vai integralmente para "O que não concluir", que é onde o leitor já espera limites de interpretação. **Nenhuma ressalva foi cortada.** LC-08 é regra de posicionamento da controvérsia, não licença para apagá-la — e a divisão da aula é o que cria o espaço para obedecer às duas coisas ao mesmo tempo.
  - **Segunda lição:** a passagem de verificação pós-divisão (modo `audit`, escopo restrito a "o texto novo introduziu alegação fora do escopo auditado?") pegou **um erro factual introduzido pela própria reescrita** — uma frase de transição afirmando que o nitrogênio "quase não deixa mineral", quando é justamente o nitrogênio ligado a argilominerais que fornece o registro de δ¹⁵N de 3,2 Ga que a aula ensina. Reescrever material já auditado **cria** risco factual novo; a passagem de verificação curta e de escopo fechado é barata e pega isso sem reabrir a auditoria inteira. Adotar como padrão após toda divisão de aula.
  - De passagem, duas linhas do CSV Cloze (`fc004`, `fc012`) tinham ponto-e-vírgula dentro do campo de texto e teriam corrompido a importação no Anki. Defeito pré-existente, corrigido. Vale incluir validação de contagem de campos dos CSVs nas próximas rodadas.
  - Bookkeeping reconciliado: o nó `17` do `course-state.yaml` ainda dizia `pending` com zero aulas, embora todo o material estivesse no disco. As dashboards também estavam paradas no módulo 16 — foram acrescentados os módulos 17 a 20, que já existiam em disco e não apareciam. Totais reais: 145 aulas publicadas, 207 planejadas.

- **[2026-08-18] Base do curso concluída — módulos 21, 25, 22, 24, 23 e 26 gerados do zero.** Fechando o bloco VII (Métodos, recursos e regional), completando a base do curso (módulos 00–26) na ordem de trilhas definida em 2026-08-18: 21 → 25 → 22 → 24 → 23 → 26. Cada módulo passou pelo pipeline completo já consolidado no curso — aulas (contrato `ensino-medio-sem-geologia-v1`) → auditoria científica em conjunto → correção → questionário final → flashcards → reconciliação de estado — sem pular etapa.
  - **Único achado de auditoria da rodada:** módulo 21 (Métodos de campo), 🟠 — a regra dos V estava incompleta na primeira redação da Aula 03 (só 3 dos 4 casos, e um resumo mnemônico que generalizava incorretamente para "V sempre aponta rio acima" nos casos inclinados). Corrigido antes de gerar questionário e flashcards, seguindo a ordem já estabelecida no curso desde o M00. Os módulos 25, 22, 24, 23 e 26 saíram limpos na primeira auditoria — cinco em seis, mantendo a tendência já observada desde o M04 de que domínios com literatura estável (aqui: métodos de campo consolidados, geologia econômica, oceanografia geológica, geologia do petróleo, geologia regional do Brasil) tendem a gerar menos achados que domínios de fronteira de pesquisa ativa.
  - **Duas pendências de controvérsia do curso foram retomadas e fechadas** conforme o registro em "Pendências a retomar" deste arquivo: **M01-F03** (origem da Lua por impacto gigante) no M25, aula 01, mencionada de passagem sem reabrir o debate técnico; e **M01-F02** (rocha mais antiga do planeta, Acasta vs. Nuvvuagittuq) no M26, aula 02 — com atualização: pesquisa mais recente (2025) converge para Nuvvuagittuq (~4,16 Ga) como a mais antiga confiavelmente datada, mas a controvérsia metodológica sobre datação sem zircão permanece parcialmente aberta, tratada como tal (LC-08), não como fato fechado. M02-F05 (plumas mantélicas) foi avaliado para o M25 e para o M26 (aula 06, sobre a origem de grandes províncias ígneas) e tratado como questão em aberto nos dois módulos, sem forçar a controvérsia onde não havia conexão direta com os objetivos de aprendizagem.
  - **Correção de currículo no M23 (Geologia do petróleo):** o `course-state.yaml` trazia 6 objetivos de aprendizagem para apenas 5 aulas planejadas — uma inconsistência herdada do planejamento curricular original. Na geração, o antigo `oa04` ("integrar os elementos no conceito de sistema petrolífero") foi removido por redundância factual com `oa02`+`oa03` combinados, e exploração/reservatórios não convencionais foram renumerados para `oa04`/`oa05`, alinhando 1:1 aulas e objetivos — registrado explicitamente no hub do módulo para rastreabilidade.
  - **Bookkeeping:** `course-state.yaml`, os seis hubs de módulo, `00-dashboard.md` e `00-progresso-do-aluno.md` foram todos atualizados no mesmo lote, preservando a ordem de trilhas (não numérica) nas duas páginas de navegação e sem marcar nenhuma caixa de aula como assistida. Total do curso: 179 aulas publicadas.
  - **Pendência aberta:** revisão didática (`revisor-didatico`) não rodou para nenhum dos seis módulos novos, nem para vários módulos anteriores do curso — não bloqueia o fechamento da base, mas é a próxima ação de qualidade recomendada. Auditoria `cross-course` cobrindo os módulos 21–26 contra os módulos 00–20 também ainda não rodou. Módulos 27–30 (área VIII) permanecem deliberadamente fora de escopo.

- **[2026-08-19] Trilha de apoio criada (módulos 31, 32, 33 — hoje 27, 28, 29; ver a renumeração de 2026-08-23 abaixo) — reforço opcional, não pré-requisito.** O aluno comparou o curso com a grade de Geologia da USP (`GradeCurricular/Geologia-USP/grade.json`) e notou que a USP intercala, nos quatro primeiros períodos, Matemática (Geometria Analítica, Cálculo I/II, Cálculo Numérico, Estatística), Física (Medidas em Física, Mecânica, Eletricidade e Magnetismo I, Oscilações e Ondas) e Química (Química Geral, Físico-Química IV) como sustentação das cadeiras de geologia, e pediu para transformar isso em uma trilha dentro deste curso.
  - **A trilha não foi criada genericamente, e sim contra o que o curso já entrega.** Um módulo "de química" ou "de física" do zero duplicaria as pontes existentes. O levantamento encontrou 7 pontes já escritas — onda (M02 a01), átomos e isótopos (M03 a03), átomo/elétrons/tabela periódica (M04 a01), ligação química (M04 a02), luz e cristais (M05 a04), energia/ calor/equilíbrio (M10 a01) e classificação biológica (M16 a02) — mais reativação embutida de tensão no M18 a01 e de ondas, gravimetria, magnetometria e métodos elétricos ao longo do M20. Os três módulos novos cobrem **só o que sobra** desse mapeamento.
  - **Achado de currículo levantado no caminho, ainda em aberto:** o M18 declara o objetivo `geologia-gemologia-m18-oa01` ("reativar força, pressão e tensão em nível funcional") e o M20 declara `geologia-gemologia-m20-oa01` ("reativar o conceito de campo físico e descrever como se mede uma anomalia"), mas **nenhuma aula escrita cobre nenhum dos dois** — o M18 está em 7/8 aulas e o M20 em 6/8, e as aulas faltantes são justamente essas duas pontes. Ou seja: dois objetivos prometidos sem entrega. As aulas 03 (pressão e tensão) e 06 (campo físico) do módulo 32 cobrem exatamente esse conteúdo. **Decisão adiada, não tomada:** quando o M18 e o M20 forem fechados, o usuário decide se escreve as pontes ali como planejado ou se as substitui por um ponteiro para o módulo 32. Nada foi alterado no M18 nem no M20 nesta rodada.
  - **Segundo achado:** a ponte do M10 (aula 01, energia/calor/equilíbrio) tem cerca de 450 palavras e é inteiramente qualitativa. Ela não é revogada nem reescrita, mas não sustenta sozinha o M10 — daí a aula 04 do módulo 31 (equilíbrio e solubilidade, quantitativa) e a aula 05 do módulo 32 (calor e transporte de calor). Sobreposição deliberada e declarada, não duplicação.
  - **Reforço opcional, e não pré-requisito formal.** Nenhum `prerequisites`, `id` ou pasta dos módulos 00–30 foi tocado. Três razões, em ordem de peso:
    1. **Impossibilidade lógica no estado.** Os módulos 04, 05, 10, 12, 18 e 20 estão `completed`. Declarar um módulo `pending` como pré-requisito de um módulo já concluído deixaria o `course-state.yaml` num estado que nenhuma ordenação topológica satisfaz, e que o `validador-estrutural-do- curso` deveria acusar. Esse argumento sozinho decide a questão.
    2. **LC-06 já resolve o problema real.** A regra obriga reativação just-in-time dentro de cada aula que usa exponencial, logaritmo, vetor ou tensor. A trilha de apoio aprofunda o que a LC-06 apenas destrava; não substitui a reativação nem passa a ser condição dela.
    3. **Convenção do curso**, registrada em 2026-08-18: reorganização de trilha nunca altera `prerequisites`, `id` ou pasta de módulo existente.
  - Consequência prática: a trilha é **recomendada e sequenciável, mas nunca bloqueante**. A tabela "quando estudar" fica na seção "Trilha de apoio" acima. Nenhum gate de qualidade do plugin muda: os módulos 31–33 passam pelo mesmo pipeline (aulas → auditoria → correção → questionário → flashcards) e valem o mesmo contrato `ensino-medio-sem-geologia-v1` (LC-01 a LC-08).

- **[2026-08-23] Curso avançado planejado como projeto separado.** Seguindo a decisão de 2026-08-18 ("Corte base / avançado" acima), o currículo do curso avançado foi levantado e gravado em `../curso-geologia-avancado/` (`course-state.yaml`, `_curso.md`, `_contexto.md`, 13 hubs de módulo, todos pendentes). Base curricular: grade da USP (`GradeCurricular/Geologia-USP/grade.json`) cruzada com a cobertura deste curso, para não duplicar. Os módulos 01–04 do curso avançado reaproveitam os objetivos já declarados nos módulos 27–30 deste curso (ainda pendentes de conteúdo aqui também); **decisão adiada:** quando o build começar, decidir se o conteúdo desses quatro módulos é gerado uma vez e compartilhado entre os dois cursos ou duplicado. Nada foi alterado nos módulos 27–30 deste curso nesta rodada — continuam pendentes e fazem parte normal deste curso, como já decidido. *(Superado no mesmo dia pela entrada "[2026-08-23] Área VIII removida" abaixo: a decisão adiada foi tomada — não duplicar; os 27–30 saíram deste curso.)*
  - **Numeração:** 31, 32, 33 na ordem química → física → matemática, que é a ordem de **produção** pedida (o `geo-redator` começa pelo 31). Não é a ordem de **estudo** recomendada — pelo alcance sobre o resto do curso, o 33 (Matemática) é o melhor ponto de entrada. Como os três têm `prerequisites: []`, as duas ordens podem divergir sem custo.
  - **Bookkeeping:** `estimated_lessons` 205 → 220 e `estimated_hours` 115–130 h → 123–138 h. Nenhuma aula escrita nesta rodada — o entregável foi a decisão curricular e o esqueleto de estado.
  - **Divergências de contagem pré-existentes, observadas e não corrigidas** (não foram introduzidas aqui, e mexer nelas estava fora do escopo): a soma de `lessons.planned` dá 221 contra `estimated_lessons: 220` (o mesmo desvio de 1 já existia antes: 206 contra 205); a soma de `lessons.completed` dá 165, o dashboard anuncia 179 aulas publicadas e há 205 arquivos de aula em disco. Vale uma passagem do `validador-estrutural-do-curso` para reconciliar.

- **[2026-08-20] Reconciliação de contagens de aulas realizada após conclusão da trilha de apoio.** A validação estrutural encontrou: 194 aulas reais em disco (M00-M26: 179 aulas; M31-M33: 15 aulas). O `estimated_lessons` foi atualizado de 220 para 194 (a contagem real). O dashboard foi atualizado para refletir 194 aulas disponíveis (antes dizia 184) e aulas planejadas = aulas reais. A soma de `lessons.planned` no `course-state.yaml` continua dando 221 (um a mais que 194, desvio não reconciliado — requer revisão manual do `course-state.yaml` módulo a módulo, fora do escopo da reconciliação automática). A soma de `lessons.completed` dá 180 (contra 194 em disco), divergência que indica 14 aulas declaradas como completed no state mas realmente existentes em disco — possivelmente aulas de módulos com status misto no state (alguns com status=pending apesar de terem aulas prontas, ou inversamente). Recomendação: passar um `gerador-de-curso-modular` em modo audit para investigar esses 14 casos de mismatch antes de tratar o estado como canônico de novo. *(Nota de 2026-08-23: onde esta entrada diz "M31-M33", leia "M27-M29" — ver a renumeração abaixo.)*

- **[2026-08-23] Área VIII removida deste curso; trilha de apoio renumerada 31–33 → 27–29.** A decisão de corte de 2026-08-18 foi finalmente executada. Os módulos 27 (Geologia ambiental e hidrogeologia), 28 (Geologia de engenharia), 29 (Geometalurgia) e 30 (Engenharia de petróleo) foram **apagados** deste curso: eram esqueletos vazios (só o hub `-modulo.md`, zero aulas, `status: pending`), e seus objetivos de aprendizagem já tinham sido absorvidos e **expandidos** nos módulos 01–12 do curso avançado irmão `../curso-geologia-avancado/` — manter os esqueletos aqui só criaria duas fontes concorrentes para o mesmo conteúdo. O mapeamento módulo-a-módulo está na seção "Corte base / avançado" acima.
  - **Renumeração da trilha de apoio.** Com o buraco de 27–30 aberto, os três módulos de apoio, que eram os últimos da lista, passaram a ocupá-lo: 31 Química → **27**, 32 Física → **28**, 33 Matemática → **29**. Isso é uma exceção deliberada à convenção de 2026-08-18 ("reorganização de trilha nunca altera `prerequisites`, `id` ou pasta de módulo existente") — a convenção existe para não quebrar referências, e aqui a alternativa (deixar 27–30 como buraco permanente na numeração) foi julgada pior para a navegação do aluno. A exceção foi paga com a atualização de **todas** as referências cruzadas, não só do nome da pasta.
  - **O que mudou junto com o número:** pastas e nomes de arquivo (`31-quimica-geociencias/31-quimica-geociencias-*` → `27-quimica-geociencias/27-quimica-geociencias-*`, idem física e matemática), `id` de módulo, `learning_objectives[].id` (`…-m31-oa01` → `…-m27-oa01`), `lessons.items[].id` e `covers_objectives`, IDs de flashcard nos CSVs (`…-m32-fb001` → `…-m28-fb001`), `claim_id` de auditoria (`GEO-M33-A01-*` → `GEO-M29-A01-*`), wikilinks, e as entradas `notion_sync.pages` (o `file:` foi reapontado, o `page_id` foi preservado — a página no Notion é a mesma).
  - **Referências cruzadas preservadas:** os objetivos `geologia-gemologia-m18-oa01` (força/pressão/tensão) e `geologia-gemologia-m20-oa01` (campo físico), declarados nos M18 e M20 e cobertos pelas aulas 03 e 06 da Física, **não mudaram de ID** — só o número do módulo que os cobre passou de 32 para 28, no texto do hub, das aulas e da auditoria da Física. A decisão adiada de 2026-08-19 (se o M18/M20 ganham aula própria ou passam a apontar para a Física) **continua em aberto**.
  - **Referências órfãs corrigidas:** o M17 (aula 01) apontava para "M27" ao falar do ciclo carbonato-silicato — repontado para o M12; o M26 (hub) e a aula 03 da Química apontavam para a área VIII — repontados para o curso avançado.
  - **Ação manual pendente do usuário:** as páginas dos quatro módulos removidos ainda existem no Notion e precisam ser apagadas à mão. A lista está no relatório desta rodada.

- **[2026-08-28] Fechamento de lacunas contra a grade obrigatória da USP — só planejamento.** O curso foi cruzado disciplina a disciplina com a grade de Geologia do IGc-USP (`GradeCurricular/Geologia-USP/Obrigatoria/`). Três lacunas de disciplina **obrigatória** sem cobertura foram fechadas **em nível de plano**: nenhuma aula, questionário ou flashcard foi gerado, para que o mapa curricular seja aprovado antes de qualquer produção.
  - **Topografia (PTR0201) → M20 expandido, 6 → 10 aulas.** O M20 cobria bússola, GPS de navegação, seção e coluna estratigráfica, mas não topografia instrumental. As aulas 07–10 (pendentes) e os objetivos `oa07`–`oa10` cobrem teoria dos erros e NBR 13133, planimetria e fechamento de poligonais, altimetria e curvas de nível, e sistema geodésico brasileiro / UTM / GNSS geodésico.
  - **Recursos energéticos (GAA0301) → módulo 29 novo,** área VII, 4 aulas, pré-requisitos 21 e 22. Havia petróleo (M22) e carvão/urânio como depósitos (M21), mas nenhuma visão de **sistema energético**: matriz global e brasileira, nuclear, geotérmica como recurso, renováveis, transição e CCS.
  - **Métodos numéricos (MAP0125) → módulo 30 novo,** trilha de apoio, 5 aulas, pré-requisito 28. É o **pré-requisito de fato** do módulo 23 do curso avançado (modelagem numérica geodinâmica), que pressupõe diferenças finitas e noção de erro numérico que nenhum módulo dos dois cursos ensinava.
  - **Por que um expandiu e o outro virou módulo — o critério é coerência temática, não conveniência.** Topografia **é** método de campo: um módulo separado ficaria órfão e, na área VII, exigiria renumerar os módulos 21–25, que já têm conteúdo em disco. Já MAP0125 é disciplina própria de 60 h com objetivo distinto do M28 (que ensina a matemática que se escreve no caderno; o 30 ensina o que acontece quando ela vai para o computador) — e manter o M28 lacrado preserva intactos sua auditoria, seu questionário e seu baralho já aprovados.
  - **Custo aceito no M20:** o módulo saiu de `completed` para `in_progress`. Seu questionário e seu baralho continuam válidos para as aulas 01–06, mas ficam **incompletos** em relação a `oa07`–`oa10` e terão de ser **estendidos, não regerados**, depois que as aulas 07–10 existirem e forem auditadas. Enquanto isso, o módulo não pode ser declarado concluído.
  - **Sem renumeração.** Os módulos 29 e 30 foram acrescentados no fim da numeração; nenhum módulo existente mudou de id, de pasta ou de nome de arquivo. Isto respeita a regra firmada depois das renumerações de 2026-08-23 e 2026-08-25. Na listagem, o 29 aparece dentro da área VII e o 30 fecha a trilha de apoio, porque `build_course_index.py` agrupa por área seguindo a **ordem do array** `modules`, não a ordem numérica dos ids — o 29 foi inserido logo após o 25 e o 30 no fim.
  - **Reparo de metadado feito de passagem:** as 6 aulas existentes do M20 não declaravam `status` no estado; passaram a declarar `completed`, o que elimina erros de schema e de contagem que o validador já acusava. O mesmo defeito persiste nos módulos 21–25 e não foi tocado nesta rodada, para manter o raio de alcance controlado.
  - **A quarta lacuna** (Exploração Mineral GAA0405 + Avaliação de Recursos Minerais GAA0404) foi fechada no curso irmão `../curso-geologia-avancado`, módulo 42, por ser matéria de especialização.
  - Volume: 29 → **31 módulos**, 183 → **196 aulas**, ~123–138 h → ~132–148 h.

- **[2026-08-29] Conferência do fechamento de lacunas e status explícito das pendências.** A sessão de 2026-08-29 reabriu a tarefa acreditando que o planejamento não tinha sido feito — o arquivo de retomada na raiz (`_RETOMAR-lacunas-grade-usp.md`) dizia "planejamento não iniciado", porque foi escrito **antes** da sessão de 2026-08-28 e nunca atualizado depois dela. A conferência contra o estado mostrou que as **quatro** lacunas já estavam plenamente planejadas e nada precisava ser recriado. O que faltava de fato, e foi feito agora:
  - **Nenhum módulo, objetivo ou aula foi criado, alterado ou renumerado nesta data.** Confirmado no estado: M20 com 10 aulas (07–10 pendentes) e 10 objetivos; M29 com 4 aulas e 4 objetivos; M30 com 5 aulas e 5 objetivos; os hubs dos três em disco. Recriar qualquer um deles teria duplicado trabalho já aprovado.
  - **Status explícito das optativas em limbo.** As quatro pendências de 2026-08-28 estavam anotadas sem status declarado, e três outras (GAA0289 Terrenos Cársticos; e, no curso avançado, GAA0342 Petrografia e Diagênese de Rochas Sedimentares e GMG0333 Introdução ao Magnetismo de Rocha) não estavam anotadas em lugar nenhum. Todas passaram a ter status na seção "Pendências de decisão em aberto", com o que cada decisão precisa resolver. Todas ficaram **adiadas**, não cortadas: cortar é decisão de escopo do usuário, não do agente.
  - **Obrigatórias de campo com código nomeado.** A linha genérica "disciplinas de campo" da tabela de 2026-08-28 virou GMG0401 e GAA0304 por extenso, status **cortado**, com o substituto declarado (M20 daqui, M41 do avançado).
  - **Pré-requisito cruzado M30 → M23 do avançado registrado dos dois lados.** Este `_contexto.md` e o `_curso.md` daqui já declaravam que o M30 é o pré-requisito de fato do módulo 23 do curso avançado; o curso avançado não dizia nada. A dependência passou a ser declarada também lá, no campo `cross_course_prerequisites` do módulo 23 e no hub do módulo, porque o grafo formal de pré-requisitos de cada curso só aceita ids do próprio curso.
  - **Escopo respeitado:** nenhuma aula, questionário ou flashcard de conteúdo foi gerado, e nada foi publicado no Notion.

## Regra de auditoria após a repartida
Uma aula reescrita **não herda** a aprovação de auditoria da aula que substituiu. Os módulos 01, 02 e 03 precisam de nova auditoria depois da reescrita, e nenhum questionário ou baralho novo deve ser gerado para eles antes disso. Os relatórios antigos permanecem no disco como registro histórico e como fonte dos achados 🔵.

## Pendências a retomar (achados 🔵 da auditoria do M01)
Controvérsias de literatura, não defeitos — revisitar quando os módulos abaixo forem auditados, para manter consistência:
> Os números abaixo já estão na numeração de 2026-08-25.

- **M01-F02** (rocha mais antiga — Acasta vs. Nuvvuagittuq): retomar no **M03** (geocronologia) e no **M25** (crátons).
- **M01-F03** (origem da Lua por impacto gigante): retomar no **M24**.
- **M01-F04** (espessura de crosta e limite manto-núcleo como faixas de referência): sob a regra LC-05 o curso passa a usar ordem de grandeza no nível iniciante, o que **neutraliza o achado nos módulos 01 e 02**. A precisão plena segue deferida ao **M19**.

## Pendências a retomar (achados 🔵 da auditoria do M02)
Quatro controvérsias concentradas no motor da tectônica e no manto profundo:
- **M02-F04** (geometria da convecção do manto — manto inteiro × estratificada em 660 km): retomar no **M18** e no **M19**.
- **M02-F05** (origem das plumas mantélicas e fixidez dos pontos quentes; dobra Havaí–Imperador): retomar no **M10**, **M18** e **M24**.
- **M02-F06** (balanço quantitativo entre slab pull, ridge push, basal drag e sucção; razão de Urey mal restringida): retomar no **M18** e **M19**.
- **M02-F07** (natureza das LLSVPs; elementos leves do núcleo externo): retomar no **M09** e no **M19**.

## Pendência a retomar (achado 🔵 do M03)
- **M03-F02**: retomar conforme registrado no relatório de auditoria do módulo 03.

Regra que vale para todos: **nenhum questionário ou flashcard pode cobrar esses pontos como fato fechado.** Pode-se perguntar sobre eles apenas em formato que peça ao aluno reconhecer a questão como aberta ou distinguir observação de interpretação. Sob LC-08, no nível iniciante eles aparecem em uma frase.

## Área temática de gemologia — movida para outro curso

Esta seção registrava a decisão de 2026-08-24 de abrir a gemologia em três módulos (06, 30 e 31),
as regras herdadas por eles, os IDs aposentados do módulo 06 e a pendência de qualidade das aulas
01–06 daquele módulo.

Em **2026-08-25** a gemologia saiu deste curso. Todo esse registro — incluindo os IDs aposentados,
que continuam válidos e não recicláveis — vive agora em **`../curso-gemologia/_contexto.md`**.
A pendência das aulas 01–06 foi resolvida na mesma data, com o aprofundamento delas.

O que sobra aqui, e que este curso precisa lembrar: os módulos **04** (Cristalografia e química dos
minerais) e **05** (Mineralogia: propriedades, identificação e óptica) são o **pré-requisito
externo** do curso de Gemologia. Mudanças de conteúdo neles têm efeito lá fora, e o hub do módulo
05 registra isso.
