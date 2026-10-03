# Auditoria científica — Módulo 10: Famílias de talhe facetado

> [!info] Curso de **Teoria da lapidação** · módulo 10 · modo **`audit-and-fix`** · profundidade **`full`** · executada em **2026-09-06**

**Material auditado:** as 5 aulas do módulo (`lapidacao-m10-a01` a `a05`), 34 alegações auditáveis declaradas nos rodapés.
**Veredito:** ✅ **Aprovado com correções aplicadas.** Nenhum achado 🔴 ou 🟠 em aberto.

| Severidade | Achados | Corrigidos | Em aberto |
|---|---|---|---|
| 🔴 Erro | 2 | 2 | 0 |
| 🟠 Impreciso | 3 | 3 | 0 |
| 🟡 Desatualizado | 0 | — | 0 |
| 🔵 Sem fonte | 1 | 1 (reescrito com a incerteza explícita) | 0 |
| ⚪ Controverso | 0 | — | 0 |
| **Total** | **6** | **6** | **0** |

> [!note] Contexto de execução
> Uma tentativa anterior desta auditoria caiu por limite de API durante a Fase 2. O estado dos cinco arquivos foi relido do zero: a aula 01 tinha o `content_hash` divergente do `course-state.yaml` (edição parcial da tentativa anterior), as aulas 02–05 estavam intactas. Toda a Fase 1 foi refeita; nenhum achado foi herdado.

---

## Achados

### 🔴 1. O talhe Barion tem coroa em DEGRAU, não coroa brilhante

**claim_id:** `MIX-BAR-WATER-001`
**Tipo:** erro factual + inconsistência interna
**Onde:** aula 03 · "Vocabulário", seção "Os dois sentidos da palavra 'misto'", seção "O talhe Barion", "Exemplo trabalhado" passo 3, "Erros comuns", "Recap relâmpago"

**Estava escrito:** "O talhe Barion, com coroa brilhante e um pavilhão de arranjo brilhante modificado, também cai aqui" · "Coroa brilhante sobre pavilhão brilhante modificado, arranjos distintos: misto no sentido 1" · "põe um pavilhão de arranjo brilhante, e não degrau, dentro do contorno alongado, e acrescenta uma fileira de **facetas cruzadas** logo abaixo da cinta" · "pensado para contornos de fantasia — oval, almofada, coração".

**Problema:** três erros somados sobre o mesmo talhe.

1. **A coroa.** O Barion é definido por uma coroa em **degrau** sobre um pavilhão de arranjo **brilhante** — ele *inverte* a receita do Ceilão. A aula afirmava o contrário.
2. **Incoerência interna decorrente.** Com "coroa brilhante sobre pavilhão brilhante", a pedra do exemplo (C) não teria dois arranjos diferentes e portanto **não seria um talhe misto**, contradizendo a própria conclusão do passo 3 e o "sentido 1" que a aula adota.
3. **O nome das facetas.** A assinatura do Barion é uma fileira de facetas **em meia-lua** (*half-moon*, *lunette*, crescente) partindo da culaça em direção à cinta — não "facetas cruzadas".
4. **O contorno de origem.** O Barion nasceu em contorno **quadrado ou quase quadrado com os quatro cantos truncados** (*cushion square*), com proporções retangulares também previstas na patente; só depois o conceito foi estendido a oval, almofada, triangular e outros. A aula o apresentava como concebido para contornos alongados de fantasia.

**Correção aplicada:** a descrição foi reescrita nos seis pontos. O Barion passa a ser apresentado como **misto invertido** — o que, além de correto, reforça a tese pedagógica da aula ("misto não é só coroa brilhante sobre pavilhão degrau"). Data e autoria precisadas: patenteado por Basil Watermeyer, África do Sul, **1971**. Acrescentada uma linha de vocabulário para "facetas em meia-lua".

