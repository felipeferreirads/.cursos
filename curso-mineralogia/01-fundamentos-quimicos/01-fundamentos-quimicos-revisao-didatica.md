# Revisão didática: Módulo 01 — Fundamentos químicos: átomo, tabela periódica e ligação

**Revisado em:** 2026-09-30 · **Modo:** `review-and-fix`
**Material:** `01-fundamentos-quimicos/` — 6 aulas (`a01`–`a06`) + hub do módulo
**Rodou depois da:** [[01-fundamentos-quimicos-auditoria|auditoria científica]] de 2026-09-30 (🔴 1 · 🟠 12 · ⚪ 1, todos corrigidos). A ordem está certa: primeiro a correção factual, depois a didática.
**Contrato de nível:** `ensino-medio-sem-geologia-v1` (LC-01 a LC-08 aplicados; o LC-09, degrau de inferência, vale só para os módulos 25-27, 37 e 50 e **não se aplica** a este módulo)
**Veredito:** **Bem ensinado com ressalvas.** As ressalvas 🔴/🟠/🟡 foram corrigidas nesta revisão.

## Resumo

🔴 0 bloqueiam · 🟠 6 prejudicam · 🟡 8 atrito · 🔵 3 sugestões — **17 achados**, 14 corrigidos, 3 (🔵) em aberto e não bloqueantes

**Carga estimada por aula** (conta só os conceitos que são de fato novos para quem saiu do ensino médio; o que o ensino médio já dá conta como reativado):

| Aula | Conceitos novos | Reativados do ensino médio | Exemplos | palavras_corpo | Duração |
|---|---|---|---|---|---|
| a01 | 4 (orbital como região de probabilidade; Pauli e Hund; sutileza 4s/3d; tabela como mapa de blocos) | átomo, camadas, distribuição eletrônica | 4 configurações no corpo + 1 trabalhado (Fe, 5 passos) + Mn | 1585 | ~28 min |
| a02 | 4 (Zef e blindagem; três tendências; ionizações sucessivas; escala de Pauling) | tabela periódica, íon | 2 tabelas de EI, 1 de χ + 1 trabalhado (6 passos) | 1482 | ~28 min |
| a03 | 4 (estado de oxidação como contabilidade; valência variável; valência mista; ressalva da convenção) | Nox, gás nobre, íon | SiO₂, Al₂O₃, Fe, Mn, S + 1 trabalhado (3 casos) | 1391 | ~28 min |
| a04 | 4 (contínuo e triângulo; caráter iônico de Pauling; ligação → propriedade; limites do χ) | as três ligações do ensino médio | NaCl, MgO, diamante, Cu + 1 trabalhado (4 casos) | 1465 | ~28 min |
| a05 | 3 (van der Waals; ponte de hidrogênio; cristal com mais de uma ligação / anisotropia) | molécula de água, polaridade | 5 minerais no corpo + 1 trabalhado (2 minerais) | 1455 | ~27 min |
| a06 | 4 (composição em óxidos; razão molar; escalas de unidade; estimativa de ordem de grandeza) | mol, massa molar, porcentagem | forsterita, pirita + 3 problemas + quartzo | 1337 | ~30 min |

Nenhuma aula passa de 4 ideias novas independentes, e todas ficam abaixo do teto de ~1600 palavras (LC-02). Não há sobrecarga que peça divisão.

---

## Achados

### 🟠 1. A regra "grupo no bloco d" só aparecia dentro do exemplo trabalhado

