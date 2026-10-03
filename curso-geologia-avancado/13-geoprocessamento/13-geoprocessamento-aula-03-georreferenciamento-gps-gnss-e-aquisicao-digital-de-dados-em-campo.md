# Aula 03: Georreferenciamento, GPS/GNSS e aquisição digital de dados em campo

**ID:** geologia-avancado-m13-a03
**Módulo:** [[13-geoprocessamento-modulo|Módulo 13 — Geoprocessamento]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** explicar como um mapa antigo sem coordenadas embutidas ou um dado coletado em campo entram, de forma posicionalmente correta, dentro de um sistema de referência e de uma base de dados espacial em SIG.
**Ao final você vai conseguir:** georreferenciar uma imagem ou mapa escaneado usando pontos de controle; explicar a diferença entre as constelações de satélite (GPS, GNSS) e entre os modos de posicionamento (autônomo, diferencial, RTK); e planejar uma campanha de coleta digital de dados de campo compatível com o SIG do projeto.
**Pré-requisito:** [[13-geoprocessamento-aula-01-fundamentos-cartograficos|Aula 01]] e [[13-geoprocessamento-aula-02-ambiente-sig-estruturas-vetorial-e-matricial|Aula 02]]. Esta aula assume domínio de datum/projeção (Aula 01) e da diferença entre vetor e raster (Aula 02) — georreferenciar é justamente inserir um raster (a imagem escaneada) dentro do sistema de referência do projeto.

## Conteúdo

### O problema: dados sem coordenadas embutidas

As duas aulas anteriores assumiram, implicitamente, que os dados já chegavam com coordenadas — um shapefile, uma planilha com colunas X/Y. Mas boa parte dos dados que um projeto de geociências precisa incorporar não nasce assim: um mapa geológico antigo em papel, escaneado; uma foto aérea histórica; um croqui de campo desenhado à mão. Esses dados existem como uma imagem — uma matriz de pixels sem qualquer informação de coordenada real associada, apenas sua própria grade de linhas e colunas de pixel. O processo que resolve isso é o **georreferenciamento**: atribuir a uma imagem (ou a um conjunto de dados sem coordenadas) um sistema de referência espacial real, de modo que ela passe a se sobrepor corretamente a outras camadas do projeto.

Esta aula cobre as duas fontes mais comuns de dados sem coordenada embutida em geociências — imagens/mapas antigos (resolvidos por georreferenciamento por pontos de controle) e dados coletados diretamente em campo (resolvidos por posicionamento GPS/GNSS) — fechando, com a Aula 02, o ciclo de como um dado entra corretamente estruturado e posicionado num SIG antes de qualquer análise.

### Georreferenciamento por pontos de controle

O método padrão de georreferenciamento consiste em identificar, na imagem sem coordenadas, um conjunto de **pontos de controle** (*ground control points*, GCPs) — feições reconhecíveis tanto na imagem quanto numa camada de referência já corretamente georreferenciada (uma imagem de satélite atual, um mapa topográfico oficial, ou coordenadas de campo coletadas por GPS). Para cada ponto de controle, o operador registra duas coisas: a posição do ponto em coordenadas de pixel (linha, coluna, na imagem original) e sua posição em coordenadas reais (x, y, no sistema de referência do projeto). A partir de um conjunto suficiente desses pares, o software ajusta uma **transformação matemática** (tipicamente uma transformação polinomial de primeiro grau — afim, que preserva paralelismo de linhas — ou de grau maior, para imagens com distorção não linear mais complexa, como fotografias aéreas antigas com deformação de lente ou de escaneamento) que mapeia qualquer pixel da imagem original para sua coordenada real correspondente.

A qualidade do georreferenciamento depende de três fatores práticos: (1) o **número de pontos de controle** — o mínimo matemático para uma transformação afim é três pontos não colineares, mas projetos reais usam bem mais, tipicamente 6 a 12 ou mais, para permitir avaliar o erro; (2) a **distribuição espacial** dos pontos — pontos concentrados numa única região da imagem produzem uma transformação instável fora dessa região, então a boa prática é distribuir os pontos de controle ao longo de toda a extensão da imagem, incluindo as bordas; (3) a **qualidade da identificação** — cada ponto de controle deve ser uma feição pontual inequívoca e estável no tempo (um cruzamento de estradas, a foz de um rio, um marco geodésico), nunca uma feição ambígua ou que muda de posição (a borda de uma mancha de vegetação, por exemplo).

O resultado numérico que avalia a qualidade do ajuste é o **RMSE** (*root mean square error*, erro quadrático médio), calculado a partir da diferença entre a posição real de cada ponto de controle e a posição que a transformação ajustada produziria para ele — quanto menor o RMSE, mais consistente é a transformação com o conjunto de pontos usado. Um RMSE aceitável depende da escala de trabalho: um erro de 5 m pode ser irrelevante num mapa regional 1:100.000, mas inaceitável num levantamento de detalhe 1:1.000 (retomando o vínculo entre escala e precisão posicional já visto na Aula 01).

```
Georreferenciamento por pontos de controle (esquemático)

  Imagem sem coordenadas (pixel: linha, coluna)     Sistema de referência real (x, y)
     ┌───────────────────┐                              ┌───────────────────┐
     │   •GCP1            │      transformação           │      •GCP1 (x1,y1) │
     │         •GCP2       │   ───────────────────►      │            •GCP2   │
     │              •GCP3  │   (afim ou polinomial,       │                •GCP3│
     └───────────────────┘    ajustada aos pares)         └───────────────────┘
     coordenadas de pixel                                 coordenadas reais (UTM)
```
A legenda a reter: cada ponto de controle fornece um par pixel↔coordenada real; a transformação ajustada a partir desses pares é aplicada a toda a imagem, não só aos pontos usados no ajuste.

### GPS e GNSS: como a posição em campo é medida

O **GPS** (*Global Positioning System*) é a constelação de satélites de posicionamento operada pelos Estados Unidos, a primeira a se tornar operacional e de uso civil amplamente disseminado. **GNSS** (*Global Navigation Satellite System*) é o termo genérico que engloba todas as constelações de posicionamento por satélite existentes — GPS (EUA), GLONASS (Rússia), Galileo (União Europeia) e BeiDou (China), entre outras — e um receptor GNSS moderno tipicamente capta sinais de várias constelações simultaneamente, o que aumenta o número de satélites visíveis e melhora a precisão e a confiabilidade do posicionamento, sobretudo em ambientes com obstrução parcial do céu (vegetação densa, terreno montanhoso — situação comum em campanhas de campo geológicas).

O princípio físico do posicionamento por satélite é a **trilateração**: cada satélite transmite continuamente sua posição orbital e um sinal de tempo preciso; o receptor mede o tempo que o sinal leva para chegar (e, a partir da velocidade da luz, a distância ao satélite) e, combinando as distâncias a quatro ou mais satélites simultaneamente visíveis, calcula sua própria posição tridimensional (x, y, z) por trilateração. Vale entender por que **quatro**, e não três: geometricamente, três distâncias já bastariam para fixar um ponto no espaço, mas o relógio do receptor não é atômico como o dos satélites, e seu erro de sincronismo entra na conta como uma quarta incógnita, resolvida simultaneamente com x, y e z — é por isso que as distâncias medidas se chamam, tecnicamente, *pseudodistâncias*. A precisão desse cálculo depende de vários fatores — número e geometria dos satélites visíveis (um parâmetro chamado *DOP*, *dilution of precision*, mede quão favorável é essa geometria), qualidade do relógio do receptor, atraso do sinal ao atravessar a ionosfera e a troposfera, e multi-caminho (o sinal refletindo em superfícies antes de chegar ao receptor, comum em áreas urbanas ou entre paredes de rocha).

Diferentes **modos de posicionamento** entregam precisões muito distintas, e escolher o modo certo para cada etapa de um projeto é uma decisão prática recorrente:

- **Posicionamento autônomo** (um único receptor, sem correção): precisão tipicamente da ordem de poucos metros a alguns metros, suficiente para navegação geral e para localizar aproximadamente um ponto de amostragem, mas insuficiente para muitos levantamentos de precisão.
- **Posicionamento diferencial (DGPS)**: usa um receptor de referência (base) em posição conhecida, que transmite correções a um ou mais receptores móveis (rover), reduzindo os erros comuns entre eles (atmosféricos, de órbita); melhora a precisão para a ordem de submétrica a poucos metros, conforme o método de correção.
- **RTK (*Real-Time Kinematic*)**: técnica diferencial que usa a fase da portadora do sinal (não apenas o código de tempo) e transmite correções em tempo real de uma base para o rover, atingindo precisão da ordem de centímetros — o padrão para levantamento topográfico e geodésico de alta precisão, incluindo muitas aplicações de geologia estrutural de detalhe e cadastro mineral.
- **Pós-processamento**: os dados brutos do receptor são gravados em campo e processados depois, em escritório, sem exigir comunicação em tempo real entre base e rover — útil justamente em áreas remotas, sem sinal de rádio ou celular para transmitir a correção ao vivo. Aqui convivem duas famílias que costumam ser confundidas. No **posicionamento relativo pós-processado** (estático, ou cinemático — PPK, *post-processed kinematic*), os dados do receptor são combinados com os de uma ou mais estações de referência de coordenadas conhecidas — no Brasil, tipicamente as da rede **RBMC** do IBGE —, atingindo precisão comparável à do RTK. No **PPP** (*Precise Point Positioning*, posicionamento por ponto preciso), o receptor é processado **isoladamente**, sem estação de referência: o que entra no lugar dela são órbitas e correções de relógio dos satélites de alta precisão, produzidas por centros de análise internacionais — é assim que funciona o serviço on-line IBGE-PPP. A contrapartida do PPP é um tempo de convergência bem maior até a solução estabilizar. Chamar todo pós-processamento de "PPP" é um erro corrente: PPP é um método específico, não sinônimo de "processado depois".

### Aquisição digital de dados em campo

Coletar dados diretamente em formato digital compatível com o SIG do projeto — em vez de anotar em caderneta de campo e digitar depois — reduz erro de transcrição e acelera a incorporação do dado ao projeto. A prática moderna usa aplicativos de coleta de campo em tablets ou celulares, integrados ao receptor GNSS do próprio dispositivo (ou a um receptor externo de maior precisão conectado por Bluetooth), que registram simultaneamente a posição e os atributos de cada ponto observado — formação geológica, atitude de acamamento, litologia, número de amostra, fotografia associada — dentro de um formulário estruturado previamente desenhado para espelhar exatamente os campos da tabela de atributos que a camada vetorial terá no SIG (Aula 02). Esse alinhamento prévio entre o formulário de campo e o esquema de atributos do SIG é o que torna a importação dos dados coletados, ao final do dia ou da campanha, um processo direto — sem a etapa manual de reformatar ou reconciliar campos.

Um ponto de atenção prático: a **precisão exigida em campo depende da natureza do dado, não é sempre a mesma**. Localizar aproximadamente o ponto de uma amostra de solo dentro de uma área de 100 ha pode ser adequado com posicionamento autônomo; já a medição precisa de uma seção geológica de detalhe, de um contato estrutural crítico ou de um marco de propriedade legal pode exigir RTK ou pós-processamento — decisão que retoma diretamente a discussão de escala e resolução da Aula 01, agora aplicada à precisão do instrumento de campo, não apenas à escala do mapa final.

## Exemplo trabalhado

**Situação:** um geólogo precisa incorporar ao SIG do projeto um mapa geológico histórico, escaneado a partir de uma publicação impressa em escala 1:100.000, sem coordenadas embutidas no arquivo de imagem. Ele identifica 8 pontos de controle bem distribuídos pela imagem — cruzamentos de rios e estradas reconhecíveis também na base cartográfica atual do projeto (SIRGAS2000, UTM 23S) — e realiza o ajuste. O software reporta um RMSE de 45 m. É esse valor aceitável para incorporar o mapa ao projeto?

**Resolução:**

A avaliação depende de comparar o RMSE reportado com o detalhe posicional implícito na escala original do mapa. No Brasil esse critério não é só folclore de prancheta: é normativo. O **Padrão de Exatidão Cartográfica (PEC)**, definido pelo Decreto nº 89.817/1984 (art. 9º), fixa o erro planimétrico admissível — em 90% dos pontos bem definidos testados em campo — em **0,5 mm** na escala da carta para a Classe A, **0,8 mm** para a Classe B e **1,0 mm** para a Classe C, com **erros-padrão** correspondentes de 0,3 mm, 0,5 mm e 0,6 mm, também na escala da carta. É dessa norma que vem a faixa de 0,5 a 1,0 mm usada como referência prática de "erro gráfico" tolerável. Em escala 1:100.000, 1 mm no papel corresponde a 100.000 mm = 100 m no terreno; portanto, 0,5 mm equivalem a 50 m e 1,0 mm a 100 m, enquanto os erros-padrão das três classes equivalem a 30 m, 50 m e 60 m.

O RMSE é a estatística que se compara ao **erro-padrão** da classe, não ao valor do PEC. Os 45 m obtidos correspondem a 0,45 mm na escala do mapa-fonte: acima do erro-padrão da Classe A (30 m), mas confortavelmente dentro do da Classe B (50 m) — o georreferenciamento é aceitável para o uso pretendido (incorporar o traço geológico histórico ao projeto atual em escala regional). O ponto importante deste exemplo é que "45 m de erro" só pôde ser julgado aceitável ou não **em relação à escala original do dado-fonte** — o mesmo RMSE de 45 m seria claramente inaceitável se o mapa-fonte fosse um levantamento de detalhe em escala 1:5.000 (onde 1 mm de erro gráfico corresponde a apenas 5 m no terreno), e o geólogo precisaria buscar mais pontos de controle, mais bem distribuídos, ou aceitar que aquele mapa específico não sustenta análise em escala de detalhe dentro do projeto atual — só em escala regional, compatível com sua origem.

## Erros comuns

- **Julgar um RMSE de georreferenciamento em valor absoluto, sem checar a escala do dado-fonte.** É exatamente o ponto do exemplo trabalhado: 45 m pode ser excelente para um mapa-fonte 1:100.000 e inaceitável para um levantamento 1:5.000 — o número sozinho não diz nada.
- **Concentrar pontos de controle numa única região da imagem.** A transformação ajustada fica instável fora da área coberta pelos pontos; distribuir GCPs até as bordas é o que garante que o ajuste valha para a imagem inteira, não só para o centro.
- **Chamar qualquer pós-processamento de "PPP".** A própria aula sinaliza isso como erro corrente: PPP é um método específico (receptor processado isoladamente, sem estação de referência); posicionamento relativo pós-processado contra a RBMC é outra família, com precisão comparável mas premissa diferente.
- **Usar posicionamento autônomo (poucos metros de precisão) para um contato estrutural crítico ou marco de propriedade legal.** A precisão exigida depende do dado, não é uma escolha de conveniência — decisão que deveria ser tomada antes da campanha, não descoberta como insuficiente depois.

## O que não concluir

- **Que mais satélites visíveis sempre significa posição melhor.** A geometria da constelação (medida pelo DOP) importa tanto quanto o número — muitos satélites agrupados numa mesma região do céu produzem DOP ruim mesmo em quantidade alta.
- **Que RTK ou PPK são sempre superiores a PPP por serem "em tempo real".** PPK e PPP têm precisões comparáveis; a escolha entre eles depende de haver ou não uma estação de referência próxima e de quanto tempo de convergência o projeto tolera, não de qual é tecnicamente "melhor" em abstrato.
- **Que um formulário de campo mal alinhado ao esquema de atributos do SIG é só um detalhe de conveniência.** É o que transforma a importação num processo direto ou numa reconciliação manual de campos — a decisão de desenho do formulário é tomada antes da campanha exatamente por isso.

## Recap relâmpago

- Georreferenciamento atribui coordenadas reais a uma imagem sem coordenadas embutidas, por meio de pontos de controle (GCPs) que relacionam posição de pixel a posição real, ajustando uma transformação matemática aplicada a toda a imagem.
- A qualidade do georreferenciamento é avaliada pelo RMSE dos pontos de controle, e o RMSE aceitável depende da escala/precisão original do dado-fonte, não é um valor fixo universal.
- GPS é uma constelação específica de satélites (EUA); GNSS é o termo genérico para todas as constelações (GPS, GLONASS, Galileo, BeiDou); o posicionamento funciona por trilateração a partir da distância medida a múltiplos satélites — quatro no mínimo, porque o erro do relógio do receptor é uma quarta incógnita resolvida junto com x, y e z.
- Os modos de posicionamento entregam precisões muito diferentes: autônomo (metros), diferencial/DGPS (submétrico a poucos metros), RTK (centimétrico, em tempo real) e pós-processado (centimétrico, sem comunicação em tempo real) — e dentro do pós-processamento convém separar o posicionamento relativo/PPK, que usa estações de referência como a RBMC, do PPP, que processa o receptor isolado com órbitas e relógios precisos.
- A precisão de posicionamento exigida em campo depende da natureza do dado — reconexão aproximada de amostra vs. levantamento estrutural de detalhe — e deve ser decidida antes da campanha, não improvisada.
- Coleta digital de campo com formulário estruturado alinhado ao esquema de atributos do SIG reduz erro de transcrição e agiliza a importação da camada vetorial ao projeto.

## Próxima aula

[[13-geoprocessamento-aula-04-geoprocessamento-vetorial-operacoes-espaciais|Aula 04 — Geoprocessamento vetorial: operações espaciais e cálculos com linhas e polígonos]]

## Fontes

- Hofmann-Wellenhof, B., Lichtenegger, H. & Wasle, E. (2008), *GNSS — Global Navigation Satellite Systems: GPS, GLONASS, Galileo & more*, Springer, cap. 1-5 (princípios de trilateração, DOP, modos de posicionamento).
- IBGE, *Rede Brasileira de Monitoramento Contínuo dos Sistemas GNSS (RBMC)* e *IBGE-PPP — serviço on-line de pós-processamento de dados GNSS* (manual do usuário), documentação técnica de referência para posicionamento relativo pós-processado e para PPP no Brasil.
- Brasil, Decreto nº 89.817, de 20 de junho de 1984, *Instruções Reguladoras das Normas Técnicas da Cartografia Nacional*, art. 8º e 9º (Padrão de Exatidão Cartográfica planimétrico e erros-padrão das Classes A, B e C).
- Longley, P. A. et al. (2015), *Geographic Information Science and Systems*, 4ª ed., Wiley, cap. 4 (georreferenciamento, transformações, precisão).

<!--
nivel: avancado
palavras_corpo: 2260  # recontado apos auditoria + revisao didatica (2026-09-08)
mapa_objetivo_secao:
  geologia-avancado-m13-oa01: "O problema: dados sem coordenadas embutidas" + "Georreferenciamento por pontos de controle" + "GPS e GNSS: como a posição em campo é medida" + "Exemplo trabalhado"
  geologia-avancado-m13-oa02: "Aquisição digital de dados em campo"

# Nota de revisão didática (achado DID-M13-A03-OBJETIVO-001): a secao "GPS e GNSS" estava
# mapeada para o oa02 ("Distinguir as estruturas vetorial e matricial e organizar bases de dados
# espaciais"), objetivo que nao a cobre. Foi remapeada para o oa01, ao qual se liga pelo eixo de
# sistema de referencia e de precisao posicional em funcao da escala, explicitado no proprio
# texto da secao "Aquisicao digital de dados em campo". Fica registrado para o orquestrador que
# o enunciado do oa01 no hub e no course-state.yaml se beneficiaria de citar tambem o metodo de
# posicionamento - ajuste curricular, fora do escopo desta revisao.

alegacoes_auditaveis:
  - claim_id: GEOPROC-M13-A03-GEORREF-001
    claim: "Georreferenciamento por pontos de controle (GCPs) associa pares de coordenadas de pixel (imagem sem coordenadas) e coordenadas reais (sistema de referência do projeto), a partir dos quais é ajustada uma transformação matemática (ex. afim, polinomial) aplicada a toda a imagem; o mínimo matemático para uma transformação afim é três pontos não colineares, mas projetos reais usam mais pontos para avaliar o erro."
    risk: fato
    source: "Longley et al. 2015, Geographic Information Science and Systems, cap. 4"
  - claim_id: GEOPROC-M13-A03-RMSE-002
    claim: "O RMSE (root mean square error) do georreferenciamento é calculado pela diferença entre a posição real de cada ponto de controle e a posição que a transformação ajustada produz para ele, e mede a qualidade do ajuste; a aceitabilidade de um RMSE numérico depende da escala e precisão do dado-fonte, não é um valor fixo universal."
    risk: fato
    source: "Longley et al. 2015, cap. 4; prática cartográfica padrão de avaliação de exatidão"
  - claim_id: GEOPROC-M13-A03-GPSGNSS-003
    claim: "GPS é a constelação de satélites de posicionamento operada pelos Estados Unidos; GNSS é o termo genérico para todas as constelações de posicionamento por satélite (GPS, GLONASS, Galileo, BeiDou, entre outras); um receptor GNSS moderno tipicamente capta sinais de múltiplas constelações simultaneamente."
    risk: fato
    source: "Hofmann-Wellenhof, Lichtenegger & Wasle 2008, GNSS, cap. 1"
  - claim_id: GEOPROC-M13-A03-TRILATERACAO-004
    claim: "O posicionamento por satélite funciona por trilateração: o receptor mede o tempo de chegada do sinal de cada satélite (e a distância correspondente, chamada pseudodistância) e combina as distâncias a quatro ou mais satélites simultaneamente visíveis para calcular sua posição tridimensional. São necessários quatro satélites, e não três, porque o erro do relógio do receptor constitui uma quarta incógnita resolvida simultaneamente com x, y e z."
    risk: fato
    source: "Hofmann-Wellenhof, Lichtenegger & Wasle 2008, GNSS, cap. 5"
    audit_note: "Ampliado na auditoria do Módulo 13 (achado GEOPROC-M13-A03-TRILATERACAO-004, laranja por omissão que gera erro): o texto original citava quatro satélites sem explicar a quarta incógnita, deixando o leitor com a impressão de que três bastariam geometricamente e os demais seriam só redundância."
  - claim_id: GEOPROC-M13-A03-MODOS-005
    claim: "Os modos de posicionamento por satélite têm precisões tipicamente distintas: autônomo (ordem de poucos metros), diferencial/DGPS (submétrico a poucos metros), RTK — usando fase da portadora com correção em tempo real — (ordem de centímetros) e pós-processamento (precisão comparável ao RTK sem necessidade de comunicação em tempo real). Dentro do pós-processamento, o posicionamento relativo pós-processado (estático ou cinemático/PPK) usa estações de referência de coordenadas conhecidas (no Brasil, a RBMC do IBGE), enquanto o PPP (Precise Point Positioning) processa o receptor isoladamente com órbitas e correções de relógio precisas, ao custo de maior tempo de convergência — PPP não é sinônimo de pós-processamento."
    risk: aproximacao
    source: "Hofmann-Wellenhof, Lichtenegger & Wasle 2008, GNSS, cap. 4, 6; IBGE, manual do usuário do serviço IBGE-PPP e documentação da RBMC; ordens de grandeza consolidadas na literatura de geodésia por satélite, valores exatos variam por equipamento e condições"
    audit_note: "Corrigido na auditoria do Módulo 13 (achado GEOPROC-M13-A03-PPP-007, laranja): a versão original rotulava como 'PPP/pós-processado' uma descrição que era, de fato, de posicionamento relativo pós-processado contra a RBMC."
  - claim_id: GEOPROC-M13-A03-ERROGRAFICO-006
    claim: "O Padrão de Exatidão Cartográfica (PEC) planimétrico, definido pelo Decreto nº 89.817/1984 (art. 9º), fixa o erro admissível em 90% dos pontos bem definidos em 0,5 mm na escala da carta (Classe A), 0,8 mm (Classe B) e 1,0 mm (Classe C), com erros-padrão correspondentes de 0,3 mm, 0,5 mm e 0,6 mm na escala da carta; é essa norma que dá origem à faixa de 0,5 a 1,0 mm usada como referência de erro gráfico tolerável, e é ao erro-padrão da classe que se compara um RMSE de georreferenciamento."
    risk: fato
    source: "Brasil, Decreto nº 89.817, de 20/06/1984, art. 8º e 9º (texto oficial, Câmara dos Deputados / Planalto)"
    audit_note: "Ancorado em fonte normativa na auditoria do Módulo 13 (achado GEOPROC-M13-A03-ERROGRAFICO-006, amarelo/sem fonte): a faixa citada era exatamente o PEC, mas o texto a apresentava como convenção informal e afirmava não substituir o PEC formal."
-->
