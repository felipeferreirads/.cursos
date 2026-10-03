# Aula 09: Altimetria — nivelamento geométrico, trigonométrico e barométrico; curvas de nível, áreas e volumes

**ID:** geologia-m20-a09
**Módulo:** [[20-metodos-campo-mapeamento-modulo|Módulo 20 — Métodos de campo e mapeamento geológico]]
**Duração estimada:** ~29 min
**Objetivo:** entender os três métodos de nivelamento topográfico, como eles alimentam a construção de curvas de nível, e como calcular área e volume a partir de dados de campo.
**Pré-requisito:** [[20-metodos-campo-mapeamento-aula-08-planimetria-azimutes-poligonais|Aula 08 — Planimetria: azimutes, rumos, coordenadas e o fechamento de poligonais com estação total]]

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **Nivelamento** | Conjunto de métodos para determinar a diferença de altitude (desnível) entre dois ou mais pontos. |
| **Desnível** | A diferença de altitude entre dois pontos. |
| **RN (referência de nível)** | Ponto de altitude conhecida e materializada em campo (marco), usado como origem para transportar altitude a outros pontos. |
| **Nível e mira** | Instrumento (nível) que gera uma linha de visada perfeitamente horizontal, e régua graduada (mira) lida através dele para obter o desnível. |
| **Curva de nível** | Linha que une, num mapa, todos os pontos de mesma altitude. |
| **Equidistância** | A diferença de altitude constante entre curvas de nível sucessivas num mesmo mapa. |
| **Cálculo de área por coordenadas** | Método que obtém a área de um polígono diretamente das coordenadas (x, y) de seus vértices, sem desenhar nem medir com régua. |
| **Volume por seções (método das áreas médias)** | Método que estima um volume multiplicando a área média de seções transversais sucessivas pela distância entre elas. |

## Antes de começar, você precisa saber

- Como uma poligonal topográfica é calculada em coordenadas e como se verifica seu fechamento — [[20-metodos-campo-mapeamento-aula-08-planimetria-azimutes-poligonais|Aula 08]].
- Como uma seção geológica usa o perfil topográfico como base do desenho — [[20-metodos-campo-mapeamento-aula-04-secao-geologica|Aula 04]].

## Ao final você vai conseguir

- [geologia-m20-oa09] Executar e interpretar nivelamento geométrico, trigonométrico e barométrico e derivar curvas de nível, áreas e volumes.

## Conteúdo

### A terceira dimensão do levantamento

As Aulas 07 e 08 resolveram a planimetria — a posição horizontal dos pontos de um levantamento. Falta a **altimetria**: a altitude de cada ponto, ou, mais especificamente, o **desnível** entre pontos, que permite depois desenhar curvas de nível, calcular área real de uma superfície inclinada e estimar volumes de terra movimentada ou de um corpo mineralizado. O processo de determinar desnível se chama **nivelamento**, e existem três métodos principais, de precisão decrescente e custo também decrescente.

### Nivelamento geométrico: o mais preciso

O **nivelamento geométrico** usa um instrumento chamado **nível**, que gera uma linha de visada perfeitamente horizontal (garantida por uma bolha de nível ou por compensador automático), e uma **mira** — régua graduada vertical, apoiada sobre o ponto de interesse. O operador, olhando pelo nível a partir de um ponto intermediário, lê a altura em que a linha horizontal de visada intercepta a mira, primeiro apoiada num ponto de altitude conhecida (a **RN**, referência de nível), depois num ponto de altitude a determinar. A diferença entre as duas leituras de mira é exatamente o desnível entre os dois pontos, porque a linha de visada é horizontal por construção — não é preciso nenhuma outra medida. É o método mais preciso dos três (erro tipicamente milimétrico a poucos centímetros por quilômetro nivelado, dependendo da classe do nivelamento), usado quando a precisão vertical importa muito, como implantação de obra ou levantamento cadastral de precisão — ao custo de ser o mais lento, porque exige visadas curtas e um ponto de apoio intermediário a cada poucos metros ou dezenas de metros.

