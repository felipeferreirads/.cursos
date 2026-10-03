# Auditoria científica — Módulo 24: Fundamentos e aplicações de machine learning em geociências

**Data do levantamento:** 2026-09-21 (passagem 2) · **Correções aplicadas em:** 2026-09-21
**Modo:** `audit-and-fix` · **Profundidade:** `full`
**Escopo:** as 6 aulas do módulo, auditadas em conjunto, mais o hub do módulo · duas passagens (ver abaixo)

> ### Nota obrigatória sobre a passagem 1 (2026-09-20) — leia antes de usar a numeração
> Este módulo foi auditado em **duas passagens**, e a primeira **não deixou relatório em disco**: a sessão de 2026-09-20 aplicou correções nas aulas e registrou as alegações correspondentes nos blocos de metadados, mas terminou antes de gravar o `auditoria.md`, o `.json` e o bloco `audit` do `course-state.yaml`. O que sobreviveu dela são **seis marcas explícitas** nos metadados das aulas, na forma `ACHADO N DA AUDITORIA de 2026-09-20`:
>
> | Achado | Onde ficou registrado | O que corrigiu |
> |---|---|---|
> | **1** | a03 · `MLGEO-M24-A03-COEFICIENTES-ESCALA-008` | a aula atribuía a desproporção do coeficiente de As à multicolinearidade; a causa direta é a **escala** da variável |
> | **2** | a04 · `MLGEO-M24-A04-INERCIA-K1-008` | a inércia com $k=1$ era dita "equivalente à variância total multivariada"; ela é **$n$ vezes** essa variância (erro de fator 60) |
> | **3** | a02 · `MLGEO-M24-A02-GETDUMMIES-DTYPE-007` | a saída declarada de `get_dummies` era `1/0`; o padrão do pandas 3.0 é **booleano** (`True/False`) |
> | **5** | a04 · `MLGEO-M24-A04-LIMIAR-CONTAGEM-009` | as 39 amostras anômalas eram atribuídas ao limiar sozinho; são **36 do limiar ± 5 trocas de ruído** (36 − 1 + 4) |
> | **8** | a03 · `MLGEO-M24-A03-KRIGAGEM-REGRESSAO-006` | "regressão linear generalizada" (ambíguo) → **mínimos quadrados generalizados (GLS)**, com a advertência GLS ≠ GLM |
> | **9** | a01 · `MLGEO-M24-A01-CNN-VIT-ESTADO-ARTE-006` | CNN apresentada como estado da arte em classificação de imagem; hoje os **ViT** lideram os referenciais de larga escala |
>
> Os achados **4, 6 e 7** daquela passagem foram aplicados ao corpo das aulas **sem deixar marca** nos metadados e **não são reconstrutíveis** — nenhum arquivo em disco os documenta. Esta passagem 2 releu o módulo inteiro do zero, de modo que qualquer problema remanescente deles estaria agora capturado pelos achados 10 a 18; mas o registro histórico deles está **perdido**, e isso fica declarado aqui em vez de disfarçado.
>
> **A numeração não foi reciclada.** Os achados desta passagem começam em **10**, para que as marcas já gravadas nas aulas (1, 2, 3, 5, 8, 9) continuem apontando para o que apontam. Os `claim_id` da passagem 1 também foram preservados sem renumeração.

> ### Nota posterior, acrescentada em 2026-09-21 pela revisão didática — nenhum achado deste relatório foi reaberto, renumerado ou revertido
> A revisão didática **dividiu a Aula 03** (achado `DID-M24-A03-CARGA-001`), e o módulo passou de 6 para 7 aulas. **Toda a numeração de aula deste relatório é a de antes da divisão.** O mapa de tradução:
>
> | Neste relatório | Hoje em disco |
> |---|---|
> | **a03** (regressão + classificação) | **par a03 + a04**. Ficaram na **a03**: regressão linear, coeficientes, floresta de regressão, krigagem e o exemplo trabalhado — ou seja, os achados 🟠 **11**, 🟠 **15**, 🟡 **17** e 🟡 **18**. Ficou na **a04**: a seção de classificação, com as duas alegações que migraram (`-CLASSIFICACAO-RESULTADO-003` e `-REGRESSAO-LOGISTICA-CONCEITO-005`), e é lá que está hoje a evidência numérica do achado 11 (cota 0,086 contra litologia 0,025) |
> | **a04** (não supervisionada) | **a05** — arquivo renomeado, ID alterado para `geologia-avancado-m24-a05` |
> | **a05** (avaliação) | **a06** — arquivo renomeado, ID `...-a06`. **É a aula do achado vermelho 10** |
> | **a06** (deep learning) | **a07** — arquivo renomeado, ID `...-a07`. Achados 🟠 **12**, 🟠 **13** e 🟠 **14** |
>
> Os `claim_id` **não** foram renumerados, aqui nem nos arquivos: os prefixos `A03`, `A04`, `A05` e `A06` designam a numeração em que cada alegação foi **emitida**, não a aula onde ela hoje mora. Os caminhos em `files_touched` do manifesto `.json` são os de **antes** da divisão; os atuais estão em `files_touched_pos_divisao`.
>
> **Duas correções deste relatório foram estendidas pela revisão didática, sem introduzir fato novo.** (i) O parágrafo "Continuidade de código", criado pelo achado 10, passou a declarar objeto por objeto qual aula produz o quê, porque com a divisão os objetos de classificação passaram a vir da Aula 04 e não mais da 03 (ver `DID-M24-A06-DEPENDENCIA-NAMESPACE-003`). (ii) A ressalva do achado 13 foi **condensada** para caber no teto de 30 min da aula, preservando os três números e a fonte (ver `DID-M24-A06A07-CARGA-005`). **O gate do módulo continua liberado**, e os **26** blocos de código das sete aulas foram reexecutados depois da divisão, na nova cadeia declarada, sem nenhuma falha.

**Veredito:** **aprovado — gate liberado.** 0 achados vermelhos e 0 laranjas **em aberto**. Os 9 achados numerados desta passagem (1 vermelho, 5 laranjas, 3 amarelos) foram **todos corrigidos cirurgicamente**. Nenhum achado azul-escuro (🔵 sem fonte) nem branco (⚪ controverso) foi levantado — a justificativa está na seção "Por que nenhum 🔵 e nenhum ⚪". **Questionário e flashcards liberados**, observadas as restrições ao fim deste relatório.

## Contagem por severidade (passagem 2)

| Severidade | Contagem | Situação |
|---|---|---|
| 🔴 Vermelho (afirmação factualmente falsa) | **1** | **corrigido** |
| 🟠 Laranja (impreciso, inconsistência interna, confusão de escopo, omissão que gera erro) | **5** | **corrigidos** |
| 🟡 Amarelo (desatualização, atribuição errada, propagação faltante) | **3** | **corrigidos** |
| 🔵 Azul (verificado e correto — registro de que foi checado) | **41** | sem alteração (são registros de verificação bem-sucedida) |
| ⚪ Branco (questão aberta na literatura) | **0** | — |

