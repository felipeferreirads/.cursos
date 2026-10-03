# Módulo 22 — Modelagem geológica 3D

> [!info] Área X. Métodos quantitativos e geoinformação · destino Obsidian · status: **concluído** (6/6 aulas escritas; auditoria científica e revisão didática concluídas em 2026-09-19; questionário final cumulativo gerado em 2026-09-19; flashcards gerados em 2026-09-19)

## Objetivo do módulo
Construir e criticar modelos geológicos tridimensionais que integrem dados de superfície, de subsuperfície e inversões geofísicas em exploração mineral e metalogênese.

## Pré-requisitos
[[21-modelagem-geoestatistica-depositos-minerais/21-modelagem-geoestatistica-depositos-minerais-modulo|Módulo 21]] e [[19-geofisica-exploracao-mineral/19-geofisica-exploracao-mineral-modulo|Módulo 19]]

## Objetivos de aprendizagem
- `geologia-avancado-m22-oa01` — Distinguir modelagem explícita e implícita e avaliar as vantagens, as limitações e os algoritmos de cada abordagem
- `geologia-avancado-m22-oa02` — Integrar dados de superfície 2D e de subsuperfície 3D, com atributos estruturais, geoquímicos e geofísicos, na construção de um modelo
- `geologia-avancado-m22-oa03` — Relacionar o tipo, o tamanho e a geometria de depósitos minerais à estratégia de modelagem e à interpretação metalogenética
- `geologia-avancado-m22-oa04` — Avaliar a incerteza de um modelo 3D e a coerência entre o modelo geológico e o modelo geofísico de inversão

## Aulas (6/6 escritas)
1. [[22-modelagem-geologica-3d-aula-01-definicoes-usos-vantagens-limitacoes-softwares|Aula 01 — Modelagem geológica 3D: definições, usos, vantagens e limitações; softwares comerciais e livres]]
2. [[22-modelagem-geologica-3d-aula-02-dados-algoritmos-modelagem-explicita-implicita|Aula 02 — Dados e algoritmos: integração de superfície (2D) e subsuperfície (3D); modelagem explícita versus implícita]]
3. [[22-modelagem-geologica-3d-aula-03-atributos-geologicos-geofisicos-inversao|Aula 03 — Atributos geológicos, estruturais, geoquímicos e geofísicos no modelo; modelos geofísicos de inversão e modelos geológicos]]
4. [[22-modelagem-geologica-3d-aula-04-geometrias-depositos-estrategia-modelagem|Aula 04 — Tipos, tamanhos e geometrias de depósitos minerais e a estratégia de modelagem]]
5. [[22-modelagem-geologica-3d-aula-05-modelo-3d-teste-interpretacao-metalogenetica|Aula 05 — O modelo 3D como ferramenta de teste da interpretação metalogenética]]
6. [[22-modelagem-geologica-3d-aula-06-estudos-caso-incerteza-critica-modelo|Aula 06 — Estudos de caso em exploração mineral e metalogênese; incerteza e crítica do modelo]]

_Conteúdo escrito em 2026-09-19 (etapa 1) em cinco aulas. A auditoria científica e a revisão didática de 2026-09-19 (etapa 2) dividiram a antiga Aula 04 em duas, levando o módulo a seis aulas — ver "Registro do módulo" abaixo. O questionário final cumulativo foi gerado em 2026-09-19 (etapa 3); os flashcards são a próxima etapa da cadeia._

## Estrutura do módulo
Uma progressão linear que converge na síntese final:

- **Aula 01** estabelece o vocabulário e o panorama (o que é modelagem 3D, explícito × implícito em alto nível, software).
- **Aula 02** aprofunda o algoritmo — como os dois fluxos de trabalho usam dado de superfície e de subsuperfície, com destaque para o método do campo potencial, que liga a modelagem implícita à geoestatística dos Módulos 20–21.
- **Aula 03** adiciona os atributos que povoam o modelo (estrutural, geoquímico, geofísico) e introduz a comparação entre modelo geológico e modelo geofísico de inversão.
- **Aulas 04 e 05** formam um par sobre o mesmo objetivo (`oa03`), separado em suas duas metades: a **Aula 04** liga a geometria do depósito (controlada pelo tipo genético) à escolha de estratégia de modelagem; a **Aula 05** usa o modelo já construído como **teste** da interpretação metalogenética, recuperando o paradigma de sistemas minerais do Módulo 19.
- **Aula 06** fecha o módulo com dois estudos de caso que combinam tudo, e sistematiza o vocabulário de incerteza de modelo — o contraponto crítico ao otimismo técnico das aulas anteriores.

## Pontos de dificuldade
Um modelo implícito interpola com elegância mesmo onde não existe dado nenhum, e a superfície suave esconde que a geometria ali é invenção do algoritmo. Casar um modelo geológico com um modelo de inversão geofísica exige aceitar que os dois têm resoluções e incertezas distintas: forçar a coincidência produz confiança falsa.

