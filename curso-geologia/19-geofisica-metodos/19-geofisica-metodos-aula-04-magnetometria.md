# Aula 04: Magnetometria — lendo a magnetização das rochas

**ID:** geologia-m19-a04
**Módulo:** [[19-geofisica-metodos-modulo|Módulo 19 — Geofísica: métodos e imageamento da Terra]]
**Duração estimada:** ~24 min
**Objetivo:** explicar como o campo magnético terrestre e a magnetização das rochas são usados para mapear estruturas geológicas, e como a magnetometria se soma à gravimetria na interpretação.

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **Campo geomagnético principal** | Campo magnético de larga escala gerado pelo dínamo do núcleo externo líquido; é o "fundo" sobre o qual se medem as anomalias. |
| **Suscetibilidade magnética** | Propriedade de um material que mede o quanto ele se magnetiza na presença de um campo externo; controla a resposta magnética da rocha. |
| **Magnetita** | Óxido de ferro (Fe₃O₄) fortemente magnético; o mineral que mais domina a resposta magnética da maioria das rochas. |
| **Anomalia magnética** | Diferença entre o campo magnético medido e o campo geomagnético de referência esperado naquele ponto. |
| **Temperatura de Curie** | Temperatura acima da qual um material perde sua magnetização permanente; para a magnetita, cerca de 580 °C, o que limita a profundidade máxima de fontes magnéticas na crosta. |
| **Magnetometria aérea** | Levantamento magnético feito por aeronave, cobrindo grandes áreas rapidamente com custo por km² muito menor que o terrestre. |

## Antes de começar, você precisa saber

- O conceito de anomalia, correção e não unicidade em métodos potenciais — [[19-geofisica-metodos-aula-03-gravimetria|Aula 03]].
- Minerais opacos de Fe-Ti formadores de rocha (magnetita, ilmenita) — [[05-mineralogia-identificacao-optica-modulo|Módulo 05]].
- O campo magnético terrestre e sua origem no núcleo — [[02-sistema-terra-tectonica-modulo|Módulo 02]].

## Ao final você vai conseguir

- [geologia-m19-oa03 · parte 2 de 2] Explicar o que controla a resposta magnética das rochas, como se calcula uma anomalia magnética e em que tipos de alvo geológico a magnetometria é mais eficaz. (A parte 1 de `oa03`, sobre gravimetria, foi coberta na Aula 03.)

## Conteúdo

### O mesmo princípio, um campo diferente

A magnetometria é irmã da gravimetria: também é um **método potencial**, mede um campo que já existe (não precisa de fonte artificial) e também sofre de não unicidade. A diferença está no campo medido e na propriedade física que ele revela: em vez de densidade, a magnetometria é sensível à **magnetização** das rochas — o quanto cada rocha responde ao campo magnético terrestre e reforça (ou enfraquece) o campo medido na superfície logo acima dela.

O **campo geomagnético principal** — gerado pelo movimento de convecção do ferro líquido no núcleo externo, funcionando como um dínamo natural — domina totalmente a leitura de qualquer magnetômetro. Uma leitura bruta em qualquer ponto da Terra é, de longe, majoritariamente esse campo de fundo; o sinal geológico de interesse é uma perturbação minúscula sobre ele, medida em **nanotesla (nT)**, tipicamente na faixa de dezenas a poucas centenas de nT, contra um campo de fundo da ordem de dezenas de milhares de nT. Remover o campo de fundo teórico esperado (modelado globalmente, como o *International Geomagnetic Reference Field*, IGRF) da leitura bruta produz a **anomalia magnética**.

### Por que magnetita domina tudo

