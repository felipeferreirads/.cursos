# Auditoria científica: Módulo 03 — Gemas coradas

**Auditado em:** 2026-08-25 (rodada 1, aulas 01–16) · 2026-08-28 (rodada 3, aulas 18–19; rodada 4, aulas 20–21)
**Material:** `03-gemas-coradas/` — hoje **21 aulas** e o hub do módulo; **16** quando a rodada 1 correu. As aulas 01–07 foram escritas em sessão anterior; as aulas 08–16 e o hub, nesta retomada. Todas são texto de primeira redação; nenhuma foi migrada de outro curso.
**Escopo desta partição:** a auditoria original de 2026-08-25 cobriu o módulo único `03-gemas-coradas-perolas`, de 21 aulas. Em 2026-08-26 aquele módulo foi dividido em `03-gemas-coradas` (aulas 01–16) e `04-perolas` (ex-aulas 17–21). Este relatório ficou com os itens das aulas 01–16; os das aulas biológicas estão em [[04-perolas-auditoria|auditoria do módulo 04]]. Nada foi reauditado, criado ou descartado na divisão.
**Segunda repartição, 2026-08-27:** a **aula 13** foi dividida em parte 1 (zircão e tanzanita, `oa13`) e parte 2 (espodumênio e iolita, objetivo novo `oa17`), e as antigas aulas 14, 15 e 16 passaram a 15, 16 e 17. As **12 alegações** da antiga aula 13 foram **particionadas por espécie**: 7 (`ZIR-*`, `TAN-*`) ficaram na parte 1 e 5 (`ESD-*`, `IOL-*`) foram para a parte 2. Nada foi reauditado, criado, alterado ou descartado; o veredito e os totais deste relatório continuam válidos. Ver o bloco `lesson_split` em `03-gemas-coradas-auditoria.json`.
**Modo:** audit-and-fix
**Profundidade:** full
**Escopo:** sistema de graduação de cor do GIA; fatores de valor de gema corada; tipos de pureza; propriedades diagnósticas de coríndon, berilo, turmalina, granada, espinélio, crisoberilo, topázio, peridoto, quartzo cristalino e microcristalino, zircão, tanzanita, espodumênio e iolita; mecanismos, estabilidade e detectabilidade de tratamentos; rotas de síntese e suas assinaturas; imitações, vidros e materiais compostos; **consistência numérica interna entre as aulas do módulo** e entre elas e os módulos 01 e 02.
**Veredito final:** **Aprovado** (rodadas 1, 3 e 4). Todas as 21 aulas do módulo estão auditadas.

> [!info] Ordem de execução
> Esta auditoria rodou **antes** da geração do questionário e do baralho, conforme a ordem adotada no curso: auditar → corrigir → só então avaliar e cardificar. Nenhum material derivado precisou de propagação, porque nenhum existia quando as correções foram aplicadas.

## Resumo

**Rodada 1 (2026-08-25, aulas 01–16):** 🔴 0 · 🟠 2 · 🟡 0 · 🔵 1 · ⚪ 2. 153 alegações registradas, 150 corretas. Os três achados 🟠/🔵 corrigidos na mesma rodada.

**Rodada 3 (2026-08-28, aulas 18–19):** 🔴 0 · 🟠 2 · 🟡 2 · 🔵 0 · ⚪ 0. 21 alegações registradas, 17 corretas. Os quatro achados corrigidos na mesma rodada (detalhe na seção "Rodada 3" abaixo).

**Rodada 4 (2026-08-28, aulas 20–21):** 🔴 0 · 🟠 0 · 🟡 0 · 🔵 0 · ⚪ 0. 16 alegações `PRO-*` registradas, **16 corretas — nenhum achado**. Datas de descoberta de depósito, contexto geológico e a metodológica `PRO-MET-001` confirmados contra GIA *G&G*, Hughes e CITES.

**Nenhum achado permanece aberto.** As controvérsias da rodada 1 e a da andesina (rodada 3) foram tratadas na redação sob a regra LC-08 e **não** são pendências. **Todas as 21 aulas do módulo estão auditadas.**

