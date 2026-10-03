# Questionário final cumulativo — Módulo 13: Geoprocessamento

**Módulo:** [[13-geoprocessamento-modulo|Módulo 13 — Geoprocessamento]]
**Cobertura:** Aulas 01 a 07 — módulo completo. As questões priorizam a **integração** entre aulas e o fio condutor que atravessa o módulo inteiro — escala, resolução e precisão — em vez de repetir isoladamente o que já foi cobrado nas três parciais.
**Objetivos avaliados:** `geologia-avancado-m13-oa01`, `geologia-avancado-m13-oa02`, `geologia-avancado-m13-oa03`, `geologia-avancado-m13-oa04`
**Pontuação total:** 100 pontos · o gabarito fica oculto; responda antes de abrir.

---

### 1. Dissertativa de síntese — `geologia-avancado-m13-q29` · oa01+oa02+oa03+oa04 · 15 pts

O hub deste módulo afirma: "um projeto de SIG produz mapas com aparência profissional independentemente da qualidade real dos dados ou da adequação do método escolhido — a responsabilidade de garantir que a aparência corresponda à validade real do resultado é sempre do analista, nunca do software." Mostre como essa mesma advertência aparece, sob formas diferentes, em pelo menos **três** momentos distintos do módulo (escala/datum na Aula 01, resolução de célula na Aula 02, RMSE na Aula 03, interpolação na Aula 05, limiar hidrológico na Aula 06, ou paleta/classificação na Aula 07) — escolha três e explique o fio condutor comum.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada (aceita qualquer combinação de três, desde que o fio condutor comum esteja correto):**

O fio condutor é: **o software nunca recusa produzir um resultado visualmente correto, mesmo quando o dado ou o método não sustentam aquele resultado — cabe ao analista, não à ferramenta, avaliar a validade real.**

- **Aula 01 (datum/escala):** sobrepor duas camadas em data diferentes (SAD69 e SIRGAS2000) desloca feições dezenas de metros no terreno real, mas o SIG desenha as duas sobrepostas sem qualquer aviso — a distorção é silenciosa.
- **Aula 02 (resolução de célula):** um raster de célula fina demais em relação à qualidade dos dados de origem "parece" mais detalhado, mas o detalhe extra é artefato de interpolação, não informação real — o software não sinaliza essa falsa precisão.
- **Aula 03 (RMSE):** um georreferenciamento com RMSE de 45 m pode ser aceitável ou não dependendo só da escala do dado-fonte — o próprio número do RMSE, isolado, não diz se o resultado é bom.
- **Aula 05 (interpolação):** qualquer interpolador, aplicado a qualquer conjunto de pontos, produz um mapa de isovalores suave e convincente, mesmo com dez pontos espalhados numa área enorme.
- **Aula 06 (limiar hidrológico):** o mesmo número de células de limiar representa áreas de contribuição muito diferentes conforme a resolução do MDE — o software aceita qualquer limiar numérico sem avisar que ele pode não corresponder à escala de drenagem real.
- **Aula 07 (paleta/classificação):** o método de classificação (quantil, intervalo igual, quebras naturais) pode fazer o mesmo conjunto de dados parecer mais ou menos preocupante, sem que um único valor de dado tenha mudado.
</details>

---

### 2. Múltipla escolha integrada — `geologia-avancado-m13-q30` · oa01 · 10 pts

Dos quatro data mencionados no módulo — Córrego Alegre, SAD69, SIRGAS2000 e WGS84 — quais dois são geocêntricos?

- a) Córrego Alegre e SAD69
- b) SAD69 e SIRGAS2000
- c) SIRGAS2000 e WGS84
- d) Córrego Alegre e WGS84

<details>
<summary>Ver resposta</summary>

**Resposta: c**

**SIRGAS2000** (elipsoide GRS80) e **WGS84** são os dois data **geocêntricos** e modernos, calculados por técnicas de posicionamento por satélite e centrados no centro de massa da Terra — apesar de terem definição praticamente coincidente, não são intercambiáveis com precisão, porque o SIRGAS2000 é estático (época 2000,4) e o WGS84 é dinâmico (acompanha o ITRF). **Córrego Alegre** (elipsoide de Hayford 1924) e **SAD69** (elipsoide UGGI-67/GRS67) são os dois data **clássicos, topocêntricos**, ajustados sem apoio de satélite — "a" é o par correto de clássicos, mas a pergunta pede os geocêntricos.
</details>

