# Questionário cumulativo — Módulo 16: Introdução à aerogeofísica

**Módulo:** [[16-aerogeofisica-modulo|Módulo 16 — Introdução à aerogeofísica]]
**Cobertura:** Aulas 01 a 05 (módulo completo — 5 aulas, no limiar da regra de parciais do plugin, ~5-6; decisão avaliada e registrada em `assessment.partials_recommendation` do `course-state.yaml`, não herdada por padrão). O módulo tem um corte natural entre aulas 02+03 (campos potenciais — magnetismo e gravidade, decaimento com a distância, ambiguidade de fonte) e aulas 04+05 (métodos não-potenciais — contagem radiométrica de superfície e indução eletromagnética dependente de frequência), com a Aula 01 transversal às quatro. Optou-se por **um questionário único**, porque o fio condutor do módulo — nenhum dos quatro métodos resolve sozinho a ambiguidade de fonte — é justamente o que um corte em duas parciais separaria.
**Objetivos avaliados:** geologia-avancado-m16-oa01, oa02, oa03, oa04 (todos)
**Distribuição:** oa01 = 4 questões (Q1-Q4), oa02 = 8 questões (Q5-Q12, cobrindo magnetometria da Aula 02 e gravimetria/gradiometria da Aula 03), oa03 = 4 questões (Q13-Q16, gamaespectrometria da Aula 04), oa04 = 2 questões (Q17-Q18, eletromagnetismo da Aula 05). Duas questões (Q9 e Q18) são de **integração multimétodo explícita**, o objetivo declarado do fechamento do módulo.

---

### 1. Múltipla escolha (oa01)
Uma empresa de exploração precisa escolher entre avião de asa fixa, helicóptero e VANT para um levantamento aeromagnético. Qual alternativa descreve corretamente a lógica da escolha?

a) O helicóptero é sempre a melhor opção, porque combina a maior resolução com a maior cobertura de área entre as três plataformas
b) Não existe uma plataforma que vença nas três frentes ao mesmo tempo — velocidade e autonomia (favorecendo reconhecimento regional) se pagam em resolução, e resolução se paga em área coberta; a escolha certa depende do problema geológico, não de qual plataforma é "melhor" em abstrato
c) A escolha entre as três plataformas é irrelevante para o resultado final, já que o processamento posterior equaliza qualquer diferença de aquisição entre elas
d) VANTs já substituíram integralmente aviões e helicópteros em todo tipo de levantamento aerogeofísico, incluindo gravimetria e gamaespectrometria de grande área

<details><summary>Ver resposta</summary>

**Resposta: b** — a Aula 01 é explícita: "não existe uma plataforma que ganhe nas três" (área, resolução, custo/velocidade). Avião de asa fixa favorece reconhecimento regional (maior velocidade e autonomia); helicóptero favorece exploração mineral de detalhe (voa mais baixo e devagar, drapeia melhor o relevo); VANT ocupa o nicho de área pequena e resolução extrema, limitado por bateria e carga útil. A alternativa a erra ao tratar o helicóptero como superior nas duas frentes ao mesmo tempo — ele perde para o avião em área/autonomia. A alternativa c contradiz o ponto central da aula: o processamento não recupera o que a aquisição não capturou. A alternativa d exagera a maturidade da plataforma — magnetometria é hoje o uso maduro de VANT, mas sensores mais pesados (gravímetro, espectrômetro gama de cristal grande) ainda dependem majoritariamente de avião e helicóptero (Aula 01).
</details>

---

### 2. Verdadeiro ou Falso (oa01)
"Se um levantamento aeromagnético de reconhecimento regional foi voado a 300 m de altura e, mais tarde, um intérprete percebe que um alvo raso ficou mal resolvido no mapa, um realce adequado (derivada, sinal analítico, continuação para baixo) aplicado ao dado já processado consegue recuperar a resolução que faltou, desde que o algoritmo seja bem escolhido."

<details><summary>Ver resposta</summary>

**Falso.** A altura de voo é o parâmetro isolado mais determinante do sinal captado, precisamente porque campos magnético e gravitacional decaem com a distância à fonte — e **nenhum processamento posterior recupera o sinal de fonte rasa perdido por voar alto demais**. Um realce reorganiza matematicamente a informação já presente no dado para tornar mais visível algum aspecto dela; ele não pode inventar o que a distância já apagou na aquisição. A continuação para baixo, em particular, simula uma altura menor e pode acentuar o que sobrou de sinal raso, mas amplifica ruído de forma agressiva e só é confiável até uma distância limitada abaixo da altura real — ela não substitui ter voado mais baixo (Aula 01, Aula 02).
</details>

---

### 3. Aplicação (cálculo, oa01)
Um levantamento aerogamaespectrométrico e aeromagnético de detalhe é planejado sobre um alvo com topo esperado a 180 m de profundidade. A altura de voo drapeada escolhida para o helicóptero é de 100 m. Calcule (a) a distância sensor-fonte relevante para o critério de Reid, (b) o teto de espaçamento de linha sem aliasing relevante (usando o fator de 2 vezes, e também o de 2,5 vezes, da prática operacional corrente), e (c) identifique o erro de projeto mais comum que o critério de Reid é usado para evitar.

