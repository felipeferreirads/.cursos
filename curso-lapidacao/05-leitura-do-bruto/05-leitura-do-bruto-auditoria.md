# Auditoria científica — Módulo 05: Leitura e orientação do bruto

**Data:** 2026-09-03
**Modo:** `audit-and-fix` · **Profundidade:** `full` + consistência interna entre as seis aulas
**Material auditado:** as 6 aulas do módulo 05, em conjunto (nenhum questionário nem baralho existia — não houve o que propagar)
**Veredito:** ✅ **Aprovado com correções aplicadas** — nenhum achado 🔴 ou 🟠 em aberto. O gate de questionário/flashcards está **liberado**.

## Resumo

| Severidade | Achados | Corrigidos | Em aberto |
|---|---|---|---|
| 🔴 Erro | 5 | 5 | 0 |
| 🟠 Impreciso | 9 | 9 | 0 |
| 🟡 Desatualizado | 0 | — | 0 |
| 🔵 Sem fonte | 0 | — | 0 |
| ⚪ Controverso | 1 | 1 (reescrito como divergência) | 0 |
| **Total** | **15** | **15** | **0** |

Distribuição por aula: a01 — 2 · a02 — 1 · a03 — 2 · a04 — 4 · a05 — 4 · a06 — 2.

Nenhuma aula passou limpa. As três cadeias mais caras do módulo — a regra de orientação da zonação de cor (a03), o custo em rendimento da orientação pleocroica (a04) e a fórmula de estimativa de peso (a05) — estavam **as três erradas**, e as duas primeiras contradiziam o exemplo trabalhado da própria aula. Este é o módulo com a maior densidade de erro estrutural auditado até aqui neste curso.

**Formato de `claim_id`:** as 31 alegações herdadas do redator e as 5 criadas nesta auditoria têm todas **4 segmentos** e casam com `^[A-Z]{2,4}-[A-Z0-9]+-[A-Z0-9]+-[0-9]{3}$`. Nenhum resíduo de 5 segmentos sobrou (verificado por regex sobre os seis arquivos). Os dois escorregões corrigidos à mão antes desta auditoria — `INC-ACHADO-PROP-001` e `JAN-DEF-EXT-001` — estão íntegros.

**Nível teórico:** varredura específica por afirmação de competência de bancada nas seis aulas. **Nenhum achado.** As seis trazem, em "O que não concluir", a exclusão explícita da destreza manual (abrir janela, cortar respeitando clivagem, travar o bruto na dop, usar dicroscópio, serrar/pré-formar/medir, ajustar o ângulo na facetadora). Os verbos dos seis objetivos são todos de conhecimento observável.

---

## 🔴 Achados de erro

### 🔴 1. Regra de orientação da faixa de cor invertida — o "pior caso" é a orientação recomendada pela literatura

**claim_id:** `ZON-FAIXA-MESA-001`
**Tipo:** erro factual (causa-efeito invertida) + inconsistência interna
**Onde:** aula 03 · "A orientação da mesa muda o caminho da luz", "Exemplo trabalhado", "Erros comuns", "Recap relâmpago"
**Está escrito:** "Já uma **faixa de cor paralela à mesa** é o pior caso de todos: a pedra fica com uma metade viva e outra apagada, e girar a pedra na mão mostra a divisão. A saída é **inclinar** a orientação para que a faixa cruze o caminho de **todos** os raios"
**Problema:** é exatamente o contrário do que a prática lapidária faz. Quando há bandamento de cor, o lapidário orienta a pedra **para que as bandas fiquem paralelas à mesa** — vista pela mesa ou pelas facetas da coroa, a cor aparece uniforme —, e a banda mais escura vai para a **culaça**, de onde irradia cor por toda a gema. O caso ruim é o oposto: a faixa **de pé**, com o plano perpendicular ao da mesa, atravessando a pedra de lado a lado; aí só os raios de uma região a cruzam e a pedra fica meio viva, meio apagada. O texto ainda entrava em contradição consigo mesmo: duas linhas acima ele já prescrevia pôr a faixa fina **na culaça** — que é, geometricamente, deitá-la paralela à cinta —, e o exemplo trabalhado repetia a prescrição correta e a proibição errada na mesma frase.
**Correção aplicada:** invertidos os dois lados. O pior caso passou a ser a faixa **de pé** (plano perpendicular ao da mesa); a saída passou a ser **deitar** a faixa, paralela à mesa e à cinta, de preferência funda, perto da culaça. Propagado para o "Exemplo trabalhado" (a linha de *Orientação* e a linha de *O que seria erro*), para "Erros comuns" (bullet 2) e para o "Recap relâmpago".
**Fonte:** prática lapidária corrente de orientação de zonação — "the Lapidarist will tend to orient the gemstone so that the bands run parallel with the table facet… normally, the darker band will be placed in the culet, as it reflects its colour throughout the gem" (Gemporia, *Learning Library*, "Zoning / Colour Banding"); GIA — o lapidário experiente atenua o efeito de face da zonação dispondo as zonas de cor **paralelas à cinta** ou colocando uma pequena concentração de cor na culaça. Consultado em 2026-09-03. · **Nível:** base de referência gemológica + literatura lapidária
**Confiança:** confirmado
**Também aparece em:** nenhum outro arquivo do curso (o módulo 06 ainda não foi escrito; a aula 01 fala de zonação só como "o que a luz difusa revela", sem regra de orientação).

### 🔴 2. As duas situações do custo em rendimento estão trocadas entre si — e contradizem o exemplo da própria aula

