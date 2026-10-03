# Aula 02: Conceitos básicos de geocronologia aplicados — minerais datáveis e os sistemas U-Pb, Rb-Sr, Sm-Nd e Lu-Hf

**ID:** geologia-avancado-m27-a02
**Módulo:** [[27-petrocronologia-modulo|Módulo 27 — Introdução à petrocronologia]]
**Duração estimada:** ~29 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** organizar, sob a ótica da petrocronologia, os sistemas isotópicos já vistos no Módulo 26 — não pelo par pai-filho em si, mas por qual mineral cada sistema data e que janela de temperatura essa combinação mineral-sistema abre na história de uma rocha.
**Ao final você vai conseguir:** listar os principais minerais datáveis por U-Pb, Rb-Sr, Sm-Nd e Lu-Hf; posicionar cada combinação mineral-sistema numa escala aproximada de temperatura de fechamento; e explicar por que a mesma rocha, datada por sistemas diferentes, pode legitimamente produzir idades diferentes sem que nenhuma delas esteja "errada".
**Pré-requisito:** [[27-petrocronologia-aula-01-o-que-e-petrocronologia|Aula 01]] (o que significa ancorar uma idade em textura e composição) e Módulo 26 completo (mecânica dos sistemas U-Pb, Rb-Sr, Sm-Nd; conceito de temperatura de fechamento de Dodson).

## Conteúdo

### Do sistema isotópico ao mineral hospedeiro

No Módulo 26 você aprendeu a mecânica de cada sistema isotópico — a equação da isócrona, a constante de decaimento, como calcular uma idade. A petrocronologia parte do mesmo arsenal, mas reorganiza a pergunta: em vez de "qual é a idade desta rocha pelo sistema X", pergunta "que mineral, nesta rocha, carrega o sistema X em concentração suficiente para dar uma idade útil, e o que a temperatura de fechamento **daquele mineral especificamente** significa para a história registrada". Essa mudança de eixo — do sistema isotópico para o mineral hospedeiro — é o que torna possível datar vários eventos de uma mesma rocha com vários minerais, cada um funcionando como um relógio que trava (fecha) numa temperatura diferente à medida que a rocha esfria ou que a reação avança.

O princípio por trás disso é a temperatura de fechamento de Dodson (1973): um sistema isotópico começa a acumular filho radiogênico de forma mensurável (ou seja, "fecha") na temperatura em que a difusão do elemento filho no retículo cristalino do mineral hospedeiro se torna lenta o bastante para não escapar do grão em tempo geológico. Minerais diferentes retêm o filho radiogênico de forma diferente mesmo para o mesmo sistema isotópico — é por isso que a temperatura de fechamento é uma propriedade da combinação **mineral + sistema**, não do sistema isotópico isoladamente.

### U-Pb: o sistema com mais minerais hospedeiros

O sistema U-Pb (e o Th-Pb associado) é o mais versátil da petrocronologia porque um número relativamente grande de minerais acessórios aceita urânio e/ou tório na sua estrutura em concentrações datáveis, e esses minerais têm temperaturas de fechamento de Pb muito diferentes entre si — o que permite, em princípio, amostrar uma mesma rocha em vários pontos de sua história térmica:

- **Zircão (ZrSiO₄).** Temperatura de fechamento de Pb extremamente alta — a difusão de Pb no zircão é tão lenta que, na prática, o sistema não é reaberto por difusão térmica em condições crustais comuns; só temperaturas superiores a ~900 °C (e tempos geológicos longos) chegam a mobilizar Pb de forma mensurável (Cherniak & Watson, 2001). Na prática, isso significa que uma idade U-Pb de zircão quase sempre registra um evento de **cristalização** (crescimento novo ou recristalização), não um resfriamento — reforçando o ponto da Aula 01 de que a idade do zircão é, antes de mais nada, uma idade de crescimento a ser lida junto com a textura.
- **Monazita ((LREE,Th)PO₄).** Historicamente tratada como tendo fechamento por volta de 700-750 °C, com base em estudos de campo (Copeland et al., 1988; Parrish, 1990), mas trabalhos experimentais de difusão mais recentes (Cherniak et al., 2004) sugerem que a perda de Pb por difusão é, na prática, desprezível até temperaturas bem mais altas (bem acima de 800 °C, dependendo do tamanho do grão e da taxa de resfriamento) — o que aproxima a monazita do comportamento do zircão: majoritariamente um registrador de **crescimento/recristalização** ligado a reação, e não um simples termômetro de resfriamento. Você vai explorar essa faceta a fundo na Aula 06.
- **Titanita (CaTiSiO₅, também chamada esfeno).** Fechamento de Pb intermediário a alto, tipicamente discutido em torno de ~650-700 °C, embora estimativas variem conforme o método e o tamanho de grão (Cherniak, 1993; Kohn & Corrie, 2011 sugerem valores ainda mais altos em alguns contextos). Cresce ao longo de uma faixa ampla de temperatura em rochas metamórficas e ígneas, o que a torna um mineral petrocronológico particularmente versátil — tema retomado na Aula 06.
- **Rutilo (TiO₂).** Fechamento mais baixo, hoje estimado em torno de ~600-640 °C para grãos de 100-200 μm resfriados a poucos °C por milhão de anos (Cherniak, 2000) — valor revisado para cima em relação a estimativas de campo mais antigas. É, portanto, um cronômetro de temperatura intermediária, útil para datar o resfriamento pós-pico metamórfico, e ainda carrega um termômetro independente próprio (Zr-em-rutilo), explorado na Aula 06.
- **Apatita (Ca₅(PO₄)₃(F,Cl,OH)).** Fechamento de Pb mais baixo entre os minerais U-Pb comuns, em torno de ~450-550 °C (a depender da composição e do tamanho de grão; Chamberlain & Bowring, 2001), tornando-a útil como cronômetro de temperatura relativamente baixa — mais próxima do domínio da termocronologia clássica que do crescimento mineral de alta temperatura.

Note o padrão: dentro de um único sistema isotópico (U-Pb), a escolha do mineral hospedeiro já define, sozinha, se a idade resultante tende a registrar um evento de cristalização de alta temperatura (zircão, monazita), um evento de temperatura intermediária (titanita, rutilo) ou um resfriamento de temperatura mais baixa (apatita). É essa hierarquia de minerais, todos rodando o mesmo par pai-filho, que permite reconstruir uma sequência temporal dentro de uma única rocha — o núcleo do método que a Aula 07 vai amarrar num caminho P-T-tempo completo.

### Sm-Nd e Lu-Hf: a granada como cronômetro

Diferente do U-Pb, que se apoia em vários minerais acessórios, os sistemas Sm-Nd e Lu-Hf aplicados à petrocronologia se apoiam quase inteiramente num único mineral maior: a **granada**. A granada incorpora samário e neodímio (moderadamente) e, de forma muito mais marcante, lutécio e itérbio — os elementos terras-raras pesados — em concentrações bem mais altas que os minerais que a rodeiam, criando um forte contraste geoquímico entre a granada e a rocha total que é exatamente o que uma isócrona precisa (Módulo 26, Aula 04).

