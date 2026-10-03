# Aula 06: Solução numérica da equação do calor — esquemas explícito (FTCS) e implícito (BTCS)

**ID:** geologia-avancado-m23-a06
**Módulo:** [[23-modelagem-numerica-geodinamica-modulo|Módulo 23 — Introdução à modelagem numérica geodinâmica]]
**Duração estimada:** ~28 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** resolver numericamente a equação da difusão formulada na Aula 05 pelos esquemas explícito (FTCS) e implícito (BTCS), incluindo a condição de estabilidade que governa o esquema explícito e a razão física por que violá-la produz um resultado impossível.
**Ao final você vai conseguir:** discretizar uma EDP no tempo e no espaço numa malha espaço-tempo; implementar em Python um passo de tempo do esquema explícito para a equação do calor 1D; calcular o passo de tempo máximo permitido pela condição de estabilidade de von Neumann e reconhecer, pelo princípio do máximo, um resultado que a equação não admite; e explicar por que o esquema implícito, ao custo de resolver um sistema linear a cada passo, é estável para qualquer passo de tempo.
**Pré-requisito:** [[23-modelagem-numerica-geodinamica-aula-05-calor-fourier-conservacao-producao-adveccao|Aula 05 deste módulo]] (a equação da difusão, ∂T/∂t = κ ∂²T/∂z²) e a Aula 02 (diferença central para a segunda derivada). **Pré-requisito cruzado obrigatório:** o Módulo 30 do curso base "Geologia — do essencial ao avançado" — *Métodos numéricos para geociências* —, aula 02 (eliminação de Gauss, usada aqui para o esquema implícito). Citado por nome, não por link, por ser dependência entre cursos.

> [!note] Esta aula é a **Parte 2** de um par.
> A [[23-modelagem-numerica-geodinamica-aula-05-calor-fourier-conservacao-producao-adveccao|Aula 05 — Parte 1]] formulou a física: a lei de Fourier, os três termos da equação de conservação de calor e a difusividade térmica κ. Esta aula resolve numericamente a forma reduzida que aquela deixou pronta, ∂T/∂t = κ ∂²T/∂z². Se essa equação e o significado de κ ainda não estiverem assentados, volte antes de seguir.

## Conteúdo

### Discretizando no tempo e no espaço: a malha espaço-tempo

A Aula 02 discretizou o **espaço**: nós de índice *i*, espaçados por Δz. Resolver uma EDP de evolução exige discretizar também o **tempo**, em passos de tamanho Δt, indexados por *n*. A notação do módulo passa então a ter dois índices: **T[i, n]** é a temperatura no nó espacial *i*, no passo de tempo *n*.

As duas derivadas da equação recebem tratamentos já conhecidos:

- A derivada **temporal** ∂T/∂t se aproxima pela **diferença progressiva no tempo**, (T[i,n+1] − T[i,n]) / Δt — o valor novo menos o valor antigo, dividido pelo passo. É a mesma diferença progressiva da aula 04 do Módulo 30, aplicada agora ao eixo do tempo.
- A derivada **espacial** de segunda ordem se aproxima pela **diferença central** já deduzida na Aula 02: (T[i+1] − 2T[i] + T[i−1]) / Δz².

Falta uma decisão, e é ela que separa os dois esquemas desta aula: **os valores espaciais usados na diferença central são tomados no passo de tempo antigo (n, já conhecido) ou no novo (n+1, ainda desconhecido)?** Tudo o que vem a seguir — custo, simplicidade e estabilidade — decorre dessa única escolha.

### Esquema explícito (FTCS): avançar sem resolver sistema

O esquema **explícito**, também chamado **FTCS** (*forward in time, central in space* — progressivo no tempo, central no espaço), usa os valores espaciais do passo **antigo**, que já são conhecidos, para calcular diretamente o valor de cada nó no passo novo:

T[i, n+1] = T[i, n] + r · (T[i+1, n] − 2T[i, n] + T[i−1, n]) + A·Δt/(ρCp)

onde

r = κΔt/Δz²

é um número adimensional que reúne, num só parâmetro, o passo de tempo, o espaçamento da malha e a difusividade térmica. Vale ler r fisicamente: ele compara a distância que o calor difunde num passo de tempo com o tamanho da célula da malha.

A vantagem do esquema explícito é sua simplicidade: cada nó novo se calcula **diretamente** a partir de valores já conhecidos, sem montar nem resolver nenhum sistema de equações. Isso é uma linha de código por nó, e nada mais.

### A condição de estabilidade, e o que significa "impossível"

