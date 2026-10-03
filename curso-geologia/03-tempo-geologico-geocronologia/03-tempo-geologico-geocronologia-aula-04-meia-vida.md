# Aula 04: Meia-vida — o relógio que não se pode adiantar

**ID:** geologia-m03-a04
**Módulo:** [[03-tempo-geologico-geocronologia-modulo|Módulo 03 — Tempo geológico e geocronologia]]
**Duração estimada:** ~30 min
**Nível:** iniciante (contrato `iniciante-absoluto-v1`)
**Objetivo:** entender o que é meia-vida, por que ela transforma o decaimento num cronômetro, e calcular idades simples contando divisões pela metade.

## Antes de começar, você precisa saber

- O que são **átomo, isótopo, pai e filho**, e o que é **decaimento** — [[03-tempo-geologico-geocronologia-aula-03-ponte-atomos-e-isotopos|aula 03 (ponte)]]. Esta aula é inútil sem aquela.
- Que o decaimento é **aleatório por átomo e regular por população**, e **imune a temperatura, pressão e química** — mesma aula.
- Ler **potências de dez** — [[00-partida-do-zero-aula-03-ordens-de-grandeza|módulo 00, aula 03]].

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **Meia-vida** | O tempo em que **metade** dos átomos-pai de uma amostra decai. |
| **Razão pai/filho** | Quantos átomos-pai restam para cada átomo-filho acumulado. |
| **Constante do isótopo** | Valor fixo, próprio de cada isótopo radioativo, que não varia. |
| **Idade absoluta** | Idade expressa em anos, e não apenas como "mais velho que". |
| **Ma** | Abreviação de milhões de anos. |
| **Ga** | Abreviação de bilhões de anos. |
| **Sistema fechado** | Amostra em que nada de pai nem de filho entrou ou saiu desde a formação. |

## Conteúdo

### O problema de contar átomos que somem

A aula anterior estabeleceu que átomos instáveis decaem a um ritmo fixo, imune a tudo o que a geologia possa fazer com a rocha. Falta transformar isso em relógio.

E aparece uma dificuldade de saída. O decaimento não é como uma vela que queima tantos centímetros por hora. Se ele fosse assim — uma quantidade fixa por ano — os átomos acabariam numa data marcada, e o relógio simplesmente pararia de existir.

Não é isso que acontece. O que é fixo não é **quanto** decai por ano, mas a **fração** que decai por ano.

Uma analogia. Imagine que, todo ano, uma cidade perde 5% dos habitantes. No primeiro ano, com 1.000 pessoas, saem 50. No ano seguinte, com 950, saem 47 — menos gente, porque 5% de um número menor é um número menor. **A porcentagem é constante; a quantidade absoluta diminui sempre.**

Os átomos radioativos se comportam exatamente assim. E daí sai uma consequência elegante:

> **Se a fração que decai por ano é constante, então o tempo para desaparecer qualquer fração fixa também é constante.**

Em particular, o tempo para desaparecer **metade** é sempre o mesmo. Esse tempo é a **meia-vida**.

### O que a meia-vida é — e o que ela não é

**Meia-vida** é o tempo necessário para que metade dos átomos-pai de uma amostra tenha decaído.

O ponto que confunde quase todo mundo é que **ela não se esgota**. Vale a tabela:

| Meias-vidas passadas | Pai restante | Filho acumulado |
|---|---|---|
| 0 | 100% | 0% |
| 1 | 50% | 50% |
| 2 | 25% | 75% |
| 3 | 12,5% | 87,5% |
| 4 | 6,25% | 93,75% |
| 5 | 3,125% | 96,875% |
| 10 | ~0,1% | ~99,9% |

Repare: depois de duas meias-vidas **não** sobra zero. Sobra um quarto. A segunda meia-vida não consome a outra metade original — ela consome metade **do que restava**.

> [!warning] O erro número um do assunto **Duas meias-vidas não significam "acabou".** Cada meia-vida corta pela metade o que sobrou, não o que havia no início. Em teoria a quantidade nunca chega a zero; na prática, ela fica pequena demais para ser medida — e é isso que define o **limite** de cada método.

Uma imagem que ajuda: uma folha de papel dobrada ao meio, depois ao meio de novo, e de novo. Cada dobra reduz à metade da anterior. Você pode dobrar muitas vezes e nunca chegar a "nada" — só a algo fino demais para manusear.

