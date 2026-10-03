# Auditoria científica — Módulo 22: Modelagem geológica 3D

**Data do levantamento:** 2026-09-19 · **Correções aplicadas em:** 2026-09-19
**Modo:** `audit-and-fix` · **Profundidade:** `full`
**Escopo:** as 5 aulas do módulo, auditadas em conjunto, mais o hub do módulo · **passagem pontual em 2026-09-19** sobre o claim `GEOMOD3D-M22-A05-ASSIMETRIATESTE-007`, emitido após esta auditoria pela divisão didática

> **Nota posterior, acrescentada em 2026-09-19 pela revisão didática — nenhum achado deste relatório foi reaberto, renumerado ou revertido.**
> A revisão didática dividiu a **Aula 04** (achado `DID-M22-A04-CARGA-001`), e o módulo passou de 5 para 6 aulas. Onde este relatório diz:
> · **a04** → hoje é o **par a04 + a05**. Ficaram na **nova a04**: as quatro famílias geométricas, a síntese e a tabela — ou seja, os achados 🔴 1, 🟠 2, 🟠 3 e 🟠 4. Ficou na **nova a05**: a seção sobre o modelo como teste da interpretação metalogenética.
> · **a05** (estudos de caso e incerteza, achados azuis B21) → hoje é a **a06**, com o arquivo renomeado e o ID alterado para `geologia-avancado-m22-a06`.
> Os `claim_id` **não** foram renumerados: os prefixos `A04` e `A05` designam a numeração em que cada alegação foi emitida.
>
> **Uma propagação faltante deste relatório foi encontrada e corrigida pela revisão didática.** O achado 🟠 3 (`GEOMOD3D-M22-A04-ZONEAMENTOPORFIRO-005`) havia sido aplicado na seção sobre pórfiros, na tabela e no Recap, mas **não** na seção metalogenética da mesma aula, que continuava descrevendo "o zoneamento **concêntrico** de alteração hidrotermal num pórfiro" e "resfriamento e queda de pressão **radialmente** decrescentes a partir de um corpo intrusivo central". O trecho foi corrigido na atual Aula 05 para a descrição já verificada contra Sillitoe (2010) — zoneamento predominantemente vertical, assinatura de um fluido que evolui ao subir e resfriar. **Nenhum fato novo foi introduzido**; a correção apenas estendeu a este trecho a formulação que o achado 🟠 3 já havia estabelecido. Ver `DID-M22-A05-ZONEAMENTORESIDUAL-004` em `22-modelagem-geologica-3d-revisao-didatica.md`.

> **Segunda nota posterior, 2026-09-19 — passagem pontual sobre um único claim. A auditoria NÃO foi reaberta nem refeita.**
> A revisão didática deixou uma pendência explícita: `GEOMOD3D-M22-A05-ASSIMETRIATESTE-007` nasceu **depois** desta auditoria, durante a divisão da aula, e por isso nunca foi verificado. Esta passagem auditou **só ele**. Resultado: **núcleo verificado** (achado azul **B22**), com **duas correções** aplicadas — 🟠 **14** (a assimetria não é uniforme entre os três testes, e o texto contradizia o próprio corpo da aula) e 🟡 **15** (a justificativa estava creditada à Aula 03, que argumenta outra coisa). Ambas **corrigidas na mesma passagem**; nenhuma ficou em aberto. O `risk` da alegação foi **mantido** como `interpretacao`, deliberadamente — ver a nota ao fim da seção de achados. **O gate do módulo continua liberado.**

**Veredito:** **aprovado — gate liberado.** 0 achados vermelhos e 0 laranjas **em aberto**. Os 15 achados numerados (1 vermelho, 6 laranjas, 8 amarelos) foram **todos corrigidos cirurgicamente** — 13 na passagem principal, 2 na passagem pontual sobre o claim `ASSIMETRIATESTE-007`. Nenhum achado branco (⚪) foi levantado: o módulo é qualitativo, mas as afirmações que faz são de classificação e de atribuição de método, não de posições em disputa. **Questionário e flashcards liberados**, observadas as restrições ao fim deste relatório.

## Contagem por severidade

| Severidade | Contagem | Situação |
|---|---|---|
| 🔴 Vermelho (afirmação factualmente falsa) | **1** | **corrigido** |
| 🟠 Laranja (impreciso, inconsistência interna, confusão de escopo, omissão que gera erro) | **6** | **corrigidos** (5 na passagem principal + 1 na pontual) |
| 🟡 Amarelo (desatualização, atribuição de fonte errada, referência bibliográfica incorreta) | **8** | **corrigidos** (7 na passagem principal + 1 na pontual) |
| 🔵 Azul (verificado e correto — registro de que foi checado) | **22** | sem alteração (são registros de verificação bem-sucedida) |
| ⚪ Branco (questão aberta na literatura) | **0** | — |

> **Nota sobre as contagens:** os números da coluna "Contagem" são os do levantamento e não mudam — um achado não se apaga ao ser corrigido, ele muda de situação.

**Alegações rastreadas:** as 19 `alegacoes_auditaveis` declaradas pelas aulas (4 na a01, 4 na a02, 4 na a03, 4 na a04, 3 na a05) foram verificadas uma a uma; a auditoria levantou mais 7, chegando a **26 alegações rastreadas**. A divisão didática acrescentou 1 alegação nova (`GEOMOD3D-M22-A05-ASSIMETRIATESTE-007`) e a passagem pontual que a auditou levantou mais 2 (`-ASSIMETRIAUNIFORME-010` e `-ATRIBUICAOA03-011`): **29 alegações rastreadas no total, nenhuma não verificada.** As 7 novas foram gravadas nos blocos de metadados das aulas ou neste manifesto: `GEOMOD3D-M22-A01-SKUAVENDOR-005`, `GEOMOD3D-M22-A02-PREREQCOKRIGAGEM-005`, `GEOMOD3D-M22-A03-FOLDFRAME-005`, `GEOMOD3D-M22-A03-TERMODOMINIO-006`, `GEOMOD3D-M22-A04-ZONEAMENTOPORFIRO-005`, `GEOMOD3D-M22-A04-NICUEGPGEOMETRIA-006`, e o par bibliográfico `GEOMOD3D-M22-FONTES-CALCAGNO2008-007` / `GEOMOD3D-M22-FONTES-LAURENT2016-008` / `GEOMOD3D-M22-FONTES-MALLET1992-009`.

**Exemplos trabalhados:** os cinco foram examinados. Nenhum deles é aritmético — o módulo é conceitual, e os exemplos pedem classificação, escolha de estratégia e crítica de modelo. Os cinco estão logicamente corretos. O da **a04** recebeu um ajuste de coerência decorrente do laranja 2 (a expressão "volume equidimensional de 600 m de diâmetro" contradizia o próprio enunciado, que descreve o corpo descendo a 1.000 m).

---

## Padrão dominante

**A VERSÃO QUE CIRCULA, NÃO A FONTE QUE SE CITA.** Este módulo repete uma assinatura específica: em cinco dos seis achados mais caros, a aula enuncia **o modelo de manual que todo mundo repete** e credita a afirmação a **uma fonte moderna que diz outra coisa**. Não é que o autor tenha inventado — é que ele escreveu de memória o que "se sabe" sobre o assunto e anexou a referência certa do tema, sem conferir se a referência sustenta aquela formulação. Os três casos mais nítidos:

1. **Zoneamento de alteração de pórfiro** (🟠 3). A aula escreve os anéis concêntricos potássica → fílica → argílica → propilítica e cita **Sillitoe (2010)**. Esse é o modelo de **Lowell e Guilbert (1970)**. Sillitoe 2010 descreve o zoneamento como **empilhado verticalmente**, de baixo para cima, com propilítica distal e profunda — e é exatamente por isso que a síntese de 2010 existe.
2. **Geometria do pórfiro** (🟠 2). A aula escreve "equidimensional a cônica" e cita Sillitoe (2010), que abre dizendo que os sistemas são **verticalmente alongados (>3 km)** e que a forma do corpo segue a forma do *stock*.
3. **Tratamento de falha em modelagem implícita** (🟠 5). A aula descreve o fluxo de **blocos de falha** do Leapfrog como se fosse "o tratamento padrão", cita **Laurent et al. (2016)** — que é um artigo sobre **dobras** — e a fonte que de fato trata de falhas no campo potencial, **Calcagno et al. (2008)**, descreve o mecanismo oposto (descontinuidade inserida **dentro** de um único campo, não partição em blocos).