**claim_id:** `PLE-REN-CUSTO-001`
**Tipo:** erro factual (geometria invertida) + inconsistência interna
**Onde:** aula 04 · "O custo em rendimento", "Recap relâmpago"
**Está escrito:** "**A cor boa está perpendicular ao comprimento do prisma.** Orientar a mesa perpendicular a essa direção significa cortar a pedra 'atravessada' no cristal: a **mesa fica limitada pela largura** do prisma e o comprimento vira sobra. […] É o caso que mais dói. — **A cor boa está ao longo do comprimento.** Aí a orientação de cor e a orientação de peso coincidem, e não há dilema"
**Problema:** a geometria é a inversa. A própria aula define, no passo 2 do procedimento, que a mesa fica **de frente para a direção pela qual a cor desejada é vista**. Logo: se a cor boa é vista **olhando ao longo do comprimento**, a mesa fica perpendicular ao comprimento, o plano da cinta fica perpendicular ao eixo do prisma e **as duas medidas da cinta ficam presas à largura** — o comprimento vira profundidade e sobra. Esse é o caso caro. Se a cor boa é vista **de lado**, a mesa fica de frente para a lateral, o plano da cinta **contém** o comprimento do cristal, e a pedra pode ser longa — orientação de cor e de peso praticamente coincidem. O erro é flagrante porque o exemplo trabalhado da mesma aula executa a versão correta: a safira mostra o azul-violeta **ao longo de c**, a mesa vai perpendicular a c, e o rendimento despenca de ~3 ct para ~1,2 ct. Texto e exemplo diziam coisas opostas.
**Correção aplicada:** as duas situações foram trocadas de lugar e reescritas na linguagem do procedimento ("a cor boa aparece olhando ao longo do comprimento" × "olhando de lado, atravessando o prisma"), com o primeiro caso marcado explicitamente como o do exemplo abaixo. Propagado para o bullet de custo do "Recap relâmpago".
**Fonte:** geometria de inscrição de sólido em prisma (a orientação da mesa fixa qual dimensão do bruto vira profundidade); Sinkankas, *Gem Cutting: A Lapidary's Manual* — perda de rendimento ao cortar atravessado no cristal; Vargas & Vargas, *Faceting for Amateurs* — orientação para cor versus a maior pedra possível; corroborado pelo exemplo trabalhado da própria aula. · **Nível:** geometria + literatura de facetamento
**Confiança:** confirmado
**Também aparece em:** aula 05, "Antes de começar" ("a pedra de cor cheia costuma ser a pedra pequena") e "Onde o peso vai" — **corretos, não alterados**: enunciam a consequência, não a geometria invertida.

### 🔴 3. Peso do bruto do exemplo da safira excede o volume geometricamente disponível

**claim_id:** `PLE-EXEM-SAFIRA-001` *(novo — os números do exemplo não existiam como alegação separada)*
**Tipo:** erro factual (dado numérico impossível)
**Onde:** aula 04 · "Exemplo trabalhado", enunciado e Passo 3
**Está escrito:** "Medidas aproximadas: 15 mm de comprimento (ao longo de c), 8 mm de diâmetro. Peso ~4,5 g (~22 ct)." · "Resultado: uma safira de ~6 mm, **~1,2 ct**"
**Problema:** **(a)** um cilindro de 15 mm × 8 mm de diâmetro tem ≈ 754 mm³; com a densidade relativa do coríndon (~3,98–4,02), o **cilindro cheio** pesaria no máximo ~3,0 g. Um barril, que afina nas duas pontas, pesa menos ainda. Os 4,5 g declarados são impossíveis — sobram ~50% de massa sem volume onde caber. **(b)** Com o fator de forma correto do brilhante redondo (0,0018 — ver achado 4), uma safira de 6,0 mm em proporções corretas dá ~1,0 ct, não 1,2 ct; 1,2 ct corresponde a ~6,5 mm. Os dois números do passo 3 não fechavam entre si.
**Correção aplicada:** **(a)** peso do bruto ajustado para **~2,6 g (~13 ct)** — o cilindro circunscrito com um fator de preenchimento de barril realista. **(b)** o diâmetro da pedra orientada para cor passou de ~6 mm para **~6,5 mm**, mantendo o 1,2 ct, que é o número usado em quatro pontos da aula (Passo 3, Passo 5, "O que não concluir", "Recap") e, portanto, o mais caro de mexer. A alternativa de peso (~12 × 7 mm, ~3 ct) foi reconferida com o fator do degrau corrigido (0,0025) e a profundidade máxima que um retângulo de 7 mm de largura admite dentro de um barril de 8 mm (~3,9 mm): 12 × 7 × 3,9 × 4,0 × 0,0025 ≈ 3,3 ct — o "talvez 3 ct" continua válido e agora é conservador. O rendimento implícito passa a ser ~9% para a pedra de cor e ~23% para a de peso, ambos dentro das faixas corrigidas da aula 05.
**Fonte:** geometria do cilindro circunscrito; densidade relativa do coríndon ~3,98–4,02; fatores de forma de estimativa de peso (redondo 0,0018; degrau/esmeralda 0,0025) — ver `REN-FORMULA-PESO-001`. Consultado em 2026-09-03. · **Nível:** geometria + dados físicos + tabela de estimativa de peso
**Confiança:** confirmado
**Também aparece em:** `course-state.yaml`, `next_action` do módulo 05, que registra "safira Sri Lanka barril, cálculo 1,2 ct cor cheia × 3 ct cor lavada" — os dois números **sobreviveram** à correção, então o registro continua verdadeiro; o `next_action` foi reescrito nesta etapa por outro motivo.

### 🔴 4. Fatores de forma da fórmula de estimativa de peso deslocados uma posição na tabela

