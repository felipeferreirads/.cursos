# Auditoria científica — Módulo 11: Sismoestratigrafia

**Auditado em:** 2026-08-30 · **Modo:** `audit-and-fix` · **Profundidade:** `full`
**Material:** `11-sismoestratigrafia/` — 6 aulas (a01 a a06)
**Veredito:** **Aprovado com correções aplicadas** — nenhum achado 🔴 ou 🟠 em aberto.

## Resumo

🔴 3 erros · 🟠 7 imprecisos · 🟡 0 desatualizados · 🔵 0 sem fonte · ⚪ 0 controversos

**Total: 10 achados.** As 28 alegações auditáveis declaradas pelas seis aulas foram usadas como
ponto de partida e todas reverificadas contra fonte. **9 dos 10 achados estão fora da lista
declarada** — inclusive os três vermelhos. O único achado que a lista do autor antecipou foi o
da resolução (`SISMO-M11-A01-WIDESS-004`), e mesmo ali o autor declarou a alegação **já com o
erro dentro dela**: a lista serviu para localizar o ponto, não para protegê-lo.

**Padrão dominante dos achados:** **atribuição**. Cinco dos dez achados são de um mesmo tipo —
o conteúdo geológico está certo, mas está pendurado no autor, no artigo, na fase tectônica ou
no mecanismo errado (Widess para o λ/4; Brown & Fisher para carbonatos; Catuneanu para uma
lista de tratos que não é a dele; a fase de rifte para o sal aptiano; a reologia do sal para o
topo plano). Esse tipo de erro é especialmente perigoso num módulo em que a disciplina inteira
é organizada por nomes próprios de 1977–1988: o aluno sai capaz de citar a fonte errada com
confiança, e um flashcard "quem definiu X?" nasce com o verso invertido.

**Segundo padrão, menor mas mais grave por item:** duas **inversões de sinal** — o exemplo
trabalhado da a02 descrevia o sintético adiantado e explicava o padrão por um mecanismo que
só produz atraso; a a06 atribuía o topo plano do sal a um processo que faz exatamente o
oposto. São os mesmos "erros de sentido" que dominaram a auditoria do Módulo 10.

**O que a auditoria olhou e considerou correto** está na seção "Verificado e correto", no fim.
Em particular, a correspondência estrutural↔sísmica com o Módulo 10 (borda flexural → onlap;
discordância de ruptura → truncamento; cunhas deltaicas pós-rifte → downlap) foi verificada
item a item e **está cientificamente correta**, sem confusão introduzida.

---

## Achados 🔴

### 🔴 1. O critério λ/4 atribuído a Widess (1973)

