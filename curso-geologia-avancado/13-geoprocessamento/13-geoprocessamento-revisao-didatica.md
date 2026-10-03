# Revisão didática: Módulo 13 — Geoprocessamento

**Revisado em:** 2026-09-08 · **Modo:** `review-and-fix`
**Material:** `13-geoprocessamento/` — 7 aulas (a01 a a07)
**Veredito:** **Bem ensinado com ressalvas** — 4 achados 🟠 e 3 🟡 corrigidos; 2 🔵 registrados como
sugestão, sem correção.

## Resumo

🔴 0 bloqueiam · 🟠 4 prejudicam · 🟡 3 atrito · 🔵 2 sugestões

**Carga estimada (após auditoria e revisão):**

| Aula | Palavras (corpo) | Conceitos novos | Diagramas | Exemplo trabalhado |
|---|---|---|---|---|
| a01 | 2.390 | ~10, mas em cadeia única (geoide → datum → coordenadas → projeção → escala) | 1 + tabela nova | numérico (escala) + conceitual (datum) |
| a02 | 2.000 | 5 | 1 | conceitual, 4 itens |
| a03 | 2.260 | 8 | 1 | numérico (PEC/escala) |
| a04 | 2.050 | 6 | 1 | numérico (buffer) + conceitual (interseção) |
| a05 | 2.210 | 6 | 1 | conceitual (escolha) + leitura de isolinhas (novo) |
| a06 | 2.460 | ~11 | 2 (1 novo) | numérico (limiar → área) |
| a07 | 2.310 | 7 | 1 | conceitual, 5 decisões |

**Nota sobre a métrica:** o campo `palavras_corpo` das sete aulas foi **recontado** por medição
direta após as edições de auditoria e de didática, substituindo a estimativa do gerador. Os
números acima não são, portanto, comparáveis um a um com os declarados nos módulos anteriores,
que seguem sendo estimativas. A comparação **interna ao módulo** é que vale, e ela mostra uma
dispersão de 23% entre a aula mais leve (a02) e a mais pesada (a06) — bem acima dos 4% do Módulo
12, mas dentro do que se espera de um módulo cuja primeira e última aulas são, por desenho,
fundação e consolidação.

**Padrão geral.** O módulo é pedagogicamente sólido e tem uma virtude que merece registro: ele
**declara os próprios pontos de armadilha em vez de escondê-los**. A a05 abre com uma seção
inteira chamada "O aviso mais importante desta aula", a a06 fecha a extração de lineamentos
dizendo em negrito que lineamento é hipótese e não confirmação, e a a07 encerra o módulo com a
frase de que o software produz mapa bonito independentemente da qualidade do dado. Nenhum
desses avisos é decorativo — cada um antecipa exatamente o erro que um autodidata cometeria
sozinho. Os achados abaixo são de acabamento e de calibragem, não de concepção.

---

## Achados

### 🟠 1. Um terço da a03 estava mapeado para um objetivo que não o cobre

