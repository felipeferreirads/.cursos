# Auditoria científica: Módulo 18 — Tectônica global e geodinâmica

**Auditado em:** 2026-08-18
**Material:** `18-tectonica-global-geodinamica/` — seis aulas, questionário final cumulativo e baralho de flashcards (`.md`, `-basic.csv`, `-cloze.csv`), auditados em conjunto
**Modo:** audit-and-fix
**Profundidade:** full
**Escopo:** cinemática de placas e polos de Euler, forças motrizes, convecção e plumas mantélicas, mecanismos de subsidência e tipos de bacia, ciclo de Wilson, colisão continental e acresção de terrenos, crátons e quilhas litosféricas, ciclo dos supercontinentes; consistência entre aulas e entre aulas, questionário e baralho
**Veredito da Fase 1:** Requer correção
**Veredito após a Fase 2:** Aprovado
**Reverificado em:** 2026-08-18 (segunda passada independente: os 12 achados originais foram reconferidos no texto dos arquivos e contra fonte; três achados novos foram encontrados e corrigidos)
**Veredito final:** Aprovado (todos os achados corrigidos; nenhum 🔴/🟠 aberto)

## Resumo

🔴 1 erro · 🟠 12 imprecisões · 🟡 0 desatualizados · 🔵 1 sem fonte · ⚪ 1 controverso Verificadas e corretas: 18 alegações de risco.

Os achados 1–12 são da primeira passada; os achados 13–15 foram encontrados na reverificação.

## Achados

### 🔴 1. Pangeia Ultima foi classificada como fechamento extrovertido

**claim_id:** `TEC-SUPERC-ULTIMA-001`
**Tipo:** erro factual
**Onde:** `18-tectonica-global-geodinamica-aula-06-ciclo-dos-supercontinentes.md` · "E o próximo supercontinente?" e Recap
**Está escrito:** "**Pangeia Ultima** (fechamento extrovertido, consumindo o Atlântico) ou **Amásia** (reunião em torno do Ártico, unindo América e Ásia)"
**Problema:** os rótulos estão trocados. Na literatura os três cenários canônicos são definidos exatamente pelo oceano que se fecha: **Pangeia Ultima** é o cenário de **introversão** — fechamento do oceano *interior*, o Atlântico, aberto na fragmentação da Pangeia; **Novopangeia** é o cenário de **extroversão** — fechamento do oceano *exterior*, o Pacífico; **Amásia** é **ortoversão** — reunião a ~90° do supercontinente anterior. Chamar Pangeia Ultima de "extrovertida" inverte a definição do próprio termo que a aula ensinou no vocabulário, e o cenário extrovertido (Novopangeia) ficava ausente da aula.
**Correção proposta:** apresentar os três cenários com o modo de fechamento correspondente — Pangeia Ultima (introversão, fecha o Atlântico), Novopangeia (extroversão, fecha o Pacífico), Amásia (ortoversão, em torno do Ártico).
**Fonte:** Davies, Green & Duarte (2018), *Back to the future: testing different scenarios for the next supercontinent gathering*, Global and Planetary Change; Davies, Green & Duarte (2020), *Back to the future II*, Earth System Dynamics 11, 291 — https://esd.copernicus.org/articles/11/291/2020/ ; Mitchell, Kilian & Evans (2012), Nature 482, 208–211 · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Recap da aula 06; "Erros comuns" da aula 06; flashcard `fb020`; índice do baralho (`flashcards.md`, coluna "Núcleo recuperado" de OA05).

### ⚪ 2. Pannótia apresentada como etapa consolidada do ciclo dos supercontinentes

**claim_id:** `TEC-SUPERC-PANNOTIA-002`
**Tipo:** controvérsia apresentada como consenso (certeza indevida)
**Onde:** aula 06 · "Os principais supercontinentes propostos" e Exemplo trabalhado; questionário · gabarito da Q14
**Está escrito:** "Um supercontinente intermediário frequentemente citado entre Rodínia e Pangeia é **Pannótia** (também chamada Gondwana pan-africana em algumas formulações)"; e, no gabarito, "O intervalo (~600–550 Ma) é mais provavelmente associado a **Pannótia/Gondwana**"
**Problema:** o estatuto de Pannótia é objeto de disputa aberta e publicada. A geocronologia dos orógenos ediacaranos–cambrianos sugere que o agrupamento começou a se fragmentar antes de terminar de se montar, e há literatura que nega sua existência como massa continental coerente (Nance & Murphy, *Pannotia: to be or not to be?*) e literatura que a defende explicitamente (Murphy, Nance et al., *Pannotia: in defence of its existence and geodynamic significance*). O material apresentava a existência como fato assentado, e o gabarito da Q14 fazia dela a resposta esperada — transformando uma disputa em item de prova. O apelido "Gondwana pan-africana" também não é a designação corrente (usa-se "Gondwana maior" ou supercontinente vendiano).
**Correção proposta:** manter Pannótia no material, com a janela c. 650–540 Ma, marcada explicitamente como **hipótese em disputa**, e apontar que a amalgamação do Gondwana Ocidental no mesmo intervalo é bem menos controversa. No gabarito da Q14, aceitar tanto "Pannótia" quanto "Gondwana (Ocidental)" e creditar quem registrar a disputa.
**Fonte:** Nance & Murphy (2022), *Pannotia: to be or not to be?*, Earth-Science Reviews — https://www.sciencedirect.com/science/article/abs/pii/S0012825222002124 ; Murphy, Nance et al. (2021), *Pannotia: in defence of its existence and geodynamic significance*, Geological Society, London, Special Publications 503 · **Nível:** revisada por pares (divergência real entre fontes do mesmo nível)
**Confiança:** em disputa
**Também aparece em:** aula 06 (Exemplo trabalhado, item 2) e questionário (gabarito e rubrica da Q14). Nenhum flashcard cobria Pannótia.

