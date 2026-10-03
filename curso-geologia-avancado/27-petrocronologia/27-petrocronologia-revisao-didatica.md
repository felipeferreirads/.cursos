# Revisão didática: Módulo 27 — Introdução à petrocronologia

**Revisado em:** 2026-09-22  ·  **Modo:** review-and-fix
**Material:** `27-petrocronologia/` — 6 aulas na entrada, **7 na saída** (Aula 04 dividida); hub do módulo
**Rodada depois de:** auditoria científica do mesmo dia ([[27-petrocronologia-auditoria|relatório]]), com 14 achados factuais já corrigidos. Nenhuma edição desta revisão introduziu fato novo.
**Veredito:** **Bem ensinado com ressalvas** — nada bloqueia o aprendizado; os dois achados que prejudicavam foram corrigidos (um deles com divisão de aula); as ressalvas são três sugestões azuis não aplicadas.

## Resumo

🔴 0 bloqueiam · 🟠 2 prejudicam · 🟡 6 atrito · 🔵 3 sugestões

**Carga estimada (depois das correções, contagem por script, ~84 palavras/min, convenção do Módulo 26):**

| Aula | Palavras do corpo | Duração | Conceitos novos centrais | Exemplos trabalhados |
|---|---|---|---|---|
| 01 — O que é petrocronologia | 1680 | ~20 min | 3 (idade significante, multidomínio, âncora textura/composição) + distinção de termocronologia | 1 |
| 02 — Sistemas e minerais datáveis | 2451 | ~29 min | 1 princípio (fechamento = mineral + sistema) aplicado a 9 pares, consolidado numa tabela | 1 |
| 03 — Técnicas analíticas | 2456 | ~29 min | 5 técnicas paralelas num único eixo de comparação, agora com tabela | 1 (três problemas) |
| 04 — Petrologia metamórfica (Parte 1) | 1675 | ~20 min | 3 (relações porfiroblasto-matriz, zoneamento de Mn, forma do caminho P-T) | 1 |
| 05 — Petrologia metamórfica (Parte 2) | 1275 | ~15 min | 3 (termômetro de troca, barômetro de volume molar, average P-T/pseudosseções) | 1 (mesma granada) |
| 06 — Minerais acessórios | 2262 | ~27 min | 1 princípio (competição Y/HREE) + 2 termômetros embutidos | 1 |
| 07 — Granada, micas e integração | 2230 | ~27 min | 3 (idade borrada/microamostragem, Lu-Hf × Sm-Nd, integração) | 1 |

---

## Achados

### 🟠 1. O cabeçalho da Aula 01 dispensava a petrologia metamórfica que o módulo usa desde a Aula 02

**ID:** `DID-M27-A01-PREREQ-PETROLOGIA-CONTRADITORIO-001`
**Tipo:** salto de pré-requisito (declarado errado)
**Onde:** Aula 01 · cabeçalho, campo Pré-requisito
**Problema:** a Aula 01 dizia "Não é necessário conhecimento prévio de petrologia metamórfica: essa base vem na Aula 04". Mas a Aula 02 já trabalha com "granulito", "pico metamórfico" e "resfriamento pós-pico" sem definir nenhum deles, e a própria Aula 04 declara como pré-requisito a petrologia metamórfica de graduação ("não ensina o básico do zero"). Quem confiasse no cabeçalho da Aula 01 chegaria à Aula 02 sem o vocabulário. O campo de pré-requisito existe justamente para quem não lê em ordem.
**Correção aplicada:** pré-requisito reescrito — assume petrologia metamórfica de graduação (fácies, pico metamórfico, reações de desidratação), diz que a Aula 02 já a usa, e diz o que as Aulas 04 e 05 acrescentam.
**Escopo:** correção local.

### 🟠 2. Aula 04 sobrecarregada: seis blocos independentes em ~30 min e um só exemplo

