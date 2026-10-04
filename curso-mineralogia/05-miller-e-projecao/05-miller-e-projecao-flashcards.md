# Flashcards — Módulo 05: Eixos cristalográficos, índices de Miller e projeção estereográfica

**Módulo:** [[05-miller-e-projecao-modulo|Módulo 05 — Eixos cristalográficos, índices de Miller e projeção estereográfica]]
**Total:** 118 cards — 100 Basic + 18 Cloze
**Faixa de IDs:** `mineralogia-m05-fb001`–`fb100` · `mineralogia-m05-fc001`–`fc018`
**Auditoria:** aprovada em 2026-10-04, sem achados 🔴/🟠 em aberto — gate liberado.
**Didática:** revisão concluída em 2026-10-04 (aula 05 dividida; aula 07 nova)
**Questionário:** gerado em 2026-10-04 (parciais 1 e 2 + final; 30 questões, 5 objetivos cobertos)
**Gerado em:** 2026-10-04, contra as aulas já auditadas e revisadas do módulo.

> [!info] Primeira geração
> Não há baralho prévio deste módulo. Todos os IDs são novos. Importe os dois CSVs num deck limpo.

## Arquivos para importar

| Arquivo | Tipo de nota no Anki | Campos |
|---|---|---|
| `05-miller-e-projecao-flashcards-basic.csv` | Basic | id, frente, verso, tags, objetivo, aula, dificuldade, fonte |
| `05-miller-e-projecao-flashcards-cloze.csv` | Cloze | id, texto, extra, tags, objetivo, aula, dificuldade, fonte |

> [!tip] Importação no Anki
> Importe os dois **separadamente**. Marque "Campos separados por ponto-e-vírgula" e mapeie `id` como primeiro campo. As tags são hierárquicas (`mineralogia::m05::...`).

## Distribuição

| Aula | Objetivo | Basic | Cloze | Total |
|---|---|---|---|---|
| a01 — Eixos e parâmetros de cela | `oa01` | 16 | 3 | 19 |
| a02 — Índices de Miller e formas | `oa02` | 18 | 2 | 20 |
| a03 — Direções e Miller-Bravais | `oa02` | 16 | 3 | 19 |
| a04 — Zonas e lei de Weiss | `oa03` | 13 | 2 | 15 |
| a05 — Projeção estereográfica | `oa04` | 14 | 2 | 16 |
| a06 — Medir na rede de Wulff | `oa05` | 10 | 2 | 12 |
| a07 — Simetria no estereograma | `oa04` | 13 | 4 | 17 |

**Cobertura:** os cinco objetivos do módulo têm card. Nenhum card órfão.

## Critérios aplicados

- **Cada card é rastreável a uma frase das aulas auditadas** (`05-miller-e-projecao-auditoria.md`); nenhum índice, ângulo, forma ou classe foi acrescentado fora delas.
- **Nenhum card pede parâmetro de cela com decimais**, seguindo a revisão didática (a tabela de minerais reais da aula 01 é de consulta). Os únicos números decorados são os ângulos do cubo (54,7°, 45°, 70,5°), os dois ângulos do quartzo que a aula 06 mede (38,2° e 46,3°) e as frações r/R.
- **Nenhum card depende de figura.** As perguntas sobre estereogramas descrevem o padrão em palavras (cheios, abertos, a cada 90°...).
- **Cloze com no máximo 3 lacunas por nota e sem chaves dentro das lacunas**: os símbolos de forma com chaves, como {101̄1}, ficaram só em cards Basic, porque uma chave dentro de `{{c1::...}}` quebra a nota no Anki.
- **As correções da auditoria têm card próprio**: eixos do cúbico ao longo de 4 ou 4̄ (`fb012`) e o ângulo entre faces de mesmos índices no cúbico (`fb015`).

## Cards Basic