### 🟠 3. Deriva da pluma do Havaí descrita como "contribuição menor"

**claim_id:** `TEC-PLUMA-HAVAI-003`
**Tipo:** imprecisão / certeza indevida
**Onde:** `19-...-aula-02-margens-de-placa-e-geodinamica-do-manto.md` · Exemplo trabalhado e "Erros comuns"
**Está escrito:** "a explicação completa combina **movimento da placa** e uma **contribuição menor de deslocamento da pluma**"; e "evidências de exceções e deslocamentos lentos em casos específicos"
**Problema:** os dados paleomagnéticos de testemunhos da cadeia Imperador indicam deriva do ponto quente havaiano para o sul de 11° a 15° de latitude entre ~81 e ~47 Ma, a taxas **acima de 40 mm/ano** — a mesma ordem de grandeza da velocidade da placa, e não uma contribuição "menor" nem um deslocamento "lento". Mais: a causa da inflexão é objeto de debate ativo, com trabalhos que a atribuem principalmente à mudança de movimento da Placa do Pacífico e outros que a atribuem principalmente ao movimento do ponto quente. O texto fechava esse debate a favor de um lado.
**Correção proposta:** dar os números da deriva, dizer que ela é comparável à velocidade da placa e declarar o debate como aberto.
**Fonte:** Tarduno et al. (2003), *The Emperor Seamounts: southward motion of the Hawaiian hotspot plume in Earth's mantle*, Science 301, 1064–1069 — https://www.science.org/doi/10.1126/science.1086442 ; Torsvik et al. (2017), *Pacific plate motion change caused the Hawaiian-Emperor Bend*, Nature Communications 8, 15660 · **Nível:** revisada por pares
**Confiança:** confirmado (quanto à deriva) · em disputa (quanto ao peso relativo das causas)
**Também aparece em:** manifesto `alegacoes_auditaveis` da aula 02 (`GEO-M18-A02-HAVAI-002`); questionário, gabarito e rubrica da Q04; flashcard `fc003` (campo *extra*).

### 🟠 4. Termo inglês incorreto no vocabulário: "slab push/pull"

**claim_id:** `TEC-FORCAS-SLABPULL-004`
**Tipo:** imprecisão nomenclatural
**Onde:** `19-...-aula-01-cinematica-de-placas-e-forcas-motrizes.md` · Vocabulário
**Está escrito:** "| **Puxão de placa (slab push/pull)** | Força de tração exercida pela porção de placa que afunda..."
**Problema:** a definição em português está correta, mas o termo inglês entre parênteses não. A força de tração da placa em subducção é **slab pull**; "slab push" não é um termo da literatura, e a barra sugere que os dois nomeiam a mesma coisa. Como o glosário existe justamente para permitir ao aluno buscar o termo original, um termo inexistente é uma armadilha de busca. O resto da aula (seção "O motor", Recap, flashcards `fb002` e `fc002`) já usava "slab pull" corretamente — ou seja, era também uma inconsistência interna.
**Correção proposta:** "**Puxão de placa (slab pull)**".
**Fonte:** Forsyth & Uyeda (1975), *On the relative importance of the driving forces of plate motion*, Geophysical Journal of the Royal Astronomical Society 43, 163–200 — https://academic.oup.com/gji/article/43/1/163/586101 ; Conrad & Lithgow-Bertelloni (2002), *How mantle slabs drive plate tectonics*, Science 298, 207–209 · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** somente no vocabulário da aula 01.

### 🟠 5. Analogia da unha ancorada no topo da faixa de velocidades

**claim_id:** `TEC-VEL-UNHA-005`
**Tipo:** imprecisão numérica (analogia que ensina ordem de grandeza errada)
**Onde:** aula 01 · "Como se mede o movimento"
**Está escrito:** "variam de poucos milímetros por ano (limites lentos) a mais de 10 cm/ano (algumas taxas de convergência no Pacífico) — para comparação, essa é aproximadamente a velocidade de crescimento de uma unha humana."
**Problema:** o pronome "essa" se prende ao número imediatamente anterior, 10 cm/ano. Unha humana cresce cerca de 1 a 3,6 cm/ano; a analogia clássica do USGS vale para a faixa central de "poucos centímetros por ano", não para o topo da faixa, que é três a dez vezes mais rápido. Como escrita, a frase ensina uma ordem de grandeza errada logo num ponto que o aluno vai memorizar.
**Correção proposta:** ancorar a analogia explicitamente na faixa central e sinalizar que o topo da faixa é várias vezes mais rápido.
**Fonte:** USGS, *This Dynamic Earth — Understanding plate motions* — https://pubs.usgs.gov/gip/dynamic/understanding.html (dorsal do Ártico < 2,5 cm/ano; Dorsal Meso-Atlântica ~2,5 cm/ano; Dorsal do Pacífico Leste > 15 cm/ano), consulta em 2026-08-18 · **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** somente na aula 01. Nenhum flashcard ou questão cobrava esse número.

