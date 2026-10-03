# Revisão didática: Módulo 01 — Gemologia geral e identificação

**Revisado em:** 2026-08-24 · **Modo:** review (relata; não altera as aulas)
**Material:** as 16 aulas novas (07–22), revisadas em conjunto e contra as 6 aulas preservadas (01–06)
**Veredito:** As aulas novas estão bem ensinadas. O módulo, como conjunto, tem um degrau de densidade não intencional entre o bloco 1 antigo e tudo o que veio depois.

## Resumo

**Achados:** 🔴 0 bloqueiam · 🟠 2 prejudicam · 🟡 3 atrito · 🔵 1 sugestão

**Carga estimada:** 22 aulas. Corpo de "Conteúdo" a "Recap": 270–341 palavras nas aulas 01–06; 876–1.258 palavras nas aulas 07–22. Todas abaixo do teto de 1.600 palavras (LC-02). 141 termos únicos nos blocos de vocabulário (6–7 por aula, dentro da faixa de LC-03). 22 exemplos trabalhados, um por aula.

**Por que esta revisão foi refeita:** a anterior, de 2026-08-17, cobria as 11 aulas do módulo antes da expansão. Cinco daquelas aulas não existem mais neste módulo. Este relatório substitui aquele.

## Achados

### 🟠 1. Degrau de densidade entre as aulas 01–06 e as aulas 07–22

**Tipo:** dificuldade desproporcional à posição no curso / carga cognitiva desigual
**Onde:** módulo inteiro, na transição da aula 06 para a 07

**Problema:** as aulas novas foram escritas com três a quatro vezes o conteúdo das preservadas, e a diferença não é estilística — é de substância ensinada.

| | Aulas 01–06 | Aulas 07–22 |
|---|---:|---:|
| Palavras de "Conteúdo" a "Recap" | 270–341 | 876–1.258 |
| Tamanho do arquivo | 4,0–4,7 KB | 9,0–13,0 KB |
| Alegações auditáveis por aula | 1–2 | 4–7 |
| Itens em "Erros comuns" | 2 | 4 |
| Fontes citadas | 2–3 | 5–7 |

Todas as seis primeiras declaram "~25 min" no cabeçalho, mas nenhuma sustenta mais que cinco a oito minutos de leitura atenta. O efeito prático é o oposto do pretendido: o aluno atravessa os fundamentos em meia hora, chega à aula 07 achando que domina o bloco, e encontra ali a primeira aula que de fato exige as três horas nominais do bloco.

O problema não é o tamanho em si — é **o que ficou de fora**. A aula 03, por exemplo, é o lugar onde densidade relativa, índice de refração e birrefringência deveriam ser instaladas como conceitos, e ela dedica uma frase a cada uma. Quatro aulas depois, a aula 07 assume densidade relativa como conceito consolidado e passa direto para a medição e para os limites do método. A aula 03 não sustenta esse peso.

**Correção sugerida:** reescrever as aulas 01–06 no mesmo contrato das novas — corpo de 900 a 1.200 palavras, exemplo trabalhado desenvolvido, quatro itens em "Erros comuns", "O que não concluir" com mais de um item, e bloco de alegações auditáveis estruturado. Não é urgente para a avaliação (os questionários já cobrem os nove objetivos do bloco 1 e as questões novas Q34–Q39 puxam justamente as aulas 07–09), mas é o item de qualidade mais relevante que resta neste módulo.

**Escopo:** exige reescrita de seis aulas. Fora do escopo desta passagem; registrado como pendência.

### 🟠 2. Duas convenções estruturais convivem dentro do mesmo módulo

**Tipo:** inconsistência de contrato de aula
**Onde:** aulas 01–06 contra aulas 07–22

**Problema:** as aulas novas seguem um padrão que as antigas não seguem, e o aluno sente a troca:

- **Bloco de objetivo.** As aulas 07–22 têm a seção `## Ao final você vai conseguir`, com o ID completo do objetivo. As aulas 01–06 não têm essa seção — o objetivo aparece só como uma linha do cabeçalho. O aluno perde o marcador explícito do que deve conseguir fazer, e o script de validação perde o vínculo aula–objetivo.
- **Ordem de abertura.** Nas aulas 01–06, "Antes de começar" vem antes de "Vocabulário desta aula"; nas 07–22, a ordem é a inversa. LC-03 exige os dois blocos, mas a alternância de ordem no meio do módulo é atrito gratuito.
- **Identificadores.** As aulas 01–06 usam a forma curta `OA-03` no bloco de cobertura; as 07–22 usam o ID completo `gemologia-m01-oa15`. Isso faz o validador estrutural enxergar dois conjuntos de objetivos onde há um só, e obrigou os questionários a carregarem as duas grafias para não acusarem falso descobrimento.
- **Formato do rodapé de metadados.** Comentário HTML de uma linha nas antigas; bloco estruturado com `nivel`, `palavras_corpo`, `cobertura` e `alegacoes_auditaveis` nas novas.

