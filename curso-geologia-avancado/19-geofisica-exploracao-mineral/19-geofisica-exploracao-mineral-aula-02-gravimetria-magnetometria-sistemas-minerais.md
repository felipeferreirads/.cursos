# Aula 02: Gravimetria e magnetometria na caracterização de sistemas minerais

**ID:** geologia-avancado-m19-a02
**Módulo:** [[19-geofisica-exploracao-mineral-modulo|Módulo 19 — Geofísica aplicada na exploração mineral]]
**Duração estimada:** ~24 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** interpretar dados gravimétricos e magnéticos em termos das propriedades físicas que cada um mede — densidade e susceptibilidade magnética — e relacioná-los à assinatura esperada de fonte, transporte e alteração hidrotermal num sistema mineral.
**Ao final você vai conseguir:** explicar que propriedade física a gravimetria e a magnetometria medem, e citar contrastes típicos de densidade e de susceptibilidade entre minérios/rochas alteradas e a rocha encaixante; distinguir magnetização induzida de magnetização remanente e explicar por que essa distinção complica a interpretação de um mapa aeromagnético; e aplicar a regra de sinal do zoneamento de um pórfiro — qual alteração acrescenta e qual destrói magnetita.
**Pré-requisito:** [[19-geofisica-exploracao-mineral-aula-01-sistemas-minerais-escalas-resolucao-espacial-profundidade-investigacao|Aula 01 deste módulo]] (o paradigma de sistemas minerais e o compromisso resolução×profundidade) e [[16-aerogeofisica/16-aerogeofisica-modulo|Módulo 16 — Introdução à aerogeofísica]], cujos fundamentos de aquisição aérea de campos potenciais esta aula retoma e aplica especificamente à exploração mineral.

## Conteúdo

### Gravimetria: a propriedade física é densidade, e o alvo raramente é o minério em si

A gravimetria mede pequeníssimas variações no campo gravitacional terrestre causadas por variações laterais de **densidade** das rochas em subsuperfície — um corpo mais denso que sua encaixante produz uma anomalia positiva (excesso de massa puxando o gravímetro com um pouco mais de força), um corpo menos denso produz uma anomalia negativa. Em exploração mineral, o contraste de densidade costuma ser considerável: minérios maciços de sulfeto e minérios de óxido de ferro (magnetita, hematita) estão entre as rochas mais densas da crosta.

Aqui há **duas réguas de densidade diferentes, e confundi-las é um erro caro**. A primeira é a do **mineral puro**:

- pirita e pirrotita — 4,5-5,2 g/cm³
- magnetita — 4,9-5,2 g/cm³
- hematita — 4,9-5,3 g/cm³
- calcopirita — em torno de 4,2 g/cm³
- esfalerita — 3,9-4,1 g/cm³
- galena — 7,4-7,6 g/cm³, o extremo da lista

A segunda régua é a do **corpo de minério**, que é a que o gravímetro de fato lê — e ela é sempre menor, porque nenhum corpo real é mineral puro: misturado à ganga (o material sem valor econômico que acompanha o minério), o sulfeto **maciço** costuma chegar ao instrumento como uma rocha de cerca de 3,5-4,5 g/cm³, contra 2,6-2,8 g/cm³ de um granito ou gnaisse típico e 2,7-3,1 g/cm³ de um basalto.

Esse contraste, tipicamente de 1 a 2 g/cm³ no corpo real (e maior ainda em minério de alto teor), é grande o bastante para que corpos de minério maciço de dimensão métrica a decamétrica produzam anomalias gravimétricas mensuráveis mesmo a profundidades de dezenas a poucas centenas de metros — e é por isso que a gravimetria de detalhe (não apenas a regional da Aula 01) segue sendo usada diretamente sobre alvos já identificados, sobretudo em depósitos de sulfeto maciço vulcanogênico (VMS) e em corpos de óxido de ferro-cobre-ouro (IOCG), onde magnetita e/ou sulfetos maciços dominam a massa do corpo.

