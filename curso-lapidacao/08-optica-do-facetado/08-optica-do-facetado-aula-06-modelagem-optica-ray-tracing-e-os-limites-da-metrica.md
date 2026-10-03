# Aula 06: Modelagem óptica do talhe — ray tracing, métricas de brilho e os limites do que um número mede

**ID:** lapidacao-m08-a06
**Módulo:** [[08-optica-do-facetado-modulo|Módulo 08]] — Óptica do talhe facetado
**Duração estimada:** ~26 min
**Objetivo:** descrever o que a modelagem óptica por ray tracing mede, nomear as ferramentas correntes e delimitar o que suas métricas não capturam.
**Pré-requisito:** todas as aulas anteriores deste módulo (ângulo crítico, ângulos-alvo, brilho/dispersão/cintilação, rendimento e cor) — esta aula fecha o módulo reunindo o que cada uma tratou de forma isolada ou aproximada.

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **ray tracing** (traçado de raios) | técnica de simulação que calcula o trajeto de raios de luz individuais através de um modelo geométrico de um objeto, aplicando as leis de reflexão e refração a cada superfície que encontram. |
| **diagrama de lapidação** | a especificação de um talhe — o ângulo e a posição de índice de cada faceta — desenhada e organizada num arquivo ou numa folha, independente de qualquer software específico. |
| **métrica de brilho** | um número calculado por um software, destinado a resumir numericamente o desempenho óptico simulado de um desenho. |
| **modelo idealizado** | uma representação simplificada do material e da geometria usada por um software de simulação, que descarta deliberadamente detalhes considerados irrelevantes para o cálculo. |

## Antes de começar, você precisa saber

- Das aulas 01 a 05 deste módulo: ângulo crítico e reflexão interna total (aula 01), ângulos-alvo por índice (aula 02), brilho/dispersão/cintilação (aula 03), o compromisso com rendimento (aula 04) e com cor (aula 05) — cada um tratado de forma teórica, isolada e com valores de referência aproximados.
- Não é preciso saber como operar nenhum software específico — esta aula trata do que essas ferramentas existem para medir e do que elas não capturam, nunca de como usá-las na prática.

## Ao final você vai conseguir

- `lapidacao-m08-oa06` — Descrever o que a modelagem óptica por ray tracing mede, nomear as ferramentas correntes e delimitar o que suas métricas não capturam.

## Conteúdo

### Da tabela ao cálculo específico

As aulas 01 a 05 trabalharam com princípios e valores de referência: a tabela da aula 02 dá um ponto de partida, mas declarou seus limites — assume um desenho padrão e não resolve variações de contorno ou proporção. A pergunta que fecha o módulo é: como calcular o desempenho óptico de um desenho **específico**, com suas próprias variações? A resposta da literatura moderna é a modelagem por **ray tracing**.

### O que o ray tracing faz

O ray tracing simula o trajeto de um número grande de raios individuais entrando num modelo geométrico do talhe. Para cada raio, o software aplica as leis de reflexão e refração em cada superfície que ele encontra — os mesmos princípios das aulas 01 a 03, mas faceta por faceta, raio por raio, em vez de num cálculo único para a pedra inteira. Depois de rastrear milhares ou milhões deles, agrega o resultado em **métricas de brilho**: números que resumem quanto da luz que entra retorna ao observador, e em que direções.

O software mais citado para desenhar o diagrama de lapidação é o **GemCad**, que especifica cada faceta por **índice** — a posição no disco dentado da máquina, não o índice de refração —, ângulo e altura, e verifica o encontro de facetas — o meetpoint da aula 04 — antes de qualquer corte. O programa companheiro de traçado de raios, **do mesmo autor**, é o **GemRay**: programa autônomo, distribuído separadamente, que abre os arquivos do GemCad e simula o comportamento óptico da geometria. Os dois são de Robert W. Strickland, que se aposentou em 2023 e liberou ambos gratuitamente, o GemRay em código aberto. O GemCad trata da forma; o GemRay, da aparência.

### O que essas métricas medem, de fato

Uma métrica de brilho típica soma, para uma posição de fonte e observador (ou uma amostra de posições), a fração de luz simulada que retorna dentro de um dado ângulo de visão. O número compara dois desenhos de forma muito mais fina que a tabela da aula 02: testar, por exemplo, se aprofundar o pavilhão em meio grau melhora ou piora o retorno para um contorno específico.

### O que essas métricas não capturam

O ponto central desta aula — e o motivo de ela fechar o módulo, não abri-lo — é que um número de brilho simulado não é a mesma coisa que "a pedra vai ficar bonita". Antes delas, desfaça-se uma suposição comum: a de que essas ferramentas ignoram cor. O GemRay **não** ignora. Ele permite escolher a cor do material, traça os raios vermelho, verde e azul separadamente e os combina numa imagem colorida — modelando, portanto, dispersão —, e implementa o mecanismo de caminho óptico da aula 05: quanto mais longe um raio viaja no material, mais luz é absorvida. Gera até animações de basculamento. As lacunas reais são outras:

