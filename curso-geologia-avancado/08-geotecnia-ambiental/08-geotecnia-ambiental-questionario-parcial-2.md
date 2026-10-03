# Questionário parcial 2 — Módulo 08: Geotecnia ambiental

**Módulo:** [[08-geotecnia-ambiental-modulo|Módulo 08 — Geotecnia ambiental]]
**Cobertura:** Aulas 04 a 06 — aterros sanitários (liners, coberturas, recalques, monitoramento); rejeitos de mineração e estruturas de contenção; recuperação de áreas degradadas e remediação de solo e aquífero.
**Recorte:** projetar, operar e reparar — as obras que a parcial 1 apenas dimensionava conceitualmente. Exemplos de dimensionamento.
**Objetivos avaliados:** `geologia-avancado-m08-oa01` (parcial), `geologia-avancado-m08-oa03` (parcial), `geologia-avancado-m08-oa04` (integral)
**Pontuação total:** 100 pontos · o gabarito fica oculto; responda antes de abrir.

---

### 1. Múltipla escolha — `geologia-avancado-m08-q10` · oa03 / oa01 · 10 pts
Um liner de fundo composto usa geomembrana de PEAD sobre camada de argila compactada (CCL). O motivo de o conjunto superar o desempenho das duas barreiras somadas em série é:

- a) A soma das resistências hidráulicas da geomembrana e da CCL é maior que a de cada uma
- b) A geomembrana elimina o fluxo advectivo pela área intacta, e a CCL, abaixo dela, confina o vazamento sob cada defeito da geomembrana, impedindo o espalhamento lateral
- c) A geomembrana é totalmente impermeável e a CCL é redundante
- d) A CCL protege a geomembrana do puncionamento, e é só isso que o arranjo composto acrescenta

<details>
<summary>Ver resposta</summary>

**Resposta: b**

O ganho do liner composto vem da **interação**, não da soma. A geomembrana intacta corta o fluxo advectivo pela área íntegra; onde há um furo de instalação, a CCL logo abaixo impede que o líquido se espalhe lateralmente e encontre outros caminhos, limitando a fuga a um vazamento local pequeno (expressões de Giroud & Bonaparte, 1989). A alternativa "a" comete o erro de tratar as barreiras como resistências independentes em série. A "c" ignora que nenhuma geomembrana instalada é isenta de defeitos. A "d" reduz o efeito a uma função secundária.
</details>

---

### 2. Aplicação (cálculo) — `geologia-avancado-m08-q11` · oa03 · 13 pts
Uma célula de aterro de 5,0 ha recebe cobertura. Dados: `P = 1100 mm/ano`, deflúvio superficial 15 % de `P`, `AET = 550 mm/ano`, `ΔS ≈ 0`. Calcule (a) a percolação anual pela cobertura e o volume de lixiviado gerado (m³/ano e m³/dia). (b) Se a barreira de fundo fosse **só** uma CCL de 0,50 m com `K = 1×10⁻⁹ m/s` e `hw = 0,30 m` de carga, calcule a vazão de fuga (mm/ano e m³/ano sobre 5 ha). (c) Comente a hierarquia dos dois números. Use 1 ano = 3,156×10⁷ s.

<details>
<summary>Ver resolução</summary>

**(a) Balanço hídrico da cobertura.**
`ES = 0,15 × 1100 = 165 mm/ano`
`L = P − ES − AET − ΔS = 1100 − 165 − 550 − 0 = 385 mm/ano`
Sobre 5,0 ha = 50 000 m²:
`V = 0,385 × 50 000 = 19 250 m³/ano ≈ 53 m³/dia`

**(b) Fuga por uma CCL isolada.**
`i = (0,50 + 0,30)/0,50 = 1,60`
`q = K·i = 1×10⁻⁹ × 1,60 = 1,6×10⁻⁹ m/s`
Base anual: `1,6×10⁻⁹ × 3,156×10⁷ ≈ 0,0505 m/ano = 50,5 mm/ano`
Sobre 5 ha: `0,0505 × 50 000 ≈ 2 525 m³/ano`

