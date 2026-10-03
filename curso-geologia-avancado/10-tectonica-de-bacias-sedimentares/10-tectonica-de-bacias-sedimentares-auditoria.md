# Auditoria científica — Módulo 10: Tectônica de bacias sedimentares

**Auditado em:** 2026-08-30 · **Modo:** `audit-and-fix` · **Profundidade:** `full`
**Material:** `10-tectonica-de-bacias-sedimentares/` — 5 aulas (a01 a a05)
**Veredito:** **Aprovado com correções aplicadas** — nenhum achado 🔴 ou 🟠 em aberto.

## Resumo

🔴 6 erros · 🟠 12 imprecisos · 🟡 0 desatualizados · 🔵 1 sem fonte · ⚪ 0 controversos

**Total: 19 achados.** As 22 alegações auditáveis declaradas pelas aulas foram usadas como
ponto de partida e todas reverificadas contra fonte; **12 dos 19 achados estão fora da lista
declarada** — inclusive quatro dos seis vermelhos. A lista do autor cobriu a substância
central e acertou nela; o que escapou foi, quase sem exceção, **nomenclatura e sentido de
efeito** — o tipo de erro que o autor não classifica como "de risco" porque acredita estar
apenas traduzindo.

**Padrão dominante dos achados:** três dos seis vermelhos são *inversões de sentido* — o
texto afirma o contrário do que a fonte diz, com a direção certa e o sinal errado
(mergulho do rollover, efeito da inversão sobre a maturação, plano da falha normal). São os
mais perigosos porque soam plausíveis e produzem flashcards exatamente errados.

---

## Achados 🔴

### 🔴 1. Rótulo "falhas selantes" para falhas truncadas pela discordância

**claim_id:** `BACIAS-M10-A02-SELANTE-101` · **Tipo:** erro factual (nomenclatura)
**Onde:** a02 · Exemplo trabalhado
**Estava escrito:** "falhas que morrem para cima ('falhas selantes', que não afetam as camadas mais jovens)"
**Problema:** "falha selante" é termo definido da geologia de petróleo e designa outra coisa —
uma falha que **barra o fluxo de fluido**, por justaposição ou por *fault gouge*. Nada a ver com
o fato de a falha ser truncada por uma discordância. Agravante curricular: a a05 deste mesmo
módulo ensina selo e armadilha, então o aluno encontra o termo duas vezes com sentidos
incompatíveis, dentro do mesmo módulo.
**Correção aplicada:** trocado por "falhas **truncadas** pela discordância", com advertência
explícita de não confundir com "falha selante", remetendo à a05.
**Confiança:** confirmado.

### 🔴 2. Alto de *footwall* chamado de "borda flexural"

**claim_id:** `BACIAS-M10-A02-FLEXURAL-102` · **Tipo:** erro factual (nomenclatura estrutural)
**Onde:** a02 · "A unidade estrutural fundamental: o meio-graben", figura, recap e manifesto
**Estava escrito:** "o lado do muro, ou *footwall*, que muitas vezes forma um alto estrutural
erguido, uma 'borda flexural' ou *flexural margin*"
**Problema:** a **borda flexural** é a margem **oposta** à falha principal — a rampa de mergulho
suave do próprio bloco do teto, com dobradiça e *onlap*. O alto de *footwall* é a **borda de
falha** (*border-fault margin*, margem de escarpa), e forma o ombro do rifte. O texto fundia as
duas margens opostas do meio-graben numa só, destruindo justamente a assimetria que a seção
existe para ensinar.
**Correção aplicada:** as duas bordas separadas explicitamente no corpo, com a advertência de
que são margens opostas; **figura ASCII redesenhada** (estava rotulada de forma coerente com o
erro); recap e claim `BACIAS-M10-A02-MEIOGRABEN-002` reescritos; Gawthorpe & Leeder 2000
acrescentada às fontes.
**Fonte:** Gawthorpe & Leeder (2000), *Basin Research* 12; Schlische & Olsen (1991) · **Nível:** revisada por pares
**Confiança:** confirmado.

