# Auditoria científica: Módulo 30 — Métodos numéricos para geociências

**Auditado em:** 2026-08-29
**Material:** `30-metodos-numericos-geociencias/` — cinco aulas
**Modo:** audit (Fase 1, 2026-08-29) → **audit-and-fix** (Fase 2, 2026-08-29, após autorização do usuário — ver "Correções aplicadas" no fim)
**Profundidade:** full
**Escopo:** erro numérico e condicionamento; eliminação de Gauss, Gauss-Seidel e dominância diagonal; bisseção e Newton-Raphson; interpolação, diferenças finitas e mínimos quadrados; trapézio, Simpson, Euler e Runge-Kutta. Verificação independente de **toda a aritmética dos exemplos trabalhados** e das âncoras geocientíficas (isócrona, geoterma, decaimento radioativo).
**Veredito final: Aprovado** — os 4 achados (1 🔴, 3 🟠) foram corrigidos em 2026-08-29. Nenhum achado em aberto.

## Resumo

🔴 1 erro · 🟠 3 imprecisões · 🟡 0 desatualizados · 🔵 0 sem fonte · ⚪ 0 controversos. Verificadas e corretas: 21 alegações.

O corpo conceitual do módulo está sólido: as definições, as ordens de convergência e as âncoras geológicas foram todas confirmadas contra fonte. **Os quatro achados estão concentrados nos exemplos trabalhados** — isto é, na aritmética e nas comparações numéricas, não na teoria. Isso importa porque, num módulo de cálculo numérico, o exemplo trabalhado é o que o aluno reproduz e o que o questionário tende a reaproveitar.

## Achados

### 🔴 1. O exemplo trabalhado afirma que Gauss-Seidel convergiria num sistema em que ele diverge

**claim_id:** `NUM-M30A02-GAUSSSEIDEL-002`
**Tipo:** erro factual (com inconsistência interna)
**Onde:** `30-metodos-numericos-geociencias-aula-02-sistemas-lineares.md` · Exemplo trabalhado, parágrafo final ("O que Gauss-Seidel faria diferente")
**Está escrito:** "isolando cada incógnita (a = 1−b−c; b da equação X; c da equação Y) e partindo de um palpite (a=b=c≈0,33), o método recalcularia as três repetidamente até convergir para os mesmos valores"

**Problema:** com **exatamente** o arranjo prescrito na frase — *a* isolado da equação de soma, *b* da equação do traçador X, *c* da equação do traçador Y — o método de Gauss-Seidel **diverge**, e diverge de forma explosiva. A matriz de iteração desse arranjo tem raio espectral ρ ≈ **9,87**; como a convergência de Gauss-Seidel exige ρ < 1, o método se afasta da solução a cada repetição. Simulação numérica partindo de a=b=c=0,33 (a mesma sugerida no texto):

| iteração | a | b | c |
|---|---|---|---|
| 1 | 0,3334 | 0,2334 | 0,9661 |
| 2 | −0,1995 | −0,5660 | 7,0944 |
| 3 | −5,5284 | −8,2396 | 67,4174 |
| 5 | −577,6 | −827,8 | 6.530,8 |
| 10 | −5,4 × 10⁷ | −7,7 × 10⁷ | 6,1 × 10⁸ |

A causa é a que a própria aula ensina duas seções antes: o sistema **não tem dominância diagonal** nesse arranjo, e não a tem em arranjo nenhum. Na equação do traçador Y, o coeficiente de *c* é 0,10 contra 0,70 + 0,30 = 1,00 dos demais — o oposto de dominância diagonal.

Isto é também uma **inconsistência interna**, e essa é a parte mais grave: a mesma aula lista, em "Erros comuns", exatamente este erro — *"Aplicar Gauss-Seidel sem checar dominância diagonal e assumir que vai convergir. Sem essa checagem [...] o método pode divergir silenciosamente"* — e então o comete no seu próprio exemplo trabalhado, sem checar. Um aluno que fizer o que a aula manda (checar antes de aplicar) vai concluir que a aula está errada; um aluno que confiar no exemplo vai internalizar que Gauss-Seidel converge em qualquer sistema de balanço de massa.

