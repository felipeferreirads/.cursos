# Aula 02: Propriedades físicas e comportamento reológico das rochas; ensaios de laboratório

**ID:** geologia-avancado-m05-a02
**Módulo:** [[05-mecanica-de-rochas-modulo|Módulo 05 — Mecânica de rochas]]
**Duração estimada:** ~29 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** caracterizar as propriedades físicas básicas da rocha intacta, descrever as fases da curva tensão-deformação até a ruptura e associar cada propriedade e cada fase ao ensaio de laboratório que a mede.
**Pré-requisito:** tensão, deformação, módulo de Young e coeficiente de Poisson (Aula 01).

## Antes de começar, você precisa saber

- Tensão normal, deformação axial e as constantes elásticas E e ν, definidas na Aula 01.
- Que porosidade é a fração de volume vazio de um material sólido — conceito já usado no Módulo 01 para solos e sedimentos, aqui reaplicado à rocha intacta.

## Conteúdo

### Propriedades físicas básicas da rocha intacta

**Rocha intacta** designa o material rochoso livre de descontinuidades macroscópicas (fraturas, juntas, planos de acamamento) — a matriz entre as descontinuidades, cujo comportamento mecânico difere do comportamento do maciço rochoso como um todo (tema retomado na Aula 04). As propriedades físicas de referência de uma rocha intacta incluem:

- **Densidade e peso específico:** massa (ou peso) por unidade de volume, obtidos por pesagem e medição de volume de um corpo de prova, com relevância direta para o cálculo de tensões geostáticas (peso da coluna de rocha sobrejacente, retomado na Aula 05).
- **Porosidade:** fração de volume ocupada por poros e microfissuras — tipicamente baixa em rochas ígneas e metamórficas sãs (< 1–5 %) e mais alta em rochas sedimentares porosas (arenitos, alguns calcários, > 10–20 %). Porosidade correlaciona-se inversamente com resistência e com módulo de elasticidade: mais espaço vazio significa menos material sólido para suportar carga e mais concentração de tensão ao redor dos poros.
- **Teor de umidade e grau de saturação:** relevantes porque a presença de água reduz a resistência de muitas rochas (efeito de enfraquecimento por umidade, mais pronunciado em rochas argilosas e em algumas rochas sedimentares fracamente cimentadas) e altera a velocidade de propagação de ondas sísmicas através do material.
- **Velocidade de propagação de ondas sônicas (Vp, Vs):** medidas por ultrassom em corpo de prova ou por perfilagem sônica em poço; usadas tanto para estimar módulos elásticos dinâmicos (E, ν, módulo de cisalhamento G, calculados a partir de Vp, Vs e densidade) quanto como indicador indireto de qualidade da rocha — velocidades mais baixas frequentemente indicam maior grau de fraturamento ou alteração, mesmo em amostras aparentemente intactas.

> [!tip] Módulos elásticos "estáticos" versus "dinâmicos"
> Módulos elásticos obtidos por ensaio de compressão (estáticos, tema desta aula) e os obtidos por velocidade de onda sônica (dinâmicos) não são numericamente idênticos — o módulo dinâmico é sistematicamente maior, porque a rocha responde de forma mais rígida a uma solicitação de altíssima frequência e baixíssima amplitude (a passagem da onda) do que a uma solicitação estática que dá tempo para microfissuras se fecharem e se propagarem. A diferença tende a ser maior em rochas mais fraturadas ou porosas.

### A curva tensão-deformação da rocha: das microfissuras ao pico e além

Um ensaio de **compressão uniaxial** (um corpo de prova cilíndrico, sem confinamento lateral, carregado axialmente até a ruptura) produz uma curva tensão-deformação axial que, para a maioria das rochas, não é uma reta simples até o pico, mas passa por fases distintas, reconhecidas na literatura clássica de mecânica das rochas (Bieniawski, 1967; Brace et al., 1966):

