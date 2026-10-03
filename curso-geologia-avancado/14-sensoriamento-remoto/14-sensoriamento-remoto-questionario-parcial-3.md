# Questionário parcial 3 — Módulo 14: Sensoriamento remoto

**Módulo:** [[14-sensoriamento-remoto-modulo|Módulo 14 — Sensoriamento remoto]]
**Cobertura:** Aulas 06 e 07 — sensoriamento remoto ativo (Radar/SAR, InSAR, LiDAR) e fotogrametria digital, produtos 3D e sensoriamento remoto termal (TIR).
**Recorte:** as técnicas que rompem a dependência de luz solar e de nuvens (sensores ativos) e a reconstrução tridimensional e térmica de superfície — o bloco de maior densidade de mecanismos físicos distintos do módulo, e onde estão dois dos três pares de sinal oposto mais críticos (Christiansen/reststrahlen e Stefan-Boltzmann/Planck).
**Objetivos avaliados:** `geologia-avancado-m14-oa04` (integral — a06 + a07)
**Pontuação total:** 100 pontos · o gabarito fica oculto; responda antes de abrir.

---

### 1. Múltipla escolha — `geologia-avancado-m14-q20` · oa04 · 10 pts

Por que sistemas SAR em banda L (comprimento de onda maior, ~15-30 cm) costumam entregar resolução espacial mais grosseira do que sistemas em banda X (~2,4-3,8 cm), se a resolução em azimute de um SAR estripe (≈ D/2, metade do comprimento físico da antena) é, notavelmente, independente do comprimento de onda?

- a) Porque o comprimento de onda maior reduz diretamente a resolução azimutal, já que Lₛ = λR/D
- b) Por restrições práticas de engenharia e de regulação — a antena física precisa ser maior para produzir um feixe utilizável em λ maior, e a largura de banda disponível/alocada (que fixa a resolução em alcance) é menor nas faixas baixas do espectro de radar — não por consequência direta da física da abertura sintética
- c) Porque sistemas em banda L não conseguem sintetizar abertura alguma, ao contrário dos de banda X
- d) Porque a resolução azimutal de qualquer SAR é sempre numericamente igual à resolução em alcance

<details>
<summary>Ver resposta</summary>

**Resposta: b**

O λ se **cancela algebricamente** na resolução azimutal (≈ D/2): um λ maior obriga a sintetizar uma abertura proporcionalmente mais longa (Lₛ = λR/D), e esse alongamento compensa exatamente o efeito do comprimento de onda maior — a resolução final não depende de λ. O que de fato torna sistemas em banda L mais grosseiros são **duas limitações práticas**: a antena física precisa ser maior para produzir um feixe utilizável nesse comprimento de onda, e a largura de banda disponível nas faixas baixas do espectro de radar (que é o que fixa a resolução em alcance, uma dimensão diferente da azimutal) tende a ser menor. "a" reproduz exatamente a regra falsa que a auditoria científica deste módulo identificou e corrigiu: tratar o λ como determinante direto da resolução azimutal, quando ele se cancela na fórmula.
</details>

---

### 2. Aplicação (cálculo) — `geologia-avancado-m14-q21` · oa04 · 10 pts

Um SAR tem ângulo de incidência θ = 35°. Uma encosta voltada para o radar tem declividade α = 42°, e a encosta oposta (voltada para longe do radar) tem declividade de 58°. Classifique a distorção geométrica esperada em cada uma das duas encostas, mostrando a comparação angular usada.

<details>
<summary>Ver resolução</summary>

**Encosta voltada para o radar (α = 42°):** compara-se α com θ. Como α (42°) > θ (35°), a condição é de **inversão de relevo (layover)** — o topo da elevação está, em distância inclinada até o sensor, mais perto do radar do que sua própria base, e a imagem processada posiciona o topo "deitado" sobre a base.

**Encosta oposta (α = 58°):** compara-se com 90° − θ = 90° − 35° = **55°**. Como a declividade (58°) supera esse limiar (55°), a condição é de **sombra de radar** — a encosta é mais íngreme que o ângulo de depressão do feixe e bloqueia completamente o sinal de alcançar a área imediatamente atrás dela, criando uma faixa sem retorno.

