# Aula 05: Krigagem simples e ordinária

**ID:** geologia-avancado-m20-a05
**Módulo:** [[20-geoestatistica-modulo|Módulo 20 — Introdução à geoestatística]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** mostrar como o modelo de variograma ajustado na Aula 04 alimenta um sistema de equações lineares — a krigagem — que pondera as amostras vizinhas para estimar o valor de um ponto ou bloco não amostrado, distinguindo krigagem simples de krigagem ordinária, krigagem de ponto de krigagem de bloco, e validando a estimativa resultante por validação cruzada.
**Ao final você vai conseguir:** explicar por que a krigagem é chamada de "melhor estimador linear não-viesado" e o que essa propriedade garante (e não garante); montar e resolver o sistema de equações de krigagem ordinária para um pequeno conjunto de amostras; explicar o papel da vizinhança de busca e da diferença entre krigagem de ponto e de bloco; e interpretar os resultados de uma validação cruzada.
**Pré-requisito:** [[20-geoestatistica-aula-04-variografia-variogramas|Aula 04 — O variograma: cálculo experimental e modelagem teórica]] (o modelo de variograma ajustado ali — efeito pepita, patamar, alcance — é o insumo direto do sistema de krigagem desta aula).

## Conteúdo

### Por que a krigagem é o "melhor estimador linear não-viesado"

Depois de quatro aulas preparando o terreno — dados compostos e descritos (Aula 01), o fenômeno formalizado como variável regionalizada sob a hipótese intrínseca (Aula 02), o efeito de suporte e a anisotropia (Aula 03), e a continuidade espacial quantificada num modelo de variograma (Aula 04) — a krigagem é o passo que efetivamente responde à pergunta original do módulo: qual é o valor esperado de um ponto ou bloco que não foi amostrado?

A krigagem estima esse valor como uma **combinação linear ponderada** das amostras vizinhas:

$$z^*(x_0) = \sum_{i=1}^n \lambda_i \, z(x_i)$$

onde $z^*(x_0)$ é o valor estimado no local $x_0$, $z(x_i)$ são os valores observados nas $n$ amostras da vizinhança, e $\lambda_i$ são os **pesos de krigagem** — o que precisa ser calculado. A ideia de ponderar amostras vizinhas por si só não é nova (a média móvel e o inverso do quadrado da distância fazem o mesmo tipo de combinação); o que torna a krigagem diferente é **como** os pesos são escolhidos: não por uma regra geométrica arbitrária (como "peso inversamente proporcional à distância"), mas resolvendo um sistema de equações que usa o **modelo de variograma** — ou seja, a estrutura de continuidade espacial real do fenômeno, calibrada nos dados — para encontrar os pesos que (1) tornam o erro de estimativa, em média, igual a zero (**não-viés**) e (2) minimizam a variância desse erro entre todos os estimadores lineares possíveis que satisfazem a condição (1). É por isso que a krigagem é descrita como o **melhor estimador linear não-viesado** (*Best Linear Unbiased Estimator*, BLUE): "melhor" no sentido estrito de variância mínima do erro, dentro da classe dos estimadores lineares não-viesados — não uma garantia de que o valor estimado seja necessariamente próximo do valor real em cada caso individual, mas de que, em média, sobre muitas estimativas, o método não erra sistematicamente para cima nem para baixo, e erra o menos possível em variância.

### Krigagem simples: quando a média é conhecida

A forma mais simples do sistema de krigagem assume que a **média da variável regionalizada, $m$, é conhecida e constante** em toda a área de trabalho — uma forma de estacionariedade de segunda ordem completa. Sob essa hipótese, a **krigagem simples (KS)** estima o desvio em relação à média, ponderando os desvios das amostras:

$$z^*_{KS}(x_0) = m + \sum_{i=1}^n \lambda_i \, [z(x_i) - m]$$

Os pesos $\lambda_i$ são obtidos resolvendo um sistema de $n$ equações lineares que usa diretamente a **função de covariância** $C(h)$ (relacionada ao variograma por $C(h) = C(0) - \gamma(h)$, sob estacionariedade de segunda ordem, onde $C(0)$ é a variância a priori/patamar total):

$$\sum_{j=1}^n \lambda_j \, C(x_i,x_j) = C(x_i,x_0) \quad \text{para cada } i=1,\dots,n$$

Não há restrição sobre a soma dos pesos. Isso significa que, quando as amostras vizinhas estão distantes (fora ou perto do limite do alcance do variograma), os pesos podem somar bem menos do que 1 — nesse caso, a krigagem simples "puxa" a estimativa de volta em direção à média global conhecida $m$, o que é matematicamente correto se $m$ de fato representa bem aquela região, mas é uma hipótese forte: exigir uma média global única e constante é raramente realista em depósitos minerais reais, onde diferentes domínios geológicos (zonas de alteração, litologias distintas) costumam ter médias locais diferentes.

### Krigagem ordinária: relaxando a exigência de uma média conhecida

A **krigagem ordinária (KO)** é a forma mais usada na prática de recursos minerais precisamente porque relaxa essa exigência: em vez de assumir uma média global constante e conhecida, ela assume apenas que a média é constante **dentro de cada vizinhança local** de estimativa, mas não exige conhecer o seu valor — a própria vizinhança de amostras "estima" a média localmente, de forma implícita. Isso se traduz numa restrição adicional sobre os pesos: eles precisam somar exatamente 1,

$$\sum_{i=1}^n \lambda_i = 1$$

o que faz com que $z^*_{KO}(x_0) = \sum \lambda_i z(x_i)$ seja sempre uma média ponderada legítima dos valores observados (sem termo de correção em relação a uma média externa). Essa restrição é incorporada ao sistema de equações por meio de um **multiplicador de Lagrange** $\mu$, resultando no **sistema de krigagem ordinária**:

$$\sum_{j=1}^n \lambda_j \, \gamma(x_i,x_j) + \mu = \gamma(x_i,x_0) \quad \text{para cada } i=1,\dots,n$$
$$\sum_{i=1}^n \lambda_i = 1$$

(o sistema pode ser escrito de forma equivalente em termos de covariância $C(h)$ em vez de variograma $\gamma(h)$; a versão em variograma é mais direta porque funciona também sob a hipótese intrínseca, sem exigir que a covariância esteja bem definida — ver Aula 02). O multiplicador de Lagrange $\mu$ não tem interpretação física direta em si, mas entra no cálculo da **variância de krigagem** — a medida de incerteza associada à estimativa, que a krigagem ordinária calcula automaticamente como subproduto do próprio sistema:

$$\sigma^2_{KO} = \sum_{i=1}^n \lambda_i \, \gamma(x_i,x_0) + \mu$$

Uma propriedade prática importante: a variância de krigagem depende inteiramente da **geometria** da configuração de amostras (suas posições relativas ao ponto estimado e entre si) e do modelo de variograma — não depende dos valores $z(x_i)$ observados. Isso significa que a variância de krigagem pode ser calculada e mapeada antes mesmo de se conhecer os teores, servindo como guia de planejamento de malha de sondagem adicional: áreas de alta variância de krigagem são áreas mal amostradas relativas ao alcance do variograma, onde furos adicionais reduzem mais a incerteza.

### Vizinhança de busca

Nenhuma estimativa de krigagem usa, na prática, **todas** as amostras do banco de dados — o custo computacional cresceria proibitivamente, e amostras muito distantes (além do alcance do variograma) não carregam informação espacial útil sobre o ponto (Aula 04). Em vez disso, define-se uma **vizinhança de busca**: uma região ao redor do ponto ou bloco a estimar. Ela é definida por três parâmetros, e vale tomá-los um a um, porque cada um responde a um problema diferente:

**1. O raio — quão longe buscar.** É ancorado no alcance do variograma, mas atenção ao sentido do ajuste: a prática usual **não** é encurtá-lo. O padrão é um raio **igual ao alcance ou maior**, e é comum estendê-lo a 1,5–2 vezes o alcance quando a malha é esparsa e o mínimo de amostras não seria atingido de outro modo. A razão é específica da krigagem ordinária: amostras além do alcance não informam mais sobre a estrutura, mas ainda ajudam a estimar implicitamente a média local — que é justamente o que a KO faz de diferente da KS. Em depósitos com malha irregular usa-se frequentemente uma **busca em múltiplas passadas**, com raio crescente a cada passada, para que os blocos bem informados sejam estimados com a vizinhança apertada e os mal informados ainda recebam estimativa.

**2. O número mínimo e máximo de amostras — quanta informação aceitar.** O **mínimo** evita estimativas construídas sobre pouquíssima informação, que ficam erráticas e sem controle local. Repare no que **não** é o motivo: o sistema em si é solúvel mesmo com uma única amostra, porque a restrição $\sum\lambda_i=1$ força $\lambda_1=1$. A instabilidade numérica de verdade vem de outro lugar — de a vizinhança conter amostras muito próximas entre si ou coincidentes, que tornam a matriz do sistema quase singular. O **máximo** mantém o sistema de equações de tamanho manejável e limita a inclusão de amostras redundantes.

**3. A setorização — de onde buscar.** É comum dividir a vizinhança em **octantes ou setores** (tipicamente quatro ou oito), exigindo um número mínimo de amostras por setor. Isso evita que a estimativa seja dominada por um agrupamento denso de amostras concentradas numa única direção, deixando outras direções sem representação — um problema comum em malhas de sondagem irregulares.

Os três parâmetros interagem, e o dimensionamento conjunto deles é hoje feito de forma quantitativa, por um conjunto de métricas conhecido como **análise quantitativa de vizinhança de krigagem** (QKNA), que mede, bloco a bloco, o quanto uma dada configuração de busca degrada a estimativa.

### Krigagem de ponto e krigagem de bloco

Tudo o que foi descrito até aqui é a **krigagem de ponto**: estimar o valor da variável regionalizada num ponto específico $x_0$, usando o valor do variograma $\gamma(x_i,x_0)$ entre cada amostra e esse ponto exato. A **krigagem de bloco** substitui o ponto $x_0$ por um volume $v$ (por exemplo, um bloco de $10\times10\times10$ m do modelo de blocos de lavra), e o lado direito do sistema de equações passa a usar a **covariância (ou variograma) médio entre cada amostra e todo o volume do bloco**, $\bar\gamma(x_i,v)$, em vez do valor pontual — na prática, aproximado numericamente pela média do variograma calculado entre a amostra e um conjunto de pontos de discretização distribuídos dentro do bloco.

O resultado direto disso é a manifestação, dentro da própria krigagem, do efeito de suporte já visto na Aula 03: a krigagem de bloco produz estimativas com variância **menor** do que a krigagem de ponto — o mesmo fenômeno de suavização por aumento de suporte, agora operacionalizado dentro do algoritmo de estimativa, e consistente com a relação de Krige. É por isso que a krigagem de bloco, não a krigagem de ponto seguida de médias simples, é o procedimento correto para popular um modelo de blocos de recursos minerais.

### Validação cruzada: a estimativa está calibrada?

Antes de aceitar um modelo de variograma e uma configuração de vizinhança como definitivos, a prática padrão é validá-los por **validação cruzada** (*cross-validation*), tipicamente no formato *leave-one-out*: remove-se temporariamente uma amostra do conjunto de dados, estima-se o seu valor por krigagem usando apenas as amostras vizinhas restantes, e compara-se o valor estimado com o valor real (que foi removido, mas é conhecido). Repetindo esse procedimento para cada amostra do conjunto, uma de cada vez, obtém-se uma coleção de erros de estimativa que pode ser resumida estatisticamente:

- **Erro médio** ($\overline{z^*-z}$) deve ser próximo de zero — um erro médio sistematicamente positivo ou negativo indica viés no modelo (por exemplo, um variograma ou vizinhança mal ajustados que sobre ou subestimam consistentemente).
- **Erro padronizado** (erro dividido pela raiz da variância de krigagem naquele ponto) deve ter variância próxima de 1 — se a variância dos erros padronizados for muito maior que 1, a variância de krigagem está subestimando a incerteza real (excesso de confiança); se for muito menor que 1, está superestimando (confiança excessivamente conservadora).

A validação cruzada não prova que o modelo está correto — apenas que ele é internamente consistente e não visivelmente enviesado sobre os próprios dados usados para ajustá-lo — mas é a checagem mínima esperada antes de qualquer modelo de blocos entrar em uso para planejamento de lavra ou relatório de recursos.

## Exemplo trabalhado

**Situação:** duas amostras de cobre (Cu, %) estão disponíveis na vizinhança de um ponto de estimativa $x_0$: a amostra 1, com teor $z_1=2,0\%$, está a $h_1=30$ m de $x_0$; a amostra 2, com teor $z_2=1,4\%$, está a $h_2=60$ m de $x_0$; e a distância entre as duas amostras é $h_{12}=40$ m. O modelo de variograma esférico ajustado (Aula 04) tem patamar $C_0+C_1=1,0$ (%)², efeito pepita nulo, e alcance $a=100$ m, o que dá os seguintes valores do próprio variograma $\gamma(h)$ para essas três distâncias: $\gamma(30)=0,437$; $\gamma(60)=0,792$; $\gamma(40)=0,568$; e $\gamma(0)=0$ (por definição).

**Pergunta:** monte e resolva o sistema de krigagem ordinária para obter os pesos $\lambda_1$, $\lambda_2$ e o valor estimado $z^*(x_0)$; calcule a variância de krigagem.

**Resolução:**

Usando a forma do sistema de krigagem ordinária em variograma apresentada na seção teórica acima ($\sum_j \lambda_j\gamma(x_i,x_j)+\mu=\gamma(x_i,x_0)$, com $\gamma(0)=0$ para o termo de cada amostra consigo mesma):

$$0\,\lambda_1 + 0,568\,\lambda_2 + \mu = 0,437$$
$$0,568\,\lambda_1 + 0\,\lambda_2 + \mu = 0,792$$
$$\lambda_1+\lambda_2=1$$

Subtraindo a primeira equação da segunda, o termo $\mu$ se cancela:

$$0,568\,\lambda_1 - 0,568\,\lambda_2 = 0,355 \implies \lambda_1-\lambda_2 \approx 0,625$$

Combinando com $\lambda_1+\lambda_2=1$: $\lambda_1 = 0,8125$ e $\lambda_2 = 0,1875$ (valores exatos, que arredondados para três casas dariam 0,813 e 0,188 — daqui em diante usamos os exatos, para que a soma continue valendo 1).

Substituindo na primeira equação: $0,568(0,1875)+\mu=0,437 \Rightarrow 0,1065+\mu=0,437 \Rightarrow \mu\approx0,330$.

**Estimativa:** $z^*(x_0) = 0,8125 \times 2,0 + 0,1875 \times 1,4 = 1,625 + 0,263 = 1,89\%$.

**Variância de krigagem:** $\sigma^2_{KO} = \lambda_1\gamma(30)+\lambda_2\gamma(60)+\mu = 0,8125(0,437)+0,1875(0,792)+0,330 \approx 0,355+0,149+0,330 = 0,833$ (%)².

**Leitura dos resultados:** a amostra 1, mais próxima ($h_1=30$ m), recebe um peso mais de quatro vezes maior ($\lambda_1=0,8125$) do que a amostra 2, mais distante ($\lambda_2=0,1875$) — o sistema de krigagem reflete diretamente a perda de continuidade espacial com a distância, exatamente como capturada pelo modelo de variograma. Note que os pesos somam exatamente 1 (a restrição da krigagem ordinária), e que a estimativa (1,89%) fica mais próxima do valor da amostra mais próxima e mais influente (2,0%) do que da mais distante (1,4%) — um comportamento qualitativamente parecido com o de um inverso da distância, mas aqui derivado formalmente da estrutura de continuidade medida pelo variograma, não de uma regra geométrica arbitrária, e acompanhado de uma medida de incerteza (a variância de krigagem) que o inverso da distância não fornece.

## Recap relâmpago

- A krigagem estima um valor não amostrado como **combinação linear ponderada** das amostras vizinhas, com pesos calculados a partir do modelo de variograma para garantir **não-viés** e **variância mínima do erro** — por isso é chamada de melhor estimador linear não-viesado (**BLUE**).
- **Krigagem simples (KS)** assume média global $m$ conhecida e constante, sem restrição sobre a soma dos pesos; **krigagem ordinária (KO)** assume apenas média local constante (desconhecida), com a restrição $\sum\lambda_i=1$ incorporada por um multiplicador de Lagrange — é a forma mais usada na prática de recursos minerais.
- A **vizinhança de busca** (raio ancorado no alcance do variograma — na prática **igual ao alcance ou maior**, por vezes 1,5–2 vezes, e frequentemente em múltiplas passadas —, número mínimo/máximo de amostras, divisão em setores/octantes) limita quais amostras entram no sistema de cada estimativa.
- **Krigagem de bloco** substitui o valor pontual por um volume, produzindo estimativas com variância menor que a krigagem de ponto (manifestação do efeito de suporte da Aula 03) — é o procedimento correto para popular um modelo de blocos.
- **Validação cruzada** (*leave-one-out*) checa se o modelo de variograma e a vizinhança estão calibrados: erro médio próximo de zero (sem viés) e variância do erro padronizado próxima de 1 (variância de krigagem nem excessiva nem insuficiente).

## Anterior

[[20-geoestatistica-aula-04-variografia-variogramas|Aula 04 — O variograma: cálculo experimental e modelagem teórica]].

Esta é a **última aula do Módulo 20** — o módulo fecha aqui por desenho, fechando o arco que abriu na Aula 01: dos dados brutos de furo à estimativa validada de um bloco não amostrado. O passo seguinte, a modelagem geoestatística completa de um depósito (simulação condicional, geoestatística não linear, estimativa de recursos recuperáveis), é o [[21-modelagem-geoestatistica-depositos-minerais/21-modelagem-geoestatistica-depositos-minerais-modulo|Módulo 21]]. Para voltar ao índice do módulo: [[20-geoestatistica-modulo|Módulo 20 — Introdução à geoestatística]].

## Fontes

- Isaaks, E. H. & Srivastava, R. M. (1989), *An Introduction to Applied Geostatistics*, Oxford University Press, capítulo 12 (krigagem ordinária: formulação do sistema, multiplicador de Lagrange, variância de krigagem; krigagem simples como o caso de média conhecida), capítulo 13 (krigagem de bloco e discretização), capítulo 14 (estratégia de busca: raio, número de amostras, setores) e capítulo 15 (validação cruzada).
- Journel, A. G. & Huijbregts, C. J. (1978), *Mining Geostatistics*, Academic Press, capítulo V (derivação formal do sistema de krigagem ordinária com multiplicador de Lagrange e propriedade BLUE).
- Goovaerts, P. (1997), *Geostatistics for Natural Resources Evaluation*, Oxford University Press, capítulo 4 (inferência e modelagem) e capítulo 5 (estimativa local com um único atributo: krigagem simples versus ordinária, vizinhança de busca, validação cruzada).
- Deutsch, J. L. & Deutsch, C. V., "Quantitative Kriging Neighborhood Analysis (QKNA)" e "Introduction to Choosing a Kriging Plan", *Geostatistics Lessons* (geostatisticslessons.com) — critérios quantitativos para dimensionar raio de busca e número de amostras (eficiência de krigagem, inclinação da regressão, peso da média na krigagem simples).

<!--
nivel: avancado
palavras_corpo: 2480
mapa_objetivo_secao:
  geologia-avancado-m20-oa04: "Por que a krigagem é o 'melhor estimador linear não-viesado'" + "Krigagem simples: quando a média é conhecida" + "Krigagem ordinária: relaxando a exigência de uma média conhecida" + "Vizinhança de busca" + "Krigagem de ponto e krigagem de bloco" + "Validação cruzada: a estimativa está calibrada?" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOEST-M20-A04-BLUE-001
    claim: "A krigagem estima o valor de um ponto ou bloco não amostrado como combinação linear ponderada das amostras vizinhas, com os pesos calculados resolvendo um sistema de equações baseado no modelo de variograma/covariância, de modo a garantir não-viés (erro médio zero) e variância mínima do erro entre todos os estimadores lineares não-viesados possíveis — propriedade que lhe vale o nome de 'melhor estimador linear não-viesado' (Best Linear Unbiased Estimator, BLUE)."
    risk: fato
    source: "Journel & Huijbregts (1978), Mining Geostatistics, Academic Press, capítulo V (derivação da propriedade BLUE da krigagem); Isaaks & Srivastava (1989), An Introduction to Applied Geostatistics, capítulo 12."
  - claim_id: GEOEST-M20-A04-KSKO-002
    claim: "A krigagem simples (KS) assume que a média m da variável regionalizada é conhecida e constante em toda a área, resolvendo um sistema de equações em covariância sem restrição sobre a soma dos pesos; a krigagem ordinária (KO) assume apenas que a média é constante dentro de cada vizinhança local (sem exigir conhecer seu valor), incorporando a restrição soma dos pesos = 1 por meio de um multiplicador de Lagrange no sistema de equações — a krigagem ordinária é a forma mais usada na prática de recursos minerais por não exigir uma média global conhecida."
    risk: fato
    source: "Isaaks & Srivastava (1989), An Introduction to Applied Geostatistics, capítulo 12 (krigagem ordinária: sistema, multiplicador de Lagrange, variância de krigagem; a krigagem simples é apresentada ali como o caso de média conhecida); Journel & Huijbregts (1978), capítulo V; Goovaerts (1997), Geostatistics for Natural Resources Evaluation, capítulo 5 (estimativa local com um único atributo: krigagem simples, ordinária e com modelo de tendência). A preferência da indústria de recursos minerais pela krigagem ordinária é observação consolidada na literatura aplicada, e decorre de ela realizar, na prática, a hipótese de quase-estacionariedade em vizinhança móvel (ver Aula 02)."
  - claim_id: GEOEST-M20-A04-VARIANCIAKRIGAGEM-003
    claim: "A variância de krigagem depende exclusivamente da geometria da configuração de amostras (posições relativas ao ponto/bloco estimado e entre si) e do modelo de variograma, não dos valores observados nas amostras — podendo, portanto, ser calculada e mapeada antes de se conhecerem os teores, e usada como guia de planejamento de malha de sondagem adicional (áreas de maior variância de krigagem indicam maior benefício de amostragem adicional relativa ao alcance do variograma)."
    risk: fato
    source: "Isaaks & Srivastava (1989), An Introduction to Applied Geostatistics, capítulo 12 (propriedade da variância de krigagem independente dos valores de dados); Journel & Huijbregts (1978), capítulo V. Uso da variância de krigagem para planejamento de malha é prática aplicada consolidada (ver Goovaerts 1997, capítulo 5)."
  - claim_id: GEOEST-M20-A04-KRIGBLOCOEFEITOSUPORTE-004
    claim: "A krigagem de bloco substitui o valor pontual no lado direito do sistema de krigagem pela covariância (ou variograma) médio entre cada amostra e todo o volume do bloco, aproximado numericamente pela média sobre pontos de discretização dentro do bloco; a estimativa resultante tem variância menor do que a krigagem de ponto, manifestando dentro do algoritmo de estimativa o mesmo efeito de suporte (relação de Krige) discutido para dados brutos na Aula 03 deste módulo, sendo o procedimento correto para popular um modelo de blocos de recursos minerais."
    risk: fato
    source: "Isaaks & Srivastava (1989), An Introduction to Applied Geostatistics, capítulo 13 (krigagem de bloco, discretização numérica, relação com efeito de suporte); Journel & Huijbregts (1978), capítulo V."
  - claim_id: GEOEST-M20-A04-VALIDACAOCRUZADA-005
    claim: "A validação cruzada leave-one-out remove cada amostra individualmente, estima seu valor por krigagem a partir das amostras vizinhas restantes, e compara com o valor real conhecido; um modelo bem calibrado apresenta erro médio próximo de zero (ausência de viés sistemático) e variância do erro padronizado (erro dividido pela raiz da variância de krigagem) próxima de 1 (nem subestimando nem superestimando a incerteza real) — a validação cruzada checa consistência interna do modelo, não garante que ele esteja cientificamente correto."
    risk: fato
    source: "Isaaks & Srivastava (1989), An Introduction to Applied Geostatistics, capítulo 15 (procedimento e critérios de interpretação da validação cruzada); Goovaerts (1997), Geostatistics for Natural Resources Evaluation, Oxford University Press, capítulo 5."
  - claim_id: GEOEST-M20-A04-RAIOBUSCA-006
    claim: "O raio da vizinhança de busca em krigagem é ancorado no alcance do variograma, e a prática consolidada é usá-lo IGUAL AO ALCANCE OU MAIOR — frequentemente 1,5 a 2 vezes o alcance quando a malha é esparsa e o número mínimo de amostras não seria atingido de outro modo —, e não menor que o alcance; em malhas irregulares usa-se busca em múltiplas passadas com raio crescente. Na krigagem ordinária, amostras além do alcance ainda contribuem para a estimativa implícita da média local. O dimensionamento é hoje feito quantitativamente por Quantitative Kriging Neighborhood Analysis (QKNA)."
    risk: fato
    source: "Deutsch, J. L. & Deutsch, C. V., 'Quantitative Kriging Neighborhood Analysis (QKNA)' e 'Introduction to Choosing a Kriging Plan', Geostatistics Lessons (geostatisticslessons.com, consultado em 2026-09-18); Isaaks & Srivastava (1989), capítulo 14 (estratégia de busca). [claim registrado na auditoria de 2026-09-18 — a versão anterior da aula dizia 'frequentemente um valor entre metade e o alcance total', o que inverte a prática documentada]"
  - claim_id: GEOEST-M20-A04-ARREDONDAMENTOPESOS-007
    claim: "No exemplo trabalhado desta aula, os pesos exatos da krigagem ordinária são lambda1 = 0,8125 e lambda2 = 0,1875 (de lambda1-lambda2 = 0,355/0,568 = 0,625 com lambda1+lambda2 = 1); mu = 0,3305; z*(x0) = 1,8875% ~ 1,89%; sigma2_KO = 0,833 (%)². Os valores do modelo esférico C0=0, C=1,0, a=100 m conferem: gamma(30)=0,4365; gamma(40)=0,568; gamma(60)=0,792."
    risk: fato
    source: "Cálculo direto verificado na auditoria de 2026-09-18 a partir da fórmula do modelo esférico e do sistema de krigagem ordinária em variograma (Isaaks & Srivastava 1989, cap. 12; Journel & Huijbregts 1978, cap. V). A versão anterior apresentava lambda2 = 0,187, que não é o arredondamento correto de 0,1875 (0,188) — os valores exatos foram adotados para preservar a soma unitária."
  - claim_id: GEOEST-M20-A04-ESTABILIDADESISTEMA-008
    claim: "O sistema de krigagem ordinária NÃO fica indeterminado por haver poucas amostras na vizinhança: com uma única amostra a restrição soma dos pesos = 1 já determina lambda1 = 1, e o sistema é solúvel. O que justifica exigir um número mínimo de amostras é a qualidade da estimativa (estimativas erráticas e mal condicionadas, sem controle local) e não a solubilidade do sistema. A instabilidade numérica genuína surge quando a vizinhança contém amostras muito próximas entre si ou coincidentes, que tornam a matriz do sistema quase singular — e, no caso do modelo gaussiano, pelo comportamento parabólico na origem com efeito pepita nulo (Aula 04)."
    risk: fato
    source: "Isaaks & Srivastava (1989), An Introduction to Applied Geostatistics, capítulos 12 e 14; Deutsch, J. L. & Deutsch, C. V., 'Introduction to Choosing a Kriging Plan', Geostatistics Lessons (consultado em 2026-09-18). [claim registrado na auditoria de 2026-09-18 — a versão anterior da aula afirmava que o sistema se torna 'indeterminado' com poucas amostras]"
nota_claim_id_pre_renumeracao: 'Os oito claim_id desta aula conservam o prefixo A04, que designa a NUMERACAO PRE-DIVISAO em que foram emitidos (esta aula era a Aula 04 do modulo), e NAO a posicao atual. A manutencao e DELIBERADA: renumera-los quebraria a rastreabilidade com o manifesto 20-geoestatistica-auditoria.json, que os referencia como GEOEST-M20-A04-BLUE-001, -KSKO-002, -VARIANCIAKRIGAGEM-003, -KRIGBLOCOEFEITOSUPORTE-004, -VALIDACAOCRUZADA-005, -RAIOBUSCA-006, -ARREDONDAMENTOPESOS-007 e -ESTABILIDADESISTEMA-008, todos com desfecho registrado. A regra do plugin e explicita: claim_id nao se recicla nem se renumera. O mesmo vale para os cinco claim_id da Aula 04 (prefixo A03) e para os dois da Aula 03 (prefixo A02).'
-->
