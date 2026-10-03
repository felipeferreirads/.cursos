# Questionário parcial 1 — Módulo 27: Introdução à petrocronologia

**Módulo:** [[27-petrocronologia-modulo|Módulo 27 — Introdução à petrocronologia]]
**Cobertura:** Aulas 01 a 03 — o que distingue a petrocronologia da geocronologia convencional; por que um único cristal pode conter mais de um domínio de crescimento; a temperatura de fechamento como propriedade da combinação mineral+sistema; e as técnicas analíticas e de imageamento (LA-ICP-MS, SIMS, TIMS, EPMA, MEV).
**Recorte:** do conceito de "idade significante" à escolha da técnica que a mede. A parcial 1 testa se você sabe explicar por que uma idade isotópica isolada não é uma conclusão geológica, reconhecer a hierarquia de temperaturas de fechamento entre minerais e sistemas, e decidir qual técnica analítica resolve espacialmente o domínio que a textura manda datar.
**Objetivos avaliados:** `geologia-avancado-m27-oa01` (integral — Aulas 01 e 02), `geologia-avancado-m27-oa02` (integral — Aula 03)
**Pontuação total:** 100 pontos · o gabarito fica oculto; responda antes de abrir.

---

### 1. Múltipla escolha — `geologia-avancado-m27-q01` · oa01 · 8 pts

Um laboratório devolve "monazita desta amostra, 480 ± 4 Ma". Segundo a distinção que a Aula 01 estabelece entre geocronologia e petrocronologia, o que falta a esse resultado para se tornar uma "idade significante" (no sentido de Engi, Lanari & Kohn, 2017)?

- a) Nada falta: uma idade isotópica com erro analítico pequeno já é, por definição, geologicamente significativa
- b) Falta repetir a análise em duplicata para confirmar a reprodutibilidade instrumental
- c) Falta amarrar o número a um domínio específico do cristal (posição microestrutural e composição química), identificando a que evento ou reação aquele domínio corresponde
- d) Falta converter a idade para uma escala de tempo relativa, já que idades absolutas não têm uso petrológico

<details>
<summary>Ver resposta</summary>

**Resposta: c**

A geocronologia responde "quando"; a petrocronologia pergunta "quando, em relação a quê" — integra a idade com textura, composição e condições P-T para dar a ela um significado petrogenético específico. Uma idade "significante" não é a de menor erro analítico, é a que está inequivocamente amarrada a um processo (Aula 01). "a" confunde precisão analítica com significado geológico — os dois são independentes. "b" descreve controle de qualidade instrumental, não o problema conceitual que a aula levanta. "d" inverte a lógica: a petrocronologia não abandona a idade absoluta, ela a torna interpretável.
</details>

---

### 2. Verdadeiro ou Falso (justifique) — `geologia-avancado-m27-q02` · oa01 · 10 pts

"Se um laboratório dissolve um grão de zircão inteiro (sem separar núcleo de borda) e mede uma razão isotópica em bloco, o resultado é uma média que corresponde à idade do evento geológico mais antigo registrado naquele grão."

<details>
<summary>Ver resposta</summary>

**Falso.**

A Aula 01 é explícita: se o grão tem mais de um domínio de crescimento (por exemplo, um núcleo magmático e uma borda metamórfica), dissolver o cristal inteiro produz uma **média ponderada** desses domínios — proporcional, grosseiramente, à massa de cada domínio dissolvida —, e essa média **não corresponde à idade de nenhum evento geológico real**, nem o mais antigo, nem o mais novo, nem qualquer ponto intermediário com existência própria. É um artefato de mistura, não uma idade de evento algum. É exatamente esse problema que motiva a análise **in situ**, dentro de domínios específicos identificados por imageamento (Aula 03), como fio condutor de todo o módulo.
</details>

---

### 3. Múltipla escolha — `geologia-avancado-m27-q03` · oa01 · 8 pts

Sobre o uso da razão Th/U do zircão como indicador de origem magmática ou metamórfica, qual afirmação é a mais fiel ao que a Aula 01 ensina?

- a) Th/U acima de ~0,1 é uma prova definitiva de origem magmática, e Th/U abaixo desse valor é uma prova definitiva de origem metamórfica, sem exceção
- b) Th/U é uma tendência útil, a ser cruzada com a textura, não um critério isolado e definitivo — rochas de alto grau pobres em monazita, por exemplo, podem produzir zircão metamórfico com Th/U elevado
- c) A razão Th/U não tem nenhuma relação com a origem do zircão, e só serve para calcular idades U-Pb
- d) Th/U é definitiva apenas em zircões ígneos, mas não pode ser medida em zircões metamórficos por nenhuma técnica

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A Aula 01 é explícita ao chamar Th/U de "tendência útil, não uma lei rígida": zircão magmático tende a Th/U mais alto (grosseiramente acima de ~0,1, frequentemente 0,5-1 ou mais) e zircão metamórfico tende a Th/U mais baixo, mas há exceções documentadas em ambas as direções, especialmente em rochas de alto grau pobres em monazita. "a" transforma uma tendência em prova absoluta, o erro exato que a aula adverte contra. "c" e "d" são falsos quanto ao fato mineralógico: Th/U se mede rotineiramente em zircões de qualquer origem, e carrega, sim, informação sobre o processo de formação.
</details>

