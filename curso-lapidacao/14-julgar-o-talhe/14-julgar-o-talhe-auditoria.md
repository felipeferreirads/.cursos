# Auditoria científica — Módulo 14: Julgar um talhe pronto

> [!info] Curso de **Teoria da lapidação** · módulo 14 de 14 · modo **`audit-and-fix`** · profundidade **`full`** · data **2026-09-07**
> Material auditado: as 4 aulas do módulo (`a01`–`a04`), 20 alegações auditáveis declaradas nos rodapés. Questionário e flashcards **não existem** para este módulo (o gate os bloqueia até esta auditoria fechar; flashcards estão `skipped` desde o módulo 06), logo **não houve propagação para material derivado**.

## Veredito

**Aprovado com correções aplicadas.** 15 achados: **4 🔴**, **10 🟠**, **1 🔵**. Todos os 🔴 e 🟠 foram corrigidos; o 🔵 foi resolvido por substituição de fonte. **Nenhum achado permanece aberto** — o gate de questionário está liberado.

Este é o módulo de encerramento, e a auditoria concentrou-se nos dois riscos que a natureza do módulo cria: **consistência cross-módulo** (ele cita definições fechadas dos módulos 02, 03, 04, 05, 06, 07, 08, 09, 10, 12 e 13) e **procedência de fonte** (o padrão recorrente deste curso, já flagrado nos módulos 09 a 13). Ambos renderam achados 🔴.

| Severidade | Quantidade | Corrigidos | Abertos |
|---|---|---|---|
| 🔴 Erro | 4 | 4 | 0 |
| 🟠 Impreciso | 10 | 10 | 0 |
| 🟡 Desatualizado | 0 | — | 0 |
| 🔵 Sem fonte | 1 | 1 (fonte substituída por outra verificada) | 0 |
| ⚪ Controverso | 0 | — | 0 |

---

## Achados

### 🔴 1. O curso tem **quatro** sentidos de "undercut", não três — e o módulo 09 reconciliou um conjunto diferente

**claim_id:** `JUL-UNDERCUT-CONT-001`
**Tipo:** inconsistência interna + erro de procedência
**Onde:** `a02` · "O defeito de nome ambíguo: undercut"; "Erros comuns"; "Recap relâmpago"; rodapé `DEF-UNDERCUT-SENT-001`

**Está escrito:** *"'Undercut' já apareceu neste curso em **três** sentidos diferentes... o sub-corte da serra fina (módulo 03, aula 01), a depressão por resistência diferencial à abrasão numa esfera ou forma torneada (módulo 07, aula 03), e a socavação de cinta do cabochão (módulo 06, aula 04)."* — e, na fonte do claim: *"as três definições originais de undercut, **já reconciliadas como sentidos distintos pelo módulo 09, aula 05**"*.

**Problema:** dois erros encadeados.
1. O verbete de vocabulário do [[09-geometria-e-diagramas-aula-05-quando-o-meetpoint-nao-fecha-cheater-e-diagnostico|módulo 09, aula 05]] estabelece um **quarto** sentido — *undercut* como a faceta que **para antes** de alcançar o ponto de encontro, oposta ao *overcut*. A aula 02 do módulo 14 omite exatamente esse, que é o sentido mais próximo do assunto do módulo (julgamento de talhe facetado).
2. O módulo 09, aula 05, reconciliou **serra + abrasão diferencial + profundidade de faceta**. Ele **não** menciona a socavação de cinta do cabochão. A fonte do claim atribuía a ele uma reconciliação que ele não fez — erro de procedência interna, o mesmo padrão dos módulos 09–13.

**Correção aplicada:** a lista passou a **quatro** sentidos numerados, com o (4) do módulo 09 incluído e wikilink; e o texto explica por que o sentido (4) não entra neste catálogo sob o nome de *undercut* — na pedra pronta ele se manifesta como **meetline**, não como depressão de superfície. A fonte do claim ganhou ressalva explícita de que a reconciliação dos quatro é feita aqui pela primeira vez. "Erros comuns" e "Recap" foram alinhados.
**Fonte:** `09-geometria-e-diagramas-aula-05...md`, tabela de vocabulário (verbete *overcut / undercut*); `06-cabochao-aula-04...md`, verbete *socavação (undercut)*; `03-maquinas-da-bancada-aula-01...md`, verbete *sub-corte (undercut)*; `07-esfera-e-torneadas-aula-03...md`. · **Nível:** material do próprio curso, já auditado e fechado
**Confiança:** confirmado
**Também aparece em:** nenhum outro arquivo do módulo 14.

---

### 🔴 2. A dicotomia "execução × material" para a extinção é falsa: o curso ensinou **cinco** causas, duas delas de projeto

