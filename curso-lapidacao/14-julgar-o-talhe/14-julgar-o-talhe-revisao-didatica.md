# Revisão didática: Módulo 14 — Julgar um talhe pronto

**Revisado em:** 2026-09-07 · **Modo:** `review-and-fix`
**Material:** `14-julgar-o-talhe/` — 4 aulas (`a01`–`a04`) + hub do módulo
**Rodou depois da:** auditoria científica de 2026-09-07 (15 achados, todos fechados) — ordem correta: correção factual antes de didática.
**Veredito:** **Bem ensinado com ressalvas** — as ressalvas foram corrigidas.

## Resumo

🔴 0 bloqueiam · 🟠 2 prejudicam · 🟡 6 atrito · 🔵 2 sugestões — **10 achados**, 8 corrigidos, 2 (🔵) em aberto e não bloqueantes

**Carga estimada por aula** (contagem de conceitos genuinamente novos, isto é, não reativados):

| Aula | Conceitos novos | Pré-req. reativados | Exemplos | palavras_corpo | Duração |
|---|---|---|---|---|---|
| a01 | 4 (os quatro critérios) | 6 módulos | 1 trabalhado, 4 passos | 1581 | ~29 min |
| a02 | 1 (o catálogo como grade) + 7 nomes reagrupados | 5 módulos | 1 trabalhado, 2 peças | 1577 | ~29 min |
| a03 | 2 (assinatura; diagnóstico reverso) | 6 módulos | 1 trabalhado, 3 passos | 1600 | ~30 min |
| a04 | 4 (recorte, repolimento, defeito propagado, irrecortável) | 4 módulos | 1 trabalhado, 3 passos | 1599 | ~30 min |

A carga nominal de `a02` parece alta (sete defeitos), mas **nenhum dos sete é novo** — a aula declara isso na abertura ("não introduz mecanismos novos") e organiza tudo por critério e por família. O que ela realmente ensina é **uma** ideia: o catálogo como grade de inspeção. É a estrutura certa para um módulo de síntese, e por isso não foi tratada como sobrecarga.

---

## Achados

### 🟠 1. A aula 04 não acompanhava a tripartição que a aula 03 passou a ensinar

**Tipo:** desalinhamento entre aulas do mesmo módulo · quebra de progressão
**Onde:** `a04` · "Antes de começar", "O que o recorte não consegue", "Erros comuns", "Recap"

**Problema:** a correção de auditoria `JUL-EXT-DICOT-001` transformou o diagnóstico da `a03` de **binário** (execução × material) em **ternário** (execução, material, **projeto** — estilo de talhe e contorno). A `a04` continuava construída sobre o binário: abria dizendo *"o diagnóstico separa defeito de execução (recortável) de defeito de material (não recortável)"*, e a palavra "estilo" não aparecia uma única vez na aula.

O efeito sobre quem lê é pior que uma imprecisão: a `a03` acabara de ensinar que a extinção de um talhe degrau **persiste** com o ângulo corrigido e **não** é do material — e a `a04`, a aula seguinte, oferecia só duas gavetas para guardar isso. O leitor com essa causa na mão não tinha onde colocá-la, e a saída natural (guardar em "material", porque persiste) é exatamente o erro que a `a03` acabara de corrigir. Achado de progressão, não de fato.

**Correção aplicada:** a `a04` passou a carregar as três origens desde a abertura, com a colocação explícita do projeto no meio da escala de custo — é geometria, logo alcançável por recorte, mas só refazendo a pedra em outro talhe. Um parágrafo curto fecha a seção dos irrecortáveis com a mesma ideia, o Recap ganhou a linha correspondente, e "Recortar sem diagnosticar primeiro" deixou de citar a dicotomia ("sem saber **a origem** do defeito").
**Escopo:** correção local. Não exigiu conteúdo factual novo — a colocação do projeto decorre das definições já auditadas de recorte (remover material para mudar geometria) e das causas de extinção do módulo 05.

---

### 🟠 2. "Causa de projeto" entrava na aula 03 como categoria sem definição

**Tipo:** termo técnico usado antes de definido (LC-01)
**Onde:** `a03` · "Vocabulário desta aula"; "Mapeando o catálogo às etapas"

**Problema:** o mesmo efeito colateral da correção anterior, um degrau acima. Depois da auditoria, "projeto" passou a ser uma das **três categorias diagnósticas** da aula — aparece no corpo, na tabela, no exemplo, em "Erros comuns" e no Recap — mas não estava na tabela de vocabulário, ao lado de "etapa de origem" e "defeito de material". O contrato LC-01 exige definição na primeira aparição, e uma categoria de classificação é justamente o tipo de termo que não pode ser inferido do contexto: o leitor entende "projeto" como sinônimo de "planejamento" e perde a oposição a "material".