O corolário para o módulo 23 e seguintes: quando a aula for qualitativa e o autor estiver em terreno familiar, a atribuição de fonte é o ponto de falha, não o conteúdo. O conteúdo "soa certo" porque é o que circula; a fonte é o que denuncia que ele não é mais o consenso.

Um segundo padrão, menor mas relevante para o curso inteiro: **o módulo consumiu um pré-requisito que o curso nunca ensinou** (🟠 6). O Módulo 20 declara a cokrigagem, em texto explícito, fora do seu escopo; a Aula 02 deste módulo a listou como pré-requisito vindo dali. Esse é o tipo de achado que só aparece auditando contra os arquivos do próprio curso, e vale repetir a checagem nos módulos seguintes.

---

## Achados

### 🔴 1. Depósitos tipo Mississippi Valley classificados como estratiformes e concordantes com o acamamento

**claim_id:** `GEOMOD3D-M22-A04-GEOMETRIAESTRATIFORME-003`
**Tipo:** erro factual (classificação)
**Onde:** a04 · seção "Depósitos estratiformes e estratabound: sedimentares e vulcanogênicos"
**Está escrito:** "Depósitos **estratiformes** (concordantes com o acamamento, como muitos depósitos sedimentares de cobre ou de chumbo-zinco tipo Mississippi Valley) e **estratabound** (confinados a uma unidade estratigráfica específica, mas não necessariamente perfeitamente concordantes, como muitos depósitos vulcanogênicos maciços de sulfetos, VMS)..."
**Problema:** a frase define corretamente os dois termos e então **coloca o MVT do lado errado**. Depósitos tipo Mississippi Valley são o exemplo de livro-texto de **estratabound**, e a literatura de referência é explícita no ponto: eles são "discordant on a deposit scale but stratabound on a district scale". O minério se aloja em brechas de colapso, cavidades de dissolução cárstica e corpos que cortam dezenas de metros da sucessão carbonática — o oposto de "concordante com o acamamento". **Por que é vermelho e não laranja:** não é imprecisão de grau. A aula constrói, na mesma frase, uma distinção terminológica formal e aloca o exemplo na categoria errada dessa distinção. Um flashcard gerado sobre essa frase ensinaria "MVT = estratiforme", que é falso, e o aluno levaria isso para qualquer leitura posterior de geologia econômica. É também o tipo de erro que contamina o Módulo 42 (avaliação de recursos), que retoma tipologia de jazida.
**Correção aplicada:** a seção foi reescrita para abrir com a distinção terminológica explícita (estratiforme = o corpo é uma camada; estratabound = confinado a uma unidade sem ser necessariamente concordante nela), realocar o MVT em estratabound com a justificativa geológica (brechas de colapso e dissolução, discordância em escala de depósito), manter o cobre sedimentar como exemplo genuíno de estratiforme (Kupferschiefer, Cinturão do Cobre da Zâmbia) e acrescentar que o VMS é estratabound por um segundo motivo — a zona de *stockwork* alimentadora, francamente discordante.
**Fonte:** Leach, D. L. & Sangster, D. F. (1993), "Mississippi Valley-type lead-zinc deposits", em Kirkham, Sinclair, Thorpe & Duke (eds.), *Mineral Deposit Modeling*, Geological Association of Canada Special Paper 40, 289-314 · **Nível:** revisada por pares / obra de referência
**Confiança:** confirmado
**Também aparece em:** a04 · tabela "Síntese: geometria como critério de decisão" (linha corrigida) e a04 · Recap relâmpago (item corrigido). Não aparece em outras aulas do módulo.

### 🟠 2. Geometria do pórfiro descrita como "equidimensional a cônica", com "funil invertido" internamente contraditório, atribuída a Sillitoe (2010)

**claim_id:** `GEOMOD3D-M22-A04-GEOMETRIAPORFIRO-002`
**Tipo:** impreciso + inconsistência interna
**Onde:** a04 · seção "Depósitos disseminados e em stockwork: pórfiros"
**Está escrito:** "A geometria resultante é aproximadamente **equidimensional a cônica** (frequentemente descrita como um 'funil' invertido, mais largo perto da superfície e afunilando em profundidade), com dimensões que podem chegar a centenas de metros a poucos quilômetros de diâmetro."
**Problema:** três defeitos empilhados. (a) **A descrição não é a da fonte citada.** Sillitoe (2010) caracteriza os sistemas porfiríticos como organizados por *stocks* e enxames de diques "vertically elongate (>3 km)", e afirma que "ore-zone geometries depend mainly on the overall form of the host stock or dike complex", com *stocks* cilíndricos hospedando corpos cilíndricos. "Equidimensional" contradiz o alongamento vertical que é a primeira coisa que a fonte diz. (b) **"Funil invertido" contradiz a própria glosa entre parênteses:** um funil invertido é estreito em cima e largo embaixo; a glosa descreve "mais largo perto da superfície e afunilando em profundidade", que é um funil na posição normal. (c) **Contradição interna com o resto do módulo:** o exemplo trabalhado da própria a04 e o Estudo de caso 2 da a05 descrevem um pórfiro de 600 m de diâmetro descendo a 1.000 m de profundidade — verticalmente alongado, não equidimensional.
**Correção aplicada:** o parágrafo foi reescrito para (i) ancorar a forma do corpo na forma da intrusão hospedeira, como a fonte faz; (ii) afirmar o alongamento vertical (>3 km para o sistema) e restringir "aproximadamente equidimensional" **à planta**; (iii) substituir "funil invertido" pela descrição que a literatura usa para o casco de minério — sino ou taça invertida encapando um núcleo de teor mais baixo; e (iv) tornar explícito o erro a evitar ("não ler equidimensional em planta como equidimensional em três dimensões"), amarrando ao exemplo trabalhado. A frase do exemplo trabalhado que dizia "volume equidimensional de 600 m de diâmetro" foi ajustada por coerência local.
**Fonte:** Sillitoe, R. H. (2010), "Porphyry copper systems", *Economic Geology*, 105(1), 3-41, DOI 10.2113/gsecongeo.105.1.3 · **Nível:** revisada por pares (síntese de referência da classe)
**Confiança:** confirmado
**Também aparece em:** a04 · tabela de síntese (linha corrigida), a04 · Recap (item corrigido), a04 · Exemplo trabalhado (coerência local corrigida). A a05 herda o número do exemplo, e passou a ficar **consistente** com a a04 após a correção — não precisou de edição.

### 🟠 3. Zoneamento de alteração de pórfiro apresentado como anéis concêntricos em planta, creditado a Sillitoe (2010)

**claim_id:** `GEOMOD3D-M22-A04-ZONEAMENTOPORFIRO-005` *(alegação nova, levantada pela auditoria)*
**Tipo:** desatualização com atribuição de fonte errada + omissão que gera erro
**Onde:** a04 · seção "Depósitos disseminados e em stockwork: pórfiros"
**Está escrito:** "usando os halos de alteração hidrotermal concêntricos característicos de pórfiros — potássica no núcleo, seguida de fílica, argílica e propilítica em direção às bordas — como domínio geométrico auxiliar"
**Problema:** essa é, literalmente, a sequência coaxial de **Lowell e Guilbert (1970)**, construída sobre San Manuel–Kalamazoo. A fonte citada pela aula, **Sillitoe (2010)**, descreve o zoneamento de outra forma: a sequência principal é **empilhada verticalmente**, de baixo para cima — sódico-cálcica, potássica, clorita-sericita, sericítica e argílica avançada —, com a **propilítica desenvolvida distalmente em níveis profundos** e a clorítica distalmente em níveis rasos; a argílica avançada forma um *lithocap* raso que pode exceder 1 km de espessura, e em sistemas telescopados os tipos rasos se sobrepõem aos profundos. **Por que não é apenas uma nota de rodapé histórica:** a aula usa esses halos como **domínio geométrico auxiliar de modelagem**. Quem monta domínios de alteração assumindo anéis concêntricos em planta vai interpolar superfícies com a orientação errada num sistema cujo zoneamento real é sobretudo vertical — o erro sai da nomenclatura e entra na geometria do modelo, que é justamente o objeto deste módulo.
**Correção aplicada:** acrescentada uma ressalva nomeada ("Uma ressalva sobre o zoneamento de alteração, porque ela muda o que se modela") que apresenta o modelo de Lowell e Guilbert (1970) **como modelo histórico**, apresenta a descrição de Sillitoe (2010) como a vigente, e fecha com a consequência prática para a construção de domínios. O trecho no corpo do parágrafo original foi reduzido a "halos de alteração hidrotermal característicos de pórfiros", sem a sequência, para não antecipar a versão errada.
**Fonte:** Sillitoe, R. H. (2010), *Economic Geology*, 105(1), 3-41 · Lowell, J. D. & Guilbert, J. M. (1970), "Lateral and vertical alteration-mineralization zoning in porphyry ore deposits", *Economic Geology*, 65(4), 373-408, DOI 10.2113/gsecongeo.65.4.373 · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** a04 · Recap (item corrigido, com a sequência vertical e a atribuição histórica explícitas). A a03 menciona "o domínio de alteração potássica tem suscetibilidade magnética consistentemente mais alta que o domínio de alteração propilítica" — **verificado e mantido**: é uma afirmação sobre contraste petrofísico entre dois domínios, não sobre a disposição geométrica deles, e continua válida sob o zoneamento vertical. A a05 fala em "domínio de alteração potássica" sem descrever zoneamento — não precisou de edição.

