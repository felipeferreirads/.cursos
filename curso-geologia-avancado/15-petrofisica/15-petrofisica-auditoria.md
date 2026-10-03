# Auditoria científica — Módulo 15: Introdução à petrofísica

**Data:** 2026-09-08
**Modo:** `audit-and-fix` · **Profundidade:** `full`
**Material auditado:** 4 aulas (`geologia-avancado-m15-a01` a `a04`), auditadas em conjunto
**Veredito:** ✅ **Aprovado após correção** — nenhum achado 🔴 ou 🟠 em aberto
**Material derivado:** nenhum. O módulo ainda não tem questionário nem baralho — a auditoria rodou antes deles, como manda a cadeia. Nada a reimportar no Anki.

---

## Resumo por severidade

| Severidade | Quantidade | Situação |
|---|---|---|
| 🔴 Erro | 2 | Corrigidos |
| 🟠 Impreciso | 7 | Corrigidos |
| 🟡 Desatualizado / nuance | 8 | Corrigidos |
| 🔵 Sem fonte | 0 | — |
| ⚪ Controverso | 2 | Um reescrito com a divergência explícita, um aceito como está |
| **Total** | **19** | **open_findings: []** |

**Passagem única** em modo `audit-and-fix` sobre as quatro aulas em conjunto. As **24 alegações auditáveis** declaradas pelas próprias aulas (5 na a01, 7 na a02, 7 na a03, 5 na a04) foram usadas como ponto de partida e reverificadas uma a uma; a auditoria levantou mais **17** fora da lista do autor, chegando a 41 alegações rastreadas. É nesse segundo grupo que estão **os dois achados vermelhos e seis dos sete laranjas** — de novo, o que o autor não marcou como arriscado foi exatamente onde o erro se escondeu. Dos 19 achados, apenas 4 correspondem a alegações que o próprio autor havia sinalizado.

Todos os exemplos numéricos foram recalculados do zero. **Um não fechava** (o de Vp/Vs da a02, achado 1); os demais conferem exatamente: porosidade total/efetiva de 24%/18% e a superestimativa relativa de 33% na a01; razões Th/U de 4,5 e 0,5 na a03; e a cadeia completa de Archie na a04 (F = 20,7, R₀ = 1,66 ohm·m, Sw = 37,1%, Sh = 63%, Rt/R₀ = 7,3). As geometrias de empacotamento de esferas foram confirmadas por cálculo direto: 1 − π/6 = 0,4764 (cúbico) e 1 − π/(3√2) = 0,2595 (romboédrico).

---

## Padrão dominante

**MINERAL OU MÉTODO CERTO NO LUGAR ERRADO — atribuição de agente físico.** Sete achados, incluindo um dos dois vermelhos, têm a mesma forma: a aula descreve corretamente **o fenômeno** e erra **quem o produz** ou **qual instrumento o mede**.

1. A **ilmenita** apresentada como contribuinte magnético relevante — sendo paramagnética em toda condição geológica (achado 2, 🔴).
2. A **porosimetria de mercúrio** apresentada como o método que identifica poros isolados — sendo, por definição, incapaz de entrar neles (achado 3, 🟠).
3. A **sísmica de refração** agrupada sob "contraste de impedância acústica" — quando obedece a contraste de velocidade apenas (achado 8, 🟠).
4. O **⁴⁰K** tratado como uma "série de decaimento" — sendo isótopo de decaimento direto (achado 6, 🟠).
5. A **hematita** admitida como fonte do magnetismo de formações ferríferas (achado 12, 🟡).
6. A **olivina** dada como causa geral da densidade do basalto (achado 10, 🟡).
7. A **susceptibilidade** posta no lugar da magnetização total, deixando de fora a remanente (achado 15, 🟡).

O padrão é caro exatamente neste módulo, porque a promessa declarada do Módulo 15 é dizer **de onde vem** cada contraste físico — trocar o agente é errar precisamente aquilo que o módulo existe para ensinar. E é o tipo de erro que vira flashcard invertido: um card "qual mineral controla a susceptibilidade magnética?" nasceria com "magnetita e ilmenita" no verso.

**PADRÃO SECUNDÁRIO: FAIXA APRESENTADA COMO MAIS ESTREITA DO QUE É.** Três achados (n de Archie 🟠, Vp de carbonato 🟡, K-U-Th de basalto 🟡) declaram uma faixa que vale só para um subcaso e a apresentam como geral. O caso do expoente n é o mais grave, porque a faixa falsa ("2 ± 0,5") erra na direção perigosa: superestima o hidrocarboneto.

**ONDE O MÓDULO ESTÁ LIMPO.** Toda a a01 até o exemplo trabalhado — definições de porosidade, empacotamento, controles texturais e diagenéticos, definição de permeabilidade por Darcy, gargantas de poro, Kozeny-Carman, e a distinção central porosidade × permeabilidade — não tem um único erro, e as faixas de permeabilidade por litologia são internamente coerentes até a conversão mD↔darcy (10⁻³ a 10⁻⁶ mD = microdarcy a nanodarcy, ✓). Toda a mecânica de Vp/Vs da a02 (fórmulas, papel de G, efeito do fluido, "bright spot", impedância acústica) está correta. Na a03, os três comportamentos magnéticos, a regra do "menos de 1% de magnetita domina a susceptibilidade", o comportamento geoquímico incompatível de U e Th, a abundância do ⁴⁰K (0,012%) e a lógica inteira do exemplo Th/U estão corretos. Na a04, a origem eletrolítica da condutividade, a condução eletrônica por sulfetos e grafita, a condutividade de superfície das argilas, a ressalva de Waxman-Smits e as duas partes da lei de Archie estão corretas.

