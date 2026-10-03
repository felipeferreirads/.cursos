# Aula 02: Cartas básicas: materiais inconsolidados, substrato rochoso, declividade e feições do terreno

**ID:** geologia-avancado-m07-a02
**Módulo:** [[07-mapeamento-geotecnico-modulo|Módulo 07 — Metodologia de mapeamento geotécnico]]
**Duração estimada:** ~29 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** elaborar as cartas básicas de um programa de cartografia geotécnica — materiais inconsolidados, substrato rochoso, declividade e feições do terreno —, escolhendo as classes de cada uma segundo critérios técnicos e legais, e avaliando como a resolução do modelo digital de elevação afeta o resultado.

**Pré-requisito:** Aula 01 deste módulo (escalas, atributos, unidades de mapeamento); classificação de solos e prospecção do Módulo 06 (Aulas 01 e 06).

## Antes de começar, você precisa saber

- Que a escala escolhida (Aula 01) fixa a menor área representável e, portanto, o nível de detalhe possível em todas as cartas básicas.
- Que os dados de subsuperfície são pontuais e escassos, enquanto relevo e feições superficiais têm cobertura contínua (Aula 01).
- Classificação SUCS e o significado de NSPT (Módulo 06, Aulas 01 e 06).

## Conteúdo

### Básicas e derivadas: a arquitetura do produto

A cartografia geotécnica organiza-se em duas camadas. As **cartas básicas** (também chamadas de documentos básicos) registram **um atributo por carta**, o mais próximo possível do dado observado, com o mínimo de interpretação. As **cartas derivadas e interpretativas** (Aula 03) combinam as básicas segundo um modelo de comportamento para responder a uma pergunta de uso.

A separação é deliberada e tem uma razão de auditoria: se a aptidão de uma área for questionada, é preciso poder voltar às camadas de origem e verificar qual atributo determinou a classificação. Uma carta interpretativa produzida sem cartas básicas rastreáveis não pode ser revista — só refeita.

### Carta de materiais inconsolidados

Registra a distribuição dos materiais que recobrem o substrato rochoso, classificados primariamente por **origem**, porque a origem controla as propriedades geotécnicas de forma mais confiável que a composição isolada:

- **Solos residuais:** formados in situ por alteração da rocha subjacente. Conservam estrutura reliquiar da rocha-mãe (foliação, veios, fraturas herdadas), que constitui plano de fraqueza mecânica e caminho preferencial de fluxo — motivo pelo qual um solo residual pode ser muito mais anisotrópico que sua granulometria sugere.
- **Solos transportados:** coluvionares (movimentados por gravidade encosta abaixo), aluvionares (fluviais), eluvionares, eólicos, marinhos.
- **Aterros:** antrópicos, classificados ainda em compactados (com controle) e lançados (sem controle) — a distinção mais importante da classe, e frequentemente a informação mais difícil de obter em área urbana consolidada.

Além do tipo genético, a carta registra a **espessura** (por isópacas, quando há sondagens suficientes) e atributos de comportamento: classificação SUCS, plasticidade, erodibilidade, e, em solos tropicais, **colapsividade** (solos porosos que perdem estrutura ao serem umedecidos sob carga) e **expansividade**.

> [!important] Colúvio é a classe que mais frequentemente decide a carta
> Depósitos coluvionares em encosta são, por definição, material que já se moveu. Costumam ser heterogêneos, pouco densos, com contato basal abrupto sobre solo residual ou rocha — um plano preferencial de escorregamento — e sensíveis à elevação da poropressão (Módulo 06, Aula 03). Numa carta de suscetibilidade a escorregamento, a delimitação do colúvio é tipicamente o atributo de maior peso, e também um dos mais difíceis de mapear, porque no topo do perfil ele pode ser indistinguível do solo residual sem observação de campo em corte exposto.

### Carta de substrato rochoso

Registra a litologia, o **grau de alteração** e de consistência, e a **profundidade do topo rochoso**. O grau de alteração é classificado em escala padronizada — de rocha sã (W1) a solo residual (W5/W6), conforme a escala da ISRM adotada também no Módulo 05 —, e é geotecnicamente mais determinante que a litologia: um gnaisse W4 comporta-se como solo, não como rocha, independentemente de sua composição mineralógica.

