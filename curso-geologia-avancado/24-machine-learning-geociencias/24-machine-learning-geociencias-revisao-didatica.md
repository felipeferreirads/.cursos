# Revisão didática — Módulo 24: Fundamentos e aplicações de machine learning em geociências

**Revisado em:** 2026-09-21 · **Modo:** `review-and-fix`
**Material:** as 6 aulas do módulo (hoje 7, após a divisão descrita abaixo) mais o hub
**Ordem respeitada:** a auditoria científica rodou **antes** (passagem 1 em 2026-09-20, passagem 2 em 2026-09-21) e está com o gate liberado — nenhuma melhoria de clareza foi aplicada sobre fato não verificado.
**Veredito:** **bem ensinado com ressalvas** — 0 achados em aberto.

## Resumo

🔴 1 bloqueia · 🟠 3 prejudicam · 🟡 3 atrito · 🔵 2 sugestões — **todos os 7 achados corrigíveis foram corrigidos**; as 2 sugestões azuis ficam registradas para o questionário e para o gerador de flashcards, que não são desta skill.

**Carga antes → depois**

| Aula | Antes (palavras · min) | Depois | Situação |
|---|---|---|---|
| 01 — IA em geociências | 2.153 · 25,6 | 2.153 · 25,6 | inalterada |
| 02 — Fluxo de trabalho | 2.326 · 27,7 | 2.330 · 27,7 | só referências |
| 03 — Supervisionada (regressão + classificação) | **2.923 · 34,8** | **2.417 · 28,8** | **dividida** |
| 04 — Supervisionada: classificação | — | **1.341 · 16,0** | **aula nova** |
| 05 — Não supervisionada (era 04) | 2.267 · 27,0 | 2.319 · 27,6 | renumerada |
| 06 — Avaliação e validação (era 05) | 2.519 · 30,0 | 2.480 · 29,5 | renumerada + corte |
| 07 — Deep learning (era 06) | **2.622 · 31,2** | **2.514 · 29,9** | renumerada + corte |

- **Aulas acima do teto de 30 min: 2 → 0.** Faixa de duração: 25,6–34,8 min → **16,0–29,9 min**. Duração total: ~176 min em 6 aulas → **~185 min em 7 aulas**.
- **Aulas: 6 → 7.** Conceitos novos na aula mais carregada: ~14 → ~9 (Aula 03) e ~5 (Aula 04).
- **Objetivos declarados sem cobertura: 0 → 0.** A divisão manteve `oa03` coberto, agora por três aulas em vez de duas.
- Métrica de **~84 palavras/min sobre o corpo da aula**, a mesma usada nas revisões didáticas dos Módulos 22 e 23, para que as decisões sejam comparáveis entre módulos. O corpo é medido de `## Conteúdo` até `## Fontes`, incluindo as linhas de código.

> **Por que a carga estourou entre a redação e agora.** As aulas foram entregues pela redação dentro do teto. Foram as **correções da auditoria** que as empurraram para fora: a antiga Aula 03 recebeu três dos nove achados da passagem 2 (o viés de cardinalidade, a convenção de desvio-padrão e a metade faltante do exemplo trabalhado) e passou de ~2.560 para 2.923 palavras; a antiga Aula 06 recebeu outros três e passou de ~2.420 para 2.622. É o mesmo mecanismo observado nos Módulos 22 e 23, e vale registrar como padrão do curso: **correção factual aumenta carga**, e a revisão didática que vem depois dela quase sempre tem trabalho de carga para fazer.

---

## Achados

### 🔴 1. A antiga Aula 03 fazia dois trabalhos: 34,8 minutos e 14 conceitos novos

**claim_id:** `DID-M24-A03-CARGA-001`
**Tipo:** sobrecarga cognitiva · excesso de conceitos novos
**Onde:** antiga Aula 03 (Modelagem supervisionada: regressão e classificação), aula inteira
**Problema:** a aula cobria, numa só sessão, **duas tarefas de aprendizado completas** — regressão e classificação — cada uma com dois algoritmos, mais a interpretação de coeficientes, mais a importância de variável e seu viés, mais a ponte com a krigagem. Contagem de conceitos novos independentes: regressão linear múltipla, mínimos quadrados, coeficiente parcial, padronização de coeficientes, multicolinearidade, árvore de decisão, floresta aleatória, `feature_importances_`, viés de cardinalidade, regressão logística, sigmoide, limiar de decisão, matriz de confusão (em prévia), GLS — **cerca de 14**, contra as 3 ou 4 que uma aula de 30 minutos sustenta. E 34,8 minutos reais contra 29 declarados.