> **Nota sobre as contagens:** os números da coluna "Contagem" são os do levantamento e não mudam — um achado não se apaga ao ser corrigido, ele muda de situação. Somando as duas passagens, o módulo tem **15 achados numerados** (1, 2, 3, 5, 8, 9 da passagem 1 + 10 a 18 da passagem 2), com 4, 6 e 7 perdidos conforme a nota acima.

**Alegações rastreadas:** a redação declarou **38**; a passagem 1 acrescentou 5 (chegando a 43) e esta passagem acrescentou **8**, fechando em **51 alegações declaradas nos arquivos** (6 na a01, 8 na a02, 11 na a03, 9 na a04, 8 na a05, 9 na a06). Todas as 51 foram verificadas nesta passagem; **nenhuma ficou não verificada**. Os IDs são únicos e todos seguem o padrão `MLGEO-M24-A0N-TEMA-NNN`.

## Método específico deste módulo

Este é o segundo módulo inteiramente computacional do curso (depois do 23), e o método foi o mesmo, endurecido num ponto: os **22 blocos de código Python das seis aulas foram extraídos dos arquivos e executados**, e cada saída foi comparada **dígito a dígito** com a saída declarada no texto. Duas diferenças em relação ao Módulo 23:

1. **Execução na cadeia declarada, não bloco a bloco.** As Aulas 02, 03 e 05 declaram compartilhar o mesmo ambiente (a 05 não recarrega dados), então os blocos das três foram executados **num único namespace, em sequência**, exatamente como o aluno faria. As Aulas 04 e 06 são autocontidas e rodaram isoladas. **Foi só assim que o achado vermelho apareceu** — bloco a bloco, com as variáveis "certas" injetadas à mão, os cinco blocos da Aula 05 passam; na cadeia real, todos os cinco falham.
2. **Ambiente idêntico ao declarado:** Python 3.13.2, NumPy 2.5.1, pandas 3.0.3, scikit-learn 1.9.1, Matplotlib 3.11.2 — as mesmas versões que as aulas declaram, o que elimina a diferença de versão como explicação para qualquer divergência.

**Resultado:** **nenhuma saída numérica declarada no módulo está errada.** Os 41 itens azuis registram isso. O único achado vermelho é de **continuidade de código**, não de conteúdo: os números estavam certos, o caminho para chegar até eles não existia.

A segunda frente foi a verificação contra os **arquivos do próprio curso** (Módulos 20 e 23, declarados pré-requisitos) — e foi lá que saiu um dos amarelos, como já havia ocorrido nos Módulos 22 e 23.

---

## Padrão dominante

**O MÓDULO ACERTA O QUE CALCULA E ESCORREGA NO QUE CONTA SOBRE O CÁLCULO.** Nenhum dos nove achados é um número errado. Todos são erros de *segunda ordem*: o código roda, o resultado está certo, e o que falha é a **frase que interpreta o resultado** — a atribuição da causa, a ressalva ausente, a comparação que não fecha, o nome da variável, o crédito à aula anterior. Três assinaturas se repetem:

1. **Interpretação de importância de variável sem as ressalvas dos métodos.** Dois achados laranjas (11 e 13) são o mesmo problema visto por dois lados. A Aula 03 usa `feature_importances_` como teste de sanidade sem a ressalva de que ela é enviesada a favor de variáveis contínuas — e o próprio módulo dá o contraexemplo, com a cota irrelevante (0,086) superando a litologia real (0,025). A Aula 06 usa importância por permutação e declara o resultado "consistente" com a floresta, omitindo que a variável que era a segunda mais importante virou zero — porque a permutação dilui variáveis correlacionadas. As duas limitações estão **documentadas na mesma página** do scikit-learn, uma ao lado da outra. Corrigidos, os dois trechos passaram a se sustentar mutuamente: cada método expõe o ponto cego do outro.
2. **A comparação que atravessa a fronteira da métrica.** O achado 14 (laranja) é o módulo tentando ordenar seis modelos num ranking único quando três são medidos por R² e três por acurácia. O resultado pedagógico central do módulo — a rede neural como pior caso — sobrevive intacto ao recorte correto (pior **entre os três de regressão**, e o único R² negativo do módulo); o que caiu foi só a generalização indevida.
3. **O crédito à aula anterior que a aula anterior não sustenta.** O achado 16 (amarelo) repete a assinatura já documentada nos Módulos 22 e 23: a Aula 02 atribui ao Módulo 20, Aula 01, o par "histograma + gráfico de dispersão". Lá o par é **histograma + boxplot**, e a palavra "dispersão" aparece apenas no sentido estatístico de espalhamento — gráfico de dispersão **nunca** é usado naquela aula, onde a relação entre duas variáveis é tratada algebricamente. **O corolário para os módulos seguintes, agora pela terceira vez:** quando a aula cita outra aula do próprio curso, a citação é o ponto de falha mais provável do texto, porque é a única fonte que o autor não abre para conferir — ele lembra do que escreveu.

Um quarto ponto, mais grave em consequência prática que em natureza: o achado 18 (amarelo) mostra que a **passagem 1 corrigiu o corpo da Aula 03 e esqueceu o cabeçalho da mesma aula e o hub do módulo**, que continuavam anunciando a expressão "regressão linear generalizada" que aquele achado existiu para remover. Propagação incompleta dentro do mesmo arquivo é o modo de falha mais silencioso de uma correção — e é exatamente por isso que o `affected_files` de cada achado deste relatório lista também cabeçalho, recap e hub, não só o parágrafo do corpo.

---

## Achados

### 🔴 10. Os cinco blocos de código da Aula 05 não rodam no ambiente que a própria aula declara

**claim_id:** `MLGEO-M24-A05-NAMESPACE-CONTINUIDADE-008`
**Tipo:** inconsistência interna / saída declarada inalcançável
**Onde:** a05 · todos os cinco blocos de código (matriz de confusão, `classification_report`, árvores de decisão, validação cruzada de acurácia, validação cruzada de MAE)
**Está escrito:** `cm = confusion_matrix(y_test, pred)` · `classification_report(y_test, pred, digits=3)` · `DecisionTreeClassifier(...).fit(X_train, y_train)` · `cross_val_score(rfc, X, y, cv=kf, scoring="accuracy")` · `cross_val_score(LinearRegression(), X, y_reg, ...)`
**Problema:** a Aula 05 **não recarrega os dados nem refaz as partições** — ela declara como pré-requisito a Aula 03 e roda no ambiente de lá. No ambiente da Aula 03, `y`, `y_train`, `y_test` e `pred` são os objetos da tarefa de **regressão** (alvo `Au_ppb`, partição não estratificada); a tarefa de classificação usa `y2`, `X_train2`, `y_train2`, `X_test2`, `y_test2` e `pred_logit`. Os quatro primeiros blocos da Aula 05 são de **classificação** e usam os nomes da regressão. Não é uma questão de estilo nem de número ligeiramente diferente: **os quatro blocos levantam exceção**, e o quinto usa `y_reg`, um nome que não existe em nenhuma das Aulas 02, 03 ou 05 (só aparece na Aula 06, uma aula **depois**). Verificado por execução, na ordem declarada:

| Bloco | Erro real |
|---|---|
| `confusion_matrix(y_test, pred)` | `ValueError: continuous is not supported` |
| `classification_report(y_test, pred)` | `ValueError: continuous is not supported` |
| `DecisionTreeClassifier().fit(X_train, y_train)` | `ValueError: Unknown label type: continuous. Maybe you are trying to fit a classifier ... on a regression target` |
| `cross_val_score(rfc, X, y, scoring="accuracy")` | `ValueError: All the 5 fits failed` |
| `cross_val_score(LinearRegression(), X, y_reg, ...)` | `NameError: name 'y_reg' is not defined` |

**Por que é vermelho e não laranja:** toda "Saída esperada" da aula é, como escrita, **factualmente falsa** — o código que a antecede não produz aquela saída, produz uma exceção. E o dano é máximo justamente na aula mais operacional do módulo: é a única aula em que o aluno não tem como descobrir sozinho o que deu errado, porque o erro não está no que ele digitou, está no material. Os **números** declarados, por outro lado, estão todos certos: com os objetos corretos, as cinco saídas se reproduzem dígito a dígito.
**Correção aplicada:** os cinco blocos passaram a usar os nomes da Aula 03 (`y_test2`, `pred_logit`, `X_train2`/`y_train2`/`X_test2`/`y_test2`, `y2` para classificação e `y` para a regressão), e um parágrafo **"Continuidade de código"** foi acrescentado antes do primeiro bloco, declarando explicitamente quais objetos vêm da Aula 03 e avisando que trocar as partições dá **erro**, não número errado. Duas frases de entorno foram ajustadas por coerência (`X, y` → `X, y2` no texto, e a introdução do último bloco explicitando a volta ao alvo de regressão).
**Fonte:** execução direta dos cinco blocos no namespace declarado — scikit-learn 1.9.1, mensagens de erro transcritas acima; e verificação de que, corrigidos, os 22 blocos das seis aulas rodam na sequência declarada sem nenhuma falha.
**Confiança:** confirmado (por execução)
**Também aparece em:** nenhum outro arquivo — o defeito é local à Aula 05.

### 🟠 11. `feature_importances_` usada como teste de sanidade sem a ressalva de viés de cardinalidade — e o módulo contém o contraexemplo

