# Revisão didática — Módulo 10: Famílias de talhe facetado

**Revisado em:** 2026-09-06 · **Modo:** `review-and-fix`
**Material:** `10-familias-de-talhe/` — 5 aulas (`lapidacao-m10-a01` a `a05`)
**Rodou depois da auditoria científica** (`10-familias-de-talhe-auditoria.md`, aprovada, 0 achados 🔴/🟠 em aberto), como o pipeline exige.
**Veredito:** ✅ **Bem ensinado com ressalvas** — todas corrigidas.

## Resumo

🔴 0 bloqueiam · 🟠 3 prejudicam · 🟡 4 atrito · 🔵 1 sugestão — **8 achados, 8 corrigidos.**

**Carga estimada por aula:**

| Aula | Conceitos novos | Pré-req. reativados | Exemplos | Duração declarada | Palavras de corpo |
|---|---|---|---|---|---|
| a01 — brilhante | 4 (arranjo radial, cintilação por multiplicidade, simetria de rotação, inventário de facetas) + a linhagem | 4 | 1 trabalhado, 4 passos | ~26 min | 1602 |
| a02 — degrau | 4 (arranjo paralelo, corredor de espelhos, caminho óptico longo, canto truncado) | 3 | 1 trabalhado, 3 passos | ~25 min | 1527 |
| a03 — misto | 3 (combinação de arranjos, os dois sentidos, Barion) | 3 | 1 trabalhado, 3 casos | ~24 min | 1507 |
| a04 — contornos | 3 (gravata-borboleta, vazamento × obstrução, defeito por contorno) | 3 | 1 trabalhado, 3 passos | ~26 min | 1444 |
| a05 — peso | 5 manobras + espalhamento | 3 | 1 trabalhado, 4 passos | ~25 min | 1598 |

Nenhuma aula estourou o limite de 3–4 ideias independentes de forma que justificasse divisão. A a05 é a mais carregada (cinco manobras), mas usa **estrutura paralela rígida** — cada manobra é "onde o peso entra / o que a óptica cobra" —, e essa repetição de forma é o que a mantém aprendível. Nenhuma divisão de aula é recomendada, e nenhum encaminhamento ao `gerador-de-curso-modular` é necessário.

---

## Achados

### 🟠 1. A aula 01 usa a anatomia da pedra sem declará-la como pré-requisito

**Tipo:** salto de pré-requisito
**Onde:** aula 01 · cabeçalho e "Antes de começar, você precisa saber"

**Problema:** a aula 01 usa **cinta** 24 vezes, **coroa** 24, **culaça** 15 e **pavilhão** 11 — e não define nenhum dos quatro, nem os declara como conhecimento prévio. O cabeçalho lista só as aulas 01 e 03 do módulo 08 e a aula 03 do módulo 09. Pior: a **primeira definição** de "coroa" e "pavilhão" no módulo aparece no vocabulário da **aula 03**, e a de "cinta" só na **aula 05** — ou seja, o módulo define depois o que a primeira aula já exigia. Quem retomar o curso pela aula 01 depois de um intervalo cai direto no vão. É o defeito mais caro do módulo porque está na primeira aula: a partir do salto, nada mais é acompanhável.

**Correção aplicada:** a aula 02 do módulo 01 (*Anatomia da pedra lapidada e nomenclatura das facetas*) foi acrescentada ao cabeçalho de pré-requisitos e reativada em **uma frase** no "Antes de começar", nomeando as cinco regiões com a glosa em linguagem comum. Cumpre LC-03 (link de aula deste curso via wikilink) sem reensinar a anatomia dentro da aula 01, e **sem custo de LC-02** — nenhum dos dois blocos entra na contagem de `palavras_corpo`.
**Escopo:** correção local.
**Desfecho:** ✅ Corrigido

---

### 🟠 2. "Quilha" definida de dois jeitos diferentes dentro do mesmo módulo

