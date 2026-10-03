# Aula 02: Densidade, propriedades elásticas e propagação de ondas sísmicas

**ID:** geologia-avancado-m15-a02
**Módulo:** [[15-petrofisica-modulo|Módulo 15 — Introdução à petrofísica]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** relacionar densidade, módulos elásticos e velocidades sísmicas (Vp, Vs) entre si e com a composição mineral, a porosidade e o fluido de poro de uma rocha.
**Ao final você vai conseguir:** distinguir densidade de grão, de matriz e bulk (aparente); explicar o que os módulos elásticos (bulk, cisalhamento, Young) medem fisicamente; calcular Vp e Vs a partir de módulos elásticos e densidade; e explicar por que a razão Vp/Vs é sensível ao fluido de poro enquanto Vs sozinha praticamente não é.
**Pré-requisito:** [[15-petrofisica-aula-01-meios-porosos-porosidade-permeabilidade-controles-geologicos|Aula 01]] — porosidade e seus controles geológicos reaparecem aqui como um dos fatores que determinam densidade e velocidade sísmica.

## Conteúdo

### Três densidades que não são a mesma coisa

Em petrofísica, "densidade" sem qualificação é uma armadilha, porque existem pelo menos três densidades distintas em jogo:

A **densidade de grão** (ou densidade mineral) é a densidade do material sólido que compõe a rocha, sem contar o espaço poroso — por exemplo, quartzo puro tem densidade de grão de cerca de 2,65 g/cm³, calcita cerca de 2,71 g/cm³, e dolomita cerca de 2,85 g/cm³. A **densidade de matriz** é essencialmente a mesma ideia aplicada a uma rocha real, que costuma ser uma mistura de minerais — um arenito quartzoso puro tem densidade de matriz próxima da do quartzo, mas um arenito arcosiano (com feldspato) ou um arenito com cimento carbonático terá densidade de matriz diferente, ponderada pela proporção de cada mineral. A **densidade bulk** (ou aparente, ρ_b) é a densidade da rocha inteira, incluindo os poros e o que quer que os preencha — água, óleo, gás ou ar:

ρ_b = (1 − φ) × ρ_matriz + φ × ρ_fluido

Essa equação, embora simplificada, já deixa claro o ponto central da aula: a densidade bulk de uma rocha real depende de **três coisas independentes** — a composição mineral (via densidade de matriz), a porosidade (φ) e o fluido que ocupa os poros. Duas rochas de composição mineral idêntica podem ter densidades bulk bem diferentes só por causa da porosidade; e a mesma rocha porosa pode mudar de densidade bulk conforme muda o fluido de poro (água substituindo gás, por exemplo) — um princípio explorado diretamente pela gravimetria (Módulo 16) e pela sísmica de reservatório (monitoramento 4D).

Como referência de ordem de grandeza, arenitos têm densidade bulk tipicamente entre 2,0 e 2,6 g/cm³ (variando principalmente com a porosidade), calcários e dolomitos entre cerca de 2,3 e 2,8 g/cm³, folhelhos entre 1,8 e 2,8 g/cm³ (a faixa mais ampla, por causa da grande variação de porosidade com a profundidade de soterramento), granitos tipicamente entre 2,6 e 2,8 g/cm³, e basaltos entre cerca de 2,8 e 3,1 g/cm³ — mais densos que o granito porque trocam o par leve quartzo (2,65) mais feldspato alcalino (~2,56) por plagioclásio cálcico (~2,76), clinopiroxênio (3,2-3,4) e óxidos de Fe-Ti como a magnetita (5,2, e por isso influente mesmo em pequena proporção). A olivina (3,3-4,4) entra nessa conta apenas nas variedades olivínicas: ela não é fase essencial de todo basalto, e o contraste de densidade com o granito já se explica sem ela.

### Módulos elásticos: o que cada um mede fisicamente

Um corpo elástico responde a uma tensão aplicada com uma deformação proporcional, e a constante de proporcionalidade é um **módulo elástico**. Quatro módulos aparecem com frequência em petrofísica, e vale entender o que cada um mede antes de usar as fórmulas:

O **módulo de compressibilidade** (ou módulo volumétrico, *bulk modulus*, K) mede a resistência de um material a mudar de **volume** sob pressão hidrostática (compressão igual em todas as direções) — quanto maior K, mais incompressível o material. É o módulo relevante para descrever como um fluido (que não resiste a cisalhamento, só a compressão) se comporta dentro dos poros.

> **Cuidado com a letra K.** Ela carrega três significados diferentes ao longo deste curso, e nenhum deles é errado — são convenções estabelecidas em disciplinas distintas que este módulo atravessa. No Módulo 01 (hidrogeologia), **K** é a **condutividade hidráulica**. Na Aula 01 deste módulo, **k** minúsculo é a **permeabilidade intrínseca**. Daqui em diante, nesta aula, **K** maiúsculo é o **módulo de compressibilidade** — nada a ver com fluxo de fluido. Sempre que encontrar um K, identifique primeiro de qual disciplina o texto está falando.

O **módulo de cisalhamento** (ou de rigidez, *shear modulus*, G ou μ) mede a resistência de um material a mudar de **forma** sem mudar de volume, sob uma tensão de cisalhamento — quanto maior G, mais rígido o material a distorções. Este módulo é a chave de uma das ideias mais úteis da petrofísica sísmica: **fluidos não têm resistência ao cisalhamento** (G do fluido = 0, seja água, óleo ou gás), então o módulo de cisalhamento de uma rocha porosa saturada depende, em primeira aproximação, apenas do arcabouço sólido (a matriz mineral e seu arranjo), não do fluido que a satura.

O **módulo de Young** (E) mede a rigidez sob tração ou compressão uniaxial simples (a razão entre tensão e deformação num ensaio de tração de uma barra, por exemplo) — o módulo mais intuitivo, mas menos usado diretamente em sísmica, mais comum em geomecânica (Módulos 05-06 deste curso).

O **coeficiente de Poisson** (σ ou ν) mede a razão entre a deformação lateral e a deformação axial quando um material é comprimido numa direção — quanto maior, mais o material "incha" lateralmente ao ser comprimido. O valor **0,5 é o limite superior teórico**, e vale a pena ser exato sobre o que ele significa, porque a formulação apressada ("fluidos são incompressíveis") ensina o oposto do que a física diz: 0,5 corresponde a um material que **não muda de volume** ao ser deformado, isto é, perfeitamente **incompressível** — o que se obtém no limite em que K é muito grande em relação a G, ou, equivalentemente, em que **G tende a zero**. Incompressibilidade é uma propriedade **volumétrica**, não de cisalhamento. Rigorosamente, o coeficiente de Poisson nem sequer é definido para um fluido, que não sustenta tensão uniaxial; 0,5 é o valor a que as relações elásticas tendem quando G → 0, e é assim que se comporta uma suspensão ou uma areia fofa saturada. Rochas secas e consolidadas ficam tipicamente entre 0,1 e 0,3; as mesmas rochas saturadas de água sobem para a faixa de 0,25 a 0,35, porque a água eleva K sem tocar em G — o mesmo mecanismo que a seção seguinte vai explorar para Vp e Vs.

Os quatro módulos não são independentes: dados dois quaisquer (mais a densidade), os outros podem ser calculados por relações da teoria da elasticidade isotrópica. Como referência de ordem de grandeza para rocha intacta, granito tem módulo de compressibilidade da ordem de dezenas de GPa (gigapascal) e módulo de cisalhamento de magnitude comparável; calcário denso situa-se em faixa semelhante ou algo mais rígida; arenitos porosos e pouco consolidados têm módulos muito mais baixos, que caem ainda mais à medida que a porosidade aumenta — a rigidez do arcabouço sólido é diluída pelo espaço poroso.

### De módulos elásticos a velocidades sísmicas

A física da propagação de ondas elásticas num meio conecta diretamente os módulos elásticos, a densidade e a velocidade de propagação de dois tipos de onda de corpo:

A **onda P** (primária, compressional) se propaga por compressão e dilatação sucessivas na direção de propagação — é a mais rápida das duas e a única que se propaga em fluidos (por isso é a única onda sísmica registrada dentro do núcleo externo líquido da Terra). Sua velocidade é:

Vp = √[(K + 4G/3) / ρ]

A **onda S** (secundária, de cisalhamento) se propaga por deformação perpendicular à direção de propagação — depende exclusivamente do módulo de cisalhamento, e por isso **não se propaga em fluidos** (G = 0 para líquidos e gases):

Vs = √(G / ρ)

Essas duas equações são o elo formal entre esta aula e a anterior: densidade (que depende de composição, porosidade e fluido) e os módulos elásticos (que dependem de composição, textura, porosidade e, no caso de K, também do fluido) determinam juntos a velocidade sísmica de qualquer rocha — a grandeza que a sísmica de reflexão e refração (assunto de módulos geofísicos posteriores) efetivamente mede em campo.

Como consequência direta de Vs depender só de G (que o fluido não altera) e Vp depender também de K (que o fluido altera, porque um fluido incompressível resiste mais à mudança de volume do que um espaço vazio ou um gás): **saturar uma rocha porosa com água, no lugar de gás, aumenta Vp mas deixa Vs praticamente inalterada.** Esse é o princípio físico por trás de uma das aplicações mais valiosas da sísmica de reservatório — identificar contatos gás-água e distinguir rocha saturada de gás de rocha saturada de água a partir de anomalias de amplitude sísmica (o fenômeno popularmente chamado de "bright spot"). A razão **Vp/Vs**, por reunir os dois efeitos num único número, é sensível tanto à litologia quanto ao fluido, e por isso é usada como indicador combinado nos dois sentidos: rochas carbonáticas tendem a razões Vp/Vs mais altas (da ordem de 1,8 a 1,9) que arenitos limpos (tipicamente entre 1,6 e 1,8), e, dentro de uma mesma litologia, a razão tende a subir quando a saturação de água aumenta em relação à de gás.

### Velocidades sísmicas típicas por litologia

Como ordem de grandeza — valores reais dependem fortemente de porosidade, pressão de confinamento, fraturamento e saturação —, arenitos cobrem a faixa mais ampla de Vp de todas as rochas comuns, de pouco mais de 1,5 km/s em areia inconsolidada rasa a mais de 4-5 km/s em arenito bem cimentado e pouco poroso; calcários e dolomitos **densos** situam-se tipicamente entre 4 e 7 km/s, mais rápidos que arenitos de porosidade equivalente — mas essa faixa vale para o carbonato de baixa porosidade, e desaba com a porosidade que a Aula 01 mostrou ser possível em carbonatos: uma greda (*chalk*) muito porosa fica em torno de 2,3-2,6 km/s, mais lenta que a maioria dos arenitos, e é o contraexemplo mais limpo de que a litologia sozinha não fixa a velocidade; folhelhos ficam tipicamente entre 2 e 4 km/s; granitos entre cerca de 5 e 6 km/s; e basaltos entre cerca de 5,5 e 6,5 km/s — entre as rochas mais rápidas da crosta superior, refletindo tanto a baixíssima porosidade quanto a rigidez elástica mais alta de sua composição máfica. Esses números explicam por que um perfil sísmico de reflexão mostra fortes refletores nos contatos entre litologias distintas: é justamente o contraste de **impedância acústica** — o produto de densidade por velocidade — entre camadas adjacentes que gera a reflexão que o método detecta.

## Exemplo trabalhado

**Situação:** um calcário saturado com água tem densidade bulk de 2,55 g/cm³, módulo de compressibilidade (K) de 40 GPa e módulo de cisalhamento (G) de 19 GPa.

**Pergunta:** calcule Vp e Vs dessa rocha, e a razão Vp/Vs. Em seguida, avalie qualitativamente o que aconteceria a Vp, a Vs e à razão Vp/Vs se essa mesma rocha, com a mesma porosidade e o mesmo arcabouço sólido, estivesse saturada com gás em vez de água.

**Resolução:**

Primeiro, converter as unidades para o Sistema Internacional coerente: ρ = 2.550 kg/m³, K = 40 × 10⁹ Pa, G = 19 × 10⁹ Pa.

Vp = √[(K + 4G/3) / ρ] = √[(40×10⁹ + 4×19×10⁹/3) / 2.550] = √[(40×10⁹ + 25,33×10⁹) / 2.550] = √[65,33×10⁹ / 2.550] = √(2,562×10⁷) ≈ **5.062 m/s ≈ 5,06 km/s**

Vs = √(G / ρ) = √(19×10⁹ / 2.550) = √(7,451×10⁶) ≈ **2.730 m/s ≈ 2,73 km/s**

Razão Vp/Vs = 5.062 / 2.730 ≈ **1,85**

Os três valores caem dentro das faixas típicas de calcário saturado de água apresentadas nas seções anteriores: Vp de 5,06 km/s dentro dos 4-7 km/s dos carbonatos densos, e Vp/Vs de 1,85 dentro dos 1,8-1,9 das rochas carbonáticas.

**Um caso-limite que vale conhecer, porque é a armadilha vizinha.** Se G fosse 24 GPa em vez de 19, com o mesmo K, teríamos Vp²/Vs² = K/G + 4/3 = 3 exatamente, ou seja **Vp/Vs = √3 ≈ 1,73** — que corresponde a um coeficiente de Poisson de exatamente 0,25, o chamado **sólido de Poisson**. Esse é o valor característico de arenito limpo consolidado e de granito, **não** de calcário saturado. Uma razão Vp/Vs de 1,73 num intervalo que o intérprete supunha carbonático é, por si só, motivo para desconfiar da litologia atribuída — e é por isso que 1,73 e 1,85 não são dois números parecidos, mas duas litologias diferentes.

**Qualitativo — mesma rocha saturada com gás:** trocar a água por gás não muda G de forma relevante (gás, como água, tem módulo de cisalhamento praticamente nulo, então o arcabouço sólido continua respondendo da mesma forma ao cisalhamento) — **Vs permanece praticamente a mesma**, algo em torno de 2,73 km/s. Mas o gás é muito mais compressível que a água, então o **K efetivo da rocha saturada cai** (a rocha como um todo fica mais fácil de comprimir), o que **reduz Vp** — tipicamente de forma perceptível, ainda que a magnitude exata dependa da geometria dos poros e da saturação. Como Vp cai e Vs não muda, **a razão Vp/Vs também cai**. Esse padrão — Vs estável, Vp e Vp/Vs caindo com a presença de gás — é exatamente o que um intérprete de sísmica de reservatório procura ao investigar um possível contato gás-água num campo de petróleo.

## Erros comuns

- **Assumir que "K" significa a mesma coisa em qualquer aula do curso.** A própria aula avisa: K é condutividade hidráulica no Módulo 01, k minúsculo é permeabilidade na Aula 01 deste módulo, e K maiúsculo aqui é módulo de compressibilidade — mesma letra, três grandezas físicas completamente diferentes.
- **Usar "densidade" sem qualificar qual das três.** Densidade de grão, de matriz e bulk respondem a perguntas diferentes; comparar um valor de grão relatado por um laboratório com um valor bulk de perfil, como se fossem a mesma coisa, produz conclusão errada sobre porosidade ou composição.
- **Atribuir litologia carbonática só porque Vp está na faixa 4-7 km/s.** O contraexemplo da própria aula (greda porosa, 2,3-2,6 km/s) mostra que porosidade alta derruba a velocidade abaixo da de muitos arenitos — velocidade sozinha não fixa litologia.
- **Confundir Vp/Vs = 1,73 (sólido de Poisson, arenito/granito) com Vp/Vs = 1,8-1,9 (carbonato saturado).** Como o próprio exemplo trabalhado enfatiza, são duas litologias diferentes, não dois números "parecidos" — um intérprete que arredondar mentalmente entre eles atribui a rocha errada ao dado sísmico.

## O que não concluir

- **Que coeficiente de Poisson de 0,5 significa "fluido puro" na rocha.** É o limite de G → 0 (arcabouço sem resistência a cisalhamento), que uma areia fofa saturada ou uma suspensão também se aproxima — não é sinônimo de "só fluido, sem sólido".
- **Que trocar o fluido de poro muda G da rocha.** Fluidos têm módulo de cisalhamento nulo tanto água quanto gás — é K que muda com o fluido, e é por isso que Vs permanece praticamente estável enquanto Vp (e a razão Vp/Vs) caem com a presença de gás.
- **Que impedância acústica é o mesmo que velocidade sísmica.** É o produto de densidade por velocidade — duas rochas com a mesma velocidade mas densidades diferentes têm impedâncias diferentes, e é o contraste de impedância, não de velocidade isolada, que gera um refletor sísmico.

## Recap relâmpago

- Densidade de grão (mineral), densidade de matriz (mistura mineral da rocha) e densidade bulk (rocha inteira, incluindo poros e fluido) são três grandezas distintas; a densidade bulk depende de composição mineral, porosidade e fluido de poro simultaneamente.
- Módulo de compressibilidade (K) mede resistência a mudar de volume; módulo de cisalhamento (G) mede resistência a mudar de forma; módulo de Young (E) e coeficiente de Poisson (σ) completam o conjunto — os quatro se relacionam entre si pela teoria da elasticidade isotrópica.
- O coeficiente de Poisson tem 0,5 como limite superior teórico, atingido quando o material não muda de volume ao ser deformado (perfeitamente incompressível, ou G → 0) — incompressibilidade é propriedade volumétrica, não de cisalhamento. Rocha seca consolidada: 0,1-0,3; a mesma rocha saturada de água: 0,25-0,35.
- Fluidos têm módulo de cisalhamento nulo: por isso G de uma rocha saturada depende essencialmente do arcabouço sólido, não do fluido, enquanto K depende dos dois.
- Vp = √[(K + 4G/3)/ρ] é a única onda sísmica de corpo que se propaga em fluidos; Vs = √(G/ρ) não se propaga em fluidos, porque depende só de G.
- Trocar o fluido de poro (água por gás) reduz K e, portanto, Vp, mas deixa Vs praticamente inalterada — a razão Vp/Vs cai, e esse padrão é a base física da detecção sísmica de contatos gás-água.
- Ordens de grandeza típicas de Vp: arenitos 1,5-5 km/s (a faixa mais ampla, dominada pela porosidade), calcários/dolomitos densos 4-7 km/s — mas greda porosa cai para 2,3-2,6 km/s, mais lenta que arenito, porque a porosidade manda mais que a litologia —, folhelhos 2-4 km/s, granitos 5-6 km/s, basaltos 5,5-6,5 km/s; o contraste de impedância acústica (densidade × velocidade) entre camadas é o que gera reflexões sísmicas.
- Vp/Vs de 1,73 (= √3) corresponde a um coeficiente de Poisson de exatamente 0,25, o "sólido de Poisson": valor de arenito limpo consolidado e de granito, não de carbonato saturado (1,8-1,9). Confundir os dois é atribuir a litologia errada a partir do dado sísmico.

## Próxima aula

[[15-petrofisica-aula-03-magnetismo-das-rochas-e-radioatividade-natural|Aula 03 — Magnetismo das rochas e radioatividade natural]] — muda o campo físico explorado: em vez de ondas elásticas, a próxima aula trata de como minerais específicos tornam uma rocha magnética ou radioativa, dois contrastes igualmente centrais para a geofísica aplicada.

## Fontes

- Mavko, G., Mukerji, T. & Dvorkin, J. (2020), *The Rock Physics Handbook*, 3ª ed., Cambridge University Press, cap. 1-2 (definições de módulos elásticos, relações Vp-Vs-densidade, efeito do fluido sobre K e G).
- Schön, J. H. (2015), *Physical Properties of Rocks: Fundamentals and Principles of Petrophysics*, 2ª ed., Elsevier, cap. 4-6 (densidade de grão/matriz/bulk, módulos elásticos e velocidades sísmicas por litologia).
- Telford, W. M., Geldart, L. P. & Sheriff, R. E. (1990), *Applied Geophysics*, 2ª ed., Cambridge University Press, cap. 4 (velocidades sísmicas típicas por litologia, densidade de rochas).
- Christensen, N. I. (1996), "Poisson's ratio and crustal seismology", *Journal of Geophysical Research*, 101(B2) (razões Vp/Vs típicas por litologia, incluindo o contraste carbonato-arenito).

<!--
nivel: avancado
palavras_corpo: 2406
mapa_objetivo_secao:
  geologia-avancado-m15-oa02: "Três densidades que não são a mesma coisa" + "Módulos elásticos: o que cada um mede fisicamente" + "De módulos elásticos a velocidades sísmicas" + "Velocidades sísmicas típicas por litologia" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: PETROFIS-M15-A02-DENSIDADEGRAO-001
    claim: "Densidade de grão típica: quartzo cerca de 2,65 g/cm3, calcita cerca de 2,71 g/cm3, dolomita cerca de 2,85 g/cm3. Densidade bulk = (1-phi) x densidade de matriz + phi x densidade do fluido."
    risk: fato
    source: "Schön 2015, Physical Properties of Rocks, cap. 4; Ellis & Singer 2007, Well Logging for Earth Scientists, cap. 1 (densidades de grão mineral de referência para perfilagem)"
  - claim_id: PETROFIS-M15-A02-DENSIDADEBULK-002
    claim: "Ordens de grandeza de densidade bulk: arenitos 2,0-2,6 g/cm3; calcários/dolomitos 2,3-2,8 g/cm3; folhelhos 1,8-2,8 g/cm3; granitos 2,6-2,8 g/cm3; basaltos 2,8-3,1 g/cm3, mais densos que o granito por serem mais ricos em minerais ferromagnesianos (piroxênio, olivina) e mais pobres em quartzo/feldspato alcalino."
    risk: aproximacao
    source: "Schön 2015, Physical Properties of Rocks, cap. 4, tabelas de densidade por litologia; Telford, Geldart & Sheriff 1990, Applied Geophysics, cap. 2. Faixas amplas e aproximadas dada a variabilidade real por porosidade e composição mineral especifica."
  - claim_id: PETROFIS-M15-A02-MODULOS-003
    claim: "Módulo de compressibilidade (K) mede resistência a mudança de volume sob pressão hidrostática; módulo de cisalhamento (G) mede resistência a mudança de forma sob tensão de cisalhamento; fluidos (líquidos e gases) têm módulo de cisalhamento nulo (G=0), portanto não resistem a cisalhamento."
    risk: fato
    source: "Mavko, Mukerji & Dvorkin 2020, The Rock Physics Handbook, cap. 1-2"
  - claim_id: PETROFIS-M15-A02-VPVSFORMULA-004
    claim: "Vp = raiz[(K + 4G/3)/rho] e Vs = raiz(G/rho), onde rho é a densidade bulk. A onda P se propaga em sólidos, líquidos e gases; a onda S depende exclusivamente do módulo de cisalhamento e não se propaga em fluidos."
    risk: fato
    source: "Mavko, Mukerji & Dvorkin 2020, The Rock Physics Handbook, cap. 2; Telford, Geldart & Sheriff 1990, Applied Geophysics, cap. 4 (equações de velocidade de onda elástica em meio isotrópico)"
  - claim_id: PETROFIS-M15-A02-FLUIDOVPVS-005
    claim: "Trocar o fluido de poro de água para gás reduz o módulo de compressibilidade efetivo (K) da rocha saturada, reduzindo Vp, mas deixa o módulo de cisalhamento (G) e, portanto, Vs, praticamente inalterados — a razão Vp/Vs cai. Esse padrão é a base física da identificação sísmica de contatos gás-água (anomalias de amplitude/'bright spot')."
    risk: fato
    source: "Mavko, Mukerji & Dvorkin 2020, The Rock Physics Handbook, cap. 1-2 (substituição de fluido, teoria de Gassmann, efeito sobre K vs G)"
  - claim_id: PETROFIS-M15-A02-VPVSRATIO-006
    claim: "Razão Vp/Vs típica: rochas carbonáticas na ordem de 1,8-1,9; arenitos limpos tipicamente entre 1,6 e 1,8. A razão tende a aumentar com o aumento da saturação de água em relação à de gás, dentro de uma mesma litologia."
    risk: aproximacao
    source: "Christensen 1996, Journal of Geophysical Research 101(B2):3139-3156, razões Vp/Vs e coeficientes de Poisson para 29 grupos de rochas (calcário ~0,31, correspondendo a Vp/Vs ~1,9; dolomito ~0,28, Vp/Vs ~1,81); Mavko, Mukerji & Dvorkin 2020, cap. 1 (efeito de saturação sobre Vp/Vs)"
  - claim_id: PETROFIS-M15-A02-EXEMPLOCALCARIO-008
    claim: "Exemplo trabalhado, calcário saturado de água: rho=2.550 kg/m3, K=40 GPa, G=19 GPa dão Vp=5.062 m/s, Vs=2.730 m/s e Vp/Vs=1,85 - dentro das faixas declaradas na aula (Vp 4-7 km/s e Vp/Vs 1,8-1,9 para carbonato). Caso-limite registrado: com G=24 GPa a razão seria exatamente raiz(3)=1,73, correspondente a coeficiente de Poisson 0,25 ('sólido de Poisson'), valor de arenito limpo e granito, NÃO de calcário saturado."
    risk: fato
    source: "Recalculado dígito a dígito na auditoria de 2026-09-08. CORREÇÃO VERMELHA: a redação original usava G=24 GPa, obtinha Vp/Vs=1,73 e afirmava que o valor caía 'dentro da faixa típica de calcário saturado de água' - contradizendo a faixa de 1,8-1,9 declarada na própria aula três parágrafos antes. G ajustado de 24 para 19 GPa; Vp, Vs, razão e o trecho qualitativo do gás recalculados; o caso-limite de 1,73 preservado como material de discriminação em vez de descartado."
  - claim_id: PETROFIS-M15-A02-VPLITOLOGIA-007
    claim: "Ordens de grandeza de Vp: arenitos 1,5-5 km/s; calcários/dolomitos DENSOS 4-7 km/s, com greda (chalk) de alta porosidade caindo para 2,3-2,6 km/s; folhelhos 2-4 km/s; granitos 5-6 km/s; basaltos 5,5-6,5 km/s. O contraste de impedância acústica (densidade x velocidade) entre camadas adjacentes gera as reflexões detectadas pela sísmica de reflexão."
    risk: aproximacao
    source: "Telford, Geldart & Sheriff 1990, Applied Geophysics, cap. 4; Schön 2015, cap. 6; SEG Wiki, Velocities in limestone and sandstone (greda 2.300-2.600 m/s; calcário em geral 3.500-6.000 m/s). Ressalva da greda acrescentada pela auditoria de 2026-09-08 (achado amarelo): a faixa 4-7 km/s sem qualificação contradizia a porosidade de 30-40% que a Aula 01 deste mesmo módulo atribui a carbonatos."
  - claim_id: PETROFIS-M15-A02-POISSONLIMITE-009
    claim: "O coeficiente de Poisson tem 0,5 como limite superior teórico, correspondente a deformação sem mudança de volume - isto é, incompressibilidade (K >> G, ou G tendendo a zero). Incompressibilidade é propriedade VOLUMÉTRICA, não de cisalhamento. Poisson não é rigorosamente definido para um fluido, que não sustenta tensão uniaxial; 0,5 é o limite das relações elásticas quando G tende a zero. Rocha seca consolidada 0,1-0,3; saturada de água 0,25-0,35."
    risk: fato
    source: "Mavko, Mukerji & Dvorkin 2020, The Rock Physics Handbook, cap. 1 (relações entre constantes elásticas isotrópicas); Christensen 1996, JGR 101(B2). CORREÇÃO LARANJA da auditoria de 2026-09-08: a redação original justificava o 0,5 como limite de 'material perfeitamente incompressível em cisalhamento', frase que troca a categoria da propriedade."
  - claim_id: PETROFIS-M15-A02-BASALTOMINERAL-010
    claim: "A densidade maior do basalto frente ao granito vem da troca de quartzo (2,65) e feldspato alcalino (~2,56) por plagioclásio cálcico (~2,76), clinopiroxênio (3,2-3,4) e óxidos de Fe-Ti (magnetita 5,2). A olivina (3,3-4,4) contribui apenas nas variedades olivínicas e NÃO é fase essencial de todo basalto."
    risk: fato
    source: "Consistência mineralógica com os módulos de petrologia ígnea do curso base e com a classificação IUGS/TAS. Correção amarela da auditoria de 2026-09-08: a redação original citava 'piroxênio, olivina' como causa geral da densidade do basalto, generalizando uma fase acessória."
-->
