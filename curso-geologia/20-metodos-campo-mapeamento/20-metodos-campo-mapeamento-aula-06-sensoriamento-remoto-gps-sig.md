# Aula 06: Sensoriamento remoto, GPS e SIG no mapeamento geológico

**ID:** geologia-m20-a06
**Módulo:** [[20-metodos-campo-mapeamento-modulo|Módulo 20 — Métodos de campo e mapeamento geológico]]
**Duração estimada:** ~27 min
**Objetivo:** entender como imagens de satélite, GPS e sistemas de informação geográfica (SIG) ampliam e organizam o trabalho de campo tradicional, sem substituí-lo.
**Pré-requisito:** [[20-metodos-campo-mapeamento-aula-05-coluna-estratigrafica|Aula 05 — Levantando e desenhando uma coluna estratigráfica]]

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **Sensoriamento remoto** | Obtenção de informação sobre a superfície da Terra por instrumentos que não tocam o alvo — sensores a bordo de satélites, aviões ou drones. |
| **Espectro eletromagnético** | A gama completa de radiação, da luz visível ao infravermelho e além, cada faixa carregando informação diferente sobre a superfície observada. |
| **Assinatura espectral** | O padrão característico de como um material (rocha, solo, vegetação, mineral) reflete ou absorve diferentes faixas do espectro eletromagnético. |
| **GPS (Sistema de Posicionamento Global)** | Rede de satélites que permite calcular a posição de um receptor na superfície da Terra por triangulação de sinais. |
| **SIG (Sistema de Informação Geográfica)** | Software que armazena, organiza e cruza dados geográficos em camadas sobrepostas (mapas, imagens, tabelas), permitindo análises espaciais. |
| **Modelo digital de elevação (MDE)** | Representação da topografia como uma grade de valores de altitude, usada para gerar mapas de relevo, sombreamento e perfis topográficos automaticamente. |

## Antes de começar, você precisa saber

- Como um mapa geológico organiza contatos e atitudes — [[20-metodos-campo-mapeamento-aula-03-mapa-geologico-regra-dos-v|Aula 03]].
- Como uma coordenada geográfica localiza um ponto de campo — [[20-metodos-campo-mapeamento-aula-01-observacao-registro-amostragem|Aula 01]].

## Ao final você vai conseguir

- [geologia-m20-oa06] Explicar como sensoriamento remoto, GPS e SIG apoiam o planejamento, a execução e a integração do mapeamento geológico de campo.

## Conteúdo

### Campo continua sendo a fonte da verdade

Antes de qualquer ferramenta digital, vale fixar um ponto que evita uma confusão comum: sensoriamento remoto, GPS e SIG **não substituem** o trabalho de campo das aulas anteriores — eles o planejam, ampliam e organizam. Nenhum satélite mede a atitude de uma camada com a precisão de uma bússola apoiada na rocha, nem coleta uma amostra orientada. O que essas ferramentas fazem é permitir que o tempo, limitado, de trabalho em campo seja usado de forma muito mais eficiente — e que os dados coletados a pé sejam integrados e visualizados numa escala que a observação direta, sozinha, nunca alcançaria.

### Sensoriamento remoto: enxergar mais do que o olho vê

**Sensoriamento remoto** é a obtenção de informação sobre a superfície terrestre por sensores que não tocam o alvo — a bordo de satélites, aviões ou, cada vez mais, drones. A ideia central é que diferentes materiais na superfície — rocha exposta, vegetação, solo, água — refletem e absorvem a luz de forma diferente ao longo do **espectro eletromagnético**, que vai muito além do que o olho humano enxerga (a luz visível é apenas uma faixa estreita desse espectro, entre o ultravioleta e o infravermelho). Esse padrão característico de reflexão e absorção, específico de cada material, é chamado de **assinatura espectral** — de forma parecida com uma impressão digital óptica.

