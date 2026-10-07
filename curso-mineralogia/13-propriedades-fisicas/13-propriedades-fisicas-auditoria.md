# Auditoria científica: Módulo 13 — Propriedades físicas e identificação macroscópica

**Auditado em:** 2026-10-07
**Material:** `curso-mineralogia/13-propriedades-fisicas/` — as 9 aulas (`-aula-01` a `-aula-09`) e as figuras 1 a 5 (lidas pelo código SVG); cruzamento com o módulo 01 (aula 05: clivagem e densidade de ligações), o módulo 02 (aula 04: número de espécies IMA), o módulo 05 (aula 03: notação da clivagem da calcita), o módulo 06 (aula 04: celas da fluorita e da calcita), o módulo 10 (aulas 01, 04 e 05: polimorfos da sílica, metamictização), o módulo 11 (aula 04: clivagem dos inossilicatos) e o módulo 12 (aula 01 e auditoria: pirrotita, partição do coríndon)
**Modo:** audit-and-fix
**Profundidade:** full, com recálculo em Python dos ângulos de clivagem (cúbicos e calcita, nas duas celas), da densidade relativa e de sua incerteza, da densidade calculada da fluorita, da composição da olivina por aditividade de volumes molares (e por interpolação linear), das razões de Rosiwal e da taxa de dose pelo inverso do quadrado
**Escopo:** as 60 alegações dos rodapés e as afirmações de risco do corpo: hábito e agregados; clivagem, partição e fratura; Mohs, Rosiwal, anisotropia e tenacidade; densidade medida e calculada; brilho e diafaneidade; cor e traço; magnetismo, luminescência e radioatividade; piezo e piroeletricidade, ácido, solubilidade e sabor; chave macroscópica e grau de confiança; as cinco figuras. Questionário e baralho ainda não existem (não foram gerados nesta etapa).
**Veredito:** Requer correção → **correções aplicadas; estado final: Aprovado** (nenhum achado aberto)
**Terceira passagem:** 2026-10-07, sobre os questionários (parcial 1, parcial 2 e final; 38 questões) e o baralho (179 Basic + 7 Cloze); 🟠 8 corrigidos (achados 21 a 28), dois deles com ajuste mínimo nas aulas 07 e 08; estado final mantido em Aprovado. Ver "Auditoria de questionários e baralho" no fim.

## Resumo

🔴 1 erro · 🟠 17 imprecisões · 🟡 0 desatualizados · 🔵 0 sem fonte · ⚪ 1 controverso (primeira passagem)
**Acumulado das três passagens:** 🔴 1 · 🟠 26 · 🟡 0 · 🔵 0 · ⚪ 1 (28 achados, todos corrigidos); 68 alegações verificadas e corretas (55 + 8 + 5), igual ao manifesto `.json`.
Verificadas e corretas: 55 das 60 alegações dos rodapés (as outras 5 viraram achados), todas as contas e as figuras 3 e 5. As figuras 1, 2 e 4 tinham erro conceitual (achados 1, 5 e 12).

Os pontos que o autor marcou "a conferir" (densidades, durezas, traços, magnetismo, luminescência) passaram quase todos no *Handbook of Mineralogy*; as exceções foram a cianita (o HoM dá 5,5 ao longo, e não 4,5 a 5) e a galena (7,58, e não ~7,5). O resto dos achados veio do corpo e das figuras: o cobre nativo "amarelo", a escala de Rosiwal apresentada como se as tabelas concordassem, duas inconsistências com módulos já fechados (partição do coríndon, módulo 12; polimorfos da sílica, módulo 10), exemplos trabalhados com enunciado incoerente (cristais "pretos" que eram pirita; pirrotita "preta"; limite de dureza tirado da resposta) e três figuras que desenhavam o conceito errado (lobo botrioidal como cristal único, romboedro como caixa, raios de luz que violam a lei da reflexão).

**Contas conferidas (Python, 2026-10-07):**

| O quê | Resultado | Onde |
|---|---|---|
| (111)∧(11-1) no cubo | 70,529° entre normais; 109,471° diedro (texto 70,53° / 109,47° ✔) | a02 |
| (110)∧(1-10) e (110)∧(101) | 90,00° e 60,00° ✔ | a02 |
| Calcita (104)∧(-114), cela a = 4,9896, c = 17,0610 Å | 74,944° entre normais; 105,056° diedro ✔ (achado 3 só na redação) | a02 |
| Calcita (10-11)∧(-1101), cela morfológica (c/4) | 74,944°, igual: mesmo plano nas duas notações ✔ | a02 |
| Ângulo plano da face do romboedro de clivagem | 78,10° / 101,90° (usado para redesenhar a figura 2) | fig-02 |
| G = 47,7/(47,7 − 32,7); extremos com ±0,1 g | 3,180; 3,145 e 3,216 → 3,18 ± 0,04 ✔ | a04 |
| M(Mg₂SiO₄), M(Fe₂SiO₄), diferença | 140,69; 203,77; 63,08 g/mol ✔ | a04 |
| V molar Fo (3,275) e Fa (4,39; HoM 4,392) | 42,96 e 46,42 (46,40) cm³/mol ✔ | a04 |
| x(Fa) para ρ = 3,60, volumes aditivos | 0,2757 (0,2753 com 4,392) → Fo72Fa28 ✔; a aproximação está **declarada** no texto ("admitindo que os volumes molares se somam (aproximação de solução ideal)") ✔ | a04 |
| x(Fa) por interpolação linear da densidade | 0,2915 → 0,29 ✔ | a04 |
| dρ/dx em x = 0,28; erro de 0,02 g/cm³ | 1,153 g/cm³ por unidade de x → 1,7 ponto percentual ("alguns pontos percentuais" ✔) | a04 |
| ρ fluorita = 4 × 78,075 / (0,6022 × 163,0); V = 5,4626³ | 3,182 g/cm³; 163,00 Å³ ✔ | a04 |
| Razões de Rosiwal | 100/0,03 = 3 333; 120/0,03 = 4 000; 5/4,5 = 1,11; 175/100 = 1,75; 175/120 = 1,46; 140 000/1 000 = 140 | a03 |
| Inverso do quadrado: (4,0 − 0,10) × (5/20)² | 0,244 µSv/h ✔ | a07 |

> [!note] Limite da verificação nesta sessão
> Os verbetes do *Handbook of Mineralogy* (Mineralogical Society of America) foram baixados e lidos diretamente dos PDFs para: acantita, aragonita, augita, barita, calcita, calcopirita, cromita, cobre, coríndon, cuprita, diamante, dolomita, faialita, fluorita, forsterita, galena, goethita, ouro, grafite, gipsita, halita, hematita, magnesio-hornblenda, cianita, magnesita, magnetita, marcassita, moscovita, pirita, pirrotita, siderita, esfalerita, silvita, talco, topázio, ortoclásio, albita, quartzo, berilo, almandina, jadeíta, actinolita, tremolita, willemita, scheelita, autunita, carnotita, uraninita, torianita, monazita-(Ce), torita, cerussita, zircão, carnalita, epsomita, malaquita, azurita, rodocrosita, ilmenita, caulinita, cinábrio, realgar, estibnita e prata. As tabelas originais de Rosiwal (1892 e 1895) foram lidas nos PDFs do acervo da GeoSphere Austria. O Mindat não abriu (HTTP 403); o que dependia dele foi conferido no HoM ou por busca. **Não conferido na fonte primária:** os limites de índice de refração por tipo de brilho (convenção de manuais, conferida em fontes de ensino; confiança "provável"); a solubilidade da halita e da gipsita (valores de manual de química).

## Achados

### 🟠 1. O "lobo" botrioidal não é um cristal

**claim_id:** `PRF-FIG01-LEGENDA-001`  ·  **Tipo:** erro factual  ·  **Onde:** aula 01 · legenda da Figura 1
**Está escrito:** "no agregado radiado e no botrioidal, cada 'raio' ou 'lobo' é, por sua vez, um cristal alongado"
**Problema:** cada lobo de um agregado botrioidal é um feixe de muitas fibras radiadas, e não um cristal único. A legenda contradizia o próprio corpo da aula ("em geral agregados de fibras radiadas") e o exemplo (b).
**Correção aplicada:** "no agregado radiado, cada 'raio' é um cristal alongado; no botrioidal, cada 'lobo' não é um cristal só, e sim um feixe de muitas fibras radiadas a partir de um centro"
**Fonte:** *Handbook of Mineralogy*, hematite ("radiating fibrous, reniform, botryoidal or stalactitic masses")  ·  **Confiança:** confirmado

### 🟠 2. A clivagem dos anfibólios é perfeita a boa, não só "boa"

