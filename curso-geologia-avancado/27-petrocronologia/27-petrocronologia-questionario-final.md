# Questionário final cumulativo — Módulo 27: Introdução à petrocronologia

**Módulo:** [[27-petrocronologia-modulo|Módulo 27 — Introdução à petrocronologia]]
**Cobertura:** o módulo inteiro — Aulas 01 a 07 (o que é petrocronologia e por que a idade precisa de âncora textural e composicional; sistemas isotópicos organizados por mineral hospedeiro e temperatura de fechamento; técnicas analíticas e de imageamento; texturas e trajetórias P-T; geotermobarometria; petrocronologia dos minerais acessórios via Y/HREE; granada e micas como cronômetros e integração de bancos de dados).
**Recorte:** integração, com peso deliberado nas conexões entre técnica, textura, composição e idade que nenhum parcial cobre sozinho. O módulo inteiro gira em torno da ordem textura → reação → condições P-T → idade: o final cumulativo testa se você consegue percorrer essa cadeia inteira num caso novo, do imageamento à duração de um evento metamórfico.
**Objetivos avaliados:** `geologia-avancado-m27-oa01`, `geologia-avancado-m27-oa02`, `geologia-avancado-m27-oa03`, `geologia-avancado-m27-oa04` (todos os quatro objetivos têm questões dedicadas ou integradas)
**Pontuação total:** 100 pontos · o gabarito fica oculto; responda antes de abrir.

---

### 21. Múltipla escolha — `geologia-avancado-m27-q21` · oa01 · 6 pts

Qual das opções resume corretamente o que significa, na prática, "ancorar uma idade em textura e em composição" (Aula 01)?

- a) Saber a posição microestrutural do domínio analisado (núcleo vs. borda, zoneamento, relações de corte) por imageamento, e usar a química do domínio (por exemplo, Th/U em zircão) como indicador — não prova isolada — do processo que o formou
- b) Confirmar que a análise isotópica foi feita em duplicata em dois laboratórios diferentes
- c) Garantir que a idade obtida seja sempre mais jovem que a idade de cristalização da rocha hospedeira
- d) Substituir a datação isotópica por uma estimativa de idade relativa baseada apenas em relações de campo, sem nenhuma análise em laboratório

<details>
<summary>Ver resposta</summary>

**Resposta: a**

Isso é textualmente o que a Aula 01 define como as duas âncoras de uma idade petrocronológica: textura (posição microestrutural, revelada por imageamento) e composição (química do domínio, como indicador de processo, nunca prova isolada e definitiva). "b" descreve controle de qualidade analítico, não o conceito de ancoragem petrológica. "c" inventa uma regra que não existe — a relação entre idade de um domínio e idade da rocha hospedeira depende do caso. "d" contraria o próprio programa do módulo, que integra idade isotópica com petrologia, não a substitui por ela.
</details>

---

### 22. Verdadeiro ou Falso (justifique) — `geologia-avancado-m27-q22` · oa01+oa02 · 8 pts

"Como o zircão praticamente não reabre por difusão térmica em condições crustais comuns, qualquer técnica analítica — LA-ICP-MS, SIMS ou TIMS — pode ser usada indistintamente para datar um zircão multi-domínio, porque o resultado sempre será o mesmo, independentemente da resolução espacial da técnica escolhida."

<details>
<summary>Ver resposta</summary>

**Falso.**

A estabilidade do sistema U-Pb do zircão contra reabertura por difusão (Aula 02) é uma coisa; a capacidade de uma técnica analítica de **isolar espacialmente** um domínio de crescimento específico dentro do grão é outra, completamente independente (Aula 03). Um zircão multi-domínio (núcleo herdado, sobrecrescimento magmático, borda metamórfica fina) exige uma técnica cuja resolução espacial (lateral ou em profundidade) seja compatível com o tamanho do domínio que se quer isolar — CA-ID-TIMS, por exemplo, dissolve o grão ou um fragmento dele sem conseguir isolar um domínio de poucos micrômetros, mesmo que o sistema isotópico em si nunca tenha sido reaberto por difusão. Ignorar a resolução espacial e escolher qualquer técnica "porque o zircão não reabre" reintroduz exatamente o problema de mistura de domínios que toda a Aula 01 existe para evitar.
</details>

