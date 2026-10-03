# Aula 06: Ordem–desordem Al/Si nos feldspatos potássicos — sanidina, ortoclásio, microclínio e o parâmetro 2t₁

**ID:** geologia-avancado-m40-a06
**Módulo:** [[40-mineralogia-dos-tectossilicatos-modulo|Módulo 40 — Mineralogia dos tectossilicatos]]
**Duração estimada:** ~30 min
**Nível:** avançado (graduação plena / pós-graduação em geologia)
**Objetivo:** entender que sanidina, ortoclásio e microclínio **não diferem em composição**, mas em onde o Al está sentado — e transformar essa ideia num número mensurável (2t₁, Δ) que registra a história térmica da rocha.

## Antes de começar, você precisa saber

- Da [[40-mineralogia-dos-tectossilicatos-aula-05-feldspatos-quimica-estrutura-e-ternario|aula 05]]: a estrutura em anéis de quatro tetraedros com sítios **T1** e **T2**, as placas (001), a posição dos cátions M e o fato de que Al:Si = 1:3 nos feldspatos alcalinos.
- Elementos de simetria: eixo binário, plano de espelho, centro de simetria; e o que significa perder um deles.
- Da [[40-mineralogia-dos-tectossilicatos-aula-02-grupo-da-silica-polimorfos-e-diagrama-p-t|aula 02]]: a distinção entre transformação deslocativa e reconstrutiva, e o conceito de metaestabilidade.
- Noções de difratometria de raios X: lei de Bragg, nλ = 2·d(hkl)·sen θ, e leitura de um difratograma I × 2θ.

## Conteúdo

### O fato estrutural que abre o problema

Volte ao anel de quatro tetraedros da aula 05. As distâncias entre a posição **M** — agora ocupada pelo K⁺ — e os diversos sítios tetraédricos **não são iguais**. Logo, os sítios T **não são estrutural nem energeticamente equivalentes**.

Isso muda tudo. Se todos os sítios fossem equivalentes, a distribuição de Al e Si seria uma questão indiferente. Como não são, a estrutura **tem preferência** — e a preferência se manifesta ou não, dependendo de quanta energia térmica há disponível para embaralhar os átomos.

### Os dois extremos

**Sanidina — desordem máxima.** No polimorfo de mais alta temperatura, de estrutura mais expandida, a distribuição de Si e Al pelas posições tetraédricas é **totalmente aleatória**: a probabilidade de que uma posição T qualquer esteja preenchida por Si ou Al é exatamente **3:1**, a mesma proporção que aparece na fórmula mínima. O retículo tem o maior grau de desordem possível.

**Microclínio máximo — ordem máxima.** No polimorfo de mais baixa temperatura, os átomos de Al são encontrados **sempre num único sítio T** — naturalmente aquele mais próximo do cátion M. É a configuração de menor energia: os cátions monovalentes ficam algo mais distantes do Si⁴⁺ e mais próximos do Al³⁺, e a distribuição de cargas na estrutura fica a mais equilibrada possível.

> [!important] A ideia central em uma frase
> Os três polimorfos de feldspato potássico têm a **mesma composição** e diferem apenas no **endereço do alumínio**. Composição é química; endereço do alumínio é **história térmica**. São duas variáveis independentes, e confundi-las inutiliza a leitura petrogenética.

### Como se mede a ordem: o parâmetro t

O guia formaliza a ideia com uma contabilidade simples. Tome como referência um **semi-anel** contendo quatro posições tetraédricas (T2O, T1m, T1O e T2m — ou o semi-anel emparelhado T2Oc, T1mc, T1Oc e T2mc). Como Si:Al = 3 nos feldspatos alcalinos, em cada conjunto de quatro posições T há, **em média, exatamente um átomo de Al**.

Chame de **t** a probabilidade de encontrar um átomo de Al numa dada posição tetraédrica. Como o semi-anel tem duas posições T1 e duas T2:

$$2t_1 + 2t_2 = 1{,}0 \qquad \text{(III.1)}$$

