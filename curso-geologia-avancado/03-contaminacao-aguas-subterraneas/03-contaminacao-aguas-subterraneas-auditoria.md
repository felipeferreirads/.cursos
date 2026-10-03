# Auditoria científica — Módulo 03: Contaminação dos recursos hídricos subterrâneos

**Módulo:** [[03-contaminacao-aguas-subterraneas-modulo|Módulo 03 — Contaminação dos recursos hídricos subterrâneos]]
**Escopo:** 5 aulas (geologia-avancado-m03-a01 a a05), 20 alegações auditáveis extraídas dos blocos de metadados de cada aula.
**Método:** verificação de cada `claim_id` contra a literatura padrão de hidrogeologia de contaminantes (Fetter 1999; Domenico & Schwartz 1998; Freeze & Cherry 1979; Wiedemeier et al. 1999; Pankow & Cherry 1996) e as fontes primárias/normativas citadas (Ogata & Banks 1961; Gelhar, Welty & Rehfeldt 1992; Hampton & Miller 1988; Foster 1987; Foster & Hirata 1988; Aller et al. 1987; USEPA 1999; legislação e normas brasileiras: Portaria GM/MS 888/2021, Resolução CONAMA 420/2009, ABNT NBR 15515-1:2007), com buscas web para confirmar valores numéricos e a atribuição de autoria/ano dos métodos.
**Data:** 2026-08-26

## Resumo do veredito

| Severidade | Contagem |
|---|---|
| 🔴 Erro | 0 |
| 🟠 Impreciso | 0 |
| 🟡 Desatualizado/a matizar | 0 |
| 🔵 Controverso (área com debate legítimo) | 0 |
| ⚪ Sem fonte direta verificável (mas plausível/consensual) | 2 |

**Veredito geral: aprovado.** Nenhum achado vermelho, laranja ou amarelo. Os dois achados ⚪ são de baixo impacto (um valor numérico de norma regulatória específica e uma nomenclatura de classe de vulnerabilidade) e não exigem correção de conteúdo.

## Achados

### ⚪ [CONTAM-M03-A01-BENZENO-004] — Valor numérico do padrão de potabilidade do benzeno
**Aula:** 01. **Claim:** "benzeno (5 µg/L pela Portaria GM/MS 888/2021)".
**Achado:** a busca confirmou que a Portaria GM/MS nº 888/2021 altera o Anexo XX da Portaria de Consolidação nº 5/2017 e mantém a tabela de substâncias químicas que representam risco à saúde, mas não foi possível recuperar o valor numérico exato da linha "benzeno" diretamente do texto legal nas buscas realizadas (o PDF oficial não retornou a tabela completa em texto indexável). O valor de 5 µg/L (0,005 mg/L) citado é o valor historicamente estável nessa tabela desde a Portaria MS 2.914/2011 e coincide com o padrão da USEPA (MCL de benzeno = 5 µg/L) — consistente e de alta plausibilidade, mas não confirmado por leitura direta da tabela oficial nesta auditoria.
**Correção proposta:** nenhuma alteração obrigatória — manter o valor citado, mas registrar a ressalva de que a confirmação foi por convergência de fontes secundárias e precedente normativo, não por leitura direta da tabela vigente. Recomenda-se checagem direta da tabela na próxima revisão do curso, caso o valor tenha sido alterado por norma superveniente.
**Confiança:** alta (por convergência), não confirmada por fonte primária direta.

### ⚪ [CONTAM-M03-A05-GOD-002] — Nomenclatura das classes de vulnerabilidade do método GOD
**Aula:** 05. **Claim:** classificação do índice GOD em "insignificante, baixa, moderada, alta ou extrema".
**Achado:** a busca confirmou a estrutura de cinco classes por faixa numérica do índice GOD (0,0–0,1; 0,1–0,3; 0,3–0,5; 0,5–0,7; 0,7–1,0), mas a nomenclatura em inglês mais reproduzida na literatura recente é *very weak / weak / moderate / strong / extreme* — o texto da aula usa uma tradução equivalente, mas não literal ("insignificante" para *very weak*, "alta" para *strong*), que é a nomenclatura usual em traduções e adaptações do método na literatura em português e espanhol da América Latina (onde o método é mais aplicado). Não há erro de valor nem de lógica — apenas uma variação de nomenclatura entre traduções, sem fonte única definitiva em português.
**Correção proposta:** nenhuma. A classificação qualitativa e as faixas numéricas usadas no exemplo trabalhado (0,72 → alta a extrema; 0,16 → baixa) são consistentes com as faixas oficiais (0,7–1,0 = extrema; 0,1–0,3 = fraca/baixa).
**Confiança:** alta.

