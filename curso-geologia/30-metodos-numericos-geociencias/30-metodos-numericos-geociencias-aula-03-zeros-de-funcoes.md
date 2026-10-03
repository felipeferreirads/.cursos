# Aula 03: Zeros de funções — localização de raízes, bisseção, Newton-Raphson e critérios de parada

**ID:** geologia-m30-a03
**Módulo:** [[30-metodos-numericos-geociencias-modulo|Módulo 30 — Métodos numéricos para geociências]]
**Duração estimada:** ~30 min
**Nível:** ensino médio completo, sem geologia prévia (contrato `ensino-medio-sem-geologia-v1`)
**Objetivo:** localizar e calcular zeros de funções por bisseção e por Newton-Raphson, com precisão pré-fixada.

> [!info] Esta aula resolve o que a álgebra simples não resolve As duas aulas anteriores trataram de sistemas **lineares** — onde cada incógnita entra multiplicada por um número. Muitos problemas geológicos reais não são lineares: envolvem potências, raízes, razões complicadas de várias grandezas ao mesmo tempo, sem fórmula fechada para isolar a incógnita. Esta aula ensina a encontrar essa incógnita mesmo assim — por aproximação sucessiva, em vez de álgebra direta.

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **Raiz (ou zero) de uma função** | Um valor de x para o qual f(x) = 0 — onde o gráfico da função cruza o eixo horizontal. |
| **Equação transcendental** | Uma equação que mistura a incógnita de formas que impedem isolá-la por álgebra direta (por exemplo, a incógnita aparece elevada a um expoente não inteiro, ou dentro de uma razão com outras potências dela mesma). |
| **Bisseção** | Método que localiza uma raiz dividindo ao meio, repetidamente, um intervalo onde se sabe que a função muda de sinal. |
| **Mudança de sinal** | Se f(a) e f(b) têm sinais opostos, e f é contínua entre a e b, existe pelo menos uma raiz entre a e b (Teorema do Valor Intermediário). |
| **Newton-Raphson** | Método que usa a reta tangente à função num ponto de partida para "saltar" até uma estimativa melhor da raiz, repetindo o processo até convergir. |
| **Derivada** | A inclinação (taxa de variação) da função num ponto — o ingrediente que Newton-Raphson usa para calcular a reta tangente. |
| **Critério de parada (tolerância)** | A regra que diz quando encerrar as repetições: por exemplo, quando a diferença entre duas estimativas sucessivas for menor que um valor pré-fixado, ou quando um número máximo de repetições for atingido. |

## Antes de começar, você precisa saber

- **Erro, tolerância e critério de parada** — [[30-metodos-numericos-geociencias-aula-01-erro-numerico|Módulo 30, aula 01]] (recomendado).
- Ler o gráfico de uma função (onde ela cruza o eixo horizontal) é suficiente; esta aula não exige cálculo diferencial prévio para a bisseção, e explica o mínimo de derivada necessário para Newton-Raphson.

## Ao final você vai conseguir

- [geologia-m30-oa03] Localizar e calcular zeros de funções por bisseção e por Newton-Raphson com precisão pré-fixada.

## Conteúdo

### Quando a álgebra simples não isola a incógnita

Boa parte da matemática de ensino médio resolve equações isolando a incógnita: em 2x + 3 = 7, basta rearranjar. Muitas equações geológicas reais não permitem esse rearranjo. Um exemplo em geoquímica: calcular a concentração de íon hidrogênio (e portanto o pH) de uma solução em que vários equilíbrios ocorrem ao mesmo tempo — num sistema com carbonato dissolvido há várias reações de dissociação simultâneas — leva a uma equação de balanço de carga que mistura a incógnita elevada a potências diferentes, um **polinômio de grau alto** sem fórmula fechada simples (ao contrário da equação do segundo grau, que tem fórmula pronta). Softwares de especiação geoquímica como o PHREEQC resolvem esse tipo de sistema rotineiramente por métodos numéricos, entre eles variantes de Newton-Raphson. Outro exemplo, em geofísica: modelos de **isostasia flexural** — como uma placa litosférica elástica se flexiona sob carga, em vez de afundar em bloco como no modelo de Airy — também caem em equações sem solução fechada simples, exigindo localizar a raiz numericamente.

### Bisseção: o método que nunca falha, mas é devagar

