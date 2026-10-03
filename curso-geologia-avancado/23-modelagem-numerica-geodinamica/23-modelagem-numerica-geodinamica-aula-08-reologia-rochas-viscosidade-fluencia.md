# Aula 08: Reologia das rochas — viscosidade efetiva, elasticidade, fluência por difusão e por deslocamento, reologia crustal e mantélica

**ID:** geologia-avancado-m23-a08
**Módulo:** [[23-modelagem-numerica-geodinamica-modulo|Módulo 23 — Introdução à modelagem numérica geodinâmica]]
**Duração estimada:** ~28 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** explicar os regimes reológicos elástico, viscoso e frágil (este último representado nos códigos por um critério plástico friccional) da litosfera, distinguir fluência por difusão e por deslocamento, e calcular a viscosidade efetiva a partir de uma lei de fluência tipo Arrhenius, interpretando sua forte dependência da temperatura.
**Ao final você vai conseguir:** explicar por que a mesma rocha pode se comportar como sólido elástico, fluido viscoso ou material plástico dependendo da escala de tempo e do nível de tensão; diferenciar fluência por difusão (linear) de fluência por deslocamento (não linear) em termos da relação entre tensão e taxa de deformação; calcular a viscosidade efetiva a partir de uma lei de fluência do tipo Arrhenius; e explicar, com um exemplo numérico, por que um erro pequeno na temperatura calculada num modelo produz um erro de ordens de grandeza na viscosidade.
**Pré-requisito:** [[23-modelagem-numerica-geodinamica-aula-07-calor-litosfera-oceanica-continental-geotermas|Aula 07 deste módulo]] (geotermas oceânica e continental) — a temperatura calculada ali é o principal insumo da reologia desta aula.

## Conteúdo

### Um mesmo material, três comportamentos

A pergunta "a litosfera é rígida ou flui?" não tem uma resposta única — depende da **escala de tempo** da deformação e do **nível de tensão** envolvido. Em escala de tempo curta (segundos a minutos, como na propagação de uma onda sísmica, ou anos a décadas, como numa deformação elástica acumulada antes de um terremoto), a rocha se comporta como um sólido **elástico**: deforma-se proporcionalmente à tensão aplicada e recupera a forma original quando a tensão é removida — a base da sismologia e de boa parte da geodésia de deformação. Em escala de tempo longa (milhares a milhões de anos, como na convecção mantélica ou no rebote pós-glacial), a mesma rocha se comporta como um fluido **viscoso**: deforma-se continuamente sob tensão sustentada, sem "lembrar" nem recuperar sua forma original — o regime que domina toda a modelagem deste módulo a partir daqui. E, em tensões altas o suficiente (próximas à superfície, onde a pressão de confinamento é baixa), a rocha se rompe de forma **frágil** — falhamento, o regime da geologia estrutural clássica, fora do escopo deste módulo. Uma advertência de vocabulário que vale para toda a literatura de modelagem geodinâmica: você vai encontrar esse mesmo regime chamado de **plástico**, e as duas palavras não são sinônimas. Deformação plástica, no sentido da mecânica dos materiais, é permanente e **contínua**, sem perda de coesão — o oposto de uma ruptura. Elas viajam juntas por uma razão específica: um meio contínuo, por construção, não sabe abrir uma fratura discreta, de modo que os códigos representam o comportamento frágil por um **critério de escoamento plástico** de atrito (Mohr-Coulomb ou Drucker-Prager), que limita a tensão suportada em função da pressão. É uma representação numérica do frágil, não uma afirmação de que romper seja plástico.

Uma forma útil de organizar essa dependência é o **tempo de Maxwell** — a razão entre a viscosidade do material e seu módulo elástico de cisalhamento, uma escala de tempo característica acima da qual o comportamento viscoso domina sobre o elástico. Para rochas do manto, o tempo de Maxwell típico é da ordem de centenas a milhares de anos — muito mais curto que os milhões de anos das escalas de tempo geodinâmicas deste módulo (convecção mantélica, evolução de orógenos), o que justifica tratar o manto e a litosfera profunda como predominantemente **viscosos** nesses problemas, mesmo sabendo que, em escalas de tempo mais curtas (sismos, ajuste isostático imediato), o mesmo material responde de forma elástica.

### Fluência por difusão e por deslocamento: dois mecanismos, duas leis

O regime viscoso da litosfera e do manto, na prática, vem da **fluência** (*creep*) — deformação lenta e contínua no estado sólido, causada por mecanismos que operam na escala do cristal. Existem dois mecanismos principais, dominantes em condições diferentes de tensão, temperatura e tamanho de grão:

**Fluência por difusão** (*diffusion creep*) ocorre pelo movimento de vacâncias atômicas (defeitos pontuais na rede cristalina) através do grão ou ao longo de seus contornos, sob a ação de uma tensão diferencial — um mecanismo dominante em tensões baixas, temperaturas altas e grãos pequenos. Sua característica central é que a relação entre tensão (σ) e taxa de deformação (ε̇) é **linear** — dobrar a tensão dobra a taxa de deformação — o que faz da fluência por difusão um comportamento **Newtoniano**, formalmente equivalente à viscosidade de um fluido comum como a água (só que muitas ordens de grandeza mais viscoso).

**Fluência por deslocamento** (*dislocation creep*) ocorre pelo movimento de discordâncias (defeitos lineares) através da rede cristalina, um mecanismo dominante em tensões mais altas e, ao contrário da fluência por difusão, **independente do tamanho de grão**. Sua característica central é que a relação entre tensão e taxa de deformação é **não linear**: a taxa de deformação escala com a tensão elevada a um expoente n tipicamente entre 3 e 4 para minerais do manto (o olivino, o mineral dominante do manto superior, tem n ≈ 3,5 em muitas calibrações experimentais) — o que faz da fluência por deslocamento um comportamento **não Newtoniano**: dobrar a tensão mais que dobra (multiplica por 2ⁿ) a taxa de deformação, uma sensibilidade muito mais forte que a fluência por difusão.

Ambos os mecanismos seguem uma **lei de fluência** do tipo Arrhenius, que combina a dependência em tensão com uma forte dependência exponencial na temperatura absoluta:

ε̇ = A · σⁿ · exp(−Q / (RT))

onde A é uma constante pré-exponencial (específica do material e do mecanismo), n é o expoente de tensão (n=1 para fluência por difusão, n≈3-4 para fluência por deslocamento), Q é a **energia de ativação** do mecanismo (a barreira energética que o processo atômico precisa vencer), R é a constante universal dos gases, e T é a temperatura absoluta (em Kelvin). O termo exp(−Q/RT) — o **fator de Arrhenius** — é o motivo pelo qual pequenas variações de temperatura produzem variações enormes na taxa de deformação, e, por consequência, na viscosidade: é justamente esse termo que o exemplo trabalhado a seguir quantifica.

### Da lei de fluência à viscosidade efetiva

A **viscosidade efetiva** η_eff de um material em fluência se define, por analogia com um fluido Newtoniano, como a razão entre a tensão e duas vezes a taxa de deformação: η_eff = σ / (2ε̇). Substituindo a lei de fluência de Arrhenius nessa definição e isolando a viscosidade:

η_eff = (1 / (2A)) · σ^(1−n) · exp(Q / (RT))

Note o sinal do expoente da temperatura: enquanto a taxa de deformação cresce com a temperatura (exp(−Q/RT) aumenta quando T aumenta), a viscosidade **diminui** com a temperatura (exp(+Q/RT) diminui quando T aumenta) — fisicamente intuitivo: material mais quente flui mais facilmente, logo é menos viscoso. Para fluência por difusão (n=1), a viscosidade não depende da tensão aplicada, um comportamento Newtoniano puro; para fluência por deslocamento (n>1), a viscosidade também depende da tensão (através do expoente 1−n, negativo), o que faz da "viscosidade" um valor local, específico daquela combinação de tensão e temperatura, não uma propriedade fixa do material — daí o nome **efetiva**: ela descreve o comportamento instantâneo do material naquelas condições, não uma constante universal.

### Reologia crustal e mantélica: minerais diferentes, leis diferentes

A crosta e o manto têm reologias distintas porque são dominados por minerais diferentes, cada um com seus próprios parâmetros de lei de fluência calibrados experimentalmente: a crosta continental superior tem seu comportamento dúctil frequentemente aproximado pela lei de fluência do **quartzo** (mais fraco, flui em temperaturas relativamente baixas), enquanto a crosta inferior e o manto superior são governados por leis de fluência de minerais máficos e do **olivino**, respectivamente — muito mais resistentes, exigindo temperaturas bem mais altas para fluir na mesma taxa. Essa diferença de reologia entre camadas, combinada com a geoterma calculada na Aula 07, é o que produz a estrutura de resistência em camadas ("envelope de resistência", ou *strength envelope*) clássica da litosfera continental — uma crosta superior frágil, uma crosta inferior dúctil e relativamente fraca (o quartzo já flui a temperaturas moderadas), e um manto litosférico superior potencialmente mais resistente (o olivino exige temperaturas mais altas) antes de se tornar dúctil também — uma estrutura que a Aula 09 retoma diretamente ao discutir onde a litosfera continental se rompe durante a extensão.

