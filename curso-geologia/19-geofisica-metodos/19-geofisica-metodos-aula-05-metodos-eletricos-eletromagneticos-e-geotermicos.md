# Aula 05: Métodos elétricos, eletromagnéticos e geotérmicos

**ID:** geologia-m19-a05
**Módulo:** [[19-geofisica-metodos-modulo|Módulo 19 — Geofísica: métodos e imageamento da Terra]]
**Duração estimada:** ~28 min
**Objetivo:** descrever como métodos de resistividade, eletromagnéticos e geotérmicos mapeiam a subsuperfície explorando propriedades elétricas e térmicas das rochas.

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **Resistividade elétrica** | Propriedade de um material que mede sua oposição à passagem de corrente elétrica; em rochas, controlada sobretudo pela água nos poros e sua salinidade. |
| **Eletrorresistividade (ER)** | Método que injeta corrente no solo por eletrodos e mede a diferença de potencial resultante, para calcular resistividade em profundidade. |
| **Polarização induzida (IP)** | Método que mede a capacidade de um material armazenar carga elétrica temporariamente (efeito capacitivo), sensível à presença de minerais metálicos disseminados. |
| **Eletromagnético (EM)** | Família de métodos que induz correntes no solo por indução eletromagnética (sem contato físico via eletrodo) e mede o campo secundário resultante. |
| **Condutor** | Corpo de baixa resistividade (alta condutividade) — tipicamente água salgada, argila, ou minério metálico maciço — que se destaca fortemente em levantamentos EM. |
| **Fluxo de calor geotérmico** | Taxa de transferência de calor do interior da Terra para a superfície, controlada pelo gradiente geotérmico e pela condutividade térmica das rochas. |
| **Gradiente geotérmico** | Taxa de aumento da temperatura com a profundidade; em média continental, cerca de 25–30 °C/km, mas varia muito por contexto tectônico. |

## Antes de começar, você precisa saber

- O conceito de anomalia e de contraste de propriedade física entre corpo e encaixante — [[19-geofisica-metodos-aula-03-gravimetria|Aula 03]], [[19-geofisica-metodos-aula-04-magnetometria|Aula 04]].
- Porosidade e permeabilidade em rochas sedimentares — [[07-rochas-sedimentares-modulo|Módulo 07]].

## Ao final você vai conseguir

- [geologia-m19-oa04] Explicar o que controla a resistividade das rochas, distinguir métodos elétricos (com contato) de eletromagnéticos (sem contato), e relacionar gradiente geotérmico e fluxo de calor a contextos tectônicos.

## Conteúdo

### O que faz uma rocha conduzir eletricidade

Ao contrário do que a intuição sugere, a rocha em si quase não conduz: minerais formadores de rocha (quartzo, feldspato, calcita) são, em geral, excelentes isolantes elétricos — ou seja, condutores muito pobres. O que realmente controla a **resistividade** de uma rocha, na imensa maioria dos casos, não é o mineral sólido, mas a **água que preenche seus poros e fraturas** — e, mais especificamente, a quantidade de sais dissolvidos nessa água, porque a condução elétrica em rocha porosa ocorre majoritariamente por íons dissolvidos se movendo no fluido, não por elétrons se movendo no mineral.

Isso tem uma consequência prática poderosa: uma rocha porosa saturada com água doce é muito mais resistiva que a mesma rocha saturada com água salgada; uma rocha compacta e seca é altamente resistiva; uma argila (que retém água ligada em sua estrutura mineral, além de ter capacidade de troca iônica na superfície das partículas) costuma ser condutiva mesmo sem muita água livre. Corpos de minério metálico maciço (sulfetos, grafita) são exceções importantes: conduzem eletricidade diretamente pelo próprio mineral, por condução eletrônica, não iônica — e por isso se destacam como fortemente condutivos mesmo secos.

### Eletrorresistividade: injetar corrente e medir a queda de potencial

O método de **eletrorresistividade (ER)** é o mais direto dos métodos elétricos: um par de eletrodos injeta corrente elétrica no solo, e outro par mede a diferença de potencial resultante em pontos próximos. A partir da geometria dos eletrodos e da voltagem medida, calcula-se uma **resistividade aparente** — que, com múltiplas configurações de espaçamento e posição de eletrodos, pode ser invertida (processada matematicamente) para estimar como a resistividade real varia com a profundidade e lateralmente, gerando um perfil ou uma pseudo-seção de resistividade.

