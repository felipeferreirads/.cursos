# Aula 01: Erro numérico — ponto flutuante, arredondamento, truncamento, propagação e condicionamento

**ID:** geologia-m30-a01
**Módulo:** [[30-metodos-numericos-geociencias-modulo|Módulo 30 — Métodos numéricos para geociências]]
**Duração estimada:** ~30 min
**Nível:** ensino médio completo, sem geologia prévia (contrato `ensino-medio-sem-geologia-v1`)
**Objetivo:** identificar as fontes de erro numérico (arredondamento, truncamento, propagação) e avaliar o condicionamento de um cálculo geológico.

> [!info] Por que esta aula abre o módulo Todo o resto do módulo — resolver sistemas, achar raízes, interpolar, integrar — depende de saber, antes de mais nada, que **todo cálculo feito num computador carrega erro**, mesmo quando o método está certo e o computador não "errou conta". Esta aula ensina a nomear e a antecipar esse erro, para que as aulas seguintes possam ser lidas com a pergunta certa: não só "o método funciona?", mas "o resultado é confiável?"

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **Erro absoluto** | A diferença entre o valor calculado e o valor exato (ou de referência): erro = \|valor aproximado − valor exato\|. |
| **Erro relativo** | O erro absoluto dividido pelo valor exato — expressa o erro como fração ou porcentagem, e por isso compara melhor grandezas de tamanhos diferentes. |
| **Ponto flutuante** | O jeito como um computador guarda números decimais na memória, com uma quantidade **finita** de dígitos — a maioria dos números reais não cabe exatamente nesse formato. |
| **Erro de arredondamento** | O erro que nasce de representar um número com dígitos finitos, quando o valor exato precisaria de infinitos (ou de mais dígitos do que o formato guarda). |
| **Erro de truncamento** | O erro que nasce de substituir um processo exato (muitas vezes infinito, ou contínuo) por uma aproximação finita — por exemplo, parar uma soma infinita depois de poucos termos, ou usar poucos passos onde caberiam infinitos. |
| **Propagação de erro** | O modo como um pequeno erro num valor de entrada se espalha e cresce (ou encolhe) ao longo de operações aritméticas, até aparecer no resultado final. |
| **Condicionamento** | O quanto um problema, por sua própria natureza matemática, amplifica um pequeno erro na entrada em um erro grande na saída — uma propriedade do **problema**, não do método usado para resolvê-lo. |

## Antes de começar, você precisa saber

- **Desvio-padrão** e a ideia de que uma medida vem com incerteza — [[28-matematica-geociencias-aula-04-estatistica-descritiva|Módulo 28, aula 04]] (recomendado).
- Notação científica e potências de dez — [[00-partida-do-zero-aula-03-ordens-de-grandeza|Módulo 00, aula 03]] (recomendado).

## Ao final você vai conseguir

- [geologia-m30-oa01] Identificar as fontes de erro numérico (arredondamento, truncamento, propagação) e avaliar o condicionamento de um cálculo geológico.

## Conteúdo

### Por que o computador "erra conta" mesmo fazendo tudo certo

A fração 1/3 não tem representação decimal finita (vira 0,333...); 1/10 (0,1), por sua vez, parece finito em base decimal — mas um computador guarda números em **base binária**, e nessa base, 0,1 vira uma dízima infinita, exatamente como 1/3 vira 0,333... em base decimal. Como a memória do computador é finita, o valor guardado é sempre um **corte** dessa dízima — próximo de 0,1, mas não exatamente 0,1. É por isso que, em praticamente qualquer linguagem de programação ou planilha, a conta 0,1 + 0,2 não devolve exatamente 0,3, mas algo como 0,30000000000000004: cada um dos três números já chegou arredondado, e a soma herda essa pequena diferença. Esse não é um defeito de um programa mal escrito — é uma consequência inevitável de representar números reais (que são infinitos) com uma quantidade finita de dígitos, chamada de **ponto flutuante**. Todo cálculo geológico feito em computador, planilha ou calculadora científica carrega esse tipo de erro de fundo, normalmente pequeno demais para importar — até que uma conta específica o amplifique (ver adiante).

### Arredondamento e truncamento: duas fontes de erro diferentes

