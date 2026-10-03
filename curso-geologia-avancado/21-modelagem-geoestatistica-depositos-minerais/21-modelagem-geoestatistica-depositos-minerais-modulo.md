# Módulo 21 — Modelagem geoestatística de depósitos minerais

> [!info] Área X. Métodos quantitativos e geoinformação · destino Obsidian · status: **concluído** (6/6 aulas escritas; auditoria científica **aprovada**, revisão didática **concluída**, questionário **gerado** 19 questões, flashcards **gerados** 30 cards)

## Objetivo do módulo
Construir o modelo geológico e geoestatístico tridimensional de um depósito mineral com geoestatística não paramétrica e não linear, para avaliação de recursos.

## Pré-requisitos
[[20-geoestatistica/20-geoestatistica-modulo|Módulo 20]]

## Objetivos de aprendizagem
- `geologia-avancado-m21-oa01` — Consolidar e validar bases de dados de mineração e montar modelos de blocos
- `geologia-avancado-m21-oa02` — Transformar variáveis contínuas em indicadoras e modelar seus variogramas, distinguindo modelos autorizados de não autorizados
- `geologia-avancado-m21-oa03` — Aplicar e interpretar a krigagem de variáveis indicadoras e a krigagem log-normal de dados transformados
- `geologia-avancado-m21-oa04` — Construir modelos em wireframe a partir de perfis de furos de sonda e integrá-los aos modelos estimados por operações lógicas

## Aulas (6/6 escritas)
1. [[21-modelagem-geoestatistica-depositos-minerais-aula-01-consolidacao-validacao-bases-dados-modelo-blocos|Aula 01 — Consolidação e validação de bases de dados de mineração; revisão do modelo de blocos e da krigagem ordinária]]
2. [[21-modelagem-geoestatistica-depositos-minerais-aula-02-geoestatistica-nao-parametrica-indicadoras|Aula 02 — Geoestatística não paramétrica: variáveis contínuas, categóricas, booleanas e indicadoras]]
3. [[21-modelagem-geoestatistica-depositos-minerais-aula-03-variograma-indicador-modelos-autorizados|Aula 03 — Variograma indicador: cálculo, modelos autorizados e escolha da abordagem]] *(Parte 1 do par indicadora)*
4. [[21-modelagem-geoestatistica-depositos-minerais-aula-04-krigagem-indicadora-relacoes-de-ordem|Aula 04 — Krigagem indicadora: sistema, interpretação e violações de relação de ordem]] *(Parte 2 do par indicadora)*
5. [[21-modelagem-geoestatistica-depositos-minerais-aula-05-geoestatistica-nao-linear-krigagem-lognormal|Aula 05 — Geoestatística não linear: dados log-normais, transformação logarítmica e krigagem log-normal]]
6. [[21-modelagem-geoestatistica-depositos-minerais-aula-06-modelagem-deposito-wireframes-delaunay|Aula 06 — Modelagem do depósito: perfis de furos, áreas de influência, triangulação de Delaunay, wireframes e integração lógica com os modelos estimados]]

_Conteúdo escrito em 2026-09-18 (etapa 1). Auditoria científica aplicada em 2026-09-18; revisão didática aplicada em 2026-09-19, quando o módulo passou de 5 para 6 aulas pela divisão da antiga Aula 03 — ver "Registro do módulo" abaixo._

## Estrutura do módulo
Duas cadeias curtas que convergem:

- **Cadeia de estimativa** — Aula 01 (dados e modelo de blocos) → Aula 02 (transformação indicadora) → Aulas 03–04 (variograma e krigagem indicadora) → Aula 05 (krigagem log-normal). Cada aula é insumo direto da seguinte.
- **Cadeia geométrica** — Aula 01 (modelo de blocos) → Aula 06 (seções, wireframes, integração lógica).

As duas convergem na Aula 06, que depende de todas as anteriores para o passo de integração: é ali que a geometria interpretada e os teores estimados viram um só modelo. As Aulas 03 e 04 são um **par indivisível** para efeito de estudo e de avaliação: a 03 modela o variograma, a 04 o usa.

## Pontos de dificuldade
A retransformação de estimativas log-normais para a escala original (Aula 05) é onde o viés entra sem aviso, porque a média do logaritmo não retorna a média dos teores — e é fácil aplicar a fórmula de krigagem simples a uma krigagem ordinária, esquecendo o termo $-\mu$.

