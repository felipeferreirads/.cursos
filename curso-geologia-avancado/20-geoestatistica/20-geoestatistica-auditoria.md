# Auditoria científica — Módulo 20: Introdução à geoestatística

**Data do levantamento:** 2026-09-18 · **Correções aplicadas em:** 2026-09-18
**Modo:** `audit-and-fix` · **Profundidade:** `full`
**Escopo:** as 4 aulas do módulo, auditadas em conjunto, mais o hub do módulo
**Veredito:** **aprovado — gate liberado.** 0 achados vermelhos e 0 laranjas em aberto; os 17 achados corrigíveis (1 vermelho, 8 laranjas, 8 amarelos) foram corrigidos cirurgicamente. **Questionário e flashcards liberados**, observadas as restrições de formato ao fim deste relatório.

## Contagem por severidade

| Severidade | Contagem | Situação |
|---|---|---|
| 🔴 Vermelho (afirmação factualmente falsa) | **1** | **corrigido** |
| 🟠 Laranja (impreciso, confusão de escopo, omissão que gera erro) | **8** | **corrigidos** |
| 🟡 Amarelo (atribuição de fonte errada, citação defeituosa, valor apresentado incorretamente) | **8** | **corrigidos** |
| 🔵 Azul (verificado e correto — registro de que foi checado) | **21** | sem alteração (são registros de verificação bem-sucedida) |
| ⚪ Branco (questão aberta na literatura apresentada como resolvida) | **0** | — |

> **Nota sobre as contagens:** os números da coluna "Contagem" são os do levantamento original e não mudam — um achado não se apaga ao ser corrigido, ele muda de situação.

**Alegações rastreadas:** as 19 `alegacoes_auditaveis` declaradas pelas aulas (5 na a01, 4 na a02, 5 na a03, 5 na a04) foram verificadas uma a uma; a auditoria levantou mais 6, chegando a **25 alegações rastreadas**. As 6 novas foram gravadas nos blocos de metadados das aulas: `GEOEST-M20-A01-VIESMEDIASIMPLES-006`, `GEOEST-M20-A01-ARITMETICAEXEMPLO-007`, `GEOEST-M20-A03-AJUSTEEXEMPLO-006`, `GEOEST-M20-A04-RAIOBUSCA-006`, `GEOEST-M20-A04-ARREDONDAMENTOPESOS-007`, `GEOEST-M20-A04-ESTABILIDADESISTEMA-008`.

**Exemplos trabalhados:** este é o primeiro módulo do curso em que **todos os quatro exemplos pedem aritmética**, e todos os quatro foram refeitos do zero, número por número. **Dois fecham sem reparo (a02 e a04 na parte numérica). Dois não fechavam**: o da a01 tinha erro de percentual e uma razão de pesos errada (🟠 3); o da a03 fechava numericamente mas chegava à conclusão certa pelo argumento errado (🟠 7). Além disso, **refiz o ajuste do modelo esférico da a03 contra os oito pontos experimentais da tabela e o sistema de krigagem da a04 contra a fórmula do modelo esférico** — as duas construções são numericamente sólidas e foram registradas como alegações novas.

---

## Padrão dominante

**A CONFUSÃO CONCEITUAL DE ALTO NÍVEL, não o erro numérico.** Este módulo quebra o padrão dos três anteriores. Os módulos 17, 18 e 19 tiveram como defeito dominante a **atribuição de fonte** — o dado certo debaixo do nome errado. Aqui a atribuição de fonte continua presente (os 8 amarelos são todos disso, e a recomendação de processo escrita nas auditorias do M18 e do M19 **segue não implementada, quarta reincidência**), mas ela não é mais o achado mais caro. O mais caro é outra coisa:

**os três achados de maior impacto deste módulo são simplificações que a literatura aplicada de geoestatística repete há décadas e que são falsas.** São erros que um autor competente comete justamente por estar reproduzindo o folclore da área, não por descuido:

1. **"A hipótese intrínseca tolera deriva"** (🔴 1). É o erro clássico do assunto. A hipótese intrínseca exige $E[Z(x+h)-Z(x)]=0$, que **é** uma condição de média constante — uma deriva a viola. A folga entre hipótese intrínseca e estacionariedade de segunda ordem está em outro lugar: na **dispensa de variância a priori finita**.
2. **"O comportamento na origem distingue esférico de exponencial"** (🟠 7). Não distingue: os dois são lineares na origem. O comportamento na origem separa o gaussiano (parabólico) dos outros dois.
3. **"A média aritmética não ponderada superestima sistematicamente"** (🟠 2). Não superestima sistematicamente: o sentido do viés segue o sinal da correlação entre comprimento e teor.

Os três têm a mesma assinatura: a afirmação errada é a *versão mnemônica* de uma afirmação certa, e é justamente por ser mais fácil de lembrar que ela circula. Isso importa para o gerador de questionários — ver `generator_warnings` ao fim.

**Observação de processo para o orquestrador:** o defeito de atribuição de fonte já custou 4 achados no M17, 6 no M18, 7 no M19 e 8 no M20. Continua piorando. A verificação recomendada (conferir, para cada entrada de Fontes, que a obra existe com aquele autor/ano/paginação **e** que o capítulo citado trata do fato que a aula lhe credita) continua sem ser implementada no gerador de aula.

---

## Achados

### 🔴 1. A hipótese intrínseca apresentada como tolerante a deriva (drift)

