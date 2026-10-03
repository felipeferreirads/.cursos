# Contexto — Curso de Teoria da Lapidação

Preferências e decisões duradouras sobre **como** este curso é ensinado. Não é estado de progresso — isso vive em `course-state.yaml`. Este arquivo **só cresce**: qualquer skill pode acrescentar uma seção ou uma linha, nenhuma pode reescrevê-lo por inteiro.

Criado em **2026-09-01** pelo `planejador-curricular`, no ato de planejamento do currículo. Nenhuma aula existia quando ele foi escrito.

## O que este curso é

Um curso **independente** sobre a teoria da lapidação — gem cutting / lapidary arts. Cobre sete famílias de técnica (facetado, cabochão, misto, esfera e formas torneadas, escultura e gravação, fancy cutting, e o tumbling como fronteira), mais o equipamento, a leitura do bruto, os tratamentos de oficina e o julgamento do talhe pronto.

**Não é um módulo do `curso-gemologia`.** A decisão foi explícita do usuário. O `curso-gemologia` continua com a aula de anatomia e talhe (módulo 01) e a aula de lapidação do diamante (módulo 02); este curso **aprofunda o que aquelas resumem**, não as substitui nem as apaga.

## Perfil e nível

- **Partida:** conclusão do **módulo 01 do curso de Gemologia** — propriedades diagnósticas gemológicas, óptica (índice de refração, ângulo crítico, reflexão interna total), dureza, tenacidade, clivagem, sensibilidade térmica, pleocroísmo e fenômenos ópticos.
- **Chegada:** avançado / especialista **teórico**.
- Aplicação prática: não declarada. O usuário quer domínio conceitual completo da área, não habilitação de bancada.

## Pré-requisito externo (cross-curso)

O pré-requisito real do módulo 01 **não está neste curso**. Ele vive no curso irmão de Gemologia:

| Pré-requisito | Onde | O que este curso assume e não reensina |
|---|---|---|
| Propriedades diagnósticas gemológicas | `curso-gemologia`, módulo **01** | dureza Mohs, tenacidade, clivagem e partição, densidade, sensibilidade térmica e química |
| Óptica da gema | `curso-gemologia`, módulo **01** | índice de refração, ângulo crítico, reflexão interna total, birrefringência, dispersão |
| Cor e fenômeno óptico | `curso-gemologia`, módulo **01** | pleocroísmo, asterismo, chatoyance, adularescência, jogo de cores, mudança de cor |

> [!warning] Regra dura de referência
> Essa dependência é referenciada **por nome**, nunca por wikilink. Um wikilink apontando para fora do curso quebra no Obsidian e é reportado como link morto pelo `validador-estrutural-do-curso`. Mesma regra já em vigor no `curso-gemologia` para as dependências do `curso-geologia`.

O curso de lapidação **não reensina propriedade de gema**. Ele a **aplica** à decisão de corte. Quando uma aula precisa de uma propriedade, ela a reativa em uma frase e cita o curso de Gemologia por nome — não a explica de novo.

## Regra dura: nenhuma competência de bancada

> [!warning] Vale para toda skill a jusante — gerador-de-aula, gerador-de-questionarios, gerador-de-flashcards, tutor-de-voz
> **Nenhuma aula, questão ou flashcard pode afirmar, sugerir ou avaliar competência de bancada ou destreza manual.**

O exame escrito avalia **princípio, escopo, geometria, causa-efeito e limite** — nunca "saber fazer". Formulações proibidas e suas substitutas:

| Não escrever | Escrever |
|---|---|
| "Você vai conseguir lapidar um cabochão" | "Você vai conseguir descrever a sequência de preformação de um cabochão e explicar o papel de cada etapa" |
| "Ajuste o cheater até o meetpoint fechar" | "Explique qual das três coordenadas está fora quando o meetpoint não fecha" |
| "Polir quartzo com óxido de cério" | "Justifique por que o óxido de cério é o polidor indicado para o quartzo" |
| "Pratique a transferência de dop" | "Compare os sistemas de dop por risco térmico, precisão de alinhamento e reversibilidade" |