O **erro de arredondamento** vem da representação: cortar um número com infinitos dígitos (ou mais dígitos do que cabem) em um número finito. O **erro de truncamento** é outra coisa — vem de substituir um processo matemático exato por uma versão finita e mais simples de calcular. Um exemplo puro de truncamento, sem nenhum arredondamento envolvido: a função seno pode ser escrita como uma soma infinita de termos (a série de Taylor); um programa que calcula sen(x) usando só os três primeiros termos dessa soma, em vez dos infinitos, comete erro de truncamento — mesmo que cada termo individual fosse guardado com precisão perfeita. As aulas seguintes deste módulo mostram truncamentos concretos: parar uma iteração de Gauss-Seidel antes da convergência total (aula 02), usar um número finito de intervalos numa integral pelo trapézio (aula 05) — em ambos os casos, o erro não vem de representar mal um número, vem de parar um processo que, em teoria, continuaria indefinidamente.

### Propagação de erro: como um erro pequeno vira um erro grande

Cada operação aritmética pode **ampliar** ou **atenuar** um erro que já existia na entrada. A forma mais traiçoeira disso é o **cancelamento catastrófico**: subtrair dois números muito próximos entre si. Considere calcular a idade de uma amostra a partir da razão entre um isótopo radiogênico acumulado e um isótopo original, quando as duas quantidades medidas são muito parecidas em magnitude — a subtração entre elas preserva pouquíssimos dígitos significativos do resultado, mesmo que cada medida individual tivesse sido feita com ótima precisão. Em termos simples: se dois números de seis dígitos significativos, ambos com pequeno erro na sexta casa, forem subtraídos e o resultado for pequeno, esse resultado pequeno pode ter apenas uma ou duas casas confiáveis — o erro relativo do resultado dispara, mesmo que o erro absoluto de cada entrada fosse minúsculo.

> [!tip] Uma analogia Imagine pesar duas pessoas de 80,3 kg e 80,1 kg numa balança que arredonda para o décimo de quilo mais próximo, e querer usar a diferença (0,2 kg) para estimar quanto uma comeu a mais que a outra num único dia. Um erro de meio grama na balança é irrelevante para os pesos de 80 kg — mas é enorme, em termos relativos, quando comparado à diferença de 200 gramas entre eles. Subtrair dois números parecidos não elimina o erro de cada um; ele apenas fica concentrado num resultado bem menor, tornando o erro relativo — não o absoluto — muito maior.

### Condicionamento: quando o próprio problema é traiçoeiro

**Condicionamento** é uma propriedade do **problema**, independente de qual método é usado para resolvê-lo: um problema **bem condicionado** faz pequenas mudanças na entrada gerarem pequenas mudanças na saída; um problema **mal condicionado** faz pequenas mudanças na entrada — do tamanho de um erro de medição comum — gerarem mudanças grandes e desproporcionais na saída. Um exemplo geológico direto: calcular o gradiente geotérmico (variação de temperatura por metro de profundidade) a partir de duas medidas de temperatura tomadas em profundidades muito **próximas** uma da outra. O gradiente é a diferença de temperatura dividida pela diferença de profundidade; quando as duas profundidades são quase iguais, o denominador fica pequeno, e qualquer erro de leitura do termômetro (que seria irrelevante se as profundidades fossem bem espaçadas) se transforma numa incerteza enorme no gradiente calculado. O problema — estimar um gradiente a partir de dois pontos próximos — está mal condicionado, e nenhum cuidado no cálculo aritmético (nenhuma casa decimal extra) resolve isso: a solução é medir em pontos mais espaçados, ou usar mais pontos (ver diferenças finitas, [[30-metodos-numericos-geociencias-aula-04-interpolacao-e-ajuste|aula 04]]). A aula 02 deste módulo retoma condicionamento a propósito de sistemas lineares quase singulares.

## Exemplo trabalhado

**Situação 1 — cancelamento catastrófico numa média de análises químicas.** Duas análises independentes do teor de um óxido numa rocha retornam 45,782% e 45,779%, cada uma com incerteza de laboratório de ±0,01 pontos percentuais. Um geoquímico quer saber a diferença entre as duas análises, para avaliar se há desacordo real entre elas.

**Passo 1.** Diferença bruta: 45,782 − 45,779 = 0,003 (pontos percentuais).

**Passo 2.** Comparar essa diferença com a incerteza de cada medida: ±0,01. O resultado (0,003) é **menor** que a incerteza declarada de uma única medida (0,01).