### 🟠 6. Extensão de retroarco equiparada ao próprio rollback

**claim_id:** `TEC-BACIA-ROLLBACK-006`
**Tipo:** imprecisão de mecanismo (causa e efeito colapsados)
**Onde:** `19-...-aula-03-tectonica-e-bacias-sedimentares.md` · "Subducção: duas bacias, dois lados da fossa"
**Está escrito:** "pode se formar por extensão local (quando o próprio processo de subducção estica a litosfera atrás do arco, um fenômeno chamado recuo de fossa ou *rollback*)"
**Problema:** o aposto nomeia como *rollback* o estiramento da litosfera, quando *rollback* é o recuo da fossa — a placa que subduz se verticaliza e a charneira migra em direção ao oceano. A extensão de retroarco é a **consequência** desse recuo, não o recuo. Colapsar causa e efeito deixa o aluno sem o mecanismo que a aula se propõe a ensinar.
**Correção proposta:** separar explicitamente o recuo da fossa (causa) da extensão atrás do arco (efeito).
**Fonte:** Schellart & Moresi / literatura de bacias de retroarco: *Dynamics of slab rollback and induced back-arc basin formation*, Earth and Planetary Science Letters (2012) — https://www.sciencedirect.com/science/article/abs/pii/S0012821X12006000 ; síntese global em Earth-Science Reviews (2022), *Back-arc basins: a global view from geophysical synthesis and analysis* · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** somente na aula 03. O flashcard `fb008` cobre antearco e não toca no mecanismo de retroarco.

### 🟠 7. Embasamento da Bacia do Paraná descrito como cratônico simples

**claim_id:** `TEC-CRATON-PARANA-007`
**Tipo:** omissão que gera erro
**Onde:** `19-...-aula-05-cratons-escudos-e-estabilizacao-continental.md` · "Dois compartimentos dentro de um mesmo cráton"
**Está escrito:** "A Bacia do Paraná [...] se assenta sobre embasamento cratônico da Plataforma Sul-Americana."
**Problema:** a frase é usada como exemplo de "bacia cratônica" logo depois de a aula definir escudo e bacia cratônica como duas faces do **mesmo** cráton — e o embasamento da Bacia do Paraná não é um cráton único. É um mosaico de blocos cratônicos (Paranapanema, Rio de la Plata, Luís Alves, além de bordas amazônica e do São Francisco) soldados por faixas móveis neoproterozoicas brasilianas, e é por isso que a literatura a classifica como bacia **intracratônica** e não como cobertura de um cráton. Como escrito, o exemplo contradiz a definição que a própria aula acabou de dar.
**Correção proposta:** descrever o embasamento como heterogêneo (blocos cratônicos + faixas brasilianas) e nomear a bacia como intracratônica.
**Fonte:** Milani et al. (2007), *Bacia do Paraná*, Boletim de Geociências da Petrobras 15(2), 265–287; Affonso et al. (2021), *Lithospheric architecture of the Paranapanema Block and adjacent nuclei*, JGR Solid Earth — https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2020JB021183 ; SGB/CPRM, léxico e mapas da Plataforma Sul-Americana · **Nível:** revisada por pares + serviço geológico nacional
**Confiança:** confirmado
**Também aparece em:** somente na aula 05. Os flashcards `fb016` e `fc012` definem bacia cratônica sem citar o Paraná — permanecem válidos.

### 🟠 8. Causalidade invertida na hipótese de padrões de manto

**claim_id:** `TEC-SUPERC-MANTO-008`
**Tipo:** imprecisão de mecanismo
**Onde:** aula 06 · "Por que os continentes voltam a se reunir? Duas famílias de hipótese", item 2
**Está escrito:** "regiões anomalamente quentes sob o antigo oceano que cercava o supercontinente, que poderiam favorecer padrões de subducção que 'puxam' os fragmentos de volta para se reunirem"
**Problema:** a cadeia causal está ao contrário. Nos modelos de manto de grau 2, as duas regiões quentes e aproximadamente antipodais (as LLSVPs africana e pacífica) estão associadas antes à **ruptura** de um supercontinente do que à sua reunião; os continentes tendem a se reagrupar sobre o **cinturão de manto descendente** que separa essas duas regiões — é exatamente esse o conteúdo da hipótese de ortoversão. Dizer que a região quente "favorece subducção que puxa os fragmentos de volta" atribui a reunião à estrutura errada.
**Correção proposta:** descrever a estrutura de grau 2 (duas regiões quentes antipodais + cinturão descendente), situar a reunião sobre o cinturão descendente e nomear a ortoversão.
**Fonte:** Mitchell, Kilian & Evans (2012), Nature 482, 208–211; Zhong et al. (2007), degree-1/degree-2 mantle convection e o ciclo dos supercontinentes; síntese em *The evolution of basal mantle structure in response to supercontinent aggregation and dispersal*, Scientific Reports (2021) — https://www.nature.com/articles/s41598-021-02359-z · **Nível:** revisada por pares
**Confiança:** confirmado quanto ao sentido da associação; os detalhes causais seguem em pesquisa ativa, e o texto corrigido declara isso
**Também aparece em:** Recap da aula 06 (item sobre as duas famílias de hipótese).