---

## Achados

### 🔴 1. O exemplo trabalhado da a02 produzia uma razão Vp/Vs de arenito e a declarava típica de calcário

**claim_id:** `PETROFIS-M15-A02-EXEMPLOCALCARIO-008`
**Tipo:** inconsistência interna + erro factual
**Onde:** a02 · Exemplo trabalhado
**Estava escrito:** "um calcário saturado com água tem [...] módulo de cisalhamento (G) de 24 GPa [...] Razão Vp/Vs = 5.313 / 3.068 ≈ **1,73** [...] Esses valores caem dentro da faixa típica de calcário saturado de água apresentada na seção anterior"
**Problema:** a aritmética estava certa, a conclusão não. Com K = 40 e G = 24, Vp²/Vs² = K/G + 4/3 = 3 exatamente, ou seja Vp/Vs = √3 ≈ 1,73 — que corresponde a um coeficiente de Poisson de exatamente 0,25, o **sólido de Poisson**, valor característico de arenito limpo consolidado e de granito. A própria aula, três parágrafos antes, declara que rochas carbonáticas ficam em 1,8-1,9 e arenitos limpos em 1,6-1,8. O exemplo produzia um número de arenito e afirmava que ele caía na faixa dos carbonatos — contradizendo o texto imediatamente anterior. Christensen (1996) dá coeficiente de Poisson ≈ 0,31 para calcário (Vp/Vs ≈ 1,9) e ≈ 0,28 para dolomito (Vp/Vs ≈ 1,81).
**Correção aplicada:** G ajustado de 24 para 19 GPa. Vp = 5.062 m/s, Vs = 2.730 m/s, Vp/Vs = 1,85 — dentro das duas faixas que a aula declara (Vp 4-7 km/s, Vp/Vs 1,8-1,9), e correspondendo a ν = 0,295, coerente com a faixa de 0,25-0,35 de rocha saturada. Os três valores foram recalculados, o trecho qualitativo do gás foi ajustado (3,07 → 2,73 km/s), e **o caso-limite foi preservado como material didático** em vez de descartado: um parágrafo novo mostra que 1,73 é o valor de arenito/granito e que encontrá-lo num intervalo suposto carbonático é motivo para desconfiar da litologia atribuída.
**Fonte:** Christensen, N. I. (1996), *JGR* 101(B2), 3139-3156 · **Nível:** revisada por pares · **Confiança:** confirmado
**Também aparece em:** recap da a02 (ajustado)

---

### 🔴 2. A ilmenita apresentada como fonte relevante de magnetismo de rocha

**claim_id:** `PETROFIS-M15-A03-ILMENITA-008`
**Tipo:** erro factual + inconsistência interna + contradição transversal
**Onde:** a03 · "Magnetismo: três comportamentos e o mineral que domina tudo"; propagado para a tabela de integração da a04
**Estava escrito:** "A **ilmenita** (FeTiO₃) também contribui de forma relevante, sobretudo em rochas máficas." · tabela da a04: "Susceptibilidade magnética | Teor de magnetita (e ilmenita)"
**Problema:** a ilmenita pura é antiferromagnética apenas **abaixo de sua temperatura de Néel**, medida entre 56 e 57,7 K em amostras terrestres, sintéticas e lunares. Acima dela — isto é, em absolutamente qualquer condição geológica — a ilmenita é **paramagnética**, e Clark (1997), a fonte que a própria aula cita para esta passagem, a classifica explicitamente entre os óxidos fracamente magnéticos. Três agravantes: (a) a aula se **autocontradiz** dois parágrafos adiante, ao explicar corretamente que granitos de série ilmenita são fracamente magnéticos — o que só faz sentido se a ilmenita não magnetizar a rocha; (b) o erro **propagava** para a tabela de síntese da a04, que é o produto de fechamento do módulo; (c) **contradiz o Módulo 09** deste mesmo curso, cuja a05 já ensina ao aluno que a separação magnética de alta intensidade "separa minerais **paramagnéticos** fracos (hematita, **ilmenita**, wolframita, monazita, granada)". O aluno sairia do Módulo 15 com o oposto do que aprendeu no Módulo 09.
**Correção aplicada:** parágrafo reescrito nomeando os contribuintes ferrimagnéticos que de fato importam — **titanomagnetitas** (série magnetita–ulvöspinélio), **maghemita** e **pirrotita monoclínica** (Fe₇S₈), esta última também já ensinada como fortemente magnética no Módulo 09, o que restabelece a consistência nos dois sentidos. Acrescentado parágrafo dedicado explicando por que a ilmenita não está na lista (T_N ≈ 57 K), ressalvando que só as **hemoilmenitas** intermediárias são ferrimagnéticas em superfície, e usando a distinção magnetita-série/ilmenita-série como confirmação do argumento em vez de deixá-la como contradição. Mecanismo da hematita corrigido de omisso para **antiferromagnetismo inclinado** (*canted*). Tabela da a04 corrigida. Recap alinhado. Fontes completadas com Ishihara (1977) e com a literatura da transição de Néel.
**Fonte:** Clark, D. A. (1997), *AGSO Journal of Australian Geology & Geophysics* 17(2), 83-103; medidas de susceptibilidade de 4 a 300 K com transição de Néel única entre 56 e 57,7 K (*EPSL*) · **Nível:** revisada por pares · **Confiança:** confirmado
**Também aparece em:** a04 (tabela de integração), recap da a03 — todos corrigidos

---

### 🟠 3. A porosimetria de mercúrio creditada por identificar exatamente o que ela não alcança

