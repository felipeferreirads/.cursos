# Aula 06: Perfilagem de poços e integração de dados geofísicos

**ID:** geologia-m19-a06
**Módulo:** [[19-geofisica-metodos-modulo|Módulo 19 — Geofísica: métodos e imageamento da Terra]]
**Duração estimada:** ~28 min
**Objetivo:** descrever os principais perfis geofísicos de poço e explicar como eles calibram e se integram aos métodos de superfície estudados no módulo.

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **Perfilagem de poço (*well logging*)** | Registro contínuo de propriedades físicas das rochas ao longo da profundidade de um poço, feito por uma ferramenta descida no furo. |
| **Perfil de raios gama (GR)** | Registra a radioatividade natural da rocha; usado sobretudo para distinguir folhelho (mais radioativo) de arenito/carbonato limpo (menos radioativo). |
| **Perfil sônico** | Mede o tempo de trânsito de uma onda sísmica através de um intervalo de rocha, dando a velocidade sísmica local — a ponte direta com a sísmica de superfície. |
| **Perfil de densidade** | Mede a densidade da rocha por atenuação de radiação gama emitida pela própria ferramenta; a ponte direta com a gravimetria. |
| **Perfil de resistividade de poço** | Mede a resistividade da rocha ao redor do furo; ajuda a distinguir fluido nos poros (água doce, água salgada, óleo, gás) — a ponte direta com os métodos elétricos de superfície. |
| **Sismograma sintético** | Sismograma artificial gerado a partir dos perfis sônico e de densidade de um poço, usado para amarrar (calibrar) a seção sísmica de superfície à profundidade real medida no poço. |
| **Integração de dados (*data integration*)** | Prática de combinar dois ou mais métodos geofísicos (e geológicos) independentes para reduzir a ambiguidade que cada um tem isoladamente. |

## Antes de começar, você precisa saber

- Sísmica de reflexão mede em tempo, não em profundidade — [[19-geofisica-metodos-aula-02-sismica-de-reflexao-e-refracao|Aula 02]].
- Gravimetria e magnetometria são sensíveis a densidade e magnetização, respectivamente — [[19-geofisica-metodos-aula-03-gravimetria|Aula 03]], [[19-geofisica-metodos-aula-04-magnetometria|Aula 04]].
- Resistividade de rocha é controlada pelo fluido nos poros — [[19-geofisica-metodos-aula-05-metodos-eletricos-eletromagneticos-e-geotermicos|Aula 05]].

## Ao final você vai conseguir

- [geologia-m19-oa05] Descrever o que medem os principais perfis geofísicos de poço e explicar como eles calibram e reduzem a ambiguidade dos métodos de superfície do módulo.

## Conteúdo

### Um poço é o único lugar onde a geofísica "vê de perto"

Todos os métodos das aulas anteriores — sísmica, gravimetria, magnetometria, elétricos — são **indiretos**: medem um campo ou uma onda na superfície (ou no ar) e inferem, por trás, o que existe em profundidade, sempre sujeitos a ambiguidade. A **perfilagem de poços** é o oposto: uma ferramenta é descida diretamente dentro de um furo já perfurado e mede as propriedades físicas da rocha *in situ*, centímetro a centímetro de profundidade, ao longo de toda a extensão do poço. É a informação mais direta e de maior resolução vertical que a geofísica oferece — o preço é que só existe onde já se perfurou, então é um dado pontual (um poço mede uma coluna vertical, não uma área).

Por isso, a perfilagem de poços cumpre uma dupla função no fluxo de trabalho geofísico: (1) caracteriza diretamente as rochas atravessadas pelo poço, servindo à interpretação geológica local; e (2) fornece os **valores reais de calibração** — velocidade sísmica real, densidade real, resistividade real — que os métodos de superfície precisam para converter suas medidas indiretas (tempo, anomalia, resistividade aparente) em profundidade e propriedade física confiáveis.

### Os perfis básicos, um a um

O **perfil de raios gama (GR)** mede a radioatividade natural da rocha, emitida principalmente por potássio, tório e urânio presentes na matriz mineral. Argilominerais (presentes em folhelhos) costumam concentrar mais desses elementos que quartzo ou calcita limpos; por isso o GR é, na prática, o perfil mais usado para diferenciar rapidamente folhelho (alta radioatividade) de arenito ou carbonato "limpos" (baixa radioatividade) — uma leitura rápida da litologia dominante ao longo do poço, sem precisar de amostra física.

