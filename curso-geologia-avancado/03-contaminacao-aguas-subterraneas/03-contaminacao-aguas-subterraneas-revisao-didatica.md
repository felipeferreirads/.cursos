# Revisão didática — Módulo 03: Contaminação dos recursos hídricos subterrâneos

**Módulo:** [[03-contaminacao-aguas-subterraneas-modulo|Módulo 03 — Contaminação dos recursos hídricos subterrâneos]]
**Escopo:** 5 aulas (a01–a05). Pergunta orientadora: alguém aprende com este material, ou só está correto?
**Data:** 2026-08-26

## Veredito geral: bem ensinado

A progressão é estritamente monotônica e segue a lógica causal do próprio fenômeno: a01 define o que é contaminação e de onde ela vem (fonte e carga) → a02 explica como o soluto se move a partir da fonte (advecção e dispersão) → a03 explica o que retarda e reduz esse soluto ao longo do caminho (sorção, biodegradação, MNA) → a04 trata do caso especial em que o contaminante não é um soluto dissolvido, mas uma fase líquida separada (LNAPL/DNAPL), mais o caso irmão da cunha salina → a05 fecha integrando tudo em ferramentas de gestão preventiva e reativa (vulnerabilidade, perímetros de proteção, etapas de investigação). Nenhuma aula usa um conceito antes de defini-lo; em particular, a05 depende explicitamente de "carga contaminante" (a01), "velocidade linear média" (a02) e "atenuação" (a03), e os três usos são consistentes com as definições originais.

## Verificações por critério

### Salto de pré-requisito
Nenhum encontrado. As seções "Antes de começar, você precisa saber" listam corretamente apenas conceitos já cobertos nas aulas anteriores deste módulo ou nos Módulos 01 (fluxo, Darcy, poços, zona não saturada) e 02 (constituintes, balanço iônico). A aula 04 depende de "sorção" e "transporte de soluto" (a02–a03) apenas para contrastar — o texto é explícito que o NAPL em si segue leis diferentes, evitando que o aluno tente aplicar a equação de advecção-dispersão à fase livre por engano. A aula 05 depende de todo o módulo anterior, o que é apropriado ao seu papel de fechamento integrador.

### Conceitos novos por aula
Dentro do limite. Cada aula gira em torno de um objetivo central com 3–5 conceitos, adequado a ~30 min em nível avançado. A aula 04 é a mais densa (LNAPL, DNAPL, três zonas de contaminação por LNAPL, controle estrutural do DNAPL, Ghyben-Herzberg), mas os dois primeiros blocos (LNAPL, DNAPL) respondem à mesma pergunta organizadora ("o que acontece com um líquido imiscível conforme sua densidade") antes de a aula abrir um terceiro caso análogo (a cunha salina, também um contato entre fluidos de densidade diferente) — a progressão interna justifica agrupar os três na mesma aula em vez de fragmentar, e a aula permanece dentro do teto de ~30 min. Não recomendo split.

### Objetivo declarado vs. seções que de fato ensinam
Conferido o `mapa_objetivo_secao` de cada aula contra o conteúdo real das seções listadas — em todos os cinco casos as seções nomeadas desenvolvem efetivamente o objetivo declarado. Nenhuma seção órfã, nenhum objetivo fantasma.

### Exemplo trabalhado: suficiência e posicionamento
Todas as cinco aulas têm um exemplo trabalhado numérico, posicionado após o desenvolvimento teórico completo, e cada um retoma diretamente a fórmula central ensinada na aula (carga contaminante em a01; v_x e tempo de trânsito em a02; R e velocidade retardada em a03; Ghyben-Herzberg em a04; índice GOD comparativo em a05). O exemplo da a05, em particular, usa dois aquíferos hipotéticos lado a lado — recurso didático eficaz para mostrar o efeito multiplicativo do método (uma camada confinante dominando o resultado mesmo com litologia igualmente permeável), que seria menos evidente com um único caso isolado.

