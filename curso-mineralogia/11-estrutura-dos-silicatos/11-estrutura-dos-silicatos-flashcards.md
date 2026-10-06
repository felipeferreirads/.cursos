# Flashcards — Módulo 11: Arquitetura dos silicatos

**Módulo:** [[11-estrutura-dos-silicatos-modulo|Módulo 11 — Arquitetura dos silicatos]]
**Total:** 65 cards — 57 Basic + 8 Cloze
**Faixa de IDs:** `mineralogia-m11-fb001`–`fb057` · `mineralogia-m11-fc001`–`fc008`
**Auditoria:** aprovada em 2026-10-06, sem achados 🔴/🟠 em aberto — gate liberado.
**Didática:** revisão concluída em 2026-10-06
**Questionário:** final cumulativo gerado em 2026-10-06 (15 questões, 4 objetivos cobertos)
**Gerado em:** 2026-10-06, contra as aulas já auditadas e revisadas do módulo.

> [!info] Primeira geração
> Não há baralho prévio deste módulo. Todos os IDs são novos. Importe os dois CSVs num deck limpo.

## Arquivos para importar

| Arquivo | Tipo de nota no Anki | Campos |
|---|---|---|
| `11-estrutura-dos-silicatos-flashcards-basic.csv` | Basic | id, frente, verso, tags, objetivo, aula, dificuldade, fonte |
| `11-estrutura-dos-silicatos-flashcards-cloze.csv` | Cloze | id, texto, extra, tags, objetivo, aula, dificuldade, fonte |

> [!tip] Importação no Anki
> Importe os dois **separadamente**. Marque "Campos separados por ponto-e-vírgula" e mapeie `id` como primeiro campo. As tags são hierárquicas (`mineralogia::m11::...`).

## Distribuição

| Aula | Objetivo | Basic | Cloze | Total |
|---|---|---|---|---|
| a01 — O tetraedro SiO₄ e a ligação Si–O | `oa01` | 12 | 1 | 13 |
| a02 — Polimerização: as seis classes | `oa02` | 13 | 3 | 16 |
| a03 — Substituição Al↔Si e compensação | `oa03` | 10 | 2 | 12 |
| a04 — Da estrutura à propriedade | `oa04` | 15 | 1 | 16 |
| a05 — Panorama e mapa da sistemática | `oa02` | 7 | 1 | 8 |

**Cobertura:** todos os objetivos do módulo têm card. Nenhum card órfão.

## Critérios aplicados

- **Cada card é rastreável a uma frase das aulas auditadas** (`11-estrutura-dos-silicatos-auditoria.md`); nenhuma estrutura, coordenação, raio, razão ou densidade foi acrescentada fora delas.
- **Todas as razões Si:O e cargas foram recalculadas em Python** antes de virar card.
- **As três correções da auditoria aparecem só na versão corrigida** (Al como o cátion tetraédrico mais comum, não o único; asbesto não é só anfibólio e o sítio A entre as vigas; Nickel-Strunz com 9.H e 9.J).
- **Nenhum card Basic repete o fato de um Cloze.**
- **Cloze com no máximo 3 lacunas e sem chaves dentro das lacunas.**
- **Nenhum card depende de figura.**

## Cards Basic