1. **Fechamento de microfissuras (I):** nos níveis mais baixos de tensão, a curva é côncava para cima — microfissuras pré-existentes, orientadas de forma desfavorável, se fecham sob a carga inicial, produzindo mais deformação por unidade de tensão do que o comportamento elástico "verdadeiro" do material.
2. **Comportamento elástico linear (II):** com as microfissuras fechadas, a curva se torna aproximadamente reta — é nesse trecho que se mede o módulo de Young estático (a inclinação da reta) e o coeficiente de Poisson (razão entre deformação lateral e axial).
3. **Propagação estável de fissuras (III):** a partir de um limiar de tensão (tipicamente 40–60% da resistência de pico), novas microfissuras começam a se propagar de forma estável — a curva começa a se afastar da reta, e o volume do corpo de prova, que vinha diminuindo (compactação), passa a se comportar de forma cada vez menos compressiva.
4. **Propagação instável de fissuras e dilatância (IV):** próximo do pico (tipicamente 80–95% da resistência de pico), a propagação de fissuras se torna instável e se auto-alimenta; o volume do corpo de prova pode passar a **aumentar** líquidamente apesar da compressão contínua — fenômeno chamado **dilatância**, causado pela abertura de microfissuras que mais que compensa a compactação dos poros.
5. **Pico e comportamento pós-pico:** a tensão máxima suportada (a **resistência à compressão uniaxial**, UCS — *uniaxial compressive strength*) marca o pico da curva. Após o pico, a curva pode cair abruptamente (comportamento **frágil**, típico de rochas duras e pouco porosas, onde a energia elástica armazenada se libera de forma descontrolada ao romper) ou declinar suavemente até um patamar residual (comportamento **dúctil** ou com **amolecimento** gradual — *strain softening* —, mais comum em rochas porosas, alteradas ou sob alto confinamento).

> [!important] Resistência residual não é zero
> Mesmo após a ruptura, uma rocha fraturada continua a suportar alguma tensão — a **resistência residual**, tipicamente controlada pelo atrito ao longo das superfícies de ruptura já formadas, e sensivelmente menor que a resistência de pico. A diferença entre pico e residual é central para prever o comportamento de uma escavação após um evento de ruptura localizado (Aula 07): a rocha rompida não desaparece, continua oferecendo alguma resistência residual.

### Comportamento reológico: além da elasticidade instantânea

**Reologia** é o estudo de como um material se deforma e flui ao longo do tempo sob tensão sustentada — para rochas, isso inclui comportamentos que a idealização puramente elástica (Aula 01) não captura:

- **Fluência (creep):** deformação que continua a aumentar ao longo do tempo sob tensão constante, mesmo abaixo da resistência de pico. Pode ser primária (taxa decrescente, tendendo a estabilizar), secundária (taxa aproximadamente constante) ou terciária (taxa crescente, anunciando ruptura por fluência) — mais pronunciada em rochas evaporíticas (sal-gema, potássio), em folhelhos e em rochas sob alta temperatura, e de relevância direta para o dimensionamento de longo prazo de escavações permanentes e de cavernas de armazenamento em sal.
- **Comportamento viscoelástico:** resposta que combina uma componente elástica instantânea com uma componente viscosa dependente do tempo — modelada por combinações de elementos mola (elástico) e amortecedor (viscoso) em modelos reológicos simplificados (Maxwell, Kelvin-Voigt, Burgers), usados para prever a evolução do fechamento de uma escavação ao longo de anos.
- **Comportamento elastoplástico:** acima de um limiar de tensão, parte da deformação passa a ser permanente (não recuperável ao descarregar) — modelo mais adequado que a elasticidade pura para descrever o comportamento de rochas próximas ou além do pico, retomado nos critérios de ruptura da Aula 03.

### Ensaios de laboratório: qual propriedade cada um mede

- **Compressão uniaxial (UCS):** o ensaio de referência — corpo de prova cilíndrico (razão altura/diâmetro recomendada de 2,5 a 3,0, conforme métodos sugeridos pela ISRM), carregado axialmente sem confinamento lateral até a ruptura, com medição simultânea de deformação axial e lateral (por extensômetros ou *strain gauges*) para obter E e ν, além da UCS.
- **Compressão triaxial:** o mesmo corpo de prova, mas confinado lateralmente por uma pressão de célula (σ3 > 0) enquanto se aumenta a tensão axial (σ1) até a ruptura — repetido em várias pressões de confinamento, permite construir o envelope de ruptura (a curva ou reta que relaciona a resistência ao confinamento), a base experimental dos critérios de ruptura da Aula 03. Rochas quase sempre ficam mais resistentes e mais dúcteis com o aumento do confinamento.
- **Ensaio brasileiro (tração indireta):** um disco (ou cilindro curto) de rocha é comprimido diametralmente entre duas placas até romper por tração ao longo do plano diametral — método indireto, porque a tração direta em rocha é difícil de aplicar sem introduzir concentrações de tensão espúrias nas garras do equipamento; fornece a **resistência à tração (σt)**, tipicamente uma pequena fração (5–10%) da UCS, refletindo a fragilidade da rocha à tração em comparação com a compressão.
- **Ensaio de cisalhamento direto:** um bloco de rocha (intacta ou, mais frequentemente, contendo uma descontinuidade, tema da Aula 04) é submetido a uma tensão normal fixa enquanto uma força cisalhante é aplicada até o deslizamento — mede diretamente a resistência ao cisalhamento em função da tensão normal.
- **Point load test (índice de carga puntiforme, Is50):** ensaio de campo simplificado, aplicando carga concentrada por pontas cônicas a um fragmento irregular de rocha ou a um testemunho de sondagem, sem a necessidade de preparar um corpo de prova padronizado — o índice obtido (Is50, normalizado para diâmetro equivalente de 50 mm) correlaciona-se empiricamente com a UCS (aproximadamente UCS ≈ 20 a 25 × Is50, variando por litologia), sendo amplamente usado como triagem rápida de resistência ao longo de um testemunho inteiro, quando ensaiar cada trecho por compressão uniaxial seria inviável em tempo e custo.

