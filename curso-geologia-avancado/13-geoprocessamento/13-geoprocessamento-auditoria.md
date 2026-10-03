# Auditoria científica — Módulo 13: Geoprocessamento

**Auditado em:** 2026-09-08 · **Modo:** `audit-and-fix` · **Profundidade:** `full`
**Material:** `13-geoprocessamento/` — 7 aulas (a01 a a07)
**Veredito:** **Aprovado com correções aplicadas** — nenhum achado 🔴 ou 🟠 em aberto.

## Resumo

🔴 2 erros · 🟠 9 imprecisos · 🟡 2 desatualizados · 🔵 0 sem fonte · ⚪ 1 controverso

**Total: 14 achados**, todos corrigidos. As 38 alegações auditáveis declaradas pelas sete aulas
foram usadas como ponto de partida e reverificadas contra fonte normativa ou primária; 22
passaram intactas, 9 tiveram o conteúdo corrigido e 7 tiveram apenas o ponteiro de capítulo da
fonte bibliográfica ajustado. Todos os cinco exemplos numéricos do módulo foram recalculados do
zero e **todos conferem** (detalhe ao final).

**O padrão dominante deste módulo é diferente do dos anteriores.** As aulas 04, 05, 06 e 07 —
a metade analítica do módulo, que é onde o risco factual costuma se concentrar — estão
conceitualmente limpas: overlay, buffer, dissolve, IDW, krigagem, spline, isolinhas, D8,
hipsometria, paletas e classificação foram verificados um a um contra Longley et al. (2015),
Burrough & McDonnell (1998), Isaaks & Srivastava (1989), O'Callaghan & Mark (1984), Strahler
(1952), Slocum et al. (2022) e Brewer (2016), sem nenhum erro de mecanismo ou de definição.
**Os dois achados vermelhos e a maioria dos laranjas estão concentrados na Aula 01 e na Aula 03
— isto é, na geodésia brasileira**, que é justamente a parte do módulo em que o dado correto é
normativo, datado e regional, e não dedutível do princípio geral. É um padrão coerente: onde o
autor podia raciocinar a partir do conceito, acertou; onde precisava do valor específico
publicado por um órgão brasileiro, escorregou.

---

## 🔴 1. Elipsoide do SAD69 trocado pelo do Córrego Alegre

**claim_id:** `GEOPROC-M13-A01-DATUM-002`
**Tipo:** erro factual
**Onde:** a01 · "Datum: o que fixa o modelo à Terra real"; "Exemplo trabalhado", Parte 2; manifesto
**Está escrito:** "o **SAD69** — South American Datum 1969, com origem no vértice Chuá, em Minas
Gerais, e elipsoide Internacional de 1924" · e, no exemplo: "SAD69: elipsoide Internacional
1924, origem topográfica no vértice Chuá".
**Problema:** o SAD69 **não** usa o elipsoide Internacional de Hayford (1924). Sua superfície de
referência é o elipsoide **UGGI-67 / GRS67** (*Geodetic Reference System 1967*, recomendado pela
União Geodésica e Geofísica Internacional em Lucerna, 1967), de semieixo maior 6.378.160 m e
achatamento 1/298,25. O elipsoide Internacional de Hayford 1924 (semieixo maior 6.378.388 m,
achatamento 1/297) é o do **Córrego Alegre**, o datum brasileiro *anterior* ao SAD69, em uso de
1950 a cerca de 1970. Trocar os dois é o erro clássico da geodésia brasileira, e aqui ele era
especialmente caro: a aula usa exatamente esse par de elipsoides como argumento de por que
coordenadas iguais em data diferentes caem em pontos diferentes do terreno — o argumento estava
certo, mas apoiado no elipsoide errado.
**Correção aplicada:** elipsoide do SAD69 corrigido para UGGI-67/GRS67 com o semieixo maior
explicitado, nos dois lugares do corpo e no manifesto; o Córrego Alegre foi nomeado no mesmo
parêntese como o datum que de fato usa Hayford 1924 — assim o aluno ganha a distinção em vez de
só perder o dado errado. O recap também passou a citar os dois data clássicos com seus
elipsoides corretos.
**Fonte:** IOGP, *EPSG Geodetic Parameter Dataset*, EPSG:6291 (South American Datum 1969) e
EPSG:4618; IBGE, *Sistemas de Referência* (documentação do SGB) para o Córrego Alegre. ·
**Nível:** normativa / base de referência.
**Confiança:** confirmado.
**Também aparece em:** nenhuma outra aula do módulo, e nenhum outro módulo do curso — a busca
transversal por `SAD69`/`Hayford` retornou apenas o Módulo 07 (a04), que cita "Córrego Alegre ou
SAD-69" sem atribuir elipsoide a nenhum dos dois. Sem propagação necessária.

---

## 🔴 2. Faixa da ondulação geoidal no Brasil subestimada em uma ordem de grandeza

