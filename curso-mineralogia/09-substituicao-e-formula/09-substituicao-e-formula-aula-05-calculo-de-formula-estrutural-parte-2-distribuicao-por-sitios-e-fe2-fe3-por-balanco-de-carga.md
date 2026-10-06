# Aula 05: Cálculo de fórmula estrutural — Parte 2: distribuição por sítios e Fe²⁺/Fe³⁺ por balanço de carga

**ID:** mineralogia-m09-a05
**Módulo:** [[09-substituicao-e-formula-modulo|Módulo 09 — Cristaloquímica II: substituição iônica, solução sólida e fórmula estrutural]]
**Duração estimada:** ~30 min (com a planilha)
**Nível:** ensino médio, sem geologia prévia (contrato `ensino-medio-sem-geologia-v1`)
**Objetivo:** distribuir os cátions de uma fórmula estrutural pelos sítios do mineral e estimar Fe²⁺ e Fe³⁺ a partir de uma análise com ferro total, pelo balanço de cargas (método de Droop), sabendo quando o método vale.
**Pré-requisito:** [[09-substituicao-e-formula-aula-04-calculo-de-formula-estrutural-parte-1-de-porcentagem-em-peso-de-oxidos-a-atomos-por-formula|Aula 04]] (cálculo até os apfu). Esta é a Parte 2.

## Vocabulário desta aula

| Termo | O que quer dizer |
|---|---|
| **ferro total (FeOt)** | todo o ferro da análise expresso como FeO, como se fosse todo Fe²⁺. |
| **balanço de cargas** | a exigência de que as cargas positivas somem 2 × número de O. |
| **cátions ideais (T)** | número de cátions da fórmula ideal: 3 na olivina, 4 no piroxênio, 8 na granada. |
| **S** | a soma de cátions que se obtém normalizando por oxigênios com todo o ferro como Fe²⁺. |
| **sítios X, Y, Z** | os três sítios de cátion da granada: X (8 vizinhos), Y (octaedro) e Z (tetraedro). |
| **sítios T, M1, M2** | os sítios de cátion dos piroxênios (como o diopsídio): T é o tetraedro; M1, um octaedro menor; M2, um sítio maior e mais irregular, onde cabem Ca e Na (módulo 34). |

## Antes de começar, você precisa saber

- Fazer a planilha da [[09-substituicao-e-formula-aula-04-calculo-de-formula-estrutural-parte-1-de-porcentagem-em-peso-de-oxidos-a-atomos-por-formula|aula 04]] até os apfu.
- Que a microssonda mede só o ferro total, e que separar Fe²⁺ e Fe³⁺ exige outro método (via úmida, Mössbauer, XANES) ou um cálculo de balanço de cargas ([[01-fundamentos-quimicos-aula-03-ions-e-estados-de-oxidacao-fe-mn-e-s|módulo 01, aula 03]]). Esta aula é esse cálculo.
- A magnetita, Fe³⁺[Fe²⁺Fe³⁺]O₄ ([[08-empacotamento-e-coordenacao-aula-06-estruturas-tipo-halita-fluorita-rutilo-corindo-espinelio-perovskita-e-esfalerita|módulo 08, aula 06]]).

## Ao final você vai conseguir

- `mineralogia-m09-oa04` — Calcular a fórmula estrutural de um mineral a partir de uma análise em porcentagem em peso de óxidos, normalizando por oxigênios ou por cátions, e distribuir os cátions pelos sítios. *Esta aula cobre a distribuição por sítios e a estimativa de Fe²⁺/Fe³⁺.*

## Conteúdo

### Distribuir pelos sítios: encha do menor para o maior

Os apfu dizem quantos átomos há; os sítios dizem onde. A regra prática segue a cristaloquímica do módulo 08: cada cátion vai para o sítio de tamanho compatível, começando pelo menor (o tetraedro).

| Mineral | Sítio tetraédrico | Octaédricos | Sítio grande |
|---|---|---|---|
| olivina M₂TO₄ | T: Si (completar até 1) | M: Mg, Fe²⁺, Ni, Mn | — |
| piroxênio M2 M1 T₂O₆ | T: Si, depois Al até 2 | M1: o resto do Al, Fe³⁺, Cr, Ti, depois Mg e Fe²⁺ | M2: Ca, Na, e o que sobrar de Fe²⁺, Mg, Mn |
| granada X₃Y₂Z₃O₁₂ | Z: Si, depois Al até 3 | Y: Al, Fe³⁺, Cr, Ti | X (8 vizinhos): Fe²⁺, Mg, Ca, Mn |