### Cada isótopo tem a sua, e elas variam enormemente

A meia-vida é uma **constante do isótopo**. Não do elemento, não da rocha, não do lugar: do isótopo. E os valores cobrem uma faixa gigantesca:

| Sistema pai → filho | Meia-vida (ordem de grandeza) | Serve para datar |
|---|---|---|
| carbono-14 → nitrogênio-14 | ~5,7 mil anos | material orgânico recente |
| urânio-235 → chumbo-207 | ~700 Ma | rochas antigas |
| potássio-40 → argônio-40 | ~1,25 Ga | rochas vulcânicas |
| urânio-238 → chumbo-206 | ~4,5 Ga | rochas muito antigas |
| rubídio-87 → estrôncio-87 | ~49 Ga | rochas muito antigas |

Daí sai a regra prática mais útil da geocronologia:

> [!tip] Escolha o relógio pela ordem de grandeza do que quer medir **A meia-vida tem que ser comparável à idade que se quer determinar.** - Meia-vida **curta demais** para o alvo: o pai já sumiu por completo, e não há o que medir. Por isso carbono-14 **não serve** para datar dinossauros: passados dezenas de milhares de anos, praticamente não resta ¹⁴C. - Meia-vida **longa demais**: quase nada decaiu ainda, o filho acumulado é pequeno demais para se distinguir de zero, e a incerteza engole o resultado. O relógio certo é o que já rodou algumas voltas, mas não terminou.

Note também um ponto que costuma passar batido: **o carbono-14 quase não é usado em geologia**. Ele cobre alguns milhares a algumas dezenas de milhares de anos — o piscar de olhos final do tempo geológico. Datar rochas é trabalho de urânio, potássio e rubídio.

### O truque que faz tudo funcionar: a razão

Falta resolver um problema que parece fatal. Para saber quanto pai decaiu, seria preciso saber **quanto pai havia no começo**. E ninguém estava lá para medir.

A saída é bonita: **não se mede o pai sozinho — mede-se o pai e o filho, e se olha a razão entre eles.**

Cada átomo-pai que decai vira exatamente um átomo-filho. Nada se perde. Então:

- **Muito pai e pouco filho** → decaiu pouco → **amostra jovem**.
- **Metade de cada** → passou-se **uma meia-vida**.
- **Pouco pai e muito filho** → decaiu muito → **amostra antiga**.

E aqui está o essencial: essa leitura **não exige saber a quantidade inicial**. Pai e filho, somados, dão a quantidade inicial. A amostra carrega a própria referência dentro de si.

Isso, porém, só é verdade sob uma condição, e ela é a mais importante desta aula:

> [!warning] A condição de sistema fechado A conta só vale se, desde a formação da rocha, **nenhum átomo de pai ou de filho entrou ou saiu** da amostra. Se o filho vazou, sobra pouco filho, e a rocha parece **mais jovem** do que é. Se filho entrou de fora, ela parece **mais velha**. Lembre da aula 03: o **ritmo** do relógio é inalterável — mas a **contagem** pode ser adulterada por processos geológicos que movimentam átomos. Nada disso é falha do método; é a realidade do material. Toda a aula 05 trata disso.

### O que a idade obtida significa

Ainda um cuidado. Quando um laboratório entrega "esta rocha tem 200 Ma", o que foi datado, estritamente, é **o momento em que o relógio começou a contar** — isto é, quando o mineral passou a reter o filho em vez de deixá-lo escapar.

Para uma rocha vulcânica, isso é praticamente o momento em que ela esfriou, e portanto a idade **de formação**. Mas para uma rocha que foi aquecida depois, o relógio pode ter sido **rezerado**, e a idade obtida é a do aquecimento, não a da formação.

Ou seja: **a datação responde "quando o relógio zerou", e cabe ao geólogo saber que evento foi esse.** É a diferença entre um número e um resultado.

> [!note] Sobre a matemática Contar meias-vidas inteiras é aritmética simples, e é o que fazemos aqui. Para uma razão qualquer — "restam 37% do pai" — a conta exige **logaritmo**, ferramenta que este curso ainda não ensinou. Sob a regra LC-06, ela não vai aparecer sem aula-ponte: a fórmula geral e o tratamento de incertezas ficam para o **módulo 09**.