**claim_id:** `DID-M13-A03-OBJETIVO-001`
**Tipo:** conteúdo órfão / objetivo mal atribuído
**Onde:** a03 · metadados `mapa_objetivo_secao`; seção "GPS e GNSS: como a posição em campo é medida"
**Problema:** a seção de GPS/GNSS — constelações, trilateração, DOP, modos de posicionamento e
suas precisões — estava mapeada para o **oa02**, cujo enunciado é "Distinguir as estruturas
vetorial e matricial e organizar bases de dados espaciais em ambiente SIG". O objetivo não tem
nenhuma relação com o conteúdo da seção. Na prática, isso deixava órfã a parte mais examinável
da a03: o gerador de questionários, que monta a cobertura a partir do mapa de objetivos, ou
ignoraria o tema, ou o cobraria sob um objetivo que a aula não ensina — o desalinhamento
aula–avaliação clássico, aqui pego antes de existir avaliação.
**Correção aplicada:** a seção foi remapeada para o **oa01**, ao qual se liga por dois fios que a
própria aula já explicita: o modo de posicionamento determina em que sistema de referência e com
que precisão posicional o dado nasce, e a seção seguinte encerra dizendo que a escolha do modo
"retoma diretamente a discussão de escala e resolução da Aula 01". O oa02 fica com "Aquisição
digital de dados em campo", que de fato trata de alinhar o formulário de campo ao esquema de
atributos da camada — isto é, de organizar a base de dados espacial. Uma nota no próprio arquivo
registra a decisão.
**Escopo:** correção local aplicada · **pendência curricular encaminhada ao orquestrador:** o
enunciado do oa01, no hub e no `course-state.yaml`, ganharia precisão se citasse também o método
de posicionamento (algo como "...e escolher o sistema de referência e o método de posicionamento
adequados a um projeto"). Reescrever um objetivo de aprendizagem é decisão curricular, fora do
escopo desta revisão — fica registrado para a próxima passagem do planejador.

### 🟠 2. O parágrafo de datum ficou denso demais depois da auditoria

**claim_id:** `DID-M13-A01-DENSIDADE-002`
**Tipo:** sobrecarga cognitiva
**Onde:** a01 · "Datum: o que fixa o modelo à Terra real"
**Problema:** achado **introduzido pela própria auditoria desta rodada**, e por isso registrado
com honestidade. Ao corrigir o elipsoide do SAD69, as datas do SIRGAS2000 e a relação estática/
dinâmica com o WGS84, o parágrafo passou a carregar quatro data, quatro elipsoides, duas
resoluções do IBGE, uma época de referência e uma taxa de movimento de placa — tudo em prosa
corrida. Cada informação está certa e é necessária; o problema é que a forma de apresentá-las
virou uma lista disfarçada de parágrafo, e o leitor de primeira viagem não tem onde ancorar.
Sobrecarga não se resolve com mais explicação, e sim com consolidação.
**Correção aplicada:** inserida, logo após o parágrafo, uma **tabela de quatro linhas** (Córrego
Alegre, SAD69, SIRGAS2000, WGS84) com elipsoide, se é geocêntrico e a situação no Brasil. Nenhum
fato novo — é destilação do que o parágrafo já dizia, na forma em que o leitor vai precisar
consultar na prática. A frase de introdução da tabela nomeia explicitamente por que ela existe
("São quatro nomes num parágrafo só, e vale consolidá-los antes de seguir").
**Escopo:** correção local.

### 🟠 3. A a05 promete construir e interpretar isolinhas, e o exemplo não fazia isso

**claim_id:** `DID-M13-A05-EXEMPLO-003`
**Tipo:** objetivo declarado sem demonstração / exemplo insuficiente
**Onde:** a05 · cabeçalho "Ao final você vai conseguir" vs. "Exemplo trabalhado"
**Problema:** o cabeçalho promete três resultados, e o exemplo trabalhado só entregava dois. O
terceiro — "construir e interpretar um mapa de isovalores (isolinhas) a partir de uma superfície
interpolada" — era ensinado numa seção conceitual sólida, mas nunca aplicado: o exemplo escolhia
entre IDW e krigagem e parava ali. É o mesmo defeito que o Módulo 12 teve na a02 e que o resto
daquele módulo não teve: as outras seis aulas do M13 mantêm a disciplina de um exemplo que
persegue o objetivo declarado até o fim.
**Correção aplicada:** o exemplo foi reestruturado em **(a)** e **(b)** sobre o mesmo cenário dos
15 poços. O item (b) apresenta três padrões de isolinha na mesma área — muito próximas, muito
espaçadas, e fechadas com valores crescentes — e pede a leitura de cada um. A resolução aplica
as regras que a seção "Construindo e lendo um mapa de isovalores" já dava, e amarra o item (b)
ao item (a): o trecho de isolinhas espaçadas cai justamente na parte pouco amostrada, e a
resolução mostra que ali a suavidade **é consequência do interpolador, não observação**. Nenhum
fato novo foi introduzido — só aplicação das regras já auditadas ao cenário já existente. O
fechamento do item explicita a lição: a mesma regra aplicada a duas regiões do mesmo mapa produz
uma conclusão confiável e uma vazia, e o que as separa é a densidade amostral.
**Escopo:** correção local.

### 🟠 4. A passagem mais difícil do módulo era a única sem apoio visual

**claim_id:** `DID-M13-A06-VISUAL-004`
**Tipo:** ausência de apoio no ponto de maior carga
**Onde:** a06 · "Análise hidrológica: direção e acumulação de fluxo"
**Problema:** essa seção encadeia cinco produtos raster derivados uns dos outros — preenchimento
de depressões, direção de fluxo, acumulação de fluxo, limiar/rede de drenagem e delimitação de
bacia — em dois parágrafos de prosa densa, sem nenhum apoio visual. É a única cadeia de
processamento com mais de três etapas do módulo inteiro, e era a única passagem difícil sem
diagrama: a a01 tem o corte elipsoide/geoide, a a02 o esquema vetor/raster, a a03 o par
pixel↔coordenada, a a04 os três overlays, a a05 os três interpoladores, a a06 as curvas
hipsométricas e a a07 o layout. Faltava exatamente onde mais fazia falta. Além disso, a estrutura
de dependência — o raster de direção de fluxo alimenta **duas** saídas diferentes — é
praticamente invisível em prosa.
**Correção aplicada:** inserido um diagrama esquemático da cadeia hidrológica, mostrando cada
etapa consumindo a saída da anterior e a bifurcação do raster de direção de fluxo em rede de
drenagem e delimitação de bacia. A legenda de fechamento acrescenta a leitura que o aluno deve
levar: só os dois últimos passos envolvem escolha do analista, e errar o preenchimento ou a
direção de fluxo contamina em silêncio tudo o que vem depois — reforço deliberado do fio
condutor do módulo.
**Escopo:** correção local.

### 🟡 5. Falso leste e falso norte citados sem definição

**claim_id:** `DID-M13-A01-FALSOLESTE-005`
**Tipo:** termo técnico usado antes de definido
**Onde:** a01 · "Sistemas de coordenadas: geográficas e planas (projetadas)"
**Problema:** "cada um com sua própria origem local de coordenadas (falso leste e falso norte,
para evitar coordenadas negativas)" dizia **para que servem** sem dizer **o que são**. O leitor
que nunca viu os termos sai sem saber que se trata de constantes somadas ao valor da coordenada —
e vai encontrá-los em toda ficha de sistema de referência que abrir.
**Correção aplicada:** oração aposta trocada por uma definição de uma linha: constantes somadas
às coordenadas para que nenhum ponto do fuso caia com valor negativo.
**Escopo:** correção local.

