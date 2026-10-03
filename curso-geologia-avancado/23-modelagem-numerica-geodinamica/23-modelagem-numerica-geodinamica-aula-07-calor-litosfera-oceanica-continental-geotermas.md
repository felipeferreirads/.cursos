# Aula 07: Calor na litosfera oceânica e continental — resfriamento e envelhecimento, geotermas estáveis e elementos produtores de calor

**ID:** geologia-avancado-m23-a07
**Módulo:** [[23-modelagem-numerica-geodinamica-modulo|Módulo 23 — Introdução à modelagem numérica geodinâmica]]
**Duração estimada:** ~28 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** calcular a geoterma e o fluxo de calor da litosfera oceânica pelo modelo de resfriamento de semi-espaço, e da litosfera continental em regime estável com produção radiogênica, e interpretar os controles de cada um.
**Ao final você vai conseguir:** calcular a temperatura a uma dada profundidade e idade de litosfera oceânica pelo modelo de resfriamento de semi-espaço; explicar por que o fluxo de calor e a profundidade batimétrica oceânicos escalam com a raiz quadrada da idade; explicar a relação linear de Lachenbruch entre fluxo de calor superficial e produção radiogênica crustal; e comparar os controles que governam a geoterma oceânica (idade, resfriamento condutivo) e a continental (produção radiogênica, fluxo de calor de base) em regime estável.
**Pré-requisito:** [[23-modelagem-numerica-geodinamica-aula-06-solucao-numerica-calor-explicito-implicito|Aula 06 deste módulo]] (solução numérica da equação do calor) e, antes dela, a Aula 05 (a formulação física do calor, de onde vêm κ e a equação da difusão).

## Conteúdo

### Litosfera oceânica: o modelo de resfriamento de semi-espaço

A litosfera oceânica nasce quente na cordilheira meso-oceânica — onde manto ascendente cristaliza e adere à base da placa — e esfria à medida que se afasta da crista, ficando mais espessa, mais densa e mais profunda (subsidindo) com o tempo. O modelo mais simples e mais usado para descrever esse resfriamento é o de **resfriamento de semi-espaço** (*half-space cooling*): trata a litosfera recém-formada como um semi-espaço homogêneo, inicialmente a uma temperatura uniforme T_m (a temperatura do manto), com a superfície mantida subitamente a 0 °C a partir do instante t=0 (o instante de formação na crista), e deixa a equação de difusão de calor da Aula 05 — sem produção, sem advecção — evoluir livremente a partir daí. Esse é exatamente o tipo de problema **simplificado com solução analítica** que a Aula 02 mencionou: a equação ∂T/∂t = κ∂²T/∂z² com essas condições de contorno específicas tem solução fechada, expressa pela **função erro** (erf):

T(z, t) = T_m · erf( z / (2√(κt)) )

onde z é a profundidade abaixo do topo da litosfera, t é o tempo decorrido desde a formação (a **idade** da litosfera naquele ponto) e κ é a difusividade térmica. A função erro cresce de 0 (em z=0, onde a condição de contorno fixa T=0) até se aproximar de 1 para argumentos grandes (longe da superfície, onde T se aproxima de T_m, a temperatura do manto não perturbado) — o formato exato de uma frente de resfriamento se propagando progressivamente para maior profundidade à medida que t aumenta.

Uma consequência direta e muito usada na prática é que a **profundidade** de qualquer isoterma de referência (por exemplo, a isoterma que define a base da litosfera térmica) cresce proporcionalmente a √t, e o **fluxo de calor superficial** — proporcional ao gradiente de temperatura na superfície, pela lei de Fourier — decresce proporcionalmente a 1/√t. Essa é a raiz da famosa relação **q ∝ 1/√idade** e **profundidade batimétrica ∝ √idade** observada em toda a litosfera oceânica jovem a intermediária: quanto mais nova a crosta oceânica, mais raso o fundo do mar e maior o fluxo de calor; quanto mais velha, mais profunda e com fluxo de calor menor. Essa relação em √t se ajusta muito bem para litosfera com menos de aproximadamente 70-80 Ma; além dessa idade, dados observados de batimetria e fluxo de calor se achatam em relação à previsão do modelo de semi-espaço puro — um desvio conhecido como o "problema do achatamento" (*flattening*), que motivou refinamentos como o **modelo de placa** (Parsons & Sclater, 1977) e sua atualização GDH1 (Stein & Stein, 1992), que impõem um limite de espessura à litosfera (mantida por calor de baixo) em vez de deixá-la esfriar indefinidamente — um refinamento que esta aula menciona, mas não desenvolve, mantendo o foco no modelo de semi-espaço como base conceitual.

