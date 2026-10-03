# Questionário final cumulativo — Módulo 06: Elementos de geomecânica

**Módulo:** [[06-elementos-de-geomecanica-modulo|Módulo 06 — Elementos de geomecânica]]
**Cobertura:** Aulas 01 a 06 — módulo completo. As questões priorizam o **encadeamento** entre aulas, não a repetição isolada de cada uma.
**Objetivos avaliados:** geologia-avancado-m06-oa01, geologia-avancado-m06-oa02, geologia-avancado-m06-oa03, geologia-avancado-m06-oa04

---

### 1. Aplicação integrada (cálculo)
Um perfil tem, de cima para baixo: 2 m de areia acima do nível d'água (γ = 17 kN/m³), 3 m de areia saturada (γsat = 20 kN/m³) e 4 m de argila normalmente adensada (γsat = 18 kN/m³). O nível d'água está a 2 m. Uma obra impõe Δσ = 60 kPa. Com e0 = 0,85 e Cc = 0,30 para a argila, calcule a tensão efetiva no **meio** da camada de argila e o recalque primário dessa camada. Use γw = 9,81 kN/m³.

<details>
<summary>Ver resolução</summary>

**Passo 1 — Localizar o ponto.** O meio da argila está a 2 + 3 + 2 = **7 m** de profundidade.

**Passo 2 — Tensão total a 7 m:**
σv = (17 × 2) + (20 × 3) + (18 × 2) = 34 + 60 + 36 = **130 kPa**

**Passo 3 — Poropressão** (coluna d'água de 7 − 2 = 5 m):
u = 9,81 × 5 = **49,05 kPa**

**Passo 4 — Tensão efetiva:**
σ'v0 = 130 − 49,05 = **80,95 ≈ 81,0 kPa**

**Passo 5 — Recalque** (argila normalmente adensada, uma só parcela com Cc; H = 4 m, a espessura **total** da camada, ainda que σ'v0 tenha sido calculada no meio dela):
ρ = (0,30 × 4)/(1 + 0,85) × log[(81,0 + 60)/81,0]
ρ = (1,20/1,85) × log(1,7407) = 0,6486 × 0,24067 = **0,156 m ≈ 15,6 cm**

**Comentário:** a questão encadeia três aulas — pesos específicos (a02), perfil de tensão efetiva (a03) e cálculo de recalque (a05). O ponto de método mais importante é usar σ'v0 do **meio** da camada como tensão representativa, mas a espessura **total** H no cálculo do recalque: a tensão média governa a deformação média, que age sobre toda a espessura.
</details>

---

### 2. Múltipla escolha
O princípio das tensões efetivas de Terzaghi afirma que σ' = σ − u. A segunda parte do princípio, frequentemente esquecida, afirma que:

a) A poropressão é sempre positiva abaixo do nível d'água
b) Todo efeito mensurável — resistência, compressão, distorção — decorre exclusivamente de mudanças na tensão efetiva
c) A tensão efetiva é a tensão física real nos pontos de contato entre grãos
d) A tensão total é sempre maior que a efetiva

<details>
<summary>Ver resposta</summary>

**Resposta: b**

É essa segunda parte que dá ao princípio seu poder preditivo: se σ e u aumentam igualmente, σ' não muda e o solo não sente nada. A alternativa "c" enuncia um erro conceitual que a aula adverte explicitamente — a tensão efetiva é uma grandeza macroscópica definida por σ − u, não a tensão nos contatos intergranulares (que é muito maior, dada a área real de contato ínfima). A alternativa "d" falha na franja capilar, onde u é negativa e σ' > σ (Aula 03).
</details>

---

### 3. Verdadeiro ou Falso
"Compactação e adensamento são o mesmo processo físico, diferindo apenas na escala de tempo."

<details>
<summary>Ver resposta</summary>

**Falso.** Diferem em quatro aspectos, não só no tempo.