Um padrão merece registro: **nenhum achado foi um erro de propriedade física** — os valores de índice de refração, birrefringência, densidade e dureza das quatorze espécies conferiram com as fontes de referência. Os problemas apareceram nas margens: uma faixa de propriedade apresentada sem o contexto de outro módulo, uma densidade de exemplo destoando do valor de referência do curso, e uma atribuição de mecanismo sem a fonte primária. **Dois dos três achados são de coerência, não de fato** — o que era esperado num módulo cujo risco principal é a quantidade de números repetidos entre aulas.

## Achados

### 🟠 1. A faixa de índice de refração da granada contradizia aparentemente o módulo 01

**claim_id:** `GRA-EST-003` (achado de **coerência entre módulos**)
**Tipo:** impreciso (inconsistência aparente com material já publicado) · **Natureza:** `inconsistencia_interna`
**Onde:** aula 08 · "Por que a tabela de propriedades é uma faixa" — confrontada com `01-gemologia-geral-aula-04-refratometro-e-polariscopio.md`
**Estava escrito:** aula 08 do módulo 03: "Índice de refração | ~**1,71 a 1,89**". Módulo 01, aula 04: "granada (isotrópica, **1,714–1,830**)".
**Problema:** os dois números estão corretos e descrevem coisas diferentes, mas o aluno encontra o segundo antes do primeiro e não tem como saber disso. O intervalo até 1,830 cobre a **série piralspita**, que responde pela quase totalidade dos casos de bancada; o teto de 1,89 só se alcança na série **ugrandita**, e na prática significa **demantoide**. Sem essa explicação, a aula 08 parece corrigir silenciosamente o módulo 01 — ou pior, parece um erro de um dos dois.
**Correção aplicada:** acrescentado, imediatamente antes da tabela de propriedades da aula 08, um parágrafo que cita o valor do módulo 01, explica que ele cobre a piralspita e declara que "as duas informações são compatíveis; a segunda é a versão completa da primeira". Nenhum número foi alterado em nenhum dos dois módulos.
**Fonte:** GIA *Gem Encyclopedia*; Webster, *Gems*; Deer, Howie & Zussman — faixas por série · **Nível:** referência de área
**Confiança:** confirmado
**Também aparece em:** `01-gemologia-geral-aula-04-refratometro-e-polariscopio.md` (não alterado — o valor lá está correto para o escopo daquela aula).
**Desfecho:** ✅ **Corrigido.**

---

### 🟠 2. Densidade da esmeralda no exemplo trabalhado destoava do valor de referência do módulo

**claim_id:** — (texto de exemplo, sem alegação auditável associada)
**Tipo:** impreciso (inconsistência numérica interna) · **Natureza:** `inconsistencia_interna`
**Onde:** aula 16 · "Exemplo trabalhado", passo 1 *(era a aula 15 até a renumeração de 2026-08-27)*
**Estava escrito:** "Densidade: **2,71**. Dentro da faixa natural."
**Problema:** a aula 06 estabelece 2,72 como o valor de referência da esmeralda, e o repete em três lugares (tabela de propriedades, tabela comparativa natural × sintética e exemplo trabalhado). Um exemplo posterior usando 2,71 é defensável fisicamente — a faixa do berilo é 2,67–2,90 — mas obriga o aluno a decidir qual número memorizar, sem nenhum ganho didático em troca. Em módulo cujo conteúdo é largamente tabelar, a coerência do número repetido vale mais que a variação realista.
**Correção aplicada:** "Densidade: **2,72**."
**Fonte:** aula 06 do próprio módulo; GIA *Gem Encyclopedia* · **Nível:** interno + referência de área
**Confiança:** confirmado
**Também aparece em:** nenhum outro ponto do módulo usava 2,71.
**Desfecho:** ✅ **Corrigido.**

---

### 🔵 3. A causa da cor do quartzo rosa maciço estava sem fonte primária e sem a ressalva do próprio trabalho