### Litosfera continental: regime estável com produção radiogênica

Diferente da litosfera oceânica, que se forma e esfria continuamente ao longo de dezenas de milhões de anos, a litosfera continental antiga tende a um **regime termicamente estável** (∂T/∂t ≈ 0) em escalas de tempo muito mais longas que seu próprio envelhecimento — sua geoterma deixa de ser controlada pela "idade" de resfriamento e passa a ser controlada por dois fatores locais: a **produção radiogênica** de calor na própria crosta (decaimento de urânio, tório e potássio, concentrados sobretudo na crosta superior, mais rica em elementos incompatíveis) e o **fluxo de calor de base**, vindo do manto sob a litosfera. Sob regime estável, a equação de calor da Aula 05 perde o termo de tempo e, sem advecção, se reduz a uma **equação diferencial ordinária** no espaço — κ d²T/dz² + A(z)/(ρCp) = 0 —, resolúvel por integração direta. É o critério da Aula 02 operando na prática: com o termo temporal eliminado, resta uma única variável independente (a profundidade z), e uma equação de uma só variável independente é, por definição, uma EDO, não uma EDP. Note que a notação acompanha: o ∂ das derivadas parciais dá lugar ao d das derivadas totais.

A relação de Lachenbruch, que fecha esta seção, sai dessa integração em dois passos. Vale segui-los separadamente, porque juntos eles ficam densos demais.

**Passo 1 — o fluxo de calor acumula a produção que está acima dele.** A taxa de variação do fluxo de calor com a profundidade é, em módulo, exatamente igual à produção local — consequência direta da lei de Fourier combinada com a conservação de energia em regime estável. O sinal depende da convenção adotada, e vale fixá-la aqui: com z orientado **para baixo** e q_z a componente do fluxo de Fourier nessa mesma direção (q_z = −k dT/dz), tem-se dq_z/dz = A(z). Traduzido para a grandeza que o geofísico mede e reporta — o fluxo **ascendente**, q = k dT/dz, positivo por convenção —, a mesma relação vira dq/dz = −A(z): o fluxo que sobe **cresce** à medida que se aproxima da superfície, porque vai acumulando tudo o que foi produzido acima de cada nível. Nos dois casos a conclusão prática é a mesma, e é só ela que importa daqui para a frente: **toda a produção radiogênica acima de uma profundidade contribui, somada, ao fluxo de calor que emerge na superfície.**

**Passo 2 — dar uma forma a A(z) e integrar.** Modela-se a produção radiogênica como decaindo exponencialmente com a profundidade:

A(z) = A₀ · e^(−z/hr)

onde A₀ é a produção na superfície e hr é a **espessura de escala** da camada produtora — a profundidade em que a produção cai a 1/e do valor de superfície. Essa forma é usada desde Lachenbruch (1970) porque reproduz o empobrecimento observado em elementos radioativos com a profundidade crustal. Integrando-a segundo o passo 1, chega-se à célebre **relação linear de Lachenbruch** entre o fluxo de calor superficial q₀ e a produção A₀:

q₀ = q_r + A₀ · hr

onde q_r é o **fluxo de calor reduzido** — o fluxo que restaria se toda a camada produtora fosse removida, essencialmente o fluxo vindo de baixo dela (crosta profunda e manto). Essa relação linear é um resultado empírico e teórico clássico da geofísica de fluxo de calor continental, verificado em várias províncias geológicas ao comparar medidas de fluxo de calor superficial com a produção radiogênica medida em amostras de superfície de diferentes profundidades de exumação — quando várias localidades de uma mesma província são plotadas num gráfico q₀ contra A₀, os pontos tendem a cair sobre uma reta, cuja inclinação estima hr e cujo intercepto estima q_r.

### Interpretando os dois controles lado a lado

