# Aula 03: Resíduos sólidos e seleção de áreas de disposição: Política Nacional de Resíduos Sólidos e plumas de contaminação

**ID:** geologia-avancado-m08-a03
**Módulo:** [[08-geotecnia-ambiental-modulo|Módulo 08 — Geotecnia ambiental]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** classificar resíduos sólidos, situar a disposição final na hierarquia da Política Nacional de Resíduos Sólidos, aplicar critérios geológico-geotécnicos de seleção de áreas de aterro e explicar a geração e a evolução da pluma de contaminação por lixiviado.

**Pré-requisito:** carga contaminante e fontes de contaminação ([[03-contaminacao-aguas-subterraneas/03-contaminacao-aguas-subterraneas-aula-01-conceito-de-contaminacao-e-fontes|Módulo 03, Aula 01]]); transporte advectivo-dispersivo e retardação ([[03-contaminacao-aguas-subterraneas/03-contaminacao-aguas-subterraneas-aula-02-transporte-advectivo-dispersivo|Aulas 02]] e [[03-contaminacao-aguas-subterraneas/03-contaminacao-aguas-subterraneas-aula-03-retardacao-e-atenuacao|03]]); vulnerabilidade de aquífero pelo método GOD ([[03-contaminacao-aguas-subterraneas/03-contaminacao-aguas-subterraneas-aula-05-caracterizacao-e-protecao-de-aquiferos|Aula 05]]); condutividade hidráulica ([[06-elementos-de-geomecanica/06-elementos-de-geomecanica-aula-04-percolacao-em-meios-porosos-e-fissurados|Módulo 06, Aula 04]]).

## Antes de começar, você precisa saber

- Que a carga contaminante de uma fonte é o produto da concentração pela vazão de lixiviado, e que ela se distribui no tempo conforme o modo de disposição (Módulo 03, Aula 01).
- Que uma pluma dissolvida avança por advecção, se espalha por dispersão e é retardada por sorção, com `R = 1 + (ρ_b/n_e)·K_d` (Módulo 03, Aulas 02 e 03).
- Que o método GOD estima a vulnerabilidade do aquífero a partir do tipo de confinamento, da litologia da zona não saturada e da profundidade do nível d'água (Módulo 03, Aula 05).

## Conteúdo

### Classificação de resíduos sólidos

No Brasil, a **ABNT NBR 10004:2004** classifica os resíduos por periculosidade:

- **Classe I — perigosos:** apresentam inflamabilidade, corrosividade, reatividade, toxicidade ou patogenicidade, ou constam de listagens de resíduos perigosos. Exigem aterro de resíduos perigosos (NBR 10157) ou tratamento/coprocessamento.
- **Classe II A — não inertes:** não perigosos, mas com propriedades como biodegradabilidade, combustibilidade ou solubilidade em água. É a classe do resíduo sólido urbano (RSU). Aterro sanitário convencional (NBR 13896).
- **Classe II B — inertes:** não liberam constituintes acima dos padrões de potabilidade quando submetidos ao ensaio de solubilização. Ex.: entulho mineral, alguns rejeitos de rocha.

A classificação define o nível de barreira exigido e, portanto, o custo de disposição.

### A hierarquia da Política Nacional de Resíduos Sólidos

A **Lei 12.305/2010** (PNRS) estabelece a ordem de prioridade na gestão de resíduos: **não geração → redução → reutilização → reciclagem → tratamento → disposição final ambientalmente adequada**. Só o que não pôde ser evitado, reaproveitado ou tratado é que vai para aterro — e "rejeito", no vocabulário da lei, é justamente esse remanescente. A PNRS também instituiu a responsabilidade compartilhada pelo ciclo de vida do produto, a logística reversa para categorias específicas (agrotóxicos, pilhas, pneus, óleos lubrificantes, eletroeletrônicos) e a exigência de planos de resíduos em três níveis (nacional, estadual, municipal). A lei determinou o **fim dos lixões** — a disposição em solo sem qualquer preparo —, prazo sucessivamente prorrogado por legislação posterior.

> [!warning] Legislação de resíduos e de barragens é volátil — confirme o texto vigente
> A PNRS foi regulamentada pelo Decreto 10.936/2022 (que substituiu o Decreto 7.404/2010). Os prazos para erradicação de lixões foram alterados pelo **art. 11 da Lei 14.026/2020** (novo marco do saneamento), que deu nova redação ao **art. 54 da própria Lei 12.305/2010**, escalonando-os por porte de município — de 2 de agosto de 2021, para capitais e municípios de região metropolitana, a 2 de agosto de 2024, para municípios com menos de 50 mil habitantes. Trate as referências desta aula como o **enquadramento** do instrumento; a redação de detalhe e os prazos devem ser reconfirmados antes de fundamentar parecer técnico. O mesmo cuidado vale para a Aula 05 (barragens de rejeito).

### Seleção de áreas: critérios geológico-geotécnicos

A escolha do local de um aterro é uma decisão de triagem territorial que combina critérios de **exclusão** (eliminam a área de imediato) e critérios de **classificação** (comparam áreas remanescentes). Os principais, seguindo a NBR 13896:

- **Distâncias mínimas:** a corpos d'água superficiais, a núcleos habitacionais e a poços de abastecimento. À parte destas, e com **base legal distinta**, vem a restrição a **aeródromos**: RSU atrai aves, e a Lei 12.725/2012 (que sucedeu a Resolução CONAMA 4/1995) veda atividades de atração de fauna na Área de Segurança Aeroportuária. Não é critério da NBR 13896 nem restrição ambiental — é segurança aérea, e é de exclusão.
- **Profundidade do nível d'água:** quanto maior a espessura da zona não saturada entre a base do aterro e o lençol, maior a atenuação e o tempo de resposta. Exige-se em geral vários metros de folga.
- **Permeabilidade natural do substrato:** um substrato de baixa condutividade hidráulica (argila, siltito, rocha sã pouco fraturada) funciona como **segunda barreira geológica**, redundante ao liner construído. Substrato arenoso ou cárstico é desfavorável.
- **Estabilidade geotécnica e ausência de processos:** áreas sem risco de escorregamento, subsidência, colapso cárstico ou inundação.
- **Vida útil:** volume disponível compatível com a demanda por 15–20 anos ou mais — mudar de área é caro e politicamente custoso.
- **Vulnerabilidade do aquífero (GOD):** áreas de vulnerabilidade alta a extrema devem ser evitadas ou exigem barreira reforçada e monitoramento denso (Módulo 03, Aula 05).

A combinação desses critérios costuma ser feita por **sobreposição ponderada em SIG**, frequentemente estruturada por AHP, exatamente como as cartas de aptidão do Módulo 07 — a seleção de aterro é um caso particular de cartografia geotécnica derivada.

### A pluma de contaminação de um aterro

Mesmo um aterro bem executado gera lixiviado — o **chorume** —, a fase líquida resultante da umidade própria do resíduo, da água de chuva infiltrada e dos produtos da decomposição. Sua composição varia com a idade do aterro: na fase **acidogênica** (primeiros anos), pH baixo, alta DBO/DQO, ácidos orgânicos voláteis e metais dissolvidos; na fase **metanogênica** (madura), pH próximo do neutro, DQO menor mas com fração recalcitrante, amônia alta e persistente. A amônia é frequentemente o contaminante que define o alcance da pluma no longo prazo, porque quase não se degrada em ambiente anaeróbio.

Se o lixiviado ultrapassa o liner, forma-se uma pluma no aquífero que evolui pelos processos do Módulo 03: **advecção** ao longo do fluxo regional, **dispersão** transversal e longitudinal, **retardação** dos constituintes sorvíveis, e **atenuação** por diluição, precipitação e biodegradação da fração lábil. O monitoramento (Aula 04) é dimensionado para detectar essa pluma antes que atinge um receptor.

## Exemplo trabalhado

**Situação:** dois terrenos são candidatos a um aterro sanitário municipal (RSU, Classe II A). Avalie-os por uma matriz de decisão ponderada com cinco critérios e pesos: profundidade do nível d'água (0,30), condutividade hidráulica natural do substrato (0,25), distância a corpos d'água e núcleos habitacionais (0,20), volume/vida útil (0,15) e acesso e uso do solo do entorno (0,10). Notas de 1 (pior) a 5 (melhor).

| Critério (peso) | Sítio A | Sítio B |
|---|---|---|
| Profundidade do nível d'água (0,30) | 2 (lençol raso, ~3 m) | 4 (lençol profundo, ~18 m) |
| `K` natural do substrato (0,25) | 2 (areia, `K` alta) | 5 (argila siltosa, `K` baixa) |
| Distâncias (0,20) | 4 | 3 |
| Volume / vida útil (0,15) | 5 (25 anos) | 3 (14 anos) |
| Acesso e entorno (0,10) | 4 | 2 |

**Resolução:**

**Sítio A:**
`0,30×2 + 0,25×2 + 0,20×4 + 0,15×5 + 0,10×4`
`= 0,60 + 0,50 + 0,80 + 0,75 + 0,40 = 3,05`

**Sítio B:**
`0,30×4 + 0,25×5 + 0,20×3 + 0,15×3 + 0,10×2`
`= 1,20 + 1,25 + 0,60 + 0,45 + 0,20 = 3,70`

**Interpretação:** o Sítio B vence apesar de ter menor volume, pior acesso e estar mais perto de núcleos habitacionais. A razão está na estrutura de pesos: os dois critérios de proteção do aquífero — profundidade do lençol e `K` natural do substrato — somam 0,55 do total, e são justamente os que a engenharia **não compensa bem**. Um substrato argiloso é uma segunda barreira geológica que se ganha de graça e dura tanto quanto a geologia; um lençol raso não se rebaixa de forma permanente e barata. Já o volume menor de B resolve-se com um plano de longo prazo, e o acesso ruim, com obra viária. A matriz também deixa explícito para o gestor **por que** B foi escolhido, o que resiste melhor a questionamento do que uma escolha sem critério declarado. Por fim: a matriz é triagem — ela indica onde investigar em detalhe (sondagens, ensaios de `K` in situ, monitoramento de nível), não dispensa essa investigação.

## Erros comuns

- **Confundir "resíduo" com "rejeito" no sentido da PNRS.** Rejeito é o que sobra depois de esgotadas as alternativas de reaproveitamento e tratamento; só ele deveria ir a aterro.
- **Escolher a área pelo custo de terreno e de acesso**, deixando os critérios hidrogeológicos para "resolver com o liner". O liner tem vida útil finita; a geologia favorável, não.
- **Ignorar a restrição de distância a aeródromos** para RSU, ou procurá-la na NBR 13896 — ela está na legislação de segurança aérea (Lei 12.725/2012), não na norma técnica, e é de exclusão.
- **Tratar a pluma de lixiviado como se estabilizasse quando a fração orgânica lábil se degrada.** A amônia e alguns sais persistem e frequentemente controlam o alcance de longo prazo.
- **Aplicar a matriz de decisão como resultado final** em vez de como ferramenta de triagem que direciona a investigação de detalhe.

## O que não concluir

- **Que aterro sanitário é sinônimo de solução ambiental completa.** É o último degrau da hierarquia da PNRS; sua existência não substitui a redução na fonte, a coleta seletiva e a compostagem.
- **Que substrato de baixa `K` dispensa liner.** A barreira geológica é redundância, não substituição — a NBR e a legislação exigem o sistema de impermeabilização construído independentemente da geologia.
- **Que a seleção de área é uma decisão técnica pura.** É uma decisão de política pública informada por critérios técnicos; a aceitação social e o zoneamento urbano são condicionantes tão determinantes quanto a hidrogeologia.

## Recap relâmpago

- A NBR 10004 classifica resíduos em Classe I (perigosos), II A (não inertes — o RSU) e II B (inertes); a classe define a barreira exigida.
- A PNRS (Lei 12.305/2010) fixa a hierarquia não geração → redução → reutilização → reciclagem → tratamento → disposição final, e determinou o fim dos lixões (prazos alterados por legislação posterior — verificar o texto vigente).
- A seleção de área combina critérios de exclusão (distâncias mínimas, inundação, carste) e de classificação (profundidade do lençol, `K` natural do substrato como segunda barreira, volume, vulnerabilidade GOD), tipicamente por sobreposição ponderada em SIG.
- O lixiviado (chorume) muda de composição da fase acidogênica (pH baixo, metais, alta DQO) à metanogênica (pH neutro, amônia persistente); a amônia costuma governar o alcance de longo prazo da pluma.
- A pluma no aquífero evolui pelos processos do Módulo 03 (advecção, dispersão, retardação, atenuação) e é o alvo do monitoramento.

## Próxima aula

[[08-geotecnia-ambiental-aula-04-aterros-sanitarios-liners-e-recalques|Aula 04 — Aterros sanitários: liners, barreiras de cobertura, projeto, operação, monitoramento e recalques]]

## Anterior

[[08-geotecnia-ambiental-aula-02-erosao-e-movimentos-de-massa|Aula 02 — Condicionantes geológico-geotécnicos de processos erosivos e movimentos gravitacionais de massa]]

## Fontes

- Brasil, Lei nº 12.305, de 2 de agosto de 2010 — Política Nacional de Resíduos Sólidos; Decreto nº 10.936, de 12 de janeiro de 2022 (regulamentação, substituiu o Decreto nº 7.404/2010); Lei nº 14.026, de 15 de julho de 2020 (novo marco do saneamento), **art. 11**, que deu nova redação ao art. 54 da Lei nº 12.305/2010 (prazos escalonados de erradicação de lixões). *Consultar o texto consolidado vigente.*
- Brasil, Lei nº 12.725, de 16 de outubro de 2012 (controle da fauna nas imediações de aeródromos e Área de Segurança Aeroportuária) — base legal da restrição de distância a aeródromos.
- ABNT NBR 10004:2004, *Resíduos sólidos — Classificação*; NBR 13896:1997, *Aterros de resíduos não perigosos — Critérios para projeto, implantação e operação*; NBR 10157:1987, *Aterros de resíduos perigosos — Critérios para projeto, construção e operação*.
- Boscov, M. E. G. (2008), *Geotecnia Ambiental*, Oficina de Textos, São Paulo, cap. 2, 3 e 5.
- Qian, X., Koerner, R. M. & Gray, D. H. (2002), *Geotechnical Aspects of Landfill Design and Construction*, Prentice Hall, cap. 3 e 4.
- Christensen, T. H., Kjeldsen, P., Bjerg, P. L. et al. (2001), "Biogeochemistry of landfill leachate plumes", *Applied Geochemistry*, 16(7–8), p. 659–718.
- Kjeldsen, P., Barlaz, M. A., Rooker, A. P. et al. (2002), "Present and long-term composition of MSW landfill leachate: a review", *Critical Reviews in Environmental Science and Technology*, 32(4), p. 297–336.
- Foster, S. & Hirata, R. (1988), *Groundwater Pollution Risk Assessment: A Methodology Using Available Data*, CEPIS/PAHO, Lima (método GOD).

<!--
nivel: avancado
palavras_corpo: ~1870

mapa_objetivo_secao:
  geologia-avancado-m08-oa03: "Classificação de resíduos sólidos" + "A hierarquia da Política Nacional de Resíduos Sólidos" + "Seleção de áreas: critérios geológico-geotécnicos" + "A pluma de contaminação de um aterro" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOAMB-M08-A03-NBR10004-001
    claim: "A ABNT NBR 10004:2004 classifica os resíduos sólidos em Classe I (perigosos — inflamáveis, corrosivos, reativos, tóxicos ou patogênicos), Classe II A (não inertes) e Classe II B (inertes, que não solubilizam constituintes acima dos padrões de potabilidade no ensaio de solubilização); o resíduo sólido urbano é Classe II A."
    risk: fato
    source: "ABNT NBR 10004:2004"
  - claim_id: GEOAMB-M08-A03-PNRS-HIERARQUIA-002
    claim: "A Lei 12.305/2010 (PNRS) estabelece a ordem de prioridade: não geração, redução, reutilização, reciclagem, tratamento e disposição final ambientalmente adequada dos rejeitos; instituiu a responsabilidade compartilhada, a logística reversa para categorias específicas e planos de resíduos nos três níveis federativos, e determinou o fim dos lixões."
    risk: fato
    source: "Brasil, Lei nº 12.305/2010, arts. 9º, 33 e 54"
  - claim_id: GEOAMB-M08-A03-PNRS-VOLATIL-003
    claim: "A PNRS foi regulamentada pelo Decreto 10.936/2022, que substituiu o Decreto 7.404/2010. Os prazos para erradicação dos lixões foram alterados pelo art. 11 da Lei 14.026/2020 (marco do saneamento), que deu nova redação ao art. 54 da Lei 12.305/2010, escalonando-os por porte de município de 2 de agosto de 2021 (capitais e municípios de região metropolitana) a 2 de agosto de 2024 (municípios com menos de 50 mil habitantes) — a redação de detalhe e os prazos devem ser reconfirmados no texto vigente."
    risk: desatualizavel
    source: "Decreto nº 10.936/2022; Lei nº 14.026/2020, art. 11, que altera o art. 54 da Lei nº 12.305/2010"
  - claim_id: GEOAMB-M08-A03-SELECAO-004
    claim: "A NBR 13896 estabelece para aterros de resíduos não perigosos critérios de seleção de área incluindo distâncias mínimas a corpos d'água e a núcleos habitacionais, profundidade adequada do nível d'água, baixa permeabilidade natural do substrato como barreira geológica, estabilidade geotécnica e vida útil mínima. A restrição de distância a aeródromos NÃO decorre dessa norma: é regra de segurança aérea, hoje na Lei 12.725/2012 (Área de Segurança Aeroportuária), que sucedeu a Resolução CONAMA 4/1995."
    risk: fato
    source: "ABNT NBR 13896:1997; Qian, Koerner & Gray 2002, cap. 3; Brasil, Lei nº 12.725/2012; Resolução CONAMA nº 4/1995 (revogada)"
  - claim_id: GEOAMB-M08-A03-LIXIVIADO-005
    claim: "O lixiviado de aterro de RSU evolui de uma fase acidogênica (pH baixo, alta DBO/DQO, ácidos orgânicos voláteis, metais dissolvidos) para uma fase metanogênica madura (pH próximo do neutro, DQO menor mas recalcitrante, amônia alta e persistente); a amônia frequentemente controla o alcance de longo prazo da pluma por não se degradar em ambiente anaeróbio."
    risk: fato
    source: "Kjeldsen et al. 2002; Christensen et al. 2001"
  - claim_id: GEOAMB-M08-A03-PLUMA-006
    claim: "Uma pluma de lixiviado que ultrapassa o liner evolui no aquífero por advecção ao longo do fluxo regional, dispersão longitudinal e transversal, retardação dos constituintes sorvíveis e atenuação por diluição, precipitação e biodegradação da fração lábil."
    risk: fato
    source: "Christensen et al. 2001; Fetter, Contaminant Hydrogeology (Módulo 03)"
  - claim_id: GEOAMB-M08-A03-MATRIZ-007
    claim: "Numa matriz de decisão ponderada com pesos 0,30 (profundidade do lençol), 0,25 (K natural do substrato), 0,20 (distâncias), 0,15 (volume) e 0,10 (acesso), o sítio com lençol profundo e substrato argiloso (notas 4 e 5) obtém 3,70 contra 3,05 do sítio com lençol raso e substrato arenoso, mesmo tendo menor volume e pior acesso, porque os critérios de proteção do aquífero somam 0,55 do peso total."
    risk: calculo
    source: "Cálculo aritmético de média ponderada; método de sobreposição ponderada / AHP (Módulo 07, Aula 03)"
-->
