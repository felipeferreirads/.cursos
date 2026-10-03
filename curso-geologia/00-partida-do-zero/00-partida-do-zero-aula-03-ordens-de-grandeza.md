# Aula 03: Tamanhos e tempos — ordens de grandeza sem susto

**ID:** geologia-m00-a03
**Módulo:** [[00-partida-do-zero-modulo|Módulo 00 — Partida do zero: o kit de sobrevivência]]
**Duração estimada:** ~30 min
**Nível:** iniciante (contrato `iniciante-absoluto-v1`)
**Objetivo:** ler e escrever potências de dez, comparar números por ordem de grandeza, e sentir na pele a diferença entre um milhão e um bilhão de anos.

## Antes de começar, você precisa saber

Só aritmética de escola: multiplicar e dividir por 10. Nada além disso.

> [!info] Esta aula não tem geologia Ela é uma **ferramenta**. Praticamente toda aula do curso usa números que não cabem na intuição — 4,54 bilhões de anos, 2.900 quilômetros, 0,002 milímetro. Sem esta aula, esses números viram ruído: o aluno lê "muito grande" e segue. Com ela, eles voltam a significar alguma coisa.

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **Potência de dez** | Um 1 seguido de zeros, escrito de forma curta: 10³ = 1.000. |
| **Expoente** | O número pequeno lá em cima. Ele conta **quantos zeros**. |
| **Notação científica** | Escrever um número como "um algarismo, vírgula, resto × 10 elevado a alguma coisa". |
| **Ordem de grandeza** | Em que casa de potência de dez o número mora. Compara-se por "quantos dez vezes maior". |
| **Ma** | Milhões de anos. Abreviação padrão em geologia. |
| **Ga** | Bilhões de anos (mil milhões). |
| **µm (micrômetro)** | Um milésimo de milímetro. |

## Conteúdo

### O problema: números grandes se parecem todos

Leia as duas frases:

> *"Aquele evento ocorreu há 65 milhões de anos."* *"Aquele evento ocorreu há 65 bilhões de anos."*

A segunda é absurda — é mais velha que o próprio universo. Mas as duas frases *soam* igual, e é por isso que a segunda passa despercebida. O cérebro humano lê números acima de alguns milhares como uma única categoria: **"muito"**.

Isso é um problema sério em geologia, porque a diferença entre milhão e bilhão é exatamente a diferença entre o surgimento dos mamíferos modernos e a formação do planeta. Não é detalhe: é toda a matéria.

A ferramenta que resolve isso é contar **zeros** em vez de ler nomes.

### Potência de dez: o expoente conta os zeros

Escrever 1.000.000.000 é ruim: ninguém confere aqueles zeros. Escrevemos 10⁹.

A regra é literalmente esta: **o expoente é a quantidade de zeros.**

| Escrito por extenso | Potência | Nome |
|---|---|---|
| 1 | 10⁰ | um |
| 1.000 | 10³ | mil |
| 1.000.000 | 10⁶ | milhão |
| 1.000.000.000 | 10⁹ | bilhão |
| 1.000.000.000.000 | 10¹² | trilhão |

E para o lado pequeno, o expoente fica **negativo** e conta as casas depois da vírgula:

| Escrito | Potência | Nome |
|---|---|---|
| 0,1 | 10⁻¹ | um décimo |
| 0,001 | 10⁻³ | um milésimo (é o milímetro em metros) |
| 0,000001 | 10⁻⁶ | um milionésimo (é o micrômetro em metros) |

Duas coisas que economizam muito esforço:

**Primeira: para multiplicar potências de dez, some os expoentes.** 10³ × 10⁶ = 10⁹. Mil vezes um milhão é um bilhão. Você não precisou contar zero nenhum.

**Segunda: para dividir, subtraia.** 10⁹ ÷ 10⁶ = 10³. Um bilhão é **mil vezes** um milhão. Guarde essa: é a resposta à pergunta que abriu a aula.

