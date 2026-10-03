# Revisão didática — Módulo 21: Modelagem geoestatística de depósitos minerais

**Revisado em:** 2026-09-19 · **Modo:** `review-and-fix`
**Material:** as 5 aulas do módulo (hoje 6, após a divisão descrita no 🔴 1) e o hub do módulo
**Entradas auxiliares:** `21-modelagem-geoestatistica-depositos-minerais-auditoria.md` (auditoria científica de 2026-09-18, veredito aprovado) e `course-state.yaml`
**Veredito:** **Bem ensinado com ressalvas** — o conteúdo é sólido e a auditoria o deixou correto; o que faltava era forma. Dois achados bloqueavam, e os dois estão corrigidos.

## Resumo

🔴 2 bloqueiam · 🟠 4 prejudicam · 🟡 4 atrito · 🔵 3 sugestões

**Todos os 🔴 e 🟠 foram corrigidos nesta passagem.** O módulo passou de **5 para 6 aulas**.

**Carga, antes e depois:**

| Aula | Antes (palavras · min) | Depois | Situação |
|---|---|---|---|
| a01 | 1.980 · ~28 min | 1.980 · ~28 min | ok |
| a02 | 1.790 · ~27 min | 1.790 · ~27 min | ok (o bloco declarava 2.030 — 13% acima do real) |
| a03 (antiga) | **2.440 · ~30 min** | — | **dividida** |
| ↳ nova a03 | — | 1.860 · ~25 min | ok |
| ↳ nova a04 | — | 1.270 · ~17 min | ok |
| a05 (ex-a04) | 2.220 · ~28 min | 2.220 · ~28 min | ok |
| a06 (ex-a05) | 2.420 · ~29 min | 2.420 · ~29 min | ok |

Nenhuma aula do módulo está no teto de 30 min. A a06, a mais longa, é a menos densa por natureza (geométrica e descritiva) e não pede divisão.

---

## Achados

### 🔴 1. A Aula 03 estava no teto de carga, e a auditoria a empurrou contra ele

**claim_id:** `DID-M21-A03-CARGA-001`
**Tipo:** excesso de conceitos novos / sobrecarga cognitiva
**Onde:** antiga Aula 03 — "Variograma e krigagem de variáveis indicadoras", inteira
**Problema:** a aula já declarava **30 min**, o teto do plugin, **antes** da auditoria. As correções de 2026-09-18 acrescentaram dois blocos densos à mesma aula — a separação entre "variância de krigagem negativa" e "probabilidade fora de $[0,1]$" (achado 🔴 1 da auditoria) e o *trade-off* SIK × OIK (achado 🟠 8) — levando-a a **2.440 palavras**, contra 1.790–2.440 nas demais. A aula acumulava, num só fôlego: fórmula do variograma indicador, leitura como pares discordantes, patamar $F(1-F)$, modelo autorizado, dois sintomas distintos com duas causas distintas, *full IK* × *median IK*, pesos independentes do limiar, sistema de krigagem, OIK × SIK, ccdf local, relação de ordem e algoritmo de correção. São doze ideias independentes numa aula de 30 min — o triplo do que a skill considera sustentável.

O sintoma didático mais claro: **o único exemplo trabalhado estava no fim**, depois de oito páginas de teoria, e servia apenas ao último terço do conteúdo. O leitor atravessava as três primeiras seções sem nenhuma pausa e sem nenhuma oportunidade de aplicar o que acabara de ler.

**Correção aplicada:** divisão em duas aulas, pelo corte que a própria auditoria sugeriu — e que o texto já trazia pronto, porque a fronteira entre "modelar o variograma" e "resolver a krigagem" é uma fronteira de assunto, não um corte arbitrário de comprimento:

- **Aula 03 — "Variograma indicador: cálculo, modelos autorizados e escolha da abordagem"** (~1.860 pal., ~25 min, 5 conceitos, cobre `oa02`). Seções: o variograma experimental indicador; modelos autorizados versus não autorizados; mediana indicadora versus krigagem indicadora completa. ID `m21-a03` preservado.
- **Aula 04 — "Krigagem indicadora: sistema, interpretação e violações de relação de ordem"** (~1.270 pal., ~17 min, 4 conceitos, cobre `oa03`). Seções: o sistema de krigagem indicadora; violações de relação de ordem; exemplo trabalhado original. Aula **nova**; o ID `m21-a04` foi **reatribuído**.

