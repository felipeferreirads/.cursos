# Módulo 30 — Métodos numéricos para geociências: erro, sistemas lineares, interpolação e integração

> [!info] A. Trilha de apoio (opcional): ciências para geociências · destino Obsidian · status: **concluído** (5/5 aulas · auditoria científica aprovada · revisão didática concluída · questionário final (15 Q) · flashcards (45 cards) — aula 05 candidata a divisão em 05a/05b)

## O que é este módulo

Quarto módulo da trilha de apoio, e o único que trata de **computar**, não de formular. O [[28-matematica-geociencias-modulo|Módulo 28]] ensina a matemática que o geólogo escreve no caderno — trigonometria, vetores, exponenciais, estatística descritiva. Este ensina o que acontece quando essa matemática vai para o computador: onde o erro nasce, quando um método iterativo converge, e como se resolve numericamente aquilo que não tem solução analítica fechada.

Corresponde à disciplina obrigatória **MAP0125 — Cálculo Numérico para Geociências** (60 h) da grade do IGc-USP, e foi criado em 2026-08-28 no fechamento de lacunas contra essa grade.

> [!important] Este módulo destrava um módulo do curso avançado
> O módulo 23 do curso `curso-geologia-avancado` (Introdução à modelagem numérica geodinâmica) pressupõe diferenças finitas, solução explícita e implícita e noção de erro numérico — e nenhum módulo de nenhum dos dois cursos ensinava isso. Este é o **pré-requisito de fato** daquele módulo. A dependência é entre cursos e por isso não aparece no grafo formal de pré-requisitos; ela é citada por nome, nunca por wikilink.

> [!success] Módulo 30 completo e fechado
> As 5 aulas foram escritas, auditadas e didaticamente revisadas em 2026-08-29. Questionário final gerado (15 questões). Flashcards gerados (45 cards). A revisão didática deixou um achado 🟠 em recomendação aberta (não-bloqueante): a **aula 05** tem 1.882 palavras (17,6% acima do teto do LC-02) e empacota integração numérica e EDOs — a correção certa é dividi-la em 05a e 05b, decisão do `gerador-de-curso-modular`. Questionário e flashcards já tratam integração (oa05a) e EDOs (oa05b) como blocos separados, com numeração que sobrevive a essa divisão futura. Ver Registro do módulo.

## Pré-requisitos

Módulo [[28-matematica-geociencias-modulo|28 — Matemática para geociências]]. Como os demais módulos da trilha de apoio, é **não bloqueante**: nenhum módulo de geologia deste curso o exige formalmente. Consulte-o quando for modelar, ajustar dados ou programar — ou antes do módulo 23 do curso avançado.

## Objetivos de aprendizagem

- `geologia-m30-oa01` — Identificar as fontes de erro numérico (arredondamento, truncamento, propagação) e avaliar o condicionamento de um cálculo geológico
- `geologia-m30-oa02` — Resolver sistemas de equações lineares por eliminação de Gauss e por Gauss-Seidel e diagnosticar quando o método iterativo converge
- `geologia-m30-oa03` — Localizar e calcular zeros de funções por bisseção e por Newton-Raphson com precisão pré-fixada
- `geologia-m30-oa04` — Interpolar e ajustar dados geológicos por interpolação polinomial, diferenças finitas e mínimos quadrados, reconhecendo os limites da extrapolação
- `geologia-m30-oa05` — Calcular integrais numéricas pelas regras do trapézio e de Simpson e resolver equações diferenciais ordinárias por Euler e Runge-Kutta, estimando o erro de cada método

## Aulas (5)

1. [[30-metodos-numericos-geociencias-aula-01-erro-numerico|Aula 01 — Erro numérico: ponto flutuante, arredondamento, truncamento, propagação e condicionamento]]
2. [[30-metodos-numericos-geociencias-aula-02-sistemas-lineares|Aula 02 — Sistemas de equações lineares: eliminação de Gauss, Gauss-Seidel e matrizes mal condicionadas]]
3. [[30-metodos-numericos-geociencias-aula-03-zeros-de-funcoes|Aula 03 — Zeros de funções: bisseção, Newton-Raphson e critérios de parada]]
4. [[30-metodos-numericos-geociencias-aula-04-interpolacao-e-ajuste|Aula 04 — Interpolação e ajuste: interpolação polinomial, diferenças finitas e mínimos quadrados]]
5. [[30-metodos-numericos-geociencias-aula-05-integracao-e-edos|Aula 05 — Integração numérica e equações diferenciais ordinárias: trapézio, Simpson, Euler e Runge-Kutta]]

## Fio condutor geológico

