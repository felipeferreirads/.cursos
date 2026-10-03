# Auditoria científica — Módulo 18: Geofísica da América do Sul

**Data do levantamento:** 2026-09-11 · **Correções aplicadas em:** 2026-09-11
**Modo:** `audit-and-fix` (levantamento em passagem audit-only, correções aplicadas cirurgicamente numa segunda passagem)

> [!warning] Leia antes: a numeração das aulas mudou depois desta auditoria
> Este relatório é um registro datado de **2026-09-11**, quando o módulo tinha **quatro** aulas. Em **2026-09-12** a Aula 03 foi **dividida em duas** e a antiga Aula 04 foi renumerada. Os `claim_id` e os IDs de achado deste relatório **não foram renomeados** — eles são identificadores estáveis e continuam válidos —, mas as referências a "Aula 03" e "Aula 04" no texto abaixo devem ser lidas com esta correspondência:
> - achados `AUD-M18-A03-*` de **gravimetria, geoide, maré terrestre e magnetometria** (`-BOUGUERCRATON-010`, `-GOTZEKRAUSE-012`, `-WARDMT-013`, `-PINTOHALLINAN-014`, `-HEIRTZLER-015`) → hoje na **Aula 03**, `...aula-03-campos-potenciais-gravimetria-geoide-mare-terrestre-magnetometria.md`;
> - achados `AUD-M18-A03-*` de **paleomagnetismo** (`-TPW-001`) → hoje na **Aula 04**, `...aula-04-paleomagnetismo-deriva-placa-sul-americana.md`;
> - achados `AUD-M18-A04-*` (sismicidade, campo de esforços, Nazca) → hoje na **Aula 05**, `...aula-05-sismicidade-campo-de-esforcos-placa-de-nazca.md`.
>
> **Todas as 17 correções desta auditoria foram verificadas uma a uma após a divisão e sobreviveram literalmente**, incluindo a vermelha `AUD-M18-A03-TPW-001` e as quatro de atribuição de fonte. O registro da divisão está em `course-state.yaml`, bloco `decisions` de 2026-09-12.
**Escopo:** as 4 aulas do módulo, auditadas em conjunto, mais o hub do módulo
**Veredito:** **aprovado — gate liberado.** 0 achados vermelhos e 0 laranjas em aberto; os 17 achados corrigíveis foram corrigidos e o achado branco recebeu o tratamento de controvérsia. **Questionário e flashcards liberados**, observadas as restrições de formato ao fim deste relatório.

## Contagem por severidade

| Severidade | Contagem | Situação |
|---|---|---|
| 🔴 Vermelho (afirmação factualmente falsa) | **3** | **corrigidos** |
| 🟠 Laranja (impreciso, confusão de escopo, certeza indevida, inconsistência interna) | **8** | **corrigidos** |
| 🟡 Amarelo (atribuição de fonte errada, citação defeituosa, valor fora do que a fonte citada sustenta) | **6** | **corrigidos** |
| 🔵 Azul (verificado e correto — registro de que foi checado) | **18** | sem alteração (não exigem correção: são registros de verificação bem-sucedida) |
| ⚪ Branco (questão genuinamente aberta na literatura apresentada como resolvida) | **1** | **tratado** — mantido, agora apresentado como controvérsia real |

> **Nota sobre as contagens:** os números da coluna "Contagem" são os do levantamento original e não mudam — um achado não se apaga ao ser corrigido, ele muda de situação. O relatório preserva cada achado com o texto original do problema e, logo abaixo, o registro do que foi feito.

**Alegações rastreadas:** as 23 `alegacoes_auditaveis` declaradas pelas aulas (6 na a01, 6 na a02, 6 na a03, 5 na a04) foram verificadas uma a uma; a auditoria levantou mais 9 fora da lista do autor, chegando a **32 alegações rastreadas**.

**Exemplos trabalhados:** os quatro foram refeitos. Não há aritmética a recalcular neste módulo (nenhum dos quatro pede conta); os quatro são exercícios de consistência e classificação. Três fecham. **O da a04 não fecha** — sua resolução inverte o sentido de mergulho da laje subductada (achado 🔴 3).

---

## Padrão dominante

**DIREÇÃO E POSIÇÃO GEOGRÁFICA — o fato certo apontado para o lado errado.** Quatro dos onze achados 🔴/🟠 têm exatamente esta forma: a unidade existe, o mecanismo existe, e a aula a coloca no quadrante errado do mapa.

1. A **Faixa Paraguai-Araguaia** posta na "borda **sudoeste**" do Cráton Amazônico. O Araguaia corre pela borda **leste**, o Paraguai pela borda **sul-sudeste**; quem ocupa a borda sudoeste é o cinturão Tucavaca (achado 🔴 2).
2. O **Cráton Rio de La Plata** posto "no Uruguai e **norte** da Argentina". Ele está no Uruguai e na Argentina **centro-oriental** — Tandilia, sudeste da província de Buenos Aires, 36°30'-38°10'S — estendendo-se ~1.000 km até as proximidades de Córdoba (achado 🟠 2).
3. As **províncias geocronológicas do Cráton Amazônico** descritas como envelhecendo "do **centro** para as **bordas**", num padrão radial. O gradiente real é unidirecional **NE → SW** (achado 🟠 3).
4. No exemplo trabalhado da a04, a laje de Nazca "aprofundando **para oeste**". Ela aprofunda para **leste**, continente adentro, afastando-se da fossa — que está a oeste (achado 🔴 3).

Por que isso é caro **neste** módulo: a aula 01 é declaradamente o **mapa-base** sobre o qual as três aulas seguintes sobrepõem dados. Um erro de posição na a01 não é um fato isolado — é a moldura que o aluno vai usar para localizar toda anomalia gravimétrica, todo perfil magnetotelúrico e todo hipocentro das aulas 02 a 04. E a a04, que fecha o módulo, é onde o sentido de mergulho da laje **é** o conteúdo: é a partir dele que se distingue subducção normal de subducção plana, que é o fio condutor declarado do módulo inteiro.

**Padrão secundário: ATRIBUIÇÃO DE FONTE.** Quatro dos seis amarelos são o mesmo defeito que dominou o Módulo 17 — o dado certo debaixo do nome errado, ou uma entrada de bibliografia colada. Aqui ele reincide com uma inversão especialmente visível: **Götze & Krause (2002)**, cujo título é *"The Central Andean gravity **high**"*, é creditado como fonte da anomalia de Bouguer **negativa** andina (🟡 1). Ver a nota transversal ao fim.

**Onde o módulo está limpo:** toda a física do método magnetotelúrico e o caso do corpo magmático do Altiplano-Puna na a02; a distinção Moho × base da litosfera; as quilhas cratônicas e suas faixas de profundidade; o fluxo de calor por província tectônica; o geoide como ferramenta de comprimento de onda longo e sua separação da Bouguer; a maré terrestre e suas ordens de grandeza; a distinção entre anomalia magnética **crustal** e a Anomalia Magnética do Atlântico Sul (campo principal/núcleo) — que é o melhor parágrafo do módulo; toda a mecânica do paleomagnetismo (inclinação → paleolatitude, declinação → rotação, a não determinação da paleolongitude); a zona de Wadati-Benioff e suas três faixas de profundidade; e o enxame de João Câmara.

---

## Achados vermelhos (todos corrigidos)

### 🔴 AUD-M18-A03-TPW-001 — A aula nega a deriva polar verdadeira e chama a negação de "resultado bem estabelecido"
**Aula 03, seção "Paleomagnetismo: como uma rocha registra onde estava"; propagado para a alegação `GEOFISSA-M18-A03-PALEOMAG-005`.**
**Tipo:** erro factual + certeza indevida.

**Está escrito:** *"não é o polo que efetivamente 'andou' (**o eixo de rotação da Terra é estável em relação ao manto em escalas geológicas, um resultado bem estabelecido**), mas sim a placa que se moveu"*.

**Problema:** a afirmação entre parênteses é falsa, e é falsa exatamente ao contrário do que a literatura estabelece. A reorientação do conjunto manto+litosfera em relação ao eixo de rotação tem nome próprio, literatura própria e medidas próprias: é a **deriva polar verdadeira** (*true polar wander*, TPW). A estabilização pelo bojo rotacional **desaparece** em escala geológica, e a orientação de equilíbrio do planeta passa a ser ditada pela distribuição de massa — ou seja, o eixo de rotação **não** é estável em relação ao manto ao longo de tempo geológico. Há TPW documentada e quantificada ao menos desde 320 Ma, com taxas que variam sistematicamente com o ciclo de supercontinentes.

O dano específico: uma APWP global **contém** uma componente de TPW somada ao movimento de placa, e separar as duas é um problema de pesquisa corrente. A aula não só omite isso — ela ensina que a componente não existe, e carimba a negação como consenso. Um aluno que encontrar o termo "true polar wander" depois vai concluir que a aula estava desatualizada ou que o termo é marginal; nenhuma das duas coisas é verdade.

**Por que vermelho e não branco:** não é uma controvérsia em que a aula escolheu um lado. É a negação da existência de um fenômeno estabelecido, apresentada como resultado firmado.

**Correção proposta:** substituir o parêntese por: *"— e a rigor a trajetória soma duas coisas: o movimento da própria placa, que é dominante, e uma componente menor de **deriva polar verdadeira** (true polar wander), a reorientação do conjunto manto-litosfera em relação ao eixo de rotação, que existe, é documentada ao menos desde o Paleozoico e cuja separação do sinal de placa é problema de pesquisa corrente"*. Atualizar a alegação `...PALEOMAG-005` no mesmo sentido e ajustar o recap, que repete a formulação ("que documenta o movimento histórico da placa (não do polo)").