As antigas Aulas 04 (krigagem log-normal) e 05 (wireframes) foram renumeradas para **05** e **06**, com título, ID, arquivo e referências internas atualizados e **zero alteração de conteúdo científico**.

**Ganho colateral no alinhamento objetivo ↔ aula.** A auditoria havia registrado (observação fora de escopo 6) que nenhum objetivo do módulo tinha correspondência 1:1 com uma aula — o `oa02` era coberto pela a02 inteira mais três seções da a03, e o `oa03` pelas duas outras seções da a03 mais a a04 inteira. A divisão caiu exatamente nessa costura: agora `oa02` = a02 + a03 e `oa03` = a04 + a05, cada objetivo com aulas inteiras e não com fatias de aula.

**Escopo:** exigiu dividir a aula.
**Desfecho:** **corrigido** (divisão aplicada).

---

### 🔴 2. Título de seção contradizendo o corpo que a auditoria acabara de corrigir

**claim_id:** `DID-M21-A05-TITULOSECAO-002`
**Tipo:** título que não corresponde ao que a seção faz
**Onde:** Aula 05 (ex-04) · cabeçalho "### Krigagem log-normal baseada em krigagem ordinária **(correção aproximada)**", replicado no `mapa_objetivo_secao` e ecoado no exemplo trabalhado
**Problema:** o achado ⚪ 9 da auditoria **inverteu** o diagnóstico do redator: a fórmula $Z^*_{OLN}=\exp[Y^*_{OK}+\sigma^2_{OK}/2-\mu]$ **não** é aproximada nem heurística — é a forma padrão, derivada por Journel (1980) e reproduzida sem variação nos tratados. O corpo da seção foi reescrito e passou a dizer isso com todas as letras ("Essa fórmula é **padrão e não é objeto de divergência**"). **O título não foi atualizado junto.**

O resultado é a pior configuração possível para material autodidata: o leitor que percorre os títulos — e o leitor que volta à aula para revisar, que é justamente quem lê títulos e recaps — leva embora "correção aproximada", exatamente a caracterização que a auditoria classificou como insustentável. Pior: o **aviso 5 ao gerador de questionários** diz, literalmente, "não gerar item que descreva a fórmula como 'heurística' ou 'aproximada'" — e o gerador leria esse título. O título sozinho reintroduzia o erro corrigido.

**Correção aplicada:** título → "### Krigagem log-normal baseada em krigagem ordinária **(o termo do multiplicador de Lagrange)**", que descreve o que a seção de fato faz. `mapa_objetivo_secao` sincronizado. No exemplo trabalhado, "(a correção aproximada específica da versão baseada em krigagem ordinária)" → "(específico da versão baseada em krigagem ordinária, onde a média é desconhecida)" — formulação retirada literalmente do corpo já corrigido ("ele é o preço, no espaço logarítmico, de a média ser desconhecida").

**Escopo:** correção local. Nenhum fato novo introduzido.
**Desfecho:** **corrigido**

---

### 🟠 3. A Parte 1 ficaria sem exemplo trabalhado e sem pausa

**claim_id:** `DID-M21-A03-EXEMPLOP1-003`
**Tipo:** ausência de pausa / exemplo tarde demais
**Onde:** nova Aula 03
**Problema:** o exemplo trabalhado da aula original é aritmético e resolve o **sistema de krigagem** — ele pertence inteiro à Parte 2. Dividir sem mais nada deixaria a Parte 1 com três seções conceituais seguidas e nenhum momento de aplicação, que é precisamente o defeito de densidade que a divisão pretendia curar.

**Correção aplicada:** exemplo trabalhado **novo** na Parte 1, construído para exercitar os três pontos de maior valor da parte — e deliberadamente **não aritmético pesado**, para não duplicar o registro da Parte 2:

