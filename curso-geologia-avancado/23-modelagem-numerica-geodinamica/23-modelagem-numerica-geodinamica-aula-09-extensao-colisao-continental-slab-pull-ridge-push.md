# Aula 09: Continentes em extensão e em colisão — ruptura continental, subsidência, evolução termal de orógenos, slab-pull, ridge-push e cunhas orogênicas

**ID:** geologia-avancado-m23-a09
**Módulo:** [[23-modelagem-numerica-geodinamica-modulo|Módulo 23 — Introdução à modelagem numérica geodinâmica]]
**Duração estimada:** ~27 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** aplicar a reologia e o calor das aulas anteriores à análise quantitativa de continentes em extensão (modelo de estiramento uniforme, subsidência térmica) e em colisão (evolução termal de orógenos, cunhas orogênicas críticas), e situar as forças de placa (slab-pull e ridge-push) como motores desses processos.
**Ao final você vai conseguir:** descrever o modelo de estiramento uniforme de McKenzie e calcular a fração de subsidência térmica atingida num dado tempo após o rifteamento; explicar por que orógenos colisionais aquecem antes de esfriar, e como isso afeta a reologia; comparar a ordem de grandeza das forças de slab-pull e ridge-push como motores da tectônica de placas; e explicar a lógica da teoria da cunha crítica para a geometria de um cinturão de dobramentos e empurrões.
**Pré-requisito:** [[23-modelagem-numerica-geodinamica-aula-08-reologia-rochas-viscosidade-fluencia|Aula 08 deste módulo]] (reologia e viscosidade efetiva) — esta aula é a síntese final do módulo, combinando calor (Aulas 05-07) e reologia (Aula 08) na interpretação quantitativa de dois cenários tectônicos completos.

## Conteúdo

### Extensão continental: o modelo de estiramento uniforme

Quando a litosfera continental se estende, ela afina, e o afinamento produz dois efeitos simultâneos sobre sua superfície: um efeito **isostático imediato** — a coluna afinada é mais leve, e a superfície subside quase instantaneamente, na escala geológica, para restaurar o equilíbrio isostático — e um efeito **térmico**, mais lento: o afinamento traz manto quente para mais perto da superfície (reduzindo a espessura da litosfera fria), elevando temporariamente a geoterma acima do seu perfil estável pré-rifteamento; à medida que a litosfera esfria de volta, ao longo de dezenas de milhões de anos, ela se contrai termicamente e a bacia continua subsidindo, agora de forma gradual e exponencialmente decrescente.

O modelo mais usado para quantificar esse processo é o **estiramento uniforme** de McKenzie (1978), que descreve o afinamento por um único parâmetro, o **fator de estiramento (ou de rifteamento) β** — a razão entre a espessura original da litosfera e sua espessura após o estiramento (β=2 significa que a litosfera ficou com metade da espessura original). O modelo assume que crosta e manto litosférico se estiram na mesma proporção (por isso "uniforme"), instantaneamente do ponto de vista geológico, e prevê dois componentes de subsidência: a subsidência de falha **inicial**, controlada diretamente por β através do balanço isostático, e a subsidência **térmica** subsequente, que decai exponencialmente conforme a litosfera reequilibra sua geoterma — a mesma física de resfriamento condutivo da Aula 07, aqui aplicada ao reaquecimento e reesfriamento de uma litosfera que já foi adelgaçada, não à formação de litosfera nova numa crista.

A fração da subsidência térmica **total** já atingida num tempo t após o rifteamento segue a forma:

S(t) / S_max = 1 − e^(−t/τ)

onde τ é uma **constante de tempo térmico** característica da litosfera de referência (tipicamente da ordem de 50 a 65 Ma para uma litosfera continental de referência de aproximadamente 125 km de espessura, segundo os parâmetros originais do modelo de McKenzie) — a mesma forma matemática de decaimento exponencial já vista para o resfriamento oceânico da Aula 07, porque o mecanismo físico subjacente (relaxamento condutivo de uma perturbação térmica) é o mesmo.

### Colisão continental: por que os orógenos aquecem antes de esfriar

