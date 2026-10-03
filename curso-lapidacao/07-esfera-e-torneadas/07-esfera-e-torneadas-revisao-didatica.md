# Revisão didática: Módulo 07 — Esfera e formas torneadas

**Curso:** Teoria da lapidação — do desbaste ao projeto óptico (`lapidacao`)
**Módulo:** 07 — Esfera e formas torneadas (área IV. Talhes de superfície curva)
**Escopo:** as 4 aulas do módulo. Questionário ainda não existe — é a etapa 3. Baralho não se aplica (dispensado a partir do módulo 06).
**Modo:** `review-and-fix`
**Data:** 2026-09-04
**Revisor:** geo-arquiteto (Opus)
**Contrato de nível:** `ensino-medio-com-gemologia-v1`
**Roda depois de:** auditoria científica de 2026-09-04 (`07-esfera-e-torneadas-auditoria.md`), que fechou com `open_findings` vazio.

**Veredito:** Bem ensinado com ressalvas — **um 🔴, resolvido**.

---

## Resumo

| Severidade | Quantidade |
|---|---|
| 🔴 Bloqueante | 1 |
| 🟠 Laranja | 2 |
| 🟡 Amarelo | 4 |
| 🔵 Azul (avaliado, com ou sem ação) | 3 |

**Aulas alteradas:** todas as quatro.
**`palavras_corpo` pós-auditoria → pós-revisão:** a01 1592→**1594** · a02 1589→**1590** · a03 1590→**1589** · a04 1594→**1596**. As quatro sob o teto de ~1600 de LC-02.

**O 🔴 é de outro tipo que os do módulo 06.** Não é termo indefinido nem exemplo insuficiente: é uma **obrigação nomeada do contrato do curso que a aula não cumpriu**. O `_contexto.md` lista três pontos em que a ilustração é essencial e a aula tem de pedi-la explicitamente — anatomia da pedra (m01 a02), as três coordenadas da faceta (m09 a02 e a03) e **a convergência da esfera (m07 a01)**. A a01 não pedia ilustração nenhuma. É o tipo de defeito que só uma revisão que lê o contrato pega, porque o texto da aula, isolado, não parece ter buraco.

---

## 🔴 1 — a01 · a ilustração que o contrato do curso nomeia para esta aula não existia

**Tipo:** objetivo apoiado em representação ausente / obrigação de contrato não cumprida
**Onde:** `07-esfera-e-torneadas-aula-01`, seção "Do cubo ao poliedro".
**Escopo:** correção local.

**Problema.** O `_contexto.md`, em "Preferências de ensino", nomeia **três** pontos do curso inteiro em que a ilustração é essencial e a aula deve pedi-la de forma explícita. Um deles é, literalmente, "a convergência da esfera (m07 a01)". A aula não trazia pedido de ilustração — nem callout, nem menção.

Não é formalismo. O argumento inteiro da a01 é **espacial e comparativo**: um sólido encolhendo a distância entre seu ponto mais distante e seu ponto mais próximo, quatro vezes seguidas, sempre em torno do mesmo centro. Em prosa, o leitor recebe quatro pares de números (26/15, 21/15, …) e precisa construir mentalmente os poliedros para ver que a faixa entre eles estreita. Quem já enxerga um cuboctaedro não precisa da aula; quem não enxerga não constrói o que a aula pede a partir das palavras. Este é exatamente o caso em que a decisão de contrato foi tomada.

Duas outras aulas do curso já cumprem a obrigação e deram o precedente de forma: o m01 a02 usa `> [!tip] Peça a ilustração aqui` e o m04 a04 usa `> [!note] Ilustração necessária`, ambas descrevendo os quadros e dizendo **o que a figura tem de deixar claro**.

