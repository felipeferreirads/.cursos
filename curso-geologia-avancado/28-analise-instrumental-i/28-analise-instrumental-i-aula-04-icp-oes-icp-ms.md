# Aula 04: Plasma de indução acoplada — ICP-OES e ICP-MS

**ID:** geologia-avancado-m28-a04
**Módulo:** [[28-analise-instrumental-i-modulo|Módulo 28 — Análise instrumental I]]
**Duração estimada:** ~28 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** entender como o plasma de argônio substitui a chama ou o forno de grafite como fonte de atomização e excitação, e como essa mesma fonte alimenta duas técnicas de detecção distintas — emissão óptica (ICP-OES) e espectrometria de massa (ICP-MS) — cada uma com seu regime de aplicação.
**Ao final você vai conseguir:** descrever como um plasma de argônio é gerado e por que sua temperatura muito mais alta que uma chama resolve limitações da AAS; distinguir o que ICP-OES e ICP-MS efetivamente medem e por que ICP-MS chega a limites de detecção muito mais baixos; reconhecer a interferência espectral típica de ICP-OES e as interferências isobáricas e poliatômicas típicas de ICP-MS, e como controlá-las; e explicar como uma curva de calibração transforma sinal em concentração.
**Pré-requisito:** Aula 03 (princípios de absorção e emissão atômica, interferências químicas e de ionização) — o plasma retoma a mesma física de transição eletrônica, aplicada a uma fonte de excitação muito mais energética.

## Conteúdo

### O plasma de argônio: uma fonte de excitação de outra ordem de grandeza

A chama usada em AAS (Aula 03) atinge temperaturas da ordem de 2000–2800 °C — suficiente para atomizar a maioria dos elementos, mas limitada para elementos que formam ligações muito estáveis ou que precisam de mais energia para excitação eficiente. O **plasma de indução acoplada** (*inductively coupled plasma*, ICP) resolve essa limitação usando um gás ionizado — tipicamente argônio, escolhido por ser quimicamente inerte e ter alto potencial de ionização — sustentado por um campo eletromagnético de radiofrequência, atingindo temperaturas centrais da ordem de 6000 a 10000 K, várias vezes mais quente que qualquer chama química.

O arranjo físico central é a **tocha de plasma** (frequentemente chamada tocha de Fassel, em referência a Velmer Fassel, um dos pesquisadores centrais no desenvolvimento da técnica): três tubos de quartzo concêntricos, com argônio fluindo entre eles em vazões distintas (gás de plasma, gás auxiliar e gás de nebulização, este último carregando a amostra). Uma bobina de indução envolve a tocha e é energizada por um gerador de radiofrequência (tipicamente 27 ou 40 MHz), criando um campo magnético oscilante que acopla energia ao gás e sustenta o plasma continuamente, uma vez iniciado por uma faísca. A amostra líquida, nebulizada em um aerossol fino, é injetada no centro do plasma através do tubo interno, onde é dessolvatada, vaporizada, atomizada e — o que a chama de AAS faz de forma limitada — parcialmente **ionizada**, um passo que a Aula 03 tratava como uma interferência indesejada em AAS e que aqui se torna, paradoxalmente, o próprio princípio de funcionamento de uma das duas técnicas de detecção.

O desenvolvimento do ICP como fonte espectroscópica é atribuído a Greenfield, Jones & Berry (1964), que publicaram "High-Pressure Plasmas as Spectroscopic Emission Sources" na revista *Analyst*, seguidos de perto por Wendt & Fassel (1965), que descreveram de forma independente uma fonte de excitação por plasma de indução acoplada em *Analytical Chemistry* — os dois grupos, trabalhando de forma paralela, estabeleceram as bases da técnica que hoje sustenta tanto ICP-OES quanto ICP-MS.

### ICP-OES: medindo a luz que o próprio plasma emite

