# Revisão didática: Módulo 30 — Métodos numéricos para geociências

**Revisado em:** 2026-08-29 · **Modo:** review-and-fix
**Material:** as 5 aulas do M30 (o módulo ainda não tem questionário nem baralho)
**Veredito da primeira passagem:** Requer revisão
**Veredito final:** Bem ensinado com ressalvas

## Resumo

**Primeira passagem:** 🔴 0 bloqueiam · 🟠 3 prejudicam · 🟡 5 atrito · 🔵 1 sugestão
**Após as correções:** 🔴 0 · 🟠 1 em aberto (exige dividir uma aula) · 🟡 0 · 🔵 1 sugestão

**Carga estimada:** 36 termos únicos nos blocos de vocabulário (7 · 8 · 7 · 7 · 7); 1 exemplo trabalhado por aula, todos com passos numerados e conferidos pela auditoria; 5 aulas declaradas de 30 min. Corpo real por aula, recontado sobre "Conteúdo" até "Próxima aula" **depois** das correções: 1.570 · 1.600 · 1.599 · 1.598 · **1.882**. Quatro dentro do teto de 1.600 do LC-02; a aula 05 permanece 17,6% acima dele, deliberadamente não podada — ver o achado 🟠 1.

A auditoria científica de 2026-08-29 aprovou o módulo (4 achados, todos corrigidos, todos em aritmética de exemplo trabalhado) e encaminhou explicitamente dois itens para esta revisão: o rótulo do Passo 1 da aula 02 (achado 🟠 3 abaixo) e a ressalva desnecessária da aula 04 (achado 🟡 7).

## Achados

### 🟠 1. A aula 05 tem 1.882 palavras e empacota dois assuntos — EM ABERTO, exige divisão

**Tipo:** sobrecarga de conteúdo / violação de teto do LC-02
**Onde:** aula 05 · corpo inteiro
**Problema:** 1.882 palavras de corpo real contra o teto de 1.600 — 17,6% acima, o maior estouro dos dois módulos revisados nesta passagem, e praticamente idêntico ao caso que o módulo 16 resolveu por divisão (aula 05 daquele módulo, 1.850 palavras, ~16% acima, dividida em 05a e 05b em 2026-08-18). O estouro aqui não é de fraseado, é estrutural: o próprio título junta os dois assuntos com um "e", e o corpo entrega duas coisas independentes, com vocabulário e critério de erro próprios. **Integração numérica** (trapézio, Simpson, ordem O(h²) e O(h⁴), a exigência de número par de intervalos) responde à pergunta "como somo área a partir de pontos". **EDOs** (Euler, RK4, primeira e quarta ordem, passo, acúmulo de erro ao longo dos passos) responde a "como projeto uma grandeza que muda". O aluno que chega ao exemplo trabalhado já atravessou cinco seções e dois conjuntos de métodos, e o exemplo cobre só o segundo assunto — a integração numérica sai da aula sem nenhum caso trabalhado próprio, apesar de ocupar as duas primeiras seções.
**Correção sugerida:** dividir em `05a — Integração numérica: trapézio e Simpson` e `05b — Equações diferenciais ordinárias: Euler e Runge-Kutta`, com a seção final "O que fica para depois: sistemas e equações de difusão espacial" fechando a 05b, já que é ela que aponta para o módulo 23 do curso avançado. A divisão libera espaço para o que hoje falta: um exemplo trabalhado de integração (a curva de subsidência que a própria aula cita como motivação e nunca calcula).
**Correção NÃO aplicada, deliberadamente.** Podar 282 palavras de uma aula cujo problema é ter dois assuntos seria comprimir conteúdo, que é exatamente o que o LC-02 proíbe ("o que não cabe vira Parte 1 / Parte 2, ou é deferido — nunca é comprimido"), e mascararia o defeito estrutural em vez de resolvê-lo. Dividir uma aula é decisão do `gerador-de-curso-modular`. O `palavras_corpo` da aula foi atualizado para o valor real (1882), de modo que o estouro fique visível no metadado em vez de escondido atrás de um "~1750" subdeclarado.
**Escopo:** exige dividir a aula. Encaminhado ao `gerador-de-curso-modular`. **Consequência para a próxima etapa:** o questionário e o baralho devem tratar integração numérica e EDOs como blocos separados, com IDs que sobrevivam à futura divisão, para não precisarem ser refeitos quando a 05 virar 05a e 05b.

