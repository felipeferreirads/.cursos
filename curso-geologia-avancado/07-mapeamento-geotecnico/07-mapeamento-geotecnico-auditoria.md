# Auditoria científica — Módulo 07: Metodologia de mapeamento geotécnico

**Módulo:** [[07-mapeamento-geotecnico-modulo|Módulo 07 — Metodologia de mapeamento geotécnico]]
**Escopo:** 4 aulas (geologia-avancado-m07-a01 a a04), 30 alegações auditáveis extraídas dos blocos de metadados de cada aula.
**Método:** verificação de cada `claim_id` contra a literatura de referência de cartografia geotécnica e análise de risco (IAEG/UNESCO 1976; Zuquette 1987; Zuquette & Gandolfi 2004; Varnes 1984; Fell et al. 2008; Burrough, McDonnell & Lloyd 2015) e contra o texto das publicações primárias e dos diplomas legais citados (De Biasi 1992; Skempton & DeLory 1957; Chung & Fabbri 2003; Ferretti, Prati & Rocca 2001; Guzzetti et al. 2008; Ministério das Cidades/IPT 2007; IPT 1986; ISRM 1981; Leis nº 6.766/1979, 10.257/2001, 12.608/2012 e 12.651/2012; Decreto nº 89.817/1984), com recálculo independente do exemplo numérico de estabilidade e verificação aritmética do exemplo de sobreposição ponderada.
**Data:** 2026-08-27

## Resumo do veredito

| Severidade | Contagem |
|---|---|
| 🔴 Erro | 0 |
| 🟠 Impreciso | 0 |
| 🟡 Desatualizado/a matizar | 1 |
| 🔵 Controverso (área com debate legítimo) | 1 |
| ⚪ Sem fonte direta verificável (mas plausível/consensual) | 2 |

**Veredito geral: aprovado.** Nenhum achado vermelho ou laranja — o gate de qualidade do plugin está satisfeito e o módulo está liberado para avaliação e memorização. O achado 🟡 diz respeito à volatilidade da legislação citada e **já está tratado no próprio texto** por um callout de advertência explícito, não exigindo correção. O achado 🔵 registra um debate metodológico ativo e legítimo. Os dois achados ⚪ são convenções e atribuições de limiar já qualificadas como tais no texto.

## Achados

### 🟡 [CARTGEO-M07-A03-LEI12608-003] — Legislação citada sujeita a alterações posteriores
**Aula:** 03 (com reflexo na Aula 02, quanto à Lei 6.766/1979).
**Claim relacionado:** exigência de mapeamento de áreas suscetíveis e de carta geotécnica de aptidão à urbanização introduzida pela Lei 12.608/2012.
**Achado:** o enquadramento descrito é correto — a Lei 12.608/2012 instituiu a Política Nacional de Proteção e Defesa Civil e alterou o Estatuto da Cidade (Lei 10.257/2001) e a Lei 6.766/1979, condicionando a ampliação do perímetro urbano, nos municípios inscritos no cadastro nacional de municípios com áreas suscetíveis, à elaboração de carta geotécnica de aptidão à urbanização. A ressalva é de **atualidade**, não de correção: esses dispositivos sofreram alterações posteriores (entre elas as introduzidas pela Lei 14.285/2021), de modo que a redação vigente pode divergir da original em detalhes de aplicação, prazos e definições. Material didático que cita legislação envelhece de forma silenciosa, e um curso de nível de especialização precisa sinalizar isso.
**Correção proposta:** nenhuma. O texto da Aula 03 **já traz um callout de advertência dedicado** ("Legislação muda; verifique o texto consolidado"), instruindo a tratar as referências legais como enquadramento estável do instrumento e a confirmar a redação atual antes de fundamentar parecer técnico. O bloco de metadados da alegação também registra a ressalva. Tratamento adequado.
**Confiança:** alta.

### 🔵 [CARTGEO-M07-A03-METODOS-004] — Modelos de aprendizado de máquina em cartografia de suscetibilidade com efeito regulatório
**Aula:** 03 (com reflexo na Aula 04). **Claim relacionado:** inclusão de algoritmos de aprendizado de máquina entre os métodos estatísticos de produção de cartas de suscetibilidade.
**Achado:** a menção é factualmente correta — florestas aleatórias, *gradient boosting* e redes neurais são hoje amplamente empregados em suscetibilidade a escorregamentos, e frequentemente superam os métodos estatísticos clássicos em métricas de desempenho. Há, contudo, um debate ativo e não encerrado na literatura sobre sua adequação quando a carta produz **efeito regulatório**: modelos de alto desempenho e baixa interpretabilidade dificultam a auditoria do critério de classificação, tensionando justamente a exigência que a Aula 01 estabelece como obrigatória (a legenda deve declarar o critério, sob pena de a carta ser inauditável) e que a Aula 04 reforça (o critério precisa ser explicitável para que possa ser contestado por quem é afetado). Argumenta-se, do outro lado, que a subjetividade dos pesos heurísticos não é mais auditável na prática, e que técnicas de explicabilidade mitigam a objeção.
**Correção proposta:** nenhuma. O texto não endossa nem rejeita a abordagem — lista o aprendizado de máquina como desenvolvimento recente dentro da família estatística e, no mesmo bloco, adverte que o método "depende inteiramente da qualidade e da completude do inventário" e "herda seus vieses", que é a limitação de maior consequência prática. As exigências de rastreabilidade e de explicitação de critério ficam declaradas nas Aulas 01 e 04 como requisitos gerais, aplicáveis a qualquer método.
**Confiança:** alta.