O mesmo θ = 35° produz, portanto, distorções diferentes nas duas encostas da mesma feição topográfica, dependendo apenas da declividade local — exatamente o mecanismo que o hub do módulo aponta como a armadilha central desta aula.
</details>

---

### 3. Verdadeiro ou Falso (justifique) — `geologia-avancado-m14-q22` · oa04 · 10 pts

"Encurtamento de rampa e inversão de relevo (layover) são dois fenômenos fisicamente distintos, sem relação entre si."

<details>
<summary>Ver resposta</summary>

**Falso.**

Encurtamento de rampa e layover são o **mesmo fenômeno dos dois lados de um único limiar**, α = θ (declividade igual ao ângulo de incidência) — não dois fenômenos independentes. Enquanto α < θ, a encosta voltada para o radar sofre encurtamento (aparece comprimida e mais clara); no caso-limite α = θ, ela colapsa numa única linha brilhante; e quando α > θ, o mesmo mecanismo geométrico se intensifica até o ponto de o eco do topo chegar ao sensor antes do eco da base — o layover. A sombra de radar, por sua vez, **não** é o "oposto" desses dois: é um terceiro caso, que ocorre na encosta oposta e se mede contra um ângulo diferente (90° − θ), não contra θ diretamente.
</details>

---

### 4. Aplicação (cálculo) — `geologia-avancado-m14-q23` · oa04 · 10 pts

Um interferograma Sentinel-1 (banda C, λ ≈ 5,6 cm) entre duas datas separadas por 24 dias mostra 2,0 ciclos completos de franja sobre uma barragem de rejeito, sem franjas significativas na área ao redor. Calcule o deslocamento de superfície ao longo da linha de visada do radar nesse período.

<details>
<summary>Ver resolução</summary>

Cada ciclo completo de franja corresponde a metade do comprimento de onda do radar, porque o sinal percorre o trajeto sensor-alvo-sensor duas vezes:

Deslocamento por franja = λ/2 = 5,6 cm / 2 = **2,8 cm**

Deslocamento total = 2,0 × 2,8 cm = **5,6 cm** ao longo da linha de visada, em 24 dias.

Uma taxa dessa ordem — mais de 5 cm em menos de um mês — sobre uma estrutura de contenção como uma barragem de rejeito é motivo de investigação geotécnica imediata, não apenas monitoramento passivo continuado, pelo mesmo raciocínio do exemplo trabalhado da Aula 06 sobre subsidência de mina: o InSAR não substitui a investigação de campo, mas aponta com precisão onde ela é mais urgente.
</details>

---

### 5. Múltipla escolha — `geologia-avancado-m14-q24` · oa04 · 10 pts

Para gerar um Modelo Digital de Terreno (MDT) sob dossel florestal denso a partir de dados LiDAR aerotransportado, qual retorno de pulso deve ser retido, e por quê?

- a) O primeiro retorno, porque representa o topo do dossel, mais próximo do sensor
- b) O último retorno classificado como solo, porque é o que, na maioria dos pulsos que conseguem atravessar as aberturas da vegetação, reflete finalmente no terreno nu
- c) Qualquer retorno serve igualmente, já que todos representam a mesma superfície física
- d) O retorno intermediário, porque corresponde à média estatística entre o topo do dossel e o solo

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Cada pulso de laser pode gerar múltiplos ecos: parte da energia reflete no topo do dossel (**primeiro retorno**), parte em vegetação intermediária, e a fração que atravessa toda a vegetação reflete finalmente no solo (**último retorno**, quando classificado como tal). Para gerar um MDT — a superfície do terreno nu, sem vegetação — é preciso filtrar a nuvem de pontos para reter **apenas os últimos retornos classificados como solo**, descartando os demais. "a" descreve o procedimento para gerar um Modelo Digital de **Superfície** (MDS, que inclui o topo do dossel), não o MDT; "c" ignora que os retornos representam alturas fisicamente diferentes; "d" descreve um procedimento que não corresponde a nenhuma das categorias de classificação de retorno usadas na prática.
</details>

---

### 6. Dissertativa curta — `geologia-avancado-m14-q25` · oa04 · 10 pts

