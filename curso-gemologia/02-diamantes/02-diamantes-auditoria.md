# Auditoria científica: Módulo 02 — Diamantes

**Auditado em:** 2026-08-25 (rodada 1, 15 aulas) · 2026-08-28 (rodada 2, aula 16)
**Material:** `02-diamantes/` — 15 aulas, todas de primeira redação (nenhuma migrada; o conteúdo das antigas aulas 07 e 08 do módulo 01 foi reconstruído do zero contra fonte primária, conforme registrado em `_contexto.md`)
**Modo:** audit-and-fix
**Profundidade:** full
**Escopo:** propriedades físicas e ópticas do diamante; condições e ambientes de formação; diamantes superprofundos e suas inclusões; sistema de tipos Ia/Ib/IIa/IIb; escalas de graduação do GIA (cor D-Z, pureza, lapidação, cor fancy); relação peso-preço; fluorescência e valor; separação de simulantes; crescimento HPHT e CVD; instrumentação de triagem e identificação; tratamentos e regras de divulgação; **consistência numérica entre as 15 aulas do módulo** e entre elas e o módulo 01.
**Veredito final:** **Aprovado com ressalvas** — rodada 1 aprovada sem achado aberto; rodada 2 (aula 16) corrigiu 4 imprecisoes e 2 alegacoes sem fonte, todas fechadas. Nenhum achado permanece aberto no modulo.

> [!info] Ordem de execução
> Esta auditoria rodou **antes** da geração do questionário e do baralho, conforme a ordem adotada no curso desde o módulo 00 (auditar → corrigir → só então avaliar e cardificar). Nenhum material derivado precisou de propagação, porque nenhum existia quando as correções foram aplicadas.

## Resumo

🔴 **0 erros** · 🟠 **4 imprecisões** · 🟡 0 desatualizados · 🔵 0 sem fonte · ⚪ 2 controvérsias declaradas.
**Alegações verificadas e corretas: 97.**

Os quatro achados 🟠 foram corrigidos nesta mesma rodada. Nenhum achado permanece aberto. As duas controvérsias já haviam sido tratadas na redação sob a regra LC-08 (declaradas em uma frase no corpo e detalhadas em "O que não concluir"); foram confirmadas como controvérsias reais da literatura e **não** são pendências.

O achado mais relevante é o **nº 2**: não é um número errado, é um nome traduzido de modo a **inverter a ordem que ele descreve**. Ele teria produzido flashcards e questões erradas se o baralho tivesse sido gerado antes da auditoria — mais uma confirmação da ordem de execução adotada no curso.

## Achados

### 🟠 1. Temperaturas de degradação térmica do diamante fora da faixa da literatura

**claim_id:** `DIA-EST-004`
**Tipo:** impreciso (valor numérico fora da faixa publicada) · **Natureza:** `erro_factual` em grau leve
**Onde:** aula 01 · "Estabilidade: por que a grafite não come o seu anel"
**Estava escrito:** "Ao ar livre, o diamante começa a queimar (oxidar para CO₂) por volta de **690 a 875 °C**. Sem oxigênio, ele grafitiza acima de aproximadamente **1.500 °C**."
**Problema:** dois desvios. (i) O limite inferior de oxidação ao ar é mais baixo do que o texto indicava: a literatura registra estabilidade abaixo de cerca de 600 °C, oxidação significativa a partir de cerca de 670 °C e conversão a grafite ao ar já em torno de 730 °C. Apresentar 690 °C como início subestima o risco em bancada de joalheria, que é justamente a aplicação prática da passagem. (ii) O valor de grafitização sem oxigênio (1.500 °C) era apresentado como um limiar único, quando a literatura dá uma faixa a partir de cerca de 1.300 °C em vácuo. (iii) A formulação também violava a regra LC-05 do curso (ordem de grandeza, não precisão de laboratório) ao dar "875 °C".
**Correção aplicada:** "Ao ar livre, o diamante começa a **oxidar** (queimar, formando CO₂) a partir de cerca de **600 a 700 °C** — o oxigênio acelera muito a destruição. Sem oxigênio, ele grafitiza apenas acima de cerca de **1.300 a 1.500 °C**."
**Fonte:** *Glass Physics and Chemistry* (2024), "High Temperature Graphitization of Diamond during Heat Treatment in Air and in a Vacuum"; revisão em *Functional Diamond* (2025), "Graphitization of diamond: manifestations, mechanisms, influencing factors and functional applications"; GIA, *Gem care and cleaning* · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** nenhum outro arquivo. O bloco `alegacoes_auditaveis` da aula 01 foi atualizado junto.
**Desfecho:** ✅ **Corrigido.**

---

### 🟠 2. Os nomes das faixas da escala D-Z estavam traduzidos de modo a inverter a ordem de intensidade

