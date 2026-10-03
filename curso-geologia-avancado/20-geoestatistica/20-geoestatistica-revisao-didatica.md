# Revisão didática — Módulo 20: Introdução à geoestatística

**Revisado em:** 2026-09-18 · **Modo:** `review-and-fix`
**Material:** `20-geoestatistica/` — as aulas do módulo, auditadas em conjunto, mais o hub
**Rodou depois de:** auditoria científica de 2026-09-18 (veredito aprovado, 17 achados corrigidos, gate liberado). A ordem da cadeia está correta: nenhuma explicação foi melhorada antes de o fato estar certo.
**Veredito:** **Bem ensinado com ressalvas.** Um achado vermelho de sobrecarga, resolvido por **divisão de aula**; sete achados menores corrigidos localmente. 0 em aberto.

## Resumo

🔴 1 bloqueia · 🟠 3 prejudicam · 🟡 4 atrito · 🔵 2 sugestões

**Carga, antes e depois da divisão:**

| Aula | Antes | Depois | Conceitos novos | Exemplo |
|---|---|---|---|---|
| a01 — Preparação de dados e estatística descritiva | 2.300 pal. · ~26 min | inalterada | 5 (o resto é revisão de estatística clássica) | 1, aritmético |
| a02 — Variáveis regionalizadas e a hipótese intrínseca | **2.505 pal. · ~32 min · 16 conceitos** | **dividida** | — | 1, para 16 conceitos |
| ↳ **nova a02** — Variáveis regionalizadas, função aleatória e estacionariedade | — | 1.960 pal. · ~22 min | 7 | 1, **novo**, classificatório |
| ↳ **nova a03** — Suporte, relação de Krige e anisotropia | — | 1.440 pal. · ~16 min | 5 | 1, o original, preservado |
| a04 — O variograma (era a03) | 2.424 pal. · ~28 min | 2.560 pal. · ~27 min | 11, todos com ancoragem visual | 1, aritmético |
| a05 — Krigagem (era a04) | 2.371 pal. · ~30 min | 2.480 pal. · ~29 min | 10, em 6 seções curtas | 1, aritmético |

O módulo passou de 4 para **5 aulas**, e nenhuma excede o teto de 30 minutos reais.

---

## O diagnóstico central

**Uma aula carregava um módulo inteiro de abstração, e a correção da auditoria a tornou mais pesada.**

A antiga Aula 02 era a única aula inteiramente conceitual do módulo — nenhum número, nenhum gráfico, nenhuma âncora concreta até o exemplo trabalhado no fim — e nela se empilhavam **dezesseis conceitos novos**: variável regionalizada, função aleatória, realização única, estacionariedade de segunda ordem, hipótese intrínseca, variograma (primeira definição formal), variância a priori não limitada, deriva, quase-estacionariedade, vizinhança móvel, krigagem universal, IRF-$k$, suporte, relação de Krige, $\bar\gamma(v,v)$, continuidade, anisotropia geométrica e zonal. O limiar do plugin é "mais de 3 ou 4 ideias independentes numa aula de 30 min".

Duas agravantes específicas deste módulo:

1. **A seção "Estacionariedade" concentrava 624 palavras e doze termos em negrito** — a maior densidade de todo o módulo, na sua passagem mais abstrata.
2. **A correção vermelha da auditoria caiu exatamente ali.** Ao desfazer a afirmação de que a hipótese intrínseca tolera deriva, a auditoria acrescentou dois parágrafos densos e **quatro termos novos** (quase-estacionariedade, vizinhança móvel, krigagem universal, IRF-$k$) à seção que já era a mais pesada. É o efeito que o `audit_preservation_note` do M18 previu e que o M19 registrou: *corrigir o fato tornou a forma pior*. O conteúdo estava certo e precisava continuar ali; o que não cabia era o volume.

