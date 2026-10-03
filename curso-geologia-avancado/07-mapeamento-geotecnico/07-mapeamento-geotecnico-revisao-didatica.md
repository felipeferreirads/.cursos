# Revisão didática — Módulo 07: Metodologia de mapeamento geotécnico

**Módulo:** [[07-mapeamento-geotecnico-modulo|Módulo 07 — Metodologia de mapeamento geotécnico]]
**Escopo:** 4 aulas (a01–a04). Pergunta orientadora: alguém aprende com este material, ou só está correto?
**Data:** 2026-08-27

## Veredito geral: bem ensinado

O módulo tem a estrutura de um funil metodológico bem construído: a01 estabelece o que é uma carta geotécnica e, sobretudo, **o que a escala autoriza decidir** → a02 produz as camadas de entrada, um atributo por carta → a03 as combina em produtos interpretativos e introduz a distinção conceitual que organiza a área inteira (suscetibilidade, perigo, risco) → a04 opera essa combinação em ambiente computacional e fecha mostrando como o produto vira decisão e que consequências isso tem sobre pessoas. A progressão é do conceito ao dado, do dado à interpretação, e da interpretação à consequência — e cada etapa é usada pela seguinte.

O acerto pedagógico central é que o módulo **não trata cartografia como técnica de representação**. Ele a trata como um encadeamento de decisões (que escala, que atributos, que unidade, que método de agregação, que operador), cada uma com consequência rastreável sobre o que a carta pode e não pode sustentar. Isso é o que separa um profissional que produz cartas de um que apenas as desenha.

## Verificações por critério

### Salto de pré-requisito
Nenhum salto interno encontrado, e a articulação com o Módulo 06 é o ponto mais bem resolvido do módulo. A a01 declara explicitamente que os parâmetros do Módulo 06 são "os atributos que esta cartografia espacializa", enquadrando o módulo anterior de forma funcional em vez de protocolar. A a03 vai além e **usa** o Módulo 06 de fato: o modelo de talude infinito é apresentado com a observação de que "cada termo da fórmula é um parâmetro daquele módulo, espacializado", e o comentário do exemplo trabalhado retoma o alerta sobre c' como intercepto de extrapolação exatamente onde ele volta a morder (tensões baixas de um talude raso). Um aluno que fez o Módulo 06 reconhece o reaproveitamento; um que não fez percebe onde precisa voltar.

### Conceitos novos por aula
Dentro do limite nas quatro aulas, com a a03 e a a04 no teto. A a03 carrega a tríade conceitual (suscetibilidade/perigo/risco), a carta de aptidão, três famílias de método, o modelo de talude infinito com exemplo numérico, as camadas de exposição e vulnerabilidade e a validação — é muita coisa. Ela se sustenta porque a tríade funciona como espinha organizadora à qual todo o resto se prende (cada método produz um dos três produtos; a validação valida o primeiro; as camadas adicionais convertem o primeiro no terceiro), e não como lista. A a04 tem carga comparável, distribuída em blocos curtos e independentes, o que é apropriado para conteúdo de natureza mais instrumental. Nenhuma das quatro precisa ser quebrada em partes hoje; a a03 é a candidata natural caso o usuário relate peso.

### Objetivo declarado vs. seções que de fato ensinam
Conferido o `mapa_objetivo_secao` das quatro aulas. Todas as seções listadas desenvolvem o objetivo declarado. Registro de balanceamento: a a03 é a única aula que cobre dois objetivos (oa01 e oa03), e o faz com divisão limpa — as seções conceituais (cadeia suscetibilidade/perigo/risco, carta de aptidão, camadas de risco) atendem ao oa01, e as seções de método e validação atendem ao oa03, que é compartilhado com a a02. A distribuição de questões e flashcards levou isso em conta para que o oa01, concentrado numa única aula, não ficasse sub-representado.

