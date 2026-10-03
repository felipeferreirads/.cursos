# Aula 06: Domínios geometalúrgicos e modelagem da variabilidade: variáveis proxy e valor do projeto

**ID:** geologia-avancado-m09-a06
**Módulo:** [[09-geometalurgia-modulo|Módulo 09 — Geometalurgia]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** definir domínio geometalúrgico, explicar a construção de um modelo geometalúrgico de blocos a partir de variáveis proxy densas e variáveis primárias esparsas, demonstrar a não aditividade do Work Index e da recuperação, e avaliar como a variabilidade metalúrgica se propaga para a recuperação, a capacidade de processamento e o valor presente líquido do projeto.

**Pré-requisito:** nenhum módulo deste curso. Reúne as cinco aulas anteriores: partição do metal (A02), liberação e P80 (A03), Work Index e capacidade (A04), recuperação e balanço metalúrgico (A05), e a distinção variável primária × proxy (A01).

## Antes de começar, você precisa saber

- Que **recuperação** e **Work Index** são variáveis primárias (caras, medidas em poucas amostras) e que **teor, litologia, alteração, dureza e mineralogia** são proxies (baratas, medidas em todos os furos) — Aula 01.
- Que a recuperação de uma rota tem teto fixado pela partição do metal (Aula 02) e pela liberação a um dado P80 (Aula 03).
- Que um Work Index maior significa mais energia por tonelada e **menos toneladas por ano** numa planta de potência instalada fixa (Aula 04).
- Que a estimativa de recursos por krigagem combina os dados de teor de forma **linear** (média ponderada) — pressuposto que esta aula vai confrontar.

## Conteúdo

### O domínio geometalúrgico

Um **domínio geometalúrgico** é um volume do depósito que responde de forma homogênea no processo — mesma recuperação, mesma moabilidade, mesma resposta a reagentes e à lixiviação —, dentro de uma tolerância aceitável para o projeto.

Constrói-se cruzando dois conjuntos de informação:

1. **Controles geológicos** — litologia, zona de intemperismo (oxidada, transição, sulfeto primário), tipo e intensidade da alteração hidrotermal, estilo textural, mineralogia de minério e de ganga.
2. **Resposta metalúrgica medida** nos testes do programa geometalúrgico.

Ponto central: **o domínio geológico não é automaticamente um domínio geometalúrgico**. Uma mesma litologia pode ter duas respostas (o mesmo granito, são e cloritizado, mói e flota diferente); duas litologias distintas podem ter a mesma resposta. O domínio geometalúrgico é **validado pelos dados de processo**, não presumido do mapa geológico.

### O modelo geometalúrgico de blocos

Cada bloco do modelo, além de teor e densidade, recebe atributos metalúrgicos: recuperação prevista por metal, energia específica de moagem (ou o Wi e os parâmetros de impacto), capacidade de processamento que aquele minério permite, consumo de reagente ou de ácido, e propriedades do rejeito.

Disso decorre, por bloco: **receita** (metal recuperável × preço), **custo de processamento** (energia, reagente) e o **tempo** que o bloco ocupa a planta. Esses atributos alimentam o sequenciamento de lavra e o cálculo de valor presente líquido (VPL): não apenas "quanto metal e quando", mas "quanto metal recuperável, a que custo e a que ritmo, e quando".

### Variável primária e proxy, na prática da modelagem

Retomando a Aula 01: a variável **primária** (recuperação, Wi ou energia, capacidade, consumo de reagente) é cara e existe em poucos pontos, com cobertura espacial esparsa. A **proxy** (teor, razão entre cobre solúvel em ácido e cobre total, litologia codificada, índice de alteração, dureza por *point load*, contagem mineralógica, geoquímica multielementar de rotina) é barata e densa, presente em todos os furos.

Constrói-se uma função **proxy → primária** (regressão, árvores de decisão, redes neurais) calibrada nas amostras que têm as duas medidas, e aplica-se a todos os blocos, que têm só as proxies.

**Preferir proxies fisicamente ligadas à causa.** A razão de solubilidade do cobre prevê a recuperação de flotação porque mede diretamente a fração não sulfetada do cobre; a dureza prevê o Wi porque é a mesma propriedade mecânica. Uma correlação sem mecanismo — um elemento-traço que "casa" com a recuperação num conjunto pequeno de amostras — não se sustenta fora da amostra.

### Não aditividade

Este é o ponto que mais confunde quem traz o instinto da estimativa de teor, onde a média ponderada funciona.

- **Teor é aditivo.** O teor de uma blenda de dois minérios é a média ponderada pelas massas. A krigagem funciona porque combina os dados de forma linear. (A krigagem vem do módulo de recursos minerais do **curso base**; os módulos 20 e 21 **deste** curso a formalizam mais adiante. Aqui basta reter que ela é um estimador **linear** — é exatamente essa linearidade que a não aditividade quebra.)
- **Work Index não é aditivo.** Blendar 50/50 um minério de Wi 12 e outro de Wi 18 **não** produz um comportamento de Wi 15 no moinho. O componente mais duro resiste mais, permanece mais tempo no circuito, e a energia se distribui de forma não linear; a moabilidade da blenda tende a ser **pior** que a média e depende da proporção e da granulometria de cada componente.
- **Recuperação não é aditiva.** A recuperação de uma blenda pode ficar **abaixo** da média ponderada das recuperações isoladas: minerais de ganga de um minério (talco, argila, minerais solúveis) contaminam a química de flotação do outro; um minério consome o reagente que faltaria ao outro; a cinética muda.

Consequência prática: **não se pode krigar recuperação ou Work Index diretamente**, como se krige teor. Modela-se a variável primária a partir de proxies que **sejam** aditivas (composição elementar, mineralogia modal), ou usa-se simulação geoestatística com modelos de mistura não lineares, propagando a incerteza em vez de suprimi-la numa média.

### Propagação para o valor do projeto

A variabilidade de recuperação e de capacidade vira uma **distribuição** de produção anual e de fluxo de caixa — não um número.

Ignorar a variabilidade — adotar uma recuperação média única e uma capacidade média única — **enviesa o VPL para cima** e subestima o risco. A planta é dimensionada para um minério médio, e a sequência de lavra dos primeiros anos (justamente os que o desconto menos penaliza) muitas vezes concentra o minério de transição, de pior recuperação e maior dureza. É o padrão por trás de rampas de produção que se arrastam e de estudos de viabilidade que não se confirmam.

O programa geometalúrgico e o **mapeamento geometalúrgico** (*geometallurgical mapping*) mitigam isso: amostragem estratificada por domínio, cobrindo todo o corpo e não só o minério de melhor teor; muitos testes pequenos (SMC, flotação de bancada) para mapear; poucos testes de piloto para validar.

## Exemplo trabalhado

**Situação:** um depósito de cobre tem dois domínios geometalúrgicos definidos e testados:

| | Domínio A — sulfeto primário | Domínio B — transição |
|---|---|---|
| Tonelagem | 60 Mt | 15 Mt |
| Teor | 0,80 % Cu | 0,70 % Cu |
| Recuperação medida | 90 % | 62 % |
| Work Index | 15,5 kWh/t | 19,0 kWh/t |

O estudo de viabilidade preliminar adotou uma **recuperação única de 88 %** e uma **capacidade única de 20 Mt/ano** para todo o minério. Preço do cobre: US$ 8 500/t.

**(a) Cobre recuperável — modelo geometalúrgico (dois domínios):**
`Domínio A: 60 × 0,0080 × 0,90 = 0,4320 Mt Cu`
`Domínio B: 15 × 0,0070 × 0,62 = 0,0651 Mt Cu`
`Total real = 0,4320 + 0,0651 = 0,4971 Mt Cu`

**(b) Cobre recuperável — premissa única de 88 %:**
`Domínio A: 60 × 0,0080 × 0,88 = 0,4224 Mt`
`Domínio B: 15 × 0,0070 × 0,88 = 0,0924 Mt`
`Total assumido = 0,4224 + 0,0924 = 0,5148 Mt Cu`

**(c) Superestimativa:**
`0,5148 − 0,4971 = 0,0177 Mt = 17 700 t Cu`
`a US$ 8 500/t → 17 700 × 8 500 ≈ US$ 150 milhões` de receita que o modelo de recuperação única promete e o depósito não entrega — quase toda concentrada no domínio B.

**(d) Efeito na capacidade:** a planta dimensionada para Wi 15,5 e 20 Mt/ano processa o domínio B (Wi 19,0) a
`20 × 15,5 / 19,0 ≈ 16,3 Mt/ano` — uma perda de ~3,7 Mt/ano de capacidade sempre que a lavra estiver no domínio B. Se o plano de lavra colocar o domínio B nos anos 1–2, os 15 Mt de transição levam `15/16,3 ≈ 0,92` ano em vez dos `15/20 = 0,75` ano previstos — cerca de **dois meses a mais** —, empurrando para a frente a produção de melhor margem do domínio A e reduzindo o VPL pelo desconto.

Atenção à leitura dos dois percentuais, que não são o mesmo número. Um Wi de 19,0 contra 15,5 exige **~23 % mais energia por tonelada** (`19,0/15,5 = 1,23`); a potência instalada é fixa, então esse mesmo fato aparece na saída como **~18 % menos toneladas por ano** (`16,3/20 = 0,82`). Energia por tonelada e toneladas por ano são recíprocos — trocar um pelo outro é o erro aritmético mais comum deste raciocínio.

**Interpretação:** o modelo de recursos vê 75 Mt a ~0,78 % Cu. O modelo geometalúrgico vê dois minérios: um bom, e um que recupera menos de dois terços do cobre e, na mesma planta, entrega ~18 % menos toneladas por ano. A diferença não é acadêmica — são US$ 150 milhões de receita inexistente e um atraso na produção nobre, concentrados no período que o fluxo de caixa desconta menos. Reconhecer isso a tempo permite redesenhar a sequência de lavra (misturar B com A em vez de lavrar B puro no início), dimensionar a planta com folga de moagem, ou rever o valor do projeto com honestidade.

## Erros comuns

- **Krigar recuperação ou Work Index diretamente**, como se fossem aditivos.
- **Supor média ponderada para a moabilidade ou a recuperação de uma blenda.**
- **Igualar domínio geológico a domínio geometalúrgico** sem validar com dados de processo.
- **Adotar uma recuperação única e uma capacidade única** no estudo de viabilidade.
- **Escolher proxies por correlação estatística sem mecanismo físico** — não generalizam para fora da amostra.
- **Amostrar o programa só no minério de melhor teor**, deixando os domínios de pior resposta sem dados.
- **Reportar o VPL como número único** quando a variabilidade metalúrgica pede uma distribuição.

## O que não concluir

- **Que todo depósito tem vários domínios geometalúrgicos** — um minério homogêneo pode ter um só; o número sai dos dados, não de uma regra.
- **Que o modelo geometalúrgico substitui o de recursos** — ele acrescenta camadas (recuperação, energia, capacidade) a cada bloco.
- **Que, uma vez classificados os domínios, a variabilidade dentro de cada um pode ser ignorada** — há variabilidade intradomínio, e ela também se propaga.
- **Que mapear a variabilidade elimina o risco** — reduz a chance de surpresa e melhora o dimensionamento, mas o minério continua variável.

## Recap relâmpago

- Um **domínio geometalúrgico** é um volume que responde de forma homogênea no processo (recuperação, moabilidade, reagente), definido cruzando controles geológicos com resposta metalúrgica medida — e **não** presumido do domínio geológico.
- O **modelo geometalúrgico de blocos** atribui a cada bloco recuperação, energia de moagem/Wi, capacidade, consumo de reagente e propriedades de rejeito, e daí receita, custo e ritmo — alimentando o sequenciamento de lavra e o VPL.
- Modela-se ligando **proxies densas** (teor, razão de solubilidade, litologia, alteração, dureza, mineralogia, geoquímica) a **variáveis primárias esparsas** (recuperação, Wi, capacidade), preferindo proxies com mecanismo físico.
- **Work Index e recuperação não são aditivos:** a blenda não se comporta pela média ponderada, e a recuperação de uma mistura pode ser pior que a média — por isso não se krigam diretamente.
- Ignorar a variabilidade **enviesa o VPL para cima**; o minério de transição, de pior recuperação e maior dureza, costuma estar no início da lavra, onde o fluxo de caixa mais pesa.
- No exemplo, tratar dois domínios (R 90 %/62 %, Wi 15,5/19,0) como um só a 88 % superestima o cobre recuperável em 17 700 t (~US$ 150 milhões) e ignora a perda de capacidade de moagem no domínio de transição — que exige ~23 % mais energia por tonelada e, a potência fixa, entrega ~18 % menos toneladas por ano.

## Próxima aula

[[10-tectonica-de-bacias-sedimentares/10-tectonica-de-bacias-sedimentares-modulo|Módulo 10 — Tectônica de bacias sedimentares]]

## Anterior

[[09-geometalurgia-aula-05-concentracao-e-recuperacao|Aula 05 — Concentração: gravítica, magnética, flotação e lixiviação; recuperação metalúrgica]]

## Fontes

- Coward, S., Vann, J., Dunham, S. & Stewart, M. (2009), "The primary-response framework for geometallurgical variables", *Seventh International Mining Geology Conference*, AusIMM, p. 109–113.
- Dunham, S. & Vann, J. (2007), "Geometallurgy, geostatistics and project value — does your block model tell you what you need to know?", *Proc. First AusIMM International Geometallurgy Conference*, Perth, p. 189–196.
- David, D. (2007), "The importance of geometallurgical analysis in plant study, design and operational phases", *Ninth Mill Operators' Conference*, AusIMM, p. 241–248.
- Philander, C. & Rozendaal, A. (2013), "The application of a novel geometallurgical template model to characterise the Namakwa Sands heavy mineral deposit, West Coast of South Africa", *Minerals Engineering*, 52, p. 82–94.
- Deutsch, C. V. (2013), "Geostatistical modelling of geometallurgical variables — problems and solutions", *Proc. Second AusIMM International Geometallurgy Conference*, Brisbane, p. 7–15.
- Coward, S. & Dowd, P. A. (2015), "Geometallurgical models for the quantification of uncertainty in mining project value chains", *Proc. APCOM 2015*, SME.
- Wills, B. A. & Finch, J. A. (2016), *Wills' Mineral Processing Technology*, 8ª ed., Butterworth-Heinemann, cap. 1 e 3.

<!--
nivel: avancado
palavras_corpo: ~1690
mapa_objetivo_secao:
  geologia-avancado-m09-oa04: "O domínio geometalúrgico" + "O modelo geometalúrgico de blocos" + "Variável primária e proxy, na prática da modelagem" + "Não aditividade" + "Propagação para o valor do projeto" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOMET-M09-A06-DOMINIO-001
    claim: "Um domínio geometalúrgico é um volume do depósito que responde de forma homogênea no processo (recuperação, moabilidade, resposta a reagentes e à lixiviação) dentro de uma tolerância, definido cruzando controles geológicos (litologia, zona de intemperismo, alteração, textura, mineralogia) com resposta metalúrgica medida; o domínio geológico não é automaticamente um domínio geometalúrgico e a distinção deve ser validada por dados de processo."
    risk: fato
    source: "Coward et al. 2009; David 2007; Philander & Rozendaal 2013"
  - claim_id: GEOMET-M09-A06-BLOCK-MODEL-002
    claim: "Um modelo geometalúrgico de blocos atribui a cada bloco, além de teor e densidade, recuperação prevista por metal, energia específica de moagem ou Work Index, capacidade de processamento, consumo de reagente e propriedades de rejeito, dos quais decorrem receita, custo de processamento e tempo de ocupação da planta por bloco, que alimentam o sequenciamento de lavra e o cálculo de VPL."
    risk: fato
    source: "Dunham & Vann 2007; David 2007; Coward & Dowd 2015"
  - claim_id: GEOMET-M09-A06-PROXY-003
    claim: "A modelagem geometalúrgica calibra uma função de variáveis proxy densas (teor, razão de solubilidade, litologia, índice de alteração, dureza, mineralogia, geoquímica multielementar) para variáveis primárias esparsas (recuperação, Work Index, capacidade, consumo de reagente), preferindo proxies ligadas fisicamente à causa (razão de solubilidade → recuperação de flotação; dureza → Work Index) em vez de correlações estatísticas sem mecanismo."
    risk: fato
    source: "Coward et al. 2009 (primary-response framework); Dunham & Vann 2007"
  - claim_id: GEOMET-M09-A06-NAO-ADITIVIDADE-004
    claim: "Teor é uma variável aditiva (a blenda é a média ponderada pelas massas e pode ser krigada); Work Index e recuperação não são aditivos: a moabilidade de uma blenda tende a ser pior que a média ponderada (o componente mais duro domina o tempo de residência), e a recuperação de uma blenda pode ficar abaixo da média por interação de minerais de ganga e de reagentes; por isso recuperação e Work Index não devem ser krigados diretamente, e sim modelados a partir de proxies aditivas ou por simulação com modelos de mistura não lineares."
    risk: fato
    source: "Deutsch 2013; Coward et al. 2009; Dunham & Vann 2007"
  - claim_id: GEOMET-M09-A06-PROPAGACAO-005
    claim: "A variabilidade de recuperação e de capacidade propaga-se para uma distribuição de produção anual e de fluxo de caixa; adotar uma recuperação e uma capacidade médias únicas enviesa o VPL para cima e subestima o risco, sobretudo porque o minério de transição — de pior recuperação e maior dureza — costuma ser lavrado nos primeiros anos, os menos penalizados pelo desconto, o que está associado a rampas de produção lentas e a estudos de viabilidade não confirmados."
    risk: fato
    source: "Dunham & Vann 2007; David 2007; Coward & Dowd 2015"
  - claim_id: GEOMET-M09-A06-EXEMPLO-006
    claim: "Para dois domínios — A: 60 Mt a 0,80 % Cu, R 90 %, Wi 15,5; B: 15 Mt a 0,70 % Cu, R 62 %, Wi 19,0 — o cobre recuperável real é 0,4320 + 0,0651 = 0,4971 Mt; assumindo R única de 88 % seria 0,4224 + 0,0924 = 0,5148 Mt; a superestimativa é 0,0177 Mt (17 700 t Cu), ~US$ 150 milhões a US$ 8 500/t, quase toda no domínio B. A capacidade da planta (dimensionada para Wi 15,5 e 20 Mt/ano) cai para 20 × 15,5/19,0 ≈ 16,3 Mt/ano ao processar o domínio B: o Wi maior exige ~23 % mais energia por tonelada (19,0/15,5 = 1,23) e, a potência instalada fixa, entrega ~18 % menos toneladas por ano (16,3/20 = 0,82) — as duas grandezas são recíprocas e não devem ser trocadas uma pela outra. Os 15 Mt do domínio B levam 15/16,3 = 0,92 ano em vez dos 15/20 = 0,75 ano previstos, cerca de dois meses a mais."
    risk: calculo
    source: "Aritmética de cobre recuperável e de capacidade por escalonamento inverso do Work Index; equação de Bond (Bond 1961)"
-->
