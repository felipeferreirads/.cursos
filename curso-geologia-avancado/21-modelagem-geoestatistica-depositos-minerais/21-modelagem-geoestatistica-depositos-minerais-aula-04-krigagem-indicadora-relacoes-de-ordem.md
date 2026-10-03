# Aula 04: Krigagem indicadora: sistema, interpretação e violações de relação de ordem

**ID:** geologia-avancado-m21-a04
**Módulo:** [[21-modelagem-geoestatistica-depositos-minerais-modulo|Módulo 21 — Modelagem geoestatística de depósitos minerais]]
**Duração estimada:** ~17 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** resolver o sistema de krigagem indicadora, ler o resultado como uma probabilidade, montar a distribuição acumulada local a partir de vários limiares, e tratar o problema das violações de relação de ordem — incluindo a escolha, não consensual, entre krigagem indicadora ordinária e simples.
**Ao final você vai conseguir:** montar e resolver o sistema de krigagem indicadora para um pequeno conjunto de amostras e interpretar o resultado como probabilidade; explicar o *trade-off* de estacionariedade entre a krigagem indicadora ordinária (OIK) e a simples (SIK); e explicar o que é uma violação de relação de ordem, por que ela ocorre e como é corrigida.
**Pré-requisito:** Aula 03 deste módulo (variograma indicador modelado — esta aula parte de um variograma já ajustado) e Módulo 20, Aula 05 (sistema de krigagem ordinária — a forma do sistema de krigagem indicadora é idêntica).

> [!info] Esta é a **Parte 2 de um par**. A [[21-modelagem-geoestatistica-depositos-minerais-aula-03-variograma-indicador-modelos-autorizados|Aula 03]] tratou do **variograma** da indicadora — calcular, modelar e escolher a abordagem. Esta aula trata da **krigagem**: o sistema, a leitura do resultado e as relações de ordem.

## Conteúdo

### O sistema de krigagem indicadora

Uma vez definido o variograma indicador (por qualquer uma das duas abordagens) para um limiar $z_c$, o sistema de equações para estimar a indicadora num ponto (ou bloco) $x_0$ tem exatamente a mesma forma do sistema de krigagem ordinária do Módulo 20 (Aula 05) — a única mudança é que a variável de entrada é a indicadora, não o teor bruto:

$$\sum_{j=1}^n \lambda_j \, \gamma_I(x_i,x_j;z_c) + \mu = \gamma_I(x_i,x_0;z_c) \quad \text{para cada } i=1,\dots,n$$
$$\sum_{i=1}^n \lambda_i = 1$$

O resultado, $i^*(x_0;z_c) = \sum_i \lambda_i\, i(x_i;z_c)$, é uma **estimativa direta da probabilidade** de que o valor real em $x_0$ seja menor ou igual a $z_c$, condicionada à vizinhança de amostras usada — em outras palavras, $i^*(x_0;z_c) \approx F(z_c \mid \text{vizinhança})$, um ponto da função de distribuição acumulada local. Essa forma que usa a média local (com a restrição $\sum\lambda_i=1$, análoga à krigagem ordinária) é a **krigagem indicadora ordinária** (*ordinary indicator kriging*, OIK); existe também uma versão de **krigagem indicadora simples** (*simple indicator kriging*, SIK), análoga à krigagem simples do Módulo 20, que assume conhecida a proporção global declusterizada $F(z_c)$ como a "média" $m$ do sistema de krigagem simples, sem a restrição sobre a soma dos pesos.

A escolha entre as duas **não** é consensual, e é bom não memorizá-la como preferência: é uma decisão de estacionariedade, com um trade-off explícito. A OIK dispensa assumir conhecida, a priori, uma proporção global única válida em toda a área — o que raramente é realista quando o depósito tem domínios geológicos distintos —, mas, justamente porque a restrição $\sum\lambda_i=1$ faz com que a média global não receba peso nenhum, ela extrapola apoiada só na vizinhança local e admite pesos negativos, o que a torna mais propensa a estimativas fora de $[0,1]$. A SIK faz o contrário: ancora a extrapolação na proporção global declusterizada, o que reduz as violações de relação de ordem, ao custo de uma hipótese de estacionariedade mais forte. Boa parte da literatura de implementação de krigagem indicadora adota a versão simples exatamente por esse motivo.