Como no Módulo 28, cada método é ancorado num caso real, para que o módulo não vire um curso de cálculo numérico genérico: propagação de erro numa idade radiométrica e numa média de análises químicas (aula 01); sistemas lineares no balanço de massa de uma mistura de fontes e na inversão de dados geofísicos (aula 02); zeros de funções no cálculo de equilíbrio químico e de profundidade de compensação (aula 03); interpolação de uma superfície topográfica ou de topo de camada a partir de furos de sonda, e ajuste de isócrona por mínimos quadrados (aula 04); integração de uma curva de subsidência e solução numérica de uma lei de decaimento ou de resfriamento (aula 05).

## Relação com o Módulo 28

Não há sobreposição: o 28 trata de **mínimos quadrados** apenas de forma implícita, ao ler uma barra de erro, e nunca formula o ajuste; a estatística descritiva do 28 é pré-requisito da aula 04 daqui, não sua repetição. Se ao gerar as aulas ficar claro que a aula 04 precisa reensinar regressão, o correto é apontar para a aula 04 do Módulo 28 e não duplicá-la.

## Pontos de dificuldade

Aceitar que o computador **não** representa 0,1 exatamente, e que somar em ordem diferente dá resultado diferente — contraintuitivo para quem confia na calculadora (aula 01). O critério de convergência de Gauss-Seidel (dominância diagonal) costuma ser decorado sem ser entendido (aula 02). Newton-Raphson diverge silenciosamente quando a derivada é pequena, e reconhecer isso é mais importante que aplicar a fórmula (aula 03). O ponto mais caro do módulo: entender que **interpolar não é ajustar** e que um polinômio de grau alto oscila entre os pontos (fenômeno de Runge) em vez de melhorar o resultado (aula 04).

## Registro do módulo

- Aulas: ✅ 5 / 5 escritas em 2026-08-29, revisadas didaticamente em 2026-08-29. Corpo real por aula: 1.570 · 1.600 · 1.599 · 1.598 · **1.882** palavras — as quatro primeiras dentro do teto de 1.600 do LC-02 e sem folga; a aula 05 acima dele, deliberadamente não podada.
- Auditoria científica: ✅ [[30-metodos-numericos-geociencias-auditoria|concluída em 2026-08-29]] — **aprovado**: 4 achados (1 🔴, 3 🟠), todos corrigidos, todos nos exemplos trabalhados; 21 alegações verificadas. 0 em aberto.
- Revisão didática: ✅ [[30-metodos-numericos-geociencias-revisao-didatica|concluída em 2026-08-29]] — **bem ensinado com ressalvas**: 0 🔴 · 3 🟠 · 5 🟡 · 1 🔵. Oito achados corrigidos nas cinco aulas, os principais deles os IDs de objetivo não canônicos (que travariam a matriz de cobertura do questionário) e o Passo 1 da aula 02, que rotulava "escalonar" um passo resolvido por substituição. **1 achado 🟠 em aberto:** a aula 05 exige divisão em 05a (integração numérica) e 05b (EDOs) — encaminhado ao `gerador-de-curso-modular`.
- Questionário: ✅ [[30-metodos-numericos-geociencias-questionario-final|final cumulativo gerado em 2026-08-29]] — 15 questões (7 múltipla escolha · 2 V/F com justificativa · 1 dissertativa curta · 5 de aplicação), gabarito comentado em toggle. Cobre os 5 objetivos: oa01 → Q1–3, oa02 → Q4–6, oa03 → Q7–8, oa04 → Q9–11, oa05 → Q12–15. **Restrição da revisão didática respeitada:** integração numérica e EDOs são blocos separados dentro de `oa05` — Q12–Q13 avaliam `oa05a` (integração; Q13 é item de aplicação próprio, regra do trapézio sobre taxa de subsidência) e Q14–Q15 avaliam `oa05b` (EDOs). A numeração 12–15 sobrevive à divisão da aula 05 em 05a/05b sem renumeração.
- Flashcards: ✅ [[30-metodos-numericos-geociencias-flashcards|baralho de repetição espaçada gerado em 2026-08-29]] — 45 cards, divididos por objetivo (oa01: 12 cards; oa02: 10 cards; oa03: 6 cards; oa04: 6 cards; oa05: 11 cards). Formatos: CSV para Anki + markdown para Notion. **Restrição da revisão didática respeitada:** integração numérica e EDOs tratadas como blocos separados dentro de oa05 (fb105–fb109 integração; fb110–fb115 EDOs), com IDs que sobrevivem à futura divisão da aula 05 em 05a/05b.

## Navegação

Módulos irmãos da trilha de apoio: [[26-quimica-geociencias-modulo|Módulo 26 — Química para geociências]] · [[27-fisica-geociencias-modulo|Módulo 27 — Física para geociências]] · [[28-matematica-geociencias-modulo|Módulo 28 — Matemática para geociências]]. Índice: [[_curso|Voltar ao curso]]