**Correção sugerida:** padronizar pelas aulas novas. As três primeiras correções são locais e baratas — acrescentar a seção de objetivo, inverter a ordem dos dois blocos de abertura e trocar `OA-0N` pelo ID completo — e podem ser feitas sem tocar no corpo das aulas, independentemente da reescrita do achado 1.

**Escopo:** correção local em seis arquivos. Não aplicada nesta passagem, para não deixar o módulo com metade das aulas reescritas e metade só remendada.

### 🟡 1. Cinco fenômenos ópticos concentrados em duas aulas

**Tipo:** excesso de conceitos novos por aula
**Onde:** aulas 13 e 14

**Problema:** a aula 14 introduz adularescência, labradorescência, jogo de cores, aventurescência e mudança de cor — cinco mecanismos físicos distintos (espalhamento, interferência, difração, reflexão e transmissão seletiva) em 1.192 palavras. Cada um exigiria, isoladamente, sua própria âncora. O hub do módulo já reconhece que os cinco "são fáceis de confundir".

**Atenuantes que fizeram este achado ficar em amarelo e não em laranja:** a aula organiza os cinco pelo **mecanismo**, não pela aparência, que é exatamente o critério certo; o assunto já foi dividido em duas partes (13 e 14), evitando uma aula única de 2.500 palavras; e a tabela comparativa dá ao aluno um lugar único para conferir a separação.

**Correção sugerida:** se a aula 14 for revisitada, considerar mover aventurescência — o mecanismo mais simples e o menos confundível dos cinco — para a aula 13, junto de asterismo e chatoyance, com as quais compartilha a origem em inclusões. Isso deixaria a aula 14 com quatro mecanismos, sendo três deles ópticos de camada fina.

### 🟡 2. Aulas 16, 17, 20 e 21 se aproximam do teto de palavras

**Tipo:** carga por aula no limite
**Onde:** aulas 16 (1.258), 17 (1.207), 20 (1.185) e 21 (1.202)

**Problema:** as quatro estão dentro de LC-02, mas são também as aulas com mais entidades a memorizar — a 16 cobre cinco materiais com constantes próprias; a 20, sete províncias. O risco não é estourar o teto, é o aluno tratar a aula como lista.

**Atenuante:** o recap de cada uma resolve isso razoavelmente bem, condensando em seis linhas o que precisa sair da aula. Os flashcards absorvem a carga de memorização, que é o desenho correto.

**Correção sugerida:** nenhuma ação imediata. Se alguma dessas aulas crescer numa revisão futura, dividir em vez de comprimir.

### 🟡 3. Verbos operacionais continuam não verificáveis por material escrito

**Tipo:** objetivo parcialmente verificável em material textual
**Onde:** OA-04, OA-05, OA-12, OA-13 e OA-14 — aulas 04, 05, 07, 08 e 09

**Problema:** "operar", "medir", "executar" e "separar" exigem equipamento, condições padronizadas e desempenho observável. O achado é o mesmo da revisão anterior, herdado e agora ampliado, porque as aulas novas acrescentaram três objetivos com verbos operacionais.

**Como está sendo tratado:** os quatro questionários trazem, no cabeçalho, um callout que declara que os cenários escritos avaliam interpretação, seleção de procedimento e registro de evidências, e não certificam destreza de bancada. Os flashcards seguem a mesma regra. A ressalva está honrada no material.

**Correção sugerida:** manter a ressalva. A verificação de execução fica reservada a prática supervisionada ou a um roteiro de bancada (`gerador-de-praticas`), que ainda não existe para este módulo.

### 🔵 1. O módulo não tem um mapa único dos instrumentos

**Tipo:** oportunidade de consolidação
**Onde:** transversal às aulas 04, 05, 07, 08, 09 e 10

**Observação:** o aluno termina o módulo tendo visto nove instrumentos e cinco técnicas de laboratório, distribuídos por seis aulas, cada um com escopo e limite próprios. A aula 06 integra os cinco primeiros, mas nada integra o conjunto completo depois que as aulas 07–10 acrescentam densidade, UV, condutividade e a camada espectroscópica. A questão Q66 do final cumulativo pede exatamente essa síntese — e é razoável que o aluno a encontre pela primeira vez na prova.

**Sugestão:** uma tabela única no hub do módulo, com as colunas *instrumento · que pergunta responde · o que não responde*, resolveria isso sem escrever aula nova.

