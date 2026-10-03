# Aula 07: Medida de distâncias e de ângulos e a teoria dos erros na topografia (NBR 13133)

**ID:** geologia-m20-a07
**Módulo:** [[20-metodos-campo-mapeamento-modulo|Módulo 20 — Métodos de campo e mapeamento geológico]]
**Duração estimada:** ~28 min
**Objetivo:** entender como distâncias e ângulos são medidos em topografia, que tipos de erro afetam toda medida, e como a NBR 13133 fixa a precisão exigida de um levantamento topográfico de apoio ao mapeamento geológico.
**Pré-requisito:** [[20-metodos-campo-mapeamento-aula-02-bussola-de-geologo-atitudes|Aula 02 — Medindo atitudes com a bússola de geólogo]]

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **Erro grosseiro** | Engano evidente, causado por falha do operador ou do equipamento (leitura trocada, anotação errada) — detectável e eliminável, nunca "aceito" numa medida. |
| **Erro sistemático** | Erro que se repete sempre no mesmo sentido e com a mesma causa (ex.: trena esticada além do comprimento nominal) — pode ser modelado e corrigido, se a causa for conhecida. |
| **Erro acidental (aleatório)** | Pequena variação inevitável, de causa não controlável, que muda de sinal e magnitude a cada medida — só pode ser tratado estatisticamente, nunca eliminado por completo. |
| **Precisão** | O grau de concordância entre medidas repetidas do mesmo valor (medidas próximas entre si, mesmo que erradas). |
| **Acurácia (exatidão)** | O grau de proximidade entre a medida e o valor verdadeiro. |
| **Tolerância** | O erro máximo aceitável, definido por norma, para que um levantamento seja considerado válido para o uso a que se destina. |
| **NBR 13133** | Norma brasileira que define os critérios de aceitação e as tolerâncias para execução de levantamentos topográficos. Edição vigente: ABNT NBR 13133:2021. |
| **Estação total** | Instrumento topográfico que combina teodolito eletrônico (mede ângulos) e distanciômetro eletrônico (mede distâncias) num único aparelho. |

## Antes de começar, você precisa saber

- Como a bússola de geólogo mede um ângulo (direção e mergulho) e por que a declinação magnética precisa ser corrigida — [[20-metodos-campo-mapeamento-aula-02-bussola-de-geologo-atitudes|Aula 02]].
- Como um mapa geológico representa a superfície mapeada — [[20-metodos-campo-mapeamento-aula-03-mapa-geologico-regra-dos-v|Aula 03]].

## Ao final você vai conseguir

- [geologia-m20-oa07] Aplicar a teoria dos erros à medição topográfica de distâncias e de ângulos e avaliar a precisão exigida pela NBR 13133.

## Conteúdo

### Por que um mapeamento geológico precisa de topografia instrumental

As aulas anteriores deste módulo trataram de observar, medir atitude e desenhar a geologia com os instrumentos clássicos de campo — bússola, caderneta, GPS de mão. Isso é suficiente para boa parte do trabalho geológico. Mas alguns produtos exigem mais precisão do que um GPS de smartphone ou uma bússola entregam: a implantação de uma malha de sondagem, o levantamento planialtimétrico de uma área de mina, a locação exata de um perfil geofísico, ou qualquer levantamento que vá para um projeto de engenharia. Nesses casos, entra a **topografia instrumental** — o conjunto de métodos e instrumentos (estação total, nível, GNSS geodésico) que medem distância, ângulo e desnível com precisão centimétrica ou melhor, seguindo normas técnicas formais. Esta aula abre essa camada de precisão com a base de tudo: como se mede, que erros existem e o que a norma brasileira exige.

### Como se mede distância e ângulo, na prática

Distâncias em topografia são medidas por três meios principais, em ordem crescente de precisão e custo: **trena de aço**, usada em pequenos comprimentos com correção de temperatura e tensão aplicada; **distanciômetro eletrônico (EDM)**, que mede distância pelo tempo de ida e volta de um feixe de luz (infravermelho ou laser) refletido num prisma; e o **GNSS geodésico** (que a Aula 10 detalha), que deriva distância e posição de sinais de satélite. Hoje, a maior parte da topografia de precisão usa a **estação total** — um instrumento que combina um teodolito eletrônico (mede ângulos horizontais e verticais com precisão de segundos de arco) e um distanciômetro eletrônico no mesmo corpo, permitindo medir, num único ponto de estação, a distância e os dois ângulos até qualquer ponto visado, e calcular automaticamente as coordenadas relativas desse ponto.

