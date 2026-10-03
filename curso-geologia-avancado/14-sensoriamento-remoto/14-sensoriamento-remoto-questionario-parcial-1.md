# Questionário parcial 1 — Módulo 14: Sensoriamento remoto

**Módulo:** [[14-sensoriamento-remoto-modulo|Módulo 14 — Sensoriamento remoto]]
**Cobertura:** Aulas 01 a 03 — conceitos, plataformas, sensores e as quatro resoluções (Aula 01); fundamentos físicos da radiação eletromagnética e da atmosfera (Aula 02); comportamento espectral de água, solos, minerais, rochas e vegetação, e geobotânica (Aula 03).
**Recorte:** o vocabulário e a física que sustentam qualquer imagem de sensoriamento remoto, antes de qualquer processamento — que sensor escolher e como ele "vê" (oa02, ensinado inteiramente pela Aula 01) e por que a radiação se comporta como se comporta ao interagir com a atmosfera e com os alvos naturais (oa01, ensinado pelas Aulas 02 e 03).
**Objetivos avaliados:** `geologia-avancado-m14-oa02` (integral — a01) · `geologia-avancado-m14-oa01` (integral — a02 + a03)
**Atenção de cobertura:** o oa02 é ensinado por uma única aula (a01) — cinco das dez questões abaixo são dedicadas a ele, para não sub-avaliar esse objetivo apesar de ele ocupar só um terço das aulas deste bloco.
**Pontuação total:** 100 pontos · o gabarito fica oculto; responda antes de abrir.

---

### 1. Múltipla escolha — `geologia-avancado-m14-q01` · oa02 · 10 pts

Uma equipe de geologia estrutural precisa de imagens de uma área da Amazônia com cobertura de nuvens persistente, e quer poder adquirir dado tanto de dia quanto de noite. Qual tipo de sensor atende a essa necessidade, e por quê?

- a) Sensor passivo óptico multiespectral, porque capta luz solar refletida com alta resolução espectral
- b) Sensor passivo termal, porque capta emissão própria do alvo e, por isso, atravessa nuvens
- c) Sensor ativo de micro-ondas (radar/SAR), porque emite sua própria energia e as micro-ondas atravessam nuvens, operando independentemente de luz solar
- d) Sensor ativo de laser (LiDAR) orbital de alta revisita, porque o laser também atravessa nuvens espessas, do mesmo modo que as micro-ondas

<details>
<summary>Ver resposta</summary>

**Resposta: c**

O radar (SAR) é um sensor **ativo de micro-ondas**: emite sua própria energia e mede o retorno, o que o torna independente de luz solar (opera de dia ou de noite) e capaz de atravessar nuvens, ao contrário de sensores ópticos passivos, que dependem de luz refletida e são bloqueados por nuvens espessas. "b" erra porque o termal, embora não dependa de luz solar (capta emissão própria), ainda é bloqueado por nuvens — a radiação termal é absorvida e espalhada por gotículas de água, do mesmo modo que o óptico. "d" erra ao estender ao laser (LiDAR) a mesma capacidade de penetração de nuvens do radar de micro-ondas — o laser, de comprimento de onda muito menor, é fortemente espalhado por nuvens espessas, não as atravessa como as micro-ondas.
</details>

---

### 2. Verdadeiro ou Falso (justifique) — `geologia-avancado-m14-q02` · oa02 · 10 pts

"O Landsat 8/9 opera em órbita geoestacionária, permanecendo sempre sobre o mesmo ponto da superfície, o que garante cobertura contínua da região amazônica."

<details>
<summary>Ver resposta</summary>

**Falso.**

O Landsat 8/9 opera em órbita **heliossíncrona**, de baixa altitude (~705 km), quase polar — não geoestacionária. Uma órbita geoestacionária fica a ~36.000 km sobre o Equador, com velocidade orbital igual à rotação da Terra, e é usada por satélites meteorológicos, não por sensores de recursos naturais como o Landsat: ela garante cobertura contínua da mesma área, mas com resolução espacial muito mais grosseira, incompatível com mapeamento geológico de detalhe. A característica da órbita heliossíncrona não é "ficar parada" sobre um ponto, e sim cruzar cada ponto da superfície sempre aproximadamente no mesmo horário solar local, mantendo iluminação comparável entre passagens sucessivas — a Amazônia é revisitada periodicamente (a cada ~8 dias, com a constelação Landsat 8+9 combinada), não continuamente.
</details>

---

### 3. Aplicação (cálculo) — `geologia-avancado-m14-q03` · oa02 · 10 pts