**claim_id:** `GEOPROC-M13-A01-ONDULACAO-007`
**Tipo:** erro factual
**Onde:** a01 · "Elipsoide e geoide: dois modelos para uma Terra irregular"
**Está escrito:** "a **ondulação geoidal** (N), que no Brasil varia tipicamente entre -5 m e
-10 m dependendo da região — pequena, mas suficiente para introduzir erro significativo em
levantamentos de precisão se ignorada".
**Problema:** duplamente errado. Primeiro na **amplitude**: no modelo oficial brasileiro
MAPGEO2015 (IBGE/EPUSP), as isolinhas de ondulação geoidal são traçadas de 5 em 5 m ao longo de
uma faixa da ordem de -30 m a +30 m — dezenas de metros, não uma faixa de 5 m. Segundo no
**sinal**: o texto apresenta N como sempre negativo no Brasil, quando o modelo cobre valores
positivos e negativos conforme a região. A consequência didática do erro é a pior possível para
uma aula de fundamentos: apresentar como "pequena" uma correção que, ignorada, erra a altitude
em dezenas de metros — e a frase seguinte, sobre combinar altitude GNSS com altitude
ortométrica, dependia justamente dessa magnitude para fazer sentido.
**Correção aplicada:** faixa corrigida para a do MAPGEO2015, com o sinal duplo explicitado, e a
qualificação "pequena" removida. Aproveitou-se a correção para introduzir a relação
*h* = *H* + *N* (altitude geométrica, ortométrica e ondulação), que é o que torna a informação
operacional e que o parágrafo já pressupunha sem escrever. O recap foi ajustado no mesmo sentido.
**Fonte:** IBGE/EPUSP (2015), *MAPGEO2015 — Modelo de Ondulação Geoidal do Brasil*, cartograma
oficial e documentação técnica (grade de 5', modelo geopotencial EIGEN-6C4 + ~950.000 estações
gravimétricas na América do Sul). · **Nível:** normativa (órgão oficial).
**Confiança:** confirmado quanto à ordem de grandeza e ao sinal duplo; o texto corrigido usa
"da ordem de -30 m a +30 m", faixa do cartograma publicado, e não afirma extremos pontuais.
**Também aparece em:** só na a01 (corpo + recap + manifesto). Nenhum outro módulo do curso
menciona ondulação geoidal.

---

## 🟠 3. SIRGAS2000 e WGS84 tratados como coincidentes a poucos centímetros

**claim_id:** `GEOPROC-M13-A01-SIRGASWGS-008`
**Tipo:** desatualização / omissão que gera erro
**Onde:** a01 · "Datum: o que fixa o modelo à Terra real"
**Está escrito:** "SIRGAS2000 e WGS84 são, na prática, quase coincidentes (diferença da ordem de
poucos centímetros na maior parte da América do Sul)".
**Problema:** a afirmação era verdadeira **em 2000** e deixa de ser com o tempo, porque as duas
realizações têm naturezas diferentes: o SIRGAS2000 é um referencial **estático**, com
coordenadas congeladas na época de referência 2000,4, enquanto o WGS84 acompanha o ITRF, que é
**dinâmico**. Como a placa Sul-Americana desloca o território brasileiro a pouco mais de 1 cm
por ano para noroeste, a divergência acumula desde 2000 e hoje está na casa dos decímetros
(abaixo de 0,5 m). Apresentá-la como "poucos centímetros" numa aula que usa exatamente o
argumento do deslocamento silencioso induz o aluno a tratar os dois como intercambiáveis em
trabalho de precisão — o oposto do que a própria aula ensina três parágrafos antes.
**Correção aplicada:** parágrafo reescrito distinguindo a coincidência de **definição** (que se
mantém — não há parâmetros oficiais de transformação publicados entre os dois) da divergência de
**realização ao longo do tempo**, com a causa (movimento de placa, ~1 cm/ano para NW) e a ordem
de grandeza atual (decímetros, < 0,5 m). A frase de fechamento passou a exigir que o projeto
declare não só o sistema, mas a **época**.
**Fonte:** IBGE, *Projeto Mudança do Referencial Geodésico (PMRG)* e documentação do SGB
(velocidade da placa Sul-Americana e uso de modelos de velocidade); SIRGAS, definição da
realização SIRGAS2000 na época 2000,4. · **Nível:** normativa.
**Confiança:** confirmado.
**Também aparece em:** só na a01.

---

## 🟠 4. Data de oficialização do SIRGAS2000 no Brasil

**claim_id:** `GEOPROC-M13-A01-OFICIALIZACAO-009`
**Tipo:** impreciso
**Onde:** a01 · "Datum: o que fixa o modelo à Terra real" e "Recap relâmpago"
**Está escrito:** "o **SIRGAS2000** (...), oficializado no Brasil desde 2015 como o único datum
válido para cartografia" · e, no recap: "SIRGAS2000 é o único datum oficial no Brasil desde
2015".
**Problema:** confunde duas datas distintas. O SIRGAS2000 foi **adotado oficialmente em 25 de
fevereiro de 2005**, pela Resolução do Presidente do IBGE nº 1/2005, que instituiu um período de
transição de dez anos durante o qual ele podia conviver com SAD69 e Córrego Alegre. O que
aconteceu em 2015 (25 de fevereiro, Resolução PR nº 1/2015) foi o **término desse período de
transição** — a partir daí ele passou a ser o único sistema de referência válido no SGB e no
SCN. Como escrito, o texto sugere que nada existia antes de 2015 e apaga a década de transição,
que é exatamente o motivo de haver tanta base legada em SAD69 circulando — informação de que a
própria aula precisa para justificar seu exemplo trabalhado.
**Correção aplicada:** as duas datas separadas e nomeadas com suas resoluções, no corpo e no
recap.
**Fonte:** IBGE, Resolução do Presidente nº 1/2005 (25/02/2005) e Resolução do Presidente
nº 1/2015 (25/02/2015); Nota Técnica do IBGE sobre o término do período de transição. ·
**Nível:** normativa.
**Confiança:** confirmado.
**Também aparece em:** o Módulo 07 (a04) diz "SIRGAS 2000 (...) de adoção obrigatória desde
2015" e cita corretamente a "Resolução do Presidente nº 1/2005 e alterações posteriores" — está
certo e **não** precisou de correção; a formulação do M13 é que estava mais frouxa. Depois desta
correção, os dois módulos passam a dizer a mesma coisa.