**(c) Hierarquia.** A fuga pelo fundo (~2 525 m³/ano na pior hipótese da CCL isolada, e duas a três ordens de grandeza menos se houver geomembrana sobre ela) é pequena frente aos ~19 250 m³/ano de lixiviado que a drenagem precisa **coletar e tratar**. O gargalo operacional de um aterro bem construído é o tratamento do lixiviado captado, não o vazamento pelo liner.
</details>

---

### 3. Verdadeiro ou Falso (justifique) — `geologia-avancado-m08-q12` · oa03 · 9 pts
"A barreira de cobertura evapotranspirativa (*store-and-release*) é preferível à convencional em qualquer clima, porque armazena a água da chuva e a devolve à atmosfera em vez de depender de uma camada rígida que fissura."

<details>
<summary>Ver resposta</summary>

**Falso.**

A cobertura evapotranspirativa **não barra** a água — administra o seu tempo de residência: armazena a chuva na capacidade de campo de uma camada espessa de solo fino e conta com a evapotranspiração da vegetação para devolvê-la à atmosfera antes que percole. Isso só funciona onde a **evapotranspiração potencial supera a precipitação** com folga — climas áridos e semiáridos. Em clima úmido o balanço `ET − P` é negativo boa parte do ano, e a cobertura deixa passar volume de lixiviado inaceitável. A escolha da cobertura é climática antes de ser geotécnica: as vantagens de custo e de tolerância a recalque só se realizam onde o clima permite confiar na evapotranspiração.
</details>

---

### 4. Dissertativa curta — `geologia-avancado-m08-q13` · oa03 · 11 pts
Explique por que o recalque de um aterro de RSU é qualitativamente diferente do recalque de uma camada de solo, e cite duas implicações diretas para o projeto da cobertura final.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:**

O recalque de aterro de RSU tem, além das parcelas imediata (rearranjo mecânico) e primária (dissipação de pressões de líquido e gás), uma parcela de longo prazo que soma a **compressão secundária** (*creep*) à **perda de massa por biodegradação** da fração orgânica. Parte do volume simplesmente **desaparece**, convertida em biogás e lixiviado — não há analogia direta com `Cc` e `Cα` de solo, e o recalque total de longo prazo chega a 15–30 % da altura.

**Duas implicações para a cobertura:**
1. A cobertura deve ser executada com **declividade inicial folgada** (maior que a final desejada), para continuar drenando depois de anos de recalque diferencial.
2. A geomembrana da cobertura precisa de **deformação admissível compatível** com o assentamento continuado; e o uso pós-fechamento fica restrito a atividades leves e reversíveis (parque, estacionamento — nunca edificação convencional).

**Comentário:** por isso o monitoramento de marcos de recalque e de poços de gás se estende por décadas no período de pós-fechamento.
</details>

---

### 5. Múltipla escolha — `geologia-avancado-m08-q14` · oa03 · 10 pts
Sobre o método de alteamento **a montante** de barragem de rejeito:

- a) É o mais seguro, porque o novo alteamento se apoia em material já adensado
- b) É o mais barato e o de menor consumo de material, mas o mais perigoso, porque incorpora rejeito não compactado — potencialmente fofo e saturado — no corpo da barragem, sobre o qual o eixo se desloca; foi a geometria de Fundão e da Barragem I da Mina do Feijão
- c) É proibido no mundo inteiro desde a década de 1990
- d) Equivale ao método de jusante, apenas com custo menor de terraplenagem

<details>
<summary>Ver resposta</summary>

**Resposta: b**

No alteamento a montante cada novo alteamento se apoia parcialmente sobre a praia de rejeito do ciclo anterior, e o eixo da crista se desloca sobre esse material não compactado, potencialmente contrátil e saturado. É o mais barato e o de menor footprint, e o mais perigoso — foi a geometria de Fundão (2015) e de Feijão I (2019). A alternativa "a" inverte o fato; a "c" é imprecisa (a proibição no Brasil veio da Resolução ANM 4/2019 e da Lei 14.066/2020, não dos anos 1990, e não é universal); a "d" ignora que o método de jusante lança material compactado sobre fundação preparada, o que muda tudo.
</details>

---

