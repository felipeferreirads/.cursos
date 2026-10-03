# Questionário final cumulativo — Módulo 09: Geometalurgia

**Módulo:** [[09-geometalurgia-modulo|Módulo 09 — Geometalurgia]]
**Cobertura:** Aulas 01 a 06 — módulo completo. As questões priorizam o **encadeamento** entre aulas — a composição dos tetos de recuperação (partição × liberação), a reciprocidade energia/capacidade, e a não aditividade de domínios geometalúrgicos — e não a repetição isolada de cada aula.
**Objetivos avaliados:** `geologia-avancado-m09-oa01`, `geologia-avancado-m09-oa02`, `geologia-avancado-m09-oa03`, `geologia-avancado-m09-oa04`
**Pontuação total:** 100 pontos · o gabarito fica oculto; responda antes de abrir.

---

### 1. Aplicação integrada (cálculo) — `geologia-avancado-m09-q20` · oa01 → oa02 (a02 → a03) · 15 pts
Um minério de cobre tem **85 %** do seu cobre em minerais sulfetados flotáveis (partição medida por mineralogia de processo, Aula 02); o restante está em óxidos e silicatos que a flotação não recupera. No `P80` de moagem escolhido, a liberação da calcopirita, medida por análise modal automatizada, é de **90 %** (Aula 03); partículas liberadas recuperam 96 % e partículas mistas, 35 %.

Calcule: (a) a recuperação esperada considerando **só** a liberação (ignorando a partição); (b) o teto composto real, considerando **também** a partição; (c) explique por que os dois tetos se multiplicam, e por que o resultado combinado pode ficar **abaixo** do menor dos dois tetos individuais.

<details>
<summary>Ver resolução</summary>

**(a) Recuperação por liberação (ignorando a partição):**
`R_liberação = 0,90 × 0,96 + 0,10 × 0,35 = 0,864 + 0,035 = 0,899 → 89,9 %`

**(b) Teto composto (partição × liberação):**
`R_total = 0,85 × 0,899 = 0,764 → 76,4 %`

**(c) Interpretação:** os dois tetos multiplicam-se porque descrevem perdas **independentes e sucessivas** — primeiro perde-se o cobre que nenhuma rota de flotação alcança (15 %, partição), depois perde-se parte do que resta por travamento residual (10,1 % do que sobrou, liberação). O produto de duas frações menores que 1 é sempre **menor ou igual ao menor dos dois fatores** (`76,4 % < 85 %`, o menor teto individual) — é essa relação que a Aula 03 resume em "os dois tetos multiplicam-se; o menor deles é sempre o que manda": nenhum ajuste de liberação recupera o cobre barrado pela partição, e nenhuma correção de partição recupera o cobre barrado pela liberação. O teto combinado é sempre mais restritivo que qualquer um dos dois tomado isoladamente.
</details>

---

### 2. Aplicação integrada (cálculo) — `geologia-avancado-m09-q21` · oa03 → oa04 (a04 → a06) · 15 pts
Uma planta é dimensionada para processar **15 Mt/ano** de um minério de `Wi = 14,0 kWh/t`, a um dado `P80`. Um domínio geometalúrgico mais duro do mesmo depósito tem `Wi = 18,5 kWh/t`.

(a) Calcule quantos por cento a mais de energia por tonelada esse domínio mais duro exige, para o mesmo `P80`. (b) Calcule a capacidade real da planta (em Mt/ano) ao processar esse domínio, a potência instalada fixa. (c) Expresse a perda de capacidade em %, e explique por que os percentuais de (a) e (c) **não são o mesmo número**, mesmo vindo do mesmo fato físico.

<details>
<summary>Ver resolução</summary>

**(a)** `18,5 / 14,0 = 1,321 →` **+32,1 % de energia por tonelada**

**(b)** `Capacidade = 15 × (14,0 / 18,5) = 15 × 0,757 = 11,35 Mt/ano`

**(c)** `Perda = (15 − 11,35) / 15 = 3,65 / 15 = 0,243 →` **−24,3 % de capacidade**

