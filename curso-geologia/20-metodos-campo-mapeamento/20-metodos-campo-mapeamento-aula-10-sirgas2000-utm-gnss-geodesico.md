# Aula 10: Sistema geodésico brasileiro, projeção UTM e posicionamento GNSS geodésico no mapeamento

**ID:** geologia-m20-a10
**Módulo:** [[20-metodos-campo-mapeamento-modulo|Módulo 20 — Métodos de campo e mapeamento geológico]]
**Duração estimada:** ~28 min
**Objetivo:** entender o referencial geodésico oficial do Brasil (SIRGAS2000), como a projeção UTM converte a superfície curva da Terra num plano de coordenadas, e como escolher o método de posicionamento GNSS conforme a precisão exigida.
**Pré-requisito:** [[20-metodos-campo-mapeamento-aula-09-nivelamento-curvas-de-nivel-areas-volumes|Aula 09 — Altimetria: nivelamento geométrico, trigonométrico e barométrico; curvas de nível, áreas e volumes]]

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **Datum geodésico** | Conjunto de parâmetros (elipsoide de referência + ponto de amarração) que define como as coordenadas geográficas de um local se relacionam com a forma real da Terra. |
| **Elipsoide de referência** | Modelo matemático simplificado da forma da Terra (um elipsoide de revolução), usado como superfície de cálculo para coordenadas geográficas. |
| **SIRGAS2000** | Datum geodésico oficial do Brasil desde 2005, baseado no elipsoide GRS80, com época de referência 2000.4. |
| **Projeção UTM** | Sistema de projeção cartográfica que divide a Terra em 60 fusos de 6° de longitude cada, representando cada fuso num plano de coordenadas métricas. |
| **Fuso** | Cada uma das 60 faixas de 6° de longitude em que a projeção UTM divide a Terra. |
| **Fator de escala** | A razão entre a distância medida na projeção e a distância real no elipsoide — na UTM, 0,9996 no meridiano central do fuso. |
| **GNSS** | Sistema Global de Navegação por Satélite — termo genérico para qualquer constelação de satélites de posicionamento (GPS americano, GLONASS russo, Galileo europeu, BeiDou chinês, entre outros). |
| **Posicionamento relativo (diferencial)** | Técnica de GNSS que usa dois ou mais receptores simultaneamente (um fixo, de coordenada conhecida) para cancelar boa parte do erro comum aos dois, aumentando muito a precisão. |
| **RTK (Real-Time Kinematic)** | Técnica de posicionamento GNSS relativo em tempo real, capaz de precisão centimétrica no próprio instante da medida em campo. |

## Antes de começar, você precisa saber

- Como distância, ângulo, poligonal e altitude são medidos e calculados com instrumentos topográficos — [[20-metodos-campo-mapeamento-aula-07-teoria-dos-erros-topografia-nbr13133|Aula 07]], [[20-metodos-campo-mapeamento-aula-08-planimetria-azimutes-poligonais|Aula 08]] e [[20-metodos-campo-mapeamento-aula-09-nivelamento-curvas-de-nivel-areas-volumes|Aula 09]].
- Como o GPS de uso geral calcula posição por triangulação de sinais de satélite — [[20-metodos-campo-mapeamento-aula-06-sensoriamento-remoto-gps-sig|Aula 06]].

## Ao final você vai conseguir

- [geologia-m20-oa10] Converter coordenadas entre o sistema geodésico brasileiro (SIRGAS2000) e a projeção UTM e escolher o método de posicionamento GNSS adequado à precisão exigida.

## Conteúdo

### Por que toda coordenada precisa de um referencial declarado

Uma coordenada geográfica (latitude, longitude) ou uma coordenada UTM (metros norte, metros leste) só faz sentido se vier acompanhada do **datum** ao qual está referida — porque o mesmo ponto físico no terreno pode ter coordenadas ligeiramente diferentes, dependendo de qual elipsoide e qual amarração serviram de base ao cálculo. Ignorar o datum é uma fonte silenciosa de erro: dois mapas do mesmo local, um em SAD69 (o datum brasileiro anterior) e outro em SIRGAS2000, podem mostrar o mesmo ponto deslocado por dezenas de metros — um erro pequeno para reconhecimento regional, mas inaceitável para qualquer levantamento de precisão ou para integrar dados de fontes diferentes num mesmo SIG (Aula 06).

### SIRGAS2000: o referencial oficial do Brasil

