# Auditoria científica: Módulo 14 — Óptica física para mineralogia: luz, refração, polarização e interferência

**Auditado em:** 2026-10-07
**Material:** `curso-mineralogia/14-optica-fisica/` — as 8 aulas (`-aula-01` a `-aula-08`) e as figuras 1 a 8 (lidas pelo código SVG, com as coordenadas conferidas em Python); cruzamento com o módulo 04 (aula 06: definição dos sistemas, monoclínico "um único eixo 2 ou 2̄"), o módulo 12 (aula 07: atividade óptica do quartzo; aula 02: extinção ondulante) e o módulo 13 (aula 05: brilho × índice de refração, lâmina de 0,03 mm), e com o plano do módulo 15 (hub)
**Modo:** audit-and-fix
**Profundidade:** full, com recálculo em Python de todas as contas (f = c/λ, v = c/n, λ no meio, Snell, ângulos críticos, Brewster, Cauchy, desvio mínimo, Malus, amplitude e intensidade da superposição, retardo Γ e ordem m) e das coordenadas das oito figuras
**Escopo:** as 69 alegações dos rodapés (`OPT-*`, todas com `audit: pendente`) e as afirmações de risco do corpo: luz e espectro; índice de refração e Snell; ângulo crítico, reflexão total e refratômetro; dispersão, Fraunhofer, Cauchy e dispersão gemológica; polarização por absorção, Malus; Brewster, dupla refração, ω/ε, birrefringência e sinal; interferência, coerência, retardo; simetria × classe óptica e orientação da indicatriz. Questionário e baralho ainda não existem (não foram gerados nesta etapa).
**Veredito:** Requer correção → **correções aplicadas; estado final: Aprovado** (nenhum achado aberto)

## Resumo

🔴 1 erro · 🟠 8 imprecisões · 🟡 0 desatualizados · 🔵 0 sem fonte · ⚪ 1 controverso (10 achados, todos corrigidos)
Verificadas e corretas: 59 das 69 alegações dos rodapés (as outras 10 viraram achados ou receberam a propagação de um achado); 1 alegação nova (`OPT-TOT-PARCIAL-001`) criada para um achado do corpo. Total no rodapé após a auditoria: 70 alegações, 59 `verificado` e 11 `corrigido`, igual ao manifesto `.json`.

Os pontos que o autor marcou "a confirmar" passaram: a dispersão gemológica de zircão (0,039), quartzo (0,013), rubi/safira (0,018), fluorita (0,007) e esfalerita (0,156) bate em LibreTexts *Gemology* 7.16 e na Gem Society, além da tabela gemselect; Bartholin (1669) está certo; os grupos CO₃ da calcita ficam em planos perpendiculares a c; a orientação da indicatriz no monoclínico (um eixo ∥ b) e no triclínico (livre) está certa; ar 1,000293 e água 1,333 a 589 nm; o refratômetro gemológico lê até cerca de 1,81; as linhas C, D e F estão certas. A exceção foi Cauchy: a data de 1836 é a da memória (Buchwald), mas a Wikipedia dá 1830 (achado 3, ⚪).

O que não estava na lista do autor rendeu os achados mais sérios: a calcita com o índice ε atribuído à vibração **perpendicular** a c (🔴, achado 6); a birrefringência do coríndon montada cruzando extremos de amostras diferentes (0,004 a 0,013; real 0,008 a 0,009, achado 7); a coerência de O e E afirmada sem a condição de luz já polarizada (achado 8); o brilho metálico atribuído à reflexão parcial oblíqua, contra o módulo 13 (achado 1); e duas incoerências de notação entre aula e figura (achados 4 e 5).

**Contas conferidas (Python, 2026-10-07):**

| O quê | Resultado | Onde |
|---|---|---|
| f = c/λ em 589, 400, 700 nm | 5,090 × 10¹⁴; 7,49 × 10¹⁴; 4,28 × 10¹⁴ Hz ✔ | a01 |
| v no quartzo (n 1,544); λ de 589 nm no quartzo | 1,942 × 10⁸ m/s; 381,5 nm ✔ (589/381 = 1,546 ≈ 1,54) | a01 |
| v no diamante (2,4175) | 1,240 × 10⁸ m/s ✔ | a02 |
| Snell ar → diamante / quartzo, 50° | 18,47° / 29,75° (sen θ₂ = 0,3169 / 0,4961) ✔ | a02, fig 02 |
| Quartzo → ar a 25°; sen θ₂ a 55° | 40,73° (0,6525); 1,265 > 1 ✔ | a03, fig 03 |
| θc fluorita 1,433 / quartzo 1,544 / diamante 2,4175 | 44,25° / 40,37° / 24,43° ✔ | a03 |
| θc quartzo em água 1,33 / 1,333 | 59,47° / 59,69° ✔ ("59,5° a 59,7°") | a03 |
| Exemplo da aula 03 (1,544/1,333) | θc 59,69°; 55° → 71,59°; 70° → 1,0884 ✔ | a03 |
| Snell ar → diamante a 60°, 486 e 687 nm | 20,83° e 21,08°; diferença 0,25° ✔ | a04 |
| Cauchy com 486 e 687 nm do diamante | A = 2,37975; B = 13 144 nm²; n(589) = 2,41764 ✔ (com A e B arredondados, 2,41769) | a04, fig 04 |
| Cauchy extrapolada às linhas B e G | n(686,7) = 2,4076; n(430,8) = 2,4506; diferença 0,0430 (publicado 0,044) | a04 |
| n(486) − n(687) do diamante | 0,0278 ✔ | a04 |
| Desvio mínimo A = 60°, D = 37° | n = 1,4979 ✔ | a04 |
| Malus, I₀ = 100 | 50; 37,5; 25 (45°); 12,5; 0; três filtros 12,5 ✔ | a05, fig 05 |
| Brewster água 1,333 / vidro 1,5 / diamante 2,4175 | 53,12° (refratado 36,88°) / 56,31° (33,69°) / 67,53° ✔ | a06, fig 06 |
| Calcita: raio O a 40°; v(ω), v(ε) | 22,81°; 1,808 e 2,017 × 10⁸ m/s (11,6%) ✔ | a06 |
| Coríndon: ε − ω com os extremos cruzados | 0,004 e 0,013 (valores sem amostra real; achado 7) | a06 |
| Superposição Δ = λ/4 | amplitude 1,414 A; intensidade 2 (de 4) ✔ | a07, fig 07 |
| Γ e m, 30 µm, 589 nm | quartzo 270 nm, 0,458; calcita 5 160 nm, 8,76; razão 19,1 ✔ | a07 |
| m da calcita em 450, 550, 650 nm | 11,47; 9,38; 7,94 ✔ | a07 |
| Γ máximo gipsita / aragonita, 30 µm | 270 nm / 4 650 nm (7,9 λ) ✔ | a08 |

> [!note] Limite da verificação
> Mindat não foi consultado (403 frequente). Os PDFs do *Handbook of Mineralogy* foram lidos diretamente (calcite, quartz, corundum, rutile, halite, fluorite, sphalerite, diamond, gypsum, aragonite, zircon). Para a dispersão gemológica não há tabela normativa do IMA; valem as tabelas de gemologia (LibreTexts, Gem Society), que concordam entre si.

## Achados

### 🟠 1. O brilho metálico não vem da reflexão parcial oblíqua

**claim_id:** `OPT-TOT-PARCIAL-001` (alegação nova, criada para este achado)
**Tipo:** inconsistência interna (com o módulo 13, já fechado)
**Onde:** aula 03 · "Reflexão parcial, reflexão total e o ponto de vista do observador"
**Está escrito:** "(é o que faz o brilho metálico e a aparência de espelho da água vista rente)"
**Problema:** o aumento da refletância com a obliquidade explica o espelho da água vista de raspão, não o brilho metálico, que vem da absorção forte pelos elétrons livres (módulo 13, aula 05: "minerais com elétrons livres"; "metálico ... junto com a absorção forte"). O brilho dos minerais transparentes cresce com n na incidência normal, como o módulo 13 ensina.
**Correção aplicada:** "(é o que dá a aparência de espelho da água vista de raspão; o brilho de uma face de mineral transparente vem dessa mesma reflexão parcial e cresce com n, como no módulo 13; já o brilho metálico tem outra origem, a absorção forte pelos elétrons livres)"
**Fonte:** Hecht, *Optics* (equações de Fresnel; reflexão em metais); módulo 13, aula 05 (auditada em 2026-10-07) · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** —

### 🟠 2. Refratômetro: quem fixa o teto é o líquido de contato