### 🔴 3. Compartimentos do sistema de antepaís em desacordo com DeCelles & Giles (1996)

**claim_id:** `BACIAS-M10-A03-DEPOZONES-103` · **Tipo:** erro factual + inconsistência interna
**Onde:** a03 · "Os quatro compartimentos de uma bacia de antepaís", legenda, recap, exemplo trabalhado
**Estava escrito:** lista de quatro itens: (1) antepaís proximal = *wedge-top* **e** *foredeep*
fundidos, (2) *forebulge*, (3) *back-bulge*, (4) antepaís não deformado
**Problema:** DeCelles & Giles (1996) — citado pela própria aula como a fonte do esquema —
definem exatamente quatro **zonas deposicionais**: *wedge-top*, *foredeep*, *forebulge*,
*back-bulge*. O antepaís não deformado **não é uma delas**: é justamente o que fica fora do
sistema. A aula fundiu duas zonas reais e promoveu a não-zona a compartimento, contradizendo
ao mesmo tempo a fonte citada e **o seu próprio manifesto de alegações**
(`BACIAS-M10-A03-COMPARTIMENTOS-002`, que lista as quatro corretas).
**Correção aplicada:** lista reconstruída com as quatro zonas de DeCelles & Giles, cada uma com
a sua definição; parágrafo acrescentado dizendo explicitamente que o antepaís não deformado
não é uma quinta zona; legenda da figura, recap e exemplo trabalhado realinhados.
**Fonte:** DeCelles & Giles (1996), *Basin Research* 8(2), p. 105–123 · **Nível:** revisada por pares
**Confiança:** confirmado.

### 🔴 4. Bacia do Amazonas oriental apresentada como antepaís de retroarco andino

**claim_id:** `BACIAS-M10-A03-AMAZONAS-104` · **Tipo:** erro factual
**Onde:** a03 · "Dois arranjos de placas" + manifesto
**Estava escrito:** "A Bacia do Antepaís Andino (…) incluindo a Bacia do Chaco e a **Bacia do
Amazonas oriental** em fases pretéritas de sua história"
**Problema:** errado duas vezes. (a) A Bacia do Amazonas é uma bacia **intracratônica
paleozoica**, não um antepaís andino — e a porção *oriental* é a mais distante possível dos
Andes. (b) O antepaís de retroarco andino no Brasil é a **Bacia do Acre** (antepaís amazônico
ocidental), e sua fase de antepaís é **neógena a atual**, não "pretérita". O erro inverte a
geografia e a cronologia ao mesmo tempo.
**Correção aplicada:** substituído por "Bacia do Chaco, bacias subandinas e, no Brasil, a Bacia
do Acre — o antepaís amazônico ocidental, instalado a partir do Neógeno"; claim
`BACIAS-M10-A03-RETROARCO-PERIFERICO-003` atualizado com a ressalva explícita de que a Bacia
do Amazonas não integra o sistema.
**Fonte:** Oliveira et al. (2023), *Basin Research* 35 (transição intracratônica → antepaís de
retroarco na Bacia do Acre); Wanderley Filho et al., em *Amazonia: Landscape and Species
Evolution* (Wiley, 2010) · **Nível:** revisada por pares
**Confiança:** confirmado.

### 🔴 5. Falha normal descrita como tendo plano vertical

**claim_id:** `BACIAS-M10-A04-PLANO-105` · **Tipo:** erro factual + inconsistência interna
**Onde:** a04 · "Antes de começar, você precisa saber"
**Estava escrito:** "ao contrário de falhas normais (**verticais**, extensão) e inversas (compressão)"
**Problema:** falhas normais têm plano **inclinado**, tipicamente da ordem de 60° (Anderson);
plano vertical é justamente a característica da transcorrente, que a frase estava tentando
contrastar — ou seja, o contraste se anula. Agravante de inconsistência interna: a a02, no bloco
equivalente, diz corretamente "ao longo de um plano de falha **inclinado**". Alta visibilidade:
está num bloco de pré-requisito, a primeira coisa que o aluno lê.
**Correção aplicada:** reescrito com os dois mergulhos típicos (normal ~60°, inversa de baixo
ângulo) e com a componente vertical do deslocamento como o contraste real.
**Confiança:** confirmado.