**Tipo:** objetivo parcialmente coberto · salto no exemplo trabalhado
**Onde:** `a01` · "A tabela periódica como mapa de subcamadas" × "Exemplo trabalhado", passo 4
**Problema:** a metade do `oa01` que pede "relacionar a configuração eletrônica à posição do elemento na tabela" era ensinada no corpo só para os blocos s e p ("o grupo indica quantos elétrons de valência existem"). A regra do bloco d, em que o número do grupo é a soma dos elétrons s e d, aparecia pela primeira vez no passo 4 do exemplo ("o grupo é 8, seis elétrons d mais dois s") e em "Erros comuns". Quem estuda sozinho tende a tomar o passo 4 como fato particular do ferro, e não como método. Aí a avaliação pergunta o grupo do manganês e ele não sabe responder.
**Correção aplicada:** uma frase no corpo, logo depois da regra dos blocos s e p: "No bloco d, some os elétrons s e d de valência: o ferro (4s² 3d⁶) soma 8 e está no grupo 8." O Recap ganhou "no bloco d, s + d dá o grupo".
**Escopo:** correção local. A regra generaliza a alegação já auditada `QUI-CONF-FE-001` (Fe grupo 8, Mn grupo 7) e foi registrada no rodapé como `QUI-TAB-GRUPOD-001`, com status **pendente** para a próxima passagem do auditor.

### 🟠 2. O método de classificação não decidia o caso metálico, e o exemplo (c) andava em círculo

**Tipo:** exemplo trabalhado com raciocínio circular · desalinhamento com o `oa04` ("classificar")
**Onde:** `a04` · "Três extremos, um contínuo"; "Exemplo trabalhado" (c); "Método geral"; Recap
**Problema:** a correção de auditoria `QUI-LIG-METAL-001` acertou o fato (o χ de Pauling do ouro é 2,54 e o do cobre é igual ao do silício, 1,90). Com isso, a regra de bolso "Δχ pequeno e χ baixo → metálica" deixou de funcionar para todos os exemplos metálicos da própria aula, e nenhum critério operacional entrou no lugar. O exemplo (c) classificava o cobre como metálico "porque os elétrons de valência se deslocalizam pelo cristal", que é a definição de ligação metálica. Um aluno consegue acompanhar a leitura, mas não consegue aplicar o método a um caso novo. Ao seguir o passo (2) do método ("χ alto ou baixo?"), ele classificaria Cu e Si do mesmo jeito.
**Correção aplicada:** (i) em "Três extremos", depois da regra de bolso: "O critério que funciona na prática: nos metais nativos e nas ligas naturais, formados só por átomos de metais (Cu, Au, Ag, Fe-Ni), a ligação é metálica." (ii) O exemplo (c) passou a dizer explicitamente que o χ sozinho não decide, porque o silício tem o mesmo 1,90, e que o que decide é serem átomos de um metal de transição num metal nativo. (iii) O passo (2) do método inclui "e se os dois átomos são de metais". (iv) A primeira linha do Recap recebeu a mesma regra.
**Escopo:** correção local. A heurística reformula o parágrafo auditado da ligação metálica, que já listava exatamente esses metais nativos. Foi registrada como `QUI-LIG-METALREGRA-001`, **pendente** de conferência pelo auditor.

### 🟠 3. Fórmula exponencial sem reativação matemática e sem conta mostrada (LC-06)

**Tipo:** matemática usada antes de reativada · salto no exemplo
**Onde:** `a04` · "O meio-termo: quase toda ligação é mista"; "Exemplo trabalhado" (a), (b), (d)
**Problema:** I = 1 − e^(−Δχ²/4) é a única exponencial do módulo. O contrato manda reativar a matemática antes do uso, e a aula não dizia o que é o "e" nem mostrava uma única conta. Os quatro casos do exemplo saltavam direto de Δχ para a porcentagem ("Δχ = 2,13 → cerca de 68%"). Quem tentasse reproduzir a conta, ou quem recebesse na prova um Δχ novo, ficava sem caminho.
**Correção aplicada:** duas frases logo depois da fórmula: o que é e ≈ 2,718, a tecla eˣ da calculadora e a conta completa para Si–O (1,54² ÷ 4 = 0,593; e^(−0,593) ≈ 0,553; I ≈ 0,447, ou ~45%).
**Escopo:** correção local. A aritmética foi refeita e bate com o valor auditado de 44,7% (`QUI-LIG-PAULING-001`). Registrada como `QUI-LIG-PAULCALC-001` (verificada).

### 🟠 4. As propriedades físicas que o `oa04` pede eram usadas antes de definidas