**claim_id:** `OPT-TOT-REFRATOMETRO-001`
**Tipo:** omissão que gera erro
**Onde:** aula 03 · "Aplicação em mineralogia e gemologia"
**Está escrito:** "O instrumento só mede gemas de n menor que o do vidro, e por isso líquidos de contato e vidros de n elevado são usados (limite prático da ordem de 1,8 em refratômetros gemológicos comuns)."
**Problema:** o valor (~1,8) está certo, a causa sugerida não. Vidro e líquido precisam ter n maior que o da gema, e quem limita é, em geral, o líquido (n ≈ 1,79 a 1,81); a leitura vai até cerca de 1,81 ("OTL", *over the limit*, acima disso).
**Correção aplicada:** "O instrumento só mede gemas de n menor que o do vidro **e** que o do líquido de contato, e por isso ambos têm n elevado; na prática quem fixa o teto é, em geral, o líquido (n ≈ 1,79 a 1,81), e o refratômetro gemológico comum lê até cerca de 1,81. Diamante, zircão e moissanita ficam acima da escala."
**Fonte:** Skyjems, *Gemological refractometer* e *Contact liquid* (https://skyjems.ca/pages/encyclopedia-gemological-refractometer), e literatura do GIA sobre refratometria (limite de 1,81, "usually the liquid"), buscados em 2026-10-07 · **Nível:** geral
**Confiança:** confirmado
**Também aparece em:** "Fontes consultadas" da aula 03 (o "a confirmar" virou fonte)

### ⚪ 3. Data da fórmula de Cauchy

**claim_id:** `OPT-DIS-CAUCHY-001`
**Tipo:** controvérsia (datação divergente entre fontes)
**Onde:** aula 04 · "Uma fórmula empírica para o formato da curva"
**Está escrito:** "Em 1836, Cauchy propôs uma fórmula simples [...] É um ajuste empírico, não uma lei"
**Problema:** Buchwald (Caltech, 2011) dá a memória de Cauchy sobre a dispersão como de 1836; a Wikipedia (*Cauchy's equation*) data a fórmula de um artigo de 1830. Além disso, Cauchy a derivou de um modelo teórico (éter elástico); o uso como ajuste empírico é posterior. As contas (A = 2,3798; B = 13 144 nm²; n(589) = 2,4176) estão certas.
**Correção aplicada:** "Na década de 1830, Cauchy propôs [...]. A memória de Cauchy sobre a dispersão é de 1836; algumas fontes datam a fórmula de um trabalho de 1830. Cauchy a tirou de um modelo teórico hoje abandonado, e ela é usada como ajuste empírico, não como lei"
**Fonte:** Buchwald, J. Z., *Cauchy's Theory of Dispersion Anticipated by Fresnel* (https://authors.library.caltech.edu/records/2zz5m-59n26); Wikipedia, *Cauchy's equation*, lidas em 2026-10-07 · **Nível:** revisada por pares / geral
**Confiança:** em disputa
**Também aparece em:** rodapé da aula 04 (`claim:` ajustado); "Fontes consultadas" da aula 04

### 🟠 4. Dispersão gemológica: a aula manda nG − nB, mas o recap e a figura escreviam nB − nG

**claim_id:** `OPT-DIS-GEM-001`
**Tipo:** inconsistência interna
**Onde:** aula 04 · Recap relâmpago e Fontes consultadas; figura 4 (cabeçalho do gráfico de barras)
**Está escrito:** "Dispersão gemológica = n(686,7 nm) − n(430,8 nm), em módulo"; figura: "Dispersão gemológica (nB − nG)"
**Problema:** o corpo define "dispersão = nG − nB" e os Erros comuns dizem "Defina sempre nG − nB (positivo)"; o recap, a linha de fontes e a figura usavam a ordem oposta, que dá número negativo. A literatura gemológica escreve "intervalo B–G" e, às vezes, "nB − nG" com o valor em módulo (LibreTexts); a aula precisa ser coerente consigo mesma.
**Correção aplicada:** recap: "Dispersão gemológica = n(430,8 nm) − n(686,7 nm) = nG − nB (o "intervalo B–G")"; figura 4: "Dispersão gemológica (nG − nB, intervalo B–G)"; fontes: explicita que algumas fontes escrevem "nB − nG" em módulo.
**Fonte:** LibreTexts, *Gemology* 7.16 *Dispersion*; Gem Society, *Gemstone dispersion*, buscados em 2026-10-07 · **Nível:** geral
**Confiança:** confirmado
**Também aparece em:** `14-optica-fisica-fig-04-dispersao.svg`

### 🟠 5. Figura 5: título da lei de Malus com I₀

**claim_id:** `OPT-FIG05-MALUS-001`
**Tipo:** inconsistência interna
**Onde:** figura 5 · título
**Está escrito:** "Polarizador, analisador e lei de Malus: I = I₀ cos²θ"
**Problema:** na aula 05, I₀ é a intensidade da **luz natural** e a lei é I = I₁ cos²θ com I₁ = I₀/2; a própria aula lista "aplicar a lei de Malus à luz natural" como erro comum. O corpo da figura estava certo (I₀/2 após o polarizador; 0,75 · I₀/2 após o analisador a 30°).
**Correção aplicada:** "Polarizador, analisador e lei de Malus: I = I₁ cos²θ, com I₁ = I₀/2"
**Fonte:** Hecht, *Optics*; aula 05 do módulo · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** —

### 🔴 6. Calcita: o índice ε é o da vibração paralela a c, não perpendicular

**claim_id:** `OPT-DUPLA-VEL-001`
**Tipo:** erro factual
**Onde:** aula 06 · "Eixo óptico, birrefringência e sinal óptico"
**Está escrito:** "Na calcita, o raio ordinário tem v = c/1,658 ≈ 1,81 × 10⁸ m/s e a vibração perpendicular ao eixo c tem v = c/1,486 ≈ 2,02 × 10⁸ m/s, mais rápida."
**Problema:** é o contrário. A vibração perpendicular a c (no plano dos grupos CO₃, que a própria aula situa perpendiculares a c) é a ordinária, de índice ω = 1,658; ε = 1,486 é o da vibração **paralela** a c (luz caminhando perpendicular a c). A frase contradizia a própria aula (o raio O vibra perpendicular ao plano que contém o eixo óptico) e a aula 08 ("a direção c [...] seu índice é ε"; figura 8: "ε (paralelo ao eixo c)"). As velocidades numéricas estavam certas.
**Correção aplicada:** "Na calcita, o raio ordinário (que vibra perpendicular ao eixo c, no plano dos grupos CO₃) tem v = c/1,658 ≈ 1,81 × 10⁸ m/s, e a vibração extraordinária **paralela** ao eixo c (luz caminhando perpendicular a c) tem v = c/1,486 ≈ 2,02 × 10⁸ m/s, mais rápida."
**Fonte:** Hecht, *Optics*; Klein & Dutrow, *Manual of Mineral Science*; *Handbook of Mineralogy*, calcite (uniaxial −, ω 1,658, ε 1,486), https://www.handbookofmineralogy.org/pdfs/calcite.pdf, lido em 2026-10-07 · **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** rodapé da aula 06 (`claim:` corrigido)

### 🟠 7. Birrefringência do coríndon: os extremos foram cruzados

**claim_id:** `OPT-DUPLA-DADOS-001` (propagado a `OPT-ANI-EXEMPLO-001`)
**Tipo:** erro factual (valor fora da faixa aceita)
**Onde:** aula 06 · tabela de uniaxiais e Exemplo trabalhado (c); rodapé da aula 08
**Está escrito:** "| coríndon | 1,767–1,772 | 1,759–1,763 | de 0,004 a 0,013 | negativo |"; exemplo (c) com "ω = 1,767 e ε = 1,763" → "0,004", e "com os extremos do intervalo do Handbook (ω = 1,772, ε = 1,759) a birrefringência chegaria a 0,013"; rodapé da aula 08: "corindon (0,004 a 0,013) 120 a 390 nm"
**Problema:** os dois índices do coríndon sobem **juntos** com Fe e Cr, e a birrefringência real fica em 0,008 a 0,009 (GIA: 0,008 a 0,010). 0,004 e 0,013 saem de parear ω mínimo com ε máximo (ou o contrário), o que mistura amostras diferentes; o exemplo ensinava esse método errado.
**Correção aplicada:** tabela: "cerca de 0,008 a 0,009"; exemplo (c) com ω = 1,767 e ε = 1,759 → ε − ω = −0,008, sinal negativo, birrefringência 0,008, com a explicação de que os índices sobem juntos e de que o cruzamento de extremos (0,004; 0,013) não corresponde a cristal nenhum; rodapé da aula 08 sem o trecho do coríndon (que não estava no corpo).
**Fonte:** GIA, *Gem Encyclopedia: Ruby* (RI 1,762–1,770; birrefringência 0,008–0,010), https://www.gia.edu/ruby; Gem Society, *Table of refractive indices and double refraction*; *Handbook of Mineralogy*, corundum (ω 1,767–1,772; ε 1,759–1,763), lidos em 2026-10-07 · **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** aula 08 (rodapé, `OPT-ANI-EXEMPLO-001`)

### 🟠 8. O e E só são coerentes se a luz que entra já for polarizada

**claim_id:** `OPT-INT-COER-001`
**Tipo:** omissão que gera erro
**Onde:** aula 07 · "Condições para ver a interferência"
**Está escrito:** "Num cristal, a dupla refração faz exatamente isso: o raio O e o raio E vêm do mesmo feixe, e portanto são coerentes."
**Problema:** com luz natural isso é falso: as duas componentes perpendiculares da luz natural são incoerentes e não interferem nem quando levadas à mesma direção (3ª lei de Fresnel-Arago); componentes de uma mesma onda polarizada interferem (4ª lei). É por isso que o microscópio tem o polarizador **abaixo** da lâmina, e o aluno precisa dessa razão no módulo 15.
**Correção aplicada:** "Num cristal iluminado com luz **já polarizada** (o polarizador abaixo da lâmina, aula 05), a dupla refração faz exatamente isso: o raio O e o raio E são as duas componentes de uma mesma vibração de entrada, e portanto são coerentes. Com luz natural isso não basta: as duas componentes perpendiculares da luz natural não guardam fase fixa entre si e não interferem, mesmo levadas à mesma direção (leis de Fresnel-Arago). Por isso o microscópio polariza a luz **antes** do cristal."
**Fonte:** Wikipedia, *Fresnel–Arago laws* (https://en.wikipedia.org/wiki/Fresnel%E2%80%93Arago_laws); Hecht, *Optics*, lidas em 2026-10-07 · **Nível:** geral / revisada por pares
**Confiança:** confirmado
**Também aparece em:** "Fontes consultadas" da aula 07

### 🟠 9. Eixos ópticos: normais às seções circulares

**claim_id:** `OPT-ANI-UNI-001`
**Tipo:** erro factual (formulação)
**Onde:** aula 08 · "Os três casos, pela simetria"
**Está escrito:** "dois eixos ópticos (as duas direções em que a seção do elipsoide é circular, onde a luz não se divide)"
**Problema:** os eixos ópticos são as **normais** às duas seções circulares do elipsoide; a frase podia ser lida como direções contidas na seção circular.
**Correção aplicada:** "(as duas direções perpendiculares às duas seções circulares do elipsoide; a luz que caminha ao longo delas não se divide)"
**Fonte:** Nesse, *Introduction to Optical Mineralogy*; Nelson, S., *Biaxial minerals* (Tulane, EENS 2110), https://www2.tulane.edu/~sanelson/eens211/biaxial.htm · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** rodapé da aula 08 (`claim:` ajustado)

### 🟠 10. Monoclínico da classe m: não há eixo binário

**claim_id:** `OPT-ANI-ORIENT-001`
**Tipo:** omissão que gera erro
**Onde:** aula 08 · lista de orientação da indicatriz
**Está escrito:** "monoclínico: o único eixo binário (b) obriga um eixo do elipsoide a coincidir com b"
**Problema:** a regra (um eixo da indicatriz ∥ b) está certa e foi confirmada (Nelson; HoM gipsita Y = b), mas a classe m não tem eixo 2: o vínculo vem da normal ao plano de simetria (2̄), como o módulo 04 define o sistema ("um único eixo 2 ou 2̄"). Sem a ressalva, a justificativa é falsa para a classe m. O triclínico sem vínculo está certo.
**Correção aplicada:** "monoclínico: o único eixo binário (b; na classe m, que não tem eixo 2, o papel é da normal ao único plano de simetria, o eixo 2̄) obriga um eixo do elipsoide a coincidir com b"
**Fonte:** Nelson, *Biaxial minerals* (Tulane); *Handbook of Mineralogy*, gypsum (Y = b) e aragonite (X = c, Y = a, Z = b); módulo 04, aula 06 · **Nível:** revisada por pares / base de referência
**Confiança:** confirmado
**Também aparece em:** rodapé da aula 08 (`claim:` ajustado)

## Verificado e correto

| claim_id | Alegação (resumo) | Fonte | Confiança |
|---|---|---|---|
| `OPT-LUZ-ONDA-001`, `OPT-LUZ-C-001` | onda EM transversal, v = λf; c = 299 792 458 m/s exato | Hecht; BIPM/SI | confirmado |
| `OPT-LUZ-VIS-001` | visível 380–750 nm, com limites variáveis declarados | Wikipedia, *Light*; manuais | confirmado |
| `OPT-LUZ-FREQ-001`, `OPT-LUZ-MEIO-001` | 5,09 × 10¹⁴ Hz; λ no quartzo 381 nm | Python; HoM quartz | confirmado |
| `OPT-LUZ-ESCALA-001`, `OPT-LUZ-SODIO-001` | λ visível ≫ distância interatômica; 589 nm como referência | Klein & Dutrow; HoM diamond | confirmado |
| `OPT-REF-N-001`, `OPT-REF-LEIS-001`, `OPT-REF-PLACA-001` | n = c/v; leis da reflexão e de Snell; placa de faces paralelas | Hecht | confirmado |
| `OPT-REF-VALORES-001` | ar 1,0003; água 1,33; fluorita 1,433–1,448; quartzo 1,544/1,553; halita 1,5443; esfalerita 2,369; diamante 2,4175 | HoM; Wikipedia, *Refractive index* (ar 1,000293; água 1,333) | confirmado |
| `OPT-REF-VEL-001`, `OPT-REF-EXEMPLO-001`, `OPT-FIG02-SNELL-001` | velocidades; 18,5° e 29,7°; figura 2 | Python; código SVG | confirmado |
| `OPT-REF-DENS-001` | diamante 3,511, esfalerita 3,9–4,1 | HoM | confirmado |
| `OPT-TOT-CRIT-001`, `OPT-TOT-MEIO-001`, `OPT-TOT-DIAM-001` | ângulo crítico; dependência dos dois índices; diamante 24,4° | Hecht; HoM | confirmado |
| `OPT-TOT-VALORES-001`, `OPT-TOT-EXEMPLO-001`, `OPT-FIG03-TOTAL-001` | 44,3° / 40,4° / 24,4°; 59,7°; 71,6°; figura 3 | Python; código SVG | confirmado |
| `OPT-DIS-N-001`, `OPT-DIS-SNELL-001`, `OPT-DIS-INTERVALO-001` | diamante 2,4354/2,4175/2,4076; 0,25°; 0,0278 | HoM; Python | confirmado |
| `OPT-DIS-NORMAL-001` | dispersão normal e anômala | Hecht | confirmado |
| `OPT-DIS-FRAUN-001` | C 656,3; D 589,3; F 486,1 nm (e B 686,7, G 430,8) | Wikipedia, *Fraunhofer lines* | confirmado |
| `OPT-DIS-GEMAS-001` | zircão 0,039; quartzo 0,013; coríndon 0,018; fluorita 0,007; esfalerita 0,156 | LibreTexts *Gemology* 7.16; Gem Society | confirmado |
| `OPT-DIS-PRISMA-001`, `OPT-FIG04-DISP-001` | desvio mínimo 1,498; figura 4 na escala | Hecht; Python; código SVG | confirmado |
| `OPT-POL-NAT-001`, `OPT-POL-MALUS-001`, `OPT-POL-CALC-001`, `OPT-POL-MICRO-001` | luz natural e polarizada; Malus; 50/37,5/12,5/0 e 12,5; microscópio | Hecht; Python; Klein & Dutrow | confirmado |
| `OPT-POL-ABS-001` | folha H: PVA com iodo absorve E ∥ cadeias | Wikipedia, *Polaroid (polarizer)* | confirmado |
| `OPT-POL-HIST-001` | Malus: reflexão 1808, lei do cos² 1809 | Wikipedia, *Étienne-Louis Malus*; MacTutor/DSB | confirmado |
| `OPT-BRE-LEI-001`, `OPT-BRE-VALORES-001`, `OPT-BRE-OCULOS-001`, `OPT-FIG06-BREWDUPLA-001` | Brewster (s-polarizada, 90° entre refletido e refratado); 53,1°/56,3°/67,5°; óculos; figura 6 | Hecht; Britannica; Python; código SVG | confirmado |
| `OPT-DUPLA-FENOM-001` | Bartholin, 1669, calcita da Islândia | MacTutor, *Erasmus Bartholin* | confirmado |
| `OPT-DUPLA-OE-001`, `OPT-DUPLA-CALCITA-001` | O vibra ⊥ seção principal, E nela; CO₃ ⊥ c | Hecht; Klein & Dutrow | confirmado |
| `OPT-DUPLA-ISO-001`, `OPT-DUPLA-EXEMPLO-001` | isotrópicos; raio O a 22,8° | HoM; Python | confirmado |
| `OPT-INT-SUP-001`, `OPT-INT-RETARDO-001`, `OPT-INT-COR-001`, `OPT-FIG07-INTERF-001` | superposição; Γ = d·Δn; cores de interferência; figura 7 | Hecht; Klein & Dutrow; código SVG | confirmado |
| `OPT-INT-QZ-001`, `OPT-INT-CC-001`, `OPT-INT-LAMINA-001` | 270 nm; 5 160 nm; 30 µm | Python; Wikipedia, *Thin section* | confirmado |
| `OPT-INT-EXTINCAO-001` | cruzados a 45°: extinção em Γ = mλ, máximo em (m + ½)λ | Hecht (I ∝ sen²2φ · sen²(πΓ/λ)) | confirmado |
| `OPT-ANI-NEUMANN-001`, `OPT-ANI-ISO-001`, `OPT-ANI-RETARDO-001` | princípio de Neumann; isotropia; retardo por direção | Nye; Klein & Dutrow; Nesse | confirmado |
| `OPT-ANI-DADOS-001`, `OPT-ANI-SISTEMAS-001`, `OPT-ANI-TENSAO-001` | índices e sistemas da tabela; anisotropia por tensão | HoM (halite, fluorite, diamond, quartz, calcite, rutile, gypsum, aragonite, sphalerite) | confirmado |
| `OPT-FIG08-INDICATRIZ-001` | esfera, elipsoide prolato do quartzo (+), triaxial | código SVG; HoM | confirmado |

## Figuras

Todas as oito figuras foram lidas pelo código, e as coordenadas, conferidas em Python:

- **Fig. 1:** onda com λ = 220 px (cristas a 116, 336, 556 e 776; cota de λ de 115 a 335) e amplitude 45 px; faixa espectral de 380 a 750 nm a 2,162 px/nm (400 nm em x = 143,2; 700 nm em 791,9); cor de 589 nm amarelo-alaranjada ✔.
- **Fig. 2:** incidente e refletido a 50,0° da normal; refratado a 29,74°; arcos de raio constante (70 e 80 px) ✔. Lei da reflexão e de Snell respeitadas.
- **Fig. 3:** 24,98° → 40,7° (com refletido fraco a 25,0°); 40,37° → rasante; 55,0° com reflexão simétrica ✔.
- **Fig. 4:** pontos do HoM na escala (486 nm em 198,9/171,8; 589 em 329,4/272,0; 687 em 453,5/327,4); curva de Cauchy correta; barras proporcionais ✔. Cabeçalho corrigido (achado 4).
- **Fig. 5:** analisador girado 30°; vibração transmitida a 30°; curva cos²θ com pontos em 0,75, 0,5 e 0,25 ✔. Título corrigido (achado 5).
- **Fig. 6:** Brewster ar-vidro 56,31°/33,69°, 90° entre refletido e refratado; na calcita, incidência normal, raio O sem desvio e raio E desviado, os dois emergindo paralelos ao incidente ✔.
- **Fig. 7:** λ = 200 px; deslocamentos de 100 px (λ/2) e 50 px (λ/4); amplitudes da soma 48, 0 e 33,9 = 24√2 ✔.
- **Fig. 8:** esfera; elipsoide do quartzo alongado ao longo de c (positivo, ε > ω), com ε ∥ c; triaxial com γ > β > α ✔.

## Consistência interna e com o resto do curso

- **Módulo 13 (brilho × índice; lâmina de 0,03 mm):** coerente depois do achado 1; a lâmina de 30 µm e o n do quartzo e do diamante batem.
- **Módulo 12:** sem contradição. A aula 07 do módulo 12 cita a atividade óptica do quartzo (giro do plano de vibração); a aula 06 deste módulo diz que ao longo do eixo óptico a luz não se divide em dois raios lineares, o que é a aproximação usual; em 30 µm o giro é de cerca de 0,65° (21,7°/mm), desprezível. Não é achado.
- **Módulo 04:** a definição de monoclínico ("um único eixo 2 ou 2̄") motivou o achado 10.
- **Módulo 15:** é remetido por nome ("módulo 15"; na aula 08, wikilink ao hub `15-microscopio-petrografico-modulo`, que existe). A aula 07 enuncia em quatro linhas a condição de extinção entre polarizadores cruzados (Γ = mλ escuro, (m + ½)λ máximo), correta, e explicitamente a deixa para o módulo 15; não desenvolve o assunto (extinção reta/oblíqua, carta de Michel-Lévy, placas). Mantida.
- **Entre aulas:** depois do achado 6, a calcita (aula 06), a indicatriz (aula 08) e a figura 8 concordam sobre ε ∥ c; depois do achado 4, a aula 04 e a figura 4 concordam sobre nG − nB; depois do achado 5, a figura 5 usa a notação da aula 05.

## Correções aplicadas

**Aplicadas em:** 2026-10-07

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `OPT-TOT-PARCIAL-001` | 🟠 | Corrigido | aula-03 |
| `OPT-TOT-REFRATOMETRO-001` | 🟠 | Corrigido | aula-03 |
| `OPT-DIS-CAUCHY-001` | ⚪ | Corrigido (divergência explicitada) | aula-04 |
| `OPT-DIS-GEM-001` | 🟠 | Corrigido | aula-04, fig-04 |
| `OPT-FIG05-MALUS-001` | 🟠 | Corrigido | fig-05 |
| `OPT-DUPLA-VEL-001` | 🔴 | Corrigido | aula-06 |
| `OPT-DUPLA-DADOS-001` | 🟠 | Corrigido | aula-06, aula-08 (rodapé, `OPT-ANI-EXEMPLO-001`) |
| `OPT-INT-COER-001` | 🟠 | Corrigido | aula-07 |
| `OPT-ANI-UNI-001` | 🟠 | Corrigido | aula-08 |
| `OPT-ANI-ORIENT-001` | 🟠 | Corrigido | aula-08 |

Também foram atualizados: as seções "Fontes consultadas" das aulas 02 a 08 (os "a confirmar" viraram fonte conferida); os rodapés `alegacoes_auditaveis` (campo `audit:` das 69 alegações; `claim:` das 10 corrigidas ou ajustadas; 1 alegação nova, `OPT-TOT-PARCIAL-001`; `palavras_corpo` recontado nas aulas 03, 04, 06, 07 e 08; YAML dos rodapés validado); o gerador de figuras de rascunho (`figs14.py`), para que uma regeneração não reintroduza os achados 4 e 5; o hub do módulo (registro da auditoria); e o `course-state.yaml` (bloco `audit` do módulo 14, `content_hash` e `palavras_corpo` das aulas). O módulo **não** foi marcado como concluído: revisão didática, questionário e baralho seguem pendentes.

**Pendências:** nenhuma de natureza factual. Não há baralho importado no Anki a corrigir (o baralho do módulo ainda não existe).

## Observações fora do escopo factual

- As figuras 2, 3 e 6 usam ponto decimal nos ângulos ("29.7°", "40.4°", "56.3°") enquanto o texto usa vírgula.
- Na figura 7, a legenda inferior (y = 548) encosta nos vales da terceira curva de soma (que desce até y ≈ 554).
- Na figura 4, a curva de Cauchy começa em 420 nm e passa um pouco acima do topo do eixo (n > 2,45) até cerca de 435 nm.
- Aula 06: "o vidro e o opala" (opala é feminino).
- Ficam para a revisão didática.

## Segunda passagem (alegações da revisão didática)

**Auditado em:** 2026-10-07  ·  **Modo:** audit-and-fix  ·  **Profundidade:** full, escopo restrito
**Escopo:** as 8 alegações que a revisão didática registrou com `audit: pendente` (`OPT-LUZ-DIDAT-001`, `OPT-REF-DIDAT-001`, `OPT-TOT-DIDAT-001`, `OPT-DIS-DIDAT-001`, `OPT-POL-DIDAT-001`, `OPT-DUPLA-DIDAT-001`, `OPT-INT-DIDAT-001`, `OPT-ANI-DIDAT-001`) e o texto que a revisão alterou em volta delas, conforme `14-optica-fisica-revisao-didatica.md`: a analogia do terceiro filtro e a conferência (b) + (c) da aula 05; o vocabulário de uniaxial, o eixo c e a ligação de Brewster com o dipolo na aula 06; o radiano, o exemplo (a) e o recap com a regra invertida da aula 07; o aviso vibração × propagação, o uniaxial reescrito, as seções circulares, o "Antes de começar" e o exemplo do princípio na aula 08; as glosas das aulas 01 a 04. As oito figuras foram relidas pelo código do gerador (`figs14.py`, diferença conferida contra a cópia anterior à revisão), regeneradas num diretório à parte e comparadas byte a byte com as do disco (iguais), renderizadas (PyMuPDF) e passadas por um teste de sobreposição texto × texto e texto × linha (métrica da fonte Arial). As 10 correções da primeira passagem foram conferidas: nenhuma foi revertida.
**Veredito:** Requer correção → **correções aplicadas; estado final: Aprovado** (nenhum achado aberto)

🔴 0 · 🟠 2 · 🟡 0 · 🔵 0 · ⚪ 0  ·  Verificadas e corretas: 7 das 8 alegações pendentes por inteiro; a oitava (`OPT-ANI-DIDAT-001`) teve dois trechos corrigidos, que viraram alegações próprias (`OPT-ANI-QZSIM-001` e `OPT-ANI-ELIPSE-001`), e o resto dela passou. Total nos rodapés: 80 alegações, 67 `verificado` e 13 `corrigido`, igual ao manifesto `.json`.

**Contas refeitas em Python (2026-10-07):**

| O quê | Resultado | Onde |
|---|---|---|
| B = (2,4354 − 2,4076)/(1/486² − 1/687²); A = 2,4354 − B/486² | 13 144,28 nm² (texto 1,314 × 10⁴ ✔); 2,37975 (texto 2,3798 ✔) | a04 |
| n(589) com A e B exatos / arredondados | 2,41764 / 2,41769 (texto 2,4176 ✔) | a04 (c) |
| Curva da fig. 4 em 436, 486, 687, 700 nm | 2,4489 (y = 96,2; topo do eixo em 90 ✔); 2,4354; 2,4076; 2,4066 (y = 333,2) | fig. 4 |
| 0,156 / 0,044 | 3,55 ("mais de três vezes" ✔) | a04 |
| cos²30° + cos²60°; 50 × 0,75 e 50 × 0,25 | 1,000; 37,5 + 12,5 = 50 ✔ | a05 |
| θB + θ₂ para n = 1,333 / 1,5 / 2,4175 | 90,0000° nos três (base do argumento do dipolo) ✔ | a06 |
| 2π rad em graus; m do quartzo 270/589 | 360°; 0,458 ("quase meio λ" ✔) | a07 |
| m da calcita em 450, 550, 650 nm | 11,47; 9,38; 7,94 ✔ (regra invertida: vermelho quase extinto, azul quase máximo ✔) | a07 (c) |
| Invariância de uma elipse de semieixos 1 e 0,8 sob giros de 60°, 90°, 120°, 180°, 360° | só 180° e 360° ✔ (premissa do argumento, com a ressalva "não circular") | a08 |
| 1,94/3,00 | 0,647 ("≈ 0,65" ✔) | a01 |

### 🟠 11. O quartzo não "só tem eixo 3"

**claim_id:** `OPT-ANI-QZSIM-001` (novo; trecho separado de `OPT-ANI-DIDAT-001`)  ·  **Tipo:** inconsistência interna  ·  **Onde:** aula 08 · "O princípio: o índice não pode ser menos simétrico que o cristal"
**Está escrito:** "(o quartzo só tem eixo 3, mas seu índice é o mesmo em todas as direções do plano perpendicular a c)"
**Problema:** o quartzo-α é da classe 32: além do eixo 3 ao longo de c, tem três eixos 2 perpendiculares a c. Como escrito, a frase é falsa e contradiz o módulo 05 (aula 01, "trigonal, classe 32") e a própria verificação `OPT-ANI-SISTEMAS-001`. O ponto que a revisão queria ensinar (em torno de c o cristal só tem ordem 3, e o índice tem simetria de revolução) está certo.
**Correção aplicada:** "(o quartzo tem em c só um eixo 3, mas seu índice é o mesmo em todas as direções do plano perpendicular a c)"
**Fonte:** *Handbook of Mineralogy*, quartz (Point Group 3 2), https://www.handbookofmineralogy.org/pdfs/quartz.pdf, lido na primeira passagem (2026-10-07); Nye, *Physical Properties of Crystals* (princípio de Neumann; tensores de 2ª ordem uniaxiais nos sistemas trigonal, tetragonal e hexagonal)  ·  **Nível:** base de referência / revisada por pares  ·  **Confiança:** confirmado

### 🟠 12. "Uma elipse só volta a si mesma com giro de 180°" vale só para a elipse não circular

**claim_id:** `OPT-ANI-ELIPSE-001` (novo; trecho separado de `OPT-ANI-DIDAT-001`)  ·  **Tipo:** omissão que gera erro  ·  **Onde:** aula 08 · "Os três casos, pela simetria" (uniaxial)
**Está escrito:** "uma elipse só volta a si mesma com giro de 180°, então esse corte é um círculo"
**Problema:** o círculo é uma elipse e volta a si mesmo com qualquer giro; sem a ressalva, a premissa é falsa justamente para o caso que o argumento conclui, e o raciocínio parece circular. Com a ressalva, ele está certo (conferido em Python: só giros de 180° e 360° preservam uma elipse de semieixos desiguais). Também vale para os eixos de rotoinversão (4̄, 3̄, 6̄), porque a indicatriz é centrossimétrica; a aula não precisa dizer isso no nível dela.
**Correção aplicada:** "uma elipse alongada (não circular) só volta a si mesma com giro de 180°, então esse corte é um círculo"
**Fonte:** Nye, *Physical Properties of Crystals*, cap. 1 (tensores de 2ª ordem e simetria); cálculo em Python (2026-10-07)  ·  **Nível:** revisada por pares  ·  **Confiança:** confirmado

As duas edições somam 6 palavras: `palavras_corpo` da aula 08 de 1.638 para 1.644 (dentro da margem de ~1.645 aceita na revisão; duração mantida em ~28 min).

### Verificado e correto (segunda passagem)

| claim_id | O que foi conferido | Fonte | Confiança |
|---|---|---|---|
| `OPT-LUZ-DIDAT-001` | intensidade ∝ amplitude² (coerente com as aulas 05 e 07); na luz nada material sobe e desce e o raio segue reto num meio homogêneo; a altura da curva da fig. 1 é o valor de E, perpendicular ao raio; 1,94/3,00 ≈ 0,65 | Hecht, *Optics* (irradiância ∝ E₀²); Python | confirmado |
| `OPT-REF-DIDAT-001` | isotrópico = mesmas propriedades ópticas em todas as direções; ω e ε chamados ômega e épsilon | Nesse; Klein & Dutrow; HoM quartz | confirmado |
| `OPT-TOT-DIDAT-001` | mesa = faceta grande e plana do topo (*table*); moissanita = carbeto de silício (SiC), simulante de diamante desde 1998, n 2,648–2,691, acima da escala do refratômetro (coerente com `OPT-TOT-REFRATOMETRO-001`); o brilho de face polida vem da reflexão parcial (coerente com `OPT-TOT-PARCIAL-001`) | Skyjems, *Moissanite*; Nassau et al., *Synthetic moissanite: a new diamond substitute* (*Gems & Gemology*, 1997), por busca em 2026-10-07 | confirmado |
| `OPT-DIS-DIDAT-001` | passo de Cauchy (ver contas); "goniômetro de prisma" coerente com o goniômetro do módulo 04 (aula 01: "instrumento que mede ângulos entre faces"); esfalerita 0,156, "mais de três vezes" a do diamante (3,55); curva da fig. 4 contínua de 486 a 687 nm e tracejada fora (`stroke-dasharray` presente nos dois trechos), dentro do eixo | Python; Gem Society, *Sphalerite* ("three times higher"; "over three times"), por busca em 2026-10-07; código SVG | confirmado |
| `OPT-POL-DIDAT-001` | o filtro do meio, a 45°, entrega uma vibração e sempre transmite; o mineral entrega duas, defasadas, e entre polarizadores cruzados transmite I₁·sen²(2φ)·sen²(πΓ/λ): nada na extinção (φ = 0) nem com Γ = mλ; cos²30° + cos²60° = 1 porque cos 60° = sen 30° | Hecht, *Optics*; Python | confirmado |
| `OPT-DUPLA-DIDAT-001` | uniaxial com um só eixo óptico, coincidente com c; c posto ao longo do eixo 4, 6 ou 3 (módulo 05, aula 01: "c ao longo do eixo 6, 6̄, 3 ou 3̄"); Brewster pelo dipolo: os dipolos que geram o refratado oscilam na direção de polarização dele (perpendicular ao raio refratado), que no ângulo de Brewster é a direção do refletido, e um dipolo não irradia ao longo do próprio eixo | Wikipedia, *Brewster's angle* (explicação física pelos dipolos), por busca em 2026-10-07; Hecht, *Optics*; Python (θB + θ₂ = 90°) | confirmado |
| `OPT-INT-DIDAT-001` | 2π rad = 360°; recap com a regra invertida entre cruzados com o cristal a 45° (Γ = mλ escuro; (m + ½)λ máximo), a mesma de `OPT-INT-EXTINCAO-001`, coerente com o exemplo (c); "quase meio λ" para m = 0,458; "Somar os caminhos em vez de subtrair" descreve o erro certo | Hecht, *Optics*; Python | confirmado |
| `OPT-ANI-DIDAT-001` (sem os dois trechos acima) | a luz que caminha numa direção só vibra nas perpendiculares (simplificação usual: a rigor é o vetor D que é transversal à normal de onda, como no Nesse); ε é o índice da vibração ao longo de c, encontrado só pela luz que caminha perpendicular a c; a luz que caminha ao longo de c vê só ω; o elipsoide de três eixos desiguais tem exatamente duas seções centrais circulares, de raio β, e os eixos ópticos são as normais a elas; ortorrômbico "três direções perpendiculares com eixo 2 ou 2̄" e monoclínico "uma só direção com eixo 2 ou 2̄ (2̄ = plano)", iguais à tabela do módulo 04, aula 06 | Nelson, *Biaxial minerals* (Tulane, EENS 2110), https://www2.tulane.edu/~sanelson/eens211/biaxial.htm; Nesse; módulo 04, aula 06 | confirmado |

Também conferido no texto alterado, sem achado: o recap da aula 05 ("divide a vibração em duas, e quanto passa depende do atraso"); "Por que a luz se divide em duas?" e "a opala" (aula 06); a nota de que o 2̄ equivale a um plano, coerente com o achado 10 da primeira passagem (classe m); "Ler 'uniaxial' e 'biaxial' como número de eixos cristalográficos" e o erro comum novo sobre ε (aula 08).

### Figuras

Rótulos e geometria certos nas oito (valores iguais aos da primeira passagem; o deslocamento de 20 px da fig. 8 e a tela maior das figs. 4 e 7 não mudam nada conceitual: na fig. 8, ε continua no semieixo ∥ c e o elipsoide do quartzo alongado em c; na fig. 4, cabeçalho "nG − nB, intervalo B–G" mantido; na fig. 5, título com I₁). O teste de sobreposição achou o que o da revisão (só texto × texto) não pegava: **rótulos cortados pelos próprios raios**. Na fig. 2, "θ₁ = 50°" e o "50°" do refletido estavam sobre os raios incidente e refletido, e "θ₂ = 29,7°" era atravessado pelo refratado; na fig. 3, o raio de 25° atravessava "ar (n ≈ 1,000)" e "quartzo (n ≈ 1,544)", e as normais tracejadas cortavam os títulos das três colunas; na fig. 6, o refratado atravessava "33,7°". Um ângulo escrito em cima de um raio pode ser lido como pertencendo ao raio errado. **Ajuste aplicado** no `figs14.py` (cópia anterior `figs14.pre_aud2.py` no scratchpad), só de posição: fig. 2, θ₁ e 50° dentro dos ângulos, acima dos arcos, e θ₂ à direita do refratado; fig. 3, os rótulos dos meios em x = 180 e as normais começando em y = 110; fig. 6, "33,7°" dentro do ângulo, mais abaixo. Regeneradas as oito; mudaram em disco só as figs. 2, 3 e 6 (as outras cinco ficaram byte a byte iguais); XML válido; o teste de sobreposição passa limpo nas oito. Registro nos rodapés de `OPT-FIG02-SNELL-001`, `OPT-FIG03-TOTAL-001` e `OPT-FIG06-BREWDUPLA-001` (continuam `verificado`).

### Correções aplicadas (segunda passagem)

**Aplicadas em:** 2026-10-07

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `OPT-ANI-QZSIM-001` | 🟠 | Corrigido | aula-08 (corpo e rodapé) |
| `OPT-ANI-ELIPSE-001` | 🟠 | Corrigido | aula-08 (corpo e rodapé) |
| `OPT-LUZ-DIDAT-001`, `OPT-REF-DIDAT-001`, `OPT-TOT-DIDAT-001`, `OPT-DIS-DIDAT-001`, `OPT-POL-DIDAT-001`, `OPT-DUPLA-DIDAT-001`, `OPT-INT-DIDAT-001`, `OPT-ANI-DIDAT-001` | — | Verificado (`audit:` de "pendente" para "verificado") | aulas 01 a 08 (rodapé) |
| `OPT-FIG02-SNELL-001`, `OPT-FIG03-TOTAL-001`, `OPT-FIG06-BREWDUPLA-001` | — | Verificado; rótulos reposicionados | fig-02, fig-03, fig-06; aulas 02, 03, 06 (rodapé) |

Também atualizados: o manifesto `.json` (2 achados, 8 alegações verificadas, notas das três figuras, `summary`), `palavras_corpo` da aula 08 (1.644) e o `course-state.yaml` (bloco `audit` do módulo 14, `content_hash` das aulas e das figuras alteradas, `palavras_corpo` da aula 08). Questionário e baralho **não** foram gerados e o módulo **não** foi fechado.

**Pendências:** nenhuma de natureza factual. A revisão didática cita o texto antigo do quartzo e da elipse só como histórico (o relatório de revisão não foi editado). Não há baralho importado no Anki a corrigir.

## Auditoria de questionários e baralho

**Auditado em:** 2026-10-07  ·  **Modo:** audit-and-fix  ·  **Profundidade:** full, escopo restrito ao material derivado
**Material:** `14-optica-fisica-questionario-parcial-1.md` (Q1–Q12, 22 pts), `-parcial-2.md` (Q13–Q25, 29 pts), `-final.md` (Q26–Q40, 29 pts); `-flashcards-basic.csv` (fb001–fb171), `-flashcards-cloze.csv` (fc001–fc009) e `-flashcards.md`
**Critério:** todo gabarito, comentário de distrator e card tem de ser verdadeiro e rastreável a uma frase das aulas atuais (versões aprovadas nas duas passagens anteriores). Conferidos também: contas, cards com fato fora das aulas, versos que não respondem à frente, sintaxe Cloze, quase-duplicatas, distratores defensáveis, objetivo sem questão, IDs de aula (arquivo 04 = `a06`, 05 = `a04`, 06 = `a07`, 07 = `a05`), regressões dos erros já corrigidos (ω/ε da calcita, com ω perpendicular a c; dispersão nG − nB; "o quartzo só tem eixo 3"; elipse alongada; eixos ópticos como normais às seções circulares; brilho metálico por absorção; refratômetro limitado pelo líquido de contato; coerência de O e E só com luz polarizada; coríndon) e a lista "O que não cobrar" da revisão didática (c com nove algarismos, limites do visível, linhas de Fraunhofer, tabela de dispersão em números, teto de 1,81, índices de minerais sem enunciado, datas de Cauchy e Malus, coeficientes de Cauchy e dedução do prisma, nomes das leis de Fresnel-Arago, extinção, Michel-Lévy, sinal dos biaxiais, orientação detalhada da indicatriz).

*(Esta seção foi gravada em dois blocos: questionários primeiro, baralho depois.)*

**Veredito:** Requer correção → **correções aplicadas; estado final: Aprovado** (nenhum achado aberto)

🔴 0 · 🟠 8 · 🟡 0 · 🔵 0 · ⚪ 0  ·  3 achados nos questionários (13 a 15) e 5 no baralho (16 a 20). Nenhum veio de texto de aula: as aulas ficaram como estavam.

### Bloco 1: questionários

**Contas refeitas em Python (2026-10-07):**

| Onde | Conta | Resultado | Gabarito |
|---|---|---|---|
| P1 Q2 | λ = v/f = 2,00 × 10⁸ / 5,09 × 10¹⁴; 589 × 2/3; distratores 589 × 1,5 e 589/2 | 392,9 nm; 392,7 nm; 883,5; 294,5 | ✔ 393 nm |
| P1 Q3 | Snell ar → diamante, 60° da normal (30° da superfície); erro com 30° | 20,99°; 11,94° | ✔ |
| P1 Q4 | θc quartzo → ar; diamante → água; água → ar | 40,37°; 33,46°; 48,61° | ✔ |
| P1 Q11 | θc 1/1,544; 1,544 · sen 35°; 1,544 · sen 45°; θc 1,333/1,544; (1,544/1,333) · sen 45° | 40,37°; 0,8856 → 62,33°; 1,0918 (> 1); 59,69°; 0,8190 → 54,99° | ✔ |
| P1 Q12 | sen 50° / sen 30°; 1,665 − 1,640 | 1,5321; 0,025 | ✔ |
| P2 Q13 | 40 · cos² 30°; distratores 40 · cos 30°, 80 · cos² 30°, 80 · cos 30° | 30,0; 34,64; 60,0; 69,28 | ✔ |
| P2 Q14 | I₀ · ½ · cos² 45° · cos² 45° | 0,125 I₀ | ✔ 12,5% |
| P2 Q15 | 1,602 − 1,580; soma (distrator) | 0,022; 3,182 | ✔ |
| P2 Q23 | tg⁻¹ 1,40; refratado; soma; O da calcita a 30° | 54,46°; 35,54°; 90,00°; 17,55° | ✔ |
| P2 Q24 | 45 000 × 0,013; m em 589, 450, 650 nm; espessura dobrada | 585 nm; 0,993, 1,300, 0,900; 1 170 nm e 1,986 | ✔ (contas) |
| P2 Q24, armadilha | d em mm sem converter: 0,045 × 0,013 / 589 | 9,9 × 10⁻⁷ (ordem de 10⁻⁶; em metros daria 10⁻⁹) | ✘ "10⁻⁸" (achado 13) |
| P2 Q25 | 25 000 × 0,008; 25 000 × 0,040 | 200 nm; 1 000 nm | ✔ |
| F Q26 | θc 1/1,333; 90° − θc; Brewster da água e refratado | 48,61°; 41,39°; 53,12°; 36,88° | ✔ |
| F Q27 | θc 1,80/2,4175; 90° − θc | 48,12°; 41,88° | ✔ |
| F Q30 | tg⁻¹ 1,5; refratado; sen⁻¹(1/1,5) (distrator) | 56,31°; 33,69°; 41,81° | ✔ |
| F Q31 | c/1,486; c/1,658 | 2,019 × 10⁸; 1,809 × 10⁸ m/s | ✔ |
| F Q32 | cos²(1,5π) | 0 | ✔ |
| F Q33 | 60 000 × 0,009; 18 000 × 0,030 | 540 nm; 540 nm | ✔ |
| F Q38 | c/1,658; 589/1,658; c/589 nm; Snell a 35°; θc | 1,809 × 10⁸ m/s; 355,2 nm; 5,093 × 10¹⁴ Hz; 20,24°; 37,09° | ✔ (contas; enunciado ajustado, achado 14) |
| F Q39 | 200/2; × cos² 30°; × cos² 60°; fração | 100; 75; 18,75; 9,375% | ✔ |
| F Q40 | 40 000 × (1,622 − 1,590); ÷ 589 | 1 280 nm; 2,173 | ✔ |

**Cobertura e matrizes (refeitas item a item):** parcial 1 = 4 + 10 + 8 = **22** pts em 12 questões (`oa01`–`oa03`); parcial 2 = 13 + 8 + 8 = **29** pts em 13 questões (`oa04`–`oa06`); final = 2 + 4 + 3 + 6 + 5 + 9 = **29** pts em **15** questões, com os 6 objetivos; total **40 questões, 80 pontos**, igual ao `course-state.yaml` e ao hub. Nenhum objetivo sem questão. As distribuições cognitiva e por tipo conferem com os rótulos das questões (P1: 4/3/5/0, 7+2+1+2; P2: 1/5/7/0, 6+3+1+3; F: 0/6/8/1, 9+2+1+3). As notas de cobertura usam os IDs certos, com as exceções de metadado do achado 15.

**Regressões e lista "não cobrar":** nenhuma regressão. ε como índice da vibração **paralela** a c e ω perpendicular aparecem certos na P2 Q18 e Q22 e na F Q31 (que trata a troca como o erro a reconhecer); O e E coerentes só com luz polarizada (P2 Q16 e Q24 (e)); nG − nB (P1 Q10 e Q12, F Q28); eixo óptico e retardo zero (P2 Q25 (d), F Q37 e Q40 (d)). Nenhuma questão pede c com nove algarismos, limites do visível, linhas de Fraunhofer, números da tabela de dispersão (a P1 Q10 dá 0,156 e 0,044 no enunciado), o teto do refratômetro, datas, coeficientes de Cauchy, a dedução do prisma (a fórmula é dada), extinção além da existência das duas regras (P2 Q20), Michel-Lévy, sinal dos biaxiais ou orientação da indicatriz. As leis de Fresnel-Arago aparecem só pelo nome num comentário de gabarito (P2 Q16), não como resposta. Todos os índices de minerais vêm no enunciado. O único fato de fora do módulo usado num gabarito, a clivagem octaédrica do diamante e da fluorita (F Q36), está no módulo 13, aula 02 (tabela de clivagens, {111} perfeita, auditada).

**Distratores:** nenhum defensável. Os mais próximos foram conferidos: P1 Q5 d) ("mesma direção, sem deslocamento e sem atraso") falha mesmo na incidência normal, pelo atraso; P2 Q16 c) ("O e E só existem com luz polarizada") é falso pela aula 06 (a calcita dá duas imagens com luz comum); F Q28 c) fica falso pela "mudança de sinal".