O ponto de partida da bisseção é o **Teorema do Valor Intermediário**: se uma função contínua f tem sinais opostos em dois pontos, a e b (um positivo, outro negativo), então ela necessariamente cruza zero em algum lugar **entre** eles. A bisseção usa esse fato de forma simples: calcula o valor da função no ponto médio do intervalo; esse ponto médio substitui a extremidade que tem o **mesmo sinal** que ele (porque a raiz não pode estar desse lado); o intervalo, agora com metade do tamanho, ainda contém a raiz, com sinais opostos garantidos nas suas novas extremidades; repete-se o processo até o intervalo ficar menor que a tolerância desejada.

> [!tip] Uma analogia É o jogo de adivinhar um número entre 1 e 100 respondendo só "maior" ou "menor": perguntando sempre pelo meio do intervalo restante, o número de tentativas necessárias cresce muito devagar (uns 7 palpites bastam para 100 números) — cada palpite elimina exatamente metade das possibilidades, nunca falha, mas também nunca "acerta de primeira" mesmo estando perto.

A bisseção tem uma virtude rara entre métodos numéricos: **sempre converge**, desde que o intervalo inicial de fato contenha uma mudança de sinal — não existe risco de divergência. O preço é a velocidade: cada repetição corta o erro pela metade, então reduzir o intervalo por um fator de mil exige por volta de dez repetições (2¹⁰ ≈ 1.024) — seguro, mas mais lento que a alternativa a seguir.

### Newton-Raphson: mais rápido, mas exige cuidado

O **Newton-Raphson** troca segurança por velocidade: em vez de cortar o intervalo ao meio, calcula a reta **tangente** à função no ponto atual (usando a derivada, que mede a inclinação da função ali) e usa o ponto onde essa tangente cruza o eixo horizontal como a próxima estimativa da raiz. Quando o palpite inicial está razoavelmente perto da raiz e a função se comporta bem, esse "salto guiado pela inclinação" converge muito mais rápido que a bisseção — dobrando, a cada repetição, o número de dígitos corretos (convergência dita **quadrática**), contra o ganho fixo por repetição da bisseção (convergência **linear**).

O preço da velocidade é a robustez: Newton-Raphson pode **divergir** (afastar-se da raiz) se o palpite inicial estiver longe demais, se a derivada da função for próxima de zero no ponto atual (a tangente fica quase horizontal e o salto seguinte cai muito longe), ou se a função tiver comportamento irregular (múltiplas raízes próximas, pontos de inflexão) perto do ponto de partida. Diferente da bisseção, que **exige** apenas saber que existe mudança de sinal num intervalo, Newton-Raphson exige calcular a derivada da função a cada passo — um custo adicional, mas normalmente compensado pela velocidade de convergência.

### Critério de parada: quando declarar "raiz encontrada"

Nenhum dos dois métodos entrega a raiz exata — ambos entregam uma **aproximação**, e é preciso decidir quando parar de repetir. As regras mais comuns: parar quando a diferença entre duas estimativas sucessivas cair abaixo de uma tolerância pré-fixada (por exemplo, 0,0001), ou quando o próprio valor da função no ponto estimado ficar suficientemente perto de zero, ou — como salvaguarda contra um método que não converge — impor um número máximo de repetições, encerrando com um aviso de que a tolerância não foi atingida se esse limite for alcançado antes da convergência. A escolha da tolerância é uma decisão de quem resolve o problema, não uma constante universal: exigir seis casas decimais de precisão numa profundidade estimada em quilômetros é, na prática, precisão descartável (a incerteza real dos dados de entrada é muito maior) — outro eco do condicionamento visto na aula 01: refinar a precisão do método além da precisão dos dados de entrada não melhora a qualidade real da resposta.

## Exemplo trabalhado

**Situação — bisseção aplicada a uma equação de vazão em canal.** A vazão Q de um canal, pela equação de Manning, relaciona-se com a profundidade de escoamento y de forma não linear (a área e o perímetro molhado do canal dependem de y de formas diferentes). Suponha que, para um canal e uma vazão fixados, a equação de Manning reduzida a uma única incógnita produza a função f(y) = y³ − 2y − 5 (em unidades convenientes), cuja raiz positiva é a profundidade de escoamento procurada.

**Passo 1 — localizar o intervalo.** f(2) = 8 − 4 − 5 = −1 (negativo). f(2,5) = 15,625 − 5 − 5 = 5,625 (positivo). Como os sinais são opostos, existe uma raiz entre 2 e 2,5.

**Passo 2 — primeira bisseção.** Ponto médio: 2,25. f(2,25) = 11,39 − 4,5 − 5 = 1,89 (positivo). Como f(2) é negativo e f(2,25) é positivo, a raiz está entre 2 e 2,25 — a nova extremidade positiva (2,5) é descartada.

**Passo 3 — segunda bisseção.** Ponto médio: 2,125. f(2,125) = 9,60 − 4,25 − 5 = 0,35 (positivo). Raiz agora entre 2 e 2,125.

