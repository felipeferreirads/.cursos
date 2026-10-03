# Questionário — Módulo 19: Geofísica aplicada na exploração mineral (Parcial 3)

**Cobre:** Aulas 06 e 07 · **Objetivo:** `geologia-avancado-m19-oa04` — explicar os fundamentos, as vantagens e as limitações da inversão geofísica e dos modelos de prospectividade mineral

## Questões

**1. (Múltipla escolha)** Qual das alternativas distingue corretamente problema direto e problema inverso em geofísica?
- a) O problema direto (modelo → anomalia) tem solução única; o problema inverso (anomalia observada → modelo) é o que a exploração precisa resolver e, em campos potenciais, é fundamentalmente não único
- b) Os dois problemas são igualmente não únicos
- c) O problema inverso sempre tem solução única se o dado for de boa qualidade
- d) O problema direto é o que a exploração precisa resolver na prática
- e) Problema direto e problema inverso são sinônimos em geofísica de exploração

**2. (Dissertativa curta)** Explique por que o problema inverso de campos potenciais (gravimetria, magnetometria) é fundamentalmente não único, mesmo com dados perfeitos e sem ruído. Use o exemplo da esfera e da casca esférica concêntrica para ilustrar, citando a condição exata sob a qual esse exemplo vale.

**3. (V/F — justifique)** Melhorar a densidade de amostragem e a qualidade do dado gravimétrico, por si só, elimina a não unicidade do problema inverso de campos potenciais.

**4. (Múltipla escolha)** Sobre a regularização por "inversão de estrutura mínima" (inversão de Occam), é correto afirmar que:
- a) Ela recupera exatamente a geometria real do corpo geológico, sem viés
- b) Ela escolhe, entre os modelos que ajustam o dado, o mais suave possível — o que tende a produzir corpos mais difusos e de contraste menor do que a geologia real, podendo superestimar o volume aparente
- c) Ela é a única forma de regularização usada em geofísica de exploração
- d) Ela elimina completamente a necessidade de dados petrofísicos
- e) Ela é aplicável apenas a dados de eletrorresistividade, não a campos potenciais

**5. (Aplicação)** Uma anomalia magnética residual isolada é invertida em 3D por duas equipes. A Equipe P usa inversão de estrutura mínima padrão, sem restrição petrofísica, e obtém um corpo largo e de baixo contraste de susceptibilidade. A Equipe Q restringe a inversão à faixa de susceptibilidade de amostras de testemunho de um furo próximo que atravessou magnetita maciça confirmada, e obtém um corpo mais estreito, mais profundo e de contraste mais alto. Os dois modelos são igualmente válidos do ponto de vista matemático? Qual equipe toma a decisão de sondagem mais bem embasada, e por quê?

**6. (V/F — justifique)** Passar de uma inversão 2D para uma inversão 3D resolve a ambiguidade fundamental do problema inverso em campos potenciais.

**7. (Múltipla escolha)** Uma "camada de evidência", no contexto de modelos de prospectividade mineral, é:
- a) O valor bruto de uma variável física medida (por exemplo, o mapa de campo magnético total em nanoteslas)
- b) Uma reinterpretação do dado bruto em termos do grau em que ele favorece a presença de um sistema mineral — já filtrada pelo modelo de sistema mineral que está sendo testado
- c) Sinônimo de "modelo de aprendizado de máquina"
- d) Um dado exclusivamente geoquímico, nunca geofísico
- e) Um mapa de prospectividade final, pronto para decisão de sondagem

**8. (V/F — justifique)** O método de pesos de evidência (weights of evidence) é uma abordagem puramente orientada por dados (data-driven), sem nenhuma influência de um modelo conceitual definido por especialistas.

**9. (Dissertativa curta)** Explique o "problema dos positivos raros" em modelos de prospectividade mineral baseados em aprendizado de máquina, citando os dois riscos que ele gera para um modelo treinado.

**10. (Aplicação)** Uma equipe dispõe de oito camadas de evidência sobre uma região de 20.000 km², incluindo uma camada de polarização induzida que cobre apenas 6% da área, e pretende treinar diretamente uma rede neural usando os 5 depósitos conhecidos da região como único conjunto de positivos. Identifique os dois problemas estruturais dessa proposta e descreva, em linhas gerais, a correção híbrida recomendada pela aula.

---

## Gabarito comentado

<details><summary>Ver respostas</summary>

**1.** Resposta: **a)**. O problema direto (dado um modelo, calcular a anomalia) tem solução única, determinada pelas leis físicas. O problema inverso (dada a anomalia, encontrar o modelo) é o que a exploração precisa resolver na prática, e em campos potenciais é fundamentalmente não único — infinitas distribuições internas produzem a mesma assinatura externa. As demais alternativas invertem ou distorcem essa relação.

**2.** Resposta esperada: é um resultado clássico da teoria do potencial — existem infinitas distribuições de massa/magnetização diferentes no interior de um volume que produzem exatamente o mesmo campo observado na superfície externa a esse volume; não é limitação de qualidade de dado, é propriedade matemática do próprio campo potencial. O exemplo da esfera e da casca: uma esfera densa pequena a certa profundidade produz, na superfície, a mesma anomalia gravimétrica que uma casca esférica mais larga e de topo mais raso, concêntrica com ela, contendo a mesma massa total. A condição exata (teorema da casca de Newton): a distribuição precisa ser **esfericamente simétrica**, a casca **concêntrica** com a esfera, e o ponto de observação **fora** da distribuição — sob essas condições, o campo externo depende só da massa total e da posição do centro.

