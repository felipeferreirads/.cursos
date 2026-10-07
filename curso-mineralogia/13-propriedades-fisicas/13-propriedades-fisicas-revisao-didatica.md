# Revisão didática: Módulo 13 — Propriedades físicas e identificação macroscópica

**Revisado em:** 2026-10-07  ·  **Modo:** review-and-fix
**Material:** `curso-mineralogia/13-propriedades-fisicas/` — as 9 aulas e as figuras 1 a 5, depois da auditoria científica aprovada ([[13-propriedades-fisicas-auditoria|relatório]]); o relatório de auditoria foi lido antes, para não reintroduzir nenhum dos 19 achados corrigidos
**Contrato de nível:** `ensino-medio-sem-geologia-v1` (LC-01 a LC-08; o LC-09, degrau de inferência explícito, não se aplica a este módulo)
**Veredito:** Bem ensinado com ressalvas → **🟠 e 🟡 corrigidos; 🔵 abertos, não bloqueantes**

## Resumo

🔴 0 bloqueiam · 🟠 4 prejudicam · 🟡 13 atrito · 🔵 4 sugestões

**Carga estimada por aula** (contagem de `gerador-de-aula`; palavras de corpo de "Conteúdo" até o fim do recap, mesmo critério dos módulos 11 e 12, depois das correções):

| Arquivo | ID | Conceitos novos | Pré-requisitos reativados | Exemplos | Visuais | Duração |
|---|---|---|---|---|---|---|
| aula 01 | `a01` | 3 (hábito × agregado; vocabulário de agregados; grau de cristalinidade) + alerta de fibras | 2 | 1 (3 itens) | 1 figura + 3 tabelas | ~25 min (~1.275) |
| aula 02 | `a02` | 4 (clivagem: direções, qualidade e {hkl}; face × clivagem; partição; fratura) | 4 | 1 (3 itens, com produto escalar) | 1 figura + 2 tabelas | ~30 min (~1.460) |
| aula 03 | `a03` | 5 (Mohs ordinal; dureza absoluta e seus métodos; anisotropia; tenacidade; procedimento do teste) + causa pela ligação, reativada | 2 | 1 (3 itens, com razões) | 1 figura + 2 tabelas | ~30 min (~1.645) |
| aula 04 | `a04` | 3 (G e balança hidrostática; incerteza de um quociente; medida × calculada e solução sólida) | 2 | 1 (3 itens, com conta) | 2 tabelas | ~28 min (~1.275) |
| aula 05 | `a05` | 3 (metálico × não metálico; brilho × índice de refração; diafaneidade) | 2 | 1 (4 itens) | 1 figura + 1 tabela | ~23 min (~1.165) |
| aula 06 | `a08` | 3 (três origens da cor; por que a cor engana; traço e seus limites) | 3 | 1 (3 itens) | 1 tabela | ~27 min (~1.255) |
| aula 07 | `a06` | 3 (magnetismo; luminescência; radioatividade), cada um com o teste seguro | 3 | 1 (3 itens, inverso do quadrado) | — | ~27 min (~1.320) |
| aula 08 | `a09` | 4 (piezo e piroeletricidade pela simetria; efervescência; solubilidade; sabor proibido) + tabela-síntese das sete propriedades | 3 | 1 (3 itens) | 3 tabelas | ~28 min (~1.425) |
| aula 09 | `a07` | 3 (identificar é inferir e a ordem dos testes; chave dicotômica; grau de confiança e registro) | 3 | 1 (4 itens) | 1 figura + 2 tabelas | ~28 min (~1.360) |

A aula 03 fica no limite (~1.645 palavras, cerca de 3% acima do teto de ~1.600); ver o achado 🟡 1, que explica por que **não** foi dividida.

## Achados

### 🟠 1. Aula 03: o objetivo pede "explicar a anisotropia", e a aula só a descrevia

