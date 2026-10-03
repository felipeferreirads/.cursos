# Aula 01: Consolidação e validação de bases de dados de mineração; revisão do modelo de blocos e da krigagem ordinária

**ID:** geologia-avancado-m21-a01
**Módulo:** [[21-modelagem-geoestatistica-depositos-minerais-modulo|Módulo 21 — Modelagem geoestatística de depósitos minerais]]
**Duração estimada:** ~28 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** mostrar como uma base de dados de furos de sonda é estruturada, validada e consolidada antes de qualquer estimativa, e retomar (sem repetir) o modelo de blocos e a krigagem ordinária do Módulo 20 como ponto de partida deste módulo.
**Ao final você vai conseguir:** descrever as tabelas relacionais que compõem uma base de dados de mineração e como elas se combinam por desaggregação espacial (*desurveying*); listar as checagens de validação que uma base precisa passar antes de alimentar um modelo de blocos; definir os parâmetros que especificam um modelo de blocos (origem, tamanho de bloco, rotação, subcelas) e justificar a escolha do tamanho do bloco a partir da malha de sondagem; e enunciar, sem refazer as contas, o que a krigagem ordinária do Módulo 20 já resolve e o que este módulo acrescenta a partir daqui.
**Pré-requisito:** Módulo 20 completo — em especial a Aula 01 (composição de amostras, estatística descritiva) e a Aula 05 (krigagem ordinária, krigagem de bloco).

## Conteúdo

### O que o Módulo 20 assumiu pronto

O Módulo 20 tratou a base de dados como algo já pronto: uma lista de teores compostos por bancada (Módulo 20, Aula 01), prontos para calcular variogramas e resolver sistemas de krigagem. Na prática de um projeto real, esse ponto de partida é o resultado de um trabalho anterior — muitas vezes subestimado — de **consolidar** dados que chegam de fontes diferentes (campanhas de sondagem de anos distintos, laboratórios distintos, formatos de arquivo distintos) e **validar** que eles descrevem, de fato, o espaço físico que dizem descrever. Um erro nessa etapa não aparece como um número estranho isolado: ele se propaga para o variograma, para os pesos de krigagem e para o relatório de recursos, e é por isso que a prática da indústria trata a validação de banco de dados como um **gate** — uma barreira que o projeto não passa sem cruzar — antes de qualquer modelagem geoestatística.

### As tabelas de uma base de dados de furos de sonda

Uma base de dados de sondagem mineral é, estruturalmente, um banco de dados **relacional**: várias tabelas que se conectam por uma chave comum, o identificador do furo (*hole ID*). As quatro tabelas centrais são:

- **Collar** (colar/boca do furo): uma linha por furo, com sua localização de superfície — coordenadas $X, Y, Z$ (cota) — e, tipicamente, a profundidade final perfurada.
- **Survey** (inclinometria): várias linhas por furo, registrando **azimute** e **mergulho/inclinação** (*dip*) medidos em profundidades específicas ao longo do furo. Um furo raramente é perfeitamente reto; ele desvia com a profundidade, sobretudo em furos longos ou em rocha muito fraturada, e a survey documenta essa trajetória real.
- **Assay** (análises): intervalos de profundidade (de–até) com os resultados de laboratório — teor de cada elemento ou variável de interesse por intervalo amostrado.
- **Lithology / geologia** (ou outras tabelas de atributos categóricos): intervalos de profundidade com litologia, alteração, mineralização, estrutura — cada atributo descrito em sua própria tabela de intervalos, que pode ter uma quebra de profundidade diferente da tabela de assay.