<details><summary>Ver resolução</summary>

**(a) Distância sensor-fonte:** não é a profundidade do alvo isolada — é a soma da altura de voo com a profundidade do topo do corpo:

100 m (altura de voo) + 180 m (profundidade do topo) = **280 m**

**(b) Teto de espaçamento de linha (critério de Reid, 1980):**

Fator 2×: 2 × 280 m = **560 m**
Fator 2,5× (limite superior da prática operacional corrente): 2,5 × 280 m = **700 m**

O espaçamento **não deve exceder** essa faixa (560-700 m) para manter a fração de potência aliasada em poucos por cento, segundo F = exp(−2π·h/Δx). Como o objetivo aqui é delinear a geometria de um alvo, não apenas detectá-lo, na prática se escolheria um espaçamento bem abaixo desse teto — o teto é um limite máximo, não uma meta a ser atingida.

**(c) Erro de projeto mais comum:** usar apenas a profundidade do topo do alvo (180 m) como se fosse a distância sensor-fonte, esquecendo de somar a altura de voo (100 m). Isso daria um teto calculado de 360-450 m em vez dos 560-700 m corretos — um erro que, num levantamento voado mais alto, faz o intérprete acreditar que a malha resolve mais do que de fato resolve, porque o sensor já parte de uma distância adicional acima do solo que a profundidade sozinha não contabiliza (Aula 01).
</details>

---

### 4. Dissertativa curta (oa01)
Uma zona de cisalhamento mineralizada tem direção geral N45°W. Um geólogo júnior sugere orientar as linhas de voo principais paralelas a essa direção, argumentando que assim "o levantamento acompanha a estrutura e cobre toda a sua extensão de uma só vez". Explique por que essa lógica está invertida, qual deveria ser a orientação correta das linhas principais, e qual é o papel das linhas de controle (tie lines) nesse desenho.

<details><summary>Ver resposta comentada</summary>

**Resposta esperada:** a lógica está invertida porque uma linha de voo **paralela** a uma estrutura linear pode percorrê-la inteira sem nunca **cruzá-la** — cada linha individual mede um perfil transversal ao longo de seu próprio percurso, e se esse percurso corre ao lado da estrutura (ou sobre ela, num único ponto) em vez de atravessá-la, a anomalia associada à estrutura fica invisível ou irreconhecível no levantamento, independentemente de quão forte seja o contraste físico. "Cobrir a extensão" não é o mesmo que "cruzar a estrutura repetidamente" — é o cruzamento repetido, por várias linhas sucessivas, que constrói a imagem da estrutura ao longo de seu comprimento.

A orientação correta é **perpendicular** à direção estrutural predominante — aqui, aproximadamente N45°E — para que cada linha atravesse a zona de cisalhamento de frente e a registre como uma anomalia nítida, e o conjunto de linhas sucessivas, cada uma cruzando a estrutura num ponto diferente ao longo de seu comprimento, reconstrua sua extensão e continuidade.

As **linhas de controle (tie lines)** são voadas perpendicularmente às linhas principais (portanto aproximadamente paralelas à direção estrutural, N45°W) e mais espaçadas (ordem de 5 a 10 vezes o espaçamento principal); sua função não é mapear diretamente o alvo, mas fornecer os pontos de cruzamento com as linhas principais usados no **nivelamento** dos dados — ajustar cada linha para eliminar deslocamentos artificiais entre linhas adjacentes antes de gerar a grade final (Aula 01).
</details>

---

### 5. Múltipla escolha (oa02)
Sobre a ordem de processamento de um dado aeromagnético (remoção de IGRF, remoção de variação diurna, nivelamento entre linhas, aplicação de realces), qual alternativa está correta?

a) A remoção do IGRF deve necessariamente vir antes da remoção da variação diurna, porque o IGRF é um modelo de referência que define a linha de base sobre a qual a diurna é calculada
b) Entre IGRF e diurna não há ordem obrigatória, já que ambas são subtrações ponto a ponto do mesmo valor medido (e subtração é comutativa); o que é obrigatório é que as duas venham antes do nivelamento, e o nivelamento antes de qualquer realce, porque nivelamento e realce misturam informação entre pontos vizinhos ou entre linhas
c) Os realces devem ser aplicados antes do nivelamento, para que o algoritmo de realce ajude a identificar visualmente os pontos de cruzamento a serem nivelados
d) A ordem entre todas as quatro etapas é totalmente livre, incluindo a posição do nivelamento e dos realces, desde que todas sejam aplicadas eventualmente

<details><summary>Ver resposta</summary>

**Resposta: b** — IGRF e variação diurna são ambas subtrações de um número do valor medido em cada ponto, e subtração é comutativa: remover primeiro uma ou outra dá o mesmo resultado. O que é obrigatório é o **bloco**: as duas precisam vir antes do nivelamento, e o nivelamento antes de qualquer realce — porque essas duas últimas etapas não são subtrações de constantes, elas **misturam informação entre pontos vizinhos** (nivelamento, comparando linhas) ou operam sobre a grade inteira (realce, um filtro espacial). Aplicar qualquer um dos dois sobre um dado ainda com deriva diurna espalharia essa deriva pelo mapa inteiro, de um jeito que nenhuma correção posterior desfaz. A alternativa a inventa uma dependência que não existe; a c inverte a lógica (realce precisa do dado já nivelado, não o contrário); a d ignora que nivelamento e realce, ao contrário de IGRF/diurna, têm posição obrigatória na cadeia (Aula 02).
</details>

