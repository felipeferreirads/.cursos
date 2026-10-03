# Revisão didática — Módulo 26: Geologia isotópica aplicada

**Revisado em:** 2026-09-22 · **Modo:** `review-and-fix`
**Material:** `26-geologia-isotopica-aplicada/` — 6 aulas na entrada, **7 na saída**
**Passagem:** 1 (revisão do zero; não reaproveita nenhuma passagem anterior)
**Veredito:** **Bem ensinado com ressalvas** — nenhum defeito impede acompanhar o que o módulo ensina, mas há **um objetivo de aprendizagem do módulo sem cobertura em aula nenhuma**, que fica em aberto e não pode ser resolvido aqui.

---

## Resumo

🔴 1 bloqueia · 🟠 5 prejudicam · 🟡 5 atrito · 🔵 2 sugestões

| Severidade | Levantados | Corrigidos | Em aberto |
|---|---|---|---|
| 🔴 Bloqueia | 1 | 0 | **1** |
| 🟠 Prejudica | 5 | 5 | 0 |
| 🟡 Atrito | 5 | 5 | 0 |
| 🔵 Sugestão | 2 | — | 2 (não são defeitos) |
| **Total** | **13** | **10** | **1 + 2 sugestões** |

O único achado em aberto é o 🔴 1 (paleoclimatologia declarada no objetivo do módulo e não ensinada em lugar nenhum). Ele **não** é corrigível nesta skill: exige conteúdo factual novo, que precisa ser escrito pelo redator e passar pelo auditor. Corrigi-lo aqui seria publicar material que não passou pelo gate.

**Carga do módulo, antes e depois.** Contagem do corpo entre `## Conteúdo` e `## Fontes`, incluindo LaTeX e tabelas, a 84 palavras/min — método agora declarado nos metadados de cada aula, porque as contagens anteriores usavam convenção não declarada e não são comparáveis:

| Aula | Antes | Depois | Conceitos novos independentes | Exemplos |
|---|---|---|---|---|
| 01 — decaimento e espectrometria | 2386 (~28,4 min) | **2563 (~30,5 min)** | 5 | 1 |
| 02 — K-Ar e Ar-Ar | 2545 (~30,3 min) | 2545 (~30,3 min) | 5 | 2 |
| 03 — Rb-Sr | 2155 (~25,7 min) | 2323 (~27,7 min) | 4 | 1 |
| 04 — Sm-Nd | 2126 (~25,3 min) | 2126 (~25,3 min) | 4 | 1 |
| 05 — U-Pb e Pb-Pb | 2177 (~25,9 min) | 2325 (~27,7 min) | 5 | 2 |
| 06 — isótopos estáveis (original) | **2548 (~30,3 min)** | — dividida — | **7** | **1** |
| 06 — δ, fracionamento, S e O | — | 2100 (~25,0 min) | 4 | 1 |
| 07 — registro ambiental (nova) | — | 2162 (~25,7 min) | 4 | 1 |

---

## Nota de método: o que esta revisão não fez

Duas linhas que valem mais que qualquer achado, porque delimitam a confiança que se pode depositar no resultado.

**Não foi inventado conteúdo factual.** Toda edição aqui ou (a) nomeia e define um conceito que o módulo já usava e já tinha auditado em outra aula, (b) mostra por extenso uma conta cujos resultados já estavam publicados e já tinham sido verificados pela auditoria de 2026-09-21, ou (c) retira uma promessa que o texto fazia e não cumpria. As duas contas expandidas (a regressão da Aula 03 e a iteração Pb-Pb da Aula 05) foram **reexecutadas em Python nesta revisão** e reproduzem os valores já publicados; não há um único número novo no módulo.

