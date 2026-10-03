# Aula 03: Mecânica do contínuo — a equação da continuidade e a equação de Stokes

**ID:** geologia-avancado-m23-a03
**Módulo:** [[23-modelagem-numerica-geodinamica-modulo|Módulo 23 — Introdução à modelagem numérica geodinâmica]]
**Duração estimada:** ~29 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** apresentar a rocha e o manto como um meio contínuo deformável e formular as duas equações que governam seu movimento — a equação da continuidade (conservação de massa) e a equação de Navier-Stokes na forma de fluxo lento (Stokes) usada em geodinâmica.
**Ao final você vai conseguir:** explicar o que significa tratar a litosfera e o manto como um meio contínuo, e em que condições essa aproximação vale; escrever a equação da continuidade e reconhecer sua forma simplificada para fluxo incompressível; escrever a equação de Stokes (Navier-Stokes sem o termo de inércia), justificar por que o termo de inércia pode ser descartado em geodinâmica, e identificar o papel físico de cada um dos seus termos.
**Pré-requisito:** [[23-modelagem-numerica-geodinamica-aula-02-algebra-linear-calculo-edp-diferencas-finitas|Aula 02 deste módulo]] (equações diferenciais parciais e diferenças finitas).

> [!note] Esta aula é a **Parte 1** de um par.
> Ela estabelece **o que** governa o movimento do meio contínuo: as duas equações, a hipótese que as justifica e o significado físico de cada termo. A [[23-modelagem-numerica-geodinamica-aula-04-malhas-descricoes-lagrangiana-euleriana|Aula 04 — Parte 2]] trata de **como** esse contínuo vira algo que um computador resolve: malhas, malha escalonada, e a escolha entre descrição lagrangiana e euleriana. O par foi dividido porque as duas metades exigem modos de pensar diferentes — física do contínuo de um lado, representação numérica do outro — e empilhá-las numa aula só dobrava a carga sem ganho nenhum. Estude as duas em sequência.

## Conteúdo

### Rocha e manto como meio contínuo

Em escalas de tempo geológico (milhares a milhões de anos), rochas que na escala humana parecem rígidas se comportam como um fluido extremamente viscoso: fluem, se deformam continuamente sob tensão, sem que seja necessário — nem útil — acompanhar o movimento de cada grão mineral individualmente. A **mecânica do contínuo** é o arcabouço que permite isso: em vez de tratar a rocha como um conjunto discreto de partículas (átomos, grãos), ela a trata como um meio **contínuo**, descrito por campos suaves — densidade, velocidade, temperatura, tensão — definidos em cada ponto do espaço, como se a matéria fosse infinitamente divisível. Essa aproximação é válida sempre que a escala do fenômeno de interesse (quilômetros, de uma célula convectiva mantélica, a metros, de uma zona de cisalhamento) é muito maior que a escala microscópica da estrutura da rocha (grãos, cristais, poros) — exatamente o caso da maioria dos problemas de geodinâmica de larga escala que este módulo trata. É essa hipótese que permite escrever equações diferenciais parciais — a linguagem da Aula 02 — para descrever como esses campos contínuos evoluem no espaço e no tempo.

Vale guardar a condição de validade, porque ela delimita o alcance de tudo o que vem a seguir: **a hipótese do contínuo vale quando a escala do problema supera largamente a escala do grão.** Quando não supera — a deformação de um único cristal de olivino, a percolação de fundido por uma rede de poros, o atrito em uma superfície de falha discreta —, a rocha volta a ser um agregado de peças, e as equações desta aula deixam de ser o instrumento certo.

### A equação da continuidade: conservação de massa

A **equação da continuidade** expressa uma ideia simples: massa não se cria nem se destrói — ela apenas se move de um lugar para outro. Na forma geral, para um meio de densidade ρ e campo de velocidade **v**:

∂ρ/∂t + ∇·(ρ**v**) = 0

