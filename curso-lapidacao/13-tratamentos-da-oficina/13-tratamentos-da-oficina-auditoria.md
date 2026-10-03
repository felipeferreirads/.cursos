# Auditoria científica — Módulo 13: Tratamentos da oficina de lapidação e a regra de divulgação

**Curso:** Teoria da lapidação · **Módulo:** 13 (`tratamentos-da-oficina`) · **Aulas auditadas:** 5
**Modo:** `audit-and-fix` · **Profundidade:** `full`
**Data:** 2026-09-07
**Veredito:** ✅ **Aprovado com correções aplicadas** — 0 achados 🔴/🟠 em aberto. Gate liberado para revisão didática e questionário.

## Sumário

| Severidade | Achados | Corrigidos | Em aberto |
|---|---|---|---|
| 🔴 Erro | 1 | 1 | 0 |
| 🟠 Impreciso | 9 | 9 | 0 |
| 🟡 Desatualizado | 0 | — | 0 |
| 🔵 Sem fonte | 1 | 1 (reescrito com a incerteza explícita) | 0 |
| ⚪ Controverso | 0 | — | 0 |
| **Total** | **11** | **11** | **0** |

**Nota de procedência.** Uma tentativa anterior desta auditoria caiu por rate-limit no meio da Fase 2. Ela havia corrigido o **corpo** da aula 02 (fusão, imersão, remoção do núcleo da mabé) sem atualizar o **rodapé de alegações auditáveis** da mesma aula, e sem gravar nada no `course-state.yaml`. Esta rodada releu os cinco arquivos do zero, conferiu hash contra o estado (só a aula 02 divergia), reverificou as correções da tentativa anterior contra fonte — **todas se confirmaram** — e fechou a inconsistência que ela deixou (AUD-13-01).

### Verificação de fronteira do módulo (ponto de atenção específico)

O módulo é "fronteira ENXUTO" por decisão de 2026-09-01. **A fronteira foi respeitada.** Verificação executada sobre os 5 arquivos:

- Zero wikilinks apontando para fora do curso. Todos os 44 wikilinks do módulo resolvem para arquivos de `curso-lapidacao`.
- O `curso-gemologia` é citado **só por nome** ("módulo 01 do curso de Gemologia", "curso de Gemologia, módulos 02 e 03"), conforme a regra dura de `_contexto.md`.
- Aquecimento clássico, irradiação, difusão reticular, preenchimento de fratura e HPHT aparecem **apenas nominalmente**, na aula 05, sem desenvolvimento de conteúdo.
- Nenhuma aula afirma competência de bancada. As correções desta auditoria mantiveram o registro teórico (nota em AUD-13-07: a ressalva sobre tanzanita foi redigida como limite de escopo, não como instrução de procedimento).

---

## Achados

### 🔴 1. Rodapé de alegações auditáveis da aula 02 contradiz o corpo já corrigido

**claim_id:** `MON-GTD-CONST-001`, `MON-ESM-CONST-001`, `MON-MABE-CONST-001`
**Tipo:** inconsistência interna
**Onde:** aula 02 · rodapé YAML `alegacoes_auditaveis`

**Está escrito (rodapé):** GTD "é **colada** sobre uma base de vidro colorido" e a granada é "quase incolor"; para a soudé, "um teste de campo clássico é observar a pedra de lado"; para a mabé, a pérola é "removida, preenchida por **núcleo** e fechada com base de madrepérola".

**Problema:** o corpo da aula afirma o oposto em cada um dos três pontos — fusão sem cimento, almandina francamente vermelha, imersão como teste que fecha o caso, núcleo **retirado** e cavidade preenchida. O manifesto é o registro legível por máquina que as skills a jusante consomem: um gerador de questionário lendo `MON-GTD-CONST-001` produziria gabarito afirmando que a GTD é colada — factualmente falso. O rodapé também declarava `palavras_corpo: 1471` contra 1625 reais.

**Correção aplicada:** as três alegações foram reescritas contra as fontes; `MON-ESM-CONST-001` passou a registrar explicitamente que inclinar a pedra é **indício**, não o teste que fecha, e que com camadas de berilo o refratômetro não denuncia nada; `MON-MABE-CONST-001` passou a registrar a remoção do núcleo e o período de crescimento corrigido. Acrescentado `MON-GTD-ANEL-001` para isolar o mecanismo de identificação (ver achado 3). "Fontes consultadas" da aula 02 atualizado — a linha ainda creditava o "teste de inclinação".