### 🟠 4. Toda a classe Ni-Cu-EGP magmática alocada na família equidimensional/pipe, incluindo os depósitos de recife, que são estratiformes

**claim_id:** `GEOMOD3D-M22-A04-NICUEGPGEOMETRIA-006` *(alegação nova, levantada pela auditoria)*
**Tipo:** confusão de escopo
**Onde:** a04 · seção "Depósitos maciços e em pipe: magmáticos e de brecha"
**Está escrito:** "Um quarto grupo geométrico compreende corpos aproximadamente **equidimensionais** ou em **pipe** (chaminé subvertical), característicos de depósitos magmáticos de níquel-cobre-EGP (elementos do grupo da platina) associados a intrusões máficas-ultramáficas..."
**Problema:** a afirmação é verdadeira para os depósitos de **conduto** (chonolitos e diques em lâmina — Noril'sk, Voisey's Bay, Jinchuan) e de **contato basal**, e **falsa para os depósitos de recife**, que são exatamente os depósitos de EGP arquetípicos de intrusões máficas-ultramáficas acamadadas. O Merensky e o UG2 no Bushveld e o J-M no Stillwater são corpos **estratiformes**, com espessura de centímetros a poucos metros e continuidade lateral de dezenas a centenas de quilômetros: o J-M tem 1 a 8 m de espessura e foi rastreado por 40 km. É a geometria **oposta** à da família em que a aula os colocou, e a estratégia de modelagem que ela implica também é oposta — superfície estratigráfica, não sólido compacto. O achado importa duplamente porque o **Módulo 33 deste curso é "Intrusões acamadadas"**: deixar passar aqui cria a contradição transversal que a auditoria `cross-course` teria de resolver depois.
**Correção aplicada:** a seção foi reescrita para nomear explicitamente os subtipos que pertencem à família pipe (conduto e contato basal, com exemplos), e acrescentado um parágrafo "O que não entra aqui, apesar de também ser Ni-Cu-EGP magmático" que realoca os depósitos de recife na família estratiforme, com as dimensões corretas, fechando com o princípio: a classe genética não determina a geometria sozinha, o mecanismo de alojamento determina. Tabela de síntese e Recap sincronizados.
**Fonte:** Naldrett, A. J. (2004), *Magmatic Sulfide Deposits: Geology, Geochemistry and Exploration*, Springer Berlin Heidelberg, DOI 10.1007/978-3-662-08444-1 · Zientek, M. L. (2012), "Magmatic ore deposits in layered intrusions — Descriptive model for reef-type PGE and contact-type Cu-Ni-PGE deposits", *U.S. Geological Survey Open-File Report* 2012-1010 · **Nível:** obra de referência + publicação de serviço geológico
**Confiança:** confirmado
**Também aparece em:** a04 · tabela de síntese (linha "controlada por estratigrafia" passou a incluir os recifes de EGP; linha "pipe" passou a dizer "de conduto e de contato basal"), a04 · Recap (dois itens corrigidos).

### 🟠 5. Tratamento de falha em modelagem implícita apresentado como procedimento padrão único, conflitando duas famílias de solução e contradizendo a fonte que de fato trata do assunto

**claim_id:** `GEOMOD3D-M22-A03-FALHASCOMOPARTICAO-001`
**Tipo:** impreciso + certeza indevida (apresenta como "o padrão" algo que é uma de duas escolhas de implementação)
**Onde:** a03 · seção "Atributos estruturais: falhas, dobras e a orientação como dado"
**Está escrito:** "O tratamento padrão de uma falha num fluxo de modelagem implícita segue uma lógica de duas etapas: 1. A falha é modelada primeiro [...] 2. **O campo potencial das unidades estratigráficas é então calculado separadamente em cada bloco delimitado pela falha**, com um deslocamento (rejeito) aplicado entre os blocos [...] e depois são costurados de volta considerando o deslocamento relativo."
**Problema:** dois defeitos. (a) **Não é "o padrão", é uma de duas famílias.** A descrição corresponde ao fluxo de **blocos de falha** adotado em pacotes comerciais de mineração (Leapfrog e outros). A outra família, e a que está na fonte canônica do próprio método do campo potencial que a aula ensinou na a02, é a de **Calcagno et al. (2008)**, implementada no GeoModeller: "faults are modelled using the same method by **inserting discontinuities in the potential field**" — o campo continua sendo **um só** sobre o volume inteiro, e a falha interrompe a correlação espacial através do plano. Apresentar a primeira como "o padrão" contradiz diretamente a fonte que a aula 02 usa para fundamentar o método. (b) **O "rejeito aplicado e depois costurado de volta" descreve um terceiro mecanismo**, de campos de deslocamento de falha, que não é o que nenhuma das duas famílias faz: no fluxo de blocos, cada bloco é modelado com os seus próprios dados e o deslocamento é **consequência**, não parâmetro de entrada.
**Correção aplicada:** a seção foi reescrita para (i) manter o que é comum às duas famílias — a falha é sempre modelada antes; (ii) apresentar as duas famílias numeradas, cada uma com a sua fonte e o seu mecanismo; (iii) remover a afirmação sobre rejeito aplicado e costura; e (iv) acrescentar por que a distinção importa para quem **audita** um modelo — na família de blocos, um bloco com poucos furos fica muito pior que o vizinho sem que nada no modelo denuncie isso, o que amarra o ponto ao fio condutor de incerteza da a05. Recap e Fontes sincronizados.
**Fonte:** Calcagno, P., Chilès, J. P., Courrioux, G. & Guillen, A. (2008), *Physics of the Earth and Planetary Interiors*, 171(1-4), 147-157 · Caumon, G. et al. (2009), *Mathematical Geosciences*, 41(8), 927-945 · documentação pública da Seequent sobre modelagem de sistemas de falha e blocos de falha no Leapfrog · **Nível:** revisada por pares + documentação de fornecedor (para o fluxo comercial)
**Confiança:** confirmado
**Também aparece em:** a03 · Recap (item corrigido), a03 · Fontes (duas referências acrescentadas), a02 · seção "Alternativas ao campo potencial" (ver 🟡 8).

### 🟠 6. Cokrigagem declarada pré-requisito vindo do Módulo 20, que a declara explicitamente fora do seu escopo

