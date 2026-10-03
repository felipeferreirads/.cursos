# Aula 05: Fluorescência de raios X — princípios, aparelhagem e efeitos de matriz

**ID:** geologia-avancado-m28-a05
**Módulo:** [[28-analise-instrumental-i-modulo|Módulo 28 — Análise instrumental I]]
**Duração estimada:** ~19 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** entender os princípios físicos da fluorescência de raios X, distinguir suas duas variantes instrumentais e reconhecer os efeitos de matriz que tornam a preparação da amostra decisiva nessa técnica.
**Ao final você vai conseguir:** explicar por que a fluorescência de raios X mede transições eletrônicas de camadas internas, e não de valência como AAS e ICP; escolher entre XRF dispersiva em comprimento de onda e dispersiva em energia conforme o objetivo analítico; explicar absorção e reforço entre elementos pela posição das bordas de absorção; e escolher entre pérola fundida, pastilha prensada e medição direta conforme a pergunta geológica.
**Pré-requisito:** Aulas 02, 03 e 04 (preparação de amostra, fusão com fundente, princípios de espectrometria atômica, ICP).

> [!note] Parte 1 de 2 da antiga Aula 05
> Esta aula e a [[28-analise-instrumental-i-aula-06-estatistica-de-contagens-limites-de-deteccao|Aula 06]] eram uma aula só, dividida pela revisão didática de 2026-09-23 por excesso de conceitos independentes. Esta ficou com a física e a aparelhagem de XRF; a Aula 06 trata a estatística de contagens, a propagação de erros e os limites de detecção, que valem para todas as técnicas do módulo.

## Conteúdo

### Uma física diferente: transições de camadas internas, não de valência

As técnicas das Aulas 03 e 04 — absorção atômica e plasma de indução acoplada — exploram transições de elétrons de **valência**, as camadas eletrônicas mais externas, que respondem a energias relativamente baixas (ultravioleta e visível, de ~190 a ~850 nm). A **fluorescência de raios X** (*X-ray fluorescence*, XRF) explora um fenômeno físico distinto: quando um átomo é irradiado por raios X de energia suficientemente alta, um fóton pode arrancar um elétron de uma **camada eletrônica interna** (K ou L, as mais próximas do núcleo), deixando uma vacância. Um elétron de uma camada mais externa então preenche essa vacância, e o excesso de energia dessa transição é liberado como um fóton de raios X secundário — a "fluorescência" que dá nome à técnica —, com energia (e comprimento de onda) característicos e específicos de cada elemento.

Essa especificidade tem uma base física formalizada em 1913 pelo físico britânico Henry Moseley, então no grupo de Ernest Rutherford em Manchester, que descobriu a relação hoje chamada **lei de Moseley**: a raiz quadrada da frequência de uma linha de raios X característica é aproximadamente proporcional ao **número atômico** do elemento emissor. O trabalho de Moseley não foi só uma descoberta espectroscópica — foi a primeira demonstração experimental de que o número atômico, e não a massa atômica, é a propriedade fundamental que organiza a tabela periódica, e é a base física que permite à XRF identificar um elemento pela energia (ou comprimento de onda) de suas linhas de emissão características, com uma relação matemática direta e previsível entre posição espectral e número atômico.

### Duas variantes instrumentais: WDXRF e EDXRF

A engenharia de um espectrômetro de fluorescência de raios X se divide em duas famílias, distinguidas pela forma como separam os fótons de raios X secundários por energia:

**Fluorescência de raios X dispersiva em comprimento de onda** (*wavelength-dispersive XRF*, WDXRF): os fótons de raios X emitidos pela amostra atingem um cristal analisador (de estrutura cristalina conhecida) que os difrata em ângulos diferentes conforme o comprimento de onda, segundo a lei de Bragg — o mesmo princípio de difração de raios X usado em cristalografia. Um detector móvel, posicionado no ângulo correspondente a cada comprimento de onda de interesse, mede a intensidade de cada linha, uma de cada vez (ou várias simultaneamente, em instrumentos multicanal com vários detectores fixos). WDXRF oferece **resolução espectral muito mais alta**, o que reduz sobreposições de linhas entre elementos vizinhos e melhora tanto a exatidão quanto o limite de detecção — é a variante de escolha para a rotina de rocha total de alta qualidade, especialmente sobre a pérola de vidro fundido preparada como descrito na Aula 02.