O verbo de todo objetivo de aprendizagem deste curso é de **conhecimento observável** — explicar, distinguir, prever, classificar, relacionar, ler, aplicar uma fórmula, inferir, avaliar uma decisão. Nunca "executar", "operar a máquina", "lapidar", "polir".

## Contrato de nível (`ensino-medio-com-gemologia-v1`)

Contrato **novo**, batizado neste curso. Vale para toda aula.

1. **LC-01 — Nenhum termo sem definição** na primeira aparição, em linguagem comum.
2. **LC-02 — Teto de ~1.600 palavras** de corpo por aula. O que não cabe vira Parte 1 / Parte 2, ou é deferido — **nunca é comprimido**.
   - **Régua de `palavras_corpo` (fixada em 2026-09-02, vale do módulo 03 em diante):** conta-se tudo entre o cabeçalho `## Conteúdo` e o fim de `## Recap relâmpago`, inclusive — ou seja, conteúdo desenvolvido + exemplo(s) trabalhado(s) + "Erros comuns" + "O que não concluir" + "Recap relâmpago". **Não** conta: título e metadados do topo, "Vocabulário desta aula", "Antes de começar, você precisa saber", "Ao final você vai conseguir", "Próxima aula", "Fontes consultadas" e o rodapé YAML. Texto dentro de tabela conta como palavra normal. Contagem por separação em espaços em branco (`len(texto.split())`); número, fração e termo hifenizado contam como uma palavra.
   - Os rodapés do **módulo 01** foram escritos antes desta régua e declaram ~200 palavras a menos que ela daria; ficam como estão (a folga do "~" cobre) e serão realinhados só se o módulo 01 for reaberto por outro motivo.
3. **LC-03 — Abertura padronizada:** "Vocabulário desta aula" (5 a 10 termos) e "Antes de começar, você precisa saber", com os links das aulas exigidas (wikilink quando dentro deste curso; **menção por nome** quando o pré-requisito é do `curso-gemologia`).
4. **LC-04 — Analogia antes do termo.**
5. **LC-05 — Ordem de grandeza, não precisão de laboratório.** **Exceção deste curso:** ângulos-alvo tabelados por índice de refração, sequências de grão, temperaturas de processo e números de dentes de índice têm valor único e **são o objeto de estudo** — vão com o valor de referência e a fonte.
6. **LC-06 — Matemática reativada antes do uso.** Decisivo no módulo 09, aula 06: a tangente é reativada antes da fórmula do tangent ratio.
7. **LC-07 — "Erros comuns", "O que não concluir" e "Recap relâmpago" obrigatórios.**
8. **LC-08 — Controvérsia em uma frase**, declarada como pergunta aberta, sem arbitrar o debate.

Convenções estruturais herdadas do `curso-gemologia`:

- Bloco **"Ao final você vai conseguir"** com o **ID COMPLETO** do objetivo (`lapidacao-m08-oa02`), nunca `OA-02`.
- Rodapé em comentário HTML com `nivel`, `palavras_corpo`, `cobertura` e `alegacoes_auditaveis` em YAML.
- Aulas de **≤30 min**; assuntos grandes divididos em Parte 1 / Parte 2, nunca comprimidos.
- Módulos de **3 a 8 aulas**, nunca semanas. Com 14 módulos, o curso usa o campo `area` com algarismo romano.

## Formato de `claim_id` — 4 segmentos, desde a primeira aula

> [!warning] Não repetir o erro do curso-gemologia
> Este curso usa **4 segmentos** desde já: `^[A-Z]{2,4}-[A-Z0-9]+-[A-Z0-9]+-[0-9]{3}$`

