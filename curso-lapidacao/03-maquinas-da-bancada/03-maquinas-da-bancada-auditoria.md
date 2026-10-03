# Auditoria científica — Módulo 03: Máquinas da bancada

> [!info] Curso de **Teoria da lapidação** · módulo 03 · modo **audit-and-fix** · profundidade **full**
> Executada em **2026-09-02** · Material auditado: as 6 aulas do módulo 03 · **Veredito: Aprovado com correções aplicadas**

## Escopo

Auditadas as 6 aulas do módulo 03, **em conjunto** (para pegar contradições entre aulas), a partir das **58 alegações auditáveis** declaradas nos rodapés (59 após esta auditoria, com o `claim_id` novo criado no achado 9) e das afirmações adicionais não declaradas pelos autores.

Hierarquia de fontes aplicada, conforme instrução do curso: **Vargas & Vargas**, **Wykoff**, **United States Faceters Guild** e **Sinkankas** para valores lapidários; catálogos correntes de fabricantes para dimensões de lâmina, roda e drum; manuais de fabricante (Ultra Tec, Facetron, Diamond Pacific) para especificação de máquina; **EPA 40 CFR 279** para o ponto regulatório; literatura revisada por pares (*Minerals*, MDPI) para o gretamento da opala; literatura de segurança de rebolos para a falha de roda abrasiva.

**Trevor Hannam** (`_fontes/faceting-made-easy-hannam-2000.txt`) foi tratado estritamente como corroboração secundária. Dois achados desta auditoria nascem exatamente de valores numéricos que estavam ancorados **só** nele — o que a política de fontes do curso veda. O `_fontes/` não foi auditado, por ser material de entrada.

## Resumo

| Severidade | Achados | Corrigidos |
|---|---|---|
| 🔴 Erro | 1 | 1 |
| 🟠 Impreciso | 10 | 10 |
| 🟡 Desatualizado | 0 | — |
| 🔵 Sem fonte | 1 | 1 |
| ⚪ Controverso | 1 | 1 |
| **Total** | **13** | **13** |

**Achados 🔴/🟠 em aberto: 0.** O gate para questionário e flashcards está liberado.

---

## Achados

### 🔴 1. O cheater descrito como capaz de corrigir "um ou dois dentes" de erro

**claim_id:** `AJU-CHEATER-IDX-001`
**Tipo:** erro factual + inconsistência interna
**Onde:** aula 05 · "Família 2 — a posição na volta: índice e cheater" (e repetido no "Recap relâmpago")
**Está escrito:** "move a pedra por uma fração de um passo de dente, **tipicamente para corrigir o equivalente a um ou dois dentes de erro acumulado**"
**Problema:** a quantificação é falsa e contradiz a própria frase que a contém. Numa roda de 96 dentes um dente vale **3,75°** de rotação; "um ou dois dentes" seriam 3,75° a 7,5°, que é um passo grosso de índice, não um ajuste fino — se o desvio fosse de um dente inteiro, a correção seria mudar de dente. A afirmação, como escrita, torna o cheater redundante com o próprio índice e destrói a distinção que é o objetivo de aprendizagem da aula. Nenhuma fonte quantifica a correção em dentes; **Hannam, a fonte citada, diz apenas "a small amount of movement, either left or right of the main setting"** e que o cheater "will allow for small errors in cutting or polishing".
**Correção aplicada:** removida a quantificação em dentes. O texto passou a "para corrigir pequenos erros de corte ou de polimento" e ganhou a âncora numérica correta: "numa roda de 96, um dente vale 3,75° de rotação, e o cheater oferece uma parcela disso — um desvio de um dente inteiro se corrige mudando de dente, não trapaceando". Recap ajustado no mesmo sentido.
**Fonte:** Hannam, *Faceting Made Easy* (2000), seção "Index Wheel & Cheater"; Wykoff, *Techniques of Master Faceting*; USFG, dicionário de facetamento · **Nível:** literatura de facetamento + aritmética do índice (360/96 = 3,75)
**Confiança:** confirmado
**Também aparece em:** "Recap relâmpago" da aula 05 — corrigido junto. A aula 04 não quantifica o cheater; nenhuma outra aula do módulo repete o dado.
**Desfecho:** **Corrigido**

---

### 🟠 2. Espessura de lâmina de slab saw dada como faixa única, incompatível com o intervalo de diâmetro declarado

**claim_id:** `SER-SLAB-DIM-001`
**Onde:** aula 01 · "Slab saw: fatiar o bruto"
**Está escrito:** "de 15 a 60 cm de diâmetro (6 a 24 polegadas) … e espessura da ordem de **1 a 1,6 mm** (0,04 a 0,065 polegada), variando com o fabricante"
**Problema:** a espessura escala com o diâmetro e a faixa declarada só vale para a metade inferior do intervalo. Catálogos atuais: lâmina de 6" ≈ 1,1 mm no rim; 10" ≈ 0,044 pol (1,1 mm); 18" ≈ 0,063 pol (1,6 mm); **24" ≈ 0,135 pol (3,4 mm)**. O teto de 1,6 mm subestima a lâmina de 60 cm por um fator de ~2. Como a aula ensina o kerf como perda de material, o erro tem consequência conceitual: subestima em metade a perda no maior corte.
**Correção aplicada:** a faixa única virou uma escala declarada — ~1,1 mm em lâminas de 15 a 25 cm, 1,6 mm nas de 45 cm, ~3 mm nas de 60 cm — com a razão física ("lâmina maior precisa de corpo mais grosso para atravessar reto").
**Fonte:** catálogos correntes de lâminas diamantadas lapidárias (notched rim 6–24 pol; Greenline 24" = .135") · **Nível:** base de referência · **Confiança:** confirmado
**Também aparece em:** "Exemplo trabalhado" da aula 01 usa "1 a 1,6 mm" para uma slab saw pequena — permanece correto sob a nova escala, nenhuma correção necessária. Recap não cita espessura.
**Desfecho:** **Corrigido**