---

### 23. Aplicação / Integração — `geologia-avancado-m27-q23` · oa02+oa03 · 12 pts

Uma amostra de gnaisse contém zircões com três domínios visíveis por imageamento CL: um núcleo herdado com zoneamento oscilatório antigo, um sobrecrescimento magmático mais recente também zonado, e uma borda metamórfica muito fina (poucos micrômetros), sem zoneamento, que poderia estar ligada a uma reação envolvendo granada. Você precisa (i) determinar a idade de cada um dos três domínios, preservando os grãos, e (ii) verificar se a borda cresceu em coexistência com granada ou depois da sua quebra.

Descreva o fluxo de trabalho completo, técnica por técnica, que resolve os dois objetivos.

<details>
<summary>Ver resposta</summary>

Primeiro, imageamento por MEV com catodoluminescência (CL) do grão inteiro, para mapear os três domínios e definir os limites entre eles (Aula 03) — sem essa etapa, qualquer escolha de ponto de análise seria um chute. Em seguida, para o núcleo herdado e o sobrecrescimento magmático — domínios largos o suficiente para um spot lateral —, usar SIMS (ou LA-ICP-MS de alta resolução espacial, se a largura permitir) para datar cada um separadamente na seção polida. Para a borda metamórfica fina, que não cabe lateralmente num spot de SIMS nem de laser (ambos da ordem de dezenas de μm), a saída é o **perfil em profundidade por SIMS** num grão irmão montado sem polir, com a face externa do cristal para cima — exatamente o Problema 2 do exemplo trabalhado da Aula 03, preservando os grãos para eventual reanálise (o que descarta CA-ID-TIMS, que destrói o material). Para o segundo objetivo — se a borda cresceu com granada presente ou depois de sua quebra —, é preciso medir, no mesmo domínio da borda (idealmente por LASS, que mede idade e composição no mesmo volume simultaneamente), o padrão de Y/HREE: um padrão de HREE achatado indica crescimento em coexistência com granada (competição pelo mesmo reservatório); um enriquecimento anormal de HREE sugere crescimento após a quebra da granada, quando o reservatório foi liberado (Aula 06).
</details>

---

### 24. Múltipla escolha — `geologia-avancado-m27-q24` · oa03 · 6 pts

Ordenando da temperatura de fechamento/crescimento mais alta para a mais baixa, qual sequência está correta, segundo o módulo?

- a) Biotita (Rb-Sr) > titanita (U-Pb) > zircão/monazita (U-Pb) > granada (Lu-Hf)
- b) Zircão/monazita (U-Pb, sem fechamento difusivo relevante até ~900 °C) > granada (Lu-Hf, fechamento relativamente alto) > titanita/rutilo (U-Pb, intermediário) > apatita (U-Pb) ≈ muscovita (Rb-Sr) > biotita (Rb-Sr, mais baixo do grupo)
- c) Apatita (U-Pb) > biotita (Rb-Sr) > zircão (U-Pb) > titanita (U-Pb)
- d) Todos os minerais e sistemas do módulo têm, na prática, a mesma temperatura de fechamento, e a ordem de datação depende só da ordem de análise no laboratório

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A tabela da Aula 02 resume exatamente essa hierarquia: zircão e monazita (U-Pb) praticamente não fecham por difusão até temperaturas muito altas (registram crescimento/recristalização); a granada por Lu-Hf fecha em temperatura relativamente alta (mais alta que o Sm-Nd na mesma granada) e tende a registrar os estágios iniciais do crescimento; titanita e rutilo (U-Pb) ocupam a faixa intermediária; apatita (U-Pb) e muscovita (Rb-Sr) ficam próximas na faixa mais baixa entre os minerais "mais quentes"; biotita (Rb-Sr) fecha a sequência com a temperatura mais baixa do grupo inteiro. "a", "c" e "d" invertem ou apagam essa hierarquia.
</details>

