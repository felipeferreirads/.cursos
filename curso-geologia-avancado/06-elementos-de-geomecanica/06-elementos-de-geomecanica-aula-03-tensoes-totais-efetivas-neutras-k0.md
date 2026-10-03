# Aula 03: Tensões totais, efetivas e neutras; pressões geostáticas e o coeficiente K0

**ID:** geologia-avancado-m06-a03
**Módulo:** [[06-elementos-de-geomecanica-modulo|Módulo 06 — Elementos de geomecânica]]
**Duração estimada:** ~28 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** aplicar o princípio das tensões efetivas de Terzaghi para calcular o perfil de tensões totais, neutras e efetivas ao longo de um perfil de solo com nível d'água, incluindo os casos de franja capilar e de fluxo ascendente, e estimar a tensão horizontal geostática pelo coeficiente de empuxo em repouso K0.

**Pré-requisito:** Aula 02 deste módulo (pesos específicos γ, γsat e γsub); noção de tensão normal e de convenção de compressão positiva, do Módulo 05, Aula 01.

## Antes de começar, você precisa saber

- Que peso específico saturado (γsat) é o peso total por unidade de volume de um solo com todos os vazios cheios de água, e que γsub = γsat − γw (Aula 02).
- Que, em geotecnia, **compressão é positiva** (mesma convenção do Módulo 05).
- Que o peso específico da água é γw ≈ 9,81 kN/m³ (frequentemente arredondado para 10 kN/m³ em estimativas).

## Conteúdo

### O problema: por que a tensão total não prevê o comportamento

Considere dois pontos, ambos a 10 m de profundidade em depósitos de areia idênticos. No primeiro, o nível d'água está na superfície; no segundo, o terreno está seco. A tensão vertical total no primeiro ponto é maior (a água pesa e contribui para a carga), e no entanto é o **segundo** ponto — o mais "leve" em tensão total — que apresenta maior resistência ao cisalhamento. A tensão total, sozinha, prevê o comportamento mecânico ao contrário.

A resolução desse paradoxo é o resultado mais importante da mecânica dos solos: a resistência e a deformação de um solo não são governadas pela tensão total que atua sobre ele, mas pela parcela dessa tensão efetivamente transmitida através do **contato entre os grãos**. A água nos vazios, sendo um fluido, não transmite cisalhamento e não empurra os grãos uns contra os outros — ela apenas os envolve, com uma pressão igual em todas as direções.

### O princípio das tensões efetivas de Terzaghi

Enunciado por Karl Terzaghi em 1923–1925, o princípio decompõe a tensão normal total num ponto em duas parcelas:

**σ' = σ − u**

onde:
- **σ** é a **tensão total** (ou normal total): a força total por unidade de área, incluindo a contribuição de sólidos e de água;
- **u** é a **poropressão**, também chamada de **pressão neutra** (o adjetivo "neutra" é a razão do nome: sendo isotrópica, ela não tem efeito de cisalhamento — é "neutra" quanto à resistência);
- **σ'** é a **tensão efetiva**: a parcela transmitida pelo esqueleto sólido, e a única que controla resistência ao cisalhamento e variação de volume.

O princípio tem duas partes, e a segunda é frequentemente esquecida: (1) a tensão efetiva é σ − u; e (2) **todo efeito mensurável de uma mudança de tensão — compressão, distorção, mudança de resistência — deve-se exclusivamente a mudanças na tensão efetiva.** É a segunda parte que dá ao princípio seu poder preditivo: se σ e u aumentam igualmente, σ' não muda e o solo não sente nada.

> [!important] Por que a poropressão "alivia" a carga sem remover peso
> Aumentar u não retira massa nenhuma do sistema — a tensão total continua a mesma. O que muda é a divisão do trabalho: a água, ao ser pressurizada, passa a suportar uma fatia maior da carga total, e sobra menos carga para ser transmitida grão a grão. Como só o contato grão a grão gera atrito, a resistência cai. É por isso que a poropressão é o mecanismo central de deslizamentos deflagrados por chuva: a chuva não adiciona peso suficiente para explicar a ruptura — ela eleva u, reduz σ' e derruba a resistência disponível.

### Cálculo do perfil geostático (nível d'água hidrostático)

Num perfil horizontal, sem fluxo, as três grandezas se calculam por soma de camadas, de cima para baixo:

- **Tensão total vertical:** σv = Σ (γi · hi) — soma do peso específico de cada camada pela sua espessura. Acima do nível d'água usa-se γ (natural ou seco); abaixo dele, γsat.
- **Poropressão:** u = γw · zw, onde zw é a altura da coluna d'água acima do ponto (a profundidade abaixo do nível d'água). Acima do NA, na condição hidrostática simples, u = 0.
- **Tensão efetiva vertical:** σ'v = σv − u.