**Fonte:** SkyJems, *Barion Cut* (coroa em degrau, pavilhão brilhante, facetas *half-moon*/lunette, contorno quadrado de cantos truncados, patente de 1971) · International Gem Society, *Barion Concept Cut Design* (Watermeyer 1971; facetas em meia-lua na cinta; centro em princípios de brilhante; exemplos triangular, almofada, keystone e oval). Consultadas em **2026-09-06**.
**Nível:** base de referência gemológica · **Confiança:** confirmado
**Também aparece em:** aula 04 (menção ao "pavilhão de arranjo brilhante modificado — o talhe Barion") — verificada, permanece **correta** após a correção, pois o pavilhão de fato é brilhante.
**Desfecho:** ✅ **Corrigido**

---

### 🔴 2. "Olhos de peixe" aplicado ao defeito errado

**claim_id:** `CON-FORMA-DEFEITO-001`
**Tipo:** erro factual (nomenclatura)
**Onde:** aula 04 · tabela "Cada contorno e seu defeito característico", linha **Oval**

**Estava escrito:** "gravata-borboleta; pontas mais claras (**"olhos de peixe"** nas extremidades)"

**Problema:** *olho de peixe* (**fish-eye**) é um defeito com definição fixa e diferente: é o **reflexo da cinta visto através da mesa**, um anel esbranquiçado no meio da pedra, causado por **pavilhão raso demais** e agravado por mesa larga e cinta grossa. Não tem relação com as extremidades claras de um oval. O erro é caro porque o termo volta no módulo 14 (julgar um talhe pronto) com o significado correto: o aluno chegaria lá com uma definição concorrente já memorizada, e um distrator de questionário construído sobre a versão errada viraria gabarito errado.

**Correção aplicada:** o rótulo foi retirado; a linha passou a "gravata-borboleta; extremidades mais claras que o centro" — o fato observável, que estava certo, foi preservado. A definição correta de fish-eye foi registrada como nota de auditoria no rodapé da aula, com a indicação de que o termo pertence ao módulo 14. **Nenhuma definição nova foi introduzida no corpo da aula** (LC-02).

**Fonte:** PriceScope, *Fish-Eye Effect* · Beyond4Cs, *So, What is a Fish Eye Effect in a Diamond?* — "a shallow pavilion creates a fish-eye effect if viewed from the table, caused by the girdle reflecting in the middle of the table". Consultadas em **2026-09-06**.
**Nível:** base de referência · **Confiança:** confirmado
**Também aparece em:** nenhum outro ponto do módulo (o manifesto `CON-FORMA-DEFEITO-001` já dizia apenas "extremidades claras", sem o rótulo — só o corpo da aula errava).
**Desfecho:** ✅ **Corrigido**

---

### 🟠 3. A ondulação da cinta não é exclusiva do "escavar"

**claim_id:** `PES-PINTAR-ESCAVAR-001`
**Tipo:** omissão que gera erro
**Onde:** aula 05 · "Manobra 4 — pintar e escavar as facetas de cinta", "Erros comuns", "Recap relâmpago", "Fontes consultadas"

**Estava escrito:** "Pintar **borra a distinção** [...]. **Escavar** tende a **ondular a cinta**, deixando-a com espessura desigual em volta (o efeito 'festonado')" · e em Erros comuns: "escavar as afasta (ondula a cinta)".

**Problema:** a aula contrastava as duas manobras atribuindo o festonamento **só** ao escavar. Pela pesquisa da GIA que fundamenta o critério de simetria do sistema de cut grade, **as duas** produzem cinta festonada de forma desigual; o que muda é **onde** a cinta afina — pintar afina os "morros" nos pontos em que o bisel/principal encontra a cinta, escavar afina os "morros" onde duas facetas de cinta se encontram. Como escrito, o aluno concluiria que uma cinta regular exclui a hipótese de pintura, que é falso.

**Correção aplicada:** o custo óptico foi reescrito para atribuir a ondulação às duas manobras e nomear a diferença de posição. O contraste que a aula quer ensinar — só pintar borra o contraste com a faceta grande — foi preservado e ficou mais nítido. Rodapé e "Fontes consultadas" atualizados com a referência primária.

