# Revisão didática — Módulo 13: Tratamentos da oficina de lapidação e a regra de divulgação

**Revisado em:** 2026-09-07 · **Modo:** `review-and-fix`
**Material:** `curso-lapidacao/13-tratamentos-da-oficina/` — 5 aulas
**Rodou depois da:** auditoria científica `audit-and-fix` (11 achados, 11 corrigidos, 0 em aberto)
**Veredito:** ✅ **Bem ensinado com ressalvas** — todas as ressalvas 🟠/🟡 corrigidas. 1 sugestão 🔵 em aberto, não bloqueante.

## Resumo

🔴 0 bloqueiam · 🟠 3 prejudicam · 🟡 2 atrito · 🔵 1 sugestão
**Corrigidos:** 5 de 6. Em aberto: 1 🔵 (sugestão, não é defeito).

**Achado estrutural da rodada:** **cinco dos seis achados foram introduzidos pelas próprias correções da auditoria**, não preexistiam nas aulas. É a mesma assinatura registrada no módulo 12 — corrigir o fato mexe na explicação, e a explicação mexida precisa de uma segunda passada. Só o DID-13-02 (ordem interna da aula 04) é defeito original do texto escrito pelo redator.

**Carga por aula:**

| Aula | Conceitos novos | Pré-req reativados | Exemplos | palavras_corpo | Avaliação de carga |
|---|---|---|---|---|---|
| a01 | 4 (pedra montada, dublê, triplete, cimento óptico) | 2 (m05a05, m06a03) | 1 trabalhado, 3 opções | 1591 | adequada |
| a02 | 3 construções + 3 indícios, sob **um** esquema unificador | 2 (a01, gemologia m01) | 1 trabalhado, 3 casos | 1625 | adequada — ver nota |
| a03 | 4 (porosidade, impregnação, estabilização, hidrofania) | 2 (m05a02, m06a01) | 1 trabalhado, 2 lotes | 1513 | adequada |
| a04 | 4 (tingimento, cera de dop, choque térmico, dopagem a frio) | 2 (a03, gemologia m01) | 1 trabalhado, 3 pedras | 1620 | adequada |
| a05 | 4 (oleamento/enceramento, código W, permanente × não permanente, gatilhos da FTC) | 2 (a04, m11a06) | 1 trabalhado, 3 cabochões | 1614 | densa — mitigada, ver DID-13-01 |

> **Nota sobre a aula 02.** À primeira vista ela parece sobrecarregada (três construções mais três métodos de identificação). Não está: as três são **instâncias paralelas de um único esquema** — "a camada visível não é a que decide a propriedade valorizada" —, e a aula torna esse esquema explícito na seção "O que cada construção esconde". Instância paralela sob esquema comum não custa o mesmo que conceito independente. Nenhum achado aberto aqui; registrado para que uma revisão futura não a "conserte" dividindo-a.

## Achados

### 🟠 1. Duas listas de três, adjacentes e de mesma forma — interferência

**claim/origem:** introduzido pela correção `AUD-13-05` · **Tipo:** sobrecarga por interferência
**Onde:** aula 05 · junção entre "O que a norma efetivamente diz" e "Formulando a regra da oficina"

**Problema.** A auditoria acrescentou, corretamente, os **três gatilhos** do § 23.24 da FTC. Só que a aula já terminava com uma regra do curso em **três pontos**. O resultado eram dois conjuntos de três itens, um logo após o outro, ambos sobre divulgação, ambos apresentados como listas — a configuração clássica de interferência proativa. O leitor sai com seis itens embaralhados e nenhuma das duas listas íntegra; e o risco é assimétrico, porque confundir as duas é exatamente o erro que a correção factual existia para evitar. Rotular em prosa ("síntese didática, não o texto da norma") avisa, mas não resolve: continua exigindo que o leitor segure as duas listas na memória de trabalho para compará-las.

