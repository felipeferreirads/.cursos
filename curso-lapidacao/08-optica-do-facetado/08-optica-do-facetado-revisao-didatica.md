# Revisão didática: Módulo 08 — Óptica do talhe facetado

**Curso:** Teoria da lapidação — do desbaste ao projeto óptico (`lapidacao`)
**Módulo:** 08 — Óptica do talhe facetado (área V. Facetamento)
**Escopo:** as 6 aulas do módulo. Questionário ainda não existe — é a etapa 5. Baralho não se aplica (dispensado a partir do módulo 06).
**Modo:** `review-and-fix`
**Data:** 2026-09-05
**Revisor:** geo-arquiteto (Opus)
**Contrato de nível:** `ensino-medio-com-gemologia-v1`
**Roda depois de:** auditoria científica + correção de 2026-09-04 (`08-optica-do-facetado-auditoria.md`), que fechou com `open_findings` vazio e veredito `approved` após 19 correções.

**Veredito:** Bem ensinado com ressalvas — **um 🔴, resolvido**.

---

## Resumo

| Severidade | Quantidade |
|---|---|
| 🔴 Bloqueante | 1 |
| 🟠 Laranja | 5 |
| 🟡 Amarelo | 6 |
| 🔵 Azul (avaliado, com ou sem ação) | 4 |

**Aulas alteradas:** todas as seis.
**`palavras_corpo` pós-correção → pós-revisão:** a01 1576→**1587** · a02 1543→**1600** · a03 1592→**1589** · a04 1605→**1598** · a05 1599→**1597** · a06 1602→**1600**. As seis **sob** o teto de ~1600 de LC-02 — e duas que entraram acima dele (a04 em 1605, a06 em 1602) saíram conformes sem invocar a folga do til.

**O padrão dominante deste módulo tem um nome: resíduo de refutação.** A auditoria de 2026-09-04 não corrigiu números soltos na aula 02 — ela **inverteu a tese**. A aula ensinava que o ângulo-alvo cai com o índice de refração; passou a ensinar que ele é quase plano, porque um piso que desce trabalha contra um teto que não desce. Uma inversão dessas deixa rastro em toda superfície que a auditoria não tinha motivo factual para tocar: entradas de vocabulário, blocos "Antes de começar", títulos de seção, blocos "Próxima aula" da aula anterior. Cinco dos sete achados 🔴/🟠 são exatamente isso — texto correto na versão antiga, que na versão nova **ensina a proposição refutada**. O auditor não os pega porque, isoladamente, cada um é uma frase de enquadramento sem alegação auditável.

---

## 🔴 1 — a02 · a entrada de vocabulário ensina exatamente a proposição que a aula existe para refutar

**Tipo:** definição que instala o modelo mental errado / contradição interna do vocabulário
**Onde:** `08-optica-do-facetado-aula-02`, tabela "Vocabulário desta aula", linha `faixa de índice de refração`.
**Escopo:** correção local.

**Problema.** A linha dizia:

> **faixa de índice de refração** — um intervalo de índice (não um valor único) **dentro do qual várias gemas diferentes compartilham o mesmo ângulo-alvo de referência**.

Isso é falso na versão corrigida da aula, e é falso **contra a própria tabela três telas abaixo**: na faixa 1,56–1,65 convivem berilo 43°, turmalina 42° e topázio 41°. Pior, a linha contradiz frontalmente a entrada `ângulo-alvo` **duas linhas acima na mesma tabela**, que a auditoria já havia corrigido para "é publicado **por material**, não por faixa de índice; a faixa organiza a leitura da tabela, não determina o valor".

A gravidade não vem do erro em si, e sim de **onde ele estava**. A tabela de vocabulário é a primeira coisa que o leitor lê, é o lugar de máxima autoridade de uma aula (é onde LC-01 promete que os termos serão definidos), e a definição que ela trazia é precisamente a tese que as seções seguintes gastam 1.600 palavras derrubando. O leitor entra com o modelo errado instalado pela fonte que deveria protegê-lo dele, e depois passa a aula inteira encontrando evidência contra o que a aula acabou de lhe dizer — sem que nada explique a contradição. É a diferença entre uma aula que corrige uma intuição comum (bom ensino) e uma aula que se contradiz (ruído).

**Correção aplicada.**

> **faixa de índice de refração** — um intervalo de índice (não um valor único) usado para **organizar** a leitura da tabela, agrupando gemas de índice próximo. Não implica que elas recebam o mesmo ângulo-alvo: dentro de uma mesma faixa os valores publicados diferem.

Preserva o termo (que o título, o objetivo `lapidacao-m08-oa02` e a coluna da esquerda da tabela usam), mata a proposição falsa, e alinha a entrada com a `ângulo-alvo` acima dela. Fora de `palavras_corpo` pela régua de LC-02.

---

## 🟠 1 — a01 · o bloco "Próxima aula" promete a versão refutada da aula 02

**Tipo:** progressão — a aula anterior anuncia como fato o que a seguinte derruba
**Onde:** `08-optica-do-facetado-aula-01`, "Próxima aula" e "O que não concluir".
**Escopo:** correção local. Toca texto adjacente a alegação auditada sem alterar fato nenhum.

**Problema.** A a01 fechava assim:

> Na aula 02 …: a tabela que converte o princípio desta aula em valores de referência **para cada família de gema**, **a base física de por que índices mais altos toleram pavilhões mais rasos**, e os limites…

