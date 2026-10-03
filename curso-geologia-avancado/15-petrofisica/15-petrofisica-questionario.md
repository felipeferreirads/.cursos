# Questionário cumulativo — Módulo 15: Introdução à petrofísica

**Módulo:** [[15-petrofisica-modulo|Módulo 15 — Introdução à petrofísica]]
**Cobertura:** Aulas 01 a 04 (módulo completo — 4 aulas, abaixo do limiar de ~5–6 que aciona questionários parciais; as quatro aulas são propriedades físicas paralelas, não uma progressão em dois blocos, e nenhum corte candidato separa objetivos inteiros — ver [[15-petrofisica-revisao-didatica|revisão didática]] e o campo `partials_recommendation` do `course-state.yaml`).
**Objetivos avaliados:** geologia-avancado-m15-oa01, oa02, oa03, oa04 (todos)
**Distribuição:** oa01 = 4 questões, oa02 = 4, oa03 = 5 (cobrindo magnetismo e radioatividade, já que o único exemplo trabalhado da Aula 03 é gamaespectrométrico), oa04 = 3, a última de síntese integrando as quatro propriedades sobre uma única rocha.

---

### 1. Múltipla escolha (oa01)
Sobre a diferença entre porosidade total e porosidade efetiva (definição de análise de testemunho), qual alternativa está correta?

a) As duas são sempre numericamente iguais, porque toda porosidade de uma rocha está, por definição, interconectada
b) A porosidade efetiva conta apenas o espaço poroso interconectado, disponível ao fluxo; a diferença para a porosidade total é a porosidade isolada, que não participa do fluxo de fluido
c) A porosidade total é sempre menor que a efetiva, porque a efetiva inclui os poros isolados além dos conectados
d) A distinção só importa em rochas ígneas e metamórficas, nunca em arenitos ou calcários

<details><summary>Ver resposta</summary>

**Resposta: b** — porosidade total inclui todo o espaço vazio, conectado ou não; porosidade efetiva (definição de testemunho) conta só o espaço interconectado, disponível ao fluxo. A diferença entre as duas é a porosidade isolada. A alternativa a erra ao supor que toda porosidade é sempre conectada — justamente o caso de uma rocha vulcânica vesicular ou de um folhelho mostra o oposto; a alternativa c inverte a relação (a total é sempre ≥ a efetiva, nunca menor); a alternativa d é falsa porque a distinção aparece em qualquer litologia com poros isolados, incluindo arenitos cimentados e calcários vugulares (Aula 01).
</details>

---

### 2. Verdadeiro ou Falso (oa01)
"A porosimetria de mercúrio é a técnica que identifica e quantifica diretamente os poros isolados de uma rocha, já que o mercúrio, sob pressão suficiente, penetra em qualquer espaço vazio do meio poroso."

<details><summary>Ver resposta</summary>

**Falso.** A intrusão de mercúrio preenche progressivamente os poros **acessíveis a partir da superfície** ao longo da rede **conectada** — ela não alcança poros isolados por definição, e essa é justamente a limitação declarada da técnica (é também a razão de a moagem da amostra alterar o resultado: moer a rocha conecta artificialmente poros antes isolados). A porosidade isolada não é medida diretamente por nenhuma técnica de injeção; ela é obtida **por diferença** entre a porosidade total (via picnometria de hélio, que mede o volume de grãos) e a porosidade conectada (Aula 01).
</details>

---

### 3. Aplicação (cálculo, oa01)
Uma amostra cilíndrica de arenito, coletada em testemunho de sondagem, tem volume total de 60 cm³. Em laboratório, mede-se volume de grãos sólidos (matriz) de 45 cm³, e, ao saturar a amostra com salmoura sob vácuo, apenas 12 cm³ de fluido entram efetivamente nos poros interconectados. Calcule (a) a porosidade total, (b) a porosidade efetiva, (c) a porosidade isolada, e (d) em quanto (%) um relatório que reportasse só a porosidade total, sem qualificar qual das duas está sendo citada, superestimaria a capacidade real de a rocha entregar fluido.

<details><summary>Ver resolução</summary>