**claim_id:** `GEOMOD3D-M22-A02-PREREQCOKRIGAGEM-005` *(alegação nova, levantada pela auditoria)*
**Tipo:** inconsistência interna do curso (salto de pré-requisito não declarado)
**Onde:** a02 · linha de pré-requisito e seção "A ligação com a geoestatística"
**Está escrito:** "**Pré-requisito:** [...] e Módulo 20 (krigagem e **cokrigagem** — o método do campo potencial desta aula é, na prática, uma cokrigagem aplicada a um problema geométrico)."
**Problema:** o Módulo 20 tem cinco aulas (preparação de dados, variáveis regionalizadas, suporte/relação de Krige/anisotropia, variografia, krigagem simples e ordinária) e **não ensina cokrigagem em nenhuma delas**. Mais do que isso: a Aula 01 do Módulo 20 diz, em texto literal e no bloco de alegações auditáveis, que explorar a relação entre duas variáveis "é objeto da **cokrigagem, fora do escopo deste módulo**". A a02 deste módulo então apoia o conceito central da aula — a equivalência do campo potencial com uma cokrigagem — num pré-requisito que o curso declarou não ter dado. O aluno que seguir a sequência chega na seção "A ligação com a geoestatística" sem ter a definição de cokrigagem em lugar nenhum.
**Correção aplicada:** (i) a linha de pré-requisito foi corrigida para citar do Módulo 20 o que ele de fato ensina (variografia, covariância espacial e krigagem) e passou a **declarar o degrau explicitamente**, avisando que a cokrigagem está fora do escopo do M20 e que esta aula a define; (ii) a seção "A ligação com a geoestatística" recebeu a definição de cokrigagem que faltava — generalização da krigagem a duas ou mais variáveis correlacionadas estimadas em conjunto, exigindo uma covariância cruzada além da covariância de cada uma —, seguida da observação de que, no campo potencial, as duas variáveis não são independentes (uma é a derivada da outra) e a covariância cruzada decorre da covariância do potencial; (iii) o Recap foi sincronizado com a definição.
**Fonte:** verificação interna contra `20-geoestatistica/20-geoestatistica-aula-01-preparacao-dados-estatistica-descritiva.md` (claim `GEOEST-M20-A01-CORRELACAOESPACIAL-005`) e contra a lista de aulas do Módulo 20 · definição de cokrigagem: Chilès, J.-P. & Delfiner, P. (2012), *Geostatistics: Modeling Spatial Uncertainty*, 2ª ed., Wiley, cap. 5 · Goovaerts, P. (1997), *Geostatistics for Natural Resources Evaluation*, Oxford University Press, cap. 6 · **Nível:** obra de referência
**Confiança:** confirmado
**Também aparece em:** a02 · Recap relâmpago (item corrigido). Encaminhado à revisão didática como achado de pré-requisito, não só factual.

### 🟡 7. Título incorreto de Calcagno et al. (2008)

**claim_id:** `GEOMOD3D-M22-FONTES-CALCAGNO2008-007` *(alegação nova, levantada pela auditoria)*
**Tipo:** referência bibliográfica incorreta
**Onde:** a02 · Fontes, e bloco `alegacoes_auditaveis` (`GEOMOD3D-M22-A02-CAMPOPOTENCIAL-002`)
**Está escrito:** "Geological modelling from field data and geological knowledge: Part I. **Modelling method coupled to a potential field**"
**Problema:** o título real é "Geological modelling from field data and geological knowledge: Part I. **Modelling method coupling 3D potential-field interpolation and geological rules**". O restante da referência (autores, periódico, volume, fascículo, páginas 147-157) está correto. A parte suprimida do título — "and geological rules" — não é decorativa: é ela que aponta para a metade do artigo que trata de regras geológicas e relações de falha, e é essa metade que sustenta a correção do achado 🟠 5.
**Correção aplicada:** título corrigido nas duas ocorrências, e a glosa da referência em a02 ampliada para mencionar o tratamento de falhas. A referência foi também **acrescentada à a03**, onde passou a ser a fonte primária do achado 🟠 5.
**Fonte:** registro do artigo em ScienceDirect (*Physics of the Earth and Planetary Interiors*, 171(1-4), 147-157) · **Nível:** normativa (registro do editor)
**Confiança:** confirmado
**Também aparece em:** a02 · bloco de alegações (source de `GEOMOD3D-M22-A02-CAMPOPOTENCIAL-002` e de `-004`), a03 · Fontes (referência acrescentada).

### 🟡 8. Laurent et al. (2016) creditado com o tratamento de redes de falha e com a partição do campo em blocos

**claim_id:** `GEOMOD3D-M22-FONTES-LAURENT2016-008` *(alegação nova, levantada pela auditoria)*
**Tipo:** atribuição de fonte errada
**Onde:** a02 · seção "Alternativas ao campo potencial" e Fontes; a03 · `source` da alegação `GEOMOD3D-M22-A03-FALHASCOMOPARTICAO-001` e Fontes
**Está escrito:** (a02) "Métodos mais recentes (por exemplo, Laurent et al., 2016) estendem o campo potencial para tratar explicitamente dobras superpostas **e redes de falhas complexas**" · (a02, Fontes) "(extensão do campo potencial a dobras superpostas **e redes de falha complexas**)" · (a03) a mesma referência listada como fonte de "tratamento de falhas como partição do campo em blocos"
**Problema:** Laurent et al. (2016), "Implicit modeling of folds and overprinting deformation", *EPSL* 456, 26-38, trata de **dobras e deformação superposta**, e não de redes de falha. O artigo constrói um referencial de dobra (*fold frame*) a partir de elementos estruturais observáveis e descreve a geometria dobrada por ângulos de rotação, expressos como funções 1D das coordenadas do referencial. A citação errada aparece em **duas aulas** e, na a03, era a **única** fonte oferecida para uma afirmação que o achado 🟠 5 mostrou estar ela mesma errada — a fonte falsa mascarava o erro de conteúdo.
**Correção aplicada:** em a02, a frase foi dividida — Laurent et al. (2016) para dobras e deformação superposta, com a descrição correta do mecanismo (*fold frame* sobre superfície axial e eixo de dobra), e falhas encaminhadas a Calcagno et al. (2008) e Caumon et al. (2009), com remissão à Aula 03. A glosa da referência em Fontes passou a dizer, em texto, que **o artigo não trata de redes de falha**, para que a correção não se perca numa reescrita futura. Em a03, o `source` da alegação foi substituído pelas fontes corretas e a referência Laurent recebeu a mesma glosa.
**Fonte:** Laurent, G., Ailleres, L., Grose, L., Caumon, G., Jessell, M. & Armit, R. (2016), *Earth and Planetary Science Letters*, 456, 26-38, DOI 10.1016/j.epsl.2016.09.040 · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** a02 · bloco de alegações (`GEOMOD3D-M22-A02-ALGORITMOSALTERNATIVOS-004`, corrigido com a ressalva explícita).

### 🟡 9. SKUA-GOCAD atribuído à Emerson — desde maio de 2022 o produto é da AspenTech

**claim_id:** `GEOMOD3D-M22-A01-SKUAVENDOR-005` *(alegação nova, levantada pela auditoria)*
**Tipo:** desatualização
**Onde:** a01 · seção "Panorama de softwares comerciais e livres" e bloco de alegações
**Está escrito:** "**SKUA-GOCAD** (Emerson, produto herdado da Paradigm, adquirida pela Emerson em 2019)"
**Problema:** a aquisição da Paradigm pela Emerson em 2019 está correta, mas não é o estado atual. Em **16 de maio de 2022**, na conclusão da transação entre a Emerson e a AspenTech, a Emerson transferiu à AspenTech os negócios OSI e **Geological Simulation Software**, do qual o SKUA-GOCAD faz parte. O produto é hoje comercializado como **Aspen SKUA**, dentro da suíte Subsurface Science & Engineering da AspenTech. Numa aula cujo objetivo declarado é "mapear o panorama de softwares", o fornecedor errado é o dado que envelhece mais rápido e que o aluno vai checar primeiro.
**Correção aplicada:** entrada reescrita com a cadeia completa e datada (Paradigm → Emerson 2019 → AspenTech 2022, produto hoje Aspen SKUA na suíte Subsurface Science & Engineering), preservando a menção à Emerson porque é o nome sob o qual o produto circulou por três anos e ainda aparece na literatura. Nova alegação auditável criada e referência acrescentada em Fontes.
**Fonte:** AspenTech (2022), comunicado "AspenTech Completes Emerson Transaction", 16 de maio de 2022 · página de produto Aspen SKUA (AspenTech) · **Nível:** normativa (comunicado corporativo oficial)
**Confiança:** confirmado
**Também aparece em:** a01 · Recap relâmpago — **verificado e não alterado**: o Recap cita "SKUA-GOCAD" sem fornecedor, e continua correto.

### 🟡 10. Início do projeto GOCAD datado como "nos anos 1990"

