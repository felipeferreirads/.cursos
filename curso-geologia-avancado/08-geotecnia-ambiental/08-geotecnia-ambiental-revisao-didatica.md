# Revisão didática — Módulo 08: Geotecnia ambiental

**Módulo:** [[08-geotecnia-ambiental-modulo|Módulo 08 — Geotecnia ambiental]]
**Escopo:** 6 aulas (a01–a06). Pergunta orientadora: alguém aprende com este material, ou só está correto?
**Modo:** `review-and-fix`. As melhorias seguras foram aplicadas ao texto; as que exigiriam reescrever a arquitetura do módulo estão registradas como ressalva justificada.
**Executada após** a auditoria científica ([[08-geotecnia-ambiental-auditoria|relatório]]), sobre o texto já corrigido.
**Data:** 2026-08-29

## Veredito geral: bem ensinado, com uma correção aplicada e três ressalvas de extensão

O módulo tem uma arquitetura clara e um acerto pedagógico central: a **a01 fabrica uma ferramenta conceitual — o tripé hidráulico–mecânico–químico — e as cinco aulas seguintes a consomem em contextos progressivamente mais difíceis**. A a03 usa o plano hidráulico para escolher o sítio; a a04 usa os três planos para dimensionar liner e cobertura; a a05 leva o plano mecânico ao caso extremo em que a resistência não drenada decide tudo; a a06 volta ao plano químico, agora para desfazer a contaminação em vez de contê-la. Isso ataca exatamente o que o hub do módulo declarou como sua maior dificuldade — "dimensionar uma barreira exige raciocinar simultaneamente em três planos, e é raro que os três otimizem juntos".

Foi encontrada **uma lacuna real** — um objetivo declarado que nenhuma seção ensinava —, corrigida nesta revisão. As demais observações são de calibragem, não de defeito.

## Achados

### 🟠 [DID-M08-A02-USLE-001] — Objetivo declarado que nenhuma seção da aula ensinava

**Aula:** 02.

**Achado:** o objetivo da a02 promete explicitamente "**estimar a perda de solo pela USLE/RUSLE**", e a alegação `GEOAMB-M08-A02-USLE-004` registra a equação. Mas nenhuma seção do Conteúdo apresentava a USLE. Ela aparecia pela primeira vez **dentro do enunciado do exemplo trabalhado**, já na forma de cinco valores numéricos — `R = 6500`, `K = 0,035`, `LS = 2,1`, `C = 0,12`, `P = 1,0` — sem que nenhum dos cinco fatores tivesse sido nomeado, definido ou dimensionado em qualquer ponto anterior. O recap então listava a fórmula como se ela tivesse sido ensinada.

O efeito prático é severo: o aluno consegue reproduzir a multiplicação (é aritmética) e **não consegue fazer nada mais** com a equação — não sabe o que cada fator representa, de onde sai, qual é manipulável nem qual é dado do sítio. A única afirmação interpretativa que o texto oferecia sobre os fatores ("a cobertura vegetal é o fator sobre o qual a intervenção tem maior efeito") chegava sem base, porque o aluno não tinha como saber que `C` é cobertura.

Agravante de clareza: a a02 usa `K` para **erodibilidade da USLE**, enquanto as aulas 01, 03, 04 e 06 usam `K` para **condutividade hidráulica**. A colisão é herdada das duas literaturas e é inevitável, mas sem uma seção que apresentasse a USLE não havia lugar algum onde o aluno fosse avisado dela — ele encontrava `K = 0,035` logo depois de uma aula inteira em que `K` valia `1×10⁻⁹ m/s`.

**Correção aplicada:** ✅ acrescentada a seção **"Quantificar a perda de solo: USLE e RUSLE"** antes da classificação de Varnes, definindo os cinco fatores um a um (com faixas típicas de `R` para o Brasil úmido e de `C` entre solo nu e floresta), nomeando a relação da RUSLE com a USLE e — o ponto que dá sentido à conclusão do exemplo — organizando os fatores por **manipulabilidade**: `R` e `LS` são dados do sítio, `K` muda lentamente, `C` e `P` são as alavancas de intervenção. A colisão de símbolo está avisada no ponto exato (`"aqui K não é condutividade hidráulica"`), e repetida no enunciado do exemplo, onde cada valor passou a vir rotulado. Recap e `mapa_objetivo_secao` atualizados.
**Efeito colateral aceito:** a a02 passou de ~1900 para ~2060 palavras. Ver a ressalva de extensão abaixo — é a melhor troca disponível, porque um objetivo não ensinado é defeito de outra ordem que uma aula longa.