### Nivelamento trigonométrico: mais rápido, um pouco menos preciso

O **nivelamento trigonométrico** obtém o desnível a partir do ângulo vertical (medido com uma estação total ou teodolito, Aula 07) e da distância até o ponto visado, usando trigonometria simples: o desnível é aproximadamente a distância multiplicada pela tangente do ângulo vertical (ou seno/cosseno, dependendo de como o ângulo é referenciado — a partir da horizontal ou do zênite). A vantagem é a velocidade: uma estação total mede, num único disparo, distância, ângulo horizontal e ângulo vertical, entregando ao mesmo tempo posição planimétrica e desnível, sem exigir os pontos de apoio intermediários do nivelamento geométrico. A desvantagem é que qualquer pequeno erro no ângulo vertical medido se propaga, ampliado pela distância, no desnível calculado — por isso o nivelamento trigonométrico é menos preciso que o geométrico em distâncias longas, embora seja o método padrão quando a estação total já está em uso para levantar a planimetria de qualquer forma.

### Nivelamento barométrico: o mais rápido, o menos preciso

O **nivelamento barométrico** usa a variação da pressão atmosférica com a altitude — quanto mais alto, menor a pressão do ar — medida por um barômetro (hoje, frequentemente embutido em GPS de mão e smartphones). É rápido e não exige visada entre pontos, o que o torna útil em terreno de vegetação densa ou relevo que dificulta a visada direta de outros métodos. Mas sua precisão é a mais baixa das três (tipicamente da ordem de metros, porque a pressão também varia com o clima e a hora do dia, não só com a altitude), e por isso serve para reconhecimento expedito ou apoio a observações de campo — nunca para levantamento de precisão ou base de projeto de engenharia.

### De pontos com altitude a curvas de nível

Uma vez que um conjunto de pontos tem altitude conhecida (por qualquer um dos três métodos), essas altitudes são interpoladas para desenhar **curvas de nível** — linhas que unem todos os pontos de mesma altitude num mapa. A diferença de altitude constante entre curvas sucessivas é a **equidistância** do mapa (por exemplo, curvas de 10 em 10 m); quanto menor a equidistância, mais detalhe o mapa mostra, ao custo de mais pontos nivelados para sustentar essa resolução. Curvas de nível próximas entre si indicam relevo íngreme; curvas espaçadas indicam relevo suave — é essa mesma leitura de relevo, aliás, que sustenta o perfil topográfico usado na construção de uma seção geológica (Aula 04) e a interpretação da regra dos V num mapa geológico (Aula 03).

### Área por coordenadas: sem régua, sem transferidor

Uma vez que os vértices de um polígono (uma poligonal fechada, ou o contorno de uma área de interesse) têm coordenadas (x, y) conhecidas — vindas do cálculo planimétrico da Aula 08 —, a área do polígono pode ser calculada diretamente por uma fórmula algébrica, sem desenhar nem medir nada fisicamente: a **fórmula de Gauss** (também chamada de fórmula do "cadarço" ou *shoelace*), que soma produtos cruzados das coordenadas de vértices sucessivos. O resultado é exato (dentro da precisão das coordenadas de entrada), muito mais confiável do que estimar área por planimetria gráfica sobre um mapa impresso.

### Volume: de seções transversais a metros cúbicos

Para estimar um volume — de terra a mover num corte de estrada, de um corpo mineralizado delimitado por seções, de um reservatório — o método mais comum em topografia é o **método das áreas médias** (ou método das seções): calcula-se a área de cada seção transversal (perpendicular ao eixo do corpo, usando o mesmo princípio de área por coordenadas), toma-se a média das áreas de duas seções sucessivas, e multiplica-se essa área média pela distância entre as duas seções — repetindo e somando para todo o comprimento do corpo. É uma aproximação (assume que o volume entre duas seções se comporta como um prisma de área média constante), mas suficientemente precisa quando as seções são bem espaçadas em relação à variação da forma real — para formas que variam de modo mais complexo entre seções, existe a fórmula prismoidal, uma correção mais refinada sobre o mesmo princípio.

