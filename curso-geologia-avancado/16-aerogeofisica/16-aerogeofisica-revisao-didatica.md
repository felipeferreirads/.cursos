# Revisão didática — Módulo 16: Introdução à aerogeofísica

**Data:** 2026-09-09
**Modo:** `review-and-fix` (melhorias aplicadas)
**Escopo:** as 5 aulas do módulo
**Veredito:** **bem ensinado com ressalvas** — 6 achados, todos corrigidos. Nenhum achado de salto de pré-requisito, nenhuma analogia que ensine modelo mental errado, nenhum objetivo declarado sem seção que o ensine (com uma exceção, corrigida).

## O que o módulo já fazia bem, antes da revisão

Registrar isto importa tanto quanto listar defeitos, porque é o padrão que as próximas aulas devem imitar.

1. **A cadeia de pré-requisitos entre aulas é declarada e honesta.** Cada aula nomeia de que aula anterior depende e **por quê**, em prosa, não como lista burocrática — a a03 chega a dizer que "a lógica de separar sinal geológico de ruído se mantém, mas aqui o ruído muda de natureza". Isso é exatamente o tipo de ponte que material autodidata costuma omitir.
2. **Cada aula tem um único fio condutor nomeado e sustentado até o fim.** a01: os parâmetros de aquisição *são* a decisão geológica. a02: o campo medido não é só geologia. a03: o inimigo mudou — agora é a própria plataforma. a04: o sinal vem só da pele do terreno. a05: nenhum método sozinho basta. Nenhuma aula divaga.
3. **As quatro aulas com exemplo trabalhado usam números que o corpo da aula já justificou**, e três delas fecham o exemplo com uma "Interpretação" que volta ao argumento central em vez de parar no resultado numérico.
4. **A a05 já trazia uma "Ressalva pedagógica"** avisando que skin depth não é profundidade máxima de detecção. É exatamente a auto-limitação que impede o leitor autodidata de sair confiante demais, e ela não estava sendo pedida por ninguém.
5. **Densidade conceitual apropriada ao nível.** Nenhuma aula introduz mais que quatro conceitos realmente novos; as demais são retomadas do Módulo 15 explicitamente marcadas como tal.

---

## Achados

### 🟠 DID-M16-A05-ESTRUTURA-001 — A síntese do módulo estava enterrada abaixo do exemplo trabalhado
**Aula 05.**

A seção "Fechando o módulo: por que nenhum método sozinho basta" é a **conclusão do módulo inteiro** — o parágrafo em que os quatro métodos finalmente se encaixam e em que a promessa feita lá no hub ("nenhum dos quatro resolve sozinho a ambiguidade de fonte") é cumprida. Ela estava marcada como `###`, isto é, como subseção, e posicionada **depois** do `## Exemplo trabalhado`.

O efeito num leitor autodidata é concreto e previsível: em todas as outras quatro aulas do módulo (e nas aulas dos Módulos 14 e 15), `## Exemplo trabalhado` é o penúltimo bloco e sinaliza "o conteúdo acabou, agora é aplicação". Quem leu quatro aulas nesse ritmo chega ao exemplo da a05, resolve, e vai direto ao recap — pulando exatamente o texto que fecha o módulo. Um leitor que estuda por varredura de títulos nem vê a seção, porque um `###` depois de um `##` lê-se como subordinado ao `##` anterior.

**Correção:** a seção foi promovida a `## Fechamento do módulo`, ficando no mesmo nível hierárquico do exemplo trabalhado e do recap. A posição foi mantida deliberadamente — mover a seção para antes do exemplo separaria a explicação de skin depth do exemplo que a aplica, trocando um problema por outro. A promoção de nível resolve a invisibilidade sem quebrar o par explicação-exemplo.

### 🟠 DID-M16-A01-VISUAL-002 — A decisão central do módulo ensinada só em prosa corrida
**Aula 01, seção "Três plataformas, três compromissos".**

A aula pedia que o leitor mantivesse simultaneamente na cabeça **três plataformas × sete atributos** (velocidade, autonomia, altura praticável, espaçamento viável, área típica, carga útil, vocação) distribuídos por três parágrafos de prosa, e só então concluísse qual escolher. E essa é a primeira decisão de projeto do módulo: o exemplo trabalhado da própria aula abre justamente escolhendo a plataforma.

Terceira ocorrência do mesmo padrão no curso — **DID-M14-A06-VISUAL-002** e **DID-M15-A01-VISUAL-002** foram idênticos: a comparação multi-eixo que sustenta a decisão central da aula sendo entregue em parágrafos sucessivos, obrigando o leitor a construir mentalmente a tabela que o autor tinha na cabeça. A recorrência sugere que vale um hábito de geração: **comparação de três ou mais alternativas por três ou mais atributos pede tabela, não prosa.**

