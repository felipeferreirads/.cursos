# Auditoria científica — Módulo 14: Sensoriamento remoto

**Material auditado:** 7 aulas (`geologia-avancado-m14-a01` a `a07`) + hub do módulo
**Modo:** `audit-and-fix` · **Profundidade:** `full` · **Passagens:** 1 (as sete aulas em conjunto)
**Data:** 2026-09-08
**Veredito:** ✅ **Aprovado** — nenhum achado 🔴 ou 🟠 em aberto

---

## Sumário

| Severidade | Quantidade | Situação |
|---|---|---|
| 🔴 Erro | 2 | todos corrigidos |
| 🟠 Impreciso | 5 | todos corrigidos |
| 🟡 Desatualizado | 2 | todos corrigidos |
| 🔵 Sem fonte | 0 | — |
| ⚪ Controverso | 2 | registrados sem escolha de lado |
| **Total** | **11** | **`open_findings: []`** |

**Alegações verificadas:** 32 declaradas nos manifestos das sete aulas, mais 9 levantadas pela auditoria fora da lista do autor (as duas 🔴 e três das 🟠 estão nesse segundo grupo — o que o autor não marcou como arriscado foi, de novo, onde o erro se escondeu).

**Exemplos numéricos recalculados do zero, todos conferem:**

| Aula | Exemplo | Verificação |
|---|---|---|
| a01 | alvo de 200 m em pixel de 30 m; revisita Landsat 8+9 | 200/30 ≈ 6-7 pixels ✅; 16 d ÷ 2 satélites defasados = 8 d ✅; cena 185 × 180 km ✅ |
| a02 | janela atmosférica: 1,4 / 0,45 / 2,2 µm | posições de absorção de H₂O e comportamento λ⁻⁴ ✅ |
| a03 | curvas de solo e vegetação geobotânica | posições de feição ✅ (mas o *mecanismo* atribuído estava errado — achado 1) |
| a04 | NDVI ao sol e em sombra | (0,45−0,05)/0,50 = **0,80** ✅; 0,6×0,45 = 0,27 e 0,6×0,05 = 0,03 ✅; (0,27−0,03)/0,30 = **0,80** ✅; queda de 40% no NIR ✅ |
| a05 | matriz de confusão 3×3, 300 pixels | linhas 100/100/100 ✅, colunas 95/90/115 ✅, total 300 ✅; global 240/300 = **80%** ✅; produtor xisto 70/100 = **70%** ✅; usuário xisto 70/90 = **77,8%** ✅; comissão 20/90 = 22,2% ✅ |
| a06 | franjas InSAR Sentinel-1 | λ/2 = 5,6/2 = **2,8 cm** ✅; 3,5 × 2,8 = **9,8 cm** ✅ |
| a07 | GCPs e anomalia térmica | 42 − 28 = **14 °C** ✅; sobreposições 80%/65% acima dos mínimos 70-80%/60-70% ✅ |

**Nenhum achado quantitativo.** Toda a aritmética do módulo está correta.

---

## Padrão dominante: PARES DE SINAL OPOSTO

Os dois achados vermelhos e um dos laranjas têm exatamente a mesma forma, e ela é específica deste módulo: o autor descreve corretamente **onde** a feição está e **para onde** ela se desloca, mas troca **qual dos dois mecanismos de sinal contrário** a produz. São três pares, e em todos os três o conteúdo "geográfico" está certo e o rótulo físico está invertido:

| Par | O que a aula dizia | O que é |
|---|---|---|
| Óxidos de ferro | a feição de 0,87-0,92 µm é **transferência de carga** | é **campo cristalino**; a transferência de carga está no UV (~0,25 µm) e sua cauda produz a queda de 0,4-0,6 µm |
| Termal / silicatos | feição de Christiansen é um **mínimo** de emissividade | é um **máximo**; os mínimos são as bandas de **reststrahlen** |
| Termal / radiometria | **Stefan-Boltzmann** converte a radiância medida em temperatura | Stefan-Boltzmann descreve a emissão **total**; a conversão de radiância **de banda** é a **inversão de Planck** |

Por que esse padrão é caro num módulo autodidata: cada um desses pares é um par de nomes próprios, e um flashcard do tipo "o que é a feição de Christiansen?" nasce com o verso exatamente invertido — o aluno revisa o erro dezenas de vezes e sai citando o termo certo para o fenômeno errado. É o mesmo mecanismo de dano do padrão ATRIBUIÇÃO identificado no Módulo 11, aplicado agora a mecanismos físicos em vez de autores.

**Padrão secundário: ESPECIFICAÇÃO OPERACIONAL VOLÁTIL.** Dois achados (Sentinel-2C, banda 11 do TIRS) não são erros de raciocínio — são fatos de calendário e de calibração de instrumento que só existem em nota técnica de agência, não são dedutíveis de princípio nenhum e mudam sozinhos com o tempo. É o análogo, aqui, do que a geodésia brasileira foi no Módulo 13. Ficam registrados como ponto de manutenção periódica.

