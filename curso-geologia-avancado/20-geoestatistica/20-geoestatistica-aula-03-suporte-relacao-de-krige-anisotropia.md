# Aula 03: Suporte, relação de Krige e anisotropia

**ID:** geologia-avancado-m20-a03
**Módulo:** [[20-geoestatistica-modulo|Módulo 20 — Introdução à geoestatística]]
**Duração estimada:** ~18 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** desenvolver as duas consequências práticas do modelo de variável regionalizada estabelecido na Aula 02 — o efeito do suporte da amostra sobre a variância observada, formalizado pela relação de Krige, e a dependência direcional da continuidade espacial, a anisotropia.
**Ao final você vai conseguir:** explicar por que a variância observada de um conjunto de teores não é uma propriedade fixa do depósito, mas do **suporte** em que ele foi medido; aplicar a relação de Krige para calcular a variância de teores de bloco a partir da variância de amostras pontuais; explicar por que ignorar o efeito de suporte distorce o planejamento de lavra numa direção previsível; e distinguir anisotropia geométrica de anisotropia zonal pela forma como cada uma se manifesta.
**Pré-requisito:** [[20-geoestatistica-aula-02-variaveis-regionalizadas-funcao-aleatoria-estacionariedade|Aula 02 — Variáveis regionalizadas, função aleatória e estacionariedade]] (a Parte 1 deste par: o conceito de variável regionalizada, a função aleatória e a definição do variograma $\gamma(h)$, que esta aula usa diretamente).

> [!note] Esta aula é a **Parte 2** de um par. A [[20-geoestatistica-aula-02-variaveis-regionalizadas-funcao-aleatoria-estacionariedade|Parte 1]] montou o modelo probabilístico; esta colhe as duas consequências que mais aparecem na prática de recursos minerais. Estude as duas em sequência.

## Conteúdo

### O suporte: por que o mesmo depósito tem variâncias diferentes

Uma das consequências menos intuitivas de tratar o teor como variável regionalizada é que a variância observada de um conjunto de dados **não é uma propriedade fixa do depósito** — depende do **suporte**: o volume, a forma, a orientação e a massa da amostra sobre a qual o valor foi medido. Um testemunho de sondagem de 1 m de comprimento e poucos centímetros de diâmetro tem um suporte muito menor do que um bloco de lavra de 10 × 10 × 10 m; e a variância dos teores medidos no suporte pequeno (amostras pontuais) é sistematicamente **maior** do que a variância que se observaria se pudesse medir o teor médio de blocos inteiros do mesmo tamanho da unidade de lavra.

A razão é intuitiva por analogia: a temperatura média de uma cidade inteira num dia varia muito menos, de um dia para o outro, do que a temperatura medida por um único termômetro num único ponto da cidade — porque a média sobre uma área grande faz com que as flutuações locais (um ponto de sombra, um ponto ensolarado) se cancelem parcialmente, restando apenas a variação de maior escala. Da mesma forma, um bloco de 10 m de lado contém uma mistura de rocha rica e pobre em seu interior, e o teor médio desse bloco varia menos, de bloco para bloco, do que o teor de amostras pontuais individuais varia de ponto para ponto — a variância entre blocos é sempre menor ou igual à variância entre pontos.

