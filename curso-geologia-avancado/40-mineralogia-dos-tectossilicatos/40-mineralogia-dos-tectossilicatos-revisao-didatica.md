# Revisão didática — Módulo 40: Mineralogia dos tectossilicatos

**Módulo:** [[40-mineralogia-dos-tectossilicatos-modulo|Módulo 40 — Mineralogia dos tectossilicatos]]
**Escopo:** 14 aulas (a01–a14), ~28.800 palavras de corpo. Pergunta orientadora: alguém aprende com este material, ou só está correto?
**Data:** 2026-08-26

## Veredito geral: bem ensinado

O módulo é o mais longo do curso avançado até aqui, e é o que tem a arquitetura interna mais explícita. A progressão vai da **regra estrutural** ao **objeto físico** ao **procedimento de bancada** ao **cálculo**, e cada bloco existe porque o anterior o tornou possível:

- **a01** estabelece a regra única que gera a classe inteira — todo oxigênio compartilhado por dois tetraedros, Al entra no lugar do Si, sobra carga, entram cátions grandes — e transforma essa regra numa cadeia causal nomeada, retomada em todas as aulas seguintes.
- **a02–a04** aplicam a regra ao caso mais simples possível (arcabouço neutro, sem cátions M): os polimorfos de sílica, primeiro no espaço P–T, depois na quiralidade e nas geminações, depois na lâmina.
- **a05–a07** introduzem o caso geral (com cátions M) e separam, deliberadamente, as **três variáveis independentes** de um feldspato: composição (a05), estado estrutural (a06) e história de exsolução (a07). Essa separação é a decisão pedagógica mais importante do módulo.
- **a08–a10** convertem tudo isso em procedimento de microscópio: as leis de geminação e o que cada uma prova (a08), o protocolo de reconhecimento (a09), a medida quantitativa do teor de An (a10).
- **a11–a12** estendem a classe aos grupos restantes, agora com o aluno já equipado para lê-los por contraste com feldspato e quartzo.
- **a13–a14** fecham com a quantificação: da análise química à fórmula estrutural (a13) e da fórmula estrutural ao diagrama de fase (a14).

O fio condutor é forte e nomeado. A "cadeia causal que organiza o módulo inteiro" do callout da a01 reaparece funcionalmente em a05 (por que existem duas séries), a11 (por que existe barreira de saturação) e a12 (por que zeólitas são leves) — não como repetição, mas como a mesma regra aplicada a objetos progressivamente mais complexos.

## Verificações por critério

### Salto de pré-requisito
**Nenhum salto interno.** Este é o ponto mais forte do módulo. Doze das catorze aulas abrem a seção "Antes de começar" com um item explicitamente rotulado *"Da aula NN:"*, nomeando o conceito específico herdado e linkando para a aula de origem — não uma referência genérica ao módulo, mas o fato exato que será usado. A a14, a mais dependente, declara **cinco** heranças distintas (a02, a07, a10, a11, a13), o que é a leitura correta do seu papel de fechamento.

Duas observações, ambas já tratadas pelo próprio material:
- A **a05** é a única aula do miolo que não herda de uma aula imediatamente anterior (salta de volta à a01). Isso é correto e não é um salto: a a05 abre o segundo grande bloco do módulo, e a sílica das a02–a04 é justamente o caso *sem* cátions M, que não precede logicamente o caso *com*.
- A carga de pré-requisitos **externos** é real e concentrada: a a03 pede grupos espaciais e eixos helicoidais; a a05 pede Hermann–Mauguin e notação de Miller; a a06 pede lei de Bragg e leitura de difratograma; a a10 pede elipsoide óptico biaxial e placa de gipso. Nada disso é ensinado aqui. O módulo trata a questão com transparência exemplar: o callout de aviso no `_modulo.md` diz sem rodeios que a dependência dura não é o Módulo 39, e sim os módulos 04 e 05 do curso base, e que este módulo **especializa** aquele repertório em vez de reconstruí-lo. Essa honestidade evita que o aluno interprete a dificuldade como falha do texto.

### Conceitos novos por aula
Dentro do limite, com duas aulas sob vigilância.