**Correção aplicada.** Tabela de contraste de duas colunas inserida na junção, como organizador prévio — norma à esquerda, síntese do curso à direita, com a linha de fecho marcando "basta um" de um lado e "o ponto 3 não é gatilho" do outro. A comparação passou a ser visual em vez de mnemônica. Os itens numerados que seguem foram enxugados: perderam o enunciado em negrito (agora na tabela) e ficaram só com a elaboração de bancada. No Recap, os dois bullets que repetiam as duas listas viraram um bullet dos gatilhos mais um bullet explícito de "não confundir". **Escopo:** correção local — não foi preciso dividir a aula.

---

### 🟠 2. Ordem interna quebrada: a aula volta ao tingimento depois de já ter mudado para o calor

**Tipo:** ordem interna invertida · **Onde:** aula 04 · seção "Por que o tingimento de ágata é tratado com mais tolerância do mercado"
**Origem:** defeito original do texto (único achado não introduzido pela auditoria)

**Problema.** A aula 04 tem duas metades anunciadas no próprio título — tingimento **e** calor de processo. O texto percorria: tingimento → cera de dop → choque térmico → materiais que proíbem calor → **e então voltava ao tingimento** para discutir a tolerância do mercado à ágata, imediatamente antes do exemplo trabalhado. Para quem lê pela primeira vez, isso desfaz o fechamento do bloco de calor e reabre um assunto já encerrado quatro seções antes; e o exemplo trabalhado, que é sobre dopagem, passava a vir depois de um parágrafo sobre ética de nomenclatura comercial. A seção também carrega a controvérsia LC-08 da aula, que ficava enterrada no lugar errado.

**Correção aplicada.** A seção foi movida para o fim do bloco de tingimento, logo após a howlita, e renomeada para "Por que o mercado tolera mais a ágata tingida". Acrescentada uma frase de dobradiça entre as duas metades ("Fecha aqui a primeira metade da aula. A segunda troca de assunto: sai a cor, entra o calor."), que sinaliza a transição que o título promete. A aula agora lê: analogia → tingimento (ágata · permanência · howlita · tolerância de mercado) → **dobradiça** → calor (cera · choque · materiais que proíbem) → exemplo de dopagem. **Escopo:** correção local, sem conteúdo novo.

---

### 🟠 3. Correção da auditoria lida como desmentido do vocabulário da própria aula

**claim/origem:** introduzido pela correção `AUD-13-11` · **Tipo:** contradição aparente
**Onde:** aula 03 · "Nem toda impregnação é igual", contra a tabela "Vocabulário desta aula"

**Problema.** O vocabulário no topo da aula estabelece uma distinção limpa e útil: **impregnação** é o processo, **estabilização** é o resultado. A correção da auditoria, mais abaixo, passou a dizer — corretamente — que "estabilizado" é termo de comércio e não um grau normativo ao lado de "impregnado". Lidas em sequência, as duas passagens soam como se a segunda derrubasse a primeira, e o leitor fica sem saber se deve confiar no vocabulário que acabou de decorar. As duas afirmações são compatíveis (uma é sobre papel semântico, outra sobre escala de intensidade), mas a aula não dizia isso — deixava a reconciliação por conta do leitor, no ponto exato em que ele está mais sobrecarregado.

**Correção aplicada.** Duas orações de reconciliação inseridas: a distinção processo × resultado adotada no vocabulário continua valendo; o que não existe é uma **escala de intensidade** por trás dos dois termos. **Escopo:** correção local, sem conteúdo factual novo.

---

### 🟡 4. Referência antecipada à howlita antes de a howlita ser apresentada

**claim/origem:** introduzido pela correção `AUD-13-06` · **Tipo:** ordem interna · **Onde:** aula 04, parágrafo da permanência

**Problema.** O parágrafo novo sobre a permanência do ônix fechava contrastando com "corantes aplicados a material mais mole e mais poroso, **como a howlita**" — mas a howlita só é apresentada no parágrafo seguinte. Contraste com um termo que o leitor ainda não conhece não é contraste; é ruído.
**Correção aplicada.** A cláusula foi retirada do parágrafo da permanência e realocada para o **fim** do parágrafo da howlita, onde os dois casos já estão na mesa e o contraste funciona. **Escopo:** local.