**Onde o módulo está limpo:** toda a metade de processamento (a04 e a05 — realce, razões, filtros, ACP, K-means, máxima verossimilhança, matriz de confusão) não tem um único erro de mecanismo ou de definição, e nem os dois exemplos numéricos que a sustentam. O mesmo vale para o princípio da abertura sintética, a relação franja-deslocamento, o retorno múltiplo do LiDAR e todo o fluxo SfM. O erro se concentrou onde a aula precisava nomear um mecanismo espectroscópico específico ou consultar uma nota técnica de agência.

---

## Achados

### 🔴 1. Mecanismos do Fe³⁺ invertidos: campo cristalino trocado por transferência de carga

**claim_id:** `SENSREM-M14-A03-FEOXIDO-001` · **Tipo:** erro factual
**Onde:** a03 · seção "Solos", seção "Minerais e rochas", exemplo trabalhado, recap, manifesto
**Estava escrito:** "uma feição adicional em torno de 0,87-0,92 µm associada à **transferência de carga** do Fe³⁺"

**Problema:** os dois mecanismos foram trocados entre si. A banda de 0,86-0,92 µm é uma transição de **campo cristalino** (ligand field) do Fe³⁺ — o envelope dos componentes do nível ⁴T₁ desdobrado —, e sua posição é justamente o que **discrimina hematita (~0,86 µm) de goethita (~0,90-0,92 µm)**. A transição de **transferência de carga** ligante-metal (O²⁻ → Fe³⁺) fica perto de 40.000 cm⁻¹, ou seja, ~0,25 µm no ultravioleta próximo; é a cauda dessa banda, ordens de grandeza mais intensa, que invade o visível pela borda azul e produz a queda de 0,4-0,6 µm — e, portanto, **a cor** do solo laterítico. A aula atribuiu a cor à feição errada e o discriminador mineralógico à física errada, num trecho cujo propósito declarado é exatamente ensinar mecanismo.

**Agravante:** o exemplo trabalhado da própria a03 usa a feição de 0,87 µm para inferir óxido de ferro e a rotulava como transferência de carga, propagando o erro para a parte da aula que o aluno mais imita.

**Correção aplicada:** as duas feições foram separadas e nomeadas corretamente no corpo, com a energia e a posição da banda de transferência de carga explicitadas; o discriminador hematita/goethita por posição foi acrescentado (informação nova que a correção tornou disponível de graça); a seção "Processos eletrônicos" ganhou uma frase distinguindo os dois submecanismos sob o rótulo comum; o exemplo trabalhado passou a inferir hematita a partir da posição em 0,86-0,87 µm; recap e manifesto alinhados.
**Fonte:** Sherman, D. M. & Waite, T. D. (1985), "Electronic spectra of Fe³⁺ oxides and oxide hydroxides in the near IR to near UV", *American Mineralogist* 70(11-12):1262-1269 · Clark (1999), *Manual of Remote Sensing* vol. 3, cap. 1 · **Nível:** revisada por pares / base de referência · **Confiança:** confirmado
**Também aparece em:** nenhum outro arquivo do curso — busca por "transferência de carga" e "campo cristalino" em todos os módulos retorna zero ocorrências fora da a03.
**Desfecho:** ✅ corrigido

---

### 🔴 2. Feição de Christiansen descrita como mínimo de emissividade, quando é máximo

**claim_id:** `SENSREM-M14-A07-CHRISTIANSEN-002` · **Tipo:** erro factual (confusão entre duas feições distintas)
**Onde:** a07 · seção "Sensoriamento remoto termal", recap, manifesto, hub do módulo
**Estava escrito:** "feições de absorção (na verdade, **mínimos de emissividade**) características ligadas ao grau de polimerização […] um princípio conhecido como **deslocamento de Christiansen**"

**Problema:** a feição de Christiansen é um **máximo** de emissividade (mínimo de reflectância), que ocorre na faixa estreita em que o índice de refração do material se aproxima do índice do meio em volta, tipicamente entre 7 e 9 µm. Os **mínimos** de emissividade no TIR são as **bandas de reststrahlen**, produzidas pelas vibrações fundamentais de estiramento Si-O, entre ~8 e 12 µm. A aula fundiu as duas num só objeto e atribuiu à feição nomeada a propriedade da outra. O **sentido** do deslocamento com a polimerização (félsico → onda mais curta) estava correto e foi preservado.

