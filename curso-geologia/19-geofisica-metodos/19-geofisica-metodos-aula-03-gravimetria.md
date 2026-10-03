# Aula 03: Gravimetria — encontrando massa escondida pelo campo gravitacional

**ID:** geologia-m19-a03
**Módulo:** [[19-geofisica-metodos-modulo|Módulo 19 — Geofísica: métodos e imageamento da Terra]]
**Duração estimada:** ~26 min
**Objetivo:** explicar como pequenas variações no campo gravitacional da Terra revelam diferenças de densidade em profundidade, e como essas variações precisam ser corrigidas antes de interpretadas.

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **Método potencial** | Método geofísico baseado em um campo de força que decai com a distância (gravidade, magnetismo), sem precisar de uma fonte ativa gerada pelo operador. |
| **Anomalia gravimétrica** | Diferença entre a gravidade medida (corrigida) e um valor de referência teórico; positiva indica excesso de massa/densidade, negativa indica déficit. |
| **Correção de ar-livre** | Ajuste que compensa a variação de gravidade só pela diferença de altitude da estação em relação ao nível do mar (sem considerar a massa da rocha entre eles). |
| **Correção Bouguer** | Ajuste que remove o efeito gravitacional da massa de rocha entre a estação e o datum de referência, assumindo uma densidade média. |
| **Anomalia Bouguer** | Anomalia obtida após as correções de latitude, ar-livre e Bouguer (**anomalia Bouguer simples**); quando também se aplica a correção de terreno, chama-se **anomalia Bouguer completa** — é essa que se interpreta em termos de estrutura geológica em terreno acidentado. |
| **Não unicidade** | Propriedade dos métodos potenciais pela qual infinitas distribuições de densidade em profundidade podem produzir a mesma anomalia observada na superfície. |

## Antes de começar, você precisa saber

- Densidade típica de rochas ígneas, sedimentares e metamórficas — [[06-rochas-igneas-modulo|Módulo 06]], [[07-rochas-sedimentares-modulo|Módulo 07]], [[08-rochas-metamorficas-modulo|Módulo 08]].
- Isostasia e equilíbrio de blocos de crosta sobre o manto — [[18-tectonica-global-geodinamica-modulo|Módulo 18]].

## Ao final você vai conseguir

- [geologia-m19-oa03 · parte 1 de 2] Explicar o que é uma anomalia gravimétrica, quais correções são necessárias para obtê-la e o que ela permite (e não permite) concluir sobre estrutura em profundidade. (A parte 2 de `oa03`, sobre magnetometria, é coberta na Aula 04.)

## Conteúdo

### Gravidade não é uma constante — é um dado

Todo mundo aprende que "g = 9,8 m/s²", como se fosse um número fixo. Na prática, a gravidade medida na superfície da Terra varia de lugar para lugar, em quantidades minúsculas mas mensuráveis, por causa da forma da Terra (achatada nos polos), da rotação, da altitude do ponto e — o que interessa à geofísica de exploração — da **distribuição de massa (densidade) nas rochas abaixo do ponto de medição**. Um corpo de rocha mais denso que o entorno (por exemplo, um corpo de minério metálico, ou uma intrusão máfica) puxa a gravidade local levemente para cima; um corpo menos denso (uma cavidade, um domo de sal, uma bacia sedimentar espessa) puxa para baixo.

A **gravimetria** mede essas variações minúsculas com instrumentos de altíssima precisão — gravímetros capazes de detectar diferenças da ordem de partes por bilhão da gravidade — e as interpreta como pistas sobre o que existe em profundidade. É, junto com a magnetometria (próxima aula), um **método potencial**: não precisa de uma fonte ativa como a sísmica; mede um campo que já existe, gerado pela própria massa da Terra.

### Da leitura bruta à anomalia: por que corrigir

Uma leitura bruta de gravímetro não serve para nada sozinha, porque é dominada por efeitos que nada têm a ver com a geologia local: a latitude (a Terra é achatada, então a gravidade varia sistematicamente do equador aos polos), a altitude da estação (gravidade diminui com a distância ao centro da Terra) e a topografia ao redor (uma montanha ao lado puxa a leitura para cima; um vale, para baixo). Isolar o sinal geológico exige remover, em sequência, cada um desses efeitos — um processo chamado de **redução gravimétrica**.

As correções principais, aplicadas em ordem, são:

1. **Correção de latitude** — remove a variação sistemática esperada pela forma e rotação da Terra, comparando a leitura a um valor de referência teórico (a "gravidade normal" para aquela latitude).
2. **Correção de ar-livre** — compensa apenas a diferença de altitude entre a estação e o nível do mar (datum), como se não houvesse massa nenhuma entre os dois — trata a estação como se estivesse "no ar".
3. **Correção Bouguer** — depois de saber a altitude, é preciso reconhecer que **há**, sim, uma laje de rocha entre a estação e o datum, e essa laje também exerce atração gravitacional. A correção Bouguer remove esse efeito, assumindo uma densidade média para essa "laje" (tipicamente ~2,67 g/cm³ para crosta continental padrão).
4. **Correção de terreno** — ajusta o efeito de morros e vales próximos que a aproximação de "laje plana" da correção Bouguer não captura.

O resultado final é a **anomalia Bouguer**: o que sobra da leitura de gravidade depois de descontar tudo que não é "geologia local em profundidade". Vale guardar a distinção de nomenclatura, porque mapas e artigos a usam: parar na correção Bouguer (etapa 3, com a aproximação de laje plana infinita) produz a **anomalia Bouguer simples**; acrescentar a correção de terreno (etapa 4) produz a **anomalia Bouguer completa**. Em terreno plano as duas quase coincidem; em terreno acidentado, a diferença é significativa. Uma anomalia positiva sugere excesso de massa (rocha mais densa que a densidade padrão assumida) abaixo daquele ponto; uma anomalia negativa sugere déficit de massa.