Sensores orbitais capturam imagens em várias faixas espectrais simultaneamente (não só a luz visível, mas também infravermelho próximo, infravermelho de ondas curtas, entre outras), e comparar essas faixas permite distinguir tipos de rocha e minerais que, à luz visível comum, pareceriam idênticos. Óxidos de ferro, por exemplo, têm assinatura espectral característica no visível e infravermelho próximo, o que torna viável mapear zonas de alteração hidrotermal associadas a certos tipos de depósito mineral a partir de imagens de satélite, antes mesmo de qualquer visita a campo — um uso direto no planejamento de exploração mineral, assunto do Módulo 21.

Além das imagens espectrais, o **modelo digital de elevação (MDE)** — uma grade de valores de altitude que cobre uma área inteira, hoje obtida por diversas técnicas orbitais e aéreas — permite gerar automaticamente mapas de relevo sombreado, calcular declividade e construir perfis topográficos (o primeiro passo de uma seção geológica, Aula 04) sem que ninguém precise transportar altitudes manualmente de curvas de nível impressas.

### GPS: da coordenada anotada à coordenada instantânea

O **GPS** (Sistema de Posicionamento Global, hoje um entre vários sistemas de navegação por satélite em operação) calcula a posição de um receptor por triangulação de sinais recebidos de múltiplos satélites simultaneamente — o mesmo princípio geométrico da trilateração sísmica vista no Módulo 19, mas usando tempo de chegada de sinal de rádio em vez de ondas sísmicas. Receptores de GPS de uso geral (incluindo os de smartphones) têm precisão tipicamente da ordem de alguns metros; equipamentos de GPS diferencial ou geodésico, usados em levantamentos de maior precisão, chegam à ordem de centímetros, ao custo de equipamento mais caro e tempo de aquisição maior por ponto.

Para o mapeamento geológico, o GPS eliminou boa parte do trabalho manual de localizar um ponto num mapa topográfico impresso por triangulação visual com feições do relevo — hoje, a coordenada de um afloramento é lida diretamente do receptor e registrada na caderneta de campo (Aula 01) em segundos, com uma precisão que a triangulação manual raramente alcançava.

### SIG: onde todos os dados se encontram

Um **SIG** (Sistema de Informação Geográfica) é o software que organiza tudo isso — imagens de satélite, modelo digital de elevação, mapas topográficos, pontos de campo com coordenada GPS, atitudes medidas, amostras coletadas, contatos digitalizados — em **camadas** sobrepostas, todas referenciadas ao mesmo sistema de coordenadas geográficas, de modo que qualquer camada possa ser ligada ou desligada, comparada ou cruzada com qualquer outra.

É essa capacidade de sobreposição que torna o SIG mais do que um simples visualizador de mapas: um geólogo pode, por exemplo, sobrepor a imagem de satélite processada para realçar assinaturas espectrais de alteração hidrotermal, o modelo digital de elevação sombreado (que realça feições estruturais como falhas lineares, muitas vezes visíveis como alinhamentos retos no relevo), e os pontos de campo já coletados com suas atitudes — e, olhando essa combinação, decidir com muito mais informação onde valem a pena os próximos dias de trabalho de campo, em vez de cobrir uma área extensa de forma uniforme e sem prioridade.

### O ciclo real de um projeto de mapeamento moderno

Na prática, projetos de mapeamento atuais seguem um ciclo que alterna entre gabinete e campo, não uma sequência única: **antes** de ir a campo, sensoriamento remoto e imagens disponíveis ajudam a planejar rotas e priorizar áreas de maior interesse; **em campo**, GPS localiza cada ponto com precisão e agilidade, enquanto observação, bússola e amostragem (Aulas 01 e 02) seguem sendo os únicos meios de obter os dados que nenhum sensor remoto capta diretamente; **de volta ao gabinete**, o SIG integra os dados novos de campo às camadas já existentes, atualizando a interpretação e, com frequência, revelando lacunas ou contradições que motivam uma nova saída de campo, num ciclo que se repete até o mapa final.

## Exemplo trabalhado