**claim_id:** `PETROFIS-M15-A01-POROSIMETRIA-008`
**Tipo:** erro factual (atribuição de método)
**Onde:** a01 · Exemplo trabalhado, enunciado
**Estava escrito:** "o restante do espaço vazio corresponde a poros isolados, identificados por porosimetria de mercúrio"
**Problema:** a intrusão de mercúrio preenche progressivamente os poros **acessíveis a partir da superfície**, do maior para o menor, ao longo da rede conectada. Poros isolados são, por definição, os que ela **não** consegue alcançar — é a limitação declarada da técnica, e a razão de a moagem da amostra alterar o resultado (ao abrir poros antes ocluídos). A porosidade isolada é obtida **por diferença**, contra a porosidade total medida por picnometria de hélio.
**Correção aplicada:** enunciado reescrito explicitando que a porosidade isolada sai por diferença e nomeando corretamente o papel de cada técnica. Bullet novo no recap.
**Fonte:** Anton Paar, *Mercury Intrusion Porosimetry Basics*; comparações He-picnometria × MIP em *ACS Energy & Fuels* · **Nível:** base de referência + revisada por pares · **Confiança:** confirmado

---

### 🟠 4. "Porosidade efetiva" ensinada numa definição só, entrando num módulo que usa a outra

**claim_id:** `PETROFIS-M15-A01-POROSIDADEEFETIVA-007`
**Tipo:** omissão que gera erro
**Onde:** a01 · "Porosidade total versus porosidade efetiva"
**Problema:** o termo tem **duas definições vivas e incompatíveis**. Em análise de testemunho, porosidade efetiva = total menos a isolada (o espaço interconectado) — a definição que a aula ensina. Em interpretação de perfil de poço, significa total menos a **água ligada à argila**, que é imóvel mesmo estando conectada. As duas coincidem em rocha limpa e divergem muito em rocha argilosa, com a de testemunho dando o valor **maior**. A omissão não seria grave num módulo qualquer — mas a a04 deste mesmo módulo entra em petrofísica de perfil e aplica Archie a uma porosidade lida em perfil densidade-nêutron. O aluno sai equipado com uma definição e vai usá-la num contexto que adota a outra.
**Correção aplicada:** parágrafo de ressalva inserido na a01 nomeando as duas definições, dizendo qual mundo usa qual, e apontando para a a04. Nota correspondente acrescentada ao exemplo trabalhado da a04, explicando por que Archie funciona ali sem qualificar de qual porosidade se trata (arenito limpo) e o que muda em rocha argilosa. Recap da a01 ajustado.
**Fonte:** Schlumberger *Energy Glossary*, verbete "effective porosity"; Cuddy, *Should petrophysics calculate total or effective porosity?*, AFES 2021 · **Nível:** base de referência da indústria · **Confiança:** confirmado

---

### 🟠 5. O limite de 0,5 do coeficiente de Poisson justificado por uma categoria trocada

**claim_id:** `PETROFIS-M15-A02-POISSONLIMITE-009`
**Tipo:** erro factual (conceitual)
**Onde:** a02 · "Módulos elásticos: o que cada um mede fisicamente"
**Estava escrito:** "Fluidos têm coeficiente de Poisson próximo de 0,5 (o limite teórico para um material perfeitamente incompressível **em cisalhamento**)"
**Problema:** "incompressível em cisalhamento" mistura duas categorias. Incompressibilidade é uma propriedade **volumétrica**: ν = 0,5 corresponde a deformação sem mudança de volume, obtida no limite em que K >> G ou, equivalentemente, em que **G → 0**. Além disso, o coeficiente de Poisson não é rigorosamente definido para um fluido, que não sustenta tensão uniaxial — 0,5 é o valor-limite das relações elásticas, não uma medida de fluido. A frase, como escrita, ensina que o fluido resiste à compressão *por cisalhamento*, contradizendo a ideia central que a mesma seção acabara de estabelecer (G do fluido = 0).
**Correção aplicada:** passagem reescrita separando o limite (0,5), sua condição (volume constante / G → 0) e a ressalva de que Poisson não se define para fluido. Faixa de rocha saturada (0,25-0,35) acrescentada ao lado da de rocha seca (0,1-0,3), e o mecanismo amarrado à seção seguinte (a água eleva K sem tocar G). Bullet novo no recap.
**Fonte:** Mavko, Mukerji & Dvorkin (2020), *The Rock Physics Handbook*, cap. 1; Christensen (1996) · **Nível:** base de referência · **Confiança:** confirmado

---

### 🟠 6. O ⁴⁰K tratado como uma terceira série de decaimento

**claim_id:** `PETROFIS-M15-A03-ESPECTROMETRIA-004`
**Tipo:** erro factual (classificação) + omissão que gera erro
**Onde:** a03 · "Radioatividade natural: de onde ela vem"
**Estava escrito:** "Cada uma das três séries emite radiação gama em energias características"
**Problema:** são **duas séries e um isótopo isolado**, não três séries. O ⁴⁰K decai diretamente, sem cadeia: ~89% por β⁻ para ⁴⁰Ca e ~11% por captura eletrônica para ⁴⁰Ar, ramo minoritário que emite o gama de 1,46 MeV. A distinção não é preciosismo terminológico: ela é **a razão** de o K ser reportado em % direto enquanto U e Th são reportados como ppm *equivalente* (eU, eTh) — porque destes se mede um **produto-filho** (²¹⁴Bi em 1,76 MeV; ²⁰⁸Tl em 2,61 MeV), não o pai. A aula afirmava o pressuposto de equilíbrio secular sem nunca explicar por que ele é necessário, deixando o aluno com um termo decorado e sem mecanismo.
**Correção aplicada:** parágrafo novo estabelecendo "duas séries e um isótopo", com o esquema de decaimento do ⁴⁰K e as três energias-diagnóstico. A explicação do "equivalente" foi reescrita para derivar do fato de a medida ser do filho, e a quebra do equilíbrio secular foi ancorada na fuga do ²²²Rn gasoso, com a consequência prática nomeada (o canal de U é o menos confiável dos três). Recap reescrito em dois bullets.
**Fonte:** IAEA (2003), *Guidelines for Radioelement Mapping Using Gamma Ray Spectrometry Data*; Ellis & Singer (2007), cap. 12-13; abundância de 0,0117% e esquema 89%/11% confirmados · **Nível:** normativa · **Confiança:** confirmado