---

### 🟡 5. Termo introduzido sem glosa (LC-01)

**claim/origem:** introduzido pela correção `AUD-13-10` · **Tipo:** termo indefinido · **Onde:** aula 01, "A construção do dublê de opala" e Recap

**Problema.** A correção nomeou o ironstone como "a rocha ferruginosa hospedeira da **opala boulder**". Ironstone ficou glosado; "opala boulder" entrou como termo novo, não glosado, e a glosa acabou quase circular (define-se o ironstone pela opala boulder, que por sua vez só se entende pelo ironstone). LC-01 exige definição na primeira aparição.
**Correção aplicada.** Reescrito sem introduzir o termo: "ironstone — a rocha ferruginosa escura dentro da qual a opala australiana costuma se formar em veios". No Recap, onde não há espaço para glosa, ficou só "ironstone", já definido no corpo. **Escopo:** local.

---

### 🔵 6. A analogia do compensado não diz onde quebra — **em aberto, não bloqueante**

**Tipo:** analogia sem limite declarado · **Onde:** aula 01, "Uma analogia para começar"

**Observação.** A analogia do marceneiro (lâmina nobre colada sobre base comum = compensado) é boa e faz o trabalho: transmite a lógica de aproveitar material fino demais para se sustentar sozinho. Ela não declara, porém, o ponto em que deixa de valer — no compensado, a base é **só** suporte mecânico; no dublê de opala, a base escura tem também função **óptica** (realce do jogo de cores por contraste), que é justamente o ponto que a aula precisa que o aluno não perca, e que aparece no "Erros comuns" como equívoco previsto.

**Por que fica em aberto.** Não é defeito: a aula explica a função óptica da base duas seções adiante, com ênfase, e a repete no Recap e nos "Erros comuns" — a cobertura existe. A melhoria seria fechar a analogia com uma frase do tipo "e é aqui que a analogia quebra: no compensado a base só sustenta; no dublê, ela também trabalha na óptica". Custaria ~25 palavras numa aula em 1591 de teto ~1600, e a decisão de onde tirar o espaço é editorial. **Escopo:** local, mas exige decidir o corte compensatório — fica registrado para a próxima abertura da aula 01, não bloqueia o módulo.

---

## Cobertura de objetivos

| Objetivo | Ensinado em | Analogia | Exemplo trabalhado | Recap | Avaliado em |
|---|---|---|---|---|---|
| `lapidacao-m13-oa01` — construção de dublês e tripletes; por que a opala é o caso central | a01 · "Por que a opala é o caso central", "A construção do dublê", "A construção do triplete" | sim (compensado) | sim, 3 opções (fatia sozinha · dublê · triplete) | sim | pendente |
| `lapidacao-m13-oa02` — distinguir granada-topo, esmeralda montada e mabé pelo que cada uma resolve e oculta | a02 · três seções de construção + "O que cada construção esconde" | sim (carroceria/chassi) | sim, 3 anéis | sim | pendente |
| `lapidacao-m13-oa03` — o que estabilização e impregnação fazem com material poroso; consequências para corte e divulgação | a03 · "Por que alguns materiais precisam disso", "Consequências para o corte", "A divulgação como parte do processo" | sim (restaurador de móveis) | sim, 2 lotes de turquesa | sim | pendente |
| `lapidacao-m13-oa04` — relacionar tingimento e calor de processo às operações da oficina; identificar materiais que proíbem calor | a04 · bloco de tingimento + bloco de calor + "Os materiais que proíbem calor de dop" | sim (tecido/corante) | sim, 3 pedras para dopagem | sim | pendente |
| `lapidacao-m13-oa05` — formular a regra de divulgação e delimitar a fronteira com o laboratório | a05 · "O que a norma efetivamente diz", "Formulando a regra da oficina", "A fronteira com o curso de Gemologia" | sim (tábua com óleo) | sim, 3 cabochões mapeados a gatilhos | sim | pendente |