O processo inverso — espessamento crustal por colisão, em vez de afinamento por extensão — produz o efeito térmico oposto ao da extensão em seu componente imediato, mas de forma qualitativamente mais complexa. O espessamento tectônico (empilhamento de nappes, duplicação de crosta) é, do ponto de vista térmico, **rápido demais** para que a condução de calor o acompanhe: uma crosta que dobra de espessura por cavalgamento tectônico carrega consigo, momentaneamente, a distribuição de temperatura que tinha antes do espessamento — mas agora concentrada num volume duas vezes menor de área superficial relativa, e com a camada radiogênica (Aula 07) também duplicada em espessura. O resultado é que a crosta espessada tende a **aquecer** nas primeiras dezenas de milhões de anos após o espessamento — tanto pela maior quantidade absoluta de produção radiogênica empilhada quanto pelo tempo que a condução de calor leva para dissipar o excesso de calor represado —, antes de eventualmente relaxar de volta a um perfil geotérmico mais próximo do estável, num processo de reequilíbrio condutivo que pode levar dezenas a mais de cem milhões de anos, dependendo da espessura final e da produção radiogênica envolvida.

Essa evolução térmica não é apenas uma curiosidade acadêmica: ela é diretamente responsável pela **trajetória metamórfica** clássica de um orógeno colisional — enterramento (aumento de pressão) seguido de aquecimento continuado mesmo após o soterramento ter cessado, seguido de exumação e resfriamento —, e, mais relevante para este módulo, tem um efeito reológico direto: como a Aula 08 mostrou, a viscosidade efetiva depende exponencialmente da temperatura, então o mesmo aquecimento pós-colisional que caracteriza um orógeno também **enfraquece** progressivamente sua crosta profunda, facilitando o fluxo dúctil lateral (extrusão de crosta média a inferior aquecida) que caracteriza muitos orógenos colisionais maduros, como o Himalaia — um caso onde os dois módulos deste curso, calor e reologia, deixam de ser tópicos separados e se tornam uma única história física conectada por retroalimentação: espessamento gera calor, calor reduz viscosidade, viscosidade reduzida facilita mais deformação.

### Forças motoras: slab-pull e ridge-push

O que impõe a tensão que estica ou comprime um continente, em primeiro lugar? As duas forças mais citadas na literatura clássica como motores primários da tectônica de placas são o **slab-pull** (a força de arrasto para baixo exercida pela flutuabilidade negativa de uma placa oceânica subductada, mais densa que o manto ao redor por estar mais fria) e o **ridge-push** (a força associada à topografia elevada da cordilheira meso-oceânica, que desliza gravitacionalmente para longe da crista devido ao contraste de densidade lateral entre litosfera jovem, quente e elevada, e litosfera mais velha, fria e mais profunda — em essência, uma consequência direta do mesmo resfriamento de semi-espaço da Aula 07). Estimativas clássicas de ordem de grandeza (Forsyth & Uyeda, 1975, *Geophysical Journal of the Royal Astronomical Society* — periódico que só passou a se chamar *Geophysical Journal International* em 1989) situam o slab-pull tipicamente em torno de 10¹³ N por metro de comprimento de zona de subducção, e o ridge-push cerca de uma ordem de grandeza menor, em torno de 10¹² N/m — o que faz do slab-pull, quando presente, a força dominante no balanço de forças de uma placa, embora ridge-push permaneça relevante sobretudo em placas sem, ou com pouca, subducção ativa em suas bordas. Essas forças, aplicadas sobre uma litosfera continental cuja resistência depende da reologia da Aula 08, é o que determina, em última instância, onde e com que taxa a extensão ou a colisão efetivamente ocorrem — a resistência integrada da litosfera (a área sob o perfil de resistência, o "envelope de resistência" mencionado na Aula 08) precisa ser superada pelas forças aplicadas para que a deformação avance.

### Cunhas orogênicas: a geometria de um cinturão de empurrões