### 🟠 9. Falhas de alto ângulo chamadas de "suturas" sem o critério da própria aula

**claim_id:** `TEC-OROG-SUTURA-009`
**Tipo:** inconsistência interna
**Onde:** `19-...-aula-04-orogenese-colisao-e-crescimento-de-cadeias.md` · Exemplo trabalhado, passo 2
**Está escrito:** "As falhas de alto ângulo que os separam são consistentes com **suturas de acresção**, marcando onde cada terreno foi soldado à margem."
**Problema:** o vocabulário da mesma aula define sutura como zona que "muitas vezes preserva fragmentos de crosta oceânica antiga", e a seção "Como diferenciar as duas na prática" usa a presença de fragmentos de crosta oceânica ou arcos como o critério de reconhecimento. No exemplo, porém, o único dado é descontinuidade estratigráfica entre blocos e falhas de alto ângulo — nada de material oceânico. Pelo critério que a aula acabou de estabelecer, o que se tem é um **limite de terreno**; "sutura" é a hipótese a testar, não a leitura já feita. O passo 3 do próprio exemplo é mais cauteloso ("a confirmação completa exigiria dados paleomagnéticos e geocronológicos"), o que confirma a inconsistência entre os passos 2 e 3.
**Correção proposta:** nomear os contatos como limites de terreno e explicitar que a promoção a sutura depende de preservação de material da litosfera oceânica consumida (ofiolitos, mélanges).
**Fonte:** Coney, Jones & Monger (1980), *Cordilleran suspect terranes*, Nature 288, 329–333; uso corrente de "sutura" e "terrane-bounding fault" na literatura de acresção cordilherana · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** o gabarito da Q09 não usa "sutura" e não precisou de ajuste; os flashcards `fb009`, `fb012`, `fc007` e `fc008` definem sutura e ofiolito corretamente e permanecem válidos.

### 🟠 10. Eras da Rodínia listadas em ordem invertida

**claim_id:** `TEC-SUPERC-RODINIA-ERA-010`
**Tipo:** inconsistência interna
**Onde:** aula 06 · "Os principais supercontinentes propostos"
**Está escrito:** "1.100 a 750 milhões de anos atrás (Neoproterozoico/Mesoproterozoico)"
**Problema:** os números vão do mais antigo ao mais recente, mas as eras vêm na ordem oposta. 1.100 Ma é Mesoproterozoico (Esteniano) e 750 Ma é Neoproterozoico (Toniano) na carta vigente da ICS. O item vizinho, sobre Columbia, usa a convenção correta ("Paleo a Mesoproterozoico") — logo a inversão é também uma inconsistência de convenção dentro da mesma lista, num ponto em que a aula está justamente ensinando ordenação cronológica (cobrada na Q12).
**Correção proposta:** "(do Mesoproterozoico ao Neoproterozoico)".
**Fonte:** ICS, *International Chronostratigraphic Chart*, versão vigente em 2026 (Esteniano 1200–1000 Ma; Toniano 1000–720 Ma) — https://stratigraphy.org/chart · **Nível:** normativa
**Confiança:** confirmado
**Também aparece em:** os intervalos numéricos em `fb018` e `fc014` estão corretos e não citam eras — sem propagação.

### 🟠 11. Regra do polo de Euler aplicada à Dorsal Meso-Atlântica inteira

**claim_id:** `TEC-CINEM-MAR-ESCOPO-011`
**Tipo:** confusão de escopo
**Onde:** aula 01 · Exemplo trabalhado, passo 3
**Está escrito:** "Por isso, ao longo de toda a Dorsal Meso-Atlântica a taxa de espalhamento não é uniforme: cresce da região mais próxima ao polo em direção à região mais distante dele"
**Problema:** o exemplo trabalhado é montado sobre o par América do Sul–África, mas a conclusão é estendida a "toda a Dorsal Meso-Atlântica" — que não é o limite de um único par de placas. Ao norte da junção tríplice dos Açores ela separa América do Norte–Eurásia; ao sul, América do Sul–África. São pares com polos de Euler distintos, e um único polo não descreve a dorsal inteira. A própria aula já tinha enunciado a regra corretamente ("o polo de Euler daquele par de placas") no início — a extensão indevida está só neste passo.
**Correção proposta:** restringir a conclusão ao segmento do par de placas em questão e explicitar por que a dorsal inteira não serve como exemplo único.
**Fonte:** USGS, *This Dynamic Earth — Understanding plate motions* — https://pubs.usgs.gov/gip/dynamic/understanding.html ; taxas do sistema Ártico–Islândia decrescendo de ~18 para ~12,7 mm/ano em direção ao norte, e ~6 mm/ano no extremo da Dorsal de Gakkel (Cochran et al., 2003, JGR Solid Earth) · **Nível:** base de referência + revisada por pares
**Confiança:** confirmado
**Também aparece em:** somente no exemplo trabalhado da aula 01. A afirmação anterior sobre a Islândia (par América do Norte–Eurásia) está correta e foi mantida.

