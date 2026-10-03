# Revisão didática: Módulo 36 — Microscopia de minérios

**Revisado em:** 2026-09-29  ·  **Modo:** review-and-fix
**Material:** `36-microscopia-de-minerios/` (4 aulas e hub), depois da auditoria científica do mesmo dia (`36-microscopia-de-minerios-auditoria.md`: 17 achados, todos tratados)
**Veredito:** **Bem ensinado com ressalvas**

## Resumo
🔴 0 bloqueiam · 🟠 0 prejudicam · 🟡 3 atrito · 🔵 3 sugestões

**Carga estimada:**

| Aula | Conceitos novos centrais | Exemplos | Palavras do corpo | Duração (~84 palavras/min) |
|---|---|---|---|---|
| a01 | 4 (luz refletida × transmitida; caminho óptico; ajuste de iluminação e meio; seção polida e seus artefatos) | 1 trabalhado | 1580 | ~19 min (antes 17) |
| a02 | 4 (refletância; cor relativa; hábito e clivagem; dureza de polimento com linha de Kalb, mais Talmage como contraste) | 1 trabalhado | 1619 | ~19 min (antes 17) |
| a03 | 4 (birreflectância/pleocroísmo; anisotropia; reflexões internas; figuras de polarização) | 1 trabalhado | 1158 | ~14 min (antes 13) |
| a04 | 4 blocos (assembleia/paragênese/sequência; quatro famílias de textura; limites da microscopia; rotina de relatório) | 1 trabalhado | 1585 | ~19 min (antes 16) |

Total do módulo: ~71 min (antes ~63). O aumento vem quase todo da auditoria (Talmage, tabela de refletância, refletores, doença da calcopirita, oxi-exsolução) e, em menor parte, dos apostos desta revisão.

## Achados

### 🟡 1. Termos usados sem definição na primeira ocorrência

**Tipo:** termo técnico antes de definido
**Onde:** a01 ("princípio de Köhler", "parfocal", "livre de tensão"); a02 ("microfotômetro", trazido pela auditoria); a04 ("pseudomorfos"; "ulvoespinélio", "titanomagnetita" e "epitaxial", trazidos pela auditoria); a03 (figuras de polarização pressupõem conoscopia de luz transmitida, sem declaração)
**Problema:** são termos de passagem, não centrais, mas o leitor autodidata tropeça neles sem ter onde conferir. Os que vieram da auditoria entraram corretos e sem glosa.
**Correção aplicada:** apostos curtos na primeira ocorrência: Köhler ("o ajuste que dá iluminação uniforme a todo o campo"), parfocal ("mantém o foco aproximado ao trocar de objetiva"), livre de tensão ("sem tensões no vidro das lentes, que alterariam a polarização"), microfotômetro ("fotômetro acoplado ao microscópio"), pseudomorfos ("o mineral novo conserva a forma do antigo"), ulvoespinélio ("Fe₂TiO₄, componente titanífero da solução sólida da magnetita, chamada então titanomagnetita"), epitaxial ("com a calcopirita orientada pelo cristal de esfalerita que cresce"). Na a03, frase no pré-requisito: "Da luz transmitida, assume-se a observação conoscópica (lente de Bertrand, isogiras)".
**Escopo:** correção local

### 🟡 2. "Borda" no objetivo e no título da seção, sem vínculo no texto

**Tipo:** objetivo com termo não ensinado explicitamente
**Onde:** a02 · "Relevo, borda e dureza de polimento"; objetivo `geologia-avancado-m36-oa02` ("hábito, clivagem, borda, dureza...")
**Problema:** o objetivo e o título listam "borda" como propriedade, mas o texto nunca diz o que se observa na borda. O aluno pode procurar uma propriedade à parte, ou confundir com "borda de reação", que a mesma seção manda não confundir com relevo.
**Correção aplicada:** "Como observar o relevo? Olhando a **borda** do grão, isto é, o contato com o vizinho: é ali que a diferença de altura aparece." Sem conteúdo factual novo.
**Escopo:** correção local

### 🟡 3. Durações desatualizadas depois da auditoria

