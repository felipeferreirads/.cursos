# Revisão didática: Módulo 19 — Geofísica: métodos e imageamento da Terra

**Revisado em:** 2026-08-18 · **Modo:** review-and-fix
**Material:** seis aulas do M19, questionário final e baralho de flashcards (`.md`, `-basic.csv`, `-cloze.csv`)
**Veredito da primeira passagem:** Requer revisão
**Veredito final:** Bem ensinado com ressalvas

## Resumo

**Primeira passagem:** 🔴 0 bloqueiam · 🟠 1 prejudica · 🟡 4 atrito · 🔵 1 sugestão
**Após as correções:** 🔴 0 bloqueiam · 🟠 0 prejudicam · 🟡 0 atrito · 🔵 1 sugestão (não corrigível nesta skill)

**Carga estimada:** 42 termos únicos nos blocos de vocabulário (após a correção do achado 🟡 1); 1 exemplo trabalhado por aula, todos com 2–3 passos encadeados; 6 aulas declaradas de 24–28 min. Corpo real por aula, recontado sobre "Conteúdo" até "Próxima aula": 1.408 · 1.143 · 1.051 · 1.080 · 1.184 · 1.226 (total 7.092) — **todas as seis aulas dentro do teto de 1.600 palavras do LC-02**, nenhuma candidata a divisão em Parte 1 / Parte 2.

A auditoria científica de 2026-08-18 já havia deixado registrada, como pendência explícita, a sub-cobertura de `oa04` no questionário (achado 🟠 10 da auditoria). Essa pendência é o achado 🟠 1 desta revisão e foi resolvida nesta mesma passagem, por instrução explícita do usuário.

## Achados

### 🟠 1. `oa04` cobria só 2 dos 46 pontos possíveis do questionário, para uma aula inteira de quatro métodos — RESOLVIDO

**Tipo:** desalinhamento aula–avaliação (sub-cobertura)
**Onde:** questionário final · matriz de cobertura
**Problema:** a Aula 05 é a única do módulo que reúne quatro técnicas distintas — eletrorresistividade, polarização induzida, eletromagnético e métodos geotérmicos — e ainda assim `oa04` tinha só as duas múltiplas escolha Q9 e Q10 (2 pontos em 40), a menor fatia do questionário por larga margem. Os outros quatro objetivos tinham, cada um, uma dissertativa própria (Q17, Q18 e Q19 cobrindo `oa03`, `oa01` e `oa05`); só `oa04` ficava sem nenhum item de "aplicar/avaliar", testando apenas reconhecimento de fato isolado. Um aluno podia acertar Q9 e Q10 de cor e nunca ter sido cobrado a raciocinar sobre quando usar ER, IP ou EM — que é precisamente a habilidade que a aula constrói (a seção "Como escolher entre os dois" é o equivalente, em outras aulas, da seção que a avaliação testa com dissertativa).
**Correção aplicada:** acrescentada a **Q20** (6 pontos, dissertativa de três partes) no questionário: um cenário de exploração mineral que pede para escolher entre ER, IP e EM para um alvo de sulfeto disseminado, explicar por que a ER isolada poderia falhar, e relacionar a ausência de anomalia magnética ao fato de que magnetismo responde a um mineral específico (magnetita), não à mineralização metálica em geral — reconectando deliberadamente com a Aula 04. `oa04` passa de 2 para 8 pontos; o questionário passa de 19 para 20 questões e de 40 para 46 pontos; matriz, autodiagnóstico, nota de corte (32/46) e contagem de níveis cognitivos foram recalculados. Nenhuma questão nem gabarito pré-existente foi alterado.
**Escopo:** correção aplicada nesta revisão, com edição direta do questionário — exceção deliberada à regra geral de que esta skill não edita avaliação, por se tratar da pendência que a própria auditoria científica encaminhou explicitamente para a revisão didática e por instrução direta do usuário para resolvê-la nesta passagem.

### 🟡 2. Vocabulário da Aula 01 com 9 termos, acima do teto do LC-03

**Tipo:** carga de vocabulário
**Onde:** aula 01 · "Vocabulário desta aula"
**Problema:** o bloco de abertura listava nove entradas (onda P, onda S, ondas de superfície, sismograma, hipocentro, epicentro, magnitude, intensidade, zona de sombra), acima do teto de 5–8 do LC-03. Das nove, "hipocentro" e "epicentro" são o par mais fácil de fundir sem perda: são definidos um em função do outro na própria aula ("epicentro: projeção do hipocentro na superfície") e nenhuma das seis aulas restantes do módulo tem esse problema.
**Correção aplicada:** as duas entradas foram fundidas em uma só — "Hipocentro e epicentro" — definindo os dois lado a lado, exatamente como o corpo do texto já os apresenta. O bloco volta a 8 termos. Nenhuma definição foi perdida.
**Escopo:** correção local, concluída.

