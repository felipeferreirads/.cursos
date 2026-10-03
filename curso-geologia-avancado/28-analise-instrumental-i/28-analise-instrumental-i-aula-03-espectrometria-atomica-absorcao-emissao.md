# Aula 03: Espectrometria atômica — princípios de absorção e emissão; a técnica de absorção atômica

**ID:** geologia-avancado-m28-a03
**Módulo:** [[28-analise-instrumental-i-modulo|Módulo 28 — Análise instrumental I]]
**Duração estimada:** ~22 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** entender os princípios físicos comuns que sustentam toda espectrometria atômica (absorção e emissão), e dominar a técnica de absorção atômica em chama e em forno de grafite como primeiro caso concreto dessa família de métodos.
**Ao final você vai conseguir:** explicar por que átomos livres em fase gasosa absorvem e emitem luz em comprimentos de onda discretos e característicos de cada elemento; distinguir espectrometria de absorção de espectrometria de emissão em termos do que cada uma mede; e escolher entre absorção atômica em chama e em forno de grafite conforme a sensibilidade exigida.
**Pré-requisito:** Aula 02 (preparação de amostra — a solução usada nesta aula é o produto direto da digestão ácida ou da dissolução do fundido de fusão). Assume-se noção básica de estrutura eletrônica atômica (níveis de energia, transições eletrônicas) de química de graduação.

## Conteúdo

### Por que um átomo livre absorve e emite luz em comprimentos de onda específicos

Todo o edifício da espectrometria atômica — absorção atômica (Aula 03), emissão em plasma (ICP-OES, Aula 04) e, com uma física distinta mas o mesmo princípio de fundo, fluorescência de raios X (Aula 05) — repousa numa ideia central da física quântica: os elétrons de um átomo só podem ocupar níveis discretos de energia, não um contínuo. Quando um átomo absorve energia suficiente (de uma fonte de luz, de calor de uma chama, da energia de um plasma), um elétron pode saltar de um nível de energia mais baixo para um mais alto — uma **transição eletrônica**. Como essa energia é quantizada (tem valores discretos, específicos de cada elemento, definidos pela configuração eletrônica de cada átomo), o comprimento de onda de luz absorvido ou emitido nessa transição também é discreto e específico — é a "impressão digital" espectral de cada elemento.

Dois processos, opostos em direção, exploram essa mesma física:

- **Absorção**: átomos no **estado fundamental** (a configuração eletrônica de energia mínima) absorvem fótons de comprimentos de onda específicos, sendo promovidos a um estado excitado. Mede-se a *diminuição* da intensidade de luz de uma fonte, ao passar por uma população de átomos livres, num comprimento de onda característico do elemento de interesse.
- **Emissão**: átomos que já estão num **estado excitado** — porque receberam energia térmica suficiente de uma chama ou de um plasma — retornam espontaneamente ao estado fundamental, e o excesso de energia é liberado como um fóton de comprimento de onda característico. Mede-se a *intensidade* de luz emitida nesse comprimento de onda.

A relação entre a intensidade do sinal medido (absorbância ou intensidade de emissão) e a concentração do elemento na amostra segue, na absorção, a **lei de Beer-Lambert**: a absorbância é proporcional ao número de átomos absorventes no caminho óptico, o que torna a técnica inerentemente quantitativa quando calibrada com padrões de concentração conhecida — princípio de calibração comum a toda a família de técnicas deste módulo, que a Aula 04 detalha (curva de calibração e sensibilidade) e a Aula 06 trata com rigor estatístico (limites de detecção e de quantificação).

### Espectrometria de absorção atômica (AAS): como funciona

A **espectrometria de absorção atômica** (*atomic absorption spectroscopy*, AAS) foi desenvolvida por Alan Walsh, físico da divisão de química industrial da CSIRO (organização de pesquisa científica da Austrália), que publicou o artigo fundador "The Application of Atomic Absorption Spectra to Chemical Analysis" em 1955, após depositar a patente correspondente em 1954. A contribuição central de Walsh foi perceber que uma **lâmpada de cátodo oco** (*hollow cathode lamp*) — uma lâmpada cujo cátodo é feito do próprio elemento que se quer medir — emite linhas espectrais extremamente estreitas e intensas, exatamente nos comprimentos de onda que os átomos livres desse elemento absorvem. Isso resolveu o problema prático de obter uma fonte de luz suficientemente monocromática e estável para medir absorção atômica com precisão analítica útil.

O arranjo instrumental básico de um espectrômetro de absorção atômica segue esta sequência:

1. **Fonte de luz**: uma lâmpada de cátodo oco (ou, numa variante posterior, uma lâmpada de descarga sem eletrodo) específica do elemento a medir, emitindo as linhas espectrais características desse elemento.
2. **Atomizador**: converte a amostra líquida (a solução preparada na Aula 02) numa nuvem de átomos livres em estado fundamental. É aqui que as duas variantes principais da técnica se diferenciam:
   - **Chama** (*flame AAS*, FAAS): a solução é nebulizada e introduzida numa chama, tipicamente de ar-acetileno (para a maioria dos elementos) ou óxido nitroso-acetileno (para elementos que formam óxidos refratários estáveis, como Al, Ti e terras-raras, que exigem temperatura de chama mais alta para atomizar eficientemente).
   - **Forno de grafite** (*graphite furnace AAS*, GFAAS, também chamada *electrothermal AAS*, ETAAS): a amostra é depositada num tubo de grafite aquecido eletricamente em etapas programadas (secagem, calcinação, atomização), atingindo temperaturas de até cerca de 2500–3000 °C na etapa de atomização. Como toda a amostra permanece confinada no tubo por um tempo mais longo (em vez de passar rapidamente por uma chama), a população de átomos livres no caminho óptico é muito maior por unidade de amostra, o que melhora os limites de detecção em uma a três ordens de grandeza em relação à chama, conforme o elemento — as fontes dão fatores que vão de ~20 a ~1000 vezes, e não há um valor único.
3. **Monocromador**: isola o comprimento de onda específico de interesse, separando-o de outras linhas emitidas pela lâmpada e de radiação de fundo do próprio atomizador.
4. **Detector**: mede a intensidade de luz transmitida, que é comparada com a intensidade sem amostra (feixe de referência ou medição alternada) para calcular a absorbância.

### Interferências típicas em AAS

Nenhuma técnica espectrométrica é livre de interferências, e reconhecê-las é o que separa um resultado confiável de um artefato interpretado como dado real — tema que a Aula 06 vai sistematizar com mais rigor estatístico, mas que já aparece de forma concreta em AAS:

- **Interferências químicas**: quando um componente da matriz da amostra forma um composto estável com o elemento de interesse antes da atomização (por exemplo, fosfato formando compostos refratários com cálcio), reduzindo a fração de átomos livres disponíveis. Controla-se com agentes liberadores ou protetores (como lantânio ou EDTA, dependendo do sistema) adicionados à solução.
- **Interferências de ionização**: em chamas de temperatura mais alta, alguns átomos (especialmente de metais alcalinos e alcalino-terrosos, como Na, K, Ca) podem se ionizar parcialmente, e um íon não absorve no mesmo comprimento de onda do átomo neutro, reduzindo o sinal. Controla-se adicionando um "supressor de ionização" — um elemento de ionização ainda mais fácil (como césio) em excesso, que satura o equilíbrio de ionização e libera o elemento de interesse na forma atômica neutra.
- **Interferências espectrais e de fundo** (*background*): absorção ou dispersão de luz por partículas não vaporizadas ou por moléculas não dissociadas na chama ou no forno, que reduzem a intensidade transmitida sem relação com o elemento de interesse. Corrigidas por sistemas de correção de fundo (lâmpada de deutério, ou o efeito Zeeman em instrumentos de forno de grafite mais sofisticados).

### Onde AAS se encaixa no panorama deste módulo

A absorção atômica foi, historicamente, uma das primeiras técnicas instrumentais quantitativas de rotina amplamente adotadas em laboratórios de geoquímica, a partir de meados da década de 1960 (o primeiro instrumento comercial saiu em 1963; antes dela, a espectrografia de emissão em arco já era usada, mas de forma semiquantitativa), e permanece em uso para determinações pontuais de elementos específicos (nota­damente Au por AAS com forno de grafite após pré-concentração, e alguns metais em análises ambientais). Mas, para a rotina moderna de geoquímica de rocha total multi-elementar — dezenas de elementos maiores e traços na mesma alíquota —, ela foi amplamente suplantada pelas técnicas de plasma de indução acoplada (ICP-OES e ICP-MS, Aula 04), que aplicam o mesmo princípio físico de espectrometria atômica, mas com uma fonte de atomização e excitação — o plasma — capaz de medir dezenas de elementos simultaneamente com muito mais rapidez. Entender AAS primeiro, porém, isola os princípios físicos comuns (transição eletrônica, lei de Beer-Lambert, interferências químicas e de ionização) num instrumento mais simples, antes de somá-los à complexidade adicional do plasma na Aula 04.

## Exemplo trabalhado: determinando Ca num basalto por AAS em chama e reconhecendo uma interferência de ionização