Volume de poros totais = 60 − 45 = **15 cm³**.

(a) Porosidade total: φ_total = 15 / 60 = 0,25 → **25%**

(b) Porosidade efetiva: φ_efetiva = 12 / 60 = 0,20 → **20%**

(c) Porosidade isolada: 25% − 20% = **5 pontos percentuais** (5/25 = 20% de toda a porosidade da amostra)

(d) Superestimativa relativa: (25% − 20%) / 20% = 5/20 = **25%** — reportar 25% de porosidade sem qualificação superestimaria em um quarto a fração de espaço que efetivamente participa do fluxo de fluido, exatamente o tipo de erro que muda uma decisão de campo de estimativa de volume recuperável ou de capacidade de armazenamento de aquífero/reservatório (Aula 01).
</details>

---

### 4. Dissertativa curta (oa01)
Um folhelho tem porosidade total de 35%, maior que a de um arenito-reservatório com porosidade de 20%. Ainda assim, a permeabilidade do arenito pode ser muitas ordens de grandeza maior que a do folhelho. Explique, em termos geométricos (não apenas "são rochas diferentes"), por que isso acontece, e diga qual dessas duas grandezas — corpo de poro ou garganta de poro — é a que controla a permeabilidade.

<details><summary>Ver resposta comentada</summary>

**Resposta esperada:** permeabilidade não depende do volume poroso total (o que a porosidade mede), mas do **tamanho das gargantas de poro** — a abertura mais estreita ao longo do caminho de conexão entre dois poros —, da **conectividade** da rede e da presença de argila/material fino obstruindo essas gargantas. No folhelho, os poros são numerosos (por isso a porosidade total é alta) mas extremamente pequenos, tortuosos e frequentemente desconectados pela orientação plana dos minerais de argila — a garganta de poro, não o corpo de poro, é o gargalo que controla o fluxo, e ela é minúscula. No arenito, mesmo com menos espaço poroso total, as gargantas entre os grãos são largas e bem conectadas, permitindo fluxo fácil. É a **garganta de poro** que controla a permeabilidade — porosidade conta o espaço, permeabilidade conta o caminho, e nada obriga os dois a andarem juntos (Aula 01).
</details>

---

### 5. Múltipla escolha (oa02)
Um intérprete de sísmica de reservatório mede, num intervalo carbonático, uma razão Vp/Vs de exatamente 1,73. Qual é a leitura correta desse valor?

a) 1,73 confirma a litologia carbonática, porque está dentro da faixa esperada de calcário e dolomito saturados de água (1,8-1,9)
b) 1,73 corresponde a um coeficiente de Poisson de 0,25 (o "sólido de Poisson"), valor característico de arenito limpo consolidado ou de granito — encontrá-lo num intervalo suposto carbonático é motivo para desconfiar da litologia atribuída
c) 1,73 é impossível fisicamente, pois nenhuma rocha real produz essa razão exata
d) 1,73 indica necessariamente saturação por gás, independentemente da litologia

<details><summary>Ver resposta</summary>

**Resposta: b** — Vp/Vs = √3 ≈ 1,73 corresponde a coeficiente de Poisson de exatamente 0,25, o valor teórico do "sólido de Poisson", característico de arenito limpo consolidado e de granito, não de carbonato saturado (cuja faixa típica é 1,8-1,9). A alternativa a comete exatamente o erro que a aula corrige: tratar 1,73 como se fosse carbonático. A alternativa c está errada porque 1,73 é um valor fisicamente comum, só que de outra litologia. A alternativa d generaliza demais — Vp/Vs cai com a presença de gás, mas 1,73 não é, por si só, prova de saturação por gás; é primariamente um indicador de litologia (Aula 02).
</details>

---

### 6. Aplicação (cálculo, oa02)
Um arenito consolidado saturado de água tem densidade bulk de 2.320 kg/m³, módulo de compressibilidade K = 18 GPa e módulo de cisalhamento G = 12 GPa. Calcule Vp, Vs e a razão Vp/Vs, e diga se o resultado é consistente com a litologia declarada (arenito) ou levantaria suspeita de erro de atribuição litológica.

