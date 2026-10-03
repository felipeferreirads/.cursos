# Módulo 23 — Introdução à modelagem numérica geodinâmica

> [!info] Área X. Métodos quantitativos e geoinformação · destino Obsidian · status: **concluído** (9/9 aulas escritas · auditoria científica ✅ concluída e aprovada · revisão didática ✅ concluída · questionário ✅ concluído · flashcards ✅ concluído — 87 cards)

## Auditoria científica

[[23-modelagem-numerica-geodinamica-auditoria|Relatório completo da auditoria científica]] · manifesto estruturado em `23-modelagem-numerica-geodinamica-auditoria.json`

**Veredito: APROVADO** (2026-09-19, modo `audit-and-fix`, profundidade `full`). 15 achados numerados — 1 🔴, 13 🟠, 1 🟡 — **todos corrigidos**, 0 em aberto. **Gate liberado** para questionário e flashcards, com sete restrições ao gerador registradas no relatório.

Os sete blocos de código Python do módulo foram **executados** (NumPy 2.5.1) e a saída comparada dígito a dígito com a declarada no texto: **nenhuma saída numérica do módulo está errada**. O único achado 🔴 veio da outra frente da auditoria, a verificação cruzada com o Módulo 30 do curso base: a antiga Aula 04 afirmava que κ era a letra usada para o decaimento radioativo e que decaimento e condução de calor obedecem à mesma forma de equação — as duas coisas falsas, e a segunda contradizendo a distinção EDO/EDP que a Aula 02 existe para construir. As Aulas 01 e 02 passaram pela auditoria integralmente, sem nenhuma edição.

> [!warning] A auditoria é anterior à divisão de aulas
> Ela rodou sobre as **7 aulas originais**; a revisão didática, logo depois, dividiu duas delas e o módulo passou a **9**. Os `claim_id` **não foram renumerados** — continuam com o prefixo da aula pré-divisão (`A03`, `A04`, `A05`…), deliberadamente, para não quebrar a rastreabilidade com o manifesto `.json`. O mapeamento está na seção "Divisões de aula" abaixo.

**Passagem pontual em 2026-09-20.** Escopo restrito às **cinco alegações novas** nascidas da divisão didática — os 15 achados de 2026-09-19 **não foram reabertos**. As cinco foram verificadas e nenhuma estava errada; a passagem gerou **um achado 🟠 novo (o de número 16), corrigido na mesma passagem**. Totais do módulo: **16 achados numerados (1 🔴, 14 🟠, 1 🟡), todos corrigidos, 0 em aberto; 40 itens azuis; 0 alegações não auditadas.** O gate segue liberado, agora com **oito** restrições ao gerador.

## Revisão didática

[[23-modelagem-numerica-geodinamica-revisao-didatica|Relatório completo da revisão didática]]

**Veredito: BEM ENSINADO COM RESSALVAS** (2026-09-19, modo `review-and-fix`). 9 achados — 1 🔴, 5 🟠, 2 🟡, 1 🔵 —, todos os 🔴 e 🟠 resolvidos. O 🔴 era um desalinhamento objetivo↔conteúdo: a Aula 01 prometia "produzir um gráfico de linha e um mapa de cores com Matplotlib" e não tinha uma linha de Matplotlib em nenhum dos seus dois exemplos trabalhados. Os dois 🟠 mais caros foram carga cognitiva, e levaram à divisão de duas aulas.

## Objetivo do módulo
Resolver numericamente, em Python, as equações de calor e de reologia aplicadas à litosfera e interpretar quantitativamente processos geodinâmicos.

## Pré-requisitos
Nenhum dentro deste curso. Pressupõe o curso base "Geologia — do essencial ao avançado" concluído; essa dependência fica fora do grafo formal de pré-requisitos.

> [!warning] Pré-requisito cruzado — estude antes o módulo 30 do curso base
> Este módulo pressupõe **cálculo numérico**: método das diferenças finitas, esquemas explícito e implícito, erro de truncamento e critério de estabilidade. As aulas 02 e 06 daqui partem desse ponto em vez de construí-lo. O curso base ganhou em 2026-08-28 o **módulo 30 — Métodos numéricos para geociências** (trilha de apoio, disciplina MAP0125 do IGc-USP), que é onde isso se aprende: erro de arredondamento e condicionamento, sistemas lineares, zeros de funções, interpolação por diferenças finitas, integração numérica e EDOs por Euler e Runge-Kutta.
>
> A dependência não aparece no grafo de pré-requisitos porque o grafo formal de cada curso só aceita módulos do próprio curso. Ela está declarada no `course-state.yaml` deste módulo, campo `cross_course_prerequisites`, desde 2026-08-29. Em produção: o módulo 30 do curso base tem de ser gerado antes deste.

