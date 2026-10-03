# Auditoria científica — Módulo 06: Cabochão

**Curso:** Teoria da lapidação — do desbaste ao projeto óptico (`lapidacao`)
**Módulo:** 06 — Cabochão (área IV. Talhes de superfície curva)
**Escopo:** as 6 aulas do módulo (`06-cabochao-aula-01` … `06-cabochao-aula-06`). Questionário e baralho **não existem** quando esta auditoria roda — é o efeito pretendido do gate.
**Modo:** `audit-and-fix` · **Profundidade:** `full`
**Data:** 2026-09-03
**Auditor:** geo-arquiteto (Opus)
**Contrato de nível:** `ensino-medio-com-gemologia-v1`

---

## Resumo

| Severidade | Quantidade |
|---|---|
| 🔴 Vermelho (erro factual) | 2 |
| 🟠 Laranja (impreciso / falso universal / termo colidente) | 6 |
| 🟡 Amarelo (imprecisão menor, contradição interna) | 4 |
| 🔵 Azul (enriquecimento, escrituração) | 2 |
| ⚪ Branco (verificado, limite de fonte registrado) | 1 |
| ✅ Verificado sem achado | 25 alegações |

**Total de alegações auditáveis:** 34 antes da auditoria → **37** depois (3 criadas).
**Achados em aberto ao final:** nenhum. Todos os 🔴 e 🟠 foram corrigidos no arquivo. **Gate liberado.**

**`palavras_corpo` antes → depois:** a01 1286→1441 · a02 1362→1537 · a03 1337→1397 · a04 1445→1599 · a05 1577→1597 · a06 1275→1330. Todas sob o teto de ~1600 de LC-02.

---

## Verificações estruturais

**Formato de `claim_id`.** As 34 alegações herdadas do redator casam com `^[A-Z]{2,4}-[A-Z0-9]+-[A-Z0-9]+-[0-9]{3}$` — **nenhum resíduo de 5 segmentos**, ao contrário dos módulos 04 e 05, onde o redator escorregou. As 3 alegações criadas nesta auditoria (`CIN-CONIC-BISEL-001`, `FEN-ASTER-CONT-001`, `FEN-ASTER-DIOP-001`) seguem o mesmo formato. Verificado por regex sobre os seis arquivos, antes e depois das correções.

**Competência de bancada.** Varredura específica por afirmação, sugestão ou avaliação de destreza manual: **nenhum achado**. As seis aulas usam construção impessoal (`serra-se`, `desbasta-se`, `marca-se`), nunca imperativo de bancada, e as seis trazem em "O que não concluir" a exclusão explícita (como operar serra/esmeril/dop; como desbastar a cúpula; como produzir a figura de asterismo; como escavar o oco; a técnica de engaste, remetida à joalheria). Os seis verbos de objetivo são de conhecimento observável — justificar, descrever, relacionar, explicar, determinar, distinguir. O passo 1 do exemplo trabalhado da a05 (localizar o eixo c sob luz pontual) descreve um **teste de diagnóstico**, não uma operação de máquina, no mesmo critério já aceito no módulo 05.

**Pré-requisito cross-curso.** O curso de Gemologia é citado **por nome** em a01, a03 e a05, nunca por wikilink. Nenhuma violação.

**Escrituração (🔵).** O `next_action` do módulo 06 declara "33 alegações auditáveis (a01=5, a02=6, a03=6, a04=6, a05=7, a06=5)". Os parciais somam 35 e a contagem real era **34** (a05 tinha 6, não 7). Erro de escrituração do redator, sem efeito sobre o conteúdo; corrigido no bloco de auditoria do `course-state.yaml`.

---

## 🔴 Vermelho 1 — a04 · o sentido da inclinação da cinta estava invertido

**Onde:** `06-cabochao-aula-04`, seção "Defeitos de cinta", os dois primeiros bullets. Alegação `CIN-INCL-UNDER-001`.

**O que dizia.**
> Inclinada **para dentro** (socavação): […] a pedra parece pequena para o engaste e **pode escapar por baixo**.
> Inclinada **para fora**: a base é menor que o topo; **o aro não consegue dobrar sobre a cinta** e a pedra fica presa só pela pressão, insegura.

**Por que é erro.** Dois erros num bloco de quatro linhas.

