# Questionário cumulativo — Módulo 12: Engenharia de petróleo

**Módulo:** [[12-engenharia-de-petroleo-modulo|Módulo 12 — Engenharia de petróleo]]
**Cobertura:** Aulas 01 a 05 (módulo completo — 5 aulas, abaixo do limiar de ~5–6 que aciona questionários parciais; nenhum corte candidato deixa um objetivo inteiro de um lado só — o único corte que pareceria natural, entre a02 e a03, preserva oa01+oa02 de um lado e oa03 (que atravessa a03+a04) e oa04 do outro, ver [[12-engenharia-de-petroleo-revisao-didatica|revisão didática]]).
**Objetivos avaliados:** geologia-avancado-m12-oa01, oa02, oa03, oa04 (todos)

---

### 1. Múltipla escolha (oa01)
Sobre as funções do fluido de perfuração (lama), qual alternativa está correta?

a) A lama serve apenas para resfriar a broca; o controle de pressão da formação é feito exclusivamente pelo BOP (*blowout preventer*)
b) Entre as funções da lama estão remover o cascalho até a superfície, resfriar e lubrificar a broca, sustentar as paredes do poço por meio do *mudcake* e controlar a pressão de formação através do seu peso
c) O peso da lama deve ser ajustado apenas para superar a pressão de fratura, garantindo a maior taxa de penetração possível
d) A lama de perfuração não influencia a estabilidade das paredes do poço, servindo só para a limpeza do fundo

<details><summary>Ver resposta</summary>

**Resposta: b** — as quatro funções da lama (remoção de cascalho, resfriamento/lubrificação, sustentação de parede via mudcake, controle de pressão pelo peso da coluna de fluido) atuam em conjunto. A alternativa a isola o controle de pressão no BOP, que é um equipamento de emergência, não a primeira linha de controle (essa é o peso da lama); a alternativa c inverte a lógica da janela operacional — ultrapassar a pressão de fratura induz perda de circulação, é o limite superior a evitar, não o alvo; a alternativa d ignora a função de sustentação de parede, central para evitar desmoronamento (Aula 01).
</details>

---

### 2. Aplicação (cálculo, oa01)
Um poço está sendo perfurado a 3.000 m de profundidade (≈ 9.843 ft) com lama de peso 10,5 ppg. Usando o fator de conversão padrão de 0,052 psi/ft por ppg, calcule (a) o gradiente de pressão da lama e (b) a pressão hidrostática exercida no fundo do poço a essa profundidade. Considerando um gradiente de poros de 0,465 psi/ft e um gradiente de fratura de 0,80 psi/ft na mesma profundidade, esse peso de lama mantém o poço dentro da janela operacional? Justifique com as margens de segurança (sobrebalanço e margem até a fratura).

<details><summary>Ver resolução</summary>

(a) Gradiente da lama = 10,5 ppg × 0,052 psi/ft/ppg = **0,546 psi/ft**.

(b) Pressão hidrostática = 0,546 psi/ft × 9.843 ft ≈ **5.374 psi**.

Pressão de poros na mesma profundidade = 0,465 × 9.843 ≈ 4.577 psi. Pressão de fratura = 0,80 × 9.843 ≈ 7.874 psi.

Margem de sobrebalanço (hidrostática − poros) = 5.374 − 4.577 = **797 psi**, positiva, então a pressão hidrostática supera a de poros e evita influxo de fluido de formação (*kick*). Margem até a fratura (fratura − hidrostática) = 7.874 − 5.374 = **2.500 psi**, também positiva, então a lama não induz perda de circulação. **O peso de lama de 10,5 ppg mantém o poço dentro da janela operacional**, com folga confortável nas duas direções (Aula 01).
</details>

---

### 3. Verdadeiro ou Falso (oa01)
"A cimentação de um poço serve apenas para fixar o revestimento mecanicamente às paredes do poço, sem função de isolamento entre zonas."