### 🟠 2. Os objetivos das cinco aulas usavam IDs locais que não batem com o hub nem com o `course-state`

**Tipo:** desalinhamento de instrumento (aula ↔ avaliação)
**Onde:** as 5 aulas · cabeçalho e bloco `mapa_objetivo_secao`
**Problema:** dois defeitos que se somam. Primeiro, nenhuma das cinco aulas tinha o bloco "Ao final você vai conseguir" que o resto do curso usa — o objetivo aparecia só como uma linha `**Objetivo:**` no cabeçalho, em prosa, sem ID. Segundo, o `mapa_objetivo_secao` de cada aula usava `OA-01` … `OA-05`, IDs locais que não existem em lugar nenhum: o hub e o `course-state.yaml` chamam esses mesmos objetivos de `geologia-m30-oa01` … `geologia-m30-oa05`. O efeito prático aparece na etapa seguinte: o `gerador-de-questionarios` monta a matriz de cobertura cruzando o ID do objetivo com as seções que o ensinam, e nesse módulo o cruzamento não fecharia — cinco objetivos no hub, cinco objetivos nas aulas, nenhum par com o mesmo nome. É o tipo de defeito que não atrapalha o aluno e trava o pipeline.
**Correção aplicada:** as cinco aulas ganharam o bloco "Ao final você vai conseguir" imediatamente antes de "Conteúdo", com o ID canônico e o texto do objetivo copiado literalmente do hub; e os cinco `mapa_objetivo_secao` passaram a usar `geologia-m30-oaNN`. Nenhum objetivo foi reformulado — só nomeado com o nome que o resto do curso já usava.
**Escopo:** correção local nas cinco aulas, concluída.

### 🟠 3. O exemplo da aula 02 rotulava "escalonar" um passo que resolve por substituição — RECEBIDO DA AUDITORIA

**Tipo:** exemplo trabalhado que não demonstra o método que a aula ensinou
**Onde:** aula 02 · "Exemplo trabalhado", Passo 1
**Problema:** encaminhado pela auditoria científica como escolha didática fora do escopo dela. A seção "Eliminação de Gauss" define escalonamento com precisão: usar uma equação para eliminar uma incógnita das demais **subtraindo múltiplos apropriados de uma equação das outras**. O exemplo trabalhado, no passo rotulado "Passo 1 — escalonar", faz outra coisa: isola a = 1 − b − c e substitui nas duas outras equações. Os dois caminhos chegam ao mesmo resultado — a auditoria confirmou a aritmética —, mas o aluno que aprende pelo exemplo, como quase todo aluno faz, sai executando substituição e chamando-a de escalonamento. Numa aula cujo objetivo declarado é "resolver por eliminação de Gauss", o único exemplo do método não demonstra o método.
**Correção aplicada:** o passo foi renomeado para "Passo 1 — eliminar *a*" e ganhou uma frase que explicita a relação entre as duas coisas: o objetivo é o mesmo do escalonamento — fazer sumir uma incógnita das demais equações —, e aqui sai mais rápido por substituição porque a terceira equação já tem todos os coeficientes iguais a 1. O aluno passa a ver o atalho **como** atalho, com a razão pela qual ele cabe neste caso específico. Nenhum número do exemplo foi alterado.
**Escopo:** correção local, concluída.

### 🟡 4. Três aulas acima do teto de palavras do LC-02