**Compactação** (a02) é densificação **mecânica** de um solo geralmente **não saturado**, por energia aplicada (impacto, vibração, amassamento), com expulsão de **ar**, e é praticamente instantânea. **Adensamento** (a05) é redução de volume de um solo **saturado**, sob carga sustentada, por expulsão de **água**, governada pela condutividade hidráulica, e leva de meses a décadas em argilas. Confundir os dois leva a erros graves de previsão de prazo e de escolha de ensaio (Proctor versus edométrico).
</details>

---

### 4. Aplicação (cálculo)
Uma areia tem Gs = 2,66 e e = 0,66. Calcule o gradiente hidráulico crítico e explique o que ocorre no fundo de uma escavação se o gradiente ascendente de saída atingir esse valor.

<details>
<summary>Ver resolução</summary>

icr = (Gs − 1)/(1 + e) = (2,66 − 1)/(1 + 0,66) = 1,66/1,66 = **1,00**

**O que ocorre:** nesse gradiente, a força de percolação ascendente (j = i·γw) iguala exatamente o peso submerso do solo. A tensão efetiva vertical **zera**: os grãos deixam de transmitir carga uns aos outros, e como a resistência ao cisalhamento de uma areia limpa é τf = σ'n·tan φ' com c' = 0, a resistência disponível cai a **zero**. O solo passa a se comportar como um fluido denso — o fenômeno de areia movediça (*quicksand*) ou levantamento de fundo (*heave*).

**Comentário:** a coincidência numérica icr ≈ 1,00 para valores típicos de Gs e e é a origem da regra prática de que o gradiente crítico é próximo da unidade — mas é uma coincidência de valores típicos, não uma identidade: solos com e muito alto ou muito baixo desviam disso (Aulas 03 e 04).
</details>

---

### 5. Múltipla escolha
Um ensaio de laboratório em amostra de rocha intacta mede k = 10⁻¹¹ m/s, enquanto um ensaio Lugeon no mesmo maciço indica absorção correspondente a k ≈ 10⁻⁶ m/s. A explicação mais provável é:

a) Erro de execução em um dos dois ensaios
b) O fluxo no maciço é dominado pelas descontinuidades, não pela matriz rochosa
c) A amostra de laboratório estava saturada e o maciço não
d) O ensaio Lugeon mede porosidade, não condutividade

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Cinco ordens de grandeza de diferença entre matriz e maciço é o resultado **esperado**, não uma anomalia. Em meios fissurados o fluxo ocorre pelas descontinuidades e obedece à lei cúbica (Q proporcional ao cubo da abertura), de modo que uma única fratura aberta pode conduzir mais água que todo o volume de matriz rochosa. O ensaio de laboratório mede a matriz; o Lugeon mede o maciço com suas fraturas — e é o segundo que interessa ao projeto. É a aplicação direta do alerta "ensaio de laboratório mede o corpo de prova, não o maciço" (Aula 04, retomando o Módulo 05, Aula 04).
</details>

---

### 6. Dissertativa curta
Duas argilas têm exatamente o mesmo Cc, o mesmo e0 e a mesma espessura, e recebem a mesma carga. Uma recalca 2 cm e a outra 18 cm. Explique como isso é possível.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:** as duas diferem na **tensão de pré-adensamento σ'p**, isto é, no histórico de tensões. Na primeira, a carga final permanece **abaixo** de σ'p, e a deformação segue o trecho de recompressão, com o índice Cr — bem menor que Cc (tipicamente 5 a 10 vezes). Na segunda, a carga ultrapassa σ'p e a trajetória entra na **reta virgem**, governada por Cc, produzindo deformação muito maior. O OCR (= σ'p/σ'v0) de cada uma é o parâmetro que distingue os dois casos (Aula 05).

**Comentário:** por isso a determinação correta de σ'p pela construção de Casagrande é frequentemente a decisão mais importante de todo um estudo de fundação — mais do que a precisão em Cc. Ela decide **qual índice** se aplica, e não apenas o valor dele.
</details>

---

