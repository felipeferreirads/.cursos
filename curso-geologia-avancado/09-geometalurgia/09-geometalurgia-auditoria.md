# Auditoria científica — Módulo 09: Geometalurgia

**Módulo:** [[09-geometalurgia-modulo|Módulo 09 — Geometalurgia]]
**Escopo:** 6 aulas (geologia-avancado-m09-a01 a a06), 40 alegações auditáveis extraídas dos blocos de metadados de cada aula (7+6+6+8+7+6). Nenhuma alegação nova precisou ser criada: as afirmações de risco do corpo já estavam cobertas pelos `claim_id` existentes.
**Modo:** `audit-and-fix`. Todos os achados 🔴, 🟠 e 🟡 foram corrigidos no texto das aulas, nos recaps, nas listas de fontes e nos blocos de metadados antes da geração do questionário e do baralho.
**Método:** verificação de cada `claim_id` contra a literatura padrão de processamento mineral e de geometalurgia (Wills & Finch, 2016; Napier-Munn, Morrell, Morrison & Kojovic, 1996; King, 2012; Petruk, 2000; Bulatovic, 2007; Marsden & House, 2006; Gupta, 2003) e contra as publicações primárias citadas (Bond 1952 e 1961; von Rittinger 1867; Kick 1885; Taggart; Gu 2003; Sutherland & Gottlieb 1991; Fandrich et al. 2007; Gay & Morrison 2006; Mariano, Evans & Manlapig 2016; Morrell 2004; Starkey & Dobby 1996; Coward et al. 2009; Dunham & Vann 2007; David 2007; Deutsch 2013; Coward & Dowd 2015; Baum 2014; Lotter 2011 e 2018; Philander & Rozendaal 2013), **com recálculo independente e do zero de todos os seis exemplos trabalhados** e verificação prospectiva contra os Módulos 20, 21, 36, 37 e 42.
**Data:** 2026-08-30

## Resumo do veredito

| Severidade | Contagem |
|---|---|
| 🔴 Erro | 1 (corrigido antes da publicação) |
| 🟠 Impreciso | 6 (corrigidos antes da publicação) |
| 🟡 Desatualizado/a matizar | 7 (3 na primeira passagem + 4 na segunda; todos corrigidos) |
| 🔵 Sem fonte verificável | 2 (resolvidos por remoção do específico não sustentado) |
| ⚪ Convenção, atalho ou faixa qualificada | 3 |

> [!note] Duas passagens
> Este relatório cobre **duas passagens de auditoria**. A primeira (achados 🔴, 🟠, os três primeiros 🟡, os 🔵 e os ⚪) aplicou as correções às aulas mas não chegou a fechar o gate no `course-state.yaml`. A segunda passagem reverificou do zero a aritmética dos seis exemplos e a substância técnica, **confirmou que todas as correções da primeira efetivamente estão no texto**, e encontrou mais **quatro achados 🟡** — três deles resíduos de correções da primeira passagem aplicadas de forma incompleta. Estão na seção "Segunda passagem" no fim.

**Veredito geral: aprovado.** Houve **um achado vermelho** — o sentido do viés estereológico invertido na Aula 02, que ensinava ao aluno exatamente o contrário do que a medida faz, e num ponto que decide se um projeto é otimista ou conservador. Foi corrigido no corpo, em "Erros comuns", no recap e no bloco de metadados, e propagado para a Aula 03, cujo exemplo consome números de liberação medidos em seção. Junto com ele foram aplicados os seis 🟠 e os três 🟡. **Nenhum achado vermelho, laranja ou amarelo permanece em aberto**, e o gate de qualidade do plugin está satisfeito.

**Não há `open_findings`:** nenhum achado exigiu decisão do usuário. Os dois 🔵 foram resolvidos pela via legítima de remover o específico não sustentado e preservar a afirmação qualitativa — nenhuma correção foi inventada. Dois pontos de envelhecimento previsível (nomes comerciais das plataformas de mineralogia automatizada; nomes comerciais dos ensaios de baixa massa para SAG) ficam registrados como `maintenance_flags`, no padrão dos Módulos 07 e 08.

**Observação sobre a densidade de achados.** Quatro dos sete achados 🔴/🟠 são **inconsistências internas aritméticas ou terminológicas** — um número que não bate com o número da frase seguinte, um termo usado antes de definido. Isso é típico de material com muitos exemplos numéricos e é exatamente o que o recálculo independente existe para pegar. Os três exemplos trabalhados de maior consequência (Bond, dois produtos, valor por domínio) estavam **corretos na formulação e na aritmética**; os erros estavam na leitura e no arredondamento dos resultados.

---

## Achados

### 🔴 [GEOMET-M09-A02-LIMITES-005] — Sentido do viés estereológico invertido

**Aula:** 02 (propagado à Aula 03). **Claim relacionado:** limitações da análise modal automatizada por MEV.

**Achado:** o texto afirmava, em três lugares independentes, que "uma seção bidimensional corta partículas fora do centro e **subestima a liberação** tridimensional (superestima o travamento)". O sentido é o oposto.

O argumento é geométrico e de mão única. Corte uma partícula **mista** fora do plano em que as duas fases coexistem: a seção pode atravessar **só uma das fases**, e o resultado é indistinguível do corte de uma partícula genuinamente liberada. O inverso não acontece — uma partícula liberada é de uma fase só em qualquer plano, e nunca aparece como mista. Logo, todo erro de classificação empurra na mesma direção: **a seção 2D superestima a liberação** e subestima o travamento. É por isso que existem os métodos de correção estereológica (King; Gay & Morrison, 2006, validado contra tomografia) e que a microtomografia de raios X é usada quando se quer a liberação 3D sem viés.

O erro tem **agravante de inconsistência interna**: o item imediatamente anterior da mesma lista de limitações diz, corretamente, que a resolução de ~1 µm faz com que "o travamento fino é subestimado" — isto é, que a liberação é superestimada. Os dois itens vizinhos apontavam para lados opostos.

E tem **consequência de projeto invertida**, que é o motivo de a severidade ser vermelha e não laranja. Do jeito que estava escrito, o aluno concluiria que a mineralogia automatizada é **conservadora** e que a planta tende a superar a previsão. A verdade é o contrário: o número bruto de liberação é **otimista**, e um projeto que o tome ao pé da letra promete uma recuperação que a planta não entrega. Essa é precisamente a classe de erro que o Módulo 09 existe para prevenir, e o material ensinava a cometê-la.

**Correção aplicada:** ✅ item de "Limitações" reescrito com o argumento geométrico explícito (por que o viés é de mão única) e com as duas saídas nomeadas (correção estereológica; micro-CT); item de "Erros comuns" invertido e reformulado em torno da consequência de projeto ("promete ao projeto uma recuperação que a planta não entrega"); recap corrigido; `claim` `GEOMET-M09-A02-LIMITES-005` reescrito por extenso; **Gay & Morrison (2006) acrescentada à lista de fontes da Aula 02**, onde era citada no `claim` mas não constava.
**Propagação para a Aula 03:** ✅ o exemplo trabalhado da a03 consome graus de liberação medidos (52 / 71 / 86 / 94 %) e os converte em recuperação. Acrescentada ressalva explícita de que esses valores carregam o viés e de que a recuperação calculada é, portanto, **um limite superior**; a definição de grau de liberação e o recap da a03 passaram a registrar a superestimativa; `claim` `GEOMET-M09-A03-LIBERACAO-001` e `GEOMET-M09-A03-EXEMPLO-006` atualizados.
**Fonte:** literatura de correção estereológica em liberação mineral (Gay & Morrison, 2006, *Part. Part. Syst. Charact.* 23(3–4):246–253; King, 2012, cap. 2; revisões recentes de quantificação do viés e de micro-CT em *Minerals Engineering* e *Int. J. Mineral Processing*). · **Nível:** revisada por pares.
**Confiança:** alta — o resultado é unânime na literatura e decorre de um argumento geométrico elementar.

---

### 🟠 [GEOMET-M09-A05-CC-001] — Critério de concentração: faixa deslocada e uma banda inteira ausente

