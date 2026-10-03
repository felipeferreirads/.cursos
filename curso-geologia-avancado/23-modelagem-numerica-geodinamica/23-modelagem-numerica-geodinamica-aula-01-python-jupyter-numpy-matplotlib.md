# Aula 01: Python para geodinâmica computacional — Jupyter, NumPy e Matplotlib; o que é e para que serve a modelagem numérica

**ID:** geologia-avancado-m23-a01
**Módulo:** [[23-modelagem-numerica-geodinamica-modulo|Módulo 23 — Introdução à modelagem numérica geodinâmica]]
**Duração estimada:** ~26 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** apresentar o que é modelagem numérica em geodinâmica e por que ela é necessária, e programar em Python as operações numéricas e gráficas básicas — com NumPy e Matplotlib, em ambiente Jupyter — que sustentam todas as aulas seguintes deste módulo.
**Ao final você vai conseguir:** explicar por que processos geodinâmicos reais em geral não têm solução analítica fechada e exigem solução numérica; criar e manipular arrays do NumPy de forma vetorizada, sem laços `for` explícitos; construir uma malha bidimensional com `meshgrid`; e produzir um gráfico de linha e um mapa de cores com Matplotlib.
**Pré-requisito:** nenhum dentro deste módulo. Pressupõe familiaridade mínima com sintaxe Python (variáveis, funções, listas) — se você nunca programou em Python, vale uma introdução rápida à linguagem antes desta aula, fora do escopo deste curso.

## Conteúdo

### Por que geodinâmica precisa de modelagem numérica

Boa parte da geologia estrutural, da estratigrafia e da petrologia deste curso descreve processos que se resolvem com raciocínio geométrico, classificação e, no máximo, uma fórmula fechada — um ângulo de mergulho, uma razão isotópica, um volume de corpo mineralizado. A geodinâmica trabalha com outro tipo de problema: como a temperatura evolui dentro de uma litosfera que esfria por milhões de anos enquanto produz calor radiogênico internamente; como o manto flui sob tensões que variam com a própria temperatura, que por sua vez depende do fluxo. Esses processos são descritos por **equações diferenciais** — equações que relacionam uma grandeza à sua taxa de variação no espaço e no tempo — e, fora de um punhado de casos muito simplificados (uma geoterma linear sem produção de calor, por exemplo), essas equações **não têm solução analítica fechada**: não existe uma fórmula que dê a resposta diretamente substituindo números.

Quando isso acontece, a única saída é a **solução numérica**: aproximar a equação contínua por um conjunto finito de pontos e operações aritméticas que um computador executa repetidamente até convergir para uma resposta suficientemente próxima da real. É esse o fio condutor deste módulo — as próximas oito aulas constroem, peça por peça, os ingredientes físicos (calor, mecânica do contínuo, reologia) e numéricos (equações diferenciais parciais, esquemas explícito e implícito) necessários para resolver numericamente problemas reais de geodinâmica. Esta aula prepara a ferramenta que todas as outras vão usar: Python, com as bibliotecas NumPy (cálculo numérico com arrays) e Matplotlib (visualização), rodando em um ambiente Jupyter.

### Jupyter: o caderno de trabalho da geociência computacional

Um **Jupyter Notebook** é um documento interativo dividido em células que podem conter código executável ou texto explicativo (Markdown), executadas de forma independente e em qualquer ordem — o que permite testar um pedaço de cálculo, ver o resultado imediatamente (um número, um gráfico, uma tabela) e ajustar o código sem reexecutar o programa inteiro do zero. Essa interatividade é o motivo pelo qual o Jupyter (originado do projeto IPython e hoje mantido pelo Project Jupyter) se tornou o ambiente padrão de geociência computacional, ciência de dados e ensino de métodos numéricos: o ciclo "escrever código → ver resultado → ajustar" fica muito mais curto do que escrever um programa completo e só ver o resultado no final. Ao longo deste módulo, todo código é apresentado como se estivesse em células de um notebook — um bloco de código por vez, com a saída esperada descrita logo em seguida.

