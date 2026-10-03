# Revisão didática — Módulo 22: Modelagem geológica 3D

**Revisado em:** 2026-09-19 · **Modo:** `review-and-fix`
**Material:** as 5 aulas do módulo (hoje 6, após a divisão descrita abaixo), mais o hub
**Rodou depois da auditoria científica** de 2026-09-19 (`22-modelagem-geologica-3d-auditoria.md`), como manda a ordem do plugin — e isso importou: a auditoria acrescentou ~1.200 palavras ao módulo, e foi esse acréscimo que empurrou a Aula 04 acima do teto de 30 min.

**Veredito:** **bem ensinado com ressalvas** — as ressalvas foram aplicadas.

## Resumo

🔴 1 bloqueia · 🟠 3 prejudicam · 🟡 3 atrito · 🔵 3 sugestões

**Carga por aula, medida depois das correções da auditoria e antes desta revisão** (contagem de "## Conteúdo" até "## Fontes", incluindo exemplo trabalhado e recap):

| Aula | Palavras | Seções | Duração declarada | Situação |
|---|---|---|---|---|
| a01 | 2.396 | 5 | ~27 min | dentro |
| a02 | 2.429 | 4 | ~29 min | no teto |
| a03 | 2.402 | 5 | ~28 min | no teto |
| **a04** | **2.764** | **7** | ~28 min declarado, **~33 min real** | **acima do teto** |
| a05 | 2.424 | 5 | ~29 min | dentro |

Para calibrar: a aula mais pesada do Módulo 20 tem 2.603 palavras e a mais pesada do Módulo 21, 2.535 — as duas aceitas. A antiga a04, com 2.764 palavras e **sete** seções, era a aula mais pesada dos três módulos e a única com sete seções.

---

## Achados

### 🔴 1. Sobrecarga da Aula 04: duas aulas dentro de uma, com sete seções e ~33 min

**claim_id:** `DID-M22-A04-CARGA-001`
**Tipo:** excesso de conceitos novos / carga cognitiva
**Onde:** antiga Aula 04, "Tipos, tamanhos e geometrias de depósitos minerais e a aplicação de modelos 3D em metalogênese"
**Problema:** a aula fazia **duas coisas diferentes**, e o próprio objetivo de aprendizagem `oa03` já denunciava isso ao ser formulado com um "e" no meio: *"Relacionar o tipo, o tamanho e a geometria de depósitos minerais à estratégia de modelagem **e** à interpretação metalogenética"*. A primeira metade é uma **taxonomia** — quatro famílias geométricas, cada uma com seus exemplos, sua geometria e sua estratégia favorecida —, cuja carga é de memorização estruturada. A segunda metade é um **argumento epistemológico** sobre como um modelo geométrico serve de teste a uma hipótese genética; a carga é de raciocínio, não de memória. São modos de pensar distintos, e empilhá-los na mesma sessão de 30 minutos faz o leitor chegar na segunda metade já saturado pela primeira.

Três agravantes: (a) o exemplo trabalhado único, no fim, exercitava **apenas** a primeira metade (escolha de estratégia para o Alvo A e o Alvo B) — a segunda metade, mais abstrata, ficava sem nenhuma prática; (b) a aula tinha **sete** seções, contra 4-5 das demais; (c) a auditoria científica acrescentou três blocos densos e necessários a ela (a ressalva do zoneamento de alteração, a distinção estratiforme/estratabound e a exclusão dos recifes de EGP), levando-a de ~2.200 para 2.764 palavras.
**Correção aplicada — divisão em Parte 1 / Parte 2**, seguindo a convenção já usada nos Módulos 17, 19, 20 e 21:

- **Nova Aula 04** — *"Tipos, tamanhos e geometrias de depósitos minerais e a estratégia de modelagem"* (2.574 palavras na mesma contagem da tabela acima, ~27 min, 6 seções). Fica com as quatro famílias geométricas, a síntese e a tabela, e **herda o exemplo trabalhado original** (Alvo A / Alvo B), que é exatamente sobre escolha de estratégia.
- **Nova Aula 05** — *"O modelo 3D como ferramenta de teste da interpretação metalogenética"* (1.786 palavras, ~20 min, 4 seções). Fica com a seção metalogenética, preservada integralmente, e recebe **exemplo trabalhado novo**.