---

### 25. Dissertativa — `geologia-avancado-m27-q25` · oa01+oa02+oa03 · 10 pts

Descreva, na ordem correta, os quatro passos que a petrocronologia percorre entre "ter um cristal na mão" e "ter uma idade com significado geológico" — e diga, para cada passo, qual aula (ou par de aulas) do módulo o ensina.

<details>
<summary>Ver resposta</summary>

A ordem, estabelecida já na Aula 04 e válida para todo o módulo, é **textura → reação → condições P-T → idade**, nunca o contrário:

1. **Textura**: ler a posição microestrutural do domínio de interesse — relações porfiroblasto-matriz, zoneamento, relações de corte, imageamento por MEV (BSE/CL) — para saber o que aquele domínio representa antes de qualquer número (Aulas 01, 03 e 04).
2. **Reação**: identificar, pela composição (zoneamento de Mn, de Y, de HREE), que reação metamórfica ou processo magmático fez aquele domínio crescer, e correlacionar com fases coexistentes ou competidoras, como a granada disputando Y/HREE com os minerais acessórios (Aulas 01, 04 e 06).
3. **Condições P-T**: converter a associação mineral em valores numéricos de pressão e temperatura por geotermobarometria convencional, average P-T ou pseudosseções, obtendo um ponto ou um campo estreito do diagrama P-T para aquele domínio (Aula 05).
4. **Idade**: só então medir a idade isotópica do domínio, usando a técnica analítica cuja resolução espacial seja compatível com o tamanho do domínio identificado nos passos anteriores (Aula 03; Aulas 02, 06 e 07 para a interpretação da idade em si).

Uma idade medida sem os três primeiros passos é, no vocabulário da Aula 01, uma idade não ancorada — um número sem significado geológico atribuível.
</details>

---

### 26. Múltipla escolha — `geologia-avancado-m27-q26` · oa03 · 8 pts

Um zircão metamórfico que cresce **depois** da quebra retrógrada da granada, herdando um reservatório de HREE recém-liberado, deve mostrar, em relação a um zircão que cresceu **durante** o crescimento ativo da mesma granada, qual padrão de HREE?

- a) Um padrão idêntico, porque o coeficiente de partição zircão/granada não muda com o estágio da reação
- b) Um padrão de HREE anormalmente enriquecido, em contraste com o padrão achatado do zircão que cresceu competindo com a granada em crescimento ativo
- c) Um padrão de HREE necessariamente ausente, porque zircão pós-quebra de granada nunca incorpora terras-raras pesados
- d) Um padrão idêntico ao de um zircão puramente magmático sem qualquer relação com granada, tornando os dois indistinguíveis por Y/HREE

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A Aula 06 é explícita: zircão que cresce em coexistência com granada em crescimento ativo mostra um padrão de HREE achatado, porque a granada já capturou a maior parte do Y/HREE disponível; zircão que cresce depois da quebra da granada herda o reservatório subitamente liberado e tende a mostrar enriquecimento de HREE anormalmente alto para aquele estágio — o oposto do padrão achatado. "a" ignora que a competição depende de haver ou não granada ativamente sequestrando o reservatório no momento do crescimento do zircão. "c" e "d" contrariam o próprio mecanismo geoquímico que a aula descreve.
</details>

---

### 27. Verdadeiro ou Falso (justifique) — `geologia-avancado-m27-q27` · oa02 · 8 pts

"Porque o SIMS amostra um volume muito menor que o LA-ICP-MS, ele sempre consegue, numa seção polida comum, isolar lateralmente uma borda metamórfica de 3-4 μm de espessura sem misturar sinal do domínio vizinho."