### ⚪ [CARTGEO-M07-A02-DEBIASI-004] — Fundamentação técnica dos limiares de 5% e 12% e referência bibliográfica de De Biasi (1992)
**Aula:** 02. **Claim:** classes de declividade <5%, 5–12%, 12–30%, 30–47% e >47% e os significados atribuídos a cada limiar.
**Achado:** os **valores** das classes conferem com a proposta de De Biasi (1992) e com seu uso consolidado na cartografia geotécnica brasileira, e os limiares de **30%** e de **45° (100%)** têm fundamento legal direto e verificável (Lei 6.766/1979 e Lei 12.651/2012, ambas conferidas). Já a fundamentação técnica atribuída aos limiares de **5%** e **12%** (urbanização sem restrição relevante, mecanização agrícola, ocupação convencional) varia de formulação entre autores que reproduzem a proposta, sem uma definição única e canônica — são limiares de origem prática, consolidados pelo uso. Ressalva adicional de baixo impacto: a paginação citada para o artigo de De Biasi na *Revista do Departamento de Geografia* (USP, n. 6) não pôde ser confirmada com segurança e deve ser verificada contra o original antes de ser reproduzida em trabalho formal.
**Correção proposta:** nenhuma obrigatória. O texto já apresenta as duas primeiras faixas com linguagem de limite prático, e reserva a linguagem categórica exatamente para os dois limiares de base legal, que é a distinção que importa para o uso.
**Confiança:** média-alta.

### ⚪ [CARTGEO-M07-A03-VALIDACAO-008] — Limiar de AUC considerado bom
**Aula:** 03. **Claim:** "valores acima de ~0,8 são usualmente considerados bons na literatura de suscetibilidade a escorregamentos".
**Achado:** a distinção entre curva de sucesso e curva de predição, e o uso da área sob a curva como métrica-resumo, conferem com Chung & Fabbri (2003) e com a prática consolidada. O limiar de 0,8, porém, é uma **convenção de interpretação** difundida, não um valor com fundamento estatístico próprio: o que constitui desempenho aceitável depende da razão de custo entre falsos positivos e falsos negativos, que em suscetibilidade a escorregamentos é fortemente assimétrica e específica de cada aplicação. O texto qualifica corretamente com "usualmente considerados" e com o til, sem apresentar 0,8 como critério de aprovação.
**Correção proposta:** nenhuma.
**Confiança:** alta.

## Verificação amostral de fórmulas, dados e citações (checklist)