- **Sm-Nd granada-rocha total.** A granada incorpora Sm e Nd moderadamente, com fracionamento Sm/Nd suficiente, em geral, para construir uma isócrona granada-rocha total (às vezes com uma segunda fase, como piroxênio, agregada para melhorar o espalhamento de pontos). A temperatura de fechamento é relativamente alta, mas depende fortemente do tamanho do grão e da taxa de resfriamento — estimativas na faixa de ~600-750 °C são comuns na literatura (Mezger et al., 1992, estimaram ~600 ± 30 °C para granadas milimétricas a centimétricas de terrenos de resfriamento lento; Ganguly & Tirone, 1999, formalizaram como esse valor sobe com o tamanho do grão e a taxa de resfriamento), o que quer dizer que uma idade Sm-Nd de granada pode registrar tanto o crescimento quanto, em rochas de resfriamento lento, uma mistura entre crescimento e reequilíbrio difusivo posterior — uma ambiguidade que a Aula 07 discute com mais profundidade.
- **Lu-Hf granada-rocha total.** O lutécio se comporta como elemento terra-rara pesado altamente compatível na granada, entrando em concentrações desproporcionalmente mais altas que em qualquer outro mineral formador de rocha (só acessórios como zircão e xenotima têm teores ainda maiores, mas em quantidade modal ínfima — e é por isso que inclusões de zircão, ricas em Hf, contaminam isócronas Lu-Hf de granada) — um contraste Lu/Hf entre granada e rocha total tipicamente maior que o contraste Sm/Nd equivalente, o que produz isócronas mais precisas e mais robustas (Scherer, Cameron & Blichert-Toft, 2000). Mais importante para a petrocronologia: a difusão de Hf na granada é suficientemente lenta para que a temperatura de fechamento do sistema Lu-Hf na granada seja, na prática, mais alta que a do Sm-Nd na mesma granada — o que significa que, quando os dois sistemas são medidos no mesmo cristal e dão idades diferentes, essa diferença não é erro: é informação sobre a taxa de resfriamento e sobre o quanto cada sistema resistiu à reabertura difusiva depois do crescimento (Scherer et al., 2000; discutido com mais detalhe na Aula 07).

Um ponto que vale reter aqui, mesmo antes da Aula 07: como o lutécio se concentra fortemente nas partes do cristal que crescem primeiro (o núcleo de uma granada zonada tende a "sequestrar" Lu de forma desproporcional durante o crescimento, tema da Aula 07), uma idade Lu-Hf de granada tende a enviesar-se para os estágios **iniciais** do crescimento do cristal, enquanto uma idade Sm-Nd, menos concentrada no núcleo, tende a refletir uma média ponderada de um intervalo maior do crescimento. Dois sistemas, um só mineral, duas janelas temporais diferentes dentro do mesmo evento de crescimento.

### Rb-Sr em micas: o registro mais "frio"

O sistema Rb-Sr (Módulo 26, Aula 03), quando aplicado a micas — biotita e muscovita —, ocupa o extremo de temperatura mais baixa deste conjunto de ferramentas. O rubídio substitui o potássio na estrutura das micas em concentrações relativamente altas, mas a temperatura de fechamento do Rb-Sr em biotita é baixa, tipicamente estimada perto de ~300-350 °C, e em muscovita um pouco mais alta, perto de ~450-500 °C (valores clássicos revisados por diferentes autores; a faixa exata depende de tamanho de grão e taxa de resfriamento, como sempre neste tipo de estimativa). Isso torna o par biotita-muscovita um cronômetro de resfriamento profundo, útil sobretudo para amarrar a extremidade final e mais fria de um caminho P-T-tempo — o oposto do papel do zircão e da monazita, que amarram a extremidade mais quente. O sistema K-Ar/Ar-Ar, já mencionado no Módulo 26, ocupa um papel semelhante nas mesmas micas, com temperaturas de fechamento na mesma ordem de grandeza.

### Por que idades diferentes da mesma rocha não competem entre si

Um erro comum de quem está começando em petrocronologia é tratar idades diferentes obtidas de uma mesma amostra como um problema a resolver — como se apenas uma pudesse estar "certa". A tabela abaixo resume por que isso normalmente não é o caso: cada combinação mineral-sistema tende a fechar (ou a crescer, no caso de zircão e monazita) numa janela de temperatura diferente, e o conjunto das idades, lido em ordem, **é** a história térmica e petrológica da rocha, não uma contradição a arbitrar.