**O sintoma que fechou o diagnóstico** — o mesmo critério usado na divisão do Módulo 23 — foi o **exemplo trabalhado**: ele exercitava **só a metade de regressão** (previsões de `Au_ppb` e cálculo manual do MAE). A metade de classificação não participava do exemplo, e uma aula cujo exemplo trabalhado só exercita metade do que ela ensina está declarando, sem querer, onde fica o seu corte. Um segundo sintoma confirmou: o Recap tinha seis marcadores, dois deles sobre classificação, e nenhum dos dois se conectava aos outros quatro.

**Por que é vermelho:** não é desconforto de leitura. Aos 34,8 minutos o leitor está na terceira família de modelos depois de ter recebido duas ressalvas interpretativas densas (escala de coeficiente e viés de impureza), e a chance de a segunda metade ser lida com atenção residual é alta. O ponto pedagógico mais forte do par — **a ordem entre os dois algoritmos se inverte quando a tarefa muda** — é exatamente o que se perde quando as duas tarefas chegam juntas e apressadas.

**Correção aplicada: divisão em duas aulas, com corte por tarefa.**
- **Aula 03 (Parte 1) — regressão:** regressão linear, leitura dos coeficientes, floresta de regressão e viés de impureza, krigagem como parente, e o **exemplo trabalhado ORIGINAL preservado palavra por palavra** (ele já era de regressão). 2.417 palavras, 28,8 min.
- **Aula 04 (Parte 2) — classificação:** a seção de classificação **preservada palavra por palavra**, mais um preâmbulo de código que torna a aula autocontida, duas frases de ponte com a Parte 1, um **exemplo trabalhado novo** e um **Recap novo**. 1.341 palavras, 16,0 min.
- As duas trazem, no cabeçalho, a nota de par ("Parte 1 de um par" / "Parte 2"), no mesmo padrão que o Módulo 20 usa no par das suas Aulas 02 e 03.
- **Nenhum fato novo foi introduzido.** O exemplo trabalhado da Aula 04 trabalha **apenas** com as contagens das duas matrizes de confusão já auditadas e com a acurácia — e **deliberadamente não usa precisão, revocação nem F1**, que só são definidas na Aula 06. Introduzi-las ali seria criar um salto de pré-requisito no ato de corrigir uma sobrecarga.

**Sobre a assimetria 28,8 × 16,0 min.** Ela é deliberada e vale explicar. O corte foi posto onde o **conteúdo** o pede (a fronteira entre as duas tarefas, denunciada pelo exemplo trabalhado), não onde a contagem de palavras ficaria simétrica. A Parte 2 é intrinsecamente mais curta porque **reaproveita** a maquinaria construída na Parte 1: a floresta aleatória já foi explicada, a leitura de importância de variável já foi estabelecida com a sua ressalva, o conjunto de dados e a partição já são conhecidos. Engordá-la até 25 min exigiria ou inventar conteúdo (vetado: não passaria pelo auditor) ou trazer as métricas de classificação da Aula 06 para cá (o que resolveria a assimetria criando duas outras: um salto de pré-requisito aqui e uma Aula 06 esvaziada). Uma aula de 16 minutos bem delimitada é um resultado melhor do que uma aula de 25 minutos inflada, e o teto do curso é **máximo**, não meta.

**Escopo:** exigiu dividir a aula (autorizado explicitamente pelo orquestrador nesta execução) e renumerar as três aulas seguintes.
**Desfecho:** **corrigido.**

### 🟠 2. Metade do exemplo trabalhado prometido não era entregue

**claim_id:** `DID-M24-A03-EXEMPLO-INCOMPLETO-002`
**Tipo:** exemplo insuficiente
**Onde:** antiga Aula 03 · Exemplo trabalhado
**Problema:** o enunciado pedia "compare, **lado a lado**, a previsão da regressão linear e da floresta aleatória", e a resolução entregava os números de um modelo só, despachando o outro com "conferidas separadamente pelo código da aula". O leitor não conseguia executar o que o enunciado mandava com o que a aula fornecia.
**Correção aplicada:** este achado foi levantado **em paralelo pela auditoria científica** da mesma data (achado 15, `MLGEO-M24-A03-EXEMPLO-RF-PREVISOES-010`), que obteve as previsões por execução (7,65; 5,75; 21,18 ppb) e completou o exemplo com a aritmética dos erros. A revisão didática **não duplicou a correção**; registra-se aqui porque o defeito é dos dois tipos ao mesmo tempo — factual (número ausente) e didático (exemplo que não cumpre o próprio enunciado) — e porque o resultado didático é excelente: o exemplo passou a mostrar que **a ordem entre os dois modelos se inverte** entre 3 e 15 amostras, o que sustenta com evidência a moral que antes era só afirmada.
**Escopo:** correção local, já aplicada pela auditoria.
**Desfecho:** **corrigido** (pela auditoria; verificado aqui).