O preço dessa simplicidade é uma restrição severa sobre o tamanho do passo de tempo. A **condição de estabilidade de von Neumann**, para esse esquema em uma dimensão, exige:

r = κΔt/Δz² ≤ 1/2

Se a condição for violada — passo de tempo grande demais para o espaçamento de malha escolhido —, a solução não fica apenas "menos precisa": ela **diverge**, produzindo oscilações que crescem sem limite e valores impossíveis já nos primeiros passos.

Mas "impossível" precisa de um critério, e o critério é preciso: a equação da difusão obedece ao **princípio do máximo** — sem termo de produção, a solução em qualquer instante posterior fica necessariamente **dentro** do intervalo entre o menor e o maior valor presentes na condição inicial e nas condições de contorno. Calor nunca se concentra espontaneamente. Um valor que escapa desse intervalo é, portanto, matematicamente impossível para a equação sendo resolvida — e repare que o critério **não** é o sinal do número: uma temperatura negativa em graus Celsius não tem nada de impossível em si (uma geoterma sob uma superfície glaciada começa negativa). O que denuncia a instabilidade é sair do intervalo permitido, não ficar abaixo de zero.

A instabilidade é, portanto, um artefato puramente numérico da discretização, sem nenhum análogo físico. É, de longe, o tropeço mais comum ao programar pela primeira vez um esquema explícito, e o exemplo trabalhado a seguir reproduz exatamente esse efeito lado a lado com um passo estável, para que a diferença fique visível.

### Esquema implícito (BTCS): estável ao custo de um sistema

O esquema **implícito**, ou **BTCS** (*backward in time, central in space* — regressivo no tempo, central no espaço), faz a escolha oposta: usa os valores espaciais do passo **novo**, ainda desconhecido, na diferença central:

T[i, n+1] − r · (T[i+1, n+1] − 2T[i, n+1] + T[i−1, n+1]) = T[i, n] + A·Δt/(ρCp)

Como o lado esquerdo envolve três incógnitas por nó — o próprio nó e seus dois vizinhos, todos no passo novo —, essa equação **não pode** ser resolvida nó a nó isoladamente. Reunindo a equação de todos os nós da malha, obtém-se exatamente o **sistema de equações lineares** que a Aula 02 já havia antecipado como destino natural da discretização por diferenças finitas — e que o Módulo 30 do curso base (aula 02) ensina a resolver.

A estrutura desse sistema é particularmente simples, e essa simplicidade é o que torna o esquema viável: como cada equação envolve só três incógnitas vizinhas, a matriz é **tridiagonal** — não-zeros apenas na diagonal principal e nas duas diagonais adjacentes. Uma matriz assim se resolve por uma variante especializada e muito barata da eliminação de Gauss, o **algoritmo de Thomas**.

Em troca desse custo adicional — montar e resolver um sistema a cada passo de tempo, em vez de uma conta direta —, o esquema implícito é **incondicionalmente estável**: qualquer tamanho de passo de tempo produz uma solução numericamente estável, sem a restrição r ≤ 1/2. Uma ressalva que costuma escapar: estabilidade **não** é precisão. Um passo de tempo grande demais continua perdendo fidelidade física, só que agora sem explodir — o erro é silencioso em vez de escandaloso, o que em certos contextos é pior.

É essa troca — simplicidade e passo limitado (explícito) versus custo de resolver um sistema e passo livre (implícito) — que orienta a escolha do esquema em qualquer código real de modelagem térmica.

## Exemplo trabalhado

**Situação: um pulso de temperatura numa malha de 5 nós, com e sem violar a condição de estabilidade.** Considere uma malha 1D de 5 nós (z = 0, 1, 2, 3, 4, com Δz = 1), extremidades fixas em T = 0 (condição de contorno), difusividade térmica κ = 0,5, e uma condição inicial com um pulso de temperatura no nó central: T = [0, 0, 100, 0, 0]. Calcule um passo de tempo do esquema explícito, sem produção de calor (A = 0), primeiro com Δt = 0,5 (estável) e depois com Δt = 2 (instável), e compare.

**Caso estável — Δt = 0,5.** r = κΔt/Δz² = 0,5 × 0,5 / 1² = 0,25, dentro do limite r ≤ 0,5. Aplicando T[i,novo] = T[i] + r·(T[i+1] − 2T[i] + T[i−1]) a cada nó interior (i=1,2,3; os nós de contorno i=0 e i=4 permanecem fixos em 0):