**Correção aplicada.** Callout instalado logo após o parágrafo da convergência, no formato do m04 (o precedente mais recente com callout nomeado), pedindo quatro quadros lado a lado — cubo, cuboctaedro, o poliedro seguinte, a esfera —, todos com o **mesmo centro marcado**, com os raios de cada etapa, e declarando o que a figura precisa mostrar: a faixa entre o ponto mais distante e o mais próximo estreitando a cada quadro. O "mesmo centro marcado" não é detalhe: é a exigência de centro único que a segunda metade da aula desenvolve, e a figura passa a ancorá-la.

**Financiamento.** 57 palavras, financiadas por corte de redundância em seis pontos da a01 — ver 🔵 1, onde cada corte é conferido.

---

## 🟠 1 — a02 · título de seção desatualizado pela própria auditoria (regressão)

**Tipo:** título que não corresponde à seção
**Onde:** `07-esfera-e-torneadas-aula-02`, seção "O princípio do copo casado e do eixo cruzado".
**Escopo:** correção local.

**Problema.** A auditoria de 2026-09-04 reescreveu essa seção inteira e removeu do módulo a noção de "par de copos casados" — a entrada de vocabulário foi apagada, e o argumento de convergência deixou de depender de dois copos de raio idêntico apontando um para o outro, passando a depender da coroa de contato e da correção mútua entre cabeçotes de mola. **O título ficou.** Um leitor que usa o sumário, ou que lê em diagonal, procura por "copo casado" no corpo e não encontra — o termo não existe mais em lugar nenhum da aula.

É a mesma patologia que a revisão do módulo 06 pegou na a02 daquele módulo ("Por que a ordem é fixa", depois que a auditoria mostrou que a ordem não era toda fixa), e a mesma que a revisão do módulo 04 pegou. **Terceira ocorrência do mesmo padrão**: quando a auditoria reescreve o corpo de uma seção, o título é o que sobrevive errado. Vale registrar como regularidade para as próximas auditorias deste curso — conferir títulos de seção é passo obrigatório da Fase 2.

**Correção aplicada.** Título trocado para "**O copo, a coroa de contato e a correção mútua**", que é literalmente a estrutura dos dois parágrafos abaixo dele: primeiro o instrumento, depois o contato em coroa, depois o mecanismo que faz o arranjo convergir em vez de só desbastar.

---

## 🟠 2 — a04 · "forma torneada" é o nome do módulo e nunca era definida no corpo

**Tipo:** LC-01, termo central sem definição na primeira aparição
**Onde:** `07-esfera-e-torneadas-aula-04`, seção "Duas exigências diferentes".
**Escopo:** correção local.

**Problema.** Efeito colateral da correção do 🔴 4 da auditoria. Ao instalar a distinção entre **sólido de revolução estrito** e **forma de eixo único**, a auditoria deixou "forma torneada" — que é o nome do módulo, do título da aula, do objetivo `lapidacao-m07-oa04` e da aula 03 que remete a ela — sem definição no corpo. A equivalência existia, mas só dentro de um parêntese da tabela de vocabulário.

O leitor chega à a04 com "forma torneada" ecoando desde o índice do curso, encontra dois termos novos que não são esse, e tem de deduzir a correspondência de uma tabela que ele leu antes de saber o que os termos significavam. Pior: as duas leituras possíveis levam a respostas opostas na avaliação — se "forma torneada" for o conjunto estrito, o obelisco fica de fora do módulo; se for o largo, fica dentro. É exatamente a distinção que `oa04` cobra.

**Correção aplicada.** Uma frase acrescentada ao fecho da seção, ao lado da fórmula `estrito ⊂ eixo único` que já estava lá: *"E **forma torneada**, o nome que o título deste módulo usa, é o rótulo do ofício para o **segundo** conjunto — o mais largo, não o mais estrito."* A definição fica no ponto exato em que os dois conjuntos acabaram de ser separados, que é o único lugar em que ela é compreensível.

---

## 🟡 1 — a03 · o callout de controvérsia fugia da convenção do curso

**Onde:** `07-esfera-e-torneadas-aula-03`, seção "Bandeamento".