**Fonte:** Vaes et al. (2025), *"Slow True Polar Wander Around Varying Equatorial Axes Since 320 Ma"*, **AGU Advances**, 10.1029/2024AV001515; Evans, D. A. D., *"True polar wander and supercontinents"* (revisão); literatura de convecção mantélica e reajuste do bojo rotacional (*Earth and Planetary Science Letters*, 2011), que afirma explicitamente que a estabilização rotacional desaparece em escalas geológicas. **Nível:** revisada por pares. **Confiança:** confirmado.
**Também aparece em:** recap relâmpago da a03, bullet de paleomagnetismo.

**Correção aplicada:** o parêntese que negava a deriva polar verdadeira foi substituído por um trecho que mantém o movimento de placa como termo dominante da APWP, nomeia a **deriva polar verdadeira** (*true polar wander*) como componente menor e real, explica que a estabilização pelo bojo rotacional desaparece em escala geológica, e registra que separar TPW do sinal de placa é problema de pesquisa corrente. Propagado para o recap (bullet de paleomagnetismo) e para a alegação `GEOFISSA-M18-A03-PALEOMAG-005`. Vaes et al. (2025), *AGU Advances*, e Evans, *True polar wander and supercontinents*, acrescentados às Fontes da a03.


### 🔴 AUD-M18-A01-PARAGUAIARAGUAIA-002 — A Faixa Paraguai-Araguaia posta no lado errado do Cráton Amazônico
**Aula 01, seção "Faixas móveis: onde os crátons se soldaram"; propagado para o recap e para a alegação `GEOFISSA-M18-A01-BRASILIANO-002`.**
**Tipo:** erro factual (posição geográfica).

**Está escrito:** *"e a **Faixa Paraguai-Araguaia**, na **borda sudoeste** do Cráton Amazônico"*.

**Problema:** a configuração da plataforma sul-americana, definida na amalgamação do Gondwana, tem o Cráton Amazônico bordejado por cinturões neoproterozoicos **a leste (Araguaia)**, **ao sul (Paraguai)** e **a sudoeste (Tucavaca)**. O Cinturão Araguaia é um cinturão N-S ao longo da margem **oriental** do cráton; o Cinturão Paraguai é uma faixa arqueada de cavalgamento com vergência para NW ao longo da margem **sul-sudeste**, sobre a margem SE do Cráton Amazônico e do Bloco Rio Apa. "Sudoeste" não é uma imprecisão de quadrante: é o lado oposto do cráton para o Araguaia, e o lugar de outra faixa (Tucavaca) que a aula não menciona.

**Correção proposta:** *"e a **Faixa Araguaia**, ao longo da borda **leste** do Cráton Amazônico, e a **Faixa Paraguai**, na borda **sul-sudeste** (sobre a margem SE do cráton e o Bloco Rio Apa)"*. Se a intenção era manter o par como uma unidade, *"o sistema Paraguai-Araguaia, que contorna as bordas leste e sul do Cráton Amazônico"* preserva a economia sem inverter o lado.

**Fonte:** Alkmim & Marshak / Pimentel, *"Paraguay and Araguaia Belts"* (capítulo de síntese); Bologna et al. (2014), *"Paraguay-Araguaia Belt Conductivity Anomaly: A fundamental tectonic boundary in South American Platform imaged by electromagnetic induction surveys"*, **Geochemistry, Geophysics, Geosystems**, 10.1002/2013GC004970; *An Overview of the Amazonian Craton Evolution* (2015), *International Journal of Geosciences*, que enuncia a configuração leste/sul/sudoeste. **Nível:** revisada por pares. **Confiança:** confirmado.
**Também aparece em:** recap relâmpago da a01 (lista de faixas brasilianas) e hub do módulo (linha da Aula 01, que não nomeia a posição — não precisa correção).

**Observação de oportunidade:** Bologna et al. (2014) é um trabalho **magnetotelúrico** sobre exatamente esta sutura. É a fonte natural para amarrar a a01 à a02 do próprio módulo, e hoje não está citada em nenhuma das duas.

**Correção aplicada:** o par colapsado foi desdobrado em **Faixa Araguaia**, ao longo da borda **leste** do Cráton Amazônico, e **Faixa Paraguai**, na borda **sul-sudeste** (sobre a margem SE do cráton e o Bloco Rio Apa). Propagado para o recap (lista de faixas brasilianas) e para a alegação `GEOFISSA-M18-A01-BRASILIANO-002`, que agora registra também que a borda sudoeste é ocupada pelo cinturão Tucavaca. **Bologna et al. (2014)** foi acrescentado às Fontes da a01, atendendo à oportunidade apontada: é um trabalho magnetotelúrico sobre esta mesma sutura, e amarra a a01 à a02 do próprio módulo.


### 🔴 AUD-M18-A04-MERGULHOOESTE-003 — O exemplo trabalhado inverte o sentido de aprofundamento da laje de Nazca
**Aula 04, Exemplo trabalhado, resolução do item (1).**
**Tipo:** erro factual (inversão de sentido) + inconsistência interna.

**Está escrito:** *"numa subducção plana, a placa não aprofunda rapidamente logo após a fossa como faria numa subducção normal, então a concentração de sismicidade rasa próxima à costa, seguida por uma extensão anômala **para leste** em vez de um **aprofundamento rápido para oeste**, é exatamente o padrão geométrico esperado."*

**Problema:** na margem andina a Fossa Peru-Chile está a **oeste** (~71-72°O na latitude do exemplo) e a placa de Nazca mergulha **para leste**, continente adentro. Numa subducção normal a laje aprofunda indo **para leste** a partir da fossa; não existe "aprofundamento para oeste" em lugar nenhum desta margem. A frase constrói uma oposição falsa — "estender-se para leste **em vez de** aprofundar para oeste" — quando os dois regimes se distinguem por **quão rápido** a laje aprofunda indo para leste, não por direções opostas.

O agravante é que a própria aula ensina o contrário duas seções acima, corretamente: *"uma superfície inclinada que mergulha **da fossa oceânica para o interior do continente**"*. A aula se contradiz dentro de si mesma, e a versão errada está no exemplo trabalhado — que é a parte que o aluno usa como modelo de raciocínio e a parte de onde o questionário costuma sair.

**Por que vermelho:** inversão de sentido em exemplo trabalhado. É a categoria de defeito que já custou achados vermelhos aos Módulos 10 e 17 deste curso, e a única do módulo capaz de produzir um gabarito invertido se propagada para a avaliação.

**Correção proposta:** *"...então a concentração de sismicidade rasa próxima à fossa e à costa, seguida por uma extensão anômala da sismicidade para **leste**, continente adentro, em vez do **aprofundamento rápido — também para leste — que uma laje de ~30° produziria logo depois da fossa**, é exatamente o padrão geométrico esperado."*

**Verificação adicional no mesmo exemplo:** a situação diz *"poucos hipocentros de profundidade intermediária a oeste de 68°O"*. Isso é geometricamente **ambíguo**, não errado: num flat slab a laje atinge ~100 km por volta de 69-68°O e segue horizontal até ~66°O, de modo que sismicidade intermediária existe sim a oeste de 68°O, e o que a distingue é ela **continuar** para leste. Recomenda-se reformular o item (1) para *"hipocentros de profundidade intermediária que, em vez de cessarem a leste de 68°O, prosseguem"* — caso contrário o dado que o item (1) oferece não sustenta a conclusão que a resolução tira dele.

**Fonte:** Cahill & Isacks (1992), *"Seismicity and shape of the subducted Nazca Plate"*, **JGR** 97(B12), 17503-17529 — já citada pela própria aula; Ramos & Folguera (2009), **GSL Special Publications** 327(1), 31-54. **Nível:** revisada por pares. **Confiança:** confirmado.

---

## Achados laranjas (todos corrigidos)

**Correção aplicada, nas duas metades do exemplo trabalhado.** (a) **Resolução do item (1):** a oposição falsa "extensão para leste **em vez de** aprofundamento rápido para oeste" foi substituída pela oposição correta — extensão anômala para leste em vez do aprofundamento rápido, **também para leste**, que uma laje de ~30° produziria logo depois da fossa —, com uma frase explícita fixando que a fossa está a oeste (~71-72°O nesta latitude), que a laje mergulha para leste nos **dois** regimes, e que o discriminante é a **taxa** de aprofundamento, não a direção. (b) **Situação, item (1):** reformulado conforme a verificação adicional, de "poucos hipocentros de profundidade intermediária a oeste de 68°O" (geometricamente ambíguo) para "sismicidade de profundidade intermediária que, em vez de cessar por volta de 68°O, prossegue continente adentro" — de modo que o dado que o item (1) oferece agora sustenta a conclusão que a resolução tira dele. Propagado para a alegação `GEOFISSA-M18-A04-FLATSLABSISMICO-003`. A contradição interna com a seção da zona de Wadati-Benioff, que já ensinava o sentido certo, está desfeita.


### 🟠 AUD-M18-A01-ARACUAI-004 — "Cráton São Francisco-Congo" apresentado como a contraparte africana do Cráton São Francisco
**Aula 01, seção "Faixas móveis".**
**Tipo:** erro de nomenclatura + confusão de escopo.