**claim_id:** `GEOEST-M20-A02-HIPOTESEINTRINSECA-002`
**Tipo:** erro factual
**Onde:** a02 · seção "Estacionariedade: por que repetir no espaço substitui repetir no tempo"; propagado para o Recap relâmpago e para o próprio bloco de alegações auditáveis
**Está escrito:** "a hipótese intrínseca continua válida mesmo em fenômenos com uma **deriva** (*drift*) regional lenta — uma tendência sistemática de aumento ou diminuição do teor médio numa direção, comum em depósitos com zoneamento geoquímico — situação em que a covariância de segunda ordem deixa de estar bem definida (a variância teórica cresce sem limite) mas o variograma dos incrementos locais ainda pode existir e ser modelado."
**Problema:** a afirmação junta uma causa errada a uma consequência certa, e o resultado é falso. A hipótese intrínseca tem **duas** condições, e a primeira é $E[Z(x+h)-Z(x)]=0$ — que é, literalmente, a exigência de que o valor esperado não mude de um ponto para outro. **Uma deriva viola essa condição**, não é acomodada por ela. O que a hipótese intrínseca dispensa é a **segunda** exigência da estacionariedade de segunda ordem: a existência de uma covariância $C(h)$ finita e bem definida, com $C(0)=\sigma^2$ finita. Fenômenos de variabilidade não limitada — variograma que sobe sem atingir patamar, modelos linear e de potência, comportamento tipo browniano — satisfazem a hipótese intrínseca e **não** satisfazem a estacionariedade de segunda ordem. É aí, e só aí, que está a folga. O parêntese sobre a variância crescer sem limite é a razão certa, mas o texto a atribui à deriva, que é um problema de outra natureza. Deriva se trata por **quase-estacionariedade em vizinhança móvel** (é isto que a krigagem ordinária faz, e é a razão prática de ela dominar a indústria) ou, formalmente, por **krigagem universal / IRF-$k$**.
**Por que é vermelho e não laranja:** é o conceito que organiza a aula inteira e o que a aula 04 usa como justificativa para preferir a krigagem ordinária. Um questionário gerado sobre a versão anterior produziria um gabarito que afirma o contrário do que a literatura estabelece, sobre o item mais provável de ser cobrado do módulo. E o erro é de **direção**, não de grau.
**Correção aplicada:** três parágrafos reescritos na a02, separando explicitamente (a) onde está a folga entre as duas hipóteses — variância não limitada — de (b) o que fazer com deriva — quase-estacionariedade (krigagem ordinária) ou krigagem universal / IRF-$k$, declaradas fora do escopo do módulo. O Recap e a alegação auditável foram realinhados. A alegação carrega nota de revisão datada.
**Fonte:** Journel & Huijbregts (1978), *Mining Geostatistics*, cap. II · Chilès & Delfiner (2012), *Geostatistics: Modeling Spatial Uncertainty*, 2ª ed., Wiley, caps. 1-2 · Matheron (1963), *Economic Geology* 58(8), 1246-1266 · M. Putti, *Kriging with the intrinsic hypothesis* (Univ. Padova) · **Nível:** revisada por pares / tratado de referência
**Confiança:** confirmado
**Também aparece em:** nenhum outro arquivo do curso — verificado contra o M13 (pré-requisito declarado) e contra o M21, que ainda não tem aulas escritas.
**Desfecho:** **corrigido**

---

### 🟠 2. Média aritmética simples descrita como superestimando sistematicamente

**claim_id:** `GEOEST-M20-A01-VIESMEDIASIMPLES-006` *(alegação nova, levantada pela auditoria)*
**Tipo:** confusão de escopo / omissão que gera erro
**Onde:** a01 · Exemplo trabalhado, item (c)
**Está escrito:** "A média simples superestima sistematicamente o teor médio sempre que amostras curtas e amostras longas não têm teores parecidos (o que é a regra, não a exceção, em depósitos reais)"
**Problema:** a palavra "sistematicamente" está errada. O viés da média não ponderada **acompanha o sinal da correlação entre comprimento da amostra e teor**: superestima quando as amostras curtas são as mais ricas, **subestima** quando são as mais pobres. Palmer (2024) documenta exatamente isso ao comparar furo a furo — em alguns a média aritmética fica acima da composição ponderada, em outros abaixo. Como escrito, a aula ensina uma regra de direção fixa que o aluno aplicaria errado metade das vezes. A observação útil, que a aula perdia, é *por que* o viés para cima é o mais comum: o geólogo tende a isolar em intervalos curtos justamente as zonas estreitas de alto teor, e é esse hábito de amostragem — não uma lei estatística — que produz a assimetria.
**Correção aplicada:** trecho reescrito para nomear a condição do viés (correlação comprimento↔teor), dar as duas direções, e explicar a razão prática do predomínio do viés para cima.
**Fonte:** Palmer, L. W. (2024), "Compositing and regularization of drillhole data for geostatistical resource estimation", *J. South. Afr. Inst. Min. Metall.* 124(6), 331 · Sinclair & Blackwell (2002), cap. 5 · **Nível:** revisada por pares
**Confiança:** confirmado
**Desfecho:** **corrigido**

---

### 🟠 3. Erro de percentual e razão de pesos errada no exemplo trabalhado da a01

**claim_id:** `GEOEST-M20-A01-ARITMETICAEXEMPLO-007` *(alegação nova, levantada pela auditoria)*
**Tipo:** erro factual (aritmética)
**Onde:** a01 · Exemplo trabalhado, item (b)
**Está escrito:** "A média simples (1,58 g/t) é **28% maior** do que a composição ponderada (1,24 g/t)." e "recebe, na média simples, o mesmo peso que os intervalos de 2,0 m — um peso quatro vezes maior do que o comprimento de rocha que ele de fato representa."
**Problema:** **dois erros numéricos numa frase.** (1) $1,5833/1,24375 = 1,273$ — a diferença é de **27%**, não 28%; com os próprios valores arredondados que a aula imprime, $1,58/1,24 = 1,274$, que também dá 27%. Não há arredondamento que produza 28. (2) O fator **4** é a razão entre 2,0 m e 0,5 m, e não a razão entre o peso que a amostra 3 recebe e o peso que lhe caberia. A amostra 3 recebe $1/6 = 16,7\%$ do peso e representa $0,5/8,0 = 6,25\%$ da rocha: recebe **2,7 vezes** mais peso do que lhe cabe. Como a frase está construída ("um peso quatro vezes maior do que o comprimento de rocha que ele de fato representa"), ela afirma a segunda coisa e dá o número da primeira.
**Correção aplicada:** "28%" → "cerca de 27%"; a razão de pesos foi reescrita com as duas frações explícitas (16,7% recebido contra 6,25% devido) e o fator corrigido para 2,7. Registrada alegação nova com a aritmética completa, para que uma auditoria futura não precise refazê-la.
**Fonte:** aritmética verificável a partir da própria tabela do exemplo · **Nível:** cálculo direto
**Confiança:** confirmado
**Desfecho:** **corrigido**