### Notação científica: potência de dez para números que não são redondos

A Terra tem cerca de 4.540.000.000 anos. Ninguém quer escrever isso.

Em **notação científica**, todo número vira duas peças: um algarismo, vírgula e o resto — depois, "vezes dez elevado a alguma coisa".

> 4.540.000.000 = **4,54 × 10⁹**

O jeito de fazer é mecânico. Ponha a vírgula logo depois do primeiro algarismo e conte quantas casas ela andou. O número de casas é o expoente.

- 4.540.000.000 → a vírgula anda **9** casas para a esquerda → 4,54 × 10⁹
- 2.900 → anda **3** casas → 2,9 × 10³
- 0,0025 → anda **3** casas para a **direita**, então o expoente é negativo → 2,5 × 10⁻³

Uma vez nessa forma, dois números se comparam **na hora**: olhe primeiro os expoentes. 4,54 × 10⁹ contra 6,5 × 10⁷? Nem precisa olhar o 4,54 e o 6,5 — nove é maior que sete, e cada degrau de expoente vale dez vezes. O primeiro é umas cem vezes maior.

Isso é ler por **ordem de grandeza**: não perguntar *"quanto exatamente?"*, mas *"em que casa esse número mora?"*.

> [!tip] Por que este curso prefere ordem de grandeza Você vai reparar que as aulas dizem "cerca de 2.900 km" e não "2.891 km". É de propósito, e é uma regra escrita do curso (LC-05). A razão é dupla. Primeira, para quem aprende, o algarismo extra não acrescenta entendimento — só peso. Segunda, valores precisos mudam quando as medições melhoram, e um curso cheio deles envelhece rápido. A ordem de grandeza, não. A precisão de laboratório entra depois, no módulo que ensina **como** se mede (M19).

### As unidades de tempo da geologia

Em geologia, o tempo se conta com duas abreviações, e elas aparecem em toda tabela e em todo artigo. Vale fixar agora:

| Abreviação | Significa | Em potência |
|---|---|---|
| **ka** | milhares de anos | 10³ anos |
| **Ma** | milhões de anos | 10⁶ anos |
| **Ga** | bilhões de anos | 10⁹ anos |

Alguns marcos do curso, escritos nas três formas, só para o olho se acostumar:

| Evento | Idade aproximada | Notação |
|---|---|---|
| Formação da Terra | ~4.540 Ma = ~4,54 Ga | 4,54 × 10⁹ anos |
| Rochas mais antigas preservadas | ~4.000 Ma = ~4,0 Ga | 4,0 × 10⁹ anos |
| Começo do Cambriano | ~539 Ma | 5,39 × 10⁸ anos |
| Fim dos dinossauros não-avianos | ~66 Ma | 6,6 × 10⁷ anos |
| Última era glacial no auge | ~20 ka | 2,0 × 10⁴ anos |

Repare no que a coluna da direita denuncia. Entre a formação da Terra (10⁹) e o fim dos dinossauros (10⁷) há **dois degraus** de expoente — ou seja, um fator de cem. Os dinossauros, que a intuição coloca no "começo de tudo", estão **quase no fim** da história do planeta.

### Fazendo o tempo profundo caber na cabeça

Números não resolvem sozinhos. É preciso traduzi-los para alguma coisa que o corpo conheça.

**A tradução mais eficiente é para segundos.**

- 1 milhão de segundos = cerca de **11 dias e meio**.
- 1 bilhão de segundos = cerca de **32 anos**.

Pare aqui um instante, porque essa comparação é a aula inteira. Um milhão de segundos é uma viagem; um bilhão de segundos é a metade de uma vida adulta. Se você tivesse começado a contar um número por segundo no dia em que nasceu, ainda não teria chegado ao primeiro bilhão.

**Mil vezes.** É o que separa um milhão de um bilhão. Agora aplique isso: quando uma aula disser que uma rocha tem 3 Ga e outra tem 3 Ma, elas não são "as duas velhas". A primeira é **mil vezes** mais velha que a segunda.