A **espectrometria de emissão óptica com plasma de indução acoplada** (*ICP optical emission spectrometry*, ICP-OES, também chamada ICP-AES) mede exatamente o princípio de emissão descrito na Aula 03: átomos e íons excitados pela energia do plasma retornam ao estado fundamental emitindo fótons em comprimentos de onda característicos de cada elemento. A diferença essencial em relação à emissão de chama (uma técnica anterior e mais limitada, não detalhada neste módulo) é que a temperatura muito mais alta do plasma excita eficientemente um número muito maior de elementos simultaneamente, incluindo muitos que a chama mal conseguia atomizar.

Um espectrômetro de ICP-OES capta a luz emitida pelo plasma e a decompõe por comprimento de onda — seja de forma **sequencial**, com um monocromador que varre um comprimento de onda de cada vez (mais lento, mas com maior flexibilidade), seja de forma **simultânea**, com um policromador (como uma rede de difração combinada com um detector de estado sólido, tipo CCD ou CID) que capta dezenas de comprimentos de onda ao mesmo tempo — o arranjo dominante na rotina moderna de geoquímica, porque permite medir uma lista extensa de elementos maiores e traços numa única leitura da mesma solução, muito mais rápido que a análise elemento por elemento típica de AAS.

ICP-OES é a técnica de escolha típica para **elementos maiores** (Si, Al, Fe, Ca, Mg, Na, K, Ti, P, Mn) e para elementos-traço em concentração relativamente alta (dezenas a centenas de ppm), onde sua faixa dinâmica linear ampla e sua robustez frente a matrizes complexas — herdada da temperatura alta do plasma, que reduz interferências químicas em relação à chama — são vantagens diretas. A interferência típica do ICP-OES é de outro tipo: **espectral**. Como o plasma excita muitos elementos ao mesmo tempo, o espectro de uma solução de rocha é rico em linhas, e a linha escolhida para um elemento pode cair sobre a de outro (sobreposição direta, ou sobre a "asa" de uma linha intensa vizinha) ou sobre um fundo elevado. Contorna-se escolhendo uma linha alternativa do mesmo elemento, livre de sobreposição, e medindo o fundo dos dois lados do pico para subtraí-lo.

### ICP-MS: usando o plasma como fonte de íons para um espectrômetro de massa

A **espectrometria de massa com plasma de indução acoplada** (*ICP mass spectrometry*, ICP-MS) usa o mesmo plasma como fonte de ionização, mas em vez de medir a luz emitida, extrai os **íons** gerados pelo plasma através de uma interface de cones amostradores (*sampler* e *skimmer cone*) para um sistema de vácuo, onde um analisador de massa — mais comumente um **quadrupolo** na rotina de geoquímica, embora instrumentos de **setor magnético de alta resolução** também sejam usados para aplicações que exigem resolver interferências isobáricas finas — separa os íons por razão massa/carga (m/z) antes de um detector contar os íons de cada massa.

A técnica foi descrita pela primeira vez por Houk, Fassel, Flesch, Svec, Gray & Taylor (1980), num trabalho de colaboração entre o grupo do Ames Laboratory na Iowa State University (EUA) e Alan Gray, na University of Surrey (Reino Unido), publicado em *Analytical Chemistry* sob o título "Inductively coupled argon plasma as an ion source for mass spectrometric determination of trace elements" — o mesmo Fassel que, quinze anos antes, havia contribuído para desenvolver o ICP como fonte de emissão óptica.

A vantagem central de ICP-MS sobre ICP-OES é a **sensibilidade**: como cada íon é contado individualmente pelo detector, em vez de medir uma intensidade de luz agregada de uma população de átomos excitados, ICP-MS atinge limites de detecção tipicamente na faixa de partes por trilhão (ppt) a partes por bilhão (ppb) para a maioria dos elementos — várias ordens de grandeza abaixo de ICP-OES —, o que a torna a técnica dominante para elementos-traço em baixa concentração: terras-raras, elementos do grupo da platina, e a maioria dos elementos-traço usados em geoquímica de petrogênese e de proveniência.

