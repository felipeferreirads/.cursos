# Aula 01: Conceito de contaminação e fontes: atividades humanas geradoras e carga contaminante

**ID:** geologia-avancado-m03-a01
**Módulo:** [[03-contaminacao-aguas-subterraneas-modulo|Módulo 03 — Contaminação dos recursos hídricos subterrâneos]]
**Duração estimada:** ~26 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** identificar as principais fontes de contaminação de águas subterrâneas por tipo de atividade humana e estimar a carga contaminante que uma fonte libera ao subsolo.
**Pré-requisito:** Módulos 01 (fluxo subterrâneo, zona não saturada, poços) e 02 (composição química das águas, balanço iônico, fácies hidroquímica) concluídos.

## Antes de começar, você precisa saber

- Conceitos de aquífero, zona não saturada e fluxo subterrâneo (Módulo 01).
- Constituintes maiores, menores e traço de uma água natural, e a ideia de fácies hidroquímica "de fundo" (Módulo 02).

## Conteúdo

### O que é contaminação, e por que a definição importa

**Contaminação** da água subterrânea é a introdução, por atividade humana, de uma substância que altera sua composição de forma mensurável em relação à condição de fundo (*background*) — a composição que a água teria pela interação natural água-rocha, estudada no Módulo 02. **Poluição** é usada por muitos autores como sinônimo, embora alguns reservem o termo para o caso em que a alteração ultrapassa um padrão de uso (por exemplo, torna a água imprópria para consumo). Nesta aula, e no restante do módulo, os dois termos são tratados como equivalentes, seguindo o uso mais comum na hidrogeologia ambiental (Fetter, 1999; Domenico & Schwartz, 1998).

A definição importa porque estabelece uma régua: para dizer que uma água está contaminada, é preciso saber qual seria sua composição natural naquele aquífero — o que exige uma amostra de referência (um poço "a montante" da fonte suspeita, ou dados históricos) e as ferramentas do Módulo 02 (fácies hidroquímica, balanço iônico) para comparar. Sem uma linha de base, um valor elevado de um constituinte pode ser natural (um aquífero cárstico já tem SO₄²⁻ alto por dissolução de gipsita, por exemplo) ou antrópico — e confundir os dois é um dos erros mais caros em investigação ambiental.

> [!warning] "Alto" não é o mesmo que "contaminado"
> Um constituinte em concentração elevada só indica contaminação quando comparado contra o que seria esperado naturalmente naquele aquífero específico. A sequência de Chebotarev (Módulo 02) já mostra que SO₄²⁻ e Cl⁻ crescem naturalmente ao longo do fluxo regional — um valor alto de cloreto perto da zona de descarga pode ser inteiramente natural.

### Classificação das fontes de contaminação

A hidrogeologia ambiental classifica as fontes de contaminação de duas formas complementares, que a investigação de campo usa lado a lado.

**Por geometria da fonte:**

- **Fonte pontual (point source):** área de dimensão pequena e bem definida — um tanque de combustível vazando, um vazamento de tubulação, uma lagoa de rejeito. Gera uma pluma de contaminação com geometria relativamente previsível a partir de um ponto de origem.
- **Fonte difusa (non-point source ou diffuse source):** distribuída sobre uma área extensa, sem um ponto de origem único — aplicação de fertilizantes e agrotóxicos numa bacia agrícola inteira, ou deposição atmosférica sobre uma região. A carga contaminante chega ao aquífero de forma distribuída, e a pluma resultante tende a ocupar uma área ampla, sem uma origem geométrica localizada.

**Por atividade geradora**, a literatura (Fetter, 1999; USEPA) agrupa as fontes mais comuns em:

- **Disposição de resíduos sólidos:** aterros sanitários e lixões — o lixiviado (líquido gerado pela percolação de água de chuva através do resíduo, carregando matéria orgânica decomposta, amônia, metais e sais) é uma fonte pontual a difusa, de longa duração (décadas), rica em matéria orgânica e com DBO/DQO elevadas.
- **Vazamento de tanques e tubulações subterrâneas:** postos de combustível (tanques de armazenamento subterrâneo, USTs — *underground storage tanks*) são a fonte pontual mais estudada mundialmente, por gerar hidrocarbonetos de petróleo (BTEX: benzeno, tolueno, etilbenzeno, xilenos) em fase livre (Aula 04).
- **Agricultura:** fonte tipicamente difusa — nitrato (de fertilizantes nitrogenados e dejetos animais) e agrotóxicos (herbicidas, pesticidas) percolam pela zona não saturada em áreas extensas de cultivo.
- **Efluentes domésticos e industriais:** fossas sépticas e sumidouros (fonte pontual a semi-difusa, dependendo da densidade), e lançamento de efluentes industriais não tratados (fonte pontual, composição variável conforme o processo industrial).
- **Mineração:** drenagem ácida de mina (oxidação de sulfetos expostos, gerando acidez e mobilização de metais) e disposição de rejeitos — fontes de longa duração, muitas vezes ativas mesmo décadas após o fechamento da mina.
- **Intrusão salina e outras fontes "não químicas industriais":** o avanço da cunha de água salgada por superexplotação costeira (Aula 04) e a salinização por irrigação também se enquadram como contaminação, ainda que a "substância" introduzida (sal) não seja um poluente industrial.

