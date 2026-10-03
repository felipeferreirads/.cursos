# Auditoria científica — Módulo 40: Mineralogia dos tectossilicatos

**Módulo:** [[40-mineralogia-dos-tectossilicatos-modulo|Módulo 40 — Mineralogia dos tectossilicatos]]
**Escopo:** 14 aulas (geologia-avancado-m40-a01 a a14), 128 alegações auditáveis extraídas dos blocos `alegacoes_auditaveis` de cada aula.
**Método:** verificação de cada `claim_id` contra a fonte primária do módulo — Vlach, S. R. F., *A Classe dos Tectossilicatos: Guia Geral da Teoria e Exercício* (IGc-USP, Série Didática USP, 49 p.), item a item — e, onde o guia cita obras de base ou onde a literatura posterior alterou o quadro, contra Deer, Howie & Zussman (1992); Klein & Hurlbut Jr. (1993, hoje Klein & Dutrow, 2007); Tröger (1979); Ribbe (1975); Smith & Brown (1988); Tuttle & Bowen (1958); Schairer & Bowen (1955); Ferry & Blencoe (1978); Mumpton (1977); Megaw (1974); Mason & Moore (1982); Ronov & Yaroshevsky (1969); Heaney, Prewitt & Gibbs (1994, RiM v. 29); Coombs et al. (1997, nomenclatura IMA de zeólitas); Bish & Ming (2001, RiMG v. 45); códigos de arcabouço da International Zeolite Association. Todos os exemplos numéricos trabalhados (fórmulas estruturais, proporções de membros finais, conversões molar↔peso, atrasos ópticos, percentagens estequiométricas de SiO₂) foram **recalculados de forma independente** a partir dos dados brutos das Tabelas 1 e 2 do guia.
**Data:** 2026-08-26

## Resumo do veredito

| Severidade | Contagem |
|---|---|
| 🔴 Erro | 0 |
| 🟠 Impreciso | 1 (corrigido) |
| 🟡 Desatualizado/a matizar | 3 (2 corrigidos, 1 já sinalizado no texto) |
| 🔵 Controverso (área com debate legítimo) | 3 |
| ⚪ Sem fonte direta verificável / nota de precisão | 3 |

**Veredito geral: aprovado, após correções.** Nenhum achado 🔴. O único achado 🟠 (atribuição autoral do índice de triclinicidade) foi corrigido na aula 06 durante esta auditoria. Dois achados 🟡 foram corrigidos na aula 14; o terceiro já vinha sinalizado no corpo da própria aula. Os três achados 🔵 registram debates científicos reais que o texto já trata como debate, não como fato assentado. **0 achados 🔴/🟠 em aberto** — o módulo está liberado para questionário e flashcards.

> [!important] Contexto: cinco correções da fonte primária já incorporadas na redação
> Esta auditoria confirma e ratifica cinco pontos em que as aulas **corrigem deliberadamente o guia do Prof. Vlach**, cada um documentado no respectivo `claim_id`. O guia é um caderno didático de 1990-2000 do IGc-USP, excelente e ainda plenamente utilizável, mas com erratas tipográficas e um quadro de nomenclatura anterior a revisões da IMA. As cinco correções estão listadas em **"Correções da fonte primária ratificadas"**, mais abaixo, e todas foram reverificadas por cálculo ou por fonte independente nesta auditoria.

## Achados