**claim_id:** `REN-FORMULA-PESO-001`
**Tipo:** erro factual (dado numérico) — três de três valores errados
**Onde:** aula 05 · "Estimar o peso antes de cortar", "Exemplo trabalhado" (opções A, B e C), "Erros comuns", "O que não concluir", "Recap relâmpago"
**Está escrito:** "cerca de **0,0020** para o brilhante redondo, **0,0025** para oval e navete, **0,0026** para o talhe degrau retangular […] trate como ±10%"
**Problema:** os valores estão **deslocados uma posição** na tabela corrente de fatores de forma. Os fatores usados na estimativa de peso de gema lapidada são: **redondo 0,0018**, **oval 0,0020**, **esmeralda/degrau 0,0025** e **navete 0,0016**. A aula atribuiu ao redondo o fator do oval, ao oval o fator do degrau, e inventou 0,0026 para o degrau. O caso mais grave é a **navete**, que a aula agrupou com o oval em 0,0025 quando o fator real é 0,0016: um erro de **+56%**, muito além do "±10%" que a própria aula declarava como margem. E a margem estava mal caracterizada: as fontes não dão um intervalo simétrico, mas um **acréscimo unidirecional** — a fórmula sobre o bloco `L × W × D` é um piso, ao qual se somam 2–10% por cinta grossa e 5–10% por barriga de pavilhão.
**Correção aplicada:** os quatro fatores corrigidos no corpo, e a navete separada do oval. A caracterização "±10%" foi substituída por "é um piso, +2–10% por cinta grossa e +5–10% por barriga de pavilhão". O exemplo trabalhado foi **recalculado**: opção A 2,5 → **2,3 ct** (rendimento continua ~6%); opção B 4,3 → **4,2 ct** (rendimento 11% → **10%**); opção C 5,8 → **5,5 ct** (rendimento continua **14%**); o ganho de C sobre B, 1,5 → **1,3 ct**. Todas as conclusões qualitativas do exemplo sobrevivem: A continua descartada por forma errada, B continua "quase o dobro de A", e a decisão B × C continua a mesma. Propagado para "Erros comuns", "O que não concluir" e o "Recap relâmpago".
**Fonte:** tabela padrão de fatores de forma para estimativa de peso de gema lapidada — redondo (diâmetro² × profundidade) × SG × 0,0018; oval L × W × D × SG × 0,0020; esmeralda 0,0025; navete 0,0016; acréscimo de 2–10% por cinta grossa e 5–10% por barriga de pavilhão. Esslinger, *Stone Weight Estimation Formula*; The Plumb Club, *How to Estimate Gem Weight*. Consultado em 2026-09-03. · **Nível:** base de referência da indústria
**Confiança:** confirmado
**Também aparece em:** aula 04, exemplo da safira — os pesos foram reconferidos com os fatores corretos (achado 3).

### 🔴 5. Kunzita descrita com clivagem perfeita "em um sentido"

**claim_id:** `INC-CLIV-KUNZ-001` *(novo — a contagem de direções de clivagem da kunzita não existia como alegação separada)*
**Tipo:** erro factual
**Onde:** aula 02 · "Exemplo trabalhado", enunciado e parágrafo *Clivagem*
**Está escrito:** "a kunzita tem clivagem perfeita em um sentido, paralela ao comprimento do prisma" · "*Clivagem.* O plano é paralelo ao comprimento do prisma. […] A mesa tem de ficar **inclinada** alguns graus em relação ao plano"
**Problema:** o espodumênio tem clivagem **perfeita em duas direções**, ambas do prisma `{110}`, paralelas ao eixo c e cruzando-se a cerca de **87°**. É precisamente essa dupla direção que faz da kunzita o caso-limite de fragilidade que o exemplo quer ilustrar; reduzi-la a "um sentido" enfraquece o próprio argumento e ensina uma restrição menor do que a real, porque com dois planos a família de orientações proibidas é bem maior. Além disso a aula omitia que a proibição alcança a **cinta**: um plano de clivagem quase paralelo à cinta da pedra pronta é uma fraqueza latente que pode partir a gema na cravação ou no uso — restrição que a própria aula enuncia na seção de conteúdo e depois esquece no exemplo.
**Correção aplicada:** "em um sentido" → "em **duas** direções, ambas paralelas ao comprimento do prisma e cruzando-se a cerca de 87°"; o parágrafo *Clivagem* passou a falar de "os dois planos" e do desvio "em relação a **ambos**", e o adendo não verificado sobre concentração de tensão na ponta do pavilhão foi substituído pela regra documentada — a proibição vale também para a cinta.
**Fonte:** dados cristalográficos do espodumênio (clivagem perfeita `{110}` em duas direções, ângulo ~87°) — Mindat / geology.com / International Gem Society, *Spodumene* e *Kunzite Faceting Information*; GIA, *Gems & Gemology* (verão de 2020), "The Fragility of the Eternal": Kunzite — Origin, Cutting, and Identification, que registra a regra de não deixar plano de clivagem quase paralelo à cinta. Consultado em 2026-09-03. · **Nível:** dados cristalográficos + base de referência gemológica
**Confiança:** confirmado
**Também aparece em:** `INC-ACHADO-PROP-001` (mesma aula), que lista a kunzita entre os materiais de clivagem marcada sem contar direções — **correto como escrito, não alterado**.

---

## 🟠 Achados de imprecisão

### 🟠 6. Faixas de rendimento subestimadas, e duas delas sem fonte

**claim_id:** `REN-FAIXA-TIP-001`
**Tipo:** dado numérico + evidência insuficiente
**Onde:** aula 05 · "Quanto se perde, tipicamente", "Erros comuns", "Recap relâmpago"
**Está escrito:** "entre **15% e 25%** do peso do bruto; bruto mal formado […] cai para **8% a 12%**; e ocasionalmente um cristal já perto da forma final passa de 30%. Para **cabochão** […] **30% a 50%** ou mais"
**Problema:** quatro problemas encadeados. **(a)** A faixa de 15–25% é a do **corte comercial de fábrica**; o corte de precisão, que é o padrão que esta aula usa em toda a discussão beleza × peso, fica em **25–33%**. **(b)** "Ocasionalmente passa de 30%" é falso: 30% já está dentro da faixa normal do corte de precisão, e bruto bem formado chega a **40%** ou mais. **(c)** A faixa de 8–12% para bruto ruim não foi localizada em nenhuma fonte — a literatura afirma que bruto com saliências a derrubar rende menos que a média, sem quantificar. **(d)** Nenhuma fonte quantifica o rendimento de cabochão; a diferença a favor do cabochão é registrada qualitativamente, e o intervalo 30–50% é atribuição não verificada.
**Correção aplicada:** faixas corrigidas para **25–33% em corte de precisão** e **15–25% em corte de fábrica**, com **>40%** para bruto quase preformado. Os dois números sem fonte saíram, seguindo a política de não inventar correção: o piso de bruto ruim virou "cai bem abaixo disso — os projetos do exemplo desta aula ficam entre 6% e 14%", que **usa o próprio exemplo trabalhado como demonstração** em vez de um número emprestado; e o cabochão passou a ser descrito como "reconhecidamente maior, embora a literatura não fixe uma faixa citável". A regra prática de planejamento (20%) foi mantida, agora com fonte. Propagado para "Erros comuns" e "Recap relâmpago".
**Fonte:** International Gem Society, *What is the Average Gemstone Faceting Yield?* — "the yield from a clean, facetable piece will usually range between 25% and 33% with custom cutting and 15% to 25% with factory cutting"; bruto excepcionalmente bem formado a 40%+; recomendação explícita de planejar por 20%. Consultado em 2026-09-03. · **Nível:** base de referência gemológica
**Confiança:** confirmado (as faixas de precisão e de fábrica, e o teto) · não verificado, e por isso removido (o piso de 8–12% e a faixa de cabochão)
**Também aparece em:** nenhum outro arquivo.