---

## 🟠 5. PPP apresentado como sinônimo de pós-processamento

**claim_id:** `GEOPROC-M13-A03-PPP-007`
**Tipo:** erro factual de nomenclatura / confusão de escopo
**Onde:** a03 · "GPS e GNSS: como a posição em campo é medida", quarto marcador
**Está escrito:** "**Pós-processamento (PPP/pós-processado)**: os dados brutos do receptor móvel
são gravados e depois corrigidos em escritório, combinando-os com dados de estações de
referência (como a rede RBMC do IBGE no Brasil)".
**Problema:** o rótulo "PPP" está colado na descrição errada. O que o texto descreve —
combinar os dados do receptor com os de estações de referência de coordenadas conhecidas, como
as da RBMC — é **posicionamento relativo pós-processado** (estático, ou cinemático: PPK). O
**PPP** (*Precise Point Positioning*) é o método oposto nesse aspecto: processa o receptor
**isoladamente**, sem estação de referência, usando no lugar dela órbitas e correções de relógio
dos satélites de alta precisão (é o que faz o serviço on-line IBGE-PPP, baseado no CSRS-PPP do
NRCan), ao custo de um tempo de convergência bem maior. É uma confusão frequente no mercado
brasileiro, e num módulo que ensina a escolher o modo de posicionamento por campanha ela leva a
erro de planejamento real — quem acha que "PPP" significa "processar depois" pode dispensar a
base achando que fez o que não fez.
**Correção aplicada:** marcador reescrito separando explicitamente as duas famílias (relativo
pós-processado/PPK com RBMC; PPP com órbitas e relógios precisos, sem base), com a advertência
nomeada de que PPP não é sinônimo de pós-processamento. O recap foi ajustado no mesmo sentido, e
a fonte da RBMC nas Fontes ganhou a referência ao manual do IBGE-PPP.
**Fonte:** IBGE, *IBGE-PPP — serviço on-line de pós-processamento de dados GNSS* (manual do
usuário) e documentação da RBMC; Hofmann-Wellenhof, Lichtenegger & Wasle (2008), *GNSS*,
cap. 6-7. · **Nível:** normativa (órgão oficial) + revisada por pares.
**Confiança:** confirmado.
**Também aparece em:** só na a03.

---

## 🟠 6. Por que quatro satélites, e não três

**claim_id:** `GEOPROC-M13-A03-TRILATERACAO-004`
**Tipo:** omissão que gera erro
**Onde:** a03 · "GPS e GNSS: como a posição em campo é medida"
**Está escrito:** "combinando as distâncias a quatro ou mais satélites simultaneamente visíveis,
calcula sua própria posição tridimensional (x, y, z) por trilateração", seguido de uma lista de
fatores de erro em que "qualidade do relógio do receptor" aparece como mais um item qualquer.
**Problema:** como escrito, o número quatro fica arbitrário — e o leitor que souber geometria vai
concluir, corretamente, que **três** distâncias bastariam para fixar um ponto no espaço, e que o
quarto satélite seria só redundância. Não é: o quarto satélite é estruturalmente necessário
porque o relógio do receptor não é atômico e seu erro de sincronismo entra no sistema como uma
**quarta incógnita**, resolvida junto com x, y e z — razão pela qual as distâncias medidas se
chamam *pseudodistâncias*. Sem essa ressalva, a afirmação fica tecnicamente incompleta a ponto
de induzir modelo mental errado, e o termo "pseudodistância", que o aluno vai encontrar em
qualquer manual de receptor, fica sem explicação.
**Correção aplicada:** duas frases inseridas no parágrafo, explicando a quarta incógnita e
introduzindo o termo pseudodistância; a lista de fatores de erro foi preservada intacta (o
relógio do receptor continua sendo, também, fonte de erro residual). Recap ajustado.
**Fonte:** Hofmann-Wellenhof, Lichtenegger & Wasle (2008), *GNSS — Global Navigation Satellite
Systems*, cap. 5 (equação de pseudodistância e solução das quatro incógnitas). ·
**Nível:** revisada por pares.
**Confiança:** confirmado.
**Também aparece em:** só na a03.

---

## 🟠 7. "Álgebra de mapas vetorial" — o termo pertence ao raster

