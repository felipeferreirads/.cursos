# Aula 05: Geoestatística não linear: dados log-normais, transformação logarítmica e krigagem log-normal

**ID:** geologia-avancado-m21-a05
**Módulo:** [[21-modelagem-geoestatistica-depositos-minerais-modulo|Módulo 21 — Modelagem geoestatística de depósitos minerais]]
**Duração estimada:** ~28 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** explicar por que distribuições log-normais de teor motivam trabalhar no espaço logarítmico, mostrar como a krigagem é aplicada aos dados transformados, e demonstrar por que a retransformação de volta à escala original exige um termo de correção de viés, não apenas a exponencial inversa.
**Ao final você vai conseguir:** reconhecer os indícios de que uma distribuição de teores é aproximadamente log-normal; aplicar a transformação logarítmica e krigar a variável transformada; explicar por que $\exp(Y^*)$ subestima sistematicamente o teor esperado, e aplicar o termo de correção que resolve isso; e distinguir a krigagem log-normal baseada em krigagem simples (fórmula exata, sob a hipótese multigaussiana) da versão baseada em krigagem ordinária, que acrescenta o multiplicador de Lagrange — e localizar onde a literatura de fato diverge sobre essa técnica.
**Pré-requisito:** Aulas 02 a 04 deste módulo (geoestatística não paramétrica) e Módulo 20, Aula 05 (krigagem simples e ordinária).

## Conteúdo

### Por que teores de mineração tendem a ser log-normais

O Módulo 20 (Aula 01) já observou que distribuições de teor em depósitos minerais costumam ser fortemente assimétricas, positivamente enviesadas, com poucos valores muito altos puxando a cauda — o motivo prático de capear **valores extremos de alto teor** antes da composição. Essa assimetria não é acidental: ela é uma consequência esperada do próprio processo geológico de formação de muitos depósitos, sobretudo os de origem hidrotermal ou de concentração supergênica, em que o teor final resulta da **multiplicação** de vários processos de enriquecimento sucessivos e parcialmente independentes (deposição inicial, remobilização, concentração secundária), em vez da soma de contribuições independentes. Um argumento clássico (derivado do teorema central do limite, mas aplicado ao produto em vez da soma de variáveis aleatórias) prevê que o **logaritmo** dessa variável resultante de um processo multiplicativo tende à normalidade — daí a distribuição **log-normal** ser um modelo razoável, empiricamente confirmado em muitos (não todos) depósitos, especialmente para metais preciosos e alguns metais de base.

O diagnóstico prático de log-normalidade não depende de teoria: verifica-se plotando o histograma do **logaritmo** dos teores e checando visualmente (ou por teste estatístico) se ele se aproxima de uma distribuição normal — o mesmo tipo de checagem gráfica (histograma, gráfico de probabilidade) já usado no Módulo 20 para os teores brutos, agora aplicado aos dados transformados. Quando essa checagem confirma log-normalidade aproximada, abre-se um caminho alternativo (e, historicamente, anterior) à geoestatística não paramétrica da Aula 02: em vez de transformar em indicadoras binárias, transforma-se a variável inteira por logaritmo, krigar no espaço transformado (onde a distribuição é bem comportada, próxima da normal) e depois **retransformar** o resultado de volta à escala original de teor.

### A transformação logarítmica e a krigagem no espaço transformado

Definindo $Y(x) = \ln[Z(x)]$, onde $Z(x)$ é o teor original, o procedimento segue os mesmos passos já vistos no Módulo 20 — mas aplicados a $Y$, não a $Z$: calcula-se a estatística descritiva de $Y$, o variograma experimental de $Y$, ajusta-se um modelo autorizado (Aula 03 deste módulo), e resolve-se o sistema de krigagem — simples ou ordinária — usando o variograma de $Y$ e os valores $y_i=\ln(z_i)$ das amostras. Até aqui, nada é conceitualmente novo: é krigagem ordinária ou simples, exatamente como no Módulo 20, só que aplicada a uma variável derivada por uma transformação matemática em vez da variável bruta.