---

### 4. Aplicação — `geologia-avancado-m27-q04` · oa01 · 14 pts

Uma amostra de gnaisse migmatítico contém zircões com dois domínios distintos por imageamento CL: (1) um domínio interno com zoneamento oscilatório concêntrico e Th/U ≈ 0,60, datado em 720 ± 6 Ma; (2) um domínio externo, sem zoneamento, texturalmente truncando o domínio interno, com Th/U ≈ 0,02, datado em 650 ± 7 Ma.

(a) Com base apenas na textura e na composição (sem nenhum outro dado), qual é a leitura petrocronológica mais provável de cada domínio? (b) O que mudaria na sua interpretação se, em vez de "truncando", a relação textural descrita fosse "o domínio externo segue o mesmo padrão de zoneamento do domínio interno, sem descontinuidade"?

<details>
<summary>Ver resposta</summary>

**(a)** O domínio interno — zoneamento oscilatório concêntrico e Th/U alto (0,60) — tem a assinatura típica de crescimento magmático (Aula 01: zoneamento oscilatório + Th/U tipicamente acima de ~0,1, aqui bem acima): 720 Ma provavelmente data a cristalização de um protólito ígneo. O domínio externo — sem zoneamento, com Th/U baixo (0,02) e truncando o domínio anterior (uma relação de corte que só o imageamento revela) — tem a assinatura típica de recristalização metamórfica: 650 Ma provavelmente data um evento metamórfico posterior, 70 milhões de anos depois da cristalização ígnea, consistente com o próprio exemplo da Aula 01.

**(b)** Se o domínio externo continuasse o mesmo padrão de zoneamento oscilatório sem descontinuidade textural, a leitura mudaria substancialmente: a ausência de uma relação de corte sugere que não há evidência textural de um evento de crescimento distinto, e a queda de Th/U de 0,60 para 0,02 sem mudança textural seria, no mínimo, difícil de conciliar com um único evento de cristalização magmática contínua — a composição sozinha (Th/U) não decide a origem sem o apoio da textura, e a Aula 01 insiste que ancorar uma idade exige as duas linhas de evidência, não uma isolada. Diante dessa contradição, a leitura mais cautelosa seria suspeitar de um artefato analítico (por exemplo, um spot que atravessou dois domínios) ou buscar uma imagem CL de resolução melhor antes de aceitar qualquer interpretação.
</details>

---

### 5. Dissertativa curta — `geologia-avancado-m27-q05` · oa01 · 10 pts

Explique a diferença entre petrocronologia e termocronologia, e por que essa distinção importa para decidir o que uma idade isotópica está de fato registrando.

<details>
<summary>Ver resposta</summary>

A termocronologia foca especificamente em taxas de resfriamento, usando a temperatura de fechamento de sistemas isotópicos (conceito de Dodson, 1973) para reconstruir quando uma rocha esfriou abaixo de certos patamares térmicos durante seu soerguimento e exumação — é, essencialmente, uma ferramenta de história térmica pós-pico. A petrocronologia é mais ampla: pode registrar resfriamento quando o cronômetro usado tem baixa temperatura de fechamento, mas seu objetivo central é vincular idades a **eventos de crescimento mineral específicos**, muitas vezes em alta temperatura, onde a temperatura de fechamento sequer é o fator limitante — o que importa ali é a reação que fez o mineral crescer. A distinção importa porque, sem ela, um leitor pode presumir que toda idade isotópica é uma "idade de resfriamento" e tentar encaixá-la numa taxa de exumação, quando na verdade ela pode estar datando a cristalização de um mineral num evento de alta temperatura (como o zircão e a monazita, discutidos com detalhe nas Aulas 02 e 06) — duas leituras geológicas completamente diferentes do mesmo número.
</details>

---

### 6. Múltipla escolha — `geologia-avancado-m27-q06` · oa01 · 8 pts

Por que a Aula 02 trata a temperatura de fechamento como uma propriedade da combinação **mineral + sistema isotópico**, e não do sistema isotópico isoladamente?