Para a **sanidina**, em que todas as posições são equiprováveis:

$$t_1 = t_2 = 0{,}25 \;\Longrightarrow\; 2t_1 = 2t_2 = 0{,}5 \qquad \text{(III.2)}$$

Sob condições energéticas mais brandas, a estrutura fica mais exigente quanto à ocupação dos sítios, e a otimização energética conduz ao **ordenamento**. Na primeira etapa, o Al tende a se concentrar nos sítios **T1** — é o caminho mais fácil — enquanto o Si migra preferencialmente para os **T2**, mantendo-se a simetria monoclínica original. Em termos de 2t₁:

| Polimorfo | Intervalo de 2t₁ | Simetria |
|---|---|---|
| Sanidina de alta temperatura | 0,50 ≤ 2t₁ < 0,67 | monoclínica C2/m |
| Sanidina de baixa temperatura | 0,67 ≤ 2t₁ ≤ 0,74 | monoclínica C2/m |
| Ortoclásio | 0,75 < 2t₁ ≤ 1,00 | monoclínica C2/m |

*(Os limites são convencionais; o pequeno hiato entre 0,74 e 0,75 é artefato de arredondamento da tabulação original, não uma descontinuidade física.)*

Em todos esses casos os dois sítios T1 são ocupados **igualmente** por Al, e o mesmo vale para os dois T2. A regra geral: **sempre que 2t₁ ≥ 0,50 se mantém a simetria monoclínica C2/m**. E a ocupância de Al nos T2 sai de graça a qualquer momento: 2t₂ = 1,00 − 2t₁.

### O passo que quebra a simetria

Aqui está a articulação mais fina da aula. Os dois sítios T1 **também são distintos entre si** — um deles fica mais próximo da posição M do que o outro. O mesmo vale para os dois T2. Daí a diferenciação em quatro rótulos:

- **T1O** e **T2O** — mais próximos ao sítio M;
- **T1m** e **T2m** — mais afastados.

Nos polimorfos **monoclínicos**, necessariamente t₁(O) = t₁(m) e t₂(O) = t₂(m). O Al não distingue O de m: a simetria o proíbe.

Configurações mais ordenadas, estáveis em temperaturas mais baixas, concentram o Al preferencialmente em **T1O** e **T2O**. E então acontece o seguinte:

> [!important] Por que ordenar mais obriga a mudar de sistema cristalino
> **Qualquer migração adicional de Al para T1O às expensas de T1m implica automaticamente a perda do eixo binário paralelo a b e do plano de espelho m paralelo a (010).** Resta apenas o **centro de simetria (i)**, que relaciona os anéis tetraédricos dois a dois. O feldspato passa a ter simetria menor, **triclínica**, do grupo espacial P1̄ (C1̄).
> Ou seja: a mudança de simetria **não é uma escolha adicional** — ela é a consequência aritmética inevitável de o Al preferir um dos dois sítios T1. Ordem e triclinicidade são o mesmo fenômeno visto de dois ângulos.

O **microclínio máximo** é o polimorfo em que **todo** o Al está concentrado em T1O:

$$t_1(O) = 1{,}00 \;\Longrightarrow\; t_1(m) = t_2(O) = t_2(m) = 0{,}00 \qquad \text{(III.3)}$$

E há um corolário geométrico bonito: as posições **T1O se alinham segundo a direção estrutural [110]**. Portanto, **todo o Al de um microclínio máximo está enfileirado ao longo de [110]**.

Os **microclínios intermediários** são as fases triclínicas com ordenamento superior ao do ortoclásio, mas inferior ao do microclínio máximo:

$$t_1(O) \neq t_1(m) \neq t_2(O) = t_2(m) \qquad \text{(III.4)}$$

### Por que essas transformações são lentas — e por que isso é útil

As transformações polimórficas de ordem–desordem envolvem rearranjos estruturais significativos: **rompimento de ligações químicas** (inclusive as tetraédricas Si–O e Al–O), migrações catiônicas para sítios cristaloquímicos específicos e reconstrução completa da estrutura. A energia necessária é significativa — o que faz com que fases feldspáticas **metaestáveis se preservem nas rochas com alguma frequência**.