---

### 🟠 3. Faixa de grão das rodas de esmeril truncada em 1200

**claim_id:** `ESM-RODA-GRAO-001`
**Onde:** aula 03 · "O esmeril lapidário" (e "Recap relâmpago")
**Está escrito:** "a faixa útil de grão vai da ordem de **60 a 1200** … com grãos ainda mais finos reservados ao polimento"
**Problema:** o teto está uma etapa abaixo do real. Os jogos correntes de bancada (6 e 8 polegadas) trazem **80, 220, 280, 600, 1200 e 3000**, e a sequência de uso corrente vai 280 → 600 → 1200 → **3000**, com o polimento só a partir do disco de **14000**. Colocar 1200 como teto faz o aluno atribuir ao polimento uma etapa (3000) que ainda é lixamento — e a distinção lixar/polir é justamente o que o módulo 02 firmou.
**Correção aplicada:** faixa corrigida para **60 a 3000**, com os grãos do jogo corrente enumerados e o polimento situado a partir de 14000. Recap atualizado.
**Fonte:** catálogos correntes de rodas de cabochão (jogos 80/220/280/600/1200/3000); sequência Diamond Pacific 280–600–1200–3000 + disco Nova 14000 · **Nível:** base de referência · **Confiança:** confirmado
**Desfecho:** **Corrigido**

---

### 🟠 4. Rachadura da roda de carbeto de silício atribuída ao giro a seco

**claim_id:** `ESM-RODA-SIC-001`
**Onde:** aula 03 · "O esmeril lapidário" (e o bullet correspondente em "Erros comuns" e no "Recap relâmpago")
**Está escrito:** "usado sempre molhado — a água resfria o corte e leva a lama, e uma roda dessas **girando a seco racha**"
**Problema:** mecanismo invertido. Girar a seco produz **superaquecimento, envidraçamento** (a face satura e para de cortar) e **poeira de sílica respirável** — esta última, aliás, a consequência mais grave e a que a aula omitia, ligada à silicose já tratada no módulo 02. O risco de a roda **rachar e se partir** vem do oposto: da absorção **desigual de umidade**, que degrada o ligante e tira a roda de balanceamento — daí a regra clássica de nunca deixar a roda parada dentro da água. Ensinar "a seco racha" faz o aluno crer que a roda molhada é a condição segura em qualquer circunstância, que é o contrário do que a prática de segurança recomenda.
**Correção aplicada:** as três consequências reais do giro a seco explicitadas (superaquece, envidraça, joga pó) e o risco de ruptura reatribuído à umidade absorvida de forma desigual. "Erros comuns" e "Recap" alinhados.
**Fonte:** literatura de segurança e manuseio de rebolos (absorção de umidade → degradação do ligante → desbalanceamento → ruptura; Norton Abrasives, *Proper Handling and Storage of Grinding Wheels*); Sinkankas · **Nível:** base de referência · **Confiança:** confirmado
**Desfecho:** **Corrigido**

---

### 🟠 5. Óleo de serra usado declarado "resíduo perigoso na maioria das jurisdições"

**claim_id:** `REF-OLEO-DESCARTE-001`
**Onde:** aula 02 · "O que cada um faz com a oficina e com quem está nela" (e "Recap relâmpago", "Erros comuns", "Vocabulário")
**Está escrito:** "óleo usado, carregado de pó de pedra fino, é **resíduo perigoso na maioria das jurisdições**"
**Problema:** falso como afirmação regulatória, e era exatamente o ponto que o redator sinalizou. Nos EUA, o óleo usado **destinado à reciclagem** é regido por norma própria — **EPA, 40 CFR Part 279, *Standards for the Management of Used Oil*** — **declaradamente menos rigorosa** que a de resíduo perigoso, justamente para incentivar a reciclagem. Ele só é tratado como perigoso se for **descartado** em vez de reciclado, ou se estiver misturado a resíduo perigoso (presunção de halogênios acima de 1.000 ppm). Uma aula teórica não pode afirmar classificação legal que não se sustenta, e a generalização "na maioria das jurisdições" não tem levantamento por trás.
**Correção aplicada:** a afirmação virou "resíduo **regulado**" — o que preserva intacto o ponto prático da aula (não vai no ralo nem no lixo comum, exige canal de coleta) — seguida da ressalva de que a classificação formal varia com a jurisdição e com a contaminação, com o caso dos EUA nomeado e citado. Vocabulário, "Erros comuns" e "Recap" alinhados ao novo termo.
**Fonte:** EPA, 40 CFR Part 279 (eCFR, consultado 2026-09-02) · **Nível:** normativa · **Confiança:** confirmado
**Desfecho:** **Corrigido**

---

### 🟠 6. Resolução do transferidor: "meio grau nas máquinas boas" inverte a relação

