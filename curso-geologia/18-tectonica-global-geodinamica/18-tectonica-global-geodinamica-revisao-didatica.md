# Revisão didática: Módulo 18 — Tectônica global e geodinâmica

**Revisado em:** 2026-08-18 · **Modo:** review-and-fix
**Material:** seis aulas do M18, questionário final cumulativo e baralho de flashcards (`.md`, `-basic.csv`, `-cloze.csv`)
**Veredito da primeira passagem:** Requer revisão
**Veredito final:** Bem ensinado com ressalvas

## Resumo

**Primeira passagem:** 🔴 0 bloqueiam · 🟠 3 prejudicam · 🟡 5 atrito · 🔵 2 sugestões
**Após as correções:** 🔴 0 bloqueiam · 🟠 1 prejudica (não corrigível nesta skill) · 🟡 0 atrito · 🔵 2 sugestões

**Carga estimada:** 41 termos únicos nos blocos de vocabulário; 1 exemplo trabalhado por aula, todos com 3 passos encadeados; 6 aulas declaradas de 26–28 min. Corpo por aula após as correções: 1.359 · 1.179 · 1.115 · 1.237 · 1.102 · 1.450 (total 7.442). **As seis aulas ficam dentro do teto de 1.600 palavras do LC-02** — ao contrário do módulo 17, este módulo não tem aula candidata a divisão.

A auditoria científica de 2026-08-18 encaminhou explicitamente dois pontos a esta revisão (o título "Duas famílias de hipótese" da aula 06 e a expressão invertida "dinâmica subsidência" da aula 05). Ambos foram recebidos e tratados — são os achados 🟡 8 e 🟡 5.

## Achados

### 🟠 1. O objetivo `oa01` do módulo não descrevia metade do que a aula 01 ensina

**Tipo:** conteúdo órfão / objetivo declarado que não cobre o material
**Onde:** hub do módulo · lista de objetivos de aprendizagem; aulas 01 e 02 · bloco "Ao final você vai conseguir"
**Problema:** o módulo declara **cinco** objetivos para **seis** aulas — as aulas 01 e 02 compartilham `oa01`. O texto de `oa01` no hub, porém, era "Explicar a dinâmica das margens de placa e a geodinâmica do manto", que descreve **só a aula 02**. Todo o conteúdo da aula 01 — polos de Euler, cinemática, as quatro forças motrizes — ficava sem nenhum objetivo de módulo que o nomeasse, apesar de ocupar uma aula inteira e de ser cobrado em Q01 e Q02 (6 dos 46 pontos). Pior: o mesmo identificador `oa01` aparecia com **três redações diferentes** — uma no hub, uma na aula 01, outra na aula 02 — sem que nada indicasse que se tratava de um objetivo repartido. O aluno que usa a lista de objetivos para se orientar não tinha como saber que a aula 01 servia a `oa01`, nem que `oa01` só se completa depois de duas aulas.
**Correção aplicada:** o `oa01` do hub foi ampliado para nomear as duas metades ("cinemática de placas (polos de Euler e forças motrizes) e a dinâmica das margens de placa e da geodinâmica do manto") e declara explicitamente o repartimento entre aula 01 e aula 02. As duas aulas passaram a marcar `[geologia-m18-oa01 · parte 1 de 2]` e `[· parte 2 de 2]`, cada uma apontando o que a outra metade cobre. É a mesma convenção de objetivo repartido que o módulo 17 já usa para `oa04`.
**Escopo:** correção local, concluída. Nenhum identificador foi renumerado — renumerar `oa01`–`oa05` cascatearia para o questionário, o baralho e as seis aulas, com risco desproporcional ao defeito.

### 🟠 2. Três termos técnicos usados sem definição, violando o LC-01

