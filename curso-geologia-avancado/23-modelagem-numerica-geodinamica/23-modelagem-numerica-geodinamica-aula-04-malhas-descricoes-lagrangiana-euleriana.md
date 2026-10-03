# Aula 04: Malhas e descrições lagrangiana e euleriana — como o contínuo vira um modelo computável

**ID:** geologia-avancado-m23-a04
**Módulo:** [[23-modelagem-numerica-geodinamica-modulo|Módulo 23 — Introdução à modelagem numérica geodinâmica]]
**Duração estimada:** ~24 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** apresentar as escolhas de representação que transformam o meio contínuo da Aula 03 em algo que um computador resolve — a família de malha, a posição das variáveis dentro da célula (malha escalonada) e a descrição do movimento (lagrangiana ou euleriana) —, e justificar por que os códigos geodinâmicos modernos combinam as duas descrições.
**Ao final você vai conseguir:** distinguir malha estruturada de não estruturada e dizer quando cada uma se justifica; explicar o que é uma malha escalonada e qual problema numérico ela resolve; diferenciar a descrição lagrangiana da euleriana de um campo em movimento; e, dado um problema geodinâmico concreto, escolher a combinação de malha e descrição adequada, inclusive o método de partículas em célula.
**Pré-requisito:** [[23-modelagem-numerica-geodinamica-aula-03-mecanica-continuo-continuidade-stokes|Aula 03 deste módulo]] (equação da continuidade e equação de Stokes).

> [!note] Esta aula é a **Parte 2** de um par.
> A [[23-modelagem-numerica-geodinamica-aula-03-mecanica-continuo-continuidade-stokes|Aula 03 — Parte 1]] estabeleceu **o que** governa o movimento do meio contínuo: continuidade e Stokes. Esta aula trata de **como** representá-lo para um computador. As equações da Parte 1 são pressuposto direto daqui — se elas ainda não estiverem assentadas, volte antes de seguir.

## Conteúdo

### A malha: onde os valores moram

Resolver as equações da Aula 03 numericamente exige, como a Aula 02 introduziu, discretizar o domínio numa **malha**: um conjunto de pontos (ou células) onde os campos — velocidade, pressão, temperatura — são calculados. A primeira escolha é a **família** da malha, e há duas:

- **Malha estruturada** — os nós formam uma grade regular, e a vizinhança de cada nó é conhecida só pelos índices: o vizinho de `[i, j]` é `[i+1, j]`, sem consulta a tabela nenhuma. É mais simples de programar e mais eficiente computacionalmente, e é a que este módulo usa. Foi exatamente uma malha estruturada que `np.meshgrid` construiu na Aula 01.
- **Malha não estruturada** — os elementos têm forma e tamanho variáveis (triângulos, tetraedros) e podem se adensar onde o problema exige e se afrouxar onde não exige, adaptando-se a geometrias irregulares: uma superfície de falha curva, o contorno de um corpo intrusivo, a topografia real de uma cadeia. O preço é que a vizinhança de cada elemento precisa ser armazenada explicitamente, e todo o código fica mais pesado. Está fora do escopo deste módulo, mas é o que sustenta boa parte dos códigos de elementos finitos usados em produção.

### A malha escalonada: por que nem tudo mora no mesmo ponto

Decidida a família, resta uma escolha mais fina e menos óbvia: **dentro de cada célula, todas as variáveis moram no mesmo ponto?** A resposta ingênua é sim — uma malha **colocalizada**, em que pressão e as componentes de velocidade compartilham exatamente os mesmos nós. E essa resposta produz um defeito numérico clássico.

O problema é que, numa malha colocalizada, a discretização do gradiente de pressão por diferença central em um nó **pula o nó vizinho imediato** e enxerga apenas os nós alternados. A consequência é que um campo de pressão que oscile de nó em nó — alto, baixo, alto, baixo — fica **invisível** para a equação: ele não produz gradiente nenhum no cálculo, e portanto não é penalizado nem corrigido. O solver aceita essa oscilação em xadrez como solução legítima, e o resultado sai com um padrão de pressão que não tem nada de físico.

