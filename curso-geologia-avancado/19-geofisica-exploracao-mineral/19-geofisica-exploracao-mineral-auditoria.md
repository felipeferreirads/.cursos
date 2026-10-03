# Auditoria científica — Módulo 19: Geofísica aplicada na exploração mineral

**Data do levantamento:** 2026-09-13 · **Correções aplicadas em:** 2026-09-13
**Modo:** `audit-and-fix` · **Profundidade:** `full`
**Escopo:** as 6 aulas do módulo, auditadas em conjunto, mais o hub do módulo
**Veredito:** **aprovado — gate liberado.** 0 achados vermelhos e 0 laranjas em aberto; os 18 achados corrigíveis (1 vermelho, 7 laranjas, 10 amarelos) foram corrigidos cirurgicamente. **Questionário e flashcards liberados**, observadas as restrições de formato ao fim deste relatório.

## Contagem por severidade

| Severidade | Contagem | Situação |
|---|---|---|
| 🔴 Vermelho (afirmação factualmente falsa) | **1** | **corrigido** |
| 🟠 Laranja (impreciso, confusão de escopo, omissão que gera erro) | **7** | **corrigidos** |
| 🟡 Amarelo (atribuição de fonte errada, citação defeituosa, valor fora do que a fonte citada sustenta) | **10** | **corrigidos** |
| 🔵 Azul (verificado e correto — registro de que foi checado) | **28** | sem alteração (não exigem correção: são registros de verificação bem-sucedida) |
| ⚪ Branco (questão aberta na literatura apresentada como resolvida) | **0** | — |

> **Nota sobre as contagens:** os números da coluna "Contagem" são os do levantamento original e não mudam — um achado não se apaga ao ser corrigido, ele muda de situação.

**Alegações rastreadas:** as 22 `alegacoes_auditaveis` declaradas pelas aulas (3 na a01, 4 na a02, 4 na a03, 4 na a04, 4 na a05, 4 na a06 — o autor declarou 23 blocos, sendo 22 alegações distintas) foram verificadas uma a uma; a auditoria levantou mais 7 fora da lista do autor, chegando a **29 alegações rastreadas**.

**Exemplos trabalhados:** os seis foram refeitos. Nenhum pede aritmética — são exercícios de classificação, seleção de método e interpretação. **Cinco fecham. O da a02 não fechava**: sua resolução invertia qual zona de alteração de pórfiro destrói magnetita (achado 🔴 1).

---

## Padrão dominante

**ATRIBUIÇÃO DE FONTE — o dado certo debaixo do nome errado, pela terceira vez seguida.** Seis dos dez amarelos têm exatamente esta forma, e o Módulo 17 e o Módulo 18 já haviam registrado este mesmo padrão como dominante e secundário, respectivamente. A recomendação de processo escrita ao fim da auditoria do M18 — *"antes de escrever o Módulo 19, acrescentar ao gerador de aula uma verificação obrigatória de que cada entrada da lista de Fontes (a) existe com aquele autor, ano, periódico e paginação e (b) trata efetivamente do fato que a aula lhe credita"* — **não foi implementada, e o M19 reincidiu**:

1. **Hronsky & Groves (2008)** creditado a *Geochemistry: Exploration, Environment, Analysis* 8(2), 107-118. O artigo está em **Australian Journal of Earth Sciences** 55(1), 3-12 (🟡 10).
2. **Wyborn, Heinrich & Jaques (1994)** citado com o título *"essence of the essence"* no *AGSO Research Newsletter*. O trabalho verificável é **"Australian Proterozoic mineral systems: essential ingredients and mappable criteria"**, nos *Proceedings of the AusIMM Annual Conference*, Darwin, 109-115 (🟡 11).
3. **Parasnis** datado de **1997**. É de **1956**, *Geophysical Prospecting* 4(3), 249-278 (🟡 12).
4. **Minerals 12(5), 583 (2022)** creditado a *"Chen, C. et al."*. Os autores são **Prikhodko, Bagrianski, Kuzmin & Sirohey** — provável contaminação pela citação vizinha de Chen et al. (2019) (🟡 13).
5. **Carranza & Laborte (2015)**: o título citado é o do artigo de *Computers & Geosciences* 74, 60-70, mas creditado ao volume e à paginação de **outro** artigo dos mesmos autores no mesmo ano (*Ore Geology Reviews* 71, 777-787) (🟡 14).
6. **"Sun, X. & Bongajum, E. (2023) e literatura recente"** + **"ScienceDirect"** como fonte — entrada sem título e sem periódico, e uma plataforma de distribuição apresentada como fonte. Mesmo defeito estrutural de `AUD-M17-A05-KAMINSKI-011` e `AUD-M18-A03-PINTOHALLINAN-014` (🟡 15).

E a ocorrência mais cara do padrão **não** é amarela: é a 🟠 8, em que **Chen et al. (2019)** — um artigo sobre um sistema de **domínio da frequência** — é usado para sustentar que o **domínio do tempo** alcança profundidades que o da frequência não alcança. É a mesma estrutura de `AUD-M18-A03-GOTZEKRAUSE-012` (o "gravity **high**" creditado pela anomalia **negativa**) e de `AUD-M17-A02-TEDESCHI-001`: **o dado creditado ao artigo que documenta o fenômeno oposto.**

**Padrão secundário: DIREÇÃO E SENTIDO.** O único vermelho é uma inversão de polaridade — qual alteração de pórfiro **destrói** e qual **acrescenta** magnetita —, exatamente a família de defeito que dominou os Módulos 10, 17 e 18. A boa notícia relativa é que aqui houve **uma** ocorrência, não quatro; a má é que ela estava no **exemplo trabalhado**, que é de onde o gerador de questionário mais tira questão.

**Onde o módulo está limpo:** toda a física da a05 (não unicidade de campos potenciais, problema mal-posto, regularização de estrutura mínima, efeito de suavização sobre o modelo, ancoragem petrofísica, inversão 3D) — é a melhor aula do módulo e passou inteira; toda a a06 (camada de evidência, pesos de evidência, positivos raros, sobreajuste, viés de amostragem de exploração, síntese híbrida), com um único defeito de citação; a física da indução eletromagnética e a caracterização do GPR na a04; os quatro quadrantes resistividade × cargabilidade da a03, que é o melhor material de avaliação do módulo; e o paradigma de sistemas minerais e a cascata de escalas da a01.

---

## Achado vermelho (corrigido)

### 🔴 AUD-M19-A02-PORFIROMAGNETITA-001 — O exemplo trabalhado inverte qual alteração de pórfiro destrói magnetita
**Aula 02, Exemplo trabalhado (resolução, parágrafos 1 e 2); propagado para a alegação `GEOMIN-M19-A02-ZONEAMENTOPORFIRO-004`.**
**Tipo:** erro factual (inversão de sentido/polaridade).

**Está escrito:** *"O **buraco magnético central** é consistente com uma zona de **destruição de magnetita** no núcleo do sistema — regime de alteração **potássica**-fílica intensa, tipicamente ácido o suficiente para destruir a magnetita primária da rocha hospedeira"*; e, na alegação, *"a zona de alteração **potássica** central tende a produzir destruição de magnetita primária (baixo magnético)"*.

**Problema:** é o inverso do modelo estabelecido. Em sistemas pórfiro, a alteração **potássica** (biotita secundária + feldspato potássico) é tipicamente **produtora** de magnetita hidrotermal — a zona potássica interna, mineralizada, é **rica** em magnetita e responde como **alto** magnético. Quem **destrói** magnetita é o invólucro de alteração **fílica/sericítica** (quartzo-sericita-pirita), mais ácido, cuja susceptibilidade é muito baixa e cuja assinatura de campo é o **baixo** magnético, classicamente descrito como um **anel** (*donut*) em torno do alto potássico. A revisão de Clark (2014) enuncia exatamente isso: zona potássica interna magnetita-rica, envolvida por invólucro fílico destrutivo de magnetita e de susceptibilidade muito baixa.