---

### 🟠 4. "Valor de corte alto" como tradução de *high-grade outlier*

**claim_id:** `GEOEST-M20-A01-CAPPING-004`
**Tipo:** erro de nomenclatura / confusão de escopo
**Onde:** a01 · seção "Histograma, boxplot e o problema dos valores extremos"
**Está escrito:** "A prática de recursos minerais chama esse segundo caso de **valor de corte alto (high-grade outlier)**"
**Problema:** **"valor de corte" já é o nome consagrado de outra coisa** — o *cut-off grade*, o limiar **econômico** que separa minério de estéril e que governa a curva teor-tonelagem. Chamar um valor extremo de alto teor de "valor de corte alto" num módulo de geoestatística de recursos minerais, onde o teor de corte vai aparecer de verdade (M21, M42), instala uma colisão terminológica num aluno que ainda não conhece nenhum dos dois termos. Agrava que o mesmo parágrafo fala em "valores acima de um limiar" — o leitor tem todos os elementos para fundir os dois conceitos.
**Correção aplicada:** "valor de corte alto" → "**valor extremo de alto teor** (*high-grade outlier*)", com aposto explícito distinguindo de teor de corte (*cut-off grade*). A alegação `-004` recebeu a nota terminológica.
**Fonte:** Sinclair & Blackwell (2002), *Applied Mineral Inventory Estimation*, cap. 7 (Outliers) · **Nível:** tratado de referência
**Confiança:** confirmado
**Desfecho:** **corrigido**

---

### 🟠 5. "Estatisticamente independentes" onde cabia "logicamente independentes"

**claim_id:** `GEOEST-M20-A01-CORRELACAOESPACIAL-005`
**Tipo:** certeza indevida / erro de terminologia
**Onde:** a01 · bloco de alegações auditáveis (o corpo da aula dizia, mais defensavelmente, "são perguntas independentes")
**Está escrito:** "as duas análises são estatisticamente independentes entre si"
**Problema:** **independência estatística é um termo técnico com significado preciso, e não é isso que se quer dizer.** O que a aula estabelece — e estabelece bem — é que correlação entre variáveis no mesmo ponto e continuidade espacial da mesma variável entre pontos são perguntas **logicamente independentes**: uma não implica nem restringe a outra. Dizer que são "estatisticamente independentes" afirma algo mais forte e falso: num depósito real as duas estruturas costumam estar relacionadas, e explorar essa relação é exatamente o que a **cokrigagem** faz, via variograma cruzado. Deixar a afirmação forte no material bloqueia conceitualmente o M21, que trata de modelagem multivariada.
**Correção aplicada:** alegação reescrita para "logicamente independentes", com a ressalva explícita de que isso não equivale a independência estatística e com o ponteiro para cokrigagem, declarada fora do escopo. O Recap da a01 ganhou a mesma precisão em uma frase.
**Fonte:** Isaaks & Srivastava (1989), caps. 3 e 7 · Goovaerts (1997), cap. 6 (estimativa local com informação secundária) · **Nível:** tratado de referência
**Confiança:** confirmado
**Desfecho:** **corrigido**

---

### 🟠 6. Relação de Krige apresentada como aproximação, e sem o domínio de referência

**claim_id:** `GEOEST-M20-A02-RELACAOKRIGE-003`
**Tipo:** impreciso / omissão que gera erro
**Onde:** a02 · seção "O suporte: por que o mesmo depósito tem variâncias diferentes"
**Está escrito:** "estabelece que a variância de blocos é **aproximadamente igual** à variância de pontos menos a variância 'dentro do bloco'"
**Problema:** **é uma identidade exata, não uma aproximação** — a aditividade das variâncias de dispersão, $D^2(\cdot|D) = D^2(\cdot|v) + D^2(v|D)$, com $D^2(\cdot|v) = \bar\gamma(v,v)$. Chamá-la de aproximação enfraquece exatamente o que o aluno precisa levar: que o efeito de suporte é uma consequência necessária, não um ajuste empírico que se pode dispensar. Agrava que a frase imediatamente seguinte apresenta a equação com sinal de igualdade, de modo que o texto contradiz a si mesmo em duas linhas. Segundo problema, de omissão: a relação só vale **dentro de um mesmo domínio de referência $D$**, e omitir isso é o que abre a porta para o aluno aplicar a subtração entre variâncias medidas em domínios geológicos diferentes.
**Correção aplicada:** "aproximadamente igual" → identidade exata, com o domínio $D$ nomeado e a origem empírica (Krige, Witwatersrand) registrada. A alegação `-003` foi reescrita na notação de variância de dispersão.
**Fonte:** Journel & Huijbregts (1978), cap. II · Isaaks & Srivastava (1989), cap. 19 (Change of Support) · Geostatistics Lessons, *Change of Support and the Volume Variance Relation* · **Nível:** tratado de referência
**Confiança:** confirmado
**Desfecho:** **corrigido**

---

### 🟠 7. O comportamento na origem apresentado como critério para distinguir esférico de exponencial

