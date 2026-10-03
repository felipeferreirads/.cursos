# Aula 04: Processos de evolução dos magmas alcalinos — Parte 2: geoquímica elemental e isotópica e modelagem petrogenética

**Módulo:** [[31-rochas-igneas-alcalinas-modulo|Módulo 31 — Rochas ígneas alcalinas: petrologia e mineralizações]]
**Duração estimada:** ~20 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** interpretar dados geoquímicos elementais e isotópicos e de química mineral em modelagens petrogenéticas de suítes alcalinas.
**Ao final você vai conseguir:** ler um padrão de elementos incompatíveis normalizado ao manto primitivo e um padrão de ETR; situar uma amostra alcalina nos componentes mantélicos HIMU, EM1, EM2 e DMM a partir de razões isotópicas de Sr e Nd; e aplicar as equações de fusão em lote e de cristalização fracionada de Rayleigh a um problema simples.
**Pré-requisito:** Aula 03, Parte 1 (processos de evolução). Módulo 26 (geologia isotópica aplicada — sistemas Sr-Nd, notação épsilon). Módulo 30, Aula 05 (primeiro uso da equação de Rayleigh).

## Conteúdo

### Padrões de elementos incompatíveis: a "impressão digital" da fonte

Rochas alcalinas são tipicamente enriquecidas em **elementos incompatíveis** (é uma característica, não o critério de definição, que é mineralógico e normativo, Aula 01) — aqueles que preferem a fase líquida à sólida durante a fusão parcial (K, Rb, Ba, Th, U, Nb, Ta, La, Ce, Sr, entre outros). A ferramenta padrão para visualizar esse enriquecimento é o **diagrama multielementar normalizado ao manto primitivo** (*spidergram*), no qual a concentração de cada elemento na amostra é dividida pela concentração estimada no manto primitivo (não fracionado) e os elementos são ordenados por incompatibilidade decrescente. Um magma alcalino típico mostra um padrão fortemente inclinado, com os elementos mais incompatíveis (Rb, Ba, Th) elevados a dezenas ou centenas de vezes o manto primitivo, decrescendo suavemente até os elementos menos incompatíveis (Yb, Lu).

Duas feições nesse padrão merecem atenção especial:

- **Anomalias de Nb-Ta**: magmas de subducção (calcialcalinos) mostram tipicamente uma anomalia negativa de Nb-Ta (um "vale" no padrão, porque esses elementos ficam retidos em fases residuais na placa subductada e no manto de cunha). Magmas alcalinos intraplaca, ao contrário, costumam **não** ter essa anomalia negativa — muitas vezes mostram Nb e Ta relativamente elevados em relação aos elementos vizinhos —, e essa ausência de anomalia negativa de Nb-Ta é um dos critérios geoquímicos usados para distinguir magmatismo intraplaca de magmatismo relacionado à subducção, mesmo em terrenos antigos onde o contexto tectônico original não é óbvio em campo.
- **Padrão de ETR fracionado**: o diagrama de elementos terras raras normalizado a condrito mostra, em magmas alcalinos gerados por baixo grau de fusão em fácies de granada (Aula 02), uma razão La/Yb alta — ETR leves muito enriquecidas, ETR pesadas relativamente baixas, porque a granada retém fortemente as ETR pesadas no resíduo mantélico. Esse padrão contrasta com o padrão mais plano de basaltos toleíticos de crista meso-oceânica, gerados em maior grau de fusão e majoritariamente em fácies de espinélio.

### Isótopos radiogênicos: Sr, Nd, Pb e os componentes mantélicos

Enquanto os elementos-traço informam sobre grau de fusão e mineralogia residual, os **isótopos radiogênicos** (que não fracionam por processos magmáticos, apenas registram a história de longo prazo da razão pai/filho na fonte) informam sobre a **natureza da fonte mantélica** em si — se ela é um manto depletado "comum" ou um reservatório com história geoquímica distinta. Os sistemas mais usados são ⁸⁷Sr/⁸⁶Sr, ¹⁴³Nd/¹⁴⁴Nd (expresso como εNd, já trabalhado no módulo 26) e as razões de Pb (²⁰⁶Pb/²⁰⁴Pb etc.).