**Está escrito:** *"a **Faixa Araçuaí** e a **Faixa Ribeira**, no sudeste, que fecham o Cráton São Francisco contra o **Cráton São Francisco-Congo (sua contraparte africana)** e contra o Cráton Rio de La Plata, respectivamente"*.

**Problema:** duas coisas. (a) **Nomenclatura:** "São Francisco-Congo" é o nome do **paleocontinente composto** — o bloco em forma de U invertido que reúne as duas metades. A contraparte africana do Cráton São Francisco é o **Cráton do Congo**, e o orógeno é o **Araçuaí-Congo Ocidental** (*Araçuaí-West Congo*). Dizer que o São Francisco fechou "contra o São Francisco-Congo" é dizer que um bloco colidiu com o conjunto do qual ele próprio é metade. (b) **Escopo/mecanismo:** o Araçuaí é o exemplo canônico de **orógeno confinado**, formado pela inversão de um **golfo** do paleocontinente São Francisco-Congo, cercado em três lados por crosta cratônica — não pelo fechamento de um oceano entre dois crátons que estavam separados. O verbo "fechar ... contra" ensina o modelo errado justamente no caso que a literatura usa como contraexemplo do modelo padrão.

**Correção proposta:** *"a **Faixa Araçuaí**, no sudeste, que junto com seu prolongamento africano (a faixa do Congo Ocidental) forma o **orógeno Araçuaí-Congo Ocidental** — um orógeno dito **confinado**, formado pela inversão de um golfo do paleocontinente São Francisco-Congo em vez do fechamento de um oceano amplo; e a **Faixa Ribeira**, a sudoeste dela"*.

**Fonte:** Pedrosa-Soares et al. (2001), *"The Araçuaí-West-Congo Orogen in Brazil: an overview of a confined orogen formed during Gondwanaland assembly"*, **Precambrian Research**; Alkmim et al., *"Kinematic evolution of the Araçuaí-West Congo orogen ... Nutcracker tectonics"*, **Precambrian Research** (2006); *"Basement inliers of the Araçuaí-West Congo orogen: key pieces for understanding the evolution of the São Francisco-Congo paleocontinent"*, **JSAES** (2023). **Nível:** revisada por pares. **Confiança:** confirmado.

**Correção aplicada:** o Araçuaí deixou de "fechar o Cráton São Francisco contra o Cráton São Francisco-Congo" e passa a ser apresentado como a metade brasileira do **orógeno Araçuaí-Congo Ocidental**, com o prolongamento africano nomeado corretamente (faixa do Congo Ocidental) e o mecanismo corrigido: **orógeno confinado**, formado pela inversão de um golfo do paleocontinente São Francisco-Congo, e não pelo fechamento de um oceano amplo entre dois crátons separados. Propagado para o recap e para a alegação `GEOFISSA-M18-A01-BRASILIANO-002`; Pedrosa-Soares et al. (2001) acrescentado às Fontes.


### 🟠 AUD-M18-A01-RIOPLATA-005 — O Cráton Rio de La Plata deslocado para o norte da Argentina
**Aula 01, lista de crátons.**
**Tipo:** impreciso (posição geográfica).

**Está escrito:** *"**Cráton Rio de La Plata (ou Rio da Prata):** no Uruguai e **norte da Argentina**, com extensão para o sul do Brasil"*.

**Problema:** os afloramentos cratônicos do Rio de La Plata na Argentina estão no **Sistema de Tandilia** ("Sierras Septentrionales de Buenos Aires"), sudeste da província de Buenos Aires, entre 36°30'-38°10'S e 57°30'-61°O — isto é, no **centro-leste/sudeste** do país, a mais de 1.500 km do norte argentino. O cráton se estende cerca de 1.000 km desde Tandilia até as proximidades dos afloramentos do cinturão Pampeano, perto de Córdoba. O norte da Argentina é domínio andino e de antepaís, não cratônico.

**Correção proposta:** *"no Uruguai e na Argentina centro-oriental (aflorando no Sistema de Tandilia, sudeste da província de Buenos Aires, e estendendo-se em subsuperfície até as proximidades de Córdoba), com extensão para o sul do Brasil"*.

**Fonte:** Rapela et al., *"The Río de la Plata Craton of Argentina and Uruguay"*, em *Geology of Southwest Gondwana*, Springer, 10.1007/978-3-319-68920-3_4; Cingolani, *"The Tandilia System of Argentina as a southern extension of the Río de la Plata craton: an overview"*, **International Journal of Earth Sciences**. **Nível:** revisada por pares. **Confiança:** confirmado.

**Correção aplicada:** "no Uruguai e norte da Argentina" passou a "no Uruguai e na Argentina centro-oriental (aflorando no **Sistema de Tandilia**, sudeste da província de Buenos Aires, e estendendo-se em subsuperfície até as proximidades de Córdoba)". Propagado para a alegação `GEOFISSA-M18-A01-CRATONS-001`, que registra explicitamente que o cráton **não** está no norte da Argentina. Rapela et al. e Cingolani acrescentados às Fontes.


### 🟠 AUD-M18-A01-AMAZONICOPROVINCIAS-006 — Acresção do Cráton Amazônico descrita como radial, do centro para as bordas
**Aula 01, verbete do Cráton Amazônico.**
**Tipo:** impreciso (geometria do padrão).

**Está escrito:** *"Internamente, o cráton se organiza em províncias geocronológicas de idades decrescentes **do centro (arqueano) para as bordas (proterozoicas)**, um padrão de acresção crustal **para fora** ao longo de bilhões de anos."*

**Problema:** o padrão real não é radial. As províncias geocronológicas do Cráton Amazônico são faixas subparalelas de direção NW-SE que envelhecem **do nordeste para o sudoeste**, numa sequência única: Ventuari-Tapajós (1,95-1,80 Ga) → Rio Negro-Juruena (1,80-1,55 Ga) → Rondoniano-San Ignacio (1,45-1,30 Ga) → Sunsás (1,25-1,00 Ga). O núcleo arqueano (Província Amazônia Central) está no **leste-nordeste**, não no centro, e a acresção se deu ao longo da margem **ocidental** de um núcleo comum — um crescimento **lateral, unidirecional**, não concêntrico.

Por que importa aqui: a aula 02 usa a arquitetura de províncias para justificar variação de espessura crustal "associada à história de acresção de cada província geocronológica dentro do cráton". Um leitor com o modelo radial na cabeça vai esperar simetria em torno de um centro num mapa que é, na verdade, um gradiente diagonal.

**Correção proposta:** *"Internamente, o cráton se organiza em províncias geocronológicas dispostas em faixas subparalelas de direção NW-SE, que envelhecem **de nordeste para sudoeste** — do núcleo arqueano da Província Amazônia Central, a leste-nordeste, até a Província Sunsás (1,25-1,00 Ga), a sudoeste —, um padrão de acresção crustal sucessiva ao longo da margem ocidental do núcleo, e não um crescimento concêntrico."*

**Fonte:** Tassinari & Macambira (1999, 2004), províncias geocronológicas do Cráton Amazônico; *An Overview of the Amazonian Craton Evolution: Insights for Paleocontinental Reconstruction* (2015). **Nível:** revisada por pares. **Confiança:** confirmado.

**Correção aplicada:** o padrão radial "do centro (arqueano) para as bordas" foi substituído pelo gradiente real — faixas subparalelas NW-SE que envelhecem **de nordeste para sudoeste**, do núcleo arqueano da Província Amazônia Central (a leste-nordeste) até a Província Sunsás (1,25-1,00 Ga, a sudoeste), com a acresção se dando ao longo da margem **ocidental** do núcleo, explicitamente **não** concêntrica. Propagado para a alegação `GEOFISSA-M18-A01-CRATONS-001`; Tassinari & Macambira acrescentados às Fontes. Com isso o leitor chega à a02 com o modelo mental certo para a variação de espessura crustal por província geocronológica.


### 🟠 AUD-M18-A01-FLATSLABMECANISMO-007 — Mecanismo errado para a supressão do vulcanismo sobre subducção plana, e em desacordo com a explicação que a própria a02 dá
**Aula 01, seção dos Andes; comparar com a a02, seção de fluxo de calor.**
**Tipo:** impreciso (mecanismo) + inconsistência interna entre aulas.

**Está escrito (a01):** *"Esses segmentos coincidem com lacunas no vulcanismo ativo (**porque a placa fria não chega a profundidade suficiente sob o continente para gerar fusão parcial na cunha mantélica logo atrás do arco**)"*.

**Problema:** o mecanismo aceito é o **fechamento da cunha mantélica**: ao se horizontalizar, a laje encosta na base da litosfera continental e **expulsa** (ou desloca para o interior) a cunha de astenosfera quente que ficava entre as duas. Sem cunha astenosférica quente, não há o que fundir — independentemente da profundidade que a laje atinge. A formulação da aula sugere que a laje precisaria "chegar mais fundo" para haver fusão, o que embute dois erros de modelo: (a) quem funde é a **cunha mantélica**, não a laje; e (b) o flat slab peruano de fato atinge 60-70 km e o chileno central ultrapassa 100 km — profundidades comparáveis às de subducção normal sob o arco —, e ainda assim não há vulcanismo. A profundidade não é a variável de controle; a presença da cunha é.