**Passo 3 — interpretação.** A diferença calculada não pode ser distinguida de zero: está dentro da faixa de incerteza de medição. Concluir "a segunda análise deu um valor menor" seria superinterpretar um número cujo erro relativo, herdado das duas medidas de entrada, é maior que o próprio valor. A lição não é que a subtração "deu errado" — é que, quando se subtraem dois números próximos, o resultado precisa sempre ser lido ao lado da incerteza de cada entrada, nunca isolado.

**Situação 2 — condicionamento do gradiente geotérmico.** Duas leituras de temperatura em um poço: 42,3 °C a 800 m e 42,6 °C a 810 m (separação de apenas 10 m), cada leitura com incerteza de ±0,1 °C.

**Passo 1.** Gradiente aparente: (42,6 − 42,3) / (810 − 800) = 0,3 / 10 = 0,03 °C/m = 30 °C/km.

**Passo 2.** Propagar a incerteza: o erro de cada leitura (±0,1 °C) já é 1/3 do próprio numerador (0,3 °C). E como o numerador é uma **diferença de duas leituras**, as duas incertezas se somam no pior caso — em que uma temperatura foi lida para cima e a outra para baixo —, chegando a ±0,2 °C (ou ±0,14 °C, somando em quadratura, se os erros forem independentes). Ou seja: um erro relativo de até ~67% no gradiente, antes mesmo de considerar outras fontes de incerteza.

**Passo 3 — comparação.** Se as mesmas duas temperaturas tivessem sido medidas a 800 m e 1.300 m (separação de 500 m), o mesmo erro de ±0,1 °C por leitura representaria uma fração muito menor do denominador, e o gradiente calculado seria muito mais confiável. O problema (calcular um gradiente) ficou mal condicionado só por causa do espaçamento pequeno entre os pontos — nada no cálculo em si mudou.

## Erros comuns

- **Achar que mais casas decimais na calculadora eliminam o erro numérico.** Mais casas reduzem o arredondamento, mas não resolvem cancelamento catastrófico nem mau condicionamento — esses vêm da estrutura do cálculo, não da quantidade de dígitos guardados.
- **Confundir erro de truncamento com erro de arredondamento.** Um é sobre parar um processo antes da hora (truncamento); o outro é sobre representar um número com dígitos finitos (arredondamento) — são independentes e se somam.
- **Tratar erro absoluto e erro relativo como a mesma coisa.** Um erro absoluto de 0,1 °C é irrelevante para uma temperatura de 1.000 °C e enorme para uma diferença de 0,3 °C — sempre perguntar "relativo a quê?".
- **Confiar num resultado só porque "o computador calculou".** O computador executa a aritmética corretamente dentro do que a representação em ponto flutuante permite; ele não avisa quando o problema em si é mal condicionado.

## O que não concluir

- **Que este módulo vai ensinar o padrão IEEE 754 (a especificação binária exata de como o ponto flutuante é guardado).** Essa aula fica no nível conceitual — "por que 0,1 + 0,2 não dá exatamente 0,3" — sem entrar na representação em bits, que é assunto de ciência da computação.
- **Que dobrar a precisão (usar mais dígitos) resolve qualquer problema mal condicionado.** Reduz o erro de arredondamento, mas um problema mal condicionado (como o gradiente de dois pontos próximos) continua amplificando a incerteza de entrada, não importa quantos dígitos o cálculo carregue.

## Recap relâmpago

- **Erro de arredondamento** vem de representar números com dígitos finitos (inclusive no ponto flutuante do computador); **erro de truncamento** vem de parar um processo infinito ou contínuo numa aproximação finita.
- **Erro relativo** (erro dividido pelo valor exato) é geralmente mais informativo que erro absoluto, porque compara o erro ao tamanho da grandeza.
- **Cancelamento catastrófico**: subtrair dois números próximos preserva poucos dígitos confiáveis do resultado, mesmo que cada entrada fosse precisa.
- **Condicionamento** é uma propriedade do problema, não do método: um problema mal condicionado amplifica pequenos erros de entrada em erros grandes de saída, e nenhum cuidado aritmético consertará isso sozinho.
- Gradientes calculados a partir de pontos muito próximos (no espaço ou no tempo) são um exemplo geológico recorrente de cálculo mal condicionado.

## Próxima aula

[[30-metodos-numericos-geociencias-aula-02-sistemas-lineares|Aula 02 — Sistemas de equações lineares: eliminação de Gauss, Gauss-Seidel e matrizes mal condicionadas]], que retoma o condicionamento visto aqui aplicado a sistemas inteiros de equações.

## Anterior