- i=1: T[0]=0, T[1]=0, T[2]=100 → T_novo[1] = 0 + 0,25×(100 − 0 + 0) = **25**
- i=2: T[1]=0, T[2]=100, T[3]=0 → T_novo[2] = 100 + 0,25×(0 − 200 + 0) = 100 − 50 = **50**
- i=3: T[2]=100, T[3]=0, T[4]=0 → T_novo[3] = 0 + 0,25×(0 − 0 + 100) = **25**

Resultado: T_novo = [0, 25, 50, 25, 0] — o pulso se espalhou de forma suave e simétrica para os vizinhos, exatamente o comportamento físico esperado de difusão. Conferindo a conservação de energia: a soma dos valores antes (0+0+100+0+0=100) é igual à soma depois (0+25+50+25+0=100) — nenhuma energia "vazou" nem "apareceu", como esperado para um passo sem produção de calor e sem perda pelos contornos (o pulso ainda não alcançou as extremidades fixas). E todos os valores continuam dentro de [0, 100], como o princípio do máximo exige.

**Caso instável — Δt = 2.** r = 0,5 × 2 / 1² = 1,0, muito acima do limite 0,5. Repetindo a mesma fórmula:

- i=1: T_novo[1] = 0 + 1,0×(100 − 0 + 0) = **100**
- i=2: T_novo[2] = 100 + 1,0×(0 − 200 + 0) = 100 − 200 = **−100**
- i=3: T_novo[3] = 0 + 1,0×(0 − 0 + 100) = **100**

Resultado: T_novo = [0, 100, −100, 100, 0] — um valor de −100 no nó central, **fora do intervalo [0, 100]** delimitado pela condição inicial e pelos contornos, ou seja, uma violação direta do princípio do máximo enunciado acima: nenhuma solução da equação da difusão sem produção pode sair desse intervalo. Junto com ele, uma oscilação violenta entre nós vizinhos que só vai piorar nos passos seguintes. Nada mudou na física do problema entre os dois casos — só o tamanho do passo de tempo —, o que confirma que a instabilidade é um artefato puramente numérico da violação da condição r ≤ 0,5, exatamente como a seção anterior descreveu.

```python
import numpy as np

def passo_explicito(T, r):
    T_novo = T.copy()
    T_novo[1:-1] = T[1:-1] + r * (T[2:] - 2*T[1:-1] + T[:-2])
    # contornos T[0] e T[-1] permanecem fixos (condicao de contorno de Dirichlet)
    return T_novo

T0 = np.array([0., 0., 100., 0., 0.])

print("estavel  (r=0.25):", passo_explicito(T0, r=0.25))
print("instavel (r=1.00):", passo_explicito(T0, r=1.00))
```

**Saída esperada:** `estavel (r=0.25): [0. 25. 50. 25. 0.]` e `instavel (r=1.00): [0. 100. -100. 100. 0.]` — reproduzindo exatamente os dois cálculos manuais acima. O esquema **implícito**, para este mesmo pulso e o mesmo Δt=2 que quebrou o esquema explícito, permaneceria estável (sem oscilação nem valor fora do intervalo) — ao custo de, em vez da conta direta usada aqui, montar e resolver a cada passo um sistema linear tridiagonal de 3 incógnitas (os três nós interiores), pelo mesmo tipo de eliminação de Gauss já ensinada no Módulo 30, aula 02.

## Recap relâmpago

- Discretizar uma EDP de evolução exige **dois** índices: *i* no espaço (Δz, como na Aula 02) e *n* no tempo (Δt). A derivada temporal vira diferença progressiva; a espacial de segunda ordem, diferença central.
- O esquema **explícito (FTCS)** calcula cada nó novo diretamente a partir dos valores antigos vizinhos, sem resolver sistema — simples e barato por passo, mas **condicionalmente estável**: exige r = κΔt/Δz² ≤ 1/2.
- Violar a condição de estabilidade não deixa a solução "um pouco pior" — produz oscilações crescentes e valores que escapam do intervalo permitido pelo **princípio do máximo** (a solução da difusão sem produção nunca sai do intervalo entre o menor e o maior valor da condição inicial e dos contornos). **O sinal de alarme é o valor fora do intervalo, não o sinal negativo em si.**
- O esquema **implícito (BTCS)** usa os valores do passo novo na diferença espacial, o que gera um sistema linear **tridiagonal** a cada passo (resolvido pelo algoritmo de Thomas, uma eliminação de Gauss especializada) — mais caro por passo, mas **incondicionalmente estável** para qualquer Δt. Estabilidade, porém, não é precisão: um passo grande demais erra em silêncio.
- A escolha entre explícito e implícito é um compromisso entre simplicidade/custo por passo e liberdade de passo — a mesma lógica de trade-off entre método direto e iterativo já vista no Módulo 30, aula 02, agora aplicada no tempo.