O corte natural do material é limpo e único: **o modelo probabilístico** (variável regionalizada, função aleatória, estacionariedade) de um lado, e **as duas consequências práticas desse modelo** (suporte e anisotropia) do outro. As seções "O suporte" e "Continuidade e anisotropia" *usam* o modelo, mas não o constroem — cortar ali não parte nenhum raciocínio ao meio.

---

## Achados

### 🔴 1. Sobrecarga cognitiva na Aula 02 — resolvida por divisão

**id:** `DID-M20-A02-CARGA-001`
**Tipo:** excesso de conceitos novos / ausência de âncora concreta
**Onde:** aula 02 inteira; seção "Estacionariedade" em particular
**Problema:** ver o diagnóstico acima — 16 conceitos novos, todos abstratos, 2.505 palavras, uma única pausa (o exemplo trabalhado, no fim), e a correção vermelha da auditoria empilhada na seção mais densa. Estimativa realista de estudo com compreensão: **~32 min**, acima do teto do plugin, e concentrados no ponto do módulo em que o leitor tem menos apoio concreto para se orientar.
**Escopo:** **exige dividir a aula.**
**Correção aplicada:** divisão em duas aulas, seguindo a convenção dos Módulos 17 e 19 deste curso (duas aulas completas e independentes, com cabeçalho, objetivo, exemplo trabalhado e recap próprios; numeração das aulas seguintes deslocada; nenhuma aula intitulada literalmente "Parte 1/2", mas o par declarado em callout no topo de ambas e no hub).

- **Nova Aula 02 — "Variáveis regionalizadas, função aleatória e estacionariedade"** (1.960 pal., ~22 min). Recebeu as três seções do modelo probabilístico. A antiga seção "Estacionariedade" foi **reorganizada em duas subseções** com título próprio — "Onde exatamente está a folga entre as duas hipóteses" e "E a deriva? Nenhuma das duas a acomoda" —, o que dá ao leitor dois pontos de parada onde antes havia um bloco corrido. Acrescentada uma **frase-âncora** ao fim da primeira (*"as duas hipóteses pedem média constante; só a de segunda ordem pede também variância finita"*), e o tratamento da deriva foi convertido de prosa corrida em **lista de dois itens**.
- **Nova Aula 03 — "Suporte, relação de Krige e anisotropia"** (1.440 pal., ~16 min). Recebeu as duas seções de consequência prática mais o exemplo trabalhado original.

**Nenhuma correção da auditoria foi desfeita, diluída ou reformulada na divisão** — ver a seção "Preservação da auditoria" abaixo.

---

### 🟠 2. A Parte 1 ficaria sem exemplo trabalhado

**id:** `DID-M20-A02-EXEMPLOP1-002`
**Tipo:** abstração sem pausa / exemplo ausente
**Onde:** nova aula 02
**Problema:** a antiga Aula 02 tinha **um único** exemplo trabalhado, e ele é inteiramente sobre a relação de Krige — pertence à Parte 2 sem discussão. A Parte 1 ficaria, então, com 1.230 palavras de abstração pura e **nenhuma pausa**, que é precisamente o defeito que a divisão existia para resolver. Dividir sem criar um exemplo teria trocado uma aula sobrecarregada por uma aula sobrecarregada mais curta.
**Escopo:** correção local (exemplo novo).
**Correção aplicada:** exemplo trabalhado **novo**, criado para esta divisão: três conjuntos de dados descritos qualitativamente, e a tarefa é classificar cada um quanto à hipótese de estacionariedade que se sustenta — (A) variograma com patamar coincidente com a variância a priori, sem tendência → segunda ordem; (B) variograma sem patamar, média constante → só intrínseca; (C) média crescendo monotonicamente numa direção → deriva, nenhuma das duas.

Duas escolhas de desenho merecem registro:

- **O exemplo drila exatamente o achado vermelho da auditoria.** O caso (C) existe para que o leitor erre — a tentação é responder "intrínseca", por raciocinar que a hipótese mais frouxa aceita mais coisas — e a resolução nomeia esse erro explicitamente, num fecho intitulado "O que o exercício treina". O ponto que a auditoria classificou como o mais valioso do módulo passou a ter um exercício dedicado.
- **Nenhuma alegação factual nova foi introduzida.** Cada um dos três casos reproduz uma frase já presente no corpo e já auditada em `GEOEST-M20-A02-HIPOTESEINTRINSECA-002`, apenas reorganizada em formato situação–pergunta–resolução. Não há um único valor numérico. Os nomes de depósito (pórfiro de Cu, laterítico de Ni, veio epitermal de Au) são rótulos de cenário, não afirmações sobre o comportamento típico dessas classes. **Fica sinalizado** para o usuário decidir se quer mandá-lo ao `auditor-cientifico` para checagem pontual, como foi feito nos Módulos 17, 18 e 19.

---

### 🟠 3. "Modelos teóricos" (a04) — três modelos, quinze negritos, um bloco só

**id:** `DID-M20-A04-MODELOSDENSIDADE-003`
**Tipo:** densidade irregular / ausência de consolidação
**Onde:** aula 04 (antiga a03), seção "Modelos teóricos"
**Problema:** 581 palavras e quinze termos em negrito na seção mais longa da aula, apresentando **três modelos comparáveis em três dimensões cada** (comportamento na origem, aproximação ao patamar, quando usar) — nove informações cruzadas, em prosa corrida. É uma tabela escrita como parágrafo. E a correção 🟠 7 da auditoria, que acrescentou a distinção precisa entre os critérios, tornou a seção **mais densa ainda**, pelo mesmo mecanismo do achado 🔴 1.
**Escopo:** correção local.
**Correção aplicada:** a **prosa foi mantida intacta** — ela argumenta, e o argumento corrigido pela auditoria tem valor — e recebeu logo abaixo uma **tabela de consolidação** de três linhas por quatro colunas (modelo · comportamento na origem · como chega ao patamar · quando usar/cautela), seguida de uma instrução de leitura que amarra a tabela ao argumento: *"a primeira coluna separa o gaussiano dos outros dois; a segunda separa o esférico dos outros dois; não existe coluna que separe esférico de exponencial pela origem — é o erro que a seção acima desfez"*. Mesmo padrão do achado `DID-M19-A03-QUADRANTES-009`. Nenhum fato novo: a tabela só reorganiza o que a prosa já diz.

---

### 🟠 4. "Vizinhança de busca" (a05) — um parágrafo de 318 palavras com cinco assuntos

**id:** `DID-M20-A05-VIZINHANCADENSIDADE-004`
**Tipo:** densidade irregular
**Onde:** aula 05 (antiga a04), seção "Vizinhança de busca"
**Problema:** **as duas correções laranjas da auditoria caíram no mesmo parágrafo** (🟠 8, raio de busca; 🟠 9, estabilidade do sistema), e o resultado acumulava, numa única sequência sem respiro: raio ancorado no alcance, o sentido do ajuste, busca em múltiplas passadas, número mínimo, por que o mínimo não é questão de solubilidade, de onde vem a instabilidade numérica real, número máximo e setorização. São **cinco decisões de projeto distintas** apresentadas como se fossem uma. Terceira ocorrência no módulo do mesmo mecanismo: o conteúdo certo, na forma errada.
**Escopo:** correção local.
**Correção aplicada:** o parágrafo foi **reorganizado em três blocos numerados e titulados** — "1. O raio — quão longe buscar", "2. O número mínimo e máximo de amostras — quanta informação aceitar", "3. A setorização — de onde buscar" —, abertos por uma frase que anuncia o critério da divisão (*"cada um responde a um problema diferente"*) e fechados por um parágrafo curto registrando que os três interagem e que o dimensionamento conjunto é hoje quantitativo (QKNA). **Nenhum conteúdo foi acrescentado ou removido**; o texto corrigido pela auditoria está integralmente preservado, apenas segmentado. O nome QKNA, que a auditoria acrescentou às Fontes, passou a ser glosado no corpo em português ("análise quantitativa de vizinhança de krigagem").