Exemplos: `FAC-ANG-CRIT-001`, `CAB-DOM-CURV-001`, `ABR-GRAO-SEQ-001`, `DOP-TRAN-RISK-001`, `TRT-EST-RESIN-001`.

O `curso-gemologia` está preso a 3 segmentos por herança e a padronização lá foi julgada de raio de impacto alto demais. Aqui não há herança: começa certo.

## IDs do curso

```text
lapidacao-m<NN>-oa<NN>    objetivo de aprendizagem
lapidacao-m<NN>-a<NN>     aula
lapidacao-m<NN>-q<NN>     questão
lapidacao-m<NN>-fb<NNN>   flashcard Basic
lapidacao-m<NN>-fc<NNN>   flashcard Cloze
```

IDs **nunca são reciclados**. Um objetivo por aula é a convenção (75 objetivos para 75 aulas); se uma aula for dividida no futuro, o objetivo novo recebe o **próximo ID livre**, não desloca os existentes.

## Pipeline de qualidade

Ordem obrigatória, por módulo (módulos 01–05): **aulas → auditoria científica → correção → questionário(s) → flashcards → revisão didática.**

**[2026-09-04] Flashcards removidos do pipeline.** Decisão do usuário: não gerar baralho de flashcards para este curso a partir do módulo 06. O módulo 05 mantém o baralho já gerado; os módulos 06+ têm `flashcards.status: skipped` no `course-state.yaml`. Pipeline dos **módulos 06 em diante**: **aulas → auditoria científica → correção → revisão didática → questionário(s).**

**Gate:** nenhum questionário (nem baralho, onde ainda houver) é gerado para um módulo com achado 🔴 ou 🟠 em aberto na auditoria.

## Escopo por bloco temático

- **I. Fundamentos do ofício** (módulos 01–02) — escopo, anatomia da pedra lapidada, famílias de talhe, a propriedade da gema como restrição de projeto, os centros de lapidação; e a física do desbaste: dureza diferencial, dano subsuperficial, sequência de grão, mecanismos de polimento, calor.
- **II. A bancada** (03–04) — serras, esmeril e drums de expansão, facetadora (mastro, cabeçote, plataforma, índice, água), tambor rotativo e vibratório; laps (aço, cobre, estanho, lucite, cerâmica, zinco), verdadeiro (truing) e manutenção, contaminação de grão, diamante × carbeto de silício × óxidos, polidores (cério, alumina, estanho, crômio), sistemas de dop e a transferência.
- **III. Do bruto ao projeto** (05) — janela de inspeção e imersão, inclusões, fraturas, clivagem, zonação de cor, pleocroísmo e eixo óptico, rendimento e o compromisso beleza × peso, janelamento e extinção como defeitos preveníveis no projeto.
- **IV. Talhes de superfície curva** (06–07) — cabochão (preforma, cúpula, cinta, base, orientação para fenômeno, variantes) e esfera e formas torneadas.
- **V. Facetamento** (08–10) — ângulo crítico aplicado ao pavilhão, ângulos-alvo por faixa de índice, brilho/dispersão/cintilação, brilho × rendimento, cor e profundidade de pavilhão, modelagem óptica; índice, três coordenadas da faceta, leitura de diagrama, meetpoint, cheater e diagnóstico, tangent ratio; brilhante, degrau, misto, contornos e retenção de peso.
- **VI. Escultura e fancy cutting** (11–12) — relevo, intaglio, camafeu, ferramentas, contas e furação, Idar-Oberstein e a escola chinesa do jade; talhe de fantasia, côncavo, sulcamento, precisão, ópticos e freeform.
- **VII. Fronteiras e julgamento** (13–14) — tratamentos da oficina e a regra de divulgação; critérios de qualidade, catálogo de defeitos, diagnóstico reverso e a decisão de recorte.

## Profundidade combinada no facetamento