**Correção aplicada:** entrada nova no vocabulário — *"**causa de projeto** — uma causa que não é falha de execução nem propriedade do material, e sim consequência de uma **escolha** feita no desenho da pedra — o estilo de talhe, o contorno."*
**Escopo:** correção local (tabela de vocabulário, fora da contagem LC-02).

---

### 🟡 3. A aula 03 declarava "defeito propagado" no vocabulário e nunca o usava

**Tipo:** vocabulário declarado e não usado
**Onde:** `a03` · "Vocabulário desta aula"

**Problema:** o termo aparecia **uma única vez** no arquivo inteiro — na própria tabela que o define. Quem é ensinado a guardar um termo e nunca o encontra em uso paga o custo de memorização sem o retorno. O conceito é real e importa, mas o lugar dele é a `a04`, que o define de novo (com redação um pouco diferente) e o usa em quatro pontos.

**Correção aplicada:** a entrada foi **substituída** pela de "causa de projeto" (achado 2) — o que resolve os dois de uma vez e mantém a tabela em 5 termos, dentro da faixa de 5 a 10 do LC-03. "Defeito propagado" continua definido e usado na `a04`, onde é de fato o conceito de trabalho.

---

### 🟡 4. A aula 02 usava *meetline* no corpo sem entrada no vocabulário — e a correção de auditoria aumentou o peso dela

**Tipo:** termo central sem entrada de vocabulário
**Onde:** `a02` · "Vocabulário desta aula"

**Problema:** *meetline* já era usada na `a02` (na origem da faceta extra), amparada pela definição da `a01` do mesmo módulo — tecnicamente conforme ao LC-01, já que a primeira aparição no módulo é definida. Mas a correção `JUL-UNDERCUT-CONT-001` deu à palavra um papel novo e bem maior: é ela que responde à pergunta "e o quarto sentido de *undercut*, onde entra?". Um termo que carrega a resolução de uma ambiguidade de quatro vias merece estar na tabela de entrada da aula, não só na da aula anterior. É exatamente a mesma correção que a revisão didática do módulo 12 aplicou à sua aula 04.

**Correção aplicada:** entrada acrescentada à tabela da `a02`, com remissão explícita à `a01` para não duplicar o ensino. A tabela passou a 8 termos (faixa 5–10 do LC-03).

---

### 🟡 5. O verbete de *undercut* da aula 02 ficou mais vago que o corpo

**Tipo:** vocabulário desatualizado em relação ao texto
**Onde:** `a02` · "Vocabulário desta aula"

**Problema:** o verbete dizia *"palavra com **mais de um** sentido neste curso"*, redação vaga que era adequada quando o corpo dizia "três" e ficou pior depois que o corpo passou a enumerar **quatro** com precisão. O aluno lê o vocabulário antes do corpo; recebê-lo vago e depois preciso inverte a ordem útil.

**Correção aplicada:** *"palavra com **quatro** sentidos distintos neste curso — aqui, como item de catálogo, qualquer depressão ou reentrância..."*.

---

### 🟡 6. A aula 01 citava duas aulas do módulo 09 e linkava só uma

**Tipo:** pré-requisito citado sem acesso
**Onde:** `a01` · "Antes de começar, você precisa saber"

**Problema:** o item dizia *"Do módulo 09, **aulas 04 e 05**"* sob um único wikilink apontando para a 04. O conteúdo reativado na segunda metade da frase ("o encontro que não fecha tem sintomas diferentes conforme a coordenada fora") é da **05** — e é justamente o pré-requisito de que a `a03` deste módulo mais depende. Num bloco cuja função é dar ao leitor o caminho de volta, um pré-requisito sem link é um pré-requisito que ele não vai revisar.

**Correção aplicada:** o item foi partido em duas orações, cada uma com seu wikilink próprio.

---

### 🟡 7. Durações declaradas desalinhadas depois da recontagem

**Tipo:** metadado que desorienta o planejamento de estudo
**Onde:** cabeçalho de `a01` e `a04`

**Problema:** as correções de auditoria mudaram as densidades (a04 saiu de 1459 para 1599 palavras), e as durações declaradas ficaram fora de ordem: a `a01`, com 1581 palavras, anunciava ~27 min, menos que a `a02` com 1577 e ~29 min. Quem usa a duração para dimensionar a sessão de estudo — que é o propósito do campo — recebe informação errada.

**Correção aplicada:** `a01` → ~29 min; `a04` → ~30 min. As quatro aulas ficam agora em 29–30 min, coerentes entre si e dentro do teto de 30 do curso.

---

### 🟡 8. O bloco `cobertura` da aula 04 omitia uma seção que cobre o objetivo

