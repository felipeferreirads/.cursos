# Auditoria científica — Módulo 01: Hidrogeologia e recursos hídricos

**Módulo:** [[01-hidrogeologia-recursos-hidricos-modulo|Módulo 01 — Hidrogeologia e recursos hídricos]]
**Escopo:** 7 aulas (geologia-avancado-m01-a01 a a07), 33 alegações auditáveis extraídas dos blocos de metadados de cada aula.
**Método:** verificação de cada `claim_id` contra a literatura padrão de hidrogeologia (Freeze & Cherry 1979; Fetter 2001; Driscoll 1986) e os artigos originais citados como fonte primária (Theis 1935; Cooper & Jacob 1946; Tóth 1963; Sophocleous 2000; Taylor et al. 2013, entre outros), além da legislação brasileira citada (Lei 9.433/1997, Constituição Federal 1988).
**Data:** 2026-08-26

## Resumo do veredito

| Severidade | Contagem |
|---|---|
| 🔴 Erro | 0 |
| 🟠 Impreciso | 0 |
| 🟡 Desatualizado/a matizar | 2 |
| 🔵 Controverso (área com debate legítimo) | 1 |
| ⚪ Sem fonte direta verificável (mas plausível/consensual) | 1 |

**Veredito geral: aprovado.** Nenhum achado vermelho ou laranja. Os quatro achados amarelo/azul/branco são todos de baixo impacto — nuances ou atualizações de precisão que não invalidam nenhum conceito ensinado — e foram sinalizados diretamente nas aulas correspondentes via callout ou nota, quando aplicável, ou registrados aqui para acompanhamento.

## Achados

### 🟡 [HIDRO-M01-A03-TOTH-002] — Nuance sobre generalidade do modelo de Tóth
**Aula:** 03. **Claim:** "Tóth (1963) demonstrou que a topografia de uma bacia sedimentar controla o desenvolvimento hierárquico de sistemas de fluxo subterrâneo local, intermediário e regional."
**Achado:** correto quanto à autoria e à tese central, mas a solução original de Tóth (1963) é estritamente 2D, em regime permanente, para um domínio homogêneo e isotrópico de geometria simples. A generalização para bacias 3D heterogêneas veio de trabalhos posteriores (Freeze & Witherspoon, 1966–1967, já citados na aula, e Tóth, 2009, *Gravitational Systems of Groundwater Flow*). A aula não afirma o contrário, mas um leitor poderia inferir que o resultado já nasceu geral.
**Correção proposta:** nenhuma alteração de texto necessária — a aula já cita Freeze & Witherspoon (1967) na mesma seção, o que mitiga a leitura de generalidade indevida. Registrado como nota de acompanhamento.
**Confiança:** alta.

### 🟡 [HIDRO-M01-A07-FOSSIL-002] — Precisão sobre "recarga desprezível" no Ogallala
**Aula:** 07. **Claim:** "partes do Aquífero Ogallala... hoje recebe recarga atual desprezível ou muito menor que a taxa histórica de extração."
**Achado:** o Ogallala é heterogêneo: porções norte (Nebraska) têm recarga atual não desprezível e taxas de depleção baixas; a caracterização de "aquífero fóssil"/recarga desprezível aplica-se com mais rigor às porções sul (Texas, Novo México, Kansas ocidental), como a própria aula já qualifica com "partes do". O texto da aula já usa a formulação corretamente restrita ("partes do... onde a recarga atual é muito menor que a taxa histórica"); o achado é de reforço, não de erro.
**Correção proposta:** nenhuma — a redação já está qualificada corretamente. Mantido como nota de vigilância para não generalizar em material futuro (Módulo 04, que retoma o tema).
**Confiança:** alta.

