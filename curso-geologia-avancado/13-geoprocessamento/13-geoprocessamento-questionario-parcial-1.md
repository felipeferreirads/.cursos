# Questionário parcial 1 — Módulo 13: Geoprocessamento

**Módulo:** [[13-geoprocessamento-modulo|Módulo 13 — Geoprocessamento]]
**Cobertura:** Aulas 01 a 03 — fundamentos cartográficos (elipsoide, geoide, datum, sistemas de coordenadas, projeções, escala), estruturas vetorial e matricial em ambiente SIG, e georreferenciamento/GPS-GNSS/aquisição digital de campo.
**Recorte:** como o dado entra correto num SIG — em que sistema de referência ele nasce (oa01) e em que estrutura ele é armazenado e organizado (oa02) — antes de qualquer análise espacial, que é assunto da parcial 2.
**Objetivos avaliados:** `geologia-avancado-m13-oa01` (integral — a01 + a03), `geologia-avancado-m13-oa02` (integral — a02 + a seção "Aquisição digital de dados em campo" da a03)
**Pontuação total:** 100 pontos · o gabarito fica oculto; responda antes de abrir.

---

### 1. Múltipla escolha — `geologia-avancado-m13-q01` · oa01 · 10 pts

Um shapefile histórico traz a anotação "Datum: Córrego Alegre". Qual elipsoide de referência esse datum usa, e qual dos outros dois data brasileiros citados nesta aula é frequentemente confundido com ele por compartilhar uma origem terrestre não geocêntrica?

- a) Elipsoide UGGI-67/GRS67; confundido com o SIRGAS2000
- b) Elipsoide Internacional de Hayford (1924); confundido com o SAD69, que também é topocêntrico (origem no vértice Chuá, MG), mas usa o elipsoide UGGI-67/GRS67
- c) Elipsoide GRS80; confundido com o WGS84, que também é geocêntrico
- d) Elipsoide Internacional de Hayford (1924); confundido com o SIRGAS2000, que usa o mesmo elipsoide

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Córrego Alegre é o datum clássico brasileiro assentado no elipsoide **Internacional de Hayford (1924)**. O erro mais comum — e o que a auditoria científica deste módulo corrigiu como achado vermelho — é atribuir esse mesmo elipsoide ao **SAD69**, que na verdade usa o elipsoide **UGGI-67/GRS67** (semieixo maior 6.378.160 m). Os dois são, de fato, parecidos no que importa para a confusão: ambos são data clássicos, topocêntricos (não geocêntricos), calculados sem apoio de satélite. "c" e "d" erram ao aproximar Córrego Alegre de datas geocêntricas modernas (SIRGAS2000, GRS80), que não têm relação de elipsoide com ele.
</details>

---

### 2. Verdadeiro ou Falso (justifique) — `geologia-avancado-m13-q02` · oa01 · 10 pts

"No Brasil, a ondulação geoidal (N) é uma correção pequena, tipicamente entre -5 m e -10 m, que pode ser desprezada em levantamentos altimétricos de precisão moderada."

<details>
<summary>Ver resposta</summary>

**Falso.**

Segundo o modelo oficial **MAPGEO2015** (IBGE/EPUSP), a ondulação geoidal no território brasileiro varia numa faixa da ordem de **-30 m a +30 m**, com isolinhas traçadas de 5 em 5 m — muito maior, em módulo, do que -5 a -10 m, e com os **dois sinais** possíveis conforme a região, não apenas negativo. Longe de desprezível, ignorar N inviabiliza qualquer combinação entre altitude geométrica (do GPS/GNSS, referida ao elipsoide) e altitude ortométrica (referida ao geoide) — as duas se relacionam por h = H + N, e um erro de dezenas de metros nessa correção se propaga diretamente para qualquer altitude calculada a partir de posicionamento por satélite.
</details>

---

### 3. Aplicação (cálculo) — `geologia-avancado-m13-q03` · oa01 · 10 pts

