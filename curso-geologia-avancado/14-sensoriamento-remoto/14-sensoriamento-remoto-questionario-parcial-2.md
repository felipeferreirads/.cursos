# Questionário parcial 2 — Módulo 14: Sensoriamento remoto

**Módulo:** [[14-sensoriamento-remoto-modulo|Módulo 14 — Sensoriamento remoto]]
**Cobertura:** Aulas 04 e 05 — processamento digital de imagens I (pré-processamento, realce de contraste, operações aritméticas entre bandas, filtragem espacial) e II (Análise de Componentes Principais, classificação supervisionada e não supervisionada, matriz de confusão).
**Recorte:** o que se faz com o número depois que a imagem já chegou corrigida — banda a banda e par a par (Aula 04), e depois todas as bandas em conjunto (Aula 05). O comportamento espectral que justifica cada operação já foi estabelecido na parcial 1; aqui o foco é o processamento em si.
**Objetivos avaliados:** `geologia-avancado-m14-oa03` (integral — a04 + a05)
**Pontuação total:** 100 pontos · o gabarito fica oculto; responda antes de abrir.

---

### 1. Múltipla escolha — `geologia-avancado-m14-q11` · oa03 · 10 pts

Uma correção converte o valor digital (DN) bruto de cada pixel numa grandeza física com significado — radiância no topo da atmosfera — compensando diferenças de calibração entre os detectores físicos do sensor. A qual das três correções de pré-processamento isso corresponde?

- a) Correção atmosférica
- b) Correção radiométrica
- c) Correção geométrica (ortorretificação)
- d) Alongamento de contraste

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A **correção radiométrica** é a que ajusta o valor digital bruto para compensar diferenças de calibração entre detectores do sensor e converte o DN em radiância no topo da atmosfera. A **correção atmosférica** vem depois, e remove a contribuição da própria atmosfera (*path radiance*) para estimar reflectância de superfície. A **correção geométrica** ajusta distorções de posição causadas pela geometria de aquisição e amarra a imagem a um sistema de coordenadas. O **alongamento de contraste** (d) não é pré-processamento nem correção — é um realce visual aplicado depois, sobre uma imagem já corrigida, e não altera a informação relativa entre pixels.
</details>

---

### 2. Verdadeiro ou Falso (justifique) — `geologia-avancado-m14-q12` · oa03 · 10 pts

"O alongamento de contraste por equalização de histograma adiciona informação nova à imagem, permitindo distinguir materiais que antes eram espectralmente idênticos."

<details>
<summary>Ver resposta</summary>

**Falso.**

O realce de contraste — seja alongamento linear, seja equalização de histograma — **não adiciona informação nova**: apenas redistribui os valores digitais existentes pela faixa de exibição, tornando diferenças sutis que já estavam presentes nos números visualmente mais perceptíveis ao olho humano. Dois materiais que eram espectralmente idênticos (mesmo valor digital) continuam idênticos depois do realce — o realce não pode criar uma distinção que os dados brutos não continham. É essa mesma razão que faz o realce de contraste não interferir em análises quantitativas posteriores (como um índice espectral): ele muda a **exibição**, não o dado subjacente usado no cálculo.
</details>

---

### 3. Múltipla escolha — `geologia-avancado-m14-q13` · oa03 · 10 pts

Qual das duas operações a seguir cancela algebricamente o efeito de sombra topográfica (queda proporcional de reflectância em todas as bandas de um pixel) — a **razão entre duas bandas**, ou um **filtro de convolução passa-alta** aplicado a uma única banda — e por quê?

