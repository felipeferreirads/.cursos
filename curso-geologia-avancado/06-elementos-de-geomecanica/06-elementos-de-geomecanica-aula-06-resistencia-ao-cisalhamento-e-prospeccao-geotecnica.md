# Aula 06: Resistência ao cisalhamento de solos e rochas e prospecção geotécnica do subsolo

**ID:** geologia-avancado-m06-a06
**Módulo:** [[06-elementos-de-geomecanica-modulo|Módulo 06 — Elementos de geomecânica]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** determinar os parâmetros de resistência ao cisalhamento de um solo (c', φ', su) a partir de ensaios de laboratório, escolher entre análise em tensões totais e efetivas conforme a condição de drenagem do problema, e selecionar os métodos de prospecção geotécnica — sondagens, ensaios in situ e geofísica — adequados a uma campanha de investigação.

**Pré-requisito:** Aula 03 deste módulo (tensão efetiva); Aula 05 (histórico de tensões, OCR); critério de Mohr-Coulomb e envoltória de ruptura, do Módulo 05, Aula 03; classificações geomecânicas, do Módulo 05, Aula 06.

## Antes de começar, você precisa saber

- O critério de Mohr-Coulomb na forma τ = c + σ·tan φ e a construção da envoltória de ruptura tangente aos círculos de Mohr (Módulo 05, Aula 03).
- Que só a **tensão efetiva** governa a resistência ao cisalhamento (Aula 03).
- Que solos sobreadensados (OCR > 1) já suportaram tensões maiores do que suportam hoje (Aula 05).

## Conteúdo

### Mohr-Coulomb em tensões efetivas

O Módulo 05 apresentou o critério de Mohr-Coulomb para rocha intacta. Em solos, ele é o mesmo critério, escrito obrigatoriamente em **tensões efetivas**:

**τf = c' + σ'n · tan φ'**

onde c' é o **intercepto de coesão efetiva** e φ' o **ângulo de atrito efetivo**. A mudança de notação não é cosmética: escrever a envoltória em tensões totais só é legítimo em situações específicas, tratadas adiante.

Fisicamente, φ' representa a resistência friccional mobilizada no contato entre grãos, e depende sobretudo do **entrosamento** (angulosidade, graduação, compacidade) — não da mineralogia isoladamente. Já c' representa qualquer parcela de resistência **independente** da tensão normal: cimentação verdadeira, ligações diagenéticas, atração eletroquímica entre partículas argilosas. Areias limpas têm c' ≈ 0 (a envoltória passa pela origem); argilas sobreadensadas exibem c' > 0.

> [!warning] c' é um parâmetro de ajuste, não uma propriedade física medida
> O intercepto c' é o resultado de extrapolar uma reta ajustada a pontos experimentais até σ'n = 0 — uma região onde frequentemente **não há ponto experimental algum**. Adotar um c' obtido em ensaios a 200–600 kPa para analisar um talude raso, onde σ'n é de poucas dezenas de kPa, superestima a resistência disponível exatamente onde ela mais importa. O mesmo alerta feito no Módulo 05 para o par (c, φ) em rocha vale aqui, e com consequências mais frequentes.

### Drenado e não drenado: a distinção que organiza tudo

Carregar um solo saturado gera excesso de poropressão (Aula 05). O que acontece com esse excesso durante o cisalhamento define duas condições-limite:

- **Condição drenada:** o carregamento é lento o bastante (ou o solo permeável o bastante) para que o excesso de poropressão dissipe conforme se forma. Δu ≈ 0, σ' é conhecida, e a análise usa **c' e φ'**. É a condição típica de areias sob qualquer carregamento estático, e de argilas no **longo prazo**.
- **Condição não drenada:** o carregamento é rápido demais para haver drenagem. Δu ≠ 0 e não é conhecido a priori, de modo que σ' também não é. A análise usa então a **resistência não drenada su** (também escrita cu), com a envoltória em tensões **totais** aparecendo horizontal (φu = 0). É a condição de argilas no **curto prazo** — fim de construção, carregamento sísmico, escavação rápida.

A escolha entre as duas não é uma preferência de método: é ditada pela relação entre a velocidade do carregamento e a condutividade hidráulica do solo (Aula 04).

> [!important] Qual condição é crítica depende do sinal do carregamento
> Para um **aterro sobre argila mole** (carregamento), o pior momento é o **fim da construção**: a poropressão está no máximo, σ' no mínimo, e a resistência disponível é a menor de toda a vida da obra — depois o adensamento aumenta σ' e a obra fica mais segura com o tempo. Para uma **escavação ou corte** (descarregamento), ocorre o oposto: o alívio gera poropressões **negativas** que dão estabilidade temporária, e à medida que elas se equilibram com o tempo σ' cai e a resistência diminui — o pior momento é o **longo prazo**. Muitos taludes de corte rompem anos após executados por exatamente essa razão.

### Ensaios de resistência em laboratório

- **Cisalhamento direto** (ASTM D3080): a amostra é forçada a romper num plano horizontal predefinido. Simples e barato, mas impõe o plano de ruptura em vez de deixá-lo se formar, e não permite controlar nem medir poropressão — é usado essencialmente em condições drenadas, com velocidade lenta.
- **Ensaio triaxial** (ASTM D4767 e correlatos): o corpo de prova cilíndrico é confinado por pressão de câmara e carregado axialmente, com controle de drenagem e medição de poropressão. É o ensaio de referência, em três modalidades:
  - **UU** (não adensado, não drenado): fornece su diretamente, para análise de curto prazo.
  - **CU** (adensado, não drenado, com medição de u): fornece c' e φ' **e** su, sendo o mais informativo por corpo de prova ensaiado.
  - **CD** (adensado, drenado): fornece c' e φ' diretamente, sem necessidade de medir u, mas é lento — dias a semanas em argilas.
- **Ensaio de compressão simples** (ASTM D2166): fornece a resistência à compressão não confinada qu de argilas, com su = qu/2. Rápido e barato, mas exige amostra indeformada coesiva e sem fissuras.
- **Ensaio de palheta (*vane*) de laboratório e de campo** (ASTM D2573): mede su in situ em argilas moles por torque, sem necessidade de amostragem — a referência prática para argilas muito moles, onde extrair amostra indeformada é inviável.

### Resistência de pico, residual e estado crítico

A curva tensão-deformação de um solo cisalhado não tem um valor único de resistência:

- Solos **densos ou sobreadensados** exibem um **pico** pronunciado, seguido de queda até um patamar. O pico decorre do **entrosamento**: para cisalhar, os grãos precisam subir uns sobre os outros, e essa **dilatância** (aumento de volume durante o cisalhamento) consome energia adicional. Superado o pico, o entrosamento é desfeito e a resistência cai.
- Solos **fofos ou normalmente adensados** não têm pico: a resistência cresce monotonicamente até um patamar, com redução de volume (contração) durante o cisalhamento.
- Ambos convergem para o mesmo patamar — o **estado crítico**, em que o solo continua a se deformar sob tensão e volume constantes, com ângulo de atrito φ'cv, independente do estado inicial de compacidade.
- Em argilas, deformações muito grandes reorientam as partículas lamelares paralelamente ao plano de ruptura, baixando a resistência ainda mais, até a **resistência residual** (φ'r), que pode ser bem inferior a φ'cv. É a resistência que governa **superfícies de ruptura preexistentes** — escorregamentos reativados, planos de falha antigos — e a razão pela qual usar parâmetros de pico na análise de um escorregamento reativado é gravemente inseguro.

O paralelo com o Módulo 05 é direto: assim como a resistência de uma descontinuidade rochosa converge para φb quando as asperezas são cisalhadas (Barton-Bandis), a resistência de um solo converge para o estado crítico quando o entrosamento é desfeito. O mecanismo — geometria de contato consumida pela deformação — é o mesmo em ambas as escalas.

### Prospecção geotécnica do subsolo

Nenhum dos parâmetros acima existe sem investigação. A campanha se organiza em três famílias, complementares e não substituíveis entre si:

**1. Sondagens e amostragem**
- **SPT (*Standard Penetration Test*):** o método mais difundido no Brasil. Um amostrador padrão é cravado por um martelo em queda livre, e conta-se o número de golpes para os 30 cm finais de penetração — o índice **N (NSPT)**. As duas normas de referência especificam martelos ligeiramente diferentes: a **NBR 6484** adota massa de 65 kg com altura de queda de 75 cm, enquanto a **ASTM D1586** adota 63,5 kg (140 lb) com queda de 76 cm (30 in) — diferença pequena, mas suficiente para que valores de N não sejam rigorosamente intercambiáveis entre normas sem a correção de energia discutida adiante. Fornece perfil estratigráfico, amostras deformadas, posição do nível d'água e correlações empíricas com compacidade de areias e consistência de argilas. Barato e universalmente disponível.
- **Sondagem rotativa:** perfuração com coroa diamantada e recuperação de testemunho contínuo em rocha, base para o cálculo de RQD e para as classificações do Módulo 05, Aula 06.
- **Amostragem indeformada** com amostrador de parede fina (**Shelby**, ASTM D1587), indispensável para ensaios de adensamento (Aula 05) e triaxiais — nenhum ensaio de deformabilidade ou resistência de argila tem valor sobre amostra deformada.

**2. Ensaios in situ**
- **CPT/CPTu (*cone penetration test*, com medição de poropressão):** crava-se um cone instrumentado a velocidade constante, registrando resistência de ponta (qc), atrito lateral (fs) e poropressão (u2) de forma **contínua** com a profundidade. Muito superior ao SPT em resolução estratigráfica e em repetibilidade, e a ferramenta de escolha para detectar lentes e camadas delgadas que o SPT, medindo a cada metro, simplesmente não vê.
- **Ensaio de palheta (*vane*)**, para su em argilas moles; **pressiômetro** e **dilatômetro (DMT)**, para deformabilidade in situ; **ensaio Lugeon**, para permeabilidade de maciço (Aula 04).

**3. Geofísica**
- **Sísmica de refração** e **MASW**: perfis de velocidade de onda P e S, úteis para localizar o topo rochoso e estimar módulos dinâmicos de forma não invasiva.
- **Eletrorresistividade (ERT)** e **GPR**: mapeamento contínuo de contrastes de resistividade e de interfaces rasas, úteis para localizar cavidades, contatos e o nível d'água.

> [!important] Geofísica não substitui sondagem — calibra-se com ela
> Métodos geofísicos entregam **cobertura contínua** de uma propriedade indireta (velocidade, resistividade) e são a forma econômica de interpolar entre furos. Sondagens entregam **verdade pontual**: estratigrafia observada e amostra física para ensaio. Uma campanha bem projetada usa geofísica para estender lateralmente o que as sondagens estabeleceram pontualmente. Interpretar uma seção geofísica sem nenhum furo de calibração é adivinhação com aparência técnica.

O **planejamento** da campanha — número, locação e profundidade das investigações — segue diretrizes normativas (no Brasil, a NBR 8036 para programação de sondagens de simples reconhecimento em edificações) e um princípio geral: investigar até uma profundidade onde o acréscimo de tensão imposto pela obra se torne pequeno frente à tensão geostática existente (usualmente onde Δσ cai abaixo de ~10% de σ'v0), porque abaixo disso a obra praticamente não altera o estado do terreno.

## Exemplo trabalhado

**Situação:** dois ensaios triaxiais CD sobre corpos de prova da mesma argila sobreadensada romperam nas seguintes condições:
- Corpo de prova 1: σ'3 = 100 kPa, σ'1 = 350 kPa
- Corpo de prova 2: σ'3 = 200 kPa, σ'1 = 600 kPa

Determine c' e φ'.

**Resolução:**

A forma da envoltória de Mohr-Coulomb em tensões principais é:

σ'1 = σ'3·Nφ + 2c'·√Nφ,  com Nφ = tan²(45° + φ'/2)

Montando as duas equações (chamando o segundo termo de K = 2c'·√Nφ):

350 = 100·Nφ + K
600 = 200·Nφ + K

Subtraindo a primeira da segunda:
250 = 100·Nφ → **Nφ = 2,50**

Substituindo na primeira:
K = 350 − (100 × 2,50) = 350 − 250 = **100 kPa**

**Ângulo de atrito efetivo:**
tan(45° + φ'/2) = √2,50 = 1,5811
45° + φ'/2 = arctan(1,5811) = 57,69°
φ'/2 = 12,69° → **φ' ≈ 25,4°**

**Coesão efetiva:**
K = 2c'·√Nφ → 100 = 2c' × 1,5811 → c' = 100/3,1623 → **c' ≈ 31,6 kPa**

**Interpretação:** o intercepto de coesão de 31,6 kPa é coerente com uma argila sobreadensada — mas note onde ele foi obtido: os dois ensaios cobrem a faixa de 100 a 200 kPa de confinamento, e o valor de c' resulta de extrapolar a envoltória até σ'n = 0, a mais de 100 kPa do ponto experimental mais próximo. Se esse mesmo solo aflorasse num talude raso, com σ'n da ordem de 20 kPa, adotar c' = 31,6 kPa atribuiria a ele uma resistência majoritariamente proveniente de um parâmetro que nenhum ensaio verificou naquela faixa. A prática correta é ensaiar na faixa de tensões da obra — e, em taludes rasos, é comum adotar c' reduzido ou nulo por segurança. Note ainda que φ' ≈ 25° é um valor de **pico**: se a análise for de um escorregamento reativado sobre superfície preexistente, o parâmetro pertinente seria a resistência residual φ'r, possivelmente bem inferior.

## Erros comuns

- **Misturar parâmetros efetivos com análise em tensões totais** (usar c' e φ' num problema de curto prazo em argila, ou su num problema drenado de longo prazo). O par de parâmetros e a condição de drenagem precisam ser coerentes entre si.
- **Extrapolar c' para fora da faixa de tensões ensaiada**, sobretudo para taludes rasos.
- **Usar resistência de pico em superfície de ruptura preexistente**, onde vale a residual — erro clássico na análise de escorregamentos reativados.
- **Aplicar correlações de NSPT sem correção** de energia (N60) e de tensão de confinamento (N1,60). O SPT bruto varia com o equipamento e o operador, e correlações publicadas pressupõem valores corrigidos.
- **Ensaiar adensamento ou triaxial sobre amostra deformada** (obtida no amostrador do SPT em vez de Shelby) — os parâmetros de deformabilidade e resistência de pico ficam sem significado.
- **Interpretar seção geofísica sem furo de calibração**, tratando um contraste de resistividade ou de velocidade como se fosse estratigrafia observada.

## O que não concluir

- **Que su é uma propriedade do solo.** A resistência não drenada depende do estado de tensões efetivas vigente antes do cisalhamento e da trajetória de tensões imposta — o mesmo solo tem su diferente em compressão triaxial, extensão e cisalhamento simples, e su cresce à medida que o depósito adensa sob nova carga.
- **Que ângulo de atrito alto garante estabilidade.** A resistência mobilizável depende de σ'n, que depende de u (Aula 03). Um φ' de 35° com poropressão elevada pode oferecer menos resistência efetiva que um φ' de 28° em terreno drenado.
- **Que mais furos é sempre melhor investigação.** Uma campanha eficaz distribui esforço entre estratigrafia (sondagens), parâmetros (amostragem indeformada e ensaios) e continuidade lateral (geofísica). Vinte furos sem uma única amostra indeformada não permitem calcular um recalque.

## Recap relâmpago

- Em solos, Mohr-Coulomb escreve-se em tensões efetivas: τf = c' + σ'n·tan φ'. φ' vem do entrosamento entre grãos; c' é um **intercepto de extrapolação**, perigoso fora da faixa de tensões ensaiada.
- **Drenado** (Δu ≈ 0, usa c' e φ') e **não drenado** (Δu ≠ 0, usa su com φu = 0) são condições ditadas pela razão entre velocidade de carregamento e condutividade hidráulica. Em aterro sobre argila o crítico é o **curto prazo**; em escavação, o **longo prazo**.
- Ensaios: cisalhamento direto (simples, plano imposto), triaxial UU/CU/CD (referência; CU é o mais informativo), compressão simples (su = qu/2) e palheta (su in situ em argila mole).
- Solos densos/sobreadensados têm **pico** por dilatância e caem para o **estado crítico** (φ'cv); argilas com grandes deformações caem ainda mais, até a **resistência residual** (φ'r), que governa superfícies de ruptura preexistentes.
- Prospecção em três famílias: **sondagens e amostragem** (SPT, rotativa, Shelby indeformada), **ensaios in situ** (CPT/CPTu contínuo, palheta, pressiômetro, dilatômetro, Lugeon) e **geofísica** (refração, MASW, ERT, GPR).
- Geofísica dá cobertura contínua de propriedade indireta e **calibra-se com sondagem**, que dá verdade pontual e amostra física — uma não substitui a outra.

## Próxima aula

Este é o fim do Módulo 06. Continue em [[07-mapeamento-geotecnico/07-mapeamento-geotecnico-modulo|Módulo 07 — Metodologia de mapeamento geotécnico]], que aplica a caracterização geotécnica aqui construída à escala do território.

## Anterior

[[06-elementos-de-geomecanica-aula-05-compressibilidade-adensamento-recalques|Aula 05 — Compressibilidade e adensamento]]

## Fontes

- Resistência ao cisalhamento, ensaios e parâmetros: Das, B. M. (2019), *Fundamentos de Engenharia Geotécnica*, 9ª ed., Cengage, cap. 12; Terzaghi, K., Peck, R. B. & Mesri, G. (1996), *Soil Mechanics in Engineering Practice*, 3ª ed., Wiley, cap. 3 e 5.
- Estado crítico e resistência residual: Schofield, A. & Wroth, P. (1968), *Critical State Soil Mechanics*, McGraw-Hill; Skempton, A. W. (1964), "Long-term stability of clay slopes" (4ª Rankine Lecture), *Géotechnique*, 14(2), p. 77–102.
- Normas de ensaio de laboratório: ASTM D3080 (cisalhamento direto); ASTM D4767 (triaxial CU em solos coesivos); ASTM D2166 (compressão simples); ASTM D2573 (ensaio de palheta em campo).
- Prospecção e amostragem: ABNT NBR 6484 (*Solo — Sondagens de simples reconhecimento com SPT*); ASTM D1586 (SPT); ASTM D1587 (amostragem por tubo de parede fina); ABNT NBR 8036 (*Programação de sondagens de simples reconhecimento dos solos para fundações de edifícios*).
- Ensaio de cone e interpretação: Lunne, T., Robertson, P. K. & Powell, J. J. M. (1997), *Cone Penetration Testing in Geotechnical Practice*, Blackie Academic & Professional; Robertson, P. K. (1990), "Soil classification using the cone penetration test", *Canadian Geotechnical Journal*, 27(1), p. 151–158.

<!--
nivel: avancado
palavras_corpo: ~2250

mapa_objetivo_secao:
  geologia-avancado-m06-oa04: "Mohr-Coulomb em tensões efetivas" + "Drenado e não drenado: a distinção que organiza tudo" + "Ensaios de resistência em laboratório" + "Resistência de pico, residual e estado crítico" + "Prospecção geotécnica do subsolo" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOMEC-M06-A06-MC-001
    claim: "Em solos, o critério de Mohr-Coulomb escreve-se em tensões efetivas, τf=c'+σ'n·tan φ', e a relação em tensões principais é σ'1=σ'3·Nφ+2c'·√Nφ com Nφ=tan²(45°+φ'/2)."
    risk: fato
    source: "Das 2019, cap. 12; Terzaghi, Peck & Mesri 1996, cap. 3"
  - claim_id: GEOMEC-M06-A06-DRENAGEM-002
    claim: "A condição drenada (Δu≈0) usa c' e φ'; a não drenada usa su com envoltória horizontal em tensões totais (φu=0). Para aterro sobre argila mole o crítico é o curto prazo; para escavação/corte, o longo prazo."
    risk: fato
    source: "Terzaghi, Peck & Mesri 1996, cap. 3 e 5; Das 2019, cap. 12"
  - claim_id: GEOMEC-M06-A06-ENSAIOS-003
    claim: "Triaxial UU fornece su; CU fornece c', φ' e su com medição de poropressão; CD fornece c' e φ' diretamente. Na compressão simples, su=qu/2."
    risk: fato
    source: "ASTM D4767; ASTM D2166; Das 2019, cap. 12"
  - claim_id: GEOMEC-M06-A06-CRITICO-004
    claim: "Solos densos/sobreadensados exibem pico por dilatância e convergem ao estado crítico (φ'cv); argilas sob grandes deformações atingem resistência residual φ'r, menor que φ'cv, que governa superfícies de ruptura preexistentes."
    risk: fato
    source: "Schofield & Wroth 1968; Skempton 1964"
  - claim_id: GEOMEC-M06-A06-SPT-005
    claim: "O SPT conta os golpes para os 30 cm finais de penetração, gerando o índice N. A NBR 6484 especifica martelo de 65 kg com queda de 75 cm; a ASTM D1586 especifica 63,5 kg (140 lb) com queda de 76 cm (30 in). Correlações exigem correção de energia (N60) e de confinamento (N1,60)."
    risk: fato
    source: "ABNT NBR 6484; ASTM D1586"
  - claim_id: GEOMEC-M06-A06-CPT-006
    claim: "O CPT/CPTu registra resistência de ponta (qc), atrito lateral (fs) e poropressão (u2) de forma contínua com a profundidade, oferecendo resolução estratigráfica e repetibilidade superiores às do SPT."
    risk: fato
    source: "Lunne, Robertson & Powell 1997; Robertson 1990"
  - claim_id: GEOMEC-M06-A06-PROFUND-007
    claim: "A profundidade de investigação é usualmente levada até onde o acréscimo de tensão da obra cai abaixo de cerca de 10% da tensão geostática efetiva existente; no Brasil a programação de sondagens em edificações segue a NBR 8036."
    risk: fato
    source: "ABNT NBR 8036; Das 2019, cap. 18"
-->