**Tipo:** objetivo não coberto (parte causal)
**Onde:** aula 03 · Anisotropia; Recap
**Problema:** `oa03` pede **explicar** a anisotropia de dureza. A seção dizia que a dureza "varia com a direção" e dava o caso da cianita, mas não dizia **por quê**. A explicação estava ao alcance (a seção anterior liga dureza a ligações, e a aula 02 liga clivagem a ligações por plano), mas o leitor tinha de fazer a ponte sozinho; uma questão do tipo "por que a cianita tem duas durezas?" ficaria sem resposta na aula.
**Correção aplicada:** frase de ponte na abertura da seção ("pelo mesmo motivo da clivagem (aula 02): as ligações que a ponta precisa romper mudam com a direção em que ela corre") e a mesma ideia no recap.
**Escopo:** correção local. **Alegação nova registrada** (`PRF-DUR-DIDAT-001`, "pendente").

### 🟠 2. Aula 04: exemplo (b) com termo errado e salto de cálculo

**Tipo:** salto no exemplo trabalhado + termo usado errado e sem definição
**Onde:** aula 04 · Exemplo trabalhado (b)
**Problema:** o enunciado chamava 42,96 e 46,42 cm³/mol de "densidade molar"; a unidade (cm³/mol) é de **volume molar**, termo que nenhuma aula anterior definiu, e a resolução falava, corretamente, em "volumes molares", o que fazia o enunciado e a resposta parecerem tratar de coisas diferentes. Depois, M = 140,69 + 63,08x e V = 42,96 + 3,46x apareciam sem dizer de onde vinham 63,08 e 3,46, e a equação ia direto a x ≈ 0,28 sem o passo algébrico.
**Correção aplicada:** "o **volume molar**, volume ocupado por um mol, é M/ρ"; os dois coeficientes explicados como diferenças (203,77 − 140,69 e 46,42 − 42,96) da troca de Mg₂ por Fe₂; a solução por multiplicação em cruz escrita (154,66 + 12,46x = 140,69 + 63,08x → x = 13,97 / 50,62 ≈ 0,28, conferido: 0,2759). Os resultados (Fo72Fa28; 0,29 pela interpolação linear) não mudaram.
**Escopo:** correção local. **Alegação nova registrada** (`PRF-DENS-DIDAT-001`, "pendente").

### 🟠 3. Aula 07: o recap devolvia a monazita aos "minerais de U e Th"

**Tipo:** recap que contradiz o corpo (e desfaz uma correção da auditoria)
**Onde:** aula 07 · Recap relâmpago
**Problema:** a auditoria (achado 16) corrigiu o corpo: a monazita não tem tório na fórmula e só é radioativa quando o recebe por substituição. O recap, porém, continuava "minerais de U e Th (uraninita, autunita, torbernita, monazita)". O recap é o trecho que o aluno relê e de onde sai o baralho; um card gerado dali reintroduziria o erro.
**Correção aplicada:** "minerais com U ou Th na fórmula (uraninita, autunita, torbernita, torita) e a monazita quando rica em Th por substituição". Encaminhado ao auditor como alegação "pendente" (`PRF-ESP-DIDAT-001`), por tocar o mesmo ponto de um achado factual.
**Escopo:** correção local.

### 🟠 4. Aula 05: o exemplo da esfalerita contradizia a regra ensinada, sem dizer

**Tipo:** exemplo que contradiz o modelo sem explicação
**Onde:** aula 05 · Exemplo trabalhado (c)
**Problema:** a seção "O que decide o brilho" ensina que n de 1,9 a 2,6 dá brilho adamantino; o exemplo (c), na mesma página, dá à esfalerita n ≈ 2,4 e brilho **resinoso**. Quem aplica a regra que acabou de aprender chega ao brilho errado, e o texto não diz por quê; o aluno perde a confiança na regra ou no exemplo.
**Correção aplicada:** frase que faz a ponte: "pelos limites da seção anterior, n ≈ 2,4 cairia no adamantino, e há espécimes claros de brilho adamantino; os limites são aproximados, e a classificação do brilho é visual". Retoma o que a própria aula já dizia ("os limites são aproximados... a classificação, por fim, é visual") e o "resinous to adamantine" do *Handbook of Mineralogy*, já citado nas Fontes.
**Escopo:** correção local. **Alegação nova registrada** (`PRF-BRI-DIDAT-001`, "pendente").