- a) O filtro passa-alta, porque realça bordas, incluindo as bordas de uma área em sombra
- b) A razão de bandas, porque um fator multiplicativo comum a ambas as bandas se cancela algebricamente na divisão; o filtro de convolução opera dentro de uma única banda e não tem como cancelar esse efeito
- c) As duas operações cancelam igualmente o efeito de sombra, porque ambas processam valores digitais
- d) Nenhuma das duas cancela o efeito de sombra — isso só é resolvido pela correção atmosférica

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A **razão de bandas** cancela, algebricamente, um fator multiplicativo comum às duas bandas envolvidas: se a sombra reduz ambas as bandas pelo mesmo fator k, a razão (k×A)/(k×B) = A/B, igual à razão sem sombra — é o mecanismo demonstrado no exemplo trabalhado da Aula 04 com o NDVI. O **filtro de convolução** é uma operação inteiramente diferente: opera **dentro de uma única banda**, combinando o valor de cada pixel com o de seus vizinhos por um kernel — não envolve duas bandas nem cancelamento algébrico nenhum; um filtro passa-alta pode realçar a *borda* de uma área em sombra (a transição abrupta de valor), mas não corrige nem cancela a própria redução de reflectância causada pela sombra. "d" está incompleto: a correção atmosférica trata da contribuição da atmosfera (*path radiance*), um problema diferente do efeito de iluminação/sombra topográfica, que a razão de bandas já resolve, sem precisar de correção adicional para esse fim específico.
</details>

---

### 4. Aplicação (cálculo) — `geologia-avancado-m14-q14` · oa03 · 15 pts

Um pixel de vegetação ao sol tem reflectância de banda vermelha = 0,04 e banda NIR = 0,50. O mesmo tipo de vegetação, num ponto vizinho em sombra parcial, recebe apenas 70% da iluminação do pixel ao sol, e as duas bandas caem proporcionalmente. Calcule o NDVI do pixel ao sol e do pixel em sombra, e explique o resultado.

<details>
<summary>Ver resolução</summary>

**Pixel ao sol:**
NDVI = (0,50 − 0,04) / (0,50 + 0,04) = 0,46 / 0,54 = **≈ 0,8519**

**Pixel em sombra (70% da iluminação):**
Vermelho = 0,04 × 0,7 = 0,028; NIR = 0,50 × 0,7 = 0,35
NDVI = (0,35 − 0,028) / (0,35 + 0,028) = 0,322 / 0,378 = **≈ 0,8519**

Os dois pixels produzem exatamente o **mesmo NDVI**, apesar de os valores brutos das duas bandas diferirem em 30% entre eles. O fator de escala 0,7 introduzido pela sombra se cancela algebricamente na razão, do mesmo modo demonstrado no exemplo trabalhado da Aula 04: (0,7×NIR − 0,7×Verm.) / (0,7×NIR + 0,7×Verm.) = 0,7×(NIR−Verm.) / [0,7×(NIR+Verm.)] = (NIR−Verm.)/(NIR+Verm.), o mesmo NDVI de antes. Um analista que julgasse o vigor da vegetação só pela banda NIR bruta concluiria, incorretamente, que a vegetação em sombra está mais fraca — quando a diferença é inteiramente um artefato de iluminação.
</details>

---

### 5. Múltipla escolha — `geologia-avancado-m14-q15` · oa03 · 10 pts

Um relatório menciona "NDWI = 0,62" para um pixel, sem indicar a fórmula usada. Considerando que existem índices homônimos chamados NDWI, o que esse número pode significar?

- a) Necessariamente delineamento de corpo d'água aberto (fórmula de McFeeters), porque NDWI só tem essa definição
- b) Pode ser o índice de McFeeters (Verde−NIR)/(Verde+NIR), que delineia água aberta, ou o índice de Gao (NIR−SWIR)/(NIR+SWIR), que mede água líquida na folha — sem saber quais bandas entraram na fórmula, não é possível interpretar o valor com segurança
- c) É necessariamente o MNDWI de Xu, por ser a formulação mais recente das três
- d) O valor 0,62 só é fisicamente possível na fórmula de Gao, porque a de McFeeters nunca ultrapassa 0,5

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Existem **dois índices distintos chamados NDWI**: o de **McFeeters (1996)**, Verde e NIR, que mede superfície de água aberta, e o de **Gao (1996)**, NIR e SWIR, que mede teor de água líquida **dentro da folha** — um índice de vegetação, não de corpos d'água. Há ainda o **MNDWI de Xu (2006)**, Verde e SWIR, variante do de McFeeters. Como as três fórmulas usam bandas diferentes e medem fenômenos fisicamente distintos, o mesmo rótulo "NDWI" pode se referir a qualquer uma delas — a advertência central da Aula 04 é justamente conferir sempre quais bandas entraram no cálculo antes de supor o que um "NDWI" mede. "a", "c" e "d" atribuem uma definição única ou uma faixa de valor fixa a um termo que é, na prática, ambíguo sem essa verificação.
</details>