**claim_id:** `GEOPROC-M13-A04-ALGEBRA-006`
**Tipo:** erro de nomenclatura / confusão de escopo
**Onde:** a04 · "Relações topológicas e consultas espaciais" (corpo, recap e Fontes)
**Está escrito:** "Essas relações (contém, está dentro, cruza, toca, é adjacente a, está a uma
distância de) formam o vocabulário de **álgebra de mapas vetorial**" — com Tomlin (1990) citado
nas Fontes como "fundamentos de álgebra de mapas".
**Problema:** *álgebra de mapas*, no sentido de Tomlin (1990), é o formalismo de operações
**célula a célula sobre rasters** — somar, multiplicar, reclassificar camadas matriciais. Não é
o nome do vocabulário de relações topológicas entre geometrias vetoriais, que tem formalização
própria e bem estabelecida: o modelo **DE-9IM** (*Dimensionally Extended 9-Intersection Model*,
de Clementini e Egenhofer), adotado pela especificação OGC *Simple Feature Access* (ISO 19125) e
implementado em praticamente todo SIG e banco de dados espacial — é de lá que vêm os operadores
`equals`, `disjoint`, `intersects`, `touches`, `crosses`, `within`, `contains` e `overlaps` com
os mesmos nomes em softwares diferentes. **Este achado era também uma contradição transversal:**
o Módulo 07 (Aula 04) já ensina álgebra de mapas corretamente, como operação raster célula a
célula, e o mesmo curso passaria a usar o termo em dois sentidos incompatíveis.
**Correção aplicada:** o vocabulário passou a ser nomeado como **relações topológicas**, com o
DE-9IM e a especificação OGC citados como sua formalização, e uma ressalva explícita separando-o
da álgebra de mapas de Tomlin, apontada como raster e remetida à Aula 06. A lista de relações foi
ajustada para a do padrão (entrou `sobrepõe` e `é disjunto de`). Nas Fontes, entrou a referência
OGC/Clementini/Egenhofer, e a entrada de Tomlin foi requalificada como formalismo raster.
Recap ajustado.
**Fonte:** OGC, *Simple Feature Access* (ISO 19125); Egenhofer & Herring (1991) e Clementini &
Di Felice (1995), formulação do modelo de nove interseções; Tomlin (1990), *Geographic
Information Systems and Cartographic Modeling*, para o escopo raster do termo original. ·
**Nível:** normativa (OGC/ISO) + revisada por pares.
**Confiança:** confirmado.
**Também aparece em:** Módulo 07 (a04, flashcards 28/44, questionário) — todos **corretos**, no
sentido raster. Nenhuma correção necessária lá; era o M13 que divergia, e a correção restaura a
consistência do curso.

---

## 🟠 8. Capítulo errado de Longley et al. (2015) para overlay e buffer

**claim_id:** `GEOPROC-M13-A04-FONTELONGLEY-007`
**Tipo:** erro factual (bibliográfico)
**Onde:** a04 · Fontes + quatro claims do manifesto
**Está escrito:** "Longley, P. A. et al. (2015), *Geographic Information Science and Systems*,
4ª ed., Wiley, cap. 14 (análise espacial vetorial, overlay, buffer)".
**Problema:** na **4ª edição** (2015), o capítulo 14 é *Spatial Analysis and Inference*
(padrões de pontos, autocorrelação, inferência estatística). Overlay, buffer, medidas e consultas
espaciais estão no capítulo **13**, *Spatial Data Analysis*. O deslize tem origem provável na 3ª
edição, em que *Spatial Data Analysis* de fato era o capítulo 14 — exatamente o tipo de erro que
sobrevive a uma troca de edição na bibliografia. Não afeta nenhuma afirmação técnica do corpo da
aula, mas manda o aluno para o capítulo errado de uma obra que o curso recomenda.
**Correção aplicada:** ponteiro corrigido para cap. 13 (*Spatial Data Analysis*) nas Fontes e nos
quatro claims do manifesto que o citavam (`OVERLAY-001`, `BUFFER-002`, `DISSOLVE-003`,
`TOPOLOGIA-004`, `CALCULO-AREA-005`).
**Fonte:** Wiley, site companheiro oficial da 4ª edição (sumário completo dos 19 capítulos:
cap. 4 *Georeferencing*, cap. 13 *Spatial Data Analysis*, cap. 14 *Spatial Analysis and
Inference*). · **Nível:** base de referência (metadado editorial oficial).
**Confiança:** confirmado.
**Também aparece em:** a03 cita "Longley et al. 2015, cap. 4 (georreferenciamento...)" — **está
correto**, cap. 4 é *Georeferencing* na 4ª edição; a02 cita "cap. 3, 7-8" para modelos de dados,
geodatabase e coleta — também correto. Sem outras correções.

---

## 🟠 9. Capítulo errado de Burrough & McDonnell (1998) para interpolação

**claim_id:** `GEOPROC-M13-A05-FONTEBURROUGH-006`
**Tipo:** erro factual (bibliográfico)
**Onde:** a05 · Fontes + dois claims do manifesto
**Está escrito:** "Burrough, P. A. & McDonnell, R. A. (1998), *Principles of Geographical
Information Systems*, Oxford University Press, cap. 8 (métodos de interpolação espacial)".
**Problema:** o capítulo 8 da edição de 1998 é *Spatial Analysis using Continuous Fields*
(análise de superfícies — declividade, derivadas de MDE). Os métodos de interpolação estão no
capítulo **5**, *Creating Continuous Surfaces from Point Data* (IDW, spline e demais
determinísticos), e no capítulo **6**, *Optimal Interpolation using Geostatistics* (variograma e
krigagem). Ironia útil: a **Aula 06** cita corretamente "Burrough & McDonnell 1998, cap. 8
(análise de superfície)" para declividade — ou seja, o mesmo módulo aponta o cap. 8 para duas
coisas diferentes, e só uma delas estava certa.
**Correção aplicada:** ponteiro corrigido nas Fontes da a05 (cap. 5 e cap. 6, com os títulos dos
capítulos explicitados para não se perder de novo numa troca de edição) e nos claims
`IDW-002`, `KRIGAGEM-003` e `SPLINE-004` do manifesto. A citação da a06 foi conferida e
**mantida** — está correta.
**Fonte:** sumário oficial de Burrough & McDonnell (1998), *Principles of Geographical
Information Systems*, Oxford University Press. · **Nível:** base de referência.
**Confiança:** confirmado.
**Também aparece em:** a02 cita "cap. 2-3" para modelos de dados — correto (cap. 2 *Data Models
and Axioms*, cap. 3 *Geographical Data in the Computer*). Nota de consistência: o Módulo 07
(a04) cita a **3ª edição** da mesma obra (Burrough, McDonnell & Lloyd, 2015), enquanto o M13
cita a 2ª (1998). As duas citações são válidas, mas a numeração de capítulos difere entre elas —
registrado abaixo como advertência para o gerador.