#### 🟠 13. P2 Q24: a armadilha dava a ordem de grandeza errada

**claim_id:** `QST-M14-CALC-001`  ·  **Tipo:** erro factual (conta)  ·  **Onde:** questionário parcial 2 · Q24, nota "Armadilha" do gabarito
**Está escrito:** "esquecer de converter mm para nm dá um m absurdo (da ordem de 10⁻⁸)"
**Problema:** com d em mm e λ em nm, m = 0,045 × 0,013 / 589 = 9,9 × 10⁻⁷, ordem de 10⁻⁶ (em metros seria 10⁻⁹; nenhuma escolha de unidade dá 10⁻⁸). O aluno que refizesse a conta do erro não acharia o número do gabarito.
**Correção aplicada:** "esquecer de converter mm para nm dá um m absurdo (0,045 × 0,013 / 589 ≈ 10⁻⁶)"
**Fonte:** Python, 2026-10-07; aula 07 (`a05`), Erros comuns ("Misturar unidades")  ·  **Confiança:** confirmado

#### 🟠 14. F Q38: "a velocidade da luz" na calcita tratada como única

**claim_id:** `QST-M14-CALCITA-001`  ·  **Tipo:** omissão que gera erro  ·  **Onde:** questionário final · Q38, enunciado e gabarito (a), (d)
**Está escrito:** "num cristal de calcita (n = 1,658, valor de ω). (a) Calcule a velocidade da luz no cristal."; gabarito: "v = c/n = 3,00 × 10⁸ / 1,658 = 1,81 × 10⁸ m/s"
**Problema:** o módulo ensina que a calcita tem duas vibrações de velocidades diferentes (aula 06: 1,81 e 2,02 × 10⁸ m/s), e a Q31 do mesmo questionário cobra a outra. "A velocidade da luz no cristal", com o n entre parênteses, faz parecer que há uma só, e o gabarito reforçava isso. As contas estavam certas.
**Correção aplicada:** enunciado: "Considere só a vibração do raio ordinário (n = ω = 1,658); a calcita tem dois índices, e a outra vibração anda em outra velocidade. (a) Calcule a velocidade dessa vibração no cristal."; gabarito (a): "v = c/ω = 3,00 × 10⁸ / 1,658 = 1,81 × 10⁸ m/s, a do raio ordinário; a vibração paralela a c (ε = 1,486) andaria a 2,02 × 10⁸ m/s, como na Q31"; (d): "Para o raio ordinário, sen θc = ...". Resposta e pontos inalterados.
**Fonte:** aula 06 (`a07`), "Eixo óptico, birrefringência e sinal óptico" (velocidades na calcita, já corrigidas pelo achado 6)  ·  **Confiança:** confirmado

