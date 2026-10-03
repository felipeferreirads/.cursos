# Auditoria científica — Módulo 17: Geofísica marinha e de bacias sedimentares

**Data:** 2026-09-10
**Modo:** `audit-and-fix` (correções aplicadas cirurgicamente no texto)
**Escopo:** as 5 aulas do módulo, em conjunto, mais o hub do módulo
**Veredito:** **aprovado** — 0 achados vermelhos em aberto, 0 achados laranjas em aberto. Gate liberado para questionário e flashcards.

## Contagem por severidade

| Severidade | Contagem | Situação |
|---|---|---|
| 🔴 Vermelho (afirmação factualmente falsa) | **1** | corrigido |
| 🟠 Laranja (impreciso, certeza indevida, inconsistência interna) | **4** | corrigidos |
| 🟡 Amarelo (atribuição errada de fonte, citação defeituosa, valor fora do que a própria equação devolve, versão desatualizada) | **8** | corrigidos |
| 🔵 Azul (verificado e correto — registro de que foi checado) | **9** | sem alteração |
| ⚪ Branco (questão genuinamente aberta na literatura) | **1** | mantida, agora apresentada como controvérsia real |

**Alegações rastreadas:** as 18 `alegacoes_auditaveis` declaradas pelas aulas (3 na a01, 3 na a02, 4 na a03, 6 na a04, 4 na a05) foram reverificadas uma a uma; a auditoria levantou mais 6 fora da lista do autor, chegando a 24 alegações rastreadas.

**Aritmética:** os três exemplos trabalhados numéricos foram recalculados. Todos fecham.
- a03: 1.500 m/s × (2,80 s ÷ 2) = 2.100 m ✔; múltipla em 2 × 2,80 = 5,60 s ✔.
- a04 (correção de Eötvös, verificada por derivação da fórmula): 7,5038 × cos 45° = **5,31** mGal/nó — a aula dizia 5,4 (achado A04-Y2).
- a04 (GDH1, verificado contra as equações da fonte primária): 48 + 96·e^(−0,0278×60) = **66,1 mW/m²** — a aula dizia 60-65 (achado A04-Y4).
- a05: sincronismo trapa (100 Ma) antes de geração (90 Ma) ✔.

## Padrão dominante

**ATRIBUIÇÃO DE FONTE — o dado certo debaixo do nome errado.** Quatro dos treze achados corrigíveis têm exatamente esta forma: o número está correto, a conclusão está correta, e o artigo creditado não é o que produziu aquele número.

1. As duas idades U-Pb do Evaporito Retiro (119,2 ± 1,6 e 119,18 ± 0,79 Ma) creditadas a **Tedeschi et al. (2017)**, que é um artigo de quimioestratigrafia de δ¹³C e **não reporta U-Pb**. As idades são de **Alkmim et al. (2024)** (achado A02-R1, o único vermelho).
2. As médias cratônicas 41/48 mW/m² creditadas a **Pollack, Hurter & Johnson (1993)**; são de **Nyblade & Pollack (1993)** (A04-Y1).
3. Uma entrada de bibliografia colada, fundindo uma referência espúria ("Kaminski, M. A. et al.") com a real (Sloan & Koh 2008) (A05-Y1).
4. **Milani & Zalán (1999)**, que trata das bacias paleozoicas **de interior** da América do Sul, creditado como panorama das bacias **marginais** brasileiras (A01-Y1).

Por que isso é caro **neste** módulo: as aulas 01, 02 e 05 se apoiam em literatura brasileira específica, quase toda fora de bases indexadas em inglês, e é justamente onde o leitor autodidata mais depende da referência para ir verificar. Uma atribuição errada não faz o aluno aprender um fato errado — faz com que, ao tentar conferir, ele não encontre nada, e conclua que o material inventou o dado. Num módulo cujo objetivo declarado é ensinar a integrar evidência de fontes independentes, é o defeito mais destoante possível.

**Padrão secundário: ESCOPO DE UMA IDADE OU DE UM BLOCO.** Dois laranjas (A02-O1, A01-O2) aplicam a um recorte estreito um número que vale para um recorte largo: "Neocomiano" do sistema de riftes inteiro aplicado ao segmento Santos-Campos-ES, e quatro concessões de Sergipe-Alagoas colapsadas numa só.

