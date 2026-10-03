# Auditoria científica — Módulo 26: Química para geociências

**Modo:** `audit-and-fix` · **Profundidade:** `full`
**Data:** 2026-08-19
**Escopo:** as 5 aulas do módulo, auditadas em conjunto (aulas 01–05), incluindo
consistência interna entre elas (mesma equação da pirita reaproveitada nas aulas 01, 02 e 05; mesmos valores de massa molar entre aulas 01 e 02). **Veredito: Aprovado.** 0 achados 🔴, 0 achados 🟠, 0 achados 🟡, 0 achados 🔵, 0 achados ⚪.

## Metodologia

Leitura das 5 aulas em conjunto, listagem de todas as alegações verificáveis (valores numéricos, definições, equações balanceadas, fatos mineralógicos e geoquímicos), verificação por `web_search` contra fontes normativas de química geral e geoquímica, e checagem cruzada de consistência interna (mesmos números e mesma equação reaparecendo em mais de uma aula do módulo).

## Verificado e correto

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `GEO-M26-A01-CONSERVACAO-MASSA-001` | Lei da conservação da massa (Lavoisier, séc. XVIII) | Química geral básica; história da química | Confirmado |
| `GEO-M26-A01-FELDSPATO-CAULINITA-002` | Hidrólise do feldspato potássico (ortoclásio) em caulinita, sílica dissolvida e K⁺: `2 KAlSi3O8 + 2H+ + H2O → Al2Si2O5(OH)4 + 4 SiO2 + 2K+` | Krauskopf & Bird, *Introduction to Geochemistry*; Faure, *Principles and Applications of Geochemistry* | Confirmado — equação conferida átomo a átomo, fecha em K, Al, Si, O, H e carga |
| `GEO-M26-A01-PIRITA-DAM-003` | Oxidação da pirita produz óxido de ferro e ácido sulfúrico, associada a drenagem ácida de mina | AMD Basics (amrclearinghouse.org); literatura consolidada de AMD/DAM | Confirmado |
| `GEO-M26-A01-FERRUGEM-BALANCEAMENTO-004` | `4 Fe + 3 O2 → 2 Fe2O3` balanceada | Estequiometria básica — conferida por contagem direta | Confirmado |
| `GEO-M26-A02-MOL-AVOGADRO-001` | 1 mol ≈ 6,02 × 10²³ partículas | Química geral básica (constante de Avogadro, CODATA) | Confirmado |
| `GEO-M26-A02-MASSA-MOLAR-PIRITA-002` | Massa molar de FeS₂ ≈ 120 g/mol | Massas atômicas IUPAC (Fe ≈ 55,85; S ≈ 32,07) | Confirmado |
| `GEO-M26-A02-MASSA-MOLAR-H2SO4-003` | Massa molar de H₂SO₄ ≈ 98 g/mol | Massas atômicas IUPAC | Confirmado |
| `GEO-M26-A02-REAGENTE-LIMITANTE-DAM-004` | Cobrir rejeito sulfetado restringindo O₂ é estratégia real de mitigação de DAM | Literatura de engenharia de minas / geoquímica ambiental sobre controle de AMD | Confirmado |
| `GEO-M26-A02-CALCULO-ESTEQUIOMETRICO-005` | 100 kg de pirita → ≈163 kg de H₂SO₄ (O₂/H₂O em excesso) | Cálculo estequiométrico refeito de forma independente a partir da equação balanceada: confere (≈163.000 g) | Confirmado |
| `GEO-M26-A03-PH-DEFINICAO-001` | pH = −log₁₀[H⁺] | Química geral básica (definição de Sørensen) | Confirmado |
| `GEO-M26-A03-PH-LOGARITMICO-002` | Escala de pH logarítmica, 1 unidade = fator 10 em [H⁺] | Química geral básica | Confirmado |
| `GEO-M26-A03-CHUVA-PH-NATURAL-003` | Chuva não poluída tem pH natural ≈5,6 (por CO₂ dissolvido) | EPA; IERE; literatura de química atmosférica — faixa citada 5,0–5,6, valor de referência 5,6 confirmado | Confirmado |
| `GEO-M26-A03-DAM-PH-004` | DAM por oxidação de sulfetos pode chegar a pH < 3 | Literatura consolidada de AMD/DAM (valores documentados, inclusive abaixo de 3 em casos extremos) | Confirmado |
| `GEO-M26-A03-PPM-PORCENTAGEM-005` | 1% = 10.000 ppm | Definição matemática direta | Confirmado |
| `GEO-M26-A04-EQUILIBRIO-DEFINICAO-001` | Definição de equilíbrio químico reversível | Química geral básica | Confirmado |
| `GEO-M26-A04-LE-CHATELIER-002` | Princípio de Le Chatelier | Química geral básica | Confirmado |
| `GEO-M26-A04-SISTEMA-CARBONATO-003` | Sistema carbonato controla dissolução/precipitação de calcita e explica cavernas cársticas e espeleotemas | Faure; Krauskopf & Bird; literatura de espeleologia cárstica | Confirmado |
| `GEO-M26-A04-DOLOMITA-CINETICA-004` | Dolomita segue o mesmo tipo de equilíbrio, mas com cinética/solubilidade diferentes da calcita | Geoquímica de carbonatos consolidada | Confirmado |
| `GEO-M26-A05-OXIDACAO-REDUCAO-001` | Definições de oxidação/redução e oxirredução | Química geral básica | Confirmado |
| `GEO-M26-A05-HEMATITA-FE3-002` | Fe³⁺ na hematita | Cálculo direto (O = −2) + mineralogia descritiva | Confirmado |
| `GEO-M26-A05-MAGNETITA-FE2-FE3-003` | Magnetita: Fe²⁺:Fe³⁺ = 1:2, estrutura de espinélio inverso | Klein & Dutrow; fontes cristaloquímicas (Fe3O4 inverse spinel, confirmado por busca) | Confirmado |
| `GEO-M26-A05-LATERITA-004` | Laterita: solo/rocha residual rica em óxidos/hidróxidos de Fe e Al, intemperismo tropical | Krauskopf & Bird; geologia econômica de depósitos residuais | Confirmado |
| `GEO-M26-A05-PIRITA-ESTADOS-OXIDACAO-005` | Estados de oxidação na oxidação da pirita: Fe +2→+3, S −1→+6, O 0→−2 | Cálculo direto a partir da equação balanceada, convenção padrão para o par dissulfeto S₂²⁻ | Confirmado |