Uma segunda tradução, agora para distância — e esta é útil porque você pode andar:

> Marque **4,54 metros** no chão. Cada metro vale 1 bilhão de anos; cada milímetro vale 1 milhão de anos. - O tempo todo dos dinossauros ocupa os **últimos ~17 centímetros**. - O gênero *Homo* ocupa os **últimos ~3 milímetros**. - Toda a história escrita cabe em **cinco milésimos de milímetro** — um traço que você não consegue desenhar nem enxergar.

Esse exercício reaparece com outra régua no módulo 03. Não é repetição: cada régua expõe uma distorção diferente da intuição.

### O outro extremo: o mundo pequeno

A geologia também desce muito. Vale ancorar a escala pequena com objetos conhecidos:

| Escala | Referência que você conhece |
|---|---|
| **1 mm** = 10⁻³ m | um grão de areia grosso |
| **0,06 mm** = 6 × 10⁻⁵ m | fronteira aproximada entre areia e silte: onde o grão deixa de ser visto a olho nu |
| **1 µm** = 10⁻⁶ m | grãos de argila e poeira fina |
| **~0,1 nm** = 10⁻¹⁰ m | o tamanho de um átomo |

O último é a razão de esta aula existir tão cedo. Entre um átomo (10⁻¹⁰ m) e o raio da Terra (~6,4 × 10⁶ m) há **dezesseis degraus** de potência de dez. Este curso vai percorrer essa faixa inteira — do arranjo dos átomos num cristal (M04) à estrutura do planeta (M02) — e frequentemente **na mesma aula**. A notação é o que permite trocar de escala sem se perder.

## Exemplo trabalhado

**Situação:** quatro perguntas de ordem de grandeza. Resolva por expoente, sem calculadora.

**(a) Uma placa tectônica se move ~5 cm por ano. Quanto em 1 milhão de anos?** 5 cm × 10⁶ = 5 × 10⁶ cm. Agora converta: 1 km = 10⁵ cm. Então 5 × 10⁶ ÷ 10⁵ = 5 × 10¹ = **50 km**. *O que isso ensina:* uma taxa ridícula na escala humana — a unha cresce mais rápido — vira 50 km num piscar de olhos geológico. E em 100 Ma, **5.000 km**: a largura de um oceano. É assim que continentes se separam.

**(b) Um rio deposita 0,1 mm de sedimento por ano. Que espessura em 10 Ma?** 0,1 mm × 10⁷ = 10⁶ mm. Como 1 km = 10⁶ mm, isso dá **1 km** de sedimento. *O que isso ensina:* pilhas sedimentares de quilômetros não exigem catástrofe nenhuma. Exigem só tempo, e nada de extraordinário acontecendo.

**(c) Um fóssil tem 500 Ma; outro tem 500 ka. Quantas vezes mais velho é o primeiro?** 500 Ma = 5 × 10⁸ anos; 500 ka = 5 × 10⁵ anos. Subtraia os expoentes: 10⁸ ÷ 10⁵ = 10³. **Mil vezes mais velho.** *O que isso ensina:* dois números que começam com "500" podem estar separados por um fator de mil. Ler o nome da unidade é obrigatório; ler só o algarismo engana.

**(d) Um cristal cresce 1 µm por ano. Quanto tempo para chegar a 1 cm?** 1 cm = 10⁻² m; 1 µm = 10⁻⁶ m. Divida: 10⁻² ÷ 10⁻⁶ = 10⁴. **Dez mil anos.** *O que isso ensina:* o cristal grande da aula 02 não é figura de linguagem. "Esfriou devagar" pode significar dezenas de milhares de anos.

**A lição:** em todos os quatro casos, a conta foi **somar ou subtrair expoentes**. Nenhuma exigiu calculadora, e todas produziram um número que se pode discutir. Essa é a competência.

