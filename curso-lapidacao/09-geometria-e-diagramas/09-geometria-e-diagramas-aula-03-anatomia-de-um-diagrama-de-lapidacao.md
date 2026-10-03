# Aula 03: Anatomia de um diagrama de lapidação — as vistas, a tabela e a sequência

**ID:** lapidacao-m09-a03
**Módulo:** [[09-geometria-e-diagramas-modulo|Módulo 09]] — Geometria da máquina e leitura de diagramas de lapidação
**Duração estimada:** ~26 min
**Objetivo:** ler um diagrama de lapidação — vista de topo, vista lateral, tabela de ângulos e índices — e extrair dele a sequência de corte.
**Pré-requisito:** [[09-geometria-e-diagramas-aula-02-angulo-indice-e-altura-as-tres-coordenadas-da-faceta|Aula 02]] deste módulo (as três coordenadas de uma faceta); [[08-optica-do-facetado-aula-06-modelagem-optica-ray-tracing-e-os-limites-da-metrica|Aula 06 do módulo 08]] deste curso (o diagrama de lapidação como especificação de talhe, e o GemCad como a ferramenta mais citada para desenhá-lo). Nenhum pré-requisito específico do curso de Gemologia.

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **diagrama de lapidação** | a especificação completa de um talhe — vistas, tabela de coordenadas e nomenclatura de fileira — já definida no módulo 08, reativada aqui em detalhe. |
| **vista de topo (plan view)** | o desenho do contorno da pedra visto de cima, com a posição angular de cada faceta marcada ao redor dele. |
| **vista lateral (perfil)** | o desenho do contorno da pedra visto de lado, mostrando a inclinação das fileiras de facetas. |
| **fileira (tier)** | um grupo de facetas na mesma altura ao redor da pedra — na prática, o mesmo ângulo e a mesma altura do mastro —, numa mesma região: main, break, star, entre outras. |
| **main** | o conjunto de facetas grandes que vai da cinta à mesa na coroa, ou da cinta à culaça no pavilhão — as maiores da seção, não necessariamente as mais numerosas. |
| **P, C, G** | abreviações correntes para pavilhão, coroa e cinta (*girdle*), usadas para localizar em que metade da pedra uma fileira fica. |

## Antes de começar, você precisa saber

- Da [[09-geometria-e-diagramas-aula-02-angulo-indice-e-altura-as-tres-coordenadas-da-faceta|Aula 02]] deste módulo: toda faceta é definida por três coordenadas independentes — ângulo, índice, altura.
- Da [[08-optica-do-facetado-aula-06-modelagem-optica-ray-tracing-e-os-limites-da-metrica|Aula 06 do módulo 08]]: um **diagrama de lapidação** é a especificação de um talhe — ângulo e posição de índice de cada faceta — organizada num arquivo ou numa folha, independente de qualquer software específico; e o **GemCad** é a ferramenta mais citada para desenhá-lo.
- Do [[01-oficio-da-lapidacao-aula-02-anatomia-da-pedra-lapidada-e-nomenclatura-das-facetas|módulo 01, aula 02]]: mesa, coroa, cinta e pavilhão, e o nome geral das facetas.
- Não é preciso saber ainda a lógica do meetpoint como técnica de corte — é a aula 04.

## Ao final você vai conseguir

- `lapidacao-m09-oa03` — Ler um diagrama de lapidação — vista de topo, vista lateral, tabela de ângulos e índices — e extrair dele a sequência de corte.

## Conteúdo

### Uma planta baixa e um corte, para uma pedra

Um diagrama de lapidação resolve o mesmo problema que a planta de uma casa: descrever um objeto tridimensional em papel sem ambiguidade. A planta não usa uma vista só — usa uma vista de cima (onde fica cada cômodo) e um corte de lado (a altura de cada parede). O diagrama faz a mesma divisão: uma **vista de topo** para a posição de cada faceta ao redor da pedra, uma **vista lateral** para a inclinação de cada fileira, e uma **tabela** que amarra as duas aos números exatos.

### A vista de topo: o contorno e a posição angular