---

### 🟡 [DID-M08-A02/A04/A05/A06-EXTENSAO] — Quatro aulas acima do teto de ~1900 palavras — ressalva justificada, sem corte

**Aulas:** 02 (~2060), 04 (~2010), 05 (~2050), 06 (~1990).

**Nota de medição, antes do achado.** Há divergência entre as duas contagens disponíveis, e ela muda o tamanho do problema. Pelo campo `palavras_corpo` declarado pelo redator, quatro aulas excedem o teto de ~1900 entre 5 % e 8 %. Por contagem independente feita nesta revisão (tokens alfanuméricos entre "## Conteúdo" e "## Próxima aula"), os números são: a01 = 1468, a02 = 2074, a03 = 1503, a04 = 1738, a05 = 1923, a06 = 1658 — isto é, **só a a02 excede claramente o teto, e a a05 o tangencia**. A diferença sistemática (~15 %) entre as duas contagens vem do método de tokenização, não de discordância sobre o texto.

Registro a divergência em vez de escolher a contagem que me convém. A leitura prudente é a do redator, e é sobre ela que decido; mas o leitor deste relatório deve saber que, pela medida independente, o desvio é bem menor do que os metadados sugerem, e que **a única aula inequivocamente longa é a a02** — justamente aquela cujo excedente eu mesmo introduzi para fechar o defeito 🟠 acima.

**Achado e decisão.** Seguindo o precedente registrado no Módulo 40 para a a14, **registro ressalva justificada em vez de enxugar**, e explico o motivo caso a caso, porque a origem do excedente é diferente em cada uma:

- **a02 (~2060).** O excedente é integralmente a seção de USLE acrescentada nesta revisão. Cortá-la reabriria o defeito 🟠 acima. **Não cortar.**
- **a04 (~2010).** O excedente está na parte (c) do exemplo trabalhado, que é onde a aula demonstra o resultado menos intuitivo do tema: o liner composto supera a **soma** das duas barreiras porque a interação entre elas confina o vazamento sob cada furo, e não porque as resistências hidráulicas se somem em série. Esse é o conceito que a aula existe para ensinar, e a auditoria acabou de **alongar** essa parte para tornar a ordem de grandeza verificável pelo aluno. Cortar aqui é cortar a tese. **Não cortar.**
- **a05 (~2050).** O excedente está no exemplo trabalhado, reescrito pela auditoria, e na ressalva sobre Fundão. O exemplo é o item que o hub do módulo nomeia como o ponto de dificuldade central ("a resistência não drenada de um material contrátil pode ser uma fração pequena da drenada, e é essa diferença que separa 'estável' de 'já rompeu'"). Já enxuguei o que dava: removi um parágrafo de interpretação que duplicava um item de "Erros comuns" e comprimi a ressalva de Fundão à metade. O que restou é carga irredutível. **Não cortar mais.**
- **a06 (~1990).** Excedente marginal (~5 %), inteiramente nos Passos 2 e 4 do exemplo de zona de captura, que a auditoria corrigiu e que agora ensinam o afunilamento do envelope — a ideia que decide o dimensionamento. **Não cortar.**

**Encaminhamento.** Nenhuma das quatro é candidata a quebra em partes: pelo pior dos dois critérios de contagem o excedente é de 5–8 %, não de 30 %, e em três delas está concentrado no exemplo trabalhado, que é o fecho da aula — o ponto em que o aluno já está com o modelo montado e a leitura acelera. Fica o registro para monitoramento: **se o usuário relatar que o módulo pesou, a candidata natural a quebra é a a05**, cortando entre "Tecnologias que reduzem a água livre" e "Liquefação", porque a segunda metade é conceitualmente autônoma e é a mais densa do módulo inteiro. A a02, embora seja a mais longa pelas duas contagens, **não** é boa candidata a quebra: suas partes (erosão, USLE, movimentos de massa, retroanálise) só fazem sentido como um percurso único do processo superficial ao processo profundo.

**Recomendação de manutenção, fora do escopo deste módulo:** os campos `palavras_corpo` do curso são preenchidos por um método de contagem que difere do usado pelos revisores em ~15 %. Vale padronizar o contador em algum ponto, porque hoje o teto de ~1900 significa coisas diferentes conforme quem mede.

---

