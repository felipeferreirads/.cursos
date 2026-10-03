# Aula 03: Propriedades de rocha-reservatório e de fluidos (PVT) e cálculo de volumes in place

**ID:** geologia-avancado-m12-a03
**Módulo:** [[12-engenharia-de-petroleo-modulo|Módulo 12 — Engenharia de petróleo]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** relacionar as propriedades físicas de rocha-reservatório (porosidade, saturação, permeabilidade) e de fluido (fator volume-formação, razão de solubilidade) ao cálculo do volume de óleo e gás originalmente presente no reservatório.
**Ao final você vai conseguir:** distinguir porosidade e permeabilidade e explicar por que uma rocha pode ter uma sem ter a outra; interpretar um relatório PVT básico (Bo, Rs); e calcular o volume de óleo original in place (OOIP) de um reservatório a partir de área, espessura, porosidade, saturação e fator volume-formação.
**Pré-requisito:** Aula 02 deste módulo — porosidade (φ) e saturação de água (Sw) obtidas de perfis, incluindo a equação de Archie.

## Conteúdo

### Porosidade e permeabilidade: propriedades independentes, frequentemente confundidas

A Aula 02 tratou a **porosidade** (φ) como a fração do volume total da rocha ocupada por espaço vazio — poros — disponível para conter fluido. É uma propriedade estática: diz quanto espaço existe, não diz nada sobre se o fluido nesse espaço consegue se mover. Essa segunda pergunta é respondida pela **permeabilidade** (k), a medida da facilidade com que um fluido flui através da rede de poros interconectados de uma rocha sob um gradiente de pressão, formalizada pela lei de Darcy (1856) e expressa na indústria em **darcy** (D) ou, mais comumente em reservatórios de petróleo, em **milidarcy** (mD, um milésimo de darcy).

A distinção importa porque as duas propriedades podem divergir de forma extrema: um folhelho pode ter porosidade razoável (5–15%, às vezes mais) mas permeabilidade extremamente baixa (frequentemente < 0,01 mD), porque os poros são minúsculos e mal conectados — por isso folhelhos armazenam hidrocarboneto mas não o liberam com facilidade para um poço convencional (a base técnica dos reservatórios não convencionais, fora do escopo quantitativo deste módulo). Já um arenito bem selecionado e pouco cimentado pode combinar porosidade de 20–25% com permeabilidade de centenas a milhares de mD — um reservatório convencional de alta qualidade. A regra geral, mas não uma lei física estrita, é que permeabilidade cresce com porosidade dentro de uma mesma família litológica, porque ambas respondem ao tamanho e à seleção dos grãos e ao grau de cimentação; a relação se rompe entre litologias diferentes (carbonatos com porosidade vugular, por exemplo, podem ter porosidade alta e permeabilidade imprevisível, dependendo de os vúgulos estarem ou não conectados entre si).

### Saturação e o conceito de saturação de água irredutível

A Aula 02 calculou Sw pela equação de Archie. Vale aprofundar um ponto: mesmo num reservatório de excelente qualidade, produzindo óleo ou gás em alta taxa, a saturação de água nunca é zero. Uma fração da água — a **saturação de água irredutível** (Swi) — fica retida por forças capilares nos poros menores e nas interfaces grão-fluido, e não se move mesmo sob a pressão de produção. Swi varia tipicamente de 10 a 40% dependendo da textura da rocha (rochas de grão fino e mal selecionadas retêm mais água irredutível que arenitos limpos de grão grosso), e distinguir Sw calculado por Archie de Swi por análise de testemunho é outro ponto onde a calibração por testemunhagem (Aula 02) tem papel decisivo: um Sw de perfil muito próximo do Swi de testemunho é, em si, um indicativo de que a zona produzirá hidrocarboneto praticamente sem água — informação de grande valor econômico antes mesmo de o poço ser testado.

### PVT: como o fluido se comporta ao sair do reservatório

Todas as propriedades discutidas até aqui descrevem a rocha. O reservatório de petróleo, porém, contém um fluido cujo comportamento muda drasticamente entre a condição de subsuperfície (alta pressão, alta temperatura) e a condição de superfície (pressão atmosférica, temperatura ambiente) — e essa mudança precisa ser quantificada para converter volume medido em superfície (o que sai do poço e é vendido) em volume que existia no reservatório (o que a geologia colocou lá). Essa é a função da análise **PVT** (pressão-volume-temperatura), realizada em laboratório sobre uma amostra de fluido recombinada ou coletada de fundo de poço.

Duas propriedades PVT dominam os cálculos deste módulo:

- O **fator volume-formação do óleo** (Bo), definido como o volume que uma unidade de óleo ocupa no reservatório dividido pelo volume que essa mesma massa de óleo ocupa em condições de superfície (tanque, após liberar o gás dissolvido). Bo é sempre maior que 1 para óleo vivo (contendo gás dissolvido), tipicamente entre 1,1 e 1,5 bbl/STB (barril de reservatório por barril de tanque, *stock tank barrel*) em óleos com razão gás-óleo moderada a alta, porque o óleo no reservatório está expandido pelo gás em solução e pela expansão térmica na temperatura de reservatório (efeito só parcialmente contrabalançado pela compressão devida à alta pressão), e "encolhe" ao ser trazido à superfície e liberar esse gás.
- A **razão de solubilidade gás-óleo** (Rs), o volume de gás (medido em condições-padrão) que está dissolvido em uma unidade de volume de óleo (medido em condições-padrão) na pressão e temperatura do reservatório, expressa em pés cúbicos padrão por barril de tanque (scf/STB). Acima da **pressão de ponto de bolha** (a pressão na qual a primeira bolha de gás se separa do óleo ao reduzir a pressão), todo o gás permanece em solução, Rs se mantém constante no seu valor máximo (Rsb) e o óleo é dito **subsaturado**; abaixo do ponto de bolha, Rs **cai progressivamente** à medida que gás sai de solução dentro do reservatório, tendendo a zero apenas em pressões muito baixas — não caindo a zero logo abaixo de Pb.

Essas duas propriedades não são constantes: variam com a pressão do reservatório ao longo da vida produtiva, e essa variação — Bo e Rs caindo à medida que a pressão cai abaixo do ponto de bolha e gás sai de solução — é justamente o que a Aula 04 usa para explicar os mecanismos de produção por depleção de gás em solução.

```
Comportamento esquemático de Bo e Rs com a queda de pressão do reservatório

pressão inicial (alta) ──────────────► pressão de abandono (baixa)
                    ponto de bolha (Pb)
Rs:  constante ───────────┤ cai progressivamente após Pb
Bo:  sobe levemente ──────┤ MÁXIMO em Pb; cai após Pb (gás sai de solução, óleo "encolhe")
```
Atenção ao sinal de Bo acima do ponto de bolha: enquanto a pressão cai da inicial até Pb, o óleo subsaturado simplesmente se expande, então Bo **sobe** ligeiramente, atingindo seu valor máximo (Bob) exatamente no ponto de bolha. Só abaixo de Pb Bo passa a **cair**, porque aí domina a perda de gás dissolvido, que encolhe o óleo mais do que a expansão por descompressão o dilata — dois regimes fisicamente distintos que o engenheiro de reservatório trata com equações separadas.

### Cálculo de volume in place: transformando propriedades em um número de negócio

O objetivo prático de tudo isto — porosidade e saturação de perfis, permeabilidade de testemunho, Bo e Rs de PVT — é responder à pergunta que orienta qualquer decisão de desenvolvimento de campo: quanto óleo (ou gás) existe originalmente no reservatório? Essa grandeza é o **óleo original in place** (OOIP, *original oil in place*), calculado pelo **método volumétrico** quando ainda não há histórico de produção suficiente para métodos de balanço de materiais (tema que a Aula 04 introduz):

OOIP (STB) = (7.758 × A × h × φ × (1 − Sw)) / Bo

onde A é a área do reservatório em acres, h é a espessura líquida de reservatório (*net pay* — a espessura efetivamente porosa, permeável e saturada de hidrocarboneto acima de um corte mínimo de qualidade, distinta da espessura bruta perfurada) em pés, φ é a porosidade média (fração), Sw é a saturação de água média (fração, de modo que 1−Sw é a saturação de óleo), Bo é o fator volume-formação (bbl/STB), e 7.758 é a constante de conversão de acre-pé para barris (1 acre-pé = 7.758 barris, uma conversão geométrica fixa, não uma propriedade física do reservatório). Uma fórmula análoga, com constante de conversão diferente (43.560, pés cúbicos por acre-pé) e usando o fator volume-formação do gás (Bg) no denominador, calcula o **gás original in place** (OGIP) para reservatórios de gás.

O OOIP é um limite superior teórico, não o volume recuperável: apenas uma fração dele — o **fator de recuperação** (FR), tema central da Aula 04 — chega efetivamente à superfície ao longo da vida produtiva do campo, porque forças capilares, heterogeneidade da rocha e a própria física dos mecanismos de deslocamento de fluido impedem a extração total. Ainda assim, o OOIP é o número fundacional de toda avaliação econômica de um campo: sem ele, não há como estimar reservas, dimensionar instalações de produção ou justificar investimento em poços adicionais.

## Exemplo trabalhado

**Situação:** um reservatório de arenito tem área de 800 acres, espessura líquida (net pay) média de 25 pés, porosidade média de 22%, saturação de água média de 30% (obtida por Archie e calibrada por testemunho, Aula 02) e fator volume-formação do óleo Bo = 1,25 bbl/STB (de análise PVT, reservatório acima do ponto de bolha). Calcule o OOIP.

**Resolução:**

OOIP = (7.758 × A × h × φ × (1 − Sw)) / Bo

Substituindo:
A = 800 acres
h = 25 ft
φ = 0,22
(1 − Sw) = 1 − 0,30 = 0,70
Bo = 1,25 bbl/STB

Numerador: 7.758 × 800 × 25 × 0,22 × 0,70
Passo 1: 7.758 × 800 = 6.206.400
Passo 2: 6.206.400 × 25 = 155.160.000
Passo 3: 155.160.000 × 0,22 = 34.135.200
Passo 4: 34.135.200 × 0,70 = 23.894.640

OOIP = 23.894.640 / 1,25 = 19.115.712 STB

O reservatório contém aproximadamente **19,1 milhões de barris de óleo** originalmente in place, em condições de tanque de superfície. Esse número, por si só, ainda não diz quanto será produzido — se este reservatório produzir por depleção por gás em solução com fator de recuperação primária de 18% (exatamente o caso que a Aula 05 retoma para calcular o ganho de EOR sobre este mesmo campo), as reservas recuperáveis por recuperação primária seriam de aproximadamente 3,4 milhões de barris (19.115.712 × 0,18 ≈ 3.440.828 STB), um número bem mais próximo do que efetivamente justifica o investimento em desenvolvimento do campo. Note também a sensibilidade do resultado a Bo: se a análise PVT tivesse sido feita incorretamente e Bo verdadeiro fosse 1,35 em vez de 1,25 (óleo mais expandido pelo gás em solução), o OOIP calculado cairia para cerca de 17,7 milhões de STB — uma diferença de quase 1,4 milhão de barris só pelo erro na propriedade de fluido, o que explica por que a qualidade da amostragem PVT é tratada com o mesmo rigor que a qualidade dos perfis na avaliação de um campo.

## Erros comuns

- **Assumir que porosidade alta implica permeabilidade alta.** É a confusão que dá nome à primeira seção desta aula: folhelhos desmentem essa suposição diretamente, e mesmo entre arenitos e carbonatos a relação só vale dentro da mesma família litológica.
- **Tratar Swi (água irredutível) como um erro de medida a ser eliminado.** Ela é física, não ruído: mesmo o reservatório mais produtivo do mundo retém água presa por capilaridade. O que se avalia é se Sw de perfil está próximo de Swi de testemunho, não se Sw chegou a zero.
- **Ler Bo caindo como "sempre ruim" ou Bo subindo como "sempre bom".** Os dois regimes são esperados: Bo sobe enquanto o óleo subsaturado se expande e cai depois do ponto de bolha porque o gás sai de solução — nenhum dos dois é anomalia, são fases normais da depleção.
- **Trocar A (acres) ou h (pés) por unidades métricas sem reconverter a constante 7.758.** A fórmula do método volumétrico é dimensionalmente amarrada a acres, pés e barris; usar hectares ou metros sem ajustar a constante de conversão produz um OOIP errado por ordens de grandeza, não por um pequeno desvio.

## O que não concluir

- **Que o OOIP calculado é o volume que será produzido.** É um limite superior teórico. O volume recuperável é sempre uma fração dele, definida pelo fator de recuperação — tema que a Aula 04 introduz e que, no próprio exemplo desta aula, reduz 19,1 milhões de STB a cerca de 3,4 milhões recuperáveis.
- **Que espessura bruta perfurada (o que a broca atravessou) é o mesmo que net pay.** Só a fração porosa, permeável e saturada de hidrocarboneto acima de um corte mínimo de qualidade entra na fórmula — intervalos improdutivos dentro do intervalo perfurado são descartados do cálculo.
- **Que Bo e Rs são propriedades da rocha.** São propriedades do fluido, medidas por PVT — por isso variam entre campos com a mesma rocha-reservatório se o óleo tiver composição ou razão gás-óleo diferente.

## Recap relâmpago

- Porosidade (espaço poroso disponível) e permeabilidade (facilidade de fluxo através dos poros conectados, medida em mD) são propriedades independentes: folhelhos podem ter porosidade razoável e permeabilidade muito baixa; arenitos limpos tendem a ter as duas altas.
- A saturação de água irredutível (Swi) é a fração de água que nunca se move, retida por forças capilares; comparar Sw de perfil (Archie) com Swi de testemunho indica se a zona produzirá com pouca ou nenhuma água.
- A análise PVT converte volume de fluido entre condições de reservatório e de superfície: Bo (fator volume-formação do óleo, tipicamente 1,1–1,5 bbl/STB) e Rs (razão de solubilidade gás-óleo, scf/STB) caracterizam esse comportamento, e ambos mudam de regime na pressão de ponto de bolha — Rs constante acima de Pb e decrescente abaixo; Bo subindo levemente até Pb, onde é máximo (Bob), e caindo abaixo dele.
- O óleo original in place (OOIP) é calculado pelo método volumétrico: OOIP = 7.758 × A × h × φ × (1−Sw) / Bo, em STB, com A em acres e h em pés — um limite superior teórico, não o volume recuperável.
- O fator de recuperação (Aula 04) converte OOIP em reservas recuperáveis; erros em qualquer propriedade de entrada (especialmente Bo, de PVT) se propagam diretamente e proporcionalmente para o volume calculado.

## Próxima aula

[[12-engenharia-de-petroleo-aula-04-mecanismos-de-producao-e-testes-de-poco|Aula 04 — Mecanismos de produção, recuperação primária e secundária e testes de poço]]

## Anterior

[[12-engenharia-de-petroleo-aula-02-perfilagem-geofisica-de-poco|Aula 02 — Avaliação de formações]]

## Fontes

- Ahmed, T. (2019), *Reservoir Engineering Handbook*, 5ª ed., Gulf Professional Publishing, cap. 1–3 (propriedades de rocha e fluido, PVT, volumetria).
- Craft, B. C. & Hawkins, M. (revisado por Terry, R. E. & Rogers, J. B., 2015), *Applied Petroleum Reservoir Engineering*, 3ª ed., Pearson/Prentice Hall, cap. 2–3 (método volumétrico, OOIP/OGIP).
- Dake, L. P. (1978), *Fundamentals of Reservoir Engineering*, Elsevier, cap. 1–2 (PVT, Bo, Rs, ponto de bolha).
- Tiab, D. & Donaldson, E. C. (2016), *Petrophysics*, 4ª ed., Gulf Professional Publishing, cap. 2, 5 (porosidade, permeabilidade, saturação irredutível).

<!--
nivel: avancado
palavras_corpo: 2010
mapa_objetivo_secao:
  geologia-avancado-m12-oa03: "Porosidade e permeabilidade: propriedades independentes, frequentemente confundidas" + "Saturação e o conceito de saturação de água irredutível" + "PVT: como o fluido se comporta ao sair do reservatório" + "Cálculo de volume in place: transformando propriedades em um número de negócio" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: PETRENG-M12-A03-PERM-001
    claim: "Permeabilidade (k), medida em darcy ou milidarcy (mD), formalizada pela lei de Darcy (1856), quantifica a facilidade de fluxo de fluido através de poros interconectados sob um gradiente de pressão, sendo independente da porosidade: folhelhos podem ter porosidade moderada (5-15%) com permeabilidade muito baixa (frequentemente < 0,01 mD), enquanto arenitos bem selecionados podem combinar porosidade de 20-25% com permeabilidade de centenas a milhares de mD."
    risk: fato
    source: "Tiab & Donaldson 2016, Petrophysics, cap. 2, 5; Ahmed 2019, Reservoir Engineering Handbook, cap. 2"
  - claim_id: PETRENG-M12-A03-SWI-002
    claim: "A saturação de água irredutível (Swi) é a fração de água retida nos poros por forças capilares que não se move mesmo sob pressão de produção, tipicamente entre 10% e 40% dependendo da textura da rocha (maior em rochas de grão fino/mal selecionadas, menor em arenitos limpos de grão grosso)."
    risk: fato
    source: "Tiab & Donaldson 2016, Petrophysics, cap. 5; Ahmed 2019, cap. 3"
  - claim_id: PETRENG-M12-A03-PVT-003
    claim: "O fator volume-formação do óleo (Bo) é a razão entre o volume de óleo no reservatório e o volume da mesma massa de óleo em condições de tanque de superfície (após liberar gás dissolvido), sendo sempre maior que 1 para óleo vivo (tipicamente 1,1-1,5 bbl/STB); a razão de solubilidade gás-óleo (Rs, em scf/STB) é o volume de gás dissolvido por barril de óleo de tanque nas condições de reservatório. Acima da pressão de ponto de bolha o oleo e subsaturado, Rs permanece constante no valor maximo (Rsb) e Bo SOBE levemente com a queda de pressao, atingindo seu maximo (Bob) exatamente em Pb; abaixo de Pb, Rs cai progressivamente (tendendo a zero so em pressoes muito baixas) e Bo cai."
    risk: fato
    source: "Dake 1978, Fundamentals of Reservoir Engineering, cap. 2; Ahmed 2019, cap. 1"
  - claim_id: PETRENG-M12-A03-OOIP-004
    claim: "O método volumétrico calcula o óleo original in place (OOIP, em barris de tanque/STB) pela fórmula OOIP = 7.758 x A x h x phi x (1-Sw) / Bo, com A a área do reservatório em acres, h a espessura líquida (net pay) em pés, phi a porosidade média (fração), Sw a saturação de água média (fração) e Bo o fator volume-formação do óleo; a constante 7.758 converte acre-pé para barris. Formula análoga com constante 43.560 (pés cúbicos por acre-pé) e Bg no lugar de Bo calcula o gás original in place (OGIP)."
    risk: fato
    source: "Craft & Hawkins (rev. Terry & Rogers) 2015, Applied Petroleum Reservoir Engineering, cap. 2-3; Ahmed 2019, cap. 3"
  - claim_id: PETRENG-M12-A03-FR-005
    claim: "O OOIP calculado pelo método volumétrico representa um limite superior teórico do óleo presente na rocha, não o volume recuperável; apenas a fração definida pelo fator de recuperação (FR) chega à superfície ao longo da vida produtiva, por efeito de forças capilares, heterogeneidade da rocha e da física dos mecanismos de deslocamento de fluido."
    risk: fato
    source: "Craft & Hawkins (rev. Terry & Rogers) 2015, cap. 2; Ahmed 2019, cap. 3, 15"
-->
