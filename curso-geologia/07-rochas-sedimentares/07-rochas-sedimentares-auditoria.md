# Auditoria científica: Módulo 07 — Rochas sedimentares

**Auditado em:** 2026-08-17
**Material:** `07-rochas-sedimentares/` — sete aulas do M07
**Modo:** `audit-and-fix`
**Profundidade:** `full`
**Escopo:** intemperismo e maturação; ternários e escala Udden–Wentworth; Folk para arenitos; Dunham e Folk para calcários; químicas, evaporíticas e orgânicas; diagênese; estruturas sedimentares e inferência.
**Veredito da Fase 1:** Requer correção

## Resumo da Fase 1

🔴 0 erros · 🟠 1 imprecisão/omissão que gera erro · 🟡 0 desatualizados · 🔵 0 sem fonte · ⚪ 0 controversos Verificadas e corretas: 16 alegações.

## Achados

### 🟠 1. A rota de Dunham para textura deposicional apagada foi omitida

**claim_id:** `SED-DUNHAM-CRYSTALLINE-001`
**Tipo:** omissão que gera erro
**Onde:** `07-rochas-sedimentares-aula-04-classificacao-carbonaticas-dunham-e-folk.md` · Conteúdo
**Está escrito:** “Se a textura deposicional foi apagada por recristalização intensa, o nome deve comunicar essa limitação, não inventar uma categoria Dunham.”
**Problema:** A ressalva é correta quanto a não reconstruir uma textura que não se preservou, mas o texto deixa de ensinar que o Dunham original inclui a classe **carbonato cristalino** (*crystalline carbonate*) justamente quando a textura deposicional não é reconhecível. Sem essa informação, o aluno pode concluir incorretamente que a classificação não oferece uma saída descritiva.
**Correção proposta:** “Se a textura deposicional foi apagada por recristalização intensa, Dunham a registra como **carbonato cristalino** (*crystalline carbonate*): esse nome comunica que a textura original não é reconhecível, sem inventá-la.”
**Fonte:** Dunham (1962), reproduzido no diagrama do USGS, *Carbonate Geology and Hydro*; AAPG, *Carbonate sedimentary rocks classification*. [USGS](https://pubs.usgs.gov/of/1983/0537/report.pdf) · [AAPG](https://wiki.aapg.org/Carbonate_sedimentary_rocks_classification) · **Nível:** revisada por pares / base de referência
**Confiança:** confirmado
**Também aparece em:** somente a aula 04.

## Verificado e correto

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `SED-WEATHERING-PROCESS-001` | Intemperismo é alteração/desagregação *in situ*; erosão envolve remoção e transporte. | [BGS RR 99-03](https://nora.nerc.ac.uk/id/eprint/3227/1/RR99003.pdf) | confirmado |
| `SED-MATURITY-001` | Maturidade textural e composicional são distinções úteis, sem diagnóstico automático de distância ou ambiente. | Boggs (2014) | provável |
| `SED-WENTWORTH-LIMITS-001` | Areia é 2–0,0625 mm; silte, 0,0625–0,004 mm; argila, <0,004 mm na escala Udden–Wentworth. | [Wentworth (1922)](https://doi.org/10.1086/622910); [USGS](https://pubs.usgs.gov/of/2003/of03-001/htmldocs/nomenclature.htm) | confirmado |
| `SED-TERNARY-READING-001` | As três frações de um ternário normalizado totalizam 100% e são lidas paralelamente ao lado oposto. | [BGS RR 99-03](https://nora.nerc.ac.uk/id/eprint/3227/1/RR99003.pdf) | confirmado |
| `SED-FOLK-ARENITE-001` | Q–F–L é aplicado à composição normalizada do arcabouço de arenitos, não a matriz ou cimento. | Folk (1974); [USGS](https://pubs.usgs.gov/dds/dds-033/USGS_3D/ssx_txt/diagenes.htm) | confirmado |
| `SED-FOLK-SCOPE-001` | Folk de arenitos não é classificação universal de rochas sedimentares nem o Folk de calcários. | [BGS RR 99-03](https://nora.nerc.ac.uk/id/eprint/3227/1/RR99003.pdf) | confirmado |
| `SED-DUNHAM-CRITERIA-001` | Dunham distingue presença de lama, suporte por lama/grãos e ligação orgânica na deposição. | [USGS](https://pubs.usgs.gov/of/1983/0537/report.pdf); [AAPG](https://wiki.aapg.org/Carbonate_sedimentary_rocks_classification) | confirmado |
| `SED-DUNHAM-LIMIT-001` | Mudstone tem <10% de grãos e wackestone >10%, ambos suportados por lama. | [AAPG](https://wiki.aapg.org/Carbonate_sedimentary_rocks_classification) | confirmado |
| `SED-FOLK-CARBONATE-001` | Folk de calcários combina allochems com micrita ou esparita; não é Q–F–L. | Folk (1962); [USGS](https://pubs.usgs.gov/of/1983/0537/report.pdf) | confirmado |
| `SED-EVAPORITE-001` | Evaporitos são descritos pela mineralogia; halita, gipsita e anidrita são constituintes comuns. | [BGS RR 99-03](https://nora.nerc.ac.uk/id/eprint/3227/1/RR99003.pdf) | confirmado |
| `SED-CHERT-001` | Chert é rocha silicosa não clástica, com origens químicas ou biogênicas possíveis. | [BGS RR 99-03](https://nora.nerc.ac.uk/id/eprint/3227/1/RR99003.pdf) | confirmado |
| `SED-DIAGENESIS-001` | Diagênese inclui compactação, cimentação, dissolução e outras mudanças pós-deposição, excluindo metamorfismo. | [USGS](https://pubs.usgs.gov/of/2003/ofr-03-037/htmltext/508document.htm) | confirmado |
| `SED-LITHIFICATION-001` | Compactação e cimentação são mecanismos importantes de litificação e modificam porosidade. | [USGS](https://pubs.usgs.gov/dds/dds-033/USGS_3D/ssx_txt/diagenes.htm) | confirmado |
| `SED-STRUCTURES-001` | Estratificação cruzada registra migração de formas de leito e pode se formar sob água ou vento. | Boggs (2014); [USGS](https://pubs.usgs.gov/of/1976/0083/report.pdf) | provável |
| `SED-STRUCTURES-002` | Gretas resultam de contração associada à perda de água; bioturbação é perturbação por organismos. | Boggs (2014); [USGS](https://pubs.usgs.gov/of/1976/0083/report.pdf) | provável |
| `SED-INFERENCE-LIMITS-001` | As estruturas não permitem, isoladamente, determinar um ambiente deposicional único. | [BGS RR 99-03](https://nora.nerc.ac.uk/id/eprint/3227/1/RR99003.pdf) | confirmado |

## Observações de fonte e escopo

- Foi consultada a BGS como referência pública para sedimentares. A IUGS mantém a competência ampla de sistemática em petrologia, mas não foi identificada uma recomendação IUGS vigente que substitua os esquemas legados Folk e Dunham; por isso eles foram verificados em suas fontes clássicas e em referências institucionais de aplicação.
- O uso do diagrama Q–F–L ficou corretamente separado do esquema modal QAPF de rochas ígneas e do Folk composicional de calcários.
- Não há avaliação ou flashcards do M07 a propagar nesta etapa.

---

## Correções aplicadas

**Aplicadas em:** 2026-08-17

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `SED-DUNHAM-CRYSTALLINE-001` | 🟠 | Corrigido | `07-rochas-sedimentares-aula-04-classificacao-carbonaticas-dunham-e-folk.md` |

**Pendências:** nenhuma. Os sete textos agora não têm achados 🔴 ou 🟠 em aberto.

**Veredito final:** Aprovado. O gate científico do M07 pode ser liberado para a revisão didática; avaliações e flashcards continuam fora do escopo desta etapa.