### 🟠 [TECTO-M40-A06-GOLDSMITH-001] — Atribuição autoral do grau de triclinicidade Δ
**Aula:** 06. **Claim relacionado:** `TECTO-M40-A06-TRICLINICIDADE-009`.
**Achado:** a redação original da aula 06 atribuía o índice de triclinicidade Δ = 12,5 × (d₁₃₁ − d₁̄₃₁) a "**Goldschmidt** & Laves", reproduzindo a grafia do item IX.4 do guia. A autoria correta é de **J. R. Goldsmith** e **F. Laves**, em *The microcline–sanidine stability relations* (Geochimica et Cosmochimica Acta, v. 5, p. 1–19, 1954). **Julian R. Goldsmith** (Universidade de Chicago, petrólogo experimental) é pessoa distinta de **Victor Moritz Goldschmidt**, o geoquímico — cuja *regra das fases mineralógicas* (P = C) aparece, corretamente atribuída, na aula 14. Um leitor que buscasse a referência pelo nome grafado no guia não a encontraria, e a coexistência dos dois sobrenomes em aulas diferentes do mesmo módulo tornava a confusão especialmente provável.
**Correção proposta:** aplicada. Na aula 06 foram corrigidos o corpo do texto (linha do grau de triclinicidade), a seção "Fontes" — com a referência bibliográfica completa e uma nota de auditoria explicitando o contraste com V. M. Goldschmidt — e o campo `source` do claim. A aula 14 foi verificada e **não** requer alteração: a atribuição da regra das fases mineralógicas a Goldschmidt está correta.
**Confiança:** alta.

### 🟡 [TECTO-M40-A14-SIO2-002] — Percentagens em peso de SiO₂ da leucita e do feldspato potássico
**Aula:** 14. **Claim relacionado:** `TECTO-M40-A14-PERITETICO-006`.
**Achado:** a aula reproduzia os valores ~54,5 % e ~65,5 % de SiO₂ em peso para leucita e feldspato potássico, lidos do eixo da Figura 19 do guia, que é explicitamente esquemática. Esses valores são **estequiométricos exatos** e não dependem de leitura de figura: KAlSi₂O₆ tem massa molar 218,25 g/mol e contém 2 × 60,08 = 120,17 g de SiO₂, logo **55,06 %**; KAlSi₃O₈ tem massa molar 278,33 g/mol e contém 3 × 60,08 = 180,25 g de SiO₂, logo **64,76 %**. Os desvios (+0,6 e −0,7 pontos percentuais) são pequenos, mas gratuitos: um aluno que reconstrua o diagrama pelas fórmulas obterá números diferentes dos da aula e não saberá qual está certo.
**Correção proposta:** aplicada. Corpo, recap e claim da aula 14 passaram a registrar **55,1 %** e **64,8 %**, com o cálculo estequiométrico explicitado e uma nota de que o guia lê valores ligeiramente distintos do eixo esquemático.
**Confiança:** alta (aritmética fechada).

### 🟡 [TECTO-M40-A12-ZEOLITAS-003] — Nomenclatura e contagem das zeólitas
**Aula:** 12. **Claim relacionado:** `TECTO-M40-A12-NOMENCLATURA-009` (já classificado como `desatualizado` na própria aula).
**Achado:** o guia trabalha com "cerca de quatro dezenas" de zeólitas naturais e com a **classificação estrutural de Breck** em 7 grupos, que era o padrão à época. O quadro foi superado: o relatório de nomenclatura da Subcomissão de Zeólitas da IMA (**Coombs et al., 1997**) e suas revisões reconhecem bem mais de setenta espécies naturais, e a descrição estrutural corrente usa os **códigos de tipo de arcabouço de três letras da International Zeolite Association** (CHA para chabasita, NAT para natrolita, ANA para analcima, FAU para faujasita etc.). A classificação de Breck continua didaticamente útil como porta de entrada às unidades secundárias, mas não é a referência de nomenclatura vigente.
**Correção proposta:** nenhuma adicional. A aula 12 já apresenta Breck como quadro histórico-didático e já traz o claim de atualização com as referências corretas, o que é o tratamento adequado — preservar o esqueleto conceitual do guia e sinalizar onde a nomenclatura andou.
**Confiança:** alta.

