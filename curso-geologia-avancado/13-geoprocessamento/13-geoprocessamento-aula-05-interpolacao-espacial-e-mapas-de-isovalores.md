# Aula 05: Interpolação espacial e mapas de isovalores a partir de nuvens de pontos

**ID:** geologia-avancado-m13-a05
**Módulo:** [[13-geoprocessamento-modulo|Módulo 13 — Geoprocessamento]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** aplicar métodos de interpolação espacial para transformar uma nuvem de pontos amostrados em uma superfície contínua (raster) e um mapa de isovalores, e escolher o método adequado a cada tipo de dado.
**Ao final você vai conseguir:** explicar o que a interpolação espacial resolve e por que todo interpolador produz um mapa "convincente" mesmo quando os dados não sustentam a superfície; comparar IDW, krigagem e interpolação por spline; e construir e interpretar um mapa de isovalores (isolinhas) a partir de uma superfície interpolada.
**Pré-requisito:** [[13-geoprocessamento-aula-02-ambiente-sig-estruturas-vetorial-e-matricial|Aula 02]]. Esta aula assume que você domina a diferença entre vetor e raster (Aula 02) — a interpolação é justamente a operação que converte uma camada vetorial de pontos amostrados numa superfície raster contínua. A [[13-geoprocessamento-aula-04-geoprocessamento-vetorial-operacoes-espaciais|Aula 04]] vem antes na sequência do módulo, mas nada aqui depende dela: se você chegou direto da Aula 02, pode seguir.

## Conteúdo

### O problema que a interpolação resolve

Um projeto de geociências raramente tem dados em todo lugar: uma campanha de amostragem geoquímica coleta solo em algumas dezenas ou centenas de pontos discretos, um levantamento de nível d'água mede o nível em alguns poços de monitoramento, um mapeamento estrutural registra atitude de acamamento em afloramentos esparsos. Mas a pergunta que geralmente importa não é "qual é o teor no ponto 17?" — é "qual é o teor em qualquer lugar da área, inclusive onde não houve amostragem?". A **interpolação espacial** é o conjunto de métodos que estimam o valor de uma variável em locais não amostrados, a partir dos valores conhecidos em pontos amostrados, apoiados na premissa geoestatística básica de que **pontos mais próximos tendem a ter valores mais parecidos que pontos mais distantes** (a chamada primeira lei da geografia, atribuída a Waldo Tobler).

O resultado de uma interpolação é tipicamente uma superfície contínua — na prática, um raster (Aula 02), onde cada célula recebe um valor estimado — que pode então ser representada visualmente como um **mapa de isovalores** (também chamado mapa de contorno, ou, no caso específico de teores químicos, mapa de isoteores): um conjunto de **isolinhas**, linhas que conectam pontos de igual valor da variável interpolada, exatamente como as curvas de nível conectam pontos de igual altitude num mapa topográfico (a curva de nível é, tecnicamente, um caso particular de isolinha, aplicado à variável elevação).

### O aviso mais importante desta aula: todo interpolador produz um mapa convincente

Antes de descrever os métodos, vale registrar o ponto de maior risco prático desta aula — citado já no hub do módulo como um dos dois pontos de dificuldade centrais: **qualquer método de interpolação, aplicado a qualquer conjunto de pontos, produz uma superfície de aparência suave e visualmente convincente, mesmo quando os dados de entrada não sustentam estatisticamente aquela superfície**. Um software de SIG não recusa interpolar dez pontos espalhados aleatoriamente numa área de 10.000 km² — ele gera o mapa de isovalores igual assim, com a mesma aparência profissional de um mapa gerado a partir de mil pontos bem distribuídos. A validade do resultado depende inteiramente de três fatores que o mapa, por si, não revela visualmente: a densidade e distribuição espacial dos pontos amostrais, a adequação estatística do método escolhido à estrutura espacial real da variável, e a validação do resultado contra pontos não usados no ajuste (técnica chamada validação cruzada). Essa é a razão pela qual a escolha e a calibração do interpolador nunca deveriam ser tratadas como um passo puramente automático de software.

### IDW (Inverso da Distância Ponderada)

O **IDW** (*Inverse Distance Weighting*) estima o valor de um ponto não amostrado como uma média ponderada dos valores dos pontos amostrados vizinhos, em que o peso de cada ponto amostral diminui com a distância ao ponto estimado, segundo uma potência (expoente) definida pelo operador — tipicamente potência 2 como padrão, embora valores maiores concentrem ainda mais a influência dos pontos mais próximos. É um método **determinístico** (não estatístico): não estima incerteza, não assume um modelo de variação espacial subjacente, apenas aplica a regra "quanto mais perto, mais peso" de forma direta. Sua vantagem é a simplicidade conceitual e computacional, e ele funciona razoavelmente bem quando a densidade amostral é alta e relativamente uniforme. Sua limitação central é que o IDW nunca extrapola além do intervalo de valores observados (o resultado interpolado está sempre entre o mínimo e o máximo dos pontos amostrais usados) e tende a criar padrões visuais em "olho de boi" concêntricos ao redor de cada ponto amostral isolado, especialmente em áreas de baixa densidade de amostragem — um artefato visual do método, não necessariamente um reflexo da variação real do fenômeno.

### Krigagem (kriging)

A **krigagem** é um método de interpolação **geoestatístico**, baseado na análise da estrutura de autocorrelação espacial dos dados — expressa por meio de um **variograma** (uma função que descreve como a diferença esperada entre os valores de dois pontos aumenta com a distância entre eles). A krigagem usa esse variograma ajustado para calcular pesos ótimos (no sentido estatístico de minimizar o erro esperado de estimativa) para cada ponto amostral na estimativa de cada local não amostrado, e — diferentemente do IDW — fornece, além do valor estimado, uma **estimativa da incerteza** dessa estimativa (a variância de krigagem), que é maior em áreas de baixa densidade amostral e menor perto de pontos amostrados. Essa capacidade de quantificar a própria incerteza é a razão pela qual a krigagem é, entre os métodos apresentados, o de escolha preferencial em aplicações onde a decisão subsequente tem custo alto — como estimativa de recursos minerais (tema retomado com muito mais profundidade nos módulos de geoestatística mais adiante no curso, Módulos 20-21) — porque permite comunicar não apenas "qual é o valor estimado", mas "quão confiável é essa estimativa naquele ponto específico". A contrapartida é a exigência de mais trabalho analítico prévio: ajustar corretamente um variograma exige entender a estrutura espacial dos dados, não é um botão a apertar sem julgamento.

### Interpolação por spline

A interpolação por **spline** ajusta uma superfície matemática suave (tipicamente baseada em funções polinomiais por partes) que passa exatamente pelos valores dos pontos amostrais, minimizando a curvatura total da superfície resultante — produzindo, por construção, a superfície visualmente mais suave entre os métodos apresentados, sem os padrões concêntricos do IDW. É adequada para variáveis que de fato variam suavemente no espaço (como uma superfície topográfica ou uma superfície potenciométrica de aquífero, retomando o Módulo 01), mas tem uma limitação importante: ao contrário do IDW, o spline **pode extrapolar além do intervalo de valores observados**, gerando picos ou depressões artificiais em regiões de baixa densidade amostral ou de mudança abrupta nos dados vizinhos — um risco que a própria suavidade do método, paradoxalmente, torna mais fácil de não perceber visualmente.

```
Comparação esquemática dos três métodos (perfil 1D através de pontos amostrais •)

  IDW: pesos por distância,              Krigagem: pesos ótimos por
  nunca extrapola além do                variograma + incerteza
  intervalo observado                    estimada (maior longe dos pontos)

  valor                                  valor        ┊ banda de incerteza
    •＿＿                                  •＿＿      ┊ mais larga aqui
        ‾‾•＿＿   •＿＿‾‾•                     ‾‾•＿＿ ┊  •＿＿‾‾•
                                                      ┊

  Spline: superfície suave, pode
  extrapolar além do intervalo
  observado (pico/depressão artificial)

  valor
    •＿＿
        ‾‾•＼＿＿   •＿＿‾‾•   ← possível overshoot
              ＼＿／  entre pontos distantes
```
A legenda a reter: os três métodos, aplicados aos mesmos pontos, produzem superfícies visivelmente diferentes — a escolha do método muda o resultado, não apenas sua aparência.

### Construindo e lendo um mapa de isovalores

Uma vez gerada a superfície interpolada (o raster contínuo), o mapa de isovalores é produzido traçando isolinhas em intervalos regulares de valor (o **intervalo de contorno**, análogo à equidistância das curvas de nível topográficas) — cada isolinha conecta todos os pontos da superfície com exatamente aquele valor. A leitura de um mapa de isovalores segue os mesmos princípios de leitura de curvas de nível: isolinhas mais próximas entre si indicam gradiente espacial mais acentuado (a variável muda rapidamente numa distância curta); isolinhas mais espaçadas indicam variação mais suave; um conjunto de isolinhas fechadas ao redor de um ponto indica um máximo ou mínimo local (um "pico" ou uma "depressão" da variável interpolada, distinguíveis pelo valor crescente ou decrescente das isolinhas concêntricas). Um mapa de isovalores geoquímico, por exemplo, usa exatamente essa lógica para identificar **anomalias** — áreas onde as isolinhas se fecham em torno de um valor muito mais alto que o entorno, frequentemente o primeiro indício visual de um alvo de prospecção mineral a ser investigado com mais detalhe.

## Exemplo trabalhado

**Situação:** uma campanha de amostragem de água subterrânea mediu a concentração de um contaminante em 15 poços de monitoramento distribuídos de forma desigual numa área de 4 km² — 12 poços concentrados numa faixa de 1 km² próxima a uma fonte conhecida de contaminação, e apenas 3 poços espalhados pelo restante dos 3 km². O geólogo quer produzir um mapa de isovalores da concentração para toda a área de 4 km². **(a)** Que fator deve pesar mais na escolha entre IDW e krigagem, e o que o mapa resultante pode e não pode afirmar com confiança? **(b)** Pronto o mapa, com isolinhas traçadas a cada 10 µg/L, ele mostra isolinhas muito próximas entre si a leste da fonte, isolinhas amplamente espaçadas a oeste, e um conjunto de isolinhas fechadas em torno de um poço no centro da faixa densa, com valores crescentes para dentro. Como se lê cada um desses três padrões?

**Resolução:**

*(a) Escolha do método.* O fator decisivo aqui não é qual método é "melhor" em abstrato — é que a **distribuição amostral é fortemente desigual**, com densidade alta numa pequena parte da área e densidade muito baixa no restante. Esse é exatamente o cenário em que a diferença prática entre IDW e krigagem mais importa: o IDW vai gerar um mapa de aparência completa e suave em toda a extensão dos 4 km², sem qualquer indicação visual de que a estimativa nos 3 km² pouco amostrados é muito menos confiável que a estimativa na faixa densamente amostrada — a mesma armadilha de "todo interpolador produz um mapa convincente" discutida no início desta aula. A krigagem, por gerar simultaneamente a superfície de valor estimado e a superfície de variância de krigagem, permite ao geólogo produzir um segundo mapa (ou uma faixa de confiança sobreposta ao primeiro) que mostra explicitamente onde a estimativa é robusta (dentro e perto da faixa dos 12 poços) e onde é essencialmente uma extrapolação de baixa confiança (a maior parte dos 3 km² restantes, cobertos por apenas 3 poços esparsos).

A escolha recomendada, portanto, é a **krigagem**, precisamente pela capacidade de quantificar essa incerteza desigual — não porque a krigagem seja intrinsecamente superior ao IDW em qualquer situação, mas porque este cenário específico (amostragem muito desigual, decisão de risco ambiental potencialmente cara) é exatamente o caso de uso em que a informação de incerteza tem valor prático direto. O mapa final pode afirmar com confiança a forma da pluma de contaminação dentro e perto da faixa densamente amostrada; não pode afirmar, com o mesmo grau de confiança, o valor estimado nas partes mais distantes dos 3 km² menos amostrados — e o relatório técnico deve comunicar essa diferença de confiança explicitamente, em vez de apresentar o mapa de isovalores inteiro como se toda a área tivesse o mesmo grau de certeza. Essa é uma instância concreta, aplicada a este módulo, do mesmo princípio de honestidade sobre limitação de dados que perpassa o curso desde os primeiros módulos de hidrogeologia.

*(b) Leitura do mapa de isovalores.* Os três padrões se leem com as regras da seção anterior — e o terceiro só se lê corretamente combinando-as com a resposta do item (a):

- **Isolinhas muito próximas a leste da fonte**: gradiente espacial acentuado — a concentração cai (ou sobe) muito em pouca distância. Com o intervalo de contorno de 10 µg/L, isolinhas separadas por poucos metros significam dezenas de µg/L de variação numa distância curta. É onde a pluma tem borda nítida.
- **Isolinhas amplamente espaçadas a oeste**: gradiente suave — a variável muda pouco ao longo de bastante distância. Aqui, porém, entra a ressalva do item (a): esse trecho está nos 3 km² cobertos por apenas 3 poços, e **suavidade em área pouco amostrada não é observação, é consequência do interpolador**. Nenhum dado sustenta que o gradiente seja realmente suave ali; a superfície de variância de krigagem é o que permite dizer isso ao leitor do relatório, e o mapa de isovalores sozinho, não.
- **Isolinhas fechadas com valores crescentes para dentro, em torno de um poço**: máximo local — um pico de concentração. Como está dentro da faixa densamente amostrada, é um máximo sustentado por dados vizinhos, e não um artefato: é exatamente o padrão que, num mapa geoquímico, se chamaria anomalia, e aqui aponta o ponto de maior concentração medida da pluma.

O contraste entre o segundo e o terceiro item é a lição a levar: **a mesma regra de leitura aplicada a duas regiões do mesmo mapa produz uma conclusão confiável e uma conclusão vazia**, e a única coisa que separa as duas é a densidade amostral — informação que não está desenhada nas isolinhas.

## Erros comuns

- **Aceitar um mapa de isovalores como evidência de confiança uniforme.** É o erro central que esta aula existe para prevenir: o software gera a mesma aparência profissional para 10 pontos esparsos ou 1.000 bem distribuídos, e nada no mapa em si avisa qual é o caso.
- **Escolher IDW por padrão do software sem considerar a distribuição amostral.** Como o exemplo trabalhado mostra, numa amostragem muito desigual o IDW esconde exatamente a informação (onde a estimativa é confiável) que mais importa comunicar — a krigagem existe, entre outras razões, para essa situação específica.
- **Ler isolinhas amplamente espaçadas em área pouco amostrada como "gradiente real suave".** Suavidade em região de baixa densidade de pontos costuma ser artefato do interpolador, não observação — só a variância de krigagem (ou uma verificação direta da densidade amostral) distingue as duas coisas.
- **Usar spline para uma variável que pode ter mudança abrupta real** (um contato geológico, uma descontinuidade de falha). A suavidade do spline é uma escolha de modelo, não uma propriedade neutra — impor suavidade a um fenômeno que varia abruptamente produz picos e depressões que não existem no terreno.

## O que não concluir

- **Que krigagem é sempre a escolha certa por ser "mais sofisticada".** Krigagem exige ajuste de variograma com julgamento analítico real; para dados densos e uniformes, o ganho sobre IDW pode não justificar o trabalho extra — a escolha depende do cenário, não de uma hierarquia fixa de qualidade dos métodos.
- **Que o IDW nunca erra por não extrapolar além do intervalo observado.** Não extrapolar evita um tipo de erro (picos irreais), mas o padrão de "olho de boi" ao redor de pontos isolados é um erro visual diferente, igualmente capaz de induzir uma leitura errada do fenômeno.
- **Que uma anomalia geoquímica identificada por isolinhas fechadas é automaticamente um alvo confirmado.** É o primeiro indício visual, dentro da área bem amostrada — ainda exige investigação de campo adicional antes de qualquer decisão de investimento, exatamente como o exemplo trabalhado trata o pico dentro da faixa densa como ponto de partida, não conclusão.

## Recap relâmpago

- A interpolação espacial estima o valor de uma variável em locais não amostrados a partir de pontos amostrados conhecidos, apoiada na premissa de que pontos próximos tendem a valores mais parecidos.
- Todo método de interpolação produz um mapa de aparência convincente independentemente da densidade ou distribuição real dos dados — a validade do resultado depende de fatores que o mapa não revela visualmente por si só.
- IDW é determinístico, pondera pelo inverso da distância, nunca extrapola além do intervalo observado, mas produz padrões de "olho de boi" em baixa densidade amostral.
- Krigagem é geoestatística, baseada em variograma, fornece tanto o valor estimado quanto sua incerteza (variância de krigagem) — preferível quando a decisão subsequente tem custo alto e a amostragem é desigual.
- Spline produz a superfície mais suave visualmente, mas pode extrapolar além do intervalo de valores observados, gerando picos ou depressões artificiais.
- Um mapa de isovalores conecta pontos de igual valor da superfície interpolada; isolinhas próximas indicam gradiente acentuado, isolinhas fechadas indicam máximo ou mínimo local (anomalias, no caso geoquímico).

## Próxima aula

[[13-geoprocessamento-aula-06-modelos-digitais-de-elevacao-declividade-hipsometria-hidrologia|Aula 06 — Modelos digitais de elevação: declividade, hipsometria, análise hidrológica e extração de lineamentos]]

## Fontes

- Isaaks, E. H. & Srivastava, R. M. (1989), *An Introduction to Applied Geostatistics*, Oxford University Press, cap. 1-5, 12 (IDW, variograma, krigagem).
- Burrough, P. A. & McDonnell, R. A. (1998), *Principles of Geographical Information Systems*, Oxford University Press, cap. 5 — *Creating Continuous Surfaces from Point Data* (IDW, spline e demais interpoladores determinísticos) e cap. 6 — *Optimal Interpolation using Geostatistics* (variograma e krigagem).
- Tobler, W. R. (1970), "A Computer Movie Simulating Urban Growth in the Detroit Region", *Economic Geography*, 46(sup1), 234-240 (primeira formulação da "primeira lei da geografia").

<!--
nivel: avancado
palavras_corpo: 2210  # recontado apos auditoria + revisao didatica (2026-09-08)
mapa_objetivo_secao:
  geologia-avancado-m13-oa03: "O problema que a interpolação resolve" + "O aviso mais importante desta aula: todo interpolador produz um mapa convincente" + "IDW (Inverso da Distância Ponderada)" + "Krigagem (kriging)" + "Interpolação por spline" + "Construindo e lendo um mapa de isovalores" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOPROC-M13-A05-TOBLER-001
    claim: "A premissa de que pontos espacialmente mais próximos tendem a ter valores mais parecidos que pontos mais distantes é conhecida como 'primeira lei da geografia', formulação atribuída a Waldo Tobler (1970)."
    risk: fato
    source: "Tobler 1970, A Computer Movie Simulating Urban Growth in the Detroit Region, Economic Geography 46(sup1)"
  - claim_id: GEOPROC-M13-A05-IDW-002
    claim: "IDW (Inverse Distance Weighting) é um método de interpolação determinístico que estima o valor em um ponto não amostrado como média ponderada dos pontos amostrais vizinhos, com peso decrescente segundo uma potência da distância; não estima incerteza; o valor interpolado nunca excede o intervalo mínimo-máximo dos pontos amostrais usados na estimativa."
    risk: fato
    source: "Burrough & McDonnell 1998, Principles of GIS, cap. 5 (Creating Continuous Surfaces from Point Data); Isaaks & Srivastava 1989, An Introduction to Applied Geostatistics"
  - claim_id: GEOPROC-M13-A05-KRIGAGEM-003
    claim: "Krigagem é um método de interpolação geoestatístico baseado na análise de autocorrelação espacial via variograma, que calcula pesos que minimizam o erro esperado de estimativa (melhor estimador linear não-viesado, no sentido geoestatístico) e fornece, além do valor estimado, uma estimativa de incerteza (variância de krigagem) maior em áreas de menor densidade amostral."
    risk: fato
    source: "Isaaks & Srivastava 1989, An Introduction to Applied Geostatistics, cap. 12; Burrough & McDonnell 1998, cap. 6 (Optimal Interpolation using Geostatistics)"
  - claim_id: GEOPROC-M13-A05-SPLINE-004
    claim: "Interpolação por spline ajusta uma superfície suave (funções polinomiais por partes) que passa exatamente pelos pontos amostrais, minimizando a curvatura total da superfície; ao contrário do IDW, o resultado pode extrapolar além do intervalo mínimo-máximo dos valores amostrais observados."
    risk: fato
    source: "Burrough & McDonnell 1998, Principles of GIS, cap. 5 (Creating Continuous Surfaces from Point Data)"
  - claim_id: GEOPROC-M13-A05-ISOLINHAS-005
    claim: "Um mapa de isovalores é formado por isolinhas que conectam pontos de igual valor de uma superfície interpolada, seguindo os mesmos princípios de leitura das curvas de nível topográficas: isolinhas mais próximas indicam gradiente espacial mais acentuado, isolinhas fechadas ao redor de um ponto indicam máximo ou mínimo local."
    risk: fato
    source: "Convenção cartográfica padrão de representação por isolinhas, consistente com Burrough & McDonnell 1998 e a prática de mapeamento geoquímico/topográfico"
-->