**Onde o módulo está limpo:** toda a física de propagação, aquisição e múltiplas da a03; a geometria do *rollover* e do arrasto reverso na a01 (ponto de risco declarado, verificado contra a literatura primária e **correto**); o par ar-livre/Bouguer da a04 e sua tabela; as anomalias magnéticas lineares e Vine & Matthews; os quatro elementos do sistema petrolífero e o requisito de sincronismo da a05; e a arquitetura pré-sal/pós-sal da margem.

---

## Achado vermelho

### 🔴 AUD-M17-A02-TEDESCHI-001 — Idades U-Pb do Evaporito Retiro atribuídas ao artigo errado
**Aula 02, quadro "Controvérsia em aberto — a idade do sal aptiano", corpo, lista de Fontes e alegação SAL-002.**
**Tipo:** erro factual (atribuição de dado a fonte que não o produziu).

**Estava escrito:** *"as datações radiométricas diretas mais citadas são as de **Tedeschi et al. (2017)**, que dataram por U-Pb lâminas de calcita em anidrita nodular do Evaporito Retiro (Bacia de Campos) e obtiveram **119,2 ± 1,6 Ma** e **119,18 ± 0,79 Ma**"*.

**Problema:** as duas idades existem e estão corretas, mas não são de Tedeschi et al. (2017). Aquele artigo — *Geology* 45(6), 543-546 — é um trabalho de **quimioestratigrafia de δ¹³C**, que correlaciona o fim da deposição evaporítica ao OAE 1a; não reporta datação U-Pb nenhuma. As duas determinações em lâminas de calcita de anidrita nodular da porção inferior do Evaporito Retiro são de **Alkmim, F. F. et al. (2024)**, *"U-Pb ages of pre- to post-salt carbonates, Santos and Campos basins, SE Brazil: implications for the evolution of the South Atlantic"*, *Marine and Petroleum Geology* — um estudo de 30 determinações U-Pb LA-ICP-MS, no qual as duas idades do Retiro são explicitamente interpretadas como a melhor aproximação do momento de deposição do sal.

**Correção aplicada:** as duas fontes foram separadas e cada dado devolvido a quem o produziu — Tedeschi et al. (2017) fica com a correlação δ¹³C/OAE 1a, Alkmim et al. (2024) com as idades U-Pb. Alkmim et al. (2024) acrescentado à lista de Fontes; a entrada de Tedeschi ganhou a ressalva explícita "o artigo **não** traz datações U-Pb", para que a confusão não se refaça.

**Fonte:** ScienceDirect S026481722400504X (Alkmim et al., *Marine and Petroleum Geology*, nov/2024, que traz a frase "*Two determinations carried out in calcite laminae of a nodular anhydrite sample extracted from the lower portion of the Retiro Evaporite (Campos Basin) returned the ages of 119.2 ± 1.6 Ma and 119.18 ± 0.79 Ma*"); GeoScienceWorld, *Geology* 45(6), 543-546 (resumo de Tedeschi et al. 2017, integralmente sobre δ¹³C). **Nível:** revisada por pares. **Confiança:** confirmado.

---

## Achados laranjas (todos corrigidos)

### 🟠 AUD-M17-A02-SALCONTROVERSIA-003 — Controvérsia real reduzida a uma disputa sobre duração
**Aula 02, quadro da idade do sal, recap e alegação SAL-002.**
**Tipo:** certeza indevida.

**Estava escrito:** *"Somando as duas coisas, a deposição do sal cai no Aptiano inferior a médio, grosso modo entre ~122 e ~116 Ma. O que permanece genuinamente em disputa é a **duração** da deposição (…) e a **correlação entre bacias**."*

**Problema:** a afirmação sobre o estado da literatura é falsa. O que está em disputa é, antes de tudo, a **posição do sal dentro do Aptiano**, e a divisão é substantiva: um campo o coloca no Aptiano inferior (δ¹³C correlacionado ao OAE 1a, Tedeschi et al. 2017; U-Pb ~119 Ma, Alkmim et al. 2024; bioestratigrafia de foraminíferos da seção sobreposta), outro perto do limite Aptiano-Albiano ou acima dele (paleomagnetismo e Ar-Ar, com destaque para 110,64 ± 0,3 Ma em silvinita de Sergipe, defendido por Szatmari et al. 2021, que descrevem o problema como "desacordo marcado" entre métodos). Há inclusive um capítulo de monografia da AGU de 2025 intitulado *The South Atlantic **Late** Aptian Evaporites*. Apresentar o Aptiano inferior como questão resolvida é escolher um lado numa disputa aberta — exatamente o que o material não deve fazer.