**claim_id:** `PRF-CLIV-ANFIB-001`  ·  **Tipo:** erro factual  ·  **Onde:** aula 02 · Qualidade; tabela de referência
**Está escrito:** "**boa** ou **distinta** (...; piroxênios e anfibólios)" e "| anfibólios | {110}, boa |"
**Problema:** o HoM dá a clivagem {110} como perfeita na tremolita e na magnesio-hornblenda e boa na actinolita; a dos piroxênios é boa (augita, jadeíta). Os anfibólios não são bom exemplo do grau "boa".
**Correção aplicada:** tabela: "{110}, perfeita a boa"; o exemplo do grau "boa" ficou só com os piroxênios.
**Fonte:** *Handbook of Mineralogy*: tremolite, magnesiohornblende, actinolite, augite, jadeite  ·  **Confiança:** confirmado

### 🟠 3. A calcita tem dois diedros de clivagem

**claim_id:** `PRF-CLIV-ANGULO-001`  ·  **Tipo:** omissão que gera erro  ·  **Onde:** aula 02 · tabela de referência
**Está escrito:** "74,9° entre as normais, 105,1° entre faces adjacentes"
**Problema:** os números estão certos (74,94° e 105,06°), mas o romboedro de clivagem tem arestas agudas e obtusas: faces adjacentes se cortam a 105,06° **e** a 74,94°. Como estava, sugeria um diedro único, como no octaedro da fluorita da linha de cima.
**Correção aplicada:** "as faces se cortam a 74,9° e a 105,1° (ângulos suplementares, nas arestas agudas e obtusas do romboedro)"
**Fonte:** cálculo em Python com a cela do HoM; módulo 06, aula 04  ·  **Confiança:** confirmado

### 🟠 4. Partição do coríndon: a versão já corrigida no módulo 12

**claim_id:** `PRF-CLIV-PARTICAO-001`  ·  **Tipo:** inconsistência com o módulo 12  ·  **Onde:** aula 02 · Partição
**Está escrito:** "o **coríndon** (partição romboédrica e basal, em geral por maclas polissintéticas; ele não tem clivagem)"
**Problema:** o HoM liga as partições {0001} e {10-11} do coríndon a böhmita exsolvida ("partings on {0001} and {10-11}, from exsolved böhmite"), e o módulo 12 já corrigiu exatamente essa certeza indevida (auditoria do 12, achado 11). "Em geral por maclas polissintéticas" reintroduzia a versão corrigida.
**Correção aplicada:** "partição basal {0001} e romboédrica {10-11}, ao longo de lamelas de macla e de lamelas de böhmita exsolvida nesses planos, como registrado no módulo 12; ele não tem clivagem"
**Fonte:** *Handbook of Mineralogy*, corundum; auditoria do módulo 12  ·  **Confiança:** confirmado

### 🟠 5. Figura 2: o romboedro estava desenhado como caixa

**claim_id:** `PRF-FIG02-ROMBO-001`  ·  **Tipo:** erro factual (figura)  ·  **Onde:** `fig-02-clivagem-e-formas.svg` · fragmento romboédrico
**Está escrito:** frente retangular (`590,170 670,170 670,215 590,215`), topo e lado em paralelogramo
**Problema:** é a mesma projeção oblíqua de uma caixa usada para o cubo, só mais comprida: nenhuma face mostra os ângulos oblíquos (78,1°/101,9° na face) que distinguem o romboedro de clivagem da calcita do fragmento cúbico. A figura existe justamente para mostrar que "o fragmento reproduz a forma da clivagem".
**Correção aplicada:** as três faces redesenhadas como paralelogramos oblíquos (frente em rombo com ângulos de ~78°/102°); rótulos inalterados.
**Fonte:** cálculo em Python (ângulo plano da face do romboedro {10-14})  ·  **Confiança:** confirmado

### ⚪ 6. Escala de Rosiwal: as tabelas não concordam

**claim_id:** `PRF-DUR-ROSIWAL-001`  ·  **Tipo:** certeza indevida  ·  **Onde:** aula 03 · Dureza absoluta; Exemplo (c); legenda e nota da Figura 3
**Está escrito:** "os valores citados na literatura são: talco 0,03; gipsita 1,25; calcita 4,5; fluorita 5; ortoclásio 37; quartzo 100; topázio 175; coríndon 1 000; diamante 140 000. (O valor da apatita aparece com números diferentes...)"
**Problema:** a divergência não é só da apatita. A Wikipedia inglesa (*Rosiwal scale*) dá quartzo 100 e apatita 5,5; a alemã (*Mohshärte*), quartzo 120 e apatita 6,5; e a tabela original do próprio Rosiwal (comunicação de 1892; *Monatsblätter des Wissenschaftlichen Club in Wien*, 1895; coríndon = 1 000) dá diamante 140 000, topázio 194, **quartzo 175**, adulária 59,2, apatita 8,0, fluorita 6,4, calcita 5,6, halita 2,0 (no lugar da gipsita) e talco 0,04. Não é possível escolher "o" valor; todas concordam no coríndon = 1 000, no diamante 140 vezes maior e na forma da curva.
**Correção aplicada:** "uma compilação muito citada dá: (...). As tabelas não concordam em todos os números: outras compilações dão 120 ao quartzo, a apatita aparece como 5,5 ou 6,5 (...), e a primeira tabela do próprio Rosiwal (1892–1895 ...) dava quartzo 175, topázio 194 e adulária 59. Concordam o coríndon = 1 000, o diamante 140 vezes mais duro que ele e a forma da curva; leia os números como **ordem de grandeza**." No exemplo (c), as razões com o quartzo a 120 entraram entre parênteses (4 000; 1,46) e a conclusão ("os números mudam com a tabela, a conclusão não") ficou explícita. Legenda e nota da Figura 3 ajustadas ("numa compilação usual"; "outras tabelas dão quartzo 120 (e a original de Rosiwal, 175)").
**Fonte:** A. Rosiwal, separata P.S.479 (1892), p. 104–105, e "Ueber die Härte der Mineralien" (1895), PDFs do acervo da GeoSphere Austria (opac.geologie.ac.at); Wikipedia, *Rosiwal scale* e *Mohshärte*, consultadas em 2026-10-07  ·  **Confiança:** em disputa

### 🟠 7. Dureza da cianita ao longo da lâmina

**claim_id:** `PRF-DUR-CIANITA-001`  ·  **Tipo:** erro factual (faixa)  ·  **Onde:** aula 03 · Anisotropia; Recap
**Está escrito:** "ao longo do comprimento da lâmina, a dureza é cerca de 4,5 a 5; atravessando a lâmina, 6,5 a 7"
**Problema:** o HoM dá "5.5 ∥ [001], 7 ∥ [100]", com os cristais alongados ∥ [001]; o valor ao longo ficava abaixo da fonte de referência, que tem precedência sobre a Wikipedia citada pela aula.
**Correção aplicada:** "cerca de 4,5 a 5,5; atravessando a lâmina, 6,5 a 7 (as fontes variam: o *Handbook of Mineralogy* dá 5,5 e 7)"; recap igual.
**Fonte:** *Handbook of Mineralogy*, kyanite  ·  **Confiança:** confirmado

### 🟠 8. Recap da aula 04 enfraquecia o próprio corpo

**claim_id:** `PRF-DENS-RECAP-001`  ·  **Tipo:** inconsistência interna  ·  **Onde:** aula 04 · Recap relâmpago
**Está escrito:** "G e ρ em g/cm³ coincidem em ordem de grandeza"
**Problema:** o corpo diz, corretamente, que coincidem nos três primeiros algarismos (0,2% de diferença com a água a 20 °C); "ordem de grandeza" (fator 10) é outra afirmação, muito mais fraca, e viraria card errado.
**Correção aplicada:** "G e ρ em g/cm³ têm praticamente o mesmo número: diferem cerca de 0,2% com a água a 20 °C"
**Fonte:** densidade da água a 20 °C, 0,9982 g/cm³  ·  **Confiança:** confirmado

### 🟠 9. Densidade da galena

**claim_id:** `PRF-DENS-GALENA-001`  ·  **Tipo:** erro factual (arredondamento)  ·  **Onde:** aula 04 · tabela e Erros comuns; aula 09 · ficha de apoio
**Está escrito:** "galena ~7,5"
**Problema:** HoM: D(meas.) = 7,58; D(calc.) = 7,57. Arredondado, ~7,6.
**Correção aplicada:** "~7,6" nas tabelas das aulas 04 e 09 e em "Erros comuns" da aula 04.
**Fonte:** *Handbook of Mineralogy*, galena  ·  **Confiança:** confirmado

### 🔴 10. O cobre nativo não é amarelo

**claim_id:** `PRF-BRI-COBRE-001`  ·  **Tipo:** erro factual  ·  **Onde:** aula 05 · Erros comuns
**Está escrito:** "Cobre nativo e pirita são amarelos, mas só um deles é cobre. Um brilho metálico dourado não é ouro."
**Problema:** o cobre nativo é vermelho-cobre (HoM: "pale rose on fresh surface, quickly darkens to copper-red"). A frase seguinte mostra que o par pretendido era ouro × pirita.
**Correção aplicada:** "Ouro nativo e pirita são amarelos e metálicos, mas só um deles é ouro. Um brilho metálico dourado não é ouro."
**Fonte:** *Handbook of Mineralogy*, copper e gold  ·  **Confiança:** confirmado