**Fonte:** GIA, *Gems & Gemology*, lab notes sobre montagens de berilo e de quartzo imitando esmeralda (detecção por imersão, observação paralela à cinta); SSEF, doublets históricos. · **Nível:** base de referência · **Confiança:** confirmado

---

### 🟠 2. Datação da granada-topo aos "séculos XVIII e XIX"

**claim_id:** `MON-GTD-CONST-001` · **Tipo:** impreciso · **Onde:** aula 02, seção "Granada-topo" e "Por que estas construções sobrevivem"

**Está escrito:** "uma construção dos séculos XVIII e XIX" / "remonta à joalheria europeia dos séculos XVIII e XIX".
**Problema:** a evidência aponta produção a partir da década de 1840 (Jura francês) e chegada ao mercado em grande quantidade nos anos 1920 — século XIX e primeiras décadas do XX, não XVIII.
**Correção aplicada:** "construção do século XIX — produzida já na década de 1840 e despejada no mercado em quantidade nos anos 1920". A repetição da datação errada na segunda seção foi removida junto com a redundância dessa seção.
**Fonte:** SSEF · **Confiança:** provável (a data de origem varia entre fontes; a exclusão do século XVIII é o ponto firme)

---

### 🟠 3. Mecanismo do anel vermelho e localização do plano de fusão

**claim_id:** `MON-GTD-ANEL-001` (novo) · **Tipo:** erro de mecanismo · **Onde:** aula 02, seção "Granada-topo" e Recap

**Está escrito:** "mostra um anel vermelho junto à cinta, **onde a lasca de granada aparece de lado**".
**Problema:** duas imprecisões encadeadas. O anel é o **contorno da lasca de granada** visto por transparência, não a lasca vista de perfil na cinta. E o plano de fusão de uma GTD notoriamente **não** coincide com o plano da cinta: ele corre logo abaixo da mesa e é tipicamente uma superfície conchoidal irregular. Como escrito, a aula ensinaria ao aluno uma geometria errada da peça — e o módulo 14 (diagnóstico reverso) vai cobrar leitura de geometria.
**Correção aplicada:** mecanismo reescrito no corpo e no Recap, com a posição do plano de fusão explicitada como ressalva. Alegação nova `MON-GTD-ANEL-001` criada para o mecanismo de identificação, separada da alegação de construção.
**Fonte:** SSEF, doublets históricos (plano de fusão conchoidal abaixo da mesa; contraste de brilho granada/vidro) · **Confiança:** confirmado

---

### 🟠 4. Período de formação da mabé

**claim_id:** `MON-MABE-CONST-001` · **Tipo:** impreciso · **Onde:** aula 02, seção "Mabé"

**Está escrito:** "em um a dois anos o animal deposita nácar por cima".
**Problema:** a faixa relatada na literatura de perlicultura é de **um a três anos**. A faixa estreita demais é do tipo que vira distrator falso num questionário.
**Correção aplicada:** "ao longo de um a três anos". · **Fonte:** literatura de perlicultura (IGI e produtores) · **Confiança:** provável

---

### 🟠 5. A regra de divulgação omitia o gatilho de valor da FTC

**claim_id:** `FTC-DIVULG-REGRA-001` · **Tipo:** omissão que gera erro / precisão normativa
**Onde:** aula 05, seção "Formulando a regra de divulgação da oficina de lapidação"

**Está escrito:** "a regra de divulgação aplicável ao que a oficina de lapidação faz com a pedra pode ser formulada em **três pontos**: (1) identidade material; (2) durabilidade e cuidado; (3) ausência de marca visual não dispensa".

