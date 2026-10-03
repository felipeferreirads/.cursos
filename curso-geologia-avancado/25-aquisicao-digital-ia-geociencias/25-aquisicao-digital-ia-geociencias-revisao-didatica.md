# Revisão didática — Módulo 25: Aquisição de dados digitais e inteligência artificial em geociências

**Revisado em:** 2026-09-21 · **Modo:** `review-and-fix`
**Material:** `25-aquisicao-digital-ia-geociencias/` (5 aulas + hub)
**Ordem respeitada:** roda **depois** da auditoria científica, concluída e aprovada no mesmo dia (veredito aprovado, 0 achados 🔴/🟠/🟡 em aberto).
**Veredito:** **Bem ensinado com ressalvas**

## Resumo

🔴 0 bloqueiam · 🟠 3 prejudicam · 🟡 5 atrito · 🔵 2 sugestões

**Nenhum achado vermelho.** Nenhum salto de pré-requisito, nenhum termo central indefinido, nenhum objetivo não ensinado, nenhum salto lógico em exemplo trabalhado. A progressão interna do módulo (campo → tipos de dado → interpretação → banco → IA) é das mais limpas do curso: cada aula usa explicitamente o que a anterior entregou, e as cinco encadeiam sem lacuna.

## Decisão de divisão: NÃO dividir, e por quê

A tarefa pedia para dividir aula sobrecarregada se necessário. **Não é necessário**, e a decisão está fundamentada em contagem, não em impressão.

Recontagem do corpo (`## Conteúdo` a `## Fontes`, com código, sem os títulos de seção), na métrica de ~84 palavras/min usada nas revisões didáticas dos Módulos 22, 23 e 24, **depois** das correções da auditoria e desta revisão:

| Aula | Palavras | Duração | Seções | Exemplos | Objetivo |
|---|---|---|---|---|---|
| 01 — Aquisição digital em campo | 2.288 | ~27,2 min | 5 | 2 | oa01 |
| 02 — Tipos e organização de dados | 2.264 | ~27,0 min | 9 | 2 | oa02 |
| 03 — Estereoscopia e interpretação integrada | 2.443 | **~29,1 min** | 5 | 2 | oa03 |
| 04 — Bancos de dados, Big Data, FAIR | 2.122 | ~25,3 min | 7 | 2 | oa02 + oa04 |
| 05 — IA aplicada | 2.217 | ~26,4 min | 5 | 2 | oa04 |
| **Módulo** | **11.334** | **~135 min** | 31 | 10 | 4/4 cobertos |

**Nenhuma aula acima do teto de 30 min.** Contraste que vale registrar: nos Módulos 23 e 24 foram as correções da auditoria que empurraram aulas de "no limite" para "acima do limite", forçando três divisões. Aqui as correções da auditoria acrescentaram 167 palavras à Aula 03 e 59 à Aula 04, e **nenhuma das duas chegou ao teto**.

A Aula 03 está dentro do teto **mas perto dele** (~29,1 min), na mesma situação em que a Aula 04 do Módulo 22 ficou depois da divisão. Se uma edição futura a empurrar acima de 30, o corte natural já está identificado e é limpo: **"como ver" (anaglifo, exagero vertical, pseudoscopia, fontes de MDT, armadilha da iluminação) | "o que concluir" (hierarquia de quatro níveis, lineamento como hipótese, integração das três fontes)**, com o exemplo trabalhado 1 (três pontos) indo para a primeira metade e o 2 (dados axiais) para a segunda — as duas metades já têm um exemplo cada, que é o sinal de que o corte é viável. **Não foi executado agora**, porque dividir uma aula que cabe no teto e serve a um objetivo único fragmentaria `oa03` sem ganho.

A Aula 02 é a que tem mais seções (9) e seria a candidata óbvia por contagem de itens. Ela **não** foi dividida, e a razão é estrutural: as sete famílias de dados são **paralelas**, não aninhadas — todas instanciam o mesmo esquema (unidade de observação + armadilha típica), anunciado numa tabela antes das subseções. O custo cognitivo da sétima família é baixo depois da terceira. O que de fato pesava nela não era a quantidade de famílias, e sim um conceito difícil que viajava de carona sem apoio (achado 2).

## Achados