### Interferências em ICP-MS: isobáricas e poliatômicas

A sensibilidade extrema de ICP-MS vem acompanhada de um conjunto de interferências específicas, centrais para qualquer geólogo interpretar um resultado de ICP-MS com espírito crítico:

- **Interferências isobáricas**: dois isótopos de elementos diferentes com a mesma massa nominal (por exemplo, ⁸⁷Rb e ⁸⁷Sr) chegam ao detector na mesma posição de m/z, somando seus sinais. Corrigidas matematicamente usando a razão isotópica conhecida do isótopo interferente medido em outra massa (por exemplo, medir ⁸⁵Rb, cuja razão ⁸⁷Rb/⁸⁵Rb é conhecida, para calcular e subtrair a contribuição de ⁸⁷Rb do sinal em massa 87).
- **Interferências poliatômicas** (ou moleculares): combinações de átomos do próprio plasma, do gás argônio, ou de componentes da matriz da amostra (ácidos residuais da digestão, Aula 02) formam íons moleculares com massa nominal igual à de um isótopo de interesse. O exemplo mais citado na literatura é ⁴⁰Ar¹⁶O⁺ (óxido de argônio) interferindo diretamente sobre ⁵⁶Fe⁺, o isótopo mais abundante do ferro — uma interferência particularmente incômoda em geoquímica, dado quão central o Fe é para petrologia ígnea e metamórfica. Controlada por células de colisão/reação (que usam um gás, como hélio ou hidrogênio, para dissociar ou desviar preferencialmente os íons poliatômicos antes que cheguem ao analisador de massa) ou pelo uso de um instrumento de setor magnético de alta resolução, capaz de separar fisicamente ⁵⁶Fe⁺ (massa exata 55,9349) de ⁴⁰Ar¹⁶O⁺ (massa exata ligeiramente diferente), mesmo que ambos tenham massa nominal 56.
- **Efeitos de matriz**: sais dissolvidos em concentração alta podem depositar-se nos cones da interface, degradando a sensibilidade ao longo de uma sequência de análise, ou suprimir/aumentar o sinal por competição de ionização no plasma. Controlados por diluição da amostra e pelo uso de um **padrão interno** — um elemento adicionado em concentração conhecida e constante a todas as amostras e padrões (tipicamente um elemento ausente ou em concentração natural desprezível diante da quantidade adicionada, como In, Rh ou Bi — o basalto de referência BHVO-2, por exemplo, tem ~0,1 ppm de In e ~0,015 ppm de Bi), cuja intensidade medida corrige variações de sensibilidade do instrumento ao longo da análise.

### Do sinal à concentração: identificação e calibração

Nas duas técnicas, a parte **qualitativa** da análise — saber *quais* elementos estão na solução — vem da posição do sinal: o comprimento de onda da linha no ICP-OES, a razão m/z no ICP-MS. A parte **quantitativa** — *quanto* de cada um — não sai pronta do instrumento: exige **calibração**. Mede-se uma série de soluções-padrão de concentração conhecida, preparadas na mesma matriz ácida das amostras, e ajusta-se uma reta de sinal contra concentração, a **curva de calibração**. A inclinação dessa reta é a **sensibilidade** do método para aquele elemento (quanto sinal cada ppm produz), e a concentração de uma amostra desconhecida é lida na reta a partir do seu sinal. O padrão interno entra aqui: adicionado igualmente a padrões e amostras, ele permite trabalhar com a razão entre o sinal do analito e o seu, que compensa as derivas de sensibilidade ao longo da sequência. É o mesmo princípio de calibração que a Aula 03 introduziu com a lei de Beer-Lambert, e a inclinação dessa reta volta na Aula 06 como denominador dos limites de detecção e de quantificação.