### 🔴 6. Geometria do *rollover* anticlinal descrita ao contrário

**claim_id:** `BACIAS-M10-A04-ROLLOVER-106` · **Tipo:** erro factual (inversão de sentido)
**Onde:** a04 · "Falhas de crescimento" + recap + manifesto
**Estava escrito:** "rotação passiva de camadas que **mergulham para longe da falha** perto da
superfície e se achatam em direção à falha em profundidade — o padrão chamado de rollover
anticlinal: uma **dobra de arrasto** assimétrica"
**Problema:** duas coisas erradas. (a) O sentido está invertido: no *rollover*, as camadas do
bloco do teto rodam **de volta em direção ao plano de falha**, e o mergulho **aumenta** quanto
mais perto dele — é a definição de **arrasto reverso** (*reverse drag*). O que o texto descreve
é o arrasto normal, o padrão oposto. (b) Chamar de "dobra de arrasto" atribui o mecanismo errado:
arrasto normal é atrito ao longo do plano; *rollover* é colapso do bloco do teto para preencher
o vazio potencial. O texto acertava a conclusão ("não por compressão") pelo caminho errado.
**Correção aplicada:** parágrafo reescrito nomeando o arrasto reverso, o sentido correto do
mergulho e o mecanismo de colapso; recap e claim `BACIAS-M10-A04-GROWTHFAULT-002` corrigidos;
acrescentada a ressalva de Grasemann et al. (2005) de que *rollover* **não** é diagnóstico
exclusivo de falha lístrica.
**Fonte:** Grasemann, Martel & Passchier (2005), *Journal of Structural Geology* 27 · **Nível:** revisada por pares
**Confiança:** confirmado.

---

## Achados 🟠

