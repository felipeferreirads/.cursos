# Auditoria científica — Módulo 05: Mecânica de rochas

**Módulo:** [[05-mecanica-de-rochas-modulo|Módulo 05 — Mecânica de rochas]]
**Escopo:** 7 aulas (geologia-avancado-m05-a01 a a07), 27 alegações auditáveis extraídas dos blocos de metadados de cada aula.
**Método:** verificação de cada `claim_id` contra a literatura padrão de mecânica das rochas (Jaeger, Cook & Zimmerman, 2007; Goodman, 1989; Hoek & Bray, 1981; Hoek, Kaiser & Bawden, 1995; Bieniawski, 1989) e as fontes primárias citadas (Griffith 1921; Hoek & Brown 1980; Hoek, Carranza-Torres & Corkum 2002; Barton 1973; Barton & Choubey 1977; Barton, Lien & Lunde 1974; Romana 1985; Patton 1966; Kirsch 1898; Deere 1964; Haimson & Cornet 2003; Goodman & Bray 1976), com recálculo independente de todos os exemplos numéricos trabalhados e verificação cruzada das fórmulas contra o texto original das publicações de referência sempre que a fórmula tem forma fechada citável.
**Data:** 2026-08-26

## Resumo do veredito

| Severidade | Contagem |
|---|---|
| 🔴 Erro | 0 |
| 🟠 Impreciso | 0 |
| 🟡 Desatualizado/a matizar | 0 |
| 🔵 Controverso (área com debate legítimo) | 1 |
| ⚪ Sem fonte direta verificável (mas plausível/consensual) | 2 |

**Veredito geral: aprovado.** Nenhum achado vermelho, laranja ou amarelo. O achado 🔵 registra uma área de debate técnico real (o papel de σ2 nos critérios de ruptura), já tratada corretamente no texto como um ponto historicamente controverso, e não como um fato assentado. Os dois achados ⚪ são de baixo impacto e não exigem correção de conteúdo.

## Achados

### 🔵 [MECROCHA-M05-A01-SIGMA2-001] — O papel de σ2 nos critérios de ruptura
**Aula:** 01 (mencionado também na Aula 03). **Claim relacionado:** "a tensão cisalhante máxima absoluta em qualquer plano é sempre (σ1−σ3)/2, independente de σ2... embora [σ2] tenha um papel debatido nos critérios de ruptura."
**Achado:** a afirmação sobre τmáx = (σ1−σ3)/2 independente de σ2 é matematicamente exata e não controversa. O texto já sinaliza corretamente, entre parênteses, que o papel de σ2 *na resistência* (não na tensão cisalhante máxima) é "debatido" — e de fato é: os critérios de Mohr-Coulomb e de Hoek-Brown, como apresentados no módulo, ignoram σ2 (tratam a ruptura como função exclusiva de σ1 e σ3), o que é uma simplificação amplamente usada na prática de engenharia, mas critérios alternativos (Drucker-Prager, Mogi-Coulomb, e evidências experimentais de ensaios poliaxiais verdadeiros) mostram que σ2 tem influência mensurável na resistência real de muitas rochas — um debate ativo na literatura de mecânica das rochas, não encerrado.
**Correção proposta:** nenhuma. O texto já trata o tema com a cautela apropriada, sem afirmar que σ2 é irrelevante para a resistência, apenas que não afeta τmáx.
**Confiança:** alta.

### ⚪ [MECROCHA-M05-A06-STANDUP-002] — Faixas de tempo de autossustentação (stand-up time) por classe de RMR
**Aula:** 06. **Claim:** "cada [classe RMR] associada, nas tabelas originais de Bieniawski, a uma faixa orientativa de tempo de autossustentação (stand-up time) e a recomendações preliminares de suporte para túneis."
**Achado:** a existência de tabelas de stand-up time associadas às classes de RMR em função do vão é bem documentada em Bieniawski (1989) e amplamente reproduzida na literatura subsequente. O texto da aula não cita valores numéricos específicos de tempo (dias, semanas) como se fossem universais — usa a expressão explicitamente qualificada "faixa orientativa" e, no exemplo trabalhado, "da ordem de dias a poucas semanas" para um caso específico de RMR 60 em vão moderado, o que é consistente com a ordem de grandeza das tabelas publicadas, mas não é uma citação literal de um valor tabelado único (que varia com o vão da escavação, não citado explicitamente no exemplo). Achado de baixo impacto: a linguagem qualitativa do texto já evita a armadilha de apresentar um número tabelado fora de contexto sem especificar o vão correspondente.
**Correção proposta:** nenhuma obrigatória. Poderia, como refinamento futuro, explicitar o vão assumido no exemplo trabalhado da Aula 06 para tornar a referência ao stand-up time totalmente auto-contida.
**Confiança:** média-alta.

