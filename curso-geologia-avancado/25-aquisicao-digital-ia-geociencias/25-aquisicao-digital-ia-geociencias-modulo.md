# Módulo 25 — Aquisição de dados digitais e inteligência artificial em geociências

> [!info] Área X. Métodos quantitativos e geoinformação · destino Obsidian · status: **aulas escritas, auditadas, revisadas e avaliadas** (5/5; auditoria científica aprovada, revisão didática concluída e questionário gerado; flashcards pendentes)

## Objetivo do módulo
Adquirir, organizar e integrar dados geológicos digitais de campo e de sensores e aplicar inteligência artificial ao mapeamento geológico e à prospectividade mineral.

## Pré-requisitos
[[24-machine-learning-geociencias/24-machine-learning-geociencias-modulo|Módulo 24]] e [[14-sensoriamento-remoto/14-sensoriamento-remoto-modulo|Módulo 14]]

## Objetivos de aprendizagem
- `geologia-avancado-m25-oa01` — Operar ferramentas de aquisição digital de dados em campo e avaliar suas vantagens e limitações frente à caderneta analógica
- `geologia-avancado-m25-oa02` — Organizar e integrar tipos distintos de dados geológicos (litológicos, geoquímicos, geocronológicos, geofísicos e isotópicos) numa base consistente
- `geologia-avancado-m25-oa03` — Interpretar estruturas geológicas de forma hierárquica a partir de estereoscopia digital, modelos digitais de terreno, sensoriamento remoto e aerogeofísica
- `geologia-avancado-m25-oa04` — Avaliar aplicações de Big Data e inteligência artificial ao mapeamento geológico, à exploração mineral e a modelos metalogenéticos

## Aulas (5/5 escritas)
1. [[25-aquisicao-digital-ia-geociencias-aula-01-aquisicao-digital-campo-ferramentas-imagens-croquis|Aula 01 — Aquisição digital de dados em campo: ferramentas, sensores do celular, imagens e croquis]]: fluxo escritório-campo-banco, acelerômetro e magnetômetro, declinação magnética, média vetorial de leituras repetidas, vantagens e limitações frente à caderneta analógica
2. [[25-aquisicao-digital-ia-geociencias-aula-02-tipos-organizacao-dados-geologicos|Aula 02 — Tipos e organização de dados geológicos]]: sete famílias de dados e suas unidades de observação, valores censurados, datum e EPSG, formato longo e junção por identificador
3. [[25-aquisicao-digital-ia-geociencias-aula-03-estereoscopia-digital-interpretacao-estrutural-integrada|Aula 03 — Estereoscopia digital por anaglifos e interpretação estrutural integrada]]: paralaxe e exagero vertical, viés de iluminação, interpretação em quatro níveis hierárquicos, problema dos três pontos, média de dados axiais
4. [[25-aquisicao-digital-ia-geociencias-aula-04-bancos-dados-big-data-fair-reprodutibilidade|Aula 04 — Bancos de dados e Big Data em geociências]]: modelagem relacional e integridade, padrões e dados abertos, princípios FAIR, reprodutibilidade
5. [[25-aquisicao-digital-ia-geociencias-aula-05-ia-aplicada-mapeamento-prospectividade-metalogenese|Aula 05 — Inteligência artificial aplicada]]: mapeamento preditivo e prospectividade, sistema mineralizador, qualidade do rótulo, pesos de evidência, validação espacial por blocos

> [!note] As aulas somam **~135 min** (25,3 a 29,1 min cada, sem divisão em partes — nenhuma acima do teto de 30 min, e a revisão didática decidiu **não dividir** nenhuma, com a contagem registrada no relatório). Os exemplos numéricos e todos os blocos de código foram executados — e reexecutados na auditoria, sem nenhuma saída errada. As referências bibliográficas, citadas de memória na redação, foram **todas conferidas em fonte primária** na auditoria; as marcas de `INCERTEZA DECLARADA` estão retiradas.

## Pontos de dificuldade
A aquisição digital não elimina o erro do observador: apenas o propaga mais rápido e com aparência de precisão, e um mergulho medido errado no celular vira dado confiável no banco. A qualidade do rótulo limita qualquer modelo de IA, porque um mapa geológico desatualizado usado como treino ensina o algoritmo a reproduzir o erro em escala.

## Questionário

**Questionário único cumulativo, sem parciais** — gerado em 2026-09-21: [[25-aquisicao-digital-ia-geociencias-questionario|Questionário do Módulo 25]] (15 questões, gabarito comentado e oculto).

## Registro do módulo
- Redação das aulas: concluída em 2026-09-21 (34 alegações auditáveis com claim_id `DIGGEO-M25-A0x-*`)
- Auditoria científica: **concluída em 2026-09-21**, em duas passagens — veredito **aprovado**. 13 achados numerados (1 vermelho, 7 laranjas, 3 amarelos, 1 perdido na passagem interrompida), **todos os identificáveis corrigidos, 0 em aberto**; 17 verificações bem-sucedidas; 43 alegações rastreadas. Relatório: [[25-aquisicao-digital-ia-geociencias-auditoria|Auditoria científica]] (mais o manifesto `.json`).
- Revisão didática: **concluída em 2026-09-21** — veredito **bem ensinado com ressalvas**. 0 achados vermelhos; 3 laranjas, 5 amarelos e 2 sugestões, **todos os 8 achados corrigidos**. Decisão registrada: **nenhuma aula dividida** (a mais longa, a Aula 03, tem ~29,1 min contra o teto de 30). Relatório: [[25-aquisicao-digital-ia-geociencias-revisao-didatica|Revisão didática]].
- Questionário: **concluído em 2026-09-21** — um questionário único cumulativo (5 aulas, abaixo do limiar de ~5-6 que pede parciais; mesmo formato do Módulo 22), 15 questões, cobrindo os quatro objetivos de aprendizagem, com duas questões de integração entre aulas não contíguas (`oa02`: Aula 02 × Aula 04; `oa02`/`oa04`: Aula 02 × Aula 05). Gabarito comentado em toggle: [[25-aquisicao-digital-ia-geociencias-questionario|Questionário]].
- Flashcards: pendente

## Navegação
Índice: [[_curso|Voltar ao curso]]