**Inclui:** ângulo crítico e ângulos-alvo por faixa de índice de refração; lógica do meetpoint faceting; índice (index gear); braço/mastro e cabeçote; cheater; tangent ratio para reescalar um design; métricas de brilho e o compromisso brilho × rendimento; leitura e execução de diagramas de lapidação.

**Não inclui:** autoria de designs novos; otimização em software. **GemCad e GemRay entram apenas como consciência de ferramenta** — o que existem, o que fazem, o que suas métricas não medem — na aula 06 do módulo 08. Nunca como conteúdo operacional.

## Fora do escopo (e por quê)

### Tratamentos — a fronteira com o `curso-gemologia`

O módulo 13 é **enxuto e de fronteira**, não uma cobertura de tratamentos. Ele cobre **só o que acontece na oficina de lapidação**:

- pedras montadas — dublês e tripletes (opala, granada-topo, esmeralda montada) e sua construção;
- estabilização e impregnação de material poroso antes de cortar — turquesa, crisocola, variscita, opala comum;
- tingimento — ágata e calcedônia, howlita;
- calor de processo — cera de dop, choque térmico na serra e no esmeril, por que não se dopa a quente tanzanita, opala e kunzita, secagem de opala;
- oleamento e enceramento como acabamento — cabochão de esmeralda, nefrita e jadeíta;
- ética e a regra de divulgação do que o lapidário faz.

**NÃO cobre**, e cita apenas **por nome** como referência cruzada ao `curso-gemologia` (módulos 02 e 03):

| Fora deste curso | Onde está |
|---|---|
| Aquecimento clássico de rubi e safira | `curso-gemologia`, módulo 03 |
| Irradiação | `curso-gemologia`, módulos 02 e 03 |
| Difusão reticular (superfície e bulk) | `curso-gemologia`, módulo 03 |
| Preenchimento de fratura com vidro ou resina | `curso-gemologia`, módulos 02 e 03 |
| HPHT | `curso-gemologia`, módulo 02 |

Razão: são tratamentos de **laboratório e de beneficiamento**, não operações da oficina de lapidação. Cobri-los aqui duplicaria material já auditado no curso irmão e criaria duas versões da mesma afirmação, que é exatamente o que o `auditor-cientifico` em modo `cross-course` existe para caçar.

### Demais exclusões

- **Joalheria, engaste e ourivesaria como ofício.** O curso trata do engaste apenas como **restrição de projeto** — a curvatura da cúpula e a espessura da cinta precisam servir a uma cravação —, nunca como técnica de joalheiro.
- **Mineralogia e cristalografia.** Pré-requisito externo. Não são reensinadas.
- **Avaliação de valor de mercado da gema pronta.** Fica no `curso-gemologia`. Este curso vai até o **custo óptico e de massa** de uma decisão de corte, e para aí.
- **Operação comercial de lapidário** — precificação de serviço, gestão, negócio.
- **Competência de bancada** — ver a regra dura acima. Não é "fora de escopo por corte editorial": é a definição do nível de chegada.

## Preferências de ensino

- Destino: **Obsidian**. O `.md` local é canônico; publicar no Notion, se um dia for feito, é passo à parte pelo `publicador-notion`.
- Aula de no máximo 30 minutos; assunto grande vira Parte 1 / Parte 2.
- Progressão sem usar conceito antes de ensiná-lo, verificável por LC-01 e LC-03.
- Números tabelados (ângulos-alvo, sequências de grão, dentes de índice) sempre com fonte declarada e com a faixa, não com um valor solto — ver LC-05.
- Ilustração é essencial em três pontos e a aula deve pedi-la explicitamente: anatomia da pedra (m01 a02), as três coordenadas da faceta e o diagrama de lapidação (m09 a02 e a03), e a convergência da esfera (m07 a01).

## Base do currículo

Framing obrigatório: **"baseado na literatura de facetamento e lapidação de..."** — nunca "equivalente ao curso X" nem "nível GIA".