## Próxima aula

[[23-modelagem-numerica-geodinamica-aula-07-calor-litosfera-oceanica-continental-geotermas|Aula 07 — Calor na litosfera oceânica e continental: resfriamento e envelhecimento, geotermas estáveis e elementos produtores de calor]] — aplicação direta da equação de calor das Aulas 05-06 a casos reais de litosfera, incluindo a solução analítica de resfriamento por semi-espaço que serve de referência para validar os esquemas numéricos construídos aqui.

## Fontes

- Esquemas de diferenças finitas explícito (FTCS) e implícito (BTCS) para a equação do calor, e a condição de estabilidade de von Neumann (r ≤ 1/2 em 1D para o esquema explícito): Press, W. H. et al., *Numerical Recipes*, 3ª ed. (2007), Cambridge University Press, capítulo sobre equações diferenciais parciais; Gerya, T., *Introduction to Numerical Geodynamic Modelling*, 2ª ed. (2019), Cambridge University Press, capítulo sobre solução numérica da equação do calor.
- Matriz tridiagonal resultante do esquema implícito e o algoritmo de Thomas como especialização da eliminação de Gauss: Press et al., *Numerical Recipes*, 3ª ed., capítulo sobre sistemas tridiagonais; retomada do Módulo 30 do curso base, aula 02 (eliminação de Gauss).
- Estabilidade incondicional do esquema implícito (BTCS) para a equação da difusão: Press et al., *Numerical Recipes*, 3ª ed., capítulo sobre equações diferenciais parciais parabólicas.
- Princípio do máximo da equação do calor (a solução não sai do intervalo definido pela condição inicial e pelas condições de contorno, na ausência de fontes): Evans, L. C., *Partial Differential Equations*, 2ª ed. (2010), American Mathematical Society, capítulo sobre a equação do calor.

<!--
nivel: avancado
palavras_corpo: 2310
cross_course_prerequisite: curso-geologia, modulo 30 (aula 02)
mapa_objetivo_secao:
  geologia-avancado-m23-oa02: "Discretizando no tempo e no espaço: a malha espaço-tempo" + "Esquema explícito (FTCS): avançar sem resolver sistema" + "A condição de estabilidade, e o que significa impossível" + "Esquema implícito (BTCS): estável ao custo de um sistema" + "Exemplo trabalhado"

divisao_de_aula: 'Esta aula e a PARTE 2 da antiga Aula 04 unica (Calor: lei de Fourier, conservacao de calor, producao e adveccao; solucoes numericas explicita e implicita; 2.587 palavras apos as correcoes da auditoria cientifica de 2026-09-19, ~31 min reais contra 30 declarados - JA NO TETO DO PLUGIN ANTES DA AUDITORIA -, 15 conceitos novos todos operacionais), dividida em 2026-09-19 pela revisao didatica (achado DID-M23-A04-CARGA-001). A PARTE 1 e a Aula 05 (lei de Fourier, os tres termos, difusividade termica). CORTE ESCOLHIDO: entre a FORMULACAO FISICA (Parte 1) e a SOLUCAO NUMERICA (esta aula). NENHUMA correcao da auditoria cientifica foi desfeita: a correcao do achado 3 (MAXIMOPRINCIPIO-007, o principio do maximo como criterio de impossibilidade, em lugar do sinal negativo) esta INTEGRALMENTE preservada aqui, no corpo, no exemplo trabalhado e no Recap, e ganhou secao propria ("A condicao de estabilidade, e o que significa impossivel"), ficando mais visivel do que estava. O EXEMPLO TRABALHADO desta aula e O ORIGINAL da antiga Aula 04, preservado PALAVRA POR PALAVRA (situacao, os seis calculos a mao dos dois casos, codigo e saida esperada), com dois acrescimos de uma frase cada que aplicam explicitamente o principio do maximo aos dois casos - o que a correcao da auditoria pedia e o formato de aula unica nao dava espaco para fazer.'