Zindler & Hart (1986), num trabalho de síntese que se tornou referência-padrão (conhecido informalmente como o "zoológico do manto", *mantle zoo*), organizaram a diversidade isotópica de basaltos de ilha oceânica (OIB) — a categoria de magma mais próxima aos alcalinos deste módulo, em termos de fonte — em componentes-extremo (*end-members*):

- **DMM** (*depleted MORB mantle*): manto depletado em elementos incompatíveis por extração passada de fundidos, baixo ⁸⁷Sr/⁸⁶Sr, εNd alto (positivo). Fonte típica de basaltos de crista meso-oceânica.
- **HIMU** (alta razão μ = ²³⁸U/²⁰⁴Pb): razões de Pb radiogênico muito elevadas, interpretado em geral como crosta oceânica antiga reciclada, que perdeu Pb (ficando com U relativamente alto) durante a alteração hidrotermal e a desidratação na subducção; exemplo clássico é a ilha de Santa Helena.
- **EM1** (*enriched mantle 1*): ⁸⁷Sr/⁸⁶Sr moderadamente elevado, εNd baixo, razões de Pb relativamente baixas; interpretado por alguns autores como envolvendo sedimento pelágico antigo ou litosfera subcontinental reciclada.
- **EM2** (*enriched mantle 2*): ⁸⁷Sr/⁸⁶Sr elevado, εNd baixo, mas com razões de Pb mais radiogênicas que EM1; frequentemente associado a sedimento terrígeno reciclado; exemplo clássico nas ilhas da Sociedade, na Polinésia Francesa.

Não há regra simples do tipo "continental = EM1, oceânico = HIMU". Províncias alcalinas continentais sobre litosfera antiga e metassomatizada, como as cretáceas brasileiras (Gibson et al., 1995), mostram com frequência assinaturas próximas de EM1 ou de mistura de componentes, refletindo a contribuição de **litosfera subcontinental antiga** (Aula 02) como fonte ou contaminante. Mas outras províncias continentais, como o magmatismo alcalino cenozoico da Europa e parte do Leste Africano, têm assinatura tipo HIMU, atribuída a manto astenosférico; e há ilhas oceânicas EM1 (Pitcairn, Tristão da Cunha) ao lado das HIMU e EM2. Interpretar a posição de uma amostra nesses diagramas (⁸⁷Sr/⁸⁶Sr vs. εNd, ou diagramas de Pb-Pb) é, portanto, uma ferramenta direta para discutir se a fonte de um magma alcalino é manto litosférico antigo, manto astenosférico profundo (pluma), ou uma mistura dos dois — questão central quando se tenta reconstruir a petrogênese de uma província alcalina continental.

### Modelagem quantitativa: fusão em lote e cristalização de Rayleigh

Duas equações fazem a ponte entre a observação geoquímica e a interpretação de processo: a de fusão em lote, nova neste curso, e a de cristalização de Rayleigh, já usada no Módulo 30 para carbonatitos e agora aplicada à evolução de magmas alcalinos silicáticos:

**Fusão parcial em lote (batch melting)**, de Shaw (1970):

C_L / C₀ = 1 / [D + F(1 − D)]

onde C_L é a concentração do elemento no líquido, C₀ a concentração na fonte antes da fusão, F a fração de fusão (0 a 1) e D o coeficiente de partição global sólido/líquido. Para um elemento fortemente incompatível (D próximo de zero), essa equação se aproxima de C_L/C₀ ≈ 1/F — ou seja, o enriquecimento no líquido é aproximadamente o inverso do grau de fusão: um grau de fusão de 1% pode enriquecer um elemento altamente incompatível em até ~100 vezes em relação à fonte, o que ajuda a explicar por que magmas de baixíssimo grau de fusão (Aula 02) são tão ricos nesses elementos.