---

### 3. Aplicação integrada (cálculo) — `geologia-avancado-m13-q31` · oa01 · 10 pts

Um levantamento de campo mede altitude elipsoidal h = 1.204,80 m num ponto onde a ondulação geoidal (N) do MAPGEO2015 é de +22,30 m. Calcule a altitude ortométrica H. Depois, explique: se esse mesmo ponto fosse tratado erroneamente como estando em SAD69 quando na verdade as coordenadas horizontais são SIRGAS2000, que outro tipo de erro (independente do erro de altitude) se somaria ao problema?

<details>
<summary>Ver resolução</summary>

**Altitude ortométrica:** H = h − N = 1.204,80 − 22,30 = **1.182,50 m**.

**Erro adicional de datum horizontal:** tratar coordenadas SIRGAS2000 como se fossem SAD69 (ou vice-versa) introduz um deslocamento **horizontal** — não vertical — da ordem de **60 a 70 m** no território brasileiro, deslocamento típico entre os dois data. Os dois erros são de natureza diferente e não se cancelam nem se somam de forma simples: o da ondulação geoidal afeta a **altitude** (componente vertical, corrigida por h = H + N), enquanto o de datum horizontal afeta a **posição planimétrica** (x, y) do ponto — um projeto real pode ter os dois problemas simultaneamente, e cada um exige sua própria correção.
</details>

---

### 4. Verdadeiro ou Falso (justifique) — `geologia-avancado-m13-q32` · oa01 · 10 pts

"Um serviço de pós-processamento que combina os dados de um receptor de campo com os de uma estação de referência da RBMC do IBGE é, tecnicamente, um exemplo de PPP (Precise Point Positioning)."

<details>
<summary>Ver resposta</summary>

**Falso.**

Esse é o **posicionamento relativo pós-processado** (estático ou cinemático — PPK), que usa uma ou mais **estações de referência de coordenadas conhecidas** (a RBMC, no Brasil) para calcular correções. O **PPP** é um método diferente: processa o receptor **isoladamente**, sem estação de referência nenhuma, usando órbitas e correções de relógio de alta precisão publicadas por centros de análise internacionais — é assim que funciona o serviço on-line IBGE-PPP. Chamar todo pós-processamento de "PPP" é um erro corrente que a auditoria científica deste módulo corrigiu explicitamente: PPP é um método específico, não sinônimo de "processado depois".
</details>

---

### 5. Múltipla escolha integrada — `geologia-avancado-m13-q33` · oa02→oa04 · 10 pts

Um projeto tem quatro insumos: (i) um MDE de 30 m; (ii) polígonos de unidades litológicas mapeadas; (iii) uma imagem de satélite multiespectral; (iv) pontos de amostragem geoquímica antes de qualquer interpolação. Depois de interpolar (iv) para gerar uma superfície contínua de teor, qual é a estrutura de dado nativa de cada um dos quatro insumos, considerando (iv) tanto antes quanto depois da interpolação?

- a) Todos são vetoriais, exceto a imagem de satélite
- b) (i) raster; (ii) vetor; (iii) raster; (iv) vetor (pontos) antes da interpolação, tornando-se raster depois
- c) (i) vetor; (ii) raster; (iii) vetor; (iv) raster antes, vetor depois
- d) Todos são raster, porque um MDE sempre converte as demais camadas para sua própria estrutura

<details>
<summary>Ver resposta</summary>

**Resposta: b**

O **MDE** (i) é nativamente raster (superfície contínua de elevação); os **polígonos litológicos** (ii) são nativamente vetoriais (feições discretas com atributos); a **imagem de satélite** (iii) é nativamente raster (grade regular de pixels, definição do próprio sensor); e os **pontos de amostragem** (iv) chegam como camada vetorial de pontos (importados por coordenada XY), mas, depois de passarem por um método de interpolação (IDW, krigagem ou spline), o resultado é uma **superfície contínua raster** — a mesma ponte entre estrutura vetorial e matricial que a Aula 05 explora. "d" está errado: um MDE não converte as demais camadas para sua própria estrutura; cada camada mantém sua estrutura nativa, e a conversão (quando ocorre) é uma decisão de análise, não uma imposição automática.
</details>

---