**Tipo:** metadado desalinhado
**Onde:** cabeçalhos e metadados das quatro aulas; hub
**Problema:** a auditoria e os apostos aumentaram o corpo de todas as aulas; cabeçalhos e hub ainda diziam 17, 17, 13 e 16 min.
**Correção aplicada:** recontagem por script (tokens entre "## Conteúdo" e "## Fontes", ~84 palavras/min, convenção dos Módulos 30–35): 19, 19, 14 e 19 min; `palavras_corpo` e `duracao_estimada_min` atualizados; hub atualizado (~71 min).
**Escopo:** correção local

### 🔵 4. Visuais que ajudariam (não aplicado)

**Tipo:** sugestão
**Onde:** a01 (esquema do caminho óptico com os três tipos de refletor); a02 (corte do bisel mostrando a linha de Kalb em dois planos de foco, como a Fig. 3.3 de Craig & Vaughan); a04 (painel exsolução × substituição × oxi-exsolução).
**Por que não aplicado:** não há imagem verificada com licença de uso; o texto se sustenta sem elas. Registrado para a publicação.

### 🔵 5. Bloco "Exsolução ou substituição?" ficou o mais denso da a04 (não aplicado)

**Tipo:** sugestão / densidade irregular
**Onde:** a04, dois parágrafos depois da tabela (doença da calcopirita e oxi-exsolução)
**Problema:** a auditoria tornou esses parágrafos corretos e mais longos. Estão legíveis e cada um fecha com uma frase-síntese ("O mecanismo em cada depósito segue debatido"; "a textura sozinha não prova o processo"), que é o que o aluno precisa levar.
**Decisão:** não encurtar (o conteúdo é o mínimo para não reinstalar a leitura errada); **não cobrar os detalhes** desses parágrafos na avaliação além das frases-síntese (restrições 14, 13 e 24).

### 🔵 6. Nenhuma aula dividida ou fundida

**Tipo:** decisão de escopo
**Onde:** módulo
**Justificativa:** todas entre ~14 e ~19 min, com quatro blocos centrais e um exemplo trabalhado cada, bem abaixo do limite de 30 min. A a02 e a a04 são as mais densas, mas cada uma tem uma costura única (a02: o que se lê com o polarizador só; a04: da textura à interpretação e ao relatório). A a03 (~14 min) não deve ser fundida à a02 (passaria de 30 min) e separa, de propósito, as propriedades dependentes da orientação.

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo | Avaliado em |
|---|---|---|---|
| `geologia-avancado-m36-oa01` (operar o microscópio, componentes, precauções, qualidade da seção) | a01 inteira | sim (a01: seção com riscos, arrancamento e halo) | questionário ainda não gerado |
| `geologia-avancado-m36-oa02` (identificar opacos: hábito, clivagem, borda, dureza por linha de Kalb e Talmage, cor, reflexões internas, birreflectância, anisotropia) | a02 (luz plana) e a03 (orientação) | sim (a02: pirita/calcopirita/galena; a03: magnetita/ilmenita, com hematita excluída) | questionário ainda não gerado |
| `geologia-avancado-m36-oa03` (texturas, microestruturas e paragênese) | a04, primeiros três blocos | sim (a04: pirita → calcopirita → covelita) | questionário ainda não gerado |
| `geologia-avancado-m36-oa04` (aplicabilidades e restrições na gênese de depósitos) | a04, "O que a microscopia de opacos faz e o que não faz" e rotina de relatório | sim (a04, passo 5 de limites) | questionário ainda não gerado |

Nenhum objetivo sem cobertura. Nenhum conteúdo órfão.

## Decisão sobre a avaliação

**Questionário único cumulativo, sem parciais.** O módulo tem 4 aulas e ~71 min, bem abaixo do limiar de ~5–6 aulas do plugin, e as aulas formam um só arco (instrumento → propriedades em luz plana → propriedades com orientação → interpretação): as a02 e a03 cobrem juntas o objetivo 02 e não devem ser avaliadas separadas.