O agravante é que a aula usa o **alto de potássio coincidente** como confirmação da leitura potássica — e o canal de K **não** discrimina as duas zonas: a sericita é uma mica potássica, de modo que a alteração fílica também produz alto de K. O aluno sai com dois erros amarrados: a polaridade magnética invertida e a crença de que o canal K sozinho identifica alteração potássica.

**Por que vermelho e não laranja:** não é imprecisão de grau, é troca de sinal, e está no exemplo trabalhado. Um questionário gerado sobre a versão anterior nasceria com gabarito invertido — foi precisamente o que custou vermelho aos Módulos 10, 17 e 18.

**Correção proposta:** relabelar o núcleo de baixo magnético como **fílico/sericítico**, registrar que a potássica **acrescenta** magnetita, explicitar que ambas dão alto de K e que é o sinal magnético que as separa, e registrar que a configuração mais ilustrada na literatura é a recíproca (alto potássico central cercado por anel fílico de baixo magnético).

**Fonte:** Clark, D. A. (2014), *"Magnetic effects of hydrothermal alteration in porphyry copper and iron-oxide copper-gold systems: A review"*, **Tectonophysics** 624-625, 46-65, DOI 10.1016/j.tecto.2013.12.011; Sillitoe, R. H. (2010), *"Porphyry Copper Systems"*, **Economic Geology** 105(1), 3-41; Dentith & Mudge (2014), já citada pela própria aula. **Nível:** revisada por pares + manual consolidado. **Confiança:** confirmado.
**Também aparece em:** corpo da seção de magnetometria (que não nomeava as zonas — recebeu o bloco de sentido), recap relâmpago (bullet de halos de magnetita) e conclusão do exemplo trabalhado.

**Correção aplicada:** o núcleo de baixo magnético passou a ser lido como **fílico/sericítico** (destrutivo de magnetita), com a ressalva explícita de que o alto de K **não** contradiz essa leitura porque a sericita é mica potássica — e de que o canal K sozinho não separa potássica de fílica, quem separa é o sinal magnético, porque as duas respondem em sentidos opostos. O anel de alto magnético passou a ser lido como núcleo potássico preservado (magnetita hidrotermal) e/ou propilítico. Acrescentado ao corpo da seção de magnetometria um bloco que fixa a **regra de sinal** (potássica acrescenta, fílica destrói, propilítica preserva ou repõe) e nomeia a inversão como o erro clássico. Propagado para o recap e para a alegação `...ZONEAMENTOPORFIRO-004`, cujo `risk` passou de `aproximacao` para `fato`. **Clark (2014)** e **Sillitoe (2010)** acrescentados às Fontes da a02.

---

## Achados laranjas (todos corrigidos)

### 🟠 AUD-M19-A02-JANELASGAMA-002 — As três janelas de energia não são as do documento que a aula cita, e ainda se tocam
**Aula 02, seção de gamaespectrometria; propagado para o recap e para a alegação `GEOMIN-M19-A02-GAMAESPECTROMETRIA-003`.**
**Tipo:** impreciso (valor fora do que a fonte citada sustenta) + implausibilidade interna.

**Está escrito:** *"K ... janela espectral tipicamente definida entre aproximadamente **1,36 e 1,60** MeV ... U ... janela entre aproximadamente **1,60 e 1,95** MeV ... Th ... janela entre aproximadamente **2,40 e 2,86** MeV"*.

**Problema:** as três estão erradas contra a própria fonte citada. As janelas padrão da IAEA (as mesmas do IAEA-TECDOC-1363 que a aula credita) são **K 1370-1570 keV**, **U 1660-1860 keV** e **Th 2410-2810 keV** — isto é, 1,37-1,57 / 1,66-1,86 / 2,41-2,81 MeV. Duas consequências: (a) as três janelas declaradas são mais largas que as reais, e a de U é quase o dobro; (b) mais grave conceitualmente, na versão da aula a janela de K **termina** em 1,60 e a de U **começa** em 1,60 — janelas contíguas. A norma faz o oposto de propósito: deixa intervalos mortos (1,57-1,66 e 1,86-2,41 MeV) justamente para limitar o vazamento de contagens entre canais, que é o problema que as correções de *stripping* depois tratam. Ensinar janelas contíguas apaga a razão de existir do *stripping*.

**Fonte:** IAEA (2003), *Guidelines for radioelement mapping using gamma ray spectrometry data*, **IAEA-TECDOC-1363** (janelas KEW/BEW/TEW). **Nível:** normativa. **Confiança:** confirmado.

**Correção aplicada:** as três janelas trocadas pelos valores da norma (1,37-1,57 / 1,66-1,86 / 2,41-2,81 MeV), com uma frase nova que nomeia os intervalos mortos entre elas e diz para que servem. Propagado para o recap e para a alegação.

### 🟠 AUD-M19-A02-DENSIDADESULFETO-004 — Faixa de densidade que exclui dois dos cinco minerais que a própria frase enumera
**Aula 02, seção de gravimetria; propagado para o recap e para a alegação `GEOMIN-M19-A02-DENSIDADES-001`.**
**Tipo:** impreciso (valor) + confusão de escopo (mineral × corpo de minério).

**Está escrito:** *"minérios maciços de sulfeto (pirita, calcopirita, pirrotita, esfalerita, **galena**) ... tipicamente ficam na faixa de **4,2 a 5,0 g/cm³**"*.

**Problema:** dos cinco minerais nomeados, **dois ficam fora da faixa declarada** — a galena tem **7,4-7,6 g/cm³**, quase 50% acima do teto, e a esfalerita **3,9-4,1 g/cm³**, abaixo do piso. Além disso, a frase confunde dois números diferentes: a densidade do **mineral puro** e a densidade do **corpo de minério**, que é sempre menor porque o corpo carrega ganga. Um corpo de sulfeto maciço real chega ao gravímetro em torno de 3,5-4,5 g/cm³, não 4,2-5,0. O contraste declarado de "1,5 a 2,5 g/cm³" é, por isso, otimista.

**Fonte:** tabela de densidades de rochas portadoras de minério do GPG (gpg.geosci.xyz): pirita/pirrotita 4,50-5,20; magnetita 4,90-5,20; hematita 4,90-5,30; **galena 7,40-7,60**; Telford, Geldart & Sheriff (1990), tabelas de densidade. **Nível:** base de referência + manual consolidado. **Confiança:** confirmado.

**Correção aplicada:** a faixa única foi substituída por âncoras mineral a mineral (pirita e pirrotita 4,5-5,2; magnetita 4,9-5,2; hematita 4,9-5,3; calcopirita ~4,2; esfalerita 3,9-4,1; **galena 7,4-7,6**), seguidas da separação explícita entre densidade de mineral e densidade do **corpo** de minério (~3,5-4,5 g/cm³ já com ganga) e do contraste recalculado (1 a 2 g/cm³). Propagado para o recap e para a alegação.

### 🟠 AUD-M19-A02-SUSCEPTIBILIDADE-005 — O teto da escala de susceptibilidade exclui justamente os alvos do módulo
**Aula 02, seção de magnetometria; propagado para o recap e para a alegação `GEOMIN-M19-A02-SUSCEPTIBILIDADE-002`.**
**Tipo:** impreciso (valor).

**Está escrito:** *"varia ... ao longo de **quase quatro ordens de grandeza** — de cerca de 10⁻⁶ ... a cerca de **10⁻²** (rochas com magnetita abundante)"*.