A auditoria instalou o LC-08 do módulo como um callout `> [!question] Em aberto`. Varredura em todas as aulas dos módulos 01 a 06: o curso **não usa callout** para controvérsia declarada. Usa prosa corrida, com uma abertura padronizada — "Controvérsia em aberto:" (m02), "Fica em aberto:" (m01, m02, m04), "Pergunta em aberto:" (m03), "Ponto em aberto:" (m03), "Uma questão em aberto:" (m04). Os únicos callouts do curso são `[!tip]` e `[!note]`, e os três existentes são **pedidos de ilustração**, não controvérsias.

Manter o callout criaria um segundo dispositivo visual para a mesma função, e — pior — colidiria com o dispositivo que este mesmo módulo acabou de usar para a ilustração da a01 (🔴 1). O leitor aprenderia que "caixa destacada" significa duas coisas diferentes.

**Correção aplicada.** Convertido para a forma corrente do curso, abrindo com "**Pergunta em aberto:**" em prosa. O conteúdo não mudou.

---

## 🟡 2 — a01 e a02 · "preforma de serra" no corpo × "preforma de esfera" no vocabulário

**Onde:** `07-esfera-e-torneadas-aula-01`, seção "Do cubo ao poliedro"; `07-esfera-e-torneadas-aula-02`, "Antes de começar".

A auditoria criou a entrada `preforma de esfera` (*sphere blank*) no vocabulário das duas aulas — corrigindo, de passagem, o "saibro" da a02 —, mas o corpo das duas usava **"preforma de serra"**. Dois nomes para a mesma coisa, um na tabela e outro no texto, na aula que introduz o conceito. LC-01 exige a definição na primeira aparição; a primeira aparição usava um termo que a tabela não definia.

**Correção aplicada.** Corpo da a01 e bullet da a02 alinhados a `preforma de esfera`, com "feita na serra" / "cortada na serra" como aposto — o que preserva a informação de **onde** a etapa acontece, que era o que "de serra" carregava, sem duplicar o termo.

---

## 🟡 3 — a03 · pré-requisito no cabeçalho descrevia a aula 02 pela versão antiga

**Onde:** `07-esfera-e-torneadas-aula-03`, linha `**Pré-requisito:**`.

Dizia "aula 02 deste módulo (convergência por **copos casados**, contato distribuído)". Depois das correções da auditoria, "copos casados" não descreve mais nada da a02. O cabeçalho da a03 anunciava ao leitor um conceito que ele não vai encontrar quando voltar à aula anterior — o sintoma clássico de "pré-requisito declarado e não usado", aqui na forma inversa: declarado com o nome errado.

**Correção aplicada.** "convergência por copos em **cabeçotes de mola**, contato distribuído em **coroa**" — os dois conceitos que a a02 de fato entrega e dos quais a a03 depende.

---

## 🟡 4 — a02 · o exemplo trabalhado ficou paralelo demais ao Conteúdo

**Onde:** `07-esfera-e-torneadas-aula-02`, "Exemplo trabalhado". Encargo 3 da auditoria.

**Avaliado, com ação parcial.** A observação da auditoria procede: depois das correções, os quatro blocos do exemplo (um eixo · dois cabeçotes · três cabeçotes · onde a máquina para) espelham as quatro seções do Conteúdo quase um a um. Ele **não** é um caso novo — é a mesma cadeia instanciada.

Mas a conclusão de que "é resumo, não exemplo" não se sustenta, por três razões. (i) O exemplo instancia com **números concretos** — preforma de cubo de 30 mm, esfera de 25 mm — que o Conteúdo não tem. (ii) Ele carrega uma restrição que **só existe nele**: o teto geométrico ("de um cubo de 30 mm não sai esfera maior que 30 mm"), instalado pela auditoria ao corrigir o erro de raio-por-diâmetro. (iii) Ele é a única passagem da aula em que os três arranjos de máquina são comparados **na mesma peça**, que é justamente o que `oa02` pede ao dizer "justificar a necessidade de eixos múltiplos" — justificar exige contraste controlado, e o Conteúdo apresenta os arranjos em sequência, não em comparação.