"Por que índices mais altos toleram pavilhões mais rasos" é literalmente a tese que o 🔴 3 da auditoria (`TAB-BASE-FISICA-001`) derrubou. A a01 não a apresenta como intuição a ser testada — apresenta como **o que a próxima aula vai demonstrar**. O leitor fecha a a01 com a proposição errada instalada e com o selo de "isto é o que vem a seguir"; abre a a02 e encontra o oposto, sem que a a02 saiba que precisa desfazer uma promessa.

Este é o custo didático típico de uma auditoria bem feita que só toca os arquivos onde a alegação vive: `TAB-BASE-FISICA-001` mora na a02, e a a01 não tinha alegação nenhuma sobre isso — só uma frase de encaminhamento. Frases de encaminhamento não têm `claim_id` e por isso atravessam a auditoria intactas mesmo quando ficam falsas.

**Correção aplicada.**

> …a tabela que converte o princípio desta aula em valores de referência **publicados material a material**, **a base física que explica por que esses valores são quase planos enquanto o ângulo crítico despenca**, e os limites do que a tabela por si só resolve.

E, em "O que não concluir", "por que a margem acima do crítico **varia** com o índice" virou "**cresce** com o índice em vez de encolher" — que é exatamente o que `TAB-EX-MARGEM-001` calcula (quartzo 1,5°, safira 7,6°). O bloco "Próxima aula" não conta para `palavras_corpo`; a linha de "O que não concluir" conta.

---

## 🟠 2 — a02 · o enquadramento de abertura e o título da seção ainda descrevem a aula pré-auditoria

**Tipo:** título que não corresponde à seção / pré-requisito descrito pela versão antiga
**Onde:** `08-optica-do-facetado-aula-02`, bloco "Antes de começar" e título da seção da tabela.
**Escopo:** correção local. É o quinto item do encargo da auditoria.

**Problema, em duas peças.**

**(a) "Antes de começar", segundo marcador.** Dizia: "*índice de refração* já foi definido; aqui ele é usado como **a única variável de entrada da tabela**". Depois da correção, o índice não é a variável de entrada de nada: ele **calcula** a coluna do ângulo crítico e **organiza** as linhas, mas o ângulo-alvo — a coluna que interessa — vem publicado material a material e não é função dele. O bloco que existe para dar ao leitor o enquadramento correto antes de começar dava o enquadramento anterior.

**(b) Título da seção.** "### A tabela — valores de referência **por faixa**", sobre uma tabela cuja coluna de valores é explicitamente por material e cujo parágrafo de abertura diz "não por faixa de índice". **Quarta ocorrência do mesmo padrão neste curso** — módulos 04, 06 e 07 tiveram título de seção desatualizado por auditoria, e sempre na a02. A auditoria de 2026-09-04 já havia trocado o título da seção de base física da a02 por esse motivo e deixou o encargo explícito de olhar este segundo título. Confirma-se: é regularidade, não coincidência.

**Correção aplicada.**

- Marcador: "Aqui ele entra de duas maneiras — calcula o ângulo crítico de cada material e organiza as linhas da tabela —, mas não é ele que determina o ângulo-alvo: esse vem publicado material a material." (fora de `palavras_corpo`)
- Título: "### A tabela — **ângulo crítico calculado, pavilhão publicado por material**", que é literalmente a distinção entre as duas colunas que o parágrafo abaixo dele faz.

Removida, de passagem, uma circularidade no parágrafo de abertura da seção: "é publicado material a material — não por faixa de índice, e é por isso que **aparece por material**" (a razão repetindo a afirmação) virou "…e por isso a tabela **tem uma coluna de material**", que explica a estrutura da tabela em vez de girar em torno de si.

---

## 🟠 3 — a06 · "índice" muda de significado sem aviso, depois de cinco aulas

**Tipo:** LC-01 — homônimo central usado sem desambiguação
**Onde:** `08-optica-do-facetado-aula-06`, seção "O que o ray tracing faz"; vocabulário; recap.
**Escopo:** correção local.

**Problema.** Ao longo de cinco aulas, "índice" significou **índice de refração** neste módulo — está no título da a02, no objetivo `oa02`, na coluna da esquerda da tabela, em dezenas de frases. Na a06, sem transição, aparece:

> o **GemCad**, que especifica cada faceta **(índice, ângulo, altura)**

Aqui "índice" é a posição no disco dentado da facetadora — o *index gear*, que só o módulo 09 vai ensinar. O leitor que carrega o significado das cinco aulas anteriores lê "cada faceta tem seu índice, seu ângulo e sua altura" e conclui que cada faceta tem um índice de refração próprio, o que é absurdo e, pior, plausível o bastante para não disparar alarme — afinal a aula acabou de falar de traçar raios por refração. E o erro é estrutural, não de detalhe: é a definição do que o GemCad **é**, que sustenta o resto da aula.

O mesmo termo aparecia sem gloss na entrada de vocabulário `diagrama de lapidação` ("ângulos e índices de cada faceta") e no recap.

**Correção aplicada.** Na primeira ocorrência do corpo, aposto que define e contrasta:

> que especifica cada faceta por **índice** — a posição no disco dentado da máquina, não o índice de refração —, ângulo e altura

Vocabulário e recap alinhados a "posição de índice". A correção mínima é o aposto, não um parágrafo sobre o sistema de índice: esse é o assunto de `lapidacao-m09-a01`, e ensiná-lo aqui inflaria a aula que fecha o módulo.

---

## 🟠 4 — a03 · "luminosidade" entra como quarto termo, sem definição, na aula sobre não confundir termos