**Correção aplicada:** as duas feições foram separadas explicitamente, com sinal, faixa e mecanismo de cada uma; o deslocamento composicional foi quantificado (~7,5-8,0 µm em félsicas, ~8,5-9,0 µm em máficas a ultramáficas) e ancorado no teor de SiO₂ além do grau de polimerização; a expressão "deslocamento de Christiansen" foi substituída por "feição de Christiansen" e "deslocamento da feição"; recap, manifesto e hub alinhados.
**Fonte:** literatura de espectroscopia de emissão termal de silicatos — mapa da Christiansen Feature do Diviner/LRO (Greenhagen et al.) · Ferrari et al. (2019), "Retrieving magma composition from TIR spectra", *Scientific Reports* 9 · Sabins & Ellis (2020) cap. 8 · **Nível:** revisada por pares · **Confiança:** confirmado
**Também aparece em:** hub do módulo (corrigido). Nenhuma ocorrência de "Christiansen" ou "reststrahlen" fora do Módulo 14.
**Desfecho:** ✅ corrigido

---

### 🟠 3. Lei errada nomeada para converter radiância de banda em temperatura

**claim_id:** `SENSREM-M14-A07-STEFANBOLTZMANN-003` · **Tipo:** erro factual / atribuição de mecanismo
**Onde:** a07 · seção "Sensoriamento remoto termal", recap, manifesto, hub
**Estava escrito:** "A relação física central que permite converter a radiância termal medida pelo sensor em temperatura é a **Lei de Stefan-Boltzmann**"

**Problema:** Stefan-Boltzmann (*M* = εσ*T*⁴) governa a **exitância radiante integrada em todos os comprimentos de onda**. Um sensor termal mede **radiância espectral dentro de uma banda estreita**, e a conversão dessa medida em temperatura de brilho é feita **invertendo a lei de Planck** — a mesma lei que a a02 já havia introduzido e que a a07 deixava de reutilizar. Havia ainda imprecisão de grandeza: Stefan-Boltzmann dá exitância (W m⁻²), não radiância (W m⁻² sr⁻¹). Classificado 🟠 e não 🔴 porque a direção física (emissão cresce com T, escalada por ε) está certa e o argumento da ambiguidade temperatura-emissividade sobrevive intacto às duas leis.

**Correção aplicada:** as duas leis foram separadas com seus papéis; a inversão de Planck foi nomeada como a operação real, amarrada explicitamente à Aula 02; "radiância" trocada por "exitância radiante" no enunciado de Stefan-Boltzmann; introduzido o termo *temperatura de brilho*; o argumento da ambiguidade foi reancorado no produto ε × função(T), válido em ambas. Recap, manifesto e hub alinhados.
**Fonte:** Jensen (2016) cap. 2 · USGS, *Landsat Collection 2 Level-2 Surface Temperature ATBD* · Sabins & Ellis (2020) cap. 8 · **Nível:** normativa / base de referência · **Confiança:** confirmado
**Desfecho:** ✅ corrigido

---

### 🟠 4. Janela dividida no Landsat 8/9 ensinada sem a advertência do USGS sobre a banda 11

**claim_id:** `SENSREM-M14-A07-TIRSB11-004` · **Tipo:** omissão que gera erro
**Onde:** a07 · seção "Sensoriamento remoto termal", exemplo trabalhado, recap, Fontes, manifesto

**Problema:** a aula apresentava o par de bandas TIRS 10 + 11 como o caminho para temperatura de superfície por janela dividida, sem nenhuma ressalva. A **banda 11 tem incerteza radiométrica residual muito maior que a banda 10** por luz espúria (*stray light*) captada de fora do campo de visão do telescópio; mesmo após o algoritmo de correção implementado na cadeia de produção em fevereiro de 2017, a variabilidade residual permanece da ordem de 1,7 K, e o **USGS recomenda explicitamente que os usuários evitem a banda 11 em análise quantitativa, nomeando as técnicas de janela dividida**. Como escrito, o material ensinava ao aluno exatamente o procedimento desaconselhado pelo operador do sensor. Ironia registrada: o artigo já citado nas Fontes da aula (Jiménez-Muñoz et al. 2014) chega a essa mesma conclusão e recomenda canal único sobre a banda 10.

**Correção aplicada:** parágrafo de ressalva operacional inserido, separando o princípio (janela dividida, válido, e método de escolha em sensores como o MODIS) da prática recomendada para este sensor (canal único sobre a banda 10, com emissividade e correção atmosférica fornecidas à parte); o enunciado do exemplo trabalhado, que já usava a banda 10, foi ajustado para nomear o método de canal único em vez de janela dividida; recap ajustado; Fontes completadas com a nota de calibração do USGS e o *status* de calibração do TIRS (Barsi et al., SPIE 2020), e a citação de Jiménez-Muñoz ganhou periódico, volume e páginas.
**Fonte:** USGS, *Landsat 8 OLI and TIRS Calibration Notices* · Barsi et al., *Landsat-8 TIRS Thermal Radiometric Calibration Status* (SPIE 2020, NTRS 20210026916) · Jiménez-Muñoz et al. (2014), *IEEE GRSL* 11(10):1840-1843 · **Nível:** normativa (operador do sensor) · **Confiança:** confirmado
**Desfecho:** ✅ corrigido