**claim_id:** `JUL-EXT-DICOT-001`
**Tipo:** inconsistência interna + omissão que gera erro
**Onde:** `a03` · "Mapeando o catálogo às etapas"; "O quadro do diagnóstico"; "Exemplo trabalhado", Passo 1; "Erros comuns"; "Recap"; rodapé `DIA-JAN-ETAPA-001`

**Está escrito:** *"...se a zona escura persistiria mesmo com o ângulo ideal, **a causa é do material**, não do processo"* — e, na tabela: *"| Extinção | facetamento **ou** material | persiste mesmo com o ângulo corrigido → é material |"*.

**Problema:** o [[05-leitura-do-bruto-aula-06-janelamento-e-extincao|módulo 05, aula 06]] fixa **cinco causas independentes** de extinção: (1) pavilhão fundo demais + *head shadow*; (2) índice de refração baixo; (3) saturação de cor alta; (4) estilo de talhe degrau; (5) contorno alongado (*bowtie*). Só (1) é de execução; (2) e (3) são de material; **(4) e (5) são decisões de projeto** — e as duas **persistem** com o ângulo corrigido. A regra diagnóstica escrita, portanto, classifica erradamente duas das cinco causas: leva o aluno a chamar "material" o que é escolha de estilo ou de contorno.

O próprio exemplo trabalhado da aula era um caso da causa omitida: uma **esmeralda em talhe degrau** com zona escura, diagnosticada como "extinção de material, o processo não é o culpado" — quando o estilo degrau é, per o módulo 05, uma causa independente de extinção e é escolha de projeto.

**Correção aplicada:** o parágrafo passou a enumerar as cinco causas com a atribuição correta (1 execução, 2 material, 2 projeto); o teste do ângulo foi reposicionado como o passo que isola **só** a causa de execução; a tabela ganhou a terceira coluna de origem (`projeto`); o Passo 1 do exemplo agora fecha com **duas** causas somadas (saturação = material; talhe degrau = projeto), nenhuma de execução; "Erros comuns" e "Recap" foram reescritos no mesmo sentido; o claim `DIA-JAN-ETAPA-001` foi reformulado com a frase explícita "persistir NÃO implica, por si só, causa de material".
**Fonte:** `05-leitura-do-bruto-aula-06-janelamento-e-extincao.md`, seção "Extinção — cinco causas independentes" e a tabela de causas. · **Nível:** material do próprio curso, já auditado e fechado
**Confiança:** confirmado
**Também aparece em:** `a04`, que herda a distinção — verificado: a lista de irrecortáveis de `a04` cita só causas de material (saturação, heterogeneidade, inclusão/zonação) e continua correta como está.

---

### 🔴 3. O dicionário de facetamento da USFG **não tem** os verbetes *windowing*, *extinction* nem *extra facet*

**claim_id:** `JUL-USFG-VERB-001`
**Tipo:** erro de procedência (fonte não diz o que se afirma que diz)
**Onde:** `a02` · "Fontes consultadas"; rodapé `DEF-JAN-EXT-001`

**Está escrito:** *"United States Faceters Guild, dicionário de facetamento — **verbetes de *windowing*, *extinction*** e defeitos de encontro de facetas."*

**Problema:** o dicionário foi consultado verbete a verbete em 2026-09-07. **Existem:** *meet* ("a term used in judging how well facets come to a point"), *meetpoint*, *girdle*, *scratch* ("a linear gouging on the facet's surface") e *polish*. **Não existem:** *windowing*, *window*, *extinction*, *extra facet*. Os termos são reais e correntes no ofício — mas não vêm dessa fonte. É exatamente o achado 🟠 11 da auditoria do módulo 09 (que constatou a ausência de *overcut* e *undercut* no mesmo dicionário) repetido em outro par de verbetes.

**Correção aplicada:** a linha de fontes foi refeita citando o dicionário **pelos verbetes que ele tem**, com as definições literais, mais uma ressalva nomeando os três que ele não tem. Janela e extinção foram reatribuídos a Sinkankas e a Vargas & Vargas — as fontes externas que o próprio módulo 05, aula 06, já usa para definir os dois termos. O claim `DEF-JAN-EXT-001` recebeu a mesma ressalva.
**Fonte:** United States Faceters Guild, *USFG Faceting Dictionary*, https://usfacetersguild.org/usfg-faceting-dictionary/ — consultado em **2026-09-07**. · **Nível:** normativa (guilda)
**Confiança:** confirmado
**Também aparece em:** ver **Pendência 1** — o rodapé do `05-leitura-do-bruto-aula-06` carrega a mesma atribuição, em módulo fechado, fora do escopo desta auditoria.

---

