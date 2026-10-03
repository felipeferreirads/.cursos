# Aula 02: Preparação de amostras e métodos analíticos clássicos

**ID:** geologia-avancado-m28-a02
**Módulo:** [[28-analise-instrumental-i-modulo|Módulo 28 — Análise instrumental I]]
**Duração estimada:** ~25 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** entender como uma amostra de rocha amostrada segundo os princípios da Aula 01 é transformada, em laboratório, numa forma que os instrumentos analíticos podem medir, e como se controla a qualidade dessa transformação.
**Ao final você vai conseguir:** descrever a sequência padrão de britagem, pulverização e homogeneização de uma amostra de rocha; distinguir fusão com fundente de digestão ácida como as duas rotas clássicas de colocar uma rocha em forma analisável, e escolher entre elas conforme o objetivo analítico; e explicar o papel de perda ao fogo, brancos de procedimento e materiais de referência certificados no controle de qualidade.
**Pré-requisito:** Aula 01 (amostragem, representatividade, heterogeneidade de constituição, contaminação).

## Conteúdo

### Da amostra de campo ao pó analítico: a cadeia de redução

A Aula 01 estabeleceu que cada etapa de redução de massa é, ela mesma, uma operação de amostragem. Na prática de laboratório, essa cadeia segue uma sequência relativamente padronizada, descrita em detalhe em Potts (1987), *A Handbook of Silicate Rock Analysis* (Blackie/Chapman & Hall):

1. **Britagem primária** (*crushing*): o bloco de rocha de campo (tipicamente 1–5 kg) é reduzido em um britador de mandíbulas a fragmentos de poucos milímetros a centímetros. Nesta etapa, minerais macios (micas, argilas) e minerais duros (quartzo, granada) se comportam de forma diferente sob impacto, o que pode introduzir uma segregação mineral sistemática se a etapa seguinte de homogeneização for malfeita.
2. **Quarteamento** (*splitting*): o material britado é reduzido a uma alíquota menor por um quarteador (*riffle splitter*) ou por quarteamento manual em cruz, nunca por "pegar uma colherada" — método que, como visto na Aula 01, introduz viés de segregação granulométrica.
3. **Pulverização** (*pulverizing/milling*): a alíquota é moída até um pó fino, tipicamente com 85–95% passando em peneira de 200 mesh (aproximadamente 75 μm) para a maioria das rotinas geoquímicas de rocha total — granulação fina o suficiente para que a heterogeneidade de constituição discutida na Aula 01 deixe de ser um problema relevante na massa de alíquota usada para fusão ou digestão (tipicamente 0,1 a 1 g).
4. **Homogeneização** e **armazenamento**: o pó é misturado (rolado, tombado) antes de ser subdividido em alíquotas para os diferentes procedimentos analíticos.

O material do equipamento em cada etapa é escolhido em função do elemento de interesse, exatamente como discutido na Aula 01 — moinhos de ágata para elementos-traço sensíveis à contaminação por metais, moinhos de aço quando a rotina é só de elementos maiores e o custo e o desgaste do equipamento pesam mais.

### Duas rotas para colocar uma rocha em solução (ou em vidro): fusão e digestão ácida

Um instrumento analítico — seja um espectrômetro de absorção atômica, um ICP ou um espectrômetro de fluorescência de raios X de laboratório — não "lê" um pedaço de rocha diretamente na forma de pó bruto na maioria dos casos (a exceção parcial é a fluorescência de raios X sobre pastilha prensada, comentada na Aula 05). É preciso primeiro decompor a estrutura cristalina da rocha. Há duas famílias clássicas de método, com lógicas e trade-offs bem diferentes. São "clássicas" no sentido de que vêm da análise de rochas por via úmida, anterior aos instrumentos; os procedimentos gravimétricos e volumétricos dessa tradição, que os instrumentos das próximas aulas substituíram na rotina, estão sistematizados em Jeffery & Hutchison (1981) e não são detalhados aqui:

**Fusão com fundente (*flux fusion*).** O pó de rocha é misturado com um fundente — na rotina moderna de rocha total, tipicamente uma mistura de tetraborato de lítio (Li₂B₄O₇) e metaborato de lítio (LiBO₂), muitas vezes numa proporção próxima de 50:50 — numa proporção de fundente para amostra da ordem de 5:1 a 10:1, e aquecido a temperaturas da ordem de 1000–1100 °C num cadinho de platina até fundir completamente. O fundido resultante pode ser vertido e resfriado como um **disco de vidro homogêneo** (a "pérola" ou *bead* usada diretamente na fluorescência de raios X, Aula 05) ou dissolvido em ácido diluído para gerar uma solução usada em ICP. A grande vantagem da fusão é que ela **dissolve minerais refratários que resistem à digestão ácida** mesmo em condições agressivas — o zircão é o exemplo clássico — o que a torna o método de escolha quando a exatidão para elementos maiores e a recuperação total da amostra são prioridade. Não é, porém, universal: a **cromita** se dissolve devagar e de forma incongruente no borato de lítio, e materiais ricos em cromita exigem diluição muito maior, temperatura mais alta ou aditivos oxidantes. A desvantagem é a diluição relativamente alta imposta pela proporção fundente:amostra, que eleva os limites de detecção para elementos-traço em concentração baixa, e o custo de reagente e energia mais alto.

**Digestão ácida** (*acid digestion*). O pó de rocha é atacado por uma combinação de ácidos fortes — tipicamente HF (que ataca a rede de silicato dissolvendo o Si como SiF₄ volátil ou como fluorsilicatos), combinado com HNO₃, HClO₄ ou HCl, muitas vezes em vaso fechado sob pressão e temperatura elevadas (digestão em bomba ou em forno de micro-ondas) para acelerar a reação e reter elementos voláteis. A vantagem central é a **diluição muito menor** que a fusão, o que favorece limites de detecção baixos para elementos-traço — por isso é a rota dominante para preparar soluções destinadas a ICP-MS (Aula 04), onde a sensibilidade a traços é o ponto forte do instrumento. A desvantagem clássica, bem documentada desde Jeffery & Hutchison (1981), *Chemical Methods of Rock Analysis*, 3ª ed., Pergamon Press, é a **dissolução incompleta de minerais resistatos**: zircão, cromita, esfeno e alguns óxidos e sulfetos podem resistir mesmo à digestão com HF em bomba fechada, deixando um resíduo insolúvel que carrega embutidos Zr, Hf, Cr e elementos terras-raras pesados hospedados nesses minerais — um viés sistemático por subestimação, não um erro aleatório, que pode passar despercebido se o laboratório não reportar a recuperação em material de referência com esses minerais.

A escolha entre as duas rotas, portanto, não é uma questão de qual é "melhor" em abstrato, mas de qual viés o objetivo analítico tolera menos: um estudo petrogenético que depende de razões de elementos terras-raras pesados ou de Zr/Hf tende a preferir fusão total (ou digestão ácida validada especificamente para reter esses elementos), enquanto um levantamento de exploração que precisa de limites de detecção baixos para muitos elementos-traço ao mesmo tempo tende a preferir digestão ácida, aceitando o risco de subestimação em minerais resistatos como uma limitação conhecida e documentada.

### Perda ao fogo (LOI): o que ela mede e por que importa

A **perda ao fogo** (*loss on ignition*, LOI) é a diferença de massa de uma alíquota de amostra antes e depois de ser aquecida a uma temperatura padronizada (comumente 900–1000 °C) por um tempo fixo. Ela mede, principalmente, a perda de água estrutural (de minerais hidratados como micas, cloritas, anfibólios e argilas) e de CO₂ (de carbonatos). Um processo age no sentido oposto: a oxidação de Fe²⁺ a Fe³⁺ durante o aquecimento *aumenta* ligeiramente a massa e mascara parte da perda, por isso é por vezes corrigida à parte em rochas ricas em Fe reduzido ou em sulfetos. A LOI é reportada como um "elemento maior" a mais na soma de óxidos de uma análise de rocha total — e seu valor é diagnóstico: uma LOI alta e inesperada num basalto que deveria ser fresco é um sinal de alteração hidrotermal, intemperismo ou presença de carbonato secundário, informação petrogenética por si só, além de ser necessária para fechar a soma de óxidos perto de 100%.