**Problema:** o teto está cerca de duas ordens de grandeza baixo. Rochas ricas em magnetita — formação ferrífera magnetítica, minério de magnetita, peridotito serpentinizado — alcançam 10⁻¹ e valores da ordem da unidade em SI, e o mineral magnetita tem susceptibilidade da ordem de alguns SI (compilação GPG: **5,8 SI**; pirrotita 1,5 SI). A escala real cobre **mais de cinco** ordens de grandeza, não quase quatro. O dano é específico deste módulo: os alvos que ele ensina a procurar (corpos de magnetita, IOCG, VMS com pirrotita) vivem exatamente acima do teto que a aula declarou, de modo que o aluno fica sem régua justamente onde vai precisar dela.

**Fonte:** Clark (1997), **AGSO Journal of Australian Geology & Geophysics** 17(2), 83-103; tabela de susceptibilidade do GPG (gpg.geosci.xyz): magnetita 5,8 SI, pirrotita 1,5 SI, maghemita 5,8 SI, hematita 6,5×10⁻³ SI. **Nível:** revisada por pares + base de referência. **Confiança:** confirmado.

**Correção aplicada:** a escala passou a "mais de cinco ordens de grandeza", com três degraus nomeados (10⁻⁶-10⁻⁵ sedimentares/félsicas; 10⁻³-10⁻² máficas comuns; 10⁻¹ a ~1 em rochas ricas em magnetita) e o teto mineral explicitado (magnetita pura ~5 SI), mais uma frase que amarra a escala ao módulo ("os alvos deste módulo vivem no topo da escala, não em 10⁻²"). Propagado para o recap e para a alegação.

### 🟠 AUD-M19-A02-PIRROTITA-006 — "Pirrotita" sem fase, repetindo defeito já corrigido no M16 — e contradizendo a ordem do M15
**Aula 02, seção de magnetometria; propagado para o recap e para a alegação `GEOMIN-M19-A02-SUSCEPTIBILIDADE-002`.**
**Tipo:** impreciso (nomenclatura) + inconsistência entre módulos.

**Está escrito:** *"A **pirrotita** também é fortemente magnética (é o **segundo mineral comum mais relevante** para magnetometria de exploração, **atrás apenas da magnetita**)"*.

**Problema:** dois pontos, ambos contra módulos já fechados deste curso.
(a) **Fase.** Só a **pirrotita monoclínica** (Fe₇S₈) é ferrimagnética; a hexagonal é antiferromagnética à temperatura ambiente e não magnetiza a rocha. O Módulo 15 faz essa distinção com cuidado, e o Módulo 16 já teve exatamente este achado — `AUD-M16-A05-PIRROTITA-Y04`, corrigido em 2026-09-09 com a justificativa de que "sem o qualificador, a aula afrouxa uma distinção que o pré-requisito faz". O M19 reintroduz o mesmo afrouxamento.
(b) **Ordem.** O Módulo 15 estabelece a hierarquia: magnetita, depois **titanomagnetitas**, **maghemita** e então **pirrotita monoclínica**. Chamar a pirrotita de "segundo mineral mais relevante, atrás apenas da magnetita" contradiz frontalmente essa ordenação, e o M15 está `completed`, com questionário e dois baralhos já gerados.

**Fonte:** Módulo 15, aula 03 e sua alegação de minerais ferrimagnéticos (auditada e aprovada em 2026-09-08); auditoria do Módulo 16, achado `AUD-M16-A05-PIRROTITA-Y04`; Clark (1997), AGSO Journal 17(2), 83-103. **Nível:** revisada por pares + coerência interna do curso. **Confiança:** confirmado.

**Correção aplicada:** a pirrotita passou a **pirrotita monoclínica (Fe₇S₈)** em todas as ocorrências magnéticas da a02 (corpo, parágrafo do halo VMS, recap, alegação), com a fase hexagonal nomeada como contraste antiferromagnético — a mesma forma da correção do M16. A ordenação foi reescrita para respeitar o M15: magnetita, depois titanomagnetitas e maghemita, e então, **entre os sulfetos**, a pirrotita monoclínica. A a03 **não** precisou de edição no ponto: lá a pirrotita aparece como condutor eletrônico, contexto em que o qualificador de fase não é exigido.

### 🟠 AUD-M19-A03-SULFETOMACICOCONDUTOR-009 — "Sulfeto maciço é excelente condutor" sem a exceção que a exploração conhece
**Aula 03, seção de mecanismos de condução; propagado para o recap e para a alegação `GEOMIN-M19-A03-CONDUCAO-001`.**
**Tipo:** omissão que gera erro.

**Está escrito:** *"um corpo de **sulfeto maciço** (dominado por esses minerais, com poucos vazios entre grãos) **costuma ser um excelente condutor elétrico**"*.

**Problema:** como escrito, autoriza a inferência "maciço ⇒ condutor", que é falsa com frequência suficiente para custar furo. Quem conduz num corpo maciço é a **rede interconectada** de pirrotita e calcopirita. A **pirita**, o sulfeto mais abundante em muitos depósitos, é um semicondutor de condutividade muito mais baixa e muito mais variável — a mesma compilação que a aula cita para pirrotita e calcopirita dá **0,003 a 1 S/m** para pirita, isto é, até **sete ordens de grandeza** abaixo da pirrotita — e a **esfalerita** é má condutora. Corpos maciços dominados por pirita ou esfalerita são regularmente discretos ou francamente resistivos em EM e resistividade. A omissão importa duplamente aqui porque a aula constrói, duas seções adiante, o diagnóstico "baixa resistividade + alta cargabilidade": sem a ressalva, um corpo maciço piritoso cai na categoria que a aula manda despriorizar.

**Fonte:** tabela de condutividade do EM GeoSci (em.geosci.xyz, estudo de caso de Lalor): pirita 0,003-1 S/m, calcopirita 1-10⁴ S/m, pirrotita 4,5×10³-7,1×10⁴ S/m; literatura de VMS, que condiciona a resposta EM à **interconexão** dos sulfetos e registra a esfalerita como má condutora. **Nível:** base de referência + revisada por pares. **Confiança:** confirmado.

**Correção aplicada:** parágrafo novo logo após a afirmação, com a regra explícita **"maciço" não garante "condutor"**, os dois contraexemplos (pirita ~10⁻³-1 S/m; esfalerita má condutora), a identificação de quem de fato conduz (rede interconectada de pirrotita e calcopirita) e o gancho para a seção seguinte (esses corpos continuam sendo alvos fortes de IP). Propagado para o recap e para a alegação.

### 🟠 AUD-M19-A04-FDEMFREQUENCIA-007 — A faixa de frequência de um sistema específico generalizada a todo FDEM
**Aula 04, seção domínio do tempo × domínio da frequência; propagado para o recap e para a alegação `GEOMIN-M19-A04-TDEMFDEM-002`.**
**Tipo:** confusão de escopo (valor de um sistema apresentado como típico da família).

**Está escrito:** *"Sistemas de FDEM **tipicamente** trabalham numa faixa de frequências de áudio (da ordem de **1 Hz a 10 kHz**)."*

**Problema:** essa é a faixa do sistema **de fonte aterrada** do artigo que a aula cita (GAFEM, 1 Hz-10 kHz), não a dos FDEM aéreos convencionais, que são os que a aula está descrevendo no parágrafo. Os sistemas de bobina rebocada operam bem acima da faixa de áudio: **DIGHEM** entre ~900 Hz e 56 kHz, **RESOLVE** entre ~400 Hz e 140 kHz — mais de uma ordem de grandeza acima do teto declarado. A troca não é cosmética: a aula usa a frequência para explicar profundidade, e um leitor que fixe "FDEM = até 10 kHz" perde justamente as altas frequências que explicam por que esses sistemas são rasos e sensíveis ao regolito.