**claim_id:** `SISMO-M11-A01-WIDESS-004` · **Tipo:** erro factual (atribuição + valor)
**Onde:** a01 · "Resolução sísmica" + Exemplo trabalhado + Recap + manifesto
**Estava escrito:** "O critério prático mais citado, derivado por Widess (1973), estabelece que
camadas com espessura inferior a cerca de λ/4 já não geram reflexões de topo e base separáveis
visualmente"
**Problema:** Widess (1973) **não** propôs λ/4. Ele propôs **λ/8**, definido como a espessura
abaixo da qual a forma de onda composta estabiliza — aproximando-se da derivada do pulso da
fonte — e apenas a amplitude continua respondendo à espessura. O **λ/4** é o **critério de
Rayleigh**, que coincide com a **espessura de sintonia** (*tuning thickness*), onde a
interferência entre topo e base atinge amplitude máxima e as duas reflexões deixam de ser
separáveis visualmente. A aula fundiu os dois limiares num só e colou o nome errado no
número. Agravante: o próprio texto descrevia, logo em seguida, o regime de Widess ("abaixo
disso, o efeito da camada fina ainda modula a amplitude") sem reconhecê-lo como um segundo
limiar — os dois conceitos estavam presentes e sobrepostos.
**Correção aplicada:** a seção de resolução foi reescrita com os **dois** limiares separados e
nomeados (Rayleigh/sintonia ≈ λ/4 para separação visual; Widess ≈ λ/8 para estabilização da
forma de onda), com uma linha explícita dizendo qual dos dois é o número usado na prática.
O exemplo trabalhado passou a dar os dois valores (25 m e 12,5 m para λ = 100 m) e o
reservatório de 8 m foi reancorado como "abaixo dos dois limiares". Recap e claim reescritos.
Kallweit & Wood (1982) acrescentada às fontes.
**Fonte:** Widess, M. B. (1973), *Geophysics* 38(6), p. 1176–1180 · Kallweit, R. S. & Wood,
L. C. (1982), "The limits of resolution of zero-phase wavelets", *Geophysics* 47(7),
p. 1035–1046. · **Nível:** revisada por pares.
**Confiança:** confirmado.
**Também aparece em:** nenhum outro arquivo — o módulo ainda não tem questionário nem baralho.

### 🔴 2. Inversão de sinal na deriva do sismograma sintético

**claim_id:** `SISMO-M11-A02-TIEDRIFT-006` · **Tipo:** inconsistência interna + erro factual
**Onde:** a02 · Exemplo trabalhado (Situação e Resolução)
**Estava escrito:** Situação — "os principais refletores do sintético aparecendo
sistematicamente mais 'cedo' em tempo do que os refletores correspondentes no dado real".
Resolução — "se o sônico subestima ligeiramente a velocidade real da formação (…'salto de
ciclo'…), cada camada adicional perfurada acumula um pequeno erro de tempo (…) exatamente o
padrão descrito."
**Problema:** as duas metades do exemplo se contradizem. O salto de ciclo faz a ferramenta
registrar tempos de trânsito **artificialmente altos** (velocidade artificialmente baixa) — o
próprio texto diz isso corretamente. Como o sintético é posicionado em tempo pela integração
do sônico, tempo de trânsito superestimado coloca cada refletor num **TWT maior**: o sintético
**atrasa**, e o atraso cresce cumulativamente com a profundidade. Um sintético *adiantado*
exigiria a hipótese oposta (velocidade superestimada) e não poderia ser explicado por salto de
ciclo. O exemplo trabalhado é justamente o lugar onde o aluno testa se entendeu o mecanismo, e
ali ele estava treinando o sinal errado.
**Correção aplicada:** a Situação passou a descrever o sintético como "mais 'tarde' (em TWT
maior)"; a Resolução ganhou duas frases que tornam o **sinal** um critério de diagnóstico
explícito ("velocidade subestimada → tempo de trânsito superestimado → sintético atrasado") e
nomeiam qual seria a explicação para o padrão oposto. Recap corrigido. Criado o claim
`SISMO-M11-A02-DERIVA-006`, inexistente no manifesto.
**Fonte:** White, R. E. & Simm, R. (2003), "Tutorial: good practice in well ties",
*First Break* 21(10) · Ellis, D. V. & Singer, J. M. (2007), *Well Logging for Earth
Scientists*, 2ª ed., cap. 9 (salto de ciclo eleva o tempo de trânsito registrado).
· **Nível:** revisada por pares / base de referência.
**Confiança:** confirmado.

### 🔴 3. Sal aptiano e carbonatos do pré-sal colocados na fase final do rifteamento

**claim_id:** `SISMO-M11-A06-SAG-005` · **Tipo:** inconsistência interna (entre módulos) +
contradição com a fonte citada
**Onde:** a06 · "A margem continental brasileira" + figura + Recap + manifesto
**Estava escrito:** "uma fase de transição, com deposição de espessos pacotes evaporíticos
(sal Aptiano) num ambiente restrito, **durante a fase final do rifteamento** (…); e, **após a
discordância de ruptura** e a instalação da margem passiva, uma fase pós-rifte dominada por
carbonatos"
**Problema:** dois problemas encadeados. (i) A ordem descrita coloca a discordância de ruptura
**acima** do sal — o que contradiz a fonte que a própria aula cita como referência da margem
brasileira: Karner & Gambôa (2007) tratam o *sag* pré-sal e seus evaporitos de cobertura como
**pós-rifte** (o título do artigo é literalmente sobre "pre-salt **sag** basins and their
capping evaporites"), e o arcabouço litoestratigráfico brasileiro corrente (Moreira et al.
2007, para Santos) posiciona o intervalo aptiano com Barra Velha + Ariri acima do fim do
falhamento principal. (ii) Contradição direta com o **Módulo 10, Aula 02**, que registra o
*sag* como a fase **pós-rifte** "onde se aloja o pré-sal do Atlântico Sul" — e essa formulação
do Módulo 10 não é incidental: ela foi o desfecho do achado `BACIAS-M10-A02-SAG-112` daquela
auditoria. O Módulo 11 desfazia, sem sinalizar, uma distinção que o Módulo 10 havia sido
corrigido para fazer. (iii) Como efeito colateral, a idade do sin-rifte ("Neocomiano") e a
posição dos reservatórios microbiais ("transição rifte-sal") ficavam ambas deslocadas.
**Correção aplicada:** o parágrafo foi reestruturado em três andares numerados (sin-rifte
Hauteriviano–Barremiano; *sag*/transição aptiano com Barra Velha e Ariri; deriva albiana em
diante), com um bloco explícito de **atenção** que declara a divergência entre escolas em vez
de resolvê-la em silêncio, nomeia qual leitura o curso adota (a de Karner & Gambôa e a do
Módulo 10, com a discordância de ruptura **abaixo** do *sag*), e adverte contra misturar as
duas convenções na mesma seção. A figura da coluna estratigráfica foi redesenhada com a
discordância de ruptura marcada na posição adotada e a ressalva na legenda. Recap corrigido.
Claims `-MARGEMBR-003` (reclassificado como `controverso`) e `-PRESAL-004` reescritos.
Moreira et al. (2007) acrescentada às fontes.
**Fonte:** Karner, G. D. & Gambôa, L. A. P. (2007), *Geological Society Special Publication*
285, p. 15–35 · Moreira, J. L. P. et al. (2007), "Bacia de Santos", *Boletim de Geociências
da Petrobras* 15(2), p. 531–549 · Mohriak, Nemčok & Enciso (2008), GSL SP 294.
· **Nível:** revisada por pares.
**Confiança:** confirmado quanto à contradição; a posição "correta" da discordância de ruptura
é genuinamente disputada, e por isso o texto passou a declarar a disputa em vez de escolher em
silêncio.