**claim_id:** `QTZ-VAR-003`
**Tipo:** sem fonte (atribuição a autores, sem referência verificável, e afirmação mais forte que a da fonte) · **Natureza:** `fonte_insuficiente`
**Onde:** aula 11 · tabela de variedades e seção "O quartzo rosa tem uma explicação em duas camadas"; bloco `alegacoes_auditaveis` e "Fontes consultadas"
**Estava escrito:** fonte declarada como "Ma, C. & Rossman, G. R., e trabalhos correlatos"; alegação afirmando "inclusões fibrosas microscópicas de um mineral do tipo dumortierita".
**Problema:** dois defeitos. (i) A referência estava incompleta e com a autoria trocada de ordem: o trabalho é **Goreva, J. S., Ma, C. & Rossman, G. R., "Fibrous nanoinclusions in massive rose quartz: The origin of rose coloration", *American Mineralogist* 86 (2001), 466–472** — uma referência verificável que a alegação não trazia. (ii) A alegação era mais assertiva do que a fonte: os próprios autores registram que o melhor equivalente pelos padrões de difração de raios X é a **dumortierita**, mas que os espectros de FTIR e Raman **não coincidem exatamente** com os da espécie, de modo que a nanofase pode não ser dumortierita e sim material aparentado. O corpo da aula já dizia "do tipo dumortierita", corretamente; a alegação auditável é que estava mais dura que o corpo.
**Correção aplicada:** a referência foi completada em "Fontes consultadas" e a alegação `QTZ-VAR-003` foi reescrita para incorporar explicitamente a ressalva dos autores. O corpo da aula não precisou de alteração.
**Fonte:** Goreva, Ma & Rossman (2001), *American Mineralogist* 86, 466–472 · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** nenhum outro arquivo.
**Desfecho:** ✅ **Corrigido.**

---

## Controvérsias declaradas (⚪ — verificadas, não são pendências)

Duas passagens do módulo declaram explicitamente um debate aberto em vez de arbitrá-lo, conforme a regra LC-08. As duas foram verificadas como controvérsias reais e **corretamente representadas**. As outras três controvérsias da auditoria original são das aulas biológicas e estão em [[04-perolas-auditoria|auditoria do módulo 04]].

| claim_id | Aula | Do que se trata | Situação na literatura |
|---|---|---|---|
| `CAL-VAR-003` | 12 | Origem do **olho-de-tigre**: pseudomorfose de sílica sobre crocidolita *versus* crescimento simultâneo em fraturas que abrem e selam | Debate aberto desde Heaney & Fisher, *Geology* 31 (2003); a aula apresenta os dois modelos sem escolher |
| `IOL-HIST-001` | 14 (era 13 até 2026-08-27) | A *sólarsteinn* das sagas nórdicas seria **iolita**? | As fontes não identificam o mineral; a literatura moderna propõe a calcita da Islândia. A aula trata a atribuição comercial à iolita como não sustentada, o que é a posição correta |

## Verificações que passaram, e que valeram o esforço

Registro do que foi checado e **não** virou achado, para que uma auditoria futura não refaça o trabalho:

- **Propriedades físicas das quatorze espécies coradas.** Índice de refração, birrefringência, caráter óptico, densidade relativa, dureza e clivagem de coríndon, berilo, turmalina, granada, espinélio, crisoberilo, topázio, peridoto, quartzo, calcedônia, zircão, zoisita, espodumênio e cordierita conferem com GIA, Mindat e Webster. **Nenhuma divergência.**
- **Sinal óptico do quartzo.** Confirmado **uniaxial positivo** — a aula 11 o usa como critério de separação contra coríndon, berilo e turmalina, todos negativos, e o critério é válido.
- **Sobreposição iolita × quartzo.** Confirmadas as faixas quase coincidentes de IR e densidade, e confirmado que o caráter óptico (biaxial negativa × uniaxial positivo) e o pleocroísmo as separam. É o eixo do exemplo trabalhado da aula 14 (a aula 13 original, até a divisão de 2026-08-27), e ele se sustenta.
- **Coerência interna dos números repetidos.** Coríndon (1,762–1,770 · 0,008 · uniaxial negativo · 4,00), berilo (1,577–1,583 · 2,72), turmalina (1,624–1,644 · 0,018–0,020), quartzo (1,544–1,553 · 0,009 · 2,65), jadeíta (1,66 · 3,34) e nefrita (1,61 · 2,95) aparecem de forma **idêntica** em todas as aulas dos módulos 01 e 03 em que são citados, após a correção do achado 🟠 2.