## Exemplo trabalhado

**Situação:** um testemunho de granito são é ensaiado em compressão triaxial em três pressões de confinamento distintas, obtendo resistência de pico de 180 MPa sem confinamento (σ3 = 0), 240 MPa a σ3 = 10 MPa e 290 MPa a σ3 = 20 MPa. Um segundo testemunho do mesmo granito, mas com alteração hidrotermal moderada e maior porosidade, ensaiado sem confinamento, rompe a apenas 60 MPa, com uma curva tensão-deformação que mostra amolecimento gradual pós-pico em vez de queda abrupta.

**Interpretação:** o aumento sistemático da resistência de pico com o confinamento (180 → 240 → 290 MPa) é o comportamento esperado e confirma que o confinamento lateral suprime a propagação de fissuras que levaria à ruptura frágil sob compressão uniaxial não confinada — essa relação entre σ1 de pico e σ3 será formalizada como envelope de ruptura na Aula 03. A diferença entre os dois testemunhos do "mesmo" granito (180 MPa são vs. 60 MPa alterado) ilustra por que a caracterização de rocha intacta em projeto real nunca se apoia num único valor "de catálogo" para uma litologia: alteração hidrotermal, mesmo moderada, pode reduzir a resistência a um terço do valor da rocha sã, e a mudança do padrão de ruptura (frágil → amolecimento gradual) já sinaliza, antes mesmo de qualquer cálculo, que o material alterado se comportará de forma mais dúctil numa escavação.

## Erros comuns

- **Tratar a UCS como uma constante do tipo litológico**, ignorando a variabilidade natural de amostra para amostra dentro do mesmo maciço (grau de alteração, microfissuração herdada, anisotropia) — projetos sérios trabalham com uma distribuição estatística de valores de resistência, não um único número.
- **Usar módulo elástico dinâmico (de ensaio sônico) diretamente em cálculos que pressupõem módulo estático**, sem aplicar a correção empírica adequada — o dinâmico tende a superestimar a rigidez real sob carregamento estático.
- **Ignorar a dilatância pré-pico**, tratando a rocha como um material que só muda de volume por compactação — em escavações profundas, a dilatância ao redor da abertura é parte do mecanismo de dano progressivo do maciço.
- **Extrapolar o índice de carga puntiforme (Is50) para UCS usando um fator de conversão genérico de manual, sem calibração local** — o fator de correlação varia significativamente por litologia e deveria, idealmente, ser calibrado com um subconjunto de ensaios de compressão uniaxial da mesma formação.

## O que não concluir

- **Que uma rocha com comportamento frágil em laboratório (queda abrupta pós-pico) sempre romperá de forma frágil e repentina no maciço.** O confinamento in situ, normalmente maior do que em muitos ensaios de laboratório não confinados, e a presença de descontinuidades (Aula 04) podem mudar substancialmente o modo de ruptura observado em escala de campo.
- **Que fluência (creep) só importa para sal-gema.** É mais pronunciada e mais estudada em evaporitos, mas ocorre, em grau menor, em praticamente qualquer rocha sob tensão sustentada por longos períodos — relevante para o dimensionamento de suportes de escavações permanentes mesmo em litologias "competentes".

## Recap relâmpago