| Mineral | Sistema | Temperatura aproximada de fechamento/crescimento | O que tende a registrar |
|---|---|---|---|
| Zircão | U-Pb | Sem fechamento difusivo relevante até ~900 °C | Cristalização/recristalização (idade de crescimento) |
| Monazita | U-Pb, Th-Pb | Difusão desprezível até temperaturas altas (>800 °C em muitos casos) | Crescimento/recristalização ligado a reação |
| Granada | Lu-Hf | Fechamento relativamente alto, mais alto que Sm-Nd na mesma granada | Estágios iniciais do crescimento (núcleo) |
| Titanita | U-Pb | ~650-700 °C (estimativas variam) | Crescimento em ampla faixa de T; às vezes resfriamento |
| Granada | Sm-Nd | ~600-750 °C (depende de tamanho de grão/taxa de resfriamento) | Crescimento, com possível mistura por difusão posterior |
| Rutilo | U-Pb | ~600-640 °C | Resfriamento pós-pico (intermediário) |
| Apatita | U-Pb | ~450-550 °C | Resfriamento (temperatura moderada) |
| Muscovita | Rb-Sr, Ar-Ar | ~450-500 °C (Rb-Sr); similar em ordem de grandeza no Ar-Ar | Resfriamento |
| Biotita | Rb-Sr, Ar-Ar | ~300-350 °C | Resfriamento profundo (fim do caminho P-T-t) |

Os valores desta tabela são **aproximações de referência da literatura**, não constantes universais: a temperatura de fechamento real de um grão depende do seu tamanho, da geometria de difusão, da taxa de resfriamento e, em alguns casos, da composição do próprio mineral — por isso a petrocronologia sempre cita a fonte experimental ou de calibração por trás de cada número, nunca trata a temperatura de fechamento como um valor fixo de tabela a ser aplicado sem crítica.

## Exemplo trabalhado: cinco idades, uma história térmica

**Situação.** Um granulito de alto grau foi datado por cinco combinações mineral-sistema diferentes: zircão U-Pb, 620 ± 5 Ma; monazita U-Pb, 615 ± 6 Ma; granada Lu-Hf, 610 ± 8 Ma; titanita U-Pb, 590 ± 7 Ma; e biotita Rb-Sr, 560 ± 10 Ma. Um leitor apressado poderia perguntar: "qual dessas é a idade 'certa' da rocha?"

**Leitura petrocronológica.** A pergunta certa não é qual idade está certa, e sim que trecho da história cada uma amarra. O zircão (620 Ma) e a monazita (615 Ma), ambos essencialmente livres de reabertura difusiva até temperaturas muito altas, registram — dentro do erro analítico, quase coincidentes — o evento de cristalização/recristalização metamórfica de alta temperatura, provavelmente o próprio pico metamórfico ou um evento muito próximo dele. A granada por Lu-Hf (610 Ma), levemente mais jovem, é consistente com registrar preferencialmente o início do crescimento do cristal (o núcleo, mais rico em Lu), ligeiramente antes ou durante o mesmo evento de alta temperatura. A titanita (590 Ma) já é sensivelmente mais jovem — 30 milhões de anos depois do zircão — e, com fechamento em torno de 650-700 °C, provavelmente registra um ponto já no resfriamento pós-pico, quando a rocha passou por essa temperatura intermediária. A biotita por Rb-Sr (560 Ma), a mais jovem de todas, com fechamento em torno de 300-350 °C, fecha a sequência: 60 milhões de anos depois do pico metamórfico, a rocha finalmente esfriou abaixo dessa temperatura mais baixa. (Por que biotita e não muscovita? Num granulito, a muscovita não é estável no pico — reage com o quartzo antes da fácies granulito —, e uma muscovita encontrada ali seria retrógrada: teria crescido abaixo da sua temperatura de fechamento e dataria o próprio crescimento, não a passagem da rocha por 450-500 °C.)

**Conclusão.** As cinco idades não competem — elas se **encadeiam**, do evento de mais alta temperatura (zircão/monazita, ~615-620 Ma) ao de mais baixa (biotita, ~560 Ma), traçando 60 milhões de anos de resfriamento progressivo. É exatamente esse tipo de sequência, construída com múltiplos minerais e múltiplos sistemas isotópicos na mesma rocha, que permite reconstruir uma taxa de resfriamento — e é esse raciocínio, generalizado para incluir também a posição P-T de cada mineral (não só sua temperatura de fechamento), que a Aula 07 formaliza como interpretação integrada de um caminho P-T-tempo.

## Recap relâmpago