**Por que os dois percentuais diferem:** energia por tonelada e toneladas por ano são grandezas **recíprocas**, e o inverso de `(1 + x)` não é `(1 − x)`. Um aumento de 32,1 % na energia específica (`18,5/14,0`) corresponde a uma queda de 24,3 % na capacidade (`14,0/18,5`), não de 32,1 %. Trocar um percentual pelo outro — tratá-los como se fossem o mesmo número com sinal invertido — é o erro aritmético mais comum desse raciocínio, nomeado explicitamente na Aula 06.
</details>

---

### 3. Dissertativa — `geologia-avancado-m09-q22` · oa04 (a06) · 12 pts
Um modelo de recursos tradicional estimaria o Work Index e a recuperação de um bloco de blenda por krigagem, do mesmo modo que estima o teor. Explique por que essa prática está **errada** para Work Index e para recuperação, mas **correta** para teor, e quais são as duas alternativas corretas de modelagem citadas na Aula 06.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:**

- **Teor é aditivo:** a blenda é a média ponderada pelas massas dos componentes; é por isso que a krigagem — um estimador linear — funciona para teor.
- **Work Index não é aditivo:** o componente mais duro domina o tempo de residência no moinho e a energia se distribui de forma não linear; a moabilidade da blenda tende a ser pior que a média ponderada sugere.
- **Recuperação não é aditiva:** minerais de ganga de um minério podem contaminar a química de flotação do outro, um minério pode consumir o reagente que faltaria ao outro, e a cinética muda; a recuperação de uma blenda pode ficar abaixo da média das recuperações isoladas.
- **Alternativas corretas:** (i) modelar a variável primária (Wi, recuperação) a partir de **proxies que sejam aditivas** — composição elementar, mineralogia modal; ou (ii) usar **simulação geoestatística com modelos de mistura não lineares**, que propaga a incerteza em vez de suprimi-la numa média única.

**Comentário:** é o ponto que mais confunde quem traz o instinto da estimativa de teor — e é o conteúdo mais importante do módulo, porque decide como (e como não) a variabilidade metalúrgica entra no modelo de blocos.
</details>

---

### 4. Múltipla escolha — `geologia-avancado-m09-q23` · oa01 → oa04 (a01, a06) · 8 pts
No modelo geometalúrgico de blocos (Aula 06), a relação entre proxies densas e variáveis primárias esparsas (Aula 01) é construída:

- a) Medindo a variável primária em todos os furos, já que ela é a que realmente importa
- b) Calibrando uma função proxy → primária nas amostras que têm as duas medidas, e aplicando-a aos blocos que só têm as proxies — preferindo proxies fisicamente ligadas à causa
- c) Substituindo a variável primária pela proxy em todo o modelo, pois são numericamente equivalentes
- d) Usando qualquer proxy que apresente correlação estatística alta, mesmo sem mecanismo físico, pois o ajuste estatístico já basta

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A variável primária é cara e esparsa por definição — medi-la em todos os furos anularia a razão de existir da proxy ("a"). A modelagem calibra a função nas amostras que têm as duas medidas e a aplica aos blocos com só a proxy, preferindo proxies com mecanismo físico (dureza → Wi; razão de solubilidade → recuperação de flotação) a correlações estatísticas sem causa, que não generalizam para fora da amostra ("d"). Primária e proxy nunca são a mesma coisa ("c").
</details>

---

### 5. Verdadeiro ou Falso (justifique) — `geologia-avancado-m09-q24` · oa02 → oa04 (a03, a06) · 8 pts
"Se dois domínios geológicos (duas litologias diferentes) têm a mesma resposta metalúrgica medida, eles devem ser tratados como domínios geometalúrgicos distintos, porque a classificação geológica sempre prevalece sobre a resposta de processo."

<details>
<summary>Ver resposta</summary>

**Falso.**