Mas o uso mais frequente da gravimetria em exploração não é detectar o próprio minério — é mapear as **estruturas de transporte e as unidades hospedeiras** do sistema mineral: o contato entre uma bacia sedimentar (menos densa) e o embasamento cristalino (mais denso) por baixo dela, a presença de uma intrusão máfica ou ultramáfica densa em profundidade que pode ser a fonte de metais, ou uma zona de falha marcada por diferença de densidade entre os blocos que ela separa. Voltando ao vocabulário da Aula 01: a gravimetria frequentemente informa mais sobre **fonte** e **transporte** do que sobre **deposição** — ela mostra onde a arquitetura profunda favorece um sistema mineral, mesmo quando não "vê" o depósito diretamente.

### Magnetometria: susceptibilidade, magnetização induzida e o problema da remanência

A magnetometria mede variações no campo magnético terrestre causadas por variações na **magnetização** das rochas — que tem dois componentes: a **magnetização induzida**, proporcional à **susceptibilidade magnética** da rocha (o quanto ela se magnetiza na presença do campo terrestre atual) e alinhada com o campo de hoje; e a **magnetização remanente**, um "registro fóssil" da magnetização adquirida quando a rocha se formou ou foi reaquecida, que pode apontar numa direção completamente diferente do campo atual se a placa se moveu ou girou desde então (o mesmo fenômeno de paleomagnetismo tratado no Módulo 18).

A susceptibilidade magnética é adimensional no Sistema Internacional e varia, entre os tipos de rocha, ao longo de **mais de cinco ordens de grandeza**. Vale fixar a régua em três degraus, porque é com ela que se lê qualquer mapa aeromagnético:

- **10⁻⁶ a 10⁻⁵** — rochas sedimentares e félsicas, praticamente não magnéticas;
- **10⁻³ a 10⁻²** — rochas máficas comuns;
- **10⁻¹ a valores da ordem da unidade** — rochas com magnetita abundante: formações ferríferas magnetíticas, minério de magnetita, peridotitos serpentinizados.

O teto dessa escala é o próprio mineral: a magnetita pura tem susceptibilidade da ordem de alguns SI (~5). Essa amplitude é justamente o que torna a magnetometria útil em exploração — **os alvos deste módulo vivem no topo da escala, não em 10⁻²**.

Quem ocupa esse topo é uma hierarquia curta de minerais. A **magnetita** é, disparado, o mineral que mais controla a variação: mesmo em proporções pequenas, ela costuma dominar a susceptibilidade total da rocha, porque sua própria susceptibilidade é ordens de grandeza maior que a da maioria dos silicatos. Depois dela vêm as titanomagnetitas e a maghemita (Módulo 15) e, entre os sulfetos, a **pirrotita monoclínica** (Fe₇S₈) — e o qualificador é obrigatório, porque só a fase monoclínica é ferrimagnética; a pirrotita hexagonal é antiferromagnética à temperatura ambiente e não magnetiza a rocha. A pirrotita monoclínica é fortemente magnética e é o sulfeto que mais importa para a magnetometria de exploração, mas com uma particularidade: sua susceptibilidade é sensivelmente dependente da intensidade do campo aplicado, o que torna sua resposta magnética mais variável e mais difícil de modelar de forma simples do que a da magnetita.

Essa dependência da magnetita e da pirrotita monoclínica é o que torna a magnetometria tão útil para mapear **halos de alteração hidrotermal** ao redor de um sistema mineral — não porque o próprio minério de interesse (ouro, cobre) seja magnético, mas porque os processos hidrotermais que o depositaram tipicamente também alteram (destroem ou criam) magnetita na rocha encaixante. Um halo de destruição de magnetita aparece como um "buraco" (baixo magnético) dentro de um fundo regional mais magnético; um halo de pirrotita monoclínica associado a um sistema VMS aparece como alto magnético.