**Tipo:** termo técnico usado antes de definido
**Onde:** aula 02 ("Ligando cada margem à geodinâmica do manto"), aula 04 (Exemplo trabalhado, passo 2), aula 05 ("Dois compartimentos dentro de um mesmo cráton")
**Problema:** o LC-01 exige que todo termo de geociências seja definido em linguagem comum na primeira ocorrência. Três escapavam, e todos em posição de carga:
- **`solidus`** (aula 02) aparecia cru — "reduz o solidus da cunha de manto sobrejacente" — numa frase que é justamente o mecanismo do magmatismo de arco. Sem o termo, a frase inteira fica opaca para quem entra sem geologia, e ela não está no vocabulário da aula nem nos pré-requisitos declarados.
- **`mélanges`** (aula 04) foi **introduzido pela própria correção da auditoria científica** no exemplo trabalhado, ao lado de "ofiolitos" — que a aula define no corpo. O termo novo entrou sem gloss: uma correção factual criou um defeito didático.
- **`greenstone belts`** (aula 05) aparecia em inglês, sem tradução nem definição, no meio da lista que caracteriza o embasamento de um escudo.
**Correção aplicada:** aposto curto em cada um, sem parágrafo novo. `solidus` → "a temperatura em que a rocha começa a fundir", mais uma frase de fechamento que reafirma o mecanismo em linguagem comum ("a água faz o manto fundir a uma temperatura mais baixa do que fundiria seco"). `mélanges` → "misturas caóticas de blocos de rocha de origens diferentes, revolvidos pela própria colisão". `greenstone belts` → "faixas de rochas vulcânicas e sedimentares metamorfizadas, típicas do Arqueano".
**Escopo:** correção local, concluída. As três glosas são definicionais e padrão de manual; nenhuma introduz alegação factual nova sujeita a auditoria.

### 🟠 3. O baralho ignora dois conceitos centrais que a avaliação cobra — ABERTO

**Tipo:** desalinhamento aula–flashcards
**Onde:** baralho (`-basic.csv`, `-cloze.csv`) versus aulas 04 e 06 e questionário
**Problema:** duas lacunas de memorização, ambas em conteúdo que o módulo trata como central:
1. **O ciclo de Wilson não tem nenhum flashcard.** Ele tem entrada própria no vocabulário da aula 04, uma seção inteira ("Um roteiro idealizado"), é o primeiro item do recap dessa aula, é citado na descrição da aula 04 no hub do módulo, e é **cobrado na Q07** (3 pts). Os sete cards de `oa03` cobrem sutura, ofiolito, acresção de terrenos e densidade da crosta — todos periféricos em relação ao roteiro que organiza a aula.
2. **Columbia/Nuna não tem card próprio**, embora a **Q12** peça exatamente a ordenação cronológica Columbia → Rodínia → Pangeia. O baralho tem card para Pangeia (`fb017`, `fc013`) e para Rodínia (`fb018`, `fc014`), mas nada que fixe que Columbia é o mais antigo dos três — que é precisamente a informação que decide a questão.
**Correção sugerida:** dois cards Basic (um para a sequência de cinco estágios do ciclo de Wilson, um para a janela de Columbia/Nuna ~1.800–1.300 Ma) e, opcionalmente, um Cloze para a ordenação dos três supercontinentes.
**Escopo:** **exige gerar item novo no baralho** — titularidade do `gerador-de-flashcards`. Esta skill **não** edita questionário nem baralho; reporta e encaminha. Não bloqueia o gate.

### 🟡 4. O vocabulário da aula 03 estourou o LC-03, e o mecanismo mais cobrado do módulo não estava nele

**Tipo:** carga de vocabulário / termo central ausente do bloco de abertura
**Onde:** aula 03 · "Vocabulário desta aula"
**Problema:** dois defeitos empilhados no mesmo bloco. Primeiro, a correção da auditoria científica (achado 🟠 15, que separou "antearco (forearc)" de "retroarco (back-arc)") levou o bloco de 8 para **9 termos**, acima do teto de 5 a 8 do LC-03 — uma correção factual necessária que produziu, de novo, um efeito colateral didático. Segundo, e mais grave: **"subsidência mecânica" não estava no vocabulário**, embora seja um dos três mecanismos que a aula existe para ensinar, apareça quatro vezes no corpo, seja a resposta esperada da **Q06** e o verso do card **`fb005`**. O bloco listava "subsidência térmica" e "subsidência flexural" como verbetes independentes e simplesmente omitia o terceiro membro do trio — deixando o aluno com dois de três nomes na abertura e o terceiro solto no meio do texto.
**Correção aplicada:** as entradas "Subsidência térmica" e "Subsidência flexural (por carga)" foram fundidas numa única entrada — "Os três mecanismos de subsidência" — que define **mecânica, térmica e flexural** lado a lado e fecha dizendo que cada regime tectônico da aula usa um deles. Isso resolve os dois defeitos de uma vez: o bloco volta a 8 termos (LC-03 cumprido) e o trio passa a ser apresentado como trio, que é como a aula o ensina e como a avaliação o cobra. Nenhuma definição foi perdida.
**Escopo:** correção local, concluída.