A soma de cada sítio tem de chegar perto do ideal (T = 1 na olivina; Z = 3, Y = 2, X = 3 na granada). Um sítio que não fecha aponta para erro de análise, elemento não analisado ou ferro no estado de oxidação errado.

### O problema do ferro

A microssonda dá **FeOt**. Se parte do ferro for Fe³⁺, ele precisaria de 1,5 O por Fe (Fe₂O₃), e a planilha só lhe deu 1 (FeO). Resultado: a soma dos O fica **pequena demais**, o fator de normalização fica **grande demais**, e a soma dos cátions **S** sai **acima do ideal T**. O excesso de cátions é a pista do Fe³⁺ escondido.

### O balanço de cargas

Agora a ideia central. Em vez dos 12 O, normalize a fórmula ao **número ideal de cátions** T (multiplique todos os apfu por T/S). Com todo o ferro como Fe²⁺, a carga total fica **abaixo** de 2 × (número de O), porque o cálculo atribuiu carga 2+ a átomos que, na verdade, são 3+. Cada Fe²⁺ que vira Fe³⁺ acrescenta exatamente +1. Logo:

**Fe³⁺ = 2 × O − (carga total com tudo Fe²⁺, normalizada a T cátions)**

Escrito em termos de S, isso é a **equação de Droop (1987)**:

**F = 2X · (1 − T/S)**

com F = Fe³⁺ por fórmula, X = número de O da fórmula, T = cátions ideais e S = soma dos cátions normalizada a X oxigênios com o ferro todo como Fe²⁺. Se S ≤ T, não há Fe³⁺ detectável.

**Conferência rápida com a magnetita.** Fe₃O₄ relatada como FeOt dá 93,09 wt% de FeO. Normalizada a 4 O, dá S = 4 Fe; T = 3. F = 2 × 4 × (1 − 3/4) = **2**. Fe total normalizado a 3 cátions = 3; logo **Fe³⁺ = 2 e Fe²⁺ = 1**: exatamente Fe²⁺Fe³⁺₂O₄.

### Quando o método vale (e quando não)

O método supõe que:

- o **ferro é o único elemento de valência variável** relevante (se houver Mn³⁺, por exemplo, ele atrapalha);
- **não há vacâncias** nos sítios de cátion (a pirrotita da aula 02, com vacâncias, quebraria a conta);
- o **O é o único ânion** (minerais com OH, F ou Cl, como micas e anfibólios, exigem cuidados adicionais);
- a **análise é boa**: S é muito sensível a erros pequenos, sobretudo no SiO₂.

Exemplo da sensibilidade: na olivina de San Carlos da aula 04, S = 3,003; a equação dá F = 2 × 4 × (1 − 3/3,003) ≈ **0,007** Fe³⁺, valor da ordem do erro da própria análise. A leitura correta é "Fe³⁺ não detectável por este método", não "0,007 Fe³⁺". Quando o Fe³⁺ importa (granadas, espinélios, piroxênios de alta pressão), o valor calculado deve ser confirmado por um método direto, como Mössbauer ou XANES.

> [!question] Pare e explique
> Por que um erro de 1% no SiO₂ de uma análise de granada pode criar ou apagar um Fe³⁺ que não existe?

## Exemplo trabalhado

**Problema.** A análise abaixo foi **construída** a partir de uma granada de fórmula conhecida (Fe²⁺₁,₈₀Mg₀,₇₅Ca₀,₄₅)(Al₁,₈₅Fe³⁺₀,₁₅)Si₃O₁₂, com o ferro todo relatado como FeO, como faria a microssonda: SiO₂ 38,24; Al₂O₃ 20,01; FeOt 29,72; MgO 6,41; CaO 5,35 (total 99,73 wt%). Usar uma análise de resposta conhecida permite conferir se o método recupera o que foi posto. (a) Normalize a 12 O com todo o Fe como Fe²⁺ e calcule S. (b) Calcule F pela equação de Droop. (c) Normalize a 8 cátions e separe Fe²⁺ e Fe³⁺. (d) Distribua pelos sítios e confira a carga. (e) Dê as frações de Fe²⁺, Mg e Ca no sítio X.

**(a)** Mols de O: SiO₂ 1,27291; Al₂O₃ 0,58875; FeO 0,41367; MgO 0,15904; CaO 0,09540; soma 2,52977. Fator = 12 ÷ 2,52977 = **4,7435**. Apfu: Si 3,019; Al 1,862; Fe 1,962; Mg 0,754; Ca 0,453. **S = 8,050**, acima de T = 8.

**(b)** F = 2 × 12 × (1 − 8/8,050) = **0,149** Fe³⁺.

