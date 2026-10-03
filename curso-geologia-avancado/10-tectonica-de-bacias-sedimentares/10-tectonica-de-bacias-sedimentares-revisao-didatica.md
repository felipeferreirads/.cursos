# Revisão didática — Módulo 10: Tectônica de bacias sedimentares

**Revisado em:** 2026-08-30 · **Modo:** `review-and-fix`
**Material:** `10-tectonica-de-bacias-sedimentares/` — 5 aulas (a01 a a05)
**Veredito:** **Bem ensinado com ressalvas**

## Resumo

🔴 0 bloqueiam · 🟠 2 prejudicam · 🟡 4 atrito · 🔵 1 sugestão

**Carga medida** (corpo de "## Conteúdo" até "## Erros comuns", contagem independente):

| Aula | Palavras | Conceitos novos | Exemplo trabalhado | Figura |
|---|---|---|---|---|
| a01 | 1918 | ~12 (bacia, acomodação, 4 mecanismos + topografia dinâmica, β, *backstripping*, flexura, rigidez flexural, *forebulge*, 4 regimes) | sim, **numérico** | sim |
| a02 | 1481 | ~7 (rifte, margem passiva, discordância de ruptura, *sag*/drifte, meio-graben, borda de falha vs. flexural, zona de acomodação, herança) | sim, interpretativo | sim |
| a03 | 1604 | ~7 (antepaís, 4 zonas deposicionais, retroarco, periférico, migração do depocentro, granocrescência) | sim, interpretativo | sim |
| a04 | 1955 | ~11 (*step-over* liberador/restritivo, *pull-apart*, falha de crescimento, índice de expansão, lístrica, arrasto reverso, *rollover*, diápiro, minibacia, *raft*, soldadura, descolamento) | sim, interpretativo | sim |
| a05 | 1594 | ~6 (inversão positiva/negativa, anticlinal de inversão, atenuação para cima, ciclo de Wilson, hábitat por regime, sal como modificador) | sim, interpretativo | sim |

A cadeia de pré-requisitos é **limpa e linear**: a01 → a02 → a03 → a04 → a05, cada aula declarando
o que consome da anterior e nenhuma usando conceito que não tenha sido ensinado ou declarado como
conhecimento externo. **Nenhum salto de pré-requisito foi encontrado** — o defeito mais grave e
mais comum, ausente aqui.

---

## Achados

### 🟠 1. A Aula 04 empilha três assuntos sem parentesco e não dizia qual é o fio

**id:** `DID-M10-A04-AMPLITUDE-001` · **Tipo:** amplitude temática / carga cognitiva
**Onde:** a04, aula inteira

**Problema.** A a04 é a aula mais larga do módulo (1955 palavras, ~11 conceitos novos) e cobre
**três famílias sem parentesco físico**: bacias *pull-apart* (cinemática de falhas
transcorrentes), falhas de crescimento (deslizamento gravitacional sob carga sedimentar) e
tectônica de sal (fluxo dúctil). O próprio título carrega um ponto-e-vírgula unindo dois blocos, e
o objetivo declarado é uma lista de três travessões — o sintoma clássico. Terminar *pull-apart*
não ajuda em nada a entender falha de crescimento: o aluno faz três partidas do zero em trinta
minutos. É a mesma patologia dos achados `DID-M09-A05-AMPLITUDE-002` e `DID-M08-EXTENSAO`.

**Decisão: ressalva justificada em vez de quebra**, seguindo o precedente dos Módulos 08 e 09.
Quebrar a a04 renumeraria a a05, invalidaria dois `content_hash`, obrigaria a reescrever links,
hub e travessias de pré-requisito da a05 — e, aqui, teria um custo extra que os módulos anteriores
não tinham: levaria o módulo de 5 para 6 aulas e **mudaria a decisão de questionário** registrada
abaixo. Custo alto para um problema de conforto, não de correção.

**Mitigação aplicada.** A costura que faltava foi feita: acrescentada a seção de abertura
**"O que une os três assuntos desta aula"**, que nomeia o fio condutor real — nas Aulas 01–03 o
espaço vinha de um mecanismo **litosférico e regional** (estirar, carregar); aqui os três casos
criam espaço por um mecanismo **local, controlado pela estrutura** (cinemática de falha, carga
sedimentar desigual, fluxo dúctil), com a consequência prática comum de que a geometria muda em
poucos quilômetros e não se deduz do regime de placas. O fio é genuíno, não retórico, e sustenta
as três seções. Custo: a a04 passou de ~1790 para 1955 palavras — no teto, mas dentro dele.

