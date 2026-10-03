# Aula 01: A água e seus constituintes químicos: unidades de concentração e balanço iônico

**ID:** geologia-avancado-m02-a01
**Módulo:** [[02-hidrogeoquimica-modulo|Módulo 02 — Hidrogeoquímica]]
**Duração estimada:** ~27 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** identificar os constituintes maiores, menores e traço de uma água natural, converter entre as unidades de concentração usadas em hidrogeoquímica e verificar a consistência de uma análise química de água pelo balanço iônico.

## Antes de começar, você precisa saber

- Conceitos básicos de química (mol, massa molar, valência/carga iônica).
- Noções de aquífero e água subterrânea do Módulo 01 (este módulo pressupõe o Módulo 01 como pré-requisito).

## Conteúdo

### Os constituintes de uma água natural

Nenhuma água natural é H₂O pura: ao atravessar a atmosfera, o solo e a rocha, ela dissolve e carrega íons, gases e substâncias em suspensão. A hidrogeoquímica organiza esses constituintes por ordem de abundância (Hem, 1985):

- **Constituintes maiores** (>5 mg/L, tipicamente): definem o caráter químico da água.
  - Cátions maiores: cálcio (Ca²⁺), magnésio (Mg²⁺), sódio (Na⁺), potássio (K⁺).
  - Ânions maiores: bicarbonato (HCO₃⁻) — e, em pH alto, carbonato (CO₃²⁻) —, sulfato (SO₄²⁻), cloreto (Cl⁻).
- **Constituintes menores** (0,01–10 mg/L): ferro, manganês, flúor, nitrato, boro, estrôncio, entre outros — não dominam a carga iônica total, mas frequentemente definem a potabilidade ou um processo geoquímico específico (ex.: nitrato como traçador de contaminação agrícola, tema do Módulo 03).
- **Constituintes traço** (<0,01 mg/L, em geral µg/L ou ng/L): metais pesados, elementos-traço, muitos deles regulados por padrão de potabilidade em concentrações mínimas.
- **Gases dissolvidos:** CO₂, O₂, H₂S, CH₄ — não aparecem no balanço iônico (são espécies neutras ou controlam equilíbrios, não cargas líquidas), mas controlam pH, potencial redox e a própria capacidade de dissolução de minerais (Aula 02).
- **Sólidos totais dissolvidos (TDS):** a soma de todos os constituintes dissolvidos, sólida residual após evaporação e secagem a 180 °C — a medida agregada mais usada para classificar uma água como doce, salobra ou salina.

> [!note] Maior em massa não é maior em carga
> Sílica dissolvida (H₄SiO₄) costuma superar em massa vários dos cátions maiores em águas de aquíferos cristalinos, mas é uma espécie neutra — não entra no balanço iônico (Aula seguinte trata sua origem). "Maior" em hidrogeoquímica clássica refere-se aos íons que dominam a carga, não a todo soluto abundante.

### Unidades de concentração: das mais comuns às mais úteis

Analistas relatam resultados em **mg/L** (miligrama por litro, numericamente igual a ppm para soluções diluídas de densidade ≈1). Mas mg/L não permite comparar diretamente a contribuição de cada íon à carga elétrica total, porque um mol de Ca²⁺ carrega o dobro da carga de um mol de Na⁺. Para isso, converte-se para:

**Concentração molar (mmol/L):** mmol/L = mg/L ÷ massa molar (g/mol).

**Concentração em miliequivalentes por litro (meq/L):** a unidade central da hidrogeoquímica clássica, porque iguala eletricamente cátions e ânions.

meq/L = mmol/L × |valência| = mg/L × |valência| / massa molar = mg/L / peso equivalente

onde o **peso equivalente** de um íon é sua massa molar dividida pelo valor absoluto da sua carga.

| Íon | Massa molar (g/mol) | Valência | Peso equivalente (g/eq) |
|---|---|---|---|
| Ca²⁺ | 40,08 | 2 | 20,04 |
| Mg²⁺ | 24,31 | 2 | 12,16 |
| Na⁺ | 22,99 | 1 | 22,99 |
| K⁺ | 39,10 | 1 | 39,10 |
| HCO₃⁻ | 61,02 | 1 | 61,02 |
| SO₄²⁻ | 96,06 | 2 | 48,03 |
| Cl⁻ | 35,45 | 1 | 35,45 |

(massas molares padrão IUPAC; tabela compilada seguindo o formato de Hem, 1985, cap. 3, e Appelo & Postma, 2005, cap. 1)

> [!important] Por que meq/L e não mg/L para comparar íons
> Um mol de Ca²⁺ (40,08 g) neutraliza duas vezes mais carga negativa que um mol de Na⁺ (22,99 g) de mesma massa molar semelhante. Comparar em mg/L confunde massa com capacidade de neutralizar carga; meq/L resolve isso, e é a unidade que torna o balanço iônico (próxima seção) uma verificação de eletroneutralidade genuína, não uma soma arbitrária.

