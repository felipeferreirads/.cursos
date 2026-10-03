# Auditoria científica — Módulo 04: Laps, abrasivos, polidores e o sistema de dop

**Data:** 2026-09-02
**Modo:** `audit-and-fix` · **Profundidade:** `full` + consistência cross-course interna (módulos 01–03)
**Material auditado:** as 6 aulas do módulo 04, em conjunto
**Veredito:** ✅ **Aprovado com correções aplicadas** — nenhum achado 🔴 ou 🟠 em aberto. O gate de questionário/flashcards está **liberado**.

## Resumo

| Severidade | Achados | Corrigidos | Em aberto |
|---|---|---|---|
| 🔴 Erro | 2 | 2 | 0 |
| 🟠 Impreciso | 6 | 6 | 0 |
| 🟡 Desatualizado | 0 | — | 0 |
| 🔵 Sem fonte | 3 | 3 (rebaixados) | 0 |
| ⚪ Controverso | 0 | — | 0 |
| **Total** | **11** | **11** | **0** |

Distribuição por aula: a01 — 3 · a02 — 3 · a03 — 0 · a04 — 1 · a05 — 3 · a06 — 1.

A aula 03 passou limpa. As duas cadeias mais caras do módulo — a régua de durezas herdada do módulo 02 e a relação lap→faceta — foram verificadas inteiras.

---

## 🔴 Achados de erro

### 🔴 1. Óxido de crômio declarado "o único dos quatro acima do quartzo" — contradiz a própria aula

**claim_id:** `POL-CRO-JAD-001`
**Tipo:** erro factual + inconsistência interna
**Onde:** aula 05 · "Óxido de crômio (Cr₂O₃)", "Erros comuns", "Recap relâmpago", "Antes de começar"
**Está escrito:** "Dureza da ordem de **8 a 8,5 na escala de Mohs** — o único dos quatro que fica **acima do quartzo**, ao contrário de cério, estanho e alumina calcinada em relação às gemas moles"
**Problema:** falso, e falso contra a própria aula. Os quatro óxidos que a aula 05 apresenta são cério (~6), estanho (~6–7), crômio (~8–8,5) e **alumina (~9)**. A alumina, que a mesma aula descreve três parágrafos antes como "dureza da ordem de 9 na escala de Mohs, quase a do coríndon", está tão acima do quartzo (7) quanto o crômio — mais, inclusive. A afirmação transporta para um conjunto de **quatro** óxidos um enunciado que só valia para o recorte de **três** do módulo 02 (cério, estanho, crômio), onde o crômio era de fato a exceção. Além de ser falsa, a frase é autocontraditória e o trecho final ("ao contrário de cério, estanho e alumina calcinada em relação às gemas moles") não fecha sintaticamente nem semanticamente.
**Correção aplicada:** o crômio passou a ser apresentado como **um dos dois** óxidos acima do quartzo, junto com a alumina, preservando o ponto pedagógico real — é ele que desmente a regra do "polidor sempre mais mole que a gema", regra que vale para cério e estanho. Propagado para "Erros comuns", "Recap relâmpago" e o bloco "Antes de começar".
**Fonte:** dados de dureza de Cr₂O₃ (eskolaita) ~8–8,5 Mohs; Al₂O₃ ~9 Mohs — consistentes com o valor já fixado em `ABR-POL-CROM-001` (módulo 02, aula 01) e com `POL-ALU-COR-001` (a própria aula 05). · **Nível:** literatura de materiais + consistência interna do curso
**Confiança:** confirmado
**Também aparece em:** nenhum outro arquivo do curso (o módulo 02 trata só do recorte de três e está correto).

### 🔴 2. Mecanismo da concavidade do lap invertido