**Tipo:** LC-01 — termo técnico usado antes de definido
**Onde:** `08-optica-do-facetado-aula-03`, seção "Brilho"; também no exemplo trabalhado e no recap.
**Escopo:** correção local.

**Problema.** A aula 03 é a aula da precisão terminológica: sua primeira seção se chama "Por que separar os três por mecanismo, não por definição", e a auditoria reforçou a entrada de vocabulário de `brilho` com a advertência sobre *brilliance* × *brightness* na USFG. No meio desse aparato, o corpo introduz um **quarto** substantivo — "talhes de **luminosidade** alta" — sem dizer o que ele é nem como se relaciona com os três.

Numa aula qualquer isso seria 🟡. Aqui é 🟠, porque a aula acabou de ensinar ao leitor que palavras parecidas nomeiam mecanismos diferentes e que tratá-las como sinônimos "custa caro no projeto". Treinado assim, o leitor faz a coisa certa — assume que "luminosidade" é um quarto efeito distinto — e erra por obedecer à aula. O termo ainda reaparece duas vezes (exemplo trabalhado e recap), consolidando o quarto conceito inexistente.

**Correção aplicada.** Aposto na primeira ocorrência:

> são descritos como talhes de **luminosidade** alta — **que é este mesmo *brightness*, e não um quarto efeito** —, mesmo tendo pouca dispersão visível.

**Financiamento:** 13 palavras, pagas pelos 15 do 🟡 4 (redundância em "Os três juntos"). Nenhuma alegação tocada.

---

## 🟠 5 — a05 · a aula depende da a02 e da a04 e não declara nenhuma das duas

**Tipo:** LC-03 — pré-requisito usado e não declarado
**Onde:** `08-optica-do-facetado-aula-05`, linha `**Pré-requisito:**` e bloco "Antes de começar".
**Escopo:** correção local, só no cabeçalho.

**Problema.** O cabeçalho da a05 declarava a a01 deste módulo, a a03 do módulo 05 e o curso de Gemologia. Não declarava a **a02** nem a **a04** — e a aula:

- abre literalmente com "A aula 04 tratou a profundidade de pavilhão como uma variável que troca desempenho óptico por rendimento";
- ancora **as duas prescrições centrais** ("mais raso" e "mais fundo") em relação ao **valor-alvo da aula 02**, referenciado seis vezes no corpo;
- fecha o exemplo trabalhado com "a mesma tabela da aula 02".

Ou seja: as duas aulas de que a a05 mais depende são as duas que ela não declara. LC-03 não é formalidade neste curso — é a peça de contrato que sustenta a promessa de "progressão sem usar conceito antes de ensiná-lo, verificável por LC-01 e LC-03". Para quem lê o módulo em ordem o custo é baixo; para quem volta à a05 isolada — que é o modo de uso normal de um vault de Obsidian — o cabeçalho manda estudar as aulas erradas.

**Correção aplicada.** a02 e a04 acrescentadas à linha de pré-requisito com wikilink e com a razão de cada uma ("o valor-alvo publicado, do qual esta aula desloca o projeto para um lado ou para o outro"; "o primeiro compromisso jogado nesta mesma variável"), e um marcador novo em "Antes de começar" que reativa o que elas entregaram e amarra o vocabulário: **é sempre em relação ao valor-alvo que a a05 diz "mais raso" ou "mais fundo"** — a âncora que a aula usava sem nomear. Ambos fora de `palavras_corpo`.

---

## 🟡 1 — a02 · a nota sobre berilo e zircão era uma errata sem leitor, e partia o argumento ao meio

**Onde:** `08-optica-do-facetado-aula-02`, seção da tabela.

A nota abria com "**Duas faixas costumam ser mal lidas.**" e corrigia colocações que **a tabela ao lado já faz certo** — berilo está em 1,56–1,65, zircão em 1,81–2,02. Para o leitor de estreia não há nada a desfazer: o parágrafo responde a uma pergunta que ele não tem. Ele existe porque a versão **anterior** da tabela punha berilo e zircão nas faixas impossíveis (🔴 2 da auditoria), e a correção virou nota de errata dirigida a um leitor que não existe.

Agravante de posição: a nota estava **entre** o conjunto da USFG e o caso do diamante, cortando ao meio a linha "os valores são planos → o diamante é o caso extremo que mostra por quê".

**Correção aplicada — reenquadramento e reposicionamento, sem tocar em fato nenhum.** A abertura de errata virou regra de leitura positiva, que serve à tese central da aula (a faixa organiza, não determina):

> E a faixa é índice de leitura, não compartimento — quem decide a linha de um material é o índice real dele. **Berilo não existe abaixo de 1,55**: …

E o parágrafo subiu para logo depois da análise da coluna plana, encadeando com o berilo que aquela análise acabou de citar. A ordem da seção passou a ser: tabela → a coluna é plana (o teto aparece) → a faixa é índice, não compartimento → o diamante como caso extremo → o conjunto da USFG com o "no magic bullet" → e daí direto para "O que a tabela não substitui", que desenvolve exatamente essa ressalva. Os dados de `TAB-ALVO-FAIXA-002` (berilo 1,562–1,602; zircão 1,810–2,024, *high* 1,92–1,98, *low* metamíctico ~1,75) seguem íntegros, palavra por palavra.

---

## 🟡 2 — a02 · a refutação chegava antes de qualquer número, e não havia transição da primeira seção para a segunda

