# Aula 06: Mol, massa molar e composição em óxidos — com as escalas e unidades da mineralogia

**ID:** mineralogia-m01-a06
**Módulo:** [[01-fundamentos-quimicos-modulo|Módulo 01 — Fundamentos químicos: átomo, tabela periódica e ligação]]
**Duração estimada:** ~30 min
**Nível:** ensino médio, sem geologia prévia (contrato `ensino-medio-sem-geologia-v1`)
**Objetivo:** calcular massa molar, proporções molares e porcentagem em massa (de elementos e de óxidos) a partir de uma fórmula mineral, e converter entre as unidades de comprimento, pressão e temperatura usadas em mineralogia.
**Pré-requisito:** [[01-fundamentos-quimicos-aula-03-ions-e-estados-de-oxidacao-fe-mn-e-s|Aula 03]] (cargas e fórmulas minerais).

## Vocabulário desta aula

| Termo | O que quer dizer |
|---|---|
| **mol** | quantidade de matéria que contém 6,02214076 × 10²³ entidades (constante de Avogadro, valor exato desde 2019). |
| **massa molar (M)** | massa de 1 mol de uma substância, em g/mol; vem da soma das massas atômicas da fórmula. |
| **massa atômica** | massa média de um átomo do elemento, relativa ao carbono-12; é o número de cada casa da tabela periódica. |
| **% em massa (wt%)** | massa de um componente dividida pela massa total, vezes 100. |
| **óxido componente** | óxido hipotético usado para relatar a composição de um mineral (SiO₂, Al₂O₃, FeO, MgO, CaO...). |
| **ångström, nanômetro, micrômetro** | 1 Å = 10⁻¹⁰ m = 0,1 nm; 1 nm = 10⁻⁹ m; 1 µm = 10⁻⁶ m. |
| **pascal (Pa), GPa, bar, kbar** | unidades de pressão: 1 GPa = 10⁹ Pa = 10 kbar; 1 bar = 10⁵ Pa. |
| **kelvin (K)** | escala absoluta de temperatura: T(K) = T(°C) + 273,15. |

## Antes de começar, você precisa saber

- Potências de dez e notação científica (ensino médio). Quem precisar, revise: 10³ × 10⁻⁵ = 10⁻².
- Regra de três e porcentagem.
- Ler fórmulas de óxidos e de minerais e os estados de oxidação de seus elementos, como na fayalita, Fe₂SiO₄ (aula 03).

## Ao final você vai conseguir

- `mineralogia-m01-oa05` — Calcular massa molar, proporções molares e porcentagem em massa de elementos e óxidos a partir de uma fórmula mineral.
- `mineralogia-m01-oa06` — Converter entre as unidades e escalas usadas em mineralogia (Å, nm, µm, GPa, kbar, °C, K) e estimar ordens de grandeza.

## Conteúdo

### O mol: contar por pesagem

Átomos são pequenos demais para contar um a um; contamos **pesando**. Um mol é um número fixo de partículas (6,022 × 10²³), escolhido de modo que a massa de 1 mol de um elemento em gramas seja numericamente igual à sua massa atômica. O carbono tem massa atômica 12,011, e 1 mol de carbono pesa 12,011 g.

Massas atômicas que usaremos (valores convencionais IUPAC, arredondados):

| H | C | O | Na | Mg | Al | Si | S | K | Ca | Mn | Fe |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1,008 | 12,011 | 15,999 | 22,990 | 24,305 | 26,982 | 28,085 | 32,06 | 39,098 | 40,078 | 54,938 | 55,845 |

### Massa molar de um mineral

Somam-se as massas atômicas de todos os átomos da fórmula. Para a forsterita, Mg₂SiO₄: 2 × 24,305 + 28,085 + 4 × 15,999 = 48,610 + 28,085 + 63,996 = **140,691 g/mol**.

Uma **porcentagem em massa de elemento** é a fração da massa molar que cabe a ele: na pirita, FeS₂, M = 55,845 + 2 × 32,06 = 119,965 g/mol, e o ferro responde por 55,845 ÷ 119,965 = 46,6%.

### Composição em óxidos: por que e como

Os laboratórios de análise química de minerais e rochas não reportam "Si, Mg, O", e sim **porcentagens em massa de óxidos**: SiO₂, Al₂O₃, FeO, MgO, CaO, Na₂O, K₂O. Por duas razões: o oxigênio é o ânion dominante (aula 02) e difícil de medir diretamente em muitos métodos, e os cátions ficam em estados de oxidação conhecidos (aula 03). O óxido relatado é uma **convenção de contabilidade**: não significa que haja SiO₂ dentro da forsterita, e sim que a massa de Si foi expressa como SiO₂.