A parte que exige cuidado — e que dá nome a esta técnica como um capítulo à parte da **geoestatística não linear** — está no próximo passo: o resultado da krigagem, $Y^*(x_0)$, é uma estimativa do **logaritmo** do teor, não do teor em si. Para obter uma estimativa útil na unidade original (g/t, %, ppm), é preciso desfazer a transformação — e é exatamente aqui, na retransformação, que o viés mais frequentemente entra sem aviso, como sinalizado no ponto de dificuldade deste módulo.

### O problema da retransformação: por que $\exp(Y^*)$ não basta

A tentação natural é desfazer o logaritmo aplicando a exponencial diretamente ao resultado da krigagem: $Z^*(x_0) \overset{?}{=} \exp\left[Y^*(x_0)\right]$. Essa operação é **enviesada para baixo** — sistematicamente subestima o teor esperado —, e a razão é uma propriedade matemática geral, não uma peculiaridade da krigagem: a função exponencial é **convexa**, e para qualquer função convexa $g$ e qualquer variável aleatória $X$, a desigualdade de Jensen garante que $E[g(X)] \ge g(E[X])$. Aplicada aqui, com $g=\exp$ e $X=Y$: o valor esperado do teor, $E[Z]=E[\exp(Y)]$, é **maior ou igual** a $\exp(E[Y])$ — ou seja, "exponenciar a média do logaritmo" (o que $\exp[Y^*(x_0)]$ faz, aproximadamente, quando $Y^*$ é uma boa estimativa de $E[Y\mid\text{vizinhança}]$) não recupera a média do teor original; recupera algo sistematicamente menor do que ela. Quanto maior a variância de $Y$, maior essa diferença — em distribuições muito assimétricas (variância do log alta), o viés da retransformação ingênua pode ser considerável, e é precisamente nos depósitos de maior variabilidade que a krigagem log-normal costuma ser cogitada em primeiro lugar, o que torna esse viés particularmente perigoso de ignorar.

Para uma variável log-normal com $Y\sim\text{Normal}(\mu_Y,\sigma_Y^2)$, a relação exata entre a média de $Z=\exp(Y)$ e os parâmetros de $Y$ é:

$$E[Z] = \exp\left(\mu_Y + \frac{\sigma_Y^2}{2}\right)$$

O termo $\exp(\sigma_Y^2/2)$ — sempre maior que 1 — é o **fator de correção log-normal**: é ele que falta na retransformação ingênua, e é ele que a krigagem log-normal precisa incorporar para produzir uma estimativa não viesada de $Z$, não apenas de $\ln Z$.

### Krigagem log-normal baseada em krigagem simples (fórmula exata)

Sob a hipótese de que o campo $Y(x)$ é **multigaussiano** (não só marginalmente normal em cada ponto, mas conjuntamente normal em qualquer combinação de pontos — uma hipótese mais forte do que a estacionariedade de segunda ordem do Módulo 20, Aula 02), a distribuição de $Y(x_0)$ condicionada aos dados vizinhos é, ela mesma, normal, com média igual à estimativa de **krigagem simples** $Y^*_{SK}(x_0)$ e variância igual à **variância de krigagem simples** $\sigma^2_{SK}(x_0)$ (Módulo 20, Aula 05). Sob essa hipótese, o valor esperado condicional do teor original é dado por uma aplicação direta da fórmula da média log-normal, mas usando os parâmetros *locais* (condicionais aos dados), não os parâmetros globais:

$$Z^*_{SLN}(x_0) = \exp\left[Y^*_{SK}(x_0) + \frac{\sigma^2_{SK}(x_0)}{2}\right]$$

Essa é a forma **exata** (dentro do modelo assumido) da krigagem log-normal, às vezes chamada de krigagem log-normal simples (*simple lognormal kriging*): ela corrige exatamente o viés de Jensen usando a própria variância de krigagem simples calculada no ponto, que já é maior nas regiões pior amostradas — um efeito adicional bem-vindo, porque a correção de viés é automaticamente maior onde a incerteza local é maior, e menor onde os dados vizinhos restringem bem a estimativa.