### 🔴 4. Cinta ondulada **não** cede a repolimento — é geometria, não superfície

**claim_id:** `JUL-REPOL-CINTA-001`
**Tipo:** erro factual + inconsistência interna
**Onde:** `a04` · "O que o recorte consegue: defeitos de execução"; "Recap"; rodapé `REC-EXEC-ALVO-001`

**Está escrito:** *"**Cinta ondulada** e **arranhão de polimento** isolado geralmente cedem a um repolimento leve, que renova só a superfície sem alterar proporção."*

**Problema:** a própria aula 02 deste módulo define cinta ondulada como *"a linha da cinta, vista de perfil, com ondulações em vez de reta — resultado de facetas de cinta desiguais entre si"*, e a aula 03 a atribui às manobras de **pintar e escavar** do módulo 10, aula 05, que alteram a **inclinação e a altura** das facetas de cinta. Isso é geometria de faceta, não estado de superfície. Um repolimento — que por definição "renova só a superfície, sem alterar proporção ou ângulo", conforme o vocabulário da própria `a04` — não pode endireitar uma linha que sobe e desce. Corrigi-la exige recortar as facetas de cinta em toda a volta, com remoção de material do perímetro.

**Correção aplicada:** o parágrafo foi separado em dois itens distintos — **arranhão isolado** como o único item do catálogo que cede a repolimento, e **cinta ondulada** explicitamente marcada como não-cedente, com a razão geométrica. O Recap foi alinhado. O claim `REC-EXEC-ALVO-001` foi reescrito item a item, com registro do que a versão anterior afirmava.
**Fonte:** este mesmo módulo, `a02` (definição de cinta ondulada) e `a04` (vocabulário de *repolimento*); `10-familias-de-talhe-aula-05-onde-o-peso-se-esconde.md` (pintar e escavar alteram a inclinação das facetas de cinta). · **Nível:** material do próprio curso + coerência interna
**Confiança:** confirmado

---

### 🟠 5. O guia de corte do IGS não trata de simetria de contorno de fantasia

**claim_id:** `JUL-IGS-FANTAS-001` · **Tipo:** erro de procedência · **Onde:** `a01` · "Fontes consultadas"; rodapé `JUL-SIM-DOIS-001`
**Está escrito:** *"International Gem Society, *Diamond Cut Quality: Ultimate Guide* — **simetria de reflexão em contornos de fantasia**; proporção como razão, não valor absoluto."*
**Problema:** o guia foi lido em 2026-09-07. A segunda metade da atribuição procede — ele dá proporção em porcentagem (mesa 52–62% da largura; altura de coroa 12,5–17% da profundidade total). A primeira **não**: o guia declara apenas que *"grading fancy diamond cuts (as opposed to round brilliants) involves much looser and more subjective parameters"*, sem qualquer orientação sobre simetria de contorno. Quem cobre isso é outro artigo do mesmo publicador.
**Correção aplicada:** a linha foi dividida em duas — o guia de corte fica com a proporção em porcentagem (com os números literais) e uma ressalva de que não cobre fantasia; a simetria de contorno de fantasia e a razão comprimento:largura passaram para *How to Grade Fancy Cut Diamonds*. Fonte do claim atualizada, com menção ao módulo 10, aula 01.
**Fonte:** IGS, *Diamond Cut Quality: Ultimate Guide*, https://www.gemsociety.org/article/diamond-cuts/ ; IGS, *How to Grade Fancy Cut Diamonds*, https://www.gemsociety.org/article/guide-grading-fancy-shaped-diamonds/ — ambos consultados em **2026-09-07**. · **Nível:** base de referência
**Confiança:** confirmado

---

### 🟠 6. "Proporção" não é uma categoria graduada do sistema de corte da GIA

**claim_id:** `JUL-GIA-CATEG-001` · **Tipo:** erro de procedência · **Onde:** `a01` e `a04` · "Fontes consultadas"; rodapé `JUL-CRIT-QUAT-001`
**Está escrito:** (a01) *"GIA — critérios de avaliação de corte (*cut grading*): simetria, **proporção** e acabamento (*polish*) como categorias distintas de julgamento"*; (a04) *"GIA — critérios de avaliação de corte usados para justificar (ou não) um recorte; **a distinção entre defeito de execução e limitação do material**."*
**Problema:** o sistema da GIA avalia **sete componentes** — brilho, fogo, cintilação, razão de peso, durabilidade, **polimento** e **simetria**. As **proporções** são a base medida a partir da qual razão de peso, durabilidade e os três componentes de aparência são calculados; não são uma categoria graduada à parte. E a GIA não tem nada sobre justificar recorte nem sobre a distinção execução × material — essa é síntese didática deste curso, não categoria daquela fonte.
**Correção aplicada:** a linha da `a01` foi refeita nomeando os sete componentes e o papel das proporções; a linha da `a04` foi substituída pelas fontes que de fato sustentam o que a aula diz (IGS sobre recorte; FTC sobre o que a norma **não** alcança), com registro explícito de que a distinção execução × material é síntese do curso. Fonte de `JUL-CRIT-QUAT-001` atualizada.
**Fonte:** GIA, *A Foundation for Grading the Overall Cut Quality of Round Brilliant Cut Diamonds* (Gems & Gemology, outono 2004) e GIA 4Cs, *Cut* — consultados em **2026-09-07**. · **Nível:** normativa
**Confiança:** confirmado

