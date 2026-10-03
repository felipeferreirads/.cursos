# Módulo 13 — Geoprocessamento

> [!info] Área X. Métodos quantitativos e geoinformação · destino Obsidian · status: **completo** (7/7 aulas escritas, auditadas e revisadas · questionários gerados · 78 flashcards gerados)

## Objetivo do módulo
Elaborar, analisar e entregar projetos cartográficos digitais em ambiente SIG, da base cartográfica à análise espacial e ao layout final, aplicados a problemas geocientíficos.

## Pré-requisitos
Nenhum dentro deste curso. Pressupõe o curso base "Geologia e Gemologia — do essencial ao avançado" concluído; essa dependência fica fora do grafo formal de pré-requisitos.

## Objetivos de aprendizagem
- `geologia-avancado-m13-oa01` — Explicar geoide, datum, sistemas de coordenadas, projeções e escala, e escolher o sistema de referência adequado a um projeto
- `geologia-avancado-m13-oa02` — Distinguir as estruturas vetorial e matricial e organizar bases de dados espaciais em ambiente SIG
- `geologia-avancado-m13-oa03` — Aplicar operações de geoprocessamento vetorial e métodos de interpolação para gerar análises espaciais e mapas de isovalores
- `geologia-avancado-m13-oa04` — Derivar variáveis morfométricas e hidrológicas de modelos digitais de elevação e entregar produtos cartográficos normatizados

## Aulas (7)
1. [[13-geoprocessamento-aula-01-fundamentos-cartograficos|Aula 01 — Fundamentos cartográficos: geoide, datum, sistemas de coordenadas, projeções e escala]] — elipsoide vs. geoide, SAD69 vs. SIRGAS2000, UTM, escolha de projeção, cálculo de escala
2. [[13-geoprocessamento-aula-02-ambiente-sig-estruturas-vetorial-e-matricial|Aula 02 — Ambiente SIG, estruturas vetorial e matricial e organização de bases de dados espaciais]] — o que é um SIG, ponto/linha/polígono vs. raster, importação de tabela de coordenadas XY, organização de base de dados espacial
3. [[13-geoprocessamento-aula-03-georreferenciamento-gps-gnss-e-aquisicao-digital-de-dados-em-campo|Aula 03 — Georreferenciamento, GPS/GNSS e aquisição digital de dados em campo]] — pontos de controle e RMSE, GPS vs. GNSS, trilateração, modos de posicionamento (autônomo, DGPS, RTK, pós-processado)
4. [[13-geoprocessamento-aula-04-geoprocessamento-vetorial-operacoes-espaciais|Aula 04 — Geoprocessamento vetorial: operações espaciais e cálculos com linhas e polígonos]] — interseção, união, diferença, buffer, dissolve, relações topológicas
5. [[13-geoprocessamento-aula-05-interpolacao-espacial-e-mapas-de-isovalores|Aula 05 — Interpolação espacial e mapas de isovalores a partir de nuvens de pontos]] — IDW, krigagem, spline, leitura de isolinhas e anomalias
6. [[13-geoprocessamento-aula-06-modelos-digitais-de-elevacao-declividade-hipsometria-hidrologia|Aula 06 — Modelos digitais de elevação: declividade, hipsometria, análise hidrológica e extração de lineamentos]] — MDT vs. MDS, declividade, curva hipsométrica, direção/acumulação de fluxo (D8), lineamentos como hipótese estrutural
7. [[13-geoprocessamento-aula-07-layout-cartografico-normatizado-e-projeto-integrado|Aula 07 — Layout cartográfico normatizado e projeto integrado de geoprocessamento]] — elementos obrigatórios de layout, paletas de cor, classificação de dados, fluxo de trabalho integrado do módulo

## Pontos de dificuldade
A tríade geoide–datum–sistema de coordenadas é onde quase todo projeto falha: sobrepor camadas em data diferentes desloca feições dezenas a centenas de metros sem que o software acuse erro nenhum (Aula 01) — o mesmo risco reaparece no georreferenciamento de mapas históricos e no posicionamento GPS/GNSS de campo (Aula 03), sempre por não declarar ou não converter o sistema de referência. A escolha do interpolador e de seus parâmetros também engana, porque todo método (IDW, krigagem, spline) produz um mapa de aparência convincente mesmo quando os dados não sustentam a superfície (Aula 05) — e o mesmo aviso, com outra roupagem, vale para lineamentos extraídos de modelo digital de elevação, que são hipótese de controle estrutural, não confirmação, até serem checados em campo (Aula 06).

## Registro do módulo
- Aulas: ✅ 7 / 7 escritas
- Auditoria científica: ✅ concluída — [[13-geoprocessamento-auditoria|relatório]] (14 achados: 2 🔴, 9 🟠, 2 🟡, 1 ⚪ — todos corrigidos; nenhum em aberto)
- Revisão didática: ✅ concluída — [[13-geoprocessamento-revisao-didatica|relatório]] (bem ensinado com ressalvas; 4 🟠 e 3 🟡 corrigidos, 2 🔵 registrados)
- Questionário: ✅ concluído — **3 parciais + 1 final cumulativo**: [[13-geoprocessamento-questionario-parcial-1|parcial 1 (a01-a03, oa01+oa02, 10 questões)]] · [[13-geoprocessamento-questionario-parcial-2|parcial 2 (a04-a05, oa03, 9 questões)]] · [[13-geoprocessamento-questionario-parcial-3|parcial 3 (a06-a07, oa04, 9 questões)]] · [[13-geoprocessamento-questionario-final|final cumulativo (todo o módulo, 10 questões)]] — 38 questões no total, 100 pontos cada questionário, cobertura: oa01 e oa02 integrais na parcial 1 + reforço no final, oa03 integral na parcial 2 + reforço no final, oa04 integral na parcial 3 + reforço no final
- Flashcards: ✅ concluído — **78 cards** (11 Basic + 67 Cloze): `13-geoprocessamento-flashcards-basic.csv` e `13-geoprocessamento-flashcards-cloze.csv`

## Navegação
Anterior: [[12-engenharia-de-petroleo/12-engenharia-de-petroleo-modulo|Módulo 12 — Engenharia de petróleo]] · Próximo: [[14-sensoriamento-remoto/14-sensoriamento-remoto-modulo|Módulo 14 — Sensoriamento remoto]] · Índice: [[_curso|Voltar ao curso]]