## Achados deferidos (não bloqueantes)

Um ponto deste módulo foi examinado, considerado **defensável como está** e registrado para revisão futura, sem correção nesta rodada. A outra nota deferida da auditoria original é da aula de biologia da pérola e ficou no módulo 04.

| id | Aula | Questão | Por que fica assim |
|---|---|---|---|
| `GEM-PER-COLONIA-001` | 10 | A atribuição das pedras do relicário dos Reis Magos, em Colônia, a **peridoto** é repetida com frequência na literatura gemológica, mas a documentação primária é fina | A aula já apresenta a afirmação de forma qualificada ("parte das 'esmeraldas' da Antiguidade e do medievo são peridoto, incluindo…"), e o ponto é ilustrativo, não estrutural. Vale confirmar com fonte museológica primária numa rodada futura |

## Método

- **Alegações auditáveis** extraídas dos blocos `alegacoes_auditaveis` em comentário HTML no rodapé das aulas. A rodada de 2026-08-25 registrou **204** alegações nas 21 aulas do módulo então único; **153** delas são das aulas que ficaram neste módulo — distribuídas hoje por 17 aulas, depois da divisão da aula 13 em 2026-08-27.
- **Priorização por risco declarado:** alegações marcadas `numero` e `nomenclatura` foram verificadas uma a uma contra fonte; as marcadas `mecanismo` foram verificadas quanto à direção causal; as marcadas `interpretacao` e `controverso` foram verificadas quanto à **calibragem** — se a afirmação é tão forte quanto a evidência sustenta, e não mais.
- **Fontes de referência, por ordem de precedência:** literatura revisada por pares (*American Mineralogist*, *Geology*, *Science*) → normas e convenções (CITES, CIBJO, LMHC, FTC) → referências de área (GIA *Gem Encyclopedia* e *Gems & Gemology*, Gem-A, Webster, Strack, Nassau, Gübelin & Koivula, Espinoza & Mann) → bases de dados minerais (Mindat, IMA-CNMNC).
- **Verificação cruzada entre módulos** executada sobre os valores numéricos repetidos, contra os módulos 01 e 02 do curso.
- **Divergência conhecida e herdada:** o formato de `claim_id` deste curso usa três segmentos (`GRA-EST-003`), enquanto o `audit.schema.json` do plugin exige quatro. É a mesma divergência já registrada em `_contexto.md` para os módulos 01 e 02, e o módulo 03 seguiu deliberadamente a convenção do curso em vez de introduzir um terceiro padrão. A exceção é o id deferido acima, que nasceu nesta auditoria e já segue o formato de quatro segmentos.

## Rodada 3 — 2026-08-28 (aulas 18 e 19, gemas de colecionador)

As aulas 18 e 19 foram escritas em 2026-08-28 para fechar a lacuna aprovada das gemas coradas de colecionador e inseridas ao fim do módulo. Esta rodada auditou as **21 alegações novas** (`SFE-`, `FDS-`, `DAN-`, `APA-`, `FLU-` na aula 18; `CIA-`, `DIO-`, `SCP-`, `BRZ-`, `OUT-` na aula 19), modo audit-and-fix, profundidade full, verificação contra GIA *Gem Encyclopedia*, Mindat, IMA-CNMNC, Webster e literatura primária.

**Resultado: 17 corretas · 🔴 0 · 🟠 2 · 🟡 2 · 🔵 0 · ⚪ 0.** Os quatro achados foram corrigidos nesta rodada. Como não há questionário nem flashcards para `oa18`/`oa19`, não houve propagação para material derivado.

### 🟠 1. Direção da tenebrescência da hackmanita invertida