| # | claim_id | Onde | Problema | Correção aplicada |
|---|---|---|---|---|
| 7 | `BACIAS-M10-A05-MATURACAO-107` | a05 · tabela de hábitat | **Sentido do efeito invertido.** A célula dizia que na bacia invertida a geradora fica "soterrada mais profundamente pela carga adicional da inversão (aumentando a maturação)". É o oposto: inversão **retira** sobrecarga, soergue e resfria a geradora, e tende a **interromper** a maturação. Contradizia o próprio corpo da a05, três seções acima, que já dizia que a inversão pode "soerguer e erodir a rocha geradora". Consequência de projeto invertida — o aluno concluiria que inverter a bacia é bom para a cozinha. | célula reescrita com o sentido correto; parágrafo de "Consequências" ampliado para nomear o efeito ("desligar a cozinha") e advertir que a intuição erra o sinal; recap corrigido; **claim novo** `BACIAS-M10-A05-MATURACAO-006` criado, porque a alegação não existia no manifesto |
| 8 | `BACIAS-M10-A05-ALPES-108` | a05 · "O que é inversão" + manifesto | "A inversão **dos Alpes Suíços** (…) durante a orogenia alpina" apresentada como exemplo de referência. Os Alpes são o orógeno, não uma bacia invertida; os exemplos canônicos de Ziegler et al. (1995) são bacias do **antepaís** alpino, a centenas de km da cadeia. | substituído por Sole Pit e demais estruturas do Mar do Norte meridional, Broad Fourteens e Wessex-Weald, com a frase que explica ser deformação compressiva **intraplaca** e não a construção do orógeno; claim `-MARDONORTE-003` reescrito |
| 9 | `BACIAS-M10-A04-DIAPIRO-109` | a04 · "Tectônica de sal" | Diapirismo atribuído à **inversão de densidade** como causa. A fonte citada pela própria aula (Jackson & Hudec) sustenta o contrário: a cobertura consolidada tem resistência ao cisalhamento e o empuxo sozinho é fraco demais para rompê-la; o motor primário é o **carregamento diferencial**. Simplificação que induz o modelo mental errado (sal como bolha de óleo subindo na água). | acrescentada a correção explícita da literatura moderna, nomeando o carregamento diferencial como motor e a extensão da cobertura como assistente, e mantendo a flutuabilidade como contribuinte; exemplo trabalhado e recap realinhados; claim `-SAL-003` reescrito; Hudec & Jackson 2007 acrescentada às fontes |
| 10 | `BACIAS-M10-A04-RAFT-110` | a04 · "Tectônica de sal" | "**Minibacias** (*minibasins* ou '*rafts*')" — trata como sinônimos duas feições distintas. *Raft* é bloco **alóctone** da cobertura que, sob extensão pelicular extrema, desliza e **perde contato** com os vizinhos, separado por grabens sindeposicionais. Minibacia é depressão que subside onde o sal foi evacuado. | "ou *rafts*" removido da definição de minibacia; *rafts* definidos à parte com o mecanismo e a área-tipo (Kwanza); recap e claim atualizados; Duval, Cramez & Jackson 1992 acrescentada às fontes |
| 11 | `BACIAS-M10-A02-BREAKUP-111` | a02 · 5 ocorrências + manifesto | "**Discordância de rifteamento**" é cunhagem não corrente: nomeia a discordância pela fase que ela **encerra**. A literatura brasileira usa "discordância de ruptura" / "discordância do *break-up*". | renomeado em todas as ocorrências para "discordância de ruptura", com o termo em inglês e a variante brasileira dados na primeira menção |
| 12 | `BACIAS-M10-A02-SAG-112` | a02 · "Duas fases" | "sequência de manto (*sag* ou *drift sequence*)" — dois problemas: "sequência de manto" não é termo da disciplina e, num curso de geologia, "manto" colide de frente com o manto terrestre; e *sag* e *drift* **não** são sinônimos (no Atlântico Sul o *sag* é a fase que hospeda o pré-sal, anterior à deriva plena). | termo cunhado removido (a metáfora preservada como "colcha"); *sag* e *drift* separados como duas fases, com o pré-sal ancorando a distinção |
| 13 | `BACIAS-M10-A02-CONJUGADAS-113` | a02 · "Duas fases" | "a margem brasileira, a oeste-africana e a leste dos EUA (…) **todas** nasceram como **um único sistema de riftes** durante a fragmentação do Gondwana e da Pangeia, **respectivamente**" — três margens para dois eventos, e não é um único sistema: Brasil/África são conjugadas do Atlântico Sul (Gondwana, Cretáceo Inferior); a costa leste dos EUA é do Atlântico Central (Pangeia, Triássico–Jurássico). | separado em duas frases, com o par conjugado nomeado como tal e cada evento com a sua idade |
| 14 | `BACIAS-M10-A01-BETA-114` | a01 · mecanismo 1 + manifesto | Subsidência descrita como "**proporcional** ao fator de estiramento β". Em McKenzie (1978) a dependência não é linear: a amplitude satura, tendendo a um máximo assintótico quando β cresce (o fator (β/π)·sen(π/β) → 1). "Proporcional" sugere que dobrar β dobra a subsidência. | reescrito como "função crescente do fator de estiramento — crescente, mas não linear: a amplitude tende a um valor máximo assintótico"; claim `-MECKENZIE-002` atualizado |
| 15 | `BACIAS-M10-A01-COLUNA-115` | a01 · mecanismo 1 | "a **crosta** mais fina e **mais densa**" — a crosta não fica mais densa ao afinar; o que fica mais densa é a **coluna litosférica**, porque manto astenosférico denso ocupa o espaço da crosta leve removida. Como está, ensina que estirar torna a crosta densa. | reescrito para "a **coluna litosférica** fica mais densa (a crosta, leve, adelgaça, e manto astenosférico mais denso ocupa o espaço liberado na base)" |
| 16 | `BACIAS-M10-A01-CARBONATO-116` | a01 · Exemplo trabalhado | "o **afinamento** progressivo das fácies para o topo (de folhelho a carbonato, sugerindo **aprofundamento relativo**…)". Carbonato sobre folhelho não indica aprofundamento — indica **plataforma faminta de clásticos**; e a passagem folhelho→carbonato não é afinamento granulométrico. | reescrito para "a redução progressiva do aporte clástico para o topo (…) uma plataforma faminta de clásticos, e não necessariamente um aprofundamento" |
| 17 | `BACIAS-M10-A03-GRANO-117` | a03 · "Migração da carga" + recap + manifesto | "um **afinamento e engrossamento** de granulometria ascendente" — autocontraditório na mesma linha; e "sucessão 'grosseiramente ascendente'" é tradução equivocada de *coarsening-upward* (o termo em português é **granocrescência ascendente**). Além disso, corpo e recap fundiam dois eixos distintos: o rejuvenescimento é **horizontal** (na direção do antepaís), a granocrescência é **vertical** (num mesmo ponto). | parágrafo reescrito separando explicitamente os dois eixos, com a passagem *back-bulge* → *forebulge* → *foredeep* → *wedge-top* como a razão física da granocrescência; recap e claim `-MIGRACAO-004` realinhados |
| 18 | `BACIAS-M10-A04-ESCALA-118` | a04 · "Bacias pull-apart" + recap + manifesto | Bacias *pull-apart* descritas como "poucos a poucas **dezenas** de quilômetros de comprimento" — subestima os dois exemplos que a própria frase dá: a Bacia do Mar Morto tem ~150 km. Também: "**Mar de Salton**" nomeia o lago raso, não a bacia (*Salton Trough*), e "O Mar Morto, **entre** a falha transformante do Levante" ficou truncado. | escala corrigida (poucos km a mais de cem, com as dimensões do Mar Morto), acrescentada a razão comprimento/largura de 3 a 4, e o critério de distinção reancorado na **concentração** da extensão e não no tamanho; nomes corrigidos para "Bacia do Mar Morto" e "Depressão de Salton (*Salton Trough*)", propagados à tabela da a01 |