**Fluorescência de raios X dispersiva em energia** (*energy-dispersive XRF*, EDXRF): usa um detector de estado sólido (por exemplo, um detector de deriva de silício) capaz de medir diretamente a energia de cada fóton incidente, sem precisar de um cristal analisador móvel, registrando um espectro inteiro de energias simultaneamente. EDXRF é mais simples, mais compacta, mais barata e mais rápida — inclusive em instrumentos portáteis de campo (*handheld XRF*, pXRF), cada vez mais usados em geologia de exploração e em triagem de testemunhos de sondagem — mas com resolução espectral menor que WDXRF, o que a torna mais sujeita a sobreposição de linhas entre elementos de número atômico próximo e, em geral, com limites de detecção um pouco piores para a mesma faixa de elementos.

A escolha entre as duas segue uma lógica já familiar deste módulo: WDXRF para exatidão e resolução em laboratório fixo, EDXRF (sobretudo pXRF) para rapidez, portabilidade e triagem — trade-offs análogos aos vistos entre ICP-OES e ICP-MS (Aula 04) e entre fusão e digestão ácida (Aula 02): a técnica "melhor" depende do objetivo, não é uma hierarquia absoluta.

### Efeitos de matriz em XRF: por que a intensidade não é diretamente proporcional à concentração

Diferente de ICP, onde a amostra chega ao detector já dissolvida em uma solução diluída e relativamente uniforme, a XRF mede a amostra na forma sólida (pérola de vidro fundido ou pastilha de pó prensado) — o que introduz **efeitos de matriz**: a intensidade de fluorescência de um elemento depende não só da sua própria concentração, mas também de como os outros elementos da matriz absorvem e reforçam os raios X, tanto os primários (do tubo de raios X) quanto os secundários (fluorescência de outros elementos). Dois efeitos são centrais:

- **Absorção**: elementos da matriz podem absorver parte da radiação de fluorescência de um elemento de interesse antes que ela saia da amostra e chegue ao detector, reduzindo o sinal medido abaixo do que a concentração real sozinha explicaria. A absorção é forte quando a **borda de absorção** do elemento da matriz fica logo abaixo da energia da linha do analito — e, para linhas K, esse elemento costuma ter número atômico *menor* que o do analito: o Cr (borda K em 5,99 keV) absorve fortemente o Fe Kα (6,40 keV). Além disso, matrizes pesadas em geral atenuam mais.
- **Reforço (enhancement)**: a fluorescência de um elemento de número atômico mais alto pode ter energia suficiente para excitar a fluorescência de um elemento de número atômico mais baixo presente na mesma matriz, aumentando artificialmente o sinal deste último — o Ni Kα (7,48 keV) reforça o Fe. Num aço inoxidável, portanto, o sinal do Fe é ao mesmo tempo absorvido pelo Cr e reforçado pelo Ni.

É exatamente por isso que a fusão com fundente de lítio (Aula 02) é tão valorizada em XRF de alta exatidão: diluir a amostra numa proporção alta e fixa de fundente reduz drasticamente a variação relativa da matriz entre amostras diferentes, tornando os efeitos de absorção e reforço muito mais previsíveis e corrigíveis matematicamente — os chamados algoritmos de correção de matriz (como o método de coeficientes de influência de Lachance-Traill ou de de Jongh, tratados em detalhe em cursos de instrumentação avançada, não neste módulo introdutório) dependem dessa diluição controlada para funcionar bem.

## Exemplo trabalhado: três perguntas, três formas de medir por XRF

**Situação.** Um projeto sobre uma suíte de basaltos faz três pedidos à mesma equipe: (a) os óxidos maiores de cada amostra, para classificação; (b) uma triagem rápida de dezenas de metros de testemunho de sondagem, ainda na caixa, para decidir que intervalos mandar ao laboratório; (c) elementos-traço como Rb, Sr, Zr e Nb, alguns em poucos ppm, para discutir a fonte do magma.

**Raciocínio.** Para (a), os elementos estão em concentração de percentual e o que importa é exatidão: WDXRF sobre **pérola fundida**. A diluição alta e fixa no fundente torna absorção e reforço previsíveis e corrigíveis de amostra para amostra, e o preço dessa diluição — limites de detecção piores (Aula 02) — não pesa em elementos maiores.

