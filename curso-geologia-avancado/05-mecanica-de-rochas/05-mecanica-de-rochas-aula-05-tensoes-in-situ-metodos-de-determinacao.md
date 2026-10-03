# Aula 05: Tensões in situ: origem e métodos de determinação (overcoring, fraturamento hidráulico, macacos planos)

**ID:** geologia-avancado-m05-a05
**Módulo:** [[05-mecanica-de-rochas-modulo|Módulo 05 — Mecânica de rochas]]
**Duração estimada:** ~28 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** explicar a origem gravitacional e tectônica das tensões naturais num maciço rochoso e descrever os princípios dos três métodos de campo mais usados para medi-las: overcoring, fraturamento hidráulico e macacos planos.
**Pré-requisito:** tensões principais e círculo de Mohr (Aula 01); critérios de ruptura, cujo uso em projeto real depende de conhecer o estado de tensão de fundo antes de qualquer escavação (Aula 03).

## Antes de começar, você precisa saber

- Tensão principal, tensor de tensões e a convenção de compressão positiva (Aula 01).
- Que a rocha responde elasticamente a alívio ou aplicação de carga (módulo de Young, Aula 02) — princípio explorado diretamente pelo overcoring.

## Conteúdo

### Por que medir tensão in situ, e não apenas calculá-la

Toda escavação, poço ou talude perturba um campo de tensão que já existia no maciço antes da intervenção humana — as **tensões in situ** (ou tensões naturais, ou tensões virgens). Conhecer esse estado de tensão de fundo é indispensável para qualquer análise de estabilidade (Aula 07): os critérios de ruptura da Aula 03 avaliam se um estado de tensão é seguro, mas só fazem sentido se o estado de tensão de entrada — antes e depois da escavação — for conhecido com razoável confiança.

A tensão in situ **não pode ser calculada com precisão apenas a partir da geologia regional e da profundidade** — depende de fatores locais difíceis de prever a priori (histórico tectônico da área, topografia, heterogeneidade do maciço, proximidade de estruturas) — por isso, projetos de grande porte (barragens, minas subterrâneas profundas, túneis, poços de petróleo) medem diretamente as tensões, em vez de assumir um valor teórico.

### Origem gravitacional: a componente vertical

A componente mais previsível do estado de tensão in situ é a **tensão vertical (σv)**, gerada pelo peso da coluna de rocha sobrejacente:

σv = ρ · g · z

onde ρ é a densidade média da rocha sobrejacente, g é a aceleração da gravidade e z é a profundidade. Para uma densidade média típica de rocha crustal (~2.700 kg/m³), essa relação é frequentemente aproximada, na prática de engenharia, por σv ≈ 0,027 MPa por metro de profundidade (ou ~27 kPa/m) — um gradiente de referência amplamente citado, embora a densidade real varie por litologia e deva, idealmente, ser confirmada localmente.

### Origem tectônica: por que a tensão horizontal raramente segue a previsão elástica simples

Se o maciço se comportasse como um meio elástico confinado lateralmente sem poder se deformar horizontalmente (condição de deformação nula lateral, K0 elástico), a tensão horizontal seria uma fração fixa da vertical, dada por K0 = ν/(1−ν), onde ν é o coeficiente de Poisson (Aula 01) — para ν típico de rocha (~0,25), essa relação previria K0 ≈ 0,33, ou seja, tensão horizontal bem menor que a vertical. Na prática, medições em todo o mundo mostram que essa previsão simples **frequentemente falha**, e por dois motivos principais:

- **Tensões tectônicas residuais:** eventos tectônicos passados (compressão orogênica, por exemplo) podem "congelar" tensões horizontais residuais no maciço, muito além do que a resposta elástica ao peso próprio explicaria — é comum, sobretudo em profundidades rasas a moderadas em terrenos com história tectônica compressiva, encontrar K = σh/σv > 1, isto é, tensão horizontal **maior** que a vertical.
- **Erosão e alívio de carga (descompressão):** se uma espessura significativa de rocha foi removida por erosão ao longo do tempo geológico, a tensão vertical no ponto atual diminuiu (menos peso sobrejacente), mas a componente horizontal, gerada e "travada" enquanto a carga vertical era maior, não se dissipa na mesma proporção — o resultado líquido é uma razão K anormalmente alta perto da superfície atual, um padrão observado repetidamente em regiões que sofreram erosão substancial (escudos cratônicos, terrenos glaciados).

> [!important] A razão K = σh/σv não é uma constante universal, nem sequer isotrópica no plano horizontal
> Em muitos locais, as duas tensões horizontais principais (σH, maior, e σh, menor) diferem significativamente entre si, além de diferirem da vertical — um estado de tensão triaxial genuinamente anisotrópico, não redutível a um único valor de K. Bases de dados globais como o *World Stress Map* compilam a orientação de σH em escala continental, mostrando padrões coerentes com a cinemática de placas em grandes regiões, mas com variação local significativa em torno da tendência regional.

