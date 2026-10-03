# Auditoria científica — Módulo 31: Rochas ígneas alcalinas: petrologia e mineralizações

**Curso:** geologia-avancado
**Módulo:** 31 — `31-rochas-igneas-alcalinas` (7 aulas; a antiga Aula 03 foi dividida em Parte 1 e Parte 2)
**Modo:** `audit-and-fix` · **Profundidade:** `full`
**Passagens:** 1 (2026-09-24). Uma tentativa anterior foi interrompida por limite de sessão antes de gravar qualquer arquivo; esta passagem começou do zero. Backup do estado antes da auditoria: `course-state.yaml.bak-20260924-pre-m31-audit` (idêntico byte a byte ao estado no início desta passagem).
**Veredito:** **Aprovado após correções.** Foram levantados 4 vermelhos, 19 laranjas, 2 amarelos, 1 azul e 1 branco, e todos foram tratados nas aulas. Nada ficou em aberto.

---

## Resumo por severidade

| Severidade | Levantados | Corrigidos / tratados | Em aberto |
|---|---|---|---|
| 🔴 Erro | 4 | 4 | **0** |
| 🟠 Impreciso | 19 | 19 | **0** |
| 🟡 Desatualizado | 2 | 2 (valor ou nome antigo mantido como referência) | **0** |
| 🔵 Sem fonte | 1 | 1 (reescrito sem afirmar a base não confirmada) | 0 |
| ⚪ Controverso | 1 | 1 (reescrito como debate) | 0 |
| **Total** | **27** | **27** | **0** |

Gate de qualidade: **liberado** para o questionário e os flashcards (0 vermelhos e 0 laranjas em aberto), com as restrições do fim deste relatório.

### Inversões de sentido

- **🔴 1 (Aula 05) é a inversão perigosa do módulo.** A aula diz que Sørensen (1997) "formalizou geoquimicamente" o índice agpaítico e que IA ≥ 1 define a rocha agpaítica. É o contrário. A definição química (e com IA ≥ 1,2) é a **original** de Ussing (1912). Sørensen trocou a química pela **mineralogia**: agpaítica é a rocha peralcalina em que Zr e Ti estão em silicatos complexos (eudialita, rinkita), e não em zircão e titanita. IA > 1 define a rocha **peralcalina**, que pode ser miaskítica. O exemplo trabalhado classificava como "agpaítica" uma amostra com IA = 1,08 só pelo índice. Uma questão de V/F ou um flashcard sobre essa aula ensinaria o critério errado.
- **🟠 12 (Aulas 03 e 07)** contradiz o Módulo 30. A Aula 03 dizia que a imiscibilidade é "o processo que melhor explica" a associação de campo entre rochas silicáticas e carbonatitos. A Aula 07 omitia a cristalização fracionada. O Módulo 30, já auditado, atribui justamente a essa rota (a cristalização fracionada) a preferência das associações de campo, e trata a rota dominante como debate.

### Padrão dominante

O mesmo dos Módulos 27-30: os erros graves **não estavam na lista de risco da redação**. A etimologia inventada de "foid", o cenário físico impossível do exemplo da Aula 02, o índice agpaítico como critério e Araxá/Catalão como rota das ETR foram escritos como fatos seguros. Um segundo padrão é próprio deste módulo. A divisão da antiga Aula 03 deixou **remissões quebradas**: "Aula 08" e "Aula 09" não existem, e várias remissões apontavam para a aula anterior à certa.

---

## Nota de método

A redação declarou **36 alegações auditáveis** (a01 5, a02 6, a03 5, a04 5, a05 5, a06 5, a07 5). A auditoria criou mais 8: seis nas aulas (a01, a03, a04, a05, a06, a07, uma em cada) e duas de módulo (`ALK-M31-MOD-REMISSOES-001` e `ALK-M31-MOD-ANFIBOLIOS-002`). O total rastreado é **44**.

**Consistência com o Módulo 30** (auditado e fechado em 2026-09-23). Foi conferida ponto a ponto contra as aulas e as 17 restrições do relatório do Módulo 30:

| Ponto do Módulo 30 | Situação no Módulo 31 |
|---|---|
| Jacupiranguito = titanoaugita + magnetita + pouca nefelina (🟠 8 do M30) | A Aula 07 está coerente. A **Aula 01** reintroduzia uma variante do erro ("rica em magnetita e apatita") → 🟠 7. |
| Sequência calcita → dolomita → ferrocarbonato (M30, Aula 05) | A Aula 07 pulava o estágio dolomítico e dizia "sequência já vista no Módulo 30" → 🟠 21. |
| ETR em ferrocarbonatitos tardios e no regolito; bastnäsita, parisita, monazita (M30, Aulas 05 e 06) | A Aula 07 punha as ETR no envelope sienítico → 🟠 22. A Aula 05 punha Araxá e Catalão como rota dominante das ETR → 🔴 4. |
| Três rotas para carbonatito, não exclusivas; a cristalização fracionada é a preferida pelas associações de campo (M30, Aula 04) | Contrariado nas Aulas 03 e 07 → 🟠 12. |
| Fenitização: feldspato alcalino, aegirina, anfibólio sódico, perda de quartzo (M30, Aula 03) | A Aula 07 está **coerente** ("empobrece em sílica e enriquece em álcalis"). |
| APIP: seis complexos, pluma de Trindade atribuída por Gibson et al. (1995), ~90-80 Ma | Os complexos estão coerentes. O modelo da pluma aparece como fato fechado nos recaps → ⚪ 27 (a ressalva não contradiz o M30, que diz "atribuída por"). |
| Nb: Brasil com ~90 % ou mais da produção mineira (sem número exato) | Não repetido no M31; nenhum conflito. |
| Rayleigh C_L/C₀ = F^(D−1) e o exemplo 0,30^(−0,95) = 3,14 (M30, Aula 05) | **Coerente**: a Aula 04 usa a mesma equação e o mesmo fator. A equação de **fusão em lote** foi dita "já usada no Módulo 30" e não foi → 🟠 8. |
| Metassomatismo modal × críptico (M30, Aula 02) | **Coerente.** |
| Lamprófiros ultramáficos (UML) e kamafugitos (M30, Aulas 01 e 03) | A Aula 06 dizia que os lamprófiros formam "duas grandes séries", sem os UML → tratado em 🟠 18. |

**Ferramentas.** Buscas na web, com resumos de artigos e páginas de referência (Mindat, Wikipedia para localidades, USGS MCS 2026, GeoScienceWorld e SciELO). A página da ScienceDirect de Foley et al. (1987) recusou acesso (HTTP 403), e por isso o achado 🔵 26 ficou sem confirmação da base da razão K₂O/Na₂O. Convenção da escala do tempo: ICS, base do Berriasiano em 143,1 ± 0,6 Ma, já consultada na auditoria do Módulo 26 (2026-09-21).

---

## Achados

### 🔴 1. Índice agpaítico como critério da série agpaítica, e o papel de Sørensen invertido