### ICP-OES e ICP-MS não competem — se complementam

Um erro comum de quem está aprendendo essas técnicas é pensar em ICP-MS como uma versão "melhor" de ICP-OES em todos os aspectos. Na prática de rotina geoquímica, as duas técnicas são frequentemente usadas **juntas, sobre a mesma solução preparada**: ICP-OES mede os elementos maiores e traços em concentração mais alta, onde sua robustez de matriz e sua faixa dinâmica ampla são vantajosas e onde a sensibilidade extrema de ICP-MS sequer é necessária (e pode até saturar o detector sem diluição adicional); ICP-MS mede os elementos-traço em concentração baixa, onde só ela atinge os limites de detecção exigidos. Um pacote analítico comercial típico de geoquímica de rocha total ("fusão + ICP-OES para maiores, digestão + ICP-MS para traços", ou variantes) reflete exatamente essa divisão de trabalho entre as duas técnicas.

## Exemplo trabalhado: escolhendo entre ICP-OES e ICP-MS para uma suíte de granitoides

**Situação.** Um estudo petrogenético de uma suíte de granitoides precisa de: (a) os dez óxidos maiores para classificação (diagrama TAS, índices de saturação em alumina) e (b) um padrão completo de elementos terras-raras (La a Lu) normalizado a condrito, para discutir a fonte do magma e a presença de fases residuais como granada ou anfibólio.

**Raciocínio.** Para (a), os óxidos maiores estão em concentração de percentual (dezenas de milhares de ppm), bem dentro da faixa dinâmica confortável de ICP-OES, que também é mais barata e mais rápida por amostra para essa finalidade — usar ICP-MS aqui seria desperdiçar a sensibilidade da técnica em elementos que não precisam dela, e arriscar saturar o detector sem diluições adicionais.

Para (b), os elementos terras-raras pesados (Tb a Lu) em granitoides evoluídos frequentemente ocorrem na faixa de frações de ppm a poucos ppm — abaixo ou na borda do limite de detecção confortável de ICP-OES, mas confortavelmente acima do limite de detecção de ICP-MS, que também mede simultaneamente toda a série de terras-raras com uma única leitura rápida. Além disso, o padrão de terras-raras precisa de precisão relativa boa entre elementos adjacentes (para captar a inclinação suave da curva condrito-normalizada e uma eventual anomalia de Eu), o que ICP-MS entrega de forma mais confiável nessa faixa de concentração.

**Conclusão prática.** A escolha não é "qual técnica é melhor", mas qual delas mede bem a faixa de concentração e a precisão relativa que a pergunta geológica exige — e, na prática de laboratório comercial, ambas costumam ser aplicadas à mesma amostra, sobre preparações às vezes distintas (fusão para OES de maiores, digestão para MS de traços, como discutido na Aula 02), compondo um único boletim analítico.

## Recap relâmpago

- O plasma de indução acoplada usa argônio ionizado por um campo de radiofrequência numa tocha de três tubos concêntricos, atingindo 6000–10000 K — muito mais quente que qualquer chama de AAS — o que atomiza e ioniza eficientemente a maioria dos elementos da tabela periódica.
- ICP-OES (Greenfield 1964; Wendt & Fassel 1965) mede a luz emitida por átomos e íons excitados no plasma, com detecção simultânea multielementar por policromador; é a técnica de escolha para elementos maiores e traços em concentração relativamente alta, e sua interferência típica é espectral (sobreposição de linhas e fundo), contornada por linha alternativa e correção de fundo.
- ICP-MS (Houk, Fassel et al., 1980) extrai os íons do plasma para um espectrômetro de massa (tipicamente um quadrupolo), contando íons individualmente por m/z; atinge limites de detecção em ppt-ppb, várias ordens de grandeza abaixo de ICP-OES, sendo a técnica dominante para terras-raras e outros elementos-traço em baixa concentração.
- Interferências isobáricas (mesma massa nominal, elementos diferentes) e poliatômicas (íons moleculares formados no plasma ou na matriz, como ⁴⁰Ar¹⁶O⁺ sobre ⁵⁶Fe⁺) são as limitações centrais de ICP-MS, corrigidas por equações de correção isotópica, células de colisão/reação ou instrumentos de setor magnético de alta resolução; padrão interno corrige variações de sensibilidade do instrumento.
- A identificação (qual elemento) vem do comprimento de onda ou da m/z; a quantificação (quanto) vem de uma curva de calibração com padrões de concentração conhecida, cuja inclinação é a sensibilidade do método.
- ICP-OES e ICP-MS não competem: rotinas modernas de geoquímica de rocha total combinam as duas sobre a mesma suíte de amostras, cada uma cobrindo a faixa de concentração em que é mais robusta e mais sensível.

