# Aula 02: Sísmica de reflexão e refração — imageando a subsuperfície com ondas artificiais

**ID:** geologia-m19-a02
**Módulo:** [[19-geofisica-metodos-modulo|Módulo 19 — Geofísica: métodos e imageamento da Terra]]
**Duração estimada:** ~28 min
**Objetivo:** explicar como levantamentos sísmicos de reflexão e refração usam ondas geradas artificialmente para mapear camadas e estruturas da subsuperfície.

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **Fonte sísmica** | Dispositivo que gera a onda artificial: explosivo, caminhão vibrador (*vibroseis*), canhão de ar (*airgun*) em levantamentos marinhos. |
| **Geofone / hidrofone** | Sensor que registra o movimento do solo (geofone, em terra) ou a pressão da água (hidrofone, no mar) causado pela onda que retorna. |
| **Impedância acústica** | Produto da densidade da rocha pela velocidade da onda P nela; um contraste de impedância entre camadas é o que gera uma reflexão. |
| **Sísmica de reflexão** | Método que registra ondas refletidas em interfaces de camadas, usado para mapear estrutura em detalhe até profundezas de vários quilômetros. |
| **Sísmica de refração** | Método que registra ondas refratadas criticamente ao longo de uma interface de alta velocidade, usado para determinar velocidades de camadas e profundidades regionais. |
| **Migração sísmica** | Processamento que reposiciona reflexões inclinadas para sua localização geométrica real, corrigindo a distorção da aquisição. |
| **Seção sísmica** | Imagem final, em tempo (ou profundidade), mostrando refletores ao longo de uma linha de aquisição — o produto que o intérprete lê. |

## Antes de começar, você precisa saber

- Que ondas P e S têm velocidades diferentes e que a velocidade sísmica depende do meio — [[19-geofisica-metodos-aula-01-sismologia-e-ondas-sismicas|Aula 01]].
- Princípios de estratigrafia e reconhecimento de camadas — [[03-tempo-geologico-geocronologia-modulo|Módulo 03]].

## Ao final você vai conseguir

- [geologia-m19-oa02] Distinguir sísmica de reflexão de sísmica de refração pelo fenômeno físico explorado, pela profundidade de investigação e pelo tipo de estrutura que cada uma resolve melhor.

## Conteúdo

### Uma sismologia em miniatura, sob controle

A Aula 01 usou terremotos naturais como fonte de ondas para inferir a estrutura profunda da Terra. A **sísmica de exploração** aplica exatamente a mesma física — ondas que viajam a velocidades diferentes em meios diferentes — mas trocando o terremoto por uma fonte controlada, ativada em posições conhecidas, e trocando estações globais por uma grade densa de sensores locais (geofones em terra, hidrofones no mar). O ganho é resolução: em vez de imagens grosseiras de milhares de quilômetros, a sísmica de exploração resolve estruturas de metros a poucos quilômetros, o suficiente para mapear uma bacia sedimentar, uma falha ou uma armadilha de petróleo.

Existem dois métodos irmãos, que exploram fenômenos físicos diferentes na mesma família de ondas: **reflexão** e **refração**.

### Reflexão: quando a onda bate e volta

Quando uma onda sísmica encontra uma interface entre duas camadas de **impedância acústica** diferente — o produto de densidade pela velocidade da onda P —, parte da energia é refletida de volta à superfície, como luz batendo num vidro. Quanto maior o contraste de impedância, mais forte a reflexão; uma interface sem contraste não gera reflexão nenhuma, mesmo que separe rochas de nomes diferentes.

Numa aquisição de reflexão, a fonte é disparada e uma linha (ou grade, em 3D) de sensores registra a chegada de energia refletida em cada interface abaixo. Repetindo esse disparo em muitas posições ao longo de uma linha, e processando os dados (correção de tempo, empilhamento de traços redundantes e **migração**, que reposiciona reflexões inclinadas para o lugar geometricamente correto), o resultado é uma **seção sísmica**: uma imagem em corte que mostra os refletores como se fosse uma radiografia das camadas.