### Overcoring: alívio de tensão medido por deformação

O método de **overcoring** (sobrefuração) mede a tensão in situ pelo princípio inverso: em vez de aplicar carga, **alivia** a tensão existente numa pequena porção de rocha e mede a deformação elástica resultante desse alívio, usando a lei de Hooke (Aula 01) para retroceder ao estado de tensão original. O procedimento típico (célula CSIRO HI, extensômetro USBM, ou *doorstopper*):

1. Perfura-se um furo piloto de pequeno diâmetro no fundo de um furo de sondagem maior.
2. Instala-se no furo piloto uma célula com sensores de deformação (extensômetros elétricos ou strain gauges) colados nas paredes, orientados em múltiplas direções.
3. Um segundo furo de diâmetro maior é perfurado ao redor (a "sobrefuração"), isolando mecanicamente o testemunho que contém a célula do restante do maciço — esse testemunho se deforma elasticamente à medida que a tensão que antes era transmitida através dele é aliviada.
4. Os sensores registram a deformação de alívio em múltiplas direções; usando as constantes elásticas da rocha (E, ν, obtidas por ensaio de compressão do próprio testemunho, Aula 02), o software de análise inverte a deformação medida para obter o tensor de tensão completo (magnitude e orientação das três tensões principais).

Overcoring é o único dos três métodos apresentados nesta aula capaz de fornecer o **tensor de tensão completo em 3D** a partir de uma única medição bem-sucedida — mas depende de a rocha se comportar de forma razoavelmente elástica e homogênea na escala do testemunho, e é sensível a microfissuração induzida pela própria perfuração.

### Fraturamento hidráulico: pressão de fluido para induzir e reabrir fraturas

O **fraturamento hidráulico** (*hydraulic fracturing*) estima tensões por um princípio diferente: pressuriza-se um trecho isolado de um furo de sondagem com fluido até que a pressão seja suficiente para **induzir uma fratura de tração** na parede do furo. A sequência de pressões registradas durante o ensaio permite estimar as tensões principais no plano perpendicular ao furo:

- **Pressão de ruptura (breakdown pressure, Pb):** a pressão na qual a fratura se inicia — depende da tensão tangencial na parede do furo e da resistência à tração da rocha (Aula 02, ensaio brasileiro).
- **Pressão de fechamento (shut-in pressure, Ps):** ao interromper o bombeamento, a pressão à qual a fratura recém-criada se fecha — interpretada como uma estimativa direta da tensão principal **menor** no plano perpendicular ao furo (σ3), porque uma fratura de tração se propaga perpendicularmente à direção de menor tensão principal e se fecha quando a pressão do fluido cai abaixo dessa tensão.
- **Pressão de reabertura (Pr):** em ciclos subsequentes de pressurização, a pressão na qual a mesma fratura, já existente, reabre — sem mais a necessidade de vencer a resistência à tração da rocha intacta (a fratura já existe), permitindo isolar a contribuição da resistência à tração na pressão de ruptura original e, por diferença, estimar a tensão principal **maior** no plano (σH).

> [!tip] Fraturamento hidráulico mede tensão no plano perpendicular ao furo, não o tensor 3D completo
> Diferente do overcoring, um único ensaio de fraturamento hidráulico fornece as duas tensões principais no plano perpendicular ao eixo do furo (tipicamente as duas tensões horizontais, se o furo for vertical) e a orientação da fratura induzida (que se alinha com a direção de σH) — não o tensor de tensão tridimensional completo numa única medição. Obter as três tensões principais exige, em geral, combinar fraturamento hidráulico com alguma estimativa independente da tensão vertical (normalmente, o cálculo gravitacional simples, considerado confiável na maioria dos contextos).

### Macacos planos: compensação de tensão numa superfície acessível

O ensaio de **macacos planos** (*flat jack test*) é aplicável quando existe uma superfície de rocha acessível (parede de um túnel ou galeria já escavada, por exemplo), e mede a tensão normal a essa superfície pelo princípio da **compensação**:

1. Instalam-se dois pinos de referência na superfície da rocha, e mede-se com precisão a distância entre eles.
2. Corta-se uma ranhura na rocha entre os pinos, perpendicular à direção de tensão que se deseja medir — o corte alivia a tensão normal àquele plano, e a distância entre os pinos muda (tipicamente diminui, já que a rocha comprimida se expande ligeiramente ao ser aliviada).
3. Insere-se um macaco plano (uma bolsa metálica achatada, pressurizável hidraulicamente) na ranhura, e pressuriza-se gradualmente até que a distância entre os pinos retorne ao valor original medido antes do corte — essa pressão de **compensação** é, por construção, uma estimativa direta da tensão normal que existia naquele plano antes do corte.

