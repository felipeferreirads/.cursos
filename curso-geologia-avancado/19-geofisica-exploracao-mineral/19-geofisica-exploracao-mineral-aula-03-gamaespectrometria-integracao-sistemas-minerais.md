# Aula 03: Gamaespectrometria e integração de assinaturas geofísicas em sistemas minerais

**ID:** geologia-avancado-m19-a03
**Módulo:** [[19-geofisica-exploracao-mineral-modulo|Módulo 19 — Geofísica aplicada na exploração mineral]]
**Duração estimada:** ~17 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** interpretar dados gamaespectrométricos em termos da propriedade física que medem — concentração de radioelementos — e combiná-los com a regra de sinal magnética da Aula 02 para discriminar zonas de alteração hidrotermal que nenhum dos dois métodos separa sozinho.
**Ao final você vai conseguir:** explicar que propriedade física a gamaespectrometria mede, e citar o contraste típico de radioatividade entre rochas alteradas e a rocha encaixante; explicar por que a gamaespectrometria só enxerga os primeiros centímetros do terreno, e o que isso implica para seu uso em exploração; e, combinando esse dado com a regra de sinal magnética estudada na Aula 02, explicar por que o canal de potássio sozinho não separa alteração potássica de fílica.
**Pré-requisito:** [[19-geofisica-exploracao-mineral-aula-02-gravimetria-magnetometria-sistemas-minerais|Aula 02 deste módulo]] (a regra de sinal do zoneamento de alteração de um pórfiro em magnetometria — potássica acrescenta magnetita, fílica destrói —, que esta aula usa diretamente para resolver a ambiguidade do canal de potássio) e [[16-aerogeofisica/16-aerogeofisica-modulo|Módulo 16 — Introdução à aerogeofísica]], cujos fundamentos de aquisição aérea radiométrica esta aula retoma e aplica especificamente à exploração mineral.

## Conteúdo

### Gamaespectrometria: só a pele do terreno, mas informativa sobre alteração

A gamaespectrometria mede a radiação gama natural emitida pelos isótopos radioativos de três elementos — potássio (K, via o isótopo ⁴⁰K), urânio (U, medido indiretamente pela linha de emissão do bismuto-214, produto da série de decaimento do urânio) e tório (Th, medido pela linha do tálio-208, produto da série do tório) — que ocorrem naturalmente em concentrações traço em quase todas as rochas. O equipamento discrimina os três elementos porque cada um produz um pico de energia característico no espectro gama, e a IAEA padroniza uma janela em torno de cada pico: o potássio produz um pico em 1,46 MeV (janela padrão **1,37-1,57 MeV**), o urânio um pico em 1,76 MeV (janela **1,66-1,86 MeV**) e o tório um pico em 2,61 MeV (janela **2,41-2,81 MeV**). Repare que as janelas **não se tocam** — há intervalos mortos entre elas (1,57-1,66 e 1,86-2,41 MeV), justamente para reduzir o vazamento de contagens de uma janela para a vizinha, que é o problema que as correções de *stripping* depois tratam. São três janelas de energia que um espectrômetro aéreo ou terrestre discrimina eletronicamente para gerar os três canais K, U (eU) e Th (eTh) — o "e" indica que urânio e tório são medidos por equivalência através dos produtos de decaimento, não diretamente.

A limitação física mais importante do método é que a radiação gama é fortemente atenuada pela própria rocha: praticamente todo o sinal detectado vem dos primeiros 30-45 cm de material — em geofísica de exploração, é comum descrever a gamaespectrometria como um método que enxerga apenas a "pele" do terreno. Isso significa que ela não detecta radioatividade em profundidade (ao contrário da gravimetria e da magnetometria, vistas na Aula 02, que respondem a corpos a centenas de metros de profundidade) — mas, dentro dessa limitação, ela é extremamente sensível a **alteração hidrotermal na superfície ou próxima dela**, porque muitos dos minerais de alteração mais diagnósticos de sistemas minerais controlam diretamente a razão K/Th/U: alteração potássica intensa (comum em pórfiros de cobre-ouro e em muitos sistemas orogênicos de ouro) eleva fortemente o canal de potássio; alteração propilítica e argílica tende a lixiviar potássio e deixar uma resposta relativamente mais rica em tório (que é geoquimicamente mais imóvel); e razões U/Th anômalas podem sinalizar zonas de intemperismo profundo ou de mobilização de urânio associada a fluidos oxidantes. Por isso a gamaespectrometria, apesar de "cega" para profundidade, é um dos métodos aerogeofísicos mais diretamente ligados ao componente de **deposição** de um sistema mineral: ela mapeia, na superfície, a própria assinatura mineralógica da alteração que acompanhou a precipitação do metal — quando essa alteração aflora ou está próxima da superfície.

Só que a alteração potássica não é a única a elevar o canal de K: a alteração **fílica/sericítica**, vista na Aula 02 como a que destrói magnetita (baixo magnético), também eleva o potássio, porque a sericita é, ela mesma, uma mica potássica. O canal K, isoladamente, não tem como distinguir as duas — e é exatamente esse ponto que o exemplo a seguir explora, combinando o dado radiométrico desta aula com a regra de sinal magnética da Aula 02.