- a) Porque a temperatura de fechamento é, na verdade, uma constante universal, e a ressalva sobre o mineral hospedeiro é apenas uma simplificação didática sem consequência prática
- b) Porque minerais diferentes retêm o filho radiogênico de forma diferente mesmo para o mesmo sistema isotópico — é a difusão do elemento filho no retículo cristalino do mineral hospedeiro que define quando o sistema "fecha", não o sistema isotópico por si só
- c) Porque cada sistema isotópico (U-Pb, Sm-Nd etc.) tem uma única temperatura de fechamento válida para qualquer mineral que o hospede, e a variação observada na prática é apenas erro analítico
- d) Porque a temperatura de fechamento depende exclusivamente da concentração do elemento-pai no mineral, não da estrutura cristalina

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A Aula 02 é explícita: a temperatura de fechamento de Dodson é a temperatura em que a difusão do elemento filho no retículo cristalino do mineral hospedeiro se torna lenta o bastante para não escapar em tempo geológico — e minerais diferentes retêm o mesmo elemento filho de forma diferente. É exatamente por isso que zircão e monazita (U-Pb) praticamente não fecham por difusão em condições crustais comuns, enquanto apatita (também U-Pb) fecha numa temperatura bem mais baixa: a diferença está no mineral hospedeiro, não no sistema isotópico. "a", "c" e "d" tratam a temperatura de fechamento como algo fixo ou determinado por um único fator, contrariando o próprio conceito de Dodson que a aula apresenta.
</details>

---

### 7. Verdadeiro ou Falso (justifique) — `geologia-avancado-m27-q07` · oa01 · 10 pts

"Quando os sistemas Lu-Hf e Sm-Nd são medidos na mesma granada zonada e dão idades diferentes, isso normalmente indica um erro analítico em um dos dois sistemas."

<details>
<summary>Ver resposta</summary>

**Falso.**

A Aula 02 trata essa diferença como **informação**, não como erro: a difusão de Hf na granada é suficientemente lenta para que a temperatura de fechamento do Lu-Hf seja, na prática, mais alta que a do Sm-Nd na mesma granada; além disso, o lutécio se concentra fortemente nas partes do cristal que crescem primeiro (o núcleo), enviesando a idade Lu-Hf para os estágios iniciais do crescimento, enquanto o Sm-Nd, menos concentrado no núcleo, tende a refletir uma média de um intervalo maior. Quando os dois sistemas dão idades diferentes no mesmo cristal, isso reflete a taxa de resfriamento e o quanto cada sistema resistiu à reabertura difusiva depois do crescimento — o mesmo raciocínio que a Aula 07 usa para estimar a duração de um evento de crescimento a partir da diferença entre as duas idades.
</details>

---

### 8. Aplicação — `geologia-avancado-m27-q08` · oa01 · 14 pts

Um granulito de alto grau foi datado por quatro combinações mineral-sistema: zircão U-Pb, 588 ± 4 Ma; monazita U-Pb, 585 ± 5 Ma; granada Lu-Hf, 580 ± 6 Ma; titanita U-Pb, 555 ± 5 Ma (com temperatura de cristalização estimada em ~660 °C pelo termômetro Zr-em-titanita). Um quinto mineral, uma mica, deveria fechar a sequência com uma idade mais jovem, registrando resfriamento numa temperatura mais baixa.

(a) Ordene as quatro idades já disponíveis do evento mais quente ao mais frio, interpretando o que cada uma provavelmente registra. (b) Para a quinta idade, qual mica você escolheria — biotita ou muscovita — sabendo que a rocha é um granulito, e por quê?

<details>
<summary>Ver resposta</summary>

**(a)** Zircão (588 Ma) e monazita (585 Ma), ambos praticamente livres de reabertura difusiva até temperaturas muito altas, registram — quase coincidentes dentro do erro — o evento de cristalização/recristalização metamórfica de alta temperatura, provavelmente próximo ao pico metamórfico. A granada por Lu-Hf (580 Ma), levemente mais jovem, é consistente com registrar preferencialmente o início do crescimento do cristal (o núcleo, mais rico em Lu), ligeiramente antes ou durante o mesmo evento de alta temperatura. A titanita (555 Ma, ~660 °C) já é sensivelmente mais jovem — mais de 30 milhões de anos depois do zircão — e, com fechamento em torno de 650-700 °C, provavelmente registra um ponto no resfriamento pós-pico.

**(b)** Biotita, não muscovita. A Aula 02 é explícita: num granulito, a **muscovita não é estável** — ela reage com o quartzo antes da fácies granulito ser atingida. Uma muscovita eventualmente encontrada nessa rocha seria retrógrada: teria crescido abaixo da sua própria temperatura de fechamento (~450-500 °C) e, portanto, dataria o seu **próprio crescimento**, não a passagem da rocha por essa temperatura durante o resfriamento — o que quebraria a lógica de "idade de resfriamento" que a sequência está construindo. A biotita, com fechamento mais baixo (~300-350 °C) e sendo mineralogicamente compatível com a paragênese de um granulito, fecha a sequência de forma consistente, como no exemplo da própria aula.
</details>