**claim_id:** `LAP-CONCAVO-CENTRO-001`
**Tipo:** erro factual (causa-efeito invertida) + certeza indevida
**Onde:** aula 02 · "O que um lap fora de plano faz com a pedra"
**Está escrito:** "**Lap côncavo** (afundado no meio, **comum porque o centro gira mais devagar e desgasta diferente**)"
**Problema:** duplo. **(a)** A cadeia causal está invertida. A periferia de um disco em rotação percorre mais distância por volta que o centro; onde há mais caminho percorrido sob a mesma carga, há mais remoção. A velocidade diferencial, isolada, faz a **periferia** desgastar mais rápido — o que empurra a placa para **convexa** (centro alto), não para côncava. Oferecer "o centro gira mais devagar" como a razão de o centro afundar é uma contradição no próprio enunciado. **(b)** "Comum" não se sustenta: a literatura de *lapping* de precisão trata côncavo e convexo como os **dois** modos possíveis, sem preponderância intrínseca — qual aparece depende de onde o trabalho se concentra ao longo do raio e de como a pressão se distribui, que é exatamente o que as máquinas de lapping controlam com anéis de condicionamento para manter a placa plana.
**Correção aplicada:** removida a atribuição causal e a alegação de frequência. O parêntese passou a dizer que qual dos dois modos aparece depende de onde o trabalho se concentra no raio e de como a pressão se distribui. O efeito na pedra — lap côncavo → faceta convexa — foi **mantido**, porque está confirmado independentemente.
**Fonte:** Kemet, controle de planicidade de placa de lapping — "a lapping plate will usually wear convex or concave"; "a convex plate produces a concave component and vice versa"; a periferia percorre mais distância e a taxa de remoção é maior na borda. Consultado em 2026-09-02. · **Nível:** literatura técnica de processo
**Confiança:** confirmado
**Também aparece em:** o efeito lap côncavo → faceta convexa reaparece no "Exemplo trabalhado" e no "Recap relâmpago" da mesma aula — **não** foi alterado, porque é a parte correta (`LAP-PLAN-NEG-001`, verificado e mantido).

---

## 🟠 Achados de imprecisão

### 🟠 3. Faixa de dureza do óxido de cério fora da régua fixada no módulo 02

**claim_id:** `POL-CER-SIL-001`
**Tipo:** inconsistência entre módulos + dado numérico
**Onde:** aula 05 · "Óxido de cério (CeO₂)", "Exemplo trabalhado", "Erros comuns", "Recap relâmpago"
**Está escrito:** "Dureza da ordem de **5 a 6 na escala de Mohs**"
**Problema:** o módulo 02 **fixou** o cério em "da ordem de 6" (aula 01, `ABR-POL-MOLE-001`; aula 04, `POL-CER-DUR-001`), e esse valor foi resultado da correção 🔴 `ABR-POL-CROM-001` daquele módulo. A aula 05 abre o intervalo para baixo, criando duas versões do mesmo dado no mesmo curso — o tipo de divergência que a auditoria transversal existe para caçar, aqui pega antes de se propagar. A extremidade 5 também não é sustentada: as fontes reportam 6, algumas até 6–7; nenhuma sustenta 5. A própria aula 05 já dizia "~6 Mohs" no bloco "Antes de começar", contradizendo o corpo.
**Correção aplicada:** alinhado para **~6** nas quatro ocorrências do corpo, resolvendo simultaneamente a divergência com o módulo 02 e a divergência interna da própria aula.
**Fonte:** literatura de materiais sobre pós polidores de cério; módulo 02, aulas 01 e 04 deste curso. · **Nível:** literatura de materiais + norma interna do curso
**Confiança:** confirmado
**Também aparece em:** módulo 02, aula 01 e aula 04 — **corretos, não alterados**. Flashcard `lapidacao-m02-fb008` (crômio) verificado: correto, não tocado.

### 🟠 4. Faixa de dureza da família dos óxidos exclui a alumina que a própria aula inclui