**Fonte:** fichas técnicas de **DIGHEM** (~900 Hz-56 kHz) e **RESOLVE** (~400 Hz-140 kHz); Chen et al. (2019), **Geophysics** 84(4), E269, que declara a faixa 1 Hz-10 kHz **para o sistema GAFEM de fonte aterrada**. **Nível:** técnica de fabricante + revisada por pares. **Confiança:** confirmado.

**Correção aplicada:** a frase única foi substituída por duas faixas separadas e rotuladas — FDEM aéreo convencional de bobina rebocada (DIGHEM ~900 Hz-56 kHz; RESOLVE ~400 Hz-140 kHz) e sistemas de fonte aterrada (~1 Hz-10 kHz) —, com uma frase acrescentada ligando frequência mais alta a penetração menor e amostragem multiprofundidade. Propagado para o recap e para a alegação.

### 🟠 AUD-M19-A04-CHENTDEM-008 — Um artigo sobre sistema de **frequência** creditado como prova da superioridade do **tempo**
**Aula 04, seção domínio do tempo × domínio da frequência; propagado para as Fontes e para a alegação `GEOMIN-M19-A04-TDEMFDEM-002`.**
**Tipo:** atribuição de fonte invertida + certeza indevida.

**Está escrito:** *"configurações especializadas — com fonte eletricamente aterrada e grande afastamento entre fonte e receptor ... já demonstraram profundidades de investigação da ordem de algumas centenas de metros a cerca de 1 km ..., **um patamar bem acima do que sistemas FDEM convencionais alcançam**"*, com a alegação registrando que Chen et al. (2019) *"menciona sistema **TDEM** aerotransportado de fonte aterrada atingindo ~800 m"*.

**Problema:** Chen et al. (2019), *"The **frequency-domain** airborne electromagnetic method with a grounded electrical source"*, **Geophysics** 84(4), E269, descreve o **GAFEM** — fonte elétrica aterrada, receptor aéreo, operando **no domínio da frequência**, de 1 Hz a 10 kHz, com estrutura rasa e profunda imageada a afastamentos fonte-receptor de **3 e 6 km**. A aula usa, portanto, um sistema **de frequência** como evidência de que o **tempo** alcança o que a frequência não alcança — a fonte sustenta o contrário do que lhe é creditado. É a mesma estrutura de `AUD-M18-A03-GOTZEKRAUSE-012` e `AUD-M17-A02-TEDESCHI-001`.

O erro de fundo é conceitual e vale mais que a citação: nesses arranjos a profundidade é governada pela **geometria e pela potência da fonte** (dipolo aterrado, afastamento quilométrico), não pelo domínio de aquisição. Misturar as duas coisas transforma uma comparação legítima (TDEM × FDEM **de bobina rebocada**) numa afirmação falsa sobre os domínios em geral.

**Fonte:** Chen, K. et al. (2019), **Geophysics** 84(4), E269, DOI 10.1190/geo2017-0777.1; Nabighian & Macnae (1991), *"Time domain electromagnetic prospecting methods"*, **SEG**, para a vantagem real do TDEM entre sistemas indutivos equivalentes. **Nível:** revisada por pares. **Confiança:** confirmado.

**Correção aplicada:** a comparação TDEM × FDEM foi restringida explicitamente a **sistemas aéreos de bobina rebocada** (a comparação justa), com os FDEM convencionais situados entre poucas dezenas e ~150-200 m. As profundidades de centenas de metros a ~1 km foram movidas para um parágrafo próprio sobre **sistemas semiaéreos de fonte aterrada**, com a explicação de que ali a profundidade vem da geometria e da potência da fonte, e de que isso vale **nos dois domínios** — com Chen et al. (2019) citado corretamente, como exemplo **de domínio da frequência**. A entrada de Fontes foi reescrita com a advertência de escopo, e a alegação registra a correção. Propagado para o recap, que ganhou um bullet novo separando "profundidade por geometria de fonte" de "profundidade por domínio".

---

## Achados amarelos (todos corrigidos)

A coluna da direita descreve o que passou a constar no arquivo, não mais uma proposta.

| ID | Aula | Achado | Correção aplicada |
|---|---|---|---|
| `AUD-M19-A01-HRONSKYGROVES-010` | a01 | **Hronsky & Groves (2008)** dado como *Geochemistry: Exploration, Environment, Analysis*, 8(2), 107-118. O artigo *"Science of targeting: definition, strategies, targeting and performance measurement"* está em **Australian Journal of Earth Sciences** 55(1), 3-12 | Citação corrigida para AJES 55(1), 3-12, com DOI 10.1080/08120090701581356, nas Fontes e na alegação `...SISTEMAMINERAL-001` |
| `AUD-M19-A01-WYBORN-011` | a01 | **Wyborn, Heinrich & Jaques (1994)** citado como *"Australian Proterozoic mineral systems: **essence of the essence**"*, *AGSO Research Newsletter*. Não foi possível confirmar artigo com esse título; o trabalho canônico e verificável tem outro título e outro veículo | Trocado para *"Australian Proterozoic mineral systems: **essential ingredients and mappable criteria**"*, **Proceedings of the AusIMM Annual Conference**, Darwin, 109-115, mantendo a menção à AGSO como instituição de origem do conceito |
| `AUD-M19-A03-PARASNIS-012` | a03 | **Parasnis** datado de **1997**; a alegação hesitava entre "1956/1997" | Corrigido para **Parasnis, D. S. (1956)**, *Geophysical Prospecting* **4(3), 249-278**, DOI 10.1111/j.1365-2478.1956.tb01409.x, com a anotação do que o artigo de fato mede |
| `AUD-M19-A04-CHEN2022AUTORES-013` | a04 | **Minerals 12(5), 583 (2022)** creditado a *"Chen, C. et al."*. Os autores são **Prikhodko, Bagrianski, Kuzmin & Sirohey** | Autoria corrigida, DOI 10.3390/min12050583 acrescentado, e a anotação ampliada para os três sistemas que a revisão cobre (AFMAG, ZTEM, MobileMT) |
| `AUD-M19-A06-CARRANZALABORTE-014` | a06 | Título do artigo de *Computers & Geosciences* **74, 60-70** (*"...with small number of prospects and data with missing values in Abra (Philippines)"*) creditado ao volume e à paginação de **outro** artigo dos mesmos autores no mesmo ano, *Ore Geology Reviews* **71, 777-787** (*"Data-driven predictive mapping of gold prospectivity, Baguio district..."*) | Desdobrado em **duas** entradas reais, cada uma com seu título, periódico, volume e paginação; a alegação `...POSITIVOSRAROS-003` cita as duas |
| `AUD-M19-A03-SUNBONGAJUM-015` | a03 | Entrada *"Sun, X. & Bongajum, E. (2023) e literatura recente sobre IP semi-empírico"* — sem título e sem periódico; a alegação ainda invocava **"ScienceDirect"**, que é plataforma, não fonte. Mesmo defeito de `AUD-M17-A05-KAMINSKI-011` e `AUD-M18-A03-PINTOHALLINAN-014` | Substituída pela fonte que efetivamente sustenta os limiares de 20%/30%: **Wu, Zou, Peng, Liu, Wu, Zhou & Tao (2022)**, *Minerals* **12(9), 1172**, DOI 10.3390/min12091172; **Gurin, Titov & Ilyin (2019)** recebeu paginação completa (**GRL 46(2), 670-677**) |
| `AUD-M19-A02-TL208-003` | a02 | Pico do **²⁰⁸Tl** dado como **2,62 MeV**. O valor é 2,6145 MeV, que arredonda para **2,61** — e é assim que aparece nos **Módulos 15 e 16**, ambos `completed`, com questionário e baralhos já gerados. "2,62" criava contradição transversal com cards já em circulação | Trocado para **2,61 MeV** no corpo, no recap e na alegação, alinhando com M15 e M16 |
| `AUD-M19-A03-CALCOPIRITA-018` | a03 | Condutividade da calcopirita dada como *"cerca de **20** a 10⁴ S/m"*. A compilação citada (EM GeoSci) dá **1 a 10⁴ S/m**; o piso de 20 não sai de fonte alguma identificável | Trocado para **~1 a 10⁴ S/m** no corpo, no recap e na alegação, com a tabela do EM GeoSci citada com seus três valores |
| `AUD-M19-A01-M14ANALOGIA-016` | a01 | *"É **exatamente o mesmo compromisso** já visto no sensoriamento remoto (Módulo 14)"*. Não é o mesmo: no M14 o compromisso entre as quatro resoluções nasce de um **orçamento fixo de fótons e de telemetria**; aqui nasce de **atenuação do sinal no meio atravessado**. Além disso, o cabeçalho prometia o par "resolução espacial × cobertura" e o corpo entregava "resolução espacial × largura de banda espectral" | Reescrito como **análogo, não idêntico**, com os dois mecanismos nomeados lado a lado e o par do M14 alinhado ao que aquele módulo de fato ensina (resolução espacial custa faixa de imageamento e número de bandas). A alegação `...RESOLUCAOPROFUNDIDADE-003` registra a ressalva |
| `AUD-M19-A05-CASCAESFERICA-017` | a05 | O exemplo esfera/casca era fechado com *"desde que a massa total e a posição do centro de massa sejam preservadas **de certa forma**"* — hedge que não enuncia a condição real | Enunciado o **teorema da casca de Newton**: o campo externo de qualquer distribuição **esfericamente simétrica** depende só da massa total e da posição do **centro**, com a casca **concêntrica** à esfera e o ponto de observação **fora** da distribuição |