**E o sentido dessa troca não é arbitrário — depende de qual assembleia de alteração agiu.** Num sistema pórfiro, a regra de primeira ordem tem três termos:

- a alteração **potássica** (biotita secundária, feldspato potássico) tipicamente **acrescenta** magnetita hidrotermal e produz um **alto** magnético no núcleo do sistema;
- a alteração **fílica/sericítica** (quartzo-sericita-pirita), mais ácida, é a **destrutiva de magnetita** e produz o **baixo** magnético, tipicamente como um anel envolvendo o núcleo potássico;
- a **propilítica**, mais distal, ocupa uma posição intermediária e pode preservar ou repor magnetita.

Inverter esses dois primeiros é o erro clássico de interpretação, porque ambos aparecem com potássio alto na gamaespectrometria (assunto da próxima aula) — a sericita também é um mineral de potássio. Guarde este ponto: **o canal de K, sozinho, não separa potássica de fílica; quem separa é o sinal magnético**, porque as duas respondem em sentidos opostos. É a discriminação de maior valor deste bloco de aulas, e a Aula 03 a exercita combinando os dois métodos.

Falta a segunda metade anunciada no título desta seção — a **remanência**, que é onde a interpretação mais cobra cuidado. Um corpo com magnetização remanente forte e desalinhada do campo atual pode produzir uma anomalia com forma (dipolo deslocado, polaridade invertida) que confunde um intérprete acostumado a assumir magnetização puramente induzida. O erro clássico de iniciante é tentar ajustar a profundidade e a geometria de um corpo assumindo só magnetização induzida quando o corpo real tem remanência significativa, chegando a uma geometria de corpo fisicamente implausível.

## Exemplo trabalhado

**Situação:** um levantamento aeromagnético sobre um segundo alvo de pórfiro de cobre-ouro — desta vez sem gamaespectrometria disponível — mostra o padrão recíproco do exemplo mais comumente ilustrado na literatura: um alto magnético circular ocupando o núcleo do sistema, cercado por um anel de baixo magnético mais estreito na borda.

**Pergunta:** interprete essa geometria em termos de zoneamento de alteração hidrotermal, e diga a que zona cada uma das duas respostas magnéticas provavelmente corresponde.

**Resolução:**

O **alto magnético central** é consistente com o núcleo de **alteração potássica** preservado — biotita secundária e feldspato potássico com magnetita hidrotermal, que a alteração potássica tipicamente acrescenta. O **anel de baixo magnético** que o envolve é consistente com o invólucro de **alteração fílica/sericítica** (quartzo-sericita-pirita), que destrói a magnetita primária e a hidrotermal e por isso produz o baixo, tipicamente em forma anelar.

Essa configuração — alto no núcleo potássico cercado por anel de baixo fílico — é a recíproca exata do padrão discutido no corpo desta aula (baixo central cercado por anel de alto), mas obedece à mesma regra de sinal: **potássica acrescenta magnetita, fílica destrói**. O que muda de um sistema para outro não é a regra, é qual zona domina espacialmente a área levantada.

**Conclusão:** só com o dado magnético já é possível propor um zoneamento de alteração plausível, porque é o **sinal** (alto ou baixo) — não a posição relativa (centro ou anel) — que carrega a informação de qual alteração agiu. O que a magnetometria sozinha não permite é confirmar a mineralogia real da alteração exposta na superfície, nem discriminar com segurança potássica de fílica no caso (menos comum, mas possível) de as duas produzirem respostas magnéticas parecidas. Para isso, a Aula 03 acrescenta a gamaespectrometria — e mostra por que ela, sozinha, também não resolve essa discriminação.

## Recap relâmpago