O primeiro termo é a taxa de variação da densidade num ponto fixo do espaço; o segundo, o **divergente** do fluxo de massa ρ**v** — uma medida de quanto massa está "saindo" (divergente positivo) ou "entrando" (divergente negativo) de uma vizinhança infinitesimal daquele ponto. A equação diz que qualquer aumento de densidade num ponto tem de ser compensado por massa convergindo para ele, e vice-versa.

Para o manto e a litosfera em escalas geológicas, uma simplificação amplamente usada é a **aproximação de incompressibilidade** (ou aproximação de Boussinesq, quando combinada com a equação de calor): tratar a densidade como aproximadamente constante ao longo do escoamento, exceto no termo de empuxo (flutuabilidade) da equação de movimento, onde pequenas variações de densidade — geradas sobretudo por variações de temperatura — é que produzem a força motriz da convecção. A aproximação parece contraditória à primeira leitura, e é bom desfazer o nó: ela **não** diz que a densidade é literalmente constante; diz que a variação de densidade é pequena demais para importar no balanço de massa, e grande o bastante para importar no balanço de forças, onde é a única coisa que põe o manto em movimento. Sob essa aproximação, a equação da continuidade se reduz a:

∇·**v** = 0

— o campo de velocidade é **solenoidal** (sem divergência): tudo que entra num volume qualquer do meio sai dele, sem acúmulo nem déficit de massa. Essa condição, embora simples de escrever, é uma restrição forte sobre qualquer campo de velocidade calculado numericamente — um resultado que viole ∇·**v** ≈ 0 sinaliza um erro no modelo antes mesmo de olhar a física do problema. O exemplo trabalhado desta aula transforma exatamente essa observação num teste executável.

### A equação de Navier-Stokes em regime de fluxo lento (Stokes)

A **equação de Navier-Stokes** descreve a conservação de momento (a versão contínua da segunda lei de Newton) para um fluido viscoso: relaciona a aceleração do material às forças que atuam sobre ele — gradiente de pressão, forças viscosas internas, forças de corpo como a gravidade — incluindo, na forma completa, um termo de inércia (massa vezes aceleração). O que torna a geodinâmica um caso especial, e mais simples de tratar numericamente, é que o manto e a litosfera se deformam de forma **extremamente lenta** comparado à sua viscosidade: o número de Reynolds — a razão adimensional entre forças inerciais e forças viscosas — é, para o manto, absurdamente pequeno (da ordem de 10⁻²⁰ ou menor), muitas ordens de grandeza abaixo do regime em que a inércia importa (como em um rio ou na atmosfera). Isso permite **desprezar completamente o termo de inércia**, reduzindo Navier-Stokes à chamada **equação de Stokes** (ou de fluxo de Stokes, ou "creeping flow"):

−∇P + ∇·[η(∇**v** + (∇**v**)ᵀ)] + ρ**g** = 0

Cada termo tem um papel físico direto: −∇P é o gradiente de pressão (empurra o material das regiões de alta para baixa pressão); ∇·[η(∇**v** + (∇**v**)ᵀ)] é o divergente da tensão viscosa (desviatória), com η a viscosidade (o quão "resistente ao fluir" é o material — a Aula 08 formaliza esse conceito em detalhe); e ρ**g** é a força de corpo devida à gravidade, que atua como motor da convecção sempre que há variação lateral de densidade (tipicamente por variação de temperatura, como visto na equação da continuidade).

A combinação simétrica (∇**v** + (∇**v**)ᵀ) dentro do divergente não é firula de notação: é o tensor de taxa de deformação, e escrevê-lo por inteiro é obrigatório justamente porque, em geodinâmica, **η varia no espaço** — por ordens de grandeza, junto com a temperatura, como a Aula 08 vai mostrar. Só no caso particular de viscosidade **constante** (e fluxo incompressível) o termo se reduz à forma simplificada η∇²**v**, que aparece em muitos textos introdutórios; usar essa forma simplificada num modelo de viscosidade variável é uma das fontes clássicas de implementação errada da equação de Stokes.