> Três limiares (decil 1, mediana, decil 9) com patamar e alcance ajustados. (a) Conferir os patamares contra $F(1-F)$ — $0{,}10\times0{,}90=0{,}09$; $0{,}50\times0{,}50=0{,}25$; $0{,}90\times0{,}10=0{,}09$. (b) Decidir se a mediana indicadora é defensável — não é: o decil 9 tem alcance de 40 m contra 90–95 m dos outros dois, que é o padrão geológico de alto teor mais localizado antecipado na Aula 02. (c) Explicar por que a mediana é o limiar de referência — porque $F(1-F)$ é máxima ali.

O item (b) é o de maior valor: ele faz o leitor **exercer** a decisão *full IK* × *median IK* com evidência, em vez de memorizar a definição das duas. A aritmética são três multiplicações de duas casas, conferidas.

**Nenhuma alegação factual nova foi introduzida.** Cada passo reaplica afirmação já auditada: `GEOMOD-M21-A03-PATAMARF-008` (patamar $=F(1-F)$, máximo $0{,}25$ na mediana), `GEOMOD-M21-A03-MEDIANAINDICADORA-004` (a hipótese da mediana indicadora) e `GEOMOD-M21-A02-VARIOGRAMAPORLIMIAR-005` (alcance menor em limiares altos). Os valores da tabela são ilustrativos e declarados como hipotéticos no enunciado, no mesmo padrão dos demais exemplos do módulo.

> **Sinalizado ao `auditor-cientifico`:** o exemplo é novo e **não foi auditado**. Ele não afirma nada fora das três alegações acima, mas se o usuário quiser rigor completo, cabe uma checagem pontual — mesmo procedimento adotado no Módulo 20 para o exemplo novo criado na divisão da antiga a02.

**Escopo:** correção local (conteúdo novo, sem fato novo).
**Desfecho:** **corrigido**

---

### 🟠 4. Lista de Fontes da Aula 03 com capítulos que a auditoria já havia corrigido

**claim_id:** `DID-M21-FONTES-A03-004`
**Tipo:** inconsistência interna visível ao leitor
**Onde:** antiga Aula 03 · seção "Fontes"
**Problema:** a auditoria corrigiu, nos achados 🟡 10 e 🟡 12, as citações de Isaaks & Srivastava (cap. 19 → **cap. 18, *Estimating a Distribution***) e de Goovaerts (cap. 6 → **cap. 7, *Assessment of Local Uncertainty***). A correção chegou aos campos `source` dos blocos de alegações da a03 — mas **não à lista de Fontes visível**, que continuava mandando o leitor ao capítulo errado. O mesmo arquivo trazia as duas versões, e a que o aluno lê é a errada.

Isto é achado de atribuição e, a rigor, matéria do `auditor-cientifico`. Não estou reabrindo nada: a correção já estava **decidida e verificada** no relatório de 2026-09-18, o que faltou foi **propagá-la**. A propagação é mecânica.

**Correção aplicada:** as listas de Fontes das novas Aulas 03 e 04 trazem os capítulos corrigidos, **com o título do capítulo além do número** — que é a mitigação que a própria auditoria recomendou, já que o número é a parte não confirmada e o título é a parte verificada. As Fontes das Aulas 05 e 06 foram conferidas e já estavam corretas.

**Escopo:** correção local.
**Desfecho:** **corrigido**

---

### 🟠 5. A mudança de natureza do módulo não estava preparada

**claim_id:** `DID-M21-A06-TRANSICAO-005`
**Tipo:** dificuldade desproporcional / transição não preparada
**Onde:** fim da Aula 05 (ex-04) → abertura da Aula 06 (ex-05)
**Problema:** as Aulas 01 a 05 são quantitativas — fórmulas, sistemas, estimadores, vieses. A Aula 06 é geométrica e, em boa parte, **qualitativa**: correlacionar contatos entre furos, decidir domínio rígido ou suave, julgar geologicamente. A própria a06 sinaliza a mudança, mas só na **segunda seção**, quando o leitor já entrou. O anúncio na a05 era uma linha protocolar de "Próxima aula", sem nenhum aviso de que o registro ia mudar.

Para material autodidata isso custa caro: o leitor chega esperando mais uma dedução e encontra julgamento geológico, e a reação típica é achar que a aula "ficou fraca" ou que perdeu alguma coisa — quando o que mudou foi o tipo de raciocínio pedido.