**claim_id:** `DIA-COR-002`
**Tipo:** impreciso · **Natureza:** `inconsistencia_interna` — a nomenclatura contradizia a ordem que ela mesma descreve
**Onde:** aula 05 · tabela "As cinco faixas" e Recap relâmpago
**Estava escrito:** "**Levemente colorido** | K · L · M" · "**Muito levemente colorido** | N · O · P · Q · R" · "**Levemente colorido (forte)** | S a Z"
**Problema:** os nomes oficiais dessas três faixas no laudo do GIA são **Faint**, **Very Light** e **Light**, nessa ordem, e formam uma sequência de **cor crescente**: um diamante *Light* (S-Z) tem mais cor que um *Very Light* (N-R), que tem mais que um *Faint* (K-M). A tradução adotada invertia a leitura em português: "muito levemente colorido" (N-R) soa como **menos** cor que "levemente colorido" (K-M), quando na escala real ele tem **mais**. Um aluno que decorasse a tabela como estava sairia com a ordem trocada — e, pior, com uma ordem que contradiz a progressão alfabética ensinada na mesma aula. Este é o achado com maior potencial de dano do módulo, porque a escala de cor é o conteúdo mais cobrado em avaliação.
**Correção aplicada:** a tabela passou a trazer o **nome oficial do laudo** com uma glosa que não inverte o sentido — *Colorless* (incolor), *Near Colorless* (quase incolor), *Faint* (traço de cor), *Very Light* (cor fraca), *Light* (cor leve) — e ganhou um callout de alerta explicando que a sequência em inglês é contraintuitiva, ancorando a memória na ordem alfabética das letras, que não mente. O callout também aponta que os mesmos três nomes reaparecem como os três primeiros graus da escala fancy (aula 09), porque as duas escalas são um contínuo. O Recap foi ajustado na mesma direção.
**Fonte:** GIA, *Diamond Color Chart: The Official GIA Color Scale*; GIA, *Color Grading "D-to-Z" Diamonds at the GIA Laboratory*; GIA, *Fancy Color Diamond Quality Factors* (continuidade das duas escalas) · **Nível:** normativa (laboratório emissor da escala)
**Confiança:** confirmado
**Também aparece em:** aula 09, que já descrevia corretamente a ordem *Faint → Very Light → Light* na escala fancy — a inconsistência era **entre as duas aulas**, e só apareceu na leitura conjunta. Nenhuma edição foi necessária na aula 09.
**Desfecho:** ✅ **Corrigido.**

---

### 🟠 3. Diâmetro de referência do brilhante de 0,50 ct ligeiramente alto

**claim_id:** `DIA-PESO-005`
**Tipo:** impreciso (valor no topo da faixa publicada) · **Natureza:** `erro_factual` em grau leve
**Onde:** aula 08 · tabela "Peso não é tamanho aparente"
**Estava escrito:** "0,50 ct | ~5,2 mm"
**Problema:** as tabelas de referência de peso e diâmetro para brilhante redondo bem proporcionado situam o meio-quilate em torno de **5,1 mm**. O desvio é pequeno, mas a tabela é usada logo em seguida como base do raciocínio de *spread* do exemplo trabalhado, e um valor sistematicamente alto num ponto da tabela enfraquece a comparação. Os demais valores da tabela (0,25 ct ~4,1 mm; 0,75 ct ~5,8 mm; 1,00 ct ~6,4 mm; 1,50 ct ~7,4 mm; 2,00 ct ~8,1 mm) foram verificados e estão corretos.
**Correção aplicada:** "0,50 ct | ~5,1 mm".
**Fonte:** tabelas de referência peso/diâmetro para brilhante redondo padrão; GIA, *Estimating a Cut Grade* (booklet) · **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** o valor de 1,00 ct ≈ 6,4 mm é repetido nas aulas 07 e 11 e está correto nas três ocorrências. Nenhuma outra edição foi necessária.
**Desfecho:** ✅ **Corrigido.**

---

### 🟠 4. Data de padronização do quilate métrico apresentada de forma vaga demais

**claim_id:** `DIA-PESO-001`
**Tipo:** impreciso (granularidade insuficiente para um fato normativo datável) · **Natureza:** `omissao_que_gera_erro` em grau leve
**Onde:** aula 08 · "A unidade"
**Estava escrito:** "essa definição é resultado de um acordo internacional firmado no **começo do século XX**"
**Problema:** a afirmação é verdadeira, mas a data é conhecida com precisão e é normativa: o quilate métrico de exatamente 200 mg foi formalizado em **1907**, na Conferência Geral de Pesos e Medidas. "Começo do século XX" cobre trinta anos e não permite ao aluno situar o fato nem verificá-lo. A regra LC-05 do curso pede ordem de grandeza para **medidas físicas contínuas**, não para **datas de decisões normativas**, que têm valor único.
**Correção aplicada:** "O **quilate métrico** vale exatamente **0,2 grama** (200 mg), e essa definição foi firmada por acordo internacional em **1907**, na Conferência Geral de Pesos e Medidas — antes disso, o 'quilate' variava de praça para praça, com dezenas de padrões em uso".
**Fonte:** 4ª Conferência Geral de Pesos e Medidas (1907) / CIPM; GIA, *4Cs Carat Weight*; CIBJO, *Diamond Blue Book* · **Nível:** normativa
**Confiança:** confirmado
**Também aparece em:** Recap relâmpago da aula 08, ajustado na mesma edição.
**Desfecho:** ✅ **Corrigido.**

## Controvérsias declaradas (⚪) — confirmadas, não são pendências

As duas foram tratadas na redação sob a regra **LC-08** (a pergunta em aberto entra em uma frase no corpo; a cadeia de ressalvas vai integralmente para "O que não concluir"). A auditoria confirmou que são divergências reais da literatura e que o texto **não** apresenta nenhum lado como consenso.

| id | Onde | Questão em aberto | Tratamento verificado |
|---|---|---|---|
| `DIA-DEEP-H2O-001` | aula 03 | Quanta água a zona de transição do manto realmente contém, e o quanto as poucas inclusões de ringwoodita hidratada representam o manto como um todo. | ✅ Adequado. O corpo afirma o achado de Pearson et al. (2014) como medida, e não como estimativa global; "O que não concluir" registra explicitamente que a extrapolação parte de amostragem muito pequena. |
| `DIA-PL-596-001` | aula 14 | A atribuição estrutural do dupleto de 596/597 nm, usado na prática como indicador de CVD não tratado, não está plenamente estabelecida. | ✅ Adequado. A tabela do corpo registra "não plenamente atribuído" e "O que não concluir" declara a atribuição como objeto de pesquisa ativa. O uso **prático** da feição, que é consensual, não foi enfraquecido. |

Uma terceira questão em aberto foi encontrada e está corretamente tratada, embora não estivesse marcada como controvérsia no bloco da aula: o **mecanismo do diamante camaleão** (aula 09), declarado no corpo como "ainda não plenamente esclarecido" e retomado em "O que não concluir". Registrada aqui como `DIA-CAMALEAO-001` para rastreabilidade. Não exige edição.