**claim_id:** `ABR-FAM-OXID-001`
**Tipo:** inconsistência interna
**Onde:** aula 04 · "Família 3 — Óxidos", "Recap relâmpago", "Fontes consultadas"
**Está escrito:** "São os mais moles do grupo — de cerca de **6 a 8,5 em Mohs** (a alumina, a mais dura, **~9** / Knoop ~2.000; o óxido de cério, o mais mole, ~6)"
**Problema:** o teto declarado da família (8,5) exclui o membro que o parêntese imediatamente a seguir dá como o mais duro dela (alumina, ~9). O intervalo e o exemplo se contradizem na mesma frase. Com cério ~6, estanho ~6–7, crômio ~8–8,5 e alumina ~9, o intervalo correto da família é **~6 a 9**.
**Correção aplicada:** "6 a 8,5" → "**6 a 9**" no corpo, no recap, na alegação auditável e na linha de fontes. Correção **word-neutral** — a aula permanece em 1581 palavras.
**Fonte:** as mesmas durezas já usadas pela aula; IGS / geology.com. · **Nível:** literatura de materiais
**Confiança:** confirmado
**Também aparece em:** aula 05, que lista os mesmos quatro óxidos com as mesmas durezas — agora consistente.

### 🟠 5. Lap de ferro fundido atribuído a etapas finas

**claim_id:** `LAP-ACO-DESB-001`
**Tipo:** erro factual (escopo de aplicação) — origem em fonte secundária
**Onde:** aula 01 · "Percorrendo os materiais"
**Está escrito:** "O ferro fundido, mais poroso que o aço, segura o grão um pouco melhor e **chega a servir para etapas mais finas**."
**Problema:** a literatura de lapidação situa o lap de ferro fundido firmemente nos estágios de **remoção** — desbaste e lixamento médio, carregado com diamante grosso a médio para redução rápida de volume —, e o pré-polimento migra para cobre, estanho ou cerâmica. A atribuição a etapas finas vinha de Hannam, que o `_fontes/README.md` classifica como fonte **secundária**, admissível para nomenclatura e nunca como fonte de alocação técnica contra a literatura forte. O redator já havia sinalizado a divergência.
**Correção aplicada:** "chega a servir para etapas mais finas" → "mas a literatura o mantém no desbaste e no lixamento médio, não no pré-polimento". A premissa correta (mais poroso, retém melhor que o aço) foi **preservada** — ela é verdadeira e é o que justifica o ferro fundido existir ao lado do aço.
**Fonte:** literatura de lapidação sobre laps de ferro fundido (estágios grosseiro e médio; carga com diamante 60–325 mesh, progredindo a 600/1200 antes de passar a cobre, estanho ou cerâmica). Consultado em 2026-09-02. · **Nível:** literatura de lapidação
**Confiança:** confirmado
**Também aparece em:** "Recap relâmpago" da mesma aula — já dizia "desbaste com grão grosso a médio", **correto, não alterado**.

### 🟠 6. Composição do *type metal* omite o antimônio, que é justamente o endurecedor

**claim_id:** `LAP-EST-POL-001`
**Tipo:** omissão que gera erro + dado numérico
**Onde:** aula 01 · "Vocabulário desta aula" e "Percorrendo os materiais"
**Está escrito:** "**chumbo-estanho** (*type metal*) | liga mole de chumbo com estanho" e "O estanho (*tin*) e a liga de chumbo com estanho (*type metal*) são **muito moles** — dureza da ordem de 1,5 em Mohs."
**Problema:** *type metal* é liga ternária de **chumbo, antimônio e estanho** — tipicamente ~80% Pb, ~15% Sb, ~5% Sn —, e o antimônio está lá **precisamente para endurecer**: chumbo puro é mole demais e encolhe ao solidificar, dando tipos sem definição. Omitir o antimônio não é um detalhe de nomenclatura: apaga o componente que responde pela propriedade em discussão. E atribuir 1,5 Mohs ao conjunto estende ao *type metal* o valor do estanho e do chumbo **puros**, que a liga antimoniada supera.
**Correção aplicada:** antimônio incluído na definição do vocabulário e no corpo; o valor 1,5 Mohs foi atribuído explicitamente ao **estanho e ao chumbo**, com a ressalva de que o antimônio endurece um pouco a liga sem tirá-la da classe dos laps moles — que é o ponto que a aula precisa sustentar.
**Fonte:** Britannica, *type metal* (composição ~80/15/5 Pb-Sb-Sn; antimônio e estanho adicionados para dureza e estabilidade dimensional); dureza Mohs de estanho e chumbo ~1,5. · **Nível:** base de referência + dados de dureza de metais
**Confiança:** confirmado
**Também aparece em:** "Recap relâmpago" da mesma aula, que só diz "Estanho e chumbo-estanho: muito moles" — **verdadeiro como escrito, não alterado**.

