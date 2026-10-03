# Aula 01: Conceitos e metodologia da cartografia geotécnica: objetivos, escalas e atributos

**ID:** geologia-avancado-m07-a01
**Módulo:** [[07-mapeamento-geotecnico-modulo|Módulo 07 — Metodologia de mapeamento geotécnico]]
**Duração estimada:** ~28 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** definir o que é uma carta geotécnica e como ela difere de um mapa geológico, selecionar a escala de trabalho adequada ao nível de decisão pretendido, e definir o conjunto de atributos a levantar e as unidades de mapeamento de um programa de cartografia geotécnica.

**Pré-requisito:** Módulo 06 completo — classificação de solos, índices físicos, tensões efetivas, percolação, compressibilidade e resistência são os atributos que esta cartografia espacializa; noções de mapeamento geológico e leitura de mapa do curso base.

## Antes de começar, você precisa saber

- Ler um mapa geológico convencional: unidades litoestratigráficas, contatos, atitudes, escala e legenda.
- Que os parâmetros geotécnicos do Módulo 06 (SUCS, NSPT, e, Cc, σ'p, c', φ', k) são obtidos em pontos — furos, amostras, ensaios — e não em áreas.

## Conteúdo

### O que muda quando o mapa passa a ser geotécnico

Um mapa geológico convencional responde a uma pergunta de história: que unidades ocorrem aqui, de que idade, em que relação estratigráfica e estrutural. Uma **carta geotécnica** responde a uma pergunta de uso: **como este terreno se comporta quando alguém constrói, escava, corta, aterra ou dispõe resíduo sobre ele.**

A diferença não é de detalhe, é de **critério de agrupamento**. No mapa geológico, duas ocorrências vão para a mesma unidade se compartilham origem e idade. Na carta geotécnica, vão para a mesma unidade se compartilham **comportamento** frente à solicitação de interesse. As duas coisas frequentemente não coincidem: um granito são e o mesmo granito com 20 m de manto de alteração pertencem à mesma unidade geológica e a unidades geotécnicas completamente distintas; inversamente, solos residuais derivados de litologias diferentes podem convergir para comportamento semelhante e formar uma única unidade geotécnica.

> [!important] A carta geotécnica é interpretativa por construção
> Um mapa geológico registra o que se observa (um contato existe ou não existe). Uma carta geotécnica registra uma **interpretação de aptidão ou de comportamento**, construída a partir de observações mais um modelo de como aquele terreno responde. Isso não a torna menos rigorosa — torna obrigatório que o critério de classificação esteja explícito na legenda e no memorial. Uma carta geotécnica sem critério declarado é inauditável.

### A linhagem do método

A cartografia geotécnica se consolidou como disciplina a partir da década de 1960–70, com dois marcos que ainda organizam a prática: o guia da **IAEG (Associação Internacional de Geologia de Engenharia)** para elaboração de mapas geológico-geotécnicos, publicado sob os auspícios da UNESCO em 1976, que padronizou tipologia, simbologia e conteúdo; e, no Brasil, a sistematização feita por **Zuquette e colaboradores** na Escola de Engenharia de São Carlos (USP) a partir dos anos 1980, que adaptou o método às condições de solos tropicais — espessos perfis de alteração, comportamento colapsível e laterítico, e a escassez de dados de subsuperfície típica do meio urbano brasileiro.

A tipologia da IAEG distingue mapas por **propósito** (de finalidade específica, como para um traçado rodoviário, ou multiuso), por **conteúdo** (analíticos, que representam um atributo isolado, ou abrangentes, que representam a síntese) e por **escala**.

### Escala: o parâmetro que define o que a carta pode decidir

A escala não é uma preferência gráfica; ela determina o **nível de decisão** que a carta pode sustentar, porque fixa a menor área representável e, por consequência, a densidade de investigação necessária. Faixas usuais e o que cada uma sustenta:

| Escala | Denominação usual | Decisão que sustenta |
|---|---|---|
| < 1:100.000 | Regional / de reconhecimento | Planejamento territorial amplo, seleção de alternativas de traçado, priorização de áreas para estudo |
| 1:100.000 a 1:25.000 | Média / de semidetalhe | Plano diretor municipal, zoneamento de uso e ocupação, expansão urbana |
| 1:25.000 a 1:10.000 | Detalhe | Loteamento, projeto de arruamento, definição de diretrizes de parcelamento |
| > 1:10.000 (1:5.000, 1:2.000) | Grande detalhe | Projeto de obra, setorização de risco em assentamento, intervenção específica |

Uma consequência prática e frequentemente ignorada: **um erro de escala é irreversível para baixo.** Uma carta 1:50.000 pode ser generalizada para 1:100.000 sem perda de validade, mas jamais pode ser ampliada para 1:5.000 e usada para decidir a implantação de uma edificação — a informação de detalhe simplesmente não foi levantada, e a ampliação gráfica cria uma aparência de precisão que os dados não sustentam.

### Atributos: o que se levanta

O conjunto de atributos é escolhido em função do objetivo da carta, e é a decisão metodológica mais consequente do trabalho. Os grupos usuais:

- **Materiais inconsolidados:** tipo genético (residual, coluvionar, aluvionar, aterro), espessura, classificação SUCS, plasticidade, resistência (NSPT), erodibilidade, colapsividade e expansividade.
- **Substrato rochoso:** litologia, grau de alteração e de consistência, profundidade do topo rochoso, estruturas e famílias de descontinuidades (Módulo 05).
- **Água subterrânea:** profundidade do nível d'água e sua variação sazonal, condições de fluxo, vulnerabilidade do aquífero.
- **Relevo:** declividade, amplitude, forma das vertentes, densidade de drenagem — quase sempre derivados de modelo digital de elevação (Aula 02).
- **Processos e feições dinâmicas:** cicatrizes de escorregamento, erosão laminar e linear (sulcos, ravinas, voçorocas), assoreamento, subsidência, cavidades, áreas inundáveis.
- **Ocupação e uso:** cortes e aterros existentes, tipologia construtiva, drenagem urbana, áreas degradadas.

> [!warning] O atributo mais escasso é a subsuperfície
> Relevo, uso e feições superficiais são hoje obtidos com facilidade e cobertura contínua por sensoriamento remoto e modelo digital de elevação. Espessura de solo, topo rochoso, nível d'água e parâmetros geotécnicos continuam vindo de pontos — sondagens, poços, cortes expostos —, tipicamente escassos e mal distribuídos em área urbana. O risco recorrente é uma carta com base topográfica excelente e base de subsuperfície frágil, cuja aparência de detalhe é dada pelo relevo, não pelo dado geotécnico. Declarar a densidade e a distribuição dos pontos de subsuperfície é parte obrigatória do memorial.

### Unidades de mapeamento e o problema do limite

Definidos os atributos, é preciso decidir **como delimitar áreas homogêneas** — a **unidade de mapeamento**, ou unidade geotécnica: uma porção do terreno cujo comportamento, para os fins da carta, pode ser tratado como uniforme. Três abordagens:

- **Landform / unidades de terreno:** delimitação por padrões fisiográficos (forma de vertente, padrão de drenagem, posição no relevo), tradicionalmente interpretados de fotografias aéreas e hoje de imagens e modelos digitais. Rápida e eficiente em área extensa, e ancorada num princípio real — a forma do relevo é resultado do comportamento do material sob intemperismo e erosão.
- **Paramétrica / por célula:** o território é dividido numa malha regular e cada célula recebe os valores dos atributos, sem pressupor unidades naturais. É a abordagem que melhor se acopla ao SIG (Aula 04) e a métodos estatísticos de suscetibilidade.
- **Por unidades geológico-geomorfológicas combinadas:** parte das unidades geológicas e as subdivide pelo grau de alteração, espessura de manto e posição no relevo — a mais usada no Brasil por trabalhar bem com solos tropicais espessos.

Em qualquer delas, os limites entre unidades geotécnicas são majoritariamente **graduais e interpretados**, não contatos observados. Representá-los com linha cheia e fina transmite uma certeza que o dado não tem — daí a prática recomendada de usar linha tracejada, faixa de transição, ou registrar explicitamente na legenda o grau de confiança de cada limite.

### O produto: carta, legenda e memorial

Uma carta geotécnica não é um único desenho. O produto completo tem três peças, e a terceira é a que separa trabalho técnico de figura ilustrativa:

1. **A carta** propriamente dita, na escala definida.
2. **A legenda**, que declara o critério de classificação de cada unidade — não apenas seu nome, mas as faixas de atributo que a definem.
3. **O memorial (ou relatório técnico)**, que documenta os dados de origem, sua densidade e distribuição, o método de delimitação, as incertezas assumidas e as **limitações de uso** da carta — inclusive a escala mínima em que ela pode ser aplicada e as decisões que ela **não** sustenta.

## Exemplo trabalhado

**Situação:** uma prefeitura de município de porte médio precisa de subsídio geotécnico para (a) revisar o plano diretor, definindo vetores de expansão urbana, e (b) decidir se autoriza a implantação de um loteamento de 40 ha numa encosta específica. Existe verba para um único programa de cartografia. Defina escala, atributos e unidades de mapeamento.

**Resolução:**

**Passo 1 — Reconhecer que são dois níveis de decisão, não um.** A revisão do plano diretor é decisão de **zoneamento** sobre todo o território municipal; a autorização do loteamento é decisão de **projeto** sobre 40 ha. As duas não cabem na mesma carta, e a tentativa de resolvê-las com um produto único produz ou uma carta cara demais (detalhe municipal inteiro) ou uma carta inválida para a segunda decisão (regional ampliada).

**Passo 2 — Definir dois produtos escalonados.**
- **Produto A — carta geotécnica municipal, 1:25.000.** Sustenta o zoneamento do plano diretor: delimita áreas aptas, aptas com restrição e inaptas à expansão urbana.
- **Produto B — carta de detalhe da gleba, 1:2.000.** Sustenta a decisão sobre o loteamento, com investigação de subsuperfície dedicada.

**Passo 3 — Atributos do Produto A** (compatíveis com 1:25.000, priorizando o que se obtém em cobertura contínua): declividade e forma de vertente derivadas de MDE; materiais inconsolidados por tipo genético e espessura estimada; profundidade do nível d'água a partir de cadastro de poços; feições erosivas e cicatrizes de escorregamento mapeadas por imagem e checadas em campo; áreas inundáveis por cota; ocupação atual.

**Passo 4 — Atributos adicionais do Produto B** (o que só faz sentido em 1:2.000): sondagens SPT com amostragem, distribuídas na gleba conforme NBR 8036; ensaios de caracterização e de resistência nas unidades críticas; levantamento das descontinuidades nos afloramentos; medição do nível d'água em duas estações do ano; levantamento topográfico dedicado.

**Passo 5 — Unidades de mapeamento.** No Produto A, unidades geológico-geomorfológicas combinadas (litologia subdividida por classe de declividade e espessura de manto), que aproveitam bem os dados de cobertura contínua. No Produto B, delimitação direta por interpolação entre sondagens, com limites tracejados onde a densidade de furos não sustenta um contato firme.

**Interpretação:** o erro que este exemplo evita é o mais comum da prática — usar a carta de zoneamento para autorizar obra específica. O Produto A pode classificar toda a encosta como "apta com restrição", o que é uma informação correta e útil para o plano diretor e **insuficiente** para decidir sobre o loteamento: dentro daqueles 40 ha pode haver setores efetivamente inaptos que a escala 1:25.000 nem representa. A escala não é um detalhe de apresentação — é o que determina se a carta pode ou não sustentar a decisão que se quer tomar com ela.

## Erros comuns

- **Ampliar graficamente uma carta de escala menor** para usá-la em decisão de detalhe, criando aparência de precisão sem dado correspondente.
- **Transcrever o mapa geológico como se fosse carta geotécnica**, mantendo unidades agrupadas por idade e origem em vez de por comportamento — e assim reunindo rocha sã e manto de alteração espesso na mesma unidade.
- **Omitir o critério de classificação da legenda**, entregando unidades nomeadas ("apta", "restrita") sem as faixas de atributo que as definem, o que torna a carta inauditável e irreprodutível.
- **Representar limites interpretados com linha cheia**, transmitindo certeza inexistente.
- **Dimensionar a carta pela disponibilidade de base topográfica** e não pela decisão a sustentar, produzindo relevo detalhado sobre dado geotécnico escasso.
- **Não declarar densidade e distribuição dos pontos de subsuperfície** no memorial, impedindo que o usuário avalie a confiabilidade espacial da carta.

## O que não concluir

- **Que carta geotécnica dispensa investigação de projeto.** Mesmo a carta de grande detalhe é um instrumento de planejamento e de diretriz; ela indica onde investigar e o que esperar, e não substitui a campanha de sondagens da obra (Módulo 06, Aula 06).
- **Que uma unidade geotécnica é internamente homogênea.** Ela é homogênea **para os fins e na escala da carta**. Numa escala maior, quase toda unidade se revela heterogênea — o que é uma propriedade do método, não um defeito da carta.
- **Que carta mais detalhada é sempre melhor.** Detalhe tem custo, e um levantamento 1:2.000 de um município inteiro é tipicamente inviável e desnecessário. O produto correto é o de menor detalhe que ainda sustenta a decisão pretendida.

## Recap relâmpago

- A carta geotécnica agrupa o terreno por **comportamento** frente ao uso, enquanto o mapa geológico agrupa por origem e idade — critérios que frequentemente não coincidem (rocha sã e seu manto de alteração são uma unidade geológica e duas geotécnicas).
- É um produto **interpretativo**, o que obriga a declarar explicitamente o critério de classificação na legenda e no memorial.
- A metodologia vem do guia **IAEG/UNESCO (1976)** e, no Brasil, da sistematização de **Zuquette** e colaboradores (EESC-USP) para solos tropicais.
- A **escala** determina o nível de decisão que a carta sustenta: regional para planejamento territorial, semidetalhe para plano diretor, detalhe para loteamento, grande detalhe para obra e setorização. Ampliar uma carta para além de sua escala é erro irreversível.
- Atributos cobrem materiais inconsolidados, substrato rochoso, água subterrânea, relevo, processos dinâmicos e ocupação. O **relevo é abundante e a subsuperfície é escassa** — a densidade de pontos precisa constar do memorial.
- Unidades de mapeamento são delimitadas por landform, por célula (paramétrica) ou por unidades geológico-geomorfológicas combinadas; seus limites são graduais e interpretados, e devem ser representados como tais.
- O produto completo é carta + legenda com critério + **memorial** declarando dados, incertezas e limitações de uso.

## Próxima aula

[[07-mapeamento-geotecnico-aula-02-cartas-basicas-materiais-substrato-declividade|Aula 02 — Cartas básicas: materiais inconsolidados, substrato rochoso, declividade e feições do terreno]]

## Anterior

Este é o início do Módulo 07. O módulo anterior é [[06-elementos-de-geomecanica/06-elementos-de-geomecanica-modulo|Módulo 06 — Elementos de geomecânica]].

## Fontes

- Metodologia de cartografia geotécnica, tipologia e escalas: IAEG — International Association of Engineering Geology (1976), *Engineering Geological Maps: A Guide to Their Preparation*, UNESCO Press, Paris.
- Sistematização brasileira e adaptação a solos tropicais: Zuquette, L. V. & Gandolfi, N. (2004), *Cartografia Geotécnica*, Oficina de Textos, São Paulo; Zuquette, L. V. (1987), *Análise crítica da cartografia geotécnica e proposição metodológica para as condições brasileiras*, tese de doutorado, EESC-USP, São Carlos.
- Cartografia geotécnica aplicada ao planejamento urbano no Brasil: Prandini, F. L. et al. (1995), *Cartografia geotécnica nos planos diretores municipais*, IPT — Instituto de Pesquisas Tecnológicas do Estado de São Paulo.
- Programação de investigação de subsuperfície: ABNT NBR 8036 (*Programação de sondagens de simples reconhecimento dos solos para fundações de edifícios*), citada como referência de densidade para o produto de detalhe.

<!--
nivel: avancado
palavras_corpo: ~2050

mapa_objetivo_secao:
  geologia-avancado-m07-oa02: "O que muda quando o mapa passa a ser geotécnico" + "A linhagem do método" + "Escala: o parâmetro que define o que a carta pode decidir" + "Atributos: o que se levanta" + "Unidades de mapeamento e o problema do limite" + "O produto: carta, legenda e memorial" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: CARTGEO-M07-A01-CRITERIO-001
    claim: "A carta geotécnica agrupa o terreno por comportamento frente ao uso, enquanto o mapa geológico agrupa por origem e idade, de modo que rocha sã e seu manto de alteração formam uma unidade geológica e duas unidades geotécnicas."
    risk: fato
    source: "IAEG/UNESCO 1976; Zuquette & Gandolfi 2004"
  - claim_id: CARTGEO-M07-A01-IAEG-002
    claim: "O guia de referência para elaboração de mapas geológico-geotécnicos é o da IAEG publicado pela UNESCO em 1976, que padronizou tipologia (por propósito, conteúdo e escala), simbologia e conteúdo."
    risk: fato
    source: "IAEG/UNESCO 1976"
  - claim_id: CARTGEO-M07-A01-ZUQUETTE-003
    claim: "No Brasil, a sistematização metodológica da cartografia geotécnica adaptada a solos tropicais foi feita por Zuquette e colaboradores na EESC-USP a partir dos anos 1980."
    risk: fato
    source: "Zuquette 1987; Zuquette & Gandolfi 2004"
  - claim_id: CARTGEO-M07-A01-ESCALA-004
    claim: "A escala determina o nível de decisão que a carta sustenta: menor que 1:100.000 para planejamento regional, 1:100.000 a 1:25.000 para plano diretor, 1:25.000 a 1:10.000 para loteamento, e maior que 1:10.000 para projeto e setorização de risco. Uma carta não pode ser ampliada além de sua escala de levantamento."
    risk: fato
    source: "IAEG/UNESCO 1976; Zuquette & Gandolfi 2004; Prandini et al. 1995"
  - claim_id: CARTGEO-M07-A01-UNIDADES-005
    claim: "As unidades de mapeamento podem ser delimitadas por landform (unidades de terreno), por abordagem paramétrica em células, ou por unidades geológico-geomorfológicas combinadas; seus limites são graduais e interpretados, não contatos observados."
    risk: fato
    source: "IAEG/UNESCO 1976; Zuquette & Gandolfi 2004"
  - claim_id: CARTGEO-M07-A01-PRODUTO-006
    claim: "O produto completo de cartografia geotécnica compreende a carta, a legenda com o critério de classificação declarado, e o memorial documentando dados de origem, densidade, método, incertezas e limitações de uso."
    risk: fato
    source: "IAEG/UNESCO 1976; Zuquette & Gandolfi 2004"
-->
