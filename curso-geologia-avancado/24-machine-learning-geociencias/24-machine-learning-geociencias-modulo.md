# Módulo 24 — Fundamentos e aplicações de machine learning em geociências

> [!info] Área X. Métodos quantitativos e geoinformação · destino Obsidian · status: **auditado e revisado** (7 aulas, após a divisão didática de 2026-09-21; auditoria científica e revisão didática concluídas, gate liberado; questionários gerados em 2026-09-21; flashcards pendentes)

## Objetivo do módulo
Aplicar o fluxo de trabalho de aprendizado de máquina a problemas geológicos reais, escolhendo o algoritmo, avaliando o desempenho e comunicando os resultados com suas limitações.

## Pré-requisitos
[[20-geoestatistica/20-geoestatistica-modulo|Módulo 20]]

## Objetivos de aprendizagem
- `geologia-avancado-m24-oa01` — Situar os ramos da inteligência artificial e identificar as fontes e os desafios específicos dos dados geológicos
- `geologia-avancado-m24-oa02` — Executar o fluxo de trabalho de aprendizado de máquina em Python: definição do problema, coleta, preparação, análise exploratória e particionamento dos dados
- `geologia-avancado-m24-oa03` — Selecionar e aplicar modelos supervisionados (regressão e classificação) e não supervisionados (agrupamento e redução de dimensionalidade)
- `geologia-avancado-m24-oa04` — Avaliar o desempenho de um modelo com métricas apropriadas, diagnosticar sobreajuste e interpretar e comunicar os resultados

## Aulas (7/7 escritas)
1. [[24-machine-learning-geociencias-aula-01-inteligencia-artificial-geociencias-ramos-aprendizado-dados|Aula 01 — Inteligência artificial em geociências: ramos, tipos de aprendizado, fontes e desafios dos dados geológicos]]: IA/ML/DL como campos aninhados, aprendizado supervisionado/não supervisionado/por reforço, fontes de dados geológicos digitais, autocorrelação espacial, escassez de rótulos e classes desbalanceadas
2. [[24-machine-learning-geociencias-aula-02-fluxo-trabalho-python-preparacao-exploracao-particionamento|Aula 02 — Fluxo de trabalho em Python: objetivo, coleta, preparação, análise exploratória e particionamento dos dados]]: pandas, tratamento de valores ausentes, codificação one-hot, `describe`/`corr`, `train_test_split` com estratificação e o risco de vazamento espacial
3. [[24-machine-learning-geociencias-aula-03-modelagem-supervisionada-regressao|Aula 03 — Modelagem supervisionada: regressão (Parte 1)]]: regressão linear múltipla, leitura dos coeficientes na escala certa, multicolinearidade, floresta aleatória de regressão e o viés de cardinalidade da importância por impureza, e a krigagem (Módulo 20) como membro da família dos mínimos quadrados generalizados (GLS, não confundir com GLM)
4. [[24-machine-learning-geociencias-aula-04-modelagem-supervisionada-classificacao|Aula 04 — Modelagem supervisionada: classificação (Parte 2)]]: regressão logística e função sigmoide, floresta aleatória de classificação, matriz de confusão e a leitura dos dois tipos de erro — por que aqui o modelo flexível vence, ao contrário da Parte 1
5. [[24-machine-learning-geociencias-aula-05-modelagem-nao-supervisionada-agrupamento-reducao-dimensionalidade|Aula 05 — Modelagem não supervisionada: agrupamento e redução de dimensionalidade]]: padronização, K-means e método do cotovelo, PCA e variância explicada, comparação com domínios geoestatísticos
6. [[24-machine-learning-geociencias-aula-06-avaliacao-desempenho-sobreajuste-validacao|Aula 06 — Medidas de avaliação de desempenho, sobreajuste e validação]]: MAE/RMSE/R², matriz de confusão, precisão/revocação/F1, diagnóstico de sobreajuste por profundidade de árvore, validação cruzada k-fold como generalização do *leave-one-out* de krigagem
7. [[24-machine-learning-geociencias-aula-07-deep-learning-aplicacoes-estudos-caso|Aula 07 — Deep learning e aplicações: redes neurais, estudos de caso com dados reais, interpretação e comunicação dos resultados]]: perceptron multicamadas, dois estudos de caso (classificação e regressão) com sobreajuste severo do MLP de regressão, importância por permutação, comunicação de limitações

> [!note] As sete aulas compartilham um único conjunto de dados sintético (60 amostras de geoquímica de solo, gerado com semente fixa na Aula 02 e reaberto nas Aulas 03 a 07), para que os mesmos modelos, métricas e comparações fiquem diretamente rastreáveis de uma aula para a próxima — inclusive a tabela-resumo dos seis modelos treinados no módulo, fechada na Aula 07. **As Aulas 03 e 04 são um par** (Parte 1, regressão; Parte 2, classificação) e devem ser estudadas em sequência: é a comparação entre as duas que sustenta a lição de que nenhum algoritmo é melhor em abstrato.