**claim_id:** `GEOMOD3D-M22-A01-GOCADORIGEM-003`
**Tipo:** valor apresentado incorretamente
**Onde:** a01 · seção "Panorama de softwares comerciais e livres" e bloco de alegações
**Está escrito:** "GOCAD nasceu como projeto acadêmico na Ecole Nationale Supérieure de Géologie, em Nancy, na França, **nos anos 1990**"
**Problema:** o projeto Gocad foi **iniciado em 1989** por Jean-Laurent Mallet e seu grupo de pesquisa; a publicação de referência que a aula cita (Mallet, 1992) é posterior ao início do projeto, e o método de interpolação suave discreta que o sustenta foi formulado em 1989. A instituição (ENSG, Nancy) está correta.
**Correção aplicada:** data corrigida para "iniciado em 1989", com a atribuição nominal a Mallet e seu grupo acrescentada, e a alegação auditável atualizada.
**Fonte:** página institucional do RING Team (Université de Lorraine), histórico do projeto Gocad · Mallet, J.-L. (1989), "Discrete smooth interpolation", *ACM Transactions on Graphics*, 8(2), 121-144 · **Nível:** institucional + revisada por pares
**Confiança:** confirmado
**Também aparece em:** nenhum outro arquivo.

### 🟡 11. "Vergência" listada como elemento incorporado pela formulação de dobra de Laurent et al. (2016)

**claim_id:** `GEOMOD3D-M22-A03-FOLDFRAME-005` *(alegação nova, levantada pela auditoria)*
**Tipo:** atribuição de fonte errada (parâmetro inexistente na formulação citada)
**Onde:** a03 · seção "Atributos estruturais: falhas, dobras e a orientação como dado"
**Está escrito:** "incorporando explicitamente a geometria da dobra (**eixo, plano axial, vergência**) como estrutura adicional do campo"
**Problema:** eixo e superfície axial estão certos; **vergência não é um elemento do referencial de dobra** de Laurent et al. (2016). A formulação constrói o *fold frame* sobre a superfície axial e o eixo da dobra e descreve a geometria dobrada por **ângulos de rotação** — o do eixo de dobra dentro da superfície axial e o da foliação dobrada em relação a ela —, expressos como funções 1D das coordenadas do referencial. Substituir os ângulos de rotação por "vergência" troca o parâmetro que o método efetivamente ajusta por um descritor estrutural qualitativo que ele não usa.
**Correção aplicada:** lista substituída pela descrição correta — referencial de dobra construído sobre superfície axial e eixo da dobra, geometria descrita por ângulos de rotação, com os dois ângulos nomeados. Nova alegação auditável criada, registrando explicitamente que vergência não é um dos elementos. Recap da a03 sincronizado.
**Fonte:** Laurent, G. et al. (2016), *Earth and Planetary Science Letters*, 456, 26-38 · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** a03 · Recap (item corrigido); a02 · seção de alternativas, onde a descrição do mecanismo foi acrescentada na mesma correção (ver 🟡 8).

### 🟡 12. Referência de Mallet (1992) com título do livro grafado errado e sem volume nem páginas; fonte primária do DSI ausente

**claim_id:** `GEOMOD3D-M22-FONTES-MALLET1992-009` *(alegação nova, levantada pela auditoria)*
**Tipo:** referência bibliográfica incorreta / incompleta
**Onde:** a01 · Fontes; a02 · Fontes
**Está escrito:** "em Turner, A. K. (ed.), *Three-Dimensional **Modelling** with Geoscientific Information Systems*, NATO ASI Series, Kluwer"
**Problema:** o título do volume usa a grafia americana, *Three-Dimensional **Modeling** with Geoscientific Information Systems*; a referência é NATO ASI Series vol. **354**, e o capítulo ocupa as páginas **123-141**. Além disso, as duas aulas creditam a Mallet (1992) a **formulação** da interpolação suave discreta; o capítulo de 1992 descreve o programa GOCAD e usa o DSI, mas o método é formulado em **Mallet (1989)**, *ACM Transactions on Graphics*, 8(2), 121-144. Um aluno que fosse procurar a matemática do DSI no capítulo de 1992 não a encontraria na forma original.
**Correção aplicada:** referência corrigida nas duas aulas (grafia do título, volume da série, intervalo de páginas, editora Kluwer/Springer Dordrecht) e a fonte primária de 1989 acrescentada como remissão, nas Fontes e nos blocos de alegações.
**Fonte:** registro do capítulo em Springer Nature Link, DOI 10.1007/978-94-011-2556-7_11 · **Nível:** normativa (registro do editor)
**Confiança:** confirmado
**Também aparece em:** a01 e a02 · blocos `alegacoes_auditaveis` (`GEOMOD3D-M22-A01-GOCADORIGEM-003` e `GEOMOD3D-M22-A02-ALGORITMOSALTERNATIVOS-004`).

### 🟡 13. Grafia do termo técnico definido "domínio" no corpo da a03

**claim_id:** `GEOMOD3D-M22-A03-TERMODOMINIO-006` *(alegação nova, levantada pela auditoria)*
**Tipo:** nomenclatura (grafia de termo técnico definido)
**Onde:** a03 · seção "Atributos geoquímicos: do domínio geométrico ao bloco populado"
**Está escrito:** "funciona como um **código de dominio geológico rígido ou suave**"
**Problema:** "dominio" sem acento, num trecho em **negrito** que introduz formalmente a terminologia herdada do Módulo 21 ("domínio rígido / domínio suave"). O termo destacado é exatamente o que o gerador de flashcards lê como frente de card e o que o gerador de questionários usa como chave de resposta — um termo destacado com grafia errada se propaga direto para o material derivado.
**Correção aplicada:** grafia corrigida para "domínio".
**Fonte:** consistência interna com `21-modelagem-geoestatistica-depositos-minerais-aula-06-*.md`, onde o termo é definido · **Nível:** interna
**Confiança:** confirmado
**Também aparece em:** nenhum outro ponto — as demais ocorrências de "domínio" nas cinco aulas estão corretas.

---

> **Passagem pontual de 2026-09-19 (posterior à divisão didática) — os achados 14 e 15 abaixo foram levantados DEPOIS dos treze acima.**
> Eles auditam a única alegação do módulo que nunca havia passado pela auditoria: `GEOMOD3D-M22-A05-ASSIMETRIATESTE-007`, emitida pela revisão didática ao dividir a antiga Aula 04 e marcada, na ocasião, como candidata a verificação futura. **Nenhum achado de 1 a 13 foi reaberto, renumerado ou revertido.** O escopo desta passagem foi um claim só.

### 🟠 14. Assimetria lógica atribuída em bloco aos três testes metalogenéticos, contradizendo o próprio corpo da aula

**claim_id:** `GEOMOD3D-M22-A05-ASSIMETRIAUNIFORME-010` *(alegação nova, levantada por esta passagem)*
**Tipo:** impreciso — inconsistência interna + confusão de escopo (propriedade válida para dois dos três casos, enunciada como válida para os três, com a mesma força e pelo mesmo motivo)
**Onde:** a05 · seção "O que cada teste pode e não pode concluir"; propagado para o Recap
**Está escrito:** "**nenhum dos três testes confirma uma hipótese metalogenética.** Todos os três têm a mesma assimetria lógica — são bons em produzir evidência **contra** uma hipótese, e fracos em produzir evidência a favor. // A razão é [...]: a coincidência geométrica entre duas coisas é fácil de obter e difícil de interpretar."
**Problema:** a **direção** da assimetria está certa para os três, mas a **medida** e a **razão** não. Os testes 1 (coerência corpo × caminho de transporte) e 3 (zoneamento × mecanismo de deposição) conferem a hipótese contra dado **já observado**: ali a coincidência geométrica é de fato barata, porque o corpo já está mapeado e várias hipóteses concorrentes o acomodam. O teste 2 (extrapolação para alvo **não perfurado**) é de outra natureza: não há coincidência a colher, porque não há dado no alvo — a hipótese é obrigada a **prever**. Pelo próprio critério que a aula invoca, o acerto de uma previsão arriscada, improvável diante do conhecimento prévio e que poderia conceivelmente ter falhado, é justamente o caso em que a evidência a favor **conta**. Pior: a aula **se contradiz**. Duas seções antes ela afirma que o teste 2 "tem uma propriedade que os outros dois não têm [...] é **caro de errar e barato de checar**" e que "é essa possibilidade de ter dado errado que dá valor ao teste" — que é a definição de previsão arriscada. O fechamento apaga a distinção que o corpo acabou de estabelecer. Consequência prática, e é o que torna isto 🟠 e não cosmético: um aluno que internalize "extrapolação não produz evidência a favor" perde o motivo pelo qual a geração de alvos é o produto mais valioso do modelo 3D em exploração, e passa a ler um furo de descoberta em alvo previsto como se fosse sorte.
**Correção aplicada:** a seção foi reescrita em três parágrafos — enunciado da assimetria como **não uniforme**; testes 1 e 3 com a justificativa da coincidência barata (que só a eles se aplica); teste 2 tratado à parte como previsão que poderia ter falhado, com a ressalva de que continua não sendo prova, porque outra hipótese pode prever o mesmo alvo. Recap sincronizado. O exemplo trabalhado (a) passou a dizer "pela assimetria **do teste 1** discutida acima", já que é do teste 1 que ele trata.
**Fonte:** Wei, X., Yin, Z., Bonner, W. & Caers, J. (2026), "Falsification of geological hypotheses using drillholes and geophysics", *Surveys in Geophysics*, 47, 289-315, DOI 10.1007/s10712-026-09936-9 — o dado independente entra como instrumento de **falsificação**, não de confirmação, e o artigo testa hipóteses de forma de corpo de sulfeto magmático de Ni-Cu, o mesmo tipo de objeto que a aula discute; critério popperiano de corroboração por previsão arriscada ("só conta como corroboração o resultado positivo de uma previsão genuinamente arriscada, que poderia conceivelmente ter sido falsa"; "previsões que se poderia fazer a partir do conhecimento prévio não testam uma teoria") · **Nível:** revisada por pares + princípio metodológico consolidado
**Confiança:** confirmado
**Também aparece em:** a05 · Recap relâmpago; a05 · bloco `alegacoes_auditaveis` (`GEOMOD3D-M22-A05-ASSIMETRIATESTE-007`, texto da alegação reescrito).