**Uma exceção, declarada.** O novo exemplo trabalhado da Aula 07 é conteúdo que não existia. Ele não afirma nenhum fato novo sobre o mundo — os oito valores são hipotéticos e a interpretação aplica, passo a passo, três mecanismos já auditados (claims 005, 006 e 008) —, e é do mesmo gênero e do mesmo nível de risco do exemplo de sulfetos que a auditoria já examinou e aprovou. Ainda assim, foi criado **depois** do auditor, e por isso recebeu claim_id próprio (`ISOGEO-M26-A07-EXEMPLO-SECAO-QUIMIOESTRATIGRAFICA-001`) com um ponto explícito a conferir na próxima passagem de auditoria. Há um segundo ponto marcado para conferência, na Aula 07: a atribuição do MIF do mercúrio ao spin nuclear é o único mecanismo que esta revisão enunciou sem que o módulo já o enunciasse, e o metadado diz como reduzi-lo sem perda didática caso não se confirme.

---

## Achados

### 🔴 1. Paleoclimatologia é declarada no objetivo do módulo, no título e no objetivo da aula — e não é ensinada em lugar nenhum

**claim_id didático:** `DID-M26-OA04-PALEOCLIMATOLOGIA-NAO-COBERTA-002`
**Tipo:** objetivo declarado não coberto
**Onde:** `geologia-avancado-m26-oa04` (hub e `course-state.yaml`); título e objetivo da Aula 06 original
**Problema:** o objetivo de aprendizagem OA-04 diz, textualmente, "Aplicar assinaturas de isótopos estáveis a problemas de metalogênese, **paleoclimatologia**, contaminação ambiental e quimioestratigrafia". A Aula 06 original repetia a palavra no título e no campo de objetivo. A palavra **"paleoclim" não aparece no corpo de nenhuma das seis aulas do módulo** — a verificação foi feita por varredura de texto, não por impressão de leitura. Não há seção sobre δ18O em foraminíferos, sobre efeito de volume de gelo, sobre paleotermometria, nem sobre testemunhos de gelo. O que existe de adjacente não cobre o objetivo: a seção de δ18O trata de **petrogênese ígnea** (contaminação crustal e água meteórica em granitos), e as excursões de δ13C são tratadas como ferramenta de **correlação estratigráfica**, não de reconstrução climática. A aula ensina, é verdade, o mecanismo que sustenta a paleotermometria — o fracionamento de equilíbrio dependente de temperatura —, mas nunca o aplica a clima.

O efeito sobre quem estuda é específico e vale nomear: um aluno que use os objetivos declarados como checklist de revisão vai procurar, no material, um conteúdo que não está lá, e terá de decidir sozinho se não entendeu ou se não foi ensinado. Em material autodidata, sem professor a quem perguntar, essa dúvida custa caro — e a resposta certa, aqui, é a segunda.

**Correção aplicada:** **nenhuma correção de conteúdo, deliberadamente.** Escrever a seção faltante significaria publicar afirmações factuais novas (valores de δ18O de foraminíferos, a relação entre δ18O e temperatura ou volume de gelo, calibrações) que não passaram pelo auditor — exatamente o que o encadeamento do plugin existe para impedir. O que foi feito foi **parar de declarar o que não se entrega**: a menção a paleoclimatologia saiu do título e do objetivo das aulas 06 e 07, para que nenhuma aula prometa o que não cumpre. O OA-04 do módulo foi **mantido como está**, para que a lacuna continue visível em vez de desaparecer por conveniência.
**Escopo:** **exige conteúdo novo** — seção nova na Aula 06 ou 07, ou uma aula 08 curta, escrita pelo `gerador-de-aula`/redator e submetida ao `auditor-cientifico` antes de qualquer questionário ou flashcard cobrar o tema.
**Situação:** **em aberto.** Registrado em `didactic_review.open_findings` no `course-state.yaml` e no `next_action`.

---

### 🟠 2. A Aula 06 empilhava sete domínios de aplicação independentes com um único exemplo trabalhado