### 🟡 [TECTO-M40-A03-OPALA-004] — Opala e moganita: o quadro moderno da sílica cripto/paracristalina
**Aula:** 03. **Claim relacionado:** `TECTO-M40-A03-OPALA-006` (já classificado como `desatualizado` na própria aula).
**Achado:** o guia trata a opala como uma variedade **única e amorfa** de sílica hidratada. A literatura posterior separa **opala-A** (genuinamente amorfa) de **opala-CT** e **opala-C** (paracristalinas, com domínios de empilhamento de cristobalita e tridimita detectáveis por difração). No mesmo campo, a **moganita** — polimorfo monoclínico de SiO₂ intercrescido em muitas calcedônias — foi descrita, teve seu status contestado em 1994 e é **espécie aceita pela IMA desde 1999**, o que muda a leitura do que "calcedônia" é em nível estrutural. A aula 02 já usa o quadro moderno ao tratar a contagem de "oito polimorfos" como ordem de grandeza e não inventário canônico.
**Correção proposta:** nenhuma adicional. A aula já registra a atualização no claim e sinaliza no corpo que a contagem clássica do guia não é fechada.
**Confiança:** alta.

### 🔵 [TECTO-M40-A02-TRIDIMITA-005] — Estabilidade da tridimita em SiO₂ puro
**Aula:** 02. **Claim relacionado:** `TECTO-M40-A02-TRIDIMITA-DEBATE-010`.
**Achado:** debate experimental legítimo e não encerrado. O diagrama P–T clássico (reproduzido no guia a partir de Klein & Hurlbut) atribui à tridimita um campo de estabilidade próprio entre quartzo e cristobalita a pressões baixas. Parte significativa da literatura experimental posterior sustenta que, em SiO₂ **quimicamente puro**, a tridimita é **metaestável** em relação à cristobalita, e que sua ocorrência natural depende de estabilização por pequenas quantidades de álcalis e de Al — exatamente os elementos que a aula 01 já explica serem tolerados pelas estruturas expandidas de alta temperatura. A fronteira tridimita/cristobalita é a linha menos firme do diagrama.
**Correção proposta:** nenhuma. A aula já trata o ponto em "O que não concluir", nomeando-o como debate e preservando o diagrama clássico como mapa didático — que é o tratamento correto. O aviso adjacente sobre o limite de uso geobarométrico de tridimita e cristobalita reforça a cautela no ponto certo.
**Confiança:** alta.

### 🔵 [TECTO-M40-A03-QUIRALIDADE-006] — Emparelhamento grupo espacial ↔ dextrogiro/levogiro, e a quiralidade nas leis de geminação
**Aula:** 03. **Claims relacionados:** `TECTO-M40-A03-GRUPOS-002` e `TECTO-M40-A03-BRASIL-003`.
**Achado:** dois pontos distintos, ambos genuinamente conflitantes entre fontes respeitáveis.
(a) Os grupos espaciais do quartzo α são P3₁21 e P3₂21 (β: P6₂22 e P6₄22), mas **qual deles corresponde ao cristal "dextrogiro"** depende da convenção adotada — sentido do eixo helicoidal estrutural versus sentido da rotação óptica observada —, e as fontes divergem no emparelhamento. A aula registra a divergência em vez de escolher um lado sem aviso, o que é o procedimento correto.
(b) Mais importante: a aula afirma, seguindo **Frondel (1962, System of Mineralogy v. III)** e Heaney et al. (1994), que a **Lei do Brasil relaciona indivíduos de quiralidades opostas** (por reflexão, geminação de crescimento), enquanto a **Lei de Dauphiné relaciona indivíduos de mesma quiralidade** (rotação de 180° em torno de c, geminação secundária ligada à inversão β→α). Esta é a leitura corrente e majoritária da literatura de referência — e ela **diverge do guia**, que atribui mesma quiralidade a ambas as leis. A aula sinaliza a divergência no campo `source` do claim.
**Correção proposta:** nenhuma. A aula adota a posição da literatura de referência e declara explicitamente que diverge da fonte primária, com a citação que sustenta a escolha. É exatamente o que uma divergência fundamentada deve fazer.
**Confiança:** alta para (b); média-alta para (a), onde a divergência é de convenção, não de fato.