#### 🟠 15. Comentários e metadados dos questionários

**claim_id:** `QST-M14-META-001`  ·  **Tipo:** inconsistência interna  ·  **Onde:** P1 Q7 (comentário), "Cobertura" e "Autodiagnóstico" da P1 e do final; matriz da P2; nota de integração e Q37 (3) do final
**Está escrito:** P1 Q7: "aulas 06 e 08 do arquivo"; P1: "aula 03, `a03`: Q4, Q9, Q10 (parte), Q11" e "Questões 4, 9, 10, 11" (aula 03); P2, matriz: Q16 na coluna "Lembrar" de `oa05`; final: "37 (aulas 05 a 08)", "aula 05, ID `a04`: Q39, Q37", "Questões 39, 37" (aula 05); Q37 (3): "(isótropo para aquele corte)"
**Problema:** a Q7 citava aulas só pelo número do arquivo, contra o critério declarado (ID e arquivo juntos, 🔵 2 da revisão didática); a Q10 da P1 não usa nada da aula 03 (é toda da aula 04), e a Q37 do final nada da aula 05; a Q16 é rotulada "explicar" no enunciado e contada como "explicar" na distribuição cognitiva, mas estava em "lembrar" na matriz; "isótropo para aquele corte" pode ser lido como se o corte fosse isotrópico, quando a aula 08 diz que ele "parece 'isotrópico'".
**Correção aplicada:** P1 Q7: "aulas 06 e 08, IDs `a07` e `a08`"; Q10 retirada da cobertura e do autodiagnóstico da aula 03 (que fica com Q4, Q9, Q11); P2: Q16 movida para "Explicar" (pontos de `oa05` inalterados, 8); final: "37 (aulas 06 a 08)", e a aula 05 fica com a Q39; Q37 (3): "(o corte perpendicular ao eixo óptico parece isotrópico entre polarizadores cruzados, embora o mineral não seja)".
**Fonte:** aulas 03, 04, 05 e 08 (`a03`, `a06`, `a04`, `a08`); revisão didática, 🔵 2  ·  **Confiança:** confirmado