Um último elemento quantitativo de síntese: por que um cinturão de dobramentos e empurrões (como o antepaís de uma cadeia colisional) assume tipicamente uma forma de **cunha** afilada, com o ápice voltado para o continente estável e a base alargando em direção à zona de colisão? A **teoria da cunha crítica** (Davis, Suppe & Dahlen, 1983), originalmente desenvolvida para prismas de acresção em zonas de subducção e depois estendida a cinturões de empurrões continentais, trata o material deformado como um material plástico friccional (Coulomb) empurrado sobre uma base de baixa resistência (um descolamento basal) — de forma análoga a uma pilha de areia sendo empurrada por uma pá de bulldozer: a pilha mantém um ângulo de inclinação (o "taper", a soma do mergulho da superfície topográfica com o mergulho do descolamento basal) determinado pelo equilíbrio entre a resistência interna do material, a resistência de atrito na base e a inclinação da própria superfície topográfica — um ângulo **crítico** abaixo do qual a cunha se deforma internamente (engrossando) até atingi-lo, e acima do qual ela avança sem se deformar mais internamente, como um bloco rígido deslizando sobre sua base. É essa mecânica de equilíbrio geométrico-friccional, e não apenas a geometria observada das camadas, que explica por que cinturões de empurrões mantêm uma forma de cunha característica e previsível ao longo de sua evolução.

## Exemplo trabalhado

**Situação: fração de subsidência térmica atingida aos 30 Ma e aos 100 Ma após um evento de rifteamento, usando τ = 62,8 Ma (valor de referência comumente citado em tratamentos didáticos do modelo de McKenzie para uma litosfera de referência de ~125 km).**

```python
import numpy as np

tau = 62.8    # Ma, constante de tempo termico de referencia

for t in [30, 100]:
    fracao = 1 - np.exp(-t / tau)
    print(t, fracao)
```

**Conferindo à mão, para t=30 Ma:** t/τ = 30/62,8 ≈ 0,4777. e^(−0,4777): usando e^(−0,5) ≈ 0,6065 e e^(0,0223) ≈ 1,0226, o produto dá e^(−0,4777) ≈ 0,6065 × 1,0226 ≈ **0,620**. Fração = 1 − 0,620 = **0,380**, ou seja, aproximadamente **38%** da subsidência térmica total já ocorreu 30 milhões de anos após o rifteamento.

**Para t=100 Ma:** t/τ = 100/62,8 ≈ 1,592. e^(−1,592): usando e^(−1,6) ≈ 0,2019 e e^(0,008) ≈ 1,008, o produto dá e^(−1,592) ≈ 0,2019 × 1,008 ≈ **0,2035**. Fração = 1 − 0,2035 = **0,7965**, ou seja, aproximadamente **80%** da subsidência térmica total já ocorreu aos 100 Ma.

**Saída esperada do código:** `t=30 → fração ≈ 0.380` e `t=100 → fração ≈ 0.797`, consistentes com os cálculos manuais (pequenas diferenças na terceira casa decimal são esperadas por arredondamento manual das exponenciais). A interpretação geológica direta: mais de um terço da subsidência térmica de uma bacia rifte acontece já nos primeiros 30 Ma — um período em que a bacia ainda pode reter registro estratigráfico sin-rift a imediatamente pós-rift —, mas pouco mais de 20% da subsidência total (1 − 0,797 = 0,203) ainda está por vir mesmo depois de 100 Ma, o que explica por que margens passivas continuam subsidindo lentamente por dezenas de milhões de anos depois que qualquer atividade extensional visível já cessou — um comportamento assintótico, nunca atingindo exatamente 100% em tempo finito, mas se aproximando dele progressivamente, à mesma taxa de decaimento exponencial vista no resfriamento oceânico da Aula 07.

## Recap relâmpago

- O **modelo de estiramento uniforme** de McKenzie (1978) descreve o afinamento litosférico pelo fator β, com subsidência de falha inicial (isostática) somada a subsidência térmica subsequente que decai exponencialmente, S(t)/S_max = 1 − e^(−t/τ), com τ da ordem de 50-65 Ma para litosfera continental de referência.
- Colisão continental **espessa** a crosta rapidamente demais para a condução acompanhar — o orógeno **aquece** antes de esfriar, um processo que dura dezenas a mais de cem milhões de anos e que, via a dependência exponencial de temperatura vista na Aula 08, **enfraquece** progressivamente a crosta profunda, favorecendo fluxo dúctil lateral em orógenos maduros.
- **Slab-pull** (arrasto gravitacional de uma placa subductada, ~10¹³ N/m) e **ridge-push** (deslizamento gravitacional a partir da topografia elevada da crista, ~10¹² N/m, uma ordem de grandeza menor) são as forças motoras clássicas da tectônica de placas — sua ação contra a resistência integrada da litosfera (o envelope de resistência da Aula 08) determina onde e quão rápido extensão ou colisão avançam.
- A **teoria da cunha crítica** (Davis, Suppe & Dahlen, 1983) explica a geometria em cunha de cinturões de dobramentos e empurrões como um equilíbrio entre resistência interna, atrito basal e inclinação topográfica — um ângulo crítico de equilíbrio, análogo a uma pilha de areia empurrada por um bulldozer.
- O exemplo numérico mostrou que ~38% da subsidência térmica ocorre nos primeiros 30 Ma pós-rifte, e ~80% aos 100 Ma — a mesma forma exponencial de relaxamento térmico presente em toda física de resfriamento condutivo vista neste módulo, desde a litosfera oceânica da Aula 07 até a bacia rifte desta aula, encerrando o módulo com essa continuidade física.