---

## Achados 🟠

### 🟠 4. Coeficiente de reflexão descrito como fração de energia

**claim_id:** `SISMO-M11-A01-RC-006` · **Tipo:** erro factual (grandeza física)
**Onde:** a01 · "O que a sísmica de reflexão mede" + manifesto (`-IMPEDANCIA-001`)
**Estava escrito:** "A fração da **energia** incidente que retorna refletida (…) é dada pelo
coeficiente de reflexão"
**Problema:** RC é uma razão de **amplitudes**, não de energias. A fração de energia refletida
é RC². A confusão não é acadêmica: a aula declara essa equação "a mais importante do módulo" e
a a02 a reutiliza para construir o sismograma sintético, que é explicitamente um traço de
amplitude.
**Correção aplicada:** "energia" → "amplitude", com uma frase que dá o contraste numérico
(RC = 0,1 devolve 10% da amplitude e 1% da energia). Recap e claim corrigidos.
**Fonte:** Sheriff & Geldart (1995), *Exploration Seismology*, 2ª ed., cap. 3–4.
· **Nível:** base de referência. **Confiança:** confirmado.

### 🟠 5. Cadeia de processamento na ordem errada

**claim_id:** `SISMO-M11-A01-ORDEM-007` · **Tipo:** erro factual (sequência de método)
**Onde:** a01 · "Processamento" (lista numerada) + Recap + manifesto (`-PROCESSAMENTO-003`)
**Estava escrito:** lista numerada com "1. Correção de NMO e empilhamento", "2. Deconvolução",
"3. Migração".
**Problema:** invertido em relação à fonte que a própria aula cita. Yilmaz organiza o
processamento convencional em torno de três processos principais **nesta ordem** —
deconvolução, empilhamento, migração —, e a deconvolução é aplicada **antes** do empilhamento,
sobre os traços individuais. Uma lista numerada comunica ordem, e a ordem aqui não é
convenção arbitrária: os três processos operam sobre eixos diferentes do dado e cada um
pressupõe o anterior.
**Correção aplicada:** itens 1 e 2 trocados, com a ordem canônica declarada na frase de
abertura e atribuída a Yilmaz, e uma cláusula no item de deconvolução dizendo que ela é
aplicada antes do empilhamento. Recap e claim atualizados.
**Fonte:** Yilmaz, Ö. (2001), *Seismic Data Analysis*, SEG, cap. 1 e 4.
· **Nível:** base de referência. **Confiança:** confirmado.

### 🟠 6. Efeito *bow-tie* atribuído também a domos de sal