Essas tabelas convergem num processo chamado **desaggregação espacial** (*desurveying*): a partir do colar (ponto de partida) e da survey (a trajetória angular medida), calcula-se a posição $X,Y,Z$ tridimensional de cada ponto ao longo do furo — e, por extensão, de cada intervalo de amostra. O método padrão para isso é a **interpolação de mínima curvatura** entre estações de survey sucessivas, que ajusta um arco circular suave entre duas medições de azimute/mergulho em vez de assumir segmentos retos entre elas. Entre os métodos de segmento reto vale distinguir dois, porque eles não são equivalentes: o **tangencial simples** (*tangential*) assume que o furo mantém a direção da última estação medida até a estação seguinte — o que produz saltos bruscos de direção a cada medição e os maiores erros de posição de toda a família de métodos, a ponto de a literatura de perfuração direcional recomendar abandoná-lo; já o **tangencial balanceado** (*balanced tangential*) pondera igualmente as direções das duas estações e alcança exatidão comparável à da mínima curvatura. É só depois desse cálculo que cada intervalo de amostra tem uma posição 3D definida, e é essa posição — não a profundidade ao longo do furo — que entra no variograma e na krigagem.

### Validação: o que se checa antes de liberar a base

A validação de banco de dados busca inconsistências que, se não corrigidas, distorcem silenciosamente a geometria ou os teores. As checagens padrão incluem:

- **Sobreposição de intervalos**: duas linhas de assay (ou de litologia) para o mesmo furo cujo intervalo de profundidade se sobrepõe — sintoma comum de erro de digitação ou de duplicação de importação.
- **Vazios (*gaps*) não documentados**: trechos do furo sem amostra e sem justificativa (perda de testemunho, por exemplo) registrada — importante distinguir de um vazio real assumido como valor ausente.
- **Profundidade de amostra além da profundidade final do furo**: intervalo de assay que começa ou termina depois do comprimento total perfurado registrado no collar.
- **Furos sem survey ou com survey incompleta**: sem trajetória medida, a desaggregação assume o furo reto na direção de colimação planejada — uma aproximação que pode divergir bastante da posição real, sobretudo em furos profundos.
- **Consistência de coordenadas**: collars fora da área do projeto, coordenadas trocadas (X por Y), ou sistema de referência (datum, projeção) inconsistente entre campanhas de sondagem de anos diferentes.
- **QA/QC de laboratório**: inserção sistemática de **duplicatas** (a mesma amostra enviada duas vezes, para medir precisão analítica), **padrões/referências certificadas** (amostras de teor conhecido, para medir exatidão/viés do laboratório) e **brancos** (material estéril, para detectar contaminação entre amostras) — os resultados desses três tipos de amostra de controle são a evidência de que os teores da base são confiáveis antes de qualquer estatística ser calculada sobre eles.

Nenhuma dessas checagens é geoestatística — são checagens de integridade de banco de dados e de controle de qualidade analítica —, mas todas são pré-condição para a etapa seguinte: sem elas, a composição por bancada, a estatística descritiva e a variografia do Módulo 20 estariam operando sobre um terreno que não é o que a base afirma ser.

### O modelo de blocos: revisão e o que muda a partir daqui

O **modelo de blocos** já apareceu implicitamente no Módulo 20 como o destino da krigagem de bloco (Aula 05): uma malha tridimensional regular de células (blocos) que discretiza o volume do depósito, cada uma recebendo, ao final da estimativa, um teor interpolado e demais atributos (densidade, código de domínio geológico, classificação de recurso). Vale fixar os parâmetros que o definem, porque este módulo vai popular esse modelo com métodos mais sofisticados do que a krigagem ordinária simples:

- **Origem**: o canto de referência (tipicamente inferior, sudoeste) a partir do qual a malha é construída.
- **Tamanho do bloco** ($\Delta x, \Delta y, \Delta z$): a dimensão de cada célula. A regra prática consolidada ancora o tamanho do bloco na **malha de sondagem**: um tamanho de bloco horizontal entre um quarto e a metade do espaçamento médio entre furos é considerado razoável — blocos muito menores que isso criam uma falsa impressão de resolução (o modelo "parece" mais detalhado do que a informação amostral sustenta) e blocos muito maiores diluem variações reais do depósito. Vale registrar que essa regra é um **ponto de partida**, não um critério de decisão: a prática atual submete o tamanho escolhido a uma análise quantitativa da vizinhança de krigagem (*QKNA*), que o julga por métricas de qualidade da estimativa — eficiência de krigagem e inclinação da regressão — em vez de fixá-lo só pela malha.
- **Rotação**: os modelos de blocos podem ser alinhados aos eixos $X,Y,Z$ ou rotacionados para acompanhar a orientação estrutural principal do corpo mineralizado (por exemplo, o rumo e o mergulho de um corpo tabular) — rotacionar o modelo evita blocos artificialmente cortados na diagonal por um corpo que não é paralelo à malha regular.
- **Subcelas (*sub-blocking*/*sub-celling*)**: dentro de um bloco "pai" de tamanho regular, permite-se dividir localmente em blocos menores ao longo dos limites de um contato geológico ou da superfície topográfica — assim o volume ocupado por um domínio geológico é representado com mais fidelidade sem abandonar a regularidade do modelo como um todo (só nas bordas há subdivisão; o interior de um domínio permanece em blocos de tamanho pleno).

O que a krigagem ordinária (Módulo 20, Aula 05) já resolve — estimar o teor de cada bloco como uma combinação linear ponderada das amostras vizinhas, com pesos calculados a partir de um único variograma ajustado à variável contínua — continua sendo a ferramenta de base. O que muda a partir da Aula 02 deste módulo é o tipo de variável e o tipo de variograma: em vez de assumir que a distribuição da variável é razoavelmente próxima da normal (implícito ao usar diretamente o variograma dos teores brutos), a geoestatística **não paramétrica** transforma a variável antes de modelar sua continuidade espacial — o primeiro passo para lidar com distribuições muito assimétricas e com múltiplos limiares de decisão (por exemplo, o **teor de corte** econômico, definido na Aula 02), que a krigagem ordinária de teores brutos, sozinha, não endereça bem.

## Exemplo trabalhado

**Situação:** um geólogo de recursos recebe uma base de dados consolidada de três campanhas de sondagem e roda uma checagem de validação em um furo específico, o furo DDH-014. A tabela de assay traz estes registros de profundidade (metros) e teor de Au (g/t):

| De (m) | Até (m) | Au (g/t) |
|---|---|---|
| 40,0 | 42,0 | 1,10 |
| 42,0 | 44,0 | 0,85 |
| 43,5 | 45,5 | 2,30 |
| 45,5 | 48,0 | 0,60 |

O collar do DDH-014 registra profundidade final de 46,0 m. A survey do furo tem apenas uma estação, no colar (profundidade 0 m).

**Pergunta:** que problemas de validação essa base apresenta, e que ação cada um exige antes da base ser liberada para composição e krigagem?

**Resolução:**

1. **Sobreposição de intervalos**: o intervalo 42,0–44,0 m e o intervalo 43,5–45,5 m se sobrepõem entre 43,5 m e 44,0 m — dois teores diferentes (0,85 g/t e 2,30 g/t) reivindicando o mesmo trecho físico do furo. Isso não pode ser composto ou creditado a um bloco sem resolução: é preciso voltar ao boletim de laboratório original (não à planilha consolidada) para determinar qual dos dois intervalos é o correto — tipicamente um erro de nova amostragem sobreposta a um intervalo já lançado, ou um erro de digitação de profundidade.
2. **Amostra além da profundidade final do furo**: o intervalo 45,5–48,0 m se estende 2,0 m além dos 46,0 m de profundidade final registrados no collar. Ou a profundidade final do collar está errada (o furo foi mais fundo do que o registrado), ou o intervalo de assay tem erro de digitação de profundidade — de novo, checagem contra o boletim original antes de aceitar qualquer um dos dois números.
3. **Survey incompleta**: uma única estação no colar não documenta a trajetória do furo — a desaggregação assume o furo reto ao longo de toda a extensão perfurada (46 m), uma aproximação que pode divergir significativamente da posição real caso o furo tenha desviado, e que o projeto deveria evitar aceitar sem, no mínimo, uma survey final de fundo de furo.

Nenhum desses três problemas é corrigível "estatisticamente" — cada um exige voltar à fonte primária do dado (boletim de laboratório, relatório de perfuração) para resolver a ambiguidade, e só depois disso a base pode alimentar a composição por bancada e a krigagem do Módulo 20.

## Recap relâmpago

- Uma base de dados de sondagem é **relacional**: collar (posição de superfície), survey (trajetória angular), assay (teores por intervalo) e litologia (atributos categóricos por intervalo) se combinam pela **desaggregação espacial** (*desurveying*, tipicamente por mínima curvatura) para dar a cada amostra uma posição 3D.
- A **validação** checa sobreposição de intervalos, vazios não documentados, amostras além da profundidade final do furo, furos sem survey adequada, consistência de coordenadas entre campanhas e o QA/QC de laboratório (duplicatas, padrões, brancos) — é pré-condição de integridade, não uma etapa geoestatística, e resolve-se voltando à fonte primária do dado.
- O **modelo de blocos** é definido por origem, tamanho de bloco (ancorado na malha de sondagem — tipicamente um quarto a metade do espaçamento entre furos, como ponto de partida a ser confirmado por análise quantitativa da vizinhança de krigagem), rotação (alinhada à estrutura do corpo, quando relevante) e subcelas (refinamento local nas bordas de um domínio, sem abandonar a regularidade geral).
- A krigagem ordinária do Módulo 20 continua sendo a ferramenta de base; o que este módulo acrescenta, a partir da Aula 02, é tratar variáveis por transformação (indicadora, log-normal) em vez de estimar diretamente o teor bruto — o passo necessário quando a distribuição é muito assimétrica ou quando o interesse está em múltiplos limiares de decisão.

## Próxima aula

Aula 02 — Geoestatística não paramétrica: variáveis contínuas, categóricas, booleanas e indicadoras. A partir de uma base já validada e de um modelo de blocos já definido, o módulo passa a tratar o problema central: como estimar uma variável sem assumir sua distribuição, transformando-a em **indicadora**.

## Fontes

- Sinclair, A. J. & Blackwell, G. H. (2002), *Applied Mineral Inventory Estimation*, Cambridge University Press, capítulo 3 (organização e validação de bancos de dados de sondagem; desaggregação espacial e métodos de cálculo de trajetória) e capítulo 4 (modelo de blocos: parametrização, tamanho de bloco e regras práticas de dimensionamento a partir da malha de amostragem).
- Rossi, M. E. & Deutsch, C. V. (2014), *Mineral Resource Estimation*, Springer, capítulo 3 (banco de dados: estrutura relacional, QA/QC — duplicatas, padrões, brancos — e checagens de validação) e capítulo 5 (modelo de blocos: origem, rotação, subcelas).
- Isaaks, E. H. & Srivastava, R. M. (1989), *An Introduction to Applied Geostatistics*, Oxford University Press (revisão de krigagem ordinária e de bloco, referência ao Módulo 20).
- PetroWiki (Society of Petroleum Engineers), *Calculation methods for directional survey* — comparação dos métodos tangencial, tangencial balanceado, ângulo médio, raio de curvatura e mínima curvatura, e a exatidão relativa de cada um.
- Deutsch, J. L. & Deutsch, C. V., *Quantitative Kriging Neighbourhood Analysis (QKNA)*, Geostatistics Lessons — avaliação quantitativa de tamanho de bloco e vizinhança de busca por eficiência de krigagem e inclinação da regressão.

<!--
nivel: avancado
palavras_corpo: 1980
mapa_objetivo_secao:
  geologia-avancado-m21-oa01: "O que o Módulo 20 assumiu pronto" + "As tabelas de uma base de dados de furos de sonda" + "Validação: o que se checa antes de liberar a base" + "O modelo de blocos: revisão e o que muda a partir daqui" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOMOD-M21-A01-DESURVEY-001
    claim: "A desaggregação espacial (desurveying) de um furo de sondagem calcula a posição 3D de cada intervalo de amostra a partir da posição do colar (survey de superfície) e da trajetória angular medida (azimute e mergulho em estações de profundidade), tipicamente pelo método de interpolação de minima curvatura entre estações sucessivas, que ajusta um arco circular suave em vez de assumir segmentos retos. Entre os métodos de segmento reto, o tangencial simples assume a direção da ultima estação medida ate a seguinte e produz os maiores erros de posição da família (a literatura de perfuração direcional recomenda abandoná-lo), enquanto o tangencial balanceado pondera igualmente as duas estações e atinge exatidão comparável a da minima curvatura — os dois NAO sao equivalentes e nao devem ser agrupados."
    risk: fato
    source: "Sinclair & Blackwell (2002), Applied Mineral Inventory Estimation, Cambridge University Press, capítulo 3; Rossi & Deutsch (2014), Mineral Resource Estimation, Springer, capítulo 3; PetroWiki (SPE), 'Calculation methods for directional survey'; Seequent, 'Borehole Desurveying Options'."
    revisao: "2026-09-18 — auditoria 🟠 3: a versão anterior agrupava 'balanced tangential' com o método tangencial cru como se ambos subestimassem a curvatura. Corrigido: o tangencial balanceado tem exatidão comparável à da mínima curvatura; quem deve ser abandonado é o tangencial simples."
  - claim_id: GEOMOD-M21-A01-ESTRUTURARELACIONAL-002
    claim: "Uma base de dados de sondagem mineral é estruturada como um banco relacional com, no mínimo, quatro tabelas conectadas pelo identificador do furo: collar (posição de superfície), survey (trajetória angular por profundidade), assay (teores por intervalo de profundidade) e litologia/atributos categóricos (por intervalo de profundidade, com quebras possivelmente diferentes das do assay)."
    risk: fato
    source: "Sinclair & Blackwell (2002), capítulo 3; Rossi & Deutsch (2014), capítulo 3."
  - claim_id: GEOMOD-M21-A01-QAQC-003
    claim: "O controle de qualidade analítica (QA/QC) de uma base de sondagem se apoia na inserção sistemática de três tipos de amostra de controle: duplicatas (mesma amostra reanalisada, medindo precisão), padrões/referências certificadas (teor conhecido, medindo exatidão/viés do laboratório) e brancos (material estéril, detectando contaminação cruzada entre amostras) — os três juntos formam a evidência mínima de confiabilidade analítica antes de qualquer estatística ser calculada sobre os teores."
    risk: fato
    source: "Rossi & Deutsch (2014), Mineral Resource Estimation, Springer, capítulo 3 (QA/QC); Sinclair & Blackwell (2002), capítulo 3."
  - claim_id: GEOMOD-M21-A01-TAMANHOBLOCO-004
    claim: "Uma regra prática consolidada para dimensionar o tamanho horizontal de um bloco no modelo de blocos é ancorá-lo na malha de sondagem, usando um valor entre um quarto e a metade do espaçamento médio entre furos — blocos menores criam resolução aparente não sustentada pela densidade de amostragem, blocos maiores diluem variações reais do depósito. A regra é um ponto de partida, nao um criterio de decisao: a pratica atual confirma o tamanho escolhido por analise quantitativa da vizinhanca de krigagem (QKNA), julgando-o por eficiencia de krigagem e inclinacao da regressao."
    risk: fato
    source: "SME Mining Engineering Handbook (regra de 1/4 a 1/2 do espaçamento médio de sondagem); Sinclair & Blackwell (2002), Applied Mineral Inventory Estimation, capítulo 4 (dimensionamento de bloco); Rossi & Deutsch (2014), capítulo 5; Deutsch & Deutsch, 'Quantitative Kriging Neighbourhood Analysis', Geostatistics Lessons."
    revisao: "2026-09-18 — auditoria 🟡 15: a faixa 1/4–1/2 foi confirmada contra o SME Mining Engineering Handbook; acrescentada a ressalva de que a regra é ponto de partida e não critério, alinhando com a recomendação de QKNA já registrada na auditoria do Módulo 20."
  - claim_id: GEOMOD-M21-A01-SUBCELAS-005
    claim: "O sub-blocking (subcelas) permite dividir localmente um bloco 'pai' de tamanho regular em blocos menores ao longo de limites de contato geológico ou da superfície topográfica, refinando a representação volumétrica de um domínio apenas nas bordas, sem abandonar a regularidade do modelo de blocos como um todo."
    risk: fato
    source: "Rossi & Deutsch (2014), Mineral Resource Estimation, Springer, capítulo 5 (parametrização do modelo de blocos, sub-celling)."
-->
