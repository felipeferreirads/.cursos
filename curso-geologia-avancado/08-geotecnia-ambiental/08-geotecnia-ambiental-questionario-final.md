# Questionário final cumulativo — Módulo 08: Geotecnia ambiental

**Módulo:** [[08-geotecnia-ambiental-modulo|Módulo 08 — Geotecnia ambiental]]
**Cobertura:** Aulas 01 a 06 — módulo completo. As questões priorizam o **encadeamento** entre aulas — em especial os objetivos `oa01` (a01, a04) e `oa03` (a03, a04, a05), que atravessam o corte das parciais — e não a repetição isolada de cada aula.
**Objetivos avaliados:** `geologia-avancado-m08-oa01`, `geologia-avancado-m08-oa02`, `geologia-avancado-m08-oa03`, `geologia-avancado-m08-oa04`
**Pontuação total:** 100 pontos · o gabarito fica oculto; responda antes de abrir.

---

### 1. Aplicação integrada (cálculo) — `geologia-avancado-m08-q19` · oa01 (a01 → a04) · 14 pts
Um liner de fundo de CCL tem 0,90 m, `n = 0,42` e `K = 1×10⁻⁹ m/s` medido em laboratório **com água destilada**; a carga sobre o liner é `hw = 0,30 m`. Nesse `K`, o tempo de trânsito advectivo da água é ~9,0 anos e o de um soluto com `R = 3` é ~27 anos. Um ensaio de compatibilidade com o lixiviado orgânico real da obra mede `K = 2,5×10⁻⁹ m/s`. Recalcule os dois tempos e comente por que nenhuma verificação puramente hidráulica ou mecânica teria acusado o problema.

<details>
<summary>Ver resolução</summary>

O gradiente não muda: `i = (0,30 + 0,90)/0,90 = 1,333`. Os tempos de trânsito são inversamente proporcionais a `K` (pois `v = K·i/n` e `t = L/v`).

Fator de degradação: `2,5×10⁻⁹ / 1×10⁻⁹ = 2,5`.

- **Trânsito da água:** `9,0 / 2,5 ≈ 3,6 anos`
- **Soluto com `R = 3`:** `27 / 2,5 ≈ 10,8 anos`
- (Vazão específica: sobe de ~0,042 m/ano para ~0,105 m/ano.)

**Comentário:** a barreira sai da faixa de segurança — os tempos de resposta caem para menos da metade —, mas o ensaio de `K` com água destilada continuaria mostrando 1×10⁻⁹ m/s, e a estabilidade de taludes, o recalque e a integridade das interfaces não teriam mudado. O efeito só aparece quando se percola o **lixiviado real** (ASTM D5084 para CCL, ASTM D6766 para GCL): fluidos de baixa constante dielétrica e cátions de alta valência comprimem a dupla camada difusa, floculam a estrutura e abrem microfissuras. É exatamente para capturar esse acoplamento entre o plano químico e o hidráulico que o ensaio de compatibilidade é obrigatório.
</details>

---

### 2. Múltipla escolha — `geologia-avancado-m08-q20` · oa01 (a01, a05) · 8 pts
O que a barreira de contenção da Aula 01 e a barragem de rejeito da Aula 05 têm em comum, do ponto de vista de método de verificação?

- a) Ambas são dimensionadas exclusivamente pelo critério de condutividade hidráulica
- b) Em ambas, a verificação convencional pode **aprovar** a estrutura enquanto a variável que realmente governa a falha fica de fora: no liner, o `K` sob o lixiviado real (não sob água destilada); na barragem, a resistência **não drenada** de material contrátil saturado (não a resistência drenada)
- c) Ambas falham sempre por galgamento
- d) Nenhuma das duas exige monitoramento após a construção

<details>
<summary>Ver resposta</summary>

**Resposta: b**

É o eixo conceitual comum do módulo: a verificação que aprova no papel não é necessariamente a que decide a falha. Na barreira, testar `K` com água destilada esconde a degradação química que o lixiviado real provoca. Na barragem de rejeito, a análise drenada pode dar `FS ≈ 1,56` (passa em 1,5) enquanto a análise não drenada pós-liquefação dá `FS ≈ 0,25` (já rompeu) — mesmo talude, mesmo material. Em ambos os casos a solução foi tornar obrigatória a verificação "escondida": ensaio de compatibilidade num caso, análise não drenada com resistência de pico e pós-pico no outro.
</details>

---

### 3. Verdadeiro ou Falso (justifique) — `geologia-avancado-m08-q21` · oa03 (a02, a03) · 8 pts
"A seleção de área para um aterro por sobreposição ponderada de critérios em SIG é, metodologicamente, um caso particular da cartografia geotécnica derivada estudada no Módulo 07."

<details>
<summary>Ver resposta</summary>