### Krigagem log-normal baseada em krigagem ordinária (o termo do multiplicador de Lagrange)

Na prática de recursos minerais, a krigagem simples raramente é preferida à ordinária pela mesma razão do Módulo 20 (Aula 05): exigir uma média global $m_Y$ conhecida e constante é uma hipótese forte. Quando se usa krigagem **ordinária** no espaço logarítmico, a fórmula exata acima deixa de valer, porque a variância de krigagem ordinária $\sigma^2_{OK}(x_0)$ não tem a mesma interpretação de variância condicional local que a variância de krigagem simples tem sob o modelo multigaussiano. A prática consolidada usa, nesse caso, uma correção que incorpora o multiplicador de Lagrange $\mu$ do próprio sistema de krigagem ordinária (Módulo 20, Aula 05) como um termo de ajuste adicional:

$$Z^*_{OLN}(x_0) = \exp\left[Y^*_{OK}(x_0) + \frac{\sigma^2_{OK}(x_0)}{2} - \mu\right]$$

Essa fórmula é **padrão e não é objeto de divergência**: ela foi derivada por Journel (1980) para o caso de média desconhecida e é reproduzida sem alteração nos tratados de referência (Webster & Oliver, 2007) e nos pacotes de software de estimativa de recursos; Rendu (1979) trata o mesmo problema de estimativa normal e log-normal e é a referência anterior mais citada ao lado dela. O termo $-\mu$ não é um remendo: ele é o preço, no espaço logarítmico, de a média ser desconhecida, e é exatamente por isso que ele não aparece na versão baseada em krigagem simples, onde a média é dada.

**Onde a literatura de fato diverge é em outro lugar** — e vale saber onde, porque é uma questão aberta, não resolvida:

- **A correção entrega mesmo uma estimativa não viesada?** Roth (1998), num artigo cujo título já é a pergunta ("a krigagem log-normal é adequada para estimativa local?"), mostra que o estimador respeita as propriedades de não viés quando se considera o **campo inteiro**, mas que, **localmente**, bloco a bloco, ele se comporta de um modo que não é nem o esperado nem o intuitivo. A resposta do artigo não é um "sim".
- **A correção depende demais do variograma.** Yamamoto (2007) argumenta que as estimativas retransformadas continuam viesadas justamente porque o termo de não viés depende **inteiramente** do modelo de variograma ajustado: dois ajustes igualmente defensáveis do mesmo variograma experimental produzem dois teores retransformados diferentes. Ele propõe um fator corretivo alternativo, ancorado na média amostral.

O efeito prático dessa divergência para quem usa a técnica é direto: a krigagem log-normal é sensível ao modelo de variograma de uma forma que a krigagem ordinária de teores brutos não é, e um relatório de recursos que a use precisa reportar o modelo ajustado, não só a estimativa. E, em qualquer das posições, permanece verdadeiro o ponto de maior risco de viés silencioso desta aula: um praticante que aplica a fórmula de krigagem simples (sem o termo $-\mu$) a uma krigagem ordinária, ou que esquece o termo de correção por completo, introduz um erro que não aparece como um número "estranho" — o resultado parece plausível, só está sistematicamente deslocado.

### Onde essa abordagem se encaixa frente à indicadora

A krigagem log-normal e a krigagem indicadora (Aulas 02–04) resolvem o mesmo problema geral — dados com distribuição de forma difícil — por caminhos diferentes. A log-normal exige a hipótese distribucional mais forte (log-normalidade, idealmente multigaussianidade no espaço transformado), mas, quando essa hipótese se sustenta, produz uma única estimativa pontual do teor esperado, diretamente comparável à krigagem ordinária de teores brutos. A krigagem indicadora dispensa a hipótese distribucional (é "não paramétrica" porque não assume forma alguma), ao custo de produzir uma distribuição de probabilidades em vez de um único número, e de exigir modelar um variograma por limiar. Na prática de projetos reais, é comum checar a log-normalidade primeiro (mais barata de implementar) e recorrer à krigagem indicadora quando a distribuição não se ajusta bem ao modelo log-normal — ou usar as duas em conjunto, cruzando resultados como checagem de consistência.