### 🟠 7. Óxido de crômio apresentado como o polidor do cromo-diopsídio

**claim_id:** `POL-CRO-DIOP-002` *(novo — o dado do cromo-diopsídio não existia como alegação separada)*
**Tipo:** certeza indevida
**Onde:** aula 05 · "Óxido de crômio (Cr₂O₃)", "A tabela mental", "Recap relâmpago"
**Está escrito:** "é o polidor do **jade** — tanto **nefrita** quanto **jadeíta** —, do **cromo-diopsídio** e de alguns materiais duros que respondem mal aos outros óxidos" · tabela: "jade — nefrita e jadeíta, **cromo-diopsídio** | **crômio**"
**Problema:** para o cromo-diopsídio, a referência gemológica dá **alumina ou óxido de cério** como os polidores da maioria dos laps, com o óxido de crômio aparecendo em uma configuração específica (Ultralap). Listá-lo ao lado do jade como cliente definidor do crômio inverte a ordem de preferência da fonte e ensina uma associação que a prática não sustenta. O jade, esse sim, é o caso canônico do crômio e permanece.
**Correção aplicada:** o cromo-diopsídio saiu da posição de cliente definidor e passou a ser mencionado como caso em que o crômio "aparece como opção, com alumina e cério à frente"; removido da linha da tabela mental e do recap.
**Fonte:** International Gem Society, *Chrome Diopside / Faceting Information*. Consultado em 2026-09-02. · **Nível:** base de referência gemológica
**Confiança:** confirmado
**Também aparece em:** `POL-MAP-MAT-001` (mapa material→óxido) mapeia "jade → crômio" — **correto, não alterado**.

### 🟠 8. Faixa de amolecimento da cera de dop estreita demais e atribuída sem verificação

**claim_id:** `DOP-CERA-TERM-001`
**Tipo:** dado numérico + omissão que gera erro
**Onde:** aula 06 · "Cera de dop", "O que não concluir", "Recap relâmpago"
**Está escrito:** "A faixa de amolecimento fica por volta de **60–80 °C** (Sinkankas)."
**Problema:** dois problemas. **(a)** A atribuição nominal a Sinkankas não foi verificada contra o texto — o próprio redator a sinalizou como não conferida, e uma citação pontual de número a uma fonte primária é exatamente o tipo de alegação que não pode ficar de pé sem verificação. **(b)** A faixa exclui a metade baixa do espectro real. Cimentos de dopping à base de goma-laca, breu e cera de abelha são moldáveis a **45–65 °C**, com formulações de ponto mais alto em 65–75 °C; ceras de facetamento comerciais ficam em torno de 74–77 °C nas formulações comuns, com as vermelhas mais altas e as **verdes deliberadamente mais baixas — e são justamente estas as indicadas para gema termossensível**. Um piso de 60 °C apaga do mapa a faixa de cera que mais importa para o eixo de risco térmico que a aula está ensinando.
**Correção aplicada:** faixa ampliada para **45–80 °C** com a dependência de formulação explicitada; a atribuição pontual a Sinkankas foi removida do corpo e substituída, na alegação auditável, pela base de verificação real. Propagado para "O que não concluir" e "Recap relâmpago". Correção **word-neutral no saldo** — a aula permanece em 1598 palavras.
**Fonte:** dados de formulação de *dopping cement* (goma-laca/breu/cera de abelha; moldável a 45–65 °C, formulações de ponto alto 65–75 °C); dados de produto de cera de facetamento (cera preta ~165 °F ≈ 74 °C; fórmula Princeton ~170 °F ≈ 77 °C; vermelhas de ponto alto, verdes de ponto baixo para pedra sensível a calor — IGS, *Choosing the Best Faceting Wax*). Consultado em 2026-09-02. · **Nível:** base de referência + dados de produto
**Confiança:** confirmado (faixa) · a composição goma-laca + cera segue corroborada
**Também aparece em:** nenhum outro arquivo.

