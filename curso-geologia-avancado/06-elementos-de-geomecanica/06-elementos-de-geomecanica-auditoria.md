# Auditoria científica — Módulo 06: Elementos de geomecânica

**Módulo:** [[06-elementos-de-geomecanica-modulo|Módulo 06 — Elementos de geomecânica]]
**Escopo:** 6 aulas (geologia-avancado-m06-a01 a a06), 34 alegações auditáveis extraídas dos blocos de metadados de cada aula.
**Método:** verificação de cada `claim_id` contra a literatura padrão de mecânica dos solos e geotecnia (Terzaghi, Peck & Mesri, 1996; Das, 2019; Cedergren, 1989; Lunne, Robertson & Powell, 1997) e contra o texto das normas e publicações primárias citadas (ASTM D698, D1557, D1586, D1587, D2166, D2216, D2434, D2435, D2487, D2573, D3080, D4253/D4254, D4767, D5084; ABNT NBR 6484 e 8036; AASHTO M 145; Terzaghi 1925; Casagrande 1936, 1948; Jáky 1944; Skempton 1964; Schofield & Wroth 1968; Mesri & Godlewski 1977; Bieniawski 1978; Serafim & Pereira 1983; Houlsby 1976; Lugeon 1933; Hvorslev 1951; Bouwer & Rice 1976; Witherspoon et al. 1980; Mayne & Kulhawy 1982; Robertson 1990; Hoek & Diederichs 2006), com recálculo independente de todos os exemplos numéricos trabalhados.
**Data:** 2026-08-27

## Resumo do veredito

| Severidade | Contagem |
|---|---|
| 🔴 Erro | 0 |
| 🟠 Impreciso | 1 (corrigido antes da publicação) |
| 🟡 Desatualizado/a matizar | 1 (corrigido antes da publicação) |
| 🔵 Controverso (área com debate legítimo) | 1 |
| ⚪ Sem fonte direta verificável (mas plausível/consensual) | 2 |