### 🟠 7. Perda de peso no recorte truncada na metade alta do espectro

**claim_id:** `REN-RECUT-PERDA-001` *(novo — o custo do recorte estava embutido em `REN-BELEZA-PESO-001` e ganhou alegação própria por ser um dado numérico independente)*
**Tipo:** dado numérico + omissão que gera erro
**Onde:** aula 05 · "A escolha que sempre aparece: beleza × peso", "Erros comuns", "Recap relâmpago"
**Está escrito:** "Relapidar uma dessas pedras para ângulos corretos (**recorte**) custa tipicamente de **10% a 30%** do peso."
**Problema:** o teto de 30% corta fora justamente os casos que motivam a aula. A literatura de recorte trabalha com **10% a 50%**, e passa de 50% em nativos muito rasos ou assimétricos — o caso citado como típico é uma safira de 3 ct rasa demais que perde ~40% ao ser levada a proporções corretas. Como a aula está usando esse número exatamente para dimensionar o preço de desfazer a "pedra de peso", subestimá-lo enfraquece o argumento central da seção.
**Correção aplicada:** "10% a 30%" → "**10% a 50%** do peso, e mais que isso quando a pedra é muito rasa ou torta". Propagado para "Erros comuns" e "Recap relâmpago".
**Fonte:** literatura de recorte de gema colorida — Justin K. Prim, *The Art and Joy of Recutting Gemstones* (perda de 10–50%); Faceting Academy, *Recutting Native Cut Gemstones* (nativos rasos e tortos passando de 50%). Consultado em 2026-09-03. · **Nível:** literatura de lapidação
**Confiança:** confirmado
**Também aparece em:** nenhum outro arquivo.

### 🟠 8. "Cristais crescem alongados ao longo do eixo óptico" generalizado indevidamente aos biaxiais

**claim_id:** `PLE-CRESC-EIXO-001` *(novo)*
**Tipo:** confusão de escopo
**Onde:** aula 04 · "O custo em rendimento", frase de abertura; "Recap relâmpago"
**Está escrito:** "Cristais crescem, na maioria, **alongados ao longo do eixo óptico** — prismas compridos."
**Problema:** vale para muitos **uniaxiais**, em que o eixo óptico é o eixo cristalográfico c e o hábito prismático é comum. Não se generaliza aos **biaxiais**, e a aula acabara de listar cinco deles (iolita, tanzanita, andaluzita, topázio, crisoberilo) três parágrafos antes. Num biaxial os dois eixos ópticos são direções da indicatriz óptica, situadas no plano óptico, e **não correspondem a nenhum eixo cristalográfico** nem à direção de alongamento — de modo que a relação entre cor, eixo óptico e hábito tem de ser levantada caso a caso e não pode ser deduzida do formato do cristal. Há ainda um ponto de calibragem: o GIA registra que o coríndon natural é "generally oriented with the c-axis perpendicular to the table, which tends to provide the best color **and weight retention**", ou seja, no bruto de coríndon típico a orientação de cor não é necessariamente a que dói — o barril muito alongado do exemplo é o caso difícil, não a regra.
**Correção aplicada:** a frase foi restrita aos uniaxiais e recebeu um parêntese explicitando que nos biaxiais os eixos ópticos não coincidem com nenhum eixo de crescimento. O bullet do "Recap relâmpago" foi alinhado ("muitos cristais uniaxiais"). Em "O que não concluir", o bullet que já isentava as medidas do exemplo passou a marcar também que se trata de um caso deliberadamente difícil e que, em bruto de coríndon menos alongado, a mesa perpendicular a c costuma reter peso também.
**Fonte:** óptica cristalina padrão (indicatriz uniaxial × biaxial; os eixos ópticos de um biaxial situam-se no plano óptico e não correspondem a eixos cristalográficos); GIA, *Gems & Gemology* (outono de 2014), "Pleochroism in Faceted Gems: An Introduction" — "the o-ray is always the darker of the two colors" no coríndon e a orientação usual com o eixo c perpendicular à mesa. Consultado em 2026-09-03. · **Nível:** literatura revisada por pares + óptica cristalina
**Confiança:** confirmado
**Também aparece em:** `PLE-CLASSE-NUM-001` (mesma aula), que classifica corretamente uniaxiais, biaxiais e isotrópicos — **verificado e correto, não alterado**.

### 🟠 9. "A causa é química, não óptica: nenhum ângulo conserta" — autocontraditório e com a física trocada