## Exemplo trabalhado

**Situação: quanto uma diferença de 50 K na temperatura muda a viscosidade efetiva por fluência por deslocamento?** Use parâmetros ilustrativos, representativos da fluência por deslocamento de olivino seco (Q ≈ 540 kJ/mol — a energia de ativação da calibração de Karato & Wu, 1993; as calibrações experimentais publicadas para esse mecanismo se espalham por cerca de 430 a 560 kJ/mol, e Hirth & Kohlstedt, 2003, dão 530 ± 4 kJ/mol, de modo que o valor usado aqui está dentro da faixa, mas não é *o* número — a própria dispersão entre calibrações é parte do problema), e compare a viscosidade efetiva a T₁ = 1000 K e T₂ = 1050 K, mantendo tensão e os demais parâmetros fixos — de modo que a razão entre as duas viscosidades dependa **apenas** do fator de Arrhenius exp(Q/RT).

```python
import numpy as np

Q = 540_000.0      # energia de ativacao, J/mol (dislocation creep em olivino seco, Karato & Wu 1993)
R = 8.314           # constante dos gases, J/(mol*K)

T1 = 1000.0          # K
T2 = 1050.0          # K  (50 K mais quente)

razao = np.exp(Q/(R*T1) - Q/(R*T2))   # eta_eff(T1) / eta_eff(T2)
print(razao)
```

**Conferindo à mão:** Q/(R·T₁) = 540.000 / (8,314 × 1000) = 540.000 / 8.314 ≈ **64,95**. Q/(R·T₂) = 540.000 / (8,314 × 1050) = 540.000 / 8.729,7 ≈ **61,86**. A diferença dos expoentes é 64,95 − 61,86 = **3,09**. A razão de viscosidades é exp(3,09): como e³ ≈ 20,09 e e^0,09 ≈ 1,094, exp(3,09) ≈ 20,09 × 1,094 ≈ **22,0**. **Saída esperada do código:** `razao ≈ 22`.

Isto é: mantendo tudo o mais constante, uma litosfera 50 K mais fria que outra tem, pela mesma lei de fluência por deslocamento, uma viscosidade efetiva cerca de **22 vezes maior** — mais de uma ordem de grandeza de diferença por uma variação de temperatura que é perfeitamente plausível como erro numérico ou de parâmetro num modelo térmico real (a diferença entre um esquema explícito mal resolvido e um bem resolvido, por exemplo, ou entre duas escolhas razoáveis de condutividade térmica na Aula 05). É exatamente esse mecanismo — a sensibilidade exponencial da viscosidade à temperatura — que a introdução do módulo já havia adiantado como "ponto de dificuldade": erros pequenos no campo térmico se traduzem, através do fator de Arrhenius, em viscosidades erradas por ordens de grandeza, o que por sua vez muda drasticamente a velocidade e o padrão de qualquer fluxo mantélico ou litosférico calculado a partir dela na Aula 09.

## Recap relâmpago

- A mesma rocha se comporta como sólido **elástico** (escalas de tempo curtas), fluido **viscoso** (escalas de tempo longas, geodinâmicas) ou se rompe de forma **frágil** (tensões altas, próximo à superfície, onde a pressão de confinamento é baixa) — o tempo de Maxwell separa o regime elástico do viscoso, e para o manto é muito mais curto que as escalas de tempo deste módulo. Nos códigos, o regime frágil é *representado* por um critério de escoamento plástico friccional (Mohr-Coulomb / Drucker-Prager); "plástico" ali é o nome do modelo, não do processo.
- **Fluência por difusão** é linear em tensão (comportamento Newtoniano, n=1); **fluência por deslocamento** é não linear (n≈3-4 para o manto), dominando em tensões mais altas.
- Ambas seguem uma lei de Arrhenius, ε̇ = A·σⁿ·exp(−Q/RT), cuja inversão dá a **viscosidade efetiva**, η_eff = (1/2A)·σ^(1−n)·exp(Q/RT) — decrescendo exponencialmente com a temperatura.
- Crosta (quartzo, mais fraca) e manto (olivino, mais resistente) têm leis de fluência com parâmetros diferentes, produzindo a estrutura de resistência em camadas ("envelope de resistência") da litosfera continental.
- O exemplo numérico mostrou que uma diferença de apenas 50 K de temperatura pode mudar a viscosidade efetiva por um fator de ordem 20 — a sensibilidade exponencial que torna a precisão do campo térmico calculado nas Aulas 05-07 diretamente responsável pela qualidade de qualquer modelo reológico construído sobre ele.