Ângulos são medidos como **ângulo horizontal** (entre duas direções vistas do mesmo ponto, no plano horizontal) e **ângulo vertical** (ou zenital, entre a direção visada e a vertical do local) — juntos, eles definem a direção do ponto visado no espaço, exatamente como direção e mergulho definem a atitude de uma camada na Aula 02, só que agora medidos por um instrumento óptico-eletrônico em vez de uma bússola manual.

### Toda medida tem erro: os três tipos

Nenhuma medida física é exata — a pergunta relevante nunca é "essa medida tem erro?", mas "que tipo de erro tem, e ele é aceitável?". A topografia clássica divide o erro em três categorias, cada uma com tratamento diferente:

**Erro grosseiro** é um engano puro e simples — o operador leu "132" em vez de "123", ou anotou o ponto errado. Não é um "erro de medição" no sentido técnico: é uma falha que deve ser detectada (por conferência, repetição da medida, ou verificação de consistência) e eliminada, nunca aceita como parte do resultado.

**Erro sistemático** tem uma causa identificável e se repete sempre no mesmo sentido: uma trena de aço que dilatou com o calor do dia mede tudo um pouco "curto" em relação ao nominal; um distanciômetro descalibrado adiciona sempre a mesma constante à distância real; uma mira de nível mal aprumada desloca toda leitura na mesma direção. Como a causa é conhecível, o erro sistemático pode — e deve — ser modelado e corrigido (por exemplo, aplicando uma correção de temperatura à distância medida com trena), em vez de simplesmente tolerado.

**Erro acidental (ou aleatório)** é o que sobra depois de eliminados os erros grosseiros e corrigidos os sistemáticos: pequenas variações de causa não controlável — vibração do ar que muda ligeiramente a leitura óptica, imprecisão humana em centrar exatamente a mira, arredondamento do próprio instrumento. Esse erro muda de sinal e magnitude a cada medida repetida, de forma imprevisível ponto a ponto, mas com um comportamento estatístico regular quando muitas medidas são comparadas — é sobre ele que a estatística de erros (desvio padrão, tolerância) se aplica, porque ele nunca é eliminado por completo, só reduzido e limitado a uma faixa aceitável.

### Precisão não é o mesmo que acurácia

Uma distinção que vale fixar: **precisão** é o quanto medidas repetidas concordam entre si (medidas agrupadas, mesmo que deslocadas do valor real por um erro sistemático não corrigido); **acurácia** (ou exatidão) é o quanto a medida está de fato próxima do valor verdadeiro. É possível ter alta precisão e baixa acurácia — por exemplo, um distanciômetro descalibrado que sempre erra por +5 cm entrega medidas muito consistentes entre si (alta precisão), mas todas erradas na mesma direção (baixa acurácia), até que a calibração seja corrigida.

### O que a NBR 13133 exige

A **ABNT NBR 13133:2021** — a edição vigente — é a norma brasileira que rege a execução de levantamentos topográficos, definindo os **critérios de aceitação** de um levantamento conforme a sua finalidade: o que precisa ser verificado, e dentro de que tolerância, para que o serviço seja aceito como válido. Para as poligonais planimétricas, essa edição **simplificou o esquema de classes** das versões anteriores (que distribuíam as poligonais em várias classes, cada uma com sua própria exigência) e adota como referência uma **precisão relativa mínima de 1:12.000** — a relação entre o erro linear de fechamento tolerado e o perímetro total percorrido, ou seja, o erro de fechamento não deve superar 1 parte em 12.000 do perímetro da poligonal. Em casos especiais, a norma admite tolerância diferente, estabelecida em comum acordo entre contratante e contratado. A essa exigência linear soma-se uma **tolerância angular**, calculada por uma fórmula que cresce com a raiz do número de estações da poligonal, refletindo que o erro acidental se acumula a cada ângulo medido ao longo do percurso.

Na prática, isso significa que a norma não pede "zero erro" (impossível), mas define, para cada finalidade de levantamento, o quanto de erro acidental acumulado é tolerável antes que o levantamento tenha que ser refeito ou ajustado — e é essa tolerância que orienta a escolha do instrumento e do método (uma poligonal de reconhecimento geológico regional tolera erro maior que a poligonal de implantação de uma barragem).

## Exemplo trabalhado