## Próxima aula

[[28-analise-instrumental-i-aula-05-fluorescencia-de-raios-x|Aula 05 — Fluorescência de raios X: princípios, aparelhagem e aplicações]]: uma técnica com física distinta (interação de raios X com elétrons de camadas internas, não transições eletrônicas de valência), que mede a amostra sólida e por isso depende tanto da preparação da Aula 02. A Aula 06 fecha o módulo com o tratamento estatístico de erro, limite de detecção e limite de quantificação, que vale para todas as técnicas vistas até aqui.

## Fontes

- Greenfield, S., Jones, I. L. & Berry, C. T. (1964), "High-Pressure Plasmas as Spectroscopic Emission Sources", *The Analyst*, 89, 713-720. VERIFICADO por busca nesta redação (2026-09-23): título, autores, periódico e paginação confirmados por múltiplas fontes de história da técnica.
- Wendt, R. H. & Fassel, V. A. (1965), "Induction-Coupled Plasma Spectrometric Excitation Source", *Analytical Chemistry*, 37, 920-922. VERIFICADO por busca nesta redação (2026-09-23): título, autores, periódico e paginação confirmados.
- Houk, R. S., Fassel, V. A., Flesch, G. D., Svec, H. J., Gray, A. L. & Taylor, C. E. (1980), "Inductively Coupled Argon Plasma as an Ion Source for Mass Spectrometric Determination of Trace Elements", *Analytical Chemistry*, 52(14), 2283-2289. VERIFICADO por busca nesta redação (2026-09-23): título, autores, periódico, volume e paginação confirmados (The Analytical Scientist, Wikipedia, OSTI).
- Jarvis, K. E., Gray, A. L. & Houk, R. S. (1992), *Handbook of Inductively Coupled Plasma Mass Spectrometry*, Blackie/Chapman & Hall, Nova York. VERIFICADO por busca nesta redação (2026-09-23): autores, editora, ano e 380 páginas confirmados (WorldCat).
- Thompson, M. & Walsh, J. N. (1989), *Handbook of Inductively Coupled Plasma Spectrometry*, 2ª ed., Blackie (1ª ed. 1983; 2ª ed. reimpressa pela Springer) — referência padrão de instrumentação ICP-OES aplicada a geoquímica, com um capítulo sobre ICP-MS (de G. E. M. Hall) na 2ª edição. Edições conferidas pela auditoria (2026-09-23); não há edição de 2003 deste livro.
- USGS, *BHVO-2 Reference Material Information Sheet* (rev. junho 2022), Tabela 2 — In 0,117 mg/kg e Bi 0,0148 mg/kg no BHVO-2. Acrescentada pela auditoria (2026-09-23).
- Inorganic Ventures, *ICP Operations Guide*, "Spectral Interference: Types, Avoidance and Correction" — tipos de interferência espectral em ICP-OES (sobreposição direta, de asa, deslocamento de fundo) e contorno por linha alternativa e correção de fundo nos dois lados do pico. Acrescentada pela revisão didática (2026-09-23), consultada nessa data.

