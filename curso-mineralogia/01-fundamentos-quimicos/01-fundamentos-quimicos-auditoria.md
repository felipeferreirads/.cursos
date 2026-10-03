# Auditoria científica: Módulo 01 — Fundamentos químicos

**Auditado em:** 2026-09-30
**Material:** `curso-mineralogia/01-fundamentos-quimicos/` — as 6 aulas (`01-fundamentos-quimicos-aula-01` a `-aula-06`)
**Modo:** audit-and-fix
**Profundidade:** full (com checagem de consistência com curso-geologia, módulo 04, aulas 01–02)
**Escopo:** todas as alegações listadas nos rodapés `alegacoes_auditaveis` (43 claim_ids originais, incluindo todos os campos `incerteza:`), mais as afirmações de risco do corpo que o autor não listou (8 claim_ids novos). Todos os cálculos derivados foram refeitos com as massas atômicas CIAAW 2024. Não há questionário nem baralho do módulo, então não houve material derivado a propagar.
**Veredito:** Requer correção → **correções aplicadas; estado final: Aprovado** (nenhum achado aberto)

## Resumo

🔴 1 erro · 🟠 12 imprecisões · 🟡 0 desatualizados · 🔵 0 sem fonte · ⚪ 1 controverso
Verificadas e corretas: 37 alegações.

Pontos pedidos explicitamente que passaram: massas atômicas (as 12 coincidem com a CIAAW 2024), massa molar e % em óxidos da forsterita, hematita, pirita, gipsita, fatores Fe/FeO e Fe/Fe₂O₃, raios de Shannon do Fe²⁺/Fe³⁺, distâncias do grafite, pressão no centro da Terra e gradiente crustal, Si–O ≈ 1,62 Å, atribuição Fe²⁺ + S₂²⁻ na pirita, fórmula de Pauling e seus percentuais. Os problemas se concentraram em modelos conceituais (4s/3d, "χ baixo" do ouro, "silicatos são duros", clivagem do diamante) e em alguns números de borda.

## Achados

### 🔴 1. Manganês com "o máximo possível" de elétrons desemparelhados num átomo