## Próxima aula

Nenhuma — última aula do Módulo 23. As próximas etapas da cadeia de produção deste curso (questionário e flashcards do módulo) tratam deste conjunto de nove aulas como uma unidade fechada. Ver [[23-modelagem-numerica-geodinamica-modulo|Módulo 23]] para o registro consolidado.

## Fontes

- Modelo de estiramento uniforme e subsidência de bacias rifte: McKenzie, D. (1978), "Some remarks on the development of sedimentary basins", *Earth and Planetary Science Letters*, 40(1), 25-32; Allen, P. A. & Allen, J. R., *Basin Analysis: Principles and Application to Petroleum Play Assessment*, 3ª ed. (2013), Wiley-Blackwell, capítulo sobre bacias de estiramento.
- Evolução termal de orógenos colisionais e trajetórias metamórficas pressão-temperatura-tempo: England, P. C. & Thompson, A. B. (1984), "Pressure—Temperature—Time paths of regional metamorphism I: Heat transfer during the evolution of regions of thickened continental crust", *Journal of Petrology*, 25(4), 894-928.
- Forças de slab-pull e ridge-push como motores da tectônica de placas, com estimativas de ordem de grandeza: Forsyth, D. & Uyeda, S. (1975), "On the relative importance of the driving forces of plate motion", *Geophysical Journal of the Royal Astronomical Society*, 43(1), 163-200, DOI 10.1111/j.1365-246X.1975.tb00631.x (o periódico foi renomeado para *Geophysical Journal International* em 1989, e é sob esse nome que o artigo hoje aparece indexado); Turcotte, D. L. & Schubert, G., *Geodynamics*, 3ª ed. (2014), Cambridge University Press, capítulo 6.
- Teoria da cunha crítica para cinturões de dobramentos e empurrões e prismas de acresção: Davis, D., Suppe, J. & Dahlen, F. A. (1983), "Mechanics of fold-and-thrust belts and accretionary wedges", *Journal of Geophysical Research*, 88(B2), 1153-1172; Dahlen, F. A. (1990), "Critical taper model of fold-and-thrust belts and accretionary wedges", *Annual Review of Earth and Planetary Sciences*, 18, 55-99.

<!--
nivel: avancado
palavras_corpo: 2283
mapa_objetivo_secao:
  geologia-avancado-m23-oa04: "Extensão continental: o modelo de estiramento uniforme" + "Colisão continental: por que os orógenos aquecem antes de esfriar" + "Forças motoras: slab-pull e ridge-push" + "Cunhas orogênicas: a geometria de um cinturão de empurrões" + "Exemplo trabalhado"

nota_de_revisao_didatica: 'Aula RENUMERADA de 07 para 09 em 2026-09-19, sem divisao (2.287 palavras, ~27 min estimados, dentro do teto), por causa das divisoes das antigas Aulas 03 e 04. Os claim_id foram DELIBERADAMENTE MANTIDOS com o prefixo A07, que designa a aula antes da renumeracao, para nao quebrar a rastreabilidade com o manifesto 23-modelagem-numerica-geodinamica-auditoria.json. NAO RENUMERAR. Alem das remissoes internas atualizadas para a nova numeracao, UMA correcao de redacao (achado DID-M23-A07-CONCORDANCIA-008, ja registrado pela auditoria cientifica como observacao fora de escopo): "a superficie subsidem quase instantaneamente" passou a "a superficie subside quase instantaneamente".'