### 🔵 12. A URL da fonte USGS citada na aula 01 não resolve

**claim_id:** `TEC-FONTE-USGS-URL-012`
**Tipo:** evidência insuficiente (fonte não verificável na referência dada)
**Onde:** aula 01 · Fontes
**Está escrito:** "USGS, [Understanding plate motions](https://www.usgs.gov/programs/earthquake-hazards/science/understanding-plate-motions), consulta em 2026-08-18."
**Problema:** a URL retorna HTTP 404. A fonte é a certa e sustenta o conteúdo da aula, mas na referência dada ela não é recuperável — quem quiser refazer a verificação não chega ao documento, e a data de consulta declarada não pode estar correta para um endereço que não responde. Não é acusação de erro no conteúdo; é falha de rastreabilidade.
**Correção proposta:** substituir pela URL canônica do capítulo em *This Dynamic Earth*, `https://pubs.usgs.gov/gip/dynamic/understanding.html`, que hospeda o material citado.
**Fonte:** USGS, *This Dynamic Earth: the story of plate tectonics* — https://pubs.usgs.gov/gip/dynamic/understanding.html · **Nível:** base de referência
**Confiança:** confirmado (quanto ao conteúdo) · a URL original não é verificável
**Também aparece em:** a aula 02 cita `https://pubs.usgs.gov/gip/dynamic/` e `https://pubs.usgs.gov/gip/dynamic/hotspots.html`, ambas no domínio correto — não foram alteradas.

### 🟠 13. Os cenários de próximo supercontinente foram apresentados como três, e a fonte citada define quatro

**claim_id:** `TEC-SUPERC-AURICA-031`
**Tipo:** omissão que gera erro
**Onde:** aula 06 · "E o próximo supercontinente?", "Erros comuns" e Recap
**Está escrito:** "cada cenário corresponde a um modo de fechamento diferente: **Pangeia Ultima** (introversão), **Novopangeia** (extroversão) e **Amásia** (ortoversão)"
**Problema:** o trabalho de Davies, Green & Duarte — citado pela própria aula, e a fonte da correção do achado 🔴 1 — testa **quatro** cenários, não três. Falta **Aurica**, em que o Atlântico e o Pacífico se fecham **simultaneamente** e um oceano novo se abre rasgando a Ásia. A omissão não é a de um item de lista qualquer: Aurica é justamente o contraexemplo que quebra a afirmação de que "cada cenário corresponde a um modo de fechamento diferente", porque combina introversão e extroversão. Como escrita, a frase ensina uma taxonomia mais limpa do que a literatura sustenta — e o aluno que encontrar Aurica numa fonte primária vai concluir que a aula está incompleta ou errada. Agrava-se no flashcard `fb020`, cuja pergunta ("Quais cenários de modelagem são propostos...") tem forma **exaustiva** e era respondida com três de quatro, citando como fonte exatamente o artigo que define os quatro.
**Correção proposta:** incluir Aurica como quarto cenário e declarar que os modos de fechamento não são mutuamente exclusivos.
**Fonte:** Davies, H.S., Green, J.A.M. e Duarte, J.C. (2020), *Back to the future II: tidal evolution of four supercontinent scenarios*, Earth System Dynamics 11, 291 — https://esd.copernicus.org/articles/11/291/2020/ (consulta em 2026-08-18) · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** flashcard `fb020`; índice do baralho (`flashcards.md`, coluna "Núcleo recuperado" de OA05); manifesto `alegacoes_auditaveis` da aula 06 (`GEO-M18-A06-FUTURO-004`).

### 🟠 14. A seção "Cobertura" do questionário descreve 13 questões num instrumento de 14