A ER é amplamente usada em hidrogeologia (localizar aquíferos, mapear intrusão de água salgada em aquíferos costeiros, já que água salgada e doce têm resistividades muito diferentes), em geotecnia (mapear zonas de solo saturado ou fraturado antes de uma obra) e em arqueologia rasa. A limitação prática é a necessidade de contato físico dos eletrodos com o solo, o que limita a velocidade de aquisição em terrenos extensos ou de acesso difícil.

### Polarização induzida: o "eco" elétrico dos minerais metálicos

Um método relacionado, a **polarização induzida (IP)**, usa a mesma injeção de corrente por eletrodos, mas mede algo diferente: em vez (ou além) da resistividade, mede o quanto o solo se comporta como um capacitor — acumulando carga durante a injeção e liberando-a lentamente quando a corrente é desligada, gerando uma "voltagem residual" que decai ao longo de milissegundos a segundos. Esse efeito de polarização é especialmente forte em rochas com **minerais metálicos disseminados** (sulfetos finamente distribuídos, não necessariamente maciços) — cada grão metálico funciona como um pequeno eletrodo que se polariza e despolariza.

Isso torna o IP uma ferramenta particularmente valiosa em exploração mineral para depósitos de sulfeto disseminado (como pórfiros de cobre), que muitas vezes têm resistividade pouco diferente da rocha encaixante — não seriam bem detectados só por ER — mas mostram um efeito de polarização muito mais forte, por causa da abundância de grãos metálicos dispersos, ainda que em baixa concentração volumétrica.

### Métodos eletromagnéticos: sem tocar o chão

Os métodos **eletromagnéticos (EM)** resolvem a limitação de contato físico da ER: em vez de injetar corrente por eletrodos, uma bobina transmissora gera um campo magnético variável no tempo, que induz correntes elétricas no subsolo (por indução eletromagnética, sem necessidade de contato) — e essas correntes induzidas, por sua vez, geram um campo magnético secundário, que uma bobina receptora capta. A intensidade e a fase desse campo secundário revelam a condutividade da subsuperfície: corpos muito condutivos (**condutores** — sulfetos maciços, grafita, água salgada, argila condutiva) respondem fortemente e de forma característica.

Como não exige contato com o solo, o EM se presta bem a levantamentos aéreos rápidos (análogos à aeromagnetometria) e é o método de escolha clássico para localizar corpos de sulfeto maciço em exploração mineral — a razão histórica pela qual o EM aéreo se tornou padrão em muitos distritos de mineração de metais base (níquel, cobre, zinco).

### Métodos geotérmicos: o calor que sobe de dentro

Um grupo diferente de métodos usa não a eletricidade, mas o **calor**. A Terra perde calor continuamente para o espaço, transferido do interior para a superfície — o **fluxo de calor geotérmico** — e a taxa com que a temperatura sobe com a profundidade, o **gradiente geotérmico**, varia de forma sistemática com o contexto tectônico: é anomalamente alto em zonas de vulcanismo ativo, dorsais meso-oceânicas e áreas de crosta adelgaçada (rifts), e mais baixo em crátons antigos, estáveis e de crosta espessa. Um valor de referência médio continental é da ordem de 25–30 °C por km, mas esse número varia amplamente por contexto — em campos geotérmicos ativos, pode ser muitas vezes maior em profundidade rasa.

Levantamentos geotérmicos medem temperatura em poços a diferentes profundidades (para calcular o gradiente local) e a **condutividade térmica** das rochas atravessadas (para calcular o fluxo de calor real, que é o produto do gradiente pela condutividade). Esses dados são a base direta da exploração de energia geotérmica — identificar áreas com fluxo de calor alto o suficiente para gerar vapor ou água quente aproveitável — e também alimentam modelos de maturação de matéria orgânica em geologia do petróleo (a temperatura em profundidade, ao longo do tempo geológico, controla quando uma rocha-geradora produz óleo ou gás).