### 🟡 3. `oa03`, repartido entre duas aulas, não declarava o repartimento

**Tipo:** objetivo repartido sem marcação
**Onde:** aula 03 e aula 04 · bloco "Ao final você vai conseguir"
**Problema:** `oa03` cobre gravimetria (aula 03) e magnetometria (aula 04) — o hub já nomeia as duas técnicas no texto do objetivo —, mas as duas aulas marcavam a mesma tag `[geologia-m19-oa03]`, sem indicar que se tratava de um objetivo em duas partes. É o mesmo padrão de risco que o módulo 18 encontrou e corrigiu para `oa01` (repartido entre aulas 01 e 02): um aluno que usa a lista de objetivos para se orientar não tem, sem essa marcação, como saber que precisa das duas aulas para completar `oa03`.
**Correção aplicada:** aula 03 marca `[geologia-m19-oa03 · parte 1 de 2]` com nota apontando a aula 04 para a parte 2; aula 04 marca `[geologia-m19-oa03 · parte 2 de 2]` apontando de volta. O texto do objetivo no hub do módulo ganhou a mesma nota entre parênteses. Mesma convenção já em uso no módulo 18.
**Escopo:** correção local, concluída.

### 🟡 4. Metadados `palavras_corpo` das seis aulas não batiam com a contagem real

**Tipo:** instrumento de verificação desalinhado
**Onde:** as seis aulas · bloco de metadados
**Problema:** os valores declarados (todos redondos: 1250, 1300, 1350, 1400) superestimavam sistematicamente a contagem real do corpo (da seção "Conteúdo" até "Próxima aula"), por até 249 palavras (aula 03: declarado 1.300, real 1.051). Como o LC-02 usa esse campo para checar o teto de 1.600, valores infladamente próximos ao teto poderiam, numa expansão futura da aula, mascarar um estouro real por mais tempo do que se o campo refletisse a contagem verdadeira — o mesmo tipo de defeito que o módulo 17 encontrou (lá, na direção oposta: subdeclarado).
**Correção aplicada:** os seis valores foram recontados programaticamente sobre o corpo real e atualizados: 1.400 · 1.150 · 1.050 · 1.080 · 1.180 · 1.230.
**Escopo:** correção local, concluída.

### 🟡 5. Parêntese truncado sobre resistividade de poço — RECEBIDO DA AUDITORIA

**Tipo:** redação que trava a leitura
**Onde:** aula 06 · "Os perfis básicos, um a um" (perfil de resistividade de poço)
**Problema:** encaminhado pela auditoria científica como observação não factual. A frase "(baixa condutividade/água salina desloca para fora, óleo e gás são muito mais resistivos que água salgada)" comprime dois fatos em uma oração truncada, sem verbo claro ligando "água salina" a "desloca para fora" — o conteúdo estava correto, a sintaxe não.
**Correção aplicada:** reescrita como duas orações completas: "água salgada é muito condutiva (baixa resistividade), enquanto óleo e gás, ocupando o espaço poroso que a água salgada deixaria, são muito mais resistivos".
**Escopo:** correção local, concluída.

### 🔵 6. `oa02` (Aula 02) é o único objetivo do módulo sem exemplo numérico próprio no questionário

**Tipo:** distribuição cognitiva
**Onde:** questionário final · matriz de avaliação
**Problema:** `oa01`, `oa03`, `oa04` (após o achado 1) e `oa05` têm cada um uma dissertativa de aplicação com números concretos para trabalhar (intervalos P-S, anomalia em nT, cenário de exploração, perfis de poço). `oa02` (reflexão/refração) tem só Q4, Q5 e a V/F Q14 — nenhuma pede ao aluno para calcular ou interpretar um dado numérico de refração, apesar de a própria aula ter um exemplo trabalhado inteiro sobre ponto de cruzamento e velocidades de camada.
**Escopo:** sugestão para o `gerador-de-questionarios`, numa eventual próxima revisão do questionário. Não é achado bloqueante — `oa02` está avaliado, só não tem o mesmo tipo de item que os demais; não foi corrigido aqui para não expandir o questionário além do necessário para resolver a pendência que a auditoria encaminhou.

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo | Avaliado em | Cards |
|---|---|---|---|---|
| `oa01` — sismologia e ondas sísmicas | aula 01, seis seções | sim — trilateração com 3 estações | Q1, Q2, Q3, Q13, Q18 — 11 pts | `fb001`–`fb010`, `fc001`–`fc006` |
| `oa02` — sísmica de reflexão e refração | aula 02, quatro seções | sim — ponto de cruzamento em levantamento de refração | Q4, Q5, Q14 — 4 pts | `fb011`–`fb020`, `fc007`–`fc012` |
| `oa03` parte 1 — gravimetria | aula 03, três seções | sim — perfil Bouguer sobre bacia sedimentar | Q6, Q7, Q15 (compartilhado) | `fb021`–`fb030`, `fc013`–`fc017` |
| `oa03` parte 2 — magnetometria | aula 04, quatro seções | sim — anomalia aeromagnética de 200 nT | Q8, Q16, Q17 (compartilhado) — 13 pts (a03+a04) | `fb031`–`fb040`, `fc018`–`fc023` |
| `oa04` — métodos elétricos, EM e geotérmicos | aula 05, cinco seções | sim — intrusão salina por ER | Q9, Q10, Q20 — 8 pts | `fb041`–`fb050`, `fc024`–`fc029` |
| `oa05` — perfilagem de poços e integração | aula 06, quatro seções | sim — zona produtora por GR+sônico+resistividade | Q11, Q12, Q19 — 10 pts | `fb051`–`fb060`, `fc030`–`fc036` |