**Aula:** 05. **Claim relacionado:** viabilidade da separação gravítica.

**Achado:** o texto dava a regra prática como "`CC > 2,5` → separação fácil, até granulometria fina; `1,75–2,5` → viável até ~100 µm; `1,5–1,75` → difícil, só material grosso; `< 1,25` → inviável". Dois defeitos contra a tabela consagrada (Taggart, reproduzida em Wills & Finch, cap. 10):

1. A faixa `1,75–2,50` corresponde a ~**150 µm**, não a ~100 µm; e a faixa `> 2,5` tem um número, ~75 µm, que o texto substituía pela expressão vaga "granulometria fina".
2. A banda **`1,25–1,50`** — viável até ~6,35 mm, o domínio da pré-concentração em fragmentos — estava simplesmente ausente, de modo que a lista saltava de 1,50 direto para 1,25 e fazia parecer que abaixo de 1,50 não há nada. Há: há um regime inteiro de operação, e é justamente onde a separação em meio denso de pré-concentração vive.

O defeito de fundo é conceitual, e por isso a correção foi além de trocar números: o critério de concentração **não se lê sozinho**. Cada faixa de `CC` vem emparelhada com um tamanho mínimo de partícula, e é o par que decide a viabilidade. Um aluno que memorizasse só os limiares de `CC` não saberia responder à pergunta que a prática faz ("dá para separar este minério **nesta** granulometria?").

**Correção aplicada:** ✅ a regra em prosa foi substituída por uma **tabela de cinco linhas** com as duas colunas (`CC` e tamanho mínimo), completada com a banda 1,25–1,50, e fechada com a leitura do padrão ("quanto menor o `CC`, mais grossa precisa ser a partícula"); item de "Erros comuns" reforçado para nomear que o critério nunca se lê sem o tamanho; recap atualizado com a tabela condensada; `claim` reescrito; atribuição da fonte corrigida de "Taggart / Gaudin" para **Taggart**, reproduzido em Wills & Finch — a formulação e a tabela são de Taggart, e a menção a Gaudin não se sustentava.
**Confiança:** alta.

---

### 🟠 [GEOMET-M09-A04-LEIS-004] — Limite inferior de validade da equação de Bond subestimado por um fator de ~3

**Aula:** 04 (propagado à Aula 03). **Claim relacionado:** faixa de aplicação das leis de cominuição.

**Achado:** o item de "Erros comuns" advertia contra aplicar Bond fora da faixa, e situava o limite inferior em "moagem ultrafina abaixo de ~15–20 µm". A literatura de moagem fina situa esse limite bem mais alto: **abaixo de ~50 µm** a equação de Bond já deixa de descrever bem o processo, e nessa faixa ela **subestima** a energia — por causa de tamanhos de bola, trajetórias e interações bola–partícula diferentes dos do moinho convencional. É aí que entram Rittinger, a equação de Charles e o gráfico de assinatura energética (*signature plot*) levantado no próprio moinho fino.

Colocar o limite em 15–20 µm dá ao aluno uma folga de operação que não existe: toda a faixa de 20 a 50 µm — que é exatamente onde vive a remoagem de concentrados, um caso muito comum — ficava indevidamente dentro do domínio "seguro" de Bond.

**Agravante de coerência interna, e o mais interessante deste achado:** o próprio exemplo trabalhado da Aula 03 aplica Bond a `P80 = 45 µm` e obtém 19,6 kWh/t. Com o limite corrigido, esse ponto passa a estar **na borda inferior da validade** — o que o texto precisava dizer, em vez de apresentar os quatro pontos da tabela como igualmente confiáveis. A correção transformou uma inconsistência em conteúdo: o aluno agora vê um cálculo sendo feito no limite do método e sendo rotulado como tal.

**Correção aplicada:** ✅ "Erros comuns" da a04 corrigido para ~50 µm, com o sentido do desvio nomeado (subestima) e as três alternativas listadas; a definição da faixa de validade acrescentada ao próprio bloco da equação de Bond, na seção "As três leis"; recap da a04 atualizado; `claim` `GEOMET-M09-A04-LEIS-004` reescrito; **Doll (2022), "Fine grinding, a refresher", acrescentada às fontes da a04**. Na a03, o exemplo ganhou ressalva explícita de que os 19,6 kWh/t do ponto de 45 µm são indicativos e que um dimensionamento real usaria ensaio de moagem fina; `claim` da a03 atualizado.
**Confiança:** alta.

---

### 🟠 [GEOMET-M09-A06-EXEMPLO-006 · a] — "Mói ~23 % mais devagar": energia por tonelada trocada por toneladas por ano

**Aula:** 06. **Claim relacionado:** exemplo trabalhado, efeito do Work Index na capacidade.

**Achado:** a interpretação do exemplo dizia que o domínio B "recupera menos de dois terços do cobre e **mói ~23 % mais devagar**". Os 23 % vêm de `19,0/15,5 = 1,226`, que é o aumento de **energia por tonelada**. A perda de **velocidade** é o recíproco: a potência instalada é fixa, então a vazão cai por `1/1,226 = 0,816`, isto é, **~18 % menos toneladas por ano** — e é exatamente o que o item (d) do próprio exemplo havia acabado de calcular, ao obter 16,3 Mt/ano contra 20 (`16,3/20 = 0,82`). O texto contradizia, na frase de fecho, a conta que fizera duas linhas antes.

O ponto tem agravante de **consistência entre aulas**: a Aula 04 faz o mesmo raciocínio com outro par de números (Wi 15 → 19, `W` 13,0 → 16,5 kWh/t, ou +27 % de energia) e conclui corretamente "a capacidade cai ~21 %" — que é `1/1,269 = 0,788`. A a04 acertou; a a06 escorregou no mesmo passo.

**Correção aplicada:** ✅ acrescentado ao exemplo da a06 um parágrafo curto que separa explicitamente as duas grandezas, dá as duas contas lado a lado (`19,0/15,5 = 1,23` e `16,3/20 = 0,82`) e nomeia a reciprocidade como "o erro aritmético mais comum deste raciocínio"; a interpretação passou a dizer "entrega ~18 % menos toneladas por ano"; recap e `claim` atualizados com os dois percentuais e a advertência.
**Confiança:** alta.

---

### 🟠 [GEOMET-M09-A06-EXEMPLO-006 · b] — US$ 153 milhões contra US$ 150 milhões na mesma página

**Aula:** 06. **Claim relacionado:** exemplo trabalhado, superestimativa de cobre recuperável.

**Achado:** a diferença correta é `0,5148 − 0,4971 = 0,0177 Mt`, ou **17 700 t Cu**, que a US$ 8 500/t valem **US$ 150,4 milhões**. O item (c) arredondava para "0,018 Mt = 18 000 t" e **em seguida multiplicava o número arredondado**, chegando a US$ 153 milhões. A interpretação, duas linhas abaixo, e o recap, no fim da aula, ambos diziam US$ 150 milhões. A mesma aula trazia dois valores diferentes para a mesma grandeza.

Não é erro de conta: é arredondamento intermediário levado adiante como se fosse resultado. Num exemplo cuja tese é justamente a de que premissas médias produzem números que o depósito não entrega, deixar o próprio cálculo inflar 1,7 % por arredondamento é um lapso de ironia desconfortável.

**Correção aplicada:** ✅ itens (a) e (b) passaram a exibir a soma com quatro casas (`0,4320 + 0,0651 = 0,4971` e `0,4224 + 0,0924 = 0,5148`), de modo que a subtração fique verificável; item (c) reescrito com `0,0177 Mt = 17 700 t` e a multiplicação explícita `17 700 × 8 500 ≈ US$ 150 milhões`; recap corrigido de 18 000 t para 17 700 t; `claim` atualizado.
**Confiança:** alta.

---

### 🟠 [GEOMET-M09-A03-EXEMPLO-006] — Recuperação a P80 106 µm arredondada para cima, e o erro propagado para dois indicadores

**Aula:** 03. **Claim relacionado:** exemplo trabalhado, recuperação estimada por grau de liberação.