1. **A conicidade tratada como defeito é a geometria normal de oficina.** O cabochão de produção é cortado de propósito com a cinta afunilando em direção à base — base ligeiramente **menor** que o topo da cinta —, exatamente para o aro do engaste fechar sem ter de dobrar longe demais. As máquinas trazem apoios de ângulo para produzi-la: a faixa recomendada é de **10° a 15°**, e o *cab rest* da Diamond Pacific para Genie/Pixie corta **12,5°**. A aula classificava essa geometria como defeito ("o aro não consegue dobrar sobre a cinta"), invertendo a causa-efeito real — é justamente ela que **permite** ao aro dobrar.
2. **"Pode escapar por baixo" é geometricamente impossível** no caso descrito. Se a base é a maior seção da pedra e o engaste tem assento, não há por onde a pedra sair para baixo. O custo verdadeiro da socavação é outro: o aro é feito para a maior seção (que passou a ser a base), o metal precisa atravessar um vão para dentro até alcançar o topo da cinta — fecha mal, enruga, segura pouco — e a silhueta encolhe, com material enterrado na base que não conta para a aparência.

**Correção aplicada.** A seção foi reescrita em quatro blocos: (i) **como é a cinta de uma pedra bem cortada** — parede vertical de ~0,5–1 mm no alto, que é o que o aro encosta (a03), conicidade de trabalho de 10°–15° abaixo dela, e pequeno bisel na aresta inferior porque aresta viva ali lasca ao cravar; (ii) **socavação** com a consequência correta; (iii) **conicidade excessiva**; (iv) **parede vertical comida**. A frase-chave instalada: *"cinta inclinada não é defeito por si"*.

**Propagação.** Foram harmonizadas as duas outras aulas que afirmavam a perpendicularidade como geometria única: a **a02** (etapa 5 e `PRE-CINTA-VERT-001`) e a **a03** (`DOM-ENG-PAREDE-001`), ambas agora dizendo que a exigência do engaste é **a parede**, não a peça inteira reta. Vocabulário da a04 reindexado (`cinta em bisel`, `socavação` e a entrada nova `conicidade de cinta`), Recap reescrito, "Erros comuns" ajustado ("não endireita **socavação** nem fio de faca").

**Alegações.** `CIN-INCL-UNDER-001` reescrita; **`CIN-CONIC-BISEL-001` criada** para a geometria de trabalho; `PRE-CINTA-VERT-001` e `DOM-ENG-PAREDE-001` corrigidas.

**Fontes.** International Gem Society, *Lapidary Fundamentals: Cabochon Cutting* (acesso 2026-09-03) — "leave a small, vertical area on the sides", mais o bisel de proteção da aresta inferior. SUVA Lapidary Supply, *Lapidary 101: How to Make a Cabochon* (acesso 2026-09-03) — ângulo de cinta de 10° a 15° e o bisel da base. Diamond Pacific, *Genie and Pixie Cab Rests* — 12,5°. Sinkankas, *Gem Cutting: A Lapidary's Manual* — cinta em bisel e socavação como defeito.

**Confiança:** alta para a geometria de trabalho (três fontes independentes convergem); alta para a impossibilidade da fuga por baixo (geometria elementar).

---

## 🔴 Vermelho 2 — a05 · a aritmética dos feixes quebrada e o eixo c estendido a mineral isométrico

**Onde:** `06-cabochao-aula-05`, seção "Asterismo". Alegação `FEN-ASTER-EIXOC-001`.

**O que dizia.**
> Em granada e diopsídio, geralmente **dois ou dois pares de conjuntos** → estrela de **4 raios**.
> **Orientação de corte:** a **base perpendicular ao eixo c** […]

**Por que é erro.**

1. **"Dois pares de conjuntos" contradiz o próprio mecanismo da aula.** Cada conjunto de inclusões paralelas produz **uma faixa** de luz, e cada faixa atravessa a pedra de lado a lado — ou seja, dois raios. Dois conjuntos dão 4 raios; três, 6. "Dois pares de conjuntos" são quatro conjuntos e dariam **8 raios**. A aula afirmava, duas linhas acima, "dois ou três conjuntos", e se contradizia na frase seguinte. Este é o ponto exatamente coberto por `lapidacao-m06-oa05` ("explicar o mecanismo geométrico"), e um aluno que decorasse a frase erraria a contagem.
2. **A regra do eixo c foi enunciada como geral logo depois de citar granada.** Granada é **isométrica**: não existe nela um eixo c distinto dos demais eixos, e por ser oticamente isotrópica também não tem eixo óptico (o que invalida, de passagem, a formulação corrente em fontes populares, "cortar perpendicular ao eixo óptico"). A regra que de fato generaliza é: **base perpendicular ao eixo de simetria que os conjuntos de inclusões compartilham** — no coríndon, o eixo c; em granada, a normal ao plano que contém os feixes.