---

## 🟠 10. Disponibilidade do SRTM a 30 m descrita como "refinamento de cobertura"

**claim_id:** `GEOPROC-M13-A06-SRTM-002`
**Tipo:** impreciso
**Onde:** a06 · "O que é um modelo digital de elevação"
**Está escrito:** "um MDE quase global com resolução original de 30 m (para a maior parte do
globo, incluindo o Brasil, desde o refinamento de cobertura completada em anos posteriores à
missão original de 2000)".
**Problema:** sugere que o dado de 30 m foi produzido depois, por refinamento — não foi. A missão
voou em fevereiro de 2000 e **já adquiriu** com espaçamento de 1 segundo de arco (~30 m) para
quase todo o globo entre 60°N e 56°S. O que mudou foi a **política de distribuição**: fora dos
Estados Unidos, por mais de uma década só se publicou a versão reamostrada para 3 segundos de
arco (~90 m); a liberação global de 1 segundo de arco começou em setembro de 2014 (América do
Sul em novembro de 2014) e se completou em 2015. A distinção não é histórica ociosa: ela explica
por que material mais antigo chama o SRTM de "MDE de 90 m" e por que é preciso conferir qual
versão do produto se tem em mãos — informação prática que a formulação original apagava.
**Correção aplicada:** parágrafo reescrito com a data da missão, o dado adquirido, a restrição de
distribuição, as datas da liberação global e a advertência prática sobre checar a versão do
produto. Manifesto atualizado.
**Fonte:** USGS EROS Archive, *SRTM 1 Arc-Second Global*; NASA Earthdata, comunicado da liberação
global de 1 arc-second da versão 3.0 (setembro de 2014). · **Nível:** normativa (agência
produtora do dado).
**Confiança:** confirmado.
**Também aparece em:** o Módulo 07 (a04) trata de sensoriamento remoto e resolução, mas não
atribui data nem resolução ao SRTM. Sem propagação.

---

## 🟠 11. ET-ADGV: sigla expandida errada e atribuída ao órgão errado

**claim_id:** `GEOPROC-M13-A07-NORMAS-005`
**Tipo:** erro factual (nomenclatura normativa)
**Onde:** a07 · Fontes + claim `ELEMENTOS-001` do manifesto
**Está escrito:** "Especificação Técnica para **Estruturação** de Dados Geoespaciais Vetoriais —
ET-ADGV (**DSG/IBGE**)".
**Problema:** três erros numa linha. (1) ET-ADGV é *Especificação Técnica para **Aquisição** de
Dados Geoespaciais Vetoriais*; quem trata de **estruturação** é a **ET-EDGV**, outra
especificação. (2) A atribuição a "DSG/IBGE" é incorreta: quem publica é a **DSG** (Diretoria de
Serviço Geográfico do Exército Brasileiro), no âmbito da INDE, com homologação pela **CONCAR** —
o IBGE não é o publicador dessas especificações. (3) Nem ET-ADGV nem ET-EDGV são a norma
pertinente ao tema desta aula: aquisição e estruturação de dados vetoriais não tratam de
simbologia nem de layout. A especificação da mesma família que trata disso é a **ET-RDG**
(*Representação de Dados Geoespaciais*).
**Correção aplicada:** entrada de Fontes reescrita nomeando corretamente as três especificações
com seus escopos e o publicador certo (DSG/Exército, homologação CONCAR), destacando a ET-RDG
como a pertinente a layout e simbologia; o Decreto nº 89.817/1984 entrou na mesma lista,
amarrando a a07 ao PEC usado na a03. Claim `ELEMENTOS-001` atualizado.
**Fonte:** DSG/Exército Brasileiro, Geoportal — páginas oficiais da ET-ADGV, ET-EDGV e ET-RDG;
INDE/CONCAR, ET-EDGV versão 3.0 (2017/2018). · **Nível:** normativa.
**Confiança:** confirmado.
**Também aparece em:** só na a07.

---

## 🟡 12. Faixa de 0,5 a 1,0 mm apresentada como convenção informal — é o PEC