**Achado:** recálculo independente: `0,71 × 0,96 + 0,29 × 0,35 = 0,6816 + 0,1015 = 0,7831`, isto é, **78,3 %**. A linha do exemplo escrevia corretamente o resultado decimal (`= 0,783`) e então o convertia para "**78,4 %**" — arredondamento para cima de um número que arredonda para baixo. Os outros três pontos (66,7 %, 87,5 %, 92,3 %) conferem exatamente.

O décimo de ponto seria irrelevante se ficasse contido, mas ele alimenta os dois indicadores que o exemplo existe para produzir:
- `150 → 106 µm`: o ganho é **+11,6** pontos, não +11,7, e a razão é **~5,5** pontos por kWh/t, não ~5,6;
- `106 → 75 µm`: o ganho é **+9,2** pontos, não +9,1 (a razão, 3,5, não muda).

E o valor "~5,6" reaparecia no recap como um dos dois números que fecham a aula.

**Correção aplicada:** ✅ `78,4 % → 78,3 %`; as duas linhas de ganho por incremento de finura recalculadas; recap corrigido de "~5,6" para "~5,5"; `claim` `GEOMET-M09-A03-EXEMPLO-006` atualizado com a série correta e enriquecido com as quatro energias de Bond, que o `claim` original não registrava.
**Confiança:** alta.

---

### 🟠 [GEOMET-M09-A01-RECUP-003] — "Razão de concentração" usada no exemplo sem ter sido definida, ao lado de uma grandeza homônima

**Aula:** 01. **Claim relacionado:** grandezas do balanço metalúrgico.

**Achado:** a Aula 01 apresenta explicitamente "**três grandezas** que descrevem o resultado, e não devem ser confundidas" — teor, recuperação e **razão de enriquecimento** — e então, no exemplo trabalhado, escreve `Massa de concentrado = 91,0 / 0,28 = 325 t` **(razão de concentração ≈ 30,8)**, introduzindo uma quarta grandeza, nunca definida, cujo nome é quase idêntico ao da terceira.

Os dois números coexistem no mesmo exemplo e são diferentes: a razão de **concentração** é `F/C = 10 000/325 = 30,8`; a razão de **enriquecimento** é `c/f = 28/1,00 = 28`. Ambos são da ordem de 30, o que torna a confusão fácil e difícil de detectar. A Aula 05 define as duas corretamente, mas quatro aulas depois — e um flashcard gerado a partir do exemplo da a01 sairia com o rótulo errado.

Registro que o número `30,8` está **correto** para a grandeza que ele de fato é. O defeito é de nomenclatura não introduzida, não de aritmética.

**Correção aplicada:** ✅ a lista de grandezas da a01 passou de três para quatro itens, com a razão de concentração definida (`F/C`) e a advertência explícita de que não se confunde com a de enriquecimento (`c/f`), remetendo à formalização da Aula 05; o exemplo passou a exibir **as duas razões lado a lado** com as fórmulas (`F/C = 10 000/325 ≈ 30,8`; `c/f = 28/1,00 = 28`), o que converte o defeito em oportunidade de contraste; recap da a01 atualizado; `claims` `GEOMET-M09-A01-RECUP-003` e `GEOMET-M09-A01-EXEMPLO-007` atualizados.
**Confiança:** alta.

---

### 🟡 [GEOMET-M09-A04-WI-VALORES-006] — Faixas de Work Index cujos exemplos de rocha não cabem nelas

**Aula:** 04. **Claim relacionado:** valores típicos de Wi.

**Achado:** as três faixas dadas eram razoáveis como ordens de grandeza, mas os exemplos de rocha atribuídos a cada uma não batem com as compilações derivadas das tabelas de Bond:

| Rocha | Onde a aula a colocava | Valor tabelado (kWh/t, base métrica) |
|---|---|---|
| Granito | 12–16 | ~16–16,5 (acima da faixa) |
| Quartzito | 12–16 | ~11 (abaixo da faixa) |
| Diorito | 18–22 | ~23 (acima da faixa) |
| Barita | 5–11 | ~5,8 ✅ |
| Basalto | 18–22 | ~19 ✅ |

Granito e quartzito estavam na mesma faixa embora estejam separados por ~5 kWh/t, e o diorito — que é a rocha comumente citada como o extremo duro das tabelas — ficava fora do topo da faixa que deveria representá-lo. Num material que usa o Wi como variável central, isso desmonta a intuição de ordem de grandeza que a lista existe para construir.

Registro um segundo ponto, de armadilha real: **as compilações publicadas divergem entre si**, em parte porque as tabelas originais de Bond estão em kWh por **tonelada curta** e nem toda reprodução converte para a base métrica (fator 1,102). Um aluno que compare duas fontes sem conferir a base concluirá que uma delas está errada.

**Correção aplicada:** ✅ a lista em prosa foi substituída por uma **tabela de quatro faixas** (moles ~5–10; intermediários ~11–16; duros ~16–20; muito duros e tenazes ~20–25), com cada rocha reposicionada e acompanhada do seu valor aproximado, e com os minérios sulfetados de Cu (~12–15) destacados por serem o caso de uso do módulo. Acrescentadas três advertências: que o Wi é resultado de ensaio e não constante de litologia (com o gancho para a variabilidade que a geometalurgia mapeia), que as compilações divergem pela base de massa, e que a tabela serve para julgar plausibilidade e nunca para substituir o ensaio. Recap da a04 atualizado com os extremos (~6 a ~23) e a faixa dos sulfetados de Cu; `claim` reescrito.
**Confiança:** alta quanto ao desalinhamento; média-alta quanto aos valores individuais, que variam entre compilações — motivo pelo qual a correção adota faixas e o texto instrui a conferir a base.

---

### 🟡 [GEOMET-M09-A05-MAGNETICA-002] — Magnetita classificada como ferromagnética

**Aula:** 05. **Claim relacionado:** separação magnética de baixa intensidade.

**Achado:** o texto dizia que a LIMS "separa minerais **ferromagnéticos**, sobretudo magnetita". Magnetita é **ferrimagnética**: tem subredes magnéticas antiparalelas e desiguais, com momento líquido não nulo — o que produz atração forte, como no ferromagnetismo, mas por um mecanismo distinto. O mesmo vale para a pirrotita monoclínica.

A literatura de processamento mineral usa "ferromagnético" em sentido amplo para a classe dos fortemente magnéticos, e nesse contexto o uso é defensável — motivo de o achado ser 🟡 e não 🟠. O que o torna corrigível é o **contexto curricular**: este curso tem os Módulos 36 e 37 (microscopia e petrografia de minério), onde as propriedades magnéticas das fases opacas são lidas com o rigor da mineralogia, e tem geofísica e magnetismo de rochas nos Módulos 16 a 19. Deixar o termo impreciso aqui prepara uma colisão com módulos que ainda vão ser escritos.

**Correção aplicada:** ✅ o item passou a dizer "minerais **fortemente magnéticos**, sobretudo magnetita e pirrotita monoclínica", com uma cláusula que registra o uso amplo da literatura de processamento, a designação rigorosa (ferrimagnética), o mecanismo em uma linha (subredes antiparalelas e desiguais) e o motivo de a distinção importar. A pirrotita foi acrescentada por coerência com a Aula 02, que a lista entre as gangas problemáticas — e cuja rota usual de remoção é justamente a magnética. Campo do tambor ajustado de ~0,1–0,3 T para **~0,1–0,4 T na superfície**, faixa efetivamente reportada. Recap e `claim` atualizados.
**Confiança:** alta.

---

### 🟡 [GEOMET-M09-A02-SISTEMAS-003] — Panorama das plataformas de mineralogia automatizada incompleto e sem sinalização de volatilidade

**Aula:** 02. **Claim relacionado:** MLA, QEMSCAN e TIMA.

**Achado:** a aula listava três plataformas (MLA, QEMSCAN, TIMA) e atribuía corretamente as origens — MLA no JKMRC (Gu, 2003), QEMSCAN derivado do QEM\*SEM da CSIRO (Sutherland & Gottlieb, 1991), TIMA da Tescan. Duas lacunas:

1. O mercado atual inclui pelo menos **Mineralogic (Zeiss)** e **AMICS (Bruker)**, ausentes da lista. Um aluno que encontrasse esses nomes num relatório de laboratório não os reconheceria como a mesma técnica.
2. A **propriedade das plataformas migrou** — o MLA passou do JKMRC pela FEI e está sob a Thermo Fisher; o QEMSCAN percorreu CSIRO → Intellection → FEI → Thermo Fisher — e o texto não sinalizava que se trata de conteúdo comercial volátil. É o tipo exato de item que envelhece sem aviso.

**Correção aplicada:** ✅ Mineralogic e AMICS acrescentados à lista; inserido callout `[!warning] Nomes comerciais envelhecem` registrando as duas trajetórias de propriedade, afirmando o que **não** muda (o princípio BSE + EDS e a natureza dos produtos) e instruindo a confirmar a plataforma que o laboratório de fato opera antes de especificar um ensaio; `claim` reescrito e seu `risk` alterado de `fato` para **`desatualizavel`**. Registrado também como `maintenance_flag` do módulo.
**Confiança:** alta.

---

### 🔵 [GEOMET-M09-A03-P80-005] — "Dobrar a geração de lama fina" entre 75 e 45 µm

**Aula:** 03. **Claim:** interpretação do exemplo trabalhado.

**Achado:** a interpretação afirmava que passar de P80 75 µm para 45 µm custa cerca de um ponto de recuperação por kWh/t "além de **dobrar** a geração de lama fina". O fator 2 é uma quantidade específica e verificável, e não é derivável dos dados do exemplo: a fração abaixo de 10–20 µm depende da **inclinação da distribuição granulométrica** do produto, que o P80 sozinho não determina — dois produtos com o mesmo P80 e distribuições de inclinações diferentes têm frações de ultrafinos bem diferentes. Não encontrei fonte que sustente o fator 2 como regra geral, e a afirmação qualitativa (a fração ultrafina aumenta, e isso pesa) é sólida e suficiente.

**Correção aplicada:** ✅ o específico não sustentado foi **removido** e substituído pela formulação qualitativa com a razão explícita: "ainda aumenta a fração ultrafina — quanto, depende da inclinação da distribuição granulométrica, e não se lê do P80 sozinho". Nenhuma correção foi inventada: a afirmação verificável saiu, a afirmação sustentada ficou, e o aluno ganhou o motivo pelo qual o número não pode ser dado. Não gera `open_finding`.
**Confiança:** alta quanto à não verificabilidade do fator 2.

---

### 🔵 [GEOMET-M09-A03-CURVAS-004] — "Tipicamente 95–97 %" para a recuperação das partículas liberadas

**Aula:** 03. **Claim:** projeção da recuperação a partir da curva de liberação.

**Achado:** o texto apresentava "tipicamente 95–97 % na flotação de um mineral bem condicionado" como se fosse uma faixa medida e tabelada. É, na prática, uma **hipótese de modelagem**: o valor adotado para a eficiência do concentrador sobre partículas liberadas num modelo de recuperação por liberação. Varia com o mineral, o circuito, o número de estágios e a definição de "bem condicionado", e não encontrei fonte que a estabeleça como faixa de referência. O exemplo da própria aula usa `0,96`, coerentemente — o que confirma a natureza de parâmetro de modelo.

**Correção aplicada:** ✅ reescrito com a incerteza explícita: "nos modelos de projeto adota-se tipicamente 95–97 % para um sulfeto bem condicionado, **hipótese de modelagem e não constante medida**". A afirmação permanece, com o seu estatuto correto. Não gera `open_finding`.
**Confiança:** alta quanto ao estatuto; média quanto à faixa, que é plausível e de uso corrente.

---

### ⚪ [GEOMET-M09-A03-LIBERACAO-001] — O limiar de liberação e as duas definições

**Aula:** 03. **Claim:** definição de partícula liberada e de grau de liberação.

**Achado:** a aula dizia "na prática, adota-se ≥ 90 % ou ≥ 95 %", o que já reconhece corretamente a divergência. Duas ressalvas de baixo risco que valia explicitar, porque ambas são fonte silenciosa de comparação indevida entre laboratórios:

1. O limiar é **convenção**, não propriedade: um mesmo produto de moagem tem graus de liberação diferentes medidos a 90 % e a 95 %, e comparar valores de fontes distintas sem conferir o limiar é comparar coisas diferentes.
2. Há **duas definições** correntes — liberação por *composição* (fração do volume da partícula) e por *superfície exposta* (fração da superfície). A flotação, que age na superfície, responde à segunda; a gravítica e a magnética, que agem na massa, respondem à primeira. A própria aula já usava implicitamente essa distinção ao dizer que a flotação recupera mistas "que tenham mineral-alvo exposto" enquanto a gravítica responde à densidade "média" da partícula — mas sem nomear que se trata de duas definições de liberação.

**Correção aplicada:** ✅ enriquecimento de baixo risco — acrescentado parágrafo curto com as duas advertências e a convenção de leitura ("salvo aviso, 'grau de liberação' é o de composição"); recap e `claim` atualizados. A definição original não estava errada; ganhou precisão.
**Confiança:** alta.

---

### ⚪ [GEOMET-M09-A02-EXEMPLO-006] — Teor de cobre da crisocola tratado como constante do mineral

**Aula:** 02. **Claim:** exemplo trabalhado de partição.

**Achado:** a tabela do exemplo dá calcopirita a 34,6 % Cu e calcosita a 79,9 % Cu — que conferem exatamente com a estequiometria (CuFeS₂: 63,55/183,53 = 34,63 %; Cu₂S: 127,10/159,17 = 79,85 %) — e crisocola a 36,0 % Cu, apresentada no mesmo formato, como se fosse igualmente uma constante. Não é. A fórmula aceita, `Cu₂₋ₓAlₓ(H₂₋ₓSi₂O₅)(OH)₄·nH₂O`, tem Cu, Al e água variáveis, e o teor real oscila em torno de 30–38 %. Os 36,0 % são plausíveis para uma composição ideal hidratada, e como **valor medido nesta amostra** a tabela está correta — mas o aluno não tinha como saber que uma das três linhas tem natureza diferente das outras duas.

**Correção aplicada:** ✅ enriquecimento de baixo risco — acrescentado parágrafo curto sob a tabela distinguindo os dois valores estequiométricos do valor medido, dando a fórmula da crisocola e a faixa, e fechando com a consequência prática (é por isso que a análise modal precisa vir com o EDS quantitativo da fase, e não só com a fórmula de biblioteca). `claim` atualizado com a ressalva. Os números do exemplo **não mudam**.
**Confiança:** alta.

---

### ⚪ [GEOMET-M09-A04-ENERGIA-001] — Repartição da energia de cominuição

**Aula:** 04. **Claim:** participação da cominuição no consumo de energia.

**Achado:** as três afirmações foram verificadas e são todas defensáveis, com a ressalva de que as fontes divergem nas margens: (a) "30 a 50 % — às vezes mais — do consumo de energia elétrica" de uma planta de flotação é a faixa clássica para o concentrador, e levantamentos de sítio reportam a cominuição como o maior consumidor isolado, por vezes acima de 50 % da energia da mina — o "às vezes mais" cobre isso; (b) "alguns pontos percentuais de toda a eletricidade gerada" — as estimativas publicadas variam de ~2 % a ~3 % ou mais, e a formulação vaga é a honesta; (c) "abaixo de 1 a 2 %" de conversão em superfície nova é o valor consagrado.

**Correção proposta:** nenhuma. As três já estão qualificadas na medida certa, e substituir a faixa por um número único pioraria o material.
**Confiança:** média-alta — o intervalo publicado é genuinamente amplo, e o texto reflete isso.

---

## Verificação independente dos exemplos trabalhados

Todos os seis foram recalculados do zero, sem reutilizar os resultados publicados.