A solução padrão é a **malha escalonada** (*staggered grid*): pressão e componentes de velocidade são calculadas em pontos **deslocados** uns dos outros dentro da mesma célula — tipicamente a pressão no centro da célula e cada componente de velocidade no meio da face correspondente. Com esse arranjo, o gradiente de pressão entre dois centros vizinhos cai exatamente sobre o ponto de velocidade entre eles, de modo que nenhuma oscilação de nó em nó passa despercebida. É por isso que a malha escalonada é praticamente universal em códigos de fluxo de Stokes por diferenças finitas.

### Lagrangiano e euleriano: quem observa o quê

A malha diz **onde** os pontos ficam. Falta a escolha de **descrição** do movimento do meio contínuo — que é sobre *como o problema é observado*, não sobre a posição física dos pontos, e as duas coisas são independentes.

Na **descrição lagrangiana**, cada ponto de observação se move junto com o material — como amarrar um flutuador a uma porção específica de fluido e segui-lo ao longo do tempo, registrando como sua temperatura, composição e posição mudam. Na **descrição euleriana**, os pontos de observação ficam fixos no espaço, e o material passa por eles — como ficar parado numa ponte e registrar, a cada instante, o que está passando por baixo, sem seguir nenhuma porção específica de água.

> A analogia mais direta: um bote descendo um rio. Observá-lo do próprio bote, sentindo a correnteza mudar de velocidade à medida que ele se move, é a visão lagrangiana. Observá-lo de uma ponte fixa, vendo a água (e o bote, ao passar) fluir por um ponto que nunca muda de lugar, é a visão euleriana.
>
> Onde a analogia quebra: no rio o bote é um objeto distinto da água. Num modelo geodinâmico o "bote" é a própria rocha — não há observador separado do material, e a descrição lagrangiana é apenas uma escolha de contabilidade, não a presença de algo boiando.

Cada descrição tem uma vantagem natural, e elas são complementares:

- A **lagrangiana** acompanha diretamente a **história** de uma porção de material — útil para rastrear composição química, ou o caminho pressão-temperatura-tempo de uma rocha metamórfica, que a Aula 09 vai discutir.
- A **euleriana** é muito mais simples de discretizar numa malha fixa e nela resolver a equação de Stokes, porque a malha **não se distorce** à medida que o material se deforma. Uma malha lagrangiana pura, colada ao material, ficaria irremediavelmente torcida depois de poucos por cento de deformação — e num modelo que estica um continente por um fator 2, isso é fatal.

### Partículas em célula: o arranjo que os códigos usam de fato

Como cada descrição tem uma vantagem que a outra não tem, boa parte dos códigos modernos de modelagem geodinâmica (como os descritos por Gerya, ou pacotes de uso corrente como o ASPECT) **combina as duas**: resolve o campo de velocidade e pressão numa **malha euleriana fixa** — que nunca se distorce — e usa um conjunto de **marcadores lagrangianos**, partículas que se movem através dessa malha fixa carregando consigo propriedades como composição e história térmica, para rastrear o material.

Essa combinação chama-se **método de partículas em célula** (*particle-in-cell*). Cada passo de tempo faz o mesmo ciclo: a malha calcula a velocidade; a velocidade transporta as partículas; as partículas informam à malha qual é o material (e, portanto, a densidade e a viscosidade) em cada célula no instante seguinte. O método aparece de forma implícita nas aulas seguintes sempre que se falar em "acompanhar" uma unidade litosférica ao longo de um modelo.

## Exemplo trabalhado

**Situação 1 — construir as coordenadas escalonadas de uma malha 1D.** Dada uma malha de 5 nós de 0 a 4 (Δ = 1), onde ficam os pontos escalonados, deslocados de meia célula, e quantos são?

```python
import numpy as np

x = np.linspace(0, 4, 5)           # nos da malha: 0, 1, 2, 3, 4
x_meio = 0.5 * (x[:-1] + x[1:])    # pontos escalonados: meio de cada celula

print(x, x.size)
print(x_meio, x_meio.size)
```