A a06 é o caso mais denso conceitualmente — ordem/desordem, parâmetro t, quebra de simetria, triclinicidade, difratometria — mas o texto amarra os cinco a **uma única pergunta** ("onde está o Al?") e desenvolve tudo como consequência dela, o que mantém a carga gerenciável. A a10 apresenta três métodos de determinação de An, mas com estrutura paralela rigorosa (princípio → procedimento → limitação) e uma tabela comparativa explícita ao fim, que é exatamente o andaime que impede a leitura como lista desconexa.

A a14 é a exceção que mereceu intervenção — ver o achado 🟡 abaixo.

### Objetivo declarado vs. seções que de fato ensinam
Conferido o `mapa_objetivo_secao` das catorze aulas contra o conteúdo real das seções nomeadas. Em todos os casos as seções listadas desenvolvem efetivamente o objetivo do cabeçalho. Nenhuma seção órfã, nenhum objetivo fantasma. Os seis objetivos de aprendizagem do módulo têm cada um pelo menos duas aulas dedicadas (ver a tabela de cobertura no [[40-mineralogia-dos-tectossilicatos-auditoria|relatório de auditoria]]).

### Exemplo trabalhado: suficiência e posicionamento
As catorze aulas têm exemplo trabalhado, sempre após o desenvolvimento teórico completo. O módulo faz uma escolha acertada de **variar o tipo** conforme a natureza do conteúdo, em vez de forçar cálculo em toda aula:

- **Diagnóstico por contradição** nas aulas conceituais (a01: uma moda com nefelina *e* quartzo; a02: três polimorfos de sílica na mesma lâmina). Ambos ensinam o mesmo movimento intelectual — usar uma restrição de coexistência como teste de consistência da própria descrição — e ambos terminam com a lição explicitada em uma frase.
- **Procedimento passo a passo** nas aulas de bancada (a08, a09, a10).
- **Cálculo fechado** nas aulas quantitativas (a13, a14).

Três exemplos merecem destaque pela construção. O da **a02** é modelar: apresenta uma assembleia que parece impossível, mostra por que a leitura ingênua falha, e converte a aparente contradição na assinatura normal de resfriamento rápido — ensinando metaestabilidade de forma muito mais durável do que a definição sozinha conseguiria. O da **a13** vai além do procedimento e inclui uma seção própria, *"A pegadinha da Tabela 1 do guia"*, que leva o aluno a encontrar um erro real na fonte primária: é a melhor peça pedagógica do módulo, porque ensina simultaneamente o cálculo e a postura crítica diante de uma tabela publicada. O da **a14** encadeia a análise F1 da a13 até o diagrama de fase, fechando o módulo com um exemplo que só é possível porque todas as aulas anteriores aconteceram.

### Analogias e risco de modelo mental errado
O módulo evita analogias decorativas e usa avisos nomeados no ponto exato de vulnerabilidade. As analogias que existem são poucas e estruturalmente honestas — a estrutura que "encolhe e abre como um fole" na transformação deslocativa (a02) transmite corretamente que nenhuma ligação se rompe; as "gaiolas" da sodalita (a11) preparam com precisão a arquitetura poliédrica das zeólitas na a12.

A série de armadilhas nomeadas é consistente e bem posicionada: "α não é sempre a fase de alta — neste grupo é a oposta" (a02); "tectossilicato não é 'silicato com muito Si', a definição é topológica" (a01); "polimerização máxima não implica densidade alta" (a01, cobrada de volta na a12); "não vi geminação em grade não prova ausência de microclínio" (a08/a09); "diagrama de fase diz o que é estável, não o que existe" (a02, a14). Cada uma ataca o erro mais previsível daquele conteúdo específico, antes que ele se instale.

### Redundância e sobrecarga cognitiva
A recorrência mais frequente do módulo — **o problema do corte**, isto é, o fato de que quase toda propriedade diagnóstica de feldspato depende da orientação da seção — aparece na a04, na a08 (com seção própria, "O problema do corte — de novo", cujo título já reconhece a repetição), na a09 e na a10. Não é redundância preguiçosa: cada aparição aplica o princípio a uma propriedade diferente (forma, traço de geminação, ângulo de extinção) e a a08 nomeia explicitamente que está retomando. É reforço espaçado deliberado do conceito que o `_modulo.md` corretamente identifica como o segundo maior obstáculo do módulo.