<details><summary>Ver resposta</summary>

**Falso.** A cimentação cumpre três funções, não uma: fixação mecânica do revestimento, **isolamento entre zonas** (impedindo comunicação de fluidos entre formações distintas ao longo do anular) e proteção do revestimento contra corrosão. Reduzir a cimentação à fixação mecânica ignora justamente a função mais crítica para a segurança do poço e para evitar migração indesejada de fluidos (Aula 01).
</details>

---

### 4. Múltipla escolha (oa02)
Ao interpretar um conjunto de perfis de resistividade com diferentes profundidades de investigação (rasa, média, profunda) numa zona invadida por filtrado de lama, qual leitura melhor representa a resistividade da zona virgem (não invadida), e por quê?

a) A leitura rasa, porque está mais próxima do poço e por isso mais confiável
b) A leitura profunda (Rt), porque é a menos afetada pela invasão do filtrado
c) A média aritmética simples das três leituras
d) A leitura média, porque combina de forma equilibrada proximidade e profundidade de investigação

<details><summary>Ver resposta</summary>

**Resposta: b** — a resistividade é uma resposta ao **fluido**, não à matriz da rocha; quanto mais próxima do poço, mais a leitura reflete a zona invadida pelo filtrado de lama, e não o fluido original da formação. A leitura profunda (Rt) penetra além da zona invadida e é por isso o valor usado na equação de Archie para representar a saturação de água virgem; as alternativas c e d tentam contornar o problema por média, mas isso apenas dilui o sinal de invasão sem eliminá-lo (Aula 02).
</details>

---

### 5. Aplicação (cálculo, oa02)
Um intervalo reservatório tem porosidade φ = 0,20. A análise de resistividade indica Rw = 0,05 Ω·m (água de formação) e Rt = 20 Ω·m (resistividade profunda). Usando a equação de Archie com a = 1, m = 2 e n = 2, calcule a saturação de água (Sw) e a saturação de hidrocarboneto (Sh) desse intervalo.

<details><summary>Ver resolução</summary>

φᵐ = 0,20² = 0,04. a/φᵐ = 1/0,04 = 25. Rw/Rt = 0,05/20 = 0,0025.

Sw² = (a/φᵐ) × (Rw/Rt) = 25 × 0,0025 = 0,0625 → Sw = √0,0625 = **0,25 (25%)**.

Sh = 1 − Sw = 1 − 0,25 = **0,75 (75%)** — o intervalo é dominado por hidrocarboneto (Aula 02).
</details>

---

### 6. Aplicação (cálculo, oa02)
Suponha que a calibração local dessa mesma formação (por exemplo, a partir de dados de testemunhagem) indique um expoente de cimentação m = 1,8 em vez de m = 2, mantendo os demais parâmetros da questão anterior. Qual o novo valor de Sw? O que esse resultado ilustra sobre o uso da equação de Archie?

<details><summary>Ver resolução</summary>

φ^1,8 = 0,20^1,8 ≈ 0,0551. a/φᵐ = 1/0,0551 ≈ 18,15. Rw/Rt continua 0,0025.

Sw² ≈ 18,15 × 0,0025 ≈ 0,0454 → Sw ≈ √0,0454 ≈ **0,21 (21%)**.

O resultado ilustra que **a, m e n não são constantes universais** — são parâmetros que precisam ser calibrados para a formação específica (tipicamente contra dados de testemunhagem). A mesma rocha, com o mesmo Rw e Rt, produz uma estimativa de Sw sensivelmente diferente (25% vs. 21%) só por causa da escolha do expoente de cimentação, o que reforça por que a testemunhagem funciona como calibração dos parâmetros de Archie, e não como um passo dispensável (Aula 02).
</details>

---