| ID | Frente | Verso | Aula | Objetivo |
|---|---|---|---|---|
| `mineralogia-m11-fb001` | Qual é a distância Si–O no tetraedro SiO₄, aproximadamente? | ~1,61–1,62 Å (1,61 pela soma dos raios de Shannon; ~1,62 medido). | a01 | `oa01` |
| `mineralogia-m11-fb002` | Qual é o ângulo O–Si–O no tetraedro SiO₄? | ~109,5°, o do tetraedro regular. | a01 | `oa01` |
| `mineralogia-m11-fb003` | Qual é a carga do grupo SiO₄ isolado? | −4 (Si +4; quatro O −2). | a01 | `oa01` |
| `mineralogia-m11-fb004` | Qual é a força de ligação (s) do Si em tetraedro, e por que ela importa? | s = 4/4 = 1, exatamente metade da carga do O: o O pode receber a outra metade de outro Si. | a01 | `oa01` |
| `mineralogia-m11-fb005` | O que é um oxigênio ponte? | O compartilhado por dois tetraedros (Si–O–Si); recebe 1 + 1 = 2. | a01 | `oa01` |
| `mineralogia-m11-fb006` | Na forsterita, de onde vêm as forças que completam os 2 de cada oxigênio? | 1 do Si e 1/3 de cada um dos três Mg octaédricos vizinhos (O não ponte). | a01 | `oa01` |
| `mineralogia-m11-fb007` | Por que os grupos CO₃²⁻ e SO₄²⁻ não polimerizam como o SiO₄? | As forças de C (4/3) e S (3/2) passam da metade da carga do O: um O entre dois deles receberia mais que 2. | a01 | `oa01` |
| `mineralogia-m11-fb008` | Por que os tetraedros SiO₄ não compartilham arestas nos silicatos comuns? | Os dois Si⁴⁺ ficariam a ~1,86 Å; compartilhando só vértices, ficam a ~3,06 Å. | a01 | `oa01` |
| `mineralogia-m11-fb009` | Por que um O não pode ser compartilhado por três tetraedros de Si? | Receberia 1 + 1 + 1 = 3, mais que os 2 de que precisa. | a01 | `oa01` |
| `mineralogia-m11-fb010` | Em que faixa varia o ângulo Si–O–Si nos silicatos? | De cerca de 120° a 180° (~144° no quartzo). | a01 | `oa01` |
| `mineralogia-m11-fb011` | O que significa o n na notação Qⁿ? | O número de oxigênios ponte do tetraedro (de 0 a 4). | a01 | `oa01` |
| `mineralogia-m11-fb012` | De que técnica vem a notação Qⁿ? | Da ressonância magnética nuclear do silício-29. | a01 | `oa01` |
| `mineralogia-m11-fb013` | Quantos O há por Si num tetraedro que compartilha n vértices? | 4 − n/2. | a02 | `oa02` |
| `mineralogia-m11-fb014` | Quais são as unidades dos ciclossilicatos de anel de 3 e de anel de 6? | Si₃O₉ (−6) e Si₆O₁₈ (−12); Si:O = 1:3 nos dois. | a02 | `oa02` |
| `mineralogia-m11-fb015` | Qual é a unidade e a carga de um inossilicato de cadeia simples? | SiO₃ (−2), também escrita Si₂O₆ (−4); Si:O = 1:3. | a02 | `oa02` |
| `mineralogia-m11-fb016` | Por que a cadeia dupla tem em média 2,5 vértices compartilhados por tetraedro? | Metade dos tetraedros divide 2 vértices e metade divide 3, para ligar as duas cadeias. | a02 | `oa02` |
| `mineralogia-m11-fb017` | Por que o quartzo, SiO₂, não precisa de outros cátions? | No arcabouço todo O é ponte: a unidade SiO₂ tem carga zero. | a02 | `oa02` |
| `mineralogia-m11-fb018` | Se anel e cadeia simples têm a mesma razão Si:O, o que os distingue? | A topologia: o anel fecha; a cadeia continua indefinidamente. | a02 | `oa02` |
| `mineralogia-m11-fb019` | Que oxigênios se deixam de fora ao calcular a razão Si:O de uma fórmula? | Os de OH, H₂O e os O ligados só a outros cátions (fora da unidade silicática). | a02 | `oa02` |
| `mineralogia-m11-fb020` | Em que classe fica a hemimorfita, Zn₄Si₂O₇(OH)₂·H₂O? | Sorossilicato (unidade Si₂O₇). | a02 | `oa02` |
| `mineralogia-m11-fb021` | Em que classe fica a tremolita, Ca₂Mg₅Si₈O₂₂(OH)₂, e por quê? | Inossilicato de cadeia dupla (anfibólio): Si₈O₂₂ = 2 × Si₄O₁₁. | a02 | `oa02` |
| `mineralogia-m11-fb022` | Em que classe fica a cianita, Al₂SiO₅, e por quê? | Nesossilicato: SiO₄ mais um O extra ligado só aos Al. | a02 | `oa02` |
| `mineralogia-m11-fb023` | O epidoto tem que unidades silicáticas? | SiO₄ e Si₂O₇ na mesma estrutura; é classificado entre os sorossilicatos. | a02 | `oa02` |
| `mineralogia-m11-fb024` | Qual é a coordenação do Be e do Al no berilo, Be₃Al₂Si₆O₁₈? | Be em NC IV; Al em NC VI. | a02 | `oa02` |
| `mineralogia-m11-fb025` | Qual é a coordenação do Zr no zircão? | NC VIII. | a02 | `oa02` |
| `mineralogia-m11-fb026` | Que carga ganha a unidade silicática para cada Al³⁺ que entra no lugar de um Si⁴⁺? | −1 a mais. | a03 | `oa03` |
| `mineralogia-m11-fb027` | Que cátion compensa a carga do Al no feldspato potássico? | O K⁺, nos vazios do arcabouço (KAlSi₃O₈). | a03 | `oa03` |
| `mineralogia-m11-fb028` | Que vetor de troca leva da albita à anortita? | CaAlNa₋₁Si₋₁. | a03 | `oa03` |
| `mineralogia-m11-fb029` | Como se passa do talco à flogopita? | Troca-se 1 Si por Al e acrescenta-se K entre as lâminas: KMg₃(AlSi₃O₁₀)(OH)₂. | a03 | `oa03` |
| `mineralogia-m11-fb030` | Na muscovita KAl₂(AlSi₃O₁₀)(OH)₂, quantos Al são tetraédricos e quantos octaédricos? | 1 tetraédrico (dentro dos parênteses) e 2 octaédricos. | a03 | `oa03` |
| `mineralogia-m11-fb031` | Que razão se usa para classificar um silicato com Al nos tetraedros? | (Si + Al tetraédrico) : O. | a03 | `oa03` |
| `mineralogia-m11-fb032` | Por que a nefelina é tectossilicato, se Si:O = 1:4? | Com o Al tetraédrico, (Si + Al):O = 8:16 = 1:2: arcabouço. | a03 | `oa03` |
| `mineralogia-m11-fb033` | Por que a jadeíta, NaAlSi₂O₆, é inossilicato e a leucita, KAlSi₂O₆, é tectossilicato? | Na jadeíta o Al é octaédrico (unidade Si₂O₆); na leucita é tetraédrico ((Si + Al):O = 1:2). | a03 | `oa03` |
| `mineralogia-m11-fb034` | O que diz a regra de Loewenstein (1954)? | Dois tetraedros de Al não compartilham o mesmo oxigênio. | a03 | `oa03` |
| `mineralogia-m11-fb035` | Qual é a maior razão Al:Si possível nos tetraedros de arcabouços e folhas? | 1:1, com Si e Al alternados (anortita). | a03 | `oa03` |
| `mineralogia-m11-fb036` | Por onde passa a clivagem de um silicato, em geral? | Entre as unidades silicáticas, pelas ligações mais fracas, sem cortar as Si–O. | a04 | `oa04` |
| `mineralogia-m11-fb037` | Que clivagem e que hábito se esperam de um nesossilicato? | Clivagem ausente ou pobre; hábito equidimensional (granada, olivina). | a04 | `oa04` |
| `mineralogia-m11-fb038` | Que nesossilicato é exceção ao hábito equidimensional? | O zircão, prismático. | a04 | `oa04` |
| `mineralogia-m11-fb039` | O que é uma viga em I nos piroxênios e anfibólios? | Duas cadeias de tetraedros, pontas voltadas uma para a outra, com a faixa de octaedros entre elas. | a04 | `oa04` |
| `mineralogia-m11-fb040` | Por onde passam as clivagens {110} dos piroxênios e anfibólios? | Entre as vigas em I, pelos sítios de cátions maiores (M2; M4 e A). | a04 | `oa04` |
| `mineralogia-m11-fb041` | Que ângulos formam as clivagens dos piroxênios? | ~87° e ~93°. | a04 | `oa04` |
| `mineralogia-m11-fb042` | Que ângulos formam as clivagens dos anfibólios? | ~56° e ~124°. | a04 | `oa04` |
| `mineralogia-m11-fb043` | Por que o ângulo de clivagem dos anfibólios é mais fechado que o dos piroxênios? | A cadeia dupla torna a viga duas vezes mais larga ao longo de b; os planos que a contornam se cruzam num ângulo menor. | a04 | `oa04` |
| `mineralogia-m11-fb044` | Que clivagem tem um filossilicato? | Uma clivagem basal perfeita, {001}. | a04 | `oa04` |
| `mineralogia-m11-fb045` | Por que o quartzo não tem clivagem? | O arcabouço de Si–O é forte nas três direções; ele se parte em fratura conchoidal. | a04 | `oa04` |
| `mineralogia-m11-fb046` | Quantas clivagens têm os feldspatos, e a que ângulo? | Duas, boas, a cerca de 90°. | a04 | `oa04` |
| `mineralogia-m11-fb047` | Qual é a ordem de densidade de forsterita, enstatita, talco e quartzo? | Forsterita (~3,28) > enstatita (~3,19) > talco (~2,7–2,8) > quartzo (2,65). | a04 | `oa04` |
| `mineralogia-m11-fb048` | Em que condição vale a regra 'mais polimerizado, menos denso'? | Só comparando silicatos de cátions parecidos (o zircão, com Zr, é denso). | a04 | `oa04` |
| `mineralogia-m11-fb049` | Qual é a série descontínua de Bowen? | Olivina → piroxênio → anfibólio → biotita, depois feldspato potássico, muscovita e quartzo. | a04 | `oa04` |
| `mineralogia-m11-fb050` | Por que o plagioclásio foge da correlação entre polimerização e ordem de cristalização? | É tectossilicato e cristaliza desde o início, numa série contínua paralela. | a04 | `oa04` |
| `mineralogia-m11-fb051` | Em que módulo da sistemática deste curso se estudam os inossilicatos? | No módulo 34 (piroxênios, piroxenoides e anfibólios). | a05 | `oa02` |
| `mineralogia-m11-fb052` | Em que módulo se estudam neso-, soro- e ciclossilicatos? | No módulo 33. | a05 | `oa02` |
| `mineralogia-m11-fb053` | Como Nickel-Strunz e Dana classificam o quartzo? | Nickel-Strunz: óxido (4.DA.05); Dana: tectossilicato. | a05 | `oa02` |
| `mineralogia-m11-fb054` | O que é a periodicidade de uma cadeia, na classificação de Liebau? | O número de tetraedros até a cadeia se repetir. | a05 | `oa02` |
| `mineralogia-m11-fb055` | Qual é a periodicidade da cadeia do piroxênio, da wollastonita e da rodonita? | 2, 3 e 5. | a05 | `oa02` |
| `mineralogia-m11-fb056` | O que é um piroxenoide? | Silicato de cadeia simples que não é piroxênio: a cadeia se repete a cada 3, 5 ou mais tetraedros. | a05 | `oa02` |
| `mineralogia-m11-fb057` | Qual é a multiplicidade da cadeia de um anfibólio, e o que ela indica? | 2: duas cadeias simples ligadas lado a lado (cadeia dupla). | a05 | `oa02` |