**claim_id:** `AJU-BATENTE-ANG-001`
**Onde:** aula 05 · "Família 1 — a inclinação" (e "Recap relâmpago")
**Está escrito:** "cobre de 0 a 90 graus, com divisões de **meio grau nas máquinas boas** (Hannam, *Faceting Made Easy*)"
**Problema:** duplo. **(a)** A relação está invertida: meio grau é a resolução de uma máquina **de entrada**. As máquinas de precisão leem o **décimo de grau** por vernier — os manuais Ultra Tec (V2R, V5) especificam linha de vernier de 0,1°, e a Facetron é vendida com precisão de 0,1°. Chamar meio grau de "máquinas boas" ensina o teto errado de precisão da máquina, o que importará no módulo 09. **(b)** O valor estava ancorado **só em Hannam** — fonte secundária que a política do curso proíbe como origem de dado numérico.
**Correção aplicada:** a escala 0–90 foi mantida (correta), e a resolução passou a ser declarada como variável com a máquina: meio grau nas simples (Hannam, agora explicitamente rotulado como a máquina de entrada) e vernier de um décimo de grau nas de precisão, com Ultra Tec e Facetron nomeadas. Recap atualizado.
**Fonte:** manuais Ultra Tec V2R e V5; especificação de 0,1° da Facetron; Hannam para a máquina de entrada · **Nível:** manual de fabricante · **Confiança:** confirmado
**Desfecho:** **Corrigido**

---

### 🟠 7. Rotação do tambor rotativo dada como "poucas rotações por minuto"

**claim_id:** `TUM-ROT-MEC-001`
**Onde:** aula 06 · "O tambor rotativo: a avalanche dentro do barril" (e "Recap relâmpago")
**Está escrito:** "um barril fechado, montado no eixo horizontal, que gira a **poucas rotações por minuto**"
**Problema:** erra a ordem de grandeza. A faixa corrente de trabalho é de **40 a 60 rpm**, e os barris pequenos de bancada em geral vêm fixos perto de 60. "Poucas rotações por minuto" sugere algo como 2 a 5 rpm — nessa velocidade a carga não chega ao ângulo de avalanche que a própria aula descreve como o mecanismo. Ainda que qualitativa, a formulação é um dado numérico disfarçado e o LC-05 exige ordem de grandeza correta.
**Correção aplicada:** "gira devagar — a faixa corrente de trabalho fica em torno de 40 a 60 rotações por minuto, e os barris pequenos de bancada em geral vêm fixos perto de 60". Recap atualizado. O contraste didático com o vibratório (que trabalha em dezenas de hertz) fica preservado e agora quantificado dos dois lados.
**Fonte:** guias de tumbling de referência (RockTumbler.com; fórum Rock Tumbling Hobby: "most store-bought smaller tumblers spin their barrels at 60 rpm"; recomendação de até 40 rpm para desbaste) · **Nível:** base de referência · **Confiança:** confirmado
**Desfecho:** **Corrigido**

---

### 🟠 8. Duração do ciclo completo de tumbling superestimada, e o exemplo em desacordo com a regra da própria aula

**claim_id:** `TUM-EST-DUR-001`
**Onde:** aula 06 · "O tambor rotativo" + "Exemplo trabalhado" + "Recap relâmpago"
**Está escrito:** "cada estágio dura da ordem de 1 a 4 semanas (o grosso é o mais demorado), e a sequência completa leva **de várias semanas a alguns meses**" · e, no exemplo: "O estágio grosso, **de 1 a 3 semanas**"
**Problema:** duplo. **(a)** O ciclo completo fica em **4 a 8 semanas** nas fontes de referência (quatro estágios, o grosso de 2 a 4 semanas em material duro, os três seguintes de ~1 semana cada). "Alguns meses" estica o teto para além do que a literatura sustenta. **(b)** Inconsistência interna: o texto diz que o grosso é o estágio mais demorado numa faixa de 1 a 4 semanas, mas o exemplo trabalhado o dá como "1 a 3" — abaixo do teto que ele mesmo deveria ocupar. As fontes põem o grosso em **2 a 4 semanas** para ágata.
**Correção aplicada:** a faixa por estágio (1 a 4 semanas) foi mantida — está correta — e detalhada: grosso de 2 a 4 semanas em material duro, os três seguintes em torno de uma semana cada; ciclo completo corrigido para **4 a 8 semanas**. O exemplo passou a "2 a 4 semanas em ágata". Recap atualizado. Os números do vibratório (estágios de dias, polimento às vezes de horas) foram verificados e mantidos, com o ciclo completo de 1 a 2 semanas acrescentado ao claim.
**Fonte:** RockTumbler.com, *How Long Does Rock Tumbling Take?*; manuais de fabricantes de tambor; Sinkankas · **Nível:** base de referência · **Confiança:** confirmado
**Desfecho:** **Corrigido**

---

### 🟠 9. "Swarf" atribuído a uma aula que nunca emprega o termo

