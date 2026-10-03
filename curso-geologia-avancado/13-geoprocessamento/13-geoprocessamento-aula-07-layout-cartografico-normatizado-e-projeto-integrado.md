# Aula 07: Layout cartográfico normatizado e projeto integrado de geoprocessamento

**ID:** geologia-avancado-m13-a07
**Módulo:** [[13-geoprocessamento-modulo|Módulo 13 — Geoprocessamento]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** montar um layout cartográfico normatizado, com todos os elementos obrigatórios de um mapa técnico, e integrar os produtos das aulas anteriores do módulo num fluxo de trabalho coerente, do dado bruto ao mapa final entregável.
**Ao final você vai conseguir:** listar e posicionar corretamente os elementos obrigatórios de um layout cartográfico técnico; escolher uma paleta de cores e uma classificação adequadas ao tipo de dado representado; e traçar o fluxo de trabalho completo de um projeto de geoprocessamento, da aquisição de dados ao mapa impresso ou digital final.
**Pré-requisito:** todas as aulas anteriores deste módulo (01-06). Esta é a aula de fechamento do módulo — ela não introduz uma técnica nova de análise espacial, mas reúne o que as seis aulas anteriores ensinaram em um produto final entregável e num fluxo de trabalho reproduzível.

## Conteúdo

### Por que o layout é parte do produto, não um acabamento

As seis aulas anteriores deste módulo trataram de como obter, estruturar e processar dados espaciais corretamente — sistema de referência (Aula 01), estrutura vetorial e matricial (Aula 02), aquisição de campo (Aula 03), operações vetoriais (Aula 04), interpolação (Aula 05) e produtos de MDE (Aula 06). Mas um projeto de geoprocessamento raramente termina numa tela de SIG: ele termina num **mapa entregável** — impresso, em PDF, ou publicado digitalmente — que precisa comunicar a informação de forma correta e autossuficiente para quem o lê sem ter acesso ao projeto de SIG original. Um mapa sem os elementos que permitem sua leitura e verificação independente (escala, orientação, sistema de referência, legenda) não é apenas um mapa "menos bonito" — é um documento tecnicamente incompleto, no mesmo sentido em que uma análise química sem unidades declaradas (retomando um princípio já visto no Módulo 02, Hidrogeoquímica) é uma análise incompleta, mesmo que os números estejam corretos.

### Os elementos obrigatórios de um layout cartográfico técnico

Um mapa técnico — geológico, hidrogeológico, de risco, geoquímico, qualquer produto cartográfico derivado de um projeto de SIG — segue uma convenção consolidada de elementos que devem estar presentes para que o mapa seja lido e verificado de forma independente:

1. **Título**: identifica de forma inequívoca o que o mapa representa, incluindo a área e, quando relevante, a data ou período dos dados.
2. **Corpo do mapa**: a área de dados propriamente dita, ocupando a maior proporção do layout.
3. **Legenda**: a chave de interpretação de cada símbolo, cor ou padrão usado no mapa — obrigatória sempre que houver mais de uma classe de informação representada, e organizada de forma lógica (por exemplo, da unidade mais antiga para a mais recente, num mapa geológico, seguindo a convenção estratigráfica).
4. **Escala gráfica e escala numérica**: a escala gráfica (uma barra com subdivisões representando distâncias reais) é preferível à escala numérica isolada porque permanece correta mesmo que o mapa seja redimensionado (ampliado ou reduzido) na reprodução — uma armadilha comum é publicar um mapa com apenas a escala numérica (ex. "1:50.000") e depois redimensionar o arquivo para caber num relatório, invalidando silenciosamente essa informação, enquanto a escala gráfica se redimensiona proporcionalmente junto com o mapa.
5. **Orientação (norte)**: uma seta ou rosa dos ventos indicando a direção norte do mapa — sempre necessária, mesmo que a convenção usual seja norte para cima, porque nem todo mapa segue essa convenção (mapas rotacionados para melhor aproveitamento do layout, por exemplo) e o símbolo remove qualquer ambiguidade.
6. **Sistema de referência**: declaração explícita do datum e da projeção usados (retomando diretamente a Aula 01) — informação sem a qual um usuário do mapa não consegue sobrepor corretamente esse produto a nenhuma outra base de dados espacial.
7. **Grade de coordenadas**: linhas ou marcas ao longo da borda do mapa indicando valores de coordenada (geográfica ou UTM), permitindo localizar qualquer ponto do mapa em coordenadas reais sem depender de um SIG.
8. **Fonte dos dados e autoria**: identifica a origem de cada camada de dados usada (órgão, levantamento, data) e quem produziu o mapa — essencial para rastreabilidade e para que um usuário avalie a confiabilidade do produto.
9. **Notas técnicas**, quando aplicável: informação adicional necessária à interpretação correta — método de interpolação usado num mapa de isovalores, limiar de acumulação de fluxo numa rede de drenagem derivada, precisão do georreferenciamento de uma base histórica — os detalhes metodológicos discutidos nas aulas anteriores deste módulo que, sem essa nota, ficariam invisíveis para quem só vê o produto final.

```
Esquema de layout cartográfico técnico (elementos obrigatórios)

┌─────────────────────────────────────────────┐
│  TÍTULO DO MAPA                              │
├───────────────────────────────┬─────────────┤
│                                 │  LEGENDA    │
│                                 │             │
│         CORPO DO MAPA          │  N          │
│      (grade de coordenadas     │  ↑          │
│       nas bordas)              │             │
│                                 │  Escala     │
│                                 │  ├──┼──┤    │
│                                 │  0  1  2 km │
├─────────────────────────────────────────────┤
│ Sistema de referência: SIRGAS2000, UTM 23S   │
│ Fonte dos dados / Autoria / Notas técnicas   │
└─────────────────────────────────────────────┘
```
A legenda a reter: nenhum desses elementos é decorativo — cada um remove uma ambiguidade específica que, sem ele, obrigaria o leitor a confiar cegamente ou a não conseguir usar o mapa de forma independente.

### Escolha de paleta de cores e classificação

A escolha de cores e da forma de classificar os dados representados não é uma questão estética isolada — ela comunica (ou distorce) a estrutura do dado. Três tipos de paleta atendem a três tipos de dado:

- **Paletas sequenciais** (uma progressão de cor clara a escura, ou de uma cor a outra em gradiente único) são adequadas a dados **ordenados** que variam ao longo de um único eixo de magnitude — um mapa de declividade, um mapa hipsométrico, um mapa de concentração geoquímica.
- **Paletas divergentes** (duas cores que divergem de um ponto médio neutro, como azul-branco-vermelho) são adequadas a dados que têm um **ponto de referência significativo** em torno do qual a interpretação muda de sentido — por exemplo, um mapa de anomalia em relação a um valor de referência (background geoquímico), onde valores acima e abaixo do ponto médio têm significados distintos, não apenas magnitudes diferentes.
- **Paletas qualitativas** (cores distintas, sem ordem inerente entre si) são adequadas a dados **categóricos**, sem relação de ordem — como um mapa geológico, onde cada unidade litoestratigráfica recebe uma cor própria e nenhuma cor é "maior" ou "menor" que outra (ainda que a convenção cartográfica geológica siga uma lógica cromática consolidada por período, uma tradição de nomenclatura de cores associada a cada sistema/período geológico, e não uma escala contínua).

O método de **classificação** de um dado contínuo (como um mapa de declividade ou de teor interpolado) em classes discretas para exibição — quantos intervalos usar e onde colocar os limites entre eles — também altera a leitura do mapa mesmo sem alterar nenhum dado subjacente: métodos comuns incluem intervalos iguais (classes de mesma amplitude numérica), quantis (classes com o mesmo número de observações em cada uma) e quebras naturais (os limites de classe posicionados onde há saltos reais na distribuição dos dados, minimizando a variância dentro de cada classe) — a escolha do método pode fazer o mesmo conjunto de dados parecer mais ou menos uniforme, mais ou menos preocupante (no caso de um mapa de risco, por exemplo), sem que um único valor de dado tenha mudado.

### O projeto integrado: do dado bruto ao mapa final

Encerrando o módulo, vale reconstruir o fluxo de trabalho completo que as seis aulas anteriores, tomadas em conjunto, definem — a sequência que um projeto real de geoprocessamento em geociências percorre:

1. **Definição do sistema de referência do projeto** (Aula 01): antes de qualquer dado entrar, decide-se o datum, a projeção e a escala de trabalho, documentando essa decisão para todo o projeto.
2. **Estruturação da base de dados** (Aula 02): planejamento de quais camadas serão vetoriais e quais serão matriciais, com esquema de atributos e organização (geodatabase, nomenclatura, separação bruto/derivado) definidos antes da entrada maciça de dados.
3. **Aquisição e incorporação de dados** (Aula 03): dados de campo coletados digitalmente e importados por coordenada, mapas históricos georreferenciados, todos trazidos para o sistema de referência único do projeto — nenhum dado entra sem essa conversão.
4. **Análise vetorial** (Aula 04): operações de sobreposição, buffer e dissolve combinam as camadas de entrada para responder as perguntas analíticas do projeto — proximidade, área de interseção, agregação por classe.
5. **Interpolação espacial**, quando aplicável (Aula 05): pontos amostrados de variáveis contínuas (geoquímica, nível d'água) são transformados em superfícies raster, com o método de interpolação e sua validação documentados junto ao produto.
6. **Produtos morfométricos e hidrológicos**, quando aplicável (Aula 06): a partir de um MDE, derivam-se declividade, hipsometria, rede de drenagem e lineamentos candidatos, sempre com a ressalva de que lineamentos remotos são hipóteses a verificar em campo.
7. **Layout e entrega** (esta aula): os produtos das etapas anteriores são organizados num layout com todos os elementos obrigatórios, paleta e classificação escolhidas de forma consciente para o tipo de dado, e entregues com a documentação metodológica que permite a outro profissional reproduzir ou auditar o resultado.

Essa sequência não é rígida — um projeto real itera entre as etapas (um mapa preliminar revela a necessidade de mais pontos de amostragem, por exemplo, retomando a base) — mas a disciplina de manter cada etapa documentada e o sistema de referência consistente do início ao fim é o que separa um projeto de geoprocessamento profissionalmente defensável de um conjunto de mapas bonitos, mas não verificáveis.

## Exemplo trabalhado

**Situação:** um relatório técnico de avaliação de área contaminada (retomando o tema do Módulo 03) precisa apresentar um mapa final combinando: um raster de concentração de contaminante interpolado por krigagem (Aula 05, a partir de 22 poços de monitoramento), um polígono vetorial da área urbana consolidada — a mesma camada do exemplo trabalhado da Aula 04, ali cruzada com o buffer da falha e aqui reaproveitada apenas como camada de contexto, e a rede de drenagem derivada de um MDE local (Aula 06). O mapa será publicado em um relatório técnico impresso em tamanho A4. Liste as decisões de layout que esse mapa específico exige, além dos elementos obrigatórios genéricos já listados.

**Resolução:**

Além dos nove elementos obrigatórios (título, corpo, legenda, escala gráfica, norte, sistema de referência, grade de coordenadas, fonte/autoria, notas técnicas), este mapa específico — por combinar um raster de concentração, um polígono de contexto e uma rede de drenagem vetorial — exige decisões adicionais coerentes com o conteúdo:

*Paleta*: a concentração de contaminante é um dado ordenado (magnitude crescente), então recebe uma **paleta sequencial** — mas se o relatório precisar destacar especificamente os pontos que excedem um valor de referência regulatório (retomando a lógica de padrão de qualidade discutida no Módulo 03), uma **paleta divergente**, centrada no valor de referência, comunica de forma mais direta "onde está acima do limite" do que uma sequencial pura, que só mostra gradiente de magnitude sem destacar esse ponto de corte específico.

*Classificação*: como o mapa tem finalidade regulatória (avaliar exposição a um valor de referência), o método de classificação apropriado não é quantil nem intervalo igual genérico — é uma classificação com **um limite de classe fixado exatamente no valor de referência regulatório**, mesmo que isso produza classes de tamanho numérico desigual, porque o que importa para o leitor do relatório é a posição de cada área em relação ao limite legal, não uma divisão estatisticamente "equilibrada" da distribuição dos dados.

*Nota técnica obrigatória*: como o raster de concentração vem de uma interpolação por krigagem (Aula 05), a nota técnica do mapa deve declarar o método de interpolação usado e, idealmente, incluir ou referenciar a informação de incerteza (variância de krigagem) — sem essa nota, o leitor do relatório não tem como saber que a superfície contínua exibida é uma estimativa com confiabilidade variável no espaço, não uma medição direta em todo lugar, distinção crítica em qualquer decisão sobre uma área contaminada.

*Camadas de contexto*: o polígono de área urbana e a rede de drenagem devem aparecer como camadas de **contexto** visualmente subordinadas ao raster de concentração (que é o dado principal do mapa) — usando cores neutras (cinza, contorno fino) para não competir visualmente com a paleta sequencial/divergente do raster, e entrando na legenda como categorias separadas e claramente identificadas, não misturadas à escala de cor do contaminante.

*Formato A4*: como o layout final é impresso em A4, a escala do mapa precisa ser escolhida de forma que a área de interesse caiba de forma legível nesse formato — retomando diretamente a Aula 01 (a razão entre distância no mapa e no terreno) e o cuidado de usar escala gráfica, não apenas numérica, justamente porque documentos impressos são frequentemente redimensionados na diagramação final do relatório.

## Erros comuns

- **Publicar um mapa só com escala numérica e depois redimensionar o arquivo.** É a armadilha nomeada explicitamente na aula: a escala numérica vira silenciosamente incorreta ao ampliar/reduzir o documento, enquanto a escala gráfica se ajusta proporcionalmente e continua correta.
- **Usar paleta sequencial para um dado com ponto de referência significativo** (um limite regulatório, um valor de background). Como o exemplo trabalhado mostra, uma sequencial só comunica gradiente de magnitude — quando o que importa é "acima ou abaixo do limite", a paleta divergente centrada nesse valor comunica a informação certa.
- **Escolher classificação por quantil ou intervalo igual quando existe um limite normativo relevante.** Dividir estatisticamente os dados quando a pergunta real é regulatória (está acima ou abaixo do valor legal) esconde exatamente a fronteira que o leitor do mapa precisa ver.
- **Tratar camadas de contexto (drenagem, área urbana) com o mesmo destaque visual do dado principal.** Isso faz o mapa competir consigo mesmo — camadas de contexto pedem cores neutras e legenda separada, subordinadas ao dado que o mapa existe para comunicar.

## O que não concluir

- **Que um mapa com aparência profissional é, por isso, metodologicamente válido.** É exatamente o fio condutor que fecha o módulo: a aparência não garante nada sobre a qualidade dos dados ou a adequação do método — só a documentação nas notas técnicas permite auditar isso.
- **Que a sequência das sete etapas do projeto integrado é rígida e linear.** Um projeto real itera — um mapa preliminar pode revelar a necessidade de mais amostragem, retomando etapas anteriores — a disciplina de documentação é o que importa manter, não seguir a ordem sem retorno.
- **Que notas técnicas são um adendo opcional para mapas "mais informais".** Sem elas, informação metodológica central (método de interpolação, limiar de rede de drenagem, precisão de georreferenciamento) fica invisível para quem só vê o produto final — e essa invisibilidade é justamente o que torna um mapa não auditável.

## Recap relâmpago

- Um layout cartográfico técnico exige nove elementos obrigatórios: título, corpo do mapa, legenda, escala gráfica e numérica, orientação/norte, sistema de referência declarado, grade de coordenadas, fonte de dados/autoria, e notas técnicas quando aplicável.
- A escala gráfica é preferível à numérica isolada porque permanece correta mesmo se o mapa for redimensionado na reprodução.
- A paleta de cores deve corresponder ao tipo de dado: sequencial para dados ordenados contínuos, divergente para dados com um ponto de referência significativo, qualitativa para dados categóricos sem ordem inerente.
- O método de classificação de um dado contínuo (intervalos iguais, quantis, quebras naturais, ou um limite fixado por norma) altera a leitura visual do mapa mesmo sem alterar nenhum valor de dado — a escolha deve ser deliberada, não padrão de software.
- O fluxo de trabalho completo de um projeto de geoprocessamento encadeia as seis aulas anteriores do módulo: sistema de referência, estrutura de dados, aquisição, análise vetorial, interpolação e produtos de MDE, culminando no layout e na entrega documentada.
- Documentar a metodologia (interpolador usado, limiar de rede de drenagem, precisão de georreferenciamento) nas notas técnicas do mapa é o que torna o produto final auditável e reprodutível por outro profissional, e não apenas visualmente convincente.

## Encerramento do módulo

Este módulo percorreu a cadeia completa do geoprocessamento em geociências: da referência geodésica que ancora qualquer coordenada ao terreno real (Aula 01), passando pela estrutura de dados que organiza a informação espacial (Aula 02), pela entrada correta de dados de campo e históricos (Aula 03), pelas operações analíticas vetoriais (Aula 04), pela transformação de amostras pontuais em superfícies contínuas (Aula 05), pelos produtos derivados de relevo e hidrologia (Aula 06), até o produto final entregável e auditável (esta aula). O fio condutor que atravessa as sete aulas é sempre o mesmo: um projeto de SIG produz mapas com aparência profissional independentemente da qualidade real dos dados ou da adequação do método escolhido — a responsabilidade de garantir que a aparência corresponda à validade real do resultado é sempre do analista, nunca do software.

## Fontes

- Slocum, T. A., McMaster, R. B., Kessler, F. C. & Howard, H. H. (2022), *Thematic Cartography and Geovisualization*, 4ª ed., CRC Press, cap. 5, 8-10 (elementos de layout, paletas de cor, classificação de dados).
- Brewer, C. A. (2016), *Designing Better Maps: A Guide for GIS Users*, 2ª ed., ESRI Press, cap. 4-6 (esquemas de cor sequencial, divergente, qualitativo).
- ABNT NBR 13133:2021, *Execução de levantamento topográfico — Procedimento* (edição vigente; cancelou e substituiu as versões de 1994 e de 2015).
- Brasil, Decreto nº 89.817/1984, *Instruções Reguladoras das Normas Técnicas da Cartografia Nacional* (define o Padrão de Exatidão Cartográfica usado na Aula 03).
- Especificações técnicas da INDE, publicadas pela DSG (Diretoria de Serviço Geográfico do Exército Brasileiro) e homologadas pela CONCAR: **ET-EDGV** (estruturação de dados geoespaciais vetoriais), **ET-ADGV** (aquisição de dados geoespaciais vetoriais) e **ET-RDG** (representação de dados geoespaciais — a mais próxima das decisões de simbologia e layout tratadas nesta aula).

<!--
nivel: avancado
palavras_corpo: 2310  # recontado apos auditoria + revisao didatica (2026-09-08)
mapa_objetivo_secao:
  geologia-avancado-m13-oa04: "Por que o layout é parte do produto, não um acabamento" + "Os elementos obrigatórios de um layout cartográfico técnico" + "Escolha de paleta de cores e classificação" + "O projeto integrado: do dado bruto ao mapa final" + "Exemplo trabalhado" + "Encerramento do módulo"

alegacoes_auditaveis:
  - claim_id: GEOPROC-M13-A07-ELEMENTOS-001
    claim: "Um mapa técnico segue uma convenção cartográfica consolidada de elementos obrigatórios de layout: título, corpo do mapa, legenda, escala (gráfica e numérica), indicação de orientação/norte, sistema de referência declarado (datum e projeção), grade de coordenadas, fonte dos dados e autoria, e notas técnicas quando aplicável."
    risk: fato
    source: "Slocum et al. 2022, Thematic Cartography and Geovisualization, cap. 5; convenção cartográfica padrão consistente com as especificações técnicas da INDE publicadas pela DSG/Exército e homologadas pela CONCAR (ET-RDG, para representação; ET-EDGV/ET-ADGV, para estruturação e aquisição de dados vetoriais)"
    audit_note: "Corrigido na auditoria do Módulo 13 (achado GEOPROC-M13-A07-NORMAS-005, laranja): a sigla ET-ADGV foi expandida como 'Estruturação' (é Aquisição; Estruturação é a ET-EDGV) e atribuída a 'DSG/IBGE' (o IBGE não a publica), e a norma pertinente a layout/simbologia é a ET-RDG."
  - claim_id: GEOPROC-M13-A07-ESCALAGRAFICA-002
    claim: "A escala gráfica (barra com subdivisões representando distâncias reais) permanece geometricamente correta mesmo que o mapa seja redimensionado (ampliado ou reduzido) na reprodução, ao contrário da escala numérica isolada, que se torna incorreta se o mapa for redimensionado sem ajuste do valor declarado."
    risk: fato
    source: "Slocum et al. 2022, Thematic Cartography and Geovisualization, cap. 8; princípio cartográfico consolidado"
  - claim_id: GEOPROC-M13-A07-PALETAS-003
    claim: "Esquemas de cor cartográficos se dividem em sequenciais (para dados ordenados contínuos, progressão de uma cor), divergentes (para dados com ponto de referência significativo, duas cores divergindo de um ponto médio) e qualitativos (para dados categóricos sem ordem inerente, cores distintas sem hierarquia)."
    risk: fato
    source: "Brewer 2016, Designing Better Maps, cap. 4-6; ColorBrewer (Brewer), referência padrão de esquemas de cor cartográficos"
  - claim_id: GEOPROC-M13-A07-CLASSIFICACAO-004
    claim: "Métodos de classificação de dados contínuos para representação em classes discretas incluem intervalos iguais (classes de mesma amplitude numérica), quantis (classes com igual número de observações) e quebras naturais (limites posicionados em saltos reais da distribuição, minimizando variância intraclasse); a escolha do método altera a aparência visual do mapa sem alterar os dados subjacentes."
    risk: fato
    source: "Slocum et al. 2022, Thematic Cartography and Geovisualization, cap. 5 (métodos de classificação de dados: equal interval, quantile, natural breaks/Jenks)"
-->