| ID | Frente | Verso | Aula | Objetivo |
|---|---|---|---|---|
| `mineralogia-m05-fb001` | Na figura padrão dos eixos cristalográficos, para onde aponta a extremidade positiva de a, de b e de c? | a para o observador, b para a direita, c para cima. | a01 | `oa01` |
| `mineralogia-m05-fb002` | Qual é a regra para lembrar os nomes dos ângulos α, β e γ entre os eixos? | Cada ângulo leva o nome do eixo que ele não toca (α entre b e c, β entre a e c, γ entre a e b). | a01 | `oa01` |
| `mineralogia-m05-fb003` | Por que os eixos cristalográficos são postos ao longo de eixos de rotação ou perpendiculares a espelhos? | Para que faces equivalentes pela simetria recebam endereços parecidos; o preço é que os eixos nem sempre são perpendiculares nem iguais. | a01 | `oa01` |
| `mineralogia-m05-fb004` | O que são os parâmetros de cela? | Os seis números a, b, c, α, β, γ da unidade que, repetida, constrói o cristal (a cela unitária). | a01 | `oa01` |
| `mineralogia-m05-fb005` | O que a forma externa de um cristal permite medir dos parâmetros de cela, sem raios X? | Só as proporções entre os comprimentos (a razão axial); os comprimentos em ångströms vêm da difração. | a01 | `oa01` |
| `mineralogia-m05-fb006` | Quanto vale 1 ångström (Å)? | 10⁻¹⁰ m, ou 0,1 nanômetro. | a01 | `oa01` |
| `mineralogia-m05-fb007` | Quais são as relações entre os parâmetros de cela no sistema tetragonal? | a₁ = a₂ ≠ c; α = β = γ = 90°. | a01 | `oa01` |
| `mineralogia-m05-fb008` | Quais são as relações entre os parâmetros de cela no sistema ortorrômbico? | a ≠ b ≠ c; α = β = γ = 90°. | a01 | `oa01` |
| `mineralogia-m05-fb009` | Quais são as relações entre os parâmetros de cela no sistema monoclínico (convenção usual)? | a ≠ b ≠ c; α = γ = 90°; β ≠ 90°, tomado como obtuso. | a01 | `oa01` |
| `mineralogia-m05-fb010` | Como são os eixos usados pelos sistemas hexagonal e trigonal? | Três eixos a iguais, a 120° entre si num plano, e c perpendicular a eles (α = β = 90°, γ = 120°). | a01 | `oa01` |
| `mineralogia-m05-fb011` | No monoclínico, na convenção mais usada em mineralogia, qual é o eixo especial e como se chama essa convenção? | O eixo b, ao longo do único eixo 2 (ou normal ao único espelho); é a 'segunda posição'. | a01 | `oa01` |
| `mineralogia-m05-fb012` | No sistema cúbico, ao longo de que elementos de simetria ficam os eixos cristalográficos? | Ao longo dos três eixos 4 ou 4̄; nas classes 23 e m3̄, que não têm nenhum dos dois, ao longo dos três eixos 2. | a01 | `oa01` |
| `mineralogia-m05-fb013` | O que quer dizer 'a ≠ b' numa tabela de relações de parâmetros? | Que a simetria não obriga a igualdade; a coincidência numérica continua possível. | a01 | `oa01` |
| `mineralogia-m05-fb014` | A cianita tem α = 89,99°. Por que ela continua triclínica? | Porque nenhuma simetria obriga esse ângulo a valer 90°: o sistema vem da simetria, não dos números. | a01 | `oa01` |
| `mineralogia-m05-fb015` | Por que o ângulo entre (100) e (111) é o mesmo na halita, na fluorita e na galena? | No cúbico não há razão axial (a₁ = a₂ = a₃, ângulos retos); os ângulos não dependem do tamanho da cela. | a01 | `oa01` |
| `mineralogia-m05-fb016` | Os parâmetros a = b, α = β = 90°, γ = 120° distinguem um cristal trigonal de um hexagonal? | Não: os dois usam eixos hexagonais; quem decide é a simetria (o quartzo, com esses eixos, é trigonal). | a01 | `oa01` |
| `mineralogia-m05-fb017` | Que índice de Miller recebe um eixo ao qual a face é paralela? | 0: o intercepto é infinito e o seu inverso é zero. | a02 | `oa02` |
| `mineralogia-m05-fb018` | Como se escreve um índice de Miller negativo? | Com uma barra sobre o número: 1̄ vale −1. | a02 | `oa02` |
| `mineralogia-m05-fb019` | Quais são os índices de Miller da face com interceptos 1a : 2b : ∞c? | (210). | a02 | `oa02` |
| `mineralogia-m05-fb020` | Uma face corta a em 2 e b em 1 e é paralela a c. Quais são os índices? | (120): os interceptos têm de ser invertidos antes de virar índices. | a02 | `oa02` |
| `mineralogia-m05-fb021` | Um índice de Miller grande num eixo diz o quê sobre o intercepto naquele eixo? | Que o intercepto é pequeno: a face corta aquele eixo perto do centro. | a02 | `oa02` |
| `mineralogia-m05-fb022` | O que são os parâmetros de Weiss? | Os interceptos de uma face escritos em unidades de a, b e c, como 1a : 2b : ∞c. | a02 | `oa02` |
| `mineralogia-m05-fb023` | Quem propôs os índices de Miller, e em que ano? | William Hallowes Miller, em 1839 (A Treatise on Crystallography). | a02 | `oa02` |
| `mineralogia-m05-fb024` | O que é a face unitária de um cristal? | A face escolhida como (111), cujos interceptos definem as proporções a : b : c. | a02 | `oa02` |
| `mineralogia-m05-fb025` | Que lei garante que os índices de Miller de faces reais são inteiros pequenos? | A lei de Haüy (racionalidade dos índices). | a02 | `oa02` |
| `mineralogia-m05-fb026` | Quais são os índices da face paralela a (210), do outro lado do cristal? | (2̄1̄0): todos os sinais trocados. | a02 | `oa02` |
| `mineralogia-m05-fb027` | Na morfologia, (420) e (210) são faces diferentes? | Não: têm a mesma orientação; reduz-se sempre aos menores inteiros. | a02 | `oa02` |
| `mineralogia-m05-fb028` | Qual é a diferença entre (hkl) e {hkl}? | (hkl) é uma face; {hkl} é a forma: todas as faces equivalentes a ela pela simetria da classe. | a02 | `oa02` |
| `mineralogia-m05-fb029` | Que forma é {100} num cristal cúbico, e quantas faces tem? | O cubo, 6 faces. | a02 | `oa02` |
| `mineralogia-m05-fb030` | Que forma é {111} num cristal cúbico holoédrico, e quantas faces tem? | O octaedro, 8 faces. | a02 | `oa02` |
| `mineralogia-m05-fb031` | Quantas faces tem o dodecaedro rômbico, e qual é o seu símbolo de forma? | 12 faces; {110}. | a02 | `oa02` |
| `mineralogia-m05-fb032` | Que forma é {210} na pirita (classe m3̄), e quantas faces tem? | O piritoedro, 12 faces pentagonais. | a02 | `oa02` |
| `mineralogia-m05-fb033` | Por que {210} tem 12 faces na classe m3̄ e 24 na classe m3̄m? | O número de faces de uma forma depende da classe: mais simetria multiplica mais a face de partida. | a02 | `oa02` |
| `mineralogia-m05-fb034` | As faces mais comuns e desenvolvidas dos cristais costumam ter índices altos ou baixos? | Baixos, como {100}, {110} e {111} (tendência empírica). | a02 | `oa02` |
| `mineralogia-m05-fb035` | Como se obtém o símbolo [uvw] de uma direção? | Andando u, v e w passos ao longo de a, b e c, da origem até um ponto da reta, e reduzindo aos menores inteiros, sem inverter. | a03 | `oa02` |
| `mineralogia-m05-fb036` | Qual é o símbolo de direção do eixo c? | [001]. | a03 | `oa02` |
| `mineralogia-m05-fb037` | O que significa o símbolo ⟨uvw⟩? | Uma família de direções equivalentes pela simetria, como ⟨111⟩, as diagonais do cubo. | a03 | `oa02` |
| `mineralogia-m05-fb038` | Em que sistema a direção [hkl] é sempre perpendicular à face (hkl)? | Só no cúbico, onde os eixos são iguais e perpendiculares. | a03 | `oa02` |
| `mineralogia-m05-fb039` | No monoclínico, a direção [001] é perpendicular à face (001)? | Não: c é inclinado em relação ao plano ab (β ≠ 90°). | a03 | `oa02` |
| `mineralogia-m05-fb040` | Por que os sistemas hexagonal e trigonal usam quatro índices para as faces? | Com três, as seis faces equivalentes do prisma ganham índices de aparência diferente; com quatro, todas são arranjos de 1, 0 e −1. | a03 | `oa02` |
| `mineralogia-m05-fb041` | Que forma é {101̄0}? | O prisma hexagonal de primeira ordem. | a03 | `oa02` |
| `mineralogia-m05-fb042` | Que forma é {112̄0}? | O prisma hexagonal de segunda ordem, girado 30° em relação ao de primeira ordem. | a03 | `oa02` |
| `mineralogia-m05-fb043` | Que forma é {0001}? | O pinacoide basal: o par de faces perpendiculares a c. | a03 | `oa02` |
| `mineralogia-m05-fb044` | Como se converte uma face (hkil) para três índices? | Apaga-se o i: (101̄1) → (101). | a03 | `oa02` |
| `mineralogia-m05-fb045` | Como fica a face (110) com quatro índices? | (112̄0), com i = −(1 + 1). | a03 | `oa02` |
| `mineralogia-m05-fb046` | Que notação o curso usa para direções nos sistemas hexagonal e trigonal? | Três índices [UVW], referidos a a₁, a₂ e c (o eixo c é [001]). | a03 | `oa02` |
| `mineralogia-m05-fb047` | Por que a clivagem da calcita aparece como {101̄4} em livros modernos e {101̄1} em antigos? | É o mesmo plano referido a celas diferentes: a cela estrutural tem c quatro vezes maior que a cela morfológica antiga. | a03 | `oa02` |
| `mineralogia-m05-fb048` | Quais são os índices da forma r do quartzo? | {101̄1}, um romboedro. | a03 | `oa02` |
| `mineralogia-m05-fb049` | Quais são os índices do prisma m do quartzo? | {101̄0}, o prisma de primeira ordem. | a03 | `oa02` |
| `mineralogia-m05-fb050` | Numa classe hexagonal como 6/mmm, que forma é {101̄1} e quantas faces tem? | Uma bipirâmide hexagonal de 12 faces. | a03 | `oa02` |
| `mineralogia-m05-fb051` | O que é uma zona de faces? | O conjunto de faces cujas arestas de interseção são paralelas a uma mesma direção, o eixo de zona [uvw]. | a04 | `oa03` |
| `mineralogia-m05-fb052` | O que são faces tautozonais? | Faces que pertencem à mesma zona. | a04 | `oa03` |
| `mineralogia-m05-fb053` | A lei das zonas de Weiss vale em sistemas de eixos oblíquos, como o monoclínico? | Sim: ela usa coordenadas ao longo dos próprios eixos, e vale em qualquer sistema. | a04 | `oa03` |
| `mineralogia-m05-fb054` | Por que toda face (hk0) pertence à zona [001]? | Porque h·0 + k·0 + 0·1 = 0: toda face com l = 0 é paralela a c. | a04 | `oa03` |
| `mineralogia-m05-fb055` | Que procedimento dá o eixo de zona de duas faces? | A regra da cruz: escrever os índices duas vezes, riscar a primeira e a última coluna e multiplicar em cruz. | a04 | `oa03` |
| `mineralogia-m05-fb056` | Qual é o eixo da zona que contém (100) e (111)? | [01̄1] (ou [011̄], a mesma reta). | a04 | `oa03` |
| `mineralogia-m05-fb057` | Trocar a ordem das duas faces na regra da cruz muda a zona? | Não: troca todos os sinais, e [uvw] e [ūv̄w̄] são a mesma reta. | a04 | `oa03` |
| `mineralogia-m05-fb058` | Como se acha a face comum a duas zonas? | Aplicando a regra da cruz aos dois eixos de zona. | a04 | `oa03` |
| `mineralogia-m05-fb059` | O que diz a regra da adição das zonas? | Se duas faces estão numa zona, a face com a soma dos seus índices também está, entre as duas. | a04 | `oa03` |
| `mineralogia-m05-fb060` | Que face resulta de (100) + (010), e onde ela fica no cubo? | (110), a face do dodecaedro que trunca a aresta vertical entre (100) e (010), na zona [001]. | a04 | `oa03` |
| `mineralogia-m05-fb061` | O que fazer antes de aplicar a lei das zonas a faces hexagonais de quatro índices? | Converter tudo para três índices: (hkl) para faces e [UVW] para direções. | a04 | `oa03` |
| `mineralogia-m05-fb062` | Qual é o eixo da zona que contém as faces r (101̄1) e z (011̄1) do quartzo? | [1̄1̄1]. | a04 | `oa03` |
| `mineralogia-m05-fb063` | A face prevista pela regra da cruz sempre existe no cristal? | Não: é uma face possível; se aparece, depende do crescimento. | a04 | `oa03` |
| `mineralogia-m05-fb064` | O que é o polo de uma face na projeção estereográfica? | O ponto onde a normal da face fura a esfera de projeção, depois projetado no plano do equador. | a05 | `oa04` |
| `mineralogia-m05-fb065` | Na projeção estereográfica, a que ponto da esfera se ligam os polos do hemisfério de cima? | Ao polo sul (o ponto de vista); o cruzamento com o plano do equador é o ponto do desenho. | a05 | `oa04` |
| `mineralogia-m05-fb066` | O que é o círculo primitivo? | O equador da esfera de projeção, que vira a borda do estereograma. | a05 | `oa04` |
| `mineralogia-m05-fb067` | Onde cai o polo de uma face vertical (paralela a c)? | Sobre o círculo primitivo. | a05 | `oa04` |
| `mineralogia-m05-fb068` | Onde cai o polo da face (001), com c na vertical? | No centro do estereograma. | a05 | `oa04` |
| `mineralogia-m05-fb069` | Como se distinguem no estereograma os polos do hemisfério de cima e os de baixo? | Ponto cheio para os de cima; círculo aberto para os de baixo. | a05 | `oa04` |
| `mineralogia-m05-fb070` | A que fração do raio do primitivo cai um polo com ρ = 45°? | 0,414 R (não 0,5 R), porque r = R·tan(ρ/2). | a05 | `oa04` |
| `mineralogia-m05-fb071` | Na convenção usual, onde ficam os polos de (010) e de (100) no estereograma? | (010) à direita, sobre o primitivo; (100) embaixo, na posição do observador. | a05 | `oa04` |
| `mineralogia-m05-fb072` | Como aparece no estereograma um grande círculo vertical? | Como um diâmetro. | a05 | `oa04` |
| `mineralogia-m05-fb073` | Um grande círculo que não é vertical nem horizontal aparece no estereograma como que tipo de linha? | Um arco que corta o primitivo em dois pontos diametralmente opostos. | a05 | `oa04` |
| `mineralogia-m05-fb074` | Onde ficam, no estereograma, os polos das faces de uma mesma zona? | Sobre um mesmo grande círculo. | a05 | `oa04` |
| `mineralogia-m05-fb075` | Quem propôs a rede de Wulff, e em que ano? | Georg (Yuri) Wulff, em 1902. | a05 | `oa04` |
| `mineralogia-m05-fb076` | Por que a cristalografia morfológica usa a rede de Wulff, e não a de Schmidt? | A de Wulff preserva a forma dos círculos e serve para construir e medir; a de Schmidt, de igual área, serve para contar densidade de medidas (geologia estrutural). | a05 | `oa04` |
| `mineralogia-m05-fb077` | Quais são φ e ρ do polo de (111) num cristal cúbico? | φ = 45° e ρ = 54,7°. | a05 | `oa04` |
| `mineralogia-m05-fb078` | Ao longo de que linhas se medem ângulos entre polos na rede de Wulff? | Ao longo de grandes círculos: os meridianos da rede ou o primitivo. | a06 | `oa05` |
| `mineralogia-m05-fb079` | Na rede de Wulff, o que se gira para trazer dois polos ao mesmo meridiano? | O papel vegetal, em torno do alfinete no centro; nunca a rede. | a06 | `oa05` |
| `mineralogia-m05-fb080` | Como se acha o polo (eixo) de uma zona na rede de Wulff? | Com o meridiano da zona sobre a rede, contam-se 90° ao longo do diâmetro L-O, passando pelo centro. | a06 | `oa05` |
| `mineralogia-m05-fb081` | A que é igual o ângulo entre duas zonas? | Ao ângulo entre os seus polos (eixos de zona). | a06 | `oa05` |
| `mineralogia-m05-fb082` | Que fórmula dá o ângulo θ entre as normais de duas faces num cristal cúbico? | cos θ = (h₁h₂ + k₁k₂ + l₁l₂) / [√(h₁² + k₁² + l₁²) · √(h₂² + k₂² + l₂²)]. | a06 | `oa05` |
| `mineralogia-m05-fb083` | Por que a fórmula do produto escalar para ângulos entre faces só vale no cúbico? | Porque ela supõe eixos iguais e perpendiculares. | a06 | `oa05` |
| `mineralogia-m05-fb084` | Qual é o ângulo entre as normais de m (101̄0) e r (101̄1) no quartzo? | 38,2° (= 90° − 51,8°). | a06 | `oa05` |
| `mineralogia-m05-fb085` | Duas faces vizinhas da ponta do quartzo, r (101̄1) e z (011̄1), fazem que ângulo entre normais? | 46,3° (medido levando as duas ao mesmo meridiano da rede). | a06 | `oa05` |
| `mineralogia-m05-fb086` | Que relação há entre o ângulo lido no estereograma e o medido com um goniômetro de contato? | O estereograma dá o ângulo entre normais; o goniômetro, o ângulo interno; os dois somam 180°. | a06 | `oa05` |
| `mineralogia-m05-fb087` | Por que contar graus ao longo de um paralelo (pequeno círculo) da rede de Wulff é erro? | Pequenos círculos não medem ângulo entre polos; só os grandes círculos medem. | a06 | `oa05` |
| `mineralogia-m05-fb088` | Como se desenha um espelho no estereograma? | Como um grande círculo em traço cheio. | a07 | `oa04` |
| `mineralogia-m05-fb089` | O que indica o primitivo desenhado em traço cheio e grosso? | Um espelho horizontal. | a07 | `oa04` |
| `mineralogia-m05-fb090` | Qual é o símbolo de um eixo 6 no estereograma? | Um hexágono, no ponto onde o eixo fura a esfera. | a07 | `oa04` |
| `mineralogia-m05-fb091` | O que é a forma geral de uma classe? | A forma cujas faces não ficam sobre nenhum elemento de simetria; tem tantas faces quanto a ordem do grupo. | a07 | `oa04` |
| `mineralogia-m05-fb092` | Um eixo 2 horizontal troca o polo de hemisfério? E um eixo 2 vertical? | O horizontal troca; o vertical só gira o polo em torno do centro, sem trocar. | a07 | `oa04` |
| `mineralogia-m05-fb093` | Um espelho vertical troca o polo de hemisfério? | Não: ele reflete o polo de um lado para o outro do espelho, no mesmo hemisfério. | a07 | `oa04` |
| `mineralogia-m05-fb094` | Como é o estereograma da forma geral de 2/m, com b na horizontal? | 4 polos: 2 cheios e 2 abertos. | a07 | `oa04` |
| `mineralogia-m05-fb095` | Como é o estereograma da forma geral de mm2, com o eixo 2 em c? | 4 polos cheios, nenhum aberto (classe polar). | a07 | `oa04` |
| `mineralogia-m05-fb096` | Como é o estereograma da forma geral de 4/mmm? | 16 polos: 8 cheios, cada um sobre um aberto. | a07 | `oa04` |
| `mineralogia-m05-fb097` | Um estereograma de forma geral tem 4 polos, cheios e abertos alternados a cada 90° em torno do centro. Qual é a classe? | 4̄. | a07 | `oa04` |
| `mineralogia-m05-fb098` | Um estereograma de forma geral tem 3 polos cheios a 120° e um aberto sob cada um. Qual é a classe? | 6̄ (= 3/m). | a07 | `oa04` |
| `mineralogia-m05-fb099` | Como se reconhece o centro de simetria num estereograma que não tem símbolo para ele? | Cada polo cheio tem um polo aberto na posição diametralmente oposta. | a07 | `oa04` |
| `mineralogia-m05-fb100` | Por que o polo de partida da forma geral não pode ficar sobre um espelho? | Porque gera uma forma especial, com menos polos que a ordem do grupo. | a07 | `oa04` |