- Distinção entre critério de agrupamento do mapa geológico (origem e idade) e da carta geotécnica (comportamento frente ao uso), com o exemplo de rocha sã e manto de alteração como uma unidade geológica e duas geotécnicas (Aula 01): consistente com IAEG/UNESCO (1976) e Zuquette & Gandolfi (2004). ✅
- Atribuição do guia de referência à IAEG, publicado pela UNESCO em 1976, com tipologia por propósito, conteúdo e escala (Aula 01): confere com a publicação original. ✅
- Atribuição da sistematização brasileira a Zuquette e colaboradores na EESC-USP a partir dos anos 1980, com adaptação a solos tropicais (Aula 01): confere com Zuquette (1987) e Zuquette & Gandolfi (2004). ✅
- Faixas de escala e o nível de decisão que cada uma sustenta, e a impossibilidade de ampliar uma carta além de sua escala de levantamento (Aula 01): consistente com IAEG/UNESCO (1976), Zuquette & Gandolfi (2004) e Prandini et al. (1995). ✅
- Composição do produto completo (carta + legenda com critério declarado + memorial com dados, incertezas e limitações de uso) (Aula 01): consistente com as fontes metodológicas citadas. ✅
- Classificação de materiais inconsolidados por origem, com estrutura reliquiar em solos residuais e contato basal do colúvio como plano preferencial de escorregamento (Aula 02): confere com Zuquette & Gandolfi (2004). ✅
- Escala de graus de alteração W1 a W6 e a primazia do grau de alteração sobre a litologia isolada (Aula 02): confere com ISRM (1981), consistente com o tratamento dado no Módulo 05. ✅
- Lei 6.766/1979, art. 3º, parágrafo único, inciso III — vedação de parcelamento em declividade igual ou superior a 30%, salvo atendidas exigências específicas das autoridades competentes (Aula 02): texto conferido; a ressalva final ("salvo...") está corretamente reproduzida na aula, e sua omissão seria um erro material. ✅
- Lei 12.651/2012, art. 4º, inciso V — encostas com declividade superior a 45°, equivalente a 100% na linha de maior declive, como Área de Preservação Permanente (Aula 02): texto conferido. ✅
- Equivalências trigonométricas dos limiares: tan 25° = 0,466 ≈ 47% e tan 45° = 1,00 = 100% (Aula 02). Recalculadas e conferem. ✅
- Subestimação **sistemática** (não aleatória) das declividades altas por MDE de resolução grosseira, por efeito de promediação da elevação em células maiores (Aula 02): consistente com a literatura de análise de terreno e com o comportamento conhecido do SRTM em relevo acidentado. Resoluções citadas (SRTM ~30 m, ALOS PALSAR RTC ~12,5 m, fotogrametria por VANT 0,1–2 m, LiDAR sub-métrica) conferem com a documentação dos produtos, assim como a propriedade distintiva do LiDAR de revelar o terreno sob dossel vegetal. ✅
- Sequência de intensidade da erosão hídrica (laminar → sulcos → ravinas → voçorocas) e a distinção da voçoroca por atingir o nível freático, passando a ser alimentada por fluxo subsuperficial (Aula 02): confere com IPT (1986). ✅
- Cadeia conceitual suscetibilidade → perigo → risco, com suscetibilidade espacial e atemporal, perigo acrescentando probabilidade temporal e magnitude, e risco acrescentando exposição e vulnerabilidade (Aula 03): confere com Varnes (1984), Fell et al. (2008) e a terminologia da UNDRR. A formulação Risco = Perigo × Exposição × Vulnerabilidade e o corolário de que encosta suscetível e desocupada tem risco nulo são consequências diretas e corretas da definição. ✅
- Três famílias de método (heurística, estatística, determinística) e seus produtos e limitações (Aula 03): consistentes com Fell et al. (2008). A afirmação de que métodos estatísticos herdam o viés do inventário é bem estabelecida na literatura. ✅
- Modelo de talude infinito, FS = [c' + (γ·z·cos²β − u)·tan φ']/(γ·z·sen β·cos β), com u = γw·z·cos²β para fluxo paralelo à encosta e nível d'água na superfície (Aula 03): fórmula conferida contra Duncan, Wright & Brandon (2014) e consistente com Skempton & DeLory (1957). A restrição declarada (rupturas planares rasas paralelas à encosta, não rotacionais profundas) está corretamente registrada. ✅
- Exemplo trabalhado da Aula 03 recalculado (z = 2 m, γsat = 19 kN/m³, c' = 5 kPa, φ' = 30°, β = 25°, γw = 9,81 kN/m³): cos 25° = 0,90631, cos²25° = 0,82139, sen 25° = 0,42262. Força motriz = 38 × 0,42262 × 0,90631 = 14,555 kPa. Tensão normal total = 38 × 0,82139 = 31,213 kPa. **Caso seco:** resistência = 5 + 31,213 × 0,57735 = 5 + 18,021 = 23,021 kPa → FS = 1,5817 ≈ **1,58**. **Caso saturado:** u = 9,81 × 2 × 0,82139 = 16,116 kPa; σ'n = 15,097 kPa; resistência = 5 + 8,717 = 13,717 kPa → FS = 0,9424 ≈ **0,94**. Ambos conferem. A variante citada na interpretação (c' = 0 no caso saturado) também confere: FS = 8,717/14,555 = 0,599 ≈ 0,60. ✅
- Conversão de suscetibilidade em perigo por acoplamento a modelo hidrológico que simule a resposta da poropressão à chuva (Aula 03): consistente com Fell et al. (2008). ✅
- Graus de risco R1 (baixo), R2 (médio), R3 (alto) e R4 (muito alto), avaliados por setor e por moradia em vistoria de campo (Aula 03): conferem com a metodologia do Ministério das Cidades/IPT (2007). ✅
- Distinção entre curva de sucesso (mesmo inventário do ajuste) e curva de predição (inventário independente), e AUC = 0,5 como equivalente ao acaso (Aula 03): confere com Chung & Fabbri (2003). Ver achado ⚪ quanto ao limiar de 0,8. ✅
- Modelos de dados vetorial e matricial, vocação de cada um, e a álgebra de mapas como operação célula a célula (Aula 04): conferem com Burrough, McDonnell & Lloyd (2015) e Tomlin (1990). A afirmação de que reamostrar para célula menor não cria informação nem altera a escala de origem é correta e importante. ✅
- SIRGAS 2000 como sistema de referência geodésico oficial do Brasil, com adoção obrigatória a partir de 2015, e a necessidade de transformação de datum (e não mera reprojeção de rótulo) para bases em Córrego Alegre e SAD-69 (Aula 04): confere com os atos normativos do IBGE. ✅
- Padrão de Exatidão Cartográfica instituído pelo Decreto nº 89.817/1984 e sua extensão aos produtos digitais (PEC-PCD) pela especificação técnica de controle de qualidade de dados geoespaciais da Diretoria de Serviço Geográfico (Aula 04): confere. ✅
- Caráter compensatório da soma ponderada e a recomendação de aplicar fatores eliminatórios como regra de veto após a agregação (Aula 04): metodologicamente correto e consistente com Burrough, McDonnell & Lloyd (2015). ✅
- Exemplo trabalhado da Aula 04 recalculado: Célula A = (0,50×5) + (0,30×2) + (0,20×2) = 2,50 + 0,60 + 0,40 = 3,50. Célula B = (0,50×3) + (0,30×4) + (0,20×4) = 1,50 + 1,20 + 0,80 = 3,50. Pesos somam 1,00. Índices idênticos, confirmando a demonstração de compensação. Confere. ✅
- Interferometria SAR por espalhadores persistentes medindo deslocamento milimétrico a centimétrico ao longo do tempo, restrita à componente na linha de visada e sujeita a perda de coerência em vegetação densa e movimento rápido (Aula 04): confere com Ferretti, Prati & Rocca (2001). ✅
- Quatro alavancas de redução de risco derivadas da própria formulação Risco = Perigo × Exposição × Vulnerabilidade (Aula 04): dedução correta a partir da definição e consistente com Fell et al. (2008) e a doutrina de gestão de risco de desastres. ✅
- Limiares pluviométricos de intensidade e duração como base de alerta antecipado (Aula 04): confere com Guzzetti et al. (2008). A atribuição da função de monitoramento e alerta no Brasil ao Cemaden, instituído em 2011, confere com a documentação institucional. ✅
- Três fontes de incerteza (posicional, temática e de modelo), com predomínio usual da de modelo, e a análise de sensibilidade como prática mínima (Aula 04): consistente com Burrough, McDonnell & Lloyd (2015) e Fell et al. (2008). ✅

