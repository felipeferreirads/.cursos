# Revisão didática: Módulo 04 — Pérolas e gemas orgânicas

**Revisado em:** 2026-08-25 (rodada 1, 5 aulas) · 2026-08-28 (rodada 2, seção "Casco de tartaruga") · **Modo:** review-and-fix · **Desfechos atualizados em:** 2026-08-28
**Material:** `curso-gemologia/04-perolas/` — 5 aulas, hub do módulo, o questionário do módulo e o baralho de flashcards
**Escopo desta partição:** a revisão original de 2026-08-25 cobriu o módulo único `03-gemas-coradas-perolas`, de 21 aulas. Em 2026-08-26 aquele módulo foi dividido; este relatório ficou com os achados das ex-aulas 17–21 (aqui 01–05), e os das aulas minerais estão em [[03-gemas-coradas-revisao-didatica|revisão didática do módulo 03]]. Nada foi rerrevisado na divisão — as observações de carga e de sequência são as de 2026-08-25, com a numeração atualizada.
**Veredito:** **Bem ensinado com ressalvas**

> [!info] Ordem de execução
> Esta revisão rodou **depois** da [[04-perolas-auditoria|auditoria científica]] (aprovada, 0 achados vermelhos ou laranjas em aberto) e depois do questionário e do baralho, de modo que o alinhamento aula ↔ avaliação ↔ flashcards pôde ser verificado com o material final. Nenhum achado desta revisão é de correção factual: os que envolviam fato foram encaminhados ao auditor na rodada anterior.

## Resumo

🔴 **0 bloqueiam** · 🟠 **1 prejudica** (**resolvido** em 2026-08-28) · 🟡 **1 atrito** (**resolvido** em 2026-08-28) · 🔵 **1 sugestão**

**Carga estimada (módulo), medida em 2026-08-25 e reconferida em 2026-08-28:**
- 5 aulas · 5 objetivos de aprendizagem · **1 objetivo por aula**, sem objetivo órfão e sem aula sem objetivo.
- Em 2026-08-25 o corpo ia de **1.667 a 1.929 palavras** por aula, com três das cinco acima de 1.800: a01 (1.810), a04 (1.924) e a05 (1.929).
- **Em 2026-08-28, após nova rodada de compressão:** todas as cinco aulas caíram ao patamar do contrato. Contadas com o mesmo contador de tokens de corpo (tabelas incluídas): a01 **1.518**, a02 **1.561**, a03 **1.538**, a04 **1.620**, a05 **1.548**. A a04 fica ~20 tokens acima de ~1.600 porque concentra seis tabelas de identificação, todas necessárias; sua prosa fora de tabela é ~1.230. Achado 1 encerrado.
- Densidade tabular alta e deliberada: as aulas 04 e 05 concentram o volume, com 35 e 28 linhas de tabela.
- Todos os 5 objetivos usam verbo verificável (explicar, distinguir, avaliar, identificar). **Nenhum** usa "entender", "conhecer" ou "saber".

> [!note] Efeito favorável da divisão de 2026-08-26
> O achado 🟠 1 abaixo tinha um agravante de **posição**: as duas aulas mais longas do curso chegavam depois de dezenove aulas de material mineral, no ponto de maior fadiga acumulada. Com a separação em módulo próprio, elas passam a ser a quarta e a quinta aula de um módulo curto, precedidas de uma fronteira natural de descanso. A carga por aula não mudou; a **posição** melhorou, e a parte do achado que dependia dela está resolvida.

## Achados

### 🟠 1. As duas aulas de gemas orgânicas estouram o teto de palavras

