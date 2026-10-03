# Revisão didática: Módulo 37 — Petrografia de minério

**Revisado em:** 2026-09-30  ·  **Modo:** review-and-fix
**Material:** `37-petrografia-de-minerio/` (7 aulas e hub), depois da auditoria científica do mesmo dia (`37-petrografia-de-minerio-auditoria.md`: 22 achados, todos tratados)
**Veredito:** **Bem ensinado com ressalvas**

## Resumo
🔴 0 bloqueiam · 🟠 2 prejudicam · 🟡 2 atrito · 🔵 3 sugestões

**Carga estimada:**

| Aula | Conceitos novos centrais | Exemplos | Palavras do corpo | Duração (~84 palavras/min) |
|---|---|---|---|---|
| a01 | 4 (fugacidades e assembleia como restrição; tampão py-po e estado de sulfetação; tampão MH; instrumentos de assembleia e reequilíbrio) | 1 trabalhado | 1489 | ~18 min (antes 16) |
| a02 | 4 (texturas primárias por ambiente; mecanismo e geometrias da substituição; regras de idade e inversão; perfil supergênico) | 1 trabalhado | 1393 | ~17 min (antes 15) |
| a03 | 4 (resistência à deformação; recristalização e junções; idiomorfismo cristaloblástico; sombras, remobilização e foliação) | 1 trabalhado | 1266 | ~15 min (antes 14) |
| a04 | 3 sistemas (Fe-Ti-O; Cr-Fe-O e bordas de alteração; Sn-W-O) | 1 trabalhado | 1139 | ~14 min (antes 12) |
| a05 | 3 blocos (escada de Cu; galena; esfalerita) + tendência de zonamento | 1 trabalhado | 1179 | ~14 min (antes 13) |
| a06 | 3 blocos (Ni; As; minerais preciosos) | 1 trabalhado | 1162 | ~14 min (antes 12) |
| a07 | 4 (coleção e paragênese composta; gerações; força da evidência; condições por estágio) | 1 trabalhado | 1286 | ~15 min (sem mudança) |

Total do módulo: ~107 min (antes ~97). O aumento vem quase todo da auditoria (tabela de sulfetação, fases refratárias, exceções dos veios, perfil supergênico, nota de classificação, Carajás, ouro invisível) e, em menor parte, dos dois exemplos reescritos aqui. Todas as aulas ficam entre ~14 e ~18 min, dentro da faixa de 12–16 min pedida com folga pequena na a01 e na a02, e bem abaixo do limite de 30 min.

## Achados

### 🟠 1. Exemplo da Aula 05 ordena duas fases que os contatos não ordenam

**Tipo:** salto no exemplo trabalhado
**Onde:** a05 · Exemplo trabalhado, passo 5
**Problema:** o passo 3 diz, corretamente, que a galena preenche espaços entre esfalerita e calcopirita e é mais nova que elas. O passo 5 falava em "a ordem esfalerita, calcopirita, galena que os contatos sugerem", pondo a esfalerita antes da calcopirita sem nenhum contato que o sustente, e concluía que essa ordem "não segue a tendência". O aluno aprende o contrário do que o módulo repete (contato sem relicto nem corte não ordena) e tira uma conclusão errada sobre a tendência Cu, Zn, Pb (galena por último coincide com ela).
**Correção aplicada:** "Os contatos só dizem que a galena veio depois da esfalerita e da calcopirita; não ordenam as duas entre si. A galena por último coincide com a tendência, mas isso não a confirma: a galena pode ser remobilizada, e a tendência não é regra. Se os contatos a contrariassem, também não seria problema." Metadado `PET-M37-A05-EXEMPLO-012` ajustado.
**Escopo:** correção local

### 🟠 2. Exemplo da Aula 06 lê a magnetita euédrica só pela chave metamórfica

**Tipo:** salto no exemplo trabalhado / leitura incompleta
**Onde:** a06 · Exemplo trabalhado, passo 4
**Problema:** a seção é de sulfeto maciço magmático com pentlandita em chamas, e nada diz que foi metamorfisada. O passo 4 justificava não atribuir idade à magnetita euédrica só com o idiomorfismo cristaloblástico (Aula 03), deixando de fora a leitura magmática que a Aula 02 ensina e que é a mais provável nesse contexto (Craig & Vaughan, §7.2 e §9.3.2: nos minérios de Fe-Ni-Cu a magnetita cristaliza euédrica enquanto o sulfeto ainda está fundido). O aluno sai achando que euédrico nunca significa nada.
**Correção aplicada:** duas leituras explícitas (magmático não metamorfisado: compatível com cristalização precoce; metamorfisado: pode ser idiomorfismo cristaloblástico), com a conclusão de registrar as duas e não atribuir idade sem outra evidência. O conteúdo factual vem de seções de Craig & Vaughan já conferidas na auditoria; metadado `PET-M37-A06-EXEMPLO-012` ajustado.
**Escopo:** correção local