### 6. Aplicação (cálculo) — `geologia-avancado-m08-q15` · oa03 / oa01 · 16 pts
Analisa-se um elemento de rejeito arenoso fofo saturado na face de jusante de uma barragem alteada a montante, a `z = 15 m` abaixo da superfície do talude, inclinação `β = 12°`, `γsat = 20 kN/m³`, lençol **na superfície com fluxo paralelo ao talude**, `γw = 9,81 kN/m³`, `φ' = 33°`. A razão de resistência liquefeita estimada por ensaios é `su(liq)/σ'v0 = 0,10`. Compare o fator de segurança na análise **drenada** e na análise **não drenada pós-liquefação** (modelo de talude infinito). Termos: `sen 12° = 0,2079`, `cos 12° = 0,9781`, `cos²12° = 0,9568`, `tan 33° = 0,6494`.

<details>
<summary>Ver resolução</summary>

**Tensão cisalhante motriz** — o peso que empurra é o **total**, não o submerso:
`τ = γsat·z·sen β·cos β = 20 × 15 × 0,2079 × 0,9781 = 300 × 0,2034 = 61,0 kPa`

**Tensões efetivas** (fluxo paralelo, `u = γw·z·cos²β`):
`σ'v0 = (γsat − γw)·z = 10,19 × 15 = 152,9 kPa`
`σ'n = (γsat − γw)·z·cos²β = 152,9 × 0,9568 = 146,2 kPa`

**(a) Análise drenada.**
`τf = σ'n·tan φ' = 146,2 × 0,6494 = 95,0 kPa`
`FS_drenado = 95,0 / 61,0 ≈ 1,56`

**(b) Análise não drenada pós-liquefação.**
`su(liq) = 0,10 × σ'v0 = 0,10 × 152,9 = 15,3 kPa`
`FS_liq = 15,3 / 61,0 ≈ 0,25`

**Interpretação:** pela conta drenada o talude **passa** no critério regulamentar de 1,5 e seria aprovado. Levado à ruptura não drenada, o mesmo talude, com a mesma geometria e o mesmo material, tem `FS ≈ 0,25` — já rompeu. Se um gatilho qualquer (alteamento rápido demais para o rejeito adensar, elevação do nível freático, pequena ruptura localizada) dispara a resposta não drenada, a resistência cai de ~95 kPa para ~15 kPa e a massa flui, mantida em movimento pela baixa resistência residual `su(liq)`. Havendo rejeito fofo saturado, **a análise drenada isolada não é suficiente** — e é por isso que a legislação proibiu a geometria de montante.

**Erro a evitar:** usar o peso submerso também no esforço motriz (hipótese de talude submerso) superestimaria `FS` por um fator próximo de `γsat/γsub ≈ 1,96`.
</details>

---

### 7. Verdadeiro ou Falso (justifique) — `geologia-avancado-m08-q16` · oa04 · 10 pts
"Contaminação do solo por chumbo e cromo pode ser tratada eficientemente por oxidação química in situ (ISCO) ou por *air sparging*, assim como se faz com solventes voláteis."

<details>
<summary>Ver resposta</summary>

**Falso.**

Metais **não são destruídos** por oxidação nem convertidos a formas voláteis inócuas — muitas vezes a oxidação os torna **mais móveis**. ISCO e air sparging são adequados a compostos orgânicos: SVE e air sparging para voláteis (VOC); ISCO e biorremediação para solventes clorados dissolvidos. Para metais, as técnicas apropriadas são a **solidificação/estabilização** (mistura com cimento/aglomerantes, que imobiliza) e a **fitoextração**. A seleção da técnica é função primária do contaminante — aplicar a rota errada pode piorar a mobilidade da pluma.
</details>

---

### 8. Múltipla escolha — `geologia-avancado-m08-q17` · oa04 · 7 pts
Um sistema de bombeamento e tratamento (*pump & treat*) opera há três anos numa pluma de solvente dissolvido. A concentração no efluente caiu rápido no primeiro ano e depois estacionou num patamar. Ao desligar as bombas para manutenção, a concentração no aquífero voltou a subir. A leitura correta é:

- a) O sistema falhou por erro de dimensionamento hidráulico e deve ser refeito
- b) São o *tailing* e o *rebound* esperados: há fonte residual (DNAPL aprisionado e massa que difundiu para camadas de baixa permeabilidade) realimentando a pluma; sem tratamento de fonte, o sistema opera indefinidamente
- c) A pluma já foi remediada e o sistema pode ser desligado
- d) O patamar indica que a meta de remediação foi atingida