### 🟡 [DID-M08-A02-ACOPLAMENTO-002] — A a02 é a aula menos acoplada do módulo, e o texto quase não a amarra

**Aula:** 02.

**Achado:** as seis aulas formam uma cadeia bem articulada, com uma exceção. A a02 é a única cujo objetivo (`oa02`) é coberto por ela sozinha, e é a única cujo conteúdo próprio quase não é consumido adiante: nem a USLE, nem a classificação de Varnes, nem os solos dispersivos, nem a retroanálise reaparecem nas aulas 03 a 06. O único elo declarado é uma frase ao fim da tabela de Varnes ("a expansão lateral em material que se liquefaz é o elo com a Aula 05"), e ele é fraco — a a05 não retoma Varnes ao explicar liquefação.

Isso **não é um defeito de sequenciamento**: a a02 responde a um objetivo de aprendizagem legítimo e autônomo do módulo (condicionantes de erosão e movimentos de massa), e sua posição inicial é correta, porque ela dá o vocabulário de estabilidade de talude que a a05 usa sem reensinar. Mas o aluno pode atravessá-la sem perceber por que ela está ali, e sem transferir nada dela para o resto.

**Correção aplicada — parcial, e deliberadamente contida:** ✅ o único reforço aplicado foi indireto, pela auditoria: a a05 passou a citar explicitamente "o modelo de talude infinito do Módulo 07, Aula 03" e a usar a **mesma formulação** que a a02 aplica, o que torna as duas aulas verificavelmente coerentes e dá ao aluno um ponto de transferência real (`τ = γsat·z·sen β·cos β`) em vez de uma menção genérica. Não fui além disso: acrescentar amarrações retóricas na a02 aumentaria a extensão de uma aula que já estourou o teto, e o problema não é grave o bastante para justificar.
**Encaminhamento à avaliação:** o questionário deve compensar essa fragilidade de acoplamento cobrando pelo menos uma questão que **atravesse** a a02 e a a05 — tipicamente pedindo que o aluno reconheça a liquefação de rejeito como um caso da mesma mecânica de poropressão/tensão efetiva que deflagra escorregamentos rasos.

---

## Verificações por critério

### Salto de pré-requisito
Nenhum salto interno encontrado. Cada aula tem "Antes de começar, você precisa saber" com o que retoma e de onde, e as retomadas são reais, não decorativas: a a01 retoma Darcy, Proctor e retardação; a a02 retoma o talude infinito do M07 e o efeito da poropressão do M06; a a04 retoma o tripé da a01 e o `Cα` do M06; a a05 retoma contração/dilatância e drenado × não drenado do M06; a a06 retoma LNAPL/DNAPL e atenuação natural do M03. Os dois pré-requisitos formais do módulo (M06 e M03) são genuinamente usados, e o hub explica em callout o que vem de cada um — nenhum aluno vai procurar uma dependência que não existe.

Uma correção da auditoria melhorou este critério diretamente: a fórmula de retardação, que aparecia nas duas seções de retomada com notação diferente da do Módulo 03, foi harmonizada. Retomada com notação divergente é pior que nenhuma retomada, porque faz o aluno duvidar se é a mesma fórmula.

### Conceitos novos por aula
Dentro do limite, com a a05 a vigiar. A a05 introduz rejeito × estéril, segregação praia/lama, três métodos de alteamento, três tecnologias de desaguamento, liquefação cíclica × estática, resistência liquefeita, quatro instrumentos de monitoramento, faixas de `FS` e descaracterização — mais dois estudos de caso. É a aula mais densa do módulo por margem confortável. A carga é gerenciável porque a organização é consistente (cada bloco responde "o que é / por que é perigoso / o que se faz") e porque o exemplo trabalhado final amarra tudo numa única conta; mas é a candidata a quebra registrada acima.

A a06 é a segunda mais densa (nove técnicas de remediação em tabela, três eixos de classificação, quatro resíduos como material geotécnico). Aqui a tabela é a decisão didática certa: nove técnicas em prosa seriam ilegíveis, e a tabela permite consulta posterior, que é como esse conteúdo é realmente usado na prática.

### Objetivo declarado vs. seções que de fato ensinam
Conferido o `mapa_objetivo_secao` das seis aulas contra o conteúdo real. **Uma falha encontrada e corrigida** (a USLE na a02, achado 🟠 acima). As demais correspondem.