**claim_id:** `EXT-CONSERTO-CAUSA-001`
**Tipo:** inconsistência interna + certeza indevida
**Onde:** aula 06 · "Extinção — cinco causas independentes", causa 3; quadro `[!note]`; "Erros comuns"; "Recap relâmpago"
**Está escrito:** "Aqui a causa é **química**, não óptica: nenhum ângulo conserta." · "**Achar que ângulo de pavilhão conserta qualquer extinção.** […] A extinção por cor saturada é absorção — nenhum ângulo a resolve; **só um talhe mais raso a atenua**."
**Problema:** duplo. **(a)** A frase se desmente duas linhas adiante: "um talhe mais raso" **é** uma mudança de ângulo de pavilhão. Dizer "nenhum ângulo conserta" e depois prescrever uma mudança de ângulo como atenuação é uma contradição que o aluno vai encontrar sozinho. O enunciado defensável é outro: manter os **ângulos corretos** não resolve; a atenuação exige sair de propósito do ótimo óptico, e por isso é um compromisso, não um conserto. **(b)** A absorção da luz por um centro de cor **é** um fenômeno óptico, de origem química. Classificá-la como "química, não óptica" ensina uma separação que não existe e que atrapalha o módulo 08, onde absorção e geometria voltam juntas.
**Correção aplicada:** a causa 3 passou a dizer que a **origem** é química — a absorção da própria cor — e que não se trata de um erro de geometria: manter os ângulos corretos não resolve. Em "Erros comuns", "nenhum ângulo a resolve" virou "nenhum ângulo **correto** a resolve; só se atenua encurtando o caminho da luz com um talhe mais raso, sacrificando brilho". A coluna "Se conserta com ângulo?" do quadro passou de "só a causa 1" para "só a 1 (a 3 apenas se atenua)". O "Recap relâmpago" foi alinhado.
**Fonte:** Sinkankas, *Gem Cutting: A Lapidary's Manual* — talhe mais raso para clarear material de cor saturada, com perda de brilho; United States Faceters Guild; Vargas & Vargas, *Faceting for Amateurs*. · **Nível:** literatura de facetamento + consistência interna
**Confiança:** confirmado
**Também aparece em:** aula 05, "A escolha que sempre aparece" — cita extinção como preço da pedra de peso, sem afirmar nada sobre correção por ângulo. **Correto, não alterado.**

### 🟠 10. Mecanismo da extinção por índice baixo descrito como vazamento "em cada rebatida"

**claim_id:** `EXT-CINCO-CAUSAS-001`
**Tipo:** omissão que gera erro
**Onde:** aula 06 · "Extinção — cinco causas independentes", causa 2
**Está escrito:** "o cone de ângulos que refletem por dentro é menor, e **mais luz vaza em cada rebatida**"
**Problema:** numa faceta atingida **acima** do ângulo crítico a reflexão interna é **total** — não vaza nada, e isso independe do índice. O que o índice baixo faz é **estreitar o cone de direções** que satisfazem essa condição: uma fração maior dos raios cai fora do cone e escapa, e a margem de erro de ângulo tolerada pelo projeto encolhe. Dito como está, o texto ensina que a reflexão interna total é parcial, o que colide de frente com o que a aula acabara de afirmar sobre o janelamento na seção anterior e com o pré-requisito do curso de Gemologia.
**Correção aplicada:** "e mais luz vaza em cada rebatida" → "então uma fração maior dos raios escapa em vez de voltar, e a margem de erro de ângulo é menor". As outras quatro causas foram conferidas uma a uma e mantidas: proporção + head shadow, saturação, estilo degrau e contorno alongado/bowtie estão corretas, mutuamente independentes e corretamente separadas — a auditoria confirma o quadro de cinco causas pedido pelo hub do módulo.
**Fonte:** United States Faceters Guild — *Refractive Index and Critical Angle* e *Design Principles* (facetas do pavilhão abaixo do ângulo crítico "janelam" em vez de refletir; o ângulo crítico é função do índice; material de índice baixo pede coroa normal ou mais alta para compensar). Consultado em 2026-09-03. · **Nível:** literatura normativa do domínio
**Confiança:** confirmado
**Também aparece em:** `JAN-CAUSA-PAV-001` (mesma aula), que descreve o mecanismo corretamente — **verificado e correto, não alterado**; a correção alinha a causa 2 a ele.

### 🟠 11. "Todos os raios convergem para a ponta antes de voltar"

**claim_id:** `ZON-ORIENT-PATH-001`
**Tipo:** certeza indevida
**Onde:** aula 03 · "A orientação da mesa muda o caminho da luz"; "Exemplo trabalhado"
**Está escrito:** "Como **todos** os raios convergem para a ponta antes de voltar, aquela lasquinha de cor 'pinta' a pedra inteira" · "Assim, **todos** os raios que entram pela mesa passam pela faixa ao convergir para a ponta"
**Problema:** num brilhante, boa parte dos raios volta após duas reflexões em facetas principais opostas do pavilhão sem passar pela região da culaça. A técnica funciona porque a **maior parte** do caminho óptico se concentra ali, não porque haja convergência total — que é uma propriedade de um cone, não de um pavilhão facetado. O quantificador absoluto transforma uma boa heurística de projeto numa lei falsa, e é o tipo de afirmação que o módulo 08 vai desmentir quando entrar em traçado de raios.
**Correção aplicada:** "todos os raios convergem" → "quase todo raio que entra pela mesa passa pela região da ponta"; no exemplo, "todos os raios […] ao convergir para a ponta" → "quase todos os raios […] na convergência para a ponta". A ressalva foi registrada na alegação auditável.
**Fonte:** GIA — mistura óptica e a técnica de posicionar cor concentrada perto da culaça (descrita como a cor "inundando" a pedra, sem afirmação de convergência total); Sinkankas, *Gem Cutting: A Lapidary's Manual*. Consultado em 2026-09-03. · **Nível:** base de referência gemológica
**Confiança:** confirmado
**Também aparece em:** "Recap relâmpago" da mesma aula, que diz apenas "faixa fina na culaça 'pinta' a pedra toda por mistura óptica" — sem quantificador absoluto, **correto, não alterado**.

### 🟠 12. Direção de vibração confundida com direção de propagação