> **Nota de honestidade sobre a contagem.** A Aula 04 saiu da divisão com 2.574 palavras, e não com as ~1.950 que a subtração pura sugeriria: o achado 🟡 7 abaixo acrescentou a ela o fio condutor explícito (pergunta organizadora, fecho por família, coluna nova na tabela). Ela está **dentro** do teto de 30 min, mas perto dele — a divisão resolveu o problema dos dois modos de pensar empilhados, que era o defeito grave, e reduziu a carga menos do que reduziu a heterogeneidade. As durações declaradas nos cabeçalhos das duas aulas foram ajustadas para refletir a contagem real (~27 e ~20 min), e não a estimativa inicial.
- A antiga Aula 05 (estudos de caso e incerteza) foi renumerada para **Aula 06**, com o arquivo renomeado e o ID atualizado de `geologia-avancado-m22-a05` para `geologia-avancado-m22-a06`.

**Nenhuma correção da auditoria científica foi desfeita, diluída ou reformulada** — ver "Preservação da auditoria" abaixo.
**Ganho colateral:** o mapeamento objetivo × aula, que a auditoria registrara como observação (nenhum objetivo com correspondência 1:1), ficou mais limpo: `oa03` passou a ter duas aulas dedicadas, uma para cada metade do seu enunciado.
**Escopo:** exigiu dividir a aula.

### 🟠 2. Parte 2 herdava a abstração sem o andaime: sistema mineral não reativado, argumento central implícito, nenhuma prática

**claim_id:** `DID-M22-A05-ANDAIME-002`
**Tipo:** pré-requisito não reativado + abstração antes do concreto + exemplo ausente
**Onde:** seção "Modelo 3D como ferramenta de teste da interpretação metalogenética" da aula original, que se tornou a Aula 05
**Problema:** isolada como aula própria, a seção mostrou três lacunas que passavam despercebidas quando ela era o apêndice de outra aula:

1. **O pré-requisito não era reativado.** A seção dizia "organizada, como o Módulo 19 (Aula 01) já apresentou, nos quatro componentes de um sistema mineral: fonte, transporte, deposição e preservação" — e seguia em frente. Citar os quatro nomes numa oração subordinada não é reativar um pré-requisito de um módulo inteiro atrás; o leitor precisa dos quatro componentes **ativos** para acompanhar os três testes, porque cada teste incide sobre um deles.
2. **O argumento central estava implícito.** A seção afirmava que o modelo "força a geometria interpretada a ser espacialmente consistente e verificável, em vez de permanecer como uma narrativa qualitativa" — uma frase que **enuncia a conclusão sem expor o raciocínio**. Por que geometria é mais testável que narrativa? O texto não dizia.
3. **Nenhum exemplo.** Três testes abstratos, um atrás do outro, sem um caso em que o leitor visse o teste acontecer.

**Correção aplicada:** a Aula 05 recebeu três blocos, **nenhum deles factual novo**: (i) a seção "De produto descritivo a instrumento de teste", que reativa os quatro componentes do sistema mineral com uma linha de conteúdo para cada um; (ii) a seção "Por que a geometria torna a hipótese testável", que explicita o argumento que o texto original usava sem enunciar — narrativa qualitativa tolera vaguidão, geometria não, e por isso o modelo "não prova a interpretação; cria condições para que ela falhe"; (iii) um exemplo trabalhado novo, construído **apenas sobre o Alvo A já usado na Aula 04**, em que o leitor aplica os três testes e precisa dizer o que contaria como evidência contra a hipótese.
**Escopo:** correção local dentro da aula nova.

### 🟠 3. Salto de pré-requisito remanescente: "cokrigagem universal" introduzida sem o sentido de "universal"

