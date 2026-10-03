# Questionário — Módulo 20: Introdução à geoestatística (cumulativo)

**Cobre:** as 5 aulas do módulo (Aula 01 — preparação de dados; Aula 02 — variáveis regionalizadas e estacionariedade; Aula 03 — suporte, relação de Krige e anisotropia; Aula 04 — o variograma; Aula 05 — krigagem simples e ordinária)
**Objetivos:** `geologia-avancado-m20-oa01` a `oa04` — note que `oa02` é coberto em conjunto pelas Aulas 02 e 03, tratadas aqui como unidade.
**Formato:** questionário único cumulativo, sem parciais (módulo com 5 aulas, fio condutor linear — ver recomendação no hub do módulo). 20 questões, misturando múltipla escolha, verdadeiro/falso com justificativa, dissertativa curta e aplicação/cálculo. Questões 10, 15 e 20 são de integração explícita entre aulas.

Responda antes de abrir o gabarito.

## Questões

**1. (Múltipla escolha — Aula 01)** Um conjunto de teores de ouro tem coeficiente de variação (CV) igual a 2,3. O que essa informação, isoladamente, permite concluir?
- a) O teor máximo do conjunto é necessariamente mais de duas vezes a média.
- b) A distribuição provavelmente é fortemente assimétrica, dominada por poucos valores altos, e merece cuidado adicional na estimativa (capeamento, transformação de dados ou método não linear).
- c) O depósito não pode ser estimado por krigagem ordinária.
- d) A distribuição é necessariamente lognormal.
- e) O efeito pepita do variograma será, necessariamente, alto.

**2. (V/F — justifique — Aula 01)** "Se duas variáveis medidas no mesmo ponto (por exemplo, Au e Ag na mesma amostra) têm correlação de Pearson próxima de zero, isso implica que nenhuma das duas tem continuidade espacial entre pontos vizinhos."

**3. (Dissertativa curta — Aula 01)** Um colega, ao ver um valor extremamente alto de teor no meio de um conjunto de compostas, propõe simplesmente excluí-lo do banco de dados antes de calcular a estatística descritiva. Explique por que essa não é a prática recomendada quando o valor é uma saca de alto teor genuína (não um erro de amostra ou de laboratório), qual é o tratamento padrão nesse caso, e por que o nome desse tratamento não deve ser confundido com "teor de corte".

**4. (Aplicação/cálculo — Aula 01)** Um furo foi amostrado em quatro intervalos:

| Amostra | Comprimento (m) | Au (g/t) |
|---|---|---|
| 1 | 0,4 | 6,0 |
| 2 | 1,2 | 1,0 |
| 3 | 0,6 | 3,5 |
| 4 | 1,8 | 0,8 |

Calcule (a) a composição ponderada por comprimento de Au para o furo inteiro (4,0 m); (b) a média aritmética simples; (c) de quantas vezes a mais (ou a menos) do que lhe cabe é o peso que a amostra 1 recebe na média simples, comparado ao peso que ela deveria ter.

**5. (Múltipla escolha — Aula 02)** A hipótese intrínseca é mais fraca do que a estacionariedade de segunda ordem. Em que consiste exatamente essa folga?
- a) A hipótese intrínseca tolera uma deriva (tendência sistemática) na média, que a estacionariedade de segunda ordem não tolera.
- b) A hipótese intrínseca dispensa a exigência de que a variância a priori (e, portanto, a função de covariância $C(h)$) seja finita e bem definida — mas continua exigindo média constante.
- c) A hipótese intrínseca não exige que a média seja constante no espaço.
- d) A hipótese intrínseca só vale para variogramas com patamar.
- e) Não há diferença prática entre as duas; a distinção é apenas histórica.

**6. (V/F — justifique — Aula 02)** "Como a hipótese intrínseca é mais fraca (aceita mais casos) do que a estacionariedade de segunda ordem, um conjunto de dados com deriva regional satisfaz pelo menos a hipótese intrínseca."

