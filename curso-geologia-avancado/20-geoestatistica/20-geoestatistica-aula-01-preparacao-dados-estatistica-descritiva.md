# Aula 01: Preparação de dados e estatística descritiva para geoestatística

**ID:** geologia-avancado-m20-a01
**Módulo:** [[20-geoestatistica-modulo|Módulo 20 — Introdução à geoestatística]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** preparar um conjunto de dados de furos de sondagem para tratamento geoestatístico — compondo amostras de comprimento variável em intervalos regulares (compositing) — e descrever esse conjunto com as ferramentas da estatística clássica (medidas de tendência central e dispersão, forma da distribuição, correlação e regressão), estabelecendo a base sobre a qual toda a geoestatística das aulas seguintes é construída.
**Ao final você vai conseguir:** compor (compositar) amostras de sondagem de comprimentos desiguais em um comprimento de suporte fixo; calcular e interpretar média, variância, desvio padrão, coeficiente de variação e assimetria de um conjunto de teores; reconhecer, em um histograma, os sinais de uma distribuição lognormal e o efeito de valores extremos sobre a média; e calcular um coeficiente de correlação e uma reta de regressão linear simples entre dois elementos, sabendo o que essa correlação NÃO prova.
**Pré-requisito:** [[13-geoprocessamento/13-geoprocessamento-modulo|Módulo 13 — Geoprocessamento]] (a lógica de dado espacial georreferenciado, tabelas de atributos e junção espacial usada aqui para organizar furos, amostras e composições).

## Conteúdo

### Por que a geoestatística começa em estatística "comum"

A pergunta que a geoestatística resolve — quanto teor existe num bloco de rocha que ninguém amostrou diretamente — parece, à primeira vista, um problema puramente espacial. Mas antes de qualquer coordenada entrar em cena, o conjunto de dados de amostras precisa passar pelo mesmo escrutínio que qualquer conjunto de dados numérico exigiria: qual é a forma da distribuição, existem valores anômalos, as amostras são comparáveis entre si. Ignorar essa etapa e ir direto ao variograma (Aula 04) é o erro mais comum de quem aprende geoestatística: um variograma calculado sobre amostras de comprimentos desiguais, ou dominado por dois ou três valores extremos não tratados, produz um modelo de continuidade espacial que não reflete o depósito — reflete um artefato de amostragem.

Este módulo trabalha o caso canônico da geoestatística de recursos minerais: teores medidos ao longo de furos de sondagem (testemunhos ou amostras de calha), que precisam alimentar uma estimativa de teor em blocos de um modelo de bloco 3D. As duas primeiras tarefas — compositar e descrever — são o objeto desta aula.

### Compositing: por que amostras de comprimento variável não podem ser comparadas diretamente

Um furo de sondagem raramente é amostrado em intervalos de comprimento constante. O geólogo de campo divide o testemunho em intervalos que respeitam os contatos litológicos e as zonas de alteração — um intervalo pode ter 0,3 m, o seguinte 2,1 m — porque o critério de amostragem é geológico, não estatístico. O problema é que uma média aritmética simples desses teores trataria um intervalo de 0,3 m e um de 2,1 m com o mesmo peso, quando o intervalo mais longo representa sete vezes mais rocha.

A solução padrão da indústria é o **compositing**: recombinar as amostras de comprimento variável em intervalos de comprimento fixo — chamados de **composições** ou, no jargão de mina a céu aberto, **composições por bancada** (*bench compositing*, quando o comprimento escolhido coincide com a altura de bancada da lavra, tipicamente 5 a 15 m) — usando uma **média ponderada pelo comprimento** de cada amostra original que cai dentro do intervalo de composição:

$$z_{comp} = \frac{\sum_i z_i \cdot l_i}{\sum_i l_i}$$

onde $z_i$ é o teor da amostra original $i$ e $l_i$ é o seu comprimento dentro do intervalo de composição. Esse procedimento garante que cada composição representa aproximadamente o mesmo volume de rocha ao longo do furo, o que é uma condição necessária (embora não suficiente) para que a estatística descritiva e o variograma calculados a partir dela sejam comparáveis ponto a ponto. Compositar em um comprimento maior do que o das amostras originais sempre **reduz a variância** do conjunto — é a primeira manifestação prática do efeito de suporte, que a Aula 03 formaliza.

A escolha do comprimento de composição não é arbitrária: comprimentos curtos demais preservam ruído de amostragem; comprimentos longos demais diluem zonas mineralizadas estreitas contra material estéril adjacente, subestimando o teor de veios finos. A prática usual ancora o comprimento de composição na altura de bancada planejada da lavra (para depósitos a céu aberto) ou em um valor próximo ao comprimento amostral mais comum do banco de dados, evitando tanto a superamostragem de intervalos curtos quanto a diluição excessiva de intervalos longos.

### Estatística descritiva univariada: para onde e quão espalhado

Com as composições em mãos, a primeira pergunta é puramente estatística: como o teor se distribui, ignorando por enquanto onde cada amostra está no espaço. As medidas centrais de sempre continuam valendo, mas em teores de metais elas se comportam de um jeito característico:

- **Média** ($\bar{z} = \frac{1}{n}\sum z_i$) — o teor médio do conjunto amostrado. É a medida mais usada, mas também a mais vulnerável a poucos valores muito altos.
- **Mediana** — o valor central quando os dados são ordenados. Em distribuições assimétricas (a norma, não a exceção, em teores de metais preciosos e de base), a mediana fica sistematicamente abaixo da média, porque a média é "puxada" para cima por uma cauda de valores altos.
- **Variância** ($s^2 = \frac{1}{n-1}\sum (z_i-\bar{z})^2$) e **desvio padrão** ($s=\sqrt{s^2}$) — medem o espalhamento em torno da média, na mesma unidade do teor (o desvio padrão) ou ao quadrado (a variância). A variância é a peça central de toda a geoestatística: o variograma da Aula 04 é, essencialmente, uma forma de decompor a variância total em função da distância entre amostras.
- **Coeficiente de variação** ($CV = s/\bar{z}$) — o desvio padrão relativo à média, adimensional, o que permite comparar a dispersão de elementos com unidades e ordens de grandeza diferentes (por exemplo, Au em g/t versus Fe em %). Na prática de recursos minerais, um CV acima de aproximadamente 1 a 2 é tomado como sinal de alerta: costuma indicar uma distribuição fortemente assimétrica, dominada por poucos valores altos, na qual a média aritmética simples é um resumo estatístico frágil e a estimativa espacial exige cuidado adicional (capeamento de outliers, transformação de dados, ou métodos não lineares fora do escopo deste módulo).
- **Assimetria (skewness)** — mede a falta de simetria da distribuição. Um coeficiente de assimetria positivo e grande indica uma cauda longa de valores altos à direita — o padrão típico de depósitos de ouro, onde a maior parte das amostras tem teor baixo e uma minoria de amostras "de alto teor" concentra uma fração desproporcional do metal contido.

Essa combinação — assimetria positiva forte e CV alto — é tão recorrente em teores de metais preciosos que a prática consolidada é assumir, como hipótese de trabalho a testar, que a distribuição se aproxima de uma **lognormal**: o logaritmo do teor, não o teor em si, é que se distribui aproximadamente de forma simétrica (normal). Verificar essa hipótese — tipicamente com um histograma do teor transformado em log — orienta decisões práticas adiante, como qual estatística de tendência central é mais robusta e como tratar valores extremos.

### Histograma, boxplot e o problema dos valores extremos

O **histograma** é a ferramenta visual central desta etapa: agrupa os teores em classes (*bins*) e mostra a frequência de cada classe, revelando de imediato a forma da distribuição — simétrica, assimétrica, bimodal (sinal frequente de que o conjunto mistura duas populações geológicas distintas, por exemplo minério e estéril amostrados juntos — um problema de **estacionariedade**, o nome que a Aula 02 dará à suposição de que a variável se comporta estatisticamente da mesma forma em todo o domínio, suposição que duas populações misturadas quebram). O **boxplot** (ou diagrama de caixa) resume a mesma informação de forma compacta — mediana, quartis, amplitude interquartil e pontos além de um limiar convencional (tipicamente 1,5 vezes a amplitude interquartil) marcados individualmente como possíveis valores atípicos.

Esses valores atípicos (*outliers*) exigem uma distinção que a estatística sozinha não resolve: um teor extremamente alto pode ser um **erro** (contaminação de amostra, erro de laboratório, erro de digitação) ou pode ser uma **saca de alto teor genuína** — um intervalo de fato muito rico, que existe fisicamente na rocha. A prática de recursos minerais chama esse segundo caso de **valor extremo de alto teor (high-grade outlier)** — termo que não deve ser confundido com **teor de corte** (*cut-off grade*), o limiar econômico que separa minério de estéril, um conceito inteiramente distinto —, e o tratamento padrão não é excluir esses valores (o que subestimaria o metal contido), mas **capear** (*capping* ou *top-cutting*): substituir os valores acima de um limiar definido estatisticamente — por exemplo, o percentil 99 da distribuição, ou o ponto onde o histograma da distribuição cumulativa de metal contido muda de inclinação — pelo próprio valor do limiar, preservando a contagem de amostras mas limitando a influência desproporcional de poucos valores extremos sobre a média e, mais adiante, sobre o variograma e a krigagem. A decisão de capear, e em que valor, depende de julgamento geológico e estatístico combinado — não existe fórmula única — e por isso deve sempre ser documentada e justificada, nunca aplicada mecanicamente.

### Estatística bivariada: correlação e regressão — e o que elas não provam

Quando duas variáveis são medidas na mesma amostra — por exemplo, teores de ouro (Au) e prata (Ag) num depósito epitermal, ou cobre (Cu) e molibdênio (Mo) num pórfiro — a pergunta natural é se elas variam juntas. O **coeficiente de correlação de Pearson** mede a força e o sentido dessa relação linear:

$$r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i-\bar{x})^2 \sum(y_i-\bar{y})^2}}$$