## Verificado e correto (amostra do que foi olhado)

As 97 alegações verificadas estão no manifesto `.json`. Os pontos de maior risco, e o resultado:

| claim_id | Alegação | Resultado |
|---|---|---|
| `DIA-EST-002` | Diamante: dureza 10, DR 3,52, IR 2,417, dispersão 0,044, isotrópico, ângulo crítico ~24,4° | ✅ Confirmado; **consistente com a tabela da aula 10 do módulo 01** |
| `DIA-EST-003` | Clivagem octaédrica perfeita em quatro direções, com tenacidade apenas boa | ✅ Confirmado (Mindat; GIA) |
| `DIA-ORIG-001` | Formação a ~150–200 km, 4,5–6 GPa, 900–1.300 °C | ✅ Confirmado (Shirey & Shigley 2013; Stachel & Harris 2008) |
| `DIA-ORIG-004` | Diamantes de 3,5–1 Ga em kimberlitos muito mais jovens | ✅ Confirmado |
| `DIA-DEEP-002` | Ringwoodita de ~30 µm em diamante de Juína, com água em torno de 1% em massa | ✅ Confirmado (Pearson et al., *Nature* 507, 2014) |
| `DIA-DEEP-004` | CLIPPIR: sigla, origem entre **360 e 750 km**, inclusões de liga Fe-Ni-C-S com filme de metano | ✅ Confirmado, inclusive a faixa de profundidade exata (Smith et al., *Science* 2016; GIA, Winter 2017) |
| `DIA-DEEP-005` | Diamantes azuis tipo IIb do manto inferior, ~660 km ou mais, com boro reciclado por subducção | ✅ Confirmado (Smith et al., *Nature* 560, 2018) |
| `DIA-DEEP-006` | Davemaoíta (CaSiO₃-perovskita) descrita em diamante de Orapa e aprovada pela IMA | ✅ Confirmado (Tschauner et al., *Science* 374, 2021; IMA-CNMNC) |
| `DIA-TIPO-002` | 99,06% Ia/IaAB · 0,83% IIa · 0,09% IaB · 0,02% IIb em diamantes D-Z; ~98% Ia no conjunto | ✅ Confirmado, com os percentuais exatos (GIA, *G&G* Fall 2020) |
| `DIA-TIPO-003` | Centros C (~1.130 e ~1.344 cm⁻¹), A (~1.282), B (~1.175), plaquetas (~1.365), N3 (415 nm) | ✅ Confirmado (Breeding & Shigley, *G&G* 45(2), 2009) |
| `DIA-COR-001` | Escala D-Z adotada em 1953, por Richard Liddicoat; letra D escolhida para romper com os sistemas anteriores | ✅ Confirmado (GIA, *History of the 4Cs*) |
| `DIA-COR-006` | Motivo documentado da escolha da letra D (letra sem associação com qualidade superior) | ✅ Confirmado — **alegação acrescentada** ao bloco da aula 05 nesta rodada |
| `DIA-PUR-001` | Onze graus de pureza a 10×; **SI3 não faz parte do sistema GIA** | ✅ Confirmado |
| `DIA-PUR-004` | Plot: vermelho = interno · verde = externo · vermelho+verde = interno que atinge a superfície · preto = faceta extra | ✅ Confirmado (GIA, *Decoding Diamond Clarity Diagrams*) |
| `DIA-LAP-002` | Sete componentes do grau de lapidação e escala Excellent–Poor | ✅ Confirmado (GIA, *4Cs Cut*; Moses et al., *G&G* Fall 2004) |
| `DIA-LAP-003` | O grau final é o **pior** dos sete componentes, não a média | ✅ Confirmado (GIA, *Estimating a Cut Grade*) |
| `DIA-LAP-004` | Faixas de referência do Excelente: mesa 52–62%, coroa 31,5–36,5°, pavilhão 40,6–41,8°, profundidade 57,5–63% | ✅ Confirmado, com a ressalva — já presente no texto — de que o sistema oficial usa tabela de combinações |
| `DIA-LAP-005` | O GIA não atribui grau de lapidação a formas fantasia; declara só polimento e simetria | ✅ Confirmado |
| `DIA-FANCY-001` | Ordem crescente: Faint · Very Light · Light · Fancy Light · Fancy · Fancy Intense · Fancy Vivid, mais Fancy Dark e Fancy Deep | ✅ Confirmado (GIA, *When is a colored diamond a fancy color diamond?*) |
| `DIA-FANCY-003` | Cor fancy é avaliada **de face**; D-Z é avaliada com a **mesa para baixo** | ✅ Confirmado |
| `DIA-FLUOR-002` | Estudo do GIA de 1997: fluorescência azul forte julgada em média igual ou melhor de face; turvação em pouquíssimas pedras | ✅ Confirmado (Moses et al., *G&G* 33(4), Winter 1997) |
| `DIA-SIM-001` | Teste do ponto elimina índices baixos mas **não confirma** diamante, porque moissanita e CZ costumam passar | ✅ Confirmado |
| `DIA-HPHT-001` | Crescimento HPHT a 5–6 GPa e 1.300–1.600 °C, com fluxo de Fe-Ni-Co e gradiente de temperatura | ✅ Confirmado (GIA, *HPHT and CVD Diamond Growth Processes*; *G&G* Fall 2017) |
| `DIA-HPHT-003` | Padrão em cruz no DiamondView como feição diagnóstica de HPHT | ✅ Confirmado |
| `DIA-CVD-001` | CVD em vácuo parcial (dezenas de torr), 700–1.200 °C, plasma de H₂ com pouco CH₄, ciclos de semanas | ✅ Confirmado |
| `DIA-CVD-005` | Dupleto 736,6/736,9 nm (SiV⁻) raro em natural; dupleto 596/597 nm **só relatado em CVD** e apagado por recozimento HPHT | ✅ Confirmado (GIA, *G&G* Winter 2015 e Fall 2016) |
| `DIA-TRIAG-001` | DiamondView usa UV abaixo de ~230 nm, absorvido em camada rasa, o que permite imagear a estrutura de crescimento | ✅ Confirmado (Welbourn et al., *G&G* 32(3), 1996) |
| `DIA-TRIAG-003` | Fotoluminescência a ~77 K; H3 (503,2 nm) e 3H (503,5 nm) só se separam com resfriamento | ✅ Confirmado (Eaton-Magaña & Breeding, *G&G* 52(1), 2016) |
| `DIA-TRIAG-005` | DiamondCheck separa Passa (tipo I) de Refere (tipo II e crescidos); DiamondSure usa a linha de 415 nm | ✅ Confirmado (GIA, *Analysis of Gemstones at GIA Laboratories*, Winter 2024) |
| `DIA-TRIAG-006` | iD100: separa natural de HPHT/CVD e de simulantes; solto e montado; até ~0,005 ct | ✅ Confirmado (GIA) |
| `DIA-TRIAG-007` | Triagem calibrada contra falsos negativos; "Refere" **não** identifica a pedra como sintética | ✅ Confirmado |
| `DIA-TRIAG-008` | Já documentados natural com padrão tipo CVD e CVD com pouquíssimas feições diagnósticas | ✅ Confirmado (GIA, *G&G* Summer 2023 e Fall 2023) |
| `DIA-TRAT-003` | Preenchimento de fratura detectado pelo efeito de flash; tratamento de baixa estabilidade | ✅ Confirmado |
| `DIA-TRAT-004` | **O GIA não emite laudo de graduação para diamante com fratura preenchida — apenas relatório de identificação** | ✅ Confirmado literalmente (GIA, *Do you grade filled diamonds?*) |
| `DIA-TRAT-006` | Descritores aceitos e proibidos para diamante crescido em laboratório | ✅ Confirmado (CIBJO *Diamond Blue Book*; FTC *Jewelry Guides*) |