---

### 6. Verdadeiro ou Falso (oa02)
"A redução ao polo (RTP) é a transformação mais confiável para centrar anomalias magnéticas sobre corpos causadores em qualquer latitude magnética, incluindo perto do equador magnético, onde a distorção de forma da anomalia é mais extrema e por isso a correção é mais necessária."

<details><summary>Ver resposta</summary>

**Falso.** É verdade que a distorção é mais extrema perto do equador magnético (inclinação próxima de zero, campo quase horizontal, anomalia podendo aparecer deslocada e como par de lóbulos). Mas é exatamente aí que a RTP se torna **matematicamente instável** — o filtro amplifica ruído de forma descontrolada porque o termo que divide a operação tende a zero quando a inclinação se aproxima de zero. A RTP é, portanto, menos confiável justamente onde seria mais necessária. Nessas condições, usam-se alternativas mais estáveis, como a redução ao equador (RTE) ou transformações que não dependem da direção do campo, como o sinal analítico (Aula 02).
</details>

---

### 7. Aplicação (cálculo, oa02)
Um levantamento aeromagnético é voado num único dia. A estação-base registra 50.120 nT às 08h00 (nível de referência) e 50.155 nT às 12h00. O IGRF calculado para a posição e a data do levantamento é 50.095 nT. Uma medida aérea feita às 12h00, sobre um ponto de interesse, registra um campo total bruto de 50.340 nT. Calcule a anomalia de campo total (TMI residual) desse ponto.

<details><summary>Ver resolução</summary>

**Passo 1 — variação diurna às 12h00:**

50.155 − 50.120 = **+35 nT**

**Passo 2 — remover a diurna da medida aérea bruta:**

50.340 − 35 = **50.305 nT**

**Passo 3 — remover o IGRF:**

50.305 − 50.095 = **+210 nT**

**TMI residual = +210 nT.** Como no exemplo da aula, a ordem entre remover a diurna e remover o IGRF não altera o resultado (ambas são subtrações comutativas do mesmo valor medido) — o que importa é que as duas sejam removidas antes de qualquer nivelamento ou realce ser aplicado sobre a grade (Aula 02).
</details>

---

### 8. Múltipla escolha (oa02)
Sobre a independência do sinal analítico em relação à direção de magnetização do corpo causador, qual afirmação está correta?

a) O sinal analítico tem amplitude totalmente independente da direção de magnetização em qualquer geometria de corpo, o que o torna sempre preferível à RTP, inclusive para plugs e lentes de sulfeto compactas
b) Essa independência é rigorosa apenas para fontes bidimensionais (diques extensos, contatos retilíneos); para corpos tridimensionais compactos, a amplitude do sinal analítico volta a depender da direção de magnetização, embora bem menos que a anomalia de campo total — a posição do máximo pode se deslocar em relação ao corpo real
c) A independência do sinal analítico só se aplica perto dos polos magnéticos, onde a inclinação é de 90°, e desaparece completamente perto do equador
d) O sinal analítico é matematicamente idêntico à redução ao polo, apenas com um nome diferente

<details><summary>Ver resposta</summary>

**Resposta: b** — a independência da amplitude do sinal analítico em relação à direção de magnetização (induzida ou remanente) é uma propriedade **rigorosa apenas para fontes 2D**. Sobre corpos 3D compactos — um plug, uma lente de sulfeto, um kimberlito — essa amplitude volta a depender da direção de magnetização, e a interpretação segura de um alvo compacto e fortemente remanente passa por modelagem direta, não por leitura visual do mapa. A alternativa a generaliza a propriedade para qualquer geometria, o erro que a literatura de divulgação costuma cometer; a c inverte a lógica (o sinal analítico é útil justamente perto do equador, onde a RTP falha); a d confunde duas transformações distintas — a RTP depende da direção do campo e é instável em baixa latitude, o sinal analítico é uma combinação de derivadas menos (mas não totalmente) dependente dessa direção (Aula 02).
</details>

---

### 9. Dissertativa curta — integração multimétodo (oa02, ligando Aulas 02 e 05)
Um levantamento eletromagnético (EM) detecta um condutor raso, e um levantamento aeromagnético sobre a mesma área mostra uma anomalia magnética moderada coincidente. Um geólogo conclui, só com base nessa coincidência, que o condutor é necessariamente um corpo sulfetado maciço de interesse econômico. Usando o que você sabe sobre magnetismo de minerais sulfetados (Módulo 15) e sobre condutores eletromagnéticos (Aula 05), explique por que essa conclusão é apressada e que minerais especificamente poderiam explicar a resposta magnética coincidente.

<details><summary>Ver resposta comentada</summary>