com $r$ variando de $-1$ (correlação linear negativa perfeita) a $+1$ (correlação linear positiva perfeita), passando por $0$ (nenhuma correlação linear). A **regressão linear simples** vai um passo além: ajusta uma reta $y = a + bx$ que minimiza a soma dos quadrados dos resíduos, permitindo prever um valor de $y$ a partir de um valor conhecido de $x$ — útil, por exemplo, quando um elemento é caro de analisar e outro, correlacionado, é barato e amplamente disponível.

É essencial marcar aqui o limite conceitual desta ferramenta, porque o restante do módulo depende de não confundi-la com o que vem a seguir: a correlação de Pearson mede a relação entre **duas variáveis diferentes medidas no mesmo local** (por exemplo, Au e Ag na mesma amostra). Ela não diz nada sobre como **a mesma variável** se relaciona entre **locais diferentes** — essa é a pergunta da continuidade espacial, que a Aula 02 introduz como variável regionalizada e a Aula 04 quantifica com o variograma. Um conjunto de teores de Au pode ter zero relação espacial entre furos vizinhos (seria "ruído puro", geologicamente implausível mas estatisticamente possível) e ainda assim ter correlação alta com Ag amostrada nos mesmos pontos, ou vice-versa: são perguntas independentes, respondidas por ferramentas diferentes.