---

## Achados azuis (verificados, corretos, sem alteração)

- **B1 — Os quatro componentes do sistema mineral (a01).** Fonte, transporte, deposição e preservação, com a mudança de pergunta que o paradigma opera: **confere**, e `McCuaig & Hronsky (2014), SEG Special Publication 18, 153-175` está citado **exatamente certo** — volume, número e paginação. Era a citação de maior risco da a01 e é a única das três que passou intacta.
- **B2 — Escalas aninhadas e espaçamento de linha de voo de 100-400 m (a01).** Dentro da prática de aquisição e **consistente com o Módulo 16**, que a a02 declara como antecedente. Apresentado corretamente como faixa típica, não como norma.
- **B3 — As duas razões físicas do compromisso resolução × profundidade (a01).** Atenuação dependente de frequência e limitação por espaçamento de estação em relação à profundidade do alvo: corretas e bem separadas uma da outra. O defeito da seção é só a analogia com o M14 (🟡 16).
- **B4 — Densidades de granito/gnaisse (2,6-2,8) e basalto (2,7-3,1 g/cm³) (a02).** Conferem. Só a faixa dos sulfetos estava errada (🟠 4).
- **B5 — Magnetita 5,1-5,2 g/cm³ (a02).** Dentro do aceito (GPG 4,90-5,20; valor de referência 5,18).
- **B6 — Magnetização induzida × remanente (a02).** A definição das duas parcelas, a dependência da induzida em relação à susceptibilidade, o caráter de "registro fóssil" da remanente e o alerta de que remanência forte e desalinhada produz forma de anomalia enganosa (dipolo deslocado, polaridade invertida) para quem assume magnetização puramente induzida: **tudo correto**, e consistente com o M15 e com o M16 (onde a RTP pressupõe magnetização induzida e o sinal analítico tolera remanência).
- **B7 — Profundidade de investigação da gamaespectrometria, 30-45 cm (a02).** Confere, e é **exatamente** o valor auditado e aprovado no Módulo 16 (achado A04-B01 daquela auditoria). Sem contradição transversal.
- **B8 — Convenção eU/eTh por medida de produto-filho (a02).** ⁴⁰K medido diretamente, U via ²¹⁴Bi e Th via ²⁰⁸Tl, com o "e" de equivalente justificado pela indireção: **correto e consistente com M15 e M16**, que tratam o assunto com a mesma formulação ("duas séries e um isótopo").
- **B9 — Condução eletrolítica × eletrônica (a03).** A distinção, a dependência da eletrolítica em relação a porosidade/saturação/salinidade e a faixa do granito são não fraturado (10³-10⁶ ohm·m, caindo a dezenas-centenas se fraturado e saturado): corretas. **Verificação transversal explícita:** o Módulo 15, aula 04, já antecipa este exato conteúdo — *"a condução deixa de ser eletrolítica (pelo fluido) e passa a ser eletrônica (pelo próprio mineral), um mecanismo à parte que a eletrorresistividade e a polarização induzida, tratadas em módulos de geofísica adiante, exploram especificamente"*. O M19 cumpre a promessa do M15 na mesma acepção, sem divergir. Melhor encaixe de pré-requisito do módulo.
- **B10 — Pirrotita 10³-10⁵ S/m (a03).** Confere com a compilação citada (EM GeoSci/Lalor: 4,5×10³-7,1×10⁴ S/m) e com a literatura de VMS. Só a calcopirita estava com o piso errado (🟡 18).
- **B11 — Por que a resistividade perde sulfeto disseminado (a03).** Falta de percolação elétrica entre grãos isolados, com a corrente ainda obrigada a atravessar a matriz: correto, e corretamente ligado ao caso econômico (pórfiro é disseminado de baixo teor por definição).
- **B12 — Mecanismo físico da IP e suas duas medidas (a03).** Polarização na interface grão condutor/eletrólito, cargabilidade em mV/V no domínio do tempo, PFE no domínio da frequência, e a afirmação de que são duas janelas para o mesmo fenômeno: **corretas**. A independência em relação à conectividade entre grãos — que é o ponto que justifica a existência do método — também.
- **B13 — Os quatro quadrantes resistividade × cargabilidade (a03).** Argila condutora = baixa resistividade + baixa cargabilidade; disseminado em rocha resistiva = resistividade moderada/alta + cargabilidade alta; sulfeto conectado = baixa resistividade + alta cargabilidade. A tabela implícita fecha, o exemplo trabalhado das Zonas A/B/C a executa corretamente, e a ressalva de que argilas ocasionalmente dão cargabilidade não desprezível está no lugar certo. **É o melhor material de avaliação do módulo.**
- **B14 — Dependência da IP de fatores petrofísicos além do teor (a03).** Tamanho de grão, área de superfície interna, textura e composição do eletrólito: correto, e reforçado independentemente por Gurin et al. (2019), que mostra que partículas passivadas não polarizam.
- **B15 — Física da indução eletromagnética (a04).** Campo primário alternado, correntes parasitas por lei de Faraday, campo secundário captado por bobina receptora, e a conclusão de que a dispensa de contato galvânico é o que viabiliza a aquisição aérea: **tudo correto**.
- **B16 — Vantagem de profundidade do TDEM sobre o FDEM (a04).** O mecanismo declarado — medir o decaimento já sem o campo primário presente permite ler janelas tardias associadas a correntes mais profundas e mais lentas — está correto para sistemas indutivos equivalentes, e Nabighian & Macnae (1991) o sustenta. O defeito da seção foi ampliar isso a arranjos de fonte aterrada (🟠 8).
- **B17 — Métodos de fonte natural (a04).** Origem do sinal em atividade global de raios, propagação na cavidade Terra-ionosfera, MT como membro crustal da família, AFMAG (*audio-frequency magnetics*) como variante rasa popularizada em plataforma aérea, e a desvantagem de variabilidade temporal do sinal exigindo processamento estatístico: **corretos**, e consistentes com o tratamento do MT no Módulo 18.
- **B18 — GPR (a04).** Faixa de dezenas de MHz a ~1 GHz, reflexão por contraste de **permissividade dielétrica**, resolução centimétrica a decimétrica, poucos metros de penetração (dezenas em material seco e resistivo), queda para menos de 1 m em material condutor, e o papel de apoio no fluxo de exploração (mapear regolito, não localizar o depósito): **tudo correto**. A frase que separa "o que controla a reflexão" (permissividade) de "o que controla a atenuação" (condutividade) é precisa e é o tipo de distinção que material didático costuma borrar.
- **B19 — Não unicidade do problema inverso de campos potenciais (a05).** O enunciado, a independência em relação à qualidade do dado, a analogia com o problema de **equivalência** em sondagem elétrica vertical e a classificação como **problema mal-posto**: corretos. Só a condição do exemplo esfera/casca precisava de precisão (🟡 17).
- **B20 — Inversão de Occam (a05).** `Constable, S. C., Parker, R. L. & Constable, C. G. (1987), "Occam's inversion: a practical algorithm for generating smooth models from electromagnetic sounding data", Geophysics, 52(3), 289-300` — **exata em autor, ano, título, volume, número e paginação**. Conferida justamente por ser a citação nominal mais visível do módulo. O conteúdo que a aula lhe credita (escolher, entre os modelos que ajustam o dado dentro do erro, o mais suave) é o do artigo.
- **B21 — Efeito da regularização por suavidade sobre a interpretação (a05).** Modelos mais difusos e espalhados que a geologia real, com risco de subestimar contraste e superestimar volume aparente, e a observação de que a escolha da regularização é ela própria decisão interpretativa: **correto e bem calibrado** — é o conteúdo que o hub declara como ponto de dificuldade do módulo, e ele está à altura.
- **B22 — Exemplo trabalhado da a05.** As duas equipes, a equivalência volume × contraste ("o que a gravimetria vê é o excesso de massa total"), e a conclusão de que a Equipe B decide melhor sem que seu modelo seja "mais verdadeiro" em sentido matemático: fecha, e é o melhor exemplo trabalhado do módulo.
- **B23 — GRAV3D/MAG3D/DCIP3D do UBC-GIF (a05).** Existem, são do Geophysical Inversion Facility da University of British Columbia e têm o uso na indústria que a aula descreve.
- **B24 — Camada de evidência e pesos de evidência (a06).** O conceito de camada de evidência como reinterpretação (não valor bruto), e o posicionamento de *weights of evidence* como ponte entre orientado por conhecimento e orientado por dados: corretos, e `Bonham-Carter (1994), Geographic Information Systems for Geoscientists: Modelling with GIS, Pergamon` está corretamente citado.
- **B25 — `Porwal & Carranza (2015), Ore Geology Reviews, 71, 477-483` (a06).** Título, periódico, volume e paginação **exatos**.
- **B26 — `Zuo & Carranza (2011), Computers & Geosciences, 37(12), 1967-1975` (a06).** **Exata.** Registrada aqui porque uma fonte terciária dava 1957 como página inicial; o bibcode ADS do artigo (`2011CG.....37.1967Z`) confirma **1967**. A aula está certa e **não deve ser "corrigida"** por quem topar com a divergência.
- **B27 — Positivos raros, sobreajuste e viés de amostragem de exploração (a06).** Os três estão corretos e bem distinguidos, e a formulação do viés de amostragem — tratar "não confirmado" como "geologicamente desfavorável" penaliza justamente a fronteira exploratória — é precisa. Só a citação de Carranza & Laborte precisava de conserto (🟡 14).
- **B28 — Exemplo trabalhado da a06.** O diagnóstico (6 positivos contra 15.000 km², mais uma camada com 8% de cobertura entrando como se fosse completa) e as três correções propostas fecham logicamente, e o tratamento da camada parcial — excluir do treinamento regional ou modelar a ausência explicitamente — é a conduta correta.

