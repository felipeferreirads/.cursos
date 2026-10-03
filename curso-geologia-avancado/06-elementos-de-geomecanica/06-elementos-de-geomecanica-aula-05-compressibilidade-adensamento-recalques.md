# Aula 05: Compressibilidade e adensamento: ensaio edométrico, cálculo de recalques e deformabilidade de maciços

**ID:** geologia-avancado-m06-a05
**Módulo:** [[06-elementos-de-geomecanica-modulo|Módulo 06 — Elementos de geomecânica]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** interpretar a curva e–log σ' de um ensaio edométrico para obter tensão de pré-adensamento, OCR e índices de compressão; calcular a magnitude do recalque por adensamento primário e o tempo necessário para atingi-lo pela teoria de Terzaghi; e estimar o módulo de deformabilidade de um maciço rochoso a partir das classificações geomecânicas.

**Pré-requisito:** Aula 03 deste módulo (tensão efetiva); Aula 04 (condutividade hidráulica); índice de vazios e sua conversão com a porosidade, da Aula 02; classificações RMR e GSI, do Módulo 05, Aula 06.

## Antes de começar, você precisa saber

- Que o índice de vazios e = Vv/Vs é o índice preferido para acompanhar variação de volume em solos, porque o volume de sólidos permanece constante durante a compressão (Aula 02).
- Que a variação de volume de um solo é governada pela **tensão efetiva**, não pela total (Aula 03).
- A distinção entre **compactação** (densificação mecânica rápida de solo não saturado por energia aplicada, Aula 02) e **adensamento** (redução de volume ao longo do tempo por expulsão de água de solo saturado sob carga sustentada) — esta aula trata do segundo.

## Conteúdo

### O mecanismo: por que a argila recalca devagar

Aplique uma carga sobre uma camada de argila saturada. No instante inicial, a água não teve tempo de sair, e como água e grãos são praticamente incompressíveis, o volume não pode mudar: **todo o acréscimo de tensão é absorvido pela poropressão** (Δu = Δσ). Pela equação de Terzaghi, σ' não mudou — e por isso o solo ainda não recalcou por adensamento.

A partir daí, o excesso de poropressão gera um gradiente hidráulico em direção às fronteiras drenantes, e a água começa a escoar. À medida que ela sai, Δu dissipa, e a mesma carga total vai sendo progressivamente transferida da água para o esqueleto sólido: σ' cresce, o índice de vazios cai, e a camada recalca. O processo termina quando Δu = 0 e todo o acréscimo virou tensão efetiva.

A **velocidade** de tudo isso é controlada pela condutividade hidráulica (Aula 04). É por isso que areias recalcam essencialmente durante a construção (drenam em minutos ou horas) e argilas continuam recalcando por anos ou décadas — mesmo mecanismo, escalas de tempo separadas por várias ordens de grandeza.

O recalque total de uma fundação tem três parcelas: o **recalque imediato** (distorção elástica sem variação de volume, instantâneo), o **adensamento primário** (dissipação do excesso de poropressão — o objeto central desta aula) e a **compressão secundária** (deformação lenta do esqueleto sob σ' já constante, tratada adiante).

### O ensaio edométrico e a curva e–log σ'

O **ensaio de adensamento unidimensional**, ou **edométrico** (ASTM D2435), confina um corpo de prova num anel rígido — impedindo deformação lateral, exatamente a condição K0 da Aula 03 — entre duas pedras porosas, e aplica estágios de carga, tipicamente dobrando a tensão a cada 24 h. Registra-se a variação de altura em cada estágio.

Plotando o índice de vazios ao final de cada estágio contra o logaritmo da tensão efetiva, obtém-se a **curva e–log σ'**, cuja forma tem dois trechos com significado físico distinto:

- Um trecho inicial **abatido** (pouca variação de e por incremento de carga) — o **trecho de recompressão**, com inclinação **Cr** (índice de recompressão, também escrito Cs, índice de expansão).
- Um trecho posterior **íngreme e aproximadamente reto** — a **reta virgem** de compressão, com inclinação **Cc** (índice de compressão).

O ponto de quebra entre os dois é a **tensão de pré-adensamento**, σ'p: a maior tensão efetiva que aquele solo já suportou em sua história. Enquanto a carga aplicada não ultrapassa σ'p, o solo apenas "refaz" um caminho que já percorreu, e deforma pouco. Ao ultrapassá-la, entra em território inédito e passa a deformar muito mais — tipicamente Cc é 5 a 10 vezes maior que Cr. **A curva e–log σ' é, literalmente, a memória de tensões do depósito.**

A determinação de σ'p a partir da curva é feita pela **construção gráfica de Casagrande (1936)**: localiza-se o ponto de curvatura máxima, traçam-se por ele a horizontal e a tangente, e a bissetriz do ângulo entre elas intercepta o prolongamento da reta virgem em σ'p.

Define-se então a **razão de sobreadensamento**:

**OCR = σ'p / σ'v0**

onde σ'v0 é a tensão efetiva vertical atual de campo (calculada como na Aula 03). OCR = 1 indica solo **normalmente adensado** (nunca suportou mais do que suporta hoje); OCR > 1 indica solo **sobreadensado**, que já suportou mais — por erosão de camadas sobrejacentes, por dessecação, por degelo de uma calota, ou por rebaixamento antigo do lençol.

> [!important] O sobreadensamento é o que separa um recalque tolerável de um recalque destrutivo
> Duas argilas com o mesmo Cc e o mesmo e0 podem recalcar de forma completamente diferente sob a mesma carga: se a carga final ficar abaixo de σ'p, a deformação segue Cr e o recalque é pequeno; se ultrapassá-la, entra na reta virgem e o recalque pode ser uma ordem de grandeza maior. Determinar σ'p corretamente é, muitas vezes, a decisão mais importante de todo o estudo de fundação.

### Cálculo da magnitude do recalque primário

Para uma camada de espessura H, índice de vazios inicial e0, sob acréscimo Δσ:

**Solo normalmente adensado** (σ'v0 = σ'p; toda a trajetória na reta virgem):

ρ = (Cc·H)/(1+e0) · log[(σ'v0 + Δσ)/σ'v0]

**Solo sobreadensado com carga final ainda abaixo de σ'p** (toda a trajetória na recompressão):

ρ = (Cr·H)/(1+e0) · log[(σ'v0 + Δσ)/σ'v0]

**Solo sobreadensado com carga final acima de σ'p** (o caso mais comum na prática, e o que exige duas parcelas):

ρ = (Cr·H)/(1+e0) · log(σ'p/σ'v0) + (Cc·H)/(1+e0) · log[(σ'v0 + Δσ)/σ'p]

O logaritmo é **decimal** (base 10) em todas as expressões, por convenção consolidada da mecânica dos solos — usar logaritmo natural produz erro de fator 2,303.

### A teoria do adensamento unidimensional de Terzaghi: quanto tempo

A magnitude diz o quanto; a teoria de Terzaghi (1925) diz **quando**. A equação de difusão do excesso de poropressão é:

∂u/∂t = cv · ∂²u/∂z²

onde **cv** é o **coeficiente de adensamento** (dimensão de área por tempo, tipicamente m²/ano), obtido do próprio ensaio edométrico pelos métodos de **Casagrande** (log do tempo, ajuste em t50) ou de **Taylor** (raiz do tempo, ajuste em t90).

A solução é organizada em dois adimensionais: o **fator tempo**

**Tv = cv·t / Hd²**

e o **grau de adensamento médio** U (fração do recalque primário já ocorrida). A relação Tv ↔ U é tabelada e independe do solo, da carga e da geometria — é a mesma curva universal para todos os casos. Valores de referência: U = 50% → Tv = 0,197; U = 90% → Tv = 0,848.

**Hd é a maior distância que uma partícula de água precisa percorrer para escapar da camada**, e é onde mora o erro mais frequente de toda a mecânica dos solos:

- Camada com drenagem nas **duas** faces (areia acima e abaixo): Hd = H/2.
- Camada com drenagem em **uma só** face (rocha impermeável ou argila rija abaixo): Hd = H.

Como Hd entra ao **quadrado**, trocar drenagem dupla por simples **quadruplica** o tempo previsto. Uma argila que adensaria 90% em 2 anos com dupla drenagem levaria 8 anos com drenagem simples — mesma carga, mesmo recalque final, quatro vezes o tempo.

> [!warning] cv não é constante ao longo do carregamento
> O coeficiente de adensamento varia com o nível de tensão, e costuma cair quando o solo passa de recompressão para a reta virgem. Adotar um cv único obtido num estágio arbitrário do ensaio e aplicá-lo a toda a faixa de carga da obra é uma simplificação comum, mas deve ser feita escolhendo o estágio cuja faixa de tensão corresponde à da obra — não o primeiro nem o último da tabela por conveniência.

### Compressão secundária

Terminada a dissipação do excesso de poropressão (U = 100%), o solo continua a deformar lentamente sob σ' constante — a **compressão secundária**, ou *creep*, governada pelo **índice de compressão secundária** Cα:

ρs = (Cα·H)/(1+ep) · log(t2/t1)

Ela é desprezível em areias e em muitas argilas inorgânicas rijas, mas domina o recalque de longo prazo em **argilas orgânicas, turfas e solos moles**, onde pode superar o próprio adensamento primário ao longo da vida útil da obra. Uma correlação de referência útil é Cα/Cc ≈ 0,04 ± 0,01 para argilas inorgânicas e ≈ 0,05 ± 0,01 para argilas orgânicas e turfas (Mesri & Godlewski, 1977).

### Deformabilidade de maciços rochosos

Em rocha, não há adensamento no sentido de Terzaghi (a porosidade é baixa e a água drena rápido demais para gerar excesso de poropressão relevante em escala de obra). O problema muda de natureza: interessa o **módulo de deformabilidade do maciço**, Em, que é sistematicamente **menor** que o módulo da rocha intacta Ei medido em laboratório, porque as descontinuidades fecham e deslizam sob carga (Módulo 05, Aula 04).

Estimativas correntes a partir das classificações geomecânicas do Módulo 05, Aula 06:

- **Bieniawski (1978):** Em = 2·RMR − 100 (GPa), válida apenas para RMR > 50.
- **Serafim & Pereira (1983):** Em = 10^[(RMR−10)/40] (GPa), que estende a estimativa para maciços de qualidade mais baixa, onde a expressão linear de Bieniawski dá valores negativos.
- **Hoek & Diederichs (2006):** formulação moderna baseada em GSI e no fator de perturbação D, na forma Em = Ei·[0,02 + (1 − D/2)/(1 + e^((60+15D−GSI)/11))], preferida quando Ei é conhecido.

Medições diretas em campo, quando o porte da obra justifica, são feitas por **ensaio dilatométrico**, **macaco plano** ou **ensaio de placa** em galeria — os mesmos princípios de alívio e compensação de tensão do Módulo 05, Aula 05.

> [!important] A razão Em/Ei é o que a classificação está realmente estimando
> Todas essas correlações traduzem uma pergunta única: quanto do módulo da rocha intacta o maciço fraturado efetivamente conserva. Para maciços de boa qualidade, Em/Ei pode passar de 0,5; para maciços muito fraturados, cai para poucos centésimos. Aplicar Ei de laboratório diretamente ao maciço superestima a rigidez — e subestima o recalque — em ordens de grandeza.

## Exemplo trabalhado

**Situação:** um aterro impõe Δσ = 80 kPa sobre uma camada de argila de 4 m de espessura, drenada em ambas as faces por camadas arenosas. Do ensaio edométrico e do perfil de tensões: σ'v0 = 100 kPa, σ'p = 130 kPa, e0 = 0,90, Cc = 0,35, Cr = 0,07, cv = 2,0 m²/ano. Calcule o OCR, o recalque por adensamento primário e o tempo para atingir 90% dele.

**Resolução:**

**Passo 1 — Classificar o solo.**
OCR = σ'p/σ'v0 = 130/100 = **1,3** → solo levemente sobreadensado.

Tensão final: σ'vf = σ'v0 + Δσ = 100 + 80 = 180 kPa. Como 180 kPa > σ'p = 130 kPa, a trajetória **cruza** a tensão de pré-adensamento: é o caso de duas parcelas.

**Passo 2 — Parcela de recompressão** (de 100 até 130 kPa, inclinação Cr):
ρ1 = (0,07 × 4)/(1 + 0,90) × log(130/100)
ρ1 = (0,28/1,90) × log(1,30) = 0,14737 × 0,11394 = 0,0168 m

**Passo 3 — Parcela na reta virgem** (de 130 até 180 kPa, inclinação Cc):
ρ2 = (0,35 × 4)/(1 + 0,90) × log(180/130)
ρ2 = (1,40/1,90) × log(1,3846) = 0,73684 × 0,14126 = 0,1041 m

**Passo 4 — Recalque primário total:**
ρ = 0,0168 + 0,1041 = **0,121 m ≈ 12,1 cm**

**Passo 5 — Tempo para 90% de adensamento.**
Drenagem em ambas as faces → Hd = H/2 = 4/2 = **2,0 m**
Para U = 90%, Tv = 0,848.
t = Tv·Hd²/cv = 0,848 × (2,0)²/2,0 = 0,848 × 4/2,0 = **1,70 ano ≈ 20 meses**

**Interpretação:** dois resultados merecem atenção. Primeiro, a distribuição do recalque: os 30 kPa iniciais (de 100 a 130 kPa, dentro da memória de tensões do solo) produzem apenas 1,7 cm, enquanto os 50 kPa seguintes (já na reta virgem) produzem 10,4 cm — seis vezes mais deformação com pouco mais de carga. Se o aterro fosse dimensionado para Δσ = 30 kPa em vez de 80 kPa, o recalque cairia para cerca de um sétimo. É a demonstração numérica de por que σ'p é o parâmetro decisivo. Segundo, o tempo: se a mesma camada fosse drenada por apenas uma face (por exemplo, com rocha impermeável na base em vez de areia), Hd seria 4,0 m e o tempo saltaria para 0,848 × 16/2,0 = 6,8 anos — quatro vezes maior, com recalque final idêntico. A identificação correta das fronteiras drenantes vale, em previsão de prazo, tanto quanto o próprio ensaio.

## Erros comuns

- **Usar Hd = H em camada com drenagem dupla** (ou o contrário). Como Hd entra ao quadrado, o erro é de fator 4 no tempo — o erro isolado mais caro desta aula.
- **Aplicar Cc a toda a trajetória quando o solo é sobreadensado**, ignorando a parcela de recompressão e superestimando o recalque; ou aplicar Cr a toda ela, quando a carga final ultrapassa σ'p, subestimando gravemente.
- **Usar logaritmo natural em vez de decimal** nas fórmulas de recalque — erro sistemático de fator 2,303.
- **Confundir adensamento com compactação** (Aula 02): compactação é rápida, mecânica e em solo não saturado; adensamento é lento, hidráulico e em solo saturado.
- **Tratar cv como constante do material** e aplicá-lo fora da faixa de tensões em que foi medido.
- **Aplicar o módulo de laboratório da rocha intacta (Ei) ao maciço** sem redução por qualidade do maciço, superestimando a rigidez.

## O que não concluir

- **Que recalque total é sinônimo de problema estrutural.** Estruturas toleram recalques absolutos surpreendentemente grandes desde que **uniformes**; o que causa dano é o **recalque diferencial** entre apoios, e é ele que os limites normativos controlam.
- **Que a teoria de Terzaghi descreve fielmente o adensamento real.** Ela assume fluxo e deformação unidimensionais, solo saturado e homogêneo, cv constante e relação e–σ' linear em escala log. Camadas reais com lentes drenantes, carregamento gradual e adensamento tridimensional desviam dessas hipóteses — a teoria é um excelente primeiro modelo, não uma descrição exata.
- **Que um OCR > 1 sempre garante recalques pequenos.** Só garante enquanto a carga final permanecer abaixo de σ'p. Ultrapassada essa tensão, o solo entra na reta virgem e se comporta como normalmente adensado dali em diante.

## Recap relâmpago

- No adensamento, o acréscimo de carga é inicialmente absorvido pela poropressão (Δu = Δσ, sem recalque primário); à medida que a água escoa, a carga migra para o esqueleto (σ' cresce) e a camada recalca — velocidade governada pela condutividade hidráulica.
- A curva e–log σ' do ensaio edométrico tem trecho de recompressão (Cr) e reta virgem (Cc), separados pela **tensão de pré-adensamento σ'p** (obtida pela construção de Casagrande); OCR = σ'p/σ'v0 distingue solo normalmente adensado (OCR = 1) de sobreadensado (OCR > 1).
- O recalque primário usa Cr abaixo de σ'p, Cc acima, e **as duas parcelas** quando a carga cruza σ'p; logaritmo sempre decimal.
- O tempo vem de Tv = cv·t/Hd², com a relação Tv ↔ U universal (U = 50% → Tv = 0,197; U = 90% → Tv = 0,848). **Hd é a maior distância até uma face drenante**: H/2 com drenagem dupla, H com drenagem simples — e entra ao quadrado.
- A compressão secundária (Cα) segue após U = 100% sob σ' constante e domina o longo prazo em argilas orgânicas e turfas.
- Em rocha, o análogo é o módulo de deformabilidade do maciço Em < Ei, estimado por RMR (Bieniawski 1978; Serafim & Pereira 1983) ou GSI (Hoek & Diederichs 2006), ou medido por dilatômetro, macaco plano ou ensaio de placa.

## Próxima aula

[[06-elementos-de-geomecanica-aula-06-resistencia-ao-cisalhamento-e-prospeccao-geotecnica|Aula 06 — Resistência ao cisalhamento de solos e rochas e prospecção geotécnica do subsolo]]

## Anterior

[[06-elementos-de-geomecanica-aula-04-percolacao-em-meios-porosos-e-fissurados|Aula 04 — Percolação de água em meios porosos e fissurados]]

## Fontes

- Teoria do adensamento unidimensional: Terzaghi, K. (1925), *Erdbaumechanik auf bodenphysikalischer Grundlage*, Deuticke; exposição moderna em Terzaghi, K., Peck, R. B. & Mesri, G. (1996), *Soil Mechanics in Engineering Practice*, 3ª ed., Wiley, cap. 3 e 16.
- Ensaio edométrico, curva e–log σ', cálculo de recalques e fator tempo: Das, B. M. (2019), *Fundamentos de Engenharia Geotécnica*, 9ª ed., Cengage, cap. 11; ASTM D2435 (*Standard Test Methods for One-Dimensional Consolidation Properties of Soils Using Incremental Loading*).
- Construção gráfica da tensão de pré-adensamento: Casagrande, A. (1936), "The determination of the pre-consolidation load and its practical significance", *Proceedings of the 1st International Conference on Soil Mechanics and Foundation Engineering*, Cambridge, v. 3, p. 60–64.
- Compressão secundária e a razão Cα/Cc: Mesri, G. & Godlewski, P. M. (1977), "Time- and stress-compressibility interrelationship", *Journal of the Geotechnical Engineering Division, ASCE*, 103(GT5), p. 417–430.
- Deformabilidade de maciços rochosos: Bieniawski, Z. T. (1978), "Determining rock mass deformability: experience from case histories", *International Journal of Rock Mechanics and Mining Sciences*, 15(5), p. 237–247; Serafim, J. L. & Pereira, J. P. (1983), "Consideration of the geomechanical classification of Bieniawski", *Proceedings of the International Symposium on Engineering Geology and Underground Construction*, Lisboa; Hoek, E. & Diederichs, M. S. (2006), "Empirical estimation of rock mass modulus", *International Journal of Rock Mechanics and Mining Sciences*, 43(2), p. 203–215.

<!--
nivel: avancado
palavras_corpo: ~2200

mapa_objetivo_secao:
  geologia-avancado-m06-oa03: "O mecanismo: por que a argila recalca devagar" + "O ensaio edométrico e a curva e–log σ'" + "Cálculo da magnitude do recalque primário" + "A teoria do adensamento unidimensional de Terzaghi: quanto tempo" + "Compressão secundária" + "Deformabilidade de maciços rochosos" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOMEC-M06-A05-MECANISMO-001
    claim: "No instante do carregamento de argila saturada, todo o acréscimo de tensão é absorvido pela poropressão (Δu=Δσ) sem mudança de σ'; o recalque primário ocorre à medida que o excesso de poropressão dissipa e a carga é transferida ao esqueleto."
    risk: fato
    source: "Terzaghi 1925; Terzaghi, Peck & Mesri 1996, cap. 3"
  - claim_id: GEOMEC-M06-A05-EDOMETRO-002
    claim: "A curva e–log σ' do ensaio edométrico (ASTM D2435) apresenta trecho de recompressão (Cr) e reta virgem (Cc), separados pela tensão de pré-adensamento σ'p; Cc é tipicamente 5 a 10 vezes maior que Cr; OCR=σ'p/σ'v0."
    risk: fato
    source: "ASTM D2435; Das 2019, cap. 11"
  - claim_id: GEOMEC-M06-A05-CASAGRANDE-003
    claim: "A tensão de pré-adensamento é determinada graficamente pela construção de Casagrande (1936), usando o ponto de curvatura máxima, a horizontal, a tangente e a bissetriz interceptando o prolongamento da reta virgem."
    risk: fato
    source: "Casagrande 1936"
  - claim_id: GEOMEC-M06-A05-RECALQUE-004
    claim: "O recalque primário usa Cr abaixo de σ'p, Cc acima, e a soma das duas parcelas quando a carga final cruza σ'p, com logaritmo decimal: ρ=(Cr·H/(1+e0))·log(σ'p/σ'v0)+(Cc·H/(1+e0))·log(σ'vf/σ'p)."
    risk: fato
    source: "Das 2019, cap. 11"
  - claim_id: GEOMEC-M06-A05-TEMPO-005
    claim: "O fator tempo é Tv=cv·t/Hd², com relação Tv↔U universal (U=50%→Tv=0,197; U=90%→Tv=0,848); Hd é a maior distância a uma face drenante, igual a H/2 com drenagem dupla e H com drenagem simples, entrando ao quadrado."
    risk: fato
    source: "Terzaghi 1925; Das 2019, cap. 11"
  - claim_id: GEOMEC-M06-A05-SECUNDARIA-006
    claim: "A compressão secundária ocorre após a dissipação do excesso de poropressão, sob σ' constante, com ρs=(Cα·H/(1+ep))·log(t2/t1); a razão Cα/Cc é ≈0,04±0,01 para argilas inorgânicas e ≈0,05±0,01 para argilas orgânicas e turfas."
    risk: fato
    source: "Mesri & Godlewski 1977"
  - claim_id: GEOMEC-M06-A05-EM-007
    claim: "O módulo de deformabilidade do maciço Em é menor que o da rocha intacta Ei, e é estimado por Em=2·RMR−100 GPa (Bieniawski 1978, só para RMR>50), Em=10^[(RMR−10)/40] GPa (Serafim & Pereira 1983) ou pela formulação em GSI e D de Hoek & Diederichs (2006)."
    risk: fato
    source: "Bieniawski 1978; Serafim & Pereira 1983; Hoek & Diederichs 2006"
-->