**claim_id didático:** `DID-M26-A06-SOBRECARGA-SETE-DOMINIOS-001`
**Tipo:** excesso de conceitos novos / sobrecarga cognitiva
**Onde:** Aula 06 original, inteira
**Problema:** 2548 palavras (~30,3 min, no teto do plugin) para cobrir a notação δ, os dois regimes de fracionamento, δ34S em metalogênese, δ18O em petrogênese, quimioestratigrafia (com **dois** sistemas independentes dentro dela, Sr e C), isótopos não tradicionais (com **três** elementos independentes dentro dela, Fe, Mo e Hg) e contaminação ambiental. São sete blocos que não se apoiam uns nos outros: quem pula o de mercúrio não perde nada para ler o de contaminação. A regra prática é de três a quatro ideias independentes por aula de 30 minutos; esta tinha o dobro.

O sintoma que confirma o diagnóstico não é a contagem, é a distribuição do esforço do aluno: a aula tinha **um** exemplo trabalhado, e ele cobria o **primeiro** dos sete domínios. Os seis restantes eram exposição sem prática — e são justamente os mais distantes da intuição de quem vem de cinco aulas de geocronologia. Uma aula em que seis sétimos do conteúdo não tem onde ser exercitado não é uma aula densa; é duas aulas mal empacotadas.

**Correção aplicada:** **divisão em duas aulas**, por corte temático e não por metade de contagem:
- **Aula 06 — "Isótopos estáveis: notação delta, fracionamento, e aplicação a minérios e magmas"** (~25 min): os dois blocos de fundamento (notação, fracionamento) mais os dois isótopos leves clássicos aplicados à rocha e ao minério (S e O), com o exemplo dos três estágios de sulfeto, que é exatamente o exemplo deste conteúdo.
- **Aula 07 — "Isótopos estáveis como registro ambiental: quimioestratigrafia, paleorredox e rastreamento de contaminação"** (~26 min): os três blocos ambientais, com um exemplo trabalhado novo que cruza δ13C e δ98Mo numa seção sedimentar.

O corte tem uma lógica que o aluno consegue enunciar, que é o teste de uma divisão boa: a Aula 06 lê a **rocha**, a Aula 07 lê o **ambiente em que a rocha se formou**. **Nenhuma frase de conteúdo foi perdida** — o texto das três seções movidas está integralmente na Aula 07.
**Escopo:** divisão de aula, com atualização do hub, do bloco `lessons` no `course-state.yaml` e do bloco "Próxima aula" da Aula 05.

---

### 🟠 3. A Aula 04 prometia um exemplo de idade-modelo que o exemplo não faz, deixando uma equação publicada sem nunca ser instanciada

**claim_id didático:** `DID-M26-A04-TDM-PROMESSA-FALSA-003`
**Tipo:** exemplo prometido e não entregue / referência interna falsa
**Onde:** Aula 04 · seção "Idade-modelo: uma idade sem isócrona"
**Está escrito (antes):** "esta aula usa, **no exemplo a seguir**, uma aproximação **linear simplificada** da evolução do manto empobrecido apenas para fins didáticos"
**Problema:** o exemplo trabalhado da Aula 04 calcula idade isocrônica e εNd(t). Ele **não** calcula T_DM, não usa manto empobrecido e não usa aproximação linear nenhuma. A promessa é falsa, e o leitor que confia nela vai procurar no exemplo algo que não está lá — e, não achando, vai supor que não entendeu.

O dano é maior que o de uma referência quebrada qualquer, porque a equação de T_DM fica publicada com três valores de referência do manto empobrecido que o aluno nunca vê preenchidos com nada. Uma fórmula que aparece, ocupa quatro linhas e nunca é usada ensina, na prática, que ela é decorativa.

