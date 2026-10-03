# Questionário final cumulativo — Módulo 14: Sensoriamento remoto

**Módulo:** [[14-sensoriamento-remoto-modulo|Módulo 14 — Sensoriamento remoto]]
**Cobertura:** Aulas 01 a 07 — módulo completo. As questões priorizam a **integração** entre aulas — inclusive a cadeia completa que o hub aponta como ausente nos exemplos trabalhados individuais — e a discriminação dos **três pares de sinal oposto** identificados pela auditoria científica, que por construção cruzam blocos de aulas: transferência de carga (Aula 03) contra campo cristalino (Aula 03); feição de Christiansen contra bandas de reststrahlen (Aula 07); e Lei de Stefan-Boltzmann contra inversão da Lei de Planck (Aulas 02 e 07).
**Objetivos avaliados:** `geologia-avancado-m14-oa01`, `geologia-avancado-m14-oa02`, `geologia-avancado-m14-oa03`, `geologia-avancado-m14-oa04`
**Pontuação total:** 100 pontos · o gabarito fica oculto; responda antes de abrir.

---

### 1. Dissertativa de síntese — `geologia-avancado-m14-q30` · oa01+oa02+oa03+oa04 · 15 pts

O módulo não tem, nas próprias aulas, um exemplo trabalhado que percorra a cadeia completa das sete aulas sobre uma mesma área — cada exemplo é local ao seu próprio tópico. Construa essa cadeia agora: para uma área de exploração mineral com afloramentos escassos e parte coberta por floresta densa, descreva, em sequência, (a) qual sensor e composição colorida escolher (Aula 01), (b) por que a banda escolhida precisa estar numa janela atmosférica (Aula 02), (c) que feição espectral seria buscada num pixel de solo exposto (Aula 03), (d) que operação tornaria essa feição mais robusta à sombra do relevo (Aula 04), (e) como reduzir a redundância entre bandas antes de classificar (Aula 05), (f) que técnica ativa monitoraria deformação de superfície e qual geraria um modelo de terreno sob a floresta (Aula 06), e (g) que técnica geraria um modelo 3D do afloramento acessível e que assinatura termal poderia indicar composição (Aula 07). Ao final, nomeie os **três pares de conceitos de sinal oposto** deste módulo e explique por que cada um é, especificamente, uma armadilha de gabarito invertido.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada (aceita variação razoável em cada etapa, desde que a cadeia e os três pares estejam corretos):**

**(a)** Um sensor com bandas SWIR (Landsat 8/9 ou ASTER) numa composição de falsa cor que leve o SWIR aos canais principais (como 7-6-4 ou 7-6-2 no Landsat), porque é lá que estão as feições diagnósticas de alteração hidrotermal.

**(b)** A banda precisa estar numa janela atmosférica (por exemplo, em torno de 2,1-2,2 µm) porque fora dela a atmosfera absorve a radiação antes de chegar ao sensor — não há sinal de superfície para captar.

**(c)** No pixel de solo exposto, buscar a feição vibracional estreita em 2,16-2,20 µm (caulinita) e, separadamente, a feição eletrônica de campo cristalino em 0,87-0,92 µm, cuja posição discriminaria hematita (~0,86 µm) de goethita (~0,90-0,92 µm) — não a cor do solo, que vem de outro mecanismo (transferência de carga).

**(d)** Uma razão de bandas (ou um índice espectral), porque o fator multiplicativo introduzido pela sombra topográfica se cancela algebricamente na divisão.

**(e)** Análise de Componentes Principais, idealmente ACP seletiva sobre o subconjunto de bandas SWIR relevantes, concentrando a transformação onde a informação mineral diagnóstica está antes de classificar.

**(f)** InSAR monitoraria deformação de superfície (por exemplo, subsidência associada a lavra); LiDAR geraria o modelo de terreno sob a floresta, via retorno múltiplo (retenção do último retorno classificado como solo) — coisa que a fotogrametria óptica não consegue.

**(g)** Fotogrametria SfM por VANT, com GCPs, geraria o modelo 3D do afloramento acessível (ortomosaico e nuvem de pontos densa); uma imagem termal buscaria o deslocamento da feição de Christiansen (não das bandas de reststrahlen) para inferir grau de polimerização/composição félsica-máfica da rocha exposta.

**Os três pares de sinal oposto:**