Nenhum objetivo descoberto e nenhuma seção órfã: as seis aulas mapeiam integralmente os cinco objetivos, com `oa03` legitimamente repartido entre as aulas 03 e 04 — repartimento que **passou a ser declarado** pela correção do achado 🟡 3. A cobertura do baralho é uniforme entre objetivos (15–17 cards cada); não há lacuna de memorização equivalente à do módulo 18.

## Verificação do contrato de nível

- **LC-01 — nenhum termo sem definição:** aprovado. Verificada a primeira ocorrência de cada termo técnico nas seis aulas, incluindo os que a correção da auditoria científica introduziu ou ajustou (titanomagnetita, anomalia Bouguer simples/completa, subsidência dinâmica não se aplica a este módulo) — todos chegam com aposto ou definição em linguagem comum. O único caso de fronteira, "impedância acústica" (aula 02), é definido no próprio vocabulário e reforçado no corpo antes de ser usado na análise da reflexão.
- **LC-02 — teto de 1.600 palavras:** aprovado nas seis aulas, entre 1.051 e 1.408 palavras reais. Nenhuma candidata a divisão — o módulo tem folga confortável do teto, ao contrário do padrão observado no módulo 17.
- **LC-03 — abertura padronizada:** aprovado após o achado 🟡 2. Os seis blocos de vocabulário ficam em 6 a 8 termos (8 · 7 · 6 · 6 · 7 · 7), e os seis blocos "Antes de começar" linkam pré-requisitos específicos (aula ou módulo, conforme a natureza do pré-requisito) sem hedge do tipo "se você já viu". Todos os alvos de wikilink internos ao módulo (aulas 01–06 entre si) foram conferidos e resolvem.
- **LC-04 — analogia antes do termo:** aprovado. A pedra no lago para ondas sísmicas se propagando (a01), o raio de luz batendo num vidro para reflexão (a02), a laje de rocha "removida" da leitura para a correção Bouguer (a03), a área "magneticamente invisível" que domina o sinal para magnetita (a04), a corrente escolhendo o fluido dos poros em vez do mineral seco (a05), e a "radiografia" indireta versus a medida direta no poço (a06) — todas aparecem antes ou junto da formalização do termo, nunca depois.
- **LC-05 — ordem de grandeza:** aprovado, e é um ponto forte do módulo. "aproximadamente entre 103° e 142°", "em torno de 6 km/s... cerca de 8 km/s", "cerca de 580 °C", "25–30 °C/km", "dezenas a poucas centenas de nT sobre um campo de dezenas de milhares de nT" — nenhum valor de risco é apresentado como constante fechada sem qualificador de faixa ou "cerca de", inclusive depois das correções numéricas da auditoria científica (velocidade da P na crosta, anomalia Bouguer simples/completa).
- **LC-06 — matemática reativada antes do uso:** aprovado. A geometria de trilateração (aula 01) e o ponto de cruzamento na refração (aula 02) são tratados qualitativamente, com a aritmética restrita ao "Exemplo trabalhado", nunca exigindo cálculo formal no corpo teórico.
- **LC-07 — blocos obrigatórios:** aprovado. As seis aulas têm "Exemplo trabalhado" e "Recap relâmpago" completos; três delas (01, 03, 05) também têm "Apoio visual" descritivo, usado quando a geometria do fenômeno (círculos de trilateração, perfil Bouguer em U, mapa de contorno geotérmico) se beneficia de uma imagem mental explícita.
- **LC-08 — controvérsia em uma frase:** não há controvérsia de literatura relevante retida no corpo das seis aulas depois da auditoria científica — a única marcada como ⚪ (saturação da escala Richter, achado 13 da auditoria) permanece como pendência do usuário e não foi tocada por esta revisão, por não ser um achado didático.