**7. (Aplicação — Aula 02)** As compostas de um depósito de zinco mostram, num mapa de contorno de teor, um crescimento regular e contínuo do teor médio de sudoeste para nordeste ao longo de toda a área — sem nenhum trecho em que a média pareça estabilizar. (a) Essa observação, isoladamente, já permite descartar alguma das duas hipóteses de estacionariedade? Qual, e por quê? (b) Que estratégia prática (dentro do escopo deste módulo) permite ainda assim estimar valores por krigagem nesse depósito?

**8. (Múltipla escolha — Aula 03)** A relação de Krige, $\sigma^2_{ponto} = \sigma^2_{bloco} + \bar\gamma(v,v)$, é:
- a) Uma aproximação empírica, válida apenas quando a distribuição é aproximadamente normal.
- b) Uma identidade exata de aditividade de variâncias de dispersão, válida dentro de um mesmo domínio geológico de referência $D$.
- c) Uma fórmula que só vale quando a anisotropia é geométrica.
- d) Uma aproximação exata apenas para o modelo de variograma gaussiano.
- e) Válida somente quando o efeito pepita é nulo.

**9. (Dissertativa curta — Aula 03)** Explique a diferença entre anisotropia geométrica e anisotropia zonal, dizendo especificamente qual parâmetro do variograma (patamar ou alcance) varia com a direção em cada caso, e dê um exemplo geológico plausível de cada uma.

**10. (Integração — Aulas 02 e 03)** A relação de Krige, como apresentada na Aula 03, decompõe a variância **total** de um conjunto de dados pontuais ($\sigma^2_{ponto}$) em variância de bloco mais variância dentro do bloco. Essa decomposição pressupõe implicitamente que $\sigma^2_{ponto}$ seja uma quantidade finita e bem definida. Retomando a distinção da Aula 02: em qual das duas hipóteses de estacionariedade essa condição está garantida, e em qual ela pode falhar? O que isso implica sobre a aplicabilidade direta da relação de Krige, na forma como foi apresentada, a um depósito cujo variograma sobe sem atingir patamar?

**11. (Múltipla escolha — Aula 04)** Qual afirmação sobre o comportamento dos modelos teóricos de variograma **muito próximo à origem** ($h\to0$) está correta?
- a) O esférico é aproximadamente linear na origem; o exponencial cresce quase verticalmente; por isso a inclinação inicial separa os dois.
- b) Esférico e exponencial são ambos aproximadamente lineares na origem (o exponencial com inclinação inicial maior); só o modelo gaussiano tem comportamento parabólico (tangente horizontal) na origem.
- c) Os três modelos — esférico, exponencial e gaussiano — têm exatamente o mesmo comportamento na origem.
- d) O gaussiano é linear na origem; esférico e exponencial são parabólicos.
- e) O comportamento na origem não permite distinguir nenhum dos três modelos entre si.

**12. (V/F — justifique — Aula 04)** "O efeito pepita de um variograma reflete exclusivamente erro de amostragem e de análise laboratorial; um efeito pepita alto sempre significa que o laboratório está cometendo erros."

**13. (Aplicação — Aula 04)** Dois variogramas experimentais foram calculados para dois depósitos diferentes, ambos com o mesmo alcance aparente de aproximadamente 90 m:
- **Depósito X:** os valores sobem de forma regular até ~90 m e então ficam praticamente constantes (uma quebra nítida de inclinação logo depois dos 90 m).
- **Depósito Y:** os valores sobem rapidamente nos primeiros lags, depois desaceleram e continuam subindo muito devagar mesmo além dos 90 m, sem nunca "travar" completamente — por isso o alcance de 90 m foi definido como o ponto em que a curva atinge 95% do patamar.

Para cada depósito, diga qual modelo teórico (esférico, exponencial ou gaussiano) melhor descreve o comportamento observado, e justifique pela forma de aproximação ao patamar — não pelo comportamento na origem.

**14. (Dissertativa curta — Aula 04)** Explique o que representa o alcance de um variograma, em termos de continuidade espacial, e diga qual decisão prática de krigagem (desenvolvida na Aula 05) ele ancora diretamente.