1. **Transferência de carga (UV, ~0,25 µm, dá a cor) × campo cristalino (0,87-0,92 µm, discrimina hematita de goethita)** — a armadilha é atribuir a cor à feição errada e o discriminador mineralógico ao mecanismo errado.
2. **Feição de Christiansen (máximo de emissividade, 7-9 µm) × bandas de reststrahlen (mínimos de emissividade, 8-12 µm)** — a armadilha é descrever a feição nomeada com a propriedade da outra.
3. **Lei de Stefan-Boltzmann (emissão total, M=εσT⁴) × inversão da Lei de Planck (converte radiância de uma banda em temperatura)** — a armadilha é nomear a lei errada como a que faz a conversão que um sensor termal realmente precisa fazer.

Cada par é perigoso especificamente porque são **nomes próprios pareados**: um flashcard do tipo "o que é a feição de Christiansen?" nasce com o verso exatamente invertido se o autor confundir os dois lados do par — o mesmo mecanismo de erro em todos os três casos, aplicado a mecanismos físicos diferentes.
</details>

---

### 2. Múltipla escolha integrada — `geologia-avancado-m14-q31` · oa01+oa04 · 10 pts

Associe corretamente o mecanismo físico à faixa espectral e ao papel diagnóstico de cada uma das três feições a seguir: (i) a feição de 0,87-0,92 µm em óxidos de ferro; (ii) a feição de Christiansen; (iii) as bandas de reststrahlen.

- a) (i) transferência de carga, discrimina hematita de goethita; (ii) mínimo de emissividade; (iii) máximo de emissividade
- b) (i) campo cristalino do Fe³⁺, discrimina hematita (~0,86 µm) de goethita (~0,90-0,92 µm); (ii) máximo de emissividade (7-9 µm); (iii) mínimo de emissividade (vibrações Si-O, 8-12 µm)
- c) (i) campo cristalino, responsável pela cor avermelhada do solo; (ii) mínimo de emissividade; (iii) máximo de emissividade
- d) (i) transferência de carga, no infravermelho próximo; (ii) máximo de emissividade; (iii) máximo de emissividade

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A feição de 0,87-0,92 µm é uma transição de **campo cristalino** do Fe³⁺ (não transferência de carga, que fica no UV, ~0,25 µm), e sua posição discrimina hematita de goethita. A feição de **Christiansen** é um **máximo** de emissividade, entre 7 e 9 µm. As bandas de **reststrahlen** são os **mínimos** de emissividade, entre 8 e 12 µm. "a" inverte o mecanismo do item (i) e os sinais dos itens (ii) e (iii); "c" mantém o mecanismo certo em (i) mas atribui a ele a cor (que é da transferência de carga) e inverte (ii) e (iii); "d" erra o mecanismo de (i) e trata (ii) e (iii) como se tivessem o mesmo sinal, quando são opostos por definição.
</details>

---

### 3. Verdadeiro ou Falso (justifique) — `geologia-avancado-m14-q32` · oa04 · 10 pts

"Como a Lei de Stefan-Boltzmann e a inversão da Lei de Planck descrevem, cada uma, aspectos da emissão termal de um corpo, qualquer uma das duas pode ser usada para converter a radiância medida por um sensor numa única banda termal em temperatura de superfície."

<details>
<summary>Ver resposta</summary>

**Falso.**

As duas leis têm papéis distintos e **não são intercambiáveis** para essa finalidade. A Lei de Stefan-Boltzmann (M = εσT⁴) descreve a exitância radiante **integrada em todos os comprimentos de onda** — uma grandeza que nenhum sensor de banda estreita mede diretamente. Um sensor termal mede radiância espectral **dentro de uma banda**, e só a **inversão da Lei de Planck** relaciona essa radiância de banda específica à temperatura (produzindo a temperatura de brilho). Usar Stefan-Boltzmann para essa conversão produziria um resultado fisicamente incorreto, porque essa lei nunca foi formulada para uma fatia estreita do espectro — é precisamente essa confusão que a auditoria científica deste módulo identificou e corrigiu na Aula 07.
</details>

---

### 4. Aplicação integrada — `geologia-avancado-m14-q33` · oa02+oa04 · 10 pts

Um alvo de deformação superficial tem 25 m de extensão no menor eixo. Um sensor óptico como o Landsat 9 (30 m de resolução espacial) e um SAR hipotético de 8 m de resolução espacial estão disponíveis para monitorar essa área. (a) Aplicando a regra de 3-5 pixels da Aula 01, qual dos dois sensores resolve espacialmente esse alvo como uma feição distinta na imagem de amplitude? (b) Independentemente dessa resolução espacial de amplitude, por que a técnica InSAR (Aula 06), usando esse mesmo SAR, poderia detectar e **medir** a deformação do alvo mesmo que ele não formasse uma feição claramente reconhecível na imagem de amplitude?