A maioria das rochas é fracamente magnética — quase todos os silicatos comuns (quartzo, feldspato, a maior parte dos minerais formadores de rocha) contribuem muito pouco para a resposta magnética. O que realmente controla o sinal é a presença, mesmo que em pequena quantidade, de minerais fortemente magnéticos — sobretudo a **magnetita** (Fe₃O₄) e as **titanomagnetitas** (a série magnetita–ulvoespinélio, comum em rochas vulcânicas), e em menor grau a pirrotita. Cuidado com um par que se parece: a **ilmenita** (FeTiO₃) é um óxido de Fe-Ti abundante, mas *paramagnética* à temperatura ambiente (sua temperatura de Néel fica bem abaixo de zero), e por isso praticamente não contribui para a anomalia — quem contribui, nas rochas que a contêm, são as intercrescências e as fases ricas em magnetita associadas a ela. Uma rocha com poucos por cento de magnetita disseminada pode dominar completamente a anomalia magnética de uma área, mesmo que o restante da rocha seja "magneticamente invisível".

Essa dependência de um mineral acessório específico, e não da composição química geral da rocha, faz da magnetometria uma ferramenta especialmente afiada para:

- **Litologias que costumam ser ricas em magnetita**: rochas ígneas máficas e ultramáficas (basalto, gabro, diabásio) costumam gerar anomalias magnéticas mais fortes que rochas félsicas (granito) ou sedimentares (em geral pobres em magnetita), o que ajuda a mapear contatos e corpos ígneos sob cobertura.
- **Corpos de minério associados a óxidos de ferro** (depósitos do tipo IOCG — óxido de ferro-cobre-ouro —, alguns depósitos de ferro bandado) que se destacam como anomalias positivas fortes.
- **Estruturas e falhas**, que muitas vezes alteram hidrotermalmente a magnetita original (destruindo-a) e por isso aparecem como "trilhas" de baixo magnetismo cortando um padrão regional mais magnético.

### O limite térmico: por que a anomalia não vem de qualquer profundidade

Existe um limite físico importante que a gravimetria não tem: a **temperatura de Curie**. Acima de certa temperatura (para a magnetita, cerca de 580 °C), a agitação térmica dos átomos destrói o alinhamento magnético ordenado do mineral, e o material perde a magnetização permanente — vira "magneticamente transparente", mesmo contendo magnetita. Como a temperatura aumenta com a profundidade (gradiente geotérmico), existe uma profundidade máxima — variável conforme o gradiente geotérmico local, mas tipicamente da ordem de dezenas de quilômetros na crosta continental — abaixo da qual nenhuma fonte pode contribuir para a anomalia magnética observada, porque tudo ali já passou da temperatura de Curie. Esse limite ajuda inclusive a estimar profundezas de isotermas em estudos de fluxo de calor regional, invertendo a lógica: a profundidade da "base magnética" (onde a anomalia desaparece) pode indicar onde a crosta cruza a temperatura de Curie.

### Aeromagnetometria: cobertura rápida, resolução regional

Por ser um método potencial passivo (não precisa de fonte artificial nem de contato físico com o solo), a magnetometria se presta muito bem a levantamentos **aéreos**: um avião ou drone voando em linhas paralelas, a altitude e espaçamento controlados, cobre milhares de quilômetros quadrados em dias, a um custo por área muito menor que qualquer método terrestre. A **magnetometria aérea** é hoje a ferramenta padrão de reconhecimento regional em exploração mineral — o primeiro passo antes de qualquer trabalho de campo detalhado, porque revela rapidamente padrões estruturais (falhas, contatos litológicos, corpos intrusivos) que orientam onde concentrar levantamentos mais caros (gravimetria terrestre detalhada, sísmica, sondagem).

Combinar magnetometria e gravimetria na mesma área é uma prática comum justamente porque reduz a não unicidade de cada método isolado: um corpo que é ao mesmo tempo denso *e* magnético (por exemplo, certos corpos de sulfeto maciço ou intrusões máficas) aparece como anomalia coincidente nos dois mapas, o que fortalece muito a interpretação — enquanto um corpo denso mas não magnético, ou magnético mas não denso, aparece em só um dos dois, ajudando a distinguir a causa provável.

