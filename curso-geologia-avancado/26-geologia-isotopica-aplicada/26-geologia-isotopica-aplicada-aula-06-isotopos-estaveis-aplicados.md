# Aula 06: Isótopos estáveis — notação delta, fracionamento, e aplicação a minérios e magmas

**ID:** geologia-avancado-m26-a06
**Módulo:** [[26-geologia-isotopica-aplicada-modulo|Módulo 26 — Geologia isotópica aplicada]]
**Duração estimada:** ~25 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** trocar a pergunta do módulo. Nas Aulas 02 a 05, a razão isotópica media **tempo**; daqui em diante ela mede **processo**. Esta aula estabelece a máquina comum a todas as aplicações — a notação δ e os dois regimes de fracionamento — e a põe para trabalhar nos dois isótopos leves clássicos da geologia de rocha e de minério: o enxofre, em gênese de depósitos minerais, e o oxigênio, em petrogênese ígnea.
**Ao final você vai conseguir:** aplicar a notação δ e dizer o que significa um valor positivo ou negativo em relação ao padrão de referência de cada elemento; explicar por que o fracionamento de equilíbrio depende da temperatura e como isso sustenta a geotermometria isotópica, e em que o fracionamento cinético difere dele; e interpretar valores de δ34S em sulfetos e de δ18O em rochas ígneas como indicativos de fonte e de processo.
**Pré-requisito:** [[26-geologia-isotopica-aplicada-aula-01-radioatividade-lei-decaimento-geocronologia-espectrometria-massa|Aula 01]] (a distinção entre isótopos radiogênicos e isótopos estáveis fracionados por massa, introduzida ali, é o eixo conceitual desta aula e da seguinte). As referências cruzadas a traçadores radiogênicos no fim da aula supõem as [[26-geologia-isotopica-aplicada-aula-03-sistema-rb-sr|Aulas 03]] e [[26-geologia-isotopica-aplicada-aula-04-metodo-sm-nd|04]] (razão inicial de Sr e εNd), mas o conteúdo próprio desta aula não depende delas.

## Conteúdo

### A notação delta: como se relata um fracionamento pequeno

Ao contrário dos sistemas radiogênicos das Aulas 02 a 05, cuja razão isotópica muda por decaimento nuclear e mede tempo, os isótopos estáveis desta aula têm razões isotópicas que **não mudam com o tempo por decaimento nenhum** — mudam porque processos físicos, químicos e biológicos discriminam levemente entre átomos mais leves e mais pesados do mesmo elemento, num fenômeno chamado **fracionamento isotópico**. Como esses fracionamentos costumam ser pequenos (frações de percentual da razão isotópica), a comunidade adotou a **notação δ** (delta), que expressa o desvio da razão isotópica de uma amostra em relação a um padrão de referência internacional, em partes por mil (‰, "por mil", não "por cento"):

$$\delta = \left(\frac{R_{\text{amostra}}}{R_{\text{padrão}}} - 1\right) \times 1000$$

onde R é a razão entre o isótopo mais pesado e o mais leve do elemento em questão (por exemplo, ¹⁸O/¹⁶O para oxigênio, ¹³C/¹²C para carbono, ³⁴S/³²S para enxofre). Cada elemento tem seu próprio padrão de referência internacional, mantido e distribuído pela Agência Internacional de Energia Atômica (IAEA): o **VSMOW** (*Vienna Standard Mean Ocean Water*, água do mar padronizada) para oxigênio e hidrogênio; o **VPDB** (*Vienna Pee Dee Belemnite*, um padrão de carbonato originalmente derivado de uma belemnite fóssil da Formação Pee Dee, Carolina do Sul) para carbono (e para oxigênio em carbonatos, quando se quer comparar diretamente com outros carbonatos); o **VCDT** (*Vienna Canyon Diablo Troilite*, derivado da troilita — FeS — de um meteorito de ferro) para enxofre; e o **AIR** (nitrogênio atmosférico) para nitrogênio. Um δ¹⁸O de +10‰ significa que a amostra é 10 partes por mil **mais rica** no isótopo pesado (¹⁸O) que o padrão VSMOW; um δ¹³C de −25‰ significa que a amostra é 25 partes por mil **mais pobre** em ¹³C que o VPDB.