Para (b), o que importa é rapidez e poder medir no galpão de testemunhos: EDXRF portátil (pXRF), medindo o testemunho diretamente. O preço é duplo. A resolução menor deixa linhas de elementos vizinhos se sobreporem, e a medição sobre rocha não preparada não tem a pérola que uniformiza a matriz — os efeitos de matriz desta aula e a heterogeneidade de grão da Aula 01 pesam mais. O resultado serve para ranquear intervalos, não como teor final.

Para (c), o problema passa a ser o limite de detecção, e aqui a pérola atrapalha: a mesma diluição que controla a matriz dilui também os traços. A rotina clássica de traços por XRF é a **pastilha de pó prensado**, sem fundente — que em troca exige corrigir efeitos de matriz maiores, porque nada os uniformizou.

**O que fixar.** Em XRF, a pergunta decide a combinação de instrumento e preparação, e cada escolha troca uma vantagem por um custo conhecido: a pérola compra exatidão com diluição, a pastilha compra sensibilidade com efeitos de matriz, o pXRF compra rapidez com resolução e representatividade. A Aula 06 retoma o caso (c) com números: um Nb de poucos ppm medido sobre pérola, e como decidir se ele sustenta uma interpretação.

## Recap relâmpago

- A fluorescência de raios X mede transições de elétrons de camadas internas (K, L), não de valência como AAS e ICP; a lei de Moseley (1913) estabelece a relação entre a energia das linhas características e o número atômico do elemento, base física da identificação elementar por XRF.
- WDXRF (dispersão por cristal analisador, lei de Bragg) tem resolução espectral mais alta e é a variante de escolha para exatidão em laboratório; EDXRF (detector de estado sólido, espectro completo simultâneo) é mais rápida, mais barata e a base dos instrumentos portáteis de campo, com resolução espectral menor.
- Efeitos de matriz (absorção e reforço entre elementos) fazem a intensidade de fluorescência não ser diretamente proporcional à concentração. A absorção forte vem do elemento cuja borda fica logo abaixo da linha do analito (o Cr absorve o Fe Kα; o Ni o reforça), não simplesmente do mais pesado.
- A fusão com fundente de lítio (Aula 02) controla os efeitos de matriz ao diluir a amostra de forma alta e fixa, ao custo de piorar limites de detecção; por isso a pérola fundida serve aos elementos maiores e a pastilha prensada, sem diluição, aos traços.

## Próxima aula

[[28-analise-instrumental-i-aula-06-estatistica-de-contagens-limites-de-deteccao|Aula 06 — Estatística de contagens, propagação de erros e limites de detecção]]: o detector de XRF, no fim, conta fótons. A próxima aula parte dessa contagem para o tratamento de erro que fecha o módulo — Poisson, propagação de incertezas, limite de detecção e de quantificação — e que vale para todas as técnicas vistas até aqui.

## Fontes

- Moseley, H. G. J. (1913), "The high-frequency spectra of the elements", *Philosophical Magazine*, série 6, 26(156), 1024-1034, doi:10.1080/14786441308635052; e (1914), "The high-frequency spectra of the elements. Part II", *Philosophical Magazine*, 27(160), 703-713, doi:10.1080/14786440408635141. Paginação conferida no Crossref pela auditoria (2026-09-23). A Parte I (dezembro de 1913) é o trabalho de Manchester; a Parte II já foi feita em Oxford.
- Agilent Technologies, *Flame Atomic Absorption Spectrometry — Analytical Methods*, 13ª ed. — linhas analíticas de ~190 nm (As 193,7; Se 196,0) a ~850 nm (Cs 852,1), base da faixa espectral citada na primeira seção. Acrescentada pela auditoria (2026-09-23).
- Sobre absorção e reforço entre Cr, Fe e Ni: material didático de XRF quantitativo do Physlab/LUMS ("Quantitative XRF: matrix effects, corrections/influence coefficients"), a partir de Jenkins (1999). Acrescentada pela auditoria (2026-09-23).
- Actlabs, "Pressed Pellet XRF" — pastilha prensada como rotina de traços por XRF, LOD típico de 1 a 5 ppm. Acrescentada pela auditoria (2026-09-23).
- Jenkins, R. (1999), *X-Ray Fluorescence Spectrometry*, 2ª ed., Chemical Analysis vol. 152, Wiley-Interscience. VERIFICADO por busca na redação (2026-09-23): autor, edição, editora, ano e número do volume na série confirmados (Wiley Analytical Science, Biblio, AbeBooks).
- Sobre efeitos de matriz e algoritmos de correção (Lachance-Traill, de Jongh): mencionados por nome como referência ao leitor que queira aprofundar em curso de instrumentação avançada; não verificados por busca específica na redação — sinalizados como nomes consolidados na literatura de XRF, não como afirmação de conteúdo técnico detalhado.