**claim_id:** `DID-M22-A02-UNIVERSAL-003`
**Tipo:** termo técnico usado antes de definido
**Onde:** a02, seção "A ligação com a geoestatística" e Recap
**Problema:** a auditoria científica corrigiu, com razão, o salto maior (a aula declarava a cokrigagem como pré-requisito do Módulo 20, que a põe fora de escopo) e inseriu a definição de cokrigagem. Mas a mesma correção **precisou** o método como "cokrigagem **universal**" — e introduziu, com isso, um segundo termo não explicado, inclusive no Recap. Um leitor que acabou de receber a definição de "cokrigagem" na frase anterior encontra um adjetivo técnico colado nela e não tem como saber se ele é decorativo ou carrega informação.
**Correção aplicada:** acrescentada uma glosa de duas orações, ancorada no que o curso **de fato já ensinou**: o Módulo 20, Aula 02, registra a **deriva** (*drift*) e nomeia a **krigagem universal** como o caminho formal para tratá-la. A glosa remete a esse ponto e fecha explicando por que a formulação universal não é um refinamento opcional no campo potencial — o potencial é uma variável cujo valor absoluto não tem significado, só os incrementos têm.
**Escopo:** correção local.

### 🟠 4. Propagação incompleta da auditoria: o zoneamento concêntrico sobreviveu na seção metalogenética

**claim_id:** `DID-M22-A05-ZONEAMENTORESIDUAL-004`
**Tipo:** inconsistência interna entre seções da mesma aula
**Onde:** terceiro teste da seção metalogenética (hoje Aula 05)
**Problema:** achado **encontrado por esta revisão e encaminhado de volta à auditoria como propagação faltante**, não como achado didático novo. A auditoria científica corrigiu, no achado `GEOMOD3D-M22-A04-ZONEAMENTOPORFIRO-005`, a descrição do zoneamento de alteração de pórfiros (de anéis concêntricos em planta para sequência empilhada verticalmente). A correção foi aplicada na seção sobre pórfiros, no Recap e na tabela — mas a seção metalogenética, no fim da mesma aula, continuava dizendo *"o zoneamento **concêntrico** de alteração hidrotermal num pórfiro, discutido acima"* e *"resfriamento e queda de pressão **radialmente** decrescentes a partir de um corpo intrusivo central"*. A mesma aula afirmava as duas coisas, em seções diferentes.
**Correção aplicada:** trecho reescrito na Aula 05 para descrever o zoneamento como predominantemente vertical, empilhado de baixo para cima com a propilítica distal, e para apresentar essa disposição como assinatura de um mecanismo de deposição governado pela **evolução vertical do fluido ao subir e resfriar**, não por afastamento radial. Registrado no bloco `nota_divisao_didatica` da Aula 05 e reportado ao relatório de auditoria.
**Escopo:** correção local. **Fato novo introduzido: nenhum** — a formulação corrigida é a que a auditoria já havia verificado contra Sillitoe (2010) e aplicado na Aula 04.

### 🟡 5. Termo `strings` usado sem definição na primeira ocorrência do módulo

**claim_id:** `DID-M22-A01-STRINGS-005`
**Tipo:** termo técnico usado antes de definido
**Onde:** a01, seção "Modelagem explícita e modelagem implícita: a distinção de alto nível"
**Problema:** *"digitaliza contatos como *strings*, e o software conecta essas *strings* numa superfície triangulada"*. O termo aparece duas vezes na mesma frase, em itálico (sinalizando que é jargão), e nunca é explicado. Ele reaparece na a02 e na a03, sempre pressuposto. É um termo de software de mineração cujo sentido não é adivinhável a partir do português nem do inglês comum — "string" sugere qualquer coisa menos uma polilinha.
**Correção aplicada:** aposto inserido na primeira ocorrência: *"o nome que os softwares de mineração dão a uma polilinha desenhada sobre uma seção, isto é, a sequência de pontos que traça um contato naquele corte"*.
**Escopo:** correção local.

### 🟡 6. Termo `rejeito` perdeu a glosa na reescrita da auditoria

**claim_id:** `DID-M22-A03-REJEITO-006`
**Tipo:** termo técnico usado antes de definido (regressão introduzida por correção anterior)
**Onde:** a03, seção sobre tratamento de falhas
**Problema:** o texto original glosava o termo na primeira ocorrência — *"com um deslocamento (rejeito) aplicado"*. A reescrita da auditoria (achado 🟠 5) removeu essa frase por estar factualmente errada, e o termo sobreviveu na frase seguinte, agora **sem** a glosa: *"não é aplicado como um parâmetro de rejeito"*. Regressão clássica de correção cirúrgica: o trecho removido carregava a definição de um termo que o trecho mantido ainda usa.
**Correção aplicada:** glosa restaurada em aposto — *"a medida do deslocamento relativo de dois blocos ao longo de uma falha"*.
**Escopo:** correção local.