### 🔵 [HIDRO-M01-A06-SAFEYIELD-002] — Área de debate técnico legítimo
**Aula:** 06. **Claim:** vazão segura (safe yield) é "considerada insuficiente isoladamente pela literatura moderna" e foi "substituída" por vazão sustentável.
**Achado:** a crítica de Sophocleous (2000) é amplamente aceita e citada, mas "substituída" é uma simplificação didática — na prática de gestão (inclusive em normas técnicas brasileiras e na própria linguagem de outorga), o conceito de vazão segura/disponibilidade hídrica continua em uso corrente ao lado de critérios de vazão sustentável, sem substituição formal completa em todos os arcabouços regulatórios. Não é um erro factual sobre a literatura acadêmica, mas é uma área onde prática regulatória e consenso acadêmico não coincidem totalmente.
**Correção proposta:** nenhuma alteração obrigatória — a aula já apresenta a crítica corretamente atribuída a uma fonte específica, sem afirmar unanimidade regulatória. Classificado como controverso apenas para registro, não como falha.
**Confiança:** média.

### ⚪ [HIDRO-M01-A04-ANATOMIA-001] — Regra prática de dimensionamento sem citação de norma específica
**Aula:** 04. **Claim:** razão D50 do pré-filtro / D50 do aquífero "entre 4 e 6".
**Achado:** a faixa numérica é consensual na literatura de engenharia de poços (Driscoll 1986 é a referência-padrão da indústria), mas normas nacionais específicas (ex.: ABNT) não fixam esse número exato — é uma regra de boas práticas de engenharia, não uma norma compulsória citável por número de artigo. Não há erro; apenas a fonte é uma prática consagrada de manual técnico, não uma norma regulatória.
**Correção proposta:** nenhuma. A fonte já citada (Driscoll 1986) é apropriada e suficiente para o nível do curso.
**Confiança:** alta.

## Verificação amostral de valores numéricos (checklist)

- Faixas de porosidade e K por litologia (Aula 01, tabela): consistentes com Freeze & Cherry (1979, Tabela 2.2) e Fetter (2001) dentro da ordem de grandeza esperada. ✅
- Fórmula de Ghyben-Herzberg e fator ~40 (Aula 06): a razão ρf/(ρs−ρf) com ρf=1,000 e ρs=1,025 dá exatamente 40 (1,000/0,025 = 40) — aritmética conferida. ✅
- Cálculo do exemplo trabalhado da Aula 05 (Cooper-Jacob, T ≈ 784 m²/dia, S ≈ 2,7×10⁻⁴): recalculado independentemente, valores batem (T = 3450/4,398 ≈ 784,4; S = 2,25×784×5,556×10⁻⁴/3600 ≈ 2,72×10⁻⁴). ✅
- Cálculo do exemplo trabalhado da Aula 02 (Darcy, vx ≈ 105 m/ano): recalculado (3,3×10⁻⁶ m/s × 86400 s/dia ≈ 0,286 m/dia × 365 ≈ 104,4 m/ano). ✅
- Percentuais de composição elementar da crosta e abundância modal — não se aplicam a este módulo (eram do módulo 40); não reutilizados aqui. N/A.
- Elementos legais citados (Lei 9.433/1997, art. 26 CF/1988, Acordo do Aquífero Guarani 2010): conferidos contra o texto normativo padrão — corretos quanto a ano, número e conteúdo essencial. ✅

## Cobertura de objetivos de aprendizagem

| Objetivo | Aulas que cobrem | Verificado |
|---|---|---|
| geologia-avancado-m01-oa01 | a01 | ✅ |
| geologia-avancado-m01-oa02 | a02, a03 | ✅ |
| geologia-avancado-m01-oa03 | a04, a05 | ✅ |
| geologia-avancado-m01-oa04 | a06, a07 | ✅ |

Todos os quatro objetivos de aprendizagem do módulo têm pelo menos uma aula dedicada e claims auditáveis correspondentes; nenhum objetivo ficou sem cobertura.

## Recomendação

Nenhuma correção obrigatória de conteúdo. Aprovar o módulo para avaliação (questionários) e memorização (flashcards). Os dois achados 🟡 e o achado 🔵 ficam registrados para consulta futura, sem bloquear a conclusão do módulo; nenhum ficou como "em aberto" com necessidade de correção pendente.