### 7. Verdadeiro ou Falso
"Como o coeficiente de adensamento cv é uma propriedade do solo, o mesmo valor obtido no ensaio edométrico pode ser aplicado a qualquer faixa de carregamento da obra."

<details>
<summary>Ver resposta</summary>

**Falso.**

O cv varia com o nível de tensão, e costuma **cair** quando o solo passa do trecho de recompressão para a reta virgem. Adotar um valor único é uma simplificação comum e aceitável, mas exige escolher o estágio do ensaio cuja faixa de tensões corresponde à da obra — não o primeiro nem o último da tabela por conveniência. Aplicar um cv de recompressão a um carregamento que leva o solo à reta virgem subestima o tempo de adensamento (Aula 05).
</details>

---

### 8. Múltipla escolha
Um escorregamento antigo é reativado num talude de argila. Para analisar a estabilidade da superfície de ruptura preexistente, o parâmetro de resistência apropriado é:

a) A resistência de pico, por ser o valor máximo mobilizável
b) A resistência residual (φ'r)
c) A resistência não drenada su obtida em ensaio UU
d) O ângulo de atrito de estado crítico φ'cv

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Numa superfície de ruptura **preexistente**, as partículas lamelares de argila já foram reorientadas paralelamente ao plano por deformações muito grandes, e a resistência disponível é a **residual** (φ'r) — inferior tanto ao pico quanto ao estado crítico. Usar a resistência de pico (alternativa "a") é o erro clássico da análise de escorregamentos reativados e leva a um fator de segurança perigosamente otimista. A alternativa "d" seria apropriada para um solo remoldado atingindo grandes deformações **sem** a reorientação característica das argilas em superfície preexistente (Aula 06).
</details>

---

### 9. Dissertativa curta
Explique por que o exemplo trabalhado da Aula 04 (vazão de 1,2 L/s e fator de segurança de 1,04) mostra que as medidas corretivas devem atuar sobre o gradiente, e não sobre a vazão. Cite duas medidas possíveis.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:** o risco não é hidráulico no sentido de volume — 1,2 L/s é trivialmente bombeável. O risco é de **anulação da tensão efetiva** no fundo da escavação, e isso depende do **gradiente de saída** comparado ao gradiente crítico, não da vazão total. Reduzir a vazão sem reduzir o gradiente não melhora a segurança — e pode piorá-la, se o fluxo remanescente se concentrar em pontos de saída. Duas medidas que atuam sobre o gradiente: (1) **aprofundar a ficha da parede-diafragma**, alongando o caminho de percolação e reduzindo i para a mesma perda de carga; (2) **rebaixar o lençol** por poços a montante, reduzindo a perda de carga total H; (3) **lastrear o fundo com filtro graduado**, que aumenta a tensão total resistente e controla a saída de partículas (Aula 04).

**Comentário:** o ponto generaliza para o alerta de "O que não concluir" da aula — uma cortina de vedação mal executada pode reduzir a vazão e, ao concentrar o fluxo restante, elevar gradientes locais e piorar o risco de piping.
</details>

---

### 10. Aplicação (interpretação de campanha)
Uma obra prevê aterro de 6 m sobre uma planície com solo mole. Proponha uma campanha de investigação mínima, justificando cada método pelo parâmetro que ele fornece e pela aula em que esse parâmetro é usado.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada — os elementos essenciais:**

1. **Sondagens SPT** — perfil estratigráfico, posição do nível d'água (indispensável para o perfil de tensão efetiva da a03) e delimitação preliminar da camada mole. Base de qualquer campanha.
2. **Amostragem indeformada (Shelby)** na camada mole — condição necessária para os ensaios seguintes; amostra do amostrador do SPT não serve.
3. **Ensaios edométricos** sobre as amostras indeformadas — fornecem e0, Cc, Cr, σ'p e cv, isto é, **todos** os parâmetros do cálculo de magnitude e de prazo do recalque (a05). Sem eles não há previsão de recalque.
4. **Ensaio de palheta (*vane*) em campo** — su in situ na argila mole, para a análise de estabilidade do aterro em condição **não drenada**, que é a condição crítica de um carregamento (a06).
5. **CPTu** — perfil contínuo de qc, fs e u2, delimitando com precisão a espessura e a continuidade lateral da camada mole e identificando lentes drenantes que o SPT (medindo a cada metro) não veria — informação decisiva para definir se a drenagem é simples ou dupla, o que altera o prazo previsto por um fator de 4 (a04 e a05).
6. **Ensaios de caracterização** (granulometria, limites de Atterberg) — classificação SUCS/AASHTO e verificação de coerência dos demais parâmetros (a01).

**Comentário:** a resposta completa demonstra o encadeamento do módulo inteiro: cada método é escolhido pelo parâmetro que alimenta um cálculo específico, e não por hábito. Uma resposta que liste apenas sondagens, sem amostragem indeformada nem ensaio de adensamento, incorre exatamente no erro discutido na questão 8 do parcial 2.
</details>

---

### 11. Múltipla escolha
Um maciço rochoso tem RMR = 65 e a rocha intacta tem Ei = 50 GPa. Pela correlação de Bieniawski (1978), o módulo de deformabilidade do maciço é:

a) 50 GPa, igual ao da rocha intacta
b) 30 GPa
c) 130 GPa
d) A correlação não é aplicável a esse RMR

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Em = 2·RMR − 100 = 2×65 − 100 = 130 − 100 = **30 GPa**.