O **SIRGAS2000** é o datum geodésico oficial do Sistema Geodésico Brasileiro desde 2005, adotado pelo IBGE em substituição ao antigo SAD69. Ele usa como superfície de referência o **elipsoide GRS80** (Geodetic Reference System 1980), amarrado a uma rede de estações geodésicas continentais medidas por GNSS, com **época de referência 2000.4** — ou seja, as coordenadas da rede correspondem à posição da crosta terrestre naquele instante de referência (2000,4 do calendário), o que importa porque a crosta se desloca lentamente com o tempo geológico e tectônico, e uma coordenada de precisão altíssima, décadas depois, tecnicamente já carrega uma pequena diferença em relação à época de referência original. Para a grande maioria dos usos em geologia de campo, essa diferença é desprezível; ela só se torna relevante em geodésia de altíssima precisão (monitoramento de deformação crustal, por exemplo). O elipsoide GRS80 do SIRGAS2000 é, na prática, equivalente ao WGS84 usado pelo GPS americano — o que faz da conversão entre um GPS de mão (que trabalha nativamente em WGS84) e o SIRGAS2000 brasileiro, para a maioria dos usos práticos, uma diferença desprezível, embora tecnicamente sejam datums distintos.

### Projeção UTM: transformar uma superfície curva num plano

Coordenadas geográficas (latitude e longitude) descrevem posição na superfície curva do elipsoide, mas mapas, estações totais e a maior parte do trabalho topográfico e de mapeamento usam coordenadas **planas**, em metros — mais fáceis de calcular distância e área (bastando geometria plana, como nas Aulas 08 e 09) do que trigonometria esférica. A **projeção UTM** (Universal Transversa de Mercator) resolve isso dividindo a Terra em **60 fusos** de 6° de longitude cada, e projetando cada fuso separadamente sobre um cilindro transverso tangente (ou secante) ao elipsoide, gerando coordenadas planas em metros dentro de cada fuso — norte (N) e leste (E), sempre positivas, com origem deslocada para evitar coordenadas negativas.

Como qualquer projeção de uma superfície curva num plano, a UTM introduz distorção — que a projeção controla, minimiza e distribui de forma previsível dentro do fuso: no **meridiano central** de cada fuso, o **fator de escala** é 0,9996 (a distância na projeção é ligeiramente menor que a distância real no elipsoide), enquanto nas bordas do fuso, a 3° do meridiano central, o fator de escala cresce para pouco mais de 1 (a distância na projeção fica ligeiramente maior que a real). Essa distorção controlada é o preço de trabalhar em coordenadas planas simples: para a maioria dos usos de mapeamento geológico, a diferença entre distância projetada e distância real dentro de um mesmo fuso é pequena o bastante para ser ignorada; só se torna relevante em levantamentos de precisão que exijam reduzir distâncias medidas em campo à distância no elipsoide (ou vice-versa).

O território brasileiro, por sua extensão em longitude, é coberto por vários fusos UTM (aproximadamente do fuso 18 ao fuso 25 sul, variando conforme a região do país) — por isso todo levantamento em coordenadas UTM precisa declarar não só o datum (SIRGAS2000), mas também o número do fuso e o hemisfério (norte ou sul), sem os quais a mesma coordenada numérica poderia corresponder a pontos completamente diferentes do planeta.

### GNSS geodésico: escolhendo a precisão certa para a tarefa

A Aula 06 já apresentou o GPS de uso geral, com precisão de poucos metros — suficiente para localizar um afloramento numa caderneta de campo, mas insuficiente para muitos levantamentos topográficos de precisão. **GNSS** é o termo mais amplo (Global Navigation Satellite System), que engloba o GPS americano e outras constelações (GLONASS, Galileo, BeiDou), e o posicionamento geodésico de maior precisão usa métodos que vão muito além do receptor único de um GPS de mão:

O **posicionamento absoluto (ponto simples)** — usado pelo GPS comum de smartphone ou GPS de mão — calcula a posição de um único receptor isoladamente, com precisão da ordem de metros, porque erros comuns a todo o sistema (atraso do sinal na atmosfera, imprecisão da órbita do satélite) afetam a medida sem correção.

O **posicionamento relativo (diferencial)** usa dois receptores simultaneamente — um fixo, sobre um ponto de coordenada já muito bem conhecida (uma base), e outro móvel, no ponto de interesse — e explora o fato de que boa parte do erro (atraso atmosférico, erro de órbita) afeta os dois receptores de forma quase idêntica, se estiverem próximos o bastante; subtraindo esse erro comum, a precisão relativa entre os dois pontos sobe para a ordem de centímetros a decímetros, dependendo do método e do tempo de observação.

O **RTK (Real-Time Kinematic)** é a forma mais ágil de posicionamento relativo: a base transmite correções ao receptor móvel em tempo real (por rádio ou internet), permitindo obter coordenada de precisão centimétrica no próprio instante da medida em campo, sem pós-processamento posterior — é o método de escolha quando um levantamento topográfico de precisão (implantação de poligonal, malha de sondagem, controle de obra) precisa de posição geodésica rápida e confiável diretamente em campo.

A escolha entre esses métodos, na prática, é sempre uma troca entre precisão exigida, tempo disponível e custo do equipamento: reconhecimento geológico regional não justifica RTK; implantação de furos de sondagem de uma campanha de exploração mineral, ou controle topográfico de uma obra, dificilmente aceita menos que RTK ou pós-processamento equivalente.

## Exemplo trabalhado