**Fontes dos 🟠, por bloco:** Allen & Allen (2013) cap. 9, 11, 12–13; McKenzie (1978), *EPSL* 40(1);
DeCelles & Giles (1996), *Basin Research* 8(2); Hudec & Jackson (2007), *Earth-Science Reviews* 82;
Jackson & Hudec (2017) cap. 1–3; Duval, Cramez & Jackson (1992), *Marine and Petroleum Geology* 9(4);
Ziegler, Cloetingh & van Wees (1995), *Tectonophysics* 252; Aydın & Nur (1982) e a compilação de
razões de aspecto de *pull-apart* em *Lithosphere* 2(3); Boletim de Geociências da Petrobras
(terminologia rifte / *sag* / drifte da margem brasileira). Todas de nível revisada por pares ou
tratado de referência; confiança **confirmado** em todos os 🟠, exceto o 12, onde a distinção
*sag*/drifte é convenção regional bem estabelecida mas não normativa.

---

## Achado 🔵 — sem fonte suficiente, **não corrigido**

### 🔵 19. Intervalo de páginas de Ziegler, Cloetingh & van Wees (1995)

**claim_id:** `BACIAS-M10-A05-CITACAO-119` · **Tipo:** evidência insuficiente
**Onde:** a05 · Fontes
**Está escrito:** "*Tectonophysics*, 252(1–4), p. 7–59"
**Problema:** as compilações divergem — a maioria dá **p. 7–61**, algumas dão 7–59; o título
também circula em duas formas ("Dynamics…" e "Geodynamics…"). Não foi possível resolver a
divergência contra o registro do editor.
**Desfecho:** **não corrigido, deliberadamente.** Nenhuma correção foi inventada. Impacto
pedagógico nulo (não afeta nenhuma afirmação do conteúdo); registrado para quem for conferir a
referência. Não gera `open_finding`.