---

### 9. Múltipla escolha — `geologia-avancado-m27-q09` · oa02 · 8 pts

Sobre a comparação entre SIMS (SHRIMP) e LA-ICP-MS quanto à resolução espacial, qual afirmação está correta?

- a) O SIMS tem resolução lateral muito maior que o LA-ICP-MS, o que permite que um spot de SIMS resolva lateralmente uma borda metamórfica de poucos micrômetros que um spot de laser não conseguiria
- b) A vantagem do SIMS está no volume/profundidade amostrados (pit de ~1-3 μm de profundidade, muito menor que as dezenas de μm de LA-ICP-MS), não na resolução lateral: lateralmente, o pit do SIMS (~15-25 μm) é da mesma ordem de grandeza de um spot de laser; bordas mais finas que isso exigem perfil em profundidade num grão não polido
- c) SIMS e LA-ICP-MS têm exatamente a mesma resolução espacial em todas as dimensões, e a escolha entre os dois depende só do custo
- d) O LA-ICP-MS tem resolução lateral e de profundidade superiores ao SIMS em qualquer configuração, o que torna o SIMS obsoleto para petrocronologia

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A Aula 03 é explícita nesse ponto (inclusive citando-o como uma correção de auditoria científica): a vantagem central do SIMS é o volume amostrado, muito menor em **profundidade** — um pit típico de SHRIMP tem profundidade de ~1-3 μm contra dezenas de μm em LA-ICP-MS —, o que reduz o risco de o feixe atravessar, em profundidade, um domínio que não se vê na superfície. Lateralmente, porém, o pit do SIMS tem ~15-25 μm de diâmetro, a mesma ordem de grandeza de um spot de laser. Uma borda de poucos micrômetros de largura não cabe num spot de SIMS tanto quanto não cabe num de laser; a saída para bordas assim é o perfil em profundidade, montando o grão sem polir. "a" inverte exatamente essa distinção (lateral em vez de profundidade) — o erro que a própria auditoria científica do módulo identificou e corrigiu. "c" e "d" ignoram os tradeoffs reais entre as duas técnicas.
</details>

---

### 10. Aplicação — `geologia-avancado-m27-q10` · oa02 · 10 pts

Para cada problema abaixo, indique a técnica (ou sequência de técnicas) mais adequada entre LA-ICP-MS/LASS, SIMS, CA-ID-TIMS, EPMA e MEV, e justifique brevemente.

(a) Datar, com a máxima precisão absoluta possível, um único evento de cristalização magmática já bem delimitado por dados de campo, aceitando destruir o material analisado.
(b) Produzir um "mapa de idade" com centenas de pontos dentro de uma monazita com zoneamento composicional complexo de domínios muito finos.
(c) Decidir, antes de qualquer análise isotópica, onde posicionar os pontos de análise num zircão com núcleo e borda visíveis apenas por contraste de luminescência.

<details>
<summary>Ver resposta</summary>

**(a)** **CA-ID-TIMS**. É a técnica que entrega a maior precisão absoluta disponível (tipicamente 0,1% ou melhor), justamente porque o evento já está bem caracterizado e a resolução espacial fina não é o gargalo — o custo aceito é consumir (destruir) o material e abrir mão de qualquer resolução espacial no sentido in situ.

**(b)** **EPMA** (datação química de monazita). O spot de EPMA (~1-2 μm, podendo ser menor que 1 μm em instrumentos modernos) é cerca de dez vezes menor que um spot típico de SIMS e várias vezes menor que um de LA-ICP-MS, permitindo mapear zoneamento finíssimo em número grande de pontos; a baixa precisão de cada ponto individual (dezenas de Ma) é compensada agregando estatisticamente muitos pontos numa "idade de população" — SIMS e LA-ICP-MS não têm resolução espacial suficiente para esse número de domínios finos, e TIMS nem sequer é espacialmente resolvido.

**(c)** **MEV** (catodoluminescência, CL). O MEV não data nada, mas a CL é a técnica-padrão para revelar zoneamento oscilatório de zircão magmático e bordas metamórficas sem zoneamento; sem essa imagem prévia, apontar um feixe de SIMS ou LA-ICP-MS num zircão zonado é, na prática, um chute às cegas quanto a que domínio de crescimento está sendo amostrado. O fluxo padrão é sempre MEV primeiro, escolha dos pontos depois, e só então a análise isotópica pela técnica escolhida conforme o problema.
</details>

---

**Total: 100 pontos.**