**Onde:** `08-optica-do-facetado-aula-02`, seções "Por que a tabela existe" e "A base física".

Dois atritos na linha argumentativa reescrita pela auditoria, ambos de custo baixo e correção barata.

**(a)** A seção 1 terminava em "a literatura publica valores de referência" e a seção 2 abria em "O ângulo crítico dá o piso", sem ponte. O leitor não sabe que pergunta a seção 2 está respondendo, e a seção 2 é a mais densa da aula.

**(b)** A seção 2 dizia "Isso explicaria um alvo caindo depressa com o índice, **e não é o que a literatura publica**" — uma negação que o leitor tem de segurar em suspenso por ~250 palavras, porque ele **ainda não viu** o que a literatura publica. Num material sem professor, uma negação sem referente é a forma mais cara de suspense.

**Correção aplicada.** Ponte no fim da seção 1 ("Sobra a pergunta que a seção seguinte responde — o que decide onde esses valores caem") e referente imediato na negação ("…e não é o que a literatura publica: **os valores da tabela abaixo mal se movem enquanto o crítico despenca**"). A estrutura hipótese → dado → confirmação continua de pé; o que muda é que o leitor agora sabe o que está esperando.

---

## 🟡 3 — a01 · duas remissões descreviam a a02 pela organização que ela não usa

**Onde:** `08-optica-do-facetado-aula-01`, fim da seção "O outro extremo" e recap.

"a faixa de ângulos de retorno eficiente que a aula 02 **tabela por índice de refração**" (corpo) e "tabelada por índice de refração na aula 02" (recap). Mesma família do 🟠 1, em grau menor: não é falso que a a02 organize por faixa, mas é a metade da a02 que ela ensina a **não** usar como determinante. Trocadas por "a aula 02 **preenche com os valores publicados para cada material**". Uma variante análoga na a01 — "a margem que a tabela da aula 02 já embute" — foi conferida e **mantida**: continua verdadeira, porque os valores publicados carregam margem.

---

## 🟡 4 — a03 · o compromisso dos três efeitos era enunciado quatro vezes seguidas

**Onde:** `08-optica-do-facetado-aula-03`, seção "Os três juntos".

A frase "material de dispersão alta com poucas facetas grandes maximiza o brilho e sacrifica o fogo; com muitas facetas pequenas revela o fogo mas cada flash de branca fica menor" aparecia no fim da seção "Dispersão", de novo em "Os três juntos", de novo (desenvolvida em três parágrafos) no exemplo trabalhado, e de novo no recap. Redundância deliberada em ponto difícil é boa prática deste curso; **quatro vezes em pouco mais de 400 palavras**, sendo que a terceira é o exemplo trabalhado imediatamente abaixo, não é reforço, é atrito.

Comprimida a segunda ocorrência — a mais próxima da primeira e a menos informativa — para "troca fogo por brilho; com muitas facetas pequenas, o inverso". **−15 palavras**, que financiaram o 🟠 4. `BRI-PROJ-COMPR-001` está integralmente preservado: o conteúdo causal segue no corpo, no exemplo e no recap.

---

## 🟡 5 — a04 · "profundidade total" definida no vocabulário e ausente do corpo

**Onde:** `08-optica-do-facetado-aula-04`, tabela de vocabulário.

A entrada existia; o termo não aparece uma vez no corpo, que fala sempre em "profundidade de **pavilhão**". É sintoma direto do encargo 4 da auditoria (as seis aulas foram enxugadas para financiar as correções): o parágrafo que usava o termo saiu, a entrada ficou. Não é conteúdo perdido — nada no argumento da a04 precisa da altura total — mas é carga cognitiva paga por nada: o leitor decora um termo na abertura e passa a aula esperando que ele apareça.

**Correção aplicada.** Linha removida. A a04 fica com cinco entradas, dentro da faixa de 5 a 10 de LC-03.

---

## 🟡 6 — a04 · a oposição precisão × nativo estava enterrada dentro do terceiro dos "três lugares"

**Onde:** `08-optica-do-facetado-aula-04`, seção "Onde o compromisso é decidido: três lugares do projeto".

A seção promete três lugares e os entrega em negrito: **Profundidade de pavilhão**, **Presença ou ausência de culaça**, **Contorno**. Mas depois do parágrafo de contorno vêm mais dois parágrafos — a definição de corte de precisão × corte nativo e o "Ponto em aberto" de LC-08 — que **não são sobre contorno** e abriam com "É aqui que a literatura opõe…", ancorando-se no "aqui" da decisão de contorno. Quem lê pela estrutura (e a seção convida a isso, com três negritos) fica sem saber onde o terceiro lugar termina, e a distinção mais disputada da aula chega como apêndice do item 3 em vez de como o que é: o rótulo que a literatura dá ao eixo inteiro.

**Correção aplicada.** Abertura trocada para "**Os três lugares reaparecem juntos numa oposição que a literatura nomeia:** corte de precisão contra corte nativo", que fecha a lista de três antes de abrir a oposição. `FAC-REN-CONTORNO-001` e `FAC-REN-NATIVO-001` intactos.

---

## 🟡 7 — a05 e a06 · a "lacuna de cor" corrigida está bem ensinada, mas o leitor é acusado três vezes de uma suposição que já foi desfeita

**Onde:** `08-optica-do-facetado-aula-05` ("O que não concluir", "Próxima aula") e `08-optica-do-facetado-aula-06` (abertura das lacunas, lacuna 1, exemplo trabalhado, "Erros comuns", recap). **É o terceiro ponto de atenção prioritária do encargo.**