**claim_id:** `TEC-QUIZ-COBERTURA-032`
**Tipo:** inconsistência interna
**Onde:** questionário final · "Cobertura"
**Está escrito:** "Distribuição cognitiva: lembrar 5; explicar 3; aplicar 4; analisar 1." e "Tipos: 5 múltipla escolha, 3 dissertativas curtas, 4 aplicações e 1 análise."
**Problema:** contagem direta dos itens: as questões de lembrar (e de múltipla escolha, que são as mesmas) são **Q01, Q03, Q05, Q07, Q10 e Q12 — seis, não cinco**. As duas linhas somam **13** e descrevem um questionário com uma questão a menos que o real. O cabeçalho ("14 questões · 46 pts"), a matriz por objetivo e os pesos declarados foram conferidos item a item e **estão corretos** — o erro está contido na seção "Cobertura". Não é erro científico: é o instrumento contradizendo a si mesmo, e o efeito prático é o aluno se autoavaliar contra um denominador errado. É o mesmo tipo de defeito de contabilidade interna encontrado no módulo 17 (`EST-M17-QUIZ-COVERAGE-029`), aqui em grau muito menor, porque nenhuma questão citada é inexistente.
**Correção proposta:** "lembrar 6" e "6 múltipla escolha".
**Fonte:** o próprio material — contagem direta dos itens e dos pesos, conferida contra o gabarito comentado · **Nível:** verificação interna
**Confiança:** confirmado
**Também aparece em:** em nenhum outro arquivo. O hub do módulo declara "14 questões e 46 pontos", que está correto.

### 🟠 15. A entrada de vocabulário funde antearco e retroarco e glosa em inglês só um dos dois

**claim_id:** `TEC-BACIA-FOREARC-TERMO-033`
**Tipo:** imprecisão nomenclatural
**Onde:** aula 03 · "Vocabulário desta aula"
**Está escrito:** "| **Bacia de antearco / retroarco (backarc)** | Bacias associadas a zonas de subducção: a de antearco fica entre a fossa e o arco vulcânico; a de retroarco, atrás do arco... |"
**Problema:** o glossário existe para permitir ao aluno buscar o termo original na literatura, que é majoritariamente em inglês. Ao juntar dois conceitos distintos numa única linha e oferecer um único termo inglês, a entrada deixa **antearco sem equivalente**: o aluno não tem como saber que o termo consagrado é **forearc** (*forearc basin*), e a leitura mais natural da barra é que "backarc" cobriria os dois. É a mesma classe de defeito do achado 🟠 4 (`TEC-FORCAS-SLABPULL-004`), em grau menor — lá o termo inglês estava **errado**, aqui está **ausente**.
**Correção proposta:** separar em duas entradas — "Bacia de antearco (forearc)" e "Bacia de retroarco (back-arc)".
**Fonte:** terminologia corrente em literatura de zonas de subducção — Balázs et al. (2022), *The Dynamics of Forearc–Back-Arc Basin Subsidence*, Tectonics — https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2021TC007078 (consulta em 2026-08-18) · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** o card `fb008` pergunta a posição da bacia de antearco sem usar termo inglês — permanece válido. Nenhuma questão do questionário usa o termo em inglês.

## Verificado e correto

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `TEC-CINEM-EULER-013` | O movimento relativo entre duas placas é uma rotação em torno de um polo de Euler; a velocidade linear varia com o seno da distância angular ao polo, sendo máxima a 90°. | USGS, *This Dynamic Earth* (2026) | confirmado |
| `TEC-CINEM-ISL-014` | A Dorsal Meso-Atlântica abre mais devagar perto da Islândia que em segmentos mais distantes do polo América do Norte–Eurásia. | USGS; Cochran et al. 2003, JGR (Ártico: ~18 → ~12,7 mm/ano para norte) | confirmado |
| `TEC-CINEM-METODOS-015` | Anomalias magnéticas do assoalho oceânico dão taxas de longo prazo; GPS/GNSS dá taxas de curto prazo, e a divergência sistemática entre elas sinaliza falha travada ou limite difuso. | USGS; EarthScope/UNAVCO | confirmado |
| `TEC-FORCAS-DOMIN-016` | Puxão de placa domina em placas com grande extensão de subducção no perímetro; empurrão de cume é real mas tipicamente bem menor; não há motor único. | Forsyth & Uyeda 1975; Conrad & Lithgow-Bertelloni 2002 (slab pull ≈ metade da força motriz total) | confirmado |
| `TEC-FORCAS-AFR-017` | A Placa Africana, cercada em boa parte por limites divergentes, depende proporcionalmente mais de empurrão de cume e do acoplamento com o manto. | Forsyth & Uyeda 1975; síntese de geodinâmica de placas | provável |
| `TEC-MANTO-SOLIDO-018` | O manto é majoritariamente sólido e flui em escalas de milhões de anos; convecção não é um oceano de rocha derretida. | USGS, *This Dynamic Earth* | confirmado |
| `TEC-MANTO-SLABMOTOR-019` | As placas em subducção são parte ativa do motor da convecção, e não passageiras de um fluxo independente. | Conrad & Lithgow-Bertelloni 2002 | confirmado |
| `TEC-MANTO-DORSAL-020` | A ascensão de manto sob dorsais é em grande parte passiva, com fusão por descompressão. | Literatura de fusão sob dorsais (modelos de upwelling passivo); USGS | confirmado |
| `TEC-MANTO-ARCO-021` | Água liberada da placa em subducção reduz o solidus da cunha mantélica e gera magmatismo de arco. | USGS; petrologia de zonas de subducção | confirmado |
| `TEC-BACIA-ACOM-022` | Bacia sedimentar define-se por espaço de acomodação (subsidência), não pelo sedimento que a preenche. | Allen & Allen, *Basin Analysis* | confirmado |
| `TEC-BACIA-TERM-023` | A subsidência térmica pós-rifte é lenta e decai exponencialmente, sustentando margens passivas espessas sem tectônica ativa. | Allen & Allen, *Basin Analysis* (modelo de McKenzie) | confirmado |
| `TEC-BACIA-FLEX-024` | Bacias de antepaís resultam de flexão da litosfera sob a carga da cadeia orogênica e recebem sedimento erodido dela. | Allen & Allen; Geological Society of London | confirmado |
| `TEC-OROG-WILSON-025` | O ciclo de Wilson (rifte → oceano → subducção → fechamento → colisão) é modelo idealizado, com estágios que se sobrepõem em casos reais. | Geological Society of London, síntese sobre o ciclo de Wilson | confirmado |
| `TEC-OROG-DENS-026` | A crosta continental é em média menos densa que a crosta oceânica e o manto, e por isso resiste à subducção; a colisão pode dobrar a espessura crustal. | USGS; petrologia/geofísica de referência (crosta tibetana 70–80 km) | confirmado |
| `TEC-OROG-TERRENOS-027` | A Cordilheira Norte-Americana é interpretada, em parte substancial, como produto de acresção sucessiva de terrenos tectonoestratigráficos. | Coney, Jones & Monger 1980, Nature 288 | confirmado |
| `TEC-OROG-HIMALAIA-028` | O Himalaia resulta da colisão Índia–Eurásia em curso, com soerguimento na ordem de milímetros por ano medido por geodesia. | USGS, síntese sobre a colisão Índia–Eurásia | confirmado |
| `TEC-CRATON-QUILHA-029` | Crátons arqueanos repousam sobre quilhas litosféricas de 200 km ou mais, de manto residual empobrecido, mais rígido e menos denso que o manto ao redor. | Pearson et al., síntese sobre cratonic mantle roots (quilhas de >150 km, até ~350 km) | confirmado |
| `TEC-SUPERC-IDADES-030` | Columbia/Nuna ~1.800–1.300 Ma, Rodínia ~1.100–750 Ma e Pangeia ~335–175 Ma, nessa ordem cronológica. | Evans & Mitchell, *What's in a name? The Columbia (Paleopangaea/Nuna) supercontinent*; Li et al. 2008, Precambrian Research | confirmado |