**Correção aplicada:** a promessa foi retirada e substituída por um parágrafo que diz explicitamente que a aula **não** calcula T_DM numericamente e **por quê** — os parâmetros de referência do manto empobrecido não são universais, dependem do modelo adotado, e aproximá-los por uma reta desloca o resultado em dezenas a centenas de milhões de anos justamente nas rochas antigas em que T_DM interessa. O que o aluno deve reter foi realocado para onde de fato está o valor: a **leitura geométrica** (T_DM é o encontro de duas curvas de evolução projetadas para trás) e a pergunta crítica que ele precisa saber fazer diante de um T_DM publicado — "contra que modelo de manto este número foi calculado?" —, que é o que decide se dois T_DM de artigos diferentes são comparáveis. A entrada de DePaolo (1981) na lista de Fontes repetia a mesma frase e foi ajustada na mesma edição, assim como o registro do claim `ISOGEO-M26-A04-IDADE-MODELO-TDM-006`, que afirmava que a aula usava a simplificação linear.
**Escopo:** correção local. Um exemplo numérico de T_DM seria a correção ideal, mas exige declarar valores de referência do manto empobrecido — conteúdo factual novo, portanto fora desta skill. Registrado como sugestão 🔵 12.

---

### 🟠 4. "Temperatura de bloqueio" é usada duas vezes, em duas aulas, e nunca definida — sendo o conceito que sustenta o ponto de dificuldade declarado do módulo

**claim_id didático:** `DID-M26-A01-TEMPERATURA-BLOQUEIO-INDEFINIDA-005`
**Tipo:** termo técnico usado antes de definido
**Onde:** Aula 01 · premissa 1 ("resfriamento abaixo de uma temperatura de bloqueio"); Aula 02 · seção de espectros ("o último resfriamento abaixo da temperatura de bloqueio do argônio para aquele mineral")
**Problema:** o termo aparece nas duas aulas sem nenhuma definição, e não é definido em nenhuma outra. Não é um termo periférico: é ele que explica por que uma idade isotópica data um **fechamento** e não uma cristalização — que é, palavra por palavra, o "ponto de dificuldade" que o hub do módulo declara como o principal ("Uma idade isotópica data um evento de fechamento do sistema, não necessariamente o evento geológico que interessa"). O módulo declara que este é o ponto duro e deixa o conceito que o sustenta sem nome explicado.

O leitor consegue seguir o parágrafo em que o termo aparece, porque o contexto sugere o sentido geral — e é exatamente esse o problema. Ele segue em frente com uma noção aproximada de um conceito que vai reaparecer na leitura de espectros de platô (Aula 02), na discórdia (Aula 05) e, sobretudo, no Módulo 27, que é inteiro sobre a diferença entre datar um mineral e datar um evento.

**Correção aplicada:** definição na primeira ocorrência (Aula 01, premissa 1), mais um bullet no recap da mesma aula. A definição acrescentada — temperatura abaixo da qual a difusão do isótopo-filho para fora da rede cristalina fica lenta demais para importar em escala geológica; acima dela o filho escapa à medida que é produzido, abaixo dela o mineral retém o que produz — **não introduz fato novo no módulo**: é exatamente o mecanismo que a Aula 02 já descreve ao tratar de perda de argônio por difusão térmica e de espectros de aquecimento escalonado (claim `ISOGEO-M26-A02-ESPECTRO-PLATO-007`, auditado), e que a Aula 05 descreve para a perda de chumbo. A revisão nomeou e definiu, no lugar certo, o que o módulo já usava. Nenhum valor numérico de temperatura de bloqueio foi publicado — isso seria fato novo.
**Escopo:** correção local (Aula 01).

---

### 🟠 5. O exemplo carro-chefe da Aula 03 pula o passo em que o resultado é produzido

**claim_id didático:** `DID-M26-A03-REGRESSAO-PASSO-OPACO-006`
**Tipo:** salto no exemplo trabalhado
**Onde:** Aula 03 · "Exemplo trabalhado: construindo e resolvendo uma isócrona Rb-Sr"
**Problema:** o exemplo verificava a colinearidade calculando três inclinações parciais — passo transparente, reproduzível — e, na frase seguinte, anunciava que "uma regressão linear completa devolve uma inclinação de aproximadamente 0,002040 e um intercepto de aproximadamente 0,70759". Os dois números aparecem do nada. O aluno acabou de fazer três contas com a calculadora na mão e, no momento em que o resultado importa, é informado dele.