A comparação entre os dois regimes é o ponto central desta aula: a litosfera **oceânica** tem uma geoterma controlada essencialmente por um único parâmetro — sua **idade** — através de um processo puramente condutivo e transiente (o calor "esquece" progressivamente a condição inicial quente da crista); a litosfera **continental**, em contraste, atinge um regime **estável** onde a geoterma reflete a distribuição vertical de fontes de calor radiogênicas na própria crosta e o fluxo vindo de baixo, praticamente independente de quando aquela crosta se formou (desde que tenha tido tempo suficiente — tipicamente dezenas a centenas de milhões de anos — para relaxar termicamente após qualquer perturbação, como um evento de espessamento orogênico, cujas consequências térmicas a Aula 09 retoma). É por isso que geotermas continentais antigas e estáveis (crátons) são caracteristicamente mais frias, a uma dada profundidade, do que a litosfera oceânica jovem: não porque o cráton seja mais velho no sentido de "mais tempo esfriando" (ele já esfriou por completo há muito tempo, atingindo o regime estável), mas porque sua geoterma estável de equilíbrio é controlada por um balanço diferente de fontes de calor — tipicamente com fluxo de calor de base e produção radiogênica crustal bem menores do que o calor "represado" na litosfera oceânica jovem logo após sua formação na cordilheira.

## Exemplo trabalhado

**Situação 1 — temperatura na litosfera oceânica aos 60 Ma, a 30 km de profundidade.** Use o modelo de semi-espaço com T_m = 1350 °C e κ = 1 × 10⁻⁶ m²/s (um valor de difusividade térmica típico usado em modelos de litosfera).

```python
import numpy as np
from scipy.special import erf

Tm = 1350.0            # temperatura do manto, C
kappa = 1e-6            # difusividade termica, m2/s
z = 30_000.0             # profundidade, m (30 km)
idade_Ma = 60.0
t = idade_Ma * 1e6 * 365.25 * 24 * 3600   # idade convertida para segundos

eta = z / (2 * np.sqrt(kappa * t))
T = Tm * erf(eta)
print(eta, T)
```

**Conferindo à mão:** t = 60×10⁶ × 31.557.600 s ≈ 1,893×10¹⁵ s. κt = 10⁻⁶ × 1,893×10¹⁵ = 1,893×10⁹ m². √(κt) ≈ 43.510 m, logo 2√(κt) ≈ 87.030 m. η = 30.000 / 87.030 ≈ **0,345**. Consultando (ou interpolando) uma tabela da função erro: erf(0,34) ≈ 0,3694 e erf(0,35) ≈ 0,3794; interpolando linearmente para η≈0,345, erf(η) ≈ 0,374. T ≈ 1350 × 0,374 ≈ **505 °C** a 30 km de profundidade, aos 60 Ma. **Saída esperada do código:** valores próximos de `eta ≈ 0.345` e `T ≈ 505` (o resultado exato de `scipy.special.erf` pode diferir da interpolação manual na segunda casa decimal, um efeito esperado de arredondamento na interpolação de tabela). O número em si é ilustrativo — depende do valor de κ e T_m escolhidos, ambos parâmetros médios da litosfera — mas a ordem de grandeza e a tendência (mais fria em relação à temperatura de manto quanto mais rasa e mais jovem a litosfera) são o ponto central do exemplo.

**Situação 2 — a relação de Lachenbruch aplicada a uma província continental.** Uma província tem produção radiogênica de superfície A₀ = 2,5 µW/m³, espessura de escala hr = 10 km, e fluxo de calor reduzido q_r = 30 mW/m². Calcule o fluxo de calor superficial esperado.

q₀ = q_r + A₀ · hr = 30 mW/m² + (2,5 µW/m³ × 10.000 m)

Convertendo unidades: 2,5 µW/m³ × 10.000 m = 25.000 µW/m² = 25 mW/m² (dividindo por 1.000 para passar de µW para mW). Logo:

q₀ = 30 + 25 = **55 mW/m²**

Esse valor está na faixa típica de fluxo de calor continental estável observado em muitas províncias graníticas maduras (tipicamente entre 40 e 70 mW/m², variando com a província), o que reforça o papel da produção radiogênica crustal como controle de primeira ordem sobre o fluxo de calor continental — bem diferente do controle por idade que domina o caso oceânico da Situação 1.

## Recap relâmpago

- O modelo de **resfriamento de semi-espaço** dá T(z,t) = T_m·erf(z/(2√(κt))) para a litosfera oceânica: a geoterma é controlada essencialmente pela **idade** da crosta, com profundidade de uma isoterma ∝ √idade e fluxo de calor ∝ 1/√idade.
- Esse ajuste em √t vale bem até ~70-80 Ma; litosfera mais velha "achata" em relação à previsão do modelo puro, o que motivou modelos de placa mais refinados (Parsons & Sclater 1977; GDH1, Stein & Stein 1992), mencionados mas não desenvolvidos aqui.
- A litosfera **continental** antiga atinge regime **estável** (∂T/∂t≈0): a equação de calor se reduz a uma EDO no espaço, controlada pela **produção radiogênica** crustal A(z) e pelo **fluxo de calor de base** — não mais pela idade de formação.
- A **relação de Lachenbruch**, q₀ = q_r + A₀·hr, liga linearmente o fluxo de calor superficial à produção radiogênica de superfície e à espessura de escala da camada produtora — um resultado clássico e testável empiricamente província por província.
- Geotermas oceânicas e continentais respondem a controles físicos distintos: transiente e dependente de idade (oceânica) versus estável e dependente da distribuição de fontes radiogênicas e do fluxo de base (continental) — a comparação central desta aula.