A **vista de topo**, ou *plan view*, mostra o contorno final da pedra visto de cima — o formato que a cinta vai ter — com cada faceta desenhada na posição angular em que ela fica ao redor do eixo. É nessa vista que a **simetria** do talhe aparece visualmente: um contorno redondo com oito raios igualmente espaçados denuncia simetria 8-fold, e é essa vista que diz que jogo de índice (aula 01) o talhe vai exigir — o número de dentes precisa ser divisível pelo número de posições que ela desenha. Ela também numera ou nomeia cada faceta, e é essa numeração que a tabela usa em cada linha.

### A vista lateral: o perfil e as fileiras

A **vista lateral**, ou perfil, mostra a pedra de lado: a altura da coroa, da cinta e do pavilhão, e a inclinação de cada **fileira** — o grupo de facetas na mesma altura ao redor da pedra, cortadas com o mesmo ângulo. É nessa vista que o vocabulário de fileira aparece: as facetas grandes que atravessam a seção inteira — da cinta à culaça no pavilhão, da cinta à mesa na coroa — formam a fileira **main**; fileiras adicionais, mais estreitas, recebem nomes como *break* (facetas que "quebram" entre a main e a cinta) ou *star* (uma coroa de facetas pequenas junto à mesa). Repare que "main" diz **tamanho**, não quantidade: num brilhante redondo há oito mains de pavilhão contra dezesseis facetas de cinta.

### A tabela: onde as coordenadas viram números

As duas vistas mostram forma; a **tabela** dá os números. Cada linha da tabela corresponde a um grupo de facetas — tipicamente uma fileira inteira, já que todas as facetas de uma mesma fileira compartilham o ângulo — e traz duas colunas centrais: **ângulo** (*mast angle*, nas tabelas em inglês) e **índice** (a posição, ou o conjunto de posições, dentro do jogo declarado). A terceira coordenada da aula 02 raramente vira coluna: a profundidade de cada corte é fixada na pedra pelo ponto de encontro, não lida de um número — é o que a aula 04 explica. Uma coluna extra indica a **localização** — P, C, G para pavilhão, coroa e cinta — e o nome da fileira. Uma tabela típica, simplificada, tem esta cara:

| Fileira | Localização | Ângulo | Índice (jogo de 96) | Nome |
|---|---|---|---|---|
| 1 | Pavilhão | 43° | 4, 12, 20, 28, 36, 44, 52, 60, 68, 76, 84, 92 | main |
| 2 | Cinta | — | — | girdle |
| 3 | Coroa | 34° | 4, 12, 20, 28, 36, 44, 52, 60, 68, 76, 84, 92 | main |
| 4 | Coroa | 20° | 0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88 | star |

Ler essa tabela é aplicar a aula 02 linha por linha: a fileira 1 declara doze facetas de pavilhão — mesmo ângulo, doze índices — numa linha só.

> **Ilustração pedida — um diagrama de lapidação completo.** Vista de topo com o contorno e os índices ao redor; vista lateral com as fileiras rotuladas (main, break, star); e, ao lado, a tabela, com uma seta ligando cada linha à fileira que ela descreve.

### A sequência: em que ordem a tabela é percorrida

Um diagrama não é lido de cima para baixo como um texto qualquer — ele é percorrido numa **sequência de corte**, e ela não é arbitrária: cada fileira depende de outra, já cortada, para ter referência de onde parar. A convenção de grande escala é estável: começa pelo pavilhão (a parte que fica escondida no engaste, mais tolerante a ajuste), passa pela cinta, e só depois vai para a coroa, terminando na mesa.

Dentro de cada seção, porém, **não há regra única sobre qual fileira vem primeiro**. O princípio que a literatura enuncia é sobre **pontos**, não sobre fileiras: a ordem é a ordem em que os pontos da pedra precisam ser estabelecidos, e as duas partidas mais comuns são um ponto de culaça ou um conjunto de pontos de cinta. Daí as duas sequências correntes — mains primeiro, até um ponto central, com as facetas de cinta vindo encontrá-las; ou facetas de cinta primeiro, fixando a linha da cinta, com as mains depois. **Qual delas é a padrão é questão em aberto: fontes do mesmo nível descrevem as duas, e a escolha pertence ao design.** O que vale nas duas é o mesmo: uma fileira só pode ser cortada **contra** facetas que já existem, e as de ângulo mais raso costumam ficar para o fim, por serem as ajustáveis — as que absorvem o erro acumulado.