Este é o exemplo mais importante do módulo — a isócrona é a técnica que as Aulas 03, 04 e 05 compartilham — e, não por acaso, é exatamente aqui que a auditoria de 2026-09-21 encontrou o seu achado laranja 2: a redação havia publicado uma inclinação "estimada por inspeção", errada em 1,5%, com mudança de período geológico na interpretação. Um passo que ninguém consegue reproduzir é onde um erro se esconde por uma passagem inteira. Corrigir o número sem abrir o passo deixa a mesma armadilha armada para a próxima vez.

**Correção aplicada:** a conta de mínimos quadrados foi mostrada por extenso — médias x̄ = 1,375 e ȳ = 0,71040, as duas somas de que a reta depende (S_xx = 4,3675 e S_xy = 0,008910), a inclinação como quociente delas e o intercepto pela passagem da reta pelo centro do conjunto. **Aritmética reexecutada em Python nesta revisão:** b = 0,00204007 e a = 0,70759491, que arredondam exatamente para os 0,002040 e 0,70759 já publicados; ln(1,00204007) = 0,00203799 e t = 143,52 Ma, consistente com os 143,5 Ma publicados. **Nenhum valor novo entrou na aula** — só o caminho até os valores que já estavam lá e já tinham sido auditados. A observação de que a inclinação ajustada não é a média das parciais, que a auditoria pedira, ganhou o número explícito (0,00205).

*Registro para a próxima auditoria, sem abrir achado:* o registro do achado laranja 2 anota inclinação 0,0020395; o recálculo desta revisão dá 0,0020401. A diferença está na sexta casa, não altera nada arredondado a 0,002040 nem a idade a uma casa decimal, e o valor **publicado** está correto nas duas contas.
**Escopo:** correção local (Aula 03).

---

### 🟠 6. O Exemplo 2 da Aula 05 ensina um método de tentativa sem mostrar uma única tentativa

**claim_id didático:** `DID-M26-A05-ITERACAO-PASSO-OPACO-006b`
**Tipo:** salto no exemplo trabalhado
**Onde:** Aula 05 · "Exemplo trabalhado 2: idade Pb-Pb por iteração"
**Problema:** a lição inteira deste exemplo é *como se resolve na mão uma equação transcendental* — testar, ver de que lado errou, refinar. O texto dizia "Para t = 2,70 × 10⁹ anos, o lado esquerdo calcula-se em aproximadamente 25,54 (alto demais)" e seguia listando mais dois resultados. O único passo que havia para ensinar era o único omitido: o aluno recebe três números e nenhum caminho até eles, num exemplo cujo objetivo declarado é justamente o caminho.

Faltava também o que torna o método um método e não um chute: **por que** 25,54 acima do alvo significa "velho demais". Sem a monotonicidade da razão ²⁰⁷Pb*/²⁰⁶Pb* com a idade, o aluno não tem como escolher a direção da tentativa seguinte.

**Correção aplicada:** a primeira tentativa (t = 2,70 Ga) foi expandida em três linhas — os dois expoentes, os dois e^x − 1 e o quociente — com a observação explícita de que as outras tentativas são a mesma conta com outro número. Foi acrescentada a razão da monotonicidade: o ²³⁵U, de meia-vida muito mais curta, esgotou-se mais cedo e acumulou seu chumbo mais cedo, de modo que a razão cresce com a idade — o que decorre diretamente das duas constantes já publicadas e auditadas na própria aula. **Aritmética reexecutada em Python:** λ235·t = 2,659095 → e^x − 1 = 13,2834; λ238·t = 0,4188375 → e^x − 1 = 0,520193; quociente = 25,5354 → 25,54, o valor já publicado. As tentativas em 2,60 Ga (24,0416) e 2,652 Ga (24,8054) também foram reconferidas e batem.
**Escopo:** correção local (Aula 05).

---