---

### 🟠 7. "Razão de cúpula" redefinida contra o módulo 06

**claim_id:** `JUL-CUPULA-RAZAO-001` · **Tipo:** inconsistência interna (redefinição de termo fechado) · **Onde:** `a01` · "Proporção — razão, não valor absoluto"; "Recap"
**Está escrito:** *"No cabochão, é a razão de cúpula (**altura sobre largura da base**)"* e, no Recap, *"altura sobre base"*.
**Problema:** o [[06-cabochao-aula-03-geometria-da-cupula-altura-curvatura-luz-engaste|módulo 06, aula 03]] fixa o termo como *"a altura da cúpula dividida pela **menor** dimensão do contorno"*, e usa esse denominador para dar as faixas de referência (~1/3, faixa 1/4–1/2). "Largura da base" é ambíguo e, numa oval 25×18, convida a usar 25 em vez de 18 — o que muda a razão em ~40% e invalida a comparação com a faixa. Um módulo de síntese não pode afrouxar um denominador que o módulo de origem fixou.
**Correção aplicada:** corpo e Recap passaram a "altura da cúpula sobre a **menor** dimensão do contorno".
**Fonte:** `06-cabochao-aula-03-geometria-da-cupula-altura-curvatura-luz-engaste.md`, verbete de vocabulário e seção "Altura: a razão de cúpula". · **Nível:** material do próprio curso, fechado
**Confiança:** confirmado

---

### 🟠 8. O brilhante redondo tem *n* = 8, e não o *n* mais alto que o jogo de índice permite

**claim_id:** `JUL-NFOLD-BRILH-001` · **Tipo:** erro factual + inconsistência interna · **Onde:** `a01` · "Simetria — dois tipos"
**Está escrito:** *"O contorno redondo do brilhante busca o *n* mais alto que o jogo de índice permite."*
**Problema:** o [[10-familias-de-talhe-aula-01-o-talhe-brilhante-facetas-triangulares-e-a-linhagem-do-brilhante-redondo|módulo 10, aula 01]] fixa que o arranjo brilhante repete *"tipicamente oito cópias iguais, giradas de 45°"*, e que as 56 facetas fora da mesa se organizam em **oito setores**. Uma roda de 96 dentes permitiria *n* = 96; o brilhante não o busca. A frase, além de contradizer módulo fechado, confunde a suavidade do **contorno** (aproximado por muitas facetas de cinta) com a **simetria de rotação do arranjo**, que é 8.
**Correção aplicada:** *"O brilhante redondo do módulo 10 tem n = 8 — oito setores repetidos a cada 45° —, e não o n mais alto que o jogo de índice permitiria"*, com wikilink para a aula de origem.
**Fonte:** `10-familias-de-talhe-aula-01...md`, seção "Por que irradiar" e a tabela de contagem de facetas. · **Nível:** material do próprio curso, fechado
**Confiança:** confirmado

---

### 🟠 9. Fechar uma janela custa **largura**, não profundidade

**claim_id:** `JUL-JANELA-DIAM-001` · **Tipo:** erro factual (geométrico) · **Onde:** `a04` · "O que o recorte consegue"; rodapé `REC-EXEC-ALVO-001`
**Está escrito:** *"**Janela** — pavilhão raso demais — recua com um pavilhão recortado mais íngreme, **ao custo de profundidade** e, portanto, de peso."*
**Problema:** a pedra já está pronta; não há material abaixo da culaça para aprofundar o pavilhão. Aumentar o ângulo, numa pedra existente, se faz **estreitando** a peça — removendo material do perímetro da cinta para dentro. O que se perde é largura (e o tamanho aparente de frente), não profundidade. Isso importa porque o próprio curso ensina, desde o módulo 05, que perder tamanho aparente custa mais que a massa.
**Correção aplicada:** reescrito para "o ângulo sobe estreitando a pedra: o custo é de **largura** e, com ela, de peso — nem sempre, mas com frequência", incorporando a ressalva da fonte de que a redução de largura nem sempre é necessária.
**Fonte:** Denver Gem Cutting, *Closing Windows on Faceted Gemstones*, https://www.gemcutting.com/faceting.services/closing.windows.gemstones/index.php — *"it may be necessary to make your gemstone 'narrower', reducing the width of the gemstone, in order to close the window. However, many times we can close a window without reducing the width at all."* Consultado em **2026-09-07**. · **Nível:** prática de oficina relatada por prestador especializado
**Confiança:** confirmado