alegacoes_auditaveis:
  - claim_id: GEODIN-M23-A07-MCKENZIE-001
    claim: "O modelo de estiramento uniforme de McKenzie (1978) descreve a subsidencia de bacias rifte como soma de uma subsidencia de falha inicial controlada pelo fator de estiramento beta (razao entre espessura litosferica original e apos o estiramento) e uma subsidencia termica subsequente que decai exponencialmente, S(t)/Smax = 1 - exp(-t/tau), com a constante de tempo termico tau da ordem de 50-65 Ma para uma litosfera continental de referencia de aproximadamente 125 km."
    risk: fato
    source: "McKenzie, D. (1978), Earth and Planetary Science Letters, 40(1), 25-32; Allen, P. A. & Allen, J. R., Basin Analysis, 3a ed. (2013), Wiley-Blackwell."
  - claim_id: GEODIN-M23-A07-OROGENO-AQUECE-002
    claim: "O espessamento crustal por colisao continental ocorre em escala de tempo rapida demais para a conducao de calor acompanhar, fazendo com que a crosta espessada tenda a aquecer nas dezenas de milhoes de anos seguintes ao espessamento antes de relaxar de volta a um perfil geotermico mais proximo do estavel, um processo que pode levar dezenas a mais de cem milhoes de anos; esse padrao termico e responsavel pela trajetoria metamorfica classica de enterramento seguido de aquecimento continuado e posterior resfriamento durante exumacao."
    risk: fato
    source: "England, P. C. & Thompson, A. B. (1984), Journal of Petrology, 25(4), 894-928."
  - claim_id: GEODIN-M23-A07-FORCAS-PLACA-003
    claim: "Estimativas classicas de ordem de grandeza situam a forca de slab-pull tipicamente em torno de 10^13 N por metro de comprimento de zona de subduccao, e a forca de ridge-push cerca de uma ordem de grandeza menor, em torno de 10^12 N/m, tornando o slab-pull geralmente a forca dominante no balanco de forcas de uma placa quando presente."
    risk: fato
    source: "Forsyth, D. & Uyeda, S. (1975), Geophysical Journal of the Royal Astronomical Society, 43(1), 163-200, DOI 10.1111/j.1365-246X.1975.tb00631.x (periodico renomeado Geophysical Journal International apenas em 1989); Turcotte & Schubert, Geodynamics, 3a ed. (2014), cap. 6."
  - claim_id: GEODIN-M23-A07-CUNHA-CRITICA-004
    claim: "A teoria da cunha critica (Davis, Suppe & Dahlen, 1983) trata um cinturao de dobramentos e empurrões ou um prisma de acrescao como um material plastico friccional (Coulomb) empurrado sobre um descolamento basal de baixa resistencia, mantendo um angulo de taper (soma da inclinacao topografica com o mergulho do descolamento basal) determinado pelo equilibrio entre resistencia interna, atrito basal e inclinacao topografica; abaixo do angulo critico a cunha se deforma internamente ate atingi-lo, acima dele avanca como um bloco relativamente rigido."
    risk: fato
    source: "Davis, D., Suppe, J. & Dahlen, F. A. (1983), Journal of Geophysical Research, 88(B2), 1153-1172; Dahlen, F. A. (1990), Annual Review of Earth and Planetary Sciences, 18, 55-99."
  - claim_id: GEODIN-M23-A07-EXEMPLO-SUBSIDENCIA-005
    claim: "Para tau=62.8 Ma, a fracao de subsidencia termica atingida em t=30 Ma e 1-exp(-30/62.8) = 0.3798 (38%), e em t=100 Ma e 1-exp(-100/62.8) = 0.7966 (80%), restando POUCO MAIS de 20% (0.2034) por vir depois de 100 Ma."
    risk: calculo
    source: "Calculo aritmetico direto a partir da formula de decaimento exponencial do modelo de McKenzie apresentada na aula, conferido por execucao (numpy 2.5.1: 0.37980 e 0.79655). O valor tau = 62.8 Ma reproduz tau = a^2/(pi^2 * kappa) do modelo original para a = 125 km e kappa = 8e-7 m2/s (62.7 Ma)."
-->