---

### 🟠 7. Os parâmetros a e m de Archie apresentados como escolhas independentes

**claim_id:** `PETROFIS-M15-A04-ARCHIEAM-006`
**Tipo:** omissão que gera erro
**Onde:** a04 · "A lei de Archie"
**Estava escrito:** "**a** é uma constante empírica (frequentemente tomada como 1, embora variações como a fórmula de Humble usem a ≈ 0,62 ou 0,65)"
**Problema:** a e m **não são botões independentes**: vêm em pares calibrados sobre um mesmo conjunto de amostras. A fórmula de Humble (Winsauer et al., 1952) é a = 0,62 **com m = 2,15**, e a variante para areias inconsolidadas é a = 0,65, também com m = 2,15. Listar os valores de a sem os m que os acompanham convida diretamente ao erro clássico de usar a = 0,62 com m = 2 — que não produz uma média prudente, produz um fator de formação errado, e errado de forma silenciosa, porque o resultado continua parecendo plausível.
**Correção aplicada:** parágrafo reescrito declarando o pareamento como armadilha explícita, com os três pares nomeados e o erro de combinação ilustrado. Recap ampliado.
**Fonte:** Winsauer et al. (1952), *AAPG Bulletin* 36(2); SEG Wiki, *Dictionary: Archie's formulas*; Ellis & Singer (2007), cap. 4 · **Nível:** revisada por pares + base de referência · **Confiança:** confirmado

---

### 🟠 8. O expoente de saturação n declarado numa faixa estreita que só vale para rocha molhável por água

**claim_id:** `PETROFIS-M15-A04-ARCHIEN-007`
**Tipo:** confusão de escopo
**Onde:** a04 · "A lei de Archie"
**Estava escrito:** "na prática varia numa faixa relativamente estreita ao redor desse valor (algo como 2 ± 0,5) para a maioria das rochas limpas"
**Problema:** falso fora da condição *water-wet*, que é a condição em que Archie mediu. n é uma função forte da **molhabilidade**: medidas clássicas dão n ≈ 1,6 (water-wet), ≈ 1,9 (neutra) e ≈ **8** (oil-wet), com valores acima de 10 em testemunhos uniformemente oil-wet a baixa saturação de salmoura. Como boa parte dos carbonatos é de molhabilidade mista ou oil-wet — e o módulo discute carbonatos —, a faixa declarada é estreita demais por um fator grande. Pior: o erro tem direção. Refazendo o exemplo da própria aula, F·Rw/Rt = 0,138 dá Sw = 37% com n = 2 e Sw = **78%** com n = 8. Assumir n = 2 numa rocha oil-wet **subestima** a saturação de água e **superestima** o hidrocarboneto.
**Correção aplicada:** passagem reescrita condicionando n ≈ 2 à molhabilidade por água, com os três valores medidos, o mecanismo físico (filme contínuo × gotas desconectadas) e a advertência sobre carbonatos. Bloco novo no exemplo trabalhado quantificando o custo com os números da própria aula (37% × 78%) e nomeando a direção do erro. Recap ampliado.
**Fonte:** Anderson, W. G. (1986), "Wettability Literature Survey — Part 3", *JPT* 38(12), 1371-1378, com os dados de Sweeney & Jennings · **Nível:** revisada por pares · **Confiança:** confirmado

---

### 🟠 9. Reflexão e refração sísmicas agrupadas sob o mesmo contraste físico

**claim_id:** `PETROFIS-M15-A04-REFRACAO-008`
**Tipo:** erro factual (atribuição de mecanismo)
**Onde:** a04 · tabela de integração
**Estava escrito:** "Sísmica de reflexão e refração (contraste de impedância acústica)"
**Problema:** os dois métodos não exploram o mesmo contraste. A **reflexão** é governada pela impedância acústica — R = (ρ₂V₂ − ρ₁V₁)/(ρ₂V₂ + ρ₁V₁), produto de densidade por velocidade. A **refração crítica** obedece à lei de Snell e depende **apenas do contraste de velocidade**, sendo insensível à densidade. Num módulo cuja tabela existe justamente para mapear propriedade física → método, agrupar os dois apaga a distinção que a tabela deveria fazer.
**Correção aplicada:** célula desmembrada, com o mecanismo de cada método declarado. Bullet novo no recap.
**Fonte:** Telford, Geldart & Sheriff (1990), cap. 4; US EPA, *Seismic Reflection* (coeficiente de reflexão) · **Nível:** base de referência · **Confiança:** confirmado

---

### 🟡 10. A olivina dada como causa geral da densidade do basalto