**Fonte:** Reinitz, Gilbertson & Geurts, *The Role of Brillianteering Variations in the GIA Cut Grading System* / *Painting and Digging Out*, **Gems & Gemology (2006)** · PriceScope, *GIA on Painting and Digging* e *Visible Effects of Painting & Digging on Superideal Diamonds*. Consultadas em **2026-09-06**.
**Nível:** revisada por pares (G&G) · **Confiança:** confirmado
**Desfecho:** ✅ **Corrigido**

---

### 🟠 4. Os números do exemplo trabalhado não fecham

**claim_id:** `PES-MORTO-PRINCIPIO-001`
**Tipo:** inconsistência interna (numérica)
**Onde:** aula 05 · "Exemplo trabalhado", enunciado e passos 2 e 3

**Estava escrito:** "A safira X mede 8,5 mm de diâmetro; a safira Y mede **9,4 mm**" · "espalha como uma de **~2,3 ct** típica" · "Espalha 9,4 mm nos mesmos 3 ct: **pavilhão perto do ângulo-alvo**".

**Problema:** pela estimativa-padrão de peso de um brilhante redondo — `ct = diâmetro(mm)² × profundidade(mm) × 0,0061 × (densidade relativa ÷ 3,52)` —, uma safira (DR ≈ 4,00) de 3,00 ct com 9,4 mm de diâmetro teria **≈ 52% de profundidade total**: uma pedra rasa, que janelaria, exatamente o oposto do "pavilhão perto do ângulo-alvo" que o passo 3 afirma. A pedra Y refutava a própria lição. O valor de referência "~2,3 ct" também estava baixo: uma safira bem proporcionada de 8,5 mm pesa ≈ 2,6 ct.

**Correção aplicada:** Y passou de 9,4 mm para **9,0 mm** (≈ 59% de profundidade — bem proporcionada) e a referência de "~2,3 ct" para **"~2,6 ct"**. X foi mantida em 8,5 mm / 3,00 ct, que dá ≈ 70% de profundidade e é coerente com a descrição de pedra "funda" e com a faixa de 62–65% do vocabulário da aula. Acrescentada a palavra "redondas" ao enunciado, para que a fórmula de diâmetro se aplique. O cálculo ficou registrado no rodapé.

**Fonte:** fórmula-padrão de estimativa de peso para brilhante redondo, com correção por densidade relativa (densidade da safira ≈ 4,00 — pré-requisito do `curso-gemologia`, módulo 01). **Confiança:** confirmado (aritmética verificável)
**Desfecho:** ✅ **Corrigido**

---

### 🟠 5. "Gema corada" definida estreita demais

**claim_id:** `MIX-COM-PADRAO-001`
**Tipo:** confusão de escopo
**Onde:** aula 03 · "Vocabulário desta aula"

**Estava escrito:** "**gema corada** (*colored stone*) | qualquer gema **transparente** que não seja o diamante **incolor**"

**Problema:** no uso corrente do comércio e do ensino gemológico, *colored stone* é **qualquer gema que não seja o diamante**, transparente ou não — a categoria inclui material opaco e translúcido (jade, turquesa, opala), que é justamente o que o programa de Graduate Colored Stones cobre. A restrição a "transparente" e o qualificador "incolor" recortavam a categoria pela conveniência desta aula (que trata de talhe facetado) e deixariam o aluno com uma definição que falha assim que ele encontrar o termo aplicado a um cabochão de turquesa — inclusive dentro deste próprio curso, nos módulos 06 e 13.

**Correção aplicada:** a linha passou a "no comércio, qualquer gema que não seja o diamante — transparente ou não — tratada como categoria à parte, com convenções de talhe próprias".

**Fonte:** uso corrente do termo no ensino e no comércio gemológico (GIA, *Graduate Colored Stones Program*, cuja cobertura inclui materiais opacos e translúcidos). **Nível:** base de referência · **Confiança:** provável — não foi localizada uma definição normativa citável literalmente; a correção **amplia** o escopo para o uso corrente em vez de fixar um recorte novo.
**Desfecho:** ✅ **Corrigido**

---

### 🔵 6. "Modelagens recentes" — atribuição não confirmada