E é justamente por serem lentas que elas registram informação. O quadro de ocorrência, considerando temperatura e gradiente de resfriamento:

| Polimorfo | Ambiente típico | Estatuto |
|---|---|---|
| **Sanidina** | rochas vulcânicas feldspáticas ácidas, intermediárias e alcalinas — alta T e resfriamento rápido, que não permite ordenamento | hoje **metaestável** |
| **Ortoclásio** | rochas subvulcânicas e de cristalização epizonal (diversas rochas graníticas e sieníticas); rochas metamórficas de grau moderado a alto | fase **primária** de T intermediária a alta |
| **Microclínios** | pegmatitos; rochas de processos diagenéticos e metamórficos de baixo a médio grau | fases **primárias** de T mais baixa |

Mas o quadro tem exceções instrutivas. Fatores **cinéticos e composicionais**, com destaque para a presença de **voláteis**, também governam qual polimorfo cristaliza — e a variedade **adulária** cristaliza com simetria **monoclínica** sob temperaturas relativamente baixas (cerca de 250–350 °C) em diversos veios epitermais. Um feldspato monoclínico não é, portanto, prova de alta temperatura.

### O caminho mais comum: ordenar durante o resfriamento

Em rochas intrusivas e metamórficas formadas em profundidades médias a elevadas — mesozonais a catazonais, como a maioria das rochas graníticas de embasamento —, o feldspato alcalino cristaliza, em boa parte dos casos, como uma **solução sólida das séries sanidina ou ortoclásio–albita**. O resfriamento mais lento, auxiliado pela atuação de fluidos (frações residuais da própria cristalização magmática, mas também partes incorporadas das encaixantes), facilita o ordenamento estrutural e a passagem para **microclínio**.

E aqui a aula 06 encontra a aula 08: a típica **geminação em grade** (ou *tartan*), caracterizada pela combinação **interpenetrada** das geminações da Albita e do Periclínio, observada em microclínios de rochas ígneas, é **consequência natural do processo de inversão de simetria ocasionado pelo ordenamento do Al**. A sua observação indica inequivocamente que processos de ordenamento fizeram parte da história evolutiva daquele feldspato.

Dois avisos completam o quadro, e ambos são operacionais:

1. **Os processos são progressivos e heterogêneos.** Iniciam-se em domínios cristalinos submicroscópicos e não ocorrem com a mesma desenvoltura nos diferentes cristais de uma rocha, nem em diferentes zonas do mesmo cristal. É frequente encontrar microclínios com graus de ordenamento diferenciados, e mesmo domínios ainda não transformados que preservam ortoclásio em escala microscópica e submicroscópica. **Esses casos só se resolvem por difratometria de raios X ou microscopia eletrônica de transmissão.**
2. **Nem todo granito ordena.** Rochas ígneas cristalizadas rapidamente em condições rasas ou subsuperficiais — diversos granitos e a maioria dos sienitos supersaturados e insaturados em SiO₂ —, relativamente jovens e anidras, podem preservar o **ortoclásio**.

### Medindo o estado estrutural por raios X

Como as diferenças estão em escala submicroscópica, a difratometria é o instrumento próprio. O princípio é direto:

**Feldspatos monoclínicos apresentam os picos (130) e (131). Nas fases triclínicas esses picos aparecem duplicados**, em (130)/(1̄30) e (131)/(1̄31), porque a perda do eixo binário e do espelho torna não equivalentes planos que antes eram simétricos. O afastamento relativo entre os picos do par é, portanto, uma medida direta de quanto o retículo se afastou da simetria monoclínica.

Isso se formaliza no **grau de triclinicidade Δ** (Goldsmith & Laves, 1954):

$$\Delta = 12{,}5 \times \left( d_{131} - d_{1\bar{3}1} \right), \qquad 0 \leq \Delta \leq 1$$