## Exemplo trabalhado

**Situação:** um levantamento aerogeofísico combinado (magnetometria + gamaespectrometria) sobre um alvo de pórfiro de cobre-ouro mostra: (a) um alto magnético circular de baixa amplitude relativa envolvendo um "buraco" magnético mais estreito no centro; (b) um alto pronunciado no canal de potássio coincidente com o centro do buraco magnético; (c) um halo de tório relativamente elevado nas bordas externas do alto magnético circular, além do limite do alto de potássio.

**Pergunta:** interprete essa combinação de assinaturas em termos das zonas de alteração hidrotermal típicas de um sistema pórfiro, e explique o papel de cada método na interpretação.

**Resolução:**

O **buraco magnético central** é consistente com uma zona de **destruição de magnetita** — e, num pórfiro, a assembleia que destrói magnetita é a **fílica/sericítica** (quartzo-sericita-pirita), ácida o suficiente para consumir a magnetita primária e a hidrotermal, não a potássica. O **alto de potássio coincidente** não contradiz essa leitura: a sericita é uma mica potássica, de modo que a zona fílica também aparece como alto no canal de K. É exatamente aí que mora a armadilha interpretativa deste exemplo — o alto de K sozinho **não** distingue alteração potássica de fílica; quem distingue é o sinal magnético, porque as duas respondem em sentidos opostos.

O **anel de alto magnético mais amplo** ao redor do buraco central é consistente com o **núcleo potássico preservado** (biotita secundária e feldspato potássico com magnetita hidrotermal, que a alteração potássica tipicamente acrescenta) e/ou com a zona propilítica externa, onde a magnetita da encaixante é preservada ou reposta por cloritização com magnetita secundária. O padrão "baixo magnético central cercado por alto magnético anelar" é, portanto, a leitura de um sistema com **núcleo fílico sobreposto** a uma raiz potássica magnetítica — e a configuração mais comumente ilustrada na literatura é a recíproca: alto magnético no núcleo potássico cercado por um **anel** (*donut*) de baixo magnético fílico, o mesmo padrão trabalhado no exemplo da Aula 02. Em qualquer das duas, o que vale é a regra de sinal: potássica acrescenta magnetita, fílica destrói.

O **halo de tório elevado além do limite do alto de potássio** é consistente com a zona de alteração argílica/propilítica externa mais distal, onde o potássio já foi lixiviado (reduzindo o canal de K) e o tório, geoquimicamente mais imóvel, se torna relativamente mais proeminente na razão — não porque haja mais tório em termos absolutos, necessariamente, mas porque a perda de K e a resistência do Th a esse mesmo intemperismo/alteração deslocam a razão K/Th observável.

**Conclusão:** nenhum dos dois métodos, isoladamente, permitiria essa interpretação com a mesma confiança. A magnetometria dá a geometria em profundidade da destruição/preservação de magnetita (um proxy indireto de alteração), mas não diz nada sobre a mineralogia real da alteração; a gamaespectrometria, limitada aos primeiros centímetros do terreno, mede diretamente o comportamento dos radioelementos na alteração exposta (ganho de K nas zonas potássica e fílica, perda de K e domínio relativo de Th nas zonas argílica/propilítica distais) mas não enxerga a raiz do sistema em profundidade — e, sozinha, não separa potássica de fílica, já que ambas enriquecem K. A combinação de ambos, alinhada espacialmente, é o que permite reconstruir o zoneamento de alteração esperado de um pórfiro — um exemplo direto de como métodos de campo potencial e radiométrico, cada um respondendo a uma propriedade física diferente, se complementam na leitura de um único sistema mineral.

## Recap relâmpago

- A **gamaespectrometria** mede radiação gama de K (pico 1,46 MeV, janela IAEA 1,37-1,57), U por equivalência via Bi-214 (pico 1,76 MeV, janela 1,66-1,86) e Th por equivalência via Tl-208 (pico 2,61 MeV, janela 2,41-2,81), mas só "enxerga" os primeiros 30-45 cm do terreno — é cega em profundidade, porém muito sensível à mineralogia de alteração exposta ou subaflorante.
- A alteração **fílica/sericítica**, não só a potássica, eleva o canal de K (a sericita também é mica potássica) — por isso o canal K, sozinho, não separa as duas; quem separa é o sinal magnético da Aula 02 (potássica dá alto, fílica dá baixo).
- Combinar magnetometria (Aula 02) e gamaespectrometria permite reconstruir zoneamentos de alteração hidrotermal — como no zoneamento potássico-fílico-propilítico-argílico de um pórfiro — que nenhum dos dois métodos revela sozinho.

## Próxima aula

[[19-geofisica-exploracao-mineral-aula-04-eletrorresistividade-polarizacao-induzida|Aula 04 — Eletrorresistividade e polarização induzida]] — os dois métodos elétricos mais usados em escala de alvo e depósito, e como eles respondem à condutividade e à capacidade de os sulfetos armazenarem carga elétrica.