A ordem das linhas na tabela geralmente **é** a ordem de corte proposta pelo autor, e invertê-la tira de uma fileira a referência contra a qual ela fecharia.

## Exemplo trabalhado

**Um diagrama simplificado de pavilhão traz duas linhas: Linha 1 — ângulo 42°, índice 0/8/16/24/32/40/48/56/64/72/80/88 (jogo 96), main. Linha 2 — ângulo 46°, índice 4/12/20/28/36/44/52/60/68/76/84/92 (jogo 96), break. O que essas duas linhas dizem, lidas juntas?**

**Passo 1 — a simetria declarada.** Cada linha tem doze índices, espaçados de 8 em 8 dentes num jogo de 96 (96 ÷ 8 = 12): o talhe tem simetria 12-fold, e a vista de topo mostraria doze raios iguais.

**Passo 2 — a relação entre as duas fileiras.** Os índices da Linha 2 (4, 12, 20...) caem exatamente **entre** os da Linha 1 (0, 8, 16...) — intercalados, não sobrepostos. Isso é típico de uma fileira main e uma fileira break vizinhas: cada break fica entre dois mains, preenchendo o intervalo.

**Passo 3 — a diferença de ângulo.** A break, a 46°, é mais inclinada que a main, a 42°; na vista lateral, isso a colocaria mais próxima da cinta.

**Passo 4 — a sequência.** A tabela propõe cortar a Linha 1 (main) primeiro, levando as doze mains a um ponto central na culaça; a Linha 2 (break) vem depois, cortada contra as bordas já existentes das mains vizinhas e fixando a linha da cinta. Um autor que partisse dos pontos de cinta inverteria as duas; o que não muda é que a segunda fecha contra a primeira — o padrão de "cortar contra o que já existe" que a aula 04 desenvolve.

## Erros comuns

- **Tratar as duas vistas como intercambiáveis.** A de topo dá posição angular (índice); a lateral dá inclinação e ordem vertical (ângulo, fileira) — nenhuma substitui a outra.
- **Achar que a ordem das linhas na tabela é arbitrária.** Cada corte precisa de uma referência já existente, e a tabela costuma vir na ordem em que essas referências aparecem.
- **Tomar "main antes de break" como regra geral.** Não é: há designs que partem do ponto de culaça e outros que partem dos pontos de cinta.
- **Confundir "main" com "a única fileira".** As mains são as facetas grandes que atravessam a seção — as maiores, não as mais numerosas —, e quase todo talhe além do mais simples tem fileiras adicionais (break, star) que a completam.

## O que não concluir

- Não concluir por que cortar contra uma referência garante precisão sem medir profundidade — é a aula 04.
- Não concluir como diagnosticar um erro quando uma fileira não fecha contra a vizinha — é a aula 05.
- Não concluir a conversão de um diagrama entre índices de refração diferentes — é a aula 06.
- Não concluir como operar a facetadora para seguir esse diagrama — competência de bancada, fora do escopo teórico deste curso.

## Recap relâmpago

- Um diagrama de lapidação combina três peças: **vista de topo** (contorno e posição angular — a simetria do talhe), **vista lateral** (perfil e inclinação das fileiras) e **tabela** (o ângulo e os índices de cada fileira; a profundidade não vem tabelada).
- Uma **fileira** é um grupo de facetas na mesma altura ao redor da pedra, com o mesmo ângulo; **main** são as facetas grandes que atravessam a seção — as maiores, não as mais numerosas —, **break** e **star** são fileiras auxiliares que a completam. **P, C, G** localizam a fileira em pavilhão, coroa ou cinta.
- Ler uma linha da tabela é aplicar a aula 02: um ângulo e um conjunto de índices (dentro de um jogo declarado) descrevendo uma fileira inteira de uma vez; a terceira coordenada fica por conta do ponto de encontro.
- A **sequência de corte** segue pavilhão → cinta → coroa; dentro de cada seção, a ordem é ditada pelos pontos de referência que precisam existir — de um ponto de culaça ou de pontos de cinta —, não por uma regra fixa de main antes de auxiliares. A ordem das linhas costuma ser a sequência proposta pelo autor.
- Índices intercalados entre duas fileiras — uma caindo entre os índices da outra — são o padrão típico de main e break vizinhas.