**claim_id:** `GEOPROC-M13-A03-ERROGRAFICO-006`
**Tipo:** desatualização / afirmação sem a fonte normativa que a sustenta
**Onde:** a03 · "Exemplo trabalhado"
**Está escrito:** "um critério prático amplamente usado é que o erro de posição aceitável (...)
não deveria exceder (...) algo da ordem de 0,5 a 1,0 mm medidos na escala do próprio mapa (um
valor tipicamente adotado como limite de 'erro gráfico' tolerável ao olho humano (...))" — e, no
manifesto, "valor de referência pedagógico, **não substitui** o padrão de exatidão cartográfica
formal (PEC)".
**Problema:** a faixa citada não é uma convenção informal sobre o olho humano — ela **é** o PEC.
O Decreto nº 89.817/1984, art. 9º, fixa o Padrão de Exatidão Cartográfica planimétrico em
**0,5 mm** na escala da carta (Classe A), **0,8 mm** (Classe B) e **1,0 mm** (Classe C), com
erros-padrão correspondentes de **0,3 mm**, **0,5 mm** e **0,6 mm**. O texto tinha o número
certo com a genealogia errada, e a nota do manifesto chegava a negar a relação com o PEC.
Havia ainda uma imprecisão estatística embutida: o PEC é um critério de 90% dos pontos, e é ao
**erro-padrão** da classe, não ao valor do PEC, que se compara um RMSE.
**Correção aplicada:** o parágrafo passou a citar o Decreto 89.817/1984 com as três classes e
seus erros-padrão, e o exemplo foi refeito na métrica correta: 45 m equivalem a 0,45 mm na escala
1:100.000 — acima do erro-padrão da Classe A (30 m), dentro do da Classe B (50 m). A conclusão
original (aceitável para uso regional, inaceitável se a fonte fosse 1:5.000) **não muda**, mas
agora está ancorada em norma. Decreto acrescentado às Fontes da a03 e da a07; claim reescrito.
**Fonte:** Brasil, Decreto nº 89.817, de 20/06/1984, art. 8º e 9º (texto oficial). ·
**Nível:** normativa.
**Confiança:** confirmado.
**Também aparece em:** o Módulo 07 (a04) já mencionava "PEC/PEC-PCD" corretamente. A correção
alinha o M13 ao vocabulário que o curso já usava.

---

## 🟡 13. ABNT NBR 13133:1994 citada como vigente

**claim_id:** `GEOPROC-M13-A07-NBR13133-006`
**Tipo:** desatualização
**Onde:** a07 · Fontes
**Está escrito:** "ABNT NBR 13133:1994 (*Execução de levantamento topográfico*)".
**Problema:** a edição de 1994 não é a vigente. A norma foi revisada e a **ABNT NBR 13133:2021**
(*Execução de levantamento topográfico — Procedimento*) cancelou e substituiu a versão anterior,
incorporando altitude normal, posicionamento GNSS, varredura a laser, nivelamento GNSS e
critérios objetivos de aceitação — justamente os tópicos que este módulo ensina nas Aulas 01 e
03. Citar a edição de 1994 num módulo de geoinformação atual é o tipo de defasagem que envelhece
o material inteiro.
**Correção aplicada:** citação atualizada para NBR 13133:2021, com menção às edições que ela
substituiu (o aluno vai encontrar referências às versões antigas na literatura).
**Fonte:** ABNT NBR 13133:2021, *Execução de levantamento topográfico — Procedimento* (folha de
rosto: cancela e substitui a edição anterior). · **Nível:** normativa.
**Confiança:** confirmado.
**Também aparece em:** só na a07.

---

## ⚪ 14. "Geocodificação por coordenadas": divergência real de nomenclatura

**claim_id:** `GEOPROC-M13-A02-GEOCOD-005`
**Tipo:** controvérsia de nomenclatura
**Onde:** a02 · "Exemplo trabalhado" + recap + manifesto; ecoava no hub do módulo e na a07
**Está escrito:** "O procedimento padrão de um SIG é a operação de **geocodificação por
coordenadas** (às vezes chamada de 'XY Table to Point' ou equivalente, conforme o software)".
**Problema:** há divergência real entre fontes do mesmo nível, e o texto escolhia um lado sem
avisar. O glossário da ESRI define *geocoding* de forma ampla, incluindo a transformação de um
par de coordenadas numa posição — nesse sentido, o termo está defensável. Na maior parte da
bibliografia de SIG e no uso corrente de mercado, porém, *geocodificação* designa
especificamente a conversão de **endereços** (texto) em coordenadas, por correspondência com uma
base de logradouros — problema tecnicamente diferente, sujeito a erro de *matching* e a taxa de
acerto, que não existe na importação de uma tabela XY. Não é erro do autor; é ambiguidade
genuína, e num curso avançado ela precisa ser nomeada em vez de resolvida em silêncio.
**Correção aplicada:** conforme a política para achados ⚪, **não se escolheu um lado**. A
operação passou a ser nomeada pelo que faz (importação de tabela de coordenadas XY) e um
parágrafo curto registra as duas acepções e por que vale reservar "geocodificação" para o caso do
endereço. Recap, claim e as ocorrências no hub do módulo e na a07 (passo 3 do fluxo integrado)
foram alinhados.
**Fonte:** ESRI, *ArcGIS Pro Documentation* — XY Table to Point e verbete de glossário
*geocoding*; QGIS Documentation — *Add Delimited Text Layer*; Longley et al. (2015), cap. 4 e 8.
· **Nível:** base de referência (documentação de fornecedor) vs. literatura acadêmica.
**Confiança:** em disputa (por definição do achado).

---

## Recálculo independente dos exemplos quantitativos

Nenhum resultado numérico do módulo foi aceito por estar escrito no texto.