com as distâncias interplanares calculadas a partir dos respectivos 2θ pela lei de Bragg. **Feldspatos monoclínicos dão Δ = 0; o microclínio máximo dá Δ = 1.** Para determinações expeditas basta obter o difratograma no intervalo estreito de **29° a 31° em 2θ (radiação CuKα)** e analisar a distribuição dos picos.

Procedimentos mais sofisticados permitem calcular diretamente as probabilidades t a partir dos parâmetros a₀, b₀, c₀, α, β e γ da cela unitária refinada — mais preciso, e bem mais trabalhoso.

Um bônus do mesmo difratograma: a **posição do pico (2̄01)** varia sistematicamente com a composição e permite determinar o teor de Or de soluções sólidas homogêneas de alta temperatura. E, quando aparecem **dois** picos (2̄01) num feldspato que quimicamente parece homogêneo, isso identifica positivamente uma **criptopertita** — duas fases exsolvidas em escala submicroscópica, tema da aula 07.

## Exemplo trabalhado

**Situação:** duas amostras de granito. Na amostra A, o feldspato potássico mostra geminação em grade nítida em quase todos os grãos; DRX dá Δ = 0,92. Na amostra B, nenhum grão mostra grade; DRX dá Δ = 0,05, e o difratograma exibe **dois** picos (2̄01). As duas amostras têm feldspato de mesma composição global, Or₈₅Ab₁₅. O que cada uma registra?

**Raciocínio.**

**Amostra A.** Δ = 0,92 é próximo do máximo: o Al está quase todo em T1O, alinhado ao longo de [110]. Trata-se de microclínio de ordenamento elevado, e a geminação em grade proeminente em número significativo de grãos confirma. Leitura: cristalização como solução sólida monoclínica em temperatura alta, seguida de **resfriamento lento**, muito provavelmente com participação de fluidos, permitindo que o ordenamento se completasse. Ambiente mesozonal a catazonal.

**Amostra B.** Δ = 0,05 indica simetria essencialmente monoclínica — Al ainda repartido igualmente entre T1O e T1m. Não é microclínio: é ortoclásio (ou sanidina) preservado. Mas atenção ao segundo dado: **dois picos (2̄01)** revelam que a amostra, embora com composição global Or₈₅Ab₁₅, não é uma fase única — ela já se separou em duas, uma potássica e outra albítica, em escala submicroscópica. É uma **criptopertita**. Leitura: resfriamento rápido, em nível raso e provavelmente anidro. Houve energia e tempo suficientes para a **exsolução** (que é migração de cátions M nas cavidades) começar, mas não para o **ordenamento** (que exige romper ligações Si–O e Al–O no arcabouço).

**A lição — e ela é a mais importante do módulo:** composição idêntica, histórias térmicas opostas. Dois feldspatos Or₈₅Ab₁₅ podem ser microclínio máximo ou criptopertita ortoclásica, e **só o estado estrutural distingue**. Note também a hierarquia de custos energéticos: a exsolução avança antes do ordenamento, porque mover K e Na pelas cavidades é mais barato do que rearranjar o arcabouço tetraédrico.

## Erros comuns

- **Ler "sanidina, ortoclásio, microclínio" como uma série composicional.** É uma série **estrutural**. A composição pode ser rigorosamente a mesma nos três.
- **Achar que 2t₁ é um teor.** É uma **probabilidade de ocupação** de um sítio, entre 0 e 1, não uma fração de massa nem uma proporção catiônica.
- **Concluir "não vi grade ⇒ é ortoclásio".** Falso, e é o erro clássico do grupo. A ausência de grade pode significar corte inadequado, ordenamento incipiente em domínios submicroscópicos, ou ortoclásio de fato. O guia é explícito: nesses casos, refira-se apenas como "feldspato potássico" e resolva por DRX ou MET.
- **Concluir "monoclínico ⇒ alta temperatura".** A adulária cristaliza monoclínica a 250–350 °C. A regra T ↔ simetria vale como tendência, não como lei.
- **Supor que ordem e desordem se distribuem homogeneamente num cristal.** Não se distribuem: os processos começam em domínios submicroscópicos e podem coexistir graus distintos no mesmo grão.
- **Confundir Δ com 2t₁.** São duas métricas do mesmo fenômeno, com definições e escalas diferentes: Δ é lido diretamente do difratograma; 2t₁ exige refinamento da cela.