### 🟠 11. Cubo dourado e calcopirita

**claim_id:** `PRF-BRI-CALCOP-001`  ·  **Tipo:** omissão que gera erro  ·  **Onde:** aula 05 · Exemplo trabalhado (a)
**Está escrito:** "(cristal cúbico dourado ...) É compatível com pirita, calcopirita e outros sulfetos"
**Problema:** a calcopirita (tetragonal) forma cristais pseudotetraédricos, não cubos. Brilho e opacidade são compatíveis com as duas; o hábito do enunciado favorece a pirita.
**Correção aplicada:** "Brilho e diafaneidade são compatíveis com pirita, calcopirita e outros sulfetos dourados (o hábito cúbico favorece a pirita: a calcopirita não forma cubos)"
**Fonte:** *Handbook of Mineralogy*, pyrite e chalcopyrite  ·  **Confiança:** confirmado

### 🟠 12. Figura 4: a geometria dos raios violava a óptica

**claim_id:** `PRF-FIG04-OPTICA-001`  ·  **Tipo:** erro factual (figura)  ·  **Onde:** `fig-04-luz-brilho-e-diafaneidade.svg`
**Está escrito:** raio refletido de (450,188) a (600,70); raio interno em dois segmentos de direções diferentes; saída de (620,332) a (800,380); rótulo "absorvida: COR" solto à esquerda
**Problema:** o refletido saía a ~52° da normal contra ~60° do incidente (lei da reflexão violada); o raio mudava de direção dentro de um meio homogêneo; e o transmitido saía a ~75°, e não paralelo ao incidente, como exige uma placa de faces paralelas. É uma figura que ensina óptica errada um módulo antes do módulo 14.
**Correção aplicada:** refletido até (650,70), simétrico ao incidente; refratado em linha reta (450,192)–(598,328), aproximando-se da normal; transmitido paralelo ao incidente e mais fino (atenuado); linha-guia tracejada do rótulo "absorvida" ao feixe interno; normais tracejadas e nota "reflexão com ângulo igual ao de incidência; em placa de faces paralelas, o feixe sai paralelo ao que entrou".
**Fonte:** óptica geométrica (lei da reflexão, lei de Snell)  ·  **Confiança:** confirmado

### 🟠 13. "Constante de uma espécie para outra"

**claim_id:** `PRF-COR-IDIO-001`  ·  **Tipo:** erro factual (formulação)  ·  **Onde:** aula 06 · Três origens da cor
**Está escrito:** "Por isso é constante de uma espécie para outra, dentro de uma variação de tom"
**Problema:** a constância da cor idiocromática é entre espécimes da **mesma** espécie; como escrito, diz o contrário do conceito.
**Correção aplicada:** "constante de um espécime para outro da mesma espécie"
**Fonte:** Klein & Dutrow; Nassau  ·  **Confiança:** confirmado

### 🟠 14. "Três cristais pretos" que incluíam a pirita

**claim_id:** `PRF-COR-EXEMPLO-001`  ·  **Tipo:** inconsistência interna  ·  **Onde:** aula 06 · Exemplo trabalhado (b)
**Está escrito:** "Três cristais pretos de brilho metálico: traços vermelho-acastanhado, preto, preto-esverdeado" → "Preto-esverdeado: pirita ou calcopirita"
**Problema:** pirita e calcopirita são amarelo-latão (HoM), não pretas; o exercício associava um cristal preto à pirita.
**Correção aplicada:** enunciado "Três cristais de brilho metálico, dois cinza-escuros a pretos e um amarelo-latão"; resposta "Preto-esverdeado, no cristal amarelo-latão: pirita ou calcopirita".
**Fonte:** *Handbook of Mineralogy*, pyrite e chalcopyrite  ·  **Confiança:** confirmado

### 🟠 15. Pirrotita: cor e traço

**claim_id:** `PRF-ESP-PIRROT-001`  ·  **Tipo:** erro factual  ·  **Onde:** aula 07 · Exemplo trabalhado (a)
**Está escrito:** "Forte atração de um espécime preto metálico: magnetita (ou pirrotita monoclínica) em hipótese; o traço (preto na magnetita; preto-acinzentado a marrom na pirrotita) e a dureza (aula 03) ajudam a separar."
**Problema:** a pirrotita fresca é amarelo-bronze a castanho-bronze ("bronze-yellow to pinchbeck-brown"), não preta, e o traço é "dark grayish black", sem marrom. O que a separa da magnetita é a cor fresca e a dureza (3,5–4,5 contra 5,5–6,5); o traço quase não ajuda.
**Correção aplicada:** "magnetita em hipótese. A pirrotita monoclínica também é atraída com força, mas é amarelo-bronze a castanho-bronze quando fresca (escurece com a alteração) e bem mais mole (3,5 a 4,5, contra 5,5 a 6,5 da magnetita); a cor da superfície fresca e a dureza (aula 03) separam as duas, e o traço ajuda pouco (preto na magnetita, preto-acinzentado escuro na pirrotita)."
**Fonte:** *Handbook of Mineralogy*, pyrrhotite e magnetite  ·  **Confiança:** confirmado

### 🟠 16. Monazita: o tório não está na fórmula

**claim_id:** `PRF-ESP-RAD-001`  ·  **Tipo:** omissão que gera erro  ·  **Onde:** aula 07 · Radioatividade
**Está escrito:** "Minerais com **urânio** ou **tório** em sua fórmula são radioativos: (...), carnotita, monazita, torita."
**Problema:** a monazita-(Ce) é um fosfato de terras raras; o Th entra por substituição, e o HoM a dá como "radioactive if thorium-rich". Na lista, ela virava "mineral de Th por fórmula".
**Correção aplicada:** monazita retirada da lista e acrescentado: "A monazita, um fosfato de terras raras, não tem tório na fórmula ideal, mas costuma recebê-lo por substituição e, quando rica em tório, é radioativa."
**Fonte:** *Handbook of Mineralogy*, monazite-(Ce)  ·  **Confiança:** confirmado

### 🟠 17. Dolomita × magnesita × siderita: a dureza não separa; a densidade sim

**claim_id:** `PRF-ESP2-MAGNES-001`  ·  **Tipo:** omissão que gera erro (e remissão a material fora do curso)  ·  **Onde:** aula 08 · Exemplo trabalhado (b)
**Está escrito:** "a magnesita costuma ter dureza maior (3,5 a 4,5; ver a ficha) e a siderita é marrom; use dureza e traço para refinar"
**Problema:** as durezas se sobrepõem (magnesita 3,5–4,5; dolomita 3,5–4) e o traço das três é branco (HoM), de modo que "dureza e traço" não refinam. O critério útil é a densidade (2,86; 3,00; 3,96). "Ver a ficha" remetia a uma ficha que o curso não tem (regra de curso autossuficiente).
**Correção aplicada:** "dureza e cor não as separam bem da dolomita (magnesita 3,5 a 4,5, dolomita 3,5 a 4); a siderita costuma ser marrom; e a **densidade** ajuda mais (dolomita ~2,86; magnesita ~3,0; siderita ~3,96; aula 04)"
**Fonte:** *Handbook of Mineralogy*, dolomite, magnesite, siderite  ·  **Confiança:** confirmado

### 🟠 18. Limite superior de dureza tirado da resposta

**claim_id:** `PRF-CHV-EXEMPLO-001`  ·  **Tipo:** inconsistência interna  ·  **Onde:** aula 09 · Exemplo trabalhado (a)
**Está escrito:** "Brilho metálico; dureza ≥ 5,5 e ≤ 6,5"
**Problema:** o enunciado só diz que o espécime risca o vidro e não é riscado pelo aço; nenhum teste fixou o limite de cima. O 6,5 vinha da resposta (pirita), e não das observações, o raciocínio circular que a própria aula ensina a evitar.
**Correção aplicada:** "dureza acima de ~5,5 (risca o vidro e resiste ao aço; nenhum teste fixou o limite de cima)"
**Fonte:** lógica do exemplo; aula 03 (registro como intervalo)  ·  **Confiança:** confirmado

### 🟠 19. "Polimorfos de baixa temperatura" do quartzo

**claim_id:** `PRF-CHV-SILICA-001`  ·  **Tipo:** inconsistência com o módulo 10  ·  **Onde:** aula 09 · Quando a chave para no grupo
**Está escrito:** "quartzo e seus polimorfos de baixa temperatura, idem (módulo 10)"
**Problema:** o módulo 10 (aulas 01 e 05) apresenta a tridimita e a cristobalita como polimorfos de **alta** temperatura da sílica, metaestáveis em vulcânicas; a remissão contradizia o módulo fechado.
**Correção aplicada:** "e a tridimita e a cristobalita, polimorfos de alta temperatura da sílica que persistem metaestáveis em rochas vulcânicas (módulo 10), formam grãos pequenos que a olho nu não se separam com segurança do quartzo"
**Fonte:** módulo 10, aulas 01 e 05 (auditados)  ·  **Confiança:** confirmado