## Exemplo trabalhado

**Situação:** um mineral vulcânico é analisado. Mede-se que **12,5% do potássio-40 original** ainda está presente, e o restante virou filho. A meia-vida do potássio-40 é de cerca de 1,25 Ga. Qual a idade?

**Passo 1 — quantas meias-vidas correspondem a 12,5%?** Conte as divisões pela metade:
- 100% → 50% ..... 1 meia-vida
- 50% → 25% ...... 2 meias-vidas
- 25% → 12,5% .... **3 meias-vidas**

**Passo 2 — multiplique.** 3 × 1,25 Ga = **3,75 Ga**.

**Passo 3 — verifique se o relógio é adequado.** 3 meias-vidas é uma leitura excelente: já decaiu o bastante para o filho ser abundante e bem medido, e ainda resta pai suficiente para ser detectado com segurança. Relógio bem escolhido.

**Passo 4 — verifique a plausibilidade geológica.** 3,75 Ga é uma idade muito grande, porém possível: a Terra tem cerca de 4,54 Ga, e existem rochas conhecidas nessa faixa. Se o resultado tivesse dado 6 Ga, algo estaria errado — nenhuma rocha terrestre pode ser mais velha que o planeta. **Sempre confira o número contra o que é fisicamente possível.**

**Passo 5 — declare o que foi datado.** O resultado data o momento em que este mineral passou a reter o filho. Para um mineral vulcânico não reaquecido, isso corresponde ao resfriamento — a idade de formação da rocha.

**Contraexemplo, para fixar o erro comum.** Se alguém dissesse "restam 12,5%, então já se passaram 12,5% do tempo" ou "sobrou pouco, então é quase uma meia-vida", estaria raciocinando de forma linear. **O decaimento não é linear.** Sobrar 12,5% significa **três** cortes pela metade, não uma fração pequena do caminho.

## Erros comuns

- **Achar que após duas meias-vidas não sobra nada.** Sobra 25%.
- **Achar que meia-vida é "metade do tempo de vida" do átomo.** É o tempo para metade da **população** decair.
- **Achar que o decaimento é linear.** Cada meia-vida corta o **restante**, não o original.
- **Usar carbono-14 para datar rochas.** Meia-vida curta demais por ordens de grandeza.
- **Achar que é preciso conhecer a quantidade inicial.** Não é: mede-se a **razão** pai/filho, e pai + filho reconstroem o inicial.
- **Achar que aquecer a rocha acelera o decaimento.** Não acelera o relógio — mas pode **zerá-lo**, deixando o filho escapar. São coisas diferentes.
- **Tratar a idade obtida como "idade da rocha" sem perguntar qual evento zerou o relógio.**

## O que não concluir

- **Que toda datação dá a idade de formação.** Dá a idade do **fechamento do sistema** para aquele mineral e aquele isótopo. Interpretar isso é o trabalho da aula 05.
- **Que a meia-vida é conhecida com precisão infinita.** É medida experimentalmente e tem incerteza própria, que entra na incerteza da idade. Módulo 09.
- **Que uma única datação basta.** A prática é datar vários minerais e vários sistemas e exigir concordância. Uma idade isolada é uma hipótese.
- **Que "3,75 Ga" é um número exato.** Toda idade radiométrica vem com uma margem, e reportá-la sem margem é reportá-la errado.
- **Que a condição de sistema fechado é sempre satisfeita.** Ela frequentemente **não** é. Reconhecer isso é a competência da próxima aula.

## Recap relâmpago

- O que é constante no decaimento é a **fração** que decai por ano, não a quantidade.
- **Meia-vida** = tempo para **metade** dos átomos-pai decair. É constante do **isótopo**.
- Cada meia-vida corta pela metade **o que restou**: 50%, 25%, 12,5%, 6,25%… **Nunca chega a zero.**
- As meias-vidas variam de milhares a dezenas de bilhões de anos.
- **Escolha o relógio pela ordem de grandeza do alvo.** ¹⁴C não data rochas.
- Mede-se a **razão pai/filho** — por isso não é preciso saber a quantidade inicial.
- Tudo depende da condição de **sistema fechado**: nada de pai nem de filho entrou ou saiu.
- A idade obtida é a do **fechamento do relógio**, e cabe ao geólogo dizer que evento foi esse.
- Razões que não são meias-vidas inteiras exigem **logaritmo** — deferido ao módulo 09.