## Erros comuns

- **Tratar milhão e bilhão como "os dois muito".** Bilhão é **mil vezes** milhão.
- **Confundir Ma com ka.** Um fator de mil escondido em duas letras.
- **Multiplicar expoentes em vez de somar.** 10³ × 10⁶ é 10⁹, não 10¹⁸.
- **Achar que expoente negativo significa número negativo.** 10⁻³ é 0,001 — pequeno e positivo.
- **Comparar os algarismos antes dos expoentes.** 6,5 × 10⁷ é bem menor que 4,54 × 10⁹, mesmo começando com um número maior. **Expoente primeiro, sempre.**
- **Copiar todos os algarismos de uma fonte.** Escrever 4.543.000.000 quando "cerca de 4,54 bilhões" é o que se sabe é falsa precisão — sugere uma certeza que a medição não tem.

## O que não concluir

- **Que "cerca de" é preguiça.** É honestidade. Toda idade geológica vem com uma margem de erro, e escrever mais algarismos do que a margem permite é afirmar mais do que se sabe. O módulo 03 trata de onde vem essa margem.
- **Que o exercício dos 4,54 metros é uma medição.** É um recurso de escala, com arredondamento deliberado. Serve para calibrar a intuição, não para citar.
- **Que taxas atuais podem ser projetadas para trás sem cuidado.** As contas (a) e (b) supõem taxa constante, o que quase nunca é verdade em geologia real. A conta dá a **ordem de grandeza**, não o valor. O módulo 01 discute exatamente esse limite.
- **Que "bilhão" quer dizer o mesmo em toda língua.** Em português e no inglês contemporâneo, bilhão é 10⁹. Em alguns usos europeus tradicionais, "billion" já significou 10¹². Ao ler fonte antiga ou traduzida, confira o número, não o nome.

## Recap relâmpago

- **O expoente conta os zeros.** 10⁶ = milhão; 10⁹ = bilhão.
- **Multiplicar = somar expoentes; dividir = subtrair.**
- **Notação científica:** um algarismo, vírgula, resto × 10 elevado ao número de casas que a vírgula andou.
- **Compare pelo expoente primeiro.** Cada degrau vale dez vezes.
- **ka = 10³ anos · Ma = 10⁶ anos · Ga = 10⁹ anos.**
- **Um bilhão é mil vezes um milhão.** Em segundos: 11 dias e meio contra 32 anos.
- Régua de **4,54 m** para a idade da Terra: dinossauros nos últimos ~17 cm; *Homo* nos últimos ~3 mm; história escrita, invisível.
- Do átomo (10⁻¹⁰ m) ao raio da Terra (10⁶ m) são **16 degraus** — a faixa que o curso percorre.
- **Ordem de grandeza é a moeda deste curso**; precisão de laboratório vem no M19.

## Anterior

[[00-partida-do-zero-aula-02-tres-tipos-de-rocha|Aula 02 — Os três tipos de rocha, em visão panorâmica]]

## Próxima aula

[[00-partida-do-zero-aula-04-terra-por-dentro|Aula 04 — A Terra por dentro, em desenho]], primeira aplicação direta desta ferramenta: você vai lidar com milhares de quilômetros e vai precisar saber o que significam.

## Fontes