**Verdadeiro.**

A seleção de área combina critérios de **exclusão** (distâncias mínimas, inundação, carste, Área de Segurança Aeroportuária) e critérios de **classificação** (profundidade do lençol, `K` natural do substrato como segunda barreira, volume/vida útil, vulnerabilidade GOD), tipicamente por **sobreposição ponderada em SIG, frequentemente estruturada por AHP** — exatamente o procedimento das cartas de aptidão do Módulo 07. A carta de "aptidão para disposição de resíduos" é uma carta geotécnica derivada como qualquer outra: mesmas camadas básicas, mesma álgebra de mapas, mesma lógica de pesos. O que muda é o conjunto de atributos priorizado, não o método.
</details>

---

### 4. Dissertativa curta — `geologia-avancado-m08-q22` · oa02 / oa03 (a02 ↔ a05) · 13 pts
A elevação da poropressão está na origem tanto do escorregamento translacional raso da Aula 02 quanto da liquefação estática de rejeito da Aula 05. Explique o mecanismo comum e a diferença essencial entre os dois casos.

<details>
<summary>Ver resposta comentada</summary>

**Mecanismo comum:** em ambos, um aumento de `u` reduz a tensão efetiva `σ' = σ − u` sem alterar de forma relevante a tensão total (o gatilho é hidráulico, não gravitacional — a massa mobilizada é praticamente a mesma antes e depois). Como a parcela friccional da resistência ao cisalhamento é `σ'n·tan φ'`, ela cai quando `σ'n` cai, e a estrutura pode passar de estável a instável.

**Diferença essencial:**
- No **escorregamento translacional raso** (colúvio sobre rocha, chuva intensa), a perda de resistência é **direta e proporcional**: `u` sobe, `σ'n` cai, `FS` cruza 1. Cessada a causa (drenagem), a resistência é recuperada. A retroanálise assume `FS = 1` e calibra `c'` e `φ'` operacionais.
- Na **liquefação estática** de rejeito arenoso **fofo e saturado**, o cisalhamento não drenado de um material **contrátil** gera excesso de poropressão **de forma auto-alimentada**: a tendência a contrair eleva `u`, que reduz `σ'`, que reduz a resistência, o que aprofunda a deformação. A resistência **desaba** de um valor drenado alto para um patamar não drenado baixo e aproximadamente constante — `su(liq) ≈ 5–12 % de σ'v0` — que não se recupera e governa o *runout* de quilômetros. Um rejeito **denso** dilataria e ganharia resistência; é a combinação fofo + saturado + contrátil que produz o colapso.

**Comentário:** a Aula 05 passou a usar a mesma formulação de talude infinito da Aula 02 justamente para tornar essa continuidade explícita.
</details>

---

### 5. Aplicação (cálculo) — `geologia-avancado-m08-q23` · oa02 · 13 pts
Um escorregamento translacional raso ocorreu em colúvio de `z = 2,5 m`, `β = 20°`, `γsat = 18 kN/m³`, com o lençol na superfície e fluxo paralelo à encosta no instante da ruptura. Ensaios independentes indicam `φ' = 30°`. Estime, por retroanálise no modelo de talude infinito, o `c'` mobilizado na ruptura. Use `γw = 9,81 kN/m³`; `sen 20° = 0,3420`, `cos 20° = 0,9397`, `cos²20° = 0,8830`, `tan 30° = 0,5774`.

<details>
<summary>Ver resolução</summary>

**Tensão cisalhante motriz:**
`τ = γsat·z·sen β·cos β = 18 × 2,5 × 0,3420 × 0,9397 = 45 × 0,3214 = 14,46 kPa`

**Tensão normal total:** `γsat·z·cos²β = 45 × 0,8830 = 39,74 kPa`
**Poropressão** (fluxo paralelo): `u = γw·z·cos²β = 9,81 × 2,5 × 0,8830 = 21,66 kPa`
**Tensão normal efetiva:** `σ'n = 39,74 − 21,66 = 18,08 kPa`

**Na ruptura, `FS = 1` → `τ = c' + σ'n·tan φ'`:**
`14,46 = c' + 18,08 × 0,5774 = c' + 10,44`
`c' = 4,02 ≈ 4,0 kPa`

**Interpretação:** o par (`c' = 4,0 kPa`, `φ' = 30°`) é a combinação de resistência compatível com a ruptura observada sob a poropressão máxima, e é ele — não o valor de um triaxial de laboratório — que deve alimentar o cálculo de estabilidade das encostas geologicamente equivalentes do entorno. O resultado depende fortemente da hipótese de lençol na superfície: um lençol mais baixo reduziria `u` e o `c'` inferido seria menor.
</details>

---