Diferente de uma equação dinâmica com inércia, a equação de Stokes é um **equilíbrio instantâneo de forças**: em qualquer instante, pressão, viscosidade e gravidade se equilibram exatamente — não existe "aceleração residual" se acumulando, o que simplifica bastante a solução numérica, mas ainda assim exige resolver uma EDP acoplada à equação da continuidade em cada instante do modelo. É essa última frase que abre a Parte 2 deste par: resolver as duas equações acopladas exige, primeiro, decidir *onde* os valores de velocidade e pressão vão morar.

## Exemplo trabalhado

**Situação: verificar numericamente que um campo de velocidade de cisalhamento puro é solenoidal (∇·v = 0).** Considere o campo de velocidade bidimensional vx = x e vz = −z — um **cisalhamento puro** (*pure shear*) na sua forma mais simples: deformação coaxial, em que o material se estica na direção x na mesma taxa em que se comprime na direção z, sem componente rotacional. (Cuidado com a vizinhança dos termos: *cisalhamento puro* e *cisalhamento simples* são regimes de deformação distintos e contrastados na geologia estrutural — o campo aqui é puro, não simples.) Calcule numericamente o divergente ∇·**v** = ∂vx/∂x + ∂vz/∂z sobre uma malha, usando a diferença central para a primeira derivada (a mesma família de fórmulas do Módulo 30, aula 04 — e, como a fórmula de segunda derivada da Aula 02, ela é de **segunda** ordem de precisão, com erro proporcional a Δx²), e compare com o valor analítico esperado.

```python
import numpy as np

x = np.linspace(-2, 2, 5)      # malha em x, Δx = 1
z = np.linspace(-2, 2, 5)      # malha em z, Δz = 1
X, Z = np.meshgrid(x, z)

vx = X                          # campo vx = x
vz = -Z                         # campo vz = -z

dvx_dx = np.gradient(vx, x, axis=1)   # central no interior, um lado nas bordas
dvz_dz = np.gradient(vz, z, axis=0)   # central no interior, um lado nas bordas

divergente = dvx_dx + dvz_dz
print(divergente)
```

**Conferindo à mão, em qualquer ponto interior:** ∂vx/∂x, para vx=x, é exatamente 1 em toda parte (a inclinação de uma reta de coeficiente 1); ∂vz/∂z, para vz=−z, é exatamente −1 em toda parte. Somando: ∇·**v** = 1 + (−1) = **0** — confirmando analiticamente que o campo é solenoidal. **Saída esperada do código:** `divergente` é uma matriz 5×5 de zeros (ou de valores numericamente indistinguíveis de zero, do tamanho do erro de ponto flutuante — o mesmo erro de arredondamento visto no Módulo 30, aula 01). O resultado é exato, não apenas aproximado, porque vx e vz são funções lineares de suas respectivas variáveis: como visto na Aula 02, a diferença central é exata para polinômios de baixo grau, e uma função linear (grau um) é o caso mais simples possível.

Uma ressalva de leitura de código que vale para todo o módulo: `np.gradient` **não** usa a diferença central em toda a malha. Ela é aplicada apenas nos nós **interiores**; nas duas bordas de cada eixo — onde falta um vizinho, exatamente o problema já encontrado na Aula 02 — a função recorre a uma diferença de um lado só (progressiva na primeira borda, regressiva na última), de primeira ordem por padrão (`edge_order=1`). Aqui as bordas também saem exatamente zero, mas por um motivo adicional ao enunciado acima: a diferença de um lado só, embora menos precisa, **também** é exata para uma função linear. Num campo não linear, as bordas seriam a parte menos precisa do resultado — e é por isso que, num modelo de verdade, é sempre nelas que mora a condição de contorno, não uma derivada estimada de improviso.