---

## 🔵 Achados sem fonte — rebaixados para qualitativo

Nos três casos abaixo a política é a mesma: **não inventar a correção**. A afirmação não era central à aula, e foi reescrita sem o número não sustentado, preservando o conteúdo conceitual.

### 🔵 9. Tolerância de planicidade de 0,05–0,1 mm

**claim_id:** `LAP-PLAN-TOL-001`
**Tipo:** evidência insuficiente
**Onde:** aula 02 · "O que um lap fora de plano faz com a pedra", "O que não concluir", "Recap relâmpago"
**Está escrito:** "um lap é tratado como fora de serviço quando a face se afasta do plano por mais do que **cerca de 0,05 a 0,1 mm** (poucos milésimos de polegada) de um lado ao outro — ordem de grandeza da literatura de facetamento (Wykoff; United States Faceters Guild)"
**Problema:** o valor não foi localizado em Wykoff, USFG, Sinkankas nem Vargas & Vargas. A única cifra recorrente na literatura — "a few thousandths of an inch" — refere-se ao **material removido por passe de truing**, não ao desvio máximo tolerado antes de o lap sair de serviço; são grandezas diferentes, e a coincidência numérica aproximada torna a confusão fácil de cometer. Além disso, um critério absoluto de planicidade não é como a literatura de facetamento trata o assunto: ela trabalha por **verificação** (régua de precisão sobre a face, procurando folga de luz) e por sintoma na pedra.
**Correção aplicada:** o número saiu. O parágrafo passou a descrever a verificação por régua de precisão e o critério relativo — enquanto o desvio se dilui na tolerância do trabalho o lap serve; quando começa a aparecer na pedra, pede dressing. Propagado para "O que não concluir" e "Recap relâmpago".
**Fonte:** ausência de fonte é o achado. Verificação por régua de precisão: prática corrente de lapidação e lapping. · **Confiança:** não verificado (o número); confirmado (a prática de verificação)

### 🔵 10. Descarte do lap "em torno de metade da espessura original"

**claim_id:** `LAP-VIDA-METAL-001`
**Tipo:** evidência insuficiente
**Onde:** aula 02 · "Vida útil", "O que não concluir", "Recap relâmpago"
**Está escrito:** "na prática, quando resta em torno de **metade da espessura original** ele já não vale a pena"
**Problema:** nenhuma das fontes primárias do curso oferece essa fração nem qualquer outra. O critério real na literatura é funcional, não dimensional.
**Correção aplicada:** a fração saiu; o critério funcional que a própria frase já continha — fino demais, empena sob a fixação, deixa de sustentar a planicidade — ficou como o critério, com a ressalva explícita de que não há fração citável. Propagado para "O que não concluir" e "Recap relâmpago".
**Fonte:** ausência de fonte é o achado. · **Confiança:** não verificado

### 🔵 11. Zinco "menos propenso a carregar demais"