**claim_id:** `OUT-FEN-001` · **Tipo:** erro de mecanismo
**Onde:** aula 19 · "As demais, em uma frase cada" e "Erros comuns"
**Estava escrito:** "passa de incolor/branco a rosa ou violeta sob luz UV **ou solar**, e volta no escuro"
**Problema:** a hackmanita ganha ou aprofunda a cor sob **UV** e **no escuro**, e **desbota** sob luz solar/visível forte — a luz solar é o que apaga a cor, não o que a produz. O texto tinha a direção solar ao contrário e dizia que a cor some no escuro, quando é no escuro que ela se regenera.
**Correção:** reescrito para "sob luz ultravioleta ou guardada no escuro ganha ou aprofunda uma cor rosa a violeta, e sob luz solar ou visível forte desbota para branco-acinzentado". O item de "Erros comuns" foi ajustado no mesmo sentido.
**Fonte:** The Fluorescent Mineral Society, *What is Tenebrescence?*; Gemworld International, *Gem Focus* (out. 2023) — "pink to violet hackmanite will bleach under sunlight". **Confiança:** confirmado.

### 🟠 2. Faixa de birrefringência da apatita estreita demais

**claim_id:** `APA-EST-001` · **Tipo:** valor fora da faixa da fonte normativa
**Onde:** aula 18 · tabela da apatita e recap
**Estava escrito:** birrefringência "~0,002–0,004"
**Problema:** a ficha da GIA dá 0,002–0,008 para a apatita gema; 0,004 como teto corta material real.
**Correção:** "~0,002–0,008 (baixa; muitas vezes ~0,003)". O ponto pedagógico (birrefringência baixa) fica intacto.
**Fonte:** GIA, *Apatite* (Gem Encyclopedia / Gemopedia). **Confiança:** confirmado.

### 🟡 3. Fórmula antiga da taaffeíta

**claim_id:** `OUT-FEN-001` · **Tipo:** nomenclatura desatualizada
**Onde:** aula 19 · "As demais, em uma frase cada"
**Estava escrito:** "Taaffeíta — BeMgAl₄O₈"
**Problema:** a fórmula aceita é **Mg₃Al₈BeO₁₆**; a IMA-CNMNC renomeou o mineral **magnesiotaaffeíta-2N′2S** em 2002 (Armbruster et al.). "Taaffeíta" segue como nome de comércio.
**Correção:** "Mg₃Al₈BeO₁₆ (a IMA a renomeou magnesiotaaffeíta-2N′2S em 2002; o comércio mantém 'taaffeíta')". O nome comercial foi preservado.
**Fonte:** Armbruster et al. (2002), *Revised nomenclature of högbomite, nigerite, and taaffeite minerals*; Mindat. **Confiança:** confirmado.

### 🟡 4. Descrição da brazilianita atribuída ao autor errado

**claim_id:** `BRZ-EST-001` / `BRZ-HIST-001` · **Tipo:** citação incorreta (só no rodapé; corpo da aula OK)
**Onde:** aula 19 · campos `source` das alegações e "Fontes consultadas"
**Estava escrito:** "Frondel, *American Mineralogist* 30:572 (1945)"
**Problema:** a descrição original da brazilianita é de **Pough & Henderson**, *American Mineralogist* 30:572–582 (1945). Frondel é outro mineralogista. O corpo da aula só diz "descrita em 1945", que está certo — o erro estava na citação.
**Correção:** citação trocada para Pough & Henderson (1945) nos três lugares.
**Fonte:** *American Mineralogist* 30:572–582 (1945); Mindat, brazilianite. **Confiança:** confirmado.

### Verificado e correto (rodada 3)