nota_alegacoes_migradas: 'As alegacoes GEODIN-M23-A04-ESQUEMA-EXPLICITO-002, GEODIN-M23-A04-ESTABILIDADE-VONNEUMANN-003, GEODIN-M23-A04-ESQUEMA-IMPLICITO-004, GEODIN-M23-A04-EXEMPLO-EXPLICITO-005 e GEODIN-M23-A04-MAXIMOPRINCIPIO-007 acompanharam para ca o texto correspondente, na divisao de 2026-09-19. Os claim_id foram DELIBERADAMENTE MANTIDOS com o prefixo A04, que designa a aula pre-divisao, para nao quebrar a rastreabilidade com o manifesto 23-modelagem-numerica-geodinamica-auditoria.json, que os referencia. NAO RENUMERAR, apesar de esta ser agora a Aula 06. As alegacoes FOURIER-CONSERVACAO-001 e KAPPA-DECAIMENTO-006 ficaram na Parte 1 (Aula 05), pelo mesmo criterio.'

alegacoes_auditaveis:
  - claim_id: GEODIN-M23-A04-ESQUEMA-EXPLICITO-002
    claim: "O esquema explicito (FTCS, forward in time central in space) para a equacao da difusao calcula o valor de cada no no passo de tempo seguinte diretamente a partir dos valores conhecidos do passo anterior, sem resolver um sistema de equacoes, usando a formula T[i,n+1] = T[i,n] + r*(T[i+1,n] - 2T[i,n] + T[i-1,n]), onde r = kappa*dt/dz^2."
    risk: fato
    source: "Press et al., Numerical Recipes, 3a ed. (2007), Cambridge University Press, cap. sobre equacoes diferenciais parciais; Gerya, Introduction to Numerical Geodynamic Modelling, 2a ed. (2019)."
  - claim_id: GEODIN-M23-A04-ESTABILIDADE-VONNEUMANN-003
    claim: "A condicao de estabilidade de von Neumann para o esquema explicito (FTCS) da equacao da difusao unidimensional exige r = kappa*dt/dz^2 <= 1/2; ultrapassar esse limite produz uma solucao numericamente instavel, com oscilacoes que crescem a cada passo de tempo, sem analogo fisico."
    risk: fato
    source: "Press et al., Numerical Recipes, 3a ed. (2007), Cambridge University Press, cap. sobre equacoes diferenciais parciais parabolicas; Gerya, Introduction to Numerical Geodynamic Modelling, 2a ed. (2019)."
  - claim_id: GEODIN-M23-A04-MAXIMOPRINCIPIO-007
    claim: "A equacao da difusao sem termo de producao obedece ao principio do maximo: a solucao em qualquer instante posterior permanece dentro do intervalo entre o menor e o maior valor presentes na condicao inicial e nas condicoes de contorno. Um valor calculado fora desse intervalo e impossivel para a equacao sendo resolvida - criterio que nao depende de o valor ser negativo, ja que uma temperatura negativa em graus Celsius e fisicamente banal."
    risk: fato
    source: "Press et al., Numerical Recipes, 3a ed. (2007), Cambridge University Press, cap. sobre equacoes diferenciais parciais parabolicas; Evans, L. C., Partial Differential Equations, 2a ed. (2010), American Mathematical Society, capitulo sobre a equacao do calor (principio do maximo)."
  - claim_id: GEODIN-M23-A04-ESQUEMA-IMPLICITO-004
    claim: "O esquema implicito (BTCS, backward in time central in space) para a equacao da difusao usa os valores do passo de tempo novo na diferenca espacial, gerando um sistema linear tridiagonal a ser resolvido a cada passo (por eliminacao de Gauss especializada, o algoritmo de Thomas); em troca do custo adicional por passo, o esquema e incondicionalmente estavel para qualquer tamanho de passo de tempo, ao contrario do esquema explicito. Estabilidade, porem, nao e precisao: um passo grande demais perde fidelidade fisica sem divergir."
    risk: fato
    source: "Press et al., Numerical Recipes, 3a ed. (2007), Cambridge University Press, caps. sobre sistemas tridiagonais e sobre equacoes diferenciais parciais parabolicas."
  - claim_id: GEODIN-M23-A04-EXEMPLO-EXPLICITO-005
    claim: "Para a malha T=[0,0,100,0,0] com nos de contorno fixos, aplicando um passo do esquema explicito com r=0.25 obtem-se T_novo=[0,25,50,25,0] (estavel, energia conservada, todos os valores dentro de [0,100]); aplicando o mesmo passo com r=1.0 (acima do limite de estabilidade 0.5) obtem-se T_novo=[0,100,-100,100,0], em que o valor -100 esta fora do intervalo [0,100] da condicao inicial e dos contornos e portanto viola o principio do maximo da equacao da difusao, demonstrando a instabilidade numerica."
    risk: calculo
    source: "Calculo aritmetico direto reproduzivel a partir da formula do esquema explicito apresentada na aula, conferido por execucao (numpy 2.5.1)."
-->