<details><summary>Ver resolução</summary>

ρ = 2.320 kg/m³, K = 18 × 10⁹ Pa, G = 12 × 10⁹ Pa.

Vp = √[(K + 4G/3) / ρ] = √[(18×10⁹ + 16×10⁹) / 2.320] = √[34×10⁹ / 2.320] = √(1,466×10⁷) ≈ **3.828 m/s ≈ 3,83 km/s**

Vs = √(G / ρ) = √(12×10⁹ / 2.320) = √(5,172×10⁶) ≈ **2.274 m/s ≈ 2,27 km/s**

Vp/Vs = 3.828 / 2.274 ≈ **1,68**

O resultado é **consistente** com a litologia declarada: Vp de 3,83 km/s está dentro da faixa ampla de arenitos (1,5-5 km/s), e Vp/Vs de 1,68 está dentro dos 1,6-1,8 típicos de arenito limpo — bem abaixo dos 1,8-1,9 de carbonato, então não há motivo para suspeitar de erro de atribuição aqui (ao contrário do caso-limite de 1,73 discutido na aula, que fica na fronteira ambígua) (Aula 02).
</details>

---

### 7. Verdadeiro ou Falso (oa02)
"A densidade do basalto é sempre maior que a do granito porque o basalto é rico em olivina, mineral ferromagnesiano denso que está presente em toda rocha basáltica."

<details><summary>Ver resposta</summary>

**Falso.** O contraste de densidade entre basalto e granito se explica inteiramente **sem invocar olivina**: a troca de quartzo (2,65 g/cm³) e feldspato alcalino (~2,56 g/cm³), abundantes no granito, por plagioclásio cálcico (~2,76 g/cm³), clinopiroxênio (3,2-3,4 g/cm³) e óxidos de Fe-Ti como a magnetita (5,2 g/cm³) já é suficiente. A olivina (3,3-4,4 g/cm³) só é fase essencial nas variedades **olivínicas** e nos picritos — generalizá-la como presente em "toda rocha basáltica" contraria a petrologia ígnea básica (Aula 02).
</details>

---

### 8. Dissertativa curta (oa02)
Explique por que, ao trocar o fluido de poro de uma rocha porosa de água para gás (mantendo a mesma porosidade e o mesmo arcabouço sólido), a velocidade Vs permanece praticamente inalterada enquanto Vp diminui perceptivelmente. Que aplicação prática de sísmica de reservatório se apoia diretamente nesse padrão?

<details><summary>Ver resposta comentada</summary>

**Resposta esperada:** Vs = √(G/ρ) depende exclusivamente do módulo de cisalhamento G, e fluidos (água ou gás) têm módulo de cisalhamento praticamente nulo em ambos os casos — trocar um pelo outro não muda como o arcabouço sólido resiste ao cisalhamento, então **Vs não muda de forma relevante**. Já Vp = √[(K + 4G/3)/ρ] depende também do módulo de compressibilidade K, e o gás é muito mais compressível que a água — o K efetivo da rocha saturada **cai** quando o fluido passa de água para gás, reduzindo Vp. Como Vp cai e Vs permanece estável, a **razão Vp/Vs também cai**. Esse padrão (Vs estável, Vp e Vp/Vs caindo com a presença de gás) é exatamente o que um intérprete de sísmica de reservatório usa para identificar **contatos gás-água** a partir de anomalias de amplitude sísmica, o fenômeno popularmente chamado de "bright spot" (Aula 02).
</details>

---

### 9. Múltipla escolha (oa03)
Entre os minerais a seguir, qual par corresponde aos contribuintes **ferrimagnéticos** (fortemente magnéticos) mais relevantes para a susceptibilidade magnética da maioria das rochas comuns, depois da magnetita?

a) Ilmenita e hematita
b) Olivina e hematita
c) Titanomagnetita e pirrotita monoclínica
d) Ilmenita e olivina

<details><summary>Ver resposta</summary>