### 6. Múltipla escolha — `geologia-avancado-m08-q24` · oa03 · 8 pts
Sobre o quadro legal das barragens de rejeito no Brasil após Mariana e Brumadinho, assinale a afirmação **correta**:

- a) A proibição do alteamento a montante e a exigência de descaracterização surgiram apenas com a Lei 14.066/2020, sem instrumento anterior
- b) A descaracterização torna a estrutura imediatamente segura e libera a área para qualquer uso
- c) A proibição do alteamento a montante e a descaracterização apareceram primeiro na Resolução ANM nº 4/2019 (semanas após Brumadinho) e foram depois elevadas a lei pela Lei 14.066/2020, que alterou a Política Nacional de Segurança de Barragens; a Resolução ANM nº 95/2022 consolidou as regras
- d) O GISTM (2020) é uma norma brasileira que substituiu as resoluções da ANM

<details>
<summary>Ver resposta</summary>

**Resposta: c**

A sequência é: Resolução ANM nº 4/2019 (primeira proibição do alteamento a montante e prazos de descaracterização) → Lei 14.066/2020, que alterou a Lei 12.334/2010 (Política Nacional de Segurança de Barragens) elevando a proibição e a descaracterização a lei → Resolução ANM nº 95/2022, que consolidou as regras antes dispersas em portarias. O **GISTM** (*Global Industry Standard on Tailings Management*, ICMM/UNEP/PRI, 2020) é o padrão **internacional** de referência, não uma norma brasileira (elimina "d"). A descaracterização é um processo de anos, com riscos próprios durante a execução (elimina "b"). Prazos e detalhes evoluem — reconfirmar o texto vigente antes de fundamentar parecer.
</details>

---

### 7. Verdadeiro ou Falso (justifique) — `geologia-avancado-m08-q25` · oa02 / oa03 · 8 pts
"O fator de segurança de projeto de um talude ou de uma barragem é um valor único, fixado em norma em 1,5, e a estrutura está segura sempre que o cálculo o supera."

<details>
<summary>Ver resposta</summary>

**Falso** — em duas frentes.

Primeiro, **o `FS` não é único**: depende da confiança nos parâmetros, das consequências da ruptura e da condição analisada. Referências correntes: `FS ≥ 1,5` para condição drenada de longo prazo com boa investigação; `FS ≥ 1,3` para fim de construção (não drenada) ou carregamento transitório; valores maiores quando há população exposta a jusante; e, havendo rejeito contrátil saturado, o `FS` que importa é o **não drenado**, não o drenado.

Segundo, **`FS` alto não garante estabilidade**: ele só é tão bom quanto os parâmetros e a hipótese de poropressão que o alimentam. Encostas com `FS` calculado alto rompem quando a poropressão excede a assumida ou quando há um plano de fraqueza não mapeado. Abordagens probabilísticas substituem o `FS` determinístico pela probabilidade de ruptura quando a incerteza dos parâmetros é grande.
</details>

---

### 8. Aplicação (cálculo) — `geologia-avancado-m08-q26` · oa03 / oa01 (a04) · 8 pts
Dois aterros vão receber cobertura final. Aterro X fica no semiárido: `P = 480 mm/ano`, evapotranspiração potencial `ETP ≈ 1700 mm/ano`. Aterro Y fica no Sul: `P = 1700 mm/ano`, `ETP ≈ 950 mm/ano`. Para cada um, diga qual tipo de cobertura é adequado e justifique com o balanço `ETP − P`.

<details>
<summary>Ver resolução</summary>

**Aterro X (semiárido):** `ETP − P ≈ 1700 − 480 = +1220 mm/ano`. A evapotranspiração potencial supera a precipitação com larga folga durante o ano — a vegetação é capaz de devolver à atmosfera a água armazenada na camada de solo antes que ela percole. **Cobertura evapotranspirativa (*store-and-release*)** é adequada e preferível: mais barata, mais tolerante a recalque (sem camada rígida a fissurar) e frequentemente mais durável.

**Aterro Y (Sul):** `ETP − P ≈ 950 − 1700 = −750 mm/ano`. O balanço é negativo boa parte do ano; não há como confiar na evapotranspiração para descartar a chuva. **Cobertura convencional (resistiva)** — geomembrana e/ou argila compactada de baixo `K` sob camadas de drenagem e solo com vegetação —, aceitando a necessidade de cuidar da fissuração por dessecação e do recalque diferencial (declividade inicial folgada).

**Comentário:** a escolha da cobertura é climática antes de ser geotécnica. Transpor a cobertura de X para Y deixaria passar volume de lixiviado inaceitável.
</details>

---