**claim_id:** `PETROFIS-M15-A02-BASALTOMINERAL-010`
**Tipo:** confusão de escopo (consistência mineralógica)
**Onde:** a02 · "Três densidades que não são a mesma coisa"
**Estava escrito:** "mais densos que o granito porque são mais ricos em minerais ferromagnesianos (piroxênio, olivina)"
**Problema:** olivina não é fase essencial de todo basalto — só das variedades olivínicas e dos picritos. O contraste de densidade com o granito se explica inteiramente sem ela, pela troca de quartzo (2,65) e feldspato alcalino (~2,56) por plagioclásio cálcico (~2,76), clinopiroxênio (3,2-3,4) e óxidos de Fe-Ti. Generalizar uma fase acessória contraria a petrologia ígnea já ensinada no curso base.
**Correção aplicada:** frase reescrita com as densidades minerais explícitas e a olivina realocada ao seu escopo real. Ganho colateral: a magnetita (5,2) aparece aqui pela primeira vez como fase densa, antecipando a a03.

---

### 🟡 11. Faixa de Vp de carbonatos incompatível com a porosidade que o próprio módulo lhes atribui

**claim_id:** `PETROFIS-M15-A02-VPLITOLOGIA-007`
**Tipo:** inconsistência interna
**Onde:** a02 · "Velocidades sísmicas típicas por litologia"
**Problema:** "calcários e dolomitos situam-se tipicamente entre 4 e 7 km/s" exclui os carbonatos de alta porosidade que a **a01 deste mesmo módulo** declara possíveis (30-40%). Uma greda (*chalk*) muito porosa fica em 2,3-2,6 km/s — mais lenta que a maioria dos arenitos.
**Correção aplicada:** faixa qualificada para carbonato **denso**, com a greda inserida como contraexemplo explícito de que a litologia sozinha não fixa a velocidade. Recap ajustado.
**Fonte:** SEG Wiki, *Velocities in limestone and sandstone* (greda 2.300-2.600 m/s) · **Confiança:** confirmado

---

### 🟡 12. Hematita admitida como fonte do magnetismo de formações ferríferas

**claim_id:** `PETROFIS-M15-A03-FERRIFERAS-009`
**Tipo:** inconsistência interna
**Onde:** a03 · "Magnetismo: três comportamentos..."
**Estava escrito:** "formações ferríferas bandadas, que podem ser fortemente magnéticas pela concentração de magnetita **e/ou hematita** em bandas maciças"
**Problema:** o "e/ou hematita" reinstala exatamente a armadilha que o parágrafo anterior desarma corretamente ("tem óxido de ferro" ≠ "é magnético"). Itabirito e minério hematíticos são fracamente magnéticos apesar do ferro alto — e essa diferença é o critério operacional corrente para separá-los da fácies magnetítica em levantamento magnético no Quadrilátero Ferrífero.
**Correção aplicada:** ressalva inserida restringindo o magnetismo às fácies ricas em magnetita, com o contraste hematítico nomeado e o exemplo brasileiro registrado. Recap ajustado.

---

### 🟡 13. Basalto agrupado com rocha ultramáfica nos teores de K, U e Th

**claim_id:** `PETROFIS-M15-A03-VALORESTIPICOS-006`
**Tipo:** confusão de escopo
**Onde:** a03 · "Minerais e rochas responsáveis pela radioatividade natural"
**Problema:** válido para toleíto oceânico e para peridotito, mas basaltos continentais e alcalinos chegam a cerca de 1% de K e alguns ppm de Th. Colapsar os dois grupos remove justamente o contraste **interno** a uma província basáltica, que é o que se explora ao mapear derrames distintos — e o Módulo 16, que depende deste, precisará dessa discriminação.
**Correção aplicada:** os dois grupos separados, com a faixa de cada um e a consequência para mapeamento nomeada.

---

### 🟡 14. "Razão Th/U alta (4,5)" sem régua de referência

**claim_id:** `PETROFIS-M15-A03-RAZAOTHU-007`
**Tipo:** certeza indevida
**Onde:** a03 · Exemplo trabalhado, interpretação da Área 1
**Problema:** 4,5 é uma razão **normal**, não alta: a IAEA usa ≈2 a 7 como faixa de rocha não alterada, com <2 indicando ambiente redutor e >7 indicando lixiviação oxidante do urânio. Chamar 4,5 de "alta" atribui poder diagnóstico a um valor comum e obscurece onde está a informação real do exercício — que é a anomalia da Área 2 (Th/U = 0,5), não a normalidade da Área 1.
**Correção aplicada:** régua da IAEA inserida antes das duas interpretações; Área 1 reinterpretada como granito **fresco** cuja informação vem dos valores absolutos altos de K e Th, com a razão apenas confirmando ausência de alteração; Área 2 explicitamente ancorada abaixo do limiar de 2. Recap reescrito em torno da régua.
**Fonte:** IAEA (2003), *Guidelines for Radioelement Mapping* · **Nível:** normativa · **Confiança:** confirmado

---

### 🟡 15. Magnetometria reduzida a susceptibilidade, deixando a magnetização remanente de fora

**claim_id:** `PETROFIS-M15-A04-INTEGRACAO-005`
**Tipo:** omissão que gera erro
**Onde:** a04 · tabela de integração
**Problema:** a magnetometria responde à **magnetização total** = induzida + remanente. A a03 introduz a remanência corretamente (e a nomeia como base do paleomagnetismo e das anomalias que persistem em rochas antigas) e a tabela então a descarta. A razão entre as duas parcelas — razão de Koenigsberger — é conceito central do Módulo 16, que tem este módulo como pré-requisito.
**Correção aplicada:** linha da tabela reescrita para "magnetização total (induzida + remanente)", com a razão de Koenigsberger nomeada.

---

### 🟡 16. Três contagens diferentes das propriedades do módulo, e nenhuma correta