Explique por que a fotogrametria digital SfM (Aula 07) não substitui o LiDAR (Aula 06) para gerar um modelo de terreno em área de vegetação densa, relacionando a limitação com o princípio físico em que a SfM se baseia.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:**

A SfM é, na origem, uma técnica **óptica passiva**: reconstrói geometria a partir de correspondência de feições visuais (pontos-chave) entre múltiplas fotografias sobrepostas — ela só consegue reconstruir **superfícies visíveis e texturizadas** na imagem. Sob dossel florestal denso, a câmera enxerga apenas o topo da vegetação; não há como identificar pontos-chave do solo em fotografias que simplesmente não o registram, porque a luz visível não atravessa a copa das árvores da mesma forma que um pulso de laser consegue passar pelas aberturas do dossel. O LiDAR resolve esse problema por um mecanismo físico completamente diferente — o **retorno múltiplo**: parte da energia de cada pulso penetra pelas aberturas do dossel e retorna do solo, permitindo separar, por classificação dos ecos, o que é vegetação do que é terreno nu. A SfM não tem equivalente a essa capacidade de "ver através" da vegetação, porque depende inteiramente de uma superfície opticamente visível para triangular — e é exatamente essa diferença de princípio físico, não uma limitação de qualidade de processamento, que faz o LiDAR ser a técnica de referência para MDT sob floresta densa, enquanto a SfM permanece limitada a superfícies expostas e texturizadas.
</details>

---

### 7. Verdadeiro ou Falso (justifique) — `geologia-avancado-m14-q26` · oa04 · 10 pts

"Sem pontos de controle no solo (GCPs), um modelo SfM fica geometricamente distorcido internamente — feições próximas ficam desproporcionais entre si dentro do próprio modelo."

<details>
<summary>Ver resposta</summary>

**Falso.**

Sem GCPs, o SfM reconstrói corretamente a **geometria relativa** da cena — formas e proporções internas entre feições próximas ficam consistentes entre si — porque essa reconstrução depende apenas da triangulação entre pontos-chave nas próprias fotografias, um processo que não exige nenhuma referência de coordenadas externa. O que falta, sem GCPs, é a amarração dessa geometria correta a um **sistema de coordenadas real**: o modelo inteiro pode estar deslocado, rotacionado, ou com uma escala global levemente distorcida em relação ao mundo real — um erro sistemático que afeta o modelo como um todo, não as proporções internas entre suas partes. É o mesmo tipo de erro sutil e silencioso discutido para georreferenciamento em geral no Módulo 13: o modelo "parece" correto, mas não está amarrado ao lugar certo.
</details>

---

### 8. Múltipla escolha — `geologia-avancado-m14-q27` · oa04 · 10 pts

Um sensor termal mede radiância espectral na banda 10 do TIRS (10,60-11,19 µm), e um analista precisa convertê-la em temperatura de superfície. Qual relação física deve ser usada para essa conversão, e por quê?

- a) A Lei de Stefan-Boltzmann (M = εσT⁴), porque ela relaciona diretamente emissividade e temperatura
- b) A inversão da Lei de Planck, porque a Lei de Stefan-Boltzmann descreve a emissão **total**, integrada em todos os comprimentos de onda, enquanto o sensor mede radiância **dentro de uma banda espectral estreita**
- c) As duas leis são equivalentes para esse propósito e podem ser usadas indistintamente
- d) Nenhuma das duas — a conversão de radiância de banda em temperatura usa exclusivamente a Lei de Wien

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A **Lei de Stefan-Boltzmann** (M = εσT⁴) descreve a exitância radiante **total**, somada sobre todos os comprimentos de onda — ela não diz quanto de radiância um sensor mede numa banda específica. Um sensor termal, como o TIRS na banda 10, mede **radiância espectral dentro de uma faixa estreita**, e a relação que dá essa grandeza para cada temperatura é a **Lei de Planck** — a conversão é feita **invertendo** essa lei, produzindo o que se chama temperatura de brilho. Confundir as duas leis foi exatamente o erro que a auditoria científica deste módulo corrigiu na Aula 07: nomear Stefan-Boltzmann como a relação que converte a medida do sensor em temperatura, quando ela descreve a emissão total, não a radiância de banda.
</details>

---

### 9. Verdadeiro ou Falso (justifique) — `geologia-avancado-m14-q28` · oa04 · 10 pts