**Tipo:** dificuldade desproporcional à posição · duração acima do contrato de nível
**Onde:** aula 04 (1.924 palavras de corpo, 35 linhas de tabela) e aula 05 (1.929 palavras, 28 linhas de tabela); as duas declaram `palavras_corpo: ~1600` no bloco de metadados
**Problema:** as duas últimas aulas são as mais longas do módulo, cerca de **20% acima** da mediana do curso. A aula 04 empilha âmbar, copal, o teste da água salgada, cinco tratamentos, os indícios de inclusão forjada e o azeviche com suas três imitações; a aula 05 empilha coral calcário, coral negro, coral bambu, o regime CITES do coral, marfim, ângulos de Schreger, seis substitutos, o regime CITES do marfim e a madrepérola. As gemas orgânicas foram divididas em duas aulas justamente para não estourar o teto — a divisão aconteceu, mas o teto continuou estourado nas duas metades. Como consequência secundária, o campo `palavras_corpo` está desatualizado em ambas (e também em a01).
**Correção sugerida:** para a aula 05, o corte mais limpo é mover **madrepérola** para o fim da aula 02 (pérolas, Parte 2), onde os moluscos *Pinctada* já estão na mesa e a madrepérola já aparece como fonte dos núcleos — a aula 05 ficaria com coral e marfim, que é o par unido pela questão legal. Para a aula 04, a compressão possível é enxugar a tabela de imitações do azeviche, cujo conteúdo essencial já está no recap.
**Escopo:** **exige redistribuir conteúdo entre aulas.** Decisão do `gerador-de-curso-modular`, com impacto em objetivos, no questionário do módulo e nos flashcards.

**Desfecho — ✅ RESOLVIDO (2026-08-28).** O achado tinha três partes, e as três fecharam:

| Parte do achado | Situação |
|---|---|
| **Posição no curso** — as duas aulas mais longas chegavam depois de dezenove aulas minerais | ✅ resolvida em **2026-08-26** pela divisão do módulo |
| **Volume da aula 05** — 1.929 palavras | ✅ resolvida em **2026-08-27**: a seção **Madrepérola** foi movida para o fim da [[04-perolas-aula-02-perolas-parte-2-tipos-e-nucleacao|aula 02]], **exatamente a correção sugerida acima**. A aula 05 passou a se chamar "Gemas orgânicas II: coral e marfim" |
| **Volume da aula 04** — 1.924 palavras | ✅ resolvida em duas rodadas: compressão em 2026-08-27 e nova poda em 2026-08-28 (recap, exemplo trabalhado, seção "o que não concluir"). A prosa fora de tabela caiu para ~1.230; o corpo total fica em ~1.620 por causa das seis tabelas de identificação, que não são comprimíveis sem perder critério diagnóstico |

**Sobre o destino da madrepérola.** A seção não foi cortada nem resumida: **mudou de aula inteira**, com as duas alegações auditáveis (`MPE-EST-001` e `MPE-USO-001`) reapontadas para o novo arquivo, o objetivo `gemologia-m04-oa02` ampliado para "…e caracterizar a madrepérola", `gemologia-m04-oa05` reduzido a "coral e marfim", e os cards `fb064` e `fb065` reatribuídos à aula 02 **sem reindexação**, para preservar o histórico do Anki. A aula 02, que absorveu a seção, foi comprimida em 2026-08-28 de 1.817 para **1.588** palavras por corte de redundância — **nenhum fato foi removido**, e as 12 alegações auditáveis do rodapé continuam todas sustentadas pelo texto.

**Nada pendente.** A tabela de imitações do azeviche foi mantida (é o critério diagnóstico azeviche × vidro preto × vulcanite, não redundante com o recap); a poda veio da prosa em volta.

---

### 🟡 2. O campo `palavras_corpo` está desatualizado em três aulas