### 🟡 15. Justificativa da assimetria creditada à Aula 03, que argumenta outra coisa — e, num ponto, o contrário

**claim_id:** `GEOMOD3D-M22-A05-ATRIBUICAOA03-011` *(alegação nova, levantada por esta passagem)*
**Tipo:** atribuição de fonte errada (fonte interna)
**Onde:** a05 · seção "O que cada teste pode e não pode concluir"; campo `source` de `GEOMOD3D-M22-A05-ASSIMETRIATESTE-007`
**Está escrito:** "A razão é a que a **Aula 03 já apontou num contexto vizinho**: a coincidência geométrica entre duas coisas é fácil de obter e difícil de interpretar." — e, no metadado: "coerente com o tratamento de coincidência geométrica já dado na Aula 03 deste módulo (achado `GEOMOD3D-M22-A03-COERENCIAFALSA-004`)".
**Problema:** a Aula 03 não diz isso. O que ela diz (`COERENCIAFALSA-004`, achado azul **B19**) é que exigir coincidência **exata** entre um modelo geológico e um modelo de inversão é erro conceitual **porque os dois têm resoluções, fontes de incerteza e definições de "contato" diferentes por construção** — um argumento sobre incompatibilidade de resolução entre dois tipos de modelo, não sobre o peso probatório de uma coincidência. E, num ponto, a a03 afirma o oposto: "uma coincidência **aproximada reforça a confiança nos dois modelos**", e o exemplo trabalhado dela conclui que a diferença de 15 m "reforça, na verdade, a confiança de que existe um mesmo contato real sendo detectado pelos dois métodos independentes". Ou seja: a a03 trata coincidência aproximada entre métodos independentes como **confirmatória**. O que a a03 de fato empresta à a05, por analogia, é a **não unicidade** (`GEOMOD3D-M22-A03-INVERSAOCOMOMODELO3D-002`, azul **B17**) — que ali é não unicidade da solução de inversão e aqui vira não unicidade entre hipóteses metalogenéticas concorrentes. Este achado é a assinatura do módulo (**"a versão que circula, não a fonte que se cita"**) aplicada a uma **referência cruzada interna**: a remissão soa certa, e é a fonte apontada que denuncia que ela não sustenta a frase.
**Correção aplicada:** a remissão foi reescrita para apontar ao que a a03 realmente fornece e como analogia declarada — "a mesma **não unicidade** que a Aula 03 discutiu entre modelo geológico e modelo de inversão, reaparecendo agora entre hipóteses metalogenéticas concorrentes". O campo `source` da alegação deixou de invocar `COERENCIAFALSA-004` como apoio do argumento e passou a citá-lo apenas como **precedente do critério de `risk`** (ver abaixo). Alegação nova registrada com o que a a03 de fato afirma.
**Fonte:** texto da própria a03 (seções "Checagem de consistência posterior" e exemplo trabalhado) e os achados azuis B17 e B19 deste relatório · **Nível:** interna
**Confiança:** confirmado
**Também aparece em:** nenhum outro ponto — a a06 remete à a03 corretamente.

**Nota sobre o campo `risk` da alegação 007.** A pendência pedia que se avaliasse promover `risk: interpretacao` para outro valor agora que a alegação foi verificada. **Mantido como `interpretacao`, deliberadamente.** Verificar uma alegação diz que ela resiste ao escrutínio, não que ela mudou de natureza: isto continua sendo um princípio **metodológico**, não uma medida, uma classificação formal nem um fato observacional. É exatamente o critério que este mesmo relatório já elogiou em `GEOMOD3D-M22-A03-COERENCIAFALSA-004` (azul **B19**: "correto — e **corretamente declarado como interpretação** no `risk` da alegação, não como medida ou classificação formal"). Promovê-la a `fato` por ter passado na auditoria seria `certeza_indevida`. O que mudou não foi o `risk`: foi o `source`, que saiu de "síntese didática [...] sem fonte única primária" para uma ancoragem revisada por pares, e o `claim`, que ganhou a cláusula que faltava.

---

## Verificado e correto

Registros de verificação bem-sucedida. Não são achados; são a prova do que foi olhado.