**Agravante — inconsistência interna:** a aula 02, tratando do mesmo fenômeno, dá uma explicação **diferente e melhor**: *"suprimem o vulcanismo do arco exatamente por afastar a fonte de calor mantélica da base da crosta continental"*. As duas aulas ensinam mecanismos distintos para o mesmo fato, e a aula que o apresenta primeiro — a que o aluno vai fixar — é a que está errada.

**Correção proposta (a01):** *"(porque a laje, ao se horizontalizar, encosta na base da litosfera continental e **fecha a cunha de manto astenosférico quente** que, na subducção normal, ocupa o espaço entre as duas placas — e é essa cunha, não a laje, que funde parcialmente para alimentar o arco)"*. Com isso a a01 passa a dizer a mesma coisa que a a02, e a remissão entre elas fica coerente.

**Fonte:** literatura sobre lacunas magmáticas em subducção plana — *"Slab underthrusting is the primary control on flat-slab size"* (2025), PMC12248310, que enuncia a associação entre achatamento da laje e fechamento da cunha mantélica quente; Ramos & Folguera (2009), **GSL SP** 327(1); Gutscher et al., sobre a geometria e a profundidade dos flat slabs peruano (60-70 km) e chileno central (>100 km). **Nível:** revisada por pares. **Confiança:** confirmado.

**Correção aplicada:** o mecanismo "a placa fria não chega a profundidade suficiente" foi substituído pelo mecanismo aceito — a laje, ao se horizontalizar, encosta na base da litosfera continental e **fecha a cunha de manto astenosférico quente**, e é essa cunha, não a laje, que funde parcialmente para alimentar o arco. Propagado para o recap da a01 e para a alegação `GEOFISSA-M18-A01-FLATSLAB-003`, que registra também os contraexemplos de profundidade (peruano 60-70 km, chileno central >100 km, e ainda assim sem vulcanismo). **A a02 não precisou de edição:** sua formulação já era a correta, e a inconsistência entre as duas aulas foi resolvida por convergência da a01 para a a02.


### 🟠 AUD-M18-A01-RIBEIRA-008 — A Faixa Ribeira apresentada como a sutura direta São Francisco / Rio de La Plata, contra a própria aula
**Aula 01, seção "Faixas móveis" e Exemplo trabalhado, Localidade 3.**
**Tipo:** impreciso + inconsistência interna.

**Está escrito:** *"a **Faixa Ribeira** ... [fecha o Cráton São Francisco] contra o Cráton Rio de La Plata"*, e, no exemplo trabalhado, *"a posição geográfica descrita (entre esses dois crátons) corresponde à região da Faixa Ribeira, que registra a colisão que fechou o oceano **entre esses dois blocos**"*.

**Problema:** a Faixa Ribeira resulta do fechamento do Oceano Adamastor pela interação de **vários** blocos — São Francisco, **Paranapanema**, Rio de La Plata, **Luis Alves**, Congo e Kalahari — e é composta por quatro terrenos tectono-estratigráficos (Ocidental, Paraíba do Sul, Oriental e Cabo Frio). Reduzi-la a uma sutura São Francisco/Rio de La Plata apaga exatamente os blocos intermediários que a **própria aula acabou de apresentar dois parágrafos antes**: o Cráton Paranapanema e o Cráton Luis Alves. A colisão São Francisco-Paranapanema (~640-620 Ma) é o que gera a Faixa Brasília meridional, não a Ribeira.

O exemplo trabalhado piora o quadro, porque transforma a simplificação em **gabarito**: pergunta a que unidade pertence uma faixa neoproterozoica "entre São Francisco e Rio de La Plata" e responde "Faixa Ribeira" como se a geografia fosse unívoca — quando o que há entre os dois é uma colagem de blocos e ao menos duas faixas (Ribeira e Dom Feliciano).

**Correção proposta:** no corpo, *"e a **Faixa Ribeira**, no sudeste, que registra o fechamento do Oceano Adamastor e a interação entre o São Francisco-Congo, o Paranapanema, o Luis Alves e o Rio de La Plata — não uma sutura simples entre dois crátons"*. No exemplo trabalhado, reformular a Localidade 3 para pedir a **categoria** ("faixa móvel brasiliana") sem exigir a identificação nominal da faixa, ou mover a localidade para um par inequívoco (p. ex. Faixa Brasília, a oeste do São Francisco).

**Fonte:** Heilbron et al., *"The Ribeira Belt"*, em *São Francisco Craton, Eastern Brazil: Tectonic Genealogy of a Miniature Continent*, Springer, 10.1007/978-3-319-01715-0_15; revisão dos arcos magmáticos neoproterozoicos do Ribeira central, **JSAES** (2020). **Nível:** revisada por pares. **Confiança:** confirmado.

**Correção aplicada, nos dois pontos.** (a) **Corpo:** a Ribeira deixou de ser "a faixa que fecha o São Francisco contra o Rio de La Plata" e passa a registrar o fechamento do **Oceano Adamastor** com a interação entre São Francisco-Congo, Paranapanema, Luis Alves e Rio de La Plata, com a negação explícita "não uma sutura simples entre dois crátons" — o que reconcilia a seção com os crátons Paranapanema e Luis Alves apresentados dois parágrafos antes. (b) **Exemplo trabalhado, Localidade 3:** a resolução deixou de nomear a Faixa Ribeira como gabarito e passa a responder a **categoria** ("faixa móvel brasiliana"), explicando que a posição geográfica dada não identifica uma faixa específica — há uma colagem de blocos e ao menos duas faixas candidatas, Ribeira e Dom Feliciano — e que nomear exigiria dado estrutural, geocronológico ou geofísico que o relatório não fornece. Heilbron et al. acrescentado às Fontes.


### 🟠 AUD-M18-A02-ESPESSURACRATON-009 — Faixa de espessura crustal cratônica deslocada para baixo em relação à fonte que a própria aula cita
**Aula 02, seção "Espessura crustal"; propagado para o recap, para a alegação `GEOFISSA-M18-A02-CRUSTALTHICK-002` e para a a03 (que reusa "35 a 42 km").**
**Tipo:** impreciso (valor).

**Está escrito:** *"O **interior cratônico estável** da placa Sul-Americana tem crosta de espessura moderada, tipicamente na faixa de **35 a 42 quilômetros**"*.

**Problema:** a fonte citada — Assumpção et al. (2013), *Crustal thickness map of Brazil* — não sustenta esse recorte. Ali a espessura média da região continental estável é ~38-40 km (e ~41 km para a porção brasileira da plataforma); o **Cráton São Francisco** fica em **38-42 km**, com espessamento local a 44 km ao norte; e a **crosta mais espessa do Brasil está justamente no Cráton Amazônico**, com anomalias de Moho de até 50-60 km no escudo das Guianas e no sul do escudo Brasil-Central. Os **35 km** do limite inferior não são valor cratônico: são a assinatura da crosta **fina** da Província Borborema (30-35 km) e de uma faixa estreita da Província Tocantins (~35 km) — isto é, de **faixas móveis**, exatamente as unidades das quais a aula quer que o cráton se distinga.

O efeito é duplo: a faixa declarada engole o contraste que a seção existe para ensinar (cráton × faixa móvel), e trunca por cima justamente a unidade que detém o recorde continental brasileiro.

**Correção proposta:** *"tipicamente na faixa de **38 a 44 quilômetros** — próxima da espessura crustal continental média global —, com o Cráton Amazônico detendo a crosta mais espessa do território brasileiro (anomalias locais de Moho a 50-60 km no escudo das Guianas). Para contraste, a crosta **mais fina** do Brasil não está sob bacia nenhuma, e sim sob faixas móveis: 30-35 km na Província Borborema e ~35 km numa faixa estreita da Província Tocantins."* Propagar para o recap da a02, para a alegação e para a frase da a03 que reusa o par "60-70 / 35-42".

**Fonte:** Assumpção, Bianchi, Julià et al. (2013), *"Crustal thickness map of Brazil: Data compilation and main features"*, **JSAES** 43, 74-85 — a própria fonte da aula; Assumpção et al. (2017), *"Lithospheric Features of the São Francisco Craton"*, Springer; *"Crustal structure of the Amazonian Craton and adjacent provinces in Brazil"*, **JSAES** (2017), média 38,2 km com faixa 27,4-48,6 km. **Nível:** revisada por pares. **Confiança:** confirmado.

**Correção aplicada:** a faixa cratônica passou de **35-42** para **38-44 km**, com dois acréscimos que a própria fonte sustenta e que restauram o contraste que a seção existe para ensinar: o **Cráton Amazônico detém a crosta mais espessa do território brasileiro** (Moho local a 50-60 km no escudo das Guianas e no sul do escudo Brasil-Central), e a crosta **mais fina** do Brasil está sob **faixas móveis** (Borborema 30-35 km; faixa estreita da Província Tocantins ~35 km), não sob bacias. Propagado para o recap da a02, para a alegação `GEOFISSA-M18-A02-CRUSTALTHICK-002` e para a frase da a03 que reusava o par "60-70 / 35-42", agora "60-70 / 38-44".


### 🟠 AUD-M18-A03-BOUGUERCRATON-010 — Bouguer do interior cratônico descrita como "moderadamente positiva"
**Aula 03, seção "Gravimetria continental"; propagado para o recap e para a alegação `GEOFISSA-M18-A03-BOUGUERANDES-001`.**
**Tipo:** impreciso (sinal) + omissão que gera erro.

**Está escrito:** *"O interior cratônico, com crosta de espessura moderada e bem equilibrada isostaticamente havia muito tempo geológico, exibe anomalias de Bouguer mais próximas de zero **ou moderadamente positivas**, sem o forte déficit regional que caracteriza a raiz andina."*