**claim_id:** `ALK-M31-A05-INDICE-AGPAITICO-001` (também cobre `ALK-M31-A05-EXEMPLO-CALCULO-005`)
**Tipo:** erro factual (inversão)
**Onde:** Aula 05 · "O índice agpaítico: a régua que separa as duas séries"; "Exemplo trabalhado" (Interpretação e O que fixar); recap
**Está escrito:** "a distinção foi formalizada geoquimicamente por Sørensen (1997) através do índice agpaítico"; "IA < 1: rocha miaskítica"; "IA ≥ 1: rocha agpaítica"; "é o critério que a literatura usa para classificar essas rochas"; "Ambas as amostras são agpaíticas (IA ≥ 1)"; "IA = 1 é o limiar formal entre miaskítico e agpaítico"; e "(do groenlandês *agpat*, um lugar perto de Ivigtut)".
**Problema:**
- Ussing (1912) introduziu "agpaítico" com critério **químico**: nefelina-sienitos peralcalinos com (Na+K)/Al ≥ **1,2**.
- Sørensen (1960, 1997) passou a definição para a **mineralogia**, e é essa a que vale hoje (Le Maitre, 2002). Rocha agpaítica é a rocha peralcalina em que os HFSE ficam em silicatos complexos de Na-Ca-Zr-Ti com halogênios (eudialita, rinkita, wöhlerita). Na miaskítica, Zr e Ti ficam em zircão e titanita.
- (Na+K)/Al > 1 define a rocha **peralcalina**. É condição necessária para a assembleia agpaítica, mas não é suficiente: há nefelina-sienitos peralcalinos miaskíticos (ver a transição miaskítica → agpaítica em Marks et al., 2011).
- Agpat fica na borda leste do próprio complexo de Ilímaussaq, e não "perto de Ivigtut".
**Correção proposta:** Reescrever a seção: IA > 1 = peralcalina; miaskítica e agpaítica definidas pela assembleia acessória (Sørensen 1997; Le Maitre 2002); Ussing 1912 como origem, com o corte químico de 1,2. No exemplo, as duas amostras passam a ser "peralcalinas": a A (1,08) fica perto do limiar e pode ser miaskítica, a B (1,70) é forte candidata, e a classificação exige lâmina. O "O que fixar" e o recap mudam no mesmo sentido.
**Fonte:** Sørensen (1997), *Mineral. Mag.* 61, 485-498. Marks e Markl (2017), *Earth-Sci. Rev.* 173, 229-258 ("A global review on agpaitic rocks"). Marks, Hettmann, Schilling, Frost e Markl (2011), *J. Petrol.* 52, 439-455. Friis (2015), BC Geological Survey Paper 2015-3 ("Ussing (1912) introduced the term agpaitic [...] AI > 1.2"). · **Nível:** normativa (Le Maitre, 2002) e revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 05 (seção, exemplo, recap, alegações 001 e 005). A Aula 07 usa "sienito agpaítico" **por mineralogia** (eudialita), o que é coerente com a definição certa, e foi mantida. A Aula 01 ("condição química central para as séries...") só diz que a peralcalinidade é central, o que é compatível.

### 🔴 2. Etimologia inventada de "foid" e o termo inexistente "foiolito"

**claim_id:** `ALK-M31-A01-FOID-FOIDOLITO-006` (criado pela auditoria)
**Tipo:** erro factual
**Onde:** Aula 01 · "Onde entram as rochas alcalinas no diagrama QAPF"; "Nomenclatura plutônica"; "Um histórico de nomes regionais"
**Está escrito:** "**Foiolito** e 'foid' derivam do grego *phelloeides* (semelhante a cortiça), termo cunhado por Rosenbusch"; "o termo 'foiolito' funciona como guarda-chuva histórico"; "foiolito e outros termos de campo central, até as foiditas [...] no vértice F".
**Problema:** "Foid" é a **contração de *feldspathoid***, proposta por Johannsen. Não há raiz grega de cortiça nem autoria de Rosenbusch. O termo da IUGS é **foidolito**: rocha plutônica do campo 15 do QAPF, com mais de 60 % de foides entre os félsicos, no **vértice F**, e não num "campo central". É o nome recomendado hoje, e não um guarda-chuva histórico. O equivalente vulcânico é o foidito.
**Correção proposta:** "foidolito (campo 15, vértice F; equivalente plutônico do foidito)". Os campos centrais do triângulo inferior são os de foide-monzossienito, foide-monzodiorito/monzogabro e foide-diorito/gabro. "Foid" é a contração de "feldspatoide" (Johannsen).
**Fonte:** Le Maitre (2002), QAPF plutônico, campo 15 e glossário. Mindat, glossário "foid" ("proposed by Johannsen [...] contracting the word feldspathoid"). · **Nível:** normativa
**Confiança:** confirmado
**Também aparece em:** só na Aula 01 (três pontos). Nenhum outro módulo usa "foiolito".

### 🔴 3. Exemplo da Aula 02: fusão em fácies de espinélio (< 70 km) sob uma litosfera de 150 km

**claim_id:** `ALK-M31-A02-EXEMPLO-006`
**Tipo:** erro factual (cenário físico impossível)
**Onde:** Aula 02 · "Exemplo trabalhado"
**Está escrito:** "sob uma mesma coluna litosférica continental de 150 km de espessura [...] Cenário A [...] descompressão até a base da litosfera [...] Fácies dominante: espinélio (fusão majoritariamente rasa, <70 km). Resultado: basalto toleítico".
**Problema:** Se o manto sobe só até a base de uma litosfera de 150 km, a fusão para em ~150 km, dentro da fácies da granada, e em baixo grau. A litosfera espessa funciona como "tampa" (Ellam, 1992): limita a coluna de fusão e favorece justamente líquidos alcalinos de baixo grau com assinatura de granada. Fusão de 12-15 % em fácies de espinélio exige litosfera fina (rifte avançado, oceano). O exemplo ensinava o modelo mental errado sobre o controle mais importante do tipo de basalto intraplaca.
**Correção proposta:** O Cenário A passa a ser sob litosfera **adelgaçada** (base a ~60 km, rifte avançado), onde a descompressão chega à fácies do espinélio. O Cenário B fica sob litosfera espessa, com fusão presa na fácies da granada. A "Leitura" acrescenta a espessura da litosfera como limite da profundidade de fusão.
**Fonte:** Ellam (1992), *Geology* 20, 153-156. Niu (2021), *Earth-Sci. Rev.* 217, 103614 (revisão: a espessura da litosfera controla a extensão da fusão e a profundidade de extração). · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** só no exemplo da Aula 02 e na alegação 006.

### 🔴 4. "Carbonatitos residuais lateríticos como Araxá e Catalão são a rota dominante de produção mundial" de ETR

**claim_id:** `ALK-M31-A05-PRODUCAO-ETR-006` (criado pela auditoria)
**Tipo:** erro factual (confusão Nb × ETR)
**Onde:** Aula 05 · "Por que isso importa para exploração mineral"
**Está escrito:** "Isso não significa que todo depósito de ETR em rocha alcalina seja agpaítico — carbonatitos residuais lateríticos, como Araxá e Catalão (Módulo 30), são a rota dominante de produção mundial atual".
**Problema:** Araxá e Catalão dominam a produção de **nióbio**, não a de ETR. A produção mundial de ETR é dominada pela China (~69 % da produção mineira em 2025, USGS): Bayan Obo (carbonatítico, de origem debatida) e as argilas de adsorção iônica do sul da China. Mountain Pass (carbonatito primário) e Mount Weld (carbonatito com enriquecimento laterítico) vêm depois. O Módulo 30 (Aula 06) dá exatamente esses depósitos para as ETR.
**Correção proposta:** "os depósitos ligados a carbonatitos, como Bayan Obo, Mountain Pass e Mount Weld (Módulo 30), respondem, junto com as argilas de adsorção iônica do sul da China, pela maior parte da produção mundial atual de ETR; Araxá e Catalão, lateríticos, dominam a de nióbio".
**Fonte:** USGS, *Mineral Commodity Summaries 2026*, Rare Earths (China 270.000 t ÓTR de ~390.000 t). Módulo 30, Aula 06 (já auditada). · **Nível:** normativa (USGS)
**Confiança:** confirmado
**Também aparece em:** só na Aula 05.

### 🟠 5. Classificação de Shand sem o CaO; piroxênio e anfibólio sódicos chamados de "félsicos"