**Cor uniforme, não cor real.** O modelo usa **uma cor única atribuída pelo operador**. Ele calcula corretamente que um pavilhão mais fundo escurece a pedra — mas sobre um material que supõe homogêneo. Zonação, pleocroísmo e variação de saturação dentro da peça, que são o assunto do módulo 05 e a razão da ordem de decisão da aula 05, ficam de fora. Uma safira zonada é lida como safira de cor média uniforme: o escurecimento por profundidade aparece, a faixa não.

**Textura e qualidade do material real.** O **modelo idealizado** assume uma pedra sem inclusões, sem fraturas internas e sem variação de polimento entre facetas. Um bruto real quase nunca é assim: inclusões espalham e absorvem luz de formas que o modelo não representa, e uma faceta mal polida devolve menos que a mesma faceta perfeita.

**Preferência estética.** A métrica **agrega num único número** o que é, no fim, julgamento de gosto: quanto de brilho vale quanto de fogo, se a cintilação densa é preferível à ampla. A ferramenta pode dizer que o desenho A devolve 4% mais luz que o B; não pode dizer que A é a escolha certa. A ordenação entre os três efeitos da aula 03 é onde o projeto deixa de ser cálculo.

### Por que a tabela e a simulação não competem entre si

A tabela da aula 02 e a simulação não competem em precisão — são ferramentas de dois momentos do projeto. A tabela decide rapidamente, sem software, a partir de uma única informação. A simulação exige um desenho já praticamente definido e serve para refiná-lo e comparar alternativas. Pular direto para ela não economiza trabalho: precisa de um ponto de partida razoável, e é isso que a tabela fornece.

### O lugar certo da ferramenta neste curso

Este curso não ensina a operar GemCad nem GemRay, nem a interpretar seus relatórios — competência de bancada digital, fora do nível teórico daqui. O que importa reter é a **consciência de ferramenta**: essas simulações existem, resolvem um problema real, e têm limites conhecidos — os três acima. Confiar numa métrica alta sem checar esses três pontos arrisca produzir os defeitos das aulas 04 e 05 — agora com um número bonito no relatório.

## Exemplo trabalhado

**Um desenho de brilhante redondo, ajustado no GemCad para um pavilhão de 40,5° num material hipotético de índice de refração 1,76, recebe uma métrica de brilho simulada muito alta no GemRay. O material real é uma safira de cor cheia, com leve zonação em faixas. O que a métrica alta garante, e o que ela deixa em aberto?**

**Observação de partida.** Os 40,5° são deliberadamente um pouco mais rasos que o pavilhão publicado para o coríndon, 42° (aula 02) — coerente com a regra da aula 05 para material de cor cheia. O desenho não está errado; está afinado para cor.

**O que a métrica garante.** A geometria, faceta por faceta, devolve eficientemente a luz simulada dentro do ângulo de observação do software — a RIT (aula 01) está bem resolvida para essa geometria, algo mais fino do que a tabela da aula 02 confirmaria sozinha.

**O que ela deixa em aberto.** A simulação **teria** apontado o escurecimento por profundidade se a safira fosse de cor uniforme — esse mecanismo o GemRay modela. O que ele não pega é a **zonação em faixas** do material real, tratada como cor homogênea; a orientação de mesa em relação a essas faixas continua sendo decisão da leitura do bruto (módulo 05). E nem métrica nem imagem decidem se este desenho é preferível a outro que troque brilho por fogo.

**A lição do exemplo.** A métrica confirma a geometria e boa parte do comportamento de cor — não o material real, com suas zonas, nem a escolha estética entre desenhos igualmente bem resolvidos.

## Erros comuns

- **Tratar uma métrica de brilho simulada como resposta final de qualidade.** Ela resolve o retorno de luz sobre uma geometria e um material idealizados; não resolve a heterogeneidade do bruto real nem arbitra preferência estética.
- **Supor que o ray tracing de facetamento ignora cor.** O GemRay escolhe cor de material, traça vermelho, verde e azul em separado — modelando dispersão — e absorve a luz proporcionalmente ao caminho percorrido. O limite não é a ausência de cor, é a **uniformidade** da cor suposta.
- **Achar que o ray tracing substitui a tabela de ângulos da aula 02.** Ele a complementa, testando variações finas de um desenho específico; é ferramenta de refinamento, não de partida.
- **Confundir GemCad com GemRay.** São dois programas autônomos do mesmo autor: o primeiro especifica a geometria, o segundo abre esse arquivo e simula o comportamento da luz nela.
- **Achar que esta aula ensina a usar essas ferramentas.** O nível deste curso é a consciência de que existem, o que medem e o que não medem — não o manuseio de nenhum software.