O **perfil sônico** mede o tempo que uma onda sísmica leva para atravessar um intervalo padronizado de rocha ao redor do poço, dando diretamente a velocidade sísmica local (o inverso do tempo de trânsito). É a ponte mais direta com a sísmica de reflexão da Aula 02: como a sísmica de superfície mede em tempo, e o poço conhece a profundidade real de cada camada, combinar sônico com profundidade permite converter tempo em profundidade com precisão — a etapa essencial antes de interpretar qualquer seção sísmica em termos geológicos reais.

O **perfil de densidade** mede a densidade da rocha por atenuação de radiação gama emitida pela própria ferramenta (uma fonte radioativa controlada) e captada de volta por um detector — quanto mais densa a rocha, mais ela absorve a radiação. É a ponte direta com a gravimetria: fornece o valor de densidade real usado para calibrar (ou substituir) a densidade média assumida na correção Bouguer, além de, combinado com o perfil sônico, permitir calcular a impedância acústica real — o parâmetro que controla a força das reflexões sísmicas.

O **perfil de resistividade de poço** mede a resistividade da rocha ao redor do furo, com ferramentas elétricas ou de indução análogas em princípio aos métodos de superfície da Aula 05. É especialmente valioso porque a resistividade responde fortemente ao **tipo de fluido** nos poros: água doce, água salgada, óleo e gás têm resistividades muito diferentes entre si, o que faz da resistividade de poço uma das ferramentas centrais para identificar zonas produtoras de hidrocarboneto em geologia do petróleo: água salgada é muito condutiva (baixa resistividade), enquanto óleo e gás, ocupando o espaço poroso que a água salgada deixaria, são muito mais resistivos.

### O sismograma sintético: a régua que amarra tempo a profundidade

Combinando o perfil sônico (velocidade) com o perfil de densidade (densidade), calcula-se a **impedância acústica** ao longo de todo o poço — exatamente a propriedade que controla onde e quão forte a sísmica de reflexão gera um refletor (Aula 02). A partir dessa impedância calculada, é possível construir um **sismograma sintético**: um sismograma artificial, previsto matematicamente a partir dos dados de poço, que mostra onde reflexões deveriam aparecer, em que tempo, se a sísmica de superfície estivesse vendo exatamente a mesma coluna de rocha que o poço atravessou.

Comparando esse sismograma sintético com a seção sísmica real de superfície na posição do poço, o intérprete ajusta (amarra) a escala de tempo da sísmica à escala de profundidade real do poço — um processo chamado de **amarração poço-sísmica**. Sem essa etapa, uma seção sísmica mostra refletores num eixo de tempo que não tem correspondência direta e confiável com profundidade real; depois da amarração, cada refletor da seção sísmica passa a ter uma profundidade geológica atribuída com confiança, e essa confiança se propaga para toda a área coberta pela sísmica, não apenas o ponto do poço.

### Por que nenhum método sozinho basta

O fio condutor de todo este módulo é que cada método geofísico é sensível a **uma propriedade física diferente** (velocidade sísmica, densidade, magnetização, resistividade, radioatividade, fluxo de calor) e cada um, isoladamente, carrega uma ambiguidade própria — não unicidade nos métodos potenciais, resolução limitada na sísmica de refração, custo e cobertura na perfilagem de poço. Nenhum desses métodos, sozinho, "resolve" a subsuperfície; o que resolve é a **integração**: usar cada método para restringir e calibrar os outros, de modo que hipóteses que sobrevivem a múltiplas linhas de evidência independentes ficam muito mais confiáveis que qualquer leitura isolada.

Um fluxo de trabalho típico de exploração combina: aeromagnetometria e/ou gravimetria regional para reconhecimento rápido de grandes estruturas; sísmica de reflexão para geometria detalhada de camadas; métodos elétricos/EM para alvos condutivos específicos; e, assim que há um poço disponível, perfilagem para calibrar tudo o que veio antes e reduzir a ambiguidade residual. É esse ciclo — reconhecimento amplo, foco progressivo, calibração direta — que caracteriza o trabalho real de um geofísico de exploração, muito mais do que a aplicação isolada de qualquer método deste módulo.

