# Aula 05: Calor — lei de Fourier, conservação de calor, produção e advecção

**ID:** geologia-avancado-m23-a05
**Módulo:** [[23-modelagem-numerica-geodinamica-modulo|Módulo 23 — Introdução à modelagem numérica geodinâmica]]
**Duração estimada:** ~23 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** formular a equação de conservação do calor a partir da lei de Fourier, identificar o papel físico de cada um dos seus três termos — difusão, produção e advecção — e trabalhar com a difusividade térmica, a grandeza que governa a rapidez com que uma perturbação térmica se espalha.
**Ao final você vai conseguir:** escrever a lei de Fourier e a equação de conservação de calor; dizer o que cada termo representa fisicamente e reconhecer, num cenário geológico descrito, qual deles domina; calcular a difusividade térmica κ a partir de k, ρ e Cp, e o fluxo de calor condutivo a partir de um gradiente geotérmico; e reduzir a equação à forma de difusão pura, que é o ponto de partida da Aula 06.
**Pré-requisito:** [[23-modelagem-numerica-geodinamica-aula-04-malhas-descricoes-lagrangiana-euleriana|Aula 04 deste módulo]] (malhas e descrições do meio contínuo) e, antes dela, a Aula 02 (diferença central para a segunda derivada).

> [!note] Esta aula é a **Parte 1** de um par.
> Ela constrói a **física** do transporte de calor: de onde vem a equação, o que cada termo significa e que grandezas entram nela. A [[23-modelagem-numerica-geodinamica-aula-06-solucao-numerica-calor-explicito-implicito|Aula 06 — Parte 2]] resolve essa mesma equação **numericamente**, pelos esquemas explícito e implícito, e trata da condição de estabilidade. O par foi dividido porque formular a física e programar o esquema são duas tarefas distintas, e a aula única as empilhava num único bloco de trinta e poucos minutos com quinze conceitos novos. Estude as duas em sequência.

## Conteúdo

### A lei de Fourier

A **lei de Fourier** afirma que o calor flui das regiões mais quentes para as mais frias, a uma taxa proporcional ao gradiente de temperatura:

**q** = −k∇T

onde **q** é o **fluxo de calor** (energia por área por tempo, em W/m²), k é a **condutividade térmica** do material (em W/(m·K) — quanto maior, mais facilmente o calor conduz) e o sinal negativo garante que o fluxo aponta **contra** o gradiente: do quente para o frio, nunca o contrário. Essa única linha é o que transforma uma medida de campo — o gradiente geotérmico lido num poço — num fluxo de energia, e é por isso que ela reaparece em toda a Aula 07.

### A equação de conservação de calor e seus três termos

A lei de Fourier descreve o transporte por condução. Combinando-a com o princípio de conservação de energia — a variação de temperatura num ponto vem do balanço entre o calor que entra, o que sai, o que é produzido internamente e o que é carregado pelo movimento do próprio material — chega-se à **equação de conservação de calor**, na forma unidimensional, na direção vertical z:

ρCp ∂T/∂t = k ∂²T/∂z² + A − ρCp v ∂T/∂z

Do lado esquerdo, ρCp ∂T/∂t é a taxa de **acúmulo** de energia térmica por unidade de volume — ρ a densidade, Cp o calor específico. É o que a equação está tentando prever: como a temperatura naquele ponto muda com o tempo. Do lado direito estão as três maneiras pelas quais ela pode mudar, e vale tomar uma de cada vez:

**Difusão — k ∂²T/∂z².** Calor se espalhando por condução através de rocha **parada**. É proporcional à **curvatura** do perfil de temperatura, não à sua inclinação: a mesma segunda derivada espacial da Aula 02. A leitura física da curvatura é direta — um ponto mais frio que a média dos seus vizinhos recebe calor dos dois lados e esquenta; um ponto mais quente que a média perde para os dois lados e esfria. Um perfil em linha reta, com curvatura nula, não muda de temperatura por difusão, por mais íngreme que seja.