**Tipo:** termo técnico central usado antes de definido (LC-01) · ordem interna invertida
**Onde:** `a01` · "Conexão com a mineralogia"; `a04` · "Ligação iônica" (clivagem, "dureza Mohs 2–2,5"), "Ligação covalente" (onde a escala de Mohs é enfim explicada), "Erros comuns" (onde "dureza" é enfim definida), "refratário"
**Problema:** o `oa04` pede relacionar a ligação a propriedades físicas, mas as propriedades não eram apresentadas. "Clivagem" aparecia na `a01` e no corpo da `a04` e só era definida no vocabulário da `a05`. "Dureza Mohs" aparecia na seção iônica, e a escala só era explicada duas seções depois. A definição de dureza ("resistência ao risco") só vinha em "Erros comuns". Para quem não tem geologia, clivagem é palavra desconhecida. Quanto à dureza, o sentido do dia a dia (duro = difícil de quebrar) é justamente o modelo errado que a própria aula combate ao separar dureza de tenacidade.
**Correção aplicada:** duas entradas novas no vocabulário da `a04`, "dureza (escala de Mohs)" e "clivagem", que passou a 10 termos, dentro do LC-03. Na `a01`, um aposto em "clivagem, a tendência de quebrar em planos lisos". Na `a04`, "refratário (resistente ao calor)".
**Escopo:** correção local. As definições usam só fatos já auditados: talco 1 e diamante 10, escala ordinal, resistência ao risco.

### 🟠 5. "Spin alto", "spin baixo" e "coordenação octaédrica" sem definição, com contradição aparente com a aula 01

**Tipo:** termo técnico usado sem definição · risco de modelo mental contraditório
**Onde:** `a03` · raios de Fe²⁺/Fe³⁺ ("em coordenação octaédrica… raios de Shannon, spin alto"); "O que não concluir" (pirita, "Fe²⁺ de spin baixo")
**Problema:** os três termos entraram com as correções e precisões da auditoria e ficaram sem definição. O caso de "spin baixo" é o mais delicado: a `a01` ensina, com a regra de Hund, que o Fe²⁺ (3d⁶) tem 4 elétrons desemparelhados, e a `a03` diz que o Fe²⁺ da pirita é "de spin baixo". A própria auditoria registrou esse contraste em "Observações não factuais". Sem uma frase que explique, o aluno fica com dois fatos que parecem se contradizer.
**Correção aplicada:** entrada "spin alto / spin baixo" no vocabulário da `a03`. Spin alto é um elétron por orbital, como em Hund, com 4 desemparelhados no Fe²⁺. Spin baixo é quando os vizinhos no cristal forçam o pareamento, e o Fe²⁺ da pirita fica com 0. O porquê fica para o módulo 48. Para coordenação octaédrica, um aposto: "o íon cercado por seis átomos vizinhos; módulo 08".
**Escopo:** correção local (o vocabulário fica fora da contagem LC-02). A definição deriva de alegações auditadas e da nota da auditoria. Foi registrada como `QUI-SPIN-DEF-001`, **pendente** de conferência pelo auditor.

### 🟠 6. A conversão mais difícil do `oa06` nunca era demonstrada

**Tipo:** objetivo com a parte difícil só afirmada, não ensinada · salto no exemplo
**Onde:** `a06` · "Unidades" e "Problema 3"
**Problema:** o `oa06` pede converter entre Å, nm, µm, GPa, kbar, °C e K. As conversões fáceis (kbar → GPa, °C → K) estavam trabalhadas. A única que exige manipular potências de dez com expoentes negativos, µm → Å, aparecia duas vezes como resultado pronto ("30 µm = 3 × 10⁵ Å") e nunca como passo. É exatamente onde erra quem tem a potência de dez enferrujada, perfil que a própria aula prevê em "Antes de começar".
**Correção aplicada:** o Problema 3 passou a mostrar a cadeia: 30 µm = 30 × 10⁻⁶ m = 3 × 10⁻⁵ m, e (3 × 10⁻⁵) ÷ 10⁻¹⁰ = 3 × 10⁵ Å. Depois vem a divisão por 1,62, que já estava no texto.
**Escopo:** correção local. Nenhum número novo: os valores são os mesmos, só com o caminho explícito.