---

### 🟠 10. Corrigir a socavação de cinta não faz a pedra sair de calibre

**claim_id:** `JUL-SOCAV-CALIBRE-001` · **Tipo:** inconsistência interna · **Onde:** `a04` · "O que o recorte consegue"; rodapé `REC-EXEC-ALVO-001`
**Está escrito:** *"**Undercut de cinta de cabochão** pode ser reduzido desbastando a base... mas ao preço de **encolher a cinta e, com ela, possivelmente sair de calibre**."*
**Problema:** por definição do [[06-cabochao-aula-04-cinta-e-base-onde-o-cabochao-mais-se-estraga|módulo 06, aula 04]], na socavação *"o contorno visto de cima fica **menor** que a base"*. Corrigi-la é desbastar o excesso da **base** até ela alinhar com o topo — o contorno visto de cima, que é justamente o que define o calibre (25×18, 18×13...) naquele módulo, **não muda**. O que se perde é a massa da base alargada. Atribuir perda de calibre a essa correção confunde-a com o caso do **ponto chato de contorno**, que é o defeito caro precisamente porque *ali* o contorno de cima encolhe — e a aula 04 usa o ponto chato dois parágrafos antes como o exemplo canônico de propagação.
**Correção aplicada:** *"o custo é a massa da base alargada, e não o calibre — o contorno visto de cima, que é o que define o calibre no módulo 06, aula 04, não encolhe nessa correção"*, com wikilink.
**Fonte:** `06-cabochao-aula-04-cinta-e-base-onde-o-cabochao-mais-se-estraga.md`, verbete *socavação*, seção de defeitos de cinta e o exemplo trabalhado do ponto chato. · **Nível:** material do próprio curso, fechado
**Confiança:** confirmado

---

### 🟠 11. O recorte não é tratamento, e os gatilhos da FTC não o alcançam

**claim_id:** `JUL-DIVULG-ESCOPO-001` · **Tipo:** confusão de escopo + certeza indevida · **Onde:** `a04` · "A divulgação, quando o recorte acontece"; "Erros comuns"; "Recap"; rodapé `REC-DIVULG-PRINC-001`
**Está escrito:** (Recap) *"Uma pedra recortada muda peso e proporção, e essa mudança **pertence à regra de divulgação do módulo 13**."*; (Erros comuns) *"**Omitir que a pedra foi recortada.** A mudança em peso e proporção é informação que pertence à divulgação, pelo mesmo princípio do módulo 13."*
**Problema:** o [[13-tratamentos-da-oficina-aula-05-oleamento-enceramento-e-a-regra-de-divulgacao-a-fronteira-do-que-o-lapidario-faz|módulo 13, aula 05]] define a "regra de divulgação" com precisão normativa: são os **três gatilhos da FTC (16 CFR § 23.24)** — não permanente, exigência especial de cuidado, efeito significativo sobre o valor —, e todos os três se aplicam a **tratamento**. Recorte não é tratamento e nenhum dos três o alcança. O corpo da aula já ressalvava ("o recorte não é tratamento no sentido daquele módulo"), mas o Recap e "Erros comuns" afirmavam a obrigação como se fosse a mesma norma. Num módulo de encerramento que reativa o 13 por nome, isso desfaz a fronteira que o 13 gastou uma aula inteira construindo — e o módulo 13 chega a advertir contra confundir os três gatilhos da norma com os três pontos didáticos do curso.
**Correção aplicada:** o corpo passou a separar **princípio** de **norma** e a nomear o fundamento efetivo — peso, medidas e qualquer laudo declarado antes do recorte deixam de descrever a pedra entregue. "Erros comuns" foi reformulado como *"Tratar o recorte como um dos tratamentos do módulo 13"*; o Recap foi alinhado; o claim `REC-DIVULG-PRINC-001` foi reescrito e a FTC entrou nas fontes **pelo que não alcança**.
**Fonte:** `13-tratamentos-da-oficina-aula-05...md`, tabela "os três gatilhos × os três pontos"; FTC, *Guides for the Jewelry, Precious Metals, and Pewter Industries*, 16 CFR § 23.24. · **Nível:** normativa
**Confiança:** confirmado

---

### 🟠 12. Cinta ondulada: o texto diz "simetria", a tabela diz "acabamento"