**Resposta: c** — depois da magnetita, os contribuintes ferrimagnéticos que de fato importam são as titanomagnetitas (série magnetita–ulvöspinélio), a maghemita e a pirrotita monoclínica (Fe₇S₈). A ilmenita (FeTiO₃) é **paramagnética** em qualquer condição geológica (sua temperatura de Néel fica em torno de 57 K, muito abaixo de qualquer ambiente terrestre de superfície ou subsuperfície rasa) — é exatamente por isso que um granito de série ilmenita é fracamente magnético. A hematita é apenas fracamente magnética, por antiferromagnetismo inclinado (*canted*), cerca de três ordens de grandeza menos suscetível que a magnetita. A olivina é paramagnética, não ferrimagnética. As alternativas a, b e d combinam pelo menos um mineral paramagnético como se fosse ferrimagnético — o erro clássico do assunto (Aula 03).
</details>

---

### 10. Verdadeiro ou Falso (oa03)
"Formações ferríferas bandadas (BIF) são sempre fortemente magnéticas, porque a hematita, um dos óxidos de ferro que as compõe, é fortemente magnética como a magnetita."

<details><summary>Ver resposta</summary>

**Falso.** A hematita **não** é fortemente magnética: seu momento magnético líquido vem de um antiferromagnetismo levemente inclinado (*canted*), cerca de três ordens de grandeza mais fraco que o ferrimagnetismo da magnetita. Formações ferríferas bandadas são fortemente magnéticas **apenas** nas fácies e itabiritos ricos em **magnetita** — o itabirito e o minério hematíticos, apesar do teor de ferro igual ou maior, são apenas **fracamente magnéticos**. É exatamente essa diferença que permite separar as duas fácies em levantamento magnético, um critério operacional de uso corrente na exploração do Quadrilátero Ferrífero. "Rico em óxido de ferro" não implica "fortemente magnético" (Aula 03).
</details>

---

### 11. Aplicação (raciocínio, oa03)
Dois plútons graníticos adjacentes têm composição química quase idêntica, mas cristalizaram sob condições redox diferentes: o Plúton A cristalizou magnetita como óxido acessório (granito de série magnetita); o Plúton B, sob condições mais redutoras, cristalizou ilmenita no lugar da magnetita (granito de série ilmenita), sem magnetita detectável. Um levantamento aeromagnético sobrevoa os dois. Preveja o padrão de anomalia esperado sobre cada plúton e justifique com o comportamento magnético de cada mineral.

<details><summary>Ver resolução</summary>

O **Plúton A** (série magnetita) deve produzir uma anomalia magnética de **alta amplitude**: a magnetita (Fe₃O₄) é ferrimagnética, com susceptibilidade ordens de grandeza maior que a de qualquer silicato paramagnético, e domina a resposta magnética da rocha mesmo em concentração acessória (menos de 1% em volume).

O **Plúton B** (série ilmenita) deve aparecer como uma anomalia de **baixa amplitude ou praticamente ausente**: a ilmenita (FeTiO₃) é **paramagnética** em qualquer condição geológica (temperatura de Néel ≈ 57 K, muito abaixo do ambiente terrestre), de modo que, na ausência de magnetita, a rocha não tem um contribuinte ferrimagnético relevante — só a resposta fraca e difusa dos silicatos paramagnéticos e da própria ilmenita.

O contraste entre os dois plútons é exatamente o mecanismo por trás da distinção de Ishihara (série magnetita vs. série ilmenita, que reflete o estado de oxidação do magma) e é o tipo de padrão que um levantamento aeromagnético (Módulo 16) usa para mapear, sem amostragem direta, a variação composicional e redox dentro de um mesmo corpo granítico (Aula 03).
</details>

---

### 12. Aplicação (cálculo, oa03)
Um levantamento aerogamaespectrométrico sobre duas áreas registra: Área A — K = 3,0%, eU = 2 ppm, eTh = 16 ppm; Área B — K = 1,2%, eU = 9 ppm, eTh = 4,5 ppm. Calcule a razão Th/U de cada área e, usando a régua da IAEA (Th/U ≈ 2 a 7 como faixa de rocha não alterada), classifique o processo geológico provável em cada uma.

<details><summary>Ver resolução</summary>