Uma feição de alteração hidrotermal tem 90 m de extensão no menor eixo. Usando a regra empírica de que um alvo precisa se estender por ao menos 3-5 pixels contíguos para ser reconhecível com alguma confiança numa imagem, essa feição é mapeável com a resolução espacial do Landsat (30 m)? E com a do Sentinel-2 nas bandas principais (10 m)? Mostre o cálculo de pixels para cada caso.

<details>
<summary>Ver resolução</summary>

**Landsat (30 m):** 90 m ÷ 30 m = **3 pixels** no menor eixo — no limite inferior da regra empírica de 3-5 pixels, portanto mapeável, mas de forma marginal: só reconhecível com alguma confiança se o contraste espectral entre a zona alterada e a encaixante for forte, do mesmo modo que o exemplo trabalhado da Aula 01 tratou um alvo de 200 m (6-7 pixels) como mapeável e um de 60 m (2 pixels) como inviável.

**Sentinel-2 (10 m):** 90 m ÷ 10 m = **9 pixels** no menor eixo — confortavelmente acima do limiar de 3-5 pixels, portanto mapeável com boa confiança, sem depender de um contraste espectral excepcionalmente forte.

O resultado ilustra o compromisso central da Aula 01: a mesma feição física passa de "mapeável no limite" para "mapeável com folga" só pela troca de sensor, sem que nada tenha mudado no terreno — e a decisão de qual sensor usar depende do tamanho esperado do alvo antes mesmo de qualquer processamento.
</details>

---

### 4. Múltipla escolha — `geologia-avancado-m14-q04` · oa02 · 10 pts

Sobre a constelação Sentinel-2, qual afirmação está correta?

- a) O par nominal em operação é 2A+2B, como desde o lançamento da missão
- b) O par nominal é 2B+2C desde 21/01/2025, e o 2A segue desde março de 2025 numa campanha de extensão que adensa a revisita sobre a Europa, a África tropical e a América do Sul
- c) O Sentinel-2 passou a operar com um único satélite a partir de 2025, reduzindo a revisita
- d) A revisita combinada mudou de 5 para 10 dias depois da substituição do 2A pelo 2C

<details>
<summary>Ver resposta</summary>

**Resposta: b**

O que é estável no Sentinel-2 é o **arranjo** — dois satélites em serviço simultâneo, defasados 180°, revisita combinada de ~5 dias — mas a **identidade** de quem ocupa essas duas posições muda: o Sentinel-2C substituiu o Sentinel-2A na operação nominal em 21/01/2025 (par atual 2B+2C), e o 2A passou, desde março de 2025, a uma campanha de extensão, defasado 36° do 2B, que adensa especificamente a revisita sobre regiões de cobertura de nuvens frequente — Europa, África tropical e América do Sul. "a" trata a identidade como fixa, quando só o arranjo é estável; "c" e "d" inventam mudanças que não ocorreram — a revisita nominal de 5 dias não mudou, e o Sentinel-2 continua operando com dois satélites simultâneos (mais o 2A em extensão, não menos satélites).
</details>

---

### 5. Dissertativa curta — `geologia-avancado-m14-q05` · oa02 · 10 pts

Explique por que não existe "o sensor ideal" que maximize simultaneamente as quatro resoluções (espacial, espectral, temporal, radiométrica), usando o compromisso que a Aula 01 descreve entre resolução espacial fina e resolução temporal.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:**

As quatro resoluções competem por um **orçamento fixo** de dado e de energia do sensor — melhorar uma quase sempre custa nas outras três. O compromisso mais direto é entre resolução espacial e temporal: um sensor de resolução espacial muito fina precisa de uma óptica maior e capta mais dado por cena, o que tende a reduzir sua faixa de imageamento (*swath*) — e uma faixa de imageamento menor cobre menos área a cada passagem, o que **piora** a resolução temporal (revisita menos área por órbita, exigindo mais órbitas, e portanto mais tempo, para cobrir a mesma região novamente). Um sensor de resolução espacial fina também tende a ter menos bandas (resolução espectral mais pobre), pela mesma pressão de orçamento de dado. Escolher um sensor para um projeto geológico é, portanto, decidir qual dessas quatro trocar por qual, de acordo com o que o problema exige — um projeto de monitoramento de deformação rápida prioriza resolução temporal; um projeto de mapeamento composicional de detalhe prioriza resolução espacial e espectral — e não existe um sensor que maximize as quatro ao mesmo tempo.
</details>

---

### 6. Múltipla escolha — `geologia-avancado-m14-q06` · oa01 · 10 pts