**claim_id:** `FCT-SWARF-XREF-001` (novo)
**Tipo:** inconsistência interna (referência cruzada falsa)
**Onde:** aula 04 · "Vocabulário desta aula", "Antes de começar, você precisa saber" e a linha de pré-requisito
**Está escrito:** "**swarf** | mistura de pó de pedra e abrasivo gasto arrancada no corte, **definida na Aula 01**" · "Da Aula 01: **swarf** é o pó de pedra e abrasivo gasto que sai do corte"
**Problema:** a aula 01 deste módulo **não usa a palavra swarf em nenhum ponto** — ela define *kerf*. O termo é definido na **Aula 05 do módulo 02** ("material removido e abrasivo gasto, acumulados na interface de corte"), que já consta como pré-requisito declarado da própria aula 04. Como a aula 04 constrói o sistema de água sobre esse termo, o aluno que voltasse à aula 01 para reativá-lo não o encontraria — quebra direta do LC-01/LC-03.
**Correção aplicada:** as três referências reapontadas. O vocabulário passou a citar a Aula 05 do módulo 02 e adotou a redação exata de lá; o bullet da Aula 01 ficou só com o *kerf*; a linha de pré-requisito idem. O bullet do módulo 02 já presente na aula cobre o swarf.
**Fonte:** curso de lapidação, módulo 02 aula 05 (Vocabulário) e módulo 03 aula 01 · **Nível:** material do próprio curso · **Confiança:** confirmado
**Desfecho:** **Corrigido**

---

### 🟠 10. A preformação situada ora antes, ora dentro do desbaste — e a cadeia canônica trocada sem aviso

**claim_id:** `PRE-FORMA-DEF-001` (e `PRE-FORMA-CAD-001`, verificado e mantido)
**Tipo:** inconsistência interna, entre aulas e dentro da aula 03
**Onde:** aula 03 · "O que é uma preforma" · contra a aula 01 ("preforma: contorno aproximado … recortado antes do desbaste") e a aula 04 (mesma formulação)
**Está escrito:** "**Antes de desbastar** qualquer curva, a pedra passa pela preformação… Na cadeia **serrar → preformar → lixar → polir**, é o segundo passo" — enquanto, quatro parágrafos adiante, a mesma aula diz "a roda de diamante dura, de grão grosso, faz o **desbaste** … e define a curva grosseira **da preforma**"
**Problema:** três desalinhamentos encadeados. **(a)** A aula afirma que a preformação vem *antes* do desbaste e depois descreve o desbaste como a operação que *produz* a preforma. **(b)** Ela substitui a cadeia canônica do módulo 01 — **serrar → desbastar → lixar → polir**, repetida no próprio bloco de pré-requisito da aula 03 — por "serrar → preformar → lixar → polir", sem declarar que se trata do mesmo segundo lugar sob outro nome. **(c)** As aulas 01 e 04 tratam a preforma como o contorno recortado na trim saw, e a aula 03 como a peça já com volume; nenhuma das duas está errada (na literatura a preformação abrange as duas operações), mas o curso apresentava as duas versões sem reconciliá-las.
**Correção aplicada:** a passagem foi reescrita para dizer explicitamente que a preformação **ocupa o segundo lugar da cadeia do módulo 01** ("preformar" é o nome do que se faz nesse lugar) e que esse lugar **comporta duas operações** — recorte do contorno na trim saw e desbaste do volume contra a roda —, fechando com a reconciliação entre as duas aulas: "na aula 01 a preforma era o contorno recém-recortado; aqui ela ganha o volume". Aulas 01 e 04 não precisaram de edição: passam a ser a vista parcial que a aula 03 completa, como o próprio bloco "Antes de começar" da aula 03 já anunciava.
**Fonte:** Sinkankas, *Gem Cutting: A Lapidary's Manual* (preformação abrangendo trimming e grinding); Vargas & Vargas, *Faceting for Amateurs* · **Nível:** literatura primária do curso · **Confiança:** confirmado
**Desfecho:** **Corrigido**

---

### 🟠 11. Rigidez tratada como propriedade da roda enquanto classe

**claim_id:** `DRUM-CINTA-FLEX-001` / `ESM-RODA-GRAO-001`
**Tipo:** omissão que gera erro
**Onde:** aula 03 · "O esmeril lapidário", "O drum de expansão", "Erros comuns" e o "Ponto em aberto" (LC-08)
**Está escrito:** "Uma **roda de metal** é dura e impõe seu raio exato à pedra" · "Rígido é para desbastar; flexível é para lixar curva" · e o ponto em aberto opondo "a flexibilidade do suporte contra a finura do grão"
**Problema:** a aula distingue corretamente matriz metálica (desbaste) de matriz de resina (acabamento), mas depois trata "roda" como sinônimo de "rígido" em toda a argumentação. As rodas de resina de acabamento correntes são montadas **sobre base de borracha macia** e são anunciadas pelos fabricantes precisamente como conformáveis à pedra, eliminando chatos. Sem essa ressalva, o aluno conclui que qualquer roda deixa chato e só o drum não deixa — e o "ponto em aberto" do LC-08 fica mal enquadrado, porque a alternativa real ao drum não é "grão mais fino num suporte rígido", é **outro suporte também complacente**.
**Correção aplicada:** uma cláusula acrescentada na seção da roda ("as de resina vêm sobre base de borracha macia e já têm alguma flexibilidade própria; rígida mesmo é a de matriz metálica"); "roda de metal" trocado por "roda de matriz metálica" na comparação com o drum; e o ponto em aberto reenquadrado para o que de fato está em disputa — "quanta complacência o suporte precisa ter para dispensar o drum". Recap atualizado. A controvérsia continua declarada como pergunta aberta, sem arbitragem, conforme o LC-08.
**Fonte:** especificação de fabricante de rodas de resina para cabochão (diamante em resina flexível sobre borracha macia; conformação à pedra) · **Nível:** base de referência · **Confiança:** confirmado
**Desfecho:** **Corrigido**

---

### 🔵 12. "Cede alguns décimos de milímetro" — número sem fonte