**claim_id:** `LAP-ZN-INTER-001`
**Tipo:** evidência insuficiente
**Onde:** aula 01 · "Percorrendo os materiais", "Recap relâmpago"
**Está escrito:** "com a vantagem de ser **menos propenso a 'carregar demais'**: acumula menos abrasivo velho e detrito, o que dá um comportamento mais previsível ao longo de uma sessão"
**Problema:** a propriedade específica não aparece em Sinkankas, Wykoff, Vargas & Vargas, USFG nem IGS — o artigo de referência do IGS sobre laps registra apenas "Zinc. No longer available." O que as fontes disponíveis sustentam sobre o zinco é outra coisa: que ele é **mais duro que o estanho** e por isso mantém a face plana por mais tempo. A afirmação original tinha, como o redator suspeitou, feição de folclore de fórum.
**Correção aplicada:** substituída pela consequência que a dureza relativa sustenta e que o próprio módulo já ensina — mais duro que o estanho, sustenta a planicidade por mais tempo e sulca menos, à custa de reter um pouco menos de abrasivo. Isso liga o zinco ao mecanismo de sulcamento da aula 02, em vez de a uma propriedade não verificável. A dureza ~2,5 Mohs, essa sim, está confirmada. Propagado para o "Recap relâmpago".
**Fonte:** dureza Mohs do zinco ~2,5 (dados de dureza de metais); consequência deduzida do mecanismo de sulcamento de `LAP-SULC-ANEL-001`. · **Confiança:** não verificado (a alegação original); confirmado (a substituta)

---

## Correção de conformidade

### `claim_id` de 3 segmentos

**Onde:** aula 02 · rodapé YAML
**Problema:** `LAP-SULC-001` tinha **3 segmentos**, violando o formato de 4 segmentos que o `_contexto.md` fixa para este curso desde a primeira aula (`^[A-Z]{2,4}-[A-Z0-9]+-[A-Z0-9]+-[0-9]{3}$`). Era o único do módulo fora do padrão.
**Correção aplicada:** renomeado para **`LAP-SULC-ANEL-001`**. Renomear foi seguro porque nenhum questionário, flashcard ou relatório apontava ainda para o ID antigo — o módulo 04 não tem material derivado. Os 44 demais `claim_id` do módulo foram validados contra a regex: todos conformes.

### Colisão de `claim_id` com o módulo 02

Verificado: os sete IDs de prefixo `POL-` da aula 05 (`POL-CER-SIL-001`, `POL-ALU-COR-001`, `POL-EST-FLD-001`, `POL-CRO-JAD-001`, `POL-MAP-MAT-001`, `POL-CER-DEB-001`, `POL-SEL-EX-001`) e o novo `POL-CRO-DIOP-002` **não colidem** com os do módulo 02 (`POL-CER-QTZ-001`, `POL-CER-DUR-001`, `POL-CROM-JADE-001`, `POL-MICR-HOOK-001`, `POL-BEIL-AMOR-001`, `POL-BEIL-EXIS-001`, `POL-QUIM-HIDR-001`, `POL-DIAM-CORI-001`, `POL-PESO-COMB-001`). Os IDs de prefixo `LAP-` das aulas 01 e 02 também não colidem com os dos módulos 01 e 03. Nenhum ID foi reciclado.

---

## Verificado e correto

O que a auditoria olhou e **passou** — registrado para que uma auditoria futura saiba o que já foi conferido e quando.

**Durezas e escalas (a01, a04, a05) — a régua herdada do módulo 02, verificada inteira:**

| Dado | Na aula | Verificado | Situação |
|---|---|---|---|
| Aço, Mohs | ~4–4,5 | 4–4,5 | ✅ |
| Cobre, Mohs | ~3 | 3 | ✅ |
| Zinco, Mohs | ~2,5 | 2,5 | ✅ |
| Estanho e chumbo, Mohs | ~1,5 | 1,5 | ✅ |
| Diamante, Knoop | ~7.000–8.000 | 7.000–8.000 (fontes até 12.000) | ✅ bate com o módulo 02 |
| Carbeto de silício, Knoop | ~2.500 | ~2.500 (faixa 2.400–3.000) | ✅ |
| Coríndon, Knoop | ~2.000 | 1.900–2.200 | ✅ bate com o módulo 02 (2.000–2.100) |
| Carbeto de silício, Mohs | ~9,5 | 9,5 | ✅ |
| Alumina, Mohs | ~9 | 9 | ✅ |
| Óxido de crômio, Mohs | ~8–8,5 | 8–8,5 (eskolaita) | ✅ bate com `ABR-POL-CROM-001` |
| Óxido de estanho, Mohs | ~6–7 | 6–7 (cassiterita) | ✅ bate com o módulo 02 |
| Jadeíta, Mohs | ~6,5–7 | 6,5–7 | ✅ |
| Linde A | ~0,3 µm, Mohs 9 | 0,3 µm, 99,9% Al₂O₃, Mohs 9 | ✅ |