**ID:** `DID-M27-A04-SOBRECARGA-SEIS-BLOCOS-002`
**Tipo:** excesso de conceitos novos · duração declarada errada
**Onde:** Aula 04 original (`...-aula-04-petrologia-metamorfica-texturas-pt.md`)
**Problema:** 2517 palavras (~30,0 min, no teto do plugin; o cabeçalho declarava ~28 min e o metadado 2280 palavras) com seis blocos de conceitos que não dependem uns dos outros: relações porfiroblasto-matriz, zoneamento composicional, forma do caminho P-T, termometria de troca, barometria de volume molar, e average P-T/pseudosseções. O critério do plugin é 3-4 ideias independentes por aula de 30 min; o mesmo padrão levou à divisão das aulas dos Módulos 19, 20 e 26 deste curso. A densidade também era irregular: as três primeiras seções são leitura de rocha (qualitativas), as três últimas são termodinâmica aplicada, e o aluno trocava de modo de raciocínio no meio da aula sem pausa nem exemplo intermediário.
**Correção aplicada — divisão em duas aulas**, por corte temático e não por metade de contagem:
- **Aula 04 — Parte 1** (texturas, microdomínios, trajetórias P-T; ~20 min): a rocha lida em termos **relativos** — qual estágio veio antes de qual, e o sentido do caminho. Ficou com a situação e as leituras textural e composicional do exemplo, mais um passo "O que falta" novo que diz o que a leitura ainda não dá (números) e aponta para a Parte 2.
- **Aula 05 — Parte 2** (geotermobarometria convencional, average P-T, pseudosseções; ~15 min, arquivo novo): a mesma rocha com **números** de P e T. Recebeu, com texto integral e inalterado, as duas seções de geotermobarometria, o parágrafo de fechamento, o passo "Leitura P-T" e o passo "O que falta" originais, retomando **a mesma granada** do exemplo — a continuidade do exemplo é o que costura o par.
- Acréscimos de ligação sem fato novo: callout de "Parte 1/Parte 2" nas duas aulas, uma seção curta de abertura na Parte 2, "Situação (retomada)", recap desdobrado. Nenhuma frase de conteúdo foi perdida.
- **Renumeração** (convenção dos Módulos 19 e 20): antigas Aulas 05 e 06 → **06 e 07**; arquivos, IDs (`m27-a05` → `a06`, `m27-a06` → `a07`, `m27-a05` reatribuído à aula nova), títulos e todas as referências internas de número de aula atualizados nas sete aulas, no hub, no `_curso.md`, no manifesto da auditoria e no `course-state.yaml`. Os `claim_id` **não** mudaram (prefixos estáveis, como no Módulo 26); os claims 005-007 da antiga Aula 04 moram agora no arquivo da Aula 05.
- A Parte 1 ficaria sem nenhuma entrada em Fontes; recebeu as três referências primárias que a auditoria já havia conferido para os claims dela (Hollister 1966, Bell 1985, England & Thompson 1984) e os dois manuais já citados no claim 001.
**Escopo:** exigiu dividir a aula.

### 🟡 3. Redação da seção de microdomínios e do recap da Aula 04

**ID:** `DID-M27-A04-REDACAO-MICRODOMINIOS-003`
**Tipo:** atrito (grafia e termo impreciso) — encaminhado pela auditoria como fora do escopo factual
**Onde:** Aula 04 · "Microdomínios composicionais"; recap
**Problema:** "a composição do líquido/fluido em equilíbrico com a granada" — erro de grafia e, num metapelito subsolidus, "líquido" sugere fusão que não há; no recap, "célula a célula" não significa nada no contexto.
**Correção aplicada:** "a composição das fases com que a granada está em equilíbrio"; "zona a zona".
**Escopo:** correção local.

### 🟡 4. A Aula 03 pede uma comparação que ela nunca mostra inteira