### 🔵 [TECTO-M40-A07-LACUNAS-007] — Limites composicionais das três lacunas dos plagioclásios
**Aula:** 07. **Claim relacionado:** `TECTO-M40-A07-LACUNAS-007`.
**Achado:** os intervalos das lacunas de peristerita (An₂–An₂₆), Bøggild (An₄₅–An₅₅) e Huttenlocher (An₇₀–An₈₀) reproduzidos do guia estão dentro da faixa reportada na literatura, mas **não são valores consensuais fechados**: diferentes autores publicam limites apreciavelmente distintos (a peristerita aparece como An₀–An₁₇ ou An₀–An₂₅ conforme a fonte; a Huttenlocher chega a An₆₇–An₉₀ em Smith & Brown, 1988), porque os limites dependem da temperatura, do estado estrutural e do critério experimental de detecção do intercrescimento. Trate-os como faixas orientativas, não como fronteiras determinadas.
**Correção proposta:** nenhuma obrigatória. Como refinamento futuro, a aula 07 poderia explicitar que os limites variam com a fonte e com a temperatura, à maneira do que a aula 02 faz com a contagem de polimorfos.
**Confiança:** alta.

### ⚪ [TECTO-M40-A07-RAIOS-008] — Raios iônicos de Na⁺ e K⁺ dependem do número de coordenação
**Aula:** 07. **Claim relacionado:** `TECTO-M40-A07-RAIOS-002`.
**Achado:** os valores Na⁺ = 0,97 Å e K⁺ = 1,33 Å são os clássicos de Pauling/Goldschmidt para **coordenação 6**. Nos sítios M dos feldspatos a coordenação real é bem maior (tipicamente 6–9 para o Na, 9–10 para o K), e a tabulação de **Shannon (1976)**, hoje padrão, dá valores substancialmente diferentes (Na⁺ ≈ 1,18 Å e K⁺ ≈ 1,51 Å em CN 8). O que o argumento da aula precisa — e o que sobrevive intacto em qualquer tabulação — é a **diferença relativa** entre os dois cátions, que é da ordem de 35–40 % e é o que torna a acomodação simultânea progressivamente impossível ao baixar a temperatura.
**Correção proposta:** nenhuma. A aula já registra a dependência do número de coordenação no campo `source` do claim, e o raciocínio físico não depende dos valores absolutos.
**Confiança:** alta.

### ⚪ [TECTO-M40-A13-SOMA-M-009] — Terceira casa decimal da soma M na Tabela 1 recalculada
**Aula:** 13. **Claim relacionado:** `TECTO-M40-A13-BARIO-006`.
**Achado:** o recálculo independente desta auditoria a partir dos dados brutos da Tabela 1 do guia (SiO₂ 65,76; Al₂O₃ 20,23; Fe₂O₃ 0,18; BaO 0,63; CaO 1,29; Na₂O 8,44; K₂O 3,69) confirma integralmente a correção feita pela aula: soma de O = 2,990, F = 10,702, e **Ba = 0,044** cátions por 32 O (o guia registra 0,004, que é a proporção catiônica **antes** da multiplicação por F). Confirma também as proporções corrigidas de membros finais, **An₆,₁Ab₇₂,₁Or₂₀,₇Cs₁,₁**. A única discrepância é de terceira casa: a aula registra ΣM = 4,035 e este recálculo obtém **ΣM ≈ 4,044** (0,044 + 0,246 + 2,915 + 0,839), diferença atribuível a arredondamentos intermediários e à tabela de pesos atômicos empregada.
**Correção proposta:** nenhuma obrigatória — a diferença é de 0,009 unidade de fórmula, muito abaixo de qualquer significado cristaloquímico, e não altera a classificação nem as proporções de membros finais. Registrado para rastreabilidade.
**Confiança:** alta.