**claim_id:** `DRUM-CINTA-FLEX-001`
**Onde:** aula 03 · "O drum de expansão"
**Está escrito:** "A borracha do drum tem uma leve **complacência** — cede **alguns décimos de milímetro** sob a pressão da pedra."
**Problema:** o valor foi sinalizado pelo próprio redator e não se confirma em nenhuma fonte. Deflexão de borracha sob carga depende da dureza Shore do tambor, da pressão de inflagem e da força aplicada; nenhum catálogo publica esse número, e a literatura de cabochão trata a complacência qualitativamente. Não é acusação de erro — é um número que não se pode sustentar, e a aula não precisa dele: o argumento é comparativo (a borracha cede, a roda metálica não).
**Correção aplicada:** o número foi **removido**, não substituído por outro — a rota legítima para um achado sem fonte. A afirmação ficou qualitativa e comparativa: "A borracha do drum tem **complacência** bem maior — cede visivelmente sob a pressão da pedra". Nenhuma conclusão da aula dependia do valor.
**Fonte:** — (não verificável) · **Confiança:** não verificado
**Desfecho:** **Corrigido (afirmação removida)**

---

### ⚪ 13. A dispensabilidade do angle cheater apresentada como consenso do ofício

**claim_id:** `AJU-CHEATER-ANG-002`
**Tipo:** certeza indevida
**Onde:** aula 05 · "Família 2 — a posição na volta: índice e cheater"
**Está escrito:** "vem em poucas máquinas e **a maioria dos facetadores o considera dispensável**; Hannam é uma das poucas fontes que separa os dois com clareza"
**Problema:** a frase apresenta como estado do ofício o que é a asserção de **uma única fonte secundária**. Hannam escreve "most faceters will tell you that the angle cheater is not necessary" — é a impressão dele, não um levantamento, e a política do curso não admite Hannam como origem de valor (aqui, também o "cerca de um décimo de grau"). O conteúdo em si não está em disputa na literatura; o que estava errado era o grau de certeza e a atribuição.
**Correção aplicada:** a afirmação foi **atribuída explicitamente** ("Hannam … **relata** que a maior parte dos facetadores o considera dispensável") e ganhou uma corroboração independente que explica *por que* isso é plausível: numa máquina cujo transferidor já traz vernier de um décimo de grau, o angle cheater é redundante com o próprio batente — ligando este achado ao achado 6. A distinção index cheater × angle cheater, que é o mérito de Hannam e o ponto que a aula existe para cravar, ficou intacta.
**Fonte:** Hannam, *Faceting Made Easy*, "Protractor, Stop & Cheater" (atribuição); manuais Ultra Tec V2R/V5 e especificação Facetron (corroboração da redundância) · **Nível:** secundária (atribuída) + manual de fabricante · **Confiança:** em disputa quanto à opinião; confirmado quanto ao mecanismo
**Desfecho:** **Corrigido (requalificado, sem arbitrar)**

---

## Verificado e correto

Alegações checadas contra fonte que **passaram sem correção** — registradas para que a auditoria seja refazível. Três delas eram pontos que os redatores sinalizaram como suspeitos e que a verificação **absolveu**.