**15. (Integração — Aulas 01 e 04)** A Aula 01 introduziu o coeficiente de variação (CV) como um indicador informal de dispersão da distribuição de teores. A Aula 04 introduziu a razão pepita/patamar ($C_0/(C_0+C_1)$) como um indicador informal da qualidade da continuidade espacial. Em que sentido essas duas razões são parecidas do ponto de vista de como devem ser usadas numa avaliação (o que cobrar delas e o que não cobrar)? Cite explicitamente o cuidado que vale para as duas.

**16. (Múltipla escolha — Aula 05)** Qual é a diferença fundamental entre krigagem simples (KS) e krigagem ordinária (KO)?
- a) A KS usa o modelo de variograma; a KO usa apenas a distância entre amostras.
- b) A KS assume uma média global conhecida e constante, sem restrição sobre a soma dos pesos; a KO assume apenas média local constante (desconhecida), impondo que os pesos somem exatamente 1.
- c) A KO só pode ser usada para krigagem de bloco; a KS só para krigagem de ponto.
- d) A KS sempre produz variância de krigagem menor que a KO.
- e) A diferença é apenas terminológica; os dois sistemas de equações são idênticos.

**17. (V/F — justifique — Aula 05)** "A variância de krigagem ordinária calculada para um ponto depende dos teores observados nas amostras vizinhas: quanto mais altos os teores, maior a variância de krigagem."

**18. (Aplicação/cálculo — Aula 05)** O modelo de variograma esférico ajustado para um depósito tem patamar $C=1,0$ (%)², efeito pepita nulo e alcance $a=100$ m — o mesmo modelo do exemplo trabalhado da Aula 05, para o qual já se sabe que $\gamma(30)=0,437$, $\gamma(60)=0,792$ e $\gamma(40)=0,568$. Duas amostras estão na vizinhança de um ponto $x_0$, nas mesmas posições do exemplo da aula ($h_1=30$ m, $h_2=60$ m, $h_{12}=40$ m), mas agora com teores $z_1=3,0\%$ e $z_2=1,0\%$. (a) Sem refazer o sistema do zero, diga o que se pode reaproveitar diretamente do exemplo da aula, e por quê. (b) Calcule a estimativa $z^*(x_0)$. (c) Qual é a variância de krigagem, e por que ela não muda em relação ao exemplo original da aula, mesmo com $z_1$ e $z_2$ diferentes?

**19. (Dissertativa curta — Aula 05)** Um colega dimensiona a vizinhança de busca de um modelo de krigagem usando um raio igual à metade do alcance do variograma, argumentando que assim garante que só entrem amostras "bem correlacionadas". Explique por que essa prática está invertida em relação ao que a literatura documenta, qual é o raio tipicamente recomendado, e por que a krigagem ordinária (especificamente) se beneficia de incluir amostras além do alcance.

**20. (Integração — Aulas 02, 04 e 05)** Um depósito de níquel laterítico apresenta deriva regional clara — o teor médio de Ni cresce de forma sistemática da base para o topo do perfil de intemperismo, documentada em todos os furos. Um geólogo júnior propõe o seguinte fluxo de trabalho: (1) ignorar a deriva porque "a hipótese intrínseca é mais fraca e deve dar conta dela"; (2) ajustar um modelo esférico ao variograma calculado sobre o depósito inteiro; (3) estimar por krigagem ordinária com um raio de busca de metade do alcance ajustado, "para não incluir amostras da parte de baixo teor". Aponte o erro conceitual em cada uma das três etapas, citando a aula e o conceito correto de cada correção.

---

## Gabarito comentado

<details><summary>Ver respostas</summary>

**1.** Resposta: **b)**. Um CV acima de ~1–2 é heurística de alerta para assimetria forte e média frágil — não um valor exato a memorizar, e não garante nenhuma das outras afirmações. (a) é falsa: CV não limita o valor máximo dessa forma. (c) é falsa: CV alto não impede krigagem, apenas pede cuidado adicional (capeamento, transformação, método não linear). (d) é falsa: CV alto é compatível com lognormal, mas não a implica. (e) é falsa: CV descreve a distribuição de teores, não diretamente o efeito pepita do variograma — são medidas de coisas diferentes (dispersão global × descontinuidade de curta escala).