## Próxima aula

[[23-modelagem-numerica-geodinamica-aula-09-extensao-colisao-continental-slab-pull-ridge-push|Aula 09 — Continentes em extensão e em colisão: ruptura continental, subsidência, evolução termal de orógenos, slab-pull, ridge-push e cunhas orogênicas]] — a síntese final do módulo, aplicando a reologia desta aula e o calor das Aulas 05-07 à análise quantitativa de continentes se estendendo ou colidindo.

## Fontes

- Regimes elástico, viscoso e plástico da litosfera e o tempo de Maxwell: Turcotte, D. L. & Schubert, G., *Geodynamics*, 3ª ed. (2014), Cambridge University Press, capítulo 7.
- Fluência por difusão e por deslocamento, leis de fluência tipo Arrhenius, e parâmetros experimentais de reologia de olivino e quartzo: Karato, S., *Deformation of Earth Materials: An Introduction to the Rheology of Solid Earth*, Cambridge University Press (2008); Hirth, G. & Kohlstedt, D. (2003), "Rheology of the upper mantle and the mantle wedge: A view from the experimentalists", em *Inside the Subduction Factory*, AGU Geophysical Monograph 138, 83-105 (E = 530 ± 4 kJ/mol para fluência por deslocamento em olivino seco).
- Energia de ativação Q = 540 kJ/mol usada no exemplo trabalhado, para fluência por deslocamento em olivino seco: Karato, S. & Wu, P. (1993), "Rheology of the upper mantle: A synthesis", *Science*, 260(5109), 771-778, DOI 10.1126/science.260.5109.771.
- Representação do comportamento frágil por critério de escoamento plástico friccional (Mohr-Coulomb / Drucker-Prager) em códigos de meio contínuo: Gerya, T., *Introduction to Numerical Geodynamic Modelling*, 2ª ed. (2019), Cambridge University Press, capítulo sobre reologia viscoelastoplástica.
- Viscosidade efetiva derivada da lei de fluência e sua dependência exponencial da temperatura: Turcotte & Schubert, *Geodynamics*, 3ª ed., capítulo 7; Ranalli, G., *Rheology of the Earth*, 2ª ed. (1995), Chapman & Hall.
- Envelope de resistência (*strength envelope*) da litosfera continental combinando reologia de crosta e manto: Ranalli, G. (1995), *Rheology of the Earth*, 2ª ed., Chapman & Hall, capítulo sobre perfis de resistência litosférica.

<!--
nivel: avancado
palavras_corpo: 2342
mapa_objetivo_secao:
  geologia-avancado-m23-oa04: "Um mesmo material, três comportamentos" + "Fluência por difusão e por deslocamento: dois mecanismos, duas leis" + "Da lei de fluência à viscosidade efetiva" + "Reologia crustal e mantélica: minerais diferentes, leis diferentes" + "Exemplo trabalhado"

nota_de_revisao_didatica: 'Aula RENUMERADA de 06 para 08 em 2026-09-19, sem divisao (2.342 palavras, ~28 min estimados, dentro do teto), por causa das divisoes das antigas Aulas 03 e 04. Os claim_id foram DELIBERADAMENTE MANTIDOS com o prefixo A06, que designa a aula antes da renumeracao, para nao quebrar a rastreabilidade com o manifesto 23-modelagem-numerica-geodinamica-auditoria.json. NAO RENUMERAR. Nenhuma alteracao de conteudo: apenas as remissoes internas a outras aulas foram atualizadas para a nova numeracao (Aula 05 -> Aula 07 para a geoterma, Aula 07 -> Aula 09 para extensao e colisao, Aulas 04-05 -> Aulas 05-07 para o campo termico).'