**claim_id:** `GEOEST-M20-A03-MODELOSTEORICOS-003`
**Tipo:** erro factual / confusão de escopo
**Onde:** a03 · seção "Modelos teóricos"; propagado para o Exemplo trabalhado, para o Recap e para "Ao final você vai conseguir"
**Está escrito:** "um crescimento aproximadamente linear a partir de $h=0$ favorece o esférico; um crescimento mais abrupto, **quase vertical**, favorece o exponencial; uma curvatura suave e horizontal na origem favorece o gaussiano."
**Problema:** **o modelo exponencial é linear na origem, não "quase vertical".** $\gamma(h)=C(1-e^{-3h/a}) \approx 3Ch/a$ para $h$ pequeno — inclinação finita, e exatamente o dobro da do esférico ($1{,}5C/a$) para o mesmo alcance. Os dois modelos têm **o mesmo tipo** de comportamento na origem. O comportamento na origem separa o **gaussiano** — único dos três com tangente horizontal e curvatura parabólica — dos outros dois, e é só isso que ele decide. Apresentá-lo como o critério de escolha entre esférico e exponencial ensina um procedimento que não funciona: diante de um variograma experimental real, o aluno tentaria ler uma diferença que não está lá. O critério que de fato separa os dois é a **forma da aproximação ao patamar** (finita e com quebra nítida no esférico; assintótica e gradual no exponencial) mais a inclinação inicial relativa.
**Agravante — o exemplo trabalhado chegava à resposta certa pelo caminho errado.** A pergunta pedia escolher o modelo "com base no crescimento entre os dois primeiros lags", e a resolução concluía "esférico" a partir de um argumento sobre linearidade na origem que não discrimina. A conclusão está certa, e por sorte os dados **de fato** discriminam — só que por outra via: um exponencial com alcance prático de 120 m preveria $\gamma(20)\approx0{,}27$ contra os 0,18 observados, e continuaria subindo além dos 120 m em vez de travar. Um aluno que reproduzisse o raciocínio da aula em outro conjunto de dados erraria.
**Correção aplicada:** a seção de modelos foi reescrita para consignar a linearidade na origem de esférico **e** exponencial, a inclinação inicial relativa, e a aproximação ao patamar como critério discriminante; o gaussiano ganhou o alcance prático a 95%, que faltava. A pergunta e a resolução do exemplo trabalhado foram refeitas com o argumento correto, incluindo a previsão numérica do exponencial concorrente e a conferência do ajuste esférico ponto a ponto. Recap e "Ao final você vai conseguir" realinhados. Alegação `-003` reescrita com nota datada, e registrada a alegação nova `GEOEST-M20-A03-AJUSTEEXEMPLO-006` com o ajuste verificado.
**Fonte:** Isaaks & Srivastava (1989), cap. 16 · Journel & Huijbregts (1978), cap. III · documentação técnica de variografia (Seequent Leapfrog, Maptek Vulcan, SAS PROC VARIOGRAM), que consigna explicitamente a linearidade na origem de ambos e o alcance prático a 95% para exponencial e gaussiano · **Nível:** tratado de referência + documentação normativa de software
**Confiança:** confirmado
**Desfecho:** **corrigido**

---

### 🟠 8. Raio de busca "entre metade e o alcance total" — inverte a prática documentada

**claim_id:** `GEOEST-M20-A04-RAIOBUSCA-006` *(alegação nova, levantada pela auditoria)*
**Tipo:** erro factual (prática invertida)
**Onde:** a04 · seção "Vizinhança de busca"; propagado para o Recap
**Está escrito:** "tipicamente definida por um raio (ancorado no alcance do variograma, frequentemente um valor **entre metade e o alcance total**)"
**Problema:** **a prática consolidada vai na direção oposta.** O raio de busca é tipicamente **igual ao alcance ou maior**, e com frequência estendido a 1,5–2 vezes o alcance quando a malha é esparsa e o mínimo de amostras não seria atingido de outro modo; buscas em múltiplas passadas com raio crescente são rotina em malha irregular. A razão específica da krigagem ordinária é que amostras **além** do alcance ainda contribuem — não para a estrutura, mas para a estimativa implícita da média local, que é justamente o que a KO faz de diferente da krigagem simples. Recomendar meio alcance produziria vizinhanças sub-informadas, estimativas erráticas e blocos não estimados. Este é um achado de consequência operacional direta: é um parâmetro que o aluno vai digitar num software.
**Correção aplicada:** parágrafo reescrito com a prática correta (raio ≥ alcance, 1,5–2× em malha esparsa), a razão específica da KO, e a menção à busca em múltiplas passadas. Recap realinhado. Alegação nova registrada com nota sobre o que a versão anterior dizia.
**Fonte:** Deutsch, J. L. & Deutsch, C. V., *Quantitative Kriging Neighborhood Analysis (QKNA)* e *Introduction to Choosing a Kriging Plan*, Geostatistics Lessons (consultados em 2026-09-18) · Isaaks & Srivastava (1989), cap. 14 (Search Strategy) · **Nível:** referência técnica aplicada + tratado
**Confiança:** confirmado
**Desfecho:** **corrigido**

---

### 🟠 9. Sistema de krigagem descrito como "indeterminado" com poucas amostras