<details>
<summary>Ver resposta</summary>

**Falso.**

A vantagem do SIMS sobre o LA-ICP-MS está na **profundidade/volume** amostrado (pit de ~1-3 μm de profundidade, contra dezenas de μm), não na resolução **lateral**: lateralmente, o pit do SIMS tem ~15-25 μm de diâmetro, a mesma ordem de grandeza de um spot de laser (Aula 03). Uma borda de 3-4 μm de espessura não cabe lateralmente num spot de SIMS tanto quanto não cabe num de laser — a saída, nesse caso, é o perfil em profundidade, feito num grão montado sem polir, com a face externa do cristal exposta ao feixe. Confundir a vantagem de profundidade do SIMS com uma vantagem lateral foi, precisamente, um dos achados corrigidos pela auditoria científica do módulo.
</details>

---

### 28. Aplicação / Integração — `geologia-avancado-m27-q28` · oa03+oa04 · 14 pts

Uma rocha metapelítica de um cinturão orogênico foi datada por: zircão U-Pb (borda, HREE achatado) = 602 ± 5 Ma; monazita U-Pb (domínio de baixo Y) = 599 ± 4 Ma; granada, microamostrada em três zonas por Sm-Nd = núcleo 605 ± 3 Ma, intermediária 596 ± 3 Ma, borda 588 ± 3 Ma; titanita U-Pb (~665 °C pelo termômetro Zr-em-titanita) = 572 ± 6 Ma; biotita Rb-Sr = 545 ± 8 Ma.

(a) Construa a sequência cronológica integrada, indicando o que cada idade amarra. (b) Calcule a duração de crescimento da granada e a taxa aproximada de resfriamento entre o fim do crescimento da granada e a idade da biotita. (c) O zircão mostra HREE achatado: o que isso acrescenta à leitura do estágio em que ele cresceu?

<details>
<summary>Ver resposta</summary>

**(a)** O núcleo da granada (605 Ma) é a idade mais antiga, marcando o início do crescimento metamórfico de alta temperatura. O zircão de borda (602 Ma) e a monazita (599 Ma) são consistentes, dentro de poucos milhões de anos, com esse mesmo intervalo de crescimento de alta temperatura, ligeiramente após o início registrado pelo núcleo da granada. A zona intermediária da granada (596 Ma) e a borda da granada (588 Ma) documentam a continuidade e o fim do crescimento do cristal. A titanita (572 Ma, ~665 °C) documenta um ponto no resfriamento pós-pico. A biotita por Rb-Sr (545 Ma, fechamento ~300-350 °C) fecha a sequência, registrando a passagem da rocha por essa temperatura mais baixa durante a exumação.

**(b)** Duração de crescimento da granada: 605 − 588 = **17 milhões de anos**. Taxa de resfriamento aproximada entre o fim do crescimento da granada (588 Ma) e a biotita (545 Ma): a rocha passou de uma condição de temperatura pelo menos equivalente à da titanita (~665 °C, registrada em 572 Ma, um ponto intermediário) até abaixo de ~300-350 °C (biotita) em 588 − 545 = 43 milhões de anos — uma taxa grosseiramente estimável na ordem de poucos °C por milhão de anos, do tipo comparável a taxas de exumação orogênica, como no exemplo da Aula 07. (Como no exemplo da própria Aula 07, essa duração de crescimento pressupõe que a granada não foi reequilibrada por difusão após cada zona ter se formado — condição a verificar antes de aceitar o número como definitivo.)

**(c)** O padrão de HREE achatado no zircão de borda é a assinatura de crescimento em coexistência com granada em crescimento ativo (Aula 06) — não apenas "evento metamórfico aos 602 Ma" de forma genérica, mas "evento metamórfico aos 602 Ma, durante o qual a granada da rocha estava presente e provavelmente crescendo", o que é consistente com o zircão de borda ter crescido dentro da janela de crescimento da granada (605-588 Ma) calculada em (b), reforçando a coerência interna de toda a reconstrução.
</details>