- **Aula 01 — dois blocos de mesmo teor, recuperações diferentes.** `m_Cu = 10 000 × 0,0100 = 100 t`. Bloco A: `100 × 0,91 = 91,0 t`; `91,0 × 8 500 = US$ 773 500`; `91,0/0,28 = 325 t` de concentrado; `10 000/325 = 30,77`. Bloco B: `63,0 t`; `US$ 535 500`; `63,0/0,24 = 262,5 → 263 t`. Diferença: `28,0 t Cu` e `US$ 238 000`; `238 000/773 500 = 30,8 % ≈ 31 %`. **Confere integralmente.** ✅ Ver achado 🟠 quanto ao rótulo da razão de concentração.
- **Aula 02 — partição e teto de flotação.** `2,20 × 0,346 = 0,7612`; `0,18 × 0,799 = 0,1438`; `0,25 × 0,360 = 0,0900`; `+ 0,0300`. Total `1,0250 % Cu`. Partição: `74,24 / 14,05 / 8,78 / 2,93 %`. Sulfetos `= 88,2 %`; `0,882 × 0,95 = 0,8379 → 83,8 %`. Não sulfetados `= 11,7 %`. **Confere integralmente.** ✅ Teores estequiométricos de calcopirita e calcosita conferidos contra as massas atômicas; ver ⚪ quanto à crisocola.
- **Aula 03 — liberação, recuperação e energia.** As quatro energias de Bond foram recalculadas com `Wi = 14`, `F80 = 12 000 µm` (`1/√12000 = 0,0091287`): `P80 150 → 140 × 0,072521 = 10,15`; `106 → 12,32`; `75 → 14,89`; `45 → 19,59`. **As quatro conferem** com os 10,2 / 12,3 / 14,9 / 19,6 publicados. ✅ As recuperações: `66,72 / 78,31 / 87,46 / 92,34 %` — o segundo ponto **não conferia** (78,4 publicado). ⚠️ **corrigido**, ver achado 🟠, com os dois indicadores derivados.
- **Aula 04 — energia específica, custo e capacidade.** `1/√106 = 0,0971286`; `1/√9000 = 0,0105409`; `150 × 0,0865877 = 12,99 → 13,0 kWh/t`. (b) `150 × 0,1049292 = 15,74 → 15,7`; `(15,7−13,0)/13,0 = 20,8 % ≈ +21 %`; `(106−75)/106 = 29,2 % ≈ 29 %`. (c) `2,7 × 12×10⁶ = 3,24×10⁷ kWh`; `× 0,09 = US$ 2,916×10⁶ ≈ 2,9 milhões`. (d) `190 × 0,0865877 = 16,45 → 16,5`; `12 × 13,0/16,5 = 9,45 ≈ 9,5 Mt/ano`; `(12−9,45)/12 = 21,2 % ≈ 21 %`. **Confere integralmente**, e a passagem de energia para capacidade está feita corretamente — é a mesma que a Aula 06 errava. ✅
- **Aula 05 — fórmula de dois produtos e balanço.** `f−t = 0,778`; `c−t = 27,428`; `R = (27,5 × 0,778)/(0,85 × 27,428) = 21,395/23,3138 = 0,91769 → 91,8 %`. `K = 27,428/0,778 = 35,25 → 35,3`. Enriquecimento `= 27,5/0,85 = 32,35 → 32,4`. Verificação em base 1 000 t: `8,50 t` alimentados; `1 000/35,3 = 28,33 t` de concentrado × `0,275 = 7,79 t`; `971,7 × 0,00072 = 0,700 t`; soma `8,49 t`. Cenário `t = 0,050`: `R = 22,00/23,3325 = 0,94290 → 94,3 %`; ganho `2,5` pontos; `0,025 × 8,50 = 0,2125 t`; `× 8 500 = US$ 1 806`; `× 30 = US$ 54 180/dia`. **Confere integralmente**, incluindo a cadeia econômica final. ✅ A derivação da fórmula a partir dos dois balanços está correta, e a afirmação de que ela dispensa as vazões — o motivo de existir — está corretamente colocada.
- **Aula 06 — valor por domínio e capacidade.** `60 × 0,0080 × 0,90 = 0,4320`; `15 × 0,0070 × 0,62 = 0,0651`; total `0,4971 Mt`. Premissa única: `0,4224 + 0,0924 = 0,5148 Mt`. Diferença `0,0177 Mt = 17 700 t`, `× 8 500 = US$ 150,45×10⁶`. ⚠️ **corrigido** (publicava US$ 153 milhões contra US$ 150 no recap — achado 🟠). Capacidade: `20 × 15,5/19,0 = 16,32 Mt/ano`; `15/16,32 = 0,919 ano` contra `15/20 = 0,75`, diferença `0,17 ano ≈ 2 meses`. **Confere.** ✅ Teor médio do modelo de recursos: `(60×0,80 + 15×0,70)/75 = 58,5/75 = 0,78 %` — **confere**. ✅ ⚠️ A leitura do efeito de capacidade estava trocada — achado 🟠, **corrigido**.

## Verificação de fórmulas, atribuições e datas

- **Equação de Bond** `W = 10·Wi·(1/√P80 − 1/√F80)`, com tamanhos em µm e `W` em kWh/t — forma métrica correta. ✅ A auto-consistência declarada na aula foi verificada: com `F80 → ∞` e `P80 = 100 µm`, `W = 10·Wi·(1/10) = Wi`, o que confirma tanto a constante 10 quanto a definição do Wi a 100 µm. Registro que circulam reproduções com "76 µm" ou "74 µm" (confusão com a malha 200 mesh); **a aula usa 100 µm, que é o correto**, e a auto-consistência prova. ✅
- **As três leis como casos de `dE = −C·dx/xⁿ`** — integração conferida: `n = 2` → `E ∝ (1/P − 1/F)` (Rittinger, área nova); `n = 1` → `E ∝ ln(F/P)` (Kick, razão de redução); `n = 1,5` → `E ∝ (1/√P − 1/√F)` (Bond). ✅
- **Atribuições e datas:** **von Rittinger 1867** ✅, **Kick 1885** ✅, **Bond 1952** ✅ — e confirmado que Bond chamou a sua de "terceira teoria da cominuição" por contar as de von Rittinger e Kick como a primeira e a segunda, fato acrescentado à aula por ser um gancho mnemônico gratuito. **Bond (1952)**, *Trans. AIME* 193:484–494, e **Bond (1961)**, *British Chemical Engineering* 6(6):378–385 e 6(8):543–548 — conferem. ✅
- **Ensaio de moabilidade de Bond:** moinho **305 × 305 mm** (12" × 12") ✅, ciclo fechado simulando **250 %** de carga circulante ✅, alimentação britada abaixo de **3,35 mm** (6 mesh) ✅, ~10 kg ✅.
- **Testes de baixa massa:** **JK DWT** (parâmetros `A` e `b`, ~75 kg em várias frações) ✅; **SMC Test** (Morrell, fração única, índice **DWi** em kWh/m³, poucos quilos, aceita fragmentos de testemunho) ✅; **SPI** (tempo em minutos para moer a P80 1,7 mm, ~2 kg) ✅. **Morrell (2004)**, *Minerals Engineering* 17(3):447–451 ✅; **Starkey & Dobby (1996)**, SAG 1996 ✅.
- **Fórmula de dois produtos** `R = c(f−t)/[f(c−t)]` — derivada independentemente dos dois balanços e conferida. ✅ `K = F/C = (c−t)/(f−t)` ✅; razão de enriquecimento `c/f` ✅.
- **Critério de concentração** `CC = (ρ_p − ρ_f)/(ρ_l − ρ_f)` — forma correta ✅; faixas corrigidas, ver achado 🟠; atribuição corrigida para **Taggart**.
- **Cinética de flotação de primeira ordem** `R(t) = R_∞(1 − e^(−kt))` ✅, com `R_∞` limitada por liberação e mineralogia ✅.
- **Equação de Elsner** `4 Au + 8 NaCN + O₂ + 2 H₂O → 4 Na[Au(CN)₂] + 4 NaOH` — balanceada e correta. ✅
- **Gu (2003)**, *JMMCE* 2(1):33–41, MLA no JKMRC ✅; **Sutherland & Gottlieb (1991)**, *Minerals Engineering* 4(7–11):753–762, QEM\*SEM da CSIRO ✅; **Fandrich et al. (2007)**, *IJMP* 84(1–4):310–320 ✅; **Gay & Morrison (2006)** ✅. Ver 🟡 quanto ao panorama comercial.
- **Coward, Vann, Dunham & Stewart (2009)**, "The primary-response framework for geometallurgical variables", Seventh International Mining Geology Conference, AusIMM — confere, **inclusive o ponto que a Aula 06 lhe atribui**: o framework trata explicitamente a não aditividade das respostas metalúrgicas como a complicação central da predição. ✅ **Dunham & Vann (2007)**, **David (2007)**, **Deutsch (2013)**, **Coward & Dowd (2015)**, **Philander & Rozendaal (2013)** — conferem quanto a autoria, veículo e objeto. ✅
- **Mariano, Evans & Manlapig (2016)**, *Minerals Engineering* 94:51–60 — confere como revisão da quebra aleatória × não aleatória, e sustenta a caracterização da fratura não preferencial como o caso geral. ✅