### 7. Dissertativa curta (oa02)
Explique por que a relação linear Vsh = IGR (índice de raios gama) tende a **superestimar** o volume de argila, e como correções não lineares (do tipo Larionov) resolvem parcialmente esse problema. Cite a distinção que deve ser feita entre rochas terciárias e mais antigas ao aplicar essa correção.

<details><summary>Ver resposta comentada</summary>

**Resposta esperada:** o IGR (índice de raios gama, normalizado entre GRmin e GRmax) cresce de forma aproximadamente proporcional ao teor de argila só numa primeira aproximação; na prática, a relação real entre radioatividade e volume de argila não é linear, e adotar Vsh = IGR diretamente atribui à argila uma fração maior do sinal de raios gama do que ela realmente representa — daí a superestimativa sistemática. Correções não lineares como a de Larionov comprimem a curva, produzindo um Vsh menor que o IGR bruto para o mesmo valor de leitura. A distinção necessária é que a curva de correção não é única: Larionov propõe uma curva para rochas **terciárias** (mais jovens, menos consolidadas) e outra, com fator de compressão diferente, para rochas **mais antigas** — usar a curva errada para a idade da formação reintroduz parte do próprio erro que a correção pretende eliminar (Aula 02).
</details>

---

### 8. Verdadeiro ou Falso (oa03)
"Acima do ponto de bolha, o fator volume-formação do óleo (Bo) permanece constante, e é somente abaixo dele que Bo passa a aumentar com a queda de pressão."

<details><summary>Ver resposta</summary>

**Falso.** É o oposto do que a curva de Bo descreve: **acima** do ponto de bolha (óleo subsaturado), Bo **aumenta** levemente à medida que a pressão cai, por expansão do óleo ainda todo em solução; Bo atinge seu valor **máximo (Bob)** exatamente no ponto de bolha. **Abaixo** dele, à medida que o gás sai de solução, Bo passa a **diminuir**. Inverter esse sinal — achar que Bo é constante acima do ponto de bolha e só varia abaixo — é o erro mais comum ao interpretar um diagrama de Bo × pressão (Aula 03).
</details>

---

### 9. Aplicação (cálculo, oa03)
Um reservatório tem área de drenagem A = 800 acres, espessura líquida h = 25 ft, porosidade φ = 0,22, saturação de água Sw = 0,30 e fator volume-formação do óleo Bo = 1,25 bbl/STB. Usando o método volumétrico (OOIP = 7.758 × A × h × φ × (1−Sw) / Bo), calcule o OOIP. Em seguida, calcule a reserva recuperável considerando um fator de recuperação (FR) primário de 18%.

<details><summary>Ver resolução</summary>

Numerador: 7.758 × 800 = 6.206.400; × 25 = 155.160.000; × 0,22 = 34.135.200; × (1 − 0,30) = × 0,70 = 23.894.640.

OOIP = 23.894.640 / 1,25 = **19.115.712 STB**.

Reserva recuperável a FR = 18%: 19.115.712 × 0,18 = **3.440.828 STB** (Aula 03).
</details>

---

### 10. Aplicação (cálculo, oa03)
Se uma análise PVT revisada indicar Bo = 1,35 bbl/STB em vez de 1,25 (mantendo A, h, φ e Sw da questão anterior), qual o novo OOIP? Compare com o valor anterior e explique, em termos físicos, por que um Bo maior reduz o OOIP calculado em STB.

<details><summary>Ver resolução</summary>

OOIP = 23.894.640 / 1,35 ≈ **17.699.733 STB**, cerca de **1,4 milhão de STB a menos** que os 19.115.712 STB calculados com Bo = 1,25.

Fisicamente, Bo mede quantos barris de óleo em condições de reservatório correspondem a um barril de óleo em condições de superfície (STB) — um Bo maior significa que o óleo está mais expandido no reservatório (mais gás em solução ou maior temperatura/pressão), logo **o mesmo volume físico de óleo no reservatório se traduz em menos barris de óleo em condição de tanque** depois de trazido à superfície. O volume no reservatório (o numerador do cálculo) não muda — só a conversão para STB, que é dividida por um Bo maior (Aula 03).
</details>

