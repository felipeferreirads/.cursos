# Aula 04: Cálculo de fórmula estrutural — Parte 1: de % em peso de óxidos a átomos por fórmula

**ID:** mineralogia-m09-a04
**Módulo:** [[09-substituicao-e-formula-modulo|Módulo 09 — Cristaloquímica II: substituição iônica, solução sólida e fórmula estrutural]]
**Duração estimada:** ~30 min (com a planilha)
**Nível:** ensino médio, sem geologia prévia (contrato `ensino-medio-sem-geologia-v1`)
**Objetivo:** transformar uma análise química em porcentagem em peso de óxidos no número de átomos de cada elemento por fórmula, normalizando por oxigênios ou por cátions, e conferir o resultado pela soma de cátions e pela neutralidade.
**Pré-requisito:** [[01-fundamentos-quimicos-aula-06-mol-massa-molar-composicao-em-oxidos-e-unidades|módulo 01, aula 06]] (mol, massa molar, % de óxidos) e [[09-substituicao-e-formula-aula-03-solucao-solida-miscibilidade-e-isomorfismo|aula 03]] (membros finais, Fo). Esta é a Parte 1; a Parte 2 (sítios e Fe³⁺) vem na aula 05.

## Vocabulário desta aula

| Termo | O que quer dizer |
|---|---|
| **análise química (wt%)** | a composição de um mineral em porcentagem em peso de óxidos, como sai de uma microssonda eletrônica (módulo 19). |
| **fórmula estrutural** | a fórmula com o número de átomos de cada elemento por unidade de fórmula, como (Mg₁,₈₀Fe₀,₂₀)SiO₄. |
| **apfu** | átomos por unidade de fórmula (do inglês *atoms per formula unit*). |
| **base de normalização** | o número fixo de oxigênios (ou de cátions) da fórmula ideal, ao qual se ajustam os números: 4 O na olivina, 6 no piroxênio. |
| **proporção atômica** | número de mols de átomos de cada elemento, antes da normalização. |

## Antes de começar, você precisa saber

- Massas molares de óxidos e a conversão de % em massa em mols: dividir pela massa molar ([[01-fundamentos-quimicos-aula-06-mol-massa-molar-composicao-em-oxidos-e-unidades|módulo 01, aula 06]]). Lá você fez o caminho de Mg₂SiO₄ para 57,29% MgO + 42,71% SiO₂; aqui você faz o caminho de volta, com uma análise real.
- O óxido relatado é uma convenção, e o ferro sai como FeO total quando a análise não distingue Fe²⁺ e Fe³⁺ (módulo 01, aulas 03 e 06).
- Neutralidade: a soma das cargas positivas é igual a 2 × número de O ([[01-fundamentos-quimicos-aula-03-ions-e-estados-de-oxidacao-fe-mn-e-s|módulo 01, aula 03]]).

## Ao final você vai conseguir

- `mineralogia-m09-oa04` — Calcular a fórmula estrutural de um mineral a partir de uma análise em porcentagem em peso de óxidos, normalizando por oxigênios ou por cátions, e distribuir os cátions pelos sítios. *Esta aula cobre o cálculo até os apfu; a distribuição por sítios e o Fe³⁺ ficam para a aula 05.*

## Conteúdo

### O problema

A microssonda (módulo 19) devolve algo assim: "SiO₂ 40,81; FeO 9,55; MnO 0,14; MgO 49,42; NiO 0,37 (% em peso)". Isso não diz diretamente quantos Mg há por fórmula. Para chegar lá, é preciso passar de **massa** para **mols** e, depois, escalar tudo para a fórmula ideal do mineral.

### A receita em cinco colunas

Monte uma tabela, uma linha por óxido:

1. **wt%** do óxido, como veio da análise.
2. **Massa molar** do óxido (módulo 01, aula 06): SiO₂ 60,083; FeO 71,844; MnO 70,937; MgO 40,304; NiO 74,692.
3. **Mols de óxido** = wt% ÷ massa molar.
4. **Mols de cátion** = mols de óxido × número de cátions no óxido (1 em SiO₂ e MgO; **2** em Al₂O₃, Fe₂O₃, Na₂O, K₂O).
5. **Mols de O** = mols de óxido × número de O no óxido (2 em SiO₂; 1 em MgO; **3** em Al₂O₃).

Depois:

6. **Soma** a coluna de O.
7. **Fator de normalização** = (O da fórmula ideal) ÷ (soma dos O).
8. **apfu** de cada cátion = mols de cátion × fator.

### A base: quantos O tem a fórmula ideal

| Mineral | Fórmula ideal | Base em O | Cátions ideais |
|---|---|---|---|
| olivina | M₂SiO₄ | 4 | 3 |
| espinélio | AB₂O₄ | 4 | 3 |
| piroxênio | M2 M1 T₂O₆ | 6 | 4 |
| feldspato | (Na,K,Ca)(Al,Si)₄O₈ | 8 | 5 |
| granada | X₃Y₂Z₃O₁₂ | 12 | 8 |