### 🟡 1. Aula 03: carga no teto; enxugada, não dividida

**Tipo:** carga cognitiva no limite
**Onde:** aula 03 · inteira
**Problema:** ~1.633 palavras depois da auditoria (a ressalva de Rosiwal, achado ⚪ 6, acrescentou ~80), e as correções desta revisão (🟠 1 e 🟡 2) somariam mais ~60, levando a ~1.690.
**Correção aplicada:** enxugada sem tirar conteúdo de ensino: o detalhe da primeira tabela de Rosiwal (topázio 194, adulária 59, halita no lugar da gipsita) passou do corpo para as Fontes, onde já estava completo, e o corpo mantém a divergência que importa (quartzo 100, 120 ou 175; apatita 5,5 ou 6,5; "leia como ordem de grandeza"), com remissão "as tabelas completas estão nas Fontes"; o "Método geral" deixou de repetir, passo a passo, o "Procedimento" da seção anterior; frases de transição e uma atribuição à Wikipedia no corpo saíram. Ficou com ~1.645 palavras (~30 min).
**Por que não dividir:** a fronteira natural seria "dureza (Mohs, absoluta, causa, anisotropia)" × "tenacidade e o teste"; a Parte 2 teria ~800 palavras (~15 min) e o módulo passaria a 10 aulas, já acima do padrão de 3 a 8 do `_contexto.md`. A aula tem 5 ideias novas, uma delas (a causa pela ligação) reativada do módulo 01, e cinco blocos curtos com tabela. Se o aluno relatar que passou de 30 min, a divisão acima é a recomendada, decisão do orquestrador.
**Escopo:** correção local (dividir não foi necessário).

### 🟡 2. Aula 03: termos sem definição e fonte no corpo

**Tipo:** termo técnico usado antes de definido (LC-01)
**Onde:** aula 03 · Dureza absoluta; Tenacidade
**Correção aplicada:** "**esclerômetro** (aparelho que risca a superfície com uma ponta de diamante sob carga controlada)"; "a **nefrita** (um agregado de anfibólio) e a **jadeíta** (um piroxênio), os dois materiais chamados jade"; "citada na Wikipedia" saiu do corpo (a fonte segue nas Fontes). Alegações em `PRF-DUR-DIDAT-001` ("pendente").

### 🟡 3. Aula 03: o procedimento pressupunha o resultado

**Tipo:** salto no procedimento
**Onde:** aula 03 · Como testar, passo (2)
**Problema:** "Pressione uma ponta aguda do mais duro contra a superfície do menos duro" exige saber de antemão qual é o mais duro, que é justamente o que o teste quer descobrir.
**Correção aplicada:** "Pressione a ponta do objeto de teste contra o espécime e arraste; se puder, faça também o contrário (uma aresta do espécime no objeto)."

### 🟡 4. Aula 03: o recap não dizia que os números de Rosiwal variam

**Tipo:** desalinhamento recap–corpo (risco para o baralho)
**Onde:** aula 03 · Recap relâmpago
**Problema:** o corpo insiste que os valores de Rosiwal são ordem de grandeza e divergem entre tabelas (achado ⚪ 6 da auditoria); o recap só dizia "degraus muito desiguais". Um card tirado do recap poderia pedir um valor como se fosse único.
**Correção aplicada:** "...o salto coríndon → diamante é o maior; os números variam com a tabela."

### 🟡 5. Aulas 01 e 02: termos sem glosa e enunciado incompleto