**claim_id:** `ALK-M31-A01-TRES-SENTIDOS-001` (também cobre o passo 2 de `ALK-M31-A01-EXEMPLO-005`)
**Tipo:** omissão que gera erro
**Onde:** Aula 01 · "Um termo usado em três sentidos diferentes", item 2; "Exemplo trabalhado", passo 2
**Está escrito:** "entre subunidade e a linha de saturação total é **metaluminosa**; e quando falta álcali para saturar o alumínio (sobra Al para minerais como muscovita ou córindon), a rocha é **peraluminosa**" e "sobrando álcali para entrar em minerais félsicos ricos em Na (piroxênio e anfibólio sódicos".
**Problema:** A classificação de Shand usa **dois** índices molares: A/NK = Al/(Na+K) e A/CNK = Al/(Ca+Na+K). Peralcalina: Al < Na+K. Metaluminosa: Na+K < Al < Ca+Na+K. Peraluminosa: Al > Ca+Na+K. Faltar álcali para o Al (A/NK > 1) **não** faz a rocha peraluminosa: se o Ca cobre o excesso, ela é metaluminosa. Aegirina e arfvedsonita são minerais **máficos**.
**Correção proposta:** Reescrever o item com os dois índices e trocar "félsicos" por "máficos sódicos".
**Fonte:** Shand (1943), *Eruptive Rocks*; Maniar e Piccoli (1989), *GSA Bull.* 101, 635-643 (A/CNK × A/NK). · **Nível:** revisada por pares (convenção consolidada)
**Confiança:** confirmado
**Também aparece em:** Aula 01 (recap: "peralcalina/metaluminosa/peraluminosa", sem definição, e mantido).

### 🟠 6. "A IUGS organiza a nomenclatura vulcânica em clãs químicos subdivididos por índice de saturação"

**claim_id:** `ALK-M31-A01-CLAS-003`
**Tipo:** confusão de escopo (atribuição)
**Onde:** Aula 01 · "Clãs alcalinos: como a IUGS organiza a nomenclatura vulcânica"; recap
**Está escrito:** "Le Maitre (2002) complementa o QAPF com uma classificação em **clãs químicos** [...] cada um subdividido por índice de saturação (mistura de normativos de quartzo, hiperstênio, olivina e nefelina...)".
**Problema:** Para rochas vulcânicas sem moda determinável, a IUGS usa o diagrama **TAS** (Le Bas et al., 1986; Le Maitre, 2002). Nele, basanito e tefrito se separam por olivina **normativa** maior ou menor que 10 %, e havaíto, mugearito e benmoreíto são as variedades **sódicas** de traquibasalto, traquiandesito basáltico e traquiandesito (Na₂O − 2 ≥ K₂O). Os melilititos têm classificação própria e não entram no TAS. Agrupar os campos do TAS em "clãs" ou séries é convenção didática da literatura de rochas alcalinas, e não categoria formal da IUGS. O objetivo do módulo usa "clãs", e o termo pode ficar, desde que dito como convenção.
**Correção proposta:** Atribuir a classificação química ao TAS, dizer que os "clãs" agrupam campos do TAS por linhagem, corrigir a subdivisão (olivina normativa 10 %; variedades sódicas) e tirar o melilitito do TAS.
**Fonte:** Le Bas, Le Maitre, Streckeisen e Zanettin (1986), *J. Petrol.* 27, 745-750. Le Maitre (2002), seções TAS e rochas melilíticas. · **Nível:** normativa
**Confiança:** confirmado
**Também aparece em:** recap da Aula 01.

### 🟠 7. Topônimos e definições: "Ilha de Fen", "rio Lujavr-Urt", "Morro do Tinguá" e jacupiranguito "rico em apatita"

**claim_id:** `ALK-M31-A01-TOPONIMOS-004`
**Tipo:** impreciso (e reintrodução de um erro corrigido no Módulo 30)
**Onde:** Aula 01 · "Um histórico de nomes regionais"; recap
**Está escrito:** "**Fenita** vem da Ilha de Fen"; "Jacupiranguito [...] nomeia uma clinopiroxenito rica em magnetita e apatita"; "**Tinguaíto** vem do Morro do Tinguá (RJ), um traquito nefelínico hipoabissal"; "**Lujavrito**, do rio Lujavr-Urt".
**Problema:**
- Fen não é ilha: é o complexo de Fen, em Nome, Telemark, nomeado pela fazenda Fen. O título do próprio Brøgger (1921) diz "Das Fengebiet in Telemark".
- O Módulo 30 corrigiu o jacupiranguito para **clinopiroxenito com nefelina, essencialmente titanoaugita e magnetita, com pouca nefelina** (Derby, 1891). A apatita não é mineral definidor.
- O tinguaíto é de Rosenbusch (1887), da serra (maciço) do Tinguá. É um **fonolito** hipabissal com aegirina abundante, e "fonolito intrusivo" é o termo preferido hoje.
- Lujavr-Urt é o nome sami do **maciço** de Lovozero, e não um rio. O lujavrito é de Brøgger (1890).
**Correção proposta:** Corrigir os quatro itens e alinhar o jacupiranguito ao texto do Módulo 30.
**Fonte:** Mindat, "Fen Complex, Nome, Telemark"; Wikipedia, "Fen Complex" (nome da fazenda Fen); Le Maitre (2002), glossário (tinguaite, lujavrite, jacupirangite); Wikipedia (de), "Lujavrit" (Brøgger 1890; Luijaur/Lujavr-Urt, Lovozero); Módulo 30, 🟠 8. · **Nível:** normativa (glossário IUGS) e base de referência
**Confiança:** confirmado
**Também aparece em:** recap da Aula 01. A Aula 07 dá o jacupiranguito como "clinopiroxênio titanífero e magnetita", o que é coerente.

### 🟠 8. Remissões quebradas depois da divisão da Aula 03, e fusão em lote "já usada no Módulo 30"

**claim_id:** `ALK-M31-MOD-REMISSOES-001` (criado pela auditoria; também cobre a parte "já usada no módulo 30" de `ALK-M31-A04-EQUACOES-004`)
**Tipo:** inconsistência interna e entre módulos
**Onde:** Aulas 01, 02, 03, 04 e 05; metadados `divisao_de_aula` das Aulas 03 e 04
**Está escrito / problema:**
- Aula 01: "os clãs que a Aula 04 a 08 vão detalhar" (não há Aula 08); "(Aula 04)" e "na Aula 04" para sienito, miaskítico e agpaítico (é a 05); "tratada na Aula 07 como parte dos stocks cumuláticos" (é a 06); "conceito que volta na Aula 09" e "(SP, Brasil; Aula 09 e módulo 30)" (não há Aula 09; é a 07); "clã sienítico na Aula 04" e "que a Aula 04 desenvolve" (é a 05).
- Aula 02: "ver Aula 09 e módulo 30" e "(Aula 09)" (é a 07); "padrões geoquímicos que a Aula 03 vai interpretar" (é a 04).
- Aula 03: "tema central da Aula 09" e "(tema da Aula 09)" (é a 07); "Aula 05 e 06" para eudialita e fluorita (a eudialita está na 05; a 06 não trata disso).
- Aula 04: "sienitos agpaíticos da Aula 06" (é a 05); "A Aula 05 (em duas partes)" (a Aula 05 é única). "Duas equações [...] retomadas do módulo 30" e, nas Fontes, Shaw (1970) "já usada no módulo 30": o Módulo 30 usa **só Rayleigh** (Aula 05). A fusão em lote é nova neste módulo.
- Aula 05: Khibiny "mais conhecido pela mineralização de apatita [...] discutida [...] nas aulas seguintes deste módulo": nenhuma aula seguinte discute isso.
- Metadados das Aulas 03 e 04: "antigas a04, a05, a06 tornam-se a05/a06, a07/a08, a09". O mapeamento real, que o hub registra, é 04 → 05, 05 → 06 e 06 → 07.
**Correção proposta:** Corrigir cada remissão, a frase das equações, a fonte de Shaw e o mapeamento dos metadados.
**Fonte:** o próprio módulo (hub e arquivos); Módulo 30 (busca por "Shaw", "fusão em lote" e "batch": nenhuma ocorrência). · **Nível:** interno
**Confiança:** confirmado

### 🟠 9. Grau de fusão como único controle da saturação em sílica; a pressão aparece só para as ETR pesadas