alegacoes_auditaveis:
  - claim_id: GEODIN-M23-A06-REGIMES-001
    claim: "A litosfera se comporta como solido elastico em escalas de tempo curtas (sismos, deformacao intersismica), como fluido viscoso em escalas de tempo geologicas longas (convecção mantelica, rebote pos-glacial) e se rompe de forma FRAGIL em tensoes altas proximo a superficie, onde a pressao de confinamento e baixa. Ruptura fragil e deformacao plastica nao sao a mesma coisa (a plastica e permanente e continua, sem perda de coesao): em codigos de meio continuo o regime fragil e REPRESENTADO por um criterio de escoamento plastico friccional (Mohr-Coulomb ou Drucker-Prager), porque um meio continuo nao abre fratura discreta. O tempo de Maxwell (razao entre viscosidade e modulo de cisalhamento elastico) separa o regime dominantemente elastico do dominantemente viscoso, sendo da ordem de centenas a milhares de anos para o manto, muito menor que escalas de tempo geodinamicas de milhoes de anos."
    risk: fato
    source: "Turcotte & Schubert, Geodynamics, 3a ed. (2014), Cambridge University Press, cap. 7."
  - claim_id: GEODIN-M23-A06-DIFUSAO-DESLOCAMENTO-002
    claim: "A fluencia por difusao (diffusion creep) tem relacao linear entre tensao e taxa de deformacao (comportamento newtoniano, expoente de tensao n=1) e depende do tamanho de grao; a fluencia por deslocamento (dislocation creep) tem relacao nao linear (expoente de tensao n tipicamente entre 3 e 4 para minerais do manto, com olivino frequentemente calibrado em torno de n=3.5) e e independente do tamanho de grao."
    risk: fato
    source: "Karato, S., Deformation of Earth Materials, Cambridge University Press (2008); Hirth, G. & Kohlstedt, D. (2003), em Inside the Subduction Factory, AGU Geophysical Monograph 138, 83-105."
  - claim_id: GEODIN-M23-A06-ARRHENIUS-003
    claim: "Ambos os mecanismos de fluencia seguem uma lei tipo Arrhenius, taxa de deformacao = A * sigma^n * exp(-Q/(R*T)), com Q a energia de ativacao, R a constante dos gases e T a temperatura absoluta; invertendo essa lei, a viscosidade efetiva (definida como tensao dividida por duas vezes a taxa de deformacao) decresce exponencialmente com o aumento da temperatura, proporcional a exp(Q/(R*T))."
    risk: fato
    source: "Turcotte & Schubert, Geodynamics, 3a ed. (2014), Cambridge University Press, cap. 7; Ranalli, G., Rheology of the Earth, 2a ed. (1995), Chapman & Hall."
  - claim_id: GEODIN-M23-A06-REOLOGIA-CROSTA-MANTO-004
    claim: "A reologia ductil da crosta continental e frequentemente aproximada por leis de fluencia calibradas para quartzo (mais fraco, flui em temperaturas relativamente baixas), enquanto o manto superior e governado por leis de fluencia de olivino (mais resistente); essa diferenca, combinada com a geoterma, produz um perfil de resistencia em camadas (strength envelope) da litosfera continental."
    risk: fato
    source: "Ranalli, G. (1995), Rheology of the Earth, 2a ed., Chapman & Hall, capitulo sobre perfis de resistencia litosferica."
  - claim_id: GEODIN-M23-A06-EXEMPLO-ARRHENIUS-005
    claim: "Para Q=540 kJ/mol (calibracao de Karato & Wu 1993 para dislocation creep de olivino seco), R=8.314 J/(mol.K), T1=1000K e T2=1050K, a razao eta_eff(T1)/eta_eff(T2) = exp(Q/(R*T1) - Q/(R*T2)) vale 22.04, ou seja, uma diferenca de 50K produz pouco mais de UMA ordem de grandeza de diferenca na viscosidade efetiva (log10 de 22.04 = 1.34), mantidos os demais parametros constantes."
    risk: calculo
    source: "Calculo aritmetico direto a partir da lei de Arrhenius apresentada na aula, conferido por execucao (numpy 2.5.1: razao = 22.0407); energia de ativacao de Karato, S. & Wu, P. (1993), Science, 260(5109), 771-778, dentro da faixa de 430-560 kJ/mol das calibracoes publicadas, com Hirth & Kohlstedt (2003) em 530 +- 4 kJ/mol."
  - claim_id: GEODIN-M23-A06-PLASTICOFRAGIL-007
    claim: "Ruptura por falhamento e comportamento FRAGIL, nao plastico: deformacao plastica, na mecanica dos materiais, e permanente e continua, sem perda de coesao. Os dois termos aparecem juntos na literatura de modelagem geodinamica porque um meio continuo nao representa fratura discreta, e o regime fragil e modelado por um criterio de escoamento plastico friccional dependente da pressao (Mohr-Coulomb ou Drucker-Prager)."
    risk: fato
    source: "Gerya, T., Introduction to Numerical Geodynamic Modelling, 2a ed. (2019), Cambridge University Press, capitulo sobre reologia viscoelastoplastica; Ranalli, G., Rheology of the Earth, 2a ed. (1995), Chapman & Hall."
-->