## Verificação de conteúdo técnico não coberto por claim específico

- **Estágios de britagem** (primária giratório/mandíbulas, ROM ~1 m → 150–200 mm, razão 3–6; secundária/terciária cônicos e rolos → 10–25 mm): conferem. ✅
- **HPGR** como britagem por leito de partículas, mais eficiente e indutora de microfissuras que beneficiam moagem e lixiviação: confere, e a ressalva em "O que não concluir" (depende de dureza, umidade e preço) é correta e bem colocada. ✅
- **Moinho SAG com 4–15 % de bolas**, circuitos **SAB** e **SABC** com britagem de *pebbles*, **AG** sem bolas, verticais (torre, Vertimill, IsaMill) para remoagem: conferem. ✅
- **Circuito fechado com hidrociclone**, *underflow* grosso ao moinho e *overflow* fino à concentração, **carga circulante 200–350 %**: confere. ✅
- **Definição de P80** como abertura pela qual passam 80 % da massa: confere, e é usada de forma consistente nas quatro aulas em que aparece. ✅
- **Janela de tamanho da flotação** (grossas acima de ~150–300 µm descolam por peso; ultrafinas abaixo de ~10 µm colidem pouco): confere com as faixas usuais. ✅
- **Reagentes de flotação** — xantatos e ditiofosfatos para sulfetos; ácidos graxos e aminas para não sulfetos; MIBC e glicóis como espumantes; cal deprimindo pirita; cianeto deprimindo esfalerita e pirita; CMC e quebracho deprimindo talco; CuSO₄ ativando esfalerita para o xantato: **todos conferem**, inclusive os pares depressor/mineral, que são o ponto mais fácil de errar do bloco. ✅ A separação funcional entre coletor e espumante, tratada duas vezes (corpo e "Erros comuns"), está correta e é a confusão certa a antecipar. ✅
- **Circuito rougher / scavenger / cleaner** e o papel de cada um: conferem. ✅
- **Rotas de lixiviação** — pilha (Cu oxidado e secundário com H₂SO₄ + SX-EW; Au com cianeto diluído), tanque agitado (CIL/CIP, Zn, U), pressão (POX; HPAL para Ni laterítico): conferem. ✅ **Biolixiviação** por acidófilos do gênero *Acidithiobacillus* e afins, em pilhas de calcosita e pré-tratamento de concentrados refratários: confere. ✅
- **Ouro refratário** como encapsulamento submicroscópico em pirita/arsenopirita, e *preg-robbing* por carbono natural como fenômeno distinto: conferem, e a insistência de que é diagnóstico mineralógico e não falha de reagente é correta e é o gancho certo para a Aula 02. ✅
- **WHIMS/HGMS a 1–2 T ou mais** para paramagnéticos fracos (hematita, ilmenita, wolframita, monazita, granada): confere. ✅
- **Minerais de ganga problemáticos** — carbonatos consumindo ácido; pirita e pirrotita consumindo O₂, cal e coletor; talco, micas e argilas hidrofóbicos ou geradores de lama; arsenopirita e fluorita como portadores de penalizantes: conferem. ✅ Registro que **crocoíta** (PbCrO₄) é exemplo pouco usual num contexto de penalizantes de concentrado — é rara demais para ter relevância industrial —, mas a afirmação não é falsa e o item traz outros dois exemplos corretos; não corrigido.
- **DRX** com refinamento de Rietveld, perda de sensibilidade abaixo de ~1–2 % em massa e cegueira a fases amorfas: confere, e o exemplo de fases amorfas dado em "Erros comuns" (crisocola, ferridrita, geles de sílica) é apropriado. ✅
- **Contraste BSE proporcional ao número atômico médio**, com sulfetos claros, silicatos escuros e óxidos intermediários: confere. ✅
- **Produtos da mineralogia automatizada** (modal, partição elementar, associação por contato de fronteira, distribuição de tamanho de grão, liberação por classe, textura quantitativa): conferem. ✅
- **Fratura não preferencial (transgranular) como o caso geral** dos minérios silicáticos e sulfetados, e **descolamento** (intergranular ou por fase frágil) como o caso favorável explorado por fragmentação de alta tensão e moagem seletiva: conferem com Mariano et al. (2016). ✅
- **Não aditividade** — teor aditivo e krigável; Wi e recuperação não aditivos, com a moabilidade da blenda tendendo a ser pior que a média (o componente duro domina o tempo de residência) e a recuperação da blenda podendo cair abaixo da média por interação de gangas e reagentes: conferem com Coward et al. (2009) e Deutsch (2013), e a conclusão prática (não krigar diretamente; modelar a partir de proxies aditivas ou simular) é a recomendação corrente da literatura. ✅ **É o conteúdo mais importante do módulo e está correto.**
- **Domínio geológico ≠ domínio geometalúrgico**, validado por dados de processo: confere com Coward et al. (2009) e Philander & Rozendaal (2013). ✅
- **Viés otimista do VPL** sob premissa de recuperação e capacidade médias únicas, e a associação com rampas de produção lentas: confere com Dunham & Vann (2007) e David (2007). ✅
- **Lógica do programa geometalúrgico** — muitos ensaios de bancada para mapear, poucos de piloto para calibrar; amostragem estratificada por domínio; caráter destrutivo do teste competindo pelo testemunho: conferem. ✅

## Consistência cruzada

Verificação prospectiva solicitada. **Os Módulos 20, 21, 36, 37 e 42 estão todos com `status: pending` e nenhuma aula escrita** — não há, portanto, contradição possível a detectar hoje. O que foi feito foi conferir que o Módulo 09 não **fixa** definições que esses módulos vão precisar contrariar.

| Conceito | Módulo que vai formalizar | Uso no Módulo 09 | Situação |
|---|---|---|---|
| Krigagem, estimador linear, modelo de blocos | M20 e M21 (pendentes); herdado do módulo de recursos do **curso base** | A06 ("Antes de começar" e "Não aditividade") | ✅ compatível — a a06 usa apenas a propriedade de **linearidade**, que é o que M20 vai estabelecer, e não antecipa nenhum resultado. Acrescentado ponteiro explícito no ponto de uso (ver revisão didática) |
| Simulação geoestatística | M21 (pendente) | A06 (mencionada como alternativa) | ✅ compatível — citada pelo nome como saída possível, sem ser usada nem definida |
| Amostragem, suporte, domínios de estimativa | M20 e M21 (pendentes) | A01 (programa), A06 (domínios) | ✅ compatível — o M09 trata domínio **geometalúrgico** (resposta de processo) e é explícito em distingui-lo do domínio geológico; não colide com "domínio de estimativa" no sentido geoestatístico |
| Propriedades magnéticas de fases opacas | M36 e M37 (pendentes) | A05 (LIMS/WHIMS) | ⚠️ **divergiria** ("ferromagnético" para magnetita) — corrigido preventivamente, ver 🟡 `MAGNETICA-002` |
| Texturas de minério (exsolução, substituição, inclusão) | M37 (pendente) | A03 (tamanho de grão herdado da história geológica) | ✅ compatível — a a03 usa os termos no sentido petrográfico corrente (lamelas de pentlandita em pirrotita como exemplo de exsolução, correto) |
| Microscopia de luz refletida | M36 (pendente) | A02 ("Métodos clássicos") | ✅ compatível, e bem calibrado: a a02 a trata como insubstituível para o primeiro diagnóstico e como calibração da biblioteca automatizada, não como técnica superada |
| Recurso, reserva, códigos de reporte | M42 (pendente) | A01 e A06 (VPL, sequenciamento) | ✅ compatível — o M09 fala de valor e sequenciamento sem entrar em classificação de recursos, que é o objeto do M42 |