**Correção aplicada:** parágrafo acrescentado ao "Próxima aula" da Aula 05, nomeando a mudança de registro, dizendo o que ela **não** é (um desvio) e o que ela é (o passo que amarra a estimativa a um corpo geológico com forma, volume e limites). Sem nenhum fato novo — é a mesma leitura que a própria a06 faz de si.

**Escopo:** correção local.
**Desfecho:** **corrigido**

---

### 🟠 6. O recap não recapitulava o que a auditoria tinha acabado de acrescentar

**claim_id:** `DID-M21-A04-RECAP-006`
**Tipo:** recap que não recapitula
**Onde:** antiga Aula 03 · "Recap relâmpago"
**Problema:** o achado 🟠 8 da auditoria reescreveu o parágrafo de OIK × SIK como um *trade-off* explícito, com as duas posições — e conectou-o diretamente ao achado vermelho (a OIK é mais propensa a estimativas fora de $[0,1]$ porque a média global não recebe peso). É um dos pontos mais cobráveis do módulo. **Nada disso chegou ao recap**, que continuava com os cinco marcadores da versão pré-auditoria.

Um recap que omite o ponto mais recém-reforçado da aula ensina ao leitor que aquilo era acessório.

**Correção aplicada:** o recap da nova Aula 04 tem três marcadores, e o **segundo** é o *trade-off* OIK × SIK — restatement direto da alegação `GEOMOD-M21-A03-SIKVSOIK-009`, sem fato novo. O recap da nova Aula 03 recebeu, no primeiro marcador, a informação de que o patamar do variograma indicador **não é parâmetro livre de ajuste** ($=F(1-F)$), que é a âncora do novo exemplo trabalhado daquela parte.

**Escopo:** correção local.
**Desfecho:** **corrigido**

---

### 🟡 7. A Aula 01 abre argumentando o que o leitor já aceitou

**claim_id:** `DID-M21-A01-ABERTURA-007`
**Tipo:** redundância / ordem invertida
**Onde:** Aula 01 · primeira seção, "Por que a base de dados vem antes da geoestatística"
**Problema:** a aula declara o Módulo 20 inteiro como pré-requisito e então gasta a primeira seção **defendendo** que a base de dados vem antes da geoestatística. Quem chegou aqui já aceitou isso — foi o que o trouxe. O conteúdo do parágrafo é útil (ele diz o que o M20 assumiu pronto e o que este módulo faz um passo acima), mas o título o enquadra como um argumento a ser vencido, e o leitor gasta atenção conferindo uma tese em vez de se orientar.

**Correção aplicada:** título → "### O que o Módulo 20 assumiu pronto". A primeira frase do parágrafo já era exatamente isso ("O Módulo 20 tratou a base de dados como algo já pronto"), de modo que o retítulo, sozinho, converte a seção de argumento em orientação. Texto do parágrafo preservado; `mapa_objetivo_secao` sincronizado.

**Escopo:** correção local (mínima, uma linha).
**Desfecho:** **corrigido**

---

### 🟡 8. Termos técnicos usados antes de qualquer sinalização

**claim_id:** `DID-M21-A01-TERMOS-008`
**Tipo:** termo técnico usado antes de definido (*forward reference* não declarada)
**Onde:** Aula 01 · primeira seção ("compostos por bancada") e última seção ("teor de corte")
**Problema:** os dois vêm do Módulo 20, o que é legítimo — o problema é que a **primeira ocorrência** de cada um não sinaliza isso. "Teores compostos por bancada" aparece na terceira linha da aula sem nenhuma âncora; mais adiante a mesma aula credita a composição por bancada ao M20, mas tarde demais. "Teor de corte" aparece num parêntese de exemplo e só é caracterizado na Aula 02.

Para um leitor que fez o M20 há semanas — o caso normal num curso autodidata — a diferença entre "termo que eu deveria saber" e "termo que será explicado" decide se ele para e volta ou se segue em frente.

**Correção aplicada:** duas glosas em aposto, ambas de **ponteiro** e não de definição — a definição existe e está auditada onde deve estar, repeti-la aqui seria reensinar o pré-requisito no meio da aula:
- "teores compostos por bancada **(Módulo 20, Aula 01)**"
- "(por exemplo, o **teor de corte** econômico, **definido na Aula 02**)"