## Exemplo trabalhado

Um levantamento aeromagnético sobre uma área de exploração mineral revela uma anomalia magnética positiva alongada, de forma linear, cruzando uma região onde o mapa geológico de superfície mostra apenas cobertura de solo residual sem afloramento. A anomalia tem cerca de 200 nT de amplitude acima do campo regional e se estende por 8 km.

A interpretação de reconhecimento: a forma linear e a amplitude sugerem um corpo tabular raso, rico em magnetita, coerente com um dique máfico (basáltico ou diabásico) ou uma zona de alteração associada a uma falha mineralizada — ambas hipóteses plausíveis e não descartáveis apenas com o dado magnético. O próximo passo do fluxo de trabalho seria sobrepor um dado gravimétrico na mesma linha: se houver também anomalia gravimétrica positiva coincidente, a hipótese de corpo máfico denso ganha força; se a gravimetria não mostrar nada, a hipótese de zona de falha com magnetita secundária (sem contraste de densidade relevante) passa a ser mais provável. Só sondagem confirmaria qual das duas está certa.

## Recap relâmpago

- Magnetometria mede a anomalia sobre o campo geomagnético principal (gerado no núcleo), em nanotesla; é sensível à magnetização, não à densidade.
- A resposta magnética da maioria das rochas é dominada por um único mineral acessório: a magnetita.
- Acima da temperatura de Curie (~580 °C para magnetita), o material perde a magnetização — o que limita a profundidade máxima de fontes magnéticas na crosta.
- Rochas máficas/ultramáficas e corpos ricos em óxidos de ferro tendem a gerar anomalias fortes; sedimentares e félsicas, anomalias fracas.
- A aeromagnetometria é o método padrão de reconhecimento regional em exploração mineral, por cobrir grandes áreas rapidamente e a baixo custo.
- Combinar magnetometria e gravimetria reduz a não unicidade de cada método isolado.

## Próxima aula

[[19-geofisica-metodos-aula-05-metodos-eletricos-eletromagneticos-e-geotermicos|Aula 05 — Métodos elétricos, eletromagnéticos e geotérmicos]] deixa a família dos métodos potenciais e passa a métodos que exploram a resistividade elétrica e o fluxo de calor da subsuperfície.

## Fontes

- USGS, [Aeromagnetic Surveys](https://www.usgs.gov/programs/national-geological-and-geophysical-data-preservation-program/science/aeromagnetic-surveys), consulta em 2026-08-18.
- SEG Wiki, [Magnetic method](https://wiki.seg.org/wiki/Magnetic_method), consulta em 2026-08-18.

<!--
nivel: geologia-avancado-v1
palavras_corpo: ~1080
mapa_objetivo_secao:
  geologia-m19-oa03: "O mesmo princípio, um campo diferente" + "Por que magnetita domina tudo" + "O limite térmico" + "Aeromagnetometria" + "Exemplo trabalhado"
alegacoes_auditaveis:
  - claim_id: GEO-M19-A04-MAGNETITA-001
    claim: "A resposta magnética da maioria das rochas é dominada pela presença de magnetita, mesmo em baixa proporção, e não pela composição química geral da rocha."
    risk: mecanismo
    source: "SEG Wiki, Magnetic method"
  - claim_id: GEO-M19-A04-CURIE-002
    claim: "A temperatura de Curie da magnetita é de aproximadamente 580 °C; acima dela, o material perde magnetização permanente."
    risk: numerico
    source: "Valor padrão de física de minerais/geofísica (Curie point da magnetita)"
  - claim_id: GEO-M19-A04-AMPLITUDE-003
    claim: "Anomalias magnéticas de interesse geológico são tipicamente de dezenas a algumas centenas de nT sobre um campo de fundo da ordem de dezenas de milhares de nT."
    risk: numerico
    source: "SEG Wiki, Magnetic method; ordens de grandeza padrão de levantamentos aeromagnéticos"
-->