A correlação é aplicável porque RMR = 65 > 50, o limite de validade da expressão linear de Bieniawski (abaixo dele ela produziria valores negativos, motivo pelo qual Serafim & Pereira propuseram a forma exponencial). O resultado ilustra o ponto central: o maciço conserva 30/50 = 60% do módulo da rocha intacta, porque as descontinuidades fecham e deslizam sob carga. A alternativa "a" comete o erro de aplicar Ei de laboratório diretamente ao maciço, superestimando a rigidez e subestimando o recalque (Aula 05, retomando o Módulo 05, Aula 06).
</details>

---

### 12. Dissertativa curta
Ao longo do módulo, o princípio das tensões efetivas reapareceu nas aulas 03, 04, 05 e 06. Descreva, em uma frase para cada aula, qual pergunta diferente ele respondeu em cada uma.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:**

- **a03** — Qual é o estado de tensão efetiva num ponto do perfil, dado o peso das camadas e a posição do nível d'água (σ' = σ − u, e o perfil geostático).
- **a04** — Como o **fluxo** de água altera esse estado, elevando ou reduzindo u e podendo anular σ' quando o gradiente ascendente atinge o crítico.
- **a05** — Como σ' **evolui no tempo** sob carga sustentada, transferindo-se progressivamente da água para o esqueleto sólido, e quanta deformação essa transferência produz.
- **a06** — Como σ' determina a **resistência disponível** ao cisalhamento (τf = c' + σ'n·tan φ'), e como a condição de drenagem decide se a análise usa σ' ou su.

**Comentário:** o que se espera aqui não é memorização, mas o reconhecimento de que o módulo tem um único eixo conceitual visto de quatro ângulos — estado, alteração por fluxo, evolução no tempo, e consequência na ruptura. Quem enxerga esse eixo aplica o princípio corretamente em situações novas; quem estudou as aulas como quatro tópicos separados tende a cometer justamente os erros listados em cada "Erros comuns".
</details>

---

### Gabarito resumido

| Questão | Resposta |
|---|---|
| 1 | σ'v0 ≈ 81,0 kPa; ρ ≈ 15,6 cm |
| 2 | b |
| 3 | Falso |
| 4 | icr = 1,00; tensão efetiva zera (areia movediça / heave) |
| 5 | b |
| 6 | ver comentário (diferença de σ'p / OCR) |
| 7 | Falso |
| 8 | b |
| 9 | ver comentário |
| 10 | ver comentário |
| 11 | b (30 GPa) |
| 12 | ver comentário |