**Situação.** Uma solução de basalto preparada por digestão ácida (Aula 02) é analisada por AAS em chama óxido nitroso-acetileno para determinar a concentração de Ca. A chama quente foi escolhida de propósito: numa matriz silicática, a chama ar-acetileno sofreria forte interferência química de Al, Si e P sobre o Ca (a que se corrige com agente liberador como o lantânio, visto acima), e a chama mais quente decompõe esses compostos. O analista mede a solução diretamente, sem qualquer tratamento adicional, e obtém um valor sistematicamente mais baixo que o esperado pela composição típica de basaltos e confirmado por um método alternativo (ICP-OES).

**Diagnóstico.** O Ca é um elemento alcalino-terroso relativamente fácil de ionizar, e na temperatura da chama óxido nitroso-acetileno a ionização do próprio cálcio passa a ser a interferência principal (na ar-acetileno ela é um efeito menor, de poucos por cento, e quem domina é a interferência química). Uma fração dos átomos de Ca liberados na chama se ioniza a Ca⁺, que não absorve no comprimento de onda característico do Ca neutro (422,7 nm) usado na medição. Esse Ca "perdido" para a ionização faz a absorbância medida ser menor do que a que corresponderia à concentração real de Ca na solução — um viés sistemático por subestimação, análogo em lógica (embora de causa física diferente) ao viés de dissolução incompleta discutido na Aula 02.

**Correção.** O analista repete a medição após adicionar um excesso de cloreto de potássio ou de césio à solução (e aos padrões de calibração, na mesma concentração). O potássio (ou césio), mais fácil de ionizar que o cálcio, satura preferencialmente o equilíbrio de ionização na chama, "protegendo" o cálcio da ionização e restaurando a proporção de átomos neutros de Ca disponíveis para absorção. O resultado corrigido concorda, dentro do erro esperado, com o valor obtido por ICP-OES.

**O que fixar.** Uma interferência de ionização não é um erro aleatório visível como dispersão entre réplicas — é um viés sistemático que se repete de forma consistente enquanto a causa (a matriz da amostra e da chama) não mudar. Reconhecê-la exige entender o princípio físico por trás da técnica, não apenas operar o instrumento; e a correção padrão (supressor de ionização) só funciona porque age exatamente na causa física do problema.

## Recap relâmpago

- Toda espectrometria atômica repousa na quantização de níveis de energia eletrônica: átomos absorvem ou emitem luz em comprimentos de onda discretos, característicos de cada elemento; absorção mede átomos no estado fundamental absorvendo luz de uma fonte, emissão mede átomos excitados liberando luz espontaneamente.
- A absorção atômica (AAS) foi desenvolvida por Alan Walsh (CSIRO, Austrália), publicada em 1955, e depende de uma lâmpada de cátodo oco específica do elemento como fonte de luz monocromática.
- AAS em chama (ar-acetileno ou óxido nitroso-acetileno) é mais simples e rápida; AAS em forno de grafite atomiza toda a amostra num tubo aquecido eletricamente, melhorando os limites de detecção em uma a três ordens de grandeza sobre a chama, conforme o elemento, ao custo de análise mais lenta, elemento por elemento.
- As principais interferências em AAS são químicas (formação de compostos refratários que reduzem átomos livres), de ionização (perda de átomos neutros para íons, especialmente em alcalinos e alcalino-terrosos) e espectrais/de fundo (absorção ou dispersão não específica) — cada uma com uma estratégia de correção própria (agentes liberadores, supressores de ionização, correção de fundo).
- Para rotina multi-elementar moderna de rocha total, AAS foi largamente suplantada por ICP-OES e ICP-MS, mas seus princípios físicos (transição eletrônica, lei de Beer-Lambert, interferências) são a base direta da Aula 04.

## Próxima aula

[[28-analise-instrumental-i-aula-04-icp-oes-icp-ms|Aula 04 — Plasma de indução acoplada (ICP-OES e ICP-MS)]]: como o plasma, em vez de uma chama ou de um forno de grafite, atinge temperaturas muito mais altas e permite medir dezenas de elementos simultaneamente, tanto por emissão óptica (ICP-OES) quanto por espectrometria de massa (ICP-MS).

## Fontes