| id | Aula | Alegação verificada | Veredito | Fonte |
|---|---|---|---|---|
| B1 | a01 | Distinção explícito/implícito: explícito = geólogo desenha a geometria (seções → *strings* → triangulação → wireframe); implícito = algoritmo interpola a superfície a partir de pontos de contato e atitudes (`GEOMOD3D-M22-A01-EXPLICITAIMPLICITA-001`) | correto | Caumon et al. (2009), *Math. Geosci.* 41(8), 927-945; Wellmann & Caumon (2018), *Adv. Geophys.* 59, 1-121 |
| B2 | a01 | Leapfrog construído sobre interpolação por funções de base radial; é dos pacotes mais usados para modelagem implícita na indústria mineral | correto | Cowan et al. (2003), 5th IMGC, 89-99; documentação Seequent (FastRBF) |
| B3 | a01 | Bentley Systems adquiriu a Seequent em 2021 | correto — **aquisição concluída em 17 de junho de 2021** | comunicado Bentley Systems de conclusão da aquisição |
| B4 | a01 | Datamine descrito como pacote britânico tradicional | correto | origem e sede da Datamine Software no Reino Unido (a propriedade atual, pelo grupo Constellation/Vela, não altera a origem descrita) |
| B5 | a01 | **Micromine descrito como australiano** | correto — **checado por risco de desatualização e confirmado que não houve mudança** | a AspenTech anunciou em jul/2022 a aquisição da Micromine, mas **rescindiu o acordo em agosto de 2023** por falta de aprovação regulatória; a empresa segue sediada em Perth. A entrada da aula não precisou de alteração. |
| B6 | a01 | Vulcan (Maptek, Austrália) entre os pacotes mais antigos do setor, forte em modelagem explícita por seção | correto | materiais institucionais Maptek |
| B7 | a01 | Petrel (SLB, antiga Schlumberger) como plataforma dominante de modelagem de reservatório | correto | a renomeação Schlumberger → SLB (2022) está corretamente registrada na aula |
| B8 | a01 | Move: Petroleum Experts adquiriu o software originalmente da Midland Valley | correto — **união em outubro de 2017** | materiais institucionais Petroleum Experts |
| B9 | a01 | GemPy: biblioteca Python de modelagem implícita do grupo de Geociência Computacional e Engenharia de Reservatórios da RWTH Aachen, publicada por de la Varga, Schaaf e Wellmann (2019), *GMD* 12(1), 1-32 (`GEOMOD3D-M22-A01-FERRAMENTASLIVRES-004`, parte) | correto, inclusive a afiliação e o volume | de la Varga, Schaaf & Wellmann (2019), DOI 10.5194/gmd-12-1-2019 |
| B10 | a01 | Loop3D: plataforma aberta de modelagem implícita probabilística de consórcio internacional incluindo a Monash University | correto — a Monash **lidera** o consórcio; iniciado por Geoscience Australia e OneGeology, com UWA, RING/Nancy e RWTH Aachen entre os parceiros | documentação pública do projeto Loop (loop3d.org); AuScope |
| B11 | a01 | SGeMS: software livre de Stanford, voltado primariamente à simulação geoestatística, mais do que à modelagem de superfícies geológicas completas | correto | Remy, Boucher & Wu (2009), *Applied Geostatistics with SGeMS*, Cambridge UP |
| B12 | a01 | Serviços geológicos nacionais (BRGM, Geological Survey of Canada) mantêm ou mantiveram programas de modelagem 3D regional a nacional | correto (a aula hedgeou com "por exemplo" e "mantêm ou já mantiveram", formulação que a evidência sustenta) | Wellmann & Caumon (2018), seção sobre cartografia 3D institucional |
| B13 | a02 | Tipos de dado de entrada: superfície 2D (mapas, MDE como limite superior, lineamentos) e subsuperfície 3D (furos com pontos de interface e orientação, seções, grades de inversão), com exigência de coordenadas e datum compartilhados (`GEOMOD3D-M22-A02-TIPOSDEDADO-001`) | correto | Wellmann & Caumon (2018), *Adv. Geophys.* 59, 1-121; Caumon et al. (2009) |
| B14 | a02 | Método do campo potencial: introduzido por Lajaunie, Courrioux & Manuel (1997), *Mathematical Geology* 29(4), 571-584; contato observado é isosuperfície do campo (mesmo valor nos pontos de interface); gradiente paralelo ao vetor normal dos dados de orientação, válido em qualquer ponto do volume (`GEOMOD3D-M22-A02-CAMPOPOTENCIAL-002`) | correto, inclusive volume, fascículo e páginas | Lajaunie et al. (1997); Calcagno et al. (2008) |
| B15 | a02 | Equivalência com cokrigagem entre o potencial e seu gradiente (`GEOMOD3D-M22-A02-EQUIVALENCIACOKRIGAGEM-003`) | correto — e **precisado**: a formulação é de **cokrigagem universal** (com deriva), detalhe acrescentado ao texto e à alegação | Lajaunie et al. (1997), seção de formulação matemática |
| B16 | a02 | Cowan, Beatson, Ross et al. (2003), "Practical implicit geological modelling", 5th International Mining Geology Conference, **Bendigo, 17-19 de novembro de 2003**, páginas 89-99 | correto em todos os campos | registro AusIMM da conferência |
| B17 | a03 | Modelo de inversão geofísica é ele próprio um modelo 3D, com resolução de dezenas a centenas de metros em levantamentos aéreos/de superfície, não unicidade da solução e representação de propriedade física contínua com transições suavizadas pela regularização (`GEOMOD3D-M22-A03-INVERSAOCOMOMODELO3D-002`) | correto | Oldenburg & Li (2005), *Near-Surface Geophysics*, SEG, cap. 5; consistente com M19 a06 |
| B18 | a03 | Inversão geologicamente restringida incorpora orientação estrutural na regularização, penalizando variação através de contatos modelados (`GEOMOD3D-M22-A03-INVERSAORESTRINGIDA-003`) | correto — o mecanismo descrito (matriz de rotação a partir de mergulhos locais alinhando a regularização à estrutura) é o do artigo | Lelièvre & Oldenburg (2009), *GJI* 178(2), 623-637 |
| B19 | a03 | Exigir coincidência geométrica exata entre modelo geológico e modelo de inversão é conceitualmente equivocado (`GEOMOD3D-M22-A03-COERENCIAFALSA-004`) | correto — e **corretamente declarado como interpretação** no `risk` da alegação, não como medida ou classificação formal | princípio metodológico consolidado; Lelièvre & Oldenburg (2009); Oldenburg & Li (2005) |
| B20 | a04 | Geometria tabular estreita e alongada de veios e zonas de cisalhamento mineralizadas de ouro orogênico, com sinuosidade e variação de espessura controladas pela estrutura hospedeira (`GEOMOD3D-M22-A04-GEOMETRIAVEIOS-001`) | correto; as faixas dimensionais citadas são conservadoras em relação à continuidade vertical de 1-2 km que a classe admite | Groves, Goldfarb, Gebre-Mariam, Hagemann & Robert (1998), *Ore Geol. Rev.* 13(1-5), 7-27 |
| B21 | a05 | As três fontes de incerteza (dado, interpretação, algoritmo) e a quantificação por realizações múltiplas, com a Bacia de Gippsland, sudeste da Austrália, como estudo de caso de Lindsay et al. (2012) (`-TRESFONTES-001`, `-REALIZACOESMULTIPLAS-002`, `-REALIZACOESGIPPSLAND-003`) | corretos os três, inclusive periódicos, volumes e páginas | Wellmann & Caumon (2018), *Adv. Geophys.* 59, 1-121; Wellmann & Regenauer-Lieb (2012), *Tectonophysics* 526-529, 207-216; Lindsay, Aillères, Jessell, de Kemp & Betts (2012), *Tectonophysics* 546-547, 10-27 |
| B22 | a05 | **Núcleo da alegação `GEOMOD3D-M22-A05-ASSIMETRIATESTE-007`**: os testes metalogenéticos viabilizados por um modelo 3D são logicamente assimétricos, produzindo evidência **contra** uma hipótese com mais força do que a favor, porque a coincidência geométrica entre o corpo e uma estrutura proposta é compatível com múltiplas hipóteses concorrentes, ao passo que um deslocamento sistemático é difícil de reconciliar com a hipótese testada — *verificado nesta passagem pontual de 2026-09-19, a única alegação do módulo que nunca havia sido auditada* | **correto — a assimetria é real, não é alegação forçada.** É o princípio de assimetria entre refutação e corroboração aplicado a um objeto geológico concreto, e a literatura recente o instancia exatamente neste domínio: Wei et al. (2026) montam um arcabouço bayesiano para **falsificar** hipóteses de forma de corpo mineralizado (sulfeto magmático de Ni-Cu) com furos e gravimetria/magnetometria, com o dado independente entrando como **instrumento de falsificação**, não de confirmação. A não unicidade que sustenta o lado fraco da assimetria é o fenômeno de incerteza conceitual documentado por Bond et al. (2007). **Duas ressalvas, tratadas como achados 🟠 14 e 🟡 15:** a assimetria não é uniforme entre os três testes (o teste 2 é previsão arriscada, não compatibilidade retrospectiva), e a justificativa estava mal creditada à a03. Corrigidas as duas, o núcleo se sustenta. `risk` **mantido** como `interpretacao` — ver a nota ao fim dos achados | Wei, Yin, Bonner & Caers (2026), *Surveys in Geophysics* 47, 289-315, DOI 10.1007/s10712-026-09936-9; Bond, Gibbs, Shipton & Jones (2007), *GSA Today* 17(11), 4-10; McCuaig & Hronsky (2014), *SEG Spec. Publ.* 18, 153-175; critério popperiano de corroboração por previsão arriscada |

---

## Correções aplicadas