**Nenhum objetivo órfão; nenhuma seção órfã.** Cada aula cobre exatamente um objetivo, conforme a convenção do curso (um objetivo por aula). O verbo de todos os cinco é de conhecimento observável — descrever, distinguir, explicar, relacionar, formular —, nenhum é "entender" ou "saber fazer", e **nenhuma aula afirma competência de bancada**.

## Verificação das regras duras do curso (pós-revisão)

| Regra | Resultado |
|---|---|
| Nível teórico, sem competência de bancada | ✅ 0 ocorrências. As seções "O que não concluir" de todas as 5 aulas remetem explicitamente procedimento de bancada para fora do escopo. |
| Pré-requisito de gemologia só por nome, nunca wikilink | ✅ 0 wikilinks para fora do curso; 3 menções nominais (a02, a04, a05). |
| LC-01 — nenhum termo sem definição na primeira aparição | ✅ após DID-13-05. |
| LC-03 — abertura padronizada (vocabulário 5–10 termos + "Antes de começar") | ✅ 5 termos por aula, 2 pré-requisitos declarados por aula, todos usados. |
| LC-04 — analogia antes do termo | ✅ 5 de 5, todas na primeira seção do conteúdo. |
| LC-07 — "Erros comuns", "O que não concluir", "Recap relâmpago" | ✅ 5 de 5. |
| LC-08 — controvérsia em uma frase, como pergunta aberta | ✅ a01 (valor maciça × montada), a03 (limiar de saturação), a04 (tolerância de mercado à ágata). a02 e a05 herdam as das anteriores. |
| LC-02 — teto de ~1.600 palavras de corpo | ✅ 1513–1625, medidas pela régua de `_contexto.md`. |

## O que está bem feito

Vale registrar, porque precisa sobreviver às próximas revisões:

- **O esquema unificador da aula 02.** "A camada visível não é a que decide a propriedade mais valorizada" transforma três construções soltas num único padrão com três instâncias. É o que impede a aula de virar catálogo, e é também o que a torna avaliável por transferência em vez de memorização.
- **A progressão de porosidade entre as aulas 03 e 04.** A aula 04 abre reativando explicitamente que o mesmo mecanismo físico que permite a estabilização por resina permite o tingimento por corante. É reativação de pré-requisito bem feita: uma frase, no lugar certo, sem reensinar.
- **Os exemplos trabalhados em três casos paralelos**, repetidos nas cinco aulas (três opções de corte, três anéis, dois lotes, três pedras, três cabochões). O formato virou uma convenção reconhecível do módulo e sustenta comparação, que é exatamente o que os objetivos "distinguir" e "relacionar" cobram.
- **O enquadramento ético sem moralismo.** As cinco aulas repetem, sem exceção, que a construção ou o tratamento não é condenável em si e que a fraude está em não declarar. Isso é o que permite ao módulo ensinar identificação sem virar caça às falsificações — e é a base didática do objetivo oa05.
- **A aula 05 como fecho real do módulo**, e não como sexta aula solta: ela recolhe nominalmente cada operação das quatro anteriores e as amarra numa regra única.

## Nota para quem gerar o questionário

A revisão didática **não altera** questionário nem baralho — este módulo ainda não tem nenhum dos dois. Além das 10 travas factuais listadas na auditoria, dois pontos de formulação nascem desta revisão:

1. **Se uma questão cobrar "os três gatilhos", a resposta é a da FTC** (não permanente · cuidado especial · efeito sobre o valor). Se cobrar "os três pontos da regra do curso", é a outra lista. Uma questão que misture as duas está reintroduzindo exatamente a interferência que DID-13-01 acabou de mitigar — e a tabela de contraste da aula 05 é o gabarito visual dessa distinção.
2. **A aula 02 deve ser avaliada por transferência, não por catálogo.** O objetivo oa02 é distinguir pelo que cada construção *resolve* e *oculta*; uma questão que só peça "qual dessas é feita de granada" mede memorização e desperdiça o esquema unificador que é o valor real da aula.