**Resposta esperada:** a conclusão é apressada porque tanto a anomalia magnética quanto a resposta EM condutora têm, cada uma isoladamente, ambiguidade de fonte. Um condutor eletromagnético pode ser um corpo sulfetado de interesse econômico, mas também, com a mesma facilidade, água salina em fratura, grafita em xisto ou solo/argila saturado — nenhum desses "falsos positivos" tem relação com mineralização. A coincidência espacial com uma anomalia magnética **restringe**, mas não **prova**: entre os sulfetos, apenas os que contêm uma fase ferrimagnética explicam a resposta magnética — especificamente a **pirrotita monoclínica** (Fe₇S₈), que é ferrimagnética. A pirita e a grafita, dois dos falsos condutores clássicos, **não são magnéticas**; e mesmo dentro dos sulfetos de ferro, a **pirrotita hexagonal** é antiferromagnética à temperatura ambiente, não ferrimagnética — só a variedade monoclínica produziria a anomalia observada. Portanto, a coincidência entre condutor EM e anomalia magnética moderada é uma hipótese de exploração mais robusta do que qualquer evidência isolada, mas ainda não é uma prova: ela elimina a grafita e a pirita puras como explicação única, mas não distingue, sozinha, entre um corpo sulfetado com pirrotita monoclínica e outras fontes menos prováveis de magnetismo coincidente com um condutor raso — a integração reduz a ambiguidade, não a elimina (Aula 05, com base no Módulo 15).
</details>

---

### 10. Verdadeiro ou Falso (oa02)
"Se dois voos aerogravimétricos passam pelo mesmo ponto geográfico, um voando para leste e o outro para oeste, e a correção de Eötvös não for aplicada, os dois registrariam o mesmo valor de gravidade, porque a rotação da Terra afeta igualmente qualquer direção de voo."

<details><summary>Ver resposta</summary>

**Falso.** O efeito Eötvös é justamente a variação sistemática da gravidade aparente causada pela composição da velocidade da aeronave com a rotação da Terra: voar para leste **soma-se** à velocidade de rotação da Terra, aumentando a aceleração centrífuga aparente e **reduzindo** a gravidade medida; voar para oeste, o efeito se **inverte**. Sem a correção de Eötvös, os dois voos registrariam valores sistematicamente diferentes no mesmo ponto — não por diferença geológica real, mas por razão puramente cinemática, dependente do rumo da aeronave. É exatamente esse efeito que a correção de Eötvös, calculada a partir da velocidade e do rumo por GNSS, remove (Aula 03).
</details>

---

### 11. Múltipla escolha (cálculo/raciocínio, oa02)
Um gradiômetro de gravidade aéreo mede, num ponto, um gradiente **vertical** (a componente G_DD do tensor, ∂g_z/∂z) de 22 Eötvös. Um intérprete quer estimar a variação de gravidade ao longo de 500 m de uma linha de voo **horizontal**. Qual alternativa trata esse cálculo corretamente?

a) Δg = 22 Eo × 0,1 mGal/km por Eo × 0,5 km = 1,1 mGal, porque a conversão de Eötvös para mGal/km vale para qualquer componente do tensor
b) Não é possível calcular a variação de gravidade ao longo da linha horizontal a partir apenas do gradiente vertical informado — seria necessário o gradiente na própria direção horizontal da linha (uma componente diferente do tensor), já que um gradiente só pode ser multiplicado por uma distância se ambos apontarem na mesma direção
c) O gradiente vertical é sempre numericamente igual ao horizontal em qualquer ponto, por isotropia do campo gravitacional, então o cálculo do item (a) está correto por outra razão
d) A equivalência correta é 1 Eötvös = 10 mGal/km, então Δg = 22 × 10 × 0,5 = 110 mGal

<details><summary>Ver resposta</summary>

**Resposta: b** — um gradiente vertical (G_DD) descreve como a gravidade variaria se a aeronave subisse ou descesse, não como ela varia ao longo de uma linha de voo horizontal, que é governada pela componente **horizontal** do tensor na direção daquela linha. Multiplicar um gradiente vertical por uma distância horizontal é um erro dimensionalmente invisível — a conta "fecha" (dá um número plausível), mas mistura duas componentes físicas diferentes do tensor. A alternativa a comete exatamente esse erro; a c inventa uma isotropia que não existe (o tensor gravitacional não é isotrópico em geral); a d erra a conversão — a equivalência correta, reverificada por derivação, é **1 Eo = 0,1 mGal/km**, não 10 mGal/km (Aula 03).
</details>

---

### 12. Dissertativa curta (oa02)
Explique por que a gradiometria de gravidade consegue resolver alvos rasos e pequenos com mais nitidez do que a gravimetria escalar aérea convencional, e por que essa mesma vantagem exige que os levantamentos de gradiometria voem mais baixo e com linhas mais próximas do que seria necessário para gravimetria convencional sobre o mesmo alvo.

<details><summary>Ver resposta comentada</summary>

**Resposta esperada:** a gradiometria mede uma **diferença** entre acelerômetros próximos entre si (a variação espacial do campo numa distância curta), em vez de medir a gravidade absoluta. Como o ruído de baixa frequência do movimento da aeronave — manobra, turbulência, boa parte da aceleração espúria — afeta igualmente todo o instrumento, ele se **cancela na própria subtração**, sobrando principalmente o sinal de variação espacial real do campo geológico. É essa vantagem, por construção, que permite à gradiometria resolver alvos rasos e pequenos que a gravimetria escalar aérea, dominada por ruído de baixa frequência do movimento, dificilmente conseguiria separar do sinal.