**Onde:** aula 01 · tabela de agregados; aula 02 · tabela de fraturas; Exemplo (b)
**Correção aplicada:** "a crisotila, uma serpentina que é a forma mais comum de amianto" (liga o termo ao alerta de fibras da mesma aula); "obsidiana (vidro vulcânico)", que torna legível a frase seguinte sobre vidros; o enunciado do exemplo (b) da aula 02 passou a pedir também (110)∧(101), que a resolução já calculava (60°) sem que o problema o pedisse. Alegações `PRF-HAB-DIDAT-001` e `PRF-CLIV-DIDAT-001` ("pendente").

### 🟡 6. Aula 04: "na tabela" incluía a apatita, que não está na tabela

**Onde:** aula 04 · Exemplo (a)
**Correção aplicada:** "Na tabela, a fluorita (3,18) é compatível, e o diamante (3,52) e a calcita (2,71) estão fora; mas, fora da tabela, a **apatita** (cerca de 3,2) também é compatível." É o contraexemplo em que a densidade não decide (pedido pela observação final da auditoria); ver também o 🟡 11.

### 🟡 7. Aula 05: objetivo não verificável e erro de redação

**Onde:** aula 05 · Objetivo; Exemplo (a)
**Correção aplicada:** "entender os dois como resposta da luz" → "explicar os dois pela luz que reflete na superfície e pela que atravessa o volume"; "deixa passar nenhuma luz" → "não deixa passar luz nenhuma".

### 🟡 8. Aula 06: frase circular, referência ambígua e remissão a módulo futuro

**Onde:** aula 06 · Três origens da cor; Por que a cor é o critério menos confiável
**Correção aplicada:** "É a classe de cor mais numerosa em minerais incolores quando puros" (circular: todo mineral incolor quando puro só pode ter cor alocromática) → "Muitos minerais comuns são assim, e é essa classe que causa a maior confusão na identificação"; "não se sabe de antemão qual das duas" (havia três classes no texto) → "num espécime desconhecido, não se sabe de antemão se a cor é idiocromática ou alocromática"; "lamelas finas de exsolução (módulo 23)" → "(módulo 09, aula 03; o processo é retomado no módulo 23)", onde a exsolução já foi definida. Alegação `PRF-COR-DIDAT-001` ("pendente").

### 🟡 9. Aula 07: termos sem glosa e nome de mineral em inglês

**Onde:** aula 07 · Vocabulário; Luminescência; Exemplo (c)
**Correção aplicada:** ferrimagnetismo ("os pequenos ímãs atômicos se alinham em sentidos opostos sem se cancelar por inteiro"); "uranilo (o íon UO₂²⁺)"; "µSv/h (microsievert por hora, unidade de taxa de dose de radiação)", unidade que o exemplo usava sem apresentar; "willemite" → "willemita" no corpo e nas Fontes, como na auditoria. Alegação `PRF-ESP-DIDAT-001` ("pendente").

### 🟡 10. Aula 08: um "erro comum" que não se entendia

**Onde:** aula 08 · Erros comuns
**Problema:** "Confundir pó de calcita com o do espécime inteiro" não dizia qual era o erro.
**Correção aplicada:** "**Comparar a reação do pó com a de um cristal inteiro.** O pó reage mais que a superfície; compare os espécimes no mesmo estado (a diferença entre os dois estados é justamente o que separa a dolomita da calcita)."

### 🟡 11. Aula 09: nome de método divergente do curso, frase ambígua e exemplo (d) indeciso