**claim_id:** `ALK-M31-A02-GRAU-FUSAO-001`
**Tipo:** omissão que gera erro
**Onde:** Aula 02 · "Por que baixo grau de fusão parcial gera magma insaturado em sílica", terceiro parágrafo
**Está escrito:** "A profundidade de fusão também importa: fusão em fácies de granada [...] muda o comportamento dos elementos terras raras pesadas".
**Problema:** A pressão é, ao lado do grau de fusão, controle **direto** da saturação em sílica. Com o aumento da pressão, o campo da olivina se expande, e líquidos de mesmo grau de fusão ficam mais pobres em sílica e mais insaturados. É o argumento central de Green e Ringwood (1967) e dos experimentos seguintes. Como escrito, o aluno conclui que a profundidade só mexe nas ETR pesadas.
**Correção proposta:** "A profundidade de fusão também importa, de duas formas: quanto maior a pressão, mais pobre em sílica e mais insaturado é o líquido para um mesmo grau de fusão; e, em fácies de granada [...] muda o comportamento das ETR pesadas".
**Fonte:** Green e Ringwood (1967), *Contrib. Mineral. Petrol.* 15, 103-190; Hirose e Kushiro (1993), *EPSL* 114, 477-489. · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** a "Leitura" do exemplo da Aula 02 (ajustada junto com 🔴 3).

### 🟠 10. "Série subalcalina/toleítica [...] a chamada série calcialcalina de Bowen"

**claim_id:** `ALK-M31-A03-SERIE-SUBALCALINA-006` (criado pela auditoria)
**Tipo:** impreciso (terminologia)
**Onde:** Aula 03 · "Por que magmas alcalinos não seguem para granito", primeira frase
**Problema:** Mistura séries distintas. Toleítica e calcialcalina são as duas séries subalcalinas (a toleítica, com enriquecimento em Fe). A série de reação de Bowen não é "a série calcialcalina".
**Correção proposta:** "Em uma série subalcalina (toleítica ou calcialcalina), a cristalização fracionada de um basalto tende a produzir termos cada vez mais ricos em sílica (andesito ou islandito, dacito e, por fim, riolito/granito)."
**Fonte:** Irvine e Baragar (1971); Le Maitre (2002). · **Nível:** normativa
**Confiança:** confirmado

### 🟠 11. Imiscibilidade silicato-carbonato "documentada experimentalmente desde os anos 1980"

**claim_id:** `ALK-M31-A03-IMISCIBILIDADE-003`
**Tipo:** impreciso (data)
**Onde:** Aula 03 · "Imiscibilidade líquido-líquido"; recap
**Problema:** O primeiro dado experimental é de Koster van Groos e Wyllie (1963), no sistema NaAlSi₃O₈-Na₂CO₃-CO₂. Os trabalhos de Freestone e Hamilton (1980) e de Kjarsgaard e Hamilton (1988, 1989) vieram depois. O Módulo 30 ressalta que parte dos líquidos carbonáticos experimentais é mais rica em Na e mais pobre em Mg que os carbonatitos naturais comuns, e a aula dizia só "rico em CaO".
**Correção proposta:** "desde os anos 1960 (Koster van Groos e Wyllie, 1963), com contribuições importantes de Freestone e Hamilton (1980) e Kjarsgaard e Hamilton (1988, 1989)". Acrescentar a ressalva da composição do líquido, alinhada ao Módulo 30.
**Fonte:** Koster van Groos, A. F. e Wyllie, P. J. (1963), *Nature* 199, 801-802. Freestone e Hamilton (1980), *CMP* 73, 105-117. · **Nível:** revisada por pares
**Confiança:** confirmado

### 🟠 12. Imiscibilidade como rota que "melhor explica" a associação; a cristalização fracionada omitida; "esmagadora maioria"

**claim_id:** `ALK-M31-A07-ASSOCIACAO-GENETICA-001` (também cobre o segundo parágrafo da imiscibilidade na Aula 03)
**Tipo:** certeza indevida e inconsistência com o Módulo 30
**Onde:** Aula 03 · "Imiscibilidade", segundo parágrafo. Aula 07 · "Por que rochas alcalinas silicáticas e carbonatitos aparecem juntos"; recap
**Está escrito:** (a03) "é o processo que melhor explica por que, em muitos complexos, o corpo carbonatítico aparece intrusivo dentro de ou adjacente a rochas silicáticas cogenéticas". (a07) "carbonatitos raramente ocorrem sozinhos, e [...] a esmagadora maioria deles está espacialmente associada"; "são **produtos gêmeos** de um mesmo evento de imiscibilidade"; "nem todo carbonatito segue a rota de imiscibilidade [...] alguns são interpretados como produto de fusão parcial direta"; recap "o mesmo processo gerador (imiscibilidade de líquidos, Aula 03)".
**Problema:** O Módulo 30 (Aula 04, auditada) dá **três rotas não exclusivas** e diz que a **cristalização fracionada** de um parental silicático carbonatado "é a rota favorecida por muitas associações de campo". A rota dominante é debatida caso a caso. O M31 elegia a imiscibilidade e, na ressalva da Aula 07, esquecia a cristalização fracionada, justamente a outra rota que também produz a "linhagem" silicática conjugada. Quanto ao número, a base de Woolley e Kjarsgaard (2008) dá **~76 %** de carbonatitos em complexos com rochas silicáticas alcalinas e 24 % fora deles. É a maioria, mas não "raramente sozinhos".
**Correção proposta:** Apresentar imiscibilidade **e** cristalização fracionada como as duas vias que ligam carbonatito e rocha silicática, com a rota dominante debatida. "Produtos gêmeos" fica restrito ao modelo de imiscibilidade. Dar "cerca de três quartos" com a fonte.
**Fonte:** Módulo 30, Aula 04 (Kjarsgaard e Hamilton, 1988; Brooker e Kjarsgaard, 2011; Yaxley et al., 2022). Woolley e Kjarsgaard (2008), *Can. Mineral.* 46, 741-752 ("Paragenetic types of carbonatite..."), citado por Simandl e Paradis (2018). · **Nível:** revisada por pares
**Confiança:** confirmado

### 🟠 13. Hiato de Daly: mecanismos descritos de forma imprecisa

**claim_id:** `ALK-M31-A03-HIATO-DALY-002`
**Tipo:** impreciso (mecanismo) com certeza indevida
**Onde:** Aula 03 · "O hiato de Daly"
**Está escrito:** "Cinética de cristalização: entre cerca de 55-60 % SiO₂ [...] a viscosidade e a taxa de nucleação de cristais mudam de regime, favorecendo cristalização mais rápida e completa"; "Imiscibilidade de líquidos [...] outro mais básico ou carbonático".
**Problema:** As explicações correntes são outras. (1) A extração de líquido de um *mush* é eficiente só numa janela de cristalinidade de ~50-70 %, o que produz saltos de composição (Dufek e Bachmann, 2010). (2) A composição do líquido muda rápido num intervalo pequeno de temperatura quando saturam fases como óxidos de Fe-Ti e apatita. (3) Imiscibilidade **silicato-silicato**, líquido rico em Fe × rico em Si, demonstrada em série **toleítica** (Charlier et al., 2011). (4) Fusão de crosta. A imiscibilidade silicato-carbonato não é explicação usual do hiato. A origem continua debatida.
**Correção proposta:** Reescrever as explicações com essas quatro vias e marcar o debate.
**Fonte:** Daly (1925), *Proc. Am. Acad. Arts Sci.* 60, 3-80 (Ascensão). Dufek e Bachmann (2010), *Geology* 38, 687-690. Charlier et al. (2011), *Geology* 39, 907-910. · **Nível:** revisada por pares
**Confiança:** confirmado

### 🟠 14. Exemplo da Aula 03: "rochas de composição traquítica intermediária (52-55 % SiO₂)" e "índice de diferenciação (álcalis/sílica)"