- A petrocronologia reorganiza os sistemas isotópicos do Módulo 26 em torno do mineral hospedeiro: a mesma combinação sistema + mineral define uma temperatura de fechamento própria, diferente de outras combinações do mesmo sistema em outro mineral.
- No sistema U-Pb, zircão e monazita praticamente não fecham por difusão em condições crustais comuns (registram crescimento/recristalização); titanita fecha em temperatura intermediária-alta; rutilo em temperatura intermediária; apatita na temperatura mais baixa do grupo.
- Sm-Nd e Lu-Hf aplicados à petrocronologia se apoiam sobretudo na granada; o Lu-Hf tende a fechar em temperatura mais alta que o Sm-Nd na mesma granada e a enviesar-se para os estágios iniciais do crescimento do cristal, por causa da forte concentração de Lu no núcleo.
- Rb-Sr (e Ar-Ar) em muscovita e biotita ocupam o extremo de temperatura mais baixa, registrando o fim de um caminho de resfriamento, com biotita fechando em temperatura mais baixa que muscovita.
- Idades diferentes de sistemas/minerais diferentes na mesma rocha normalmente não competem: lidas em conjunto, do mineral de fechamento mais alto ao mais baixo, elas reconstroem uma sequência temporal e uma taxa de resfriamento — o esqueleto de um caminho P-T-tempo.

## Próxima aula

[[27-petrocronologia-aula-03-tecnicas-analiticas-imageamento|Aula 03 — Técnicas analíticas e de imageamento]]: como medir essas idades e essas composições dentro de domínios específicos de um cristal — LA-ICP-MS, SIMS, TIMS, microssonda eletrônica (EPMA) e MEV, com suas resoluções espaciais e limitações próprias.

## Fontes

- Dodson, M. H. (1973), "Closure temperature in cooling geochronological and petrological systems", *Contributions to Mineralogy and Petrology*, 40, 259-274.
- Cherniak, D. J. & Watson, E. B. (2001), "Pb diffusion in zircon", *Chemical Geology*, 172, 5-24. VERIFICADO por busca nesta redação (2026-09-22): relação de Arrhenius e conclusão de baixíssima mobilidade de Pb confirmadas (ADS, ScienceDirect).
- Cherniak, D. J., Watson, E. B., Grove, M. & Harrison, T. M. (2004), "Pb diffusion in monazite: a combined RBS/SIMS study", *Geochimica et Cosmochimica Acta*, 68, 829-840 — estimativa experimental de temperatura de fechamento de Pb em monazita superior a 900 °C para grãos de 10 μm resfriados a 10 °C/Ma. Paginação conferida no Crossref pela auditoria (2026-09-22), doi:10.1016/j.gca.2003.07.012.
- Copeland, P., Parrish, R. R. & Harrison, T. M. (1988), "Identification of inherited radiogenic Pb in monazite and its implications for U-Pb systematics", *Nature*, 333, 760-763 — estimativa de campo de fechamento de Pb em monazita (~720-750 °C). Paginação conferida no Crossref pela auditoria (2026-09-22), doi:10.1038/333760a0.
- Parrish, R. R. (1990), "U-Pb dating of monazite and its application to geological problems", *Canadian Journal of Earth Sciences*, 27, 1431-1450, doi:10.1139/e90-152 — estimativa de campo de fechamento de Pb em monazita (~725 ± 25 °C). Acrescentado pela auditoria (2026-09-22): era citado no corpo e faltava aqui.
- Cherniak, D. J. (1993), "Lead diffusion in titanite and preliminary results on the effects of radiation damage on Pb transport", *Chemical Geology*, 110, 177-194 — referência clássica de difusão de Pb em titanita. Paginação conferida no Crossref pela auditoria (2026-09-22), doi:10.1016/0009-2541(93)90253-F.
- Kohn, M. J. & Corrie, S. L. (2011), "Preserved Zr-temperatures and U-Pb ages in high-grade metamorphic titanite: Evidence for a static hot channel in the Himalayan orogen", *Earth and Planetary Science Letters*, 311, 136-143, doi:10.1016/j.epsl.2011.09.008 — titanita que retém idades U-Pb e temperaturas de Zr em alto grau. Acrescentado pela auditoria (2026-09-22): era citado no corpo e faltava aqui.
- Cherniak, D. J. (2000), "Pb diffusion in rutile", *Contributions to Mineralogy and Petrology*, 139, 198-207. VERIFICADO por busca nesta redação (2026-09-22): relação de Arrhenius, faixa experimental (700-1100 °C) e temperatura de fechamento revisada (~600-640 °C) confirmadas (ADS, Springer).
- Chamberlain, K. R. & Bowring, S. A. (2001), "Apatite-feldspar U-Pb thermochronometer: a reliable, mid-range (~450 °C), diffusion-controlled system", *Chemical Geology*, 172, 173-200. VERIFICADO por busca nesta redação (2026-09-22): título e valor de referência (~450 °C) confirmados (ResearchGate, Academia.edu).
- Scherer, E. E., Cameron, K. L. & Blichert-Toft, J. (2000), "Lu-Hf garnet geochronology: closure temperature relative to the Sm-Nd system and the effects of trace mineral inclusions", *Geochimica et Cosmochimica Acta*, 64, 3413-3432. VERIFICADO por busca nesta redação (2026-09-22): título, volume e paginação confirmados (ADS, ScienceDirect).
- Ganguly, J. & Tirone, M. (1999), "Diffusion closure temperature and age of a mineral with arbitrary extent of diffusion: theoretical formulation and applications", *Earth and Planetary Science Letters*, 170, 131-140 — referência de fechamento de Sm-Nd em granada dependente de tamanho de grão e taxa de resfriamento. Paginação conferida no Crossref pela auditoria (2026-09-22), doi:10.1016/S0012-821X(99)00089-8.
- Mezger, K., Essene, E. J. & Halliday, A. N. (1992), "Closure temperatures of the Sm-Nd system in metamorphic garnets", *Earth and Planetary Science Letters*, 113, 397-409, doi:10.1016/0012-821X(92)90141-H — fechamento de Sm-Nd em granada de ca. 600 ± 30 °C em granadas de 0,1-5 cm de terrenos de resfriamento lento. Acrescentado pela auditoria (2026-09-22): era citado no corpo e faltava aqui; valor conferido no resumo original.