**Por que normalizar por oxigênios?** Porque, em minerais sem vacâncias de oxigênio, o número de O por fórmula é fixo pela estrutura, enquanto os cátions podem variar (substituições, vacâncias). E há uma vantagem escondida: como cada mol de O foi calculado a partir dos cátions com as cargas assumidas, a soma das cargas dos cátions normalizados sai **exatamente** 2 × base. A neutralidade fica garantida pela construção; o teste de qualidade passa a ser a **soma dos cátions**, que tem de se aproximar do valor ideal.

**Normalizar por cátions** (por exemplo, 3 cátions na olivina) é a alternativa quando o oxigênio da fórmula é incerto, ou quando se quer comparar com a base de O: em vez do passo 7, use (cátions ideais) ÷ (soma dos mols de cátion). As duas bases dão quase o mesmo resultado numa análise boa; quando divergem, algo está errado (aula 05).

> [!question] Pare e explique
> Por que a soma das cargas sai sempre igual a 2 × base quando se normaliza por oxigênios? O que, então, sobra para conferir a análise?

## Exemplo trabalhado

**Problema.** A olivina de San Carlos (Arizona) é um padrão de laboratório muito usado; uma análise de referência dela é: SiO₂ 40,81; FeO 9,55; MnO 0,14; MgO 49,42; NiO 0,37 (total 100,29 wt%). Calcule (a) a fórmula estrutural na base de 4 O; (b) a soma dos cátions; (c) a neutralidade; (d) o Fo; (e) a fórmula na base de 3 cátions.

**(a)** As colunas (valores arredondados; contas com todos os dígitos):

| Óxido | wt% | M (g/mol) | mol óxido | mol cátion | mol O |
|---|---|---|---|---|---|
| SiO₂ | 40,81 | 60,083 | 0,67923 | 0,67923 | 1,35845 |
| FeO | 9,55 | 71,844 | 0,13293 | 0,13293 | 0,13293 |
| MnO | 0,14 | 70,937 | 0,00197 | 0,00197 | 0,00197 |
| MgO | 49,42 | 40,304 | 1,22618 | 1,22618 | 1,22618 |
| NiO | 0,37 | 74,692 | 0,00495 | 0,00495 | 0,00495 |
| **Soma** | | | | | **2,72449** |

Fator = 4 ÷ 2,72449 = **1,4682**. Multiplicando a coluna de cátions:

**Si 0,997 · Fe 0,195 · Mn 0,003 · Mg 1,800 · Ni 0,007**

Fórmula: **(Mg₁,₈₀₀Fe₀,₁₉₅Ni₀,₀₀₇Mn₀,₀₀₃)Si₀,₉₉₇O₄**.

**(b)** Soma dos cátions: **3,003** (ideal: 3). Sítio octaédrico (Mg + Fe + Ni + Mn) = 2,006; tetraédrico (Si) = 0,997. Uma análise excelente.

**(c)** Cargas: 4 × 0,997 + 2 × (1,800 + 0,195 + 0,007 + 0,003) = **8,00** = 2 × 4 O. ✔ (Como previsto, a neutralidade fecha por construção.)

**(d)** Fo = Mg / (Mg + Fe) = 1,800 / (1,800 + 0,195) = **90,2%** → **Fo₉₀**, o valor tabelado para esse padrão (Fo₉₀,₁).

**(e)** Na base de 3 cátions, o fator é 3 ÷ 2,04526 (soma dos mols de cátion); resultam Si 0,996, Mg 1,799, Fe 0,195, e O = **3,996**, praticamente 4. As duas bases concordam, como deve ser numa análise boa.

**Método geral:** wt% → ÷ M → mols de óxido → × cátions e × O → soma de O → fator = base/soma → apfu → confira a soma dos cátions (e, se quiser, a outra base).

## Erros comuns

- **Esquecer o 2 de Al₂O₃, Na₂O, K₂O, Fe₂O₃** na coluna de cátions (e o 3 de Al₂O₃ na de O). É o erro mais frequente da planilha.
- **Normalizar pela soma das porcentagens** em vez da soma dos O. A porcentagem é massa; a fórmula é contagem de átomos.
- **Usar a base errada:** 4 O para um piroxênio dá metade da fórmula.
- **Ler a neutralidade como teste de qualidade** numa normalização por O: ela fecha sempre; o teste é a soma dos cátions.
- **Arredondar no meio da conta.** Arredonde só no fim.

## O que não concluir

- Que um total de 100,29% (ou de 99,5%) signifique erro. Toda análise tem incerteza, e um total um pouco acima ou abaixo de 100 é normal; elementos não analisados (H₂O, F) e o Fe³⁺ relatado como FeO (aula 05) também afastam o total de 100.
- Que a fórmula diga onde cada cátion está. Ela diz quantos há; a distribuição pelos sítios é a aula 05.
- Que o terceiro algarismo decimal seja exato. Ele reflete a precisão da análise, não a do cristal.

## Recap relâmpago