## Verificado e correto (seleção)

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `PRF-CLIV-TABELA-001` | halita/galena {100}; fluorita/diamante {111}; esfalerita {011}; calcita {10-11}; micas e talco {001}; ortoclásio {001} e {010}; topázio {001} perfeita; olivina e berilo imperfeitas | HoM | confirmado |
| `PRF-CLIV-CALCITA-001` | {10-11} morfológica = {10-14} estrutural; mesmo ângulo nas duas celas | HoM; módulo 05 aula 03; Python | confirmado |
| `PRF-CLIV-FRATURA-001` | conchoidal (quartzo), serrilhada (cobre, ouro, prata "hackly"), estilhaçada (gipsita "splintery") | HoM | confirmado |
| `PRF-DUR-LIGACAO-001` | halita 2–2,5; coríndon 9; aragonita 3,5–4; grafite 1–2 | HoM | confirmado |
| `PRF-DUR-TENAC-001` | acantita e grafite sécteis; gipsita flexível inelástica; moscovita elástica; jadeíta "very tough"; actinolita (nefrita) "tough in fibrous aggregates"; cobre, ouro, prata maleáveis e dúcteis | HoM | confirmado |
| `PRF-DUR-ESCLER-001` | esclerômetro: coríndon 400, diamante 1 500 | Wikipedia, *Mohs scale* | confirmado |
| `PRF-DENS-FAIXAS-001` | gipsita 2,317; halita 2,168; calcita 2,710; fluorita 3,18; forsterita 3,275; diamante 3,511; faialita 4,392; barita 4,50; pirita 5,018; magnetita 5,175; hematita 5,26; ouro 19,3 | HoM | confirmado |
| `PRF-DENS-OLIVINA-001` | Fo72Fa28 por volumes aditivos; 0,29 linear; aproximação declarada | Python | confirmado |
| `PRF-BRI-ESFAL-001` | esfalerita n = 2,369, brilho "resinous to adamantine", clivagem {011} | HoM | confirmado |
| `PRF-BRI-DIAF-001` | ouro "opaque in all but thinnest foils", "blue and green in transmitted light" | HoM | confirmado |
| `PRF-BRI-IR-001` | vítreo 1,3–1,9; adamantino 1,9–2,6; submetálico 2,6–3; metálico > 3 | convenção de manuais (LibreTexts; webmineral) | provável |
| `PRF-COR-TRACOS-001` | hematita "cherry-red or reddish brown"; pirita "greenish black to brownish black"; calcopirita "greenish black"; goethita "brownish yellow"; esfalerita "pale brown to pale yellow and white"; malaquita "pale green" | HoM | confirmado |
| `PRF-ESP-MAGN-001` | magnetita "strongly magnetic"; pirrotita "magnetic, varying (...) inversely with iron content"; ilmenita "weakly magnetic"; pirita "paramagnetic" | HoM | confirmado |
| `PRF-ESP-UV-001` | willemita verde-amarela (SW e LW); scheelita "bright bluish white" em SW; autunita "strong yellow-green" | HoM | confirmado |
| `PRF-ESP2-PIEZO-001` | 21 classes sem centro, 20 piezoelétricas (exceto 432), 10 polares | cristalografia padrão | confirmado |
| `PRF-ESP2-DENS-001` | halita 2,168; silvita 1,993 ("salty taste, with bitter overtones") | HoM | confirmado |
| `PRF-CHV-POLIM-001` | marcassita 6–6,5 e 4,887, traço "grayish or brownish black"; aragonita 3,5–4 e 2,95 | HoM | confirmado |
| `PRF-CHV-ESPECIES-001` | mais de 6 mil espécies IMA (6.161 em julho de 2025) | módulo 02, aula 04 (auditado) | confirmado |

A lista completa das 55 alegações verificadas, com a fonte de cada uma, está no manifesto `13-propriedades-fisicas-auditoria.json`.

**Conferido sem mudança, com nota:** (i) o HoM escreve "piezoelectric and pyroelectric" no verbete do quartzo; a aula 08 segue a cristalografia (classe 32 não é polar, logo não há piroeletricidade verdadeira; o sinal de quartzo aquecido de modo desigual é efeito secundário, via piezoeletricidade), e a seção Fontes da aula registra a divergência. (ii) O HoM dá ao ortoclásio clivagem perfeita em {001} **e** {010}; "{010} boa" da aula está dentro da variação entre autores que a própria aula declara. (iii) O quartzo tem clivagem romboédrica "rarely observable, poor" no HoM; "ausente" é a convenção de campo. (iv) "Ouro nativo ~19" é o valor do ouro puro (19,3); ouro nativo com prata fica abaixo, sem afetar o uso da aula (separar de pirita, ~5); a seção Fontes da aula 04 registra a ressalva.

## Figuras

- **Figura 1 (hábito e agregados):** desenhos corretos (prismático com terminação, acicular, tabular, equante; drusa, radiado, botrioidal, granular). Erro só na legenda (achado 1).
- **Figura 2 (clivagem e formas):** cúbica, octaédrica e basal corretas; o fragmento romboédrico era uma caixa (achado 5), redesenhado.
- **Figura 3 (Mohs × Rosiwal):** posições recalculadas com y = 295 − 37,5·log₁₀(v): todas as nove barras batem com os valores do texto (0,03 → 352,1; 140 000 → 102,0). Sem erro de desenho; a nota do rodapé foi ampliada pelo achado 6.
- **Figura 4 (luz no mineral):** geometria dos raios errada (achado 12), redesenhada.
- **Figura 5 (chave):** ramos coerentes com os valores: metálico mole (galena 2,5; ouro 2,5–3; calcopirita 3,5–4) e duro (hematita, magnetita, pirita); não metálico mole com unha (gipsita) ou ácido (calcita × fluorita) e duro sem clivagem (quartzo). A hematita (HoM 5–6) fica no limite da lâmina de aço (~5,5); como a figura é declarada "simplificada" e a legenda diz que cada folha é hipótese, não há correção. *Observação de desenho, sem correção:* as caixas das folhas "galena" e "ouro" se sobrepõem em 2 px.
- Todas as cinco SVG validadas como XML depois das edições.

## Consistência interna e com o resto do curso

- **Módulo 01, aula 05:** clivagem do diamante pela densidade de ligações por área: coerente.
- **Módulo 05, aula 03:** calcita {10-14} = {10-11}: coerente, e o ângulo de 74,94° sai igual nas duas celas.
- **Módulo 06, aula 04:** fluorita (a = 5,4626 Å, Z = 4, ρ 3,18) e cela da calcita: coerentes; o módulo 06 já citava o "romboedro de clivagem, com ângulos entre faces de cerca de 75° e 105°", na mesma forma que a aula 02 ficou depois do achado 3.
- **Módulo 10:** metamictização (aula 04) coerente; polimorfos da sílica corrigidos na aula 09 (achado 19).
- **Módulo 11, aula 04:** ângulos 87°/93° e 56°/124° dos inossilicatos coerentes; a qualidade da clivagem dos anfibólios agora segue o HoM (achado 2).
- **Módulo 12:** pirrotita monoclínica perto de Fe₇S₈ (aula 01, corrigida na auditoria do 12) coerente com a aula 07; partição do coríndon alinhada (achado 4).
- **Entre as aulas deste módulo:** galena ~7,6 igual nas aulas 04 e 09; densidades de halita/silvita iguais nas aulas 04 e 08; durezas de pirita, magnetita, hematita e calcopirita iguais nas aulas 06 e 09; o critério de confiança da aula 09 bate com o exemplo depois do achado 18.
- **Regra de curso autossuficiente:** a remissão "ver a ficha" (aula 08) foi removida (achado 17); as remissões aos cursos irmãos (curso-geologia, curso-gemologia) são por nome, sem wikilink, como manda a regra.

## Correções aplicadas

**Aplicadas em:** 2026-10-07

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `PRF-FIG01-LEGENDA-001` | 🟠 | Corrigido | aula-01 |
| `PRF-CLIV-ANFIB-001` | 🟠 | Corrigido | aula-02 |
| `PRF-CLIV-ANGULO-001` | 🟠 | Corrigido | aula-02 |
| `PRF-CLIV-PARTICAO-001` | 🟠 | Corrigido | aula-02 |
| `PRF-FIG02-ROMBO-001` | 🟠 | Corrigido | fig-02 |
| `PRF-DUR-ROSIWAL-001` | ⚪ | Corrigido (divergência explicitada) | aula-03, fig-03 |
| `PRF-DUR-CIANITA-001` | 🟠 | Corrigido | aula-03 |
| `PRF-DENS-RECAP-001` | 🟠 | Corrigido | aula-04 |
| `PRF-DENS-GALENA-001` | 🟠 | Corrigido | aula-04, aula-09 |
| `PRF-BRI-COBRE-001` | 🔴 | Corrigido | aula-05 |
| `PRF-BRI-CALCOP-001` | 🟠 | Corrigido | aula-05 |
| `PRF-FIG04-OPTICA-001` | 🟠 | Corrigido | fig-04 |
| `PRF-COR-IDIO-001` | 🟠 | Corrigido | aula-06 |
| `PRF-COR-EXEMPLO-001` | 🟠 | Corrigido | aula-06 |
| `PRF-ESP-PIRROT-001` | 🟠 | Corrigido | aula-07 |
| `PRF-ESP-RAD-001` | 🟠 | Corrigido | aula-07 |
| `PRF-ESP2-MAGNES-001` | 🟠 | Corrigido | aula-08 |
| `PRF-CHV-EXEMPLO-001` | 🟠 | Corrigido | aula-09 |
| `PRF-CHV-SILICA-001` | 🟠 | Corrigido | aula-09 |