### O princípio da eletroneutralidade e o balanço iônico

Toda solução aquosa é eletricamente neutra: a soma das cargas positivas iguala a soma das cargas negativas. Como consequência,

Σ cátions (meq/L) ≈ Σ ânions (meq/L)

Essa igualdade é a base do **balanço iônico** (também chamado erro de balanço de cargas, *ion balance error*, IBE), a verificação de consistência mais usada em hidrogeoquímica:

**Erro de balanço (%) = 100 × (ΣCátions − ΣÂnions) / (ΣCátions + ΣÂnions)**, com as somas em meq/L, usando os constituintes maiores (Ca, Mg, Na, K como cátions; HCO₃, SO₄, Cl como ânions — e CO₃²⁻ quando o pH é alto o suficiente para ser significativo).

Um erro de balanço dentro de **±5%** é geralmente aceito como análise consistente para águas de TDS moderado a alto; para águas muito diluídas (TDS baixo, poucos meq/L totais), erros absolutos pequenos em mg/L já produzem percentuais maiores, e a tolerância costuma ser relaxada (até ±10–15% em alguns protocolos) porque o denominador é pequeno (Custodio & Llamas, 1983; APHA *Standard Methods*).

> [!warning] O balanço iônico não confirma que a análise está certa — só que não está grosseiramente errada
> Um erro de balanço aceitável não garante ausência de erro analítico: dois erros de sinal oposto e magnitude semelhante (um cátion superestimado, um ânion subestimado) podem se cancelar e passar despercebidos. O balanço é uma condição **necessária**, não **suficiente**, para validar uma análise — mas sua violação (erro fora da faixa aceitável) é evidência forte e direta de problema analítico, de unidade trocada, ou de um constituinte maior não determinado (ex.: nitrato alto não incluído na soma de ânions).

### Causas comuns de desbalanço

- **Erro de unidade ou de laboratório** (o mais comum na prática): um resultado relatado em unidade errada, ou diluição mal aplicada.
- **Constituinte maior faltante na análise**: se a água tem nitrato ou fluoreto em concentração significativa e o boletim não os reporta, o balanço fecha artificialmente mal para os ânions.
- **Amostra com TDS muito baixo** ou próximo do limite de detecção de algum constituinte maior — erro relativo se amplifica.
- **Erro analítico real** de titulação (alcalinidade/HCO₃⁻, geralmente titulada em campo ou logo após coleta — ver Aula 04) ou de leitura instrumental.
- **Ácidos orgânicos não considerados** como carga aniônica em águas ricas em matéria orgânica (águas de pântano, turfeiras) — casos em que o balanço padrão de íons inorgânicos subestima os ânions estruturalmente, não por erro de laboratório.

## Exemplo trabalhado

**Situação:** uma análise de água subterrânea reporta (em mg/L): Ca²⁺ = 64, Mg²⁺ = 24, Na⁺ = 46, K⁺ = 4, HCO₃⁻ = 293, SO₄²⁻ = 48, Cl⁻ = 35. Verifique o balanço iônico.

**Conversão para meq/L** (mg/L ÷ peso equivalente):

- Ca²⁺: 64 / 20,04 = 3,19
- Mg²⁺: 24 / 12,16 = 1,97
- Na⁺: 46 / 22,99 = 2,00
- K⁺: 4 / 39,10 = 0,10
- **Σ cátions = 3,19 + 1,97 + 2,00 + 0,10 = 7,26 meq/L**

- HCO₃⁻: 293 / 61,02 = 4,80
- SO₄²⁻: 48 / 48,03 = 1,00
- Cl⁻: 35 / 35,45 = 0,99
- **Σ ânions = 4,80 + 1,00 + 0,99 = 6,79 meq/L**

**Erro de balanço = 100 × (7,26 − 6,79) / (7,26 + 6,79) = 100 × 0,47 / 14,05 ≈ 3,3%**

**Conclusão:** dentro da faixa aceitável (±5%) — a análise é consistente o suficiente para uso em interpretação hidrogeoquímica (diagramas da Aula 05). Note que o excesso é de cátions: se o erro fosse muito maior, a primeira hipótese a checar seria um ânion maior faltante (nitrato? fluoreto?) ou erro na titulação de alcalinidade, que costuma ser o constituinte mais sensível a atraso entre coleta e análise (Aula 04).

## Erros comuns