A mesma vantagem tem um custo: o **gradiente** de um corpo geológico cai com a distância à fonte **mais rapidamente** do que a própria gravidade cai com a distância. Um corpo que ainda produziria um sinal gravimétrico mensurável a uma certa altura de voo pode já estar abaixo do limiar de detecção do gradiômetro na mesma altura — por isso a gradiometria exige voar mais baixo e com linhas mais próximas do que a gravimetria convencional para o mesmo alvo, o que também explica por que ela é reservada a levantamentos de detalhe, não de reconhecimento regional (Aula 03, com a mesma lógica de altura de voo vista na Aula 01).
</details>

---

### 13. Múltipla escolha (oa03)
Sobre a ordem de processamento de um dado aerogamaespectrométrico, qual sequência está correta?

a) Espectro bruto → correção de altura → stripping (Compton) → tempo morto → background → conversão em concentração
b) Espectro bruto → tempo morto → background (cósmico + aeronave + radônio) → stripping (Compton) → correção de altura → conversão em concentração
c) Espectro bruto → background → stripping → tempo morto → conversão em concentração → correção de altura
d) A ordem entre stripping e correção de altura é arbitrária, desde que ambas sejam aplicadas antes da conversão em concentração

<details><summary>Ver resposta</summary>

**Resposta: b** — a sequência correta é tempo morto → background (cósmico, aeronave, radônio) → stripping (Compton) → correção de altura (atenuação atmosférica) → conversão em concentração. O **stripping vem antes da correção de altura**, e isso não é arbitrário: o stripping resolve um problema **espectral** (de qual elemento veio cada contagem) e precisa operar sobre as contagens de cada janela antes que elas sejam reescaladas; a correção de altura resolve um problema de **transporte** (quanto do sinal que saiu do solo chegou ao detector) e seus coeficientes de atenuação são definidos **por elemento**, o que só faz sentido depois que as contagens já foram separadas por elemento — e as próprias razões de stripping são corrigidas para a altura de voo antes de aplicadas, então a informação de altura entra no stripping, não o contrário. As alternativas a e c invertem essa ordem obrigatória; a d trata como opcional uma ordem que é obrigatória por razão física, ao contrário do par IGRF/diurna da Aula 02, que de fato é comutativo (Aula 04).
</details>

---

### 14. Verdadeiro ou Falso (oa03)
"Uma área com razão Th/U de 6,0 está dentro da faixa de 2 a 7 considerada normal para rocha não alterada pela régua da IAEA, portanto não há motivo algum para desconfiar de processo de alteração ali, já que o valor está dentro do intervalo esperado."

<details><summary>Ver resposta</summary>

**Falso**, ou pelo menos incompleto de um jeito que importa. A faixa 2-7 é uma faixa larga de **tolerância**, não o valor esperado — o valor de referência crustal é bem mais estreito, em torno de **3,5 a 4** (crosta continental superior ≈3,9; crosta continental total ≈4,3). Um Th/U de 6,0 está tecnicamente "dentro da faixa", mas já é sensivelmente mais alto que a crosta média e **merece uma segunda olhada**, porque existe um gradiente interpretável dentro da faixa: valores se afastando do centro (~3,5-4) em direção ao limite superior (7) já podem refletir início de lixiviação de urânio por intemperismo oxidante, mesmo sem cruzar o limiar formal de 7. Ler a régua como um simples semáforo (dentro = normal, fora = anômalo) faz perder exatamente esse gradiente, que é onde a alteração incipiente aparece primeiro (Aula 04).
</details>

---

### 15. Aplicação (cálculo, oa03)
Um levantamento aerogamaespectrométrico sobre duas áreas registra: Área C — K = 2,8%, eU = 3,0 ppm, eTh = 18,0 ppm; Área D — K = 0,6%, eU = 10,8 ppm, eTh = 5,4 ppm. Calcule a razão Th/U de cada área e, usando a régua da IAEA (faixa 2-7 de tolerância e valor de referência crustal ≈3,5-4), interprete cada uma.

<details><summary>Ver resolução</summary>

**Área C:** Th/U = 18,0 / 3,0 = **6,0**

Está tecnicamente dentro da faixa de tolerância (2-7), mas bem acima do valor de referência crustal (~3,5-4) — não chega a cruzar o limiar de 7 que caracterizaria lixiviação clara, mas o afastamento do centro da distribuição já é um sinal de atenção: compatível com início de processo de lixiviação de urânio por intemperismo, ainda incipiente, não com rocha fresca típica.

**Área D:** Th/U = 5,4 / 10,8 = **0,5**

Está bem **abaixo** do limite inferior (2) da faixa — a assinatura clássica de **enriquecimento de urânio em ambiente redutor**, como um folhelho negro rico em matéria orgânica, onde a precipitação e retenção do urânio (insolúvel em condições redutoras) não é acompanhada pelo tório.

Nos dois casos, a leitura correta exige comparar a razão contra a régua **e** contra o valor de referência crustal — o simples "dentro/fora da faixa 2-7" perderia a diferença de grau entre a Área C (levemente elevada, incipiente) e um caso mais extremo que cruzasse o limiar de 7 (Aula 04).
</details>