**Cristalização fracionada de Rayleigh**, já usada no módulo 30 para carbonatitos e retomada aqui para a série silicática:

C_L / C₀ = F^(D−1)

onde agora F é a fração de líquido remanescente (não de fusão) e D o coeficiente de partição do mineral (ou conjunto de minerais) que está cristalizando e sendo removido do sistema. Para um elemento incompatível (D<1), a concentração no líquido residual **aumenta** à medida que F diminui (mais cristalização, menos líquido remanescente); para um elemento compatível (D>1), a concentração no líquido **diminui**. É essa equação que formaliza, matematicamente, a observação da Parte 1 desta aula: por que o líquido residual de um magma alcalino em cristalização fracionada fica progressivamente mais enriquecido em álcalis e em elementos incompatíveis, empurrando a composição para o campo fonolítico.

Um modelo petrogenético completo, na prática, combina essas equações com os dados isotópicos (que não mudam por cristalização fracionada, só por mistura ou assimilação) para testar hipóteses: um trend de elementos-traço compatível com cristalização fracionada, mas com isótopos que variam sistematicamente ao longo da série, aponta para **assimilação concomitante à cristalização fracionada (AFC)**, um processo em que o magma incorpora rocha encaixante (crustal, tipicamente) enquanto cristaliza — modelado pela formulação de DePaolo (1981), que estende a equação de Rayleigh simples para incluir um termo de assimilação proporcional à taxa de cristalização.

## Exemplo trabalhado

**Situação.** Uma fonte mantélica (manto metassomatizado, Aula 02) funde em lote com F = 0,02 (2%) e gera um líquido alcalino primário. Considere o elemento Nb, fortemente incompatível, com D ≈ 0,01 no resíduo peridotítico.

**1. Enriquecimento por fusão.**

C_L/C₀ = 1/[D + F(1−D)] = 1/[0,01 + 0,02 × 0,99] ≈ 1/[0,01 + 0,0198] = 1/0,0298 ≈ **33,6**

O líquido primário sai cerca de 34 vezes mais rico em Nb do que a fonte mantélica — consistente com o forte enriquecimento em elementos de alto campo de força (HFSE, cátions pequenos e de carga alta, como Nb, Ta, Zr, Hf e Ti) observado em magmas alcalinos de baixo grau de fusão.

**2. Enriquecimento adicional por cristalização fracionada de Rayleigh.** Suponha que esse líquido primário cristalize fracionadamente até restar F = 0,3 (30% de líquido remanescente), removendo um conjunto de minerais (olivina, clinopiroxênio, plagioclásio) para os quais o Nb tem D efetivo ≈ 0,05 (incompatível nesses minerais).

C_L/C₀(cristalização) = F^(D−1) = 0,3^(0,05−1) = 0,3^(−0,95)

0,3^(−0,95) = 10^(−0,95 × log₁₀0,3) = 10^(−0,95 × (−0,523)) = 10^(0,497) ≈ **3,14**

O líquido residual, depois da cristalização fracionada, fica ainda cerca de 3,1 vezes mais rico em Nb do que estava no início da cristalização.

**3. Enriquecimento total.** Combinando os dois processos (fusão seguida de cristalização): 33,6 × 3,14 ≈ **105 vezes** o teor de Nb da fonte mantélica original — uma ordem de grandeza que ilustra por que rochas alcalinas evoluídas (fonolitos, sienitos agpaíticos da Aula 05) podem concentrar elementos de alto campo de força o suficiente para se tornarem minério.

**O que fixar.** Baixo grau de fusão e cristalização fracionada subsequente atuam na mesma direção — ambos enriquecem elementos incompatíveis no líquido residual —, e é essa combinação, não um processo isolado, que explica concentrações econômicas de Nb, ETR e outros elementos de alto campo de força em rochas alcalinas evoluídas.

## Recap relâmpago