**Tipo:** violação de teto de carga
**Onde:** aulas 02 (1.693), 03 (1.633) e 04 (1.710)
**Problema:** estouros de 2% a 7% sobre o teto de 1.600. Diferente da aula 05 (achado 🟠 1), aqui o excesso é de fraseado, não de assunto: cada uma das três tem um objetivo único e coerente, e a prolixidade se concentrava em lugares identificáveis — a seção de abertura da 02 (um parágrafo de 180 palavras para dizer onde sistemas lineares aparecem), a seção de abertura da 03 (200 palavras encadeadas num período só) e três seções da 04 (mínimos quadrados, extrapolação e o primeiro item de "O que não concluir").
**Correção aplicada:** poda de prolixidade nas três, sem cortar nenhuma ideia, ressalva, qualificador ou exemplo — as reduções vêm de períodos longos quebrados, parênteses explicativos convertidos em aposto e repetições de fraseado eliminadas. Corpos finais: 1.600 · 1.599 · 1.598. As três ficaram **sem folga** sob o teto; qualquer acréscimo futuro exige poda equivalente.
**Escopo:** correção local, concluída.

### 🟡 5. Ordem dos blocos de abertura invertida nas cinco aulas

**Tipo:** desvio de padrão de abertura (LC-03)
**Onde:** as 5 aulas · entre o cabeçalho e "Conteúdo"
**Problema:** o LC-03 fixa a ordem — bloco "Vocabulário desta aula", depois bloco "Antes de começar, você precisa saber" — e as cinco aulas do M30 traziam a ordem oposta, ao contrário do resto do curso, inclusive do módulo 29 revisado na mesma passagem. Não é cosmético: o "Antes de começar" existe para o aluno detectar sozinho que voltou cedo demais, e ele detecta melhor depois de ver o vocabulário que a aula vai exigir. Ler primeiro os pré-requisitos e só depois descobrir que a aula fala de "dominância diagonal" e "substituição regressiva" inverte a ordem da decisão.
**Correção aplicada:** os dois blocos foram trocados de posição nas cinco aulas. Nenhum conteúdo foi alterado.
**Escopo:** correção local, concluída.

### 🟡 6. Aula 02 com 9 termos no vocabulário, um deles nunca usado no corpo

**Tipo:** carga de vocabulário acima do teto (LC-03) + entrada órfã
**Onde:** aula 02 · "Vocabulário desta aula"
**Problema:** nove entradas contra o teto de 5 a 8 do LC-03. E a entrada excedente era, coincidentemente, a única do bloco que a aula não usa: "matriz aumentada" aparece uma única vez no arquivo inteiro, na própria tabela de vocabulário — o corpo trata o escalonamento em termos de equações, não de matriz, e nunca monta a tabela de coeficientes que a entrada descreve. Vocabulário órfão custa duas vezes: ocupa uma vaga do teto e ensina ao aluno um termo que a aula não vai reforçar.
**Correção aplicada:** a entrada "Matriz aumentada" foi removida. O bloco volta a 8 termos, dentro do teto, e nenhuma definição usada pela aula foi perdida. (A alternativa considerada — fundir "método iterativo" com "Gauss-Seidel", que se definem um em função do outro — ficou desnecessária.)
**Escopo:** correção local, concluída.

### 🟡 7. Ressalva desnecessária no ajuste de isócrona — RECEBIDO DA AUDITORIA

**Tipo:** hedge que ensina um modelo mental errado
**Onde:** aula 04 · "Exemplo trabalhado", Situação 2, Passo 2
**Problema:** encaminhado pela auditoria, que verificou que os quatro pares fornecidos são **exatamente** colineares e que, portanto, o ajuste por mínimos quadrados devolve exatamente 0,05 — não "muito próximo de 0,05", como o texto dizia. A ressalva não estava errada por acidente de arredondamento: ela ensinava que o atalho de dois pontos é uma aproximação do método completo, quando neste caso os dois coincidem por construção. O aluno saía com a impressão de que mínimos quadrados é uma versão mais caprichada do "traçar pelos extremos" — que é precisamente a confusão que a aula 04, segundo o próprio hub, existe para desfazer.
**Correção aplicada:** o passo agora afirma a coincidência exata e usa essa coincidência para ensinar o contraste: com dados reais os pontos se dispersam, o atalho de dois pontos passa a depender de **quais** dois pontos foram escolhidos, e é por isso que se ajusta sobre todos. A ressalva virou o argumento.
**Escopo:** correção local, concluída.