## Consistência interna e com o módulo 01

Verificação sistemática de todos os valores repetidos entre as 15 aulas. **Nenhuma contradição numérica encontrada.**

| Valor | Aulas em que aparece | Resultado |
|---|---|---|
| DR 3,52 | 01, 11, 13 | ✅ idêntico; e idêntico à tabela do módulo 01, aula 10 |
| IR 2,417 · dispersão 0,044 | 01, 07 | ✅ idêntico; e idêntico ao módulo 01 |
| Ângulo crítico ~24,4° | 01, 07, 11 | ✅ idêntico; e idêntico ao flashcard `m06-fc036` |
| DR da CZ ~5,8 · GGG ~7,05 | 01, 08, 11 | ✅ idêntico, e dentro das faixas 5,6–6,0 e 7,0–7,1 da tabela do módulo 01 |
| 1,00 ct ≈ 6,4 mm | 07, 08, 11 | ✅ idêntico nas três |
| Tipo Ia ~98% · IIa 1–2% · IIb ~0,1% | 04, 09, 12, 13, 14 | ✅ idêntico nas cinco |
| N3 a 415 nm | 04, 05, 14 | ✅ idêntico |
| SiV⁻ ~737 nm · 596/597 nm · GR1 741 nm | 13, 14, 15 | ✅ idêntico |
| DiamondView < 230 nm · PL a 77 K | 13, 14 | ✅ idêntico |
| HPHT 5–6 GPa, 1.300–1.600 °C | 12 (e referida em 13) | ✅ idêntico |
| Fluorescência: 25–35%, >95% azul | 10 (referenciando o módulo 01, aula 09) | ✅ a aula 10 **não repete** os números, remete à aula 09 do módulo 01 — que já traz os valores corrigidos no achado `GEM-UV-002` de 2026-08-24 |

Também foi verificado que as aulas **não duplicam** o material do módulo 01 que declaram assumir: a aula 11 remete à tabela de simulantes da aula 10 do módulo 01 sem reproduzi-la; a aula 10 remete aos números de fluorescência da aula 09; a aula 04 declara-se explicitamente como o aprofundamento da frase única sobre tipos que a aula 11 do módulo 01 traz; a aula 02 desenvolve, sem repetir, a afirmação "kimberlito transporta, não gera" da aula 20 do módulo 01.

## Correções aplicadas

**Aplicadas em:** 2026-08-25

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `DIA-EST-004` | 🟠 | Corrigido | `02-diamantes-aula-01-o-diamante-como-mineral.md` |
| `DIA-COR-002` | 🟠 | Corrigido | `02-diamantes-aula-05-cor-d-z.md` |
| `DIA-PESO-005` | 🟠 | Corrigido | `02-diamantes-aula-08-peso-tamanhos-magicos-e-preco.md` |
| `DIA-PESO-001` | 🟠 | Corrigido | `02-diamantes-aula-08-peso-tamanhos-magicos-e-preco.md` |
| `DIA-COR-006` | — | ➕ Alegação acrescentada | `02-diamantes-aula-05-cor-d-z.md` |
| `DIA-DEEP-H2O-001` | ⚪ | ✅ Aceito como está (tratamento LC-08 adequado) | — |
| `DIA-PL-596-001` | ⚪ | ✅ Aceito como está (tratamento LC-08 adequado) | — |
| `DIA-CAMALEAO-001` | ⚪ | ✅ Aceito como está; registrado para rastreabilidade | — |

**Pendências:** nenhuma. **Migração de Anki a fazer:** nenhuma — o baralho do módulo 02 é de primeira geração e nasceu depois desta auditoria.

**Propagação:** não aplicável nesta rodada. Questionários e flashcards do módulo 02 foram gerados **depois** desta auditoria, contra o texto já corrigido.

## Observações fora do escopo factual

