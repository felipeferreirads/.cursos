# Auditoria científica: Módulo 06 — Rochas ígneas e magmatismo

**Auditado em:** 2026-08-17
**Material:** `06-rochas-igneas/` — oito aulas
**Modo:** audit-and-fix
**Profundidade:** full
**Escopo:** mecanismos de fusão e evolução magmática, série de Bowen, texturas, corpos ígneos, QAPF, TAS e ambientes tectônicos; consistência entre aulas
**Veredito final:** Aprovado

## Resumo

🔴 0 erros · 🟠 2 imprecisões · 🟡 0 desatualizados · 🔵 1 sem fonte · ⚪ 0 controversos Verificadas e corretas: 13 alegações.

## Achados

### 🟠 1. O escopo do QAPF foi apresentado de forma ampla demais

**claim_id:** `PET-QAPF-SCOPE-001`
**Tipo:** confusão de escopo
**Onde:** aula 06 · “Antes do nome, escolha a régua certa” e roteiro QAPF
**Está escrito:** “O QAPF é a régua formal recomendada pela IUGS para rochas ígneas cristalinas [...]” e “Se é afanítica ou vítrea [...] a rota será TAS.”
**Problema:** QAPF não é uma classificação indiscriminada de toda rocha ígnea cristalina. O roteiro principal vale para rochas plutônicas adequadas à classificação modal; rochas ultramáficas, gabroicas e especiais têm diagramas/regras próprios. TAS é indicado para muitas rochas vulcânicas comuns quando a moda não pode ser determinada, mas também tem exclusões.
**Correção proposta:** restringir explicitamente o QAPF às rochas adequadas ao esquema e apresentar TAS como rota frequente, não universal.
**Fonte:** Le Maitre et al., *Igneous Rocks: A Classification and Glossary of Terms*, IUGS, 2ª ed. (2002), capítulo 2, [Cambridge Core](https://www.cambridge.org/core/books/abs/igneous-rocks-a-classification-and-glossary-of-terms/classification-and-nomenclature/CDE0C29406FE932BA336508541A32286) · **Nível:** normativa
**Confiança:** confirmado
**Também aparece em:** aula 07, na comparação QAPF–TAS.

### 🟠 2. O roteiro TAS não manda normalizar a análise para base anidra

**claim_id:** `PET-TAS-NORM-002`
**Tipo:** omissão que gera erro
**Onde:** aula 07 · “Roteiro TAS” e exemplo trabalhado
**Está escrito:** “Leia SiO₂ [...] Some Na₂O e K₂O [...] Plote o par”.
**Problema:** o procedimento formal requer recalcular a análise para 100% em base anidra antes de plotar. Sem essa etapa, amostras com água, CO₂ ou total analítico diferente de 100% podem cair num campo incorreto.
**Correção proposta:** inserir a conferência de alteração e a normalização para 100% sem H₂O e CO₂ antes da plotagem; declarar que o exemplo já está normalizado.
**Fonte:** Le Maitre et al. (2002), recomendações IUGS; British Geological Survey, *Rock Classification Scheme, Volume 1: Igneous*, reedição 2020, [BGS](https://www.bgs.ac.uk/download/bgs-rock-classification-scheme-igneous/) · **Nível:** normativa
**Confiança:** confirmado
**Também aparece em:** nenhum outro arquivo nesta fase.

### 🔵 3. O manifesto técnico acrescenta uma profundidade não demonstrada no texto

**claim_id:** `PET-SLAB-DEPTH-003`
**Tipo:** evidência insuficiente
**Onde:** aula 08 · comentário `alegacoes_auditaveis`
**Está escrito:** “a placa pode permanecer sólida além de 100 km de profundidade.”
**Problema:** a aula e a fonte USGS citada sustentam o mecanismo geral — fluidos da placa favorecem fusão na cunha mantélica —, mas não documentam esse limite numérico específico. O número não é necessário ao objetivo.
**Correção proposta:** remover “além de 100 km de profundidade” e manter a afirmação qualitativa.
**Fonte:** USGS, [Are the tectonic plates floating on magma?](https://www.usgs.gov/faqs/are-tectonic-plates-floating-magma), atualizado em 2026 · **Nível:** base de referência
**Confiança:** não verificado
**Também aparece em:** somente no comentário técnico da aula 08.

## Verificado e correto

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `PET-MELT-MECH-004` | Descompressão e água podem iniciar fusão sem exigir uma camada global de magma. | USGS, “Are the tectonic plates floating on magma?” (2026) | confirmado |
| `PET-MELT-PART-005` | Fusão parcial separa líquido e resíduo de composições diferentes. | USGS/GIA e petrologia de referência | confirmado |
| `PET-FRAC-CRYST-006` | Separar cristais modifica o líquido remanescente. | USGS, estudos de inclusões de melt | confirmado |
| `PET-BOWEN-SERIES-007` | Os ramos descontínuo e contínuo são modelos gerais, não listas obrigatórias. | petrologia ígnea de referência | confirmado |
| `PET-TEXTURE-COOL-008` | Resfriamento lento tende a grãos maiores; rápido, a grãos finos ou vidro. | USGS, “What are igneous rocks?” (2026) | confirmado |
| `PET-TEXTURE-VES-009` | Vesículas registram bolhas preservadas, não um estilo eruptivo único. | USGS | confirmado |
| `PET-CROSSCUT-AGE-010` | O corpo que corta é relativamente mais jovem que o cortado. | USGS | confirmado |
| `PET-DYKE-SILL-011` | Dique é discordante; soleira é aproximadamente concordante com a estrutura encaixante. | BGS | confirmado |
| `PET-QAPF-EXAMPLE-012` | Q=24, A=36, P=40 cai no campo monzogranito. | Le Maitre et al. (2002) | confirmado |
| `PET-TAS-AXES-013` | TAS usa SiO₂ contra Na₂O+K₂O em porcentagem de óxidos. | Le Maitre et al. (2002) | confirmado |
| `PET-TAS-EXAMPLE-014` | O ponto SiO₂=50 e álcalis=3 cai no campo basalto. | Le Maitre et al. (2002) | confirmado |
| `PET-RIDGE-MELT-015` | Dorsais favorecem fusão por descompressão e produção de crosta oceânica. | USGS | confirmado |
| `PET-SUBDUCTION-FLUID-016` | Água liberada em subducção favorece fusão do manto sobrejacente. | USGS | confirmado |

## Observações não factuais

- Há wikilinks desatualizados e uma sequência “próxima aula” ainda baseada no plano antigo de seis aulas; serão tratados na revisão didática, não como achados científicos.

---

## Correções aplicadas

**Aplicadas em:** 2026-08-17

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `PET-QAPF-SCOPE-001` | 🟠 | Corrigido | aula 06 |
| `PET-TAS-NORM-002` | 🟠 | Corrigido | aula 07 |
| `PET-SLAB-DEPTH-003` | 🔵 | Corrigido por remoção da precisão sem fonte | aula 08 |

**Pendências:** nenhuma. Gate científico liberado: 0 achados vermelhos ou laranja abertos.