## O que não concluir

- Não concluir como instalar, configurar ou operar GemCad ou GemRay — fora do escopo teórico deste curso.
- Não concluir como otimizar um desenho novo em software — autoria de projeto está fora do escopo do curso.
- Não concluir a leitura completa de um diagrama de lapidação real — é assunto do módulo 09.
- Não tomar o exemplo da safira como prova de que ray tracing é inútil — ele resolve bem o problema para o qual foi desenhado, incluindo cor; a lição é sobre o que fica de fora.

## Recap relâmpago

- O ray tracing simula o trajeto de raios de luz individuais através de um modelo geométrico do talhe, aplicando reflexão e refração faceta por faceta, e agrega o resultado em métricas de brilho.
- **GemCad** especifica a geometria exata do diagrama (ângulos, posições de índice, meetpoint); **GemRay**, programa autônomo do mesmo autor (Robert W. Strickland), abre esse arquivo e simula o comportamento óptico da geometria. Ambos foram liberados gratuitamente em 2023, o GemRay em código aberto.
- Essas ferramentas resolvem o que a tabela da aula 02 não resolve: o comportamento óptico fino de um desenho específico, com sua própria geometria.
- O GemRay **modela cor**: cor de material escolhida pelo operador, traçado separado de vermelho, verde e azul (logo, dispersão), absorção proporcional ao caminho óptico e animação de basculamento. Três lacunas reais permanecem: **cor uniforme, não real** (zonação, pleocroísmo e variação de saturação ficam de fora), **textura e qualidade do material** (inclusões, fraturas, polimento variável, ausentes do modelo idealizado) e **preferência estética** (a ordenação entre brilho, fogo e cintilação não é redutível a um número).
- Este curso trata essas ferramentas apenas como consciência de existência e de limite — nunca como tutorial de operação ou de otimização de projeto.

## Próxima aula

Encerra o módulo 08. O próximo módulo do curso — [[09-geometria-e-diagramas-modulo|módulo 09 — Geometria da máquina e leitura de diagramas de lapidação]] — parte exatamente de onde esta aula fechou: como ler um diagrama de lapidação real, a lógica do meetpoint na prática, e a fórmula completa do tangent ratio para reescalar um desenho entre índices de refração diferentes.

## Fontes consultadas

- Robert W. Strickland — *GemCad for Windows* e *GemRay for Windows*, gemcad.com (documentação do autor), e o manual do GemRay (2012). Fonte das capacidades do programa citadas nesta aula: seleção de cor de material, traçado separado dos raios vermelho, verde e azul, absorção proporcional ao caminho óptico, animação de basculamento, e a liberação gratuita de ambos em 2023 com o GemRay em código aberto. Consultadas em 2026-09-04.
- *(O dicionário de facetamento da USFG não contém verbetes para* GemCad *nem* GemRay*: a fonte destes é a documentação do autor, acima.)*
- Vargas & Vargas, *Faceting for Amateurs*; Wykoff, *Techniques of Master Faceting* — o papel do diagrama de lapidação como especificação do projeto, anterior a qualquer simulação.

<!--
nivel: ensino-medio-com-gemologia-v1
palavras_corpo: 1600
cobertura:
  lapidacao-m08-oa06: [Conteúdo, "Exemplo trabalhado", "Erros comuns", "O que não concluir", "Recap relâmpago"]