**claim_id:** `PETROFIS-M15-A04-CONTAGEM-009`
**Tipo:** inconsistência interna
**Onde:** a04 · título de seção, corpo e recap
**Problema:** o título dizia "as **quatro** propriedades físicas do módulo", o corpo dizia "**seis** propriedades" e o recap dizia "as **seis** propriedades" — enquanto as três listas enumeravam **sete** itens (porosidade, permeabilidade, densidade, elasticidade, magnetismo, radioatividade, condutividade). Defeito pequeno, mas na seção de fechamento do módulo, que é a que o aluno usa para conferir se cobriu tudo.
**Correção aplicada:** título generalizado, corpo e recap corrigidos para sete.

---

### 🟡 17. "Quase todo método geofísico" depende da porosidade, seguido de duas exceções em cinco

**claim_id:** `PETROFIS-M15-A04-QUASETODO-010`
**Tipo:** certeza indevida
**Onde:** a04 · parágrafo de fechamento da tabela
**Problema:** a frase generalizava e o mesmo parágrafo então listava magnetometria e gamaespectrometria como cegas à variável — duas exceções em cinco métodos, o que é muito para caber em "quase todo". O achado é de precisão, mas também de oportunidade perdida: a contagem exata (três dependem, dois não) é justamente o que transforma a observação em argumento a favor da integração multimétodo.
**Correção aplicada:** frase reescrita com a contagem explícita e a conclusão invertida em ganho — "o método que ignora a porosidade é o que resolve a ambiguidade do método que não a ignora". Recap alinhado.

---

### ⚪ 18. A criação de porosidade por dolomitização apresentada como consenso

**claim_id:** `PETROFIS-M15-A01-DOLOMITIZACAO-006`
**Tipo:** controvérsia
**Onde:** a01 · "Porosidade: definição e o que ela não diz sozinha"
**Estava escrito:** "dolomitização (a conversão de calcita a dolomita reduz o volume do sólido em cerca de 12-13%, **criando poros novos**)"
**Problema:** o **número está certo** — 2 × 36,9 cm³/mol de calcita contra 64,3 cm³/mol de dolomita dá ~13% de redução do sólido. O que não é consenso é a consequência. O modelo mol a mol (Weyl, 1960) produz esse ganho, mas exige um sistema **aberto** que importe Mg e exporte Ca; o modelo alternativo de substituição volume a volume com cimentação (Lucia) prevê **redução** de porosidade; e há literatura que trata os "13% de porosidade" como artefato de uma hipótese de trabalho que a rocha real raramente satisfaz. Machel (2004) faz a reavaliação crítica de referência.
**Desfecho:** conforme a política para achados controversos, **nenhum lado foi escolhido**. O número foi mantido e reforçado com a aritmética molar explícita; a consequência porosa foi reescrita como hipótese condicional, com as duas posições e seus proponentes nomeados. Recap ajustado. Fontes completadas com Weyl (1960) e Machel (2004).

---

### ⚪ 19. Densidade de grão da dolomita: mineral (2,85) × convenção de perfilagem (2,87)

**claim_id:** `PETROFIS-M15-A02-DENSIDADEGRAO-001`
**Tipo:** controvérsia de convenção
**Onde:** a02 · "Três densidades que não são a mesma coisa"
**Problema:** "dolomita cerca de 2,85 g/cm³" está correto como **densidade mineral** (faixa 2,84-2,86). Mas a convenção de densidade de matriz usada em interpretação de perfil — o mundo em que a a04 entra — é **2,87**. Não é erro; é divergência de convenção entre dois usos que este módulo atravessa.
**Desfecho:** **não corrigido, e deliberadamente.** A aula diz "densidade de grão", contexto em que 2,85 é o valor certo, e trocar por 2,87 introduziria erro no contexto declarado. Registrado aqui para que uma futura aula de perfilagem não trate a divergência como contradição. Sem impacto no material.

---

## Verificado e correto (não gerou achado)

- **Geometrias de empacotamento**: 47,6% (cúbico) e 26% (romboédrico) — confirmados por cálculo direto.
- **Faixas de porosidade por litologia** (a01) — coerentes com Schön e Ellis & Singer.
- **Faixas de permeabilidade** e a conversão mD↔darcy: 10⁻³ a 10⁻⁶ mD = microdarcy a nanodarcy ✓; nanodarcy = bilionésimo de darcy ✓.
- **Definição de permeabilidade por Darcy**, controle por garganta de poro, Kozeny-Carman, e a tese central porosidade ≠ permeabilidade.
- **Exemplo trabalhado da a01**: 12/50 = 24%, 9/50 = 18%, 6 pp isolados = 25% da porosidade, superestimativa relativa de 33% — todos conferem.
- **Densidades de grão** quartzo 2,65 e calcita 2,71 ✓ (dolomita, ver achado 19).
- **Faixas de densidade bulk** por litologia — coerentes com Telford e Schön.
- **Vp = √[(K+4G/3)/ρ] e Vs = √(G/ρ)** ✓; onda P como única a atravessar o núcleo externo ✓.
- **Efeito do fluido**: G insensível, K sensível, Vp cai e Vs não muda com gás, Vp/Vs cai — mecanismo de *bright spot* correto.
- **Vp/Vs 1,8-1,9 (carbonatos) e 1,6-1,8 (arenitos limpos)** ✓ contra Christensen (1996).
- **Impedância acústica** como origem das reflexões ✓.
- **Os três comportamentos magnéticos** e seus minerais representativos ✓.
- **Regra do "menos de 1% de magnetita domina a susceptibilidade"** ✓; hematita ~3 ordens de grandeza abaixo ✓.
- **Séries magnetita/ilmenita** (Ishihara) ✓ — e é essa passagem correta que denunciou o achado 2.
- **Abundância do ⁴⁰K de ~0,012%** ✓ (valor exato 0,0117%).
- **Incompatibilidade geoquímica de U e Th** por raio iônico, concentração em líquidos residuais e em zircão/monazita/allanita/apatita ✓; mobilidade do U em meio oxidante e reprecipitação em meio redutor ✓.
- **Teores de K-U-Th de granito** (3-5% K, 3-5 ppm U, 15-20 ppm Th) ✓ contra IAEA.
- **Unidades API** e o poço-padrão do American Petroleum Institute ✓.
- **Exemplo Th/U**: 18/4 = 4,5 e 6/12 = 0,5 ✓; lógica de interpretação sólida.
- **Origem eletrolítica da condutividade**, isolamento dos silicatos, condução eletrônica por sulfetos maciços e grafita ✓.
- **Condutividade de superfície** por dupla camada elétrica e a ressalva de Waxman-Smits ✓.
- **Archie (1942)**, *Transactions of the AIME* 146(1), 54-62 — citação correta; Gus Archie corretamente identificado como engenheiro.
- **F = R₀/Rw = a/φ^m** e **Sw = (F·Rw/Rt)^(1/n)** ✓; m sobe com tortuosidade e cai com fraturamento ✓ (pareamento correto, achado só na independência de a e m).
- **Exemplo de Archie da a04**: F = 20,7, R₀ = 1,66, Sw = 37,1%, Sh = 63%, Rt/R₀ ≈ 7,3 — recalculados, todos conferem.
- **Penetração da gamaespectrometria** de poucos cm a dm ✓.
- **As 16 referências bibliográficas originais** foram conferidas uma a uma quanto a ano, volume, edição e paginação. **Nenhuma tem defeito** — contraste notável com o Módulo 12 (1 achado bibliográfico) e o Módulo 13 (4). Sete referências novas foram acrescentadas pelas correções (Weyl 1960, Machel 2004 e o glossário Schlumberger na a01; Ishihara 1977 e a literatura da transição de Néel na a03; Winsauer et al. 1952 e Anderson 1986 na a04), totalizando 23.