---

## Nota transversal — a recomendação do M18 não foi implementada, e o M19 pagou por isso

A auditoria do Módulo 18 fechou com uma recomendação explícita ao orquestrador, registrada tanto no relatório quanto no `process_defect_note` do estado: **antes de escrever o Módulo 19**, acrescentar ao gerador de aula uma verificação obrigatória de que cada entrada da lista de Fontes (a) existe com aquele autor, ano, periódico e paginação e (b) trata efetivamente do fato que a aula lhe credita.

O Módulo 19 foi escrito em 2026-09-12 sem essa verificação, e o resultado é mensurável: **7 dos 18 achados corrigíveis deste módulo são exatamente o defeito que a verificação teria pego** — os seis amarelos de atribuição mais a laranja `...CHENTDEM-008`. Somando os três módulos, o padrão já custou **4 achados no M17, 6 no M18 e 7 no M19**: está piorando, não melhorando.

Duas das ocorrências são **cópias estruturais exatas** de achados anteriores:
- `AUD-M19-A03-SUNBONGAJUM-015` é a entrada de bibliografia sem título nem periódico, igual a `AUD-M17-A05-KAMINSKI-011` e `AUD-M18-A03-PINTOHALLINAN-014`;
- `AUD-M19-A04-CHENTDEM-008` é o dado creditado ao artigo do fenômeno **oposto**, igual a `AUD-M18-A03-GOTZEKRAUSE-012` (o "gravity **high**" pela anomalia **negativa**) e a `AUD-M17-A02-TEDESCHI-001`.

**Recomendação, agora com prioridade elevada:** a verificação de Fontes deixa de ser sugestão e passa a ser **pré-condição de entrega de aula**. O custo é de minutos na redação; aqui teria evitado 7 dos 18 achados, e no M18 teria evitado 6 dos 17.

## Nota transversal — consistência com os módulos pré-requisito (14 e 15) e com o 16

Verificação explícita contra os módulos que o M19 declara como antecedentes. **Uma contradição encontrada e corrigida; as demais frentes estão limpas.**

1. **Módulo 15 (petrofísica), pré-requisito formal — CONTRADIÇÃO ENCONTRADA E CORRIGIDA.** A a02 chamava a pirrotita de "segundo mineral comum mais relevante, atrás apenas da magnetita", sem qualificar a fase. O M15 estabelece (a) que só a **monoclínica** é ferrimagnética e (b) a ordem magnetita → titanomagnetitas → maghemita → pirrotita monoclínica. O M15 está `completed` com questionário e dois baralhos gerados, de modo que a divergência atingiria material já em revisão. Corrigido nos dois pontos (🟠 6). **Agravante de processo:** este é o mesmo achado que o Módulo 16 já teve (`AUD-M16-A05-PIRROTITA-Y04`) — a correção do M16 não impediu a reincidência no M19.
2. **Módulo 15, condutividade elétrica — consistente, e é o melhor encaixe do módulo.** A aula 04 do M15 antecipa explicitamente o conteúdo da a03 do M19, nomeando a condução eletrônica por sulfetos maciços e grafita como "um mecanismo à parte que a eletrorresistividade e a polarização induzida, tratadas em módulos de geofísica adiante, exploram especificamente". O M19 cumpre a promessa na mesma acepção, sem repetir nem divergir.
3. **Módulo 15, densidade e susceptibilidade — sem contradição numérica.** O M15 não declara faixa numérica de susceptibilidade, de modo que a correção do teto na a02 do M19 (🟠 5) não gera divergência com nada já publicado; e as densidades do M19 agora batem com as compilações de referência.
4. **Módulo 15/16, gamaespectrometria — UMA divergência numérica, corrigida.** O pico do ²⁰⁸Tl aparecia como **2,62 MeV** no M19 contra **2,61 MeV** no M15 e no M16, ambos com flashcards e questionário já gerados (cards `geologia-avancado-m15-fb032`, `m15-fc040`, `m16-fb051`, `m16-fc040` carregam 2,61). Corrigido para 2,61 no M19 (🟡 3). As janelas de energia, que o M15 e o M16 não declaram, foram corrigidas contra a norma IAEA (🟠 2) sem tocar em nada daqueles módulos. A profundidade de 30-45 cm e a convenção eU/eTh conferem com os dois.
5. **Módulo 16 (aerogeofísica), invocado pela a02 — consistente.** Espaçamento de linha de voo, magnetização induzida × remanente, e as três janelas radiométricas convergem depois das correções. A a02 não reensina aquisição aérea; remete e aplica.
6. **Módulo 14 (sensoriamento remoto), pré-requisito formal — sem contradição factual, mas com uma analogia frouxa, corrigida.** O M14 ensina quatro resoluções competindo por um orçamento fixo de energia e de dado; o M19 chamava isso de "exatamente o mesmo compromisso" do par resolução × profundidade, que é físico e de outra natureza. Nenhum valor do M14 foi contrariado; o que se corrigiu foi o grau de identidade alegado (🟡 16).
7. **Módulo 18 (geofísica da América do Sul), invocado pela a02 e pela a04** para paleomagnetismo e magnetotelúrico: remetido sem repetir dado e sem divergir da versão auditada daquele módulo.