**Avaliado: a reformulação está clara, e a divisão de trabalho entre as duas aulas é correta.** A a05 mantém o corpo inteiramente sobre cor e profundidade e só sinaliza a limitação em "O que não concluir"; a a06 é quem a desenvolve, com a estrutura certa — nomeia a suposição comum, mata-a com as capacidades documentadas do GemRay, e só então lista as três lacunas reais. A a06 acerta especialmente ao **não** deixar a lacuna 1 vaga: "Uma safira zonada é lida como safira de cor média uniforme: o escurecimento por profundidade aparece, a faixa não" é a frase que faz a distinção morder. Nenhuma redundância de **conteúdo** entre as duas: a a05 diz que a ferramenta não substitui a leitura do bruto, a a06 diz por quê.

O que sobra é de **tom**, não de substância. Entre as duas aulas, o leitor é posicionado como portador da crença errada em quatro lugares — "desfaça-se uma suposição comum" (a06), "**Ao contrário do que se supõe**, a simulação teria apontado…" (exemplo trabalhado da a06), "**Supor** que o ray tracing ignora cor" (Erros comuns), depois de a a05 já o ter prevenido duas vezes. Na terceira acusação o leitor nunca teve a chance de ter a crença: a a05 o vacinou antes.

**Ação.** Removido "Ao contrário do que se supõe," do exemplo trabalhado da a06 (−5 palavras) — o único dos quatro que é puramente retórico, já que os outros três têm função estrutural (introduzir as lacunas, ser um erro comum, fechar o recap). O restante mantido: a suposição é genuinamente corrente no ofício, e LC-07 obriga "Erros comuns" e "Recap relâmpago" a existirem.

Corrigida, na mesma passada, uma referência vaga da a05: "o que ele não substitui é a leitura de material **da seção anterior**" — e "seção anterior", lida de dentro de "O que não concluir", tanto pode ser o exemplo trabalhado quanto "Erros comuns". Trocada por "a leitura de **saturação do bruto (módulo 05)**", que nomeia o alvo. Palavra por palavra, neutra.

---

## 🔵 1 — o título da aula 02 · **avaliado e MANTIDO**, com justificativa

**É o segundo ponto de atenção prioritária do encargo, e a decisão é não mexer.**

A suspeita procede em forma: o título é "Ângulos-alvo **por faixa de índice de refração** — a tabela e o que ela realmente diz", e a lição central passou a ser que os valores são publicados por material. Três razões, na ordem do peso, sustentam a manutenção.

**(1) O título já contém o seu próprio antídoto, e ele é um bom dispositivo didático.** A segunda metade — "**e o que ela realmente diz**" — enquadra a primeira como *o objeto sob exame*, não como *a tese ensinada*. É a estrutura clássica de uma aula que parte da expectativa ingênua do leitor e a corrige: "por faixa de índice" é exatamente o que quem chega ao assunto espera encontrar, e é o que o mundo real chama a tabela. Remover essa metade **apagaria a expectativa que a aula existe para corrigir** e deixaria a aula sem adversário.

**(2) A cascata é muito maior do que o encargo supõe, e o item mais alto dela é intocável por esta skill.** A expressão "ângulos-alvo por faixa de índice de refração" não vive só no título e no nome do arquivo. Ela está, verbatim:

| Onde | O quê |
|---|---|
| `course-state.yaml` → `learning_outcomes` | "…dos **ângulos-alvo por faixa de índice de refração** e dos compromissos entre brilho, cor e rendimento" |
| `course-state.yaml` → `modules[08].objective` e hub do módulo | "ângulo crítico, **ângulos-alvo por faixa de índice de refração**, brilho, dispersão e cintilação" |
| `course-state.yaml` → `lapidacao-m08-oa02` e o bloco "Ao final você vai conseguir" da aula | "Ler uma tabela de **ângulos-alvo por faixa de índice de refração**, explicar sua base física e declarar seus limites" |
| `_contexto.md`, "Escopo por bloco temático" e "Profundidade combinada no facetamento" | "**ângulos-alvo por faixa de índice**" (duas ocorrências) |

Trocar o título da aula sem trocar o **objetivo de aprendizagem** produziria uma aula cujo título e cujo `lapidacao-m08-oa02` discordam — mais incoerência, não menos. E trocar o objetivo é decisão de **currículo**: pertence ao `planejador-curricular` / `gerador-de-curso-modular`, não a esta skill nem à auditoria (que registrou a mesma reserva no encargo: "objetivo de aprendizagem não se altera por auditoria"). Um renome parcial deixaria o curso pior do que encontrou.

**(3) O defeito real era interno, e foi corrigido.** O que de fato atritava era o **título da seção** ("valores de referência por faixa", sobre uma tabela por material) e a **entrada de vocabulário** — 🔴 1 e 🟠 2, ambos aplicados. Com a entrada de vocabulário corrigida, o leitor recebe a chave de leitura do título **antes** de entrar no conteúdo: a faixa organiza, não determina. O título deixa de ser uma afirmação errada e passa a ser o rótulo do objeto que a aula disseca.

**Encaminhado, não executado:** se o `gerador-de-curso-modular` reabrir os objetivos do módulo 08 por outro motivo, `lapidacao-m08-oa02` merece ser reformulado para algo como "Ler a tabela de ângulos-alvo, explicar por que os valores publicados são quase planos apesar da queda do ângulo crítico, e declarar seus limites" — e só então o título da aula, o nome do arquivo e os wikilinks acompanham, numa passada única e coerente.

