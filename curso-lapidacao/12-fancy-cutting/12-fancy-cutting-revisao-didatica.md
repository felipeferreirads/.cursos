# Revisão didática — Módulo 12: Fancy cutting

**Revisado em:** 2026-09-07 · **Modo:** `review-and-fix` · **Agente:** geo-arquiteto/Opus
**Material:** as 5 aulas de `12-fancy-cutting/`, já auditadas e densificadas na mesma data
**Veredito:** **Bem ensinado com ressalvas** — 5 achados, todos corrigidos, nenhum bloqueante.

> [!info] Contexto desta revisão
> Ela roda **imediatamente depois** da auditoria científica, que além de corrigir 10 achados factuais **reescreveu e expandiu boa parte do corpo das cinco aulas** (reforço de densidade: de 906–2205 para 1635–1684 palavras). Uma densificação dessa magnitude é exatamente o tipo de intervenção que desalinha metadados e cria redundância — e foi aí que os achados desta revisão se concentraram. **Nenhum deles existia antes da densificação**; todos foram introduzidos ou expostos por ela.

## Resumo

🔴 **0** bloqueiam · 🟠 **3** prejudicam · 🟡 **2** atrito · 🔵 **0** sugestões

**Carga por aula (após a revisão):**

| Aula | Conceitos novos | Pré-req reativados | Exemplos | Corpo | Duração |
|---|---|---|---|---|---|
| a01 | 3 (fantasia, corte negativo, espectro de normais) | 3 (m09, m10, m11 + gemologia por nome) | 1 trabalhado + Context Cut | 1635 | ~29 min |
| a02 | 4 (espectro de normais, aberração esférica, mandril/raio, tolerância do côncavo) | 3 (m08 a01/a04, m12 a01) | 1 trabalhado (2 raios) | 1684 | ~29 min |
| a03 | 4 (sulco cilíndrico, disco óptico, Luminaires, critério óptico×decorativo) | 3 (m11, m12 a01/a02) | 1 trabalhado (2 pedras) | 1656 | ~29 min |
| a04 | 4 (precisão, meetpoint×meetline, n-fold, talhe espelho) | 4 (m08 a06, m09 a01/a04/a05, m10) | 1 trabalhado (2 designs) | 1653 | ~29 min |
| a05 | 3 (freeform, talhe de autor, eixos independentes) | 4 (m05, m08 a01/a04, m12 a04) | 1 trabalhado (2 opções) | 1673 | ~29 min |

Nenhuma aula ultrapassa 4 conceitos independentes — dentro do limite. **Nenhuma precisa ser dividida.**

---

## Achados

### 🟠 1. Vocabulário desatualizado em relação ao corpo densificado

**Tipo:** termo técnico central ausente do bloco de entrada (LC-03)
**Onde:** aulas 02, 03 e 04 · "Vocabulário desta aula"

**Problema:** a densificação promoveu vários termos a **peça central do mecanismo** — aparecendo no corpo, em "Erros comuns" e no "Recap relâmpago" — sem que fossem acrescentados à tabela de vocabulário, que é justamente o bloco pelo qual o aluno entra na aula. Quem lê a tabela primeiro (o comportamento que a estrutura LC-03 induz) chega ao mecanismo sem os termos que ele usa.

- **a02:** faltavam **espectro de normais** e **aberração esférica** — os dois pilares do mecanismo corrigido.
- **a03:** faltava **espelho cilíndrico**, que é o que explica por que o sulcado produz *linhas* onde o brilhante produz *pontos*.
- **a04:** faltava **meetline**, usado no corpo, em "Erros comuns" e no Recap.

**Agravante em a02:** a entrada existente de **espelho côncavo** dizia "espalha ou concentra a luz conforme a geometria" — vaga e, pior, *hedge* exatamente no ponto que a auditoria acabara de corrigir. O aluno recebia a versão indecisa no vocabulário e a versão precisa no corpo.

**Correção aplicada:** as quatro entradas acrescentadas, e a de `espelho côncavo` reescrita para dizer o que de fato acontece (converge para um foco a ~*R*/2, e só depois abre).
**Escopo:** correção local. ✅ Corrigido

---

### 🟠 2. A analogia da colher não dizia onde quebra — num ponto em que ela agora carrega peso

**Tipo:** analogia que pode ensinar modelo mental errado
**Onde:** aula 02 · "Uma analogia para começar"

**Problema:** depois da correção factual, a analogia da colher deixou de ser ornamento e passou a **sustentar o argumento**: é ela que o aluno usa para aceitar que côncavo *converge* antes de abrir. Uma analogia que carrega essa carga precisa declarar seus limites, e esta não declarava nenhum. Dois riscos concretos: (a) a concha é uma calota **esférica**, enquanto a faceta da gema é parede de **cilindro**, curva numa direção só — e essa diferença é justamente o que a aula 03 vai explorar; (b) a colher induz a pensar que o **foco** é o que importa na gema, quando o que importa é o espectro de normais.

**Correção aplicada:** callout `[!info]` "Onde a analogia da colher quebra", com as duas ressalvas e a instrução de uso — "use a colher para lembrar que côncavo converge, não para imaginar o que a pedra faz com a luz".
**Escopo:** correção local. ✅ Corrigido

---

### 🟠 3. Duração declarada calibrada para a versão curta das aulas

**Tipo:** desalinhamento entre metadado e carga real
**Onde:** as 5 aulas · cabeçalho "Duração estimada"