**claim_id:** `ALK-M31-A03-EXEMPLO-005`
**Tipo:** impreciso
**Problema:** Numa série basanito → fonolito, o termo que falta entre o fonotefrito (49 %) e o fonolito (57 %) é o **tefrifonolito**. O traquito é termo evoluído da série saturada, e não intermediário a 52-55 %. O índice de diferenciação (Thornton e Tuttle, 1960) é a soma normativa qz + or + ab + ne + lc + kp, e não "álcalis/sílica". O passo 2 também atribuía o salto à extração de um componente carbonatítico como explicação principal, em desacordo com 🟠 13.
**Correção proposta:** "tefrifonolítica (~52-55 % SiO₂)"; "junto com os álcalis (e com o índice de diferenciação)"; passo 2 reescrito com a janela de extração como primeira hipótese e a separação de líquidos como alternativa a testar.
**Fonte:** Le Bas et al. (1986); Thornton e Tuttle (1960), *Am. J. Sci.* 258, 664-684. · **Nível:** normativa
**Confiança:** confirmado

### 🟠 15. "Rochas alcalinas continentais tendem a EM1; ilhas oceânicas, a HIMU ou EM2"

**claim_id:** `ALK-M31-A04-ZINDLER-HART-003`
**Tipo:** confusão de escopo
**Onde:** Aula 04 · "Isótopos radiogênicos"; recap
**Problema:** Generaliza demais. Várias províncias alcalinas continentais têm assinatura tipo **HIMU** ou FOZO: o Cenozoico da Europa (reservatório astenosférico europeu) e parte do Leste Africano. Várias ilhas oceânicas são **EM1** (Pitcairn, Tristão da Cunha, a própria cadeia de Walvis de Zindler e Hart). O que vale é que províncias continentais antigas com litosfera metassomatizada, como as cretáceas brasileiras (Gibson et al., 1995), mostram com frequência assinatura tipo EM1 ou mistura. A origem do HIMU como "desgaseificação" também não é a interpretação corrente. A leitura usual é crosta oceânica reciclada que perdeu Pb (e ficou com U relativo) na alteração e na desidratação da subducção.
**Correção proposta:** Restringir a afirmação, dar os contraexemplos e corrigir a origem do HIMU.
**Fonte:** Zindler e Hart (1986), *Annu. Rev. Earth Planet. Sci.* 14, 493-571. Hoernle, Zhang e Graham (1995), *Nature* 374, 34-39. Stracke (2012), *Chem. Geol.* 330-331, 274-299. Gibson et al. (1995). · **Nível:** revisada por pares
**Confiança:** confirmado

### 🟠 16. "Rochas alcalinas são, por definição operacional, enriquecidas em elementos incompatíveis"

**claim_id:** `ALK-M31-A04-DEFINICAO-OPERACIONAL-006` (criado pela auditoria)
**Tipo:** inconsistência interna
**Problema:** A Aula 01 define rocha alcalina pela mineralogia e pela química normativa (Le Maitre, 2002), e não pelo teor de incompatíveis. O enriquecimento é **típico**, não definidor.
**Correção proposta:** "Rochas alcalinas são tipicamente enriquecidas...".
**Fonte:** Le Maitre (2002); Aula 01. · **Nível:** normativa
**Confiança:** confirmado

### 🟠 17. Nomenclatura de anfibólios e da astrofilita: hornblenda "cálcico-alcalina", kaersutita "sódica", Zr essencial na astrofilita

**claim_id:** `ALK-M31-MOD-ANFIBOLIOS-002` (criado pela auditoria; também cobre parte de `ALK-M31-A05-MINERAIS-EXOTICOS-002` e de `ALK-M31-A06-LAMPROFIROS-002`)
**Tipo:** impreciso (nomenclatura IMA)
**Onde:** Aula 05 (duas vezes: "anfibólio cálcico-alcalino") e item Astrofilita; Aula 06 (lamprófiros calcialcalinos: "anfibólio cálcico-alcalino (hornblenda)"; lamprófiros alcalinos: "anfibólio sódico a sódico-cálcico (kaersutita, barkevikita)"); recap da Aula 06 ("anfibólio sódico")
**Problema:** Pela nomenclatura IMA dos anfibólios, a hornblenda é anfibólio **cálcico**. "Cálcico-alcalino" é nome de série magmática, não de grupo mineral. A kaersutita é anfibólio **cálcico** rico em Ti, e não sódico. A astrofilita é K₂NaFe₇Ti₂Si₈O₂₈(OH)₄F: Zr não é essencial, e entra no análogo zircofilita.
**Correção proposta:** "anfibólio cálcico (hornblenda)"; "anfibólio cálcico rico em Ti (kaersutita)"; astrofilita "silicato de K-Na-Fe-Ti (o Zr entra no análogo zircofilita)".
**Fonte:** Hawthorne et al. (2012), *Am. Mineral.* 97, 2031-2048 (nomenclatura IMA). Mindat, "Kaersutite" (subgrupo cálcico) e "Astrophyllite". · **Nível:** normativa (IMA)
**Confiança:** confirmado

### 🟠 18. "Rocher e Streckeisen (1978, 1980)" e as "duas grandes séries" de lamprófiros

**claim_id:** `ALK-M31-A06-LAMPROFIROS-002`
**Tipo:** impreciso (atribuição e omissão)
**Onde:** Aula 06 · "Lamprófiros"
**Problema:** "Rocher" não existe na bibliografia: a sistematização é de **Rock** (1977, 1987, 1991), que as Fontes da própria aula citam. A recomendação da IUGS é de **Streckeisen (1979)**. Rock reconhece, além das séries calcialcalina e alcalina, os **lamprófiros ultramáficos** (alnöito, aillikito, damtjernito), que o Módulo 30 já apresentou.
**Correção proposta:** "Streckeisen (1979, recomendação da IUGS) e Rock (1977, 1987, 1991)"; acrescentar os UML com remissão ao Módulo 30.
**Fonte:** Streckeisen (1979), *Geology* 7, 331-335. Rock (1977), *Earth-Sci. Rev.* 13, 123-169. Rock (1987), GSSP 30, 191-226. · **Nível:** normativa e revisada por pares
**Confiança:** confirmado

### 🟠 19. Ultrapotássicas: faltava o critério de MgO, e o Grupo III era "intermediário"

**claim_id:** `ALK-M31-A06-ULTRAPOTASSICAS-003`
**Tipo:** omissão que gera erro
**Onde:** Aula 06 · "Rochas ultrapotássicas"; exemplo; recap
**Problema:** Foley et al. (1987) usam **três** filtros: K₂O > 3 % em peso, **MgO > 3 % em peso** e K₂O/Na₂O > 2. O MgO é o que exclui as rochas félsicas potássicas, como sienitos ricos em K. O Grupo III é o do **tipo Província Romana** (plagioleucitítico): alto CaO e Al₂O₃, em zonas orogênicas. Não é "intermediário entre os dois anteriores". A frase de que a baixa razão Al₂O₃/(K₂O+Na₂O) "impede a cristalização de feldspato alcalino" não vale para todo o grupo: rochas do tipo romano têm plagioclásio e sanidina.
**Correção proposta:** Incluir o MgO nos critérios e no exemplo, redefinir o Grupo III e restringir a frase sobre o feldspato aos lamproítos e kamafugitos.
**Fonte:** Foley, Venturelli, Green e Toscani (1987), *Earth-Sci. Rev.* 24, 81-134 (resumo e citações secundárias convergentes). · **Nível:** revisada por pares
**Confiança:** confirmado (os três filtros e os grupos); ver 🔵 26 para a base da razão

### 🟠 20. Ijolito como "equivalente plutônico [...] de um basanito ou nefelinito"

**claim_id:** `ALK-M31-A06-CUMULATOS-SEQUENCIA-001`
**Tipo:** impreciso
**Problema:** O ijolito (nefelina + 30-70 % de máficos, campo dos foidolitos) é o equivalente plutônico do **nefelinito**. O basanito tem plagioclásio e olivina, e seu equivalente plutônico é o teralito (foide-gabro). "Saturado em nefelina" não é expressão petrográfica.
**Correção proposta:** "o equivalente plutônico de um nefelinito".
**Fonte:** Le Maitre (2002), glossário (ijolite, theralite). · **Nível:** normativa
**Confiança:** confirmado