**(c)** Multiplique tudo por 8/S = 0,9938: Si 3,000; Al 1,850; Fe total 1,950; Mg 0,750; Ca 0,450. Fe³⁺ = 0,149; **Fe²⁺ = 1,950 − 0,149 = 1,801**. (Pelo balanço de cargas: com tudo Fe²⁺, a carga a 8 cátions seria 23,851; faltam 24 − 23,851 = 0,149 cargas, uma por Fe³⁺. Mesma resposta.)

**(d)** Z: Si **3,000**. Y: Al 1,850 + Fe³⁺ 0,149 = **1,999**. X: Fe²⁺ 1,801 + Mg 0,750 + Ca 0,450 = **3,001**. Carga: 4 × 3,000 + 3 × (1,850 + 0,149) + 2 × (1,801 + 0,750 + 0,450) = **24,00** = 2 × 12. ✔ O método recuperou a fórmula de partida.

**(e)** Fe²⁺ 1,801/3,001 = **60%**; Mg **25%**; Ca **15%** no sítio X.

**Repare no total:** 99,73%. Com o Fe separado em FeO 27,44 e Fe₂O₃ 2,54, a mesma granada soma 100,00%: o Fe³⁺ relatado como FeO "perde" o oxigênio extra. Um total baixo pode ser sinal de Fe³⁺.

**Método geral:** (1) normalize a X oxigênios com todo o Fe como Fe²⁺ e some S; (2) se S > T, F = 2X(1 − T/S); (3) multiplique tudo por T/S e separe Fe³⁺ = F, Fe²⁺ = Fe total − F; (4) encha os sítios do menor para o maior; (5) confira as somas dos sítios e a carga; (6) desconfie de F pequeno demais (ruído) e confirme F importante por método direto.

## Erros comuns

- **Aplicar a equação a um mineral com OH, F ou vacâncias** como se fosse anidro e completo.
- **Usar a base errada:** X e T têm de ser do mesmo mineral (granada: 12 e 8; piroxênio: 6 e 4; espinélio: 4 e 3).
- **Esquecer de renormalizar** por T/S antes de separar Fe²⁺ e Fe³⁺.
- **Levar a sério um Fe³⁺ de 0,01.** Ele está dentro do erro da análise.
- **Encher os sítios fora de ordem**, pondo Al no octaedro antes de completar o tetraedro.

## O que não concluir

- Que o balanço de cargas **meça** o Fe³⁺. Ele o **estima**, supondo a estequiometria; quem mede é Mössbauer, XANES ou a via úmida.
- Que S = T prove ausência de Fe³⁺: erros da análise podem mascarar valores pequenos.
- Que a distribuição por sítios "do menor para o maior" seja sempre a verdadeira. Ela é a convenção que funciona para os minerais comuns; ordenamentos especiais (como Fe²⁺ e Mg entre M1 e M2 nos piroxênios) exigem dados estruturais.

## Recap relâmpago

- Sítios: tetraedro primeiro (Si, depois Al até completar), octaedros depois, sítio grande por último; confira a soma de cada sítio.
- Fe³⁺ escondido no FeOt faz S > T.
- Balanço de cargas a T cátions: Fe³⁺ = 2·O − carga (com tudo Fe²⁺). Droop: F = 2X(1 − T/S).
- Magnetita: S = 4, T = 3 → F = 2 → Fe²⁺Fe³⁺₂O₄. Granada construída: S = 8,050 → F = 0,149; Alm₆₀, Mg 25%, Ca 15% no sítio X.
- Vale para O como único ânion, sem vacâncias, Fe como único de valência variável e análise boa; F pequeno é ruído.

## Próxima aula

Em [[09-substituicao-e-formula-aula-06-classificacao-geoquimica-de-goldschmidt-e-elementos-traco-compativeis-e-incompativeis|Aula 06 — Classificação geoquímica de Goldschmidt e elementos-traço]], o comportamento dos elementos em escala de planeta e de magma: por que uns vão para os silicatos, outros para os sulfetos, e por que alguns ficam no líquido até o fim.

## Fontes consultadas

- Droop, G. T. R. (1987). A general equation for estimating Fe³⁺ concentrations in ferromagnesian silicates and oxides from microprobe analyses, using stoichiometric criteria. *Mineralogical Magazine* 51, 431–435. Equação F = 2X(1 − T/S) e hipóteses (ferro como único elemento de valência variável; O como único ânion) — conferido por busca em 2026-10-06.
- Métodos diretos (via úmida, Mössbauer, XANES): Forshaw & Pattison (2021), já citado no módulo 01, aula 03.
- Klein & Dutrow, *Manual of Mineral Science*, 23ª ed. (sítios X, Y, Z da granada; M1, M2 e T do piroxênio).
- Grew, E. S. et al. (2013). Nomenclature of the garnet supergroup. *American Mineralogist* 98, 785–811 (sítios X dodecaédrico, Y octaédrico, Z tetraédrico) — conferido por busca em 2026-10-06.
- A análise da granada é **construída** a partir de uma fórmula escolhida, para conferir o método; não é a análise de um espécime real. Todas as contas (análise construída, normalização, equação de Droop, magnetita, olivina de San Carlos) feitas em Python em 2026-10-06.