### 🟡 7. A Aula 01 terminou esta revisão no teto de duração, em parte por causa da própria revisão

**claim_id didático:** `DID-M26-A01-DURACAO-NO-TETO-007`
**Tipo:** carga no limite
**Onde:** Aula 01, inteira
**Problema:** a aula passou de ~28,4 para ~30,5 minutos, e a definição de temperatura de bloqueio do achado 🟠 4 responde por boa parte do acréscimo. Vale registrar o incômodo honestamente: esta skill corrige sobrecarga dividindo, não enchendo, e aqui uma correção de clareza empurrou uma aula para o limite.

**Decisão, e por que não dividir:** a Aula 01 é um arco único — lei do decaimento → equação da idade → premissas → como se mede. Dividi-la separaria a dedução da sua aplicação, o que é pior que 30 minutos. E cortar conteúdo bom para caber num número seria trocar um defeito real por um cosmético.
**Correção aplicada:** nenhuma no texto. Ficou registrado nos metadados da aula que nenhuma passagem futura deve acrescentar texto ali sem cortar o equivalente, e o método de contagem de palavras passou a ser declarado em todas as aulas, para que a próxima passagem compare o mesmo número. A Aula 02 está na mesma situação (~30,3 min) e pela mesma razão não foi dividida: K-Ar e ⁴⁰Ar/³⁹Ar são um arco só, e o segundo existe para consertar o primeiro.
**Escopo:** registro, sem edição.

---

### 🟡 8. Na Aula 03, a digressão sobre qual λ usar interrompe o fio sem se explicar

**claim_id didático:** `DID-M26-A03-ORDEM-DIGRESSAO-LAMBDA-008`
**Tipo:** ordem interna subótima
**Onde:** Aula 03 · seção entre a construção da isócrona e a interpretação petrogenética
**Problema:** a seção sobre o valor numérico da constante de decaimento do ⁸⁷Rb ficava encaixada entre "aqui está a equação da isócrona" e "e aqui está o que o intercepto significa", cortando ao meio o movimento natural da aula. O título que tinha ("O que o valor numérico da constante de decaimento revela sobre a maturidade de um método") prometia uma reflexão metodológica geral e entregava, na prática, a escolha de um número para o exemplo.
**Correção aplicada:** a seção **não** foi movida, porque ela precisa vir antes do exemplo, que escolhe um λ. Recebeu título novo ("Uma pausa antes de interpretar: qual λ usar, e por que a pergunta tem resposta") e uma frase de ponte que declara ao leitor que a interrupção é deliberada e para que serve. Sinalizar uma digressão custa uma linha e devolve ao leitor o controle do fio.
**Escopo:** correção local (Aula 03).

---

### 🟡 9. O (t) de εNd(t) é prometido no cabeçalho, nunca introduzido na teoria, e aparece de surpresa dentro do exemplo

**claim_id didático:** `DID-M26-A04-NOTACAO-EPSILON-T-011`
**Tipo:** notação usada antes de introduzida
**Onde:** Aula 04 · "O reservatório condrítico uniforme (CHUR) e a notação εNd" e exemplo trabalhado
**Problema:** o cabeçalho promete "converter uma razão ¹⁴³Nd/¹⁴⁴Nd medida em um valor **εNd(t)**". A seção de teoria define εNd **sem argumento**, contra o CHUR de hoje. O (t) só aparece já dentro do exemplo, onde o aluno descobre sem aviso que precisa recalcular também o CHUR para trás no tempo — e onde a aula, é justo dizer, explica bem a conta. Mas a surpresa vem antes da explicação, e quem lê material sozinho gasta a surpresa achando que perdeu um parágrafo.
**Correção aplicada:** parágrafo de advertência de notação ao fim da seção de teoria: o que o (t) significa (os dois termos avaliados na idade da rocha, não hoje), por que o CHUR precisa ser recalculado (ele também acumula ¹⁴³Nd) e que é quase sempre o εNd(t) que se publica. Nenhum número novo; a equação de evolução do CHUR continua sendo apresentada no exemplo, onde é usada.
**Escopo:** correção local (Aula 04).