## Pontos de dificuldade
Dados geológicos violam a premissa de amostras independentes: amostras vizinhas são autocorrelacionadas, e um particionamento aleatório vaza informação do treino para o teste e infla a acurácia aparente (Aulas 01, 02 e 06 tratam do problema e da correção por blocagem espacial/`GroupKFold`). Classes desbalanceadas, como depósito contra não depósito, tornam a acurácia global uma métrica enganosa (Aula 06, com o exemplo do classificador de risco geotécnico com 96% de acurácia e revocação zero; a Aula 04 já prepara o terreno mostrando que a diferença de acurácia entre dois classificadores pode ser um único falso positivo). Um terceiro ponto, que emergiu na redação e não estava antecipado no planejamento original: com conjuntos de dados geológicos tipicamente pequenos, um modelo de alta capacidade (a rede neural de regressão da Aula 07, com 257 parâmetros para 45 amostras de treino) pode sobreajustar tão severamente a ponto de ter desempenho **pior do que prever a média** (R² negativo em teste) — o resultado mais dramático de todo o módulo, e um contra-exemplo direto à intuição de que "mais sofisticado é sempre melhor". Um quarto, levantado pela auditoria: **nenhuma medida de importância de variável é neutra** — a importância por impureza favorece variáveis contínuas sobre binárias (a ponto de a cota irrelevante superar a litologia real, Aulas 03 e 04), e a importância por permutação dilui variáveis correlacionadas (a ponto de a distância à falha aparecer nula, Aula 07).

## Registro do módulo
- **Redação das aulas: concluída em 2026-09-20** — 6 aulas na redação, todo o código executado e conferido (Python 3.13.2, scikit-learn 1.9.1, pandas 3.0.3, NumPy 2.5.1, Matplotlib 3.11.2). 38 alegações auditáveis registradas na redação; **hoje são 52**, todas com `claim_id` único (6 na Aula 01, 8 na Aula 02, 9 na Aula 03, 3 na Aula 04, 9 na Aula 05, 8 na Aula 06, 9 na Aula 07) — 13 levantadas pelas duas passagens de auditoria e 1 pela divisão didática.
- **Auditoria científica: concluída — 2026-09-20 (passagem 1) e 2026-09-21 (passagem 2, `audit-and-fix`, `full`). Veredito: aprovado, gate liberado** (0 vermelhos e 0 laranjas em aberto). Passagem 2: 9 achados numerados (1 vermelho, 5 laranjas, 3 amarelos), **todos corrigidos**; os 22 blocos de código foram extraídos e executados na sequência declarada, e **nenhuma saída numérica do módulo está errada**. O achado vermelho era de continuidade de código na aula de avaliação, não de conteúdo. Relatório: [[24-machine-learning-geociencias-auditoria|auditoria do módulo]].
- **Revisão didática: concluída em 2026-09-21 (`review-and-fix`). Veredito: bem ensinado com ressalvas** — 0 achados em aberto. A antiga Aula 03 (34,8 min, regressão + classificação) foi **dividida** nas atuais Aulas 03 e 04, e o módulo passou de 6 para 7 aulas, com renumeração das três últimas. Nenhuma aula acima do teto de 30 min: a faixa é de 16 a 29,9 min (~185 min no total). Relatório: [[24-machine-learning-geociencias-revisao-didatica|revisão didática do módulo]].
- **Avaliação: ✅ gerada em 2026-09-21 — 3 parciais + 1 final cumulativo, 42 questões, 100 pontos cada questionário:** [[24-machine-learning-geociencias-questionario-parcial-1|parcial 1 (a01-a02, oa01+oa02, 8 questões)]] · [[24-machine-learning-geociencias-questionario-parcial-2|parcial 2 (a03-a05, oa03, 11 questões)]] · [[24-machine-learning-geociencias-questionario-parcial-3|parcial 3 (a06-a07, oa04, 10 questões)]] · [[24-machine-learning-geociencias-questionario-final|final cumulativo (a01-a07, os quatro objetivos, 13 questões, com três questões de integração explícita)]]. Os quatro objetivos (`oa01`-`oa04`) têm questões dedicadas; nenhum ficou descoberto. As **seis restrições** da auditoria foram respeitadas: nenhum ranking único dos seis modelos (o final q37 testa o erro e exige comparar só dentro de cada tarefa); nenhuma pergunta "qual a variável mais importante" sem dizer o método (o final q39 usa a formulação sem método como o erro a criticar); inércia com k=1 sempre n×p = 180; limiar (36) distinto do rótulo (39); krigagem é GLS com GLM como distrator; nenhuma questão depende de `get_dummies` mostrar 1 e 0. A parcial 2 traz a questão de aplicação que atravessa o par a03/a04 (q15), como sugerido pela revisão didática. Somente valores já auditados; cenários hipotéticos declarados como tais no enunciado.
- Flashcards: pendente
- Fechamento formal do módulo: pendente

## Plano de avaliação (decidido e executado em 2026-09-21)
Sete aulas passam do limite de ~5–6 que justifica questionário único (os Módulos 22, com 6 aulas, recebeu um só; o 23, com 9, recebeu 3 parciais + 1 final). Aqui o corte natural é por **objetivo de aprendizagem**, e cada parcial cobre um objetivo inteiro:

| Questionário | Aulas | Objetivos | Duração coberta |
|---|---|---|---|
| Parcial 1 | 01–02 | `oa01`, `oa02` | ~53 min |
| Parcial 2 | 03–05 | `oa03` (supervisionado e não supervisionado) | ~72 min |
| Parcial 3 | 06–07 | `oa04` | ~60 min |
| Final cumulativo | 01–07 | os quatro | ~185 min |

O questionário precisa respeitar as **seis restrições** registradas em `assessment_gate.restrictions` no `course-state.yaml` e detalhadas ao fim do relatório de auditoria — em particular: não pedir para ordenar os seis modelos num ranking único (R² e acurácia não são comparáveis), e nunca perguntar "qual a variável mais importante" sem dizer por qual método.

## Navegação
Próximo: [[25-aquisicao-digital-ia-geociencias/25-aquisicao-digital-ia-geociencias-modulo|Módulo 25 — Aquisição de dados digitais e inteligência artificial em geociências]] Índice: [[_curso|Voltar ao curso]]
