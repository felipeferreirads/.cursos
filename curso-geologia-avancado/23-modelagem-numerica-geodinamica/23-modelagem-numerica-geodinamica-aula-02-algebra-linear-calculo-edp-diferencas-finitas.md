# Aula 02: Álgebra linear, cálculo e equações diferenciais parciais — solução analítica versus numérica e o método das diferenças finitas

**ID:** geologia-avancado-m23-a02
**Módulo:** [[23-modelagem-numerica-geodinamica-modulo|Módulo 23 — Introdução à modelagem numérica geodinâmica]]
**Duração estimada:** ~26 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** distinguir equações diferenciais ordinárias de equações diferenciais parciais, explicar quando um problema geodinâmico admite solução analítica e quando exige solução numérica, e aplicar o método das diferenças finitas para aproximar derivadas espaciais — a base da discretização usada em todo o resto do módulo.
**Ao final você vai conseguir:** diferenciar uma EDO de uma EDP pelo número de variáveis independentes envolvidas; explicar por que a maioria dos problemas geodinâmicos reais não tem solução analítica fechada; escrever e aplicar a fórmula de diferença central de segunda ordem para aproximar uma segunda derivada espacial; e descrever, em termos gerais, como a discretização por diferenças finitas transforma uma EDP contínua num conjunto de pontos (a malha) e operações aritméticas sobre eles.
**Pré-requisito:** [[23-modelagem-numerica-geodinamica-aula-01-python-jupyter-numpy-matplotlib|Aula 01 deste módulo]] (NumPy vetorizado). **Pré-requisito cruzado obrigatório:** o Módulo 30 do curso base "Geologia — do essencial ao avançado" — *Métodos numéricos para geociências* —, especialmente a aula 01 (erro numérico e condicionamento), a aula 02 (sistemas lineares por eliminação de Gauss e por Gauss-Seidel) e a aula 04 (diferenças finitas para estimar uma derivada a partir de dados discretos, e o fenômeno de Runge). Esta aula não reensina esse conteúdo — parte diretamente dele para o caso de **equações diferenciais parciais**, que o Módulo 30 deliberadamente deixou para este módulo (ver a aula 05 daquele módulo, seção final). Essa dependência é cruzada entre cursos e por isso é citada aqui por nome, não por link — o grafo formal de pré-requisitos deste curso só aceita módulos do próprio curso.

> [!note] O que o título desta aula promete, e o que ela de fato faz
> "Álgebra linear" e "cálculo" aparecem no título porque são os **dois pré-requisitos que esta aula reativa e põe para trabalhar**, não conteúdo que ela ensina do zero. O cálculo (derivada, derivada parcial, erro de truncamento) vem do Módulo 30, aulas 01 e 04; a álgebra linear (sistemas lineares, Gauss, Gauss-Seidel) vem do Módulo 30, aula 02, e reaparece aqui apenas na última seção, como o **destino** para onde a discretização leva — quem resolve o sistema de fato é a Aula 06. O conteúdo novo desta aula é outro: a distinção EDO/EDP e o método das diferenças finitas aplicado à segunda derivada. Se você chegou aqui esperando uma revisão de álgebra linear, ela está no Módulo 30, não aqui.

## Conteúdo

### EDO e EDP: o que muda quando o espaço entra em cena

O Módulo 30 do curso base fechou com **equações diferenciais ordinárias (EDO)** — equações que relacionam uma grandeza à sua taxa de variação em relação a **uma única variável independente**, tipicamente o tempo, como o decaimento radioativo dN/dt = −λN. Uma **equação diferencial parcial (EDP)**, em contraste, relaciona uma grandeza às suas taxas de variação em relação a **duas ou mais variáveis independentes** ao mesmo tempo — por exemplo, temperatura que varia tanto com a profundidade *z* quanto com o tempo *t*. A notação muda de acordo: a derivada de uma função de uma variável se escreve d/dt (derivada "total"); a derivada de uma função de várias variáveis, mantendo as demais fixas, se escreve com o símbolo ∂ ("derivada parcial") — ∂T/∂t é a taxa de variação da temperatura no tempo, num ponto fixo do espaço; ∂T/∂z é a taxa de variação da temperatura na profundidade, num instante fixo. A equação do calor que a Aula 05 vai formular, ∂T/∂t = κ ∂²T/∂z², é uma EDP porque envolve derivadas parciais em relação a duas variáveis independentes (tempo e profundidade) na mesma equação — é essa presença simultânea de espaço e tempo que separa qualitativamente este módulo do Módulo 30 do curso base, que tratou apenas do tempo isoladamente (a EDO do decaimento) ou apenas do espaço isoladamente (a interpolação e as diferenças finitas da aula 04 daquele módulo, aplicadas a um conjunto de dados sem variação temporal).