## Verificação amostral de valores numéricos (checklist)

- Fórmula de velocidade linear média v_x = (K×i)/n_e (Aula 02): consistente com a formulação padrão de Freeze & Cherry (1979, cap. 2) e Fetter (1999). ✅
- Exemplo trabalhado da Aula 02 (v_D = 0,032 m/dia; v_x = 0,128 m/dia; t ≈ 938 dias): recalculado independentemente — 8×0,004=0,032; 0,032/0,25=0,128; 120/0,128=937,5. Confere. ✅
- Solução de Ogata-Banks (Aula 02): forma C(x,t)/C₀ = ½erfc((x−v_xt)/(2√(D_Lt))) conferida contra Ogata & Banks (1961, USGS Prof. Paper 411-A) e reproduzida em Fetter (1999, cap. 2) e Domenico & Schwartz (1998, cap. 14) — correta. ✅
- Fator de retardação R = 1 + (ρ_b/n_e)×K_d e K_d = K_oc×f_oc (Aula 03): formulação padrão de Freeze & Cherry (1979, cap. 9) e Fetter (1999, cap. 4). ✅
- Exemplo trabalhado da Aula 03 (K_d=0,4 L/kg; R=3,88; v_soluto≈0,033 m/dia; t≈3.636 dias): recalculado — 200×0,002=0,4; (1,8/0,25)=7,2; 7,2×0,4=2,88; 1+2,88=3,88; 0,128/3,88=0,033; 120/0,033≈3.636. Confere. ✅
- Sequência de aceptores de elétrons (Aula 03): O₂ > NO₃⁻ > Mn(IV) > Fe(III) > SO₄²⁻ > CO₂, ordem termodinâmica padrão, conferida contra Wiedemeier et al. (1999, cap. 4) e a literatura consolidada de biorremediação. ✅
- Classificação LNAPL/DNAPL por densidade relativa à água (Aula 04): consistente com Fetter (1999, cap. 7) e Pankow & Cherry (1996). ✅
- Efeito de superestimativa da espessura de LNAPL em poço de monitoramento (Aula 04): atribuição a Hampton & Miller (1988) conferida — é a referência padrão citada na literatura de caracterização de LNAPL (Fetter, 1999; USEPA guidance documents). ✅
- Relação de Ghyben-Herzberg e o multiplicador ≈40 (Aula 04): confirmado por busca — densidade da água doce ≈1,000 g/cm³, água do mar ≈1,025 g/cm³, resultando no fator ≈40 (1,000/0,025), consistente com USGS (Circular 1262) e a literatura clássica (Freeze & Cherry, 1979; Custodio & Llamas, 1983). Exemplo trabalhado (z₁=60 m; z₂=36 m; Δz=24 m) recalculado e conferido. ✅
- Método GOD, três parâmetros e produto multiplicativo (Aula 05): confirmado por busca — Foster & Hirata (1988) e reproduções subsequentes da metodologia (ex.: revisões em periódicos indexados) confirmam G×O×D com cada parâmetro de 0 a 1. ✅
- Método DRASTIC, sete parâmetros somados e ponderados (Aula 05): atribuição a Aller et al. (1987, USEPA/600/2-87-035) é a referência padrão e correta da literatura de vulnerabilidade de aquíferos. ✅
- Etapas de investigação de área contaminada e normas brasileiras citadas (Aula 05): ABNT NBR 15515-1:2007 (avaliação preliminar) e Resolução CONAMA 420/2009 (valores orientadores) são as referências normativas corretas e vigentes para o procedimento de gerenciamento de áreas contaminadas no Brasil, com a CETESB como referência de procedimento estadual amplamente adotada como modelo nacional. ✅

## Cobertura de objetivos de aprendizagem

| Objetivo | Aulas que cobrem | Verificado |
|---|---|---|
| geologia-avancado-m03-oa01 | a01 | ✅ |
| geologia-avancado-m03-oa02 | a02, a03 | ✅ |
| geologia-avancado-m03-oa03 | a04 | ✅ |
| geologia-avancado-m03-oa04 | a05 | ✅ |

Todos os quatro objetivos de aprendizagem do módulo têm pelo menos uma aula dedicada e claims auditáveis correspondentes; nenhum objetivo ficou sem cobertura.

## Recomendação

Nenhuma correção obrigatória de conteúdo. Aprovar o módulo para avaliação (questionário) e memorização (flashcards). Os dois achados ⚪ ficam registrados para consulta futura — em especial, recomenda-se que uma futura auditoria transversal do curso confirme o valor exato da tabela vigente de VMP para benzeno diretamente na fonte primária, caso o valor seja usado novamente em módulos futuros de qualidade da água.