**Aplicadas em:** 2026-09-19

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `GEOMOD3D-M22-A04-GEOMETRIAESTRATIFORME-003` | 🔴 | Corrigido | a04 (corpo, tabela, recap, alegação) |
| `GEOMOD3D-M22-A04-GEOMETRIAPORFIRO-002` | 🟠 | Corrigido | a04 (corpo, tabela, recap, exemplo trabalhado, alegação) |
| `GEOMOD3D-M22-A04-ZONEAMENTOPORFIRO-005` | 🟠 | Corrigido | a04 (corpo, recap, fontes, alegação nova) |
| `GEOMOD3D-M22-A04-NICUEGPGEOMETRIA-006` | 🟠 | Corrigido | a04 (corpo, tabela, recap, fontes, alegação nova) |
| `GEOMOD3D-M22-A03-FALHASCOMOPARTICAO-001` | 🟠 | Corrigido | a03 (corpo, recap, fontes, alegação) |
| `GEOMOD3D-M22-A02-PREREQCOKRIGAGEM-005` | 🟠 | Corrigido | a02 (pré-requisito, corpo, recap, alegação nova) |
| `GEOMOD3D-M22-FONTES-CALCAGNO2008-007` | 🟡 | Corrigido | a02 (fontes, alegações), a03 (fontes) |
| `GEOMOD3D-M22-FONTES-LAURENT2016-008` | 🟡 | Corrigido | a02 (corpo, fontes, alegação), a03 (fontes, alegação) |
| `GEOMOD3D-M22-A01-SKUAVENDOR-005` | 🟡 | Corrigido | a01 (corpo, fontes, alegação nova) |
| `GEOMOD3D-M22-A01-GOCADORIGEM-003` | 🟡 | Corrigido | a01 (corpo, alegação) |
| `GEOMOD3D-M22-A03-FOLDFRAME-005` | 🟡 | Corrigido | a03 (corpo, recap, alegação nova) |
| `GEOMOD3D-M22-FONTES-MALLET1992-009` | 🟡 | Corrigido | a01 (fontes, alegação), a02 (fontes, alegação) |
| `GEOMOD3D-M22-A03-TERMODOMINIO-006` | 🟡 | Corrigido | a03 (corpo) |
| `GEOMOD3D-M22-A05-ASSIMETRIAUNIFORME-010` | 🟠 | Corrigido *(passagem pontual)* | a05 (seção "O que cada teste pode e não pode concluir", recap, exemplo trabalhado, fontes, alegações) |
| `GEOMOD3D-M22-A05-ATRIBUICAOA03-011` | 🟡 | Corrigido *(passagem pontual)* | a05 (corpo, alegação `ASSIMETRIATESTE-007`, alegação nova) |
| `GEOMOD3D-M22-A05-ASSIMETRIATESTE-007` | 🔵 | **Verificado** (azul B22) — núcleo se sustenta; `risk` mantido como `interpretacao`, `source` e `claim` reescritos | a05 (bloco `alegacoes_auditaveis`, Fontes) |

**Pendências:** nenhuma. Nenhum achado ficou aguardando decisão do usuário. **A pendência deixada pela revisão didática — o claim `ASSIMETRIATESTE-007` nunca auditado — foi fechada em 2026-09-19.**

**Arquivos tocados:** as cinco aulas (`-aula-01-` a `-aula-05-`) — a a05 apenas por **verificação**, sem edição, já que as correções da a04 a tornaram consistente sem precisar alterá-la — mais o hub do módulo e o `course-state.yaml`. **Na passagem pontual de 2026-09-19**, um arquivo a mais: a atual `-aula-05-modelo-3d-teste-interpretacao-metalogenetica.md` (corpo, recap, exemplo trabalhado, Fontes e bloco `alegacoes_auditaveis`), além deste relatório, do `.json` e do `course-state.yaml`. A a04 e a a06 foram relidas nos trechos vizinhos e **não** precisaram de alteração — nenhuma delas repete a formulação da assimetria.

**Material derivado:** o módulo **não tinha** questionário, baralho de flashcards nem glossário no momento da auditoria. Não houve propagação a fazer, e **não há card já importado no Anki a corrigir à mão**.

---

## Restrições ao gerador de questionário e de flashcards

O gate está liberado, mas seis correções deste relatório mudaram o que é resposta certa. Nenhum item pode ser gerado contra as formulações antigas:

1. **MVT é estratabound, não estratiforme** (🔴 1). Não gerar item que classifique o Pb-Zn tipo Mississippi Valley como estratiforme ou concordante com o acamamento. Se a distinção estratiforme × estratabound virar questão — e é boa questão —, o MVT é o exemplo da **segunda** categoria, e o cobre sedimentar, da primeira.
2. **Pórfiro é equidimensional em planta, verticalmente alongado em 3D** (🟠 2). Não gerar item cuja resposta correta seja "geometria equidimensional" sem a qualificação "em planta", nem item que use "funil invertido".
3. **Zoneamento de alteração de pórfiro é empilhado verticalmente** (🟠 3). Não gerar item que cobre a sequência concêntrica potássica → fílica → argílica → propilítica **como descrição vigente**. Ela pode ser cobrada como **modelo histórico de Lowell e Guilbert (1970)**, contrastada com a descrição de Sillitoe (2010) — e essa é, inclusive, uma questão melhor.
4. **Ni-Cu-EGP não tem geometria única** (🟠 4). Não gerar item que associe "Ni-Cu-EGP magmático" a uma só geometria. Conduto e contato basal → pipe; recife (Merensky, UG2, J-M) → estratiforme.
5. **Falhas em modelagem implícita têm duas soluções, não uma** (🟠 5). Não gerar item cuja resposta correta seja "o padrão é calcular um campo por bloco de falha". A resposta certa contempla as duas famílias, e a distinção entre elas é matéria legítima de questão de aplicação.

6. **A assimetria dos três testes metalogenéticos NÃO é uniforme** (🟠 14). Não gerar item cuja resposta correta seja "os três testes são igualmente fracos para confirmar" ou "nenhum dos três produz evidência a favor". A resposta certa distingue: testes **1 e 3** conferem a hipótese contra dado já observado (coincidência barata, assimetria acentuada); teste **2** obriga a hipótese a prever um alvo ainda não perfurado — uma previsão que poderia ter falhado e, ao ser confirmada, vale como evidência a favor de um modo que a compatibilidade retrospectiva não vale. Essa distinção é **boa questão de aplicação** e vale ser cobrada diretamente, inclusive como dissertativa curta. Também **não** creditar à Aula 03 a tese de que "coincidência geométrica é evidência fraca" (🟡 15): a a03 diz que **exigir coincidência exata** entre modelo geológico e inversão é erro conceitual, e trata coincidência **aproximada** entre métodos independentes como **reforço** de confiança. O que a a03 empresta à a05 é a **não unicidade**.

Observação adicional: a **cokrigagem** passou a ser definida dentro da a02 (🟠 6) e pode ser cobrada; **não** a trate como conhecimento vindo do Módulo 20.

---

## Recomendação de formato do questionário

**Questionário único cumulativo, sem parciais.** O módulo tem 5 aulas, dentro do limiar de ~5-6 do plugin, e a progressão é linear e convergente (a05 integra explicitamente a01-a04), o que torna um corte em blocos artificial: qualquer parcial cortaria antes da síntese que é o ponto do módulo. Mesmo critério aplicado nos Módulos 20 e 21. Se a revisão didática dividir alguma aula e o módulo passar a 6, a recomendação **não muda** — 6 continua dentro do limiar, e uma divisão por carga cognitiva não cria corte conceitual novo.

Sugestão de composição, para o gerador: cobertura dos quatro objetivos de aprendizagem, com pelo menos duas questões de **integração** explícita — uma ligando geometria de depósito (a04) à escolha de algoritmo (a02), outra ligando incerteza de modelo (a05) à coerência geológico-geofísica (a03).

---

## Observações fora de escopo (didática, para o revisor-didatico)

1. **A a02 é a aula mais pesada do módulo e ficou mais pesada com esta auditoria.** Ela já declarava ~29 min e 2.180 palavras; a correção do 🟠 6 acrescentou a definição de cokrigagem, que é um conceito novo denso, e a do 🟡 8 ampliou o parágrafo de alternativas. É a primeira aula a olhar para uma eventual divisão em Parte 1 / Parte 2, com corte natural visível: dados de entrada e fluxo explícito numa parte; campo potencial, cokrigagem e comparação das abordagens na outra.
2. **A a04 também cresceu**, com três blocos novos (ressalva de zoneamento, distinção estratiforme/estratabound, exclusão dos recifes de EGP). Declarava ~28 min e 2.200 palavras. Segunda candidata a divisão.
3. **O salto de pré-requisito do 🟠 6 é tanto factual quanto didático.** A auditoria o corrigiu declarando e definindo; cabe ao revisor avaliar se a definição inserida basta ou se o conceito merece mais espaço.
4. **Nenhuma aula do módulo tem exemplo trabalhado aritmético.** É coerente com um módulo conceitual, mas destoa do padrão dos Módulos 20 e 21 e pode deixar o aluno sem prática de manipulação. Decisão do revisor.
5. **O mapeamento objetivo × aula não é 1:1**: `oa01` é coberto por a01 e a02, `oa02` por a02 e a03, `oa03` por a04 e a05, `oa04` por a03 e a05. Não é defeito — mas o gerador de questionário precisa cobrir cada objetivo a partir de mais de uma aula.