Observação de balanceamento: o `oa03` é coberto por três aulas (a03, a04, a05) e o `oa02` e o `oa04` por uma cada. Isso reflete corretamente o peso do tema — disposição de resíduos e rejeitos é o núcleo do módulo — e nenhum objetivo fica subatendido, mas precisa ser levado em conta na distribuição das questões para que `oa02` e `oa04` não fiquem sub-representados.

### Exemplo trabalhado: suficiência e posicionamento
As seis aulas têm exemplo numérico, todos posicionados após o desenvolvimento teórico completo. Três merecem destaque:

- O da **a01** é o mais bem construído do módulo. Ele não calcula uma vazão e para: converte a vazão em **tempo de trânsito** (9 anos para a água, 27 para um soluto com `R = 3`) e, na interpretação, mostra que dobrar `K` por incompatibilidade química cortaria todos os tempos pela metade "sem que nenhuma verificação puramente hidráulica ou mecânica tivesse acusado o problema". Em um só exemplo o aluno vê por que o alvo de `K` é aquele, por que a barreira não é impermeável, e por que o ensaio de compatibilidade existe. É a justificativa numérica do tripé inteiro.
- O da **a04** é comparativo e termina com uma inversão de expectativa útil: depois de calcular a fuga pelo fundo, mostra que ela é pequena frente ao lixiviado que a drenagem precisa **coletar e tratar** — "o gargalo operacional de um aterro bem construído é o tratamento do lixiviado captado, não o vazamento pelo fundo". Isso desmonta a intuição de que a barreira é o problema central.
- O da **a05** ficou **mais forte depois da correção da auditoria**. Com os números errados, o contraste era `FS = 2,9` ("folga confortável") contra `0,47`. Com os números corretos, é `FS = 1,56` — que **passa** no critério regulamentar de 1,5 — contra `0,25`. A lição deixou de ser "a conta drenada é otimista" e passou a ser "a estrutura atende à norma e está liquefeita", que é exatamente o que aconteceu nos dois casos brasileiros que a aula discute. Vale registrar como caso em que uma correção factual melhorou a pedagogia em vez de apenas preservá-la.

O da **a03** merece nota à parte por ensinar algo que não é geotecnia: a matriz de decisão vence pelo peso, e a interpretação explica **por que** os critérios hidrogeológicos pesam 0,55 — "um substrato argiloso é uma segunda barreira geológica que se ganha de graça e dura tanto quanto a geologia; um lençol raso não se rebaixa de forma permanente e barata". Ensina a distinguir o que a engenharia compensa do que ela não compensa, que é a competência real da seleção de áreas.

### Analogias e risco de modelo mental errado
O módulo mantém o padrão consolidado no curso de preferir **avisos nomeados** a analogias soltas, colocados no ponto de vulnerabilidade: "os três planos competem" (a01), "estabilizar uma voçoroca só na superfície" (a02), "confundir resíduo com rejeito no sentido da PNRS" (a03), "a escolha da cobertura é climática antes de ser geotécnica" (a04), "achar que liquefação zera a resistência" (a05), "o bombeamento e tratamento raramente atinge a meta sozinho" (a06).

Duas explicações merecem elogio por ensinarem o **mecanismo** e não o resultado. Na a01, "por que se compacta no ramo úmido" explica a estrutura floculada × dispersa em vez de mandar decorar a regra — e, o que é melhor, fecha dizendo que é "o mesmo ensaio de Proctor lido com objetivos opostos", o que reorganiza retroativamente o que o aluno aprendeu no Módulo 06. Na a04, a cobertura evapotranspirativa é definida por contraste funcional ("não barra a água — administra o seu tempo de residência"), o que impede a leitura errada mais provável, a de que é uma barreira mais barata.

Um item novo entrou nesta revisão e merece registro: a advertência de que o `K` da USLE não é o `K` de condutividade hidráulica. Colisão de símbolo entre subáreas é uma fonte silenciosa de confusão, e o custo de avisar é uma linha.

Nenhuma analogia identificada carrega modelo mental que precise de correção não sinalizada pela própria aula.

### Redundância e sobrecarga cognitiva
O tripé da a01 reaparece nas aulas 03, 04, 05 e 06, mas cada retomada o aplica a uma pergunta diferente (onde construir; como construir; o que acontece quando o plano mecânico domina; como desfazer), com generalização progressiva e não repetição — mesmo padrão de fio condutor que a revisão do Módulo 06 elogiou na tensão efetiva.