### Exemplo trabalhado: suficiência e posicionamento
As quatro aulas têm exemplo trabalhado, todos após o desenvolvimento teórico, e — o ponto notável deste módulo — **os quatro são de naturezas diferentes**, cada um adequado ao tipo de competência que a aula desenvolve:
- A a01 tem um exemplo de **decisão de projeto de trabalho** (definir escala, atributos e unidades para duas demandas distintas), que é exatamente a competência de quem planeja uma campanha. Ele acerta ao mostrar que a resposta correta é *dois produtos*, não um — ensinando a reconhecer quando a pergunta está mal-posta.
- A a02 tem um exemplo de **crítica de dado**: dado um valor de declividade de 28% obtido de SRTM, avaliar o que se pode concluir. A escolha de 28% é deliberadamente próxima do limiar legal de 30%, o que torna a incerteza consequente em vez de acadêmica.
- A a03 tem o único exemplo **numérico** do módulo, e é o mais importante: mostra o mesmo talude passando de FS 1,58 a 0,94 apenas por saturação, o que quantifica o mecanismo qualitativo que o Módulo 06 havia ensinado. A interpretação em três leituras (é suscetibilidade, não é perigo, não é risco) transforma o cálculo num exercício da tríade conceitual da própria aula — o exemplo faz dois trabalhos ao mesmo tempo.
- A a04 tem um exemplo **aritmeticamente trivial e conceitualmente denso**: duas células com índices idênticos e situações opostas. A simplicidade do cálculo é uma virtude, porque desloca toda a atenção para o que está sendo ensinado (o caráter compensatório da agregação), sem competição de carga aritmética.

### Analogias e risco de modelo mental errado
O módulo mantém o padrão do curso de avisos nomeados em vez de analogias soltas, e os posiciona bem: "a carta geotécnica é interpretativa por construção" (a01), "o atributo mais escasso é a subsuperfície" (a01), "colúvio é a classe que mais frequentemente decide a carta" (a02), "a declividade calculada depende da resolução do MDE" (a02), "por que essa distinção não é preciosismo terminológico" (a03), "resolução da célula não é escala da carta" (a04), "reduzir risco tem quatro caminhos, e três não são obras" (a04), "o mapa produz consequência sobre pessoas" (a04).

Três merecem destaque por atacarem modelos mentais especificamente perigosos nesta área:
- O callout da a03 sobre a distinção suscetibilidade/risco **não se limita a definir** — explica os dois erros simétricos que a confusão produz (tratar suscetibilidade alta em área vazia como emergência; tratar suscetibilidade média em favela consolidada como situação tranquila). Nomear as duas falhas opostas é muito mais eficaz que enunciar a definição correta, porque o aluno reconhece o erro que estaria prestes a cometer.
- O callout da a04 sobre as quatro alavancas de redução de risco desfaz o viés profissional mais previsível do público deste curso — a tendência do olhar geotécnico a enxergar apenas obra —, e o faz derivando as alavancas da própria fórmula já ensinada, não por asserção externa.
- O callout final da a04 ("o mapa produz consequência sobre pessoas") é o único do módulo de natureza ética, e está corretamente posicionado: no fim, depois que o aluno já sabe quanta incerteza há na cadeia, de modo que o dever de declará-la aparece como consequência técnica e não como moralismo acrescentado.

Nenhuma analogia identificada carrega modelo mental que precise de correção não sinalizada pela própria aula.

### Redundância e sobrecarga cognitiva
O tema da **incompatibilidade entre aparência de precisão e acurácia real** reaparece quatro vezes: ampliar carta além da escala (a01), resolução do MDE subestimando declividade (a02), FS calculado sobre parâmetros incertos (a03) e reamostragem de raster mais precisão gráfica do SIG (a04). É a redundância mais extensa do módulo, e é justificada: cada aparição trata de um mecanismo diferente pelo qual o mesmo erro se instala, e as quatro juntas constroem um hábito de leitura crítica que nenhuma isolada construiria. O texto inclusive nomeia a conexão na a04 ("este é o mesmo erro da Aula 01 na sua versão digital"), o que impede que soe repetitivo.

Um ponto de atenção genuíno: a tríade suscetibilidade/perigo/risco é definida na a03 e retomada na a04 em dois lugares (as quatro alavancas e o exemplo). A retomada é breve e funcional, não redundante — mas é o conceito de cuja compreensão tudo depende, e é o item que a avaliação precisava cobrar mais de uma vez em formatos diferentes, o que foi feito.