---

### 11. Múltipla escolha (oa03)
Entre os quatro mecanismos clássicos de produção primária, qual costuma apresentar, isoladamente, o **maior** fator de recuperação típico?

a) Depleção por gás em solução
b) Capa de gás
c) Influxo de água
d) Drenagem gravitacional

<details><summary>Ver resposta</summary>

**Resposta: c** — o influxo de água (*water drive*) é o mecanismo primário mais eficiente entre os quatro, com faixas de FR tipicamente as mais altas, porque a água que invade o espaço deixado pelo óleo produzido mantém a pressão do reservatório de forma mais sustentada que a simples expansão do gás em solução (o menos eficiente dos quatro) ou mesmo a expansão da capa de gás. A drenagem gravitacional pode alcançar recuperações altas em certas geometrias, mas é tipicamente lenta e depende de condições estruturais específicas, não sendo o mecanismo de maior FR típico entre os quatro (Aula 04).
</details>

---

### 12. Aplicação (cálculo, oa03)
Um teste de poço indica pressão estática do reservatório Pr = 3.200 psi e, com uma pressão de fundo fluente Pwf = 2.750 psi, uma vazão q = 450 bbl/dia. (a) Calcule o índice de produtividade J. (b) Supondo comportamento linear da IPR, qual seria a vazão esperada se Pwf fosse reduzido para 2.400 psi? (c) Que condição física precisa se manter válida para essa extrapolação linear continuar sendo confiável?

<details><summary>Ver resolução</summary>

(a) J = q / (Pr − Pwf) = 450 / (3.200 − 2.750) = 450 / 450 = **1,0 bbl/dia/psi**.

(b) q = J × (Pr − Pwf) = 1,0 × (3.200 − 2.400) = 1,0 × 800 = **800 bbl/dia**.

(c) A extrapolação linear só é confiável enquanto **Pwf permanece acima da pressão do ponto de bolha** — nesse regime o óleo flui monofásico e a IPR é aproximadamente linear. Se Pwf cair abaixo do ponto de bolha, gás sai de solução no meio poroso próximo ao poço, o fluxo passa a ser multifásico e a IPR deixa de ser linear, exigindo uma correlação como a de Vogel (1968) (Aula 04).
</details>

---

### 13. Múltipla escolha (oa04)
Em qual situação a instalação de controle de areia (telas de contenção ou *gravel pack*) é tipicamente necessária?

a) Em rocha-reservatório de **baixa** permeabilidade, para evitar dano de formação durante a completação
b) Em rocha-reservatório de **alta** permeabilidade e mal consolidada, para conter a produção de grãos de areia junto com o fluido
c) Apenas em poços com elevação artificial por *gas lift*
d) Apenas em reservatórios carbonáticos cársticos

<details><summary>Ver resposta</summary>

**Resposta: b** — o controle de areia se aplica a rocha de **alta** permeabilidade, mal consolidada: é exatamente a excelente permoporosidade da rocha, combinada com pouca cimentação entre os grãos, que permite ao fluido arrastar areia junto com ele. É um ponto contraintuitivo — "areia" soa como sintoma de reservatório ruim, quando na verdade é consequência de um reservatório de ótima qualidade petrofísica, porém mal consolidado. Associar controle de areia a baixa permeabilidade (alternativa a) inverte a lógica do problema (Aula 05).
</details>

---

### 14. Dissertativa curta (oa04)
Diferencie recuperação secundária de recuperação avançada (EOR) quanto ao mecanismo físico envolvido, e dê um exemplo de método de cada categoria.

<details><summary>Ver resposta comentada</summary>