Um fóton de ultravioleta próximo (λ ≈ 0,25 µm) e um fóton de infravermelho de ondas curtas (λ ≈ 2,2 µm) chegam ao mesmo detector. Qual dos dois carrega mais energia por fóton, e por quê?

- a) O de SWIR, porque comprimento de onda maior implica maior frequência
- b) O de UV, porque comprimento de onda menor implica maior frequência (c = λν) e, por E = hν, maior energia por fóton
- c) Os dois têm exatamente a mesma energia, porque E depende apenas da intensidade do feixe, não do comprimento de onda
- d) O de SWIR, porque está mais próximo da faixa usada pelos sensores geológicos e por isso é mais "forte"

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Comprimento de onda (λ) e frequência (ν) são inversamente relacionados por c = λν — quanto menor o λ, maior o ν. E a energia de cada fóton é E = hν: maior frequência significa maior energia por fóton. Como 0,25 µm é um comprimento de onda muito menor que 2,2 µm, o fóton de UV tem frequência muito mais alta e, portanto, carrega mais energia por fóton — é exatamente essa relação que explica, na Aula 06, por que sensoriamento remoto em micro-ondas (comprimento de onda muito maior, energia por fóton muito menor) precisa ser feito por sensores ativos: a emissão natural nessa faixa é fraca demais para um sensor passivo captar. "a" inverte a relação entre λ e ν; "c" e "d" confundem energia por fóton com intensidade do feixe ou com "importância" prática, que não são a mesma grandeza física.
</details>

---

### 7. Verdadeiro ou Falso (justifique) — `geologia-avancado-m14-q07` · oa01 · 10 pts

"O espalhamento de Rayleigh afeta igualmente todas as bandas do visível, já que depende apenas da presença de moléculas de ar na atmosfera, não do comprimento de onda da radiação."

<details>
<summary>Ver resposta</summary>

**Falso.**

O espalhamento de Rayleigh é **inversamente proporcional à quarta potência do comprimento de onda** (λ⁻⁴) — está longe de afetar igualmente todas as bandas. Comprimentos de onda curtos (azul) são espalhados muito mais intensamente do que comprimentos de onda longos (vermelho, infravermelho): é exatamente essa dependência espectral forte que explica por que o céu é azul e por que a banda azul de qualquer sensor óptico chega ao solo mais degradada por espalhamento atmosférico do que as demais bandas, exigindo correção mais agressiva no pré-processamento. Tratar o espalhamento de Rayleigh como uniforme entre bandas apaga justamente o mecanismo físico que explica esse fenômeno tão citado (o céu azul) e a maior vulnerabilidade prática da banda azul em qualquer produto óptico.
</details>

---

### 8. Aplicação — `geologia-avancado-m14-q08` · oa01 · 10 pts

Um engenheiro de instrumentação avalia três faixas candidatas para uma nova banda de sensoriamento remoto óptico voltada a mapear minerais de alteração hidrotermal: 1,9 µm, 0,48 µm e 2,1 µm. Avalie cada uma quanto à absorção atmosférica e ao espalhamento, e diga qual é a mais adequada ao objetivo.

<details>
<summary>Ver resolução</summary>

**1,9 µm:** está dentro de uma faixa de forte absorção atmosférica por vapor d'água (a mesma família de bandas de absorção citada na Aula 02, ao lado de 1,4 µm) — a atmosfera bloqueia a maior parte da radiação solar nessa faixa antes de chegar ao alvo, e o pouco que retorna é absorvido de novo na subida. Um sensor aqui captaria muito pouco sinal útil de superfície. **Descartada.**

**0,48 µm (azul-esverdeado):** está numa janela atmosférica (a radiação atravessa), mas é comprimento de onda relativamente curto dentro do visível, portanto fortemente afetado pelo espalhamento de Rayleigh (proporcional a λ⁻⁴) — o contraste da imagem cai e a razão sinal-ruído se degrada, prejudicando a discriminação entre minerais espectralmente próximos. **Viável, mas subótima.**

**2,1 µm (SWIR):** está numa janela atmosférica razoavelmente limpa, fora das principais bandas de absorção de vapor d'água e CO₂, e o espalhamento de Rayleigh nessa faixa é ordens de grandeza menor do que no azul (λ⁻⁴ decresce rapidamente com o aumento do comprimento de onda). Além disso, é justamente nessa região que argilominerais e outros minerais de alteração hidrotermal têm feições de absorção vibracionais diagnósticas (mecanismo detalhado na Aula 03). **Escolha correta** — fisicamente limpa e informativa para o objetivo declarado, coerente com por que sensores geológicos reais (ASTER, Landsat 8/9) concentram bandas na região SWIR.
</details>