**Escala de grão (a03) —** `CON-GRAO-NUM-001` **confirmado**, o que era o achado mais provável do módulo por ser síntese sem fonte única. Grão de desbaste 200–300 µm: 60 mesh ≈ 254 µm, coerente com o ~260 µm do exemplo trabalhado. Polimento fino 0,25–1 µm: 100.000 mesh ≈ 0,25 µm, 14.000 ≈ 1 µm — bate exatamente. Partícula sobrevivente de 10–30 µm riscando um estágio sub-mícron: plausível e internamente consistente, já que 10–30 µm corresponde à faixa 600–1200 mesh e o risco resultante é ordens de grandeza mais fundo do que um estágio de 0,25 µm remove. A aula declara os valores como ordem de grandeza, conforme LC-05.

**Mecanismos de polimento (a04, a05) —** as aulas **reativam** os três mecanismos do módulo 02 (microabrasão/Hooke; escoamento e camada de Beilby; ação químico-mecânica/Preston–Grebenshchikov, síntese de Cook) **sem recreditá-los**, atribuindo-os corretamente ao módulo 02 e citando os nomes na mesma forma. Sem achado. A controvérsia do cério (`POL-CER-DEB-001`) está declarada como pergunta aberta, conforme LC-08, sem arbitrar o debate.

**Outras alegações verificadas e mantidas:** `LAP-PLAN-NEG-001` (faceta como negativo do lap — confirmado pela literatura de lapping: "a convex plate produces a concave component and vice versa"); `LAP-MOLE-CUT-001` (lap mole retém mais e corta mais); `LAP-CER-ESTAB-001` (cerâmica, arestas limpas, gemas duras); `LAP-SINTER-VIDA-001` (sinterizado × eletrodepositado); `POL-EST-FLD-001` (estanho para feldspato, opala, turquesa e material poroso — **confirmado**, incluindo a preferência sobre o cério para material poroso, sem que a redação exija ressalva de impregnação); "putty powder" = óxido de estanho (**confirmado**, MFA Cameo); a narrativa histórica do cério deslocando o estanho como polidor de uso geral por custo e desempenho sobre sílica (**confirmado** — cério é notoriamente barato, estanho caro); `POL-ALU-COR-001` e a sobreposição declarada "a alumina pole quartzo de forma aceitável"; toda a aula 06 exceto o achado 8 — `DOP-MEC-ALIN-001`, `DOP-ADE-REV-001`, `DOP-TRANSF-LOG-001` e a lógica coaxial da transferência.

**Fronteiras de escopo verificadas:**

- **a06 × módulo 13** — a aula cita **opala, tanzanita e kunzita** como exemplos e remete "quais e por quê" ao módulo 13 por nome. Está **exatamente no limite** que o `_contexto.md` autoriza ("no máximo opala/tanzanita/kunzita como exemplos"), sem invadir. O bloco "O que não concluir" reforça a fronteira. Sem achado.
- **a06 × módulo 01** — "cinta" é usada como termo estabelecido. **Confirmado**: definida no módulo 01, aula 02 ("a faixa mais larga da pedra, onde o engaste segura"), com seção própria. Sem salto de pré-requisito.
- **Nível teórico** — as seis aulas foram varridas em busca de competência de bancada afirmada. **Nenhuma ocorrência.** Todas as seis trazem, em "O que não concluir", a negativa explícita de procedimento ("a aula não diz como carregar um lap, com que pressão…"), e a aula 02 chega a marcar o ponto no corpo ("*Como* e *com que frequência* fazer isso é competência de bancada e está fora deste curso"). A regra dura do curso está respeitada.

---

## Correções aplicadas