<!--
nivel: avancado
palavras_corpo: 2326
recontagem_didatica: "Recontado por script na revisao didatica de 2026-09-23, depois da ultima edicao, a ~84 palavras/min (achado DID-M28-DURACOES-DECLARADAS-006). Valor declarado antes: 1920."
palavras_corpo_metodo: "tokens separados por espaco entre '## Conteudo' e '## Fontes', incluindo tabelas, seguindo a convencao do modulo 26/27."
duracao_estimada_min: 28

mapa_objetivo_secao:
  geologia-avancado-m28-oa02: "O plasma de argônio: uma fonte de excitação de outra ordem de grandeza" + "ICP-OES: medindo a luz que o próprio plasma emite" + "ICP-MS: usando o plasma como fonte de íons para um espectrômetro de massa" + "Interferências em ICP-MS: isobáricas e poliatômicas"
  geologia-avancado-m28-oa03: "ICP-OES e ICP-MS não competem — se complementam" + "Exemplo trabalhado"
  geologia-avancado-m28-oa04: "Do sinal à concentração: identificação e calibração" (curva de calibração e sensibilidade, base do cálculo de LOD/LOQ na Aula 06)

alegacoes_auditaveis:
  - claim_id: ANINST-M28-A04-HISTORIA-ICP-OES-001
    claim: "O ICP como fonte de emissao optica foi desenvolvido por Greenfield, Jones & Berry (1964), 'High-Pressure Plasmas as Spectroscopic Emission Sources', The Analyst 89, 713-720, seguido de perto por Wendt & Fassel (1965), 'Induction-Coupled Plasma Spectrometric Excitation Source', Analytical Chemistry 37, 920-922."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-23): ambas as citacoes confirmadas por multiplas fontes (ScienceDirect, Wiley, Wikipedia 'Inductively coupled plasma atomic emission spectroscopy')."
  - claim_id: ANINST-M28-A04-HISTORIA-ICP-MS-002
    claim: "O ICP-MS foi descrito pela primeira vez por Houk, Fassel, Flesch, Svec, Gray & Taylor (1980), 'Inductively coupled argon plasma as an ion source for mass spectrometric determination of trace elements', Analytical Chemistry 52(14), 2283-2289, fruto de colaboracao entre o Ames Laboratory (Iowa State University) e Alan Gray (University of Surrey, Reino Unido)."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-23): citacao completa, autores e afiliacoes confirmados por multiplas fontes (The Analytical Scientist, OSTI, Wikipedia 'Inductively coupled plasma mass spectrometry')."
  - claim_id: ANINST-M28-A04-TEMPERATURA-PLASMA-003
    claim: "O plasma de argonio de um ICP atinge temperaturas centrais da ordem de 6000 a 10000 K, sustentado por um campo eletromagnetico de radiofrequencia tipicamente de 27 ou 40 MHz, numa tocha de tres tubos de quartzo concentricos (tocha de Fassel)."
    risk: fato
    source: "Valores de temperatura e frequencia de radiofrequencia sao conhecimento consolidado e amplamente citado em manuais de instrumentacao ICP (Thompson & Walsh; Jarvis, Gray & Houk 1992); nao verificados por busca especifica nesta redacao, faixa citada e ampla o suficiente para cobrir variacao entre fabricantes e configuracoes."
  - claim_id: ANINST-M28-A04-LOD-ICP-MS-VS-OES-004
    claim: "ICP-MS atinge limites de deteccao tipicamente na faixa de partes por trilhao (ppt) a partes por bilhao (ppb) para a maioria dos elementos, varias ordens de grandeza abaixo dos limites de deteccao tipicos de ICP-OES."
    risk: fato
    source: "Comparacao padrao entre as duas tecnicas, amplamente documentada na literatura de quimica analitica instrumental (Jarvis, Gray & Houk 1992; Thompson & Walsh); ordens de grandeza exatas variam por elemento e por instrumento, nao verificadas contra uma tabela numerica especifica nesta redacao."
  - claim_id: ANINST-M28-A04-INTERFERENCIA-ArO-Fe-005
    claim: "A interferencia poliatomica de oxido de argonio (40Ar16O+) sobre 56Fe+ (isotopo mais abundante do ferro) e um dos exemplos mais citados de interferencia poliatomica em ICP-MS, controlada por celulas de colisao/reacao (He ou H2) ou por instrumentos de setor magnetico de alta resolucao."
    risk: fato
    source: "Interferencia amplamente documentada e citada como exemplo didatico canonico na literatura de ICP-MS (Jarvis, Gray & Houk 1992 e literatura subsequente sobre celulas de colisao/reacao); nao verificada por busca especifica de valor de massa exata nesta redacao, mas o fenomeno em si e consenso solido do campo."
  - claim_id: ANINST-M28-A04-PADRAO-INTERNO-006
    claim: "O uso de um padrao interno (elemento ausente ou em concentracao natural desprezivel diante da quantidade adicionada, como In, Rh ou Bi - 'ausente' corrigido pela auditoria 2026-09-23, achado 8; BHVO-2 tem In ~0,117 e Bi ~0,015 mg/kg -, adicionado em concentracao constante) corrige variacoes de sensibilidade do instrumento de ICP-MS ao longo de uma sequencia analitica, incluindo efeitos de deposicao salina nos cones da interface."
    risk: fato
    source: "Pratica padrao de controle de qualidade em ICP-MS, consolidada em manuais de instrumentacao (Jarvis, Gray & Houk 1992; Thompson & Walsh) e em protocolos de laboratorios comerciais de geoquimica; elementos especificos citados (In, Rh, Bi) sao exemplos tipicos, nao uma lista exaustiva ou normativa."
  - claim_id: ANINST-M28-A04-EXEMPLO-GRANITOIDES-007
    claim: "Exemplo pedagogico hipotetico de escolha entre ICP-OES (para oxidos maiores de uma suite de granitoides) e ICP-MS (para o padrao completo de elementos terras-raras, incluindo pesados em baixa concentracao) na mesma suite de amostras."
    risk: hipotetico
    source: "Exemplo pedagogico construido especificamente para esta aula; a logica de faixa de concentracao e sensibilidade relativa das duas tecnicas segue diretamente os principios verificados nesta aula, mas os valores numericos de concentracao nao correspondem a uma suite publicada especifica."
  - claim_id: ANINST-M28-A04-THOMPSON-WALSH-BIBLIO-008
    claim: "Thompson & Walsh, Handbook of Inductively Coupled Plasma Spectrometry: 1a ed. Blackie 1983; 2a ed. Blackie 1989 (reimpressa pela Springer), com capitulo de ICP-MS de G. E. M. Hall."
    risk: fato
    source: "Criado pela auditoria de 2026-09-23 (achado 9, amarelo). Open Library (edicoes 1983 e 1989); Springer doi:10.1007/978-1-4613-0697-9; resenha em Mineralogical Magazine (1983). A citacao '1989/2003, Blackie/Springer' da redacao nao tinha edicao de 2003 localizavel."
  - claim_id: ANINST-M28-A04-INTERFERENCIA-ESPECTRAL-OES-009
    claim: "A interferencia tipica do ICP-OES e espectral: o plasma excita muitos elementos ao mesmo tempo, o espectro e rico em linhas, e a linha do analito pode sofrer sobreposicao direta, sobreposicao pela asa de uma linha intensa vizinha ou fundo elevado; contorna-se escolhendo uma linha alternativa do mesmo elemento livre de sobreposicao e medindo o fundo dos dois lados do pico para subtrai-lo."
    risk: fato
    source: "Criado pela revisao didatica de 2026-09-23 (achado DID-M28-OA02-INTERFERENCIA-OES-AUSENTE-003) e VERIFICADO na mesma data: Inorganic Ventures, ICP Operations Guide, 'Spectral Interference: Types, Avoidance and Correction' (tipos: direct overlap, wing overlap, background shift, stray light; linha alternativa e correcao de fundo por pontos dos dois lados do pico); ScienceDirect Topics 'Spectral overlap' (linha alternativa suficientemente sensivel e livre de interferencia quando a resolucao nao basta). Nivel: base de referencia (fabricante de padroes) + enciclopedia. Proxima auditoria deve reconferir."
  - claim_id: ANINST-M28-A04-CALIBRACAO-QUALI-QUANTI-010
    claim: "Em ICP-OES e ICP-MS a identificacao (qualitativa) vem do comprimento de onda ou da m/z; a quantificacao exige curva de calibracao com solucoes-padrao de concentracao conhecida preparadas na mesma matriz acida das amostras; a inclinacao da reta e a sensibilidade; o padrao interno, adicionado igualmente a padroes e amostras, permite trabalhar com a razao analito/padrao interno, que compensa derivas de sensibilidade."
    risk: fato
    source: "Criado pela revisao didatica de 2026-09-23 (achado DID-M28-A04-CALIBRACAO-NAO-ENSINADA-002). Conteudo DEFINICIONAL de quimica analitica instrumental, sem numero nem atribuicao: calibracao externa e padrao interno como ja descritos nesta aula (claim 006) e na Aula 03 (lei de Beer-Lambert); LOD = 3 sigma/m com m = inclinacao da curva, ja auditado na Aula 06 (claim A05-005). Referencias padrao: Skoog, Holler & Crouch (Principles of Instrumental Analysis, 7a ed.) e Thompson & Walsh (1989). Proxima auditoria deve reconferir."