---

## Gate de avaliação

**LIBERADO.** 0 achados 🔴 e 0 🟠 em aberto — todos corrigidos em 2026-09-13, com a correção aplicada também aos recaps, ao exemplo trabalhado da a02 e às alegações auditáveis que repetiam o dado errado. **Questionário e baralho de flashcards podem ser gerados**, observadas as restrições abaixo.

Os pontos que bloqueavam o gate foram desfeitos na origem:

- a **polaridade magnética das zonas de alteração de pórfiro** está corrigida no corpo, no exemplo trabalhado, no recap e na alegação — potássica acrescenta magnetita, fílica destrói. O risco de gabarito invertido, que era o mais caro do módulo, desapareceu;
- as **três janelas de gamaespectrometria** são agora as da IAEA, com os intervalos mortos entre elas nomeados;
- as **densidades** deixaram de excluir a galena e a esfalerita da própria lista que enumeravam, e separam mineral de corpo de minério;
- o **teto da susceptibilidade** subiu de 10⁻² para a ordem da unidade, devolvendo régua aos alvos do módulo;
- a **pirrotita** ganhou a fase (monoclínica) e a ordem do M15;
- **"maciço ⇒ condutor"** deixou de ser inferência autorizada pelo texto;
- a comparação **TDEM × FDEM** foi restringida ao arranjo em que ela é verdadeira, e a fonte de frequência deixou de ser creditada pela superioridade do tempo.

### `generator_warnings` — advertências para quem gerar questionário e flashcards

Quinze pontos mudaram nesta auditoria. **Gerar item a partir da versão anterior das aulas produz gabarito errado.** As advertências de maior valor:

1. **O PAR DE SINAL OPOSTO MAIS VALIOSO DO MÓDULO: potássica × fílica.** Alteração **potássica acrescenta** magnetita → **alto** magnético; alteração **fílica/sericítica destrói** magnetita → **baixo** magnético, tipicamente anelar. O erro corrigido (potássica destrói) é **o distrator perfeito**, porque é o que o senso comum sugere para quem associa "alteração intensa" a "destruição". Prefira questão de **discriminação** a questão de definição isolada.
2. **NÃO gerar card nem gabarito que diga que a alteração potássica destrói magnetita** — foi exatamente esse o erro corrigido.
3. **Ponto de discriminação de alto valor, novo no material após a correção:** *o canal K da gamaespectrometria **não** distingue alteração potássica de fílica, porque a sericita também é mica potássica — quem distingue é o sinal magnético.* Rende excelente questão de aplicação e é o tipo de sutileza que separa leitura mecânica de leitura real.
4. **Janelas de gamaespectrometria: usar 1,37-1,57 / 1,66-1,86 / 2,41-2,81 MeV** (IAEA). Os valores antigos (1,36-1,60 / 1,60-1,95 / 2,40-2,86) são **distratores**, e "as janelas são contíguas" é distrator conceitual forte, com a resposta certa sendo "há intervalos mortos entre elas, para limitar vazamento entre canais".
5. **Picos: K 1,46 · ²¹⁴Bi 1,76 · ²⁰⁸Tl 2,61 MeV.** Usar **2,61**, nunca 2,62 — é o valor dos Módulos 15 e 16, que já têm cards em circulação. Qualquer card novo com 2,62 entraria em conflito direto com `m15-fb032`, `m15-fc040`, `m16-fb051` e `m16-fc040`.
6. **Densidades: a galena (7,4-7,6 g/cm³) é o distrator numérico mais forte do bloco de gravimetria**, porque quebra a intuição de que "sulfeto maciço fica em torno de 4-5". Boa questão de aplicação: por que a densidade de um **corpo** de sulfeto maciço (3,5-4,5) é menor que a dos **minerais** que o compõem? (Resposta: ganga.) Não cobrar "4,2-5,0" como faixa de sulfeto maciço — era o valor errado.
7. **Susceptibilidade: usar "mais de cinco ordens de grandeza, de ~10⁻⁶ a valores da ordem da unidade".** "Até 10⁻²" agora é **distrator**, não gabarito. Magnetita mineral ~5 SI é par numérico limpo e novo no material.
8. **Pirrotita: sempre MONOCLÍNICA (Fe₇S₈) em contexto magnético.** "Pirrotita hexagonal é ferrimagnética" é distrator; e não gerar item que a coloque como "segundo mineral mais magnético depois da magnetita" — contradiz a ordem do M15 (titanomagnetitas, maghemita, pirrotita monoclínica). Em contexto de **condução elétrica**, porém, "pirrotita" sem qualificador está correto: não transformar isso em armadilha.
9. **PAR DE SINAL OPOSTO nº 2, e excelente distrator: "maciço" × "condutor".** Um corpo maciço dominado por **pirita** (~10⁻³-1 S/m) ou **esfalerita** pode ser **resistivo**; quem conduz é a rede interconectada de pirrotita e calcopirita. Questão de aplicação de alto valor: um corpo maciço confirmado por sondagem que **não** apareceu no levantamento EM — o que explica? Ponto novo no material após a correção.
10. **Condutividades: pirrotita 10³-10⁵, calcopirita 1-10⁴, pirita 0,003-1 S/m.** Não usar "20 S/m" como piso da calcopirita (valor corrigido). O contraste pirrotita × pirita, de até sete ordens de grandeza entre dois sulfetos, é o melhor par numérico da a03.
11. **PAR DE SINAL OPOSTO nº 3, já pronto na aula e intocado pela auditoria: os quatro quadrantes resistividade × cargabilidade.** Baixa ρ + baixa M = argila/água salobra; ρ moderada + alta M = disseminado; baixa ρ + alta M = sulfeto conectado. É o material de avaliação mais denso do módulo e não exige nenhuma ressalva de auditoria.
12. **TDEM × FDEM: a comparação só vale entre sistemas aéreos de BOBINA REBOCADA.** Não gerar item que diga que o TDEM alcança ~1 km "porque é domínio do tempo" — nesses casos a profundidade vem da **fonte aterrada e do afastamento quilométrico**, e existe sistema de **frequência** (GAFEM) fazendo o mesmo. Distrator forte e contraintuitivo, novo no material.
13. **Frequências de FDEM: DIGHEM ~900 Hz-56 kHz, RESOLVE ~400 Hz-140 kHz** para aéreos convencionais; ~1 Hz-10 kHz só para fonte aterrada. "FDEM vai só até 10 kHz" agora é distrator.
14. **Citações corrigidas — não gerar item que reproduza as antigas:** Hronsky & Groves está em *Australian Journal of Earth Sciences* 55(1), 3-12 (não em GEEA); Parasnis é de **1956** (não 1997); *Minerals* 12(5), 583 é de **Prikhodko et al.** (não Chen); Carranza & Laborte "…in Abra" está em *Computers & Geosciences* 74, 60-70. De modo geral: **não gerar questão cujo gabarito seja uma referência bibliográfica** — é o ponto mais frágil deste módulo e o que menos ensina.
15. **Occam: Constable, Parker & Constable (1987), Geophysics 52(3), 289-300 — conferida e exata.** Se alguém encontrar "1957-1975" para Zuo & Carranza em alguma base, **a aula está certa com 1967-1975** (bibcode ADS `2011CG.....37.1967Z`): não "corrigir".