---

### 29. Dissertativa — `geologia-avancado-m27-q29` · oa04 · 10 pts

Explique por que a integração de múltiplos cronômetros numa única rocha (o procedimento da Aula 07) fica muito mais difícil em terrenos polimetamórficos, e por que a disciplina de ancorar toda idade em textura e composição (Aula 01) deixa de ser apenas boa prática nesses casos.

<details>
<summary>Ver resposta</summary>

Em terrenos que sofreram mais de um evento metamórfico, cada mineral pode conter domínios formados em eventos distintos: um zircão pode ter um núcleo do evento 1 e uma borda do evento 2; uma granada pode ter zonas de crescimento do evento 1, uma zona de reabsorção parcial, e novo crescimento do evento 2. Nesse cenário, o procedimento de integração da Aula 07 — reunir idades, atribuir cada uma a uma posição no caminho P-T, ordená-las cronologicamente e calcular taxas — só funciona se cada idade individual já estiver corretamente associada ao evento certo; misturar domínios de dois eventos diferentes numa única "sequência" produziria uma reconstrução sem sentido geológico, análoga ao problema da idade "borrada" de um cristal inteiro dissolvido em bloco, mas em escala de todo o terreno. É por isso que a disciplina de nunca interpretar uma idade sem antes caracterizar a textura e a composição do domínio específico analisado — a lição central da Aula 01 — deixa de ser uma boa prática recomendável e se torna a única forma de não colapsar dois (ou mais) eventos geológicos distintos numa única "idade da rocha" artefatual.
</details>

---

### 30. Múltipla escolha — `geologia-avancado-m27-q30` · oa04 · 6 pts

No exemplo de integração da Aula 07 (zircão, monazita, granada microamostrada, titanita e mica), o que permite calcular uma **duração** para o crescimento da granada, e não apenas uma idade única?

- a) O fato de a granada ser datada por Sm-Nd, um sistema que, por si só, sempre dá idades múltiplas para o mesmo cristal
- b) A microamostragem de zonas concêntricas de crescimento dentro do mesmo cristal, datando cada zona separadamente, em vez de dissolver o cristal inteiro em bloco
- c) O uso exclusivo de EPMA, que mede concentrações elementares em vez de razões isotópicas
- d) A comparação entre a idade da granada e a idade do zircão, que por si só já define uma duração de crescimento da granada

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A duração vem da **microamostragem** (Pollington & Baxter, método discutido na Aula 07): extrair várias frações concêntricas de um único cristal de granada e datar cada uma independentemente, em vez de medir uma isócrona de cristal inteiro (que daria uma média ponderada sem existência geológica própria — o mesmo problema da idade "borrada" que a Aula 01 descreve para o zircão). "a" está errado: o sistema isotópico em si não gera múltiplas idades automaticamente, é a estratégia de amostragem por zona que faz isso. "c" descreve EPMA, usado para datação química de monazita (Aula 03), não para o método de microamostragem de granada por Sm-Nd. "d" confunde comparação entre minerais diferentes (que dá pontos de ancoragem cronológica) com a duração de crescimento de um único cristal (que exige zonas do mesmo cristal).
</details>

---

### 31. Integração final — `geologia-avancado-m27-q31` · oa01+oa02+oa03+oa04 · 14 pts

Uma amostra de granulito de alto grau apresenta: zircões com núcleo de zoneamento oscilatório (Th/U ≈ 0,55) e borda sem zoneamento truncando o núcleo (Th/U ≈ 0,04, HREE achatado); monazita com domínios de Y alternando alto-baixo-alto; granada de alguns milímetros; titanita; e uma mica que precisa ser identificada corretamente antes de datada.