Uma equipe mede a mesma distância entre dois marcos, com a mesma trena de aço, cinco vezes seguidas, obtendo: 48,32 m; 48,35 m; 48,31 m; 48,34 m; 48,33 m. As cinco leituras estão bem próximas entre si — a dispersão é pequena, um sinal de boa **precisão** do processo de medida (a variação entre 48,31 e 48,35 m é da ordem do erro acidental esperado para trena de aço nesse comprimento). Depois, a equipe percebe que a trena usada estava com um trecho inicial dobrado e mal esticado, o que fazia com que toda medida saísse cerca de 4 cm mais curta que o real — um **erro sistemático**, com causa identificada e sentido único (sempre "curto"). Corrigindo essa constante em todas as cinco leituras, a distância corrigida sobe para aproximadamente 48,37 m, valor mais próximo do real — ou seja: a medida original era precisa (leituras concordantes entre si), mas não era acurada (deslocada do valor verdadeiro pelo erro sistemático), até a correção ser aplicada. Se, numa sexta leitura, alguém tivesse anotado "483,3 m" por engano de posição decimal, isso seria um **erro grosseiro** — descartável de imediato, não incorporável a nenhuma média.

## Recap relâmpago

- Topografia instrumental (estação total, nível, GNSS geodésico) entra quando o mapeamento geológico exige precisão centimétrica, além do que bússola e GPS de mão entregam.
- A estação total combina teodolito eletrônico (ângulos horizontal e vertical) e distanciômetro eletrônico (distância) no mesmo instrumento.
- Erro grosseiro é engano detectável e eliminável; erro sistemático tem causa conhecida, sentido único, e pode ser corrigido; erro acidental é a variação residual inevitável, tratada estatisticamente.
- Precisão (concordância entre medidas repetidas) não é o mesmo que acurácia (proximidade do valor verdadeiro) — dá para ter uma sem a outra.
- A NBR 13133 (edição vigente: 2021) define os critérios de aceitação e as tolerâncias de levantamentos topográficos: para poligonais planimétricas, uma precisão relativa mínima de referência de 1:12.000 (razão entre erro de fechamento e perímetro) e uma tolerância angular que cresce com a raiz do número de estações.

## Próxima aula

[[20-metodos-campo-mapeamento-aula-08-planimetria-azimutes-poligonais|Aula 08 — Planimetria: azimutes, rumos, coordenadas e o fechamento de poligonais com estação total]] usa exatamente os ângulos e distâncias medidos aqui para calcular coordenadas e verificar, na prática, se uma poligonal fecha dentro da tolerância da norma.

## Fontes

- ABNT NBR 13133:2021, *Execução de levantamento topográfico* — critérios de aceitação, precisão relativa mínima de 1:12.000 e tolerância angular das poligonais planimétricas. Edição confirmada na auditoria científica de 2026-08-29.
- COBRAC/UFSC, *Atualização da NBR 13133 e seus impactos* — documenta a simplificação das classes e tolerâncias das poligonais planimétricas na revisão de 2021. Consulta em 2026-08-29.

<!--
nivel: ensino-medio-sem-geologia-v1
palavras_corpo: ~1350
mapa_objetivo_secao:
  geologia-m20-oa07: "Por que um mapeamento geológico precisa de topografia instrumental" + "Como se mede distância e ângulo, na prática" + "Toda medida tem erro: os três tipos" + "Precisão não é o mesmo que acurácia" + "O que a NBR 13133 exige" + "Exemplo trabalhado"
alegacoes_auditaveis:
  - claim_id: GEO-M20-A07-CLASSIFICACAO-ERROS-001
    claim: "Erros de medição topográfica se classificam em grosseiro (engano detectável/eliminável), sistemático (causa conhecida, sentido único, corrigível) e acidental/aleatório (variação residual inevitável, tratada estatisticamente)."
    risk: conceitual
    source: "teoria clássica de erros em topografia, consistente com literatura técnica revisada em 2026-08-29"
  - claim_id: GEO-M20-A07-NBR13133-PRECISAO-002
    claim: "A ABNT NBR 13133:2021 (edição vigente) simplificou o esquema de classes das poligonais planimétricas das edições anteriores e adota precisão relativa mínima de referência de 1:12.000, admitindo tolerância diferente em casos especiais por acordo entre contratante e contratado; a tolerância angular cresce com a raiz do número de estações (Ta = 3 x p x raiz(n) + 10\")."
    risk: numerico
    source: "ABNT NBR 13133:2021; COBRAC/UFSC, 'Atualização da NBR 13133 e seus impactos'. Edição e valor confirmados na auditoria de 2026-08-29 (achado TOP-M20A07-NBR13133-002, corrigido) — a pendência anterior sobre a edição exata está resolvida."
-->