**Veredito geral: aprovado.** Nenhum achado vermelho. O único achado 🟠 e o único 🟡 foram identificados durante esta auditoria e **corrigidos no texto das aulas antes da geração do questionário e do baralho**, de modo que nenhum achado vermelho ou laranja permanece em aberto — o gate de qualidade do plugin está satisfeito. O achado 🔵 registra uma área de debate técnico real (a natureza do intercepto c'), já tratada com a cautela adequada no texto. Os dois achados ⚪ são aproximações de ordem de grandeza já qualificadas como tais.

## Achados

### 🟠 [GEOMEC-M06-A06-SPT-005] — Especificação do martelo do SPT atribuída conjuntamente a duas normas divergentes
**Aula:** 06. **Claim relacionado:** especificação do ensaio SPT.
**Achado:** a redação inicial da Aula 06 apresentava "SPT (NBR 6484 / ASTM D1586)" com uma única especificação de martelo — 65 kg caindo de 75 cm — como se as duas normas coincidissem. Elas não coincidem: a **ABNT NBR 6484** especifica massa de 65 kg e altura de queda de 75 cm, enquanto a **ASTM D1586** especifica 63,5 kg (140 lb) e queda de 762 mm (30 in). A diferença de energia nominal é pequena (cerca de 4%), mas a atribuição de um único par de valores a ambas as normas é factualmente incorreta, e o ponto tem consequência prática: é justamente a variabilidade de energia efetivamente transferida que motiva a correção para N60, mencionada logo adiante na mesma aula.
**Correção proposta:** separar as duas especificações e explicitar que os valores de N não são rigorosamente intercambiáveis entre normas sem correção de energia.
**Status:** ✅ **corrigido** no texto da Aula 06 e no bloco de metadados correspondente, antes da geração do questionário e do baralho.
**Confiança:** alta.

### 🟡 [GEOMEC-M06-A03-K0-004] — A expressão K0 = 1 − sen φ' é a forma simplificada de Jáky, não a expressão original
**Aula:** 03. **Claim relacionado:** estimativa de K0 para solos normalmente adensados.
**Achado:** a redação inicial atribuía a Jáky (1944) diretamente a expressão K0 = 1 − sen φ'. A formulação teórica original de Jáky é mais longa — K0 = (1 − sen φ)(1 + ⅔ sen φ)/(1 + sen φ) —, e a forma simples é a aproximação prática que o próprio Jáky derivou dela e que a literatura subsequente consagrou. A atribuição não é falsa em espírito (a simplificação é do próprio autor), mas apresentar apenas a forma reduzida como "a correlação de Jáky" omite que se trata de uma aproximação, o que importa num curso de nível de especialização. As duas formas diferem por poucos por cento na faixa usual de φ' (25°–40°), sem impacto no exemplo trabalhado.
**Correção proposta:** registrar a expressão original e caracterizar explicitamente 1 − sen φ' como a aproximação prática dela derivada.
**Status:** ✅ **corrigido** no texto da Aula 03 e no bloco de metadados correspondente.
**Confiança:** alta.

### 🔵 [GEOMEC-M06-A06-COESAO-008] — O estatuto físico do intercepto de coesão efetiva c'
**Aula:** 06. **Claim relacionado:** "c' representa qualquer parcela de resistência independente da tensão normal: cimentação verdadeira, ligações diagenéticas, atração eletroquímica entre partículas argilosas."
**Achado:** há debate legítimo e ativo na mecânica dos solos sobre se c' corresponde a um fenômeno físico real ou é um artefato de ajuste linear a uma envoltória curva. A escola de estado crítico (Schofield & Wroth, 1968, e desenvolvimentos posteriores) sustenta que, para solos não cimentados, a coesão verdadeira é nula e o intercepto observado resulta de ajustar uma reta a uma envoltória efetivamente curva sobre uma faixa restrita de tensões — posição defendida com particular ênfase por Schofield em trabalhos posteriores. A prática de projeto, por outro lado, adota c' > 0 rotineiramente para solos sobreadensados e cimentados. O texto da aula não toma partido dogmático: apresenta c' com os mecanismos que lhe são usualmente atribuídos e, no mesmo bloco, adverte explicitamente em callout que se trata de "um parâmetro de ajuste, não uma propriedade física medida", obtido por extrapolação a uma região sem dados experimentais — tratamento adequado e honesto de uma questão em aberto.
**Correção proposta:** nenhuma. O texto já sinaliza a natureza de ajuste do parâmetro no ponto exato onde o aluno estaria mais exposto a tomá-lo como propriedade física.
**Confiança:** alta.

### ⚪ [GEOMEC-M06-A04-LUGEON-006] — Conversão entre unidade Lugeon e condutividade hidráulica
**Aula:** 04. **Claim:** "uma unidade Lugeon... corresponde a uma condutividade da ordem de 10⁻⁷ m/s".
**Achado:** a definição da unidade Lugeon (1 L/min por metro de furo sob 1 MPa) é exata e não controversa (Lugeon, 1933; Houlsby, 1976). Já a conversão para condutividade hidráulica é uma estimativa que depende da geometria do trecho ensaiado (comprimento e diâmetro) e da hipótese de fluxo radial permanente; os valores citados na literatura concentram-se em torno de 1,0 a 1,3 × 10⁻⁷ m/s, e não há um fator de conversão único e universal. O texto qualifica corretamente o valor com "da ordem de" e reforça, na seção "O que não concluir", que a conversão é aproximada e que o parâmetro de projeto é a própria absorção medida, não o k convertido.
**Correção proposta:** nenhuma. A qualificação já presente no texto é adequada.
**Confiança:** alta.

### ⚪ [GEOMEC-M06-A05-SECUNDARIA-006] — Faixas da razão Cα/Cc
**Aula:** 05. **Claim:** "Cα/Cc ≈ 0,04 ± 0,01 para argilas inorgânicas e ≈ 0,05 ± 0,01 para argilas orgânicas e turfas".
**Achado:** as faixas correspondem às reportadas por Mesri & Godlewski (1977) e reproduzidas na literatura subsequente, e a constância aproximada da razão Cα/Cc para um dado solo é um resultado bem estabelecido. Ressalva de baixo impacto: compilações posteriores registram valores fora dessas faixas para materiais específicos (turfas muito fibrosas e alguns rejeitos podem exceder 0,06; areias ficam abaixo de 0,02), de modo que os valores devem ser lidos como faixas típicas por classe de material, não como constantes. O texto já os introduz como "uma correlação de referência útil", sem apresentá-los como universais.
**Correção proposta:** nenhuma obrigatória.
**Confiança:** média-alta.

## Verificação amostral de fórmulas e cálculos (checklist)

- Cu = D60/D10 e Cc = (D30)²/(D10·D60) (Aula 01): consistentes com ASTM D2487. ✅
- Linha A da carta de plasticidade, IP = 0,73(LL−20) (Aula 01): confere com Casagrande (1948) e ASTM D2487. ✅
- Limiares do SUCS (50% na peneira nº 200; LL = 50% separando baixa e alta compressibilidade) (Aula 01): conferem com ASTM D2487. ✅
- Índice de grupo AASHTO, GI = (F200−35)[0,2+0,005(LL−40)] + 0,01(F200−15)(IP−10), com truncamento em zero (Aula 01): confere com AASHTO M 145. ✅
- Relações de índices físicos: n = e/(1+e), e = n/(1−n), w = Mw/Ms (base seca), γd = γ/(1+w) (Aula 02): conferem com Das (2019, cap. 2). Exemplo trabalhado recalculado (Mt=185 g, Ms=160 g, V=100 cm³, Gs=2,68): w=15,6%, Vs≈59,7 cm³, Vv≈40,3 cm³, e≈0,675, n≈40,3%, Sr≈62,0%. Confere, inclusive a identidade de conferência Sr·e = w·Gs (0,620×0,675 = 0,4185; 0,15625×2,68 = 0,41875 — coincidem dentro do arredondamento). ✅
- Dr = (emáx−e)/(emáx−emín) e sua distinção de Gs (Aula 02): confere com ASTM D4253/D4254. ✅
- Curva de saturação γd,zav = Gs·γw/(1+w·Gs) e dependência da curva de Proctor em relação à energia aplicada (Aula 02): conferem com ASTM D698 e D1557. ✅
- Princípio das tensões efetivas σ' = σ − u, incluindo sua segunda parte (todo efeito mensurável decorre de variação de σ') (Aula 03): confere com Terzaghi (1925) e Terzaghi, Peck & Mesri (1996, cap. 2). ✅
- Equivalência entre σ'v = σv − u e a acumulação de γsub abaixo do NA, e sua restrição à condição hidrostática (Aula 03): verificada algebricamente e consistente com Das (2019, cap. 8). ✅
- Poropressão negativa na franja capilar (u = −γw·hc) elevando σ' e gerando coesão aparente (Aula 03): confere com Das (2019, cap. 8). ✅
- K0 = σ'h/σ'v em tensões efetivas; K0 ≈ 1 − sen φ' (Jáky 1944) e K0,SA ≈ K0,NA·(OCR)^sen φ' (Mayne & Kulhawy 1982) (Aula 03): fórmulas conferidas contra as publicações originais. Ver achado 🟡 quanto à forma simplificada. ✅
- Gradiente crítico icr = γsub/γw = (Gs−1)/(1+e) (Aula 03): identidade verificada algebricamente a partir das definições de γsat e e; para Gs=2,65 e e=0,65, icr = 1,65/1,65 = 1,00, confirmando a regra prática de icr ≈ 1. ✅
- Exemplo trabalhado da Aula 03 recalculado (4 m com γ=17 kN/m³ + 6 m com γsat=20 kN/m³, NA a 4 m, φ'=32°): σv = 68+120 = 188 kPa; u = 9,81×6 = 58,86 kPa; σ'v = 129,14 kPa; conferência pelo peso submerso: 68 + (10,19×6) = 129,14 kPa — as duas vias coincidem. K0 = 1 − sen 32° = 1 − 0,5299 = 0,4701; σ'h = 60,7 kPa; σh = 119,6 kPa. Confere. ✅
- Equação de Laplace para fluxo permanente e as relações da rede de fluxo Q = k·H·(Nf/Nd) (Aula 04): conferem com Das (2019, cap. 7) e Cedergren (1989). ✅
- Condutividade equivalente de pacote estratificado: média aritmética ponderada na direção paralela às camadas e média harmônica na perpendicular; transformação de escala √(kv/kh) e k_eq = √(kh·kv) em meio anisotrópico (Aula 04): conferem com Das (2019, cap. 7). ✅
- Força de percolação j = i·γw e distinção entre heave e piping (Aula 04): conferem com Terzaghi, Peck & Mesri (1996, cap. 2 e 4) e Cedergren (1989). A afirmação de que piping pode iniciar em gradientes locais inferiores ao icr médio e é causa histórica frequente de ruptura de barragens de terra é bem estabelecida na literatura de segurança de barragens. ✅
- Expressões dos permeâmetros de carga constante, k = (Q·L)/(A·Δh·t), e de carga variável, k = (a·L)/(A·t)·ln(h1/h2) (Aula 04): conferem com Das (2019, cap. 7), ASTM D2434 e D5084. ✅
- Exemplo trabalhado da Aula 04 recalculado (k=2×10⁻⁵ m/s, H=6 m, Nf=4, Nd=12, extensão 30 m, γsat=20 kN/m³, último elemento de 0,5 m): q = 2×10⁻⁵×6×(1/3) = 4,0×10⁻⁵ m³/s·m; Q = 1,2×10⁻³ m³/s = 1,2 L/s; Δh por queda = 0,5 m; i_saída = 1,0; γsub = 10,19 kN/m³; icr = 10,19/9,81 = 1,0387; FS = 1,039 ≈ 1,04. Confere. ✅
- Lei cúbica em meio fissurado e a distinção entre abertura hidráulica e mecânica (Aula 04): confere com Witherspoon et al. (1980). ✅
- Curva e–log σ' com trechos de recompressão (Cr) e reta virgem (Cc); construção de Casagrande para σ'p; OCR = σ'p/σ'v0 (Aula 05): conferem com Casagrande (1936), ASTM D2435 e Das (2019, cap. 11). A relação típica Cc entre 5 e 10 vezes Cr é consistente com a literatura, e o texto a apresenta como faixa típica, não como regra fixa. ✅
- Fórmulas de recalque primário nos três casos (NA, SA abaixo de σ'p, e SA cruzando σ'p), com logaritmo decimal (Aula 05): conferem com Das (2019, cap. 11). ✅
- Equação de difusão do adensamento, Tv = cv·t/Hd², e os pares de referência U=50% → Tv=0,197 e U=90% → Tv=0,848 (Aula 05): conferem com Terzaghi (1925) e as tabelas reproduzidas em Das (2019, cap. 11). A definição de Hd como a maior distância a uma face drenante (H/2 com dupla drenagem, H com simples) e seu efeito quadrático conferem. ✅
- Exemplo trabalhado da Aula 05 recalculado (H=4 m, dupla drenagem, σ'v0=100 kPa, σ'p=130 kPa, Δσ=80 kPa, e0=0,90, Cc=0,35, Cr=0,07, cv=2,0 m²/ano): OCR = 1,30; σ'vf = 180 kPa > σ'p, logo duas parcelas. ρ1 = (0,28/1,90)·log(1,30) = 0,147368×0,113943 = 0,01679 m; ρ2 = (1,40/1,90)·log(1,38462) = 0,736842×0,141264 = 0,10409 m; ρ = 0,1209 m ≈ 12,1 cm. Tempo: Hd = 2,0 m; t = 0,848×4/2,0 = 1,696 ano ≈ 20 meses. Verificação da variante com drenagem simples citada na interpretação: Hd = 4,0 m → t = 0,848×16/2,0 = 6,78 anos, quatro vezes maior. Confere. ✅
- Compressão secundária ρs = (Cα·H/(1+ep))·log(t2/t1) e a razão Cα/Cc (Aula 05): conferem com Mesri & Godlewski (1977). Ver achado ⚪. ✅
- Correlações de deformabilidade de maciço: Em = 2·RMR − 100 GPa para RMR > 50 (Bieniawski 1978); Em = 10^[(RMR−10)/40] GPa (Serafim & Pereira 1983); e a expressão de Hoek & Diederichs (2006) Em = Ei·[0,02 + (1−D/2)/(1+e^((60+15D−GSI)/11))] (Aula 05): as três conferem com as publicações originais, inclusive a restrição de validade RMR > 50 na primeira (abaixo desse valor a expressão linear produz resultados negativos, motivo declarado da proposta de Serafim & Pereira). ✅
- Mohr-Coulomb em tensões efetivas e a forma em tensões principais σ'1 = σ'3·Nφ + 2c'·√Nφ com Nφ = tan²(45°+φ'/2) (Aula 06): confere com Das (2019, cap. 12). ✅
- Condições drenada e não drenada, envoltória horizontal (φu = 0) em análise por su, e a inversão de qual prazo é crítico entre carregamento (aterro: curto prazo) e descarregamento (escavação: longo prazo) (Aula 06): conferem com Terzaghi, Peck & Mesri (1996, cap. 3 e 5). ✅
- Modalidades triaxiais UU, CU e CD e seus produtos; su = qu/2 na compressão simples (Aula 06): conferem com ASTM D4767, D2166 e Das (2019, cap. 12). ✅
- Pico por dilatância, convergência ao estado crítico (φ'cv) e resistência residual (φ'r) governando superfícies preexistentes (Aula 06): conferem com Schofield & Wroth (1968) e Skempton (1964). ✅
- Exemplo trabalhado da Aula 06 recalculado (CD, σ'3=100 → σ'1=350 kPa; σ'3=200 → σ'1=600 kPa): subtração das equações dá Nφ = 250/100 = 2,50 e K = 100 kPa; tan(45°+φ'/2) = √2,50 = 1,58114 → 45°+φ'/2 = 57,688° → φ' = 25,38° ≈ 25,4°; c' = 100/(2×1,58114) = 31,62 kPa. Verificação inversa: com φ'=25,38° e c'=31,62 kPa, σ'1 para σ'3=100 kPa dá 100×2,50 + 100 = 350 kPa, e para σ'3=200 kPa dá 600 kPa. Confere exatamente. ✅
- Especificações e propósitos dos métodos de prospecção — SPT, sondagem rotativa, amostrador Shelby (ASTM D1587), CPT/CPTu, palheta (ASTM D2573), pressiômetro, dilatômetro, sísmica de refração, MASW, ERT, GPR (Aula 06): conferem com as normas citadas e com Lunne, Robertson & Powell (1997). Ver achado 🟠 quanto à especificação do martelo. ✅
- Critério de profundidade de investigação (até onde Δσ cai abaixo de ~10% de σ'v0) e a referência à NBR 8036 para programação de sondagens em edificações (Aula 06): consistente com a prática normativa e com Das (2019, cap. 18); o texto apresenta o limiar de 10% como valor usual, não como prescrição normativa literal. ✅

## Cobertura de objetivos de aprendizagem

| Objetivo | Aulas que cobrem | Verificado |
|---|---|---|
| geologia-avancado-m06-oa01 | a01 | ✅ |
| geologia-avancado-m06-oa02 | a02, a03, a04 | ✅ |
| geologia-avancado-m06-oa03 | a05 | ✅ |
| geologia-avancado-m06-oa04 | a06 | ✅ |

Todos os quatro objetivos de aprendizagem do módulo têm pelo menos uma aula dedicada e alegações auditáveis correspondentes; nenhum objetivo ficou sem cobertura.

## Recomendação

Aprovar o módulo para avaliação (questionários) e memorização (flashcards). As duas correções identificadas (🟠 especificação do martelo do SPT; 🟡 forma original da expressão de Jáky) já foram aplicadas ao texto das aulas e aos blocos de metadados, de modo que **nenhum achado vermelho ou laranja permanece em aberto**. O achado 🔵 fica registrado como referência de um debate técnico legítimo (o estatuto físico de c'), já tratado com a cautela apropriada no texto; os dois achados ⚪ são aproximações de ordem de grandeza qualificadas como tais.
