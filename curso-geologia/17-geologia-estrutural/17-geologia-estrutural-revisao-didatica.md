# Revisão didática: Módulo 17 — Geologia estrutural e deformação

**Revisado em:** 2026-08-18 · **Modo:** review-and-fix
**Material:** seis aulas do M17, questionário final e baralho de flashcards
**Veredito da primeira passagem:** Requer revisão
**Veredito final:** Bem ensinado com ressalvas

## Resumo

**Primeira passagem:** 🔴 0 bloqueiam · 🟠 4 prejudicam · 🟡 4 atrito · 🔵 1 sugestão
**Após as correções:** 🔴 0 bloqueiam · 🟠 2 prejudicam (nenhuma corrigível nesta skill) · 🟡 0 atrito · 🔵 1 sugestão

**Carga estimada:** 47 termos únicos nos blocos de vocabulário; 1 exemplo trabalhado por aula, todos com 2–3 perguntas encadeadas; 6 aulas declaradas de ~30 min. Corpo por aula após as correções: 1.329 · 1.470 · 1.499 · 1.431 · 1.471 · **2.071**. Cinco aulas ficam dentro do teto de 1.600 palavras do LC-02; a aula 06 não fica, e é o achado 🟠 3.

A auditoria científica de 2026-08-18 encaminhou explicitamente um ponto a esta revisão ("se restar dificuldade de leitura no trecho, é assunto do `revisor-didatico`"). Ele foi recebido e tratado — é o achado 🟠 1.

## Achados

### 🟠 1. A aula 06 ensinava dois padrões em "V" de origens diferentes sob um título que nomeia só um

**Tipo:** título que não corresponde à seção / modelo mental errado
**Onde:** aula 06 · seção "Como dobras aparecem em mapa: a regra do V"
**Problema:** a seção abria anunciando dobras e gastava os dois primeiros terços com a regra do V — que é um fenômeno de **camada inclinada cruzando o relevo**, não de dobra — incluindo as três exceções e o critério de cota. Só depois pivotava para o V do caimento, com um "de origem diferente" solto no meio do texto. Quem lê pela primeira vez atravessa a regra do V inteira acreditando que ela é a regra das dobras, e sai com os dois padrões fundidos num só. Foi exatamente a fusão que a auditoria desfez no plano factual e encaminhou aqui no plano de leitura.
**Correção aplicada:** a seção foi partida em duas — "A regra do V: lendo o mergulho de uma camada pelo traço no vale" e "Como dobras aparecem em mapa: o V do caimento e o padrão de idades" — com um parágrafo de abertura que anuncia os dois padrões e avisa que confundi-los é a forma mais fácil de ler um mapa ao contrário. O `mapa_objetivo_secao` foi atualizado.
**Escopo:** correção local, concluída.

### 🟠 2. O exemplo trabalhado da aula 06 era ambíguo justamente no ponto em que a regra é aplicada

**Tipo:** salto no exemplo trabalhado / enunciado ambíguo
**Onde:** aula 06 · "Exemplo trabalhado", situação e Pergunta 1
**Problema:** a situação dizia "camadas sedimentares cruzando um vale profundo em formato de 'V' bem definido, com a ponta do V apontando para leste". Lido literalmente, o "V" é o do **vale** — a forma do relevo em corte. A regra do V, porém, se aplica ao **traço de afloramento da camada** desenhado no mapa. Um iniciante aplicaria a regra à topografia e chegaria à resposta certa por acaso, com o modelo errado. A Pergunta 1 desfazia a ambiguidade, mas tarde demais: a leitura já tinha sido feita.
**Correção aplicada:** a situação passou a nomear o traço de afloramento explicitamente, com um parêntese que fixa a distinção ("o 'V' de que a regra trata é sempre o do traço da camada desenhado no mapa, nunca o formato do vale visto em corte"), e a Pergunta 1 foi enxugada para não repetir o enunciado.
**Escopo:** correção local, concluída.

### 🟠 3. A aula 06 está muito acima do teto de palavras e concentra conceitos demais — ABERTA