Uma equipe de mapeamento em Salvador (BA), aproximadamente na longitude 38°30'W, precisa saber em que fuso UTM lançar suas coordenadas. Os fusos UTM têm 6° de largura, numerados a partir do antimeridiano (180°W); a fórmula geral, válida nos dois hemisférios, é: número do fuso = parte inteira de (longitude + 180°)/6, mais 1 — com a longitude **negativa** a oeste. Para 38°30'W: (−38,5 + 180)/6 = 23,58; parte inteira 23; mais 1 = **fuso 24**. Na prática de campo, porém, mais simples que a fórmula é lembrar que o fuso 24S cobre de 42°W a 36°W, faixa que contém 38°30'W. Logo, a equipe lança suas coordenadas como UTM, fuso 24S, datum SIRGAS2000 — e declara essas três informações (fuso, hemisfério, datum) em todo arquivo e mapa gerado, exatamente porque a mesma coordenada numérica sem essa declaração seria ambígua.

Para a precisão exigida, a equipe compara dois cenários: localizar um afloramento observado a pé, para amarrar num SIG regional — nesse caso, um GPS de posicionamento absoluto (poucos metros de erro) é mais que suficiente, dado que a incerteza da própria delimitação visual do afloramento já é da mesma ordem. Já para implantar, com exatidão, os pontos de coleta de uma malha de sondagem geoquímica que será revisitada por várias equipes ao longo de meses, a equipe opta por RTK, cuja precisão centimétrica garante que todas as equipes, em datas diferentes, encontrem exatamente o mesmo ponto físico — algo que um GPS de posicionamento absoluto, com seu erro de metros, não garantiria de forma confiável.

## Recap relâmpago

- Toda coordenada precisa vir acompanhada do datum ao qual está referida — o mesmo ponto físico tem coordenadas diferentes em datums diferentes (ex.: SAD69 vs. SIRGAS2000).
- SIRGAS2000 é o datum oficial do Brasil desde 2005, baseado no elipsoide GRS80, com época de referência 2000.4, e praticamente equivalente ao WGS84 do GPS para a maioria dos usos práticos.
- A projeção UTM divide a Terra em 60 fusos de 6° de longitude, com fator de escala 0,9996 no meridiano central de cada fuso — o Brasil é coberto por vários fusos, que devem sempre ser declarados junto com a coordenada.
- Posicionamento absoluto (receptor único) tem precisão de metros; posicionamento relativo/diferencial (dois receptores) sobe para centímetros a decímetros; RTK entrega centímetros em tempo real, direto em campo.
- A escolha do método GNSS depende da precisão exigida pela tarefa — reconhecimento regional não justifica RTK, mas implantação de malha de sondagem ou controle de obra normalmente exige.

## Fontes

- IBGE, Resolução do Sistema Geodésico Brasileiro sobre adoção do SIRGAS2000 (2005) — elipsoide GRS80, época de referência 2000.4, consultado em 2026-08-29.
- Literatura técnica sobre projeção UTM (fusos de 6°, fator de escala 0,9996 no meridiano central) e métodos de posicionamento GNSS (absoluto, relativo/diferencial, RTK), consultada em 2026-08-29.

<!--
nivel: ensino-medio-sem-geologia-v1
palavras_corpo: ~1450
mapa_objetivo_secao:
  geologia-m20-oa10: "Por que toda coordenada precisa de um referencial declarado" + "SIRGAS2000" + "Projeção UTM" + "GNSS geodésico: escolhendo a precisão certa para a tarefa" + "Exemplo trabalhado"
alegacoes_auditaveis:
  - claim_id: GEO-M20-A10-SIRGAS2000-PARAMETROS-001
    claim: "SIRGAS2000 é o datum geodésico oficial do Brasil desde 2005, baseado no elipsoide GRS80, com época de referência 2000.4."
    risk: factual
    source: "IBGE, resolução de adoção do SIRGAS2000; busca web em 2026-08-29"
  - claim_id: GEO-M20-A10-UTM-FUSOS-002
    claim: "A projeção UTM divide a Terra em 60 fusos de 6° de longitude, com fator de escala 0,9996 no meridiano central de cada fuso."
    risk: numerico
    source: "busca web em 2026-08-29 sobre parâmetros padrão da projeção UTM"
  - claim_id: GEO-M20-A10-FUSO-SALVADOR-003
    claim: "O fuso UTM 24S cobre a faixa de longitude aproximada de 42°W a 36°W, contendo Salvador (BA), próxima de 38°30'W."
    risk: numerico
    source: "cálculo por numeração padrão de fusos UTM a partir do antimeridiano; conferir com carta de fusos oficial antes de uso em levantamento real"
  - claim_id: GEO-M20-A10-PRECISAO-GNSS-004
    claim: "Posicionamento absoluto GNSS tem precisão da ordem de metros; posicionamento relativo/diferencial, ordem de centímetros a decímetros; RTK, ordem de centímetros em tempo real."
    risk: numerico
    source: "consenso de literatura técnica de geodésia/GNSS; valores em ordem de grandeza relativa, não como especificação de fabricante específico"
-->