Esse é exatamente o tipo de checagem que um código de modelagem geodinâmica real faz de forma rotineira: se o divergente do campo de velocidade calculado — para um caso genuinamente incompressível — não for numericamente próximo de zero, é sinal de erro na formulação ou na discretização da equação de Stokes, antes mesmo de examinar se os valores de temperatura ou tensão fazem sentido físico.

## Recap relâmpago

- A **mecânica do contínuo** trata rocha e manto como um meio contínuo (não partículas discretas). Condição de validade: a escala do fenômeno de interesse supera largamente a escala do grão — abaixo disso (um cristal, um poro, uma superfície de falha), as equações desta aula não servem.
- A **equação da continuidade** (∂ρ/∂t + ∇·(ρ**v**) = 0) expressa conservação de massa; sob a aproximação de incompressibilidade, comum em geodinâmica, reduz-se a ∇·**v** = 0 — um campo de velocidade solenoidal. A aproximação não diz que ρ é constante: diz que sua variação é desprezível no balanço de **massa** e decisiva no balanço de **forças**, onde é o motor da convecção.
- Em geodinâmica, o número de Reynolds do manto é tão baixo (~10⁻²⁰) que o termo de inércia da equação de Navier-Stokes pode ser desprezado, reduzindo-a à **equação de Stokes**: −∇P + ∇·[η(∇**v** + (∇**v**)ᵀ)] + ρ**g** = 0 — um **equilíbrio instantâneo** de forças, não uma equação de aceleração.
- O tensor simétrico completo dentro do divergente é obrigatório porque **η varia no espaço**; só com η constante o termo vira η∇²**v**. Usar a forma simplificada num modelo de viscosidade variável é erro de implementação clássico.
- Verificar numericamente que ∇·**v** ≈ 0 num modelo incompressível é uma checagem básica de consistência, direta a partir das diferenças finitas já vistas na Aula 02.

## Próxima aula

[[23-modelagem-numerica-geodinamica-aula-04-malhas-descricoes-lagrangiana-euleriana|Aula 04 — Malhas e descrições lagrangiana e euleriana: como o contínuo vira um modelo computável]] (Parte 2 deste par) — onde os valores de velocidade e pressão moram dentro do domínio discretizado, por que os códigos de Stokes os colocam em pontos deslocados uns dos outros, e a escolha entre seguir o material e ficar parado vendo-o passar.

## Fontes

- Mecânica do contínuo aplicada a rocha e manto em escala geológica, e a hipótese de continuidade: Turcotte, D. L. & Schubert, G., *Geodynamics*, 3ª ed. (2014), Cambridge University Press, capítulos 2 e 6.
- Equação da continuidade, aproximação de incompressibilidade e aproximação de Boussinesq em convecção mantélica: Turcotte & Schubert, *Geodynamics*, 3ª ed., capítulo 6; Schubert, G., Turcotte, D. L. & Olson, P., *Mantle Convection in the Earth and Planets* (2001), Cambridge University Press.
- Número de Reynolds do manto e a redução de Navier-Stokes à equação de Stokes (fluxo de Stokes) em geodinâmica: Turcotte & Schubert, *Geodynamics*, 3ª ed., capítulo 6; Gerya, T., *Introduction to Numerical Geodynamic Modelling*, 2ª ed. (2019), Cambridge University Press, capítulo sobre equações governantes.
- Forma conservativa em tensão do termo viscoso para viscosidade variável: Gerya, T., *Introduction to Numerical Geodynamic Modelling*, 2ª ed. (2019), capítulo sobre a equação de Stokes com viscosidade variável.
- Cisalhamento puro (coaxial) e cisalhamento simples (não coaxial) como regimes distintos de deformação: Fossen, H., *Structural Geology*, 2ª ed. (2016), Cambridge University Press, capítulo sobre deformação coaxial e não coaxial.
- Comportamento de `numpy.gradient` (diferenças centrais de segunda ordem no interior, diferenças de um lado só nas bordas, `edge_order=1` por padrão): documentação oficial NumPy, `numpy.gradient` (numpy.org/doc/stable/reference/generated/numpy.gradient.html).