---

### 🟠 5. "SWIR nos três canais" é impossível no OLI, e as composições listadas contradiziam o exemplo da própria aula

**claim_id:** `SENSREM-M14-A01-COMPOSICAO-005` · **Tipo:** erro factual + inconsistência interna
**Onde:** a01 · seção "Composições coloridas", exemplo trabalhado, recap, manifesto
**Estava escrito:** "composições que colocam bandas do infravermelho de ondas curtas (SWIR) **nos três canais** — por exemplo, no Landsat 8, as bandas **7-5-3 ou 6-5-2** em R-G-B"

**Problema:** três defeitos encadeados. (a) O OLI tem **exatamente duas** bandas SWIR (6 e 7) — nenhuma composição pode ocupar os três canais com SWIR, e a frase afirma uma impossibilidade física do sensor. (b) Nem 7-5-3 nem 6-5-2 têm mais de uma banda SWIR: 7-5-3 é a combinação convencionalmente rotulada "natural com remoção atmosférica" e 6-5-2, "agricultura"; as convencionalmente chamadas de geologia e de SWIR são **7-6-2** e **7-6-4**. (c) **Inconsistência interna**: o exemplo trabalhado da mesma aula usa 7-6-4 e a descreve corretamente banda a banda, e o manifesto declarava 7-6-4 — só o corpo da aula divergia.

**Correção aplicada:** o parágrafo foi reescrito explicitando que o OLI tem duas bandas SWIR e que o padrão é usá-las mais uma terceira banda de contraste, nomeando 7-6-2 e 7-6-4; "nos três canais" removido; o exemplo trabalhado passou a se referir à composição já apresentada, fechando a inconsistência; recap e manifesto alinhados. Preservada e reforçada a ressalva (correta, e já presente no manifesto original) de que esses rótulos são convenção de mercado e de software, **não norma** — o que importa é saber quais bandas entraram em cada canal.
**Fonte:** NASA/USGS *Landsat 8 Data Users Handbook* (o OLI possui duas bandas SWIR — fato normativo) · convenções de rotulagem de combinação conferidas em fontes de referência de mercado, que divergem entre si e por isso não foram tratadas como norma · **Nível:** normativa (para o número de bandas) / geral (para os rótulos) · **Confiança:** confirmado
**Desfecho:** ✅ corrigido

---

### 🟠 6. Resolução mais grosseira da banda L atribuída ao comprimento de onda

**claim_id:** `SENSREM-M14-A06-BANDALRESOL-006` · **Tipo:** confusão de escopo / mecanismo
**Onde:** a06 · seção "Radar de Abertura Sintética (SAR)", recap, manifesto
**Estava escrito:** "banda L penetra mais fundo na vegetação […] mas com resolução espacial tipicamente mais grosseira **para uma mesma abertura sintética**"

