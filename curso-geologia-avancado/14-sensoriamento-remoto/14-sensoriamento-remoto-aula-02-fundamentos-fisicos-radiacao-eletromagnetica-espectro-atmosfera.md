# Aula 02: Fundamentos físicos: radiação eletromagnética, espectro e interação com a atmosfera

**ID:** geologia-avancado-m14-a02
**Módulo:** [[14-sensoriamento-remoto-modulo|Módulo 14 — Sensoriamento remoto]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** explicar a física por trás de toda imagem de sensoriamento remoto — o que é radiação eletromagnética, como o Sol e a Terra a emitem, e como a atmosfera filtra, espalha e absorve essa radiação antes (e depois) de ela atingir o alvo.
**Ao final você vai conseguir:** descrever a radiação eletromagnética em termos de comprimento de onda e frequência; localizar as regiões do espectro usadas em sensoriamento remoto (visível, infravermelho próximo, SWIR, termal, micro-ondas); explicar as leis físicas que regem emissão e reflexão; e prever, para uma dada faixa espectral, se a atmosfera deixa passar, absorve ou espalha a radiação.
**Pré-requisito:** [[14-sensoriamento-remoto-aula-01-conceitos-plataformas-sensores-composicoes-coloridas|Aula 01]] — pressupõe já conhecidos os termos sensor, banda, resolução espectral e a ideia geral de composição colorida.

## Conteúdo

### Por que a física vem antes da interpretação

A Aula 01 tratou bandas e resoluções como dados de ficha técnica, sem explicar de onde vêm. Esta aula preenche essa lacuna: toda a informação que um sensor de imagem capta é, na origem, um fenômeno físico único — radiação eletromagnética se propagando do Sol (ou da própria Terra) até o sensor, atravessando a atmosfera duas vezes (na descida do Sol até o alvo, e na subida do alvo até o sensor) e interagindo com a superfície no meio do caminho. Entender essa cadeia física é o que permite, mais adiante, prever por que a água aparece escura no infravermelho, por que a vegetação satura no verde, ou por que certas bandas de satélite simplesmente não existem — porque a atmosfera bloqueia toda a radiação naquela faixa antes que ela chegue a lugar nenhum.

### Radiação eletromagnética: comprimento de onda, frequência e energia

**Radiação eletromagnética** é energia que se propaga no espaço (inclusive no vácuo, sem precisar de meio material) na forma de ondas oscilantes de campos elétrico e magnético, viajando à velocidade da luz (*c* ≈ 3 × 10⁸ m/s). Duas grandezas descrevem essa onda de forma equivalente: o **comprimento de onda** (λ, lambda), a distância entre dois picos sucessivos da onda, normalmente medido em micrômetros (µm, 10⁻⁶ m) ou nanômetros (nm, 10⁻⁹ m) nas faixas usadas em sensoriamento remoto óptico; e a **frequência** (ν, ni), o número de oscilações completas por segundo, em Hertz. As duas se relacionam por *c* = λ × ν — comprimento de onda e frequência são inversamente proporcionais: onda mais curta, frequência mais alta, e vice-versa.

A terceira grandeza, e a que mais importa fisicamente, é a **energia** de cada fóton (o quantum de radiação eletromagnética), dada por *E* = h × ν, onde h é a constante de Planck. Como frequência e comprimento de onda são inversamente relacionados, isso significa que **radiação de comprimento de onda mais curto carrega mais energia por fóton** — raios gama e raios X (comprimentos de onda picométricos a subnanométricos) são extremamente energéticos, enquanto ondas de rádio (comprimentos de onda de metros a quilômetros) carregam pouquíssima energia por fóton. Guarde essa relação: ela é o que explicará, na Aula 06, por que sensoriamento remoto na faixa de micro-ondas é feito quase sempre por sensores **ativos**, que emitem sua própria energia. A energia por fóton ali é tão baixa, e a emissão natural da Terra nessa faixa tão fraca, que um sensor passivo teria muito pouco sinal com que trabalhar — ao contrário do sensor óptico, que simplesmente capta os fótons de luz solar refletida, já abundantes.

### O espectro eletromagnético e as janelas usadas em sensoriamento remoto

O **espectro eletromagnético** é o intervalo contínuo de todos os comprimentos de onda possíveis, organizado por convenção em regiões nomeadas — não existe fronteira física abrupta entre elas, são divisões de conveniência. As regiões relevantes para este curso, da menor para a maior comprimento de onda:

| Região | Faixa aproximada | Uso principal em sensoriamento remoto |
|---|---|---|
| Ultravioleta (UV) | 0,01-0,4 µm | pouco usado (forte absorção atmosférica); aplicações específicas de composição mineral e detecção de SO₂ vulcânico |
| Visível | 0,4-0,7 µm | cor verdadeira; azul, verde, vermelho como bandas discretas |
| Infravermelho próximo (NIR) | 0,7-1,3 µm | vigor de vegetação, contraste água/terra |
| Infravermelho de ondas curtas (SWIR) | 1,3-3 µm | minerais de alteração hidrotermal, teor de umidade |
| Infravermelho termal (TIR) | 3-14 µm (uso prático: 8-14 µm) | temperatura de superfície, emissividade mineral |
| Micro-ondas | 1 mm-1 m | radar (SAR), atravessa nuvens e, em parte, vegetação |

Uma observação importante de nomenclatura: **visível mais infravermelho próximo e SWIR** são muitas vezes agrupados sob o termo genérico **VNIR-SWIR** ou simplesmente "óptico" nos sensores multiespectrais, porque toda essa faixa depende de radiação solar refletida — em contraste com o termal, que depende de emissão própria do alvo (a distinção física entre refletância e emissão é o assunto da próxima seção).

### Duas fontes de radiação: reflexão da luz solar e emissão térmica própria

Um sensor passivo pode captar radiação por dois mecanismos fisicamente distintos, e distingui-los é essencial para entender por que o termal (Aula 07) se comporta de forma tão diferente do óptico.

No **visível ao SWIR** (até cerca de 3 µm), a radiação captada é majoritariamente luz solar que incidiu no alvo e foi **refletida** — o alvo em si não está "brilhando", está devolvendo parte da luz que recebeu. Por isso, sensores ópticos passivos não funcionam à noite: sem Sol, não há luz a refletir.

Já a partir de cerca de 3 µm, e dominantemente entre 8-14 µm (a "janela atmosférica" termal, ver seção seguinte), a radiação captada é majoritariamente **emissão térmica própria** do alvo — todo objeto com temperatura acima do zero absoluto emite radiação eletromagnética espontaneamente, com intensidade e distribuição espectral que dependem da sua temperatura (lei de Planck para o corpo negro) e da sua **emissividade** (ε), a eficiência relativa com que um material real emite radiação térmica comparado a um corpo negro ideal (ε = 1) na mesma temperatura — a maioria dos materiais naturais tem emissividade entre 0,85 e 0,98, variando de forma diagnóstica com a composição mineral, o que sustenta o mapeamento litológico por sensoriamento termal (Aula 07). A grande vantagem prática: como a emissão termal é própria do alvo, não depende de luz solar, um sensor termal capta imagem tanto de dia quanto de noite.

### Como a atmosfera interfere: absorção, espalhamento e janelas atmosféricas

A radiação eletromagnética atravessa a atmosfera duas vezes no trajeto Sol → alvo → sensor, e a atmosfera não é um meio neutro — ela interage com a radiação de duas formas principais.

A **absorção** ocorre quando moléculas atmosféricas (vapor d'água, dióxido de carbono, ozônio, oxigênio, principalmente) absorvem radiação em comprimentos de onda específicos, correspondentes aos seus níveis de energia molecular — nessas faixas, a radiação simplesmente não atravessa a atmosfera em quantidade utilizável, e nenhum sensor orbital opera ali. As faixas onde a atmosfera é relativamente transparente são chamadas **janelas atmosféricas**, e é dentro delas que os sensores de satélite posicionam suas bandas — não por escolha de engenharia, mas por necessidade física. É por isso que, por exemplo, praticamente nenhum sensor óptico orbital opera em torno de 1,4 µm ou 1,9 µm (fortíssima absorção por vapor d'água) — e é também por isso que a banda "cirrus" do Landsat 8/9 (1,36-1,38 µm, mencionada na Aula 01) foi projetada deliberadamente **dentro** de uma banda de absorção de vapor d'água: como o sinal da superfície nessa faixa é quase todo absorvido antes de chegar ao sensor, qualquer sinal que ainda assim retorna vem quase exclusivamente do espalhamento por cirros em alta altitude, tornando essa banda um detector eficiente desse tipo específico de nuvem.

O **espalhamento** ocorre quando a radiação é redirecionada em múltiplas direções ao colidir com moléculas de ar ou partículas em suspensão (aerossóis, poeira, fumaça), sem ser absorvida — é o espalhamento, e não a absorção, o principal responsável pela "névoa atmosférica" (*haze*) que reduz o contraste das imagens e pelo próprio azul do céu. Dois regimes dominam, conforme o tamanho da partícula em relação ao comprimento de onda: o **espalhamento de Rayleigh**, causado por moléculas de gás muito menores que o comprimento de onda da luz visível, é inversamente proporcional à quarta potência do comprimento de onda (λ⁻⁴) — afeta muito mais o azul (comprimento de onda curto) do que o vermelho, e é justamente por isso que o céu é azul e que a banda azul de qualquer sensor óptico chega ao solo mais degradada por espalhamento atmosférico do que as demais, exigindo correção mais agressiva no pré-processamento; o **espalhamento de Mie**, causado por partículas maiores (aerossóis, poeira, fumaça, gotículas), tem menor dependência do comprimento de onda e domina em condições de atmosfera poluída ou com queimadas ativas.

A consequência prática, central para todo o resto do módulo: nenhuma imagem bruta de satélite mostra a reflectância "verdadeira" da superfície — o que o sensor mede é uma mistura da radiação que veio do alvo com radiação espalhada pela própria atmosfera (o chamado *path radiance*, radiância de trajeto), e separar as duas é exatamente o objetivo da correção atmosférica, primeira etapa do processamento digital de imagens que a Aula 04 vai apresentar.

## Exemplo trabalhado

**Situação:** um sensor está sendo projetado para mapear composição mineral de superfície numa região árida, e o engenheiro de instrumentação precisa decidir em que faixa espectral posicionar uma nova banda, evitando duas armadilhas: (a) posicioná-la numa faixa de forte absorção atmosférica, onde nenhum sinal útil chegaria ao sensor; (b) posicioná-la de forma que o espalhamento atmosférico degrade o contraste a ponto de inutilizar a banda. Considerando as faixas candidatas 1,4 µm, 2,2 µm e 0,45 µm, qual é a mais adequada, e por quê?

**Resolução:**

*Candidata 1,4 µm:* está dentro de uma banda de forte absorção por vapor d'água — a atmosfera bloqueia a maior parte da radiação solar nessa faixa antes mesmo de chegar ao alvo, e o que sobra é absorvido de novo na volta. Um sensor projetado para captar reflectância de superfície aqui captaria muito pouco sinal útil — esta é, na prática, uma faixa reservada para detectar propriedades da própria atmosfera (como a banda cirrus do Landsat 8/9), não da superfície. **Descartada.**

*Candidata 0,45 µm (azul):* está numa janela atmosférica (a radiação atravessa), mas é fortemente afetada pelo espalhamento de Rayleigh, proporcional a λ⁻⁴ — como 0,45 µm é um comprimento de onda relativamente curto dentro do visível, o espalhamento aqui é significativamente mais intenso do que em comprimentos de onda maiores, o que reduz o contraste da imagem e degrada a razão sinal-ruído úteis para discriminar minerais sutilmente diferentes entre si. Não está tecnicamente inviabilizada, mas é subótima para esse objetivo específico. **Viável, mas não ideal.**

*Candidata 2,2 µm (SWIR):* está dentro de uma janela atmosférica razoavelmente limpa (fora das principais bandas de absorção por vapor d'água e CO₂), e o espalhamento de Rayleigh nessa faixa é ordens de grandeza menor que no azul, porque λ⁻⁴ decresce rapidamente com o aumento do comprimento de onda — além disso, 2,2 µm é justamente a região onde argilominerais e outros minerais de alteração hidrotermal têm feições de absorção diagnósticas fortes (mecanismo detalhado na Aula 03), tornando essa faixa não apenas fisicamente limpa, mas também informativa para o objetivo declarado. **Escolha correta**, e coerente com a razão pela qual sensores geológicos reais (ASTER, Landsat 8/9) concentram várias bandas na região SWIR.

## Erros comuns

- **Posicionar (ou escolher) uma banda de satélite numa faixa de forte absorção atmosférica esperando captar sinal de superfície.** Como o exemplo trabalhado mostra com 1,4 µm, o sinal que sobra ali é quase todo da própria atmosfera (cirros), não da superfície — banda de absorção serve para monitorar atmosfera, não terreno.
- **Achar que espalhamento e absorção são o mesmo fenômeno.** Absorção remove energia da radiação (a molécula "consome" o fóton); espalhamento apenas redireciona a radiação sem absorvê-la — são as duas causas físicas distintas por trás da mesma degradação visível (perda de contraste), e a correção adequada depende de saber qual predomina.
- **Ignorar a banda azul como "só mais uma banda" ao avaliar qualidade de imagem.** Ela sofre o espalhamento de Rayleigh mais intenso (λ⁻⁴ cresce rapidamente para comprimentos de onda curtos) — é sistematicamente a banda mais degradada por névoa atmosférica, e exige a correção mais agressiva.
- **Assumir que sensor termal "vê calor" da mesma forma que sensor óptico "vê luz".** São dois mecanismos físicos diferentes (emissão própria vs. reflexão de luz solar) — é por isso, e só por isso, que o termal funciona à noite e o óptico não.

## O que não concluir

- **Que comprimento de onda maior significa sempre "menos informação útil".** Ondas de rádio carregam pouca energia por fóton, mas SWIR e micro-ondas (comprimentos maiores que o visível) carregam informação diagnóstica de mineral e de superfície que o visível simplesmente não tem.
- **Que as janelas atmosféricas são uma escolha de engenharia dos fabricantes de satélite.** São uma necessidade física — a atmosfera bloqueia certas faixas independentemente do sensor; a engenharia escolhe onde posicionar bandas dentro das janelas que existem, não decide onde as janelas ficam.
- **Que emissividade é uma propriedade fixa e universal de "rocha" ou "solo".** Ela varia de forma diagnóstica com a composição mineral específica — é essa variação, não um valor único, que sustenta o mapeamento litológico por sensoriamento termal (Aula 07).

## Recap relâmpago

- Radiação eletromagnética se propaga como onda (descrita por comprimento de onda λ e frequência ν, relacionadas por c = λν) e como quanta de energia (E = hν) — comprimento de onda curto significa energia por fóton mais alta.
- O espectro eletromagnético usado em sensoriamento remoto vai do ultravioleta ao micro-ondas; visível (0,4-0,7 µm), infravermelho próximo (0,7-1,3 µm) e SWIR (1,3-3 µm) dependem de reflexão de luz solar; o termal (dominantemente 8-14 µm) depende de emissão térmica própria do alvo, regida pela temperatura e pela emissividade do material.
- Sensores ópticos passivos (visível a SWIR) não operam à noite, porque dependem de luz solar refletida; sensores termais operam de dia e de noite, porque captam emissão própria.
- A atmosfera absorve radiação em faixas específicas (vapor d'água, CO₂, ozônio) — sensores só operam nas janelas atmosféricas onde a absorção é baixa; fora delas, praticamente nenhum sinal de superfície chega ao sensor.
- O espalhamento atmosférico redistribui radiação sem absorvê-la; o espalhamento de Rayleigh (moléculas de gás, proporcional a λ⁻⁴) afeta muito mais o azul do que o vermelho ou o infravermelho, e é o responsável pelo céu azul e pela maior degradação da banda azul em imagens de satélite; o espalhamento de Mie (aerossóis, poeira, fumaça) tem menor dependência espectral.
- Nenhuma imagem bruta mostra a reflectância verdadeira da superfície — ela está misturada com radiância espalhada pela atmosfera (*path radiance*); separar as duas é o objetivo da correção atmosférica, primeira etapa do processamento digital de imagens (Aula 04).

## Próxima aula

[[14-sensoriamento-remoto-aula-03-comportamento-espectral-agua-solos-minerais-rochas-vegetacao-geobotanica|Aula 03 — Comportamento espectral de água, solos, minerais, rochas e vegetação; geobotânica]] — com a física da radiação e da atmosfera estabelecida, a próxima aula aplica esse arcabouço para explicar por que cada tipo de alvo natural tem uma "assinatura" espectral própria e reconhecível.

## Fontes

- Jensen, J. R. (2016), *Introductory Digital Image Processing: A Remote Sensing Perspective*, 4ª ed., Pearson, cap. 2 (radiação eletromagnética, leis de Planck e Stefan-Boltzmann, interação com a atmosfera).
- Sabins, F. F. & Ellis, J. M. (2020), *Remote Sensing: Principles, Interpretation, and Applications*, 4ª ed., Waveland Press, cap. 1 (espectro eletromagnético, janelas atmosféricas, espalhamento de Rayleigh e Mie).
- Lillesand, T. M., Kiefer, R. W. & Chipman, J. W. (2015), *Remote Sensing and Image Interpretation*, 7ª ed., Wiley, cap. 1 (fundamentos físicos, refletância vs. emitância).
- NASA/USGS, *Landsat 8 Data Users Handbook* (justificativa de posicionamento da banda cirrus dentro de banda de absorção de vapor d'água).

<!--
nivel: avancado
palavras_corpo: 1983
mapa_objetivo_secao:
  geologia-avancado-m14-oa01: "Por que a física vem antes da interpretação" + "Radiação eletromagnética: comprimento de onda, frequência e energia" + "O espectro eletromagnético e as janelas usadas em sensoriamento remoto" + "Duas fontes de radiação: reflexão da luz solar e emissão térmica própria" + "Como a atmosfera interfere: absorção, espalhamento e janelas atmosféricas" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: SENSREM-M14-A02-ONDAENERGIA-001
    claim: "Radiação eletromagnética se propaga à velocidade da luz (c ≈ 3×10^8 m/s), relacionando comprimento de onda e frequência por c = λν; a energia de cada fóton é E = hν (h = constante de Planck), de modo que comprimento de onda mais curto corresponde a maior energia por fóton."
    risk: fato
    source: "Jensen 2016, Introductory Digital Image Processing, cap. 2; física ondulatória padrão"
  - claim_id: SENSREM-M14-A02-EMISSIVIDADE-002
    claim: "Todo objeto com temperatura acima do zero absoluto emite radiação eletromagnética espontaneamente (lei de Planck para o corpo negro); a emissividade (ε) é a razão entre a emitância radiante de um material real e a de um corpo negro ideal na mesma temperatura, e a maioria dos materiais naturais tem emissividade entre 0,85 e 0,98."
    risk: aproximacao
    source: "Sabins & Ellis 2020, Remote Sensing, cap. 1 e 8 (faixa típica de emissividade de materiais naturais); Lillesand, Kiefer & Chipman 2015, cap. 1"
  - claim_id: SENSREM-M14-A02-JANELA-003
    claim: "A atmosfera absorve fortemente radiação eletromagnética em faixas específicas associadas a vapor d'água, CO2 e ozônio (ex.: em torno de 1,4 µm e 1,9 µm); sensores ópticos orbitais posicionam suas bandas dentro das janelas atmosféricas onde a absorção é baixa. A banda cirrus do Landsat 8/9 (1,36-1,38 µm) foi posicionada deliberadamente dentro de uma banda de forte absorção de vapor d'água para detectar espalhamento por nuvens cirros em alta altitude."
    risk: fato
    source: "NASA/USGS, Landsat 8 Data Users Handbook (banda 9, cirrus); Jensen 2016, cap. 2 (janelas atmosféricas)"
  - claim_id: SENSREM-M14-A02-RAYLEIGH-004
    claim: "O espalhamento de Rayleigh, causado por moléculas de gás muito menores que o comprimento de onda da luz, é inversamente proporcional à quarta potência do comprimento de onda (λ⁻⁴), afetando muito mais comprimentos de onda curtos (azul) do que longos (vermelho, infravermelho) — mecanismo responsável pela cor azul do céu. O espalhamento de Mie, causado por partículas maiores (aerossóis, poeira, fumaça), tem menor dependência espectral."
    risk: fato
    source: "Sabins & Ellis 2020, Remote Sensing, cap. 1; física atmosférica padrão (teoria de espalhamento de Rayleigh e de Mie)"
-->