## Exemplo trabalhado

**Situação:** um furo de sondagem foi amostrado em seis intervalos de comprimento desigual, com teores de ouro (Au, g/t) e prata (Ag, g/t) analisados em cada intervalo:

| Amostra | Comprimento (m) | Au (g/t) | Ag (g/t) |
|---|---|---|---|
| 1 | 1,0 | 0,8 | 3 |
| 2 | 1,5 | 1,2 | 5 |
| 3 | 0,5 | 4,5 | 18 |
| 4 | 2,0 | 1,0 | 4 |
| 5 | 1,0 | 0,9 | 3,5 |
| 6 | 2,0 | 1,1 | 4,5 |

**Pergunta:** (a) compor esses seis intervalos em uma única composição representando o furo inteiro de 8,0 m; (b) calcular a média aritmética simples do Au (sem ponderar por comprimento) e comparar com a composição ponderada, explicando a diferença; (c) qual das duas médias de Au é a estimativa correta do teor médio ao longo do furo, e por quê.

**Resolução:**

**(a) Composição ponderada por comprimento.** O comprimento total do furo é $1,0+1,5+0,5+2,0+1,0+2,0 = 8,0$ m. A composição ponderada de Au é:

$$z_{comp,Au} = \frac{(0,8\times1,0)+(1,2\times1,5)+(4,5\times0,5)+(1,0\times2,0)+(0,9\times1,0)+(1,1\times2,0)}{8,0}$$

