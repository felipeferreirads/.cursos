# Revisão didática: Módulo 12 — Defeitos cristalinos e maclas

**Revisado em:** 2026-10-06  ·  **Modo:** review-and-fix
**Material:** `curso-mineralogia/12-defeitos-e-maclas/` — as 6 aulas do planejamento (agora 7, depois da divisão da aula 02) e as figuras 1 a 3, depois da auditoria científica aprovada; relatório de auditoria lido antes, para não reintroduzir nenhum dos 12 erros corrigidos
**Contrato de nível:** `ensino-medio-sem-geologia-v1`
**Veredito:** Requer revisão → **🟠 e 🟡 corrigidos; 🔵 abertos, não bloqueantes**

## Resumo

🔴 0 bloqueiam · 🟠 3 prejudicam · 🟡 11 atrito · 🔵 3 sugestões

**Carga estimada por aula** (contagem de `gerador-de-aula`; palavras de corpo de "Conteúdo" até o fim do recap, mesmo critério do módulo 11, depois das correções):

| Arquivo | ID | Conceitos novos | Pré-requisitos reativados | Exemplos | Visuais | Duração |
|---|---|---|---|---|---|---|
| aula 01 | `a01` | 5 (equilíbrio exponencial; vacância e intersticial; Schottky e Frenkel com neutralidade; centro de cor; não estequiometria) + difusão e substituição reativadas | 3 | 1 (3 itens, com exponencial) | 1 figura | ~30 min (~1.650) |
| aula 02 | `a02` | 4 (cunha, hélice e mista; vetor de Burgers, perfeita × parcial; sistema de deslizamento e escalada; crescimento em espiral) | 2 | 1 (4 itens) | 1 figura | ~28 min (~1.270) |
| aula 03 | `a07` | 3 (contorno de grão; falha de empilhamento; contorno de antifase) | 4 | 1 (4 itens) | 1 tabela | ~22 min (~1.040) |
| aula 04 | `a03` | 3 (definição e elemento de macla; plano de composição × plano de macla; quatro tipos) | 3 | 1 (3 itens, com trigonometria) | 1 figura + 1 tabela | ~29 min (~1.470) |
| aula 05 | `a04` | 3 (crescimento; transformação e variantes; deformação) | 3 | 1 (4 itens) | 1 tabela | ~28 min (~1.430) |
| aula 06 | `a05` | 2 (cinco leis dos feldspatos; teste contra a simetria 2/m) | 3 | 1 (3 itens) | 1 tabela | ~27 min (~1.120) |
| aula 07 | `a06` | 2 (leis de seis minerais; dupla convenção de índices) | 3 | 1 (5 itens) | 1 tabela | ~29 min (~1.430) |

A aula 01 fica no limite (~1.650 palavras, cerca de 3% acima do teto de ~1.600); ver o achado 🟡 3.

## Achados

### 🟠 1. Aula 02 com dois objetivos e sete ideias novas

**Tipo:** sobrecarga cognitiva
**Onde:** antiga aula 02 (Discordâncias e defeitos planares), inteira
**Problema:** a aula cobria `oa02` e `oa03` com sete conceitos novos independentes (discordância e seus tipos, vetor de Burgers, sistemas de deslizamento e escalada, crescimento em espiral, contorno de grão, falha de empilhamento, contorno de antifase), uma figura, um exemplo de quatro itens com conta e três pré-requisitos de módulos distintos, em ~1.580 palavras de corpo. Pela contagem de carga, passava de 40 minutos. O hub já previa a divisão. A fronteira conceitual é nítida: defeitos em linha × defeitos em superfície.
**Correção aplicada:** dividida em duas aulas, sem deslocar IDs:
- **Aula 02, Parte 1 — discordâncias e o vetor de Burgers** (`mineralogia-m12-a02`, cobre `oa02`): o texto original das seções de discordância, deformação e crescimento em espiral, com as correções da auditoria (achado 6) intactas.
- **Aula 03, Parte 2 — contornos de grão, falhas de empilhamento e contornos de antifase** (`mineralogia-m12-a07`, ID novo, cobre `oa03`): o texto original dos defeitos planares (com o achado 7 da auditoria intacto), mais uma abertura de ponte ("o que muda ao atravessar o plano?"), uma tabela-resumo, um item novo no exemplo (mármore, contorno de alto ângulo) e erros comuns próprios.