**claim_id:** `SISMO-M11-A01-BOWTIE-008` · **Tipo:** confusão de escopo
**Onde:** a01 · "Processamento", item de migração + Recap + manifesto (`-PROCESSAMENTO-003`)
**Estava escrito:** "efeito conhecido como *bow-tie*, comum sob sinclinais e domos de sal"
**Problema:** o *bow-tie* é o artefato de **foco enterrado** (*buried focus*), produzido
especificamente por um sinclinal cuja curvatura excede a da frente de onda — aparece no dado
não migrado como duas falsas antiformas cruzadas. Corpos de sal degradam a imagem por
mecanismos **diferentes**: difrações nas bordas e distorção do campo de ondas pela alta
velocidade do sal (que a própria aula trata dois parágrafos adiante, como *pull-up*). Juntar
os dois numa frase ensina que o *bow-tie* é um artefato genérico de "estrutura complexa",
quando ele é o exemplo-livro de uma geometria específica.
**Correção aplicada:** frase reescrita nomeando o foco enterrado e a geometria sinclinal, com
o mecanismo do sal separado numa oração própria. Recap e claim atualizados.
**Fonte:** Yilmaz (2001), cap. 4 (migração, foco enterrado) · Sheriff & Geldart (1995), cap. 9.
· **Nível:** base de referência. **Confiança:** confirmado.

### 🟠 7. Downlap e toplap definidos pela inclinação absoluta da ponta da camada