## Fontes normativas e primárias consultadas

- ICS, *International Chronostratigraphic Chart*, versão vigente em 2026 — https://stratigraphy.org/chart
- USGS, *This Dynamic Earth: the story of plate tectonics*, consulta em 2026-08-18 — https://pubs.usgs.gov/gip/dynamic/
- Forsyth, D. e Uyeda, S. (1975), Geophysical Journal of the Royal Astronomical Society 43, 163–200
- Conrad, C.P. e Lithgow-Bertelloni, C. (2002), Science 298, 207–209
- Tarduno, J.A. et al. (2003), Science 301, 1064–1069
- Torsvik, T.H. et al. (2017), Nature Communications 8, 15660
- Coney, P.J., Jones, D.L. e Monger, J.W.H. (1980), Nature 288, 329–333
- Li, Z.X. et al. (2008), Precambrian Research 160
- Nance, R.D., Murphy, J.B. e Santosh, M. (2014), Gondwana Research 25
- Murphy, J.B. et al. (2021), Geological Society, London, Special Publications 503; Nance & Murphy (2022), Earth-Science Reviews
- Mitchell, R.N., Kilian, T.M. e Evans, D.A.D. (2012), Nature 482, 208–211
- Davies, H.S., Green, J.A.M. e Duarte, J.C. (2018/2020), Global and Planetary Change; Earth System Dynamics 11, 291
- Milani, E.J. et al. (2007), Boletim de Geociências da Petrobras 15(2); SGB/CPRM, materiais sobre a Plataforma Sul-Americana
- Allen, P.A. e Allen, J.R., *Basin Analysis: Principles and Application to Petroleum Play Assessment*

## Observações não factuais

- A seção "Por que os continentes voltam a se reunir?" continua intitulada "Duas famílias de hipótese" enquanto o vocabulário agora traz três termos (introversão, extroversão, ortoversão). A contagem segue correta — são duas *famílias* de mecanismo, e os três modos se distribuem entre elas —, mas a escolha de título é ponto para a revisão didática, não achado factual.
- A aula 05 usa a expressão "dinâmica subsidência de origem mantélica", com ordem de palavras invertida. É correção de redação, não de fato; fica para o `revisor-didatico`.

---

## Correções aplicadas