### ⚪ [TECTO-M40-A04-CRISTOBALITA-010] — Sinal óptico da cristobalita de baixa, tomado de fonte determinativa
**Aula:** 04. **Claim relacionado:** `TECTO-M40-A04-CRISTOBALITA-SINAL-006`.
**Achado:** o trecho correspondente do item II.3 do guia está ilegível na extração do PDF, e o valor foi tomado das obras determinativas que o próprio guia adota como referência de bancada (Tröger, 1979; DHZ, 1992): cristobalita α **uniaxial negativa**, ω ≈ 1,487, ε ≈ 1,484. Verificado contra as tabelas determinativas padrão — os valores conferem e são consensuais. Achado registrado apenas porque a cadeia de custódia até a fonte primária do módulo está interrompida neste ponto específico, não porque haja dúvida sobre o dado.
**Correção proposta:** nenhuma.
**Confiança:** alta.

## Correções da fonte primária ratificadas

Cinco pontos em que as aulas corrigem o guia. Todos reverificados nesta auditoria; nenhum permanece em aberto.

| # | Aula | O que o guia registra | O que está correto | Verificação |
|---|---|---|---|---|
| 1 | 04 | "atraso de 0,009 nm" para o quartzo | 0,009 é a **birrefringência** (adimensional); o **atraso** em lâmina de 30 µm é δ = 30 000 nm × 0,009 = **270 nm** | Aritmética fechada ✅ |
| 2 | 11 | "birrefringência 0,002 nm" para a leucita | idem: 0,002 é adimensional; atraso ≈ 30 000 × 0,002 = **60 nm** | Aritmética fechada ✅ |
| 3 | 06 | grupo espacial "P2/m (C2/m)" dos feldspatos potássicos monoclínicos | **C2/m** — "P2/m" é lapso tipográfico, incompatível com a estrutura de anéis duplos centrada | DHZ 1992; Ribbe 1975 ✅ |
| 4 | 07 | labradorescência atribuída ao intercrescimento de **Huttenlocher** | a labradorescência é produzida pelo intercrescimento de **Bøggild** (An₄₅–An₅₅) | Ribbe 1975; Smith & Brown 1988 ✅ |
| 5 | 13 | Tabela 1: Ba = 0,004 na fórmula estrutural; An₆,₁Ab₇₂,₈Or₂₀,₉Cs₀,₁ | Ba = **0,044** (proporção catiônica não multiplicada por F); **An₆,₁Ab₇₂,₁Or₂₀,₇Cs₁,₁** | Recálculo independente ✅ (ver ⚪-009) |

## Verificação amostral de cálculos e valores (checklist)

**Fórmulas estruturais e proporções de membros finais (aulas 13 e 14)**
- Tabela 1 (feldspato alcalino baritífero) recalculada do zero: ΣO = 2,990 · F = 10,702 · Si 11,714 · Al 4,247 · Fe³⁺ 0,024 · Ba 0,044 · Ca 0,246 · Na 2,915 · K 0,839 · ΣT = 15,984. Confere com a aula, com a ressalva de 3ª casa em ΣM registrada em ⚪-009. ✅
- Análise F1 da Tabela 2 recalculada do zero (SiO₂ 66,97; Al₂O₃ 18,75; Fe₂O₃ 0,88; CaO 0,36; Na₂O 7,88; K₂O 5,39): ΣO = 2,9882 · F = 10,7086 · fórmula (Ca₀,₀₇Na₂,₇₂K₁,₂₃)(Al₃,₉₄Fe³⁺₀,₁₂Si₁₁,₉₄)O₃₂ · ΣT = 15,992 · ΣM = 4,017 · **An₁,₇Ab₆₇,₈Or₃₀,₅**. Confere exatamente. ✅
- Classificação de F1 como **anortoclásio**: Or 30,5 % molecular < 37 %, o limite anortoclásio/sanidina adotado no item III.1.1 do guia. Internamente consistente. ✅
- Conversão molar → peso de F1 para uso na Figura 21 (aula 14): normalização ao binário Ab–Or dá Ab 68,96 / Or 31,04 mol %; com PM(Ab) = 262,22 e PM(Or) = 278,33 g/mol resulta **Ab₆₇,₇Or₃₂,₃ em peso**. Recalculado e confere. ✅
- Regra dos segmentos proporcionais (regra da balança) aplicada ao solvus dos feldspatos alcalinos (aulas 07 e 14): formulação consistente com Ribbe (1975). ✅