**Produção — A.** Calor gerado internamente, principalmente por decaimento radioativo de urânio, tório e potássio, concentrados sobretudo na crosta. Tem unidade de potência por volume (W/m³). A Aula 07 retoma esse termo em detalhe, porque é ele que governa a geoterma continental estável.

**Advecção — −ρCp v ∂T/∂z.** Calor sendo fisicamente **transportado pelo movimento do material**, a uma velocidade v. É o termo mais fácil de confundir com o primeiro, e a distinção vale guardar: na difusão a rocha está parada e o calor atravessa; na advecção é a **própria rocha** que se move, levando sua temperatura consigo. Uma pluma mantélica ascendente, uma placa subductando, magma subindo por um conduto — todos advectam calor.

### A difusividade térmica κ

É comum agrupar k/(ρCp) numa única grandeza, a **difusividade térmica**:

κ = k/(ρCp)

com unidade de m²/s. Ela mede a rapidez com que uma perturbação térmica se espalha, e é a mesma constante κ que reaparece em qualquer equação de difusão — de calor, de espécies químicas, de momento —, o que é o motivo de todas elas terem a mesma forma matemática, ∂(grandeza)/∂t = κ ∂²(grandeza)/∂z².

> [!warning] Atenção a um falso parentesco de símbolos
> A constante **λ** do decaimento radioativo (Módulo 30 do curso base, aula 05, dN/dt = −λN) **não** é κ, e o decaimento radioativo **não** é um fenômeno de difusão. O decaimento é uma EDO de primeira ordem no tempo, com solução exponencial, sem nenhuma derivada espacial; a difusão é uma EDP de segunda ordem no espaço. É exatamente a distinção que a Aula 02 construiu, e é a primeira vez no módulo em que ela é usada para valer.

Sem advecção e sem produção, a equação de conservação de calor se reduz à forma mais simples possível:

∂T/∂t = κ ∂²T/∂z²

Essa é a **equação da difusão**. Ela é o ponto de partida da Aula 06, que a resolve numericamente, e é também a equação cuja solução analítica — pelo modelo de resfriamento de semi-espaço — governa a litosfera oceânica na Aula 07. Vale reconhecê-la quando reaparecer: é a mesma equação nos dois casos, resolvida por dois caminhos diferentes.

## Exemplo trabalhado

**Situação 1 — calcular a difusividade térmica e o fluxo de calor de uma crosta continental.** Uma rocha crustal tem condutividade térmica k = 2,7 W/(m·K) (um valor representativo; a faixa medida em rochas crustais vai de cerca de 2 a 4), densidade ρ = 2.700 kg/m³ e calor específico Cp = 1.000 J/(kg·K) (o valor padrão em geodinâmica, mas atenção: o calor específico da rocha **cresce com a temperatura** — a crosta média vale cerca de 760 J/(kg·K) à superfície e só passa por 1.000 perto de 220 °C). O gradiente geotérmico medido num poço é de 20 °C/km. Calcule (a) a difusividade térmica κ e (b) o fluxo de calor condutivo em superfície.

```python
k   = 2.7       # condutividade termica, W/(m*K)
rho = 2700.0    # densidade, kg/m3
Cp  = 1000.0    # calor especifico, J/(kg*K)

kappa = k / (rho * Cp)          # m2/s
grad  = 20.0 / 1000.0           # 20 C/km convertido para K/m
q     = k * grad                # lei de Fourier, em modulo, W/m2

print(kappa, q, q * 1000)       # kappa em m2/s; q em W/m2 e em mW/m2
```

**Conferindo à mão, (a):** ρCp = 2.700 × 1.000 = 2,7 × 10⁶ J/(m³·K). Logo κ = 2,7 / (2,7 × 10⁶) = **1,0 × 10⁻⁶ m²/s**. Guarde esse número: é exatamente o κ ≈ 1 × 10⁻⁶ m²/s que a Aula 07 vai usar no modelo de resfriamento da litosfera oceânica, e que a Aula 06 vai usar no critério de estabilidade. Ele não é um valor arbitrário caído do céu — sai de três propriedades medíveis de rocha comum. E é robusto: varrendo k de 2 a 3,8 e Cp de 760 a 1.000, κ fica entre 0,7 e 1,9 × 10⁻⁶ m²/s, o que é a razão de os modelos térmicos de litosfera adotarem κ ≈ 1 × 10⁻⁶ m²/s como constante.