**Problema.** Este é o achado mais sério do módulo depois do 🔴, e é exatamente o ponto sinalizado como sensível. A norma real — **16 CFR § 23.24**, *Disclosure of treatments to gemstones* — também tem três gatilhos, mas **não são esses**: (a) o tratamento não é permanente; (b) o tratamento cria exigências especiais de cuidado; (c) o tratamento tem efeito significativo **sobre o valor** da pedra; e os três são independentes, basta um. A aula mapeava apenas (a)/(b), **omitia (c) inteiramente**, e acrescentava um terceiro ponto que não é gatilho da norma. Como a aula anuncia "três pontos" e a seção "O que não concluir" declara seguir "o princípio geral da literatura consultada (AGTA, FTC)", o leitor sai convencido de que decorou os três gatilhos da FTC — e sai com o conjunto errado. Consequência prática: o ônix comercial, cujo tingimento é permanente, ficaria sem gatilho aplicável na versão anterior da aula.

Adicionalmente, a aula não registrava **§ 23.25(d)(4)**, que para produto composto exige qualificação clara e ostensiva de que o produto (A) não tem as mesmas características da pedra que o nomeia e (B) exige cuidado especial — exigência mais forte que a de tratamento comum, e diretamente aplicável às pedras montadas das aulas 01 e 02.

**Correção aplicada:** seção nova "O que a norma efetivamente diz" com os três gatilhos do § 23.24 e a regra de composto do § 23.25(d)(4); a regra de três pontos do curso foi mantida, mas **explicitamente rotulada como síntese didática**, e o ponto (3) marcado no próprio texto como leitura do curso, não como quarto gatilho da norma. Recap, Exemplo trabalhado (agora mapeia cada etiqueta ao gatilho que a obriga), "Erros comuns" e "Fontes consultadas" propagados. Alegação `FTC-DIVULG-REGRA-001` reescrita para carregar o texto da norma; alegação nova `FTC-SINTESE-CURSO-001` criada para a síntese do curso, de modo que as duas coisas não voltem a se confundir.

**Fonte:** FTC, *Guides for the Jewelry, Precious Metals, and Pewter Industries*, **16 CFR § 23.24** (texto verificado literalmente) e **§ 23.25(d)(4)**; versão vigente das Guides, revisão de 2018. · **Nível:** normativa · **Confiança:** confirmado

---

### 🟠 6. Tingimento tratado como geralmente não permanente

**claim_id:** `TIN-AGA-PROC-001`, `FTC-DIVULG-REGRA-001` · **Tipo:** confusão de escopo
**Onde:** aula 04, seção "Tingimento"; aula 05, ponto 2 da regra

**Está escrito (aula 05):** "material tingido pode desbotar com exposição prolongada à luz ou a produtos de limpeza".
**Problema:** enunciado como regra geral, contradiz a própria aula 04. A carbonização açúcar/ácido que produz o ônix comercial é descrita na literatura como **penetrante e permanente** — o carbono fica alojado no poro. Confundir os dois casos leva o aluno a aplicar o gatilho (a) da FTC onde ele não vale, e a concluir que o ônix não precisaria ser declarado.
**Correção aplicada:** aula 04 ganhou parágrafo distinguindo a permanência do ônix da instabilidade de corantes em material mais mole e poroso (howlita), e amarrando isso ao gatilho de divulgação correto; Recap da aula 04 e ponto 2 da regra na aula 05 propagados; Exemplo trabalhado da aula 05 reescrito para mostrar o ônix caindo no gatilho (c), não no (a); "Erros comuns" da aula 05 ganhou o item "achar que 'permanente' dispensa o aviso". Datação do tingimento industrial de ágata corrigida de "mais de um século" para o início do século XIX em Idar-Oberstein.
**Fonte:** literatura de tratamento de ágata (processo açúcar/ácido sulfúrico descrito como penetrante e permanente); histórico de Idar-Oberstein · **Confiança:** confirmado

---

### 🟠 7. Tanzanita — risco de "alterar a cor" no calor da cera de dop

**claim_id:** `CAL-PROIBE-CALOR-001` · **Tipo:** confusão de escopo · **Onde:** aula 04, "Os materiais que proíbem calor de dop"