---

### 🟡 5. "Estacionariedade" usada na a01 sem glosa, três aulas antes de ser definida

**id:** `DID-M20-A01-ESTACIONARIEDADE-005`
**Tipo:** termo técnico usado antes de definido
**Onde:** aula 01, seção "Histograma, boxplot e o problema dos valores extremos"
**Estava escrito:** "um problema de **estacionariedade** que volta na Aula 02"
**Problema:** o termo aparece **em negrito**, o que sinaliza ao leitor "isto é um conceito", e vem sem uma palavra de explicação. A remissão à aula seguinte é honesta, mas não ajuda quem está lendo *agora* e precisa entender por que um histograma bimodal é um problema. O leitor fica com um rótulo vazio num raciocínio que deveria fechar sozinho.
**Escopo:** correção local (aposto).
**Correção aplicada:** glosa em aposto, meia linha, dizendo o que o termo significa e o que a mistura de populações quebra: *"o nome que a Aula 02 dará à suposição de que a variável se comporta estatisticamente da mesma forma em todo o domínio, suposição que duas populações misturadas quebram"*. Não é definição formal — essa continua sendo da a02 — é o mínimo para o argumento da a01 fechar.

---

### 🟡 6. $\bar\gamma(v,v)$ usada na a03 sem dizer que é um valor fornecido

**id:** `DID-M20-A03-GAMABARRA-006`
**Tipo:** dependência para a frente não sinalizada
**Onde:** aula 03 (Parte 2), seção "O suporte"
**Estava escrito:** "$\bar{\gamma}(v,v)$ [...] calculada a partir do modelo de variograma da Aula 03" (na numeração antiga)
**Problema:** o leitor é convidado a **usar** uma quantidade cujo cálculo pertence a uma aula posterior, e a formulação sugere que ele deveria saber calculá-la. No exemplo trabalhado o valor é simplesmente dado, mas nada no texto diz que é assim que deve ser por enquanto — o leitor atento trava procurando o que não está ali. Segundo problema no mesmo trecho: a relação de Krige, corrigida pela auditoria para exigir um domínio $D$ comum, ficou com essa condição embutida numa frase longa, onde é fácil não registrá-la como *condição de uso*.
**Escopo:** correção local.
**Correção aplicada:** um callout de aviso logo abaixo da equação, com os **dois cuidados** que a fazem funcionar ou falhar, numerados: (1) o domínio $D$ precisa ser o mesmo nos dois termos, e subtrair variâncias de domínios geológicos diferentes não é a relação de Krige; (2) $\bar\gamma(v,v)$ não se calcula dos dados brutos — vem do modelo de variograma da Aula 04, e **até lá trate-a como valor fornecido**, que é como o exemplo trabalhado a apresenta. Nenhum fato novo: o item (1) é a correção da auditoria promovida a condição explícita, e o item (2) é a remissão que já existia, dita de forma utilizável.

---

### 🟡 7. Aula final sem navegação de saída

**id:** `DID-M20-A05-NAVEGACAO-007`
**Tipo:** estrutura / navegação
**Onde:** aula 05, fim
**Problema:** as demais aulas fecham com "## Próxima aula" e um wikilink. A a05, por ser a última, não tinha nada — passava do recap direto para as Fontes, deixando o leitor num beco: nenhum link adiante, nenhum de volta, nenhuma indicação de que o módulo acaba ali **por desenho** e não por arquivo faltando. Mesmo achado que `DID-M19-A06-NAVEGACAO-016`.
**Escopo:** correção local.
**Correção aplicada:** seção "## Anterior" acrescentada na posição em que os Módulos 17, 18 e 19 a colocam, com o backlink da a04, mais uma linha declarando que esta é a última aula do módulo, fechando o arco que a a01 abriu (*"dos dados brutos de furo à estimativa validada de um bloco não amostrado"*), o ponteiro para o Módulo 21 e o retorno ao hub. Os três wikilinks foram conferidos contra o disco e resolvem. Uma seção "## Anterior" também foi acrescentada às novas a03 e a04, que a divisão deixou no meio da cadeia.