**Conferindo à mão, (b):** o gradiente precisa entrar em unidades SI: 20 °C/km = 20 K / 1.000 m = 0,020 K/m. Pela lei de Fourier, em módulo, q = k × (dT/dz) = 2,7 × 0,020 = **0,054 W/m² = 54 mW/m²**. **Saída esperada do código:** `kappa ≈ 1e-06`, `q ≈ 0.054`, `q*1000 ≈ 54`. O valor cai dentro da faixa típica de fluxo de calor continental estável que a Aula 07 vai discutir (cerca de 40 a 70 mW/m²) — o que é um bom sinal de que os três parâmetros escolhidos são mutuamente consistentes, e não três números avulsos.

**Situação 2 — qual termo domina?** Para cada cenário, diga qual dos três termos do lado direito da equação é o dominante, aplicando as definições da seção anterior.

*(a) Uma soleira de diabásio de 10 m intrudida em folhelho frio, três meses depois da intrusão.* **Difusão.** O magma parou; o que acontece agora é calor atravessando rocha imóvel, do corpo quente para a encaixante fria. Nenhum material está se deslocando, e a escala de tempo é curta demais para que a produção radiogênica some qualquer coisa perceptível.

*(b) Uma crosta continental estável e antiga, com geoterma que não muda há centenas de milhões de anos.* **Produção.** Sem movimento de material, não há advecção; e o perfil já relaxou, de modo que o termo de acúmulo à esquerda é aproximadamente zero. O que sustenta a geoterma nesse estado é o balanço entre a difusão e o calor gerado internamente por U, Th e K — exatamente o regime que a Aula 07 vai formular.

*(c) Uma placa oceânica fria descendo numa zona de subducção a alguns centímetros por ano.* **Advecção.** A placa carrega consigo sua própria temperatura baixa para dentro de um manto quente. É a rocha que se move; o transporte por condução existe, mas é lento demais para reaquecer a placa na escala de tempo em que ela desce — e é justamente por isso que uma placa subductada permanece fria e densa o bastante para puxar a placa atrás dela, como a Aula 09 vai retomar.

## Recap relâmpago

- A **lei de Fourier**, **q** = −k∇T, liga fluxo de calor a gradiente de temperatura, com o sinal negativo garantindo que o calor vai do quente para o frio. É ela que converte um gradiente geotérmico medido em poço num fluxo de energia.
- A **equação de conservação de calor**, ρCp ∂T/∂t = k∂²T/∂z² + A − ρCp v∂T/∂z, tem três termos do lado direito: **difusão** (calor atravessando rocha parada, proporcional à *curvatura* do perfil, não à inclinação), **produção** (A, decaimento de U, Th e K na crosta) e **advecção** (a própria rocha se movendo e levando sua temperatura).
- **Difusão versus advecção** é a distinção que mais se confunde: na primeira a rocha está parada e o calor atravessa; na segunda a rocha se move e carrega o calor.
- A **difusividade térmica** κ = k/(ρCp), em m²/s, mede a rapidez com que uma perturbação térmica se espalha. Para rocha crustal comum ela dá ≈ 1 × 10⁻⁶ m²/s — o valor que reaparece nas Aulas 06 e 07. **κ não é λ**: o decaimento radioativo é EDO no tempo, a difusão é EDP no espaço.
- Sem produção e sem advecção, a equação vira a **equação da difusão**, ∂T/∂t = κ ∂²T/∂z² — resolvida numericamente na Aula 06 e analiticamente (semi-espaço) na Aula 07.

## Próxima aula

[[23-modelagem-numerica-geodinamica-aula-06-solucao-numerica-calor-explicito-implicito|Aula 06 — Solução numérica da equação do calor: esquemas explícito (FTCS) e implícito (BTCS)]] (Parte 2 deste par) — como resolver no computador a equação formulada aqui, e a condição de estabilidade que, violada, faz a solução explodir sem nenhum aviso de natureza física.

## Fontes