Um receptor GNSS registra, num ponto de campo, a altitude elipsoidal (geométrica) h = 812,40 m. A ondulação geoidal (N) do MAPGEO2015 para esse ponto é de -18,60 m. Calcule a altitude ortométrica (H) desse ponto — a que efetivamente interessa para relacionar com uma cota de nível ou uma seção geológica local — e explique por que simplesmente usar h como se fosse H seria um erro nesse caso.

<details>
<summary>Ver resolução</summary>

Da relação h = H + N, isola-se H:

H = h − N = 812,40 − (−18,60) = 812,40 + 18,60 = **831,00 m**

Usar h (812,40 m) diretamente como se fosse a altitude ortométrica introduziria um erro de **18,60 m** — nesse caso o geoide está abaixo do elipsoide no ponto (N negativo), então a altitude física real acima do nível médio dos mares (H) é maior que a altitude geométrica lida diretamente do GPS. Um erro dessa magnitude é grande o bastante para invalidar o cruzamento com uma cota topográfica de referência ou com a espessura de uma unidade geológica medida por outros meios — exatamente o tipo de deslocamento silencioso que a Aula 01 descreve: o software não acusa nada, o número simplesmente está errado.
</details>

---

### 4. Múltipla escolha — `geologia-avancado-m13-q04` · oa01 · 10 pts

Sobre a adoção do SIRGAS2000 como sistema de referência oficial no Brasil, qual afirmação está correta?

- a) O SIRGAS2000 foi oficializado numa única data, 25/02/2015, quando passou a ser o único sistema válido
- b) O SIRGAS2000 foi adotado em 2005 (Resolução IBGE/PR 1/2005), com um período de transição de dez anos, e passou a ser o único sistema de referência válido no SGB e no SCN a partir de 25/02/2015 (Resolução IBGE/PR 1/2015)
- c) O SIRGAS2000 é usado no Brasil desde 1969, substituindo o SAD69 na mesma data
- d) A transição do SAD69 para o SIRGAS2000 não teve prazo definido e segue em aberto até hoje

<details>
<summary>Ver resposta</summary>

**Resposta: b**

São **duas datas**, não uma: a **adoção oficial em 25/02/2005** (Res. IBGE/PR 1/2005), que abriu um período de transição de dez anos em que SAD69 ainda podia ser usado, e o **fim da transição em 25/02/2015** (Res. IBGE/PR 1/2015), quando o SIRGAS2000 passou a ser o único sistema válido no Sistema Geodésico Brasileiro (SGB) e no Sistema Cartográfico Nacional (SCN). Tratar 2015 como a única data relevante apaga a década de transição — que é justamente a razão de ainda existir tanto acervo cartográfico legado em SAD69 circulando em projetos atuais.
</details>

---

### 5. Dissertativa curta — `geologia-avancado-m13-q05` · oa01 · 10 pts

Um geólogo recebe duas camadas vetoriais com coordenadas UTM numericamente idênticas para um mesmo ponto de interesse — uma em SAD69, outra em SIRGAS2000, ambas fuso 23S. Ele conclui que, como os números batem, as camadas estão corretamente sobrepostas. Explique por que essa conclusão é falsa e qual é a ordem de grandeza do erro envolvido no território brasileiro.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:**

SAD69 e SIRGAS2000 são data distintos — origens diferentes (SAD69 topocêntrico, no vértice Chuá; SIRGAS2000 geocêntrico) e elipsoides diferentes (UGGI-67/GRS67 contra GRS80). Coordenadas com o **mesmo valor numérico** em datum diferente correspondem a **locais físicos diferentes** no terreno real — a numeração da grade UTM não "sabe" a que datum pertence, o deslocamento acontece na conversão de coordenada para posição real. No Brasil, essa diferença entre SAD69 e SIRGAS2000 é da ordem de **60 a 70 metros** na maior parte do território (variando regionalmente). O erro do geólogo é presumir que "mesma UTM, mesmo fuso" significa "mesmo lugar" — a correção exige reprojetar (transformar de datum) uma das camadas para o mesmo sistema de referência da outra antes de qualquer sobreposição ou análise conjunta.
</details>

---