A distinção **composição × estado estrutural** aparece na a05, a06, a09 e a13 — também deliberadamente, e também é o primeiro obstáculo listado nos "Pontos de dificuldade". Correto: são os dois eixos que, confundidos, inutilizam toda a leitura petrogenética.

### Recap que recapitula
Os recaps das catorze aulas cobrem os pontos efetivamente desenvolvidos no corpo, sem introduzir fato novo nem omitir conceito central. Em aulas quantitativas (a06, a10, a13, a14) os recaps retomam corretamente as **fórmulas e os valores numéricos**, não apenas conclusões qualitativas — apropriado para conteúdo que será cobrado em cálculo. Verificado que as três correções de auditoria aplicadas durante esta revisão propagaram-se aos recaps correspondentes.

### Dificuldade proporcional à posição no curso
O módulo é o penúltimo do curso e o mais exigente, o que está correto. A progressão interna de dificuldade é monotonicamente crescente em integração — a a14 é legitimamente a mais difícil e depende de cinco aulas anteriores.

Registro uma **escalada de densidade** mensurável: as aulas 01–04 têm em média ~1.670 palavras de corpo; as 05–09, ~2.040; as 10–14, ~2.390. O aumento acompanha a mudança de natureza do conteúdo (de conceitual para procedimental e quantitativo) e é defensável, mas significa que o aluno que calibrou o próprio ritmo pelas quatro primeiras aulas vai sentir as cinco últimas como visivelmente mais pesadas. O `_modulo.md` sinaliza os três pontos de dificuldade, o que mitiga parcialmente.

### Desalinhamento aula ↔ avaliação
Verificado contra os três questionários e o baralho gerados para este módulo ([[40-mineralogia-dos-tectossilicatos-questionario-parcial-1|parcial 1]], [[40-mineralogia-dos-tectossilicatos-questionario-parcial-2|parcial 2]], [[40-mineralogia-dos-tectossilicatos-questionario-final|final]], [[40-mineralogia-dos-tectossilicatos-flashcards|flashcards]]): toda questão e todo flashcard remete a conceito efetivamente ensinado em alguma das catorze aulas. Sem desalinhamento.

Dois cuidados foram tomados na geração da avaliação e devem ser preservados em revisões futuras:
1. A **Parte IV do questionário final** (roteiro prático, derivada da Parte B do guia) foi formulada para ser respondível a partir das tabelas diagnósticas das aulas, e não apenas por quem tem lâminas e microscópio à mão. Cobrar observação de lâmina real de um aluno autodidata seria o desalinhamento mais óbvio possível, e foi evitado.
2. Nenhuma questão exige **leitura de figura do guia** que não esteja reproduzida ou descrita em texto nas aulas. Os diagramas do guia (Figuras 2, 7, 10, 12, 18–23) não estão no material; onde uma questão depende do conteúdo deles, esse conteúdo aparece verbalizado ou tabelado na aula correspondente.

## Achados

### 🟡 [DID-M40-A14-EXTENSAO-001] — A aula 14 estoura o teto de 30 minutos
**Aula:** 14. **Severidade:** amarela (ajuste recomendado, não bloqueante).
**Achado:** com ~2.560 palavras de corpo e **quatro sistemas binários distintos** (VII.1 eutético, VII.2 peritético, VII.3 solução sólida completa, VII.4 solução sólida parcial com mínimo), mais o vocabulário termodinâmico de abertura e a regra das fases, a a14 ultrapassa o teto de ~2.500 palavras / 30 min adotado pelo curso. É a aula mais longa e a mais dependente do módulo — combinação que aumenta o risco de o aluno chegar cansado exatamente aos dois últimos sistemas, que são os que exigem contraste mais fino (a diferença entre um ponto de mínimo e um eutético é sutil e é o ponto conceitual mais escorregadio da aula).
**Por que não foi quebrada em duas partes:** a divisão natural seria VII.1–VII.2 (fases imiscíveis) e VII.3–VII.4 (soluções sólidas), mas o valor pedagógico da aula está justamente na **comparação entre os quatro sistemas** — o quadro comparativo final e a distinção mínimo × eutético perderiam força se os termos comparados estivessem em arquivos separados. A quebra também exigiria renumerar a avaliação e o estado do módulo sem ganho didático proporcional.
**Correção aplicada:** inserido um **ponto de pausa sugerido** entre VII.2 e VII.3, com callout explicando que os dois primeiros sistemas formam um bloco fechado (fases imiscíveis, F = 0 num ponto fixo) e que os dois seguintes mudam de assunto (soluções sólidas). Dá ao aluno permissão explícita para dividir a sessão sem perder o fio, preservando a comparação final intacta.
**Recomendação futura:** se o módulo for revisto, avaliar mover o vocabulário de abertura ("O vocabulário mínimo" + "A regra das fases", ~500 palavras) para o fim da a13, que tem folga conceitual e já opera com fórmulas e proporções. Isso traria a a14 para dentro do teto sem tocar nos quatro sistemas.