**ID:** `DID-M27-A03-COMPARACAO-SEM-CONSOLIDACAO-004`
**Tipo:** consolidação ausente · recap que não recapitula · título que não corresponde
**Onde:** Aula 03 · entre "MEV" e o exemplo; recap; título da seção SIMS
**Problema:** o objetivo é "comparar LA-ICP-MS, SIMS, TIMS e EPMA quanto a resolução espacial, precisão típica e natureza destrutiva". Os números estavam espalhados em cinco seções de prosa, e o recap os repetia um a um em cinco parágrafos longos — o aluno nunca via a comparação num lugar só, e o recap não destilava a regra de decisão que o exemplo ensina. Além disso, depois da correção da auditoria sobre SIMS (vantagem em volume/profundidade, não em resolução lateral), o título "SIMS: mais resolução espacial" passou a contradizer a própria seção.
**Correção aplicada:** tabela "As cinco técnicas lado a lado" (só números já presentes no texto e já auditados); recap reescrito como regra de escolha (problema → técnica), sem repetir números; título da seção SIMS alinhado ("volume amostrado muito menor"). A aula foi de ~28,0 para ~29,2 min — o recap mais curto compensou quase toda a tabela.
**Escopo:** correção local.

### 🟡 5. "Comportamento espelhado ao do zircão"

**ID:** `DID-M27-A06-ESPELHADO-AMBIGUO-005`
**Tipo:** analogia ambígua
**Onde:** Aula 06 (antiga 05) · "Monazita: zoneamento de ítrio"
**Problema:** "espelhado" pode ser lido como **invertido** (imagem no espelho), e o que o texto ensina é o contrário: a monazita responde à granada **do mesmo jeito** que o zircão (empobrecida durante o crescimento da granada, enriquecida depois da quebra). Numa seção que a auditoria acabou de corrigir justamente na sequência de Y, uma palavra que sugere o oposto é o pior atrito possível.
**Correção aplicada:** "responde a ela do mesmo jeito que o zircão (não ao contrário)".
**Escopo:** correção local.

### 🟡 6. Durações e contagens de palavras declaradas não batiam com as aulas

**ID:** `DID-M27-DURACOES-DECLARADAS-006`
**Tipo:** metadado de carga errado
**Onde:** cabeçalho e bloco de metadados das seis aulas originais; `load_note` do `course-state.yaml`
**Problema:** a redação declarou 1780/2150/2050/2280/2020/2150 palavras e 24/28/27/28/29/29 min; a contagem real, pelo método que os próprios metadados declaram, era 1657/2335/2168/2515/2060/2056 — e as durações declaradas não correspondiam a nenhuma taxa única (entre 70 e 82 palavras/min). O caso mais sério era a Aula 04 declarada em ~28 min quando estava no teto de ~30, o que escondeu a sobrecarga do achado 2. A Aula 02 está hoje em ~29,2 min por causa das correções da auditoria e **não** foi dividida (é um arco único: princípio → nove pares → tabela → exemplo); fica registrado que nenhuma passagem futura deve acrescentar texto a ela sem cortar equivalente.
**Correção aplicada:** as sete aulas declaram agora `palavras_corpo` e `duracao_estimada_min` recalculados por script a ~84 palavras/min, e os cabeçalhos e o hub foram alinhados.
**Escopo:** correção local.

### 🟡 7. Referências cruzadas que apontavam para o lugar errado

**ID:** `DID-M27-REFERENCIAS-CRUZADAS-007`
**Tipo:** atrito de navegação · termo usado antes de apresentado
**Onde:** várias aulas
**Problema e correção:**
- Aula 04: "a mesma lógica composicional, aplicada ao ítrio, vai aparecer com protagonismo na Aula 06" apontava para a aula de **granada** (numeração antiga), quando o ítrio é protagonista na aula de **minerais acessórios**. Agora: "nas Aulas 06 e 07".
- Aula 01: "LA-ICP-MS in situ" no exemplo, duas aulas antes de a técnica ser apresentada, sem explicação. Acrescentado aposto de uma linha remetendo à Aula 03.
- Aula 02: notação "Aula 26.04" / "Aula 26.03", que não aparece em nenhum outro lugar do curso. Agora "Módulo 26, Aula 04/03".
- Aula 07: "técnicas já apresentadas [...] nesta Aula 03" → "na Aula 03"; "caminho P-T da Aula 04" → "das Aulas 04 e 05".
**Escopo:** correção local.