<!--
nivel: avancado
palavras_corpo: 2451
palavras_corpo_metodo: "tokens separados por espaco entre '## Conteudo' e '## Fontes', incluindo tabela, seguindo a convencao do modulo 26."
duracao_estimada_min: 29

mapa_objetivo_secao:
  geologia-avancado-m27-oa01: "Do sistema isotopico ao mineral hospedeiro" + "U-Pb: o sistema com mais minerais hospedeiros" + "Sm-Nd e Lu-Hf: a granada como cronometro" + "Rb-Sr em micas: o registro mais 'frio'" + "Por que idades diferentes da mesma rocha nao competem entre si" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: PETROCRON-M27-A02-ZIRCAO-FECHAMENTO-001
    claim: "A difusao de Pb no ziracao e tao lenta que o sistema U-Pb do ziracao nao e reaberto por difusao termica em condicoes crustais comuns; apenas temperaturas acima de aproximadamente 900 C, em tempos geologicos longos, mobilizam Pb de forma mensuravel."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-22): Cherniak & Watson (2001), Chemical Geology 172, 5-24, relacao de Arrhenius D=1,1x10^-1 exp(-550+/-30 kJ/mol/RT) m2/s no intervalo 1000-1500 C, e conclusao de que razoes isotopicas de Pb nao sao alteradas por difusao em volume em condicoes geologicas comuns."
  - claim_id: PETROCRON-M27-A02-MONAZITA-FECHAMENTO-002
    claim: "Estimativas de campo classicas situam o fechamento de Pb em monazita perto de 700-750 C (Copeland et al. 1988, Parrish 1990); trabalho experimental mais recente (Cherniak et al. 2004) sugere temperaturas de fechamento mais altas, ultrapassando 900 C para graos pequenos com taxa de resfriamento de 10 C/Ma."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-22): resultado de busca cita 'Copeland et al. (1988) estimated a closure temperature of Pb in monazite at 720-750C for 10-100 micron crystals cooled at 20C/Ma'; 'Parrish (1990) suggested a closure temperature of 725+/-25C'; 'Cherniak et al. (2004) found higher closure temperatures... in excess of 900C, given a cooling rate of 10C/Ma'."
  - claim_id: PETROCRON-M27-A02-TITANITA-FECHAMENTO-003
    claim: "A titanita tem fechamento de Pb intermediario a alto, discutido tipicamente em torno de 650-700 C, com variacao conforme metodo e tamanho de grao."
    risk: fato
    source: "Cherniak, D.J. (1993), Chemical Geology 110, 177-194 (difusao de Pb em titanita); Kohn, M.J. & Corrie, S.L. (2011) sugerem valores mais altos em alguns contextos. AUDITORIA (2026-09-22): Cherniak 1993 e Kohn & Corrie 2011 (EPSL 311, 136-143) conferidos no Crossref; Kohn & Corrie acrescentado as Fontes (achado 4). A faixa 650-700 C e apresentada como 'estimativas variam', o que e correto."
  - claim_id: PETROCRON-M27-A02-RUTILO-FECHAMENTO-004
    claim: "O fechamento de Pb no rutilo e hoje estimado em torno de 600-640 C para graos de 100-200 micrometros resfriados a poucos graus C por milhao de anos, valor revisado para cima em relacao a estimativas de campo mais antigas."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-22): Cherniak (2000), Contributions to Mineralogy and Petrology 139, 198-207, relacao de Arrhenius D=3,9x10^-10 exp(-250+/-12 kJ/mol/RT) m2/s (700-1100 C); resultado de busca confirma 'closure temperature is about 100C higher than rutile closure temperature determinations from past field-based studies' e 'ca. 600-640C for rutile 0.1-0.2 mm diameter cooled at 3C/Myr'."
  - claim_id: PETROCRON-M27-A02-APATITA-FECHAMENTO-005
    claim: "O fechamento de Pb na apatita e o mais baixo entre os minerais U-Pb comuns discutidos nesta aula, em torno de 450-550 C, a depender de composicao e tamanho de grao."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-22): Chamberlain, K.R. & Bowring, S.A. (2001), Chemical Geology 172, 173-200, titulo confirma 'mid-range (~450C), diffusion-controlled system'; resultado de busca tambem cita faixa 375-600 C dependendo do contexto."
  - claim_id: PETROCRON-M27-A02-LUHF-GRANADA-006
    claim: "O sistema Lu-Hf em granada tende a fechar em temperatura mais alta que o Sm-Nd na mesma granada, e o Lu se concentra desproporcionalmente nas partes do cristal que crescem primeiro (nucleo), enviesando a idade Lu-Hf para os estagios iniciais do crescimento."
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-22): Scherer, Cameron & Blichert-Toft (2000), Geochimica et Cosmochimica Acta 64, 3413-3432, demonstra Lu/Hf elevado da granada e avalia fechamento relativo dos dois sistemas; a concentracao preferencial de Lu no nucleo de granadas zonadas e discutida com mais profundidade na Aula 07 desta serie, com fonte propria (Baxter & Scherer 2013)."
  - claim_id: PETROCRON-M27-A02-RBSR-MICAS-007
    claim: "O fechamento de Rb-Sr em biotita e tipicamente estimado perto de 300-350 C, e em muscovita perto de 450-500 C; o sistema K-Ar/Ar-Ar nas mesmas micas ocupa faixa de temperatura de fechamento semelhante em ordem de grandeza."
    risk: fato
    source: "Valores classicos de referencia amplamente citados na literatura de termocronologia de micas (por exemplo, compilacoes de Jager, Purdy & Jager 1976, e McDougall & Harrison 1999 para Ar-Ar). AUDITORIA (2026-09-22): conferido - valores classicos de Rb-Sr ~300 C (biotita) e ~500 C (muscovita), Jager 1967 e Purdy & Jager 1976; a faixa da aula esta dentro deles."
  - claim_id: PETROCRON-M27-A02-EXEMPLO-CINCO-IDADES-008
    claim: "Exemplo pedagogico hipotetico: granulito com ziracao U-Pb 620+/-5 Ma, monazita U-Pb 615+/-6 Ma, granada Lu-Hf 610+/-8 Ma, titanita U-Pb 590+/-7 Ma e biotita Rb-Sr 560+/-10 Ma, interpretado como sequencia de resfriamento de 620 a 560 Ma (60 milhoes de anos)."
    risk: hipotetico
    source: "Exemplo pedagogico construido especificamente para esta aula, com valores plausiveis e consistentes com a hierarquia de temperaturas de fechamento apresentada no corpo da aula, mas nao correspondente a uma amostra real publicada. ACHADO 5 DA AUDITORIA (2026-09-22, laranja, corrigido): a redacao usava MUSCOVITA Rb-Sr num GRANULITO e a lia como resfriamento por 450-500 C; muscovita nao e estavel na facies granulito (Ms + Qz reage antes dela - Dyck et al. 2020, JMG 38, 29-52), e uma muscovita retrograda dataria crescimento. Trocada por biotita (~300-350 C, valor que a propria aula da); idade e intervalo mantidos."
  - claim_id: PETROCRON-M27-A02-LU-CONCENTRACAO-GRANADA-009
    claim: "A granada concentra Lu mais que qualquer outro mineral formador de rocha; acessorios como zircao e xenotima tem teores ainda maiores de HREE, mas em quantidade modal infima, e inclusoes de zircao (ricas em Hf) contaminam isocronas Lu-Hf de granada."
    risk: fato
    source: "Criado pela auditoria (2026-09-22). ACHADO 3 (laranja, corrigido): a redacao dizia 'mais altas que em qualquer outra fase da rocha'. Rubatto & Hermann (2007), Chemical Geology 241, 38-61: 'Zircon contains significantly more heavy-REE than garnet at temperatures of 800-850 C'; Scherer, Cameron & Blichert-Toft (2000) tratam o efeito de inclusoes."
  - claim_id: PETROCRON-M27-A02-FONTES-AUSENTES-010
    claim: "As obras citadas no corpo da aula (Parrish 1990; Mezger, Essene & Halliday 1992; Kohn & Corrie 2011) constam da lista de Fontes com metadados conferidos; Mezger et al. (1992) estimam fechamento de Sm-Nd em granada de ca. 600 +/- 30 C."
    risk: fato
    source: "Criado pela auditoria (2026-09-22). ACHADO 4 (laranja, corrigido): as tres obras eram citadas no corpo e faltavam nas Fontes, e Mezger et al. eram creditados vagamente com 'valores de referencia' de uma faixa 600-750 C. Crossref: doi:10.1139/e90-152, doi:10.1016/0012-821X(92)90141-H (resumo lido), doi:10.1016/j.epsl.2011.09.008. Parte do mesmo achado toca a Aula 06."
auditoria:
  data: 2026-09-22
  achados: "3 (laranja, corrigido), 4 (laranja, corrigido), 5 (laranja, corrigido)"
  incertezas_declaradas_resolvidas: "paginacao de Cherniak et al. 2004, Copeland et al. 1988, Cherniak 1993 e Ganguly & Tirone 1999 - todas corretas como citadas; valores de Rb-Sr em micas conferidos"
revisao_didatica:
  data: 2026-09-22
  achados:
    - "DID-M27-REFERENCIAS-CRUZADAS-007 (amarelo): notacao 'Aula 26.04' / 'Aula 26.03' trocada por 'Modulo 26, Aula 04/03'."
    - "DID-M27-DURACOES-DECLARADAS-006 (amarelo): ~29,2 min reais (2451 palavras) contra ~28 declarados. NAO dividida: e um arco unico (do sistema isotopico ao mineral hospedeiro, com a tabela e o exemplo como sintese). Nenhuma passagem futura deve acrescentar texto aqui sem cortar equivalente."
-->