<details>
<summary>Ver resposta</summary>

**Resposta: b**

O pump & treat contém bem a pluma, mas a concentração no efluente cai depressa e depois estaciona (*tailing*), e volta a subir quando as bombas param (*rebound*). A causa é a fonte residual — DNAPL aprisionado e massa que difundiu para dentro de camadas de baixa permeabilidade e retorna lentamente (*back-diffusion*). Sem tratar a fonte, o sistema não encerra. A estratégia moderna combina remoção agressiva de fonte com contenção/atenuação de pluma. As alternativas "c" e "d" confundem patamar com meta atingida; a "a" atribui a um erro de projeto um comportamento que é intrínseco ao método.
</details>

---

### 9. Aplicação (cálculo) — `geologia-avancado-m08-q18` · oa04 · 15 pts
Uma pluma de solvente dissolvido com ~150 m de largura deve ser contida por bombeamento e tratamento. Aquífero: espessura saturada `b = 12 m`, `K = 15 m/dia`, gradiente regional `i = 0,005`, porosidade efetiva `n = 0,20`. Para **um** poço bombeando `Q = 200 m³/dia`, calcule (a) a vazão específica `q` do fluxo regional, (b) a largura assintótica da zona de captura `W∞` e a largura na linha transversal do poço `W₀`, (c) o ponto de estagnação a jusante `x_L`, e (d) avalie se um poço basta.

<details>
<summary>Ver resolução</summary>

**(a) Fluxo regional (Darcy).**
`q = K·i = 15 × 0,005 = 0,075 m/dia`
(velocidade real, se necessário: `v = q/n = 0,075 / 0,20 = 0,375 m/dia`)

**(b) Largura da zona de captura** (poço único em fluxo uniforme):
`W∞ = Q / (b·q) = 200 / (12 × 0,075) = 200 / 0,9 ≈ 222,2 m` → `± 111,1 m` do eixo
`W₀ = Q / (2·b·q) = 111,1 m` → `± 55,6 m` do eixo (metade da assintótica)

**(c) Ponto de estagnação a jusante:**
`x_L = Q / (2π·b·q) = 200 / (2π × 0,9) = 200 / 5,655 ≈ 35,4 m`

**(d) Avaliação.** A largura assintótica (222,2 m) excede a largura da pluma (150 m), então um poço é **geometricamente capaz** de interceptá-la. Mas o envelope **afunila** em direção ao poço: na linha transversal do poço tem só 111,1 m, **menos que os 150 m da pluma**. Um envelope de 150 m só existe a partir de cerca de 30 m a montante do poço — logo, o poço precisa ficar bem a jusante da pluma, e não coincidente com ela, e ainda com margem para a incerteza de `K` e de `i`. Na prática adota-se frequentemente uma linha de 2–3 poços de menor vazão, para dar redundância, reduzir o rebaixamento excessivo num único ponto e cobrir a pluma com folga. E o dimensionamento hidráulico é só metade do projeto: o sistema opera por décadas (tailing/rebound), e o custo dominante é o bombeamento e o tratamento continuados.
</details>

---

## Gabarito resumido

| Questão | ID | Resposta |
|---|---|---|
| 1 | q10 | b |
| 2 | q11 | L = 385 mm/ano; V ≈ 19 250 m³/ano (~53 m³/dia); fuga CCL ≈ 50,5 mm/ano (~2 525 m³/ano); coleta >> fuga |
| 3 | q12 | Falso (só onde ET potencial > P — árido/semiárido) |
| 4 | q13 | ver comentário (biodegradação remove massa; declividade inicial folgada + GM deformável) |
| 5 | q14 | b |
| 6 | q15 | τ = 61,0 kPa; FS drenado ≈ 1,56; FS pós-liquefação ≈ 0,25 |
| 7 | q16 | Falso (metais: S/E e fitoextração, não ISCO/air sparging) |
| 8 | q17 | b |
| 9 | q18 | q = 0,075 m/dia; W∞ ≈ 222 m; W₀ ≈ 111 m; x_L ≈ 35 m; um poço só se locado a jusante da pluma — recomendável linha de 2–3 poços |