**Problema:** as durações (25–28 min, desiguais entre si) foram estimadas quando os corpos tinham **906–1126 palavras**. Após a densificação para 1635–1684, elas subestimavam a carga e — pior para o planejamento de estudo — continuavam **desiguais**, sugerindo que a aula 03 (~25 min) fosse sensivelmente mais leve que a 01 (~28 min), quando as duas passaram a ter praticamente o mesmo tamanho.

**Correção aplicada:** as cinco uniformizadas em **~29 min**, coerente com corpos de ~1650 palavras e ainda dentro do teto de 30 min do curso.
**Escopo:** correção local. ✅ Corrigido

---

### 🟡 4. Redundância introduzida pela própria revisão em a02

**Tipo:** redundância
**Onde:** aula 02 · "Uma analogia" e "O que a curva faz com um feixe"

**Problema:** o callout do achado 2 e o callout `[!warning]` herdado da auditoria passaram a dizer a mesma coisa sobre converge×diverge, em dois lugares próximos — e a soma empurrou a aula para **1754 palavras**, 154 acima do teto e fora da faixa das outras quatro. Redundância deliberada é legítima em ponto difícil, mas aqui as duas formulações competiam em vez de se reforçarem.

**Correção aplicada:** os dois callouts foram diferenciados por função — o `[!info]` trata **dos limites da analogia**, o `[!warning]` trata **do erro a evitar** — e ambos foram enxugados, junto com três parágrafos vizinhos. Aula 02 fechou em **1684**.
**Escopo:** correção local. ✅ Corrigido

---

### 🟡 5. Erro de grafia em pré-requisito

**Tipo:** atrito de leitura
**Onde:** aula 02 · "Antes de começar" — "defeito **preveniível**"

**Correção aplicada:** → "prevenível". ✅ Corrigido

---

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo | Recap cobre | Avaliado em |
|---|---|---|---|---|
| `lapidacao-m12-oa01` — situar a fantasia e explicar o corte negativo | a01, seções 2–7 | sim (citrino, 2 cenários) | sim | questionário pendente |
| `lapidacao-m12-oa02` — faceta côncava × plana e o princípio da máquina | a02, todas as seções | sim (ametista, 2 raios) | sim | questionário pendente |
| `lapidacao-m12-oa03` — efeito óptico do sulcamento × decorativo | a03, seções 2–6 | sim (2 citrinos + imersão) | sim | questionário pendente |
| `lapidacao-m12-oa04` — precisão e ópticos por simetria e padrão | a04, seções 2–6 | sim (2 designs, mesmo erro) | sim | questionário pendente |
| `lapidacao-m12-oa05` — lógica do freeform e regras que permanecem | a05, seções 2–7 | sim (turmalina, 2 opções) | sim | questionário pendente |

**Cobertura: 5/5.** Cada objetivo é ensinado por seções dedicadas, exercitado num exemplo trabalhado com **estrutura comparativa** (dois cenários contrastados) e destilado no recap. Nenhum objetivo órfão, nenhuma seção órfã.

**Verificação de progressão:** nenhum salto de pré-requisito. A cadeia interna do módulo é limpa — a01 estabelece o corte negativo e o espectro de normais; a02 aprofunda a óptica e a máquina; a03 aplica ao sulco (e reativa a02 explicitamente); a04 vira para o eixo oposto (simetria estrita) reativando o m09; a05 fecha contrastando com a04 e com a01. O pré-requisito externo de gemologia é citado **por nome** em a01, a02, a03 e a05, nunca por wikilink.

---

## O que está bem feito (preservar)

- **A estrutura comparativa dos cinco exemplos trabalhados.** Todos usam a mesma forma — dois cenários que diferem numa variável, com o desfecho contrastado — e ela funciona bem para este assunto, em que quase tudo é um *trade-off*. O exemplo de a04 é o melhor do módulo: injeta **o mesmo erro** em dois designs e mostra que um o revela e o outro o esconde. Vale como modelo para os módulos 13 e 14.
- **A honestidade epistêmica.** O módulo declara incerteza em três níveis diferentes e distingue-os bem: controvérsia real da literatura (brilho do côncavo, LC-08), atribuição disputada (Context Cut), e procedência da própria ferramenta didática (teste da imersão). Material autodidata que ensina *o que não se sabe* é raro e deve ser preservado.
- **A disciplina de "o que não concluir".** Em especial a insistência de a05 de que "freeform não é sem regra" e a de a01 de que a fantasia não suspende o ângulo crítico — duas armadilhas naturais do tema, ambas antecipadas.
- **As pontes curriculares criadas na densificação.** "O que substitui a tabela de ângulos" (a02 ↔ m08), "Por que quase sempre no verso" (a03 ↔ a01) e a repartição 4+6 meses do Dom Pedro (a01 ↔ m05) transformam dados soltos em ligações com o resto do curso.
- **A tabela freeform × fantasia como eixos independentes** (a05). É a correção de uma confusão que o próprio módulo poderia ter induzido ao tratar os dois assuntos lado a lado.

## Encaminhamentos (não são defeitos)

- Nenhuma aula precisa ser dividida; nenhuma exige aula nova no módulo.
- **Ilustração:** o mecanismo de a02 (feixe paralelo → convergência a *R*/2 → abertura, com o espectro de normais) e o sistema de duas peças do disco óptico em a03 (espelho atrás + lente na frente) são os dois pontos do módulo em que um diagrama pouparia mais texto. Registrado como sugestão ao orquestrador — **não instalado**, porque `_contexto.md` nomeia apenas três pontos de ilustração obrigatória no curso e nenhum é neste módulo.
- **Alinhamento com a avaliação:** não verificável nesta rodada — o questionário ainda não existe. As sete travas registradas no relatório de auditoria e no `course-state` devem ser respeitadas quando ele for gerado.