**Tipo:** sobrecarga cognitiva / excesso de conceitos novos
**Onde:** aula 06 · corpo inteiro
**Problema:** a aula tinha 1.938 palavras de corpo contra um teto LC-02 de 1.600 (21% acima), e o metadado declarava ~1.600, mascarando a violação. Ela carrega oito blocos conceituais independentes: direção, mergulho, símbolo de atitude, regra do V, as três exceções da regra, o V do caimento, o padrão de idades em mapa, traço e símbolos de falha, seção geológica e mergulho aparente. O limite de referência é 3 a 4 ideias independentes por aula de 30 min. Agrava que o próprio hub do módulo declara esta aula como ponto de dificuldade ("raciocínio em 3D a partir de dados 2D de mapa"): a aula mais difícil do módulo é também a mais longa e a mais densa.
**Correção sugerida:** dividir em duas partes. Parte 1 — "Estruturas em mapa": atitude, símbolo, regra do V e exceções, V do caimento, padrão de idades, traço de falha. Parte 2 — "Da vista de cima ao corte vertical": construção de seção geológica e mergulho aparente. O corte é limpo porque as duas metades já são conceitualmente separadas no texto atual.
**Escopo:** **exige dividir a aula** — decisão do `gerador-de-curso-modular`, não desta skill. Não improvisado aqui.
**Nota de transparência:** as correções 🟠 1 e 🟠 2 acrescentaram cerca de 130 palavras a esta aula, levando-a de 1.938 para 2.071. Isso é deliberado e não contradiz o achado: clareza não se compra comprimindo uma aula já sobrecarregada — encher de explicação piora a sobrecarga, e a correção certa continua sendo a divisão. O metadado `palavras_corpo` foi atualizado para 2.070 com a nota do encaminhamento, para que o excesso fique visível em vez de mascarado.

### 🟠 4. Referência cruzada imprecisa na aula 02, com promessa de conteúdo que nenhuma aula entrega

**Tipo:** referência cruzada incorreta / promessa não cumprida
**Onde:** aula 02 · seção "Rúptil: quando a rocha fratura"
**Problema:** o texto dizia que juntas e falhas são estruturas "que este módulo detalha nas aulas 04 e 05". Dois defeitos empilhados: a aula 05 é sobre zonas de cisalhamento, um fenômeno **dúctil**, e não trata de junta nem de falha rúptil — o aluno que for lá procurar não acha; e a aula 04 declara explicitamente que as juntas ficam "fora do escopo detalhado deste módulo", de modo que o detalhamento prometido para elas não existe em lugar nenhum. Uma promessa não cumprida em material autodidata custa caro: o aluno não tem a quem perguntar se procurou no lugar errado ou se o conteúdo não existe.
**Correção aplicada:** o trecho passou a apontar só a aula 04 e a declarar o que ela de fato entrega — "que detalha as falhas e trata das juntas só o suficiente para separar uma coisa da outra". O ponteiro dúctil para a aula 05, que já estava correto no parágrafo seguinte, ficou intacto.
**Escopo:** correção local, concluída.

### 🟡 5. Blocos de vocabulário acima do teto de 8 termos nas aulas 03 e 04

**Tipo:** carga de vocabulário / violação de LC-03
**Onde:** aula 03 (9 termos) e aula 04 (10 termos)
**Problema:** o LC-03 fixa o bloco "Vocabulário desta aula" em 5 a 8 termos, e as duas aulas mais densas em nomenclatura o estouravam. As entradas excedentes eram, nos dois casos, membros de pares que a própria aula ensina como contraste ou como caso particular — apresentá-los como verbetes independentes multiplica a contagem sem acrescentar distinção.
**Correção aplicada:** na aula 03, "Anticlinal" e "Sinclinal" viraram uma entrada única de par contrastado, que é como a aula os ensina (9 → 8). Na aula 04, "Falha reversa" absorveu "Falha de cavalgamento" — que a própria aula apresenta como "um caso especial de falha reversa" — e "Falha transcorrente" absorveu "Sentido dextral / sinistral", que é atributo dela e não termo autônomo (10 → 8). Nenhuma definição foi perdida, nenhum limite numérico da auditoria foi alterado.
**Escopo:** correção local, concluída.

### 🟡 6. "Rejeito" definido no vocabulário da aula 04 e nunca usado no corpo dela

**Tipo:** termo declarado mas não exercitado
**Onde:** aula 04 · vocabulário versus corpo
**Problema:** "rejeito (slip)" ocupava uma linha do bloco de vocabulário e não reaparecia uma única vez na aula. O termo é depois cobrado de fato — a aula 05 fala em "rejeito de camada marcadora" e a dissertativa D2(b) do questionário depende dele —, mas o aluno o encontra na tabela, não vê uso, e chega à aula 05 com um termo que leu uma vez e nunca aplicou.
**Correção aplicada:** o corpo da aula 04 passa a nomear o termo onde o conceito já aparecia — "é esse deslocamento — o **rejeito** — que a define". Uma palavra, no lugar onde a definição já estava sendo dada em outras palavras.
**Escopo:** correção local, concluída.

### 🟡 7. A aula 06 terminava sem fechamento de módulo