### 🟡 8. "Dois pontos P-T" seguidos de três domínios

**ID:** `DID-M27-A05-DOIS-PONTOS-TRES-DOMINIOS-008`
**Tipo:** salto no exemplo trabalhado (leve)
**Onde:** Aula 05 (trecho vindo da antiga Aula 04) · exemplo, "Leitura P-T"
**Problema:** "aplicando [...] à composição do núcleo e à composição da borda [...] obtêm-se dois pontos P-T distintos: o núcleo [...], o intervalo intermediário e a borda [...]" — anuncia dois pontos e descreve três domínios; o aluno fica sem saber se a zona intermediária foi medida.
**Correção aplicada:** "à composição do núcleo, da zona intermediária e da borda [...] obtêm-se pontos P-T distintos".
**Escopo:** correção local.

### 🔵 9. Os termômetros embutidos da Aula 06 não têm exemplo

**ID:** `DID-M27-A06-TERMOMETROS-SEM-EXEMPLO-009`
**Tipo:** sugestão · exemplo insuficiente
**Onde:** Aula 06 · titanita e rutilo
**Observação:** o cabeçalho promete "aplicar o raciocínio do termômetro Zr-em-rutilo e Zr-em-titanita"; a aula explica o raciocínio (o mineral datado é seu próprio termômetro) e a Aula 07 usa uma temperatura de Zr-em-titanita no exemplo integrado, mas nenhum exemplo mostra uma concentração de Zr virando temperatura. **Não aplicada:** exigiria publicar as equações de calibração (Zack et al. 2004 / Watson et al. 2006; Hayden et al. 2008) — conteúdo factual novo, que pertence ao redator e ao auditor. Não bloqueia: o objetivo é conceitual e está coberto.

### 🔵 10. Nenhuma figura num módulo cujo conteúdo é geométrico

**ID:** `DID-M27-DIAGRAMAS-010`
**Tipo:** sugestão · apoio visual
**Observação:** três coisas neste módulo são essencialmente figuras: o caminho P-T horário × anti-horário (Aula 04), a escada de temperaturas de fechamento (Aula 02, hoje uma tabela) e o gráfico idade × temperatura de fechamento da integração (Aula 07). A prosa as descreve com cuidado e o aluno acompanha; um esquema em cada uma economizaria releitura. **Não aplicada:** produzir figuras corretas está fora do escopo de uma revisão de texto.

### 🔵 11. OA-04 ("interpretar bancos de dados") é tratado em nível conceitual

**ID:** `DID-M27-OA04-BANCO-DE-DADOS-CONCEITUAL-011`
**Tipo:** sugestão · objetivo coberto em nível mais baixo que o verbo
**Observação:** a Aula 07 descreve o procedimento de integração em quatro passos e o aplica num exemplo com sete idades — o que cobre o objetivo. Mas "banco de dados" aparece num parágrafo, e o aluno nunca manipula uma tabela de análises (mineral, domínio, composição, idade, incerteza). Uma prática com uma tabela sintética de 20-30 análises (skill gerador-de-praticas) fecharia a distância. **Não aplicada:** material novo.