### 🟡 5. "dinâmica subsidência de origem mantélica" — ordem de palavras invertida

**Tipo:** redação que trava a leitura de um termo técnico
**Onde:** aula 05 · "Por que a subsidência em bacia cratônica é diferente"
**Problema:** encaminhado pela auditoria científica como correção de redação. A expressão saiu com a ordem do inglês (*dynamic subsidence*), produzindo "dinâmica subsidência de origem mantélica" — que em português lê como se "dinâmica" fosse o substantivo. O termo consagrado é **subsidência dinâmica**, e ele aparece exatamente no ponto em que a aula está nomeando a hipótese menos familiar da seção.
**Correção aplicada:** "(a chamada **subsidência dinâmica**, de origem mantélica)", com o termo em negrito por ser a primeira e única ocorrência.
**Escopo:** correção local, concluída.

### 🟡 6. Quatro pré-requisitos declarados como hesitação, sem link, quebrando o LC-03

**Tipo:** pré-requisito não acionável
**Onde:** aula 03, aula 04, aula 05 e aula 06 · bloco "Antes de começar, você precisa saber"
**Problema:** o LC-03 exige que o bloco "linke as aulas anteriores exigidas", para que "o aluno tenha que poder detectar sozinho que voltou cedo demais". Quatro itens falhavam nisso, e falhavam de um jeito específico: eram redigidos como **dúvida sobre se o aluno já viu o assunto**, num curso linear em que ele necessariamente já viu.
- aula 03: "se você já viu esse tema no módulo de rochas sedimentares, revise rapidamente" — sem link, e o módulo 07 vem 11 módulos antes.
- aula 04: "Metamorfismo regional [...], se você já tiver visto esse tema; caso contrário, o essencial é reapresentado aqui" — sem link para o módulo 08.
- aula 05 e aula 06: "a escala de tempo geológico [...]; se precisar refrescar a memória, revise a escala" — sem link para o módulo 03.
O efeito prático é o oposto do pretendido: o aluno que **não** lembra não recebe o endereço para onde voltar, e o hedge sugere que o conteúdo talvez nem exista no curso.
**Correção aplicada:** os quatro itens passaram a apontar o módulo real — `[[07-rochas-sedimentares-modulo]]`, `[[08-rochas-metamorficas-modulo]]` e `[[03-tempo-geologico-geocronologia-modulo]]` (duas vezes) — com o hedge removido. Os **20 alvos de wikilink** do módulo foram conferidos um a um: todos existem, nenhuma cadeia de pré-requisito quebrada.
**Escopo:** correção local, concluída.

### 🟡 7. Os metadados `palavras_corpo` das seis aulas estavam subdeclarados

**Tipo:** instrumento de verificação desalinhado
**Onde:** as seis aulas · bloco de metadados
**Problema:** os valores declarados (950 a 1.100) não batiam com nenhuma contagem real, e todos os seis erravam **para baixo** — de 65 palavras (aula 03) a 409 (aula 01). É o campo que a própria revisão didática usa para conferir o LC-02: subdeclarado de forma sistemática, ele mascararia um estouro de teto no momento em que ele aparecesse. No módulo 17 esse mesmo defeito escondeu a única violação real de LC-02 do módulo.
**Correção aplicada:** os seis valores foram recontados sobre o corpo real (da seção "Conteúdo" até "Próxima aula", excluindo metadados) e corrigidos, já refletindo todas as edições desta revisão e da auditoria: 1.359 · 1.179 · 1.115 · 1.237 · 1.102 · 1.450.
**Escopo:** correção local, concluída.

### 🟡 8. A aula 06 dividia três modos de reunião entre "duas famílias", sem dizer que eram coisas de tipos diferentes