Repare que a notação só faz sentido acoplada ao seu padrão: um δ¹⁸O de +10‰ contra VSMOW e o mesmo valor contra VPDB são afirmações diferentes sobre a mesma rocha, e trocar um pelo outro é o erro de leitura mais comum da área. Todo valor publicado carrega o padrão junto — quando não carrega, o dado está incompleto.

### Fracionamento dependente de massa: equilíbrio e cinética

O fracionamento isotópico ocorre porque a massa de um átomo afeta discretamente a energia de suas ligações químicas e a velocidade de reações e de processos de transporte em que ele participa — um átomo mais pesado forma ligações ligeiramente mais fortes e se move ligeiramente mais devagar. Dois regimes de fracionamento dominam a geoquímica isotópica estável:

- **Fracionamento de equilíbrio.** Entre duas fases em equilíbrio químico (por exemplo, dois minerais coexistentes, ou um mineral e um fluido), a distribuição de isótopos pesados e leves entre as duas fases atinge um estado estacionário que depende da temperatura: quanto mais alta a temperatura, menor a diferença isotópica entre as fases (a energia térmica "diluiu" a preferência sutil de ligação). Essa dependência de temperatura é a base da **geotermometria isotópica**: medindo o fracionamento entre dois minerais coexistentes de uma rocha (por exemplo, quartzo e magnetita), e usando uma calibração experimental do fracionamento em função de T, estima-se a temperatura de equilíbrio da rocha. É o mesmo tipo de raciocínio de um geotermômetro de elementos maiores, com a diferença de que aqui o termômetro é a diferença isotópica entre as duas fases, e não a partição de um elemento entre elas.
- **Fracionamento cinético.** Em processos irreversíveis ou incompletos (evaporação, reações biológicas, difusão), a molécula ou o átomo mais leve reage ou se move mais rápido que o mais pesado, produzindo fracionamentos frequentemente maiores que os de equilíbrio, e sensíveis à taxa do processo, não só à temperatura. A fotossíntese, por exemplo, discrimina fortemente contra o ¹³CO₂ em favor do ¹²CO₂, deixando a matéria orgânica fotossintetizada isotopicamente mais leve (δ¹³C mais negativo) que o CO₂ atmosférico do qual ela se originou — um fracionamento cinético biológico que sustenta boa parte da interpretação de δ¹³C em rochas sedimentares ricas em matéria orgânica.

A distinção entre os dois regimes não é acadêmica: ela decide **o que** o número que você mediu está registrando. Um fracionamento de equilíbrio registra uma temperatura; um fracionamento cinético registra a existência, e às vezes a intensidade, de um processo em andamento. Ler um como o outro é atribuir temperatura a uma bactéria, ou metabolismo a um par de minerais.

### δ34S em depósitos minerais: fonte magmática versus biológica

O enxofre tem quatro isótopos estáveis, e a razão ³⁴S/³²S é um dos traçadores mais usados em metalogênese porque suas duas principais vias de fracionamento produzem assinaturas numericamente muito distintas:

- **Enxofre de fonte magmática ou mantélica** (sulfetos em depósitos ortomagmáticos de Ni-Cu-EGP associados a intrusões máficas-ultramáficas, ou sulfetos em pórfiros cupríferos derivados de magmas subvulcânicos) tende a ter δ34S próximo de **0 ± 2‰** — refletindo a composição do manto, homogênea o suficiente para que valores próximos de zero sejam interpretados como "enxofre magmático não fracionado".
- **Redução bacteriana de sulfato** (RBS, um processo metabólico em que bactérias anaeróbias reduzem sulfato marinho dissolvido a sulfeto, tipicamente em ambientes de fundo oceânico pobres em oxigênio) discrimina fortemente contra o ³⁴S, produzindo sulfeto biogênico com δ34S bastante **negativo** — frequentemente entre −10‰ e −40‰ ou mais negativo, dependendo da taxa de redução e da disponibilidade de sulfato — enquanto o sulfato residual não reduzido fica progressivamente enriquecido em ³⁴S (mais positivo). Esse é um processo central na gênese de muitos depósitos sedimentares-exalativos (SEDEX) e de sulfetos maciços vulcanogênicos (VMS) com componente biogênico, onde o enxofre do minério é uma mistura, em proporções variáveis, de enxofre de fonte hidrotermal/magmática e enxofre biogênico incorporado da coluna d'água ou do sedimento encaixante.

Repare que a RBS é um fracionamento **cinético** da seção anterior, e é por isso que ele é tão grande: 30 ou 40 partes por mil separam o sulfeto biogênico do enxofre magmático, uma distância que nenhum fracionamento de equilíbrio a temperatura magmática produziria. É justamente essa magnitude que torna o δ34S um discriminador tão limpo entre as duas vias.

Medir δ34S em diferentes gerações de sulfeto de um mesmo depósito (por exemplo, pirita diagenética precoce versus pirita hidrotermal tardia) permite, portanto, reconstruir a proporção relativa de enxofre de cada via ao longo da história de formação do depósito — um dado central para modelos genéticos de jazidas, e o objeto do exemplo trabalhado desta aula.

### δ18O em petrogênese ígnea

O oxigênio, sendo o elemento mais abundante da maioria das rochas, é um traçador petrogenético natural. O manto terrestre tem uma composição isotópica de oxigênio notavelmente homogênea: zircões de origem mantélica (de kimberlitos, ou de rochas máficas não contaminadas) mostram δ18O ≈ 5,3 ± 0,3‰ (VSMOW) — um valor de referência amplamente citado, derivado de compilações de dados de zircão de múltiplos ambientes mantélicos. Essa homogeneidade é o que faz o traçador funcionar: quando a referência é apertada, um desvio pequeno já é diagnóstico. Desvios sistemáticos desse valor mantélico são, então, diagnósticos de processo:

- **δ18O mais alto que o mantélico** (acima de 7‰) tipicamente indica incorporação de material crustal supracrustal enriquecido em ¹⁸O por intemperismo, diagênese ou alteração hidrotermal de baixa temperatura — por assimilação ou por fusão parcial de crosta já alterada, elevando o δ18O do magma acima do valor mantélico puro.
- **δ18O mais baixo que o mantélico** indica interação com água meteórica (chuva, neve) circulada em alta temperatura antes de reagir com a rocha — água meteórica tem δ18O bem mais negativo que a água do mar, e sistemas hidrotermais de caldeira vulcânica ou de rifteamento continental produzem granitos de δ18O anomalamente baixo por esse mecanismo.

Esse raciocínio complementa diretamente a razão inicial de Sr (Aula 03) e o εNd (Aula 04), e vale entender por que os três não são redundantes: Sr e Nd registram a história isotópica **de longo prazo** do reservatório que forneceu o magma — uma assinatura acumulada em centenas de milhões a bilhões de anos de decaimento. O oxigênio registra a interação **de curto prazo** com fluido crustal ou meteórico, que pode ter acontecido no último quilômetro de ascensão do magma. Um granito pode ter Sr e Nd de assinatura mantélica e δ18O crustal: isso não é contradição, é a informação — magma de fonte profunda que interagiu com água superficial perto do fim da sua história. Três traçadores que respondem a escalas de tempo diferentes contam, juntos, uma história que nenhum deles conta sozinho.

## Exemplo trabalhado: interpretando três amostras de sulfeto de um mesmo depósito

**Situação.** Um depósito polimetálico foi amostrado em três estágios distintos de mineralização, com os seguintes valores de δ34S medidos em pirita (dados hipotéticos, construídos para este exemplo):