### 🟡 6. Pré-requisito declarado e não usado na a05

**claim_id:** `DID-M13-A05-PREREQ-006`
**Tipo:** pré-requisito declarado mas não usado
**Onde:** a05 · cabeçalho
**Problema:** a a05 declarava como pré-requisitos a a02 **e** a a04, mas justificava só a a02 (e
com razão: a interpolação converte vetor em raster). Nada no corpo da a05 usa overlay, buffer,
dissolve ou relação topológica. Pré-requisito inflado tem custo real em material autodidata: o
leitor que pulou a a04 acredita que precisa voltar e não precisa, e o leitor que não pulou
procura na a05 uma conexão que não existe.
**Correção aplicada:** a a04 saiu da lista de pré-requisitos e passou a ser mencionada como
posição na sequência do módulo, com a ressalva explícita de que nada ali depende dela.
**Escopo:** correção local.

### 🟡 7. Referência vaga a "outra aula" no exemplo da a07

**claim_id:** `DID-M13-A07-REFERENCIA-007`
**Tipo:** referência interna imprecisa
**Onde:** a07 · "Exemplo trabalhado", enunciado da situação
**Problema:** "(Aula 04, usado na operação de interseção com o buffer da falha em outra aula,
aqui reaproveitado como camada de contexto)" cita a Aula 04 e, na mesma frase, se refere a ela
como "outra aula", como se fossem duas. Numa aula de fechamento, cujo valor está justamente em
amarrar as seis anteriores, uma referência cruzada ambígua desfaz parte do trabalho.
**Correção aplicada:** reescrita para "a mesma camada do exemplo trabalhado da Aula 04, ali
cruzada com o buffer da falha e aqui reaproveitada apenas como camada de contexto".
**Escopo:** correção local.

### 🔵 8. O passo 3 do exemplo da a04 entrega o resultado pronto

**claim_id:** `DID-M13-A04-EXEMPLO-008`
**Tipo:** sugestão (exemplo com etapa não executada pelo leitor)
**Onde:** a04 · "Exemplo trabalhado", Passo 3
**Observação:** os passos 1 e 2 são executáveis pelo leitor (o buffer é calculado à mão como
checagem de sanidade, a interseção é escolhida com justificativa), mas o passo 3 introduz o
resultado com "Suponha que o SIG retorne (...) uma área de interseção de 1,35 km²". Não é
defeito: a área de uma interseção geométrica real não tem como ser calculada analiticamente a
partir dos dados do enunciado, e o texto é honesto ao declarar o valor como suposto. O que o
passo 3 de fato ensina — **qual dos três números reportar**, e por quê não são os 7,2 km² nem os
8,4 km² — é ensinado bem.
**Não corrigido.** Vira sugestão para o gerador de questionários: uma questão que apresente os
três números (7,2 / 8,4 / 1,35 km²) e pergunte qual reportar, com justificativa, cobre o
raciocínio central do exemplo sem exigir mudança na aula.

### 🔵 9. A a06 é a aula mais densa do módulo

**claim_id:** `DID-M13-A06-DENSIDADE-009`
**Tipo:** sugestão (densidade a monitorar)
**Onde:** a06, inteira
**Observação:** com ~2.460 palavras e cerca de onze itens (MDT/MDS, SRTM, declividade,
hipsometria, curva hipsométrica e estágios evolutivos, preenchimento de depressões, direção de
fluxo, acumulação, limiar, bacia, hillshade e lineamentos), a a06 é a mais pesada do módulo — e
o parágrafo do SRTM cresceu na auditoria desta rodada. Contra a heurística de "3 a 4 ideias
independentes por aula de 30 min", ela pareceria candidata a divisão. **Não é**, e por um motivo
específico: os onze itens não são independentes — todos são produtos derivados do mesmo objeto
(o MDE), por operações de vizinhança sobre a mesma grade, o que é exatamente o tipo de cadeia que
uma aula única ensina melhor que duas. O diagrama acrescentado pelo achado 4 reduz a carga da
parte mais pesada.
**Não corrigido.** Fica o registro: se o aluno reportar que a a06 pesou, o corte natural existe e
é limpo — morfometria (MDT/MDS, declividade, hipsometria) numa aula, hidrologia e lineamentos na
seguinte. Decisão do orquestrador, não desta revisão.