## Próxima aula

Na [[09-geometria-e-diagramas-aula-04-meetpoint-faceting-a-logica-do-ponto-de-encontro|Aula 04 — Meetpoint faceting]], a ideia de "cortar contra o que já existe", só mencionada de passagem aqui, ganha nome e mecanismo: por que encontrar facetas num ponto exato substitui a necessidade de medir profundidade diretamente.

## Fontes consultadas

- [[08-optica-do-facetado-aula-06-modelagem-optica-ray-tracing-e-os-limites-da-metrica|módulo 08, aula 06]] deste curso — a definição de diagrama de lapidação, reativada nesta aula.
- United States Faceters Guild, *dicionário de facetamento* — *Tier*: "a group of facets at the same elevation around the stone"; *Main Facets*: "a set of large facets which extend from Girdle to Table on the Crown, or from Girdle to Culet on the Pavilion". Consultada em 2026-09-06. O dicionário **não** define *main* como a fileira mais numerosa.
- Robert W. Strickland, *GemCad for Windows — User's Guide*, e Sky Jems, *Faceting Diagram* — a estrutura de vista de topo, vista lateral e tabela (*mast angle* e posições de índice como as colunas centrais). Consultadas em 2026-09-06.
- Vargas & Vargas, *Faceting for Amateurs* — a leitura de diagramas impressos e a convenção de sequência pavilhão-cinta-coroa.
- United States Faceters Guild, *Sequencing Facets* — o princípio de sequência: "the sequencing of facets is determined by the order in which points on the stone must be made, and the two most common starting places were either a culet point or a set of girdle points", e a prática de deixar as facetas ajustáveis (de degrau, de ângulo mais raso) para o fim, para absorver o erro acumulado. Consultada em 2026-09-06. Essa fonte **não** enuncia uma regra de "main antes de break".
- The Gemology Project, verbete *Faceting*, e Geosciences LibreTexts 17.2 *Faceting* — descrevem a sequência oposta, com as facetas de cinta (*break*) cortadas antes das mains, em pavilhão e coroa. É a divergência declarada nesta aula. Consultados em 2026-09-06.

<!--
nivel: ensino-medio-com-gemologia-v1
palavras_corpo: 1598
cobertura:
  lapidacao-m09-oa03: [Conteúdo, "Exemplo trabalhado", "Erros comuns", "Recap relâmpago"]