- Lei de Fourier e equação de conservação de calor com produção e advecção, definição e valores típicos de difusividade térmica: Turcotte, D. L. & Schubert, G., *Geodynamics*, 3ª ed. (2014), Cambridge University Press, capítulo 4.
- Condutividade térmica, densidade e calor específico de rochas crustais, e a difusividade térmica resultante: Turcotte & Schubert, *Geodynamics*, 3ª ed., capítulo 4 (tabela de propriedades térmicas e problemas resolvidos de geoterma continental).
- Distinção entre transporte condutivo e advectivo de calor em geodinâmica: Gerya, T., *Introduction to Numerical Geodynamic Modelling*, 2ª ed. (2019), Cambridge University Press, capítulo sobre a equação do calor.
- Dependência do calor específico e da condutividade térmica da crosta com a temperatura, densidade crustal de referência (2.700 kg/m³) e a prática de adotar κ ≈ 1 mm²/s constante nos modelos térmicos de litosfera: Whittington, A. G., Hofmeister, A. M. & Nabelek, P. I. (2009), "Temperature-dependent thermal diffusivity of the Earth's crust and implications for magmatism", *Nature*, 458, 319-321, DOI 10.1038/nature07818.

<!--
nivel: avancado
palavras_corpo: 1944
mapa_objetivo_secao:
  geologia-avancado-m23-oa03: "A lei de Fourier" + "A equação de conservação de calor e seus três termos" + "A difusividade térmica κ" + "Exemplo trabalhado"

divisao_de_aula: 'Esta aula e a PARTE 1 da antiga Aula 04 unica (Calor: lei de Fourier, conservacao de calor, producao e adveccao; solucoes numericas explicita e implicita; 2.587 palavras apos as correcoes da auditoria cientifica de 2026-09-19, ~31 min reais contra 30 declarados - JA NO TETO DO PLUGIN ANTES DA AUDITORIA -, 15 conceitos novos todos operacionais), dividida em 2026-09-19 pela revisao didatica (achado DID-M23-A04-CARGA-001). A PARTE 2 e a Aula 06 (esquemas explicito e implicito). CORTE ESCOLHIDO: entre a FORMULACAO FISICA (Fourier, os tres termos, difusividade - esta aula) e a SOLUCAO NUMERICA (malha espaco-tempo, FTCS, estabilidade de von Neumann, BTCS - Parte 2). E o corte mais limpo do modulo: a secao de origem desta aula era a UNICA das quatro que nao fala de discretizacao, e as outras tres nao adicionam nada a fisica. NENHUMA correcao da auditoria cientifica foi desfeita: a correcao do achado VERMELHO 1 (KAPPA-DECAIMENTO-006, o falso parentesco entre kappa e a constante de decaimento) esta INTEGRALMENTE preservada nesta metade e ganhou um callout proprio, ficando mais visivel do que estava; a do achado 3 (MAXIMOPRINCIPIO-007) acompanhou o texto do esquema explicito para a Parte 2, tambem integral.'

exemplo_trabalhado_novo: 'O exemplo trabalhado desta aula foi CRIADO na divisao de 2026-09-19, porque o exemplo original da antiga Aula 04 (pulso de temperatura com r=0.25 e r=1.0) e inteiramente sobre o esquema explicito e ficou, PALAVRA POR PALAVRA e com a correcao do achado 3 da auditoria, na Parte 2. A SITUACAO 1 introduz VALORES NUMERICOS NOVOS (k = 2.7 W/(m.K), rho = 2700 kg/m3, Cp = 1000 J/(kg.K)) e e, portanto, ALEGACAO FACTUAL NOVA - ver nota_ao_auditor. Ela foi construida para ser AUTOCONSISTENTE COM O MODULO: os tres parametros foram escolhidos de modo que kappa = k/(rho*Cp) reproduza exatamente o kappa = 1e-6 m2/s que a Aula 07 ja declara e que a auditoria ja verificou (B24), e que q = k*grad com 20 C/km caia dentro da faixa de 40-70 mW/m2 que a Aula 07 ja declara e que a auditoria ja verificou (B25). Aritmetica conferida por execucao. A SITUACAO 2 NAO CONTEM NENHUMA ALEGACAO FACTUAL NOVA: e a aplicacao classificatoria, sem valor numerico nenhum, das tres definicoes ja auditadas em FOURIER-CONSERVACAO-001 (difusao = calor atravessando rocha parada; producao = decaimento de U, Th, K na crosta; adveccao = a propria rocha se movendo). Os tres cenarios (soleira resfriando, craton estavel, placa subductando) sao rotulos de situacao geologica, nao afirmacoes quantitativas sobre elas.'