**Consistência interna do módulo** (a que efetivamente rendeu achados): o `P80` é definido na a03 e reutilizado sem redefinição nas a04 e a06 ✅; `Wi` é definido na a04 e reutilizado na a06 ✅; recuperação é definida na a01, tem seu teto por partição fixado na a02, seu teto por liberação na a03 e sua medição na a05 — cadeia coerente ✅; a passagem energia-por-tonelada → toneladas-por-ano é feita na a04 e na a06, e **divergia** entre as duas — corrigido, ver 🟠. A razão de concentração era usada na a01 e definida só na a05 — corrigido, ver 🟠.

## Cobertura de objetivos de aprendizagem

| Objetivo | Aulas que cobrem | Verificado |
|---|---|---|
| geologia-avancado-m09-oa01 | a01, a02 | ✅ |
| geologia-avancado-m09-oa02 | a03 | ✅ |
| geologia-avancado-m09-oa03 | a04, a05 | ✅ |
| geologia-avancado-m09-oa04 | a06 | ✅ |

Os quatro objetivos têm cobertura efetiva, e o `mapa_objetivo_secao` de cada aula corresponde ao conteúdo realmente desenvolvido. Nenhum objetivo ficou sem alegações auditáveis correspondentes, e — ao contrário do Módulo 08 — nenhum objetivo é prometido sem seção que o ensine.

## Pontos de manutenção periódica

Registrados como `maintenance_flags` do módulo no `course-state.yaml`, no padrão dos Módulos 07 e 08. Não bloqueiam o gate: são conteúdo correto hoje, que envelhece de forma previsível e já está sinalizado na própria aula.

1. **Plataformas de mineralogia automatizada (Aula 02)** — MLA, QEMSCAN, TIMA, Mineralogic, AMICS. Marcas e proprietários migram; a aula traz callout de advertência explícito e o `claim` está marcado `risk: desatualizavel`.
2. **Ensaios de baixa massa para SAG (Aula 04)** — SMC Test/DWi, SPI, JK DWT e as metodologias de dimensionamento (Morrell, SAGDesign) são **produtos comerciais** de laboratórios específicos, sujeitos a mudança de nome, de protocolo e de disponibilidade. O conteúdo físico (o SAG quebra por impacto e o Wi de Bond não descreve isso) é estável; os nomes não.

## Correções aplicadas

**Aplicadas em:** 2026-08-30

| claim_id | Sev. | Desfecho | Arquivos alterados |
|---|---|---|---|
| `GEOMET-M09-A02-LIMITES-005` | 🔴 | Corrigido | aula-02, aula-03 (propagação) |
| `GEOMET-M09-A05-CC-001` | 🟠 | Corrigido | aula-05 |
| `GEOMET-M09-A04-LEIS-004` | 🟠 | Corrigido | aula-04, aula-03 (propagação) |
| `GEOMET-M09-A06-EXEMPLO-006` (a) | 🟠 | Corrigido | aula-06 |
| `GEOMET-M09-A06-EXEMPLO-006` (b) | 🟠 | Corrigido | aula-06 |
| `GEOMET-M09-A03-EXEMPLO-006` | 🟠 | Corrigido | aula-03 |
| `GEOMET-M09-A01-RECUP-003` | 🟠 | Corrigido | aula-01 |
| `GEOMET-M09-A04-WI-VALORES-006` | 🟡 | Corrigido | aula-04 |
| `GEOMET-M09-A05-MAGNETICA-002` | 🟡 | Corrigido | aula-05 |
| `GEOMET-M09-A02-SISTEMAS-003` | 🟡 | Corrigido · `maintenance_flag` | aula-02 |
| `GEOMET-M09-A03-P80-005` | 🔵 | Corrigido com ressalva (específico removido) | aula-03 |
| `GEOMET-M09-A03-CURVAS-004` | 🔵 | Corrigido com ressalva (estatuto explicitado) | aula-03 |
| `GEOMET-M09-A03-LIBERACAO-001` | ⚪ | Enriquecido (baixo risco) | aula-03 |
| `GEOMET-M09-A02-EXEMPLO-006` | ⚪ | Enriquecido (baixo risco) | aula-02 |
| `GEOMET-M09-A04-ENERGIA-001` | ⚪ | Aceito como está | — |
| `GEOMET-M09-A04-SAG-TESTES-007` | — | `maintenance_flag` (sem achado) | — |

**Arquivos tocados:** as seis aulas (`09-geometalurgia-aula-01` a `-06`), este relatório, o hub do módulo e o `course-state.yaml`. **Não há material derivado a propagar:** questionário e flashcards ainda não existem — esta auditoria é o gate que os precede, que é exatamente a ordem que evita um baralho nascer com o viés estereológico invertido.

**Pendências:** nenhuma. Nenhum achado aguarda decisão do usuário.

## Recomendação

**Aprovar o módulo para avaliação (questionários) e memorização (flashcards).** O achado 🔴, os seis 🟠 e os três 🟡 foram aplicados ao texto das aulas, aos recaps, às listas de fontes e aos blocos de metadados, de modo que **nenhum achado vermelho, laranja ou amarelo permanece em aberto** e não há `open_findings`. Os dois 🔵 foram resolvidos por remoção do específico não sustentado, sem invenção de correção; os três ⚪ são convenções e faixas qualificadas, duas delas enriquecidas com ressalva de baixo risco.

Cinco advertências para quem gerar a avaliação e o baralho:

- **O sentido do viés estereológico inverteu.** Qualquer questão ou flashcard sobre limitações da mineralogia automatizada deve dizer que a seção 2D **superestima** a liberação. Um card gerado a partir da versão anterior estaria ensinando o oposto do correto, e este é o item de maior risco de propagação do módulo inteiro. **Distrator natural, e excelente:** "subestima a liberação".
- **A Aula 03 mudou de números.** A recuperação a P80 106 µm é **78,3 %** (não 78,4), o ganho de 150→106 µm é **+11,6 pontos** e a razão é **~5,5 pontos por kWh/t** (não 5,6). O recap também mudou.
- **A Aula 06 mudou dois números e uma conclusão.** A superestimativa é **17 700 t Cu ≈ US$ 150 milhões** (não 18 000 t / US$ 153 milhões), e o efeito do Wi maior é **~23 % mais energia por tonelada e ~18 % menos toneladas por ano** — as duas grandezas são recíprocas e a distinção agora está no texto. Uma questão que peça ao aluno para converter uma na outra cobre exatamente o achado.
- **O critério de concentração agora tem cinco faixas, cada uma com um tamanho de partícula.** Questão que cobre só o limiar de `CC` sem o tamanho perde o ponto que a correção introduziu. Os valores corretos: >2,5 → ~75 µm; 1,75–2,50 → ~150 µm; 1,50–1,75 → ~1,7 mm; 1,25–1,50 → ~6,35 mm; <1,25 → inviável.
- **Não cobrar Bond abaixo de ~50 µm** como se fosse aplicação de rotina — a aula agora ensina que é o limite inferior de validade. E não cobrar a tabela de Wi como valores a memorizar: ela existe para julgar plausibilidade, e o texto diz isso três vezes.

---

## Segunda passagem (2026-08-30)

