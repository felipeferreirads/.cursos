# Questionário parcial 1 — Módulo 08: Geotecnia ambiental

**Módulo:** [[08-geotecnia-ambiental-modulo|Módulo 08 — Geotecnia ambiental]]
**Cobertura:** Aulas 01 a 03 — conceitos e propriedades geotécnicas que governam barreiras e taludes; erosão e movimentos gravitacionais de massa; resíduos sólidos e seleção de áreas de disposição.
**Recorte:** caracterizar o material, os processos do terreno e escolher o sítio — nenhuma obra é construída ainda. Exemplos no espírito de avaliação e licenciamento.
**Objetivos avaliados:** `geologia-avancado-m08-oa01` (parcial), `geologia-avancado-m08-oa02` (integral), `geologia-avancado-m08-oa03` (parcial)
**Pontuação total:** 100 pontos · o gabarito fica oculto; responda antes de abrir.

---

### 1. Múltipla escolha — `geologia-avancado-m08-q01` · oa01 · 10 pts
Numa mesma obra comparam-se dois solos para o liner de fundo de uma célula de aterro: (I) uma argila muito plástica compactada 3 pontos acima da umidade ótima; (II) um silte arenoso bem graduado compactado na ótima. Sobre o tripé hidráulico–mecânico–químico, a leitura correta é:

- a) O solo I é superior nos três planos, por ser mais fino
- b) O solo I tende a atingir o alvo de `K` mas é o mais fraco e o mais suscetível a fissuração por dessecação e a ataque químico; o solo II é mais resistente e estável, mas dificilmente atinge `K ≤ 1×10⁻⁹ m/s`
- c) O solo II é superior nos três planos, por ser mais resistente
- d) Os dois são equivalentes, porque o que decide o desempenho da barreira é apenas a espessura

<details>
<summary>Ver resposta</summary>

**Resposta: b**

O ponto central da Aula 01 é que os três planos competem e raramente otimizam juntos. A argila muito plástica compactada no ramo bem úmido produz estrutura dispersa e `K` baixo (plano hidráulico satisfeito), mas paga com menor resistência ao cisalhamento (plano mecânico) e maior vulnerabilidade a fissuração por dessecação, a recalque diferencial e à compressão da dupla camada difusa por lixiviado de baixa constante dielétrica ou rico em cátions de alta valência (plano químico). O silte arenoso bem graduado é estável e resistente, mas raramente chega ao alvo de `K`. As alternativas "a" e "c" ignoram a competição entre planos; a "d" ignora que o projeto de barreira é a negociação entre os três critérios, não o cálculo de nenhum isolado.
</details>

---

### 2. Verdadeiro ou Falso (justifique) — `geologia-avancado-m08-q02` · oa01 · 10 pts
"Para minimizar a condutividade hidráulica de uma argila de barreira, deve-se compactá-la na umidade ótima do ensaio de Proctor, que é a que produz a densidade seca máxima."

<details>
<summary>Ver resposta</summary>

**Falso.**

Densidade seca máxima e `K` mínimo **não coincidem**. Na umidade ótima e no ramo seco, a argila compacta em torrões rígidos separados por macroporos — estrutura floculada, com caminhos preferenciais e `K` relativamente alto. Compactando 1 a 3 pontos percentuais **acima** da ótima (ramo úmido), as partículas se orientam paralelamente, os torrões se amassam e os macroporos fecham — estrutura dispersa, com `K` uma a duas ordens de grandeza menor. Para uma barreira, compacta-se deliberadamente no ramo úmido, aceitando a perda de resistência e de rigidez em troca da estanqueidade. É o mesmo ensaio de Proctor lido com objetivo oposto ao de um aterro de suporte de carga.
</details>

---

### 3. Aplicação (cálculo) — `geologia-avancado-m08-q03` · oa01 · 15 pts
Um liner de fundo é formado por 0,75 m de argila compactada com `K = 8×10⁻¹⁰ m/s` e porosidade `n = 0,40`. A camada de coleta de lixiviado mantém no máximo `hw = 0,30 m` de carga hidráulica sobre o topo do liner; a base é drenante (carga nula). Calcule (a) o gradiente hidráulico, (b) a vazão específica advectiva em mm/ano, (c) o tempo de trânsito advectivo da água e (d) o tempo de chegada de um soluto com fator de retardação `R = 2`. Use 1 ano = 3,156×10⁷ s.

<details>
<summary>Ver resolução</summary>

**(a) Gradiente.** Carga total no topo do liner: `hw + L = 0,30 + 0,75 = 1,05 m`; na base: 0.
`i = 1,05 / 0,75 = 1,40`

**(b) Vazão específica (lei de Darcy).**
`q = K·i = 8×10⁻¹⁰ × 1,40 = 1,12×10⁻⁹ m/s`
Em base anual: `1,12×10⁻⁹ × 3,156×10⁷ ≈ 0,0354 m/ano`, ou seja **≈ 35 mm/ano** por m² de liner.