**claim_id:** `CON-BOW-CAUSA-001`
**Tipo:** evidência insuficiente
**Onde:** aula 04 · seção "O efeito gravata-borboleta", "Erros comuns", "Recap relâmpago"

**Estava escrito:** "**Modelagens recentes** atribuem a maior parte do escurecimento a esse segundo mecanismo [obstrução], não ao vazamento."

**Problema:** o **mecanismo** de obstrução está bem atestado — a literatura gemológica descreve a gravata-borboleta como uma sombra que nasce fora da pedra e é projetada para dentro pelas facetas. O que **não** se confirmou foi a atribuição a "modelagens recentes": nenhum estudo de modelagem identificável foi localizado, e ao menos uma fonte do mesmo nível (Ada Diamonds) descreve o bow-tie como reflexão mal direcionada, distinguindo-o do vazamento **sem hierarquizar** os dois mecanismos. Como a aula declara este ponto como controvérsia LC-08, apoiar um dos lados numa autoridade inexistente enfraquece justamente a declaração de controvérsia.

**Correção aplicada:** o achado 🔵 foi tratado pela via legítima de **reescrever com a incerteza explícita**, não removendo o conteúdo nem inventando fonte. As três ocorrências passaram a atribuir a descrição à literatura gemológica em geral e a declarar que o peso relativo dos dois mecanismos **não está resolvido por medida publicada**. A controvérsia LC-08 fica mais honesta do que estava.

**Fonte:** SkyJems, *Bow-Tie Effect in Faceted Gemstones* · GoodStone, *What Is the Bow-Tie Effect in Elongated Diamonds?* · Ada Diamonds, *Bowties and Light Leakage Explained*. Consultadas em **2026-09-06**.
**Confiança:** em disputa (quanto ao peso relativo) / confirmado (quanto à existência dos dois mecanismos)
**Desfecho:** ✅ **Corrigido com ressalva** — permanece declarado como pergunta aberta, que é o desfecho correto para um LC-08.

---

## Verificado e correto

Alegações de risco que passaram a verificação, com a fonte e a data em que foram conferidas (2026-09-06):

| claim_id | O que foi conferido | Resultado |
|---|---|---|
| `BRI-FAC-CONTAGEM-001` | 57/58 facetas; coroa 33 (mesa + 8 cunhas + 8 estrelas + 16 de cinta), pavilhão 24/25 (8 principais + 16 de cinta + culaça) | ✅ GIA, *Anatomy of a Round Brilliant* |
| `BRI-LIN-TOLK-001` | Tolkowsky 1919, *Diamond Design*, Universidade de Londres, coroa 34,5°, pavilhão 40,75°, mesa 53%, profundidade 59,3%, 33 + 25 facetas | ✅ confirmado nos quatro valores |
| `BRI-LIN-MORSE-001` | Morse, Boston, anos 1860; cinta a 1/3 abaixo da mesa e 2/3 acima da culaça; "corte americano"; máquina de arredondar de Morse e Charles Field, patente de **1874** | ✅ Lang Antiques, *American Jewelry: Part III* |
| Mazarin / Peruzzi (corpo da a01) | brilhante duplo = 17 facetas de coroa; brilhante triplo = 33 facetas de coroa; séculos XVII–XVIII | ✅ Cape Town Diamond Museum |
| `DEG-ESM-CANTO-001` | talhe esmeralda = degrau retangular de cantos truncados; baguete sem truncagem; Asscher = degrau quadrado de cantos truncados | ✅ |
| `DEG-COR-CAMINHO-001` / `PES-PAV-PROFUNDO-001` | pavilhão raso → janela; pavilhão fundo demais → extinção ("cabeça-de-prego") | ✅ GIA, *Colored Stone Cut Quality* — "shallow pavilions create windows, overly deep pavilions create extinction" |
| `CON-BOW-INEVITAVEL-001` | toda pedra alongada tem algum grau de gravata-borboleta; o talhe decide se é suave ou dura | ✅ |
| `MIX-CEI-TRAD-001` | talhe Ceilão = coroa brilhante sobre pavilhão degrau, Sri Lanka, safira e rubi | ✅ |
| `PES-PINTAR-ESCAVAR-001` (direção) | pintar = inclinar em direção ao bisel/principal; escavar = inclinar para longe e uma na direção da outra | ✅ G&G 2006 (o erro estava só no efeito sobre a cinta — achado 3) |
| `MIX-SENT-DOIS-001` | os dois sentidos de "misto" e a divergência entre a literatura anglófona e a de língua portuguesa | ✅ divergência real — LC-08 legítimo, mantido |