---

### 🟡 7. O exemplo da aula 02 pedia uma ordenação e respondia só o primeiro colocado

**Tipo:** exemplo trabalhado incompleto · premissa contraditória
**Onde:** `a02` · "Exemplo trabalhado", enunciado e passos 3–4
**Problema:** o enunciado dizia "sem consultar os números, ordene…", mas o passo 4 usava os números. O passo 3 respondia só "Na, o mais fácil" e deixava de fora justamente a parte instrutiva: entre Mg e Al, a anomalia do Al que o corpo acabara de ensinar inverte a previsão.
**Correção aplicada:** enunciado "primeiro pela posição na tabela, e só depois conferindo com os números". O passo 3 dá a ordem pela tendência e mostra a inversão real (Al 578 < Mg 738). O passo 4 confere com a tabela (0,93; 1,31; 1,61).

### 🟡 8. A aula 02 usava termos das aulas seguintes sem ponte

**Tipo:** termo usado antes de definido
**Onde:** `a02` · parágrafo das eletronegatividades de Allred ("valência variável", "estado de oxidação"); ionizações sucessivas ("silicatos", "carbonatos"); vocabulário ("kJ/mol")
**Problema:** "valência variável" e "estado de oxidação" entraram com a correção `QUI-EN-PAULING-001` e só são definidos na `a03`. "Silicatos" e "carbonatos" não eram definidos em nenhum lugar do módulo antes do uso. "kJ/mol" pressupõe o mol, que o aluno viu no ensino médio mas que o curso só retoma na `a06`.
**Correção aplicada:** apostos curtos: "que formam íons de cargas diferentes, tema da aula 03", "a carga atribuída ao íon", "minerais de silício e oxigênio", "com o grupo CO₃". No vocabulário, "kJ/mol, isto é, a energia para ionizar um mol de átomos (o mol é revisto na aula 06)". Também foi corrigida a concordância "se lê" → "se leem".

### 🟡 9. O parágrafo 4s/3d, o mais denso do módulo, não dizia o que levar dele

**Tipo:** densidade irregular
**Onde:** `a01` · "A ordem de preenchimento"
**Problema:** a correção `QUI-ORB-ENERGIA-001` está certa e precisa ficar. O parágrafo, porém, passou a trazer num só bloco energia de orbital × energia total, repulsão eletrônica e a diferença entre K/Ca e metais de transição. Para o aluno, falta a consequência operacional, que é o que ele de fato vai usar na `a03`.
**Correção aplicada:** uma frase ao fim, que não altera o fato auditado: "Na prática do curso: escreva a configuração pela ordem de Madelung e, no íon, retire primeiro o 4s."

### 🟡 10. "Giro" do spin sem dizer onde a analogia quebra (LC-04)

**Tipo:** analogia sem ressalva
**Onde:** `a01` · princípio de Pauli
**Problema:** "giro" entre aspas sugere uma rotação literal, modelo que o curso não quer fixar. O contrato pede que a analogia diga onde ela quebra.
**Correção aplicada:** "o nome é histórico, não uma rotação literal".

### 🟡 11. Aula 05: quatro termos sem definição e uma remissão duplicada

**Tipo:** termo usado antes de definido · redundância
**Onde:** `a05` · tabela de energias ("energia de rede"); talco ("tetraedros… octaedros"); diamante ("{111}"); enxofre/gelo ("IMA"); "(módulo 13). O módulo 13 retoma"
**Correção aplicada:** apostos curtos. Energia de rede: "a energia para desmontar o cristal iônico em íons separados". Tetraedros e octaedros: "um cátion no centro e O ou OH nos vértices; módulo 11". {111}: "notação de índices de Miller do módulo 05". IMA: "a Associação Mineralógica Internacional, que aprova as espécies minerais; módulo 02". A remissão duplicada ao módulo 13 foi retirada.