**a01 — escala a partir de medida de campo.** 1 km = 100.000 cm; 4 cm / 100.000 cm = 1/25.000 —
confere. 1 cm no mapa → 25.000 cm = 250 m — confere. Deslocamento de 65 m em escala 1:25.000:
6.500 cm / 25.000 = 0,26 cm = 2,6 mm — confere. **Todos os valores batem** (o deslocamento
SAD69→SIRGAS2000 de 60 a 70 m no Brasil foi conferido à parte contra a ordem de grandeza
consolidada nos parâmetros do IBGE — mantido).

**a03 — RMSE contra a escala do dado-fonte.** Em 1:100.000, 1 mm = 100 m — confere; 0,5 mm =
50 m e 1,0 mm = 100 m — conferem. Em 1:5.000, 1 mm = 5 m — confere. Valores acrescentados pela
correção 12: erros-padrão das Classes A/B/C = 0,3/0,5/0,6 mm = 30/50/60 m em 1:100.000 —
conferem; RMSE de 45 m = 0,45 mm na escala — confere, e cai entre o EP da Classe A e o da
Classe B, como o texto corrigido afirma. **Todos os valores batem.**

**a04 — buffer bilateral e área.** Largura total = 300 + 300 = 600 m — confere. Área ≈ 12.000 m ×
600 m = 7.200.000 m² = 7,2 km² — confere. Acréscimo das extremidades arredondadas, ignorado
deliberadamente pelo texto: π × 300² = 282.743 m² ≈ 0,28 km², ou 3,9% do total — a qualificação
"pequeno acréscimo" está adequada. Os 8,4 km² da área urbana e o 1,35 km² de interseção são
dados/resultado hipotéticos declarados como tais, internamente coerentes (1,35 < 7,2 e
1,35 < 8,4, como tem de ser numa interseção). **Todos os valores batem.**

**a06 — limiar de acumulação convertido em área.** 12,5 m × 12,5 m = 156,25 m² — confere.
500 × 156,25 = 78.125 m² — confere. 78.125 / 1.000.000 = 0,078125 km² ≈ 0,078 km² = 7,8125 ha ≈
7,8 ha — confere. Comparação com MDE de 30 m: 30² = 900 m²; 500 × 900 = 450.000 m² = 0,45 km² —
confere. Razão entre os dois: 0,45 / 0,078125 = 5,76 — "quase seis vezes maior" está correto.
**Todos os valores batem.**

**a06 — conversão declividade porcentagem/graus.** tan 45° = 1 = 100% — confere; a faixa 0° a
90° para declividade em graus está correta.

---

## Verificação transversal com módulos anteriores

Busca em todo o curso por `SAD69`, `SIRGAS`, `ondulação geoidal`, `álgebra de mapas`,
`geocodifica` e `Hayford`. Fora do Módulo 13, o vocabulário aparece só no **Módulo 07**
(Mapeamento geotécnico, a04 e seus derivados) e numa questão do **Módulo 08**.