<details>
<summary>Ver resolução</summary>

**(a)** Landsat: 25 m ÷ 30 m < 1 pixel — o alvo é menor que um único pixel, **totalmente inviável** de resolver como feição distinta. SAR hipotético: 25 m ÷ 8 m ≈ 3,1 pixels — no limite inferior da regra de 3-5 pixels, portanto **mapeável**, ainda que de forma marginal.

**(b)** A medição de deformação por InSAR não depende de "enxergar" o contorno do alvo como um objeto visualmente distinto na imagem de **amplitude** — ela usa a **fase** da onda retroespalhada, comparada pixel a pixel entre duas datas. Cada pixel individual, mesmo sem formar uma feição reconhecível isoladamente, registra sua própria diferença de fase se a superfície ali se deslocou ao longo da linha de visada do radar, com sensibilidade de milímetros a centímetros — muito além do que a resolução espacial de amplitude sozinha permitiria supor. A única exigência física adicional é **coerência** de retroespalhamento suficiente entre as duas aquisições; a resolução espacial do sensor define o tamanho do menor pixel individualmente mensurável, não o tamanho mínimo de uma área para ser detectada como deformada.
</details>

---

### 5. Dissertativa curta integrada — `geologia-avancado-m14-q34` · oa01+oa03 · 10 pts

Um analista aplica ACP seletiva (Aula 05) sobre as bandas SWIR de uma cena para realçar argilominerais, mas não verifica antes, nas curvas espectrais da Aula 03, se a caulinita e a esmectita têm feições sobrepostas na mesma faixa espectral. Explique por que essa omissão pode comprometer a interpretação da componente resultante.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:**

A Aula 03 mostra que a caulinita tem feição dupla característica em ~2,16-2,20 µm, e a esmectita/montmorilonita tem feição mais larga e assimétrica próxima de ~2,20 µm — duas posições **muito próximas**, dentro da mesma faixa geral do SWIR. A ACP seletiva, por definição, concentra a transformação exatamente no subconjunto de bandas escolhido — mas ela não sabe, por si só, distinguir qual mineral específico está causando a variância capturada numa dada componente; ela apenas reorganiza a informação estatística presente nas bandas de entrada. Se as bandas escolhidas não têm resolução espectral suficiente para separar as feições próximas de caulinita e esmectita (um problema mais grave em sensores multiespectrais de bandas largas do que em hiperespectrais, conforme a própria Aula 03 explica), a componente resultante pode misturar sinal dos dois minerais, e o analista que assumir "esta componente é caulinita" sem verificar essa sobreposição corre o risco de atribuir a um mineral um sinal que na verdade vem de dois, ou predominantemente do outro. A lição de fundo, comum às Aulas 03 e 05: uma técnica de processamento (ACP) só produz interpretação mineral confiável quando calibrada pelo conhecimento prévio de quais feições espectrais realmente existem — e onde elas podem se confundir — no material que está sendo mapeado.
</details>

---

### 6. Verdadeiro ou Falso (justifique) — `geologia-avancado-m14-q35` · oa03+oa04 · 10 pts

"Um lineamento realçado por filtro de detecção de borda (Aula 04) numa imagem óptica e uma franja de deformação num interferograma InSAR (Aula 06) têm o mesmo grau de confiabilidade como evidência de estrutura geológica, porque ambos são produtos de processamento digital de um sensor remoto."

<details>
<summary>Ver resposta</summary>

**Falso.**

As duas evidências têm natureza epistemológica diferente, apesar de ambas serem produtos de processamento digital. Um lineamento de filtro de borda é, por definição, **hipótese de controle estrutural, não confirmação**: o mesmo filtro realça igualmente artefatos de origem não geológica (estradas, bordas de uso do solo, mosaico de cenas) com exatamente a mesma aparência visual de um traço estrutural real — a imagem óptica, sozinha, não distingue as duas causas. Uma franja InSAR, por outro lado, mede uma grandeza física direta — a diferença de fase da onda retroespalhada entre duas datas —, e essa diferença de fase **só** existe (acima do nível de ruído, com coerência suficiente) se a superfície de fato se deslocou ao longo da linha de visada; não há um "artefato de fase" espectralmente indistinguível de deslocamento real da mesma forma que uma estrada é indistinguível de uma falha para um filtro de borda. Isso não torna o InSAR imune a interpretação errada (a ambiguidade de causa raiz — subsidência de mina versus tectônica versus compactação de bacia — ainda exige contexto, como no exemplo trabalhado da Aula 06), mas a natureza da evidência de base é mais direta fisicamente do que a de um realce de borda óptico.
</details>