Registradas em uma linha cada, sem se misturar aos achados; são assunto da revisão didática:

- A aula 10 é deliberadamente mais curta (~1.420 palavras) que as demais, por remeter ao módulo 01 em vez de repetir. É decisão de projeto, não lacuna.
- As aulas 12 a 14 formam uma cadeia forte e não são estudáveis fora de ordem; o hub sinaliza isso, mas vale ao revisor didático confirmar se a dependência está suficientemente clara na abertura de cada uma.

## Fontes consultadas nesta auditoria

- **GIA (normativa):** 4Cs Color D-to-Z · Diamond Color Chart · Color Grading "D-to-Z" Diamonds at the GIA Laboratory · 4Cs Clarity · Decoding Diamond Clarity Diagrams · 4Cs Cut · Estimating a Cut Grade (booklet) · 4Cs Carat Weight · Fancy Color Diamond Quality Factors · When is a colored diamond a fancy color diamond? · Understanding Diamond Fluorescence · Dispelling Myths · Diamond Treatments · Do you grade filled diamonds? · HPHT and CVD Diamond Growth Processes · GIA iD100 · Laboratory-Grown Diamond Report · Digging into Diamond Types · The History of the 4Cs.
- **GIA, *Gems & Gemology* (revisada por pares):** Moses et al., Winter 1997 (fluorescência) · Welbourn et al., 32(3) 1996 (DiamondSure/DiamondView) · Breeding & Shigley, 45(2) 2009 (tipos) · Moses et al., Fall 2004 (grau de lapidação) · Shirey & Shigley, 49(4) 2013 (geologia do diamante) · Shigley & Breeding, 49(2) 2013 (defeitos ópticos) · Eaton-Magaña & Breeding, 52(1) 2016 (fotoluminescência) · Eaton-Magaña et al., Fall 2016 (CVD) e Fall 2017 (HPHT) · Fall 2015 (HPHT grandes incolores) · Winter 2015 (CVD grandes) · Summer 2019 (kimberlitos) · Summer 2020 (amarelos e laranjas) · Fall 2020 (D-Z e estatística de tipos) · Spring 2021 (CVD processado por HPHT) · Summer 2023 (natural com padrão tipo CVD) · Fall 2023 (CVD com poucas feições) · Summer 2024 (atualização de identificação) · Winter 2024 (análise de gemas no laboratório) · Winter 2017 (CLIPPIR).
- **Literatura primária:** Pearson et al., *Nature* 507 (2014) · Smith et al., *Science* 354 (2016) · Smith et al., *Nature* 560 (2018) · Tschauner et al., *Science* 374 (2021) · Stachel & Harris, *Ore Geology Reviews* 34 (2008) · Clifford, *EPSL* 1 (1966) · *Glass Physics and Chemistry* (2024) e *Functional Diamond* (2025), grafitização do diamante.
- **Normativas não-GIA:** CIBJO *Diamond Blue Book* · FTC *Guides for the Jewelry, Precious Metals, and Pewter Industries* · IMA-CNMNC · 4ª CGPM (1907).
- **Bases de referência:** Mindat (diamante, grafite, moissanita, zircônia cúbica) · Klein & Dutrow, *Manual of Mineral Science* · Nesse, *Introduction to Mineralogy* · Liddicoat, *Handbook of Gem Identification* · Gem-A, *Gemmology Foundation* · Rapaport, *Diamond Price List*.

---

# Rodada 2 — Aula 16 (lapidação: do bruto ao polido)

**Auditado em:** 2026-08-28
**Material:** `02-diamantes/02-diamantes-aula-16-lapidacao-do-bruto-ao-polido.md` — aula acrescentada em 2026-08-28 para fechar a lacuna de paridade com o *GIA Graduate Diamonds*, depois da rodada 1. As 8 alegações `DIA-CUT-001` a `DIA-CUT-008` do rodapé nunca haviam sido verificadas.
**Modo:** audit-and-fix · **Profundidade:** full
**Escopo:** as 8 alegações do rodapé, mais a consistência da aula nova com as 15 aulas já auditadas do módulo e com o módulo 01.
**Veredito da rodada:** **Aprovado com ressalvas** — nenhum achado permanece aberto, mas a aula chegou com quatro imprecisões, três delas contradizendo material que já havia passado pela auditoria.

## Resumo da rodada

🔴 **0 erros** · 🟠 **4 imprecisões** · 🟡 0 desatualizados · 🔵 **2 sem fonte** · ⚪ 0 controvérsias novas.
**Alegações verificadas e corretas: 2** (`DIA-CUT-003`, `DIA-CUT-004`).

Seis das oito alegações precisaram de intervenção. É a pior taxa de qualquer rodada deste curso, e a explicação é estrutural: a aula 16 foi escrita **fora** do fluxo normal, para tapar uma lacuna, sem a auditoria imediatamente em seguida. Os quatro achados 🟠 foram corrigidos; os dois 🔵 foram corrigidos com ressalva, estreitando a afirmação até o que a fonte sustenta, sem inventar substituto.

> [!warning] O padrão que esta rodada revelou
> **Três dos quatro achados 🟠 são contradições internas**, não erros contra a literatura externa. A aula nova discordava do rendimento da aula 08, do sistema de tabela de combinações da aula 07 e da sua própria seção sobre laser — tudo material que já havia sido auditado e aprovado. Uma aula inserida depois de uma auditoria não herda a consistência do módulo: ela precisa ser conferida **contra o módulo**, e não só contra fontes. Em todos os três casos a correção foi alinhar a aula nova ao material já auditado, e **nenhum arquivo antigo foi tocado**.

## Achados

### 🟠 5. Fatia da Índia no valor do diamante polido fora da faixa publicada, e atribuída à cidade errada