> [!note] A mesma substância, fontes diferentes
> Nitrato aparece tanto em fontes agrícolas difusas (fertilizante) quanto em fontes pontuais (fossa séptica, chorume de aterro). Identificar a fonte correta de um contaminante específico costuma exigir mais que a concentração medida — traçadores isotópicos (δ¹⁵N do nitrato, por exemplo) ou o padrão espacial da pluma ajudam a distinguir a origem, tema que ultrapassa o escopo desta aula introdutória.

### Carga contaminante: o que a fonte efetivamente libera

Identificar a fonte não basta para prever seu impacto — é preciso estimar a **carga contaminante** (*contaminant loading*), a massa de um contaminante liberada ao meio por unidade de tempo. A carga é o dado de entrada de qualquer modelo de transporte (Aulas 02 e 03): sem ela, não há como estimar a concentração resultante na água subterrânea.

A forma mais simples de estimar a carga é:

**Carga (massa/tempo) = Concentração da fonte × Vazão de infiltração através da fonte**

Por exemplo, para um aterro sanitário, a vazão de infiltração de lixiviado pode ser estimada a partir do balanço hídrico do solo de cobertura (precipitação menos evapotranspiração menos escoamento superficial, ajustado pela permeabilidade da camada de cobertura) e a concentração, de amostras do próprio lixiviado ou de valores de referência da literatura. Para uma fonte agrícola difusa, a carga é frequentemente expressa por área (massa/área/tempo) — por exemplo, kg de N por hectare por ano aplicados como fertilizante, dos quais uma fração (a "fração de lixiviação") efetivamente atinge a zona saturada.

Dois fatores controlam quanto da carga aplicada na superfície chega, de fato, ao aquífero:

- **Atenuação na zona não saturada:** parte do contaminante é retida, degradada ou volatilizada antes de atingir o lençol freático (mecanismos detalhados na Aula 03) — nem toda carga aplicada na superfície chega à zona saturada.
- **Duração da fonte:** uma fonte pode ser de pulso único (um derramamento acidental, carga alta e breve) ou contínua (um aterro em operação, carga sustentada por anos a décadas) — a duração determina se a pluma resultante tende a se estabilizar (fonte contínua, em regime permanente) ou a se diluir e degradar progressivamente após cessar (fonte de pulso).

> [!important] Carga contaminante não é o mesmo que concentração no aquífero
> A carga descreve o que a fonte libera; a concentração que se observa num poço de monitoramento a jusante é o resultado da carga *depois* de passar pelos processos de transporte e atenuação (Aulas 02 e 03) ao longo do trajeto fonte-poço. Duas fontes com a mesma carga podem produzir concentrações muito diferentes num poço, dependendo da distância, da velocidade de fluxo e da capacidade de atenuação do meio.

## Exemplo trabalhado

**Situação:** um posto de combustível opera com um tanque subterrâneo de gasolina com pequeno vazamento crônico, estimado em 15 L de gasolina por dia infiltrando no solo, com concentração de benzeno na gasolina de aproximadamente 1.000 mg/L (valor típico de gasolina brasileira, que contém etanol anidro, mas ainda carrega benzeno residual). Estime a carga diária de benzeno liberada ao subsolo.

**Cálculo:**

Carga = Volume infiltrado × Concentração de benzeno na fase líquida

Carga = 15 L/dia × 1.000 mg/L = 15.000 mg/dia = 15 g/dia de benzeno

**Interpretação:** essa é a carga *na fonte*, antes de qualquer atenuação na zona não saturada. Como a gasolina vazada forma uma fase separada não aquosa (LNAPL, Aula 04) que fica retida acima do lençol freático, apenas a fração de benzeno que se dissolve na água de infiltração (governada por sua solubilidade e pela partição entre as fases, não pelo volume total vazado) efetivamente entra na água subterrânea como soluto dissolvido — o cálculo acima superestima a carga dissolvida real se aplicado ingenuamente. Ele serve, porém, para dimensionar a ordem de grandeza do problema e justificar por que mesmo um vazamento "pequeno" (15 L/dia é imperceptível na operação do posto) sustenta uma fonte contaminante por anos, dado o baixo limite de potabilidade do benzeno (5 µg/L pela Portaria GM/MS 888/2021) frente aos gramas por dia liberados.

## Erros comuns