A profundidade do topo rochoso é o dado que mais depende de subsuperfície, e portanto o de maior incerteza espacial. Onde as sondagens são escassas, é comum e legítimo complementá-la com sísmica de refração ou eletrorresistividade (Módulo 06, Aula 06), desde que a carta declare quais trechos são interpolados entre furos e quais vêm de método indireto calibrado.

Quando o objetivo da carta envolve escavação, estabilidade de talude rochoso ou fundação em rocha, registram-se também as **famílias de descontinuidades** e, se houver testemunho, o RQD e as classificações do Módulo 05.

### Carta clinográfica (de declividade)

A declividade é o atributo de relevo mais usado em geotecnia, e a carta que o representa é obtida hoje quase sempre por processamento de **modelo digital de elevação (MDE)**. O ponto metodológico central não é como calculá-la — é **como escolher as classes**.

As classes não devem ser divisões aritméticas arbitrárias (0–10%, 10–20%...), e sim **limiares com significado técnico ou legal**. A proposta de **De Biasi (1992)**, largamente adotada no Brasil, usa cinco classes ancoradas em limiares reais:

| Classe | Significado do limiar |
|---|---|
| < 5% | Limite para urbanização sem restrição relevante de declividade; abaixo disso o problema típico passa a ser drenagem e inundação, não estabilidade |
| 5 – 12% | Limite prático para ocupação urbana convencional e para mecanização agrícola |
| 12 – 30% | Ocupação possível com movimentação de terra e projeto específico de drenagem e contenção |
| 30 – 47% | A partir de 30% incide a restrição da **Lei 6.766/1979** (art. 3º, parágrafo único, III), que não permite parcelamento do solo em terrenos com declividade igual ou superior a 30%, salvo atendidas exigências específicas das autoridades competentes |
| > 47% | 47% equivale a 25°, limiar historicamente adotado na legislação florestal para restrição de corte raso; acima de **45° (100%)** a encosta é Área de Preservação Permanente pelo Código Florestal vigente (Lei 12.651/2012, art. 4º, V) |

> [!warning] A declividade calculada depende da resolução do MDE
> Um MDE mais grosseiro **suaviza** o relevo: as células maiores promediam a elevação numa área maior, achatando as vertentes íngremes e preenchendo as feições estreitas. O efeito prático é uma **subestimação sistemática das declividades altas** — exatamente a faixa que decide a classificação legal e a suscetibilidade. Uma carta clinográfica derivada de MDE de 30 m (SRTM) pode não classificar como "acima de 30%" uma encosta que um MDE de 12,5 m ou um levantamento LiDAR classificaria. A resolução do MDE de origem é informação obrigatória do memorial, e a escala da carta clinográfica não pode ser maior do que a resolução do MDE sustenta.

Outras cartas de relevo frequentemente produzidas na mesma etapa: **hipsométrica** (classes de altitude), **de amplitude local**, **de forma de vertente** (convexa, retilínea, côncava — a côncava concentra fluxo e é preferencialmente instável) e **de densidade de drenagem**.

### Carta de feições e processos do terreno

Registra o que **já aconteceu e está acontecendo** no terreno — e é a carta básica de maior valor preditivo, porque um processo instalado é a evidência mais direta de que as condições para ele existem naquele lugar:

- **Cicatrizes de escorregamento** (rasos translacionais, rotacionais, corridas de detritos), ativas ou vegetadas.
- **Erosão** em sequência de intensidade: laminar, sulcos, ravinas, **voçorocas** (quando a incisão atinge o nível freático, o processo muda de natureza e passa a ser alimentado também por fluxo subsuperficial, tornando-se muito mais difícil de estabilizar).
- **Feições de inundação e de assoreamento**, planícies e terraços, marcas de cheia.
- **Subsidência e colapso**, dolinas em terreno cárstico, cavidades de mineração antiga.
- **Feições antrópicas** que alteram o comportamento: cortes, aterros, taludes de estrada, barramentos, lançamento de água servida em encosta.