### 9. Dissertativa curta — `geologia-avancado-m08-q27` · oa04 · 11 pts
Explique por que não existe uma técnica de remediação universalmente superior, citando os fatores que governam a seleção e dando um exemplo em que a geologia derrota uma técnica que seria adequada para o contaminante.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada — a seleção depende de:**
1. **Contaminante e fase:** VOC respondem a SVE e air sparging; solventes clorados dissolvidos, a PRB de ferro zero-valente e biorremediação anaeróbia; metais, a solidificação/estabilização e fitoextração (nunca oxidação ou volatilização); DNAPL em fase livre exige remoção de fonte antes de qualquer tratamento de pluma.
2. **Geologia:** técnicas de injeção e extração falham em meio heterogêneo e de baixa permeabilidade.
3. **Tempo e custo:** pump & treat e ANM são baratos por ano mas duram décadas; ISCO e escavação são caros e rápidos.

**Exemplo em que a geologia derrota a técnica:** a oxidação química in situ (ISCO) é adequada para um solvente clorado dissolvido, mas num aquífero com lentes argilosas o oxidante injetado segue os caminhos preferenciais de maior permeabilidade e **não alcança a massa retida por difusão** nas lentes de baixa `K`. Quando a injeção para, essa massa retorna por *back-diffusion* e a concentração volta a subir — a técnica certa para o contaminante fracassa pela heterogeneidade do meio.

**Comentário:** quase todo projeto real combina várias técnicas em série ou em paralelo, e atingir a meta de remediação é ausência de risco inaceitável para o uso pretendido — não retorno à condição pré-degradação.
</details>

---

### 10. Dissertativa curta (síntese) — `geologia-avancado-m08-q28` · oa01–oa04 · 14 pts
O módulo percorre a vida inteira de uma obra de contenção ambiental. Em uma frase para cada aula, diga qual etapa dessa vida ela cobre e qual conceito-eixo (condutividade hidráulica ou tensão efetiva) ela mobiliza.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:**

- **a01 — caracterizar o material e a barreira.** Define o tripé hidráulico–mecânico–químico e o alvo `K ≤ 1×10⁻⁹ m/s`; a **condutividade hidráulica** é a variável mestra da barreira, e a compactação no ramo úmido é o meio de minimizá-la.
- **a02 — caracterizar os processos do terreno.** Erosão e movimentos de massa; a **tensão efetiva** governa a deflagração — a chuva eleva `u`, reduz `σ'n` e a resistência friccional despenca (retroanálise assume `FS = 1`).
- **a03 — escolher o sítio.** Classificação de resíduos, hierarquia da PNRS e critérios de seleção de área; o `K` **natural do substrato** entra como segunda barreira geológica, e a pluma de lixiviado evolui pelos processos advectivo-dispersivos.
- **a04 — projetar e operar o aterro.** Liner composto, balanço hídrico/HELP, cobertura convencional × evapotranspirativa, recalque por biodegradação; o `K` de projeto e o gradiente sobre o liner determinam a fuga, e o `K` só vale sob o fluido em que foi medido.
- **a05 — conter o rejeito e reparar a estrutura.** Lama × rejeito arenoso, métodos de alteamento, filtrado, liquefação estática; a **tensão efetiva** sob cisalhamento não drenado é o que separa `FS ≈ 1,56` de `FS ≈ 0,25`.
- **a06 — recuperar e remediar.** Metas de recuperação, mapa das técnicas de remediação, zona de captura de poço (`q = K·i`), resíduos como material geotécnico; a **condutividade hidráulica** volta a governar — a heterogeneidade de `K` derrota injeção e extração.

**Comentário:** quem enxerga esse fio — caracterizar → escolher → projetar/operar → reparar/remediar, com `K` e `σ'` reaparecendo em cada etapa — aplica o módulo a situações novas; quem estudou as seis aulas como tópicos separados tende a cometer os erros listados em cada "Erros comuns".
</details>

---

## Gabarito resumido

| Questão | ID | Resposta |
|---|---|---|
| 1 | q19 | t_água ≈ 3,6 anos; t_soluto ≈ 10,8 anos; só o ensaio de compatibilidade com lixiviado real acusa |
| 2 | q20 | b |
| 3 | q21 | Verdadeiro (mesma álgebra de mapas ponderada do Módulo 07) |
| 4 | q22 | ver comentário (queda de σ' por u; direta e recuperável × colapso auto-alimentado a su(liq)) |
| 5 | q23 | τ = 14,46 kPa; σ'n = 18,08 kPa; c' ≈ 4,0 kPa |
| 6 | q24 | c |
| 7 | q25 | Falso (FS depende da condição; não drenado para rejeito saturado; FS alto não garante nada) |
| 8 | q26 | X (ETP−P = +1220): evapotranspirativa; Y (ETP−P = −750): convencional resistiva |
| 9 | q27 | ver comentário (contaminante/fase, geologia, tempo/custo; ISCO derrotado por back-diffusion) |
| 10 | q28 | ver comentário (uma etapa e um eixo por aula) |