Os arquivos das antigas aulas 03 a 06 foram renumerados para 04 a 07 (IDs mantidos); links, remissões internas ("aula 0X"), hub, `course-state.yaml`, caminhos do manifesto da auditoria e uma nota de renumeração no relatório de auditoria foram atualizados.
**Escopo:** exigia dividir a aula (autorizado pelo orquestrador nesta tarefa).

### 🟠 2. Fórmula do ângulo da aragonita sem passo e com a razão invertida em relação ao módulo 11

**Tipo:** salto no exemplo trabalhado
**Onde:** aula 04 (antiga 03) · Exemplo trabalhado (b)
**Problema:** a conta "2 · arctan(b/a)" aparecia sem justificativa. O aluno já fez a mesma conta no módulo 11, aula 04, mas escrita como 2 · arctan(a·senβ/b), que dá o ângulo suplementar. Sem ponte, as duas fórmulas parecem se contradizer.
**Correção aplicada:** frase de ponte antes da conta: é a mesma conta da clivagem dos piroxênios, sem o senβ porque a aragonita é ortorrômbica; os dois ângulos entre (110) e (1̄10) são 2 · arctan(a/b) e 2 · arctan(b/a), que somam 180°. Módulo 11, aula 04 acrescentado aos pré-requisitos. Os valores (116,2° e 63,8°) não mudaram.
**Escopo:** correção local.

### 🟠 3. Contorno de antifase sem imagem concreta e com símbolos de grupo espacial fora do núcleo

**Tipo:** abstração antes do concreto + salto de pré-requisito
**Onde:** aula 03 (Parte 2, antiga aula 02) · Contorno de antifase
**Problema:** a explicação era só verbal ("arranjo deslocado, uma fase trocada") e o exemplo da pigeonita usava C2/c → P2₁/c, notação do módulo 07, que é de aprofundamento e não faz parte da trilha núcleo. O leitor do núcleo não tinha como ler a frase "a fase fria perde uma das translações".
**Correção aplicada:** (1) analogia do piso xadrez assentado a partir de dois cantos, com a frase "onde a imagem quebra" (sítios de Al/Si ou posições de átomos, em 3D; contorno não necessariamente reto); (2) leitura só da primeira letra dos símbolos, apoiada no módulo 06, aula 02: C tem a translação até o centro de uma face, P não; é essa a translação perdida. Módulo 06, aula 02 acrescentado aos pré-requisitos. O texto corrigido pela auditoria (achado 7) foi mantido palavra por palavra.
**Escopo:** correção local. **Alegação nova registrada** (`CRI-PLAN-ANTIF-002`, "pendente") para a segunda passagem do auditor.

### 🟡 1. Aula 01: termos e notações sem definição

**Onde:** aula 01 · equilíbrio, difusão, cor, condutividade
**Correção aplicada:** glosas curtas para exp(x) (= e elevado a x), eV (elétron-volt, unidade de energia), "relógios isotópicos" (idades pelo decaimento radioativo), "coloidais" (minúsculas, de metal) e **não estequiometria** (composição fora da proporção de números inteiros da fórmula ideal).

### 🟡 2. Aula 01: o exemplo (b) repetia o exemplo do texto

**Tipo:** exemplo trivial (não exige aplicar o método)
**Onde:** aula 01 · Exemplo trabalhado (b)
**Problema:** Ca²⁺ na halita com uma vacância de Na⁺ já estava resolvido, com a mesma conta, na seção "Substitucional".
**Correção aplicada:** trocado por um caso declarado **hipotético** (M³⁺ em sítio de Na⁺, compensado só por vacâncias: 2 por M³⁺), conta pura de carga, com remissão a "O que não concluir" (o balanço diz o que é permitido, não o que acontece). O exemplo do Ca²⁺ continua no texto e no recap.

### 🟡 3. Aula 01: densidade no limite, redação com sentido trocado e aviso duplicado