---

### 9. Verdadeiro ou Falso (justifique) — `geologia-avancado-m14-q09` · oa01 · 10 pts

"A cor avermelhada característica de um solo laterítico tropical é produzida pela mesma feição espectral (0,87-0,92 µm) que discrimina hematita de goethita."

<details>
<summary>Ver resposta</summary>

**Falso.**

São **dois mecanismos eletrônicos distintos**, e é justamente essa distinção que a Aula 03 constrói com cuidado. A **cor** do solo laterítico vem da cauda de uma banda de **transferência de carga** ligante-metal (O²⁻ → Fe³⁺), centrada no ultravioleta próximo (~0,25 µm) e intensa o bastante para invadir o visível pela borda azul, produzindo a queda de reflectância de 0,4-0,6 µm que o olho lê como vermelho-amarelado. A feição de **0,87-0,92 µm**, mais fraca e larga, é uma transição de **campo cristalino** do próprio íon Fe³⁺ — mecanismo diferente, faixa espectral diferente (infravermelho próximo, não ultravioleta/visível) — e sua posição exata é o que **discrimina hematita (~0,86 µm) de goethita (~0,90-0,92 µm)**, não a cor. Confundir os dois mecanismos foi exatamente o erro vermelho que a auditoria científica deste módulo corrigiu na Aula 03: atribuir a cor à feição de campo cristalino, ou o discriminador mineralógico à transferência de carga, inverte ambos.
</details>

---

### 10. Dissertativa curta — `geologia-avancado-m14-q10` · oa01 · 10 pts

Um geólogo de exploração observa, numa imagem multiespectral, uma área de vegetação com a borda vermelha deslocada para comprimentos de onda mais curtos, coincidente espacialmente com um alvo geoquímico de cobre já conhecido por amostragem de solo antiga. Ele conclui, só com essa imagem, que há **confirmação** de um novo corpo mineralizado abaixo da vegetação. Avalie essa conclusão à luz do que a Aula 03 ensina sobre geobotânica.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:**

A conclusão está **incorreta** em seu grau de certeza. O deslocamento da borda vermelha para comprimentos de onda mais curtos (*blue shift*) é, de fato, um sinal geobotânico consistente com estresse vegetal por metais — e sua coincidência espacial com uma anomalia geoquímica já conhecida reforça a hipótese. Mas a geobotânica produz **evidência indireta e probabilística, nunca confirmação**: o mesmo padrão de estresse (deslocamento de borda vermelha, redução de vigor) pode vir de deficiência hídrica, doença, compactação do solo, ou dezenas de outras causas não geológicas — a coincidência com a anomalia geoquímica antiga eleva a prioridade da área para investigação, mas não substitui verificação de campo (amostragem de solo, biogeoquímica de folhas, trincheira). Tratar esse sinal como confirmação de um "novo corpo mineralizado" superestima a robustez de uma evidência que, por natureza, é sempre indireta — o papel correto da geobotânica é gerar hipóteses e priorizar investigação, não substituí-la.
</details>

---

## Gabarito resumido

| Questão | ID | Resposta |
|---|---|---|
| 1 | q01 | c (SAR ativo de micro-ondas: independente de luz solar, atravessa nuvens) |
| 2 | q02 | Falso (Landsat 8/9 é heliossíncrono, não geoestacionário) |
| 3 | q03 | 90/30 = 3 pixels (marginal); 90/10 = 9 pixels (confortável) |
| 4 | q04 | b (par nominal 2B+2C desde jan/2025; 2A em campanha de extensão sobre a América do Sul) |
| 5 | q05 | ver comentário (as quatro resoluções competem por orçamento fixo; espacial fina reduz swath, que piora a temporal) |
| 6 | q06 | b (λ menor → ν maior → E maior; UV mais energético que SWIR) |
| 7 | q07 | Falso (Rayleigh ∝ λ⁻⁴, afeta muito mais o azul) |
| 8 | q08 | 2,1 µm (SWIR limpo e diagnóstico); 1,9 µm descartada (absorção); 0,48 µm viável mas subótima (Rayleigh) |
| 9 | q09 | Falso (cor = transferência de carga UV; 0,87-0,92 µm = campo cristalino, discrimina hematita/goethita) |
| 10 | q10 | ver comentário (evidência indireta e probabilística, não confirmação; exige verificação de campo) |
