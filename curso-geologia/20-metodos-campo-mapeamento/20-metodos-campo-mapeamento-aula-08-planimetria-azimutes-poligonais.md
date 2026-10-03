# Aula 08: Planimetria — azimutes, rumos, coordenadas e o fechamento de poligonais com estação total

**ID:** geologia-m20-a08
**Módulo:** [[20-metodos-campo-mapeamento-modulo|Módulo 20 — Métodos de campo e mapeamento geológico]]
**Duração estimada:** ~29 min
**Objetivo:** entender como azimute e rumo descrevem uma direção, como uma poligonal topográfica é calculada em coordenadas a partir de ângulos e distâncias, e como se verifica se ela fecha dentro da tolerância aceitável.
**Pré-requisito:** [[20-metodos-campo-mapeamento-aula-07-teoria-dos-erros-topografia-nbr13133|Aula 07 — Medida de distâncias e de ângulos e a teoria dos erros na topografia]]

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **Azimute** | Ângulo horizontal medido a partir do norte, no sentido horário, de 0° a 360°, até a direção de interesse. |
| **Rumo** | Ângulo horizontal medido a partir do norte ou do sul, para leste ou para oeste, sempre entre 0° e 90°, acompanhado do quadrante (ex.: N30E). |
| **Poligonal** | Sequência de pontos ligados por alinhamentos retos, medidos em ângulo e distância, usada como esqueleto de apoio de um levantamento topográfico. |
| **Projeções (Δx, Δy)** | As componentes norte-sul e leste-oeste de um alinhamento, calculadas a partir de sua distância e de seu azimute. |
| **Erro de fechamento** | A diferença entre a coordenada final calculada de uma poligonal fechada e sua coordenada inicial conhecida — deveria ser exatamente zero num levantamento sem erro algum. |
| **Precisão relativa** | O erro de fechamento expresso como fração do perímetro total da poligonal (ex.: 1:15.000), usado para comparar poligonais de tamanhos diferentes. |
| **Compensação (regra de Bowditch)** | Método de distribuir o erro de fechamento entre os lados da poligonal, proporcionalmente ao comprimento de cada um, para obter coordenadas finais ajustadas. |

## Antes de começar, você precisa saber

- Como se mede um ângulo e uma distância com estação total, e a diferença entre erro sistemático e acidental — [[20-metodos-campo-mapeamento-aula-07-teoria-dos-erros-topografia-nbr13133|Aula 07]].
- Como coordenadas geográficas localizam um ponto de campo — [[20-metodos-campo-mapeamento-aula-01-observacao-registro-amostragem|Aula 01]].

## Ao final você vai conseguir

- [geologia-m20-oa08] Calcular azimutes, rumos e coordenadas de uma poligonal e verificar seu erro de fechamento.

## Conteúdo

### Do ângulo lido ao ponto no mapa

A Aula 07 mostrou como medir ângulo e distância com precisão instrumental. Esta aula fecha o ciclo da **planimetria** (a geometria horizontal do levantamento, sem considerar altitude): como transformar essas medidas — ângulo e distância entre pontos sucessivos — em coordenadas utilizáveis num mapa, e como verificar se o resultado é confiável antes de aceitá-lo.

### Azimute e rumo: duas formas de dizer a mesma direção

**Azimute** é o ângulo horizontal medido a partir do norte, sempre no sentido horário, variando continuamente de 0° a 360°. Um alinhamento apontando exatamente para leste tem azimute 90°; apontando para sul, azimute 180°; para noroeste, azimute 315°. É a forma mais direta de descrever uma direção para cálculo, porque cada valor de azimute corresponde a exatamente uma direção, sem ambiguidade.