### 🟠 3. Uma seção-chave da Aula 06 falava de um resultado produzido em outra aula, sem os objetos para reproduzi-lo

**claim_id:** `DID-M24-A06-DEPENDENCIA-NAMESPACE-003`
**Tipo:** salto de pré-requisito (operacional)
**Onde:** Aula 06 (era 05) · seção "Métricas de classificação: a matriz de confusão" e as três seções seguintes
**Problema:** a aula abre a seção mais importante com "**Saída esperada**, para a regressão logística da Aula 03" — isto é, ela interpreta um resultado que **não produz**, e cujos objetos ela não recarrega. Do ponto de vista de quem estuda, isso tem duas consequências: o leitor precisa ter a sessão anterior aberta (o que a aula não dizia), e não tem como conferir de onde vêm as quatro células da matriz.
**Correção aplicada:** a auditoria científica já havia corrigido a face **factual** do problema (achado 10, vermelho: os nomes de variável estavam errados e o código levantava exceção) e acrescentado o parágrafo "Continuidade de código". A revisão didática **estendeu** esse parágrafo para a face pedagógica: ele agora declara, objeto por objeto, **qual aula produz o quê** (`X` e `y` vêm da Aula 03; `y2`, a partição estratificada e `pred_logit` vêm da Aula 04), em vez de dizer só "o ambiente da Aula 03". A divisão da antiga Aula 03 tornou essa explicitação obrigatória — e, de quebra, melhor: a matriz de confusão que a Aula 06 formaliza é agora produzida na aula **imediatamente anterior** (Aula 04), não duas aulas antes.
**Escopo:** correção local.
**Desfecho:** **corrigido.**

### 🟠 4. Treze referências cruzadas apontariam para a aula errada depois da divisão

**claim_id:** `DID-M24-MOD-REFERENCIAS-CRUZADAS-004`
**Tipo:** integridade de progressão
**Onde:** as sete aulas e o hub
**Problema:** o módulo é fortemente encadeado — as aulas se citam 90 vezes por número ("a Aula 05 formaliza", "retomada na Aula 06", "as Aulas 03 a 06 vão reabrir"). Uma divisão que renumera três aulas e não reescreve cada uma dessas referências produz um material em que **a navegação mente**, o que é pior do que não ter referência nenhuma: o leitor abre a aula citada, não encontra o assunto, e perde a confiança no encadeamento inteiro.
**Problema específico e mais traiçoeiro:** as referências **plurais e de intervalo** ("Aulas 03 a 06", "Aulas 03 e 05", "Aulas 02 a 05") não se resolvem por substituição mecânica de número, porque cada uma delimita um **conjunto de assuntos**, não um índice. "Os métodos das Aulas 03 a 05, nenhum deles uma rede neural" e "os métodos mais simples das Aulas 03 a 05" viraram, respectivamente, "03 a 06" e "03 a 05" — a primeira mudou, a segunda não, porque a primeira incluía a aula de métricas e a segunda não.
**Correção aplicada:** as 90 referências foram remapeadas **uma a uma, por significado**, não por número. Cada substituição foi aplicada por script com contagem esperada declarada, de modo que qualquer divergência abortasse a operação em vez de reescrever silenciosamente o trecho errado. Em particular, as referências a "Aula 03" foram separadas em três grupos: as que falam de **regressão** (permaneceram 03), as que falam de **classificação** (viraram 04) e as que falam das duas (viraram "Aulas 03 e 04"). As 13 referências de intervalo foram reavaliadas pelo conjunto de assuntos que delimitam.
**Escopo:** correção local, em todos os arquivos do módulo.
**Desfecho:** **corrigido** — verificado por varredura: nenhum slug antigo e nenhum ID antigo restam no módulo, e o validador de links não aponta nenhum link quebrado no Módulo 24.

### 🟡 5. Duas aulas ficaram no limite depois das correções da auditoria