**Problema:** a formulação é algebricamente defensável apenas sob a restrição artificial de manter fixo o *comprimento da abertura sintética* — o que não é como um SAR é projetado. O resultado de manual é o oposto do que o aluno vai memorizar: a **resolução em azimute de um SAR estripe é independente do comprimento de onda**, valendo ≈ *D*/2, metade do comprimento físico da antena, porque um λ maior obriga a sintetizar uma abertura proporcionalmente mais longa (*L*ₛ = λ*R*/*D*) e o λ se cancela. A frase, como escrita, planta a regra falsa "λ maior ⇒ pior resolução" como se fosse física fundamental. A observação empírica (sistemas em banda L *são* mais grosseiros) está certa; a causa apontada, não.

**Correção aplicada:** parágrafo dedicado inserido, dando o resultado *D*/2, mostrando por que o λ se cancela, e nomeando as duas causas reais da limitação prática — antena física maior necessária e menor largura de banda disponível/alocada nas faixas baixas, que é o que fixa a resolução em alcance. A afirmação empírica foi mantida, agora desacoplada da causa errada; a menção "banda X entrega resolução mais fina" foi reformulada para "é usada onde se quer detalhe fino". Recap ajustado e claim novo acrescentado ao manifesto.
**Fonte:** Woodhouse (2006), *Introduction to Microwave Remote Sensing*, cap. 6-7 · formulação padrão δ_az = *D*/2 · **Nível:** base de referência · **Confiança:** confirmado
**Desfecho:** ✅ corrigido

---

### 🟠 7. Condições de layover e de sombra formuladas contra um ângulo não definido

**claim_id:** `SENSREM-M14-A06-LAYOVER-007` · **Tipo:** impreciso (omissão que impede aplicar a regra)
**Onde:** a06 · seção "Geometria de imageamento lateral", recap, manifesto
**Estava escrito:** layover "quando a encosta é íngreme o bastante (**mais inclinada que a linha de visada do radar**)"; sombra em encostas "**mais íngremes que o ângulo de visada**"

**Problema:** "linha de visada" é uma reta, não um ângulo — não há com o que comparar uma declividade —, e "ângulo de visada" é usado na aula sem definição e, no caso da sombra, aponta para o complemento errado. As condições corretas se organizam numa única comparação, entre a declividade da encosta (α) e o **ângulo de incidência** (θ), medido a partir da vertical local: encurtamento quando α < θ (com o caso-limite α = θ, em que a encosta colapsa numa linha brilhante), layover quando α > θ, e sombra na encosta oposta quando sua declividade supera **90° − θ**, o ângulo de depressão. O ângulo de incidência é, além disso, um dos pontos de atenção que o próprio planejamento do módulo mandou verificar, e a aula o cita adiante ("exige saber […] o ângulo de incidência") sem nunca tê-lo usado para nada.

**Correção aplicada:** frase de enquadramento inserida antes das três distorções, apresentando a comparação α vs. θ como o critério único que resolve as três; cada uma das três condições passou a declarar seu limiar; caso-limite α = θ acrescentado; recap reescrito com os três limiares; manifesto atualizado.
**Fonte:** Woodhouse (2006) cap. 6 · Sabins & Ellis (2020) cap. 4 · convergência de fontes técnicas de SAR sobre os limiares α < θ / α > θ / β > 90° − θ · **Nível:** base de referência · **Confiança:** confirmado
**Desfecho:** ✅ corrigido

---

### 🟡 8. Constelação Sentinel-2 descrita como 2A + 2B

**claim_id:** `SENSREM-M14-A01-SENTINEL2C-008` · **Tipo:** desatualização
**Onde:** a01 · seção "As quatro resoluções", tabela de sensores, recap, manifesto

**Problema:** correto até janeiro de 2025, não mais. O **Sentinel-2C substituiu o Sentinel-2A na operação nominal em 21 de janeiro de 2025**; o par nominal é hoje **2B + 2C** (o 2D sucederá o 2B). O 2A não foi desligado: desde março de 2025 opera numa campanha de extensão, defasado 36° do 2B, que adensa a revisita **sobre a Europa, a África tropical e a América do Sul** — exatamente as regiões mais penalizadas por nuvem, e portanto informação de valor prático direto para o leitor brasileiro, que a redação antiga não só omitia como impedia. A revisita nominal de 5 dias não mudou.

**Correção aplicada:** parágrafo reescrito distinguindo o **arranjo** (dois satélites simultâneos defasados 180°, 5 dias — estável) da **identidade** dos satélites (que muda com o tempo), com as datas e a campanha de extensão nomeadas e sua consequência para a América do Sul explicitada; tabela e recap ajustados; manifesto atualizado com a data e a fonte.
**Fonte:** SentiWiki/Copernicus, *S2 Mission* · ESA *Sentinel-2 User Handbook* · **Nível:** normativa (operador da missão) · **Confiança:** confirmado
**Também aparece em:** Módulo 07, a04, cita "Sentinel-2 ~10 m" numa tabela de resolução, sem nomear satélites da constelação — **não precisou de correção**.
**Desfecho:** ✅ corrigido

---

### 🟡 9. Reflectância da água no azul-verde qualificada como "relativamente alta" sem escala absoluta

**claim_id:** `SENSREM-M14-A03-AGUAREFL-009` · **Tipo:** impreciso / omissão que gera erro
**Onde:** a03 · seção "Água", manifesto

**Problema:** "reflectância relativamente alta e razoavelmente uniforme na faixa azul-verde" é verdadeiro como afirmação *relativa*, dentro da própria curva da água, mas em termos absolutos a reflectância da água limpa é baixa em todo o espectro — da ordem de poucos por cento mesmo no seu máximo. Sem o qualificador, o aluno pode ler "alta" como "clara", o que colide com o fato operacional que a mesma seção ensina em seguida (água é escura em qualquer banda) e com o que o NDWI de fato explora, que não é o verde ser alto e sim o verde ser **menos baixo que o NIR**.

**Correção aplicada:** "relativamente alta" trocada por "mais alta", e ressalva de escala inserida ao fim da seção, amarrando explicitamente a leitura relativa ao mecanismo do índice; manifesto ajustado.
**Fonte:** Sabins & Ellis (2020) cap. 2 · Jensen (2016) cap. 2 (curvas de reflectância de água limpa) · **Nível:** base de referência · **Confiança:** confirmado
**Desfecho:** ✅ corrigido

---

### ⚪ 10. Coeficiente Kappa apresentado como métrica pacífica

**claim_id:** `SENSREM-M14-A05-KAPPA-010` · **Tipo:** controvérsia (certeza indevida)
**Onde:** a05 · seção "Matriz de confusão", recap, Fontes, manifesto

**Problema:** não é erro do autor — é divergência real e ativa entre fontes do mesmo nível. Congalton & Green (2019), a referência-padrão que a própria aula cita, ensina e recomenda o Kappa, e ele segue reportado em cerca de metade da literatura recente. Do outro lado, Pontius & Millones (2011), no artigo deliberadamente intitulado *Death to Kappa*, argumentam que a linha de base de "acaso" é arbitrária e propõem substituí-lo por desacordo de quantidade e desacordo de alocação; e Foody (2020) argumenta sua inadequação específica para *comparar* acurácias de mapas distintos. Um aluno que conheça só um dos lados vai interpretar mal metade do que ler.

**Tratamento (política para achados ⚪ — nenhum lado escolhido):** parágrafo inserido registrando as duas posições com seus argumentos e seus proponentes, e fechando com a postura defensável que ambos os lados sustentam — reportar sempre a matriz completa e as acurácias de produtor e usuário por classe, que ninguém disputa, e tratar o Kappa como número de contexto. "Penaliza esse efeito" abrandado para "se propõe a penalizar". Recap ajustado, Fontes completadas com os dois artigos da crítica, manifesto reclassificado com `risk: controverso`.
**Confiança:** em disputa
**Desfecho:** ⚪ registrado, sem escolha de lado — **não bloqueia gate**

---

### ⚪ 11. Dois índices diferentes chamados NDWI

**claim_id:** `SENSREM-M14-A04-NDWIHOMONIMO-011` · **Tipo:** ambiguidade de nomenclatura
**Onde:** a04 · seção "Operações aritméticas", recap, Fontes, manifesto

**Problema:** a atribuição da aula estava **correta** — NDWI = (Verde − NIR)/(Verde + NIR) é de fato de McFeeters (1996), e para corpos d'água. O que faltava era a advertência: existe um segundo índice homônimo, de **Gao (1996)**, definido como (NIR − SWIR)/(NIR + SWIR), que mede **água líquida na folha** e é índice de vegetação, não de água superficial — e a a03 deste mesmo módulo ensina justamente que o SWIR responde à água foliar, deixando o aluno a um passo da confusão. Há ainda o **MNDWI** de Xu (2006), (Verde − SWIR)/(Verde + SWIR).

**Tratamento:** parágrafo inserido nomeando os três índices com suas fórmulas, seus autores e o que cada um mede, e fechando com a regra prática (conferir as bandas antes de supor o que um "NDWI" mede); recap e Fontes completados; manifesto ampliado. Nenhuma correção foi necessária no que a aula já afirmava.
**Fonte:** McFeeters (1996), *IJRS* 17(7):1425-1432 · Gao (1996), *RSE* 58(3):257-266 · Xu (2006), *IJRS* 27(14):3025-3033 · **Nível:** revisada por pares · **Confiança:** confirmado
**Desfecho:** ⚪ registrado e explicitado no material — **não bloqueia gate**

---

## Verificado e correto

Passou intacto (amostra do que foi conferido e não gerou achado):

**Especificações de sensor** — Landsat 8/9: 11 bandas, 30 m multiespectral, 15 m pancromática, 100 m termal, 12 bits, órbita ~705 km, cruzamento do Equador ~10h local, revisita 16 d (8 d combinado), cena 185 × 180 km, banda cirrus 1,36-1,38 µm, bandas 6 (1,57-1,65 µm), 7 (2,11-2,29 µm), 4 (0,64-0,67 µm), TIRS 10 (10,60-11,19 µm) e 11 (11,50-12,51 µm). Sentinel-2: 13 bandas, 10/20/60 m, ~786 km, B4 665 nm, B8 842 nm. ASTER: 14 bandas, VNIR 15 m / SWIR 30 m / TIR 90 m, 6 bandas SWIR, 5 termais, perda do detector SWIR em 2008. Sentinel-1 banda C a 5,405 GHz (~5,6 cm), par de 12 dias.

**Física** — c = λν e E = hν; regiões espectrais (UV 0,01-0,4; visível 0,4-0,7; NIR 0,7-1,3; SWIR 1,3-3; TIR 3-14 com uso prático 8-14; micro-ondas 1 mm-1 m); Rayleigh ∝ λ⁻⁴ e sua consequência sobre a banda azul; Mie e sua menor dependência espectral; *path radiance*; emissividade de materiais naturais entre 0,85 e 0,98; racional de projeto da banda cirrus **dentro** de uma banda de absorção de vapor d'água.

**Espectroscopia** — dubleto da caulinita em 2,16-2,20 µm; esmectita e ilita/muscovita próximas de 2,20 µm com forma distinguível; calcita e dolomita em 2,3-2,35 µm; bandas de absorção da água em 1,4 e 1,9 µm no solo; borda vermelha em 0,68-0,75 µm; absorção de clorofila em ~0,45 e ~0,68 µm com pico verde em ~0,55 µm; reflectância NIR foliar de 40-50% controlada pelo mesofilo; *blue shift* da borda vermelha sob estresse por metais, com a ressalva de evidência indireta corretamente mantida.

**Processamento** — NDVI de Rouse et al. (1973, NASA SP-351) com faixas de valor por alvo; cancelamento algébrico do fator multiplicativo na razão; alongamento linear e por equalização; kernels de convolução, Sobel e Prewitt; ACP e o comportamento típico da PC1 (com a ressalva, já presente e correta, de que a atribuição por componente não é fixa); ACP seletiva de Loughlin (1991); K-means e rotulação pós-classificação; máxima verossimilhança, SVM e Random Forest; definições de acurácia global, do produtor e do usuário; pixel misto.

**Ativo e 3D** — princípio da abertura sintética por Doppler; frequências e comprimentos de onda das bandas X, C e L; efeito visual e causa do encurtamento de rampa; fase, interferograma, franja = λ/2 pelo trajeto de ida e volta, desdobramento de fase, perda de coerência em vegetação; SRTM por interferometria de duas antenas simultâneas; LiDAR corretamente classificado como **ativo**, ~1064 nm com a hedge de faixa por fabricante, retorno múltiplo com o mecanismo certo (o pulso passa **pelas aberturas** do dossel, não *através* das folhas) e geração de MDT sob floresta; paralaxe e sua relação com a distância; fluxo SfM completo (pontos-chave → nuvem esparsa → ajuste de feixes → nuvem densa → MDS/ortomosaico/malha) e o papel dos GCPs; limitações do SfM.

**Bibliografia** — 23 referências conferidas uma a uma (autor, ano, periódico, volume, edição, editora). Todas corretas, incluindo as que costumam falhar: Linder 4ª ed. 2016 (existe), Richards 6ª ed. 2022, Congalton & Green 3ª ed. 2019, Sabins & Ellis 4ª ed. 2020 Waveland, Hunt 1977 *Geophysics* 42(3), Gates et al. 1965 *Applied Optics* 4(1), Loughlin 1991 *PE&RS* 57(9), Wehr & Lohr 1999 *ISPRS J.* 54(2-3), Westoby et al. 2012 *Geomorphology* 179, James & Robson 2012 *JGR* 117. **Nenhum achado bibliográfico** — contraste notável com o Módulo 13, que teve quatro.

**Pontos do planejamento verificados e sem achado:** LiDAR classificado como ativo ✅; penetração de dossel descrita pelo mecanismo correto ✅; conversão DN → radiância → reflectância aparece apenas em termos qualitativos na a04, **sem fórmula nem constante numérica** — não havia parâmetro de sensor nem ângulo solar a conferir; EVI (Huete et al. 2002) e valores de NDVI para vegetação senescente **não são tratados no módulo** — ausência, não erro (encaminhado como sugestão ao gerador).

---

## Verificação cruzada entre módulos

Busca em todo o curso por *transferência de carga*, *campo cristalino*, *Christiansen*, *reststrahlen*, *polimerização*, *NDVI*, *Kappa*, *Sentinel*, *emissividade*, *InSAR*, *LiDAR*, *SAR*.

**Nenhuma contradição transversal.** Fora do Módulo 14, o vocabulário de sensoriamento remoto aparece apenas no **Módulo 07, a04** (SIG, sensoriamento remoto e análise de risco), e ali está **integralmente consistente** com o que a a06 do Módulo 14 ensina: InSAR em escala milimétrica a centimétrica, medindo apenas a componente na linha de visada, perdendo coerência em vegetação densa e movimento rápido; LiDAR para terreno sob dossel. Os dois módulos se reforçam em vez de divergir.

Os pares de sinal oposto dos achados 1 e 2 (transferência de carga / campo cristalino, Christiansen / reststrahlen) **não aparecem em nenhum outro módulo do curso** — a busca retorna zero ocorrências fora do Módulo 14 —, de modo que os dois vermelhos não contaminaram nada além das próprias aulas. O termo *polimerização* aparece no Módulo 40 (tectossilicatos), em sentido cristaloquímico, plenamente compatível com o uso da a07.

**Complementaridade registrada, não tratada como achado:** o Módulo 07 menciona técnicas de série temporal por espalhadores persistentes (PS-InSAR), que a a06 do Módulo 14 não desenvolve. Não é contradição — é um tópico que o módulo especializado poderia ter, e fica anotado para uma eventual revisão de escopo.

---

## Advertências para o gerador de questionários e de flashcards

1. **Os três pares de sinal oposto são o material de avaliação mais valioso do módulo**, e o erro corrigido é o distrator perfeito em cada um: (a) transferência de carga no UV, dando a cor, contra campo cristalino em 0,87-0,92 µm, separando hematita de goethita; (b) feição de Christiansen = **máximo** de emissividade contra bandas de reststrahlen = **mínimos**; (c) Stefan-Boltzmann = emissão **total** contra inversão de Planck = radiância **de banda** → temperatura. Prefira questões de discriminação a questões de definição isolada.
2. **Não gerar nenhum card ou gabarito que atribua a feição de 0,87-0,92 µm à transferência de carga, nem que chame a feição de Christiansen de mínimo de emissividade, nem que diga que Stefan-Boltzmann converte a medida do sensor em temperatura.** Foram exatamente esses três os erros corrigidos.
3. **Hematita ~0,86 µm vs. goethita ~0,90-0,92 µm** é um par numérico limpo, novo no material após a correção, e rende card de discriminação direta.
4. **Deslocamento da feição de Christiansen**: ~7,5-8,0 µm em félsicas, ~8,5-9,0 µm em máficas/ultramáficas — cuidado com o sentido, é contraintuitivo (mais SiO₂ ⇒ onda mais **curta**).
5. **Banda 11 do TIRS**: distrator forte é "usar janela dividida com as bandas 10 e 11 do Landsat 8/9", que é o procedimento formalmente desaconselhado pelo USGS. Questão de aplicação de primeira qualidade.
6. **O OLI tem duas bandas SWIR, não três** — distrator "composição com SWIR nos três canais". E não criar questão que dependa de um rótulo de composição como se fosse norma: os rótulos divergem entre fontes.
7. **Resolução azimutal do SAR ≈ D/2, independente de λ** — distrator "banda L tem pior resolução porque o comprimento de onda é maior", que é justamente a intuição corrigida. A causa real é antena maior e menos largura de banda.
8. **α vs. θ é o melhor candidato a questão de aplicação quantitativa do bloco de sensores ativos**: dado um ângulo de incidência e uma declividade, dizer qual das três distorções ocorre. Cobre a armadilha central declarada pelo hub, e admite variação numérica infinita.
9. **Sentinel-2**: cobrar o **arranjo** (dois satélites simultâneos, 5 dias) e não a identidade dos satélites, que muda; se cobrar a identidade, cobrar a distinção 2A/2C com a data de 21/01/2025, nunca a revisita como se dependesse dela.
10. **NDWI**: qualquer questão sobre NDWI precisa dizer de quem é a fórmula ou dar as bandas. Excelente questão de discriminação: dadas três fórmulas normalizadas, dizer o que cada uma mede.
11. **Kappa**: não criar questão de gabarito fechado que trate o Kappa como métrica pacífica nem como métrica desacreditada — é achado ⚪. Se for cobrado, que seja como questão dissertativa sobre a divergência, ou não seja cobrado.
12. **A matriz de confusão da a05 já está aritmeticamente correta e é reutilizável** — dá para gerar questões novas sobre a mesma tabela (acurácia de produtor e usuário de granito e de solo/vegetação, ainda não calculadas na aula) sem inventar número nenhum.
13. **O exemplo de NDVI ao sol e em sombra da a04 é o melhor exemplo de "por que a razão cancela"** do módulo, e o resultado 0,80 = 0,80 é limpo para questão de cálculo com números novos.

---

## Correções aplicadas

**Aplicadas em:** 2026-09-08 · **Modo:** `audit-and-fix`

| claim_id | Sev. | Desfecho | Arquivos alterados |
|---|---|---|---|
| `SENSREM-M14-A03-FEOXIDO-001` | 🔴 | Corrigido | aula-03 |
| `SENSREM-M14-A07-CHRISTIANSEN-002` | 🔴 | Corrigido | aula-07, modulo |
| `SENSREM-M14-A07-STEFANBOLTZMANN-003` | 🟠 | Corrigido | aula-07, modulo |
| `SENSREM-M14-A07-TIRSB11-004` | 🟠 | Corrigido | aula-07, modulo |
| `SENSREM-M14-A01-COMPOSICAO-005` | 🟠 | Corrigido | aula-01 |
| `SENSREM-M14-A06-BANDALRESOL-006` | 🟠 | Corrigido | aula-06 |
| `SENSREM-M14-A06-LAYOVER-007` | 🟠 | Corrigido | aula-06, modulo |
| `SENSREM-M14-A01-SENTINEL2C-008` | 🟡 | Corrigido | aula-01 |
| `SENSREM-M14-A03-AGUAREFL-009` | 🟡 | Corrigido | aula-03 |
| `SENSREM-M14-A05-KAPPA-010` | ⚪ | Registrado sem escolha de lado | aula-05 |
| `SENSREM-M14-A04-NDWIHOMONIMO-011` | ⚪ | Registrado e explicitado | aula-04 |

**Material derivado a propagar:** **nenhum.** O módulo ainda não tem questionário nem baralho — a auditoria rodou antes deles, como manda a cadeia. Nada a reimportar no Anki.

**Pendências:** nenhuma. `open_findings: []`. Os dois achados ⚪ são registros de divergência real da literatura e de homonímia, tratados no texto conforme a política, e por definição não bloqueiam o gate.
