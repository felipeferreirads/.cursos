# Módulo 20 — Introdução à geoestatística

> [!info] Área X. Métodos quantitativos e geoinformação · destino Obsidian · status: **MÓDULO FECHADO** (redação 2026-09-18; auditoria científica 2026-09-18 — aprovada, gate liberado; revisão didática 2026-09-18 — Aula 02 dividida em duas; questionário 2026-09-18 — 20 questões, único cumulativo; flashcards 2026-09-18 — 45 cards)

## Objetivo do módulo
Modelar a continuidade espacial de uma variável regionalizada por variografia e estimar valores por krigagem ordinária.

## Pré-requisitos
[[13-geoprocessamento/13-geoprocessamento-modulo|Módulo 13]]

## Objetivos de aprendizagem
- `geologia-avancado-m20-oa01` — Preparar e descrever estatisticamente dados de furos de sonda, incluindo composição por bancada, distribuições, correlação e regressão
- `geologia-avancado-m20-oa02` — Explicar o conceito de variável regionalizada e a hipótese intrínseca, e o papel do suporte, da continuidade e da anisotropia
- `geologia-avancado-m20-oa03` — Calcular e modelar variogramas experimentais, interpretando alcance, patamar, efeito pepita e anisotropias
- `geologia-avancado-m20-oa04` — Estimar valores por krigagem simples e ordinária, de ponto e de bloco, e validar a estimativa por validação cruzada

## Aulas (5/5 escritas)
1. [[20-geoestatistica-aula-01-preparacao-dados-estatistica-descritiva|Aula 01 — Preparação de dados e estatística descritiva]]: composição de amostras de furos de sonda (compositing), medidas de tendência central e dispersão, histograma, boxplot e tratamento de valores extremos, correlação e regressão linear simples
2. [[20-geoestatistica-aula-02-variaveis-regionalizadas-funcao-aleatoria-estacionariedade|Aula 02 — Variáveis regionalizadas, função aleatória e estacionariedade]] (Parte 1): função aleatória e realização única, estacionariedade de segunda ordem versus hipótese intrínseca, onde está a folga entre as duas, e por que a deriva não é acomodada por nenhuma delas
3. [[20-geoestatistica-aula-03-suporte-relacao-de-krige-anisotropia|Aula 03 — Suporte, relação de Krige e anisotropia]] (Parte 2): efeito de suporte, relação de Krige como identidade exata de variâncias de dispersão, continuidade espacial, anisotropia geométrica e zonal
4. [[20-geoestatistica-aula-04-variografia-variogramas|Aula 04 — O variograma: cálculo experimental e modelagem teórica]]: variograma experimental, lags e tolerâncias, efeito pepita, patamar, alcance, modelos esférico/exponencial/gaussiano e variogramas direcionais
5. [[20-geoestatistica-aula-05-krigagem-simples-ordinaria|Aula 05 — Krigagem simples e ordinária]]: sistema de krigagem (KS e KO), vizinhança de busca, krigagem de ponto versus bloco, validação cruzada

> [!note] As Aulas 02 e 03 são **Parte 1 e Parte 2** de um par — resultado da divisão, em 2026-09-18, da antiga Aula 02 única, que a revisão didática identificou como sobrecarregada (2.505 palavras inteiramente abstratas, 16 conceitos novos). Estude-as em sequência. A divisão seguiu a convenção já usada nos Módulos 17 e 19 deste curso.

## Pontos de dificuldade
O efeito de suporte é contraintuitivo: a distribuição dos teores de blocos não é a distribuição das amostras, e ignorar isso superestima sistematicamente o minério recuperável. O efeito pepita mistura variabilidade real de pequena escala com erro de amostragem, e separar as duas parcelas exige informação que o variograma sozinho não fornece. E há um terceiro ponto, que a auditoria científica identificou como o mais escorregadio do módulo: **a hipótese intrínseca não tolera deriva** — a folga dela em relação à estacionariedade de segunda ordem é a dispensa de variância a priori finita, e não a acomodação de uma média que varia no espaço.

## Registro do módulo
- Redação das aulas: concluída em 2026-09-18 (4 aulas originais, 19 alegações auditáveis registradas nos blocos de metadados)
- **Auditoria científica: concluída em 2026-09-18** — [[20-geoestatistica-auditoria|relatório]] · veredito **aprovado, gate liberado**. 17 achados corrigíveis (1 vermelho, 8 laranjas, 8 amarelos), **todos corrigidos**; 0 em aberto. 25 alegações rastreadas (19 do autor + 6 levantadas pela auditoria); 21 verificadas e corretas. Os quatro exemplos trabalhados foram refeitos número por número.
- **Revisão didática: concluída em 2026-09-18** — [[20-geoestatistica-revisao-didatica|relatório]] · veredito **bem ensinado com ressalvas**. A Aula 02 foi **dividida em duas** (achado vermelho de sobrecarga); as demais receberam correções locais de densidade, navegação e glosa. 0 achados em aberto.
- **Questionário: concluído em 2026-09-18** — [[20-geoestatistica-questionario|questionário]] · formato **único cumulativo, sem parciais** (ver abaixo). 20 questões (múltipla escolha, V/F com justificativa, dissertativa curta, aplicação/cálculo), 3 de integração explícita entre aulas, gabarito comentado e oculto. Todas as restrições de formato da auditoria respeitadas.
- **Flashcards: concluído em 2026-09-18** — [[20-geoestatistica-flashcards|baralho]] · formato CSV compatível com Anki, sem cabeçalho (frente;verso). 45 cards cobrindo conceitos-chave das 5 aulas. Respeitadas as 10 advertências de formato do relatório de auditoria (especialmente hipótese intrínseca, comportamento na origem, viés de média, relação de Krige, raio de busca, estabilidade numérica, terminologia de outliers).

## Recomendação de formato do questionário
**Questionário único cumulativo, sem parciais.** Mesmo depois da divisão da Aula 02, o módulo tem **5 aulas**, dentro do limiar de ~5–6 do plugin abaixo do qual não se dividem parciais. Três razões reforçam:

1. **Fio condutor único e linear.** Cada aula é insumo direto da seguinte — dados → modelo de função aleatória → suporte e anisotropia → variograma → krigagem. Não há corte conceitual que não parta a cadeia ao meio.
2. **As Aulas 02 e 03 são um par indivisível** para fins de avaliação: as duas cobrem o mesmo objetivo (`oa02`), e separá-las num corte de parcial desfaria justamente a unidade que a divisão didática preservou.
3. **As questões de maior valor são de integração entre aulas** — por exemplo, cruzar a hipótese de estacionariedade (a02) com a escolha do modelo de variograma (a04) e com o raio de busca (a05). Um questionário único é o que permite cobrá-las.

Comparação com os módulos vizinhos: o M19 (7 aulas) usou 3 parciais + final; o M17 (6 aulas) usou questionário único. O M20, com 5, fica do lado do único.

## Navegação
Próximo: [[21-modelagem-geoestatistica-depositos-minerais/21-modelagem-geoestatistica-depositos-minerais-modulo|Módulo 21 — Modelagem geoestatística de depósitos minerais]] Índice: [[_curso|Voltar ao curso]]