**claim_id:** `PLE-ORIENT-PROC-001`
**Tipo:** erro factual (mecanismo) de baixo impacto na conclusão
**Onde:** aula 04 · "Qual cor se quer, e onde ela está", passo 2
**Está escrito:** "a mesa da pedra pronta tem de ficar de frente para a direção 1 — ou seja, a luz que entra reto pela mesa **vibra predominantemente naquela direção** e devolve aquela cor"
**Problema:** a luz que **viaja** numa direção vibra no plano **perpendicular** a ela — é o fato que sustenta a seção seguinte da própria aula ("olhando exatamente ao longo do eixo óptico não há pleocroísmo"). A justificativa dada, tomada ao pé da letra, contradiz o vocabulário que a aula define ("direção de vibração: o plano em que a luz 'balança' ao atravessar o cristal"). A conclusão prática — mesa perpendicular à direção pela qual a cor desejada é vista — está certa; só a razão oferecida estava errada.
**Correção aplicada:** a oração explicativa passou a dizer que "a luz que entra reto pela mesa **viaja** naquela direção e devolve aquela cor", removendo a atribuição de vibração. Edição de uma palavra, sem tocar na conclusão.
**Fonte:** óptica cristalina padrão (a direção de vibração é perpendicular à de propagação); GIA, *Gems & Gemology* (outono de 2014), "Pleochroism in Faceted Gems: An Introduction"; vocabulário da própria aula. · **Nível:** óptica + consistência interna
**Confiança:** confirmado
**Também aparece em:** `PLE-EIXO-OPT-001` (mesma aula), que enuncia corretamente a relação eixo óptico → cor ordinária — **verificado e correto, não alterado**.

### 🟠 13. Índice de refração da granada dado como valor único

**claim_id:** `BRU-IMER-IDX-001`
**Tipo:** dado numérico (LC-05: número tabelado sem faixa)
**Onde:** aula 01 · "A imersão"
**Está escrito:** "Gemas de índice alto (coríndon ~1,76, granada **~1,74**) nunca terão casamento com líquido comum"
**Problema:** "granada" é um **grupo**, com índice espalhado de ~1,714 (piropo) a ~1,888 (demantoide), passando por almandina ~1,79 e espessartita ~1,80. O valor 1,74 corresponde a piropo/grossulária e fica abaixo das granadas mais comuns em bancada. A régua LC-05 deste curso exige, para número tabelado, valor de referência **com faixa e fonte** — e o resto da mesma lista (água, glicerina, álcool) traz faixa ou aproximação declarada. A granada era a única entrada com valor único e falso como representante do grupo.
**Correção aplicada:** "granada ~1,74" → "granada **1,71–1,89 conforme a espécie**". Os demais índices da lista foram conferidos e mantidos: água 1,333, isopropanol 1,377, glicerina 1,473, óleo mineral 1,46–1,48, coríndon 1,76, berilo 1,58. A faixa e as fontes ficaram registradas na alegação auditável.
**Fonte:** índices de refração do grupo da granada (piropo ~1,714; grossulária ~1,73; almandina ~1,79; espessartita ~1,80; andradita/demantoide ~1,888) — dados gemológicos padrão; índices de refração de água, isopropanol, glicerina e óleo mineral (dados físico-químicos padrão). Consultado em 2026-09-03. · **Nível:** dados gemológicos e físico-químicos
**Confiança:** confirmado
**Também aparece em:** aula 05, "Antes de começar", que dá a **densidade** da granada como 3,8–4,2 — grandeza diferente, com faixa declarada, **correta, não alterada**. Aula 06 cita a granada como material de índice alto, sem número — **correto, não alterado**.

### 🟠 14. "Limitado pela menor dimensão útil" não bate com o bloco declarado no mesmo exemplo

**claim_id:** `REN-ESTIM-PROC-001`
**Tipo:** inconsistência interna
**Onde:** aula 05 · "Exemplo trabalhado", opção A
**Está escrito:** "A maior pedra redonda que cabe no bloco tem diâmetro ~8,5 mm **(limitado pela menor dimensão útil)**"
**Problema:** o volume aproveitável declarado três linhas acima é 11 × 9 × 8 mm. A **menor** dimensão é 8 mm, e é ela que vira a profundidade da pedra (a opção A usa 5,6 mm de profundidade, folgada dentro dos 8). O que limita o **diâmetro** é a menor das duas medidas do **plano da cinta** — os 9 mm. Como a opção B, logo abaixo, usa um contorno de 10,5 × 8,5 mm nesse mesmo plano, o exemplo contradiz a própria justificativa em quatro linhas.
**Correção aplicada:** "(limitado pela menor dimensão útil)" → "(limitado pela menor medida do contorno disponível, os 9 mm)".
**Fonte:** consistência interna do exemplo (bloco 11 × 9 × 8 mm; contorno de B em 10,5 × 8,5 mm no mesmo plano). · **Nível:** verificação aritmética interna
**Confiança:** confirmado
**Também aparece em:** nenhum outro arquivo.

---

## ⚪ Achado controverso

### ⚪ 15. Direção da melhor cor na água-marinha — as fontes divergem

**claim_id:** `BRU-AQUA-ORIENT-001` *(novo)*
**Tipo:** controvérsia
**Onde:** aula 01 · "Exemplo trabalhado", passo 1 e passo 4(a)
**Está escrito:** "numa água-marinha a cor **costuma ser mais forte olhando ao longo do comprimento do cristal**" · "(a) Orientação: mesa perpendicular ao comprimento, para ver a cor mais forte de frente."
**Problema:** há divergência real entre fontes do mesmo nível. Parte da literatura lapidária recomenda orientar "no c" para o melhor azul — o que corresponde à mesa perpendicular ao comprimento e valida a afirmação da aula. Outra parte situa o azul mais profundo na observação **perpendicular** ao eixo c, o que é o esperado se a cor mais saturada do berilo for a do raio extraordinário, visível apenas quando a luz não viaja ao longo de c. O dicroísmo da água-marinha é, além disso, descrito como **fraco** por várias fontes, o que reduz a nitidez do critério e explica a divergência. A aula apresentava um dos lados como regra da espécie.
**Correção aplicada (política ⚪: não arbitrar o debate):** o passo 1 passou a registrar que "a cor mais forte pode estar ao longo do comprimento ou atravessada no cristal — a literatura de lapidação divide-se sobre qual das duas domina — e a janela lateral permite comparar as duas direções antes de decidir". O passo 4(a) deixou de enunciar uma regra da espécie e passou a registrar um achado **daquela peça**: "nesta peça a cor mais forte apareceu olhando ao longo do comprimento, então a mesa vai perpendicular a ele". O exemplo fica factualmente seguro, e o efeito pedagógico melhora: a leitura passa a **decidir** a orientação em vez de confirmá-la.
**Fonte:** International Gem Society, *Aquamarine Faceting Information* — dicroísmo "fraco", "orientating on the 'c' is slightly better"; contra fontes gemológicas que atribuem o azul mais profundo ao raio extraordinário, visível perpendicularmente a c. Consultado em 2026-09-03. · **Nível:** base de referência gemológica (divergente)
**Confiança:** em disputa
**Também aparece em:** nenhum outro arquivo. **Não é** um caso de LC-08 no corpo da aula (a controvérsia declarada da a01 é outra); fica registrada na alegação auditável e neste relatório.