- wt% ÷ massa molar = mols de óxido; × cátions do óxido; × O do óxido.
- Fator = O da fórmula ideal ÷ soma dos O; apfu = mols de cátion × fator.
- Bases: olivina e espinélio 4 O; piroxênio 6; feldspato 8; granada 12.
- Normalizar por O garante a neutralidade; o teste é a soma dos cátions (olivina: 3).
- San Carlos: (Mg₁,₈₀Fe₀,₁₉₅Ni₀,₀₀₇Mn₀,₀₀₃)Si₀,₉₉₇O₄; cátions 3,003; Fo₉₀.

## Próxima aula

Em [[09-substituicao-e-formula-aula-05-calculo-de-formula-estrutural-parte-2-distribuicao-por-sitios-e-fe2-fe3-por-balanco-de-carga|Aula 05 — Cálculo de fórmula estrutural, Parte 2]], os cátions são distribuídos pelos sítios e o "excesso de cátions" que aparece quando há Fe³⁺ escondido no FeO total vira uma estimativa de Fe²⁺ e Fe³⁺ por balanço de carga.

## Fontes consultadas

- Jarosewich, E., Nelen, J. A. & Norberg, J. A. (1980). Reference samples for electron microprobe analysis. *Geostandards Newsletter* 4, 43 (olivina de San Carlos, USNM 111312/444). Conferidos por busca em 2026-10-06: SiO₂ = 40,81 wt% e Fo₉₀,₁. Os demais óxidos (FeO 9,55; MnO 0,14; MgO 49,42; NiO 0,37) são os valores usualmente citados para esse padrão; não foi possível abrir a tabela original nesta sessão (ver auditoria). A coerência interna foi conferida: Fo calculado 90,2 e soma de cátions 3,003.
- IUPAC/CIAAW, massas atômicas abreviadas (as mesmas do módulo 01, aula 06).
- Klein & Dutrow, *Manual of Mineral Science*, 23ª ed. (recálculo de análises; bases de normalização).
- Todas as contas feitas em Python em 2026-10-06.

<!--
nivel: ensino-medio-sem-geologia-v1
palavras_corpo: 1047
cobertura:
  mineralogia-m09-oa04: [Conteúdo, Exemplo trabalhado]
alegacoes_auditaveis:
  - claim_id: CRQ-FORM-RECEITA-001
    claim: "Receita: wt% / M = mol oxido; x cations e x O do oxido; fator = O ideal / soma O; apfu = mol cation x fator; normalizar por cations: fator = cations ideais / soma mol cations."
    risk: conceito
    source: "Klein & Dutrow"
    audit: "verificado em 2026-10-06"
  - claim_id: CRQ-FORM-BASES-001
    claim: "Bases: olivina e espinelio 4 O (3 cations); piroxenio 6 O (4); feldspato 8 O (5); granada 12 O (8)."
    risk: numero
    source: "Klein & Dutrow; Droop (1987)"
    audit: "verificado em 2026-10-06"
  - claim_id: CRQ-FORM-NEUTRO-001
    claim: "Normalizando por O, a soma das cargas dos cations sai exatamente 2 x base (por construcao); o teste de qualidade e a soma dos cations."
    risk: conceito
    source: "calculo; Droop (1987)"
    audit: "verificado em 2026-10-06 (demonstrado no calculo: carga 8,00 e 24,00)"
  - claim_id: CRQ-FORM-SANCARLOS-001
    claim: "Olivina de San Carlos (Jarosewich et al., 1980): SiO2 40,81; FeO 9,55; MnO 0,14; MgO 49,42; NiO 0,37; total 100,29; Fo 90,1."
    risk: numero
    source: "busca (SiO2 40,81 e Fo 90,1 confirmados); demais oxidos: valores usualmente citados"
    audit: "🔵 parcialmente verificado em 2026-10-06: SiO2 40,81 e Fo 90,1 confirmados por busca (Jarosewich et al. 1980; Lambart et al. 2022); FeO, MnO, MgO e NiO nao conferidos na tabela original (acesso bloqueado); coerencia interna confere (Fo 90,2; soma 3,003). Texto ja traz a ressalva. Adiado, nao bloqueante"
  - claim_id: CRQ-FORM-SCCALC-001
    claim: "San Carlos na base de 4 O: fator 1,4682; Si 0,997; Fe 0,195; Mn 0,003; Mg 1,800; Ni 0,007; soma 3,003; carga 8,00; Fo 90,2; base 3 cations: O = 3,996."
    risk: numero
    source: "calculo"
    audit: "verificado em 2026-10-06 (calculo)"
  - claim_id: CRQ-FORM-TOTAL-001
    claim: "Totais um pouco acima ou abaixo de 100% sao normais; H2O, F e Fe3+ relatado como FeO afastam o total de 100."
    risk: numero
    source: "pratica de microssonda (Klein & Dutrow; Reed, Electron Microprobe Analysis)"
    audit: "verificado em 2026-10-06 (formulacao qualitativa, sem faixa numerica)"
-->
