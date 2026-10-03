# Auditoria científica — Módulo 23: Introdução à modelagem numérica geodinâmica

> [!info] **Modo:** `audit-and-fix` · **Profundidade:** `full` · **Data:** 2026-09-19 · **Correções aplicadas em:** 2026-09-19
> **Alvo:** as 7 aulas do módulo 23 auditadas em conjunto, mais o hub do módulo.
> **Veredito: APROVADO.** 15 achados numerados (1 🔴, 13 🟠, 1 🟡), **todos corrigidos**. **0 vermelhos e 0 laranjas em aberto — gate liberado** para questionário e flashcards, observadas as restrições ao gerador registradas mais abaixo.
>
> **Segunda passagem em 2026-09-20** (pontual, escopo restrito às 5 alegações nascidas da divisão didática): **+1 achado 🟠, corrigido**, e 5 itens azuis. **Totais do módulo: 16 achados numerados (1 🔴, 14 🟠, 1 🟡), 16 corrigidos, 0 em aberto; 40 itens azuis; 0 alegações não auditadas.** Gate segue liberado, agora com **oito** restrições ao gerador. Ver a seção final "Passagem pontual pós-divisão".

## Como este módulo foi auditado

Este é o módulo mais quantitativo do curso até aqui, e isso mudou o método. Em vez de confrontar afirmações descritivas contra fontes normativas, a maior parte do esforço foi em **duas frentes que os módulos anteriores não tinham**:

1. **Execução real do código.** Todos os sete blocos de código Python das aulas foram extraídos e **executados** (NumPy 2.5.1), e a saída comparada, dígito a dígito, com a saída declarada no texto. Onde a aula declara uma conferência à mão, a conferência à mão também foi refeita. Nenhuma saída numérica declarada no módulo está errada — ver a seção "Verificado e correto", entradas B5, B9, B14, B19, B24, B25, B30 e B35.
2. **Coerência de notação entre este módulo e o módulo 30 do curso base**, que ele declara como pré-requisito cruzado. Foi aqui que apareceu o único achado 🔴: uma identificação de símbolos que o módulo 30 não sustenta.

O padrão dominante dos achados é revelador e vale enunciar antes da lista.

> [!warning] **Padrão dominante: a simplificação que estava certa na aula anterior e deixou de estar nesta.**
> Nove dos quinze achados têm a mesma forma. A aula enuncia uma versão simplificada de uma relação — a que basta para o caso imediatamente à mão — e não avisa que ela **deixa de valer** exatamente no cenário que o módulo constrói duas aulas adiante. O termo viscoso da equação de Stokes escrito na forma de viscosidade constante, num módulo cuja Aula 06 existe para mostrar que a viscosidade varia por ordens de grandeza (achado 2). A diferença central creditada por um resultado que nas bordas da malha não foi calculado por diferença central (achado 7). A relação dq/dz = A(z) enunciada sem convenção de sinal, três linhas antes de uma conclusão cujo sinal é o oposto (achado 4). Nenhum desses é um erro de fato isolado: todos são **omissões que se tornam erro** na hora em que o aluno aplica a fórmula ao problema realista que o módulo prometeu ensinar. Foi por isso que quase todos ficaram em 🟠 e nenhum em 🟡: não é material envelhecido, é material que arredonda no ponto onde arredondar custa caro.

---

## Achados

### 🔴 1. κ apresentado como o símbolo do decaimento radioativo, e decaimento apresentado como difusão

**claim_id:** `GEODIN-M23-A04-KAPPA-DECAIMENTO-006`
**Tipo:** erro factual + inconsistência interna
**Onde:** Aula 04 · seção "A lei de Fourier e a conservação de calor"
**Estava escrito:** "É comum agrupar k/(ρCp) numa única grandeza, a **difusividade térmica** κ (mesma letra grega já usada na Aula 02 e no Módulo 30, aula 05, para o decaimento radioativo — não é coincidência: ambos os fenômenos, condução de calor e difusão em geral, obedecem à mesma forma matemática de equação)."

**Problema:** duas afirmações falsas encadeadas, e as duas se propagariam.

*Primeira:* κ **não** é a letra usada para o decaimento radioativo em lugar nenhum do currículo. O Módulo 30 do curso base, aula 05, escreve `dN/dt = −λN, onde λ é a constante de decaimento` — verificado no arquivo. E a Aula 02 **deste** módulo escreve, no primeiro parágrafo da primeira seção, "o decaimento radioativo dN/dt = −λN". A Aula 02 não usa κ uma única vez. A frase inventa uma identidade de símbolos que contradiz literalmente as duas aulas que ela cita como apoio.

*Segunda, e pior:* decaimento radioativo e condução de calor **não** "obedecem à mesma forma matemática de equação". O decaimento é uma EDO de primeira ordem no tempo, sem nenhuma derivada espacial, com solução exponencial; a difusão é uma EDP de segunda ordem no espaço. Essa é, ponto por ponto, **a distinção que a Aula 02 inteira existe para construir** — e que a Aula 04 é a primeira a usar. Afirmar a equivalência aqui desfaz o pré-requisito imediatamente anterior.

**Por que é 🔴 e não 🟠:** não é imprecisão de grau. Um flashcard gerado sobre esta frase ensinaria "κ = constante de decaimento" (falso) e "decaimento radioativo é difusão" (falso), e o faria numa aula cujo objetivo declarado é justamente separar EDO de EDP. O erro ataca a espinha conceitual do módulo, não um detalhe dele.

**Correção aplicada:** parágrafo reescrito. κ mantido como difusividade térmica, com sua unidade (m²/s) e com a razão correta de ela reaparecer em toda equação de difusão (calor, espécies químicas, momento) — que é o que de fato dá a elas a mesma forma matemática. Acrescentada a advertência explícita de falso parentesco: λ do decaimento **não** é κ, e decaimento **não** é difusão, com a razão (EDO de primeira ordem no tempo × EDP de segunda ordem no espaço) e a remissão correta à Aula 02.
**Fonte:** Turcotte, D. L. & Schubert, G., *Geodynamics*, 3ª ed. (2014), Cambridge University Press, cap. 4 (definição e unidade da difusividade térmica) · Módulo 30 do curso base, aula 05, linhas 44, 66, 72, 94 e 128 (notação λ, verificada no arquivo). · **Nível:** normativa (livro-texto de referência) + verificação direta no material do curso · **Confiança:** confirmado
**Também aparece em:** só na Aula 04. O Recap da Aula 04 já dizia apenas "κ=k/(ρCp) é a difusividade térmica", sem o parentesco falso, e não precisou de alteração.
**Desfecho:** ✅ **Corrigido**

---

### 🟠 2. Termo viscoso da equação de Stokes escrito na forma que só vale com viscosidade constante

**claim_id:** `GEODIN-M23-A03-STOKESVISCOSO-006` (edita também `GEODIN-M23-A03-REYNOLDS-STOKES-002`)
**Tipo:** omissão que gera erro
**Onde:** Aula 03 · seção "A equação de Navier-Stokes em regime de fluxo lento (Stokes)"; propagado para o Recap e para o bloco de alegações
**Estava escrito:** "−∇P + ∇·(η∇**v**) + ρ**g** = 0"

**Problema:** a forma ∇·(η∇**v**) só coincide com o termo viscoso correto quando **η é constante** (com fluxo incompressível), caso em que ambos se reduzem a η∇²**v**. Para viscosidade variável, o termo é o divergente do tensor de tensão **desviatória**, ∇·[η(∇**v** + (∇**v**)ᵀ)] = ∇·(2ηε̇).

O que torna isto caro neste módulo específico: **a Aula 06 existe para mostrar que η varia por ordens de grandeza com a temperatura.** A aula escreve a equação na forma de viscosidade constante três aulas antes de dedicar uma aula inteira a demonstrar que a viscosidade não é constante. Um aluno que implementasse a equação como escrita produziria um solver silenciosamente errado — e, pior, errado de um jeito que não dispara nenhum dos testes de sanidade que a própria aula ensina (o divergente continuaria zero).

**Correção aplicada:** equação reescrita como −∇P + ∇·[η(∇**v** + (∇**v**)ᵀ)] + ρ**g** = 0 no corpo, na glosa termo a termo e no Recap. Acrescentado parágrafo curto explicando que a combinação simétrica é o tensor de taxa de deformação, que escrevê-la por inteiro é obrigatório porque η varia no espaço, e que a redução a η∇²**v** vale apenas para η constante — nomeando o atalho como uma das fontes clássicas de implementação errada. Bloco de alegações sincronizado; claim novo `STOKESVISCOSO-006` registrado.
**Fonte:** Gerya, T., *Introduction to Numerical Geodynamic Modelling*, 2ª ed. (2019), Cambridge University Press, capítulo sobre a equação de Stokes com viscosidade variável; formulação conservativa em tensão σ'ᵢⱼ = 2ηε̇ᵢⱼ = η(∂vᵢ/∂xⱼ + ∂vⱼ/∂xᵢ) confirmada na literatura corrente de discretização de Stokes variável-viscosidade (arXiv:2509.19061, 2026) · Turcotte & Schubert, *Geodynamics*, 3ª ed., cap. 6 · **Nível:** normativa + revisada por pares · **Confiança:** confirmado
**Também aparece em:** Recap da Aula 03 (corrigido). A Aula 06, que descreve a variação de η, não repete a equação e não precisou de alteração.
**Desfecho:** ✅ **Corrigido**

---

### 🟠 3. "Temperatura negativa é fisicamente impossível" — o critério certo é o princípio do máximo

**claim_id:** `GEODIN-M23-A04-MAXIMOPRINCIPIO-007`
**Tipo:** omissão que gera erro
**Onde:** Aula 04 · seção "Esquema explícito (FTCS)", exemplo trabalhado (caso instável) e Recap
**Estava escrito:** "temperaturas fisicamente impossíveis (negativas, ou muito acima de qualquer produção de calor razoável)" e "uma temperatura **negativa** de −100 no nó central, fisicamente impossível"

**Problema:** −100 °C não tem nada de fisicamente impossível. Uma geoterma sob uma superfície glaciada começa negativa; o módulo 30 do curso base e os módulos de hidrogeologia deste curso trabalham rotineiramente com temperaturas abaixo de zero na escala Celsius. O aluno que sair daqui com a regra "negativo = erro numérico" vai aplicá-la errado na primeira vez que encontrar um perfil térmico de clima frio.