$$= \frac{0,8+1,8+2,25+2,0+0,9+2,2}{8,0} = \frac{9,95}{8,0} = 1,24 \text{ g/t}$$

**(b) Média aritmética simples (não ponderada) de Au:**

$$\bar{z}_{Au} = \frac{0,8+1,2+4,5+1,0+0,9+1,1}{6} = \frac{9,5}{6} = 1,58 \text{ g/t}$$

A média simples (1,58 g/t) é **cerca de 27% maior** do que a composição ponderada (1,24 g/t). A diferença vem inteiramente da amostra 3: um intervalo curto (0,5 m) mas de teor alto (4,5 g/t) recebe, na média simples, o mesmo peso que os intervalos de 2,0 m — isto é, 1/6 do total (16,7%), embora represente apenas $0,5/8,0 = 6,25\%$ da rocha amostrada, cerca de 2,7 vezes mais peso do que lhe caberia.

**(c) Qual é a estimativa correta.** A composição ponderada por comprimento (1,24 g/t) é a estimativa fisicamente correta do teor médio ao longo do furo, porque pondera cada teor pela quantidade de rocha que ele representa — exatamente o princípio de compositing desenvolvido acima. A média simples é **enviesada sempre que o comprimento da amostra se correlaciona com o teor**, e o sentido do viés acompanha o sinal dessa correlação: superestima quando as amostras curtas são as mais ricas, subestima quando são as mais pobres. Na prática de sondagem o primeiro caso é o mais frequente — o geólogo tende a isolar em intervalos curtos justamente as zonas estreitas de alto teor —, e por isso o viés observado costuma ser para cima, como neste exemplo; mas ele não aponta sistematicamente numa única direção. Em qualquer dos dois sentidos, esse viés se propagaria para qualquer estatística e qualquer variograma calculado a partir dela — é por isso que o compositing precede toda análise estatística e espacial subsequente, não é um refinamento opcional.

## Recap relâmpago

- **Compositing** transforma amostras de comprimento variável em intervalos de comprimento fixo por **média ponderada pelo comprimento**, condição necessária para que a estatística descritiva e o variograma sejam calculados sobre unidades comparáveis; ignorar essa etapa introduz viés sistemático, não apenas ruído.
- As medidas descritivas centrais (**média**, **mediana**) e de dispersão (**variância**, **desvio padrão**, **coeficiente de variação**) resumem a distribuição de teores; teores de metais, sobretudo preciosos, tendem a **assimetria positiva forte** e CV alto, aproximando-se de uma distribuição **lognormal**.
- **Histograma** e **boxplot** revelam a forma da distribuição e apontam **valores extremos**, que podem ser erro de amostra/laboratório ou saca de alto teor genuína; o tratamento padrão é o **capeamento (capping)** de um limiar estatisticamente definido, não a exclusão.
- **Correlação de Pearson** e **regressão linear** medem a relação entre **duas variáveis diferentes no mesmo local** — não dizem nada sobre a continuidade espacial da **mesma variável** entre locais diferentes, que é o objeto das próximas aulas. São perguntas **logicamente independentes**: uma não implica nem restringe a outra (o que não significa que, num depósito real, as duas estruturas não possam estar relacionadas — explorar essa relação é objeto da cokrigagem, fora do escopo deste módulo).

## Próxima aula

[[20-geoestatistica-aula-02-variaveis-regionalizadas-funcao-aleatoria-estacionariedade|Aula 02 — Variáveis regionalizadas, função aleatória e estacionariedade]] — como tratar um teor espacialmente distribuído como uma função aleatória, e as hipóteses de estacionariedade que tornam possível inferir estatística espacial a partir de uma única realização geológica. É a Parte 1 de um par: a Parte 2 (Aula 03) trata do efeito de suporte e da anisotropia.

