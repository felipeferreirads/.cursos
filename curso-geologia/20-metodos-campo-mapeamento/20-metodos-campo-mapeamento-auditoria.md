# Auditoria científica — Módulo 20: Métodos de campo e mapeamento geológico

> [!info] Este relatório cobre o módulo em **duas rodadas**
> **Rodada 1 (2026-08-18)** — Aulas 01–06, modo `audit-and-fix`. Resultado: aprovado, 1 achado 🟠 corrigido.
> **Rodada 2 (2026-08-29)** — Aulas 07–10 (topografia instrumental), modo `audit` seguido de `audit-and-fix`. Resultado: 1 🟠 + 1 🟡, ambos corrigidos. Ver [Extensão — Aulas 07–10](#extensão--aulas-0710-topografia-instrumental-rodada-2) no fim deste arquivo.
> Este é o **único** relatório de auditoria do módulo 20. Não há arquivo separado para as aulas novas.

**Escopo acumulado:** as 10 aulas do módulo
**Veredito consolidado (2026-08-29): Aprovado** — 3 achados ao todo nas duas rodadas (2 🟠, 1 🟡), todos corrigidos. Nenhum achado em aberto.

---

# Rodada 1 — Aulas 01–06 (2026-08-18)

**Modo:** audit-and-fix (dentro do pipeline do curso)
**Escopo:** as 6 aulas do módulo, auditadas em conjunto
**Data:** 2026-08-18
**Veredito: Aprovado, com 1 achado 🟠 corrigido**

## Achados

### 🟠 1. Regra dos V incompleta: faltava o caso de mergulho a favor do vale mais íngreme que ele

**claim_id:** `GEO-M20-F01`
**Tipo:** omissão que gera erro
**Onde:** `20-metodos-campo-mapeamento-aula-03-mapa-geologico-regra-dos-v.md` · seção "A regra dos V: como o relevo distorce a forma de um contato"
**Estava escrito:** a aula descrevia apenas três casos (horizontal; mergulho a favor do vale mais suave que ele; mergulho contra o vale) e fechava com um resumo mnemônico afirmando que, em qualquer caso inclinado, "o V do contato aponta na direção do mergulho aparente da camada" e que os casos inclinados sempre produzem V apontando rio acima.
**Problema:** existe um quarto caso — mergulho a favor do sentido do vale e **mais íngreme** que a inclinação do próprio vale — em que o V do contato inverte de sentido e aponta rio **abaixo**, na direção do mergulho. A versão original da aula não cobria esse caso e o resumo final generalizava incorretamente, dando a entender que contatos inclinados sempre produzem V rio acima. Um aluno que aplicasse a regra como resumida erraria a leitura de um mapa real nesse caso específico.
**Correção aplicada:** reescrita da seção com os quatro casos, na ordem correta, e substituição do resumo mnemônico por uma explicação que deixa explícito que o sentido do V depende da comparação entre o mergulho da camada e a inclinação do vale, não apenas do sentido do mergulho isoladamente. Recap relâmpago e bloco de alegações auditáveis da aula também atualizados.
**Fonte:** SERC Carleton (Visible Geology teaching materials), [Rule of V's](https://serc.carleton.edu/visiblegeology/teaching_materials/310972.html); Geological Digressions, [The Rule of Vs in geological mapping](https://www.geological-digressions.com/the-rule-of-vs-in-geological-mapping/) · **Nível:** base de referência (material didático de geologia estrutural amplamente replicado; consistente com Compton, *Manual of Field Geology*, e Marshak & Fossen, *Structural Geology*).
**Confiança:** confirmado (múltiplas fontes didáticas independentes convergem no mesmo padrão de 4 casos).
**Também aparece em:** nenhum outro arquivo do módulo repetia o resumo incompleto — a Aula 04 (seção geológica) usa a regra dos V apenas de forma implícita, sem repetir o resumo, e não precisou de correção.
**Desfecho:** corrigido diretamente na aula (achado 🟠, correção direta conforme regra da skill). Nenhum questionário ou flashcard existia ainda no momento da correção — a auditoria roda antes da avaliação, então não há material derivado a propagar.

## Verificado e correto

As demais alegações auditáveis marcadas nas seis aulas foram verificadas contra fonte e não apresentaram erro:

| claim_id | Aula | Alegação | Fonte | Confiança |
|---|---|---|---|---|
| `GEO-M20-A01-CADERNETA-001` | 01 | Caderneta de campo é o documento primário do trabalho geológico | prática padrão (Compton; USGS field methods) | provável (prática metodológica, não um fato isolado verificável por busca única) |
| `GEO-M20-A01-AMOSTRA-ORIENTADA-002` | 01 | Amostra orientada é marcada antes de ser destacada da rocha | prática padrão de geologia estrutural/paleomagnetismo | provável |
| `GEO-M20-A02-DIRECAO-MERGULHO-001` | 02 | Direção é a interseção horizontal do plano inclinado com plano horizontal; mergulho é o ângulo perpendicular à direção, 0°–90° | definição padrão (Marshak & Fossen; Compton) | confirmado |
| `GEO-M20-A02-BUSSOLA-002` | 02 | Bússola de geólogo combina bússola magnética e clinômetro | prática padrão de campo | confirmado |
| `GEO-M20-A02-DECLINACAO-003` | 02 | Declinação magnética varia com local e tempo, exigindo correção periódica | NOAA/modelos de campo magnético; prática padrão | confirmado |
| `GEO-M20-A03-CONTATO-TRACO-001` | 03 | Contato observado (linha cheia), inferido (tracejada), coberto (pontilhada) | convenção FGDC/USGS de simbolização cartográfica geológica | confirmado |
| `GEO-M20-A04-EXAGERO-VERTICAL-001` | 04 | Escala vertical exagerada é comum em seções, distorce ângulos aparentes | prática padrão (Compton; Groshong, *3-D Structural Geology*) | confirmado |
| `GEO-M20-A04-SECAO-BALANCEADA-002` | 04 | Seção balanceada testa plausibilidade geométrica ao "desdobrar" a estrutura | geologia estrutural clássica (Dahlstrom; Groshong) | confirmado |
| `GEO-M20-A05-ESPESSURA-REAL-001` | 05 | Espessura aparente ≥ espessura real, igualdade só quando horizontal ou medida perpendicular | geometria estrutural padrão | confirmado (decorre diretamente de trigonometria — cos do ângulo de mergulho) |
| `GEO-M20-A05-BASTAO-JACOB-002` | 05 | Bastão de Jacob é instrumento graduado com clinômetro para espessura real em campo | Wikipedia (Jacob's staff); AAPG Bulletin (Kummel 1943); ResearchGate | confirmado |
| `GEO-M20-A05-SECAO-TIPO-003` | 05 | Seção-tipo é referência formal para descrever/correlacionar unidade estratigráfica | North American Stratigraphic Code; International Stratigraphic Guide (ICS) | confirmado |
| `GEO-M20-A06-ASSINATURA-ESPECTRAL-001` | 06 | Materiais têm assinaturas espectrais distintas, permitindo mapear alteração hidrotermal por sensoriamento remoto | USGS; prática padrão de exploração mineral | confirmado |
| `GEO-M20-A06-GPS-PRECISAO-002` | 06 | GPS de uso geral: ordem de metros; DGPS/RTK/geodésico: ordem de centímetros | múltiplas fontes técnicas convergentes (TerraFlow, Mapscaping, RTK GPS Survey) | confirmado |

## Consistência interna do módulo

Verificado especificamente porque auditorias anteriores do curso encontraram inconsistências transversais entre aulas de um mesmo módulo:

- Numeração de pontos, notação de atitude (direção/mergulho vs. azimute do mergulho) e terminologia (afloramento, contato, atitude) usadas de forma consistente nas 6 aulas.
- A Aula 04 (seção geológica) usa a atitude e a projeção em profundidade de forma coerente com o que a Aula 02 ensina sobre direção e mergulho, e com a regra dos V corrigida da Aula 03.
- A Aula 05 (coluna estratigráfica) reutiliza corretamente o conceito de atitude da Aula 02 para justificar a diferença entre espessura aparente e real.
- Nenhum valor numérico se repete de forma divergente entre as aulas — o módulo não trata de idades geológicas nem de propriedades físicas de minerais, que foram a origem das inconsistências numéricas encontradas em módulos anteriores (crosta continental, taxa de espalhamento).

## Observação fora de escopo (não é achado factual)

Nenhuma observação didática relevante — a revisão de didática, se necessária, cabe ao `revisor-didatico` e não foi acionada nesta rodada por não haver sinal de sobrecarga cognitiva ou salto de pré-requisito nas seis aulas.

## Correções aplicadas

**Aplicadas em:** 2026-08-18

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `GEO-M20-F01` | 🟠 | Corrigido | 20-metodos-campo-mapeamento-aula-03-mapa-geologico-regra-dos-v.md |

**Pendências da rodada 1:** nenhuma.

---

# Extensão — Aulas 07–10 (topografia instrumental), rodada 2

**Auditado em:** 2026-08-29
**Material:** aulas 07, 08, 09 e 10, acrescentadas ao módulo em 2026-08-29
**Modo:** audit (Fase 1) → **audit-and-fix** (Fase 2, após autorização do usuário — ver "Correções aplicadas" no fim)
**Profundidade:** full
**Escopo verificado com prioridade:** tolerâncias e classes da NBR 13133; datum SIRGAS2000 (elipsoide e época de referência); fator de escala da projeção UTM; classificação dos métodos de nivelamento; regra de Bowditch. Toda a aritmética dos exemplos trabalhados foi recalculada.
**Veredito: Aprovado** — 0 🔴, 1 🟠 e 1 🟡, ambos corrigidos em 2026-08-29.

## Resumo da rodada 2

🔴 0 erros · 🟠 1 impreciso · 🟡 1 desatualizado · 🔵 0 sem fonte · ⚪ 0 controversos. Verificadas e corretas: 14 alegações.

As quatro aulas são, no conjunto, tecnicamente sólidas: **todos os valores normativos e numéricos de risco conferidos bateram** — 1:12.000, Tα crescendo com √n, GRS80, época 2000.4, 0,9996, 60 fusos de 6°, fuso 24S de 42°W a 36°W, hierarquia de precisão dos três nivelamentos, e Bowditch proporcional ao comprimento dos lados. Os dois achados são pontuais: uma fórmula auxiliar que devolve o fuso errado, e a descrição de um esquema de classes que a edição vigente da norma já simplificou.

## Achados da rodada 2

### 🟠 2. A fórmula prática de número de fuso UTM devolve o fuso errado

**claim_id:** `TOP-M20A10-UTMFUSO-003`
**Tipo:** impreciso (com inconsistência interna)
**Onde:** `20-metodos-campo-mapeamento-aula-10-sirgas2000-utm-gnss-geodesico.md` · Exemplo trabalhado
**Está escrito:** "a fórmula prática para longitude oeste é: número do fuso = 31 − (parte inteira de longitude/6, com ajuste de sinal)"

**Problema:** a fórmula, aplicada como escrita, dá o fuso errado — inclusive no próprio exemplo em que aparece. Para Salvador, a 38°30'W: parte inteira de 38,5/6 = parte inteira de 6,417 = 6; 31 − 6 = **25**. Mas o fuso correto é o **24**, como a própria frase seguinte da aula conclui pela via prática ("o fuso 24S cobre de 42°W a 36°W"). A aula se contradiz em duas linhas consecutivas.

O erro é sistemático, não um caso isolado: com "parte inteira" (piso), a fórmula erra em uma unidade sempre que |longitude|/6 não for inteiro exato. Para São Paulo, 46,6°W: 31 − 7 = 24, quando o fuso correto é 23. O que funciona é o **teto**, não a parte inteira: fuso = 31 − ⌈|λ|/6⌉ → 31 − ⌈6,417⌉ = 31 − 7 = 24 ✓; e 31 − ⌈7,767⌉ = 31 − 8 = 23 ✓. Equivalentemente, e válido para os dois hemisférios: fuso = ⌊(λ + 180)/6⌋ + 1, com λ negativo a oeste → ⌊(−38,5 + 180)/6⌋ + 1 = ⌊23,58⌋ + 1 = 24 ✓.

A expressão "com ajuste de sinal" sinaliza que o autor sabia que a fórmula estava incompleta, mas ela é publicada como se fosse utilizável.

**Correção proposta:** "a fórmula geral, válida nos dois hemisférios, é: número do fuso = ⌊(longitude + 180°)/6⌋ + 1, com a longitude negativa a oeste — para 38°30'W: ⌊(−38,5 + 180)/6⌋ + 1 = ⌊23,58⌋ + 1 = 24. Na prática de campo, é mais simples lembrar que o fuso 24S cobre de 42°W a 36°W, faixa que contém 38°30'W."
**Fonte:** [EPSG:32724 — WGS 84 / UTM zone 24S](https://epsg.io/32724) (limites 42°W–36°W, meridiano central 39°W, fator de escala 0,9996); [Universal Transverse Mercator coordinate system](https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system) (numeração dos 60 fusos a partir do antimeridiano) · **Nível:** base de referência (registro EPSG é a referência normativa de facto para parâmetros de projeção)
**Confiança:** confirmado
**Também aparece em:** **nenhum arquivo derivado.** Conferidos um a um: o questionário final e os três arquivos de flashcards cobrem fusos, fator de escala e declaração de datum, mas **nenhum reproduz esta fórmula**. Não há propagação a fazer — a correção se esgota na aula 10.

---

### 🟡 3. A NBR 13133 é descrita pelo esquema de classes da edição de 1994, já simplificado na edição vigente

**claim_id:** `TOP-M20A07-NBR13133-002`
**Tipo:** desatualização
**Onde:** `20-metodos-campo-mapeamento-aula-07-teoria-dos-erros-topografia-nbr13133.md` · "O que a NBR 13133 exige"; e a linha de Fontes
**Está escrito:** "A norma classifica poligonais planimétricas em classes conforme o rigor exigido, associando a cada classe uma **precisão relativa mínima** [...] (por exemplo, uma precisão relativa de 1:12.000 significa que...)"; e, em Fontes, "ABNT NBR 13133 (edição vigente)".

**Problema:** o **número está certo** e o conceito de precisão relativa está corretamente explicado — o que está desatualizado é a moldura normativa em volta dele. A edição de 1994 organizava as poligonais planimétricas em classes (IP, IIP, IIIP, IVP), cada uma com sua própria precisão relativa. A edição vigente, **ABNT NBR 13133:2021**, incorporou uma **simplificação das classes e tolerâncias** das poligonais planimétricas (inclusive com GNSS) e adota **1:12.000 como a precisão relativa mínima de referência**, com a ressalva de que, em casos especiais, a tolerância adequada deve ser estabelecida em comum acordo entre contratante e contratado. Ou seja: 1:12.000 não é "um exemplo de valor de uma classe entre várias", é o valor mínimo de referência geral da norma atual.

Some-se a isso que a aula cita "edição vigente" sem nomeá-la. Numa alegação normativa, a edição **é** parte do fato: um leitor que consultar a edição de 1994 encontrará um esquema diferente e concluirá que a aula está errada. O bloco `alegacoes_auditaveis` da própria aula já registrava essa dúvida ("confirmar edição exata da norma antes de citar valor numérico em contexto normativo formal") — **esta auditoria resolve essa pendência**: a edição é a de 2021 e o valor 1:12.000 está confirmado nela.

Confirmado também, e correto na aula: a **tolerância angular cresce com o número de vértices** — a norma a expressa como Tα = 3·p·√n + 10″, onde p é a precisão nominal do equipamento para a finalidade e n o número de estações. O crescimento é com √n, o que é consistente com o argumento de acúmulo de erro acidental que a aula usa.

**Correção proposta:** "A **ABNT NBR 13133:2021** é a edição vigente da norma brasileira que rege a execução de levantamentos topográficos. Ela define os **critérios de aceitação** de um levantamento e, para as poligonais planimétricas, simplificou o esquema de classes das edições anteriores: adota como valor de referência uma **precisão relativa mínima de 1:12.000** (o erro linear de fechamento não deve superar 1 parte em 12.000 do perímetro percorrido), admitindo tolerância diferente, em casos especiais, mediante acordo entre contratante e contratado. À precisão relativa soma-se uma **tolerância angular** que cresce com a raiz do número de estações da poligonal, refletindo o acúmulo de erro acidental a cada ângulo medido."
**Fonte:** [ABNT NBR 13133:2021, *Execução de levantamento topográfico*](https://arquivos.ufrrj.br/arquivos/20230102302b983573184b44fe6044133/ABNT_NBR_13133_2021-1-1.pdf) (57 p., © ABNT 2021); [*Atualização da NBR 13133 e seus impactos*, COBRAC/UFSC](https://ojs.sites.ufsc.br/index.php/cobrac/article/download/10632/9068) — documenta a simplificação das classes e tolerâncias das poligonais planimétricas na revisão de 2021 · **Nível:** normativa · **Versão:** ABNT NBR 13133:2021 (consultada em 2026-08-29)
**Confiança:** confirmado
**Também aparece em:** o questionário final (questões 18 e 19 e seus gabaritos) e os flashcards `geologia-m20-fb066` e `fb067` usam o mesmo enquadramento. **Nenhum deles fica errado com a correção** — o gabarito da questão 19 inclusive já diz "nas classes atualizadas", e o valor 1:12.000 permanece o mesmo. A propagação, quando a correção for aplicada, é de precisão de linguagem, não de gabarito: nenhuma resposta muda.

## Verificado e correto — rodada 2 (aulas 07–10)

| claim_id | Aula | Alegação | Fonte | Confiança |
|---|---|---|---|---|
| `TOP-M20A07-ERROS3TIPOS-004` | 07 | Erro grosseiro (detectável/eliminável), sistemático (causa conhecida, sentido único, corrigível) e acidental (residual, tratado estatisticamente) | teoria clássica de erros em topografia | confirmado |
| `TOP-M20A07-PRECACUR-005` | 07 | Precisão (concordância entre repetições) ≠ acurácia (proximidade do valor verdadeiro); é possível ter uma sem a outra | metrologia padrão (VIM/ISO) | confirmado |
| `TOP-M20A07-TOLANGULAR-006` | 07 | A tolerância angular da NBR 13133 cresce com o número de vértices da poligonal (Tα = 3·p·√n + 10″) | NBR 13133:2021; COBRAC/UFSC | confirmado |
| `TOP-M20A07-ESTACAOTOTAL-007` | 07 | Estação total = teodolito eletrônico (ângulos) + distanciômetro eletrônico (distâncias) no mesmo corpo | literatura técnica de topografia | confirmado |
| `TOP-M20A08-AZIMUTERUMO-008` | 08 | Conversão rumo→azimute por quadrante: NE = rumo; SE = 180−rumo; SW = 180+rumo; NW = 360−rumo | trigonometria de topografia plana | confirmado |
| `TOP-M20A08-PROJECOES-009` | 08 | Projeção N-S = distância × cos(azimute); projeção E-W = distância × sen(azimute) | topografia plana padrão | confirmado |
| `TOP-M20A08-BOWDITCH-010` | 08 | A regra de Bowditch (compass rule) distribui o erro de fechamento proporcionalmente ao comprimento de cada lado | [Compass/Bowditch rule](https://calculator.academy/compass-rule-adjustment-calculator/); prática topográfica padrão | confirmado |
| `TOP-M20A08-EXEMPLONUM-011` | 08 | Projeções, erro de fechamento ≈ 43,9 m e precisão relativa ≈ 1:9 do exemplo, recalculados | recálculo (cos/sen dos azimutes 60°, 170°, 290°) | confirmado |
| `TOP-M20A09-NIVELPRECISAO-012` | 09 | Precisão decrescente: geométrico (ordem milimétrica) > trigonométrico (centimétrica) > barométrico (métrica) | literatura técnica de topografia (CPE Tecnologia; dissertação USP sobre nivelamento) | confirmado |
| `TOP-M20A09-GAUSSAREA-013` | 09 | Fórmula de Gauss (shoelace) para A(0,0), B(120,0), C(60,80) dá 4.800 m²; confere com ½ × base × altura | recálculo | confirmado |
| `TOP-M20A09-AREASMEDIAS-014` | 09 | Volume por áreas médias: [(15+25)/2] × 20 = 400 m³ | recálculo | confirmado |
| `TOP-M20A10-SIRGAS2000-015` | 10 | SIRGAS2000: datum oficial do Brasil desde fevereiro de 2005 (Resolução PR 01/2005 do IBGE), elipsoide GRS80, época de referência 2000,4 | [IBGE, RPR 01/25fev2005](https://geoftp.ibge.gov.br/metodos_e_outros_documentos_de_referencia/normas/rpr_01_25fev2005.pdf); [IBGE/PMRG](https://www.ibge.gov.br/geociencias/informacoes-sobre-posicionamento-geodesico/sirgas/16691-projeto-mudanca-do-referencial-geodesico-pmrg.html) | confirmado |
| `TOP-M20A10-UTMPARAMS-016` | 10 | UTM: 60 fusos de 6° de longitude; fator de escala 0,9996 no meridiano central; fuso 24S de 42°W a 36°W (meridiano central 39°W) | [EPSG:32724](https://epsg.io/32724); [UTM](https://en.wikipedia.org/wiki/Universal_Transverse_Mercator_coordinate_system) | confirmado |
| `TOP-M20A10-GNSSPRECISAO-017` | 10 | Posicionamento absoluto ~metros; relativo/diferencial ~centímetros a decímetros; RTK ~centímetros em tempo real | consenso de literatura técnica de geodésia/GNSS | confirmado |

### Nota sobre o SIRGAS2000 (não é achado)

A aula diz "datum geodésico oficial do Brasil desde 2005", o que está correto. Vale registrar, para eventual enriquecimento futuro (não é erro): houve um período de transição de dez anos — entre 25/02/2005 e 25/02/2015 admitia-se também SAD69 e Córrego Alegre, e só **desde 25/02/2015 o SIRGAS2000 é o único** sistema oficialmente adotado. Isso reforça, em vez de contradizer, o argumento da aula sobre por que todo dado antigo precisa ter o datum declarado.

## Consistência interna — aulas 07–10 e o resto do módulo

- A cadeia 07 → 08 → 09 → 10 é coerente: os erros da 07 alimentam o fechamento da 08, cujas coordenadas alimentam a área da 09, situadas no referencial da 10.
- O ângulo vertical apresentado na 07 é reusado corretamente na 09 (nivelamento trigonométrico).
- A precisão do GPS de mão da aula 06 (ordem de metros) é consistente com o posicionamento absoluto da aula 10 — sem divergência numérica entre as duas rodadas de aulas.
- A "precisão relativa" é definida de forma idêntica nas aulas 07 e 08. Nenhum valor numérico diverge entre aulas.

## Observações não factuais (fora de escopo)

- Aula 08, exemplo trabalhado: ΔE total é apresentado como 7,7 m, que é a soma dos valores **já arredondados** exibidos (103,9 + 26,0 − 122,2); com os valores sem arredondar, 7,81 m. O erro de fechamento (43,9 m) e a precisão relativa (≈1:9) não mudam. Prática de arredondamento aceitável, registrada apenas por transparência.
- **Gate invertido, a registrar:** o questionário e os flashcards foram estendidos para `oa07`–`oa10` em 2026-08-29, **antes** desta auditoria — o inverso da ordem que o plugin prescreve (aulas → auditoria → avaliação → flashcards). Não houve dano nesta rodada: a verificação carta a carta e questão a questão não encontrou nenhum gabarito ou verso errado. Mas o `validate_state.py` passa a acusar `gate.assessment` e `gate.flashcards` para o módulo 20 enquanto o achado 🟠 estiver aberto, e é correto que acuse.

---

## Correções aplicadas — rodada 2

**Aplicadas em:** 2026-08-29 (modo `audit-and-fix`, autorizado pelo usuário após a entrega da Fase 1)

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `TOP-M20A10-UTMFUSO-003` | 🟠 | **Corrigido** | aula 10 |
| `TOP-M20A07-NBR13133-002` | 🟡 | **Corrigido** | aula 07, questionário final, `-flashcards-basic.csv`, `-flashcards.md` |

**O que mudou:**

- **Aula 10, exemplo trabalhado** — a fórmula do fuso passou a ser a geral e correta, `parte inteira de (longitude + 180°)/6, mais 1`, válida nos dois hemisférios, com o cálculo explícito para 38°30'W dando 24. A regra prática de campo (fuso 24S cobre 42°W–36°W) foi mantida como atalho, agora coerente com a fórmula em vez de contradizê-la.
- **Aula 07** — a norma passou a ser nomeada como **ABNT NBR 13133:2021**, com o registro de que essa edição simplificou o esquema de classes das anteriores e adota 1:12.000 como precisão relativa mínima de referência (e não como valor de uma classe entre várias), incluindo a ressalva de acordo entre contratante e contratado em casos especiais. A tolerância angular passou a ser descrita como crescendo com a **raiz** do número de estações. Ajustados, na mesma medida: a entrada da tabela de vocabulário, o recap relâmpago e a seção de Fontes.
- **Bloco `alegacoes_auditaveis` da aula 07** — a pendência que o próprio autor havia registrado ("confirmar edição exata da norma antes de citar valor numérico") foi **resolvida e marcada como tal**, com a edição e o valor confirmados.

**Propagação verificada arquivo a arquivo:**

- **Fórmula do fuso UTM** — reconferida no questionário final e nos três arquivos de flashcards (`.md`, `-basic.csv`, `-cloze.csv`): **não aparece em nenhum**. Nada a propagar; a correção se esgotou na aula 10, como a Fase 1 previa.
- **NBR 13133** — aparece em quatro lugares derivados. Corrigidos: o gabarito da questão 18 (passou a nomear a edição de 2021 e deixou de falar em "classes de precisão") e o gabarito da questão 19 ("nas classes atualizadas" → "a NBR 13133:2021 adota precisão relativa mínima de referência de 1:12.000"); e o card `geologia-m20-fb066`, cujo verso passou a "Os critérios de aceitação e as tolerâncias para execução de levantamentos topográficos (edição vigente: ABNT NBR 13133:2021)". Conferidos e **inalterados por não precisarem de correção**: `fb067`, `fb068` e `fc035`, que tratam de precisão relativa e acúmulo de erro angular sem depender da edição. **Nenhuma resposta correta mudou** — nenhuma questão ficou sem sentido e nenhum distrator virou gabarito.
- Atualizada também a linha de `pendencias` em `-flashcards.md`, que ainda declarava a auditoria das aulas 07–10 como não realizada.

> [!warning] Aviso sobre o Anki
> O card `fb066` teve o verso alterado. Se este baralho já foi importado no Anki, reimportar o CSV atualiza o card pelo `id` — mas, dependendo da configuração de importação, um card já em revisão pode não ser sobrescrito. Confira o `fb066` no Anki depois de reimportar.

**Pendências da rodada 2:** nenhuma. **Gate científico liberado:** 0 achados 🔴 ou 🟠 em aberto no módulo. Nenhum achado 🔵 ou ⚪ foi levantado em nenhuma das duas rodadas.