**Por que laranja e não branco:** o texto já vinha rotulado como "controvérsia em aberto", mas o conteúdo do quadro **negava** a controvérsia principal e declarava resolvido o que não está. A etiqueta certa sobre um conteúdo errado é pior que nenhuma etiqueta.

**Correção aplicada:** o quadro foi reescrito expondo os dois campos com suas evidências, sem escolher um. Acrescentada a observação de que a moldura "radiométrico × bioestratigráfico" de Szatmari et al. já não separa os campos de forma limpa, porque o U-Pb de Alkmim et al. é ele próprio radiométrico e cai no campo oposto — a divergência hoje é tanto **entre métodos radiométricos diferentes** (U-Pb em calcita × Ar-Ar em silvinita) quanto entre radiometria e bioestratigrafia. Mantidos os pontos de consenso: deposição muito rápida (estimativas de 400-600 ka) e correlação entre bacias em aberto. Recap ampliado com o mesmo aviso.

**Confiança:** confirmado quanto à existência dos dois campos; a disputa em si permanece ⚪ (ver abaixo).

### 🟠 AUD-M17-A02-RIFTEIDADE-002 — Idade de abertura do rifte do segmento central puxada ~9 Ma para trás
**Aula 02, Estágio 2, exemplo trabalhado, recap e alegação ESTAGIOS-001.**
**Tipo:** confusão de escopo.

**Estava escrito:** *"para o segmento central da margem brasileira (Santos-Campos-Espírito Santo), a fase rifte se desenvolve principalmente durante o **Neocomiano ao Barremiano** (grosso modo entre ~143 e 121 Ma…)"*.

**Problema:** "Neocomiano ao Barremiano" é a formulação de Chang et al. (1992) para o *East Brazil Rift System* **como um todo**. Convertida em número, ela puxa o início para a base do Cretáceo, ~143 Ma — o que é defensável para os segmentos interiores e nordestinos (Recôncavo-Tucano-Jatobá, Sergipe-Alagoas), onde o registro sin-rifte começa mesmo no Berriasiano-Valanginiano, mas **não** para o segmento central, que a frase declara estar descrevendo. Ali a fase rifte abre com os basaltos da Formação Camboriú no **Hauteriviano**, em torno de **134 Ma**, contemporâneos do magmatismo Paraná-Etendeka, e o preenchimento sedimentar sin-rifte propriamente dito (Formações Piçarras e Itapema) é **Barremiano a Aptiano basal**. A aula errava por ~9 Ma justamente no segmento que escolheu como foco — e o fazia numa aula que, três seções adiante, ensina que o rifteamento é **diácrono**, contradizendo a si mesma.

**Correção aplicada:** o parágrafo foi reescrito distinguindo explicitamente as duas escalas: o "Neocomiano" de Chang et al. para o sistema inteiro, e ~134-121 Ma para Santos-Campos-ES, com as unidades nomeadas. O erro virou material didático — a distinção agora reforça a diacronia em vez de contradizê-la. Propagado para o exemplo trabalhado, para o recap (que ganhou um bullet próprio sobre idades) e para a alegação. Acrescentada também a observação de que "Neocomiano" é termo informal, sem status na carta da ICS.

**Fonte:** literatura estratigráfica da Bacia de Santos (Fm. Camboriú hauteriviana, ~134-130 Ma; Piçarras barremiana; Itapema Barremiano superior-Aptiano basal); Chang et al. (1992), *Tectonophysics* 213. **Confiança:** confirmado.

### 🟠 AUD-M17-A04-EOTVOSORDEM-004 — Ordem de grandeza contradizendo os próprios números da frase seguinte
**Aula 04, gravimetria marinha, e recap.**
**Tipo:** inconsistência interna.

**Estava escrito:** *"a correção de Eötvös é **uma ordem de grandeza** maior no ar do que no mar. Num navio, ela vale cerca de 5,4 mGal por nó (…) algumas **dezenas** de mGal a 5-10 nós (…). Numa aeronave a algumas centenas de nós, o mesmo efeito pode ultrapassar **1 Gal (mais de 1.000 mGal)**."*