**Tipo:** metadado de cobertura incompleto
**Onde:** `a04` · rodapé YAML

**Problema:** as aulas 01, 02 e 03 declaram `[Conteúdo, Exemplo trabalhado, Erros comuns, O que não concluir, Recap relâmpago]`; a `a04` omitia "O que não concluir". A seção existe e é substantiva para o objetivo `oa04` — dois dos seus quatro itens delimitam **o que não se conclui sobre o recorte**, que é metade do enunciado do objetivo. A omissão faz o `gerador-de-questionarios` subestimar a cobertura da aula.

**Correção aplicada:** seção acrescentada ao bloco `cobertura`.

---

### 🔵 9. Sugestão — o quadro comparativo poderia fechar o módulo

**Onde:** `a04` · "Próxima aula" (o parágrafo de encerramento do curso)
**Observação:** a `a01` tem a tabela "os quatro critérios por família", a `a02` tem "o quadro do catálogo" e a `a03` tem "o quadro do diagnóstico" — três tabelas que, juntas, são a espinha do módulo. O parágrafo final do curso as menciona em prosa. Um quarto quadro consolidando defeito → critério → etapa → recortável seria a ficha de referência natural para o aluno voltar depois. **Não aplicado:** custaria palavras que o teto LC-02 não tem, e a decisão de acrescentar uma seção pertence ao `gerador-de-curso-modular`, não a esta skill. Registrado como oportunidade.

### 🔵 10. Sugestão — apoio visual em `a02`

**Onde:** `a02` · catálogo de defeitos
**Observação:** o `_contexto.md` já elege três pontos do curso onde a ilustração é essencial e os pede explicitamente na aula. O catálogo de defeitos é forte candidato a um quarto: sete defeitos descritos só em palavras ("a linha da cinta sobe e desce", "base mais larga que o topo") são exatamente o tipo de conteúdo que uma figura resolve em segundos. **Não aplicado:** acrescentar um pedido de ilustração ao contrato do curso é decisão do orquestrador. Registrado para o usuário decidir.

---

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo | Fechado por | Avaliado em |
|---|---|---|---|---|
| `lapidacao-m14-oa01` — enumerar os critérios e explicar o que cada um mede | `a01`, quatro seções nomeadas + tabela por família | sim (pedra oval, 4 passos) | Erros comuns, O que não concluir, Recap | questionário ainda não gerado |
| `lapidacao-m14-oa02` — identificar e nomear os defeitos pelo aspecto visível | `a02`, cinco seções + quadro do catálogo | sim (esfera de ágata + brilhante de quartzo) | idem | idem |
| `lapidacao-m14-oa03` — inferir a etapa de origem a partir do defeito | `a03`, mapeamento item a item + quadro do diagnóstico + seção de limite | sim (esmeralda, 3 passos) | idem | idem |
| `lapidacao-m14-oa04` — avaliar o recorte por ganho × perda e delimitar o que ele não conserta | `a04`, cinco seções cobrindo as duas metades do enunciado | sim (safira, 3 passos) | idem (bloco `cobertura` corrigido, achado 8) | idem |

**Cobertura completa: 4/4.** Nenhum objetivo órfão, nenhuma seção órfã. Cada aula tem exatamente um objetivo e o cobre inteiro, incluindo a segunda metade dos enunciados compostos (`oa04` cobre tanto "avaliar" quanto "delimitar o que não conserta"). Todos os quatro verbos são de conhecimento observável — enumerar, identificar, inferir, avaliar — conforme a regra dura do curso; nenhum objetivo usa "entender", "conhecer" ou "saber", e nenhum avalia execução de bancada.

**Alinhamento com a avaliação:** não verificável ainda — o questionário do módulo 14 não existe (o gate o bloqueava até a auditoria fechar). Os pontos que a avaliação precisa cobrir estão listados em `traps_for_quiz_generator` no manifesto da auditoria.

---

## Progressão do módulo

A cadeia das quatro aulas é a mais limpa do curso e merece registro: **critério → nome → causa → decisão**. Cada aula responde a uma pergunta que a anterior deixou explicitamente em aberto, e cada uma diz, no bloco "O que não concluir", qual pergunta pertence à seguinte. Foi conferido item a item:

- `a01` adia o catálogo, o diagnóstico e o recorte → entregues em `a02`, `a03`, `a04`.
- `a02` adia a causa e a distinção acidente × manobra → entregues em `a03` e `a04`.
- `a03` adia a decisão de agir → entregue em `a04`.
- `a04` fecha o curso e não adia nada.