**claim_id:** `SISMO-M11-A03-DIPTERM-005` · **Tipo:** confusão de escopo + figura incorreta
**Onde:** a03 · "Os padrões de terminação" (Downlap e Toplap) + figura ASCII + Recap +
manifesto (`-TERMINACOES-002`)
**Estava escrito:** Downlap — "terminam, em sua **extremidade de menor mergulho** (a base,
'morro abaixo')". Toplap — "terminam, em sua **extremidade de maior mergulho** (o topo)".
**Problema:** o critério definidor não é a inclinação absoluta da extremidade da camada; é
(i) a **direção** da terminação — *downdip* para downlap, *updip* para toplap — e (ii) para
separar onlap de downlap, a inclinação **relativa** entre refletor e superfície de base
(*baselap*: onlap quando a superfície mergulha mais que os refletores, downlap quando os
refletores mergulham mais que a superfície). A formulação da aula funciona por acidente em
clinoformas sigmoides e oblíquas tangenciais, onde a base realmente aplana, e **falha** em
clinoformas oblíquas paralelas, cujo mergulho é constante até a base — justamente o subtipo que
a a04 lista quatro parágrafos adiante. É uma regra de um subcaso apresentada como definição.
**Problema adicional, na figura:** o painel DOWNLAP da figura ASCII desenhava a superfície de
downlap **acima** das clinoformas, invertendo a geometria que o painel existe para ensinar.
**Correção aplicada:** as duas definições reescritas em termos de *updip*/*downdip*; o par
onlap–downlap reancorado no conceito de *baselap* e no critério de inclinação relativa,
com a advertência explícita "não é a inclinação absoluta da ponta da camada que decide".
Figura ASCII inteiramente redesenhada, agrupada por qual superfície-limite recebe a terminação
(base vs. topo) e com a superfície de downlap na posição correta. Recap e claim atualizados.
Mitchum (1977, parte 11 — o glossário da Memoir 26) acrescentada às fontes.
**Fonte:** Mitchum, R. M., Vail, P. R. & Thompson, S. (1977), AAPG Memoir 26, parte 2 ·
Mitchum, R. M. (1977), AAPG Memoir 26, parte 11 (glossário), p. 205–212 · Catuneanu (2006),
cap. 2. · **Nível:** normativa da disciplina. **Confiança:** confirmado.

### 🟠 8. Sismofácies carbonáticas atribuídas a Brown & Fisher (1977)

**claim_id:** `SISMO-M11-A04-BROWNFISHER-006` · **Tipo:** erro factual (atribuição)
**Onde:** a04 · "Sismofácies carbonáticas" + Recap + Fontes + manifesto (`-CARBONATOS-003`)
**Estava escrito:** "um ponto sistematizado por **Brown & Fisher (1977)** no mesmo volume da
AAPG Memoir 26"
**Problema:** o artigo de Brown & Fisher na Memoir 26 (p. 213–248) é
*"Seismic-stratigraphic interpretation of depositional systems: examples from Brazilian rift
and pull-apart basins"* — sistemas deposicionais **siliciclásticos** em bacias brasileiras. Ele
não sistematiza sismofácies carbonáticas. A referência carbonática do próprio volume é
**Bubb & Hatlelid (1977), parte 10, "Seismic recognition of carbonate buildups"**, p. 185–204.
Erro de consequência dupla: além de citar errado, deixava a aula sem sua fonte-chave e
mantinha Brown & Fisher rotulados de forma que esconde o que eles de fato oferecem ao curso
(exemplos brasileiros, diretamente úteis à a06).
**Correção aplicada:** atribuição corrigida para Bubb & Hatlelid (1977) no corpo, no recap e no
claim; Bubb & Hatlelid acrescentada às Fontes; a entrada de Brown & Fisher mantida, com
"siliciclásticos" em destaque para explicitar o escopo.
**Fonte:** Bubb, J. N. & Hatlelid, W. G. (1977), AAPG Memoir 26, parte 10, p. 185–204
(também em *AAPG Bulletin* 62(5), p. 772–791). · **Nível:** normativa da disciplina.
**Confiança:** confirmado.

### 🟠 9. Assinatura de plataforma estratificada generalizada a construções recifais

**claim_id:** `SISMO-M11-A04-RECIFE-007` · **Tipo:** omissão que gera erro + inconsistência
interna
**Onde:** a04 · "Sismofácies carbonáticas" + Recap + manifesto (`-CARBONATOS-003`)
**Estava escrito:** "Um **recife de borda de plataforma** ou uma rampa carbonática progradante
gera, tipicamente, uma configuração de clinoformas (…) produzindo refletores internos
frequentemente mais fortes e mais contínuos"
**Problema:** a generalização é válida para plataformas e rampas **bem estratificadas** e falsa
para o **recife** que a frase nomeia primeiro. A assinatura clássica de um *buildup* recifal
maciço, na literatura de reconhecimento sísmico de carbonatos, é o oposto: configuração
interna **refletor-livre a caótica** (o núcleo é homogêneo em impedância), geometria externa em
**monte**, e diagnóstico feito pelo **entorno** — refletor de topo, difrações de borda, onlap
das encaixantes contra os flancos, *drape* por compactação diferencial, *pull-up* de
velocidade. Agravante de inconsistência interna: a própria a04, três parágrafos antes, já
classificava "pacotes carbonáticos maciços" como sismofácies **transparente**, e a seção de
carbonatos contradizia essa classificação sem notar.
**Correção aplicada:** a seção foi reorganizada em duas alíneas explicitamente contrastadas —
plataforma/rampa estratificada (refletores internos fortes e contínuos, borda nítida) e
construção recifal (refletor-livre a caótica por dentro, monte por fora, diagnóstico pelo
entorno) —, com a frase de fechamento dizendo que a lista de configurações internas, sozinha,
não basta para carbonatos. Recap e claim atualizados.
**Fonte:** Bubb & Hatlelid (1977), AAPG Memoir 26, parte 10 · Sarg, J. F. (1988), SEPM
Special Publication 42, p. 155–181. · **Nível:** normativa da disciplina.
**Confiança:** confirmado.

### 🟠 10. Lista de "quatro tratos de sistemas" sem o trato de estágio de queda

**claim_id:** `SISMO-M11-A05-FSST-006` · **Tipo:** omissão que gera erro + erro de atribuição
**Onde:** a05 · "Sequência deposicional e os tratos de sistemas" + figura + Recap + manifesto
(`-TRATOS-003`)
**Estava escrito:** "o núcleo conceitual é estável em torno de **quatro tratos principais**",
seguido de LST, TST, HST e **SMST** — este último descrito como "reconhecido em **versões
posteriores** do modelo", com Catuneanu (2006) citado na mesma frase como "a referência mais
usada para conciliar as diferentes escolas".
**Problema:** dois erros que se reforçam. (i) Os quatro tratos de Catuneanu (2006) são LST,
TST, HST e **FSST** (*falling-stage systems tract*) — e o FSST estava **inteiramente ausente**
da aula, embora ela invoque Catuneanu como a síntese moderna. Numa aula avançada de
estratigrafia de sequências, omitir o trato depositado durante a queda do nível relativo do
mar é omitir a principal diferença entre o modelo dos anos 1980 e o que se usa hoje — e joga
para dentro do LST tudo o que se deposita durante a queda (incisão de vale, leques de assoalho
de bacia), que é exatamente o erro que o FSST existe para evitar. (ii) O SMST não é de
"versões posteriores": é o trato basal da "sequência de tipo 2" do **modelo Exxon original**
(Posamentier & Vail 1988; Van Wagoner et al. 1988), os mesmos trabalhos que a aula chama de
"originais" duas linhas antes.
**Correção aplicada:** o FSST foi acrescentado como quarto trato, com sua assinatura sísmica
(quebras de plataforma descendo em degraus, ausência de topsets, formação progressiva da
discordância subaérea) e sua história de nomenclatura (Hunt & Tucker 1992 → Plint & Nummedal
2000 → Catuneanu 2006). O SMST foi movido para um parágrafo à parte, reposicionado como
integrante do modelo Exxon original e explicitamente sinalizado como "não confundir com o
FSST". O item do LST ganhou a ressalva de que leques e incisão migram de trato conforme a
convenção adotada; o exemplo trabalhado passou a dar as duas leituras em vez de uma; a figura
da curva de nível relativo do mar foi redesenhada com o FSST e com a observação de que a SB
**se forma durante a queda** e é diácrona. Recap e claim reescritos. Hunt & Tucker (1992) e
Plint & Nummedal (2000) acrescentadas às fontes.
**Fonte:** Hunt, D. & Tucker, M. E. (1992), *Sedimentary Geology* 81(1–2), p. 1–9 ·
Plint, A. G. & Nummedal, D. (2000), GSL Special Publication 172, p. 1–17 · Catuneanu, O.
(2006), *Principles of Sequence Stratigraphy*, cap. 3–5. · **Nível:** revisada por pares /
base de referência. **Confiança:** confirmado.

### 🟠 11. Topo plano do sal atribuído à reologia

**claim_id:** `SISMO-M11-A06-TOPOSAL-009` · **Tipo:** erro factual (mecanismo invertido)
**Onde:** a06 · Exemplo trabalhado
**Estava escrito:** "o topo plano reflete o **comportamento reológico** do sal, que tende a
nivelar sua superfície superior independentemente do relevo abaixo"
**Problema:** mecanismo invertido. O topo plano de uma camada de sal autóctone é uma feição
**deposicional** — evaporitos precipitam a partir de uma salmoura e preenchem a depressão até
uma superfície nivelada, pela mesma razão que qualquer corpo d'água tem superfície plana —,
enquanto a base irregular replica a topografia herdada. O comportamento reológico do sal faz o
**oposto** do que a frase afirma: o fluxo salífero rompe o nivelamento e produz diápiros,
muralhas e um topo de sal fortemente irregular. Como está, a frase ensinaria que quanto mais o
sal flui, mais plano fica seu topo — e o aluno acabou de ler, no Módulo 10 (Aula 04), toda a
tectônica de sal que diz o contrário.
**Correção aplicada:** frase reescrita nomeando a origem deposicional do topo plano e a
advertência explícita de que o fluxo salífero faz o oposto, com a leitura útil que decorre
disso (topo plano preservado indica sal pouco mobilizado). Criado o claim
`SISMO-M11-A06-TOPOSAL-009`, inexistente no manifesto.
**Fonte:** Hudec, M. R. & Jackson, M. P. A. (2007), "Terra infirma: understanding salt
tectonics", *Earth-Science Reviews* 82 (já citada no Módulo 10, a04) · Jackson & Hudec
(2017), *Salt Tectonics: Principles and Practice*, cap. 2 e 6.
· **Nível:** base de referência. **Confiança:** confirmado.

### 🟠 12. Idade da fase sin-rifte da margem leste brasileira

**claim_id:** `SISMO-M11-A06-IDADERIFTE-008` · **Tipo:** impreciso (cronoestratigrafia)
**Onde:** a06 · "A margem continental brasileira" + figura + manifesto (`-MARGEMBR-003`)
**Estava escrito:** "uma fase **sin-rifte (Neocomiano**, dentro do Cretáceo Inferior)"
**Problema:** "Neocomiano" (Berriasiano–Hauteriviano em uso estrito) é cedo demais para a fase
sin-rifte de Santos e Campos, cujo preenchimento sedimentar começa no **Barremiano** e cujas
rochas geradoras lacustres principais são do **Barremiano superior ao Aptiano inferior**
(Fms. Itapema e Piçarras em Santos; Gp. Lagoa Feia em Campos). A aula usa o termo justamente na
frase que ancora a geradora do pré-sal, de modo que a imprecisão cai sobre o elemento mais
importante do sistema petrolífero descrito. Registrado como 🟠 e não 🔴 porque a literatura
brasileira de fato usa "Neocomiano" em sentido amplo como sinônimo informal de "Cretáceo
Inferior pré-Aptiano" — é imprecisão de convenção, não afirmação falsa isolada.
**Correção aplicada:** idade corrigida para "Hauteriviano a Barremiano", com a convenção
brasileira registrada entre parênteses em vez de apagada, e as unidades litoestratigráficas
nomeadas. Figura e claim atualizados. Moreira et al. (2007) acrescentada às fontes.
**Fonte:** Moreira, J. L. P. et al. (2007), "Bacia de Santos", *Boletim de Geociências da
Petrobras* 15(2), p. 531–549 · Karner & Gambôa (2007), GSL SP 285.
· **Nível:** revisada por pares. **Confiança:** confirmado.

---

## Verificado e correto

Auditoria que não acha nada só vale se mostrar o que olhou. Verificado contra fonte e
**mantido sem alteração**:

- **A conexão com o Módulo 10 (o ponto que a tarefa mandou verificar em especial).** As três
  correspondências afirmadas pela a03 estão **cientificamente corretas**: (i) *borda flexural
  de meio-graben → onlap* — a borda flexural é a rampa de mergulho suave do bloco do teto,
  oposta à falha principal, e é por definição a superfície contra a qual a sucessão sin-rifte
  faz onlap; a a03 usa a mesma definição que o Módulo 10 fixou após o achado
  `BACIAS-M10-A02-FLEXURAL-102`, sem reintroduzir a confusão com o alto de *footwall*.
  (ii) *discordância de ruptura → truncamento erosivo* — correto, e a a03 é cuidadosa ao
  acrescentar que a sucessão pós-rifte faz **onlap** sobre a mesma superfície, que é o que de
  fato se observa. (iii) *cunhas deltaicas progradantes pós-rifte → downlap* — correto.
  Nenhuma confusão introduzida. A única contradição real com o Módulo 10 estava na a06 e é o
  achado 🔴 3, em outro assunto (posição do *sag*).
- **Impedância acústica, Z = ρ·V, e a dissociação refletor ≠ contato litológico** (a01).
- **Cobertura múltipla / CMP e o ganho de sinal-ruído por empilhamento** (a01).
- **Zona de Fresnel como controle da resolução horizontal, e sua redução pela migração** (a01).
- **Perfil sônico e perfil de densidade** (RHOB por espalhamento Compton de raios gama),
  construção do sismograma sintético por convolução da série de RC com a wavelet, papel de
  *checkshot*/VSP como calibração independente mais confiável que o sônico isolado (a02).