O que a auditoria pegou de real é que o exemplo **não força uma decisão**. Isso é uma limitação, não um defeito: a aula é de mecanismo, e `oa02` é de nível "explicar", não "decidir". Uma aula de nível *explicar* pode legitimamente ter um exemplo que instancia em vez de decidir — foi o mesmo critério aplicado na a01 do módulo 06.

**Ação.** Nenhuma reestruturação. A folga da a02 é de 10 palavras, e qualquer caso novo teria de ser financiado cortando mecanismo recém-instalado pela auditoria, que é exatamente o que o encargo proibia. Registrado para o `gerador-de-questionarios`: a questão de aplicação de `oa02` deve pedir a **decisão** que o exemplo não pede — dado um diâmetro-alvo e uma tabela de faixas de copo, qual copo serve e por que o copo não determina o diâmetro final.

---

## 🔵 1 — Verificação corte a corte dos enxugamentos da auditoria (encargo 1)

A auditoria acrescentou material substancial às quatro aulas e financiou tudo cortando redundância, deixando o encargo explícito de verificar se algum corte removeu **conteúdo** em vez de repetição. Verificado, corte a corte, contra a versão pré-auditoria. **Nenhum corte removeu conteúdo.** Detalhe:

**a01 (seis cortes).** (1) Abertura da seção "Do cubo ao poliedro" — a frase removida ("a forma que resulta se aproxima da esfera por etapas") é dita de novo, com números, dois parágrafos abaixo. (2) Fecho do parágrafo do cuboctaedro — "o maior desvio entre a forma e uma esfera inscrita caiu, porque as pontas mais distantes do centro foram removidas" virou "as pontas mais distantes do centro foram removidas", e o desvio passou a ser dado **numericamente** na frase seguinte, o que é mais forte, não mais fraco. (3) Fecho da seção de propagação de erro — "porque cada etapa posterior assume que o centro está certo e continua removendo material em torno dele" aparece íntegro em "Erros comuns" e no Recap. (4) Fecho do exemplo trabalhado — a frase sobre a esfera ser o exame mais severo de simetria foi removida **aqui** porque já fecha a primeira seção da aula, quarenta linhas acima. (5) e (6) Primeiro parágrafo e "Erros comuns" 1 — compressão de sintaxe, sem perda de proposição.

**a02 (dois cortes).** (1) O exemplo trabalhado encolheu ~40% — mas só depois que o Conteúdo passou a carregar o mecanismo dos polos e da mola, que antes não estavam em lugar nenhum. O exemplo perdeu explicação e manteve instanciação, que é a divisão de trabalho correta entre as duas seções. (2) Uma frase sobre troca de copo mudar a granulometria foi removida — era acréscimo da própria auditoria, não sustentado por nenhum achado, e a aula não a promete em lugar nenhum.

**a03 (três cortes).** (1) Seção de abertura, comprimida de ~135 para ~90 palavras: o que saiu foi a enumeração de exemplos de material heterogêneo, que reaparece completa dois parágrafos abaixo com o mecanismo junto. (2) A seção de diagnóstico foi de ~150 para ~110 — o que saiu foi a repetição da causa raiz, que o corpo já estabelecera nas duas seções anteriores. (3) A explicação dos dois centros perdeu a paráfrase ("um imposto pela máquina, outro herdado da geologia") e ganhou a formulação direta ("Numa esfera há **dois centros**"), que é mais curta e mais nomeável.

**a04 (dois cortes estruturais).** (1) A seção "O que continua igual, e o que muda" foi **fundida** na seção nova "Duas exigências diferentes". Confirmado que nada se perdeu: a exigência de centro migrou para o fim da primeira seção e a variação de raio ao longo do eixo migrou para dentro da definição de sólido de revolução estrito, onde na verdade explica melhor (é ali que ela distingue esfera de ovo **dentro** do mesmo conjunto). (2) "A fronteira com a escultura livre" foi de ~205 para ~130 palavras, porque o teste em duas perguntas substituiu duas exposições sucessivas do mesmo critério. Único conteúdo removido: a frase "produzida numa máquina de eixo único, como as descritas neste módulo", que sobrevive no Recap.