---

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo | Avaliado em |
|---|---|---|---|
| OA-01 — distinguir petrocronologia de geocronologia; idade ancorada em textura e composição | Aula 01 (todas as seções); Aula 02 (fechamento = mineral + sistema) | sim — Aula 01 (zircão núcleo/borda), Aula 02 (cinco idades) | — (questionário ainda não gerado) |
| OA-02 — selecionar a técnica analítica | Aula 03 (cinco seções + tabela) | sim — Aula 03 (três problemas) | — |
| OA-03 — zoneamento de acessórios e de granada × trajetórias P-T e reações | Aulas 04, 05, 06; Aula 07 (seções 1-3) | sim — Aulas 04/05 (granada zonada), 06 (zircão com HREE) | — |
| OA-04 — interpretar dados integrados; duração e condições de um evento | Aula 07 (integração, polimetamorfismo) | sim — Aula 07 (sete idades, 15 Ma de crescimento, resfriamento) | — |

Nenhum objetivo sem cobertura; nenhuma seção órfã. Alinhamento com avaliação e flashcards não verificável ainda (não existem).

---

## Decisão sobre a avaliação do módulo

**Formato: 2 questionários parciais + 1 questionário final cumulativo.** O módulo tem agora **7 aulas** (~167 min), acima do limite de ~5-6 aulas em que o plugin recomenda um questionário único; e o mesmo formato foi usado no Módulo 26, de tamanho igual.

| Questionário | Aulas | Objetivos | Carga |
|---|---|---|---|
| Parcial 1 | 01-03 | OA-01, OA-02 | ~78 min de aula |
| Parcial 2 | 04-07 | OA-03, OA-04 | ~89 min de aula |
| Final cumulativo | 01-07 | OA-01 a OA-04, com questões de integração (ex.: temperatura de fechamento × técnica × zoneamento) | — |

O corte entre os parciais segue a costura do módulo: as Aulas 01-03 respondem "o que datar e com quê"; as Aulas 04-07 respondem "o que a idade significa na história P-T da rocha". As Partes 1 e 2 da antiga Aula 04 ficam no mesmo parcial, como deve ser um par.

**Restrições obrigatórias para quem gerar o questionário e os flashcards** (vêm das correções da auditoria e desta revisão):
1. Coeficiente de partição zircão/granada dos HREE: cobrar com o **sentido corrigido** — maior que 1 **a favor do zircão**; a granada domina o orçamento pela **abundância modal**. É a pegadinha natural do módulo e o erro que a auditoria removeu.
2. Monazita e Y: a sequência é **alto (pré-granada) → baixo (durante o crescimento da granada) → alto (após a quebra)**.
3. SIMS: **não** cobrar "resolução lateral superior à do LA-ICP-MS"; a vantagem é o volume amostrado/profundidade.
4. Fusão parcial por desidratação da biotita **produz** granada; não usar como exemplo de quebra da granada.
5. Zonas Sm-Nd de granada como idades de crescimento **só** com a ressalva da temperatura de fechamento (Aula 07).
6. **Não** cobrar o limite inferior de temperatura dos experimentos de Ferry & Spear (retirado das aulas por ser não verificável), nem equações de calibração dos termômetros de Zr (as aulas não as dão), nem paginação ou lista de autores de referências.

---

## O que está bem feito

Registrado para que as próximas revisões **não** estraguem:
1. **Um exemplo que atravessa o módulo.** O zircão da Aula 01 (núcleo 550 Ma, borda 480 Ma) volta na Aula 06 com a informação de HREE, e a leitura fica mais específica sem mudar de objeto. A granada da Aula 04 volta na Aula 05 com números. Essa continuidade ensina que a petrocronologia **acumula** leituras sobre o mesmo cristal — não a desfaça reescrevendo os exemplos isoladamente.
2. **Todo exemplo termina em interpretação, e vários dizem o que o número não significa** ("As cinco idades não competem", "O que falta").
3. **A ordem textura → reação → P-T → idade é declarada na Aula 04 e cumprida pelo módulo** — as aulas de técnica (03) e de petrologia (04-05) vêm antes das de cronômetros (06-07).
4. **Incerteza é declarada onde existe:** Th/U como "tendência útil, não lei rígida", o debate das granadas rotacionadas "não resolvido aqui", os valores de fechamento como "aproximações de referência, não constantes universais".
