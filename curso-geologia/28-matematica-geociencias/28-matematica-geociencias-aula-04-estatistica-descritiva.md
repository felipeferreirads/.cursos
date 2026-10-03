# Aula 04: Estatística descritiva — média, dispersão, histograma e leitura de incerteza

**ID:** geologia-m28-a04
**Módulo:** [[28-matematica-geociencias-modulo|Módulo 28 — Matemática para geociências]]
**Duração estimada:** ~30 min
**Nível:** ensino médio completo, sem geologia prévia (contrato `ensino-medio-sem-geologia-v1`)
**Objetivo:** calcular e interpretar média, mediana, desvio-padrão e histograma de dados geológicos, e ler uma barra de erro.

> [!info] Esta aula formaliza uma leitura que o curso já pediu para fazer O [[27-fisica-geociencias-aula-01-grandezas-unidades-e-medida|Módulo 27, aula 01]] distinguiu **precisão** de **exatidão** e introduziu a ideia de incerteza de medida sem formalizar como calculá-la a partir de várias medidas. Esta aula fecha essa lacuna com as ferramentas de estatística descritiva — úteis tanto para um conjunto de idades radiométricas quanto para medidas repetidas de mergulho em campo.

## Antes de começar, você precisa saber

- **Precisão** e **exatidão** — [[27-fisica-geociencias-aula-01-grandezas-unidades-e-medida|Módulo 27, aula 01]] (recomendado).
- O que é **meia-vida** e por que uma idade radiométrica vem com incerteza — [[03-tempo-geologico-geocronologia-aula-04-meia-vida|Módulo 03, aula 04]] (recomendado).

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **Média** | A soma de todos os valores de um conjunto, dividida pela quantidade de valores — o "centro de massa" dos dados. |
| **Mediana** | O valor que fica exatamente no meio de um conjunto de dados ordenados do menor para o maior. |
| **Desvio-padrão** | Um número que mede o quanto os valores de um conjunto, em média, se afastam da média — quanto maior, mais espalhados os dados. |
| **Variância** | O desvio-padrão elevado ao quadrado; usado nos cálculos intermediários, raramente interpretado diretamente. |
| **Histograma** | Um gráfico de barras que mostra quantos valores de um conjunto caem em cada faixa (intervalo), revelando a forma da distribuição dos dados. |
| **Incerteza (±)** | A margem declarada em torno de um valor medido, que expressa o quanto ele pode variar por causa de limitações da medição. |

## Conteúdo

### Média e mediana: dois jeitos de achar o "centro" de um conjunto

Ao medir a mesma grandeza várias vezes — o mergulho de uma camada em cinco pontos de um afloramento, ou a idade de uma rocha por cinco análises independentes — os valores raramente saem idênticos. A **média** resume o conjunto somando todos os valores e dividindo pela quantidade deles; é a ferramenta mais comum, mas é sensível a valores muito fora do padrão (um único erro grosseiro de medição pode puxar a média inteira para um lado). A **mediana** — o valor central quando os dados são ordenados — é mais resistente a esse tipo de distorção: um valor absurdamente alto ou baixo muda pouco a posição do "meio" da fila, ainda que mude bastante a soma total usada na média.

> [!tip] Uma analogia Imagine cinco pessoas numa sala, com rendas de R$ 2 mil, 2,5 mil, 3 mil, 3,5 mil e 4 mil — a média e a mediana coincidem em R$ 3 mil. Agora troque a última pessoa por alguém com renda de R$ 1 milhão: a **mediana** continua em R$ 3 mil (ainda é o valor do meio), mas a **média** dispara para mais de R$ 200 mil — um número que não representa bem "a pessoa típica da sala". Esse é o motivo pelo qual estatísticas de renda costumam usar mediana, e por que vale sempre perguntar qual das duas está sendo reportada.

### Desvio-padrão: o quanto os dados se espalham

Duas amostras podem ter exatamente a mesma média e, ainda assim, contar histórias muito diferentes: uma com valores todos próximos da média, outra com valores espalhados para longe dela. O número que captura essa diferença é o **desvio-padrão**: em termos simples, a distância típica entre cada valor do conjunto e a média do conjunto. Um desvio-padrão pequeno significa dados concentrados (alta precisão, no vocabulário da aula 01 do Módulo 27); um desvio-padrão grande significa dados espalhados (baixa precisão).

O cálculo, passo a passo: para cada valor, calcula-se a diferença em relação à média, eleva-se essa diferença ao quadrado (para que valores acima e abaixo da média não se cancelem), faz-se a média dessas diferenças ao quadrado — esse resultado intermediário é a **variância** — e, por fim, tira-se a raiz quadrada da variância para voltar à unidade original da grandeza medida. É esse último número, já na mesma unidade dos dados originais (graus, Ma, metros), que é chamado de desvio-padrão.

### Histograma: enxergar a forma da distribuição