**Onde:** aula 09 · Identificar é inferir; A ordem dos testes; Exemplo (c) e (d)
**Problema:** (i) "a escada de inferência do curso" vinha com degraus diferentes dos da espinha didática do `_contexto.md` (observação → descrição interpretativa → interpretação genética → hipótese de processo), que o aluno ainda não viu; (ii) "Cada um tem risco; o ácido, a água e o risco danificam" usava "risco" em dois sentidos na mesma frase; (iii) no exemplo (d), o topázio era citado como compatível "e tem clivagem basal", deixando no ar se a observação "sem clivagem" o descartava, e a confiança "baixa a média" não aplicava o critério da tabela da própria aula; (iv) os exemplos das aulas 08 e 09 usavam a densidade como critério decisivo, sem mostrar um caso em que ela não decide (observação final da auditoria).
**Correção aplicada:** (i) "É uma escada de inferência, a mesma ideia que o curso usará para as texturas (módulos 25 a 27) e a catalogação (módulo 50), aqui aplicada à identificação"; (ii) "Cada um tem seus perigos, e o ácido e a água danificam o espécime, como o teste de dureza"; (iii) o topázio fica "menos provável, sem excluí-lo: um grão pequeno pode não mostrar a clivagem, e só descarta o que foi testado", e a confiança passa a **baixa**, com a razão (duas propriedades estáveis; cor e brilho são pistas; alternativas abertas); (iv) no exemplo (c): "a densidade, que descartou o ouro, aqui não decide (pirita ~5,0, marcassita ~4,9)". Com o 🟡 6 (aula 04: fluorita × apatita), o módulo passa a ter dois casos explícitos em que a densidade não resolve. Alegação `PRF-CHV-DIDAT-001` ("pendente").

### 🟡 12. Figura 5: folhas de ramos diferentes coladas

**Tipo:** visual que confunde a estrutura da chave
**Onde:** `13-propriedades-fisicas-fig-05-chave-macroscopica.svg` · folhas do ramo metálico
**Problema:** a caixa da calcopirita (ramo "mole") e a da hematita (ramo "duro") se sobrepunham em 12 px, e galena e ouro em 2 px (esta última já notada pela auditoria): as seis folhas metálicas pareciam uma fileira única, apagando justamente a bifurcação por dureza que a figura existe para mostrar.
**Correção aplicada:** folhas com 90 px de largura, 4 px de folga dentro de cada ramo e 18 px entre os ramos; descidas 18 px (y = 360) para não encostar na folha "gipsita"; setas e textos reposicionados. Nenhum rótulo mudou; XML validado.

### 🟡 13. Contagem de palavras nos rodapés

**Onde:** campo `palavras_corpo` das nove aulas e do `course-state.yaml`
**Correção aplicada:** recontado depois das correções (mesmo critério: de "Conteúdo" até o fim do recap): 1.275 · 1.458 · 1.643 · 1.275 · 1.163 · 1.253 · 1.321 · 1.427 · 1.361. A duração declarada da aula 03 passou de ~28 para ~30 min.

### 🔵 1. Questionário: o que cobrar e o que não cobrar

**Sugestão para o `gerador-de-questionarios`:** o módulo tem 9 aulas, acima do limite de ~5–6, então cabem 2–3 questionários parciais e um final. `oa05` e `oa06` ocupam duas aulas cada e devem pesar de acordo. **Não** cobrar valores de Rosiwal nem os limites de índice de refração por tipo de brilho como números a decorar (são ordem de grandeza e convenção, e as fontes divergem); cobrar a conclusão (Mohs é ordinal; o salto coríndon → diamante é o maior; brilho cresce com n). Bons itens de aplicação já prontos nos exemplos: intervalo de dureza por objetos, G com incerteza, idio × alo × pseudocromático, traço de metálicos, piezo × piro pela classe, registro de cinco campos com grau de confiança.
**Desfecho:** aberto, não bloqueante.

### 🔵 2. Módulo com 9 aulas

**Sugestão:** o `_contexto.md` prevê módulos de 3 a 8 aulas; a redação dividiu duas aulas por carga (decisão registrada no hub) e chegou a 9. Esta revisão não dividiu a aula 03 também por isso (ver 🟡 1). Sem ação.
**Desfecho:** registrado.