### 🟡 8. `palavras_corpo` divergente nas cinco aulas, subdeclarado em duas

**Tipo:** instrumento de verificação desalinhado
**Onde:** as 5 aulas · bloco de metadados
**Problema:** valores declarados ~1520, ~1650, ~1720, ~1780, ~1750 contra reais 1.570, 1.693, 1.633, 1.710, 1.882. Divergência nas duas direções, e a direção perigosa aparece nos dois extremos do módulo: a aula 01 declarava 50 palavras **a menos** do que tinha, e a aula 05 declarava 132 a menos — ou seja, o metadado do maior estouro do módulo era o que mais o subestimava. Três dos cinco valores declarados já ultrapassavam o teto de 1.600 sem que isso tivesse sido tratado.
**Correção aplicada:** os cinco valores foram recontados programaticamente sobre o corpo real, depois de todas as demais correções, e gravados sem o til: 1570 · 1600 · 1599 · 1598 · 1882. O último fica deliberadamente acima do teto, como registro visível do achado 🟠 1.
**Escopo:** correção local, concluída.

### 🔵 9. Integração numérica é o único método do módulo sem analogia e sem exemplo próprio

**Tipo:** distribuição desigual de apoio à compreensão
**Onde:** aula 05 · "Integração numérica"
**Problema:** as cinco aulas usam analogia de cotidiano com consistência — a balança de décimo de quilo para cancelamento catastrófico, os três amigos dividindo a conta para Gauss-Seidel, o jogo do "maior ou menor" para bisseção, a linha desenhada à mão para Runge, o velocímetro olhado uma vez só para Euler. Trapézio e Simpson não têm nenhuma, e também não têm exemplo trabalhado (o único da aula é de EDO). São os dois únicos métodos do módulo que o aluno recebe apenas em prosa expositiva.
**Escopo:** sugestão, resolvida naturalmente pela divisão proposta no achado 🟠 1 — uma aula 05a dedicada à integração teria espaço tanto para a analogia quanto para o exemplo da curva de subsidência que a própria aula já cita como motivação. Registrada aqui para que a divisão, quando ocorrer, não se limite a partir o texto ao meio.

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo | Avaliado em | Cards |
|---|---|---|---|---|
| `geologia-m30-oa01` — fontes de erro e condicionamento | aula 01, quatro seções | sim — duas situações (análise química; gradiente geotérmico) | pendente | pendente |
| `geologia-m30-oa02` — Gauss, Gauss-Seidel e convergência | aula 02, cinco seções | sim — mistura de três fontes, com contraexemplo de divergência | pendente | pendente |
| `geologia-m30-oa03` — zeros por bisseção e Newton-Raphson | aula 03, quatro seções | sim — vazão em canal, quatro passos + comparação | pendente | pendente |
| `geologia-m30-oa04` — interpolação, diferenças finitas, mínimos quadrados | aula 04, cinco seções | sim — duas situações (topo de camada; isócrona) | pendente | pendente |
| `geologia-m30-oa05` — integração numérica **e** EDOs | aula 05, cinco seções | **parcial** — só EDO (Euler contra solução exata); integração sem exemplo | pendente | pendente |

Um objetivo por aula, sem repartimento e sem seção órfã — mas `oa05` é o único que cobre dois assuntos, e é exatamente essa acumulação que produz o achado 🟠 1. Se a aula 05 for dividida, `oa05` deve ser dividido junto, em `oa05a` (integração) e `oa05b` (EDOs), ou a matriz de cobertura continuará mascarando a lacuna de exemplo da integração.