### Recap que recapitula
Os recaps das quatro aulas cobrem os pontos efetivamente desenvolvidos, sem introduzir fato novo. São mais longos que a média do curso (seis a sete itens contra cinco), o que é proporcional à extensão das aulas e à natureza do conteúdo — este é um módulo com muitos critérios e limiares a reter, e não fórmulas centrais poucas e memoráveis como o Módulo 06. O recap da a03 acerta ao abrir exatamente pela cadeia conceitual, que é o item de maior valor de retenção.

### Dificuldade proporcional à posição no curso
O módulo é o sétimo do curso avançado e o terceiro da sub-área de geotecnia. A dificuldade não é computacional — só a a03 tem cálculo — e sim de **julgamento**: escolher escala, escolher atributo, escolher método de agregação, decidir o que a carta pode sustentar. Isso é apropriado para a posição, e representa uma mudança bem gerida em relação ao Módulo 06, que era intensivo em cálculo. A transição é explicitada logo na a01 (os parâmetros do módulo anterior são o que esta cartografia espacializa), de modo que o aluno entende que mudou o tipo de competência exigida, e não o assunto.

### Desalinhamento aula ↔ avaliação
Verificado contra o questionário e o baralho gerados (ver [[07-mapeamento-geotecnico-questionario|questionário]] e [[07-mapeamento-geotecnico-flashcards|flashcards]]): toda questão e todo flashcard remete a conceito efetivamente ensinado. Nenhuma questão exige operar software de SIG, traçar uma carta, ou memorizar números de artigos de lei — a avaliação cobra o **limiar** (30%, 45°) e o **efeito jurídico**, que é o que a aula ensina, e não a citação normativa, que a aula fornece como referência. Também não há questão que exija AHP na sua mecânica de matrizes, que a a03 apenas cita como recurso de estruturação de pesos sem desenvolver. Sem desalinhamento.

### Decisão sobre questionário único
O módulo tem 4 aulas, abaixo do limiar de parciais, e recebeu **um questionário cumulativo único**, em linha com os módulos 02, 03 e 04 do curso e com a regra do plugin. A decisão é reforçada por uma razão de conteúdo: as quatro aulas formam uma cadeia de produção única (conceito → cartas básicas → cartas derivadas → operação e decisão), sem corte conceitual natural que justificasse partir a avaliação — diferentemente do Módulo 06, onde o corte entre caracterização e comportamento hidromecânico era nítido. Um questionário integrado é, aqui, também o formato que melhor avalia o que o módulo ensina, já que a competência central é encadear as etapas.

## Pontos fortes a preservar
- A **tríade suscetibilidade/perigo/risco** ensinada não como definições mas como **cadeia de decisões com consequências práticas nomeadas**, incluindo os dois erros simétricos que sua confusão produz. É o núcleo do módulo e está muito bem tratado.
- A **variedade deliberada dos exemplos trabalhados** (decisão de projeto, crítica de dado, cálculo, aritmética simples com conteúdo denso), cada um casado com o tipo de competência da sua aula, em vez do formato único de exercício numérico.
- O exemplo da a03, que **quantifica** com FS 1,58 → 0,94 o mecanismo que o Módulo 06 havia ensinado qualitativamente, e depois usa o próprio resultado para exercitar a tríade conceitual da aula.
- O fio da **precisão aparente versus acurácia real** atravessando as quatro aulas por mecanismos diferentes, com a conexão explicitada em vez de deixada implícita.
- O callout das **quatro alavancas de redução de risco**, que corrige o viés profissional mais previsível do público derivando a correção da fórmula já ensinada.
- O fechamento **ético e não moralista** da a04, posicionado depois da discussão de incerteza, de modo que os deveres profissionais apareçam como consequência técnica.

## Recomendação
Nenhuma correção didática necessária. Aprovar o módulo sem ressalvas de pedagogia. Ficam registrados, para monitoramento e não como defeitos atuais: a densidade da a03, candidata natural a quebra em partes caso o usuário relate peso; e a necessidade de revisitar periodicamente as referências legais das aulas 02 e 03, conforme apontado no achado 🟡 do [[07-mapeamento-geotecnico-auditoria|relatório de auditoria]] — conteúdo que envelhece sem sinalização é um risco didático, não apenas factual.
