# Aula 05: Aerolevantamentos eletromagnéticos de fonte artificial e natural e estudos de caso integrados

**ID:** geologia-avancado-m16-a05
**Módulo:** [[16-aerogeofisica-modulo|Módulo 16 — Introdução à aerogeofísica]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** distinguir os aerolevantamentos eletromagnéticos de fonte artificial e de fonte natural, explicar por que a frequência do sinal controla a profundidade de investigação, e fechar o módulo mostrando como os quatro métodos aerogeofísicos vistos se integram na prática exploratória.
**Ao final você vai conseguir:** distinguir sistemas EM de domínio de frequência e de domínio de tempo, e sistemas de fonte artificial de sistemas de fonte natural (VLF, AFMAG/campo natural); calcular a profundidade de investigação aproximada (skin depth) de um sinal EM a partir da resistividade do meio e da frequência; e explicar como magnetometria, gravimetria/gradiometria, gamaespectrometria e eletromagnetismo se complementam para reduzir a ambiguidade que cada método sozinho carrega.
**Pré-requisito:** [[16-aerogeofisica-aula-04-aerogamaespectrometria-canais-k-eu-eth-mapas-ternarios|Aula 04]] e, para a segunda metade desta aula (integração), as Aulas 02 e 03 inteiras — a síntese final desta aula reativa os quatro métodos do módulo. Pressupõe também [[15-petrofisica/15-petrofisica-aula-04-condutividade-eletrica-lei-de-archie|Módulo 15, Aula 04]] — condutividade elétrica das rochas como a propriedade física que a eletromagnetometria explora.

## Conteúdo

### O princípio comum: campo primário induz corrente, corrente gera campo secundário

Todo método eletromagnético (EM) aéreo explora o mesmo princípio físico, independentemente da fonte do sinal: um **campo magnético primário**, variável no tempo, atravessa o subsolo e, onde encontra um material condutor, induz nele **correntes parasitas** (correntes de Foucault/eddy currents); essas correntes, por sua vez, geram um **campo magnético secundário**, que se soma ao primário e é o que o receptor a bordo da aeronave efetivamente detecta e separa do primário. A intensidade e a forma desse campo secundário dependem diretamente da condutividade elétrica do material no subsolo — a mesma propriedade física estudada pela lei de Archie no Módulo 15, agora explorada não por corrente elétrica injetada por eletrodos (como em métodos terrestres de resistividade), mas por indução eletromagnética a distância, sem contato físico com o solo. É essa ausência de contato que torna o método viável a partir do ar.

A diferença entre os sistemas está em **de onde vem o campo primário**: sistemas de **fonte artificial** (ou fonte controlada) geram o próprio campo primário a bordo, com um transmissor cuja forma de onda e frequência são conhecidas e controladas; sistemas de **fonte natural** (ou passivos) usam campos eletromagnéticos que já existem no ambiente, gerados por fenômenos externos, e medem apenas a resposta do subsolo a esses campos preexistentes.

### Sistemas de fonte artificial: domínio de frequência e domínio de tempo

**Domínio de frequência (FDEM, frequency-domain electromagnetics).** O transmissor emite continuamente em uma ou mais frequências fixas simultaneamente (tipicamente de algumas centenas de hertz a mais de 100 kHz — sistemas helitransportados modernos operam rotineiramente numa faixa da ordem de 400 Hz a 130 kHz), e o receptor mede a amplitude e a fase (ou, de forma equivalente, as componentes em fase e em quadratura) do campo secundário em cada frequência. Frequências mais altas respondem preferencialmente a condutores rasos e de resposta rápida; frequências mais baixas penetram mais fundo, mas com resolução espacial mais grosseira — de modo que um sistema multifrequência entrega, num único voo, informação sobre condutividade em várias profundidades aproximadas simultaneamente. Fisicamente, o transmissor e o receptor costumam ser bobinas montadas numa configuração fixa e conhecida (frequentemente rebocadas num "bird" atrás da aeronave, ou, em alguns sistemas, montadas rigidamente numa asa ou lança), e essa geometria fixa é o que permite calibrar a resposta em termos de condutividade aparente do subsolo.

**Domínio de tempo (TDEM, time-domain electromagnetics).** Em vez de transmitir continuamente, o sistema emite um **pulso** de corrente no transmissor e o desliga abruptamente; durante o intervalo em que o transmissor está desligado, as correntes parasitas induzidas no subsolo continuam decaindo por alguns milissegundos, e é justamente esse **decaimento**, medido pelo receptor no intervalo entre pulsos, que carrega a informação sobre a condutividade e a profundidade do corpo condutor — corpos mais condutores e maiores decaem mais devagar, permitindo que o sinal seja medido em janelas de tempo sucessivas após o desligamento do pulso, cada uma correspondendo aproximadamente a uma profundidade de investigação diferente (janelas mais tardias correspondem a maior profundidade). A frequência de base do ciclo liga-desliga é escolhida em função da frequência da rede elétrica local — tipicamente **25 Hz onde a rede é de 50 Hz e 30 Hz onde é de 60 Hz** —, de modo que o empilhamento de muitos ciclos com polaridade alternada cancele a interferência das linhas de transmissão de energia em vez de acumulá-la. O TDEM se tornou, nas últimas décadas, o sistema dominante em exploração mineral aérea, em parte por discriminar melhor a resposta de corpos condutores de pequena dimensão em meio a uma cobertura condutora (como solo ou saprolito úmido) do que o FDEM, cuja resposta contínua mistura mais facilmente as duas contribuições.

### Sistemas de fonte natural: VLF e o campo eletromagnético natural (AFMAG)

**VLF (Very Low Frequency).** Aproveita, como fonte primária, as transmissões de rádio de muito baixa frequência (tipicamente na faixa de 15 a 30 kHz) operadas para comunicação militar e de navegação em várias partes do mundo — sinais potentes o suficiente para se propagar por milhares de quilômetros e, por isso, detectáveis como campo primário praticamente em qualquer lugar do planeta onde o transmissor esteja favoravelmente orientado em relação à estrutura geológica de interesse. O receptor aéreo mede a distorção desse campo distante causada por condutores rasos no subsolo (fraturas preenchidas por água, veios sulfetados, zonas de cisalhamento condutoras) — a frequência relativamente alta do VLF limita a profundidade de investigação a valores rasos, o que faz do método uma ferramenta de detalhe estrutural raso, não de investigação profunda.

**AFMAG / EM de campo natural (natural-field EM, NFEM).** Explora campos eletromagnéticos naturais de frequência muito mais baixa que o VLF (tipicamente na faixa de dezenas a algumas centenas de hertz), originados principalmente pela atividade de relâmpagos ao redor do globo: cada descarga emite um pulso eletromagnético de banda larga (os *sferics*) que se propaga a distâncias continentais **dentro do guia de onda formado entre a superfície da Terra e a base da ionosfera**, refletindo-se entre as duas — não *através* da ionosfera —, o que mantém um campo eletromagnético natural de baixa frequência disponível em qualquer ponto do planeta, a qualquer hora. Por operar em frequência muito mais baixa que o VLF e que a maioria dos sistemas FDEM/TDEM ativos, o AFMAG/NFEM investiga profundidades substancialmente maiores — sistemas aéreos modernos baseados nesse princípio (como os que medem a razão tipper do campo natural) são usados especificamente quando o alvo de interesse está profundo demais para ser alcançado por sistemas de fonte artificial convencionais, ao custo de um sinal mais fraco e mais sujeito a ruído atmosférico variável, o que geralmente exige tempos de integração maiores e processamento mais cuidadoso do que os sistemas de fonte controlada.

### Profundidade de investigação: por que frequência baixa penetra mais fundo

A razão física por trás da regra "frequência baixa penetra mais fundo", usada acima tanto para comparar VLF com AFMAG quanto para comparar janelas de tempo dentro de um mesmo sistema TDEM, tem uma expressão quantitativa: a **profundidade pelicular** (skin depth), a distância na qual a amplitude de uma onda eletromagnética que se propaga num meio condutor cai a cerca de 37% (1/e) do seu valor na superfície. Em unidades práticas de geofísica de exploração, a profundidade pelicular aproximada é dada por:

δ (em metros) ≈ 503 × √(ρ / f)

onde ρ é a resistividade do meio em ohm-metro e f é a frequência em hertz. A relação mostra, de forma explícita, por que a profundidade de investigação cresce com a resistividade do meio (meios mais resistivos deixam o campo penetrar mais fundo antes de ser atenuado) e diminui com a frequência (frequências mais altas são atenuadas mais rapidamente) — e é exatamente essa segunda dependência que explica por que o AFMAG/campo natural, operando em dezenas de hertz, investiga profundidades muito maiores do que o VLF, operando em dezenas de quilohertz, no mesmo terreno.

## Exemplo trabalhado

**Situação:** um levantamento aéreo sobre uma área de rocha granítica relativamente resistiva (resistividade estimada de 1.000 ohm-m) precisa decidir entre um sistema VLF, operando a 20 kHz, e um sistema aéreo de campo natural (AFMAG/NFEM), operando a 30 Hz, para investigar uma estrutura condutora suspeita a cerca de 250 m de profundidade.

**Pergunta:** calcule a profundidade pelicular aproximada de cada sistema nesse terreno e determine qual é capaz de "enxergar" a estrutura a 250 m.

**Resolução:**

**Sistema VLF (f = 20.000 Hz):**

δ = 503 × √(1.000 / 20.000) = 503 × √0,05 = 503 × 0,2236 ≈ **112 m**

**Sistema AFMAG/NFEM (f = 30 Hz):**

δ = 503 × √(1.000 / 30) = 503 × √33,33 = 503 × 5,77 ≈ **2.902 m**

**Interpretação:** a profundidade pelicular do VLF nesse terreno resistivo (≈112 m) é bem menor que a profundidade da estrutura de interesse (250 m) — o sinal já estaria fortemente atenuado antes mesmo de alcançar o alvo, tornando o VLF inadequado para essa investigação específica, embora seja uma ferramenta excelente para mapear condutores muito mais rasos (fraturas, veios, contatos) na mesma área. A profundidade pelicular do AFMAG/NFEM (≈2.900 m) está bem acima da profundidade do alvo, o que significa que o sinal de 30 Hz ainda carrega energia suficiente na profundidade de 250 m para responder à presença do condutor, tornando esse sistema a escolha adequada para o objetivo declarado.

**Ressalva pedagógica:** a profundidade pelicular é uma medida de atenuação do campo primário, não uma "profundidade máxima de detecção" no sentido estrito — na prática, a detectabilidade real de um corpo específico também depende do seu tamanho, de seu contraste de condutividade com a rocha encaixante e do nível de ruído do sistema, e a interpretação quantitativa completa de um levantamento EM real usa modelagem numérica, não apenas a fórmula da profundidade pelicular. Ainda assim, a comparação acima captura corretamente a razão física de fundo pela qual sistemas de fonte natural de baixa frequência são a escolha típica para alvos profundos que sistemas ativos de alta frequência simplesmente não alcançam.

## Fechando o módulo: por que nenhum método sozinho basta

Cada um dos quatro métodos vistos neste módulo explora uma propriedade física diferente — magnetismo (Aula 02), densidade (Aula 03), radioatividade natural (Aula 04) e condutividade elétrica (esta aula) —, e cada um carrega sua própria ambiguidade quando usado isoladamente: uma anomalia magnética pode vir de magnetita disseminada sem valor econômico algum; uma anomalia gravimétrica pode vir de uma variação de espessura sedimentar sem relação com mineralização; uma anomalia radiométrica reflete apenas a composição dos primeiros centímetros de solo, podendo estar mascarada por cobertura; e um condutor eletromagnético pode ser um corpo sulfetado de interesse econômico ou, com a mesma facilidade, água salina em fratura, grafita em xisto, ou solo argiloso saturado — três "falsos positivos" clássicos que produzem resposta condutora forte sem qualquer relação com minério.

É exatamente por isso que a exploração mineral moderna raramente decide com base num único método aerogeofísico: um alvo eletromagnético condutor que **coincide** espacialmente com uma anomalia magnética moderada (sugerindo sulfetos com alguma **pirrotita monoclínica**, a fase ferrimagnética vista no Módulo 15 — e não apenas pirita ou grafita, ambas não magnéticas, nem a pirrotita hexagonal, que é antiferromagnética à temperatura ambiente), com uma leve anomalia gravimétrica positiva (sugerindo maior densidade que a rocha encaixante) e com um halo de alteração potássica visível no mapa ternário gamaespectrométrico circundante, é uma hipótese de exploração muito mais robusta do que qualquer uma dessas quatro evidências isoladamente — cada método elimina algumas das explicações alternativas que os outros três não conseguem descartar sozinhos. Essa é a mesma lógica de integração multimétodo com que o Módulo 15 fechou o estudo da petrofísica, e é o motivo pelo qual aquele módulo é pré-requisito deste: a aerogeofísica não é quatro instrumentos independentes que por acaso voam na mesma aeronave — é a aplicação, em escala regional e à distância, do mesmo princípio de que nenhuma propriedade física isolada resolve sozinha a ambiguidade geológica que a interpretação integrada existe para reduzir.

## Erros comuns

- **Tratar profundidade pelicular como "profundidade máxima de detecção".** A própria ressalva pedagógica da aula avisa: é uma medida de atenuação do campo primário; detectabilidade real também depende do tamanho do corpo, do contraste de condutividade e do ruído do sistema — a interpretação quantitativa completa exige modelagem numérica.
- **Escolher VLF para um alvo profundo por ser o sistema "mais simples ou mais barato".** Como o exemplo trabalhado calcula, a 20 kHz a profundidade pelicular em rocha resistiva já fica bem abaixo do alvo — o sinal se atenua antes de alcançá-lo, tornando o método fisicamente inadequado, não apenas subótimo.
- **Interpretar qualquer condutor eletromagnético como sulfeto econômico.** Água salina em fratura, grafita em xisto e solo argiloso saturado produzem resposta condutora igualmente forte — são os três falsos positivos clássicos que a aula nomeia explicitamente.
- **Usar a frequência de base errada num sistema TDEM** (25 Hz numa rede de 60 Hz, ou vice-versa). A escolha é casada à frequência da rede elétrica local especificamente para cancelar essa interferência por empilhamento com polaridade alternada — usar a frequência errada reintroduz o ruído que o método existe para cancelar.

## O que não concluir

- **Que pirrotita presente implica automaticamente resposta magnética.** Só a pirrotita monoclínica é ferrimagnética; a pirrotita hexagonal é antiferromagnética à temperatura ambiente — a mesma fórmula química não garante o mesmo comportamento magnético, distinção que a aula liga diretamente ao Módulo 15.
- **Que um método aerogeofísico isolado pode confirmar um alvo de exploração por si só.** A aula fecha o módulo inteiro com esse ponto: cada método carrega sua própria ambiguidade, e é a coincidência espacial de evidências de métodos diferentes que transforma uma anomalia isolada em hipótese robusta.
- **Que TDEM é sempre superior a FDEM em qualquer cenário.** TDEM discrimina melhor corpos condutores pequenos em meio a cobertura condutora — uma vantagem específica, não superioridade universal; um sistema multifrequência FDEM ainda entrega informação simultânea em várias profundidades aproximadas num único voo.

## Recap relâmpago

- Todo método EM explora o mesmo princípio: um campo primário variável no tempo induz correntes parasitas em material condutor no subsolo, que geram um campo secundário detectado pelo receptor — a diferença entre sistemas está em se o campo primário é gerado a bordo (fonte artificial) ou já existe no ambiente (fonte natural).
- FDEM (domínio de frequência) transmite continuamente em frequências fixas (de centenas de Hz a mais de 100 kHz em sistemas helitransportados) e mede amplitude/fase; TDEM (domínio de tempo) emite pulsos, com frequência de base casada à rede elétrica local (25 Hz onde a rede é 50 Hz, 30 Hz onde é 60 Hz), e mede o decaimento do campo secundário no intervalo desligado, com janelas de tempo sucessivas correspondendo a profundidades crescentes — hoje o sistema dominante em exploração mineral aérea.
- VLF usa transmissões de rádio de 15-30 kHz como fonte, útil para mapear condutores rasos (fraturas, veios) a baixo custo de profundidade de investigação; AFMAG/campo natural usa energia eletromagnética natural de dezenas a poucas centenas de Hz (originada sobretudo por relâmpagos globais, cujos pulsos se propagam no guia de onda entre a superfície e a base da ionosfera), investigando profundidades muito maiores, ao custo de sinal mais fraco.
- A profundidade pelicular (skin depth), δ ≈ 503√(ρ/f), cresce com a resistividade do meio e diminui com a frequência — a base física de por que sistemas de baixa frequência (AFMAG) penetram muito mais fundo que sistemas de alta frequência (VLF) no mesmo terreno; é uma medida de atenuação, não uma profundidade máxima de detecção no sentido estrito.
- Condutores eletromagnéticos têm ambiguidade clássica (sulfeto econômico vs. água salina, grafita ou argila saturada) — a mesma lógica de ambiguidade que afeta isoladamente magnetismo, gravidade e radiometria vistos nas aulas anteriores.
- Nenhum dos quatro métodos aerogeofísicos do módulo resolve sozinho a ambiguidade geológica; a coincidência espacial de evidências de métodos diferentes (ex.: condutor EM + anomalia magnética moderada + leve excesso gravimétrico + halo potássico radiométrico) é o que transforma uma anomalia isolada numa hipótese de exploração robusta — a mesma lógica de integração multimétodo que fechou o Módulo 15 de petrofísica, do qual este módulo depende.

## Próxima aula

Este é o fim do Módulo 16. O [[17-geofisica-marinha-bacias-sedimentares/17-geofisica-marinha-bacias-sedimentares-modulo|Módulo 17 — Geofísica marinha e de bacias sedimentares]] mantém a lógica de campos potenciais e de aquisição em plataforma móvel construída aqui, mas troca o ar pela água e o alvo exploratório pontual pela arquitetura de uma bacia inteira — e é lá que a sísmica, apenas mencionada até agora como a grande ausente da aerogeofísica, entra como método principal.

## Fontes

- Telford, W. M., Geldart, L. P. & Sheriff, R. E. (1990), *Applied Geophysics*, 2ª ed., Cambridge University Press, cap. 6 (princípio de indução eletromagnética, fórmula de profundidade pelicular, VLF).
- Nabighian, M. N. & Macnae, J. C. (1991), "Time domain electromagnetic prospecting methods", em *Electromagnetic Methods in Applied Geophysics*, vol. 2, SEG (fundamentos de TDEM, janelas de tempo, profundidade de investigação).
- CSEG Recorder, "Airborne Electromagnetic Systems – State of the Art and Future Directions" (comparação de sistemas FDEM e TDEM, frequências e configurações típicas de transmissor/receptor).
- MDPI Minerals 14(7):704, "Airborne Natural Total Field Broadband Electromagnetics — Configurations, Capabilities, and Advantages" (2024) (faixas de frequência de sistemas AFMAG/campo natural, origem em atividade de relâmpagos, aplicação a alvos profundos).
- Referências gerais de VLF aéreo (faixa de frequência de transmissores VLF de 15-30 kHz usados como fonte primária em prospecção).

<!--
nivel: avancado
palavras_corpo: 2247
mapa_objetivo_secao:
  geologia-avancado-m16-oa04: "O princípio comum: campo primário induz corrente, corrente gera campo secundário" + "Sistemas de fonte artificial: domínio de frequência e domínio de tempo" + "Sistemas de fonte natural: VLF e o campo eletromagnético natural (AFMAG)" + "Profundidade de investigação: por que frequência baixa penetra mais fundo" + "Exemplo trabalhado" + "Fechando o módulo: por que nenhum método sozinho basta"

alegacoes_auditaveis:
  - claim_id: AEROGEOFIS-M16-A05-PRINCIPIO-001
    claim: "Métodos eletromagnéticos aéreos exploram indução: um campo primário variável no tempo induz correntes parasitas (eddy currents) em material condutor no subsolo, que geram um campo secundário detectado pelo receptor; a intensidade e forma do campo secundário dependem da condutividade elétrica do subsolo, a mesma propriedade explorada pela lei de Archie em métodos de resistividade por contato, mas aqui medida sem contato físico com o solo."
    risk: fato
    source: "Telford, Geldart & Sheriff 1990, Applied Geophysics, cap. 6, fundamentos de indução eletromagnética em prospecção."
  - claim_id: AEROGEOFIS-M16-A05-FDEMTDEM-002
    claim: "Sistemas FDEM transmitem continuamente em frequências fixas (de algumas centenas de Hz a mais de 100 kHz; sistemas helitransportados modernos operam numa faixa da ordem de 400 Hz a 130 kHz) e medem amplitude/fase (ou componentes em fase e quadratura) do campo secundário; sistemas TDEM emitem pulsos e medem o decaimento do campo secundário durante o intervalo desligado, com janelas de tempo sucessivas correspondendo a profundidades de investigação crescentes; a frequência de base do transmissor é casada à frequência da rede elétrica local — tipicamente 25 Hz onde a rede é de 50 Hz e 30 Hz onde é de 60 Hz — para que o empilhamento com polaridade alternada cancele a interferência de linhas de transmissão. TDEM tornou-se o sistema dominante em exploração mineral aérea nas últimas décadas."
    risk: aproximacao
    source: "Nabighian & Macnae 1991, Time domain electromagnetic prospecting methods, Electromagnetic Methods in Applied Geophysics vol. 2, SEG; CSEG Recorder, Airborne Electromagnetic Systems – State of the Art and Future Directions; especificações de sistemas comerciais (VTEM, TEMPEST: frequências de base de 25/30 Hz; RESOLVE/DIGHEM: frequências FDEM até ~130 kHz). CORREÇÃO AMARELA da auditoria de 2026-09-09: a redação original limitava o FDEM a 'dezenas de kHz' (subestimando a faixa alta dos sistemas helitransportados) e descrevia a sincronização do TDEM como 'múltiplo ímpar de metade da frequência da rede', formulação que não corresponde às frequências de base efetivamente usadas."
  - claim_id: AEROGEOFIS-M16-A05-VLF-003
    claim: "Sistemas VLF aéreos usam como fonte primária transmissões de rádio de muito baixa frequência (tipicamente 15-30 kHz), operadas para comunicação militar/navegação e detectáveis a longa distância; o método é usado para mapear condutores rasos (fraturas preenchidas por água, veios sulfetados, zonas de cisalhamento condutoras), com profundidade de investigação limitada pela frequência relativamente alta."
    risk: fato
    source: "CSEG Recorder, Airborne Electromagnetic Systems; Telford, Geldart & Sheriff 1990, cap. 6 (VLF total field magnitudes usually in the 15-30 kHz range)."
  - claim_id: AEROGEOFIS-M16-A05-AFMAG-004
    claim: "AFMAG / EM de campo natural (natural-field EM) explora campos eletromagnéticos naturais de frequência muito mais baixa que o VLF (tipicamente dezenas a algumas centenas de Hz), originados principalmente por atividade de relâmpagos ao redor do globo: cada descarga emite um pulso de banda larga (sferic) que se propaga a distâncias continentais DENTRO do guia de onda entre a superfície da Terra e a base da ionosfera, refletindo-se entre as duas (não atravessando a ionosfera). Por operar em frequência muito mais baixa, investiga profundidades substancialmente maiores que VLF ou sistemas FDEM/TDEM ativos convencionais, ao custo de sinal mais fraco e mais sujeito a ruído atmosférico variável."
    risk: aproximacao
    source: "MDPI Minerals 14(7):704 (2024), Airborne Natural Total Field Broadband Electromagnetics — Configurations, Capabilities, and Advantages; pesquisa web confirmando faixa de AFMAG de aproximadamente 25-1000 Hz (mais especificamente 25-600 Hz em uso corrente) e origem em atividade global de relâmpagos como fonte de energia eletromagnética natural de baixa frequência."
  - claim_id: AEROGEOFIS-M16-A05-SKINDEPTH-005
    claim: "A profundidade pelicular (skin depth) de uma onda eletromagnética num meio condutor é aproximada, em unidades práticas de geofísica de exploração, por delta (m) = 503 x raiz(rho/f), com rho a resistividade em ohm-m e f a frequência em Hz; a profundidade pelicular cresce com a resistividade do meio e diminui com a frequência."
    risk: fato
    source: "Telford, Geldart & Sheriff 1990, Applied Geophysics, cap. 6 (fórmula padrão de skin depth em unidades práticas, constante 503, usada correntemente em geofísica de exploração eletromagnética)."
  - claim_id: AEROGEOFIS-M16-A05-AMBIGUIDADE-006
    claim: "Condutores eletromagnéticos identificados em levantamento aéreo têm ambiguidade de fonte clássica: sulfetos maciços de interesse econômico produzem resposta condutora, mas água salina em fratura, grafita em xisto e argila/solo saturado também produzem resposta condutora forte sem relação com mineralização — por isso a interpretação de um alvo EM costuma exigir integração com outros métodos (magnetometria, gravimetria, gamaespectrometria) para reduzir a ambiguidade."
    risk: fato
    source: "Nabighian & Macnae 1991, Time domain electromagnetic prospecting methods, SEG (discussão de falsos condutores/false conductors em EM: grafita, água salina, argila); CSEG Recorder, Airborne Electromagnetic Systems (uso integrado de EM com outros métodos na exploração mineral)."
-->