Repetindo o sistema para cada limiar do conjunto escolhido, obtém-se um conjunto de estimativas $i^*(x_0;z_{c,1}), i^*(x_0;z_{c,2}), \dots$ — pontos discretos da distribuição acumulada local em $x_0$, que juntos aproximam a **ccdf local** completa (Aula 02): a partir dela é possível ler diretamente a probabilidade de o bloco estar acima de qualquer teor de corte de interesse, ou combinar os limiares para obter uma estimativa da média condicional (útil para geoestatística não linear, Aula 04).

### Violações de relação de ordem

Como cada limiar é krigado **separadamente** (mesmo na abordagem da mediana indicadora, em que os pesos são os mesmos para todos os cortes, a estimativa muda de limiar para limiar, porque os dados de entrada — a indicadora — mudam a cada corte), nada no procedimento garante, por construção, duas propriedades que uma função de distribuição acumulada genuína precisa ter: (1) **estar sempre dentro de $[0,1]$**, e (2) **ser não decrescente em $z_c$** (a probabilidade de estar abaixo de um limiar maior não pode ser menor do que a probabilidade de estar abaixo de um limiar menor). Na prática, é comum que as estimativas brutas de $i^*(x_0;z_c)$ ao longo dos vários limiares violem uma ou ambas as condições — um fenômeno chamado **violação de relação de ordem** (*order relation violation*), mais frequente nos limiares extremos (muito baixos ou muito altos), onde há poucos dados informativos.

A correção padrão (implementada, por exemplo, no algoritmo clássico de Deutsch & Journel) não descarta as estimativas nem refaz a krigagem: ela ajusta a sequência de valores estimados por limiar de duas formas — corrigindo valores fora de $[0,1]$ para o limite mais próximo (0 ou 1) e, para a monotonicidade, calculando a sequência corrigida por dois caminhos (uma correção "de baixo para cima" e outra "de cima para baixo" ao longo dos limiares) e tomando a média das duas, um procedimento puramente numérico de pós-processamento que não altera o variograma nem o sistema de krigagem em si. A frequência e a magnitude das violações de relação de ordem funcionam, na prática, como um diagnóstico indireto de qualidade: um conjunto de dados com muitas violações grandes geralmente indica poucos dados na vizinhança de busca, limiares extremos mal amostrados, ou um variograma mal ajustado — informação de volta para revisar a modelagem, não só um detalhe de implementação a corrigir silenciosamente.

## Exemplo trabalhado

**Situação:** para o limiar $z_c=1{,}0\%$ Cu, duas amostras estão na vizinhança de um bloco a estimar $x_0$: a amostra 1, com indicadora $i_1=1$ (teor abaixo do corte), está a $h_1=25$ m de $x_0$; a amostra 2, com indicadora $i_2=0$ (teor acima do corte), está a $h_2=50$ m de $x_0$; a distância entre as duas amostras é $h_{12}=35$ m. O variograma indicador ajustado nesse limiar (modelo esférico autorizado) tem patamar $C=0{,}22$ (a variância da indicadora nesse limiar, $F(z_c)[1-F(z_c)]$, com $F(z_c)\approx 0{,}33$), efeito pepita nulo e alcance $a=80$ m. Pela fórmula do modelo esférico, $\gamma(h)=C\left[1{,}5\frac{h}{a}-0{,}5\left(\frac{h}{a}\right)^3\right]$ para $h<a$, o que dá $\gamma_I(25)=0{,}0998$; $\gamma_I(35)=0{,}1352$; $\gamma_I(50)=0{,}1794$.

**Pergunta:** resolva o sistema de krigagem indicadora ordinária para obter $i^*(x_0;1{,}0\%)$ e interprete o resultado.

**Resolução:**

O sistema (forma idêntica à da krigagem ordinária, Módulo 20 Aula 05, com a variável indicadora):

$$0\,\lambda_1 + 0{,}1352\,\lambda_2 + \mu = 0{,}0998$$
$$0{,}1352\,\lambda_1 + 0\,\lambda_2 + \mu = 0{,}1794$$
$$\lambda_1+\lambda_2=1$$

Subtraindo a primeira da segunda: $0{,}1352\lambda_1 - 0{,}1352\lambda_2 = 0{,}0796 \implies \lambda_1-\lambda_2 \approx 0{,}589$.