**Tipo:** termo definido de duas formas
**Onde:** aula 04 · "Vocabulário desta aula" — versus aulas 02 e 05

**Estava escrito:** aula 04: "**quilha** / **ponta** | a aresta ou o vértice agudo de um contorno — a ponta da pêra, as duas pontas da marquise, o bico e a fenda do coração."
Aula 02: "**quilha** (*keel*) | no talhe degrau, a aresta comprida no fundo do pavilhão".
Aula 05: "**quilha deslocada** | no degrau, a aresta do fundo do pavilhão fora do eixo de simetria".

**Problema:** o mesmo termo nomeia duas coisas distintas em três aulas consecutivas — a aresta do fundo do pavilhão (02 e 05, uso correto e consistente) e o vértice agudo do contorno (04). O leitor que memoriza a definição da aula 02 lê a Manobra 3 da aula 05 corretamente, mas tropeça na aula 04; quem memoriza a da 04 lê a Manobra 3 errado. Como as três aulas são vizinhas e a aula 05 depende explicitamente da 04, a colisão é praticamente garantida.

**Correção aplicada:** a linha da aula 04 passou a definir apenas **ponta** — que é o que a própria linha descreve — com uma ressalva curta apontando o outro sentido e onde ele vale. A definição consistente (02/05) foi preservada intacta.
**Escopo:** correção local. **Sem custo de LC-02** (vocabulário não é contado).
**Desfecho:** ✅ Corrigido

---

### 🟠 3. O exemplo trabalhado da aula 05 faz exatamente o que o "O que não concluir" proíbe

**Tipo:** desalinhamento interno / instrução contraditória
**Onde:** aula 05 · "Exemplo trabalhado" versus "O que não concluir"

**Estava escrito:** o exemplo pede "**localizar as manobras em X**" e conclui que a safira "provavelmente combina cinta grossa e pavilhão profundo". Doze linhas depois: "Não concluir **como diagnosticar, numa pedra pronta, qual manobra foi usada** — é o diagnóstico reverso do módulo 14."

**Problema:** a aula ensina uma coisa e, na seção seguinte, diz que essa coisa não foi ensinada. Não é um detalhe de redação: o bloco "O que não concluir" é justamente o que delimita o que o aluno pode levar para a avaliação, e ele estava anulando o exercício central da aula. O aluno diligente conclui que errou o exemplo; o aluno desatento conclui que os dois blocos são decorativos.

**Correção aplicada:** a fronteira foi redesenhada onde ela de fato está — a aula infere manobras a partir de **peso e diâmetro** (dois números), o módulo 14 lê a pedra inteira por protocolo. O bullet passou a "Não concluir o protocolo de diagnóstico reverso: aqui se infere de peso e diâmetro, lá se lê a pedra inteira — módulo 14."
**Escopo:** correção local.
**Desfecho:** ✅ Corrigido

---

### 🟡 4. Título de seção não corresponde ao conteúdo (aula 01)

**Tipo:** título que não corresponde
**Onde:** aula 01 · "### A linhagem: cada **talhe** resolveu um problema do anterior"

**Problema:** dos oito itens numerados da lista, dois não são talhes — o item 4 é a proposta de proporções de Morse e o item 5 é uma **máquina** (a de arredondar a cinta, de 1874). O título promete uma sucessão de talhes e entrega uma sucessão de marcos, o que faz o leitor procurar um "talhe Morse" e um "talhe bruting" que não existem.

**Correção aplicada:** "cada **talhe**" → "cada **passo**". Uma palavra, custo zero de contagem.
**Desfecho:** ✅ Corrigido

---

### 🟡 5. O recap da aula 02 introduz um exemplo que a aula não deu

**Tipo:** recap que não recapitula
**Onde:** aula 02 · "Recap relâmpago" — "o degrau satura material pálido a médio — por isso serve à água-marinha e ao **morganita**"