## Exemplo trabalhado

**Situação:** duas amostras de Au (g/t) estão na vizinhança de um bloco a estimar $x_0$: $z_1=2{,}0$ g/t (logaritmo $y_1=\ln 2{,}0=0{,}6931$) a $h_1=30$ m de $x_0$, e $z_2=1{,}4$ g/t ($y_2=\ln 1{,}4=0{,}3365$) a $h_2=60$ m de $x_0$; a distância entre as amostras é $h_{12}=40$ m. O variograma do logaritmo dos teores foi ajustado (modelo esférico, patamar $1{,}0$, pepita nula, alcance $100$ m — os mesmos parâmetros usados no exemplo de krigagem ordinária do Módulo 20, Aula 05, aqui reaproveitados para o espaço log), dando o mesmo sistema já resolvido naquela aula: $\lambda_1=0{,}8125$, $\lambda_2=0{,}1875$, $\mu=0{,}330$ e $\sigma^2_{OK}(x_0)=0{,}833$.

**Pergunta:** calcule $Y^*_{OK}(x_0)$ e, a partir dele, a estimativa de krigagem log-normal (baseada em krigagem ordinária) do teor $Z^*_{OLN}(x_0)$; compare com a retransformação ingênua $\exp[Y^*_{OK}(x_0)]$.

**Resolução:**

$$Y^*_{OK}(x_0) = 0{,}8125\times 0{,}6931 + 0{,}1875\times 0{,}3365 = 0{,}5632+0{,}0631=0{,}6263$$

**Retransformação ingênua** (sem correção): $\exp(0{,}6263) = 1{,}871$ g/t.

**Krigagem log-normal (com correção):**

$$Z^*_{OLN}(x_0) = \exp\left[0{,}6263 + \frac{0{,}833}{2} - 0{,}330\right] = \exp\left[0{,}6263+0{,}4165-0{,}330\right] = \exp(0{,}7128) \approx 2{,}04 \text{ g/t}$$

**Leitura dos resultados:** a diferença entre a retransformação ingênua ($1{,}87$ g/t) e a estimativa log-normal corrigida ($2{,}04$ g/t) é de quase $0{,}17$ g/t — cerca de 8% do valor corrigido, ou 9% da retransformação ingênua —, inteiramente atribuível ao termo de correção de viés $\sigma^2_{OK}/2$ (que puxa a estimativa para cima, corrigindo a subestimativa de Jensen) parcialmente compensado pelo termo $-\mu$ (específico da versão baseada em krigagem ordinária, onde a média é desconhecida). Note que os pesos $\lambda_1,\lambda_2$ usados aqui são os mesmos calculados no Módulo 20 para o exemplo de krigagem ordinária de teores brutos — o que muda entre os dois exemplos não é a mecânica do sistema de krigagem (idêntica, seja a variável o teor bruto ou o seu logaritmo), mas o que se faz com o resultado depois de obtê-lo: um teor bruto krigado já está na escala certa; um logaritmo krigado precisa do passo extra de retransformação com correção de viés antes de ser reportado como teor.

## Recap relâmpago