---

## Verificação transversal (cross-module)

Busca em todo o curso por: Archie, ilmenita, magnetita, hematita, pirrotita, Poisson, porosidade efetiva, susceptibilidade, expoente de cimentação, expoente de saturação, impedância acústica.

**UMA CONTRADIÇÃO TRANSVERSAL ENCONTRADA, e ela é o achado 2.** O Módulo 09 (Geometalurgia), a05, já ensina ao aluno — corretamente — que a separação magnética de alta intensidade "separa minerais **paramagnéticos** fracos (hematita, **ilmenita**, wolframita, monazita, granada)", e que a de baixa intensidade separa "magnetita e **pirrotita monoclínica**... a rigor ferrimagnéticos". A redação original da a03 do Módulo 15 afirmava o oposto sobre a ilmenita. A correção **restabelece a consistência nos dois sentidos**: a ilmenita passa a ser declarada paramagnética, e a pirrotita monoclínica passa a ser nomeada entre os ferrimagnéticos, exatamente como o Módulo 09 já a classificava. Os dois módulos agora se reforçam.

**Módulo 12 (Engenharia de petróleo), a02 — lei de Archie.** Sem contradição. O Módulo 12 já ensina que "esses parâmetros não são universais: são calibrados por rocha e por bacia... e seu uso sem calibração local é uma fonte conhecida de erro sistemático", o que é plenamente compatível com o que a a04 corrigida agora aprofunda. Duas observações registradas:

1. **Divergência numérica menor, harmonizada.** O Módulo 12 usa m de 1,8-2,2 para "arenitos consolidados"; o Módulo 15 usava 1,8-2,0 para "arenitos limpos". As faixas não se contradizem (são populações diferentes), mas o aluno que comparasse os dois números não teria como saber disso. A a04 passou a declarar as duas faixas e a nomear o Módulo 12 explicitamente.
2. **Incompletude, não erro, deixada intocada no Módulo 12.** A a02 do Módulo 12 apresenta n como "tipicamente próximo de 2" sem a ressalva de molhabilidade do achado 8. Isso **não é falso** — é menos completo. Como o Módulo 12 está fechado, com questionário de 16 questões e baralho de 239 flashcards já gerados, alterá-lo exigiria repropagar por todo esse material derivado, e o custo/risco não se justifica para uma incompletude que não induz a erro (o próprio Módulo 12 já adverte que os parâmetros exigem calibração local). **Encaminhado para a auditoria `cross-course` de fechamento do curso**, onde a decisão pode ser tomada com o curso inteiro à vista.

**Módulo 05 (Mecânica de rochas)** usa módulo de Young e coeficiente de Poisson em contexto geomecânico estático, sem colisão com o uso dinâmico/sísmico do Módulo 15. A correção do achado 5 alinha os dois: a definição de Poisson passou a ser dada com o rigor que o Módulo 05 já pressupõe.

**Colisão de símbolos registrada, sem correção.** O símbolo **K** significa condutividade hidráulica no Módulo 01 (hidrogeologia) e módulo de compressibilidade no Módulo 15; o símbolo **k** é permeabilidade intrínseca na a01 do Módulo 15. Não é erro em nenhum dos dois — é convenção estabelecida em ambas as disciplinas —, mas é um ponto de confusão previsível. **Encaminhado à revisão didática** (não é achado factual).

---

## Advertências ao gerador de questionários e de flashcards