**Tipo:** metadado que não corresponde ao material
**Onde:** blocos de metadados das aulas 01, 04 e 05
**Problema:** as três declaram `~1600`, e medem entre 1.810 e 1.929. O campo existe para que a próxima revisão de carga confie nele em vez de recontar; desatualizado, ele esconde exatamente o achado 1.
**Correção sugerida:** recontar e atualizar o campo nas três aulas.
**Escopo:** correção local. **Não aplicada** — o método de contagem original não é o mesmo que esta revisão usou (a minha inclui marcação de tabela e negrito), e substituir uma estimativa por outra sem alinhar o método pioraria o registro em vez de melhorá-lo. Fica registrado para quem gerar as aulas.
**Situação em 2026-08-28: ✅ resolvido.** A ressalva de método caiu — os dois contadores concordam dentro de 0,5 %. Os cinco campos `palavras_corpo` passaram a declarar valor medido: a01 1.590, a02 1.588, a03 1.538, a04 1.620 (com comentário sobre a fração tabular) e a05 1.569. Nenhuma aula ainda declara `~1600`.

---

### 🔵 3. O módulo herda um pré-requisito de categoria que nunca declara em bloco

**Onde:** hub do módulo · aulas 01, 02 e 04
**Observação:** três noções vêm inteiras do módulo 03 e são usadas aqui sem serem reensinadas — a regra de divulgação (aula 14 de lá), a reserva de "sintético" a gema mineral (aula 15) e a categoria de peça montada (aula 16), sem a qual a mabe é descrita errado. As aulas citam cada uma no seu "Antes de começar", o que é correto, mas o aluno que abre o módulo pelo hub não vê a dependência reunida.
**Desfecho (2026-08-26):** aplicado na divisão. O hub do módulo 04 passou a declarar as três noções como pré-requisito explícito, com link para a aula de origem de cada uma.

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo trabalhado | Avaliado em | Flashcards |
|---|---|---|---|---|
| `gemologia-m04-oa01` — biologia da pérola e do nácar | a01 · Conteúdo | sim | Q1–Q3 · Q13–Q15 | 16 |
| `gemologia-m04-oa02` — tipos comerciais, nucleação, madrepérola | a02 · Conteúdo | sim | Q4–Q6 · Q14 | 17 |
| `gemologia-m04-oa03` — sete fatores, ensaios e tratamentos | a03 · Conteúdo | sim | Q7–Q9 · Q13, Q16 | 15 |
| `gemologia-m04-oa04` — âmbar, copal, azeviche | a04 · Conteúdo | sim | Q10, Q11 · Q13, Q16 | 18 |
| `gemologia-m04-oa05` — coral e marfim | a05 · Conteúdo | sim | Q12 · Q13, Q16 | 15 |

**Nenhum objetivo não coberto. Nenhum conteúdo órfão de objetivo. Nenhum objetivo sem exemplo trabalhado. Nenhum objetivo sem questão e sem card.**

**Alinhamento aula ↔ avaliação:** verificado no questionário do módulo. O Bloco A distribui as questões por objetivo com os quatro níveis cognitivos declarados em matriz; o Bloco B faz o papel de cumulativo, exigindo duas ou mais aulas por questão. A opção por **um só questionário, sem parciais**, está correta para um módulo de cinco aulas: o limiar do plugin para partir a avaliação é de seis.

**Alinhamento aula ↔ flashcards:** verificado. O baralho ancora cada card numa alegação auditável das aulas, distribui 15 a 18 cards por objetivo sem concentração indevida, e — o ponto que mais frequentemente falha — **formula as três controvérsias declaradas como debates abertos**, e não como fato fechado (idade do âmbar báltico, fronteira copal–âmbar, divulgação do *maeshori*). Nenhum card decora o periférico ignorando o central.

---

## Rodada 2 — 2026-08-28 (seção "Casco de tartaruga", aula 05)

A seção de casco de tartaruga foi acrescentada à aula 05 em 2026-08-28 (~250 palavras), depois da auditoria científica da própria seção (aprovada, 0 achado).

**Veredito: Bem ensinado.** 🔴 0 · 🟠 0 · 🟡 0 · 🔵 1.