### 🟢 [DID-M40-A05-NOMENCLATURA-002] — Densidade de nomenclatura na aula 05, bem administrada
**Aula:** 05. **Severidade:** verde (observação, sem ação).
**Achado:** a a05 introduz, em uma única aula, os limites de nomenclatura dos plagioclásios (seis nomes), os polimorfos alcalinos (sanidina, ortoclásio, microclínio, anortoclásio, monalbita, albita alta e baixa) e cinco variedades gemológicas ou de hábito (celsiana, adulária, clevelandita, amazonita, pedra-da-lua) — mais de vinte termos. Em abstrato, é exatamente o perfil de aula que produz sobrecarga.
**Por que não é um problema aqui:** o texto separa em seções distintas e explicita a natureza de cada bloco. A seção *"A nomenclatura, e o que ela é"* — o título já faz o trabalho — enquadra os limites de An como **convenção**, não como fronteira natural, o que dispensa o aluno de memorizá-los como fato físico. As variedades ficam num bloco terminal claramente periférico. E a seção *"A albita pertence às duas séries"* antecipa e desarma a confusão mais provável do conjunto. A carga nominal é alta; a carga cognitiva real, não.
**Ação:** nenhuma.

## Pontos fortes a preservar

- **A cadeia causal nomeada da a01** ("Al entra no lugar do Si → sobra carga → entram cátions grandes") é o melhor recurso pedagógico do módulo. Ela converte quatro grupos minerais aparentemente independentes em três respostas ao mesmo problema de balanço de carga, e é o que impede que o módulo se leia como catálogo. Qualquer revisão futura deve mantê-la e continuar retomando-a explicitamente em a05, a11 e a12.
- **A separação deliberada entre composição, estado estrutural e exsolução** nas aulas 05–07, em três aulas em vez de uma. É a decisão que mais custou em extensão e a que mais rende: é exatamente a confusão que o `_modulo.md` identifica como o obstáculo nº 1 do módulo, e o material a ataca separando as variáveis em arquivos distintos antes de recombiná-las na a09.
- **O exemplo trabalhado da a13**, que conduz o aluno a descobrir um erro aritmético real na Tabela 1 do guia do Prof. Vlach. Ensinar o procedimento e a desconfiança produtiva no mesmo exemplo é raro e vale muito num módulo cuja fonte primária é um caderno didático com erratas conhecidas.
- **A honestidade sobre o pré-requisito real.** O callout do `_modulo.md` que diz que a dependência dura não é o Módulo 39, e sim os módulos 04 e 05 do curso base, evita que o aluno procure em vão uma continuidade que não existe e enquadra corretamente o módulo como especialização, não como continuação.
- **O tratamento das divergências com a fonte primária.** Onde as aulas corrigem o guia (cinco pontos) ou divergem dele (quiralidade das leis de geminação do quartzo), elas dizem que estão fazendo isso e mostram a evidência. Isso ensina, de passagem, como se lê literatura técnica datada — uma habilidade que nenhuma aula do módulo declara ensinar, mas que o módulo inteiro modela.

## Recomendação

**Aprovar o módulo.** Nenhuma correção didática bloqueante. O único achado 🟡 (extensão da a14) já teve mitigação aplicada — ponto de pausa sugerido inserido entre VII.2 e VII.3 — e fica registrada a recomendação de refinamento futuro (mover o vocabulário termodinâmico de abertura para o fim da a13) para o caso de o módulo ser revisto.