- Walsh, A. (1955), "The Application of Atomic Absorption Spectra to Chemical Analysis", *Spectrochimica Acta*, 7, 108-117, doi:10.1016/0371-1951(55)80013-6 (artigo fundador da técnica). Título, volume e paginação conferidos no Crossref pela auditoria (2026-09-23).
- CSIROpedia, "Atomic absorption spectroscopy" e "Atomic absorption spectroscopy publications" (páginas institucionais de história da CSIRO). VERIFICADO por busca nesta redação (2026-09-23): confirma Alan Walsh, a patente australiana de 1954 e a publicação de 1955.
- Skoog, D. A., Holler, F. J. & Crouch, S. R., *Principles of Instrumental Analysis*, 7ª ed. (2017/2018), Cengage — capítulo 9, "Atomic Absorption and Atomic Fluorescence Spectrometry", referência padrão de graduação/pós-graduação para os princípios de AAS, tipos de atomizador e interferências descritos nesta aula. VERIFICADO por busca nesta redação (2026-09-23) quanto a edição, ano e numeração do capítulo.
- Sobre a melhoria dos limites de detecção do forno de grafite sobre a chama (uma a três ordens de grandeza, conforme o elemento): Harvey, D., *Analytical Chemistry 2.1*, §10.4 (LibreTexts) — vapor "até 1000×" mais concentrado que na chama, exemplo do Zn com ~420×; Sperling, M., "Flame and Graphite Furnace Atomic Absorption Spectrometry in Environmental Analysis", *Encyclopedia of Analytical Chemistry*, Wiley — limites 20 a 200 vezes menores. As fontes não convergem num valor único; por isso a aula dá só a ordem de grandeza (correção da auditoria, 2026-09-23).
- Agilent Technologies, *Flame Atomic Absorption Spectrometry — Analytical Methods*, 13ª ed. — entrada do Ca: interferência química pronunciada na chama ar-acetileno (corrigida com Sr ou La), ionização como efeito de 5-10% nessa chama e como interferência principal na chama óxido nitroso-acetileno (corrigida com 2000-5000 µg/mL de K). Acrescentada pela auditoria (2026-09-23).
- CSIROpedia, "Atomic absorption spectroscopy" — primeiro instrumento comercial (Perkin-Elmer 303) em 1963 e crescimento das vendas em 1963-67. Acrescentada pela auditoria (2026-09-23).

<!--
nivel: avancado
palavras_corpo: 1867
recontagem_didatica: "Recontado por script na revisao didatica de 2026-09-23, depois da ultima edicao, a ~84 palavras/min (achado DID-M28-DURACOES-DECLARADAS-006). Valor declarado antes: 1850."
palavras_corpo_metodo: "tokens separados por espaco entre '## Conteudo' e '## Fontes', incluindo tabelas, seguindo a convencao do modulo 26/27."
duracao_estimada_min: 22