<!--
nivel: avancado
palavras_corpo: 1593
recontagem_didatica: "Recontado por script na revisao didatica de 2026-09-23, depois da ultima edicao, a ~84 palavras/min (achado DID-M28-DURACOES-DECLARADAS-006). Valor declarado antes: PREENCHER."
palavras_corpo_metodo: "tokens separados por espaco entre '## Conteudo' e '## Fontes', incluindo tabelas, contados por script."
duracao_estimada_min: 19

divisao_de_aula: "Parte 1 da antiga Aula 05 unica (divisao pela revisao didatica de 2026-09-23, achado DID-M28-A05-SOBRECARGA-SEIS-BLOCOS-001). ID m28-a05 MANTIDO; arquivo RENOMEADO de 28-analise-instrumental-i-aula-05-fluorescencia-de-raios-x-estatistica-erros.md para 28-analise-instrumental-i-aula-05-fluorescencia-de-raios-x.md, porque o nome antigo anunciava a estatistica que foi para a Aula 06. Ficaram aqui, com texto integral, as secoes de fisica de XRF, WDXRF x EDXRF e efeitos de matriz e os bullets 1-3 do recap. Claims 001, 002, 003 e 007 permanecem neste arquivo. Acrescimos da revisao: callout de Parte 1, exemplo trabalhado NOVO (tres formas de medir por XRF), bullet 4 do recap e fecho do bullet 3. O exemplo novo so recombina fatos ja auditados no modulo (perola x pastilha x pXRF; ver claim 008)."