**Arquivos alterados neste bloco:** `14-optica-fisica-questionario-parcial-1.md`, `-parcial-2.md`, `-final.md` (gabaritos e metadados acima; o registro de geração de cada um ganhou uma nota da auditoria). Nenhuma resposta, ID de questão ou pontuação mudou. Nenhuma aula precisou de ajuste.

### Bloco 2: baralho

**Conferência:** os 171 Basic e os 9 Cloze foram lidos um a um contra as aulas atuais (incluídas as seções Fontes). Contas dos cards refeitas em Python: fb085 (I₀/2 · cos² 45° · cos² 45° = 0,125 I₀ ✔) e fc008 (30 000 × 0,009 = 270 nm; 30 000 × 0,172 = 5 160 nm ✔). Contagem por aula conferida (17, 17 + 1, 16 + 1, 20 + 1, 22 + 1, 25 + 1, 25 + 3, 29 + 1, pela ordem dos arquivos; 171 + 9 = 180), igual ao `flashcards.md` e ao `course-state.yaml`. As colunas `aula` e `objetivo` dos CSVs usam os IDs certos (arquivo 04 = `a06`, 05 = `a04`, 06 = `a07`, 07 = `a05`; os cards de retardo por direção, fb164–fb166, em `a08`/`oa06`, como na aula). A tabela do `flashcards.md` confere campo a campo com os CSVs (180 de 180, por script, depois das correções). Sintaxe Cloze válida (c1 a c3, contíguos, sem chaves internas).