Combinando com $\lambda_1+\lambda_2=1$: $\lambda_1 \approx 0{,}794$ e $\lambda_2 \approx 0{,}206$.

Substituindo na primeira equação: $0{,}1352(0{,}206)+\mu=0{,}0998 \Rightarrow 0{,}0279+\mu=0{,}0998 \Rightarrow \mu\approx 0{,}072$.

**Estimativa:** $i^*(x_0;1{,}0\%) = 0{,}794\times 1 + 0{,}206\times 0 = 0{,}794$.

**Leitura do resultado:** a probabilidade estimada de que o bloco $x_0$ tenha teor de Cu menor ou igual a $1{,}0\%$ é de aproximadamente $79{,}4\%$ — e, portanto, a probabilidade complementar de estar em minério de teor igual ou acima do corte é de cerca de $20{,}6\%$. O peso maior ($0{,}794$) recai sobre a amostra mais próxima e que está do lado "baixo" do corte, exatamente como no exemplo de krigagem ordinária do Módulo 20 — mas a interpretação do número final mudou por completo: ali, o resultado era um teor esperado em unidades da variável (%); aqui, é uma probabilidade, adimensional e confinada, por definição, a $[0,1]$. Repetindo esse mesmo procedimento para outros limiares (por exemplo, $0{,}5\%$ e $1{,}5\%$) e verificando que as três estimativas resultantes são não decrescentes e permanecem dentro de $[0,1]$ — sem precisar de correção de relação de ordem, neste caso — constrói-se um primeiro esboço da distribuição acumulada local do bloco.

## Recap relâmpago

- O sistema de **krigagem indicadora** tem a forma exata do sistema de krigagem ordinária (Módulo 20), mas krigando a indicadora: o resultado $i^*(x_0;z_c)$ é uma estimativa direta da probabilidade $F(z_c\mid\text{vizinhança})$, um ponto da distribuição acumulada local; repetindo para vários limiares, reconstrói-se a **ccdf local** anunciada na Aula 02.
- A escolha entre **OIK** e **SIK** é um *trade-off* de estacionariedade, **não** uma preferência estabelecida. A OIK não exige uma proporção global conhecida, mas, como a restrição $\sum\lambda_i=1$ deixa a média global sem peso, extrapola só pela vizinhança e admite pesos negativos — ficando mais propensa a estimativas fora de $[0,1]$. A SIK ancora a extrapolação na proporção global declusterizada e produz menos violações, ao custo de uma hipótese de estacionariedade mais forte.
- Como cada limiar é krigado separadamente, as estimativas brutas podem violar as propriedades de uma distribuição genuína (fora de $[0,1]$, não monotônicas) — **violação de relação de ordem**, corrigida por um procedimento numérico padrão (médias de correção ascendente/descendente) que não altera o variograma nem o sistema; violações grandes e frequentes são sinal de vizinhança pobre ou variograma mal ajustado, não só um detalhe a corrigir silenciosamente.

## Próxima aula

Aula 05 — Geoestatística não linear: dados log-normais, transformação logarítmica e krigagem log-normal. A abordagem não paramétrica das Aulas 02 a 04 lida com a assimetria transformando a variável em indicadoras binárias; a próxima aula trata do outro caminho clássico — transformar a variável por logaritmo — e mostra por que a retransformação de volta à escala original é onde o viés mais frequentemente entra sem aviso.

## Anterior

[[21-modelagem-geoestatistica-depositos-minerais-aula-03-variograma-indicador-modelos-autorizados|Aula 03 — Variograma indicador: cálculo, modelos autorizados e escolha da abordagem]] (Parte 1 deste par).

## Fontes

