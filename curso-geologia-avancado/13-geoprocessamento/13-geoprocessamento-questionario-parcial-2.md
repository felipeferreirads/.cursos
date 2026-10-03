# Questionário parcial 2 — Módulo 13: Geoprocessamento

**Módulo:** [[13-geoprocessamento-modulo|Módulo 13 — Geoprocessamento]]
**Cobertura:** Aulas 04 e 05 — geoprocessamento vetorial (sobreposição, buffer, dissolve, relações topológicas) e interpolação espacial (IDW, krigagem, spline, mapas de isovalores).
**Recorte:** o que se faz com o dado depois que ele já entrou correto no SIG (parcial 1) — a análise sobre dados vetoriais e pontuais. Os produtos derivados de MDE (Aula 06) ficam para a parcial 3.
**Objetivos avaliados:** `geologia-avancado-m13-oa03` (integral — a04 + a05)
**Pontuação total:** 100 pontos · o gabarito fica oculto; responda antes de abrir.

---

### 1. Múltipla escolha — `geologia-avancado-m13-q11` · oa03 · 10 pts

Um analista quer saber apenas a porção de uma unidade litológica que está dentro de um polígono de concessão mineral, descartando tanto a parte da unidade fora da concessão quanto a parte da concessão sem aquela litologia. Qual operação de sobreposição responde exatamente a essa pergunta?

- a) União (Union)
- b) Diferença (Erase/Difference)
- c) Interseção (Intersect)
- d) Dissolve

<details>
<summary>Ver resposta</summary>

**Resposta: c**

A **interseção** retorna apenas a área onde as duas camadas de entrada se sobrepõem espacialmente — exatamente "o que existe dentro de quê". A **união** manteria também as áreas não sobrepostas de ambas; a **diferença** retornaria a área de uma camada não coberta pela outra (o oposto do que se quer); o **dissolve** não é uma operação de sobreposição entre duas camadas — funde polígonos adjacentes de uma mesma camada que compartilham um atributo.
</details>

---

### 2. Aplicação (cálculo) — `geologia-avancado-m13-q12` · oa03 · 15 pts

Uma linha de contato geológico de 8 km de extensão, aproximadamente retilínea, precisa de uma zona de segurança de 150 m para cada lado, conforme norma do projeto. Calcule (a) a largura total da zona de segurança e (b) a área aproximada do buffer resultante, ignorando o pequeno acréscimo das extremidades arredondadas. (c) Se essa zona de segurança for cruzada, por interseção, com um polígono de área de vegetação nativa de 2,1 km², e o SIG retornar uma área de interseção de 0,95 km², que valor deve ser reportado como "área de vegetação nativa exposta à zona de segurança do contato", e por quê não é nem o valor do buffer nem o da vegetação inteira?

<details>
<summary>Ver resolução</summary>

**(a)** O buffer é bilateral por padrão: 150 m de cada lado da linha somam **300 m** de largura total.

**(b)** Área ≈ comprimento × largura total = 8.000 m × 300 m = 2.400.000 m² = **2,4 km²** (estimativa de ordem de grandeza, sem as extremidades arredondadas que o software calcula com precisão).

**(c)** O valor a reportar é os **0,95 km²** resultantes da interseção — nem os 2,4 km² do buffer inteiro (que inclui área sem vegetação nativa), nem os 2,1 km² da vegetação inteira (que inclui área fora da zona de segurança), mas especificamente a porção onde as duas condições coexistem: vegetação nativa **e** dentro da zona de segurança. É exatamente esse número — e só ele — que a operação combinada de buffer seguida de interseção é capaz de produzir de forma defensável; reportar qualquer um dos outros dois valores superestimaria a exposição real.
</details>

---

### 3. Verdadeiro ou Falso (justifique) — `geologia-avancado-m13-q13` · oa03 · 10 pts

"As relações topológicas usadas em consultas espaciais vetoriais — como 'dentro de', 'cruza', 'toca' — são formalizadas pelo mesmo formalismo que a álgebra de mapas de Tomlin, aplicado a geometrias vetoriais em vez de células."

<details>
<summary>Ver resposta</summary>

**Falso.**

São dois formalismos distintos, para dois modelos de dado distintos. As relações topológicas vetoriais (contém, está dentro, cruza, toca, sobrepõe, é disjunto de) são formalizadas pelo modelo **DE-9IM** (*Dimensionally Extended 9-Intersection Model*, Clementini e Egenhofer), adotado pela especificação OGC *Simple Features* (ISO 19125). A **álgebra de mapas**, no sentido de **Tomlin (1990)**, é o formalismo de operações **célula a célula sobre rasters** — soma, multiplicação, reclassificação entre camadas matriciais — tema retomado na Aula 06 deste módulo, não desta. Confundir os dois é um erro registrado explicitamente pela auditoria científica deste módulo, inclusive porque contradiria o vocabulário já fixado nos Módulos 07 e 08 do curso, onde "álgebra de mapas" designa consistentemente a operação raster.
</details>