**Está escrito:** "o choque térmico pode fraturar a pedra ou, em casos extremos, **alterar sua cor**".
**Problema:** mistura duas faixas de temperatura que o módulo existe para separar. A cera de dop trabalha em dezenas de graus acima do ambiente (as de baixa temperatura, usadas justamente em material sensível, amolecem na casa dos 60–80 °C); a alteração de cor da tanzanita é produto do **aquecimento clássico**, a centenas de graus — que é matéria do `curso-gemologia`, não deste módulo. O risco real de bancada é a fratura, que tende a abrir ao longo dos planos de clivagem da zoisita. Como escrito, o texto puxava para dentro do módulo um efeito que a fronteira manda deixar de fora.
**Correção aplicada:** substituído por fratura ao longo da clivagem, com nota explícita de que a mudança de cor pertence ao aquecimento clássico e ao curso irmão. Recap e alegação propagados.
**Fonte:** literatura lapidária sobre dopagem a frio (tanzanita propensa a fratura térmica ao longo da clivagem; ceras de baixa temperatura ~60–80 °C) · **Confiança:** confirmado

---

### 🟠 8. Nomenclatura: "dope" em vez de "dop"

**claim_id:** `CAL-DOP-CERA-001` · **Tipo:** nomenclatura / inconsistência interna · **Onde:** aula 04, vocabulário e seção "Calor de processo" (3 ocorrências)

**Está escrito:** "fixar temporariamente a pedra numa haste metálica (o **dope**)".
**Problema:** a haste é o **dop**. O próprio curso já fixou a grafia: o módulo 04 (`laps-abrasivos-e-dop`) escreve "o dop" 41 vezes e nunca "dope"; o slug do módulo e o título desta própria aula usam "dop". Termo básico grafado de dois jeitos no mesmo curso é exatamente o que produz flashcard e distrator inconsistentes.
**Correção aplicada:** as 3 ocorrências corrigidas para "dop", com remissão ao módulo 04 no vocabulário; alegação atualizada com nota de grafia. Também removida a qualificação "metálica", que o módulo 04 não sustenta como universal.
**Fonte:** consistência interna do curso (módulo 04) + literatura lapidária (Sinkankas; USFG) · **Confiança:** confirmado

---

### 🟠 9. Oleamento e enceramento descritos como estritamente superficiais

**claim_id:** `ACA-OLE-CERA-001` · **Tipo:** impreciso · **Onde:** aula 05, vocabulário e seção "Oleamento e enceramento como acabamento"

**Está escrito:** "O oleamento de acabamento desta aula é **superficial**"; "aplicação de uma fina camada de cera **na superfície** da pedra pronta".
**Problema:** em material poroso opaco ou translúcido, o óleo e a cera penetram a microporosidade que aflora na superfície — não formam um filme. O próprio sistema de divulgação da AGTA classifica a operação como forma de **impregnação**, sob o código **W** (enceramento/oleamento: impregnação de cera, parafina ou óleo incolor em gema porosa opaca ou translúcida). A aula construía a distinção com o preenchimento de fratura sobre o eixo errado ("superfície contra interior"), que a fonte não sustenta.
**Correção aplicada:** distinção reancorada em **alvo e método** (fratura interna sob vácuo, em laboratório, contra brilho de superfície na bancada), que é o eixo que a fonte sustenta e que preserva intacta a fronteira do módulo. Acrescentado o código W, sua obrigatoriedade de divulgação e a nota de cuidado associada (nada de ultrassom nem vapor). Vocabulário, Recap e alegação propagados.
**Fonte:** AGTA, *Gemstone Information Manual*, código de tratamento **W** · **Nível:** base de referência · **Confiança:** confirmado

---

### 🟠 10. Base do dublê de opala — ironstone tratado como rara

**claim_id:** `TRT-OPL-DUBL-001` · **Tipo:** impreciso · **Onde:** aula 01, "A construção do dublê de opala" e Recap

**Está escrito:** "um disco de potch (opala comum) ou, **com menor frequência**, de outro material escuro e estável".
**Problema:** inverte a frequência relativa. O **ironstone** — a rocha ferruginosa hospedeira da opala boulder — é uma das bases mais correntes na prática australiana, ao lado do potch preto; obsidiana e vidro preto também são usados. "Com menor frequência" descarta como exceção o que é prática corrente.
**Correção aplicada:** os quatro materiais nomeados, com o ironstone identificado como hospedeira da opala boulder. Recap e alegação propagados.
**Fonte:** literatura australiana de opala sobre construção de dublê e triplete · **Confiança:** confirmado

---

### 🔵 11. Atribuição de "impregnado × estabilizado" a vocabulário formal de laboratório