**Aplicadas em:** 2026-08-18

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `TEC-SUPERC-ULTIMA-001` | 🔴 | Corrigido | aula 06 (vocabulário, "E o próximo supercontinente?", Erros comuns, Recap, manifesto); `flashcards-basic.csv` (`fb020`); `flashcards.md` |
| `TEC-SUPERC-PANNOTIA-002` | ⚪ | Corrigido com ressalva — disputa explicitada, nenhum lado escolhido | aula 06 (seção dos supercontinentes, Exemplo trabalhado, Erros comuns, Recap, manifesto); `questionario-final.md` (gabarito e rubrica da Q14) |
| `TEC-PLUMA-HAVAI-003` | 🟠 | Corrigido | aula 02 (Exemplo trabalhado, Erros comuns, Fontes, manifesto); `questionario-final.md` (gabarito e rubrica da Q04); `flashcards-cloze.csv` (`fc003`) |
| `TEC-FORCAS-SLABPULL-004` | 🟠 | Corrigido | aula 01 (vocabulário) |
| `TEC-VEL-UNHA-005` | 🟠 | Corrigido | aula 01 ("Como se mede o movimento") |
| `TEC-BACIA-ROLLBACK-006` | 🟠 | Corrigido | aula 03 ("Subducção: duas bacias, dois lados da fossa") |
| `TEC-CRATON-PARANA-007` | 🟠 | Corrigido | aula 05 ("Dois compartimentos dentro de um mesmo cráton"; Fontes) |
| `TEC-SUPERC-MANTO-008` | 🟠 | Corrigido | aula 06 ("Duas famílias de hipótese", item 2; Recap) |
| `TEC-OROG-SUTURA-009` | 🟠 | Corrigido | aula 04 (Exemplo trabalhado, passo 2) |
| `TEC-SUPERC-RODINIA-ERA-010` | 🟠 | Corrigido | aula 06 (item Rodínia) |
| `TEC-CINEM-MAR-ESCOPO-011` | 🟠 | Corrigido | aula 01 (Exemplo trabalhado, passo 3) |
| `TEC-FONTE-USGS-URL-012` | 🔵 | Corrigido por substituição da URL pela canônica do mesmo documento | aula 01 (Fontes) |
| `TEC-SUPERC-AURICA-031` | 🟠 | Corrigido (reverificação) | aula 06 ("E o próximo supercontinente?", Erros comuns, Recap, manifesto); `flashcards-basic.csv` (`fb020`); `flashcards.md` |
| `TEC-QUIZ-COBERTURA-032` | 🟠 | Corrigido (reverificação) | `questionario-final.md` (seção "Cobertura") |
| `TEC-BACIA-FOREARC-TERMO-033` | 🟠 | Corrigido (reverificação) | aula 03 (Vocabulário) |

**Pendências:** nenhuma. Zero achados 🔴 ou 🟠 em aberto — **gate científico liberado** para o módulo 18.

**Ressalva de propagação (Anki):** os cards `fb020` (Basic) e `fc003` (Cloze) mudaram de conteúdo. Se o baralho do módulo 18 já foi importado, reimportar o CSV **não** sobrescreve necessariamente cards já existentes — localize os dois pelo `id` e corrija ou remova à mão. Registrado também no cabeçalho de `18-tectonica-global-geodinamica-flashcards.md`.

**Estado do curso:** o bloco `audit` do módulo 18 **não** foi gravado em `course-state.yaml`, por coordenação externa com as sessões que processam os módulos 17 e 20 em paralelo. O registro da auditoria foi feito apenas no hub do módulo (`18-tectonica-global-geodinamica-modulo.md`). A consolidação do estado, e a execução de `scripts/validate_state.py`, ficam para o passo de consolidação.

## Reverificação de 2026-08-18

Segunda passada independente sobre o módulo já corrigido, para confirmar que as correções da primeira passada foram de fato aplicadas e se sustentam:

- **Os 12 achados originais foram reconferidos no texto dos arquivos** — todos presentes e aplicados, nas aulas 01 a 06 e nos derivados. A execução foi **idempotente**: nenhuma reedição da primeira passada foi necessária.
- **Quatro correções foram reconferidas contra fonte**, e todas se sustentam: a atribuição Pangeia Ultima = introversão / Novopangeia = extroversão / Amásia = ortoversão (Davies, Green & Duarte); a deriva do ponto quente havaiano a taxas **acima de 40 mm/ano entre ~81 e ~47 Ma**, com paleolatitudes de 32 ± 8,8 °N em Detroit a 21 ± 5,5 °N em Kōko, o que sustenta os 11°–15° declarados (Tarduno et al. 2003); o limite Meso/Neoproterozoico em **1000 Ma** (Esteniano 1200–1000; Toniano 1000–720), que confirma a inversão corrigida no achado 🟠 10; e a janela de Pangeia **~335–175 Ma**.
- **A contabilidade do questionário foi conferida item a item** — cabeçalho, matriz por objetivo e pesos batem com o conteúdo real (14 questões, 46 pontos, e as somas por OA de 13/6/9/6/12). O único desvio estava na seção "Cobertura" (achado 🟠 14).
- **Os 35 cards** dos três arquivos de flashcards batem entre si e com as aulas corrigidas.
- **Três achados novos** foram encontrados, fora do alcance da primeira passada: dois deles (🟠 14 e 🟠 15) porque a primeira passada olhou o conteúdo científico e não a contabilidade interna do instrumento de avaliação nem a completude das glosas do vocabulário; e um (🟠 13) porque exigia voltar à fonte primária já citada e verificar não o que ela **afirma**, mas quantos casos ela **enumera** — o tipo de omissão que só aparece relendo a fonte, não o texto.