**Onde:** aula 01 · inteira; "O que não concluir"
**Problema:** ~1.680 palavras antes das correções, acima do teto de ~1.600; "Que todos os defeitos pontuais **se previnem** por simples balanço de carga" (o sentido é *prever*, não *prevenir*); o aviso de que E = 1 eV é fictício aparecia duas vezes.
**Correção aplicada:** enxugada (frases de transição, aviso duplicado removido do "O que não concluir"), frase reescrita ("Que o balanço de carga, sozinho, preveja quais defeitos se formam"). Ficou com ~1.650 palavras, ~30 min. **Não foi dividida:** os três "o que eles fazem" (difusão, cor, condutividade) são de um parágrafo cada, nível "relacionar", e remetem aos módulos que os desenvolvem; uma Parte 2 só com eles teria ~10 min. Se o aluno relatar que passou de 30 min, a fronteira natural é "tipos e carga" × "o que eles fazem", decisão do orquestrador.

### 🟡 4. Aula 02: termos usados antes de definidos

**Onde:** aula 02 (Parte 1) · Deformação plástica; crescimento em espiral
**Problema:** "tensão de cisalhamento" só era definida na antiga aula 04; "extinção ondulante" é vocabulário do módulo 15 (posterior); "supersaturação" e "SiC" sem apoio.
**Correção aplicada:** "tensão de cisalhamento" no vocabulário; glosa da extinção ondulante ("entre polarizadores cruzados, o grão não escurece todo de uma vez ao girar a platina"); "supersaturação (excesso de material dissolvido, módulo 03)"; "SiC (carbeto de silício)".

### 🟡 5. Aula 02: exemplo (a) com passo implícito e sem caso de discordância mista

**Onde:** aula 02 (Parte 1) · Exemplo trabalhado
**Problema:** "a/2 · |[110]| = a/2 · √2" pulava por que [110] mede a√2 e por que metade dele é uma translação; e o método ("outro ângulo: mista") não tinha nenhum item de treino.
**Correção aplicada:** passo explícito (diagonal da face por Pitágoras; a/2⟨110⟩ vai do vértice ao centro da face, translação do retículo de faces centradas, módulo 06); item (d) novo: b = [100], linha [110] num cúbico, 45°, mista. Alegação registrada como "pendente" (`CRI-DISC-DIDAT-001`).

### 🟡 6. Aula 03: "MET" abreviado sem definição

**Onde:** antiga aula 02 · Exemplo (d)(ii) ("ao MET")
**Correção aplicada:** MET no vocabulário da Parte 2 e escrito por extenso na primeira ocorrência do texto.

### 🟡 7. Aula 04: termos sem glosa e remissão a módulo futuro

**Onde:** aula 04 (antiga 03) · Os quatro tipos; Erros comuns; O que não concluir
**Correção aplicada:** "trilling, quatrilling, sixling (nomes do inglês para maclas de três, quatro e seis indivíduos)"; "esqueletismo (crescimento mais rápido nas arestas e nos vértices que no centro das faces, módulo 25)"; exsolução remetida também ao módulo 09, aula 03, onde já foi definida (antes só ao 23, posterior).

### 🟡 8. Aula 05: pré-requisito não declarado e termo sem glosa

**Onde:** aula 05 (antiga 04) · Macla de deformação
**Problema:** o contraste "a discordância desloca um vetor inteiro" depende da aula 02, que não estava nos pré-requisitos; "böhmita exsolvida" sem apoio.
**Correção aplicada:** aula 02 nos pré-requisitos e no "Antes de começar"; "böhmita (um oxi-hidróxido de alumínio, AlO(OH)) exsolvida nesses planos, isto é, separada do coríndon em lamelas finas (exsolução, módulo 09, aula 03)". Alegação registrada como "pendente" (`MIN-MACLA-DIDAT-002`).

### 🟡 9. Aula 06: "anortoclásio" sem definição; título divergente no estado