O que de fato torna o valor impossível é outra coisa, e é mais útil: a equação da difusão sem termo de produção obedece ao **princípio do máximo** — a solução em qualquer instante posterior permanece dentro do intervalo entre o menor e o maior valor presentes na condição inicial e nos contornos. No exemplo, esse intervalo é [0, 100]. O valor −100 é impossível porque **escapa do intervalo**, não porque é negativo. E o mesmo critério pega o outro modo de falha (valores acima de 100) com a mesma frase, em vez de com o "muito acima de qualquer produção razoável" que a aula usava e que é vago demais para servir de teste.

**Correção aplicada:** princípio do máximo enunciado explicitamente na seção do esquema explícito, com a justificativa física ("calor nunca se concentra espontaneamente") e a ressalva de que temperatura negativa em Celsius não tem nada de impossível em si. Exemplo trabalhado e Recap reescritos para diagnosticar o valor como "fora do intervalo [0, 100] delimitado pela condição inicial e pelos contornos". Claim `MAXIMOPRINCIPIO-007` acrescentado ao bloco; `EXEMPLO-EXPLICITO-005` sincronizado; Evans (2010) acrescentado às Fontes.
**Fonte:** Evans, L. C., *Partial Differential Equations*, 2ª ed. (2010), American Mathematical Society, capítulo sobre a equação do calor (princípio do máximo) · Press, W. H. et al., *Numerical Recipes*, 3ª ed. (2007), cap. sobre EDPs parabólicas · **Nível:** normativa · **Confiança:** confirmado
**Também aparece em:** Recap da Aula 04 (corrigido).
**Desfecho:** ✅ **Corrigido**

---

### 🟠 4. dq/dz = A(z) enunciado sem convenção de sinal, contra a conclusão tirada na mesma frase

**claim_id:** `GEODIN-M23-A05-SINALFLUXO-008`
**Tipo:** omissão que gera erro
**Onde:** Aula 05 · seção "Litosfera continental: regime estável com produção radiogênica"
**Estava escrito:** "como a taxa de variação do fluxo de calor com a profundidade é exatamente igual à produção local (dq/dz = A(z), consequência direta da lei de Fourier combinada com a conservação de energia em regime estável), toda a produção radiogênica acima de uma profundidade contribui, somada, ao fluxo de calor que emerge na superfície."

**Problema:** o sinal depende inteiramente de uma convenção que a aula não declara, e sob a convenção que o próprio contexto sugere a equação sai com o sinal trocado em relação à conclusão que a segunda metade da frase tira dela.

Com z para baixo — a orientação que a aula usa em toda a parte, inclusive na geoterma — e q_z a componente do fluxo de Fourier nessa mesma direção (q_z = −k dT/dz, portanto um número negativo, já que T cresce com z), vale de fato dq_z/dz = A(z). Mas **q₀, o fluxo de calor superficial que a aula acabou de definir e que a relação de Lachenbruch usa três parágrafos adiante, é o fluxo ascendente reportado como positivo** — e para essa grandeza a relação correta é dq/dz = **−**A(z). É precisamente esse sinal negativo que produz a conclusão enunciada: o fluxo que sobe **cresce** em direção à superfície porque vai acumulando a produção de tudo o que está acima. Escrita sem a convenção, a equação e a conclusão que dela se tira têm sinais opostos.

**Correção aplicada:** convenção fixada explicitamente. A frase agora dá as duas formas — dq_z/dz = A(z) para a componente descendente, dq/dz = −A(z) para o fluxo ascendente positivo, "a grandeza que o geofísico mede e reporta" — com a leitura física do sinal negativo, e fecha registrando que a conclusão prática é a mesma nos dois casos. Claim `SINALFLUXO-008` acrescentado ao bloco de alegações.
**Fonte:** Turcotte & Schubert, *Geodynamics*, 3ª ed. (2014), cap. 4 (balanço de calor em regime estável com produção; q₀ = q_m + integral da produção) · **Nível:** normativa · **Confiança:** confirmado
**Também aparece em:** a relação de Lachenbruch q₀ = q_r + A₀·hr, logo abaixo, já estava correta e não foi tocada — ela é consequência da integração, e o achado é sobre o enunciado do passo intermediário.
**Desfecho:** ✅ **Corrigido**

---

### 🟠 5. "Romper de forma plástica/frágil" — dois termos que a modelagem junta por um motivo que a aula não dá

**claim_id:** `GEODIN-M23-A06-PLASTICOFRAGIL-007`
**Tipo:** nomenclatura / omissão que gera erro
**Onde:** Aula 06 · Objetivo, seção "Um mesmo material, três comportamentos", Recap
**Estava escrito:** "a rocha pode se romper de forma **plástica/frágil** — falhamento, o regime da geologia estrutural clássica"

**Problema:** ruptura por falhamento é comportamento **frágil**. Deformação **plástica**, na mecânica dos materiais, é permanente e **contínua, sem perda de coesão** — literalmente o oposto de uma ruptura. Escrever "romper de forma plástica" como se fossem sinônimos é errado, e é errado num curso de geologia onde o aluno já viu a distinção frágil/dúctil tratada com rigor.

O incômodo é que os dois termos **de fato** viajam juntos na literatura de modelagem geodinâmica — e a aula não diz por quê, que é a parte instrutiva. A razão é mecânica, não terminológica: um meio contínuo, por construção, não sabe abrir uma fratura discreta, então os códigos representam o regime frágil por um **critério de escoamento plástico friccional dependente da pressão** (Mohr-Coulomb ou Drucker-Prager). "Plástico", ali, é o nome do modelo numérico, não do processo geológico. Sem essa distinção, a Aula 07 fica incoerente: ela descreve a cunha crítica como "material plástico friccional (Coulomb)" — usando o termo no sentido de modelo — três parágrafos depois de o aluno ter aprendido que plástico é sinônimo de romper.

**Correção aplicada:** o regime passou a ser nomeado **frágil** no Objetivo, no corpo e no Recap. Acrescentada advertência de vocabulário explicando que plástico ≠ frágil na mecânica dos materiais, e explicando por que a literatura de modelagem usa o critério plástico friccional para representar o frágil num meio contínuo. Claim `PLASTICOFRAGIL-007` acrescentado; `REGIMES-001` sincronizado; Gerya (2019), capítulo de reologia viscoelastoplástica, acrescentado às Fontes.
**Fonte:** Gerya, T., *Introduction to Numerical Geodynamic Modelling*, 2ª ed. (2019), capítulo sobre reologia viscoelastoplástica · Ranalli, G., *Rheology of the Earth*, 2ª ed. (1995), Chapman & Hall · **Nível:** normativa · **Confiança:** confirmado
**Também aparece em:** Aula 07, "material plástico friccional (Coulomb)" na cunha crítica — **não alterado, e agora correto**: com a distinção estabelecida na Aula 06, o uso na Aula 07 passa a ser o uso legítimo do termo (nome do modelo).
**Desfecho:** ✅ **Corrigido**

---

### 🟠 6. "Diferença central de primeira ordem" contradiz a convenção que a Aula 02 estabeleceu

**claim_id:** `GEODIN-M23-A03-ORDEMDIFCENTRAL-007`
**Tipo:** inconsistência interna
**Onde:** Aula 03 · exemplo trabalhado, enunciado
**Estava escrito:** "Calcule numericamente o divergente ∇·**v** = ∂vx/∂x + ∂vz/∂z sobre uma malha, usando diferença central de primeira ordem"

**Problema:** a diferença central para a **primeira derivada**, (f[i+1] − f[i−1])/(2Δx), é de **segunda** ordem de precisão — erro de truncamento proporcional a Δx². A Aula 02, uma aula antes, fixou "ordem" como ordem de **precisão** de forma explícita: "a fórmula de **diferença central de segunda ordem** [...] com erro proporcional a Δz²". Sob a convenção que o próprio módulo acabou de estabelecer, "primeira ordem" está errado. A leitura alternativa (ordem da derivada) só existiria se o módulo não tivesse fixado a outra, e fixou.

O custo prático: o aluno sai com a impressão de que a fórmula do divergente é menos precisa que a fórmula da segunda derivada da aula anterior, quando as duas são igualmente de segunda ordem — e isso é justamente o tipo de comparação que ele vai precisar fazer para escolher uma malha.

**Correção aplicada:** enunciado reescrito para "a diferença central para a primeira derivada (a mesma família de fórmulas do Módulo 30, aula 04 — e, como a fórmula de segunda derivada da Aula 02, ela é de **segunda** ordem de precisão, com erro proporcional a Δx²)". Claim `ORDEMDIFCENTRAL-007` acrescentado ao bloco.
**Fonte:** Chapra, S. C. & Canale, R. P., *Numerical Methods for Engineers*, 7ª ed., capítulo sobre diferenciação numérica · Press et al., *Numerical Recipes*, 3ª ed., capítulo sobre derivação numérica · **Nível:** normativa · **Confiança:** confirmado
**Consistência com o módulo 30 do curso base (checada):** o módulo 30, aula 04, não rotula as fórmulas de diferença finita com ordem nenhuma — diz apenas que "a diferença central costuma ser mais precisa que as outras duas para o mesmo espaçamento". A convenção "ordem = ordem de precisão" é, portanto, **originária deste módulo**, introduzida na Aula 02, e a Aula 03 era o único lugar que a violava.
**Desfecho:** ✅ **Corrigido**

---

### 🟠 7. `np.gradient` não usa diferença central nas bordas, e o resultado foi creditado a ela

**claim_id:** `GEODIN-M23-A03-GRADIENTEBORDA-008`
**Tipo:** omissão que gera erro
**Onde:** Aula 03 · exemplo trabalhado, comentários do código e explicação da saída
**Estava escrito:** comentários `# diferenca central em x` / `# diferenca central em z`; e "`divergente` é uma matriz 5×5 de zeros [...] O resultado é exato [...] porque [...] a diferença central é exata para polinômios de baixo grau"

**Problema:** `np.gradient` aplica diferenças centrais de segunda ordem **apenas nos nós interiores**. Nas duas bordas de cada eixo — onde falta um vizinho, exatamente o problema que a Aula 02 discutiu ao explicar por que uma malha de 5 nós só tem 3 nós interiores — a função recorre a uma diferença **de um lado só**, de primeira ordem por padrão (`edge_order=1`). Numa matriz 5×5, isso é a moldura inteira: **16 dos 25 valores** não foram calculados pela fórmula à qual o texto credita o resultado.