---

## 🔵 2 — verificação corte a corte dos enxugamentos da auditoria (encargo 4)

A auditoria cortou cerca de 283 palavras da a06 e deixou a a04 com ~60 líquidas a menos depois de ganhar três blocos novos. Sem a versão pré-auditoria em disco, a verificação foi feita por **sintoma**: um corte que remove conteúdo deixa rastro — termo definido e não usado, referência a passagem inexistente, argumento com degrau, objetivo descoberto.

Varredura completa das seis aulas, entrada de vocabulário por entrada de vocabulário e remissão por remissão. **Um sintoma encontrado, e ele confirma o encargo:** `profundidade total` na a04 (🟡 5) — entrada órfã cujo parágrafo evaporou. Um segundo, menor, na a06: `modelo idealizado` estava definido no vocabulário, aparecia no recap, e sumira do corpo, onde a lacuna 2 dizia "o modelo geométrico". Alinhado para `modelo idealizado`, sem custo de palavras.

**Nada mais.** Os seis objetivos continuam cobertos por Conteúdo **e** exemplo **e** recap; nenhuma remissão interna aponta para passagem removida; as três seções da a06 que mais encolheram ("O que essas métricas medem, de fato", "Por que a tabela e a simulação não competem", "O lugar certo da ferramenta") continuam entregando o que `oa06` pede, cada uma. A conclusão é a mesma do módulo 07: os cortes da auditoria removeram repetição, não conteúdo.

---

## 🔵 3 — LC-08: duas declarações para seis aulas (encargo 3)

**Avaliado: duas é o número certo.** Ambas são divergências genuínas sobre um fato, não decisões de gosto encenadas como controvérsia, e ambas estão no **coração** do objetivo da sua aula, não na margem:

- **a03** — até onde "mais facetas por mais fogo" compensa. Está dentro de `oa03` ("pelo que cada um cobra do projeto"): sem o ponto de retorno decrescente, o leitor sai com uma regra monotônica falsa.
- **a04** — a disputa sobre "corte nativo". Está dentro de `oa04`: o termo é um dos dois polos que a aula usa para nomear o compromisso, e usá-lo sem registrar que parte do comércio o emprega como sinônimo de defeito ensinaria uma categoria técnica neutra que não existe assim.

Ambas em **prosa**, com as aberturas padronizadas do curso ("Pergunta em aberto:", "Ponto em aberto:") — a convenção fixada na revisão do módulo 07, que reserva callout para pedido de ilustração. Conferido: o módulo 08 não usa callout em nenhuma das seis aulas, e portanto não repete o atrito do m07 a03. Nenhuma terceira candidata foi instalada: as duas cobrem os dois pontos em que a literatura de fato diverge, e um módulo de seis aulas com duas controvérsias está na mesma densidade do módulo 07 (uma para quatro).

---

## 🔵 4 — a04 · a derivação dos 76,9% · **não aplicada**, por teto

**Onde:** `08-optica-do-facetado-aula-04`, exemplo trabalhado, Rota A.

O exemplo afirma que "para uma seção elíptica de 1,3:1, o maior círculo inscrito tem área de 76,9% da elipse **(1/1,3)**". O leitor recebe a razão pronta; por que a razão entre as áreas é igual a `b/a` não está no texto — está só na alegação `FAC-REN-ELIPSE-001` (área da elipse = πab, do círculo inscrito = πb², razão = b/a). São duas linhas de geometria elementar que fechariam o passo.

**Não aplicado**, por três razões: (i) `oa04` é sobre **onde** o compromisso é decidido, não sobre geometria de elipse — o número está ali como ordem de grandeza, conforme LC-05; (ii) o resultado é verificável pelo leitor sem a derivação (1 ÷ 1,3 = 0,769 está explícito); (iii) a a04 entrou nesta revisão **acima** do teto (1605) e as ~20 palavras teriam de sair de mecanismo auditado. Registrado como oportunidade, se a a04 for reaberta com folga.

---

## Progressão

**LIMPA depois desta revisão; tinha um vazamento antes dela.** A cadeia a01 (o princípio) → a02 (os valores) → a03 (os efeitos que os valores servem) → a04 (o que eles custam em peso) → a05 (o que eles custam em cor) → a06 (o que a ferramenta calcula e o que não calcula) é estritamente crescente. Cada aula declara o que a anterior entregou, e **nenhuma usa resultado de aula posterior**: todas as remissões para frente são negativas, no bloco "O que não concluir" — verificado uma a uma.

O vazamento era o 🟠 1: a a01 anunciava a a02 pela tese refutada. Corrigido, a passagem a01→a02 ficou mais forte do que antes da auditoria, porque a a01 agora entrega à a02 exatamente a pergunta que a a02 responde ("por que esses valores são quase planos enquanto o crítico despenca") em vez de entregar uma resposta errada.

Duas amarrações que a auditoria criou e que esta revisão confirma como as melhores do módulo: **a01→a02**, o mecanismo da extinção (a luz perdida na segunda faceta) deixou de ser um detalhe da a01 e virou o **teto** que explica toda a tabela da a02 — a mesma proposição sustentando duas conclusões em níveis diferentes; e **a04→a05**, a mesma variável de projeto (profundidade de pavilhão) resolvendo dois problemas distintos, com a a05 abrindo por avisar que não são o mesmo compromisso e a a04 fechando com o mesmo aviso em "O que não concluir" — reforço cruzado deliberado, dos dois lados.