## Fontes

- Isaaks, E. H. & Srivastava, R. M. (1989), *An Introduction to Applied Geostatistics*, Oxford University Press, capítulo 2 (descrição univariada: medidas de posição e dispersão, histograma, valores extremos) e capítulo 3 (descrição bivariada: correlação e regressão).
- Sinclair, A. J. & Blackwell, G. H. (2002), *Applied Mineral Inventory Estimation*, Cambridge University Press, capítulo 4 (conceitos estatísticos na estimativa de inventário mineral), capítulo 5 (dados e qualidade de dados, incluindo compositing de furos) e capítulo 7 (outliers e seu tratamento).
- Palmer, L. W. (2024), "Compositing and regularization of drillhole data for geostatistical resource estimation", *Journal of the Southern African Institute of Mining and Metallurgy*, 124(6), 331 (efeito do compositing sobre média e variância; viés da média não ponderada).
- Journel, A. G. & Huijbregts, C. J. (1978), *Mining Geostatistics*, Academic Press, capítulo II (fundamentos estatísticos e tratamento de distribuições assimétricas em teores).

<!--
nivel: avancado
palavras_corpo: 2300
mapa_objetivo_secao:
  geologia-avancado-m20-oa01: "Por que a geoestatística começa em estatística 'comum'" + "Compositing: por que amostras de comprimento variável não podem ser comparadas diretamente" + "Estatística descritiva univariada: para onde e quão espalhado" + "Histograma, boxplot e o problema dos valores extremos" + "Estatística bivariada: correlação e regressão — e o que elas não provam" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOEST-M20-A01-COMPOSITING-001
    claim: "O compositing (composição de amostras) recombina intervalos de amostragem de comprimento variável em intervalos de comprimento fixo por média ponderada pelo comprimento de cada amostra original, sendo condição necessária para que a estatística descritiva e o variograma sejam calculados sobre unidades comparáveis; compositar em comprimento maior que o das amostras originais reduz a variância do conjunto (primeira manifestação do efeito de suporte)."
    risk: fato
    source: "Sinclair & Blackwell (2002), Applied Mineral Inventory Estimation, Cambridge University Press, capítulo 5 (dados e qualidade de dados, compositing de furos); Palmer, L. W. (2024), 'Compositing and regularization of drillhole data for geostatistical resource estimation', J. South. Afr. Inst. Min. Metall., 124(6), 331. Prática padrão da indústria de estimativa de recursos minerais. [fonte revisada na auditoria de 2026-09-18 — a citação anterior a Isaaks & Srivastava cap. 4 estava incorreta: aquele capítulo trata de descrição espacial, não de compositing]"
  - claim_id: GEOEST-M20-A01-CVLIMIAR-002
    claim: "Um coeficiente de variação (CV = desvio padrão / média) acima de aproximadamente 1 a 2 é tomado, na prática de recursos minerais, como sinal de alerta de distribuição fortemente assimétrica dominada por poucos valores altos, exigindo cuidado adicional na estimativa espacial (capeamento de outliers, transformação de dados)."
    risk: aproximacao
    source: "Regra prática consolidada na literatura de geoestatística de recursos minerais (ver Isaaks & Srivastava 1989, cap. 2; Sinclair & Blackwell 2002, caps. 4 e 6). Apresentada como limiar orientativo da prática, não como norma estatística fixa — o valor exato varia por commodity e por depósito; em veios de ouro com forte efeito pepita a literatura documenta CV bem acima de 2."
  - claim_id: GEOEST-M20-A01-LOGNORMAL-003
    claim: "Teores de metais, sobretudo metais preciosos como ouro, tendem a apresentar distribuições com assimetria positiva forte, aproximando-se de uma distribuição lognormal, na qual o logaritmo do teor (não o teor bruto) se distribui aproximadamente de forma simétrica."
    risk: fato
    source: "Journel & Huijbregts (1978), Mining Geostatistics, Academic Press, capítulo II; Isaaks & Srivastava (1989), capítulo 2. Observação empírica amplamente documentada na literatura de avaliação de depósitos de metais preciosos."
  - claim_id: GEOEST-M20-A01-CAPPING-004
    claim: "O tratamento padrão para valores extremos genuínos (não erros de amostragem/laboratório) em teores de metais é o capeamento (capping/top-cutting) — substituir valores acima de um limiar estatisticamente definido (por exemplo, percentil 99, ou ponto de inflexão da curva de metal contido acumulado) pelo próprio valor do limiar, preservando a contagem de amostras mas limitando a influência desproporcional sobre média e variograma; a exclusão simples do valor não é a prática recomendada, pois subestima o metal contido. O termo correto em português é 'valor extremo de alto teor' — não 'valor de corte alto', que colide com teor de corte (cut-off grade), conceito econômico distinto."
    risk: aproximacao
    source: "Sinclair & Blackwell (2002), Applied Mineral Inventory Estimation, capítulo 7 (outliers e seu tratamento em avaliação de recursos). Apresentado como prática consolidada da indústria; o limiar de corte específico depende de julgamento geológico-estatístico caso a caso, não de fórmula única."
  - claim_id: GEOEST-M20-A01-CORRELACAOESPACIAL-005
    claim: "O coeficiente de correlação de Pearson e a regressão linear simples medem a relação entre duas variáveis diferentes medidas no mesmo local (por exemplo, Au e Ag na mesma amostra); essa medida é conceitualmente distinta da continuidade espacial de uma mesma variável entre locais diferentes, que é quantificada pelo variograma (Aula 04). As duas perguntas são logicamente independentes — uma não implica nem restringe a outra — o que NÃO equivale a independência estatística: num depósito real as duas estruturas podem estar relacionadas, e explorar essa relação é objeto da cokrigagem (fora do escopo deste módulo)."
    risk: fato
    source: "Distinção conceitual padrão da literatura de geoestatística, ver Isaaks & Srivastava (1989), capítulos 3 (descrição bivariada: correlação e regressão) e 7 (continuidade espacial amostral / variograma), e Journel & Huijbregts (1978), capítulo II."
  - claim_id: GEOEST-M20-A01-VIESMEDIASIMPLES-006
    claim: "A média aritmética simples de amostras de furo de comprimento variável é enviesada em relação à composição ponderada por comprimento sempre que o comprimento da amostra se correlaciona com o teor, e o SENTIDO do viés acompanha o sinal dessa correlação: superestima quando as amostras curtas são as mais ricas, subestima quando são as mais pobres. O viés para cima é o caso mais frequente na prática, porque o geólogo tende a isolar em intervalos curtos as zonas estreitas de alto teor — mas não é um viés sistemático numa única direção."
    risk: fato
    source: "Palmer, L. W. (2024), 'Compositing and regularization of drillhole data for geostatistical resource estimation', J. South. Afr. Inst. Min. Metall., 124(6), 331 (documenta que, entre furos, a média aritmética não ponderada ora fica acima, ora abaixo da composição ponderada). Sinclair & Blackwell (2002), capítulo 5."
  - claim_id: GEOEST-M20-A01-ARITMETICAEXEMPLO-007
    claim: "No exemplo trabalhado desta aula (6 intervalos, 8,0 m totais), a composição ponderada por comprimento de Au é 9,95/8,0 = 1,24 g/t e a média aritmética simples é 9,5/6 = 1,58 g/t; a média simples é cerca de 27% maior que a composição ponderada (1,5833/1,24375 = 1,273). A amostra 3 (0,5 m) recebe 1/6 = 16,7% do peso na média simples embora represente 0,5/8,0 = 6,25% da rocha amostrada — cerca de 2,7 vezes mais peso do que lhe caberia."
    risk: fato
    source: "Aritmética verificável a partir dos próprios dados da tabela do exemplo. Recalculada na auditoria de 2026-09-18; a versão anterior da aula afirmava '28% maior' e 'peso quatro vezes maior do que o comprimento de rocha que representa' (o fator 4 é a razão entre 2,0 m e 0,5 m, não a razão entre o peso recebido e o peso devido)."
-->