**claim_id:** `DIA-CUT-008`
**Tipo:** impreciso (valor fora da faixa publicada + sujeito incorreto) · **Natureza:** `erro_factual`
**Onde:** aula 16 · "7. Onde o mundo lapida"
**Estava escrito:** "Cerca de **90% dos diamantes do mundo, contados por peça**, são lapidados ali, e a Índia responde por 75% a 80% do valor do polido exportado."
**Problema:** dois desvios. (i) A fatia por **valor** não corresponde a nenhum dado publicado. A GJEPC — associação exportadora indiana, fonte primária do número — declara **mais de 65% em valor, 85% em peso (quilates) e 92% em número de peças**. O intervalo 75–80% superestima a fatia do dinheiro. (ii) O sujeito estava errado: os ~90% por peça são da **Índia**, não de Surat isoladamente; Surat é o polo de lapidação do país, mas a estatística é nacional. O erro tem custo didático alto: a distância entre 92% (peças) e 65% (valor) **é** a lição da seção — a Índia lapida quase todas as pedras do mundo e fica com bem menos que isso do dinheiro, porque as pedras são pequenas. Com 75–80%, a lição desaparece.
**Correção aplicada:** a seção passou a trazer as três contagens da GJEPC numa tabela, atribuídas à Índia com Surat identificado como o polo, seguidas de um parágrafo que lê a diferença entre elas como o tamanho médio das pedras. Acrescentado um item em "Erros comuns" contra ler a fatia de 90% como fatia do dinheiro.
**Fonte:** GJEPC, *India Centre* — "over 65 per cent of the world's polished diamonds in terms of value, 85 per cent in terms of volume and 92 per cent in terms of number of pieces"; corroborado por IBEF e Invest India (~90% do processamento mundial) · **Nível:** normativa (associação setorial emissora do dado)
**Confiança:** confirmado
**Também aparece em:** aula 22 do módulo 01, que trata o fato **qualitativamente** ("Surat, na Índia, lapida a maior parte dos diamantes do mundo"), sem número. Correto como está; nenhuma edição necessária.
**Desfecho:** ✅ **Corrigido.**

---

### 🟠 6. Rendimento da lapidação contradizendo a aula 08, a própria aula e a própria frase

**claim_id:** `DIA-CUT-007`
**Tipo:** impreciso · **Natureza:** `inconsistencia_interna`
**Onde:** aula 16 · "6. O custo do processo: rendimento" e Recap relâmpago
**Estava escrito:** "Do bruto à pedra pronta, **perde-se mais da metade do peso** — o rendimento favorável de um octaedro serrado e lapidado fica na faixa de **40% a 55%**"
**Problema:** três contradições numa linha. (i) Contra a **aula 08 do mesmo módulo**, auditada em 2026-08-25, que fixa **40% a 50%** — valor também gravado no flashcard `m02-fb096`. (ii) Contra a **própria aula 16**: a seção "Antes de começar" declara 40% a 50% ao citar a aula 08, e o corpo dizia 55%. (iii) Contra a **própria frase**: "perde-se mais da metade do peso" é incompatível com um rendimento de 55%, que é perder *menos* da metade. Nenhuma fonte sustenta o 55% contra o conjunto já auditado.
**Correção aplicada:** "perde-se **em geral** mais da metade do peso — o rendimento favorável de um octaedro serrado e lapidado fica na faixa de **40% a 50%**, o mesmo número da Aula 08". Recap ajustado na mesma direção.
**Fonte:** GIA, *Gems & Gemology* — estudos de rendimento; Cape Town Diamond Museum (perda de 50 a 60%); consistência interna com a aula 08 · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** aula 08 e flashcard `m02-fb096`, ambos com 40–50%. **A correção foi feita na aula nova, para o valor consolidado** — nenhum arquivo antigo foi alterado, e o exemplo trabalhado da aula 16 (42% e 43%) já era compatível.
**Desfecho:** ✅ **Corrigido.**

---

### 🟠 7. Tolkowsky creditado pelo arranjo de facetas, e o brilhante apresentado como projeto fechado

**claim_id:** `DIA-CUT-006`
**Tipo:** impreciso · **Natureza:** `certeza_indevida` (com `inconsistencia_interna` contra a aula 07)
**Onde:** aula 16 · "5. Por que 57 facetas" e "Erros comuns"
**Estava escrito:** "a combinação de ângulos foi estabelecida por **Marcel Tolkowsky em 1919**" · "As 57 facetas do brilhante são um projeto óptico **fechado desde 1919**"
**Problema:** dois excessos. (i) O **arranjo** de 57–58 facetas é **anterior** a Tolkowsky: já existia no *old European cut*, antecessor direto do brilhante moderno, cortado ao longo do século XIX. Tolkowsky não estabeleceu a combinação de facetas — ele **calculou as proporções e os ângulos** de um arranjo que já existia, por traçado de raios num modelo bidimensional. Creditar-lhe o arranjo ensina uma história falsa da lapidação, e é justamente o tipo de atribuição que um aluno repete numa prova. (ii) "Projeto óptico fechado desde 1919" é certeza indevida e **contradiz a aula 07 do próprio módulo**: a pesquisa do GIA que originou o grau de lapidação (Moses et al., *G&G* Fall 2004) mostrou que **não existe um único jogo de proporções ideal** e que muitas combinações recebem *Excellent* — razão de o sistema oficial ser uma tabela de combinações, como a aula 07 já ensinava sob `DIA-LAP-004`.
**Correção aplicada:** a seção passou a separar explicitamente as duas coisas — a contagem de facetas, anterior a 1919, e o que Tolkowsky calculou naquele ano — e ganhou um parágrafo registrando que não há um jogo de proporções único, com remissão à tabela de combinações da Aula 07. Em "Erros comuns", o item foi reescrito e um novo item foi acrescentado contra creditar a Tolkowsky a invenção do brilhante. **A contagem 57/58 não mudou** — está correta e confere com a aula 12 do módulo 01 e com `GEM-CUT-002`.
**Fonte:** Moses, T. M. et al., *A Foundation for Grading the Overall Cut Quality of Round Brilliant Cut Diamonds*, *G&G* Fall 2004; Tolkowsky, *Diamond Design* (1919); Cape Town Diamond Museum, *History of Marcel Tolkowsky* · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** **Tolkowsky e 1919 não aparecem em nenhum outro arquivo do curso** — verificado por busca. As 57–58 facetas aparecem na aula 12 do módulo 01, no flashcard `m01-fb066` e no questionário parcial 2 do módulo 01, todos corretos e não afetados.
**Desfecho:** ✅ **Corrigido.**