Nenhuma aula usa o resultado de uma posterior. Nenhum salto de pré-requisito: os 11 módulos citados aparecem sempre com wikilink e com a reativação em uma frase, nunca reensinados — o que é o comportamento correto para um módulo de síntese e o que mantém as quatro aulas dentro de 30 minutos apesar do repertório enorme que mobilizam.

A `a03` é declarada no hub como o ponto de maior dificuldade do curso, e a estrutura confirma isso: é a única que precisa manter cinco famílias de talhe simultaneamente na cabeça. Ela se sustenta por três decisões acertadas — abre reancorando num caso menor já dominado (o meetpoint do módulo 09), mapeia um defeito por parágrafo em vez de discorrer, e fecha com uma tabela de sete linhas que serve de rede de segurança. Não foi encontrada sobrecarga que justificasse divisão.

---

## O que está bem feito

- **A abertura da `a01`** ("um crítico gastronômico não precisa saber cozinhar") resolve de uma vez o problema mais delicado do módulo: justificar por que se julga sem saber fazer, num curso cuja regra dura proíbe competência de bancada. A analogia é apresentada como analogia, não é forçada além do ponto, e a aula não volta a ela — uso exemplar.
- **Os quatro blocos "O que não concluir"** funcionam como sistema, não como formalidade: os três primeiros fazem o encadeamento do módulo, e o quarto item de cada um marca a fronteira de bancada. É o mecanismo que mantém o nível teórico sem precisar repetir a regra a cada parágrafo.
- **A tabela "os quatro critérios por família"** (`a01`) é o melhor artefato do módulo: mostra num relance que "não se aplica" é uma resposta legítima, e é ela que sustenta o primeiro erro comum da aula ("cobrar encontro de facetas de um cabochão").
- **A insistência em distinguir defeito de manobra** (`a02` e `a03`: "não é 'o que saiu errado', mas 'que troca foi feita'") é a ideia mais madura do módulo e aparece nos três lugares certos — corpo, erros comuns e recap.
- **O Passo 3 do exemplo da `a03`** ensina, pelo exemplo, a resistir à causa única. Um exemplo trabalhado cuja conclusão é "não existe uma causa comum, e forçá-la seria o erro" é raro e vale mais que o próprio diagnóstico.
- **O parágrafo de encerramento da `a04`** percorre os 14 módulos na ordem e nomeia o que cada bloco entregou. É o fecho que um curso de 14 módulos merece.

---

## Correções aplicadas

**Aplicadas em:** 2026-09-07

| # | Sev. | Desfecho | Arquivo |
|---|---|---|---|
| 1 | 🟠 | Corrigido | `...aula-04-recorte...md` |
| 2 | 🟠 | Corrigido | `...aula-03-diagnostico-reverso...md` |
| 3 | 🟡 | Corrigido (resolvido junto com o 2) | `...aula-03-diagnostico-reverso...md` |
| 4 | 🟡 | Corrigido | `...aula-02-o-catalogo-de-defeitos...md` |
| 5 | 🟡 | Corrigido | `...aula-02-o-catalogo-de-defeitos...md` |
| 6 | 🟡 | Corrigido | `...aula-01-os-criterios...md` |
| 7 | 🟡 | Corrigido | `...aula-01-os-criterios...md`, `...aula-04-recorte...md` |
| 8 | 🟡 | Corrigido | `...aula-04-recorte...md` |
| 9 | 🔵 | Não aplicado — encaminhado ao orquestrador (exige nova seção; teto LC-02) | — |
| 10 | 🔵 | Não aplicado — encaminhado ao usuário (decisão de contrato do curso) | — |

**Nenhum questionário ou baralho foi alterado** — não existem para este módulo, e desalinhamento com avaliação é reportado, nunca corrigido por esta skill.

**Nenhum conteúdo factual novo foi introduzido.** A única adição substantiva (a colocação da causa de projeto na escala de custo do recorte, achado 1) deriva de definições já auditadas: recorte é remoção de material para mudar geometria, e estilo de talhe e contorno são geometria. Não passa por afirmação nova sobre o mundo.

**Densidade LC-02 depois desta revisão:**

| Aula | Após auditoria | Após revisão didática | Teto |
|---|---|---|---|
| a01 | 1581 | 1581 (só vocabulário e cabeçalho) | ~1600 ✅ |
| a02 | 1577 | 1577 (só vocabulário) | ~1600 ✅ |
| a03 | 1600 | 1600 (só vocabulário) | ~1600 ✅ |
| a04 | 1599 | **1599** (adição do achado 1 compensada por corte de redundância) | ~1600 ✅ |

**Pendências:** os dois 🔵 (quadro consolidado de fechamento; pedido de ilustração no catálogo de defeitos), ambos fora do escopo desta skill e sem efeito sobre o gate. Nenhum 🔴 ou 🟠 em aberto.