As fontes são a interpretação de imagens e fotografias aéreas — hoje complementadas por séries temporais, que permitem datar a instalação de um processo — mais a checagem de campo, insubstituível para distinguir cicatriz de escorregamento antiga de feição erosiva ou de corte antrópico vegetado.

### As fontes de dados de relevo

| Fonte | Resolução típica | Uso adequado |
|---|---|---|
| SRTM | ~30 m | Escala regional, reconhecimento |
| ALOS PALSAR (RTC) | ~12,5 m | Semidetalhe, plano diretor |
| Fotogrametria aérea / VANT | 0,1 – 2 m | Detalhe e grande detalhe |
| LiDAR aerotransportado | sub-métrica | Grande detalhe; único que penetra o dossel vegetal e revela o **terreno** sob a mata, decisivo em encosta florestada |

## Exemplo trabalhado

**Situação:** numa encosta a ser mapeada em 1:10.000, dispõe-se de: MDE SRTM de 30 m, imagens de satélite de alta resolução, oito sondagens SPT dispersas e um dia de campo. Um trecho da encosta tem declividade calculada de 28% pelo SRTM. Avalie o que se pode e o que não se pode concluir, e proponha a sequência de trabalho.

**Resolução:**

**Passo 1 — Reconhecer a incompatibilidade de resolução.** Para escala 1:10.000, um MDE de 30 m é insuficiente: cada célula do MDE corresponde a 3 mm na carta, e a suavização do SRTM subestima sistematicamente as declividades altas. O valor de 28% é, portanto, uma **estimativa por baixo**.

**Passo 2 — Reconhecer a consequência jurídica da incerteza.** 28% está imediatamente abaixo do limiar de 30% da Lei 6.766/1979. Como a subestimação do SRTM é sistemática e pode facilmente exceder os 2 pontos percentuais de folga, **não é possível afirmar, com esse dado, que o trecho está abaixo do limiar legal.** Classificá-lo como "abaixo de 30%" seria uma conclusão que o dado não sustenta, com consequência direta sobre a permissão de parcelamento.

**Passo 3 — Obter relevo compatível com a escala.** Levantamento por VANT (fotogrametria) sobre a encosta, gerando MDE submétrico, ou LiDAR se houver cobertura vegetal densa — sem isso, a carta clinográfica não pode ser emitida em 1:10.000. Recalcular a declividade e verificar a classificação com dado adequado.

**Passo 4 — Ordenar as demais cartas básicas pelo que o dia de campo pode agregar.** As imagens e o MDE novo resolvem relevo e feições superficiais em gabinete. O dia de campo deve ser gasto no que **só o campo resolve**: percorrer cortes expostos para distinguir colúvio de solo residual e medir a espessura do manto, checar cicatrizes de escorregamento identificadas em imagem (confirmando se são cicatrizes ou feições antrópicas vegetadas) e verificar surgências d'água.

**Passo 5 — Declarar a incerteza da subsuperfície.** Oito sondagens numa encosta são pouco para isópacas confiáveis em 1:10.000. A carta de materiais inconsolidados deve trazer limites tracejados, e o memorial deve registrar a densidade e a distribuição dos furos — inclusive apontando os setores onde a espessura foi extrapolada, e não interpolada.

**Interpretação:** o caso ilustra o erro mais consequente desta aula, que é silencioso: o dado de relevo tem aparência de precisão (um número com duas casas, calculado por software) e carrega uma incerteza sistemática, não aleatória — o SRTM não erra para mais e para menos com igual probabilidade em encosta íngreme, ele **erra sempre para menos**. Tratar 28% como um valor confiável apenas porque saiu do processamento é confundir precisão numérica com acurácia.

## Erros comuns