### NumPy: arrays e operações vetorizadas

Python puro representa uma sequência de números como uma **lista**, e uma lista não sabe fazer aritmética elemento a elemento — somar duas listas com `+` as concatena, não soma seus valores. O **NumPy** (Numerical Python) resolve isso com o **array**: uma estrutura de dados especializada em guardar números do mesmo tipo, em que operações aritméticas (`+`, `-`, `*`, `/`, potência) se aplicam automaticamente a cada elemento — a chamada **vetorização**. Isso importa por dois motivos. O primeiro é de legibilidade: escrever `T = T0 + gradiente * z` para um array `z` inteiro é mais direto do que escrever um laço `for` percorrendo cada profundidade uma por uma. O segundo é de desempenho: por baixo dos panos, o NumPy delega essas operações a rotinas compiladas (escritas em C), muito mais rápidas do que um laço `for` interpretado do Python puro — uma diferença que se torna decisiva quando a malha de um modelo geodinâmico tem milhares ou milhões de pontos, como as aulas seguintes vão ter.

As funções mais usadas neste módulo para *criar* arrays são: `np.linspace(início, fim, n)`, que gera `n` valores igualmente espaçados entre início e fim (inclusive as pontas) — ideal para construir um eixo de profundidade ou de tempo; `np.arange(início, fim, passo)`, que gera valores com um passo fixo; `np.zeros(n)` e `np.ones(n)`, que criam arrays preenchidos de zeros ou uns, úteis para inicializar um campo antes de preenchê-lo num laço de tempo; e `np.meshgrid(x, z)`, que combina dois arrays 1D num par de arrays 2D representando as coordenadas de cada ponto de uma malha retangular — a base de qualquer modelo em duas dimensões espaciais, que vai reaparecer a partir da Aula 03.

### Matplotlib: visualizar o resultado

Um número isolado raramente convence tanto quanto uma curva ou um mapa. O **Matplotlib** é a biblioteca de visualização padrão do ecossistema científico Python. As duas funções mais usadas neste módulo são `plt.plot(x, y)`, que desenha uma curva ligando pares de pontos — perfeita para uma geoterma (temperatura por profundidade) ou uma curva de resfriamento (temperatura por tempo) —, e `plt.imshow(campo)` (ou `plt.contourf`), que exibe uma matriz 2D como um mapa de cores — a forma natural de visualizar um campo de temperatura ou de velocidade calculado sobre uma malha bidimensional, como as Aulas 03 a 07 vão produzir. Um gráfico bem rotulado (eixos com unidade, uma barra de cor com escala) não é enfeite: é o que permite verificar, num relance, se um resultado numérico faz sentido físico — uma geoterma que esfria com a profundidade, por exemplo, denuncia um erro de sinal antes mesmo de olhar os números.

## Exemplo trabalhado

**Situação 1 — uma geoterma linear ilustrativa, vetorizada.** Construa, sem usar nenhum laço `for`, um array de profundidades de 0 a 40 km com 5 pontos, e a temperatura correspondente supondo uma temperatura de superfície de 10 °C e um gradiente geotérmico constante de 25 °C/km (um valor ilustrativo, deliberadamente simplificado — a Aula 07 vai construir geotermas reais, não lineares).

```python
import numpy as np
import matplotlib.pyplot as plt

z = np.linspace(0, 40, 5)      # profundidade, km: 5 pontos de 0 a 40
T = 10 + 25 * z                # geoterma linear ilustrativa, °C

print(z)
print(T)

plt.plot(T, z)                 # temperatura no eixo x, profundidade no eixo y
plt.gca().invert_yaxis()       # profundidade cresce para BAIXO
plt.xlabel("Temperatura (°C)")
plt.ylabel("Profundidade (km)")
plt.show()
```