Área A: Th/U = 16 / 2 = **8**

Área B: Th/U = 4,5 / 9 = **0,5**

**Área A (Th/U = 8):** está **acima** do limite superior da faixa normal (7), o que sugere **lixiviação de urânio por intemperismo oxidante** — o tório é geoquimicamente mais imóvel que o urânio e fica retido enquanto o urânio é removido em solução, elevando a razão Th/U acima do padrão de rocha fresca (compare com o exemplo da aula, em que um granito **fresco** dava Th/U = 4,5, dentro da faixa normal — a diferença de processo está exatamente em cruzar o limiar de 7).

**Área B (Th/U = 0,5):** está bem **abaixo** do limite inferior (2), o que sugere **enriquecimento de urânio em ambiente redutor** — a assinatura clássica de folhelho negro rico em matéria orgânica, onde o ambiente redutor favorece a precipitação e retenção do urânio (insolúvel em condições redutoras) sem afetar o tório da mesma forma.

Nos dois casos, é a razão Th/U comparada contra a régua da IAEA — não o valor absoluto isolado de nenhum canal — que carrega a informação diagnóstica sobre o processo geológico (Aula 03).
</details>

---

### 13. Dissertativa curta (oa03)
Explique a frase "duas séries de decaimento e um isótopo isolado" aplicada à radioatividade natural das rochas. Por que o potássio é reportado em % de massa direto, enquanto urânio e tório são reportados como ppm equivalente (eU, eTh)? E por que o canal de urânio é, dos três, o menos confiável?

<details><summary>Ver resposta comentada</summary>

**Resposta esperada:** urânio e tório decaem através de longas **séries** (cadeias sucessivas de emissão alfa e beta até um isótopo estável de chumbo) — são **duas séries**. O ⁴⁰K, ao contrário, decai **diretamente**, sem cadeia: cerca de 89% por emissão β⁻ para ⁴⁰Ca e cerca de 11% por captura eletrônica para ⁴⁰Ar, ramo que emite o gama de 1,46 MeV — é **um isótopo isolado**, não uma terceira série.

A diferença de unidade vem exatamente dessa assimetria: o fóton de 1,46 MeV medido para o potássio vem do **próprio** ⁴⁰K, então K é reportado direto, em % de massa. U e Th, porém, praticamente não emitem gama úteis eles próprios — o detector registra fótons de **produtos-filhos** bem abaixo na cadeia (²¹⁴Bi em 1,76 MeV para a série do U; ²⁰⁸Tl em 2,61 MeV para a série do Th). Como a medida é do filho e não do pai, o resultado é reportado como ppm **equivalente** (eU, eTh) — o "equivalente" é a admissão honesta dessa indireção, e converter a contagem do filho na concentração do pai pressupõe **equilíbrio secular** ao longo da cadeia.

O canal de urânio é o menos confiável porque um dos membros intermediários da sua cadeia é o **radônio (²²²Rn)**, um gás que **escapa** da rocha — isso rompe o equilíbrio secular com frequência, fazendo a leitura de eU subestimar ou distorcer o urânio real presente, uma fragilidade que a série do tório não compartilha (Aula 03).
</details>

---

### 14. Aplicação (cálculo, oa04)
Um intervalo-reservatório tem porosidade φ = 0,18 e resistividade da água de formação Rw = 0,06 ohm·m. A resistividade profunda medida é Rt = 9 ohm·m. Calcule a saturação de água Sw usando (a) a fórmula de Humble corretamente pareada (a = 0,62 com m = 2,15) e (b) o erro comum de combinar a = 0,62 com m = 2 (do par "de Archie"). Compare os dois resultados e explique por que o erro (b) é perigoso mesmo parecendo plausível.

<details><summary>Ver resolução</summary>

**(a) Par correto (Humble: a = 0,62, m = 2,15):**

φ^m = 0,18^2,15 ≈ 0,0250. F = a/φ^m = 0,62 / 0,0250 ≈ **24,8**.

R₀ = F × Rw = 24,8 × 0,06 ≈ **1,49 ohm·m**.