### Analogias e risco de modelo mental errado
A analogia central da a04 ("LNAPL flutua análogo a uma mancha de óleo sobre um lago") vem imediatamente qualificada ("com ressalvas importantes") e seguida da explicação técnica da franja capilar — evita que o aluno leve a analogia longe demais e imagine uma camada estritamente horizontal e uniforme. O contraste explícito "DNAPL contraria a intuição de que contaminante segue o fluxo da água" (callout de aviso) é, na verdade, uma correção deliberada de um modelo mental que o aluno traria das Aulas 02–03 (onde todo transporte é apresentado na direção do fluxo) — funciona bem porque nomeia o próprio erro esperado antes que ele se instale. Nenhuma analogia identificada carrega um modelo mental que precise ser desfeito sem que a própria aula já o sinalize.

### Redundância e sobrecarga cognitiva
"Atenuação" aparece em a01 (como o processo que reduz quanto da carga aplicada chega à zona saturada) e é desenvolvida em profundidade em a03 (mecanismos específicos) — a01 antecipa o termo sem defini-lo tecnicamente, o que é apropriado (a03 é quem detalha), mas vale registrar que a01 usa a palavra antes de sua definição formal completa; não chega a ser confuso porque o contexto de a01 já deixa claro que se trata de "retenção/degradação/volatilização", e a03 formaliza cada mecanismo individualmente. "Direção de fluxo" e "velocidade linear média" (a02) são retomados em a05 (perímetros assimétricos) sem repetição redundante — cada retomada aplica o conceito a um problema novo. Nenhuma sobrecarga identificada.

### Recap que recapitula
Os quatro a seis itens de "Recap relâmpago" de cada aula cobrem os pontos centrais efetivamente desenvolvidos no corpo, sem introduzir fato novo nem omitir conceito central.

### Dificuldade proporcional à posição no curso
O módulo é o terceiro do curso avançado, com os Módulos 01 e 02 como pré-requisitos explícitos e verificados. As cinco aulas somam ~26–29 min cada, com a mesma estrutura de consolidação dos módulos anteriores (erros comuns, o que não concluir, recap, fontes) — nível de exigência consistente. A a05, que integra os quatro objetivos anteriores em ferramentas de gestão, é apropriadamente a mais sintética/aplicada, condizente com seu papel de fechamento — mesma lógica já usada com sucesso na a05 do Módulo 02.

### Desalinhamento aula ↔ avaliação
Verificado contra o questionário cumulativo e o baralho de flashcards gerados para este módulo (ver [[03-contaminacao-aguas-subterraneas-questionario|questionário]] e [[03-contaminacao-aguas-subterraneas-flashcards|flashcards]]): toda questão e todo flashcard remetem a um conceito efetivamente ensinado em alguma das cinco aulas; nenhuma questão exige conhecimento não coberto pelo módulo (por exemplo, nenhuma questão cobra técnicas específicas de remediação ativa, explicitamente citadas na a05 como "fora do escopo desta aula introdutória"). Sem desalinhamento.

## Pontos fortes a preservar
- O uso de callouts de aviso para corrigir, de forma antecipada e nomeada, o erro conceitual mais provável de cada aula — "alto não é contaminado" (a01), "mais dispersão não é chegada mais rápida" (a02), "sorção não remove massa" (a03), "DNAPL contraria a intuição de seguir o fluxo" (a04), "vulnerabilidade não é risco" (a05) — mesmo padrão pedagógico consolidado nos Módulos 01 e 02, aplicado com a mesma disciplina e, neste módulo, especialmente bem calibrado porque cada aviso ataca diretamente uma confusão que o conteúdo anterior do próprio curso poderia induzir.
- O exemplo trabalhado encadeado entre a02, a03 e a04 (mesmo aquífero hipotético, retomando v_x = 0,128 m/dia da a02 no cálculo de retardação da a03) reforça a continuidade do módulo como um raciocínio único que se acumula, em vez de exemplos desconexos aula a aula.
- Conexões explícitas e corretas com o Módulo 01 (cunha salina, gestão quantitativa) e antecipação correta do Módulo 04 (dimensionamento de campos de poços, perímetros de proteção) — sem exigir conhecimento do módulo futuro.

## Recomendação
Nenhuma correção didática necessária. Aprovar o módulo sem ressalvas de pedagogia.