- O diagrama multielementar normalizado ao manto primitivo mostra, em magmas alcalinos, forte enriquecimento em elementos incompatíveis e tipicamente ausência de anomalia negativa de Nb-Ta (ao contrário de magmas de subducção).
- O padrão de ETR fracionado (La/Yb alto) reflete fusão em baixo grau na fácies de granada, que retém ETR pesadas no resíduo.
- Os componentes mantélicos de Zindler & Hart (1986) — DMM, HIMU, EM1, EM2 — organizam a diversidade isotópica de Sr-Nd-Pb; províncias alcalinas sobre litosfera antiga metassomatizada (como as cretáceas brasileiras) tendem a EM1 ou misturas, mas não há regra geral continental × oceânico.
- A equação de fusão em lote (Shaw, 1970) e a de cristalização de Rayleigh (esta já usada no Módulo 30 para carbonatitos) se aplicam à série silicática alcalina; para elementos incompatíveis, ambos os processos enriquecem o líquido residual na mesma direção.
- Isótopos não mudam por cristalização fracionada simples, apenas por mistura ou assimilação (AFC, DePaolo 1981) — por isso a combinação de dados isotópicos e elementares é o que permite distinguir fracionamento puro de contaminação crustal.

## Próxima aula

A Aula 05 aplica esses fundamentos petrogenéticos às rochas sieníticas: como a série miaskítica evolui para a série agpaítica, e o que essa transição — registrada na mineralogia, não só na geoquímica — significa para o potencial econômico em elementos de terras raras e de alto campo de força.

## Fontes

- Zindler, A. & Hart, S. (1986), "Chemical Geodynamics", *Annual Review of Earth and Planetary Sciences*, 14, 493-571 — componentes mantélicos DMM, HIMU, EM1, EM2. Referência clássica consolidada, uso corrente na literatura de geoquímica isotópica.
- Shaw, D. M. (1970), "Trace element fractionation during anatexis", *Geochimica et Cosmochimica Acta*, 34, 237-243 — equação de fusão em lote. Referência consolidada, CONFERIDA na auditoria (2026-09-24); a equação é nova neste módulo (o Módulo 30 usa só a de Rayleigh).
- Hoernle, K., Zhang, Y.-S. & Graham, D. (1995), "Seismic and geochemical evidence for large-scale mantle upwelling beneath the eastern Atlantic and western and central Europe", *Nature*, 374, 34-39 — assinatura tipo HIMU do magmatismo alcalino cenozoico europeu. CONFERIDO na auditoria (2026-09-24).
- DePaolo, D. J. (1981), "Trace element and isotopic effects of combined wallrock assimilation and fractional crystallization", *Earth and Planetary Science Letters*, 53, 189-202 — formulação de AFC. Referência consolidada da literatura de petrogênese ígnea.

<!--
nivel: avancado
palavras_corpo: 1682
duracao_estimada_min: 20
palavras_corpo_metodo: "tokens separados por espaco entre '## Conteudo' e '## Fontes', incluindo tabelas, contados por script a ~84 palavras/min."

mapa_objetivo_secao:
  geologia-avancado-m31-oa03: "Toda a aula: padroes multielementares e de ETR, componentes mantelicos (Zindler & Hart), equacoes de fusao em lote e cristalizacao de Rayleigh, AFC, exemplo trabalhado com calculo numerico"

divisao_de_aula: "Parte 2 da antiga Aula 03 unica (geoquimica elemental e isotopica e modelagem petrogenetica), dividida da Parte 1 (Aula 03, cristalizacao fracionada e imiscibilidade) por serem blocos conceituais independentes. ID m31-a04 (aula nova na sequencia renumerada); antigas a04, a05, a06 tornam-se a05, a06, a07 (mapeamento CORRIGIDO na auditoria 2026-09-24; o texto anterior dava 'a05/a06, a07/a08, a09')."