### Controle de qualidade: brancos, réplicas e materiais de referência certificados

A etapa de preparação — fusão ou digestão — é onde a maior parte da contaminação e da perda sistemática discutidas na Aula 01 realmente acontece, e por isso é onde o controle de qualidade precisa ser mais rigoroso. Três instrumentos de controle, comuns a toda a química analítica e formalizados por normas como as recomendações IUPAC de validação de métodos, se aplicam diretamente aqui:

- **Branco de procedimento** (*procedural blank*): uma "amostra" que passa por toda a cadeia de preparação — fundente, ácidos, cadinho, todos os passos — sem nenhuma rocha real. Ele mede a contaminação introduzida pelos próprios reagentes e pelo processo, e seu valor é subtraído (ou, minimamente, reportado) para saber que fração de um sinal medido vem do processo e não da amostra.
- **Réplicas de preparação**: a mesma amostra, processada duas ou mais vezes desde o pó até o resultado final, avalia a precisão (reprodutibilidade) de toda a cadeia — não só a precisão instrumental, que é medida por reinjeção da mesma solução final (a Aula 06 trata a diferença entre precisão instrumental e precisão de método com mais rigor estatístico).
- **Material de referência certificado (MRC)**: uma amostra homogeneizada, com composição estabelecida por consenso entre múltiplos laboratórios de referência e distribuída por um órgão como o USGS (nos EUA, materiais como BHVO-2, um basalto havaiano, ou BCR-2, um basalto do rio Columbia) ou o GSJ (Serviço Geológico do Japão, série JB e JG). A rigor, os materiais geoquímicos do USGS trazem valores de referência compilados de estudos multilaboratoriais, e o próprio USGS declara não ter publicado para eles uma caracterização metrologicamente rastreável — "certificado" no sentido estrito é outra categoria. Para o uso descrito aqui, a lógica é a mesma, e é por isso que o texto fala daqui em diante em **valor de referência**, que cobre os dois casos. Processar um material de referência junto com as amostras desconhecidas, do início ao fim da cadeia de preparação, e comparar o resultado obtido com o valor de referência é o teste mais direto de **exatidão** (não só precisão) de todo o processo — inclusive da etapa de preparação, e não só da leitura instrumental.

## Exemplo trabalhado: escolhendo o método de preparação para dois objetivos analíticos

**Situação.** Um laboratório recebe duas solicitações: (a) uma série de andesitos de um arco vulcânico para um estudo petrogenético que depende criticamente de razões de elementos terras-raras pesados (Yb, Lu) e de Zr/Hf, usadas para discutir a presença de granada residual na fonte do magma; e (b) uma bateria de 200 amostras de sedimento de corrente de um programa de exploração regional, precisando de baixos limites de detecção para uma lista ampla de elementos-traço (Cu, Pb, Zn, As, Sb, Mo, Au) a custo controlado por amostra.

**Raciocínio.** Para o caso (a), a presença de zircão residual (que concentra Zr, Hf e pode reter parte dos terras-raras pesados) torna a digestão ácida arriscada: se o zircão não dissolver completamente, os resultados de Zr, Hf e HREE ficarão sistematicamente subestimados, exatamente o tipo de viés que comprometeria a conclusão sobre granada residual. A fusão total com tetraborato/metaborato de lítio, apesar do custo maior e da diluição mais alta, é a escolha defensável — porque garante que todo o Zr do zircão entre na solução final.

Para o caso (b), o volume de amostras (200) e a prioridade de custo e de limite de detecção baixo para uma lista ampla de elementos-traço favorecem a digestão ácida (frequentemente uma digestão parcial ou "quase-total" com água régia ou uma combinação multiácida, mais barata que HF em bomba fechada) seguida de leitura em ICP-MS (Aula 04) — aceitando que a recuperação de elementos hospedados em minerais resistatos pode ser incompleta, uma limitação tolerável para um levantamento de triagem regional cujo objetivo é identificar anomalias relativas, não obter a composição total exata de cada amostra.

**Conclusão prática.** A escolha do método de preparação é uma decisão analítica tão importante quanto a escolha do instrumento — e precisa ser tomada em função do objetivo geológico da análise, não por hábito de laboratório.