Sw = (F × Rw / Rt)^(1/n), com n = 2: Sw = (1,49 / 9)^(1/2) = (0,1655)^(1/2) ≈ **0,406 → 40,6%**.

**(b) Combinação errada (a = 0,62 com m = 2):**

φ^m = 0,18² = 0,0324. F = 0,62 / 0,0324 ≈ **19,1**.

R₀ = 19,1 × 0,06 ≈ **1,15 ohm·m**.

Sw = (1,15 / 9)^(1/2) = (0,1276)^(1/2) ≈ **0,357 → 35,7%**.

**Comparação:** o par correto dá Sw ≈ 40,6%; a combinação errada dá Sw ≈ 35,7% — uma diferença de quase 5 pontos percentuais, **e o resultado errado continua sendo um número plausível**, dentro de faixas normais de saturação. Isso é exatamente o que torna o erro perigoso: **a** e **m** não são botões independentes, vêm em pares calibrados sobre o mesmo conjunto de amostras (a forma "de Archie" usa a = 1 com m entre 1,8 e 2,0; a fórmula de Humble usa a = 0,62 **com** m = 2,15), e misturar o **a** de um par com o **m** de outro produz um fator de formação simplesmente errado — não uma média prudente —, sem qualquer sinal de alerta no resultado final (Aula 04).
</details>

---

### 15. Verdadeiro ou Falso (oa04)
"O expoente de saturação n pode ser assumido como 2 em qualquer rocha, water-wet ou oil-wet, pois a equação de Archie foi calibrada de forma a cobrir igualmente as duas condições de molhabilidade."

<details><summary>Ver resposta</summary>

**Falso.** Archie mediu especificamente em condição **water-wet** (molhável por água), e é só nessa condição que n ≈ 2 é uma aproximação razoável — medidas clássicas (Sweeney & Jennings) dão n ≈ 1,6 em rocha water-wet, ≈ 1,9 em molhabilidade neutra e ≈ **8** (podendo passar de 10) em rocha **oil-wet**. O mecanismo físico é que, numa rocha water-wet, a água permanece como filme contínuo na parede do poro e continua conduzindo mesmo com pouca água; numa rocha oil-wet, esse filme se rompe em gotas desconectadas, e a condução despenca. Boa parte dos carbonatos é de molhabilidade mista ou oil-wet — herdar n = 2 nesse caso não é imprecisão pequena: com os mesmos dados de resistividade, n = 2 pode dar Sw ≈ 37% enquanto n = 8 dá Sw ≈ 78% — assumir n = 2 numa rocha oil-wet **subestima** a saturação de água e **superestima** o hidrocarboneto, o erro na direção mais perigosa possível para uma decisão de perfurar (Aula 04).
</details>

---

### 16. Aplicação (síntese, integração a01→a04, oa04)
Um arenito limpo (predominantemente quartzoso) tem porosidade φ = 20% (0,20), medida por perfil de densidade-nêutron. Saturado com água (densidade do fluido ρ_fluido = 1,00 g/cm³) e com densidade de matriz de quartzo ρ_matriz = 2,65 g/cm³, calcule:

(a) a densidade bulk da rocha;
(b) Vp, Vs e a razão Vp/Vs, sabendo que essa rocha tem módulo de compressibilidade K = 18 GPa e módulo de cisalhamento G = 12 GPa, e diga se o resultado é consistente com a litologia declarada;
(c) qualitativamente, que assinatura magnética e radiométrica você esperaria de um arenito quartzoso limpo como esse, e por quê;
(d) a saturação de água Sw pela lei de Archie, sabendo que a resistividade da água de formação é Rw = 0,03 ohm·m, a resistividade profunda medida é Rt = 15 ohm·m, e usando os parâmetros-padrão de arenito limpo (a = 1, m = 2, n = 2).

<details><summary>Ver resolução</summary>

**(a) Densidade bulk (Aula 02):**

ρ_b = (1 − φ) × ρ_matriz + φ × ρ_fluido = 0,80 × 2,65 + 0,20 × 1,00 = 2,12 + 0,20 = **2,32 g/cm³**