- A **gravimetria** mede contrastes de **densidade**; os minerais de minério são densos (pirita e pirrotita 4,5-5,2 g/cm³, magnetita 4,9-5,2, hematita 4,9-5,3, calcopirita ~4,2, esfalerita 3,9-4,1, galena 7,4-7,6 g/cm³), e um corpo de sulfeto **maciço** real, já misturado à ganga, chega ao gravímetro em torno de 3,5-4,5 g/cm³, contra 2,6-2,8 g/cm³ de granitos/gnaisses e 2,7-3,1 g/cm³ de basaltos — mas o uso mais comum da gravimetria em exploração é mapear estruturas de fonte e transporte (contatos, intrusões densas, falhas), não só o próprio minério.
- A **magnetometria** mede **magnetização**, com dois componentes: **induzida** (proporcional à susceptibilidade magnética, alinhada ao campo atual) e **remanente** (registro fóssil, pode apontar em direção diferente) — a susceptibilidade cobre mais de cinco ordens de grandeza (de ~10⁻⁶ em sedimentares e félsicas a ~10⁻¹ e valores da ordem da unidade em rochas ricas em magnetita; a magnetita pura, ~5 SI), dominada sobretudo por magnetita, com a **pirrotita monoclínica** (Fe₇S₈ — só essa fase é ferrimagnética) magnética mas de resposta mais variável, dependente do campo aplicado.
- Halos de **destruição** ou **criação de magnetita** por alteração hidrotermal, não o minério de interesse em si, costumam ser o que a magnetometria de exploração realmente detecta ao redor de um sistema mineral — e o sentido importa: em pórfiros, a alteração **potássica acrescenta** magnetita (alto magnético) e a **fílica/sericítica destrói** (baixo magnético, tipicamente anelar). É o sinal (não a posição relativa) que identifica qual alteração agiu.

## Próxima aula

[[19-geofisica-exploracao-mineral-aula-03-gamaespectrometria-integracao-sistemas-minerais|Aula 03 — Gamaespectrometria e integração de assinaturas geofísicas em sistemas minerais]] — o terceiro método de campo potencial/radiométrico deste bloco, e por que ele, combinado com a regra de sinal magnética desta aula, resolve uma ambiguidade que nenhum dos dois métodos resolve sozinho.

## Fontes

- Telford, W. M., Geldart, L. P. & Sheriff, R. E. (1990), *Applied Geophysics*, 2nd ed., Cambridge University Press (tabelas de densidade e susceptibilidade magnética de minerais e rochas comuns).
- Clark, D. A. (1997), "Magnetic petrophysics and magnetic petrology: aids to geological interpretation of magnetic surveys", *AGSO Journal of Australian Geology & Geophysics*, 17(2), 83-103 (magnetização induzida versus remanente, papel da magnetita e da pirrotita monoclínica).
- Clark, D. A. (2014), "Magnetic effects of hydrothermal alteration in porphyry copper and iron-oxide copper-gold systems: A review", *Tectonophysics*, 624-625, 46-65, DOI 10.1016/j.tecto.2013.12.011 (qual zona de alteração acrescenta e qual destrói magnetita em sistemas pórfiro, e a assinatura magnética anelar resultante).
- Sillitoe, R. H. (2010), "Porphyry Copper Systems", *Economic Geology*, 105(1), 3-41 (zoneamento de alteração potássica-fílica-propilítica-argílica avançada em sistemas pórfiro).