Em krigagem de indicadoras, atenção a um par de sintomas que se parecem e apontam para lugares diferentes: **variância de krigagem negativa** é o sintoma específico de um modelo de variograma **não autorizado**; **probabilidade estimada fora de $[0,1]$** não é — ela aparece com variogramas perfeitamente autorizados, quase sempre por **pesos negativos** (efeito de tela) e vizinhança de busca pobre, e é tratada como caso particular das **violações de relação de ordem** (Aula 04). Confundir os dois manda o aluno refazer o variograma quando o que precisa examinar é a vizinhança.

## Registro do módulo
- **Auditoria científica:** concluída em 2026-09-18 — [[21-modelagem-geoestatistica-depositos-minerais-auditoria|relatório]] · veredito **aprovado, gate liberado**. 1 vermelho, 7 laranjas e 7 amarelos corrigidos; 19 azuis registrados; 1 branco tratado com as duas posições expostas. **0 vermelhos e 0 laranjas em aberto.**
- **Revisão didática:** concluída em 2026-09-19 — [[21-modelagem-geoestatistica-depositos-minerais-revisao-didatica|relatório]] · modo `review-and-fix`. A antiga Aula 03 (2.440 palavras, no teto de 30 min) foi dividida nas atuais Aulas 03 e 04; as antigas 04 e 05 foram renumeradas para 05 e 06. Nenhuma correção da auditoria foi desfeita ou diluída.
- **Questionário:** concluído em 2026-09-19 — [[21-modelagem-geoestatistica-depositos-minerais-questionario|questionário]] · único cumulativo, 19 questões (16 individuais + 3 de integração), cobrindo os quatro objetivos de aprendizagem. Respeita todas as restrições do gate de avaliação (ver "Formato do questionário — decisão final" abaixo).
- **Flashcards:** concluídos em 2026-09-19 — [[21-modelagem-geoestatistica-depositos-minerais-flashcards|baralho]] · 30 cards, CSV sem cabeçalho, pronto para Anki, respeitando todas as 10 restrições críticas do gate de avaliação.

### Formato do questionário — decisão final
**Questionário único cumulativo, sem parciais.** Decisão registrada pela auditoria científica (2026-09-18) e **confirmada pela revisão didática após a divisão da Aula 03** (2026-09-19).

O módulo tem 6 aulas, dentro do limiar de ~5–6 do plugin a partir do qual se dividem parciais, e três razões sustentam a decisão:

1. **A divisão da Aula 03 não criou um corte conceitual novo** — ela repartiu um corte que já existia dentro da aula (variograma × krigagem). Usar essa costura como fronteira de parcial seria transformar uma medida de carga cognitiva em uma fronteira de avaliação, que é coisa diferente.
2. **As Aulas 03 e 04 são um par indivisível para avaliação**, ambas servindo à cadeia indicadora (a 03 cobre `oa02`, a 04 cobre `oa03`). Separá-las num corte de parcial desfaria exatamente a unidade que a divisão didática preservou.
3. **As questões de maior valor são de integração entre aulas** — a estrutura do módulo são duas cadeias que convergem na Aula 06, e partir em parciais cortaria a convergência.

Comparação com os vizinhos: Módulo 20 (5 aulas, também após divisão didática) e Módulo 17 (6 aulas) usaram questionário único; Módulo 19 (7 aulas) usou 3 parciais + final.

> **Restrições obrigatórias herdadas da auditoria** (ver o relatório para o detalhe): não cobrar a adequação da krigagem log-normal à estimativa local com gabarito fechado; não cobrar "OIK ou SIK, qual é a melhor?" com gabarito fechado; o número de limiares (5–15) e a faixa 1/4–1/2 de tamanho de bloco são critérios, não valores a memorizar; não cobrar modelagem implícita, inversão geofísica nem simulação sequencial; terminologia do M20 obrigatória (**valor extremo de alto teor** para *high-grade outlier*; **teor de corte** reservado ao *cutoff*).

## Navegação
Próximo: [[22-modelagem-geologica-3d/22-modelagem-geologica-3d-modulo|Módulo 22 — Modelagem geológica 3D]] Índice: [[_curso|Voltar ao curso]]