**Regressões:** nenhuma nos cards que tratam dos erros já corrigidos: fb110 (ε 1,486 da vibração paralela a c; ω 1,658 perpendicular, no plano dos CO₃), fb154 e fb109 (a luz que caminha ao longo de c vê só ω), fb145 ("em c ele tenha só um eixo 3"), fb152 ("elipse não circular"), fb159 (eixos ópticos perpendiculares às seções circulares), fb047 (brilho metálico pela absorção dos elétrons livres), fb050 (o líquido fixa o teto, sem número), fb061 e fb062 (nG − nB), fb116 (coríndon só como o erro de cruzar extremos). A exceção foi a coerência de O e E (achado 17).

**Fatos fora das aulas:** nenhum card fabricado. Os versos que vão além da frase literal da aula são paráfrases dela (fb030, "só o seno é proporcional a 1/n", da aula 02, Erros comuns; fb055, "menos de 1°", dos 0,25° da aula 04).

#### 🟠 16. Itens da lista "não cobrar" no baralho: valores de dispersão e coeficientes de Cauchy

**claim_id:** `FLC-M14-NAOCOBRAR-001`  ·  **Tipo:** inconsistência interna (com a revisão didática e com os critérios declarados no próprio `flashcards.md`)  ·  **Onde:** fc003; fb059
**Está escrito:** fc003: "Dispersão gemológica (nG − nB): diamante {{c1::0,044}}; esfalerita {{c2::0,156}}; fluorita {{c3::0,007}}." (extra: "o que importa é a ordem relativa"); fb059: "Como se acham A e B de Cauchy com dois pares (λ, n)?" / "Subtraindo as duas equações, A desaparece e dá B; depois se calcula A."
**Problema:** a revisão didática manda não cobrar a tabela de dispersão em números ("cobrar só a ordem relativa") nem os coeficientes A e B de Cauchy; o próprio `flashcards.md` declarava "nenhum card pede [...] coeficientes [...] de Cauchy". O fc003 pedia exatamente três números para decorar, e o extra o contradizia; o fb059 pedia o procedimento de cálculo dos coeficientes. Os valores em si estão certos (achados anteriores).
**Correção aplicada:** fc003: "Dispersão gemológica, da maior para a menor: {{c1::esfalerita}} > {{c2::diamante}} > zircão > rubi e safira > {{c3::quartzo}} > fluorita." (extra: "Só a ordem relativa importa; os valores de nG − nB ficam na tabela da aula 04, sem decorar."). Como a ordem passou ao fc003, o fb064 (que pedia a mesma ordem) foi reaproveitado para outro fato da aula 04: "Por que as lentes do microscópio precisam corrigir a dispersão?" / "Sem correção, a dispersão borra a imagem com franjas de cor." (aula 04, "O que a dispersão faz na prática"). fb059: "Por que o índice de refração de um mineral deve vir sempre acompanhado do comprimento de onda?" / "Porque n depende de λ (dispersão): um n 'do diamante' é sempre n(λ), e o valor muda com a cor." (aula 04, Erros comuns; tag de `cauchy` para `dispersao`). O fb056 (forma da fórmula de Cauchy) e o fb058 (interpolar, não extrapolar) ficam: não pedem coeficientes.
**Fonte:** revisão didática, "O que não cobrar"; aula 04 (`a06`)  ·  **Confiança:** confirmado