**claim_id:** `GEOEST-M20-A04-ESTABILIDADESISTEMA-008` *(alegação nova, levantada pela auditoria)*
**Tipo:** erro factual
**Onde:** a04 · seção "Vizinhança de busca"
**Está escrito:** "Um número mínimo de amostras evita estimativas baseadas em pouquíssima informação (e o sistema de krigagem se torna numericamente instável, ou mesmo **indeterminado**, com poucas amostras)"
**Problema:** o sistema de krigagem ordinária **não fica indeterminado por escassez de amostras**. Com uma única amostra, a restrição $\sum\lambda_i=1$ já determina $\lambda_1=1$ e o sistema é resolvido. A justificativa para exigir um número mínimo é de **qualidade de estimativa** — estimativas erráticas, sem controle local, sem suavização — e não de solubilidade. A instabilidade numérica genuína tem outra origem: amostras muito próximas ou coincidentes na vizinhança, que tornam a matriz do sistema quase singular (e, no caso do gaussiano, o comportamento parabólico na origem com pepita nulo, já mencionado na a03). Como escrito, o texto atribui ao número de amostras um efeito que pertence à **configuração** delas.
**Correção aplicada:** trecho reescrito separando as duas coisas — o mínimo de amostras existe por qualidade de estimativa; a instabilidade numérica vem de amostras quase coincidentes. Alegação nova registrada.
**Fonte:** Isaaks & Srivastava (1989), caps. 12 e 14 · Geostatistics Lessons, *Introduction to Choosing a Kriging Plan* · **Nível:** tratado de referência
**Confiança:** confirmado
**Desfecho:** **corrigido**

---

### 🟡 10. Arredondamento inconsistente dos pesos de krigagem

**claim_id:** `GEOEST-M20-A04-ARREDONDAMENTOPESOS-007` *(alegação nova, levantada pela auditoria)*
**Tipo:** valor apresentado incorretamente
**Onde:** a04 · Exemplo trabalhado
**Está escrito:** "$\lambda_1 \approx 0,813$ e $\lambda_2 \approx 0,187$"
**Problema:** os valores exatos são $\lambda_1 = 0,8125$ e $\lambda_2 = 0,1875$. Arredondados para três casas dariam 0,813 e **0,188** — 0,187 não é o arredondamento de 0,1875. A aula escolheu 0,187 para que a soma fechasse em 1,000, o que é compreensível mas cria um número que não é nem exato nem corretamente arredondado, justo numa aula em que a soma unitária dos pesos é o conceito em jogo. O aluno que refizesse a conta encontraria 0,1875 e não saberia se errou.
**Correção aplicada:** exemplo passou a usar os valores exatos 0,8125 e 0,1875, com nota explicando o arredondamento. A estimativa e a variância de krigagem foram recalculadas com eles ($1,625+0,263=1,89\%$; $\sigma^2_{KO}=0,833$). Alegação nova registrada com a verificação numérica completa.
**Fonte:** cálculo direto, verificado contra a fórmula do modelo esférico e o sistema de krigagem ordinária · **Nível:** cálculo direto
**Confiança:** confirmado
**Desfecho:** **corrigido**

---

### 🟡 11 a 17. Atribuição de capítulo errada — sete ocorrências, quatro obras

Sete achados de mesma natureza, agrupados porque a correção é a mesma operação: o **livro** citado é o certo, o **capítulo** não. A tabela de conteúdos de cada obra foi conferida contra fonte bibliográfica. Todos **corrigidos**, nas listas de Fontes e nos blocos de alegações.

| # | claim_id | Obra | Estava | Correto | Onde |
|---|---|---|---|---|---|
| 11 | `GEOEST-M20-FONTES-ISAAKS-A01-010` | Isaaks & Srivastava (1989) | caps. 2 e 4, "tratamento de outliers"; alegação `-005` citando caps. 2 e 5 | cap. 2 (Univariate Description) e cap. 3 (Bivariate Description); alegação `-005` → caps. 3 e 7 | a01 |
| 12 | `GEOEST-M20-FONTES-SINCLAIR-A01-011` | Sinclair & Blackwell (2002) | cap. 3, "compositing e estatística descritiva" | cap. 3 é **Continuity**. Compositing → cap. 5 (Data and Data Quality); estatística descritiva/CV → caps. 4 e 6; outliers/capping → cap. 7 | a01 |
| 13 | `GEOEST-M20-FONTES-ISAAKS-A02-012` | Isaaks & Srivastava (1989) | caps. 4 e 9 | cap. 9 (Random Function Models) e cap. **19** (Change of Support) — cap. 4 é Spatial Description e não trata de efeito de suporte | a02 |
| 14 | `GEOEST-M20-FONTES-JOURNEL-A02-013` | Journel & Huijbregts (1978) | cap. III, "hipótese intrínseca e relação de Krige" | cap. **II** (The Theory of Regionalized Variables) — é ali que estão a hipótese intrínseca e as variâncias de dispersão; o cap. III é análise estrutural | a02 |
| 15 | `GEOEST-M20-FONTES-ISAAKS-A03-014` | Isaaks & Srivastava (1989) | caps. 5, 6 e 7 | cap. 7 (variograma experimental, direcionais) e cap. **16** (Modelling the Sample Variogram: modelos permissíveis, anisotropia) — caps. 5 e 6 descrevem os conjuntos de dados do livro | a03 |
| 16 | `GEOEST-M20-FONTES-ISAAKS-A04-015` | Isaaks & Srivastava (1989) | "caps. 12 (krigagem simples) e 13 (krigagem ordinária)" | cap. 12 é **Ordinary Kriging**, 13 é **Block Kriging**; acrescentados 14 (Search Strategy) e 15 (Cross Validation), que a aula usa e não citava | a04 |
| 17 | `GEOEST-M20-FONTES-GOOVAERTS-A04-016` | Goovaerts (1997) | caps. 5 e 6, "validação cruzada" | cap. 5 (Local Estimation: Accounting for a Single Attribute) cobre KS, KO, vizinhança e validação cruzada; o cap. 6 é informação **secundária** (cokrigagem) e não trata de validação cruzada | a04 |

**Fonte da verificação:** sumários bibliográficos conferidos de Isaaks & Srivastava (1989, OUP, 561 p.), Journel & Huijbregts (1978, Academic Press), Goovaerts (1997, OUP, 483 p.) e Sinclair & Blackwell (2002, Cambridge, 381 p.) · **Confiança:** confirmado

---

## Verificado e correto