**claim_id:** `DID-M24-A06A07-CARGA-005`
**Tipo:** carga cognitiva no limite
**Onde:** Aula 06 (30,0 min) e Aula 07 (31,2 min)
**Problema:** as duas terminaram a auditoria no teto ou acima dele. A Aula 07 é a mais delicada do módulo para dividir — ela fecha o arco do módulo (rede neural → dois estudos de caso → interpretação → comunicação → tabela-resumo dos seis modelos), e cortá-la em duas fragmentaria justamente a narrativa de fechamento.
**Correção aplicada:** em vez de dividir, **corte de prolixidade** — a correção mínima que resolve, dado que o excesso era de 0,0 e 1,2 min, não de conceitos. Quatro cortes na Aula 07 (a ressalva da importância por permutação condensada sem perder nenhum fato; o parêntese do ranking; a recomendação de classificação, hoje redundante com o novo exemplo da Aula 04; e o fecho da tabela-resumo) e dois na Aula 06 (a duplicação "recebe todo o conjunto / usa o conjunto inteiro", e o cenário dos 5% que o próprio exemplo trabalhado da aula repete em seguida com números). Resultado: **29,5 e 29,9 min**. Nenhum conceito, número ou ressalva foi removido — só palavras que os diziam duas vezes.
**Escopo:** correção local.
**Desfecho:** **corrigido.**

### 🟡 6. Redundância: o mesmo cenário de desbalanceamento demonstrado duas vezes na mesma aula

**claim_id:** `DID-M24-A06-REDUNDANCIA-DESBALANCEAMENTO-006`
**Tipo:** redundância
**Onde:** Aula 06 · seção "Métricas de classificação" (parágrafo "Por que a acurácia sozinha engana") e Exemplo trabalhado
**Problema:** o parágrafo demonstrava o argumento com um cenário hipotético de 5% de amostras mineralizadas e 95% de acurácia; o exemplo trabalhado, três telas depois, demonstrava **o mesmo argumento** com 4% de encostas instáveis e 96% de acurácia. Duas demonstrações do mesmo ponto, com números diferentes, na mesma aula — e a segunda é a boa, porque é completa (tem matriz de confusão, revocação zero e precisão indefinida) e porque a decisão que ela pede ao leitor é realista.
**Correção aplicada:** o parágrafo foi reduzido a **anunciar** o que o exemplo trabalhado vai fazer e a guardar o que precisa ser retido agora (por que precisão, revocação e F1 são indispensáveis quando a classe de interesse é a rara). A demonstração ficou onde funciona melhor: no exemplo, com números.
**Escopo:** correção local.
**Desfecho:** **corrigido.**

### 🟡 7. O `palavras_corpo` das aulas estava desatualizado e o hub anunciava contagens erradas

**claim_id:** `DID-M24-MOD-METADADOS-CARGA-007`
**Tipo:** atrito de manutenção
**Onde:** bloco de metadados das sete aulas e "Registro do módulo" no hub
**Problema:** o campo `palavras_corpo` é o insumo da decisão de carga, e estava desatualizado **desde a passagem 1 da auditoria** — a antiga Aula 03 declarava 2.298 palavras quando já tinha ~2.560. Um campo de carga desatualizado é pior que ausente: ele faz a revisão seguinte concluir que a aula está dentro do teto quando ela não está, que é exatamente o que quase aconteceu aqui. O hub, pelo mesmo motivo, anunciava 38 alegações auditáveis quando já havia 51, e uma distribuição por aula que não correspondia a nenhum arquivo.
**Correção aplicada:** `palavras_corpo` recontado nas sete aulas pela mesma métrica, e o registro do hub refeito com as contagens reais (52 alegações, com a distribuição por aula), a faixa de duração e o veredito das duas etapas de qualidade.
**Escopo:** correção local.
**Desfecho:** **corrigido.**

### 🔵 8. Sugestão: o par Aula 03 / Aula 04 é o melhor material de questão do módulo, e pede uma questão que atravesse as duas

**claim_id:** `DID-M24-A03A04-SUGESTAO-AVALIACAO-008`
**Onde:** Aulas 03 e 04
**Observação:** a divisão criou uma oportunidade que não existia. Os mesmos dois algoritmos, sobre os mesmos dados, em duas tarefas, com **resultado invertido** (linear ganha na regressão, floresta ganha na classificação) é o tipo de comparação que uma questão de aplicação explora muito bem — e que uma questão de memorização estraga, se perguntar apenas "qual modelo é melhor". A pergunta boa é *por que* a ordem se inverte (forma da fronteira de decisão contra linearidade da relação subjacente, com o tamanho da amostra pesando nos dois casos).
**Encaminhamento:** `gerador-de-questionarios`, no Parcial 2. Não é correção; nada foi alterado.

### 🔵 9. Sugestão: um apoio visual ajudaria em dois pontos específicos