### 🔵 3. Aula 02: o golpe vem antes da regra de segurança

**Sugestão:** a aula abre com "Bata num cristal de halita..." e só no fim diz que não se quebra espécime de coleção. Um "(em pensamento; as regras do golpe estão no fim da aula)" na abertura evitaria a leitura literal.
**Desfecho:** aberto, não bloqueante.

### 🔵 4. Aula 09 (d): a densidade separa mal quartzo de berilo

**Sugestão (para o auditor, não editado):** a resolução diz que a densidade (2,65) é o próximo teste; ela separa bem o quartzo do topázio e da turmalina, mas o berilo incolor tem densidade próxima da do quartzo. Vale o auditor conferir se convém uma ressalva.
**Desfecho:** aberto, encaminhado à segunda passagem do auditor.

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo | Avaliado em |
|---|---|---|---|
| `mineralogia-m13-oa01` — hábito e agregados | aula 01 (`a01`) | sim (drusa de quartzo; botrioidal fibroso radiado; mármore sacaroide) | (questionário a gerar) |
| `mineralogia-m13-oa02` — clivagem, partição, fratura e {hkl} | aula 02 (`a02`) | sim ({100} por 3 direções; ângulos 70,53°, 90°, 60°; topázio) | (questionário a gerar) |
| `mineralogia-m13-oa03` — Mohs, dureza absoluta, tenacidade, anisotropia | aula 03 (`a03`) | sim (intervalo por objetos; cianita; razões de Rosiwal) | (questionário a gerar) |
| `mineralogia-m13-oa04` — densidade relativa e calculada | aula 04 (`a04`) | sim (G = 3,18 ± 0,04; olivina Fo72Fa28; fluorita 3,18) | (questionário a gerar) |
| `mineralogia-m13-oa05` — brilho, diafaneidade, cor e traço | aulas 05 e 06 (`a05`, `a08`) | sim (quatro descrições de brilho; rubi, malaquita, opala; três traços; ouro × pirita) | (questionário a gerar) |
| `mineralogia-m13-oa06` — propriedades especiais e teste seguro | aulas 07 e 08 (`a06`, `a09`) | sim (ímã; UV; inverso do quadrado; piezo × piro; dolomita; halita × silvita) | (questionário a gerar) |
| `mineralogia-m13-oa07` — chave, grau de confiança e testes pendentes | aula 09 (`a07`) | sim (pirita com marcassita não excluída; grão incolor de dureza 7) | (questionário a gerar) |

Nenhum objetivo descoberto depois do 🟠 1; nenhuma seção órfã (o procedimento de teste da aula 03 serve a `oa03` e é pré-requisito explícito de `oa07`). A parte "explicar por que a cor é o critério menos confiável" de `oa05` tem seção própria na aula 06; a parte "teste seguro" de `oa06` tem a tabela-síntese das sete propriedades na aula 08.

## O que está bem feito (manter)

- O "Método geral" e as seções "O que não concluir" repetem, aula após aula, a mesma disciplina: cada propriedade **estreita a lista** e nenhuma identifica sozinha. Quando a aula 09 transforma isso em registro de cinco campos e grau de confiança, o aluno já praticou a ideia oito vezes.
- As propriedades são explicadas pela estrutura e pela ligação, e não só listadas: clivagem pela densidade de ligações por plano, dureza pela força e pelo número de ligações, brilho pelo índice de refração, piezo e piroeletricidade pela simetria (com a tabela halita × calcita × quartzo × turmalina, que deriva a resposta da classe em vez de pedir que se decore).
- A segurança está onde o teste está, e não num apêndice: fibras asbestiformes (aula 01), golpe (02), risco e pó (03), pós tóxicos (06), ímã de neodímio, UV e radônio (07), ácido, H₂S e sabor proibido (08).
- Os exemplos trabalhados forçam o aluno a parar no degrau certo ("compatível", "em hipótese", "pendente"), e o exemplo da pirita (aula 09) fecha o módulo com um caso honesto de confiança média.
- As correções da auditoria se integraram bem ao texto: a divergência de Rosiwal virou lição de método ("os números mudam com a tabela, a conclusão não"), e o exemplo da aula 09 agora pratica exatamente o raciocínio não circular que a aula ensina.