- **Refletor como aproximação de superfície cronoestratigráfica**, com a ressalva de diacronia
  local mantida — a formulação da a03 não exagera a proposição de Vail et al. (1977).
- **Definição de sismofácies** (configuração interna, continuidade, amplitude, frequência,
  velocidade intervalar, geometria externa) e sua atribuição a Mitchum, Vail & Sangree (1977),
  parte 6 (a04) — atribuição correta.
- **Sigmoide vs. oblíqua e a razão aporte/acomodação** (a04): sigmoide indica acomodação
  abundante frente ao aporte, oblíqua o inverso com bypass no topo — bate com Mitchum et al.
- **Afogamento de plataforma carbonática ("give-up") e construção topográfica autogênica**
  (a04), incluindo o mecanismo alternativo por sufocamento siliciclástico.
- **Definição de sequência deposicional** (Mitchum, Vail & Thompson 1977) e **diagrama de
  Wheeler** (Wheeler 1958) — atribuições e conteúdo corretos (a05).
- **Associação estatística trato ↔ elemento de sistema petrolífero** (geradora na MFS,
  reservatório no LST, selo no TST), inclusive a ressalva explícita de que é tendência e não
  regra (a06) — a ressalva é o que salva a seção.
- **Critério de espessura constante vs. variável para separar deformação pós-deposicional de
  crescimento sinsedimentar** (a06) — critério padrão, corretamente enunciado nos dois sentidos.
