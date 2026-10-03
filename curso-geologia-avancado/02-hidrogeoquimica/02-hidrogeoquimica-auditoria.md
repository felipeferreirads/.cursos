# Auditoria científica — Módulo 02: Hidrogeoquímica

**Módulo:** [[02-hidrogeoquimica-modulo|Módulo 02 — Hidrogeoquímica]]
**Escopo:** 5 aulas (geologia-avancado-m02-a01 a a05), 17 alegações auditáveis extraídas dos blocos de metadados de cada aula.
**Método:** verificação de cada `claim_id` contra a literatura padrão de hidrogeoquímica (Hem 1985; Appelo & Postma 2005; Custodio & Llamas 1983; Freeze & Cherry 1979) e os artigos/normas originais citados como fonte primária (Piper 1944; Stiff 1951; Schoeller 1962; Chebotarev 1955; Puls & Barcelona 1996; legislação brasileira: Decreto-Lei 7.841/1945, Portaria GM/MS 888/2021, Resolução CONAMA 396/2008).
**Data:** 2026-08-26

## Resumo do veredito

| Severidade | Contagem |
|---|---|
| 🔴 Erro | 0 |
| 🟠 Impreciso | 0 |
| 🟡 Desatualizado/a matizar | 1 |
| 🔵 Controverso (área com debate legítimo) | 0 |
| ⚪ Sem fonte direta verificável (mas plausível/consensual) | 1 |

**Veredito geral: aprovado.** Nenhum achado vermelho ou laranja. Os dois achados 🟡/⚪ são de baixo impacto e não exigem correção de conteúdo.

## Achados

### 🟡 [HIDROGEOQ-M02-A04-PORTARIA-001] — Nomenclatura histórica da norma de potabilidade
**Aula:** 04. **Claim:** "Portaria GM/MS nº 888/2021 ... que atualizou a antiga Portaria de Consolidação nº 5/2017 do Ministério da Saúde."
**Achado:** a Portaria GM/MS nº 888, de 4 de maio de 2021, de fato altera o Anexo XX da Portaria de Consolidação nº 5/2017 (que por sua vez consolidou normas anteriores, incluindo a Portaria MS nº 2.914/2011). A relação de sucessão está correta, mas o texto da aula simplifica uma cadeia regulatória com mais de um degrau histórico (2914/2011 → PRC 5/2017, Anexo XX → alterado pela Portaria 888/2021) numa frase só. Não é um erro, apenas uma simplificação da linhagem normativa completa, adequada ao nível da aula.
**Correção proposta:** nenhuma alteração obrigatória — a aula já identifica corretamente a norma vigente (Portaria GM/MS 888/2021) como a referência prática para potabilidade. Registrado para precisão histórica, caso o Módulo 03 (que trata de contaminação e também cita padrões de qualidade) precise detalhar a cadeia normativa completa.
**Confiança:** alta.

### ⚪ [HIDROGEOQ-M02-A04-LOWFLOW-002] — Valor numérico de vazão em amostragem de baixa vazão
**Aula:** 04. **Claim:** amostragem de baixa vazão usa vazão "tipicamente <0,5 L/min".
**Achado:** o valor está de acordo com a prática consagrada (Puls & Barcelona, 1996, recomendam tipicamente 0,1–0,5 L/min, ajustado conforme a formação e o diâmetro do poço), mas o protocolo original não fixa um único número absoluto — a vazão ótima varia com a condutividade hidráulica local e deve ser calibrada em campo para minimizar o rebaixamento. Não há erro, mas o número é uma aproximação de faixa consensual, não uma constante normativa fixa.
**Correção proposta:** nenhuma. O valor citado está dentro da faixa usual da literatura e é apropriado ao nível introdutório da aula.
**Confiança:** alta.

## Verificação amostral de valores numéricos (checklist)

- Pesos equivalentes da tabela da Aula 01 (Ca²⁺ 20,04; Mg²⁺ 12,16; Na⁺ 22,99; K⁺ 39,10; HCO₃⁻ 61,02; SO₄²⁻ 48,03; Cl⁻ 35,45 g/eq): recalculados a partir das massas molares IUPAC padrão e das valências corretas — todos conferem. ✅
- Exemplo trabalhado da Aula 01 (balanço iônico, erro ≈3,3%): recalculado independentemente a partir dos mg/L fornecidos — Σcátions = 7,26 meq/L, Σânions = 6,79 meq/L, erro = 3,3%. Confere. ✅
- Questão 1 do questionário (erro de balanço ≈11,3%): recalculado — Σcátions = 4,39 meq/L, Σânions = 3,50 meq/L, erro = 11,3%. Confere. ✅
- Fórmula da hidrólise do feldspato-K (Aula 02): estequiometria balanceada (K, Al, Si, O, H, C conferidos lado a lado) — consistente com a forma padrão apresentada em Appelo & Postma (2005) e Freeze & Cherry (1979). ✅
- Faixa de pH da chuva natural (≈5,6) e razão Cl⁻/Na⁺ da água do mar (≈1,8 em massa) (Aula 03): consistentes com Hem (1985) e Appelo & Postma (2005). ✅
- Faixa de PCO₂ do solo (10–100× atmosférico) (Aula 03): consistente com a ordem de grandeza reportada em Appelo & Postma (2005, cap. 3) para solos com atividade biológica moderada a alta; solos muito ativos podem exceder esse valor, o que a aula já qualifica ("podendo chegar a mais"). ✅
- Gradiente geotérmico continental (~25–30 °C/km) (Aula 03, exemplo trabalhado): consistente com valores padrão de crosta continental estável fora de contexto vulcânico ativo (Freeze & Cherry, 1979, cap. 6; Custodio & Llamas, 1983). ✅
- Critérios de estabilização de parâmetros de campo (±0,1 pH, ±3% EC, ±10 mV Eh, ±10% OD) (Aula 04): consistentes com os valores de referência do protocolo USEPA de baixa vazão (Puls & Barcelona, 1996). ✅
- Datas e autoria dos diagramas (Piper 1944, Stiff 1951, Schoeller 1962) (Aula 05): conferidas contra as referências bibliográficas originais citadas — autoria, ano e periódico corretos. ✅
- Autoria e ano da sequência de Chebotarev (1955) (Aula 02): conferido — Chebotarev publicou a série em *Geochimica et Cosmochimica Acta*, volume 8, em três partes ao longo de 1955. ✅

## Cobertura de objetivos de aprendizagem

| Objetivo | Aulas que cobrem | Verificado |
|---|---|---|
| geologia-avancado-m02-oa01 | a01 | ✅ |
| geologia-avancado-m02-oa02 | a02, a03 | ✅ |
| geologia-avancado-m02-oa03 | a04 | ✅ |
| geologia-avancado-m02-oa04 | a05 | ✅ |

Todos os quatro objetivos de aprendizagem do módulo têm pelo menos uma aula dedicada e claims auditáveis correspondentes; nenhum objetivo ficou sem cobertura.

## Recomendação

Nenhuma correção obrigatória de conteúdo. Aprovar o módulo para avaliação (questionário) e memorização (flashcards). O achado 🟡 e o achado ⚪ ficam registrados para consulta futura, sem bloquear a conclusão do módulo.