**Conferindo à mão:** `x[:-1]` são os nós sem o último, `[0, 1, 2, 3]`; `x[1:]` são os nós sem o primeiro, `[1, 2, 3, 4]`. A média elemento a elemento dá `[0,5; 1,5; 2,5; 3,5]`. **Saída esperada:** `x = [0. 1. 2. 3. 4.]` com `x.size = 5`, e `x_meio = [0.5 1.5 2.5 3.5]` com `x_meio.size = 4`.

Repare na contagem, porque ela é a origem de metade dos erros de índice em código de malha escalonada: **uma malha de n nós tem n−1 centros de célula.** Numa formulação escalonada, a pressão vive nesses 4 centros e as componentes de velocidade nos 5 nós — dois arrays de tamanhos diferentes, deliberadamente. Quem tenta somá-los diretamente recebe um erro de forma do NumPy, e esse erro é um aliado: ele avisa que as duas grandezas não moram no mesmo lugar.

**Situação 2 — escolher malha e descrição para três problemas.** Para cada situação, decida a família de malha e a descrição, aplicando os critérios das seções acima.

*(a) Convecção térmica num caixa retangular de manto, geometria simples, deformação muito grande acumulada.* Malha **estruturada** (a geometria é um retângulo — não há nada de irregular a acomodar) e **euleriana**, com marcadores lagrangianos. A deformação acumulada é justamente o que proíbe a malha lagrangiana pura: ela se torceria até se tornar inutilizável muito antes do fim do modelo. Os marcadores fazem o trabalho de memória que a malha fixa não pode fazer.

*(b) Rastrear o caminho pressão-temperatura-tempo de uma porção de crosta durante uma colisão.* A pergunta é sobre a **história de uma porção específica de material** — é o que a descrição **lagrangiana** faz e a euleriana não faz. Na prática, isso é um marcador lagrangiano dentro de um modelo euleriano: a malha resolve a mecânica, e o marcador registra por onde aquela porção passou e a que temperatura.

*(c) Deformação em torno de uma superfície de falha curva, com necessidade de resolução fina só perto dela.* Aqui a geometria é irregular e a demanda de resolução é localizada: caso de malha **não estruturada**, que adensa elementos perto da falha e os afrouxa longe dela. É o único dos três que sai do escopo deste módulo — e é sintomático que seja também o único em que a geometria, e não a deformação, é o problema dominante.

## Recap relâmpago

- **Malha estruturada** (grade regular, vizinhança implícita nos índices — a deste módulo, a mesma que `np.meshgrid` constrói) versus **não estruturada** (elementos de forma e tamanho variáveis, adaptáveis a geometria irregular, ao custo de armazenar a vizinhança explicitamente).
- Numa malha **colocalizada** (tudo no mesmo nó), uma oscilação de pressão de nó em nó fica invisível para a diferença central do gradiente e passa como solução legítima — o padrão espúrio em xadrez. A **malha escalonada** (*staggered grid*) resolve isso pondo pressão no centro da célula e cada componente de velocidade no meio da face correspondente.
- Uma malha de **n nós tem n−1 centros de célula** — a contagem que produz a maior parte dos erros de índice em código escalonado.
- **Lagrangiano** = o ponto de observação se move com o material (registra a história de uma porção); **euleriano** = o ponto fica fixo e o material passa (a malha nunca se distorce). Analogia do bote no rio visto de bordo versus visto da ponte — com a ressalva de que, no modelo, o bote *é* a rocha.
- Códigos modernos combinam as duas: **malha euleriana fixa** para velocidade e pressão, **marcadores lagrangianos** para composição e história térmica. É o método de **partículas em célula** (*particle-in-cell*).

## Próxima aula

[[23-modelagem-numerica-geodinamica-aula-05-calor-fourier-conservacao-producao-adveccao|Aula 05 — Calor: lei de Fourier, conservação de calor, produção e advecção]] — a terceira EDP central do módulo, agora para o calor, e a grandeza que a Aula 08 vai mostrar ser a que mais importa para a viscosidade.