Dois degraus adicionais, identificados pela auditoria e pela revisão de 2026-09-19 e já tratados no texto das aulas:

- A **cokrigagem**, que sustenta o método do campo potencial da Aula 02, está declarada **fora do escopo do Módulo 20**. A Aula 02 passou a defini-la no próprio texto — não a procure nas aulas anteriores.
- A **classe genética de um depósito não determina a sua geometria** (Aula 04). O mesmo rótulo "Ni-Cu-EGP magmático" cobre corpos em pipe e corpos estratiformes, e o critério que de fato prevê a estratégia de modelagem é a natureza física do limite entre minério e encaixante.

## Questionário

**Questionário único cumulativo, sem parciais** — gerado em 2026-09-19: [[22-modelagem-geologica-3d-questionario|Questionário do Módulo 22]] (15 questões, gabarito comentado e oculto).

O critério do plugin é gerar parciais apenas acima de ~5-6 aulas. O módulo tem 6, dentro do limiar, e a divisão da antiga Aula 04 foi motivada por **carga cognitiva**, não por um corte conceitual novo — as Aulas 04 e 05 continuam servindo ao mesmo objetivo de aprendizagem (`oa03`), em duas metades. Além disso, a progressão é linear e convergente: a Aula 06 integra explicitamente tudo o que veio antes, de modo que qualquer parcial cortaria o módulo antes da síntese que é o seu ponto.

Recomendação registrada pela auditoria científica e confirmada pela revisão didática. Composição: cobertura dos quatro objetivos de aprendizagem, com três questões de integração explícita entre aulas — geometria de depósito (Aula 04) × escolha de algoritmo (Aula 02); incerteza de modelo (Aula 06) × coerência geológico-geofísica (Aula 03); e geometria/estratégia (Aula 04) × teste da interpretação metalogenética (Aula 05), já que as duas servem ao mesmo objetivo `oa03`. As **sete restrições** registradas em `assessment_gate.restrictions` do manifesto de auditoria foram lidas e respeitadas antes de escrever qualquer item (nenhum item classifica MVT como estratiforme, descreve pórfiro como equidimensional/funil invertido, atribui o zoneamento concêntrico a Sillitoe 2010, trata Ni-Cu-EGP como família única em pipe, apresenta o tratamento de falha implícita como padrão único, trata cokrigagem como pré-requisito do Módulo 20, ou dá como gabarito que os três testes metalogenéticos são igualmente fracos).

## Registro do módulo

- **Auditoria científica:** concluída em 2026-09-19 · modo `audit-and-fix` · **veredito: aprovado, gate liberado**. 13 achados numerados (1 vermelho, 5 laranjas, 7 amarelos), **todos corrigidos**; 21 registros azuis de verificação bem-sucedida; nenhum achado branco. 0 vermelhos e 0 laranjas em aberto. Relatório: [[22-modelagem-geologica-3d-auditoria|Auditoria científica do Módulo 22]] (manifesto em `22-modelagem-geologica-3d-auditoria.json`).
- **Revisão didática:** concluída em 2026-09-19 · modo `review-and-fix`. Resultado principal: **divisão da antiga Aula 04** (2.764 palavras / ~33 min depois das correções da auditoria) nas atuais Aulas 04 e 05, com a antiga Aula 05 renumerada para Aula 06. Relatório: [[22-modelagem-geologica-3d-revisao-didatica|Revisão didática do Módulo 22]].
- **Questionário:** concluído em 2026-09-19 · questionário único cumulativo · 15 questões (múltipla escolha, V/F com justificativa, dissertativa curta, aplicação/interpretação, uma aplicação numérica de ordem de grandeza), gabarito comentado e oculto. Arquivo: [[22-modelagem-geologica-3d-questionario|Questionário do Módulo 22]].
- **Flashcards:** concluído em 2026-09-19 · 56 cards · CSV sem cabeçalho (frente;verso) · formato Anki · respeitando as 7 restrições ao gerador. Arquivo: `22-modelagem-geologica-3d-flashcards.csv`.

> [!warning] Nota sobre os `claim_id`
> Os identificadores de alegação auditável **não foram renumerados** na divisão da Aula 04. O prefixo `A04` designa a numeração em que cada alegação foi emitida, não a aula em que ela hoje se encontra. As alegações `GEOMOD3D-M22-A04-*` estão distribuídas entre as Aulas 04 e 05, e as `GEOMOD3D-M22-A05-*` da auditoria original estão hoje na Aula 06.

## Navegação
Próximo: [[23-modelagem-numerica-geodinamica/23-modelagem-numerica-geodinamica-modulo|Módulo 23 — Introdução à modelagem numérica geodinâmica]] Índice: [[_curso|Voltar ao curso]]