#### 🟠 17. fb129: O e E apresentados como coerentes sem a condição de luz polarizada

**claim_id:** `FLC-M14-COER-001` (regressão de `OPT-INT-COER-001`, achado 8)  ·  **Tipo:** omissão que gera erro  ·  **Onde:** fb129
**Está escrito:** "Por que o raio O e o raio E de um cristal são coerentes?" / "São as duas componentes de uma mesma vibração polarizada de entrada."
**Problema:** a frente afirma, sem condição, que O e E são coerentes, que é a frase que o achado 8 corrigiu na aula 07: com luz natural eles não são. Num card revisado dezenas de vezes, a frente é o que fica; o "polarizada" escondido no verso não desfaz a premissa.
**Correção aplicada:** "Por que, com luz que entra já polarizada, o raio O e o raio E de um cristal são coerentes?" / "São as duas componentes de uma mesma vibração de entrada, e por isso mantêm fase fixa entre si." O fb130 (por que o microscópio polariza antes do cristal: com luz natural as componentes não interferem) já estava certo e fica.
**Fonte:** aula 07 (`a05`), "Condições para ver a interferência"; Wikipedia, *Fresnel–Arago laws*, já citada no achado 8  ·  **Confiança:** confirmado

#### 🟠 18. fb160: "só duas seções centrais são circulares" sem dizer que é o biaxial