## Alinhamento entre as aulas

A progressão segue a ordem natural de "profundidade de investigação decrescente, custo crescente de resolução": sismologia natural em escala global (01) → o mesmo princípio em miniatura com fonte controlada (02) → métodos potenciais que não precisam de fonte alguma, primeiro densidade (03) depois magnetização (04) → métodos que precisam de contato ou indução, elétricos e térmicos (05) → a única medida direta, dentro do poço, que calibra tudo o que veio antes (06). Cada aula reutiliza explicitamente o vocabulário da anterior — "método potencial" nasce na aula 03 e a aula 04 o reaproveita sem reensinar; "anomalia" e "contraste" atravessam as aulas 03 a 05; "tempo versus profundidade", que nasce na aula 02, é resolvido de fato só na aula 06 — e a aula 06 fecha o módulo citando as cinco aulas anteriores por nome, uma a uma, no bloco de pré-requisitos e no corpo.

Duas escolhas de sequência merecem registro por serem acertos deliberados. A primeira: reflexão vem **antes** de refração dentro da própria aula 02, mesmo a refração sendo historicamente anterior (Mohorovičić, 1909) — a aula ensina o método de maior uso corrente primeiro e usa a refração, o método mais "estranho" conceitualmente (a onda que chega depois de percorrer um caminho mais longo chega primeiro), como o segundo, apoiado na intuição de reflexão já formada. A segunda: perfilagem de poço fecha o módulo, e não abre — apesar de ser, em tese, o método fisicamente mais simples de entender (uma ferramenta que mede direto, sem inversão) —, porque só faz sentido pedagógico depois que o aluno já sabe *o que* cada método de superfície mede e *por que* precisa de calibração; a aula 06 é, na prática, a aula que dá significado retroativo às cinco anteriores.

## O que está bem feito

A disciplina de nomear explicitamente **o que um método não permite concluir** — não unicidade na gravimetria e magnetometria, ambiguidade fluido/rocha na resistividade de poço, resolução grosseira da refração — é o traço mais forte do módulo, e ele se propagou até o questionário: a nota de abertura do questionário ("quase toda questão aqui testa se você sabe o que uma medida permite concluir, e o que ela não permite") não é retórica, é uma descrição precisa do que as questões realmente cobram (Q15, Q16, Q17b são exemplos diretos).

O exemplo trabalhado da aula 04 é o melhor caso de raciocínio ambíguo bem conduzido do módulo: apresenta uma anomalia magnética, dá duas hipóteses plausíveis, e explicita exatamente que dado adicional (gravimetria) decidiria entre elas e por quê — sem fingir que o dado magnético sozinho resolve o problema. A Q20 acrescentada nesta revisão foi desenhada para replicar essa mesma estrutura de raciocínio (ambiguidade → método complementar → limite do método complementar) em `oa04`, mantendo o padrão do módulo em vez de introduzir um estilo de questão diferente.

O fio condutor da aula 06 — cada método é sensível a uma propriedade física diferente, nenhum resolve sozinho — funciona como síntese genuína do módulo inteiro, não como resumo genérico: ela nomeia, um a um, os cinco métodos anteriores e o tipo de ambiguidade específico de cada um, o que dá ao encerramento do módulo um fechamento real em vez de um "e assim terminamos" solto.

## Gate didático

**Liberado.** Nenhum achado 🔴. Os cinco achados corrigíveis nesta skill (🟠 1 e 🟡 2–5) foram aplicados; nenhuma edição introduziu alegação factual nova, e nenhuma tocou em número, limite, classificação ou fonte já validados pela auditoria científica de 2026-08-18.

O achado 🟠 1 é um caso deliberado de exceção à regra geral desta skill de não editar questionário: a auditoria científica já havia identificado e encaminhado exatamente essa lacuna, e o usuário instruiu explicitamente a resolvê-la nesta passagem, incluindo escrever a questão nova. Nenhum fato novo foi introduzido na Q20 além do que as aulas 04 e 05 já ensinam (magnetismo controlado por magnetita especificamente; IP sensível a disseminação metálica via efeito capacitivo) — a questão testa aplicação e integração, não conteúdo inédito.

Uma sugestão permanece registrada, não bloqueante e fora do escopo de correção direta:

1. **Achado 🔵 6** — `oa02` não tem item de aplicação numérica no questionário, ao contrário dos demais objetivos. Registrado para uma eventual expansão futura do `gerador-de-questionarios`, não corrigido nesta passagem.

O `course-state.yaml` **não** foi alterado por esta execução, conforme a restrição de coordenação em paralelo; o registro do módulo foi feito apenas no hub `19-geofisica-metodos-modulo.md`. Nenhum arquivo fora de `19-geofisica-metodos/` foi tocado — em particular, nada nos módulos 16, 18 e 19.