- **Usar MDE de resolução incompatível com a escala da carta**, e reportar declividades como se fossem medidas e não estimadas.
- **Adotar classes de declividade aritméticas** (0–10%, 10–20%) em vez de limiares com significado técnico e legal, produzindo uma carta que não conversa com a decisão que precisa sustentar.
- **Classificar materiais inconsolidados apenas por granulometria**, ignorando a origem — e assim perdendo a distinção entre colúvio e solo residual, que é a mais relevante para estabilidade de encosta.
- **Tratar litologia como se fosse comportamento**, ignorando o grau de alteração: um gnaisse W4 comporta-se como solo.
- **Confundir cicatriz de escorregamento com feição erosiva ou corte antrópico** na interpretação de imagem, sem checagem de campo.
- **Interpolar topo rochoso entre furos distantes com linha cheia**, sem distinguir setores interpolados de extrapolados.

## O que não concluir

- **Que declividade alta implica instabilidade e declividade baixa implica segurança.** A declividade é um fator entre vários: uma encosta íngreme em rocha sã pode ser estável, e uma vertente suave com colúvio espesso sobre contato basal desfavorável e nível d'água raso pode não ser. A carta clinográfica é insumo, não conclusão — o cruzamento vem na Aula 03.
- **Que ausência de cicatriz de escorregamento indica ausência de suscetibilidade.** A ausência pode significar que o processo ainda não foi deflagrado, que a cicatriz foi apagada por ocupação ou vegetação, ou que o período de imagens disponível não cobre o último evento extremo.
- **Que LiDAR resolve todos os problemas de relevo.** Ele resolve o relevo com excelência, inclusive sob vegetação — mas não diz nada sobre espessura de manto, topo rochoso, nível d'água ou parâmetros geotécnicos, que continuam vindo de subsuperfície.

## Recap relâmpago

- Cartas **básicas** registram um atributo cada, próximas do dado observado; cartas **derivadas** (Aula 03) as combinam. A separação existe para que a interpretação seja rastreável e revisável.
- **Materiais inconsolidados** classificam-se primariamente por **origem** (residual, coluvionar, aluvionar, aterro compactado ou lançado), mais espessura e atributos de comportamento; o **colúvio** é tipicamente o atributo decisivo em suscetibilidade a escorregamento.
- No **substrato rochoso**, o **grau de alteração** (escala W1–W6 da ISRM) é geotecnicamente mais determinante que a litologia; a profundidade do topo rochoso é o dado de maior incerteza espacial.
- As classes da **carta clinográfica** devem seguir limiares técnicos e legais (proposta de De Biasi: <5%, 5–12%, 12–30%, 30–47%, >47%), com destaque para os 30% da Lei 6.766/1979 e os 45° (100%) do Código Florestal vigente.
- A resolução do **MDE** subestima sistematicamente as declividades altas — precisão numérica não é acurácia, e a resolução de origem é informação obrigatória do memorial.
- A **carta de feições e processos** tem o maior valor preditivo, porque processo instalado é evidência direta de que as condições existem ali; exige checagem de campo para distinguir cicatriz de feição erosiva ou de corte antrópico.

## Próxima aula

[[07-mapeamento-geotecnico-aula-03-cartas-derivadas-aptidao-suscetibilidade-risco|Aula 03 — Cartas derivadas e interpretativas: aptidão física ao assentamento urbano, suscetibilidade e risco]]

## Anterior

[[07-mapeamento-geotecnico-aula-01-conceitos-metodologia-escalas-atributos|Aula 01 — Conceitos e metodologia da cartografia geotécnica]]

## Fontes

- Cartas básicas, atributos e classificação de materiais inconsolidados: Zuquette, L. V. & Gandolfi, N. (2004), *Cartografia Geotécnica*, Oficina de Textos, São Paulo; IAEG/UNESCO (1976), *Engineering Geological Maps: A Guide to Their Preparation*.
- Classes de declividade e carta clinográfica: De Biasi, M. (1992), "A carta clinográfica: os métodos de representação e sua confecção", *Revista do Departamento de Geografia*, USP, n. 6, p. 45–60.
- Restrição legal ao parcelamento em declividade igual ou superior a 30%: Brasil, Lei nº 6.766, de 19 de dezembro de 1979, art. 3º, parágrafo único, inciso III.
- Encostas com declividade superior a 45° como Área de Preservação Permanente: Brasil, Lei nº 12.651, de 25 de maio de 2012 (Código Florestal), art. 4º, inciso V.
- Escala de graus de alteração de maciços rochosos: ISRM (1981), *Rock Characterization, Testing and Monitoring: ISRM Suggested Methods*, Pergamon (retomando o Módulo 05).
- Feições erosivas e evolução de voçorocas: IPT (1986), *Orientações para o combate à erosão no Estado de São Paulo*, Instituto de Pesquisas Tecnológicas do Estado de São Paulo.