### Quando existe solução analítica — e quando não existe

Uma **solução analítica** é uma fórmula fechada que dá o valor da grandeza diretamente, substituindo os parâmetros do problema — como a solução exponencial N(t) = N₀e^(−λt) do decaimento radioativo, ou, como a Aula 07 vai mostrar, a geoterma de resfriamento de uma litosfera oceânica em regime muito simplificado. Soluções analíticas existem para um conjunto restrito de EDPs com geometria simples, condições de contorno simples e coeficientes constantes — casos que servem, sobretudo, como **referência para testar métodos numéricos**, exatamente como o Módulo 30 usou o decaimento radioativo (que tem solução exata) para validar o método de Euler contra um resultado conhecido. Assim que qualquer ingrediente realista entra — produção de calor que varia com a profundidade, uma condutividade térmica que muda entre camadas, uma geometria irregular, uma reologia não linear que depende exponencialmente da própria temperatura que se está calculando —, a fórmula fechada deixa de existir, e a única saída é aproximar a solução numericamente. Isso não é uma limitação rara: é a situação **normal** em geodinâmica quantitativa, e é o motivo de este módulo existir. As Aulas 04 a 07 trabalham quase inteiramente nesse regime sem solução fechada.

### O método das diferenças finitas: de um conjunto de dados a uma equação

O Módulo 30 (aula 04) já introduziu as fórmulas de diferença finita para estimar a **primeira derivada** de uma função a partir de valores discretos: diferença progressiva, regressiva e central. O método das diferenças finitas, aplicado à solução de uma EDP, generaliza essa mesma ideia de duas formas. Primeiro, em vez de partir de um conjunto de dados observados, o método **cria** os pontos discretos deliberadamente: discretiza-se o domínio contínuo (o intervalo de profundidade, por exemplo) num conjunto de pontos igualmente espaçados — os **nós** da **malha** —, separados por um passo espacial fixo Δz. Segundo, para resolver uma equação como a do calor, que envolve a **segunda derivada** ∂²T/∂z² (a curvatura do perfil de temperatura, não apenas sua inclinação), é preciso uma fórmula de diferença finita para a segunda derivada, não apenas para a primeira.

A fórmula de **diferença central de segunda ordem** para a segunda derivada, no nó *i* de uma malha de espaçamento Δz, é:

∂²T/∂z² ≈ (T[i+1] − 2·T[i] + T[i−1]) / Δz²

Ela usa o valor do nó, o do vizinho à frente e o do vizinho atrás, e mede o quanto o nó central "destoa" da média dos seus vizinhos — exatamente o que a curvatura de uma função mede geometricamente. Essa é a fórmula central que sustenta a discretização espacial de toda equação de calor deste módulo (Aulas 05-06) e, de forma equivalente em mais dimensões, da equação de Navier-Stokes (Aula 03).

### Da malha discretizada a um sistema — a ponte de volta ao Módulo 30

Depois que o domínio é discretizado numa malha e as derivadas são substituídas por suas aproximações de diferença finita, uma EDP contínua vira, em cada nó da malha, uma equação algébrica relacionando o valor do nó aos valores dos seus vizinhos. Reunindo essas equações — uma por nó — obtém-se exatamente aquilo que o Módulo 30 (aula 02) já ensinou a resolver: um **sistema de equações lineares**, seja resolvido diretamente (eliminação de Gauss) seja de forma iterativa (Gauss-Seidel). É essa ponte — de EDP para malha, de malha para sistema linear — que a Aula 06 percorre por completo ao construir os esquemas explícito e implícito para a equação do calor: o esquema explícito evita montar um sistema a cada passo (calcula cada nó novo diretamente a partir dos valores antigos vizinhos, sem resolver nada), enquanto o esquema implícito monta, a cada passo de tempo, exatamente um sistema linear do tipo que o Módulo 30 já ensinou a resolver.

## Exemplo trabalhado