Um par de conceitos vizinhos é tratado com a redundância certa: **resíduo × rejeito** (sentido da PNRS) na a03 e **rejeito × estéril** (sentido da mineração) na a05. A palavra "rejeito" tem dois significados técnicos distintos em duas aulas do mesmo módulo, e as duas aulas definem o seu por contraste, cada uma em "Erros comuns". A distinção é feita duas vezes de propósito, e é o tipo de redundância que se justifica.

Ponto de atenção real: as faixas de `FS` de projeto aparecem na a02 (taludes permanentes) e na a05 (barragens de rejeito), com valores iguais (1,5 drenado, 1,3 não drenado). A repetição é legítima porque os contextos regulatórios diferem — a a05 remete à classe de risco da ANM —, mas o aluno pode lê-la como redundância pura. Não corrigi: apontar a diferença exigiria um parágrafo em duas aulas já longas, e o custo do mal-entendido é baixo.

### Recap que recapitula
Os recaps das seis aulas cobrem os pontos efetivamente desenvolvidos, sem introduzir fato novo nem omitir conceito central, e retomam as **fórmulas** centrais e não apenas as conclusões qualitativas — apropriado para um módulo com seis exemplos numéricos. Os da a04 e da a05 têm seis itens em vez dos cinco habituais, proporcional à extensão dessas aulas.

Três recaps foram atualizados nesta rodada para não descolarem do corpo corrigido: o da a02 (fatores da USLE, abandono da classe "complexo" por Hungr et al., piping como uma das duas causas dominantes), o da a01 (norma de compatibilidade por material) e o da a06 (as duas larguras da zona de captura). Recap que sobrevive intacto a uma correção do corpo é recap que não estava recapitulando.

### Dificuldade proporcional à posição no curso
O módulo é o oitavo do curso avançado e o quarto da sub-área de geotecnia, com M06 e M07 já cursados. A curva interna é crescente em integração: a01 e a02 são de caracterização e diagnóstico; a03 introduz decisão sob critérios múltiplos; a04 exige encadear balanço hídrico, Darcy e recalque; a05 exige escolher entre condições de análise **antes** de calcular — a decisão de mais alto nível do módulo — e a06 exige selecionar tecnologia em função de três variáveis acopladas. A ordem está correta, e a a05 está no lugar certo: tarde o bastante para que o aluno já tenha o tripé e a mecânica de talude, cedo o bastante para que a a06 possa fechar com remediação.

A transição do M07 (cartografia, escala regional) para o M08 (obra, escala de projeto) é feita sem descontinuidade porque a a02 e a a03 explicitamente reutilizam a maquinaria do M07 — talude infinito, suscetibilidade × risco, sobreposição ponderada em SIG — aplicada agora a um sítio, e não a um município.

### Desalinhamento aula ↔ avaliação
**Não verificável nesta rodada:** questionários e flashcards do módulo ainda não foram gerados — este relatório é o gate que os precede. A verificação de alinhamento deve ser refeita depois da geração. Deixo registradas três restrições que a avaliação precisa respeitar, todas derivadas do que as aulas efetivamente ensinam:

1. **Não cobrar traçado de rede de fluxo nem modelagem HELP.** A a04 ensina a **interpretar** um balanço hídrico e a saber o que o HELP faz; não ensina a operá-lo. Questão que peça saída de HELP está fora do que foi ensinado.
2. **Não cobrar dimensionamento estrutural de barragem.** A a05 ensina a **comparar** condições de análise e a entender por que o método de montante é proibido; não ensina a projetar alteamento.
3. **Cobrar os números corrigidos.** O exemplo da a05 mudou (`τ = 61,0 kPa`, `FS = 1,56` e `0,25`) e o da a06 ganhou a distinção entre largura assintótica e largura na linha do poço. Questão baseada nos valores antigos estaria errada.

---

## Decisão sobre questionários: **PARCIAIS (2 + 1 final cumulativo)**

Registro a avaliação feita, por ser o segundo módulo de **seis** aulas do curso e, portanto, aplicação direta do critério fixado no Módulo 06: *acionar parciais quando houver corte conceitual natural; manter questionário único quando as aulas formarem bloco indivisível*.

**Decisão: acionar parciais.** Há corte conceitual natural, e ele não é uma divisão pela metade por conveniência aritmética:

- **Parcial 1 — aulas 01 a 03: caracterizar e decidir onde.** As três respondem a perguntas de diagnóstico e de escolha de sítio. A a01 caracteriza o material e a barreira; a a02 caracteriza os processos que o terreno impõe; a a03 classifica o resíduo e escolhe o lugar. Nenhuma delas constrói nada. Os exemplos trabalhados confirmam o recorte: tempo de trânsito, perda de solo e retroanálise, matriz de seleção de área — todos de avaliação, nenhum de dimensionamento.
- **Parcial 2 — aulas 04 a 06: projetar, operar e reparar.** A a04 dimensiona o aterro; a a05 dimensiona e monitora a estrutura de rejeito; a a06 repara o que vazou. Os exemplos são de projeto: balanço hídrico e fuga, `FS` drenado × não drenado, zona de captura.

O corte cai entre a a03 e a a04, exatamente na fronteira profissional entre **viabilidade e licenciamento** (onde se escolhe o sítio) e **projeto executivo** (onde se dimensiona a obra) — um limite que existe na prática da área, e não apenas na estrutura do texto.

Três razões adicionais sustentam a decisão:

1. **Ponto de verificação antes da a05.** A a05 é a aula mais difícil do módulo e depende criticamente do tripé da a01 e da mecânica de talude da a02. Um aluno que erre a parcial 1 deve rever tensão efetiva e poropressão **antes** de tentar liquefação — mesmo argumento que o Módulo 06 usou para posicionar sua parcial 1 antes da a05 daquele módulo.
2. **Extensão.** Quatro das seis aulas excedem o teto de palavras. Um questionário único cobrindo os quatro objetivos exigiria cerca de vinte questões numa sessão só, o que transforma autoavaliação em prova de resistência — o mesmo argumento registrado no Módulo 06.
3. **Objetivos.** `oa02` (só a02) cai inteiro na parcial 1 e `oa04` (só a06) inteiro na parcial 2, o que garante que os dois objetivos de aula única não fiquem diluídos.

**Instrução ao gerador de questionários.** Dois objetivos **atravessam** o corte: `oa01` (a01 e a04) e `oa03` (a03, a04 e a05). As parciais cobrem cada lado; é o **final cumulativo** que precisa carregar as questões de integração — em especial (a) o tripé da a01 aplicado ao liner composto da a04, e (b) a cadeia completa classificar → selecionar sítio → dimensionar barreira → monitorar, que atravessa a03–a05. Incluir também pelo menos uma questão ligando a a02 à a05 pelo mecanismo comum de poropressão e tensão efetiva, para compensar o baixo acoplamento da a02 registrado no achado 🟡 acima.

---

## Pontos fortes a preservar

- O **tripé hidráulico–mecânico–químico** como ferramenta fabricada na a01 e consumida por todas as demais, com o plano químico — o menos óbvio dos três — reaparecendo tanto na contenção (a04) quanto na remediação (a06). É a decisão didática mais valiosa do módulo e atinge diretamente a dificuldade que o hub previu.
- O exemplo da **a01**, que converte condutividade em **tempo** e depois mostra a sensibilidade a `K`: justifica numericamente, num só lugar, o alvo de projeto, a não impermeabilidade da barreira e a existência do ensaio de compatibilidade.
- A **inversão de expectativa** no fecho do exemplo da a04 (o gargalo é tratar o lixiviado coletado, não o vazamento pelo fundo), que reordena a intuição do aluno sobre onde está o problema de um aterro.
- O contraste **`FS` regulamentar × `FS` real** da a05, que depois da correção da auditoria mostra uma estrutura que atende à norma e está liquefeita — a lição exata dos dois casos brasileiros que a aula discute.
- A palavra **"rejeito"** definida por contraste duas vezes, em dois sentidos técnicos diferentes (PNRS na a03, mineração na a05), cada uma em "Erros comuns". Tratamento correto para um homônimo técnico dentro de um mesmo módulo.
- A interpretação da matriz da **a03**, que ensina a distinguir o que a engenharia compensa (volume, acesso) do que ela não compensa (geologia, lençol) — competência transferível para muito além de aterros.

## Recomendação

**Aprovar o módulo para avaliação e memorização.** Uma correção didática foi aplicada (o ensino da USLE na a02, que fechava um objetivo declarado sem seção correspondente). Ficam registradas, para monitoramento e não como impedimento: a extensão de quatro aulas 5–8 % acima do teto, com a justificativa caso a caso e a a05 identificada como única candidata a quebra futura; e o baixo acoplamento da a02 ao resto do módulo, a ser compensado por uma questão de integração no final cumulativo.

**Questionários: parciais (a01–a03 e a04–a06) mais final cumulativo**, conforme o critério fixado no Módulo 06 e detalhado acima.