**Correção:** inserida tabela comparativa de 7 linhas × 3 colunas, seguida de uma frase de leitura que entrega a conclusão que só a tabela torna óbvia — *velocidade e autonomia se pagam em resolução, e resolução se paga em área coberta; nenhuma plataforma ganha nas três*. **Nenhum dado novo:** todos os valores da tabela são destilação dos três parágrafos que já estavam na aula. Os parágrafos foram mantidos, porque neles está o *porquê* de cada número, que a tabela não carrega.

### 🟠 DID-M16-A04-VISUAL-003 — Cadeia de correções sem esquema, num ponto em que a ordem virou argumento
**Aula 04, seção "Do sinal bruto ao dado geologicamente interpretável".**

A auditoria científica corrigiu a ordem de duas correções nesta seção (achado AUD-M16-A04-ORDEMCORRECOES-001) e, ao fazê-lo, transformou a ordem num argumento explícito da aula. Mas a sequência continuava apresentada como quatro parágrafos em negrito, sem nenhum lugar em que o leitor pudesse ver a cadeia inteira de uma vez — o que é o mínimo para memorizar uma sequência de cinco passos cuja ordem é o ponto.

**Correção:** inserido um esquema de linha única (`espectro bruto → ① tempo morto → ② background → ③ stripping → ④ altura → ⑤ conversão → K %, eU ppm, eTh ppm`) logo antes dos parágrafos, com os passos numerados e a frase "cada etapa, uma por uma" fazendo a ponte. O recap foi reescrito com a mesma cadeia em setas. Custo: duas linhas. Ganho: a sequência inteira cabe num olhar, e a numeração dá ao leitor um índice para voltar.

### 🟡 DID-M16-A02-OBJETIVOORDEM-004 — Objetivo declarado prometia uma "ordem correta" que a aula não ensinava — e que não existe
**Aula 02, cabeçalho e seção de correções.**

O cabeçalho prometia: *"aplicar, **na ordem correta**, as correções de IGRF e de variação diurna"*. O corpo apresentava as duas correções, o exemplo aplicava diurna primeiro e IGRF depois — e **em nenhum momento a aula dizia que essa ordem importa, nem por quê**. O leitor que estuda pelo objetivo declarado, que é como se estuda material autodidata, termina a aula sem saber se decorou uma ordem obrigatória, se a ordem do exemplo foi arbitrária, ou se perdeu a explicação.

Pior: **a ordem entre IGRF e diurna de fato não importa** — as duas são subtrações, e subtração comuta. A promessa do cabeçalho era vazia no sentido literal.

**Correção — e aqui a revisão fez mais do que aparar a promessa, porque havia um conceito bom escondido no defeito.** O objetivo foi reescrito para *"sabendo o que na cadeia de processamento tem ordem obrigatória e o que não tem"*, e foi acrescentado ao corpo um parágrafo curto que responde a isso: entre IGRF e diurna a ordem é indiferente; o que é obrigatório é que ambas venham antes do **nivelamento**, e o nivelamento antes de qualquer **realce** — porque essas duas etapas *misturam informação entre pontos vizinhos* e espalhariam a deriva pelo mapa inteiro, de forma irreversível.

O parágrafo fecha com uma regra transferível que serve aos quatro métodos do módulo: *esta etapa é uma subtração ponto a ponto, ou mistura informação entre pontos vizinhos (ou entre canais)? Só a segunda impõe ordem.* Isso conecta diretamente à a04, onde a ordem entre stripping e altura **é** obrigatória exatamente por ser do segundo tipo — transformando dois fatos isolados numa única regra. Item de recap acrescentado.

*Nota de fronteira:* este acréscimo está no limite entre revisão didática e conteúdo novo. Foi feito porque (a) não introduz nenhum fato externo — a comutatividade da subtração e a natureza do nivelamento já estavam implícitas no que a aula afirmava —, e (b) sem ele o objetivo declarado teria de ser simplesmente amputado, deixando o leitor sem saber o que fazer com a ordem que o exemplo usa.

### 🟡 DID-M16-A01-TERMOANTESDEDEFINIR-005 — "Drapeamento" usado dois parágrafos antes de ser definido
**Aula 01.**