---

### 4. Dissertativa curta — `geologia-avancado-m13-q14` · oa03 · 10 pts

Um mapa geológico digitalizado tem 34 polígonos separados, todos pertencentes à mesma unidade litoestratigráfica, mapeados individualmente em diferentes sessões de campo. Explique o que a operação dissolve faz nesse caso, e por que calcular a área total da unidade somando as áreas dos 34 polígonos individuais, sem dissolver antes, é uma prática arriscada.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:**

O **dissolve**, aplicado pelo atributo de unidade litoestratigráfica, remove as fronteiras internas entre os polígonos adjacentes que compartilham esse valor, fundindo-os numa única feição (ou num conjunto menor de feições, se a unidade não for espacialmente contígua) — eliminando as "costuras" do levantamento original e simplificando a visualização.

Somar as áreas dos 34 polígonos individuais sem dissolver é arriscado porque polígonos mapeados em sessões de campo diferentes podem ter, entre si, **pequenas sobreposições ou lacunas nas bordas** (erros de digitalização, de traçado em campo, ou de junção entre folhas de mapeamento adjacentes) — somar as áreas individuais nesse caso conta a área sobreposta **duas vezes**, ou deixa de contar áreas de lacuna, produzindo um valor de área total sistematicamente incorreto. O dissolve, ao fundir os polígonos numa geometria única antes do cálculo, evita essa dupla contagem (ou subcontagem) de forma estruturalmente correta.
</details>

---

### 5. Múltipla escolha — `geologia-avancado-m13-q15` · oa03 · 10 pts

Qual das afirmações abaixo distingue corretamente IDW e krigagem?

- a) IDW é geoestatístico e fornece incerteza; krigagem é determinístico e não fornece incerteza
- b) Os dois produzem exatamente o mesmo resultado numérico, diferindo apenas na velocidade de processamento
- c) IDW é determinístico (pondera pelo inverso da distância, sem modelo estatístico subjacente) e nunca extrapola além do intervalo de valores observados; krigagem é geoestatística, baseada em variograma, e fornece tanto o valor estimado quanto uma estimativa de incerteza (variância de krigagem)
- d) Krigagem sempre produz padrões de "olho de boi" ao redor de cada ponto amostral; IDW nunca produz esse artefato

<details>
<summary>Ver resposta</summary>

**Resposta: c**

O IDW é **determinístico**: aplica a regra "quanto mais perto, mais peso" sem modelo estatístico de fundo, e o valor interpolado está sempre entre o mínimo e o máximo dos pontos amostrais usados (nunca extrapola). A krigagem é **geoestatística**: usa a estrutura de autocorrelação espacial (variograma) para calcular pesos ótimos e entrega, além do valor estimado, a **variância de krigagem** — maior em áreas de baixa densidade amostral. "a" inverte os dois métodos; "b" ignora que os métodos produzem superfícies visivelmente diferentes; "d" atribui o artefato de "olho de boi" ao método errado — é característico do IDW, não da krigagem.
</details>

---

### 6. Aplicação — `geologia-avancado-m13-q16` · oa03 · 15 pts

Uma campanha amostrou o nível estático de um aquífero em 20 poços, distribuídos de forma razoavelmente uniforme por toda a área de 6 km² de interesse — sem concentração numa sub-região específica. O geólogo precisa decidir entre IDW e krigagem para gerar o mapa potenciométrico. Diferente do cenário de amostragem desigual visto na aula, aqui a distribuição é uniforme. Isso torna a escolha do método irrelevante? Justifique considerando o que cada método oferece além do mapa de valores em si.

<details>
<summary>Ver resolução</summary>

Não torna a escolha irrelevante, mas muda o que está em jogo. Com amostragem uniforme, o argumento mais forte a favor da krigagem no cenário desigual — mostrar onde a estimativa é confiável e onde não é — perde parte da força, porque a incerteza tende a ser mais homogênea em toda a área. Ainda assim, a krigagem continua sendo a escolha preferível sempre que a decisão subsequente tiver custo alto (aqui, um mapa potenciométrico usado para gestão de um aquífero), porque ela entrega a **variância de krigagem** como produto adicional, permitindo comunicar objetivamente o grau de confiança da superfície — algo que o IDW, por ser determinístico, simplesmente não oferece, mesmo com amostragem uniforme. A decisão, portanto, depende menos da uniformidade da amostragem e mais de quanto a aplicação subsequente se beneficia de uma medida explícita de incerteza; para um mapa exploratório de baixo risco, o IDW, mais simples computacionalmente, pode ser suficiente.
</details>

---

### 7. Verdadeiro ou Falso (justifique) — `geologia-avancado-m13-q17` · oa03 · 10 pts