- Distribuições de teor fortemente assimétricas em depósitos minerais são frequentemente aproximadas por uma distribuição **log-normal**, consistente com processos geológicos multiplicativos de enriquecimento — diagnosticada checando se o **logaritmo** dos teores se aproxima de uma normal.
- A krigagem log-normal krigar $Y=\ln(Z)$ com a mesma mecânica de sistema de krigagem do Módulo 20 (simples ou ordinária), mas o resultado $Y^*$ é uma estimativa do logaritmo, não do teor.
- **Retransformar ingenuamente** com $\exp(Y^*)$ **subestima sistematicamente** o teor esperado — consequência da convexidade da exponencial (desigualdade de Jensen) —, e exige o **fator de correção log-normal** $\exp(\sigma_Y^2/2)$.
- A forma **exata** da correção usa a krigagem simples: $Z^*_{SLN}=\exp[Y^*_{SK}+\sigma^2_{SK}/2]$, válida sob a hipótese multigaussiana. A forma usada com krigagem ordinária, $Z^*_{OLN}=\exp[Y^*_{OK}+\sigma^2_{OK}/2-\mu]$, acrescenta o multiplicador de Lagrange do sistema e é **igualmente padrão** (Journel, 1980) — a fórmula não é objeto de divergência. O que a literatura discute é (a) se a krigagem log-normal serve para estimativa **local**, e não só global (Roth, 1998), e (b) o quanto o termo de não viés fica refém do modelo de variograma ajustado (Yamamoto, 2007).
- Esquecer o termo de correção, ou aplicar a fórmula de krigagem simples a uma krigagem ordinária, é o **ponto de maior risco de viés silencioso** do módulo: o resultado parece plausível e está sistematicamente deslocado.
- A krigagem log-normal (hipótese distribucional forte, uma estimativa pontual) e a krigagem indicadora (sem hipótese distribucional, uma distribuição de probabilidades) resolvem o mesmo problema de assimetria por caminhos diferentes e complementares, não concorrentes.

## Próxima aula

Aula 06 — Modelagem do depósito: perfis de furos, áreas de influência, triangulação de Delaunay, wireframes e integração lógica com os modelos estimados. Com as ferramentas de estimativa não paramétrica e não linear estabelecidas, a última aula do módulo volta à geometria: como construir a envoltória sólida do depósito a partir dos furos de sonda e integrá-la, por operações lógicas, ao modelo de blocos estimado nas aulas anteriores.

**Espere uma mudança de registro.** As Aulas 01 a 05 foram quantitativas — fórmulas, sistemas de equações, estimadores e seus vieses. A Aula 06 é geométrica e, em boa parte, qualitativa: o passo que ela acrescenta não se resolve com uma equação, começa com um geólogo decidindo à mão qual contato de um furo corresponde a qual contato do furo vizinho. Não é um desvio do módulo — é o que amarra tudo o que foi estimado até aqui a um corpo geológico com forma, volume e limites.

## Anterior

[[21-modelagem-geoestatistica-depositos-minerais-aula-04-krigagem-indicadora-relacoes-de-ordem|Aula 04 — Krigagem indicadora: sistema, interpretação e violações de relação de ordem]].

## Fontes

- Journel, A. G. & Huijbregts, C. J. (1978), *Mining Geostatistics*, Academic Press (krigagem log-normal: formulação baseada em krigagem simples, hipótese multigaussiana, fator de correção).
- Journel, A. G. (1980), "The lognormal approach to predicting local distributions of selective mining unit grades", *Mathematical Geology*, 12(4), 285–303 — **fonte primária da retransformação log-normal**, nos casos de média conhecida (krigagem simples) e desconhecida (krigagem ordinária, com o termo $-\mu$).
- Rendu, J.-M. (1979), "Normal and lognormal estimation", *Journal of the International Association for Mathematical Geology*, 11(4), 407–422 — tratamento anterior do problema de estimativa normal e log-normal, referência clássica citada ao lado de Journel (1980).
- Webster, R. & Oliver, M. A. (2007), *Geostatistics for Environmental Scientists*, 2ª ed., Wiley — apresentação de referência das duas fórmulas de retransformação (SK e OK) e das variâncias retransformadas.
- Roth, C. (1998), "Is lognormal kriging suitable for local estimation?", *Mathematical Geology*, 30(8), 999–1009 — o estimador é não viesado sobre o campo inteiro, mas apresenta localmente comportamento nem esperado nem intuitivo.
- Yamamoto, J. K. (2007), "On unbiased backtransform of lognormal kriging estimates", *Computational Geosciences*, 11(3), 219–234 — as estimativas retransformadas permanecem viesadas porque o termo de não viés depende inteiramente do modelo de variograma; propõe fator corretivo alternativo.
- Goovaerts, P. (1997), *Geostatistics for Natural Resources Evaluation*, Oxford University Press, capítulo 7, *Assessment of Local Uncertainty* (métodos não lineares; krigagem log-normal e suas limitações práticas).
- Sinclair, A. J. & Blackwell, G. H. (2002), *Applied Mineral Inventory Estimation*, Cambridge University Press, capítulo 9 (aplicação da krigagem log-normal em avaliação de recursos minerais e riscos de viés de retransformação).