**Rumo** é uma notação mais antiga, ainda comum em documentos e plantas: mede o ângulo a partir do norte **ou** do sul, para leste **ou** para oeste, sempre entre 0° e 90°, e precisa vir acompanhado do quadrante para ser interpretado — por exemplo, "N30E" (30° a leste do norte) ou "S45W" (45° a oeste do sul). Um rumo de 30° sozinho é ambíguo (poderia ser em qualquer um dos quatro quadrantes); o azimute correspondente a N30E é simplesmente 30°, e a um rumo S45W corresponde o azimute 180° + 45° = 225°. A conversão entre os dois depende de em qual quadrante o rumo está: no primeiro quadrante (NE) azimute = rumo; no segundo (SE) azimute = 180° − rumo; no terceiro (SW) azimute = 180° + rumo; no quarto (NW) azimute = 360° − rumo.

### De ângulo e distância a coordenadas: as projeções

Cada lado de uma poligonal, com sua distância medida e seu azimute calculado, pode ser decomposto em duas componentes: o quanto ele avança para norte-sul e para leste-oeste. Essas componentes são chamadas de **projeções**, e se calculam com trigonometria simples: a projeção norte-sul (chamada tradicionalmente de "latitude" do lado, sem relação com a latitude geográfica) é a distância multiplicada pelo cosseno do azimute; a projeção leste-oeste ("departamento" ou "abscissa") é a distância multiplicada pelo seno do azimute. Somando essas projeções, lado a lado, a partir de um ponto de coordenada conhecida, chega-se à coordenada de cada vértice seguinte da poligonal — é assim que uma estação total, medindo só ângulo e distância a cada estação, entrega ao final um conjunto de coordenadas relativas de toda a poligonal.

### O teste da poligonal fechada: será que os números batem?

Quando a poligonal é **fechada** — isto é, o último lado retorna ao ponto de partida (ou a outro ponto de coordenada já conhecida) — surge um teste poderoso: somando todas as projeções norte-sul, o resultado deveria ser exatamente zero (o deslocamento total em norte-sul, ao longo de um percurso fechado, tem que se cancelar); o mesmo vale para a soma das projeções leste-oeste. Na prática, por causa do erro acidental acumulado em cada medida de ângulo e distância (Aula 07), a soma nunca fecha em exatamente zero — sobra um pequeno resíduo em cada eixo, chamado de **erro de fechamento linear**, cuja magnitude (a distância entre o ponto final calculado e o ponto inicial conhecido) mede o quanto de erro acidental se acumulou ao longo de toda a poligonal.

Esse erro de fechamento, sozinho, não diz muito — um erro de 30 cm é insignificante numa poligonal de 3 km de perímetro, mas seria grave numa de 50 m. Por isso se calcula a **precisão relativa**: o erro de fechamento dividido pelo perímetro total, expresso como fração (ex.: erro de fechamento de 20 cm num perímetro de 3.000 m dá uma precisão relativa de 1:15.000). É esse número — não o erro absoluto — que se compara à tolerância mínima da NBR 13133 (Aula 07) para decidir se a poligonal é aceitável.

Se a poligonal fecha dentro da tolerância, o pequeno erro residual costuma ser distribuído entre os vértices por um método de **compensação** — o mais comum, a regra de Bowditch, distribui a correção em cada lado proporcionalmente ao seu comprimento (lados mais longos, que em geral carregam mais oportunidade de erro acidental acumulado, recebem correção proporcionalmente maior), gerando coordenadas finais ajustadas para uso no mapa.

## Exemplo trabalhado

Uma poligonal fechada de três lados começa e termina no mesmo ponto P0, com coordenada (0, 0). As distâncias e azimutes medidos são: lado 1, 120 m, azimute 60°; lado 2, 150 m, azimute 170°; lado 3, 130 m, azimute 290°. Calculando as projeções de cada lado (distância × cos(azimute) para norte-sul, distância × sen(azimute) para leste-oeste):

- Lado 1: ΔN = 120 × cos(60°) = 60,0 m; ΔE = 120 × sen(60°) = 103,9 m
- Lado 2: ΔN = 150 × cos(170°) = −147,7 m; ΔE = 150 × sen(170°) = 26,0 m
- Lado 3: ΔN = 130 × cos(290°) = 44,5 m; ΔE = 130 × sen(290°) = −122,2 m