---

### 7. Aplicação (cálculo) integrada — `geologia-avancado-m14-q36` · oa03+oa01 · 10 pts

Um pixel sobre uma possível anomalia geobotânica tem reflectância: banda Vermelho = 0,04, banda NIR = 0,38, banda Verde = 0,06. Calcule o NDVI e o NDWI de McFeeters desse pixel, e diga o que os dois valores, em conjunto, sugerem sobre a cobertura desse pixel (vegetação, solo exposto ou água).

<details>
<summary>Ver resolução</summary>

**NDVI** = (NIR − Vermelho) / (NIR + Vermelho) = (0,38 − 0,04) / (0,38 + 0,04) = 0,34 / 0,42 = **≈ 0,8095**

**NDWI (McFeeters)** = (Verde − NIR) / (Verde + NIR) = (0,06 − 0,38) / (0,06 + 0,38) = −0,32 / 0,44 = **≈ −0,7273**

Os dois valores são **consistentes entre si e apontam na mesma direção**: um NDVI alto e positivo (0,81), na faixa típica de vegetação densa e vigorosa (0,6-0,9, segundo a Aula 04), indica alta reflectância no NIR em relação ao vermelho — assinatura de vegetação sadia. O NDWI fortemente negativo (−0,73) confirma que o pixel **não é água** (água produziria NDWI alto e positivo) — é exatamente o padrão esperado para vegetação, o inverso do de água, conforme a Aula 04 descreve. A leitura conjunta: este é um pixel de **vegetação sadia**, não solo exposto (que teria NDVI próximo de zero) nem água. Se o objetivo fosse investigar estresse geobotânico, esses valores sozinhos não indicam anomalia — seria preciso comparar com valores de referência da vegetação circundante e verificar deslocamento de borda vermelha, conforme a Aula 03.
</details>

---

### 8. Múltipla escolha integrada — `geologia-avancado-m14-q37` · oa01+oa02 · 10 pts

Uma composição em cor verdadeira (bandas 4-3-2 do Landsat) de uma área laterítica mostra solo avermelhado uniforme, sem variação visível de cor. Um colega conclui que não há como diferenciar hematita de goethita remotamente nessa área sem amostragem física. Ele está certo?

- a) Certo — a cor é a única forma de diferenciar os dois minerais remotamente, e se ela é uniforme, não há mais informação a extrair
- b) Errado — a diferenciação usa a posição da feição eletrônica de campo cristalino em 0,87-0,92 µm (hematita ~0,86 µm, goethita ~0,90-0,92 µm), não a cor (que vem de outro mecanismo, a transferência de carga no ultravioleta); um sensor com resolução espectral adequada nessa faixa permitiria a distinção
- c) Errado — basta usar qualquer composição SWIR do Landsat, porque o SWIR já contém a mesma informação da feição de 0,87 µm
- d) Certo, porque a transferência de carga também discrimina hematita de goethita, e ela já foi verificada pela cor uniforme

<details>
<summary>Ver resposta</summary>

**Resposta: b**

O colega confunde os dois mecanismos que a Aula 03 separa deliberadamente: a **cor** vem da cauda de uma banda de transferência de carga no ultravioleta, e é um sinal amplo e pouco específico — dois solos com mineralogia de óxido de ferro diferente podem ter cor visualmente muito parecida. O **discriminador real** entre hematita e goethita é a posição da feição eletrônica de **campo cristalino**, em 0,87-0,92 µm — infravermelho próximo, fora do visível, portanto invisível numa composição de cor verdadeira, mas acessível a um sensor com resolução espectral suficiente nessa faixa (hiperespectral, ou multiespectral bem posicionado). "c" erra porque a faixa de 0,87-0,92 µm é infravermelho próximo, não SWIR — bandas SWIR (1,3-3 µm) não cobrem essa feição específica. "d" erra ao atribuir à transferência de carga o poder discriminador que só a feição de campo cristalino tem.
</details>

---

### 9. Dissertativa curta integrada — `geologia-avancado-m14-q38` · oa04 · 10 pts

O objetivo da aula 07 pede situar as três técnicas de geração de modelo tridimensional do módulo — InSAR/MDE por curvas de nível, LiDAR e fotogrametria SfM — por seus pontos fortes e limitações relativas. Faça essa comparação em três ou quatro frases, indicando quando cada uma é a escolha natural.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:**