## Próxima aula

[[23-modelagem-numerica-geodinamica-aula-08-reologia-rochas-viscosidade-fluencia|Aula 08 — Reologia das rochas: viscosidade efetiva, elasticidade, fluência por difusão e por deslocamento, reologia crustal e mantélica]] — como a temperatura calculada aqui entra, de forma exponencial, no cálculo da viscosidade que controla o fluxo do manto e da litosfera.

## Fontes

- Modelo de resfriamento de semi-espaço, solução por função erro e a relação √idade para profundidade batimétrica e fluxo de calor oceânicos: Turcotte, D. L. & Schubert, G., *Geodynamics*, 3ª ed. (2014), Cambridge University Press, capítulo 4.
- Modelo de placa como refinamento do resfriamento de semi-espaço para litosfera oceânica mais velha, e o efeito de achatamento (*flattening*): Parsons, B. & Sclater, J. G. (1977), "An analysis of the variation of ocean floor bathymetry and heat flow with age", *Journal of Geophysical Research*, 82(5), 803-827; Stein, C. A. & Stein, S. (1992), "A model for the global variation in oceanic depth and heat flow with lithospheric age", *Nature*, 359, 123-129.
- Produção radiogênica crustal decaindo exponencialmente com a profundidade e a relação linear de Lachenbruch entre fluxo de calor superficial e produção: Lachenbruch, A. H. (1970), "Crustal temperature and heat production: Implications of the linear heat-flow relation", *Journal of Geophysical Research*, 75(17), 3291-3300; Turcotte & Schubert, *Geodynamics*, 3ª ed., capítulo 4.
- Geotermas continentais estáveis em regime cratônico e sua relação com produção radiogênica e fluxo de base: Turcotte & Schubert, *Geodynamics*, 3ª ed., capítulo 4.

<!--
nivel: avancado
palavras_corpo: 2362
mapa_objetivo_secao:
  geologia-avancado-m23-oa03: "Litosfera oceânica: o modelo de resfriamento de semi-espaço" + "Litosfera continental: regime estável com produção radiogênica" + "Interpretando os dois controles lado a lado" + "Exemplo trabalhado"

nota_de_revisao_didatica: 'Aula RENUMERADA de 05 para 07 em 2026-09-19, sem divisao, por causa das divisoes das antigas Aulas 03 e 04. Os claim_id foram DELIBERADAMENTE MANTIDOS com o prefixo A05, que designa a aula antes da renumeracao, para nao quebrar a rastreabilidade com o manifesto 23-modelagem-numerica-geodinamica-auditoria.json. NAO RENUMERAR. UNICA alteracao de conteudo (achado DID-M23-A05-DENSIDADE-006): o paragrafo que derivava a relacao de Lachenbruch era, depois da correcao do achado laranja 4 da auditoria cientifica (SINALFLUXO-008), o mais denso do modulo - cerca de 300 palavras encadeando a relacao dq/dz, as duas convencoes de sinal, a conclusao, o modelo exponencial de A(z), a espessura de escala e a integracao final. Foi quebrado em dois passos rotulados, com a forma A(z) = A0*exp(-z/hr) promovida a formula destacada. NENHUM fato foi alterado ou removido, e a correcao da auditoria esta integralmente preservada, palavra por palavra, dentro do Passo 1. UNICO acrescimo: a definicao de espessura de escala como a profundidade em que a producao cai a 1/e do valor de superficie - que nao e fato novo, e a leitura direta da formula exponencial ja presente, e fecha uma lacuna real (o termo era nomeado em negrito e nunca definido).'