**Candidata a quebra futura**, se o usuário relatar fadiga: corte entre "Falhas de crescimento" e
"Tectônica de sal". A Parte 1 ficaria com *pull-apart* e falhas de crescimento (as duas de
controle por falha, com o vocabulário sinsedimentar herdado da a02 servindo às duas); a Parte 2
com tectônica de sal inteira, que já tem autonomia conceitual e o seu próprio exemplo trabalhado.

### 🟠 2. O objetivo `oa03` é ensinado na a02, mas a a02 não o credita

**id:** `DID-M10-OA03-MAPEAMENTO-002` · **Tipo:** desalinhamento aula–avaliação
**Onde:** a02 · `mapa_objetivo_secao`; e `course-state.yaml` · `covers_objectives` da a02

**Problema.** O `oa03` diz "interpretar o **controle do embasamento** e das estruturas
sin-sedimentares no preenchimento da bacia". A a02 tem uma seção chamada, literalmente,
**"Controle do embasamento sobre a geometria do rifte"** — a instância mais direta e mais
explícita desse objetivo em todo o módulo — e, apesar disso, o mapa de objetivos da a02 creditava
tudo ao `oa02`, e o estado listava só `oa02` em `covers_objectives`. O `oa03` aparecia como
propriedade exclusiva da a04.

**Por que importa (e não é só burocracia):** o gerador de questionários lê exatamente esse mapa.
Do jeito que estava, todas as questões de `oa03` sairiam da a04 — *pull-apart*, falha de
crescimento, sal — e a **herança estrutural do embasamento**, que é o que o objetivo nomeia em
primeiro lugar, ficaria sem nenhuma questão. O objetivo seria avaliado pela metade que ele
menciona por último.

**Correção aplicada** (metadado, sem tocar no texto da aula): o `mapa_objetivo_secao` da a02 foi
desdobrado — `oa02` recebe "Duas fases" + "meio-graben" + exemplo; `oa03` recebe "Controle do
embasamento" + "Preenchimento sin-rifte" + exemplo. O `covers_objectives` da a02 no
`course-state.yaml` passou a incluir `oa03`.

### 🟡 3. Contagens de palavras declaradas não correspondiam ao texto

**id:** `DID-M10-PALAVRAS-003` · **Tipo:** metadado enganoso

Os cinco `palavras_corpo` declarados eram quase uniformes (~1930 a ~2020), sugerindo cinco aulas
de peso equivalente. A contagem independente mostra variação de **32%** entre a mais leve e a mais
pesada (1481 na a02 contra 1955 na a04). É o padrão que a revisão do Módulo 09 elogiou por
ausência ("divergência máxima de 4 palavras… contra ~15% no Módulo 08") — aqui a divergência é
maior que a do Módulo 08. Não é defeito de aprendizado, mas corrompe a única métrica objetiva que
as revisões seguintes usam para julgar o orçamento de 30 minutos.

**Correção aplicada:** os cinco valores substituídos pela contagem medida, com o intervalo de
medição declarado explicitamente no próprio campo ("Conteudo ate Erros comuns, contagem medida"),
para que a próxima revisão compare a mesma coisa.

### 🟡 4. As cinco legendas de figura abriam itálico e nunca fechavam

**id:** `DID-M10-LEGENDAS-004` · **Tipo:** atrito de renderização

Todas as cinco legendas começavam com `*Leia…` / `*A ordem…` sem asterisco de fechamento. Em
Obsidian isso não vira itálico: vira um asterisco solto grudado na primeira palavra da legenda,
logo abaixo do diagrama — exatamente no ponto onde o olho vai depois de ler a figura. As aulas do
Módulo 09 usam legenda em texto corrido, sem marcação.

**Correção aplicada:** marcador removido nas cinco aulas, alinhando ao estilo da casa. Texto das
legendas inalterado.

### 🟡 5. A Aula 01 é a mais pesada do módulo, e é a primeira

**id:** `DID-M10-A01-CARGA-005` · **Tipo:** carga cognitiva / posição na progressão