**claim_id:** `DID-M24-MOD-SUGESTAO-VISUAL-009`
**Onde:** Aula 04 (fronteira de decisão) e Aula 06 (curva treino × teste)
**Observação:** dois momentos do módulo são intrinsecamente geométricos e hoje são explicados só em prosa. (i) Na Aula 04, "um método que particiona o espaço em regiões contra um método que traça um único plano" é a explicação central do resultado, e um esquema de duas fronteiras sobre a nuvem de pontos a tornaria imediata. (ii) Na Aula 06, o diagnóstico de sobreajuste é uma **curva** (acurácia de treino subindo para 1,000 enquanto a de teste despenca para 0,533 conforme a profundidade cresce) apresentada como cinco linhas de texto impresso. As duas são figuras que o próprio código do módulo geraria com `plt.scatter` e `plt.plot`. **Não implementei** porque exigiria escrever e verificar código novo, gerando conteúdo que não passou pelo auditor — e o módulo já declara Matplotlib como pré-requisito (Módulo 23, Aula 01), então a lacuna é de ilustração, não de capacidade.
**Encaminhamento:** próxima passagem de conteúdo, se houver. Não é correção; nada foi alterado.

---

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo trabalhado | Avaliação planejada |
|---|---|---|---|
| `oa01` — situar os ramos da IA e os desafios dos dados geológicos | Aula 01 (4 seções) | sim (três tarefas a classificar) | Parcial 1, Final |
| `oa02` — executar o fluxo de trabalho em Python | Aula 02 (6 seções) | sim (partição de regressão) | Parcial 1, Final |
| `oa03` — selecionar e aplicar modelos supervisionados e não supervisionados | Aula 03 (regressão), **Aula 04 (classificação)**, Aula 05 (não supervisionado), e a Aula 07 nas duas seções de estudo de caso | sim, um em cada uma das quatro | Parcial 2, Final |
| `oa04` — avaliar desempenho, diagnosticar sobreajuste, interpretar e comunicar | Aula 06 (4 seções), Aula 07 (interpretação e comunicação) | sim (as 200 encostas; a tabela dos seis modelos) | Parcial 3, Final |

**Nenhum objetivo sem cobertura, e nenhuma seção órfã.** A divisão preservou a cobertura de `oa03`, que agora se distribui por três aulas em vez de duas — e o mapa `mapa_objetivo_secao` de cada aula foi ajustado para refletir isso.

## O que está bem feito (e deve ser preservado)

Vale registrar, porque é o que dá ao módulo a qualidade que ele tem e o que uma revisão futura não deveria "melhorar":

1. **O conjunto de dados único, com semente fixa, atravessando seis aulas.** É a melhor decisão de projeto do módulo. Ele permite que a comparação entre modelos seja literal (mesmas 45 amostras de treino, mesmas 15 de teste), e transforma a tabela-resumo final num fechamento de verdade em vez de uma lista. A `cota_m` deliberadamente irrelevante, plantada na Aula 02 e cobrada como teste de sanidade em três aulas diferentes, é um dispositivo pedagógico de primeira ordem.
2. **O módulo ensina o que não funciona, com números.** O MLP de regressão com R² negativo, a floresta que perde para a regressão linear, a acurácia de 0,333 sem padronização, a cota de ruído superando a litologia real na importância por impureza: um material introdutório que só mostra sucessos ensina a confiar em modelos; este ensina a desconfiar deles, o que é o que um geólogo precisa.
3. **As pontes com o Módulo 20 são reais, não decorativas.** Krigagem como GLS, *leave-one-out* como caso extremo de k-fold, domínios geoestatísticos contra agrupamento: nos três casos a aula diz **onde a analogia quebra**, que é o que distingue uma ponte de uma confusão.
4. **A advertência sobre vazamento espacial aparece três vezes, deliberadamente** (Aulas 01, 02 e 06) — e isso **não** é a redundância do achado 6. É reforço em ponto difícil, cada vez num registro diferente (conceito, código, correção por `GroupKFold`), que é exatamente como um ponto contraintuitivo deve ser tratado em material autodidata.

## Observação fora do escopo desta skill

**Nenhum desalinhamento aula–avaliação a reportar**, porque o módulo ainda **não tem** questionário nem baralho de flashcards — os dois vêm depois, e é a ordem certa: eles nascerão sobre um material já corrigido e já redividido, sem retrabalho. O plano de avaliação (3 parciais + 1 final, um parcial por objetivo) foi decidido e registrado no hub e no `course-state.yaml`, mas **não foi gerado** nesta passagem.