<!--
nivel: avancado
palavras_corpo: 2401
mapa_objetivo_secao:
  geologia-avancado-m23-oa02: "Rocha e manto como meio contínuo" + "A equação da continuidade: conservação de massa" + "A equação de Navier-Stokes em regime de fluxo lento (Stokes)" + "Exemplo trabalhado"

divisao_de_aula: 'Esta aula e a PARTE 1 da antiga Aula 03 unica (Mecanica do continuo: equacao da continuidade e equacao de Navier-Stokes; malhas e descricoes lagrangiana e euleriana; 2.622 palavras apos as correcoes da auditoria cientifica de 2026-09-19, ~31 min reais contra 29 declarados, 14 conceitos novos), dividida em 2026-09-19 pela revisao didatica (achado DID-M23-A03-CARGA-002), seguindo a convencao dos Modulos 17, 19, 20, 21 e 22 deste curso. A PARTE 2 e a Aula 04 (malhas e descricoes lagrangiana e euleriana). CORTE ESCOLHIDO: entre a FISICA DO CONTINUO (o que governa o movimento: continuidade e Stokes, esta aula) e a REPRESENTACAO NUMERICA (onde os valores moram e quem os observa: malhas, malha escalonada, lagrangiano x euleriano, Parte 2). E o unico corte do material que nao parte nenhum raciocinio ao meio: a secao de malhas USAVA as equacoes construidas aqui, mas nao contribuia para constru-las, e nao participava do exemplo trabalhado. NENHUMA correcao da auditoria cientifica de 2026-09-19 foi desfeita na divisao: o termo viscoso conservativo em tensao (laranja 2, STOKESVISCOSO-006), a ordem de precisao da diferenca central (laranja 6, ORDEMDIFCENTRAL-007), a ressalva sobre as bordas de np.gradient (laranja 7, GRADIENTEBORDA-008) e o cisalhamento puro (laranja 8, PURESHEAR-009) estao INTEGRALMENTE preservados nesta metade, palavra por palavra. A alegacao MALHA-ESCALONADA-004 e a LAGRANGE-EULER-003 acompanharam o texto correspondente para a Parte 2 - ver nota_alegacoes_migradas.'

nota_alegacoes_migradas: 'As alegacoes GEODIN-M23-A03-LAGRANGE-EULER-003 e GEODIN-M23-A03-MALHA-ESCALONADA-004 NAO estao mais declaradas aqui: acompanharam o texto correspondente para a Aula 04 (Parte 2) na divisao de 2026-09-19. Os claim_id foram DELIBERADAMENTE MANTIDOS com o prefixo A03, que designa a aula pre-divisao, para nao quebrar a rastreabilidade com o manifesto 23-modelagem-numerica-geodinamica-auditoria.json, que os referencia. NAO RENUMERAR.'