**Aplicada nesta passagem.** A seção "Mapa dos instrumentos" foi acrescentada ao hub, com as catorze entradas (nove instrumentos de bancada e cinco técnicas de laboratório) e a aula de origem de cada uma. É a única alteração de arquivo feita por esta revisão; nenhuma aula foi tocada.

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo trabalhado | Avaliado em |
|---|---|---|---|
| OA-01 — definir gema; espécie, variedade e nome comercial | a01 | etiqueta "jade verde" | parcial 1 (Q01, Q02); final (Q63) |
| OA-02 — origem da cor | a02 | dois coríndons de cores distintas | parcial 1 (Q03, Q04); final (Q65) |
| OA-03 — propriedades diagnósticas | a03 | pedra azul oferecida como safira | parcial 1 (Q05, Q06); final (Q64) |
| OA-04 — refratômetro e polariscópio | a04 | sequência combinada dos dois | parcial 1 (Q07, Q08); final (Q64) — execução requer prática |
| OA-05 — dicroscópio, espectroscópio, lupa e microscópio | a05 | sequência numa gema verde | parcial 1 (Q09); final (Q66) — execução requer prática |
| OA-06 — fluxo de identificação | a06 | pedra vermelha oferecida como rubi | parcial 1 (Q10); final (Q76) |
| OA-11 — proveniência, laudos e fatores de valor | a22 | laudo lido por seções | parcial 3 (Q62); final (Q74, Q76) |
| OA-12 — densidade relativa e líquidos pesados | a07 | incolor de 1,80 ct que resulta em CZ | parcial 1 (Q34, Q35); final (Q64, Q72) |
| OA-13 — fluorescência UV | a08 | anel com central inerte e seis laterais uniformes | parcial 1 (Q36, Q37); final (Q67) |
| OA-14 — condutividade e simulantes | a09 | duplo acionamento térmico e elétrico | parcial 1 (Q38, Q39); final (Q64) |
| OA-15 — laboratório espectroscópico | a10 | que técnica para que pergunta | parcial 2 (Q40, Q41); final (Q66, Q77) |
| OA-16 — anatomia e estilos de talhe | a11 | descrição completa de uma peça | parcial 2 (Q42, Q43); final (Q68) |
| OA-17 — proporções e desempenho óptico | a12 | diagnóstico por efeito visual | parcial 2 (Q44, Q45); final (Q68) |
| OA-18 — asterismo e chatoyance | a13 | estrela de seis raios e a seda | parcial 2 (Q46, Q47); final (Q69) |
| OA-19 — demais fenômenos ópticos | a14 | cinco mecanismos comparados | parcial 2 (Q48, Q49); final (Q65, Q69) |
| OA-20 — jade e o sistema A/B/C | a15 | bracelete com etiqueta "tipo A" | parcial 3 (Q50, Q51); final (Q63) |
| OA-21 — materiais opacos | a16 | constantes e tratamentos por material | parcial 3 (Q52, Q53); final (Q70) |
| OA-22 — durabilidade e cuidados | a17 | recomendação de uso e limpeza | parcial 3 (Q54, Q55); final (Q70, Q71) |
| OA-23 — metais preciosos e montagem | a18 | fundo fechado e estimativa de peso | parcial 3 (Q56, Q57); final (Q72) |
| OA-24 — geologia das gemas | a19 | por que esmeralda é improvável | parcial 3 (Q58); final (Q73) |
| OA-25 — províncias brasileiras | a20 | província por província | parcial 3 (Q59, Q60); final (Q73, Q74) |
| OA-26 — mercado, cadeia e ética | a21 | limites do Kimberley e do Rapaport | parcial 3 (Q61); final (Q75) |

Nenhum objetivo ficou sem questão. Nenhuma questão cobra conteúdo que não esteja em alguma aula.

## Verificação do contrato de nível