### Restrição de formato

Nenhuma. Não há achado ⚪ neste módulo, e nenhum ponto do material ficou com incerteza que impeça questão fechada. Os dois únicos lugares onde a aula deve ser cobrada **com** a ressalva que ela própria já traz são: (a) os limiares de linearidade da cargabilidade (20% disseminado / 30% veio-maciço) são **ordem de grandeza de modelagem e laboratório**, não constante física — cobrar a existência da não linearidade, não o número como se fosse exato; e (b) o zoneamento de pórfiro é **padrão típico**, não assinatura universal — cobrar a regra de sinal, não a geometria como se fosse obrigatória em todo sistema.

---

## Recomendação preliminar — parciais ou questionário único

**Preliminar, e a decisão é do `gerador-de-questionarios`, não desta auditoria.** Com **6 aulas**, o módulo está no limiar da regra do plugin (parciais a partir de ~5-6 aulas). Duas observações que a geração deve pesar:

- as 6 aulas se agrupam de forma **muito limpa em três blocos**, e os blocos coincidem com fronteiras de objetivo: **a01 (oa01)** · **a02 (oa02)** · **a03+a04 (oa03)** · **a05+a06 (oa04)**. Um corte em **três parciais** (a01+a02 / a03+a04 / a05+a06) mais um **final cumulativo** respeitaria os quatro objetivos sem partir nenhum ao meio;
- o módulo tem **fio condutor forte e explícito** (o sistema mineral abre na a01 e fecha na a06; o compromisso resolução × profundidade atravessa as seis), o que dá material real para um cumulativo com questões de integração — não seria um cumulativo artificial.

**Inclinação:** 3 parciais + 1 final cumulativo, como no Módulo 13. Mas a decisão fica aberta.

---

## Observações fora de escopo (não são achados factuais)

Registradas em uma linha cada para não se perderem, e pertencem a outras skills:

- **Didática (`revisor-didatico`):** a correção 🔴 1 e a 🟠 6 entraram como blocos novos dentro de parágrafos já longos da a02 — o parágrafo de magnetometria agora carrega susceptibilidade, hierarquia de minerais, halos de alteração, regra de sinal de pórfiro e remanência numa única sequência. É exatamente o efeito que o `audit_preservation_note` do M18 previu ("corrigir o fato tornou a forma pior"). A revisão didática deve olhar este parágrafo primeiro; o conteúdo está certo, a forma pede quebra.
- **Didática:** a a02 é agora a aula mais densa do módulo em fatos numéricos por parágrafo (densidades de seis minerais, três degraus de susceptibilidade, três picos e três janelas). Vale conferir se ainda cabe nos ~30 min declarados.
- **Estrutural (`validador-estrutural-do-curso`):** os wikilinks de pré-requisito das aulas usam formato de caminho (`[[15-petrofisica/15-petrofisica-modulo|Módulo 15]]`) enquanto os links internos usam nome de arquivo puro — mesma observação feita no M18, ainda pendente de decisão sobre qual forma resolve no vault.

---

## Desfecho — correções aplicadas

**Aplicadas em:** 2026-09-13

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `AUD-M19-A02-PORFIROMAGNETITA-001` | 🔴 | Corrigido | aula-02 (corpo, exemplo trabalhado, recap, alegação, Fontes) |
| `AUD-M19-A02-JANELASGAMA-002` | 🟠 | Corrigido | aula-02 (corpo, recap, alegação) |
| `AUD-M19-A02-DENSIDADESULFETO-004` | 🟠 | Corrigido | aula-02 (corpo, recap, alegação) |
| `AUD-M19-A02-SUSCEPTIBILIDADE-005` | 🟠 | Corrigido | aula-02 (corpo, recap, alegação) |
| `AUD-M19-A02-PIRROTITA-006` | 🟠 | Corrigido | aula-02 (corpo em três pontos, recap, alegação, Fontes) |
| `AUD-M19-A03-SULFETOMACICOCONDUTOR-009` | 🟠 | Corrigido | aula-03 (corpo, recap, alegação) |
| `AUD-M19-A04-FDEMFREQUENCIA-007` | 🟠 | Corrigido | aula-04 (corpo, recap, alegação) |
| `AUD-M19-A04-CHENTDEM-008` | 🟠 | Corrigido | aula-04 (corpo, recap, alegação, Fontes) |
| `AUD-M19-A01-HRONSKYGROVES-010` | 🟡 | Corrigido | aula-01 (Fontes, alegação) |
| `AUD-M19-A01-WYBORN-011` | 🟡 | Corrigido | aula-01 (Fontes, alegação) |
| `AUD-M19-A03-PARASNIS-012` | 🟡 | Corrigido | aula-03 (Fontes, alegação) |
| `AUD-M19-A04-CHEN2022AUTORES-013` | 🟡 | Corrigido | aula-04 (Fontes, alegação) |
| `AUD-M19-A06-CARRANZALABORTE-014` | 🟡 | Corrigido | aula-06 (Fontes, alegação) |
| `AUD-M19-A03-SUNBONGAJUM-015` | 🟡 | Corrigido | aula-03 (Fontes, alegação) |
| `AUD-M19-A02-TL208-003` | 🟡 | Corrigido | aula-02 (corpo, recap, alegação) |
| `AUD-M19-A03-CALCOPIRITA-018` | 🟡 | Corrigido | aula-03 (corpo, recap, alegação) |
| `AUD-M19-A01-M14ANALOGIA-016` | 🟡 | Corrigido | aula-01 (corpo, alegação) |
| `AUD-M19-A05-CASCAESFERICA-017` | 🟡 | Corrigido | aula-05 (corpo, alegação) |

**Arquivos tocados:** as seis aulas (a01, a02, a03, a04, a05, a06) e o hub do módulo. Os 28 achados 🔵 não geraram edição — são registros de verificação bem-sucedida.

**Pendências: nenhuma.** Nenhum achado aguarda decisão do usuário, e não há controvérsia aberta na literatura afetando este módulo.

**Material derivado a propagar: nenhum.** O módulo não tinha questionário nem baralho quando as correções foram aplicadas — a auditoria rodou antes deles, como manda a cadeia. **Nada a reimportar no Anki e nenhum card em revisão a corrigir à mão.** Esta era a melhor hora possível: a inversão de polaridade do pórfiro não chegou a virar gabarito nem card.

**Atenção para os Módulos 15 e 16:** o único ponto que tocava material já gerado era o pico do ²⁰⁸Tl, e ele foi resolvido **alinhando o M19 aos módulos fechados** (2,61), não o contrário. Nenhum card do M15 ou do M16 precisa de alteração.

**Manifesto estruturado:** `19-geofisica-exploracao-mineral-auditoria.json`