Também foram atualizados: as seções "Fontes consultadas" das nove aulas (os "a conferir" e "de memória" viraram fonte conferida, com o verbete do HoM; na aula 05, a atribuição dos limites de índice de refração à Wikipedia foi corrigida, porque o verbete não traz esses números); os rodapés `alegacoes_auditaveis` (campo `audit:` das 60 alegações; texto `claim:` das 9 corrigidas ou ajustadas; 14 alegações novas para os achados que vieram do corpo e das figuras; `palavras_corpo` recontado; YAML dos rodapés validado); o hub do módulo (registro da auditoria); e o `course-state.yaml` (bloco `audit` do módulo 13, `content_hash` e `palavras_corpo` das nove aulas). As aulas foram regravadas com fim de linha LF, como as do módulo 12.

**Pendências:** nenhuma. Não há questionário nem baralho a propagar (ainda não existem; o gate para gerá-los fica liberado, sem achado 🔴/🟠 aberto).

## Observações fora do escopo factual

- A aula 03 passou a ~1.630 palavras de corpo com a ressalva de Rosiwal (achado 6); vale a revisão didática conferir se continua dentro dos 30 minutos.
- A aula 08 (b) e a aula 09 agora usam a densidade como critério principal em dois exemplos; a revisão didática pode querer um contraexemplo em que a densidade não decide.

## Segunda passagem (alegações da revisão didática)

**Auditado em:** 2026-10-07  ·  **Modo:** audit-and-fix  ·  **Profundidade:** full, escopo restrito
**Escopo:** as 8 alegações que a revisão didática registrou com `audit: pendente` (`PRF-HAB-DIDAT-001`, `PRF-CLIV-DIDAT-001`, `PRF-DUR-DIDAT-001`, `PRF-DENS-DIDAT-001`, `PRF-BRI-DIDAT-001`, `PRF-COR-DIDAT-001`, `PRF-ESP-DIDAT-001`, `PRF-CHV-DIDAT-001`), a sugestão 🔵 4 da revisão (densidade × berilo no exemplo (d) da aula 09) e o texto que a revisão alterou, conforme `13-propriedades-fisicas-revisao-didatica.md`: a aula 03 enxugada (Rosiwal entre corpo e Fontes, esclerômetro, ponte da anisotropia, jade, procedimento, recap); os exemplos (a) e (b) da aula 04 (apatita fora da tabela; volume molar e passos algébricos); o exemplo (c) da aula 05; as frases reescritas da aula 06; as glosas e o recap da aula 07; o "erro comum" reescrito da aula 08; os itens (i) a (iv) e os exemplos (c) e (d) da aula 09. As 19 correções da primeira passagem foram conferidas: nenhuma foi revertida (a do achado 6, Rosiwal, foi só reorganizada: o corpo mantém a divergência do quartzo, 100, 120 ou 175, e da apatita; as Fontes mantêm a tabela original).
**Veredito:** Requer correção → **correção aplicada; estado final: Aprovado** (nenhum achado aberto)

🔴 0 · 🟠 1 · 🟡 0 · 🔵 0 · ⚪ 0  ·  Verificadas e corretas: 8 das 8 alegações pendentes, mais o texto alterado em volta delas. O achado novo veio da sugestão 🔵 4 da revisão, e não de uma alegação `DIDAT`.

**Contas refeitas em Python (2026-10-07):**

| O quê | Resultado | Onde |
|---|---|---|
| Volume molar Fo = 140,69 / 3,275; Fa = 203,77 / 4,39 | 42,959 e 46,417 cm³/mol (texto 42,96 e 46,42 ✔) | a04 (b) |
| Diferenças Fa − Fo (massa e volume) | 63,08 g/mol e 3,458 cm³/mol (texto 3,46 ✔) | a04 (b) |
| 3,60 × 42,96 e 3,60 × 3,46 | 154,656 e 12,456 (texto 154,66 e 12,46 ✔) | a04 (b) |
| 154,66 − 140,69 e 63,08 − 12,46; quociente | 13,97 e 50,62; 0,27598 ✔ | a04 (b) |
| x(Fa) sem arredondar os passos | 0,27575 (0,27534 com faialita 4,392) → Fo72Fa28 ✔ | a04 (b) |
| Interpolação linear (3,60 − 3,275) / (4,39 − 3,275) | 0,2915 → 0,29 ✔ | a04 (b) |
| M(Mg₂SiO₄), M(Fe₂SiO₄) com massas atômicas padrão | 140,69 e 203,77 ✔ | a04 (b) |
| G = 47,7 / 15,0; extremos com ± 0,1 g | 3,180; 3,145 e 3,216 ✔ (apatita ~3,2 dentro) | a04 (a) |
| (110)∧(101) e (111)∧(11-1) no cubo | 60,000° e 70,529° ✔ | a02 (b) |

### 🟠 20. A densidade não separa bem o quartzo do berilo

**claim_id:** `PRF-CHV-BERILO-001` (novo; o trecho não estava em `PRF-CHV-DIDAT-001`)  ·  **Tipo:** omissão que gera erro  ·  **Onde:** aula 09 · Exemplo trabalhado (d)
**Está escrito:** "Confiança **baixa**: (...) e várias alternativas seguem abertas; a densidade (2,65) é o próximo teste."
**Problema:** o exemplo lista berilo, turmalina e topázio incolores como alternativas ao quartzo e indica a densidade como o próximo teste, sem dizer até onde ela vai. Ela descarta o topázio (3,49–3,57) e a turmalina incolor (elbaíta, 2,90–3,10), mas o berilo vai de 2,63 a 2,97, crescendo com o teor de álcalis (D calc. 2,640): um berilo pobre em álcalis tem a densidade do quartzo dentro da incerteza da balança hidrostática (± 0,04 no exemplo da aula 04). O aluno que medisse 2,65 concluiria "quartzo" com um teste que não exclui o berilo, o mesmo erro de método que a aula condena ("só descarta o que foi testado"). É a sugestão 🔵 4 da revisão didática, confirmada.
**Correção aplicada:** "O próximo teste é a densidade (quartzo 2,65), mas ela não fecha tudo: descarta o topázio (~3,5) e a turmalina incolor (~2,9 a 3,1), e separa mal o berilo (2,63 a 2,97, conforme o teor de álcalis), que pode ter a densidade do quartzo; para ele, o teste seguinte é o índice de refração (módulo 14 em diante) ou a difração." Fontes da aula ampliadas com os verbetes; alegação nova no rodapé; `palavras_corpo` de 1.361 para 1.415 (duração mantida em ~28 min).
**Fonte:** *Handbook of Mineralogy* (Mineral Data Publishing, v. 1), verbetes beryl (H 7,5–8; D(meas.) 2,63–2,97 "increasing with alkali content"; n 1,565–1,610), topaz (H 8; {001} perfeita; D 3,49–3,57) e elbaite (H 7; D 2,90–3,10), PDFs lidos em 2026-10-07; quartzo 2,65 e n ≈ 1,54 já nas aulas 04 e 05  ·  **Nível:** base de referência  ·  **Confiança:** confirmado

### Verificado e correto (segunda passagem)