- **Somar mg/L diretamente para checar neutralidade elétrica.** mg/L não é proporcional à carga; a soma só faz sentido fisicamente em meq/L.
- **Esquecer que HCO₃⁻ é, em geral, a espécie de carbonato dominante em pH natural (6,3–8,3)**, e que CO₃²⁻ só se torna significativo acima de pH ≈ 8,3 — incluir CO₃²⁻ desnecessariamente distorce o balanço em águas de pH neutro.
- **Tratar erro de balanço pequeno como prova de que não há erro analítico algum** (ver o alerta acima sobre erros que se cancelam).
- **Usar peso equivalente errado** por esquecer a valência (ex.: tratar Ca²⁺ como se fosse monovalente).

## O que não concluir

- **Que um balanço de 4% significa que a análise está "quase perfeita".** A tolerância de ±5% é um critério de triagem prático, não uma medida de precisão analítica absoluta — cada constituinte individual pode ter incerteza própria maior.
- **Que toda água com balanço ruim deve ser descartada sem investigação.** Antes de descartar, verificar se algum constituinte maior (nitrato, fluoreto, ácidos orgânicos) foi omitido da soma, o que é a causa mais frequentemente recuperável.

## Recap relâmpago

- Constituintes maiores dominam a carga iônica (Ca, Mg, Na, K / HCO₃, SO₄, Cl); menores e traço não dominam massa nem carga, mas podem definir potabilidade ou um processo específico.
- **meq/L = mg/L / peso equivalente**, onde peso equivalente = massa molar / |valência| — é a unidade que permite comparar cargas de íons diferentes.
- **Balanço iônico:** erro (%) = 100×(Σcátions−Σânions)/(Σcátions+Σânions) em meq/L; ±5% é a faixa de aceitação usual, mais permissiva em águas de TDS muito baixo.
- O balanço é condição necessária, não suficiente, para validar uma análise — erros que se cancelam passam despercebidos.

## Próxima aula

[[02-hidrogeoquimica-aula-02-origem-dos-solutos-e-mineralizacao|Aula 02 — Origem dos solutos e mineralização das águas: interação água-rocha, troca iônica e sistema carbonático]]

## Anterior

Primeira aula do módulo. Pressupõe o [[01-hidrogeologia-recursos-hidricos/01-hidrogeologia-recursos-hidricos-modulo|Módulo 01 — Hidrogeologia e recursos hídricos]] concluído.

## Fontes

- Classificação de constituintes maiores, menores e traço; TDS: Hem, J. D. (1985), *Study and Interpretation of the Chemical Characteristics of Natural Water*, 3ª ed., USGS Water-Supply Paper 2254, cap. 3.
- Unidades de concentração, peso equivalente e balanço iônico: Appelo, C. A. J. & Postma, D. (2005), *Geochemical Processes and Applications*, 2ª ed., Balkema, cap. 1; Custodio, E. & Llamas, M. R. (1983), *Hidrología Subterránea*, Omega, cap. 13.
- Critério de aceitação do erro de balanço (±5%): Custodio & Llamas (1983); APHA/AWWA/WEF, *Standard Methods for the Examination of Water and Wastewater*.

<!--
nivel: avancado
palavras_corpo: ~1650

mapa_objetivo_secao:
  geologia-avancado-m02-oa01: "Os constituintes de uma água natural" + "Unidades de concentração: das mais comuns às mais úteis" + "O princípio da eletroneutralidade e o balanço iônico" + "Causas comuns de desbalanço" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: HIDROGEOQ-M02-A01-CONSTITUINTES-001
    claim: "Constituintes maiores de água natural (>5 mg/L tipicamente) são Ca2+, Mg2+, Na+, K+ como cátions e HCO3-, SO4(2-), Cl- como ânions; constituintes menores ficam na faixa 0,01-10 mg/L e traço abaixo de 0,01 mg/L."
    risk: fato
    source: "Hem 1985, cap. 3"
  - claim_id: HIDROGEOQ-M02-A01-PESOEQ-002
    claim: "Peso equivalente de um íon é a massa molar dividida pelo valor absoluto da valência; meq/L = mg/L dividido pelo peso equivalente."
    risk: fato
    source: "Appelo & Postma 2005, cap. 1"
  - claim_id: HIDROGEOQ-M02-A01-BALANCO-003
    claim: "O erro de balanço iônico é calculado como 100*(soma cátions - soma ânions)/(soma cátions + soma ânions) em meq/L, com tolerância usual de ±5% para águas de TDS moderado a alto, relaxada para águas muito diluídas."
    risk: fato
    source: "Custodio & Llamas 1983, cap. 13; APHA Standard Methods"
  - claim_id: HIDROGEOQ-M02-A01-HCO3-004
    claim: "HCO3- é a espécie de carbonato dominante em pH natural entre aproximadamente 6,3 e 8,3; CO3(2-) só se torna significativo acima de pH aproximadamente 8,3."
    risk: fato
    source: "Hem 1985, cap. 3; Appelo & Postma 2005, cap. 1 (diagrama de especiação do sistema carbonático)"
-->