**Problema:** os próprios números dados dizem outra coisa. Dezenas de mGal contra mais de 1.000 mGal é um fator da ordem de **30 vezes**, ou seja, uma a duas ordens de grandeza — e o leitor que fizer a conta vai encontrar a contradição dentro do mesmo parágrafo. O bloco de alegações da aula, curiosamente, já trazia a formulação certa ("falso por uma a duas ordens de grandeza"); o corpo não tinha sido acertado.

**Por que laranja e não amarelo:** "quantas ordens de grandeza" é exatamente o tipo de coisa que vira flashcard e questão de múltipla escolha, e o material derivado herdaria a versão errada do corpo, não a certa do metadado.

**Correção aplicada:** corpo e recap passaram a dizer "uma a duas ordens de grandeza", com o fator ~30 explicitado. A fórmula padrão *E* = 7,5038 · *V*(nós) · cos φ · sen α (+ 0,004154 · *V*²) foi acrescentada ao corpo, de modo que o número deixa de ser memorizado e passa a ser derivável. **O sentido do efeito foi reverificado e está correto:** leste soma-se à rotação e reduz a gravidade medida (correção positiva a somar de volta); o sinal não depende do hemisfério, só a magnitude escala com cos φ.

**Fonte:** Telford, Geldart & Sheriff (1990), cap. 2; constante conferida contra a implementação de referência do GMT (`mgd77list`: `7.5038*V*cos(lat)*sin(az) + 0.004154*V²`) e contra a entrada "Eötvös effect" do SEG Wiki; Harlan (1968), *JGR* 73(14), 4675-4679. **Confiança:** confirmado.

### 🟠 AUD-M17-A01-SEALBLOCOS-005 — Seis descobertas de Sergipe-Alagoas colapsadas num só bloco
**Aula 01, panorama das bacias marginais, e alegação BACIAS-BR-003.**
**Tipo:** impreciso.

**Estava escrito:** *"Barra, Farfan, Moita Bonita, Muriú, Poço Verde e Cumbe, **várias delas no bloco BM-SEAL-11**"*.

**Problema:** o polo de águas profundas de Sergipe abrange **quatro** concessões — BM-SEAL-4 e BM-SEAL-11 (em parceria) e BM-SEAL-4A e BM-SEAL-10 (100% Petrobras). Poço Verde está em BM-SEAL-4; o escoamento de gás de Farfan, Barra e Muriú se dá pelos blocos BM-SEAL-10 e BM-SEAL-11. Concentrar tudo em BM-SEAL-11 é o mesmo tipo de erro que a auditoria anterior desta aula já havia corrigido uma vez (a redação original citava "Pau-Brasil/BM-SEAL-11", sendo Pau-Brasil um bloco do pré-sal da Bacia de **Santos**): a menção a BM-SEAL-11 sobreviveu à primeira correção sem ser reverificada.

**Correção aplicada:** substituído por "distribuídas pelas concessões BM-SEAL-4, BM-SEAL-4A, BM-SEAL-10 e BM-SEAL-11, e não por um bloco só". Alegação atualizada com o detalhamento por bloco.

**Fonte:** comunicados Petrobras sobre o polo de Sergipe águas profundas e sobre o gasoduto de escoamento; formulários 6-K da Petrobras de 2014 (Poço Verde/BM-SEAL-4). **Confiança:** confirmado.

---

## Achados amarelos (todos corrigidos)