Esfeno (`SFE-EST-001`, `SFE-DISP-001` — IR 1,84–2,11, dispersão 0,051 > diamante, dureza 5–5,5, confirmados contra GIA e IGS); feldspatos-gema (`FDS-EST-001`, `FDS-VAR-001` — faixa de IR ~1,52–1,57 e clivagens ~90° batem com oligoclásio/labradorita/ortoclásio); **andesina** (`FDS-AND-001` — a controvérsia da difusão de cobre não divulgada está redigida como pergunta aberta, exatamente como a literatura a trata; GIA *G&G* Winter 2022); danburita (`DAN-EST-001`, `DAN-MERC-001` — IR 1,630–1,636, DR ~3,0, dureza 7–7,5); fluorita (`FLU-EST-001`, `FLU-USO-001` — IR 1,434, dureza 4, clivagem octaédrica perfeita em 4 direções, Blue John); cianita (`CIA-EST-001`, `CIA-DUR-001` — IR 1,712–1,734, dureza direcional 4–5 / 6,5–7); diopsídio (`DIO-EST-001`, `DIO-VAR-001` — IR 1,675–1,701, cromo-diopsídio comercial da Sibéria a partir de 1988, escurece acima de ~1–2 ct); escapolita (`SCP-EST-001`, `SCP-VAR-001` — série marialita–meionita, IR 1,540–1,580, uniaxial negativa); brazilianita (valores IR/DR/dureza, tipo Minas Gerais, cor não tratada); petalita e pollucita (`OUT-EST-001`); sinhalita (`OUT-SIN-001` — MgAlBO₄, reconhecida como espécie em 1952, ex-"peridoto marrom"); kornerupina.

## Rodada 4 — 2026-08-28 (aulas 20 e 21, procedências)

As aulas 20 e 21 foram escritas em 2026-08-28 para fechar a lacuna aprovada da sistemática de procedências mundiais. Esta rodada auditou as **16 alegações `PRO-*`** — histórico de descoberta de depósitos, contexto geológico e a metodológica `PRO-MET-001` — contra GIA *Gems & Gemology*, Hughes (*Ruby & Sapphire*), Giuliani et al. (*Gemstones: Genesis, Deposits and Mining*), CITES e literatura de depósito.

**Resultado: 16 corretas · 🔴 0 · 🟠 0 · 🟡 0 · 🔵 0 · ⚪ 0. Nenhum achado.** Verificado item a item:

- **`PRO-MMR-001/002/003`** — Mogok em mármore pobre em ferro, fluorescência forte, *pigeon's blood*; Mong Hsu no mercado por 1992 com núcleo azul removido por aquecimento; restrições de importação de rubi/jade birmanês mudando desde 2003 e reendurecendo pós-2021. Confirmados (GIA *G&G* 1995, 2000, 2014; Hughes).
- **`PRO-LKA-001/002`** — *illam* aluvionar em Ratnapura/Elahera/Balangoda, paleta completa de safira + padparadscha + crisoberilo/alexandrita/sinhalita; *geuda* leitoso valorizado a partir dos anos 1970 pelo aquecimento que dissolve o rutilo. Confirmados.
- **`PRO-KSH-001`** — Caxemira acima de 4.000 m (Padar/Zaskar, ~4.500 m), lavrada sobretudo **1881–fim da década de 1880** (pico 1882–1887), azul aveludado por espalhamento, prêmio histórico e de escassez, determinação de origem a mais disputada. Confirmado (GIA *G&G* 2015).
- **`PRO-AFG-001`** — Panjshir esmeralda em veio hidrotermal carbonático; Jegdalek rubi/espinélio em mármore (tipo Mogok); norte do Paquistão rubi/esmeralda/água-marinha/topázio rosa de Katlang/peridoto de Sapat. Confirmado.
- **`PRO-THA-001`** — Chanthaburi–Trat e Pailin ligados a basalto rico em ferro (rubi escuro sem fluorescência); produção local reduzida; Chanthaburi maior centro mundial de corte e tratamento térmico, recebendo bruto de Moçambique/Madagascar/Tanzânia. Confirmado (Hughes).
- **`PRO-MOZ-001`** — Montepuez descoberto **maio de 2009**, rubi em **anfibolito** (não mármore), ferro intermediário, maior fonte mundial em volume e qualidade. Confirmado (GIA *G&G* Spring 2015; Summer 2019).
- **`PRO-MDG-001`** — Ilakaka descoberto **1998**, depósito secundário, safira de toda a paleta próxima da cingalesa; par Sri Lanka × Madagascar dos mais difíceis. Confirmado (GIA *G&G* 2001).
- **`PRO-TZA-001/002`** — Merelani única fonte de tanzanita; tsavorita descrita na Tanzânia (1967) e no Quênia (1970) por Campbell Bridges; Mahenge espinélio 2007; Winza rubi 2007. Confirmados (GIA *G&G* 2009).
- **`PRO-COL-001`** — Muzo/Chivor/Coscuez em folhelho negro carbonático, inclusão trifásica com cristal cúbico de halita como indicador **forte mas não conclusivo** (ocorre também no Afeganistão e na China). Confirmado.
- **`PRO-ZMB-001`** — Kafubu/Kagem em xisto com pegmatito, verde mais azulado por ferro, Kagem maior mina de esmeralda do mundo, leilão em canal formal. Confirmado (GIA *G&G* 2005).
- **`PRO-AUS-001`** — NSW e Queensland, safira de basalto rica em ferro; Lightning Ridge (opala negra), Coober Pedy, Andamooka. Confirmado.
- **`PRO-MET-001`** — as três camadas de evidência (inclusões + química de traços por LA-ICP-MS + espectro), comparação a coleção de referência, e os quatro limites (é comparação não medida; depósitos novos degradam a base; tratamento apaga evidência; laboratórios divergem). Calibragem correta contra LMHC e GIA — a afirmação não é mais forte que a evidência sustenta.