**2.** **Falso.** Correlação entre duas variáveis diferentes no mesmo ponto (o que a Pearson mede) e continuidade espacial da mesma variável entre pontos diferentes (o que o variograma mede) são perguntas **logicamente independentes** — uma não implica nem restringe a outra. Um CV de correlação próximo de zero entre Au e Ag no mesmo ponto não diz nada sobre se o Au (ou a Ag) tem ou não continuidade espacial entre furos vizinhos. Note que "logicamente independentes" não é o mesmo que "estatisticamente independentes": num depósito real as duas estruturas podem estar relacionadas, e explorar essa relação é objeto da cokrigagem (fora do escopo deste módulo).

**3.** Excluir o valor subestimaria o metal contido, porque o valor existe fisicamente na rocha. O tratamento padrão é o **capeamento** (*capping*/*top-cutting*): substituir os valores acima de um limiar estatisticamente definido (por exemplo, percentil 99, ou o ponto de inflexão da curva de metal contido acumulado) pelo próprio valor do limiar — preserva a contagem de amostras e limita a influência desproporcional sobre média e variograma, sem descartar a informação de que ali existe um valor alto. O termo correto é **valor extremo de alto teor** (*high-grade outlier*); "teor de corte" (*cut-off grade*) é um conceito totalmente diferente — o limiar **econômico** que separa minério de estéril na curva teor-tonelagem — e confundir os dois é um erro terminológico específico deste módulo.

**4.** (a) Comprimento total = 0,4+1,2+0,6+1,8 = 4,0 m. Soma ponderada = (6,0×0,4)+(1,0×1,2)+(3,5×0,6)+(0,8×1,8) = 2,4+1,2+2,1+1,44 = 7,14. Composição ponderada = 7,14/4,0 = **1,785 g/t**. (b) Média simples = (6,0+1,0+3,5+0,8)/4 = 11,3/4 = **2,825 g/t** — cerca de 58% maior que a composição ponderada, puxada pela amostra 1 (curta e rica). (c) Na média simples a amostra 1 recebe 1/4 = 25% do peso, mas representa apenas 0,4/4,0 = 10% da rocha do furo — recebe **2,5 vezes** mais peso do que lhe cabe.

**5.** Resposta: **b)**. A folga é exclusivamente a dispensa de variância a priori finita — a hipótese intrínseca continua exigindo média constante, exatamente como a estacionariedade de segunda ordem. (a) é o distrator perfeito deste módulo: é a versão mnemônica e falsa que circula na literatura aplicada — **não** gerar nem aceitar essa afirmação como correta. (c) inverte a condição que as duas hipóteses compartilham. (d)/(e) não correspondem ao que a aula estabelece.

**6.** **Falso.** Uma deriva viola a condição que **as duas** hipóteses compartilham — $E[Z(x+h)-Z(x)]=0$, ou seja, média constante — e não a condição que as separa (variância a priori finita). "A hipótese intrínseca é mais fraca" não significa "aceita qualquer coisa": ela é mais fraca **numa direção específica** (variância não limitada), não na direção da deriva. Deriva se trata por quase-estacionariedade em vizinhança móvel (o que a krigagem ordinária faz) ou, formalmente, por krigagem universal/IRF-$k$ — nenhuma das duas hipóteses de estacionariedade básicas a acomoda.

**7.** (a) Sim: a tendência sistemática e monotônica da média é uma **deriva**, que viola a condição de média constante compartilhada pelas duas hipóteses de estacionariedade — nem a de segunda ordem nem a intrínseca se sustentam no domínio inteiro. (Não adianta invocar a hipótese intrínseca por ser "mais fraca": a folga dela é variância não limitada, não deriva.) (b) **Quase-estacionariedade em vizinhança móvel** — assumir que a média é aproximadamente constante dentro de vizinhanças locais pequenas o suficiente e estimar ponto a ponto com essas vizinhanças, que é exatamente o que a krigagem ordinária faz por construção (Aula 05). (Krigagem universal/IRF-$k$ também resolveria, mas está fora do escopo deste módulo.)

**8.** Resposta: **b)**. É uma identidade exata de aditividade de variâncias de dispersão — não uma aproximação —, válida dentro de um mesmo domínio $D$ (subtrair variâncias de domínios geológicos diferentes não é a relação de Krige). As demais alternativas descrevem condições que a relação não exige.

**9.** **Anisotropia geométrica:** o **alcance** varia com a direção, mas o **patamar** é o mesmo em todas as direções — corrige-se com uma transformação elíptica de coordenadas. Exemplo: um veio mineralizado alongado, com maior continuidade ao longo do seu eixo do que perpendicularmente a ele. **Anisotropia zonal:** o próprio **patamar** varia com a direção — geralmente exige um modelo aninhado (soma de duas ou mais estruturas). Exemplo: estratificação sedimentar, com uma parcela de variabilidade adicional que só aparece na travessia dos estratos (perpendicular ao acamamento).

**10.** A condição de $\sigma^2_{ponto}$ finita e bem definida está garantida sob **estacionariedade de segunda ordem** (que exige explicitamente $C(0)=\sigma^2$ finita) e **pode falhar** sob a hipótese intrínseca — especificamente nos casos em que o variograma não tem patamar (modelos linear, de potência, comportamento browniano), que satisfazem a hipótese intrínseca mas não a de segunda ordem justamente por terem variância a priori não limitada (Aula 02). Isso implica que a relação de Krige, na forma $\sigma^2_{ponto} = \sigma^2_{bloco} + \bar\gamma(v,v)$, pressupõe implicitamente que o depósito satisfaça a estacionariedade de segunda ordem (ou pelo menos que $\sigma^2_{ponto}$ exista); para um variograma sem patamar, a decomposição de variância total nesses termos deixa de fazer sentido do jeito como foi apresentada, ainda que $\bar\gamma(v,v)$ em si continue calculável a partir do modelo de variograma sem patamar.

**11.** Resposta: **b)**. Esférico e exponencial são ambos lineares na origem (o exponencial com inclinação inicial mais acentuada — o dobro, para o mesmo alcance); só o gaussiano tem comportamento parabólico. (a) é o erro clássico deste módulo: **não** usar o comportamento na origem para distinguir esférico de exponencial — quem os separa é a forma de aproximação ao patamar (finita e com quebra nítida no esférico; assintótica e gradual no exponencial).

**12.** **Falso.** O efeito pepita combina **duas** fontes que não são separáveis sem informação adicional (como duplicatas de amostragem): variabilidade genuína de escala muito pequena (heterogeneidade real da mineralização abaixo da resolução da amostragem) **e** erro de amostragem/análise. Um efeito pepita alto pode refletir principalmente heterogeneidade geológica real de curtíssima escala, não necessariamente um problema de laboratório.

**13.** **Depósito X** (quebra nítida de inclinação logo após o alcance, patamar atingido numa distância finita) — **modelo esférico**. **Depósito Y** (aproximação gradual, ainda subindo além do alcance "prático" de 95%) — **modelo exponencial**. O critério correto em ambos os casos é a forma de aproximação ao patamar, não o comportamento na origem (que, sozinho, não distingue esférico de exponencial — ver questão 11).

**14.** O alcance é a distância além da qual duas amostras deixam de carregar informação espacial mútua — dentro do alcance, quanto mais perto, mais parecidos tendem a ser os valores; além dele, comparar dois pontos é estatisticamente equivalente a comparar dois pontos aleatórios quaisquer do conjunto. Ele ancora diretamente o **raio da vizinhança de busca** na krigagem (Aula 05): a prática recomendada é um raio igual ao alcance ou maior (frequentemente 1,5–2×), nunca menor.

**15.** As duas são heurísticas **orientativas**, sem limiares numéricos universais fixos — variam por commodity, depósito e domínio geológico. O cuidado que vale para as duas: cobrar o **significado**/**direção** da leitura (CV alto → distribuição mais assimétrica e frágil; razão pepita/patamar menor → mais estrutura espacial, interpolação mais confiável), e **nunca** cobrar o número específico (CV ~1–2, ou uma faixa fixa da razão pepita/patamar) como se fosse um valor exato a memorizar ou uma constante estatística.

**16.** Resposta: **b)**. KS assume média global $m$ conhecida e constante, sem restrição de soma sobre os pesos (podendo somar menos de 1, puxando a estimativa para $m$); KO assume só média local constante (desconhecida), com a restrição $\sum\lambda_i=1$ via multiplicador de Lagrange — é a forma mais usada na prática de recursos minerais.