**Óptica e cristalografia**
- Atraso do quartzo: 30 µm × 0,009 = 270 nm, coerente com cores de interferência de cinza claro a branco de 1ª ordem. ✅
- Atraso da leucita: 30 µm × 0,002 = 60 nm, coerente com o caráter quase isótropo. ✅
- Índices do quartzo (ω 1,544 / ε 1,553, uniaxial positivo, Δ = 0,009); nefelina (ε 1,525 / ω 1,545, uniaxial negativa); leucita (n ≈ 1,51, uniaxial positiva); analcima (n = 1,485, isótropa); sodalita (n ≈ 1,48, isótropa, subindo a ~1,50 com SO₄); opala (n ≈ 1,46, isótropa); cristobalita α (ω 1,487 / ε 1,484, uniaxial negativa): todos conferidos contra Tröger (1979) e DHZ (1992). ✅
- Grupos espaciais: sanidina e ortoclásio C2/m; microclínio C1̄; albita alta e baixa C1̄; monalbita C2/m; anortita I1̄; nefelina e kalsilita P6₃; leucita tetragonal I4₁/a; sodalita P4̄3n; chabasita R3̄m. Conferidos contra DHZ (1992). ✅
- Ângulo agudo entre os traços de {010} e {001} em cortes (100) ≈ 87° (aula 10): consistente com a geometria triclínica dos plagioclásios em DHZ (1992). ✅
- Simetrias α/β de quartzo (32 / 622), tridimita (ortorrômbica / hexagonal) e cristobalita (tetragonal / cúbica). ✅

**Termodinâmica e relações de fases**
- Regra das fases de Gibbs F + P = C + 2 e sua forma isobárica F + P = C + 1; aplicação ao diagrama unário da sílica (campo divariante, curva univariante, ponto triplo invariante). ✅
- Regra das fases mineralógicas de Goldschmidt (F = 2 ⇒ P = C) — atribuição a V. M. Goldschmidt correta na aula 14 (contrastar com o achado 🟠-001, que trata de outro autor). ✅
- Inversão β→α do quartzo a 573 °C sob 1 atm, com inclinação positiva dP/dT pela equação de Clapeyron. ✅
- Coesita acima de ~20 kbar e stishovita acima de ~75 kbar; coordenação **octaédrica** do Si na stishovita explicando ρ ≈ 4,35 g/cm³. ✅
- Densidades: tridimita 2,26 · cristobalita 2,32 · quartzo α 2,65 · coesita ~3,00 · stishovita ~4,35; zeólitas 2,0–2,5; nefelina 2,56–2,67; leucita 2,49; sodalita 2,27–2,50; analcima 2,27. ✅
- Sistema Ab–SiO₂ eutético (Tuttle & Bowen, 1958); Lc–SiO₂ peritético (Schairer & Bowen, 1955, in DHZ 1992); Ab–An solução sólida completa (Bowen, 1913, in DHZ 1992); Ab–Or com ponto de mínimo (Tuttle & Bowen, 1958). Atribuições conferidas. ✅
- Barreira térmica albítica no sistema NaAlSiO₄–SiO₂ e a assimetria em relação ao sistema potássico (onde o peritético permite atingir composições saturadas). Raciocínio conferido contra o item VII.2 do guia e DHZ (1992). ✅
- Efeito de P(H₂O): desloca liquidus e solidus para T menores **sem** deslocar o solvus; a ~2,5 kbar o solidus intercepta o solvus e o mínimo vira eutético (dois feldspatos). Consistente com Tuttle & Bowen (1958). ✅