**Saída esperada:** `z = [ 0. 10. 20. 30. 40.]` e `T = [ 10. 260. 510. 760. 1010.]`. Conferindo à mão o terceiro ponto (z = 20 km): T = 10 + 25 × 20 = 10 + 500 = 510 °C — bate com a saída. A operação `10 + 25 * z` foi aplicada de uma só vez aos cinco elementos do array, sem nenhum laço explícito — é isso que "vetorizado" quer dizer na prática.

As quatro últimas linhas produzem o **gráfico de linha**: `plt.plot(T, z)` desenha a curva, e as três seguintes são o que separa um gráfico legível de um rabisco. Repare especialmente em `invert_yaxis()`: uma geoterma se lê com a profundidade crescendo **para baixo**, ao contrário do padrão do Matplotlib, e esquecer essa linha produz uma figura que parece certa e está de cabeça para baixo. É o primeiro exemplo concreto da observação feita acima — o gráfico é o instrumento de conferência, e um gráfico mal rotulado não confere nada. (Os valores de temperatura acima de mil graus a 40 km só aparecem porque o gradiente foi mantido constante por toda a profundidade de propósito, para deixar a aritmética simples; nenhuma litosfera real tem um gradiente linear tão íngreme mantido até essa profundidade — a Aula 07 mostra por quê.)

**Situação 2 — uma malha 2D com `meshgrid`.** Construa uma malha retangular de 4 pontos em x (horizontal, 0 a 3) por 3 pontos em z (profundidade, 0 a 2), e calcule em cada ponto da malha o campo `f = x - z`.

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 3, 4)          # 4 pontos: 0, 1, 2, 3
z = np.linspace(0, 2, 3)          # 3 pontos: 0, 1, 2
X, Z = np.meshgrid(x, z)          # X e Z: matrizes 3x4 (linhas=z, colunas=x)
F = X - Z

print(X.shape, F)