- Journel, A. G. (1983), "Nonparametric estimation of spatial distributions", *Mathematical Geology*, 15(3), 445–468.
- Isaaks, E. H. & Srivastava, R. M. (1989), *An Introduction to Applied Geostatistics*, Oxford University Press, capítulo 18, *Estimating a Distribution* (formulação do sistema de krigagem indicadora, ordinária e simples; relações de ordem).
- Mizuno, T. & Deutsch, C. V., *Sequential Indicator Simulation*, Geostatistics Lessons — a escolha entre krigagem simples e ordinária como decisão de estacionariedade; pesos negativos aplicados a dados indicadores e estimativas fora de $[0,1]$.
- Deutsch, C. V., *An Overview of Multiple Indicator Kriging*, Geostatistics Lessons — causas de estimativas fora de $[0,1]$ e de violação de relação de ordem.
- Deutsch, C. V. & Journel, A. G. (1998), *GSLIB: Geostatistical Software Library and User's Guide*, 2ª ed., Oxford University Press, capítulo V (algoritmo de correção de violação de relação de ordem na krigagem indicadora).
- Goovaerts, P. (1997), *Geostatistics for Natural Resources Evaluation*, Oxford University Press, capítulo 7, *Assessment of Local Uncertainty* (montagem da ccdf local a partir de múltiplos limiares).

<!--
nivel: avancado
palavras_corpo: 1270
mapa_objetivo_secao:
  geologia-avancado-m21-oa03: "O sistema de krigagem indicadora" + "Violações de relação de ordem" + "Exemplo trabalhado"

divisao_didatica:
  nota: "Parte 2 da antiga Aula 03 unica (aula NOVA; o ID m21-a04 foi REATRIBUIDO - a antiga a04, de krigagem log-normal, passou a a05, e a antiga a05, de wireframes, passou a a06). Dividida em 2026-09-19 pela revisao didatica (achado DID-M21-A03-CARGA-001). Recebeu as duas secoes de estimativa (sistema de krigagem indicadora, violacoes de relacao de ordem) mais o exemplo trabalhado ORIGINAL, aritmetico, preservado SEM NENHUMA ALTERACAO de conteudo cientifico - incluindo os valores corrigidos pela auditoria de 2026-09-18 (gamma(25)=0,0998, gamma(35)=0,1352, gamma(50)=0,1794, F(zc) aprox. 0,33, lambda1=0,794, lambda2=0,206, mu=0,072, i*=0,794). Todo o texto das duas secoes foi COPIADO LITERALMENTE da versao auditada. UNICO ACRESCIMO: o recap ganhou um terceiro marcador sobre o trade-off OIK x SIK, que a auditoria introduziu no corpo (achado laranja 8) mas que nunca chegara ao recap - restatement da alegacao GEOMOD-M21-A03-SIKVSOIK-009, sem fato novo."
  claim_ids_congelados: "Os prefixos A03 nos claim_id designam a numeracao PRE-DIVISAO em que cada alegacao foi emitida, nao a posicao atual da aula. Renumera-los quebraria a rastreabilidade com 21-modelagem-geoestatistica-depositos-minerais-auditoria.json e .md."