**(c) Tempo de trânsito advectivo da água.**
`v = q/n = 1,12×10⁻⁹ / 0,40 = 2,80×10⁻⁹ m/s`
`t = L/v = 0,75 / 2,80×10⁻⁹ = 2,68×10⁸ s ≈ 8,5 anos`

**(d) Chegada do soluto retardado.**
`t_soluto = R·t = 2 × 8,5 ≈ 17 anos`

**Interpretação:** o liner não impede o fluxo — retarda-o. A água leva ~8,5 anos para atravessar 0,75 m de argila; um contaminante sorvível com `R = 2`, ~17 anos. É esse tempo que fundamenta o alvo de `K` e o programa de monitoramento. Se o lixiviado orgânico da obra elevasse `K`, todos os tempos cairiam na mesma proporção — daí a obrigatoriedade do ensaio de compatibilidade (ASTM D5084 para CCL, ASTM D6766 para GCL).
</details>

---

### 4. Múltipla escolha — `geologia-avancado-m08-q04` · oa02 · 10 pts
Uma voçoroca em solo residual de granito, após anos de crescimento, atingiu o nível d'água. Sobre a evolução daí em diante:

- a) Ela estabiliza, porque o solo saturado tem maior coesão
- b) Ela passa a crescer por erosão interna e solapamento das paredes comandados pelo fluxo de água subterrânea, podendo avançar mesmo sem chuva
- c) Ela só volta a crescer nas próximas chuvas intensas, pelo escoamento superficial concentrado
- d) A erosão cessa, porque abaixo do lençol não há gradiente hidráulico

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Enquanto a feição está acima do lençol, o motor é o escoamento superficial concentrado. Ao atingir o lençol freático, o **fluxo de água subterrânea nas paredes e no fundo** passa a comandar a evolução por erosão interna (piping) e por solapamento da base, que descalça o talude e provoca desabamentos sucessivos. A voçoroca cresce então de forma continuada, independentemente de chuva — é o estágio mais difícil e caro de estabilizar, e o erro clássico é tratá-la só na superfície. As alternativas "c" e "d" ignoram o novo mecanismo; a "a" inverte o efeito da saturação sobre a resistência.
</details>

---

### 5. Verdadeiro ou Falso (justifique) — `geologia-avancado-m08-q05` · oa02 · 10 pts
"Solos dispersivos são detectados na campanha geotécnica de rotina pelos ensaios de granulometria e limites de Atterberg, que acusam a alta fração de argila sódica."

<details>
<summary>Ver resposta</summary>

**Falso.**

Os solos dispersivos — argilas com alta proporção de sódio trocável (PST/SAR elevada), que defloculam espontaneamente em contato com água de baixa salinidade, **sem necessidade de velocidade de fluxo** — **não são identificados** por granulometria nem por limites de Atterberg. Exigem ensaios específicos: **pinhole test** (Sherard et al., 1976), crumb test, ensaio de dupla hidrometria e química do extrato de saturação. Aterros e diques construídos com solo dispersivo sem tratamento (adição de cal, filtros bem graduados) rompem por piping poucos anos após a construção — daí a regra de não aceitar solo em aterro ou dique sem ensaio de dispersividade.
</details>

---

### 6. Dissertativa curta — `geologia-avancado-m08-q06` · oa02 · 12 pts
Explique o princípio da retroanálise (*back-analysis*) de um escorregamento: por que se assume `FS = 1`, por que se fixa um dos parâmetros de resistência em vez de resolver para os dois, e por que o par de parâmetros obtido é mais confiável para o projeto do entorno do que um ensaio triaxial de laboratório.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada — três pontos:**

1. **`FS = 1`:** o escorregamento efetivamente ocorreu, logo, no instante da ruptura, a resistência mobilizada igualou exatamente a solicitação — por definição, `FS = 1`. Fixando a geometria observada e o regime de poropressão estimado para aquele momento, a equação de equilíbrio fica com os parâmetros de resistência como únicas incógnitas.
2. **Fixar um parâmetro:** há **uma equação e dois incógnitos** (`c'` e `φ'`). Deixar os dois livres produz infinitas combinações que satisfazem `FS = 1`. Fixa-se um — em geral `φ'`, por ensaio ou por tipo de solo — e resolve-se para o outro.
3. **Confiabilidade:** o par obtido é o de resistência **operacional** daquela geometria e daquele modelo, e incorpora automaticamente efeitos de escala, estrutura relíquia, fissuras e planos de fraqueza que um corpo de prova pequeno de laboratório não captura. É o que deve alimentar o cálculo de estabilidade das encostas geologicamente análogas do entorno.

**Comentário:** a parte mais delicada da retroanálise é reconstituir as condições hidrológicas do dia da ruptura — o `c'` inferido depende fortemente da hipótese de poropressão adotada.
</details>

---

### 7. Aplicação (cálculo) — `geologia-avancado-m08-q07` · oa02 · 15 pts
Estime a perda de solo anual pela USLE de uma encosta de pastagem degradada com cordões vegetados em nível: `R = 7000` (erosividade), `K = 0,028` (erodibilidade — não confundir com condutividade hidráulica), `LS = 1,8` (fator topográfico), `C = 0,25` (pastagem degradada), `P = 0,8` (cordões em nível), em unidades métricas usuais (t·ha⁻¹·ano⁻¹). Compare com a faixa de tolerância de 4 a 12 t·ha⁻¹·ano⁻¹ e diga qual fator, alterado, teria maior efeito.