A seção se integra bem ao resto da aula: entra depois de coral e marfim, com a mesma estrutura (o que é → tabela de propriedades → como se denuncia → imitações → regime legal) e fecha reforçando o fio condutor da aula — **identificar não é legalizar** —, agora aplicado a um terceiro material. O termo `bekko` aparece glosado por aposição; `casco prensado` é introduzido e explicado; a distinção grânulo de pigmento × faixa/redemoinho é o critério operacional certo e a ressalva de que a densidade não separa está redigida contra a simplificação de varejo. O vocabulário, o recap, os "Erros comuns" e o "O que não concluir" da aula 05 já foram atualizados com entradas de casco de tartaruga na redação.

### 🔵 R2-1. A linha de índice de refração na tabela do casco de tartaruga não é usada

**Observação:** a tabela dá `IR ~1,55`, mas nenhuma parte do texto usa o índice de refração para identificar ou separar casco de tartaruga — coerente com o resto do módulo, onde o refratômetro quase não serve, mas um leitor que vem das aulas minerais pode esperar que o número tenha função. Não é defeito: a tabela padroniza o formato das fichas do módulo. Manter.

### Cobertura de objetivos (rodada 2)

| Objetivo | Ensinado em | Exemplo trabalhado | Avaliado em |
|---|---|---|---|
| `gemologia-m04-oa05` — identificar coral, marfim **e casco de tartaruga** | a05 · Conteúdo (3 seções) | sim — o exemplo é de marfim; casco de tartaruga não tem exemplo trabalhado próprio | Q12 do questionário final cobre **só coral e marfim** — a parte de casco de tartaruga está **pendente** para o `gerador-de-questionarios` |

O objetivo `oa05` foi ampliado na redação de 2026-08-28 para incluir casco de tartaruga. A cobertura por questão ficou parcial: registrado em `course-state.yaml > assessment.partial_coverage_note`.

## O que está bem feito

Vale registrar, porque estas escolhas precisam sobreviver às próximas revisões:

- **A pérola em três partes, e não em uma.** Biologia, tipos e avaliação são três aulas porque são três competências diferentes, e a sequência é a certa: sem entender o saco perlífero, a diferença entre nucleação com conta e por tecido não faz sentido; sem os tipos, os sete fatores não têm em que se apoiar.
- **A honestidade sobre o limite duro do módulo.** "A bancada não separa pérola natural de cultivada" aparece na aula 01, volta no exemplo trabalhado e volta no recap. É a lição mais importante do módulo, e o material não a suaviza.
- **A separação entre radiografia e espectroscopia.** Duas perguntas, dois exames, e a insistência de que confundi-los é o erro técnico mais comum do assunto. O card `fc010` e a Q8 do questionário reforçam o mesmo ponto por caminhos diferentes.
- **A simetria "sintético : mineral :: cultivada : pérola".** É um dispositivo de memória raro: ensina duas regras de nomenclatura pelo preço de uma, e ainda deriva delas a definição de imitação de pérola. Reaproveitar em outros cursos.
- **A nota ética do âmbar birmanês e o tratamento do marfim.** As duas mostram que identificação e juízo de legalidade são atos distintos, e a a05 ensina o procedimento — documentar, não julgar, não participar. É conteúdo profissional que a maioria do material de gemologia omite.
- **Os ensaios destrutivos sempre com a ressalva.** Solvente, ponto quente e ácido nunca aparecem sem "área discreta e autorização". Em material orgânico, isso não é preciosismo: é a diferença entre um exame e um dano.

## Navegação

- Hub: [[04-perolas-modulo|Módulo 04 — Pérolas e gemas orgânicas]]
- Auditoria científica: [[04-perolas-auditoria|relatório e desfechos]]
- Revisão do módulo irmão: [[03-gemas-coradas-revisao-didatica|Módulo 03 — Gemas coradas]]
- Baralho: [[04-perolas-flashcards|índice do baralho]]
- Índice: [[_curso|Voltar ao curso]]