O ensaio de macacos planos é conceitualmente simples e direto, mas mede apenas a tensão normal ao plano do corte — para caracterizar o tensor de tensão completo num ponto, são necessários cortes em múltiplas orientações, tornando o método mais trabalhoso quando o objetivo é a caracterização tridimensional completa, mas particularmente útil e confiável para verificar a tensão numa direção específica de interesse imediato (por exemplo, perpendicular ao eixo de uma escavação já feita).

## Exemplo trabalhado

**Situação:** um ensaio de fraturamento hidráulico realizado a 500 m de profundidade num furo vertical registra pressão de fechamento (shut-in) Ps = 9,5 MPa. A densidade média da rocha sobrejacente é 2.650 kg/m³. Estime a razão K = σh/σv nesse ponto e discuta se o resultado é consistente com a previsão elástica simples (K0 = ν/(1−ν), com ν = 0,22 para a litologia local).

**Resolução:**

σv = ρ·g·z = 2.650×9,81×500 ≈ 1,30×10⁷ Pa ≈ 13,0 MPa.

σh (estimada por Ps) ≈ 9,5 MPa.

K = σh/σv ≈ 9,5/13,0 ≈ 0,73.

K0 elástico previsto = ν/(1−ν) = 0,22/0,78 ≈ 0,28.

**Interpretação:** a razão K medida (≈0,73) é bem maior que a prevista pela resposta elástica simples ao peso próprio (≈0,28) — um sinal de que uma componente tectônica residual (ou efeito de descompressão por erosão, a depender do contexto geológico regional) está contribuindo significativamente para a tensão horizontal nesse local, além do que o peso da rocha sobrejacente explicaria isoladamente. Esse tipo de divergência é exatamente por que projetos não podem assumir K0 elástico como default em qualquer maciço — e por que a medição direta, e não o cálculo teórico, é o procedimento correto sempre que a obra tiver porte suficiente para justificar o custo do ensaio.

## Erros comuns

- **Assumir K0 = ν/(1−ν) como valor de projeto sem medição**, ignorando que tensões tectônicas residuais e efeitos de descompressão por erosão frequentemente produzem razões K muito diferentes da previsão elástica — especialmente perto da superfície.
- **Tratar um único ensaio de fraturamento hidráulico como suficiente para obter o tensor de tensão 3D completo**, esquecendo que ele fornece apenas as tensões no plano perpendicular ao furo.
- **Interpretar a pressão de ruptura (breakdown, Pb) diretamente como uma tensão principal**, quando na verdade Pb depende também da resistência à tração da rocha — a pressão de fechamento (Ps) e a de reabertura (Pr), que isolam esses efeitos, são as leituras corretas para inferir tensões principais.
- **Assumir que a tensão medida num único ponto (por overcoring, fraturamento hidráulico ou macacos planos) representa o estado de tensão de todo o maciço de um projeto extenso**, sem considerar a variabilidade espacial documentada em bases como o World Stress Map e sem repetir medições em pontos distintos quando a obra o justifica.

## O que não concluir

- **Que a tensão horizontal é sempre menor que a vertical.** Esse é o resultado esperado apenas sob a hipótese elástica simples de deformação lateral nula; tensões tectônicas residuais tornam K > 1 uma observação comum, não uma exceção rara, sobretudo em profundidades rasas a moderadas.
- **Que overcoring, fraturamento hidráulico e macacos planos são métodos concorrentes, dos quais só um deveria ser escolhido.** São frequentemente complementares: overcoring dá o tensor 3D completo mas é sensível à qualidade local da rocha testemunhada; fraturamento hidráulico é mais robusto em profundidade e em furos longos, mas dá apenas o estado plano; macacos planos são úteis para verificação pontual numa superfície já acessível. Projetos de grande porte frequentemente combinam mais de um método para validação cruzada.

## Recap relâmpago

- A tensão in situ tem uma componente gravitacional previsível (σv ≈ ρgz) e uma componente horizontal cuja magnitude e razão K = σh/σv frequentemente se desviam da previsão elástica simples devido a tensões tectônicas residuais e a efeitos de descompressão por erosão.
- Overcoring alivia tensão numa pequena porção de rocha e mede a deformação elástica resultante, fornecendo o tensor de tensão 3D completo a partir de constantes elásticas conhecidas.
- Fraturamento hidráulico usa a pressão de fechamento (shut-in) para estimar a tensão principal menor e a pressão de reabertura para estimar a maior, no plano perpendicular ao furo — não o tensor 3D completo numa única medição.
- Macacos planos medem a tensão normal a um plano específico numa superfície já acessível, pelo princípio da compensação (pressão que restaura a distância original entre pinos de referência após um corte de alívio).
- A tensão in situ deve ser medida diretamente, não apenas calculada, sempre que a obra justificar o custo — a variabilidade real observada em campo frequentemente contradiz previsões teóricas simples.