## O que não concluir

- **Que a geminação em grade mede o grau de ordenamento.** Ela **atesta** que houve inversão de simetria por ordenamento; a quantificação vem da DRX. Grade proeminente em número significativo de grãos permite **inferir** que o microclínio máximo, ou de ordenamento elevado, é a fase majoritária — inferência, não medida.
- **Que Δ = 1 significa "resfriamento lentíssimo".** Significa ordenamento completo, que também depende de fluidos, de composição e de tempo geológico total, não só da taxa de resfriamento.
- **Que ortoclásio preservado num granito prova idade jovem.** Prova cinética desfavorável ao ordenamento — resfriamento rápido, nível raso, ambiente anidro. Juventude é uma correlação frequente, não a causa.
- **Que a exsolução e o ordenamento são processos independentes.** Como a aula 07 detalha, o rearranjo estrutural provocado pela exsolução **colabora** com o ordenamento do Al, e vice-versa; na prática eles ocorrem de forma mais ou menos simultânea.

## Recap relâmpago

- Os sítios T **não são equivalentes**: as distâncias até M variam ⇒ a estrutura tem preferência de onde pôr o Al.
- **Sanidina = desordem máxima** (Al e Si aleatórios, 3:1). **Microclínio máximo = ordem máxima** (todo o Al no sítio mais próximo de M).
- **2t₁ + 2t₂ = 1,0.** Sanidina: t₁ = t₂ = 0,25 ⇒ 2t₁ = 0,5. **Sanidina alta 0,50–0,67 · sanidina baixa 0,67–0,74 · ortoclásio 0,75–1,00**, todas **monoclínicas C2/m** (regra: 2t₁ ≥ 0,50 ⇒ monoclínico). 2t₂ = 1 − 2t₁.
- Os T1 se subdividem em **T1O** (perto de M) e **T1m**. Nos monoclínicos t₁(O) = t₁(m). **Migrar Al de T1m para T1O destrói o eixo binário ‖ b e o espelho ‖ (010) ⇒ triclínico C1̄.**
- **Microclínio máximo: t₁(O) = 1,00**, todo o Al alinhado segundo **[110]**. Intermediários: t₁(O) ≠ t₁(m) ≠ t₂(O) = t₂(m).
- Transformações **rompem ligações Si–O e Al–O** ⇒ lentas, com energia alta ⇒ **metaestabilidade comum**.
- **Sanidina** ⇒ vulcânicas resfriadas rápido (metaestável). **Ortoclásio** ⇒ subvulcânicas/epizonais e metamórficas de grau moderado a alto. **Microclínio** ⇒ pegmatitos, diagênese, metamorfismo baixo a médio. **Exceção: adulária, monoclínica a 250–350 °C.**
- **DRX:** monoclínico dá (130) e (131); triclínico **duplica** em (130)/(1̄30) e (131)/(1̄31). **Δ = 12,5 × (d₁₃₁ − d₁̄₃₁)**, de 0 (monoclínico) a 1 (microclínio máximo); intervalo expedito **29°–31° 2θ CuKα**. Pico **(2̄01)** dá composição; **dois** picos (2̄01) ⇒ criptopertita.

## Próxima aula

[[40-mineralogia-dos-tectossilicatos-aula-07-solvus-e-exsolucao-pertitas|Aula 07 — Solvus e exsolução nos feldspatos alcalinos: pertitas, antipertitas, mesopertitas e criptopertitas]]

## Anterior

[[40-mineralogia-dos-tectossilicatos-aula-05-feldspatos-quimica-estrutura-e-ternario|Aula 05 — Feldspatos: química, estrutura e ternário]]

## Fontes