---

### 🟡 10. "Suíce ígnea"

**claim_id didático:** `DID-M26-A03-GRAFIA-SUITE-010`
**Tipo:** erro de digitação
**Onde:** Aula 03 · "Construindo a equação da isócrona"
**Problema:** "rochas distintas de uma mesma **suíce** ígnea". Apontado pela auditoria de 2026-09-21 como observação fora do escopo dela.
**Correção aplicada:** "suíte ígnea". Corrigida também a grafia "Ziscoes" por "Zircoes" no bloco de metadados da Aula 06, encontrada nesta revisão.
**Escopo:** correção local.

---

### 🟡 11. Os pré-requisitos declarados das Aulas 05 e 06 omitem aulas de que elas dependem explicitamente

**claim_id didático:** `DID-M26-PREREQ-DECLARADOS-INCOMPLETOS-012`
**Tipo:** pré-requisito usado e não declarado
**Onde:** cabeçalhos das Aulas 05 e 06
**Problema:** a Aula 05 declarava as Aulas 03 e 04, mas o corpo se apoia, por escrito, na Aula 01 ("aplicando a equação geral da idade da Aula 01") e duas vezes na Aula 02 ("a mesma lógica de filho inicial desprezível do argônio na Aula 02"; "ao contrário de uma medida K-Ar de mineral único (Aula 02)"). A Aula 06 declarava apenas a Aula 01, e a seção de δ18O apoia-se em 03 e 04 para o argumento de complementaridade entre traçadores. O defeito é leve — nenhum aluno que leia o módulo em ordem tropeça nele —, mas o cabeçalho de pré-requisito existe justamente para quem **não** lê em ordem, que é quem revisa, quem volta e quem consulta.
**Correção aplicada:** pré-requisitos das duas reescritos, dizendo a razão de cada dependência em vez de só listar números. Na Aula 06 ficou explícito que 03 e 04 são necessárias apenas para as referências cruzadas do fim, não para o conteúdo próprio da aula — o que é informação útil para quem precisa decidir o que reler. A Aula 07, nova, declara 06 (sem a qual não se sustenta) e 03.
**Escopo:** correção local (cabeçalhos).

---

### 🔵 12. A Aula 04 tem folga para um exemplo numérico de idade-modelo

**Tipo:** oportunidade, não defeito
**Onde:** Aula 04
**Situação:** é a aula mais leve do módulo (~25 min contra ~30 das Aulas 01 e 02) e a única cuja equação central — a de T_DM — nunca é instanciada. Um exemplo numérico fecharia a distância entre "explicar o que T_DM estima" (que o objetivo declara e a aula entrega) e "calcular um T_DM" (que a aula não entrega e não promete). **Não aplicada** porque escrever o exemplo exige declarar valores de referência do manto empobrecido, que é conteúdo factual novo e pertence ao redator e ao auditor, não a esta skill.

---

### 🔵 13. O módulo pede que o aluno leia diagramas e não mostra nenhum

**Tipo:** oportunidade, não defeito
**Onde:** Aula 02 (espectro de aquecimento escalonado) e Aula 05 (concórdia e discórdia)
**Situação:** o OA-02 diz "construindo e lendo os **diagramas** correspondentes", e o módulo não tem uma única figura. Nos dois casos acima a geometria **é** o conteúdo: o formato em U ou escada ascendente de um espectro de perda de argônio, e a posição dos interceptos superior e inferior de uma discórdia sobre uma curva côncava. A prosa das duas aulas descreve as formas com cuidado e o aluno consegue acompanhar — por isso isto é sugestão e não achado. Mas um esquema em cada uma economizaria bastante releitura, e é o tipo de apoio visual que a skill de geração de aulas prevê. **Não aplicada:** produzir figuras corretas está fora do escopo de uma revisão didática de texto.