---

### 6. Verdadeiro ou Falso (justifique) — `geologia-avancado-m14-q16` · oa03 · 10 pts

"Um lineamento realçado por um filtro de detecção de borda (Sobel ou Prewitt) numa imagem óptica é, por si só, confirmação de uma estrutura geológica — falha, fratura ou contato litológico."

<details>
<summary>Ver resposta</summary>

**Falso.**

Um lineamento realçado por filtro de detecção de borda é **hipótese de controle estrutural, não confirmação**. O mesmo filtro realça igualmente transições abruptas de valor de origem inteiramente não estrutural — limites de uso do solo, estradas, bordas de nuvem residual, artefatos de mosaico entre cenas — e a imagem, por si só, não distingue essas causas de uma feição geológica real. Só a checagem de campo, ou a integração com outros dados independentes (como os produtos ativos das Aulas 06 e 07 — InSAR, LiDAR), separa um lineamento geológico real de um artefato de outra natureza.
</details>

---

### 7. Múltipla escolha — `geologia-avancado-m14-q17` · oa03 · 10 pts

Sobre a Análise de Componentes Principais (ACP) aplicada a uma imagem multiespectral, qual afirmação está correta?

- a) A PC1 sempre corresponde exatamente à litologia dominante da cena, em qualquer imagem processada
- b) A PC1 tipicamente concentra o fator dominante de brilho geral/iluminação, mas qual componente captura qual tipo de informação não é fixo nem previsível de antemão — precisa ser verificado caso a caso, examinando a carga de cada banda original em cada componente
- c) As componentes principais resultantes são sempre correlacionadas entre si, do mesmo modo que as bandas espectrais originais
- d) A ACP seletiva (orientada a feição) sempre usa todas as bandas do sensor, nunca um subconjunto escolhido

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A PC1 costuma capturar o fator dominante de variância comum entre bandas — na maioria das imagens ópticas, esse fator é o brilho geral/iluminação — mas a Aula 05 registra explicitamente que isso é um **padrão comum, não garantido**: qual componente captura qual informação depende da cena específica (cobertura de vegetação, tipos de solo e rocha presentes, condições de iluminação daquela data) e precisa ser verificado examinando a carga de cada banda original em cada componente, não assumido a partir de exemplos de outros trabalhos. "a" trata como certeza universal o que é apenas um padrão frequente; "c" inverte a própria definição da ACP, cujo objetivo é justamente produzir componentes **não correlacionadas** (ortogonais); "d" contradiz a definição de ACP seletiva, que por definição aplica a transformação a um **subconjunto** deliberado de bandas.
</details>

---

### 8. Dissertativa curta — `geologia-avancado-m14-q18` · oa03 · 10 pts

Distinga classificação supervisionada de não supervisionada quanto ao conhecimento prévio exigido, e explique o que significa "rotulação pós-classificação" no contexto do K-means.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:**

A classificação **não supervisionada** (K-means é o algoritmo mais comum) não usa nenhum conhecimento prévio sobre as classes: o algoritmo agrupa os pixels automaticamente por similaridade espectral, em um número de agrupamentos definido a priori pelo analista, de forma iterativa (atribui cada pixel ao centro mais próximo, recalcula os centros, repete até estabilizar). O resultado é um mapa de agrupamentos espectrais **sem rótulo de classe geológica nenhum** — cabe ao analista, depois de rodar o algoritmo, examinar cada agrupamento (localização, assinatura espectral média, contexto de terreno, eventual confirmação de campo) e decidir a que classe temática real ele corresponde: essa etapa posterior é a **rotulação pós-classificação**.