**Correção aplicada.** A frase do mecanismo passou a enunciar a regra de contagem explicitamente ("cada conjunto gera uma faixa […] dois conjuntos dão 4 raios, três dão 6") antes dos exemplos. A orientação foi reformulada para o eixo de simetria compartilhado, com o parêntese sobre granada isométrica. Recap e "O que não concluir" alinhados.

**Enriquecimento factual acoplado (novo).** No **diopsídio estrela** os dois conjuntos de agulhas **não são perpendiculares entre si**, de modo que os quatro raios **não se cruzam a 90°** — e isso é propriedade do material (simetria monoclínica), não erro de orientação do corte. O fato serve diretamente ao objetivo da aula e previne o diagnóstico errado "estrela torta = bruto mal orientado", que o módulo 14 (diagnóstico reverso) herdaria.

**Alegações.** `FEN-ASTER-EIXOC-001` reescrita; **`FEN-ASTER-DIOP-001` criada**.

**Fontes.** GIA — asterismo no coríndon (rutilo a 60/120° no plano perpendicular ao eixo c; estrela de 6 raios) e estrela de 4 raios em granada e diopsídio. Literatura gemológica corrente sobre diopsídio estrela (acesso 2026-09-03) — duas direções de agulhas; as direções da estrela não se cruzam a 90° e isso não decorre de má orientação do bruto. Sinkankas, *Gem Cutting: A Lapidary's Manual* — base perpendicular ao eixo para a estrela.

**Confiança:** alta.

---

## 🟠 Laranja 1 — a05 · o contorno redondo dado como obrigatório para estrela

**Onde:** `06-cabochao-aula-05`, seção "Asterismo" e "Erros comuns".

**O que dizia.** "O **contorno deve ser redondo** […]: uma oval distorce a estrela" e, em Erros comuns, "**Usar contorno oval para estrela**. […] Oval é para o olho-de-gato de um feixe só."

**Por que é impreciso.** É uma proibição absoluta contradita pela prática universal: safira e rubi estrela são correntemente lapidados em **oval**, e os critérios de qualidade de pedra estrela (estrela centrada, raios retos e equivalentes) se aplicam a cabochão **redondo ou oval**. O que a simetria sustenta é uma afirmação mais fraca: o redondo com cúpula de revolução é o caso ideal, porque a simetria da cúpula acompanha a dos feixes; quanto mais alongada a oval, mais desiguais ficam os raios. Como estava, a frase produziria distrator errado num questionário ("qual contorno para safira estrela?").

**Correção aplicada.** Corpo, Recap e o bullet de "Erros comuns" (que virou "**Achar que só o redondo serve para estrela**") reescritos com a formulação gradual. Alegação **`FEN-ASTER-CONT-001` criada**.

**Fontes.** GIA — critérios de qualidade da pedra estrela em cabochão redondo ou oval; levantamento de oferta comercial corrente de safira estrela (acesso 2026-09-03), com os dois contornos igualmente presentes.

---

## 🟠 Laranja 2 — a01 · "material com esses fenômenos é **sempre** lapidado em cabochão"

**Onde:** `06-cabochao-aula-01`, Gatilho 2 e alegação `CAB-ESC-FEN-001`.

**Por que é impreciso.** Falso universal. A regra vale com força diferente por fenômeno: para **asterismo e chatoyance** a superfície curva é de fato obrigatória, porque o efeito é um reflexo que só se reúne numa curva; já **opala com jogo de cores** e **pedra da lua** aparecem facetadas no comércio, com o fenômeno mais fraco e picotado. Deixar "sempre" transforma um raciocínio de mecanismo numa regra decorada — o oposto do que `lapidacao-m06-oa01` pede.

**Correção aplicada.** Parágrafo do Gatilho 2 e Recap reescritos com a gradação por fenômeno e o fecho "regra forte, não lei sem exceção"; alegação reescrita.

**Fontes.** GIA — fenômenos ópticos e talhe; Sinkankas — cabochão para pedras fenomenais.