---

## Verificado e correto (amostra do que passou)

- Constante de tempo da subsidência térmica de McKenzie, "da ordem de 60 Ma" — confere
  (τ = a²/π²κ ≈ 63 Ma para a = 125 km). Circula também "~50 Ma" com litosfera mais fina;
  a a01 está na faixa canônica.
- Definição de β como razão entre espessura litosférica original e final — correta.
- Fator multiplicador da carga sedimentar: "1.000 m de espaço tectônico → 2.500 a 3.000 m de
  sedimento" e "mais da metade do espaço total" — conferem com (ρm−ρw)/(ρm−ρs) ≈ 2,8.
- Aritmética do exemplo trabalhado da a01: 900 m / 15 Ma = 60 m/Ma e 3.300 m / 110 Ma = 30 m/Ma
  — ambas corretas.
- Amplitude (dezenas a poucas centenas de metros) e largura (dezenas a mais de cem km) do
  *forebulge* — dentro da faixa publicada.
- Distinção retroarco vs. periférico e a atribuição a Dickinson (1974) — corretas; Pó e Ganges
  são exemplos periféricos válidos.
- Densidade do sal menor que a dos sedimentos compactados abaixo de ~1.000–1.500 m — confere.
- Definições de inversão positiva e negativa contra Cooper & Williams (1989) — corretas, inclusive
  a observação de que "negativa" é menos frequente na literatura.
- Os quatro elementos do sistema petrolífero e o papel do sincronismo, contra Magoon & Dow (1994)
  — corretos.
- Citações conferidas e exatas: McKenzie 1978 *EPSL* 40(1) 25–32; Dickinson 1974 SEPM SP 22 1–27;
  Kingston et al. 1983 *AAPG Bulletin* 67(12) 2175–2193; DeCelles & Giles 1996 *Basin Research*
  8(2) 105–123; Gibbs 1984 *JGS* 141(4) 609–620; Ebinger 1989 *GSA Bulletin* 101(7) 885–903;
  Christie-Blick & Biddle 1985 SEPM SP 37 1–34; Crans, Mandl & Haremboure 1980 *JPG* 2(3) 265–307.

## Verificação de consistência entre aulas