<!--
nivel: avancado
palavras_corpo: 1702
mapa_objetivo_secao:
  geologia-avancado-m19-oa02: "Gravimetria: a propriedade física é densidade, e o alvo raramente é o minério em si" + "Magnetometria: susceptibilidade, magnetização induzida e o problema da remanência" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOMIN-M19-A02-DENSIDADES-001
    claim: "Densidades dos minerais de minério: pirita e pirrotita 4,5-5,2 g/cm³; magnetita 4,9-5,2; hematita 4,9-5,3; calcopirita ~4,2; esfalerita 3,9-4,1; galena 7,4-7,6 g/cm³. Um corpo de sulfeto MACIÇO real, já misturado à ganga, tem densidade de rocha tipicamente entre 3,5 e 4,5 g/cm³, contra 2,6-2,8 g/cm³ de granito/gnaisse típico e 2,7-3,1 g/cm³ de basalto — contraste suficiente para produzir anomalias gravimétricas mensuráveis em corpos de dimensão métrica a decamétrica a profundidades de dezenas a poucas centenas de metros."
    risk: aproximacao
    source: "Telford, Geldart & Sheriff (1990), Applied Geophysics, 2nd ed., Cambridge University Press, tabelas de densidade de minerais e rochas; tabela de densidades de rochas portadoras de minério do GPG (gpg.geosci.xyz): pirita/pirrotita 4,50-5,20; magnetita 4,90-5,20; hematita 4,90-5,30; galena 7,40-7,60 g/cm³. CORREÇÃO LARANJA da auditoria de 2026-09-13 (AUD-M19-A02-DENSIDADESULFETO-004): a redação original dava a faixa 4,2-5,0 g/cm³ para 'sulfetos maciços' enumerando cinco minerais dos quais DOIS ficam fora dela — a galena (7,4-7,6) por muito acima e a esfalerita (3,9-4,1) por baixo —, e confundia densidade de MINERAL com densidade do CORPO de minério, que é menor por causa da ganga."
  - claim_id: GEOMIN-M19-A02-SUSCEPTIBILIDADE-002
    claim: "A susceptibilidade magnética (adimensional, SI) das rochas varia por MAIS DE CINCO ordens de grandeza: ~10⁻⁶ a 10⁻⁵ em sedimentares e félsicas pouco magnéticas, 10⁻³ a 10⁻² em máficas comuns, e 10⁻¹ a valores da ordem da unidade em rochas ricas em magnetita (formação ferrífera magnetítica, minério de magnetita, peridotito serpentinizado); o próprio mineral magnetita tem susceptibilidade da ordem de alguns SI (~5). A magnetita domina a susceptibilidade total mesmo em proporções pequenas na rocha; depois dela vêm titanomagnetitas e maghemita (Módulo 15) e, entre os sulfetos, a pirrotita MONOCLÍNICA (Fe7S8) - só essa fase é ferrimagnética, a hexagonal é antiferromagnética a temperatura ambiente. A susceptibilidade da pirrotita monoclínica é sensivelmente dependente da intensidade do campo aplicado, tornando sua resposta mais variável do que a da magnetita."
    risk: aproximacao
    source: "Clark (1997), AGSO Journal of Australian Geology & Geophysics, 17(2), 83-103; Clark & Emerson (1991), 'Notes on rock magnetization characteristics in applied geophysical studies', Exploration Geophysics, 22(4); tabela de susceptibilidade do GPG (gpg.geosci.xyz): magnetita 5,8 SI, pirrotita 1,5 SI, hematita 6,5x10⁻³ SI. DUAS CORREÇÕES LARANJAS da auditoria de 2026-09-13: (AUD-M19-A02-SUSCEPTIBILIDADE-005) o teto declarado de 10⁻² subestimava a escala em cerca de duas ordens de grandeza e excluía justamente os alvos magnetíticos deste módulo; (AUD-M19-A02-PIRROTITA-006) 'pirrotita' sem qualificador de fase repetia o defeito já corrigido no Módulo 16 (AUD-M16-A05-PIRROTITA-Y04) contra a distinção que o Módulo 15 faz, e a ordenação 'segundo mineral mais relevante, atrás apenas da magnetita' contradizia a ordem estabelecida no Módulo 15 (titanomagnetitas, maghemita, pirrotita monoclínica)."
  - claim_id: GEOMIN-M19-A02-ZONEAMENTOPORFIRO-004
    claim: "Em depósitos tipo pórfiro, a alteração POTÁSSICA (biotita secundária, feldspato potássico) tipicamente ACRESCENTA magnetita hidrotermal e produz ALTO magnético, enquanto a alteração FÍLICA/SERICÍTICA (quartzo-sericita-pirita), mais ácida, é a destrutiva de magnetita e produz BAIXO magnético, tipicamente como anel envolvendo o núcleo potássico; a propilítica, distal, preserva ou repõe magnetita. AMBAS, potássica e fílica, dão alto no canal K da gamaespectrometria (a sericita é uma mica potássica), de modo que o canal K sozinho NÃO as distingue - quem distingue é o sinal magnético, porque as duas respondem em sentidos opostos. Zonas argílica/propilítica mais distais tendem a lixiviar K e apresentar razão K/Th relativamente mais baixa (Th geoquimicamente mais imóvel)."
    risk: fato
    source: "Clark, D. A. (2014), 'Magnetic effects of hydrothermal alteration in porphyry copper and iron-oxide copper-gold systems: A review', Tectonophysics, 624-625, 46-65, DOI 10.1016/j.tecto.2013.12.011 - zona potássica interna mineralizada e RICA em magnetita, envolvida por um invólucro de alteração fílica DESTRUTIVA de magnetita e de susceptibilidade muito baixa, com a assinatura de campo tipicamente descrita como alto magnético cercado por baixo anelar (donut); Sillitoe (2010), 'Porphyry Copper Systems', Economic Geology 105(1), 3-41; Dentith & Mudge (2014), Geophysics for the Mineral Exploration Geoscientist, Cambridge University Press. CORREÇÃO VERMELHA da auditoria de 2026-09-13 (AUD-M19-A02-PORFIROMAGNETITA-001): a redação original INVERTIA o sinal, atribuindo a destruição de magnetita à alteração potássica. Apresentado como padrão típico de zoneamento, não como assinatura universal - a resposta real varia com a mineralogia de alteração dominante, o grau de sobreposição fílica e o nível de erosão."