Monte o plano de trabalho completo: (a) que técnica de imageamento vem primeiro e por quê; (b) como interpretar o núcleo e a borda do zircão, incluindo o que o HREE achatado da borda acrescenta; (c) como ler a sequência alto-baixo-alto de Y na monazita; (d) qual técnica escolher para datar a borda fina do zircão preservando o grão; (e) qual mica é petrologicamente adequada para o Rb-Sr desse granulito, e por quê.

<details>
<summary>Ver resposta</summary>

**(a)** MEV com catodoluminescência (CL), antes de qualquer análise isotópica — é a técnica-padrão para revelar zoneamento oscilatório magmático e bordas metamórficas sem zoneamento em zircão, e sem essa imagem a escolha de qualquer ponto de análise seria um chute (Aula 03).

**(b)** O núcleo — zoneamento oscilatório concêntrico e Th/U alto (0,55) — tem a assinatura de crescimento magmático (Aula 01). A borda — sem zoneamento, truncando o núcleo, com Th/U baixo (0,04) — tem a assinatura de recristalização metamórfica. O HREE achatado da borda acrescenta que esse evento metamórfico ocorreu **em coexistência com granada em crescimento ativo** (Aula 06): a granada estava presente e provavelmente crescendo, competindo pelo mesmo reservatório de HREE que achatou o padrão do zircão.

**(c)** Y alto → baixo → alto na monazita é a assinatura de domínios que cresceram **antes** da granada (Y alto, reservatório ainda disponível), **durante** o crescimento ativo da granada (Y baixo, reservatório sendo drenado) e **depois** da quebra da granada (Y alto de novo, reservatório liberado) — a mesma competição geoquímica do item (b), vista do lado da monazita (Aula 06).

**(d)** Perfil em profundidade por SIMS, num grão irmão montado sem polir com a face externa exposta ao feixe — a borda fina não cabe lateralmente num spot de SIMS nem de LA-ICP-MS (ambos da ordem de dezenas de μm de diâmetro), e essa é a única das técnicas do módulo que preserva o grão para eventual reanálise, ao contrário do CA-ID-TIMS, que destrói o material (Aula 03).

**(e)** Biotita, não muscovita. Num granulito, a muscovita não é estável — reage com o quartzo antes da fácies granulito ser atingida — e uma muscovita eventualmente presente seria retrógrada, datando o seu próprio crescimento (numa temperatura abaixo da sua temperatura de fechamento) em vez de registrar a passagem da rocha pela temperatura de fechamento do Rb-Sr durante o resfriamento (Aula 02). A biotita, mineralogicamente compatível com a paragênese granulítica e com fechamento mais baixo (~300-350 °C), é a escolha correta para fechar a extremidade fria da trajetória P-T-tempo dessa rocha.
</details>

---

### 32. Aplicação — `geologia-avancado-m27-q32` · oa02+oa03 · 6 pts

Por que a variante LASS (*laser ablation split-stream*) do LA-ICP-MS é particularmente útil para o tipo de raciocínio desenvolvido na Aula 06 (correlacionar idade U-Pb de zircão com o padrão de Y/HREE do mesmo domínio)?

<details>
<summary>Ver resposta</summary>

Porque o LASS divide o material ablacionado por um único pulso de laser e o envia simultaneamente a dois espectrômetros — um medindo a razão isotópica U-Pb, outro medindo elementos-traço (Y e terras-raras pesados) — no mesmo volume de material e no mesmo instante (Kylander-Clark, Hacker & Cottle, 2013, Aula 03). Isso garante que a idade e a composição vêm exatamente do mesmo domínio físico do cristal, sem o risco de que dois spots separados (um para idade, outro para composição), mesmo próximos, tenham amostrado partes ligeiramente diferentes de um cristal zonado — o que comprometeria justamente a correlação idade-processo que a Aula 06 usa para interpretar o comportamento de Y/HREE em zircão, monazita e titanita.
</details>

---

**Total: 100 pontos.**