---

## 🟠 Laranja 3 — a01 · dureza citada como se fosse tenacidade

**Onde:** `06-cabochao-aula-01`, exemplo trabalhado (b): "transparente, sem inclusões, **tenacidade alta (8,5 Mohs)**, cor boa".

**Por que é impreciso.** 8,5 é a **dureza** Mohs do crisoberilo, não sua tenacidade. A confusão é exatamente a que o pré-requisito do curso de Gemologia separa e que o próprio Gatilho 3 desta aula usa como distinção operante ("tenacidade baixa — que lasca com facilidade"). Deixar a colagem no exemplo trabalhado ensina, no ponto de maior atenção do leitor, que uma coisa é evidência da outra.

**Correção aplicada.** "**dureza 8,5** e boa tenacidade (são duas propriedades distintas — a dureza resiste ao risco, a tenacidade resiste ao lascar)". A alegação `CAB-ESC-TEN-001` recebeu a mesma advertência.

---

## 🟠 Laranja 4 — a06 · "efeito de olho de peixe" aplicado à base plana de um cabochão

**Onde:** `06-cabochao-aula-06`, cabochão duplo. Alegação `VAR-DUP-TRANSL-001`.

**Por que é impreciso.** *Fisheye* / olho de peixe é um defeito de **pedra facetada** — a reflexão da cinta vista pela mesa quando o pavilhão é raso demais — e o curso vai ensiná-lo com esse sentido no módulo 14 (catálogo de defeitos e diagnóstico reverso). Usá-lo aqui para outro fenômeno (o brilho chapado que a base plana devolve num cabochão translúcido) planta uma colisão de termo dentro do próprio curso, do tipo que o modo `cross-course` do auditor existe para caçar.

**Correção aplicada.** Termo removido; a reflexão morta ficou descrita pelo que é ("um brilho chapado, sem vida, que devolve o plano da base em vez de deixar a luz passar"). Alegação reescrita com a razão da remoção registrada.

---

## 🟠 Laranja 5 — a02 · "a ordem é fixa" onde há duas escolas

**Onde:** `06-cabochao-aula-02`, seção "Por que a ordem é fixa" e alegação `PRE-ORDEM-FIXA-001`.

**Por que é impreciso.** Duas das amarras são geométricas e realmente não têm alternativa (contorno fechado antes da cúpula; base plana antes da dopagem). A terceira — dopar **por último** — é uma escola, não uma necessidade: há prática corrente que dopa logo após o recorte grosso e desbasta o contorno com a peça já no bastão, ganhando firmeza e centragem à custa de acesso. A justificativa dada pela aula ("o dop atrapalha o acesso à cinta") também é fraca, já que o bastão é mais fino que a pedra.

**Correção aplicada.** A seção separa agora as duas amarras rígidas da posição aberta da dopagem, e a divergência foi declarada como **pergunta em aberto**, sem arbitrar — o que de quebra instala o **único LC-08 do módulo** (ver o achado 🔵 2). Recap e alegação alinhados; "Erros comuns" ajustado.

**Fontes.** Sinkankas (dopagem após o contorno) × SUVA Lapidary Supply, *Lapidary 101* (acesso 2026-09-03): dopagem logo após o recorte, contorno desbastado com a peça dopada.

---

## 🟠 Laranja 6 — a02 e a03 · a perpendicularidade da cinta como geometria única

**Onde:** `06-cabochao-aula-02` etapa 5 (`PRE-CINTA-VERT-001`) e `06-cabochao-aula-03` seção "A exigência do engaste" (`DOM-ENG-PAREDE-001`).

**Por que é impreciso.** Propagação do 🔴 1. Corrigir só a a04 deixaria o módulo se contradizendo: uma aula mandando a parede sair rigorosamente perpendicular, outra descrevendo a conicidade de trabalho como normal.

**Correção aplicada.** Nas duas aulas, a perpendicular permanece como **geometria de referência** (é ela que faz o contorno visível coincidir com o contorno real) e a exigência do engaste passa a ser nomeada com precisão: **a parede**, não a peça inteira reta. A a03 ganhou a meia-frase "abaixo dessa parede a cinta ainda pode afunilar de leve para a base (aula 04)". Vocabulário da a02 (`cinta`) ajustado.

---

## 🟡 Amarelo 1 — a03 · o caminho óptico do exemplo (b) ignora a parede de cinta