**Checado e não é achado:** a a02 menciona a *local ccdf* como "a peça central" antes de a a04 construí-la — a auditoria levantou isso, mas a primeira ocorrência **já vem glosada** ("função de distribuição acumulada local, distribuição condicional aos dados vizinhos") e já declara onde será usada. É *forward reference* bem feita. Só atualizei o destino do ponteiro, que a divisão mudou de Aula 03 para Aula 04.

**Escopo:** correção local.
**Desfecho:** **corrigido**

---

### 🟡 9. Nenhuma aula tinha navegação de saída; a última não fechava o arco

**claim_id:** `DID-M21-NAVEGACAO-009`
**Tipo:** estrutura / orientação
**Onde:** todas as aulas (ausência de "## Anterior"); Aula 06 (ex-05), ausência de fecho
**Problema:** as aulas do módulo tinham "Próxima aula" mas não o retorno, quebrando a convenção estabelecida no Módulo 20 (achado `DID-M20-A05-NAVEGACAO-007`). E a última aula do módulo simplesmente terminava no recap: sem fecho do arco, sem dizer que o módulo acaba ali por desenho, sem ponteiro para o Módulo 22 no lugar onde o leitor está quando termina.

**Correção aplicada:** seção "## Anterior" acrescentada às Aulas 03, 04, 05 e 06, imediatamente antes de "## Fontes", seguindo o formato do M20 — com a marcação "(Parte 1 deste par)" no retorno da a04 para a a03. A Aula 06 recebeu, além do retorno, o parágrafo de fecho: o arco que vai da base bruta de furos ao modelo de blocos codificado por domínio, o ponteiro para o Módulo 22 e o link de volta ao hub.

As Aulas 03 e 04 receberam ainda um *callout* de abertura declarando que são **Parte 1 e Parte 2 de um par**, com link recíproco — para que quem cair na a04 por busca saiba imediatamente que o variograma que ela usa foi modelado na anterior.

**Escopo:** correção local.
**Desfecho:** **corrigido**

---

### 🟡 10. Blocos `palavras_corpo` dessincronizados

**claim_id:** `DID-M21-PALAVRAS-010`
**Tipo:** metadado desatualizado
**Onde:** blocos de metadados das cinco aulas originais
**Problema:** os valores declarados divergiam do texto real, e a maior divergência era na a02 — **2.030 declaradas contra 1.790 reais**, 13% acima. Metadado de carga que não bate com o texto é pior que metadado ausente: é exatamente o campo que uma revisão futura (ou o próprio gerador) consulta para decidir se uma aula precisa ser dividida.

**Correção aplicada:** seis valores sincronizados com a contagem real do corpo (Conteúdo + Exemplo + Recap): a01 1.980; a02 1.790; a03 1.860; a04 1.270; a05 2.220; a06 2.420. Durações estimadas ajustadas na mesma passagem para as duas aulas novas (~25 min e ~17 min).

**Escopo:** correção local.
**Desfecho:** **corrigido**

---

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo trabalhado | Situação |
|---|---|---|---|
| `oa01` — consolidar e validar bases; montar modelos de blocos | Aula 01 (integral) | sim (validação do DDH-014, não numérico) | **1:1 com a aula** |
| `oa02` — transformar em indicadoras e modelar seus variogramas, distinguindo modelos autorizados | Aula 02 (integral) + Aula 03 (integral) | sim, **dois**: tabela de indicadoras (a02) e leitura de três variogramas por limiar (a03, novo) | coberto por par de aulas inteiras |
| `oa03` — aplicar e interpretar krigagem indicadora e krigagem log-normal | Aula 04 (integral) + Aula 05 (integral) | sim, **dois**, ambos aritméticos e auditados: sistema de krigagem indicadora (a04) e retransformação log-normal (a05) | coberto por par de aulas inteiras |
| `oa04` — construir wireframes e integrá-los por operações lógicas | Aula 06 (integral) | sim (bissetriz e circuncírculo, não numérico) | **1:1 com a aula** |

Nenhum objetivo ficou descoberto, nenhuma seção ficou órfã, e todos os quatro têm exemplo trabalhado. **A divisão melhorou o mapeamento**: antes, dois objetivos eram cobertos por fatias de uma mesma aula; agora cada objetivo é coberto por aulas inteiras.