O resultado em si está certo, e foi verificado por execução: a matriz sai toda zero. Mas sai zero por um motivo que o texto não dá — a diferença de um lado só **também** é exata para função linear. Como escrito, a explicação ensina que `np.gradient` é diferença central em toda a malha, o que fará o aluno subestimar o erro nas bordas no primeiro campo não linear que ele derivar, que é exatamente onde a precisão de um modelo costuma se perder.

**Correção aplicada:** comentários do código trocados para `# central no interior, um lado nas bordas`. Acrescentado parágrafo de ressalva explicando o comportamento de `np.gradient`, ligando-o ao problema dos nós de borda já visto na Aula 02, dando o motivo adicional de as bordas também saírem exatamente zero aqui, e fechando com a consequência prática (num campo não linear as bordas são a parte menos precisa — e é por isso que num modelo de verdade é nelas que mora a condição de contorno). Claim `GRADIENTEBORDA-008` acrescentado; `EXEMPLO-DIVERGENTE-005` sincronizado; documentação NumPy acrescentada às Fontes.
**Fonte:** documentação oficial NumPy, `numpy.gradient` (numpy.org/doc/stable/reference/generated/numpy.gradient.html), consultada em 2026-09-19: "second order accurate central differences in the interior points and either first or second order accurate one-sided [...] differences at the boundaries", `edge_order=1` por padrão · **Nível:** normativa (documentação oficial da biblioteca) · **Confiança:** confirmado
**Desfecho:** ✅ **Corrigido**

---

### 🟠 8. "Cisalhamento puro simples" funde os nomes de dois regimes de deformação contrastados

**claim_id:** `GEODIN-M23-A03-PURESHEAR-009`
**Tipo:** nomenclatura
**Onde:** Aula 03 · exemplo trabalhado, enunciado
**Estava escrito:** "o campo de velocidade bidimensional vx = x e vz = −z (um cisalhamento puro simples: o material se estica na direção x na mesma taxa em que se comprime na direção z)"

**Problema:** **cisalhamento puro** (*pure shear*, coaxial) e **cisalhamento simples** (*simple shear*, não coaxial) são dois regimes de deformação formalmente distintos e sistematicamente contrastados na geologia estrutural. Colocar as duas palavras encostadas, nessa ordem, produz um nome que parece um terceiro regime ou uma fusão dos dois. O campo descrito **é** cisalhamento puro (o autor claramente quis dizer "um caso simples de cisalhamento puro"), mas num curso de geologia avançada a colisão de termos é exatamente o tipo de coisa que um aluno memoriza errado.

**Correção aplicada:** reescrito como "um **cisalhamento puro** (*pure shear*) na sua forma mais simples: deformação coaxial, em que o material se estica na direção x na mesma taxa em que se comprime na direção z, sem componente rotacional", com ressalva explícita entre parênteses de que puro e simples são regimes distintos e de que o campo aqui é puro. Claim `PURESHEAR-009` acrescentado; Fossen (2016) acrescentado às Fontes.
**Fonte:** Fossen, H., *Structural Geology*, 2ª ed. (2016), Cambridge University Press, capítulo sobre deformação coaxial e não coaxial · **Nível:** normativa (livro-texto de referência da disciplina) · **Confiança:** confirmado
**Desfecho:** ✅ **Corrigido**

---

### 🟠 9. Citação entre aspas atribuída à Aula 02 que a Aula 02 não contém

**claim_id:** `GEODIN-M23-A05-CITACAOA02-007`
**Tipo:** inconsistência interna
**Onde:** Aula 05 · seção "Litosfera continental: regime estável com produção radiogênica"
**Estava escrito:** "[...] resolúvel por integração direta, exatamente o tipo de simplificação que a Aula 02 descreveu como \"problema que deixa de ser EDP quando se remove a dependência temporal\"."

**Problema:** a frase entre aspas **não aparece na Aula 02**, nem em paráfrase. A Aula 02 discute a distinção EDO/EDP pelo número de variáveis independentes e discute solução analítica × numérica, mas em nenhum momento trata a redução de uma EDP a uma EDO por remoção do termo temporal. A atribuição é fabricada, e as aspas a apresentam como citação literal.

A física está certa — remover ∂T/∂t de fato deixa uma equação de uma só variável independente, que é uma EDO. O defeito é de rastreabilidade: o aluno que voltar à Aula 02 procurando a frase não a encontra, e perde a confiança nas remissões internas do módulo, que são numerosas e, em todos os outros casos verificados, corretas.

**Correção aplicada:** aspas removidas e a remissão reconstruída sobre o que a Aula 02 **de fato** ensina: "É o critério da Aula 02 operando na prática: com o termo temporal eliminado, resta uma única variável independente (a profundidade z), e uma equação de uma só variável independente é, por definição, uma EDO, não uma EDP." Acrescentada a observação de que a notação acompanha (∂ vira d), que é o sinal visível da mudança e reforça o critério da Aula 02.
**Fonte:** verificação direta no arquivo da Aula 02 deste módulo (busca literal da frase e leitura integral das quatro seções) · **Nível:** verificação interna do material · **Confiança:** confirmado
**Desfecho:** ✅ **Corrigido**

---

### 🟠 10. "Conductivo" não existe em português

**claim_id:** `GEODIN-M23-MOD-CONDUTIVO-001`
**Tipo:** nomenclatura
**Onde:** Aula 05 (3 ocorrências: "Ao final você vai conseguir", seção "Interpretando os dois controles lado a lado", bloco de alegações) e Aula 07 (4 ocorrências: seções de extensão e de colisão, constante de tempo térmico, Recap)
**Estava escrito:** "resfriamento conductivo", "processo puramente conductivo e transiente", "relaxamento conductivo", "reequilíbrio conductivo"

**Problema:** o adjetivo derivado de *condução* / *condutor* em português é **condutivo** (fluxo condutivo, transferência condutiva, resfriamento condutivo). "Conductivo" é decalque direto do inglês *conductive* e não é forma portuguesa. Num módulo cujo vocabulário técnico o aluno vai reusar em textos e relatórios, a grafia importada se fixa e viaja.