auditoria:
  data: 2026-09-23
  modo: audit-and-fix
  relatorio: 28-analise-instrumental-i-auditoria.md
  achados_nesta_aula:
    - "8 (laranja) ANINST-M28-A04-PADRAO-INTERNO-006 - padrao interno 'ausente na amostra' -> ausente ou desprezivel - corrigido"
    - "9 (amarelo) ANINST-M28-A04-THOMPSON-WALSH-BIBLIO-008 (novo) - metadado de Thompson & Walsh - corrigido"
  verificados_sem_achado: "001 (Greenfield et al. 1964, Analyst 89(1064), 713; Wendt & Fassel 1965, Anal. Chem. 37(7), 920-922 - Crossref), 002 (Houk et al. 1980, Anal. Chem. 52(14), 2283-2289 - Crossref), 003 (plasma 6000-10000 K, 27/40 MHz), 004 (LOD ICP-MS ppt-ppb), 005 (40Ar16O+ sobre 56Fe+), 007 (exemplo granitoides; TAS com analise quimica e compativel com a politica de terminologia)"

revisao_didatica:
  data: 2026-09-23
  modo: review-and-fix
  relatorio: 28-analise-instrumental-i-revisao-didatica.md
  achados_nesta_aula:
    - "DID-M28-A04-CALIBRACAO-NAO-ENSINADA-002 (laranja) - secao 'Do sinal a concentracao' e bullet de recap acrescentados (titulo prometia metodos qualitativos e quantitativos; sensibilidade usada na Aula 06 sem definicao)"
    - "DID-M28-OA02-INTERFERENCIA-OES-AUSENTE-003 (laranja) - interferencia espectral do ICP-OES acrescentada (claim 009, verificado) e no recap"
    - "DID-M28-REFERENCIAS-CRUZADAS-007 (amarelo) - Proxima aula aponta a nova Aula 05 e anuncia a Aula 06"
  claims_criados: "009 (verificado nesta revisao, Inorganic Ventures), 010 (definicional)"
-->