Nenhuma — primeira aula do módulo.

## Fontes

- Erro de arredondamento, erro de truncamento e representação em ponto flutuante: Chapra, S. C. & Canale, R. P., *Numerical Methods for Engineers*, 7ª ed., McGraw-Hill, capítulo sobre erros de arredondamento e truncamento.
- Condicionamento e propagação de erro: Burden, R. L. & Faires, J. D., *Numerical Analysis*, 9ª ed., Cengage, capítulo introdutório sobre erro e estabilidade.
- Comparação de resultados analíticos com incerteza declarada em geoquímica isotópica: retomada de [[28-matematica-geociencias-aula-04-estatistica-descritiva|Módulo 28, aula 04]].

<!--
nivel: ensino-medio-sem-geologia-v1
palavras_corpo: 1570
bridge_lesson: true

mapa_objetivo_secao:
  geologia-m30-oa01: "Por que o computador \"erra conta\" mesmo fazendo tudo certo" + "Arredondamento e truncamento: duas fontes de erro diferentes" + "Propagação de erro: como um erro pequeno vira um erro grande" + "Condicionamento: quando o próprio problema é traiçoeiro" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEO-M30-A01-PONTO-FLUTUANTE-001
    claim: "Computadores representam números reais em ponto flutuante com uma quantidade finita de dígitos em base binária; números que têm representação decimal finita (como 0,1) podem ter representação binária infinita, causando erro de arredondamento (exemplo: 0,1 + 0,2 não resulta exatamente em 0,3 em aritmética de ponto flutuante padrão)."
    risk: fato
    source: "Chapra & Canale, Numerical Methods for Engineers, 7ª ed., cap. sobre erros de arredondamento; padrão IEEE 754 de aritmética de ponto flutuante"
  - claim_id: GEO-M30-A01-TRUNCAMENTO-002
    claim: "Erro de truncamento resulta de aproximar um processo matemático exato (frequentemente infinito ou contínuo) por uma versão finita, como usar poucos termos de uma série infinita ou poucas iterações de um processo iterativo; é conceitualmente distinto do erro de arredondamento."
    risk: fato
    source: "Chapra & Canale, Numerical Methods for Engineers, 7ª ed.; Burden & Faires, Numerical Analysis, 9ª ed., cap. introdutório"
  - claim_id: GEO-M30-A01-CANCELAMENTO-003
    claim: "A subtração de dois números de ponto flutuante muito próximos em valor ('cancelamento catastrófico') preserva poucos dígitos significativos confiáveis no resultado, mesmo quando cada operando individual é conhecido com boa precisão, porque o erro relativo do resultado é ampliado."
    risk: fato
    source: "Burden & Faires, Numerical Analysis, 9ª ed., cap. sobre erro e estabilidade; Chapra & Canale, Numerical Methods for Engineers, 7ª ed."
  - claim_id: GEO-M30-A01-CONDICIONAMENTO-004
    claim: "Condicionamento é uma propriedade inerente de um problema matemático (não do algoritmo usado para resolvê-lo), que descreve o quanto pequenas perturbações na entrada são amplificadas em mudanças na saída; um problema mal condicionado amplifica desproporcionalmente o erro de entrada."
    risk: fato
    source: "Burden & Faires, Numerical Analysis, 9ª ed.; Chapra & Canale, Numerical Methods for Engineers, 7ª ed."
  - claim_id: GEO-M30-A01-GRADIENTE-CONDICIONAMENTO-005
    claim: "Calcular um gradiente (razão entre diferenças) a partir de dois pontos de amostragem muito próximos entre si é um exemplo de problema mal condicionado: o mesmo erro absoluto de medição em cada ponto representa uma fração maior do denominador pequeno, ampliando o erro relativo do gradiente calculado."
    risk: interpretacao
    source: "aplicação didática do conceito de condicionamento (Burden & Faires; Chapra & Canale) a cálculo de gradiente geotérmico, prática comum em geofísica de poço"

nota_trilha_apoio: >-
  Aula 1 de 5 do módulo 30 (trilha de apoio, opcional, não bloqueante), criada em
  2026-08-29 na fase de build aprovada. Corresponde à MAP0125 (Cálculo Numérico
  para Geociências), primeira lacuna fechada contra a grade obrigatória do
  IGc-USP identificada em 2026-08-28. Abre o módulo estabelecendo erro e
  condicionamento como vocabulário comum para as quatro aulas seguintes.
-->