## Rodada — 2026-08-28 (seção "Casco de tartaruga", registrada na auditoria do módulo 04)

A seção de casco de tartaruga foi acrescentada à aula 05 do **módulo 04**; sua auditoria está no relatório daquele módulo. Registro cruzado aqui só para completar o inventário das aulas novas de 2026-08-28: 4 alegações `TRT-*`, **0 achado**.

## Correções aplicadas

### Rodada 1 — 2026-08-25

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `GRA-EST-003` | 🟠 | Corrigido | 03-gemas-coradas-aula-08-granadas-o-grupo-e-as-series.md |
| — (exemplo trabalhado) | 🟠 | Corrigido | 03-gemas-coradas-aula-16-rotas-de-sintese-e-suas-assinaturas.md (era a aula 15 até 2026-08-27) |
| `QTZ-VAR-003` | 🔵 | Corrigido | 03-gemas-coradas-aula-11-quartzo-cristalino-variedades-coradas.md |

Como o questionário e o baralho deste módulo foram gerados **depois** desta rodada, não houve propagação para material derivado com valores antigos. Nem a divisão do módulo em 2026-08-26 nem a divisão da aula 13 em 2026-08-27 alteraram texto de espécie.

### Rodada 3 — 2026-08-28 (aulas 18 e 19)

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `OUT-FEN-001` | 🟠 | Corrigido (direção da tenebrescência) | 03-gemas-coradas-aula-19-…-brazilianita-e-outras.md |
| `APA-EST-001` | 🟠 | Corrigido (birrefringência 0,002–0,008) | 03-gemas-coradas-aula-18-…-apatita-e-fluorita.md |
| `OUT-FEN-001` | 🟡 | Corrigido (fórmula Mg₃Al₈BeO₁₆ / magnesiotaaffeíta-2N′2S) | 03-gemas-coradas-aula-19-…-brazilianita-e-outras.md |
| `BRZ-EST-001` / `BRZ-HIST-001` | 🟡 | Corrigido (citação → Pough & Henderson 1945) | 03-gemas-coradas-aula-19-…-brazilianita-e-outras.md |

**Propagação:** nenhuma — `oa18` e `oa19` ainda não têm questão nem flashcard. Nenhum arquivo antigo do módulo foi tocado; nada a reimportar no Anki.

### Rodada 4 — 2026-08-28 (aulas 20 e 21)

Nenhuma correção: as 16 alegações `PRO-*` passaram limpas. Únicas edições de arquivo foram as flags `pendencias.auditoria_cientifica` dos rodapés das aulas 20 e 21 (`true → false`).

**Pendências:** as aulas 18 a 21 seguem sem revisão didática, sem questão e sem flashcard (fora do escopo destas rodadas).

## Navegação

- Módulo: [[03-gemas-coradas-modulo|Módulo 03 — Gemas coradas]]
- Auditoria do módulo irmão: [[04-perolas-auditoria|Módulo 04 — Pérolas e gemas orgânicas]]
- Revisão didática: [[03-gemas-coradas-revisao-didatica|relatório]]
- Contexto do curso: [[_contexto|decisões duradouras]]