Uma equipe de mapeamento recebe, antes de ir a campo, uma imagem de satélite multiespectral de uma área remota, processada para realçar zonas com assinatura espectral de óxido de ferro — um indicador possível de alteração hidrotermal. Sobrepondo essa imagem, no SIG, a um modelo digital de elevação sombreado, a equipe nota que a zona de assinatura espectral coincide com um alinhamento retilíneo no relevo, possível expressão de uma falha. Com essa informação, a equipe planeja a rota de campo priorizando essa faixa, em vez de cobrir a área inteira de forma uniforme. Em campo, cada afloramento visitado nessa faixa é localizado por GPS em segundos, descrito e amostrado segundo os métodos das aulas anteriores. De volta ao gabinete, os pontos de campo — agora com litologia, atitude e amostras associadas — são carregados no SIG como uma nova camada, sobrepostos à imagem original: a comparação confirma que a faixa de assinatura espectral corresponde, de fato, a uma zona de alteração associada a uma falha, informação que orienta a etapa seguinte do projeto.

## Recap relâmpago

- Sensoriamento remoto, GPS e SIG ampliam e organizam o trabalho de campo — não o substituem; a observação direta continua sendo a única fonte de certos dados (atitude, amostra orientada, descrição detalhada).
- Sensoriamento remoto usa a assinatura espectral de diferentes materiais, capturada por sensores orbitais em várias faixas do espectro eletromagnético, para distinguir rochas e minerais a distância.
- O modelo digital de elevação (MDE) permite gerar relevo sombreado, declividade e perfis topográficos automaticamente.
- GPS calcula posição por triangulação de sinais de satélite, com precisão de metros (uso geral) a centímetros (equipamento geodésico/diferencial).
- Um SIG organiza todos esses dados em camadas sobrepostas e referenciadas geograficamente, permitindo cruzar informações para planejar e interpretar o mapeamento.
- Um projeto de mapeamento moderno alterna entre gabinete (planejamento e integração via SIG/sensoriamento remoto) e campo (observação direta), em ciclo, não numa única passada.

## Próxima aula

[[20-metodos-campo-mapeamento-aula-07-teoria-dos-erros-topografia-nbr13133|Aula 07 — Medida de distâncias e de ângulos e a teoria dos erros na topografia (NBR 13133)]] aprofunda a precisão instrumental: a partir daqui, o módulo passa do GPS de uso geral e do SIG para a topografia instrumental (estação total, nivelamento, GNSS geodésico) usada quando o mapeamento exige precisão centimétrica.

## Fontes

- USGS, [Remote Sensing](https://www.usgs.gov/faqs/what-remote-sensing-and-what-it-used), consulta em 2026-08-18.
- USGS, [The Global Positioning System](https://www.usgs.gov/faqs/what-does-gps-stand-and-what-does-gps-do), consulta em 2026-08-18.

<!--
nivel: ensino-medio-sem-geologia-v1
palavras_corpo: ~1250
mapa_objetivo_secao:
  geologia-m20-oa06: "Campo continua sendo a fonte da verdade" + "Sensoriamento remoto" + "GPS" + "SIG" + "O ciclo real de um projeto de mapeamento moderno" + "Exemplo trabalhado"
alegacoes_auditaveis:
  - claim_id: GEO-M20-A06-ASSINATURA-ESPECTRAL-001
    claim: "Diferentes materiais de superfície (rocha, solo, vegetação, óxidos de ferro) têm assinaturas espectrais distintas, capturáveis por sensores orbitais multiespectrais, permitindo mapear zonas de alteração hidrotermal a distância."
    risk: metodologico
    source: "sensoriamento remoto geológico padrão (ex.: USGS; literatura de exploração mineral por imageamento espectral)"
  - claim_id: GEO-M20-A06-GPS-PRECISAO-002
    claim: "Receptores GPS de uso geral têm precisão tipicamente da ordem de metros; GPS diferencial/geodésico chega à ordem de centímetros."
    risk: numerico
    source: "USGS; especificações padrão de sistemas GNSS civis e geodésicos"
-->
