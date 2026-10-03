# Auditoria científica — Módulo 04: Exploração, explotação e gestão dos recursos hídricos subterrâneos

**Módulo:** [[04-exploracao-gestao-aguas-subterraneas-modulo|Módulo 04 — Exploração, explotação e gestão dos recursos hídricos subterrâneos]]
**Escopo:** 4 aulas (geologia-avancado-m04-a01 a a04), 17 alegações auditáveis extraídas dos blocos de metadados de cada aula.
**Método:** verificação de cada `claim_id` contra a literatura padrão de hidrogeologia de exploração e gestão (Todd & Mays, 2005; Kruseman & de Ridder, 1994; Driscoll, 1986; Fetter, 2001) e as fontes primárias/normativas citadas (Sophocleous, 2000; Galloway & Burbey, 2011; Dillon et al., 2019; Lei Federal 9.433/1997; Acordo sobre o Aquífero Guarani, 2010), com verificação cruzada dos cálculos numéricos dos exemplos trabalhados e buscas web para confirmar datas e atribuição de autoria dos instrumentos legais e das metodologias.
**Data:** 2026-08-26

## Resumo do veredito

| Severidade | Contagem |
|---|---|
| 🔴 Erro | 0 |
| 🟠 Impreciso | 0 |
| 🟡 Desatualizado/a matizar | 0 |
| 🔵 Controverso (área com debate legítimo) | 0 |
| ⚪ Sem fonte direta verificável (mas plausível/consensual) | 1 |

**Veredito geral: aprovado.** Nenhum achado vermelho, laranja ou amarelo. O achado ⚪ é de baixo impacto (uma prática de engenharia consolidada sem fórmula fechada única na literatura) e não exige correção de conteúdo.

## Achados

### ⚪ [EXPLOT-M04-A02-ESPACAMENTO-003] — Espaçamento economicamente ótimo entre poços
**Aula:** 02. **Claim:** "o espaçamento entre poços de um campo resulta de um balanço entre reduzir a interferência hidráulica (maior espaçamento) e conter o custo de tubulação de adução e de área de terreno, existindo um espaçamento economicamente ótimo além do qual o ganho hidráulico marginal é pequeno".
**Achado:** a afirmação qualitativa (trade-off entre interferência hidráulica e custo de infraestrutura) é amplamente aceita e consistente com Driscoll (1986, cap. 17) e com a prática de projeto descrita em Todd & Mays (2005). Não existe, porém, uma fórmula fechada única e universalmente citada para "o" espaçamento economicamente ótimo — cada projeto resolve esse trade-off por otimização caso a caso (custo de tubulação real do projeto × ganho hidráulico calculado por superposição), não por uma equação de manual. O texto da aula já apresenta a ideia como um princípio de balanço, não como uma fórmula fechada, o que é consistente com o estado da literatura.
**Correção proposta:** nenhuma. O tratamento qualitativo do texto já está alinhado à ausência de uma fórmula fechada única.
**Confiança:** alta.

## Verificação amostral de valores numéricos e cálculos (checklist)