**Uma perda avaliada e aceita.** A a01 já não diz "no limite matemático, ninguém chega a esse limite por corte discreto na bancada". A informação sobrevive transformada — a aula agora diz **onde o corte discreto para** (a preforma) e **o que assume dali em diante** (a abrasão contínua), que é mais informativo que a negação anterior.

---

## 🔵 2 — a04 · carga de conceitos (encargo 2)

**Avaliado, mantido, com justificativa.** A a04 é de longe a aula mais densa do módulo depois da auditoria: dois critérios aninhados, um teste de duas perguntas, três formas, duas tradições de proporção do obelisco e a distinção gota × briolette. Contados como ideias independentes, seriam sete ou oito — acima do limite de 3 a 4 que a skill usa.

**Não são independentes, e é isso que a salva.** A estrutura efetiva é: **um** critério com dois níveis (`estrito ⊂ eixo único`), **um** procedimento que o aplica (o teste em duas perguntas), e **três instâncias** que são as três respostas possíveis do procedimento — ovo (sim/sim), obelisco (sim/não), escultura livre (não). A gota × briolette é a **quarta** instância e serve de caso de teste do critério dentro de um mesmo par de formas parecidas. As duas faixas de proporção do obelisco são um dado sob LC-05, não um conceito.

É o mesmo padrão que a revisão do módulo 06 aceitou na a05 daquele módulo: conceitos **contrastivos** instanciando um gabarito único, não conceitos somativos. E o gabarito aqui é ainda mais forte, porque o teste em duas perguntas é literalmente um algoritmo que o aluno executa, e o exemplo trabalhado o executa nas três peças, na mesma ordem, com a mesma redação. A fórmula `estrito ⊂ eixo único` funciona como organizador prévio de uma linha.

**Nada dividido, nada encaminhado.** Com a correção do 🟠 2, o único termo que faltava para fechar o gabarito ("forma torneada" = o conjunto largo) entrou.

---

## 🔵 3 — LC-08 e a posição da preforma (encargo 4)

**Uma controvérsia basta para este módulo.** A auditoria instalou a pergunta aberta sobre a causa do socavamento entre bandas de ágata (a03), e ela é boa por três motivos: é genuína (as fontes divergem de fato), é **central** — está no coração de `oa03`, não numa margem — e ensina uma distinção epistemológica útil, a de que duas hipóteses podem prever o mesmo observável e mesmo assim não serem a mesma coisa.

A candidata que a auditoria sugeriu para uma segunda — quantas faces vale a pena tirar na serra antes de passar à máquina — foi avaliada e **descartada**. Ela é uma decisão de eficiência de oficina, não uma divergência sobre um fato, e o curso é teórico: transformá-la em controvérsia declarada seria encenação, e ainda por cima em terreno de bancada. Mesma decisão e mesmo raciocínio da revisão do módulo 06.

Nota de escrituração: o módulo 07 sai com **uma** controvérsia declarada, contra quatro do módulo 04, uma do 05 e uma do 06.

---

## Progressão

**LIMPA.** A cadeia a01 (por que converge) → a02 (como a máquina realiza) → a03 (o que o material faz com isso) → a04 (o que muda quando o alvo não é esférico) é estritamente crescente. Cada aula declara no cabeçalho o que a anterior entregou, e nenhuma usa resultado de aula posterior — todas as remissões para frente são negativas, no bloco "O que não concluir".

**Nenhum salto de pré-requisito.** Verificado termo a termo: `sólido de revolução` (a01, definido), `preforma de esfera` (a01, definido, reusado em a02), `polo` (a02, definido uma frase antes do uso), `coroa de contato` (a02, definido no ato), `heterogeneidade de resistência à abrasão` (a03, definida e ancorada no módulo 02), `sólido de revolução estrito` e `forma de eixo único` (a04, definidos no ato), `briolette` (a04, definida no ato).