**Correção aplicada:** as 7 ocorrências substituídas por "condutivo"/"condutiva" nos dois arquivos, incluindo dentro do bloco de alegações auditáveis da Aula 05. Verificado por busca: zero ocorrências restantes no módulo.
**Fonte:** formação regular do adjetivo em português a partir de *condução*/*condutor*; uso corrente na literatura geofísica em português (fluxo condutivo, gradiente condutivo) · **Nível:** normativa (ortografia/terminologia) · **Confiança:** confirmado
**Desfecho:** ✅ **Corrigido**

---

### 🟠 11. Q = 540 kJ/mol creditado a uma fonte que publica outro número

**claim_id:** `GEODIN-M23-A06-QOLIVINAFONTE-006`
**Tipo:** impreciso (atribuição de fonte)
**Onde:** Aula 06 · exemplo trabalhado, enunciado e comentário do código; bloco de alegações
**Estava escrito:** "(Q ≈ 540 kJ/mol, um valor de energia de ativação frequentemente citado na literatura de reologia mantélica)"; comentário `# (ilustrativo, ordem de grandeza da dislocation creep em olivino)`; e, no bloco de alegações, "de ordem de grandeza consistente com Hirth & Kohlstedt (2003)".

**Problema:** o valor 540 kJ/mol não é um valor genérico "de ordem de grandeza": é a calibração específica de **Karato & Wu (1993)** para fluência por deslocamento em olivino seco. A fonte que a aula credita, **Hirth & Kohlstedt (2003), publica 530 ± 4 kJ/mol** — número diferente, e com barra de erro apertada o bastante para que 540 esteja fora dela. Creditar o número a quem publicou outro é defeito de rastreabilidade numa aula cuja tese inteira é que **esse número importa exponencialmente**: se 50 K mudam a viscosidade por um fator 22, 10 kJ/mol de diferença em Q não são detalhe editorial.

**Correção aplicada:** atribuição corrigida para Karato & Wu (1993), com a faixa das calibrações publicadas (~430–560 kJ/mol) e o valor de Hirth & Kohlstedt (530 ± 4 kJ/mol) dados explicitamente, e com a observação de que o valor usado está dentro da faixa mas não é *o* número — a dispersão entre calibrações é ela própria parte do problema que a aula ensina. Comentário do código atualizado. Karato & Wu (1993) acrescentado às Fontes, e Hirth & Kohlstedt (2003) qualificado com seu valor.
**Fonte:** Karato, S. & Wu, P. (1993), "Rheology of the upper mantle: A synthesis", *Science*, 260(5109), 771-778, DOI 10.1126/science.260.5109.771 · Hirth, G. & Kohlstedt, D. (2003), em *Inside the Subduction Factory*, AGU Geophysical Monograph 138, 83-105 (E = 530 ± 4 kJ/mol, dry dislocation creep) · faixa 430–560 kJ/mol entre calibrações publicadas confirmada em busca · **Nível:** revisada por pares · **Confiança:** confirmado
**Desfecho:** ✅ **Corrigido**

---

### 🟠 12. "Uma ordem e meia de grandeza" no bloco de alegações, contra 1,34 calculado

**claim_id:** `GEODIN-M23-A06-EXEMPLO-ARRHENIUS-005`
**Tipo:** inconsistência interna
**Onde:** Aula 06 · bloco de alegações auditáveis (metadados)
**Estava escrito:** "uma diferenca de 50K produz uma diferenca de aproximadamente uma ordem e meia de grandeza na viscosidade efetiva"

**Problema:** log₁₀(22,04) = **1,34** — pouco mais de **uma** ordem de grandeza, não uma e meia. O **corpo** da aula está certo ("mais de uma ordem de grandeza de diferença"); só o bloco de metadados exagera. Isso não é irrelevante: o bloco de alegações é precisamente o que a auditoria seguinte e o gerador de flashcards leem primeiro, de modo que o arredondamento generoso seria o que se propagaria para o card, enquanto a formulação correta ficaria presa no corpo.

**Correção aplicada:** texto do claim corrigido para "pouco mais de UMA ordem de grandeza (log10 de 22.04 = 1.34)", com o valor exato 22.04 substituindo "aproximadamente 22" e com a fonte registrando a conferência por execução (NumPy 2.5.1: 22,0407). Corpo da aula não alterado — já estava correto.
**Fonte:** cálculo aritmético direto, conferido por execução · **Nível:** cálculo reproduzível · **Confiança:** confirmado
**Desfecho:** ✅ **Corrigido**

---

### 🟠 13. "Quase 20%" quando o próprio cálculo da aula dá 20,3%

**claim_id:** `GEODIN-M23-A07-RESTANTE20-006`
**Tipo:** inconsistência interna
**Onde:** Aula 07 · exemplo trabalhado, interpretação geológica
**Estava escrito:** "mas quase 20% da subsidência total ainda está por vir mesmo depois de 100 Ma"

**Problema:** a aula calcula, três linhas acima, fração = 0,7965 aos 100 Ma. O que resta é 1 − 0,7965 = **0,2035**, ou seja, **pouco mais** de 20% — não "quase". A palavra aponta na direção errada (sugere 19-e-pouco), e numa aula de métodos numéricos cuja virtude declarada é conferir cada número à mão, o advérbio que contradiz o próprio resultado três linhas acima é o tipo de deslize que desautoriza o método que a aula está ensinando.

**Correção aplicada:** trocado para "pouco mais de 20% da subsidência total (1 − 0,797 = 0,203)", com a subtração explícita. Claim `EXEMPLO-SUBSIDENCIA-005` sincronizado com os valores exatos (0,3798 e 0,7966) e com o registro da conferência por execução, mais a verificação independente de que τ = 62,8 Ma reproduz τ = a²/(π²κ) do modelo original de McKenzie para a = 125 km e κ = 8×10⁻⁷ m²/s (62,7 Ma).
**Fonte:** cálculo aritmético direto, conferido por execução (NumPy 2.5.1: 0,37980 e 0,79655) · McKenzie, D. (1978), *EPSL* 40(1), 25-32, para os parâmetros de referência · **Nível:** cálculo reproduzível + revisada por pares · **Confiança:** confirmado
**Desfecho:** ✅ **Corrigido**

---

### 🟠 14. Hub do módulo declara código Matplotlib real que não existe em nenhuma aula

**claim_id:** `GEODIN-M23-HUB-MATPLOTLIB-001`
**Tipo:** erro factual (afirmação sobre o próprio material)
**Onde:** `23-modelagem-numerica-geodinamica-modulo.md` · parágrafo de registro após a lista de aulas
**Estava escrito:** "com trechos de código Python reais (NumPy, Matplotlib, SciPy) nos exemplos trabalhados das Aulas 01, 02, 04, 05, 06 e 07"

**Problema:** três imprecisões numa frase só, verificadas bloco a bloco:

- **Matplotlib não aparece em nenhum bloco de código do módulo.** Ele é apresentado e discutido em prosa na Aula 01 (`plt.plot`, `plt.imshow`, `plt.contourf`), mas nenhum dos sete blocos executáveis o importa ou o usa. A afirmação é falsa como escrita.
- A lista de aulas com código **omite a Aula 03**, que tem um bloco de código completo (o teste de divergente com `np.gradient`).
- **SciPy** aparece em uma única aula (a 05, `scipy.special.erf`), não no conjunto que a enumeração sugere.

**Correção aplicada:** parágrafo reescrito listando as sete aulas (inclusive a 03) e separando o que é executado do que é apenas exposto: NumPy nas sete, SciPy só na Aula 05, Matplotlib em nenhuma. A lacuna do Matplotlib foi explicitamente **encaminhada à revisão didática**, com o motivo: a Aula 01 declara entre seus resultados esperados "produzir um gráfico de linha e um mapa de cores com Matplotlib", e nenhuma seção da aula entrega isso. Esse desalinhamento objetivo↔conteúdo é achado didático, não factual, e está registrado abaixo em "Observações fora de escopo".
**Fonte:** inspeção direta dos sete blocos de código das sete aulas · **Nível:** verificação interna do material · **Confiança:** confirmado
**Desfecho:** ✅ **Corrigido** (a parte factual; a lacuna pedagógica fica com a revisão didática)

---

### 🟡 15. Forsyth & Uyeda (1975) citado sob um nome de periódico que só existiria em 1989

**claim_id:** `GEODIN-M23-A07-FORSYTHPERIODICO-007`
**Tipo:** desatualização (citação)
**Onde:** Aula 07 · seção "Forças motoras: slab-pull e ridge-push", lista de Fontes e bloco de alegações
**Estava escrito:** "Forsyth, D. & Uyeda, S. (1975), \"On the relative importance of the driving forces of plate motion\", *Geophysical Journal International*, 43(1), 163-200"

**Problema:** o artigo de 1975 saiu no *Geophysical Journal of the Royal Astronomical Society*. O periódico só foi renomeado *Geophysical Journal International* em **1989**, catorze anos depois. É um anacronismo bibliográfico: quem procurar o artigo sob o nome dado não o encontra nos índices da época nem na capa do volume, embora o encontre hoje na plataforma do OUP, que reindexou o acervo antigo sob o nome atual — o que é, provavelmente, a origem do deslize.

**Por que 🟡 e não 🔵:** o dado não é "não verificável"; é verificável e estava desatualizado. Autores, ano, título, volume e páginas estavam todos corretos — só o nome do periódico pertence a outra época.

**Correção aplicada:** citação corrigida no corpo, nas Fontes e no bloco de alegações para *Geophysical Journal of the Royal Astronomical Society*, 43(1), 163-200, com DOI 10.1111/j.1365-246X.1975.tb00631.x, e com a nota de que o periódico foi renomeado em 1989 e é sob o nome novo que o artigo hoje aparece indexado — preservando a forma antiga em vez de apagá-la, para que o aluno reconheça as duas.
**Fonte:** Wiley Online Library, DOI 10.1111/j.1365-246X.1975.tb00631.x (registro original, *Geophys. J. R. astr. Soc.* 43, 163-200); acervo histórico do GJI no Oxford Academic · **Nível:** base de referência bibliográfica · **Confiança:** confirmado
**Desfecho:** ✅ **Corrigido**

---

## Verificado e correto

Os 35 itens abaixo foram checados. Trinta e tres passaram **sem necessidade de edição nenhuma**; os dois restantes (B11 e B30) registram a **metade verificada** de alegações cujas outras metades viraram os achados 2 e 12. Os doze marcados com ▶ foram verificados por **execução real do código** (NumPy 2.5.1) ou por recálculo independente, não por leitura.

### Aula 01 — Python, Jupyter, NumPy, Matplotlib

| # | O que foi verificado | Veredito | Fonte |
|---|---|---|---|
| B1 | Vetorização do NumPy e delegação a rotinas compiladas (`NUMPY-VETORIZACAO-001`) | correto | Harris, C. R. et al. (2020), *Nature* 585, 357-362, DOI 10.1038/s41586-020-2649-2 |
| B2 | `np.meshgrid` devolve forma `(len(z), len(x))` por padrão (`MESHGRID-002`) | ▶ correto — execução devolve `(3, 4)` | Documentação oficial NumPy, `numpy.meshgrid` |
| B3 | Jupyter: células independentes, origem no IPython, Project Jupyter (`JUPYTER-003`) | correto | Kluyver, T. et al. (2016), IOS Press, 87-90 |
| B4 | Matplotlib como padrão de visualização; `plt.plot`, `plt.imshow`, `plt.contourf` (`MATPLOTLIB-004`) | correto | Hunter, J. D. (2007), *CiSE* 9(3), 90-95 |
| B5 | ▶ Exemplo da geoterma: `T = [10, 260, 510, 760, 1010]` (`EXEMPLO-GEOTERMA-005`) | **exato** — saída executada idêntica à declarada | cálculo reproduzível |

Verificada também, por execução, a segunda situação da Aula 01 (não declarada como alegação): `F = X − Z` dá `[0,1,2,3]` na linha z=0 e `[-2,-1,0,1]` na linha z=2, e o ponto (x=2, z=1) cai de fato na segunda linha, terceira coluna, com valor 1 — como o texto afirma.

### Aula 02 — EDO/EDP e diferenças finitas

| # | O que foi verificado | Veredito | Fonte |
|---|---|---|---|
| B6 | Distinção EDO × EDP pelo número de variáveis independentes (`EDOEDP-001`) | correto | Chapra & Canale, *Numerical Methods for Engineers*, 7ª ed. |
| B7 | (T[i+1] − 2T[i] + T[i−1])/Δz², erro ∝ Δz², **exata para polinômios até grau três** (`DIFCENTRAL2-002`) | correto — o termo de erro depende da quarta derivada, nula até grau 3 | Chapra & Canale, 7ª ed.; Press et al., *Numerical Recipes*, 3ª ed. |
| B8 | Discretização de EDP → sistema linear por nó → Gauss / Gauss-Seidel (`DISCRETIZACAO-SISTEMA-003`) | correto | Gerya (2019), cap. introdutório; Chapra & Canale, 7ª ed. |
| B9 | ▶ Exemplo: `d2T = [2. 2. 2.]` para T(z)=z², Δz=1 (`EXEMPLO-DIFCENTRAL-004`) | **exato** — execução confirma, e as três conferências à mão do texto (i=1, 2, 3) estão todas certas | cálculo reproduzível |

### Aula 03 — Mecânica do contínuo

| # | O que foi verificado | Veredito | Fonte |
|---|---|---|---|
| B10 | ∂ρ/∂t + ∇·(ρv) = 0; incompressibilidade → ∇·v = 0, campo solenoidal (`CONTINUIDADE-001`) | correto | Turcotte & Schubert, *Geodynamics*, 3ª ed., cap. 6 |
| B11 | Número de Reynolds do manto da ordem de 10⁻²⁰ ou menor (metade de `REYNOLDS-STOKES-002`) | ▶ correto — recalculado: ρ=3300 kg/m³, v≈10⁻⁹ m/s, L=10⁶ m, η=10²¹ Pa·s → Re = 3,3×10⁻²¹ | Turcotte & Schubert, 3ª ed., cap. 6 |
| B12 | Lagrangiano × euleriano; marcadores lagrangianos em malha euleriana (*particle-in-cell*) (`LAGRANGE-EULER-003`) | correto | Gerya (2019), caps. de discretização e advecção; Kronbichler et al. (2012), *GJI* 191(1), 12-29 (ASPECT) |
| B13 | Malha escalonada evita oscilação espúria de pressão em malha colocalizada (`MALHA-ESCALONADA-004`) | correto | Gerya (2019), cap. de discretização da equação de Stokes |
| B14 | ▶ Divergente de (vx=x, vz=−z) numericamente nulo (`EXEMPLO-DIVERGENTE-005`) | **exato** — execução devolve matriz 5×5 de zeros exatos (não apenas ruído de ponto flutuante). Ressalva sobre *por que* as bordas também zeram: achado 7 | cálculo reproduzível + doc. NumPy |
| — | Validade da hipótese do contínuo quando a escala do fenômeno supera a da estrutura da rocha | correto (não declarada como alegação) | Turcotte & Schubert, 3ª ed., caps. 2 e 6 |

### Aula 04 — Calor e esquemas numéricos

| # | O que foi verificado | Veredito | Fonte |
|---|---|---|---|
| B15 | q = −k∇T e ρCp ∂T/∂t = k∂²T/∂z² + A − ρCp v∂T/∂z (`FOURIER-CONSERVACAO-001`) | correto, com A em W/m³ | Turcotte & Schubert, 3ª ed., cap. 4 |
| B16 | FTCS: T[i,n+1] = T[i,n] + r(T[i+1,n] − 2T[i,n] + T[i−1,n]), r = κΔt/Δz² (`ESQUEMA-EXPLICITO-002`) | correto, inclusive o termo de produção A·Δt/(ρCp) acrescentado no corpo | Press et al., 3ª ed.; Gerya (2019) |
| B17 | Estabilidade de von Neumann: r ≤ 1/2 em 1D (`ESTABILIDADE-VONNEUMANN-003`) | correto | Press et al., 3ª ed., cap. de EDPs parabólicas |
| B18 | BTCS: sistema **tridiagonal** por passo, algoritmo de Thomas, **incondicionalmente estável** (`ESQUEMA-IMPLICITO-004`) | correto, inclusive a ressalva de que estabilidade não é precisão | Press et al., 3ª ed., caps. de sistemas tridiagonais e de EDPs parabólicas |
| B19 | ▶ Exemplo: `[0,25,50,25,0]` (r=0,25) e `[0,100,−100,100,0]` (r=1,0) (`EXEMPLO-EXPLICITO-005`) | **exato** — execução idêntica; as seis conferências à mão do texto estão todas certas; conservação de energia (soma 100 → 100) confirmada | cálculo reproduzível |
| — | Equação implícita com as três incógnitas do passo novo, e a identificação do sistema com o Módulo 30 aula 02 | correto | Press et al., 3ª ed. |

### Aula 05 — Calor na litosfera

| # | O que foi verificado | Veredito | Fonte |
|---|---|---|---|
| B20 | T(z,t) = T_m·erf(z/(2√(κt))); isoterma ∝ √idade, fluxo ∝ 1/√idade (`SEMIESPACO-001`) | correto | Turcotte & Schubert, 3ª ed., cap. 4 |
| B21 | Ajuste bom até ~70-80 Ma; achatamento; modelo de placa e GDH1 (`ACHATAMENTO-002`) | correto, e as duas referências conferem: Parsons & Sclater (1977), *JGR* 82(5), 803-827; Stein & Stein (1992), *Nature* 359, 123-129 | as próprias |
| B22 | A(z) = A₀e^(−z/hr) → q₀ = q_r + A₀·hr, com q_r o fluxo reduzido (`LACHENBRUCH-003`) | correto; referência confere: Lachenbruch (1970), *JGR* 75(17), 3291-3300 | a própria; Turcotte & Schubert, cap. 4 |
| B23 | Oceânica = transiente e dependente de idade; continental = estável, produção + fluxo de base (`CONTROLES-OCEANICA-CONTINENTAL-004`) | correto | Turcotte & Schubert, 3ª ed., cap. 4 |
| B24 | ▶ Exemplo erf: η ≈ 0,345 e T ≈ 505 °C (`EXEMPLO-ERF-005`) | **exato** — execução dá η = 0,34472 e T = **505,03 °C**. A interpolação manual da tabela de erf feita no texto (0,374) também está certa | cálculo reproduzível |
| B25 | ▶ Lachenbruch: 2,5 µW/m³ × 10 km = 25 mW/m²; q₀ = 55 mW/m²; faixa típica 40-70 mW/m² (`EXEMPLO-LACHENBRUCH-006`) | **exato**, inclusive a conversão de unidades | cálculo reproduzível; Turcotte & Schubert, cap. 4 |

### Aula 06 — Reologia

| # | O que foi verificado | Veredito | Fonte |
|---|---|---|---|
| B26 | Tempo de Maxwell (η/μ) da ordem de centenas a milhares de anos para o manto (parte de `REGIMES-001`) | ▶ correto — recalculado: η=10²¹ Pa·s, μ=7×10¹⁰ Pa → 453 anos | Turcotte & Schubert, 3ª ed., cap. 7 |
| B27 | Difusão: n=1, newtoniana, dependente de tamanho de grão, favorecida a baixa tensão / alta T / grão fino. Deslocamento: n≈3-4, olivino ≈3,5, independente de tamanho de grão (`DIFUSAO-DESLOCAMENTO-002`) | correto, inclusive o enquadramento de "temperaturas altas" para a difusão, que é a formulação padrão dos mapas de mecanismo de deformação (fluência Nabarro-Herring a alta T e baixa tensão) | Karato (2008); Hirth & Kohlstedt (2003), AGU Monograph 138, 83-105 |
| B28 | ε̇ = A·σⁿ·exp(−Q/RT) e η_eff = σ/(2ε̇) = (1/2A)·σ^(1−n)·exp(+Q/RT) (`ARRHENIUS-003`) | correto — a inversão algébrica foi refeita, inclusive a troca de sinal do expoente e a leitura física (mais quente ⇒ menos viscoso) | Turcotte & Schubert, cap. 7; Ranalli (1995) |
| B29 | Quartzo (crosta, mais fraco) × olivino (manto, mais resistente); envelope de resistência em camadas (`REOLOGIA-CROSTA-MANTO-004`) | correto | Ranalli (1995), cap. de perfis de resistência litosférica |
| B30 | ▶ Exemplo Arrhenius: Q/RT₁ = 64,95; Q/RT₂ = 61,86; razão ≈ 22 (`EXEMPLO-ARRHENIUS-005`, núcleo aritmético) | **exato** — execução dá 64,9507 / 61,8578 / **22,0407**; as três conferências à mão do texto conferem. Só a glosa "ordem e meia" foi corrigida: achado 12 | cálculo reproduzível |

### Aula 07 — Extensão e colisão

| # | O que foi verificado | Veredito | Fonte |
|---|---|---|---|
| B31 | β = espessura original / espessura final; S(t)/S_max = 1 − e^(−t/τ); τ de 50-65 Ma para litosfera de ~125 km (`MCKENZIE-001`) | ▶ correto, e **verificado por derivação independente**: τ = a²/(π²κ) com a = 125 km e κ = 8×10⁻⁷ m²/s dá **62,7 Ma**, que é o τ = 62,8 Ma usado no exemplo | McKenzie (1978), *EPSL* 40(1), 25-32; Allen & Allen (2013) |
| B32 | Orógeno colisional aquece antes de esfriar; trajetória P-T-t de enterramento, aquecimento, exumação (`OROGENO-AQUECE-002`) | correto; referência confere: England & Thompson (1984), *J. Petrology* 25(4), 894-928 | a própria |
| B33 | Slab-pull ~10¹³ N/m, ridge-push ~10¹² N/m, slab-pull dominante quando presente (`FORCAS-PLACA-003`, valores) | correto — ordens de grandeza conferem com a literatura clássica; o nome do periódico da referência é o achado 15, não o valor | Turcotte & Schubert, 3ª ed., cap. 6; Forsyth & Uyeda (1975) |
| B34 | Cunha crítica: material friccional de Coulomb sobre descolamento basal; taper = mergulho topográfico + mergulho do descolamento; abaixo do crítico deforma internamente, acima avança rígida (`CUNHA-CRITICA-004`) | correto; referência confere: Davis, Suppe & Dahlen (1983), *JGR* 88(B2), 1153-1172 | a própria; Dahlen (1990), *Annu. Rev.* 18, 55-99 |
| B35 | ▶ Exemplo de subsidência: 0,380 aos 30 Ma e 0,797 aos 100 Ma (`EXEMPLO-SUBSIDENCIA-005`, núcleo aritmético) | **exato** — execução dá 0,37980 e 0,79655; as decomposições manuais de exponencial feitas no texto conferem. Só o "quase 20%" foi corrigido: achado 13 | cálculo reproduzível |

> [!note] **Nota sobre as duas alegações declaradas que passaram só pela metade**
> `GEODIN-M23-A03-REYNOLDS-STOKES-002` e `GEODIN-M23-A06-EXEMPLO-ARRHENIUS-005` foram **parcialmente** aprovadas. O número de Reynolds (B11) e a aritmética de Arrhenius (B30) passaram intactos e estão registrados acima como azuis; mas cada uma dessas alegações carregava uma segunda metade — a forma do termo viscoso de Stokes e a glosa "uma ordem e meia de grandeza" — que precisou de correção, e essas metades estão nos achados 2 e 12. Contagem final: **35 entradas azuis**, das quais 33 correspondem a alegações aprovadas por inteiro.

---

## Verificação cruzada com o módulo 30 do curso base

Este módulo declara, no hub e nos cabeçalhos das Aulas 02 e 04, dependência do **Módulo 30 do curso base** (*Métodos numéricos para geociências*), já fechado e aprovado. Todas as remissões foram conferidas contra os arquivos daquele módulo:

| Remissão feita aqui | Confere? |
|---|---|
| Módulo 30 aula 01 — erro de truncamento e arredondamento | ✅ o conteúdo está lá, e o uso aqui (erro ∝ Δz², ruído de ponto flutuante) é coerente |
| Módulo 30 aula 02 — eliminação de Gauss e Gauss-Seidel | ✅ está lá; a ponte "EDP → malha → sistema linear" construída na Aula 02 daqui é legítima |
| Módulo 30 aula 04 — diferenças finitas progressiva, regressiva e central | ✅ está lá. **Ressalva:** o módulo 30 não rotula as fórmulas com ordem de precisão; a convenção "ordem = ordem de precisão" nasce na Aula 02 **deste** módulo. Isso é coerente (o módulo avançado pode ser mais formal), mas foi a origem do achado 6 |
| Módulo 30 aula 05 — EDO do decaimento radioativo | ⚠️ **origem do achado 1.** O módulo 30 escreve `dN/dt = −λN` com λ, nunca κ, e trata o decaimento como EDO com solução exponencial — nunca como difusão |
| Aula 02 daqui: "o Módulo 30 deliberadamente deixou [as EDPs] para este módulo (ver a aula 05 daquele módulo, seção final)" | ✅ confere — a aula 05 do módulo 30 de fato distingue o resfriamento de parâmetro concentrado (lei de Newton) da equação de difusão completa, declarando esta última fora do seu escopo |

**Conclusão:** uma única inconsistência de notação entre os cursos, corrigida (achado 1). O restante da ponte entre os dois módulos é sólido e bem construído.

---

## Correções aplicadas

**Aplicadas em:** 2026-09-19 (mesma data do levantamento; passagem única)

| # | claim_id | Sev. | Desfecho | Arquivos alterados |
|---|---|---|---|---|
| 1 | `GEODIN-M23-A04-KAPPA-DECAIMENTO-006` | 🔴 | Corrigido | aula-04 |
| 2 | `GEODIN-M23-A03-STOKESVISCOSO-006` | 🟠 | Corrigido | aula-03 |
| 3 | `GEODIN-M23-A04-MAXIMOPRINCIPIO-007` | 🟠 | Corrigido | aula-04 |
| 4 | `GEODIN-M23-A05-SINALFLUXO-008` | 🟠 | Corrigido | aula-05 |
| 5 | `GEODIN-M23-A06-PLASTICOFRAGIL-007` | 🟠 | Corrigido | aula-06 |
| 6 | `GEODIN-M23-A03-ORDEMDIFCENTRAL-007` | 🟠 | Corrigido | aula-03 |
| 7 | `GEODIN-M23-A03-GRADIENTEBORDA-008` | 🟠 | Corrigido | aula-03 |
| 8 | `GEODIN-M23-A03-PURESHEAR-009` | 🟠 | Corrigido | aula-03 |
| 9 | `GEODIN-M23-A05-CITACAOA02-007` | 🟠 | Corrigido | aula-05 |
| 10 | `GEODIN-M23-MOD-CONDUTIVO-001` | 🟠 | Corrigido | aula-05, aula-07 |
| 11 | `GEODIN-M23-A06-QOLIVINAFONTE-006` | 🟠 | Corrigido | aula-06 |
| 12 | `GEODIN-M23-A06-EXEMPLO-ARRHENIUS-005` | 🟠 | Corrigido | aula-06 |
| 13 | `GEODIN-M23-A07-RESTANTE20-006` | 🟠 | Corrigido | aula-07 |
| 14 | `GEODIN-M23-HUB-MATPLOTLIB-001` | 🟠 | Corrigido | modulo.md |
| 15 | `GEODIN-M23-A07-FORSYTHPERIODICO-007` | 🟡 | Corrigido | aula-07 |

**Arquivos tocados:** `aula-03`, `aula-04`, `aula-05`, `aula-06`, `aula-07`, `modulo.md`. As **Aulas 01 e 02 foram auditadas e não precisaram de nenhuma edição** — passaram integralmente, inclusive nos exemplos executados.

**Alegações novas registradas nos blocos de metadados das aulas (8):** `A03-STOKESVISCOSO-006`, `A03-ORDEMDIFCENTRAL-007`, `A03-GRADIENTEBORDA-008`, `A03-PURESHEAR-009`, `A04-KAPPA-DECAIMENTO-006`, `A04-MAXIMOPRINCIPIO-007`, `A05-SINALFLUXO-008`, `A06-PLASTICOFRAGIL-007`. O módulo passa de **35 para 43 alegações auditáveis declaradas em arquivo**.

**Fontes acrescentadas ao módulo (6):**
- Evans, L. C. (2010), *Partial Differential Equations*, 2ª ed., American Mathematical Society — princípio do máximo (aula 04)
- Fossen, H. (2016), *Structural Geology*, 2ª ed., Cambridge University Press — cisalhamento coaxial × não coaxial (aula 03)
- Documentação oficial NumPy, `numpy.gradient` — comportamento nas bordas (aula 03)
- Karato, S. & Wu, P. (1993), "Rheology of the upper mantle: A synthesis", *Science* 260(5109), 771-778, DOI 10.1126/science.260.5109.771 — origem de Q = 540 kJ/mol (aula 06)
- Gerya, T. (2019), cap. de reologia viscoelastoplástica — critério plástico friccional para o frágil (aula 06)
- Forsyth & Uyeda (1975) com periódico e DOI corretos (aula 07)

**Pendências:** nenhuma. Nenhum achado 🔵 ou ⚪ foi levantado (ver abaixo).

**Material derivado a propagar:** nenhum existia no momento da auditoria — sem questionário, sem baralho de flashcards, sem glossário. **Não há card já importado no Anki a corrigir à mão.**

> [!note] **Por que não há nenhum achado 🔵 (sem fonte) nem ⚪ (controverso)**
> Não é omissão. Este módulo é quantitativo e didaticamente conservador: ele ensina resultados estabelecidos há décadas (Fourier, Stokes, von Neumann, McKenzie, Lachenbruch, Davis-Suppe-Dahlen) e, onde a literatura de fato diverge, **a própria aula já declara a divergência** — a Aula 05 apresenta o modelo de semi-espaço e imediatamente registra o problema do achatamento e os modelos de placa concorrentes; a Aula 06 qualifica os parâmetros de fluência como "ilustrativos" e "calibrações experimentais". Não há, no módulo, afirmação específica que a auditoria não tenha conseguido confirmar, nem posição em disputa apresentada como consenso fechado. O único ponto que chegou perto foi a energia de ativação do olivino — e ele virou 🟠 de atribuição (achado 11), não ⚪, porque a dispersão entre calibrações é um fato bem documentado, não uma controvérsia aberta.

---

## Gate de avaliação

> [!success] **GATE LIBERADO** para `gerador-de-questionarios` e `gerador-de-flashcards`.
> 0 achados 🔴 e 0 🟠 em aberto. Os 15 achados numerados foram todos corrigidos na mesma passagem. Nenhuma alegação do módulo permanece não auditada (43 declaradas em arquivo + 6 rastreadas só no relatório = 49, todas com desfecho).

### Restrições ao gerador (7)

Estes são os pontos em que o material **antes** dizia outra coisa. Uma questão ou um card que reproduza a formulação antiga estará errado mesmo parecendo consistente com a memória de quem leu o módulo cedo demais.

1. **κ NÃO é a constante de decaimento, e decaimento NÃO é difusão** (vermelho 1). Não gerar item que identifique κ com λ, nem item cuja resposta correta afirme que condução de calor e decaimento radioativo "têm a mesma forma de equação". A distinção **é** boa questão — mas o gabarito é que decaimento é EDO de primeira ordem no tempo e difusão é EDP de segunda ordem no espaço.
2. **O termo viscoso de Stokes é ∇·[η(∇v + (∇v)ᵀ)]** (laranja 2). Não gerar item cuja resposta correta seja ∇·(η∇v) ou η∇²v **sem** a qualificação "para viscosidade constante". Boa questão possível: por que a forma simplificada não serve num modelo cuja viscosidade depende da temperatura.
3. **O critério de instabilidade é o princípio do máximo, não o sinal negativo** (laranja 3). Não gerar item cuja resposta correta seja "a temperatura ficou negativa, logo é impossível". O gabarito é "o valor saiu do intervalo delimitado pela condição inicial e pelos contornos".
4. **dq/dz = A(z) só vale com a convenção declarada** (laranja 4). Não cobrar o sinal sem dar a convenção no enunciado. Se cobrar, a resposta para o fluxo **ascendente** (o que se mede e se reporta) é dq/dz = −A(z).
5. **Ruptura é frágil; "plástico" é o nome do modelo numérico** (laranja 5). Não gerar item que trate plástico e frágil como sinônimos. A distinção rende boa questão de aplicação: por que um código de meio contínuo precisa de um critério plástico friccional para representar falhamento.
6. **A diferença central para a primeira derivada é de segunda ordem** (laranja 6). Não gerar item cuja resposta correta seja "primeira ordem" para a fórmula (f[i+1] − f[i−1])/(2Δx).
7. **`np.gradient` não é diferença central nas bordas** (laranja 7). Não gerar item que afirme que a função aplica diferença central em toda a malha. Se o comportamento de borda virar questão, o gabarito é: central de segunda ordem no interior, um lado só (primeira ordem, `edge_order=1`) nas bordas.

**Além disso, ao gerar:** o número Q = 540 kJ/mol deve ser atribuído a Karato & Wu (1993), não a Hirth & Kohlstedt (2003); a razão de viscosidades do exemplo é 22,04, ou seja **pouco mais de uma** ordem de grandeza (log₁₀ = 1,34), nunca "uma ordem e meia"; e a fração de subsidência remanescente aos 100 Ma é **pouco mais** de 20%.

---

## Recomendação de formato do questionário

**Recomendado: 3 questionários parciais + 1 final cumulativo.**

O módulo tem **7 aulas**, acima do limiar de ~5-6 do plugin — o mesmo tamanho do Módulo 19, que usou 3 parciais + final, e do Módulo 14, que também usou parciais. Mas o argumento decisivo aqui não é a contagem: é que **este módulo tem três camadas genuinamente distintas**, e um questionário único não conseguiria testar nenhuma delas com profundidade suficiente sem inchar.

| Parcial | Aulas | Eixo | Objetivo |
|---|---|---|---|
| **Parcial 1 — a ferramenta e o método numérico** | 01-02 | Python/NumPy vetorizado, EDO × EDP, diferenças finitas, ordem de precisão | `oa01`, início de `oa02` |
| **Parcial 2 — as equações governantes e sua solução** | 03-04 | Continuidade, Stokes, lagrangiano/euleriano, calor, FTCS/BTCS, estabilidade | `oa02`, início de `oa03` |
| **Parcial 3 — a litosfera real** | 05-07 | Geotermas oceânica e continental, reologia, extensão e colisão | `oa03`, `oa04` |
| **Final cumulativo** | 01-07 | Integração | os quatro |

**Por que esse corte, e não outro:** os cortes 02│03 e 04│05 são as duas únicas descontinuidades reais do módulo. Em 02│03 o objeto muda de *método* para *física*; em 04│05 muda de *equação genérica* para *litosfera concreta com números medidos*. Cortar em qualquer outro ponto separaria coisas que a aula seguinte usa na primeira linha.

**O final cumulativo é obrigatório aqui**, e por um motivo que este módulo tem mais que os anteriores: a cadeia de dependência **calor → reologia → deformação** só existe atravessando as três parciais. A pergunta central do módulo — por que um erro pequeno no campo térmico da Aula 04 destrói a viscosidade da Aula 06 e, com ela, o modelo de extensão da Aula 07 — não cabe em parcial nenhuma. Pelo menos duas questões do final devem ser de **integração explícita**: uma ligando estabilidade numérica (a04) a sensibilidade exponencial da viscosidade (a06); outra ligando geoterma (a05) a resistência litosférica e localização da ruptura (a06-a07).

**Se a revisão didática dividir alguma aula:** a recomendação **não muda**. O corte em três blocos é conceitual, não aritmético — uma divisão por carga cognitiva acrescenta uma parte dentro de um bloco existente, sem criar fronteira nova. (Uma divisão da Aula 04, a candidata mais provável, ficaria inteira dentro da Parcial 2.)

---

## Observações fora de escopo (para a revisão didática)

Não são achados factuais. Ficam registrados aqui porque apareceram durante a leitura integral.

1. **A Aula 01 promete Matplotlib e não entrega.** Entre os resultados esperados: "produzir um gráfico de linha e um mapa de cores com Matplotlib". Nenhuma seção da aula, nem nenhum dos dois exemplos trabalhados, contém uma linha de Matplotlib. É desalinhamento objetivo↔conteúdo — o mais nítido do módulo. A parte factual (o hub afirmava que havia código Matplotlib) já foi corrigida no achado 14; a lacuna pedagógica é da revisão didática.
2. **Frase quebrada na Aula 01**, seção "Por que geodinâmica precisa de modelagem numérica": "É exatamente esse é o fio condutor deste módulo" — verbo duplicado.
3. **Concordância na Aula 07**, primeira seção: "a coluna afinada é mais leve, e a superfície subsidem quase instantaneamente" — deveria ser "subside".
4. **A Aula 04 é a mais pesada do módulo e ficou mais pesada com esta auditoria.** Já declarava ~30 min e 2.080 palavras, no teto do plugin; as correções dos achados 1 e 3 acrescentaram o parágrafo do princípio do máximo e reescreveram o da difusividade. É a primeira candidata a divisão em Parte 1 / Parte 2, com corte natural visível entre a formulação física (Fourier, conservação, advecção) e os dois esquemas numéricos.
5. **A Aula 03 também cresceu** (achados 2, 7 e 8 acrescentaram um parágrafo sobre o tensor de taxa de deformação e outro sobre o comportamento de `np.gradient`). Declarava ~29 min; vale remedir.
6. **Densidade tripla nas aulas com código.** Aulas 04, 05, 06 e 07 pedem, simultaneamente, sintaxe Python, um conceito matemático novo e uma interpretação geológica. É o risco de sobrecarga específico deste módulo, e não existia nos módulos 20-22.
7. **A comparação final da Aula 05** ("fluxo de calor de base e produção radiogênica crustal bem menores do que o calor 'represado' na litosfera oceânica jovem") compara um fluxo com um calor armazenado. A conclusão está certa, mas a formulação mistura grandezas de dimensões diferentes.

---

## Adendo — o módulo foi dividido depois desta auditoria (2026-09-19)

> [!warning] Leia isto antes de usar os nomes de aula deste relatório
> A revisão didática rodou logo depois desta auditoria, no mesmo dia, e **dividiu duas aulas**. O módulo passou de **7 para 9**. Esta auditoria **não foi reaberta**: os 15 achados não foram renumerados, revertidos nem reavaliados, e as 15 correções continuam aplicadas. Mas os números de aula citados acima são os de **antes** da divisão.

| Aula citada neste relatório | Onde o conteúdo está hoje |
|---|---|
| Aula 03 (mecânica do contínuo) | **Aula 03** (continuidade e Stokes) + **Aula 04** (malhas, lagrangiano/euleriano) |
| Aula 04 (calor) | **Aula 05** (Fourier, três termos, difusividade) + **Aula 06** (FTCS, estabilidade, BTCS) |
| Aula 05 | **Aula 07** |
| Aula 06 | **Aula 08** |
| Aula 07 | **Aula 09** |
| Aulas 01 e 02 | inalteradas |

**Os `claim_id` não foram renumerados**, deliberadamente: um `GEODIN-M23-A03-…` pode hoje estar declarado na Aula 04, e um `GEODIN-M23-A04-…` na Aula 06. Renumerá-los quebraria a rastreabilidade com este relatório e com o manifesto. Cada aula afetada traz a nota `nota_alegacoes_migradas` no seu bloco de metadados. No `.json`, o campo `affected_files` de cada achado foi preservado com os caminhos da época, e o caminho atual está no campo irmão `affected_files_pos_divisao`.

### As 15 correções foram preservadas — conferidas uma a uma

As quatro que mais corriam risco na divisão:

- **Vermelho 1 (`KAPPA-DECAIMENTO-006`)** ficou integral na nova **Aula 05** e **ganhou um callout próprio**, ficando mais visível do que estava enterrado no meio de um parágrafo.
- **Laranja 3 (`MAXIMOPRINCIPIO-007`)** acompanhou o esquema explícito para a nova **Aula 06** e **ganhou seção própria** — "A condição de estabilidade, e o que significa 'impossível'". O formato de aula única não dava espaço para isso.
- **Laranjas 2, 6, 7 e 8** (`STOKESVISCOSO`, `ORDEMDIFCENTRAL`, `GRADIENTEBORDA`, `PURESHEAR`) ficaram integrais na nova **Aula 03**, palavra por palavra.
- **Laranja 4 (`SINALFLUXO-008`)** está integral na nova **Aula 07**, dentro do "Passo 1" do parágrafo que a revisão didática reestruturou por densidade.

### Quatro alegações novas ainda não auditadas

Nasceram na divisão e nas correções didáticas, **depois** desta auditoria. Nenhuma é um achado; nenhuma contradiz correção aplicada; **o gate continua liberado.**

| claim_id | Aula | O que é | Verificação já feita |
|---|---|---|---|
| `GEODIN-M23-A03-MALHA-COLOCALIZADA-010` | 04 | O *mecanismo* pelo qual a oscilação de pressão de nó em nó fica invisível numa malha colocalizada. Que a malha escalonada evita o problema já estava auditado (B13); o mecanismo é novo. | nenhuma contra fonte; ancorada em Gerya (2019) e Patankar (1980) |
| `GEODIN-M23-A03-EXEMPLO-ESCALONADA-011` | 04 | Aritmética dos pontos escalonados; n nós dão n−1 centros de célula. | **conferida por execução** |
| `GEODIN-M23-A04-EXEMPLO-PROPRIEDADES-008` | 05 | k = 2,7 W/(m·K), ρ = 2.700 kg/m³, Cp = 1.000 J/(kg·K) → κ = 1,0×10⁻⁶ m²/s e q = 54 mW/m². | **aritmética conferida por execução**; os dois *resultados* coincidem com valores que esta auditoria já verificou (B24 e B25). Falta verificar a **representatividade dos três parâmetros de entrada** — é a única das quatro com valores medidos, e a de maior prioridade |
| `GEODIN-M23-A01-MATPLOTLIB-API-006` e `-EXEMPLO-MAPA-007` | 01 | Sintaxe do Matplotlib e previsão dos extremos do campo no mapa de cores. Entraram para fechar o achado didático 🔴 — a aula prometia Matplotlib e não tinha uma linha dele. | **sintaxe conferida contra a documentação oficial** (`origin` de `imshow`, `label` de `colorbar`). O código **não pôde ser executado**: Matplotlib não está instalado no ambiente, ao contrário do NumPy |

**Recomendação:** uma passagem pontual do `auditor-cientifico` sobre as quatro, com prioridade para `EXEMPLO-PROPRIEDADES-008`. → **Executada em 2026-09-20. Ver a seção "Passagem pontual pós-divisão" no fim deste relatório.**

### A recomendação de questionário foi confirmada

As duas divisões caíram **dentro** dos blocos que este relatório já havia proposto — 03│04 e 05│06 estão ambos na Parcial 2. O mapeamento passa a **01-02 / 03-06 / 07-09**, e as fronteiras conceituais (02│03 e 06│07) são exatamente as mesmas. A previsão registrada acima em "Se a revisão didática dividir alguma aula: a recomendação não muda" se confirmou.

---

---

## Passagem pontual pós-divisão (2026-09-20)

> [!info] **Escopo estritamente limitado**
> Esta é uma **segunda passagem**, restrita às **cinco alegações novas** que nasceram na divisão didática de 2026-09-19 e que a auditoria de 2026-09-19 — anterior a elas — não podia ter visto. **Os 15 achados numerados não foram reabertos, reavaliados nem renumerados, e as 15 correções continuam aplicadas.** Nenhum `claim_id` foi reciclado.
>
> **Resultado: as 5 alegações foram verificadas e nenhuma estava errada (itens azuis P2 a P6). 1 achado 🟠 novo — o de número 16 —, corrigido na mesma passagem.** Nenhum vermelho. **O gate continua liberado.**
>
> O 🟠 não contradiz nenhum dos cinco itens azuis: ele é sobre uma **ressalva ausente** ao lado de um valor que está correto, não sobre um valor errado.

### O que mudou no ambiente, e por que isso importa

A revisão didática deixou duas alegações pendentes por uma razão puramente operacional: **o Matplotlib não estava instalado**, e ela se recusou — corretamente — a declarar como verificado um código que não pôde rodar. Nesta passagem o Matplotlib foi **instalado (3.11.2)** e os dois blocos da Aula 01 foram **executados na íntegra**, com backend `Agg`, sobre NumPy 2.5.1.

Isso eleva as duas alegações de "sintaxe conferida contra a documentação" para **"comportamento conferido contra a implementação"**, que é um grau de evidência mais forte: a documentação diz o que a função promete, a execução mostra o que ela faz.

---

### 🟠 16. `Cp = 1.000 J/(kg·K)` apresentado sem ressalva, num exemplo ancorado em medida de superfície

**claim_id:** `GEODIN-M23-A04-CPRESSALVA-009` *(alegação levantada por esta passagem)*
**Alegação-mãe:** `GEODIN-M23-A04-EXEMPLO-PROPRIEDADES-008`
**Tipo:** omissão que gera erro
**Onde:** Aula 05 · Exemplo trabalhado, Situação 1

**Estava escrito:** *"Uma rocha crustal tem condutividade térmica k = 2,7 W/(m·K) (um valor representativo; a faixa medida em rochas crustais vai de cerca de 2 a 4), densidade ρ = 2.700 kg/m³ e calor específico Cp = 1.000 J/(kg·K)."*

**Problema:** a assimetria de tratamento. O texto dá a `k` uma faixa medida explícita e apresenta `Cp` **cru**, como se fosse uma constante de rocha — e `Cp` é justamente o parâmetro dos três cujo valor de laboratório à temperatura ambiente mais se afasta do número usado. Pela equação de `Cp` bulk-crustal de Whittington, Hofmeister & Nabelek (2009), a crosta média vale **761 J/(kg·K) a 25 °C** e só passa por **1.000 J/(kg·K) perto de 220 °C**.

O que torna isso 🟠 e não uma observação de estilo é o **contexto do enunciado**: ele fala em "gradiente geotérmico medido num poço" e pede "o fluxo de calor condutivo **em superfície**". O leitor que tomar `Cp = 1.000` como a propriedade da rocha à superfície e recalcular obtém κ = 1,0 × 10⁻⁶ m²/s onde o valor coerente com a superfície seria ≈ 1,3 × 10⁻⁶. A frase seguinte — *"sai de três propriedades medíveis de rocha comum"* — reforça a leitura de que os três são medidas diretas, e para `Cp` isso pedia uma ressalva.

**Correção aplicada:** uma ressalva de **uma cláusula**, no mesmo formato que `k` já tinha, mais uma frase de robustez. Nenhum valor foi alterado e **nenhum resultado mudou**: κ = 1,0 × 10⁻⁶ m²/s e q = 54 mW/m² permanecem.

> "…e calor específico Cp = 1.000 J/(kg·K) **(o valor padrão em geodinâmica, mas atenção: o calor específico da rocha cresce com a temperatura — a crosta média vale cerca de 760 J/(kg·K) à superfície e só passa por 1.000 perto de 220 °C)**."

> "…sai de três propriedades medíveis de rocha comum. **E é robusto: varrendo k de 2 a 3,8 e Cp de 760 a 1.000, κ fica entre 0,7 e 1,9 × 10⁻⁶ m²/s, o que é a razão de os modelos térmicos de litosfera adotarem κ ≈ 1 × 10⁻⁶ m²/s como constante.**"

A segunda frase é o que impede a ressalva de virar um problema pedagógico: ela mostra que a dispersão **não ameaça** o número que o módulo vai reusar nas Aulas 06 e 07 — que é precisamente o ponto que a aula quer fixar.

**Fonte:** Whittington, A. G., Hofmeister, A. M. & Nabelek, P. I. (2009), "Temperature-dependent thermal diffusivity of the Earth's crust and implications for magmatism", *Nature*, **458**, 319-321, DOI 10.1038/nature07818 — equações (3) e (4), avaliadas numericamente nesta passagem. · **Nível:** revisada por pares · **Confiança:** confirmado
**Desfecho:** **corrigido** · **Propagação:** nenhuma — questionário, baralho e glossário continuam inexistentes.

---

### Itens azuis desta passagem — verificados e corretos

| # | claim_id | Aula | O que faltava | Como foi verificado | Situação |
|---|---|---|---|---|---|
| **P2** | `GEODIN-M23-A01-MATPLOTLIB-API-006` | 01 | executar o código | **Executado.** `invert_yaxis()` → `ylim = (42.0, −2.0)`, eixo decrescente para cima. `imshow(origin="upper")` → `extent = [−0.5, 3.5, 2.5, −0.5]`, linha 0 no topo. `colorbar(label=…)` aceita o argumento e o rótulo é lido de volta do objeto. Sem erro nem aviso de depreciação. | ✅ correto |
| **P3** | `GEODIN-M23-A01-EXEMPLO-MAPA-007` | 01 | conferir a figura | **Executado.** `argmax = (linha 0, coluna 3)` valor 3,0; `argmin = (linha 2, coluna 0)` valor −2,0; `clim = (−2.0, 3.0)`. Posição na figura confirmada por transformação para coordenadas de tela: máximo em (427,2; 360,8), mínimo em (129,6; 114,4) — **mais à direita e mais alto**, ou seja, canto superior direito × canto inferior esquerdo, como o texto afirma. | ✅ correto |
| **P4** | `GEODIN-M23-A03-MALHA-COLOCALIZADA-010` | 04 | verificar contra Gerya (2019) e Patankar (1980) | **Verificado contra fonte**, nas três partes do mecanismo: o estêncil `[−1 0 +1]` **aniquila** um campo que alterna de nó em nó (os dois vizinhos usados têm o mesmo valor); o solver aceita o xadrez como solução estacionária legítima, de comprimento de onda de duas células; e o remédio acopla a velocidade da face a um gradiente de estêncil compacto entre centros **diretamente** vizinhos. Gerya 2ª ed. 2019 (CUP) confirmada como edição e ano. | ✅ correto |
| **P5** | `GEODIN-M23-A03-EXEMPLO-ESCALONADA-011` | 04 | só formalizar o registro | **Re-executado.** `x_meio = [0.5 1.5 2.5 3.5]`, `size = 4` contra `x.size = 5`. A generalização *n* nós → *n*−1 centros verificada exaustivamente para *n* de 2 a 59. | ✅ correto |

| **P6** | `GEODIN-M23-A04-EXEMPLO-PROPRIEDADES-008` | 05 | avaliar a **representatividade** dos três parâmetros de entrada | **Confirmada contra fonte** — detalhado logo abaixo. Aritmética re-executada: κ = 1,0 × 10⁻⁶ m²/s e q = 0,054 W/m² = 54 mW/m². | ✅ correto |

**Sobre `EXEMPLO-PROPRIEDADES-008` (P6, a de maior prioridade):** a pergunta pendente era a **representatividade dos três parâmetros de entrada**, e a resposta é **sim, os três são representativos** — o achado 🟠 16 acima é sobre a *ressalva ausente*, não sobre os valores:

- **ρ = 2.700 kg/m³** — é **exatamente** a densidade crustal de referência adotada por Whittington et al. (2009) para a crosta média, com a justificativa explícita de que compressão e expansão térmica se compensam em boa parte.
- **k = 2,7 W/(m·K)** — cai no meio da faixa crustal calculada pelo mesmo trabalho (**3,8** à superfície, caindo para **1,9** na transição α-β do quartzo), o que corrobora a faixa "cerca de 2 a 4" que a própria aula declara.
- **Cp = 1.000 J/(kg·K)** — valor padrão em geodinâmica, correspondente à crosta média a ≈ 220 °C. Representativo, com a ressalva agora registrada no texto.

E os **dois resultados** foram confirmados contra fonte independente, não apenas pela aritmética:

- **κ = 1,0 × 10⁻⁶ m²/s** — Whittington et al. abrem o artigo registrando que é o valor que a maioria dos modelos térmicos de litosfera assume como constante.
- **q = 54 mW/m²** — cai dentro da faixa continental que a aula declara (40-70), abaixo da média continental de 58 mW/m². O material didático de referência do MIT (12.201, cap. 5) faz **o mesmo cálculo** com 20 K/km e k = 3,0 e chega a ~60 mW/m²: mesma conta, mesma ordem, `k` ligeiramente diferente.

### Ressalva de atribuição registrada, sem edição

Em `MALHA-COLOCALIZADA-010`: a malha escalonada **não** foi inventada por Patankar (1980) — vem do método MAC de **Harlow & Welch (1965)**, e **Patankar & Spalding (1972)** a popularizaram. **A aula não reivindica autoria** para Patankar: cita-o como a exposição de referência do problema da malha colocalizada, o que está correto. **Não exigiu edição**; fica registrado para que uma auditoria futura não levante o ponto como se fosse novo.

### Contagens depois desta passagem

| | Levantamento 2026-09-19 | Passagem pontual 2026-09-20 | Total |
|---|---|---|---|
| 🔴 | 1 | 0 | **1** |
| 🟠 | 13 | **1** | **14** |
| 🟡 | 1 | 0 | **1** |
| 🔵 (verificado e correto) | 35 | **5** | **40** |
| **Achados numerados** | 15 | **1** | **16** |
| **Em aberto** | 0 | **0** | **0** |

**Alegações não auditadas: 0.** As cinco que estavam pendentes foram fechadas; uma alegação nova (`CPRESSALVA-009`) nasceu **desta** passagem e já nasce auditada e com fonte.

**Gate: continua liberado** para questionário e flashcards. As sete restrições ao gerador registradas em 2026-09-19 permanecem em vigor, **e esta passagem acrescenta uma oitava**:

> **Restrição 8 ao gerador** — ao cobrar a difusividade térmica, não formular item que apresente `Cp = 1.000 J/(kg·K)` como *a* medida de rocha crustal à temperatura ambiente. O valor é o padrão de modelagem geodinâmica e corresponde a ≈ 220 °C; à superfície a crosta média está perto de 760 J/(kg·K). Item sobre κ ≈ 1 × 10⁻⁶ m²/s como constante adotada nos modelos térmicos de litosfera **é** seguro e desejável.

**Arquivos alterados nesta passagem:** `…-aula-05-calor-fourier-conservacao-producao-adveccao.md` (corpo, Fontes e bloco de metadados), `…-aula-01-…md` e `…-aula-04-…md` (**apenas** blocos de metadados — nenhuma linha de conteúdo), este relatório, o manifesto `.json` e o hub do módulo.

---

*Relatório gerado pela skill `auditor-cientifico` em modo `audit-and-fix`, profundidade `full`. Manifesto estruturado: `23-modelagem-numerica-geodinamica-auditoria.json`. Adendo de divisão acrescentado em 2026-09-19 pela revisão didática, sem reabrir a auditoria. Passagem pontual pós-divisão executada em 2026-09-20 pela mesma skill, também sem reabrir os 15 achados.*