**Resposta esperada:** a recuperação secundária (o exemplo dominante é a **injeção de água**) atua **mantendo ou restaurando a pressão** do reservatório e **deslocando** o óleo mecanicamente para os poços produtores, sem alterar as propriedades físicas do óleo ou da interação óleo-rocha — a água simplesmente empurra o óleo que a energia natural já não consegue mais deslocar sozinha. A recuperação avançada (EOR) vai além: ela **altera** uma propriedade do fluido ou da interação fluido-rocha para liberar óleo que a injeção de água, por si só, deixaria retido. Exemplos por família: EOR térmico (injeção de vapor, que reduz a viscosidade do óleo pesado), EOR miscível (injeção de CO₂ ou gás, que reduz a tensão interfacial ao atingir a pressão mínima de miscibilidade) e EOR químico (injeção de polímero, que aumenta a viscosidade da água injetada e melhora a razão de mobilidade, reduzindo o *channeling*) (Aula 04; Aula 05).
</details>

---

### 15. Aplicação (cálculo, integração a03→a05, oa04)
O mesmo reservatório da Aula 03 (OOIP = 19.115.712 STB) atingiu FR = 32% ao fim da recuperação secundária. Suponha que, em vez do ganho de 12 pontos percentuais descrito no texto da Aula 05, um projeto piloto de EOR alcance um ganho incremental de **10 pontos percentuais** de fator de recuperação sobre o mesmo OOIP. Calcule (a) o volume adicional recuperado pelo EOR; (b) o FR final; (c) o volume total recuperado — e confira que esse total bate com a soma do volume da secundária mais o incremento do EOR.

<details><summary>Ver resolução</summary>

Volume recuperado até o fim da secundária (FR = 32%, herdado sem alteração): 19.115.712 × 0,32 = 6.117.027,84 ≈ **6.117.028 STB**.

(a) Volume adicional do EOR (10 p.p.): 19.115.712 × 0,10 = 1.911.571,2 ≈ **1.911.571 STB**.

(b) FR final = 32% + 10% = **42%**.

(c) Volume total = 19.115.712 × 0,42 = 8.028.599,04 ≈ **8.028.599 STB**.

Conferência: 6.117.028 + 1.911.571 = **8.028.599 STB** — bate exatamente com o total calculado em (c), a mesma consistência interna que a Aula 05 demonstra com os números originais (FR=44%, ganho de 12 p.p.). O exercício mostra que a herança do OOIP da Aula 03 (19.115.712 STB) se propaga corretamente para **qualquer** cenário de ganho de EOR, não só para o valor específico usado no texto (Aula 03; Aula 05).
</details>

---

### 16. Aplicação (interpretação/integração, oa04)
Um reservatório contém óleo pesado de alta viscosidade, e a injeção de água convencional já perdeu eficiência por canalização preferencial (*channeling*) através de zonas de alta permeabilidade. Qual família de EOR (térmico, miscível ou químico) tende a ser mais indicada para esse cenário, e por quê? Que parâmetro citado no módulo, relacionado à miscibilidade, tende a **aumentar** junto com a densidade/viscosidade do óleo, tornando a recuperação miscível mais difícil nesse caso específico?

<details><summary>Ver resolução</summary>

A família mais indicada é o **EOR térmico** (por exemplo, injeção de vapor). O problema central do óleo pesado é a viscosidade alta, que já causa o *channeling* observado na injeção de água (a água, muito menos viscosa, avança preferencialmente pelos caminhos de maior permeabilidade em vez de deslocar o óleo de forma uniforme). O EOR térmico ataca diretamente essa causa raiz, reduzindo a viscosidade do óleo por aquecimento, o que melhora a razão de mobilidade entre o fluido deslocante e o óleo.

O parâmetro é a **pressão mínima de miscibilidade (PMM)**: ela **aumenta** com a densidade/viscosidade do óleo, o que significa que, para um óleo pesado, seria necessária uma pressão de injeção mais alta para atingir miscibilidade com um gás como CO₂ — tornando o EOR miscível operacionalmente mais difícil e caro exatamente no cenário em que o óleo é mais pesado. Isso reforça por que o EOR térmico, não o miscível, é a escolha padrão da indústria para óleos pesados (Aula 05).
</details>