## Fontes

- Malha estruturada e não estruturada, malha escalonada (*staggered grid*), descrições lagrangiana e euleriana, e o método de partículas em célula (*particle-in-cell*) em códigos de modelagem geodinâmica: Gerya, T., *Introduction to Numerical Geodynamic Modelling*, 2ª ed. (2019), Cambridge University Press, capítulos sobre discretização e sobre advecção.
- Oscilação espúria de pressão em malha colocalizada e sua supressão por escalonamento das variáveis: Gerya, T., *Introduction to Numerical Geodynamic Modelling*, 2ª ed. (2019), capítulo sobre discretização da equação de Stokes; Patankar, S. V., *Numerical Heat Transfer and Fluid Flow* (1980), Hemisphere, capítulo sobre o campo de pressão em malha colocalizada.
- Código euleriano com marcadores lagrangianos como arquitetura de uso corrente: Kronbichler, M., Heister, T. & Bangerth, W. (2012), "High accuracy mantle convection simulation through modern numerical methods", *Geophysical Journal International*, 191(1), 12-29 (o código ASPECT).

<!--
nivel: avancado
palavras_corpo: 2036
mapa_objetivo_secao:
  geologia-avancado-m23-oa02: "A malha: onde os valores moram" + "A malha escalonada: por que nem tudo mora no mesmo ponto" + "Lagrangiano e euleriano: quem observa o quê" + "Partículas em célula: o arranjo que os códigos usam de fato" + "Exemplo trabalhado"

divisao_de_aula: 'Esta aula e a PARTE 2 da antiga Aula 03 unica (Mecanica do continuo: equacao da continuidade e equacao de Navier-Stokes; malhas e descricoes lagrangiana e euleriana; 2.622 palavras apos as correcoes da auditoria cientifica de 2026-09-19, ~31 min reais contra 29 declarados, 14 conceitos novos), dividida em 2026-09-19 pela revisao didatica (achado DID-M23-A03-CARGA-002), seguindo a convencao dos Modulos 17, 19, 20, 21 e 22 deste curso. A PARTE 1 e a Aula 03 (continuidade e Stokes). CORTE ESCOLHIDO: entre a FISICA DO CONTINUO (Parte 1) e a REPRESENTACAO NUMERICA (esta aula). O texto de origem desta metade era UMA UNICA SECAO de quatro paragrafos, em que tres familias de malha, a patologia da pressao colocalizada, duas descricoes de movimento e o metodo de particulas em celula estavam empilhados - o primeiro paragrafo sozinho era um periodo de mais de 100 palavras com tres definicoes dentro. A divisao deu a cada um desses blocos uma secao propria com espaco para ser explicado. NENHUMA correcao da auditoria cientifica foi desfeita: nenhum dos 15 achados de 2026-09-19 tocava este texto.'

exemplo_trabalhado_novo: 'O exemplo trabalhado desta aula foi CRIADO na divisao de 2026-09-19, porque o exemplo original da antiga Aula 03 (verificacao do divergente de um campo de cisalhamento puro) e inteiramente sobre a equacao da continuidade e ficou, PALAVRA POR PALAVRA e com as quatro correcoes da auditoria que o tocavam, na Parte 1. A SITUACAO 1 e aritmetica pura e verificavel: x_meio = 0.5*(x[:-1] + x[1:]) para x = linspace(0,4,5) da [0.5, 1.5, 2.5, 3.5], e uma malha de n nos tem n-1 centros de celula - conferido por execucao. A SITUACAO 2 NAO CONTEM NENHUMA ALEGACAO FACTUAL NOVA: e a aplicacao classificatoria, sem qualquer valor numerico, dos criterios ja enunciados no corpo e ja auditados em LAGRANGE-EULER-003 e MALHA-ESCALONADA-004 (malha estruturada para geometria simples; nao estruturada para geometria irregular com resolucao localizada; euleriana com marcadores quando a deformacao acumulada e grande; lagrangiana quando a pergunta e sobre a historia de uma porcao de material). Cada um dos tres casos reproduz um criterio ja presente no corpo, reorganizado em formato situacao-decisao-justificativa. Nenhuma fonte nova foi consultada para constru-lo.'