---

### 🟡 8. Os cinco blocos `palavras_corpo` desatualizados

**id:** `DID-M20-PALAVRAS-008`
**Tipo:** metadado divergente do material
**Onde:** blocos de metadados das cinco aulas
**Problema:** declarado × real antes desta passagem: a01 2.010 × 2.303; a04 2.080 × 2.556; a05 2.130 × 2.481. As três subestimavam, a a04 em **23%**, e a soma declarada ficava mais de 1.100 palavras abaixo da real — o que desalinha qualquer estimativa de carga feita a partir do metadado, que é exatamente o insumo de decisões como a deste relatório. Mesmo achado que `DID-M19-PALAVRAS-019`.
**Escopo:** correção local.
**Correção aplicada:** os cinco valores sincronizados com a contagem real pós-revisão, arredondados à dezena como é a convenção do curso: **a01 2300 · a02 1960 · a03 1440 · a04 2560 · a05 2480** (contagens exatas: 2.303 / 1.964 / 1.444 / 2.556 / 2.481). Contam Conteúdo + Exemplo trabalhado + Recap, excluindo cabeçalho, navegação e Fontes. Nenhum outro campo do bloco de metadados foi tocado.

---

### 🔵 Sugestões (não são defeitos)

- **`DID-M20-S1` — falta um visual, e é o módulo que mais o pediria.** A a04 descreve em palavras a anatomia de um variograma (curva subindo da origem, intercepto do efeito pepita, platô do patamar, alcance no eixo x) e as três formas de modelo. É um gráfico. Nenhuma das cinco aulas tem apoio visual, e esta é a única do módulo em que a ausência custa — todo o vocabulário da aula é definido *por referência a uma figura que o leitor precisa imaginar*. Um único diagrama com os três elementos anotados serviria à a04 e seria reaproveitado na a05. Fora do escopo desta skill; registrado para o orquestrador.
- **`DID-M20-S2` — o par a02/a03 é candidato natural a uma sessão de `tutor-de-voz`.** A a02 é agora a aula mais conceitual e menos numérica do módulo, e a discriminação que ela treina (segunda ordem × intrínseca × deriva) é do tipo que se consolida respondendo em voz alta, não relendo. O exemplo trabalhado novo já tem o formato de três casos para classificar, que converte diretamente em pergunta socrática.

---

## Cobertura de objetivos

Os quatro objetivos permanecem cobertos, com exemplo trabalhado em cada um. A divisão **não criou objetivo novo** — as duas metades cobrem `oa02`, seguindo o precedente do M19, em que a divisão da Aula 02 deixou a02 e a03 cobrindo `oa02` em conjunto.

| Objetivo | Ensinado em | Exemplo | Avaliação |
|---|---|---|---|
| `oa01` — preparar e descrever dados de furos (composição, distribuições, correlação, regressão) | a01, integral (5 seções) | sim, aritmético (compositing ponderado × média simples) | pendente |
| `oa02` — variável regionalizada, hipótese intrínseca, suporte, continuidade, anisotropia | **a02 + a03**, em conjunto | sim, **dois**: classificatório (hipóteses) na a02; aritmético (relação de Krige) na a03 | pendente |
| `oa03` — calcular e modelar variogramas experimentais | a04, integral (4 seções) | sim, aritmético (ajuste do modelo esférico a 8 lags) | pendente |
| `oa04` — krigagem simples e ordinária, ponto e bloco, validação cruzada | a05, integral (6 seções) | sim, aritmético (sistema de KO resolvido à mão) | pendente |