<!--
nivel: ensino-medio-sem-geologia-v1
palavras_corpo: 1312
cobertura:
  mineralogia-m09-oa04: [Conteúdo, Exemplo trabalhado]
alegacoes_auditaveis:
  - claim_id: CRQ-FE3-DROOP-001
    claim: "Droop (1987), Mineral. Mag. 51, 431-435: F = 2X(1 - T/S); hipoteses: Fe unico de valencia variavel, O unico anion (e sem vacancias)."
    risk: numero
    source: "busca (resumo do artigo)"
    audit: "verificado em 2026-10-06 (busca: Mineral. Mag. 51, 431-435; F = 2X(1-T/S); hipoteses)"
  - claim_id: CRQ-FE3-BALANCO-001
    claim: "Normalizando a T cations com todo Fe como Fe2+, a carga fica abaixo de 2 x O em exatamente o numero de Fe3+ (cada conversao acrescenta +1); equivalente a Droop."
    risk: conceito
    source: "calculo; Droop (1987)"
    audit: "verificado em 2026-10-06 (algebra conferida: 24 - 24x8/S = 24(1-8/S))"
  - claim_id: CRQ-FE3-MAGNET-001
    claim: "Magnetita como FeOt: 93,09 wt% FeO; S = 4 em 4 O; T = 3; F = 2 -> Fe2+ 1, Fe3+ 2."
    risk: numero
    source: "calculo"
    audit: "verificado em 2026-10-06 (calculo)"
  - claim_id: CRQ-FE3-GRANADA-001
    claim: "Granada construida (Fe2+1,80 Mg0,75 Ca0,45)(Al1,85 Fe3+0,15)Si3O12: SiO2 38,24; Al2O3 20,01; FeOt 29,72; MgO 6,41; CaO 5,35 (99,73); fator 4,7435; S = 8,050; F = 0,149; Fe2+ 1,801; carga 24,00; X: 60/25/15%; com FeO 27,44 + Fe2O3 2,54 o total e 100,00."
    risk: numero
    source: "calculo"
    audit: "verificado em 2026-10-06 (calculo: recupera a formula de partida)"
  - claim_id: CRQ-FE3-SITIOS-001
    claim: "Distribuicao: olivina T = Si, M = Mg, Fe2+, Ni, Mn; piroxenio T = Si + Al ate 2, M1 = Al restante, Fe3+, Cr, Ti, Mg, Fe2+, M2 = Ca, Na, resto; granada Z = Si + Al ate 3, Y = Al, Fe3+, Cr, Ti, X = Fe2+, Mg, Ca, Mn (8 vizinhos)."
    risk: fato
    source: "Klein & Dutrow; Morimoto (1988); Grew et al. (2013)"
    audit: "verificado em 2026-10-06 (Grew et al. 2013 por busca: X dodecaedrico, Y octaedrico, Z tetraedrico)"
  - claim_id: CRQ-FE3-SC-001
    claim: "Olivina de San Carlos: S = 3,003 na base de 4 O; F = 0,007, da ordem do erro: Fe3+ nao detectavel pelo metodo."
    risk: numero
    source: "calculo"
    audit: "verificado em 2026-10-06 (calculo)"
  - claim_id: CRQ-FE3-LIMITES-001
    claim: "O metodo exige O como unico anion (micas e anfibolios exigem cuidados), sem vacancias, Fe como unico de valencia variavel (Mn3+ atrapalha); S e muito sensivel a erros, sobretudo no SiO2; Fe3+ importante deve ser confirmado por Mossbauer ou XANES."
    risk: conceito
    source: "Droop (1987); Forshaw & Pattison (2021)"
    audit: "verificado em 2026-10-06"
  - claim_id: CRQ-FE3-PXSITIOS-001
    claim: "Piroxenios: T tetraedro; M1 octaedro menor; M2 sitio maior e mais irregular, onde cabem Ca e Na."
    risk: conceito
    source: "Morimoto (1988); Klein & Dutrow"
    audit: "verificado em 2026-10-06 (segunda passagem; acrescentado pela revisao didatica)"
-->