### 🟡 3. Durações desatualizadas depois da auditoria

**Tipo:** metadado desalinhado
**Onde:** cabeçalhos e metadados das sete aulas; hub
**Problema:** a auditoria e os dois exemplos reescritos aumentaram o corpo de seis aulas; cabeçalhos e hub diziam 16, 15, 14, 12, 13, 12 e 15 min.
**Correção aplicada:** recontagem por script (tokens entre "## Conteúdo" e "## Fontes", ~84 palavras/min, convenção dos Módulos 30–36): 18, 17, 15, 14, 14, 14 e 15 min; `palavras_corpo` e `duracao_estimada_min` atualizados; hub atualizado (~107 min).
**Escopo:** correção local

### 🟡 4. Técnicas analíticas do ouro invisível sem ponte

**Tipo:** termo técnico sem ponte
**Onde:** a06 · "Ouro visível e ouro invisível"
**Problema:** SIMS e LA-ICP-MS aparecem só pela sigla. Foram ensinadas no Módulo 27 (Aula 03), mas o aluno não tem como saber onde revê-las.
**Correção aplicada:** link para o [[27-petrocronologia/27-petrocronologia-aula-03-tecnicas-analiticas-imageamento|Módulo 27, Aula 03]] depois das siglas. O microscópio eletrônico de transmissão já aparece por extenso.
**Escopo:** correção local

### 🔵 5. A Aula 01 ficou a mais densa do módulo (não aplicado)

**Tipo:** sugestão / densidade irregular
**Onde:** a01, bloco "O tampão pirita-pirrotita e o estado de sulfetação" (tabela de cinco níveis resumida e parágrafo sobre HS/IS/LS) e parágrafo das fases refratárias
**Problema:** a auditoria tornou esses trechos corretos e mais longos (~18 min). Estão legíveis e fecham com frases que dizem o que o aluno pode afirmar ("não é uma classificação de depósitos"; "a assembleia registra o último equilíbrio").
**Decisão:** não dividir (quatro blocos centrais, um exemplo, abaixo de 30 min); **não cobrar** os níveis extremos da escala nem a lista de fases refratárias além do que está nas restrições da auditoria (1, 3 e 4).

### 🔵 6. Visuais que ajudariam (não aplicado)

**Tipo:** sugestão
**Onde:** a01 (diagrama log fS₂ × T com a curva py-po e as faixas de sulfetação); a02 (perfil supergênico vertical com o nível freático e as duas frentes; veio sintaxial × antitaxial); a05 (escada de Cu com os teores); a07 (diagrama paragenético em barras).
**Por que não aplicado:** não há imagem verificada com licença de uso; as tabelas das aulas cobrem o essencial. Registrado para a publicação.

### 🔵 7. Nenhuma aula dividida ou fundida

**Tipo:** decisão de escopo
**Onde:** módulo; em especial a06 + a07
**Justificativa:** a06 (~14 min) e a07 (~15 min) somariam ~29 min, no limite de 30, mas cobrem objetivos diferentes (oa03 e oa04) e a a07 depende de todas as fases das a04–a06; a divisão de 2026-09-30 foi feita por sobrecarga de conceitos novos, e nada nesta revisão a desfaz. As demais aulas têm três ou quatro blocos centrais e um exemplo cada. YAML e hub mantêm as 7 aulas.

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo | Avaliado em |
|---|---|---|---|
| `geologia-avancado-m37-oa01` (condições T, fO₂, fS₂ × assembleias) | a01 inteira; retomado na a07 ("Ler as condições, estágio por estágio") | sim (a01: py-po-sl-mt com hematita tardia; a07: passo 5) | questionário ainda não gerado |
| `geologia-avancado-m37-oa02` (texturas primárias, de substituição, metamórficas e de deformação; ordem temporal) | a02 (primárias, substituição, supergênico) e a03 (metamórficas e de deformação) | sim (a02: furo supergênico; a03: minério metamorfisado) | questionário ainda não gerado |
| `geologia-avancado-m37-oa03` (identificar óxidos, sulfetos de Cu-Pb-Zn-Ni-As e preciosos) | a04, a05, a06 | sim (a04: cromita e titanomagnetita; a05: veio Cu-Pb-Zn; a06: sulfeto magmático com pentlandita e violarita) | questionário ainda não gerado |
| `geologia-avancado-m37-oa04` (reconstruir a paragênese e inferir condições do depósito) | a07 inteira | sim (a07: três seções, três estágios) | questionário ainda não gerado |

Nenhum objetivo sem cobertura. Nenhum conteúdo órfão. O oa03 fala em "grupos dos óxidos (… Sn-W-O)"; a a04 agora avisa que scheelita e wolframita não são óxidos em todas as classificações (texto curricular mantido).

## Decisão sobre a avaliação