- Sequência lógica das três fases (exploração → avaliação → explotação) e uso de SEV como método geofísico de exploração (Aula 01): consistente com Todd & Mays (2005, cap. 8) e Fetter (2001, cap. 15). ✅
- Necessidade de teste de longa duração (72h+) para detectar limites hidráulicos na fase de avaliação (Aula 01): consistente com Kruseman & de Ridder (1994). ✅
- Distinção terminológica "exploração" (busca) vs. "explotação" (extração econômica) em português técnico (Aula 01): uso consolidado na literatura em português (ABAS, traduções de Todd & Mays); não há um único dicionário técnico oficial citável, mas o uso é consistente entre as fontes em português consultadas. ✅ (nota terminológica, não afirmação factual empírica)
- Fórmula de rebaixamento composto por superposição, s_total(P) = Σᵢ(Qᵢ/4πT)·W(uᵢ) (Aula 02): consistente com a extensão padrão da solução de Theis para múltiplos poços (Kruseman & de Ridder, 1994, cap. 5; Fetter, 2001, cap. 5). ✅
- Exemplo trabalhado da Aula 02 (T=500 m²/dia, S=2×10⁻⁴, Q=1.920 m³/dia, t=3.650 dias, r=200 m e r≈283 m): recalculado independentemente pela aproximação de Cooper-Jacob — s_B ≈ s_D ≈ 4,01 m, s_C ≈ 3,80 m, soma ≈ 11,8 m. Confere com a fórmula T=2,3Q/(4πT_·Δs) e S=2,25Tt₀/r²S aplicada de forma consistente (mesma formulação já auditada e aprovada no Módulo 01, Aula 05). ✅
- Distinção entre vazão sustentável do campo e soma de vazões ótimas individuais (Aula 02): consistente com Driscoll (1986, cap. 17). ✅
- Método dos poços imagem para limites de recarga/barreira (Aula 02): mesma referência já auditada e aprovada no Módulo 01 (Ferris et al., 1962, citado indiretamente via Kruseman & de Ridder, 1994). ✅
- Ciclo de vida de projeto de abastecimento (viabilidade → projeto básico → executivo → implantação → operação) (Aula 03): consistente com prática de engenharia de projetos de infraestrutura hídrica descrita em Todd & Mays (2005, cap. 8). ✅
- Definição e uso de LCOW (custo nivelado da água) como análogo ao LCOE (Aula 03): metodologia consolidada, documentada por organismos como o World Bank Group em notas técnicas sobre tarifação de água. ✅
- Exemplo trabalhado da Aula 03 (CAPEX R$ 2,4 milhões, OPEX R$ 180 mil/ano, 20 anos, 1.200.000 m³/ano): recalculado — custo total = 2.400.000 + 180.000×20 = 6.000.000; volume total = 1.200.000×20 = 24.000.000 m³; custo médio = 6.000.000/24.000.000 = 0,25 R$/m³. Confere. ✅
- Questão 10 do questionário (CAPEX R$ 1,8 milhão, OPEX R$ 120 mil/ano, 15 anos, 900.000 m³/ano): recalculado — custo total = 1.800.000 + 120.000×15 = 3.600.000; volume total = 900.000×15 = 13.500.000 m³; custo médio = 3.600.000/13.500.000 ≈ 0,2667 R$/m³. Confere com o valor apresentado (≈ R$ 0,267/m³). ✅
- Distinção entre tarifa de serviço e cobrança pelo uso da água bruta, com base na Lei 9.433/1997 (Aula 03): consistente com os artigos 5º, 12 e 19–22 da Lei Federal 9.433/1997, que tratam da outorga e da cobrança como instrumentos distintos da tarifação de serviço de saneamento (regulada por legislação de saneamento básico, não pela Lei das Águas). ✅
- Definição de superexplotação como assinatura temporal de desequilíbrio persistente, não valor absoluto de vazão (Aula 04): consistente com a crítica de Sophocleous (2000) ao conceito de safe yield, já auditada no Módulo 01. ✅
- Sinais físicos de superexplotação (rebaixamento persistente, intrusão salina, redução de baseflow, secamento de nascentes, subsidência, deterioração de qualidade) (Aula 04): consistente com a literatura padrão de gestão de recursos hídricos subterrâneos (Sophocleous, 2000; Galloway & Burbey, 2011 para subsidência). ✅
- Mecanismo de subsidência por consolidação inelástica de camadas confinantes argilosas, com casos documentados (Cidade do México, Vale de San Joaquin) (Aula 04): confirmado por busca — Galloway & Burbey (2011, *Hydrogeology Journal* 19(8)) é a referência de revisão padrão citada na literatura sobre subsidência induzida por bombeamento, e os dois casos citados são amplamente documentados na literatura (subsidência de vários metros em ambos os casos ao longo do século XX). ✅
- Definição de uso conjuntivo e de MAR/ASR (Aula 04): consistente com Dillon et al. (2019, *Hydrogeology Journal* 27(1)), revisão de referência sobre recarga gerenciada de aquíferos. ✅
- Acordo sobre o Aquífero Guarani (2010), assinado por Brasil, Argentina, Paraguai e Uruguai, sem criar órgão supranacional de gestão direta (Aula 04): confirmado por busca — o acordo, assinado em San Juan (Argentina) em 2010, estabelece cooperação e compartilhamento de dados, mantendo a gestão da porção do aquífero em cada território sob competência nacional (e, no Brasil, estadual). ✅

## Cobertura de objetivos de aprendizagem

| Objetivo | Aulas que cobrem | Verificado |
|---|---|---|
| geologia-avancado-m04-oa01 | a01 | ✅ |
| geologia-avancado-m04-oa02 | a02 | ✅ |
| geologia-avancado-m04-oa03 | a03 | ✅ |
| geologia-avancado-m04-oa04 | a04 | ✅ |

Todos os quatro objetivos de aprendizagem do módulo têm uma aula dedicada e claims auditáveis correspondentes; nenhum objetivo ficou sem cobertura.

## Recomendação

Nenhuma correção obrigatória de conteúdo. Aprovar o módulo para avaliação (questionário) e memorização (flashcards). O único achado ⚪ fica registrado para referência futura — não há fórmula fechada única de espaçamento ótimo de campo de poços a citar, e o texto já trata o tema corretamente como um princípio de balanço de projeto, não como um cálculo padronizado.