**claim_id:** `MLGEO-M24-A03-MDI-VIES-CARDINALIDADE-009`
**Tipo:** omissão que gera erro
**Onde:** a03 · seção "Regressão com floresta aleatória", seção "Classificação" e Recap
**Está escrito:** "a de menor importância de todas é justamente `litologia_xisto`, quase zero, **sugerindo que a informação de litologia já está capturada indiretamente pelos teores geoquímicos correlacionados a ela**" e, no Recap, "(A `feature_importances_` da floresta já é adimensional e **não precisa dessa correção**.)"
**Problema:** a explicação oferecida é plausível mas **incompleta de um jeito que engana**, e a prova está no próprio módulo. A importância por redução de impureza é documentadamente enviesada **a favor de variáveis de alta cardinalidade** (contínuas) e **contra** binárias. Na floresta de classificação da mesma aula, `cota_m` — que é **puro ruído por construção** — recebe importância **0,086**, maior que a de `litologia_xisto` (**0,025**), que carrega informação geológica real. Ou seja: a aula usa a `feature_importances_` como instrumento de teste de sanidade ("a variável irrelevante deve pesar pouco") sem dizer que o instrumento tem um viés capaz de inverter a ordem entre uma variável de ruído e uma variável verdadeira — e sem notar que, na sua própria tabela, ele **inverteu**. O aluno sai com a leitura "a litologia não informa nada", quando parte daquele zero é artefato do método.
**Correção aplicada:** três edições cirúrgicas na a03. (i) Na seção da floresta de regressão, a ressalva foi acrescentada com o viés nomeado, o contraexemplo do próprio módulo (0,086 contra 0,025) e o encaminhamento para a importância por permutação da Aula 06 como medida sem esse viés. (ii) Na seção de classificação, a inversão passou a ser apontada onde os dois números aparecem, com a advertência explícita de não ler "a elevação informa mais que a rocha encaixante". (iii) No Recap, "não precisa dessa correção" virou "não precisa dessa correção **de escala** — mas tem um viés próprio".
**Fonte:** documentação oficial scikit-learn 1.9.1, [5.2 Permutation feature importance](https://scikit-learn.org/stable/modules/permutation_importance.html), consultada em 2026-09-21: as importâncias por impureza são *"strongly biased"* e *"favor high cardinality features (typically numerical features) over low cardinality features such as binary features"*; *"permutation-based feature importances do not exhibit such a bias"*. · **Nível:** documentação normativa da biblioteca. Valores 0,086 e 0,025 confirmados por execução.
**Confiança:** confirmado
**Também aparece em:** a06 (a seção de importância por permutação, tratada no achado 13, ficou coerente com esta correção); Recap da a03.

### 🟠 12. "A rede converge" contradiz o `ConvergenceWarning` que a própria aula produz

**claim_id:** `MLGEO-M24-A06-CONVERGENCIA-007`
**Tipo:** inconsistência interna
**Onde:** a06 · seção "Estudo de caso 2: regressão — quando mais capacidade piora o resultado"
**Está escrito:** "a rede **converge** (depois de atingir o limite de 5.000 iterações sem sinal claro de estabilização, um aviso adicional de que o ajuste está no limite) para uma solução que reproduz o treino quase exatamente e generaliza mal"
**Problema:** a frase afirma e nega a mesma coisa em dez palavras. A rede **não** converge: `mlp_reg.n_iter_` = 5.000, isto é, o treinamento termina por **esgotar** o limite de iterações, e o scikit-learn emite um `ConvergenceWarning` — que, ademais, **aparece impresso na tela junto com os resultados** e não estava anunciado em nenhuma "Saída esperada" da aula, embora o metadado da própria alegação `-REGRESSAO-SOBREAJUSTE-004` o registre corretamente. O aluno vê um aviso que o texto não previu, sobre um fenômeno que o texto nega. (Por contraste, os dois `MLPClassifier` da aula **convergem** de fato, em 2.514 de 3.000 iterações, e não emitem aviso — a assimetria é informativa e agora está no texto.)
**Correção aplicada:** a frase foi reescrita para "a rede **não converge**: o treinamento termina por esgotar o limite de 5.000 iterações, e o scikit-learn imprime um `ConvergenceWarning` junto com os números acima — um aviso adicional, na própria saída, de que o ajuste está no limite. Ela para numa solução que reproduz o treino quase exatamente e generaliza mal."
**Fonte:** execução direta do bloco com captura explícita de avisos (scikit-learn 1.9.1): `n_iter_` = 5.000 e `ConvergenceWarning` emitido para o `MLPRegressor`; `n_iter_` = 2.514 sem aviso para o `MLPClassifier`.
**Confiança:** confirmado (por execução)
**Também aparece em:** nenhum outro arquivo (o Recap da a06 já falava de sobreajuste, não de convergência).

### 🟠 13. Importância por permutação declarada "consistente" com a da floresta, omitindo a divergência que mais ensina

**claim_id:** `MLGEO-M24-A06-PERMUTACAO-CORRELACAO-008`
**Tipo:** omissão que gera erro
**Onde:** a06 · seção "Interpretação: importância por permutação"
**Está escrito:** "O padrão qualitativo — `Cu_ppm` dominando, a variável geograficamente irrelevante (`cota_m`) entre as mais baixas — **é consistente** com o que a importância de variável da floresta (Aula 03) já havia mostrado"
**Problema:** a afirmação é verdadeira nos dois aspectos que escolhe citar e **silencia sobre o terceiro**, que é o mais visível: `dist_falha_m` é a **segunda variável mais importante** na floresta de regressão (0,240) e na de classificação (0,261), e na importância por permutação do MLP ela é **−0,002**, ou seja, nula. Selecionar os dois pontos de concordância e chamar o conjunto de "consistente" deixa o aluno com a impressão de que os dois métodos concordam, quando eles divergem de forma dramática numa variável central — e, pior, deixa aberta a leitura errada de que a distância à falha é irrelevante, que a Aula 03 já havia trabalhado para desmontar. A causa é conhecida e documentada: `dist_falha_m` correlaciona **r = −0,90** com `Cu_ppm`, e a importância por permutação **dilui variáveis correlacionadas**, porque embaralhar uma delas não derruba o desempenho — o modelo recupera a mesma informação pela outra.
**Correção aplicada:** um parágrafo foi acrescentado logo após o trecho, nomeando a divergência com os três números (0,240 / 0,261 / −0,002), dando a causa documentada, amarrando-a ao raciocínio do coeficiente parcial pequeno da Aula 03 ("acrescenta pouco ao que as outras já dizem" ≠ "não tem relação com o alvo") e fechando com a simetria dos pontos cegos: a impureza favorece contínuas sobre binárias (achado 11), a permutação dilui correlacionadas. O bullet correspondente do Recap recebeu a mesma ressalva em uma linha.
**Fonte:** documentação oficial scikit-learn 1.9.1, [5.2 Permutation feature importance](https://scikit-learn.org/stable/modules/permutation_importance.html), seção *"Misleading values on strongly correlated features"*, consultada em 2026-09-21: *"When two features are correlated and one of the features is permuted, the model still has access to the latter through its correlated feature. This results in a lower reported importance value for both features, though they might actually be important."* · **Nível:** documentação normativa da biblioteca. Valores confirmados por execução.
**Confiança:** confirmado
**Também aparece em:** Recap da a06.

### 🟠 14. Os seis modelos do módulo ordenados num ranking único, misturando R² com acurácia

**claim_id:** `MLGEO-M24-A06-COMPARACAO-METRICAS-009`
**Tipo:** confusão de escopo
**Onde:** a06 · fecho da seção "Estudo de caso 2" (e o metadado `-RESUMO-SEIS-MODELOS-006`)
**Está escrito:** "entre os seis modelos treinados neste módulo (regressão linear, floresta de regressão, regressão logística, floresta de classificação, MLP de classificação, MLP de regressão), o de maior capacidade nominal (a rede de regressão, com 257 parâmetros) produziu **o pior resultado de todos**"
**Problema:** não existe a operação que a frase pressupõe. Os três modelos de regressão são avaliados por R²/MAE e os três de classificação por acurácia/F1; não há transformação que ponha as duas famílias na mesma escala, e "o MLP de regressão (R² = −0,12) foi pior que o MLP de classificação (acurácia = 0,867)" não é uma comparação com significado. O problema é agravado pelo contexto: a frase é a **conclusão** do resultado pedagógico mais forte do módulo, e uma conclusão apoiada numa comparação indefinida é frágil justamente onde precisa ser sólida — sobretudo porque a versão correta é igualmente contundente e não custa nada.
**Correção aplicada:** o recorte foi restringido para "o pior resultado **entre os três modelos de regressão** — e o único R² negativo de todo o módulo", com um parêntese acrescentado explicando por que os seis não são ordenáveis num ranking único. O metadado `-RESUMO-SEIS-MODELOS-006` recebeu a mesma correção, porque repetia a formulação antiga.
**Fonte:** consequência direta das definições formalizadas na Aula 05 do próprio módulo (R² compara o erro do modelo com o de prever a média de um alvo contínuo; acurácia é fração de acertos de classe) — as duas medem grandezas diferentes de objetos diferentes.
**Confiança:** confirmado
**Também aparece em:** bloco de metadados da a06 (`-RESUMO-SEIS-MODELOS-006`), corrigido. O Recap da a06 **não** precisou de correção: lá a comparação já estava restrita à regressão.

### 🟠 15. O exemplo trabalhado da Aula 03 anuncia uma comparação lado a lado e não a entrega

**claim_id:** `MLGEO-M24-A03-EXEMPLO-RF-PREVISOES-010`
**Tipo:** inconsistência interna
**Onde:** a03 · Exemplo trabalhado
**Está escrito:** enunciado: "**compare, lado a lado, a previsão da regressão linear e da floresta aleatória** (regressão de `Au_ppb`) para as três primeiras amostras do conjunto de teste"; e, na resolução: "**Previsões da floresta aleatória:** conferidas separadamente pelo código da aula."
**Problema:** o exemplo pede explicitamente uma comparação entre dois modelos, apresenta os números de um só e despacha o outro com uma remissão vaga a "o código da aula" — que, de fato, imprime as métricas agregadas da floresta, não as três previsões individuais pedidas. O aluno não tem como fazer o que o enunciado manda com o que a aula dá, e a metade faltante é justamente a que fecharia o raciocínio.
**Correção aplicada:** as previsões da floresta para as três amostras foram obtidas por execução (**7,65; 5,75; 21,18 ppb**) e inseridas no lugar da remissão, seguidas de um parágrafo novo com a aritmética dos erros (0,22; 13,51; 11,29 → MAE 8,34 ppb) e do fato que o cálculo revela: **nestas três amostras a floresta sai melhor** que a regressão linear (8,34 contra 9,08), o **inverso** do que vale nas 15 amostras completas (5,778 contra 5,128). A ordem entre dois modelos se inverte ao trocar a base de comparação de 15 amostras para 3 — o que **reforça** a moral que o exemplo já tinha ("uma métrica sobre poucas amostras é instável"), agora com evidência em vez de asserção.
**Fonte:** execução direta do `RandomForestRegressor(n_estimators=300, random_state=42)` da aula sobre a mesma partição (scikit-learn 1.9.1): `rf.predict(X_test)[:3]` = [7.65, 5.75, 21.18]; aritmética conferida à mão.
**Confiança:** confirmado (por execução)
**Também aparece em:** nenhum outro arquivo.

### 🟡 16. Par de instrumentos gráficos atribuído ao Módulo 20, Aula 01, que aquela aula não usa

**claim_id:** `MLGEO-M24-A02-ATRIBUICAO-M20-GRAFICOS-008`
**Tipo:** atribuição interna errada
**Onde:** a02 · seção "4. Análise exploratória: descrever antes de modelar"
**Está escrito:** "o mesmo par de instrumentos gráficos (histograma para distribuição, dispersão para relação entre duas variáveis) já **used** no Módulo 20, Aula 01, para descrever dados de furo de sondagem antes da geoestatística"
**Problema:** o Módulo 20, Aula 01, usa **histograma e boxplot** — é o título da própria seção lá ("Histograma, boxplot e o problema dos valores extremos"). **Gráfico de dispersão não aparece naquela aula**: a relação entre duas variáveis é tratada algebricamente, por coeficiente de correlação de Pearson e reta de regressão linear simples, e a palavra "dispersão" ocorre lá apenas no sentido estatístico de espalhamento ("medidas de dispersão"), nunca como gráfico. O aluno que voltar ao Módulo 20 para rever o gráfico de dispersão não o encontra, e o efeito colateral é pior que a imprecisão: ele fica sem saber se perdeu algo ou se o material está errado. (No mesmo trecho havia o anglicismo "used" por "usado".)
**Correção aplicada:** o trecho foi reescrito para creditar ao Módulo 20 o que é dele — o **histograma**, ao lado do boxplot — e declarar que o **gráfico de dispersão é novo aqui**, lembrando que lá a relação entre duas variáveis entrava por via algébrica. O anglicismo foi corrigido na mesma edição.
**Fonte:** verificação direta contra o arquivo do próprio curso `20-geoestatistica/20-geoestatistica-aula-01-preparacao-dados-estatistica-descritiva.md`, em 2026-09-21 (busca textual por "dispersão"/"scatter"/"diagrama" no arquivo inteiro).
**Confiança:** confirmado
**Também aparece em:** nenhum outro arquivo do Módulo 24 repete a atribuição. As demais remissões ao Módulo 20 (Pearson na a02, regressão simples na a03, BLUE e *leave-one-out* na a03/a05, estacionariedade e domínios na a04) foram todas verificadas contra os arquivos e **estão corretas** — itens azuis B33 a B37.

### 🟡 17. Desvio-padrão citado sem dizer a convenção, e a reprodução com pandas dá outro número

**claim_id:** `MLGEO-M24-A03-DDOF-DESVIO-011`
**Tipo:** omissão que gera erro (reprodutibilidade)
**Onde:** a03 · seção "Regressão: prever um número contínuo", parágrafo "Como (não) ler estes coeficientes"
**Está escrito:** "porque o arsênio varia numa faixa 43 vezes mais estreita (desvio-padrão de **7,7 ppm** no treino, contra **330,5 ppm** do cobre)" — e, no parágrafo seguinte, que multiplicar cada coeficiente pelo desvio-padrão da sua variável "**equivale** a reajustar o modelo sobre variáveis padronizadas (`StandardScaler`)"
**Problema:** os dois números são os desvios **populacionais** (divisor $n$, `ddof=0`), que é a convenção do `StandardScaler` — e é por isso que a equivalência afirmada é exata. Mas a aula não diz isso, e o leitor que fizer o caminho natural (`X_train.std()` no pandas, cujo padrão é o divisor $n-1$) obtém **7,83** e **334,28**, e efeitos padronizados 1,1% maiores (Zn 7,133; Cu 6,739; As 5,386; litologia 1,020; cota −0,592; dist 0,587) que **não** coincidem mais com o ajuste sobre `StandardScaler`. Diante de números que não fecham, a conclusão provável do aluno é que o material está errado — quando o material está certo e a convenção é que estava implícita.
**Correção aplicada:** o parêntese foi ampliado para declarar que os desvios são populacionais (divisor $n$, convenção do `StandardScaler`), registrar os valores que o `pandas.std()` devolve (7,8 e 334,3) e dizer que a equivalência do parágrafo seguinte só é exata na convenção populacional.
**Fonte:** documentação oficial scikit-learn (`StandardScaler`, variância populacional) e pandas (`DataFrame.std`, parâmetro `ddof`, padrão 1), versões 1.9.1 e 3.0.3; ambos os conjuntos de valores confirmados por execução em 2026-09-21.
**Confiança:** confirmado (por execução)
**Também aparece em:** nenhum outro arquivo.

### 🟡 18. Propagação faltante do achado 8 da passagem 1: o cabeçalho da Aula 03 e o hub continuavam com a expressão removida

**claim_id:** `MLGEO-M24-A03-KRIGAGEM-REGRESSAO-006` (o mesmo da passagem 1 — este achado é a propagação faltante daquele, não um fato novo)
**Tipo:** propagação faltante
**Onde:** a03 · linha "Ao final você vai conseguir" · e hub do módulo, item 3 da lista de aulas
**Está escrito:** a03, cabeçalho: "explicar por que a krigagem ordinária é, formalmente, um caso particular de **regressão linear generalizada**"; hub: "e a krigagem (Módulo 20) como caso particular de **regressão linear generalizada**"
**Problema:** o achado 8 da passagem 1 existiu **precisamente para remover essa expressão**, por ser ambígua entre mínimos quadrados generalizados (GLS, a família a que a krigagem pertence) e modelo linear generalizado (GLM, a família da regressão logística ensinada na mesma aula) — e o próprio metadado registra que "a expressão ambígua 'regressão linear generalizada' foi removida do texto". Ela foi removida do **corpo** e ficou no **cabeçalho da mesma aula** e no **hub do módulo**, que são justamente os dois lugares que o aluno lê primeiro e que uma futura geração de flashcards varreria. Uma correção que não alcança o cabeçalho do próprio arquivo não está aplicada.
**Correção aplicada:** cabeçalho da a03 reescrito para "pertence, formalmente, à família dos mínimos quadrados generalizados (GLS) — e por que isso não é a mesma coisa que modelo linear generalizado (GLM)"; item 3 do hub reescrito para "como membro da família dos mínimos quadrados generalizados (GLS, não confundir com GLM)".
**Fonte:** Cressie, N., *Statistics for Spatial Data*, ed. revisada (1993), Wiley, cap. 3 (krigagem como problema de mínimos quadrados generalizados) — a mesma fonte do achado 8; e verificação por busca textual em todos os `.md` do curso.
**Confiança:** confirmado
**Também aparece em:** `course-state.yaml`, no registro datado de `decisions` de 2026-09-20, que repete a expressão antiga. **Deliberadamente não alterado:** aquele bloco é um registro histórico do que foi decidido naquela data, e reescrevê-lo apagaria o histórico em vez de corrigi-lo. Nenhum outro arquivo do curso contém a expressão.

---

## Por que nenhum 🔵 (sem fonte) e nenhum ⚪ (controverso)

Não é omissão, e vale justificar, porque um módulo de auditoria sem nenhum achado dessas duas cores costuma indicar auditoria rasa.

**Nenhum 🔵 (sem fonte / não verificável):** toda alegação deste módulo é de uma de três naturezas, e as três são verificáveis até o fim. (i) **Saída de código** — verificável por execução, e foram 22 blocos executados; não há como uma dessas ficar "não confirmada". (ii) **Definição ou propriedade matemática** (MAE ≤ RMSE, R² negativo, inércia = $n \times p$ sob padronização, LOO como caso extremo de k-fold, colapso algébrico de camadas lineares sem ativação) — demonstrável, não dependente de fonte empírica. (iii) **Comportamento documentado de biblioteca** (padrão booleano do `get_dummies`, prefixo `neg_` do `scoring`, viés da importância por impureza, diluição da permutação, `ConvergenceWarning`) — a documentação da versão exata está disponível e foi consultada. Nenhuma alegação do módulo é uma afirmação empírica sobre o mundo geológico que dependesse de dado de campo não publicado. O conjunto de dados, sendo **declaradamente sintético**, não sustenta nem pede alegação empírica sobre depósitos reais — e a aula é explícita nisso, o que é a razão pela qual nenhuma das interpretações geoquímicas do módulo precisou ser auditada como fato de campo.

**Nenhum ⚪ (controverso):** o módulo é introdutório e opera inteiramente sobre consenso metodológico de aprendizado de máquina. As duas afirmações que **poderiam** ser controversas foram examinadas e não são. (i) A posição de CNN frente a ViT (a01) é genuinamente movente, e é por isso que a passagem 1 a reescreveu (achado 9); a formulação atual — ViT liderando referenciais de larga escala, CNN mantendo vantagem em conjunto pequeno — é a leitura padrão e não atribui consenso a um lado. (ii) "Domínios de estimativa são definidos predominantemente por critério geológico, com verificação estatística secundária" (a04) é uma afirmação sobre **prática profissional** que poderia ser disputada; ela está ancorada em Rossi & Deutsch (2014) cap. 4 e é **consistente com o que os Módulos 21 e 22 deste curso já estabeleceram e auditaram** a partir da mesma fonte, e a aula a apresenta como ênfase relativa ("predominantemente", "secundariamente"), não como regra absoluta — o que a mantém do lado correto da linha.

---

## Verificado e correto (itens azuis)

### Saídas de código executadas — 22 blocos, nenhuma divergência

| # | Aula | O que foi verificado por execução |
|---|---|---|
| B1 | a02 | Geração do conjunto: `df.shape` = (60, 9); 3 ausentes em `As_ppm` (índices 5, 22, 41) e zero nas demais |
| B2 | a02 | `dtypes` e `isna().sum()` conforme o texto (colunas de texto como `str` no pandas 3.0) |
| B3 | a02 | Mediana de `As_ppm` = **7,82** ppm; 0 ausentes após `fillna` |
| B4 | a02 | `get_dummies` devolve `litologia_xisto` booleana, `False/False/False` nas três primeiras linhas (achado 3 da passagem 1, confirmado) |
| B5 | a02 | `describe()`: Cu de 5,0 a 1.202,4 (média 365,37, mediana 271,05); Au de 0,1 a 73,48 (média 20,82); `anomalo` média 0,65 |
| B6 | a02 | Matriz de correlação: Cu–Zn 0,95; Cu–dist −0,90; Zn–dist −0,85; Au–Cu/As/Zn 0,89/0,85/0,89; **todos os \|r\| de `cota_m` ≤ 0,10** (máximo 0,10 com Cu) |
| B7 | a02 | `train_test_split` estratificado: (45, 6) e (15, 6); treino 29/16; teste 10/5; total 39/21 |
| B8 | a02 | Partição de regressão: médias 18,74 (treino) e 27,06 (teste); razão 27,06/18,74 = **1,4436** ("cerca de 45% mais alta") |
| B9 | a03 | Regressão linear: seis coeficientes e intercepto dígito a dígito; MAE 5,128; RMSE 6,759; R² 0,7879 |
| B10 | a03 | Razão 0,6881/0,0202 = 34,1 ("34 vezes") e 330,55/7,74 = 42,7 ("43 vezes") |
| B11 | a03 | Efeitos padronizados (`ddof=0`): Zn 7,053; Cu 6,664; As 5,326; litologia 1,009; cota −0,585; dist 0,581 — e identidade exata com `LinearRegression` sobre `StandardScaler().fit_transform` |
| B12 | a03 | Floresta de regressão: MAE 5,778; RMSE 7,582; R² 0,7331; as seis importâncias dígito a dígito |
| B13 | a03 | Logística: acurácia 0,867 e matriz `[[4,1],[1,9]]`; floresta: 0,933 e `[[5,0],[1,9]]`; seis importâncias da floresta classificadora |
| B14 | a03 | Exemplo trabalhado: `y_test`[:3] = 7,87 / 19,26 / 9,89 e previsões lineares 5,28 / 8,86 / 24,15; erros 2,59 / 10,40 / 14,26; MAE 27,25/3 = 9,08 |
| B15 | a04 | Padronização: média `[-0., -0., -0.]` e desvio `[1., 1., 1.]` (o `-0.` é artefato de ponto flutuante, como o texto diz) |
| B16 | a04 | K-means $k=2$: inércia 55,75; grupos 45 e 15; médias por grupo (208,6/6,2/107,2 e 835,6/19,6/346,1) |
| B17 | a04 | Cotovelo: `[180.0, 55.75, 31.9, 22.38, 18.28, 16.35]`; quedas 69,03% → 42,78% → 29,84% ("69%, 43%, 30%") |
| B18 | a04 | `crosstab`: cluster 0 = 20/25 e cluster 1 = 1/14 |
| B19 | a04 | PCA: variância explicada 0,9203 / 0,0663 / 0,0133 (soma 1,0); acumulada 0,9867; *loadings* do PC1 e PC2 dígito a dígito |
| B20 | a04 | Projeção: 2 primeiras amostras em (−1,271; 0,224) e (−1,708; −0,102) — **e a leitura de que são de baixo teor se confirma**: S01 (Cu 174,1; As 5,35; Zn 40,2) e S02 (Cu 80,5; As 1,84; Zn 42,1) contra médias de 365,4 / 9,5 / 167,0 |
| B21 | a05 | Árvores: 0,911/0,933 em `max_depth` 1 e 2; **1,000/0,533 idênticos** em 3, 5 e `None`; *gap* de 0,467 |
| B22 | a05 | `classification_report`: classe 1 com 0,900/0,900/0,900 e suporte 10; classe 0 com 0,800/0,800/0,800 e suporte 5; acurácia 0,867 |
| B23 | a05 | Validação cruzada de acurácia: `[0.917, 0.917, 0.833, 0.833, 0.833]`, média 0,867, desvio 0,041 — **e os 0,933 da divisão única ficam a 1,62 desvios acima da média**, confirmando o "cerca de 1,6" do metadado |
| B24 | a05 | Validação cruzada de MAE: 6,235 / 6,947 / 7,215 / 6,304 / 7,527; média 6,846 |
| B25 | a06 | MLP sem padronização 0,333 contra 0,867 com padronização; linha de base da classe majoritária 10/15 = 0,667 |
| B26 | a06 | Floresta 0,933 contra MLP 0,867; acurácia de treino do MLP 1,000 (*gap* 0,133) |
| B27 | a06 | Contagem de parâmetros: **65** ($6\times8+8+8+1$) somando `coefs_` e `intercepts_`; e **257** ($6\times16+16+16\times8+8+8+1$) na rede de regressão; 257/45 = 5,7 ("mais de 5 por amostra") |
| B28 | a06 | MLP de regressão: R² treino 0,9991; R² teste **−0,1208**; MAE teste 12,716 — contra R² 0,7879 da linear na mesma tarefa |
| B29 | a06 | Importância por permutação: Cu 0,216; litologia 0,104; As 0,067; Zn 0,047; cota 0,027; dist −0,002 |
| B30 | todas | **Os 22 blocos das seis aulas executam na sequência declarada, sem nenhuma falha, depois da correção do achado 10** |

### Conceitos e definições verificados contra fonte

| # | Aula | O que foi verificado | Fonte |
|---|---|---|---|
| B31 | a01 | Inclusão estrita IA ⊃ ML ⊃ DL; ML como inferência da regra a partir de dados contra sistema especialista de regras fixas | Goodfellow et al. (2016) cap. 1; Géron (2022) cap. 1 |
| B32 | a01/a05 | Taxonomia supervisionado / não supervisionado / por reforço / semi-supervisionado pelo critério da presença de rótulo; acurácia enganosa sob desbalanceamento | Géron (2022) caps. 1 e 3; ESL 2ª ed. caps. 1 e 14 |
| B33 | a02/a03 | Coeficiente de Pearson e regressão linear simples **estão** no Módulo 20, Aula 01, e a extensão para múltiplas variáveis é legítima | arquivo do próprio curso, verificado |
| B34 | a03/a05 | Krigagem como BLUE e validação cruzada *leave-one-out* **estão** no Módulo 20, Aula 05, nos termos em que o Módulo 24 as invoca | arquivo do próprio curso, verificado |
| B35 | a04 | "O Módulo 20 não tratou explicitamente de agrupamento" — **verdadeiro**: nenhuma das cinco aulas de lá usa agrupamento (a única ocorrência de "agrupamento" é sobre setorização de vizinhança) | arquivo do próprio curso, verificado |
| B36 | a04 | A exigência de estacionariedade dentro do domínio **está** no Módulo 20, Aula 02, como a aula afirma | arquivo do próprio curso, verificado |
| B37 | a02 | O hábito de "prever o resultado antes de rodar" **está** no Módulo 23, Aula 01, e é lá declarado como "o hábito que as aulas seguintes vão cobrar" — atribuição correta | arquivo do próprio curso, verificado |
| B38 | a03 | Krigagem ordinária pertence à família dos mínimos quadrados generalizados (GLS), com a estrutura de covariância dada pelo variograma; e GLS ≠ GLM | Cressie (1993) cap. 3 |
| B39 | a03 | Dupla aleatorização da floresta (*bootstrap* de linhas + subconjunto de variáveis por divisão) reduzindo variância; permutação como origem do método de importância | Breiman (2001), *Machine Learning* 45(1), 5-32 |
| B40 | a04 | K-means: dois passos até convergência, minimizando inércia; método do cotovelo; PCA com componentes ortogonais ordenados por variância e *loadings* | ESL 2ª ed. §14.3.6; Jolliffe (2002) 2ª ed. |
| B41 | a04 | Domínios de estimativa definidos por critério geológico, com verificação estatística secundária — **e coerência com os Módulos 21 e 22 deste curso**, que citam o mesmo cap. 4 da mesma fonte para "domínios rígidos e suaves" | Rossi & Deutsch (2014) cap. 4; arquivos do próprio curso |

### Bibliografia conferida referência por referência

Todas as referências citadas pelas seis aulas foram verificadas quanto a autor, ano, veículo, volume, fascículo, páginas e DOI. **Nenhuma está errada** — este é o primeiro módulo computacional do curso em que a bibliografia passa inteira, contra 3 achados amarelos bibliográficos no Módulo 22:

- **Bergen, Johnson, de Hoop & Beroza (2019)**, *Science* **363**(6433), eaau0323, DOI 10.1126/science.aau0323 — confere, inclusive o fascículo e o número de artigo.
- **Roberts et al. (2017)**, *Ecography* **40**(8), **913-929**, DOI 10.1111/ecog.02881 — confere exatamente, páginas incluídas.
- **McKinney (2010)**, *Proc. 9th Python in Science Conference*, **56-61**, DOI 10.25080/Majora-92bf1922-00a — **confere, e a checagem importou**: circulam duas paginações para este artigo (51-56 e 56-61), e a citação oficial da própria pandas é **56-61**, a que a aula usa. Não havia achado aqui, e "corrigir" para 51-56 teria introduzido um erro.
- **Breiman (2001)**, *Machine Learning* **45**(1), 5-32, DOI 10.1023/A:1010933404324 — confere.
- **Dosovitskiy et al. (2021)**, ICLR, arXiv:2010.11929 — confere.
- **Hastie, Tibshirani & Friedman**, ESL 2ª ed. (2009): **§9.6 = Missing Data** (citada na a02 para imputação) e **§14.3.6 = K-means** (citada na a04) — as duas confirmadas; §7.10 (validação cruzada), §2.9 e §7.2-7.3 (viés-variância), caps. 3, 4, 11 e 15 coerentes com o conteúdo citado.
- **Goodfellow, Bengio & Courville (2016)**, caps. 6 e 6.5 (retropropagação); **Géron (2022)** 3ª ed., caps. 1, 2, 3, 4, 9, 10-11; **Jolliffe (2002)** 2ª ed.; **Cressie (1993)** ed. revisada, cap. 3; **Pedregosa et al. (2011)**, *JMLR* 12, 2825-2830; **Rossi & Deutsch (2014)** cap. 4 — todos coerentes com o que lhes é atribuído.
- Documentação oficial de **pandas 3.0** e **scikit-learn 1.9** — as versões citadas existem e são as instaladas; os comportamentos atribuídos a elas foram confirmados por execução.

### Exemplos trabalhados

Os seis foram examinados. **Cinco passaram**; o da a03 recebeu a metade que faltava (achado 15). A aritmética de todos foi refeita à mão: o MAE das três amostras da a03 (27,25/3 = 9,0833), a inércia $n \times p = 60 \times 3 = 180$ da a04, a contagem 36 − 1 + 4 = 39 da a04, a acurácia 192/200 = 0,96 e a revocação 0/8 = 0 da a05, e a tabela dos seis modelos da a06 (todos os valores conferidos contra as execuções das Aulas 03, 05 e 06). O exemplo da a05 (as 200 encostas) é hipotético e internamente consistente, inclusive na observação, correta, de que a precisão da classe rara é **indefinida** (0/0) e não zero.

---

## Correções aplicadas

**Aplicadas em:** 2026-09-21

| claim_id | Sev. | Desfecho | Arquivos alterados |
|---|---|---|---|
| `MLGEO-M24-A05-NAMESPACE-CONTINUIDADE-008` | 🔴 10 | **Corrigido** | aula-05 (5 blocos de código + nota de continuidade + 2 ajustes de entorno) |
| `MLGEO-M24-A03-MDI-VIES-CARDINALIDADE-009` | 🟠 11 | **Corrigido** | aula-03 (seção da floresta de regressão, seção de classificação, Recap) |
| `MLGEO-M24-A06-CONVERGENCIA-007` | 🟠 12 | **Corrigido** | aula-06 (estudo de caso 2) |
| `MLGEO-M24-A06-PERMUTACAO-CORRELACAO-008` | 🟠 13 | **Corrigido** | aula-06 (seção de importância por permutação, Recap) |
| `MLGEO-M24-A06-COMPARACAO-METRICAS-009` | 🟠 14 | **Corrigido** | aula-06 (estudo de caso 2, metadado `-RESUMO-SEIS-MODELOS-006`) |
| `MLGEO-M24-A03-EXEMPLO-RF-PREVISOES-010` | 🟠 15 | **Corrigido** | aula-03 (Exemplo trabalhado) |
| `MLGEO-M24-A02-ATRIBUICAO-M20-GRAFICOS-008` | 🟡 16 | **Corrigido** | aula-02 (seção de análise exploratória) |
| `MLGEO-M24-A03-DDOF-DESVIO-011` | 🟡 17 | **Corrigido** | aula-03 (parágrafo "Como (não) ler estes coeficientes") |
| `MLGEO-M24-A03-KRIGAGEM-REGRESSAO-006` | 🟡 18 | **Corrigido** (propagação da passagem 1) | aula-03 (cabeçalho), hub do módulo |

**Arquivos tocados (8):** `...aula-02-...md`, `...aula-03-...md`, `...aula-05-...md`, `...aula-06-...md`, `...modulo.md`, `...auditoria.md` (este), `...auditoria.json`, `course-state.yaml`.
**Aulas não tocadas:** **a01 e a04 passaram integralmente** nesta passagem e não precisaram de nenhuma edição (as duas já haviam sido corrigidas na passagem 1, achados 9 e 2/5 respectivamente).

**Além das correções de achado, três atualizações de registro** (bookkeeping, sem conteúdo novo): (i) os 8 novos `claim_id` foram gravados nos blocos de metadados das aulas 02, 03, 05 e 06; (ii) o campo `palavras_corpo` foi recontado nas quatro aulas editadas, porque estava **desatualizado desde a passagem 1** (a a03 declarava 2.298 palavras quando já tinha ~2.560 após as correções daquela passagem); (iii) o registro do módulo no hub foi atualizado com o veredito e as contagens reais de alegações.

**Pendências:** nenhuma. Nenhum achado ficou aguardando decisão do usuário.

**Propagação externa:** **nenhuma necessária.** O módulo não tem questionário, baralho de flashcards nem glossário — nada foi gerado antes desta auditoria, o que é a ordem correta da cadeia. **Não há card já importado no Anki a corrigir à mão.**

---

## Restrições para o questionário e os flashcards

O gate está liberado, mas seis pontos deste módulo são armadilhas conhecidas e **não** devem virar questão ou card na formulação ingênua:

1. **Nunca peça para ordenar os seis modelos por desempenho** (achado 14). R² e acurácia não são comparáveis. Comparações válidas: dentro da regressão (linear > floresta > MLP) ou dentro da classificação (floresta > logística = MLP).
2. **Nunca formule um card do tipo "qual a variável mais importante?"** sem dizer **por qual método**. A resposta muda: `Zn_ppm` pelo coeficiente padronizado, `Zn_ppm`/`dist_falha_m` pela impureza da floresta de regressão, `Cu_ppm` pela impureza da floresta de classificação e pela permutação do MLP. E `dist_falha_m` vale 0,261 na floresta e −0,002 na permutação (achado 13).
3. **A inércia com $k=1$ é $n \times p = 180$, não a variância total multivariada (3)** — erro de fator 60, corrigido na passagem 1 (achado 2). Um card que diga "a inércia com k=1 é a variância total" está errado.
4. **As 39 amostras anômalas não vêm do limiar sozinho:** 36 do limiar de Cu > 180 ppm, mais 4 e menos 1 pelo ruído de rótulo de 12% (achado 5 da passagem 1). Questão sobre a contagem precisa distinguir limiar (36) de rótulo (39).
5. **Krigagem é GLS, não GLM** (achados 8 e 18). Um distrator com "modelo linear generalizado" é legítimo e bom; a alternativa correta é mínimos quadrados generalizados.
6. **`get_dummies` devolve booleano** no pandas 3.0 (achado 3 da passagem 1). Não formule card cuja resposta seja "1 e 0" na tela.

E um ponto de conteúdo, não de armadilha: o resultado mais forte do módulo para avaliação é o **R² negativo em teste** da rede de regressão contra R² 0,9991 em treino, com 257 parâmetros para 45 amostras. É o único caso do curso em que um modelo fica pior do que prever a média, e o objetivo de aprendizagem `oa04` depende dele.

---

## Observações fora do escopo da auditoria

Três coisas saltaram aos olhos e **não** são achados factuais — ficam registradas para quem cuida delas:

1. **Para a revisão didática (bloqueante para a decisão de divisão):** as correções desta passagem, somadas às da passagem 1, deixaram **duas aulas acima do teto de 30 minutos** pela métrica de ~84 palavras/min usada nos Módulos 22 e 23. Recontagem do corpo das seis aulas: a01 2.106 (~25 min), a02 2.299 (~27), **a03 2.891 (~34)**, a04 2.267 (~27), a05 2.463 (~29), **a06 2.622 (~31)**. A a03 é o caso claro: ela já era a aula mais carregada (regressão linear + interpretação de coeficientes + floresta + classificação + krigagem como GLS) e recebeu três das nove correções desta passagem. É o mesmo mecanismo que levou à divisão de aulas nos Módulos 22 e 23.
2. **Débito de schema pré-existente, deliberadamente não normalizado:** o bloco de metadados de **todas** as aulas do curso (verificado nos Módulos 20, 22, 23 e 24) não é YAML válido, por causa da sintaxe `"Seção A" + "Seção B"` no `mapa_objetivo_secao`. A sub-árvore `alegacoes_auditaveis` **é** válida isoladamente e foi parseada nesta auditoria para validar os 51 `claim_id`. Isso não foi corrigido: é um padrão do curso inteiro, e normalizá-lo em um módulo só criaria divergência entre módulos.
3. **A Aula 06 não tem seção "Próxima aula"**, por ser a última do módulo — coerente com os módulos anteriores, mas é item do validador estrutural, não desta auditoria.