### 6. Múltipla escolha — `geologia-avancado-m13-q06` · oa02 · 10 pts

Um projeto precisa representar, ao mesmo tempo, (i) os contatos litológicos mapeados em campo, com atributos de nome de formação e tipo de contato, e (ii) uma superfície contínua de concentração geoquímica interpolada em toda a área. Qual estrutura de dados é a nativamente adequada para cada um, e por quê?

- a) Ambos devem ser vetoriais, porque vetor é sempre mais preciso que raster
- b) Contatos litológicos como raster (célula a célula) e concentração interpolada como vetor, porque o vetor permite consultas por atributo
- c) Contatos litológicos como vetor (feições discretas com identidade e atributos individuais) e concentração interpolada como raster (fenômeno de variação contínua, sem limites naturais)
- d) Ambos devem ser raster, porque um SIG moderno sempre converte vetor em raster antes de qualquer análise

<details>
<summary>Ver resposta</summary>

**Resposta: c**

O critério de decisão não é "qual estrutura é melhor" — é se o fenômeno tem **limites discretos e identidade individual** (vetor: contatos litológicos, cada um com atributos próprios de formação e tipo de contato) ou **varia continuamente no espaço, sem fronteiras naturais** (raster: uma superfície de concentração interpolada, onde cada célula é apenas um valor estimado, sem "feição" própria). "a" e "d" erram ao tratar uma estrutura como universalmente superior; "b" inverte exatamente o critério correto.
</details>

---

### 7. Verdadeiro ou Falso (justifique) — `geologia-avancado-m13-q07` · oa02 · 10 pts

"Um raster de resolução espacial mais fina (célula menor) é sempre preferível, porque representa o terreno com mais detalhe, independentemente da qualidade dos dados de origem que geraram o raster."

<details>
<summary>Ver resposta</summary>

**Falso.**

A resolução espacial é o parâmetro mais crítico de um raster, mas uma célula fina demais **em relação à qualidade dos dados de origem** cria uma falsa impressão de precisão: o raster "parece" mais detalhado, mas o detalhe extra é artefato de interpolação ou reamostragem, não informação real adicional. O paralelo é direto com o princípio de escala da Aula 01 — não faz sentido produzir um produto de resolução fina a partir de uma base cujo levantamento original não sustenta aquele nível de detalhe. Uma célula grossa demais, por outro lado, também é problemática por suavizar feições reais — o ponto central é que a resolução adequada é a que **corresponde à qualidade e à densidade dos dados de origem**, não a menor célula tecnicamente possível.
</details>

---

### 8. Aplicação — `geologia-avancado-m13-q08` · oa02 · 10 pts

Um projeto recebe uma planilha com 40 linhas: colunas de coordenada X (leste) e Y (norte) em UTM SIRGAS2000, mais colunas de número de amostra e teor em ppm — sem qualquer geometria explícita. Descreva o procedimento correto para transformar essa planilha numa camada vetorial utilizável no SIG, e explique por que chamar essa operação de "geocodificação" pode ser impreciso, dependendo da fonte consultada.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:**

O procedimento é a **importação de tabela de coordenadas XY** (por exemplo, "XY Table to Point" ou "Adicionar camada de texto delimitado", conforme o software): a partir dos campos de coordenada X e Y e do sistema de referência declarado da planilha (que precisa ser conhecido — aqui, UTM SIRGAS2000), o SIG gera uma camada vetorial de **pontos**, um por linha, transportando automaticamente os demais campos (número da amostra, teor em ppm) para a tabela de atributos da nova camada.

Quanto ao nome: o glossário da ESRI usa "geocodificação" em sentido amplo, que incluiria esse caso. Mas na maior parte da bibliografia de SIG e no uso corrente de mercado, **geocodificação** designa especificamente a conversão de **endereços** (texto) em coordenadas, por comparação com uma base de logradouros — um problema tecnicamente distinto, sujeito a erro de correspondência (matching), que não está em jogo aqui. Por isso é mais preciso nomear a operação pelo que ela faz — importação de tabela XY — e reservar "geocodificação" para o caso do endereço.
</details>