## Exemplo trabalhado

Uma equipe precisa da área de um terreno triangular cujos vértices, já calculados por planimetria (Aula 08), têm coordenadas (em metros): A(0, 0), B(120, 0), C(60, 80). Pela fórmula de Gauss para um polígono de três vértices:

Área = ½ |x_A(y_B − y_C) + x_B(y_C − y_A) + x_C(y_A − y_B)|
Área = ½ |0×(0 − 80) + 120×(80 − 0) + 60×(0 − 0)|
Área = ½ |0 + 9.600 + 0| = 4.800 m²

Para o volume, a mesma equipe mede duas seções transversais de um talude a escavar, separadas por 20 m de distância ao longo do eixo: a primeira seção tem área de 15 m², a segunda tem área de 25 m². Pelo método das áreas médias: volume = [(15 + 25) / 2] × 20 = 20 × 20 = 400 m³ de material entre as duas seções.

## Recap relâmpago

- Nivelamento geométrico (nível + mira) é o mais preciso dos três métodos, mas o mais lento, por exigir pontos de apoio intermediários e visadas curtas.
- Nivelamento trigonométrico usa ângulo vertical e distância (estação total) — mais rápido, um pouco menos preciso, e o padrão quando a planimetria já está sendo levantada com o mesmo instrumento.
- Nivelamento barométrico usa variação de pressão atmosférica com altitude — o mais rápido e menos preciso dos três, útil só para reconhecimento expedito.
- Curvas de nível unem pontos de mesma altitude; a equidistância é a diferença de altitude constante entre curvas sucessivas; curvas próximas indicam relevo íngreme.
- A fórmula de Gauss calcula área de um polígono diretamente das coordenadas de seus vértices, sem desenho nem régua.
- O método das áreas médias estima volume multiplicando a área média de duas seções sucessivas pela distância entre elas.

## Próxima aula

[[20-metodos-campo-mapeamento-aula-10-sirgas2000-utm-gnss-geodesico|Aula 10 — Sistema geodésico brasileiro, projeção UTM e posicionamento GNSS geodésico no mapeamento]] encerra o módulo situando essas coordenadas planimétricas e altimétricas dentro do referencial geodésico oficial do Brasil e da projeção cartográfica usada em todo mapa geológico.

## Fontes

- Literatura técnica de topografia sobre métodos de nivelamento (geométrico, trigonométrico, barométrico), cálculo de área por coordenadas (fórmula de Gauss) e volume por método das áreas médias, consultada em 2026-08-29.

<!--
nivel: ensino-medio-sem-geologia-v1
palavras_corpo: ~1400
mapa_objetivo_secao:
  geologia-m20-oa09: "A terceira dimensão do levantamento" + "Nivelamento geométrico" + "Nivelamento trigonométrico" + "Nivelamento barométrico" + "De pontos com altitude a curvas de nível" + "Área por coordenadas" + "Volume: de seções transversais a metros cúbicos" + "Exemplo trabalhado"
alegacoes_auditaveis:
  - claim_id: GEO-M20-A09-PRECISAO-METODOS-NIVELAMENTO-001
    claim: "Nivelamento geométrico é o mais preciso (ordem de mm a poucos cm/km), trigonométrico intermediário, barométrico o menos preciso (ordem de metros), nessa ordem relativa de precisão."
    risk: numerico
    source: "consenso de literatura técnica de topografia; valores de precisão expressos em ordem de grandeza relativa, não como tolerância normativa fechada"
  - claim_id: GEO-M20-A09-EXEMPLO-NUMERICO-002
    claim: "Valores numéricos do exemplo trabalhado (área por Gauss, volume por áreas médias) foram calculados diretamente pelas fórmulas descritas no texto, não extraídos de fonte externa."
    risk: numerico
    source: "cálculo interno consistente (fórmula de Gauss e método das áreas médias aplicados aos valores dados)"
-->
