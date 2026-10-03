# Aula 02: Propriedades físicas das rochas, perfilagem de poços, amarração poço-sísmica e resolução

**ID:** geologia-avancado-m11-a02
**Módulo:** [[11-sismoestratigrafia-modulo|Módulo 11 — Sismoestratigrafia]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** mostrar como as propriedades físicas das rochas medidas em poço (velocidade sônica, densidade) constroem o sismograma sintético que amarra o dado sísmico à profundidade real, e aprofundar a discussão de resolução iniciada na Aula 01 com o problema prático da calibração poço-sísmica.

**Pré-requisito:** Aula 01 deste módulo — impedância acústica, coeficiente de reflexão e os limites de resolução vertical e horizontal da sísmica.

## Antes de começar, você precisa saber

- Da Aula 01: que um refletor sísmico marca um contraste de **impedância acústica** (Z = ρ·V), e que a resolução vertical da sísmica é limitada a frações do comprimento de onda dominante — tipicamente muito pior que a resolução de dados de poço.
- Que um **poço** registra propriedades físicas continuamente ao longo de sua trajetória através de ferramentas descidas por cabo (perfilagem, ou *well logging*), com resolução vertical de centímetros a poucos decímetros — ordens de grandeza melhor que a sísmica.

## Conteúdo

### Por que o poço é indispensável para interpretar sísmica

A Aula 01 terminou com um problema sem solução própria: a sísmica enxerga a geometria de grandes volumes de rocha, mas não resolve espessuras finas nem diz, sozinha, que litologia gerou cada refletor. O poço resolve exatamente esse ponto cego, porque mede as mesmas grandezas físicas que controlam a reflexão sísmica — velocidade e densidade — só que em escala vertical de centímetros, ao longo de toda a trajetória perfurada. A dificuldade é que poço e sísmica não falam a mesma língua por padrão: o poço mede profundidade real (em metros, medida ao longo do cabo ou da coluna), e a sísmica opera nativamente em tempo de viagem duplo (TWT, em milissegundos, como visto na Aula 01). Amarrar os dois — transformar a informação de profundidade do poço num referencial de tempo comparável à seção sísmica — é a etapa que torna a interpretação sismoestratigráfica confiável, em vez de especulativa.

### As duas ferramentas que constroem a ponte: perfil sônico e perfil de densidade

Duas medidas de poço são, para os fins desta disciplina, as protagonistas. O **perfil sônico** (*sonic log*, ou DT) mede o tempo de trânsito de uma onda elástica através de um intervalo fixo de rocha ao redor do poço, registrado tipicamente em microssegundos por pé (ou metro) — o inverso da velocidade. O **perfil de densidade** (*density log*, ou RHOB) mede a densidade da formação por atenuação de radiação gama emitida por uma fonte na ferramenta. Multiplicando velocidade (derivada do sônico) por densidade, camada a camada ao longo do poço, obtém-se um perfil contínuo de **impedância acústica** — exatamente a grandeza que a Aula 01 identificou como a origem física de todo refletor sísmico.

A partir desse perfil de impedância, calcula-se o **coeficiente de reflexão** em cada interface (a mesma fórmula RC = (Z₂−Z₁)/(Z₂+Z₁) da Aula 01), e convolucionando essa série de coeficientes de reflexão com o pulso da fonte sísmica usado no levantamento (a **wavelet**, estimada a partir do próprio dado processado), obtém-se um **sismograma sintético**: uma traço sísmico artificial, previsto a partir apenas das medidas de poço, que pode ser comparado diretamente com o traço sísmico real mais próximo do poço. Quando o sintético e o real se alinham bem — os principais refletores do sintético coincidem, em tempo, com os principais refletores do dado real —, diz-se que o poço está **amarrado** (*well tie*) à sísmica, e a correspondência profundidade-tempo estabelecida por essa amarração (a **curva tempo-profundidade**, T-Z) passa a ser a régua de conversão usada em toda a interpretação daquela área.

```
Construção do sismograma sintético (esquemático)

perfil sônico (DT)  ----\
                          \
perfil de densidade (RHOB) --> impedância Z(profundidade) --> série de RC(profundidade)
                                                                        |
                                                     convolução com wavelet estimada
                                                                        |
                                                                        v
                                                        sismograma sintético (em tempo)
                                                                        |
                                              comparação com traço sísmico real no poço
                                                                        |
                                                                        v
                                                curva tempo-profundidade (T-Z) = a "amarração"
```
Cada seta representa uma transformação física ou matemática; a etapa final — comparar sintético com real — é onde o intérprete valida (ou ajusta) a amarração antes de confiar em qualquer marco estratigráfico picado na sísmica.

### O que pode dar errado na amarração, e por que importa

A amarração poço-sísmica raramente é perfeita na primeira tentativa, e os motivos do desajuste são, eles mesmos, informação geológica. Um desajuste sistemático de tempo ao longo de todo o poço costuma indicar erro na estimativa da wavelet ou nas correções de tempo aplicadas ao dado (checkshot ou VSP — perfis de velocidade registrados diretamente com geofones no poço, que fornecem uma medida independente do tempo de trânsito real e são o padrão-ouro de calibração, mais confiável que o sônico sozinho por não sofrer os efeitos de invasão de lama e de más condições de poço que distorcem localmente a leitura sônica). Um desajuste concentrado num intervalo específico costuma indicar que a rocha ali tem uma resposta elástica anisotrópica ou uma feição (gás na formação, por exemplo, que reduz fortemente a velocidade e produz uma amarração local ruim mesmo com wavelet correta) que os dados de poço convencionais não capturam bem.

O ponto conceitual mais importante desta etapa é este: um refletor sísmico que "parece" corresponder a um limite de sequência ou a uma superfície de discordância só pode ser afirmado como tal depois de amarrado a um marco estratigráfico independentemente identificado no poço (por bioestratigrafia, por exemplo — datação por microfósseis, fora do escopo técnico desta aula mas essencial na prática profissional). Sem essa amarração, toda leitura cronológica de um refletor (o tema central da Aula 03) é uma hipótese não testada, por mais convincente que pareça visualmente.

### Resolução revisitada: o que o poço resolve que a sísmica não resolve

A Aula 01 estabeleceu que a resolução vertical sísmica, mesmo em boas condições, raramente é melhor que alguns metros, e piora com a profundidade. A perfilagem de poço opera numa escala inteiramente diferente: um perfil sônico ou de densidade típico é amostrado a cada 15 a 20 centímetros, e resolve camadas de espessura métrica ou menor com clareza — a mesma camada de 8 m do exemplo trabalhado da Aula 01, invisível como par de refletores na sísmica, aparece perfeitamente definida, com topo e base nítidos, em qualquer perfil de poço que a atravesse.

Vale reparar onde, exatamente, essa discrepância é resolvida na prática — porque a resposta já está na própria construção do sismograma sintético, três seções acima, e passa despercebida na primeira leitura. A série de coeficientes de reflexão calculada a partir do poço tem a resolução do poço: ela registra cada mudança de impedância centimétrica ao longo da trajetória, e teria centenas de picos onde a sísmica mostra um punhado de refletores. O que reconcilia as duas escalas é a **convolução com a wavelet**: como a wavelet tem uma banda de frequências limitada (a mesma banda do levantamento sísmico), convolucioná-la com a série de RC funciona como um filtro passa-banda — o sintético que sai da conta já é uma versão *degradada de propósito* do poço, rebaixada à resolução da sísmica. É por isso que o sintético é comparável ao traço real: ele não é "o poço", é "o poço visto com os olhos da sísmica". E é também por isso que a amarração poço-sísmica não elimina o limite de resolução da Aula 01 — ela apenas informa o intérprete sobre o que está escondido dentro de cada refletor composto, sem torná-lo visível na seção.

Essa discrepância de escala não é um defeito de um método frente ao outro — é o motivo pelo qual os dois são usados juntos, e não um no lugar do outro. A sísmica fornece cobertura espacial contínua (uma área inteira de uma bacia, entre poços) mas com resolução vertical grosseira; o poço fornece resolução vertical excelente, mas só no ponto exato de sua trajetória. A prática profissional de interpretação sismoestratigráfica é, no fundo, um exercício constante de usar o poço para calibrar o que a sísmica não resolve diretamente e usar a sísmica para extrapolar espacialmente o que o poço só vê num ponto — e é essa combinação, não qualquer um dos dois métodos isoladamente, que sustenta a leitura de sistemas deposicionais inteiros a partir de um punhado de poços e uma malha sísmica (tema que amadurece nas Aulas 04 e 05).

Um refinamento vale menção porque aparece com frequência em bacias com múltiplos poços: quando há um número suficiente de poços amarrados de forma consistente numa mesma área, é possível construir mapas de velocidade intervalar mais robustos que a análise de velocidade sísmica sozinha forneceria, reduzindo a incerteza da conversão tempo-profundidade em toda a área — não apenas nos pontos de poço. Esse é um dos motivos práticos pelos quais bacias maduras, com muitos poços perfurados ao longo de décadas, produzem interpretações sismoestratigráficas sistematicamente mais confiáveis que bacias de fronteira exploratória com poucos poços.

## Exemplo trabalhado

**Situação:** um poço tem perfil sônico e de densidade completos, e um sismograma sintético foi gerado e comparado ao traço sísmico real. O ajuste é bom no intervalo raso (0–1.500 m) mas se deteriora progressivamente abaixo de 2.800 m, com os principais refletores do sintético aparecendo sistematicamente mais "tarde" em tempo (em TWT maior) do que os refletores correspondentes no dado real, num desvio que cresce com a profundidade. Que hipóteses explicam esse padrão, e como discriminar entre elas?

**Resolução:**

Um desajuste que cresce progressivamente com a profundidade, e não um salto localizado num único intervalo, aponta para um erro sistemático e acumulativo — não para uma anomalia litológica pontual (que produziria um desajuste concentrado, não uma deriva crescente). A hipótese mais comum nesse padrão é um viés na velocidade usada para a conversão tempo-profundidade abaixo da seção rasa: se o sônico subestima ligeiramente a velocidade real da formação (um problema conhecido em poços com más condições de furo, onde a ferramenta sônica sofre de "salto de ciclo" e registra tempos de trânsito artificialmente altos, isto é, velocidades artificialmente baixas), cada camada adicional perfurada acumula um pequeno erro de tempo **no mesmo sentido**, e o desvio total cresce com a profundidade. Repare que o sinal do desvio é obrigatório e serve de teste: velocidade subestimada significa tempo de trânsito superestimado, logo o sintético coloca cada refletor num TWT **maior** que o real — ele "atrasa" progressivamente, exatamente o padrão descrito. Se o sintético aparecesse sistematicamente adiantado, a explicação teria de ser a oposta (velocidade superestimada, por exemplo por um sônico rodado em intervalo cimentado ou por erro de datum/*replacement velocity* na seção rasa), e não a de salto de ciclo. A forma de discriminar essa hipótese de outras (erro de wavelet, por exemplo, que tende a produzir desajuste mais uniforme em todas as profundidades) é comparar o sônico com um dado independente de velocidade: um checkshot ou VSP no mesmo poço, que não sofre do mesmo problema de más condições de furo, fornece uma medida direta do tempo de trânsito real e permite corrigir (recalibrar) o sônico antes de reconstruir o sintético. A conclusão de trabalho é que, sem esse dado independente, a amarração abaixo de 2.800 m nesse poço deve ser tratada como pouco confiável, e qualquer marco estratigráfico picado nesse intervalo carrega incerteza adicional de profundidade até a recalibração ser feita.

## Recap relâmpago

- Os perfis **sônico** (velocidade) e de **densidade** (RHOB), combinados, reconstroem o perfil de impedância acústica de um poço em profundidade — a mesma grandeza física (Z = ρ·V) que gera reflexões sísmicas (Aula 01).
- Convolucionando a série de coeficientes de reflexão derivada do poço com a wavelet do levantamento sísmico, obtém-se um **sismograma sintético**; compará-lo ao traço sísmico real produz a **amarração poço-sísmica** e a curva tempo-profundidade (T-Z) que converte toda a interpretação daquela área.
- Um desajuste sistemático e crescente com a profundidade costuma indicar erro de velocidade acumulado (más condições de furo no sônico), e o **sinal** do desvio identifica a direção do erro: sônico subestimando a velocidade (salto de ciclo) atrasa o sintético em relação ao dado real, nunca o adianta. Um desajuste localizado costuma indicar uma feição elástica pontual (gás, anisotropia). Checkshots e VSP são medidas independentes mais confiáveis que o sônico sozinho para calibrar essas situações.
- Nenhum refletor pode ser afirmado como marco estratigráfico ou cronológico sem amarração a um marco identificado de forma independente no poço — sem isso, a leitura cronológica de refletores (Aula 03) é hipótese não testada.
- Poço e sísmica têm escalas de resolução complementares e não substituíveis: resolução vertical excelente e cobertura pontual no poço; cobertura espacial contínua e resolução vertical grosseira na sísmica. A interpretação sismoestratigráfica combina os dois deliberadamente.
- A reconciliação entre as duas escalas acontece na própria **convolução com a wavelet**: por ter banda de frequências limitada, ela filtra a série de RC do poço até a resolução da sísmica. O sintético é "o poço visto com os olhos da sísmica" — e por isso a amarração informa o que há dentro de um refletor composto sem tornar isso visível na seção.

## Próxima aula

[[11-sismoestratigrafia-aula-03-refletores-e-terminacoes|Aula 03 — Refletores como linhas de tempo: significado estratigráfico e cronológico e padrões de terminação]]

## Anterior

[[11-sismoestratigrafia-aula-01-fundamentos-do-metodo-sismico|Aula 01 — Fundamentos do método sísmico de reflexão]]

## Fontes

- Sheriff, R. E. & Geldart, L. P. (1995), *Exploration Seismology*, 2ª ed., Cambridge University Press, cap. 4 e 9 (velocidade, resolução).
- Ellis, D. V. & Singer, J. M. (2007), *Well Logging for Earth Scientists*, 2ª ed., Springer, cap. 1, 9 e 17 (perfil sônico, perfil de densidade, sismograma sintético).
- White, R. E. & Simm, R. (2003), "Tutorial: good practice in well ties", *First Break*, 21(10), p. 75–83 (metodologia de amarração poço-sísmica, uso de checkshot/VSP).
- Mitchum, R. M., Vail, P. R. & Sangree, J. B. (1977), "Seismic stratigraphy and global changes of sea level, part 6", em Payton, C. E. (org.), *Seismic Stratigraphy — Applications to Hydrocarbon Exploration*, AAPG Memoir 26, p. 117–133.

<!--
nivel: avancado
palavras_corpo: 1701 (Conteudo ate Exemplo trabalhado, recontagem apos auditoria cientifica e revisao didatica 2026-08-30)
mapa_objetivo_secao:
  geologia-avancado-m11-oa01: "Por que o poço é indispensável para interpretar sísmica" + "As duas ferramentas que constroem a ponte" + "O que pode dar errado na amarração, e por que importa" + "Resolução revisitada" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: SISMO-M11-A02-PERFIS-001
    claim: "O perfil sônico (DT) mede o tempo de trânsito de uma onda elástica por um intervalo fixo de rocha (inverso da velocidade), e o perfil de densidade (RHOB) mede a densidade da formação por atenuação de radiação gama; multiplicando velocidade por densidade camada a camada obtém-se o perfil contínuo de impedância acústica do poço."
    risk: fato
    source: "Ellis & Singer 2007, cap. 9 e 17"
  - claim_id: SISMO-M11-A02-SINTETICO-002
    claim: "O sismograma sintético é construído convolucionando a série de coeficientes de reflexão derivada do perfil de impedância do poço com a wavelet sísmica estimada do levantamento; comparar o sintético ao traço sísmico real mais próximo do poço, ajustando a correspondência tempo-profundidade, constitui a amarração poço-sísmica (well tie), que estabelece a curva tempo-profundidade (T-Z) usada na conversão da interpretação naquela área."
    risk: fato
    source: "White & Simm 2003, First Break 21(10); Ellis & Singer 2007, cap. 17"
  - claim_id: SISMO-M11-A02-CHECKSHOT-003
    claim: "Checkshots e VSP (perfis sísmicos verticais, registrados com geofones no próprio poço) fornecem uma medida direta e independente do tempo de trânsito, geralmente considerada mais confiável que o perfil sônico isolado para calibração de amarração poço-sísmica, porque o sônico é suscetível a distorções por más condições de poço (invasão de lama, salto de ciclo) que subestimam a velocidade real da formação."
    risk: fato
    source: "White & Simm 2003, First Break 21(10); Ellis & Singer 2007, cap. 1"
  - claim_id: SISMO-M11-A02-DERIVA-006
    claim: "O sinal da deriva (drift) entre sismograma sintetico e traco sismico real e diagnostico e nao arbitrario: como o tempo de transito integrado do sonico e usado para posicionar cada refletor em tempo, um sonico que SUBESTIMA a velocidade (tempo de transito artificialmente alto, tipico de salto de ciclo em ma condicao de furo) produz um sintetico ATRASADO em relacao ao dado real (TWT maior), com o atraso crescendo cumulativamente com a profundidade; o padrao oposto (sintetico adiantado) exige velocidade superestimada e nao pode ser explicado por salto de ciclo."
    risk: fato
    source: "White & Simm 2003, First Break 21(10) (boas praticas de amarracao e correcao de deriva por checkshot); Ellis & Singer 2007, cap. 9 (salto de ciclo eleva o tempo de transito registrado)"
    audit: "achado vermelho corrigido em 2026-08-30 (SISMO-M11-A02-TIEDRIFT-006): o exemplo trabalhado descrevia o sintetico como ADIANTADO e explicava o padrao por sonico subestimando a velocidade - as duas metades se contradiziam"
  - claim_id: SISMO-M11-A02-RESOLUCAO-004
    claim: "A perfilagem de poço (perfis sônico e de densidade) tem resolução vertical da ordem de centímetros a poucos decímetros (amostragem tipica de 15-20 cm), ordens de grandeza melhor que a resolução vertical sísmica típica (metros a dezenas de metros conforme a profundidade, ver Aula 01), o que torna o poço a ferramenta de calibração indispensável para camadas finas não resolvidas diretamente pela sísmica."
    risk: fato
    source: "Ellis & Singer 2007, cap. 1; Sheriff & Geldart 1995, cap. 9"
  - claim_id: SISMO-M11-A02-MARCOESTRAT-005
    claim: "Um refletor sísmico só pode ser afirmado com confiança como correspondente a um limite de sequência, discordância ou marco cronoestratigráfico específico após amarração a um marco identificado de forma independente no poço (por exemplo, por bioestratigrafia); sem essa amarração, a atribuição cronológica de um refletor permanece uma hipótese não testada."
    risk: fato
    source: "Mitchum, Vail & Sangree 1977, AAPG Memoir 26; White & Simm 2003"
-->