Para converter a fórmula em óxidos, reescreva-a como soma de óxidos: Mg₂SiO₄ = 2 MgO + SiO₂. Depois use as massas molares dos óxidos: MgO = 24,305 + 15,999 = 40,304; SiO₂ = 28,085 + 2 × 15,999 = 60,083.

O ferro tem um cuidado à parte (aula 03): se a análise não diz o estado de oxidação, o ferro é relatado como **FeO total** ou como **Fe₂O₃ total**. Os fatores de conversão vêm das massas: Fe em FeO = 55,845 ÷ 71,844 = 0,7773; Fe em Fe₂O₃ = 2 × 55,845 ÷ 159,687 = 0,6994.

### Do peso ao mol: a razão entre os átomos

A fórmula nasce de **proporções molares**, não de proporções de massa. Dividindo a % em massa de cada óxido pela sua massa molar, obtém-se o **número relativo de mols**. A razão entre esses números revela a estequiometria. Essa é a base do cálculo de fórmula estrutural do módulo 09.

### Unidades: escalas que a mineralogia usa

**Comprimento.** A escala do átomo e do cristal é o **ångström** (1 Å = 0,1 nm = 100 pm). Ordens de grandeza de referência: a ligação Si–O mede cerca de 1,62 Å; o diâmetro de um íon, de ~0,5 Å (Si⁴⁺ em coordenação 4, isto é, com quatro vizinhos) a ~2,8 Å (O²⁻) e ~3,6 Å (Cl⁻), segundo os raios de Shannon; a cela unitária (o bloco mínimo que, repetido, constrói o cristal; módulo 06) de um mineral comum, 5 a 20 Å; uma lâmina delgada de rocha para microscópio, 30 µm = 0,03 mm = 3 × 10⁵ Å; um grão de areia, 0,06 a 2 mm.

**Pressão.** A unidade do SI é o pascal, pequeno demais para a Terra, então usam-se **GPa** (10⁹ Pa) e, em petrologia (o estudo das rochas), o **kbar** (mil bar). A conversão é 1 GPa = 10 kbar; 1 bar = 10⁵ Pa ≈ 1 atm (1 atm = 1,01325 bar). Como orientação, a pressão litostática (a exercida pelo peso das rochas acima) cresce cerca de 27 MPa por km na crosta (0,027 GPa/km): 10 km correspondem a ~0,27 GPa = ~2,7 kbar. Regra de bolso: 1 kbar ≈ 3 a 4 km de profundidade. No centro da Terra, a pressão é da ordem de 360 GPa.

**Temperatura.** Em petrologia, usa-se °C; em termodinâmica, kelvin: T(K) = T(°C) + 273,15. Uma diferença de 1 K é igual a uma diferença de 1 °C. A escala absoluta é obrigatória nas fórmulas de energia livre do módulo 22.

**Estimar ordens de grandeza.** Arredonde para a potência de dez mais próxima, calcule e confira se o resultado faz sentido. Se a resposta diz que uma lâmina delgada tem 10 Å de espessura, algo saiu errado por cinco ordens de grandeza.

## Exemplo trabalhado

**Problema 1.** Escreva a composição da forsterita (Mg₂SiO₄) em % de óxidos e confira proporções molares.

1. Massa molar: 140,691 g/mol (acima).
2. Em óxidos: 2 MgO + 1 SiO₂ → massas 2 × 40,304 = 80,608 e 60,083 (soma = 140,691, confere).
3. **%MgO = 80,608 ÷ 140,691 = 57,29%; %SiO₂ = 60,083 ÷ 140,691 = 42,71%** (soma = 100%).
4. Proporção molar: 57,29 ÷ 40,304 = 1,421; 42,71 ÷ 60,083 = 0,711. Razão 1,421 ÷ 0,711 = 2,0 → **2 MgO : 1 SiO₂**, o que retorna à fórmula Mg₂SiO₄.

**Problema 2 (hematita).** Qual o % de Fe em Fe₂O₃ (M = 159,687)? 2 × 55,845 ÷ 159,687 = **69,94%**. Se uma análise dá 30% de Fe₂O₃ total, o ferro puro é 30 × 0,6994 = 20,98%.