- **Desacoplamento estrutural infra-sal/supra-sal e o desafio de imageamento sub-sal** (a06).
  O manifesto do autor sinalizava este último por precaução, como possivelmente sem fonte
  única; a dificuldade de imageamento através do sal (alta velocidade e geometria irregular
  distorcendo o campo de ondas, exigindo migração em profundidade com modelo de velocidade de
  sal) é consensual na literatura de processamento. **Não gera achado 🔵.**

---

## Correções aplicadas

**Aplicadas em:** 2026-08-30

| claim_id | Sev. | Desfecho | Arquivos alterados |
|---|---|---|---|
| `SISMO-M11-A01-WIDESS-004` | 🔴 | Corrigido | a01 (corpo, exemplo, recap, fontes, manifesto) |
| `SISMO-M11-A02-TIEDRIFT-006` | 🔴 | Corrigido | a02 (exemplo, recap, manifesto — claim `-DERIVA-006` criado) |
| `SISMO-M11-A06-SAG-005` | 🔴 | Corrigido com ressalva declarada | a06 (corpo, figura, recap, fontes, manifesto) |
| `SISMO-M11-A01-RC-006` | 🟠 | Corrigido | a01 (corpo, recap, manifesto) |
| `SISMO-M11-A01-ORDEM-007` | 🟠 | Corrigido | a01 (corpo, recap, manifesto) |
| `SISMO-M11-A01-BOWTIE-008` | 🟠 | Corrigido | a01 (corpo, recap, manifesto) |
| `SISMO-M11-A03-DIPTERM-005` | 🟠 | Corrigido | a03 (corpo, figura, recap, fontes, manifesto) |
| `SISMO-M11-A04-BROWNFISHER-006` | 🟠 | Corrigido | a04 (corpo, recap, fontes, manifesto) |
| `SISMO-M11-A04-RECIFE-007` | 🟠 | Corrigido | a04 (corpo, recap, manifesto) |
| `SISMO-M11-A05-FSST-006` | 🟠 | Corrigido | a05 (corpo, figura, exemplo, recap, fontes, manifesto) |
| `SISMO-M11-A06-TOPOSAL-009` | 🟠 | Corrigido | a06 (exemplo, manifesto — claim criado) |
| `SISMO-M11-A06-IDADERIFTE-008` | 🟠 | Corrigido | a06 (corpo, figura, manifesto) |