## Verificação do contrato de nível

- **LC-01 — nenhum termo sem definição:** aprovado. Verificada a primeira ocorrência de cada termo técnico nas cinco aulas. O módulo é rigoroso nisso: "derivada" ganha entrada própria no vocabulário da aula 03 (a aula que a usa) em vez de ser assumida; "ordem de um método" é definida na aula 05 antes de "primeira ordem" e "quarta ordem" aparecerem; "equação transcendental" é explicada sem jargão. Nenhum caso de fronteira.
- **LC-02 — teto de 1.600 palavras:** aprovado em quatro aulas após o achado 🟡 4 (1.570 · 1.600 · 1.599 · 1.598). **Reprovado na aula 05** (1.882), deliberadamente não corrigido — ver o achado 🟠 1. É a única violação de contrato aberta do módulo.
- **LC-03 — abertura padronizada:** aprovado após os achados 🟡 5 e 🟡 6. Os cinco blocos de vocabulário ficam em 7 · 8 · 7 · 7 · 7 termos, e a ordem vocabulário → pré-requisitos passou a valer nas cinco. Os blocos "Antes de começar" marcam cada pré-requisito como "exigido" ou "recomendado", distinção que só este módulo faz no curso e que vale a pena preservar. Todos os wikilinks das cinco aulas foram conferidos e resolvem, inclusive os externos para os módulos 00, 03 e 28.
- **LC-04 — analogia antes do termo:** aprovado, com a ressalva do achado 🔵 9. Onde há analogia, ela vem na ordem certa e — traço notável deste módulo — várias delas dizem **onde quebram**: a do velocímetro na aula 05 é retomada no fim do exemplo trabalhado para explicar exatamente o que RK4 faz de diferente, e a do jogo de adivinhação na aula 03 já embute a limitação do método ("nunca acerta de primeira mesmo estando perto").
- **LC-05 — ordem de grandeza:** aprovado. "uns 7 palpites", "por volta de dez repetições (2¹⁰ ≈ 1.024)", "cerca de um dezesseis avos", "aproximadamente 1,1%" — os números do módulo são de método, não de mundo, e mesmo assim vêm com qualificador de aproximação onde cabe. Os valores corrigidos pela auditoria (±0,2 °C, ~67%, f(2,0625) ≈ −0,351, 2,094568) foram preservados intactos por esta revisão.
- **LC-06 — matemática reativada antes do uso:** aprovado, e é o eixo do módulo. Derivada é reativada na aula 03 antes de Newton-Raphson; exponencial e meia-vida são explicitamente devolvidas ao Módulo 28, aula 03, antes do exemplo da aula 05; a estatística descritiva do Módulo 28, aula 04, é linkada nas aulas 01 e 04. Nenhum aparato matemático entra sem aviso.
- **LC-07 — blocos obrigatórios:** aprovado. As cinco aulas já tinham "Erros comuns", "O que não concluir" e "Recap relâmpago", além de "Exemplo trabalhado" — ao contrário do módulo 29, revisado na mesma passagem, onde os dois primeiros faltavam nas quatro aulas.
- **LC-08 — controvérsia em uma frase:** não se aplica. O módulo não tem controvérsia de literatura retida: os métodos são consolidados e as escolhas entre eles (bisseção contra Newton, Gauss contra Gauss-Seidel, trapézio contra Simpson) são apresentadas como trade-offs de engenharia com critério explícito, não como disputas em aberto.

## Alinhamento entre as aulas