> [!warning] Pré-requisito de ferramenta — sintaxe básica de Python
> Este é o único módulo do curso que pressupõe **saber programar minimamente**. A Aula 01 assume familiaridade com variáveis, funções e listas em Python; ela ensina NumPy e Matplotlib, não a linguagem. Se você nunca programou, faça uma introdução rápida a Python antes de começar — está fora do escopo do curso, e a Aula 01 declara isso no seu cabeçalho. Registrado aqui, e não só lá, porque é no hub que se planeja o estudo.

## Objetivos de aprendizagem
- `geologia-avancado-m23-oa01` — Programar em Python operações numéricas e gráficas com NumPy e Matplotlib aplicadas a problemas geológicos
- `geologia-avancado-m23-oa02` — Resolver equações diferenciais parciais por métodos numéricos explícitos e implícitos e explicar a equação da continuidade e a de Navier-Stokes
- `geologia-avancado-m23-oa03` — Calcular geotermas e fluxo de calor para a litosfera oceânica e continental e interpretar seus controles
- `geologia-avancado-m23-oa04` — Explicar a reologia da litosfera e aplicá-la à análise quantitativa de continentes em extensão e em colisão

## Aulas (9)
1. [[23-modelagem-numerica-geodinamica-aula-01-python-jupyter-numpy-matplotlib|Aula 01 — Python para geodinâmica computacional: Jupyter, NumPy e Matplotlib; o que é e para que serve a modelagem numérica]]
2. [[23-modelagem-numerica-geodinamica-aula-02-algebra-linear-calculo-edp-diferencas-finitas|Aula 02 — Álgebra linear, cálculo e equações diferenciais parciais: solução analítica versus numérica e o método das diferenças finitas]]
3. [[23-modelagem-numerica-geodinamica-aula-03-mecanica-continuo-continuidade-stokes|Aula 03 — Mecânica do contínuo: a equação da continuidade e a equação de Stokes]] *(Parte 1 de um par)*
4. [[23-modelagem-numerica-geodinamica-aula-04-malhas-descricoes-lagrangiana-euleriana|Aula 04 — Malhas e descrições lagrangiana e euleriana: como o contínuo vira um modelo computável]] *(Parte 2)*
5. [[23-modelagem-numerica-geodinamica-aula-05-calor-fourier-conservacao-producao-adveccao|Aula 05 — Calor: lei de Fourier, conservação de calor, produção e advecção]] *(Parte 1 de um par)*
6. [[23-modelagem-numerica-geodinamica-aula-06-solucao-numerica-calor-explicito-implicito|Aula 06 — Solução numérica da equação do calor: esquemas explícito (FTCS) e implícito (BTCS)]] *(Parte 2)*
7. [[23-modelagem-numerica-geodinamica-aula-07-calor-litosfera-oceanica-continental-geotermas|Aula 07 — Calor na litosfera oceânica e continental: resfriamento e envelhecimento, geotermas estáveis e elementos produtores de calor]]
8. [[23-modelagem-numerica-geodinamica-aula-08-reologia-rochas-viscosidade-fluencia|Aula 08 — Reologia das rochas: viscosidade efetiva, elasticidade, fluência por difusão e por deslocamento, reologia crustal e mantélica]]
9. [[23-modelagem-numerica-geodinamica-aula-09-extensao-colisao-continental-slab-pull-ridge-push|Aula 09 — Continentes em extensão e em colisão: ruptura continental, subsidência, evolução termal de orógenos, slab-pull, ridge-push e cunhas orogênicas]]

As 7 aulas originais foram escritas em 2026-09-19; a revisão didática do mesmo dia dividiu duas delas, e o módulo passou a 9. **Todas as 9 têm código Python real nos exemplos trabalhados, cada um com verificação numérica manual.** As bibliotecas usadas são **NumPy** (nas nove), **Matplotlib** (na Aula 01, acrescentado pela revisão didática) e **SciPy** (`scipy.special.erf`, apenas na Aula 07). As Aulas 02 e 06 declaram o Módulo 30 do curso base (Métodos numéricos para geociências) como pré-requisito cruzado explícito no cabeçalho, conforme a convenção do curso.

## Divisões de aula (2026-09-19)

| Aula original | Virou | Corte |
|---|---|---|
| Aula 03 — Mecânica do contínuo; malhas e descrições | **Aula 03** (continuidade e Stokes) + **Aula 04** (malhas, lagrangiano/euleriano) | física do contínuo │ representação numérica |
| Aula 04 — Calor; soluções explícita e implícita | **Aula 05** (Fourier, três termos, difusividade) + **Aula 06** (FTCS, estabilidade, BTCS) | formulação física │ solução numérica |
| Aula 05 → **Aula 07**, Aula 06 → **Aula 08**, Aula 07 → **Aula 09** | renumeração simples, sem alteração de conteúdo | — |