Essa relação, formalizada por Matheron como **relação de Krige** (*Krige's relation*) a partir da constatação empírica de D. G. Krige no Witwatersrand, é uma **identidade exata** — não uma aproximação — de aditividade de variâncias de dispersão **dentro de um mesmo domínio de referência $D$**: a variância de pontos dentro de $D$ é igual à variância de blocos dentro de $D$ somada à variância de pontos dentro de um bloco (a variância que se perde ao promediar um volume maior):

$$\sigma^2_{ponto} = \sigma^2_{bloco} + \bar{\gamma}(v,v)$$

onde $\bar{\gamma}(v,v)$ é a variância média dentro de um bloco de volume $v$ — o quanto o teor varia entre pontos dentro do próprio bloco.

> [!warning] Dois cuidados com esta equação, porque são eles que a fazem funcionar ou falhar:
> 1. **O domínio $D$ precisa ser o mesmo nos dois termos.** Subtrair variâncias medidas em domínios geológicos diferentes (uma litologia contra outra, uma zona de alteração contra outra) não é a relação de Krige e não dá resultado interpretável.
> 2. **$\bar{\gamma}(v,v)$ não se calcula a partir dos dados brutos** — ela se obtém do modelo de variograma ajustado, que é assunto da Aula 04. Enquanto isso, trate-a como um valor **fornecido**: no exemplo trabalhado abaixo ela é dada de partida, e é assim que você a usará até chegar lá.

Ignorar o efeito de suporte é um erro clássico e caro em avaliação de recursos: aplicar diretamente, a um modelo de blocos de lavra, os parâmetros estatísticos calculados sobre amostras pontuais (compositas de furo) superestima sistematicamente a proporção de blocos de teor muito alto ou muito baixo, distorcendo o planejamento de lavra e a seleção de minério. Repare que a distorção atinge **as duas caudas** da distribuição: blocos ricos demais e blocos pobres demais são igualmente superestimados em número, porque a distribuição pontual é simplesmente mais larga do que a de blocos.

### Continuidade e anisotropia: a forma da semelhança espacial

**Continuidade espacial** é o grau em que valores próximos se parecem entre si — quanto maior a continuidade, mais devagar a semelhança se degrada com a distância, e mais confiável é usar uma amostra para prever o valor de um ponto vizinho não amostrado.

A continuidade de uma variável regionalizada quase nunca é a mesma em todas as direções: um veio mineralizado alongado, um paleocanal fluvial, ou uma zona de cisalhamento hospedeira de mineralização impõem uma direção preferencial de continuidade — o teor tende a se parecer mais entre dois pontos separados ao longo do eixo do veio do que entre dois pontos com a mesma distância, mas perpendiculares a ele. Essa dependência da continuidade em relação à direção é a **anisotropia**, e a Aula 04 mostra como ela se manifesta e se modela formalmente no variograma.

Duas formas principais aparecem na prática, e a diferença entre elas está em **qual parâmetro muda com a direção**:

- **Anisotropia geométrica** — o **patamar** (a variância total) é igual em todas as direções, mas o **alcance** (a distância até onde existe continuidade) muda com a direção. É o caso do veio alongado: a mesma variabilidade total, alcançada mais longe ao longo do eixo do que perpendicularmente a ele. Tipicamente corrigida por uma transformação elíptica de coordenadas.
- **Anisotropia zonal** — mais complexa: o **próprio patamar** muda com a direção. Associa-se em geral a domínios geológicos com escalas de heterogeneidade fundamentalmente diferentes em direções diferentes — por exemplo, estratificação sedimentar, com continuidade muito maior ao longo do acamamento do que perpendicular a ele, e com uma parcela de variabilidade que só existe na travessia dos estratos.

## Exemplo trabalhado

**Situação:** um geólogo de recursos dispõe de compositas de furo de sondagem (suporte pontual, aproximadamente 1 m) de um corpo mineralizado tabular, com variância observada $\sigma^2_{ponto} = 4,0$ (g/t)². O modelo de variograma ajustado para este depósito (antecipando a Aula 04) indica que a variância média dentro de um bloco de lavra de 10 × 10 × 5 m é $\bar{\gamma}(v,v) = 1,5$ (g/t)². Uma segunda área do mesmo depósito, com litologia mais homogênea, tem variância pontual mais baixa, $\sigma^2_{ponto} = 1,2$ (g/t)², e variância dentro de bloco $\bar{\gamma}(v,v) = 0,3$ (g/t)².

**Pergunta:** usando a relação de Krige, estime a variância dos teores de bloco (10 × 10 × 5 m) em cada uma das duas áreas, e discuta o que a comparação revela sobre o risco de aplicar diretamente a estatística de amostras pontuais ao planejamento de lavra por blocos.

**Resolução:**

Isolando a variância de bloco na relação de Krige: $\sigma^2_{bloco} = \sigma^2_{ponto} - \bar{\gamma}(v,v)$.

**Área 1 (mais heterogênea):** $\sigma^2_{bloco} = 4,0 - 1,5 = 2,5$ (g/t)². A variância de bloco (2,5) é 62,5% da variância pontual (4,0) — uma redução considerável, mas o bloco ainda retém boa parte da variabilidade original, porque a variância "perdida" dentro do bloco ($\bar{\gamma}(v,v)=1,5$) é relativamente pequena frente à variância pontual total.

**Área 2 (mais homogênea):** $\sigma^2_{bloco} = 1,2 - 0,3 = 0,9$ (g/t)². A variância de bloco (0,9) é 75% da variância pontual (1,2) — proporcionalmente, uma redução menor do que na Área 1.

**Discussão:** em ambas as áreas, a variância de bloco é menor do que a variância pontual, confirmando o princípio de que blocos suavizam a variabilidade observada em amostras pontuais — mas a magnitude da redução não é igual, porque depende da relação entre o tamanho do bloco e a continuidade espacial própria de cada área (embutida em $\bar{\gamma}(v,v)$). Se um planejador de lavra aplicasse a distribuição de teores pontuais (compositas) diretamente ao modelo de blocos, sem essa correção, ele superestimaria sistematicamente a proporção de blocos de teor extremo (muito alto ou muito baixo) em ambas as áreas — mas o erro relativo seria maior na Área 1, onde a diferença entre as duas variâncias é maior em termos absolutos. É exatamente essa distorção que a mudança de suporte, formalizada aqui e operacionalizada pela krigagem de bloco (Aula 05), existe para corrigir.

## Recap relâmpago

- O **suporte** (volume, forma, orientação e massa da amostra) muda a variância observada: a variância de blocos é sempre menor ou igual à de pontos. A variância **não é propriedade do depósito**, e sim do par depósito-suporte.
- A **relação de Krige** é uma **identidade exata** de aditividade de variâncias de dispersão dentro de um mesmo domínio $D$: $\sigma^2_{ponto} = \sigma^2_{bloco} + \bar{\gamma}(v,v)$. Os dois cuidados são manter $D$ fixo e lembrar que $\bar\gamma(v,v)$ vem do modelo de variograma, não dos dados brutos.
- Ignorar o efeito de suporte **superestima a proporção de blocos de teor extremo — nas duas caudas**, alto e baixo —, porque a distribuição pontual é mais larga que a de blocos. É o que a krigagem de bloco (Aula 05) existe para corrigir.
- **Continuidade espacial** é o grau de semelhança entre pontos próximos; **anisotropia** é a dependência dessa continuidade em relação à direção. **Geométrica**: muda o alcance, o patamar é o mesmo. **Zonal**: muda também o patamar. As duas são formalizadas no variograma da próxima aula.

## Próxima aula

[[20-geoestatistica-aula-04-variografia-variogramas|Aula 04 — O variograma: cálculo experimental e modelagem teórica]] — como calcular $\gamma(h)$ a partir dos dados, os três elementos estruturais do variograma (efeito pepita, patamar, alcance), os modelos teóricos permissíveis e a modelagem formal da anisotropia introduzida aqui.

## Anterior

[[20-geoestatistica-aula-02-variaveis-regionalizadas-funcao-aleatoria-estacionariedade|Aula 02 — Variáveis regionalizadas, função aleatória e estacionariedade]] (Parte 1 deste par).

## Fontes

- Journel, A. G. & Huijbregts, C. J. (1978), *Mining Geostatistics*, Academic Press, capítulo II (variâncias de dispersão e relação de Krige entre suporte pontual e de bloco).
- Isaaks, E. H. & Srivastava, R. M. (1989), *An Introduction to Applied Geostatistics*, Oxford University Press, capítulo 19 (mudança de suporte, efeito de suporte em avaliação de recursos), capítulo 7 (variogramas direcionais) e capítulo 16 (modelagem da anisotropia geométrica e zonal).
- Matheron, G. (1963), "Principles of geostatistics", *Economic Geology*, 58(8), 1246-1266, DOI 10.2113/gsecongeo.58.8.1246 (artigo fundador; formalização do efeito de suporte).

<!--
nivel: avancado
palavras_corpo: 1440
mapa_objetivo_secao:
  geologia-avancado-m20-oa02: "O suporte: por que o mesmo depósito tem variâncias diferentes" + "Continuidade e anisotropia: a forma da semelhança espacial" + "Exemplo trabalhado"

divisao_de_aula: 'Esta aula e a PARTE 2 da antiga Aula 02 unica (Variaveis regionalizadas e a hipotese intrinseca, 2.505 palavras de corpo, ~32 min reais, 16 conceitos novos abstratos), dividida em 2026-09-18 pela revisao didatica (achado DID-M20-A02-CARGA-001), seguindo a convencao dos Modulos 17 e 19 deste curso. A PARTE 1 e a Aula 02 (variaveis regionalizadas, funcao aleatoria e estacionariedade). Esta metade recebeu as duas secoes de CONSEQUENCIA PRATICA do modelo - suporte e anisotropia - mais o EXEMPLO TRABALHADO ORIGINAL da antiga Aula 02, preservado palavra por palavra por ser inteiramente sobre a relacao de Krige.'

exemplo_trabalhado_preservado: 'O exemplo trabalhado desta aula E O ORIGINAL da antiga Aula 02, preservado PALAVRA POR PALAVRA (situacao, pergunta, resolucao e discussao), com uma unica alteracao, puramente de numeracao: as duas remissoes internas "Aula 03" e "Aula 04" foram renumeradas para "Aula 04" e "Aula 05" por causa do deslocamento das aulas seguintes. Nenhum numero, nenhuma conta e nenhuma conclusao foi tocada. A aritmetica foi reconferida na auditoria cientifica de 2026-09-18 (verified_ok B10) e fecha: 4,0-1,5=2,5 (62,5%); 1,2-0,3=0,9 (75%).'

alegacoes_auditaveis:
  - claim_id: GEOEST-M20-A02-RELACAOKRIGE-003
    claim: "A relação de Krige é uma IDENTIDADE EXATA de aditividade de variâncias de dispersão dentro de um mesmo domínio de referência D (não uma aproximação): a variância de teores de suporte pontual dentro de D é igual à variância de teores de suporte de bloco dentro de D somada à variância média de pontos dentro de um bloco, γ-barra(v,v) — σ²(ponto|D) = σ²(bloco|D) + γ-barra(v,v) —, de modo que a variância de bloco é sempre menor ou igual à variância pontual. Ignorar essa relação e aplicar a estatística de amostras pontuais diretamente a um modelo de blocos de lavra superestima sistematicamente a proporção de blocos de teor extremo (efeito de suporte), nas duas caudas da distribuição. A propriedade aditiva foi constatada empiricamente por D. G. Krige nos depósitos de ouro do Witwatersrand e formalizada por Matheron."
    risk: fato
    source: "Journel & Huijbregts (1978), Mining Geostatistics, capítulo II (formalização da relação de Krige / 'volume-variance relationship' e aditividade das variâncias de dispersão); Isaaks & Srivastava (1989), capítulo 19 (mudança de suporte, discussão aplicada do efeito de suporte em avaliação de recursos)."
  - claim_id: GEOEST-M20-A02-ANISOTROPIA-004
    claim: "A anisotropia geométrica ocorre quando o patamar do variograma é igual em todas as direções mas o alcance varia com a direção, corrigível por uma transformação elíptica de coordenadas; a anisotropia zonal ocorre quando o próprio patamar varia com a direção, tipicamente associada a domínios geológicos com escalas de heterogeneidade distintas em direções diferentes (por exemplo, estratificação sedimentar)."
    risk: fato
    source: "Isaaks & Srivastava (1989), An Introduction to Applied Geostatistics, capítulo 7 (variogramas direcionais) e capítulo 16 (modelagem do variograma amostral: anisotropia geométrica e zonal, modelos aninhados); Journel & Huijbregts (1978), capítulo III."

nota_claim_id_pre_divisao: 'Os dois claim_id acima conservam o prefixo A02, que designa a AULA PRE-DIVISAO em que foram emitidos, e NAO a aula em que hoje residem. A manutencao e DELIBERADA: renumera-los quebraria a rastreabilidade com o manifesto 20-geoestatistica-auditoria.json, que os referencia como GEOEST-M20-A02-RELACAOKRIGE-003 e GEOEST-M20-A02-ANISOTROPIA-004, ambos com desfecho registrado. A regra do plugin e explicita: claim_id nao se recicla nem se renumera. As alegacoes -001 e -002 permanecem declaradas na Aula 02 (Parte 1), onde esta o texto correspondente.'
-->