**Passo 4 — terceira bisseção.** Ponto médio: 2,0625. f(2,0625) ≈ 8,774 − 4,125 − 5 = −0,351 (negativo). Raiz agora entre 2,0625 e 2,125 — um intervalo de largura 0,0625, já convergindo para próximo de **y ≈ 2,09**.

**Comparação com Newton-Raphson:** a derivada de f(y) = y³ − 2y − 5 é f'(y) = 3y² − 2. Partindo de y₀ = 2: f(2) = −1, f'(2) = 10, próxima estimativa y₁ = 2 − (−1)/10 = 2,1. A raiz verdadeira é ≈2,09455. Já nesse primeiro passo, o erro de Newton-Raphson (≈0,005) é menor que a **margem garantida** pela bisseção após três repetições (±0,031, a metade da largura do intervalo restante) — embora o ponto médio da bisseção, neste caso, tenha calhado de cair ainda mais perto. A diferença aparece de verdade no passo seguinte: y₂ = 2,094568, com erro da ordem de 0,00002 — uma precisão que a bisseção só garantiria por volta da décima primeira repetição. É essa aceleração, e não o primeiro passo isolado, que a convergência quadrática descreve — ao custo de precisar calcular a derivada.

## Erros comuns

- **Aplicar bisseção sem confirmar mudança de sinal no intervalo escolhido.** Se f(a) e f(b) tiverem o mesmo sinal, o método não garante encontrar raiz nenhuma ali, mesmo que exista uma raiz fora desse intervalo.
- **Usar Newton-Raphson com um palpite inicial arbitrário, sem verificar se está razoavelmente perto da raiz.** Um palpite ruim, ou um ponto onde a derivada é próxima de zero, pode fazer o método divergir em vez de convergir.
- **Confundir "a função ficou perto de zero" com "a raiz foi encontrada com a precisão desejada".** Os dois critérios (proximidade da função a zero e proximidade entre estimativas sucessivas) medem coisas ligeiramente diferentes e, em casos raros, podem discordar — funções muito "achatadas" perto da raiz podem ter f(x) próximo de zero num x ainda distante da raiz verdadeira.
- **Pedir mais precisão do que os dados de entrada sustentam.** Iterar até a sexta casa decimal quando a incerteza da medição original é de 5% é esforço computacional sem ganho real de confiabilidade.

## O que não concluir

- **Que esta aula ensina a resolver sistemas de várias equações não lineares simultâneas (como um software real de especiação geoquímica faz).** O caso tratado aqui é de **uma** função de **uma** incógnita; sistemas multivariados não lineares (como o balanço de carga completo de um sistema carbonático com vários equilíbrios) exigem generalizações (Newton-Raphson multivariado) fora do escopo desta aula introdutória.
- **Que Newton-Raphson é sempre a escolha certa por ser mais rápido.** Quando a robustez importa mais que a velocidade — por exemplo, sem garantia de um bom palpite inicial — a bisseção (ou uma combinação das duas, usando bisseção para "chegar perto" e Newton-Raphson para refinar) é a escolha mais segura.

## Recap relâmpago

- Uma **raiz** de f(x) é um valor onde f(x) = 0; muitas equações geológicas não lineares não têm fórmula fechada para isolar a incógnita e exigem localizar a raiz numericamente.
- **Bisseção** divide ao meio, repetidamente, um intervalo com mudança de sinal confirmada — sempre converge, mas devagar (convergência linear).
- **Newton-Raphson** usa a reta tangente (via derivada) para saltar até uma estimativa melhor — converge muito mais rápido (quadrática), mas pode divergir com palpite ruim ou derivada próxima de zero.
- **Critério de parada** define quando encerrar: diferença entre estimativas sucessivas, valor da função perto de zero, ou um limite máximo de repetições como salvaguarda.
- Exigir mais precisão do método do que a incerteza dos dados de entrada sustenta é esforço sem ganho real — eco direto do condicionamento visto na aula 01.

## Próxima aula

[[30-metodos-numericos-geociencias-aula-04-interpolacao-e-ajuste|Aula 04 — Interpolação e ajuste: interpolação polinomial, diferenças finitas e mínimos quadrados]]

## Anterior

[[30-metodos-numericos-geociencias-aula-02-sistemas-lineares|Aula 02 — Sistemas de equações lineares]]

## Fontes