### 🟡 12. Pré-requisito da aula 06 apontava um mineral que a aula 03 não trata

**Tipo:** pré-requisito declarado incorreto
**Onde:** `a06` · "Antes de começar"
**Problema:** o texto dizia "minerais como forsterita, Mg₂SiO₄ (aula 03)", mas a `a03` trabalha a **fayalita**, Fe₂SiO₄. Quem volta à aula 03 para revisar não encontra o que o cabeçalho promete.
**Correção aplicada:** "Ler fórmulas de óxidos e de minerais e os estados de oxidação de seus elementos, como na fayalita, Fe₂SiO₄ (aula 03)."

### 🟡 13. Seção de unidades da aula 06 com vocabulário de módulos futuros sem definição

**Tipo:** termo usado antes de definido
**Onde:** `a06` · "Unidades" ("coordenação 4", "cela unitária", "petrologia", "pressão litostática")
**Correção aplicada:** apostos: "isto é, com quatro vizinhos", "o bloco mínimo que, repetido, constrói o cristal; módulo 06", "o estudo das rochas", "a exercida pelo peso das rochas acima".

### 🟡 14. Aula 03: rótulo que não corresponde, redundância e nomes de técnicas sem sinalização

**Tipo:** título ou rótulo que não corresponde · redundância · carga periférica
**Onde:** `a03` · "Um exemplo de ordem de grandeza: hematita…"; "óxidos negros e pretos"; "Nomes e grafia"
**Problema:** o que vinha depois do rótulo não é ordem de grandeza nenhuma, e sim exemplos de minerais. "Negros e pretos" já estava apontado pela auditoria como redundância. O parágrafo dos métodos (microssonda, FRX, via úmida, Mössbauer, XANES) despeja cinco nomes técnicos sem avisar que não precisam ser guardados agora.
**Correção aplicada:** "Exemplos:"; "óxidos pretos de manganês"; e uma frase final: "Não é preciso guardar esses nomes agora; a ideia a levar é que a análise de rotina mede o ferro total."

---

### 🔵 15. Sugestão: reativar o "diagrama de Linus Pauling" do ensino médio

**Onde:** `a01` · "A ordem de preenchimento"
**Observação:** o aluno brasileiro que sai do ensino médio costuma conhecer essa sequência como o diagrama das diagonais atribuído a Pauling. Dizer que a "regra de Madelung" é esse mesmo diagrama transformaria um conceito que parece novo em reativação, e reduziria a carga percebida da aula mais longa do módulo. **Não aplicado:** é uma afirmação nova sobre nomenclatura escolar e atribuição histórica, que não passou pelo auditor. Além disso, a `a01` está em 1585 palavras, perto do teto. Fica registrado para o auditor e o orquestrador.

### 🔵 16. Sugestão: apoio visual em `a04` e `a05`

**Onde:** `a04` (triângulo de Van Arkel–Ketelaar), `a05` (empilhamento de lâminas no grafite, talco, mica e gipsita)
**Observação:** o triângulo é descrito só em palavras ("os três tipos nos vértices e as ligações reais no meio"), e as quatro estruturas em lâmina da `a05` são o tipo de conteúdo que uma figura resolve de uma vez. **Não aplicado:** o `_contexto.md` não lista o módulo 01 entre os pontos de ilustração essencial, e acrescentar um pedido de ilustração ao contrato é decisão do orquestrador.

### 🔵 17. Sugestão: o parêntese do ponto de fusão do MgO interrompe o argumento

**Onde:** `a04` · "Ligação iônica", último item
**Observação:** o argumento "dobrar a carga pesa mais que o resto" é interrompido por um parêntese de 30 palavras sobre a divergência entre medidas (correção ⚪ `QUI-LIG-MGONACL-001`). Levar esse parêntese para uma nota depois da lista deixaria o argumento mais limpo. **Não aplicado de propósito:** é o texto da correção da auditoria, que expõe a divergência onde o número aparece, e mexer na posição de uma alegação controversa corrigida cabe ao auditor.