nota_ao_auditor: 'RESOLVIDA EM 2026-09-20 pela passagem pontual do auditor-cientifico - ver nota_passagem_pontual abaixo. Registro historico do que estava pendente: UMA ALEGACAO NOVA nasceu nesta divisao e NAO passou pela auditoria cientifica de 2026-09-19, que e anterior a ela: EXEMPLO-PROPRIEDADES-008 (k = 2.7 W/(m.K), rho = 2700 kg/m3, Cp = 1000 J/(kg.K) como valores representativos de rocha crustal, e os dois resultados que deles decorrem, kappa = 1e-6 m2/s e q = 54 mW/m2 para um gradiente de 20 C/km). A aritmetica esta conferida por execucao e os dois RESULTADOS coincidem com valores que a auditoria ja verificou em outras aulas do modulo; o que NAO foi verificado contra fonte e a representatividade dos tres parametros de entrada. Sinalizada para checagem pontual pelo auditor-cientifico, como foi feito nos Modulos 17, 18, 19, 20 e 22.'

alegacoes_auditaveis:
  - claim_id: GEODIN-M23-A04-FOURIER-CONSERVACAO-001
    claim: "A lei de Fourier estabelece que o fluxo de calor por conducao e proporcional ao gradiente negativo de temperatura, q = -k*grad(T); combinada com a conservacao de energia, resulta na equacao de conservacao de calor rho*Cp*dT/dt = k*d2T/dz2 + A - rho*Cp*v*dT/dz, com termos de difusao, producao radiogenica (A) e adveccao pelo movimento do material a velocidade v."
    risk: fato
    source: "Turcotte & Schubert, Geodynamics, 3a ed. (2014), Cambridge University Press, cap. 4."
  - claim_id: GEODIN-M23-A04-KAPPA-DECAIMENTO-006
    claim: "A difusividade termica kappa = k/(rho*Cp), de unidade m2/s, e a constante que aparece em qualquer equacao de difusao e e a razao de todas elas terem a mesma forma matematica. Ela NAO e a constante de decaimento radioativo lambda (Modulo 30 do curso base, aula 05, dN/dt = -lambda*N), e o decaimento radioativo NAO e um fenomeno de difusao: e uma EDO de primeira ordem no tempo, sem derivada espacial, enquanto a difusao e uma EDP de segunda ordem no espaco."
    risk: fato
    source: "Turcotte & Schubert, Geodynamics, 3a ed. (2014), Cambridge University Press, cap. 4 (definicao e unidade da difusividade termica); Modulo 30 do curso base, aula 05 (notacao lambda para a constante de decaimento)."
  - claim_id: GEODIN-M23-A04-EXEMPLO-PROPRIEDADES-008
    claim: "Para k = 2.7 W/(m.K), rho = 2700 kg/m3 e Cp = 1000 J/(kg.K), valores representativos de rocha crustal (a condutividade termica medida em rochas crustais fica tipicamente entre 2 e 4 W/(m.K)), a difusividade termica e kappa = k/(rho*Cp) = 1.0e-6 m2/s; e um gradiente geotermico de 20 C/km = 0.020 K/m produz, pela lei de Fourier, um fluxo condutivo de q = 2.7 * 0.020 = 0.054 W/m2 = 54 mW/m2, dentro da faixa de 40-70 mW/m2 tipica de fluxo de calor continental estavel."
    risk: calculo
    source: "Calculo aritmetico direto conferido por execucao; propriedades termicas de rochas crustais e faixa de fluxo de calor continental: Turcotte & Schubert, Geodynamics, 3a ed. (2014), cap. 4. REPRESENTATIVIDADE DOS TRES PARAMETROS DE ENTRADA AUDITADA E CONFIRMADA na passagem pontual de 2026-09-20: rho = 2700 kg/m3 e exatamente a densidade crustal de referencia adotada por Whittington, Hofmeister & Nabelek (2009, Nature 458, 319-321); k = 2.7 W/(m.K) esta no meio da faixa crustal calculada pelo mesmo trabalho (3.8 a superficie caindo para 1.9 na transicao alfa-beta do quartzo), coerente com a faixa de 2 a 4 declarada na aula; Cp = 1000 J/(kg.K) e o valor padrao em geodinamica e corresponde a crosta media a ~220 C pela equacao (3) do mesmo trabalho, que da 761 J/(kg.K) a 25 C - ressalva acrescentada ao texto, ver CPRESSALVA-009. Os dois RESULTADOS tambem confirmados contra fonte independente: kappa = 1e-6 m2/s e declarado por Whittington et al. como o valor que a maioria dos modelos termicos de litosfera assume; e q = 54 mW/m2 fica dentro da faixa continental (media continental 58 mW/m2, Fowler apud Van der Hilst, MIT OCW 12.201, cap. 5), que da exatamente o mesmo calculo com 20 K/km e k = 3.0 resultando em ~60 mW/m2."
  - claim_id: GEODIN-M23-A04-CPRESSALVA-009
    claim: "O calor especifico da rocha crustal NAO e constante: cresce com a temperatura. Pela equacao de Cp bulk-crustal de Whittington, Hofmeister & Nabelek (2009) - Cp[J/(mol.K)] = 199.50 + 0.0857*T - 5.0e6*T^-2 para T < 846 K, com massa molar media 221.78 g/mol -, a crosta media vale 761 J/(kg.K) a 298 K (25 C) e passa por 1000 J/(kg.K) em ~497 K (~220 C). O valor Cp = 1000 J/(kg.K) usado no exemplo e o padrao em geodinamica, nao a medida de rocha a temperatura ambiente. A difusividade resultante e robusta a essa dispersao: varrendo k de 2 a 3.8 W/(m.K) e Cp de 760 a 1000 J/(kg.K), kappa fica entre 0.7 e 1.9e-6 m2/s, e por isso kappa ~ 1e-6 m2/s e adotado como constante nos modelos termicos de litosfera."
    risk: fato
    source: "Whittington, A. G., Hofmeister, A. M. & Nabelek, P. I. (2009), 'Temperature-dependent thermal diffusivity of the Earth's crust and implications for magmatism', Nature, 458, 319-321, DOI 10.1038/nature07818, equacoes (3) e (4) e texto introdutorio. Equacao avaliada numericamente na passagem pontual de 2026-09-20. ALEGACAO LEVANTADA PELA PASSAGEM PONTUAL do auditor-cientifico (achado laranja P1)."

nota_passagem_pontual: 'PASSAGEM PONTUAL DO AUDITOR-CIENTIFICO em 2026-09-20 sobre a alegacao nova EXEMPLO-PROPRIEDADES-008, que a divisao didatica de 2026-09-19 deixara pendente quanto a REPRESENTATIVIDADE dos tres parametros de entrada. RESULTADO: os tres sao representativos e os dois resultados derivados sao corroborados por fonte independente - registrado como item azul. UM achado laranja: o texto declarava faixa medida so para k e apresentava Cp = 1000 J/(kg.K) sem ressalva, num exemplo ancorado em medida de SUPERFICIE (gradiente em poco, fluxo em superficie), enquanto o Cp bulk-crustal a 25 C e ~761 J/(kg.K). Acrescentada ressalva de uma clausula sobre a dependencia com a temperatura, mais uma frase de robustez de kappa, mais a fonte Whittington et al. (2009) na lista de Fontes. NENHUM VALOR FOI ALTERADO e nenhum resultado mudou: kappa = 1.0e-6 m2/s e q = 54 mW/m2 permanecem. Nenhum dos 15 achados da auditoria de 2026-09-19 foi reaberto.'
-->