Somando: ΔN total = 60,0 − 147,7 + 44,5 = −43,2 m (deveria ser 0); ΔE total = 103,9 + 26,0 − 122,2 = 7,7 m (deveria ser 0). O erro de fechamento linear é a distância desse ponto até a origem: √(43,2² + 7,7²) ≈ 43,9 m. Esse valor, isoladamente, seria alarmante — mas o perímetro da poligonal é 120 + 150 + 130 = 400 m, o que daria uma precisão relativa de aproximadamente 1:9 (43,9 m de erro em 400 m de perímetro), muito pior que qualquer tolerância da NBR 13133. Nesse caso hipotético, um erro dessa magnitude para um perímetro tão curto indicaria quase certamente um **erro grosseiro** não detectado (um ângulo ou distância anotado errado), e a poligonal deveria ser refeita ou reconferida em campo antes de qualquer compensação — compensar (distribuir) um erro dessa ordem seria mascarar um problema real, não corrigi-lo.

## Recap relâmpago

- Azimute mede direção a partir do norte, 0° a 360°, sentido horário; rumo mede a partir do norte ou do sul, 0° a 90°, com quadrante — os dois descrevem a mesma direção, mas exigem conversão entre si.
- Cada lado de uma poligonal se decompõe em projeções norte-sul e leste-oeste (distância × cosseno e distância × seno do azimute), que somadas a partir de um ponto conhecido geram as coordenadas dos vértices seguintes.
- Numa poligonal fechada, a soma das projeções deveria ser exatamente zero em cada eixo; o resíduo real é o erro de fechamento linear.
- A precisão relativa (erro de fechamento dividido pelo perímetro) é o que se compara à tolerância da norma — não o erro absoluto isolado.
- Um erro de fechamento muito acima do esperado para o perímetro é sinal de erro grosseiro não detectado, não de erro acidental normal — a poligonal deve ser reconferida, não simplesmente compensada.
- A compensação (ex.: regra de Bowditch) distribui um erro de fechamento aceitável entre os lados, proporcionalmente ao comprimento de cada um.

## Próxima aula

[[20-metodos-campo-mapeamento-aula-09-nivelamento-curvas-de-nivel-areas-volumes|Aula 09 — Altimetria: nivelamento geométrico, trigonométrico e barométrico; curvas de nível, áreas e volumes]] muda o eixo de medida da horizontal para a vertical: em vez de coordenadas no plano, o desnível entre pontos.

## Fontes

- Literatura técnica de topografia sobre cálculo de poligonais planimétricas (azimute, rumo, projeções, erro de fechamento, compensação por Bowditch), consultada em 2026-08-29.

<!--
nivel: ensino-medio-sem-geologia-v1
palavras_corpo: ~1300
mapa_objetivo_secao:
  geologia-m20-oa08: "Do ângulo lido ao ponto no mapa" + "Azimute e rumo: duas formas de dizer a mesma direção" + "De ângulo e distância a coordenadas: as projeções" + "O teste da poligonal fechada: será que os números batem?" + "Exemplo trabalhado"
alegacoes_auditaveis:
  - claim_id: GEO-M20-A08-AZIMUTE-RUMO-CONVERSAO-001
    claim: "Conversão entre rumo e azimute depende do quadrante: NE azimute=rumo, SE azimute=180-rumo, SW azimute=180+rumo, NW azimute=360-rumo."
    risk: conceitual
    source: "trigonometria padrão de topografia plana, consistente com literatura técnica revisada em 2026-08-29"
  - claim_id: GEO-M20-A08-EXEMPLO-NUMERICO-002
    claim: "Valores numéricos do exemplo trabalhado (projeções, erro de fechamento, precisão relativa) foram calculados diretamente pela trigonometria descrita no texto, não extraídos de fonte externa."
    risk: numerico
    source: "cálculo interno consistente (seno/cosseno dos azimutes fornecidos), conferir arredondamento se reaproveitado como questão de prova"
-->