Vinte e uma alegações foram checadas e **passaram sem alteração**. As de maior risco:

| # | Aula | Alegação | Fonte da verificação |
|---|---|---|---|
| B1 | a01 | Fórmula da composição ponderada por comprimento e o fato de que compositar em comprimento maior reduz a variância (primeira manifestação do efeito de suporte) | Sinclair & Blackwell (2002) cap. 5; Palmer (2024) |
| B2 | a01 | CV acima de ~1 a 2 como sinal de alerta de distribuição fortemente assimétrica | Confirmado como heurística; literatura de veios de ouro com forte pepita documenta CV > 20, o que **reforça** a natureza orientativa do limiar — nota acrescentada à alegação |
| B3 | a01 | Tendência lognormal dos teores de metais preciosos | Journel & Huijbregts (1978) cap. II |
| B4 | a01 | Capeamento (não exclusão) como tratamento padrão de extremo genuíno; percentil 99 ou inflexão da curva de metal acumulado | Sinclair & Blackwell (2002) cap. 7 |
| B5 | a01 | Limiar de 1,5 × amplitude interquartil no boxplot; fórmulas de variância amostral ($n-1$) e de $r$ de Pearson | Convenção de Tukey; fórmulas conferidas |
| B6 | a02 | Matheron formaliza a variável regionalizada nos anos 1960 a partir do trabalho empírico de D. G. Krige na mineração de ouro sul-africana | Matheron (1963), *Economic Geology* 58(8), 1246-1266 — **citação conferida em volume, número e paginação** |
| B7 | a02 | Estacionariedade de segunda ordem: $E[Z(x)]=m$ constante e $Cov$ dependente só de $h$, com $C(0)=\sigma^2$ | Journel & Huijbregts (1978) cap. II |
| B8 | a02 | Segunda ordem ⟹ intrínseca, e a recíproca é falsa | Confirmado (a *razão* estava errada — 🔴 1 — mas a relação de força, não) |
| B9 | a02 | Anisotropia geométrica (mesmo patamar, alcance variável, transformação elíptica) versus zonal (patamar variável) | Isaaks & Srivastava (1989) caps. 7 e 16 |
| B10 | a02 | **Exemplo trabalhado, aritmética:** $4,0-1,5=2,5$ (62,5% de 4,0); $1,2-0,3=0,9$ (75% de 1,2); redução relativa maior na Área 1 | Recalculado — **fecha** |
| B11 | a02 | Ignorar o efeito de suporte superestima a proporção de blocos de teor extremo (alto **e** baixo) | Isaaks & Srivastava (1989) cap. 19 |
| B12 | a03 | Fórmula do variograma experimental; lags, tolerância de distância e tolerância angular; efeito de tolerâncias estreitas/largas | Isaaks & Srivastava (1989) cap. 7; Clark (1979) cap. 2 |
| B13 | a03 | Efeito pepita como soma não separável de variabilidade real de curtíssima escala e erro de amostragem/análise; origem do nome | Journel & Huijbregts (1978) cap. III |
| B14 | a03 | Patamar igual à variância a priori sob estacionariedade de segunda ordem; alcance como distância além da qual não há informação espacial mútua | Isaaks & Srivastava (1989) caps. 7 e 16 |
| B15 | a03 | Alcance prático do exponencial a 95% do patamar | Confirmado — e estendido ao gaussiano, que a aula omitia |
| B16 | a03 | Direcionais a cada 22,5° ou 30° cobrindo 180°, por equivalência entre $h$ e $-h$ | Isaaks & Srivastava (1989) cap. 7 |
| B17 | a03 | **Exemplo trabalhado, ajuste:** pepita ~0,04–0,06 por extrapolação dos dois primeiros lags; patamar 0,60 batendo com a variância a priori; alcance ~120 m | Refeito. O modelo esférico $C_0=0,05$, $C_1=0,55$, $a=120$ prevê 0,19 / 0,32 / 0,43 / 0,52 / 0,58 contra os observados 0,18 / 0,32 / 0,44 / 0,52 / 0,58 — **ajuste excelente, exemplo bem construído** |
| B18 | a04 | Propriedade BLUE: não-viés + variância mínima do erro dentro da classe dos estimadores lineares não-viesados, com a ressalva explícita de que não garante acerto em cada caso individual | Journel & Huijbregts (1978) cap. V |
| B19 | a04 | Sistema de KS em covariância sem restrição de soma; $C(h)=C(0)-\gamma(h)$; pesos somando menos de 1 puxam a estimativa para $m$ | Isaaks & Srivastava (1989) cap. 12 |
| B20 | a04 | Sistema de KO em variograma com multiplicador de Lagrange; $\sigma^2_{KO}=\sum\lambda_i\gamma(x_i,x_0)+\mu$; variância de krigagem independente dos valores observados e mapeável antes dos teores | Isaaks & Srivastava (1989) cap. 12; Journel & Huijbregts (1978) cap. V |
| B21 | a04 | **Exemplo trabalhado, aritmética completa:** $\gamma(30)=0,4365$; $\gamma(40)=0,568$; $\gamma(60)=0,792$ pelo modelo esférico $C=1,0$, $a=100$, pepita nula; $\lambda_1-\lambda_2=0,355/0,568=0,625$; $\mu=0,3305$; $z^*=1,8875\%$; $\sigma^2_{KO}=0,833$ | Recalculado do zero — **fecha em todos os passos** (salvo o arredondamento do 🟡 10) |

Também verificados e corretos: krigagem de bloco usando $\bar\gamma(x_i,v)$ por discretização e produzindo variância menor que a krigagem de ponto; divisão da vizinhança em quadrantes/octantes contra agrupamento direcional; validação cruzada *leave-one-out* com erro médio ≈ 0 e variância do erro padronizado ≈ 1, e a ressalva de que ela checa consistência interna e não correção do modelo.

---

## Verificação transversal