Um atalho útil e muito usado: abaixo do nível d'água, e **somente na condição hidrostática (sem fluxo)**, subtrair u de σv equivale a acumular o peso específico submerso, ou seja σ'v = Σ(γi·hi) acima do NA + Σ(γsub,i·hi) abaixo do NA. Os dois caminhos dão o mesmo número.

> [!warning] O atalho de γsub só vale sem fluxo
> Acumular γsub é uma consequência da hipótese hidrostática (u = γw·zw), não uma definição de tensão efetiva. Havendo fluxo vertical — ascendente ou descendente —, u deixa de ser γw·zw e o atalho passa a dar resultado errado. Nesse caso volte sempre à definição: calcule σv, calcule u a partir da carga hidráulica real, e subtraia.

### Franja capilar: poropressão negativa

Acima do nível d'água, a água pode subir por capilaridade nos vazios finos, formando a **franja capilar**. Nessa zona a água está sob **tensão** (sucção), e a poropressão é **negativa**: u = −γw·hc, onde hc é a altura acima do NA.

Uma poropressão negativa, aplicada a σ' = σ − u, **aumenta** a tensão efetiva (subtrair um negativo soma). Esse é o mecanismo físico da chamada "coesão aparente" das areias úmidas: um castelo de areia se sustenta porque a sucção capilar aumenta σ' entre os grãos, e desmorona quando seca (a sucção some) ou quando é submerso (u passa a positivo). O adjetivo "aparente" registra que não se trata de coesão verdadeira — nenhuma cimentação foi criada —, e sim de um ganho de resistência friccional emprestado da sucção, que desaparece com ela.

### Tensão horizontal geostática e o coeficiente K0

Tudo acima trata da direção vertical. A tensão horizontal geostática é obtida a partir dela pelo **coeficiente de empuxo em repouso**:

**K0 = σ'h / σ'v**

Note que **K0 relaciona tensões efetivas, não totais** — é um dos erros de aplicação mais comuns. Para obter a tensão horizontal total, calcule σ'h = K0·σ'v e depois some a poropressão de volta: σh = σ'h + u.

"Em repouso" significa que o solo não sofreu deformação lateral (condição de deformação lateral nula, εh = 0), a situação típica de um depósito que se formou por sedimentação sucessiva sem movimento horizontal. Estimativas de K0:

- Pela **elasticidade**, sob deformação lateral nula: K0 = ν/(1−ν) — a mesma expressão vista no Módulo 05, Aula 05 para maciços rochosos. É teoricamente limpa, mas depende de um ν que raramente se conhece bem em solo.
- Pela **correlação de Jáky (1944)**, muito mais usada na prática para solos **normalmente adensados**: K0 ≈ 1 − sen φ', onde φ' é o ângulo de atrito efetivo (Aula 06). Para φ' = 30°, K0 ≈ 0,5. Vale registrar que essa forma simples é a **aproximação prática** derivada por Jáky de uma expressão teórica mais longa — K0 = (1 − sen φ)(1 + ⅔ sen φ)/(1 + sen φ) —; as duas diferem por poucos por cento na faixa usual de φ', e a forma simplificada é a universalmente adotada.
- Para solos **sobreadensados** (que já suportaram tensão maior no passado — conceito desenvolvido na Aula 05), K0 é maior, podendo ultrapassar 1: a descarga não devolve a tensão horizontal na mesma proporção em que devolve a vertical, e parte do empuxo horizontal fica "presa" no depósito. A correção usual é K0,SA ≈ K0,NA · (OCR)^sen φ'.

> [!important] K0 é um estado, não uma propriedade
> K0 não é uma constante do material como Gs. Ele descreve o estado de tensão de um depósito que não se deformou lateralmente. Se o solo é escavado, carregado por uma fundação ou empurrado por uma cortina, a condição de repouso é rompida e o estado migra para empuxo ativo (Ka, solo se expande lateralmente) ou passivo (Kp, solo é comprimido lateralmente) — estados diferentes, com coeficientes diferentes, para o mesmo solo.

### Fluxo ascendente e o gradiente crítico