Auditadas em conjunto, como manda o procedimento para módulo. Três contradições entre aulas foram
achadas e todas entraram como achado: o plano da falha normal (a02 correto × a04 errado, #5); os
compartimentos de antepaís (corpo da a03 × manifesto da a03, #3); e o efeito da inversão sobre a
maturação (corpo da a05 × tabela da a05, #7). Verificado ainda que a cadeia de vocabulário fecha:
espaço de acomodação (a01) → sin-rifte/pós-rifte (a01, a02) → meio-graben (a02, reutilizado em a04
e a05) → flexura (a01, a03) → armadilha (a04, a05). Nenhuma contradição com módulos já escritos;
o M11 (Sismoestratigrafia), que consumirá o vocabulário de terminação de estratos anunciado na a01,
ainda está `pending`.

## Correções aplicadas

**Aplicadas em:** 2026-08-30

| claim_id | Sev. | Desfecho | Arquivos alterados |
|---|---|---|---|
| `BACIAS-M10-A02-SELANTE-101` | 🔴 | Corrigido | aula-02 |
| `BACIAS-M10-A02-FLEXURAL-102` | 🔴 | Corrigido | aula-02 (corpo, figura, recap, manifesto, fontes) |
| `BACIAS-M10-A03-DEPOZONES-103` | 🔴 | Corrigido | aula-03 (corpo, legenda, recap, exemplo) |
| `BACIAS-M10-A03-AMAZONAS-104` | 🔴 | Corrigido | aula-03 (corpo, manifesto) |
| `BACIAS-M10-A04-PLANO-105` | 🔴 | Corrigido | aula-04 |
| `BACIAS-M10-A04-ROLLOVER-106` | 🔴 | Corrigido | aula-04 (corpo, recap, manifesto, fontes) |
| `BACIAS-M10-A05-MATURACAO-107` | 🟠 | Corrigido | aula-05 (tabela, corpo, recap, manifesto — claim novo `-MATURACAO-006`) |
| `BACIAS-M10-A05-ALPES-108` | 🟠 | Corrigido | aula-05 (corpo, manifesto) |
| `BACIAS-M10-A04-DIAPIRO-109` | 🟠 | Corrigido | aula-04 (corpo, exemplo, recap, manifesto, fontes) |
| `BACIAS-M10-A04-RAFT-110` | 🟠 | Corrigido | aula-04 (corpo, recap, manifesto, fontes) |
| `BACIAS-M10-A02-BREAKUP-111` | 🟠 | Corrigido | aula-02 (5 ocorrências + manifesto) |
| `BACIAS-M10-A02-SAG-112` | 🟠 | Corrigido | aula-02 |
| `BACIAS-M10-A02-CONJUGADAS-113` | 🟠 | Corrigido | aula-02 |
| `BACIAS-M10-A01-BETA-114` | 🟠 | Corrigido | aula-01 (corpo, manifesto) |
| `BACIAS-M10-A01-COLUNA-115` | 🟠 | Corrigido | aula-01 |
| `BACIAS-M10-A01-CARBONATO-116` | 🟠 | Corrigido | aula-01 |
| `BACIAS-M10-A03-GRANO-117` | 🟠 | Corrigido | aula-03 (corpo, recap, manifesto) |
| `BACIAS-M10-A04-ESCALA-118` | 🟠 | Corrigido | aula-04 (corpo, recap, manifesto) + aula-01 (tabela) |
| `BACIAS-M10-A05-CITACAO-119` | 🔵 | Aceito como está | — |

**Pendências:** nenhuma que bloqueie o gate. Único item aberto é o 🔵 19 (intervalo de páginas
de uma referência), sem impacto de conteúdo e sem `open_finding`.

## Advertências ao gerador de questionários e de flashcards

Os pontos abaixo mudaram nesta auditoria. Gerar item a partir da versão antiga produz gabarito
errado — confira contra o texto corrigido, não contra a memória do módulo.

1. **Rollover mergulha PARA a falha**, não para longe dela. É arrasto **reverso**. Qualquer item
   sobre *rollover* precisa cobrar esse sentido, que é o ponto inteiro da feição.
2. **Inversão levanta a geradora e interrompe a maturação.** Não a aprofunda. Este é o distrator
   natural e o mais tentador do módulo — vale um item dedicado.
3. **Quatro zonas deposicionais de antepaís:** *wedge-top*, *foredeep*, *forebulge*, *back-bulge*.
   O antepaís não deformado **não** é uma delas — excelente distrator, e o item deve cobrar
   justamente essa exclusão.
4. **Borda flexural ≠ alto de *footwall*.** São as margens opostas do meio-graben. Outro distrator
   de primeira, porque o erro é o que o senso comum sugere.
5. **Diápiro é dirigido por carregamento diferencial**, não por flutuabilidade sozinha.
6. ***Raft* não é minibacia.** Se cobrar um, não cobre o outro no mesmo item.
7. **Antepaís andino no Brasil = Bacia do Acre**, neógena. A Bacia do Amazonas é intracratônica
   paleozoica e serve como distrator, nunca como resposta.
8. **Falha normal tem plano inclinado (~60°)**; vertical é a transcorrente.
9. O termo é **discordância de ruptura** (*break-up unconformity*), não "de rifteamento".
10. Granocrescência ascendente é **vertical**; o rejuvenescimento das sequências é **horizontal**,
    na direção do antepaís. Não fundir os dois num item só.