- **Álgebra de mapas** — o M07 usa o termo corretamente, no sentido raster de Tomlin ("somar,
  multiplicar e reclassificar camadas célula a célula"), inclusive nos flashcards 28 e 44 e no
  questionário final do M08. O M13 (a04) o usava no sentido vetorial: **contradição transversal
  real**, resolvida pelo achado 7 em favor do M07, que estava certo. Nenhum material derivado do
  M07/M08 precisou de correção.
- **SIRGAS2000 / transformação de datum** — o M07 diz "adoção obrigatória desde 2015" e cita a
  Resolução PR nº 1/2005 "e alterações posteriores": correto. O M13 é que estava mais frouxo
  (achado 4). Depois da correção, os dois dizem a mesma coisa.
- **PEC** — o M07 já citava "PEC/PEC-PCD"; o M13 agora ancora a mesma norma pelo decreto
  (achado 12). Consistente.
- **Burrough & McDonnell** — o M07 cita a 3ª edição (2015, com Lloyd); o M13, a 2ª (1998). Ambas
  válidas, mas com numeração de capítulos diferente. Não é achado, e sim uma inconsistência
  editorial a vigiar.

Nenhuma contradição pendente entre módulos.

---

## Correções aplicadas

**Aplicadas em:** 2026-09-08

| claim_id | Sev. | Desfecho | Arquivos alterados |
|---|---|---|---|
| `GEOPROC-M13-A01-DATUM-002` | 🔴 | Corrigido | aula-01 |
| `GEOPROC-M13-A01-ONDULACAO-007` | 🔴 | Corrigido | aula-01 |
| `GEOPROC-M13-A01-SIRGASWGS-008` | 🟠 | Corrigido | aula-01 |
| `GEOPROC-M13-A01-OFICIALIZACAO-009` | 🟠 | Corrigido | aula-01 |
| `GEOPROC-M13-A03-PPP-007` | 🟠 | Corrigido | aula-03 |
| `GEOPROC-M13-A03-TRILATERACAO-004` | 🟠 | Corrigido | aula-03 |
| `GEOPROC-M13-A04-ALGEBRA-006` | 🟠 | Corrigido | aula-04 |
| `GEOPROC-M13-A04-FONTELONGLEY-007` | 🟠 | Corrigido | aula-04 |
| `GEOPROC-M13-A05-FONTEBURROUGH-006` | 🟠 | Corrigido | aula-05 |
| `GEOPROC-M13-A06-SRTM-002` | 🟠 | Corrigido | aula-06 |
| `GEOPROC-M13-A07-NORMAS-005` | 🟠 | Corrigido | aula-07 |
| `GEOPROC-M13-A03-ERROGRAFICO-006` | 🟡 | Corrigido | aula-03 (+ Fontes da aula-07) |
| `GEOPROC-M13-A07-NBR13133-006` | 🟡 | Corrigido | aula-07 |
| `GEOPROC-M13-A02-GEOCOD-005` | ⚪ | Corrigido com ressalva (duas acepções registradas, sem escolha de lado) | aula-02, aula-07, hub do módulo |

**Pendências:** nenhuma. Nenhum achado 🔴 ou 🟠 em aberto — o gate para o gerador de
questionários e o de flashcards está liberado.

**Material derivado:** nada a propagar. O módulo ainda não tem questionário nem baralho — a
auditoria rodou antes deles, como manda a cadeia. Nada a reimportar no Anki.

---

## Nota de validação estrutural

`validate_links.py` e `validate_state.py` foram executados depois das correções. Nenhum link
quebrado foi introduzido — os 16 erros de link do curso são pré-existentes e todos em
`flashcards.md` de outros módulos (wikilink apontando para arquivo `.csv`, que o validador não
resolve como nota).

Em `validate_state.py`, o Módulo 13 acrescenta duas famílias de erro, ambas de **convenção, não
de conteúdo**, e nenhuma delas nova no curso:

1. **`lesson.count` e `state.schema` de status** — o schema do plugin espera `completed`,
   `approved` e `approved_with_reservations`; este curso usa `complete` em todos os módulos
   desde o 01. Adotar o valor do schema só no Módulo 13 quebraria a consistência com os doze
   módulos anteriores, então mantive a convenção do curso. A divergência é do curso inteiro
   contra o schema, e a correção certa é uma passagem única de normalização, não um remendo
   local.
2. **`audit.manifest.schema` / `claim_id`** — o schema exige o padrão
   `^[A-Z]{2,4}-[A-Z0-9]+-[A-Z0-9]+-[0-9]{3}$` (quatro segmentos, prefixo de 2 a 4 letras). Os
   `claim_id` deste módulo têm cinco segmentos e prefixo de sete letras
   (`GEOPROC-M13-A01-DATUM-002`), porque essa é a convenção que o próprio autor das aulas usou
   nos blocos `alegacoes_auditaveis` — e o manifesto do Módulo 12 já falha no mesmo teste, pelo
   mesmo motivo. Renumerar os IDs para satisfazer o schema quebraria a rastreabilidade com os
   manifestos das aulas e com o histórico, e a política desta skill é explícita em não reciclar
   nem renumerar `claim_id`. Fica registrado para o mantenedor do plugin: ou o schema se afrouxa
   para o padrão que o curso adotou, ou a normalização é feita de uma vez em todos os módulos.

Duas correções foram aplicadas ao manifesto para eliminar erros que **eram** legítimos:
`confidence` passou de `"em disputa"` para `"em_disputa"` (valor do enum), e os campos de raiz
`numeric_recheck`, `cross_module_check` e `derived_material_note`, que o schema não permite,
saíram do `.json` — o conteúdo deles permanece neste relatório e no `course-state.yaml`.

---

## Advertências para o gerador de questionários e de flashcards

1. **Não gere questão nem card que atribua o elipsoide Internacional/Hayford 1924 ao SAD69.** O
   par correto é: Córrego Alegre → Hayford 1924; SAD69 → UGGI-67/GRS67; SIRGAS2000 → GRS80. Esse
   trio é excelente material de questão de discriminação — e um distrator perfeito é exatamente
   o erro que esta auditoria corrigiu.
2. **A ondulação geoidal no Brasil é de dezenas de metros e tem os dois sinais.** Qualquer card
   com faixa estreita ou só negativa está errado. A relação *h* = *H* + *N* rende card de cálculo.
3. **SIRGAS2000: duas datas, não uma.** 2005 (adoção, Res. PR 1/2005) e 25/02/2015 (fim da
   transição, Res. PR 1/2015). Uma questão que peça a distinção vale mais que uma que peça "a
   data".
4. **PPP ≠ pós-processamento.** Ponto contraintuitivo e de erro corrente no mercado: rende ótima
   questão de aplicação ("campanha em área remota sem base próxima — qual método?") e um
   distrator forte.
5. **Quatro satélites por causa da quarta incógnita (relógio do receptor).** Distrator natural:
   "três, porque a posição é tridimensional".
6. **Álgebra de mapas é raster (Tomlin); relações topológicas vetoriais são DE-9IM/OGC.** O
   Módulo 07 já cobra álgebra de mapas no sentido raster — não crie questão no M13 que contradiga
   aquele gabarito.
7. **PEC: compare RMSE com o erro-padrão, não com o valor do PEC.** Classes A/B/C = 0,5/0,8/1,0
   mm (PEC) e 0,3/0,5/0,6 mm (EP). Questão de cálculo pronta: dado um RMSE e uma escala, em que
   classe o produto se enquadra.
8. **SRTM: 30 m desde a aquisição (2000); o que mudou em 2014-2015 foi a liberação.** Distrator:
   "a resolução foi melhorada por reprocessamento".
9. **Limiar de acumulação de fluxo depende da resolução.** O exemplo da a06 (500 células a 12,5 m
   vs. a 30 m) é o melhor candidato a questão de aplicação quantitativa do módulo.
10. **Cuidado com "geocodificação"** ao redigir enunciados: use "importação de tabela XY" e
    reserve geocodificação para endereço, como as aulas corrigidas fazem.