**Problema:** *morganita* aparece pela primeira e única vez no recap. Um recap existe para destilar o que foi ensinado; quando ele traz material novo, deixa de ser revisável — o aluno que revisa só o recap encontra um termo que não consegue rastrear no corpo.

**Correção aplicada:** em vez de apagar o exemplo (que é bom), ele foi **ancorado no corpo**: a frase sobre material de cor pálida a média passou a citar "água-marinha, morganita, berilo claro". O recap ficou honesto e o corpo ganhou concretude no ponto exato onde ela ajuda. +7 palavras, dentro do teto.
**Desfecho:** ✅ Corrigido

---

### 🟡 6. "Quilha" declarada no vocabulário da aula 02 e nunca usada no corpo

**Tipo:** vocabulário declarado mas não usado
**Onde:** aula 02 · "Vocabulário desta aula" versus "Conteúdo"

**Problema:** a aula 02 define **quilha** — e o corpo nunca emprega a palavra, nem menciona que o pavilhão de um degrau termina numa aresta em vez de um ponto. O termo fica órfão, e a aula 05 (Manobra 3) chega assumindo que ele já foi visto em uso. É também uma oportunidade perdida: a quilha é um dos contrastes mais nítidos entre degrau e brilhante, e a aula existe justamente para construir esse contraste.

**Correção aplicada:** uma frase no ponto onde o contraste é feito — "E onde o brilhante fecha o pavilhão num ponto — a culaça —, o degrau o fecha numa aresta comprida, a **quilha**." O termo passa a ser usado onde foi definido, e a aula 05 herda a base.
**Desfecho:** ✅ Corrigido

---

### 🟡 7. Objetivo truncado no bloco "Ao final você vai conseguir" (aula 03)

**Tipo:** objetivo declarado de forma incompleta
**Onde:** aula 03 · "Ao final você vai conseguir"

**Problema:** a aula declarava "`lapidacao-m10-oa03` — Caracterizar o talhe misto e distinguir seus dois sentidos correntes.", enquanto o hub do módulo e o `course-state.yaml` trazem a formulação completa, que **nomeia** os dois sentidos. A versão curta esconde do aluno metade do que ele será cobrado, e diverge da fonte canônica do objetivo.

**Correção aplicada:** o enunciado foi restaurado por inteiro. Bloco não contado em `palavras_corpo`.
**Desfecho:** ✅ Corrigido

---

### 🔵 8. "Cabeça-de-prego" merecia entrada de vocabulário

**Tipo:** sugestão — termo recorrente só definido em linha
**Onde:** aula 05

**Problema:** não é defeito — LC-01 está cumprido, o termo é explicado na primeira aparição. Mas ele reaparece quatro vezes (Manobra 2, exemplo passo 2, "Erros comuns", "Recap relâmpago") e será reutilizado no módulo 14. Um termo com essa vida útil é mais fácil de revisar a partir da tabela de vocabulário que caçando a primeira ocorrência no meio do texto.

**Correção aplicada:** entrada acrescentada ao vocabulário, restatando a definição que já estava na aula — **nenhum conteúdo factual novo**. A tabela foi de 7 para 8 linhas, dentro da faixa de 5–10 de LC-03, e sem custo de contagem.
**Desfecho:** ✅ Corrigido

---

### Observação sem achado — redundância deliberada, mantida

A tese "só bruto caro justifica a retenção de peso" aparece três vezes na aula 05 (fecho, "Erros comuns", "Recap relâmpago"). Isso foi **avaliado e mantido** como redundância deliberada: é a conclusão que organiza a aula inteira e o tipo de ponto que material autodidata deve repetir. Apenas a formulação de "Erros comuns" foi enxugada, para que as três não fossem literalmente a mesma frase — repetição que reforça é a que reformula.