Pré-requisito externo do `curso-gemologia` citado **por nome** em a01, a02 e a05, nunca por wikilink. Verificado. Pré-requisitos internos por wikilink, todos resolvíveis dentro do curso.

---

## Cobertura de objetivos

| Objetivo | Nível declarado | Ensinado em | Exemplo | Recap | Célula vazia |
|---|---|---|---|---|---|
| `lapidacao-m08-oa01` | aplicar | a01 — quatro seções | sim (quartzo 35° × 43°) | sim | — |
| `lapidacao-m08-oa02` | aplicar | a02 — quatro seções | sim (quartzo × safira, mesmo 42°) | sim | — |
| `lapidacao-m08-oa03` | analisar | a03 — cinco seções | sim (zircão em brilhante × degrau) | sim | — |
| `lapidacao-m08-oa04` | analisar | a04 — três seções, três lugares | sim (ametista, rota A × rota B) | sim | — |
| `lapidacao-m08-oa05` | analisar | a05 — seis seções | sim (almandina × granada pálida) | sim | — |
| `lapidacao-m08-oa06` | explicar | a06 — seis seções | sim (safira zonada, métrica alta) | sim | — |

Um objetivo por aula, seis objetivos, seis aulas, **nenhuma célula vazia e nenhum conteúdo órfão**. Os seis verbos são de conhecimento observável — aplicar, ler/explicar, distinguir, explicar/identificar, relacionar, descrever/delimitar; nenhum "entender/conhecer/saber" e **nenhum verbo de execução**. Os três exemplos de nível `analisar` (a03, a04, a05) exercem de fato a análise: cada um compara **duas** alternativas sobre um material ou bruto fixo, isolando a decisão de projeto como a única variável — que é a forma canônica de fazer o leitor analisar em vez de reconhecer.

**Uma ressalva de forma, não de cobertura:** o enunciado de `oa02` ("ler uma tabela de ângulos-alvo **por faixa de índice de refração**") descreve a aula pela organização que ela ensina a relativizar. A cobertura é integral — a aula ensina a ler a tabela, explica a base física e declara os limites, que são as três partes do objetivo. O que fica desalinhado é o **enunciado**, e a correção dele é de currículo, não de didática: ver 🔵 1 e a nota ao `gerador-de-questionarios` abaixo.

**Varredura de competência de bancada:** nenhum achado. Todo texto acrescentado nesta revisão descreve leitura de tabela, geometria, nomenclatura e ordem de decisão de projeto — nunca operação de máquina nem destreza manual. A a06 continua declarando o manuseio de GemCad e GemRay como fora de escopo em "O que não concluir".

---

## Desalinhamento aula–avaliação

**NÃO VERIFICÁVEL nesta etapa** — o questionário do módulo 08 ainda não existe. Registrado para o `gerador-de-questionarios`, em ordem de importância:

1. **`oa02` NÃO pode ser cobrado na forma "dada a faixa de índice X, qual o ângulo-alvo?"** — essa é exatamente a proposição que a auditoria derrubou, e uma questão assim reintroduziria o erro corrigido como gabarito. A cobrança legítima de `oa02` é: (a) ler a tabela distinguindo a coluna **calculada** da **publicada**; (b) explicar por que a coluna publicada é plana enquanto o crítico despenca — o piso-com-teto; (c) declarar os limites (desenho de referência, "no magic bullet", o ray tracing como refinamento).
2. **`oa02` exige uma questão sobre a MARGEM, não sobre o alvo.** O resultado mais contraintuitivo do módulo é que a margem sobre o crítico **cresce** com o índice (quartzo 1,5°, safira 7,6°, mesmo pavilhão de 42°). Uma questão que dê dois materiais e peça a margem, ou que peça qual dos dois tem mais folga, testa a tese central. Uma que peça só o valor de 42° testa memória de tabela.
3. **`oa05` exige um caso em que a direção do ajuste NÃO é dedutível da tabela da a02.** Dois materiais de índice idêntico e saturações opostas — a estrutura do exemplo trabalhado das duas granadas. Uma questão em que o material já entrega a resposta ("é uma ametista escura, logo…") testa reconhecimento, não a relação que `oa05` cobra.
4. **`oa06` NÃO pode cobrar "o ray tracing não modela cor" em nenhuma forma, nem como distrator premiado.** É a afirmação falsa que era a espinha da aula 06 antes da correção. O que se cobra é a lacuna **real**: cor **uniforme atribuída**, não cor real do bruto. Um bom distrator é justamente "porque o software ignora a cor" — errado, e sedutor para quem leu uma versão antiga do assunto em outra fonte.
5. **`oa04` exige que o pavilhão raso apareça como manobra de RENDIMENTO, não como erro conservador.** Com o contorno solto, o pavilhão raso permite diâmetro maior — é a manobra agressiva mais comum do ofício, e a origem mais frequente de pedras janeladas. Uma questão que trate pavilhão raso como "cautela" reintroduz o 🟠 9 da auditoria.
6. **Armadilhas legítimas vindas da auditoria, todas boas como distratores:** coríndon recebe 42°, não 38°–40° (a02); o berilo recebe pavilhão **mais fundo** que o quartzo apesar do índice maior (a02); a dispersão **impede** o pavilhão do diamante de subir, não o levanta (a02); a extinção é escape na **segunda** faceta, não perda por absorção (a01, e a RIT não tem perda); *brilliance* é o guarda-chuva da USFG, *brightness* é o efeito isolado (a03); "corte nativo" é origem e método, não qualidade (a04); GemRay é programa **autônomo** do mesmo autor, não módulo do GemCad (a06).
7. **NÃO cobrar a margem de 2,5° da a01 como valor de projeto** — a auditoria a requalificou como leitura aritmética daquele exemplo; a literatura só diz "vários graus". Cobrar o **raciocínio** (por que existe margem) é legítimo; cobrar um número, não.
8. **Duas declarações de LC-08 (a03 e a04) NÃO podem ser cobradas como se tivessem resposta.** Se aparecerem, é como "o que está em aberto aqui e por quê" — o mesmo tratamento do questionário do módulo 07.
9. **Nível teórico:** nenhuma questão pode pedir ajuste, medição ou operação de facetadora, nem manuseio de GemCad/GemRay. O módulo tem **6 aulas**, acima do limiar de ~5–6 da skill, o que pode pedir questionários parciais mais um final cumulativo — ao contrário do questionário único do módulo 07.