- **LC-01 — nenhum termo sem definição:** aprovado nas aulas 07–22. Todas abrem com "Vocabulário desta aula" e os termos novos do corpo recebem definição na primeira ocorrência. A aula 19 introduz "elementos incompatíveis", "metassomatismo" e "ultramáfica" com definição inline, e a aula 20 reativa "cráton", introduzido na aula 07 do módulo antes da reestruturação.
- **LC-02 — teto de 1.600 palavras:** aprovado. Máximo observado: 1.258 palavras (aula 16). Ver 🟡 2 para as quatro aulas mais próximas do teto.
- **LC-03 — abertura padronizada:** aprovado quanto à existência dos blocos (as 22 aulas têm os dois, com 6 a 7 termos de vocabulário cada). Ver 🟠 2 quanto à ordem dos blocos, que alterna entre as aulas antigas e as novas.
- **LC-04 — analogia antes do termo:** aprovado. Isopor e aço para densidade relativa (a07); camiseta branca sob luz negra para fluorescência (a08); as duas ancoram o cotidiano antes do nome técnico. A aula 12 é a mais exigente do módulo nesse quesito e resolve o ângulo crítico sem fórmula.
- **LC-05 — ordem de grandeza:** aprovado com uma observação. As aulas novas trazem números exatos com frequência — 365 nm, 254 nm, 415 nm, 737 nm, 437 nm, 2800–3000 cm⁻¹, 24,4°, 57 facetas. Nenhum deles é falsa precisão: são posições espectrais, contagens e constantes definidoras, que perdem a função se arredondadas. Onde havia margem real de variação, as aulas usaram faixas (opala 1,37–1,47; zircão 3,90–4,73), que é o comportamento correto.
- **LC-06 — matemática reativada antes do uso:** aprovado. A única fórmula do módulo, DR = P(ar) ÷ [P(ar) − P(água)], é aritmética simples, é apresentada depois da explicação física do empuxo e é imediatamente aplicada num exemplo numérico. O ângulo crítico é tratado qualitativamente, sem Snell.
- **LC-07 — "Erros comuns", "O que não concluir" e "Recap relâmpago":** aprovado. As 22 aulas têm as três seções. Nas aulas novas elas têm quatro, três e seis itens respectivamente; nas antigas, dois, um e quatro (ver 🟠 1).
- **LC-08 — controvérsia em uma frase:** aprovado. A trava da reforma do Processo de Kimberley (aula 21) é apresentada como impasse declarado, sem entrar no debate dos plenários; a opinião de origem geográfica (aula 22) é qualificada como opinião e não como medida, em uma frase, sem discutir a literatura de discordância entre laboratórios.

## Alinhamento entre as aulas

A progressão do módulo é cumulativa e está correta: nomenclatura → cor → propriedades → instrumentos ópticos → fluxo → propriedades físicas medidas → laboratório → lapidação → fenômenos → materiais fora do fluxo padrão → durabilidade → montagem → geologia → geografia → mercado → documentos. Nenhuma aula usa conceito que ainda não foi ensinado.

Três articulações merecem registro por funcionarem bem:

- A aula 09 fecha o bloco 1 no mesmo problema que a aula 07 abriu — a pedra incolor de identidade duvidosa — e o resolve com um instrumento diferente. A repetição do caso é deliberada e ensina convergência melhor que um enunciado sobre convergência.
- A aula 12 é o único ponto em que o módulo cobra o pré-requisito de óptica do módulo 05 com peso real, e o faz depois de a aula 11 ter instalado o vocabulário de partes da pedra. A ordem 11 → 12 é necessária e está correta.
- A aula 15 (jade) só faz sentido depois da aula 10 (FTIR), porque a detecção do tipo B depende dela. A ordem está respeitada.

Uma articulação frágil: a aula 22 fecha o módulo com o tema que a aula 06 abriu — o que uma conclusão gemológica pode e não pode afirmar. A simetria é boa, mas nenhuma das duas aponta para a outra, e o aluno não é convidado a reler a 06 à luz da 22. Um link recíproco resolveria.

## O que está bem feito

As aulas novas mantêm uma disciplina difícil: nenhuma delas confunde o que o instrumento mede com o que ele prova. A aula 08 é o melhor exemplo — trata a fluorescência como triagem por seis parágrafos e depois dedica um bloco inteiro a dizer o que ela não resolve, incluindo a armadilha de ler inércia como sinal. A aula 13 faz o mesmo com o asterismo, transformando um efeito bonito num diagnóstico de inclusões orientadas.

A separação entre categorias que o mercado embaralha é o fio condutor mais forte do módulo, e é sustentada até o fim: espécie contra nome comercial (a01, a15), simulante contra sintético (a09), forma contra estilo contra qualidade (a11), dureza contra tenacidade contra estabilidade (a17), e identificação contra origem contra proveniência contra valor (a22). Cinco distinções da mesma família, ensinadas em momentos diferentes, todas com o mesmo formato de contraste. Isso é desenho curricular, não acaso.

As aulas 19 e 20 fazem algo que o resto do curso de gemologia não faria sozinho: devolvem a gema ao seu contexto geológico e conectam o módulo aos módulos 07 a 26. A aula 19, em particular, dá à raridade uma explicação causal — química incomum, espaço, tempo estável e sobrevivência — em vez de tratá-la como fato de mercado.

## Gate didático

**Liberado.** Nenhum achado vermelho. Os dois achados laranjas dizem respeito às **aulas 01–06 preservadas**, não às aulas novas nem à avaliação, e por isso não bloqueiam os quatro questionários nem o baralho, que já estão gerados e cobrem os 22 objetivos.

**Pendência registrada:** reescrita das aulas 01–06 no contrato das aulas novas (🟠 1) e padronização estrutural das mesmas seis aulas (🟠 2). Enquanto isso não acontecer, o módulo entrega um bloco 1 mais fraco que os blocos 2 e 3, e o aluno que vier do módulo 05 encontra o degrau na aula 07.