| claim_id | O que foi conferido | Fonte | Confiança |
|---|---|---|---|
| `PRF-HAB-DIDAT-001` | crisotila é do grupo da serpentina e é a forma mais comum de amianto (cerca de 95% do amianto usado nos EUA, proporção parecida em outros países) | Wikipedia, *Chrysotile*, e USGS (asbestos), por busca em 2026-10-07 | confirmado |
| `PRF-CLIV-DIDAT-001` | obsidiana = vidro vulcânico; (110)∧(101) = 60°, que a resolução já dava, agora pedido no enunciado; os dois ângulos da clivagem {110} (60° e 90°) | definição usual; Python | confirmado |
| `PRF-DUR-DIDAT-001` | anisotropia de dureza pela mesma causa da clivagem (as ligações a romper mudam com a direção); esclerômetro = ponta de diamante arrastada sob carga conhecida (Turner, 1896), e a tabela "absolute hardness" da Wikipedia (coríndon 400, diamante 1 500) é declarada "measured by a sclerometer"; nefrita = agregado entrelaçado de tremolita-actinolita (anfibólio), jadeíta = piroxênio, os dois chamados jade, tenacidade pela microestrutura; o detalhe da tabela original de Rosiwal nas Fontes é o mesmo do achado 6 (subconjunto) | Klein & Dutrow; Wikipedia, *Mohs scale* e *Sclerometer*; literatura de jade (por busca); HoM jadeíta e actinolita (primeira passagem) | confirmado |
| `PRF-DENS-DIDAT-001` | "volume molar" (M/ρ, cm³/mol) no lugar de "densidade molar"; 63,08 e 3,46 como diferenças; multiplicação em cruz; x = 0,276 → Fo72Fa28 (ver a tabela de contas). Exemplo (a): apatita ~3,2 compatível com 3,18 ± 0,04 | Python; HoM fluorapatite (D(meas.) 3,1–3,25; D(calc.) 3,18), lido em 2026-10-07 | confirmado |
| `PRF-BRI-DIDAT-001` | n ≈ 2,4 (HoM 2,369) cairia no adamantino pelos limites convencionais; o HoM dá brilho "resinous to adamantine", e as ricas em Fe chegam ao submetálico: há espécimes claros adamantinos; a classificação é visual | HoM sphalerite (lido em 2026-10-07); Wikipedia, *Sphalerite*, por busca | confirmado |
| `PRF-COR-DIDAT-001` | "muitos minerais comuns são alocromáticos, e essa classe causa a maior confusão" (a frase circular saiu); exsolução definida no módulo 09, aula 03 e retomada no 23; "num espécime desconhecido, não se sabe se a cor é idio- ou alocromática" | Klein & Dutrow; módulo 09, aula 03 | confirmado |
| `PRF-ESP-DIDAT-001` | ferrimagnetismo: subredes de momentos antiparalelos e desiguais, magnetização líquida não nula (Néel, 1948; magnetita); uranilo = UO₂²⁺, com U⁶⁺, ativador da fluorescência da autunita; o sievert é a unidade SI de dose equivalente, e µSv/h é taxa; recap da monazita agora coerente com o achado 16; torita (ThSiO₄) tem Th na fórmula; "willemita" | literatura de magnetismo (por busca); uvminerals.org (autunita, uranilo); SI (BIPM); HoM monazita-(Ce) e torita (primeira passagem) | confirmado |
| `PRF-CHV-DIDAT-001` | exemplo (c): a densidade não decide entre pirita (Mindat 4,8–5,0; HoM 5,018) e marcassita (4,83–4,92; HoM 4,887), faixas que se tocam; exemplo (d): topázio com {001} perfeita, menos provável sem excluí-lo; confiança "baixa" coerente com a tabela da aula; a escada de inferência é a da espinha didática do `_contexto.md`, adotada nos módulos 25–27, 37 e 50 (a aula cita 25–27 e 50 sem dizer "só") | Mindat, por busca em 2026-10-07; HoM topaz e marcasite; `_contexto.md` | confirmado |

Também conferido no texto alterado, sem achado: o passo (2) reescrito do procedimento de dureza (aula 03); "os números variam com a tabela" no recap da aula 03; o "erro comum" da aula 08 (o pó reage mais que a superfície; coerente com a tabela de efervescência e com `PRF-ESP2-ACIDO-001`); "Cada um tem seus perigos, e o ácido e a água danificam o espécime" (aula 09); a figura 5 reespaçada (só posições; rótulos iguais aos conferidos na primeira passagem).

### Correções aplicadas (segunda passagem)

**Aplicadas em:** 2026-10-07

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `PRF-CHV-BERILO-001` | 🟠 | Corrigido | aula-09 (corpo do exemplo (d), Fontes consultadas, rodapé com alegação nova, `palavras_corpo`) |
| `PRF-HAB-DIDAT-001`, `PRF-CLIV-DIDAT-001`, `PRF-DUR-DIDAT-001`, `PRF-DENS-DIDAT-001`, `PRF-BRI-DIDAT-001`, `PRF-COR-DIDAT-001`, `PRF-ESP-DIDAT-001`, `PRF-CHV-DIDAT-001` | — | Verificado (rodapé `audit:` de "pendente" para "verificado") | aulas 01 a 07 e 09 (só rodapé, exceto a 09) |

Também atualizados: o manifesto `.json` (1 achado novo, 8 alegações verificadas, contagens do resumo), o hub do módulo (registro da segunda passagem) e o `course-state.yaml` (bloco `audit` do módulo 13; `content_hash` das oito aulas tocadas e `palavras_corpo` da aula 09). Nenhuma figura foi alterada. O relatório da revisão didática não foi editado: a sugestão 🔵 4 dele fica como registro histórico, e o achado 20 registra a correção.

**Pendências:** nenhuma. Não há questionário nem baralho a propagar (ainda não existem). Quando forem gerados, não devem tratar a densidade 2,65 como prova de quartzo diante do berilo, e devem seguir a sugestão 🔵 1 da revisão (Rosiwal e limites de n como ordem de grandeza, não como números a decorar).

## Auditoria de questionários e baralho

**Auditado em:** 2026-10-07  ·  **Modo:** audit-and-fix  ·  **Profundidade:** full, escopo restrito ao material derivado
**Material:** `13-propriedades-fisicas-questionario-parcial-1.md` (Q1–Q11, 22 pts), `-parcial-2.md` (Q12–Q23, 29 pts), `-final.md` (Q24–Q38, 39 pts); `-flashcards-basic.csv` (fb001–fb179), `-flashcards-cloze.csv` (fc001–fc007) e `-flashcards.md`
**Critério:** todo gabarito, distrator comentado e card tem de ser verdadeiro e rastreável a uma frase das aulas atuais (versões já auditadas em duas passagens). Conferidos também: contas, cards com fato fora das aulas, versos que não respondem à frente, sintaxe Cloze, quase-duplicatas, distratores defensáveis, objetivo sem questão, IDs de aula (aula 06 = `a08`, 07 = `a06`, 08 = `a09`, 09 = `a07`) e as orientações já fixadas (nenhum número de Rosiwal nem corte de índice de refração cobrado como valor a decorar; monazita só "quando rica em tório"; densidade sem separar pirita × marcassita nem quartzo × berilo).
**Veredito:** Requer correção → **correções aplicadas; estado final: Aprovado** (nenhum achado aberto)

🔴 0 · 🟠 8 · 🟡 0 · 🔵 0 · ⚪ 0

Dois achados (26 e 27) vieram de frases das aulas 07 e 08 que as duas passagens anteriores deixaram passar e que o material derivado tornou explícitas; foram corrigidos na aula com ajuste mínimo e propagados.

**Contas refeitas em Python (2026-10-07):**

| Onde | Conta | Resultado | Gabarito |
|---|---|---|---|
| P1 Q6 | olivina de ρ = 3,80 por volumes aditivos (V = 42,959 e 46,417 cm³/mol); interpolação linear | x = 0,4516 → Fo55Fa45; linear 0,471 | ✔ |
| P1 Q10 (b)(c)(d) | (100)∧(110); (100)∧(111); (011)∧(1 1̄ 0) | 45,00°; 54,74°; 120,00° entre vetores → 60° entre planos | ✔ |
| P1 Q11 | 36,0 / 10,2; 35,9 / 10,0; 36,1 / 10,4 | 3,529; 3,590; 3,471 → 3,53 ± 0,06 | ✔ |
| P2 Q21 | 6,2 − 0,12; ÷ 16; + 0,12 | 6,08; 0,38; 0,50 µSv/h | ✔ |
| F Q37 (a) | 3,567³; 8 × 12,011 / (0,6022 × V) | 45,385 Å³; 3,516 g/cm³ | ✔ |
| F Q37 (b) | 2,000 / 0,570; 1,999 / 0,568; 2,001 / 0,572 | 3,509; **3,519**; **3,498** | ✘ expressões trocadas (achado 21) |
| F Q37 (c)(d) | (3,516 − 3,509) / 3,516; 2,1 / 0,77; 1,9 / 0,37 | 0,2%; 2,727; 5,135 | ✔ |

**Cobertura:** os 7 objetivos têm questão no final; os parciais cobrem `oa01`–`oa04` e `oa05`–`oa06`; as matrizes somam 22, 29 e 39 pontos (refeito item a item; total 90 pontos em 38 questões, igual ao `course-state.yaml`); as distribuições cognitiva e por tipo conferem com as listas de questões. Cada aula e cada objetivo têm cards (19, 23+2, 22+1, 18+3, 19, 19, 22, 19+1 e 18, pela ordem das aulas no arquivo). As colunas `aula` dos CSVs e as notas de cobertura dos questionários usam os IDs certos. A tabela do `flashcards.md` confere campo a campo com os CSVs (186 de 186, conferido por script). Sintaxe Cloze válida (c1 a c3, sem chaves internas). Nenhum número de Rosiwal nem limite de índice de refração é cobrado (P2 Q12 e fb088/fb089 cobram só a relação; fb049 e fb051, só a conclusão); a monazita só aparece em fb137, com "rica em tório"; Q25 e fb169 tratam a densidade como incapaz de separar pirita de marcassita, e Q38 (c), fb177 e fb178, como incapaz de excluir o berilo. Os dados fora das aulas (pesagens e densidade hipotéticas; cela do diamante na Q37) estão declarados nos registros de geração.