O termo **drapeamento** aparece pela primeira vez entre parênteses na descrição do avião de asa fixa ("manter altura de voo baixa e constante (drapeamento do relevo)"), como se fosse autoexplicativo, e só recebe definição dois parágrafos adiante, na seção de altura de voo. É um termo técnico de tradução não óbvia (do inglês *draping*) e é **um dos parâmetros centrais da aula** — não um adorno de vocabulário. O leitor encontra o termo num contexto em que ele é usado para justificar uma limitação do avião, sem ter como avaliar o argumento.

**Correção:** glosa inserida na primeira ocorrência, em aposto — *"subir e descer acompanhando a topografia para preservar a mesma distância ao terreno, em vez de voar num plano horizontal fixo"*. A definição posterior foi mantida, porque lá ela tem função diferente (contrastar drapeamento com altura barométrica constante).

### 🟡 DID-M16-A05-FECHAMENTO-006 — A última aula do módulo não fechava o módulo para o leitor
**Aula 05.**

As aulas 01 a 04 terminam com uma seção `## Próxima aula` que diz para onde se vai e por quê. A a05 simplesmente não tinha a seção — passava do recap direto para as fontes. Para quem estuda em sequência, isso é um beco sem saída: a aula acaba, e não há indicação de que o módulo terminou nem de para onde ir. A convenção do curso (verificada na aula 04 do Módulo 15) é que a última aula de um módulo mantém a seção, declarando o fim do módulo e apontando o módulo seguinte.

**Correção:** seção `## Próxima aula` acrescentada, declarando o fim do Módulo 16 e apontando o [[17-geofisica-marinha-bacias-sedimentares/17-geofisica-marinha-bacias-sedimentares-modulo|Módulo 17]] com a ponte conceitual (a lógica de campos potenciais e de plataforma móvel se mantém; troca-se o ar pela água e o alvo pontual pela arquitetura de bacia; e a sísmica, a grande ausente da aerogeofísica, entra como método principal). Link verificado — o arquivo de destino existe.

---

## Verificações que não geraram achado

- **Salto de pré-requisito:** nenhum. Toda referência ao Módulo 15 é explícita e nomeia a aula de origem. As referências internas ao módulo (a02 → a01 para estação-base e teste em oito; a04 → a01 para altura de voo; a05 → a02/a03/a04 na síntese) são todas para trás, nunca para frente, com uma exceção deliberada e sinalizada (a01 antecipa a gamaespectrometria da a04 ao justificar altura de voo baixa).
- **Excesso de conceitos novos por aula:** dentro do limite em todas as cinco. A aula mais carregada é a a04 (janelas de energia, quatro correções, mapa ternário, razão Th/U), mas três desses quatro blocos são **retomadas declaradas** do Módulo 15, o que reduz a carga real.
- **Objetivo declarado sem seção que o ensine:** verificado um a um contra o `mapa_objetivo_secao` de cada aula. Todos cobertos, salvo o caso DID-004 acima.
- **Analogia que ensina modelo mental errado:** nenhuma. A única analogia estrutural do módulo — correção de Eötvös : correção de latitude, na a03 — é legítima (ambas removem um efeito cinemático/geométrico previsível e calculável) e está corretamente delimitada.
- **Recap que não recapitula:** os cinco recaps foram conferidos linha a linha contra o corpo. Todos fiéis; três deles foram atualizados nesta passagem e na auditoria para refletir as correções.
- **Dificuldade desproporcional à posição no curso:** apropriada. O módulo é o 16º de um curso de especialização, com o Módulo 15 como pré-requisito imediato e efetivamente usado.
- **Redundância:** uma repetição introduzida pela própria auditoria (o teste de erro de rumo em oito descrito duas vezes em parágrafos consecutivos na a02) foi detectada e removida ainda nesta passagem.

## Encaminhamento ao orquestrador

**Hábito de geração sugerido, com base em três ocorrências (M14, M15, M16):** quando uma aula comparar **três ou mais alternativas por três ou mais atributos**, e essa comparação sustentar a decisão central da aula, gerar a tabela junto com a prosa — não em vez dela. Os três achados foram idênticos em forma e todos exigiram a mesma correção depois do fato.

## Notas para o questionário

- O par **"ordem obrigatória × ordem indiferente"** (a02, acréscimo desta passagem) é o melhor material conceitual novo do módulo e conversa diretamente com a cadeia de correções da a04. Questão de integração natural entre as duas aulas.
- A **tabela de plataformas** da a01 admite questão de aplicação direta ("dado este alvo e esta área, qual plataforma?") sem exigir nenhum número que a aula não publique.
- O **esquema de pipeline** da a04 é a forma de cobrar a sequência de correções sem transformar a questão em memorização cega: pedir a *justificativa* de uma posição na cadeia, não a lista.
