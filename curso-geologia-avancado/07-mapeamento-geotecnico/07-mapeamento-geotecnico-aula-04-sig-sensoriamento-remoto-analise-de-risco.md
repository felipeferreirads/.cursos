# Aula 04: SIG, imagens de satélite e análise de risco aplicados ao planejamento urbano

**ID:** geologia-avancado-m07-a04
**Módulo:** [[07-mapeamento-geotecnico-modulo|Módulo 07 — Metodologia de mapeamento geotécnico]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** operar a cadeia SIG que produz uma carta derivada (modelos de dados, referencial geodésico, álgebra de mapas e agregação ponderada), selecionar produtos de sensoriamento remoto conforme o processo a detectar, avaliar a propagação de incerteza no resultado, e traduzir a carta em instrumento efetivo de planejamento urbano e de gestão de risco.

**Pré-requisito:** Aulas 01 a 03 deste módulo — em especial a cadeia suscetibilidade → perigo → risco e as três famílias de método da Aula 03.

## Antes de começar, você precisa saber

- A distinção entre suscetibilidade, perigo e risco, e que risco exige exposição e vulnerabilidade (Aula 03).
- Que as cartas básicas registram um atributo cada e as derivadas as combinam (Aula 02).
- Que a resolução do MDE limita a escala da carta e subestima sistematicamente declividades altas (Aula 02).

## Conteúdo

### O SIG como ambiente de análise, não como programa de desenho

Um SIG não é uma prancheta digital. O que ele acrescenta à cartografia geotécnica é a capacidade de **operar sobre os atributos**: cruzar camadas, calcular sobre elas, e produzir uma carta derivada como **resultado de uma operação declarada e reexecutável**, e não como um desenho feito à mão sobre um fundo. Essa reexecutabilidade é o que torna a carta auditável — mudou um peso ou entrou uma sondagem nova, refaz-se a análise e compara-se.

**Dois modelos de dados**, com vocações distintas:

- **Vetorial** (pontos, linhas, polígonos com topologia): adequado a feições de limite definido — lotes, edificações, drenagem, cicatrizes, unidades de mapeamento delimitadas por interpretação. Preserva a geometria exata e comporta atributos ricos por feição.
- **Matricial (raster)**: o espaço é uma malha de células, cada uma com um valor. Adequado a fenômenos contínuos — elevação, declividade, distância, índices — e é o modelo que viabiliza a **álgebra de mapas**: somar, multiplicar e reclassificar camadas célula a célula. Praticamente toda carta de suscetibilidade é produzida em raster, e depois generalizada para vetor na apresentação.

> [!warning] Resolução da célula não é escala da carta
> Reamostrar um raster de 30 m para células de 2 m não cria informação — cria células menores com o mesmo conteúdo. A escala continua sendo a do dado de origem, e a única mudança real é a aparência de detalhe. Este é o mesmo erro da Aula 01 (ampliar carta além de sua escala) na sua versão digital, e é mais fácil de cometer porque o software executa a reamostragem sem qualquer aviso.

### Referencial geodésico e a integração de camadas

Camadas de origens diferentes chegam em sistemas de referência diferentes, e sobrepô-las sem reprojetar produz deslocamentos que podem chegar a dezenas ou centenas de metros — o suficiente para colocar uma edificação no polígono errado de uma carta de risco. No Brasil, o sistema de referência geodésico oficial é o **SIRGAS 2000**, de adoção obrigatória desde 2015, e é para ele que todas as camadas devem ser convertidas antes de qualquer cruzamento. Bases mais antigas em Córrego Alegre ou SAD-69 exigem transformação de datum, não simples mudança de rótulo.

A qualidade posicional dos produtos, no Brasil, é avaliada pelo **Padrão de Exatidão Cartográfica** — instituído pelo Decreto nº 89.817/1984 e estendido aos produtos digitais pela especificação técnica de controle de qualidade de dados geoespaciais (PEC-PCD) —, que classifica os produtos em classes conforme o erro posicional admissível para cada escala. Declarar a classe do produto é parte do memorial (Aula 01).

### Álgebra de mapas e a armadilha da compensação

O método heurístico da Aula 03 se implementa como **sobreposição ponderada**: cada fator é reclassificado numa escala comum (por exemplo, 1 a 5), recebe um peso, e o índice de suscetibilidade da célula é a soma ponderada.

O problema — subestimado com frequência — é que a soma ponderada é **compensatória**: um valor extremo num fator pode ser diluído por valores baixos nos demais, e duas células com situações fisicamente muito diferentes podem receber o mesmo índice. Quando existe um fator **eliminatório** (uma condição que, por si só, define inaptidão — uma cavidade, uma APP, uma cicatriz ativa), ele não deve entrar como parcela de uma soma: deve entrar como **regra de veto**, aplicada depois da agregação. A prática recomendada é combinar as duas lógicas — soma ponderada para os fatores graduais, regras restritivas para os eliminatórios.

### Sensoriamento remoto: escolher o sensor pelo processo

Cada produto detecta bem um tipo de coisa. A escolha se faz pelo processo a mapear, não pela disponibilidade:

| Produto | O que resolve bem | Uso típico em geotecnia urbana |
|---|---|---|
| Óptico de média resolução (Landsat ~30 m, Sentinel-2 ~10 m, CBERS) | Cobertura sistemática e gratuita, séries longas | Mudança de uso e cobertura, expansão urbana, cicatrizes grandes |
| Óptico de alta resolução (submétrico, comercial ou VANT) | Detalhe de feições e edificações | Inventário de cicatrizes, cadastro de ocupação, setorização |
| **SAR interferométrico (InSAR)** | Deslocamento de superfície em escala **milimétrica a centimétrica**, independente de nuvem e de iluminação | **Subsidência**, movimentos lentos de encosta, recalque de aterro, deformação em área de mineração |
| LiDAR | Terreno **sob o dossel vegetal** | Relevo e cicatrizes antigas em encosta florestada |

O **InSAR** merece destaque porque acrescenta uma dimensão que a cartografia clássica não tinha: **o tempo**. Técnicas de série temporal (como as baseadas em espalhadores persistentes) medem o deslocamento acumulado de alvos estáveis ao longo de anos, permitindo distinguir um talude que está se movendo lentamente de outro apenas geometricamente desfavorável — informação que transforma suscetibilidade em evidência de atividade. Suas limitações são reais: mede apenas a componente do deslocamento na linha de visada do satélite, perde coerência em áreas de vegetação densa ou de movimento rápido, e exige alvos estáveis, o que funciona bem em área urbana e mal em encosta florestada.

Um segundo uso decisivo do sensoriamento é a **detecção de mudança multitemporal**: comparar séries de imagens para datar a instalação de um processo, verificar se uma cicatriz é recente ou antiga, e — em planejamento urbano — acompanhar o **avanço da ocupação sobre áreas classificadas como inaptas**, que é o principal indicador de que a carta não está sendo efetiva.

### Da carta ao instrumento: onde a análise vira decisão

Uma carta de risco só produz efeito se for incorporada aos instrumentos que regulam o uso do solo. Os canais principais, no Brasil:

- **Plano diretor e lei de uso e ocupação do solo:** a carta de aptidão (Aula 03) fundamenta o zoneamento, o perímetro urbano e os parâmetros construtivos por zona.
- **Licenciamento e aprovação de parcelamento:** a carta indica onde exigir estudo geotécnico específico, e onde a restrição legal já se aplica (declividade ≥ 30%, APP — Aula 02).
- **Defesa civil:** a setorização de risco (Aula 03) alimenta o plano de contingência, a definição de rotas e pontos de apoio, e a priorização de obras.
- **Monitoramento e alerta:** a integração da carta com **limiares pluviométricos** — a chuva acumulada, em dado intervalo, associada historicamente à deflagração de escorregamentos naquela região — permite emitir alerta antes do evento. No Brasil, essa função é exercida pelo **Cemaden** (Centro Nacional de Monitoramento e Alertas de Desastres Naturais), articulado com as defesas civis estaduais e municipais.

> [!important] Reduzir risco tem quatro caminhos, e três não são obras
> Como Risco = Perigo × Exposição × Vulnerabilidade (Aula 03), há mais de uma alavanca. Pode-se reduzir o **perigo** (contenção, drenagem, estabilização), reduzir a **exposição** (remoção, restrição de uso, impedir novas ocupações), reduzir a **vulnerabilidade** (melhoria construtiva, regularização, capacitação, plano de evacuação) ou reduzir a **consequência residual** (alerta antecipado, seguro, plano de contingência). A leitura estritamente geotécnica tende a enxergar apenas a primeira, que é usualmente a mais cara e nem sempre a mais eficaz por unidade de recurso investido.

### Incerteza: o que se propaga até a decisão

Cada camada carrega erro, e a álgebra de mapas os combina. Três fontes distintas, que exigem tratamentos distintos:

- **Posicional:** onde a feição está (avaliada pelo PEC-PCD).
- **Temática:** se a classificação está certa (a célula classificada como colúvio é mesmo colúvio).
- **De modelo:** se a relação assumida entre fatores e processo é válida, e se os pesos são adequados.

A terceira costuma dominar, e é a menos reportada. A prática mínima é a **análise de sensibilidade**: repetir a análise variando os pesos e os limiares de classe, e verificar quanto o resultado muda. Se uma variação plausível de pesos altera substancialmente o polígono de "inapta", a carta precisa declarar isso — e o polígono precisa ser lido como faixa, não como linha.

> [!warning] O mapa produz consequência sobre pessoas
> Uma carta de risco define quem é removido, qual imóvel perde valor, onde a prefeitura investe e quem recebe alerta. Isso impõe três deveres que não são técnicos, mas profissionais: **declarar a incerteza** em vez de escondê-la atrás da aparência de precisão do SIG; **explicitar o critério** para que possa ser contestado por quem é afetado; e **não permitir que o produto circule sem o memorial**, porque uma carta desacompanhada de suas limitações será usada além do que sustenta. A precisão gráfica de um SIG é sempre maior que a acurácia dos dados que o alimentam — e quem lê o mapa não tem como saber disso.

## Exemplo trabalhado

**Situação:** uma carta de suscetibilidade a escorregamentos é montada por sobreposição ponderada de três fatores, reclassificados de 1 (mínima) a 5 (máxima): declividade (peso 0,50), material inconsolidado (peso 0,30) e forma de vertente (peso 0,20). Duas células apresentam:

- **Célula A:** declividade = 5, material = 2, forma = 2
- **Célula B:** declividade = 3, material = 4, forma = 4

Calcule o índice de cada uma e avalie o resultado. Em seguida, considere que a Célula A contém uma cicatriz de escorregamento ativa mapeada em campo, e proponha o tratamento adequado.

**Resolução:**

**Índice da Célula A:**
IA = (0,50 × 5) + (0,30 × 2) + (0,20 × 2) = 2,50 + 0,60 + 0,40 = **3,50**

**Índice da Célula B:**
IB = (0,50 × 3) + (0,30 × 4) + (0,20 × 4) = 1,50 + 1,20 + 0,80 = **3,50**

**Avaliação:** as duas células recebem **exatamente o mesmo índice** e cairão na mesma classe de suscetibilidade, apesar de descreverem situações fisicamente distintas. A Célula A é uma encosta muito íngreme em material e forma favoráveis; a Célula B é uma vertente de declividade moderada em material desfavorável e forma côncava (que concentra fluxo). Um mesmo número, dois problemas diferentes — e, provavelmente, duas medidas de mitigação diferentes.

Essa é a **compensação** inerente à soma ponderada: o valor extremo de declividade da Célula A foi diluído pelos valores baixos dos outros dois fatores. O método não está errado; está sendo lido como se produzisse um diagnóstico, quando produz um **ordenamento**. O índice serve para hierarquizar o território para investigação, não para explicar o mecanismo de cada célula.

**Tratamento da cicatriz ativa:** uma cicatriz ativa não é mais um fator de predisposição — é **evidência direta de que o processo ocorre ali**. Incluí-la como quarta parcela de uma soma ponderada seria um erro conceitual: com peso 0,2, por exemplo, ela poderia ser compensada por valores baixos nos demais fatores e a célula sairia em classe média. O tratamento correto é uma **regra restritiva aplicada após a agregação**: toda célula com cicatriz ativa (e sua zona de influência a montante e a jusante) é reclassificada diretamente para a classe máxima de suscetibilidade, independentemente do índice calculado.

A mesma lógica de veto vale para os fatores eliminatórios de natureza legal — APP por declividade superior a 45° (Aula 02) — e físicos — cavidade, área de subsidência confirmada por InSAR.

**Interpretação:** o exemplo mostra que a escolha do **operador de agregação** é uma decisão metodológica tão consequente quanto a escolha dos pesos, e recebe muito menos atenção. Soma ponderada para fatores graduais e compensáveis, regras restritivas para os eliminatórios — e, na apresentação, sempre acompanhar a carta de suscetibilidade das cartas básicas, para que o leitor possa recuperar **por que** uma célula caiu naquela classe. Uma carta que informa apenas o índice final é irrastreável, exatamente o problema que a separação entre básicas e derivadas (Aula 02) existe para evitar.

## Erros comuns

- **Reamostrar raster para célula menor e tratar o produto como carta de maior escala**, criando aparência de detalhe sem informação nova.
- **Cruzar camadas em sistemas de referência distintos** sem transformação de datum, deslocando feições em dezenas ou centenas de metros.
- **Usar soma ponderada para fatores eliminatórios**, permitindo que uma condição de veto seja compensada por valores baixos em outros fatores.
- **Escolher o sensor pela disponibilidade e não pelo processo** — usar óptico de média resolução para detectar movimento lento de encosta, quando o produto adequado é InSAR.
- **Tratar InSAR como medida de deslocamento total**, ignorando que ele mede apenas a componente na linha de visada do satélite e perde coerência em vegetação densa e movimento rápido.
- **Reportar apenas incerteza posicional**, omitindo a incerteza temática e a de modelo, que costuma dominar.
- **Entregar a carta sem o memorial**, permitindo que circule e seja usada além do que sustenta.

## O que não concluir

- **Que o SIG produz objetividade.** Ele torna a subjetividade **explícita e reexecutável** — os pesos continuam sendo uma escolha do analista. Isso é um ganho real de auditabilidade, não a eliminação do julgamento.
- **Que resolução espacial fina implica boa carta.** Uma carta de células de 1 m alimentada por parâmetros geotécnicos de duas sondagens é precisa e inacurada. Resolução é do dado de relevo; acurácia depende do dado geotécnico, que continua escasso (Aula 01).
- **Que a carta de risco resolve o risco.** A carta é diagnóstico. A redução do risco depende de decisão política, recurso, capacidade institucional e continuidade — e uma carta excelente arquivada não reduziu risco nenhum. O indicador de efetividade não é a qualidade do mapa, é a evolução da ocupação nas áreas que ele classificou como inaptas.
- **Que obra de contenção é sempre a melhor medida.** Das quatro alavancas (perigo, exposição, vulnerabilidade, consequência residual), a obra atua só na primeira e costuma ser a mais cara, exigindo manutenção permanente — que, se não houver, devolve o risco ao patamar anterior com a agravante de uma ocupação agora consolidada.

## Recap relâmpago

- O SIG é ambiente de **análise reexecutável**, não prancheta digital: **vetorial** para feições de limite definido, **raster** para fenômenos contínuos e para a álgebra de mapas. Resolução da célula **não** é escala da carta.
- Toda camada deve ser levada ao referencial oficial (**SIRGAS 2000** no Brasil, obrigatório desde 2015) por transformação de datum antes de qualquer cruzamento; a qualidade posicional segue o **PEC/PEC-PCD**.
- A soma ponderada é **compensatória** — duas células fisicamente distintas podem receber o mesmo índice. Fatores **eliminatórios** (cicatriz ativa, APP, cavidade) entram como **regra de veto** após a agregação, não como parcela da soma.
- Escolha do sensor pelo processo: óptico para uso e cobertura e inventário de cicatrizes, **LiDAR** para terreno sob dossel, e **InSAR** para deslocamento milimétrico — subsidência e movimentos lentos —, com a limitação de medir só a componente na linha de visada.
- A carta vira decisão pelos instrumentos: plano diretor e zoneamento, licenciamento, setorização para defesa civil, e **limiares pluviométricos** para alerta (no Brasil, via **Cemaden**).
- Risco = Perigo × Exposição × Vulnerabilidade abre **quatro alavancas** de redução, e três delas não são obra: reduzir exposição, reduzir vulnerabilidade e reduzir a consequência residual.
- Incerteza tem três fontes — **posicional, temática e de modelo** —, sendo a de modelo a que costuma dominar e a menos reportada; a **análise de sensibilidade** sobre pesos e limiares é a prática mínima, e o memorial é obrigatório porque o mapa produz consequência sobre pessoas.

## Próxima aula

Este é o fim do Módulo 07. Continue em [[08-geotecnia-ambiental/08-geotecnia-ambiental-modulo|Módulo 08 — Geotecnia ambiental]].

## Anterior

[[07-mapeamento-geotecnico-aula-03-cartas-derivadas-aptidao-suscetibilidade-risco|Aula 03 — Cartas derivadas e interpretativas: aptidão, suscetibilidade e risco]]

## Fontes

- Fundamentos de SIG, modelos de dados e álgebra de mapas: Burrough, P. A., McDonnell, R. A. & Lloyd, C. D. (2015), *Principles of Geographical Information Systems*, 3ª ed., Oxford University Press; Tomlin, C. D. (1990), *Geographic Information Systems and Cartographic Modeling*, Prentice Hall.
- Sistema de referência geodésico brasileiro: IBGE, Resolução do Presidente nº 1/2005 e alterações posteriores, que estabelecem o SIRGAS 2000 como sistema de referência geodésico oficial no Brasil, com adoção obrigatória a partir de 2015.
- Padrão de exatidão cartográfica: Brasil, Decreto nº 89.817, de 20 de junho de 1984 (Instruções Reguladoras das Normas Técnicas da Cartografia Nacional); Diretoria de Serviço Geográfico do Exército, *Especificação Técnica para Controle de Qualidade de Dados Geoespaciais (ET-CQDG)*, que estende o PEC aos produtos cartográficos digitais.
- Interferometria SAR aplicada a deslocamento de superfície: Ferretti, A., Prati, C. & Rocca, F. (2001), "Permanent scatterers in SAR interferometry", *IEEE Transactions on Geoscience and Remote Sensing*, 39(1), p. 8–20.
- Suscetibilidade, perigo e risco aplicados ao planejamento: Fell, R. et al. (2008), "Guidelines for landslide susceptibility, hazard and risk zoning for land use planning", *Engineering Geology*, 102(3–4), p. 85–98.
- Limiares pluviométricos para deflagração de escorregamentos: Guzzetti, F., Peruccacci, S., Rossi, M. & Stark, C. P. (2008), "The rainfall intensity–duration control of shallow landslides and debris flows: an update", *Landslides*, 5(1), p. 3–17.
- Monitoramento e alerta no Brasil: Cemaden — Centro Nacional de Monitoramento e Alertas de Desastres Naturais, instituído em 2011, vinculado ao ministério responsável pela pasta de ciência e tecnologia.
- Cartografia geotécnica e planejamento urbano: Zuquette, L. V. & Gandolfi, N. (2004), *Cartografia Geotécnica*, Oficina de Textos, São Paulo.

<!--
nivel: avancado
palavras_corpo: ~2400

mapa_objetivo_secao:
  geologia-avancado-m07-oa04: "O SIG como ambiente de análise, não como programa de desenho" + "Referencial geodésico e a integração de camadas" + "Álgebra de mapas e a armadilha da compensação" + "Sensoriamento remoto: escolher o sensor pelo processo" + "Da carta ao instrumento: onde a análise vira decisão" + "Incerteza: o que se propaga até a decisão" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: CARTGEO-M07-A04-MODELOS-001
    claim: "O modelo vetorial é adequado a feições de limite definido e o matricial a fenômenos contínuos, sendo o raster o que viabiliza a álgebra de mapas célula a célula; reamostrar um raster para célula menor não cria informação nem altera a escala do dado de origem."
    risk: fato
    source: "Burrough, McDonnell & Lloyd 2015; Tomlin 1990"
  - claim_id: CARTGEO-M07-A04-SIRGAS-002
    claim: "O SIRGAS 2000 é o sistema de referência geodésico oficial do Brasil, de adoção obrigatória desde 2015, e camadas em Córrego Alegre ou SAD-69 exigem transformação de datum antes de cruzamento."
    risk: fato
    source: "IBGE, Resolução do Presidente nº 1/2005 e alterações posteriores"
  - claim_id: CARTGEO-M07-A04-PEC-003
    claim: "A qualidade posicional de produtos cartográficos no Brasil é avaliada pelo Padrão de Exatidão Cartográfica, instituído pelo Decreto nº 89.817/1984 e estendido aos produtos digitais (PEC-PCD) pela ET-CQDG da Diretoria de Serviço Geográfico."
    risk: fato
    source: "Brasil, Decreto nº 89.817/1984; DSG, ET-CQDG"
  - claim_id: CARTGEO-M07-A04-COMPENSACAO-004
    claim: "A soma ponderada é compensatória: duas células com combinações de fatores fisicamente distintas podem receber índice idêntico. Fatores eliminatórios devem ser aplicados como regra de veto após a agregação, não como parcela da soma."
    risk: fato
    source: "Burrough, McDonnell & Lloyd 2015; Fell et al. 2008"
  - claim_id: CARTGEO-M07-A04-INSAR-005
    claim: "A interferometria SAR, especialmente por técnicas de espalhadores persistentes, mede deslocamento de superfície em escala milimétrica a centimétrica ao longo do tempo, mas apenas na componente da linha de visada do satélite, perdendo coerência em vegetação densa e em movimento rápido."
    risk: fato
    source: "Ferretti, Prati & Rocca 2001"
  - claim_id: CARTGEO-M07-A04-ALAVANCAS-006
    claim: "Como Risco = Perigo × Exposição × Vulnerabilidade, a redução do risco dispõe de quatro alavancas — reduzir o perigo (obra), a exposição (remoção e restrição de uso), a vulnerabilidade (melhoria construtiva e capacitação) e a consequência residual (alerta e contingência) — das quais apenas a primeira é obra de engenharia."
    risk: fato
    source: "Fell et al. 2008; UNDRR terminology"
  - claim_id: CARTGEO-M07-A04-LIMIARES-007
    claim: "Limiares pluviométricos relacionam intensidade e duração da chuva à deflagração de escorregamentos rasos e corridas de detritos, e são a base de sistemas de alerta antecipado; no Brasil essa função é exercida pelo Cemaden, instituído em 2011."
    risk: fato
    source: "Guzzetti et al. 2008; documentação institucional do Cemaden"
  - claim_id: CARTGEO-M07-A04-INCERTEZA-008
    claim: "A incerteza de uma carta derivada tem três fontes — posicional, temática e de modelo —, sendo a de modelo usualmente dominante e a menos reportada; a análise de sensibilidade sobre pesos e limiares de classe é a prática mínima de tratamento."
    risk: fato
    source: "Burrough, McDonnell & Lloyd 2015; Fell et al. 2008"
-->