**Tipo:** navegação / convenção do curso quebrada
**Onde:** aula 06 · fim do arquivo
**Problema:** a aula 06 tinha apenas o bloco "Anterior". Todas as outras aulas do módulo têm "Próxima aula", e a última aula de cada módulo do curso (verificado em M06 e M16) traz um bloco de encerramento que aponta para o módulo seguinte. O módulo 17 simplesmente parava, sem sinalizar ao aluno que ele tinha chegado ao fim nem para onde ir.
**Correção aplicada:** bloco "Próxima aula" de encerramento acrescentado, na forma curta usada no M16, apontando para o Módulo 18.
**Escopo:** correção local, concluída.

### 🟡 8. Os metadados `palavras_corpo` das seis aulas divergiam do texto real

**Tipo:** instrumento de verificação desalinhado
**Onde:** as seis aulas · bloco de metadados
**Problema:** os valores declarados (1.450 a 1.650) não batiam com nenhuma contagem real. Cinco aulas estavam **superdeclaradas** — a aula 05 declarava 1.650 tendo 1.471, e passava por violar um teto que na verdade respeita — e a aula 06 estava **subdeclarada** em quase 340 palavras, mascarando a única violação real de LC-02 do módulo. Esse é o campo que a própria revisão didática usa para conferir o LC-02: errado, ele inverte o diagnóstico.
**Correção aplicada:** os seis valores foram recontados e corrigidos. A aula 06 recebeu, junto do número, a nota do encaminhamento ao `gerador-de-curso-modular`.
**Escopo:** correção local, concluída.

### 🔵 9. Desalinhamento aula–avaliação e aula–baralho, já registrado e sob outra titularidade — ABERTO

**Tipo:** desalinhamento entre o que a aula ensina e o que a avaliação cobra
**Onde:** questionário final (matriz de cobertura) e baralho
**Problema:** `oa04` parte 2 (zonas de cisalhamento) e `oa05` (mapas e seções) só são avaliados por questões de aplicação e dissertativas, sem nenhum item de múltipla escolha — o aluno não tem checagem rápida de recordação nos dois objetivos finais, justamente os que fecham o módulo. E o baralho segue sem card sobre o sentido do V em dobras com caimento, o ponto que a auditoria corrigiu como achado 🔴 1: o conteúdo mais delicado do módulo não tem cobertura de memorização.
**Correção sugerida:** ambos já estão registrados como pendências do relatório de auditoria de 2026-08-18 e pertencem ao `gerador-de-questionarios` e ao `gerador-de-flashcards`. Esta skill **não** edita questionário nem baralho — reporta e encaminha.
**Escopo:** exige geração de item novo em outra skill. Confirmado aqui, não duplicado como pendência nova.

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo | Avaliado em |
|---|---|---|---|
| `oa01` — distinguir tensão (stress) de deformação (strain) | aula 01, quatro seções | sim — arenito de 500 m encurtado para 400 m | 1, 2, V1, D1(a) — 6 pts |
| `oa02` — relacionar comportamento rúptil e dúctil às condições | aula 02, seis seções | sim — calcário a 2 km versus 18 km | 3, 4, A1, D1(b) — 7 pts |
| `oa03` — classificar dobras | aula 03, cinco seções | sim — calha com camada jovem no núcleo, e a variante tombada | 5, 6, 7, V2, A2 — 7 pts |
| `oa04` parte 1 — classificar falhas | aula 04, seis seções | sim — plano a 55° com camada marcadora deslocada | 8, 9, 10, V3 — 5 pts |
| `oa04` parte 2 — classificar zonas de cisalhamento | aula 05, cinco seções | sim — lâmina de milonito com porfiroclasto sigma e fábrica S-C | V4, A3, D2(a), D2(b) — 7 pts · **sem múltipla escolha** |
| `oa05` — interpretar mapas e seções estruturais | aula 06, seis seções | sim — traço em V para leste, flancos a 30°/35° | A4, D3 — 7 pts · **sem múltipla escolha** |

Nenhum objetivo descoberto, nenhuma seção órfã: as seis aulas mapeiam integralmente os cinco objetivos do módulo, com `oa04` legitimamente repartido entre as aulas 04 e 05. A ressalva de cobertura está no tipo de item, não na existência dele — achado 🔵 9.

## Verificação do contrato de nível