---

### 9. Múltipla escolha — `geologia-avancado-m13-q09` · oa01 · 10 pts

Por que o posicionamento por satélite exige sinal de pelo menos **quatro** satélites simultaneamente visíveis, e não apenas três?

- a) Porque a posição é bidimensional (x, y), e cada satélite adicional aumenta a precisão linearmente
- b) Porque três distâncias bastariam geometricamente para fixar um ponto no espaço, mas o relógio do receptor não é atômico como o dos satélites — seu erro de sincronismo é uma quarta incógnita, resolvida junto com x, y e z; por isso as distâncias medidas se chamam pseudodistâncias
- c) Porque um satélite é sempre reservado como backup em caso de falha de sinal
- d) Porque o DOP (dilution of precision) exige exatamente quatro satélites por definição matemática

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Três distâncias já bastariam para fixar geometricamente um ponto em três dimensões (x, y, z) — o problema é que o **relógio do receptor** não tem a precisão do relógio atômico dos satélites, e esse erro de sincronismo entra na equação como uma **quarta incógnita**, resolvida simultaneamente com as três coordenadas espaciais. É por isso que as distâncias calculadas a partir do tempo de chegada do sinal são chamadas tecnicamente de **pseudodistâncias**, não distâncias exatas. "a" erra a dimensionalidade (o posicionamento é tridimensional); "c" e "d" não são o motivo real.
</details>

---

### 10. Dissertativa curta — `geologia-avancado-m13-q10` · oa01 · 10 pts

Um mapa geológico histórico foi georreferenciado com RMSE de 45 m, a partir de pontos de controle. Um colega afirma que esse valor é "alto demais, sempre inaceitável". Explique por que essa afirmação, sem mais informação, está incompleta — o que falta saber para julgar se 45 m é aceitável?

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:**

O RMSE não tem um limiar universal de aceitabilidade — ele precisa ser julgado **em relação à escala (e à precisão posicional) do dado-fonte original**. O critério normativo brasileiro é o **Padrão de Exatidão Cartográfica (PEC)**, do Decreto nº 89.817/1984: o RMSE se compara ao **erro-padrão** da classe (0,3 mm, 0,5 mm ou 0,6 mm na escala da carta, para as Classes A, B e C), não ao valor do próprio PEC (0,5 mm, 0,8 mm, 1,0 mm). Um mesmo RMSE de 45 m pode ser perfeitamente aceitável para uma carta-fonte em escala regional (1:100.000, onde 45 m correspondem a 0,45 mm, dentro do erro-padrão da Classe B) e completamente inaceitável para uma carta-fonte de detalhe (1:5.000, onde o mesmo erro corresponderia a 9 mm no papel). Falta, portanto, saber a **escala original do mapa-fonte** antes de julgar o RMSE — a afirmação do colega ignora essa dependência.
</details>

---

## Gabarito resumido

| Questão | ID | Resposta |
|---|---|---|
| 1 | q01 | b (Córrego Alegre = Hayford 1924; confundido com SAD69, que usa UGGI-67/GRS67) |
| 2 | q02 | Falso (ondulação geoidal no Brasil é da ordem de -30 a +30 m, MAPGEO2015) |
| 3 | q03 | H = h − N = 812,40 − (−18,60) = 831,00 m |
| 4 | q04 | b (adoção em 2005, exclusividade a partir de 2015) |
| 5 | q05 | ver comentário (mesmo número, datum diferente = local físico diferente; diferença de 60-70 m no Brasil) |
| 6 | q06 | c (contatos litológicos = vetor; concentração interpolada = raster) |
| 7 | q07 | Falso (célula fina sem dados que sustentem cria falsa impressão de precisão) |
| 8 | q08 | ver comentário (importação de tabela XY; geocodificação reservada para endereço) |
| 9 | q09 | b (quarta incógnita = erro do relógio do receptor; pseudodistância) |
| 10 | q10 | ver comentário (RMSE precisa ser comparado ao erro-padrão da classe do PEC, função da escala do dado-fonte) |
