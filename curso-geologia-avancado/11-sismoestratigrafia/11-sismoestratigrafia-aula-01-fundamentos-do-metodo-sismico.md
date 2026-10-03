# Aula 01: Fundamentos do método sísmico de reflexão: propagação de ondas, aquisição e processamento

**ID:** geologia-avancado-m11-a01
**Módulo:** [[11-sismoestratigrafia-modulo|Módulo 11 — Sismoestratigrafia]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** explicar como uma onda sísmica se reflete em contrastes de impedância acústica no subsolo, como o método de reflexão adquire esse sinal em campo (fonte, receptores, cobertura múltipla) e quais etapas de processamento transformam o dado bruto numa seção interpretável, introduzindo a noção de resolução sísmica que orienta o resto do módulo.

**Pré-requisito:** nenhum módulo deste curso além de noções gerais de estratigrafia e de propagação de ondas do curso base. Recomenda-se ter concluído o Módulo 10 (Tectônica de bacias sedimentares), cujo vocabulário de bacias e discordâncias será usado nas próximas aulas.

## Antes de começar, você precisa saber

- Que uma **onda sísmica** é uma perturbação elástica que se propaga por um meio transportando energia, não matéria — o mesmo princípio de uma onda numa corda ou do som no ar, mas em rocha.
- Que **impedância acústica** é o produto entre a velocidade de propagação da onda e a densidade do meio (Z = ρ·V); ela aparecerá formalmente nesta aula como a grandeza física que controla se — e quanto — uma onda se reflete numa interface.
- Que uma **discordância** é uma superfície de erosão ou não deposição que separa pacotes de rocha de idades distintas — conceito já usado no Módulo 10 para separar sequências sin-rifte e pós-rifte.

## Conteúdo

### O que a sísmica de reflexão mede, de fato

O método sísmico de reflexão não "vê" rocha, não "vê" litologia e não mede idade. Ele mede uma única coisa: o tempo que uma onda elástica leva para viajar da superfície até uma interface no subsolo, refletir, e voltar até um receptor — e a amplitude dessa reflexão. Tudo o que a sismoestratigrafia faz, dos padrões de terminação de refletores (Aula 03) às sismofácies (Aula 04), é inferência geológica construída sobre essa medida física simples. Vale internalizar isso agora, porque é a fonte do erro conceitual mais comum do módulo inteiro: uma seção sísmica não é uma "foto" do subsolo, é um mapa de tempos de viagem e amplitudes que precisa ser traduzido em geologia — e essa tradução carrega hipóteses.

Uma onda sísmica se reflete numa interface entre duas camadas sempre que há um contraste de **impedância acústica**, Z = ρ·V, onde ρ é a densidade e V a velocidade de propagação da onda no meio. A fração da **amplitude** incidente que retorna refletida — em incidência normal, a aproximação de primeira ordem usada na maior parte da interpretação — é dada pelo **coeficiente de reflexão**:

RC = (Z₂ − Z₁) / (Z₂ + Z₁)

onde Z₁ é a impedância da camada superior e Z₂ a da camada inferior. Vale guardar a distinção, porque ela reaparece em qualquer leitura quantitativa de amplitude: RC é uma razão de **amplitudes**, não de energias — a fração da *energia* incidente que retorna é RC², de modo que um RC de 0,1 devolve 10% da amplitude, mas apenas 1% da energia. Esta é a equação mais importante do módulo: ela diz que um refletor não marca, necessariamente, um contato litológico — marca um contraste de impedância. Um arenito bem cimentado sobre um folhelho compactado pode gerar um refletor forte; dois folhelhos de idades muito diferentes, mas com densidade e velocidade parecidas, podem não gerar refletor nenhum, mesmo havendo uma discordância de milhões de anos entre eles. Essa dissociação entre "limite litológico" e "refletor" é exatamente o que torna necessária a amarração com poços (Aula 02) antes de qualquer interpretação estratigráfica séria.

### Aquisição: como o dado nasce em campo

A aquisição sísmica de reflexão segue uma lógica comum em terra e em mar, com equipamentos diferentes. Uma **fonte** controlada gera um pulso de energia — no mar, tipicamente um canhão de ar comprimido (*air gun*); em terra, um caminhão vibrador (*vibroseis*) ou, historicamente, explosivos. Um arranjo de **receptores** — geofones em terra, hidrofones rebocados em cabos (*streamers*) no mar — registra o retorno da energia ao longo do tempo, tipicamente por vários segundos, numa amostragem de poucos milissegundos.

O elemento que faz a sísmica de reflexão funcionar bem, e não apenas registrar ruído, é a **cobertura múltipla** (*multi-fold coverage*, ou *CMP — common midpoint*). A mesma subsuperfície é iluminada repetidamente, a partir de pares fonte-receptor com posições diferentes, mas que compartilham o mesmo ponto médio na superfície. Sheriff & Geldart, no tratado de referência da disciplina, descrevem esse arranjo como o alicerce de toda a sísmica de exploração moderna: somando (empilhando) dezenas ou centenas de traços que amostram o mesmo ponto em subsuperfície sob ângulos diferentes, o sinal coerente (a reflexão real) se reforça e o ruído aleatório se cancela — um ganho de razão sinal-ruído que nenhuma técnica de processamento posterior consegue replicar. É por isso que a etapa de campo mais cara de um levantamento sísmico não é "gravar mais forte", é "gravar de mais posições".

```
Geometria de cobertura múltipla (esquemático, um único CMP)

fonte1        fonte2         fonte3          fonte4
  \             \              \               \
   \             \              \               \
    \_____________\______________\_______________\____ superfície
                          |
                          | (todos os raios convergem
                          |  no mesmo ponto médio comum)
                          v
                     ponto refletor
                     em subsuperfície
```
Cada disparo ilumina o mesmo ponto em subsuperfície a partir de um ângulo diferente; empilhar os traços correspondentes reforça o sinal coerente e atenua o ruído — a razão de ser da cobertura múltipla (Sheriff & Geldart).

### Processamento: do dado bruto à seção interpretável

O dado bruto de campo não é interpretável diretamente — ele carrega múltiplas reflexões espúrias, distorções geométricas e ruído. Yilmaz organiza a cadeia convencional em torno de três processos principais, **nesta ordem**: deconvolução, empilhamento e migração — a ordem importa, porque cada um opera sobre um eixo diferente do dado (o tempo, o afastamento, o espaço) e o seguinte pressupõe o anterior já aplicado:

1. **Deconvolução**: comprime o pulso da fonte, que naturalmente tem duração finita, num pulso mais curto e nítido — melhorando a resolução vertical e removendo parte das reverberações (múltiplas de curto período). É aplicada ainda antes do empilhamento, sobre os traços individuais.
2. **Correção de NMO** (*normal moveout*) e empilhamento (*stacking*): compensa o fato de que, num mesmo CMP, o tempo de viagem cresce com o afastamento fonte-receptor (o raio percorre um caminho mais longo), alinhando os traços antes de somá-los.
3. **Migração** (*migration*): reposiciona geometricamente os refletores para seu local real em subsuperfície. Refletores inclinados e estruturas curvas (dobras, falhas, corpos de sal) aparecem distorcidos no dado empilhado bruto — a migração usa um modelo de velocidades para "desfazer" essa distorção. Sem migração, uma seção sísmica pode mostrar estruturas que sequer existem: o caso clássico é o *bow-tie*, o artefato de **foco enterrado** que um sinclinal fechado produz, aparecendo no dado não migrado como duas falsas antiformas cruzadas. Corpos de sal degradam a imagem por outro caminho — difrações nas bordas e distorção do campo de ondas pela alta velocidade do sal —, e não pelo mecanismo do *bow-tie*.
4. **Análise de velocidade e conversão tempo-profundidade**: toda a seção processada até aqui existe no domínio do tempo de viagem duplo (*two-way travel time*, TWT, em milissegundos), não em profundidade. Converter para profundidade exige um modelo de velocidades independente — tipicamente calibrado por perfis de poço (Aula 02) — e é uma fonte relevante de incerteza, porque pequenos erros de velocidade se acumulam em erros de profundidade crescentes com a espessura.

Um ponto que merece ênfase porque confunde iniciantes: a seção sísmica interpretada no dia a dia da indústria está, na maior parte dos casos, **em tempo**, não em profundidade. Duas camadas de mesma espessura real, mas velocidades diferentes, ocupam intervalos de tempo diferentes na seção — um efeito chamado de "pull-up" ou "pull-down" de velocidade, que pode simular uma estrutura (um alto ou um baixo) que não existe na profundidade real. Interpretar estrutura em seção de tempo sem cuidado é um dos erros mais recorrentes de quem começa na disciplina.

### Resolução sísmica: o que o dado consegue, de fato, distinguir

Toda medida física tem um limite de resolução, e a sísmica não é exceção. A **resolução vertical** — a menor espessura de camada que ainda produz reflexões distintas de topo e base, em vez de uma única reflexão combinada — é controlada pelo comprimento de onda dominante do pulso sísmico, λ = V/f, onde V é a velocidade da camada e f a frequência dominante do sinal. Aqui é preciso separar **dois limiares distintos**, cuja confusão é o erro mais comum do assunto — inclusive em material didático, que com frequência atribui a Widess um número que não é dele:

- **Critério de Rayleigh**, ou espessura de sintonia (*tuning thickness*), em torno de **λ/4**. É o limite prático de *separação visual*: abaixo dessa espessura, as reflexões de topo e base deixam de ser distinguíveis como dois eventos e passam a interferir num único refletor composto — e é exatamente na espessura de sintonia que a amplitude desse refletor composto atinge um máximo. É este o número que se usa no dia a dia quando se diz "a resolução vertical deste dado é X metros".
- **Limite de Widess (1973)**, em torno de **λ/8**. Widess mostrou que, abaixo dessa espessura, a *forma* da onda composta para de mudar — ela estabiliza, aproximando-se da derivada do pulso da fonte — e apenas a **amplitude** continua variando, de modo aproximadamente proporcional à espessura da camada. É esse comportamento que permite, com técnicas específicas de inversão, estimar espessuras bem abaixo do limite de separação visual; mas a informação geométrica direta (topo e base como superfícies mapeáveis) já se perdeu antes disso.

Em resumo: λ/4 é onde topo e base deixam de ser vistos separadamente; λ/8 é onde a camada deixa de ter qualquer expressão de forma própria e vira pura amplitude. Como a frequência sísmica útil decai com a profundidade (as altas frequências são absorvidas preferencialmente pela rocha), a resolução vertical piora sistematicamente com a profundidade: um levantamento típico de exploração pode resolver poucos metros perto da superfície e dezenas de metros a profundidades de vários quilômetros.

A **resolução horizontal** é controlada por um princípio diferente, a **zona de Fresnel**: a área da interface refletora que efetivamente contribui, de forma coerente, para a reflexão registrada num ponto da superfície — não um único ponto infinitesimal, mas um disco cujo raio cresce com a profundidade e com o comprimento de onda. Feições menores que a zona de Fresnel não são resolvidas individualmente; aparecem borradas ou somadas ao sinal de sua vizinhança. A migração (etapa 3 do processamento) reduz o tamanho efetivo da zona de Fresnel — é uma de suas funções, além do reposicionamento geométrico — e por isso a resolução horizontal de uma seção bem processada é significativamente melhor que a de um dado empilhado sem migração.

O saldo prático: um dado sísmico é excelente para mapear a geometria de grandes volumes de rocha e a arquitetura de pacotes deposicionais (o objeto de todo este módulo), mas tem um piso de resolução que nenhum processamento elimina — e é exatamente por isso que a amarração com dados de poço, que enxergam em escala de centímetros, é indispensável para calibrar o que o dado sísmico não consegue ver sozinho. Essa amarração é o tema da Aula 02.

## Exemplo trabalhado

**Situação:** um levantamento sísmico marítimo tem frequência dominante de 30 Hz numa camada com velocidade de 3.000 m/s. Qual é, aproximadamente, a resolução vertical nessa profundidade, e o que isso implica para identificar um reservatório de 8 m de espessura nessa área?

**Resolução:**

O comprimento de onda dominante é λ = V/f = 3.000/30 = 100 m. O critério de Rayleigh (λ/4) dá um limite de separação visual de aproximadamente 25 m — a espessura de sintonia: camadas mais espessas que isso geram reflexões de topo e base distintas; camadas mais finas produzem um único refletor composto, cuja amplitude pode até informar a espessura (por técnicas de inversão sísmica, fora do escopo desta aula), mas cuja geometria de topo e base não é separável diretamente na seção. O limite de Widess (λ/8) fica em cerca de 12,5 m — abaixo dele, a forma de onda já não muda mais, só a amplitude. Um reservatório de 8 m está abaixo dos dois limiares — a sísmica sozinha não vai "mostrar" esse reservatório como um par de refletores distintos. Na prática, seções assim são interpretadas com apoio de amarração de poço (Aula 02) e de técnicas de atributos sísmicos que exploram a amplitude do refletor composto, e não a separação visual de topo e base. A conclusão de trabalho não é "a sísmica é inútil aqui" — é "a sísmica sozinha não resolve essa espessura, e qualquer interpretação de reservatório fino exige integração com dado de poço e, idealmente, modelagem de amplitude".

## Recap relâmpago

- A sísmica de reflexão mede tempo de viagem e amplitude de ondas refletidas em contrastes de **impedância acústica** (Z = ρ·V); um refletor marca um contraste de impedância, não necessariamente um contato litológico — ponto que só se resolve com amarração de poço.
- O coeficiente de reflexão RC = (Z₂ − Z₁)/(Z₂ + Z₁) formaliza essa relação e é a base de toda leitura quantitativa de amplitude sísmica — é uma razão de **amplitudes**; a fração de energia refletida é RC².
- A **cobertura múltipla** (CMP) é o alicerce da aquisição: iluminar o mesmo ponto em subsuperfície de várias posições permite empilhar traços, reforçando o sinal coerente e atenuando o ruído (Sheriff & Geldart).
- O processamento (deconvolução → NMO/empilhamento → migração → conversão tempo-profundidade, nessa ordem) transforma o dado bruto em seção interpretável; sem migração, um sinclinal fechado aparece como duas falsas antiformas cruzadas (*bow-tie*, foco enterrado), e a maior parte da interpretação de rotina ocorre em domínio de tempo, não de profundidade.
- A **resolução vertical** é limitada pelo comprimento de onda dominante, com **dois** limiares que não se confundem: **λ/4** (critério de Rayleigh, espessura de sintonia) é onde topo e base deixam de ser separáveis visualmente; **λ/8** (limite de Widess, 1973) é onde a forma de onda estabiliza e só a amplitude ainda responde à espessura. Ambos pioram com a profundidade; a **resolução horizontal** é limitada pela zona de Fresnel, reduzida pela migração. Nenhum processamento elimina esse piso de resolução — ele é o motivo estrutural pelo qual a sismoestratigrafia depende de poços para calibração.

## Próxima aula

[[11-sismoestratigrafia-aula-02-perfilagem-e-resolucao|Aula 02 — Propriedades físicas das rochas, perfilagem de poços, amarração poço-sísmica e resolução]]

## Anterior

[[11-sismoestratigrafia-modulo|Módulo 11 — Sismoestratigrafia (hub)]]

## Fontes

- Sheriff, R. E. & Geldart, L. P. (1995), *Exploration Seismology*, 2ª ed., Cambridge University Press, cap. 1–4 e 9 (aquisição, cobertura múltipla, processamento, resolução).
- Widess, M. B. (1973), "How thin is a thin bed?", *Geophysics*, 38(6), p. 1176–1180 (limite de camada fina, ~λ/8: estabilização da forma de onda e amplitude proporcional à espessura).
- Kallweit, R. S. & Wood, L. C. (1982), "The limits of resolution of zero-phase wavelets", *Geophysics*, 47(7), p. 1035–1046 (comparação formal entre o critério de Rayleigh/sintonia, ~λ/4, e o limite de Widess, ~λ/8).
- Yilmaz, Ö. (2001), *Seismic Data Analysis: Processing, Inversion, and Interpretation of Seismic Data*, SEG, cap. 1 e 4 (deconvolução, migração).
- Mitchum, R. M., Vail, P. R. & Sangree, J. B. (1977), "Seismic stratigraphy and global changes of sea level, part 6: stratigraphic interpretation of seismic reflection patterns in depositional sequences", em Payton, C. E. (org.), *Seismic Stratigraphy — Applications to Hydrocarbon Exploration*, AAPG Memoir 26, p. 117–133 (fundamentos da leitura estratigráfica de dados sísmicos).

<!--
nivel: avancado
palavras_corpo: 1894 (Conteudo ate Exemplo trabalhado, recontagem apos auditoria cientifica e revisao didatica 2026-08-30)
mapa_objetivo_secao:
  geologia-avancado-m11-oa01: "O que a sísmica de reflexão mede, de fato" + "Aquisição: como o dado nasce em campo" + "Processamento: do dado bruto à seção interpretável" + "Resolução sísmica: o que o dado consegue, de fato, distinguir" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: SISMO-M11-A01-IMPEDANCIA-001
    claim: "Um refletor sísmico se forma em qualquer interface com contraste de impedância acústica (Z = densidade x velocidade); a fração da AMPLITUDE incidente refletida em incidência normal é dada pelo coeficiente de reflexão RC = (Z2-Z1)/(Z2+Z1), sendo a fração de ENERGIA refletida igual a RC ao quadrado. Um refletor sísmico marca um contraste de impedância acústica, não necessariamente um contato litológico ou uma superfície temporal por si só."
    risk: fato
    source: "Sheriff & Geldart 1995, cap. 3-4"
    audit: "corrigido em 2026-08-30 (SISMO-M11-A01-RC-006): a versao original dizia 'fracao de energia', o que confunde razao de amplitude com razao de energia"
  - claim_id: SISMO-M11-A01-CMP-002
    claim: "A cobertura múltipla (CMP - common midpoint) é o método padrão de aquisição sísmica de reflexão: pares fonte-receptor em posições diferentes que compartilham o mesmo ponto médio de subsuperfície são registrados e posteriormente empilhados após correção de NMO, aumentando a razão sinal-ruído em relação a um único disparo."
    risk: fato
    source: "Sheriff & Geldart 1995, cap. 1 e 4"
  - claim_id: SISMO-M11-A01-PROCESSAMENTO-003
    claim: "A cadeia de processamento sísmico convencional se organiza, na ordem, em torno de tres processos principais - deconvolucao (compressao do pulso da fonte, melhora de resolucao vertical, aplicada antes do empilhamento), correcao de NMO e empilhamento, e migracao (reposicionamento geometrico dos refletores, colapso do artefato bow-tie de foco enterrado produzido por sinclinais fechados) - seguidos de analise de velocidade e conversao tempo-profundidade calibrada por dados de poco; a maior parte da interpretacao sismica de rotina ocorre no dominio do tempo de viagem duplo (TWT), nao em profundidade."
    risk: fato
    source: "Yilmaz 2001, cap. 1 e 4 (ordem deconvolucao-empilhamento-migracao); Sheriff & Geldart 1995, cap. 9"
    audit: "corrigido em 2026-08-30 (SISMO-M11-A01-ORDEM-007 e -BOWTIE-008): a ordem estava invertida (NMO/empilhamento antes da deconvolucao) e o bow-tie estava atribuido tambem a domos de sal"
  - claim_id: SISMO-M11-A01-WIDESS-004
    claim: "A resolucao vertical sismica tem DOIS limiares distintos, que nao devem ser confundidos: o criterio de Rayleigh, ou espessura de sintonia (tuning thickness), em torno de lambda/4, abaixo do qual as reflexoes de topo e base deixam de ser separaveis visualmente e a amplitude do refletor composto atinge um maximo; e o limite de Widess (1973), em torno de lambda/8, abaixo do qual a forma da onda composta estabiliza (aproximando-se da derivada do pulso da fonte) e apenas a amplitude continua variando, de forma aproximadamente proporcional a espessura. O numero usado na pratica como 'resolucao vertical' e o lambda/4 de Rayleigh, NAO o lambda/8 de Widess."
    risk: fato
    source: "Widess 1973, Geophysics 38(6), p. 1176-1180; Kallweit & Wood 1982, Geophysics 47(7), p. 1035-1046"
    audit: "corrigido em 2026-08-30 (achado vermelho): a versao original atribuia o criterio lambda/4 a Widess 1973. Widess propos lambda/8; lambda/4 e o criterio de Rayleigh / espessura de sintonia"
  - claim_id: SISMO-M11-A01-FRESNEL-005
    claim: "A resolução horizontal da sísmica de reflexão é controlada pelo tamanho da zona de Fresnel, a área da interface refletora que contribui coerentemente para a reflexão registrada; o raio dessa zona cresce com a profundidade e com o comprimento de onda, e a migração sísmica reduz o tamanho efetivo da zona de Fresnel, melhorando a resolução horizontal em relação ao dado não migrado."
    risk: fato
    source: "Sheriff & Geldart 1995, cap. 4 e 9; Yilmaz 2001, cap. 4"
-->