**Onde:** aula 06 (antiga 05) · Combinações; `course-state.yaml`
**Correção aplicada:** "o anortoclásio (um feldspato alcalino triclínico, rico em Na, módulo 36)"; título da aula no estado alinhado ao do arquivo ("periclina" → sem subtítulo, como no hub; o texto usa "periclínio"). Alegação "pendente" (`MIN-FELD-DIDAT-001`).

### 🟡 10. Aula 07: notação diferente do resto do curso e termos sem apoio

**Onde:** aula 07 (antiga 06) · Espinélio; Quartzo; Gipsita; exemplo (a); recap
**Problema:** "m3m" onde os módulos 04 e 05 escrevem m3̄m; "propriedades ópticas rotatórias opostas" sem explicação; "as chamadas *maclas* do diamante" era tautológico; "selenita" sem glosa.
**Correção aplicada:** m3̄m em todas as ocorrências do corpo; "(giram o plano de vibração da luz polarizada em sentidos contrários; módulo 14)"; "no diamante, em que esses cristais maclados achatados recebem, no comércio, o nome de *macles*"; "selenita, a variedade transparente". Alegação "pendente" (`MIN-QTZ-DIDAT-001`).

### 🟡 11. Contagem de palavras subestimada nos rodapés e no estado

**Onde:** campo `palavras_corpo` das seis aulas e do `course-state.yaml`
**Problema:** os valores declarados (1.460, 1.386, 1.259, 1.257, 1.027, 1.187) ficavam 130 a 210 palavras abaixo da contagem pelo critério do módulo 11, o que escondia que a aula 02 estava no teto e a 01 acima dele.
**Correção aplicada:** recontado nas sete aulas, de "Conteúdo" até o fim do recap, depois das correções.

### 🔵 1. Figura da discordância em hélice

**Sugestão:** a figura 2 só mostra a cunha; a hélice (b ∥ linha, "escada em caracol") fica só no texto. Um esquema 3D simples da rampa helicoidal ajudaria a aula 02.
**Desfecho:** aberto, não bloqueante.

### 🔵 2. Raio do cátion intersticial na figura 1

**Sugestão:** a auditoria observou que o cátion intersticial do Frenkel foi desenhado menor que o regular (raio 6 × 11); como é o mesmo íon, convém igualar numa próxima regeração.
**Desfecho:** aberto, não bloqueante.

### 🔵 3. "Seção rômbica" do periclínio

**Sugestão:** a nota da aula 06 nomeia a "seção rômbica" sem explicá-la (o plano é corretamente dado como (h0l)). A explicação pede geometria da cela triclínica e cabe no módulo 36.
**Desfecho:** registrado para o módulo 36.

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo | Avaliado em |
|---|---|---|---|
| `mineralogia-m12-oa01` — defeitos pontuais e o que fazem | aula 01 (`a01`) | sim (Schottky da fluorita; M³⁺ hipotético; n/N a 500 e 1000 K) | (questionário a gerar) |
| `mineralogia-m12-oa02` — discordâncias e vetor de Burgers | aula 02 (`a02`) | sim (b da halita e do quartzo; cunha; mista) | (questionário a gerar) |
| `mineralogia-m12-oa03` — defeitos planares | aula 03 (`a07`) | sim (subgrão, mica, pigeonita, mármore) | (questionário a gerar) |
| `mineralogia-m12-oa04` — macla, elemento e tipos | aula 04 (`a03`) | sim (pirita, plagioclásio, gipsita, rutilo; aragonita; anel de 60°) | (questionário a gerar) |
| `mineralogia-m12-oa05` — origem e leis nomeadas | aulas 05, 06, 07 (`a04`, `a05`, `a06`) | sim (calcita, microclínio, Dauphiné, Carlsbad; teste 2/m; m3̄m, Brasil, estaurolita, anel de 45°, gipsita) | (questionário a gerar) |

Nenhum objetivo descoberto; nenhuma seção órfã. Com a divisão, cada um dos objetivos `oa01` a `oa04` tem uma aula própria. Para o questionário: `oa05` ocupa três aulas e deve pesar de acordo; o módulo passou a ter 7 aulas, acima do limite de ~5–6 do `gerador-de-questionarios`, que prevê 2–3 questionários parciais mais um final.

## O que está bem feito (manter)