"Se um mapa de isovalores tem aparência suave e profissional, isso é evidência de que a densidade e a distribuição dos pontos amostrais usados são adequadas."

<details>
<summary>Ver resposta</summary>

**Falso.**

Esse é o ponto de maior risco prático da interpolação espacial: **qualquer** método, aplicado a **qualquer** conjunto de pontos — inclusive dez pontos espalhados aleatoriamente numa área enorme — produz uma superfície de aparência suave e visualmente convincente, com a mesma aparência profissional de um mapa gerado a partir de mil pontos bem distribuídos. A aparência do mapa não revela, por si só, a densidade amostral, a adequação do método à estrutura espacial real da variável, nem se o resultado foi validado contra pontos não usados no ajuste (validação cruzada). Por isso a escolha e a calibração do interpolador nunca deveriam ser tratadas como um passo puramente automático de software.
</details>

---

### 8. Múltipla escolha — `geologia-avancado-m13-q18` · oa03 · 10 pts

Num mapa de isovalores de teor geoquímico, um conjunto de isolinhas fechadas, com valores crescentes para dentro, aparece centrado num único poço dentro de uma área densamente amostrada. O que esse padrão indica?

- a) Um artefato do interpolador, sempre — isolinhas fechadas nunca refletem dado real
- b) Um máximo local sustentado pelos dados vizinhos — no caso geoquímico, uma anomalia, candidata a alvo de prospecção
- c) Um erro de digitação nas coordenadas do poço central
- d) Necessariamente um mínimo local, já que isolinhas fechadas sempre representam depressões

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Um conjunto de isolinhas fechadas com valores **crescentes** para dentro indica um **máximo local** — e, como está dentro da faixa densamente amostrada (não numa região de baixa densidade, onde o mesmo padrão poderia ser artefato do interpolador), é um máximo sustentado por dados vizinhos, não um artefato. Num mapa geoquímico, esse é exatamente o padrão chamado **anomalia** — o primeiro indício visual de um alvo de prospecção a investigar com mais detalhe. "a" e "c" descartam sem justificativa a possibilidade de um padrão real; "d" erra a direção — isolinhas fechadas indicam máximo **ou** mínimo, dependendo de os valores crescerem ou decrescerem para dentro, não sempre mínimo.
</details>

---

### 9. Dissertativa curta — `geologia-avancado-m13-q19` · oa03 · 10 pts

No exemplo trabalhado de buffer e interseção da Aula 04 (zona de segurança de uma falha cruzada com área urbana), o texto apresenta três números: a área do buffer inteiro, a área da zona urbana inteira, e a área de interseção entre os dois — dizendo "suponha que o SIG retorne 1,35 km²" para essa última. Por que o exemplo precisa "supor" esse valor, em vez de calculá-lo diretamente a partir do enunciado, e qual dos três números é o correto a reportar?

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:**

A área de uma interseção geométrica real entre duas geometrias complexas (um buffer com extremidades arredondadas e um polígono de área urbana de forma irregular) **não tem como ser calculada analiticamente** a partir de um enunciado em prosa — ela depende da forma exata das duas geometrias, algo que só o SIG, operando sobre a geometria real, pode calcular com precisão. Por isso o exemplo declara o valor como suposto, em vez de fingir uma dedução que não existe.

O número correto a reportar é o da **interseção** (1,35 km² no exemplo) — nem a área do buffer inteiro (que inclui território fora da área urbana), nem a área urbana inteira (que inclui território fora da zona de segurança), mas especificamente a porção onde as duas condições coexistem. É esse o raciocínio central do exemplo: saber **qual dos três números** responde à pergunta feita, independentemente de qual deles seja numericamente maior ou mais fácil de calcular.
</details>

---

## Gabarito resumido

| Questão | ID | Resposta |
|---|---|---|
| 1 | q11 | c (interseção) |
| 2 | q12 | largura 300 m; área do buffer ≈ 2,4 km²; reportar 0,95 km² da interseção |
| 3 | q13 | Falso (relações topológicas vetoriais = DE-9IM/OGC; álgebra de mapas = Tomlin, raster) |
| 4 | q14 | ver comentário (dissolve funde e evita dupla contagem de área em bordas sobrepostas/com lacunas) |
| 5 | q15 | c (IDW determinístico sem incerteza, nunca extrapola; krigagem geoestatística, com variância de krigagem) |
| 6 | q16 | ver comentário (krigagem ainda preferível quando a decisão tem custo alto, mesmo com amostragem uniforme) |
| 7 | q17 | Falso (todo interpolador produz mapa convincente, independentemente da qualidade dos dados) |
| 8 | q18 | b (máximo local / anomalia, dentro de área bem amostrada) |
| 9 | q19 | ver comentário (área não é dedutível do enunciado; reportar a interseção, 1,35 km²) |