alegacoes_auditaveis:
  - claim_id: GEODIN-M23-A03-CONTINUIDADE-001
    claim: "A equacao da continuidade, d(rho)/dt + div(rho*v) = 0, expressa a conservacao de massa de um meio continuo; sob a aproximacao de incompressibilidade (densidade aproximadamente constante ao longo do escoamento, comum em modelagem de manto e litosfera), reduz-se a div(v) = 0, um campo de velocidade solenoidal."
    risk: fato
    source: "Turcotte & Schubert, Geodynamics, 3a ed. (2014), Cambridge University Press, cap. 6."
  - claim_id: GEODIN-M23-A03-REYNOLDS-STOKES-002
    claim: "O numero de Reynolds do manto terrestre e extremamente baixo (ordem de 10^-20 ou menor), o que torna desprezivel o termo de inercia da equacao de Navier-Stokes e permite reduzi-la a equacao de Stokes (fluxo lento/creeping flow): -grad(P) + div(eta*(grad(v) + grad(v)^T)) + rho*g = 0, um equilibrio instantaneo entre gradiente de pressao, tensao viscosa desviatoria e forca de corpo gravitacional. A forma com o tensor simetrico completo e obrigatoria para viscosidade variavel, que e o caso em geodinamica; apenas com eta constante o termo viscoso se reduz a eta*laplaciano(v)."
    risk: fato
    source: "Turcotte & Schubert, Geodynamics, 3a ed. (2014), Cambridge University Press, cap. 6; Gerya, T., Introduction to Numerical Geodynamic Modelling, 2a ed. (2019), Cambridge University Press, cap. sobre equacoes governantes e sobre discretizacao conservativa em tensao."
  - claim_id: GEODIN-M23-A03-EXEMPLO-DIVERGENTE-005
    claim: "Para o campo de velocidade vx=x, vz=-z, o divergente analitico d(vx)/dx + d(vz)/dz = 1 + (-1) = 0 em todo ponto, e a aproximacao numerica reproduz esse valor exatamente (a menos de erro de ponto flutuante), porque tanto a diferenca central (nos interiores) quanto a diferenca de um lado so usada por np.gradient nas bordas sao exatas para funcoes lineares."
    risk: calculo
    source: "Calculo analitico direto e propriedade de exatidao das formulas de diferenca finita para polinomios de baixo grau, reproduzivel a partir do codigo apresentado na aula; documentacao oficial NumPy, funcao numpy.gradient (diferencas centrais de segunda ordem no interior, um lado nas bordas com edge_order=1 por padrao)."
  - claim_id: GEODIN-M23-A03-STOKESVISCOSO-006
    claim: "Em fluxo de Stokes com viscosidade variavel, o termo viscoso da equacao de momento e o divergente do tensor de tensao desviatoria, div(eta*(grad(v) + grad(v)^T)) = div(2*eta*taxa_de_deformacao); a forma div(eta*grad(v)) so coincide com ela quando eta e constante (e o fluxo e incompressivel), caso em que ambas se reduzem a eta*laplaciano(v)."
    risk: fato
    source: "Gerya, T., Introduction to Numerical Geodynamic Modelling, 2a ed. (2019), Cambridge University Press, capitulo sobre a equacao de Stokes com viscosidade variavel; Turcotte & Schubert, Geodynamics, 3a ed. (2014), cap. 6."
  - claim_id: GEODIN-M23-A03-ORDEMDIFCENTRAL-007
    claim: "A formula de diferenca central para a PRIMEIRA derivada, (f[i+1]-f[i-1])/(2*dx), tem erro de truncamento proporcional a dx^2, ou seja, e de SEGUNDA ordem de precisao - a mesma ordem da formula de diferenca central para a segunda derivada usada na Aula 02."
    risk: fato
    source: "Chapra & Canale, Numerical Methods for Engineers, 7a ed., capitulo sobre diferenciacao numerica; Press et al., Numerical Recipes, 3a ed., capitulo sobre derivacao numerica."
  - claim_id: GEODIN-M23-A03-GRADIENTEBORDA-008
    claim: "numpy.gradient aplica diferencas centrais de segunda ordem apenas nos nos interiores do eixo; nas duas bordas usa diferencas de um lado so (progressiva e regressiva), de primeira ordem por padrao (edge_order=1)."
    risk: fato
    source: "Documentacao oficial NumPy, numpy.gradient (numpy.org/doc/stable/reference/generated/numpy.gradient.html)."
  - claim_id: GEODIN-M23-A03-PURESHEAR-009
    claim: "O campo de velocidade vx=x, vz=-z e um cisalhamento puro (pure shear): deformacao coaxial, com estiramento em x e encurtamento em z na mesma taxa e sem componente rotacional; cisalhamento puro e cisalhamento simples sao regimes de deformacao distintos e nao devem ser nomeados juntos."
    risk: fato
    source: "Fossen, H., Structural Geology, 2a ed. (2016), Cambridge University Press, capitulo sobre deformacao coaxial e nao coaxial; Turcotte & Schubert, Geodynamics, 3a ed. (2014), cap. 6."
-->