**Tipo:** taxonomia confusa / título que não corresponde à seção
**Onde:** aula 06 · "Por que os continentes voltam a se reunir? Duas famílias de hipótese"
**Problema:** encaminhado pela auditoria científica. O vocabulário da aula define **três** modos irmãos — introversão, extroversão, ortoversão — e a seção seguinte os distribui entre **duas** famílias, com introversão e extroversão na família 1 e ortoversão emergindo no fim da família 2. Lido pela primeira vez, o aluno não tem como perceber que os três são respostas à mesma pergunta (onde os fragmentos se reencontram) enquanto as duas famílias respondem a outra (por que se reencontram ali). A contagem "duas" versus "três" fica sem explicação e a ortoversão parece um conceito de outra categoria, e não o terceiro membro do trio que a avaliação e o card `fb020` cobram lado a lado.
**Correção aplicada:** parágrafo curto de andaime antes da lista, fixando a distinção entre **resultado geométrico** (os três modos) e **causas propostas** (as duas famílias), e dizendo qual família explica quais modos. O título foi mantido — ele está correto, o que faltava era a ponte.
**Escopo:** correção local, concluída.

### 🔵 9. `oa02` e `oa04` não têm questão de "explicar"

**Tipo:** distribuição cognitiva desigual entre objetivos
**Onde:** questionário final · matriz de avaliação
**Problema:** `oa01`, `oa03` e `oa05` têm cada um uma questão dissertativa de explicação (Q02, Q08, Q13). `oa02` (bacias) e `oa04` (crátons) têm apenas lembrar + aplicar, 6 pontos cada. Não é defeito de cobertura — os cinco objetivos são avaliados, e a matriz declara corretamente "Objetivos sem questão: nenhum" — mas os dois objetivos ficam sem o item que verifica se o aluno sabe *articular* o mecanismo, e não só reconhecê-lo e aplicá-lo a um caso dado.
**Escopo:** sugestão para o `gerador-de-questionarios`. Não é achado bloqueante e não foi corrigido aqui.

### 🔵 10. A aula 01 é a mais longa e a mais abstrata, e abre o módulo

**Tipo:** dificuldade versus posição na progressão
**Onde:** aula 01
**Problema:** a aula 01 tem o maior corpo do módulo depois da 06 (1.359 palavras), sete termos de vocabulário e é a única que pede raciocínio geométrico em esfera (rotação de Euler, velocidade linear proporcional ao seno da distância angular). Ela cumpre o LC-04 — a analogia da toalha de mesa para o *slab pull* vem antes do termo — mas a primeira seção ("Placas não escorregam: elas giram") entrega o teorema antes de qualquer imagem cotidiana, e é a porta de entrada do módulo. Não foi alterada: está dentro de todos os contratos de nível, e mexer na abertura de um módulo aprovado é risco maior que o ganho. Fica registrado como o ponto do módulo em que o autodidata tem mais chance de precisar de uma segunda leitura.
**Escopo:** observação, sem correção. Se o `gerador-de-curso-modular` revisitar o módulo, é o candidato natural a ganhar uma analogia de abertura (um disco girando, um globo terrestre).

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo | Avaliado em | Cards |
|---|---|---|---|---|
| `oa01` parte 1 — cinemática, polos de Euler e forças motrizes | aula 01, quatro seções | sim — par Sul-Americana/Africana com polo hipotético | Q01, Q02 — 6 pts | `fb001`, `fb002`, `fc001`, `fc002` |
| `oa01` parte 2 — convecção, plumas e margens | aula 02, quatro seções | sim — inflexão Havaí–Imperador | Q03, Q04 — 7 pts | `fb003`, `fb004`, `fc003` |
| `oa02` — regime tectônico → tipo de bacia e mecanismo de subsidência | aula 03, seis seções | sim — sucessão rifte → margem passiva | Q05, Q06 — 6 pts · **sem "explicar"** | `fb005`–`fb008`, `fc004`–`fc006` |
| `oa03` — ciclo de Wilson, colisão e acresção de terrenos | aula 04, cinco seções | sim — cinco blocos em 300 km | Q07, Q08, Q09 — 9 pts | `fb009`–`fb012`, `fc007`–`fc009` · **ciclo de Wilson sem card** |
| `oa04` — crátons, quilha, escudo e bacia cratônica | aula 05, cinco seções | sim — raiz de 220 km com duas porções em superfície | Q10, Q11 — 6 pts · **sem "explicar"** | `fb013`–`fb016`, `fc010`–`fc012` |
| `oa05` — ciclo dos supercontinentes | aula 06, cinco seções | sim — dois crátons com polos próximos em ~600–550 Ma | Q12, Q13, Q14 — 12 pts | `fb017`–`fb020`, `fc013`–`fc015` · **Columbia sem card** |