É exatamente o inverso do princípio da Aula 06: o domínio geometalúrgico é **validado pelos dados de processo**, não presumido do mapa geológico. Se duas litologias distintas respondem da mesma forma ao processamento (mesma recuperação, mesma moabilidade), elas podem — e devem — ser tratadas como um único domínio geometalúrgico, mesmo sendo dois domínios geológicos. É o espelho do exemplo do granito são/cloritizado (uma litologia, duas respostas): aqui são duas litologias, uma resposta.
</details>

---

### 6. Aplicação (cálculo) — `geologia-avancado-m09-q25` · oa02 → oa03 (a03, a05) · 14 pts
A um dado `P80`, o grau de liberação medido da calcopirita é 80 %; partículas liberadas recuperam 96 % e mistas, 30 %, por flotação. Na planta em operação, as correntes medidas são: alimentação `f = 0,90 % Cu`, concentrado `c = 25,0 % Cu`, rejeito `t = 0,20 % Cu`.

(a) Calcule a recuperação teórica esperada pelo modelo de liberação. (b) Calcule a recuperação real medida pela fórmula de dois produtos. (c) Compare as duas e proponha uma explicação plausível para a diferença, lembrando do viés de medida da liberação em seção polida.

<details>
<summary>Ver resolução</summary>

**(a)** `R_teórica = 0,80 × 0,96 + 0,20 × 0,30 = 0,768 + 0,06 = 0,828 → 82,8 %`

**(b)** `R_real = [c(f − t)] / [f(c − t)] = [25,0 × (0,90 − 0,20)] / [0,90 × (25,0 − 0,20)]`
`R_real = (25,0 × 0,70) / (0,90 × 24,80) = 17,5 / 22,32 = 0,784 → 78,4 %`

**(c)** A recuperação real medida na planta (78,4 %) é **inferior** à recuperação teórica projetada a partir da liberação (82,8 %). Uma explicação plausível: o grau de liberação de 80 % foi medido em seção polida 2D, que **superestima** sistematicamente a liberação real (viés estereológico) — a liberação 3D verdadeira é menor que 80 %, de modo que a recuperação teoricamente projetada a partir dela também é otimista. A planta, sujeita à liberação real (menor) e a perdas adicionais (cinética, entranhamento, distribuição de tamanho), entrega uma recuperação abaixo da estimativa baseada na medida em seção polida.
</details>

---

### 7. Múltipla escolha — `geologia-avancado-m09-q26` · oa02 → oa03 (a03, a05) · 8 pts
Uma planta decide aumentar o número de estágios de limpeza (*cleaner*) da flotação, mantendo a mesma moagem. O resultado esperado é:

- a) Deslocamento de toda a curva teor-recuperação para fora, ganhando teor e recuperação simultaneamente
- b) Deslocamento ao longo da mesma curva, trocando recuperação por teor de concentrado mais alto — sem ganho líquido
- c) Nenhum efeito, pois estágios de limpeza não alteram nem teor nem recuperação
- d) Redução da liberação mineral, pois mais limpeza sobremoi as partículas

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Mais estágios de limpeza, com a mesma moagem (mesma liberação), é **andar sobre a mesma curva** teor-recuperação: ganha-se teor de concentrado e perde-se recuperação, sem deslocar a curva. Só moer mais fino (mais liberação) ou trocar de minério **desloca** a curva inteira e melhora as duas grandezas simultaneamente — o que a limpeza, isoladamente, não faz. "d" inventa um mecanismo (limpeza não muda o tamanho de partícula).
</details>

---

### 8. Dissertativa curta — `geologia-avancado-m09-q27` · oa01 → oa04 (a01, a06) · 10 pts
Explique por que um programa geometalúrgico bem desenhado usa **muitos** testes de bancada baratos e **poucos** testes de piloto caros, e como essa lógica de amostragem se conecta à construção dos domínios geometalúrgicos e do modelo de blocos da Aula 06.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:** os testes de bancada, de gramas a poucos quilos, são baratos o suficiente para serem feitos em dezenas ou centenas de amostras, cobrindo de forma estratificada toda a variabilidade do depósito — litologias, estágios de alteração, zonas de intemperismo. Os testes de piloto, com toneladas e custo alto, validam e calibram o projeto em poucas amostras compostas. Essa cobertura densa e barata é exatamente o que alimenta a construção dos **domínios geometalúrgicos** (que precisam de resposta metalúrgica medida em número suficiente de pontos para serem validados, não presumidos do mapa geológico) e a calibração da função **proxy → primária** do modelo de blocos: sem amostragem estratificada, a relação proxy-primária seria calibrada só onde o minério é mais fácil de amostrar, e o modelo propagaria essa lacuna a todo o depósito.
</details>