| ID | Aula | Achado | Correção |
|---|---|---|---|
| A01-Y1 | a01 | Milani & Zalán (1999), sobre bacias paleozoicas **de interior**, citado como panorama das bacias **marginais** brasileiras | entrada reescrita: passa a servir de contraponto à categoria **intracratônica**, com remissão a Mohriak et al. (2008) e ANP para as marginais |
| A02-Y1 | a02 | Tedeschi et al. (2017) paginado como *Geology* 45(6), **543-549** na lista de Fontes, enquanto o bloco de alegações da mesma aula dizia 543-546 | corrigido para **543-546**, que é o correto |
| A02-Y2 | a02 | Carta ICS citada como **v2023/09** em cinco pontos; a vigente é a **v2026/06** | atualizado; acrescentada a observação de que os limites do Cretáceo aqui usados (143,1 / 132,6 / 121,4 / 113,2 Ma) **não mudaram** entre as duas versões, para que ninguém refaça as contas achando que mudaram |
| A02-Y3 | a02 | Intervalo do sal declarado como "~122-116 Ma" — mas 122 Ma é **Barremiano** pela própria carta que a aula adota (base do Aptiano 121,4), contradizendo o "sag = Aptiano" da mesma seção | trocado por "deposição encerrada em torno de 120-119 Ma", que é o que as datações do campo 1 sustentam |
| A04-Y1 | a04 | Médias cratônicas 41/48 mW/m² atribuídas a Pollack, Hurter & Johnson (1993) | atribuídas a **Nyblade & Pollack (1993)**, *JGR* 98(B7), 12207-12218, acrescentado às Fontes; Pollack et al. (1993) mantido para as médias globais 65/101, que são de lá |
| A04-Y2 | a04 | "cerca de **5,4** mGal por nó a 45°" | 7,5038 × cos 45° = **5,31**; corrigido para ~5,3 e a fórmula explicitada |
| A04-Y3 | a04 | "a anomalia ar-livre (…) é praticamente **o oposto** dela em magnitude" — zero não é o oposto de +300 mGal, e o par não é simétrico | trocado por "diferem por **centenas de mGal**", que é o que a tabela imediatamente acima já mostrava |
| A04-Y4 | a04 | "~**60-65** mW/m² em crosta oceânica de ~60 Ma" fica abaixo do que a própria equação do GDH1 devolve | corrigido para **~66 mW/m²**, com a conta (48 + 96·e^(−1,668)) explicitada; as duas equações do GDH1 acrescentadas ao corpo |
| A04-Y5 | a04 | Quebra interna do GDH1 (**55 Ma**) fundida com a idade de selamento hidrotermal (**~65 Ma**) numa faixa única de "50-65 Ma" | separadas, com a origem de cada número nomeada; Stein & Stein (1994) acrescentado às Fontes |
| A04-Y6 | a04 | Patamar assintótico declarado como "da ordem de 45-50 mW/m²" | precisado para **48 mW/m²**, que é o valor no segundo ramo da equação |
| A05-Y1 | a05 | Entrada de bibliografia colada: "Kaminski, M. A. et al. **e** Sloan, E. D. & Koh, C. A. (2008)" | nome espúrio removido (Kaminski trabalha com foraminíferos, não com hidratos); Sloan & Koh (2008) confere e foi mantido |

## Achados azuis (verificados, sem alteração)