**Química e abundância**
- Abundância crustal em % peso: O 46,60 · Si 27,72 · Al 8,13 · Fe 5,00 · Ca 3,63 · Na 2,83 · K 2,59 · Mg 2,09, somando 98,59 % (Mason & Moore, 1982). ✅
- Abundância modal: plagioclásio 39 % · quartzo 12 % · feldspato alcalino 12 % (Ronov & Yaroshevsky, 1969), com a ressalva — já feita na aula 01 — de que é estimativa de modelo, não medida. ✅
- Limites de nomenclatura dos plagioclásios por % molecular de An (10/30/50/70/90). ✅
- Estequiometria das três reações da barreira de saturação em sílica (equações IV.1 a IV.3 do guia). ✅
- Feldspatos: Z = 4 na cela unitária ⇒ base de 32 O; leucita Z = 16 ⇒ cálculo sobre a fórmula mínima com 6 O. ✅

## Cobertura de objetivos de aprendizagem

| Objetivo | Aulas que cobrem | Verificado |
|---|---|---|
| geologia-avancado-m40-oa01 | a01, a11, a12 | ✅ |
| geologia-avancado-m40-oa02 | a02, a03, a04 | ✅ |
| geologia-avancado-m40-oa03 | a05, a06 | ✅ |
| geologia-avancado-m40-oa04 | a07, a09 | ✅ |
| geologia-avancado-m40-oa05 | a04, a08, a09, a10, a11, a12 | ✅ |
| geologia-avancado-m40-oa06 | a13, a14 | ✅ |

Os seis objetivos têm pelo menos duas aulas dedicadas e claims auditáveis correspondentes; nenhum objetivo ficou sem cobertura.

## Cobertura das Partes B e C do guia

O guia tem três partes. A **Parte A** (itens I a VII, teoria) está integralmente coberta pelas 14 aulas. As outras duas foram tratadas assim, e esta auditoria confirma que nada do conteúdo científico se perdeu:

- **Parte B — item VIII, atividades práticas ao microscópio.** São seis roteiros de bancada que pressupõem lâminas delgadas numeradas de uma litoteca e o guia de Tröger em mãos. Não viraram aula, porque uma aula que o aluno não pode executar não ensina; viraram a **Parte IV do questionário final** (roteiro prático), reformulada para ser respondível a partir das tabelas diagnósticas das aulas 04, 08, 09, 10, 11 e 12, e executável ao microscópio por quem tiver acesso a um. O item VIII.6 — o quadro comparativo geral que distingue feldspato alcalino, plagioclásio, quartzo e feldspatoide — é a questão de fechamento do questionário final e gerou um bloco próprio de flashcards.
- **Parte C — item IX, exercícios diversos.** Distribuída pelos três questionários: IX.1 (questões gerais) como dissertativas; IX.2 (fórmulas estruturais da Tabela 2) como questões de aplicação, tendo a aula 13 já resolvido a análise F1 como exemplo trabalhado; IX.3 (cristalização, exsolução e polimorfismo de F1) como questão integradora do questionário final; IX.4 (difratometria de raios X) já incorporada ao corpo da aula 06 e cobrada no parcial 1; IX.5 (diagramas de fase) cobrada no parcial 2 e no final.

## Recomendação

**Aprovar o módulo** para avaliação (questionários) e memorização (flashcards). As três correções aplicadas durante esta auditoria (uma 🟠 na aula 06, duas 🟡 na aula 14) já estão nos arquivos, propagadas para corpo, recap, seção "Fontes" e blocos de metadados conforme o caso. Os achados 🔵 e ⚪ ficam registrados como rastreabilidade e não exigem alteração: em todos eles o texto das aulas já trata a incerteza com a cautela adequada, nomeando o debate em vez de escolher um lado em silêncio.

Duas recomendações de refinamento futuro, ambas opcionais e nenhuma bloqueante:
1. Explicitar na aula 07 que os limites das três lacunas dos plagioclásios variam com a fonte, com a temperatura e com o critério de detecção (achado 🔵-007).
2. Ao revisar a aula 13, harmonizar a terceira casa decimal de ΣM da Tabela 1 com o recálculo desta auditoria (achado ⚪-009).