A classificação **supervisionada**, ao contrário, começa com conhecimento prévio: o analista define áreas de treinamento (polígonos ou pontos cuja classe verdadeira já é conhecida, por campo, mapas existentes ou interpretação confiável), e o algoritmo (Máxima Verossimilhança, SVM, Random Forest) aprende a partir dessas amostras a regra que separa uma classe de outra, aplicando-a depois a todos os demais pixels. A não supervisionada é útil quando faltam amostras de treinamento confiáveis, ou como etapa exploratória inicial; a supervisionada é preferível quando já se dispõe de conhecimento de campo suficiente para definir boas áreas de treinamento — que, em qualquer dos dois métodos supervisionados, é o fator que mais determina a qualidade do resultado final.
</details>

---

### 9. Aplicação (cálculo) — `geologia-avancado-m14-q19` · oa03 · 15 pts

Reutilizando a matriz de confusão do exemplo trabalhado da Aula 05 (300 pixels de validação, três classes: Granito, Xisto, Solo/vegetação):

| Verdadeiro \ Classificado | Granito | Xisto | Solo/veg. | Total verdadeiro |
|---|---|---|---|---|
| Granito | 80 | 15 | 5 | 100 |
| Xisto | 10 | 70 | 20 | 100 |
| Solo/veg. | 5 | 5 | 90 | 100 |
| Total classificado | 95 | 90 | 115 | 300 |

A aula calculou a acurácia do produtor e do usuário só para a classe Xisto. Calcule agora a acurácia do **produtor** e do **usuário** para as classes **Granito** e **Solo/vegetação**, e diga qual das três classes tem o melhor desempenho combinado.

<details>
<summary>Ver resolução</summary>

**Granito:**
Acurácia do produtor = pixels verdadeiramente Granito corretamente classificados / total verdadeiramente Granito = 80 / 100 = **80%**
Acurácia do usuário = pixels verdadeiramente Granito entre os classificados como Granito / total classificado como Granito = 80 / 95 = **≈ 84,2%**

**Solo/vegetação:**
Acurácia do produtor = 90 / 100 = **90%**
Acurácia do usuário = 90 / 115 = **≈ 78,3%**

**Comparação:** Granito tem produtor 80% e usuário 84,2%; Xisto (já calculado na aula) tem produtor 70% e usuário 77,8%; Solo/vegetação tem produtor 90% (o mais alto das três) mas usuário 78,3% (mais baixo que Granito, e próximo do de Xisto). Olhando as duas métricas em conjunto, o **Granito** tem o desempenho mais equilibrado e mais alto nas duas dimensões (80%/84,2%), enquanto o Solo/vegetação, apesar da melhor acurácia do produtor, sofre bastante comissão (muitos pixels de Xisto e Granito sendo incorretamente rotulados como Solo/vegetação — 20 do Xisto e 5 do Granito somam os 25 pixels que "vazam" para essa classe). O Xisto continua sendo a classe mais fraca das três em ambas as métricas, confirmando a leitura já feita no exemplo trabalhado: a acurácia global de 80% esconde essa fraqueza específica.
</details>

---

## Gabarito resumido

| Questão | ID | Resposta |
|---|---|---|
| 1 | q11 | b (correção radiométrica: DN → radiância, compensa calibração de detectores) |
| 2 | q12 | Falso (realce não adiciona informação nova, só redistribui valores existentes) |
| 3 | q13 | b (razão de bandas cancela fator multiplicativo comum; filtro de convolução não) |
| 4 | q14 | NDVI sol = NDVI sombra = 0,8519 (fator de sombra se cancela na razão) |
| 5 | q15 | b (NDWI ambíguo: McFeeters verde/NIR água aberta, ou Gao NIR/SWIR água na folha) |
| 6 | q16 | Falso (lineamento por filtro de borda é hipótese, não confirmação) |
| 7 | q17 | b (PC1 tipicamente = brilho, mas não garantido; verificar carga de banda caso a caso) |
| 8 | q18 | ver comentário (não supervisionada agrupa sem classe prévia + rotulação pós-classificação; supervisionada usa amostras de treinamento conhecidas) |
| 9 | q19 | Granito: produtor 80%, usuário 84,2%; Solo/veg.: produtor 90%, usuário 78,3%; Granito tem o melhor desempenho combinado |