**3.** Falso. A não unicidade é uma propriedade matemática do próprio campo potencial, não uma limitação de qualidade ou densidade de amostragem do dado — nenhuma quantidade de dado melhor, por si só, resolve o problema. É preciso introduzir informação externa ao dado (regularização, petrofísica local) para escolher um modelo específico entre os infinitos matematicamente compatíveis.

**4.** Resposta: **b)**. A inversão de estrutura mínima escolhe o modelo mais suave entre os que ajustam o dado, o que tende a produzir corpos mais difusos e de menor contraste do que a geologia real, e pode superestimar o volume aparente por "espalhar" a massa/magnetização por um volume modelado maior. a) está errada — a regularização é uma escolha, não uma recuperação exata da geologia; c) está errada — existem regularizações alternativas (por exemplo, impondo esparsidade); d) está errada — a petrofísica local continua sendo a forma mais eficaz de restringir o modelo; e) está errada — ela se aplica também a campos potenciais.

**5.** Resposta esperada: sim, do ponto de vista puramente matemático, ambos os modelos reproduzem a mesma anomalia observada dentro do erro de medição — é a manifestação concreta da não unicidade, já que o que o dado "vê" é, em primeira aproximação, o produto entre volume e contraste, não os dois separadamente. A **Equipe Q** toma a decisão mais bem embasada, não porque seu modelo seja mais "verdadeiro" num sentido matemático absoluto, mas porque ela ancorou a inversão numa restrição externa vinda de dado petrofísico real e local (testemunho de magnetita já confirmado), reduzindo o espaço de modelos possíveis a um subconjunto geologicamente plausível — enquanto a Equipe P deixou o contraste inteiramente a critério da preferência genérica por suavidade do algoritmo, sem verificação de plausibilidade geológica.

**6.** Falso. A inversão 3D não elimina a ambiguidade fundamental — ela apenas a expressa num espaço de modelo maior e mais realista. O que ela ganha é a possibilidade de restringir a inversão simultaneamente por múltiplos conjuntos de dados de métodos diferentes ou por um modelo geológico 3D prévio, o que é, na prática, uma forma mais rica de fazer o mesmo trabalho de regularização — reduzir o espaço de modelos matematicamente possíveis a um subconjunto geologicamente plausível, não eliminar a não unicidade em si.

**7.** Resposta: **b)**. Uma camada de evidência é uma reinterpretação do dado bruto — por exemplo, "distância a um contato interpretado" ou "presença de halo de destruição de magnetita" — em termos de sua relevância para um sistema mineral, e não o valor bruto da variável física. a) descreve o dado bruto, que ainda não é camada de evidência; c) confunde camada de evidência com o algoritmo que a usa; d) é falsa — camadas de evidência podem vir de geofísica, geoquímica, estrutura ou geologia; e) confunde camada de evidência (um insumo) com o mapa de prospectividade final (a síntese de várias camadas).

**8.** Falso. Pesos de evidência é uma técnica **intermediária**: usa a distribuição espacial de depósitos já conhecidos para calcular estatisticamente o peso de cada camada, mas ainda é supervisionada por um modelo conceitual escolhido pelo intérprete — uma ponte entre a abordagem puramente orientada por conhecimento (regras e pesos definidos a priori por especialistas) e a puramente orientada por dados (aprendizado de máquina sem definição prévia de pesos).

**9.** Resposta esperada: depósitos minerais economicamente viáveis são, por definição, extremamente raros no espaço geográfico — um conjunto de treinamento típico tem algumas dezenas de positivos contra milhares a dezenas de milhares de km² sem depósito confirmado. Os dois riscos: (1) **sobreajuste** — o modelo memoriza características específicas (inclusive irrelevantes) dos poucos depósitos conhecidos e falha em generalizar; (2) **viés de amostragem de exploração** — áreas sem depósito confirmado podem simplesmente não ter sido exploradas o suficiente, e tratar "não confirmado" como "geologicamente desfavorável" penaliza sistematicamente as fronteiras exploratórias menos estudadas, que costumam ser onde a exploração moderna mais quer buscar.

**10.** Resposta esperada: os dois problemas estruturais são (1) **desbalanceamento extremo de classes** — apenas 5 positivos contra 20.000 km² favorece forte sobreajuste, sem capacidade real de generalização; e (2) **viés de cobertura de uma camada parcial** — a camada de IP, cobrindo só 6% da área, pode fazer o algoritmo aprender a associar "ausência de dado de IP" a "ausência de depósito" nas áreas não cobertas, um artefato de amostragem de aquisição, não geológico. A correção híbrida: usar o modelo de sistema mineral para decidir, com base em conhecimento geológico (não só disponibilidade de dado), quais camadas representam evidência de fonte/transporte/deposição/preservação; tratar a camada parcial de IP separadamente (para refinar prioridade dentro da área coberta, sem enviesar o modelo regional); e complementar o aprendizado de máquina com pesos de evidência informados pelo modelo conceitual, em vez de depender exclusivamente de padrões estatísticos aprendidos de poucos exemplos positivos.

</details>
