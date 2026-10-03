# Aula 04: Geoprocessamento vetorial: operações espaciais e cálculos com linhas e polígonos

**ID:** geologia-avancado-m13-a04
**Módulo:** [[13-geoprocessamento-modulo|Módulo 13 — Geoprocessamento]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** aplicar as operações espaciais fundamentais de geoprocessamento vetorial — sobreposição, buffer, dissolve e relações topológicas — para responder perguntas analíticas concretas sobre dados geológicos.
**Ao final você vai conseguir:** executar e interpretar as operações de interseção, união e diferença entre camadas vetoriais; construir e usar um buffer; dissolver polígonos por atributo comum; e formular uma consulta espacial combinando várias dessas operações.
**Pré-requisito:** [[13-geoprocessamento-aula-02-ambiente-sig-estruturas-vetorial-e-matricial|Aula 02 — Ambiente SIG, estruturas vetorial e matricial]]. Esta aula assume que você já sabe o que é uma camada vetorial (ponto, linha, polígono) e sua tabela de atributos — aqui a pergunta muda de "como o dado é estruturado" para "que perguntas analíticas dá para responder cruzando camadas vetoriais".

## Conteúdo

### Geoprocessamento vetorial como álgebra de conjuntos espaciais

As três aulas anteriores construíram a base — sistema de referência, estrutura de dados, aquisição — para que o dado esteja correto e bem organizado. A partir desta aula, o módulo entra na parte analítica: o **geoprocessamento vetorial** é o conjunto de operações que combinam duas ou mais camadas vetoriais, ou transformam uma única camada, para gerar informação nova — informação que não estava explícita em nenhuma camada isolada, mas emerge do cruzamento entre elas. A analogia mais útil é a de uma álgebra de conjuntos aplicada a formas geométricas: assim como a teoria de conjuntos define interseção, união e diferença entre conjuntos abstratos, o geoprocessamento vetorial define operações geometricamente análogas entre polígonos, linhas e pontos, preservando (e recombinando) os atributos de cada camada de origem.

Essas operações são o instrumento que permite, por exemplo, responder "quais unidades litológicas estão a menos de 200 m de uma falha mapeada?", ou "qual é a área total de rocha hospedeira dentro de um polígono de concessão mineral?" — perguntas que nenhuma camada isolada responde, mas que a combinação correta de operações resolve de forma direta e reprodutível.

### Sobreposição (overlay): interseção, união e diferença

As operações de **sobreposição** (*overlay*) combinam duas camadas de polígonos (ou uma camada de polígono com uma de linha ou ponto) gerando uma nova camada cuja geometria resulta de uma operação booleana entre as geometrias de entrada, e cuja tabela de atributos combina os campos de ambas as camadas de origem para cada feição resultante.

- **Interseção (Intersect)**: retorna apenas a área (ou porção de linha/ponto) onde as duas camadas de entrada se sobrepõem espacialmente — o equivalente geométrico da interseção de conjuntos. É a operação padrão para responder "o que existe dentro de quê" — por exemplo, cruzar um polígono de unidade litológica com um polígono de área de concessão mineral para obter exatamente a porção daquela litologia que está dentro da concessão, com os atributos de ambas as camadas preservados na feição resultante.
- **União (Union)**: combina as geometrias das duas camadas de entrada, preservando todas as áreas de ambas (sobrepostas ou não), e mantendo, para cada porção resultante, os atributos de qualquer camada que a cubra (com valores nulos onde uma das camadas não tem cobertura). É usada quando se precisa manter a extensão total de ambas as camadas, não apenas a área comum.
- **Diferença (Erase/Difference)**: retorna a porção de uma camada que **não** está coberta pela outra — o equivalente geométrico da diferença de conjuntos (A menos B). É a operação natural para responder "que área da minha zona de estudo ainda não foi mapeada em detalhe", subtraindo o polígono do mapeamento existente da área total de interesse.

```
Sobreposição: interseção, união e diferença (esquemático)

  Camada A (círculo)     Camada B (quadrado)

     ╱‾‾╲                 ┌────┐
    │    │       +        │    │
     ╲__╱                 └────┘

  Interseção (A ∩ B)     União (A ∪ B)        Diferença (A − B)
     apenas a             toda a área          A sem a parte
     área comum           de A e de B          comum com B
       ░░
      ░░░░                (contorno            ╱‾‾╲░░
       ░░                  combinado)         │    ░ (parte
                                                ╲__╱  fora de B)
```
A legenda a reter: as três operações partem das mesmas duas camadas de entrada, mas a geometria de saída — e, consequentemente, a área calculável a partir dela — muda de forma fundamental conforme a operação escolhida.

### Buffer: a zona de influência

O **buffer** (zona de influência, ou área de amortecimento) gera um novo polígono que representa todas as posições localizadas a uma distância especificada de uma feição de entrada — um ponto, uma linha ou outro polígono. Um buffer de 500 m em torno de um poço de monitoramento gera um círculo de raio 500 m centrado nele; um buffer de 200 m em torno de uma linha de falha gera uma faixa de 200 m de largura acompanhando todo o traço da falha. Buffers de múltiplas feições da mesma camada podem ser gerados individualmente (um por feição) ou dissolvidos numa única geometria (a união de todos os buffers individuais), conforme o objetivo da análise — dissolvido, quando o interesse é a área total de influência combinada; individual, quando é preciso manter a identidade de qual feição gerou qual buffer.

O buffer é a operação central para responder perguntas de proximidade e de área de risco ou de influência: distância de segurança em torno de uma falha ativa, raio de captura de um poço de bombeamento (retomando um conceito já visto no Módulo 01 de hidrogeologia, agora com uma ferramenta de SIG para representá-lo espacialmente), ou zona de exclusão em torno de uma área ambientalmente sensível. Combinado com uma operação de interseção — por exemplo, cruzar o buffer de uma falha com um polígono de uso do solo — o buffer permite responder perguntas compostas do tipo "que área urbana está dentro da zona de risco de uma falha ativa".

### Dissolve: agregando polígonos por atributo comum

A operação **dissolve** remove as fronteiras internas entre polígonos adjacentes que compartilham o mesmo valor num atributo escolhido, fundindo-os numa única feição maior. Por exemplo, um mapa geológico digitalizado polígono a polígono (um polígono por afloramento cartografado individualmente) pode ter dezenas de polígonos separados pertencentes à mesma unidade litoestratigráfica — o dissolve por esse atributo de unidade produz um único polígono (ou um conjunto de polígonos, se a unidade não for espacialmente contígua) representando toda a extensão daquela unidade no mapa, sem as costuras internas do levantamento original.

O dissolve tem duas utilidades práticas centrais: simplificar a visualização de um mapa (um mapa geológico regional geralmente mostra unidades dissolvidas, não os polígonos de mapeamento de detalhe que as compõem) e viabilizar cálculos de área agregada por classe — a área total de uma formação geológica numa bacia, por exemplo, é calculada de forma direta e correta somando as áreas do(s) polígono(s) dissolvido(s), evitando o erro de contar a mesma unidade várias vezes ao somar polígonos individuais que, entre si, podem ter sido mapeados com pequenas sobreposições ou lacunas nas bordas.

### Relações topológicas e consultas espaciais

Além das operações que geram novas geometrias, um SIG permite formular **consultas espaciais** baseadas em relações topológicas entre camadas, sem necessariamente gerar uma nova camada persistente — por exemplo, "selecione todos os pontos de amostragem que estão *dentro* deste polígono", "selecione todas as linhas de falha que *cruzam* este polígono de unidade litológica", ou "selecione todos os polígonos que *tocam* a borda deste outro polígono". Essas relações (contém, está dentro, cruza, toca, sobrepõe, é disjunto de, está a uma distância de) formam o vocabulário das **relações topológicas** entre geometrias, formalizado no modelo **DE-9IM** (*Dimensionally Extended 9-Intersection Model*, de Clementini e Egenhofer), que a especificação OGC *Simple Features* adota e praticamente todo SIG e banco de dados espacial implementa — daí os nomes de operador serem os mesmos em softwares diferentes. Vale não confundir esse vocabulário com o termo vizinho **álgebra de mapas**: no sentido de Tomlin, álgebra de mapas é o formalismo de operações célula a célula sobre **rasters**, e reaparece no módulo na Aula 06, não aqui. A maioria dos SIGs oferece uma ferramenta de seleção por localização que aplica essas relações diretamente, sem exigir que o usuário calcule a operação de sobreposição completa quando o objetivo é apenas selecionar feições, não gerar uma geometria nova.

A diferença prática entre uma operação de sobreposição (que cria uma nova camada com geometria recombinada) e uma consulta espacial (que apenas seleciona feições existentes com base numa relação) é importante para a eficiência do projeto: gerar uma camada de interseção completa quando o objetivo real é apenas "quantos poços existem dentro desta bacia" é um passo a mais e desnecessário — uma seleção por localização responde a mesma pergunta de forma mais direta e sem criar um produto intermediário a mais para gerenciar (retomando a disciplina de organização de base de dados discutida na Aula 02).

## Exemplo trabalhado

**Situação:** um projeto de avaliação de risco geológico tem duas camadas vetoriais: (1) uma linha representando o traço de uma falha ativa conhecida, com 12 km de extensão; e (2) um polígono de uso do solo classificado como "área urbana consolidada", com área de 8,4 km². A norma técnica do projeto define uma zona de segurança de 300 m a cada lado da falha. Calcule a área de sobreposição entre a zona de segurança da falha e a área urbana, usando as operações de geoprocessamento vetorial apresentadas nesta aula.

**Resolução:**

*Passo 1 — Buffer.* Gera-se um buffer de 300 m em torno da linha de falha. Como o buffer é bilateral por padrão (300 m para cada lado da linha, salvo configuração explícita em contrário), a zona de segurança resultante tem, ao longo de um trecho reto da falha, largura total de 600 m (300 m + 300 m). A área desse buffer, para um trecho aproximadamente retilíneo de comprimento L, se aproxima geometricamente por:

Área do buffer ≈ comprimento da linha × largura total + área das extremidades arredondadas

Para uma estimativa de ordem de grandeza (ignorando o pequeno acréscimo das extremidades arredondadas, que o software calcula automaticamente com precisão): Área ≈ 12.000 m × 600 m = 7.200.000 m² = 7,2 km². Esse valor é a área aproximada da zona de segurança gerada pelo buffer — o SIG calcula o valor exato, geometricamente correto, incluindo as extremidades; a estimativa manual serve para conferir se o resultado do software está na ordem de grandeza certa (uma checagem de sanidade importante em qualquer geoprocessamento, para pegar erros grosseiros de unidade ou de parâmetro).

*Passo 2 — Interseção.* Cruza-se o polígono do buffer da falha (resultado do Passo 1) com o polígono de área urbana consolidada, usando a operação de **interseção**. A camada resultante contém apenas a porção geométrica onde as duas camadas de entrada se sobrepõem — ou seja, a área urbana que está, de fato, dentro da zona de segurança de 300 m da falha.

*Passo 3 — Cálculo de área.* A área da camada resultante da interseção (calculada diretamente pelo SIG a partir da geometria da nova feição, usando as ferramentas de cálculo de geometria em coordenadas projetadas — nunca em coordenadas geográficas não projetadas, que distorceriam o cálculo de área, retomando o cuidado com projeção da Aula 01) é o número que efetivamente importa para o relatório de risco: **não** os 7,2 km² do buffer inteiro (que inclui área não urbana), **nem** os 8,4 km² da área urbana inteira (que inclui área fora da zona de segurança), mas especificamente a porção onde as duas condições coexistem — área urbana **e** dentro da zona de segurança. Suponha que o SIG retorne, para esse cruzamento específico, uma área de interseção de 1,35 km²: esse é o valor a reportar como "área urbana consolidada exposta à zona de segurança da falha ativa", e é exatamente o tipo de número que só a operação correta de sobreposição (buffer seguido de interseção, não apenas um dos dois isoladamente) é capaz de produzir de forma defensável.

## Erros comuns

- **Gerar uma camada de interseção completa quando o objetivo é só contar ou selecionar feições.** Se a pergunta é "quantos poços existem dentro desta bacia", uma seleção por localização responde direto — criar uma nova camada de geometria recombinada é um passo a mais, um produto intermediário a mais para gerenciar, sem necessidade.
- **Calcular área em coordenadas geográficas (graus) em vez de projetadas.** É o erro que o próprio exemplo trabalhado evita explicitamente: um grau de longitude não tem comprimento constante no terreno, e calcular área direto em graus produz um número sem significado físico direto.
- **Confundir união (mantém toda a extensão de ambas) com interseção (só a área comum).** As duas partem das mesmas camadas de entrada, mas a diferença de área resultante pode ser de ordens de grandeza — usar a errada muda o número final sem gerar qualquer erro visível no software.
- **Somar áreas de polígonos individuais de mapeamento em vez de dissolver primeiro.** Se polígonos vizinhos da mesma unidade têm pequenas sobreposições ou lacunas na borda (comum em digitalização manual), somar sem dissolver conta a mesma área mais de uma vez ou deixa buracos.

## O que não concluir

- **Que buffer é sempre bilateral e sempre representa risco ou perigo.** É bilateral por padrão em torno de uma linha, mas o conceito serve para qualquer zona de influência — inclusive proteção ou benefício (raio de captura de um poço de bombeamento), não só risco.
- **Que "álgebra de mapas" e "operações vetoriais de sobreposição" são o mesmo vocabulário.** São dois formalismos distintos por design — álgebra de mapas é célula a célula sobre raster (Tomlin, retomado na Aula 06); overlay vetorial opera sobre geometrias discretas. Usar os termos como sinônimos confunde a escolha de ferramenta.
- **Que a operação de sobreposição certa é sempre uma única etapa.** O exemplo trabalhado precisa de duas operações encadeadas (buffer, depois interseção) para responder à pergunta real — perguntas analíticas compostas raramente se resolvem com uma operação isolada.

## Recap relâmpago

- O geoprocessamento vetorial combina camadas por operações análogas a uma álgebra de conjuntos aplicada a geometrias, gerando informação nova a partir do cruzamento entre camadas.
- Sobreposição (overlay) inclui interseção (só a área comum), união (toda a área de ambas) e diferença (uma camada menos a área coberta pela outra) — a escolha da operação muda fundamentalmente a geometria e a área resultante.
- Buffer gera a zona de influência a uma distância especificada de um ponto, linha ou polígono; pode ser individual (por feição) ou dissolvido (união de todos os buffers).
- Dissolve funde polígonos adjacentes que compartilham um atributo comum, simplificando visualização e viabilizando cálculo correto de área agregada por classe, sem dupla contagem.
- Consultas espaciais por relação topológica (dentro, cruza, toca, a uma distância de) selecionam feições existentes sem gerar uma nova camada — mais eficientes que uma sobreposição completa quando o objetivo é só seleção; esse vocabulário é formalizado pelo modelo DE-9IM da especificação OGC Simple Features, e não se confunde com a álgebra de mapas de Tomlin, que é raster (Aula 06).
- Perguntas analíticas complexas (como área urbana dentro da zona de segurança de uma falha) exigem encadear operações — aqui, buffer seguido de interseção — e o cálculo de área deve sempre ser feito em coordenadas projetadas, nunca em coordenadas geográficas.

## Próxima aula

[[13-geoprocessamento-aula-05-interpolacao-espacial-e-mapas-de-isovalores|Aula 05 — Interpolação espacial e mapas de isovalores a partir de nuvens de pontos]]

## Fontes

- Longley, P. A., Goodchild, M. F., Maguire, D. J. & Rhind, D. W. (2015), *Geographic Information Science and Systems*, 4ª ed., Wiley, cap. 13 — *Spatial Data Analysis* (consultas, medidas, buffer e overlay vetoriais).
- OGC (Open Geospatial Consortium), *Simple Feature Access* (ISO 19125), modelo DE-9IM de relações topológicas entre geometrias — Clementini, E. & Di Felice, P. (1995) e Egenhofer, M. & Herring, J. (1991), formulação original do modelo de nove interseções.
- Tomlin, C. D. (1990), *Geographic Information Systems and Cartographic Modeling*, Prentice Hall (fundamentos de álgebra de mapas — formalismo raster, retomado na Aula 06, não aplicável ao vocabulário vetorial desta aula).
- ESRI, *ArcGIS Pro Documentation* — An overview of the Analysis toolbox (Buffer, Intersect, Union, Erase, Dissolve), documentação técnica de referência consistente com a literatura acadêmica citada.

<!--
nivel: avancado
palavras_corpo: 2050  # recontado apos auditoria + revisao didatica (2026-09-08)
mapa_objetivo_secao:
  geologia-avancado-m13-oa03: "Geoprocessamento vetorial como álgebra de conjuntos espaciais" + "Sobreposição (overlay): interseção, união e diferença" + "Buffer: a zona de influência" + "Dissolve: agregando polígonos por atributo comum" + "Relações topológicas e consultas espaciais" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOPROC-M13-A04-OVERLAY-001
    claim: "As operações de sobreposição (overlay) vetorial incluem interseção (retorna apenas a área de sobreposição entre duas camadas, com atributos combinados), união (preserva toda a área de ambas as camadas, sobreposta ou não) e diferença/erase (retorna a porção de uma camada não coberta pela outra) — análogas às operações de interseção, união e diferença da teoria de conjuntos aplicadas a geometrias."
    risk: fato
    source: "Longley et al. 2015, Geographic Information Science and Systems, cap. 13 (Spatial Data Analysis)"
  - claim_id: GEOPROC-M13-A04-BUFFER-002
    claim: "Um buffer gera um polígono representando todas as posições a uma distância especificada de uma feição de entrada (ponto, linha ou polígono); buffers de múltiplas feições podem ser mantidos individuais ou dissolvidos numa única geometria (união de todos os buffers)."
    risk: fato
    source: "Longley et al. 2015, cap. 13; ESRI ArcGIS Pro Documentation — Buffer"
  - claim_id: GEOPROC-M13-A04-DISSOLVE-003
    claim: "A operação dissolve remove fronteiras internas entre polígonos adjacentes que compartilham o mesmo valor num atributo escolhido, fundindo-os numa única feição; é usada para simplificar visualização e para calcular área agregada por classe sem dupla contagem de polígonos sobrepostos ou fragmentados na origem."
    risk: fato
    source: "Longley et al. 2015, cap. 13; ESRI ArcGIS Pro Documentation — Dissolve"
  - claim_id: GEOPROC-M13-A04-TOPOLOGIA-004
    claim: "Consultas espaciais baseadas em relações topológicas (contém, está dentro, cruza, toca, é adjacente a, está a uma distância de) permitem selecionar feições existentes com base em sua relação espacial com outra camada, sem necessariamente gerar uma nova camada de geometria recombinada como nas operações de overlay."
    risk: fato
    source: "Longley et al. 2015, Geographic Information Science and Systems, cap. 13 (seleção por localização / spatial query); OGC Simple Feature Access (ISO 19125), modelo DE-9IM"
  - claim_id: GEOPROC-M13-A04-CALCULO-AREA-005
    claim: "O cálculo de área de feições vetoriais deve ser realizado em um sistema de coordenadas projetado (planas, em metros), não em coordenadas geográficas (graus de latitude/longitude), porque o cálculo direto de área em graus não corresponde a área real no terreno e produz resultado incorreto ou de interpretação ambígua."
    risk: fato
    source: "Snyder 1987, Map Projections, cap. 1 (propriedades de área de projeções); Longley et al. 2015, cap. 4 e 13, consistente com a prática padrão de SIG"
-->