| Estágio | δ34S (‰, VCDT) |
|---|---|
| 1 — pirita diagenética precoce, sedimento encaixante | −28,5 |
| 2 — pirita hidrotermal principal, veio mineralizado | +1,2 |
| 3 — pirita tardia, borda de veio próxima à rocha encaixante | −9,8 |

**Interpretação.** O Estágio 1, com δ34S fortemente negativo (−28,5‰), é consistente com enxofre produzido por redução bacteriana de sulfato marinho durante a diagênese precoce do sedimento — o sulfato original da água do mar, isotopicamente mais pesado, foi progressivamente reduzido a sulfeto por bactérias, que discriminam fortemente contra o ³⁴S, deixando o sulfeto biogênico residual isotopicamente muito leve. O Estágio 2, próximo de 0‰ (+1,2‰), é consistente com enxofre de fonte magmática ou hidrotermal profunda, sem fracionamento biológico significativo — a assinatura típica do fluido mineralizante principal. O Estágio 3, intermediário (−9,8‰), é consistente com uma **mistura** entre o fluido hidrotermal principal (Estágio 2) e enxofre biogênico incorporado localmente da rocha encaixante sedimentar próxima à borda do veio (semelhante em origem ao do Estágio 1, mas diluído pela contribuição hidrotermal) — um padrão comum em depósitos onde um fluido de fonte magmática interage, na zona de deposição, com rochas encaixantes ricas em sulfeto biogênico pré-existente. A leitura conjunta dos três estágios sugere um modelo genético em que o depósito se formou por um fluido hidrotermal de fonte profunda que, ao encontrar a sequência sedimentar encaixante (já portadora de sulfeto biogênico diagenético), incorporou e mesclou enxofre local em graus variáveis ao longo da evolução do sistema — exatamente o tipo de reconstrução que uma leitura isolada de um único valor de δ34S jamais permitiria.

**O que o exemplo não permite concluir.** Vale marcar o limite: os três valores estabelecem que há **duas fontes** de enxofre e que elas se misturaram em proporções diferentes ao longo do tempo. Eles não estabelecem a proporção numérica da mistura no Estágio 3 — para isso seria preciso saber o δ34S exato dos dois membros extremos no momento daquela mistura, e o Estágio 1 dá apenas uma amostra de um reservatório biogênico que é, ele mesmo, heterogêneo. Uma isotopia de enxofre bem lida delimita modelos genéticos; ela raramente fecha um sozinha.

## Recap relâmpago

- A notação δ (partes por mil) expressa o desvio da razão isotópica de uma amostra em relação a um padrão internacional — VSMOW para O e H, VPDB para C, VCDT para S, AIR para N — e um valor δ sem o seu padrão declarado é um dado incompleto.
- **Fracionamento de equilíbrio** depende de temperatura (menor fracionamento em T mais alta), e é a base da geotermometria isotópica por pares de minerais coexistentes; **fracionamento cinético** ocorre em processos irreversíveis, costuma ser maior e registra a existência de um processo, não uma temperatura. Confundir os dois é atribuir temperatura a um metabolismo.
- δ34S distingue enxofre de fonte magmática (≈0 ± 2‰) de enxofre biogênico por redução bacteriana de sulfato (tipicamente −10‰ a −40‰ ou mais negativo, um fracionamento cinético e por isso tão grande); misturar as duas fontes em proporções variáveis ao longo da história de um depósito é um modelo genético comum em jazidas SEDEX e VMS.
- δ18O mantélico de referência ≈ 5,3 ± 0,3‰ (VSMOW, em zircão); valores mais altos indicam contaminação por material crustal supracrustal reciclado, valores mais baixos indicam interação com água meteórica circulada em alta temperatura.
- Sr e Nd (Aulas 03 e 04) registram a história de **longo prazo** da fonte; o oxigênio registra interação de **curto prazo** com fluido. Assinaturas discordantes entre eles não são contradição — são a história do magma em duas escalas de tempo.