**claim_id:** `QUI-CONF-DESEMP-001`
**Tipo:** erro factual
**Onde:** aula 01 · Exemplo trabalhado ("Para comparar")
**Está escrito:** "cinco d, um em cada orbital, **5 desemparelhados** (o máximo possível num átomo)."
**Problema:** falso. O cromo no estado fundamental (3d⁵ 4s¹, termo ⁷S) tem 6 elétrons desemparelhados; o európio (4f⁷ 6s², ⁸S) tem 7; o gadolínio (4f⁷ 5d¹ 6s², ⁹D) tem 8. Cinco é o máximo de uma **subcamada d**, não de um átomo.
**Correção proposta:** "(o máximo que uma subcamada d comporta; átomos como o cromo, com 6, e o gadolínio, com 8, têm mais)."
**Fonte:** NIST Atomic Spectra Database, *Ground States and Ionization Energies* (https://physics.nist.gov/PhysRefData/ASD/ionEnergy.html), consultado em 2026-09-30  ·  **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** só na aula 01 (o recap "Mn = 5 desemparelhados" está correto e foi mantido).

### 🟠 2. "O 4s tem energia menor que o 3d nos átomos neutros"

**claim_id:** `QUI-ORB-ENERGIA-001`
**Tipo:** confusão de escopo (modelo mental errado)
**Onde:** aula 01 · A ordem de preenchimento
**Está escrito:** "O 4s tem energia menor que o 3d nos átomos neutros, apesar de ser de camada maior. Mas, quando o átomo vira íon, é o 4s que perde elétrons primeiro."
**Problema:** vale para K e Ca, não para os metais de transição. Do Sc em diante, o orbital 3d fica abaixo do 4s; a configuração 4s² continua sendo a de menor energia **total** por causa da repulsão entre elétrons. O texto ensinava a explicação contraditória ("o 4s é mais baixo, mas sai primeiro") que a literatura de ensino de química aponta como falha, e isso é justamente o caso do ferro, que é o foco do módulo.
**Correção proposta (aplicada):** explicar que 4s < 3d no K e no Ca; nos metais de transição 3d < 4s e o 4s² persiste pela repulsão eletrônica; por isso o 4s ioniza primeiro; Madelung prevê a configuração do átomo neutro, não um ranking fixo de energia dos orbitais.
**Fonte:** Scerri, E. (2013), "The trouble with the aufbau principle", *Education in Chemistry* 50(6), 24–26 (https://edu.rsc.org/feature/the-trouble-with-the-aufbau-principle/2000133.article); Scerri (2017), *Foundations of Chemistry* (doi:10.1007/s10698-016-9249-0)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** aula 03 ("perde primeiro os elétrons do 4s"). Está correto e não foi alterado.

### 🟠 3. O bloco f inteiro chamado de "terras raras", com o lantânio como exemplo

**claim_id:** `QUI-TAB-TERRASRARAS-001`
**Tipo:** confusão de escopo (nomenclatura)
**Onde:** aula 01 · A tabela periódica como mapa de subcamadas
**Está escrito:** "**bloco f**: lantanídeos e actinídeos (as "terras raras" mineralógicas, como o lantânio e o cério)."
**Problema:** pela IUPAC, terras raras são Sc, Y e os lantanídeos (La–Lu). Os actinídeos não são terras raras, e Sc e Y, que são, ficam no bloco d. O La também é exemplo ruim de bloco f: no estado fundamental ele é 5d¹ 6s², sem nenhum elétron f (NIST).
**Correção proposta (aplicada):** "lantanídeos e actinídeos (U e Th estão entre os actinídeos). Os lantanídeos, junto com o escândio e o ítrio (bloco d), formam os elementos terras raras da IUPAC [...] Os actinídeos não são terras raras."
**Fonte:** IUPAC, *Nomenclature of Inorganic Chemistry — Recommendations 2005* (Red Book); NIST ASD (La I: 5d 6s²)  ·  **Nível:** normativa
**Confiança:** confirmado
**Também aparece em:** —

### 🟠 4. Definição de elétron de valência contradiz a própria aula

**claim_id:** `QUI-VAL-DEF-001`
**Tipo:** inconsistência interna
**Onde:** aula 01 · Vocabulário × seção "A tabela periódica como mapa"
**Está escrito:** "elétron da camada mais externa ocupada; é o que participa das ligações." Mais adiante: "Fe e Mn [...] seus elétrons de valência incluem os do 4s e os do 3d".
**Problema:** o 3d não está na camada mais externa (n = 4). Pela definição do vocabulário, os elétrons 3d do Fe não seriam de valência, o que contradiz o texto e a aula 03.
**Correção proposta (aplicada):** acrescentar ao vocabulário: "Nos metais de transição (Fe, Mn...) contam também os elétrons d da camada anterior (3d)."
**Fonte:** Atkins & Jones, *Chemical Principles*; coerência interna  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** a mesma simplificação está no curso-geologia (ver seção de consistência).

### 🟠 5. Tamanho do núcleo e razão núcleo/átomo

**claim_id:** `QUI-ATOMO-ESCALA-001`
**Tipo:** erro factual (valor na borda da faixa)
**Onde:** aula 01 · Tamanhos; Recap
**Está escrito:** "O núcleo de um átomo mede cerca de 10⁻¹⁵ m [...] A razão é de aproximadamente 100 000 para 1."
**Problema:** 10⁻¹⁵ m só vale para o hidrogênio (diâmetro de ~1,7 fm). Pela relação R ≈ 1,2 fm·A^(1/3), o núcleo do O tem ~6 fm de diâmetro, o do Fe ~9 fm e o do U ~15 fm. Para os elementos dos minerais, a razão átomo/núcleo fica entre 10⁴ e 10⁵. A analogia da ervilha no estádio continua válida.
**Correção proposta (aplicada):** "entre 10⁻¹⁵ e 10⁻¹⁴ m (de ~2 × 10⁻¹⁵ m no hidrogênio a ~1,5 × 10⁻¹⁴ m no urânio) [...] A razão fica entre 10 000 e 100 000 para 1." No recap: "Núcleo ≈ 10⁻¹⁵ a 10⁻¹⁴ m".
**Fonte:** relação empírica R = r₀A^(1/3), r₀ ≈ 1,2 fm (Krane, *Introductory Nuclear Physics*); raio de carga do próton ≈ 0,84 fm (CODATA)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** —

### 🟠 6. Energias de ionização do ferro (2ª e 4ª)

**claim_id:** `QUI-EI-SUCESS-001`
**Tipo:** erro factual (menor)
**Onde:** aula 02 · Ionizações sucessivas; aula 03 · O ferro
**Está escrito:** "ferro: 763; 1562; 2957; 5290 kJ/mol" (aula 02); "763; 1562; 2957 kJ/mol" (aula 03)
**Problema:** o NIST dá 16,19921 eV = **1563,0** kJ/mol e 54,91 ± 0,04 eV = **5298** kJ/mol. O valor 5290 fica fora da incerteza do NIST (±4 kJ/mol). Os demais valores pedidos no `incerteza:` conferem: Na 495,8/4562,4; Mg 737,7/1450,7/7732,7; Al 577,5/1816,7/2744,8/11577,5; Si 786,5; K 418,8; Cl 1251,2; Fe 1ª 762,5 e 3ª 2957,4.
**Correção proposta (aplicada):** 1562 → 1563 (aulas 02 e 03); 5290 → 5298 (aula 02).
**Fonte:** NIST ASD, *Ionization Energies* (consulta por espécie), 2026-09-30; conversão 1 eV = 96,4853 kJ/mol  ·  **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** aula 03 (corrigida).

### 🟠 7. Escala de eletronegatividade sem versão e sem estado de oxidação

**claim_id:** `QUI-EN-PAULING-001`
**Tipo:** omissão que gera erro
**Onde:** aula 02 · tabela de χ; aula 04 · tabela de caráter iônico
**Está escrito:** "χ (Pauling) [...] Fe 1,83 [...] Mn 1,55" e "Fe–O | 1,61 | ~48%"
**Problema:** os 11 valores estão corretos, mas são a **revisão de Allred (1961)** da escala de Pauling, que é por estado de oxidação: 1,83 é o Fe(II) e 1,55 o Mn(II); para o Fe(III), Allred dá 1,96. Sem esse aviso, o aluno usa 1,83 para o Fe³⁺ da hematita (Δχ 1,61 em vez de 1,48; caráter iônico ~48% em vez de ~42%). Escala declarada: **Pauling, valores revisados por Allred (1961), como tabulados no CRC Handbook**. Não é a escala de Allen.
**Correção proposta (aplicada):** nota abaixo da tabela da aula 02 explicando a escala e a dependência do estado de oxidação; rótulo "Fe–O (com χ do Fe²⁺)" na tabela da aula 04; fonte da aula 02 atualizada para Allred (1961).
**Fonte:** Allred, A. L. (1961), *J. Inorg. Nucl. Chem.* 17, 215–221; tabela compilada em KnowledgeDoor Elements Handbook (Fe(III) 1,96; Mn(II) 1,55; Cu(II) 2,00)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** aula 04 (tabela e exemplo trabalhado).

### 🟠 8. "Só a análise química não diz qual das duas cargas está presente"

**claim_id:** `QUI-FE-ANALISE-001`
**Tipo:** omissão que gera erro
**Onde:** aula 03 · Nomes e grafia
**Está escrito:** "Só a análise química não diz qual das duas cargas está presente; isso exige outro método (módulo 20) ou um cálculo de balanço de cargas (módulo 09)."
**Problema:** como está escrito, é falso para a análise química clássica por via úmida, em que a titulação determina o FeO separadamente. Quem mede só o ferro total são as análises de rotina (microssonda eletrônica, FRX).
**Correção proposta (aplicada):** "As análises de rotina, como a microssonda eletrônica e a fluorescência de raios X, medem só o ferro total [...] Separar Fe²⁺ de Fe³⁺ exige um método específico (titulação química por via úmida, espectroscopia Mössbauer ou XANES; módulo 20) ou um cálculo de balanço de cargas (módulo 09)."
**Fonte:** Droop, G. T. R. (1987), *Mineralogical Magazine* 51, 431–435; Forshaw & Pattison (2021), *Contributions to Mineralogy and Petrology* (https://link.springer.com/article/10.1007/s00410-021-01814-4)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** a aula 06 fala de "FeO total / Fe₂O₃ total" de forma compatível; não foi alterada.

### 🟠 9. Ouro com "χ baixo"; Cu "baixo" e Fe "intermediário" no mesmo texto

**claim_id:** `QUI-LIG-METAL-001`
**Tipo:** inconsistência interna (modelo mental errado)
**Onde:** aula 04 · Ligação metálica; Exemplo (c); regra dos três extremos
**Está escrito:** "têm átomos com χ baixo (Cu 1,90; Au 2,54; Ag 1,93)" e "(c) Cu–Cu. Δχ = 0 e χ = 1,90 (baixo)", enquanto no exemplo (d) o Fe (1,83) é "intermediário".
**Problema:** os valores de Pauling estão certos, mas 2,54 não é baixo: é quase o valor do S (2,58) e maior que o do C (2,55). O Si (1,90, semicondutor covalente) tem o mesmo χ e o mesmo Δχ = 0 do Cu. Isso mostra que "Δχ pequeno + χ baixo → metálica" é regra de bolso que falha exatamente nos metais nativos que a aula usa. O triângulo de Van Arkel–Ketelaar funciona melhor com a escala de Allen (Au 1,92).
**Correção proposta (aplicada):** "χ de Pauling moderado a alto" e parágrafo curto sobre o limite da regra (o ouro, e o silício com Δχ = 0 que não é metal; o caráter metálico depende da deslocalização dos elétrons); "(regra de bolso...)" na lista dos três extremos; no exemplo (c), "χ = 1,90 (moderado); é um elemento do bloco d, com elétrons de valência que se deslocalizam pelo cristal".
**Fonte:** Allred (1961)/CRC (valores de Pauling); Allen, L. C. & Capitani, J. F. (1993), "Van Arkel–Ketelaar triangles", *J. Mol. Struct.* 300 (https://www.sciencedirect.com/science/article/abs/pii/002228609387053C); valores de Allen via tabela de eletronegatividades (Wikipedia, data page, com CRC/WebElements)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** curso-geologia, módulo 04, aula 02 ("eletronegatividade baixa" nos metais). Ver consistência.

### 🟠 10. "Os silicatos combinam dureza alta"

**claim_id:** `QUI-LIG-SILDUREZA-001`
**Tipo:** confusão de escopo
**Onde:** aula 04 · O meio-termo
**Está escrito:** "por isso os silicatos combinam dureza alta (as ligações são fortes e direcionais) com pontos de fusão muito altos, e o quartzo tem dureza 7."
**Problema:** a generalização é falsa, e a própria aula 05 mostra o contraexemplo (talco, dureza 1). A dureza alta depende de a ligação Si–O forte se estender nas três direções, como no quartzo.
**Correção proposta (aplicada):** "É uma ligação forte e com direção preferida; quando ela liga os tetraedros em todas as direções do espaço, como no quartzo, o resultado é dureza alta (7) e ponto de fusão alto. Isso não vale para todo silicato: nos silicatos em lâminas, como o talco, [...] o mineral é mole (aula 05)."
**Fonte:** *Handbook of Mineralogy* (quartz: H = 7; talc: H = 1)  ·  **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** —

### ⚪ 11. Ponto de fusão do periclásio (MgO) dado como valor único

**claim_id:** `QUI-LIG-MGONACL-001`
**Tipo:** controvérsia (certeza indevida)
**Onde:** aula 04 · Ligação iônica
**Está escrito:** "o periclásio (+2/−2, íons menores) funde a cerca de 2800 °C e tem dureza 5,5 (valores de referência, para a auditoria conferir)."
**Problema:** as medidas publicadas do MgO vão de 3073 a 3250 K (≈ 2800 a 2977 °C). O valor tradicional é ~2800–2825 °C; a medida por aquecimento a laser de Ronchi & Sheindlin (2001) deu 3250 ± 20 K (≈ 2977 °C). O texto mostrava só o extremo baixo e ainda carregava uma nota interna ("para a auditoria conferir") dentro da aula. NaCl a 801 °C (800,7) e as durezas de halita (2–2,5) e periclásio (5,5) conferem.
**Correção proposta (aplicada):** "funde entre cerca de 2800 e 3000 °C (as medidas divergem: o valor tradicional é ~2800 °C, e a medida por aquecimento a laser de 2001 deu ~2980 °C) e tem dureza 5,5." A conclusão da aula (dobrar a carga pesa mais) não muda.
**Fonte:** Ronchi, C. & Sheindlin, M. (2001), *J. Appl. Phys.* 90, 3325 (https://ui.adsabs.harvard.edu/abs/2001JAP....90.3325R/abstract); PubChem (NaCl 800,7 °C); *Handbook of Mineralogy* (halite, periclase)  ·  **Nível:** revisada por pares
**Confiança:** em disputa (faixa)
**Também aparece em:** —

### 🟠 12. Diamante "sem plano de fraqueza pronunciado"

**claim_id:** `QUI-ANISO-DIAMANTE-001`
**Tipo:** omissão que gera erro
**Onde:** aula 05 · A ideia geral: anisotropia
**Está escrito:** "O diamante, ligado com a mesma força nas quatro direções, não tem um plano de fraqueza tão pronunciado, e por isso a propriedade é muito mais uniforme."
**Problema:** o diamante tem **clivagem perfeita {111}** (octaédrica), usada na lapidação para clivar pedras. Com o texto como estava, o aluno conclui que o diamante não cliva. A clivagem vem da menor densidade de ligações por área nos planos {111}, não de um tipo de ligação mais fraco. A aula já adianta essa ideia em "O que não concluir".
**Correção proposta (aplicada):** "não tem nenhum plano de ligação fraca. Mesmo assim ele tem clivagem perfeita, paralela às faces do octaedro ({111}): nesses planos há menos ligações por área a romper. Aqui quem decide a clivagem não é o tipo de ligação, e sim a densidade de ligações em cada plano (módulo 13)."
**Fonte:** *Handbook of Mineralogy*, Diamond ("Cleavage: {111}, perfect")  ·  **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** aula 04 (diamante "racha", correto e mantido).

### 🟠 13. Razão entre ligações fortes e fracas incoerente com a própria tabela

**claim_id:** `QUI-LIG-RAZAO-001`
**Tipo:** inconsistência interna (cálculo)
**Onde:** aula 05 · Comparação de energias; Recap
**Está escrito:** "A diferença é de **uma a duas ordens de grandeza**" e "Ligações fortes (200 a 800 kJ/mol) são 10 a 100 vezes mais energéticas que as fracas."
**Problema:** com os números da tabela, forte/ponte de H = 200/40 a 800/10 = **5 a 80×**, e forte/van der Waals = 200/5 a 800/0,5 = **40 a 1600×**, ou seja, uma a três ordens de grandeza. As faixas da tabela foram conferidas e estão certas: C–C ~350; energia de rede do NaCl 786–788 kJ/mol; ponte de H ≤ ~40, com o dímero de água ~21 kJ/mol (De).
**Correção proposta (aplicada):** "vai de uma a três ordens de grandeza: pelos números da tabela, a ponte de hidrogênio é de 5 a 80 vezes mais fraca que uma ligação forte, e a van der Waals, de 40 a mais de 1000 vezes"; recap alinhado.
**Fonte:** cálculo sobre a tabela da aula; Arunan et al. (2011), IUPAC, *Pure Appl. Chem.* 83, 1637 (https://publications.iupac.org/pac/pdf/2011/pdf/8308x1637.pdf); Born–Haber do NaCl (LibreTexts, Inorganic Chemistry)  ·  **Nível:** normativa (definição) / geral (energia de rede)
**Confiança:** confirmado
**Também aparece em:** —

### 🟠 14. "O diâmetro de um íon, 2 a 3 Å"

**claim_id:** `QUI-UNID-ESCALA-001`
**Tipo:** confusão de escopo
**Onde:** aula 06 · Unidades (Comprimento)
**Está escrito:** "o diâmetro de um íon, 2 a 3 Å;"
**Problema:** a faixa só cobre ânions e cátions grandes. Pelos raios de Shannon, Si⁴⁺ (IV) tem 0,26 Å de raio (diâmetro ~0,5 Å), Al³⁺ (VI) 0,535, Mg²⁺ (VI) 0,72, O²⁻ (VI) 1,40 (diâmetro 2,8 Å) e Cl⁻ (VI) 1,81 (diâmetro 3,6 Å). Os cátions pequenos são justamente os que o curso mais usa. Si–O ≈ 1,62 Å (1,61–1,63), lâmina de 30 µm = 3 × 10⁵ Å, cela de 5–20 Å e areia de 0,06–2 mm conferem.
**Correção proposta (aplicada):** "o diâmetro de um íon, de ~0,5 Å (Si⁴⁺ em coordenação 4) a ~2,8 Å (O²⁻) e ~3,6 Å (Cl⁻), segundo os raios de Shannon;"
**Fonte:** Shannon, R. D. (1976), *Acta Cryst.* A32, 751–767, via base de raios iônicos de Shannon (Imperial College, http://abulafia.mt.ic.ac.uk/shannon/), consultada em 2026-09-30  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** —

## Verificado e correto

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `QUI-ORB-CAP-001` | s/p/d/f: 1/3/5/7 orbitais; 2/6/10/14 e⁻; Pauli | química geral consolidada | confirmado |
| `QUI-ORB-ORDEM-001` | Ordem de Madelung 1s…7s (claim reescrito junto com o achado 2) | NIST ASD; Scerri 2013 | confirmado |
| `QUI-CONF-FE-001` | Fe [Ar]3d⁶4s² (⁵D), Mn [Ar]3d⁵4s² (⁶S); período 4, grupos 8 e 7; 4 e 5 desemparelhados | NIST ASD | confirmado |
| `QUI-ORB-FORMA-001` | 5 orbitais d, "quatro lóbulos na maioria" | química geral consolidada | confirmado |
| `QUI-CONF-EXC-001` | Cr [Ar]3d⁵4s¹; Cu [Ar]3d¹⁰4s¹ | NIST ASD | confirmado |
| `QUI-PERIOD-TEND-001` | Tendências periódicas; anomalia Al (577,5) < Mg (737,7) | NIST ASD | confirmado |
| `QUI-RAIO-ATOM-001` | Na ~1,9 Å, Cl ~1,0 Å, convenção variável (Na: empírico 1,80, calculado 1,90, metálico 1,86; Cl: empírico 1,00, covalente 0,99) | Slater (1964) via tabela de raios atômicos | confirmado (com ressalva já presente no texto) |
| `QUI-EN-INTENSIDADE-001` | Pauling construída de energias de ligação; valores dependem da escala | Pauling (1960); Allred (1961) | confirmado |
| `QUI-MIN-OXIDO-001` | Periclásio MgO, coríndon Al₂O₃ | Handbook of Mineralogy | confirmado |
| `QUI-OX-CARGA-001` | Cargas usuais; regra da soma com O = −2 | IUPAC Gold Book | confirmado |
| `QUI-FE-ESTADO-001` | Fe²⁺ = 3d⁶; Fe³⁺ = 3d⁵ (4s sai primeiro) | NIST ASD; Scerri | confirmado |
| `QUI-FE-MAG-001` | Magnetita Fe²⁺Fe³⁺₂O₄; hematita Fe³⁺; siderita e fayalita Fe²⁺ | balanço de cargas | confirmado |
| `QUI-FE-RAIO-001` | Shannon VI spin alto: Fe²⁺ 0,78 Å; Fe³⁺ 0,645 Å | Shannon (1976) | confirmado |
| `QUI-MN-ESTADO-001` | Rodocrosita Mn²⁺; hausmannita Mn²⁺Mn³⁺₂O₄; pirolusita Mn⁴⁺ | Handbook of Mineralogy | confirmado |
| `QUI-S-ESTADO-001` | S: −2 galena, −1 pirita (Fe²⁺ + S₂²⁻), 0 nativo, +6 sulfatos. A atribuição da pirita (Fe²⁺ de spin baixo + dissulfeto) é a aceita, com base em Mössbauer e XPS; a nota interna "marcado para a auditoria" foi trocada por essa informação | HoM (pyrite); literatura XPS/Mössbauer | confirmado |
| `QUI-OX-CONVENCAO-001` | Estado de oxidação é convenção de contagem | IUPAC Gold Book | confirmado |
| `QUI-FE-D5-001` | Estabilidade do d⁵ como guia simplificado | NIST: 3ª EI Fe 2957 < Mn 3248 kJ/mol | confirmado (a aula já traz a ressalva) |
| `QUI-LIG-ESPECTRO-001` | Contínuo; triângulo de Van Arkel–Ketelaar (1941/1947; livros de 1956 e 1958) | Allen & Capitani (1993) | confirmado |
| `QUI-LIG-PAULING-001` | I = 1 − e^(−Δχ²/4): 71,2 / 67,8 / 47,7 / 44,7 / 13,1%; 50% em Δχ ≈ 1,67 | Pauling (1960); recálculo | confirmado (a aula já a apresenta como heurística sem consenso) |
| `QUI-LIG-DIAMANTE-001` | Tetraedro 109,5°; dureza 10; Mohs 1812 (divulgada em 1822–1824) | HoM; Science History Institute | confirmado |
| `QUI-LIG-SIO-001` | Si–O ~metade iônica (Pauling); quartzo H = 7 | Pauling; HoM | confirmado |
| `QUI-LIG-PIRITA-001` | Pirita semicondutora, frágil, brilho metálico | HoM (pyrite) | confirmado |
| `QUI-LIG-ENERGIA-001` | Faixas: covalente 200–500; rede NaCl ~800 (786–788); ponte de H 10–40 (água ~20); vdW 0,5–5 kJ/mol | Arunan et al. 2011; Born–Haber | confirmado (ordens de grandeza) |
| `QUI-GRAFITE-DIST-001` | C–C 1,42 Å; entre planos 3,35 Å; H 1–2 | HoM (2H: a = 2,464, c = 6,711 Å) | confirmado |
| `QUI-TALCO-ESTR-001` | Talco: H = 1, clivagem {001} perfeita | HoM | confirmado |
| `QUI-MICA-K-001` | Moscovita KAl₂(AlSi₃O₁₀)(OH)₂; H 2,5 ∥ clivagem (4 ⊥) | HoM | confirmado |
| `QUI-GIPSITA-H-001` | Gipsita: {010} perfeita; H = 2; H₂O = 20,93% | HoM; recálculo CIAAW 2024 | confirmado |
| `QUI-ENXOFRE-001` | S₈; H 1,5–2,5; funde ~115 °C (monoclínico 115,21 °C) | HoM; PubChem/CRC | confirmado |
| `QUI-BRUCITA-001` | Brucita {0001} perfeita; H 2,5 | HoM | confirmado |
| `QUI-AGUA-ANG-001` | Gelo é espécie válida (grandfathered); ângulo 104,5° | Mindat; conhecimento consolidado | confirmado |
| `QUI-MOL-AVOG-001` | N_A = 6,02214076 × 10²³ mol⁻¹ exato | NIST CODATA / BIPM | confirmado |
| `QUI-MASSA-ATOM-001` | 12 massas atômicas | CIAAW Abridged Standard Atomic Weights 2024 | confirmado |
| `QUI-FORST-MOLAR-001` | 140,691 g/mol; 57,29% MgO; 42,71% SiO₂; razão 2,000 | recálculo | confirmado |
| `QUI-FEOX-FATOR-001` | 0,7773; 0,6994; pirita 119,965 e 46,6% Fe; 30% Fe₂O₃ → 20,98% Fe | recálculo | confirmado |
| `QUI-UNID-PRESS-001` | 1 GPa = 10 kbar; 1 atm = 101 325 Pa; ρgh = 26,5 MPa/km a 2,7 g/cm³; 1 kbar = 3,4–3,8 km; centro da Terra ~364 GPa (PREM) | NIST; PREM via Fei et al. (2007, PNAS 104, 9182) e literatura | confirmado |
| `QUI-UNID-TEMP-001` | K = °C + 273,15 | BIPM | confirmado |
| `QUI-QZ-DENS-001` | ρ = 2,65; 2,66 × 10²² fórmulas; 7,97 × 10²² átomos por cm³ | HoM; recálculo | confirmado |

Outros cálculos das aulas refeitos e corretos: lâmina/Si–O = 1,85 × 10⁵; 2,5 kbar = 0,25 GPa ≈ 9,3 km; 750 °C = 1023,15 K; Δχ(Ca–O) = 2,44 e Δχ(S–O) = 0,86 (aula 05); reação 4 FeO + O₂ → 2 Fe₂O₃ balanceada.

## Consistência com curso-geologia, módulo 04 (aulas 01–02)

Só relato: o curso-geologia está fora do escopo desta correção e **não foi alterado**. As aulas de mineralogia também não copiam o texto de geologia. Contradições encontradas, do ponto de vista do que a mineralogia agora ensina:

1. **Ligação iônica como "transferência completa".** Geologia, aula 02 (seção "Três formas" e recap: "Iônica — transferência completa de elétron"). A mineralogia, aula 04, lista esse modo de pensar como **erro comum** ("Achar que 'iônica' significa transferência total de elétrons"). A geologia se corrige em parte em "Erros comuns" (espectro contínuo), mas o recap repete a versão absoluta.
2. **Elétrons de valência só na camada mais externa, e camadas preenchidas "de dentro para fora, uma de cada vez".** Geologia, aula 01. A mineralogia, aula 01 (após a correção 2 e 4), ensina que o 3d entra na valência dos metais de transição e que o 4s é ocupado antes do 3d. A geologia reconhece a exceção dos elementos de transição só para a regra do octeto.
3. **Metais com "eletronegatividade baixa".** Geologia, aula 02, com o ouro nativo como exemplo clássico. É o mesmo problema corrigido no achado 9: pelo χ de Pauling, o ouro tem 2,54.
4. **Coerente:** o flúor como mais eletronegativo; a tendência de χ; a halita mole apesar de iônica (geologia 2–2,5, mineralogia 2–2,5); diamante e grafite como polimorfos; cátion menor e ânion maior que o átomo neutro.

Sugestão (fora deste escopo): passar o curso-geologia/04 aulas 01–02 pelo auditor, pelo menos para o recap da ligação iônica.

## Observações não factuais

- As seções "Fontes consultadas" das aulas citam livros (Klein & Dutrow, Atkins & Jones, Nesse, Kittel, Housecroft & Sharpe) que o autor não consultou de fato, porque as aulas foram escritas de memória. Onde esta auditoria checou em fonte real, a citação foi acrescentada ou substituída; as citações de livro restantes indicam só o corpo de referência, sem conferência de página.
- Aula 03: "óxidos negros e pretos de manganês" é redundância de redação.
- Aula 03: a pirita tem Fe²⁺ de spin baixo (0 elétrons desemparelhados), o que contrasta com os "4 desemparelhados" do Fe²⁺ ensinados via Hund na aula 01. A menção "de spin baixo" foi incluída; o módulo 48 (campo cristalino) é o lugar natural para explicar.
- Aula 05: a definição de ponte de hidrogênio (H ligado a O, N, F) é mais restrita que a da IUPAC 2011 (X mais eletronegativo que H). Para minerais (O–H···O) é suficiente.

---

## Correções aplicadas

**Aplicadas em:** 2026-09-30

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `QUI-CONF-DESEMP-001` | 🔴 | Corrigido | aula-01 |
| `QUI-ORB-ENERGIA-001` | 🟠 | Corrigido | aula-01 |
| `QUI-TAB-TERRASRARAS-001` | 🟠 | Corrigido | aula-01 |
| `QUI-VAL-DEF-001` | 🟠 | Corrigido | aula-01 |
| `QUI-ATOMO-ESCALA-001` | 🟠 | Corrigido | aula-01 |
| `QUI-EI-SUCESS-001` | 🟠 | Corrigido | aula-02, aula-03 |
| `QUI-EN-PAULING-001` | 🟠 | Corrigido | aula-02, aula-04 |
| `QUI-FE-ANALISE-001` | 🟠 | Corrigido | aula-03 |
| `QUI-LIG-METAL-001` | 🟠 | Corrigido | aula-04 |
| `QUI-LIG-SILDUREZA-001` | 🟠 | Corrigido | aula-04 |
| `QUI-LIG-MGONACL-001` | ⚪ | Corrigido com ressalva (divergência exposta como faixa) | aula-04 |
| `QUI-ANISO-DIAMANTE-001` | 🟠 | Corrigido | aula-05 |
| `QUI-LIG-RAZAO-001` | 🟠 | Corrigido | aula-05 |
| `QUI-UNID-ESCALA-001` | 🟠 | Corrigido | aula-06 |

Também foram atualizados: os rodapés `alegacoes_auditaveis` das 6 aulas (os campos `incerteza:` foram resolvidos e trocados por `audit:` com data e desfecho; 8 claim_ids novos; `palavras_corpo` recontado); as seções "Fontes consultadas" com as fontes realmente consultadas; `01-fundamentos-quimicos-modulo.md` (registro); `course-state.yaml` (bloco `audit` do módulo 01, hashes, `palavras_corpo`, `next_action`, `updated_at`).

**Pendências:** nenhuma pendência factual no módulo. Fontes que não consegui abrir diretamente estão no manifesto: a tabela do PREM (PDF da Harvard truncado, espelho da McGill fora do ar, IRIS negou acesso; o valor de 364 GPa foi confirmado por literatura revisada que cita o PREM); as páginas do Mindat (HTTP 403; usei o *Handbook of Mineralogy*, da mesma hierarquia); WebElements (403); NIST WebBook sem Tf do MgO (usei Ronchi & Sheindlin 2001).

**Aviso de baralho já importado:** não se aplica. O módulo ainda não tem questionário nem flashcards, e nenhum foi gerado nesta etapa.