| Alegação | Veredito | Fonte |
|---|---|---|
| **Lâmina fina de trim saw a partir de 0,1 mm** (`SER-TRIM-DIM-001`) — sinalizado como "otimista" | ✅ confirmado: lâminas ultrafinas de lapidação são catalogadas com kerf de **0,004 a 0,012 pol (0,1 a 0,3 mm)**, justamente para material caro (opala, turquesa) | catálogos de lâminas ultrafinas (Pro Slicer / Super Slicer) |
| Diâmetro de trim saw de 10 a 25 cm (4 a 10 pol) | ✅ confirmado (trim saws de 4" a 8" são a faixa corrente) | catálogos de serras de acabamento |
| **"Sinterizada" = liga metálica (metal bond)** (`SER-LAM-CONSTR-001`) — dúvida terminológica do redator | ✅ confirmado: sinterizada e *metal-bonded* designam a mesma construção — diamante prensado a quente distribuído em toda a espessura do rim, com auto-renovação conforme a borda se desgasta | catálogos de lâminas sinterizadas; literatura de ferramenta diamantada |
| Eletrodepositada = camada única fixada por níquel, comum em lâminas muito finas | ✅ confirmado | idem |
| Segmentos soldados a prata, com fendas, em lâminas grandes | ✅ confirmado, e reforçado: **lâminas de 16 pol e maiores são tipicamente de rim segmentado**, exatamente para refrigeração e saída de pó | catálogos de lâminas de slabbing |
| **Matriz mole que se desgasta e expõe diamante novo; matriz dura envidraça** (`SER-LAM-MATRIZ-001`) — a ponte com "o lap que satura" | ✅ confirmado. A analogia com o lap saturado do módulo 02 é ponte didática declarada e ensina o modelo mental certo (perda de exposição do grão), não um erro | literatura de ferramenta diamantada; envidraçamento de rebolo |
| Lâmina diamantada corta por abrasão/micro-lascamento, sem gume (`SER-LAM-DIAM-001`) | ✅ confirmado | Sinkankas; USFG |
| Kerf > espessura da lâmina; material do kerf é perda total (`SER-KERF-PERDA-001`) | ✅ confirmado | literatura de serragem |
| Lâmina fina flexiona sob carga lateral → sub-corte (`SER-LAM-FINA-001`) | ✅ confirmado | catálogos e literatura de lapidação |
| **A controvérsia LC-08 da aula 01** (corte torto: lâmina fina × avanço rápido demais) | ✅ é debate real na literatura amadora, e está corretamente posto como pergunta aberta sem arbitragem | fóruns e literatura de lapidação amadora |
| Lascamento de saída por falta de apoio atrás da beirada (`SER-SAIDA-LASC-001`) | ✅ confirmado | usinagem de materiais frágeis |
| Serra pode disparar plano de clivagem (`SER-CLIV-RISK-001`) | ✅ confirmado, e coerente com o curso de Gemologia, módulo 01 | Sinkankas; curso de Gemologia m01 |
| Serra de fio diamantado: corte em curva, perda mínima, material frágil (`SER-FIO-VAR-001`) | ✅ confirmado | literatura de escultura lapidária |
| Óleo com lubricidade maior; água pura resfria bem e lubrifica pouco (`REF-OLEO-LUBR-001`, `REF-AGUA-LUBR-001`) | ✅ confirmado | Sinkankas; USFG |
| Refrigerante solúvel devolve lubricidade e traz aditivo anticorrosão (`REF-SOLU-ADIT-001`) | ✅ confirmado. **A decisão do redator de não introduzir faixa de diluição foi correta**: a proporção é específica de produto (varia de ~1:10 a ~1:50 entre fabricantes) e cairia em receita de bancada, vedada pelo nível teórico do curso | fichas técnicas de refrigerante solúvel |
| Óleo impregna material poroso, altera cor e peso; material denso não sofre (`REF-OLEO-IMPREG-001`) | ✅ confirmado | Sinkankas; curso de Gemologia m01 (porosidade) |
| **Opala greta por ciclo molha-seca** (`REF-AGUA-OPALA-001`) — sinalizado pelo redator como possivelmente sem lastro | ✅ **confirmado, e com fonte revisada por pares**. A opala contém 3–21% de água; tensões internas surgem de qualquer desidratação, com encolhimento superficial e gretamento progressivo. O dano vem de **encharcamento prolongado ou de ciclos molha-seca repetidos**, e o mecanismo é exatamente o descrito na aula: a casca seca encolhe sobre o miolo ainda úmido | *Minerals* (MDPI) 13(3):356, **Cracking of Gem Opals** (2023); literatura de conservação de opala |
| Água pura oxida aço da serra; barramento enferrujado trava o carro (`REF-AGUA-OXI-001`) | ✅ confirmado | USFG; Sinkankas |
| Névoa de óleo respirável e risco de incêndio (`REF-OLEO-NEVOA-001`) | ✅ confirmado | higiene ocupacional de óleos de corte |
| Água congela em oficina fria; óleo mineral não, nessas temperaturas (`REF-AGUA-CONGELA-001`) | ✅ confirmado (ponto de fluidez de óleo mineral bem abaixo de 0 °C) | propriedades físicas |
| Refrigerante sujo como veículo de contaminação de grão (`REF-GRAO-CONTAM-001`) | ✅ confirmado | Sinkankas |
| Esmeril de eixo horizontal, pedra contra a periferia (`ESM-EIXO-CONF-001`) | ✅ confirmado | Sinkankas; catálogos |
| Curva como negativo do cilindro; pedra parada gera chato (`ESM-RODA-CURV-001`, `ESM-CHATO-RISK-001`) | ✅ confirmado | geometria de retificação; literatura de cabbing |
| **Roda de bancada de 15 a 20 cm (6 a 8 pol)** (`ESM-RODA-DIM-001`) | ✅ confirmado — 6" e 8" são exatamente os dois formatos correntes (Genie/CabKing 6"; Titan/CabKing 8") | catálogos de máquinas de cabochão |
| **Drum de expansão de ~15 cm (6 pol)** (`DRUM-EXP-CONF-001`), inflando por força centrífuga | ✅ confirmado como o formato típico (8" também existe, mas 6" é o corrente); o mecanismo de expansão está correto | catálogos de drums de expansão |
| Preforma fixa contorno e proporção; lixar e polir não mudam a forma (`PRE-FORMA-CAD-001`) | ✅ confirmado — a tese central da aula 03 está certa | Sinkankas |
| Progressão roda dura → drum flexível (`ESM-DRUM-PROG-001`) | ✅ confirmado | Sinkankas; Lapidary Journal |
| Facetadora posiciona, o lap remove (`FCT-FACET-DEF-001`) | ✅ confirmado | Vargas & Vargas; Wykoff |
| Plataforma, mastro/braço, cabeçote: função de cada um (`FCT-PLATAF-FUN-001`, `FCT-MASTRO-FUN-001`, `FCT-CABECOTE-FUN-001`) | ✅ confirmado | Vargas & Vargas; USFG |
| **Jogos de índice de 32, 64 e 96 dentes, com o 96 acompanhando a máquina** (`FCT-INDEX-DENTES-001`) — sinalizado pelo redator | ✅ **confirmado**. O 96 é o padrão de fato (divisível por 2, 3, 4, 6, 8, 12, 16, 24, 32, 48 — e a notação da maioria dos diagramas publicados); **96 e 64 cobrem ~80% dos designs publicados**; e o brilhante redondo padrão é cortável em 32, 64 e 96. O 48 de Hannam e os 72/77/80/120 existem, mas a aula diz "os mais comuns" e a escolha está correta | USFG, dicionário de facetamento; catálogos de index gears (Ultra Tec); Vargas & Vargas |
| Índice dá repetibilidade rotacional (`FCT-INDEX-DEF-001`) | ✅ confirmado | USFG; Hannam (corroboração) |
| **Numa roda de 96: de 12 em 12 dá 8 facetas; de 8 em 8 dá 12** (`AJU-INDICE-SIM-001`) | ✅ aritmética conferida (96/12 = 8; 96/8 = 12) | — |
| Sistema de água cumpre a tríade calor/aderência/swarf (`FCT-AGUA-FUN-001`) | ✅ confirmado, e coerente com o módulo 02 aula 05 | Sinkankas; curso de lapidação m02 a05 |
| **"Quill"** — divergência de rótulo sinalizada pelo redator | ✅ sem achado. Hannam usa "quill or dop arm" de forma frouxa; o uso da aula (cabeçote = porta-dop, prende o dop por mandril e carrega a roda de índice) é o **mais preciso** dos dois e coincide com o dicionário da USFG. Nenhuma correção necessária | USFG, dicionário de facetamento; Hannam |
| Escala do batente de 0 a 90° (`AJU-BATENTE-ANG-001`, parte não corrigida) | ✅ confirmado | Hannam; manuais de fabricante |
| Altura do mastro governa profundidade e posição, não o ângulo (`AJU-MASTRO-ALT-001`) | ✅ confirmado — e é o diagnóstico correto para meetpoint que não fecha por faceta curta ou longa | Wykoff; Vargas & Vargas |
| **Cheater é ajuste de índice, não de ângulo** — a tese da aula 05 | ✅ confirmado. É de fato o erro corrente da literatura amadora, e Hannam está entre os que acertam | Hannam; Wykoff; USFG |
| **As "duas famílias / dois planos"** (`AJU-FACETA-2FAM-001`) — declarado pelo redator como síntese didática do curso | ✅ sem achado factual. Não é terminologia consagrada e o rodapé **já a declara como síntese didática** — o que é o tratamento correto. A partição é logicamente válida (plano radial × posição na volta) e não contradiz nenhuma fonte. Fica registrada para o `revisor-didatico` decidir se o rótulo merece aviso no corpo da aula | Wykoff; USFG (meetpoint faceting) |
| Vibratório: peso desbalanceado, fricção de baixa amplitude, preserva a forma (`TUM-VIB-MEC-001`) | ✅ confirmado — "the grinding step of a vibratory tumbler smooths the rocks but does not round them" | RockTumbler.com; Lapidary Journal |
| Rotativo desbasta e arredonda, vibratório quase só pole; vibratório para pré-polir lote (`TUM-ROT-VIB-001`) | ✅ confirmado | RockTumbler.com; USFG |
| Estágios do vibratório em dias; polimento às vezes em horas | ✅ confirmado (~2 dias por estágio; ciclo completo de 1 a 2 semanas) | RockTumbler.com |
| Produtos e limites do tumbling (`TUM-PROD-SAIDA-001`, `TUM-LIM-FORMA-001`) | ✅ confirmado | Sinkankas |
| **Fluorita: clivagem octaédrica perfeita e baixa tenacidade** (`TUM-LIM-TENAC-001`) | ✅ confirmado, e **consistente em três lugares**: com o curso de Gemologia módulo 01 aula 18 ("kunzita e fluorita clivam com facilidade") e com a correção `CAL-APAT-FRAG-001` do módulo 02 desta mesma disciplina, que já isolara a fluorita como o caso de clivagem octaédrica perfeita | curso de Gemologia m01 a18; auditoria m02 |
| Material poroso retém composto de polimento no tambor (`TUM-LIM-PORO-001`) | ✅ confirmado | Sinkankas; curso de Gemologia m01 |
| Ponto em aberto da aula 06 (vibratório alcança ou só se aproxima do polimento do rotativo) | ✅ é divergência real, corretamente posta como pergunta aberta | literatura de tumbling |