alegacoes_auditaveis:
  - claim_id: RAY-MODEL-MEDE-001
    claim: "Ray tracing (traçado de raios) é uma técnica de simulação computacional que calcula o trajeto de um número grande de raios de luz individuais através de um modelo geométrico de um objeto, aplicando as leis de reflexão e de refração a cada superfície encontrada; aplicado a um diagrama de lapidação, o cálculo é feito faceta por faceta, e o resultado agregado de milhares de raios é resumido em métricas de brilho que estimam a fração de luz simulada que retorna na direção do observador."
    risk: definicao
    source: "United States Faceters Guild — dicionário de facetamento, referências a modelagem óptica e ray tracing; princípio geral de ray tracing em óptica computacional"
  - claim_id: RAY-FERR-GEMCAD-001
    claim: "GemCad, desenvolvido por Robert W. Strickland, é o software mais citado na comunidade de facetamento amador para especificar a geometria de um diagrama de lapidação — ângulo, índice e altura de cada faceta — e verificar o encontro de facetas (meetpoint). O GemRay NÃO é um módulo do GemCad: é um programa AUTÔNOMO, do mesmo autor, distribuído separadamente, que abre os arquivos salvos pelo GemCad e simula o comportamento óptico da geometria já especificada, calculando métricas de retorno de luz. Strickland aposentou-se em 2023 e liberou os dois gratuitamente, com o GemRay em código aberto."
    risk: definicao
    source: "gemcad.com — páginas GemCad for Windows e GemRay for Windows; manual do GemRay, Robert W. Strickland, 2012. Consultadas em 2026-09-04. CORRIGIDO na auditoria de 2026-09-04 (achado laranja 7): a versão anterior chamava o GemRay de 'módulo' do GemCad e hedgeava o nome como 'referido na literatura como', sugerindo tradição oral incerta, quando é nome próprio documentado de produto com autoria conhecida. O hedge de rodapé 'nomes e atribuição de autoria sujeitos a confirmação' foi removido: a confirmação foi feita."
  - claim_id: RAY-LIMITE-COR-001
    claim: "O GemRay MODELA cor: permite selecionar a cor do material, traça os raios vermelho, verde e azul separadamente e os combina numa imagem colorida (modelando, portanto, dispersão), e absorve a luz proporcionalmente à distância percorrida dentro do material — implementando precisamente o mecanismo de caminho óptico da aula 05. A lacuna real não é a ausência de cor, é a UNIFORMIDADE da cor suposta: o modelo usa uma cor única atribuída pelo operador e não representa zonação, pleocroísmo nem variação de saturação dentro da peça. Um desenho pode obter métrica alta e ainda assim decepcionar num bruto zonado, porque a simulação leu como homogêneo um material que não é — e é por isso que a orientação para zonação (módulo 05) precede o ajuste de profundidade, como a aula 05 estabelece."
    risk: causa-efeito
    source: "gemcad.com — GemRay for Windows; manual do GemRay, Robert W. Strickland, 2012 ('quanto mais longe um raio viaja através do material, mais a luz é absorvida'; seleção de cor de material; traçado RGB separado; animações de basculamento). Consultadas em 2026-09-04. CORRIGIDO na auditoria de 2026-09-04 (achado vermelho 4): a versão anterior afirmava que essas ferramentas não calculam a absorção seletiva que produz a cor — negando ao GemRay capacidades que ele documentadamente tem. Era a primeira das 'três lacunas' e a justificativa de a aula fechar o módulo, e a mesma afirmação estava propagada na aula 05."
  - claim_id: RAY-LIMITE-MAT-001
    claim: "O modelo geométrico usado pelas simulações de ray tracing assume uma pedra idealizada, homogênea, sem inclusões, sem zonação de cor e sem variação de qualidade de polimento entre facetas; um bruto real, como avaliado na leitura do bruto (módulo 05 deste curso), tipicamente contém inclusões que espalham e absorvem luz, e facetas com qualidade de polimento variável, nenhum dos quais representado pelo modelo idealizado da simulação."
    risk: definicao
    source: "Consciência de ferramenta declarada pela literatura de facetamento; módulo 05 deste curso (leitura do bruto — inclusões, zonação, fraturas)"
  - claim_id: RAY-TAB-COMPLEM-001
    claim: "A tabela de ângulos-alvo por índice de refração (aula 02 deste módulo) e a simulação por ray tracing não são etapas concorrentes nem substituíveis entre si: a tabela fornece rapidamente uma faixa de ângulos plausível a partir de uma única variável de entrada (o índice de refração), sem exigir um desenho já definido, enquanto a simulação exige um desenho praticamente completo, faceta por faceta, para refinar variações finas e comparar alternativas de contorno. A tabela funciona como o ponto de partida geometricamente razoável de que a simulação precisa para ser útil."
    risk: causa-efeito
    source: "Síntese entre a aula 02 deste módulo e o papel documentado do ray tracing como ferramenta de refinamento, não de partida, no fluxo de projeto de facetamento"
  - claim_id: RAY-LIMITE-PERCEP-001
    claim: "Uma métrica de brilho simulada agrega o comportamento de um grande número de raios num ÚNICO VALOR NUMÉRICO, e essa agregação embute uma ponderação estética que não é redutível a número: quanto de brilho vale quanto de fogo, se a cintilação densa é preferível à ampla, qual de dois desenhos igualmente bem resolvidos é a escolha certa. A simulação pode afirmar que um desenho devolve mais luz que outro; não pode afirmar que ele é o melhor. A ordenação entre os três efeitos da aula 03 é julgamento de projeto, não cálculo."
    risk: causa-efeito
    source: "Definição dos três efeitos (aula 03 deste módulo) aplicada ao caráter agregado de uma métrica única. AJUSTADO na auditoria de 2026-09-04 (achado vermelho 4): a versão anterior apoiava esta lacuna no caráter ESTÁTICO da métrica ('fotografia congelada'), argumento enfraquecido pelo fato de o GemRay gerar animações de basculamento (tilt); a lacuna foi realocada para a agregação estética, que se sustenta."
-->
