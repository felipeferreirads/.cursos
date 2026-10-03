# Aula 02: Aeromagnetometria — fundamentos, correções, reduções e realces de mapas magnéticos

**ID:** geologia-avancado-m16-a02
**Módulo:** [[16-aerogeofisica-modulo|Módulo 16 — Introdução à aerogeofísica]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** explicar como o campo magnético total medido em voo é transformado em mapa geológico interpretável, cobrindo o instrumento de medida, as correções que isolam o sinal geológico e os realces que tornam esse sinal visível.
**Ao final você vai conseguir:** explicar o que um magnetômetro aéreo mede e por que ele mede um campo escalar; aplicar a um dado bruto as correções de IGRF e de variação diurna, sabendo o que na cadeia de processamento tem ordem obrigatória e o que não tem; explicar por que a redução ao polo é necessária e por que ela é instável perto do equador magnético; e escolher entre os principais realces (derivadas, sinal analítico, continuação) conforme o objetivo de interpretação.
**Pré-requisito:** [[16-aerogeofisica-aula-01-planejamento-de-voo-plataformas-parametros-de-aquisicao-controle-de-qualidade|Aula 01]] — os parâmetros de aquisição ali definidos (altura, espaçamento, estação-base) são o que torna as correções desta aula possíveis; e [[15-petrofisica/15-petrofisica-aula-03-magnetismo-das-rochas-e-radioatividade-natural|Módulo 15, Aula 03]] — esta aula assume que você já sabe que a magnetita (não a ilmenita, paramagnética) domina a resposta magnética das rochas, e que a magnetização total tem uma parcela induzida e uma parcela remanente.

## Conteúdo

### O que o magnetômetro aéreo mede

Um magnetômetro aéreo mede a **intensidade magnética total** (Total Magnetic Intensity, TMI) — o módulo do vetor campo magnético no ponto de medida, sem distinguir a direção do campo. Isso é uma escolha deliberada de instrumentação: os magnetômetros escalares usados hoje na quase totalidade dos levantamentos aéreos são de vapor de metal alcalino bombeado opticamente (césio ou potássio) ou, historicamente, de precessão de prótons; ambos medem apenas a magnitude do campo, com sensibilidade, estabilidade e taxa de amostragem muito maiores que as de um magnetômetro vetorial (do tipo fluxgate), que mede as três componentes do campo mas com exatidão absoluta menor e sujeito a deriva. Por isso o fluxgate triaxial não é, em geral, o sensor de mapeamento de um aerolevantamento: seu papel característico a bordo é outro, e é alimentar o **sistema de compensação magnética da aeronave** — é ele que informa a atitude da aeronave em relação ao campo ambiente, sem a qual não se modela a contaminação magnética da própria fuselagem. A taxa de amostragem típica de um magnetômetro de vapor de césio é alta o suficiente (dezenas de leituras por segundo) para que, mesmo em avião voando a centenas de quilômetros por hora, o espaçamento entre amostras ao longo da linha fique na ordem de poucos metros — muito menor que o espaçamento entre linhas, o que faz da resolução ao longo da linha, na prática, quase sempre melhor que a resolução entre linhas.

O sensor magnético é normalmente posicionado o mais longe possível da estrutura metálica e dos sistemas elétricos da aeronave — rebocado atrás dela num invólucro aerodinâmico (o "bird" ou stinger) ou montado na ponta de uma longarina (boom) — precisamente para minimizar a magnetização própria da aeronave que o teste de erro de rumo em oito, visto na Aula 01, detecta e quantifica.

### O campo medido não é só geologia: o que precisa ser removido

O campo magnético total medido em qualquer ponto da Terra é a soma de várias contribuições, e apenas uma delas interessa à interpretação geológica de superfície: a resposta magnética das rochas rasas da crosta (a anomalia magnética crustal, que reflete o que a Aula 03 do Módulo 15 já ensinou — sobretudo o teor de magnetita e titanomagnetita, com contribuição da magnetização remanente). As outras contribuições precisam ser identificadas e removidas, e cada uma tem sua correção própria:

**O campo principal da Terra**, gerado no núcleo externo, é de longe a maior componente (a intensidade do campo total na superfície varia, por latitude magnética, de cerca de 25.000 nT perto do equador magnético a cerca de 65.000 nT próximo aos polos magnéticos) e varia suavemente em escala global e ao longo dos anos (variação secular). Essa componente é modelada e removida usando o **IGRF** (International Geomagnetic Reference Field), um modelo matemático de referência do campo principal e de sua variação secular, mantido e atualizado a cada cinco anos por um grupo de trabalho internacional (IAGA) — a geração mais recente em uso é o IGRF-14 (coeficientes finalizados em 2024). Subtrair o valor do IGRF, calculado para a posição e a data exatas de cada medida, do campo total medido produz a **anomalia de campo total** (Total Magnetic Intensity anomaly ou, na sigla mais usada, TMI residual), que já não contém o campo principal — mas o IGRF é um modelo de baixa resolução espacial construído para descrever o campo em escala global, e em algumas regiões ele é uma aproximação grosseira da realidade local; nesses casos, prefere-se remover um campo regional determinado localmente (ajustado ao próprio levantamento) em vez do IGRF puro, e essa é uma decisão de processamento que precisa ser documentada.

**A variação diurna**, de origem externa (correntes elétricas na ionosfera e na magnetosfera, moduladas pelo vento solar e pela posição do Sol ao longo do dia), muda o campo medido em qualquer ponto ao longo de um único dia de voo, tipicamente em dezenas de nanotesla em condições calmas — e é justamente aqui que a estação-base terrestre da Aula 01 se torna indispensável: como o campo diurno afeta toda a área do levantamento de forma praticamente simultânea (é uma variação temporal, não espacial), a leitura contínua da estação-base ao longo do voo permite calcular a variação diurna no momento de cada medida aérea e subtraí-la — um processo diferente do IGRF (que remove uma componente suave e previsível de longo prazo) porque a variação diurna é medida em tempo real, não modelada.

Depois de removidos o IGRF e a variação diurna, resta ainda o nivelamento entre linhas (Aula 01) para eliminar deslocamentos residuais nos cruzamentos, e só então o dado está pronto para as transformações de interpretação.

**O que tem ordem obrigatória e o que não tem.** Vale separar as duas coisas, porque é um ponto em que se decora ordem à toa. Entre IGRF e diurna **não há ordem obrigatória**: as duas são subtrações de números do mesmo valor medido, e subtração é comutativa — remover primeiro o IGRF e depois a diurna dá exatamente o mesmo resultado que o inverso. O que **é** obrigatório é o bloco: as duas precisam vir **antes** do nivelamento, e o nivelamento **antes** de qualquer realce. A razão é que nivelamento e realces não são subtrações de constantes — o nivelamento ajusta cada linha comparando-a com as vizinhas, e um realce é um filtro que opera sobre a grade inteira; aplicar qualquer um dos dois sobre um dado que ainda contém a deriva diurna significa espalhar essa deriva por toda a área do mapa, de forma que nenhuma correção posterior desfaz. Compare com a Aula 04, onde a ordem entre duas correções internas (stripping e altura) **é** obrigatória por razão física: não é regra geral, é caso a caso.

Guarde a pergunta, porque ela serve para os quatro métodos do módulo: *esta etapa é uma subtração ponto a ponto, ou ela mistura informação entre pontos vizinhos (ou entre canais)?* Só a segunda impõe ordem.

### Redução ao polo: por que a forma da anomalia engana

Mesmo depois de todas as correções, a anomalia magnética de um corpo geológico simples (por exemplo, um dique tabular verticalizado e homogêneo) **não** aparece no mapa como um pico simétrico centrado sobre o corpo — sua forma depende da **inclinação e da declinação magnética do local**, porque a magnetização induzida do corpo segue a direção do campo ambiente, e a geometria de como um dipolo inclinado projeta sua anomalia sobre um plano horizontal distorce a forma observada. Em latitudes médias e altas, onde a inclinação é alta (o campo é quase vertical), essa distorção é moderada; perto do equador magnético, onde a inclinação se aproxima de zero (o campo é quase horizontal), a distorção é extrema — a anomalia de um corpo pode aparecer deslocada lateralmente do corpo real por uma distância maior que sua própria profundidade, e frequentemente aparece como um par de lóbulos (positivo e negativo) em vez de um único máximo, dificultando enormemente a localização visual do corpo.

A **redução ao polo** (RTP, reduction to pole) é a transformação matemática que corrige essa distorção: ela recalcula a anomalia como se ela tivesse sido medida no polo magnético, onde a inclinação é de 90° e a anomalia de um corpo simples aparece centrada e simétrica sobre ele, facilitando a interpretação geométrica direta. O problema é que a própria matemática da RTP se torna instável — o filtro amplifica ruído de forma descontrolada — exatamente nas baixas latitudes magnéticas onde ela seria mais necessária, porque o termo que divide a operação tende a zero quando a inclinação se aproxima de zero. Perto do equador magnético, portanto, usam-se alternativas mais estáveis, como a **redução ao equador** (RTE, análoga à RTP mas formulada para inclinação baixa) ou transformações que não dependem da direção do campo, como o sinal analítico, discutido a seguir.

### Realces: tornando visível o que já está no dado

Um realce (enhancement) não adiciona informação ao dado — ele reorganiza matematicamente a informação já presente para tornar mais visível algum aspecto específico da anomalia, geralmente às custas de suprimir outro. Os realces mais usados em mapas aeromagnéticos são:

**Derivadas verticais e horizontais.** A primeira derivada vertical do campo acentua os contrastes de curto comprimento de onda (fontes rasas e de bordas nítidas) em relação aos de longo comprimento de onda (fontes profundas e regionais), funcionando como um filtro passa-alta natural; derivadas horizontais destacam gradientes laterais, úteis para localizar bordas e contatos.

**Sinal analítico.** É uma combinação das derivadas horizontais e vertical cuja amplitude, ao contrário da anomalia de campo total, é muito **menos dependente da direção de magnetização do corpo** (da inclinação/declinação do campo ambiente e de o corpo ter magnetização remanente em direção diferente da induzida) — sua amplitude máxima tende a ficar centrada sobre as bordas do corpo causador, o que o torna especialmente valioso perto do equador magnético, onde a RTP é instável, e em áreas com forte magnetização remanente, onde a direção de magnetização é desconhecida e a RTP (que pressupõe magnetização puramente induzida na direção do campo atual) pode produzir resultados enganosos.

Aqui cabe uma ressalva que a literatura de divulgação costuma omitir e que muda o quanto se pode confiar no resultado: essa independência é **rigorosa apenas para fontes bidimensionais** — corpos muito mais longos que largos, como um dique extenso ou um contato retilíneo, em que a geometria não varia ao longo do strike. Para corpos **tridimensionais** compactos (um plug, uma lente de sulfeto, um kimberlito), a amplitude do sinal analítico **volta a depender** da direção de magnetização, embora bem menos que a anomalia de campo total. Na prática isso significa que o sinal analítico é a alternativa certa à RTP para mapear estruturas lineares em baixa latitude magnética, mas não é um passe livre: sobre um alvo compacto e fortemente remanente, a posição do máximo do sinal analítico ainda pode se deslocar em relação ao corpo, e a interpretação segura passa por modelagem direta em vez de leitura visual do mapa.

**Derivada tilt (tilt derivative).** É a razão entre a derivada vertical e a amplitude do gradiente horizontal total, uma transformação que normaliza a amplitude do sinal (equalizando fontes fracas e fortes num mesmo mapa) e cujo valor zero cai aproximadamente sobre a borda do corpo — útil para mapear contatos diretamente sem depender de amplitude absoluta.

**Continuação para cima e para baixo (upward/downward continuation).** É o cálculo de como o campo apareceria se medido a uma altura diferente da altura de voo real: a continuação para cima simula um voo mais alto, suprimindo o ruído de alta frequência e as fontes muito rasas para destacar tendências regionais mais profundas; a continuação para baixo simula um voo mais baixo, acentuando fontes rasas — mas amplifica ruído de forma agressiva e só é confiável até uma distância limitada abaixo da altura real de aquisição.

A escolha de qual realce aplicar depende do objetivo interpretativo: mapeamento estrutural regional favorece derivadas e continuação para cima; localização precisa de bordas de corpos individuais favorece sinal analítico ou tilt; qualquer realce, porém, é aplicado sobre o dado já corrigido de IGRF, variação diurna e nivelado — nunca antes.

## Exemplo trabalhado

**Situação:** um levantamento aeromagnético é realizado num dia de 8 horas de voo. No início do voo (08h00, hora local), a estação-base registra 45.230 nT; ao meio-dia (12h00), registra 45.268 nT; ao final da tarde (16h00), registra 45.241 nT. O valor do IGRF calculado para a posição e a data do levantamento é de 45.210 nT (considerado constante ao longo do dia, por a variação secular ser lenta demais para importar num único dia). Uma medida aérea específica, feita às 12h00 sobre um ponto de interesse, registra um campo total bruto de 45.410 nT.

**Pergunta:** calcule a anomalia de campo total (TMI residual) desse ponto, após remover a variação diurna e o IGRF.

**Resolução:**

**Passo 1 — variação diurna no momento da medida.** Às 12h00, a estação-base registrou 45.268 nT. Definindo um nível de referência da estação-base (por exemplo, a leitura do início do voo, 45.230 nT), a variação diurna acumulada até as 12h00 é:

Variação diurna (12h00) = 45.268 − 45.230 = **+38 nT**

**Passo 2 — remover a variação diurna da medida aérea.** A medida aérea bruta (45.410 nT) contém essa mesma variação temporal, que afeta toda a área do levantamento por igual naquele instante. Subtraindo-a:

Campo corrigido de diurna = 45.410 − 38 = **45.372 nT**

**Passo 3 — remover o IGRF.** O IGRF (45.210 nT) representa o campo principal da Terra na posição e data do levantamento. Subtraindo-o do campo já corrigido de diurna:

Anomalia de campo total (TMI residual) = 45.372 − 45.210 = **+162 nT**

**Uma ressalva sobre o datum da diurna.** Escolher a leitura das 08h00 como nível de referência da estação-base foi uma decisão arbitrária: qualquer outro nível (a média do dia, o próprio valor do IGRF na posição da estação) produziria a mesma *forma* de anomalia deslocada por uma constante. O que o Passo 1 remove é a **variação** temporal, não o valor absoluto do campo na estação — e é por isso que a TMI residual se interpreta por **contraste relativo** entre pontos do levantamento, não pelo valor absoluto isolado. O deslocamento constante que sobra é justamente uma das coisas que o nivelamento em cruzamentos (Aula 01) absorve.

**Interpretação:** os +162 nT que restam não são mais campo principal nem variação temporal externa — são, dentro da precisão das correções aplicadas, a contribuição magnética das rochas rasas sob aquele ponto do levantamento: uma anomalia positiva desse tamanho é compatível, por exemplo, com uma concentração local de magnetita acima do fundo regional (um corpo máfico raso, uma zona de alteração magnética, ou uma estrutura similar), a ser confirmada com o restante do mapa e, se necessário, com realces como o sinal analítico para localizar suas bordas com mais precisão. Note que a ordem das correções importa: se a variação diurna não fosse removida antes de comparar duas medidas feitas em horários diferentes do mesmo voo, uma simples deriva temporal do campo poderia ser confundida com uma variação geológica real ao longo da linha.

## Erros comuns

- **Aplicar um realce (derivada, sinal analítico) antes do nivelamento entre linhas.** A aula é explícita: realces misturam informação entre pontos vizinhos, então qualquer deriva residual não nivelada se espalha pelo mapa inteiro de um jeito que nenhuma correção posterior desfaz.
- **Usar RTP perto do equador magnético esperando o mesmo resultado estável de latitudes médias.** É exatamente onde a matemática da RTP amplifica ruído descontroladamente — a alternativa (RTE ou sinal analítico) existe precisamente para esse cenário.
- **Tratar a independência de direção do sinal analítico como absoluta.** É rigorosa só para fontes bidimensionais (diques, contatos retilíneos); sobre um corpo 3D compacto e remanente, a posição do máximo ainda pode se deslocar — a leitura visual do mapa, nesse caso, precisa de modelagem direta, não só olhar a imagem.
- **Comparar duas medidas de horários diferentes do mesmo voo sem remover a variação diurna primeiro.** Como o exemplo trabalhado mostra, uma deriva temporal de dezenas de nT pode ser confundida com variação geológica real ao longo da linha se não for subtraída antes de qualquer comparação.

## O que não concluir

- **Que a ordem entre IGRF e variação diurna importa.** São subtrações de números do mesmo valor medido — comutativas, sem ordem obrigatória entre si; o que é obrigatório é que ambas precedam nivelamento e realce, categorias diferentes de operação.
- **Que um realce "revela" informação nova sobre o corpo geológico.** Ele reorganiza matematicamente o que já está no dado, geralmente suprimindo um aspecto para destacar outro — nunca adiciona sinal que a aquisição não capturou.
- **Que continuação para baixo é sempre segura para "recuperar" resolução perdida por voo alto.** Ela amplifica ruído de forma agressiva e só é confiável até uma distância limitada abaixo da altura real de aquisição — não é o inverso livre da continuação para cima.

## Recap relâmpago

- Magnetômetros aéreos modernos (vapor de césio ou potássio, bombeados opticamente) medem a intensidade magnética total (TMI) — um campo escalar, sem componente direcional —, com taxa de amostragem alta o suficiente para que o espaçamento entre amostras ao longo da linha seja de poucos metros, bem menor que o espaçamento entre linhas.
- O campo medido soma o campo principal da Terra (dezenas de milhares de nT, variando de ≈25.000 nT no equador magnético a ≈65.000 nT nos polos magnéticos), a variação diurna de origem externa e a anomalia crustal de interesse geológico — só a última interessa à interpretação.
- O IGRF (modelo internacional atualizado a cada cinco anos, geração atual IGRF-14) remove o campo principal e sua variação secular de longo prazo; a variação diurna, medida em tempo real por uma estação-base terrestre simultânea, é removida separadamente porque afeta toda a área do levantamento ao mesmo tempo, não podendo ser modelada como o IGRF.
- **Entre IGRF e diurna não há ordem obrigatória** (são subtrações, e subtração é comutativa); o obrigatório é que as duas venham antes do **nivelamento**, e o nivelamento antes de qualquer **realce** — porque essas duas etapas misturam informação entre pontos vizinhos e espalhariam a deriva pelo mapa inteiro. A pergunta que decide ordem, em qualquer método: a etapa é subtração ponto a ponto, ou mistura pontos/canais?
- A redução ao polo (RTP) corrige a distorção de forma da anomalia causada pela inclinação/declinação magnética local, centrando a anomalia sobre o corpo causador — mas é instável perto do equador magnético, onde a inclinação tende a zero; nesses casos usam-se alternativas como a redução ao equador ou transformações independentes da direção de magnetização.
- O sinal analítico tem amplitude muito menos dependente da direção de magnetização do corpo (induzida ou remanente) e da inclinação/declinação do campo, sendo especialmente útil perto do equador magnético e em áreas com forte magnetização remanente, onde a RTP pode enganar — mas essa independência é **rigorosa só para fontes 2D** (diques, contatos retilíneos); sobre corpos 3D compactos a amplitude volta a depender da direção de magnetização, e a leitura visual do mapa precisa ser confirmada por modelagem.
- Derivadas (vertical, horizontal, tilt) acentuam contrastes de curto comprimento de onda e localizam bordas; continuação para cima simula voo mais alto e suprime ruído/fontes rasas, continuação para baixo simula voo mais baixo e acentua fontes rasas, mas amplifica ruído. Todo realce é aplicado sobre o dado já corrigido e nivelado, nunca antes.

## Próxima aula

[[16-aerogeofisica-aula-03-aerogravimetria-e-gradiometria|Aula 03 — Aerogravimetria e gradiometria]] — muda o campo físico medido de magnetismo para gravidade, mas mantém a mesma lógica de separar sinal geológico de ruído: aqui o ruído dominante não vem de fora da Terra, e sim do próprio movimento da aeronave.

## Fontes

- Telford, W. M., Geldart, L. P. & Sheriff, R. E. (1990), *Applied Geophysics*, 2ª ed., Cambridge University Press, cap. 6 (instrumentação magnética, componentes do campo medido, redução ao polo).
- Reeves, C. (2005), *Aeromagnetic Surveys: Principles, Practice and Interpretation*, Geosoft (processamento de dados aeromagnéticos: IGRF, diurna, nivelamento, realces).
- IAGA V-MOD / NOAA NCEI, "International Geomagnetic Reference Field (IGRF)" (definição, atualização a cada cinco anos, geração IGRF-14 finalizada em 2024).
- Nabighian, M. N. et al. (2005), "The historical development of the magnetic method in exploration", *Geophysics*, 70(6) (evolução de instrumentação, sinal analítico, derivada tilt).
- Li, X. (2006), "Understanding 3D analytic signal amplitude", *Geophysics*, 71(2), L13-L16 (a invariância da amplitude do sinal analítico à direção de magnetização vale para fontes 2D, não para corpos 3D).
- BGS Earthwise, OR/14/014 Part 3: Data processing (fluxo de correção diurna e remoção do IGRF em levantamentos aeromagnéticos).

<!--
nivel: avancado
palavras_corpo: 2817
mapa_objetivo_secao:
  geologia-avancado-m16-oa02: "O que o magnetômetro aéreo mede" + "O campo medido não é só geologia: o que precisa ser removido" + "Redução ao polo: por que a forma da anomalia engana" + "Realces: tornando visível o que já está no dado" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: AEROGEOFIS-M16-A02-INSTRUMENTO-001
    claim: "Magnetômetros aéreos modernos (vapor de césio ou potássio, bombeados opticamente) medem a intensidade magnética total (TMI), um campo escalar; magnetômetros de precessão de prótons são de uso mais antigo. Magnetômetros vetoriais (fluxgate) medem as três componentes do campo, com exatidão absoluta menor e sujeitos a deriva, e seu papel característico a bordo é alimentar o sistema de compensação magnética da aeronave (medida de atitude em relação ao campo ambiente), não o mapeamento. Gradiômetros aeromagnéticos são construídos com múltiplos sensores ESCALARES (césio) separados espacialmente, não com fluxgates."
    risk: fato
    source: "Telford, Geldart & Sheriff 1990, Applied Geophysics, cap. 6; Nabighian et al. 2005, Geophysics 70(6), historical development of the magnetic method; Reeves 2005, cap. sobre instrumentação e compensação de aeronave. CORREÇÃO AMARELA da auditoria de 2026-09-09: a redação original atribuía ao fluxgate 'resolução angular mais grosseira' (a limitação real é exatidão absoluta e deriva) e afirmava que fluxgates são usados 'sobretudo em gradiômetros', quando o uso aeronáutico dominante é a compensação magnética da aeronave."
  - claim_id: AEROGEOFIS-M16-A02-CAMPOTOTAL-002
    claim: "A intensidade do campo magnético total da Terra na superfície varia por latitude magnética de cerca de 25.000 nT próximo ao equador magnético a cerca de 65.000 nT próximo aos polos magnéticos."
    risk: fato
    source: "Telford, Geldart & Sheriff 1990, Applied Geophysics, cap. 6 (valores de referência do campo geomagnético por latitude)."
  - claim_id: AEROGEOFIS-M16-A02-IGRF-003
    claim: "O IGRF (International Geomagnetic Reference Field) é um modelo matemático internacional do campo principal da Terra e de sua variação secular, mantido pela IAGA e atualizado a cada cinco anos; a geração mais recente, IGRF-14, teve seus coeficientes finalizados em novembro de 2024. O IGRF é removido do campo total medido para isolar a anomalia crustal, mas é uma aproximação de baixa resolução espacial que pode ser localmente imprecisa, levando ao uso de um campo regional ajustado localmente em seu lugar em alguns levantamentos."
    risk: fato
    source: "NOAA NCEI / IAGA V-MOD, International Geomagnetic Reference Field (IGRF); Wikipedia, International Geomagnetic Reference Field (data de finalização do IGRF-14); BGS Earthwise OR/14/014 Part 3 (limitações locais do IGRF e uso de modelo regional alternativo)."
  - claim_id: AEROGEOFIS-M16-A02-DIURNA-004
    claim: "A variação diurna do campo magnético, de origem externa (correntes ionosféricas/magnetosféricas moduladas pelo vento solar), é medida em tempo real por uma estação-base terrestre simultânea ao voo (por afetar toda a área do levantamento de forma aproximadamente simultânea) e removida da medida aérea; esse procedimento é distinto da remoção do IGRF, que modela uma componente de variação lenta e previsível."
    risk: fato
    source: "BGS Earthwise OR/14/014 Part 3: Data processing (correção de diurna via estação-base e remoção subsequente do IGRF); Telford, Geldart & Sheriff 1990, cap. 6."
  - claim_id: AEROGEOFIS-M16-A02-RTP-005
    claim: "A redução ao polo (RTP) corrige a distorção de forma da anomalia magnética causada pela inclinação e declinação magnética local, recalculando a anomalia como se medida no polo magnético (inclinação 90°), onde ela aparece centrada e simétrica sobre um corpo simples. A RTP é matematicamente instável em baixas latitudes magnéticas, onde a inclinação se aproxima de zero, exigindo alternativas como a redução ao equador (RTE) ou transformações independentes da direção de magnetização, como o sinal analítico."
    risk: fato
    source: "Telford, Geldart & Sheriff 1990, Applied Geophysics, cap. 6; Nabighian et al. 2005, Geophysics 70(6) (instabilidade da RTP em baixa latitude magnética e uso do sinal analítico como alternativa)."
  - claim_id: AEROGEOFIS-M16-A02-SINALANALITICO-006
    claim: "O sinal analítico é uma combinação das derivadas horizontais e vertical do campo magnético cuja amplitude é muito menos dependente da direção de magnetização do corpo causador (induzida ou remanente) e da inclinação/declinação do campo ambiente do que a anomalia de campo total, sendo especialmente útil perto do equador magnético e em corpos com magnetização remanente significativa. RESSALVA ESSENCIAL: essa invariância é rigorosa APENAS para fontes bidimensionais (diques extensos, contatos retilíneos); para corpos tridimensionais compactos a amplitude do sinal analítico volta a depender da direção de magnetização, de modo que o método não dispensa modelagem direta sobre alvos compactos e fortemente remanentes."
    risk: fato
    source: "Nabighian et al. 2005, Geophysics 70(6), historical development of the magnetic method in exploration (propriedades do sinal analítico); Li, X. (2006), Understanding 3D analytic signal amplitude, Geophysics 71(2):L13-L16 (demonstração de que a invariância à direção de magnetização vale para fontes 2D e NÃO para corpos 3D). CORREÇÃO LARANJA da auditoria de 2026-09-09: a redação original afirmava a independência como propriedade geral, sem a distinção 2D/3D, e recomendava o sinal analítico como alternativa robusta à RTP sem qualificar o alcance dessa robustez."
  - claim_id: AEROGEOFIS-M16-A02-REALCES-007
    claim: "Derivadas verticais/horizontais acentuam contrastes de curto comprimento de onda (fontes rasas); a derivada tilt normaliza amplitude e tem valor zero aproximadamente sobre a borda do corpo; continuação para cima simula voo mais alto (suprime ruído e fontes rasas, realça tendências regionais) e continuação para baixo simula voo mais baixo (acentua fontes rasas, mas amplifica ruído e só é confiável a distância limitada abaixo da altura real de voo)."
    risk: fato
    source: "Telford, Geldart & Sheriff 1990, cap. 6; Nabighian et al. 2005, Geophysics 70(6)."
-->