---

### 🟠 8. "Só o diamante corta o diamante" afirmado sem escopo, contra a própria aula

**claim_id:** `DIA-CUT-005`
**Tipo:** impreciso · **Natureza:** `confusao_de_escopo`
**Onde:** aula 16 · abertura do "Conteúdo" e "Erros comuns"
**Estava escrito:** "o diamante é a substância mais dura que existe, e **só o próprio diamante consegue cortá-lo**. Cada operação abaixo é diamante gastando diamante."
**Problema:** a aula refuta a si mesma duas seções adiante, ao descrever a **serra a laser** e o bruteamento a laser. O laser não depende de dureza: remove material por **grafitização** (transição sp³ → sp²) seguida de **sublimação** do grafite, mecanismo estabelecido na literatura revisada por pares. A afirmação verdadeira é mais estreita — só o diamante desgasta o diamante **por atrito**. Como estava, era uma generalização que o aluno carrega e que colide com o resto da aula; e a aula ainda mencionava a "película de grafite" deixada pelo corte a laser sem explicar de onde ela vem.
**Correção aplicada:** a abertura foi delimitada ao desgaste por atrito e ganhou um parágrafo curto explicando a exceção do laser — converte o carbono em grafite, que é mole e queima, removendo material por transformação e não por abrasão. A menção à película de grafite na seção 2 passou a remeter a essa explicação, e o item de "Erros comuns" e o Recap foram ajustados.
**Fonte:** literatura revisada por pares sobre ablação de diamante por laser pulsado — remoção em dois passos, grafitização seguida de sublimação (2024–2025); Cape Town Diamond Museum (scaife a 3.000 rpm; é o pó de diamante que corta, não a lâmina) · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** nenhum outro arquivo afirma a exclusividade. **Desfecho:** ✅ **Corrigido.**

---

### 🔵 9. "Padrão de mercado" da Sarine sem fonte independente do fabricante

**claim_id:** `DIA-CUT-001`
**Tipo:** sem fonte · **Natureza:** `evidencia_insuficiente`
**Onde:** aula 16 · "1. Planejamento e marcação"
**Estava escrito:** "equipamentos como os da Sarine tornaram-se **padrão**"
**Problema:** o **mecanismo** descrito está confirmado — escaneamento 3D, mapeamento de inclusões em três dimensões, modelagem das pedras possíveis com peso, pureza e valor. O que não se confirmou é a afirmação de **fatia de mercado**: "padrão" aparece na documentação da própria Sarine, que descreve o *Advisor* como *the world standard for rough planning*. Não há dado público de participação de mercado, e há concorrentes. Não é acusação de erro — é afirmação específica apoiada só no fabricante.
**Correção aplicada:** a frase passou a nomear o que é verificável (a linha *Galaxy*, de mapeamento de inclusões, e o *Advisor*, de planejamento, como a referência mais citada da indústria) e a registrar explicitamente que há concorrentes e que a fatia de cada fabricante não é dado público.
**Fonte:** Sarine Technologies, documentação das linhas Galaxy e Advisor (fonte do fabricante, declarada como tal); GIA, *How Are Diamonds Cut and Polished?* · **Nível:** geral
**Confiança:** provável
**Desfecho:** ✅ **Corrigido com ressalva** (afirmação estreitada até a fonte; nada inventado).

---

### 🔵 10. "Em minutos" para o corte a laser: falsa precisão

**claim_id:** `DIA-CUT-002`
**Tipo:** sem fonte · **Natureza:** `evidencia_insuficiente`
**Onde:** aula 16 · "2. Dividir o bruto: clivagem ou serragem"
**Estava escrito:** "Hoje a **serra a laser** faz o mesmo corte **em minutos**"
**Problema:** o resto da alegação está confirmado — disco finíssimo de **bronze fosforoso** carregado de pó de diamante e óleo, e **4 a 8 horas** para atravessar um bruto de 1 ct. O que não se sustenta é a precisão "em minutos": as fontes divergem sobre o tempo absoluto do corte a laser, e há descrições técnicas que falam em horas conforme o equipamento e a seção. Consensuais são a **comparação relativa** e a menor perda de material.
**Correção aplicada:** a precisão não sustentada foi substituída pela comparação relativa ("em uma fração desse tempo e desperdiça menos material") e a faixa bem documentada do disco tradicional (4 a 8 horas para 1 ct) foi explicitada, ganhando um dado que a aula não tinha.
**Fonte:** Caspi, A., *Modern Diamond Cutting and Polishing*, *G&G* 33(2), Summer 1997; descrições técnicas do corte a laser (divergentes quanto ao tempo absoluto) · **Nível:** revisada por pares
**Confiança:** em disputa (quanto ao tempo absoluto)
**Desfecho:** ✅ **Corrigido com ressalva.**

## Verificado e correto nesta rodada

| claim_id | Alegação | Resultado |
|---|---|---|
| `DIA-CUT-003` | Cullinan de 3.106 ct clivado em 1908 pela oficina Asscher, em Amsterdã | ✅ Confirmado — peso, ano, técnica, oficina e cidade conferem. Joseph Asscher clivou em **fevereiro de 1908**, na segunda tentativa; a serragem foi descartada por risco. Precisões acrescentadas ao rodapé, sem alterar o corpo |
| `DIA-CUT-004` | Bruteamento com duas pedras em eixos girando em sentidos opostos, formando o cinturão | ✅ Confirmado, inclusive o aspecto granular e fosco do cinturão bruto, que o laudo distingue do cinturão facetado |

