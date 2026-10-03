# Aula 05: Rejeitos de mineração: características geotécnicas, técnicas de disposição e estruturas de contenção

**ID:** geologia-avancado-m08-a05
**Módulo:** [[08-geotecnia-ambiental-modulo|Módulo 08 — Geotecnia ambiental]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** caracterizar geotecnicamente a lama e o rejeito arenoso, distinguir os métodos construtivos de barragem (montante, jusante, linha de centro) e as tecnologias de rejeito espessado, em pasta e filtrado, explicar a liquefação estática e sua relação com as rupturas de Fundão e da Mina do Feijão, e situar o monitoramento, o fator de segurança de projeto e a descaracterização.

**Pré-requisito:** resistência ao cisalhamento, comportamento drenado × não drenado, contração e dilatância ([[06-elementos-de-geomecanica/06-elementos-de-geomecanica-aula-06-resistencia-ao-cisalhamento-e-prospeccao-geotecnica|Módulo 06, Aula 06]]); tensão efetiva e poropressão ([[06-elementos-de-geomecanica/06-elementos-de-geomecanica-aula-03-tensoes-totais-efetivas-neutras-k0|Módulo 06, Aula 03]]); adensamento ([[06-elementos-de-geomecanica/06-elementos-de-geomecanica-aula-05-compressibilidade-adensamento-recalques|Aula 05]]); estabilidade de taludes ([[07-mapeamento-geotecnico/07-mapeamento-geotecnico-aula-03-cartas-derivadas-aptidao-suscetibilidade-risco|Módulo 07, Aula 03]]).

## Antes de começar, você precisa saber

- Que uma areia fofa saturada, ao ser cisalhada sem drenagem, tende a **contrair**, gera excesso de poropressão positivo, perde `σ'` e pode perder resistência abruptamente; uma areia densa dilata e ganha resistência (Módulo 06, Aula 06).
- Que a resistência não drenada `su` de um solo contrátil pode ser uma fração pequena da tensão efetiva de confinamento, muito abaixo da resistência drenada (Módulo 06, Aula 06).

## Conteúdo

### O que é rejeito, e por que ele é difícil

No beneficiamento mineral, a rocha lavrada é britada e moída, e o mineral de interesse é separado. Sobra o **rejeito**: a fração sem valor econômico, descartada em geral como **polpa** (mistura de sólidos finos e água) bombeada para uma estrutura de contenção. Não confundir com o **estéril**, a rocha removida para acessar o minério, disposta seca em pilhas.

O rejeito é geotecnicamente problemático por três razões: é produzido continuamente por décadas, em volume enorme; chega saturado e fofo; e sua granulometria varia muito conforme o minério e o processo.

### Lama versus rejeito arenoso

Ao ser lançado numa estrutura, o rejeito **segrega hidraulicamente**: as partículas grossas depositam perto do ponto de descarga, formando a **praia**, e as finas são carreadas para o interior do reservatório, formando a **lama** decantada.

| | Rejeito arenoso (*sands*) | Lama (*slimes*) |
|---|---|---|
| Granulometria | Areia fina a silte | Silte a argila |
| Plasticidade | Não plástico | Baixa a média plasticidade |
| Condutividade hidráulica | Média — drena | Muito baixa — retém água |
| Adensamento | Rápido | Muito lento; densidade baixa por muito tempo |
| Resistência | Friccional; se fofo e saturado, suscetível a liquefação | Baixa; alta compressibilidade |

O rejeito arenoso, quando compactado e drenado, é bom material de construção de aterro. Fofo e saturado, é o material mais perigoso da geotecnia. A lama nunca é material de construção — é carga a conter.

### Métodos construtivos de barragem de rejeito

A barragem cresce com a mina. Três geometrias de alteamento:

- **Montante (*upstream*):** cada novo alteamento se apoia parcialmente sobre a praia de rejeito depositada no ciclo anterior. É o mais barato e o de menor consumo de material, e **o mais perigoso**: o corpo da barragem incorpora rejeito não compactado, potencialmente fofo e saturado, e o eixo se desloca sobre esse material. Foi a geometria de Fundão e da Barragem I da Mina do Feijão.
- **Jusante (*downstream*):** cada alteamento é lançado a jusante do anterior, sobre fundação preparada e material compactado. É o mais seguro e o mais caro, com maior footprint e volume de aterro.
- **Linha de centro (*centerline*):** solução intermediária — o eixo da crista permanece fixo e o alteamento cresce meio para montante, meio para jusante.

> [!warning] Legislação de barragens de rejeito mudou depois de Mariana e Brumadinho — confirme o texto vigente
> A proibição do método a montante e a exigência de descaracterização apareceram primeiro na **Resolução ANM nº 4/2019**, editada semanas após Brumadinho, e foram depois elevadas a lei: a Lei 12.334/2010 (Política Nacional de Segurança de Barragens) foi alterada pela **Lei 14.066/2020**, que proibiu novas barragens alteadas a montante e determinou a **descaracterização** das existentes em prazos definidos. A **Resolução ANM nº 95/2022** consolidou as regras de segurança de barragens de mineração (antes dispersas em portarias do DNPM/ANM, entre elas a Portaria 70.389/2017). O padrão internacional de referência é o **GISTM — Global Industry Standard on Tailings Management** (2020). Prazos e exigências de detalhe evoluem; reconfirme antes de fundamentar parecer.

### Tecnologias que reduzem a água livre

A alternativa estrutural ao problema é retirar água do rejeito antes de dispô-lo, em ordem crescente de desaguamento:

- **Espessado (*thickened*):** adensado em espessadores até um teor de sólidos que elimina a segregação e permite disposição em pilha de baixa declividade, ainda bombeável.
- **Pasta (*paste*):** desaguado além do espessado, com consistência que não exsuda água livre ao ser depositado.
- **Filtrado (*filtered* / *dry stack*):** desaguado por filtros-prensa até umidade próxima da ótima de compactação, transportado por correia ou caminhão e **compactado** como um aterro convencional. Elimina a barragem e o risco de liquefação, ao custo de energia e operação de filtragem — hoje a solução preferida para novos empreendimentos onde é viável.

### Liquefação: o comportamento não intuitivo

**Liquefação** é a perda súbita e grande de resistência de um solo granular fofo e saturado quando o cisalhamento não drenado leva a poropressão a subir e a tensão efetiva a cair a valores muito baixos. O solo passa a se comportar como um líquido viscoso e flui.

- **Liquefação cíclica:** deflagrada por carregamento cíclico rápido — um sismo.
- **Liquefação estática:** deflagrada **sem necessidade de sismo**, por qualquer processo que empurre um rejeito contrátil saturado para a ruptura não drenada: alteamento rápido demais para o rejeito adensar, elevação do nível freático, sobrecarga, erosão interna, ruptura local que redistribui tensão. Foi o mecanismo identificado nos painéis técnicos independentes de **Fundão** (Samarco, Mariana, 2015) e da **Barragem I da Mina do Feijão** (Vale, Brumadinho, 2019).

> [!note] Uma ressalva sobre Fundão
> Em Fundão o painel de Morgenstern et al. (2016) registrou **três pequenos eventos sísmicos** cerca de 90 min antes do colapso e concluiu que podem ter **acelerado** um processo já em curso — não que o tenham causado; a causa fundamental foi a perda de confinamento por extrusão lateral da lama. Em Feijão I não houve gatilho externo algum. A lição: quando o material já está no limiar, o gatilho pode ser desprezível.

O ponto que contraria a intuição: a resistência **não cai a zero**. Ela desaba de um valor drenado alto para um patamar não drenado baixo e **aproximadamente constante** — a resistência liquefeita `su(liq)`, tipicamente 5 a 12 % da tensão efetiva vertical para rejeito fofo. É essa resistência residual que governa a distância que a massa liquefeita percorre (*runout*) — que em Fundão e Feijão foi de quilômetros.

### Monitoramento, fator de segurança e descaracterização

**Monitoramento:** piezômetros (a poropressão é o parâmetro crítico — ela precede a ruptura), inclinômetros, marcos superficiais, medidores de vazão dos drenos, e cada vez mais **InSAR** (interferometria de radar de satélite) para deslocamento milimétrico de superfície em toda a face. Sistemas de alerta e planos de ação emergencial (PAE) são obrigatórios.

**Fator de segurança de projeto:** a prática pós-Brumadinho exige verificação em **condição não drenada com resistência de pico e pós-pico** sempre que houver material contrátil saturado, não bastando a análise drenada. Faixas usuais: `FS ≥ 1,5` para condição de longo prazo drenada, `FS ≥ 1,3` para condição não drenada, com exigências específicas por classe de risco na regulamentação da ANM.

**Descaracterização:** processo de reprocessar, remover ou estabilizar o rejeito e reconformar a estrutura de modo que ela **deixe de ser uma barragem** — sem lâmina d'água, sem risco de ruptura por fluxo. É a obrigação legal imposta às barragens a montante pela Lei 14.066/2020.

## Exemplo trabalhado

**Situação:** analisa-se um elemento de rejeito arenoso fofo saturado na face de jusante de uma barragem alteada a montante, a `z = 15 m` de profundidade abaixo da superfície do talude, sob inclinação `β = 12°`. `γsat = 20 kN/m³`, lençol **na superfície com fluxo paralelo ao talude**, `γw = 9,81 kN/m³`, `φ' = 33°`. A razão de resistência liquefeita estimada por ensaios é `su(liq)/σ'v0 = 0,10`. Compare o fator de segurança na análise **drenada** e na análise **não drenada pós-liquefação**. Use o modelo de talude infinito do Módulo 07, Aula 03.

**Resolução:**

**Tensão cisalhante motriz** — o peso que empurra é o **total**, não o submerso:
`τ = γsat·z·sen β·cos β = 20 × 15 × 0,2079 × 0,9781 = 300 × 0,2034 = 61,0 kPa`

**Tensões efetivas no elemento** (fluxo paralelo, `u = γw·z·cos²β`):
`σ'v0 = (γsat − γw)·z = 10,19 × 15 = 152,9 kPa`
`σ'n = (γsat − γw)·z·cos²β = 152,9 × 0,9568 = 146,2 kPa`

**(a) Análise drenada.**
`τf,drenada = σ'n · tan φ' = 146,2 × tan 33° = 146,2 × 0,6494 = 95,0 kPa`
`FS_drenado = 95,0 / 61,0 ≈ 1,56`

**(b) Análise não drenada pós-liquefação.**
`su(liq) = 0,10 × σ'v0 = 0,10 × 152,9 = 15,3 kPa`
`FS_liq = 15,3 / 61,0 ≈ 0,25`

**Interpretação:** repare no que o par de números diz. Pela conta drenada convencional o talude tem `FS ≈ 1,56` — **passa** no critério regulamentar de 1,5, e um projeto assim seria aprovado. Levado à ruptura não drenada, o mesmo talude, com a mesma geometria e o mesmo material, tem `FS ≈ 0,25`: já rompeu. A diferença não é um refinamento de segunda ordem; é a diferença entre uma estrutura que atende à norma no papel e uma estrutura que flui. Se um gatilho qualquer — um alteamento rápido demais para o rejeito adensar, uma elevação do nível freático por chuva, uma pequena ruptura localizada que transfere carga — dispara a resposta não drenada, a resistência cai de ~95 kPa para ~15 kPa, e a massa flui, mantida em movimento pela baixa resistência residual `su(liq)`.

É por isso que, havendo rejeito fofo saturado, **a análise drenada isolada não é suficiente**, e é por isso que a legislação passou a proibir a geometria de montante, que constrói a barragem sobre esse material.

## Erros comuns

- **Confundir rejeito com estéril**: o estéril é rocha, disposto seco em pilha; o rejeito é a fração processada, em geral polpa saturada.
- **Verificar a estabilidade de estrutura com rejeito contrátil saturado só pela análise drenada.** É preciso a verificação não drenada com resistência de pico e pós-pico.
- **Tratar um talude percolado como talude submerso**, usando o peso submerso também no esforço motriz. Com lençol na superfície e fluxo paralelo, o esforço motriz é `γsat·z·sen β·cos β` (peso total) e só a tensão normal efetiva usa `γsub` — trocar os dois superestima o `FS` por um fator próximo de `γsat/γsub`.
- **Achar que liquefação zera a resistência.** Ela cai a um patamar `su(liq)` baixo e aproximadamente constante — é esse patamar que define o runout.
- **Tratar a barragem a montante como "igual, só mais barata".** Ela incorpora rejeito não compactado no corpo da estrutura, e é essa a diferença que a torna proibida no Brasil.
- **Subestimar o tempo de adensamento da lama.** Ela retém água e permanece fofa e de baixa resistência por décadas — não se pode contar com ganho de resistência rápido.
- **Ignorar a poropressão no monitoramento.** É o parâmetro que precede a ruptura; deslocamento visível já é tarde.

## O que não concluir

- **Que rejeito filtrado elimina todo o risco geotécnico.** Elimina a barragem e a liquefação de fluxo, mas a pilha compactada ainda precisa de drenagem, controle de compactação e estabilidade de taludes, e o filtrado pode reumedecer.
- **Que `FS` drenado alto significa estrutura segura.** Se há material contrátil saturado, o `FS` que importa é o não drenado.
- **Que a descaracterização torna a área imediatamente segura e livre.** É um processo de anos, com riscos próprios durante a execução (manuseio de rejeito potencialmente instável) e monitoramento continuado.
- **Que as rupturas de Fundão e Feijão foram eventos imprevisíveis.** Os painéis técnicos independentes identificaram mecanismos de liquefação estática associados a condições construtivas e de drenagem conhecidas e monitoráveis.

## Recap relâmpago

- Rejeito é a fração processada sem valor, disposta em geral como polpa saturada; estéril é rocha disposta seca. Ao ser lançado, o rejeito segrega em praia arenosa (drena, friccional) e lama (silte-argila, retém água, adensa lentamente, baixa resistência).
- Métodos de alteamento: **montante** (barato, incorpora rejeito fofo no corpo, o mais perigoso — proibido para novas barragens no Brasil), **jusante** (seguro, caro), **linha de centro** (intermediário).
- Espessado, pasta e filtrado retiram água antes da disposição; o filtrado (*dry stack*) é compactado como aterro e elimina barragem e liquefação de fluxo.
- **Liquefação** é a perda súbita de resistência de solo granular fofo saturado sob cisalhamento não drenado; a **estática** ocorre sem sismo e foi o mecanismo de Fundão (2015) e Feijão I (2019). A resistência não zera: cai a `su(liq) ≈ 5–12 % de σ'v0`, que governa o runout.
- O monitoramento prioriza a **poropressão** (piezômetros), com inclinômetros, marcos e InSAR; a verificação de estabilidade deve incluir a condição **não drenada** quando há material contrátil saturado.
- A **descaracterização** reconforma a estrutura para que deixe de ser barragem — obrigação legal para as barragens a montante (Lei 14.066/2020; Resolução ANM 95/2022 — verificar o texto vigente).

## Próxima aula

[[08-geotecnia-ambiental-aula-06-recuperacao-e-remediacao|Aula 06 — Recuperação de áreas degradadas, remediação de solo e aquífero e uso de resíduos em projetos geotécnicos]]

## Anterior

[[08-geotecnia-ambiental-aula-04-aterros-sanitarios-liners-e-recalques|Aula 04 — Aterros sanitários: liners, barreiras de cobertura, projeto, operação, monitoramento e recalques]]

## Fontes

- Vick, S. G. (1990), *Planning, Design, and Analysis of Tailings Dams*, BiTech Publishers, Vancouver.
- Robertson, P. K., de Melo, L., Williams, D. J. & Wilson, G. W. (2019), *Report of the Expert Panel on the Technical Causes of the Failure of Feijão Dam I*, publicado por Vale S.A.
- Morgenstern, N. R., Vick, S. G., Viotti, C. B. & Watts, B. D. (2016), *Report on the Immediate Causes of the Failure of the Fundão Dam*, Fundão Tailings Dam Review Panel.
- ICMM, UNEP & PRI (2020), *Global Industry Standard on Tailings Management (GISTM)*.
- Jefferies, M. & Been, K. (2016), *Soil Liquefaction: A Critical State Approach*, 2ª ed., CRC Press, cap. 2 e 8.
- Blight, G. (2010), *Geotechnical Engineering for Mine Waste Storage Facilities*, CRC Press.
- Brasil, Lei nº 12.334/2010 (Política Nacional de Segurança de Barragens), alterada pela Lei nº 14.066, de 30 de setembro de 2020; Agência Nacional de Mineração, Resolução ANM nº 4, de 15 de fevereiro de 2019 (primeira proibição do alteamento a montante e prazos de descaracterização) e Resolução ANM nº 95, de 7 de fevereiro de 2022 (consolidação). *Consultar o texto consolidado vigente.*
- Robertson, P. K. (2010), "Evaluation of flow liquefaction and liquefied strength using the cone penetration test", *Journal of Geotechnical and Geoenvironmental Engineering, ASCE*, 136(6), p. 842–853.

<!--
nivel: avancado
palavras_corpo: ~2050
# Ressalva registrada na revisão didática (DID-M08-A05-EXTENSAO): acima do teto de ~1900,
# mantida por decisão — o excedente está na ressalva sobre Fundão e no exemplo trabalhado,
# que carregam o conceito mais difícil do módulo. Ver 08-geotecnia-ambiental-revisao-didatica.md.

mapa_objetivo_secao:
  geologia-avancado-m08-oa03: "O que é rejeito, e por que ele é difícil" + "Lama versus rejeito arenoso" + "Métodos construtivos de barragem de rejeito" + "Tecnologias que reduzem a água livre" + "Liquefação: o comportamento não intuitivo" + "Monitoramento, fator de segurança e descaracterização" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOAMB-M08-A05-REJEITO-ESTERIL-001
    claim: "Rejeito é a fração sem valor econômico gerada no beneficiamento mineral, descartada em geral como polpa saturada bombeada para estrutura de contenção; estéril é a rocha removida para acessar o minério, disposta seca em pilha. Ao ser lançado, o rejeito segrega hidraulicamente em praia arenosa junto ao ponto de descarga e lama fina no interior do reservatório."
    risk: fato
    source: "Vick 1990, cap. 1 e 3; Blight 2010"
  - claim_id: GEOAMB-M08-A05-LAMA-ARENOSO-002
    claim: "O rejeito arenoso (areia fina a silte, não plástico) drena, adensa rápido e é friccional, sendo bom material de construção quando compactado e drenado, mas suscetível a liquefação quando fofo e saturado; a lama (silte a argila, baixa a média plasticidade) tem condutividade muito baixa, adensa lentamente e permanece de baixa densidade e baixa resistência por décadas."
    risk: fato
    source: "Vick 1990, cap. 4; Blight 2010"
  - claim_id: GEOAMB-M08-A05-METODOS-003
    claim: "A barragem de rejeito é alteada por método de montante (apoio parcial sobre a praia do ciclo anterior — mais barato e mais perigoso, pois incorpora rejeito não compactado no corpo), de jusante (sobre fundação preparada e material compactado — mais seguro e mais caro) ou de linha de centro (eixo da crista fixo). Fundão e a Barragem I da Mina do Feijão eram alteadas a montante."
    risk: fato
    source: "Vick 1990, cap. 6; Morgenstern et al. 2016; Robertson et al. 2019"
  - claim_id: GEOAMB-M08-A05-DESAGUAMENTO-004
    claim: "As tecnologias de rejeito espessado, em pasta e filtrado retiram água antes da disposição em grau crescente; o rejeito filtrado (dry stack) é desaguado por filtros-prensa até umidade próxima da ótima de compactação e disposto compactado como aterro, eliminando a barragem e o risco de liquefação de fluxo, ao custo de energia de filtragem."
    risk: fato
    source: "Blight 2010; Davies, M. P. (2011), 'Filtered dry stacked tailings', Proc. Tailings and Mine Waste 2011"
  - claim_id: GEOAMB-M08-A05-LIQUEFACAO-005
    claim: "A liquefação estática é a perda súbita e grande de resistência de um solo granular fofo e saturado quando o cisalhamento não drenado eleva a poropressão e reduz a tensão efetiva, deflagrada sem necessidade de sismo por alteamento rápido, elevação do nível freático, sobrecarga, erosão interna ou ruptura local; foi o mecanismo identificado pelos painéis técnicos independentes de Fundão (2015) e da Barragem I da Mina do Feijão (2019). Ressalva de precisão: em Fundão o painel registrou três pequenos eventos sísmicos ~90 min antes do colapso e os considerou possíveis ACELERADORES de um processo já em curso, não a causa — a causa fundamental foi a perda de confinamento por extrusão lateral da lama; em Feijão I não houve gatilho externo."
    risk: fato
    source: "Morgenstern et al. 2016 (Fundão Tailings Dam Review Panel); Robertson et al. 2019 (Expert Panel, Feijão Dam I); Jefferies & Been 2016, cap. 2"
  - claim_id: GEOAMB-M08-A05-SU-LIQ-006
    claim: "Na liquefação de fluxo a resistência não cai a zero: desaba de um valor drenado alto para um patamar não drenado baixo e aproximadamente constante (resistência liquefeita su(liq)), tipicamente 5 a 12 % da tensão efetiva vertical para rejeito fofo, que governa a distância de runout da massa mobilizada."
    risk: fato
    source: "Robertson 2010; Jefferies & Been 2016, cap. 8; Robertson et al. 2019"
  - claim_id: GEOAMB-M08-A05-DESCARACT-007
    claim: "A proibição do alteamento a montante e a exigência de descaracterização foram introduzidas pela Resolução ANM nº 4/2019 e depois elevadas a lei: a Lei 14.066/2020 alterou a Política Nacional de Segurança de Barragens (Lei 12.334/2010) para proibir novas barragens de rejeito alteadas a montante e determinar a descaracterização das existentes; a Resolução ANM nº 95/2022 consolidou as regras de segurança de barragens de mineração (antes dispersas, entre elas a Portaria DNPM 70.389/2017), e o GISTM (2020) é o padrão internacional de referência."
    risk: desatualizavel
    source: "Resolução ANM nº 4/2019; Brasil, Lei nº 14.066/2020 (altera a Lei nº 12.334/2010); Resolução ANM nº 95/2022; ICMM/UNEP/PRI 2020 (GISTM)"
  - claim_id: GEOAMB-M08-A05-EXEMPLO-008
    claim: "Para um elemento de rejeito fofo saturado a z = 15 m sob talude de β = 12°, γsat = 20 kN/m³, lençol na superfície com fluxo paralelo ao talude, φ' = 33° e su(liq)/σ'v0 = 0,10: τ motriz = γsat·z·sen β·cos β = 61,0 kPa; σ'v0 = 152,9 kPa; σ'n = 146,2 kPa; FS drenado ≈ 1,56 e FS não drenado pós-liquefação ≈ 0,25. O esforço motriz usa o peso TOTAL e a resistência usa o peso SUBMERSO — usar o peso submerso nos dois lados (hipótese de talude submerso) dobraria indevidamente o FS drenado."
    risk: calculo
    source: "Modelo de talude infinito com percolação paralela (Módulo 07, Aula 03; mesma formulação usada na Aula 02 deste módulo); razão de resistência liquefeita de Robertson 2010"
-->