**Correção proposta (preferida):** transformar o parágrafo no contraexemplo que ele já é. Em vez de afirmar convergência, escrever que este sistema **não** satisfaz dominância diagonal (mostrando a equação Y: 0,10 contra 1,00), que aplicar Gauss-Seidel a ele nesse arranjo diverge, e que é por isso que a checagem vem antes da aplicação. Isso corrige o fato, elimina a contradição e reforça o objetivo de aprendizagem `geologia-m30-oa02` ("diagnosticar quando o método iterativo converge") melhor do que a versão atual.

**Correção alternativa (se a intenção era mostrar convergência):** reordenar as equações — isolar *a* da equação X, *b* da equação Y e *c* da equação de soma dá ρ ≈ 0,913 e converge (devagar). Mas continua sem dominância diagonal, então exigiria explicar que a condição é suficiente e não necessária. Menos didático; registrado apenas para o caso de o autor preferir manter um exemplo convergente.

**Fonte:** critério de convergência (ρ(T) < 1 é condição necessária e suficiente; dominância diagonal estrita é suficiente e não necessária) — Burden & Faires, *Numerical Analysis*, 9ª ed., cap. sobre métodos iterativos; Chapra & Canale, *Numerical Methods for Engineers*, 7ª ed.; confirmação independente em [ScienceDirect, Jacobi Iteration overview](https://www.sciencedirect.com/topics/computer-science/jacobi-iteration) e [ELA, *Convergence on Gauss-Seidel iterative methods*](https://emis.de/ft/34278) · **Nível:** revisada por pares
**Verificação:** ρ e a trajetória de divergência calculados diretamente sobre o sistema publicado na aula (numpy, 2026-08-29). Reprodutível.
**Confiança:** confirmado
**Também aparece em:** nenhum outro arquivo — o módulo 30 ainda não tem questionário nem flashcards. **É por isso que este achado precisa ser fechado antes de a avaliação ser gerada:** um questionário escrito sobre este exemplo nasceria com gabarito errado.

---

### 🟠 2. O erro relativo do gradiente geotérmico é apresentado como "até ~33%" quando o limite propagado é o dobro

**claim_id:** `NUM-M30A01-PROPGRAD-001`
**Tipo:** impreciso (propagação de erro subestimada)
**Onde:** `30-metodos-numericos-geociencias-aula-01-erro-numerico.md` · Exemplo trabalhado, Situação 2, Passo 2
**Está escrito:** "o erro em cada temperatura (±0,1 °C) é 1/3 do próprio numerador (0,3 °C) — um erro relativo de até ~33% só de leitura"

**Problema:** a primeira metade da frase é aritmeticamente correta (0,1 / 0,3 = 1/3). A segunda metade não segue dela. O numerador do gradiente é uma **diferença de duas leituras**, e cada uma carrega ±0,1 °C. No pior caso os dois erros têm sinais opostos e se somam: a incerteza da diferença chega a ±0,2 °C, ou **~67%** de 0,3 °C. Somando em quadratura (erros independentes), ±0,14 °C, ou **~47%**. O valor de ~33% é a contribuição de **uma** leitura, não o erro relativo do resultado — e a palavra "até" o apresenta justamente como cota superior, que é o que ele não é.

O achado importa mais aqui do que importaria em outra aula: esta é a aula que ensina propagação de erro, e o exemplo subestima em 2× a propagação que ele existe para demonstrar. O argumento qualitativo (o problema está mal condicionado) permanece válido — e fica mais forte com o número certo.

**Correção proposta:** "o erro de cada leitura (±0,1 °C) já é 1/3 do numerador (0,3 °C); como o numerador é uma diferença de duas leituras, a incerteza propagada chega a ±0,2 °C no pior caso (±0,14 °C somando em quadratura) — um erro relativo de até ~67% no gradiente, antes de considerar qualquer outra fonte de incerteza."
**Fonte:** propagação de incerteza em soma/diferença — Chapra & Canale, *Numerical Methods for Engineers*, 7ª ed., cap. sobre propagação de erro; Burden & Faires, *Numerical Analysis*, 9ª ed. · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** o mesmo raciocínio de gradiente reaparece na aula 04 ("Diferenças finitas"), mas ali de forma qualitativa, sem número — não precisa de correção.

---

### 🟠 3. A comparação final entre bisseção e Newton-Raphson inverte quem chegou mais perto

**claim_id:** `NUM-M30A03-BISNEWTON-003`
**Tipo:** impreciso (com inconsistência interna)
**Onde:** `30-metodos-numericos-geociencias-aula-03-zeros-de-funcoes.md` · Exemplo trabalhado, "Comparação com Newton-Raphson"
**Está escrito:** "Já nesse primeiro passo, Newton-Raphson chegou mais perto da raiz (~2,0946) do que a bisseção depois de três repetições"

**Problema:** não é o que os números da própria aula mostram. Raiz verdadeira: 2,0945515.

| | estimativa | erro |
|---|---|---|
| Newton-Raphson, 1 passo | 2,1 | 5,4 × 10⁻³ |
| Bisseção, 3 repetições (ponto médio de [2,0625; 2,125]) | 2,09375 | **8,0 × 10⁻⁴** |

A bisseção está cerca de **7× mais perto**, não mais longe. E a aula já tinha dito isso: o Passo 4 conclui "já convergindo para próximo de **y ≈ 2,09**" — que é 2,09375, a estimativa melhor. A frase final contradiz o passo anterior.

O que é verdade, e sustenta a lição pretendida sem inverter os fatos: (a) o erro de Newton após 1 passo (5,4 × 10⁻³) já é menor que a **garantia** da bisseção após 3 repetições (±3,1 × 10⁻², a semilargura do intervalo) — a bisseção acertou por sorte do ponto médio, não por garantia; e (b) no **segundo** passo Newton chega a 2,0945681 (erro 1,7 × 10⁻⁵), precisão que a bisseção só garante por volta da 11ª repetição. A convergência quadrática aparece aí, não no primeiro passo.

**Correção proposta:** "Depois de dois passos, Newton-Raphson chega a 2,0945681 — erro da ordem de 10⁻⁵, precisão que a bisseção só garantiria por volta da décima primeira repetição. Já no primeiro passo, o erro de Newton (≈0,005) é menor que a **margem garantida** pela bisseção após três repetições (±0,031), embora o ponto médio do intervalo da bisseção, nesse caso particular, tenha calhado de cair ainda mais perto. É essa aceleração — e não o primeiro passo isolado — que a convergência quadrática descreve."
**Fonte:** ordem de convergência de bisseção (linear, erro ≤ (b−a)/2ⁿ⁺¹) e de Newton-Raphson (quadrática) — Chapra & Canale, *Numerical Methods for Engineers*, 7ª ed., caps. sobre métodos de intervalo e métodos abertos; Burden & Faires, *Numerical Analysis*, 9ª ed. · **Nível:** revisada por pares
**Verificação:** iterações recalculadas diretamente sobre f(y) = y³ − 2y − 5 (2026-08-29). Reprodutível.
**Confiança:** confirmado
**Também aparece em:** nenhum outro arquivo (módulo sem avaliação gerada).

---

### 🟠 4. Erro de arredondamento na avaliação de f(2,0625)

**claim_id:** `NUM-M30A03-FEVAL-004`
**Tipo:** impreciso (aritmética)
**Onde:** `30-metodos-numericos-geociencias-aula-03-zeros-de-funcoes.md` · Exemplo trabalhado, Passo 4
**Está escrito:** "f(2,0625) ≈ 8,78 − 4,125 − 5 = −0,34"

**Problema:** 2,0625³ = 8,77368, que arredonda para **8,77**, não 8,78; e f(2,0625) = −0,35132, que arredonda para **−0,35**, não −0,34. Dois dígitos errados na última casa. O sinal e a conclusão (a raiz passa a estar entre 2,0625 e 2,125) não mudam, então o impacto é pequeno — mas é um erro de arredondamento numa aula cujo assunto declarado é erro de arredondamento, e é o tipo de valor que um flashcard captura literalmente.

Os demais valores do exemplo foram conferidos e estão corretos: f(2) = −1; f(2,5) = 5,625; f(2,25) = 1,89062; f(2,125) = 0,34570.

**Correção proposta:** "f(2,0625) ≈ 8,774 − 4,125 − 5 = −0,351 (negativo)."
**Fonte:** cálculo direto, verificado em 2026-08-29 · **Nível:** aritmética verificável
**Confiança:** confirmado
**Também aparece em:** nenhum outro arquivo.

## Verificado e correto

As alegações abaixo foram checadas contra fonte (ou recalculadas) e passaram.

| claim_id | Aula | Alegação | Fonte | Confiança |
|---|---|---|---|---|
| `NUM-M30A01-PONTOFLUT-005` | 01 | Base binária torna 0,1 uma dízima; 0,1 + 0,2 ≠ 0,3 exatamente em ponto flutuante | Chapra & Canale, 7ª ed.; IEEE 754 | confirmado |
| `NUM-M30A01-TRUNCAMENTO-006` | 01 | Truncamento (parar processo infinito) é distinto de arredondamento (representação finita) | Burden & Faires, 9ª ed. | confirmado |
| `NUM-M30A01-CANCELAMENTO-007` | 01 | Subtração de números próximos amplia o erro relativo do resultado | Burden & Faires, 9ª ed. | confirmado |
| `NUM-M30A01-CONDICIONAMENTO-008` | 01 | Condicionamento é propriedade do problema, não do algoritmo | Burden & Faires, 9ª ed. | confirmado |
| `NUM-M30A01-EXEMPLO1-009` | 01 | 45,782 − 45,779 = 0,003, menor que a incerteza de ±0,01 de cada medida | recálculo | confirmado |
| `NUM-M30A01-GEOTERMA-010` | 01 | (42,6 − 42,3)/(810 − 800) = 0,03 °C/m = 30 °C/km | recálculo | confirmado |
| `NUM-M30A02-GAUSSDIRETO-011` | 02 | Escalonamento + substituição regressiva; pivotamento parcial reduz amplificação de erro sem mudar a solução | Chapra & Canale, 7ª ed. | confirmado |
| `NUM-M30A02-DOMINANCIA-012` | 02 | Dominância diagonal estrita é condição **suficiente e não necessária** para Gauss-Seidel | Burden & Faires, 9ª ed.; [ELA](https://emis.de/ft/34278) | confirmado |
| `NUM-M30A02-CUSTOCUBO-013` | 02 | Custo da eliminação de Gauss cresce com o cubo do número de incógnitas | Chapra & Canale, 7ª ed. | confirmado |
| `NUM-M30A02-EXEMPLOMISTURA-014` | 02 | a ≈ 0,333, b = 0,5, c ≈ 0,167 resolvem o sistema de três fontes; verificam nas três equações originais | recálculo | confirmado |
| `NUM-M30A03-TVI-015` | 03 | Teorema do Valor Intermediário sustenta a bisseção; convergência garantida, ordem linear | Chapra & Canale, 7ª ed. | confirmado |
| `NUM-M30A03-BISSECAO2N-016` | 03 | Reduzir o intervalo por fator de mil exige ~10 repetições (2¹⁰ ≈ 1.024); ~7 palpites para 100 números | recálculo | confirmado |
| `NUM-M30A03-DIVERGNEWTON-017` | 03 | Newton-Raphson pode divergir com palpite ruim, derivada próxima de zero ou raízes múltiplas próximas | Burden & Faires, 9ª ed. | confirmado |
| `NUM-M30A03-PHREEQC-018` | 03 | Códigos de especiação geoquímica (PHREEQC/USGS) resolvem equilíbrio não linear por métodos da família Newton-Raphson | documentação técnica PHREEQC (USGS) | provável |
| `NUM-M30A03-FLEXURA-019` | 03 | Isostasia flexural (placa elástica) não tem solução fechada simples e é resolvida numericamente | Turcotte & Schubert, *Geodynamics*, 3ª ed. | confirmado |
| `NUM-M30A04-RUNGE-020` | 04 | Fenômeno de Runge: polinômios de grau alto oscilam entre os pontos, sobretudo nas bordas | Chapra & Canale, 7ª ed. | confirmado |
| `NUM-M30A04-DIFCENTRAL-021` | 04 | Diferença central tem erro de truncamento menor que progressiva/regressiva para o mesmo espaçamento | Chapra & Canale, 7ª ed. | confirmado |
| `NUM-M30A04-INTERPOLACAO-022` | 04 | 120 + 0,4 × 25 = 130 m para o topo interpolado da camada | recálculo | confirmado |
| `NUM-M30A04-ISOCRONA-023` | 04 | Inclinação da isócrona (0,735 − 0,705)/(0,70 − 0,10) = 0,05; inclinação ↔ idade via λ, intercepto ↔ razão inicial | recálculo; Faure & Mensing, *Isotopes*, 3ª ed. | confirmado |
| `NUM-M30A05-ORDENS-024` | 05 | Trapézio composto O(h²), Simpson composto O(h⁴) com número par de intervalos, Euler O(h), RK4 O(h⁴) | Chapra & Canale, 7ª ed.; Burden & Faires, 9ª ed. | confirmado |
| `NUM-M30A05-EULEREXEMPLO-025` | 05 | Euler com h=1: N(1)=900, N(2)=810; exato 1.000·e^(−0,2) = 818,73; erro ≈ 8,7 átomos ≈ 1,1% | recálculo | confirmado |

## Consistência interna do módulo

- A cadeia conceitual "condicionamento" é usada de forma coerente nas cinco aulas: definida na 01, aplicada a sistemas quase redundantes na 02, a critério de parada na 03 e a diferenças finitas na 04.
- O exemplo do gradiente geotérmico aparece na aula 01 e é retomado na aula 04 sem divergência de valores.
- A referência cruzada ao Módulo 23 do curso avançado (EDPs de difusão de calor) é feita de forma consistente nas aulas 04 e 05.
- **Uma inconsistência encontrada**, registrada como achado 1: a aula 02 contradiz a si mesma entre a seção "Erros comuns" e o exemplo trabalhado.

## Observações não factuais (fora de escopo desta auditoria)

- Aula 04, Situação 2: os quatro pares fornecidos são **exatamente** colineares (inclinação 0,05 em todos os intervalos consecutivos), então o ajuste por mínimos quadrados devolve exatamente 0,05, não "muito próximo de 0,05". A ressalva do texto é desnecessária, não errada.
- Aula 02, Passo 1: o exemplo resolve o sistema por substituição, não por escalonamento matricial, embora a etapa esteja rotulada "escalonar". Os dois são equivalentes no resultado; a escolha é didática e cabe ao `revisor-didatico`, não a esta auditoria.

---

## Correções aplicadas

**Aplicadas em:** 2026-08-29 (modo `audit-and-fix`, autorizado pelo usuário após a entrega da Fase 1)

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `NUM-M30A02-GAUSSSEIDEL-002` | 🔴 | **Corrigido** | aula 02 |
| `NUM-M30A01-PROPGRAD-001` | 🟠 | **Corrigido** | aula 01 |
| `NUM-M30A03-BISNEWTON-003` | 🟠 | **Corrigido** | aula 03 |
| `NUM-M30A03-FEVAL-004` | 🟠 | **Corrigido** | aula 03 |

**O que mudou em cada aula:**

- **Aula 01, Situação 2, Passo 2** — a incerteza propagada passou a ser calculada sobre a *diferença* das duas leituras: ±0,2 °C no pior caso (±0,14 °C em quadratura), ou até ~67% de erro relativo, no lugar dos ~33% anteriores. O restante do exemplo e a conclusão sobre mau condicionamento não mudaram.
- **Aula 02, fecho do exemplo trabalhado** — o parágrafo foi convertido no contraexemplo que ele já era. Passou a mandar checar a dominância diagonal *antes*, a mostrar que a equação Y tem 0,10 contra 1,00, e a registrar que o método diverge (c > 67 na terceira repetição, > 6.500 na quinta). O ponto de que Gauss-Seidel é a ferramenta certa para sistemas grandes foi preservado, agora corretamente separado deste caso. A contradição com a seção "Erros comuns" desapareceu.
- **Aula 03, Passo 4** — `f(2,0625) ≈ 8,774 − 4,125 − 5 = −0,351`, no lugar de `8,78 − 4,125 − 5 = −0,34`.
- **Aula 03, comparação final** — a afirmação invertida foi substituída pela comparação correta: o erro de Newton no primeiro passo (≈0,005) contra a *margem garantida* da bisseção (±0,031), e o segundo passo de Newton (2,094568, erro ≈0,00002) contra as ~11 repetições que a bisseção precisaria. A convergência quadrática agora é ilustrada onde ela de fato aparece.

**Propagação:** nenhuma necessária. O módulo 30 não tem questionário nem flashcards gerados — foi justamente por isso que a auditoria rodou antes, e é o cenário em que o gate funciona como deveria: o erro foi pego antes de chegar ao material de revisão ativa.

**Pendências:** nenhuma. **Gate científico liberado:** 0 achados 🔴 ou 🟠 em aberto. O módulo está factualmente limpo para a geração do questionário e dos flashcards.