**Os `claim_id` não foram renumerados.** Uma alegação que nasceu na antiga Aula 03 continua com o prefixo `A03` mesmo tendo migrado para a atual Aula 04; o mesmo vale para `A04` → Aula 06, `A05` → Aula 07, `A06` → Aula 08 e `A07` → Aula 09. É deliberado: o manifesto `23-modelagem-numerica-geodinamica-auditoria.json` os referencia, e renumerar quebraria o histórico. Cada aula afetada traz a nota `nota_alegacoes_migradas` no seu bloco de metadados.

> [!success] As cinco alegações novas foram auditadas — passagem pontual de 2026-09-20
> Nasceram nas divisões e nas correções didáticas de 2026-09-19, **depois** da auditoria científica, e ficaram pendentes: `GEODIN-M23-A01-MATPLOTLIB-API-006` e `GEODIN-M23-A01-EXEMPLO-MAPA-007` (Aula 01), `GEODIN-M23-A03-MALHA-COLOCALIZADA-010` e `GEODIN-M23-A03-EXEMPLO-ESCALONADA-011` (Aula 04), `GEODIN-M23-A04-EXEMPLO-PROPRIEDADES-008` (Aula 05).
>
> **Todas as cinco foram verificadas e nenhuma estava errada** (itens azuis P2 a P6 do relatório). O Matplotlib foi **instalado (3.11.2)** e os dois blocos da Aula 01 **executados na íntegra** — era a razão operacional da pendência. O mecanismo do padrão em xadrez foi verificado contra fonte, e a **representatividade dos três parâmetros térmicos** de `EXEMPLO-PROPRIEDADES-008` foi confirmada (ρ = 2.700 kg/m³ é a densidade crustal de referência de Whittington et al. 2009; k = 2,7 W/(m·K) está no meio da faixa crustal; κ = 1 × 10⁻⁶ m²/s é o valor que os modelos térmicos de litosfera adotam).
>
> A passagem gerou **um achado 🟠 (o de número 16), já corrigido**: `Cp = 1.000 J/(kg·K)` aparecia sem ressalva num exemplo ancorado em medida de superfície, enquanto o Cp da crosta média vale ~760 J/(kg·K) a 25 °C e só passa por 1.000 perto de 220 °C. Acrescentada uma ressalva de uma cláusula; **nenhum valor e nenhum resultado mudaram**. **Alegações não auditadas no módulo: 0.**

## Pontos de dificuldade
A condição de estabilidade do esquema explícito é o primeiro tropeço prático: um passo de tempo grande demais faz a solução divergir sem nenhum aviso de natureza física. E a reologia depende exponencialmente da temperatura, de modo que erros pequenos no campo térmico produzem viscosidades erradas por ordens de grandeza. Some-se a isso o risco de sobrecarga específico deste módulo: as aulas com código pedem, ao mesmo tempo, sintaxe Python, um conceito matemático novo e uma interpretação geológica — foi por isso que duas delas foram divididas.

## Formato do questionário — decisão

**3 questionários parciais + 1 final cumulativo.**

| Parcial | Aulas | Eixo | Objetivos |
|---|---|---|---|
| 1 — a ferramenta e o método numérico | 01-02 | Python/NumPy vetorizado, Matplotlib, EDO × EDP, diferenças finitas, ordem de precisão | `oa01`, início de `oa02` |
| 2 — as equações governantes e sua solução | 03-06 | Continuidade, Stokes, malhas, lagrangiano/euleriano, calor, FTCS/BTCS, estabilidade | `oa02`, início de `oa03` |
| 3 — a litosfera real | 07-09 | Geotermas oceânica e continental, reologia, extensão e colisão | `oa03`, `oa04` |
| Final cumulativo | 01-09 | Integração | os quatro |

A decisão foi tomada pela auditoria científica sobre o módulo de 7 aulas e **confirmada sem alteração** pela revisão didática depois da divisão para 9. Os cortes 02│03 e 06│07 são as **duas únicas descontinuidades reais** do módulo: em 02│03 o objeto muda de *método* para *física*; em 06│07 muda de *equação genérica* para *litosfera concreta com números medidos*. Qualquer outro corte separaria coisas que a aula seguinte usa na primeira linha. As duas divisões caíram **dentro** dos blocos existentes — 03│04 e 05│06 estão ambos na Parcial 2 —, exatamente como a auditoria previu ao registrar a recomendação como robusta a divisão.

O **final cumulativo é obrigatório**: a cadeia calor → reologia → deformação só existe atravessando as três parciais, e a pergunta central do módulo — por que um erro pequeno no campo térmico da Aula 06 destrói a viscosidade da Aula 08 e, com ela, o modelo de extensão da Aula 09 — não cabe em parcial nenhuma. Pelo menos duas questões do final devem ser de integração explícita.