Nenhum objetivo não coberto. Nenhuma seção órfã: as onze seções de conteúdo do módulo mapeiam para um dos quatro objetivos, e os `mapa_objetivo_secao` das cinco aulas foram reescritos para refletir a nova divisão.

**Efeito da divisão sobre a avaliação:** `oa02` passou a ter **duas aulas e dois exemplos trabalhados**, o que o torna o objetivo mais bem instrumentado do módulo — e, não por acaso, é o que carrega o achado vermelho da auditoria. O gerador de questionários deve tratar a02 e a03 como uma unidade ao cobrir `oa02`.

---

## Preservação da auditoria

**Nenhuma correção da auditoria científica de 2026-09-18 foi desfeita, diluída ou reformulada**, e a reverificação foi feita literalmente após cada edição. Os pontos de maior risco, e onde estão agora:

| Correção da auditoria | Onde estava | Onde está agora | Estado |
|---|---|---|---|
| 🔴 Hipótese intrínseca × deriva | a02, seção Estacionariedade + recap + alegação | nova a02, **duas subseções próprias** + recap + alegação + **exemplo trabalhado novo que a exercita** | intacta e **reforçada** |
| 🟠 Relação de Krige como identidade exata, domínio $D$ | a02, seção Suporte | nova a03, seção Suporte + **callout com os dois cuidados** | intacta e **promovida a condição explícita** |
| 🟠 Anisotropia geométrica × zonal | a02, seção Continuidade | nova a03, **reorganizada em lista de dois itens** | intacta |
| 🟠 Origem não distingue esférico de exponencial | a03, Modelos teóricos + exemplo + recap | a04, mesma prosa + **tabela de consolidação** que a reafirma | intacta e **reforçada** |
| 🟠 Raio de busca ≥ alcance; sistema solúvel com 1 amostra | a04, Vizinhança de busca | a05, **três blocos numerados** | intacta |
| 🟠/🟡 Correções da a01 (viés, 27%, 2,7×, terminologia, independência lógica) | a01 | a01, inalteradas | intactas |
| 🟡 Todas as correções de capítulo bibliográfico | Fontes das 4 aulas | Fontes das 5 aulas, **redistribuídas** conforme o conteúdo de cada metade | intactas |

**Alegações auditáveis e `claim_id`:** as 25 alegações rastreadas continuam todas declaradas, e **nenhum `claim_id` foi renumerado**, apesar de as aulas terem mudado de número. Os prefixos `A02`, `A03` e `A04` passam a designar a **numeração pré-divisão** em que cada alegação foi emitida, e não a posição atual da aula. Isso é deliberado: renumerá-los quebraria a rastreabilidade com `20-geoestatistica-auditoria.json`, que os referencia com desfecho registrado, e a regra do plugin é explícita — `claim_id` não se recicla nem se renumera. Cada aula afetada carrega uma nota de metadados (`nota_claim_id_pre_divisao`, `nota_claim_id_pre_renumeracao`, `nota_alegacoes_migradas`) explicando o descasamento para quem ler o arquivo daqui a meses.

A distribuição ficou assim: `-001` e `-002` (prefixo A02) na **a02**; `-003` e `-004` (prefixo A02) na **a03**, para onde o texto correspondente migrou; as cinco `A03-*` na **a04**; as oito `A04-*` na **a05**.

---

## Propagação para material derivado

**Nada a propagar.** O questionário e os flashcards deste módulo **não existem**, de modo que a renumeração das aulas, a divisão e as correções de cabeçalho não exigem nenhuma reconciliação: serão gerados a partir da versão já corrigida e já dividida. Nada a reimportar no Anki, nenhum card em revisão a corrigir à mão.

O relatório e o manifesto da **auditoria não foram alterados** — nenhum achado desta revisão contradiz, revisa ou reabre achado dela. Os `claim_id` que o manifesto referencia continuam todos válidos e localizáveis (ver a seção anterior).