---

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo trabalhado | Observação |
|---|---|---|---|
| `oa01` — geoide, datum, coordenadas, projeções, escala; escolher o sistema de referência | a01 (todas as seções) · a03 ("O problema", "Georreferenciamento por pontos de controle", "GPS e GNSS") | sim (a01 numérico + conceitual; a03 numérico) | mapeamento da a03 corrigido pelo achado 1; enunciado do objetivo a rever pelo planejador |
| `oa02` — vetorial vs. matricial; organizar bases de dados espaciais | a02 (todas as seções) · a03 ("Aquisição digital de dados em campo") | sim (a02, 4 itens) | íntegro |
| `oa03` — operações vetoriais e interpolação; mapas de isovalores | a04 (todas) · a05 (todas) | sim (a04 numérico; a05 agora com leitura de isolinhas) | as duas metades do objetivo passaram a ter demonstração após o achado 3 |
| `oa04` — variáveis morfométricas e hidrológicas de MDE; produtos normatizados | a06 (todas) · a07 (todas) | sim (a06 numérico; a07 conceitual, 5 decisões) | íntegro |

Nenhum objetivo sem seção que o ensine. Nenhuma seção órfã após o achado 1.

**Cadeia de pré-requisitos:** a01 → a02 → a03 (a01+a02) → a04 (a02) → a05 (a02) → a06 (a02) →
a07 (todas). Cada aula nomeia o que consome da anterior. As a04, a05 e a06 dependem apenas da
a02 e podem, a rigor, ser lidas em qualquer ordem entre si — a sequência linear é de conveniência
narrativa, não de dependência, e a correção do achado 6 passou a dizer isso ao leitor em vez de
deixá-lo supor. O módulo não tem pré-requisito de outro módulo do curso.
**NENHUM SALTO DE PRÉ-REQUISITO.**

**Alinhamento com a avaliação:** não avaliável nesta rodada — o módulo ainda não tem questionário
nem baralho. As sugestões dos achados 1, 8 e 9 foram encaminhadas ao gerador de questionários.

---

## O que está bem feito

- **Os avisos de armadilha são o melhor traço do módulo.** A a05 dedica uma seção inteira, antes
  de qualquer método, a dizer que todo interpolador produz mapa convincente; a a06 fecha
  lineamentos com "hipótese, não confirmação" e lista as três origens alternativas (artefato de
  iluminação, controle litológico, feição antrópica); a a07 encerra o módulo dizendo que a
  responsabilidade pela correspondência entre aparência e validade é do analista. Material
  autodidata avançado precisa exatamente disso, e é raro.
- **O fio condutor escala/resolução/precisão atravessa as sete aulas sem repetir a explicação.**
  Aparece como escala na a01, como resolução de célula na a02, como RMSE contra escala do
  dado-fonte na a03, como coordenadas projetadas para cálculo de área na a04, como densidade
  amostral na a05, como resolução do MDE e limiar de acumulação na a06, e como escolha de escala
  para o A4 na a07. Cada retomada é uma encarnação nova do mesmo princípio, sempre nomeando de
  onde veio — é o oposto de redundância.
- **Todos os exemplos trabalhados terminam em interpretação, não em número.** O da a06 é o melhor
  do módulo: calcula a área do limiar, e então mostra que o mesmo limiar em outra resolução dá
  uma rede hidrologicamente diferente — o número serve ao argumento metodológico, não o
  contrário.
- **A a07 fecha o módulo reconstruindo o fluxo de trabalho aula por aula**, no mesmo padrão de
  encerramento que funcionou nos Módulos 11 e 12, e o exemplo trabalhado dela reaproveita as
  camadas dos exemplos anteriores em vez de inventar um cenário novo.
- **Nenhum termo central é usado antes de definido**, com a exceção corrigida no achado 5. A
  disciplina de definir por aposto na primeira ocorrência (GCP, RMSE, DOP, multi-caminho,
  variograma, hillshade, pour point, geodatabase) é consistente nas sete aulas.
- **A a05 nomeia a própria limitação do método recomendado.** Ao escolher krigagem, o texto diz
  explicitamente que não é por superioridade intrínseca, e sim porque aquele cenário específico
  torna a informação de incerteza valiosa. Ensinar critério de escolha em vez de ranking de
  métodos é o que separa material avançado de material introdutório.