**Onde:** `06-cabochao-aula-03`, exemplo trabalhado (b).

Os números dados (~6,6 mm → ~4 mm) são exatamente **duas vezes a altura da cúpula**, o que despreza a parede de cinta de ~0,5–1 mm que a mesma aula exige duas seções antes — subestimando o caminho real em cerca de 20%. A razão entre os dois casos, que é o que o exemplo ensina, continua correta.

**Correção aplicada.** O texto passou a dizer que o caminho central é a ida e volta pela espessura da pedra — **cúpula mais parede de cinta** — e que os números citados são a **parcela que a cúpula controla**. Nenhum número alterado.

---

## 🟡 Amarelo 2 — a01 · material mole "não guarda o brilho de espelho de uma faceta"

**Onde:** `06-cabochao-aula-01`, Gatilho 3.

A afirmação vale para **uso em joia**, não como possibilidade técnica: fluorita, calcita e esfalerita são rotineiramente facetadas como pedra de coleção, e a lista da aula ("serpentina, fluorita, calcita, obsidiana e âmbar quase sempre vão para cabochão") lida sem qualificador contradiz o que qualquer vitrine de coleção mostra.

**Correção aplicada.** Qualificador "em **uso de joia**" no critério, parêntese sobre pedra de coleção, e "**quando o destino é joia**" na lista. Alegação `CAB-ESC-TEN-001` reescrita: "o critério é de uso, não de possibilidade".

---

## 🟡 Amarelo 3 — a01 e a05 · "fogo" para o jogo de cores da opala

O termo é corrente no jargão de oficina, mas o curso vai usar "fogo" no sentido óptico de **dispersão** no módulo 08 (brilho, dispersão, cintilação). Duas palavras iguais para dois fenômenos diferentes, dentro do mesmo curso, sem aviso.

**Correção aplicada.** No corpo das duas aulas o termo foi substituído por "jogo de cores" / "camada de cor" (custo zero de palavras) e a **entrada de vocabulário** da a05 recebeu a glosa do duplo uso, remetendo ao módulo 08. A tabela de vocabulário fica fora da régua de LC-02, então a correção não consumiu orçamento.

---

## 🟡 Amarelo 4 — a06 · contradição interna do cabochão duplo

A aula dizia, na mesma seção, que o duplo "serve para material **fino demais** para dar altura de cúpula de um lado só" e que "as duas cúpulas consomem **mais** material em altura". As duas afirmações são verdadeiras em condições diferentes e a aula não as separava.

**Correção aplicada.** O caso do material fino foi explicitado (distribuir a pouca espessura em duas curvas rasas, para que nenhuma face fique plana) e o custo foi condicionado ("mantida a mesma cúpula superior do simples, a segunda curva pede espessura a mais: o duplo economiza material **fino**, não material em geral"). Tabela-resumo ajustada.

---

## 🔵 Azul 1 — a04 · o bisel da aresta inferior da cinta (aplicado)

Enriquecimento de fonte, aplicado junto com o 🔴 1 porque completa a geometria da cinta e é a razão prática pela qual a aresta de baixo não fica viva: aresta viva ali lasca no momento de cravar. Entra na alegação nova `CIN-CONIC-BISEL-001`.

## 🔵 Azul 2 — módulo · LC-08 ausente nas seis aulas (resolvido de passagem)

Varredura por marcador de controvérsia: **zero** ocorrências nas seis aulas do módulo 06 (o módulo 04 tem quatro aulas com controvérsia declarada; o módulo 05, uma). A correção do 🟠 5 instalou uma — a posição da dopagem na sequência —, declarada como pergunta aberta e sem arbitrar o debate, na forma que LC-08 pede. Registrado aqui como observação para a revisão didática decidir se o módulo precisa de mais.

---

## ⚪ Branco 1 — a05 · a indexação do plano das lamelas da pedra da lua

Verificado e **mantido como está**. A aula diz que as lamelas de exsolução ficam "num plano cristalográfico definido, ligado à clivagem principal" e que a base vai "**paralela ao plano das lamelas** (aproximadamente o plano de clivagem principal)". As fontes confirmam sem ressalva a regra de corte — a base do cabochão paralela ao plano das camadas — e confirmam o mecanismo (espalhamento da luz de comprimento de onda curto por lamelas de ortoclásio e albita, com as lamelas mais finas produzindo espalhamento de tipo Rayleigh e o azul). A **indexação cristalográfica exata** do plano de exsolução, porém, varia entre fontes. A aula acertou ao não indexá-lo e ao hedgear com "aproximadamente": indexar aqui seria precisão que a evidência disponível não sustenta. Nada a corrigir.

