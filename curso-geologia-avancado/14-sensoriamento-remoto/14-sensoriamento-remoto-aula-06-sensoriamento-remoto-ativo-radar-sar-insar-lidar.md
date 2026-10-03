# Aula 06: Sensoriamento remoto ativo: Radar/SAR, InSAR e LiDAR

**ID:** geologia-avancado-m14-a06
**Módulo:** [[14-sensoriamento-remoto-modulo|Módulo 14 — Sensoriamento remoto]]
**Duração estimada:** ~40 min (medição direta: 3.218 palavras — acima da meta de 30 min do curso; ver o registro na revisão didática do módulo)
**Nível:** avançado (especialização em geologia)
**Objetivo:** explicar o princípio físico e a geometria de aquisição do radar de abertura sintética (SAR), como a interferometria de radar (InSAR) mede deformação de superfície com precisão milimétrica a centimétrica, e como o LiDAR gera modelos de elevação de alta resolução mesmo sob cobertura vegetal.
**Ao final você vai conseguir:** explicar por que o SAR opera independentemente de luz solar e de nuvens; reconhecer e prever as distorções geométricas típicas de imagens de radar (encurtamento de rampa, inversão de relevo, sombra de radar); calcular o deslocamento de superfície a partir de uma franja de interferograma; e explicar como o LiDAR separa o retorno de topo de dossel do retorno de solo.
**Pré-requisito:** [[14-sensoriamento-remoto-aula-05-pdi-ii-transformacoes-multivariadas-classificacao|Aula 05]] — e, mais diretamente, a distinção entre sensor passivo e ativo já introduzida na Aula 01, que esta aula desenvolve em profundidade.

## Conteúdo

### Por que sensores ativos mudam o jogo: independência de luz solar e de nuvens

Toda a discussão até aqui — óptico, multiespectral, PDI — tratou de sensores **passivos**, que dependem de luz solar refletida ou de emissão térmica própria do alvo. Esta aula trata de sensores **ativos**: instrumentos que emitem sua própria energia (micro-ondas, no caso do radar; pulsos de laser, no caso do LiDAR) e medem o sinal que retorna após interagir com a superfície. Essa diferença de princípio tem duas consequências práticas que justificam, sozinhas, por que sensoriamento remoto ativo é indispensável em geociências: como a energia é emitida pelo próprio sensor, ele opera de dia ou de noite, sem depender de iluminação solar; e como as micro-ondas atravessam nuvens (ao contrário da luz visível e do infravermelho, absorvidos ou espalhados por gotículas de nuvem), o radar funciona sob cobertura de nuvem praticamente completa — uma vantagem decisiva em regiões tropicais de nebulosidade persistente, como grande parte do Brasil, onde imagens ópticas utilizáveis (a Aula 01 já discutiu esse ponto) podem ficar meses indisponíveis numa mesma área durante a estação chuvosa.

### Radar de Abertura Sintética (SAR): o princípio físico

**Radar** (*Radio Detection And Ranging*) mede a distância e as propriedades de um alvo emitindo um pulso de micro-ondas e cronometrando o tempo até o eco voltar. A energia que volta — não o tempo, mas a *quantidade* de sinal devolvida pelo alvo em direção ao sensor — é o **retroespalhamento** (*backscatter*), e é ela que dá o brilho de cada pixel numa imagem de radar: o tempo diz **onde** o alvo está, o retroespalhamento diz **como ele é**. O princípio é idêntico, em essência, ao de qualquer radar de navegação ou meteorológico, mas aplicado ao imageamento da superfície terrestre a partir de uma plataforma em movimento (satélite ou aeronave).