**Arquivos alterados nesta passagem:** as cinco aulas (duas criadas pela divisão, três renumeradas e editadas), o hub do módulo e este relatório. **Não tocados**, por serem etapa do `geo-operacional`: `00-dashboard.md`, `_curso.md`, `00-progresso-do-aluno.md`, e o `status` / `current_module` / `next_action` do módulo no estado.

### Advertência para quem gerar o questionário e os flashcards

Os `generator_warnings` da auditoria continuam **integralmente válidos** — nenhum valor numérico, nenhuma direção de viés e nenhuma citação foi alterada nesta passagem. Quatro pontos desta revisão os **complementam**:

1. **As aulas mudaram de número.** Qualquer item que remeta a "Aula 03" precisa ser conferido: a antiga a03 (variograma) é a atual **a04**, e a antiga a04 (krigagem) é a atual **a05**. Os `claim_id`, ao contrário, **não** mudaram — não os use para inferir em que aula o conteúdo está.
2. **`oa02` agora tem duas aulas e dois exemplos.** Tratar a02 e a03 como unidade ao cobrir esse objetivo; uma questão que cruze a hipótese de estacionariedade (a02) com o efeito de suporte (a03) é legítima e de alto valor.
3. **O exemplo trabalhado novo da a02 é material de avaliação de primeira qualidade** — os três casos (segunda ordem / só intrínseca / deriva) convertem diretamente em questão de classificação, e o caso (C) é o distrator que a auditoria pediu. Mas note que ele **não foi auditado** (ver achado 🟠 2): use o raciocínio, não invente casos novos por analogia.
4. **A tabela de modelos da a04 é cobrável como tabela.** Depois da consolidação, "qual coluna separa o gaussiano dos outros dois" e "qual coluna *não* separa esférico de exponencial" são perguntas que o material agora responde de forma inequívoca — e são exatamente as duas que o erro corrigido pela auditoria tornava impossíveis.

---

## O que o módulo já fazia bem

Registrado porque é o padrão que as próximas aulas devem imitar, e porque a divisão precisou preservá-lo.

1. **A progressão é a mais limpa do curso até aqui.** Cinco aulas, cinco degraus, cada um insumo direto do seguinte: dados brutos → modelo probabilístico → consequências do modelo → ferramenta de medida → estimador. Cada aula declara no cabeçalho o que a anterior lhe entrega, e entrega ao fim o que a seguinte vai usar. Foi justamente essa limpeza que tornou a divisão fácil: havia um corte natural e só um.
2. **A a01 faz uma coisa que quase nenhum material de geoestatística faz: delimita o que a ferramenta *não* diz.** A seção "correlação e regressão — e o que elas não provam" separa explicitamente correlação entre variáveis no mesmo ponto de continuidade da mesma variável entre pontos, e avisa que o resto do módulo depende de não confundir as duas. É prevenção de erro conceitual antes de o erro ter chance de se formar.
3. **Os quatro exemplos trabalhados são todos aritméticos e todos verificáveis** — o primeiro módulo do curso em que isso acontece. A auditoria refez os quatro número por número. O da a04, em particular, é uma construção excelente: os oito pontos experimentais foram gerados a partir de um modelo esférico real, e o ajuste que a resolução propõe reproduz os dados com erro na terceira casa. Não é um exemplo ilustrativo, é um exemplo que **fecha**.
4. **As analogias são honestas e dizem onde param.** A do termômetro da cidade (para o efeito de suporte) é a melhor do módulo: explica a redução de variância por promediação sem sugerir que o bloco é uma média simples de pontos, e não gera nenhum modelo mental que precise ser desfeito depois.
5. **O hub declara os pontos de dificuldade antes de eles aparecerem** — e depois desta cadeia passou a declarar três, incluindo o que a auditoria identificou como o mais escorregadio do assunto.