Se houver fluxo de água **ascendente** através do solo (por exemplo, no fundo de uma escavação abaixo do nível d'água), a poropressão em profundidade fica **maior** que a hidrostática. Como σv não muda, σ'v cai. Aumentando o gradiente hidráulico o suficiente, σ'v chega a zero: os grãos deixam de transmitir carga uns aos outros e o solo perde toda a resistência friccional — fenômeno chamado de **areia movediça**, *quicksand*, ou ruptura hidráulica de fundo (*heave*).

O gradiente hidráulico que anula a tensão efetiva é o **gradiente crítico**:

**icr = γsub/γw = (Gs−1)/(1+e)**

Para valores típicos (Gs ≈ 2,65, e ≈ 0,65), icr ≈ 1,0 — daí a regra prática, muito difundida, de que o gradiente crítico é próximo da unidade. Essa é a ponte direta para a Aula 04, onde o gradiente hidráulico é definido formalmente e medido.

## Exemplo trabalhado

**Situação:** um perfil tem 4 m de areia acima do nível d'água (γ = 17 kN/m³), seguidos de 6 m de areia saturada (γsat = 20 kN/m³). O nível d'água está a 4 m de profundidade. Calcule σv, u e σ'v a 10 m de profundidade, e estime σ'h e σh nesse ponto, sabendo que a areia é normalmente adensada com φ' = 32°. Use γw = 9,81 kN/m³.

**Resolução:**

Tensão total a 10 m — soma das duas camadas:
σv = (17 × 4) + (20 × 6) = 68 + 120 = **188 kPa**

Poropressão a 10 m — altura de coluna d'água acima do ponto = 10 − 4 = 6 m:
u = 9,81 × 6 = **58,9 kPa**

Tensão efetiva vertical:
σ'v = 188 − 58,9 = **129,1 kPa**

*Conferência pelo atalho do peso submerso* (válido aqui, pois o perfil é hidrostático, sem fluxo):
γsub da camada saturada = 20 − 9,81 = 10,19 kN/m³
σ'v = (17 × 4) + (10,19 × 6) = 68 + 61,1 = 129,1 kPa. Confere.

Coeficiente de empuxo em repouso, por Jáky:
K0 = 1 − sen 32° = 1 − 0,530 = **0,470**

Tensão horizontal efetiva:
σ'h = 0,470 × 129,1 = **60,7 kPa**

Tensão horizontal total — soma-se a poropressão de volta (a água pressiona igualmente em todas as direções):
σh = 60,7 + 58,9 = **119,6 kPa**

**Interpretação:** a água reduz a tensão efetiva vertical em quase um terço (de 188 para 129 kPa), e é esse valor reduzido — não os 188 kPa — que governa a resistência disponível nesse ponto. Note também que σ'h < σ'v (K0 < 1), o estado normal de um depósito sedimentar não sobreadensado: o solo é "mais apertado" verticalmente do que lateralmente. Se esse mesmo perfil sofresse erosão de vários metros de cobertura, tornando-se sobreadensado, K0 subiria e a relação poderia até se inverter.

## Erros comuns

- **Aplicar K0 à tensão total** (σh = K0·σv) em vez de à efetiva. O caminho correto é σ'h = K0·σ'v e depois σh = σ'h + u. Aplicar à total subestima σh sempre que houver água.
- **Usar o atalho do peso submerso em situação com fluxo.** γsub só reproduz σ' na condição hidrostática; com fluxo ascendente ou descendente é obrigatório calcular u a partir da carga hidráulica real.
- **Somar γsat acima do nível d'água** por descuido de leitura do perfil, ou continuar com γ natural abaixo dele — os dois erros deslocam todo o perfil de tensões.
- **Tratar poropressão negativa como impossível** e zerar u na franja capilar. A sucção é real, aumenta σ' e explica a estabilidade temporária de taludes e escavações em solo úmido não saturado.
- **Confundir "tensão neutra" com "tensão nula".** Neutra significa isotrópica e sem efeito de cisalhamento, não ausente — seu valor pode ser alto.

## O que não concluir

- **Que a água sempre reduz a resistência do solo.** Poropressão *positiva* reduz σ'; sucção (poropressão negativa, solo não saturado) aumenta σ' e a resistência. O sinal de u é que decide, não a presença de água.
- **Que a tensão efetiva é uma tensão de contato real medida entre grãos.** É uma grandeza macroscópica definida por σ − u, extraordinariamente eficaz como preditor de comportamento, mas não é a tensão física nos pontos de contato intergranular (que é muito maior, pois a área real de contato é ínfima).
- **Que K0 ≈ 0,5 vale para qualquer solo.** Isso decorre de Jáky com φ' ≈ 30° em solo normalmente adensado. Argilas rijas sobreadensadas podem ter K0 > 1, e usar 0,5 nesses casos subestima gravemente o empuxo sobre estruturas de contenção.

## Recap relâmpago

- O princípio de Terzaghi, σ' = σ − u, e sua segunda metade: **toda** mudança de resistência ou de volume decorre de mudança na tensão efetiva, nunca da total isolada.
- Perfil geostático: σv por acúmulo de γ·h (γ acima do NA, γsat abaixo); u = γw·zw; σ'v = σv − u. O atalho de acumular γsub abaixo do NA equivale a isso, **mas só sem fluxo**.
- Na franja capilar u é negativa, o que aumenta σ' e gera a "coesão aparente" — resistência emprestada da sucção, que some ao secar ou ao saturar.
- K0 = σ'h/σ'v relaciona tensões **efetivas**; estima-se por K0 ≈ 1 − sen φ' (Jáky, solo normalmente adensado) ou ν/(1−ν) (elasticidade). Solos sobreadensados têm K0 maior, podendo passar de 1.
- Fluxo ascendente eleva u e reduz σ'v; quando o gradiente atinge icr = γsub/γw = (Gs−1)/(1+e) ≈ 1, a tensão efetiva zera e ocorre areia movediça.

## Próxima aula

[[06-elementos-de-geomecanica-aula-04-percolacao-em-meios-porosos-e-fissurados|Aula 04 — Percolação de água em meios porosos e fissurados]]

## Anterior

[[06-elementos-de-geomecanica-aula-02-indices-fisicos-e-compactacao|Aula 02 — Índices físicos de solos e rochas e compactação]]

## Fontes

- Princípio das tensões efetivas: Terzaghi, K. (1925), *Erdbaumechanik auf bodenphysikalischer Grundlage*, Deuticke; formulação moderna em Terzaghi, K., Peck, R. B. & Mesri, G. (1996), *Soil Mechanics in Engineering Practice*, 3ª ed., Wiley, cap. 2.
- Cálculo de tensões geostáticas, franja capilar e gradiente crítico: Das, B. M. (2019), *Fundamentos de Engenharia Geotécnica*, 9ª ed., Cengage, cap. 8–9.
- Coeficiente de empuxo em repouso (correlação empírica): Jáky, J. (1944), "The coefficient of earth pressure at rest", *Journal of the Society of Hungarian Architects and Engineers*, 78(22), p. 355–358; extensão para solos sobreadensados em Mayne, P. W. & Kulhawy, F. H. (1982), "K0–OCR relationships in soil", *Journal of the Geotechnical Engineering Division, ASCE*, 108(GT6), p. 851–872.
- Relação elástica K0 = ν/(1−ν) sob deformação lateral nula: Jaeger, J. C., Cook, N. G. W. & Zimmerman, R. W. (2007), *Fundamentals of Rock Mechanics*, 4ª ed., Blackwell, cap. 11 (retomando o Módulo 05, Aula 05).

<!--
nivel: avancado
palavras_corpo: ~1850

mapa_objetivo_secao:
  geologia-avancado-m06-oa02: "O problema: por que a tensão total não prevê o comportamento" + "O princípio das tensões efetivas de Terzaghi" + "Cálculo do perfil geostático (nível d'água hidrostático)" + "Franja capilar: poropressão negativa" + "Tensão horizontal geostática e o coeficiente K0" + "Fluxo ascendente e o gradiente crítico" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOMEC-M06-A03-TERZAGHI-001
    claim: "O princípio das tensões efetivas de Terzaghi é σ'=σ−u, e todo efeito mensurável (resistência, variação de volume) decorre de mudanças na tensão efetiva, não na total."
    risk: fato
    source: "Terzaghi 1925; Terzaghi, Peck & Mesri 1996, cap. 2"
  - claim_id: GEOMEC-M06-A03-PERFIL-002
    claim: "No perfil geostático hidrostático, σv=Σγi·hi (γ acima do NA, γsat abaixo), u=γw·zw, e σ'v=σv−u equivale a acumular γsub abaixo do NA — equivalência válida apenas sem fluxo."
    risk: fato
    source: "Das 2019, cap. 8"
  - claim_id: GEOMEC-M06-A03-CAPILAR-003
    claim: "Na franja capilar a poropressão é negativa (u=−γw·hc), o que aumenta a tensão efetiva e gera a chamada coesão aparente."
    risk: fato
    source: "Das 2019, cap. 8"
  - claim_id: GEOMEC-M06-A03-K0-004
    claim: "K0=σ'h/σ'v relaciona tensões efetivas; estimado por K0≈1−sen φ' (Jáky 1944, forma simplificada da expressão original (1−sen φ)(1+⅔ sen φ)/(1+sen φ)) para solos normalmente adensados, por ν/(1−ν) pela elasticidade, e corrigido por (OCR)^sen φ' para sobreadensados, podendo exceder 1."
    risk: fato
    source: "Jáky 1944; Mayne & Kulhawy 1982; Das 2019, cap. 9"
  - claim_id: GEOMEC-M06-A03-ICR-005
    claim: "O gradiente hidráulico crítico que anula a tensão efetiva é icr=γsub/γw=(Gs−1)/(1+e), próximo de 1 para valores típicos (Gs≈2,65, e≈0,65)."
    risk: fato
    source: "Das 2019, cap. 9"
-->