## Próxima aula

[[03-tempo-geologico-geocronologia-aula-05-datacao-na-pratica|Aula 05 — Datação radiométrica na prática: o que se data e o que dá errado]]

## Anterior

[[03-tempo-geologico-geocronologia-aula-03-ponte-atomos-e-isotopos|Aula 03 (ponte) — Átomos, isótopos e radioatividade]]

## Fontes

- Valores de meia-vida: tabelas de nuclídeos de referência; ordens de grandeza conforme a regra LC-05.
- Idade da Terra (~4,54 Ga): C. Patterson, 1956 — desenvolvido na aula 07.

<!--
nivel: iniciante-absoluto-v1
palavras_corpo: ~1600

mapa_objetivo_secao:
  OA-04: "O problema de contar átomos que somem" + "O que a meia-vida é" + "Cada isótopo tem a sua" + "O truque que faz tudo funcionar: a razão" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEO-M03-A04-MEIA-VIDA-DEF-001
    claim: "Meia-vida é o intervalo em que metade dos átomos-pai de uma população decai, e é constante para cada isótopo."
    risk: fato
    source: "física nuclear consolidada"
  - claim_id: GEO-M03-A04-SERIE-002
    claim: "Após 1, 2, 3, 4 e 5 meias-vidas restam respectivamente 50%, 25%, 12,5%, 6,25% e 3,125% do isótopo-pai."
    risk: numero
    source: "cálculo aritmético direto por divisões sucessivas"
  - claim_id: GEO-M03-A04-VALORES-MEIA-VIDA-003
    claim: "Meias-vidas de referência: carbono-14 ~5,7 mil anos; urânio-235 ~700 Ma; potássio-40 ~1,25 Ga; urânio-238 ~4,5 Ga; rubídio-87 ~49 Ga."
    risk: numero
    source: "tabelas de nuclídeos; ordem de grandeza conforme LC-05. Valor de Rb-87 revisado na literatura recente — a aula usa ordem de grandeza justamente por isso"
  - claim_id: GEO-M03-A04-C14-NAO-ROCHAS-004
    claim: "O carbono-14 não serve para datar rochas nem material de idade geológica, por ter meia-vida curta demais."
    risk: interpretacao
    source: "limite prático do método em torno de algumas dezenas de milhares de anos"
  - claim_id: GEO-M03-A04-RAZAO-005
    claim: "A datação usa a razão pai/filho, o que dispensa conhecer a quantidade inicial de pai, já que pai mais filho reconstroem o total inicial."
    risk: interpretacao
    source: "princípio da geocronologia. Pressupõe ausência de filho inicial — hipótese tratada na aula 05 e corrigida por isócrona no M09"
  - claim_id: GEO-M03-A04-SISTEMA-FECHADO-006
    claim: "A validade da idade depende da condição de sistema fechado para pai e filho desde a formação."
    risk: interpretacao
    source: "premissa central da geocronologia; desenvolvida na aula 05"
  - claim_id: GEO-M03-A04-IDADE-FECHAMENTO-007
    claim: "Uma idade radiométrica data o fechamento do sistema isotópico, que pode ou não coincidir com a formação da rocha."
    risk: interpretacao
    source: "conceito de temperatura de fechamento; desenvolvido na aula 05"
  - claim_id: GEO-M03-A04-IDADE-TERRA-008
    claim: "A Terra tem cerca de 4,54 bilhões de anos, o que impõe um teto de plausibilidade a qualquer idade de rocha terrestre."
    risk: numero
    source: "Patterson 1956; valor consolidado. Ordem de grandeza conforme LC-05"

nota_repartida: >-
  Aula nova da repartida de 2026-08-16. Corresponde ao segundo terço da antiga aula
  02 (decaimento-radioativo-e-datacao-radiometrica). Sob a regra LC-06, a fórmula
  exponencial e o uso de logaritmo foram removidos: a aula trabalha por contagem de
  divisões pela metade, e o tratamento geral fica deferido ao M09 junto com
  isócronas e incertezas.
-->