### 🟡 7. Aula 04 sem fio condutor explícito entre as quatro famílias

**claim_id:** `DID-M22-A04-FIOCONDUTOR-007`
**Tipo:** estrutura — critério unificador revelado só no fim
**Onde:** nova a04
**Problema:** as quatro famílias geométricas eram apresentadas em sequência e o critério que as unifica — **a natureza física do limite entre minério e encaixante** — só aparecia na seção de síntese, depois da tabela. Quem lê linearmente percorre quatro blocos aparentemente independentes, cada um com seus nomes de depósito, e só no fim descobre que havia uma pergunta única organizando tudo. Isso transforma em memorização de lista o que deveria ser aplicação de um critério.
**Correção aplicada:** (i) a pergunta organizadora foi **antecipada** para o fim da primeira seção, como instrução de leitura; (ii) cada uma das quatro famílias fecha agora com uma linha em itálico "*Limite entre minério e encaixante:*", que responde a pergunta naquele caso; (iii) a tabela de síntese ganhou uma **coluna** com esse critério, entre os exemplos e a estratégia; (iv) a síntese ganhou um parágrafo mostrando que a coluna do limite prevê a estratégia melhor do que a classe genética prevê; e (v) a resolução do exemplo trabalhado passou a apontar que a justificativa passou por essa coluna, e não pela gênese.
**Escopo:** correção local.

### 🔵 8. Nenhuma aula do módulo tem exemplo trabalhado quantitativo

**claim_id:** `DID-M22-MODULO-SEMARITMETICA-008`
**Tipo:** sugestão — prática ausente
**Onde:** módulo inteiro
**Observação:** os seis exemplos trabalhados do módulo são todos de classificação, escolha de estratégia ou crítica de modelo. Nenhum pede manipulação numérica. É coerente com a natureza do módulo — modelagem 3D em nível conceitual é qualitativa —, e o único ponto genuinamente quantitativo (a equivalência do campo potencial com cokrigagem) não se resolve com aritmética de guardanapo. Mas destoa dos Módulos 20 e 21, que treinam o leitor em manipulação, e a transição pode dar a impressão de que o módulo "afrouxou".
**Não corrigido, deliberadamente:** um exercício quantitativo aqui exigiria fabricar dados de campo potencial ou de covariância que não passaram pelo auditor. A skill proíbe introduzir conteúdo factual não verificado, e a regra vale mesmo quando o conteúdo é um exemplo numérico plausível. **Encaminhado ao gerador de questionários**, que pode construir uma questão de aplicação quantitativa a partir do vocabulário já auditado sem precisar inseri-la na aula.

### 🔵 9. A Aula 01 lista onze softwares sem apoio de retenção

**claim_id:** `DID-M22-A01-LISTASOFTWARE-009`
**Tipo:** sugestão — densidade de nomes próprios
**Onde:** a01, "Panorama de softwares comerciais e livres"
**Observação:** onze produtos, com fornecedor, país e histórico corporativo, em três blocos. É a seção com maior densidade de nomes próprios do módulo e a de menor valor conceitual — e é também a que envelhece mais rápido, como a auditoria mostrou ao encontrar dois achados aqui (o fornecedor do SKUA-GOCAD e a data do GOCAD). A aula acerta ao fechar a seção com o critério de escolha, que é o que de fato precisa ser retido.
**Não corrigido:** o objetivo declarado da aula inclui explicitamente "identificar os principais softwares comerciais e livres do mercado", então a lista está cumprindo um objetivo, não sobrando. **Encaminhado ao gerador de flashcards** com a recomendação de **não** gerar cards de "qual empresa é dona de qual software": é o conteúdo mais perecível do módulo e o de menor valor de aprendizagem. Cards sobre **que tipo de fluxo cada pacote privilegia** (implícito/RBF, explícito por seção, reservatório) são úteis; cards sobre propriedade corporativa não são.