**Problema 3 (unidades).**
- Quantas ligações Si–O (1,62 Å) cabem na espessura de uma lâmina de 30 µm? Passe tudo para metro: 30 µm = 30 × 10⁻⁶ m = 3 × 10⁻⁵ m. Como 1 Å = 10⁻¹⁰ m, são (3 × 10⁻⁵) ÷ 10⁻¹⁰ = 3 × 10⁵ Å. Então (3 × 10⁵) ÷ 1,62 ≈ **1,9 × 10⁵**, da ordem de 10⁵.
- 2,5 kbar em GPa: 2,5 ÷ 10 = **0,25 GPa**, correspondente a ~9 km de profundidade (0,25 ÷ 0,027).
- 750 °C em K: 750 + 273,15 = **1023,15 K**.

**Quantos átomos há em 1 cm³ de quartzo?** Densidade ~2,65 g/cm³; M(SiO₂) = 60,083 → 2,65 ÷ 60,083 = 0,0441 mol de SiO₂ → 0,0441 × 6,022 × 10²³ ≈ 2,7 × 10²² unidades de fórmula, ou 8 × 10²² átomos (3 por unidade). Ordem de grandeza: 10²², razão pela qual nunca contamos átomos, só mols.

## Erros comuns

- **Trocar massa por mols.** A razão entre massas (57,29 : 42,71) não é a razão entre átomos; só a razão entre mols é.
- **Esquecer de multiplicar pelos índices:** em Mg₂SiO₄ o magnésio entra duas vezes.
- **Somar o ferro como FeO e como Fe₂O₃ na mesma conta,** sem decidir se é ferro total ou se há Fe²⁺ e Fe³⁺ separados.
- **Misturar kbar com GPa:** 1 GPa = 10 kbar, não 100.
- **Somar 273 a uma diferença de temperatura.** A soma vale para temperaturas, não para diferenças.
- **Esquecer que wt% de óxido é convenção,** não a forma real em que o elemento está no mineral.

## O que não concluir

- Que o % de óxidos revele quais minerais há numa rocha: muitos minerais diferentes podem ter o mesmo % de SiO₂.
- Que 1 kbar corresponda exatamente a 3,5 km: a conversão depende da densidade da rocha.
- Que as massas atômicas sejam constantes: variam levemente com os isótopos (S, por exemplo); usamos valores convencionais.

## Recap relâmpago

- 1 mol = 6,02214076 × 10²³ entidades; a massa molar (g/mol) é a soma das massas atômicas da fórmula (forsterita: 140,691).
- Composição em óxidos: MgO e SiO₂ na forsterita: 57,29% e 42,71%; razão molar 2 : 1.
- O ferro é relatado como FeO ou Fe₂O₃ total; Fe/FeO = 0,7773; Fe/Fe₂O₃ = 0,6994.
- Comprimento: 1 Å = 0,1 nm = 100 pm; lâmina delgada 30 µm = 3 × 10⁵ Å; Si–O ≈ 1,62 Å.
- Pressão: 1 GPa = 10 kbar = 10⁹ Pa; ~27 MPa/km na crosta; 1 kbar ≈ 3 a 4 km.
- Temperatura: K = °C + 273,15; diferenças de 1 K e 1 °C são iguais.
- Estime a ordem de grandeza antes e depois de cada conta.

## Próxima aula

Este é o fim do módulo 01. O próximo, [[02-o-que-e-mineral-modulo|Módulo 02 — O que é um mineral: definição, espécie e classificação]], usa o que foi visto aqui (íons, ligações, fórmulas e óxidos) para fixar, com precisão normativa, o que a IMA chama de mineral.

## Fontes consultadas

- IUPAC/CIAAW, *Abridged Standard Atomic Weights* (tabela de 2024, consultada em 2026-09-30).
- BIPM, *SI Brochure* (9ª ed.) e NIST/CODATA: constante de Avogadro 6,02214076 × 10²³ mol⁻¹ (exata) e atmosfera padrão 101 325 Pa (exata).
- Raios iônicos: Shannon, R. D. (1976), *Acta Crystallographica* A32, 751–767 (Si⁴⁺ IV 0,26 Å; O²⁻ VI 1,40 Å; Cl⁻ VI 1,81 Å).
- Pressão no centro da Terra (~364 GPa): PREM, Dziewonski & Anderson (1981), *Physics of the Earth and Planetary Interiors* 25, 297–356.
- Klein & Dutrow, *Manual of Mineral Science*, 23ª ed.: composição química e análise em óxidos.
- Densidade do quartzo e valores de ligação Si–O: Mindat / *Handbook of Mineralogy*; Nesse, *Introduction to Mineralogy*.