"A feição de Christiansen, entre 7 e 9 µm, é um mínimo de emissividade — o mesmo tipo de feição que as bandas de reststrahlen, entre 8 e 12 µm."

<details>
<summary>Ver resposta</summary>

**Falso.**

São feições de **sinal oposto**, e não devem ser confundidas. A **feição de Christiansen** é um **máximo** de emissividade (correspondentemente, um mínimo de reflectância), que aparece onde o índice de refração do material se aproxima do índice do meio ao redor, tipicamente entre 7 e 9 µm. As **bandas de reststrahlen**, ao contrário, são os **mínimos** de emissividade, produzidos pelas vibrações fundamentais de estiramento das ligações Si-O, na faixa de ~8 a 12 µm — são elas as "feições de absorção" no sentido usual do termo. Tratar a feição de Christiansen como mínimo foi exatamente o erro vermelho que a auditoria científica deste módulo corrigiu na Aula 07, fundindo as duas feições e atribuindo à nomeada a propriedade da outra.
</details>

---

### 10. Aplicação — `geologia-avancado-m14-q29` · oa04 · 10 pts

Um analista quer aplicar o algoritmo de janela dividida (*split-window*), usando as bandas 10 e 11 do TIRS (Landsat 8/9), para estimar temperatura de superfície com correção atmosférica embutida, num estudo quantitativo de anomalia térmica numa pilha de rejeito. Essa escolha é recomendada? Justifique com base na calibração do sensor.

<details>
<summary>Ver resolução</summary>

**Não é recomendada.** A banda 11 do TIRS tem incerteza radiométrica residual muito maior do que a banda 10, causada por luz espúria (*stray light*) captada de fora do campo de visão do telescópio. Mesmo depois do algoritmo de correção implementado na cadeia de processamento em fevereiro de 2017, a variabilidade residual da banda 11 permanece da ordem de **1,7 K**, e o **USGS recomenda explicitamente que os usuários evitem a banda 11 em análise quantitativa — incluindo justamente as técnicas de janela dividida**, que dependem da diferença de absorção atmosférica entre as duas bandas para funcionar corretamente.

O caminho recomendado para o Landsat 8/9 é um método de **canal único** aplicado sobre a banda 10, com correção atmosférica e emissividade fornecidas separadamente — não porque o princípio da janela dividida esteja errado (ele segue sendo o método de escolha em sensores cujas duas bandas termais são igualmente confiáveis, como o MODIS), mas porque, neste sensor específico, uma de suas duas bandas termais não tem a qualidade radiométrica necessária para sustentar a técnica. Ignorar essa ressalva operacional e aplicar janela dividida ao TIRS introduziria erro sistemático justamente na banda mais suscetível — uma armadilha específica de calibração de instrumento, não de raciocínio físico.
</details>

---

## Gabarito resumido

| Questão | ID | Resposta |
|---|---|---|
| 1 | q20 | b (resolução azimutal independe de λ; banda L mais grosseira por antena maior e menor largura de banda disponível) |
| 2 | q21 | encosta voltada: α(42°)>θ(35°) → layover; encosta oposta: 58°>55°(90°−θ) → sombra de radar |
| 3 | q22 | Falso (encurtamento e layover são o mesmo fenômeno dos dois lados do limiar α=θ; sombra é um terceiro caso) |
| 4 | q23 | 2,0 × 2,8 cm = 5,6 cm ao longo da linha de visada em 24 dias |
| 5 | q24 | b (último retorno classificado como solo → MDT sob dossel) |
| 6 | q25 | ver comentário (SfM é óptica passiva, não penetra vegetação; LiDAR separa solo por retorno múltiplo) |
| 7 | q26 | Falso (sem GCP a geometria relativa é correta; falta é amarração ao sistema de coordenadas real) |
| 8 | q27 | b (inversão de Planck converte radiância de banda em temperatura; Stefan-Boltzmann é emissão total) |
| 9 | q28 | Falso (Christiansen = máximo de emissividade; reststrahlen = mínimos) |
| 10 | q29 | Não recomendada (banda 11 tem incerteza residual ~1,7 K; USGS desaconselha em análise quantitativa; usar canal único na banda 10) |