<details>
<summary>Ver resolução</summary>

`A = R·K·LS·C·P = 7000 × 0,028 × 1,8 × 0,25 × 0,8`
`A = 196 × 1,8 × 0,25 × 0,8 = 352,8 × 0,25 × 0,8 = 88,2 × 0,8 = 70,6 t·ha⁻¹·ano⁻¹`

**Comparação:** `70,6 / 12 ≈ 5,9` e `70,6 / 4 ≈ 17,7` — a encosta perde de **seis a dezoito vezes** o tolerável (declara-se a faixa, não um múltiplo único, porque a própria tolerância é uma faixa).

**Fator de maior efeito:** `C` (uso e manejo da cobertura). Trocar `C = 0,25` por `C ≈ 0,004` (floresta) levaria `A` a ~1,1 t·ha⁻¹·ano⁻¹ — abaixo da tolerância. `R` e `LS` são dados do sítio, praticamente não manipuláveis; `K` muda muito lentamente; `C` e `P` são as alavancas de intervenção, e `C` é a de maior efeito.
</details>

---

### 8. Múltipla escolha — `geologia-avancado-m08-q08` · oa03 · 10 pts
Sobre os critérios geológico-geotécnicos de seleção de área para aterro sanitário de RSU, assinale a afirmação **correta**:

- a) Um substrato natural de baixa condutividade hidráulica dispensa o liner construído, por funcionar como barreira única
- b) A restrição de distância mínima a aeródromos é um critério da NBR 13896, de natureza ambiental
- c) O substrato de baixa `K` é uma **segunda barreira geológica**, redundante ao liner; e a restrição a aeródromos é regra de **segurança aérea** (Lei 12.725/2012), de exclusão, e não critério da NBR 13896
- d) Os critérios hidrogeológicos podem ser relaxados desde que o liner seja reforçado, porque a engenharia compensa bem a geologia desfavorável

<details>
<summary>Ver resposta</summary>

**Resposta: c**

O substrato de baixa `K` (argila, siltito, rocha sã pouco fraturada) é redundância à barreira construída, não substituição — a norma e a legislação exigem o sistema de impermeabilização independentemente da geologia (elimina "a"). A restrição de distância a aeródromos decorre de o RSU atrair aves: está na Lei 12.725/2012 (Área de Segurança Aeroportuária, que sucedeu a Resolução CONAMA 4/1995), é de exclusão, e **não** é critério da NBR 13896 nem restrição ambiental (elimina "b"). A alternativa "d" enuncia justamente o erro que a aula adverte: o liner tem vida útil finita, a geologia favorável dura tanto quanto a geologia — os critérios de proteção do aquífero (profundidade do lençol, `K` do substrato) são os que a engenharia **não** compensa bem.
</details>

---

### 9. Dissertativa curta — `geologia-avancado-m08-q09` · oa03 · 8 pts
Descreva como a composição do lixiviado (chorume) de um aterro de RSU muda da fase acidogênica para a fase metanogênica, e explique por que a amônia costuma governar o alcance da pluma no longo prazo.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:**

- **Fase acidogênica** (primeiros anos): pH baixo, alta DBO/DQO, ácidos orgânicos voláteis e metais dissolvidos (mais solúveis em pH ácido).
- **Fase metanogênica** (aterro maduro): pH próximo do neutro, DQO menor mas com fração recalcitrante, e **amônia alta e persistente**.
- **Amônia no longo prazo:** ela quase não se degrada em ambiente anaeróbio e não precipita como os metais quando o pH sobe. Enquanto a fração orgânica lábil é atenuada por biodegradação e os metais são retidos por precipitação e sorção, a amônia continua avançando com o fluxo — por isso frequentemente é ela, e não a carga orgânica inicial, que define até onde a pluma chega décadas depois.

**Comentário:** o erro correspondente é tratar a pluma como se estabilizasse quando a fração orgânica lábil se degrada. A amônia e alguns sais persistem e controlam o alcance de longo prazo.
</details>

---

## Gabarito resumido

| Questão | ID | Resposta |
|---|---|---|
| 1 | q01 | b |
| 2 | q02 | Falso (compacta-se no ramo úmido; densidade máxima ≠ `K` mínimo) |
| 3 | q03 | i = 1,40; q ≈ 35 mm/ano; t_água ≈ 8,5 anos; t_soluto ≈ 17 anos |
| 4 | q04 | b |
| 5 | q05 | Falso (exige pinhole test; não aparecem em granulometria/Atterberg) |
| 6 | q06 | ver comentário (FS = 1; fixa φ'; parâmetro operacional) |
| 7 | q07 | A ≈ 70,6 t·ha⁻¹·ano⁻¹; 6 a 18× o tolerável; `C` é a maior alavanca |
| 8 | q08 | c |
| 9 | q09 | ver comentário (acidogênica → metanogênica; amônia persiste) |