**Um questionário único cumulativo, sem parciais.** O módulo tem 7 aulas, acima do limiar de ~5–6 aulas do plugin, mas o total é ~107 min e as aulas não formam blocos independentes: a a07 é a síntese que só se avalia com o módulo inteiro, e a divisão da antiga a06 em duas foi de carga, não de tema. Parciais separariam justamente o que o módulo pede para integrar (texturas das a02–a03 aplicadas às fases das a04–a06 e lidas por estágio na a07). Um único questionário, maior e com blocos internos, avalia melhor.

Forma sugerida: ~18–22 questões, com blocos por objetivo (oa01 ~4, oa02 ~6 com a02 e a03 juntas, oa03 ~6 com a04, a05 e a06, oa04 ~3) e tipos misturados (múltipla escolha, V/F, dissertativa curta, aplicação), mais três questões de integração:

1. **Assembleia e condições (a01 + a03 + a07):** uma seção metamorfisada com pirita, pirrotita, esfalerita, magnetita e película de hematita; o aluno decide o que coexistiu, lê fS₂ e fO₂ qualitativas no último equilíbrio, diz que a esfalerita informaria a pressão e descarta a hematita tardia.
2. **Ordem por contatos com armadilhas de inversão (a02 + a03 + a06):** inclusão que é relicto, pentlandita em chamas na pirrotita, arsenopirita euédrica em matriz recristalizada e calcopirita em fraturas de pirita; o aluno ordena só o que os contatos sustentam.
3. **Da coleção ao diagrama (a07 + a02 + a05):** três seções de um furo com uma zona supergênica; o aluno monta os estágios, põe covelita e calcocita no supergênico pela posição e diz o que a paragênese não classifica.

**Restrições obrigatórias** para o gerador (além das 22 do fim de `37-petrografia-de-minerio-auditoria.md` e das herdadas do Módulo 36 que o módulo reutiliza):

23. **Exemplos trabalhados:** contato reto, preenchimento simples entre duas fases ou vizinhança não ordenam as duas fases vizinhas entre si; não fazer questão que exija ordenar esfalerita e calcopirita do exemplo da a05.
24. **Euédrico:** em minério magmático não metamorfisado, euédrico incluso é compatível com cristalização precoce; em minério metamorfisado, pode ser porfiroblasto. Cobrar a necessidade de decidir o contexto, não uma regra única.
25. **Tendência Cu, Zn, Pb** só como hipótese: coincidir com ela não a confirma, contrariá-la não é problema.
26. Não cobrar os níveis "muito baixo" e "muito alto" da escala de sulfetação como memorização, nem a lista completa de fases refratárias; cobrar as leituras (baixo × intermediário × alto; pirita, arsenopirita e esfalerita guardam composição melhor que pirrotita e sulfetos de Cu-Fe).
27. Não cobrar os códigos Nickel-Strunz nem a classificação de Dana; cobrar só que a scheelita não é óxido.
28. Não cobrar siglas de técnicas analíticas além do que a a06 afirma (ouro invisível: nem óptico nem MEV).
29. Não cobrar visuais inexistentes nem as referências bibliográficas.

## O que está bem feito

Registrado para que as próximas revisões **não** estraguem:

1. **Inversões anunciadas em bloco próprio:** inclusão × substituição (a02), euédrico magmático × metamórfico (a03), pentlandita em chamas (a06) e as duas direções da frente supergênica (a02) são ditas como armadilha, com o sentido certo e a razão.
2. **Todos os exemplos trabalhados terminam em "compatível, não confirmado"** e dizem o que confirmaria (microssonda, difração, contexto de campo).
3. **"Reconhecer antes de interpretar"** fecha a a01 ligando cada leitura de tampão à identificação correta das fases do Módulo 36.
4. **Resistência à deformação como quarta propriedade** (a03), explicitamente distinta das três durezas do Módulo 36.
5. **Leitura por estágio** (a07) retoma a a01 e impede o erro mais caro do módulo: misturar fases de estágios diferentes num mesmo tampão.
6. **Controvérsias abertas sem vencedor** (doença da calcopirita, origem das exsoluções) remetidas ao Módulo 36 e listadas como pendência no recap do módulo.

## Correções aplicadas

| Achado | Arquivos |
|---|---|
| 🟠 1 exemplo da a05 | aula-05 (corpo e metadado do exemplo) |
| 🟠 2 exemplo da a06 | aula-06 (corpo e metadado do exemplo) |
| 🟡 3 durações | as sete aulas (cabeçalho e metadados), hub |
| 🟡 4 ponte para o Módulo 27 | aula-06 |

**Conteúdo factual novo introduzido por esta revisão:** apenas a leitura magmática da magnetita euédrica no exemplo da a06, apoiada em Craig & Vaughan (§7.2 e §9.3.2), seções já conferidas na auditoria. Nenhuma alegação auditável criada; claims em disco continuam 74 (72 da redação + 2 criados pela auditoria), sem duplicata.