---

### 9. Múltipla escolha — `geologia-avancado-m09-q28` · oa04 (a06) · 5 pts
Adotar uma única recuperação média e uma única capacidade média para todo o depósito no estudo de viabilidade tende a:

- a) Subestimar o VPL, por ser uma hipótese conservadora
- b) Enviesar o VPL para cima e subestimar o risco, sobretudo se o minério de pior resposta for lavrado nos primeiros anos
- c) Não ter efeito no VPL, pois a média sempre se realiza no longo prazo
- d) Superestimar apenas o custo de energia, sem afetar a receita

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Ignorar a variabilidade enviesa o VPL para cima: a planta é dimensionada para um minério médio que não existe em lugar nenhum da mina, e o minério de transição — de pior recuperação e maior dureza — costuma estar sequenciado nos primeiros anos, justamente os que o desconto menos penaliza. É o padrão por trás de rampas de produção que se arrastam e de estudos de viabilidade que não se confirmam. "a" inverte o efeito; "c" ignora que o fluxo de caixa é descontado ano a ano, não uma média atemporal; "d" restringe indevidamente o efeito só ao custo.
</details>

---

### 10. Múltipla escolha — `geologia-avancado-m09-q29` · oa01 → oa04 (a01, a06) · 5 pts
Qual das alternativas resume corretamente a relação entre o modelo geometalúrgico e o modelo de recursos minerais?

- a) O modelo geometalúrgico substitui o modelo de recursos, pois a recuperação é mais importante que o teor
- b) O modelo geometalúrgico acrescenta, a cada bloco do modelo de recursos, atributos de recuperação, energia/moabilidade, capacidade e consumo de reagente — sem alterar a estimativa de teor —, permitindo calcular receita, custo e ritmo por bloco
- c) O modelo geometalúrgico só é necessário quando o depósito tem baixo teor
- d) O modelo geometalúrgico dispensa a necessidade de testes metalúrgicos, pois deriva tudo da mineralogia teórica

<details>
<summary>Ver resposta</summary>

**Resposta: b**

É a síntese da Aula 01, reafirmada na Aula 06: a geometalurgia **complementa** o modelo de recursos, adicionando camadas de recuperação, energia, capacidade e consumo de reagente a cada bloco, sem tocar na estimativa de teor. Disso decorrem receita, custo de processamento e tempo de ocupação da planta por bloco — o que alimenta o sequenciamento de lavra e o cálculo de VPL. "a" e "c" propõem substituição ou condicionalidade que a aula rejeita explicitamente; "d" ignora que a relação proxy-primária só existe porque testes metalúrgicos foram feitos em algumas amostras.
</details>

---

## Gabarito resumido

| Questão | ID | Resposta |
|---|---|---|
| 1 | q20 | R_liberação 89,9 %; teto composto 76,4 % (< menor teto individual, 85 %) |
| 2 | q21 | +32,1 % energia; capacidade 11,35 Mt/ano; −24,3 % (percentuais recíprocos, não simétricos) |
| 3 | q22 | ver comentário (teor aditivo; Wi e recuperação não aditivos; proxies aditivas ou simulação de mistura) |
| 4 | q23 | b |
| 5 | q24 | Falso (domínio validado por dados de processo; duas litologias com mesma resposta = um domínio) |
| 6 | q25 | R_teórica 82,8 %; R_real 78,4 %; diferença por viés estereológico (liberação medida é otimista) |
| 7 | q26 | b |
| 8 | q27 | ver comentário (bancada barata mapeia; piloto caro calibra; alimenta domínios e modelo proxy-primária) |
| 9 | q28 | b |
| 10 | q29 | b |