<!--
nivel: avancado
palavras_corpo: 2150
mapa_objetivo_secao:
  geologia-avancado-m21-oa03: "Por que teores de mineração tendem a ser log-normais" + "A transformação logarítmica e a krigagem no espaço transformado" + "O problema da retransformação: por que exp(Y*) não basta" + "Krigagem log-normal baseada em krigagem simples (fórmula exata)" + "Krigagem log-normal baseada em krigagem ordinária (o termo do multiplicador de Lagrange)" + "Onde essa abordagem se encaixa frente à indicadora" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOMOD-M21-A04-ORIGEMLOGNORMAL-001
    claim: "Distribuicoes de teor em deposito minerais tendem a ser aproximadamente log-normais em muitos casos (nao todos), atribuido a processos geologicos multiplicativos de enriquecimento sucessivo (analogo ao teorema central do limite aplicado ao produto de variaveis aleatorias em vez da soma); o diagnostico pratico e verificar se o logaritmo dos teores se aproxima de uma distribuicao normal, por histograma ou grafico de probabilidade."
    risk: fato
    source: "Journel & Huijbregts (1978), Mining Geostatistics, Academic Press; Isaaks & Srivastava (1989), An Introduction to Applied Geostatistics, capítulo 18 (Estimating a Distribution); Sinclair & Blackwell (2002), Applied Mineral Inventory Estimation, capítulo 9."
  - claim_id: GEOMOD-M21-A04-VIESJENSEN-002
    claim: "A retransformacao ingenua Z*=exp(Y*) subestima sistematicamente o teor esperado, consequencia da desigualdade de Jensen aplicada a funcao convexa exponencial (E[g(X)] >= g(E[X]) para g convexa); para uma variavel log-normal Y~Normal(mu_Y, sigma_Y^2), a media exata de Z=exp(Y) e E[Z]=exp(mu_Y + sigma_Y^2/2), sendo exp(sigma_Y^2/2) (sempre >1) o fator de correcao que falta na retransformacao ingenua."
    risk: fato
    source: "Resultado padrao de teoria de probabilidade (media da distribuição log-normal) aplicado à krigagem por Journel & Huijbregts (1978), Mining Geostatistics; Journel, A. G. (1980), 'The lognormal approach to predicting local distributions of selective mining unit grades', Mathematical Geology, 12(4), 285-303; Webster, R. & Oliver, M. A. (2007), Geostatistics for Environmental Scientists, 2a ed., Wiley."
  - claim_id: GEOMOD-M21-A04-KRIGAGEMSLN-003
    claim: "Sob a hipotese de campo multigaussiano, a krigagem log-normal baseada em krigagem simples tem forma exata Z*_SLN(x0) = exp[Y*_SK(x0) + sigma^2_SK(x0)/2], onde Y*_SK e a estimativa de krigagem simples do logaritmo do teor e sigma^2_SK e a variancia de krigagem simples correspondente — a distribuicao condicional de Y(x0) dado os dados vizinhos e, sob essa hipotese, normal com esses parametros."
    risk: fato
    source: "Journel & Huijbregts (1978), Mining Geostatistics, Academic Press; Journel, A. G. (1980), Mathematical Geology, 12(4), 285-303 (derivação da krigagem log-normal simples sob hipótese multigaussiana); Webster & Oliver (2007), Geostatistics for Environmental Scientists, 2a ed., Wiley."
  - claim_id: GEOMOD-M21-A04-KRIGAGEMOLN-004
    claim: "A krigagem log-normal baseada em krigagem ordinaria usa Z*_OLN(x0) = exp[Y*_OK(x0) + sigma^2_OK(x0)/2 - mu], incorporando o multiplicador de Lagrange mu do sistema de krigagem ordinaria. A FORMULA EM SI E PADRAO E NAO E OBJETO DE DIVERGENCIA: foi derivada por Journel (1980) para o caso de media desconhecida e e reproduzida sem alteracao nos tratados de referencia (Webster & Oliver, 2007) e no software de estimativa de recursos; Rendu (1979) trata o mesmo problema e e a referencia anterior mais citada ao lado dela. A controversia real da literatura e OUTRA, e esta em dois pontos: (a) Roth (1998) mostra que o estimador respeita o nao vies sobre o campo inteiro mas se comporta localmente de modo nem esperado nem intuitivo, questionando seu uso para estimativa LOCAL; (b) Yamamoto (2007) argumenta que as estimativas retransformadas permanecem viesadas porque o termo de nao vies depende inteiramente do modelo de variograma ajustado, e propoe um fator corretivo alternativo ancorado na media amostral."
    risk: controverso
    source: "Journel, A. G. (1980), 'The lognormal approach to predicting local distributions of selective mining unit grades', Mathematical Geology, 12(4), 285-303 (derivacao para media conhecida e desconhecida); Webster, R. & Oliver, M. A. (2007), Geostatistics for Environmental Scientists, 2a ed., Wiley (as duas formulas, com e sem o termo -mu); Rendu, J.-M. (1979), J. Int. Assoc. Math. Geol., 11(4), 407-422; Roth, C. (1998), 'Is lognormal kriging suitable for local estimation?', Mathematical Geology, 30(8), 999-1009; Yamamoto, J. K. (2007), 'On unbiased backtransform of lognormal kriging estimates', Computational Geosciences, 11(3), 219-234."
    revisao: "2026-09-18 — auditoria ⚪ 9. O redator marcou esta alegação como controversa supondo que a fórmula variasse entre fontes. A checagem cruzada contra Journel (1980), Webster & Oliver (2007) e a documentação de software mostrou que a fórmula é única e estável: NAO há erro nem divergência sobre ela, e a atribuição primária correta é Journel (1980), não Rendu (1979). A controvérsia genuína existe, mas é sobre a adequação da técnica à estimativa local (Roth 1998) e sobre a dependência do termo de não viés em relação ao variograma (Yamamoto 2007). Texto reescrito para expor as duas posições. Mantido como ⚪: não bloqueia o gate."
  - claim_id: GEOMOD-M21-A04-EXEMPLONUMERICO-005
    claim: "No exemplo trabalhado desta aula (y1=ln(2,0)=0,6931, y2=ln(1,4)=0,3365, pesos lambda1=0,8125/lambda2=0,1875, mu=0,330, sigma^2_OK=0,833, reaproveitados do exemplo de krigagem ordinaria do Modulo 20 Aula 05), Y*_OK(x0)=0,6263; a retransformacao ingenua da exp(0,6263)=1,871 g/t; a krigagem log-normal corrigida (base OK) da exp(0,6263+0,4165-0,330)=exp(0,7128) aproximadamente 2,04 g/t. A diferenca de 0,169 g/t equivale a 8,3% do valor corrigido e a 9,0% da retransformacao ingenua."
    risk: fato
    source: "Cálculo direto refeito na auditoria a partir dos valores de lambda1, lambda2, mu e sigma^2_OK já auditados no Módulo 20 (course-state.yaml, seção do módulo 20, worked_examples_note), aplicados à fórmula de krigagem log-normal ordinária: Y*=0,626271; exp(Y*)=1,8706; exp(0,712771)=2,0396; diferenca 0,1690."
    revisao: "2026-09-18 — auditoria 🟡 14: a aula dizia cerca de 9% do valor final. 0,169/2,04 = 8,3% (valor final corrigido); os 9,0% são em relação à retransformação ingênua. Texto corrigido para nomear as duas bases."
-->