- **Chamar de "contaminada" qualquer água com concentração elevada de um constituinte**, sem comparar contra a condição de fundo natural daquele aquífero específico.
- **Confundir fonte pontual com fonte difusa** ao investigar uma pluma de nitrato — antes de atribuir a uma fossa séptica isolada (pontual), é preciso descartar contribuição agrícola regional (difusa), e vice-versa.
- **Tratar a carga na fonte como se fosse igual à concentração que chegará ao poço de monitoramento**, ignorando que o transporte (Aulas 02 e 03) modifica a carga ao longo do trajeto.
- **Assumir que toda a massa vazada de um produto líquido (como gasolina) se dissolve na água** — parte permanece como fase separada (Aula 04), e só a fração efetivamente dissolvida participa do transporte de soluto.

## O que não concluir

- **Que identificar a atividade geradora (posto, aterro, fazenda) já resume a investigação.** A mesma atividade pode gerar cargas muito diferentes conforme a idade da fonte, o volume envolvido e as condições de operação — a classificação por tipo de atividade é o ponto de partida, não a conclusão da caracterização.
- **Que uma fonte de pulso único (derramamento pontual, já contido) deixa de ser relevante depois de removida a fonte física.** Se a carga já infiltrou e formou uma pluma dissolvida, o processo de transporte (Aulas 02–03) continua a partir da massa já presente no aquífero, independentemente de a fonte original ainda existir ou não.

## Recap relâmpago

- Contaminação é a alteração, por atividade humana, da composição de uma água em relação à sua condição de fundo natural — exige uma linha de base para ser reconhecida, não apenas um valor "alto".
- Fontes se classificam por geometria (pontual × difusa) e por atividade geradora (resíduos sólidos, tanques/tubulações, agricultura, efluentes, mineração, intrusão salina, entre outras).
- **Carga contaminante = concentração na fonte × vazão de infiltração** — é o dado de entrada dos modelos de transporte das próximas aulas, e não deve ser confundida com a concentração observada num poço a jusante.
- Atenuação na zona não saturada e duração da fonte (pulso × contínua) controlam quanto da carga aplicada de fato atinge a zona saturada e por quanto tempo.

## Próxima aula

[[03-contaminacao-aguas-subterraneas-aula-02-transporte-advectivo-dispersivo|Aula 02 — Transporte de solutos em subsuperfície: advecção e dispersão hidrodinâmica]]

## Anterior

Primeira aula do módulo. Pressupõe os Módulos [[01-hidrogeologia-recursos-hidricos/01-hidrogeologia-recursos-hidricos-modulo|01]] e [[02-hidrogeoquimica/02-hidrogeoquimica-modulo|02]] concluídos.

## Fontes

- Definição de contaminação/poluição e classificação de fontes: Fetter, C. W. (1999), *Contaminant Hydrogeology*, 2ª ed., Prentice Hall, cap. 1–2.
- Fontes de contaminação e carga contaminante: Domenico, P. A. & Schwartz, F. W. (1998), *Physical and Chemical Hydrogeology*, 2ª ed., Wiley, cap. 15–16.
- Padrão de potabilidade do benzeno: Portaria GM/MS nº 888/2021, Anexo XX (5 µg/L).

<!--
nivel: avancado
palavras_corpo: ~1750

mapa_objetivo_secao:
  geologia-avancado-m03-oa01: "O que é contaminação, e por que a definição importa" + "Classificação das fontes de contaminação" + "Carga contaminante: o que a fonte efetivamente libera" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: CONTAM-M03-A01-DEFINICAO-001
    claim: "Contaminação da água subterrânea é a introdução, por atividade humana, de substância que altera sua composição em relação à condição de fundo natural (background); alguns autores reservam 'poluição' para quando a alteração ultrapassa um padrão de uso."
    risk: fato
    source: "Fetter 1999, cap. 1"
  - claim_id: CONTAM-M03-A01-FONTES-002
    claim: "Fontes de contaminação se classificam por geometria em pontuais (point source) e difusas (non-point/diffuse source), e por atividade geradora em disposição de resíduos sólidos, vazamento de tanques/tubulações, agricultura, efluentes domésticos/industriais, mineração e intrusão salina."
    risk: fato
    source: "Fetter 1999, cap. 1-2; Domenico & Schwartz 1998, cap. 15"
  - claim_id: CONTAM-M03-A01-CARGA-003
    claim: "Carga contaminante (massa/tempo) é estimada como concentração na fonte multiplicada pela vazão de infiltração através da fonte; para fontes difusas é frequentemente expressa por área (massa/área/tempo)."
    risk: fato
    source: "Domenico & Schwartz 1998, cap. 15-16"
  - claim_id: CONTAM-M03-A01-BENZENO-004
    claim: "O padrão de potabilidade para benzeno no Brasil (Portaria GM/MS 888/2021) é 5 microgramas por litro."
    risk: fato
    source: "Portaria GM/MS 888/2021, Anexo XX"
-->
