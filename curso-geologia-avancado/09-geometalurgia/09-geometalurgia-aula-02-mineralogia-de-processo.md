# Aula 02: Caracterização de minério e ganga: mineralogia de processo e análise modal automatizada

**ID:** geologia-avancado-m09-a02
**Módulo:** [[09-geometalurgia-modulo|Módulo 09 — Geometalurgia]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** listar as perguntas que o processamento faz à mineralogia — em que minerais está o metal (partição), que minerais de ganga são problemáticos, que propriedades físicas e de superfície importam — e explicar o princípio, os produtos e as limitações da análise modal automatizada por microscopia eletrônica de varredura (MLA, QEMSCAN, TIMA), baseada em imagem de elétrons retroespalhados combinada com microanálise por EDS.

**Pré-requisito:** nenhum módulo deste curso. Da Aula 01: minério, ganga, recuperação, o papel da liberação e da textura, variável primária × proxy. Pressupõe mineralogia (módulo 05 do curso base): identificação de minerais opacos, fórmulas químicas, DRX.

## Antes de começar, você precisa saber

- Que a recuperação de uma rota de concentração tem um teto fixado pela mineralogia: só se recupera o metal que está num mineral que a rota consegue separar (Aula 01).
- Que a **difração de raios X (DRX)** identifica fases cristalinas e permite quantificação (refinamento de Rietveld), mas perde sensibilidade abaixo de ~1–2 % em massa e não vê fases amorfas (módulo 05 do curso base).
- Que num microscópio eletrônico de varredura (MEV) o sinal de **elétrons retroespalhados (BSE)** cresce com o número atômico médio da região analisada, e que um detector **EDS** (espectrometria de raios X por dispersão de energia) mede os elementos presentes num ponto.

## Conteúdo

### O que a mineralogia de processo precisa responder

A mineralogia de processo é a mineralogia lida com as perguntas do beneficiamento. São três famílias de pergunta:

**Onde está o metal — a partição (*deportment*).** Não basta saber que há 1 % de cobre; é preciso saber que fração desse cobre está em calcopirita, em calcosita, em crisocola, em cobre adsorvido em óxidos de ferro. Cada mineral portador tem uma rota e uma recuperação própria. A partição é o dado que fixa o teto de recuperação antes de qualquer questão de circuito.

**Que minerais de ganga são problemáticos.** A ganga não é neutra. Carbonatos consomem ácido na lixiviação de cobre; pirita e pirrotita consomem oxigênio, cal e coletor na flotação e podem contaminar o concentrado com enxofre; talco, micas e argilas são naturalmente hidrofóbicos ou geram lama, prejudicando a seletividade da flotação e o espessamento; minerais como arsenopirita (As), fluorita (F) e crocoíta levam ao concentrado elementos **penalizantes**, que reduzem o preço pago ou impedem a venda.

**Que propriedades físicas e de superfície governam a separação.** Densidade (separação gravítica), susceptibilidade magnética (separação magnética), resposta a coletor e ao pH (flotação), dureza e abrasividade (cominuição), solubilidade (lixiviação). A mineralogia informa todas.

### Métodos clássicos e seus limites

A **microscopia óptica de luz refletida** é barata, insubstituível para um primeiro diagnóstico de sulfetos e texturas, e serve de calibração para os métodos automatizados — mas é subjetiva, lenta para quantificar e limitada em grãos finos. A **DRX** dá a composição modal do material bruto, com as limitações de sensibilidade já citadas. A **química por dissolução seletiva** (por exemplo, a razão entre cobre solúvel em ácido sulfúrico fraco e cobre total) é barata e mede diretamente uma fração de interesse, servindo de proxy. O **MEV com EDS manual** identifica fases ponto a ponto, mas não quantifica área nem produz estatística de partículas em volume útil.

### Análise modal automatizada: o princípio

A análise modal automatizada por MEV resolve o problema de quantificar. O procedimento:

1. **Preparação.** Prepara-se uma seção polida — em geral grãos moídos e peneirados por fração de tamanho, montados em resina e polidos —, recoberta com carbono para condução.
2. **Segmentação por BSE.** A imagem de elétrons retroespalhados tem brilho proporcional ao número atômico médio: sulfetos aparecem claros, silicatos escuros, óxidos intermediários. O *software* segmenta a imagem em regiões de brilho homogêneo, cada uma uma fase mineral candidata.
3. **Identificação por EDS.** Em cada região, um espectro rápido de raios X característicos dá a composição elementar, comparada a uma **biblioteca de minerais** para classificar a fase.
4. **Modos de operação.** Mapeamento completo de partículas (todos os pixels classificados), varredura pontual em grade (mais rápida), ou busca dedicada de fases raras e pesadas (ouro, elementos do grupo da platina), guiada pelo brilho de BSE.

O **MLA** (*Mineral Liberation Analyser*, desenvolvido no JKMRC — Gu, 2003), o **QEMSCAN** (derivado do QEM\*SEM da CSIRO — Sutherland & Gottlieb, 1991), o **TIMA** (Tescan), o **Mineralogic** (Zeiss) e o **AMICS** (Bruker) usam a mesma física; diferem em *software*, estratégia de aquisição e detalhes de calibração.

> [!warning] Nomes comerciais envelhecem
> As plataformas trocam de dono e de marca com frequência — o MLA nasceu no JKMRC, passou pela FEI e hoje está sob a Thermo Fisher; o QEMSCAN percorreu CSIRO → Intellection → FEI → Thermo Fisher. O que **não** muda é o princípio BSE + EDS e a natureza dos produtos. Ao especificar um ensaio, confirme qual plataforma o laboratório de fato opera, em vez de citar a sigla de memória.

### O que a técnica entrega

- **Composição modal** — percentual em massa de cada mineral, mais robusta que a DRX para fases de poucos por cento.
- **Partição elementar (*deportment*)** — combinando a modal com a fórmula (ou o EDS quantitativo) de cada mineral, o percentual de cada elemento alocado a cada mineral.
- **Associação mineral** — comprimento (ou área) de contato de fronteira entre pares de minerais: diz a quem o mineral-alvo está encostado, e portanto de quem precisa se separar.
- **Distribuição de tamanho de grão** do mineral na rocha, medida diretamente.
- **Grau de liberação por classe de tamanho** de partícula (tema da Aula 03).
- **Textura quantitativa** — inclusões, coroas de reação, disseminação, exsolução.

### Limitações

- **Resolução espacial** da ordem de 1 µm (tamanho do feixe e volume de interação): grãos e inclusões submícron ficam mal resolvidos, e o travamento fino é subestimado.
- **Fases de química e número atômico médio parecidos** são difíceis de distinguir (por exemplo, alguns sulfossais entre si; silicatos de ganga semelhantes).
- **Estatística de partículas:** a precisão para um mineral raro depende de quantos grãos dele foram contados; ouro e EGP costumam exigir varredura dedicada.
- **Viés de preparação:** segregação por densidade na montagem da seção, orientação preferencial de grãos alongados, e o fato de a fração analisada já ter sido britada — o que altera a liberação aparente.
- **Viés estereológico:** uma seção bidimensional corta partículas fora do centro, e o corte de uma partícula mista pode atravessar **só uma das fases** — resultado indistinguível do corte de uma partícula genuinamente liberada. O viés é de mão única: uma partícula liberada nunca aparece como mista, mas uma mista aparece como liberada com frequência. Logo, a seção 2D **superestima a liberação** tridimensional (subestima o travamento). Há correções estereológicas (King; Gay & Morrison, 2006) e a microtomografia de raios X mede a liberação em 3D sem o viés, mas ambas custam mais.
- É uma **imagem estática de uma seção**: mede mineralogia, não comportamento. Modal não é metalurgia.
- **Custo e tempo** por amostra limitam quantas amostras do programa recebem mineralogia quantitativa.

### Como isso entra no programa geometalúrgico

A mineralogia quantitativa é feita num subconjunto de amostras e correlacionada com proxies baratas e densas — sobretudo a geoquímica multielementar — para que a partição do metal e a mineralogia de ganga possam ser propagadas ao modelo de blocos (Aula 06).

## Exemplo trabalhado

**Situação:** a análise modal automatizada de um minério de cobre, com os teores de cobre de cada mineral, dá:

| Mineral | Massa (%) | Cu no mineral (%) |
|---|---|---|
| Calcopirita (CuFeS₂) | 2,20 | 34,6 |
| Calcosita (Cu₂S) | 0,18 | 79,9 |
| Crisocola (silicato de Cu) | 0,25 | 36,0 |
| Cu em óxidos de Fe (limonita cuprífera) | — | contribui 0,030 % Cu ao total |

Os teores de Cu da calcopirita e da calcosita são os estequiométricos (CuFeS₂ → 34,6 % Cu; Cu₂S → 79,9 % Cu). O da **crisocola não é**: a fórmula aceita, `Cu₂₋ₓAlₓ(H₂₋ₓSi₂O₅)(OH)₄·nH₂O`, tem Cu, Al e água variáveis, e o teor real oscila em torno de 30–38 %. Os 36,0 % da tabela são o valor **medido nesta amostra**, não uma constante do mineral — e é por isso que a análise modal precisa vir acompanhada do EDS quantitativo da fase.

Calcule o teor de cobre do minério, a partição do cobre entre os minerais e a recuperação máxima teórica por flotação de sulfetos, supondo que a flotação recupera 95 % do cobre que está em sulfetos.

**Resolução:**

Cobre aportado por cada mineral (percentual absoluto no minério):
`Calcopirita: 2,20 × 0,346 = 0,761 %`
`Calcosita:   0,18 × 0,799 = 0,144 %`
`Crisocola:   0,25 × 0,360 = 0,090 %`
`Óxidos de Fe:               0,030 %`
`Cu total = 0,761 + 0,144 + 0,090 + 0,030 = 1,025 % Cu`

Partição do cobre:
`Calcopirita: 0,761 / 1,025 = 74,2 %`
`Calcosita:   0,144 / 1,025 = 14,0 %`
`Crisocola:   0,090 / 1,025 =  8,8 %`
`Óxidos de Fe: 0,030 / 1,025 = 2,9 %`

Cobre em sulfetos flotáveis (calcopirita + calcosita) = `74,2 + 14,0 = 88,2 %` do cobre total.

Recuperação máxima teórica por flotação:
`R_máx = 0,882 × 0,95 = 0,838 → 83,8 %`

**Interpretação:** o teto de recuperação por flotação — cerca de 84 % — já está definido pela partição, antes de qualquer discussão sobre liberação, reagente ou circuito. Nenhum ajuste de flotação recupera o cobre que está em crisocola e em óxidos de ferro (11,7 % do total); para esse cobre seria preciso uma rota de lixiviação ácida. A proxy barata para essa fração seria a razão entre cobre solúvel em ácido e cobre total, medida em todos os furos — é ela que, propagada ao modelo, sinalizaria onde a flotação sozinha deixa metal para trás.

## Erros comuns

- **Confundir composição modal com composição química** — um mineral pode ser abundante e pobre no metal, ou raro e o principal portador.
- **Pedir análise modal automatizada e interpretá-la como medida de metalurgia** — ela alimenta a previsão, não a substitui.
- **Ignorar minerais de ganga menores mas penalizantes ou consumidores de reagente** (talco, arsenopirita, carbonatos, pirrotita).
- **Esquecer o viés estereológico** — a seção 2D **superestima** a liberação; tomar o número bruto como verdade promete ao projeto uma recuperação que a planta não entrega.
- **Tratar a resolução de ~1 µm como se resolvesse tudo** — inclusões submícron passam despercebidas.
- **Montar a seção sem controlar a segregação por densidade** — o modal sai enviesado a favor dos minerais pesados no fundo da amostra.
- **Usar DRX para quantificar uma fase abaixo de ~2 % ou amorfa** (crisocola, ferridrita, geles de sílica).

## O que não concluir

- **Que MLA, QEMSCAN e TIMA "medem a recuperação"** — medem mineralogia, associação e liberação.
- **Que a técnica distingue todos os minerais** — polimorfos e fases isoquímicas exigem catodoluminescência, DRX ou EBSD.
- **Que uma amostra caracterizada representa o depósito** — só o desenho de amostragem estratificado dá representatividade.
- **Que a microscopia óptica ficou obsoleta** — continua sendo o melhor primeiro olhar sobre sulfetos e texturas e calibra a biblioteca automatizada.

## Recap relâmpago

- A **mineralogia de processo** pergunta: em que minerais está o metal (**partição** / *deportment*), que minerais de ganga são problemáticos (consumidores de ácido e de reagente, geradores de lama, penalizantes) e que propriedades físicas e de superfície governam a separação.
- A **análise modal automatizada por MEV** (MLA, QEMSCAN, TIMA) segmenta uma seção polida pelo brilho de **BSE** (proporcional ao número atômico médio) e identifica cada fase por **EDS**, classificando-a contra uma biblioteca de minerais.
- Entrega, quantitativos: **composição modal, partição elementar, associação mineral, distribuição de tamanho de grão e grau de liberação**.
- Limitações: **resolução ~1 µm** (finos), fases de química e Z̄ parecidos, estatística de fases raras, viés de preparação e **viés estereológico** (a seção 2D **superestima** a liberação, porque o corte de uma partícula mista pode atravessar só uma das fases), e o fato de ser uma imagem estática.
- A **partição do metal fixa o teto de recuperação de uma rota**: no exemplo, 88 % do cobre em sulfetos → no máximo ~84 % por flotação, quaisquer que sejam a liberação e o reagente.

## Próxima aula

[[09-geometalurgia-aula-03-textura-e-liberacao|Aula 03 — Textura, tamanho de grão e liberação mineral: curvas de liberação]]

## Anterior

[[09-geometalurgia-aula-01-o-que-e-geometalurgia|Aula 01 — O que é geometalurgia: da caracterização geológica ao processo e o programa geometalúrgico]]

## Fontes

- Wills, B. A. & Finch, J. A. (2016), *Wills' Mineral Processing Technology*, 8ª ed., Butterworth-Heinemann, cap. 1 e 12.
- Gu, Y. (2003), "Automated scanning electron microscope based mineral liberation analysis: an introduction to JKMRC/FEI Mineral Liberation Analyser", *Journal of Minerals & Materials Characterization & Engineering*, 2(1), p. 33–41.
- Sutherland, D. N. & Gottlieb, P. (1991), "Application of automated quantitative mineralogy in mineral processing", *Minerals Engineering*, 4(7–11), p. 753–762.
- Fandrich, R., Gu, Y., Burrows, D. & Moeller, K. (2007), "Modern SEM-based mineral liberation analysis", *International Journal of Mineral Processing*, 84(1–4), p. 310–320.
- Gay, S. L. & Morrison, R. D. (2006), "Using two-dimensional sectional distributions to infer three-dimensional volumetric distributions — validation using tomography", *Particle & Particle Systems Characterization*, 23(3–4), p. 246–253.
- Baum, W. (2014), "Ore characterization, process mineralogy and lab automation — a roadmap for future mining", *Minerals Engineering*, 60, p. 69–73.
- Lotter, N. O., Baum, W., Reeves, S., Arrué, C. & Bradshaw, D. J. (2018), "The business value of best practice process mineralogy", *Minerals Engineering*, 116, p. 226–238.

<!--
nivel: avancado
palavras_corpo: ~1710
mapa_objetivo_secao:
  geologia-avancado-m09-oa01: "O que a mineralogia de processo precisa responder" + "Métodos clássicos e seus limites" + "Análise modal automatizada: o princípio" + "O que a técnica entrega" + "Limitações" + "Como isso entra no programa geometalúrgico" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOMET-M09-A02-DEPORTMENT-001
    claim: "A mineralogia de processo determina a partição (deportment) do metal entre os minerais portadores, a identidade e o efeito dos minerais de ganga problemáticos (consumidores de ácido como carbonatos; consumidores de reagente e oxigênio como pirita e pirrotita; geradores de lama e naturalmente hidrofóbicos como talco, micas e argilas; portadores de elementos penalizantes como arsenopirita) e as propriedades físicas e de superfície relevantes à separação."
    risk: fato
    source: "Wills & Finch 2016, cap. 1 e 12; Baum 2014; Lotter et al. 2018"
  - claim_id: GEOMET-M09-A02-PRINCIPIO-002
    claim: "A análise modal automatizada por MEV segmenta uma seção polida usando o contraste de elétrons retroespalhados (BSE), cuja intensidade cresce com o número atômico médio, e identifica cada região por espectrometria de raios X por dispersão de energia (EDS) comparada a uma biblioteca de minerais."
    risk: fato
    source: "Gu 2003; Sutherland & Gottlieb 1991; Fandrich et al. 2007"
  - claim_id: GEOMET-M09-A02-SISTEMAS-003
    claim: "MLA (Mineral Liberation Analyser, desenvolvido no JKMRC, depois FEI, hoje Thermo Fisher), QEMSCAN (derivado do QEM*SEM da CSIRO, via Intellection e FEI, hoje Thermo Fisher), TIMA (Tescan), Mineralogic (Zeiss) e AMICS (Bruker) são sistemas de análise modal automatizada baseados no mesmo princípio BSE + EDS, diferindo em software, estratégia de aquisição e calibração; os nomes comerciais e a propriedade das plataformas mudam com frequência, o princípio não."
    risk: desatualizavel
    source: "Gu 2003; Sutherland & Gottlieb 1991; Fandrich et al. 2007; CSIRO (histórico do QEM*SEM/QEMSCAN); catálogos vigentes dos fabricantes"
  - claim_id: GEOMET-M09-A02-PRODUTOS-004
    claim: "A análise modal automatizada entrega, de forma quantitativa: composição modal (% massa por mineral), partição elementar, associação mineral (contato de fronteira entre pares de minerais), distribuição de tamanho de grão e grau de liberação por classe de tamanho."
    risk: fato
    source: "Gu 2003; Fandrich et al. 2007; Wills & Finch 2016, cap. 12"
  - claim_id: GEOMET-M09-A02-LIMITES-005
    claim: "As principais limitações da análise modal automatizada por MEV são: resolução espacial da ordem de 1 µm (subestima travamento fino); dificuldade de distinguir fases de número atômico médio e química semelhantes; dependência do número de partículas contadas para fases raras; viés de preparação da seção; e viés estereológico, em que a seção bidimensional SUPERESTIMA a liberação tridimensional, porque o corte de uma partícula mista pode atravessar só uma das fases e ficar indistinguível do corte de uma partícula liberada, enquanto uma partícula liberada nunca aparece como mista — viés de mão única, corrigível de forma imperfeita por métodos estereológicos ou eliminável por microtomografia de raios X."
    risk: fato
    source: "Fandrich et al. 2007; Wills & Finch 2016, cap. 12; Gay & Morrison 2006; King 2012, cap. 2; literatura de correção estereológica e de micro-CT"
  - claim_id: GEOMET-M09-A02-EXEMPLO-006
    claim: "Para um minério com calcopirita 2,20 % massa (34,6 % Cu, estequiométrico), calcosita 0,18 % massa (79,9 % Cu, estequiométrico), crisocola 0,25 % massa (36,0 % Cu, valor medido — a crisocola tem Cu variável, ~30–38 %, pela fórmula Cu2-xAlx(H2-xSi2O5)(OH)4·nH2O) e 0,030 % Cu em óxidos de Fe: Cu total = 1,025 %; partição = 74,2 % calcopirita, 14,0 % calcosita, 8,8 % crisocola, 2,9 % óxidos; cobre em sulfetos flotáveis = 88,2 %; recuperação máxima teórica por flotação a 95 % de recuperação de sulfetos = 83,8 %."
    risk: calculo
    source: "Aritmética de partição; Wills & Finch 2016, cap. 3 e 12"
-->