- Bisseção, Newton-Raphson, Teorema do Valor Intermediário e ordem de convergência: Chapra, S. C. & Canale, R. P., *Numerical Methods for Engineers*, 7ª ed., McGraw-Hill, capítulos sobre zeros de funções (roots of equations).
- Comparação de robustez e velocidade entre métodos de intervalo e métodos abertos: Burden, R. L. & Faires, J. D., *Numerical Analysis*, 9ª ed., Cengage.
- Uso de Newton-Raphson (e métodos correlatos) em softwares de especiação geoquímica para resolver sistemas de equilíbrio não lineares: descrição padrão do funcionamento de códigos de especiação como o PHREEQC (USGS), usada aqui apenas como motivação conceitual, não como cálculo reproduzido nesta aula.
- Isostasia flexural como exemplo de equação sem solução fechada simples: Turcotte, D. L. & Schubert, G., *Geodynamics*, 3ª ed., Cambridge University Press, capítulo sobre flexura da litosfera.

<!--
nivel: ensino-medio-sem-geologia-v1
palavras_corpo: 1599
bridge_lesson: true

mapa_objetivo_secao:
  geologia-m30-oa03: "Quando a álgebra simples não isola a incógnita" + "Bisseção: o método que nunca falha, mas é devagar" + "Newton-Raphson: mais rápido, mas exige cuidado" + "Critério de parada: quando declarar \"raiz encontrada\"" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEO-M30-A03-TVI-BISSECAO-001
    claim: "Pelo Teorema do Valor Intermediário, se uma função contínua f tem sinais opostos em dois pontos a e b, existe pelo menos uma raiz de f no intervalo (a,b); o método da bisseção usa esse fato para localizar a raiz dividindo repetidamente o intervalo ao meio, com convergência garantida e de ordem linear."
    risk: fato
    source: "Chapra & Canale, Numerical Methods for Engineers, 7ª ed., cap. sobre métodos de intervalo (bracketing methods)"
  - claim_id: GEO-M30-A03-NEWTON-RAPHSON-002
    claim: "O método de Newton-Raphson estima a próxima aproximação de uma raiz usando a interseção da reta tangente à função no ponto atual (calculada com a derivada) com o eixo horizontal, e apresenta convergência quadrática (aproximadamente dobrando o número de dígitos corretos a cada iteração) quando o palpite inicial está suficientemente próximo da raiz e a derivada não é próxima de zero."
    risk: fato
    source: "Chapra & Canale, Numerical Methods for Engineers, 7ª ed., cap. sobre métodos abertos (open methods); Burden & Faires, Numerical Analysis, 9ª ed."
  - claim_id: GEO-M30-A03-DIVERGENCIA-NEWTON-003
    claim: "O método de Newton-Raphson pode divergir ou convergir para uma raiz diferente da desejada quando o palpite inicial está distante da raiz, quando a derivada da função é próxima de zero no ponto atual, ou quando há múltiplas raízes próximas ou pontos de inflexão na vizinhança do palpite."
    risk: fato
    source: "Chapra & Canale, Numerical Methods for Engineers, 7ª ed.; Burden & Faires, Numerical Analysis, 9ª ed., cap. sobre métodos abertos"
  - claim_id: GEO-M30-A03-ESPECIACAO-GEOQUIMICA-004
    claim: "Softwares de especiação geoquímica em uso corrente, como o PHREEQC (desenvolvido pelo USGS), resolvem sistemas de equações de equilíbrio químico não lineares (balanço de massa e balanço de carga com múltiplos equilíbrios simultâneos) numericamente, empregando métodos iterativos da família Newton-Raphson."
    risk: fato
    source: "documentação técnica do PHREEQC (USGS) sobre o algoritmo de resolução numérica de equilíbrio químico"
  - claim_id: GEO-M30-A03-ISOSTASIA-FLEXURAL-005
    claim: "Modelos de isostasia flexural, que tratam a litosfera como uma placa elástica que se flexiona sob carga (em contraste com o modelo de Airy, de compensação em bloco), resultam em equações diferenciais cuja solução para a deflexão ou profundidade de compensação, em geral, não tem forma fechada simples e é obtida numericamente."
    risk: fato
    source: "Turcotte, D. L. & Schubert, G., Geodynamics, 3ª ed., Cambridge University Press, cap. sobre flexura da litosfera"

nota_trilha_apoio: >-
  Aula 3 de 5 do módulo 30 (trilha de apoio, opcional, não bloqueante), criada em
  2026-08-29. A equação usada no exemplo trabalhado (y³ − 2y − 5 = 0) é uma
  simplificação didática representativa da forma de uma equação de Manning
  reduzida, escolhida por ter raiz não trivial e permitir comparação direta
  entre bisseção e Newton-Raphson; os valores numéricos da equação de Manning
  em si não foram derivados de um canal real.
-->