**claim_id:** `JUL-CINTA-CRIT-001` · **Tipo:** inconsistência interna · **Onde:** `a02` · "O quadro do catálogo"; "Exemplo trabalhado"; rodapé `DEF-QUILHA-CINTA-001`
**Está escrito:** a seção que introduz o defeito chama-se *"Defeitos de **simetria e proporção**: quilha deslocada e cinta ondulada"*, mas a linha da tabela diz *"| Cinta ondulada | **proporção / acabamento** | facetado |"*, e o exemplo repete "proporção/acabamento da cinta".
**Problema:** contradição dentro da mesma aula, a três parágrafos de distância. E a classificação externa resolve a favor do cabeçalho: a GIA lista *wavy girdle* entre as características de **simetria**, ao lado de *off-center culet* e da variação de espessura de cinta; *polish* cobre risco, lasca e entalhe de superfície, não a linha da cinta.
**Correção aplicada:** a linha da tabela passou a "simetria / proporção" e o exemplo foi alinhado; o claim `DEF-QUILHA-CINTA-001` ganhou a frase de que a GIA classifica os dois como característica de simetria.
**Fonte:** GIA, características de simetria em avaliação de corte (*extra facet*, *wavy girdle*, *off-center culet*, variação de espessura de cinta) — consultado em **2026-09-07**. · **Nível:** normativa
**Confiança:** confirmado

---

### 🟠 13. Referência à aula errada do módulo 05

**claim_id:** `JUL-M05A06-REF-001` · **Tipo:** erro de procedência interna · **Onde:** `a02` · "Defeitos de proporção óptica"
**Está escrito:** *"O ponto novo desta aula, contra o da **aula 05** do módulo 05..."*
**Problema:** a aula que define janela e extinção é a **06** do módulo 05 ("Janelamento e extinção"); a **05** é "Rendimento". O parágrafo inteiro, inclusive o wikilink imediatamente anterior, aponta para a 06 — o número solto é o único elemento errado, e é o tipo de erro que o aluno leva para a busca no vault.
**Correção aplicada:** "aula 06 do módulo 05".
**Fonte:** `05-leitura-do-bruto-aula-05-rendimento.md` e `05-leitura-do-bruto-aula-06-janelamento-e-extincao.md`. · **Nível:** material do próprio curso
**Confiança:** confirmado

---

### 🟠 14. A causa que o IGS dá para a ondulação de cinta é outra (e é melhor)

**claim_id:** `JUL-IGS-CINTA-001` · **Tipo:** erro de procedência · **Onde:** `a02` · "Fontes consultadas"
**Está escrito:** *"International Gem Society, *Diamond Cut Quality: Ultimate Guide* — culaça deslocada e **ondulação de cinta por facetas de cinta desiguais**."*
**Problema:** o guia atribui as duas coisas a causas trocadas em relação ao que a linha afirma. Ele diz *"uneven pavilion facets create an off-center culet"* (culaça ← facetas de **pavilhão** desiguais) e, sobre a cinta, *"the girdle should wrap around the diamond evenly, instead of rippling up and down"*, atribuindo a ondulação à manobra **deliberada** de economia de peso: *"gem cutters might deliberately cut the girdle this way in order to save weight, a method called painting"*. O achado é de procedência, mas o conteúdo real da fonte **reforça** o curso: é a confirmação externa de que a ondulação de cinta vem de *pintar*, exatamente o que o módulo 10, aula 05, ensina.
**Correção aplicada:** a linha de fontes foi refeita com as citações literais e com a atribuição correta de cada causa, e passou a apontar o wikilink do módulo 10, aula 05, como o ponto do curso que a fonte confirma. `DEF-QUILHA-CINTA-001` recebeu a mesma fonte.
**Fonte:** IGS, *Diamond Cut Quality: Ultimate Guide*, https://www.gemsociety.org/article/diamond-cuts/ — consultado em **2026-09-07**. · **Nível:** base de referência
**Confiança:** confirmado

---

### 🔵 15. Sinkankas creditado por um capítulo de recorte que não se confirmou