**Aplicadas em:** 2026-09-02

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `POL-CRO-JAD-001` | 🔴 | Corrigido | aula-05 |
| `LAP-CONCAVO-CENTRO-001` | 🔴 | Corrigido | aula-02 |
| `POL-CER-SIL-001` | 🟠 | Corrigido | aula-05 |
| `ABR-FAM-OXID-001` | 🟠 | Corrigido | aula-04 |
| `LAP-ACO-DESB-001` | 🟠 | Corrigido | aula-01 |
| `LAP-EST-POL-001` | 🟠 | Corrigido | aula-01 |
| `POL-CRO-DIOP-002` (novo) | 🟠 | Corrigido | aula-05 |
| `DOP-CERA-TERM-001` | 🟠 | Corrigido | aula-06 |
| `LAP-PLAN-TOL-001` | 🔵 | Corrigido com ressalva (rebaixado a qualitativo) | aula-02 |
| `LAP-VIDA-METAL-001` | 🔵 | Corrigido com ressalva (rebaixado a qualitativo) | aula-02 |
| `LAP-ZN-INTER-001` | 🔵 | Corrigido com ressalva (substituído pela alegação sustentada) | aula-01 |
| `LAP-SULC-001` → `LAP-SULC-ANEL-001` | conformidade | Renomeado | aula-02 |

**Arquivos tocados:** as aulas 01, 02, 04, 05 e 06 (corpo + rodapé YAML + fontes consultadas). A aula 03 **não foi alterada** — passou limpa.

**Propagação:** nenhum material derivado existia para propagar. O módulo 04 ainda **não tem** questionário nem baralho de flashcards — a ordem do pipeline foi respeitada e a auditoria rodou antes deles, que é precisamente o que evita gabarito e verso nascerem errados. Os módulos 01–03 foram varridos em busca dos mesmos fatos: o módulo 02 estava correto em todos os pontos tocados e **não foi alterado**; o flashcard `lapidacao-m02-fb008` (dureza do óxido de crômio) foi verificado e está correto.

**`palavras_corpo` — ressincronizado com a contagem real em todas as aulas alteradas:**

| Aula | Antes | Depois | Δ |
|---|---|---|---|
| a01 | 1578 | **1592** | +14 |
| a02 | 1579 | **1588** | +9 |
| a03 | 1597 | **1597** | 0 (não alterada) |
| a04 | 1581 | **1581** | 0 (correção word-neutral) |
| a05 | 1571 | **1587** | +16 |
| a06 | 1598 | **1598** | 0 (saldo word-neutral) |

Nenhuma aula ultrapassou 1.600. Contagem pela régua LC-02 fixada em 2026-09-02 (de `## Conteúdo` ao fim de `## Recap relâmpago`, `len(texto.split())`).

**Pendências:** nenhuma. Zero achados em aberto.

---

## Observações fora do escopo da auditoria

Não são achados factuais. Ficam registrados para a **revisão didática**, que é quem decide sobre eles:

1. **a04 · exemplo trabalhado antecipa a a05.** O exemplo da safira conclui "Polimento: **alumina** (o óxido mais duro, ~9) ou diamante finíssimo", e o da ametista indica "óxido de cério" — enquanto o bloco "O que não concluir" da mesma aula promete "Não concluir qual **óxido** polir cada gema… é a aula 05". Factualmente as duas indicações estão **corretas** e batem com a a05; a tensão é de escopo declarado, não de verdade. A revisão didática decide se ajusta a promessa ou o exemplo.
2. **a02 · o parêntese corrigido do lap côncavo ficou mais denso** que a redação original. A correção era obrigatória (achado 🔴 2), mas a frase resultante carrega duas condicionantes num aposto. Cabe ao revisor didático avaliar se merece virar oração própria.
3. **a05 · densidade numérica alta** — quatro óxidos, cada um com dureza, mecanismo e clientela, mais as durezas de jade, quartzo e coríndon. Está correto e dentro de LC-05, mas é a aula com mais números por parágrafo do módulo.