alegacoes_auditaveis:
  - claim_id: DIA-TRES-PECAS-001
    claim: "Um diagrama de lapidacao combina tres pecas complementares: a vista de topo (plan view, contorno da pedra visto de cima com a posicao angular de cada faceta), a vista lateral (perfil, mostrando a inclinacao e a ordem vertical das fileiras) e a tabela. As colunas centrais da tabela sao DUAS — o angulo (mast angle) e a posicao ou o conjunto de posicoes de indice de cada fileira; a terceira coordenada da aula 02 raramente vira coluna, porque a profundidade de cada corte e fixada na pedra pelo ponto de encontro (aula 04). Nenhuma das tres pecas sozinha especifica o talhe por completo."
    risk: fato tecnico
    source: "Robert W. Strickland, GemCad for Windows User's Guide (plan view, profile view e facet table); Sky Jems, Faceting Diagram (colunas de mast angle e index positions; 'together, these two parameters uniquely locate each facet on the stone's surface'). Verificado em 2026-09-06."
  - claim_id: DIA-VISTA-TOPO-001
    claim: "A vista de topo mostra o contorno final da pedra e a posicao angular de cada faceta ao redor do eixo; e nessa vista que a simetria do talhe fica visivel, e o numero de posicoes que ela desenha precisa ser divisor do numero de dentes do jogo de indice escolhido (ver modulo 09, aula 01, deste curso)."
    risk: consistencia interna
    source: "curso de lapidacao, modulo 09 aula 01 (regra de divisibilidade da simetria); Robert W. Strickland, GemCad for Windows User's Guide"
  - claim_id: DIA-FILEIRA-NOME-001
    claim: "Uma fileira (tier) e um grupo de facetas na mesma altura ao redor da pedra — na pratica, com o mesmo angulo e a mesma altura do mastro. As mains sao as facetas grandes que vao da cinta a mesa na coroa, ou da cinta a culaca no pavilhao: sao as MAIORES da secao, nao as mais numerosas (num brilhante redondo, oito mains de pavilhao contra dezesseis facetas de cinta). Fileiras adicionais e mais estreitas recebem nomes como break (entre a main e a cinta) ou star (junto a mesa, na coroa). P, C e G sao abreviacoes correntes para pavilhao, coroa e cinta (girdle)."
    risk: fato tecnico
    source: "United States Faceters Guild, dicionario de facetamento — Tier: 'a group of facets at the same elevation around the stone'; Main Facets: 'a set of large facets which extend from Girdle to Table on the Crown, or from Girdle to Culet on the Pavilion'. Contagem do brilhante redondo padrao. Verificado em 2026-09-06."
  - claim_id: DIA-SEQ-ORDEM-001
    claim: "A sequencia de corte sugerida por um diagrama de lapidacao segue, em grande escala, pavilhao, depois cinta, depois coroa, terminando na mesa. DENTRO de cada secao NAO ha regra fixa de main antes das fileiras auxiliares: o principio enunciado pela literatura e que a ordem e determinada pela ordem em que os PONTOS da pedra precisam ser estabelecidos, e as duas partidas mais comuns sao um ponto de culaca ou um conjunto de pontos de cinta. Em qualquer das duas, uma fileira so pode ser cortada contra facetas que ja existem, e as facetas de angulo mais raso (as ajustaveis) costumam ficar por ultimo, para absorver o erro acumulado na cadeia."
    risk: mecanismo
    source: "United States Faceters Guild, Sequencing Facets: 'the sequencing of facets is determined by the order in which points on the stone must be made, and the two most common starting places were either a culet point or a set of girdle points'; 'if you can let your accumulation of small errors end up on a step facet, you can often save yourself the necessity of cheating'. Verificado em 2026-09-06 — essa fonte NAO enuncia regra de main antes de break."
  - claim_id: DIA-SEQ-INICIO-001
    claim: "CONTROVERSIA DECLARADA (LC-08). Qual fileira e cortada primeiro dentro de uma secao e materia de divergencia real entre fontes de referencia do mesmo nivel. A tradicao de meetpoint faceting descreve as mains do pavilhao cortadas primeiro ate um ponto central, com as facetas de cinta vindo depois encontra-las; The Gemology Project e o Geosciences LibreTexts descrevem a ordem inversa, com as facetas de cinta (break) cortadas antes das mains, tanto no pavilhao quanto na coroa. A aula NAO arbitra o debate: registra as duas ordens e atribui a escolha ao design."
    risk: controversia
    source: "GemologyOnline.com, Preform vs Meetpoint faceting ('cutting your pavilion facets to a central point, then cutting your girdle facets in to meet your pavilion facets'); The Gemology Project, verbete Faceting (coroa: break 47 graus, depois main 42, depois star 27, depois mesa); Geosciences LibreTexts 17.2 Faceting (pavilhao: break facets primeiro, depois mains). Verificado em 2026-09-06."
  - claim_id: DIA-EX-INTERCALADO-001
    claim: "Numa tabela de diagrama, indices intercalados entre duas fileiras — os indices de uma fileira caindo exatamente entre os indices da outra, no mesmo jogo de dentes — sao o padrao tipico de uma fileira main e uma fileira break vizinhas, em que cada break preenche o intervalo angular entre duas mains consecutivas."
    risk: interpretacao
    source: "sintese didatica do curso a partir da estrutura de diagramas descrita por United States Faceters Guild e Robert W. Strickland (GemCad)"
-->