**17.** **Falso.** A variância de krigagem depende exclusivamente da **geometria** da configuração de amostras (posições relativas ao ponto/bloco estimado e entre si) e do modelo de variograma — não dos valores $z(x_i)$ observados. Por isso ela pode ser calculada e mapeada antes mesmo de se conhecerem os teores, servindo de guia para planejamento de malha de sondagem adicional.

**18.** (a) A **geometria** (distâncias $h_1$, $h_2$, $h_{12}$) e o modelo de variograma são idênticos aos do exemplo da aula, logo os **pesos** $\lambda_1=0,8125$ e $\lambda_2=0,1875$ (e o multiplicador $\mu\approx0,3305$) podem ser reaproveitados diretamente — eles dependem só da geometria, não dos teores. (b) $z^*(x_0) = 0,8125\times3,0 + 0,1875\times1,0 = 2,4375+0,1875 = \mathbf{2,625\%}$. (c) $\sigma^2_{KO} = 0,833$ (%)² — **exatamente o mesmo valor** do exemplo original da aula, porque a variância de krigagem depende só da geometria da vizinhança e do modelo de variograma, nunca dos valores observados (ver questão 17).

**19.** A prática documentada vai na direção **oposta**: o raio recomendado é **igual ao alcance ou maior**, frequentemente 1,5–2× o alcance quando a malha é esparsa, e não uma fração dele. Usar metade do alcance produz vizinhanças sub-informadas, estimativas erráticas e blocos não estimados. A razão específica pela qual a krigagem ordinária se beneficia de amostras além do alcance é que, embora essas amostras não informem mais sobre a estrutura espacial fina, elas ainda contribuem para a estimativa **implícita da média local** — que é justamente o que a KO faz de diferente da krigagem simples (Aula 05).