## Recap relâmpago

- A cadeia de preparação (britagem → quarteamento → pulverização → homogeneização) reduz progressivamente a massa da amostra e precisa seguir a granulação exigida pela rotina analítica (tipicamente ~200 mesh / ~75 μm para rocha total) sem introduzir segregação nem contaminação.
- Fusão com fundente de lítio (tetraborato/metaborato) dissolve minerais refratários que resistem à digestão ácida, como o zircão (a cromita é a exceção notória, exige condições especiais), e é o método de escolha quando exatidão em elementos maiores e em elementos hospedados em minerais resistatos é prioridade; a desvantagem é a diluição alta, que piora limites de detecção para traços.
- Digestão ácida (HF + outros ácidos, em bomba ou micro-ondas) dá diluição baixa e favorece limites de detecção para elementos-traço, mas pode deixar minerais resistatos (zircão, cromita, esfeno) parcialmente indissolvidos, subestimando sistematicamente Zr, Hf, Cr e terras-raras pesados hospedados neles.
- A perda ao fogo (LOI) mede sobretudo água estrutural e CO₂ liberados a alta temperatura, entra na soma de óxidos de uma análise de rocha total, e sinaliza alteração ou intemperismo quando anormalmente alta.
- Branco de procedimento, réplicas de preparação e material de referência (MRC em sentido estrito, ou materiais com valores de referência multilaboratoriais, como o BHVO-2 do USGS) processados junto com as amostras são os três instrumentos padrão de controle de qualidade de toda a cadeia de preparação — e a comparação com o valor de referência é o teste direto de exatidão, não só de precisão.

## Próxima aula

[[28-analise-instrumental-i-aula-03-espectrometria-atomica-absorcao-emissao|Aula 03 — Espectrometria atômica: princípios de absorção e de emissão]]: como a solução preparada nesta aula é finalmente lida por um instrumento, começando pelos princípios físicos comuns a toda espectrometria atômica antes de entrar em ICP e em XRF nas Aulas 04 e 05.

## Fontes

- Potts, P. J. (1987), *A Handbook of Silicate Rock Analysis*, Blackie & Son (EUA: Chapman & Hall). VERIFICADO por busca nesta redação (2026-09-23): editora, ano e extensão confirmados (Cambridge Core, American Mineralogist).
- Jeffery, P. G. & Hutchison, D. (1981), *Chemical Methods of Rock Analysis*, 3ª ed., Pergamon Press, Oxford. VERIFICADO por busca nesta redação (2026-09-23): título, autores, edição e editora confirmados (Amazon, Google Books, resenha em *Mineralogical Magazine*).
- XRF Scientific (recurso técnico industrial, não acadêmico), páginas sobre fusão com tetraborato/metaborato de lítio para preparação de pérolas de XRF. VERIFICADO por busca nesta redação (2026-09-23): confirma a mistura 50:50 de tetraborato e metaborato de lítio como fluxo de propósito geral para amostras geológicas e a granulação de pó recomendada (≤100 μm) antes da fusão.
- Currie, L. A. (1995), "Nomenclature in Evaluation of Analytical Methods including Detection and Quantification Capabilities (IUPAC Recommendations 1995)", *Pure and Applied Chemistry*, 67(10), 1699-1723, doi:10.1351/pac199567101699 — base normativa para os conceitos de branco de procedimento e validação de método retomados nesta aula e detalhados na Aula 06. VERIFICADO por busca nesta redação (2026-09-23).
- Merkle, R. K. W., Loubser, M. & Gräser, P. P. H. (2004), "Incongruent dissolution of chromite in lithium tetraborate flux", *X-Ray Spectrometry*, 33, 222-224, doi:10.1002/xrs.759 — limite da fusão com borato de lítio para a cromita. Acrescentada pela auditoria (2026-09-23).
- USGS, *BHVO-2 Reference Material Information Sheet* (rev. junho 2022) e *BCR-2 Information Sheet* — origem dos materiais (BHVO-2: lava de 1919 do Kilauea; BCR-2: Basalto do Rio Columbia, pedreira Bridal Veil Flow, Oregon, coletado em 1996) e estatuto dos valores. Acrescentada pela auditoria (2026-09-23).