- Propriedades físicas básicas da rocha intacta — densidade, porosidade, umidade, velocidade sônica — correlacionam-se com resistência e rigidez; módulos elásticos dinâmicos (sônicos) são sistematicamente maiores que os estáticos (de ensaio de compressão).
- A curva tensão-deformação de um ensaio uniaxial passa por fechamento de microfissuras, comportamento elástico linear, propagação estável e depois instável de fissuras (com dilatância), pico (UCS) e comportamento pós-pico (frágil ou com amolecimento gradual até uma resistência residual não nula).
- Comportamento reológico inclui fluência (creep, mais pronunciada em evaporitos e sob alta temperatura), resposta viscoelástica e comportamento elastoplástico acima de um limiar de tensão.
- Compressão uniaxial mede UCS, E e ν; compressão triaxial constrói o envelope de ruptura em função do confinamento; o ensaio brasileiro mede resistência à tração indireta; o cisalhamento direto mede resistência ao cisalhamento; o point load test (Is50) é uma triagem de campo correlacionada empiricamente com a UCS.

## Próxima aula

[[05-mecanica-de-rochas-aula-03-criterios-de-ruptura-mohr-coulomb-griffith-hoek-brown|Aula 03 — Critérios de ruptura aplicáveis às rochas: Mohr-Coulomb, Griffith e Hoek-Brown]]

## Anterior

[[05-mecanica-de-rochas-aula-01-tensao-deformacao-circulo-de-mohr|Aula 01 — Tensão e deformação em rochas: estado de tensão, tensões principais e círculo de Mohr]]

## Fontes

- Fases da curva tensão-deformação até a ruptura (fechamento de fissuras, propagação estável e instável, dilatância): Bieniawski, Z. T. (1967), "Mechanism of brittle fracture of rock", *International Journal of Rock Mechanics and Mining Sciences*, 4(4).
- Propriedades físicas, ensaios de laboratório (UCS, triaxial, brasileiro, cisalhamento direto) e métodos sugeridos: Goodman, R. E. (1989), *Introduction to Rock Mechanics*, 2ª ed., Wiley, cap. 3 e 6.
- Comportamento reológico, fluência e modelos viscoelásticos em rochas: Jaeger, J. C., Cook, N. G. W. & Zimmerman, R. W. (2007), *Fundamentals of Rock Mechanics*, 4ª ed., Blackwell, cap. 10.
- Índice de carga puntiforme (point load test) e correlação empírica com UCS: ISRM (International Society for Rock Mechanics), *Suggested Methods for Determining Point Load Strength*, 1985 (revisado).

<!--
nivel: avancado
palavras_corpo: ~1850

mapa_objetivo_secao:
  geologia-avancado-m05-oa01: "Propriedades físicas básicas da rocha intacta" + "A curva tensão-deformação da rocha: das microfissuras ao pico e além" + "Comportamento reológico: além da elasticidade instantânea" + "Ensaios de laboratório: qual propriedade cada um mede" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: MECROCHA-M05-A02-MODULOS-001
    claim: "Módulos elásticos dinâmicos, obtidos por velocidade de onda sônica, são sistematicamente maiores que os módulos estáticos obtidos por ensaio de compressão, sobretudo em rochas mais fraturadas ou porosas."
    risk: fato
    source: "Jaeger, Cook & Zimmerman 2007, cap. 10; prática consolidada de caracterização geotécnica"
  - claim_id: MECROCHA-M05-A02-CURVATD-002
    claim: "A curva tensão-deformação de um ensaio de compressão uniaxial em rocha passa por fases de fechamento de microfissuras, comportamento elástico linear, propagação estável e depois instável de fissuras (com dilatância volumétrica), pico de resistência (UCS) e comportamento pós-pico frágil ou com amolecimento gradual até uma resistência residual não nula."
    risk: fato
    source: "Bieniawski 1967; Goodman 1989, cap. 3"
  - claim_id: MECROCHA-M05-A02-FLUENCIA-003
    claim: "Fluência (creep) sob tensão sustentada é particularmente pronunciada em rochas evaporíticas (sal-gema) e em folhelhos, e sob temperaturas elevadas, sendo relevante para o dimensionamento de longo prazo de escavações permanentes."
    risk: fato
    source: "Jaeger, Cook & Zimmerman 2007, cap. 10"
  - claim_id: MECROCHA-M05-A02-ENSAIOS-004
    claim: "Compressão uniaxial mede UCS e as constantes elásticas estáticas; compressão triaxial, repetida em diferentes confinamentos, constrói o envelope de ruptura; o ensaio brasileiro mede resistência à tração indireta; o point load test (Is50) correlaciona-se empiricamente com a UCS, com fator de conversão dependente da litologia."
    risk: fato
    source: "ISRM 1985; Goodman 1989, cap. 6"
-->