### 🟠 1. O aparato central da Aula 05 entregue num parágrafo monolítico

**claim_id:** `DID-M25-A05-CARGA-METALOGENETICO-001`
**Tipo:** sobrecarga localizada / abstração sem apoio estrutural
**Onde:** Aula 05 · "O papel do modelo metalogenético: escolher o que o algoritmo vê"
**Problema:** um único parágrafo de cerca de 340 palavras, sem quebra e sem lista, carregava: o problema das 60 camadas com 30 depósitos; os quatro componentes do sistema mineralizador; uma cadeia de atribuição com quatro trabalhos citados; **o processo de tradução em quatro passos**; três exemplos de proxy remetendo às Aulas 02 e 03; a escolha do modelo por província com dois tipos de depósito; e a não transferibilidade. O processo de quatro passos é o aparato de que o objetivo `oa04` depende — é o que transforma modelo genético em camada de banco de dados — e estava enunciado em prosa corrida, entre parênteses de citação, na posição em que o leitor já perdeu o fio. Um leitor de primeira viagem sai da seção sabendo que "o modelo decide as camadas" e **sem conseguir reproduzir os quatro passos**, que é justamente o que a avaliação vai cobrar.
**Correção aplicada:** parágrafo quebrado em cinco; os quatro passos promovidos de prosa a **lista numerada**, com a glosa curta de cada um; a frase-chave ("o modelo decide as camadas; o algoritmo decide os pesos") movida para a abertura da seção, onde serve de âncora, em vez de aparecer no fim como conclusão; a frase de transição "só que ter o modelo genético não basta" acrescentada para explicitar por que McCuaig et al. entram. **Nenhum fato novo**: os quatro passos já estavam no texto, palavra por palavra, e foram verificados na auditoria (item azul B2).
**Escopo:** correção local.

### 🟠 2. Fechamento composicional: conceito pesado de carona, sem apoio e sem destino

**claim_id:** `DID-M25-A02-FECHAMENTO-ORFAO-002`
**Tipo:** conceito difícil sem exemplo · pré-requisito prometido inexistente
**Onde:** Aula 02 · "Geoquímica: valores, unidades e limites de detecção"
**Problema:** três sentenças introduziam dados composicionais, a não independência por fechamento em 100%, a tradição de Aitchison e as razões logarítmicas — sem um único exemplo concreto do efeito, sem dizer o que o aluno deve **fazer** com a informação, e remetendo a uma matriz de correlação do Módulo 24. Duas agravantes que só aparecem olhando o curso inteiro: (i) **nenhuma aula deste curso desenvolve razões logarítmicas** — verificado por varredura em todos os módulos —, de modo que o aluno fica esperando um desenvolvimento que nunca chega; (ii) a censura, que é o conceito vizinho e de dificuldade comparável, recebe texto **mais** um exemplo trabalhado inteiro e volta na Aula 05, o que torna o contraste de tratamento visível dentro da própria seção. Ao lado de um conceito bem ensinado, o mal ensinado fica mais confuso, não menos.
**Correção aplicada:** (i) o mecanismo ficou concreto em uma oração — se a sílica sobe, algo tem de descer, e as duas colunas aparecem anticorrelacionadas sem que nada geológico as ligue; (ii) o ponto foi **explicitamente rebaixado a alerta, não técnica**, dizendo que o tratamento por razões logarítmicas está fora do escopo do curso e que nenhuma aula adiante o desenvolve; (iii) a instrução operacional passou a ser dita ("ao ver uma matriz de correlação de elementos maiores em % de óxido, parte do que ela mostra é artefato, e a conclusão precisa dizer isso"); (iv) o porquê do efeito ser menor nos traços ficou explícito (somam fração ínfima do total).
**Nota de fronteira com a auditoria:** as duas elaborações concretas são desdobramentos de afirmações **já presentes e já verificadas** (`DIGGEO-M25-A02-COMPOSICIONAL-004` e item azul B15), não fato novo. A alegação de que o curso não desenvolve o tema é sobre o próprio curso e foi conferida nos arquivos.
**Escopo:** correção local. *Se o tema devesse ser ensinado de verdade, seria aula nova num módulo de estatística geoquímica — fora do escopo deste módulo, registrado aqui como decisão consciente e não como omissão.*