## Fontes

- Clark, D. A. (2014), "Magnetic effects of hydrothermal alteration in porphyry copper and iron-oxide copper-gold systems: A review", *Tectonophysics*, 624-625, 46-65, DOI 10.1016/j.tecto.2013.12.011 (qual zona de alteração acrescenta e qual destrói magnetita em sistemas pórfiro, e a assinatura magnética anelar resultante).
- Sillitoe, R. H. (2010), "Porphyry Copper Systems", *Economic Geology*, 105(1), 3-41 (zoneamento de alteração potássica-fílica-propilítica-argílica avançada em sistemas pórfiro).
- IAEA (2003), *Guidelines for radioelement mapping using gamma ray spectrometry data*, IAEA-TECDOC-1363, International Atomic Energy Agency (janelas de energia espectral padrão para K, U e Th e profundidade de penetração do sinal gama).
- Dentith, M. & Mudge, S. T. (2014), *Geophysics for the Mineral Exploration Geoscientist*, Cambridge University Press (zoneamento de assinaturas geofísicas em depósitos tipo pórfiro e uso conjunto de magnetometria e gamaespectrometria).

<!--
nivel: avancado
palavras_corpo: 1219
mapa_objetivo_secao:
  geologia-avancado-m19-oa02: "Gamaespectrometria: só a pele do terreno, mas informativa sobre alteração" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOMIN-M19-A02-GAMAESPECTROMETRIA-003
    claim: "A gamaespectrometria discrimina potássio (pico de energia 1,46 MeV, do próprio ⁴⁰K, janela padrão IAEA 1,37-1,57 MeV), urânio (medido por equivalência via o pico de 1,76 MeV do bismuto-214, produto da série de decaimento do urânio, janela 1,66-1,86 MeV) e tório (medido por equivalência via o pico de 2,61 MeV do tálio-208, produto da série do tório, janela 2,41-2,81 MeV). As três janelas padrão NÃO são contíguas: há intervalos mortos entre elas (1,57-1,66 e 1,86-2,41 MeV), que reduzem o vazamento de contagens entre canais. O sinal gama detectado é fortemente atenuado pela rocha, vindo predominantemente dos primeiros 30-45 cm de material — o método não detecta radioatividade em profundidade."
    risk: fato
    source: "IAEA (2003), Guidelines for radioelement mapping using gamma ray spectrometry data, IAEA-TECDOC-1363 (janelas de energia espectral padrão KEW 1370-1570 keV, BEW 1660-1860 keV, TEW 2410-2810 keV, e profundidade efetiva de penetração do sinal gama natural). CORREÇÃO LARANJA + AMARELA da auditoria de 2026-09-13: (AUD-M19-A02-JANELASGAMA-002) as três janelas declaradas (1,36-1,60 / 1,60-1,95 / 2,40-2,86) não eram as do documento citado e ainda se tocavam em 1,60 MeV, o que a norma evita deliberadamente; (AUD-M19-A02-TL208-003) o pico do ²⁰⁸Tl, 2,6145 MeV, arredonda para 2,61 e é assim que aparece nos Módulos 15 e 16, ambos já com questionário e baralhos gerados — '2,62' criava contradição transversal."

nota_alegacao_compartilhada: 'GEOMIN-M19-A02-ZONEAMENTOPORFIRO-004 (regra de sinal potassica/filica em magnetometria) permanece declarada na Aula 02 (Parte 1), onde a frase correspondente do corpo esta escrita. O exemplo trabalhado desta aula A APLICA e a exercita, mas nao a redeclara aqui, para nao duplicar claim_id.'

divisao_de_aula:
  data: '2026-09-18'
  origem: 'Antiga Aula 02 unica (Gravimetria, magnetometria e gamaespectrometria), 2.480 palavras de corpo, dividida em duas por decisao do usuario apos achado DID-M19-A02-CARGA-004 (revisao didatica, orange, em aberto). Esta e a METADE 2 (gamaespectrometria + integracao multimetodo), criada como nova Aula 03, empurrando as antigas Aulas 03-06 para 04-07. O ID desta aula (geologia-avancado-m19-a03) e NOVO; o antigo m19-a03 (eletrorresistividade) passou a m19-a04.'
  exemplo_trabalhado_preservado: 'O exemplo trabalhado desta aula E O ORIGINAL da antiga Aula 02, preservado PALAVRA POR PALAVRA (situacao, pergunta, resolucao e conclusao), incluindo a correcao vermelha da auditoria de 2026-09-13 (AUD-M19-A02-PORFIROMAGNETITA-001, que corrigiu a inversao de polaridade potassica/filica). Nao foi movido para a Aula 02 (Parte 1) porque a discriminacao de maior valor do modulo - o canal K nao separa potassica de filica, quem separa e o sinal magnetico - so existe na intersecao entre magnetometria (Aula 02) e gamaespectrometria (esta aula), exatamente como a revisao didatica de 2026-09-13 (open_findings_note de DID-M19-A02-CARGA-004) previu e recomendou caso a divisao fosse feita.'
-->