### 🟠 21. Q37 (b): as duas expressões dos extremos estavam trocadas

**claim_id:** `QST-M13-CALC-001`  ·  **Tipo:** inconsistência interna (conta)  ·  **Onde:** questionário final · Q37 (b), gabarito
**Está escrito:** "Extremos: 2,001 / (2,001 − 1,429) = **3,519** e 1,999 / (1,999 − 1,431) = **3,498**"
**Problema:** 2,001 / 0,572 = 3,498 e 1,999 / 0,568 = 3,519; os resultados estavam certos, mas cada um ao lado da expressão errada. O aluno que refizesse a conta pelo método da aula 04 (W_ar menor com W_água maior dá o máximo) acharia o gabarito errado.
**Correção aplicada:** "Extremos: 1,999 / (1,999 − 1,431) = **3,519** e 2,001 / (2,001 − 1,429) = **3,498**" (resultado, G = 3,51 ± 0,01, inalterado)
**Fonte:** Python, 2026-10-07; aula 04, exemplo (a)  ·  **Confiança:** confirmado

### 🟠 22. Q25: calcopirita "descartada pela dureza" num enunciado sem dureza

**claim_id:** `QST-M13-CALCOP-001`  ·  **Tipo:** inconsistência interna  ·  **Onde:** questionário final · Q25, comentário do distrator d)
**Está escrito:** "d) a calcopirita foi descartada pela dureza e pela densidade (cerca de 4,2)"
**Problema:** o enunciado da Q25 não dá dureza (só hábito, cor, brilho, tenacidade, traço e densidade); o comentário copiava o exemplo da aula 09, que tem o teste do canivete. Descartar por um teste que não foi feito é o erro que a aula 09 condena ("só descarta o que foi testado").
**Correção aplicada:** "d) a calcopirita fica descartada pela densidade (cerca de 4,2, longe de 4,95) e pelo hábito cúbico, que ela não forma (aula 05); o traço preto-esverdeado é compartilhado com a pirita e não a favorece."
**Fonte:** aula 09 (ficha de apoio: calcopirita ~4,2) e aula 05 (exemplo (a): "a calcopirita não forma cubos")  ·  **Confiança:** confirmado

### 🟠 23. Q38 (e): o índice de refração parecia dar "confirmado"

**claim_id:** `QST-M13-IRCONF-001`  ·  **Tipo:** omissão que gera erro  ·  **Onde:** questionário final · Q38 (e), gabarito
**Está escrito:** "O **índice de refração** (módulo 14 em diante) ou a **difração de raios X**; o resultado seria registrado como provável, e não confirmado até esse teste"
**Problema:** "até esse teste" põe o índice de refração entre os testes que confirmam. Pela aula 09, "confirmado" só vem de método que mede composição ou estrutura (difração, análise química); o índice de refração separa o quartzo do berilo, mas a identificação continua provável.
**Correção aplicada:** "O **índice de refração** (módulo 14 em diante) separaria o quartzo do berilo, mas a identificação continuaria **provável**; só a **difração de raios X** (ou a análise química) a registraria como confirmada"
**Fonte:** aula 09 (Vocabulário, "confirmado"; grau de confiança)  ·  **Confiança:** confirmado

### 🟠 24. Q12: comentário dizia que a clivagem não muda o tipo de brilho

**claim_id:** `QST-M13-BRILHO-001`  ·  **Tipo:** inconsistência com a aula  ·  **Onde:** questionário parcial 2 · Q12, comentário do distrator d)
**Está escrito:** "d) a clivagem afeta a superfície exposta, mas não o tipo de brilho em si."
**Problema:** contradiz a aula 05: "o nacarado só aparece nos planos de clivagem {001} das micas e do talco, e o mesmo cristal tem brilho vítreo nas faces de fratura". O distrator continua errado (o número de direções não explica a sequência vítreo → metálico), mas pela razão certa.
**Correção aplicada:** "d) a superfície de clivagem pode mudar a aparência do brilho (o nacarado das micas e do talco só aparece nela), mas o número de direções de clivagem não explica a sequência de vítreo a metálico."
**Fonte:** aula 05 (O que decide o brilho)  ·  **Confiança:** confirmado

### 🟠 25. Parcial 1: três comentários de gabarito fora das aulas ou imprecisos

**claim_id:** `QST-M13-COMENT-001`  ·  **Tipo:** inconsistência interna  ·  **Onde:** questionário parcial 1 · Q4 (distrator c), Q6 (distrator d), Q10 (d)
**Está escrito:** Q4: "c) o topázio não é descrito com fratura que se propaga assim"; Q6: "a) e d) estão longe do cálculo (d inverte os papéis do Mg e do Fe)"; Q10 (d): "o módulo de 0,5 dá **60°** (o suplementar, 120°, é o ângulo entre as faces vizinhas do dodecaedro; a aula usa o agudo)"
**Problema:** Q4: afirmação vaga sobre a fratura do topázio, sem apoio na aula (o *Handbook* dá "subconchoidal to uneven"), quando a razão que a aula dá é outra (a quebra plana em {001} é clivagem, não fratura). Q6: Fo30Fa70 não é a inversão de nenhuma resposta (a de Fo55Fa45 seria Fo45Fa55). Q10 (d): o diedro de 120° do dodecaedro é fato fora da aula, e (011) e (1 1̄ 0) nem são faces vizinhas (os vetores fazem 120° entre si); a nota misturava as duas coisas.
**Correção aplicada:** Q4: "c) a fratura é a quebra onde não há plano de fraqueza; uma quebra plana ao longo de {001} é clivagem, e não fratura"; Q6: "a) e d) estão longe do cálculo."; Q10 (d): "o ângulo entre os vetores é 120°, e entre os dois planos, como direções de clivagem, toma-se o agudo: **60°**, um dos dois ângulos da clivagem {110} da aula (60° e 90°)". Respostas e pontos inalterados.
**Fonte:** aula 02 (fratura; tabela de clivagens; exemplo (b)); Python  ·  **Confiança:** confirmado

### 🟠 26. Piroeletricidade exige eixo polar único: o quartzo tem eixos de pontas diferentes

**claim_id:** `PRF-ESP2-POLAR-001` (origem: `PRF-ESP2-PIEZO-001`, aula 08)  ·  **Tipo:** omissão que gera erro  ·  **Onde:** aula 08 · Vocabulário ("eixo polar") e Piezo e piroeletricidade; questionário parcial 2 · Q20, gabarito; cards fb147, fb148, fb150, fb151
**Está escrito:** aula 08: "eixo polar: direção cujas duas pontas são diferentes (sem espelho nem eixo 2 que as troque)"; "Dez das 20 têm um eixo polar, uma direção cujas pontas são diferentes"; Q20: "[o quartzo] não tem eixo polar (pontas iguais), então a temperatura não gera polarização"; fb150: "Não tem centro de simetria, mas também não tem eixo polar."
**Problema:** pela definição da própria aula, o quartzo (32) tem eixos polares: os três eixos 2 (eixos a) têm pontas diferentes, e é ao longo deles que aparece a carga piezoelétrica. O que falta ao quartzo é um eixo polar **único**: os três são equivalentes pelo eixo 3, e as polarizações se cancelam. A Q20 dizia "pontas iguais", o que é falso para os eixos a. O critério das 10 classes piroelétricas é o eixo polar único.
**Correção aplicada:** aula 08, Vocabulário: "...; para a piroeletricidade, ela tem de ser **única**, sem outra direção equivalente pela simetria"; corpo: "**Dez** das 20 têm um **eixo polar único**, uma direção cujas pontas são diferentes e que nenhuma operação de simetria repete em outra direção (...). (O quartzo tem três direções de pontas diferentes, os eixos a, mas a simetria as torna equivalentes e os efeitos se cancelam: ele não é polar.)"; Fontes e rodapé (`PRF-ESP2-PIEZO-001`) atualizados; `palavras_corpo` de 1.427 para 1.464 (duração mantida em ~27 min). Q20: "(...) mas não tem eixo polar **único**: seus três eixos a têm pontas diferentes, mas são equivalentes pela simetria, e os efeitos se cancelam (...)", e a turmalina com "eixo polar **único**". Cards: fb147 ("eixo polar único"), fb148 (definição com a condição de unicidade), fb150 (verso com os três eixos a), fb151 ("eixo polar único").
**Fonte:** *International Tables for Crystallography*, vol. D, sec. 3.3.6.3, e literatura de piezoeletricidade do α-quartzo (grupo 32 com três eixos 2 polares e eixo 3 não polar; piroeletricidade só com eixo polar único), por busca em 2026-10-07  ·  **Nível:** normativa  ·  **Confiança:** confirmado
**Também aparece em:** aula 08, questionário parcial 2, flashcards-basic.csv, flashcards.md. *Fora deste módulo, não corrigido:* o módulo 04 (aula 05 e card `mineralogia-m04-fb049`) tem a mesma imprecisão; ver Observações.