**Problema:** a metade "próximas de zero" está certa; "ou moderadamente positivas" como descrição **geral** do interior cratônico não está. Sobre crosta continental normal, a anomalia de Bouguer é ~0 ao nível do mar e fica **progressivamente mais negativa** com a elevação — e é isso que se observa no escudo brasileiro: no SE do Brasil, a região de topografia mais alta é caracterizada por Bouguer **mais baixa**, sinal de que a isostasia regional se mantém; a Bacia do Parnaíba se assenta num *low* amplo de ~-40 mGal.

Onde há Bouguer francamente **positiva** no interior do continente, ela **não** é a assinatura de "cráton bem compensado": é um alto estreito alinhado ao **eixo** de bacias intracratônicas — na Bacia do Amazonas, uma cadeia de altos de +40 a +90 mGal coincidente com o eixo de máxima espessura sedimentar, ladeada por *lows* de ~-40 mGal —, e reflete **subplacagem máfica e afinamento crustal** sob o eixo da bacia, um mecanismo completamente diferente. A aula, ao oferecer "moderadamente positiva" como leitura normal do cráton, entrega ao aluno um sinal diagnóstico com a explicação trocada.

**Correção proposta:** *"O interior cratônico, com crosta de espessura moderada e isostaticamente equilibrada havia muito tempo geológico, exibe anomalias de Bouguer próximas de zero ao nível do mar, tornando-se moderadamente negativas onde a topografia sobe — sem o forte déficit regional que caracteriza a raiz andina. Altos de Bouguer francamente positivos no interior do continente existem, mas são estreitos e alinhados ao **eixo** de bacias intracratônicas (na Bacia do Amazonas, +40 a +90 mGal sobre o eixo de máxima espessura sedimentar, ladeados por lows de ~-40 mGal), e a leitura deles não é 'cráton compensado': é afinamento crustal e subplacagem máfica sob o eixo da bacia."*

**Fonte:** Tozer et al. (2017), *"Crustal structure, gravity anomalies, and subsidence history of the Parnaíba cratonic basin"*, **JGR Solid Earth**, 10.1002/2017JB014348; Assumpção et al. (2002), *"Crustal thicknesses in SE Brazilian Shield by receiver function analysis: Implications for isostatic compensation"*, **JGR** 107(B1); literatura sobre os altos gravimétricos do eixo da Bacia do Amazonas. **Nível:** revisada por pares. **Confiança:** confirmado.

**Correção aplicada:** "próximas de zero ou moderadamente positivas" passou a "próximas de zero ao nível do mar, tornando-se moderadamente **negativas** onde a topografia sobe", e foi acrescentado o trecho que devolve a leitura correta aos altos francamente positivos do interior: são estreitos, alinhados ao **eixo** de bacias intracratônicas (Bacia do Amazonas, +40 a +90 mGal sobre o eixo de máxima espessura sedimentar, ladeados por *lows* de ~-40 mGal) e significam **afinamento crustal e subplacagem máfica**, não cráton compensado. Propagado para o recap da a03 e para a alegação `GEOFISSA-M18-A03-BOUGUERANDES-001`; Tozer et al. (2017) e Assumpção et al. (2002) acrescentados como fontes da alegação.


### 🟠 AUD-M18-A04-ESFORCOSANDES-011 — A energia potencial gravitacional dos Andes rebaixada a perturbação local, e uma "tração" atribuída à placa cavalgante
**Aula 04, seção "O campo de esforços regional"; propagado para o recap e para a alegação `GEOFISSA-M18-A04-CAMPOESFORCOS-005`.**
**Tipo:** impreciso + confusão de escopo.

**Está escrito:** *"o **empurrão de dorsal** (*ridge push*) ... e a **resistência (ou eventual tração)** transmitida pela zona de subducção andina no lado oposto da placa — de modo que ... boa parte do interior da placa Sul-Americana está sob um regime de compressão de escala de placa, resultante do balanço entre essas forças de borda, ainda que **localmente** esse padrão regional possa ser perturbado por estruturas crustais herdadas e por processos superficiais, **como o próprio peso e a erosão diferencial da topografia andina**."*

**Problema:** dois pontos.

(a) **"eventual tração" não se aplica.** *Slab pull* atua sobre a placa **subductante** (Nazca), não sobre a placa **cavalgante** (Sul-Americana). Não há mecanismo reconhecido pelo qual a subducção andina transmita **tração** ao interior da placa Sul-Americana; o que ela transmite é força resistiva/compressiva ao longo da margem. O parêntese introduz um mecanismo inexistente num ponto em que a aula está justamente montando o balanço de forças.

(b) **A topografia andina está do lado errado da hierarquia.** Na modelagem de referência do campo de esforços intraplaca sul-americano, o regime compressivo E-O de primeira ordem resulta da **interação entre o empurrão de dorsal e as forças colisionais ao longo da margem ocidental**, e as **forças de flutuabilidade/topográficas** — explicitamente incluindo a crosta continental elevada da Cordilheira Andina, ao lado da dorsal e das margens continentais — são um dos **dois processos tectônicos principais**, não um ruído. A aula inverte isso: nomeia "o próprio peso ... da topografia andina" como perturbação **local** de um padrão regional que, na literatura, ela ajuda a **produzir**.

**Correção proposta:** remover "(ou eventual tração)"; e reescrever o fecho como *"...resultante do balanço entre o empurrão de dorsal, as forças colisionais transmitidas ao longo da margem convergente ocidental e as forças de flutuabilidade da topografia elevada — a própria Cordilheira Andina, cuja energia potencial gravitacional é uma das fontes de primeira ordem do campo, e não uma perturbação local. O que perturba localmente esse padrão são estruturas crustais herdadas, cargas sedimentares flexurais e afinamentos litosféricos."* Acrescentar Coblentz & Richardson (1996) às Fontes.

**Fonte:** Coblentz & Richardson (1996), *"Analysis of the South American intraplate stress field"*, **JGR Solid Earth** 101, 8643-8657, 10.1029/96JB00090; Assumpção et al. (2016), *"Intraplate stress field in South America from earthquake focal mechanisms"*, **JSAES**. **Nível:** revisada por pares. **Confiança:** confirmado.

**Correção aplicada, nos dois pontos.** (a) "(ou eventual tração)" foi removido e substituído por uma ressalva explícita de que *slab pull* atua sobre a placa **subductante** (Nazca) e não sobre a cavalgante, e que o que a margem convergente transmite ao interior sul-americano é força **resistiva/compressiva**. (b) A topografia andina foi promovida de perturbação local a **fonte de primeira ordem** do campo, com o balanço reescrito como empurrão de dorsal + forças colisionais da margem ocidental + forças de flutuabilidade da topografia elevada; as perturbações locais passaram a ser estruturas crustais herdadas, cargas sedimentares flexurais e afinamentos litosféricos. Propagado para o recap e para a alegação `GEOFISSA-M18-A04-CAMPOESFORCOS-005`; **Coblentz & Richardson (1996)** e Assumpção et al. (2016) acrescentados às Fontes.

---

## Achados amarelos (todos corrigidos)

Os seis foram corrigidos. A coluna da direita descreve o que passou a constar no arquivo, não mais uma proposta.