## Cards Cloze

| ID | Texto | Extra | Aula | Objetivo |
|---|---|---|---|---|
| `mineralogia-m11-fc001` | Neso {{c1::SiO₄}} (Si:O 1:4); soro {{c2::Si₂O₇}} (2:7); tecto {{c3::SiO₂}} (1:2). | Cargas: −4, −6 e 0. | a02 | `oa02` |
| `mineralogia-m11-fc002` | Ino de cadeia dupla: unidade {{c1::Si₄O₁₁}}, razão Si:O {{c2::4:11}}. | Carga −6. | a02 | `oa02` |
| `mineralogia-m11-fc003` | Filossilicato: unidade {{c1::Si₂O₅}} (ou Si₄O₁₀), razão Si:O {{c2::2:5}}. | Cada tetraedro divide 3 vértices. | a02 | `oa02` |
| `mineralogia-m11-fc004` | Q{{c1::0}} = tetraedro isolado; Q{{c2::4}} = arcabouço. | n = oxigênios ponte por tetraedro. | a01 | `oa01` |
| `mineralogia-m11-fc005` | Soma de forças num O ponte: Si–O–Si = {{c1::2}}; Si–O–Al = {{c2::1,75}}; Al–O–Al = {{c3::1,5}}. | Base da regra de Loewenstein. | a03 | `oa03` |
| `mineralogia-m11-fc006` | Do quartzo à albita: Si₄O₈ → {{c1::AlSi₃O₈}} (−1) + Na⁺ = {{c2::NaAlSi₃O₈}}. | Al tetraédrico compensado por cátion. | a03 | `oa03` |
| `mineralogia-m11-fc007` | Ângulo entre as clivagens {110} = 2 × arctan({{c1::a·senβ}} / {{c2::b}}), e o suplemento. | Diopsídio: 93,0° e 87,0°; tremolita: 55,7° e 124,3°. | a04 | `oa04` |
| `mineralogia-m11-fc008` | Nickel-Strunz: 9.D = {{c1::inossilicatos}}; 9.E = {{c2::filossilicatos}}; 9.G = {{c3::zeólitas}}. | 9.F: tectossilicatos sem água zeolítica. | a05 | `oa02` |

## Navegação

[[11-estrutura-dos-silicatos-modulo|← Hub do módulo]] · [[11-estrutura-dos-silicatos-questionario-final|Questionário final]] · [[11-estrutura-dos-silicatos-auditoria|Auditoria do módulo]]

## Histórico

- 2026-10-06 — primeira geração (fb001–fb057, fc001–fc008). Antes de receber ID definitivo, cinco cards Basic que repetiam o fato de um Cloze foram retirados e dois apontados pelo `validate_flashcards.py` como quase-duplicatas (O ponte × não ponte; periodicidade × multiplicidade) foram reformulados.
