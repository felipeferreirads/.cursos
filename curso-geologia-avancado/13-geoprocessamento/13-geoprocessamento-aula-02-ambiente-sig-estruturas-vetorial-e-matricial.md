# Aula 02: Ambiente SIG, estruturas vetorial e matricial e organização de bases de dados espaciais

**ID:** geologia-avancado-m13-a02
**Módulo:** [[13-geoprocessamento-modulo|Módulo 13 — Geoprocessamento]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** distinguir as duas formas fundamentais de representar dados espaciais num SIG — vetorial e matricial — e explicar como organizar uma base de dados espacial coerente para um projeto de geociências.
**Ao final você vai conseguir:** decidir se um dado geológico deve ser representado como vetor ou como matriz (raster); explicar a estrutura de atributos de um dado vetorial; descrever os componentes de um raster (célula, resolução, valor); e organizar camadas de um projeto em um esquema lógico de bases de dados espaciais.
**Pré-requisito:** [[13-geoprocessamento-aula-01-fundamentos-cartograficos|Aula 01 — Fundamentos cartográficos]]. Esta aula assume que você já sabe que todo dado espacial existe dentro de um sistema de referência (datum, projeção, escala) — aqui a pergunta muda de "onde" para "como esse dado é armazenado e estruturado".

## Conteúdo

### O que é um SIG e por que a estrutura de dados importa antes de qualquer análise

Um **Sistema de Informação Geográfica (SIG)**, ou GIS (*Geographic Information System*), é um ambiente de software que integra dados espaciais (com localização definida por coordenadas) e dados de atributo (características associadas a cada localização) para armazenar, consultar, analisar e visualizar informação georreferenciada. A diferença central de um SIG para um editor de desenho comum é justamente essa integração: num SIG, um polígono que representa um afloramento não é só uma forma geométrica — ele carrega, associado a si, uma tabela de atributos com litologia, idade, coordenadas de coleta, número de amostra, e o que mais o projeto exigir. É essa ligação entre geometria e atributo que permite consultas como "mostre todos os afloramentos de idade cretácea a menos de 500 m de uma falha", e é o motivo pelo qual, antes de qualquer operação de geoprocessamento (temas das Aulas 04 e 05), o dado precisa estar bem estruturado.

Todo dado espacial dentro de um SIG é armazenado numa de duas estruturas fundamentalmente diferentes — vetorial ou matricial — e a escolha entre elas não é estética, é funcional: cada estrutura é mais eficiente e mais correta para um tipo de fenômeno geográfico, e usar a errada compromete a análise antes mesmo de ela começar.

### Estrutura vetorial: geometria discreta com atributos

O modelo **vetorial** representa o espaço por meio de geometrias discretas — **pontos**, **linhas** e **polígonos** — cada uma definida por um conjunto de coordenadas (x, y, e opcionalmente z) e associada a uma tabela de atributos. É a estrutura natural para representar feições com limites bem definidos e identidade individual:

- **Pontos**: feições sem dimensão relevante na escala do mapa — um poço, um afloramento, a localização de uma amostra, uma estação de monitoramento.
- **Linhas**: feições unidimensionais — uma falha, um rio, um perfil sísmico, uma estrada, um contato geológico traçado em planta.
- **Polígonos**: feições bidimensionais fechadas — uma unidade litológica mapeada, uma bacia hidrográfica, uma área de concessão mineral, um lago.

Cada feição vetorial carrega, na tabela de atributos associada, quantos campos o projeto exigir — um polígono de unidade litológica pode ter campos para nome da formação, idade, litologia dominante, espessura estimada e fonte de mapeamento. Essa tabela funciona como um banco de dados relacional simples: cada linha da tabela corresponde a uma feição geométrica, e cada coluna a um atributo. A precisão do modelo vetorial é alta para representar limites nítidos (uma falha é uma linha bem definida), mas ele fica ineficiente e conceitualmente inadequado para representar fenômenos que variam de forma contínua no espaço, sem limites naturais — um campo de temperatura, uma superfície de elevação, uma concentração geoquímica interpolada. É exatamente aí que entra o modelo matricial.

### Estrutura matricial (raster): o espaço dividido em células

O modelo **matricial**, ou **raster**, representa o espaço como uma grade regular de células (pixels), cada uma com um único valor numérico associado — elevação, reflectância espectral, concentração de um elemento, classe de uso do solo. Ao contrário do vetor, o raster não tem "feições" individuais com identidade própria: o que existe é uma superfície contínua de valores, amostrada em intervalos regulares.

Os parâmetros que definem um raster são: a **resolução espacial** (o tamanho de cada célula no terreno — por exemplo, um raster de resolução 30 m tem cada célula representando um quadrado de 30 × 30 m no mundo real), a **extensão** (a área total coberta pela grade), o **número de linhas e colunas** e o **tipo de dado** armazenado em cada célula (inteiro, decimal, categórico). A resolução espacial é o parâmetro mais crítico na prática: uma resolução grosseira (célula grande) suaviza detalhes reais do terreno e pode ocultar feições geológicas relevantes (uma pequena falha, um talvegue estreito), enquanto uma resolução fina demais em relação à qualidade dos dados de origem cria uma falsa impressão de precisão — o raster "parece" detalhado, mas o detalhe é artefato da interpolação, não informação real (o mesmo problema de escala discutido na Aula 01, aqui reencarnado como resolução de célula).

```
Vetor vs. raster (esquemático, mesma área)

VETOR (polígono, linha, ponto)          RASTER (grade de células)
  ┌──────╲                               ┌─┬─┬─┬─┬─┐
  │ pol.  ╲___linha (falha)              ├─┼─┼─┼─┼─┤
  │  A     ╲                             ├─┼─┼─┼─┼─┤  cada célula =
  │         •  ponto (amostra)           ├─┼─┼─┼─┼─┤  1 valor numérico
  └──────────╲                           └─┴─┴─┴─┴─┘
  geometria discreta + tabela            grade regular, sem
  de atributos separada                  identidade individual por célula
```
A legenda a reter: o vetor guarda "o quê" e "onde" separadamente (geometria + tabela); o raster guarda "quanto" em cada posição da grade, sem uma tabela de atributos por célula individual.

Um raster do tipo **categórico** (ou temático) usa cada valor de célula para representar uma classe discreta — por exemplo, um mapa de uso do solo em que o valor 1 significa "floresta", 2 significa "pastagem" e assim por diante, geralmente acompanhado de uma tabela de atributos de raster (*raster attribute table*) que traduz cada valor numérico em rótulo. Isso mostra que a fronteira entre vetor e raster não é absoluta: é possível converter um polígono vetorial em raster categórico (processo chamado *rasterização*) e, inversamente, transformar um raster categórico em polígonos vetoriais (*vetorização*), quando a análise exigir a estrutura oposta.

### Quando usar cada estrutura: o critério de decisão

A pergunta que decide entre vetor e raster não é "qual é melhor" — é "o fenômeno tem limites discretos e identidade individual, ou varia continuamente no espaço?". Feições com bordas nítidas, contáveis, com atributos qualitativamente distintos (poços, falhas, polígonos de propriedade, unidades litoestratigráficas mapeadas em planta) pedem vetor. Fenômenos de variação contínua, amostrados ou modelados em toda a extensão de uma área (elevação do terreno, temperatura, concentração geoquímica interpolada, imagem de satélite) pedem raster. Um projeto de geoprocessamento típico em geociências combina os dois: a topografia entra como raster (um modelo digital de elevação, tema central da Aula 06), enquanto falhas, poços e unidades geológicas mapeadas entram como vetor — e boa parte do valor de um SIG está justamente em cruzar as duas estruturas (por exemplo, extrair a elevação de cada ponto de amostragem vetorial a partir de um raster de MDE).

### Organizando a base de dados espacial de um projeto

Um projeto de SIG raramente tem uma única camada — ele acumula dezenas de camadas vetoriais e raster ao longo do tempo, e sem organização a base vira inutilizável. Três práticas sustentam uma base de dados espacial coerente:

1. **Sistema de referência único e documentado**: todas as camadas do projeto devem estar no mesmo datum e sistema de coordenadas (Aula 01), ou pelo menos ter esse dado registrado nos metadados de cada camada, para que a reprojeção, quando necessária, seja feita conscientemente — nunca assumida.
2. **Esquema de nomenclatura e metadados consistente**: cada camada carrega, no nome do arquivo ou em metadados associados, informação sobre conteúdo, data de criação, fonte e versão — prática que evita a armadilha comum de acumular arquivos como "mapa_final_v2_REVISADO.shp" sem saber qual é, de fato, a versão vigente.
3. **Separação entre dados brutos e dados derivados**: manter uma cópia intocada dos dados originais (levantamento de campo, download de órgão oficial) separada dos produtos gerados por processamento (uma interpolação, uma reclassificação), de modo que qualquer etapa de análise possa ser refeita do zero caso um erro seja descoberto — disciplina que se torna decisiva quando o módulo chegar às operações de geoprocessamento propriamente ditas (Aulas 04-06), que costumam ser executadas em várias iterações até o resultado ficar correto.

Um **geodatabase** (formato de banco de dados espacial mais estruturado que um conjunto solto de shapefiles, capaz de armazenar múltiplas camadas vetoriais e raster com regras de integridade, domínios de atributo e relacionamentos entre tabelas) é a ferramenta que a maioria dos SIGs profissionais oferece para impor essa organização de forma sistemática, em vez de depender só da disciplina do usuário.

## Exemplo trabalhado

**Situação:** um projeto de mapeamento geológico regional recebeu os seguintes dados: (1) um modelo digital de elevação SRTM de resolução 30 m cobrindo toda a área; (2) um shapefile de contatos litológicos digitalizados a partir de mapeamento de campo; (3) uma planilha com 40 pontos de amostragem geoquímica (coordenadas UTM e teor de um elemento em ppm); (4) uma imagem de satélite multiespectral da área. Para cada um, decida se a estrutura nativa é vetorial ou matricial, e explique como os dados (3) — inicialmente uma planilha, sem geometria — entram no SIG.

**Resolução:**

O **MDE SRTM** (1) é nativamente **raster**: representa uma superfície contínua de elevação, amostrada em células de 30 × 30 m, sem feições individuais discretas — cada célula é só um valor de altitude. A **imagem de satélite multiespectral** (4) também é **raster**: cada pixel carrega valores de reflectância em várias bandas espectrais, uma grade regular por definição do próprio sensor (tema aprofundado no Módulo 14, Sensoriamento remoto).

Os **contatos litológicos digitalizados** (2) são nativamente **vetoriais**: cada contato é uma linha (ou, se fechado, delimita um polígono de unidade litológica) com identidade individual e atributos associados (nome da unidade, tipo de contato — deposicional, tectônico, intrusivo). Representar contatos como raster seria tecnicamente possível (rasterizando as linhas), mas perderia a precisão geométrica do traço e a capacidade de consultar atributos por feição individual — por isso contatos mapeados permanecem vetoriais na prática.

Os **40 pontos de amostragem geoquímica** (3) chegam ao projeto como uma tabela sem geometria explícita — apenas coordenadas numéricas numa planilha. O procedimento padrão de um SIG é a **importação de tabela de coordenadas XY** ("XY Table to Point", "Adicionar camada de texto delimitado" ou equivalente, conforme o software): a partir dos dois campos de coordenada (X/leste, Y/norte) e do sistema de referência declarado da planilha (que precisa ser conhecido — Aula 01), o SIG gera uma camada vetorial de **pontos**, um por linha da planilha, com todos os demais campos (número da amostra, teor em ppm) transportados automaticamente para a tabela de atributos da nova camada vetorial. A partir desse momento, os 40 pontos existem como uma camada vetorial regular, que pode ser cruzada com o raster de MDE (para extrair a elevação de cada ponto de coleta) ou servir de entrada para um método de interpolação espacial, gerando um raster contínuo de teor estimado em toda a área — a ponte entre estrutura vetorial e matricial que a Aula 05 deste módulo vai explorar em detalhe.

Uma nota de vocabulário, porque a literatura diverge: o glossário da ESRI define *geocodificação* de forma ampla, incluindo a conversão de um par de coordenadas em uma posição — e nesse sentido a operação acima seria "geocodificação por coordenadas". Na maior parte da bibliografia de SIG, porém, *geocodificação* designa especificamente a conversão de **endereços** (texto) em coordenadas, por comparação com uma base de referência de logradouros, que é um problema bem diferente e sujeito a erro de correspondência. Vale nomear a operação pelo que ela faz — importar uma tabela XY — e reservar "geocodificação" para o caso do endereço.

## Erros comuns

- **Escolher raster ou vetor pelo formato de arquivo disponível, não pela natureza do fenômeno.** A pergunta certa é se o fenômeno tem limites discretos e identidade individual (vetor) ou varia continuamente (raster) — forçar um contato geológico nítido em raster, ou uma superfície contínua em polígonos, degrada a análise mesmo que o arquivo "abra sem erro".
- **Usar resolução de célula fina demais em relação à qualidade real dos dados de origem.** Um raster de alta resolução interpolado de dados esparsos parece detalhado, mas o detalhe extra é artefato da interpolação, não informação nova — a mesma armadilha da escala cartográfica da Aula 01, agora como resolução de célula.
- **Chamar qualquer conversão coordenada→ponto de "geocodificação".** Na maior parte da literatura de SIG o termo é reservado à conversão de endereço (texto) em coordenada; confundir os dois nomes numa reunião de projeto pode levar alguém a esperar (e não obter) correspondência com uma base de logradouros.
- **Deixar múltiplas versões de uma camada sem nomenclatura clara ("final_v2_REVISADO").** É o erro que a terceira prática de organização da aula existe para prevenir — sem separação entre dado bruto e derivado, uma análise errada não pode ser refeita do zero com confiança.

## O que não concluir

- **Que vetor é "mais preciso" e raster é "menos preciso" em termos absolutos.** Cada estrutura é mais adequada a um tipo de fenômeno; um raster bem amostrado descreve uma superfície contínua melhor que qualquer vetor poderia, e um vetor mal digitalizado pode ser menos preciso que um raster de boa resolução.
- **Que rasterizar ou vetorizar um dado é uma operação sem perda.** Rasterizar um contato geológico perde a precisão geométrica do traço original; vetorizar um raster categórico introduz simplificação nos limites entre classes — a conversão é uma ferramenta, não uma equivalência.
- **Que um geodatabase resolve organização de projeto sozinho.** Ele impõe regras de integridade, mas sistema de referência documentado e nomenclatura consistente continuam sendo disciplina de quem usa o projeto, não algo que o formato garante por si.

## Recap relâmpago

- Um SIG integra geometria espacial e tabela de atributos, permitindo consultas que cruzam localização e características — a diferença central para um simples editor de desenho.
- O modelo vetorial representa feições discretas (pontos, linhas, polígonos) com identidade individual e atributos em tabela associada; é adequado a feições com limites nítidos.
- O modelo matricial (raster) representa o espaço como grade regular de células, cada uma com um valor numérico; é adequado a fenômenos de variação contínua. Resolução espacial (tamanho de célula) é seu parâmetro mais crítico.
- Vetor e raster são conversíveis (rasterização e vetorização); um projeto típico combina os dois, cruzando informação entre eles.
- Coordenadas em planilha (sem geometria) tornam-se camada vetorial de pontos por importação de tabela XY, desde que o sistema de referência das coordenadas seja conhecido — operação distinta da geocodificação de endereços, com a qual parte da literatura a confunde.
- Uma base de dados espacial bem organizada exige sistema de referência único e documentado, nomenclatura/metadados consistentes e separação entre dados brutos e derivados.

## Próxima aula

[[13-geoprocessamento-aula-03-georreferenciamento-gps-gnss-e-aquisicao-digital-de-dados-em-campo|Aula 03 — Georreferenciamento, GPS/GNSS e aquisição digital de dados em campo]]

## Fontes

- Longley, P. A., Goodchild, M. F., Maguire, D. J. & Rhind, D. W. (2015), *Geographic Information Science and Systems*, 4ª ed., Wiley, cap. 3, 7-8 (modelos vetorial e matricial de dados).
- Burrough, P. A. & McDonnell, R. A. (1998), *Principles of Geographical Information Systems*, Oxford University Press, cap. 2-3.
- ESRI, *ArcGIS Pro Documentation* — Vector and Raster Data Models (documentação técnica de referência de estrutura de dados, consistente com a literatura acadêmica citada).

<!--
nivel: avancado
palavras_corpo: 2000  # recontado apos auditoria + revisao didatica (2026-09-08)
mapa_objetivo_secao:
  geologia-avancado-m13-oa02: "O que é um SIG e por que a estrutura de dados importa antes de qualquer análise" + "Estrutura vetorial: geometria discreta com atributos" + "Estrutura matricial (raster): o espaço dividido em células" + "Quando usar cada estrutura: o critério de decisão" + "Organizando a base de dados espacial de um projeto" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOPROC-M13-A02-SIG-001
    claim: "Um SIG (Sistema de Informação Geográfica) integra dados espaciais (geometria com localização definida por coordenadas) e dados de atributo associados, permitindo armazenamento, consulta, análise e visualização de informação georreferenciada."
    risk: fato
    source: "Longley et al. 2015, Geographic Information Science and Systems, cap. 1"
  - claim_id: GEOPROC-M13-A02-VETOR-002
    claim: "O modelo vetorial representa o espaço por geometrias discretas (pontos, linhas, polígonos), cada uma associada a uma tabela de atributos, sendo adequado para feições com limites bem definidos e identidade individual (ex.: poços, falhas, polígonos de unidades litológicas)."
    risk: fato
    source: "Burrough & McDonnell 1998, Principles of GIS, cap. 2-3; Longley et al. 2015, cap. 3"
  - claim_id: GEOPROC-M13-A02-RASTER-003
    claim: "O modelo matricial (raster) representa o espaço como uma grade regular de células (pixels), cada uma com um único valor numérico associado, definida por resolução espacial (tamanho de célula), extensão, número de linhas/colunas e tipo de dado; é adequado para fenômenos de variação espacial contínua (ex.: elevação, imagens de satélite)."
    risk: fato
    source: "Burrough & McDonnell 1998, cap. 2; Longley et al. 2015, cap. 3"
  - claim_id: GEOPROC-M13-A02-CONVERSAO-004
    claim: "Dados vetoriais e matriciais são interconversíveis: rasterização converte geometria vetorial em raster (útil para representação categórica/temática), vetorização converte raster categórico em polígonos vetoriais."
    risk: fato
    source: "Longley et al. 2015, Geographic Information Science and Systems, cap. 3, 8"
  - claim_id: GEOPROC-M13-A02-GEOCOD-005
    claim: "Uma tabela com coordenadas X/Y numéricas pode ser convertida em camada vetorial de pontos por importação de tabela XY, transportando os demais campos da tabela para os atributos da nova camada; essa conversão exige que o sistema de referência (datum, projeção) das coordenadas da tabela seja conhecido e declarado. O termo 'geocodificação' é usado em sentido amplo pelo glossário da ESRI (incluindo coordenadas), mas na maior parte da bibliografia de SIG designa especificamente a conversão de endereços em coordenadas."
    risk: fato
    source: "ESRI ArcGIS Pro Documentation (XY Table to Point; glossário: geocoding) e QGIS Documentation (Add Delimited Text Layer), consistente com Longley et al. 2015, cap. 4 e 8"
    audit_note: "Ajustado na auditoria do Módulo 13 (achado GEOPROC-M13-A02-GEOCOD-005, branco/controverso): divergência real de nomenclatura entre fontes de mesmo nível, resolvida explicitando as duas acepções em vez de escolher um lado."
  - claim_id: GEOPROC-M13-A02-GEODATABASE-006
    claim: "Um geodatabase é um formato de banco de dados espacial estruturado, capaz de armazenar múltiplas camadas vetoriais e raster com regras de integridade, domínios de atributo e relacionamentos entre tabelas, oferecendo organização mais sistemática que um conjunto solto de arquivos shapefile."
    risk: fato
    source: "ESRI, ArcGIS Pro Documentation — What is a geodatabase; Longley et al. 2015, cap. 7"
-->