## Próxima aula

[[05-mecanica-de-rochas-aula-06-classificacoes-geomecanicas-rmr-q-gsi-smr|Aula 06 — Classificações geomecânicas de maciços rochosos: RMR, Q, GSI e SMR]]

## Anterior

[[05-mecanica-de-rochas-aula-04-descontinuidades-geometria-resistencia-permeabilidade|Aula 04 — Descontinuidades: geometria, resistência ao cisalhamento e permeabilidade do maciço]]

## Fontes

- Origem gravitacional e tectônica das tensões in situ, e desvios da previsão elástica K0: Jaeger, J. C., Cook, N. G. W. & Zimmerman, R. W. (2007), *Fundamentals of Rock Mechanics*, 4ª ed., Blackwell, cap. 11.
- Método de overcoring (célula CSIRO HI, USBM) e inversão de deformação de alívio: Amadei, B. & Stephansson, O. (1997), *Rock Stress and Its Measurement*, Chapman & Hall, cap. 4–5 (referência padrão para métodos de medição de tensão in situ, consistente com Goodman 1989, cap. 9).
- Fraturamento hidráulico, pressões de ruptura, fechamento e reabertura: Haimson, B. C. & Cornet, F. H. (2003), "ISRM suggested methods for rock stress estimation — Part 3: hydraulic fracturing (HF) and/or hydraulic testing of pre-existing fractures (HTPF)", *International Journal of Rock Mechanics and Mining Sciences*, 40(7-8).
- Método de macacos planos: Goodman, R. E. (1989), *Introduction to Rock Mechanics*, 2ª ed., Wiley, cap. 9.
- Variabilidade regional de orientação de tensão horizontal: base de dados *World Stress Map* (Heidelberg Academy of Sciences and Humanities), disponível em world-stress-map.org.

<!--
nivel: avancado
palavras_corpo: ~1950

mapa_objetivo_secao:
  geologia-avancado-m05-oa02: "Por que medir tensão in situ, e não apenas calculá-la" + "Origem gravitacional: a componente vertical" + "Origem tectônica: por que a tensão horizontal raramente segue a previsão elástica simples" + "Overcoring: alívio de tensão medido por deformação" + "Fraturamento hidráulico: pressão de fluido para induzir e reabrir fraturas" + "Macacos planos: compensação de tensão numa superfície acessível" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: MECROCHA-M05-A05-GRAVITACIONAL-001
    claim: "A tensão vertical in situ é aproximada por σv=ρgz, correspondendo a um gradiente de referência de aproximadamente 0,027 MPa por metro de profundidade para densidade crustal média (~2.700 kg/m³)."
    risk: fato
    source: "Jaeger, Cook & Zimmerman 2007, cap. 11; aproximação padrão da literatura de mecânica das rochas"
  - claim_id: MECROCHA-M05-A05-K0-002
    claim: "Sob a hipótese elástica de deformação lateral nula, a razão entre tensão horizontal e vertical seria K0=ν/(1−ν); medições de campo frequentemente mostram desvios significativos dessa previsão, incluindo K>1, atribuídos a tensões tectônicas residuais e a efeitos de descompressão por erosão."
    risk: fato
    source: "Jaeger, Cook & Zimmerman 2007, cap. 11; Amadei & Stephansson 1997"
  - claim_id: MECROCHA-M05-A05-OVERCORING-003
    claim: "O método de overcoring mede o tensor de tensão 3D completo a partir da deformação elástica de alívio de um testemunho isolado por sobrefuração, usando as constantes elásticas da rocha para inverter a deformação medida."
    risk: fato
    source: "Amadei & Stephansson 1997, cap. 4-5"
  - claim_id: MECROCHA-M05-A05-FRATHIDRAULICO-004
    claim: "No ensaio de fraturamento hidráulico, a pressão de fechamento (shut-in) estima a tensão principal menor e a pressão de reabertura permite estimar a tensão principal maior no plano perpendicular ao furo, sem fornecer o tensor 3D completo numa única medição."
    risk: fato
    source: "Haimson & Cornet 2003 (ISRM suggested methods)"
  - claim_id: MECROCHA-M05-A05-MACACOPLANO-005
    claim: "O ensaio de macacos planos mede a tensão normal a um plano de corte específico pelo princípio da compensação: a pressão hidráulica que restaura a distância original entre pinos de referência após o corte de alívio estima a tensão normal pré-existente naquele plano."
    risk: fato
    source: "Goodman 1989, cap. 9"
-->