## Contradições entre aulas

Verificadas explicitamente, já que as 6 aulas foram escritas em paralelo e a auditoria foi pedida em conjunto:

- **Preforma / preformação** — a única contradição real de conceito entre aulas (01 e 04 contra 03), e ela existia **também dentro da aula 03**. Resolvida no achado 10.
- **Swarf** — referência cruzada falsa da aula 04 para a aula 01. Resolvida no achado 9.
- **Cadeia de etapas** — "serrar → desbastar → lixar → polir" agora é a única cadeia canônica no módulo, com "preformar" declarado como o nome do segundo lugar.
- **Refrigerante e as três funções** — aulas 01, 02 e 04 concordam entre si e com o módulo 02 aula 05; a aula 02 delimita corretamente o escopo (não transportar conclusões de serra para facetadora, esmeril e laps).
- **Cheater × índice × batente** — aulas 04 e 05 concordam: a aula 04 diz que o índice não controla o ângulo, a aula 05 diz o mesmo do cheater. Após o achado 1, também concordam quanto à magnitude do ajuste.
- **Roda de índice de 96 dentes** — usada como exemplo nas aulas 04 e 05 com os mesmos números; a aritmética da aula 05 confere.
- **Rigidez × complacência** — aulas 03 (roda/drum) e 05 (nada a ver com rigidez) não colidem; o ajuste do achado 11 é interno à aula 03.
- **Fronteiras de escopo** — os deferimentos para os módulos 04, 06, 08, 09 e 11 são coerentes entre as seis aulas; nenhuma invade o território da outra.

## Nível teórico (regra dura do curso)