**Situação: verificar a fórmula de diferença central de segunda ordem contra uma função de segunda derivada exata conhecida.** Tome a função-teste T(z) = z², cuja segunda derivada exata é constante: d²T/dz² = 2, para qualquer z. Discretize z de 0 a 4 em 5 nós igualmente espaçados (Δz = 1) e calcule a segunda derivada aproximada em cada nó interior pela fórmula de diferença central, comparando com o valor exato.

```python
import numpy as np

z = np.linspace(0, 4, 5)        # nós: 0, 1, 2, 3, 4  (Δz = 1)
T = z**2                        # funcao-teste, segunda derivada exata = 2

dz = z[1] - z[0]
d2T = (T[2:] - 2*T[1:-1] + T[:-2]) / dz**2   # diferenca central, nos interiores

print(T)
print(d2T)
```

**Conferindo à mão, no nó i=2 (z=2):** T[1]=1, T[2]=4, T[3]=9 (valores de z², para z=1,2,3). Aplicando a fórmula: (9 − 2×4 + 1) / 1² = (9 − 8 + 1) / 1 = 2/1 = **2** — exatamente o valor exato da segunda derivada. Repetindo para i=1 (z=1): T[0]=0, T[1]=1, T[2]=4 → (4 − 2 + 0)/1 = 2. E para i=3 (z=3): T[2]=4, T[3]=9, T[4]=16 → (16 − 18 + 4)/1 = 2. **Saída esperada do código:** `d2T = [2. 2. 2.]` para os três nós interiores (i=1, 2, 3) — a malha de 5 nós tem 3 nós interiores, porque a diferença central precisa de um vizinho de cada lado e não pode ser calculada nas duas pontas (z=0 e z=4) sem informação adicional sobre condição de contorno, um ponto que a Aula 06 retoma ao formular as condições de contorno da equação do calor.

O resultado bater exatamente com o valor exato (2, sem nenhum erro de arredondamento) não é coincidência: a fórmula de diferença central de segunda ordem é **exata** para qualquer polinômio de grau até três — como T(z)=z² é de grau dois, o erro de truncamento da fórmula (que depende da quarta derivada da função, nula para um polinômio de grau dois) é rigorosamente zero neste caso particular. Para uma função geológica real — não polinomial —, a fórmula segue sendo uma aproximação, com erro proporcional a Δz², que diminui conforme a malha é refinada — exatamente a mesma lógica de erro de truncamento já vista no Módulo 30 (aula 01) para a diferença de primeira ordem.

## Recap relâmpago

- Uma **EDO** envolve derivadas em relação a uma única variável independente (o Módulo 30 tratou do tempo isoladamente); uma **EDP** envolve derivadas parciais em relação a duas ou mais variáveis independentes ao mesmo tempo (tipicamente espaço e tempo) — a equação do calor da Aula 05 é uma EDP.
- **Solução analítica** (fórmula fechada) só existe para casos simplificados, usados sobretudo como referência para testar métodos numéricos; a maioria dos problemas geodinâmicos reais não tem solução fechada e exige solução numérica — a situação normal deste módulo, não a exceção.
- O método das diferenças finitas discretiza o domínio contínuo numa malha de **nós** espaçados por Δz, e aproxima as derivadas parciais por fórmulas envolvendo os valores dos nós vizinhos.
- A **diferença central de segunda ordem**, ∂²T/∂z² ≈ (T[i+1] − 2T[i] + T[i−1]) / Δz², aproxima a segunda derivada espacial e é exata para polinômios até grau três — a peça central da discretização espacial usada nas Aulas 03 a 09.
- Discretizar uma EDP numa malha gera, em cada nó, uma equação algébrica ligando vizinhos — reunindo todos os nós, obtém-se um sistema de equações lineares, resolvido pelos mesmos métodos (Gauss, Gauss-Seidel) já ensinados no Módulo 30 do curso base; é exatamente essa ponte que o esquema implícito da Aula 06 percorre por completo.

## Próxima aula

[[23-modelagem-numerica-geodinamica-aula-03-mecanica-continuo-continuidade-stokes|Aula 03 — Mecânica do contínuo: a equação da continuidade e a equação de Stokes]] — a segunda EDP central deste módulo, agora para o movimento do material (não para o calor), com a mesma lógica de malha e discretização introduzida aqui. É a Parte 1 de um par: a Parte 2 (Aula 04) trata das malhas e das descrições lagrangiana e euleriana.