Também conferidos e corretos, sem alegação própria no rodapé: **57 facetas / 58 com culaça facetada** (idêntico à aula 12 do módulo 01 e a `GEM-CUT-002`); **scaife de ferro fundido a ~3.000 rpm**; **bronze fosforoso** na lâmina de serra; a divisão **blocagem → brilhantamento**; a existência de direções duras e moles do **grão**; e a transferência da triagem e da venda do bruto da De Beers de Londres para **Gaborone em 2013**, por acordo firmado em 2011 — data precisada no texto seguindo o mesmo critério de `DIA-PESO-001`.

## Consistência interna — rodada 2

A aula 16 entrou depois da rodada 1, e a verificação foi refeita contra o módulo:

| Valor | Onde | Resultado |
|---|---|---|
| Rendimento do bruto 40–50% | aulas 08 e 16, flashcard `m02-fb096` | ⚠️ **contradição encontrada** (aula 16 dizia 40–55%) → corrigida na aula 16 |
| Grau de lapidação como tabela de combinações | aulas 07 e 16 | ⚠️ **contradição encontrada** ("projeto fechado desde 1919") → corrigida na aula 16 |
| Só diamante corta diamante | aula 16, abertura vs. seções 2 e 3 | ⚠️ **contradição interna à própria aula** → corrigida |
| 57–58 facetas | aula 16, aula 12 do módulo 01, `m01-fb066`, questionário parcial 2 do módulo 01 | ✅ idêntico |
| Tamanhos mágicos e o degrau de 1 ct | aulas 08 e 16 | ✅ coerente; o exemplo trabalhado da a16 usa o degrau corretamente |
| Clivagem octaédrica | aulas 01 e 16 | ✅ idêntico |

## Correções aplicadas — rodada 2

**Aplicadas em:** 2026-08-28

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `DIA-CUT-008` | 🟠 | Corrigido | `02-diamantes-aula-16-lapidacao-do-bruto-ao-polido.md` |
| `DIA-CUT-007` | 🟠 | Corrigido | `02-diamantes-aula-16-lapidacao-do-bruto-ao-polido.md` |
| `DIA-CUT-006` | 🟠 | Corrigido | `02-diamantes-aula-16-lapidacao-do-bruto-ao-polido.md` |
| `DIA-CUT-005` | 🟠 | Corrigido | `02-diamantes-aula-16-lapidacao-do-bruto-ao-polido.md` |
| `DIA-CUT-001` | 🔵 | Corrigido com ressalva | `02-diamantes-aula-16-lapidacao-do-bruto-ao-polido.md` |
| `DIA-CUT-002` | 🔵 | Corrigido com ressalva | `02-diamantes-aula-16-lapidacao-do-bruto-ao-polido.md` |
| `DIA-CUT-003` · `DIA-CUT-004` | — | ✅ Verificados e corretos | — (rodapé enriquecido) |

**Um único arquivo de conteúdo foi tocado.** Todas as três contradições foram resolvidas **em favor do material já auditado**, e por isso nem a aula 07, nem a aula 08, nem o flashcard `m02-fb096`, nem o módulo 01 precisaram de edição.

**Propagação:** **não necessária**, e verificada por busca em todo o curso, não presumida. Tolkowsky e "1919" não aparecem em nenhum outro arquivo; o rendimento aparece na aula 08 e em `m02-fb096` já com 40–50%, valor para o qual a aula 16 foi alinhada; a fatia da Índia aparece na aula 22 do módulo 01 apenas qualitativamente, sem número; a contagem de facetas não mudou. **O `oa16` continua sem questão e sem flashcard** — nenhum material derivado existe para propagar.

**Migração de Anki a fazer:** nenhuma. Nenhum card foi alterado.

**Pendências:** nenhuma da auditoria. Fora do escopo factual, uma observação encaminhada à revisão didática: a aula 16 usa **culaça** e **cinturão** onde a aula 12 do módulo 01, que ela declara como pré-requisito de anatomia, usa **cúlete** e **cintura (rondiz)**.

## Fontes consultadas na rodada 2

- **Normativas e setoriais:** GJEPC, *India Centre* (fatias da Índia por peça, peso e valor) · IBEF e Invest India (corroboração) · GIA, *4Cs Cut* e *How Are Diamonds Cut and Polished?* · De Beers / Governo de Botsuana (acordo de 2011, mudança para Gaborone em 2013).
- **Revisadas por pares:** Caspi, A., *Modern Diamond Cutting and Polishing*, *G&G* 33(2), Summer 1997 · Moses, T. M. et al., *A Foundation for Grading the Overall Cut Quality of Round Brilliant Cut Diamonds*, *G&G* Fall 2004 · literatura de ablação de diamante por laser pulsado, grafitização sp³→sp² e sublimação (2024–2025).
- **Bases de referência e históricas:** Royal Collection Trust, *The Crown Jewels* (clivagem do Cullinan, 1908) · Royal Asscher · Cape Town Diamond Museum, *Diamond Cutting and Polishing* e *History of Marcel Tolkowsky* · Tolkowsky, *Diamond Design* (1919).
- **Do fabricante, declarada como tal:** Sarine Technologies, documentação Galaxy e Advisor.

> [!note] Divergência conhecida, não introduzida aqui
> Os `claim_id` desta rodada seguem o padrão de **três segmentos** do curso (`DIA-CUT-001`), e não os quatro que o `audit.schema.json` do plugin exige. É a divergência já registrada como pendência 8 em `_contexto.md`, herdada do curso de origem. Manter o padrão do curso foi decisão deliberada: renomear só as alegações novas criaria uma segunda divergência dentro do mesmo módulo.