### 6. Aplicação integrada — `geologia-avancado-m13-q34` · oa03 · 10 pts

Um mapa cruza um buffer de 400 m em torno de um poço de monitoramento (área calculada pelo software: 0,50 km²) com um polígono de área agrícola de 3,2 km². A interseção entre os dois retorna 0,31 km². O relatório do projeto precisa afirmar "a área agrícola exposta à zona de influência do poço". Qual dos três valores deve constar no relatório, e que erro conceitual cometeria alguém que reportasse o valor de 0,50 km² para essa finalidade?

<details>
<summary>Ver resolução</summary>

O valor correto é **0,31 km²** — o resultado da **interseção**, que é a única geometria que representa simultaneamente as duas condições exigidas: estar dentro da zona de influência do poço **e** ser área agrícola.

Reportar 0,50 km² (a área do buffer inteiro) cometeria o erro de tratar toda a zona de influência do poço como se fosse área agrícola — mas o buffer, por definição, inclui qualquer tipo de uso do solo dentro daquele raio, não apenas terra agrícola. O erro é confundir "a área da zona de influência" com "a área agrícola dentro da zona de influência" — dois números diferentes que só a operação de interseção (não o buffer isolado) consegue produzir corretamente.
</details>

---

### 7. Verdadeiro ou Falso (justifique) — `geologia-avancado-m13-q35` · oa03→oa04 · 10 pts

"A álgebra de mapas de Tomlin e as relações topológicas do modelo DE-9IM são, na prática, dois nomes para o mesmo conjunto de operações, aplicáveis indiferentemente a dados vetoriais ou matriciais."

<details>
<summary>Ver resposta</summary>

**Falso.**

São formalismos distintos, ligados a modelos de dado distintos, e essa distinção é reforçada deliberadamente neste módulo por ser uma **contradição transversal** identificada e corrigida pela auditoria científica: a **álgebra de mapas** (Tomlin, 1990) é o formalismo de operações **célula a célula sobre rasters** — soma, multiplicação, reclassificação entre camadas matriciais (retomada na Aula 06, na derivação de produtos de MDE). O **DE-9IM** (Clementini e Egenhofer, adotado pela especificação OGC Simple Features) formaliza **relações topológicas entre geometrias vetoriais** — contém, está dentro, cruza, toca (Aula 04). Essa distinção é a mesma já fixada nos Módulos 07 e 08 deste curso, onde "álgebra de mapas" designa consistentemente a operação raster — nenhum material deste módulo pode contradizer esse vocabulário já estabelecido.
</details>

---

### 8. Aplicação integrada (cálculo) — `geologia-avancado-m13-q36` · oa04 · 10 pts

Um analista compara dois MDEs da mesma bacia — um de resolução 10 m e outro de resolução 25 m — usando o mesmo limiar de acumulação de fluxo de 1.000 células em ambos. Calcule a área de drenagem contribuinte mínima representada por esse limiar em cada resolução, e explique por que a rede de drenagem derivada do MDE de 25 m provavelmente terá canais reais "faltando" em comparação com a do MDE de 10 m.

<details>
<summary>Ver resolução</summary>

**MDE de 10 m:** célula = 10 × 10 = 100 m². Área mínima = 1.000 × 100 = 100.000 m² = **0,10 km²**.

**MDE de 25 m:** célula = 25 × 25 = 625 m². Área mínima = 1.000 × 625 = 625.000 m² = **0,625 km²**.

A área mínima no MDE de 25 m é mais de **6 vezes maior** que no de 10 m, usando exatamente o mesmo número de células como limiar. Isso significa que, no MDE de 25 m, um trecho de canal real cuja bacia de contribuição tenha, por exemplo, 0,3 km² **não seria classificado como canal** (porque está abaixo do limiar de 0,625 km² efetivo), enquanto o mesmo trecho, no MDE de 10 m, estaria bem acima do limiar de 0,10 km² e apareceria corretamente na rede derivada. O limiar em número de células, sem conversão para área real, é a causa direta dessa omissão — não um problema do algoritmo D8 em si.
</details>

---

### 9. Dissertativa curta — `geologia-avancado-m13-q37` · oa01→oa03 · 10 pts

Explique por que a Aula 04 insiste que o cálculo de área de feições vetoriais deve ser feito em coordenadas projetadas (planas), nunca em coordenadas geográficas (graus), e relacione essa exigência com a discussão de projeções da Aula 01.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:**