mapa_objetivo_secao:
  geologia-avancado-m28-oa02: "Por que um átomo livre absorve e emite luz em comprimentos de onda específicos" + "Espectrometria de absorção atômica (AAS): como funciona" + "Interferências típicas em AAS"
  geologia-avancado-m28-oa03: "Onde AAS se encaixa no panorama deste módulo" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: ANINST-M28-A03-WALSH-1955-001
    claim: "Alan Walsh, fisico da CSIRO (Australia), desenvolveu a espectrometria de absorcao atomica, depositou patente australiana em 1954 e publicou o artigo fundador 'The Application of Atomic Absorption Spectra to Chemical Analysis' em 1955, introduzindo a lampada de catodo oco como fonte de luz monocromatica especifica do elemento."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-23): CSIROpedia e AZoM confirmam Walsh, CSIRO, a patente de 1954 (Australian Patent Specification 163,586) e a publicacao de 1955. Paginacao do artigo (Spectrochimica Acta, 7, 108-117) CONFERIDA no Crossref pela auditoria de 2026-09-23 (doi:10.1016/0371-1951(55)80013-6)."
  - claim_id: ANINST-M28-A03-CHAMA-TIPOS-002
    claim: "AAS em chama tipicamente usa chama ar-acetileno para a maioria dos elementos e chama oxido nitroso-acetileno (mais quente) para elementos que formam oxidos refrattarios estaveis, como Al, Ti e terras-raras."
    risk: fato
    source: "Principio padrao de instrumentacao AAS, consolidado em manuais de quimica analitica instrumental (Skoog, Holler & Crouch, Principles of Instrumental Analysis, 7a ed., cap. 9); nao verificado por busca especifica nesta redacao, classificado como conhecimento consolidado de alta confianca do campo."
  - claim_id: ANINST-M28-A03-FORNO-GRAFITE-SENSIBILIDADE-003
    claim: "AAS em forno de grafite (ETAAS/GFAAS) atinge temperaturas de ate cerca de 2500-3000 C na etapa de atomizacao e melhora os limites de deteccao em uma a tres ordens de grandeza em relacao a chama, conforme o elemento (fontes dao de ~20x a ~1000x; nao ha valor unico - redacao corrigida pela auditoria 2026-09-23, achado 5)."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-23): fontes tecnicas convergentes (Wikipedia 'Graphite furnace atomic absorption', EAG Laboratories, Torontech, CASRAI) confirmam melhoria de sensibilidade na faixa de uma a tres ordens de grandeza, com valores especificos variando entre as fontes (10-1000x, 100-1000x, 20-200x conforme a fonte). Faixa de temperatura do forno de grafite e valor tipico de manuais de instrumentacao, nao conferido contra especificacao de fabricante especifico nesta redacao."
  - claim_id: ANINST-M28-A03-INTERFERENCIA-IONIZACAO-CA-004
    claim: "Calcio, sendo alcalino-terroso relativamente facil de ionizar, sofre interferencia de ionizacao na chama oxido nitroso-acetileno (onde ela e a interferencia principal), que subestima a absorbancia medida no comprimento de onda 422,7 nm; a correcao padrao e adicionar excesso de um supressor de ionizacao (potassio ou cesio) a amostra e aos padroes. Na chama ar-acetileno a interferencia dominante sobre o Ca em matriz silicatica e quimica (Al, Si, P), e a ionizacao e efeito de 5-10%. [Corrigido pela auditoria 2026-09-23, achado 7 vermelho: a redacao atribuia a ionizacao a chama ar-acetileno.]"
    risk: fato
    source: "Principio padrao de quimica analitica instrumental para AAS, amplamente documentado em manuais de referencia (Skoog et al.); o comprimento de onda de 422,7 nm para a linha de absorcao do calcio e um valor de conhecimento consolidado e alta confianca na espectroscopia atomica, nao verificado por busca especifica nesta redacao."
  - claim_id: ANINST-M28-A03-EXEMPLO-CA-BASALTO-005
    claim: "Exemplo pedagogico hipotetico de subestimacao de Ca em basalto por AAS em chama devido a interferencia de ionizacao, corrigida por adicao de supressor de ionizacao e confirmada por comparacao com ICP-OES."
    risk: hipotetico
    source: "Exemplo pedagogico construido especificamente para esta aula, ilustrando um principio real (interferencia de ionizacao do calcio em AAS) com valores e narrativa hipoteticos, nao correspondentes a uma analise publicada especifica. [Auditoria 2026-09-23: chama trocada para oxido nitroso-acetileno - ver claim 004.]"
  - claim_id: ANINST-M28-A03-ADOCAO-AAS-HISTORICO-006
    claim: "A AAS foi uma das primeiras tecnicas instrumentais quantitativas de rotina adotadas em laboratorios de geoquimica, a partir de meados da decada de 1960 (primeiro instrumento comercial em 1963); a espectrografia de emissao em arco, semiquantitativa, ja era usada antes."
    risk: fato
    source: "Criado pela auditoria de 2026-09-23 (achado 6). CSIROpedia 'Atomic absorption spectroscopy' (Perkin-Elmer 303 em 1963; vendas 1963-67); Grimes & Marranzino (1968), USGS Circular 591."

auditoria:
  data: 2026-09-23
  modo: audit-and-fix
  relatorio: 28-analise-instrumental-i-auditoria.md
  achados_nesta_aula:
    - "5 (laranja) ANINST-M28-A03-FORNO-GRAFITE-SENSIBILIDADE-003 - 'fontes convergem em 100-1000x' -> uma a tres ordens de grandeza - corrigido (corpo, recap, Fontes)"
    - "6 (laranja) ANINST-M28-A03-ADOCAO-AAS-HISTORICO-006 (novo) - 'primeira tecnica espectrometrica' e 'final da decada de 1960' - corrigido"
    - "7 (VERMELHO) ANINST-M28-A03-INTERFERENCIA-IONIZACAO-CA-004 (cobre EXEMPLO-CA-BASALTO-005) - exemplo do Ca movido para chama oxido nitroso-acetileno - corrigido"
  incertezas_resolvidas: "Paginacao de Walsh (1955) 7, 108-117 conferida no Crossref; marca de incerteza retirada."
  verificados_sem_achado: "001 (Walsh, CSIRO, patente 1954), 002 (tipos de chama)"

revisao_didatica:
  data: 2026-09-23
  modo: review-and-fix
  relatorio: 28-analise-instrumental-i-revisao-didatica.md
  achados_nesta_aula:
    - "DID-M28-REFERENCIAS-CRUZADAS-007 (amarelo) - promessa 'calibracao tratada com rigor na Aula 05' (que nao tratava calibracao) redirecionada para Aula 04 (curva de calibracao) e Aula 06 (limites); interferencias remetem a Aula 06"
-->