---

## Verificado e correto

O que foi conferido e **não** gerou achado:

**Alegações auditáveis aprovadas sem alteração (21 de 36):** `BRU-JAN-DEF-001`, `BRU-ILUM-MODO-001`, `BRU-DEC-CINCO-001`, `BRU-LEIT-LIM-001`; `INC-POS-ZONA-001`, `INC-CAB-MULT-001`, `INC-FRAT-PROP-001`, `INC-CLIV-ORIENT-001`, `INC-ACHADO-PROP-001`; `ZON-PADRAO-TIPO-001`, `ZON-TALHE-MIX-001`, `ZON-VS-PLEO-001`; `PLE-CLASSE-NUM-001`, `PLE-EIXO-OPT-001`, `PLE-TILT-COMPR-001`, `PLE-DECISAO-DEST-001`; `REN-PERDAS-ONDE-001`, `REN-BELEZA-PESO-001`; `JAN-DEF-EXT-001`, `JAN-CAUSA-PAV-001`, `EXT-PREVISAO-PROJ-001`.

**Pontos de atenção levantados pelo hub do módulo, conferidos um a um:**

- **As cinco causas de extinção (a06)** — conferidas individualmente. Proporção + head shadow, saturação alta, estilo degrau e contorno alongado/bowtie estão **corretas e bem separadas**; só a causa 2 (índice baixo) teve o mecanismo corrigido (achado 10). A independência mútua das cinco se sustenta, e a soma de duas delas no Caso 1 do exemplo trabalhado (proporção + saturação) está correta.
- **A distinção janela × extinção (a06)** — **correta e bem construída**. Janela = luz entra pela mesa e sai pelo fundo, centro claro, vê-se através; extinção = luz não volta ao olho, zona escura. A assimetria "janelamento com causa essencialmente única, extinção com causas múltiplas" bate com a literatura da USFG, que trata o janelamento como consequência direta de facetas de pavilhão abaixo do ângulo crítico. A homonímia com a "janela de inspeção" da aula 01 está sinalizada em "Antes de começar" — boa prática, mantida.
- **Índices e proporções da a06** — quartzo ~1,55, feldspato ~1,53, coríndon ~1,76, zircão ~1,95: **corretos** como ordem de grandeza (zircão alto 1,925–1,984). A profundidade de ~70% do diâmetro para brilhante redondo em quartzo confere com pavilhão de 41–43° e coroa usual (≈ 67–70%); a de ≈ 66% para a turmalina da a05 é ligeiramente alta mas dentro da tolerância declarada. **Nenhum achado.**
- **Bowtie** — a atribuição a contornos alongados e pontudos (navete, oval comprida, gota), a ausência em contorno redondo e a quase-ausência em quadrado estão **corretas**, assim como o mecanismo (as facetas do pavilhão que cruzam a largura não conseguem todas ficar no ângulo certo).
- **Desvio da mesa em relação ao plano de clivagem (a02), "acima de uns 5 a 10 graus"** — **confirmado**. A literatura de facetamento de topázio trabalha com 7°, 7–10° ou 5–15° conforme a fonte, e a faixa da aula está no meio dela. A regra correlata — a mesma proibição vale para a cinta — foi **acrescentada** ao exemplo da kunzita (achado 5).
- **Pleocroísmo do coríndon (a04)** — **confirmado pelo GIA**: no coríndon "o raio ordinário é sempre a mais escura das duas cores", e o coríndon natural é usualmente orientado com o eixo c perpendicular à mesa. A premissa do exemplo (azul-violeta saturado ao longo de c, azul-esverdeado mais fraco de lado) está correta.
- **Classes ópticas (a04)** — uniaxiais (coríndon, quartzo, turmalina, zircão, berilo) dicroicos; biaxiais (iolita, tanzanita, andaluzita, topázio, crisoberilo) tricroicos; isotrópicos (granada, espinélio, diamante, fluorita) sem pleocroísmo: **todas as doze atribuições corretas**.
- **Padrões de zonação (a03)** — faixas na safira, setores na ametista, núcleo no berilo, parti-color e melancia na turmalina: **corretos**.
- **Materiais de clivagem marcada (a02)** — topázio, kunzita/espodumênio, fluorita, diamante, feldspato: **todos corretos** (só a contagem de direções da kunzita estava errada, achado 5).
- **Densidades relativas (a05)** — quartzo ~2,65, coríndon ~4,0, granada 3,8–4,2, turmalina ~3,1: **corretas**.
- **Aritmética do exemplo da a05** — as três opções foram recalculadas com os fatores corrigidos e conferem: A 2,26 → 2,3 ct (5,6%); B 4,15 → 4,2 ct (10,4%); C 5,53 → 5,5 ct (13,8%). O bruto de 8,0 g = 40 ct está certo. O bloco 11 × 9 × 8 mm comporta os três contornos.
- **Kerf de serra (a05), "~0,3 mm a alguns milímetros"** — consistente com o módulo 03 e com a espessura corrente de lâmina de trim saw. **Nenhum achado.**