<!--
nivel: avancado
palavras_corpo: ~2100

mapa_objetivo_secao:
  geologia-avancado-m07-oa03: "Básicas e derivadas: a arquitetura do produto" + "Carta de materiais inconsolidados" + "Carta de substrato rochoso" + "Carta clinográfica (de declividade)" + "Carta de feições e processos do terreno" + "As fontes de dados de relevo" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: CARTGEO-M07-A02-BASICAS-001
    claim: "As cartas básicas registram um atributo cada, próximas do dado observado, e as derivadas as combinam segundo um modelo de comportamento; a separação existe para tornar a interpretação rastreável e revisável."
    risk: fato
    source: "Zuquette & Gandolfi 2004; IAEG/UNESCO 1976"
  - claim_id: CARTGEO-M07-A02-MATERIAIS-002
    claim: "Materiais inconsolidados classificam-se primariamente por origem (residual, coluvionar, aluvionar, eólico, marinho, aterro compactado ou lançado); solos residuais conservam estrutura reliquiar da rocha-mãe, e depósitos coluvionares apresentam contato basal que constitui plano preferencial de escorregamento."
    risk: fato
    source: "Zuquette & Gandolfi 2004"
  - claim_id: CARTGEO-M07-A02-ALTERACAO-003
    claim: "O grau de alteração do substrato, em escala padronizada de W1 (rocha sã) a W5/W6 (solo residual) segundo a ISRM, é geotecnicamente mais determinante que a litologia isolada."
    risk: fato
    source: "ISRM 1981; Zuquette & Gandolfi 2004"
  - claim_id: CARTGEO-M07-A02-DEBIASI-004
    claim: "A proposta de classes de declividade de De Biasi (1992), adotada no Brasil, usa os limiares <5%, 5–12%, 12–30%, 30–47% e >47%, ancorados em significados técnicos e legais."
    risk: fato
    source: "De Biasi 1992"
  - claim_id: CARTGEO-M07-A02-LEI6766-005
    claim: "A Lei 6.766/1979, art. 3º, parágrafo único, inciso III, não permite o parcelamento do solo em terrenos com declividade igual ou superior a 30%, salvo atendidas exigências específicas das autoridades competentes."
    risk: fato
    source: "Brasil, Lei nº 6.766/1979, art. 3º"
  - claim_id: CARTGEO-M07-A02-APP-006
    claim: "Pelo Código Florestal vigente (Lei 12.651/2012, art. 4º, inciso V), as encostas ou partes destas com declividade superior a 45°, equivalente a 100% na linha de maior declive, são Área de Preservação Permanente."
    risk: fato
    source: "Brasil, Lei nº 12.651/2012, art. 4º, V"
  - claim_id: CARTGEO-M07-A02-MDE-007
    claim: "MDE de resolução mais grosseira suaviza o relevo e subestima sistematicamente (não aleatoriamente) as declividades altas; a resolução de origem limita a escala máxima da carta clinográfica. Resoluções típicas: SRTM ~30 m, ALOS PALSAR ~12,5 m, fotogrametria por VANT 0,1–2 m, LiDAR sub-métrica, sendo o LiDAR o único que revela o terreno sob dossel vegetal."
    risk: fato
    source: "Zuquette & Gandolfi 2004; documentação técnica dos produtos SRTM, ALOS PALSAR RTC e LiDAR aerotransportado"
  - claim_id: CARTGEO-M07-A02-VOCOROCA-008
    claim: "A sequência de intensidade da erosão hídrica é laminar, sulcos, ravinas e voçorocas, e a voçoroca se distingue por atingir o nível freático, passando a ser alimentada também por fluxo subsuperficial."
    risk: fato
    source: "IPT 1986"
-->