**Para o gerador de questionários:** trate **a02+a03 como unidade** ao cobrir `oa02` e **a04+a05 como unidade** ao cobrir `oa03`.

---

## Preservação das correções da auditoria

Nenhuma correção da auditoria científica de 2026-09-18 foi desfeita, diluída ou reformulada. O texto científico das seções migradas foi **copiado literalmente** do arquivo auditado, não reescrito. Reverificação literal após cada edição, com atenção aos pontos de maior risco:

| Correção da auditoria | Onde está agora | Situação |
|---|---|---|
| 🔴 1 — dois sintomas, duas causas (variância negativa × fora de $[0,1]$) | nova a03, seção "Modelos autorizados…" + recap | **intacta e reforçada** — o recap da a03 a mantém integral, e a nova a04 a reencontra em "Violações de relação de ordem" |
| 🟠 2 — a KO não assume distribuição (robustez × otimalidade) | a02, inalterada | intacta |
| 🟠 3 — tangencial simples ≠ tangencial balanceado | a01, inalterada | intacta |
| 🟠 4 — Delaunay maximiza o menor ângulo **da triangulação**; unicidade só em posição geral | a06, inalterada | intacta |
| 🟠 5 — mediana indicadora: pesos independentes do limiar, um sistema por bloco | nova a03, seção "Duas abordagens" + recap | **intacta e reforçada** pelo novo exemplo trabalhado, item (b) |
| 🟠 6 — $F(z_c)\approx0{,}33$ e remoção de "variância máxima teórica" | nova a04, exemplo trabalhado (original, preservado) | intacta; **promovida** no recap da a03 ("patamar não é parâmetro livre") |
| 🟠 7 — aritmética do exemplo a 4 casas ($0{,}0998$/$0{,}1352$/$0{,}1794$ → $\lambda_1=0{,}794$) | nova a04, exemplo trabalhado, **copiado sem uma vírgula de diferença** | intacta |
| 🟠 8 — OIK × SIK como *trade-off*, não preferência | nova a04, seção "O sistema de krigagem indicadora" | **intacta e promovida ao recap**, que antes a omitia (🟠 6 desta revisão) |
| ⚪ 9 — fórmula log-normal OK é padrão (Journel 1980), controvérsia em Roth/Yamamoto | a05, corpo e recap intactos | **intacta e agora coerente com o título** (🔴 2 desta revisão) |
| 🟡 10–13 — capítulos bibliográficos | Fontes das a03/a04 corrigidas; a02, a05, a06 já estavam | **propagação concluída** (🟠 4 desta revisão) |
| 🟡 14 — as duas bases percentuais (8% / 9%) | a05, exemplo trabalhado, inalterado | intacta |
| 🟡 15 — faixa 1/4–1/2 como ponto de partida, confirmada por QKNA | a01, inalterada | intacta |

**As 27 alegações auditáveis continuam todas declaradas e nenhum `claim_id` foi renumerado.** Os prefixos `A03` designam a numeração **pré-divisão** em que cada alegação foi emitida, não a posição atual da aula — renumerá-los quebraria a rastreabilidade com o relatório e o manifesto da auditoria. A distribuição após a divisão:

- **nova a03:** `-001` (variograma indicador), `-002` (modelo autorizado), `-003` (sintoma do modelo não autorizado — o vermelho), `-004` (mediana indicadora)
- **nova a04:** `-005` (sistema IK), `-009` (SIK × OIK), `-006` (relação de ordem), `-007` (exemplo numérico), `-008` (patamar $F$)

---

## Encaminhado ao `auditor-cientifico` (não tratado aqui)

Dois pontos de fato, deixados intactos por não serem matéria desta skill:

1. **O fator 2 na leitura do variograma indicador.** A a03 diz que "o variograma indicador é, portanto, uma **proporção de pares discordantes** naquela distância". Com o fator $\frac{1}{2N(h)}$ da própria fórmula impressa logo acima, $\hat\gamma_I(h)$ é a **metade** dessa proporção — a proporção é $2\hat\gamma_I(h)$. A afirmação foi verificada pela auditoria (azul B12, alegação `GEOMOD-M21-A03-VARIOGRAMAINDICADOR-001`) e **não a alterei**. Registro para uma checagem pontual: a leitura vale exatamente para $2\gamma$, e a diferença muda o resultado de qualquer questão que peça o número.
2. **Numeração interna divergente numa nota de revisão.** A alegação `GEOMOD-M21-A01-TAMANHOBLOCO-004` traz, na sua nota, "auditoria 🟡 16"; o relatório numera esse achado como 🟡 15. Divergência de escrituração, sem efeito sobre o conteúdo — e consistente com a discrepância de contagem de amarelos já registrada no manifesto da auditoria.

---

## O que está bem feito

Vale registrar, porque tem de sobreviver às próximas revisões:

- **A escada de transformações é exemplar.** O módulo apresenta três caminhos para o mesmo problema — indicadora (a02–a04), logaritmo (a05), geometria (a06) — e, em cada transição, diz explicitamente **o que se ganha e o que se paga**. A seção "Onde essa abordagem se encaixa frente à indicadora" (a05) é o melhor parágrafo do módulo nesse aspecto: fecha o par de métodos como complementares, não concorrentes, e dá o critério prático de escolha.
- **A reutilização dos valores do Módulo 20 no exemplo da a05** ($\lambda_1=0{,}8125$, $\mu=0{,}330$, $\sigma^2_{OK}=0{,}833$) é uma decisão didática de primeira qualidade: o leitor reconhece o sistema já resolvido e a atenção fica toda no que é novo — o que se faz com o resultado depois de obtê-lo. A própria aula nomeia esse ponto na leitura dos resultados.
- **Os dois exemplos aritméticos do módulo agora fecham número por número**, e o da a04 explicita a comparação com o exemplo de krigagem ordinária do M20. São base segura para questões de aplicação.
- **A a01 resiste à tentação de virar um capítulo de banco de dados.** Ela lista as checagens de validação, mostra três delas num furo concreto e para — mantendo o foco em por que isso é pré-condição da geoestatística, não em como se administra um banco.
- **A a06 é honesta sobre o limite do quantitativo.** Dizer que dois geólogos podem, com razão, traçar contatos diferentes entre os mesmos furos é o tipo de afirmação que material técnico costuma evitar, e é justamente o que prepara o leitor para a decisão domínio rígido × domínio suave no fim da aula.

---

## Sugestões (🔵, não são defeitos)

- **`DID-M21-S1` — Apoio visual.** O módulo não tem nenhuma figura. Três pediriam por si: o par Voronoi/Delaunay com a dualidade explícita (a06), a família de variogramas indicadores em vários limiares mostrando o alcance encurtando com o teor (a03), e o fluxo seção → *string* → triangulação → *end cap* → sólido (a06). Fora do escopo desta skill; registrado para o orquestrador.
- **`DID-M21-S2` — Sessão de `tutor-de-voz` para o par a03/a04.** A discriminação "variância negativa × fora de $[0,1]$" é classificatória e socrática por natureza — o formato falado é onde ela rende mais, porque o erro do aluno aparece na hora.
- **`DID-M21-S3` — Ponte explícita para o Módulo 42.** A auditoria registrou quatro decisões deste módulo que o M42 (exploração mineral e avaliação de recursos) vai reencontrar. Quando o M42 for escrito, esta revisão recomenda que ele **cite as aulas 03–05 deste módulo nominalmente** em vez de reexpor o assunto: o risco de divergência silenciosa é alto justamente nos quatro pontos que a auditoria isolou.

---

## Formato do questionário — recomendação confirmada

**Questionário único cumulativo, sem parciais.** A recomendação da auditoria foi reavaliada após a divisão e **não muda**. A decisão final, com as três razões e as restrições herdadas, está registrada no hub do módulo, em "Formato do questionário — decisão final".

Em resumo: a divisão levou o módulo a 6 aulas, ainda dentro do limiar de ~5–6 do plugin, e não criou um corte conceitual novo — repartiu um que já existia dentro de uma aula. Usar essa costura como fronteira de parcial confundiria uma medida de carga cognitiva com uma fronteira de avaliação. As Aulas 03 e 04 são um par indivisível para avaliar, e as questões de maior valor do módulo são as de integração entre as duas cadeias, que uma divisão em parciais cortaria.