O termo "**abertura sintética**" resolve um problema físico específico: a resolução espacial de um radar convencional (de "abertura real") depende diretamente do tamanho físico da antena — quanto maior a antena, mais estreito o feixe e melhor a resolução — e uma antena física grande o bastante para resolução útil a partir de órbita seria fisicamente inviável de lançar. A solução do SAR é sintetizar, por processamento de sinal, uma antena efetivamente muito maior do que a antena física: à medida que o satélite se desloca ao longo de sua órbita, ele emite múltiplos pulsos sucessivos sobre o mesmo alvo, e o processamento combina esses múltiplos ecos — usando a mudança de frequência Doppler entre eles, causada pelo movimento relativo entre plataforma e alvo — como se tivessem vindo de uma antena única, com o comprimento de todo o trecho de órbita percorrido durante a aquisição. É esse truque de processamento, não uma antena fisicamente gigante, que permite ao SAR alcançar resolução espacial da ordem de metros a partir de centenas de quilômetros de altitude.

O radar opera na faixa de **micro-ondas**, e diferentes sensores usam diferentes **bandas** dentro dessa faixa, cada uma com propriedades de penetração distintas — quanto maior o comprimento de onda, maior a capacidade de penetrar em vegetação e, em certas condições, em solo seco e areia:

| Banda | Frequência aproximada | Comprimento de onda aproximado | Penetração/uso típico |
|---|---|---|---|
| X | 8-12 GHz | ~2,4-3,8 cm | pouca penetração; alta resolução, mapeamento urbano e de gelo |
| C | 4-8 GHz | ~5,6 cm | penetração moderada; o "cavalo de batalha" — Sentinel-1, RADARSAT |
| L | 1-2 GHz | ~15-30 cm | boa penetração em dossel vegetal; interesse geológico e florestal, ALOS-2, NISAR |

A escolha de banda é, mais uma vez (o mesmo padrão de compromisso já visto na Aula 01 para resoluções), uma decisão de projeto: banda X enxerga pouco além do topo do dossel vegetal e é usada onde se quer detalhe fino sobre superfície exposta; banda L penetra mais fundo na vegetação — de interesse direto para geologia em terrenos cobertos por floresta, onde o retorno em banda L carrega mais informação do solo e menos apenas da copa das árvores — e, na prática, os sistemas em banda L entregam resolução mais grosseira que os de banda X.