## Cobertura de objetivos de aprendizagem

| Objetivo | Aulas que cobrem | Verificado |
|---|---|---|
| geologia-avancado-m07-oa01 | a03 | ✅ |
| geologia-avancado-m07-oa02 | a01 | ✅ |
| geologia-avancado-m07-oa03 | a02, a03 | ✅ |
| geologia-avancado-m07-oa04 | a04 | ✅ |

Todos os quatro objetivos de aprendizagem do módulo têm pelo menos uma aula dedicada e alegações auditáveis correspondentes; nenhum objetivo ficou sem cobertura.

## Nota de consistência com módulos anteriores

Verificada a coerência das retomadas do Módulo 06 e do Módulo 05 feitas neste módulo, para evitar contradição entre módulos:
- O modelo de talude infinito da Aula 03 usa c', φ' e o efeito da poropressão sobre σ'n exatamente como definidos no Módulo 06, Aulas 03 e 06 — inclusive reproduzindo, no comentário sobre a sensibilidade a c', a mesma advertência sobre o intercepto de coesão como parâmetro de extrapolação registrada no achado 🔵 da auditoria do Módulo 06. Sem contradição.
- A escala de alteração W1–W6 da Aula 02 é a mesma da ISRM adotada no Módulo 05. Sem contradição.
- A menção a sísmica de refração e eletrorresistividade como complemento à sondagem para topo rochoso (Aula 02) reproduz corretamente o princípio estabelecido no Módulo 06, Aula 06 (geofísica calibra-se com sondagem, não a substitui). Sem contradição.

## Recomendação

Aprovar o módulo para avaliação (questionários) e memorização (flashcards). Nenhum achado vermelho ou laranja, e portanto nenhuma pendência bloqueante. O achado 🟡 sobre volatilidade da legislação já está tratado no texto por callout dedicado e deve ser reavaliado em futuras revisões do curso; recomenda-se registrá-lo como ponto de manutenção periódica, já que é o tipo de conteúdo que envelhece sem sinalização. O achado 🔵 e os dois ⚪ não exigem alteração.