**Consistência entre as seis aulas:** conferidas as cadeias que atravessam o módulo — leitura (a01) → restrição (a02, a03, a04) → rendimento (a05) → defeito óptico (a06). As remissões cruzadas ("é a aula 05", "é o módulo 08", "é o módulo 14") estão todas corretas e nenhuma promete o que a aula indicada não entrega. A única contradição inter-aula encontrada era a da orientação da faixa de cor (achado 1), interna à a03.

**Consistência com os módulos 01–04:** nenhum dado do módulo 05 colide com valor já fixado nos módulos anteriores. O kerf remete ao módulo 03; a densidade e o índice remetem ao curso de Gemologia por nome, como manda o contrato. Nenhum wikilink aponta para fora do curso.

---

## Correções aplicadas

**Aplicadas em:** 2026-09-03

| claim_id | Sev. | Desfecho | Arquivos alterados |
|---|---|---|---|
| `ZON-FAIXA-MESA-001` | 🔴 | Corrigido | aula-03 |
| `PLE-REN-CUSTO-001` | 🔴 | Corrigido | aula-04 |
| `PLE-EXEM-SAFIRA-001` | 🔴 | Corrigido (claim nova) | aula-04 |
| `REN-FORMULA-PESO-001` | 🔴 | Corrigido | aula-05 |
| `INC-CLIV-KUNZ-001` | 🔴 | Corrigido (claim nova) | aula-02 |
| `REN-FAIXA-TIP-001` | 🟠 | Corrigido, com dois números removidos por falta de fonte | aula-05 |
| `REN-RECUT-PERDA-001` | 🟠 | Corrigido (claim nova) | aula-05 |
| `PLE-CRESC-EIXO-001` | 🟠 | Corrigido (claim nova) | aula-04 |
| `EXT-CONSERTO-CAUSA-001` | 🟠 | Corrigido | aula-06 |
| `EXT-CINCO-CAUSAS-001` | 🟠 | Corrigido (causa 2) | aula-06 |
| `ZON-ORIENT-PATH-001` | 🟠 | Corrigido | aula-03 |
| `PLE-ORIENT-PROC-001` | 🟠 | Corrigido | aula-04 |
| `BRU-IMER-IDX-001` | 🟠 | Corrigido | aula-01 |
| `REN-ESTIM-PROC-001` | 🟠 | Corrigido | aula-05 |
| `BRU-AQUA-ORIENT-001` | ⚪ | Corrigido — reescrito como divergência declarada, sem arbitrar | aula-01 |

**Pendências:** nenhuma. `open_findings` está vazio.

**Material derivado:** nenhum. O módulo 05 não tinha questionário nem baralho quando esta auditoria rodou — que é exatamente o ponto do gate. Nada a propagar, e o `gerador-de-questionarios` recebe o módulo já limpo.

### Custo em palavras das correções

Todas as correções que acrescentavam texto foram **financiadas por corte de redundância local na própria aula**, para não estourar o teto de ~1.600 palavras de LC-02. Nenhuma correção foi comprimida a ponto de perder conteúdo; o que saiu foi repetição entre corpo, "Erros comuns" e "Recap relâmpago". Trechos removidos, por aula:

- **a01** — "Água já resolve a maior parte dos casos" (duplicava o bullet da água no corpo); "é a iluminação de trabalho mais usada" → "é a mais usada"; "e sujam menos que parece"; "Ela não faz parte do projeto final; é descartável" → "Ela é descartável".
- **a03** — a seção "A regra que junta tudo" perdeu as enumerações que o "Recap relâmpago" repete literalmente; três bullets de "Erros comuns" foram compactados; o fecho de *Custo* no exemplo perdeu uma coda circular.
- **a04** — "a mais difícil do curso" (repetido na seção seguinte); a enumeração "cor A na direção 1, cor B na direção 2…"; "Um lote comercial vendido por peso… inverteria a conta" (repetido em duas outras seções); dois bullets de "Erros comuns"/"O que não concluir" compactados.
- **a05** — a caracterização longa do piso da fórmula; o parágrafo de rendimento reescrito mais curto que o original.
- **a06** — "Usar um ângulo de pavilhão 'genérico' num quartzo é o jeito clássico de produzir janela" (repetido em "Erros comuns" e no Recap); a seção "Prever, não remediar" perdeu os parênteses que o Recap repete item a item.

`palavras_corpo` pós-auditoria: **a01 1591 · a02 1592 · a03 1592 · a04 1600 · a05 1597 · a06 1594** — as seis sob o teto. Os rodapés YAML das seis aulas foram ressincronizados.

---

## Encaminhado à revisão didática

Três pontos foram detectados durante a auditoria e **não pertencem a esta skill**:

1. **a04 · a analogia do celofane ensina o modelo mental errado.** "Olhe através de duas folhas de celofane sobrepostas, uma azul e uma amarela: verde" descreve **mistura subtrativa de dois filtros empilhados** — que é precisamente o que o pleocroísmo **não** é. O pleocroísmo é absorção dependente da direção de vibração num único material homogêneo, sem nada empilhado. O aluno que carregar a analogia vai prever que girar a pedra mistura cores, quando o fenômeno é o oposto: cada direção entrega **uma** cor. LC-04 exige analogia antes do termo, mas não uma analogia que precise ser desfeita depois.
2. **a03 · a densidade de correção da aula 03 deslocou o equilíbrio da seção de orientação.** A correção do achado 1 obrigou a reescrever o parágrafo mais importante da aula e, para pagar as palavras, a seção "A regra que junta tudo" ficou bem mais enxuta que as demais. Cabe ao revisor decidir se o fecho ainda organiza o suficiente.
3. **a04 · a aula está exatamente no teto (1600).** Qualquer melhoria didática nela terá de ser financiada por corte, e o texto já passou por uma rodada de compressão nesta auditoria. Prioridade de corte sugerida: o "Recap relâmpago", que é o mais redundante dos seis do módulo.

Nenhum dos três é achado factual e nenhum bloqueia o gate.