---

### 16. Dissertativa curta (oa03)
Um relatório de exploração descreve um halo vermelho no mapa ternário sobre um sistema pórfiro cuprífero como "zona de alteração potássica, com sericita e feldspato potássico secundários introduzidos pelos fluidos hidrotermais". Aponte o que está tecnicamente incorreto nessa descrição e explique por que o mapa gamaespectrométrico, sozinho, não permite corrigir esse erro.

<details><summary>Ver resposta comentada</summary>

**Resposta esperada:** a descrição funde num só nome duas zonas de alteração que o modelo de zoneamento de pórfiro cuprífero (Lowell & Guilbert, 1970) trata como **distintas**. A alteração **potássica** propriamente dita, no núcleo quente do sistema, introduz **feldspato potássico e biotita** secundários — não sericita. A alteração **fílica (sericítica)**, mais rasa e mais fria, que envolve a potássica, introduz **sericita + quartzo + pirita**. Colocar sericita na descrição da zona potássica embaralha o modelo de zoneamento, e a distinção importa na exploração porque as duas zonas têm relações diferentes com a mineralização de cobre.

O mapa gamaespectrométrico sozinho não permite corrigir esse erro porque **ambas as zonas produzem um alto de potássio** no canal K — o sensor registra "mais potássio aqui", não "qual zona do modelo de zoneamento está aqui". A gamaespectrometria não distingue a mineralogia responsável pelo enriquecimento (feldspato potássico + biotita vs. sericita + quartzo + pirita); essa distinção exige petrografia ou mapeamento geológico de campo — o mapa ternário indica **onde** investigar, não substitui a investigação (Aula 04).
</details>

---

### 17. Aplicação (cálculo, oa04)
Um levantamento aéreo sobre um terreno com resistividade estimada de 500 ohm-m precisa decidir entre um sistema VLF operando a 25 kHz e um sistema AFMAG/campo natural operando a 50 Hz, para investigar uma estrutura condutora suspeita a 150 m de profundidade. Calcule a profundidade pelicular aproximada de cada sistema e determine qual é capaz de "enxergar" a estrutura. Em seguida, explique por que esse resultado não deve ser lido como "profundidade máxima de detecção" no sentido estrito.

<details><summary>Ver resolução</summary>

**Sistema VLF (f = 25.000 Hz):**

δ = 503 × √(500 / 25.000) = 503 × √0,02 = 503 × 0,1414 ≈ **71 m**

**Sistema AFMAG/NFEM (f = 50 Hz):**

δ = 503 × √(500 / 50) = 503 × √10 = 503 × 3,162 ≈ **1.590 m**

**Interpretação:** a profundidade pelicular do VLF (≈71 m) é bem menor que a profundidade do alvo (150 m) — o sinal já estaria fortemente atenuado antes de alcançar a estrutura, tornando o VLF inadequado para esse objetivo específico (ainda que seja excelente para condutores muito mais rasos). A profundidade pelicular do AFMAG/NFEM (≈1.590 m) está bem acima dos 150 m do alvo, então o sinal de 50 Hz ainda carrega energia suficiente naquela profundidade — o AFMAG/NFEM é a escolha adequada.

**Por que não é "profundidade máxima de detecção":** a profundidade pelicular é uma medida de **atenuação** do campo primário — a distância na qual sua amplitude cai a cerca de 37% (1/e) do valor de superfície —, não um limite binário de detecção. A detectabilidade real de um corpo específico depende também do seu tamanho, de seu contraste de condutividade com a rocha encaixante e do nível de ruído do sistema; a interpretação quantitativa completa de um levantamento EM real usa modelagem numérica, não apenas a fórmula de skin depth. A comparação acima captura corretamente a razão física de fundo (frequência baixa penetra mais fundo), mas não substitui uma avaliação de detectabilidade real (Aula 05).
</details>

---

### 18. Aplicação de síntese — integração multimétodo (Aulas 01-05, todos os objetivos)
Um levantamento aerogeofísico integrado (magnetometria, gradiometria de gravidade, gamaespectrometria e EM de domínio de tempo) sobrevoa uma área de 80 km² de terreno com cobertura laterítica moderada, usando helicóptero, altura de voo drapeada de 70 m e linhas espaçadas a 150 m. Num polígono de 1,5 km² dentro da área, os quatro conjuntos de dados mostram, de forma espacialmente coincidente:

- **EM (TDEM):** um condutor de resposta forte e decaimento lento (compatível com corpo grande e/ou muito condutor);
- **Magnetometria:** uma anomalia magnética de amplitude moderada, sem inversão de polaridade abrupta ao longo do corpo, sugerindo geometria alongada (2D);
- **Gradiometria de gravidade:** um leve excesso gravimétrico (gradiente pouco acima do nível de ruído documentado do sistema) coincidente com o condutor;
- **Gamaespectrometria:** um halo de potássio elevado no mapa ternário (tom avermelhado) circundando a área do condutor, com Th/U ao redor de 4 fora do halo e caindo para valores mais baixos dentro dele.