## Próxima aula

[[26-geologia-isotopica-aplicada-aula-07-isotopos-estaveis-registro-ambiental|Aula 07 — Isótopos estáveis como registro ambiental]]: a mesma máquina de fracionamento aplicada não mais à rocha ou ao minério, mas ao **ambiente** que os cercou — correlacionar estratos pela composição química da água do mar, ler o estado redox de um oceano antigo com isótopos não tradicionais de Fe, Mo e Hg, e rastrear a fonte de um contaminante.

## Fontes

- Faure, G. & Mensing, T. M. (2005), *Isotopes: Principles and Applications*, 3ª ed., Wiley — capítulos 16 a 22 (isótopos estáveis de H, C, N, O, S; notação delta; padrões de referência; fracionamento de equilíbrio e cinético).
- Hoefs, J. (2021), *Stable Isotope Geochemistry*, 9ª ed., Springer (Springer Textbooks in Earth Sciences, Geography and Environment; ISBN 978-3-030-77691-6) — referência abrangente de isótopos estáveis tradicionais e suas aplicações em petrogênese, paleoclimatologia e metalogênese. CORRIGIDO na auditoria (2026-09-21): a edição de 2021 é a **9ª**, não a 8ª; a 8ª edição é de 2018.
- Valley, J. W. et al. (2005), "4.4 billion years of crustal maturation: oxygen isotope ratios of magmatic zircon", *Contributions to Mineralogy and Petrology*, 150(6), 561-580 (doi 10.1007/s00410-005-0025-8) — valor de referência δ18O mantélico de zircão de 5,3 ± 0,3‰ VSMOW. CONFERIDO na auditoria (2026-09-21): volume e paginação confirmados.

<!--
nivel: avancado
palavras_corpo: 2100
duracao_estimada_min: 25