1. **O par 1,73 × 1,85 é o material de avaliação mais valioso do módulo.** Vp/Vs = √3 = 1,73 ⇔ ν = 0,25 é arenito limpo/granito; 1,8-1,9 é carbonato. O erro corrigido virou o distrator perfeito, e o parágrafo do caso-limite na a02 já entrega a discriminação pronta. Prefira questão de discriminação a definição isolada.
2. **NÃO gerar card ou gabarito que diga que a ilmenita contribui para a susceptibilidade magnética de rocha.** Foi exatamente esse o erro corrigido, e ele contradiz o Módulo 09. O distrator correto é "magnetita **e ilmenita**"; a resposta certa é "magnetita e titanomagnetita". Excelente card: *por que um granito de série ilmenita é fracamente magnético?*
3. **Ilmenita: T_N ≈ 57 K** é par numérico limpo e novo no material após a correção.
4. **"Duas séries e um isótopo"** é formulação de alto valor mnemônico. As três energias (K 1,46 MeV; ²¹⁴Bi 1,76 MeV; ²⁰⁸Tl 2,61 MeV) são novas no material e formam trinca limpa. O melhor card conceitual do bloco: *por que se escreve eU e eTh, mas apenas K?*
5. **Fuga do radônio** como razão de o canal de U ser o menos confiável — cadeia causal completa, ótima para dissertativa curta.
6. **n de Archie × molhabilidade** é a melhor questão de aplicação quantitativa do módulo: os números 37% (n=2) e 78% (n=8) já estão calculados na a04 sobre o mesmo dado, admitem variação numérica infinita, e a questão pode cobrar a **direção** do erro (superestima hidrocarboneto), que é onde está o valor.
7. **a e m em pares**: distrator forte é "a = 0,62 com m = 2". Não criar questão que trate a e m como escolhas independentes.
8. **Reflexão × refração**: distrator forte é atribuir impedância acústica à refração.
9. **Th/U contra a régua da IAEA** (<2 redutor, 2-7 normal, >7 lixiviado): não criar questão de gabarito fechado que chame 4,5 de "alto". A questão boa cobra o limiar, não o adjetivo.
10. **Porosidade efetiva** é achado de duas definições: qualquer questão precisa dizer se o contexto é testemunho ou perfil. Excelente questão de discriminação.
11. **Dolomitização é achado ⚪ branco**: não criar questão de gabarito fechado que afirme que a dolomitização cria porosidade, nem que não cria. Os ~13% de redução do sólido, esses sim, são cobráveis como estequiometria.
12. **Densidade da dolomita** (achado 19): se usar em questão, especificar "densidade de grão" (2,85) e não misturar com a convenção de perfilagem (2,87).
13. **Porosimetria de mercúrio não alcança poro isolado** — distrator forte, e o exemplo da a01 já está aritmeticamente correto e reutilizável para números novos.
14. **Greda a 2,3-2,6 km/s** é o contraexemplo mais limpo do módulo contra "litologia determina velocidade" — novo no material após a correção.
15. **Três métodos dependem da porosidade, dois são cegos a ela**: contagem exata, ótima para questão de integração e para o fechamento do módulo.

---

## Correções aplicadas

**Aplicadas em:** 2026-09-08

| claim_id | Sev. | Desfecho | Arquivos alterados |
|---|---|---|---|
| `PETROFIS-M15-A02-EXEMPLOCALCARIO-008` | 🔴 | Corrigido | aula-02 |
| `PETROFIS-M15-A03-ILMENITA-008` | 🔴 | Corrigido | aula-03, aula-04 |
| `PETROFIS-M15-A01-POROSIMETRIA-008` | 🟠 | Corrigido | aula-01 |
| `PETROFIS-M15-A01-POROSIDADEEFETIVA-007` | 🟠 | Corrigido | aula-01, aula-04 |
| `PETROFIS-M15-A02-POISSONLIMITE-009` | 🟠 | Corrigido | aula-02 |
| `PETROFIS-M15-A03-ESPECTROMETRIA-004` | 🟠 | Corrigido | aula-03 |
| `PETROFIS-M15-A04-ARCHIEAM-006` | 🟠 | Corrigido | aula-04 |
| `PETROFIS-M15-A04-ARCHIEN-007` | 🟠 | Corrigido | aula-04 |
| `PETROFIS-M15-A04-REFRACAO-008` | 🟠 | Corrigido | aula-04 |
| `PETROFIS-M15-A02-BASALTOMINERAL-010` | 🟡 | Corrigido | aula-02 |
| `PETROFIS-M15-A02-VPLITOLOGIA-007` | 🟡 | Corrigido | aula-02 |
| `PETROFIS-M15-A03-FERRIFERAS-009` | 🟡 | Corrigido | aula-03 |
| `PETROFIS-M15-A03-VALORESTIPICOS-006` | 🟡 | Corrigido | aula-03 |
| `PETROFIS-M15-A03-RAZAOTHU-007` | 🟡 | Corrigido | aula-03 |
| `PETROFIS-M15-A04-INTEGRACAO-005` | 🟡 | Corrigido | aula-04 |
| `PETROFIS-M15-A04-CONTAGEM-009` | 🟡 | Corrigido | aula-04 |
| `PETROFIS-M15-A04-QUASETODO-010` | 🟡 | Corrigido | aula-04 |
| `PETROFIS-M15-A01-DOLOMITIZACAO-006` | ⚪ | Reescrito com a divergência explícita | aula-01 |
| `PETROFIS-M15-A02-DENSIDADEGRAO-001` | ⚪ | Aceito como está (registrado) | — |

**Pendências:** nenhuma bloqueante. `open_findings: []`.
Uma recomendação encaminhada para fora do módulo: reavaliar, na auditoria `cross-course` de fechamento do curso, se a a02 do Módulo 12 deve receber a ressalva de molhabilidade do achado 8 — decisão adiada por causa do custo de repropagação num módulo já fechado, e porque a afirmação de lá não é falsa, apenas menos completa.

**Gate:** ✅ liberado para o gerador de questionários.