Varridas as seis aulas em busca de afirmação de competência de bancada ou destreza manual. **Nenhum achado.** Cada aula fecha "O que não concluir" negando explicitamente a leitura operacional, os diagnósticos da aula 05 param em "qual grandeza está fora e qual ajuste a governa" (e o texto diz isso literalmente), e a aula 02 recusa a receita de diluição. Um registro para a revisão didática, não achado de auditoria: o subtítulo "**De volta à facetadora, agora com a mão nos controles**" (aula 05) é a única formulação do módulo que flerta com a linguagem de operação, embora o corpo da seção não o faça.

## Observações fora do escopo da auditoria

Registradas sem misturar com os achados factuais:

- **Tamanho das aulas (LC-02).** As correções aumentaram cinco das seis aulas. Nenhuma prosa do redator foi cortada — o ajuste do teto é da revisão didática, não desta auditoria —, e apenas o texto que a própria auditoria instalou foi comprimido onde ficou redundante. `palavras_corpo` ressincronizado em todos os rodapés com a contagem real pela régua fixada em `_contexto.md`. As aulas 03 (1721) e 05 (1759) são as que mais excedem o teto de ~1.600 e são as candidatas naturais a corte ou a divisão em Parte 1 / Parte 2.
- **Três `claim_id` da aula 03 nasceram com 3 segmentos e foram renomeados pelo orquestrador em 2026-09-02**, antes de qualquer material derivado: `PRE-DEF-001` → `PRE-FORMA-DEF-001`, `PRE-CADEIA-001` → `PRE-FORMA-CAD-001`, `DRUM-CONF-001` → `DRUM-EXP-CONF-001`. Motivo: a regra dura de `_contexto.md` (`^[A-Z]{2,4}-[A-Z0-9]+-[A-Z0-9]+-[0-9]{3}$`) existe para não repetir a herança de 3 segmentos do `curso-gemologia`. O `auditor-cientifico` não renumera `claim_id` por conta própria (é a âncora do histórico), mas aqui os três eram do dia, sem questionário/flashcard apontando, citados só nesta auditoria — custo mínimo agora, crescente depois. A aula 03, este relatório e o manifesto `.json` foram todos atualizados. O `claim_id` novo criado nesta auditoria (`FCT-SWARF-XREF-001`) já nasceu com 4 segmentos.
- **Aulas ainda marcadas como `pending` no `course-state.yaml`.** As seis entradas de `lessons.items` do módulo 03 continuam com `status: pending`, sem `file` e sem `content_hash`, embora os seis arquivos existam e estejam auditados. Só o bloco `audit` foi gravado por esta auditoria, conforme o escopo recebido.
- **Wikilinks quebrados (assunto do `validador-estrutural-do-curso`, não meu).** Três alvos não correspondem a arquivo existente: na aula 01, `03-maquinas-da-bancada-aula-02-oleo-ou-agua-como-refrigerante-de-serra-desempenho-contaminacao-e-consequencias` (o arquivo é `…-refrigerante-de-serra.md`); na aula 04, duas ocorrências de `03-maquinas-da-bancada-aula-03-esmeril-e-drums-de-expansao-rodas-de-diamante-cintas-resinoides-e-a-preformacao-em-curva` (o arquivo é `…-esmeril-e-drums-de-expansao.md`). A aula 06 aponta para `04-laps-abrasivos-e-dop-modulo`, que ainda não existe — esperado, o módulo 04 está pendente.

## Correções aplicadas

**Aplicadas em:** 2026-09-02

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `AJU-CHEATER-IDX-001` | 🔴 | Corrigido | aula-05 |
| `SER-SLAB-DIM-001` | 🟠 | Corrigido | aula-01 |
| `ESM-RODA-GRAO-001` | 🟠 | Corrigido | aula-03 |
| `ESM-RODA-SIC-001` | 🟠 | Corrigido | aula-03 |
| `REF-OLEO-DESCARTE-001` | 🟠 | Corrigido | aula-02 |
| `AJU-BATENTE-ANG-001` | 🟠 | Corrigido | aula-05 |
| `TUM-ROT-MEC-001` | 🟠 | Corrigido | aula-06 |
| `TUM-EST-DUR-001` | 🟠 | Corrigido | aula-06 |
| `FCT-SWARF-XREF-001` (novo) | 🟠 | Corrigido | aula-04 |
| `PRE-FORMA-DEF-001` | 🟠 | Corrigido | aula-03 |
| `DRUM-CINTA-FLEX-001` (rigidez como classe) | 🟠 | Corrigido | aula-03 |
| `DRUM-CINTA-FLEX-001` (décimos de mm) | 🔵 | Corrigido (afirmação removida) | aula-03 |
| `AJU-CHEATER-ANG-002` | ⚪ | Corrigido (requalificado, sem arbitrar) | aula-05 |

**`palavras_corpo` após as correções:** a01 **1657** · a02 **1679** · a03 **1721** · a04 **1488** · a05 **1759** · a06 **1510**. Todos os rodapés ressincronizados com a contagem real.

**Material derivado:** nenhum questionário e nenhum baralho de flashcards existiam no momento da auditoria — a ordem do pipeline foi respeitada, então **não houve propagação a fazer**. Nenhum baralho deste módulo foi importado no Anki, portanto não há card já em revisão a corrigir à mão.

**Pendências:** nenhuma. Os 13 achados foram resolvidos na mesma passada; **0 achado 🔴 ou 🟠 em aberto**, gate liberado para o `gerador-de-questionarios` e o `gerador-de-flashcards`.