- **A01-B1 — O *rollover* e o arrasto reverso estão corretos, e este era o ponto de maior risco do módulo.** A a01 diz que as camadas do bloco do teto "rodam de volta em direção ao plano de falha, com o mergulho **aumentando** quanto mais perto dele se está", por **colapso do bloco do teto** e não por atrito, e que *rollover* **não** é diagnóstico de falha lístrica. Conferido contra a literatura primária: "*hanging wall strata with a dip that increases toward a normal fault (i.e. rollover anticline or reverse drag)*" e a ressalva de que o arrasto reverso também se forma sobre falhas planares de extensão finita em profundidade. **Confere em todos os pontos**, inclusive com o texto já corrigido do Módulo 10 (a04), verificado palavra a palavra para consistência transversal. Era aqui que uma inversão de sentido teria sido mais cara, e ela não está.
- **A01-B2 — Bacia de Santos como maior bacia marginal em área: promovido de 🔵 a confirmado.** A auditoria anterior deixara este ponto como não verificado. Confirmado: ~352 mil km² até a cota batimétrica de 3.000 m, contra ~100 mil km² de Campos — e é de fato a maior bacia sedimentar *offshore* do Brasil. Limites conferem: Alto de Cabo Frio ao norte (com Campos), Alto de Florianópolis ao sul (com Pelotas).
- **A02-B1 — Alto de Florianópolis (Santos/Pelotas) e Alto de Vitória (Campos/Espírito Santo):** ambos corretos como descritos. Propagação do rifteamento de sul para norte: correta.
- **A02-B2 — Membro Ibura, Formação Muribeca, Sergipe-Alagoas:** seção evaporítica menos espessa que a de Santos porém mineralogicamente mais variada, com silvita, carnalita e taquidrita, sustentando a lavra de potássio de Taquari-Vassouras. Correto, e a ressalva de que "o sal não está ausente fora de Santos e Campos" é acertada e vale a ênfase que recebe.
- **A03-B1 — Velocidade do som na água do mar.** Referência de 1.500 m/s e faixa oceânica de ~1.450 a 1.570 m/s: confere (NPL; DOSITS). Taxas de variação com temperatura, salinidade e pressão, coerentes. Fator de duas a três vezes em relação a rochas sedimentares consolidadas: correto.
- **A03-B2 — Aquisição marinha.** Air guns e supressão do *bubble pulse* por arranjo; tiro a intervalo de distância e não de tempo; hidrofones como sensores de **pressão** contra geofones como sensores de **velocidade de partícula**; múltiplos streamers com posicionamento acústico contínuo; cobertura CDP contínua; papel do offset mínimo e máximo. Tudo correto. Reflexão quase perfeita na interface água-ar e múltipla de fundo em ~2× o tempo primário: corretos.
- **A03-B3 — Sonar e batimetria.** Varredura lateral pela **intensidade** do retorno e não pelo tempo de trânsito; feixe único contra multifeixe; faixa (*swath*) proporcional à lâmina d'água; cobertura de 100% em levantamento moderno. Corretos.
- **A04-B1 — Correção de Bouguer marinha e o par ar-livre/Bouguer.** Contraste água-rocha 2,67 − 1,03 ≈ 1,64 g/cm³: confere. Sobre oceano profundo compensado, ar-livre ≈ 0 e Bouguer fortemente positiva; sob montanhas compensadas, o espelho. Faixa de +220 a +330 mGal conferida contra levantamentos de bacias oceânicas (valores tipicamente em torno de +300 mGal, com registros acima de +240 mGal em porções centrais de bacia): **dentro do usual**, mantida. Densidade do sal ~2,2 g/cm³ contra encaixantes 2,4-2,7, e velocidade sísmica do sal ~4.500 m/s (a05): corretas.
- **A04-B2 — Anomalias magnéticas lineares e o modelo GDH1.** Vine & Matthews (1963), *Nature* 199, 947-949: confere, e o mecanismo (magnetização remanente adquirida abaixo do ponto de Curie, faixas simétricas em relação ao eixo da dorsal) está correto. GDH1 confirmado como o modelo de referência que substituiu Parsons & Sclater (1977), com placa mais fina e mais quente em profundidade e ajuste muito melhor para litosfera >70 Ma — exatamente como a aula descreve. Equações conferidas na fonte primária.

## Achado branco (questão genuinamente aberta, mantida com ressalva)

- **A02-W1 — A idade do sal do Atlântico Sul.** Depois da correção do achado laranja A02-O1, a aula passa a expor os dois campos sem escolher lado. A disputa **permanece aberta na literatura** e não cabe à auditoria resolvê-la. Consequência operacional: **não gerar questão de gabarito fechado, nem flashcard, que fixe uma idade única para o sal aptiano.** O que é cobrável com segurança é (a) que a controvérsia existe e qual é o eixo dela, (b) que a deposição foi rápida, (c) a armadilha de escala de tempo (125 Ma era Aptiano na GTS2012 e hoje é Barremiano).

## Correções aplicadas

**Aplicadas em:** 2026-09-10

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `AUD-M17-A02-TEDESCHI-001` | 🔴 | Corrigido | aula-02 |
| `AUD-M17-A02-RIFTEIDADE-002` | 🟠 | Corrigido | aula-02 |
| `AUD-M17-A02-SALCONTROVERSIA-003` | 🟠 | Corrigido | aula-02 |
| `AUD-M17-A04-EOTVOSORDEM-004` | 🟠 | Corrigido | aula-04 |
| `AUD-M17-A01-SEALBLOCOS-005` | 🟠 | Corrigido | aula-01 |
| `AUD-M17-A02-ICSVERSAO-006` | 🟡 | Corrigido | aula-02 |
| `AUD-M17-A02-TEDESCHIPAG-007` | 🟡 | Corrigido | aula-02 |
| `AUD-M17-A04-CRATONFONTE-008` | 🟡 | Corrigido | aula-04 |
| `AUD-M17-A04-EOTVOSVALOR-009` | 🟡 | Corrigido | aula-04 |
| `AUD-M17-A04-ARLIVREOPOSTO-010` | 🟡 | Corrigido | aula-04 |
| `AUD-M17-A05-KAMINSKI-011` | 🟡 | Corrigido | aula-05 |
| `AUD-M17-A01-MILANIZALAN-012` | 🟡 | Corrigido | aula-01 |
| `AUD-M17-A04-GDH1VALOR-013` | 🟡 | Corrigido | aula-04 |
| `AUD-M17-A04-GDH1SELAMENTO-014` | 🟡 | Corrigido | aula-04 |
| `AUD-M17-A01-SANTOSAREA-013` | 🔵 | Verificado e promovido a confirmado | aula-01 (alegação) |
| `AUD-M17-A02-SALIDADE-W1` | ⚪ | Mantido como controvérsia, agora com os dois campos | aula-02 |