---

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo | Fechado por | Avaliado em |
|---|---|---|---|---|
| `mineralogia-m01-oa01`: estrutura do átomo e configuração → posição na tabela | `a01`, Conteúdo (tamanhos, orbitais, subcamadas, ordem, notação, tabela como mapa; regra do bloco d agora no corpo, achado 1) | sim (Fe, 5 passos; Mn para comparar) | Erros comuns, O que não concluir, Recap | questionário ainda não gerado |
| `mineralogia-m01-oa02`: prever raio, EI e χ | `a02`, Conteúdo (Zef, três tendências, ionizações sucessivas, χ) | sim (Na, Mg, Al, agora completo, achado 7) | idem | idem |
| `mineralogia-m01-oa03`: carga de íons e estado de oxidação, incl. Fe, Mn, S | `a03`, Conteúdo (cargas de bolso, regra da soma, Fe, Mn, S, convenção) | sim (fayalita, pirita, gipsita) | idem | idem |
| `mineralogia-m01-oa04`: classificar a ligação (5 tipos) e relacionar a propriedades | `a04` (três fortes; método agora operacional, achado 2; propriedades definidas, achado 4) + `a05` (duas fracas, anisotropia) | sim (MgO, Si–O, Cu, Fe–S; gipsita, brucita) | idem | idem |
| `mineralogia-m01-oa05`: massa molar, razão molar, % em massa de elementos e óxidos | `a06`, Conteúdo (mol, massa molar, óxidos, do peso ao mol) | sim (forsterita; hematita; pirita no corpo) | idem | idem |
| `mineralogia-m01-oa06`: converter unidades e estimar ordens de grandeza | `a06`, "Unidades" (comprimento, pressão, temperatura, estimativa) | sim (Problema 3, agora com a cadeia µm → Å, achado 6; átomos em 1 cm³ de quartzo) | idem | idem |

**Cobertura completa: 6/6.** Nenhum objetivo órfão e nenhuma seção órfã. Todos os verbos são verificáveis (descrever/relacionar, prever, determinar, classificar, calcular, converter); nenhum usa "entender", "conhecer" ou "saber". O único objetivo dividido entre duas aulas (`oa04`) declara a divisão nas duas, no bloco "Ao final você vai conseguir".

### Orientação para o `gerador-de-questionarios` (alinhamento com a avaliação futura)

O questionário e o baralho ainda não existem, então o alinhamento não pode ser verificado. Para que a avaliação cobre o que as aulas ensinam, e só isso:

- **Deve cobrir** o grupo de um elemento do bloco d pela soma s + d (`oa01`); a ordenação Na/Mg/Al pela 1ª EI **com** a anomalia do Al (`oa02`); o salto das ionizações sucessivas → carga (`oa02`); a magnetita como valência mista e a pirita como Fe²⁺ + S₂²⁻ (`oa03`); a classificação de Cu–Cu pelo critério dos metais nativos, **não** pelo valor de χ (`oa04`); por que talco, mica e gipsita clivam onde clivam (`oa04`); o % de óxidos e a volta à razão molar (`oa05`); a conversão µm → Å e kbar → GPa → profundidade (`oa06`).
- **Pode pedir cálculo** com a fórmula de Pauling, porque a conta agora está mostrada (achado 3), desde que forneça o valor de Δχ ou a tabela de χ.
- **Não deve cobrar** teoria do campo cristalino, o porquê do spin baixo (fica para o módulo 48), nomes das técnicas analíticas de Fe²⁺/Fe³⁺ (a aula diz para não guardá-los), valores de χ de Allen, nem o valor exato do ponto de fusão do MgO (a aula o dá como faixa).
- **Armadilhas que o questionário deve evitar reintroduzir** (corrigidas na auditoria): "4s tem energia menor que 3d em todo átomo neutro"; "5 desemparelhados é o máximo de um átomo"; "metais têm χ baixo"; "silicatos são duros"; "o diamante não tem clivagem"; actinídeos como terras raras; ligação iônica como transferência total.