| ID | Aula | Achado | Correção aplicada |
|---|---|---|---|
| `AUD-M18-A03-GOTZEKRAUSE-012` | a03 | **Götze & Krause (2002) creditado pela anomalia de Bouguer *negativa* andina.** O artigo chama-se *"The Central Andean gravity **high**, a relic of an old subduction complex?"* e trata de um **alto** de gravidade residual isostática centrado no **flanco ocidental** dos Andes Centrais a ~24°S, atribuído a um corpo denso de ~400 km de comprimento entre 10 e 38 km de profundidade, possivelmente um complexo de subducção Ordovício-Siluriano. É a feição de **sinal oposto** ao que a aula usa a referência para sustentar. | Manter Götze & Krause como leitura sobre o **alto** do antearco (e é um bom contraponto didático: nem toda anomalia andina é negativa). Creditar a Bouguer regional negativa e a estrutura de densidade da margem a **Tassara et al. (2006)**, JGR 111(B9), já citada, e à compilação gravimétrica andina |
| `AUD-M18-A03-WARDMT-013` | a03/a02 | **Ward et al. (2014) anotado como "integração sísmica e magnetotelúrica".** O artigo é uma inversão conjunta de **dispersão de ondas de superfície + funções do receptor** — inteiramente sísmica; nenhum dado MT entra nela. O corpo magmático do Altiplano-Puna que ele imageia é descrito como zona elíptica de baixa velocidade S de ~200 km de diâmetro e ~10 km de espessura na crosta média | Trocar a anotação para "(corpo magmático do Altiplano-Puna por inversão conjunta **sísmica**: dispersão de ondas de superfície e funções do receptor; ~200 km de diâmetro, ~10 km de espessura, crosta média)". O lado magnetotelúrico já está corretamente coberto por Comeau et al. (2015) |
| `AUD-M18-A03-PINTOHALLINAN-014` | a03 | **Entrada de bibliografia colada:** *"Pinto, V., Hallinan, S. E. et al., compilações de mapas aeromagnéticos regionais do Serviço Geológico do Brasil (CPRM)..."* — sem ano, sem periódico, com a inicial errada, e fundindo autores de trabalhos distintos. Mesmo defeito do achado `AUD-M17-A05-KAMINSKI-011` do módulo anterior | Separar em duas entradas reais: **Hallinan, S. E., Mantovani, M. S. M., Shukowsky, W. & Braggion Jr., I. (1993)**, *"Estrutura do Escudo Sul-Brasileiro: uma revisão através de dados gravimétricos e magnetométricos"*, **Revista Brasileira de Geociências**; e **Pinto, L. G. R. & Vidotti, R. M. (2019)**, sobre domínios do embasamento da Bacia do Paraná por gravimetria e magnetometria. Manter a menção ao acervo aerogeofísico do SGB/CPRM como **acervo**, não como autoria |
| `AUD-M18-A03-HEIRTZLER-015` | a03 | **"Heirtzler, J. R. et al., literatura padrão sobre a Anomalia Magnética do Atlântico Sul"** — sem ano, sem periódico, e com "et al." num artigo de autor único | Citar corretamente: **Heirtzler, J. R. (2002)**, *"The future of the South Atlantic anomaly and implications for radiation damage in space"*, **Journal of Atmospheric and Solar-Terrestrial Physics** 64(16), 1701-1708, DOI 10.1016/S1364-6826(02)00120-7. O conteúdo que a aula sustenta com ela está **correto** — o defeito é só a citação |
| `AUD-M18-A01-PERUFLATSLAB-016` | a01, a04 | **Flat slab peruano dado como "~3-15°S"**, creditado a Ramos & Folguera (2009) — que o situa em **5-15°S**. Ramos et al. (2002) e as revisões posteriores dão 5-15°S ou 5-14°S; o limite norte de 3°S não sai da fonte citada. (O pampeano, "~27-33°S", **confere**: Ramos et al. 2002 dá 27°00'-33°30'S) | Trocar para **"~5-15°S"** nos **quatro** lugares em que aparece: corpo e recap da a01, e corpo e recap da a04. Atualizar as alegações `GEOFISSA-M18-A01-FLATSLAB-003` e `GEOFISSA-M18-A04-FLATSLABSISMICO-003` |
| `AUD-M18-A04-ASSUMPCAO1998-017` | a04 | **Assumpção (1998), BSSA 88(1), 160-169, creditado por "sismicidade intraplaca brasileira, incluindo Mogi Guaçu".** O artigo chama-se *"Seismicity and stresses in the Brazilian **passive margin**"* e trata da sismicidade das margens NE (onshore, transcorrente) e SE (offshore, inversa) — não do interior cratônico nem de Mogi Guaçu (SP), que fica a ~300 km da costa | Manter Assumpção (1998) para o campo de esforços **da margem**. Creditar a sismicidade intraplaca do interior a **Assumpção et al. (2004)**, *"Intraplate seismicity in SE Brazil: stress concentration in lithospheric thin spots"*, **Geophysical Journal International** 159(1), 390-399, e/ou à síntese de sismicidade intraplaca brasileira, que é onde o evento de Mogi Guaçu efetivamente aparece |

---

## Achado branco (controvérsia real — mantida, agora apresentada como controvérsia)

### ⚪ AUD-M18-A01-CHACOPARANA-W1 — A Bacia Chaco-Paranaense classificada sem ressalva como bacia de antepaís
**Aula 01, seção "Bacias sedimentares"; propagado para o recap e para a alegação `GEOFISSA-M18-A01-BACIAS-005`.**

**Está escrito:** *"**Bacias de antepaís (foreland):** ... a **Bacia Chaco-Paranaense**, a Bacia de Bermejo e a Bacia de Magallanes, entre outras"*.

**Problema:** a classificação tectônica da Chaco-Paranaense é objeto de divergência real. Um campo a trata como **bacia de antepaís**, iniciada no Oligoceno superior pela resposta flexural ao encurtamento do retroarco andino; outro a trata como **bacia intracratônica / sag de margem passiva**, com ~500.000 km² sobre crosta continental, baixas taxas de subsidência e atividade magmática e tectônica limitada. A divergência é substantiva e em parte geográfica — a porção ocidental tem caráter de antepaís andino, a oriental não.

Isso é especialmente sensível **nesta aula**, cujo exercício central é justamente pedir ao leitor que classifique uma bacia em uma das três famílias. Oferecer como exemplo de antepaís uma bacia cuja família é disputada corrói o próprio critério que a seção ensina. As outras duas — Bermejo e Magallanes — são exemplos limpos e não têm esse problema.

**Correção proposta:** ou (a) retirar a Chaco-Paranaense da lista de antepaís, deixando Bermejo e Magallanes, que são inequívocas; ou (b) mantê-la com a ressalva explícita, que é didaticamente mais rico: *"a Bacia Chaco-Paranaense — cuja classificação é ela própria disputada, lida como antepaís andino por sua porção ocidental e como bacia intracratônica/sag por sua porção oriental, e um bom lembrete de que as três famílias são um esquema de primeira ordem, não gavetas estanques"*.

**Fonte:** *"Andean foreland evolution and flexure in NW Argentina: Chaco-Paraná Basin"*, **Tectonophysics** (2014) — leitura de antepaís; *"Late Paleozoic tectono-sedimentary evolution of eastern Chaco-Paraná Basin (Uruguay, Brazil, Argentina and Paraguay)"*, **JSAES** (2020) — leitura intracratônica. **Nível:** revisada por pares. **Confiança:** em disputa (é o achado).