### O que a gravimetria enxerga bem — e o problema que ela nunca resolve sozinha

A gravimetria é sensível a **contraste de densidade**, não a tipo de rocha por si só — o que importa é a diferença de densidade entre o corpo-alvo e a rocha encaixante ao redor. Por isso funciona bem para:

- Mapear a espessura de **bacias sedimentares** (rochas sedimentares, menos densas, sobre embasamento cristalino mais denso, gera anomalia negativa sobre a bacia).
- Localizar corpos de **minério metálico** denso (sulfetos maciços, por exemplo) como anomalias positivas discretas.
- Mapear domos de **sal**, que é bem menos denso que a rocha sedimentar encaixante, como anomalias negativas características.
- Estudar a **isostasia** regional — se uma cadeia de montanhas está ou não em equilíbrio de flutuação sobre o manto, comparando a anomalia Bouguer observada com a esperada para uma crosta espessada compensando isostaticamente.

O limite fundamental de qualquer método potencial — gravimetria e magnetometria igualmente — é a **não unicidade**: uma mesma anomalia observada na superfície pode ser produzida por infinitas combinações diferentes de forma, profundidade e contraste de densidade do corpo em profundidade. Um corpo pequeno, denso e raso pode produzir a mesma anomalia que um corpo grande, menos denso e mais profundo. Por isso a interpretação gravimétrica **nunca** conclui sozinha; ela restringe hipóteses e é sempre combinada com geologia de superfície conhecida, poços, ou outros métodos (sísmica, magnetometria) para reduzir a ambiguidade.

> **Apoio visual:** um perfil de anomalia Bouguer ao longo de uma linha que cruza uma bacia sedimentar mostraria uma curva em "U" — gravidade mais baixa no centro da bacia (mais sedimento leve empilhado), subindo nas bordas onde o embasamento denso está mais raso.

## Exemplo trabalhado

Uma linha de estações gravimétricas cruza uma região onde se suspeita a presença de uma bacia sedimentar sobre embasamento granítico. Depois de aplicadas as correções de latitude, ar-livre, Bouguer e terreno, o perfil de anomalia Bouguer mostra um mínimo de -25 mGal no centro da linha, subindo gradualmente para -5 mGal nas bordas, ao longo de ~15 km.

A leitura qualitativa: o mínimo central indica déficit de massa relativo — coerente com sedimento (densidade típica ~2,3–2,5 g/cm³) substituindo granito (densidade típica ~2,65–2,70 g/cm³) numa espessura maior no centro da bacia. Um modelo direto (assumindo uma geometria simples e o contraste de densidade estimado) converteria essa anomalia numa estimativa de espessura de sedimento — mas, por causa da não unicidade, essa estimativa só ganha confiança real quando calibrada por um poço de referência ou por uma linha sísmica de reflexão na mesma área, que resolve a geometria com muito mais precisão vertical.

## Recap relâmpago

- Gravimetria é um método potencial: mede o campo gravitacional já existente, sem precisar de fonte ativa.
- A leitura bruta precisa de correções (latitude, ar-livre, Bouguer, terreno) para virar uma anomalia Bouguer interpretável.
- Anomalia positiva sugere excesso de massa/densidade em profundidade; negativa, déficit.
- É sensível a contraste de densidade, não ao tipo de rocha por si só — útil para bacias, corpos de minério denso, domos de sal e estudos de isostasia.
- Todo método potencial sofre de não unicidade: a mesma anomalia pode vir de infinitas combinações de forma, profundidade e densidade — por isso não interpreta sozinho.

## Próxima aula

[[19-geofisica-metodos-aula-04-magnetometria|Aula 04 — Magnetometria]] segue no mesmo grupo de métodos potenciais, trocando densidade por magnetização — e mostra por que os dois métodos, aplicados juntos, ajudam a reduzir a não unicidade um do outro.

## Fontes

- USGS, [Gravity Data of the United States](https://www.usgs.gov/programs/national-geological-and-geophysical-data-preservation-program/science/gravity-data), consulta em 2026-08-18.
- SEG Wiki, [Gravity method](https://wiki.seg.org/wiki/Gravity_method), consulta em 2026-08-18.

<!--
nivel: geologia-avancado-v1
palavras_corpo: ~1050
mapa_objetivo_secao:
  geologia-m19-oa03: "Gravidade não é uma constante" + "Da leitura bruta à anomalia" + "O que a gravimetria enxerga bem" + "Exemplo trabalhado"
alegacoes_auditaveis:
  - claim_id: GEO-M19-A03-CORRECOES-001
    claim: "A anomalia Bouguer resulta da aplicação sequencial das correções de latitude, ar-livre, Bouguer e terreno sobre a leitura gravimétrica bruta."
    risk: mecanismo
    source: "SEG Wiki, Gravity method"
  - claim_id: GEO-M19-A03-NAO-UNICIDADE-002
    claim: "Métodos potenciais (gravimetria, magnetometria) sofrem de não unicidade: a mesma anomalia de superfície pode ser produzida por múltiplas combinações de forma, profundidade e contraste físico do corpo."
    risk: mecanismo
    source: "SEG Wiki, Gravity method; literatura padrão de geofísica de exploração"
  - claim_id: GEO-M19-A03-DENSIDADE-003
    claim: "Densidade típica de granito ~2,65-2,70 g/cm3; de rocha sedimentar ~2,3-2,5 g/cm3 (valores de ordem de grandeza, variam com litologia e compactação)."
    risk: numerico
    source: "Valores de referência padrão de petrofísica/geofísica de exploração"
-->