plt.imshow(F, origin="upper")     # a matriz 2D como mapa de cores
plt.colorbar(label="F = x - z")   # a escala, sem a qual as cores nao dizem nada
plt.xlabel("indice em x")
plt.ylabel("indice em z (profundidade)")
plt.show()
```

**Saída esperada:** `X.shape` é `(3, 4)` — 3 linhas (uma por valor de z) e 4 colunas (uma por valor de x), porque `meshgrid` replica cada array 1D ao longo da outra dimensão para formar a malha completa. Na linha z = 0, `F` reproduz `x` inteiro: `[0, 1, 2, 3]`; na linha z = 2, cada valor cai 2 unidades: `[-2, -1, 0, 1]`. Conferindo o ponto (x=2, z=1): F = 2 − 1 = 1, que aparece na segunda linha, terceira coluna da matriz `F` — confirmando que `X` e `Z` de fato carregam a coordenada de cada ponto da malha, não uma lista solta de valores. Esse par `(X, Z)` é exatamente o tipo de malha que as Aulas 03 a 09 vão usar para representar um domínio geológico bidimensional (uma seção vertical da litosfera, por exemplo) e calcular campos de temperatura, velocidade ou tensão em cada ponto dele.

As cinco últimas linhas produzem o **mapa de cores**: `plt.imshow(F)` pinta cada elemento da matriz 3×4 com a cor correspondente ao seu valor, e `plt.colorbar` acrescenta a escala — sem ela, as cores são bonitas e mudas. O argumento `origin="upper"` põe a primeira linha da matriz no topo da figura, que é o que se quer quando o índice de linha é profundidade: linha 0 é a superfície. Aqui o campo `F = x − z` é simples o bastante para você prever o resultado antes de rodar — o canto superior direito (x alto, z baixo) é o valor máximo, 3; o canto inferior esquerdo (x baixo, z alto) é o mínimo, −2 —, e é exatamente por isso que ele serve de teste: **quando o gráfico contradiz a previsão que você fez de cabeça, o erro está no código, não na sua cabeça.** Esse é o hábito que as aulas seguintes vão cobrar a cada campo calculado.

## Recap relâmpago

- Processos geodinâmicos reais são descritos por equações diferenciais sem solução analítica fechada na maioria dos casos — daí a necessidade de resolvê-los numericamente, o fio condutor deste módulo.
- **Jupyter Notebook** organiza código em células executáveis independentemente, com resultado imediato — o ambiente padrão de trabalho em geociência computacional.
- **NumPy** representa sequências numéricas como **arrays**, sobre os quais operações aritméticas são **vetorizadas** (aplicadas a todos os elementos de uma vez, sem laço `for` explícito) — mais legível e muito mais rápido que Python puro para malhas grandes.
- `np.linspace`, `np.arange`, `np.zeros`/`np.ones` criam arrays 1D; `np.meshgrid` combina dois arrays 1D numa malha 2D de coordenadas, a base de qualquer modelo espacial deste módulo.
- **Matplotlib** (`plt.plot` para curvas, `plt.imshow`/`plt.contourf` para campos 2D) é a ferramenta de visualização usada para verificar, visualmente, se um resultado numérico faz sentido físico. Dois hábitos a levar: **inverter o eixo vertical** num gráfico de profundidade (`invert_yaxis`) e **sempre pôr a barra de cor com rótulo** num mapa de campo — e, acima de tudo, prever o resultado antes de olhar a figura, porque é a discordância entre previsão e figura que denuncia o erro.

## Próxima aula

[[23-modelagem-numerica-geodinamica-aula-02-algebra-linear-calculo-edp-diferencas-finitas|Aula 02 — Álgebra linear, cálculo e equações diferenciais parciais: solução analítica versus numérica e o método das diferenças finitas]] — o primeiro contato com equações diferenciais parciais e com a discretização que o restante do módulo usa, apoiado no cálculo numérico já visto no Módulo 30 do curso base.

## Fontes

- NumPy como biblioteca padrão de computação com arrays em Python científico, incluindo o mecanismo de vetorização: Harris, C. R. et al. (2020), "Array programming with NumPy", *Nature*, 585, 357-362, DOI 10.1038/s41586-020-2649-2; documentação oficial NumPy (numpy.org).
- Matplotlib como biblioteca padrão de visualização científica em Python: Hunter, J. D. (2007), "Matplotlib: A 2D graphics environment", *Computing in Science & Engineering*, 9(3), 90-95, DOI 10.1109/MCSE.2007.55.
- Jupyter Notebook como ambiente interativo padrão de ciência computacional, originado do projeto IPython: Kluyver, T. et al. (2016), "Jupyter Notebooks — a publishing format for reproducible computational workflows", em *Positioning and Power in Academic Publishing*, IOS Press, 87-90; documentação oficial do Project Jupyter (jupyter.org).

<!--
nivel: avancado
palavras_corpo: 2173
mapa_objetivo_secao:
  geologia-avancado-m23-oa01: "Por que geodinâmica precisa de modelagem numérica" + "Jupyter: o caderno de trabalho da geociência computacional" + "NumPy: arrays e operações vetorizadas" + "Matplotlib: visualizar o resultado" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEODIN-M23-A01-NUMPY-VETORIZACAO-001
    claim: "O NumPy representa sequencias numericas como arrays sobre os quais operacoes aritmeticas sao aplicadas elemento a elemento (vetorizadas) delegando a execucao a rotinas compiladas, o que e mais rapido que um laco for interpretado em Python puro para arrays grandes."
    risk: fato
    source: "Harris, C. R. et al. (2020), 'Array programming with NumPy', Nature, 585, 357-362, DOI 10.1038/s41586-020-2649-2; documentacao oficial NumPy (numpy.org)."
  - claim_id: GEODIN-M23-A01-MESHGRID-002
    claim: "np.meshgrid combina dois arrays 1D em um par de arrays 2D que representam as coordenadas de cada ponto de uma malha retangular, com a forma (numero de pontos do segundo array, numero de pontos do primeiro array) por padrao."
    risk: fato
    source: "Documentacao oficial NumPy, funcao numpy.meshgrid (numpy.org/doc)."
  - claim_id: GEODIN-M23-A01-JUPYTER-003
    claim: "Jupyter Notebook e um documento interativo dividido em celulas de codigo ou texto Markdown, executaveis independentemente, originado do projeto IPython e mantido pelo Project Jupyter, e e amplamente adotado como ambiente de geociencia computacional e ciencia de dados."
    risk: fato
    source: "Kluyver, T. et al. (2016), 'Jupyter Notebooks — a publishing format for reproducible computational workflows', em Positioning and Power in Academic Publishing, IOS Press, 87-90; documentacao oficial do Project Jupyter (jupyter.org)."
  - claim_id: GEODIN-M23-A01-MATPLOTLIB-004
    claim: "Matplotlib e a biblioteca padrao de visualizacao grafica do ecossistema cientifico Python, oferecendo plt.plot para curvas 2D e plt.imshow/plt.contourf para exibir campos bidimensionais como mapas de cor."
    risk: fato
    source: "Hunter, J. D. (2007), 'Matplotlib: A 2D graphics environment', Computing in Science & Engineering, 9(3), 90-95, DOI 10.1109/MCSE.2007.55."
  - claim_id: GEODIN-M23-A01-EXEMPLO-GEOTERMA-005
    claim: "Para z = np.linspace(0, 40, 5) e T = 10 + 25*z, o array resultante e T = [10, 260, 510, 760, 1010] graus Celsius, conferido em z=20 km: T = 10 + 25*20 = 510."
    risk: calculo
    source: "Calculo aritmetico direto reproduzivel a partir do codigo apresentado na aula."
  - claim_id: GEODIN-M23-A01-MATPLOTLIB-API-006
    claim: "plt.plot(x, y) desenha uma curva; plt.gca().invert_yaxis() inverte o eixo vertical, necessario para que a profundidade cresca para baixo num grafico de geoterma; plt.imshow(matriz, origin='upper') exibe uma matriz 2D como mapa de cores com a primeira linha no topo da figura; e plt.colorbar aceita o argumento label para rotular a escala de cor."
    risk: fato
    source: "Documentacao oficial Matplotlib: pyplot.plot, pyplot.imshow (parametro origin, valores 'upper' e 'lower') e pyplot.colorbar (parametro label), consultada em 2026-09-19. CONFIRMADA POR EXECUCAO na passagem pontual de 2026-09-20 (Matplotlib 3.11.2 instalado no ambiente, backend Agg, NumPy 2.5.1): os dois blocos de codigo da aula rodam sem erro nem aviso de depreciacao; plt.gca().invert_yaxis() produz ylim = (42.0, -2.0), isto e, eixo vertical decrescente para cima, com a profundidade crescendo para baixo; plt.imshow(F, origin='upper') produz extent = [-0.5, 3.5, 2.5, -0.5] e ylim = (2.5, -0.5), colocando a linha 0 da matriz no topo da figura; e plt.colorbar(label=...) aceita o argumento e grava o rotulo no eixo da barra ('F = x - z', lido de volta do objeto)."
  - claim_id: GEODIN-M23-A01-EXEMPLO-MAPA-007
    claim: "Para o campo F = X - Z sobre a malha x = [0,1,2,3] e z = [0,1,2], o valor maximo e 3, no canto de x alto e z baixo (linha 0, coluna 3), e o minimo e -2, no canto de x baixo e z alto (linha 2, coluna 0); com origin='upper' esses cantos aparecem, respectivamente, no topo a direita e na base a esquerda da figura."
    risk: calculo
    source: "Calculo aritmetico direto a partir do codigo da aula (F = X - Z ja verificado por execucao na auditoria de 2026-09-19, item azul B5) combinado com a convencao origin='upper' da documentacao oficial Matplotlib. FIGURA CONFERIDA POR EXECUCAO na passagem pontual de 2026-09-20: F = [[0,1,2,3],[-1,0,1,2],[-2,-1,0,1]]; argmax = (linha 0, coluna 3) com valor 3.0 e argmin = (linha 2, coluna 0) com valor -2.0, batendo com os extremos declarados no texto; a barra de cor cobre exatamente clim = (-2.0, 3.0). Posicao na figura confirmada transformando as coordenadas de dados em coordenadas de tela: o maximo cai em (x=427.2, y=360.8) e o minimo em (x=129.6, y=114.4), isto e, o maximo esta mais a DIREITA e mais ALTO que o minimo - canto superior direito e canto inferior esquerdo, como o texto afirma."

nota_passagem_pontual: 'PASSAGEM PONTUAL DO AUDITOR-CIENTIFICO em 2026-09-20 sobre MATPLOTLIB-API-006 e EXEMPLO-MAPA-007, as duas alegacoes que a revisao didatica de 2026-09-19 deixara pendentes por falta de Matplotlib no ambiente. O Matplotlib foi INSTALADO (3.11.2) e os DOIS blocos de codigo da aula foram EXECUTADOS na integra. RESULTADO: nenhuma correcao necessaria - ambas registradas como itens azuis P2 e P3 da passagem pontual. A saida numerica declarada no texto bate digito a digito (z = [0. 10. 20. 30. 40.], T = [10. 260. 510. 760. 1010.], X.shape = (3, 4), F com linha z=0 igual a [0,1,2,3] e linha z=2 igual a [-2,-1,0,1]); a chamada invert_yaxis() de fato inverte o eixo; origin="upper" de fato poe a linha 0 no topo; colorbar(label=...) de fato rotula a escala; e os extremos previstos no texto (maximo 3 no canto superior direito, minimo -2 no canto inferior esquerdo) foram confirmados tanto pelos indices da matriz quanto pela posicao em coordenadas de tela. NENHUMA LINHA DA AULA FOI ALTERADA. Nenhum dos 15 achados da auditoria de 2026-09-19 foi reaberto.'

nota_ao_auditor: 'RESOLVIDA EM 2026-09-20 - ver nota_passagem_pontual acima. Registro historico do que estava pendente: DUAS ALEGACOES NOVAS nasceram na revisao didatica de 2026-09-19 e NAO passaram pela auditoria cientifica da mesma data, que e anterior a elas: MATPLOTLIB-API-006 e EXEMPLO-MAPA-007. Elas entraram para fechar o achado didatico VERMELHO DID-M23-A01-OBJETIVO-001 - a aula declarava entre seus resultados esperados "produzir um grafico de linha e um mapa de cores com Matplotlib" e NAO TINHA UMA LINHA de Matplotlib em nenhum dos dois exemplos trabalhados, defeito que a propria auditoria registrou em out_of_scope_observations. A sintaxe foi conferida contra a documentacao oficial do Matplotlib (parametro origin de imshow e parametro label de colorbar) em 2026-09-19; o codigo NAO pode ser executado porque o Matplotlib nao esta instalado no ambiente de verificacao, ao contrario do NumPy. Sinalizadas para checagem pontual pelo auditor-cientifico.'

nota_de_revisao_didatica: 'Aula NAO dividida (1.812 palavras, ~27 min estimados antes desta revisao, abaixo do teto). A revisao de 2026-09-19 acrescentou, aos DOIS exemplos trabalhados ja existentes, o codigo Matplotlib que a aula prometia e nao entregava - quatro linhas no exemplo da geoterma (grafico de linha, com eixo de profundidade invertido) e cinco no exemplo da malha (mapa de cores com barra de escala) -, mais um paragrafo de leitura para cada. NENHUM exemplo novo foi criado e nenhum paragrafo existente foi reescrito: o codigo entrou nos blocos que ja existiam, junto dos dados que ele plota, que e onde ele pedagogicamente pertence. Tambem corrigida a frase quebrada "E exatamente esse e o fio condutor deste modulo" (verbo duplicado), ja registrada pela auditoria como observacao fora de escopo.'
-->