Valor dentro da faixa típica de arenitos (2,0-2,6 g/cm³), consistente com um arenito de porosidade moderada.

**(b) Vp, Vs e Vp/Vs (Aula 02):**

Em unidades SI: ρ = 2.320 kg/m³, K = 18×10⁹ Pa, G = 12×10⁹ Pa.

Vp = √[(K + 4G/3)/ρ] = √[(18×10⁹ + 16×10⁹)/2.320] = √(1,466×10⁷) ≈ **3.828 m/s ≈ 3,83 km/s**

Vs = √(G/ρ) = √(12×10⁹/2.320) = √(5,172×10⁶) ≈ **2.274 m/s ≈ 2,27 km/s**

Vp/Vs = 3.828/2.274 ≈ **1,68**

Vp de 3,83 km/s cai dentro da faixa ampla de arenitos (1,5-5 km/s), e Vp/Vs de 1,68 está dentro dos 1,6-1,8 de arenito limpo — **consistente** com a litologia declarada, bem distante da faixa de carbonato (1,8-1,9) e longe do caso-limite ambíguo de 1,73.

**(c) Assinatura magnética e radiométrica esperada (Aula 03):**

Um arenito quartzoso **limpo** deve ser **fracamente magnético**: o quartzo é diamagnético, e um arenito limpo tem pouco ou nenhum mineral ferrimagnético acessório (magnetita, titanomagnetita) — a menos que contenha magnetita detrítica, que não é o caso de um arenito quartzoso puro. Radiometricamente, deve ser **"frio"**: quartzo não incorpora K, U nem Th em quantidade relevante, então os três canais (K, eU, eTh) tendem a valores baixos, salvo contaminação por argila (que elevaria K) ou por fosfato/matéria orgânica (que elevaria U) — nenhuma das quais está presente num arenito quartzoso limpo como o descrito.

**(d) Saturação de água por Archie (Aula 04):**

F = a/φ^m = 1/(0,20)² = 1/0,04 = **25**

R₀ = F × Rw = 25 × 0,03 = **0,75 ohm·m**

Sw = (F × Rw/Rt)^(1/n) = (25 × 0,03/15)^(1/2) = (0,75/15)^(1/2) = (0,05)^(1/2) ≈ **0,224 → 22,4%**

Sh = 1 − Sw ≈ **77,6%**

**Síntese:** a mesma rocha — um arenito limpo de porosidade 20% — produz, ao longo das quatro aulas do módulo, uma cadeia de contrastes físicos coerentes entre si: densidade moderada (2,32 g/cm³) e velocidade sísmica na faixa esperada de arenito (Vp/Vs = 1,68, não confundível com carbonato); ausência de assinatura magnética ou radiométrica forte (rocha "fria" e fracamente magnética, porque o quartzo não hospeda K, U, Th nem magnetita); e, pela resistividade, uma saturação de água baixa (22,4%) que classificaria o intervalo como candidato a reservatório de hidrocarboneto (Sh ≈ 78%). É exatamente essa cadeia — porosidade → densidade/velocidade → magnetismo/radioatividade → condutividade — que justifica por que a petrofísica é a base sobre a qual o Módulo 16 (aerogeofísica) constrói a interpretação de contrastes físicos medidos a distância (Aulas 01, 02, 03 e 04).
</details>

---

### Gabarito resumido

| Questão | Resposta |
|---|---|
| 1 | b |
| 2 | Falso |
| 3 | φ_total=25%, φ_efetiva=20%, isolada=5 p.p., superestimativa=25% |
| 4 | ver comentário |
| 5 | b |
| 6 | Vp≈3,83 km/s; Vs≈2,27 km/s; Vp/Vs≈1,68; consistente com arenito |
| 7 | Falso |
| 8 | ver comentário |
| 9 | c |
| 10 | Falso |
| 11 | ver comentário |
| 12 | Th/U(A)=8 → lixiviação oxidante; Th/U(B)=0,5 → enriquecimento redutor (folhelho negro) |
| 13 | ver comentário |
| 14 | Sw correto≈40,6%; Sw errado≈35,7% |
| 15 | Falso |
| 16 | ρ_b=2,32 g/cm³; Vp≈3,83 km/s; Vs≈2,27 km/s; Vp/Vs≈1,68; fracamente magnético e "frio"; Sw≈22,4%, Sh≈77,6% |