- **Sinkankas**, *Gem Cutting: A Lapidary's Manual* — a sequência serrar → desbastar → lixar → polir e os capítulos de cabochão, facetado, esfera e conta, tambor, escultura, gravação, mosaico e embutido. É a espinha da ordem geral do curso.
- **Vargas & Vargas**, *Faceting for Amateurs* — orientação do bruto, obtenção da maior pedra possível, cartas de transposição e tabelas de ângulo de coroa e culaça.
- **Wykoff**, *Beginner's Guide to Faceting* e *Techniques of Master Faceting*.
- **United States Faceters Guild** — ângulo crítico e índice de refração, escolha de ângulos para o brilhante redondo, meetpoint faceting, conversão de design pelo tangent ratio (fórmula e limites), dicionário de facetamento.
- **William Holland School of Lapidary Arts** e a taxonomia de disciplinas das guildas norte-americanas — a divisão canônica em cabochão, facetamento, esfera, intarsia, escultura, opala e tumbling.
- **GIA** — a tradição lapidária de Idar-Oberstein, a evolução da escultura chinesa de jade, pleocroísmo em gemas facetadas, e a arte e ciência do fantasy carving.
- **Lapidary Journal** e **Rock & Gem** — cabochão, freeform e facetamento côncavo.
- **Patente de Douglas Hoffman** (facetamento côncavo-convexo) e a bibliografia sobre **Bernd Münsteiner** e o talhe de fantasia.
- **AGTA Gemstone Information Manual** e a regra de divulgação da **FTC** — pedras montadas e material estabilizado.

## Decisões (registro por data)

- **[2026-09-01]** Criar a teoria da lapidação como **curso independente**, não como módulo do `curso-gemologia`.
- **[2026-09-01]** Nível de chegada **avançado/especialista teórico**; regra dura de não-competência-de-bancada.
- **[2026-09-01]** Pré-requisito de gemologia **cross-curso, referido por nome, nunca por wikilink**.
- **[2026-09-01]** Facetamento até projeto óptico e leitura de diagrama; **GemCad/GemRay só como consciência de ferramenta**.
- **[2026-09-01]** Tratamentos como **módulo-fronteira enxuto**; tratamentos de laboratório ficam no `curso-gemologia` e entram só por referência cruzada.
- **[2026-09-01]** Ordem: **física do desbaste e equipamento antes das técnicas de talhe**. A alternativa (cabochão primeiro, equipamento pelo caminho) foi rejeitada porque tornaria o módulo de equipamento redundante e obrigaria a reensinar máquina e abrasivo dentro de cada técnica.
- **[2026-09-01]** Equipamento em **dois módulos por coesão**: 03 é a máquina, 04 é a interface com a pedra. O módulo 02 fica com o **mecanismo**; o 04, com o **inventário e as regras de casamento**. Sem essa separação os dois se sobrepõem.
- **[2026-09-01]** `claim_id` de **4 segmentos** desde a primeira aula.
- **[2026-09-01]** O módulo 14 (julgar um talhe pronto) fecha o curso e depende de **todas** as famílias de talhe. É ele que justifica a ordenação topológica inteira: sem ter visto cabochão, esfera, facetado e fancy, o diagnóstico reverso não tem repertório.
- **[2026-09-02]** **Régua de `palavras_corpo` (LC-02) fixada** — ver seção "Contrato de nível", item LC-02.
- **[2026-09-02]** **Dívida de schema do plugin (spin-off)** — `course-state.schema.json` e `audit.schema.json` do FFS-PluginStudy rejeitam campos que as skills gravam; será tratado em trabalho separado, não bloqueia o build.
- **[2026-09-04]** **Flashcards fora do pipeline a partir do módulo 06.** Decisão do usuário. O módulo 05 mantém o baralho já gerado; módulos 06+ têm `flashcards.status: skipped`. Ver seção "Pipeline de qualidade".
