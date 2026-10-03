# Aula 03: Série de reação de Bowen e diferenciação magmática

**ID:** geologia-m06-a03
**Módulo:** [[06-rochas-igneas-modulo|Módulo 06 — Rochas ígneas e magmatismo]]
**Duração estimada:** ~30 min
**Objetivo:** usar a série de reação de Bowen para explicar a ordem geral de cristalização e a mudança do líquido magmático.

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **Cristalização** | Formação de um sólido mineral organizado a partir de um líquido. |
| **Série de Bowen** | Modelo experimental da ordem geral de cristalização de silicatos comuns. |
| **Série descontínua** | Ramo em que um mineral é substituído por outro de estrutura diferente. |
| **Série contínua** | Ramo em que o plagioclásio muda gradualmente de composição. |
| **Plagioclásio** | Série de feldspatos entre membros mais ricos em cálcio e em sódio. |
| **Diferenciação magmática** | Evolução de um magma para líquidos e rochas de composições diferentes. |

## Antes de começar, você precisa saber

- Como separar cristais pode mudar o líquido restante — [[06-rochas-igneas-aula-02-geracao-e-evolucao-dos-magmas|aula 02 deste módulo]].
- Que olivina, piroxênio, anfibólio, biotita, quartzo e feldspatos são minerais distintos — [[05-mineralogia-identificacao-optica-aula-02-grupos-minerais-formadores-de-rocha|Módulo 05, aula 02]].
- Que uma solução sólida varia entre membros extremos — [[04-cristalografia-quimica-minerais-aula-03-definicao-de-mineral|Módulo 04, aula 03]].

## Ao final você vai conseguir

- [geologia-m06-oa03] Aplicar a série de reação de Bowen para prever tendências gerais de cristalização e diferenciação magmática.

## Conteúdo

### Uma fila de ingredientes que se solidificam

Quando uma mistura de chocolate com frutas esfria, alguns ingredientes endurecem antes de outros. A ordem não é aleatória: depende do material e das condições. A **série de reação de Bowen** resume uma ordem geral, vista em experimentos e em rochas, pela qual minerais silicáticos comuns cristalizam de um magma em resfriamento.

“Reação” não significa explosão. Se um cristal inicial continua em contato com um líquido que mudou ao resfriar, ele pode reagir e dar lugar a mineral mais estável nas novas condições. O modelo tem dois ramos.

~~~mermaid
flowchart TB
  subgraph D["Ramo descontínuo"]
    O["olivina"] --> P["piroxênio"] --> A["anfibólio"] --> B["biotita"]
  end
  subgraph C["Ramo contínuo"]
    PC["plagioclásio mais rico em cálcio"] --> PS["plagioclásio mais rico em sódio"]
  end
  B --> T["feldspato potássico, muscovita e quartzo: tardios, se a composição permitir"]
  PS --> T
~~~

*Observe: à esquerda, minerais diferentes se sucedem; à direita, o plagioclásio muda de composição.*

### Dois ramos, duas mudanças

No **ramo descontínuo**, muda a identidade do mineral: olivina, piroxênio, anfibólio e biotita. É como trocar uma peça inteira de um jogo de montar por outra, com encaixes diferentes. Nem todo magma passa por todos: água, pressão, composição inicial e resfriamento modificam o resultado.

No **ramo contínuo**, o mineral continua sendo plagioclásio, mas sua composição muda gradualmente de mais rica em cálcio para mais rica em sódio. A analogia é ajustar as proporções de duas tintas sem trocar de tinta. Isso é possível porque plagioclásios formam uma solução sólida.

Na parte tardia aparecem feldspato potássico, muscovita e quartzo, desde que os componentes necessários estejam disponíveis. Eles não são “melhores”; apenas costumam cristalizar mais tarde no modelo.

### Por que isso diferencia um magma

Se cristais iniciais ficam em contato com o líquido e reagem completamente, o sistema pode se aproximar do equilíbrio. Mas se são retirados do líquido, há **cristalização fracionada**. É como retirar castanhas de uma granola: o restante deixa de ter a mesma receita.

Minerais iniciais tendem a retirar do líquido componentes que suas estruturas aceitam, como ferro, magnésio e cálcio em muitos casos. O líquido restante fica relativamente enriquecido no que não foi capturado. A sequência ajuda a explicar por que um magma pode produzir rochas com maior proporção de minerais máficos ou félsicos.

Antes de seguir: por que retirar cristais produz efeito maior no líquido do que deixá-los reagir com ele durante todo o resfriamento?

## Exemplo trabalhado

Um líquido contém componentes capazes de formar olivina, piroxênio, plagioclásio e, mais tarde, quartzo. Olivina cristaliza cedo e é separada.

1. A olivina incorpora parte do ferro e magnésio.
2. Como saiu, não reage completamente com o líquido ao continuar o resfriamento.
3. O líquido torna-se relativamente menos máfico e pode formar outros minerais.
4. A conclusão não é “toda olivina vira piroxênio”, mas que Bowen prevê tendências de cristalização e diferenciação.

## Erros comuns

- **Ler a série como lista obrigatória.** Ela é modelo geral; condições reais alteram o caminho.
- **Achar que “contínua” significa ausência de mudança.** O plagioclásio muda de composição.
- **Supor que quartzo sempre aparece.** É preciso restar sílica suficiente no líquido.

## O que não concluir

- **Que a série identifica sozinha uma rocha.** Ela explica cristalização; classificação formal por proporções minerais entra na aula 06.
- **Que fornece temperaturas exatas universais.** Pressão, água e composição deslocam intervalos de cristalização.

## Recap relâmpago

- Bowen resume tendências gerais de cristalização de silicatos.
- Ramo descontínuo: olivina → piroxênio → anfibólio → biotita.
- Ramo contínuo: plagioclásio mais cálcico → mais sódico.
- Minerais tardios só aparecem se a composição permitir.
- Separar cristais do líquido produz diferenciação por fracionamento.

## Próxima aula

[[06-rochas-igneas-aula-04-texturas-igneas-e-resfriamento|Aula 04 — Texturas ígneas e história de resfriamento]] mostra o que o tamanho e o arranjo dos cristais contam sobre o resfriamento.

## Fontes

- GIA, [Gems Formed in Magmatic Rocks](https://www.gia.edu/gems-gemology/winter-2022-colored-stones-unearthed), consulta em 2026-08-17.
- U.S. Geological Survey, [Magma mixing and crystal fractionation](https://volcanoes.usgs.gov/observatories/yvo/jlowenstern/meltinclusions/pet_studies.php), consulta em 2026-08-17.

<!--
nivel: ensino-medio-sem-geologia-v1
palavras_corpo: ~850
mapa_objetivo_secao:
  geologia-m06-oa03: "Uma fila de ingredientes que se solidificam" + "Dois ramos, duas mudanças" + "Por que isso diferencia um magma" + "Exemplo trabalhado"
alegacoes_auditaveis:
  - claim_id: GEO-M06-A03-BOWEN-RAMOS-001
    claim: "A série de Bowen descreve uma tendência geral do ramo descontínuo olivina-piroxênio-anfibólio-biotita e do plagioclásio de mais cálcico para mais sódico no ramo contínuo."
    risk: classificacao
    source: "GIA, Gems Formed in Magmatic Rocks"
  - claim_id: GEO-M06-A03-FRACIONAMENTO-002
    claim: "Separar cristais do líquido durante o resfriamento pode modificar a composição do líquido remanescente."
    risk: mecanismo
    source: "USGS, Magma mixing and crystal fractionation"
-->