### 🟠 3. Pico de densidade na integração das três fontes, agravado pela correção da auditoria

**claim_id:** `DID-M25-A03-DENSIDADE-INTEGRACAO-003`
**Tipo:** densidade irregular · digressão para conteúdo de outro módulo
**Onde:** Aula 03 · "Integrar as três fontes: a lógica da coincidência"
**Problema:** o terceiro marcador da lista acumulava, num só parágrafo: o que a aerogeofísica mede (duas coisas), três filtros de realce de borda nomeados com referência, a instabilidade da redução ao polo em baixa latitude e — depois do achado laranja 8 da auditoria — a distinção entre o sinal analítico 2D e 3D com uma quarta referência. Seis ideias, três delas de conteúdo dos Módulos 16 e 19, dentro de um marcador cujo trabalho era apenas dizer *o que cada fonte enxerga*. **Esta revisão reconhece que a correção da auditoria, factualmente necessária, criou o pico**: a ressalva é certa e tinha de entrar, mas entrou no pior lugar possível, no meio de uma enumeração paralela onde o leitor está comparando três fontes lado a lado.
**Correção aplicada:** o marcador voltou a fazer só o seu trabalho (o que a aerogeofísica mostra, com um ponteiro). Os três filtros e a ressalva 2D/3D saíram para uma **nota destacada** logo abaixo, com título próprio, dizendo de saída que o cálculo é dos Módulos 16 e 19 e que aqui basta saber o que esperar e a ressalva — isto é, sinalizando ao leitor que aquilo é **ressalva a arquivar, não técnica a aprender agora**. Nenhuma palavra de conteúdo factual foi removida; o texto foi reposicionado e enquadrado.
**Escopo:** correção local.

### 🟡 4. Ordem invertida na seção de padrões: contabilidade de estatuto antes do porquê

**claim_id:** `DID-M25-A04-ORDEM-PADROES-004`
**Tipo:** abstração antes do concreto (ordem interna)
**Onde:** Aula 04 · "Padrões de interoperabilidade"
**Problema:** depois dos achados 3 e 9 da auditoria, a seção passou a abrir com cerca de 150 palavras de estatuto de padrão (quem é OGC, quem é CGI, o que o INSPIRE obriga, que esquema fica fora das regras de implementação) e só **terminava** com a razão de tudo aquilo existir — que "granito" tenha definição publicada e identificador estável. O leitor atravessava a contabilidade sem saber para que serve, que é a receita conhecida para não retê-la.
**Correção aplicada:** a razão passou ao **primeiro parágrafo**, junto com a apresentação dos dois padrões; a contabilidade de estatuto ficou no segundo, agora lida como consequência de uma pergunta já formulada. Acrescentada, no fecho, a lição de método que sobrevive à mudança de versão: antes de citar um padrão, confira de quem ele é e o que obriga. Conteúdo idêntico, ordem invertida.
**Escopo:** correção local.

### 🟡 5. Meta-comentário sobre o plano do curso interrompendo o primeiro framework do módulo

**claim_id:** `DID-M25-A01-METACOMENTARIO-005`
**Tipo:** atrito / ruído de bastidor em posição crítica
**Onde:** Aula 01 · "O fluxo escritório, campo, banco"
**Problema:** dois parênteses longos — 43 e 35 palavras — explicavam que o plano do curso escreve "GIS-Pro" e "FieldClino", que o primeiro não é nome de produto e que o segundo se chama FieldMove Clino. O conteúdo é legítimo (a auditoria o registrou como decisão editorial declarada, e ela **não** foi desfeita), mas a **posição** era ruim: o primeiro deles caía dentro do passo 1 de 3 do primeiro framework do módulo inteiro, de modo que a primeira coisa que o aluno lê sobre preparação de campanha é uma nota de rodapé sobre o vocabulário interno do curso.
**Correção aplicada:** os passos e o parágrafo de ferramentas ficaram limpos; o esclarecimento de nomenclatura foi **preservado integralmente** numa nota destacada depois do parágrafo, onde cumpre a mesma função sem cortar a exposição. Nada do que a auditoria decidiu manter foi removido.
**Escopo:** correção local.

### 🟡 6. Pré-requisito do Módulo 20 declarado sem dizer o que se reativa