Vale desfazer aqui uma intuição errada e muito comum, porque ela produz uma regra falsa: **não é o comprimento de onda em si que piora a resolução do SAR**. A resolução em azimute de um SAR estripe é, notavelmente, *independente* do comprimento de onda — vale aproximadamente **D/2**, metade do comprimento físico da antena, porque um λ maior obriga o sensor a sintetizar uma abertura proporcionalmente mais longa (*L*ₛ = λ*R*/*D*) e o λ se cancela na conta. O que de fato torna os sistemas de banda L mais grosseiros são duas restrições de engenharia e de regulação: a antena física precisa ser maior para produzir um feixe utilizável em λ maior, e a largura de banda disponível (que é o que fixa a resolução em alcance) é menor nas faixas baixas do espectro alocadas ao radar. É uma limitação prática, não uma consequência da física da abertura sintética.

### Geometria de imageamento lateral e suas distorções características

Diferente de um sensor óptico, que imageia aproximadamente na vertical (ou perto disso, com pequena inclinação), o SAR imageia sempre **lateralmente** (*side-looking*), com o feixe apontado obliquamente para um dos lados da trajetória do satélite, nunca diretamente para baixo — necessidade geométrica do próprio princípio de síntese de abertura. Essa geometria oblíqua produz três distorções sistemáticas e previsíveis, que qualquer intérprete de imagem de radar precisa reconhecer antes de qualquer leitura de relevo, e que invertem intuições formadas a partir de imagens ópticas — o ponto de atenção que o hub do módulo já sinaliza como armadilha central desta aula. Qual das três ocorre não é sorteio: depende de uma comparação única e simples entre a **declividade da encosta (α)** e o **ângulo de incidência (θ)**, medido a partir da vertical local. Fixar essa comparação resolve as três de uma vez.

O **encurtamento de rampa** (*foreshortening*) ocorre em encostas voltadas para o radar, enquanto a declividade for **menor que o ângulo de incidência** (α < θ): como o pulso de radar percorre uma distância inclinada menor para alcançar o topo de uma encosta voltada para ele do que percorreria numa superfície plana equivalente, essas encostas aparecem **comprimidas e mais claras** (maior retorno concentrado numa faixa de imagem menor) do que sua extensão horizontal real sugeriria. No caso-limite α = θ, a encosta inteira colapsa numa única linha muito brilhante na imagem.

A **inversão de relevo** (*layover*) é o caso extremo do encurtamento de rampa, e começa exatamente onde ele termina: quando a declividade **supera o ângulo de incidência** (α > θ), o topo da elevação está, em termos de distância inclinada até o sensor, **mais perto** do radar do que sua própria base — o eco do topo chega ao sensor antes do eco da base, e a imagem processada posiciona o topo "deitado sobre" a base, invertendo completamente a ordem espacial do relevo. Layover é comum em terreno montanhoso íngreme e é a distorção mais severa e mais difícil de corrigir das três, porque a informação original de profundidade relativa se perde na própria aquisição — não é recuperável só reprocessando a imagem.

A **sombra de radar** (*radar shadow*) ocorre no lado oposto, e sua condição é a complementar: a encosta voltada para longe do radar entra em sombra quando sua declividade supera **90° − θ**, ou seja, quando ela é mais íngreme que o ângulo de depressão do feixe (o ângulo entre a linha de visada e a horizontal). Nessa situação a encosta bloqueia completamente o feixe de chegar à área imediatamente atrás dela, criando uma região sem nenhum retorno de sinal (aparecendo como uma faixa escura/preta na imagem, sem informação nenhuma), análoga em efeito visual — mas não em causa física — à sombra que o Sol projeta atrás de uma elevação numa imagem óptica.

O esquema abaixo põe as três num só desenho. O satélite está à esquerda, olhando obliquamente para a direita; θ é o ângulo de incidência, medido da vertical local, e α é a declividade de cada encosta.

```text
        satélite
           \
            \  θ = ângulo de incidência (da vertical)
             \      |
              \  θ  |
               \----|
                \   |
      linha de   \  |
      visada      \ |
                   \|
  ─────────────────────────────────────────────────────────────
                    ENCOSTAS VOLTADAS PARA O RADAR
                    ────────────────────────────
                       α < θ          α = θ            α > θ
                        /\             /|              /|
                       /  \           / |             / |
                      /    \         /  |            /  |
                  ENCURTAMENTO    LINHA ÚNICA      LAYOVER
                  comprimida e     brilhante      topo "deitado"
                  mais clara      (caso-limite)   sobre a base
  ─────────────────────────────────────────────────────────────
                    ENCOSTA VOLTADA PARA LONGE DO RADAR
                    ──────────────────────────────────
                          α < 90°−θ          α > 90°−θ
                             /\                /\
                            /  \              /  \
                           /    \_            /    |
                        (imagem normal,    SOMBRA DE RADAR
                         só alongada)      faixa preta, sem
                                           retorno nenhum
  ─────────────────────────────────────────────────────────────
  REGRA ÚNICA:  compare a declividade α com θ (frente) ou com
                90°−θ, o ângulo de depressão (verso).
```

Note o que o desenho torna visível e a prosa esconde: **encurtamento e layover não são dois fenômenos, são o mesmo fenômeno dos dois lados de um limiar** (α = θ), e a sombra não é o "oposto" deles — é um terceiro caso, que ocorre na outra encosta e se mede contra o outro ângulo. Note também que um mesmo θ pode produzir as três coisas na mesma cena: basta que o terreno tenha declividades diferentes.

A consequência prática dessas três distorções: interpretar relevo numa imagem SAR exige saber, antes de tudo, a direção de imageamento (de que lado o radar estava olhando) e o ângulo de incidência — a mesma feição topográfica pode aparecer comprimida numa órbita e alongada ou em sombra na órbita seguinte, dependendo apenas da geometria de aquisição, sem que nada tenha mudado no terreno real.

### Interferometria de radar (InSAR): medindo deformação de superfície com precisão de milímetros

O SAR mede não apenas a intensidade do retorno (usada para gerar a imagem de amplitude discutida até aqui), mas também a **fase** da onda retroespalhada — a posição relativa da onda dentro de seu ciclo de oscilação no momento em que retorna ao sensor. A **interferometria de radar** (InSAR) explora essa informação de fase, comparando duas imagens SAR da mesma área, adquiridas em datas diferentes (ou por duas antenas simultâneas, no caso de configurações específicas de mapeamento topográfico), a partir de órbitas geometricamente muito próximas: subtraindo a fase de uma imagem da fase da outra, pixel a pixel, gera-se um **interferograma** — um mapa de diferença de fase que se repete em ciclos completos, visualizado tipicamente como um padrão de "franjas" coloridas concêntricas.

Se a superfície não se moveu entre as duas datas de aquisição, a diferença de fase reflete apenas a diferença de geometria orbital entre as duas passagens (usada, nesse caso, para derivar topografia — a base do método usado para gerar o modelo de elevação global SRTM, mencionado no Módulo 13). Se a superfície **se deslocou** ao longo da linha de visada do radar entre as duas datas — por subsidência (afundamento do terreno, frequentemente associado a extração de água subterrânea, petróleo ou mineração subterrânea), por soerguimento, ou por deformação associada a atividade sísmica ou vulcânica — essa diferença de fase adicional se manifesta como franjas extras no interferograma, e cada ciclo completo de franja corresponde a um deslocamento de exatamente **metade do comprimento de onda** do radar utilizado, porque o sinal percorre o trajeto sensor-alvo-sensor duas vezes (ida e volta) — para o Sentinel-1 (banda C, ~5,6 cm de comprimento de onda), uma franja completa corresponde a aproximadamente 2,8 cm de deslocamento ao longo da linha de visada. Como frações de uma franja completa são mensuráveis com boa precisão no processamento, o InSAR alcança sensibilidade a deformações da ordem de milímetros a centímetros — muito além do que qualquer outra técnica de sensoriamento remoto de imageamento entrega para esse tipo de medição, e por isso o InSAR é hoje ferramenta padrão de monitoramento de subsidência de mineração e de bacias de petróleo, de estabilidade de barragens e pilhas de rejeito, e de deformação pré e pós-sísmica e vulcânica.

A técnica tem uma limitação importante: a fase medida é ambígua em múltiplos de um ciclo completo (o problema do **desdobramento de fase**, ou *phase unwrapping* — o interferograma bruto só mostra a parte fracionária de quantos ciclos de deslocamento ocorreram, não o número inteiro de ciclos, exigindo processamento adicional para reconstruir o deslocamento total), e a comparação entre duas imagens exige que a superfície mantenha **coerência** suficiente entre as datas. Coerência, aqui, é uma medida (de 0 a 1) de quanto o padrão de retroespalhamento de um pixel permaneceu o mesmo entre as duas aquisições: se os espalhadores dentro daquele pixel não se moveram nem mudaram, a fase medida é comparável e a diferença de fase significa deslocamento; se mudaram, a diferença de fase vira ruído e o interferograma não diz nada ali. Vegetação que muda rapidamente (agricultura, floresta em crescimento) degrada essa coerência e dificulta ou impede a interferometria confiável nessas áreas, restringindo a técnica, na prática, sobretudo a superfícies relativamente estáveis (rocha exposta, solo urbano, estruturas).

### LiDAR: elevação de alta resolução por tempo de voo de pulso de laser

**LiDAR** (*Light Detection And Ranging*) é, em princípio físico, análogo ao radar, mas usa pulsos de luz laser (tipicamente no infravermelho próximo, comprimento de onda em torno de 1.064 nm para a maioria dos sistemas topográficos) em vez de micro-ondas, medindo o tempo de ida e volta de cada pulso para calcular a distância entre o sensor (tipicamente aerotransportado, embora existam sistemas orbitais e terrestres) e o alvo — com a posição exata do sensor no espaço determinada simultaneamente por um sistema integrado de GNSS de alta precisão e uma unidade de medição inercial (IMU), que registra a orientação da plataforma a cada instante.

A capacidade que torna o LiDAR especialmente valioso em geologia de terreno vegetado é o **retorno múltiplo**: cada pulso de laser emitido pode gerar mais de um eco de retorno, porque parte da energia do pulso é refletida pelo topo do dossel vegetal, parte penetra por entre as folhas e galhos (através das aberturas do dossel) e é refletida por vegetação em níveis mais baixos, e a fração que consegue atravessar toda a vegetação é finalmente refletida pelo solo — sistemas LiDAR modernos registram vários desses retornos por pulso (tipicamente de 2 a vários, conforme o sistema), classificando-os posteriormente por algoritmo em categorias como "primeiro retorno" (topo de dossel), "retornos intermediários" (vegetação) e "último retorno" (predominantemente solo, quando o pulso consegue atravessar a vegetação). Filtrando a nuvem de pontos para reter apenas os últimos retornos classificados como solo, é possível gerar um **Modelo Digital de Terreno** (MDT, a superfície do terreno nu, sem vegetação nem construções — terminologia já introduzida no Módulo 13) mesmo em áreas de cobertura florestal densa, algo inviável com sensoriamento óptico passivo ou mesmo com a maioria das configurações de radar, e por isso o LiDAR aerotransportado é hoje a técnica de referência para gerar modelos de terreno de alta resolução (tipicamente submétrica a poucos metros) sob dossel florestal — uso central em mapeamento de lineamentos estruturais, deslizamentos e feições geomorfológicas finas em terrenos tropicais cobertos por vegetação densa, onde imagens ópticas e a maioria dos radares simplesmente não enxergam o solo.

## Exemplo trabalhado

**Situação:** uma mina subterrânea de carvão está sendo monitorada por InSAR usando pares de imagens Sentinel-1 (banda C, comprimento de onda ≈ 5,6 cm). Um interferograma entre duas datas separadas por 12 dias mostra 3,5 ciclos completos de franja sobre a área da mina, concentrados numa região elíptica compatível com a extensão da lavra subterrânea, e nenhuma franja significativa na área ao redor. (a) Qual é o deslocamento de superfície ao longo da linha de visada do radar nesses 12 dias? (b) Que fenômeno geológico esse padrão sugere, e por que a ausência de franjas na área ao redor é uma informação relevante?

**Resolução:**

*Parte (a) — cálculo do deslocamento.* Cada ciclo completo de franja corresponde a metade do comprimento de onda do radar, porque o sinal percorre o trajeto duas vezes (ida e volta). Para o Sentinel-1: deslocamento por franja = λ/2 = 5,6 cm / 2 = 2,8 cm. Com 3,5 ciclos completos de franja observados:

Deslocamento total = 3,5 × 2,8 cm = **9,8 cm** ao longo da linha de visada do radar, em 12 dias.

Vale notar que esse valor é o deslocamento **projetado na linha de visada do radar**, não necessariamente o deslocamento vertical puro — converter para deslocamento vertical exigiria conhecer o ângulo de incidência do radar e assumir (ou verificar independentemente) que o movimento é predominantemente vertical, hipótese razoável para subsidência mas que precisa ser declarada, não presumida silenciosamente.

*Parte (b) — interpretação geológica.* Um padrão de franjas concêntricas, restrito espacialmente a uma área elíptica que coincide com a extensão de uma lavra subterrânea ativa, e ausente na área ao redor, é a assinatura clássica de **subsidência induzida por mineração subterrânea** — o rebaixamento progressivo da superfície causado pelo colapso ou pela compactação de vazios deixados pela extração de minério em profundidade, um fenômeno que se propaga da frente de lavra até a superfície ao longo de meses a anos, dependendo da profundidade e da geometria da cavidade. A magnitude calculada, quase 10 cm em apenas 12 dias, indica uma taxa de subsidência elevada — merecendo investigação geotécnica imediata, não apenas monitoramento passivo continuado, porque taxas dessa ordem podem preceder eventos de colapso mais abruptos. A ausência de franjas na área ao redor é informação tão importante quanto a presença delas na área da mina: ela indica que o fenômeno é **espacialmente restrito** à zona de influência da lavra (não uma deformação regional mais ampla, que teria outras causas — tectônica, compactação de bacia sedimentar, rebaixamento regional de aquífero) e reforça a atribuição causal à atividade de mineração especificamente, um raciocínio de exclusão espacial que só a cobertura de área ampla do InSAR — impossível de replicar com instrumentação pontual de campo, como marcos geodésicos — torna possível de fazer com essa clareza.

## Erros comuns

- **Achar que banda L é mais grosseira porque comprimento de onda maior "piora resolução".** A aula desfaz isso explicitamente: a resolução em azimute do SAR é independente de λ (≈ D/2); banda L é mais grosseira por exigir antena física maior e ter menos largura de banda disponível — restrição de engenharia, não física da abertura sintética.
- **Confundir encurtamento de rampa com layover por não checar α contra θ.** São o mesmo fenômeno em lados opostos de um limiar (α = θ) — a regra única (comparar declividade com ângulo de incidência, e a encosta oposta com 90°−θ) resolve as três distorções de uma vez; adivinhar pela aparência visual da imagem sem essa comparação leva a erro de interpretação de relevo.
- **Interpretar deslocamento de InSAR na linha de visada como deslocamento vertical direto.** Como o próprio exemplo trabalhado ressalva, converter exige conhecer o ângulo de incidência e assumir (ou verificar) que o movimento é predominantemente vertical — presumir isso silenciosamente é o erro.
- **Tentar rodar InSAR sobre vegetação que muda rápido (agricultura, floresta em crescimento) esperando resultado confiável.** A baixa coerência entre datas transforma a diferença de fase em ruído — a técnica é restrita, na prática, a superfícies relativamente estáveis.

## O que não concluir

- **Que o radar "vê através" de qualquer nuvem e qualquer vegetação por igual.** Atravessa nuvens (todas as bandas) mas a penetração em vegetação depende da banda — X penetra pouco, L penetra mais; não é uma capacidade uniforme do "radar" genérico.
- **Que ausência de franjas no interferograma significa ausência de qualquer atividade.** Pode significar estabilidade real, mas também pode significar perda de coerência (vegetação mudando) — a ausência de franja só é informativa quando se sabe que a coerência ali era suficiente para medir.
- **Que o LiDAR sempre atravessa a vegetação até o solo em qualquer densidade de dossel.** A fração de energia que penetra depende das aberturas do dossel; em floresta extremamente densa, menos pulsos alcançam o solo, e a qualidade do MDT resultante depende dessa fração de últimos retornos disponível.

## Recap relâmpago

- Sensores ativos (radar, LiDAR) emitem sua própria energia e medem o retorno; por isso operam independentemente de luz solar, e o radar de micro-ondas atravessa nuvens — vantagem decisiva em regiões tropicais de nebulosidade persistente.
- SAR sintetiza, por processamento de sinal ao longo da trajetória orbital, uma antena efetivamente muito maior que a antena física, alcançando resolução métrica a partir de órbita; bandas de radar mais longas (L) penetram mais em vegetação, bandas mais curtas (X) são usadas onde se quer detalhe fino. Cuidado com a regra falsa: a resolução em azimute do SAR é **independente do comprimento de onda** (≈ D/2, metade da antena física) — os sistemas de banda L são mais grosseiros por exigirem antena maior e por terem menos largura de banda disponível, não por causa do λ em si.
- A geometria de imageamento lateral do SAR produz três distorções sistemáticas, e qual delas ocorre depende de comparar a declividade da encosta (α) com o ângulo de incidência (θ): encurtamento de rampa quando α < θ (encostas voltadas ao radar aparecem comprimidas e claras), inversão de relevo/layover quando α > θ (topo "deitado" sobre a base) e sombra de radar quando a encosta oposta é mais íngreme que 90° − θ (área sem retorno) — reconhecer a geometria de aquisição é pré-requisito para interpretar relevo em imagem SAR.
- InSAR compara a fase de duas imagens SAR da mesma área em datas diferentes; cada ciclo completo de franja no interferograma corresponde a metade do comprimento de onda do radar (deslocamento ida e volta), permitindo medir deformação de superfície com precisão de milímetros a centímetros — aplicado a subsidência de mineração, deformação de bacias, estabilidade de barragens e monitoramento sísmico/vulcânico.
- InSAR exige desdobramento de fase (resolver a ambiguidade de múltiplos ciclos) e depende de coerência de retroespalhamento entre as datas comparadas — vegetação que muda rapidamente degrada ou inviabiliza a técnica nessas áreas.
- LiDAR mede distância por tempo de voo de pulsos de laser (tipicamente ~1.064 nm); o registro de múltiplos retornos por pulso permite separar topo de dossel, vegetação intermediária e solo, gerando Modelos Digitais de Terreno de alta resolução mesmo sob floresta densa — capacidade que nem o sensoriamento óptico nem a maioria dos radares replicam.

## Próxima aula

[[14-sensoriamento-remoto-aula-07-fotogrametria-produtos-3d-sensoriamento-termal|Aula 07 — Fotogrametria digital, produtos 3D e sensoriamento remoto termal (TIR)]] — última aula do módulo: fecha o conjunto de técnicas de geração de modelos tridimensionais (agora por fotogrametria, complementando o LiDAR desta aula) e retoma o sensoriamento termal, mencionado desde a Aula 02 mas ainda não desenvolvido em profundidade.

## Fontes

- Woodhouse, I. H. (2006), *Introduction to Microwave Remote Sensing*, CRC Press, cap. 5-7 e 9 (princípio do SAR, bandas de radar, geometria de imageamento lateral e distorções, fundamentos de InSAR).
- Hanssen, R. F. (2001), *Radar Interferometry: Data Interpretation and Error Analysis*, Kluwer Academic Publishers (referência padrão de InSAR, relação franja-deslocamento, desdobramento de fase).
- ESA/Copernicus, *Sentinel-1 User Handbook* e material técnico de interferometria (comprimento de onda banda C, ~5,6 cm; relação deslocamento por franja).
- NASA Earthdata, "Synthetic Aperture Radar (SAR)" — bandas de radar (X, C, L) e aplicações (referência de frequência/comprimento de onda por banda).
- Wehr, A. & Lohr, U. (1999), "Airborne laser scanning — an introduction and overview", *ISPRS Journal of Photogrammetry and Remote Sensing*, 54(2-3) (princípio do LiDAR aerotransportado, retornos múltiplos, geração de MDT sob vegetação).

<!--
nivel: avancado
palavras_corpo: 3218
mapa_objetivo_secao:
  geologia-avancado-m14-oa04: "Por que sensores ativos mudam o jogo: independência de luz solar e de nuvens" + "Radar de Abertura Sintética (SAR): o princípio físico" + "Geometria de imageamento lateral e suas distorções características" + "Interferometria de radar (InSAR): medindo deformação de superfície com precisão de milímetros" + "LiDAR: elevação de alta resolução por tempo de voo de pulso de laser" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: SENSREM-M14-A06-SARPRINCIPIO-001
    claim: "SAR sintetiza, por processamento de sinal explorando a mudança de frequência Doppler entre pulsos sucessivos ao longo da trajetória orbital, uma antena efetivamente muito maior que a antena física real, alcançando resolução espacial da ordem de metros a partir de altitude orbital — capacidade inviável com uma antena de abertura real de tamanho fisicamente lançável."
    risk: fato
    source: "Woodhouse 2006, Introduction to Microwave Remote Sensing, cap. 5-6"
  - claim_id: SENSREM-M14-A06-BANDAS-002
    claim: "Bandas de radar comumente usadas em sensoriamento remoto: banda X (~8-12 GHz, ~2,4-3,8 cm), banda C (~4-8 GHz; o Sentinel-1 opera a 5,405 GHz, ~5,6 cm; tambem RADARSAT) e banda L (~1-2 GHz, ~15-30 cm, usada pelo ALOS-2 e pelo NISAR); comprimentos de onda maiores (banda L) penetram mais em dossel vegetal do que comprimentos de onda menores (banda X)."
    risk: fato
    source: "NASA Earthdata, Synthetic Aperture Radar (SAR); ESA/Copernicus Sentinel-1 User Handbook — valores de frequência/comprimento de onda consolidados na literatura de SAR"
  - claim_id: SENSREM-M14-A06-RESOLUCAOAZIMUTE-006
    claim: "A resolução em azimute de um SAR estripe é independente do comprimento de onda, valendo aproximadamente D/2 (metade do comprimento físico da antena), porque um comprimento de onda maior obriga a sintetizar uma abertura proporcionalmente mais longa (Ls = lambda.R/D) e o lambda se cancela. Os sistemas de banda L entregam resolução mais grosseira que os de banda X por restrições práticas — antena física maior necessária e menor largura de banda disponível/alocada, que é o que fixa a resolução em alcance — e não por consequência direta do comprimento de onda na geometria de abertura sintética."
    risk: fato
    source: "Woodhouse 2006, Introduction to Microwave Remote Sensing, cap. 6-7; formulação padrão de resolução azimutal de SAR (delta_az = D/2). Acrescentado na auditoria do Modulo 14 (claim SENSREM-M14-A06-BANDALRESOL-006): a redacao anterior atribuía a resolução mais grosseira da banda L ao comprimento de onda 'para uma mesma abertura sintética', o que induz a regra falsa 'lambda maior implica pior resolução'."
  - claim_id: SENSREM-M14-A06-DISTORCOES-003
    claim: "A geometria de imageamento lateral do SAR produz três distorções geométricas sistemáticas, discriminadas pela comparação entre a declividade da encosta (alfa) e o ângulo de incidência (teta), medido a partir da vertical local: encurtamento de rampa/foreshortening quando alfa < teta (encostas voltadas ao radar aparecem comprimidas e mais claras; no limite alfa = teta a encosta colapsa numa linha brilhante), inversão de relevo/layover quando alfa > teta (o eco do topo chega ao sensor antes do eco da base, invertendo a ordem espacial na imagem) e sombra de radar quando a encosta oposta é mais íngreme que 90 graus menos teta, isto é, que o ângulo de depressão (ausência de retorno). Condições angulares explicitadas na auditoria do Modulo 14 (claim SENSREM-M14-A06-LAYOVER-007), que antes estavam formuladas contra uma 'linha de visada'/'ângulo de visada' não definida."
    risk: fato
    source: "Woodhouse 2006, Introduction to Microwave Remote Sensing, cap. 6; Sabins & Ellis 2020, Remote Sensing, cap. 4 (distorções geométricas de imagens de radar)"
  - claim_id: SENSREM-M14-A06-INSAR-004
    claim: "Em InSAR, cada ciclo completo de franja no interferograma corresponde a um deslocamento de superfície ao longo da linha de visada do radar igual a metade do comprimento de onda usado, porque o sinal percorre o trajeto sensor-alvo-sensor duas vezes; para o Sentinel-1 (banda C, comprimento de onda ≈ 5,6 cm), isso equivale a aproximadamente 2,8 cm por franja completa, permitindo medir deformação com sensibilidade de milímetros a centímetros."
    risk: fato
    source: "Hanssen 2001, Radar Interferometry, cap. 2-3; ESA, How does interferometry work? e Sentinel-1 InSAR Product Guide (ASF/HyP3)"
  - claim_id: SENSREM-M14-A06-LIDAR-005
    claim: "LiDAR mede distância por tempo de voo de pulsos de laser, tipicamente na faixa de infravermelho próximo em torno de 1.064 nm para a maioria dos sistemas topográficos aerotransportados; o registro de múltiplos retornos por pulso (primeiro retorno de topo de dossel, retornos intermediários de vegetação, último retorno predominantemente de solo) permite gerar Modelos Digitais de Terreno de alta resolução mesmo sob cobertura florestal densa, filtrando a nuvem de pontos para reter apenas os retornos classificados como solo."
    risk: aproximacao
    source: "Wehr & Lohr 1999, ISPRS Journal of Photogrammetry and Remote Sensing 54(2-3); o comprimento de onda exato varia por fabricante/sistema (tipicamente na faixa de 900-1550 nm para sistemas topográficos), 1.064 nm citado como valor de referência comum, não universal"
-->