## Cards Cloze

| ID | Texto | Extra | Aula | Objetivo |
|---|---|---|---|---|
| `mineralogia-m05-fc001` | O ângulo α fica entre os eixos {{c1::b e c}}; o ângulo β, entre {{c2::a e c}}; o ângulo γ, entre {{c3::a e b}}. | Cada ângulo leva o nome do eixo que não toca. | a01 | `oa01` |
| `mineralogia-m05-fc002` | O sistema cúbico tem {{c1::1}} parâmetro de cela independente; o tetragonal e o hexagonal, {{c2::2}}; o ortorrômbico, {{c3::3}}. |  | a01 | `oa01` |
| `mineralogia-m05-fc003` | O sistema monoclínico tem {{c1::4}} parâmetros de cela independentes; o triclínico, {{c2::6}}. |  | a01 | `oa01` |
| `mineralogia-m05-fc004` | Para obter os índices de Miller, tomam-se os interceptos em unidades de a, b, c, calculam-se os {{c1::inversos}} e reduz-se aos {{c2::menores inteiros}}. | Paralelo = intercepto infinito = índice 0. | a02 | `oa02` |
| `mineralogia-m05-fc005` | Os interceptos em unidades de a, b, c chamam-se parâmetros de {{c1::Weiss}}; os seus inversos reduzidos, índices de {{c2::Miller}}. |  | a02 | `oa02` |
| `mineralogia-m05-fc006` | Nos índices de Miller-Bravais (hkil), o terceiro índice vale i = {{c1::−(h + k)}}. | Também chamados de Bravais-Miller. | a03 | `oa02` |
| `mineralogia-m05-fc007` | Faces se escrevem entre {{c1::parênteses}}, formas entre {{c2::chaves}} e direções entre {{c3::colchetes}}. | Família de direções: ⟨uvw⟩. | a03 | `oa02` |
| `mineralogia-m05-fc008` | No quartzo, a face r de índices (101̄1) se alterna na ponta com a face z de índices ({{c1::011̄1}}). | As duas formas são romboedros. | a03 | `oa02` |
| `mineralogia-m05-fc009` | Lei das zonas: a face (hkl) pertence à zona [uvw] quando {{c1::hu + kv + lw = 0}}. | Vale em qualquer sistema. | a04 | `oa03` |
| `mineralogia-m05-fc010` | Pela regra da adição, (100) + (110) = {{c1::(210)}}, face que fica entre (100) e (110) na zona [001]. |  | a04 | `oa03` |
| `mineralogia-m05-fc011` | A distância do polo ao centro do estereograma é r = {{c1::R·tan(ρ/2)}}, em que ρ é o ângulo entre a normal da face e o eixo c. | Por isso 45° cai a 0,414 R. | a05 | `oa04` |
| `mineralogia-m05-fc012` | O azimute φ é medido no primitivo a partir do polo {{c1::(010)}}, no sentido {{c2::horário}}; a distância polar ρ é medida a partir de {{c3::c}}. |  | a05 | `oa04` |
| `mineralogia-m05-fc013` | No cúbico, (100)∧(111) = {{c1::54,7}}°; (100)∧(110) = {{c2::45}}°; (111)∧(11̄1) = {{c3::70,5}}°. | Ângulos entre normais; valem para qualquer mineral cúbico. | a06 | `oa05` |
| `mineralogia-m05-fc014` | Redes de Wulff impressas para uso costumam ter linhas a cada {{c1::2}}°. |  | a06 | `oa05` |
| `mineralogia-m05-fc015` | No estereograma, o eixo 2 é uma {{c1::elipse}}, o eixo 3 um {{c2::triângulo}} e o eixo 4 um {{c3::quadrado}}. | Eixo 6: hexágono. | a07 | `oa04` |
| `mineralogia-m05-fc016` | O número de polos da forma geral é igual à {{c1::ordem do grupo}}. | Ex.: 2/m tem 4; 4/mmm tem 16. | a07 | `oa04` |
| `mineralogia-m05-fc017` | Forma geral de 4/m: 4 polos cheios {{c1::sobre}} 4 abertos; de 422: 4 cheios e 4 abertos {{c2::deslocados}}; de 4mm: {{c3::8 cheios}}. | As três classes têm ordem 8. | a07 | `oa04` |
| `mineralogia-m05-fc018` | Em m3̄m, os eixos 4 ficam nos polos do {{c1::cubo}}, os eixos 3 nos do {{c2::octaedro}} e os eixos 2 nos do {{c3::dodecaedro rômbico}}. | A lista 3A₄ 4A₃ 6A₂ 9P C, desenhada. | a07 | `oa04` |

## Navegação

[[05-miller-e-projecao-modulo|← Hub do módulo]] · [[05-miller-e-projecao-questionario-final|Questionário final]] · [[05-miller-e-projecao-auditoria|Auditoria do módulo]]

## Histórico

- 2026-10-04 — primeira geração (fb001–fb100, fc001–fc018).
- 2026-10-04 — **checagem científica do baralho, antes de fechar o módulo.** Cada card foi conferido contra a frase da aula auditada de onde vem; índices, eixos de zona e ângulos foram recalculados (os mesmos valores do registro de contas da auditoria). Resultado: 0 🔴, 0 🟠. Antes de receber ID definitivo, o rascunho foi ajustado: três pares apontados pelo `validate_flashcards.py` como quase-duplicatas ({111} × {110}; grande círculo vertical × inclinado; m∧r × r∧z do quartzo) foram reescritos com perguntas de formato distinto; um cloze sobre as formas r e z com os símbolos entre chaves foi refeito com os índices de face entre parênteses.
- 2026-10-04 — `validate_flashcards.py`: 0 erros, 0 avisos (Basic e Cloze).