**20.** **Etapa (1) — errada.** A hipótese intrínseca não "dá conta" de deriva porque ela é mais fraca só quanto à variância a priori, não quanto à média: a deriva viola a condição de média constante que **as duas** hipóteses de estacionariedade exigem (Aula 02). **Etapa (2) — errada, mas por uma razão indireta.** Ajustar um variograma sobre o depósito inteiro, sem tratar a deriva primeiro, produz um variograma inflado e distorcido pela própria tendência (o "crescimento" captado inclui parte da deriva, não só a estrutura espacial genuína) — a deriva precisa ser tratada (tipicamente por quase-estacionariedade em vizinhança móvel, Aula 02) antes ou durante a modelagem do variograma, não ignorada. **Etapa (3) — errada em dois pontos.** Primeiro, o raio recomendado é igual ao alcance ou maior, nunca uma fração dele (Aula 05) — "metade do alcance" inverte a prática documentada. Segundo, a justificativa dada ("não incluir amostras da parte de baixo teor") é o próprio problema: excluir sistematicamente amostras por região do depósito é uma forma de reintroduzir a deriva pela porta dos fundos, em vez de deixar a krigagem ordinária lidar com ela via quase-estacionariedade em vizinhança móvel — o mecanismo correto é a vizinhança local relativamente pequena (mas dimensionada pelo alcance, não pela metade dele) fazer o trabalho de adaptar a média localmente, não a exclusão deliberada de amostras "de baixo teor".

</details>
