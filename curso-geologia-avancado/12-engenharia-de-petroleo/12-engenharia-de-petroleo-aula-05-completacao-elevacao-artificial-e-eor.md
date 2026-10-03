# Aula 05: Completação, elevação artificial e recuperação avançada (EOR); gestão de reservatórios

**ID:** geologia-avancado-m12-a05
**Módulo:** [[12-engenharia-de-petroleo-modulo|Módulo 12 — Engenharia de petróleo]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** comparar métodos de recuperação secundária e avançada (EOR) quanto à aplicabilidade e ao ganho de recuperação, e situar completação e elevação artificial como as etapas de engenharia que conectam o reservatório à superfície ao longo da vida produtiva do poço.
**Ao final você vai conseguir:** descrever os principais tipos de completação e de elevação artificial e quando cada um se aplica; distinguir os três grandes grupos de EOR (térmico, miscível, químico) por mecanismo físico e por tipo de óleo ao qual se aplicam; e calcular o ganho de recuperação esperado de um projeto de EOR comparado à recuperação primária e secundária já obtidas.
**Pré-requisito:** Aula 04 deste módulo — mecanismos de produção primária, recuperação secundária por injeção de água e fator de recuperação.

## Conteúdo

### Completação: conectar o reservatório ao poço

Ao final da perfuração (Aula 01), o poço atravessa o reservatório, mas ainda não está pronto para produzir — falta a **completação** (*well completion*), o conjunto de operações e equipamentos que estabelece e controla o fluxo entre a formação e a superfície. A escolha central da completação é como o revestimento de produção se conecta à rocha-reservatório, e há duas famílias principais:

**Completação a poço revestido e canhoneado** (*cased-hole completion*): o revestimento de produção desce cimentado por toda a extensão do reservatório (como qualquer outra fase, Aula 01), e depois **canhoneios** (*perforations*) — pequenos furos disparados por cargas explosivas moldadas, descidas por cabo ou por tubos — atravessam o revestimento e o cimento, criando túneis de comunicação com a rocha. A vantagem é o controle preciso: só os intervalos desejados são canhoneados, e zonas de água ou de rocha de má qualidade dentro do mesmo reservatório podem ser deixadas isoladas.

**Completação a poço aberto** (*open-hole completion*): o revestimento de produção é assentado no topo do reservatório, e a seção que atravessa a própria rocha-reservatório não é revestida nem cimentada — o poço fica em contato direto com a formação. É mais simples e barata, e maximiza a área de contato entre poço e reservatório, mas oferece pouco ou nenhum controle seletivo sobre quais intervalos produzem, e é usada principalmente em reservatórios homogêneos, competentes (que não desmoronam sem revestimento) e sem zonas de água próximas a evitar.

Uma variante intermediária, comum em reservatórios de arenito mal consolidado ou friável — tipicamente rochas de **alta** permeabilidade e alta vazão, jovens e pouco cimentadas, não de baixa permeabilidade —, usa **controle de areia**. As duas soluções não são sinônimas: as **telas de contenção** (*sand screens*) podem ser instaladas sozinhas, filtrando os grãos na própria parede da coluna; no ***gravel pack***, a tela é combinada com o preenchimento do anular (em poço aberto ou nos túneis de canhoneio) por areia selecionada de alta permeabilidade, que faz a filtragem antes de o fluido chegar à tela. A função de ambas é impedir que grãos de rocha sejam arrastados junto com o fluido produzido — a produção de areia é um problema operacional real em rochas mal consolidadas, capaz de erodir equipamentos de superfície e de fundo de poço ao longo do tempo.

### Elevação artificial: quando o reservatório não empurra mais sozinho

A Aula 04 tratou a recuperação primária como movida pela diferença de pressão entre reservatório e superfície. Enquanto essa diferença for suficiente para vencer o peso da coluna de fluido no próprio poço e ainda entregar vazão econômica, o poço produz por **elevação natural** (*natural flow*). À medida que a pressão do reservatório declina — inevitável ao longo da vida produtiva, mesmo com recuperação secundária ativa — chega um ponto em que essa energia natural não é mais suficiente, e o poço precisa de **elevação artificial** (*artificial lift*) para continuar produzindo. Os métodos dominantes:

- **Bombeio mecânico** (*sucker rod pumping* — o cavalo-de-pau, ou *pumpjack*, símbolo visual mais reconhecível da produção de petróleo terrestre): uma bomba de fundo de poço, acionada por uma haste que se move para cima e para baixo a partir de um motor de superfície, eleva o fluido em ciclos. Simples, robusto e de baixo custo de manutenção, mas limitado em profundidade e em vazão, e menos adequado a poços muito desviados ou horizontais, onde o atrito da haste contra a parede do poço se torna problemático.
- **Bombeio centrífugo submerso** (*electrical submersible pump*, ESP): uma bomba multiestágio elétrica, submersa no próprio fluido produzido, é descida junto com a coluna de produção e alimentada por cabo elétrico da superfície. Suporta vazões e profundidades muito maiores que o bombeio mecânico, sendo o método dominante em poços de alta vazão e em ambientes offshore, mas é eletromecanicamente mais complexo, mais caro e mais sensível a produção de areia e a gás livre na sucção da bomba.
- **Gas lift**: gás comprimido é injetado no anular do poço e entra na coluna de produção por válvulas calibradas a profundidades específicas, reduzindo a densidade média da coluna de fluido e, com isso, a pressão hidrostática que o reservatório precisa vencer para produzir — o inverso conceitual do problema de controle de poço da Aula 01, onde se queria aumentar essa pressão. É flexível e lida bem com produção de areia e com poços desviados, mas depende de disponibilidade de gás comprimido em volume e pressão suficientes, um recurso nem sempre disponível no campo.

A escolha entre esses métodos, na prática, pondera profundidade, vazão desejada, desvio do poço, disponibilidade de energia elétrica ou de gás comprimido, e o custo de capital e operacional ao longo da vida remanescente do poço — não existe um método universalmente superior.

### Recuperação avançada (EOR): recuperando o que a água não desloca

A recuperação secundária por injeção de água (Aula 04) desloca óleo mecanicamente, mas deixa para trás uma fração significativa presa por forças capilares mesmo em zonas bem varridas, além de não alterar a viscosidade do óleo remanescente — uma limitação crítica em óleos pesados, cuja alta viscosidade os torna praticamente imóveis sob o gradiente de pressão típico de uma injeção de água convencional. A **recuperação avançada** (*enhanced oil recovery*, EOR, também chamada de recuperação terciária, embora nem sempre venha depois cronologicamente de uma fase secundária) reúne métodos que alteram as propriedades do fluido ou da interação rocha-fluido para liberar esse óleo remanescente, agrupados em três famílias:

**EOR térmico**: injeta calor no reservatório, tipicamente como vapor (*steam injection*, incluindo variantes como injeção cíclica de vapor e *steam flooding* contínuo), para reduzir drasticamente a viscosidade de óleos pesados e extrapesados — a viscosidade de muitos óleos pesados cai por ordens de grandeza com um aumento moderado de temperatura, tornando o EOR térmico o método dominante e às vezes o único economicamente viável para esse tipo de óleo (como nos grandes projetos de areias betuminosas e óleo pesado da bacia de Alberta, no Canadá, e de campos de óleo pesado venezuelanos). A combustão in situ (queima controlada de parte do próprio óleo dentro do reservatório) é uma variante térmica menos comum, tecnicamente mais complexa de controlar.

**EOR miscível**: injeta um fluido que se torna miscível (mistura-se completamente, sem interface física, eliminando a tensão interfacial que retém óleo por capilaridade) com o óleo do reservatório nas condições de pressão e temperatura locais — tipicamente CO₂ ou gás hidrocarboneto leve (metano, etano, GLP) injetado a alta pressão. O CO₂ miscível é particularmente relevante hoje por acoplar recuperação de óleo a armazenamento geológico de carbono (uma parte do CO₂ injetado permanece retida no reservatório ao final do projeto), tornando-o um dos poucos métodos de EOR com um argumento ambiental adicional além do estritamente econômico. Aplica-se melhor a óleos leves a médios, com pressão de reservatório suficiente para atingir miscibilidade (a *pressão mínima de miscibilidade*, que aumenta com a densidade/viscosidade do óleo).

**EOR químico**: injeta produtos químicos dissolvidos na água de injeção para melhorar sua capacidade de deslocar óleo — polímeros (aumentam a viscosidade da água injetada, reduzindo a diferença de mobilidade entre água e óleo e mitigando o canalização preferencial já visto na Aula 04), surfactantes (reduzem a tensão interfacial entre óleo e água, liberando óleo retido por capilaridade de forma análoga, em princípio físico, ao EOR miscível) e álcalis (reagem com ácidos orgânicos do próprio óleo para gerar surfactantes in situ, em formulações combinadas como o processo ASP — álcali-surfactante-polímero). É tecnicamente versátil, mas sensível à salinidade e à temperatura do reservatório e ao custo dos produtos químicos, o que historicamente limitou sua adoção em larga escala fora de projetos específicos bem caracterizados.

```
EOR por família: mecanismo físico dominante e aplicação típica

térmico   → reduz viscosidade do óleo (vapor, combustão in situ)     → óleo pesado/extrapesado
miscível  → elimina interface óleo-fluido injetado (CO2, gás leve)   → óleo leve/médio, pressão suficiente
químico   → melhora mobilidade/reduz tensão interfacial (polímero,
            surfactante, álcali)                                    → versátil, sensível a salinidade/custo
```
Nenhuma das três famílias é estritamente superior às outras — a escolha depende do tipo de óleo, das condições do reservatório e da economia local de cada projeto.

### Gestão de reservatórios: o fio que amarra o módulo inteiro

Tudo o que este módulo cobriu — perfuração e completação de poços, avaliação de formações por perfil e testemunho, propriedades de rocha e fluido, mecanismos de produção e testes de poço, e agora elevação artificial e EOR — converge na disciplina de **gestão de reservatórios** (*reservoir management*): o processo contínuo e iterativo de monitorar o comportamento real de um campo (pressão, produção, corte de água, corte de gás) contra o modelo geológico e de engenharia construído a partir dos dados de poço, atualizar esse modelo quando o comportamento observado diverge da previsão, e decidir, com base nele, onde perfurar poços adicionais, quando converter um poço produtor em injetor, quando instalar elevação artificial e quando (e se) justificar um projeto de EOR. A gestão de reservatórios só foi formalizada como disciplina autônoma a partir do início dos anos 1990 (Wiggins & Startzman, 1990; Satter et al., 1994; Thakur, 1996), consolidando a prática de projeto que a literatura clássica de injeção de água (Craig, 1971; Willhite, 1986) já vinha acumulando desde os anos 1970. Um princípio central da disciplina é que a gestão eficaz de um reservatório depende de decisões tomadas cedo na vida do campo — a malha de poços, o momento de iniciar injeção de água, a preservação de pressão acima do ponto de bolha — porque decisões corretivas tardias raramente recuperam o fator de recuperação perdido por decisões subótimas no início. É por isso que a integração entre geologia, geofísica e engenharia de reservatórios, o tema de fundo deste módulo inteiro, é tratada como disciplina central, não acessória, na indústria de petróleo.

## Exemplo trabalhado

**Situação:** o mesmo reservatório da Aula 03 (OOIP = 19.115.712 STB) foi produzido por depleção por gás em solução, alcançando um fator de recuperação primária de 18%. Um projeto de injeção de água subsequente elevou o fator de recuperação total (primária + secundária) para 32%. A empresa avalia agora um projeto piloto de EOR miscível com CO₂, com ganho incremental estimado de 12 pontos percentuais de fator de recuperação sobre o OOIP original. Calcule: (a) o volume já recuperado até o fim da recuperação secundária; (b) o volume adicional esperado do projeto de EOR; (c) o fator de recuperação final total, se o EOR for bem-sucedido.

**Resolução:**

(a) Volume recuperado até o fim da secundária = OOIP × FR total (primária+secundária)
= 19.115.712 × 0,32 ≈ 6.117.028 STB

(b) Volume adicional esperado do EOR = OOIP × ganho incremental de FR
= 19.115.712 × 0,12 ≈ 2.293.885 STB

(c) Fator de recuperação final total = FR já obtido + ganho incremental do EOR
= 32% + 12% = 44%

Volume total recuperado ao final do EOR = OOIP × 0,44 = 19.115.712 × 0,44 ≈ 8.410.913 STB

O projeto de EOR, se bem-sucedido, elevaria o volume total recuperado de aproximadamente 6,1 milhões para 8,4 milhões de barris — um ganho incremental de cerca de 2,3 milhões de barris. Note que esse ganho é **ligeiramente inferior** ao obtido pela própria recuperação secundária (32% − 18% = 14 pontos percentuais, ou cerca de 2,68 milhões de STB): 12 pontos percentuais rendem menos barris que 14 pontos aplicados ao mesmo OOIP. Os dois ganhos são da mesma ordem de grandeza, mas o do EOR é o menor — e é obtido sobre um campo já bastante depletado, a um custo por barril tipicamente muito mais alto. Esse tipo de comparação — o ganho absoluto em barris de cada etapa adicional de recuperação, não apenas o ganho percentual — é exatamente o número que justifica (ou não) o investimento adicional de capital em um projeto de EOR: mesmo um ganho percentual moderado pode representar um volume de negócio substancial quando aplicado a um OOIP suficientemente grande, o que explica por que projetos de EOR se concentram preferencialmente em campos maduros de grande volume original, onde mesmo poucos pontos percentuais adicionais de recuperação justificam o investimento.

## Erros comuns

- **Associar controle de areia a rocha de baixa permeabilidade.** É o oposto: telas e gravel pack existem justamente para os arenitos jovens, pouco cimentados e de **alta** permeabilidade e alta vazão, onde grãos soltos migram com o fluido.
- **Tratar telas de contenção e gravel pack como sinônimos.** São soluções distintas — a tela sozinha filtra na própria coluna; o gravel pack acrescenta uma camada de areia selecionada no anular antes da tela. Confundir as duas é confundir duas engenharias de custo e desempenho diferentes.
- **Escolher elevação artificial só pela vazão ou só pela profundidade.** A escolha real pondera profundidade, vazão, desvio do poço e disponibilidade de energia elétrica ou gás comprimido simultaneamente — um ESP de alta vazão não serve de nada sem energia elétrica confiável no local.
- **Comparar EOR só em pontos percentuais de fator de recuperação, sem converter para barris.** O próprio exemplo trabalhado mostra que 12 pontos percentuais no EOR rendem menos barris que os 14 pontos da secundária anterior sobre o mesmo OOIP — decisão de investimento se faz em volume absoluto, não só em percentual.

## O que não concluir

- **Que existe um método de elevação artificial universalmente superior.** Não existe: cada um tem seu nicho de profundidade, vazão, desvio de poço e disponibilidade de energia — a aula é explícita nisso.
- **Que EOR é sempre a etapa final que "recupera tudo que sobrou".** Mesmo um projeto de EOR bem-sucedido deixa óleo para trás; o ganho é incremental e tipicamente menor, em pontos percentuais, que o da recuperação secundária que o precedeu.
- **Que gestão de reservatórios é uma etapa isolada no fim do processo.** É um ciclo contínuo desde a primeira decisão de malha de poços — decisões tardias raramente compensam decisões subótimas tomadas cedo, o oposto de um "conserto de fim de vida".

## Recap relâmpago

- A completação conecta reservatório e poço: a poço revestido e canhoneado (controle seletivo por intervalo) ou a poço aberto (mais simples, sem seletividade, exige rocha competente e homogênea); o controle de areia (telas isoladas ou gravel pack, soluções distintas) lida com arenito mal consolidado, tipicamente de alta permeabilidade.
- A elevação artificial (bombeio mecânico, ESP, gas lift) assume a produção quando a energia natural do reservatório não é mais suficiente; a escolha depende de profundidade, vazão, desvio do poço e disponibilidade de energia elétrica ou gás comprimido.
- EOR térmico (vapor, combustão in situ) reduz viscosidade e domina em óleo pesado/extrapesado; EOR miscível (CO₂, gás leve) elimina a interface óleo-fluido e aplica-se a óleo leve/médio com pressão de reservatório suficiente; EOR químico (polímero, surfactante, álcali) melhora mobilidade/reduz tensão interfacial e é versátil mas sensível a salinidade e custo.
- O ganho de um projeto de EOR deve ser avaliado tanto em pontos percentuais de fator de recuperação quanto em volume absoluto (OOIP × ganho de FR) — o segundo é o que efetivamente justifica investimento.
- Gestão de reservatórios integra todo o conteúdo do módulo em um ciclo contínuo de monitorar, atualizar o modelo e decidir; decisões de malha de poços e momento de injeção tomadas cedo na vida do campo dificilmente são compensadas por correções tardias.

## Encerramento do módulo

Este módulo percorreu a cadeia completa da engenharia de petróleo: construir o poço (Aula 01), avaliar a formação que ele atravessa (Aula 02), caracterizar rocha e fluido para calcular quanto hidrocarboneto existe (Aula 03), entender como e quanto desse volume é produzido naturalmente e por injeção de água (Aula 04), e completar essa cadeia com os métodos que sustentam a produção ao longo da vida do poço e recuperam o que os métodos convencionais deixam para trás (Aula 05). Isso fecha a Área IX — Especializações aplicadas do curso; o próximo módulo inicia a Área X, de métodos quantitativos e geoinformação.

## Anterior

[[12-engenharia-de-petroleo-aula-04-mecanismos-de-producao-e-testes-de-poco|Aula 04 — Mecanismos de produção, recuperação primária e secundária e testes de poço]]

## Fontes

- Bellarby, J. (2009), *Well Completion Design*, Elsevier Developments in Petroleum Science 56, cap. 1-3, 9 (poço revestido/canhoneado vs. poço aberto, controle de areia).
- Brown, K. E. (1980), *The Technology of Artificial Lift Methods*, PennWell, cap. 1-2 (bombeio mecânico, ESP, gas lift).
- Green, D. W. & Willhite, G. P. (2018), *Enhanced Oil Recovery*, 2ª ed., SPE Textbook Series, cap. 1, 3, 5, 7 (EOR térmico, miscível, químico).
- Lake, L. W. (1989), *Enhanced Oil Recovery*, Prentice Hall, cap. 1-2 (visão geral e classificação dos métodos de EOR).
- Craig, F. F. (1971), *The Reservoir Engineering Aspects of Waterflooding*, SPE Monograph 3 (fundamentos de gestão de projetos de injeção de água).
- Satter, A. & Thakur, G. C. (1994), *Integrated Petroleum Reservoir Management*, PennWell, cap. 1 (princípios de gestão de reservatórios).
- Wiggins, M. L. & Startzman, R. A. (1990), "An Approach to Reservoir Management", SPE-20747-MS, SPE Annual Technical Conference and Exhibition, New Orleans (formalização da gestão de reservatórios como disciplina).
- Willhite, G. P. (1986), *Waterflooding*, SPE Textbook Series 3 (literatura clássica de injeção de água que antecede a disciplina).

<!--
nivel: avancado
palavras_corpo: 2060
mapa_objetivo_secao:
  geologia-avancado-m12-oa04: "Completação: conectar o reservatório ao poço" + "Elevação artificial: quando o reservatório não empurra mais sozinho" + "Recuperação avançada (EOR): recuperando o que a água não desloca" + "Gestão de reservatórios: o fio que amarra o módulo inteiro" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: PETRENG-M12-A05-COMPLETACAO-001
    claim: "Completação a poço revestido e canhoneado desce revestimento de produção cimentado por toda a extensão do reservatório e usa canhoneios (perfurações por cargas explosivas moldadas) para criar comunicação seletiva com a formação; completação a poço aberto deixa a seção reservatório sem revestimento nem cimento, sendo mais simples e barata mas sem controle seletivo de intervalos, aplicável a reservatórios homogêneos e competentes. O controle de areia (telas de contencao instaladas sozinhas, ou gravel pack, em que a tela e combinada com o preenchimento do anular por areia selecionada de alta permeabilidade) aplica-se a arenitos mal consolidados ou friaveis, tipicamente de ALTA permeabilidade e alta vazao — nao de baixa permeabilidade; telas isoladas e gravel pack sao solucoes distintas, nao sinonimos."
    risk: fato
    source: "Bellarby 2009, Well Completion Design, cap. 1-3"
  - claim_id: PETRENG-M12-A05-ELEVACAO-002
    claim: "Os três principais métodos de elevação artificial são bombeio mecânico (sucker rod pumping/pumpjack, robusto e barato mas limitado em profundidade/vazão), bombeio centrífugo submerso (ESP, elétrico, suporta vazões e profundidades maiores, dominante offshore, mais sensível a areia e gás livre) e gas lift (injeção de gás no anular para reduzir a densidade da coluna de fluido, flexível e tolerante a poços desviados e produção de areia, mas dependente de gás comprimido disponível)."
    risk: fato
    source: "Brown 1980, The Technology of Artificial Lift Methods, cap. 1-2"
  - claim_id: PETRENG-M12-A05-EOR-003
    claim: "A recuperação avançada (EOR) se divide em três famílias por mecanismo físico: térmico (injeção de vapor ou combustão in situ, reduz viscosidade, dominante em óleo pesado/extrapesado), miscível (CO2 ou gás hidrocarboneto leve injetado a pressão suficiente para eliminar a interface com o óleo, aplicável a óleo leve/médio, com a pressão mínima de miscibilidade aumentando com a densidade/viscosidade do óleo) e químico (polímeros, surfactantes e álcalis, que melhoram a mobilidade da água injetada ou reduzem a tensão interfacial, sensível a salinidade, temperatura e custo)."
    risk: fato
    source: "Green & Willhite 2018, Enhanced Oil Recovery, cap. 1, 3, 5, 7; Lake 1989, Enhanced Oil Recovery, cap. 1-2"
  - claim_id: PETRENG-M12-A05-CO2-004
    claim: "A injeção miscível de CO2 para EOR pode acoplar recuperação de óleo a armazenamento geológico de carbono, já que parte do CO2 injetado permanece retido no reservatório ao final do projeto."
    risk: fato
    source: "Green & Willhite 2018, Enhanced Oil Recovery, cap. 5 (miscible gas flooding e CO2-EOR)"
  - claim_id: PETRENG-M12-A05-GESTAO-005
    claim: "Gestão de reservatórios é o processo contínuo de monitorar o comportamento observado de um campo (pressão, produção, corte de água/gás) contra o modelo geológico-de engenharia, atualizar esse modelo e decidir ações operacionais (poços adicionais, conversão para injetor, elevação artificial, projetos de EOR); decisões tomadas cedo na vida do campo (malha de poços, momento de início de injeção de água) têm impacto desproporcional no fator de recuperação final e raramente são compensadas por correções tardias. A disciplina foi formalizada como tal no inicio dos anos 1990 (Wiggins & Startzman 1990; Satter et al. 1994; Thakur 1996), e nao nos anos 1970-80 por Craig/Willhite — estes sao a literatura classica de waterflooding sobre a qual ela se apoiou."
    risk: fato
    source: "Satter & Thakur 1994, Integrated Petroleum Reservoir Management, cap. 1; Wiggins & Startzman 1990, SPE ATCE, 'An Approach to Reservoir Management'; Craig 1971, The Reservoir Engineering Aspects of Waterflooding, SPE Monograph 3"
-->