## Consistência interna verificada

- A equação balanceada da oxidação da pirita (`4 FeS2 + 15 O2 + 8 H2O → 2 Fe2O3 + 8 H2SO4`) é usada de forma **idêntica** nas aulas 01, 02 e 05 — sem divergência de coeficientes entre as três.
- As massas molares de FeS₂ (120 g/mol) e H₂SO₄ (98 g/mol) usadas na aula 02 são as mesmas reaproveitadas implicitamente na aula 05. Sem divergência.
- Os valores de pH nos dois cenários da aula 03 (pH 6 e pH 3) e a comparação de "cem vezes" (pH 5→3) na introdução da mesma aula são matematicamente consistentes entre si (10² e 10³, respectivamente, conferidos).
- Nenhuma aula deste módulo redefine vocabulário já fixado pelas pontes do Módulo 04 (átomo, elétron, ligação química) de forma divergente — checado contra `04-cristalografia-quimica-minerais-aula-01` e `-aula-02`.

## Nota (fora do escopo da auditoria, apenas registro)

A equação de oxidação da pirita usada nas três aulas é a equação **global balanceada** (net reaction), consolidada em fontes de referência de AMD/DAM — não descreve o mecanismo real em etapas (que envolve intermediários como Fe²⁺, Fe³⁺, tiossulfato, sulfito e outros, conforme a literatura de cinética de oxidação de pirita). Isso é prática padrão em ensino introdutório de estequiometria e não constitui erro; nenhuma das aulas afirma que a reação ocorre num único passo elementar.

## Correções aplicadas

Nenhuma. Nenhum achado 🔴/🟠/🟡/🔵/⚪ — nada a corrigir nesta rodada.

**Pendências:** nenhuma.