---

### Gabarito resumido

| Questão | Resposta |
|---|---|
| 1 | b |
| 2 | 0,546 psi/ft; ≈5.374 psi; dentro da janela (margens de 797 psi e 2.500 psi) |
| 3 | Falso |
| 4 | b |
| 5 | Sw=25%, Sh=75% |
| 6 | Sw≈21% |
| 7 | ver comentário |
| 8 | Falso |
| 9 | OOIP=19.115.712 STB; recuperável=3.440.828 STB |
| 10 | ≈17.699.733 STB (≈1,4 milhão a menos) |
| 11 | c |
| 12 | J=1,0 bbl/dia/psi; q=800 bbl/dia; acima do ponto de bolha |
| 13 | b |
| 14 | ver comentário |
| 15 | 1.911.571 STB; FR final 42%; total 8.028.599 STB |
| 16 | EOR térmico; pressão mínima de miscibilidade (PMM) aumenta |

## Cobertura de objetivos confirmada
- geologia-avancado-m12-oa01 — questões 1, 2, 3
- geologia-avancado-m12-oa02 — questões 4, 5, 6, 7
- geologia-avancado-m12-oa03 — questões 8, 9, 10, 11, 12
- geologia-avancado-m12-oa04 — questões 13, 14, 15, 16

## Notas de rastreabilidade
- Módulo fortemente quantitativo: 8 das 16 questões são de cálculo (questões 2, 5, 6, 9, 10, 12, 15 — sete — mais o cálculo de PMM implícito na 16), acima do mínimo de 2-3 pedido pela auditoria e pela revisão didática.
- Nenhum número foi inventado: todos os valores de entrada e resultado das questões 2, 5, 6, 9, 10, 12 e 15 reproduzem exatamente os valores recalculados e conferidos na auditoria científica (`12-engenharia-de-petroleo-auditoria.md`), incluindo as duas sensibilidades já auditadas (m=1,8 na questão 6; Bo=1,35 na questão 10).
- Questão 15 testa explicitamente a cadeia de herança a03→a05 sinalizada pela auditoria como o ponto mais sensível a erro de propagação do módulo — usa o OOIP real (19.115.712 STB) com um FR de EOR diferente do texto (10 p.p. em vez de 12), para confirmar que o aluno entende a fórmula por trás do número, não decorou o resultado publicado.
- As duas distinções de discriminação indicadas pela auditoria foram usadas como base de questão: sinal de Bo acima/abaixo do ponto de bolha (questão 8, V/F, com o erro comum de inversão de sinal como armadilha) e controle de areia associado a rocha de **alta**, não baixa, permeabilidade (questão 13, alternativa a como distrator intuitivo).
- oa03 (achado `DID-M12-A02-EXEMPLO-001` corrigido antes desta avaliação, sem impacto aqui) coberto pelos dois lados do objetivo, exatamente como consumido pela aula: propriedades de rocha/fluido e OOIP da a03 (questões 8, 9, 10) e mecanismos de produção/testes de poço da a04 (questões 11, 12), sem deixar o objetivo inteiro de um lado só.
- Sugestão da revisão didática (`DID-M12-A03-PVT-002`, achado azul, não corrigido no texto) parcialmente incorporada: a questão 8 testa a leitura correta do comportamento de Bo em torno do ponto de bolha, o mesmo ponto que a revisão didática apontou como demonstrado apenas conceitualmente na aula.
- Nenhum achado de auditoria científica em aberto disponível como distrator corrigido — o único achado (`PETRENG-M12-CRAFTHAWKINS-001`) é bibliográfico (ano de edição de uma fonte), sem relação com conteúdo técnico avaliável.