---

## Progressão do módulo

A cadeia é **átomo → tendência → carga → ligação forte → ligação fraca → contagem e unidades**, e cada aula entrega à seguinte exatamente o que ela usa. Conferido item a item:

- `a01` prepara o 4s-antes-do-3d e o 3d⁵/3d⁶, e a `a03` os usa para Fe²⁺/Fe³⁺ e Mn.
- `a02` prepara o salto das EI → carga e a χ, e a `a03` (cargas) e a `a04` (Δχ) os usam.
- `a03` prepara as cargas e a regra da soma, e a `a04` (Coulomb, q₁·q₂) e a `a06` (óxidos, FeO/Fe₂O₃) as usam.
- `a04` termina com "ligação forte ≠ isotropia", e a `a05` abre a partir disso.
- `a05` fecha a ligação, e a `a06` fecha o módulo com a contabilidade da composição.

Nenhuma aula usa o resultado de uma posterior. As remissões para a frente (módulos 05, 06, 08, 09, 10, 11, 13, 20, 22, 48) são todas do tipo "detalhado mais adiante", sem exigir o conteúdo. Com as correções dos achados 4, 5, 8, 11 e 13, nenhum termo técnico fica sem definição na primeira aparição.

---

## O que está bem feito

- **As ionizações sucessivas da `a02`** são o melhor momento didático do módulo: uma tabela de três linhas faz o aluno *ver* de onde vêm Na⁺, Mg²⁺ e Al³⁺, e a frase "a tabela periódica e a energia de ionização dizem a mesma coisa" amarra tudo. O contraste com o ferro, sem salto, prepara a `a03` sem antecipá-la.
- **A honestidade epistêmica da `a03`**, no caso (b) do exemplo ("a aritmética só diz que o par de S soma −2 se o ferro for +2; que o ferro seja mesmo Fe²⁺ vem de dados estruturais e espectroscópicos, não da conta"), ensina a separar a conta da evidência. É raro em material introdutório e prepara a regra do plugin de separar fato de interpretação.
- **As analogias com ressalva** (abelha em longa exposição, plateia atrás de pessoas altas, fita adesiva fraca) seguem o LC-04 à risca: cada uma diz onde quebra.
- **A comparação talco × mica na `a05`** ("a mesma arquitetura, com a 'cola' entre as lâminas trocada") é o tipo de contraste mínimo que fixa um conceito, e a tabela de anisotropia logo depois consolida sem repetir.
- **Os blocos "O que não concluir"** fazem trabalho real: previnem as generalizações erradas mais prováveis (raio atômico = raio iônico; brilho metálico = ligação metálica; % de óxidos revela os minerais).
- **As correções da auditoria foram integradas sem virar remendo:** o 4s/3d, o ouro, a clivagem do diamante e a razão entre ligações ficaram no fluxo do texto, e não em notas soltas.

---

## Correções aplicadas

**Aplicadas em:** 2026-09-30

| # | Sev. | Desfecho | Arquivo |
|---|---|---|---|
| 1 | 🟠 | Corrigido | `...aula-01-o-atomo-por-dentro...md` |
| 2 | 🟠 | Corrigido | `...aula-04-ligacao-ionica-covalente...md` |
| 3 | 🟠 | Corrigido | `...aula-04-ligacao-ionica-covalente...md` |
| 4 | 🟠 | Corrigido | `...aula-04-ligacao-ionica-covalente...md`, `...aula-01-o-atomo-por-dentro...md` |
| 5 | 🟠 | Corrigido | `...aula-03-ions-e-estados-de-oxidacao...md` |
| 6 | 🟠 | Corrigido | `...aula-06-mol-massa-molar...md` |
| 7 | 🟡 | Corrigido | `...aula-02-tabela-periodica...md` |
| 8 | 🟡 | Corrigido | `...aula-02-tabela-periodica...md` |
| 9 | 🟡 | Corrigido | `...aula-01-o-atomo-por-dentro...md` |
| 10 | 🟡 | Corrigido | `...aula-01-o-atomo-por-dentro...md` |
| 11 | 🟡 | Corrigido | `...aula-05-ligacoes-fracas...md` |
| 12 | 🟡 | Corrigido | `...aula-06-mol-massa-molar...md` |
| 13 | 🟡 | Corrigido | `...aula-06-mol-massa-molar...md` |
| 14 | 🟡 | Corrigido | `...aula-03-ions-e-estados-de-oxidacao...md` |
| 15 | 🔵 | Não aplicado; encaminhado ao auditor e ao orquestrador (fato novo; teto LC-02) | — |
| 16 | 🔵 | Não aplicado; encaminhado ao orquestrador (contrato de ilustração) | — |
| 17 | 🔵 | Não aplicado de propósito (texto de correção ⚪ da auditoria) | — |