### 🟠 21. Sequência do carbonatito "calcio → ferrocarbonatito", sem o estágio dolomítico, dita "já vista no Módulo 30"

**claim_id:** `ALK-M31-A07-ZONEAMENTO-002`
**Tipo:** inconsistência com o Módulo 30
**Onde:** Aula 07 · "O arranjo espacial típico"
**Problema:** O Módulo 30 (Aula 05, auditado) ensina calcita → **dolomita** → ferrocarbonato (sövito/alvikito → beforsito → ferrocarbonatito). Dizer "evoluindo por vezes para ferrocarbonatito [...] sequência já vista no Módulo 30" apaga o estágio intermediário.
**Correção proposta:** "evoluindo, nos estágios tardios, para dolomita-carbonatito e ferrocarbonatito, na sequência calcita → dolomita → ferrocarbonato do Módulo 30".
**Fonte:** Módulo 30, Aula 05; Chakhmouradian e Zaitsev (2012), *Elements* 8, 347-353. · **Nível:** revisada por pares
**Confiança:** confirmado

### 🟠 22. Mineralização por zona: ETR postas no envelope sienítico, pirocloro "no carbonatito propriamente dito"

**claim_id:** `ALK-M31-A07-MINERALIZACAO-ZONAS-006` (criado pela auditoria)
**Tipo:** inconsistência com o Módulo 30 (confusão de escopo)
**Onde:** Aula 07 · segundo parágrafo do zoneamento; "O que fixar" do exemplo; recap
**Problema:** Nos complexos com carbonatito, as ETR concentram-se sobretudo nos **carbonatitos tardios** (ferrocarbonatitos com bastnäsita, parisita e monazita) e no **regolito** laterítico, como ensinam as Aulas 05 e 06 do Módulo 30 (Catalão I, Mountain Pass, Mount Weld). O pirocloro também ocorre em foscoritos. Silicatos de Zr-Nb-ETR em sienito dependem de a porção sienítica ser **agpaítica**, o que não é regra num complexo com carbonatito. Como estava, a aula ensinava "ETR no envelope sienítico" como modelo geral.
**Correção proposta:** Reescrever a zonação mineral: fosfato e Nb no núcleo carbonatítico e nos foscoritos; ETR nos carbonatitos tardios e no regolito; Zr-Nb-ETR no sienito **quando** ele for agpaítico. Ajustar o recap e o "O que fixar".
**Fonte:** Módulo 30, Aulas 05 e 06; Simandl e Paradis (2018); Chakhmouradian e Zaitsev (2012). · **Nível:** revisada por pares
**Confiança:** confirmado

### 🟠 23. Poços de Caldas "ao longo do Arco de Ponta Grossa"; "Alinhamento Cabo Frio" e sua idade; "área geologicamente modesta"

**claim_id:** `ALK-M31-A07-PROVINCIAS-BRASILEIRAS-004`
**Tipo:** impreciso
**Onde:** Aula 07 · "Magmatismo alcalino na Plataforma Sul-Americana", terceiro item e parágrafo final
**Problema:** A província do Arco de Ponta Grossa (PR-SP, com Jacupiranga, Juquiá e Tunas) é do **Cretáceo Inferior**. Poços de Caldas é o extremo oeste de outra estrutura, o **Alinhamento Magmático Poços de Caldas–Cabo Frio**: 26 centros alcalinos, com idades de ~84 a ~49 Ma que diminuem de oeste para leste, do Cretáceo Superior ao Eoceno (Riccomini et al., 2005). O texto punha Poços como exemplo do Arco de Ponta Grossa e separava do "Alinhamento Cabo Frio" o complexo que é o extremo do alinhamento. A Plataforma Sul-Americana também não é "área geologicamente modesta": cobre a maior parte do continente.
**Correção proposta:** Separar as duas províncias com as idades certas e trocar "numa área geologicamente modesta" por "numa mesma plataforma".
**Fonte:** Riccomini, Velázquez e Gomes (2005), em Comin-Chiaramonti e Gomes (eds.), *Mesozoic to Cenozoic Alkaline Magmatism in the Brazilian Platform*, EDUSP, 31-55. Revisão petrocronológica no *Anuário do Instituto de Geociências* (UFRJ), "Poços de Caldas – Cabo Frio Alignment: a Petrochronological Review of an Unconventional Plume Model" (84-49 Ma; 26 centros). Almeida (1983). · **Nível:** revisada por pares
**Confiança:** confirmado (as idades como faixa)

### 🟡 24. "Barkevikita"

**claim_id:** `ALK-M31-A06-BARKEVIKITA-006` (criado pela auditoria)
**Tipo:** desatualizado
**Onde:** Aula 06 · lamprófiros alcalinos
**Problema:** O nome foi desacreditado pela IMA em 1978. Os anfibólios antes chamados "barkevikita" são ferro-edenita (espécime-tipo), hastingsita ou magnesio-hastingsita, conforme a localidade. O aluno vai encontrar o nome em textos antigos sobre camptonitos.
**Correção proposta:** "(nos textos antigos, 'barkevikita', nome desacreditado pela IMA; corresponde a anfibólios cálcicos ricos em Fe, como a hastingsita e a ferro-edenita)".
**Fonte:** Mindat, "Barkevikite" (discredited 1978). · **Nível:** base de referência (IMA)
**Confiança:** confirmado

### 🟡 25. Cretáceo "entre 145 e 66 milhões de anos atrás"

**claim_id:** `ALK-M31-A07-PLATAFORMA-SA-CRETACEO-003`
**Tipo:** desatualizado
**Onde:** Aula 07 · "Magmatismo alcalino na Plataforma Sul-Americana"; metadado da alegação
**Problema:** Na carta vigente da ICS, a base do Berriasiano (e do Cretáceo) está em **143,1 ± 0,6 Ma**. O valor de 145,0 Ma é da carta anterior. Esta é a convenção que o curso já adotou na auditoria do Módulo 26 (consulta de 2026-09-21).
**Correção proposta:** "grosso modo, entre ~143 e 66 milhões de anos atrás (cartas anteriores da ICS davam ~145 Ma para a base)".
**Fonte:** ICS, *International Chronostratigraphic Chart* (versão vigente consultada na auditoria do Módulo 26, 2026-09-21). · **Nível:** normativa
**Confiança:** confirmado

### 🔵 26. "Razão molar K₂O/Na₂O > 2" como critério de Foley et al. (1987)

**claim_id:** `ALK-M31-A06-EXEMPLO-CALCULO-005`
**Tipo:** evidência insuficiente
**Onde:** Aula 06 · "Rochas ultrapotássicas"; exemplo; recap
**Problema:** As fontes secundárias consultadas dão "K₂O/Na₂O > 2" sem dizer se a razão é em % peso ou molar. O texto integral de Foley et al. (1987) não pôde ser lido (ScienceDirect, HTTP 403). O exemplo tem a aritmética certa (2,63 e 0,89 em base molar), e a conclusão é a mesma em % peso (4,0 e 1,35).
**Correção proposta:** Não afirmar a base como parte da definição. Dar o critério como "K₂O/Na₂O > 2", pedir que se confira a base em cada trabalho e mostrar que, no exemplo, as duas bases levam à mesma conclusão. Nenhum valor foi inventado.
**Fonte:** Foley et al. (1987), resumo e citações secundárias. · **Nível:** revisada por pares (parcial)
**Confiança:** não verificado (a base da razão)
**Desfecho:** tratado. A afirmação não confirmada foi retirada. Não aguarda decisão: o aluno não perde conteúdo e a conclusão do exemplo não muda.

### ⚪ 27. Pluma de Trindade apresentada como fato nos recaps