## Registro do módulo
- Aulas: ✅ **9/9** — 7 escritas em 2026-09-19 (etapa 1 da cadeia de produção — redação), duas delas divididas em 2026-09-19 pela revisão didática, totalizando 9.
- Auditoria científica: ✅ **concluída e aprovada** em 2026-09-19 (modo `audit-and-fix`, profundidade `full`), **mais passagem pontual em 2026-09-20**. Totais: **16 achados (1 🔴, 14 🟠, 1 🟡), todos corrigidos, 0 em aberto**; 40 itens azuis. As alegações auditáveis declaradas nos blocos de metadados passaram de **35 para 49**; 55 rastreadas no total, **0 não auditadas**. Sete fontes acrescentadas ao módulo. Onze blocos de código executados. **Gate liberado** para questionário e flashcards, com **oito** restrições ao gerador.
- Revisão didática: ✅ **concluída** em 2026-09-19 (modo `review-and-fix`). 9 achados (1 🔴, 5 🟠, 2 🟡, 1 🔵); todos os 🔴 e 🟠 resolvidos. Duas aulas divididas, cinco renumeradas, Matplotlib acrescentado à Aula 01. Nenhuma correção da auditoria científica foi desfeita na divisão.
- Questionário: ✅ concluído — **3 parciais + 1 final cumulativo**, blocos 01-02 / 03-06 / 07-09 (recomendação da auditoria, confirmada sem alteração pela revisão didática após a divisão): [[23-modelagem-numerica-geodinamica-questionario-parcial-1|parcial 1 (a01-a02, oa01+início de oa02, 8 questões)]] · [[23-modelagem-numerica-geodinamica-questionario-parcial-2|parcial 2 (a03-a06, oa02+início de oa03, 12 questões)]] · [[23-modelagem-numerica-geodinamica-questionario-parcial-3|parcial 3 (a07-a09, oa03+oa04, 11 questões)]] · [[23-modelagem-numerica-geodinamica-questionario-final|final cumulativo (todo o módulo, 13 questões, com questão obrigatória de integração cruzando os três blocos)]] — 44 questões no total, 100 pontos cada questionário. Cobertura: os quatro objetivos de aprendizagem (`oa01`-`oa04`) com questões dedicadas em pelo menos uma parcial cada, mais reforço de integração no final. As oito restrições do `audit.generator_warnings`/`assessment_gate` foram lidas e respeitadas: κ nunca é tratado como a constante de decaimento radioativo λ (q07 do parcial 1 e q15 do parcial 2 testam essa distinção diretamente); o termo viscoso de Stokes usa sempre a forma completa div[η(∇v+∇vᵀ)], com a forma simplificada restrita explicitamente a η constante (q09 do parcial 2, q34 do final); o critério de instabilidade numérica usado é sempre o princípio do máximo violado, nunca "temperatura negativa" (q19 do parcial 2, q37 do final); a convenção de sinal de dq/dz = ±A(z) é declarada antes de qualquer cálculo (q42 do final); ruptura frágil e o modelo numérico "plástico" nunca aparecem como sinônimos (q25 do parcial 3); a diferença central para a primeira derivada é sempre tratada como de segunda ordem de precisão (q07 do parcial 1); `np.gradient` é tratado como não usando diferença central nas bordas (q11 do parcial 2); Q = 540 kJ/mol é sempre atribuído a Karato & Wu (1993), nunca a Hirth & Kohlstedt (q26 do parcial 3); a razão de viscosidades do exemplo de Arrhenius é usada como ≈22 (pouco mais de uma ordem de grandeza), nunca duas ordens (q27 do parcial 3 generaliza o cálculo para novos valores de temperatura); e a subsidência remanescente aos 100 Ma é sempre "pouco mais de 20%", nunca "quase 20%" (q29 do parcial 3, testada como V/F direto contra o erro específico).
- Flashcards: ✅ concluído em 2026-09-20 — **87 cards** em formato CSV frente;verso pronto para Anki, [[23-modelagem-numerica-geodinamica-flashcards|baralho]]. Respeitadas as oito restrições do gate: κ vs λ (10 cards), termo viscoso de Stokes (5 cards), princípio do máximo (4 cards), convenção de sinal dq/dz (3 cards), frágil vs modelo plástico (4 cards), ordem de precisão de diferença central (4 cards), np.gradient bordas (2 cards), Cp com temperatura (3 cards); núcleo conceitual (47 cards) e valores numéricos verificados (não reensinados como "verdade universal")

## Navegação
Próximo: [[24-machine-learning-geociencias/24-machine-learning-geociencias-modulo|Módulo 24 — Fundamentos e aplicações de machine learning em geociências]] Índice: [[_curso|Voltar ao curso]]