- Não equivalência dos sítios T, desordem da sanidina, ordem do microclínio máximo, equações III.1 a III.4, intervalos de 2t₁ dos polimorfos, diferenciação T1O/T1m/T2O/T2m, perda de simetria e passagem a triclínico, alinhamento do Al segundo [110], ocorrências, exceção da adulária, geminação em grade como consequência do ordenamento, heterogeneidade dos domínios: Vlach, S. R. F., *A Classe dos Tectossilicatos: Guia Geral da Teoria e Exercício*, IGc-USP, Série Didática USP, item III.3 e Figura 9.
- Esquemas estruturais e migração de Al/Si entre sítios (Figura 9 do guia): Laves, F. (1960), in Ribbe, P. H. (1975), *Feldspar Mineralogy*, MSA Short Course Notes v. 2.
- Estabilidade e evolução do estado estrutural em função da temperatura e do gradiente de resfriamento (Figura 6, direita): Putnis, A. & McConnell, J. D. C. (1980), *Principles of Mineral Behavior*, Blackwell.
- Grau de triclinicidade Δ, duplicação dos picos (130) e (131), uso do pico (2̄01) e padrões de difração de feldspatos alcalinos (Figuras 22 e 23 do guia): Goldsmith, J. R. & Laves, F. (1954), *The microcline–sanidine stability relations*, Geochimica et Cosmochimica Acta, v. 5, p. 1–19, e Ribbe, P. H. (1975), *Feldspar Mineralogy*, MSA Short Course Notes v. 2, conforme item IX.4 do guia. **Nota de auditoria:** o guia grafa "Goldschmidt & Laves"; a autoria correta do índice de triclinicidade é de **J. R. Goldsmith** e **F. Laves** — não de V. M. Goldschmidt, o geoquímico cuja *regra das fases mineralógicas* aparece, corretamente atribuída, na aula 14.
- **Correção de notação aplicada nesta aula:** o grupo espacial dos feldspatos potássicos monoclínicos é **C2/m**; a grafia "P2/m (C2/m)" que aparece no item III.3 do guia é lapso tipográfico. Ver achado `TECTO-M40-A06-GRUPO-ESPACIAL-005` no [[40-mineralogia-dos-tectossilicatos-auditoria|relatório de auditoria]].

<!--
nivel: avancado
palavras_corpo: ~2140