Nenhum objetivo descoberto e nenhuma seção órfã: as seis aulas mapeiam integralmente os cinco objetivos, com `oa01` legitimamente repartido entre as aulas 01 e 02 — repartimento que **passou a ser declarado** pela correção do achado 🟠 1. As ressalvas de cobertura estão no baralho (achado 🟠 3) e no tipo de item (achado 🔵 9), não na existência de cobertura.

## Verificação do contrato de nível

- **LC-01 — nenhum termo sem definição:** aprovado **após** o achado 🟠 2. Os três termos crus (`solidus`, `mélanges`, `greenstone belts`) foram glosados. O melhor caso do módulo é "nappe / manto de cavalgamento", que entra no vocabulário da aula 04 com a tradução ao lado, e "anatexia", glosado por aposto no próprio ponto de uso ("fusão parcial crustal (anatexia)"). A aula 06 acerta ao descrever as duas regiões quentes do manto sem introduzir a sigla LLSVP, que seria carga sem retorno neste nível.
- **LC-02 — teto de 1.600 palavras:** **aprovado nas seis aulas**, entre 1.102 e 1.450. Nenhuma aula do módulo é candidata a divisão em Parte 1 / Parte 2 — diferentemente do módulo 17, cuja aula 06 segue em aberto por 2.071 palavras.
- **LC-03 — abertura padronizada:** aprovado após os achados 🟡 4 e 🟡 6. Os seis blocos de vocabulário ficam agora em 6 a 8 termos (7 · 7 · 8 · 7 · 6 · 6), e os seis blocos "Antes de começar" linkam todos os pré-requisitos exigidos. Os 20 alvos de wikilink foram conferidos e todos resolvem.
- **LC-04 — analogia antes do termo:** aprovado. Piche e vidro escoando para a convecção do manto (a02), a toalha de mesa puxada pelo peso que já caiu para o *slab pull* (a01), a tábua sob peso para a flexão litosférica (a03), a boia funda e resistente para a quilha cratônica (a05). A da aula 03 é a mais bem construída porque a mesma imagem sustenta a definição no vocabulário e o mecanismo no corpo.
- **LC-05 — ordem de grandeza:** aprovado, e é um dos pontos fortes do módulo. "cerca de 220 km", "200 km ou mais", "da ordem de 11° a 15°", "aproximadamente 335–300". A correção da auditoria sobre a analogia da unha (achado 🟠 5 da auditoria) deixou a faixa central e o topo da faixa explicitamente separados, que é exatamente o que o LC-05 pede.
- **LC-06 — matemática reativada antes do uso:** aprovado. A dependência do seno da distância angular aparece de forma qualitativa ("proporcional ao seno", "máxima a 90°") e a aula não pede nenhum cálculo — o exemplo trabalhado raciocina por posição relativa ao polo, não por trigonometria.
- **LC-07 — blocos obrigatórios:** aprovado. As seis aulas têm "Erros comuns", "O que não concluir" e "Recap relâmpago" completos. Os "Erros comuns" atacam confusões reais e específicas — manto líquido × manto que flui, toda erupção como limite de placa, escudo × cráton, ciclo como relógio de período fixo.
- **LC-08 — controvérsia em uma frase:** aprovado com ressalva de estilo. As quatro controvérsias do módulo entram declaradas e sem que a aula arbitre: a deriva da pluma havaiana, o estatuto de Pannótia, o mecanismo de formação da quilha cratônica e os detalhes causais dos padrões de manto. A passagem sobre Pannótia na aula 06 é a mais longa das quatro (cerca de 100 palavras, contra a frase única que o LC-08 sugere), mas foi **mantida como está**: ela é o produto direto da correção ⚪ 2 da auditoria científica, e comprimi-la arriscaria enfraquecer justamente a marcação de disputa que a auditoria introduziu. Fica registrado como tensão consciente entre o LC-08 e o gate científico, resolvida a favor do gate.

## Alinhamento entre as aulas