A reflexão é o método de maior resolução vertical e lateral entre os sísmicos, e por isso é o principal método de exploração de petróleo e gás, de mapeamento de bacias sedimentares e de estudos geotécnicos rasos de alta precisão. O custo é logístico: exige aquisição densa (muitas fontes e receptores) e processamento computacional pesado.

### Refração: quando a onda "corre" ao longo da interface

A sísmica de refração explora um fenômeno diferente: a **refração crítica**. Quando uma onda atinge uma interface entre uma camada mais lenta (acima) e outra mais rápida (abaixo) num ângulo específico — o **ângulo crítico** —, parte da energia não reflete nem penetra: ela viaja *ao longo* da interface na velocidade da camada inferior, mais rápida, e continuamente "vaza" energia de volta à superfície, num padrão análogo a uma onda de choque.

Em distâncias suficientemente grandes da fonte, essa onda refratada — mesmo percorrendo um caminho mais longo (desce, corre ao lado, sobe de novo) — chega **antes** da onda que viajou direto pela camada superior mais lenta, porque a maior velocidade ao longo do trecho intermediário compensa o caminho extra. É essa "chegada em primeira quebra" que os geofísicos leem para calcular a **velocidade** de cada camada e a **profundidade** da interface, a partir da geometria dos tempos de chegada em função da distância fonte-receptor.

A refração dá resolução vertical mais grosseira que a reflexão, mas exige aquisição mais simples e barata, e é especialmente eficaz para determinar velocidades regionais e profundidade do embasamento cristalino. Foi exatamente esse fenômeno — a onda refratada criticamente chegando antes da direta a grandes distâncias — que permitiu a Andrija Mohorovičić identificar, em 1909, a **descontinuidade de Mohorovičić** (o limite crosta-manto, ou "Moho"). Vale a ressalva histórica: ele não dispunha de um levantamento com fonte artificial como os descritos aqui, e sim das curvas de tempo-percurso de um **terremoto natural** (vale do Kupa, Croácia, 8 de outubro de 1909), nas quais identificou um segundo conjunto de chegadas P mais rápidas além de algumas centenas de quilômetros. Levantamentos de refração com fonte controlada vieram depois e passaram a mapear o Moho rotineiramente.

### Como escolher entre os dois

A escolha não é estética: reflexão e refração respondem perguntas diferentes.

- **Reflexão** é o método de escolha quando o objetivo é mapear a **geometria detalhada** de camadas — estruturas, falhas, dobras, armadilhas — em profundidades de dezenas de metros a vários quilômetros, com resolução de metros. É o padrão da indústria de petróleo e gás.
- **Refração** é o método de escolha quando o objetivo é obter **velocidades de camada** e **profundidade do embasamento** em levantamentos regionais ou geotécnicos rasos (por exemplo, determinar a espessura de solo até a rocha sã antes de uma fundação), com menor exigência de equipamento.

Na prática, muitos levantamentos combinam os dois: a refração ajuda a calibrar velocidades usadas na conversão tempo-profundidade da seção de reflexão, porque a sísmica bruta é medida em **tempo de percurso** (segundos), não em profundidade — transformar um eixo de tempo em um eixo de profundidade real exige conhecer a velocidade sísmica de cada camada, e é aí que os dois métodos se encontram.

> **Apoio visual:** imagine dois raios saindo da mesma fonte — um reflete na interface e volta em linha quase vertical até um receptor próximo (reflexão); outro desce até o ângulo crítico, "corre" horizontalmente na camada rápida e sobe de novo, sendo captado por um receptor distante primeiro que a onda direta (refração). São dois caminhos geométricos diferentes explorando a mesma interface.

## Exemplo trabalhado