**O encadeamento ficou melhor depois da auditoria, não pior.** Três amarrações novas que não existiam:
- a01 → a02: a preforma de serra, que antes era negada como "modelo pedagógico", virou a etapa que a a02 herda.
- a02 → a04: o argumento dos polos, que na a02 explica por que um eixo **não basta** para a esfera, reaparece na a04 explicando por que um eixo é **exatamente o que se quer** quando o alvo tem polos. A mesma proposição servindo a duas conclusões opostas é o tipo de amarração que material autodidata quase nunca tem.
- a02 → a03: o "contato em coroa" da a02 é o que torna a suposição de uniformidade da a03 enunciável.

**Pré-requisito externo do curso de Gemologia** citado por nome na a03 (dureza de Mohs da turquesa), nunca por wikilink.

---

## Cobertura de objetivos

| Objetivo | Nível declarado | Ensinado em | Exemplo | Recap | Atingido no nível? |
|---|---|---|---|---|---|
| `lapidacao-m07-oa01` — explicar por que o desbaste sucessivo converge e por que a esfera expõe erro de simetria | explicar | a01, três seções | sim, com números | sim | **sim** — e agora com a figura que o contrato exigia |
| `lapidacao-m07-oa02` — descrever o princípio da máquina e justificar eixos múltiplos | explicar | a02, quatro seções | sim, três arranjos na mesma peça | sim | **sim** |
| `lapidacao-m07-oa03` — prever os defeitos da heterogeneidade, incluindo undercut e bandeamento | analisar | a03, quatro seções | sim, duas esferas contrastadas | sim | **sim** — o "prever" é exercido porque o exemplo pede diagnóstico, não reconhecimento |
| `lapidacao-m07-oa04` — relacionar eixo e proporção e distinguir da escultura livre | analisar | a04, quatro seções | sim, três peças pelo mesmo teste | sim | **sim**, depois do 🟠 2 |

Um objetivo por aula, quatro objetivos, quatro aulas. **Nenhuma célula vazia.** Os quatro verbos são de conhecimento observável — explicar, descrever, prever, relacionar; nenhum "entender/conhecer/saber" e nenhum verbo de execução. Nenhum conteúdo órfão: todas as seções das quatro aulas servem ao objetivo declarado da sua aula.

**Uma observação sobre `oa03`.** O verbo é *prever*, nível analisar, e antes da auditoria o exemplo não o exercia de verdade — a Esfera B era resolvida por reconhecimento de material ("é ágata, logo não é undercut"). Depois da correção do 🔴 3 da auditoria, o exemplo exige aplicar um critério (o relevo) a dois casos que **não** se distinguem pelo material. O objetivo passou a ser atingido no nível declarado por efeito da auditoria, não desta revisão — registrado porque é o mesmo tipo de ganho que o 🟠 1 da revisão do módulo 06 teve de produzir à mão.

---

## Desalinhamento aula–avaliação

**NÃO VERIFICÁVEL nesta etapa** — o questionário do módulo 07 ainda não existe. Registrado para o `gerador-de-questionarios`:

1. **`oa02` exige uma questão de decisão, não de descrição.** Ver 🟡 4: o exemplo trabalhado da a02 instancia mas não decide. A questão de aplicação deve fechar essa lacuna — dado um diâmetro-alvo e as faixas de trabalho dos copos, qual copo serve, e por que o copo escolhido **não** determina o diâmetro final.

2. **`oa03` exige um caso em que o material não decide.** A questão tem de apresentar duas esferas do **mesmo** material (ágata, de preferência) com defeitos diferentes, e pedir o diagnóstico pelo relevo. Uma questão do tipo "é ágata, logo o defeito é X" reintroduz exatamente o erro que o 🔴 3 da auditoria corrigiu.