Reverificação independente das seis aulas: recálculo do zero dos seis exemplos trabalhados, reconferência das fórmulas, das atribuições e das faixas numéricas, e **verificação de que cada correção declarada na primeira passagem está efetivamente no texto**.

**Resultado da verificação da primeira passagem:** todas as correções foram confirmadas no arquivo — o sentido do viés estereológico (a02 e a03), a tabela de cinco faixas do critério de concentração (a05), o limite de ~50 µm de Bond (a04 e a03), os dois números da a06 e a reciprocidade energia/capacidade, o `78,3 %` e os indicadores derivados da a03, a quarta grandeza da a01, a tabela de Wi por faixas (a04), "fortemente magnéticos" (a05) e o callout de nomes comerciais (a02). **A aritmética dos seis exemplos confere integralmente**, incluindo as quatro energias de Bond da a03, a cadeia econômica da a05 e o escalonamento inverso de capacidade da a06. A equação de Elsner foi rebalanceada elemento a elemento e fecha; os teores estequiométricos de calcopirita (34,63 %) e calcosita (79,86 %) conferem; a tabela de Taggart confere linha a linha.

Quatro achados novos, todos 🟡, **três deles resíduos de correções da primeira passagem aplicadas de forma incompleta** — o padrão é instrutivo: a correção mudou o conteúdo e esqueceu a moldura em volta dele.

### 🟡 [GEOMET-M09-A01-GRANDEZAS-008] — "Três grandezas" seguido de quatro itens

**Aula:** 01. **Resíduo de:** `GEOMET-M09-A01-RECUP-003` (🟠, primeira passagem).

**Achado:** a correção da primeira passagem acrescentou corretamente a razão de concentração à lista de grandezas do balanço, levando-a de três para quatro itens — mas deixou a frase de abertura dizendo "**Três** grandezas descrevem o resultado, e não devem ser confundidas", imediatamente seguida de quatro marcadores. Sem consequência factual, mas é uma contradição visível na mesma linha de visão, e numa lista cujo propósito declarado é justamente *não confundir* as grandezas.

**Correção aplicada:** ✅ "Três" → "Quatro".
**Confiança:** alta.

---

### 🟡 [GEOMET-M09-A03-ARRED-007] — Parcelas exibidas que não somam o total exibido

**Aula:** 03. **Resíduo de:** `GEOMET-M09-A03-EXEMPLO-006` (🟠, primeira passagem).

**Achado:** a primeira passagem corrigiu o resultado de `78,4 %` para `78,3 %`, que é o valor certo (`0,71 × 0,96 + 0,29 × 0,35 = 0,6816 + 0,1015 = 0,7831`). Mas manteve as parcelas exibidas com três casas: a linha ficou `= 0,682 + 0,102 = 0,783`, e **0,682 + 0,102 = 0,784**. O aluno que conferir a conta na página encontra uma soma que não fecha, exatamente na linha que a auditoria anterior tinha ido lá corrigir. As outras três linhas do exemplo fecham com três casas; só esta não fecha, porque `0,1015` está no meio de um arredondamento.

Vale registrar a ironia: o achado `GEOMET-M09-A06-EXEMPLO-006 · b` da primeira passagem era precisamente "arredondamento intermediário levado adiante", e a solução adotada lá foi exibir quatro casas. A mesma solução não foi aplicada aqui.

**Correção aplicada:** ✅ a linha passou a exibir quatro casas, `= 0,6816 + 0,1015 = 0,7831 → 78,3 %`, tornando a soma verificável. Os demais números do exemplo não mudam.
**Confiança:** alta.

---

### 🟡 [GEOMET-M09-A04-WI-CARVAO-009] — Carvão na faixa dos moles, contra a própria tabela de Bond

**Aula:** 04. **Resíduo de:** `GEOMET-M09-A04-WI-VALORES-006` (🟡, primeira passagem).

**Achado:** a primeira passagem reconstruiu a tabela de Work Index em quatro faixas e reposicionou granito, quartzito e diorito contra as compilações de Bond — mas deixou **carvão** na faixa "moles ~5–10". A tabela de Bond dá carvão em torno de **11,4 kWh por tonelada curta**, isto é, **~12,5 kWh/t na base métrica** (fator 1,102), que é a faixa dos **intermediários**. É o mesmo defeito que o achado original corrigiu nas outras litologias, sobrevivendo numa entrada que não tinha valor numérico ao lado e por isso passou despercebida.

Verificação das demais entradas contra Bond (1961), convertidas para base métrica: barita ~5–7 ✅, gipsita ~7,4 ✅, quartzito ~10,6 ✅, dolomito ~12,4 ✅, calcário ~12,8 ✅, quartzo ~14–15 ✅, granito ~15,9 ✅, taconita ~16,4 ✅, xisto ~18,1 ✅, basalto ~18,8 ✅, gabro ~20,3 ✅, diorito ~21–23 ✅. **Carvão era a única entrada fora da sua faixa.**

**Correção aplicada:** ✅ carvão movido da linha "Moles" para a linha "Intermediários", com o valor `(~12)` explicitado; gipsita ganhou o seu `(~7)`, que faltava; `claim` `GEOMET-M09-A04-WI-VALORES-006` atualizado.
**Confiança:** alta quanto ao desenquadramento; média quanto ao valor único, já que a moabilidade do carvão varia fortemente com o *rank* e é convencionalmente medida pelo HGI, não pelo Wi de Bond — motivo de o valor entrar como `~12` e não como número fechado.

---

### 🟡 [GEOMET-M09-A04-WI-DIORITO-010] — Diorito descrito como rocha máfica de grão fino

**Aula:** 04. **Achado novo** (não é resíduo).

**Achado:** a linha "muito duros e tenazes" da tabela de Wi lia "diorito (~23) e outras **rochas máficas de grão fino** e tenazes". A descrição está petrograficamente errada em duas frentes: o diorito é uma rocha plutônica **fanerítica** (grão médio a grosso), não de grão fino, e é de composição **intermediária**, não máfica. Pior, a descrição dada corresponde bem ao **basalto** — que está na faixa de baixo, "duros ~16–20". A frase, portanto, descrevia a faixa vizinha.

O erro é de baixo impacto metalúrgico e altíssima visibilidade num **curso de geologia**: é exatamente o tipo de nomenclatura que o aluno-alvo domina, e vê-la errada num material que ele está usando para aprender engenharia de processo corrói a confiança no resto da tabela. A tenacidade do diorito vem da trama entrelaçada de plagioclásio e anfibólio, não da granulação fina.

**Correção aplicada:** ✅ reescrito para "diorito (~23) e outras rochas ígneas **de trama entrelaçada e alta tenacidade**", que nomeia a causa real e não colide com a faixa de baixo; `claim` atualizado.
**Confiança:** alta.

---

### Desfecho da segunda passagem

| claim_id | Sev. | Desfecho | Arquivos alterados |
|---|---|---|---|
| `GEOMET-M09-A01-GRANDEZAS-008` | 🟡 | Corrigido | aula-01 |
| `GEOMET-M09-A03-ARRED-007` | 🟡 | Corrigido | aula-03 |
| `GEOMET-M09-A04-WI-CARVAO-009` | 🟡 | Corrigido | aula-04 |
| `GEOMET-M09-A04-WI-DIORITO-010` | 🟡 | Corrigido | aula-04 |

**Nenhum achado 🔴, 🟠 ou 🟡 permanece em aberto.** Não há `open_findings`. Os dois `maintenance_flags` da primeira passagem seguem válidos e não bloqueiam o gate.

**Veredito da segunda passagem: aprovado.** O módulo está liberado para questionário e flashcards.

**Advertência acrescentada para quem gerar a avaliação:** a Aula 03 usa a expressão "superestima a liberação" em **dois sentidos diferentes** — o viés estereológico da medida em seção 2D (Aula 02) e o erro de *modelagem* de supor descolamento num minério de fratura não preferencial ("Erros comuns"). São coisas distintas e uma questão mal formulada os funde. Se for cobrar o viés estereológico, ancore explicitamente na medida por seção polida.