### 🔵 10. Aulas 02 e 03 permanecem no teto de 30 min

**claim_id:** `DID-M22-A0203-TETO-010`
**Tipo:** sugestão — margem de carga
**Onde:** a02 (2.429 palavras após esta revisão, ~30 min) e a03 (2.402, ~30 min)
**Observação:** as duas ficaram no teto do plugin depois dos acréscimos da auditoria, e a a02 tem a maior densidade conceitual do módulo — oito conceitos independentes (dado de interface, dado de orientação, campo potencial/isosuperfície, gradiente como restrição, cokrigagem, RBF, DSI, referencial de dobra). **Não foram divididas**, por decisão deliberada: dividir três das cinco aulas originais transformaria um módulo de cinco aulas em oito e fragmentaria uma progressão que funciona. As duas estão **no** teto, não acima dele, e diferentemente da a04 não empacotam dois modos de pensar distintos — a a02 é uma sequência única (que dado entra → como o algoritmo o usa → como as abordagens se comparam).
**Recomendação para quem retomar o módulo:** se a a02 receber qualquer acréscimo futuro, ela passa a ser a próxima candidata a divisão, com corte natural já visível — dados de entrada e fluxo explícito na Parte 1; campo potencial, cokrigagem e comparação das abordagens na Parte 2.

---

## Preservação da auditoria científica

A divisão da Aula 04 aconteceu **depois** da auditoria e tocou exatamente os parágrafos que ela tinha corrigido. Registro explícito do que foi preservado, para que uma verificação futura não precise reabrir o diff:

| Achado da auditoria | Onde está hoje | Estado |
|---|---|---|
| 🔴 1 `-GEOMETRIAESTRATIFORME-003` (MVT é estratabound) | Aula 04, seção "Depósitos estratiformes e estratabound" + tabela + recap | preservado, texto idêntico |
| 🟠 2 `-GEOMETRIAPORFIRO-002` (alongamento vertical, sem "funil invertido") | Aula 04, seção "Depósitos disseminados e em stockwork" + tabela + recap + exemplo trabalhado | preservado, texto idêntico |
| 🟠 3 `-ZONEAMENTOPORFIRO-005` (zoneamento vertical, Lowell e Guilbert como histórico) | Aula 04, ressalva nomeada + recap + fontes — **e agora também na Aula 05**, onde a propagação estava faltando (ver 🟠 4 acima) | preservado **e estendido** |
| 🟠 4 `-NICUEGPGEOMETRIA-006` (recifes de EGP fora da família pipe) | Aula 04, seção "Depósitos maciços e em pipe" + tabela + recap | preservado, texto idêntico |
| 🟠 6 `-PREREQCOKRIGAGEM-005` (cokrigagem definida no texto) | Aula 02 — **e reforçado** pela glosa de "universal" (ver 🟠 3 acima) | preservado **e estendido** |
| 🟡 9, 10, 12 (SKUA-GOCAD/AspenTech, GOCAD 1989, Mallet 1992) | Aula 01, corpo + fontes + alegações | preservado, texto idêntico |
| 🟡 7, 8, 11, 13 e 🟠 5 (Calcagno, Laurent, fold frame, grafia, famílias de falha) | Aulas 02 e 03 | preservado, texto idêntico |

**`claim_id` não foram renumerados.** As alegações `GEOMOD3D-M22-A04-*` hoje se distribuem entre as Aulas 04 (`-001`, `-002`, `-003`, `-005`, `-006`) e 05 (`-004`); as `GEOMOD3D-M22-A05-*` emitidas pela auditoria estão hoje na Aula 06. Cada aula carrega essa explicação num bloco `nota_divisao_didatica` ou `nota_renumeracao_didatica` no seu rodapé de metadados, e o hub repete o aviso.

**Uma alegação nova** foi emitida pela Aula 05 ao explicitar o argumento do achado 🟠 2 desta revisão: `GEOMOD3D-M22-A05-ASSIMETRIATESTE-007`, sobre a assimetria lógica dos três testes metalogenéticos. Está declarada com `risk: interpretacao` e com a fonte descrita como síntese didática apoiada em McCuaig & Hronsky (2014) — **não** como medida ou classificação formal.