---

## Verificado sem achado (amostra do que foi conferido e passou)

- **Chatoyance (a05).** Um único conjunto de fibras; cada fibra reflete num plano perpendicular ao seu comprimento; a faixa resultante cruza a pedra **perpendicular** às fibras; base **paralela** às fibras e eixo longo da oval **paralelo** às fibras; cúpula mais alta = olho mais fino e nítido. Tudo confere.
- **Asterismo no coríndon (a05).** Três conjuntos de rutilo a 120° no plano perpendicular ao eixo c → 6 raios. Confere.
- **Altura da cúpula de estrela ~1/2 da largura (a05, `FEN-STAR-ALT-001`).** Confere: o cabochão alto é definido por razão altura/largura acima de 0,5, e a razão dada — concentrar a luz numa estrela mais apertada, o que um domo raso não faz — é a da literatura.
- **Localizar o eixo c sob luz pontual (a05).** Método correto. Recebeu, de passagem, a ressalva de hábito (num cristal tabular de coríndon o eixo c é a direção **curta**, perpendicular à chapa), para que o leitor não procure sempre "o eixo longo do prisma".
- **Adularescência (a05).** Mecanismo e orientação confirmados — ver ⚪ 1.
- **Jogo de cores (a05).** Difração por grade tridimensional de esferas de sílica de tamanho uniforme; cor dependente do tamanho das esferas e do ângulo; corte seguindo a camada de cor, domo baixo para não atravessá-la. Confere.
- **Razão de cúpula (a03, `DOM-ALT-RAZ-001` e `DOM-ESC-RAZAO-001`).** ~1/3 como ponto de partida, faixa 1/4–1/2; domo baixo para material escuro (encurta o caminho e clareia), domo alto para material pálido (alonga e adensa). Confere com a literatura de proporção de cabochão, e a aula está corretamente enquadrada por LC-05 (valor **e** faixa **e** fonte, declarados como alvo de trabalho).
- **Cabochão oco para almandina (a06, `VAR-OCO-ESCURO-001`).** Confere, e é prática documentada de longa data: escavar o verso da almandina escura para deixar a luz passar.
- **Calibres (a02, a06).** Oval 25×18, 18×13, 14×10, 8×6; redondo 6, 8, 10 mm. São tamanhos de catálogo correntes. Confere.
- **Propagação do defeito de contorno (a04, `CIN-CONT-ASSIM-001`).** A cadeia correção não-local → encolhimento → perda de calibre → cúpula descentrada → razão de cúpula fora do alvo é internamente consistente e os números do exemplo (0,4 mm de reta → ~24,3×17,4; ápice ~0,3 mm fora do centro) fecham com a geometria. Confere, e a aula já se protege com "não tomar os 0,4 mm e o 25×18 como valores de regra".
- **Defeitos de base (a04).** Convexa → balanço; côncava → apoio só na borda, prende sujeira; fora de esquadro → pedra montada olhando torto; fosca sob translúcido → luz volta espalhada. Confere.
- **Variantes calibrado e freeform (a06).** O calibrado inverte a prioridade do módulo 05 (contorno manda sobre rendimento) e o freeform é livre só no perímetro. Confere.

---

## Alegações corrigidas

`CIN-INCL-UNDER-001` · `FEN-ASTER-EIXOC-001` · `CAB-ESC-FEN-001` · `CAB-ESC-TEN-001` · `VAR-DUP-TRANSL-001` · `PRE-ORDEM-FIXA-001` · `PRE-CINTA-VERT-001` · `DOM-ENG-PAREDE-001` · `DOM-CAMINHO-COR-001`

## Alegações criadas

`CIN-CONIC-BISEL-001` (a04) · `FEN-ASTER-CONT-001` (a05) · `FEN-ASTER-DIOP-001` (a05)

## Alegações renomeadas

Nenhuma. Todas as 34 herdadas já estavam no formato de 4 segmentos.

---

## Material derivado

**Nenhum.** O módulo 06 não tinha questionário nem baralho quando esta auditoria rodou — que é exatamente o efeito pretendido do gate. Nada a propagar; o `gerador-de-questionarios` recebe o módulo já limpo.