O fio condutor do módulo é o condicionamento, e ele é conduzido com uma consistência que merece registro: nasce na aula 01 como propriedade do problema, reaparece na aula 02 no pivô pequeno e nas equações quase paralelas, na aula 03 como argumento contra pedir mais precisão do que os dados sustentam, e na aula 04 na diferença finita calculada sobre pontos próximos demais — que é literalmente o mesmo exemplo do gradiente geotérmico da aula 01, retomado pelo nome. Quatro aulas usando o mesmo conceito em quatro contextos diferentes, sem reensiná-lo nenhuma vez, é a estrutura que o módulo prometia no hub e cumpriu.

A ancoragem geológica também é consistente e não decorativa: cada método chega junto com o problema de geociências que o exige — balanço de massa de proveniência para sistemas lineares, equilíbrio químico e isostasia flexural para zeros de função, topo de camada entre furos e isócrona para interpolação e ajuste, decaimento radioativo para EDO. Nenhuma dessas âncoras é um enfeite colado no fim da seção; em todos os casos ela abre a seção e motiva o método.

A escolha de fechar o módulo apontando explicitamente para o módulo 23 do curso avançado, nomeando o que **não** é ensinado aqui (EDPs, malhas espaciais, esquemas explícito e implícito), é o oposto de um encerramento vago e é a razão de este módulo existir. Vale notar que essa seção final é também a que mais sofre com o tamanho da aula 05: ela chega depois de o aluno já ter atravessado dois assuntos completos.

## O que está bem feito

O exemplo trabalhado da aula 02 é o melhor do módulo, e por um motivo raro: ele **falha de propósito**. Depois de resolver o sistema por eliminação, o exemplo tenta Gauss-Seidel no mesmo sistema, mostra que a dominância diagonal não vale (0,10 contra 1,00), aplica o método assim mesmo e exibe os valores explodindo — c passa de 67 na terceira repetição e de 6.500 na quinta. Um contraexemplo executado até a divergência ensina o critério de convergência de um jeito que nenhuma formulação da condição suficiente ensina, e ataca diretamente o ponto que o hub identifica como o mais decorado sem ser entendido do módulo. (Essa passagem nasceu da correção do único achado 🔴 da auditoria científica, o que a torna o segundo caso, nesta rodada, de um erro corrigido virando o melhor material do módulo.)

A comparação bisseção × Newton-Raphson na aula 03, também reescrita pela auditoria, acerta o alvo pedagógico difícil: em vez de afirmar que Newton é mais rápido, ela mostra o primeiro passo em que a vantagem é modesta e o segundo em que ela explode (erro de 0,00002, contra as ~11 repetições que a bisseção precisaria), e diz com todas as letras que "é essa aceleração, e não o primeiro passo isolado, que a convergência quadrática descreve". Convergência quadrática é um conceito que quase sempre é enunciado e quase nunca é mostrado.

## Gate didático

**Liberado com uma restrição nomeada.** Nenhum achado 🔴. Os oito achados corrigíveis nesta skill (🟠 2, 🟠 3 e 🟡 4–8) foram aplicados; nenhuma edição introduziu alegação factual nova, e nenhuma tocou em número, fórmula, ordem de convergência ou resultado de exemplo validados pela auditoria científica de 2026-08-29 — em particular, os quatro valores que aquela auditoria corrigiu foram preservados sem alteração.

Permanece **um achado 🟠 em aberto**, o achado 1, que esta skill não deve corrigir: a aula 05 tem 1.882 palavras e dois assuntos, e a correção certa é dividi-la, o que é decisão do `gerador-de-curso-modular`. A restrição que isso impõe à etapa seguinte:

> O `gerador-de-questionarios` e o `gerador-de-flashcards` devem tratar **integração numérica** (trapézio, Simpson) e **EDOs** (Euler, RK4) como dois blocos separados dentro de `geologia-m30-oa05`, com numeração de questões e de cards que sobreviva a uma futura divisão da aula 05 em 05a e 05b. Devem também cobrir integração numérica com pelo menos um item de aplicação, já que a aula não tem exemplo trabalhado próprio para ela — a lacuna do achado 🔵 9.

Fora essa restrição, o módulo está liberado para questionário e flashcards.