**Nenhum questionário ou baralho foi alterado.** Eles não existem para este módulo e não foram gerados.

**Nenhum valor numérico auditado foi alterado.** Um script conferiu, depois das edições, que cada valor auditado das seis aulas (EIs, χ, raios, massas atômicas, massas molares, porcentagens, fatores Fe/FeO e Fe/Fe₂O₃, energias de ligação, pontos de fusão, durezas, pressões) continua presente e idêntico no texto. Os textos das alegações auditadas nos rodapés não foram tocados.

**Conteúdo introduzido por esta revisão e rastreado:** quatro alegações novas foram registradas nos rodapés `alegacoes_auditaveis`, para que nada entre sem passar pelo auditor.

| claim_id | Aula | Natureza | Status |
|---|---|---|---|
| `QUI-TAB-GRUPOD-001` | a01 | generalização de `QUI-CONF-FE-001` (grupo = s + d no bloco d) | **pendente** de conferência pelo auditor |
| `QUI-SPIN-DEF-001` | a03 | definição de spin alto/baixo, derivada de `QUI-CONF-FE-001`, `QUI-S-ESTADO-001` e da nota da auditoria | **pendente** de conferência pelo auditor |
| `QUI-LIG-METALREGRA-001` | a04 | heurística metais nativos → metálica, reformulando `QUI-LIG-METAL-001` | **pendente** de conferência pelo auditor |
| `QUI-LIG-PAULCALC-001` | a04 | aritmética de `QUI-LIG-PAULING-001` | verificada (recálculo) |

Os demais acréscimos são apostos de definição terminológica (clivagem, dureza/Mohs, refratário, coordenação, cela unitária, pressão litostática, petrologia, energia de rede, tetraedro/octaedro, notação {111}, IMA, silicatos, carbonatos, kJ/mol), sem afirmação quantitativa nova.

**Densidade LC-02 depois desta revisão** (régua: palavras separadas por espaço, de `## Conteúdo` até o fim do `## Recap relâmpago`; a mesma régua reproduz exatamente os valores gravados pela auditoria):

| Aula | Após auditoria | Após revisão didática | Teto |
|---|---|---|---|
| a01 | 1520 | 1585 | ~1600 ✅ |
| a02 | 1416 | 1482 | ~1600 ✅ |
| a03 | 1368 | 1391 | ~1600 ✅ |
| a04 | 1362 | 1465 | ~1600 ✅ |
| a05 | 1404 | 1455 | ~1600 ✅ |
| a06 | 1285 | 1337 | ~1600 ✅ |

**Observação estrutural fora do escopo desta skill:** dois claim_ids pré-existentes da `a05`, `QUI-ENXOFRE-001` e `QUI-BRUCITA-001`, têm 3 segmentos. Isso viola o formato de 4 segmentos que o `_contexto.md` fixa desde a primeira aula. Não foram renomeados aqui, porque IDs são referenciados pela auditoria e a renomeação cabe ao auditor ou ao validador.

**Pendências:** os três 🔵 (achados 15–17) e a conferência das três alegações pendentes pelo auditor. Nenhum achado didático 🔴 ou 🟠 fica em aberto.