---

## Encaminhado à revisão didática

1. **a04 — a aula fechou em 1599, um ponto do teto.** A correção do 🔴 1 acrescentou um bloco novo (a geometria correta da cinta) que foi financiado por corte de redundância em cinco pontos: o fecho de "Por que cinta e base parecem triviais", a introdução do ponto chato, o "Custo real da opção B", a seção "O que o engaste não conserta" e a causa da base côncava. Nenhum desses cortes removeu conteúdo — todos removeram repetição do Recap —, mas a revisão didática deve confirmar que o ritmo da aula não ficou seco e que a a04 não perdeu a respiração que tinha.

2. **a05 — folga de 3 palavras.** Mesmo caso, mais apertado. Ficou registrado que qualquer melhoria didática na a05 precisa ser financiada por corte, e que o texto instalado pelas correções (aritmética dos feixes, eixo de simetria, granada isométrica, diopsídio a 90°, redondo × oval) **não pode** ser o financiador.

3. **Volume do módulo como um todo.** As seis aulas entraram na auditoria entre 1275 e 1577 palavras, bem abaixo dos módulos 01–05 (~1590–1600). Não é violação de LC-02 — é teto, não piso — e a auditoria devolveu as seis para a faixa 1330–1599. Mas a a01 e a a06, as duas mais curtas antes e depois, merecem exame didático explícito: **exemplo insuficiente, conceito subdesenvolvido ou recap que não recapitula** por efeito da concisão. Elas têm folga para receber desenvolvimento (a06 fechou em 1330, com 270 palavras de margem; a03, em 1397, com 200).

4. **a05 — carga de conceitos.** Quatro mecanismos ópticos distintos mais quatro regras de orientação numa aula só, agora com a distinção adicional entre eixo c e eixo de simetria genérico. Está correto e é o objeto do objetivo `oa05`, mas é a aula mais densa do módulo e a revisão deve julgar se a estrutura em quatro blocos paralelos basta como organizador prévio.

5. **LC-08.** Ver 🔵 2: o módulo tinha zero controvérsias declaradas e a auditoria instalou uma (a02, posição da dopagem). Cabe à revisão didática decidir se o módulo pede mais alguma.

---

## Fontes consultadas nesta auditoria

- Sinkankas, *Gem Cutting: A Lapidary's Manual* — capítulo de cabochão: seleção de material, sequência de preformação, proporção da cúpula, defeitos de cinta e base, cabochão duplo e oco, orientação de pedra fenomenal.
- International Gem Society, *Lapidary Fundamentals: Cabochon Cutting* (acesso 2026-09-03) — a área vertical da lateral que apoia o aro, o bisel de proteção da aresta inferior, a sequência laje → gabarito → serra → desbaste.
- SUVA Lapidary Supply, *Lapidary 101: How to Make a Cabochon* (acesso 2026-09-03) — ângulo de cinta de 10° a 15°, bisel da base, base plana para engaste, dopagem logo após o recorte.
- Diamond Pacific, *Genie and Pixie Cab Rests* — cab rest de 12,5°.
- GIA — asterismo, chatoyance, adularescência e jogo de cores: mecanismo e orientação de corte; critérios de qualidade da pedra estrela.
- Lapidary Journal / Rock & Gem — razão de cúpula, parede de cinta, ponto chato de contorno, freeform, domo baixo para opala.
- Literatura gemológica corrente sobre diopsídio estrela (acesso 2026-09-03) — duas direções de agulhas; os raios não se cruzam a 90° por propriedade do material.
- Literatura gemológica corrente sobre pedra da lua e adularescência (acesso 2026-09-03) — exsolução ortoclásio/albita, espalhamento, base paralela ao plano das lamelas.
- Literatura corrente sobre cabochão oco em almandina (acesso 2026-09-03) — escavação do verso para clarear material escuro.
- William Holland School of Lapidary Arts e a taxonomia das guildas — cabochão como disciplina; preformação como etapa distinta; calibrado para joia de série.
- AGTA Gemstone Information Manual — conformidade dimensional e requisitos do engaste de aro.
- `_contexto.md` deste curso — contrato `ensino-medio-com-gemologia-v1`, régua de `palavras_corpo`, formato de `claim_id`, regra dura de não-competência-de-bancada.