Uma lista de números é difícil de interpretar de relance; um **histograma** resolve isso agrupando os valores em faixas (por exemplo, "35°–37°", "37°–39°" para medidas de mergulho) e desenhando uma barra cuja altura mostra quantos valores caíram em cada faixa. O histograma revela de imediato o que a média e o desvio-padrão, sozinhos, escondem: se os dados se concentram num único pico central (o padrão mais comum, dito "em forma de sino"), se há dois grupos separados (o que pode indicar duas populações distintas — por exemplo, duas gerações de cristalização diferentes numa mesma rocha), ou se um valor isolado se destaca longe dos demais (candidato a erro de medição ou a um evento geológico genuinamente diferente).

### O que "±" significa quando um número vem com incerteza

Quando um laboratório reporta uma idade como "245 ± 3 Ma", o número depois do "±" não é um capricho — ele expressa a **incerteza** da medição, e tipicamente corresponde a um desvio-padrão (ou a um múltiplo dele, como duas vezes o desvio-padrão, convenção que varia por laboratório e deve constar do relatório). Isso significa que o valor real provavelmente está dentro dessa faixa, mas **não** com certeza absoluta — apenas com um nível de confiança declarado. Duas consequências práticas:

- **Comparar duas idades exige comparar as faixas, não só os números centrais.** Uma idade de 245 ± 3 Ma e outra de 249 ± 4 Ma têm faixas que se sobrepõem (242–248 e 245–253) — são estatisticamente **compatíveis**, mesmo os números centrais sendo diferentes. Já 245 ± 2 Ma contra 260 ± 2 Ma têm faixas que não se tocam — são **incompatíveis**, e a diferença provavelmente reflete algo geológico real, não apenas ruído de medição.
- **Uma incerteza pequena não garante um resultado correto.** Ela garante apenas **precisão** — resultados repetíveis e próximos entre si. Se houver um problema sistemático (por exemplo, perda de gás argônio numa datação K-Ar, contaminação da amostra), o resultado pode ser preciso e, ainda assim, **inexato** — exatamente a distinção entre precisão e exatidão já vista no Módulo 27.

## Exemplo trabalhado

**Situação:** cinco análises independentes da mesma amostra de rocha retornam as seguintes idades: 241 Ma, 244 Ma, 243 Ma, 258 Ma e 245 Ma.

**Passo 1 — calcular a média.** (241 + 244 + 243 + 258 + 245) / 5 = 1.231 / 5 = **246,2 Ma**.

**Passo 2 — calcular a mediana.** Ordenando: 241, 243, 244, 245, 258. O valor central é **244 Ma**.

**Passo 3 — comparar média e mediana.** A média (246,2 Ma) ficou puxada para cima em relação à mediana (244 Ma), por causa do valor de 258 Ma, visivelmente mais alto que os outros quatro — um sinal de alerta.

**Passo 4 — avaliar o valor discrepante.** Descartando 258 Ma como possível erro analítico (a decisão de descartar ou não exige critério estatístico e justificativa geológica, não é automática), a média dos quatro restantes fica: (241 + 244 + 243 + 245) / 4 = 973 / 4 = **243,25 Ma**, um valor bem mais coerente e próximo da mediana original.

**Passo 5 — interpretar o resultado final.** Reportar algo como "243 ± 2 Ma (n = 4, excluindo um valor discrepante)" é mais honesto do que reportar "246 Ma" sem qualquer menção à dispersão dos dados — o segundo número esconde exatamente a informação (o valor de 258 Ma destoando dos demais) que mais importa para avaliar a confiabilidade do resultado.

## Erros comuns

- **Reportar só a média, sem desvio-padrão nem tamanho da amostra.** Um único número esconde se os dados eram consistentes entre si (poucos valores, muito espalhados) ou robustos (muitos valores, bem concentrados).
- **Descartar um valor discrepante sem justificativa.** Um dado fora do padrão pode ser erro de medição — mas também pode ser sinal geológico real (por exemplo, um segundo evento de recristalização). Descartar automaticamente, sem investigar a causa, é tão errado quanto manter sem questionar.
- **Achar que duas médias diferentes significam, por si só, resultados incompatíveis.** É preciso comparar as faixas de incerteza, não só os números centrais — faixas que se sobrepõem indicam compatibilidade estatística, mesmo com médias diferentes.
- **Confundir desvio-padrão pequeno com resultado correto.** Desvio-padrão pequeno mede apenas **precisão** (repetibilidade); não garante **exatidão** (proximidade do valor verdadeiro) — um erro sistemático pode produzir medidas muito precisas e, ao mesmo tempo, erradas.

## O que não concluir

- **Que esta aula ensina testes de hipótese formais, intervalos de confiança com base em distribuições específicas, ou a regressão linear usada em diagramas isócronos de geocronologia.** Essas ferramentas mais avançadas de estatística inferencial ficam para um tratamento quantitativo mais completo, fora do escopo desta aula introdutória.
- **Que todo conjunto de dados geológicos segue uma distribuição "em forma de sino" (normal).** Muitos seguem, mas alguns (por exemplo, tamanho de partículas sedimentares, ou intervalos entre eventos sísmicos) seguem distribuições bem diferentes — reconhecer isso é parte de por que o histograma é examinado antes de aplicar qualquer fórmula.