---

## O que está bem feito

**A recuperação da aula 02 é o melhor trabalho do módulo, e ela sobreviveu à reescrita.** Depois de perder a tabela inteira para o 🔴 1 da auditoria, a aula não ficou remendada: ganhou uma tese própria — piso que desce contra teto que não desce — que é mais interessante do que a que tinha antes, e um exemplo trabalhado que **confirma** essa tese em vez de a contradizer. Dois materiais com pisos separados por 6,1° recebendo o mesmo 42° é um dado que só faz sentido sob a explicação certa, e a aula o usa exatamente assim. Poucas aulas saem de uma refutação mais fortes do que entraram.

**A a05 é a aula mais bem construída do módulo.** Abre desarmando a confusão com a a04 antes que ela aconteça ("é importante não confundir os dois compromissos"), constrói a mesma variável servindo a duas lógicas **opostas**, e — o toque que o módulo hub previa como o ponto mais sutil — dedica uma seção inteira à **ordem de decisão** quando a cor não é uniforme: orientação primeiro, profundidade depois, porque a primeira decide **onde** a cor boa fica no caminho e a segunda decide **quanto** caminho existe. Essa é a distinção que separa quem entendeu de quem decorou a regra.

**A a06 fecha o módulo em vez de apenas terminá-lo.** A escolha de nomear a suposição errada e matá-la antes de listar as lacunas reais é boa pedagogia — e é o oposto do que uma aula corrigida às pressas faria, que seria apagar a afirmação falsa e seguir. A frase "Uma safira zonada é lida como safira de cor média uniforme: o escurecimento por profundidade aparece, a faixa não" faz, em vinte palavras, o trabalho que um parágrafo inteiro de qualificação faria pior.

**A separação entre a04 e a05 é exemplar como projeto de módulo.** A mesma variável física, dois compromissos, duas aulas, cada uma avisando explicitamente que a outra existe e que não são a mesma coisa. É o antídoto exato para o erro que o leitor cometeria sozinho.

---

## Não executado, por escopo

- Módulo **NÃO** marcado como concluído — `modules[08].status` permanece `pending`, só fecha depois do questionário.
- **Questionário NÃO gerado** — é a etapa 5. Flashcards não se aplicam (dispensados a partir do módulo 06).
- **Nenhum questionário nem flashcard alterado** — esta skill reporta desalinhamento, não o corrige.
- **Objetivos de aprendizagem NÃO alterados** — `lapidacao-m08-oa02` fica como está; a reformulação sugerida é decisão de currículo (ver 🔵 1).
- **Título e nome de arquivo da aula 02 NÃO alterados** — avaliado e mantido, com justificativa de cascata (🔵 1). Nenhum wikilink do módulo 08 mudou de destino; o hub não precisou de renome.
- **Validador estrutural NÃO rodado** — etapa da `geo-operacional`.
- **`_curso.md` NÃO reconciliado** — etapa da `geo-operacional`.
- **Nenhum fato novo introduzido.** Todo texto acrescentado reformula, conecta ou desambigua material já auditado; as 38 alegações e seus `claim_id` de 4 segmentos seguem intactos, nenhum renomeado, nenhum removido.

---

## Régua de `palavras_corpo`

A mesma de `_contexto.md` (2026-09-02): de `## Conteúdo` ao fim de `## Recap relâmpago` inclusive, `len(texto.split())`. A contagem reproduziu **exatamente** os seis valores declarados pela correção antes desta revisão (1576/1543/1592/1605/1599/1602), o que revalida a régua pela **sétima** vez.

| Aula | Pós-correção | Pós-revisão | Δ |
|---|---|---|---|
| a01 | 1576 | **1587** | +11 |
| a02 | 1543 | **1600** | +57 |
| a03 | 1592 | **1589** | −3 |
| a04 | 1605 | **1598** | −7 |
| a05 | 1599 | **1597** | −2 |
| a06 | 1602 | **1600** | −2 |

Nenhuma aula precisou ser dividida em Parte 1 / Parte 2. **As duas aulas que entraram acima do teto saíram conformes** — a a04 (1605) e a a06 (1602) —, cada uma por corte de redundância declarado acima, sem invocar a folga do til. A a02, que entrou com a maior folga do módulo (1543, herdada do enxugamento da auditoria), gastou-a inteira nas correções do 🟠 2 e dos 🟡 1 e 🟡 2, e fechou em 1600 exatos. Rodapés ressincronizados nas seis.