alegacoes_auditaveis:
  - claim_id: GEODIN-M23-A05-SEMIESPACO-001
    claim: "O modelo de resfriamento de semi-espaco para litosfera oceanica da a temperatura T(z,t) = Tm * erf(z/(2*sqrt(kappa*t))), com Tm a temperatura do manto, kappa a difusividade termica e t a idade da litosfera; disso decorre que a profundidade de uma isoterma de referencia escala com a raiz quadrada da idade e o fluxo de calor superficial escala com o inverso da raiz quadrada da idade."
    risk: fato
    source: "Turcotte & Schubert, Geodynamics, 3a ed. (2014), Cambridge University Press, cap. 4."
  - claim_id: GEODIN-M23-A05-ACHATAMENTO-002
    claim: "O ajuste do modelo de semi-espaco a dados observados de batimetria e fluxo de calor oceanicos e bom ate aproximadamente 70-80 Ma; litosfera mais velha apresenta um achatamento (flattening) em relacao a previsao do modelo puro, o que motivou o modelo de placa de Parsons & Sclater (1977) e sua atualizacao GDH1 de Stein & Stein (1992)."
    risk: fato
    source: "Parsons, B. & Sclater, J. G. (1977), Journal of Geophysical Research, 82(5), 803-827; Stein, C. A. & Stein, S. (1992), Nature, 359, 123-129."
  - claim_id: GEODIN-M23-A05-LACHENBRUCH-003
    claim: "Modelando a producao radiogenica crustal como decaindo exponencialmente com a profundidade, A(z) = A0 * exp(-z/hr), a integracao da equacao de calor em regime estavel leva a relacao linear de Lachenbruch entre o fluxo de calor superficial q0 e a producao de superficie A0: q0 = qr + A0*hr, onde qr e o fluxo de calor reduzido (vindo de baixo da camada produtora)."
    risk: fato
    source: "Lachenbruch, A. H. (1970), Journal of Geophysical Research, 75(17), 3291-3300; Turcotte & Schubert, Geodynamics, 3a ed., cap. 4."
  - claim_id: GEODIN-M23-A05-CONTROLES-OCEANICA-CONTINENTAL-004
    claim: "A geoterma da litosfera oceanica e controlada essencialmente por um processo condutivo transiente dependente da idade da crosta desde sua formacao na crista meso-oceanica, enquanto a geoterma da litosfera continental antiga atinge um regime termicamente estavel controlado pela distribuicao vertical de producao radiogenica crustal e pelo fluxo de calor de base, praticamente independente do momento de formacao da crosta continental."
    risk: fato
    source: "Turcotte & Schubert, Geodynamics, 3a ed. (2014), Cambridge University Press, cap. 4."
  - claim_id: GEODIN-M23-A05-SINALFLUXO-008
    claim: "Em regime estavel e sem adveccao, a taxa de variacao do fluxo de calor com a profundidade tem modulo igual a producao radiogenica local, e o SINAL depende da convencao: com z orientado para baixo e q_z a componente do fluxo de Fourier nessa direcao (q_z = -k dT/dz), vale dq_z/dz = A(z); para o fluxo ASCENDENTE q = k dT/dz, reportado como positivo na geofisica de fluxo de calor, vale dq/dz = -A(z), ou seja, o fluxo que sobe cresce em direcao a superficie ao acumular a producao de tudo o que esta acima."
    risk: fato
    source: "Turcotte & Schubert, Geodynamics, 3a ed. (2014), Cambridge University Press, cap. 4 (balanco de calor em regime estavel com producao)."
  - claim_id: GEODIN-M23-A05-EXEMPLO-ERF-005
    claim: "Para Tm=1350 C, kappa=1e-6 m2/s, z=30 km e idade=60 Ma, o parametro eta = z/(2*sqrt(kappa*t)) vale aproximadamente 0.345, e T = Tm*erf(eta) resulta em aproximadamente 505 C, um valor ilustrativo dependente dos parametros escolhidos."
    risk: calculo
    source: "Calculo aritmetico direto a partir da formula de resfriamento de semi-espaco apresentada na aula, reproduzivel com scipy.special.erf."
  - claim_id: GEODIN-M23-A05-EXEMPLO-LACHENBRUCH-006
    claim: "Para A0=2.5 microW/m3, hr=10 km e qr=30 mW/m2, a relacao de Lachenbruch da q0 = 30 + (2.5 microW/m3 * 10000 m convertido para mW/m2 = 25 mW/m2) = 55 mW/m2, valor dentro da faixa tipica observada em provincias continentais graniticas maduras (aproximadamente 40-70 mW/m2)."
    risk: calculo
    source: "Calculo aritmetico direto a partir da relacao de Lachenbruch apresentada na aula; faixa tipica de fluxo de calor continental estavel: Turcotte & Schubert, Geodynamics, 3a ed., cap. 4."
-->