A progressão é cumulativa e sem salto: como as placas se movem e o que as move (01) → o que sustenta esse movimento por baixo (02) → onde o sedimento se acumula em cada regime (03) → o que acontece quando o oceano fecha (04) → o que sobra estável depois (05) → como tudo isso se repete em escala de bilhões de anos (06). Cada aula reutiliza a anterior sem reensiná-la, e as três últimas dependem explicitamente das três primeiras.

Duas escolhas de sequência merecem registro por serem acertos. A primeira: bacias sedimentares (03) vêm **antes** de orogênese (04), embora a bacia de antepaís dependa da carga orogênica — funciona porque a aula 03 declara a dependência e a difere ("tema da próxima aula"), e a aula 04 devolve o ponteiro ao explicar que gera a carga discutida antes. A segunda: crátons (05) vêm **depois** de orogênese (04), e não junto do material sobre litosfera do módulo 02 — a dependência real é de "o que é uma orogênese", porque cráton se define pela **ausência** dela, e a aula está posicionada de acordo com a dependência real, não com a afinidade temática.

O módulo também se conecta bem para fora: a aula 01 declara o módulo 17 como pré-requisito, e a aula 06 fecha apontando o módulo 19 como o lugar onde as ferramentas para testar esses modelos serão vistas.

## O que está bem feito

A disciplina em separar **observação de interpretação** é o ponto mais forte do módulo, e ela aparece na estrutura, não só em ressalvas soltas. O exemplo trabalhado da aula 02 é o melhor caso do curso nesse aspecto: ele constrói o modelo simples (pluma fixa, placa que se move), mostra o dado que o confirma (idades progressivas) e só então apresenta o dado paleomagnético que o complica (a fonte também se moveu) — terminando com "modelo de trabalho útil, não uma lei absoluta". O aluno sai sabendo o modelo **e** sabendo por que ele é provisório, que é a estrutura certa para material autodidata.

Os blocos "O que não concluir" fazem trabalho que os "Erros comuns" não fariam: em vez de listar confusões de vocabulário, eles barram **generalizações indevidas** — que uma única cadeia de ilhas prove a velocidade exata da placa, que toda margem hoje passiva sempre foi passiva, que toda crosta antiga seja um cráton, que um mecanismo isolado explique o ciclo dos supercontinentes. É a defesa contra o modo de falha mais comum de quem estuda sozinho, que é extrapolar o caso ensinado.

As aulas 03 e 05 tratam com cuidado o ponto em que a geologia brasileira entra: a Bacia do Paraná é usada como exemplo **e** como advertência, depois da correção da auditoria, mostrando que a categoria "bacia cratônica" não se aplica limpa a ela. Um exemplo que ensina os limites da própria categoria vale mais que três exemplos que a confirmam.

## Gate didático

**Liberado.** Nenhum achado 🔴. Os sete achados corrigíveis nesta skill foram aplicados; nenhuma edição introduziu alegação factual nova, e nenhuma tocou em número, limite, classificação ou fonte já validados pela auditoria científica de 2026-08-18 e por sua reverificação da mesma data.

Duas correções desta revisão foram, na origem, **efeitos colaterais didáticos de correções factuais** — o termo `mélanges` introduzido sem gloss pela auditoria (🟠 2) e o vocabulário da aula 03 empurrado a 9 termos pela separação antearco/retroarco (🟡 4). Vale registrar o padrão: rodar o auditor antes do revisor está certo, mas a passagem do primeiro para o segundo precisa olhar especificamente o que o auditor **acrescentou** ao texto, não só o que ele corrigiu.

Uma ressalva permanece aberta, fora da titularidade desta skill e não bloqueante:

1. **Achado 🟠 3** — o baralho não tem card para o **ciclo de Wilson** (cobrado na Q07) nem para **Columbia/Nuna** (cobrado na Q12). Encaminhado ao `gerador-de-flashcards`. Somam-se a isso as duas sugestões 🔵 9 e 🔵 10, ambas não bloqueantes.

O `course-state.yaml` **não** foi alterado por esta execução, conforme a restrição de coordenação em paralelo; o registro do módulo foi feito apenas no hub `18-tectonica-global-geodinamica-modulo.md`. Nenhum arquivo fora de `18-tectonica-global-geodinamica/` foi tocado — em particular, nada nos módulos 16 e 20.