alegacoes_auditaveis:
  - claim_id: ALK-M31-A04-NB-TA-001
    claim: "Magmas de subduccao mostram anomalia negativa de Nb-Ta no diagrama multielementar; magmas alcalinos intraplaca tipicamente nao mostram essa anomalia negativa - criterio geoquimico para distinguir os dois ambientes."
    risk: fato
    source: "Consolidado na literatura de geoquimica de magmas (padrao amplamente documentado em manuais de petrologia igneas, ex. Winter, Rollinson)."
  - claim_id: ALK-M31-A04-ETR-GRANADA-002
    claim: "Razao La/Yb alta em magmas alcalinos reflete fusao em baixo grau na facies de granada, que retem ETR pesadas no residuo."
    risk: fato
    source: "Consolidado na literatura de petrologia experimental e geoquimica de elementos-traco; conectado ao conteudo ja apresentado na Aula 02 deste modulo."
  - claim_id: ALK-M31-A04-ZINDLER-HART-003
    claim: "Zindler & Hart (1986) definem os componentes mantelicos DMM, HIMU, EM1 e EM2 a partir de sistematica isotopica Sr-Nd-Pb de OIB; provincias alcalinas sobre litosfera antiga metassomatizada (ex.: cretaceas brasileiras) tendem a EM1 ou misturas, mas ha provincias continentais tipo HIMU (Europa cenozoica) e ilhas EM1 (Pitcairn, Tristao); HIMU = crosta oceanica reciclada com perda de Pb."
    risk: interpretacao
    source: "Zindler & Hart 1986, Annu Rev Earth Planet Sci 14:493-571; Hoernle et al. 1995, Nature 374:34-39; Stracke 2012, Chem Geol 330-331:274-299. CORRIGIDO na auditoria 2026-09-24 (laranja 15): antes 'continental = EM1, oceanico = HIMU/EM2' como regra e HIMU por 'desgaseificacao'."
  - claim_id: ALK-M31-A04-EQUACOES-004
    claim: "Equacao de fusao em lote (Shaw 1970): CL/C0 = 1/[D+F(1-D)] (nova neste modulo). Equacao de cristalizacao de Rayleigh: CL/C0 = F^(D-1) (ja usada no M30, Aula 05). AFC formalizado por DePaolo (1981)."
    risk: fato
    source: "Shaw 1970, GCA 34:237-243; DePaolo 1981, EPSL 53:189-202. CORRIGIDO na auditoria 2026-09-24 (laranja 8): o texto dizia que as duas equacoes ja tinham sido usadas no modulo 30; o M30 usa so a de Rayleigh."
  - claim_id: ALK-M31-A04-EXEMPLO-CALCULO-005
    claim: "Exemplo hipotetico: fusao em lote F=0,02, D=0,01 -> CL/C0 ~33,6; cristalizacao de Rayleigh F=0,3, D=0,05 -> fator adicional ~3,14; enriquecimento total ~105x."
    risk: hipotetico
    source: "Aritmetica sobre valores inventados para fins didaticos; calculos conferidos internamente (log e potenciacao)."
  - claim_id: ALK-M31-A04-DEFINICAO-OPERACIONAL-006
    claim: "Rochas alcalinas sao tipicamente enriquecidas em elementos incompativeis; o enriquecimento e caracteristica, nao criterio de definicao (a definicao e mineralogica e normativa, Aula 01)."
    risk: fato
    source: "Le Maitre 2002. Criado pela auditoria 2026-09-24 (laranja 16): o texto dizia 'por definicao operacional'."

auditoria:
  data: 2026-09-24
  modo: audit-and-fix
  relatorio: 31-rochas-igneas-alcalinas-auditoria.md
  achados_nesta_aula: "laranja 15 (ZINDLER-HART-003), laranja 16 (DEFINICAO-OPERACIONAL-006), laranja 8 (MOD-REMISSOES-001: fusao em lote nao usada no M30; Aula 06 -> 05; 'Aula 05 (em duas partes)'; metadado divisao_de_aula)"
  verificados_sem_achado: "001 (anomalia negativa de Nb-Ta em magmas de subduccao), 002 (La/Yb alto por granada residual), 004 (equacoes e referencias Shaw 1970, DePaolo 1981), 005 (aritmetica refeita: 33,6; 3,14, o mesmo fator do M30 a05; ~105)"
-->