> **Apoio visual:** lado a lado, um perfil GR (mostrando picos em folhelho), um perfil sônico (mostrando velocidade menor em folhelho, maior em arenito compacto ou carbonato) e a seção sísmica correspondente já amarrada em profundidade ilustrariam como a mesma sequência de camadas aparece de três formas físicas diferentes, mas geometricamente consistentes.

## Exemplo trabalhado

Um poço exploratório perfura uma sequência que inclui, a 2.400 m de profundidade, um intervalo de 30 m com GR baixo (rocha "limpa"), velocidade sônica alta (~4.800 m/s) e resistividade muito alta comparada às camadas de água salgada acima e abaixo.

A leitura integrada: GR baixo descarta folhelho, indicando arenito ou carbonato; velocidade alta é coerente com rocha bem litificada e pouco porosa, ou porosa mas com fluido resistivo nos poros; e a resistividade muito acima do esperado para água salgada é o indicador mais direto de que os poros dessa rocha não estão saturados com água salgada, mas sim com um fluido muito mais resistivo — a assinatura clássica de uma zona com **hidrocarboneto** (óleo ou gás) nos poros. Nenhum dos três perfis, isolado, seria conclusivo (rocha compacta seca também dá velocidade alta; um carbonato puro também dá GR baixo); é a combinação dos três que sustenta a interpretação, exatamente o princípio de integração que fecha o módulo.

## Recap relâmpago

- Perfilagem de poço mede propriedades físicas diretamente na rocha atravessada — a informação mais direta e de maior resolução vertical da geofísica, mas limitada ao ponto do poço.
- GR distingue folhelho (alto) de rocha limpa (baixo); sônico dá velocidade sísmica; densidade complementa o sônico para impedância acústica; resistividade de poço distingue tipo de fluido nos poros.
- O sismograma sintético, construído de sônico + densidade, permite amarrar a sísmica de superfície (em tempo) à profundidade real do poço.
- Cada método geofísico é sensível a uma propriedade física diferente e carrega sua própria ambiguidade; a integração entre métodos é o que sustenta interpretações confiáveis, não qualquer método isolado.

## Próxima aula

Este é o fechamento do Módulo 19. O [[20-metodos-campo-mapeamento-modulo|Módulo 20 — Métodos de campo e mapeamento geológico]] volta à superfície e trata de como o geólogo integra tudo isso — geofísica incluída — ao trabalho direto de campo e ao mapa geológico.

## Fontes

- SEG Wiki, [Well logging](https://wiki.seg.org/wiki/Well_logging), consulta em 2026-08-18.
- Schlumberger Oilfield Glossary (glossário técnico padrão da indústria), termos "gamma ray log", "sonic log", "density log", "synthetic seismogram", consulta em 2026-08-18.

<!--
nivel: geologia-avancado-v1
palavras_corpo: ~1230
mapa_objetivo_secao:
  geologia-m19-oa05: "Um poço é o único lugar" + "Os perfis básicos" + "O sismograma sintético" + "Por que nenhum método sozinho basta" + "Exemplo trabalhado"
alegacoes_auditaveis:
  - claim_id: GEO-M19-A06-GR-001
    claim: "O perfil de raios gama mede radioatividade natural (K, Th, U), usado sobretudo para distinguir folhelho (mais radioativo) de arenito/carbonato limpos (menos radioativo)."
    risk: mecanismo
    source: "SEG Wiki, Well logging; Schlumberger Oilfield Glossary"
  - claim_id: GEO-M19-A06-SINTETICO-002
    claim: "O sismograma sintético é gerado combinando perfis sônico e de densidade (impedância acústica) e usado para amarrar a sísmica de superfície à profundidade real do poço."
    risk: mecanismo
    source: "Schlumberger Oilfield Glossary, synthetic seismogram"
  - claim_id: GEO-M19-A06-RESISTIVIDADE-POCO-003
    claim: "A resistividade de poço responde fortemente ao tipo de fluido nos poros (água salgada muito condutiva; óleo e gás muito mais resistivos), usada para identificar zonas produtoras."
    risk: mecanismo
    source: "SEG Wiki, Well logging; Schlumberger Oilfield Glossary, resistivity log"
-->