---

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo trabalhado | Avaliado em |
|---|---|---|---|
| **OA-01** — lei do decaimento e princípio da espectrometria de massa | Aula 01 (seções 2 a 6) | sim (idade de mineral hipotético) | — questionário não existe |
| **OA-02** — calcular idades nos cinco sistemas e ler os diagramas | Aulas 02, 03, 04, 05 | sim, nas quatro (6 exemplos) | — |
| **OA-03** — interpretar razão inicial de Sr, εNd e discordância U-Pb | Aulas 03, 04, 05 | sim, nas três | — |
| **OA-04** — isótopos estáveis em metalogênese, **paleoclimatologia**, contaminação ambiental e quimioestratigrafia | metalogênese → Aula 06; quimioestratigrafia e contaminação → Aula 07; **paleoclimatologia → nenhuma** | sim nas duas (sulfetos; seção quimioestratigráfica) | — |

Três dos quatro objetivos estão cobertos com folga e com exemplo. O OA-04 está coberto em três dos seus quatro ramos — ver o achado 🔴 1. A coluna de avaliação está vazia porque o módulo ainda não tem questionário nem baralho: a revisão didática correu antes deles, que é a ordem certa. **Consequência para quem for gerar a avaliação:** o questionário do módulo **não deve** cobrar paleoclimatologia enquanto o achado 🔴 1 estiver em aberto, sob pena de cobrar o que o material não ensina — que é o desalinhamento aula–avaliação que esta skill existe para pegar.

---

## O que está bem feito

Vale registrar com precisão, porque é o que as próximas revisões não devem estragar.

**A espinha dorsal do módulo é exemplar.** A equação geral da idade é deduzida uma vez na Aula 01 e depois **reconhecida** — não rededuzida — em cada sistema: a Aula 02 a apresenta com o fator de ramificação, a Aula 03 a transforma em isócrona, a Aula 04 diz explicitamente que a isócrona Sm-Nd tem "exatamente a mesma forma", a Aula 05 a aplica duas vezes em paralelo. O aluno aprende uma equação e a vê render cinco métodos. Essa economia é difícil de conseguir e fácil de destruir numa revisão apressada que "explique melhor" cada aula isoladamente.

**As aulas dizem quando estão simplificando.** A Aula 04 declara que a curva de DePaolo não é linear; a Aula 02 declara que os critérios de platô são convenção e não regra universal; a Aula 03 declara que usa o λ clássico por ser o de manuais e que um trabalho atual deve usar a recomendação IUPAC-IUGS; os exemplos declaram, todos, que seus dados são hipotéticos. Material autodidata que sinaliza os próprios atalhos ensina, junto com o conteúdo, o hábito de procurar os atalhos alheios.

**A Aula 02 ensina a desconfiar do próprio método.** A seção "Onde ainda mora a incerteza" poderia ter sido cortada sem prejuízo aparente — e é a mais formativa da aula. Dizer ao aluno que a idade que ele acabou de aprender a calcular depende de uma calibração ainda em disputa, e que ler um artigo exige conferir qual convenção o autor declarou, é ensinar geocronologia como ela é praticada, não como ela aparece numa tabela.

**As referências cruzadas apontam para conteúdo que existe.** Foram verificadas uma a uma nesta revisão: todas as menções a "Aula 0X" e ao Módulo 25 e 27 correspondem a material real e ao que ele de fato diz. Numa cadeia de sete aulas com esse grau de interdependência, isso não é automático.

**Os exemplos terminam em interpretação geológica, não em número.** Nenhum dos oito exemplos trabalhados do módulo para no resultado: todos dizem o que o número significa, e vários dizem o que ele **não** significa. A Aula 03 chega a observar que a incerteza analítica típica é da mesma ordem da distância do resultado ao limite cronoestratigráfico, e que por isso a idade não decide sozinha de que lado da fronteira o evento caiu. Essa é a diferença entre ensinar a fazer a conta e ensinar geocronologia.