- **LC-01:** aprovado. A primeira ocorrência de cada termo de geociências vem com definição em português comum. "Milonito" é o caso mais bem resolvido: aparece na aula 02, é definido ali mesmo e traz o ponteiro para o aprofundamento na aula 05, em vez de ser usado cru.
- **LC-02:** **reprovado na aula 06** (2.071 palavras contra teto de 1.600) — achado 🟠 3, aberto. Aprovado nas outras cinco, entre 1.329 e 1.499.
- **LC-03:** aprovado após as correções. As seis aulas têm "Antes de começar" com link direto para o material exigido, e todos os blocos de vocabulário ficam agora em 7 ou 8 termos. Os sete alvos de wikilink de pré-requisito (M00 a05, M01, M02, M07, M08 e as aulas internas) foram conferidos um a um e todos existem — nenhuma cadeia de pré-requisito quebrada.
- **LC-04:** aprovado. Cada aula abre pela analogia cotidiana antes do termo técnico: massa de modelar (a01), chocolate gelado e derretido (a02), folha de papel empurrada pelas pontas (a03), lanterna e piso do mineiro (a04), gelo cortado a machado versus massa mole (a05). A analogia da aula 05 é a mais bem construída porque declara o próprio limite — falha e zona de cisalhamento como dois extremos de um contínuo, não como duas coisas separadas.
- **LC-05:** aprovado. Os números aparecem como ordem de grandeza com a variabilidade declarada ("~10 e ~15 km", "não é um valor fixo e universal").
- **LC-06:** aprovado. O tensor de stress entra de forma qualitativa e a aula 01 declara explicitamente, em "O que não concluir", que a álgebra de tensores não será exigida — reativação dispensada porque o uso não é matemático.
- **LC-07:** aprovado. As seis aulas têm "Erros comuns", "O que não concluir" e "Recap relâmpago" completos.
- **LC-08:** aprovado. A divergência 30° × 45° no corte do cavalgamento aparece como divergência declarada, sem que a aula arbitre — exatamente o que o LC-08 pede.

## Alinhamento entre as aulas

A progressão é cumulativa e sem salto: causa e efeito (01) → o que decide a resposta (02) → produto dúctil (03) → produto rúptil (04) → produto dúctil concentrado (05) → leitura integrada em mapa (06). A aula 06 funciona como integração das anteriores e reutiliza dobras da 03 e falhas da 04 sem reensiná-las.

Duas escolhas de sequência merecem registro por serem acertos, não defeitos. A primeira: dobras (dúctil) vêm antes de falhas (rúptil), invertendo a ordem em que a aula 02 apresenta os dois regimes. Funciona porque a aula 03 é a mais visual do módulo e a 04 depende de vocabulário de stress que a 03 não consome. A segunda: a aula 05 é apresentada como "equivalente dúctil da falha" e por isso vem **depois** da 04, embora o regime dúctil tenha sido introduzido antes — a dependência real é da anatomia da falha, não do regime, e a aula está posicionada de acordo com a dependência real.

Após a correção do achado 🟠 4, não resta ponteiro cruzado apontando para aula errada em nenhuma das seis aulas.

## O que está bem feito

Os exemplos trabalhados são o ponto mais forte do módulo. Nenhum é ilustração passiva: todos encadeiam 2 a 3 perguntas em que a última testa o caso que quebra a intuição construída pelas anteriores — a dobra tombada que mantém o nome de sinclinal (a03), o mergulho de 55° conferido contra a previsão de Anderson (a04), a impossibilidade de medir rejeito numa zona de cisalhamento (a05). É a estrutura certa para material autodidata, onde ninguém está por perto para propor o contraexemplo.

O módulo também separa com disciplina o que é observação do que é inferência, e nomeia os limites em vez de os esconder: a transição rúptil-dúctil vem com a variabilidade declarada, a teoria de Anderson vem rotulada como padrão idealizado, a divergência de 30° × 45° no cavalgamento fica exposta como divergência. Os blocos "Erros comuns" atacam pares de confusão reais e específicos — dúctil × mole, milonito × brecha, eixo × plano axial, teto/muro × esquerda/direita — e não genéricos.

## Gate didático

**Liberado.** Nenhum achado 🔴. Os quatro achados corrigíveis nesta skill foram aplicados; nenhuma edição introduziu alegação factual nova, e nenhuma tocou em número, limite ou classificação já validados pela auditoria científica de 2026-08-18.

Duas ressalvas permanecem abertas, ambas fora da titularidade desta skill e nenhuma bloqueante:

1. **Achado 🟠 3** — a aula 06 precisa ser dividida em Parte 1 / Parte 2 pelo `gerador-de-curso-modular`. Até lá, é a aula do módulo em que o autodidata tem mais chance de estourar os 30 min declarados e mais chance de sair com retenção parcial.
2. **Achado 🔵 9** — cobertura de múltipla escolha para `oa04` parte 2 e `oa05` (`gerador-de-questionarios`) e card do sentido do V em dobra com caimento (`gerador-de-flashcards`), ambos já registrados pela auditoria.

O `course-state.yaml` **não** foi alterado por esta execução, conforme a restrição de coordenação em paralelo; o registro do módulo foi feito apenas no hub `17-geologia-estrutural-modulo.md`. Nenhum arquivo fora de `17-geologia-estrutural/` foi tocado.