*(Doze linhas para dez achados: `-SAG-005` e `-IDADERIFTE-008` compartilham o mesmo parágrafo
e foram corrigidos na mesma edição, assim como `-BROWNFISHER-006` e `-RECIFE-007`; ficam
separados na tabela porque são alegações distintas e devem ser rastreáveis em separado.)*

**Pendências:** nenhuma. Nenhum achado 🔵 ou ⚪ ficou aberto; `open_findings` vazio.

**Material derivado a propagar:** nenhum. O módulo 11 ainda não tem questionário nem baralho
de flashcards — a auditoria rodou antes deles, como manda a cadeia. Nada a reimportar no Anki.

---

## Advertências ao gerador de questionários e de flashcards

Sete pontos mudaram nesta auditoria de forma que **gerar item a partir da versão antiga
produziria gabarito errado**. Os quatro primeiros são distratores de primeira qualidade,
justamente porque a versão errada é a que o senso comum (ou o material didático corrente)
sugere:

1. **Widess é λ/8, não λ/4.** O λ/4 é Rayleigh / espessura de sintonia. Uma questão "qual é o
   limite de Widess?" com alternativa λ/4 é o distrator mais forte do módulo inteiro.
2. **RC é razão de amplitudes, não de energias.** A energia refletida é RC².
3. **A ordem do processamento é deconvolução → empilhamento → migração**, não NMO primeiro.
4. **O topo plano do sal é deposicional.** O fluxo salífero torna o topo irregular, não plano.
5. **Existem quatro tratos de sistemas no modelo atual, e o quarto é o FSST**, não o SMST — e
   o SMST pertence ao modelo Exxon **original**, não a revisões posteriores.
6. **Downlap e toplap se definem por *downdip*/*updip*** e, no par *baselap*, pela inclinação
   **relativa** entre refletor e superfície — não pela inclinação absoluta da ponta da camada.
7. **Carbonatos têm duas assinaturas opostas:** plataforma estratificada (refletores internos
   fortes e contínuos) vs. *buildup* recifal (refletor-livre/caótico por dentro, monte por
   fora). Uma questão que peça "a assinatura sísmica de carbonatos" sem qualificar qual dos
   dois casos está mal formulada.

Duas advertências adicionais, de natureza diferente — pontos onde o material passou a declarar
uma **divergência real** em vez de uma resposta única, e onde uma questão de alternativa única
seria indevida:

8. **Posição da discordância de ruptura na margem brasileira** (abaixo do *sag*, como o curso
   adota, ou acima do sal). Avaliável como dissertativa que peça as duas leituras e o motivo da
   disputa; **não** como múltipla escolha com uma resposta certa.
9. **Fronteira LST/FSST** (a que trato pertencem os leques de assoalho de bacia e a incisão de
   vale). Mesma restrição: a resposta depende da convenção, e a aula agora dá as duas.