divisao_de_aula:
  data: '2026-09-18'
  origem: 'Antiga Aula 02 unica (Gravimetria, magnetometria e gamaespectrometria), 2.480 palavras de corpo, dividida em duas por decisao do usuario apos achado DID-M19-A02-CARGA-004 (revisao didatica, orange, em aberto) ter deixado a decisao explicitamente encaminhada e sem recomendacao fechada. Esta e a METADE 1 (campos potenciais: gravimetria + magnetometria), mantendo o ID a02. A METADE 2 (gamaespectrometria + integracao) passou a ser a nova Aula 03, empurrando as antigas Aulas 03-06 para 04-07.'
  exemplo_trabalhado_novo: 'O exemplo trabalhado original (zoneamento de porfiro cruzando magnetometria com gamaespectrometria) foi INTEIRO preservado, sem alteracao de uma palavra, na Aula 03 (gamaespectrometria), porque a discriminacao de maior valor do modulo - o canal K nao separa potassica de filica, quem separa e o sinal magnetico - so existe na intersecao dos dois metodos (ver open_findings_note da revisao didatica). Esta Aula 02 (Parte 1) recebeu um exemplo trabalhado NOVO, criado para esta divisao: interpreta o padrao RECIPROCO (alto magnetico central cercado por anel de baixo) usando SOMENTE dado magnetico. NAO E ALEGACAO FACTUAL NOVA - e a aplicacao qualitativa, sem nenhum valor numerico novo, da mesma regra de sinal ja auditada (GEOMIN-M19-A02-ZONEAMENTOPORFIRO-004) e da mesma frase ja presente no corpo original ("a configuracao mais comumente ilustrada na literatura e a reciproca: alto magnetico no nucleo potassico cercado por um anel de baixo magnetico filico"), apenas reorganizada em formato de situacao-pergunta-resolucao. Nenhuma fonte nova foi consultada para constru-lo. Fica sinalizado para o usuario decidir se quer mandar ao auditor-cientifico para checagem pontual, como foi feito no M17 e no M18.
-->