nota_alegacoes_migradas: 'As alegacoes GEODIN-M23-A03-LAGRANGE-EULER-003 e GEODIN-M23-A03-MALHA-ESCALONADA-004 acompanharam para ca o texto correspondente, na divisao de 2026-09-19. Os claim_id foram DELIBERADAMENTE MANTIDOS com o prefixo A03, que designa a aula pre-divisao, para nao quebrar a rastreabilidade com o manifesto 23-modelagem-numerica-geodinamica-auditoria.json, que os referencia. NAO RENUMERAR, apesar de esta ser agora a Aula 04.'

nota_passagem_pontual: 'PASSAGEM PONTUAL DO AUDITOR-CIENTIFICO em 2026-09-20 sobre MALHA-COLOCALIZADA-010 e EXEMPLO-ESCALONADA-011. RESULTADO: nenhuma correcao necessaria - ambas registradas como itens azuis P4 e P5 da passagem pontual. MALHA-COLOCALIZADA-010 foi verificada contra fonte e o mecanismo confere nas tres partes (o estencil [-1 0 +1] aniquila a oscilacao de no em no; o solver aceita o xadrez como solucao legitima; a malha escalonada acopla a velocidade da face a um gradiente compacto entre centros diretamente vizinhos). EXEMPLO-ESCALONADA-011 foi re-executada e bate digito a digito. Registrada apenas uma ressalva de ATRIBUICAO que nao contradiz o texto da aula: a malha escalonada vem do metodo MAC de Harlow & Welch (1965), popularizada por Patankar & Spalding (1972); a aula nao reivindica autoria para Patankar (1980), cita-o como a exposicao de referencia do problema - o que esta correto e nao exigiu edicao. NENHUMA LINHA DA AULA FOI ALTERADA. Nenhum dos 15 achados da auditoria de 2026-09-19 foi reaberto.'

nota_ao_auditor: 'RESOLVIDAS EM 2026-09-20 - ver nota_passagem_pontual acima. Registro historico do que estava pendente: DUAS ALEGACOES NOVAS nasceram nesta divisao e NAO passaram pela auditoria cientifica de 2026-09-19, que e anterior a elas: MALHA-COLOCALIZADA-010 (o mecanismo pelo qual a oscilacao de pressao de no em no fica invisivel para a diferenca central numa malha colocalizada - o corpo original afirmava que a malha escalonada evita o problema, ja auditado, mas NAO explicava o mecanismo, que foi acrescentado aqui pela revisao didatica) e EXEMPLO-ESCALONADA-011 (aritmetica dos pontos escalonados, verificada por execucao). Sinalizadas para checagem pontual pelo auditor-cientifico, como foi feito nos Modulos 17, 18, 19, 20 e 22.'