**claim_id:** `DID-M25-A05-PREREQ-M20-006`
**Tipo:** pré-requisito declarado sem reativação
**Onde:** Aula 05 · cabeçalho
**Problema:** o cabeçalho dava ao Módulo 24 um parêntese detalhado (fluxo de trabalho, floresta aleatória, matriz de confusão, validação cruzada, vazamento espacial) e ao Módulo 20 um **link nu**. Um pré-requisito que não diz o que se deve lembrar não é reativado: ou o aluno relê o módulo inteiro, ou o ignora — e na prática ignora. Pior, o conteúdo do Módulo 20 é exatamente o que sustenta o exemplo trabalhado 2 desta aula.
**Correção aplicada:** nomeado o que se reativa — a noção de **continuidade espacial** (amostras próximas se parecem, e o quanto se parecem tem alcance mensurável) — com a razão de ela importar aqui: é ela que torna a validação por blocos necessária, e não uma preciosidade. Conteúdo do Módulo 20 conferido nos arquivos (aulas 02 e 04).
**Escopo:** correção local.

### 🟡 7. Erro de concordância em frase de definição

**claim_id:** `DID-M25-A04-CONCORDANCIA-007`
**Tipo:** atrito de redação
**Onde:** Aula 04 · "Modelagem relacional"
**Problema:** "Regras de **normalização** manda não repetir o mesmo fato" — sujeito plural, verbo singular, numa frase que define um conceito. Encaminhado pela auditoria científica como observação fora do escopo dela.
**Correção aplicada:** "As regras de **normalização** mandam não repetir...".
**Escopo:** correção local.

### 🟡 8. Duração declarada e contagem de palavras desatualizadas em todas as cinco aulas

**claim_id:** `DID-M25-MOD-METADADOS-CARGA-008`
**Tipo:** metadado que desinforma quem planeja a sessão de estudo
**Onde:** cabeçalho e bloco de metadados das cinco aulas
**Problema:** o campo `palavras_corpo` era o da redação e não refletia as correções da auditoria; e a **duração declarada no cabeçalho** — que é o número que o aluno usa para decidir se abre a aula agora — estava errada em três aulas, com a Aula 03 anunciando ~24 min para um corpo de ~29 min. Errar 5 minutos numa aula de 30 é errar um sexto da sessão. O mesmo defeito foi levantado na revisão didática do Módulo 24.
**Correção aplicada:** `palavras_corpo` recontado nas cinco (2.288 / 2.264 / 2.443 / 2.122 / 2.217) e duração declarada alinhada (~27 / ~27 / ~29 / ~25 / ~26 min). Método de contagem declarado nesta revisão, para ser refeito igual no futuro.
**Escopo:** correção local.

## Sugestões não aplicadas

### 🔵 9. Dois pontos intrinsecamente geométricos existem só em prosa

**claim_id:** `DID-M25-A03-SUGESTAO-VISUAL-009`
A percepção de relevo por paralaxe e o viés de iluminação (feição paralela ao sol que desaparece) são fenômenos **visuais** ensinados apenas com palavras, numa aula cujo tema é olhar imagens. Um par de esquemas — deslocamento de paralaxe em função da altitude, e o mesmo lineamento sob dois azimutes de sol — valeria mais que os parágrafos. **Não implementado:** exigiria produzir figura ou código novo, gerando conteúdo que não passou pelo auditor científico. Mesma decisão tomada no Módulo 24 (`DID-M24-MOD-SUGESTAO-VISUAL-009`).

### 🔵 10. O fio da censura é o melhor material de questão de aplicação do módulo