A a01 tem o segundo maior corpo (1918 palavras) e a **maior densidade de vocabulário novo** do
módulo — cerca de doze conceitos independentes, incluindo quatro mecanismos de subsidência, uma
quinta influência (topografia dinâmica), β, *backstripping*, rigidez flexural, *forebulge*, o
esquema de classificação inteiro e o vocabulário de terminação de estratos. Tudo isso antes de o
leitor ter qualquer apoio concreto, porque é a primeira aula.

**Não corrigido, deliberadamente, e o motivo importa.** A correção certa para sobrecarga é
dividir, não explicar mais — encher a a01 de esclarecimento pioraria exatamente o que se quer
resolver. E dividir a a01 é a pior candidata do módulo: ela é a aula-mapa, e separar os mecanismos
de subsidência da classificação por regime que eles justificam quebraria o único par que precisa
ser lido junto. A densidade aqui é o preço de ter uma aula-mapa, e a aula a paga bem: os quatro
mecanismos vêm numerados, com uma figura e um exemplo numérico. Registrado para que o gerador
saiba que a a01 é a aula de maior densidade do módulo — e, se houver fadiga relatada, o candidato
a corte é a seção "Geometria e arquitetura", que **antecipa** a02–a04 em vez de ensinar algo que
só a a01 pode ensinar.

### 🔵 6. Quatro dos cinco exemplos trabalhados têm forma idêntica

**id:** `DID-M10-EXEMPLOS-006` · **Tipo:** sugestão / variedade de prática

Os exemplos das aulas 02, 03, 04 e 05 têm todos o mesmo molde: "uma seção sísmica (ou um
levantamento) mostra (i), (ii), (iii) — identifique os elementos e explique". É um molde bom, e
é de fato o gesto profissional da disciplina. Mas só a a01 tem aritmética, e o módulo ensina
várias grandezas calculáveis que nunca são calculadas: taxa de subsidência, fator β, índice de
expansão de falha de crescimento, fator de amplificação por carga sedimentar (~2,8), razão
comprimento/largura de *pull-apart*.

**Não corrigido no texto:** trocar um exemplo trabalhado exigiria conteúdo factual novo que não
passou pela auditoria — fora do escopo desta skill. **Encaminhado ao gerador de questionários**
(ver abaixo).

---

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo | Observação |
|---|---|---|---|
| `oa01` — mecanismos de subsidência | a01 ("O que é uma bacia sedimentar", "Os mecanismos de subsidência") | sim, numérico | coberto por inteiro numa aula só |
| `oa02` — classificar por regime, geometria e arquitetura | a01 ("mapa mental", "Geometria e arquitetura"), a02, a03 | sim (3×) | o objetivo mais espalhado do módulo — atravessa três aulas |
| `oa03` — controle do embasamento e das estruturas sin-sedimentares | a02 ("Controle do embasamento", "Preenchimento sin-rifte"), a04 | sim (2×) | **crédito da a02 restaurado** nesta revisão (achado 2) |
| `oa04` — inversão e hábitat do petróleo | a05 (aula inteira) | sim | objetivo duplo, coberto por uma aula só; é a aula de síntese |

**Nenhum objetivo sem seção que o ensine. Nenhuma seção órfã.** Todas as seções substanciais das
cinco aulas servem a um objetivo declarado.

---

## Recomendação de avaliação: **questionário ÚNICO cumulativo**

Decisão: **um questionário só, cumulativo, cobrindo as cinco aulas.** Sem parciais.

Aplicação do critério fixado no Módulo 06 e reafirmado no 09 — parciais quando o módulo é grande
**e** existe corte conceitual natural que nenhum objetivo atravessa. Aqui as duas condições falham,
e a segunda falha de forma decisiva:

1. **Tamanho.** Cinco aulas, abaixo do limiar de ~5–6 que aciona parciais. Alinha com os Módulos
   02, 03, 04 e 07 (4–5 aulas, questionário único) e não com os Módulos 06, 08 e 09 (6 aulas,
   parciais + final).