**claim_id:** `EST-GRAU-ESPECTRO-001` · **Tipo:** evidência insuficiente · **Onde:** aula 03, "Nem toda impregnação é igual"

**Está escrito:** "a gemologia distingue, **no vocabulário técnico de laboratório**, gradações como 'impregnado' e 'estabilizado'".
**Problema:** não foi possível confirmar que exista tal gradação formal. O que se confirma é o contrário: a AGTA tem uma entrada **única** — código **I**, impregnação de gema porosa com agente incolor — **sem** graus de intensidade dentro dela; "estabilizado" é termo de comércio, consagrado sobretudo para a turquesa, não um grau normativo paralelo. A afirmação como escrita atribuía à norma uma distinção que a norma não faz.
**Correção aplicada:** reescrita com a incerteza explícita e a atribuição corrigida — o texto agora diz que o vocabulário disponível **não** resolve a gradação, nomeia o código I e identifica "estabilizado" como uso comercial. A pergunta aberta LC-08 da aula foi preservada; ela é sobre o **limiar de saturação**, que segue genuinamente sem consenso, e não depende da atribuição corrigida. Achado **fechado** — não fica como pendência.
**Fonte:** AGTA, *Gemstone Information Manual*, código de tratamento **I** · **Confiança:** confirmado para a correção; a gradação original permanece não verificada porque, ao que se apurou, não existe

---

## Verificado e correto (não gerou achado)

- **Aula 01** — construção de dublê e triplete de opala; função dupla da base escura (suporte mecânico + realce por contraste, imitando a opala preta natural); capa de quartzo ou vidro protegendo contra desgaste e perda de água ao custo óptico de uma interface a mais; opala como material relativamente mole (Mohs 5–6,5) e sensível à umidade; vulnerabilidade da interface colada a calor, solvente e ultrassom; pedra montada como técnica declarável e não como fraude por definição.
- **Aula 02** — soudé: evolução dos materiais (cristal de rocha com camada gelatinosa verde → espinélio sintético incolor → quartzo ou berilo incolor), cor concentrada em lâmina fina, imersão paralela à cinta como teste que fecha, refratômetro inútil com camadas de berilo. Mabé como pérola cultivada de fato e não imitação; núcleo hemisférico fixado contra a parede interna da concha; indícios de bolha, linha de cola e peso.
- **Aula 03** — gênese de turquesa, crisocola e variscita por precipitação em fraturas e cavidades de rocha alterada, e a porosidade daí resultante; impregnação sob vácuo seguida de cura; hidrofania da opala comum e o ciclo de absorção/secagem como causa de craquelamento; consequências do corte em material estabilizado (resposta mais previsível, possível escurecimento e brilho resinoso, sensibilidade diferente a calor e solvente); estabilização frequentemente invisível e o que isso implica para a divulgação.
- **Aula 04** — processo açúcar + ácido sulfúrico com carbonização nos poros produzindo o ônix comercial; sais metálicos para outras cores; howlita branca a cinza-claro com veios escuros, porosa, tingida de azul para imitar turquesa; kunzita com clivagem fácil somando risco mecânico e térmico; opala somando calor e hidrofania; as duas fontes de choque térmico (atrito do corte e água de refrigeração) e o mecanismo de expansão diferencial.
- **Aula 05** — oleamento/enceramento como acabamento de cabochão de esmeralda, nefrita e jadeíta; tradição chinesa de manutenção contínua da peça pelo dono; a divulgação como cadeia de informação que nasce na bancada; a lista de tratamentos de laboratório devolvida ao curso irmão.

## Observação fora do escopo factual

- Aula 03, Exemplo trabalhado: "o lapidário desbasta e **polui** sem sobressaltos" — erro de digitação por "poli". Corrigido de passagem; não é achado.

---

## Correções aplicadas