## Cobertura de objetivos confirmada
- geologia-avancado-m15-oa01 — questões 1, 2, 3, 4
- geologia-avancado-m15-oa02 — questões 5, 6, 7, 8
- geologia-avancado-m15-oa03 — questões 9, 10, 11, 12, 13
- geologia-avancado-m15-oa04 — questões 14, 15, 16

## Notas de rastreabilidade
- Achado `DID-M15-OA03-AMPLITUDE-008` (revisão didática) atendido: oa03 recebeu 5 das 16 questões (mais que os 4 dos demais objetivos), e das cinco, três (9, 10, 11) cobrem especificamente a metade **magnética** do objetivo, que na Aula 03 não tinha nenhum exemplo trabalhado numérico — a questão 11 constrói um exercício de raciocínio inédito (dois plútons, série magnetita vs. série ilmenita) para preencher exatamente essa lacuna.
- Achado `DID-M15-INTEGRACAO-007` (revisão didática) atendido: nenhum exemplo trabalhado das quatro aulas atravessa o módulo — a questão 16 fecha essa lacuna com uma cadeia de síntese sobre uma única rocha (arenito limpo), percorrendo porosidade (a01) → densidade bulk e Vp/Vs (a02) → assinatura magnética/radiométrica qualitativa (a03) → Sw por Archie (a04), com todas as fórmulas já entregues pelo módulo e nenhum fato novo introduzido.
- Nenhum achado de auditoria em aberto foi reproduzido como afirmação de gabarito. Ao contrário, os pontos corrigidos pela auditoria foram usados deliberadamente como **distratores**, conforme os `generator_warnings` do `course-state.yaml`: Vp/Vs = 1,73 como valor de arenito/granito, não de carbonato (questões 5 e 6); ilmenita como paramagnética, nunca listada como fonte de magnetismo (questão 9, distrator "ilmenita e hematita"/"ilmenita e olivina"); hematita como fracamente magnética mesmo em BIF (questão 10); razão Th/U contra a régua da IAEA em vez de adjetivo solto — a questão 12 usa números **diferentes** dos da aula (Th/U = 8 e 0,5, em vez de 4,5 e 0,5) para testar se o aluno aplica a régua, não decorou o resultado; pareamento a/m de Archie com o erro comum (a=0,62 com m=2) quantificado lado a lado com o par correto (questão 14); expoente n dependente de molhabilidade, com a direção do erro (superestima hidrocarboneto) explicitada (questão 15).
- Nenhum achado branco (dolomitização, densidade de grão 2,85 vs. 2,87) foi transformado em questão de gabarito fechado, conforme a advertência do relatório de auditoria — a porosidade secundária por dolomitização segue sem entrar no questionário como fato de resposta única.
- Cinco das 16 questões são de cálculo numérico com valores próprios, não copiados dos exemplos trabalhados das aulas (questões 3, 6, 12, 14, 16), o que exige que o aluno aplique a fórmula em vez de reconhecer o número: porosidade (Aula 01: 60/45/12 cm³, distinto de 50/38/9), Vp/Vs (Aula 02: K=18/G=12, distinto de K=40/G=19), Th/U (Aula 03: K=3,0%/1,2%, distinto de 4,2%/1,8%), Archie a/m (Aula 04: φ=0,18/Rw=0,06/Rt=9, distinto de φ=0,22/Rw=0,08/Rt=12) e a síntese da questão 16 (φ=0,20/K=18/G=12/Rw=0,03/Rt=15, combinação nova que não repete nenhum dos exemplos das aulas mas reutiliza as mesmas fórmulas).
- Mapeamento 1:1 objetivo-aula do módulo (único no curso com essa propriedade, conforme a revisão didática) preservado no questionário: cada bloco de questões de um objetivo se apoia primariamente na aula correspondente, com a questão 16 sendo a exceção deliberada que atravessa as quatro.