2. **Nenhum corte limpo existe** — este é o argumento de peso, e é o inverso exato do que decidiu
   o Módulo 09, onde nenhum objetivo atravessava o corte. Aqui **todo corte candidato parte um
   objetivo ao meio**:
   - corte a01–a02 / a03–a05 → parte `oa02` (a01, a02 | a03) **e** `oa03` (a02 | a04);
   - corte a01–a03 / a04–a05 → parte `oa03` (a02 | a04);
   - qualquer corte antes da a05 → **estranha a aula de síntese**, que existe justamente para
     integrar os quatro regimes e não tem sentido isolada numa parcial.

3. **A estrutura do módulo é radial, não sequencial.** a01 é o mapa, a02–a04 são os três regimes
   pendurados nele, e a05 fecha voltando ao mapa. Uma parcial cortaria no meio dos raios. A
   pergunta que o módulo inteiro ensina a fazer — "que regime gerou o espaço aqui, e o que isso
   implica?" — só é avaliável cumulativamente.

**Razão que NÃO se aplica aqui**, registrada para que a decisão não seja lida como automática: no
Módulo 08 um dos argumentos para parciais foi o excesso de palavras por aula. Aqui a a04 e a a01
encostam no teto (1955 e 1918), mas nenhuma o excede, e as contagens agora são honestas (achado 3)
— a decisão se sustenta na estrutura de objetivos, não no volume.

### Encaminhamentos ao gerador de questionários

- **Inclua ao menos duas questões de cálculo** (`DID-M10-EXEMPLOS-006`): o módulo é quase todo
  qualitativo, e as grandezas existem. Candidatas: taxa de subsidência a partir de espessura e
  duração (a01, tem exemplo pronto); fator de amplificação da carga sedimentar (~2,8, a01);
  índice de expansão de falha de crescimento (a04).
- **Cubra `oa03` pelos dois lados** (`DID-M10-OA03-MAPEAMENTO-002`): herança estrutural do
  embasamento e zonas de acomodação (a02) **e** estruturas sinsedimentares (a04). Não deixe o
  objetivo inteiro sair da a04.
- **Não distribua as questões da a04 uniformemente pelas três famílias**
  (`DID-M10-A04-AMPLITUDE-001`): tectônica de sal é o que o resto do curso consome (M11
  sismoestratigrafia, M12 engenharia de petróleo, e a própria a05) e merece peso; *pull-apart*
  vale uma questão de reconhecimento.
- **A a05 é a matéria natural de integração** — é a aula que já pensa em módulo. Puxe dela as
  questões que compõem duas aulas anteriores.
- **Consulte as dez advertências no fim da auditoria científica**, que listam o que mudou nas
  correções. Quatro delas são distratores de primeira qualidade justamente porque o erro corrigido
  era o que o senso comum sugere: rollover mergulha para a falha; inversão levanta a geradora; o
  antepaís não deformado não é uma zona deposicional; borda flexural não é o alto de *footwall*.

---

## O que está bem feito

- **Cadeia de pré-requisitos limpa e explícita.** Cada aula declara o que consome da anterior, no
  cabeçalho e no bloco "Antes de começar". Nenhum salto. Num módulo cuja aula final depende das
  quatro anteriores, isso não é pouco.
- **Todas as cinco aulas têm figura, e cada figura ensina algo que o texto sozinho não ensinaria**
  — a curva de subsidência, a assimetria do meio-graben, a ordem espacial das zonas de antepaís,
  a geometria do *step-over*, a atenuação para cima do anticlinal de inversão. Em todos os casos a
  ideia é intrinsecamente geométrica, e o diagrama é a forma certa de dizê-la.
- **A dupla "Erros comuns" + "O que não concluir" é usada com disciplina nas cinco aulas**, e são
  seções genuinamente distintas: a primeira lista confusões, a segunda lista generalizações
  indevidas. A segunda é rara em material autodidata e é o que impede o aluno de sair com regras
  falsas ("todo folhelho lacustre implica rifte", "toda margem passiva antiga será invertida").
- **Os cinco recaps destilam em vez de repetir.** Nenhum recicla frases do corpo.
- **A a05 fecha o módulo voltando à pergunta organizadora da a01**, e o faz explicitamente no
  "Encerramento do módulo". O módulo tem começo e fim, não só uma sequência de aulas.
- **O nível é consistente** entre as cinco aulas: mesmo registro, mesma densidade de termo técnico
  destacado, mesma disposição de nomear a literatura quando ela importa e de omiti-la quando não.