## Correções aplicadas

| # | Severidade | Desfecho | Arquivos |
|---|---|---|---|
| 🟠 1 | 🟠 | Corrigido | aula-03 |
| 🟠 2 | 🟠 | Corrigido | aula-04 |
| 🟠 3 | 🟠 | Corrigido | aula-07 |
| 🟠 4 | 🟠 | Corrigido | aula-05 |
| 🟡 1–4 | 🟡 | Corrigido (🟡 1: enxugada, não dividida) | aula-03 |
| 🟡 5 | 🟡 | Corrigido | aula-01, aula-02 |
| 🟡 6 | 🟡 | Corrigido | aula-04 |
| 🟡 7 | 🟡 | Corrigido | aula-05 |
| 🟡 8 | 🟡 | Corrigido | aula-06 |
| 🟡 9 | 🟡 | Corrigido | aula-07 |
| 🟡 10 | 🟡 | Corrigido | aula-08 |
| 🟡 11 | 🟡 | Corrigido | aula-09 |
| 🟡 12 | 🟡 | Corrigido | fig-05 |
| 🟡 13 | 🟡 | Corrigido | todas as aulas, `course-state.yaml` |
| 🔵 1–4 | 🔵 | 1 e 3 abertos; 2 registrado; 4 encaminhado ao auditor | — |

**Afirmações factuais acrescentadas ou tocadas pela revisão** (nenhuma das 19 correções da auditoria foi revertida; a do achado 6, Rosiwal, foi reorganizada entre corpo e Fontes sem perder a divergência; todas as novas estão nos rodapés com `audit: pendente` para a segunda passagem do `auditor-cientifico`):

| claim_id | Aula | O que foi acrescentado |
|---|---|---|
| `PRF-HAB-DIDAT-001` | 01 | crisotila = serpentina, a forma mais comum de amianto |
| `PRF-CLIV-DIDAT-001` | 02 | obsidiana = vidro vulcânico; (110)∧(101) = 60° pedido no enunciado |
| `PRF-DUR-DIDAT-001` | 03 | anisotropia de dureza pela mesma causa da clivagem; esclerômetro (ponta de diamante sob carga controlada); nefrita = agregado de anfibólio, jadeíta = piroxênio; detalhe da tabela original de Rosiwal movido para as Fontes |
| `PRF-DENS-DIDAT-001` | 04 | volume molar = M/ρ (não "densidade molar"); passos 63,08, 3,46, 154,66, 12,46, 13,97 / 50,62 = 0,276 |
| `PRF-BRI-DIDAT-001` | 05 | n ≈ 2,4 da esfalerita cairia no adamantino; há espécimes claros adamantinos; classificação visual |
| `PRF-COR-DIDAT-001` | 06 | "muitos minerais comuns são alocromáticos"; exsolução remetida ao módulo 09, aula 03 |
| `PRF-ESP-DIDAT-001` | 07 | ferrimagnetismo; uranilo = UO₂²⁺; µSv/h; monazita no recap só quando rica em Th; willemita |
| `PRF-CHV-DIDAT-001` | 09 | densidade não separa pirita (~5,0) de marcassita (~4,9); topázio menos provável sem clivagem visível, não excluído; confiança "baixa" em (d); escada de inferência como versão da dos módulos 25-27 e 50 |

**Pendente antes do questionário:** segunda passagem do auditor sobre essas oito alegações e sobre a sugestão 🔵 4 (o gate formal só bloqueia achados 🔴/🟠 da auditoria, mas são afirmações que ainda não passaram por ele).