alegacoes_auditaveis:
  - claim_id: GEOMOD-M21-A03-SISTEMAIK-005
    claim: "O sistema de krigagem indicadora ordinaria tem a mesma forma do sistema de krigagem ordinaria (soma de pesos vezes variograma indicador mais multiplicador de Lagrange igual ao variograma indicador entre amostra e ponto/bloco alvo, com restricao soma dos pesos = 1), diferindo apenas por usar a variavel indicadora como dado de entrada; o resultado i*(x0;z_c) e uma estimativa direta de F(z_c | vizinhanca), um ponto da funcao de distribuicao acumulada local (ccdf local)."
    risk: fato
    source: "Isaaks & Srivastava (1989), An Introduction to Applied Geostatistics, capítulo 18 (Estimating a Distribution) (formulação do sistema de krigagem indicadora, ordinária e simples)."
  - claim_id: GEOMOD-M21-A03-SIKVSOIK-009
    claim: "A escolha entre krigagem indicadora ordinaria (OIK) e simples (SIK) NAO e consensual na literatura e depende da decisao de estacionariedade, nao de uma preferencia estabelecida. A OIK dispensa conhecer a priori uma proporcao global unica, mas, como a restricao soma(lambda)=1 faz a media global nao receber peso algum, ela extrapola apoiada so na vizinhanca local e admite pesos negativos, ficando mais propensa a estimativas fora de [0,1]. A SIK ancora a extrapolacao na proporcao global declusterizada, reduzindo violacoes de relacao de ordem ao custo de uma hipotese de estacionariedade mais forte; boa parte da literatura de implementacao de krigagem indicadora adota a versao simples por esse motivo."
    risk: controverso
    source: "Mizuno & Deutsch, Sequential Indicator Simulation, Geostatistics Lessons (the best kriging option will depend on the stationarity decision; em SK a probabilidade e estimada a partir dos dados condicionantes e de uma media global declusterizada, enquanto em OK a soma dos pesos e 1 e a media global nao recebe peso); Deutsch, C. V., An Overview of Multiple Indicator Kriging, Geostatistics Lessons; Goovaerts (1997), capítulo 7 (Assessment of Local Uncertainty)."
    revisao: "2026-09-18 — alegação nova, criada pela auditoria (🟠 8). A versão anterior afirmava que a OIK é preferida na prática, apresentando como consenso uma escolha que a literatura trata como trade-off de estacionariedade, e cuja outra ponta (SIK) é adotada justamente por reduzir violações de relação de ordem."
  - claim_id: GEOMOD-M21-A03-RELACAODEORDEM-006
    claim: "Como cada limiar e krigado separadamente, as estimativas brutas de i*(x0;z_c) ao longo de varios limiares nao sao garantidamente monotonicas nem confinadas a [0,1] — violacao de relacao de ordem; a correcao padrao (ex.: algoritmo de Deutsch & Journel) ajusta valores fora de [0,1] para o limite mais proximo e resolve a monotonicidade tomando a media entre uma correcao ascendente e uma descendente ao longo dos limiares, sem alterar o variograma ou o sistema de krigagem; violacoes grandes/frequentes tipicamente indicam vizinhanca pobre em dados ou variograma mal ajustado."
    risk: fato
    source: "Deutsch, C. V. & Journel, A. G. (1998), GSLIB: Geostatistical Software Library and User's Guide, 2ª ed., Oxford University Press, capítulo V (algoritmo de correção de relação de ordem); Isaaks & Srivastava (1989), capítulo 18 (Estimating a Distribution)."
  - claim_id: GEOMOD-M21-A03-EXEMPLONUMERICO-007
    claim: "No exemplo trabalhado desta aula (limiar 1,0% Cu; variograma esferico patamar C=0,22, pepita nula, alcance a=80 m; gamma(25)=0,0998, gamma(35)=0,1352, gamma(50)=0,1794), a solucao do sistema de krigagem indicadora ordinaria e lambda1=0,794, lambda2=0,206, mu=0,072, i*(x0)=0,794."
    risk: fato
    source: "Cálculo direto refeito na auditoria a partir da fórmula do modelo esférico (gamma(h) = C[1,5(h/a) - 0,5(h/a)^3] para h<a: gamma(25)=0,099768; gamma(35)=0,135164; gamma(50)=0,179395) e do sistema de krigagem ordinária aplicado à variável indicadora (formulação de Isaaks & Srivastava 1989, caps. 12 e 18)."
    revisao: "2026-09-18 — auditoria 🟠 7: a aritmética exibida não era reproduzível. Com os gammas de 3 casas antes impressos (0,100 / 0,135 / 0,179), 0,079/0,135 = 0,585, não 0,589, e lambda1 daria 0,793. O resultado final 0,795 só fechava contra os gammas exatos, que não apareciam no texto. Corrigido passando a 4 casas: 0,0796/0,1352 = 0,589 e lambda1 = 0,794."
  - claim_id: GEOMOD-M21-A03-PATAMARF-008
    claim: "A variancia de uma variavel indicadora num limiar z_c e F(z_c)[1-F(z_c)], que vale no maximo 0,25 (no limiar da mediana, onde F=0,5). No exemplo trabalhado desta aula, o patamar C=0,22 corresponde a F(z_c) aproximadamente 0,33 (0,33 x 0,67 = 0,221), nao a 0,30 (0,30 x 0,70 = 0,21)."
    risk: fato
    source: "Variancia de uma variavel de Bernoulli, p(1-p); conferido por calculo direto na auditoria (F(1-F)=0,22 tem raizes F=0,3268 e F=0,6732)."
    revisao: "2026-09-18 — alegação nova, criada pela auditoria (🟠 6). A versão anterior declarava o patamar 0,22 como sendo F(1-F) com F aproximadamente 0,30, o que dá 0,21: inconsistência interna do próprio exemplo. Removido também o qualificador variância máxima teórica, porque F(1-F) é a variância naquele limiar e o máximo (0,25) ocorre só na mediana."
-->