> **PENDÊNCIA FECHADA em 2026-09-19.** Este claim foi auditado numa **passagem pontual** do auditor científico, de escopo restrito a ele (a auditoria do módulo não foi reaberta). **Núcleo verificado** — achado azul **B22**: a assimetria entre refutação e corroboração é real e ancorada em Wei, Yin, Bonner & Caers (2026), *Surveys in Geophysics* 47, 289-315. Duas correções foram aplicadas na aula: 🟠 **14** (`-ASSIMETRIAUNIFORME-010`, a assimetria não é uniforme — o teste 2 é previsão arriscada, e o texto contradizia o próprio corpo da aula) e 🟡 **15** (`-ATRIBUICAOA03-011`, a justificativa estava creditada à Aula 03, que argumenta outra coisa). O `risk` foi **mantido** como `interpretacao`, deliberadamente. Ver `22-modelagem-geologica-3d-auditoria.md`, achados 14 e 15 e azul B22.

---

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo trabalhado | Avaliado em |
|---|---|---|---|
| `oa01` — explícito × implícito, vantagens, limitações, algoritmos | a01 (seções 1, 3, 4, 5) + a02 (seções 2, 3, 4) | sim, nas duas | questionário pendente |
| `oa02` — integrar dado 2D/3D com atributos estruturais, geoquímicos e geofísicos | a02 (seção 1) + a03 (seções 1, 2, 3) | sim, nas duas | questionário pendente |
| `oa03` — geometria de depósito → estratégia de modelagem **e** interpretação metalogenética | **a04** (primeira metade do objetivo) + **a05** (segunda metade) | sim, um em cada | questionário pendente |
| `oa04` — incerteza do modelo 3D e coerência geológico-geofísica | a03 (seções 4, 5) + a06 (seções 1, 2, 4, 5) | sim, nas duas | questionário pendente |

Nenhum objetivo ficou descoberto e nenhuma seção ficou órfã. O `oa03`, que antes era servido por uma aula sobrecarregada, passou a ter uma aula por metade do seu enunciado — a melhoria estrutural mais relevante desta revisão.

**Nota ao gerador de questionários:** nenhum objetivo tem correspondência 1:1 com uma única aula. Todo item de avaliação precisa ser escrito sabendo de qual **par** de aulas ele extrai, e os objetivos `oa01`, `oa02` e `oa04` pedem pelo menos uma questão que cruze as duas aulas que os servem.

---

## O que está bem feito

Vale registrar, porque precisa sobreviver às próximas revisões:

- **O fio condutor crítico do módulo é excelente e raro.** O módulo ensina uma técnica e, ao mesmo tempo, ensina a desconfiar dela — a "falsa sensação de certeza" é anunciada na Aula 01, reaparece como suavidade do campo potencial na Aula 02, como erro de forçar coincidência com a inversão na Aula 03, e vira o vocabulário sistemático da Aula 06. Poucos materiais técnicos fazem isso, e nenhum faz por acidente.
- **O exemplo trabalhado da Aula 06** — "liste três perguntas que um revisor técnico deveria fazer antes de aceitar este modelo" — é o melhor do módulo. Ele não testa recuperação; testa se o leitor adquiriu um **hábito de crítica**, que é exatamente o que a aula se propôs a ensinar.
- **Os dois alvos (A e B) atravessam três aulas** — introduzidos na 04, retomados na 05 e usados como estudos de caso na 06. É um recurso de continuidade barato e eficaz, que poupa o leitor de reconstruir contexto a cada aula, e a divisão da Aula 04 foi feita preservando-o.
- **O exemplo trabalhado da Aula 03** (a discrepância de 15 m entre modelo geológico e modelo de inversão) resolve, num caso concreto, exatamente a armadilha conceitual que o hub do módulo anuncia como sua dificuldade central. Exemplo e dificuldade declarada coincidem, o que é menos comum do que deveria.
- **As referências cruzadas para os Módulos 19, 20 e 21 são densas e, com uma exceção já corrigida, precisas.** O módulo se comporta como parte de um curso, não como texto avulso.