**Tratamento aplicado — opção (b), que é a conduta prescrita para achado branco: não escolher lado, e sim expor a divergência.** A Chaco-Paranaense saiu da enumeração direta de exemplos de antepaís — que agora abre com **Bermejo e Magallanes**, os exemplos inequívocos — e passou a entrar com a ressalva explícita de que sua classificação é ela própria disputada, lida como antepaís andino pela porção ocidental e como intracratônica/*sag* pela oriental, fechando com o lembrete didático de que as três famílias são um esquema de primeira ordem, não gavetas estanques. Propagado para o recap e para a alegação `GEOFISSA-M18-A01-BACIAS-005`, cujo `risk` passou de `fato` para `controversia`.

**A controvérsia permanece aberta na literatura** e não cabia à auditoria resolvê-la — o que mudou é que a aula não a apresenta mais como resolvida. **Não bloqueia o gate**, mas **restringe o formato das questões**: nenhuma questão fechada deve exigir que a Chaco-Paranaense seja classificada como antepaís. O que é cobrável com segurança é a **existência** da divergência e seu eixo geográfico.

---

## Achados azuis (verificados, corretos, sem alteração — não exigem correção)

- **B1 — Zona de Wadati-Benioff e suas três faixas de profundidade (a04).** Nome, atribuição a Wadati e Benioff como reconhecimento independente, e o corte convencional raso (até ~70 km, interface, megaterremotos) / intermediário (~70-300 km, intralaje, desidratação mineral e transformações de fase) / foco profundo (~300-700 km, mecanismo em pesquisa ativa, com as hipóteses de transformação metaestável e instabilidade termal por cisalhamento nomeadas corretamente): **tudo confere.** Esta era a seção de maior risco declarado da a04 e está limpa.
- **B2 — O sismo profundo da Bolívia (a04): correto como escrito, e a alegação do autor pode ser fechada.** A alegação `GEOFISSA-M18-A04-BOLIVIA-002` pedia explicitamente que a auditoria conferisse magnitude, profundidade e data. Confirmado: **9 de junho de 1994** (8 de junho em hora local), **Mw 8,2** (algumas soluções dão 8,3), **profundidade ~631 km**, epicentro ~55 km NNO de Reyes, Bolívia. Foi **o maior sismo de foco profundo já registrado instrumentalmente até 2013**, quando o evento do Mar de Okhotsk (24/05/2013, Mw 8,3, 609 km) o superou, com momento sísmico ~30% maior. Portanto a formulação hedgeada da aula — *"um dos maiores sismos de foco profundo já instrumentalmente registrados"* — **está correta e é a formulação certa**; trocá-la por "o maior" seria introduzir um erro. *Recomendação opcional, não achado:* inserir data, Mw e profundidade no corpo, já que agora estão conferidos, e nomear o Okhotsk 2013 como o recordista atual. **Fonte:** USGS event page usp0006dzc; Kikuchi & Ishii (1994), **GRL**; Ye et al. (2013), **Science** (Okhotsk).
- **B3 — Enxame de João Câmara (a04).** Início em **agosto de 1986**, intensificação em novembro, evento principal em **30/11/1986 (mb 5,1)**, segundo pico em **20/03/1987 (mb 5,0)**, mais de 1.000 eventos registrados, atividade prolongando-se pelo restante da década — a descrição da aula ("ativo entre meados e o final da década de 1980") **confere**. A associação a reativação de estrutura do embasamento também: o Sistema de Falhas Samambaia, falhas normais E-O a ENE-WSW, 30-40 km de comprimento. Ferreira et al. (1998), **GJI** 134(2), 341-355, está **corretamente** citado aqui.
- **B4 — Mogi Guaçu (a04) existe e é bom exemplo.** O maior evento do sudeste brasileiro ocorreu em **1922** perto de Mogi Guaçu (SP), **mb 5,1 (~Mw 4,8)**, intensidade até VI MMI e raio de percepção ~300 km. O fato está correto; o defeito é só de **fonte** (ver 🟡 `...ASSUMPCAO1998-017`).
- **B5 — Quilhas cratônicas, 150-250 km (a02).** Confere e está bem calibrado: tomografia de ondas de superfície dá ~200 km para a porção arqueana meridional do Cráton São Francisco; litosfera térmica de 200-300 km sob o sul do Amazônico e o São Francisco; e o Rio de La Plata meridional retém quilha de **200-250 km**. Nomear os três crátons juntos, como a aula faz, é **sustentado** pela literatura — não era óbvio e foi verificado um a um.
- **B6 — Altiplano-Puna, 60-70 km (a02, a03).** Dentro do aceito. Beck & Zandt (2002) e a literatura subsequente sustentam ~70 km, com a faixa usualmente dada como 60-75 km e Moho localmente >80 km sob o Altiplano (e ~45 km sob a Puna setentrional, uma heterogeneidade que a aula não precisa cobrir). A comparação com Himalaia/Tibete (70-80 km) é justa. *Nota:* se algum dia o número for retocado, o limite superior usual é 75, não 70.
- **B7 — Crosta oceânica 6-8 km (a02).** Confere com a espessura padrão de crosta oceânica madura.
- **B8 — Física do método magnetotelúrico (a02).** Fonte de sinal (variações naturais do campo EM, ionosfera/magnetosfera), relação frequência-profundidade, alcance de longo período até manto litosférico e astenosfera, e — o ponto mais fácil de errar — a ênfase em que o que controla a queda de resistividade é a **interconexão** da fase condutiva, não sua fração volumétrica. Correto nos três agentes citados (fluido salino, grafita, fusão parcial).
- **B9 — Corpo magmático do Altiplano-Puna (a02).** Existe, está na **crosta média**, é imageado tanto por sismologia quanto por MT, e a caracterização como uma das maiores acumulações de fusão parcial documentadas em crosta continental é sustentada. Ward et al. (2014): ~200 km de diâmetro, ~10 km de espessura. Comeau et al. (2015), **Geology** 43(3), 243-246, **confere exatamente** na paginação e no conteúdo (MT de banda larga, modelos 2D e 3D, topo do APMB mais raso sob o Uturuncu). Aula correta; só a **anotação** de Ward está errada (🟡 `...WARDMT-013`).
- **B10 — Fluxo de calor por província (a02) e os ~40 mW/m² do exemplo trabalhado.** Coerente: os valores cratônicos sul-americanos estão na faixa baixa continental (São Francisco ~35-42 mW/m²; Cráton do Amazonas em faixa ampla de normalidade), com valores altos nas faixas móveis e em zonas de litosfera fina. Os ~40 mW/m² atribuídos ao interior do Cráton Amazônico no exemplo trabalhado estão dentro do observado. A aula acerta ao apresentar isso **qualitativamente**, dada a cobertura desigual de dados — o que o próprio hub já registra nos Pontos de dificuldade.
- **B11 — Maré terrestre (a03).** Deslocamento vertical de dezenas de centímetros e variação de gravidade "de dezenas a algumas centenas de microgals por ciclo": **confere.** A amplitude típica de gravidade de maré é da ordem de 100 μGal, com a conversão de referência entre 2 e 3 μGal por cm de deslocamento. Previsibilidade por modelo a partir das posições Lua-Sol-Terra e a necessidade da correção em estações fixas de longa duração: corretas.
- **B12 — Anomalia crustal × Anomalia Magnética do Atlântico Sul (a03).** O melhor parágrafo do módulo, e foi verificado justamente por ser o tipo de distinção onde um material se engana. A SAA é feição do **campo principal** gerado pelo dínamo do núcleo externo, com relevância para engenharia de satélites e dose de radiação em órbita, e não é anomalia crustal nem entra em interpretação estrutural. Tudo correto — inclusive a observação de que a semelhança de nome e unidade é a origem da confusão. Só a citação precisa de conserto (🟡 `...HEIRTZLER-015`).
- **B13 — Mecânica do paleomagnetismo (a03).** Aquisição de magnetização remanente (resfriamento abaixo do ponto de Curie em ígneas; alinhamento detrítico em sedimentos), óxidos de Fe-Ti como portadores, dipolo geocêntrico axial em primeira ordem, inclinação → paleolatitude, declinação → rotação local, construção do polo paleomagnético e da APWP, e a limitação estrutural de **não** determinar paleolongitude: **tudo correto**, e a limitação da paleolongitude é enunciada com precisão incomum. O defeito da seção é apenas o parêntese sobre TPW (🔴 1) — o resto é sólido.
- **B14 — Geoide × Bouguer (a03).** Separação por comprimento de onda, sensibilidade do geoide a heterogeneidades profundas de densidade no manto (inclusive lajes subductadas e plumas), complementaridade em vez de substituição, e o alerta de que usar o geoide para mapear uma bacia local não funciona porque o sinal está no comprimento de onda errado: corretos.
- **B15 — Ciclo Brasiliano, ~900-500 Ma (a01).** Confere como faixa aproximada: o ciclo é datado ~900-480 Ma, com a amalgamação do Gondwana Ocidental começando no intervalo 900-700 Ma e a amalgamação final em ~550-530 Ma, e com o pico orogênico maior na transição Ediacarano/Cambriano. A ressalva de diacronismo que a própria alegação do autor já traz é correta e vale a pena manter.
- **B16 — Moho × base da litosfera (a02).** A distinção (salto composicional/de velocidade × transição reológica) e a afirmação de que a litosfera é sempre mais espessa que a crosta: corretas.
- **B17 — Bouguer andina entre as mais negativas do planeta (a03).** Confere; a comparação com o Himalaia é adequada. É só a **fonte** que está trocada (🟡 `...GOTZEKRAUSE-012`).
- **B18 — Limites da placa Sul-Americana (a01).** Dorsal Meso-Atlântica a leste, Fossa Peru-Chile a oeste, subducção de Nazca e, ao sul do ponto tríplice do Chile, da placa Antártica; complexidade ao norte (Caribe) e ao sul (Scotia): corretos.

---

## Nota transversal — o Módulo 17 já tinha esta doença, e ela não foi tratada

A auditoria do Módulo 17 identificou como **padrão dominante** a "ATRIBUIÇÃO DE FONTE — o dado certo debaixo do nome errado", com quatro ocorrências, e explicou por que isso é especialmente caro num curso autodidata: o leitor que vai conferir não encontra nada e conclui que o material inventou o dado.

**O Módulo 18 reincide com quatro ocorrências do mesmo padrão** — `GOTZEKRAUSE-012`, `WARDMT-013`, `PINTOHALLINAN-014`, `HEIRTZLER-015`, mais `ASSUMPCAO1998-017` e a discrepância de faixa em `PERUFLATSLAB-016`, que são a mesma família. Duas delas são cópias estruturais exatas de achados do M17: `PINTOHALLINAN-014` é a entrada de bibliografia colada com autor espúrio (igual a `AUD-M17-A05-KAMINSKI-011`), e `GOTZEKRAUSE-012` é o dado creditado ao artigo que trata do fenômeno **oposto** (igual a `AUD-M17-A02-TEDESCHI-001`, o vermelho daquele módulo).

Isto não é coincidência de dois módulos: é um defeito do processo de redação, não do conteúdo de um módulo específico. **Recomendação ao orquestrador:** antes de escrever o Módulo 19, acrescentar ao gerador de aula uma verificação obrigatória de que cada entrada da lista de Fontes (a) existe com aquele autor, ano, periódico e paginação e (b) trata efetivamente do fato que a aula lhe credita. É barato na redação e, aqui, teria evitado seis dos dezessete achados.

**Situação depois da correção:** as seis ocorrências deste padrão no Módulo 18 estão corrigidas nos arquivos — a entrada com autor espúrio foi desfeita em três referências reais, a citação sem ano ganhou DOI e paginação, a anotação que contradizia o título do artigo foi reescrita, e os dois dados creditados ao artigo errado foram devolvidos à fonte que de fato os produz. **A recomendação de processo, porém, continua de pé:** ela é sobre o Módulo 19 em diante, e corrigir o M18 não a atende.

## Nota transversal — consistência com os módulos anteriores

Verificação explícita contra os módulos que este declara como antecedentes. **Nenhuma contradição encontrada.**

1. **Módulo 15 (petrofísica), pré-requisito formal:** densidade, velocidade sísmica, porosidade e condutividade elétrica são usadas na a02 na mesma acepção do M15, agora em escala de placa. A a01 declara corretamente que **não** aciona o M15, e não aciona. Sem salto.
2. **Módulo 17 (geofísica marinha):** a a03 remete às correções de campos potenciais (Eötvös, Bouguer marinha) do M17 sem reensiná-las e sem divergir. As anomalias magnéticas lineares da crosta oceânica são invocadas na a01 e na a03 na mesma acepção auditada e aprovada no M17. A família de bacias de margem passiva (Santos, Campos, Espírito Santo, Sergipe-Alagoas) é remetida ao M17 sem repetir dado, o que evita justamente o tipo de divergência numérica que uma auditoria transversal caçaria.
3. **Compensação isostática:** o princípio é usado na a02 e na a03 de forma consistente entre si e com o M17 — crosta espessa e menos densa flutuando mais alto e mais fundo, produzindo déficit de massa e Bouguer negativa. O sentido **não** está invertido em nenhum dos três pontos (verificado individualmente, dado o histórico de inversões dos Módulos 10 e 17).
4. **Classificação de bacias:** a a01 declara explicitamente que a classificação por **contexto tectônico** é complementar, e não concorrente, à classificação por **mecanismo de subsidência** do M10/M17. Declaração de compatibilidade correta e bem-vinda — é o mesmo acerto didático que a auditoria do M17 elogiou.

O que **não** se sustentou na verificação transversal foi interno ao próprio módulo: a a01 e a a02 dão **mecanismos diferentes** para a supressão do vulcanismo em subducção plana (achado 🟠 `...FLATSLABMECANISMO-007`), e a a01 contradiz a si mesma ao introduzir o Cráton Paranapanema e, dois parágrafos adiante, tratar a Faixa Ribeira como sutura direta São Francisco/Rio de La Plata (🟠 `...RIBEIRA-008`).

---

## Gate de avaliação

**LIBERADO.** 0 achados 🔴 e 0 🟠 em aberto — todos corrigidos em 2026-09-11, com a correção aplicada também aos recaps, exemplos trabalhados e alegações auditáveis que repetiam o dado errado. **Questionário e baralho de flashcards podem ser gerados**, observadas as restrições de formato abaixo.

Os cinco pontos que bloqueavam o gate foram desfeitos na origem:

- a posição das faixas (**Araguaia** na borda leste, **Paraguai** na borda sul-sudeste) e a localização do **Cráton Rio de La Plata** (Tandilia, sudeste de Buenos Aires) estão corretas no corpo, no recap e nas alegações — um flashcard de localização gerado agora nasce certo;
- o **sentido de aprofundamento da laje** está corrigido no exemplo trabalhado da a04 e reforçado por uma frase que fixa a fossa a oeste e o mergulho para leste nos dois regimes: o risco de gabarito invertido, que era o mais caro do módulo, desapareceu;
- a faixa de espessura crustal cratônica passou a **38-44 km**, com o contraste cráton × faixa móvel restaurado (e a crosta mais fina do Brasil devolvida às faixas móveis, onde ela de fato está);
- **"Bouguer moderadamente positiva sobre cráton"** deixou de ser afirmação da aula e virou distrator: o texto agora ensina "próxima de zero ao nível do mar, moderadamente negativa onde a topografia sobe";
- a **Localidade 3** do exemplo trabalhado da a01 não pede mais o nome da faixa, e a **Chaco-Paranaense** entra com ressalva de controvérsia — as duas questões que a literatura não fechava saíram do formato de gabarito.

**Restrições de formato que permanecem válidas** (não bloqueiam a geração; delimitam o que pode ser cobrado em questão fechada):

- (a) **Não** cobrar a classificação tectônica da Bacia Chaco-Paranaense em questão fechada (⚪ `...CHACOPARANA-W1`, tratado mas não resolvido pela literatura). Bermejo e Magallanes são os exemplos seguros de antepaís; o cobrável é a **existência** da divergência e seu eixo geográfico.
- (b) **Não** cobrar a origem da Patagônia como fato resolvido. A controvérsia alóctone × autóctone é corretamente apresentada nas aulas 01 e 03 e **o cobrável é o eixo da controvérsia e o papel do dado paleomagnético nela**, nunca um veredito.
- (c) Ao cobrar a APWP, cobrar que ela é **dominada pelo movimento de placa** e que há uma componente menor de **deriva polar verdadeira** somada, cuja separação é problema de pesquisa corrente (texto já corrigido). Nunca afirmar que o eixo de rotação é fixo em relação ao manto — é exatamente o erro que foi corrigido.
- (d) Ao cobrar o sismo profundo da Bolívia, cobrar "**um dos maiores** já registrados instrumentalmente", nunca "o maior" — o recordista é o evento do Mar de Okhotsk de 2013. A formulação hedgeada da aula está certa e não deve ser "melhorada".
- (e) Ao cobrar subducção plana, cobrar a **geometria em profundidade** e a extensão da sismicidade continente adentro, e **não** o campo de esforços superficial — que, como a própria a04 diz corretamente, não discrimina os dois regimes. Ao cobrar o sentido, cobrar que a laje mergulha **para leste em ambos os regimes** e que o discriminante é a **taxa** de aprofundamento.
- (f) Ao cobrar limites de flat slab, usar **5-15°S** (peruano) e **27-33°S** (pampeano) — valores já corrigidos no texto.
- (g) Ao cobrar espessura crustal cratônica, usar **38-44 km** (não 35-42, que era o valor errado), e lembrar que a crosta **mais fina** do Brasil está sob faixas móveis (Borborema 30-35 km), não sob bacias — o contraste é bom material de questão de aplicação.
- (h) Ao cobrar Bouguer sobre cráton, a resposta é "próxima de zero ao nível do mar, moderadamente **negativa** onde a topografia sobe". "Moderadamente positiva" agora é **distrator**, não gabarito.

---

## Observação fora de escopo (não é achado factual)

Duas coisas saltaram à vista e pertencem a outras skills, registradas aqui em uma linha cada para não se perderem:

- **Estrutural (`validador-estrutural-do-curso`):** o cabeçalho da a03 usa o wikilink em formato de caminho — `[[17-geofisica-marinha-bacias-sedimentares/17-geofisica-marinha-bacias-sedimentares-modulo|Módulo 17]]` — enquanto os links internos ao módulo usam nome de arquivo puro. As duas formas convivem no curso; vale conferir qual resolve no vault.
- **Didática (`revisor-didatico`):** a a03 carrega quatro blocos conceituais independentes (Bouguer, geoide, maré terrestre, paleomagnetismo) em ~2.200 palavras declaradas, sendo a maior das quatro aulas, e o paleomagnetismo tem material próprio suficiente para uma aula inteira. Não é achado desta auditoria — é exatamente o tipo de carga que produziu o encaminhamento `DID-M17-A04-CARGA-003` no módulo anterior.

---

## Desfecho — correções aplicadas

**Aplicadas em:** 2026-09-11

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `AUD-M18-A03-TPW-001` | 🔴 | Corrigido | aula-03 (corpo, recap, alegação, Fontes) |
| `AUD-M18-A01-PARAGUAIARAGUAIA-002` | 🔴 | Corrigido | aula-01 (corpo, recap, alegação, Fontes) |
| `AUD-M18-A04-MERGULHOOESTE-003` | 🔴 | Corrigido | aula-04 (exemplo trabalhado — situação e resolução —, alegação) |
| `AUD-M18-A01-ARACUAI-004` | 🟠 | Corrigido | aula-01 (corpo, recap, alegação, Fontes) |
| `AUD-M18-A01-RIOPLATA-005` | 🟠 | Corrigido | aula-01 (corpo, alegação, Fontes) |
| `AUD-M18-A01-AMAZONICOPROVINCIAS-006` | 🟠 | Corrigido | aula-01 (corpo, alegação, Fontes) |
| `AUD-M18-A01-FLATSLABMECANISMO-007` | 🟠 | Corrigido | aula-01 (corpo, recap, alegação) — a02 não precisou de edição: já estava correta |
| `AUD-M18-A01-RIBEIRA-008` | 🟠 | Corrigido | aula-01 (corpo, recap, exemplo trabalhado, alegação, Fontes) |
| `AUD-M18-A02-ESPESSURACRATON-009` | 🟠 | Corrigido | aula-02 (corpo, recap, alegação), aula-03 (corpo) |
| `AUD-M18-A03-BOUGUERCRATON-010` | 🟠 | Corrigido | aula-03 (corpo, recap, alegação) |
| `AUD-M18-A04-ESFORCOSANDES-011` | 🟠 | Corrigido | aula-04 (corpo, recap, alegação, Fontes) |
| `AUD-M18-A03-GOTZEKRAUSE-012` | 🟡 | Corrigido | aula-03 (Fontes, alegação) |
| `AUD-M18-A03-WARDMT-013` | 🟡 | Corrigido | aula-02 (Fontes) |
| `AUD-M18-A03-PINTOHALLINAN-014` | 🟡 | Corrigido | aula-03 (Fontes) |
| `AUD-M18-A03-HEIRTZLER-015` | 🟡 | Corrigido | aula-03 (Fontes) |
| `AUD-M18-A01-PERUFLATSLAB-016` | 🟡 | Corrigido | aula-01 (corpo, recap, alegação), aula-04 (corpo, recap, alegação) |
| `AUD-M18-A04-ASSUMPCAO1998-017` | 🟡 | Corrigido | aula-04 (Fontes, alegação) |
| `AUD-M18-A01-CHACOPARANA-W1` | ⚪ | Mantido como controvérsia, agora com os dois campos expostos | aula-01 (corpo, recap, alegação) |

**Arquivos tocados:** os quatro arquivos de aula (a01, a02, a03, a04) e o hub do módulo. Os 18 achados 🔵 não geraram edição — são registros de verificação bem-sucedida, e alterá-los seria introduzir erro onde não havia.

**Pendências:** **nenhuma.** Nenhum achado aguarda decisão do usuário. O único item que permanece **aberto na literatura** — e não no material — é a controvérsia ⚪ da Bacia Chaco-Paranaense, que não bloqueia o gate: a aula agora a apresenta como controvérsia, e a restrição (a) do gate diz o que não cobrar.

**Material derivado a propagar: nenhum.** O módulo não tinha questionário nem baralho quando as correções foram aplicadas — a auditoria rodou antes deles, como manda a cadeia. **Nada a reimportar no Anki**, e nenhum card em revisão a corrigir à mão. Esta era a melhor hora possível para corrigir: o erro não chegou a virar gabarito nem card.

**Manifesto estruturado:** `18-geofisica-america-do-sul-auditoria.json`