Forma sugerida: ~14–16 questões; oa01 ~3, oa02 ~6 (a02 e a03 juntas), oa03 ~3, oa04 ~3; tipos misturados (múltipla escolha, V/F, dissertativa curta, aplicação), com três questões de integração:

1. **Identificação em cadeia (a02 + a03):** um par difícil lido em ordem — refletância relativa e cor, depois dureza pela linha de Kalb, depois anisotropia e reflexões internas — separando pirita/calcopirita/pirrotita ou magnetita/ilmenita/esfalerita/hematita, com a conclusão "compatível, não confirmado".
2. **Artefato ou textura (a01 + a04):** halo de relevo, arrancamento triangular na galena e riscos contra borda de reação e substituição; o aluno decide o que é da seção e o que é geológico.
3. **Da textura ao relatório (a04 + a02/a03):** reconstruir uma sequência paragenética curta a partir de contatos (fratura preenchida, relictos, película supergênica) e redigir o item "interpretação e limitações" com grau de confiança.

**Restrições obrigatórias** para o gerador (além das 17 do fim de `36-microscopia-de-minerios-auditoria.md`):

18. **"Borda"** no sentido da a02 = contato onde se lê o relevo; não confundir com "borda de reação", e nunca cobrar relevo como evidência de reação.
19. **Paragênese:** aceitar as duas acepções (associação formada no mesmo evento, uso europeu e do curso; sequência de formação, uso de Craig & Vaughan). Não fazer questão cuja resposta dependa de uma delas ser "a errada".
20. **Figuras de polarização** só qualitativas (cruz estacionária em isotrópico; isogiras que se abrem ao girar num anisotrópico; uso para anisotropia fraca). Não cobrar a explicação das rotações de reflexão.
21. **Fórmula de refletância:** cobrar só as leituras qualitativas (k maior → R maior; em óleo R cai). Não pedir cálculo.
22. **Refletores e diafragmas:** não cobrar percentuais de luz de cada refletor; cobrar a diferença qualitativa (vidro plano: incidência vertical e abertura total; prisma: mais brilho, metade da abertura).
23. Não cobrar Fe₂TiO₄, a lista de padrões da COM, as referências bibliográficas nem visuais inexistentes.
24. Doença da calcopirita e oxi-exsolução: cobrar só as frases-síntese (exsolução explica poucos casos; debate substituição × crescimento conjunto; ilmenita em magnetita sobretudo oxi-exsolução; textura sozinha não prova o processo).

## O que está bem feito

Registrado para que as próximas revisões **não** estraguem:

1. **Comparação relativa como fio condutor**: todas as aulas repetem que se compara grão vizinho nas mesmas condições, e o recap do módulo fecha nisso.
2. **Exemplos trabalhados com passo de limite**: todos terminam em "compatível, não confirmado" e dizem o que confirmaria.
3. **Artefato antes de interpretação**: a a01 ensina a desconfiar da seção antes de qualquer propriedade, e a a04 retoma o ponto nas restrições.
4. **Aviso explícito do ponto de maior inversão** ("isotrópico = escuro estável; anisotrópico = brilha e apaga") em bloco próprio na a03.
5. **Divisão a02/a03 pelo modo de observação** (só polarizador × nicóis cruzados), que evita misturar birreflectância com anisotropia.
6. **Controvérsias abertas sem vencedor** (doença da calcopirita, oxi-exsolução) terminando em frase que diz o que o aluno pode afirmar.

## Correções aplicadas

| Achado | Arquivos |
|---|---|
| 🟡 1 termos | aula-01, aula-02, aula-03, aula-04 |
| 🟡 2 borda | aula-02 |
| 🟡 3 durações | aula-01, aula-02, aula-03, aula-04 (cabeçalho e metadados), hub |

**Conteúdo factual novo introduzido por esta revisão:** apenas glosas de manual em apostos (Köhler, parfocal, lentes livres de tensão, microfotômetro, pseudomorfo, fórmula e papel do ulvoespinélio, epitaxia). Nenhuma alegação auditável criada; claims em disco continuam 33, sem duplicata.