> **Apoio visual:** um mapa de contorno de gradiente geotérmico regional mostraria valores baixos e uniformes sobre um cráton antigo, contrastando com uma faixa estreita de valores muito altos ao longo de uma zona de rift ativo ou arco vulcânico — o mesmo tipo de contraste que a Aula 19 já associou a diferentes ambientes tectônicos.

## Exemplo trabalhado

Uma investigação hidrogeológica costeira usa ER para verificar se um aquífero de água doce está sendo invadido por água do mar. O perfil de resistividade mostra valores altos (>100 ohm·m) na porção rasa do aquífero, próximos à linha de costa, mas caindo abruptamente para valores muito baixos (<5 ohm·m) numa cunha que se aprofunda em direção ao continente a partir do litoral.

A leitura: água doce é resistiva; água salgada, por causa da alta concentração iônica, é muito condutiva (baixa resistividade). A cunha de baixa resistividade que avança sob o continente é a assinatura clássica de **intrusão salina** — água do mar mais densa se infiltrando por baixo da água doce mais leve num aquífero costeiro sobre-explotado. Esse é exatamente o tipo de diagnóstico rápido e não invasivo (sem precisar perfurar múltiplos poços de monitoramento) que a ER oferece em gestão de recursos hídricos.

## Recap relâmpago

- Resistividade de rocha é controlada, na maioria dos casos, pela água nos poros e sua salinidade — não pelo mineral sólido, exceto em minério metálico maciço (condução eletrônica).
- ER injeta corrente por eletrodos e mede potencial; útil para aquíferos, intrusão salina, geotecnia — mas exige contato físico.
- IP mede o efeito de polarização (capacitivo) do solo; sensível a minerais metálicos disseminados, mesmo com pouco contraste de resistividade.
- EM induz correntes por bobina, sem contato físico; padrão em exploração aérea de sulfetos maciços e outros condutores fortes.
- Fluxo de calor geotérmico e gradiente geotérmico variam sistematicamente com o contexto tectônico — altos em rifts e vulcanismo ativo, baixos em crátons estáveis.

## Próxima aula

[[19-geofisica-metodos-aula-06-perfilagem-de-pocos-e-integracao-de-dados|Aula 06 — Perfilagem de poços e integração de dados geofísicos]] fecha o módulo mostrando como medir essas mesmas propriedades físicas (velocidade sísmica, densidade, resistividade, radioatividade) diretamente dentro de um poço, e como calibrar e integrar todos os métodos de superfície entre si.

## Fontes

- SEG Wiki, [Electrical resistivity method](https://wiki.seg.org/wiki/Electrical_resistivity_method), consulta em 2026-08-18.
- SEG Wiki, [Induced polarization](https://wiki.seg.org/wiki/Induced_polarization), consulta em 2026-08-18.
- USGS, [Geothermal gradients in the conterminous United States](https://www.usgs.gov/publications/geothermal-gradients-conterminous-united-states), consulta em 2026-08-18.

<!--
nivel: geologia-avancado-v1
palavras_corpo: ~1180
mapa_objetivo_secao:
  geologia-m19-oa04: "O que faz uma rocha conduzir eletricidade" + "Eletrorresistividade" + "Polarização induzida" + "Métodos eletromagnéticos" + "Métodos geotérmicos" + "Exemplo trabalhado"
alegacoes_auditaveis:
  - claim_id: GEO-M19-A05-RESISTIVIDADE-001
    claim: "A resistividade elétrica de rochas porosas é controlada majoritariamente pela água nos poros e sua salinidade (condução iônica), não pelo mineral sólido, exceto em minério metálico maciço (condução eletrônica)."
    risk: mecanismo
    source: "SEG Wiki, Electrical resistivity method"
  - claim_id: GEO-M19-A05-IP-002
    claim: "Polarização induzida é especialmente sensível a minerais metálicos disseminados (não apenas maciços), por efeito capacitivo em grãos individuais."
    risk: mecanismo
    source: "SEG Wiki, Induced polarization"
  - claim_id: GEO-M19-A05-GRADIENTE-003
    claim: "Gradiente geotérmico médio continental é da ordem de 25-30 °C/km, variando amplamente por contexto tectônico (mais alto em rifts e vulcanismo ativo, mais baixo em crátons)."
    risk: numerico
    source: "USGS, Geothermal gradients in the conterminous United States"
-->