- O "Método geral" fecha todos os exemplos trabalhados e é o mesmo raciocínio em escalas diferentes: balanço de carga (aula 01), ângulo entre b e a linha (aula 02), "o que muda ao atravessar" (aula 03), tipo geométrico → elemento → teste de simetria (aulas 04, 06 e 07).
- A restrição "o elemento de macla não pode ser elemento de simetria do cristal" é ensinada uma vez (aula 04) e usada como ferramenta de dedução duas vezes: albita e periclínio impossíveis em 2/m (aula 06) e (100) impossível em m3̄m (aula 07). O aluno deriva a regra "polissintética ⇒ triclínico" em vez de decorá-la.
- A aula 05 trata os indícios de origem como tendências, com uma seção "o que não concluir" em cada item do exemplo; o Dauphiné ambíguo vira lição de método.
- A dupla convenção de índices (calcita {01̄18}/{01̄12}, estaurolita {031}/{032}) é apresentada como a mesma coisa em duas celas, não como dois fatos para decorar.
- A conta de n/N (aula 01) deixa claro que E é fictício e que a lição é a forma exponencial; o número sustenta a intuição de que difusão "congela" no frio.

## Correções aplicadas

| # | Severidade | Desfecho | Arquivos |
|---|---|---|---|
| 🟠 1 | 🟠 | Corrigido (aula dividida) | aula-02 (Parte 1), aula-03 (Parte 2, nova); aulas 04–07 renomeadas; hub; `course-state.yaml`; manifesto e nota no relatório de auditoria |
| 🟠 2 | 🟠 | Corrigido | aula-04 |
| 🟠 3 | 🟠 | Corrigido | aula-03 |
| 🟡 1–3 | 🟡 | Corrigido (🟡 3: enxugada, não dividida) | aula-01 |
| 🟡 4–5 | 🟡 | Corrigido | aula-02 |
| 🟡 6 | 🟡 | Corrigido | aula-03 |
| 🟡 7 | 🟡 | Corrigido | aula-04 |
| 🟡 8 | 🟡 | Corrigido | aula-05 |
| 🟡 9 | 🟡 | Corrigido | aula-06, `course-state.yaml` |
| 🟡 10 | 🟡 | Corrigido | aula-07 |
| 🟡 11 | 🟡 | Corrigido | todas as aulas, `course-state.yaml` |
| 🔵 1–3 | 🔵 | 1 e 2 abertos; 3 registrado para o módulo 36 | — |

**Afirmações factuais acrescentadas ou tocadas pela revisão** (nenhuma das 12 correções da auditoria foi revertida ou reescrita; todas as novas estão nos rodapés com `audit: pendente` para a segunda passagem do `auditor-cientifico`):

| claim_id | Aula | O que foi acrescentado |
|---|---|---|
| `CRI-DEFPT-DIDAT-001` | 01 | glosas de exp, eV, não estequiometria, relógios isotópicos, coloidal; exemplo (b) hipotético (conta de carga) |
| `CRI-DISC-DIDAT-001` | 02 | a/2⟨110⟩ = translação do retículo de faces centradas; 45° entre [100] e [110]; glosa de extinção ondulante |
| `CRI-PLAN-ANTIF-002` | 03 | a translação perdida na pigeonita é a de centragem C; analogia do piso xadrez |
| `MIN-MACLA-DIDAT-001` | 04 | 2·arctan(a/b) + 2·arctan(b/a) = 180° e ponte com o módulo 11; glosas de trilling e esqueletismo |
| `MIN-MACLA-DIDAT-002` | 05 | böhmita = AlO(OH); exsolvida = separada em lamelas |
| `MIN-FELD-DIDAT-001` | 06 | anortoclásio = feldspato alcalino triclínico rico em Na |
| `MIN-QTZ-DIDAT-001` | 07 | rotação do plano da luz polarizada em sentidos opostos; *macles* do diamante; selenita = variedade transparente; m3̄m |

**Pendente antes do questionário:** segunda passagem do auditor sobre essas sete alegações (o gate formal só bloqueia achados 🔴/🟠 da auditoria, mas são afirmações que ainda não passaram por ele).