**claim_id:** `FLC-M14-SECAO-001`  ·  **Tipo:** omissão que gera erro  ·  **Onde:** fb160
**Está escrito:** "O que é uma seção circular do elipsoide?" / "O corte do elipsoide por um plano central que dá um círculo; só duas seções centrais são circulares."
**Problema:** a aula 08 diz isso do elipsoide de três eixos desiguais. Como escrito, vale para qualquer indicatriz, e é falso para a do uniaxial (uma só seção central circular, a perpendicular a c) e para a esfera (todas). O card isolado, fora da sequência, perde o contexto do biaxial.
**Correção aplicada:** "O que é uma seção circular da indicatriz de um biaxial, e quantas há?" / "O corte do elipsoide de três eixos desiguais por um plano central que dá um círculo; são só duas."
**Fonte:** aula 08 (`a08`), "Os três casos, pela simetria"; Nelson, *Biaxial minerals* (Tulane, EENS 2110), já citado na segunda passagem  ·  **Confiança:** confirmado

#### 🟠 19. fc002: a lacuna c3 vinha respondida no próprio texto

**claim_id:** `FLC-M14-CLOZE-001`  ·  **Tipo:** inconsistência interna (Cloze malformado)  ·  **Onde:** fc002
**Está escrito:** "Ângulo crítico, indo de n maior para n menor: sen θc = {{c1::n₂}} / {{c2::n₁}}, com {{c3::n₁ > n₂}}."
**Problema:** "indo de n maior para n menor" fica visível no card da lacuna c3, que pede "n₁ > n₂": a resposta está na pergunta. Além disso, c3 repetia o fato do fb039 ("Do meio de n maior para o de n menor").
**Correção aplicada:** "Ângulo crítico, para a luz que vai do meio 1 para o meio 2: sen θc = {{c1::n₂}} / {{c2::n₁}}." (extra: "Só existe se n₁ > n₂; sai da lei de Snell com θ₂ = 90°."). O Cloze passa de 3 para 2 lacunas (o Anki gera um card a menos na importação).
**Fonte:** aula 03 (`a03`), "Ângulo crítico"  ·  **Confiança:** confirmado

#### 🟠 20. Quase-duplicatas no baralho

**claim_id:** `FLC-M14-DUPLIC-001`  ·  **Tipo:** inconsistência interna  ·  **Onde:** fc001 × fb020 × fb021; fc005 × fb096; fc007 × fb134; fb037 × fb041; fb075 × fb088; fb109 × fb155
**Está escrito:** fc001 "{{c3::normal}}", o mesmo fato de fb021 ("Com a normal.") e do verso de fb020 ("todos os ângulos [...] se medem em relação a ela"); fc005 "em que n₂ é o índice do meio {{c3::refletor}}", igual a fb096 ("Em tg θB = n₂/n₁, o que é n₂?" / "O índice do meio refletor"); fb134 "De que dois fatores depende o retardo?" / "Da espessura da lâmina e da birrefringência", a fórmula do fc007 em palavras; fb037 terminava com "nele o refratado sai a 90° da normal", a resposta de fb041; fb088 ("Que erro comum envolve a imagem do polarizador como grade de fendas?" / "as moléculas absorvem a componente ao longo delas e deixam passar a perpendicular") repetia fb075; fb109 ("Que luz vê só o índice ω num uniaxial?" / "A que caminha ao longo do eixo óptico [...]: ela não se divide") e fb155 ("Por que a luz que caminha ao longo do eixo óptico de um uniaxial não se divide?" / "[...] o índice é um só, ω") pediam o mesmo fato nos dois sentidos.
**Problema:** contraria os critérios declarados no `flashcards.md` ("Um fato por card"; "nenhum Basic repete o fato de um Cloze") e faz cards competirem na revisão.
**Correção aplicada:** fc001 sem a lacuna c3 ("... sen θ₂ (ângulos medidos a partir da normal)."); fb020 só com a definição ("O que é a normal, numa interface?" / "A reta perpendicular à interface no ponto onde o raio chega."); fc005 sem a lacuna c3 ("Lei de Brewster: tg θB = {{c1::n₂}} / {{c2::n₁}}.", extra "n₁: meio de onde a luz vem; n₂: meio refletor."); fb037 sem a frase final; fb134 reaproveitado: "Um retardo grande implica birrefringência grande?" / "Não: depende também da espessura; uma lâmina espessa e pouco birrefringente pode igualar uma fina e muito birrefringente." (aula 07, "O que não concluir"); fb088 reaproveitado: "Os polarizadores ideais usados nas contas existem?" / "Não: filtros reais absorvem algo da luz paralela ao eixo e deixam passar algo da perpendicular; as contas usam polarizadores ideais." (aula 05, "O que não concluir"); fb155 reaproveitado: "Como aparece, entre polarizadores cruzados, uma lâmina cortada perpendicular a um eixo óptico?" / "Escura (Γ ≈ 0), como se fosse isotrópica, embora o mineral seja anisotrópico: o retardo depende do corte." (aula 08, "O que não concluir"; tag `retardo`). fc001 e fc005 passam de 3 para 2 lacunas.
**Fonte:** aulas 02, 03, 05, 06, 07 e 08  ·  **Confiança:** confirmado

### Verificado e correto (terceira passagem)

| claim_id | O que foi conferido | Fonte | Confiança |
|---|---|---|---|
| `QST-M14-CALC-002` | todas as contas dos gabaritos (tabela do bloco 1) e dos cards fb085 e fc008; só a armadilha da P2 Q24 tinha erro | Python, 2026-10-07 | confirmado |
| `QST-M14-GABAR-001` | os 40 gabaritos e os comentários de distratores, contra as aulas atuais; nenhum distrator defensável; a clivagem {111} do diamante e da fluorita (F Q36) rastreada ao módulo 13, aula 02 | aulas 01 a 08; módulo 13, aula 02 | confirmado |
| `QST-M14-OA-001` | 6 de 6 objetivos com questão no final; parciais com `oa01`–`oa03` e `oa04`–`oa06`; matrizes de 22, 29 e 29 pontos (final: 15 questões); total 40 q e 80 pts; distribuições cognitiva e por tipo | course-state.yaml; matrizes | confirmado |
| `QST-M14-NAOCOBRAR-001` | nenhuma questão cobra c com nove algarismos, visível, Fraunhofer, tabela de dispersão em números, teto de 1,81, datas de Cauchy e Malus, coeficientes de Cauchy, dedução do prisma, nomes das leis de Fresnel-Arago, extinção além da existência das duas regras, Michel-Lévy, sinal dos biaxiais ou orientação da indicatriz; índices sempre no enunciado | revisão didática, "O que não cobrar" | confirmado |
| `FLC-M14-RASTRO-001` | 180 cards rastreados a frases das aulas; nenhum fato fabricado; versos respondem às frentes; IDs de aula e objetivos; contagens por aula; md × CSV 180/180 | aulas 01 a 08; CSVs | confirmado |
| `FLC-M14-REGRESSAO-001` | ε ∥ c e ω ⊥ c (fb110, fb154, fb109); quartzo com um só eixo 3 em c (fb145); elipse não circular (fb152); eixos ópticos normais às seções circulares (fb159); brilho metálico por absorção (fb047); teto do refratômetro pelo líquido (fb050); nG − nB (fb061, fb062); coríndon só como erro (fb116) | achados 1, 2, 4, 6, 7, 9, 11, 12 | confirmado |

### Correções aplicadas (terceira passagem)

**Aplicadas em:** 2026-10-07

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `QST-M14-CALC-001` | 🟠 | Corrigido | questionario-parcial-2 (Q24) |
| `QST-M14-CALCITA-001` | 🟠 | Corrigido | questionario-final (Q38) |
| `QST-M14-META-001` | 🟠 | Corrigido | questionario-parcial-1 (Q7, Cobertura, Autodiagnóstico), questionario-parcial-2 (matriz), questionario-final (nota de integração, Q37, Cobertura, Autodiagnóstico) |
| `FLC-M14-NAOCOBRAR-001` | 🟠 | Corrigido | flashcards-cloze.csv e flashcards.md (fc003); flashcards-basic.csv e flashcards.md (fb059, fb064) |
| `FLC-M14-COER-001` | 🟠 | Corrigido | flashcards-basic.csv e flashcards.md (fb129) |
| `FLC-M14-SECAO-001` | 🟠 | Corrigido | flashcards-basic.csv e flashcards.md (fb160) |
| `FLC-M14-CLOZE-001` | 🟠 | Corrigido | flashcards-cloze.csv e flashcards.md (fc002) |
| `FLC-M14-DUPLIC-001` | 🟠 | Corrigido | flashcards-basic.csv, flashcards-cloze.csv e flashcards.md (fb020, fb037, fb088, fb134, fb155, fc001, fc005) |

Também atualizados: o registro de geração dos três questionários, o cabeçalho, os critérios e o histórico do `flashcards.md`, o manifesto `.json` (8 achados, 6 alegações verificadas, contagens) e o `course-state.yaml` (bloco `audit`). Nenhuma aula e nenhuma figura foram alteradas (os `content_hash` das aulas continuam válidos); nenhum ID de card ou de questão mudou; respostas e pontuação dos questionários ficaram iguais; as contagens do baralho (171 + 9) também. Se o baralho já tiver sido importado no Anki, os cards fb020, fb037, fb059, fb064, fb088, fb129, fb134, fb155, fb160, fc001, fc002, fc003 e fc005 precisam ser editados à mão (e os cards c3 de fc001, fc002 e fc005, apagados): reimportar o CSV pode não sobrescrever cards existentes.

**Pendências:** nenhuma de natureza factual. Fica, não bloqueante e fora do escopo da auditoria, o 🔵 3 da revisão didática (acrescentar 05 e 13 a `prerequisites` do módulo 14 é decisão curricular do usuário).

### Observações (terceira passagem)

- Fora do escopo factual: a F Q26 (calcular o ângulo crítico da água) está rotulada "explicar" e contada assim na matriz e na distribuição cognitiva; pela tarefa, seria "aplicar". É coerente dentro do questionário e não muda pontos; fica para a revisão didática, se for o caso.