## Recap relâmpago

- **Média** = soma dividida pela quantidade; sensível a valores extremos. **Mediana** = valor central; resistente a eles.
- **Desvio-padrão** mede o espalhamento típico dos dados em torno da média; pequeno = dados concentrados (alta precisão); grande = dados espalhados.
- **Histograma** revela a forma da distribuição — pico único, dois grupos, ou valor isolado destoante — informação que média e desvio-padrão sozinhos escondem.
- **"±"** expressa incerteza, tipicamente ligada ao desvio-padrão; comparar dois resultados exige comparar as **faixas**, não só os números centrais.
- Incerteza pequena garante **precisão**, não **exatidão** — as duas seguem independentes, como já visto no Módulo 27.

## Próxima aula

Nenhuma — última aula do módulo. Ver [[28-matematica-geociencias-modulo|Módulo 28]] para o questionário final.

## Anterior

[[28-matematica-geociencias-aula-03-exponenciais-e-logaritmos|Aula 03 — Exponenciais e logaritmos]]

## Fontes

- Média, mediana, desvio-padrão, variância e histograma: estatística descritiva elementar (conteúdo padrão de ensino médio/introdutório).
- Interpretação de incerteza (±) em datação radiométrica e comparação de faixas de idade: Faure & Mensing (2005), *Isotopes: Principles and Applications*, 3ª ed., Wiley, capítulo sobre tratamento de erros; Dickin, A. P. (2005), *Radiogenic Isotope Geology*, 2ª ed., Cambridge University Press, capítulo introdutório sobre incerteza analítica.
- Distinção entre precisão e exatidão: retomada de [[27-fisica-geociencias-aula-01-grandezas-unidades-e-medida|Módulo 27, aula 01]].

<!--
nivel: ensino-medio-sem-geologia-v1
palavras_corpo: ~1440
bridge_lesson: true

mapa_objetivo_secao:
  OA-04: "Média e mediana: dois jeitos de achar o centro de um conjunto" + "Desvio-padrão: o quanto os dados se espalham" + "Histograma: enxergar a forma da distribuição" + "O que ± significa quando um número vem com incerteza" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEO-M28-A04-MEDIA-MEDIANA-001
    claim: "A média é a soma dos valores de um conjunto dividida pela quantidade de valores e é sensível a valores extremos (outliers); a mediana é o valor central de um conjunto ordenado e é mais resistente a esses valores."
    risk: fato
    source: "estatística descritiva elementar"
  - claim_id: GEO-M28-A04-DESVIO-PADRAO-002
    claim: "O desvio-padrão é calculado como a raiz quadrada da média dos quadrados dos desvios de cada valor em relação à média do conjunto (variância), expressando o espalhamento típico dos dados na mesma unidade da grandeza original."
    risk: fato
    source: "estatística descritiva elementar"
  - claim_id: GEO-M28-A04-INCERTEZA-DESVIO-003
    claim: "A incerteza reportada como '±' em uma medição científica tipicamente corresponde ao desvio-padrão ou a um múltiplo declarado dele, e representa um intervalo de confiança, não uma garantia absoluta do valor verdadeiro."
    risk: interpretacao
    source: "prática padrão de reporte de incerteza em ciências físicas; Faure & Mensing 2005, Isotopes: Principles and Applications, cap. sobre tratamento de erros"
  - claim_id: GEO-M28-A04-COMPARAR-FAIXAS-004
    claim: "Para avaliar se duas medições com incerteza são estatisticamente compatíveis, deve-se comparar as faixas definidas pelo valor central mais/menos a incerteza, e não apenas os valores centrais isoladamente."
    risk: interpretacao
    source: "princípio padrão de comparação de medidas com incerteza; Dickin 2005, Radiogenic Isotope Geology, cap. introdutório"
  - claim_id: GEO-M28-A04-PRECISAO-NAO-EXATIDAO-005
    claim: "Um desvio-padrão pequeno indica alta precisão (repetibilidade), mas não garante exatidão (proximidade do valor verdadeiro), já que erros sistemáticos podem produzir medições precisas e inexatas ao mesmo tempo."
    risk: interpretacao
    source: "retomada de 27-fisica-geociencias-aula-01-grandezas-unidades-e-medida; princípio consolidado de metrologia"

nota_trilha_apoio: >-
  Aula 4 de 4 do módulo 28 (trilha de apoio, opcional, não bloqueante), criada em
  2026-08-19. Formaliza o cálculo de incerteza a partir de medidas repetidas, que
  27-fisica-geociencias-aula-01 introduziu conceitualmente (precisão vs. exatidão)
  sem entrar em cálculo estatístico. Última aula do módulo 28 e da trilha de apoio
  inteira (27+28+29).
-->