3. **`oa04` exige o obelisco ou a briolette como caso.** Uma questão que só use esfera e ovo testa o critério estrito e deixa passar quem não entendeu a inclusão `estrito ⊂ eixo único` — que é o coração da aula.

4. **Armadilhas legítimas vindas da auditoria, todas boas como distratores:** o copo **não** fixa o diâmetro final, define uma faixa (a02); um eixo único **não** obriga a um cilindro — a calha decide o perfil (a02); as máquinas comerciais são de **duas e três** cabeças, não "3 a 6" (a02); ágata **socava**, sim (a03); na turquesa, quem afunda depende da matriz (a03); o obelisco **não** é sólido de revolução estrito (a04); *briolette* **não** é sinônimo de gota (a04); as duas faixas de proporção do obelisco são de tradições diferentes (a04).

5. **Não cobrar tolerância de esfericidade em número.** A auditoria removeu a afirmação por falta de fonte (🔵 1 da auditoria). Cobrar o **método** — paquímetro em várias direções, maior menos menor — é legítimo; cobrar um valor não é.

6. **Não cobrar o mecanismo antigo dos polos.** "Velocidade linear menor perto do centro" era o mecanismo errado e foi corrigido; se aparecer como alternativa, tem de ser distrator, nunca gabarito.

---

## O que está bem feito

- **A a03 tem o melhor argumento do módulo**, e ele sobreviveu intacto à correção do seu próprio 🔴: a ideia de que uma esfera tem **dois centros** — um imposto pela máquina, um herdado da geologia da pedra — e que a leitura do bruto do módulo 05 existe para aproximá-los. É uma amarração cross-módulo genuína, não decorativa.
- **A reciprocidade a02 ↔ a04.** "Um eixo não basta" e "um eixo é o que se quer" são a mesma proposição lida de dois lados, e a a04 diz isso explicitamente. Instalada pela auditoria, mas vale preservar em qualquer revisão futura.
- **O bloco "O que não concluir" das quatro aulas** faz o trabalho pesado de conter o escopo teórico do curso, e faz sem soar defensivo. A a01 chegou a usá-lo para declarar uma **lacuna de fonte** ("não concluir qual é a tolerância…"), que é um uso novo e bom do bloco.
- **A a04 fechou um critério que estava quebrado sem inflar.** Saiu com 1596 palavras ensinando dois critérios onde antes ensinava um errado com 1589.

---

## Não executado, por escopo

- **módulo NÃO marcado como concluído** — `modules[07].status` permanece `pending`; fecha depois do questionário.
- **validador-estrutural NÃO rodado** — é da geo-operacional.
- **`_curso.md` NÃO reconciliado** — é da geo-operacional.
- **questionário NÃO existe** — é a etapa 3. Flashcards não se aplicam (dispensados a partir do módulo 06).
- **hub `07-esfera-e-torneadas-modulo.md` NÃO tocado nesta etapa** — o callout de pipeline ali é genérico (descreve o gate, não afirma o estado da auditoria) e portanto não passou a dizer nada falso; a reconciliação do hub fica com a geo-operacional.
- **Nenhum questionário ou flashcard alterado** — a skill não os toca; desalinhamento é reportado, não corrigido aqui.

---

## Régua de `palavras_corpo`

A mesma de `_contexto.md` (2026-09-02): de `## Conteúdo` ao fim de `## Recap relâmpago` inclusive, `len(texto.split())`. A contagem reproduziu **exatamente** os quatro valores declarados pela auditoria antes desta revisão (1592/1589/1590/1594), o que revalida a régua pela quinta vez. Rodapé ressincronizado nas quatro aulas.

**Um registro para o `_contexto.md`, se ele for reaberto:** a a01 entrou nesta etapa 2 **acima** do teto, com 1604 palavras — o único caso do curso depois do módulo 01. Saiu em 1594, sem perda de conteúdo (ver 🔵 1) e com a ilustração do contrato instalada. A folga do "~" não precisou ser invocada.