**Pergunta:** (a) que hipótese geológica integrada essas quatro evidências sustentam em conjunto, e por que nenhuma delas, isoladamente, sustentaria essa hipótese com a mesma força? (b) Que verificação de campo ou ressalva você recomendaria antes de declarar essa área um alvo de perfuração, considerando as limitações específicas de cada método discutidas ao longo do módulo?

<details><summary>Ver resolução</summary>

**(a) Hipótese integrada:** a coincidência espacial das quatro evidências sustenta a hipótese de um corpo sulfetado condutor com alguma fase ferrimagnética (compatível com pirrotita monoclínica, não pirita nem grafita puras, que não são magnéticas) e densidade um pouco maior que a encaixante, associado a um sistema de alteração hidrotermal que produziu um halo de enriquecimento em potássio na superfície ou subsuperfície rasa.

Isoladamente, nenhuma evidência sustentaria essa força de hipótese: **o condutor EM** sozinho tem ambiguidade clássica de fonte — poderia ser água salina em fratura, grafita em xisto ou argila/solo saturado, três "falsos positivos" que produzem resposta condutora forte sem relação com mineralização (Aula 05). **A anomalia magnética** sozinha poderia vir de magnetita disseminada sem valor econômico (Aula 05, fechamento do módulo) — apenas coincidente com um condutor ela começa a apontar para um sulfeto especificamente ferrimagnético. **O excesso gravimétrico**, perto do limiar de ruído do sistema, seria fraco demais para sustentar sozinho qualquer interpretação — mas reforça a hipótese ao ser coincidente com as outras três. **O halo potássico** da gamaespectrometria, sozinho, é ambíguo quanto à zona de alteração exata (potássica vs. fílica — a gamaespectrometria não separa as duas, Aula 04) e reflete apenas os primeiros 30-45 cm de terreno, podendo estar mascarado ou distorcido pela cobertura laterítica descrita no enunciado. É a coincidência das quatro, cada uma eliminando algumas explicações alternativas que as outras três não conseguem descartar sozinhas, que transforma a anomalia isolada numa hipótese de exploração robusta.

**(b) Verificações e ressalvas recomendadas:**

- **Sobre o halo potássico:** determinar se a cobertura laterítica sobre o alvo é **residual** (formada in situ sobre a rocha/alteração subjacente, caso em que o sinal radiométrico é informativo sobre o que está embaixo) ou **transportada** (caso em que o eTh e o K medidos refletem o material transportado, não a rocha em profundidade) — isso é trabalho de mapeamento de regolito e geomorfologia, não da gamaespectrometria isoladamente (Aula 04). Também vale confirmar em campo/petrografia se o halo reflete alteração potássica (feldspato potássico + biotita) ou fílica (sericita + quartzo + pirita), já que o mapa ternário não distingue as duas.
- **Sobre a anomalia magnética:** como a geometria sugerida é alongada (2D), a leitura da posição da anomalia é relativamente confiável mesmo sem RTP perfeita ou modelagem fina — mas se a geometria real se revelar mais compacta (3D) em detalhamento posterior, a posição do máximo magnético (e do sinal analítico, se usado) pode não coincidir exatamente com o corpo, exigindo modelagem direta antes de decidir a posição do furo (Aula 02).
- **Sobre o excesso gravimétrico:** por estar perto do nível de ruído documentado do sistema de gradiometria, recomenda-se reprocessar com filtro de comprimento de onda adequado e, se possível, voar uma linha de repetição sobre o polígono para confirmar que o sinal é reprodutível e não ruído residual de movimento da aeronave (Aula 03).
- **Sobre o condutor EM:** um decaimento lento é compatível com corpo grande/muito condutor, mas grafita em xisto também pode produzir decaimento lento — a distinção final entre sulfeto econômico e falso condutor não é feita por nenhum dos quatro métodos aéreos isoladamente, e sim por sondagem ou levantamento terrestre de detalhe, que a aerogeofísica **direciona**, mas não substitui (Aula 01, Aula 05).

Em suma: a integração multimétodo é o que justifica investir em verificação de campo nesse polígono específico em vez de outro — mas "hipótese robusta" não é "prova", e cada uma das quatro camadas de evidência carrega uma ressalva própria que precisa ser resolvida antes de declarar o alvo pronto para perfuração (síntese do módulo, Aula 05).
</details>

---

### Gabarito resumido

| Questão | Resposta |
|---|---|
| 1 | b |
| 2 | Falso |
| 3 | distância sensor-fonte=280 m; teto=560-700 m; erro comum=usar só a profundidade |
| 4 | ver comentário |
| 5 | b |
| 6 | Falso |
| 7 | TMI residual = +210 nT |
| 8 | b |
| 9 | ver comentário |
| 10 | Falso |
| 11 | b |
| 12 | ver comentário |
| 13 | b |
| 14 | Falso |
| 15 | Th/U(C)=6,0 → levemente elevado, atenção; Th/U(D)=0,5 → enriquecimento redutor |
| 16 | ver comentário |
| 17 | δ_VLF≈71 m (inadequado); δ_AFMAG≈1.590 m (adequado); skin depth é atenuação, não profundidade máxima de detecção |
| 18 | ver comentário |