**claim_id:** `JUL-SINK-RECORTE-001` · **Tipo:** evidência insuficiente · **Onde:** `a04` · "Fontes consultadas"
**Está escrito:** *"Sinkankas, *Gem Cutting: A Lapidary's Manual* — **recorte e repolimento como retrabalho de pedra já lapidada**; a perda de massa como custo inerente."*
**Problema:** o índice corrente da obra descreve capítulos de cabochão, facetado, esfera e conta, tambor, escultura, gravação, embutido e mosaico. Não foi possível confirmar seção dedicada ao retrabalho de pedra já lapidada. Sinkankas é a espinha bibliográfica do curso e a atribuição pode estar certa — mas não foi verificada, e o resto do módulo tem histórico de super-atribuição.
**Desfecho:** **corrigido com ressalva.** Não se inventou correção nem se removeu Sinkankas: a linha foi rebaixada ao que ele comprovadamente sustenta neste curso (a sequência de trabalho e os defeitos de cinta reativados do módulo 06), e a substância do recorte passou para fontes **verificadas e on-point** que não estavam sendo usadas: a série do IGS sobre recorte e repolimento. Como consequência, a aula ganhou apoio externo direto onde antes tinha só atribuição não conferida.
**Fonte:** IGS, *Re-Cutting, Re-Polishing, and Repairing Gemstones* — em especial *How it Works: Recutting Gems to Maximize Value* (https://www.gemsociety.org/article/recutting-gems-maximize-value/) e *Recutting Diamonds and Colored Gemstones* (https://www.gemsociety.org/article/recutting-diamonds-and-colored-stones/) — consultadas em **2026-09-07**: o recorte pode elevar o valor de uma pedra mal talhada, condicionado a "recut without much weight loss". · **Nível:** base de referência
**Confiança:** não verificado (a atribuição original) / confirmado (a fonte substituta)

---

## Verificado e correto

O que foi conferido e **passou** — registrado para que uma auditoria futura não refaça o trabalho:

| Ponto verificado | Contra o quê | Resultado |
|---|---|---|
| *meetline* como termo do curso, atribuído à `a01`/`a02` ao módulo 12, aula 04 | `12-fancy-cutting-aula-04`, verbete de vocabulário e "Erros comuns" | ✅ correto; o módulo 12 nomeia e define *meetline* como o defeito, e o distingue de *meetpoint* |
| *meetpoint* atribuído ao dicionário da USFG (`a01`) | USFG Faceting Dictionary, 2026-09-07 | ✅ verbetes *meet* e *meetpoint* existem, com as definições citadas |
| *extra facet* como característica de **simetria** da GIA (`a02`) | GIA, características de simetria | ✅ "additional facet placed without regard to pattern symmetry or standard cutting style" |
| *scratch* como característica de **polimento** (`a02`) | GIA e USFG Dictionary | ✅ presente nas duas; a USFG dá "a linear gouging on the facet's surface" |
| Sub-corte da serra fina atribuído ao módulo 03, aula 01 (`a02`) | `03-maquinas-da-bancada-aula-01`, verbete *sub-corte (undercut)* | ✅ correto, inclusive o mecanismo (lâmina fina flexiona sob carga lateral) |
| Socavação de cinta atribuída ao módulo 06, aula 04 (`a02`, `a03`, `a04`) | `06-cabochao-aula-04` | ✅ correto, incluindo o sentido da inclinação (base mais larga que o topo) |
| Undercut de material heterogêneo atribuído ao módulo 07, aula 03 (`a02`, `a03`, `a04`) | `07-esfera-e-torneadas-aula-03` | ✅ correto |
| Pintar e escavar atribuídos ao módulo 10, aula 05 (`a02`) | `10-familias-de-talhe-aula-05` | ✅ correto; o módulo 10 registra que "as duas ondulam a cinta, em pontos opostos" |
| Quilha/culaça deslocada como manobra de peso, não acidente (`a02`, `a03`) | `10-familias-de-talhe-aula-05`, manobra 3 | ✅ correto |
| "Só um talhe mais raso atenua a extinção por saturação, ao custo de brilho" (`a04`) | `05-leitura-do-bruto-aula-06`, "Erros comuns" | ✅ reprodução fiel |
| Razão entre eixos de ovo/esfera e faixas por forma (`a01`) | `07-esfera-e-torneadas-aula-04` (ovo 1,3–1,5:1; obelisco ornamental 3:1–5:1) | ✅ as faixas existem e são por forma |
| Raciocínio de calibre e propagação do ponto chato (`a04`) | `06-cabochao-aula-04`, exemplo trabalhado | ✅ correto (a oval 25×18 vira ~24,3×17,4 e sai do calibre) |
| Wykoff creditado pelo diagnóstico de faceta fora de posição (`a03`) | mesma atribuição já auditada e mantida em `09-geometria-e-diagramas-aula-05` | ✅ consistente com módulo fechado |
| Contaminação de grão e sequência pulada como assinaturas distintas (`a03`) | `04-laps-abrasivos-e-dop-aula-03` e `02-fisica-do-desbaste-aula-03` | ✅ mecanismo reproduzido corretamente |
| Todos os 20 `claim_id` do módulo | regex `^[A-Z]{2,4}-[A-Z0-9]+-[A-Z0-9]+-[0-9]{3}$` | ✅ 20/20 com **4 segmentos**; nenhum com 5 |
| Todos os wikilinks das 4 aulas | arquivos em disco | ✅ todos os alvos existem |
| Regra de não-competência-de-bancada | as 4 aulas | ✅ nenhuma formulação de destreza manual; os quatro blocos "O que não concluir" excluem explicitamente instrumento de bancada, execução de reparo e técnica de recorte |
| Pré-requisito de gemologia | as 4 aulas + hub | ✅ citado só por nome no hub; nenhuma aula cria wikilink para fora do curso |

---

## Correções aplicadas

**Aplicadas em:** 2026-09-07

| claim_id | Sev. | Desfecho | Arquivos alterados |
|---|---|---|---|
| `JUL-UNDERCUT-CONT-001` | 🔴 | Corrigido | `...aula-02-o-catalogo-de-defeitos...md` |
| `JUL-EXT-DICOT-001` | 🔴 | Corrigido | `...aula-03-diagnostico-reverso...md` |
| `JUL-USFG-VERB-001` | 🔴 | Corrigido | `...aula-02-o-catalogo-de-defeitos...md` |
| `JUL-REPOL-CINTA-001` | 🔴 | Corrigido | `...aula-04-recorte...md` |
| `JUL-IGS-FANTAS-001` | 🟠 | Corrigido | `...aula-01-os-criterios...md` |
| `JUL-GIA-CATEG-001` | 🟠 | Corrigido | `...aula-01-os-criterios...md`, `...aula-04-recorte...md` |
| `JUL-CUPULA-RAZAO-001` | 🟠 | Corrigido | `...aula-01-os-criterios...md` |
| `JUL-NFOLD-BRILH-001` | 🟠 | Corrigido | `...aula-01-os-criterios...md` |
| `JUL-JANELA-DIAM-001` | 🟠 | Corrigido | `...aula-04-recorte...md` |
| `JUL-SOCAV-CALIBRE-001` | 🟠 | Corrigido | `...aula-04-recorte...md` |
| `JUL-DIVULG-ESCOPO-001` | 🟠 | Corrigido | `...aula-04-recorte...md` |
| `JUL-CINTA-CRIT-001` | 🟠 | Corrigido | `...aula-02-o-catalogo-de-defeitos...md` |
| `JUL-M05A06-REF-001` | 🟠 | Corrigido | `...aula-02-o-catalogo-de-defeitos...md` |
| `JUL-IGS-CINTA-001` | 🟠 | Corrigido | `...aula-02-o-catalogo-de-defeitos...md` |
| `JUL-SINK-RECORTE-001` | 🔵 | Corrigido com ressalva (fonte substituída por outra verificada) | `...aula-04-recorte...md` |

**Propagação:** nenhuma necessária. O módulo 14 não tem questionário nem baralho (gate respeitado: nenhum foi gerado antes desta auditoria; flashcards estão `skipped` desde o módulo 06). O hub `14-julgar-o-talhe-modulo.md` não repete nenhum dos dados corrigidos. O `_curso.md` não repete nenhum deles.

**Impacto na régua LC-02** (recontagem após as correções, régua de 2026-09-02):

| Aula | Antes | Depois | Teto |
|---|---|---|---|
| a01 | 1557 | **1581** | ~1600 ✅ |
| a02 | 1500 | **1577** | ~1600 ✅ |
| a03 | 1549 | **1600** | ~1600 ✅ |
| a04 | 1459 | **1599** | ~1600 ✅ |

Onde a correção acrescentou substância (as cinco causas de extinção na `a03`; os quatro custos de recorte na `a04`), cortou-se redundância no mesmo arquivo para caber no teto: nenhuma aula precisou ser dividida, e nenhuma teve conteúdo comprimido.

**Pendências:**

1. **Fora do escopo desta auditoria — módulo 05, aula 06.** O rodapé de `05-leitura-do-bruto-aula-06-janelamento-e-extincao.md` traz, na fonte de `JAN-EXT-DEF-001`, a atribuição *"United States Faceters Guild — dicionario de facetamento (windowing, extinction)"* — o **mesmo erro** do achado 🔴 3, num módulo fechado. Não foi tocado (a auditoria estava restrita ao módulo 14) e não bloqueia o gate do módulo 14. Fica registrado aqui para uma passada `cross-course` ou uma reabertura pontual do módulo 05. Correção sugerida: reatribuir a Sinkankas e a Vargas & Vargas, que a mesma linha já cita, e acrescentar a ressalva de ausência dos verbetes.
2. **Nada mais em aberto.** Nenhum achado 🔴 ou 🟠 pendente. O gate para `revisor-didatico` e para `gerador-de-questionarios` está liberado.