alegacoes_auditaveis:
  - claim_id: GEODIN-M23-A03-LAGRANGE-EULER-003
    claim: "Na descricao lagrangiana de um meio em movimento, os pontos de observacao se movem junto com o material; na descricao euleriana, os pontos de observacao permanecem fixos no espaco e o material passa por eles. Codigos modernos de modelagem geodinamica frequentemente combinam as duas, resolvendo velocidade e pressao em uma malha euleriana fixa e usando marcadores lagrangianos (particulas) para rastrear propriedades do material, no metodo conhecido como particle-in-cell."
    risk: fato
    source: "Gerya, T., Introduction to Numerical Geodynamic Modelling, 2a ed. (2019), Cambridge University Press, capitulos sobre discretizacao e advecção."
  - claim_id: GEODIN-M23-A03-MALHA-ESCALONADA-004
    claim: "A malha escalonada (staggered grid), em que pressao e componentes de velocidade sao calculadas em pontos deslocados dentro da mesma celula, e uma tecnica usada em codigos de fluxo de Stokes para evitar oscilacoes espurias de pressao que ocorrem quando todas as variaveis compartilham os mesmos nos de uma malha colocalizada."
    risk: fato
    source: "Gerya, T., Introduction to Numerical Geodynamic Modelling, 2a ed. (2019), Cambridge University Press, capitulo sobre discretizacao da equacao de Stokes."
  - claim_id: GEODIN-M23-A03-MALHA-COLOCALIZADA-010
    claim: "Numa malha colocalizada, a discretizacao do gradiente de pressao por diferenca central em um no usa os nos alternados e pula o vizinho imediato, de modo que um campo de pressao que oscila de no em no nao produz gradiente no calculo e e aceito pelo solver como solucao legitima - o padrao espurio em xadrez. Na malha escalonada, com pressao no centro da celula e componentes de velocidade no meio das faces, o gradiente entre dois centros vizinhos cai sobre o ponto de velocidade entre eles, e nenhuma oscilacao de no em no passa despercebida."
    risk: fato
    source: "Gerya, T., Introduction to Numerical Geodynamic Modelling, 2a ed. (2019), Cambridge University Press (edicao e ano confirmados; o indice do volume registra as entradas 'staggered grid' e 'Stokes equation'), capitulo sobre discretizacao da equacao de Stokes; Patankar, S. V., Numerical Heat Transfer and Fluid Flow (1980), Hemisphere, capitulo sobre o campo de pressao em malha colocalizada. VERIFICADA CONTRA FONTE na passagem pontual de 2026-09-20 e CONFIRMADA em cada uma das tres partes do mecanismo: (i) o operador de diferenca simetrica, de estencil [-1 0 +1], ANIQUILA um campo de pressao que alterna de no em no, porque os dois vizinhos usados no calculo tem o mesmo valor e a diferenca da zero - a oscilacao nao produz gradiente e portanto nao e penalizada; (ii) o solver aceita esse campo como solucao estacionaria legitima, e o resultado e o padrao espurio em xadrez, de comprimento de onda igual a duas celulas; (iii) o remedio proposto por Patankar e Spalding e armazenar pressao e velocidade em malhas deslocadas, de modo que as velocidades nas faces da celula fiquem acopladas a um gradiente de estencil compacto entre centros de celula DIRETAMENTE vizinhos - que e exatamente a formulacao da aula. Literatura de CFD contemporanea consultada para a confirmacao independente do mecanismo e da atribuicao a Patankar. RESSALVA DE ATRIBUICAO, nao contradiz a aula: a malha escalonada NAO foi inventada por Patankar (1980) - ela vem do metodo MAC de Harlow & Welch (1965), e Patankar & Spalding (1972) a popularizaram; a aula nao afirma autoria, cita Patankar (1980) apenas como a exposicao de referencia do problema da malha colocalizada, o que esta correto."
  - claim_id: GEODIN-M23-A03-EXEMPLO-ESCALONADA-011
    claim: "Para x = np.linspace(0, 4, 5), os pontos escalonados x_meio = 0.5*(x[:-1] + x[1:]) valem [0.5, 1.5, 2.5, 3.5], e uma malha de n nos tem exatamente n-1 centros de celula."
    risk: calculo
    source: "Calculo aritmetico direto reproduzivel a partir do codigo apresentado na aula, conferido por execucao (numpy 2.5.1). RE-EXECUTADA E CONFIRMADA na passagem pontual de 2026-09-20: x = [0. 1. 2. 3. 4.] com x.size = 5 e x_meio = [0.5 1.5 2.5 3.5] com x_meio.size = 4, batendo com a saida declarada; a conferencia a mao do texto tambem confere (x[:-1] = [0. 1. 2. 3.] e x[1:] = [1. 2. 3. 4.]). A generalizacao 'uma malha de n nos tem n-1 centros de celula' foi verificada exaustivamente para n de 2 a 59."
-->