## Conformidade com as regras duras do curso

| Regra | Verificação | Resultado |
|---|---|---|
| Nível **teórico** — nenhuma competência de bancada | varredura das 5 aulas por formulações proibidas | ✅ 0 ocorrências; os cinco blocos "O que não concluir" excluem a bancada explicitamente |
| `claim_id` de **4 segmentos**, regex `^[A-Z]{2,4}-[A-Z0-9]+-[A-Z0-9]+-[0-9]{3}$` | 34 IDs conferidos por script | ✅ 34/34 válidos, **nenhum de 5 segmentos** |
| **LC-02** — teto de ~1.600 palavras de corpo | recontagem pela régua do curso após as correções | ✅ a01 1602 · a02 1499 · a03 1507 · a04 1444 · a05 1599 |
| Pré-requisito de **gemologia só por nome** | varredura de wikilinks | ✅ nenhum wikilink para fora do curso |
| Nenhum `claim_id` novo inventado | inventário antes/depois | ✅ 34 antes, 34 depois |

> [!warning] Observação sobre LC-02 na aula 01
> A recontagem pela régua dá **1602** palavras para a aula 01, contra as 1598 declaradas pelo redator — 4 palavras de deriva de medição (marcadores `##` de cabeçalho contados ou não). **O corpo da aula 01 não foi alterado por esta auditoria** (só o rodapé de alegações), então o valor declarado foi mantido em 1598. A folga do "~" cobre a diferença; nada a fazer.

---

## Correções aplicadas

**Aplicadas em:** 2026-09-06

| claim_id | Sev. | Desfecho | Arquivos alterados |
|---|---|---|---|
| `MIX-BAR-WATER-001` | 🔴 | Corrigido | aula 03 (vocabulário, corpo, exemplo, erros comuns, recap, fontes, rodapé) |
| `CON-FORMA-DEFEITO-001` | 🔴 | Corrigido | aula 04 (tabela de contornos, rodapé) |
| `PES-PINTAR-ESCAVAR-001` | 🟠 | Corrigido | aula 05 (manobra 4, erros comuns, recap, fontes, rodapé) |
| `PES-MORTO-PRINCIPIO-001` | 🟠 | Corrigido | aula 05 (exemplo trabalhado, rodapé) |
| `MIX-COM-PADRAO-001` | 🟠 | Corrigido | aula 03 (vocabulário) |
| `CON-BOW-CAUSA-001` | 🔵 | Corrigido com ressalva | aula 04 (corpo, erros comuns, recap, rodapé) |
| `BRI-LIN-EUROP-001` | 🟠 | Corrigido (consistência do manifesto) | aula 01 (rodapé) |

> A linha `BRI-LIN-EUROP-001` é um sétimo ajuste, de **consistência interna do manifesto**: o rodapé da aula 01 chamava o talhe Mazarin de "meio-brilhante", enquanto o corpo da aula — correto — diz "brilhante duplo (Mazarin)". *Meio-brilhante* designa outro talhe. Como o manifesto é o que as skills a jusante leem para montar questões, o rodapé foi alinhado ao corpo. Não alterou o corpo nem a contagem de palavras.

**Arquivos alterados:** aulas 01, 03, 04 e 05. **A aula 02 não foi tocada** — passou a auditoria sem achado.

**Material derivado a propagar:** nenhum. O módulo 10 ainda **não tem questionário**, e os flashcards estão dispensados deste curso a partir do módulo 06. A propagação da Fase 2 é vazia por construção — a auditoria correu antes da avaliação, como o pipeline exige.

**Pendências:** nenhuma. Nenhum achado 🔴 ou 🟠 em aberto; o gate para a revisão didática e o questionário está **liberado**.