NOTA DE REVISAO DIDATICA (2026-09-22, revisor-didatico, modo review-and-fix):
  Esta aula e o resultado da DIVISAO da Aula 06 original (achado laranja DID-1). A aula original
  tinha 2546 palavras (~30,3 min, no teto do plugin) e SETE dominios de aplicacao independentes
  (notacao, fracionamento, delta34S metalogenese, delta18O petrogenese, quimioestratigrafia,
  isotopos nao tradicionais, contaminacao ambiental) com UM unico exemplo trabalhado, que cobria
  so o primeiro deles. A divisao ficou: esta aula = fundamentos (notacao + fracionamento) mais os
  dois isotopos leves classicos aplicados a rocha e minerio (S e O), com o exemplo de sulfetos;
  Aula 07 = as aplicacoes ambientais (quimioestratigrafia, paleorredox com Fe/Mo/Hg, contaminacao),
  com um exemplo trabalhado proprio. Nenhuma frase de conteudo foi removida do modulo: o texto das
  secoes movidas esta integralmente na Aula 07.
  ACRESCIMOS DESTA REVISAO (nenhum fato novo, so explicitacao do que a aula ja pressupunha):
  (a) paragrafo sobre a notacao delta so fazer sentido acoplada ao padrao; (b) frase ligando a RBS
  ao fracionamento CINETICO da secao anterior, que a aula original nunca conectava, embora tivesse
  ensinado os dois; (c) explicitacao de por que Sr/Nd e O nao sao redundantes (escalas de tempo
  diferentes), que a aula original afirmava em uma linha sem desenvolver; (d) secao 'O que o exemplo
  nao permite concluir'; (e) frase sobre a homogeneidade do manto ser o que faz o tracador de O
  funcionar.
  OBJETIVO DECLARADO CORRIGIDO (achado laranja DID-4): o cabecalho da aula original prometia
  'calcular o fracionamento entre duas fases em equilibrio isotopico', e a aula NUNCA calcula
  fracionamento nenhum - nao apresenta alfa, nem 1000*ln(alfa), nem equacao de calibracao. O
  objetivo declarado foi alinhado ao que a aula de fato ensina ('explicar por que o fracionamento de
  equilibrio depende da temperatura e como isso sustenta a geotermometria isotopica'). Nenhum
  objetivo de aprendizagem DO MODULO foi afetado: o OA-04 nao menciona geotermometria.
  PALEOCLIMATOLOGIA (achado vermelho DID-2, EM ABERTO): o titulo e o objetivo da aula original
  declaravam paleoclimatologia, e NENHUMA secao dela ensinava paleoclimatologia - a palavra nao
  aparece no corpo de nenhuma das seis aulas do modulo. A declaracao foi retirada do nivel da aula
  para que nenhuma aula prometa o que nao entrega, mas o OA-04 DO MODULO continua pedindo
  paleoclimatologia e ela segue SEM COBERTURA. Isso NAO foi resolvido aqui e NAO deve ser
  fabricado na revisao didatica: exige secao ou aula nova escrita pelo redator e submetida a
  auditoria. Registrado em didactic_review.open_findings no course-state.yaml.

mapa_objetivo_secao:
  geologia-avancado-m26-oa04: "A notação delta" + "Fracionamento dependente de massa: equilíbrio e cinética" + "δ34S em depósitos minerais" + "δ18O em petrogênese ígnea" + "Exemplo trabalhado"
  NOTA: esta aula cobre os ramos METALOGENESE e (parcialmente) petrogenese do OA-04. Os ramos
  QUIMIOESTRATIGRAFIA e CONTAMINACAO AMBIENTAL passaram para a Aula 07. O ramo PALEOCLIMATOLOGIA
  continua sem cobertura em todo o modulo - ver achado vermelho DID-2.

alegacoes_auditaveis:
  NOTA DE RASTREABILIDADE (2026-09-22): a divisao da aula manteve os claim_id ORIGINAIS, inclusive
  para os claims que passaram a viver no arquivo da Aula 07 (005, 006, 007, 008, 009, 010 e 013,
  todos com prefixo ISOGEO-M26-A06-). Os ids NAO foram renomeados para A07 de proposito: eles sao
  identificadores estaveis e o relatorio e o manifesto da auditoria de 2026-09-21 apontam para
  eles. Renomear invalidaria a rastreabilidade de uma auditoria ja fechada por uma mudanca que e
  de arquivo, nao de conteudo. Ficam nesta aula: 001, 002, 003, 004, 011 e 012.

  - claim_id: ISOGEO-M26-A06-NOTACAO-DELTA-PADROES-001
    claim: "A notacao delta e definida como delta = (R_amostra/R_padrao - 1) x 1000, em partes por mil; os padroes internacionais de referencia mantidos pela IAEA sao VSMOW (Vienna Standard Mean Ocean Water) para oxigenio e hidrogenio, VPDB (Vienna Pee Dee Belemnite) para carbono, VCDT (Vienna Canyon Diablo Troilite) para enxofre, e AIR (nitrogenio atmosferico) para nitrogenio."
    risk: fato
    source: "Convencao padrao de geoquimica de isotopos estaveis, amplamente documentada em Faure & Mensing (2005), Isotopes: Principles and Applications, 3a ed., Wiley, cap. 16-17, e em Hoefs, J., Stable Isotope Geochemistry. Nomes e origem historica dos padroes (VPDB de belemnite fossil da Formacao Pee Dee; VCDT de troilita do meteorito Canyon Diablo) sao conhecimento consolidado da area.
    ACHADO AMARELO 4 (auditoria 2026-09-21), claim ISOGEO-M26-A06-HOEFS-EDICAO-012: a lista de fontes desta aula creditava 'Hoefs, J. (2021), Stable Isotope Geochemistry, 8a ed., Springer'. O par ano/edicao esta errado: a edicao de 2021 e a NONA (Springer Textbooks in Earth Sciences, Geography and Environment, ISBN 978-3-030-77691-6, que declara discutir 47 elementos com variacao isotopica natural resolvivel); a 8a edicao e de 2018 (ISBN 978-3-319-78526-4). Corrigido para '9a ed.' mantendo o ano 2021, com o ISBN acrescentado para desambiguar. Severidade amarela, e nao laranja, porque a obra e a referencia certas - o que estava desatualizado era o numero da edicao, exatamente o tipo de erro que a redacao havia sinalizado como INCERTEZA DECLARADA.
    ACRESCIMO DA REVISAO DIDATICA (2026-09-22): o paragrafo final desta secao, dizendo que um valor delta so significa alguma coisa acoplado ao seu padrao e que um delta18O de +10 por mil contra VSMOW e contra VPDB sao afirmacoes diferentes, e consequencia direta da propria definicao ja auditada (delta e medido CONTRA um padrao); nao introduz fato novo nem valor numerico de conversao entre escalas."
  - claim_id: ISOGEO-M26-A06-FRACIONAMENTO-EQUILIBRIO-CINETICO-002
    claim: "Fracionamento de equilibrio isotopico entre duas fases depende da temperatura (menor fracionamento em temperaturas mais altas), base da geotermometria isotopica por pares minerais coexistentes; fracionamento cinetico ocorre em processos irreversiveis ou incompletos (evaporacao, reacoes bioquimicas, difusao), onde a especie mais leve reage ou se move mais rapido, produzindo fracionamentos frequentemente maiores e dependentes da taxa do processo. A fotossintese discrimina fortemente contra o 13C, deixando materia organica isotopicamente mais leve (delta13C mais negativo) que o CO2 atmosferico de origem."
    risk: fato
    source: "Principio fisico-quimico consolidado de fracionamento isotopico, amplamente documentado em Faure & Mensing (2005), cap. 16, e Hoefs, Stable Isotope Geochemistry. Mecanismo de discriminacao fotossintetica contra 13C e conhecimento padrao de bioquimica isotopica.
    ACRESCIMO DA REVISAO DIDATICA (2026-09-22): a frase de fecho ('um fracionamento de equilibrio registra uma temperatura; um cinetico registra a existencia de um processo') e reformulacao didatica do que a propria alegacao ja afirma, sem fato novo."
  - claim_id: ISOGEO-M26-A06-ENXOFRE-METALOGENESE-003
    claim: "Enxofre de fonte magmatica/mantelica em depositos ortomagmaticos de Ni-Cu-EGP e porfiros cupriferos tende a delta34S proximo de 0 +/- 2 por mil; reducao bacteriana de sulfato (RBS) discrimina fortemente contra 34S, produzindo sulfeto biogenico com delta34S tipicamente entre -10 e -40 por mil ou mais negativo, processo central na genese de depositos SEDEX e VMS com componente biogenico, onde o enxofre do minerio e mistura variavel de fonte hidrotermal/magmatica e biogenica."
    risk: fato
    source: "Principio geoquimico consolidado de metalogenese isotopica de enxofre, documentado em Faure & Mensing (2005), cap. 20 (isotopos de enxofre), e em literatura padrao de deposito mineral (Ohmoto & Rye, e sucessores). Faixas numericas (0+/-2 por mil magmatico; -10 a -40 por mil ou mais negativo biogenico) sao ordens de grandeza amplamente replicadas na literatura didatica, nao verificadas contra uma unica fonte primaria nesta redacao - risco considerado baixo pela consistencia entre multiplas fontes tercearias.
    ACRESCIMO DA REVISAO DIDATICA (2026-09-22): a frase que classifica a RBS como fracionamento CINETICO, e que atribui a magnitude do fracionamento a essa natureza, liga dois conteudos que a aula original ensinava separadamente sem nunca conecta-los. A classificacao da reducao bacteriana de sulfato como processo cinetico (biologico, irreversivel) segue diretamente da definicao de fracionamento cinetico ja auditada no claim 002, que lista 'reacoes bioquimicas' entre os processos cineticos. Sem fato novo."
  - claim_id: ISOGEO-M26-A06-DELTA18O-MANTELICO-ZIRCAO-004
    claim: "Zircoes de origem mantelica (kimberlitos, rochas maficas nao contaminadas) mostram delta18O aproximadamente 5,3 +/- 0,3 por mil (VSMOW), valor de referencia amplamente citado derivado de compilacoes de multiplos ambientes mantelicos; delta18O mais alto que o mantelico indica incorporacao de material crustal supracrustal reciclado (enriquecido em 18O por intemperismo/diagenese/alteracao de baixa temperatura), delta18O mais baixo indica interacao com agua meteorica circulada em alta temperatura."
    risk: fato
    source: "VERIFICADO por busca na redacao (2026-09-21): resultado de busca confirma 'The mantle range for zircon delta18O values is 5.3 +/- 0.3 permil (VSMOW)... the average delta18O of mantle zircons is 5.3 permil', associado a Valley, J.W. et al., Contributions to Mineralogy and Petrology. Interpretacao de desvios (crustal reciclado vs agua meteorica) e conhecimento consolidado de petrologia isotopica de oxigenio, documentado em Faure & Mensing (2005), cap. 18. CONFERIDO na auditoria (2026-09-21): Valley, J.W. et al. (2005), CMP 150(6), 561-580, doi 10.1007/s00410-005-0025-8, volume e paginacao confirmados.
    NOTA: a grafia 'Ziscoes' que constava deste registro foi corrigida para 'Zircoes' na revisao didatica (2026-09-22); erro de digitacao no metadado, sem efeito sobre o conteudo.
    ACRESCIMO DA REVISAO DIDATICA (2026-09-22): o paragrafo sobre Sr/Nd registrarem historia de LONGO PRAZO da fonte e o O registrar interacao de CURTO PRAZO com fluido, e sobre assinaturas discordantes entre eles serem informacao e nao contradicao, e sintese dos mecanismos ja auditados nas Aulas 03 (razao inicial de Sr acumulada por decaimento ao longo do tempo geologico), 04 (idem para epsilonNd) e desta secao (alteracao por fluido meteorico ou crustal). Nao introduz fato novo, apenas explicita a razao pela qual os tres tracadores nao sao redundantes - o que a aula original afirmava em uma linha sem desenvolver."
  - claim_id: ISOGEO-M26-A06-EXEMPLO-TRES-ESTAGIOS-SULFETO-011
    claim: "Para tres estagios hipoteticos de pirita com delta34S de -28,5 por mil (diagenetica precoce), +1,2 por mil (hidrotermal principal) e -9,8 por mil (tardia, borda de veio), a interpretacao consistente com os principios desta aula e: estagio 1 = reducao bacteriana de sulfato durante diagenese; estagio 2 = fonte magmatica/hidrotermal profunda sem fracionamento biologico significativo; estagio 3 = mistura entre fluido hidrotermal principal e enxofre biogenico local incorporado da rocha encaixante."
    risk: interpretacao
    source: "Dados de entrada (os tres valores de delta34S) sao hipoteticos, construidos especificamente para este exemplo pedagogico e nao correspondem a um deposito real analisado. A interpretacao segue diretamente os principios de fracionamento de enxofre em metalogenese apresentados nesta aula (claim ISOGEO-M26-A06-ENXOFRE-METALOGENESE-003) e e logicamente consistente com eles, mas e um exercicio de aplicacao didatica, nao um resultado publicado.
    ACRESCIMO DA REVISAO DIDATICA (2026-09-22): o paragrafo 'O que o exemplo nao permite concluir' delimita o alcance da inferencia (duas fontes, sim; proporcao numerica da mistura, nao). E uma restricao epistemica sobre o proprio exemplo, mais conservadora que o texto original, e nao afirma nenhum fato geologico novo."
-->