Coordenadas geográficas (latitude/longitude, em graus) localizam pontos sobre a superfície **curva** do elipsoide — o comprimento de um grau de longitude muda com a latitude, então calcular "área" diretamente a partir de diferenças de graus não corresponde a uma área real e consistente no terreno. Coordenadas **projetadas** (como UTM), resultado de uma projeção matemática da superfície curva para um plano, permitem trabalhar com distâncias e áreas em metros de forma direta, como numa planta cartesiana comum.

A ligação com a Aula 01: toda projeção distorce pelo menos uma das três propriedades geométricas (forma, área, distância) — nenhuma preserva as três. Um cálculo de área feito num sistema de coordenadas geográficas não usa nenhuma projeção que preserve área; feito numa projeção conforme (como a UTM, usada para trabalho local a regional), o erro de área introduzido é pequeno o bastante para a maioria dos usos práticos dentro de um único fuso — mas calcular área diretamente em graus, sem projeção alguma, produziria um resultado sem correspondência real e potencialmente muito distorcido, sobretudo em latitudes altas.
</details>

---

### 10. Dissertativa de encerramento — `geologia-avancado-m13-q38` · oa01+oa02+oa03+oa04 · 5 pts

O objetivo declarado deste módulo é "elaborar, analisar e entregar projetos cartográficos digitais em ambiente SIG, da base cartográfica à análise espacial e ao layout final". Em duas ou três frases, explique como as sete aulas do módulo, em conjunto, cumprem essa promessa — e por que um mapa final tecnicamente "bonito" não é, por si só, prova de que o projeto foi bem feito.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada (síntese, não fatos novos):**

O sistema de referência (Aula 01) fixa em que geodésia o projeto inteiro vive; a estrutura de dados (Aula 02) organiza como cada informação é armazenada; o georreferenciamento e a aquisição de campo (Aula 03) trazem dados novos para dentro desse sistema, corretamente posicionados; as operações vetoriais (Aula 04) e a interpolação (Aula 05) transformam camadas isoladas em análise; os produtos de MDE (Aula 06) derivam variáveis de relevo e hidrologia; e o layout (Aula 07) entrega tudo isso de forma auditável. Um mapa final "bonito" não é prova de projeto bem feito porque, como o módulo insiste do início ao fim, o software produz aparência profissional independentemente da qualidade real dos dados — um datum errado na Aula 01, uma resolução inadequada na Aula 02, um interpolador mal escolhido na Aula 05 ou um limiar hidrológico não convertido em área na Aula 06 podem estar silenciosamente embutidos no mapa final sem que sua aparência dê qualquer sinal disso. A validade de um projeto de geoprocessamento se avalia pela documentação e pelo método em cada etapa, não pela aparência do produto final.
</details>

---

## Gabarito resumido

| Questão | ID | Resposta |
|---|---|---|
| 1 | q29 | ver comentário (fio condutor: aparência profissional não garante validade — datum, resolução, RMSE, interpolação, limiar, paleta) |
| 2 | q30 | c (SIRGAS2000 e WGS84 são geocêntricos) |
| 3 | q31 | H = 1.204,80 − 22,30 = 1.182,50 m; erro de datum horizontal seria deslocamento de 60-70 m, natureza distinta do erro de altitude |
| 4 | q32 | Falso (isso é posicionamento relativo pós-processado/PPK com RBMC; PPP processa o receptor isolado) |
| 5 | q33 | b (MDE raster; litologia vetor; imagem raster; pontos vetor antes → raster depois da interpolação) |
| 6 | q34 | reportar 0,31 km² (interseção); 0,50 km² erra ao tratar toda a zona de influência como agrícola |
| 7 | q35 | Falso (álgebra de mapas = Tomlin/raster; DE-9IM = relações topológicas vetoriais — não confundir, contradiria M07/M08) |
| 8 | q36 | 0,10 km² a 10 m; 0,625 km² a 25 m; MDE grosseiro omite canais reais abaixo do limiar efetivo maior |
| 9 | q37 | ver comentário (graus não correspondem a área real; projeção plana permite cálculo direto em metros; nenhuma projeção preserva tudo) |
| 10 | q38 | ver comentário (síntese das sete aulas; aparência não garante validade do projeto) |