Verificação explícita contra o **M13 (geoprocessamento)**, pré-requisito declarado, e contra o **M15 (petrofísica)** e o **M19**, que tocam tratamento estatístico de dado geofísico. **Nenhuma contradição encontrada.** O M20 não repete nenhum valor numérico já fixado em módulo fechado.

Ponto de atenção para adiante, registrado e **não** tratado como achado: o **M21 (modelagem geoestatística de depósitos minerais)** e o **M42 (exploração mineral e avaliação de recursos)** ainda não têm aulas escritas, e três decisões terminológicas deste módulo precisam ser herdadas por eles sem divergência — (a) **valor extremo de alto teor** ≠ **teor de corte**; (b) a hipótese intrínseca **não** acomoda deriva, que é assunto de quase-estacionariedade / krigagem universal; (c) a relação de Krige é identidade exata dentro de um domínio $D$.

---

## Correções aplicadas

**Aplicadas em:** 2026-09-18

| claim_id | Sev. | Desfecho | Arquivos alterados |
|---|---|---|---|
| `GEOEST-M20-A02-HIPOTESEINTRINSECA-002` | 🔴 | Corrigido | aula-02 (corpo, recap, alegação) |
| `GEOEST-M20-A01-VIESMEDIASIMPLES-006` | 🟠 | Corrigido | aula-01 (exemplo trabalhado, alegação nova) |
| `GEOEST-M20-A01-ARITMETICAEXEMPLO-007` | 🟠 | Corrigido | aula-01 (exemplo trabalhado, alegação nova) |
| `GEOEST-M20-A01-CAPPING-004` | 🟠 | Corrigido | aula-01 (corpo, alegação) |
| `GEOEST-M20-A01-CORRELACAOESPACIAL-005` | 🟠 | Corrigido | aula-01 (recap, alegação) |
| `GEOEST-M20-A02-RELACAOKRIGE-003` | 🟠 | Corrigido | aula-02 (corpo, alegação) |
| `GEOEST-M20-A03-MODELOSTEORICOS-003` | 🟠 | Corrigido | aula-03 (corpo, pergunta e resolução do exemplo, recap, cabeçalho, alegação) |
| `GEOEST-M20-A04-RAIOBUSCA-006` | 🟠 | Corrigido | aula-04 (corpo, recap, alegação nova) |
| `GEOEST-M20-A04-ESTABILIDADESISTEMA-008` | 🟠 | Corrigido | aula-04 (corpo, alegação nova) |
| `GEOEST-M20-A04-ARREDONDAMENTOPESOS-007` | 🟡 | Corrigido | aula-04 (exemplo trabalhado, alegação nova) |
| `GEOEST-M20-FONTES-ISAAKS-A01-010` | 🟡 | Corrigido | aula-01 (Fontes, alegação `-005`) |
| `GEOEST-M20-FONTES-SINCLAIR-A01-011` | 🟡 | Corrigido | aula-01 (Fontes, alegações `-001`, `-002`, `-004`) |
| `GEOEST-M20-FONTES-ISAAKS-A02-012` | 🟡 | Corrigido | aula-02 (Fontes, alegações `-002`, `-003`, `-004`) |
| `GEOEST-M20-FONTES-JOURNEL-A02-013` | 🟡 | Corrigido | aula-02 (Fontes, alegações `-002`, `-003`) |
| `GEOEST-M20-FONTES-ISAAKS-A03-014` | 🟡 | Corrigido | aula-03 (Fontes, alegações `-001`, `-002`, `-003`, `-004`, `-005`) |
| `GEOEST-M20-FONTES-ISAAKS-A04-015` | 🟡 | Corrigido | aula-04 (Fontes, alegação `-002`) |
| `GEOEST-M20-FONTES-GOOVAERTS-A04-016` | 🟡 | Corrigido | aula-04 (Fontes, alegações `-002`, `-005`) |

**Fontes acrescentadas ao módulo** (não estavam em nenhuma aula e sustentam correções): Palmer (2024), *J. South. Afr. Inst. Min. Metall.* 124(6), 331; Chilès & Delfiner (2012), *Geostatistics: Modeling Spatial Uncertainty*, 2ª ed., Wiley; Deutsch & Deutsch, *QKNA* e *Introduction to Choosing a Kriging Plan*, Geostatistics Lessons.

**Pendências:** nenhuma. **0 vermelhos e 0 laranjas em aberto.**

**Material derivado:** o módulo **não tinha** questionário, baralho de flashcards nem glossário quando as correções foram aplicadas. Não há nada a propagar e **nenhum card no Anki a corrigir à mão** — esta era a melhor hora possível para corrigir, e em particular a inversão conceitual da hipótese intrínseca não chegou a virar gabarito.

---

## Gate de avaliação

**Status: LIBERADO** para `gerador-de-questionarios` e `gerador-de-flashcards`, em 2026-09-18.

0 achados vermelhos e 0 laranjas em aberto; nenhum achado branco; nenhuma controvérsia real da literatura apresentada como resolvida.

### Restrições para a avaliação

1. **O limiar de CV (~1 a 2) não é constante.** Cobrar o *significado* de um CV alto (assimetria forte, média frágil, necessidade de capeamento ou método não linear), **nunca o número como valor a memorizar**. Depósitos de ouro com forte efeito pepita têm CV bem acima de 2.
2. **A razão pepita/patamar não tem limiares universais.** Cobrar a direção da leitura (razão menor = mais estrutura espacial = interpolação mais confiável), não faixas numéricas.
3. **Comprimento de composição e raio de busca são decisões de projeto, não fórmulas.** Cobrar o critério (altura de bancada / comprimento amostral modal; raio ≥ alcance), não um valor.
4. **Não cobrar krigagem universal, IRF-$k$, cokrigagem nem métodos não lineares** como conteúdo — os quatro aparecem no módulo apenas como ponteiros declarados fora do escopo.