mapa_objetivo_secao:
  geologia-avancado-m28-oa02: "Uma física diferente: transições de camadas internas, não de valência" + "Duas variantes instrumentais: WDXRF e EDXRF" + "Efeitos de matriz em XRF"
  geologia-avancado-m28-oa03: "Duas variantes instrumentais: WDXRF e EDXRF" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: ANINST-M28-A05-MOSELEY-LEI-001
    claim: "Henry Moseley, no grupo de Ernest Rutherford em Manchester, descobriu em 1913 a lei que relaciona a raiz quadrada da frequencia de uma linha de raios X caracteristica ao numero atomico do elemento emissor, demonstrando experimentalmente que o numero atomico (nao a massa atomica) e a propriedade fundamental que organiza a tabela periodica."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-23): Wikipedia 'Moseley's law', Britannica e historyofinformation.com confirmam autor, ano, instituicao e o conteudo conceitual da descoberta. Paginacao CONFERIDA no Crossref pela auditoria de 2026-09-23: Phil. Mag. 26(156), 1024-1034 (1913) e 27(160), 703-713 (1914)."
  - claim_id: ANINST-M28-A05-WDXRF-EDXRF-DIFERENCA-002
    claim: "WDXRF usa um cristal analisador que difrata raios X por comprimento de onda segundo a lei de Bragg, com resolucao espectral mais alta; EDXRF usa um detector de estado solido que mede diretamente a energia de cada foton, registrando o espectro inteiro simultaneamente, com resolucao espectral menor mas maior rapidez, simplicidade e portabilidade (base dos instrumentos portateis pXRF)."
    risk: fato
    source: "Distincao padrao e amplamente documentada na literatura de instrumentacao de XRF (Jenkins 1999, X-Ray Fluorescence Spectrometry, 2a ed., Wiley); nao verificada por busca especifica nesta redacao alem da confirmacao bibliografica do livro, classificada como conhecimento consolidado de alta confianca do campo."
  - claim_id: ANINST-M28-A05-EFEITOS-MATRIZ-003
    claim: "Efeitos de matriz em XRF incluem absorcao (elementos da matriz cuja borda de absorcao fica logo abaixo da linha do analito - frequentemente de Z MENOR, ex. Cr absorvendo Fe Ka - absorvendo a fluorescencia antes de sair da amostra; 'Z mais alto' corrigido pela auditoria 2026-09-23, achado 11) e reforco/enhancement (fluorescencia de um elemento excitando a fluorescencia de outro de numero atomico mais baixo), e sao atenuados pela dilicao controlada da fusao com fundente de litio."
    risk: fato
    source: "Principio padrao de fisica de XRF, documentado em manuais de instrumentacao (Jenkins 1999; Potts 1987, ja citado na Aula 02); nao verificado por busca especifica adicional nesta redacao, classificado como conhecimento consolidado do campo."
  - claim_id: ANINST-M28-A05-FAIXA-ESPECTRAL-VALENCIA-007
    claim: "As linhas analiticas de AAS e ICP-OES (transicoes de valencia) cobrem o ultravioleta e o visivel, de ~190 nm (As 193,7; Se 196,0) a ~850 nm (Cs 852,1)."
    risk: fato
    source: "Criado pela auditoria de 2026-09-23 (achado 10). Agilent, Flame AAS Analytical Methods, 13a ed. (texto lido). A redacao dizia 'visivel e ultravioleta proxima'."
  - claim_id: ANINST-M28-A05-EXEMPLO-TRES-PREPARACOES-008
    claim: "Exemplo pedagogico hipotetico (criado pela revisao didatica): perola fundida + WDXRF para oxidos maiores (diluicao fixa controla a matriz; o custo em LOD nao pesa em maiores); pXRF sobre testemunho para triagem (resolucao menor, sem perola que uniformize a matriz, resultado para ranquear intervalos); pastilha prensada para tracos como Rb, Sr, Zr e Nb (sem diluicao do fundente, em troca de efeitos de matriz maiores a corrigir)."
    risk: hipotetico
    source: "Criado pela revisao didatica de 2026-09-23 (achado DID-M28-A05-SOBRECARGA-SEIS-BLOCOS-001: a Parte 1 precisava de exemplo proprio). Nenhum fato externo novo: recombina o que o modulo ja afirma e a auditoria conferiu - perola para exatidao e diluicao que piora LOD (Aula 02, claim A02-002), pXRF para triagem com resolucao menor (claim 002), perola controla efeitos de matriz (claim 003), pastilha prensada como rotina de tracos por XRF (auditoria achado 13, Actlabs), Rb, Sr, Y, Zr e Nb medidos bem por XRF pelas linhas K (relatorio de auditoria, achado 13). 'Pastilha exige corrigir matriz maior' e inferencia direta do claim 003 (sem diluicao, nada uniformiza a matriz)."

auditoria:
  data: 2026-09-23
  modo: audit-and-fix
  relatorio: 28-analise-instrumental-i-auditoria.md
  nota_divisao: "Auditada como parte da antiga Aula 05 (arquivo 28-analise-instrumental-i-aula-05-fluorescencia-de-raios-x-estatistica-erros.md). Os achados 12 e 13 da mesma auditoria vivem hoje na Aula 06."
  achados_nesta_aula:
    - "10 (laranja) ANINST-M28-A05-FAIXA-ESPECTRAL-VALENCIA-007 (novo) - 'ultravioleta proxima' -> UV-visivel ~190-850 nm - corrigido"
    - "11 (laranja) ANINST-M28-A05-EFEITOS-MATRIZ-003 - absorcao pela borda, nao por 'Z mais alto' - corrigido"
  incertezas_resolvidas: "Paginacao de Moseley (1913, 1914) conferida no Crossref; marcas retiradas."
  verificados_sem_achado: "001 (lei de Moseley), 002 (WDXRF x EDXRF)"

revisao_didatica:
  data: 2026-09-23
  modo: review-and-fix
  relatorio: 28-analise-instrumental-i-revisao-didatica.md
  achados_nesta_aula:
    - "DID-M28-A05-SOBRECARGA-SEIS-BLOCOS-001 (laranja) - antiga Aula 05 dividida; esta e a Parte 1, com exemplo proprio"
-->