Um levantamento de refração terrestre dispara uma fonte e registra os primeiros tempos de chegada em geofones a distâncias crescentes (10 m, 50 m, 100 m, 300 m, 500 m da fonte). Para distâncias pequenas, o tempo de chegada cresce em linha reta com a distância, numa inclinação que corresponde à velocidade da camada superior (por exemplo, solo/rocha alterada, ~500 m/s). A partir de certa distância — o **ponto de cruzamento** —, a inclinação muda para uma reta mais suave, correspondente a uma velocidade maior (por exemplo, rocha sã, ~3.500 m/s): esse é o sinal de que, a partir dali, a onda refratada criticamente chega antes da onda direta.

A distância em que ocorre essa mudança de inclinação (o ponto de cruzamento) permite calcular, por geometria simples envolvendo as duas velocidades, a profundidade da interface solo–rocha sã. Esse é exatamente o tipo de resultado usado em estudos geotécnicos: "a rocha sã começa a X metros de profundidade neste local" — informação direta para projeto de fundações, sem precisar perfurar um poço em cada ponto do terreno.

## Recap relâmpago

- A sísmica de exploração usa fontes controladas e sensores densos para aplicar, em escala local, o mesmo princípio de tempo de percurso da sismologia natural.
- Reflexão: energia que volta em interfaces de contraste de impedância acústica; alta resolução; produz seções sísmicas detalhadas; padrão em petróleo e gás.
- Refração: energia que viaja ao longo de uma interface no ângulo crítico e chega antes em distâncias maiores; dá velocidades de camada e profundidade de embasamento; mais barata e mais grosseira.
- Sísmica bruta é medida em tempo; converter para profundidade exige velocidades, frequentemente obtidas por refração ou por poços de calibração.
- Foi a análise de ondas refratadas criticamente — em registros de um terremoto natural, não num levantamento com fonte artificial — que levou Mohorovičić a identificar o Moho em 1909.

## Próxima aula

[[19-geofisica-metodos-aula-03-gravimetria|Aula 03 — Gravimetria]] muda de família de método: em vez de ondas elásticas, usa variações no campo gravitacional da Terra para inferir diferenças de densidade em profundidade.

## Fontes

- Kearey, Brooks & Hill, *An Introduction to Geophysical Exploration*, 3ª ed. — literatura padrão de geofísica de exploração usada como base do método descrito.
- SEG (Society of Exploration Geophysicists), [SEG Wiki — Seismic reflection method](https://wiki.seg.org/wiki/Seismic_reflection_method), consulta em 2026-08-18.
- SEG Wiki, [Seismic refraction method](https://wiki.seg.org/wiki/Seismic_refraction_method), consulta em 2026-08-18.

<!--
nivel: geologia-avancado-v1
palavras_corpo: ~1150
mapa_objetivo_secao:
  geologia-m19-oa02: "Uma sismologia em miniatura" + "Reflexão" + "Refração" + "Como escolher entre os dois" + "Exemplo trabalhado"
alegacoes_auditaveis:
  - claim_id: GEO-M19-A02-IMPEDANCIA-001
    claim: "Uma reflexão sísmica ocorre em interfaces com contraste de impedância acústica (densidade x velocidade P); sem contraste, não há reflexão."
    risk: mecanismo
    source: "SEG Wiki, Seismic reflection method; Kearey, Brooks & Hill"
  - claim_id: GEO-M19-A02-REFRACAO-CRITICA-002
    claim: "Refração crítica ocorre no ângulo crítico numa interface de velocidade crescente; a onda refratada pode chegar antes da onda direta em distâncias maiores."
    risk: mecanismo
    source: "SEG Wiki, Seismic refraction method"
  - claim_id: GEO-M19-A02-MOHO-003
    claim: "A descontinuidade de Mohorovičić foi identificada em 1909 a partir de ondas refratadas criticamente registradas de um terremoto natural (vale do Kupa), não de um levantamento de refração com fonte artificial."
    risk: historico
    source: "Literatura clássica de sismologia (Mohorovičić, 1909/1910); revisão histórica em Prodehl & Mooney, 100 years of seismic research on the Moho"
-->