<!--
nivel: avancado
palavras_corpo: 2111
recontagem_didatica: "Recontado por script na revisao didatica de 2026-09-23, depois da ultima edicao, a ~84 palavras/min (achado DID-M28-DURACOES-DECLARADAS-006). Valor declarado antes: 1780."
palavras_corpo_metodo: "tokens separados por espaco entre '## Conteudo' e '## Fontes', incluindo tabelas, seguindo a convencao do modulo 26/27."
duracao_estimada_min: 25

mapa_objetivo_secao:
  geologia-avancado-m28-oa01: "Da amostra de campo ao pó analítico: a cadeia de redução" + "Controle de qualidade: brancos, réplicas e materiais de referência certificados"
  geologia-avancado-m28-oa03: "Duas rotas para colocar uma rocha em solução (ou em vidro): fusão e digestão ácida" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: ANINST-M28-A02-CADEIA-PREPARACAO-001
    claim: "A cadeia padrao de preparacao de rocha total segue britagem primaria, quarteamento, pulverizacao ate granulacao tipica de ~200 mesh (~75 micrometros) e homogeneizacao, conforme descrito em Potts (1987)."
    risk: fato
    source: "Potts, P.J. (1987), A Handbook of Silicate Rock Analysis, Blackie/Chapman & Hall - referencia padrao de preparacao de amostra em geoquimica de rocha total. Granulacao de ~200 mesh e convencao amplamente citada na pratica de laboratorios comerciais de geoquimica (ALS, SGS, Bureau Veritas), nao verificada por norma unica especifica nesta redacao."
  - claim_id: ANINST-M28-A02-FUSAO-FUNDENTE-LI-002
    claim: "A fusao com fundente de tetraborato/metaborato de litio (tipicamente proporcao proxima de 50:50, fundente:amostra da ordem de 5:1 a 10:1, temperatura ~1000-1100 C) dissolve minerais refrattarios resistentes a digestao acida, como o zircao (a cromita e excecao notoria: dissolucao lenta e incongruente, exige condicoes especiais - correcao da auditoria 2026-09-23), sendo usada tanto para gerar perolas de vidro para XRF quanto solucoes para ICP apos dissolucao acida do fundido."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-23): fontes tecnicas (XRF Scientific, VWR) confirmam a mistura 50:50 de tetraborato e metaborato de litio como fluxo de proposito geral para amostras geologicas neutras e sua capacidade de dissolver oxidos refrattarios. Proporcao fundente:amostra e faixa de temperatura sao valores tipicos de pratica de laboratorio, nao verificados contra uma unica norma citavel."
  - claim_id: ANINST-M28-A02-DIGESTAO-ACIDA-RESISTATOS-003
    claim: "A digestao acida (HF combinado com outros acidos, em bomba fechada ou micro-ondas) pode deixar minerais resistatos como zircao, cromita e esfeno parcialmente indissolvidos, subestimando sistematicamente Zr, Hf, Cr e elementos terras-raras pesados hospedados nesses minerais - limitacao documentada desde Jeffery & Hutchison (1981)."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-23) quanto a existencia, autoria, edicao e editora de Jeffery & Hutchison (1981), Chemical Methods of Rock Analysis, 3a ed., Pergamon Press. A limitacao especifica de dissolucao incompleta de zircao/cromita por HF e um principio bem estabelecido na literatura de geoquimica analitica (citado tambem em Potts 1987), mas a atribuicao exata dessa formulacao a paginas especificas de Jeffery & Hutchison nao foi conferida linha a linha nesta redacao."
  - claim_id: ANINST-M28-A02-LOI-DEFINICAO-004
    claim: "A perda ao fogo (LOI) mede a diferenca de massa de uma alicota aquecida a temperatura padronizada (comumente 900-1000 C), refletindo principalmente perda de agua estrutural e de CO2 de carbonatos, e em rochas ricas em Fe reduzido pode ser parcialmente compensada por ganho de massa por oxidacao de Fe2+ a Fe3+."
    risk: fato
    source: "Definicao padrao de LOI em geoquimica de rocha total, consolidada em manuais de preparacao de amostra (Potts 1987) e em relatorios de laboratorios comerciais de geoquimica; a faixa de temperatura 900-1000 C e uma convencao amplamente usada mas nao unica (alguns protocolos usam 950 C fixo, outros ate 1050 C) - nao verificada contra uma norma internacional unica nesta redacao."
  - claim_id: ANINST-M28-A02-MRC-EXEMPLOS-005
    claim: "Materiais de referencia como BHVO-2 (basalto havaiano, USGS) e BCR-2 (basalto do rio Columbia, USGS - 'basalto colunar' corrigido pela auditoria 2026-09-23; o USGS declara nao ter caracterizacao metrologicamente rastreavel desses materiais) e a serie JB/JG do GSJ (Servico Geologico do Japao) sao usados para validar a exatidao de toda a cadeia analitica, incluindo a etapa de preparacao."
    risk: fato
    source: "BHVO-2, BCR-2 (USGS) e a serie JB/JG (GSJ) sao materiais de referencia geoquimica amplamente citados e usados na literatura internacional de geoquimica de rocha total; nao verificados numero de lote ou valores certificados especificos nesta redacao, apenas a existencia e a instituicao emissora, que sao de conhecimento consolidado no campo."
  - claim_id: ANINST-M28-A02-EXEMPLO-ANDESITO-SEDIMENTO-006
    claim: "Exemplo pedagogico hipotetico comparando a escolha de fusao total (para um estudo petrogenetico de arco vulcanico dependente de Zr/Hf e HREE) versus digestao acida (para um levantamento de exploracao regional de 200 amostras de sedimento de corrente com foco em custo e limite de deteccao para elementos-traco)."
    risk: hipotetico
    source: "Exemplo pedagogico construido especificamente para esta aula; nao corresponde a um estudo publicado especifico. A logica de escolha de metodo segue diretamente os principios de fusao vs. digestao acida discutidos e verificados nas fontes desta aula."