### Avisos ao gerador de questionários e de flashcards

Dez pontos mudaram nesta auditoria. **Gerar item a partir da versão anterior das aulas produz gabarito errado.** Os de maior valor:

1. **O par de discriminação mais valioso do módulo é "variância não limitada" × "deriva".** A hipótese intrínseca é mais fraca que a estacionariedade de segunda ordem porque **dispensa variância a priori finita** — não porque tolera deriva. "Tolera deriva" é o **distrator perfeito**, porque é exatamente o que circula na literatura aplicada e o que o senso comum sugere. Prefira questão de discriminação a definição isolada. **Não gerar card nem gabarito que diga que a hipótese intrínseca acomoda deriva** — foi esse o erro vermelho corrigido.
2. **Segundo par de alto valor: comportamento na origem.** Esférico e exponencial são **ambos lineares** na origem; só o gaussiano é parabólico. O que separa esférico de exponencial é a **aproximação ao patamar** (finita com quebra nítida × assintótica). O distrator natural é "o exponencial sobe quase vertical na origem" — era o que a aula dizia.
3. **Terceiro: direção do viés da média não ponderada.** Não é sistemático para cima; segue o sinal da correlação comprimento↔teor. O viés para cima predomina por um motivo de prática de amostragem, não por lei estatística.
4. **Não gerar item que trate a relação de Krige como aproximação** — é identidade exata, dentro de um mesmo domínio $D$.
5. **Não gerar item que recomende raio de busca menor que o alcance** — a prática é ≥ alcance, frequentemente 1,5–2×.
6. **Não gerar item que diga que o sistema de krigagem fica indeterminado com poucas amostras** — ele é solúvel até com uma.
7. **Terminologia:** usar **valor extremo de alto teor** para *high-grade outlier*. **"Valor de corte" está reservado ao cut-off grade** e um item que os confunda é um erro que este módulo acabou de corrigir.
8. **"Logicamente independentes", não "estatisticamente independentes"**, para a relação entre correlação no ponto e continuidade espacial.
9. **Os quatro exemplos trabalhados são todos aritméticos e todos conferidos** — são base segura para questão de aplicação. Valores canônicos: composição 1,24 g/t contra média simples 1,58 g/t (a01); $\sigma^2_{bloco}$ 2,5 e 0,9 (a02); esférico $C_0=0,05$, $C_1=0,55$, $a=120$ m (a03); $\lambda_1=0,8125$, $\lambda_2=0,1875$, $z^*=1,89\%$, $\sigma^2_{KO}=0,833$ (a04).
10. **A variância de krigagem não depende dos valores observados** — é dos pontos mais contraintuitivos e mais bem estabelecidos do módulo, excelente para verdadeiro/falso.

### Recomendação de formato do questionário

**Questionário único, sem parciais.** O módulo tem **4 aulas**, abaixo do limiar de ~5–6 do plugin a partir do qual se dividem parciais. Além do número, dois fatores reforçam: (a) o módulo tem **um único fio condutor linear** — cada aula é insumo direto da seguinte (dados → modelo de função aleatória → variograma → krigagem), de modo que não existe corte conceitual natural que não parta a cadeia ao meio; (b) a correspondência aula↔objetivo é **1:1** (a01→oa01, a02→oa02, a03→oa03, a04→oa04), sem agrupamento que sugira fronteira de parcial. Um questionário único cumulativo cobre os quatro objetivos e, mais importante, permite as questões de **integração entre aulas** — que são as de maior valor aqui, porque o módulo inteiro é uma cadeia de dependências.

Comparação com os módulos vizinhos: o M19 (7 aulas) usou 3 parciais + final; o M17 (6 aulas) usou questionário único. O M20, com 4, fica claramente do lado do único.

---

## Observações fora de escopo (para o `revisor-didatico`)

1. **a02 — sobrecarga criada pela própria correção vermelha.** A correção da hipótese intrínseca acrescentou dois parágrafos densos a uma seção que já era a mais abstrata do módulo, e introduziu quatro termos novos (quase-estacionariedade, vizinhança móvel, krigagem universal, IRF-$k$) numa aula que já carregava função aleatória, realização, estacionariedade de segunda ordem, hipótese intrínseca, suporte, relação de Krige e anisotropia. **O conteúdo está certo; a forma pede intervenção.** Esta é a seção a olhar primeiro.
2. **a02 é a aula mais pesada do módulo** mesmo antes da correção — é a única inteiramente conceitual, sem apoio numérico até o exemplo final, e introduz mais conceitos novos que qualquer outra. Candidata natural a divisão em Parte 1 / Parte 2 pela convenção dos módulos 17 e 19.
3. **a03 — erro de digitação:** em "Alcance (range, $a$) — a distância na qual o variograma atinge (ou se aproxima assintoticamente d)o patamar", o parêntese está fechado no lugar errado. Deveria ser "(ou se aproxima assintoticamente do) patamar".
4. **a03 — o exemplo trabalhado ficou mais longo** com a correção do 🟠 7, que acrescentou a comparação com o exponencial e a conferência ponto a ponto do ajuste. Vale checar se o ganho de rigor não custou fluidez.
5. **a04 — a seção "Vizinhança de busca" cresceu** com as correções dos 🟠 8 e 🟠 9 e virou o parágrafo mais denso da aula, acumulando raio, múltiplas passadas, mínimo/máximo de amostras, instabilidade numérica e setorização. Pede quebra.
6. **Termos técnicos usados antes de definidos:** a a01 menciona "estacionariedade" (na discussão de histograma bimodal) e "efeito de suporte" antes de a a02 os definir; a a02 usa $\bar\gamma(v,v)$ "calculada a partir do modelo de variograma da Aula 03", que ainda não existe. São *forward references* declaradas, não erros — mas o revisor deve julgar se o aluno consegue seguir.