## Cobertura de objetivos confirmada
- geologia-avancado-m16-oa01 — questões 1, 2, 3, 4
- geologia-avancado-m16-oa02 — questões 5, 6, 7, 8, 9, 10, 11, 12
- geologia-avancado-m16-oa03 — questões 13, 14, 15, 16
- geologia-avancado-m16-oa04 — questões 17, 18

## Notas de rastreabilidade

- Achados vermelhos/laranjas da auditoria (`audit.dominant_pattern` do `course-state.yaml`, padrão "ORDEM E DIRECAO") foram usados deliberadamente como **distratores**, nunca como afirmação de gabarito:
  - Stripping vs. correção de altura (Aula 04): a Q13 apresenta a ordem invertida (altura antes de stripping) como alternativa incorreta (a), e a ordem correta com justificativa física própria como resposta certa (b).
  - Gradiente vertical multiplicado por distância horizontal (Aula 03): a Q11 constrói o cálculo especificamente para testar se o aluno reconhece esse erro dimensionalmente invisível, com a alternativa errada (a) reproduzindo a conta "que fecha" e a correta (b) explicando por que a operação não é válida.
  - Espaçamento de linha por profundidade isolada, não por distância sensor-fonte (Aula 01): a Q3 pede explicitamente o cálculo da distância sensor-fonte como soma de altura + profundidade, e a Q1/recap reforçam que a decisão de plataforma/altura não tem "melhor" absoluto.
  - Sinal analítico independente da direção de magnetização só para fontes 2D (Aula 02): Q8 tem como distrator (a) a generalização para "qualquer geometria de corpo", corrigida pela alternativa b.
  - Alteração potássica vs. fílica como zonas distintas (Aula 04): Q16 usa como cenário exatamente o erro de nomenclatura corrigido pela auditoria (sericita atribuída à zona potássica) e pede a correção justificada.
  - IAEA-TECDOC-1363, não "TRS 452": nenhuma questão pede a designação do documento por nome, mas a régua Th/U (Q14, Q15) e a cadeia de processamento (Q13) se apoiam no conteúdo desse documento, corretamente atribuído nas fontes da Aula 04.
  - Th/U crustal ≈3,5-4 como refinamento da faixa 2-7, não contradição dela (Aula 04, Módulo 15): Q14 e Q15 testam explicitamente a diferença entre "dentro da faixa" e "próximo do valor de referência crustal", com a Área C da Q15 (Th/U=6,0) desenhada para estar tecnicamente dentro da faixa mas merecer atenção — nem tratada como anômala nem como normal sem ressalva.
  - Magnetismo de rocha: titanomagnetita/maghemita/pirrotita monoclínica, não ilmenita (paramagnética): Q9 usa a distinção pirrotita monoclínica (ferrimagnética) vs. pirrotita hexagonal (antiferromagnética) vs. pirita/grafita (não magnéticas) como o núcleo do raciocínio de integração, consistente com o Módulo 15.
  - 1 Eötvös = 0,1 mGal/km, não invertido: Q11 inclui como distrator (d) a inversão "1 Eo = 10 mGal/km".
  - Skin depth não é profundidade máxima de investigação: Q17 pede explicitamente essa ressalva como parte da resposta, não apenas o cálculo numérico.
- Duas questões de integração multimétodo explícita, conforme pedido: Q9 (condutor EM + anomalia magnética, ligando Aulas 02 e 05, com o raciocínio mineral específico pirrotita monoclínica vs. falsos condutores) e Q18 (síntese final com os quatro métodos sobre um mesmo alvo, incluindo a etapa de verificação/ressalva por método, o fio condutor declarado no fechamento da Aula 05).
- Nenhum achado azul ou branco da auditoria (ex.: nuances de precisão de sistemas comerciais Falcon/Air-FTG) foi transformado em fato de gabarito fechado — apenas os achados vermelhos/laranjas/amarelos, que representam risco real de erro conceitual, viraram material de questão.
- Seis das dezoito questões são de cálculo numérico com valores próprios, distintos dos exemplos trabalhados das aulas, exigindo aplicação da fórmula em vez de reconhecimento do número: espaçamento de linha (Q3: 100 m + 180 m, distinto de 60-80 m + 150 m), TMI residual (Q7: 50.120/50.155/50.095/50.340 nT, distinto de 45.230/45.268/45.210/45.410 nT), conversão de gradiente (Q11: 22 Eo/500 m, distinto de 18 Eo/400 m, usado aqui para testar o erro conceitual em vez do cálculo em si), Th/U (Q15: K/eU/eTh de duas áreas novas, distintas das do exemplo da Aula 04), skin depth (Q17: ρ=500 ohm-m, VLF 25 kHz, AFMAG 50 Hz, alvo a 150 m, distinto de ρ=1.000 ohm-m/20 kHz/30 Hz/250 m da Aula 05) e a síntese da Q18 (cenário integrado novo, sem repetir nenhum exemplo trabalhado das cinco aulas).
- Todos os valores numéricos reutilizados como referência (não como resposta a decorar) seguem os já auditados do módulo: 1 Eo = 0,1 mGal/km; Th/U crustal ≈3,5-4; skin depth δ≈503√(ρ/f); ordem de processamento gamaespectrométrico com stripping antes da altura.