<!--
nivel: ensino-medio-sem-geologia-v1
palavras_corpo: 1337
cobertura:
  mineralogia-m01-oa05: [Conteúdo, Exemplo trabalhado]
  mineralogia-m01-oa06: [Conteúdo, Exemplo trabalhado]
alegacoes_auditaveis:
  - claim_id: QUI-MOL-AVOG-001
    claim: "A constante de Avogadro vale exatamente 6,02214076e23 por mol desde a redefinicao do SI de 2019."
    risk: numero
    source: "BIPM, SI Brochure 9a ed.; NIST CODATA"
    audit: "verificado em 2026-09-30"
  - claim_id: QUI-MASSA-ATOM-001
    claim: "Massas atomicas usadas: H 1,008; C 12,011; O 15,999; Na 22,990; Mg 24,305; Al 26,982; Si 28,085; S 32,06; K 39,098; Ca 40,078; Mn 54,938; Fe 55,845."
    risk: numero
    source: "IUPAC CIAAW, Abridged Standard Atomic Weights 2024 (ciaaw.org), consultada em 2026-09-30"
    audit: "verificado em 2026-09-30: os 12 valores coincidem com a tabela abreviada de 2024 (S = 32,06 +- 0,02)"
  - claim_id: QUI-FORST-MOLAR-001
    claim: "Forsterita Mg2SiO4: M = 140,691 g/mol; 57,29% MgO e 42,71% SiO2; razao molar MgO:SiO2 = 2:1."
    risk: numero
    source: "recalculo com CIAAW 2024 em 2026-09-30"
    audit: "verificado (57,294% / 42,706%; 1,4214/0,7108 = 2,000)"
  - claim_id: QUI-FEOX-FATOR-001
    claim: "Fatores de conversao: Fe/FeO = 0,7773 (M FeO = 71,844); Fe/Fe2O3 = 0,6994 (M Fe2O3 = 159,687); pirita FeS2 M = 119,965 g/mol, 46,6% Fe; 30% Fe2O3 -> 20,98% Fe."
    risk: numero
    source: "recalculo com CIAAW 2024 em 2026-09-30"
    audit: "verificado (0,77731; 0,69943; 46,55%; 20,982%)"
  - claim_id: QUI-UNID-PRESS-001
    claim: "1 GPa = 10 kbar = 1e9 Pa; 1 bar = 1e5 Pa; 1 atm = 1,01325 bar; pressao litostatica da crosta ~27 MPa/km (rho ~2,7 g/cm3); 1 kbar ~ 3-4 km; pressao no centro da Terra da ordem de 360 GPa."
    risk: numero
    source: "BIPM/NIST (101 325 Pa exato); rho g h = 26,5 MPa/km a 2,7 g/cm3; PREM (Dziewonski & Anderson 1981): 364 GPa no centro, 329 GPa no limite nucleo interno/externo"
    audit: "verificado em 2026-09-30 (1 kbar = 3,4-3,8 km para rho 3,0-2,7)"
  - claim_id: QUI-UNID-ESCALA-001
    claim: "Ligacao Si-O ~1,62 A; diametro de ions de ~0,5 A (Si4+ IV) a ~2,8 A (O2-) e ~3,6 A (Cl-); lamina delgada de ~30 micrometros = 3e5 A; cela unitaria de minerais comuns de ~5-20 A; grao de areia 0,06-2 mm."
    risk: numero
    source: "Shannon (1976); Greenwood & Earnshaw (Si-O 1,61-1,63 A); escala de Wentworth"
    audit: "corrigido em 2026-09-30 (antes: 'diametro de um ion, 2 a 3 A', que exclui os cations pequenos do proprio curso: Si4+, Al3+, Mg2+)"
  - claim_id: QUI-UNID-TEMP-001
    claim: "T(K) = T(C) + 273,15; uma diferenca de 1 K equivale a 1 C."
    risk: fato
    source: "BIPM SI Brochure"
    audit: "verificado em 2026-09-30"
  - claim_id: QUI-QZ-DENS-001
    claim: "Densidade do quartzo ~2,65 g/cm3; 1 cm3 tem ~2,7e22 unidades de formula SiO2 (~8e22 atomos)."
    risk: numero
    source: "Handbook of Mineralogy (quartz, D = 2,65); recalculo"
    audit: "verificado em 2026-09-30 (2,656e22; 7,97e22)"
-->