- Bureau International des Poids et Mesures (BIPM) — Sistema Internacional de Unidades: prefixos e notação.
- International Commission on Stratigraphy — [stratigraphy.org](https://stratigraphy.org/) (uso de ka, Ma e Ga; idades de referência da carta).
- Cálculos aritméticos diretos, verificáveis pelo leitor.

<!--
nivel: iniciante-absoluto-v1
palavras_corpo: ~1470  # medido: conteudo + exemplo trabalhado; teto LC-02 = 1.600

mapa_objetivo_secao:
  OA-03: "O problema" + "Potência de dez" + "Notação científica" + "As unidades de tempo" + "Fazendo o tempo profundo caber na cabeça" + "O outro extremo" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEO-M00-A03-NOTACAO-001
    claim: "Em notação de potências de dez, o expoente corresponde ao número de casas decimais deslocadas; multiplicação soma expoentes e divisão os subtrai."
    risk: fato
    source: "aritmética elementar; verificável"
  - claim_id: GEO-M00-A03-UNIDADES-TEMPO-002
    claim: "Em geociências, ka designa milhares de anos (10³), Ma milhões (10⁶) e Ga bilhões (10⁹)."
    risk: definicao
    source: "convenção adotada pela ICS e pela literatura geocronológica"
  - claim_id: GEO-M00-A03-IDADE-TERRA-003
    claim: "A Terra tem cerca de 4,54 bilhões de anos (4,54 Ga)."
    risk: numero
    source: "valor consolidado por datação de meteoritos. Ordem de grandeza conforme LC-05; verificar consistência com M01-a04 e M03-a05"
  - claim_id: GEO-M00-A03-MARCOS-004
    claim: "Marcos usados: rochas mais antigas preservadas ~4,0 Ga; base do Cambriano ~539 Ma; extinção dos dinossauros não-avianos ~66 Ma; máximo da última glaciação ~20 ka."
    risk: numero
    source: "ICS, carta cronoestratigráfica internacional v2024/12 — base do Cambriano 538,8 ± 0,6 Ma (GSSP de Fortune Head, Terra Nova); limite K-Pg 66,0 Ma. Máximo da última glaciação ~20 ka: literatura quaternária. A idade da rocha mais antiga preservada relaciona-se ao achado aberto M01-F02 (Acasta x Nuvvuagittuq): a aula usa ordem de grandeza justamente para não arbitrar a disputa"
    auditoria_2026-08-16: "placeholder CONFERIR VERSÃO resolvido; valores conferidos contra a carta ICS v2024/12 e mantidos"
  - claim_id: GEO-M00-A03-SEGUNDOS-005
    claim: "Um milhão de segundos corresponde a cerca de 11,6 dias e um bilhão de segundos a cerca de 31,7 anos."
    risk: numero
    source: "cálculo aritmético direto (10⁶/86400 e 10⁹/31.557.600)"
  - claim_id: GEO-M00-A03-REGUA-006
    claim: "Numa régua de 4,54 metros para a idade da Terra (1 mm = 1 Ma), a era dos dinossauros ocupa cerca de 17 cm e o gênero Homo cerca de 3 mm."
    risk: numero
    source: "cálculo aritmético direto; recurso didático arredondado, declarado como tal. Régua distinta da usada em M01-a06 e M03-a07 — verificar na auditoria que as três não se contradizem"
  - claim_id: GEO-M00-A03-ESCALA-GRAO-007
    claim: "A fronteira granulométrica entre areia e silte situa-se em torno de 0,06 mm, próximo do limite de resolução do olho nu."
    risk: numero
    source: "escala de Wentworth (limite areia/silte em 1/16 mm = 0,0625 mm); detalhado no M07"
  - claim_id: GEO-M00-A03-BILHAO-AMBIGUO-008
    claim: "O termo bilhão designa 10⁹ em português e no inglês contemporâneo, mas já designou 10¹² em usos europeus tradicionais."
    risk: fato
    source: "escala curta x escala longa; alerta de leitura de fontes antigas"

nota_repartida: >-
  Aula-ferramenta nova, criada na repartida de 2026-08-16. É o alvo de wikilink mais
  citado do módulo 00 junto com a aula 02 (5 ocorrências: 01-a04, 01-a06, 03-a03,
  03-a04, 03-a07) — o nome do arquivo é contrato. Ela é o pré-requisito operacional
  da regra LC-05 e da aula-ponte de meia-vida do M03: sem potências de dez, o M03-a04
  não tem como funcionar sem logaritmo, que LC-06 proíbe naquele nível.
-->