**claim_id:** `DID-M25-A02A05-SUGESTAO-AVALIACAO-010`
O tratamento de valores censurados atravessa o módulo com três aparições encadeadas e crescentes: a convenção de registro (Aula 02, texto), o efeito quantitativo da substituição (Aula 02, exemplo trabalhado 2, com médias de 10,50 a 13,00 ppb sobre as mesmas análises) e a contaminação do treino de um modelo (Aula 05, limitação final). É o único fio do módulo que percorre três aulas com a mesma variável e ganha consequência a cada passo — material ideal para uma questão de aplicação que peça ao aluno prever o efeito da convenção sobre um modelo, não recitar a definição. **Encaminhado ao `gerador-de-questionarios`.** Não é correção; nada foi alterado.

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo trabalhado | Avaliado em |
|---|---|---|---|
| `oa01` — Operar ferramentas de aquisição digital e avaliar vantagens e limitações frente à caderneta | Aula 01, seções 2 a 5 | sim (2: declinação; média de polos) | questionário pendente |
| `oa02` — Organizar e integrar tipos distintos de dados numa base consistente | Aula 02 (integral) + Aula 04, seções "Modelagem relacional" e "Padrões" | sim (4: junção/censura; média sob convenções; SQL com restrições; diagnóstico FAIR) | questionário pendente |
| `oa03` — Interpretar estruturas hierarquicamente a partir de estereoscopia, MDT, sensoriamento e aerogeofísica | Aula 03 (integral) | sim (2: três pontos; média axial) | questionário pendente |
| `oa04` — Avaliar aplicações de Big Data e IA ao mapeamento, à exploração e a modelos metalogenéticos | Aula 04, seções "Big Data", "FAIR", "Reprodutibilidade" + Aula 05 (integral) | sim (2: pesos de evidência; validação espacial) | questionário pendente |

**4 de 4 objetivos cobertos, todos com pelo menos um exemplo trabalhado.** Nenhum conteúdo órfão: as 31 seções do módulo mapeiam todas para um dos quatro objetivos, conforme o campo `mapa_objetivo_secao` de cada aula, conferido seção a seção.

Os quatro objetivos são **verificáveis** (operar, organizar, interpretar, avaliar) — nenhum formulado com "entender" ou "conhecer". A ressalva possível é `oa04`, cujo verbo "avaliar" abrange desde diagnosticar falhas FAIR até criticar um mapa de prospectividade; ele é servido por duas aulas, o que é adequado, mas é o objetivo que mais exige do questionário para ser demonstrado. **Encaminhado**: `oa04` merece questões nas duas metades, não só na Aula 05.

## Alinhamento com a avaliação

Não há questionário nem baralho de flashcards ainda — a revisão correu antes deles, que é a ordem certa. **Nada a desalinhar, e nada a corrigir aqui.** Os dois encaminhamentos acima (achado 10 e a ressalva de `oa04`) são as entradas que esta revisão deixa para o `gerador-de-questionarios`.

## O que está bem feito

Específico, porque precisa ser preservado nas próximas revisões:

- **A progressão entre as cinco aulas é a mais limpa do curso até aqui.** Cada aula abre reativando nominalmente o que a anterior entregou, e cada "Próxima aula" anuncia o problema que a seguinte resolve, não só o assunto dela. A Aula 04 chega dizendo "com dados de campo (Aula 01), dados analíticos (Aula 02) e interpretações (Aula 03) em mãos" — isso é andaime explícito, e funciona.
- **O módulo ensina a desconfiar de instrumento, e o faz com método.** Três armadilhas de primeira ordem — a casa decimal que não é precisão (Aula 01), espaçamento de pixel que não é resolução (Aula 03), "sem depósito conhecido" que não é "sem depósito" (Aula 05) — têm a mesma forma lógica e são apresentadas cada uma no seu contexto, sem serem chamadas de padrão. O aluno sai com o reflexo, não com a regra.
- **Os dez exemplos trabalhados exercitam o que a aula ensina, e cada aula tem dois.** Nenhum é decorativo e nenhum exercita só metade da aula — que foi exatamente o sintoma diagnóstico das divisões nos Módulos 22, 23 e 24. Vários vão além do cálculo e ensinam a **ler** o resultado: o "Cuidado com o que esse resultado não diz" da Aula 01 (coesão mede precisão, não exatidão) e as "Limitações que o exemplo esconde" da Aula 05 são o melhor ensino do módulo.
- **A divergência entre fontes é tratada como conteúdo, não escondida.** A Aula 01 ensina que dois estudos no mesmo periódico chegam a conclusões opostas sobre celulares como bússola, e extrai a lição operacional certa (afere-se, não se presume). Uma aula pior escolheria um lado.
- **Os recaps destilam em vez de repetir.** Os cinco condensam, trazem os números decisivos e não copiam frases do corpo — inclusive o da Aula 05, que reduz cinco limitações a duas linhas sem perder nenhuma.