**Pendências:** nenhuma. Nenhum achado aguarda decisão do usuário.

## Material derivado a propagar

**Nenhum.** O módulo não tem questionário nem baralho — a auditoria rodou antes deles, como manda a cadeia. Nada a reimportar no Anki.

## Notas para quem for gerar questionário e flashcards

1. **NÃO fixar uma idade única para o sal aptiano** em gabarito fechado ou card (achado branco A02-W1). O cobrável é o eixo da controvérsia e a armadilha de escala de tempo.
2. **A armadilha de escala de tempo é a melhor questão conceitual do módulo.** "Um artigo de 2010 diz que o sal tem ~125 Ma e está 'na base do Aptiano'. Pela carta vigente, a que andar essa idade corresponde?" Resposta: **Barremiano** — porque a base do Aptiano caiu de 125,0 (GTS2012) para 121,4 Ma. Ensina que a idade numérica muda sem que a atribuição de andar mude.
3. **Rifte: cobrar o escopo, não a data.** Distrator forte, e foi o erro corrigido: "~143 Ma" como início do rifte em Santos. A resposta certa é ~134 Ma no segmento central, e ~143 Ma só vale para o sistema de riftes leste-brasileiro como um todo. Excelente dissertativa curta: *por que a mesma pergunta "quando começou o rifte?" tem duas respostas certas nesta margem?*
4. **Eötvös: cobrar o sentido e a plataforma, não decorar 5,3.** Sentido: leste **reduz** a gravidade medida, correção positiva; não depende do hemisfério. Plataforma: dezenas de mGal num navio contra mais de 1.000 numa aeronave — fator ~30. Distrator forte: "o sinal inverte no hemisfério sul".
5. **O par ar-livre/Bouguer sobre oceano profundo é o melhor par de discriminação da a04.** Ar-livre ≈ 0, Bouguer fortemente **positiva** (+220 a +330 mGal). Distrator perfeito: inverter os dois, ou dizer que a ar-livre "já se aproxima" da Bouguer — que foi um erro corrigido na auditoria anterior desta aula.
6. **GDH1: a questão boa é a das duas idades.** 55 Ma é a quebra do modelo; ~65 Ma é o selamento hidrotermal. Distrator forte: tratá-las como o mesmo número. Também dá boa questão de cálculo: aplicar 48 + 96·e^(−0,0278·t) e obter 66 mW/m² em 60 Ma.
7. ***Rollover*: cobrar o sentido do mergulho, que é o ponto inteiro da feição.** As camadas rodam **em direção** à falha e o mergulho **aumenta** perto dela; o mecanismo é colapso do bloco do teto, não atrito; e a feição **não** prova que a falha é lístrica. Os três distratores óbvios são as três negações disso. Este ponto é consistente com o Módulo 10 e pode ser cobrado sem risco de contradição transversal.
8. **A cadeia de sincronismo da a05 é a melhor questão de aplicação do módulo.** Trapa em 100 Ma, geração em 90 Ma → sincronismo satisfeito. A questão de discriminação inverte os números e pergunta o que acontece.
9. **Fluxo de calor: usar a tabela de réguas acrescentada na a04.** Cráton arqueano ~41, proterozoico ~48, média continental 65, média oceânica 101 mW/m². Boa questão: *por que a média oceânica global é mais que o dobro da cratônica?* Resposta: idade média da litosfera.
10. **Estrutura de questionário recomendada:** ver a decisão registrada no `course-state.yaml`, campo `assessment_plan` — questionário **único cumulativo**, sem parciais.