### ⚪ [MECROCHA-M05-A02-ISLINDEX-003] — Fator de conversão entre Is50 e UCS
**Aula:** 02. **Claim:** "o índice obtido (Is50...) correlaciona-se empiricamente com a UCS (aproximadamente UCS ≈ 20 a 25 × Is50, variando por litologia)".
**Achado:** a faixa de 20–25 é a mais citada na literatura de referência (ISRM 1985; diversos manuais de geotecnia), mas alguns autores relatam fatores de conversão fora dessa faixa (de 10 a mais de 30) para litologias específicas ou para tamanhos de amostra fora da faixa recomendada — o próprio texto já qualifica a faixa como variável por litologia, tratando-a corretamente como uma aproximação de ordem de grandeza, não como uma constante universal.
**Correção proposta:** nenhuma. O texto já trata o fator como aproximado e dependente de litologia, e recomenda explicitamente calibração local nos "erros comuns".
**Confiança:** alta.

## Verificação amostral de fórmulas e cálculos (checklist)

- Centro e raio do círculo de Mohr 2D (C=(σx+σy)/2, R=√[((σx−σy)/2)²+τxy²]) e regra do ângulo duplo (Aula 01): consistente com Jaeger, Cook & Zimmerman (2007, cap. 2). Exemplo recalculado (σx=40, σy=15, τxy=10): C=27,5 MPa, R≈16,0 MPa, σ1≈43,5 MPa, σ3≈11,5 MPa, θp≈19,3°. Confere. ✅
- Construção do diagrama de Mohr 3D com três círculos tangentes em σ1, σ2, σ3 e τmáx=(σ1−σ3)/2 (Aula 01): consistente com Jaeger, Cook & Zimmerman (2007, cap. 3). ✅
- Fases da curva tensão-deformação até a ruptura, incluindo dilatância pré-pico (Aula 02): consistente com Bieniawski (1967) e Goodman (1989, cap. 3). ✅
- Critério de Mohr-Coulomb linear e sua tendência a superestimar resistência em altos confinamentos por rochas terem envelope real côncavo (Aula 03): consistente com Jaeger, Cook & Zimmerman (2007, cap. 4). ✅
- Critério de Griffith 2D, (σ1−σ3)²=8σt(σ1+σ3), e razão teórica compressão/tração=8 (Aula 03): consistente com a dedução original de Griffith (1921), reproduzida em Jaeger, Cook & Zimmerman (2007, cap. 4); a observação de que rochas reais tipicamente excedem essa razão é consistente com dados experimentais amplamente reportados na literatura. ✅
- Critério de Hoek-Brown original (1980) para rocha intacta e generalizado (2002) para maciço, com fórmulas de mb, s, a em função de GSI, mi e D (Aula 03 e Aula 06): fórmulas conferidas contra Hoek, Carranza-Torres & Corkum (2002) — correspondem exatamente às equações publicadas. Exemplo trabalhado da Aula 03 (σci=100 MPa, mi=15, σ3=5 MPa) recalculado: σ1≈137,3 MPa. Confere. ✅
- Parâmetros geométricos padronizados de descontinuidades segundo ISRM (1978) (Aula 04): consistente com o documento original da ISRM. ✅
- Critério de Barton-Bandis, τ=σn·tan[φb+JRC·log10(JCS/σn)] (Aula 04): consistente com Barton & Choubey (1977). Exemplo trabalhado (JRC=12, JCS=80 MPa, φb=30°, σn=0,2 e 4 MPa) recalculado: ângulos efetivos ≈61,2° e ≈45,6° respectivamente. Confere. ✅
- Lei cúbica de fluxo em fratura plana (Q∝e³) (Aula 04): consistente com a solução clássica de fluxo laminar entre placas paralelas, citada em Goodman (1989, cap. 6). ✅
- Gradiente de tensão vertical gravitacional (σv≈0,027 MPa/m para densidade ~2.700 kg/m³) e razão K0=ν/(1−ν) sob deformação lateral nula (Aula 05): consistente com Jaeger, Cook & Zimmerman (2007, cap. 11). Exemplo trabalhado (z=500 m, ρ=2.650 kg/m³, Ps=9,5 MPa, ν=0,22) recalculado: σv≈13,0 MPa, K≈0,73, K0 previsto≈0,28. Confere. ✅
- Princípios de overcoring, fraturamento hidráulico (pressões de ruptura, fechamento, reabertura) e macacos planos (Aula 05): consistente com Amadei & Stephansson (1997) e Haimson & Cornet (2003, métodos sugeridos ISRM). ✅
- Componentes e pesos do RMR (Bieniawski 1989) e definição de RQD (Deere 1964) (Aula 06): consistentes com as publicações originais. Exemplo trabalhado (soma=60, Classe III) recalculado e confere com as faixas de classe publicadas (Classe III: RMR 41–60, "regular"/"fair rock"). ✅
- Fórmula do sistema Q (Barton, Lien & Lunde 1974) e uso do ábaco De×ESR para suporte (Aula 06): consistente com a publicação original. ✅
- Ábaco de GSI (estrutura × condição de superfície) e fórmulas de conversão para mb, s, a (Aula 06): consistente com Hoek (1994) e Hoek, Carranza-Torres & Corkum (2002). ✅
- Fórmula do SMR (Romana 1985) e definição dos fatores F1–F4 (Aula 06): consistente com a publicação original. ✅
- Condições cinemáticas para ruptura planar, em cunha e tombamento (Aula 07): consistente com Hoek & Bray (1981, cap. 5–9). ✅
- Fórmula de fator de segurança para ruptura planar com água em trinca de tração (Aula 07): consistente com Hoek & Bray (1981, cap. 6). Exemplo trabalhado (W=4.500 kN, ψp=35°, A=180 m², c=20 kPa, φ=32°, sem água) recalculado: N≈3.686 kN, T≈2.581 kN, força resistente≈5.904 kN, FS≈2,29. Confere. ✅
- Equações de Kirsch para concentração de tensão tangencial ao redor de abertura circular (teto/piso: 3σh−σv=(3K−1)σv; paredes: 3σv−σh=(3−K)σv) (Aula 07): recálculo por superposição de duas soluções uniaxiais de Kirsch confirma σθ=σv[(1+K)±2(1−K)], com o sinal "+" nas paredes (alinhadas com a direção de σv) e "−" no teto/piso (alinhado com a direção de σh) — consistente com Kirsch (1898), reproduzido em Jaeger, Cook & Zimmerman (2007, cap. 5). Uma primeira redação da Aula 07 havia atribuído as duas expressões trocadas entre teto/piso e paredes; o recálculo independente desta auditoria identificou a inversão, e o texto da aula, o recap e o bloco de metadados foram corrigidos antes da publicação do módulo. ✅ (corrigido)
- Método de convergência-confinamento e papel do momento de instalação do suporte (Aula 07): consistente com Hoek, Kaiser & Bawden (1995, cap. 8). ✅

## Cobertura de objetivos de aprendizagem

| Objetivo | Aulas que cobrem | Verificado |
|---|---|---|
| geologia-avancado-m05-oa01 | a01, a02 | ✅ |
| geologia-avancado-m05-oa02 | a03, a05 | ✅ |
| geologia-avancado-m05-oa03 | a04, a06 | ✅ |
| geologia-avancado-m05-oa04 | a07 | ✅ |

Todos os quatro objetivos de aprendizagem do módulo têm pelo menos uma aula dedicada e claims auditáveis correspondentes; nenhum objetivo ficou sem cobertura.

## Recomendação

Nenhuma correção obrigatória de conteúdo. Aprovar o módulo para avaliação (questionários) e memorização (flashcards). O achado 🔵 fica registrado como referência de uma área de debate técnico legítimo (papel de σ2 na resistência da rocha), já tratada com a cautela adequada no texto; os dois achados ⚪ são aproximações de ordem de grandeza já qualificadas como tal, sem exigir alteração.