O **InSAR** não gera propriamente um modelo de terreno detalhado a partir do zero (embora sirva de base histórica para modelos como o SRTM quando não há deslocamento entre datas) — sua força real é medir **deformação** de superfície ao longo do tempo, com precisão de milímetros a centímetros, mas só em áreas de coerência suficiente (superfícies relativamente estáveis; vegetação que muda rapidamente degrada a técnica). O **LiDAR** é a escolha natural para gerar um **Modelo Digital de Terreno de alta resolução sob vegetação densa**, porque seus múltiplos retornos por pulso conseguem separar o eco do solo do eco do dossel — algo que nenhuma das outras duas técnicas replica. A **fotogrametria SfM** é a escolha mais acessível e de menor custo para modelar **superfícies expostas e texturizadas com alto detalhe** (afloramentos, taludes, frentes de lavra), produzindo também um ortomosaico de altíssima resolução — mas, sendo óptica passiva, não penetra vegetação nem funciona bem sobre superfícies homogêneas sem textura (água parada, neve lisa). Em resumo: LiDAR vence sob dossel, SfM vence em detalhe de superfície exposta a baixo custo, e InSAR vence em medir mudança ao longo do tempo — nenhuma substitui as outras duas nos seus respectivos domínios.
</details>

---

### 10. Dissertativa de encerramento — `geologia-avancado-m14-q39` · oa01+oa02+oa03+oa04 · 5 pts

O objetivo declarado deste módulo é "interpretar imagens de sensores ópticos, ativos e termais e aplicar processamento digital e classificação para extrair informação geológica e ambiental". Em duas ou três frases, explique como as sete aulas, em conjunto, cumprem essa promessa — e por que nenhuma técnica isolada deste módulo, sozinha, entrega uma resposta geológica confiável.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada (síntese, não fatos novos):**

O vocabulário e a escolha de sensor (Aula 01) e a física da radiação e da atmosfera (Aula 02) estabelecem o que uma imagem pode e não pode captar; as assinaturas espectrais de água, solo, mineral e vegetação (Aula 03) dão significado composicional a esses números; o processamento digital, banda a banda e depois em conjunto (Aulas 04 e 05), extrai e realça essa informação e a converte em mapa temático; os sensores ativos (Aula 06) rompem a dependência de luz e nuvens e acrescentam medição de deformação e de terreno sob vegetação; e a fotogrametria e o termal (Aula 07) fecham com modelagem 3D e leitura de temperatura e composição por emissividade. Nenhuma técnica isolada é suficiente porque cada uma tem uma limitação estrutural própria — um lineamento de filtro de borda é hipótese, não confirmação; uma classificação supervisionada só é tão boa quanto suas amostras de treinamento; um sinal geobotânico é sempre indireto; uma leitura termal única mistura temperatura, emissividade e efeito de iluminação — e é a combinação de evidências independentes, integrada com verificação de campo, que transforma uma imagem em informação geológica confiável, nunca uma imagem sozinha.
</details>

---

## Gabarito resumido

| Questão | ID | Resposta |
|---|---|---|
| 1 | q30 | ver comentário (cadeia integrada a01-a07 sobre uma mesma área; os três pares de sinal oposto nomeados) |
| 2 | q31 | b (campo cristalino discrimina hematita/goethita; Christiansen = máximo; reststrahlen = mínimos) |
| 3 | q32 | Falso (Stefan-Boltzmann é emissão total; só a inversão de Planck converte radiância de banda em temperatura) |
| 4 | q33 | Landsat <1 pixel (inviável); SAR ≈3,1 pixels (mapeável); InSAR mede deformação por fase, independente da resolução de amplitude |
| 5 | q34 | ver comentário (caulinita e esmectita têm feições próximas em ~2,2 µm; ACP seletiva não separa minerais sem resolução espectral suficiente) |
| 6 | q35 | Falso (lineamento óptico é hipótese; franja InSAR mede grandeza física direta de deslocamento) |
| 7 | q36 | NDVI ≈ 0,81 (vegetação); NDWI ≈ −0,73 (não água); pixel de vegetação sadia |
| 8 | q37 | b (discriminador é a posição de campo cristalino em 0,87-0,92 µm, não a cor; feição é NIR, não SWIR) |
| 9 | q38 | ver comentário (LiDAR vence sob dossel; SfM vence em detalhe de superfície exposta; InSAR vence em medir deformação) |
| 10 | q39 | ver comentário (síntese das sete aulas; nenhuma técnica isolada é suficiente sem integração e verificação de campo) |