**claim_id:** `ALK-M31-A06-APIP-KAMAFUGITOS-004` (também cobre o texto sobre a pluma na Aula 07)
**Tipo:** controvérsia
**Onde:** Aula 06 · "Kamafugitos e a APIP"; recap ("sob a pluma de Trindade"). Aula 07 · Plataforma Sul-Americana
**Problema:** O modelo de Gibson et al. (1995) é o mais citado, mas é contestado. Reconstruções paleomagnéticas indicam que o *hotspot* de Trindade não estava sob a APIP a ~85 Ma (Ernesto, 2005), e outros autores atribuem o magmatismo a anomalias térmicas de longa duração no manto ou a fontes litosféricas, sem pluma. O Módulo 30 diz "atribuída por Gibson et al. (1995)", o que é compatível com a ressalva.
**Correção proposta:** Manter a atribuição a Gibson et al. (1995) e acrescentar, em uma frase, que o modelo é debatido (Ernesto, 2005). Recap sem "sob a pluma" como fato.
**Fonte:** Ernesto (2005), 9º Congresso Internacional da SBGf, "Paleomagnetism of the post-Paleozoic alkaline magmatism in the Brazilian Platform: questioning the mantle plume model". Gibson et al. (1995), *J. Petrol.* 36, 189-229. · **Nível:** revisada por pares / anais
**Confiança:** em disputa

---

## Verificado e correto

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `ALK-M31-A01-QAPF-002` | QAPF para M < 90 %; Q e F mutuamente exclusivos (nefelina + 2 SiO₂ = albita) | Le Maitre 2002 | confirmado |
| `ALK-M31-A01-TRES-SENTIDOS-001` (parte) | Prefixo "alcalino" de Le Maitre 2002 (foides ou anfibólio/piroxênio alcalino modais; foides ou acmita normativos); linha de Irvine e Baragar (1971) | Le Maitre 2002, glossário | confirmado |
| `ALK-M31-A01-EXEMPLO-005` | Moda A 64,7 % e F 35,3 % no campo do fonolito; (54 %; 13,5 %) logo acima da divisa tefrifonolito/fonolito do TAS (13,3 % a 54 % de SiO₂) | aritmética refeita; Le Bas et al. 1986 | confirmado |
| `ALK-M31-A02-CO2-SOLIDUS-002` | CO₂ abaixa o solidus do peridotito | Wyllie e Huang 1975 (conferido no M30) | confirmado |
| `ALK-M31-A02-METASSOMATISMO-003` | Modal × críptico | coerente com o M30, Aula 02 (auditado) | confirmado |
| `ALK-M31-A02-PILET-VEIOS-004` | Fusão de veios ricos em anfibólio a 1,5 GPa, reação com lherzolito; alternativa à crosta reciclada | Pilet, Baker e Stolper 2008, *Science* 320, 916-919 (resumo) | confirmado |
| `ALK-M31-A02-AMBIENTES-005` | Riftes, ilhas oceânicas, margens cratônicas e pós-orogênico | literatura consolidada | provável |
| `ALK-M31-A03-PLANO-CRITICO-001` | Plano crítico de subsaturação em sílica (Fo-Di-Ab), divisor térmico em baixa pressão | Yoder e Tilley 1962, *J. Petrol.* 3, 342-532 | confirmado |
| `ALK-M31-A03-VOLATEIS-004` | Solubilidade do CO₂ maior em líquidos mais insaturados | literatura experimental | provável |
| `ALK-M31-A04-NB-TA-001` | Anomalia negativa de Nb-Ta em magmas de subducção, ausente nos intraplaca | literatura consolidada | confirmado |
| `ALK-M31-A04-ETR-GRANADA-002` | La/Yb alta por granada residual | literatura consolidada | confirmado |
| `ALK-M31-A04-EQUACOES-004` | C_L/C₀ = 1/[D + F(1−D)] (Shaw 1970, *GCA* 34, 237-243); C_L/C₀ = F^(D−1); AFC de DePaolo 1981 (*EPSL* 53, 189-202) | referências conferidas | confirmado (a remissão ao M30: ver 🟠 8) |
| `ALK-M31-A04-EXEMPLO-CALCULO-005` | 1/0,0298 = 33,6; 0,3^(−0,95) = 3,14 (o mesmo fator do M30, Aula 05); 33,6 × 3,14 ≈ 105 | aritmética refeita | confirmado |
| `ALK-M31-A05-MINERAIS-EXOTICOS-002` (parte) | Eudialita, aegirina (NaFe³⁺Si₂O₆), arfvedsonita/riebeckita, lovozerita (silicato de Zr em anel), loparita; Ilímaussaq, Lovozero-Khibiny (Khibiny: apatita-nefelina) | Sørensen 1997; Marks e Markl 2017; Mindat | confirmado |
| `ALK-M31-A05-POCOS-DE-CALDAS-003` | U, Zr, ETR; primeira mineração de urânio do país; agpaicidade variável por corpo | Ulbrich e Gomes 1981 | provável |
| `ALK-M31-A05-METALURGIA-EUDIALITA-004` | Eudialita mais difícil de processar que bastnäsita/monazita | literatura de processamento (gel de sílica na lixiviação ácida) | provável |
| `ALK-M31-A05-EXEMPLO-CALCULO-005` (aritmética) | A: 0,1902/0,1765 = 1,08; B: 0,2412/0,1422 = 1,70 | aritmética refeita | confirmado (a interpretação: ver 🔴 1) |
| `ALK-M31-A06-EXEMPLO-CALCULO-005` (aritmética) | X: 0,0510/0,0194 = 2,63; Y: 0,0372/0,0419 = 0,89 | aritmética refeita | confirmado |
| `ALK-M31-A06-APIP-KAMAFUGITOS-004` (parte) | Grande volume de kamafugitos na APIP, junto de kimberlitos, lamproítos e carbonatitos | Gibson et al. 1995; M30, Aula 06 | confirmado |
| `ALK-M31-A07-ZONEAMENTO-002` (parte) | Complexo zonado com núcleo carbonatítico, ijolito/piroxenito, foscorito, sienito e fenito; padrão não universal; fenitização com dessilicificação | M30, Aula 03; Simandl e Paradis 2018 | confirmado |
| `ALK-M31-A07-PROVINCIAS-BRASILEIRAS-004` (parte) | APIP com os seis complexos; Jacupiranga do Cretáceo Inferior, localidade-tipo do jacupiranguito, fosfato em Cajati | M30, Aula 06 | confirmado |

**Bibliografia.** Conferida na forma autor-ano-periódico-volume-páginas para 21 referências das Fontes das aulas: Le Maitre 2002; Irvine e Baragar 1971; Brøgger 1921; Green e Ringwood 1967; Wyllie 1979; Pilet et al. 2008; Yoder e Tilley 1962; Daly 1925; Freestone e Hamilton 1980; Kjarsgaard e Hamilton 1988/1989; Zindler e Hart 1986; Shaw 1970; DePaolo 1981; Sørensen 1997; Marks e Markl 2017; Ulbrich e Gomes 1981; Rock 1987; Foley et al. 1987; Gibson et al. 1995; Woolley e Kjarsgaard 2008; Le Bas 1987; Simandl e Paradis 2018. Nenhum volume ou paginação errado. O erro bibliográfico estava **no texto** ("Rocher e Streckeisen", 🟠 18; Shaw "já usada no módulo 30", 🟠 8).

---

## Correções aplicadas

**Aplicadas em:** 2026-09-24

| # | claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|---|
| 1 | `ALK-M31-A05-INDICE-AGPAITICO-001` | 🔴 | Corrigido | aula-05 |
| 2 | `ALK-M31-A01-FOID-FOIDOLITO-006` | 🔴 | Corrigido | aula-01 |
| 3 | `ALK-M31-A02-EXEMPLO-006` | 🔴 | Corrigido | aula-02 |
| 4 | `ALK-M31-A05-PRODUCAO-ETR-006` | 🔴 | Corrigido | aula-05 |
| 5 | `ALK-M31-A01-TRES-SENTIDOS-001` | 🟠 | Corrigido | aula-01 |
| 6 | `ALK-M31-A01-CLAS-003` | 🟠 | Corrigido | aula-01 |
| 7 | `ALK-M31-A01-TOPONIMOS-004` | 🟠 | Corrigido | aula-01 |
| 8 | `ALK-M31-MOD-REMISSOES-001` | 🟠 | Corrigido | aula-01, aula-02, aula-03, aula-04, aula-05 |
| 9 | `ALK-M31-A02-GRAU-FUSAO-001` | 🟠 | Corrigido | aula-02 |
| 10 | `ALK-M31-A03-SERIE-SUBALCALINA-006` | 🟠 | Corrigido | aula-03 |
| 11 | `ALK-M31-A03-IMISCIBILIDADE-003` | 🟠 | Corrigido | aula-03 |
| 12 | `ALK-M31-A07-ASSOCIACAO-GENETICA-001` | 🟠 | Corrigido | aula-03, aula-07 |
| 13 | `ALK-M31-A03-HIATO-DALY-002` | 🟠 | Corrigido | aula-03 |
| 14 | `ALK-M31-A03-EXEMPLO-005` | 🟠 | Corrigido | aula-03 |
| 15 | `ALK-M31-A04-ZINDLER-HART-003` | 🟠 | Corrigido | aula-04 |
| 16 | `ALK-M31-A04-DEFINICAO-OPERACIONAL-006` | 🟠 | Corrigido | aula-04 |
| 17 | `ALK-M31-MOD-ANFIBOLIOS-002` | 🟠 | Corrigido | aula-05, aula-06 |
| 18 | `ALK-M31-A06-LAMPROFIROS-002` | 🟠 | Corrigido | aula-06 |
| 19 | `ALK-M31-A06-ULTRAPOTASSICAS-003` | 🟠 | Corrigido | aula-06 |
| 20 | `ALK-M31-A06-CUMULATOS-SEQUENCIA-001` | 🟠 | Corrigido | aula-06 |
| 21 | `ALK-M31-A07-ZONEAMENTO-002` | 🟠 | Corrigido | aula-07 |
| 22 | `ALK-M31-A07-MINERALIZACAO-ZONAS-006` | 🟠 | Corrigido | aula-07 |
| 23 | `ALK-M31-A07-PROVINCIAS-BRASILEIRAS-004` | 🟠 | Corrigido | aula-07 |
| 24 | `ALK-M31-A06-BARKEVIKITA-006` | 🟡 | Corrigido (nome antigo mantido como referência) | aula-06 |
| 25 | `ALK-M31-A07-PLATAFORMA-SA-CRETACEO-003` | 🟡 | Corrigido (valor antigo mantido como referência) | aula-07 |
| 26 | `ALK-M31-A06-EXEMPLO-CALCULO-005` | 🔵 | Corrigido com ressalva (afirmação não confirmada retirada) | aula-06 |
| 27 | `ALK-M31-A06-APIP-KAMAFUGITOS-004` | ⚪ | Corrigido com ressalva (reescrito como debate) | aula-06, aula-07 |

Também foram alterados: o bloco `alegacoes_auditaveis` das sete aulas (claims criados pela auditoria e fontes atualizadas); um bloco `auditoria` no fim dos metadados de cada aula; e o hub do módulo (registro).

**Propagação.** O módulo **não tem questionário, baralho nem glossário**: a auditoria correu antes deles, e nenhum card no Anki precisa de correção. Busquei no curso inteiro "foiolito", "Ilha de Fen", "Rocher", "barkevikita", "índice agpaítico" e "agpaít"/"miaskít". Fora do M31, o único outro uso é o Módulo 40, Aula 11 (feldspatoides), que cita "miasquítico ou agpaítico" sem definir por índice, e é compatível. Nenhum outro módulo repete os fatos corrigidos.

**Pendências:** nenhuma.

---

## Restrições obrigatórias para quem gerar a avaliação (questionário e flashcards)

1. **Agpaítico × miaskítico é mineralógico** (Sørensen, 1997; Le Maitre, 2002): agpaítica = HFSE em silicatos complexos (eudialita, rinkita); miaskítica = zircão e titanita. **IA = (Na+K)/Al > 1 define peralcalina**, condição necessária, **não suficiente**. Nunca cobrar "IA ≥ 1 ⇒ agpaítica". Ussing (1912) = origem do termo, critério químico IA ≥ 1,2.
2. **Foid = contração de "feldspatoide"** (Johannsen); **foidolito** = campo 15 do QAPF, vértice F. Nunca "foiolito" nem etimologia grega.
3. Tipo de basalto intraplaca: litosfera **espessa** limita a fusão à fácies da granada e a baixo grau (efeito tampa). Não cobrar fusão em fácies de espinélio sob litosfera de 150 km.
4. **ETR:** produção mundial dominada por China/Bayan Obo, argilas iônicas, Mountain Pass e Mount Weld. **Araxá e Catalão = nióbio.** Nunca "Araxá e Catalão dominam as ETR".
5. **Shand:** usar os dois índices (A/NK e A/CNK). Peraluminosa exige Al > Ca+Na+K.
6. Classificação química vulcânica da IUGS = **TAS** (Le Bas et al., 1986). "Clãs" são agrupamento didático; basanito × tefrito por olivina normativa de 10 %; melilitito fora do TAS.
7. **Fen** = complexo em Telemark (não ilha); **jacupiranguito** = titanoaugita + magnetita + pouca nefelina (não cobrar apatita nem titanita como definidoras); **tinguaíto** = fonolito hipabissal (Serra do Tinguá); **lujavrito** = maciço de Lovozero.
8. A pressão controla a saturação em sílica ao lado do grau de fusão.
9. Imiscibilidade silicato-carbonato: experimental **desde 1963** (Koster van Groos e Wyllie). Associação carbonatito-rocha silicática: **imiscibilidade e cristalização fracionada**, rota dominante **em debate**. ~3/4 dos carbonatitos estão em complexos com rocha silicática; não cobrar "raramente ocorrem sozinhos".
10. Hiato de Daly: origem **debatida** (janela de extração de ~50-70 % de cristais; mudança rápida de composição; imiscibilidade silicato-silicato em série toleítica; fusão crustal). Não cobrar uma única causa.
11. Isótopos: não cobrar "continental = EM1, oceânico = HIMU/EM2" como regra.
12. Hornblenda e kaersutita = anfibólios **cálcicos**; arfvedsonita e riebeckita = **sódicos**; barkevikita = nome desacreditado.
13. Lamprófiros: Streckeisen (1979) e **Rock** (1977, 1987, 1991); séries calcialcalina, alcalina e ultramáfica (UML). Não cobrar "Rocher".
14. Ultrapotássicas: **K₂O > 3 %, MgO > 3 % e K₂O/Na₂O > 2** (Foley et al., 1987). Não cobrar se a razão é molar ou em peso: dar os dados de forma que as duas bases levem à mesma conclusão.
15. Ijolito = equivalente plutônico do **nefelinito**.
16. Carbonatito: sequência **calcita → dolomita → ferrocarbonato** (Módulo 30). ETR sobretudo em carbonatitos tardios e no regolito; Zr-Nb-ETR no sienito só quando agpaítico.
17. **Arco de Ponta Grossa** (Cretáceo Inferior; Jacupiranga) ≠ **Alinhamento Poços de Caldas–Cabo Frio** (~84-49 Ma). Não cobrar idades exatas de cada centro.
18. Cretáceo: base em **~143 Ma** (ICS vigente). Não cobrar 145 Ma como valor atual.
19. **Pluma de Trindade:** modelo de Gibson et al. (1995), **contestado** (Ernesto, 2005). Não cobrar como fato.
20. Números dos exemplos hipotéticos (IA 1,08 e 1,70; fator 105; razões 2,63 e 0,89) não são constantes a memorizar.