## Fontes

- Classificação de equações diferenciais ordinárias e parciais, e a distinção entre derivada total e derivada parcial: Chapra, S. C. & Canale, R. P., *Numerical Methods for Engineers*, 7ª ed., McGraw-Hill, capítulo introdutório sobre equações diferenciais.
- A fórmula de diferença central de segunda ordem para a segunda derivada e sua ordem de erro de truncamento (proporcional a Δz², exata para polinômios até grau três): Chapra & Canale, *Numerical Methods for Engineers*, 7ª ed., capítulo sobre diferenciação numérica; Press, W. H. et al., *Numerical Recipes*, 3ª ed., Cambridge University Press, capítulo sobre derivação numérica.
- Discretização de equações diferenciais parciais por diferenças finitas em geodinâmica, e a ligação entre esquemas explícito/implícito e sistemas lineares: Gerya, T., *Introduction to Numerical Geodynamic Modelling*, 2ª ed. (2019), Cambridge University Press, capítulo introdutório sobre discretização; Turcotte, D. L. & Schubert, G., *Geodynamics*, 3ª ed. (2014), Cambridge University Press, capítulo 4.
- Sistemas lineares por eliminação de Gauss e por Gauss-Seidel como retomada direta: Módulo 30 do curso base, aula 02.

<!--
nivel: avancado
palavras_corpo: 2152
cross_course_prerequisite: curso-geologia, modulo 30 (aulas 01, 02, 04)
mapa_objetivo_secao:
  geologia-avancado-m23-oa02: "EDO e EDP: o que muda quando o espaço entra em cena" + "Quando existe solução analítica — e quando não existe" + "O método das diferenças finitas: de um conjunto de dados a uma equação" + "Da malha discretizada a um sistema — a ponte de volta ao Módulo 30" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEODIN-M23-A02-EDOEDP-001
    claim: "Uma equacao diferencial ordinaria (EDO) envolve derivadas em relacao a uma unica variavel independente; uma equacao diferencial parcial (EDP) envolve derivadas parciais em relacao a duas ou mais variaveis independentes simultaneamente, como espaco e tempo."
    risk: fato
    source: "Chapra & Canale, Numerical Methods for Engineers, 7a ed., capitulo introdutorio sobre equacoes diferenciais."
  - claim_id: GEODIN-M23-A02-DIFCENTRAL2-002
    claim: "A formula de diferenca central de segunda ordem para a segunda derivada e d2T/dz2 aproximadamente igual a (T[i+1] - 2T[i] + T[i-1])/dz^2, com erro de truncamento proporcional a dz^2, sendo exata para polinomios de grau ate tres (quarta derivada nula)."
    risk: fato
    source: "Chapra & Canale, Numerical Methods for Engineers, 7a ed., capitulo sobre diferenciacao numerica; Press et al., Numerical Recipes, 3a ed., capitulo sobre derivacao numerica."
  - claim_id: GEODIN-M23-A02-DISCRETIZACAO-SISTEMA-003
    claim: "Ao discretizar uma equacao diferencial parcial por diferencas finitas em uma malha de nos, cada no gera uma equacao algebrica relacionando seu valor aos dos nos vizinhos; reunindo as equacoes de todos os nos obtem-se um sistema de equacoes lineares, que pode ser resolvido por metodos diretos (eliminacao de Gauss) ou iterativos (Gauss-Seidel)."
    risk: fato
    source: "Gerya, T., Introduction to Numerical Geodynamic Modelling, 2a ed. (2019), Cambridge University Press, capitulo introdutorio; Chapra & Canale, Numerical Methods for Engineers, 7a ed."
  - claim_id: GEODIN-M23-A02-EXEMPLO-DIFCENTRAL-004
    claim: "Para T(z) = z^2 discretizada em nos de espacamento dz=1 (z=0,1,2,3,4), a diferenca central de segunda ordem aplicada aos nos interiores (z=1,2,3) resulta em d2T/dz2 = 2 em cada um, igual ao valor exato da segunda derivada de z^2, sem erro de truncamento porque a formula e exata para polinomios de grau dois."
    risk: calculo
    source: "Calculo aritmetico direto reproduzivel a partir do codigo apresentado na aula, decorrente da propriedade de exatidao da formula para polinomios ate grau tres."
-->