**Aplicadas em:** 2026-09-07

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `MON-GTD-CONST-001` · `MON-ESM-CONST-001` · `MON-MABE-CONST-001` | 🔴 | Corrigido | aula 02 |
| `MON-GTD-CONST-001` | 🟠 | Corrigido | aula 02 |
| `MON-GTD-ANEL-001` (novo) | 🟠 | Corrigido | aula 02 |
| `MON-MABE-CONST-001` | 🟠 | Corrigido | aula 02 |
| `FTC-DIVULG-REGRA-001` · `FTC-SINTESE-CURSO-001` (novo) | 🟠 | Corrigido | aula 05 |
| `TIN-AGA-PROC-001` · `FTC-DIVULG-REGRA-001` | 🟠 | Corrigido | aula 04, aula 05 |
| `CAL-PROIBE-CALOR-001` | 🟠 | Corrigido | aula 04 |
| `CAL-DOP-CERA-001` | 🟠 | Corrigido | aula 04 |
| `ACA-OLE-CERA-001` | 🟠 | Corrigido | aula 05 |
| `TRT-OPL-DUBL-001` | 🟠 | Corrigido | aula 01 |
| `EST-GRAU-ESPECTRO-001` | 🔵 | Corrigido com ressalva (reescrito com a incerteza explícita) | aula 03 |

**Pendências:** nenhuma. Nenhum achado 🔴 ou 🟠 em aberto — o gate do módulo está liberado.

**Propagação.** Não havia questionário nem baralho de flashcards para propagar (o módulo estava em `assessment: pending`, e este curso dispensa flashcards a partir do módulo 06). O questionário a ser gerado deve respeitar as travas listadas abaixo.

### Travas para o gerador de questionário

Pontos em que uma questão mal formulada reintroduziria um erro que esta auditoria acabou de fechar:

1. **GTD é unida por FUSÃO, não por cimento.** "Colada" só pode aparecer como distrator, nunca como resposta. Corolário legítimo de questão: uma GTD não descola por solvente como um dublê de opala descolaria.
2. **O plano de fusão da GTD não fica no plano da cinta** — corre abaixo da mesa e é irregular. O anel vermelho é o contorno da lasca, não a lasca vista de perfil.
3. **O teste que fecha a soudé é a IMERSÃO paralela à cinta**, não a inclinação. Com camadas de berilo, o refratômetro não distingue.
4. **A mabé não é imitação** — é pérola cultivada com cúpula de nácar verdadeiro. O núcleo é **retirado**; a cavidade é preenchida.
5. **Os três gatilhos da FTC são (a) não permanente, (b) cuidado especial, (c) efeito significativo sobre o valor**, independentes entre si. Não confundir com a regra de três pontos do curso, que é síntese didática — e cujo ponto (3) não é gatilho da norma. Se uma questão cobrar "os três gatilhos", a resposta é a do § 23.24.
6. **Tingimento de ágata é permanente.** Uma questão que use o ônix como exemplo de tratamento não permanente está errada; o gatilho que o obriga é o de valor.
7. **O risco de bancada da tanzanita é fratura, não mudança de cor.** Mudança de cor pertence ao aquecimento clássico, curso de Gemologia.
8. **Grafia "dop"**, nunca "dope".
9. **Oleamento/enceramento é impregnação (código W da AGTA)**, não filme de superfície. A distinção com o preenchimento de fratura é alvo e método, não "superfície contra interior".
10. **Fronteira:** aquecimento clássico, irradiação, difusão reticular, preenchimento de fratura e HPHT podem ser citados por nome como fora do escopo, mas nenhuma questão pode cobrar seu mecanismo.

## Fontes consultadas nesta auditoria

- **Federal Trade Commission**, *Guides for the Jewelry, Precious Metals, and Pewter Industries*, **16 CFR Part 23** — § 23.24 (divulgação de tratamentos: os três gatilhos, texto verificado literalmente), § 23.25(d)(4) (produtos compostos), § 23.19 (definições de pérola). Versão vigente, revisão de 2018.
- **American Gem Trade Association**, *Gemstone Information Manual* — códigos de tratamento **I** (impregnação) e **W** (enceramento/oleamento), obrigatoriedade de divulgação e notas de cuidado.
- **Gemological Institute of America**, *Gems & Gemology* — lab notes sobre montagens de berilo e de quartzo imitando esmeralda; detecção por imersão.
- **Swiss Gemmological Institute (SSEF)** — doublets históricos: granada da série piropo-almandina fundida a vidro, plano de fusão conchoidal abaixo da mesa.
- Literatura lapidária e de perlicultura para dopagem a frio, choque térmico, formação da mabé e construção de dublê e triplete de opala.