### 🟠 27. Uranilo da autunita e tungstato da scheelita não são ativadores no sentido da aula

**claim_id:** `PRF-ESP-LUMIN-002` (origem: `PRF-ESP-LUMIN-001`, aula 07)  ·  **Tipo:** inconsistência interna  ·  **Onde:** aula 07 · Luminescência ("A causa"); card fb130
**Está escrito:** aula 07: "a luminescência vem de **ativadores**: Mn²⁺ (...), terras raras (...), o uranilo (o íon UO₂²⁺), em minerais de urânio como a autunita (verde-amarelada), e o tungstato da scheelita"; Vocabulário: "ativador: impureza ou defeito que causa luminescência"; fb130: "Que ativadores causam luminescência (...)? (...) uranilo (autunita verde-amarelada) e o tungstato da scheelita"
**Problema:** na autunita o uranilo é da fórmula, e na scheelita (CaWO₄) o grupo WO₄²⁻ também: são casos de luminescência intrínseca (autoativada), e não de impureza ou defeito. O card ensinava o aluno a chamar de impureza um componente essencial. O uranilo como ativador em traços existe (faz fluorescer muitos minerais), e isso fica.
**Correção aplicada:** aula 07: "(...) terras raras (algumas fluoritas de tom azulado) e o uranilo (o íon UO₂²⁺), que em traços faz fluorescer muitos minerais. Em alguns, o centro que emite é parte da própria fórmula (luminescência **intrínseca**, ou autoativada): o uranilo da autunita (verde-amarelada) e o tungstato da scheelita (azul-esbranquiçada, com luz ultravioleta de ondas curtas)."; Fontes e rodapé (`PRF-ESP-LUMIN-001`) atualizados; `palavras_corpo` de 1.321 para 1.341. fb130: frente "Que ativadores (impurezas) causam luminescência, e em que dois minerais o centro que emite é da própria fórmula?", verso com a separação. O recap da aula ("ativadores (Mn²⁺, terras raras, uranilo)") e a Q18 do parcial 2 seguem corretos (uranilo em traços).
**Fonte:** Fluorescent Mineral Database (uvminerals.org: autunita "self-activating", uranilo integral à fórmula; uranilo em traços como ativador de muitos minerais); literatura de luminescência da scheelita (WO₄²⁻ como ativador intrínseco), por busca em 2026-10-07  ·  **Nível:** base de referência / revisada por pares  ·  **Confiança:** confirmado
**Também aparece em:** aula 07, flashcards-basic.csv, flashcards.md

### 🟠 28. Quase-duplicatas no baralho

**claim_id:** `FLC-M13-DUPLIC-001`  ·  **Tipo:** inconsistência interna  ·  **Onde:** fc001 × fb026, fb027, fb028; fb048 × fb049; fb092 × fb095; fb040 × fb041
**Está escrito:** fb026–fb028: "{100}, perfeita, em 3 direções a 90°", "{111}, perfeita, em 4 direções (octaédrica)", "{110}, perfeita, em 6 direções (dodecaedro rômbico)", o mesmo fato das lacunas de fc001; fb049 ("Por que é erro dizer que o quartzo (7) é quase duas vezes mais duro que a fluorita (4)?" / "os degraus de Mohs são desiguais: a escala só dá ordem") repete fb048; fb092 termina com "o mesmo cristal é vítreo na fratura", a resposta de fb095; fb040 e fb041 pedem a mesma lista (obsidiana e opala).
**Problema:** contraria os critérios declarados no `flashcards.md` ("Nenhum card Basic repete o fato de um Cloze"; um fato por card) e faz cards competirem na revisão.
**Correção aplicada:** fb026 "{100}, perfeita, cúbica: planos a 90°."; fb027 "{111}, perfeita (octaédrica)."; fb028 "{110}, perfeita (dodecaedro rômbico)." (o número de direções fica só no fc001); fb049 passou a perguntar "O número da dureza absoluta muda com o método (Rosiwal, esclerômetro). O que não muda?" / "A ordem dos minerais e o fato de os degraus serem desiguais; só o valor numérico depende do método." (aula 03: "O número muda com o método; a ordem e a desigualdade dos degraus, não"); fb092 "Nos planos de clivagem {001} de micas e talco (e nos da apofilita)."; fb040 "Superfície curva e lisa, em ondas concêntricas, como a do vidro quebrado; entre os minerais, o quartzo é o exemplo clássico." CSV e md.
**Fonte:** aulas 02, 03 e 05  ·  **Confiança:** confirmado

### Verificado e correto (terceira passagem)

| claim_id | O que foi conferido | Fonte | Confiança |
|---|---|---|---|
| `QST-M13-CALC-002` | todas as contas dos gabaritos (tabela acima); só a Q37 (b) tinha erro | Python, 2026-10-07 | confirmado |
| `QST-M13-GABAR-001` | os 38 gabaritos e os comentários de distratores, contra as aulas atuais; nenhum distrator defensável (o b) da Q25, "é pirita, porque o hábito cúbico...", continua errado pela aula 09: o hábito é pista instável e a marcassita não foi excluída) | aulas 01 a 09 | confirmado |
| `QST-M13-OA-001` | 7 de 7 objetivos com questão no final; matrizes de 22, 29 e 39 pontos; distribuições cognitiva e por tipo; IDs `aNN` das notas de cobertura | course-state.yaml; matrizes | confirmado |
| `FLC-M13-RASTRO-001` | 186 cards rastreados a frases das aulas (incluídas as seções Fontes); nenhum fato fabricado; versos respondem às frentes; IDs de aula e objetivos; contagens por aula | aulas 01 a 09; CSVs | confirmado |
| `FLC-M13-TERMOS-001` | monazita só "quando rica em tório" (fb137); sem número de Rosiwal (fb049, fb050, fb051) nem corte de índice de refração (fb088, fb089, fb094); cianita 4,5–5,5 / 6,5–7 (fb057); galena ~7,6 (fc005, fb082); pirita × marcassita (fb168, fb169, Q25) e quartzo × berilo (fb177, Q38) sem separação por densidade; calcita 74,9°/105,1° (fb029); anfibólios "perfeita a boa" (fb032); ouro e pirita, e não cobre, no par dourado (fb110, fb120) | achados 2, 3, 6, 7, 9, 10, 16 e 20 | confirmado |

### Correções aplicadas (terceira passagem)

**Aplicadas em:** 2026-10-07

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `QST-M13-CALC-001` | 🟠 | Corrigido | questionario-final (Q37) |
| `QST-M13-CALCOP-001` | 🟠 | Corrigido | questionario-final (Q25) |
| `QST-M13-IRCONF-001` | 🟠 | Corrigido | questionario-final (Q38) |
| `QST-M13-BRILHO-001` | 🟠 | Corrigido | questionario-parcial-2 (Q12) |
| `QST-M13-COMENT-001` | 🟠 | Corrigido | questionario-parcial-1 (Q4, Q6, Q10) |
| `PRF-ESP2-POLAR-001` | 🟠 | Corrigido | aula-08 (Vocabulário, corpo, Fontes, rodapé, `palavras_corpo`), questionario-parcial-2 (Q20), flashcards-basic.csv e flashcards.md (fb147, fb148, fb150, fb151) |
| `PRF-ESP-LUMIN-002` | 🟠 | Corrigido | aula-07 (corpo, Fontes, rodapé, `palavras_corpo`), flashcards-basic.csv e flashcards.md (fb130) |
| `FLC-M13-DUPLIC-001` | 🟠 | Corrigido | flashcards-basic.csv e flashcards.md (fb026, fb027, fb028, fb040, fb049, fb092) |

Também atualizados: o registro de geração dos três questionários, o cabeçalho e o histórico do `flashcards.md`, o manifesto `.json` (8 achados, 5 alegações verificadas, contagens) e o `course-state.yaml` (bloco `audit`; `content_hash` e `palavras_corpo` das aulas 07 e 08). Nenhuma figura foi alterada; nenhum ID de card ou de questão mudou; respostas e pontuação dos questionários ficaram iguais. Se o baralho já tiver sido importado no Anki, os cards fb026, fb027, fb028, fb040, fb049, fb092, fb130, fb147, fb148, fb150 e fb151 precisam ser editados à mão: reimportar o CSV pode não sobrescrever cards existentes.

**Pendências:** nenhuma neste módulo.

### Observações (terceira passagem)

- **Fora do escopo deste módulo, não corrigido:** o módulo 04 (já fechado), aula 05, diz que nas 10 classes polares "um sentido de uma direção difere do oposto", e o card `mineralogia-m04-fb049` diz que elas são "as únicas em que os dois sentidos de uma direção podem diferir". Pelo achado 26, isso é falso como escrito (o quartzo, da classe 32, tem direções polares e não é de classe polar); falta "única". Fica para a auditoria transversal ou para uma correção pontual do módulo 04.