---

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo trabalhado | Recap cobre | Pronto para avaliação |
|---|---|---|---|---|
| `lapidacao-m10-oa01` — lógica geométrica do brilhante e a linhagem | a01, seções 1–4 | sim (europeu antigo × moderno, 4 passos) | sim | ✅ |
| `lapidacao-m10-oa02` — o que o degrau faz com cor e inclusão, e quando é a escolha certa | a02, seções 2–5 | sim (água-marinha × almandina) | sim | ✅ |
| `lapidacao-m10-oa03` — o misto e seus dois sentidos | a03, seções 1–4 | sim (três pedras, dois critérios) | sim | ✅ |
| `lapidacao-m10-oa04` — contorno → defeito previsível, incl. gravata-borboleta | a04, seções 1–4 | sim (marquise × oval de um bruto 3:1) | sim | ✅ |
| `lapidacao-m10-oa05` — manobras de retenção de peso e custo óptico | a05, manobras 1–5 | sim (duas safiras de 3,00 ct) | sim | ✅ |

**5 objetivos, 5 aulas, cobertura 1:1. Nenhum objetivo órfão, nenhuma seção órfã.** Nenhum conteúdo substancial deixou de servir a um objetivo declarado.

**Alinhamento com a avaliação:** o módulo ainda não tem questionário e os flashcards estão dispensados (decisão de 2026-09-04, módulos 06+). Nada a verificar nem a reportar como desalinhado.

## Nota para quem gerar o questionário

Três pontos deste módulo são armadilhas boas — e o gabarito precisa ficar do lado certo delas:

1. **Brilhante ≠ redondo.** "Brilhante" é o arranjo; "redondo" é o contorno. Existem brilhantes ovais, pêra, coração e almofada. Distrator natural.
2. **O Barion é o misto invertido** — coroa em **degrau** sobre pavilhão **brilhante**, com facetas em meia-lua. A versão anterior da aula dizia o contrário e foi corrigida pela auditoria (achado 🔴 1); qualquer questão sobre o Barion tem de refletir a versão corrigida.
3. **Duas controvérsias LC-08 declaradas**, que não admitem gabarito fechado: os dois sentidos de "misto" (a03) e a causa da gravata-borboleta — vazamento × obstrução (a04), onde o peso relativo dos mecanismos foi explicitamente marcado como não resolvido. Cobrar "qual é a causa" como pergunta de resposta única contradiria a aula.

Lembrete da regra dura do curso: **nenhuma questão pode avaliar competência de bancada.** Os verbos disponíveis são explicar, distinguir, prever, classificar, relacionar, inferir e avaliar uma decisão.

## O que está bem feito

- **A estrutura "imagem antes do nome"** abre as aulas 01 e 02 (a roda de carroça; a escada em volta da pedra) e cumpre LC-04 com elegância: o leitor visualiza antes de receber o rótulo. É o melhor recurso do módulo e deve sobreviver a qualquer revisão futura.
- **A arquitetura do módulo é exemplar:** a01 e a02 apresentam dois arranjos **opostos**, a03 os combina, a04 mostra o que o contorno faz com a combinação, a05 mostra o que o dinheiro faz com tudo. Cada aula depende da anterior de forma real, não decorativa.
- **Os cinco exemplos trabalhados são contrastivos**, nunca ilustrativos: sempre duas ou três alternativas comparadas com uma decisão ao fim. É o formato que efetivamente ensina critério, em vez de apenas demonstrar um caso.
- **A estrutura paralela das cinco manobras da aula 05** ("onde o peso entra / o que a óptica cobra") é o que impede uma aula de cinco conceitos de virar sobrecarga.
- **As duas declarações LC-08 são honestas**, formuladas como pergunta aberta e sem arbitrar o debate — inclusive depois de a auditoria ter removido uma apelação a autoridade inexistente na aula 04.
- **Nenhuma analogia ensina modelo mental errado.** As duas centrais (raios de roda; degraus de escada) são estruturalmente fiéis ao que descrevem e não geram inferência falsa.