mapa_objetivo_secao:
  geologia-avancado-m40-oa03: "O fato estrutural que abre o problema" + "Os dois extremos" + "Como se mede a ordem: o parâmetro t" + "O passo que quebra a simetria" + "Por que essas transformações são lentas — e por que isso é útil" + "O caminho mais comum: ordenar durante o resfriamento" + "Medindo o estado estrutural por raios X" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: TECTO-M40-A06-SITIOS-001
    claim: "As distancias entre a posicao M ocupada pelo K+ e os diversos sitios tetraedricos T1 e T2 sao variaveis, de modo que esses sitios nao sao estrutural nem energeticamente equivalentes; na sanidina a distribuicao de Si e Al e totalmente aleatoria na proporcao 3:1 e no microclinio maximo todo o Al ocupa o sitio T mais proximo do cation M."
    risk: fato
    source: "Vlach, Guia dos Tectossilicatos, item III.3 e Figura 9"
  - claim_id: TECTO-M40-A06-EQUACOES-002
    claim: "Para um semi-anel de quatro posicoes tetraedricas vale 2t1 + 2t2 = 1,0; na sanidina t1 = t2 = 0,25 e portanto 2t1 = 2t2 = 0,5; no microclinio maximo t1(O) = 1,00 e t1(m) = t2(O) = t2(m) = 0,00; nos microclinios intermediarios t1(O) diferente de t1(m) diferente de t2(O) = t2(m); e 2t2 = 1,00 - 2t1."
    risk: fato
    source: "Vlach, Guia dos Tectossilicatos, item III.3, equacoes III.1 a III.4"
  - claim_id: TECTO-M40-A06-INTERVALOS-003
    claim: "Os intervalos convencionais de 2t1 sao: sanidina de alta temperatura 0,50 <= 2t1 < 0,67; sanidina de baixa temperatura 0,67 <= 2t1 <= 0,74; ortoclasio 0,75 < 2t1 <= 1,00; e sempre que 2t1 >= 0,50 a simetria e monoclinica."
    risk: numero
    source: "Vlach, Guia dos Tectossilicatos, item III.3"
  - claim_id: TECTO-M40-A06-SIMETRIA-004
    claim: "Qualquer migracao adicional de Al para T1O as expensas de T1m implica a perda do eixo binario paralelo ao eixo b e do plano de simetria m paralelo a (010), restando apenas o centro de simetria, o que leva a simetria triclinica P-1 (C-1); as posicoes T1O se alinham segundo a direcao estrutural [110]."
    risk: fato
    source: "Vlach, Guia dos Tectossilicatos, item III.3 e Figura 9"
  - claim_id: TECTO-M40-A06-GRUPO-ESPACIAL-005
    claim: "O grupo espacial dos feldspatos potassicos monoclinicos (sanidina e ortoclasio) e C2/m."
    risk: fato
    source: "DHZ 1992; Ribbe 1975 — CORRIGE a grafia 'P2/m (C2/m)' do item III.3 do guia, que e lapso tipografico"
  - claim_id: TECTO-M40-A06-OCORRENCIA-006
    claim: "Sanidina ocorre em rochas vulcanicas feldspaticas acidas, intermediarias e alcalinas rapidamente resfriadas, hoje como fase metaestavel; ortoclasio e fase primaria de temperaturas intermediarias a altas em rochas subvulcanicas e epizonais e em metamorficas de grau moderado a alto; microclinios sao fases primarias em pegmatitos e em rochas de processos diageneticos e metamorficos de baixo a medio grau."
    risk: fato
    source: "Vlach, Guia dos Tectossilicatos, item III.3 e Figura 6"
  - claim_id: TECTO-M40-A06-ADULARIA-007
    claim: "A variedade adularia cristaliza com simetria monoclinica sob temperaturas relativamente baixas, de cerca de 250 a 350 graus Celsius, em diversos veios epitermais."
    risk: numero
    source: "Vlach, Guia dos Tectossilicatos, item III.3"
  - claim_id: TECTO-M40-A06-GRADE-008
    claim: "A geminacao em grade ou tartan, combinacao interpenetrada das geminacoes da Albita e do Periclinio observada em microclinios, e consequencia natural da inversao de simetria ocasionada pelo ordenamento do Al, e a sua observacao indica inequivocamente que processos de ordenamento fizeram parte da historia daquele feldspato."
    risk: fato
    source: "Vlach, Guia dos Tectossilicatos, itens III.3 e III.5"
  - claim_id: TECTO-M40-A06-TRICLINICIDADE-009
    claim: "O grau de triclinicidade e definido por Delta = 12,5 x (d131 - d1-31), com 0 <= Delta <= 1; feldspatos monoclinicos apresentam Delta = 0 e o microclinio maximo Delta = 1; para determinacoes expeditas basta o difratograma entre 29 e 31 graus 2theta para radiacao CuKalfa."
    risk: numero
    source: "Vlach, Guia dos Tectossilicatos, item IX.4; Goldsmith, J. R. & Laves, F. (1954), Geochim. Cosmochim. Acta 5:1-19, in Ribbe (1975) — CORRIGE a grafia 'Goldschmidt & Laves' do guia"
  - claim_id: TECTO-M40-A06-DRX-PICOS-010
    claim: "Feldspatos monoclinicos apresentam picos (130) e (131) que aparecem duplicados em (130)/(1-30) e (131)/(1-31) nas fases triclinicas; a posicao do pico (2-01) permite determinar a composicao de solucoes solidas homogeneas de alta temperatura e a presenca de dois picos (2-01) identifica positivamente criptopertitas."
    risk: fato
    source: "Vlach, Guia dos Tectossilicatos, item IX.4 e Figura 22; Ribbe (1975)"
-->