auditoria:
  data: 2026-09-23
  modo: audit-and-fix
  relatorio: 28-analise-instrumental-i-auditoria.md
  achados_nesta_aula:
    - "3 (laranja) ANINST-M28-A02-FUSAO-FUNDENTE-LI-002 - cromita como excecao a dissolucao por fusao - corrigido (corpo e recap)"
    - "4 (laranja) ANINST-M28-A02-MRC-EXEMPLOS-005 - BCR-2 = basalto do rio Columbia; estatuto dos valores do USGS - corrigido"
  verificados_sem_achado: "001 (cadeia de preparacao, ~85% < 75 um), 003 (resistatos na digestao acida; Jeffery & Hutchison 1981 conferido), 004 (LOI e oxidacao de Fe2+), 006 (exemplo andesito x sedimento)"

revisao_didatica:
  data: 2026-09-23
  modo: review-and-fix
  relatorio: 28-analise-instrumental-i-revisao-didatica.md
  achados_nesta_aula:
    - "DID-M28-A02-METODOS-CLASSICOS-TITULO-008 (amarelo) - frase de escopo: 'classicas' = vindas da analise por via umida; gravimetria e volumetria remetidas a Jeffery & Hutchison (1981), ja citado e conferido, sem detalhar"
    - "DID-M28-A02-WDXRF-ANTES-DE-DEFINIDO-009 (amarelo) - 'de comprimento de onda dispersivo' trocado por 'de laboratorio' (WDXRF so e definido na Aula 05)"
    - "DID-M28-A02-LOI-OXIDACAO-AMBIGUA-010 (amarelo) - frase da LOI reescrita: a oxidacao de Fe2+ age no sentido oposto (ganho de massa), nao e 'medida' pela LOI"
    - "DID-M28-A02-MRC-VALOR-CERTIFICADO-011 (amarelo) - apos a ressalva da auditoria, o texto e o recap passam a falar em 'valor de referencia'; recap nao chama mais o BHVO-2 de MRC"
    - "DID-M28-REFERENCIAS-CRUZADAS-007 (amarelo) - precisao de metodo e Currie remetem a Aula 06"
-->
