# Revisão didática — Módulo 09: Geometalurgia

**Módulo:** [[09-geometalurgia-modulo|Módulo 09 — Geometalurgia]]
**Escopo:** 6 aulas (geologia-avancado-m09-a01 a a06), ~10 700 palavras de corpo.
**Modo:** `review-and-fix`.
**Pergunta desta revisão:** não "isto é verdade?" (é a auditoria científica, já aprovada), mas **"alguém aprende com isto?"**
**Data:** 2026-08-30

## Veredito

**Bem ensinado.** O módulo é o mais bem construído da Área IX até aqui em três aspectos mensuráveis: as contagens de palavras declaradas são **honestas** (divergência máxima de 4 palavras contra a contagem independente, contra ~15 % de divergência no Módulo 08), a densidade conceitual é **uniforme** entre as seis aulas (32 a 38 termos técnicos destacados por aula), e **nenhum objetivo de aprendizagem é prometido sem seção que o ensine** — o defeito que rendeu o único 🟠 didático do Módulo 08.

Quatro achados, **um 🟠 e três 🟡**. O 🟠 foi corrigido com acréscimo de conteúdo; dois 🟡 foram corrigidos no texto; um 🟡 é ressalva justificada com encaminhamento.

| Severidade | Contagem |
|---|---|
| 🔴 Impeditivo | 0 |
| 🟠 Compromete o aprendizado | 1 (corrigido) |
| 🟡 Atrito ou risco menor | 3 (2 corrigidos, 1 ressalva justificada) |

## O que está bem feito

Registro antes dos defeitos, porque a maior parte das decisões didáticas do módulo está certa e não deve ser mexida numa revisão futura:

- **A ponte geologia → engenharia de processo é feita explicitamente**, e não presumida. A a01 nomeia o erro de quem vem da geologia ("tratar recuperação como sinônimo de teor") em vez de esperar que o aluno não o cometa.
- **A cadeia dos tetos de recuperação é cumulativa e está sinalizada.** Teto por partição (a02) → teto por liberação (a03) → medição real (a05). E a a03 fecha o laço em "O que não concluir" explicitando que **os dois tetos se multiplicam** e o menor manda. É o melhor parágrafo pedagógico do módulo.
- **Pré-requisitos externos apontados no ponto de uso**, não só no cabeçalho: a a06 interrompe a explicação de não aditividade para dizer de onde vem a krigagem e o que basta reter dela (linearidade). É exatamente o que evita o salto de pré-requisito.
- **Os seis recaps recapitulam de fato**, e carregam os números dos exemplos — não são listas de tópicos.
- **Um exemplo trabalhado por aula, sempre no fim, sempre numérico e sempre consequente.** Nenhum exemplo é decorativo.

## Achados

### 🟠 [DID-M09-A03-CURVAS-001] — A aula das curvas não tinha curva nenhuma

**Aula:** 03.

**Achado:** a aula se chama "**curvas de liberação**", e o seu objetivo declarado termina em "**ler a curva de liberação e a curva teor-recuperação** para escolher o alvo de moagem P80". A aula descrevia as duas curvas em prosa competente — monotonia, assíntota, relação inversa, andar sobre a curva × mudar de curva — e **não desenhava nenhuma das duas**. Não havia figura, esquema, gráfico ASCII, nada. O aluno saía sabendo enunciar propriedades de um objeto gráfico que nunca viu.

Isso é um objetivo declarado que nenhuma seção entrega por inteiro: **"ler" uma curva é uma habilidade visual**, e não se adquire lendo a descrição verbal de uma curva. Agrava-se por dois motivos:

1. A propriedade que mais importa da curva de liberação — que ela **achata** — é uma propriedade de *forma*. Ela é o motivo de existir o ótimo econômico da seção seguinte, e a prosa a enunciava ("assíntota abaixo de 100 %") sem que o aluno pudesse vê-la.
2. A distinção **andar sobre a curva × trocar de curva** é a ideia mais operacionalmente útil da aula, e é intrinsecamente geométrica: uma é deslocamento ao longo de uma linha, a outra é deslocamento da linha. Em prosa, as duas soam parecidas; em figura, são obviamente diferentes.

A tabela de quatro pontos do exemplo trabalhado era o mais perto de um gráfico que a aula chegava — e vem 30 linhas depois, já dentro de um cálculo de recuperação, tarde demais para servir de apoio visual ao conceito.

**Correção aplicada:** ✅ acrescentados **dois gráficos ASCII** na seção "Curvas de liberação e curva teor-recuperação":

- a **curva de liberação** plotada com os quatro pontos reais do exemplo desta mesma aula (52/71/86/94 % a P80 150/106/75/45 µm), com o eixo P80 correndo de grosso para fino e a assíntota tracejada — seguida de uma instrução explícita de leitura ("leia o formato, não os pontos") que nomeia o achatamento e o liga ao ótimo econômico da seção seguinte;
- a **curva teor-recuperação** com duas séries sobrepostas (o mesmo minério tal como moído e moído mais fino), que torna visível o deslocamento da curva inteira — seguida do parágrafo que separa as duas leituras e conclui que só trocar de curva é ganho real, e que ele custa energia.

Recap da aula reescrito para carregar as duas ideias novas (achatamento; as duas leituras). `claim` `GEOMET-M09-A03-CURVAS-004` atualizado para registrar a concavidade e a distinção.

**Custo:** a a03 passou de 1 758 para 1 899 palavras de corpo — encostando no teto de ~1 900, mas dentro dele, e o acréscimo fecha um objetivo que estava aberto. `palavras_corpo` atualizado no bloco de metadados.

---

### 🟡 [DID-M09-A05-AMPLITUDE-002] — A aula de maior amplitude temática do módulo

**Aula:** 05. **Desfecho: ressalva justificada, com ponto de quebra nomeado.**

**Achado:** a a05 cobre **cinco famílias de assunto sem parentesco físico entre si** — separação gravítica, separação magnética, flotação, lixiviação e o balanço metalúrgico algébrico — no mesmo orçamento de palavras em que a a03 cobre só liberação e a a04 só cominuição. A seção de flotação sozinha tem cinco sub-blocos (reagentes, física do contato trifásico, cinética, circuito, curva). O objetivo declarado da aula é, ele próprio, o sintoma: é uma lista de compras com quatro travessões e onze itens entre parênteses.

As métricas objetivas **não** flagram a aula: 1 771 palavras (dentro do teto) e 38 termos destacados (igual à a04). O que a diferencia não é o volume, é a **ausência de fio condutor**: na a04, britagem, moinho, circuito e as três leis são o mesmo assunto visto de ângulos diferentes, e cada seção prepara a seguinte. Na a05, terminar a separação magnética não ajuda em nada a entender flotação. O aluno faz cinco partidas do zero em trinta minutos.

**Por que não foi quebrada agora.** Seguindo o precedente do `DID-M08-EXTENSAO` (Módulo 08), aplico ressalva justificada em vez de corte. Quebrar a a05 em duas renumeraria a a06, invalidaria os `content_hash` das duas, e obrigaria a reescrever os links de navegação, o hub do módulo, as travessias de pré-requisito da a06 e o bloco `lessons` inteiro do `course-state.yaml` — um custo alto para um problema que é de conforto, não de correção, e que a estrutura interna da aula já mitiga (cada família tem o seu cabeçalho, e o aluno pode parar entre elas).

**Mitigação aplicada:** a única costura que faltava foi feita — ver o achado seguinte, que liga a curva teor-recuperação da a05 à da a03 em vez de recomeçá-la.

**Encaminhamento — candidata a quebra futura, se o usuário relatar fadiga:** a a05, no corte entre **"Separação magnética"** e **"Flotação"**. Parte 1 ficaria com o princípio comum e as duas separações por propriedade física de massa (gravítica, magnética) — as duas que respondem à liberação *por composição*, o que dá à Parte 1 um fio condutor real. Parte 2 ficaria com flotação (que responde à liberação *por superfície*), lixiviação e o balanço metalúrgico. O corte é limpo e a a03 já preparou a distinção composição × superfície que o justifica.

**Encaminhamento à avaliação:** não distribuir as questões uniformemente pelas cinco famílias da a05. A flotação e o balanço de dois produtos são o que o resto do curso consome; gravítica e magnética valem uma questão de reconhecimento cada.

---

### 🟡 [DID-M09-A05-REDUNDANCIA-003] — A curva teor-recuperação ensinada duas vezes do zero

**Aula:** 05 (em relação à 03).

**Achado:** a a03 define a curva teor-recuperação por inteiro: relação inversa, andar ao longo por tempo/dosagem/limpeza, mudar de curva por moagem ou minério. A a05 **redefine a mesma coisa do zero** ("o resultado de uma flotação não é um ponto, é uma curva. Quanto mais se insiste..."), sem uma palavra que sinalize retomada — e isso apesar de o próprio bloco "Antes de começar" da a05 já declarar, três seções acima, que o aluno chega sabendo disso pela Aula 03.

A aula, portanto, contradiz o seu próprio contrato de pré-requisito: promete partir de um conhecimento e então o reensina como se fosse novo. O efeito prático é duplo — gasta orçamento de palavras numa aula que já é a mais larga do módulo (achado anterior), e ensina implicitamente ao aluno que os blocos "Antes de começar" não são para levar a sério.

Registro que a a05 **tinha** algo novo a dizer: quem move o ponto de operação na prática da flotação, e que o critério de escolha é econômico e não técnico. Isso não estava na a03. O defeito era de moldura, não de conteúdo — o novo estava escondido dentro de uma repetição do velho.

**Correção aplicada:** ✅ o parágrafo foi reescrito como **retomada explícita** ("a Aula 03 já mostrou a curva e a diferença entre andar sobre ela e trocar de curva"), seguida da nomeação do que a a05 acrescenta: os controles de operação da flotação e o critério econômico de escolha do ponto. Acrescentada a consequência que fecha a ideia — duas plantas com o mesmo minério podem operar deliberadamente em pontos diferentes da mesma curva. A a05 passou de 1 771 para 1 809 palavras; `palavras_corpo` atualizado.

---

### 🟡 [DID-M09-A03-COLISAO-004] — "Superestima a liberação" em dois sentidos na mesma aula

**Aula:** 03. **Desfecho: sem alteração de texto; encaminhado à avaliação.**

**Achado:** depois da correção do achado 🔴 da auditoria científica, a expressão "**superestima a liberação**" passou a aparecer na a03 em dois sentidos genuinamente diferentes:

1. **Viés de medida** (ressalva do exemplo trabalhado): a seção 2D superestima a liberação real — é uma propriedade do instrumento, e vale sempre.
2. **Erro de modelagem** ("Erros comuns"): assumir descolamento num minério de fratura não preferencial superestima a liberação a uma dada moagem — é uma escolha errada do analista, e vale só quando ele a comete.

Os dois estão corretos e os contextos são distintos no lugar em que aparecem. O risco não é de leitura da aula, é de **extração**: um flashcard ou uma questão gerada a partir de qualquer um dos dois, fora do contexto, produz um card ambíguo ou francamente errado — e o primeiro dos dois é o item de maior consequência do módulo inteiro, o que a auditoria científica classificou como 🔴.

**Decisão:** não alterar o texto. Inserir um aviso de desambiguação no corpo custaria clareza para resolver um problema que não é do leitor. O tratamento correto é no gerador.

**Encaminhamento à avaliação e ao baralho:** ao cobrar o viés estereológico, **ancorar explicitamente na medida por seção polida** ("a medida de liberação em seção polida bidimensional..."), nunca na expressão nua. Ao cobrar a fratura não preferencial, ancorar na hipótese de descolamento. Os dois nunca devem aparecer no mesmo item. Registrado também na auditoria científica.

## Decisão sobre a avaliação: parciais ou questionário único

**Decisão: PARCIAIS — 2 parciais mais 1 final cumulativo.**

O padrão do projeto é questionário único para ~5–6 aulas, com a exceção fixada no Módulo 06 e aplicada no Módulo 08: **acionar parciais quando houver corte conceitual natural**. O Módulo 09 tem esse corte, e o tem de forma mais limpa que o Módulo 08.

**O corte: a01–a03 / a04–a06.**

| | Parcial 1 (a01–a03) | Parcial 2 (a04–a06) |
|---|---|---|
| Pergunta que responde | **O que este minério é?** | **O que se faz com ele, e como se modela?** |
| Conteúdo | vocabulário e programa; partição do metal; textura e liberação | cominuição e índices; rotas de concentração; domínios e variabilidade |
| Objetivos | `oa01` (a01, a02) e `oa02` (a03) — **ambos integrais** | `oa03` (a04, a05) e `oa04` (a06) — **ambos integrais** |
| Natureza dos exemplos | diagnóstico (partição, recuperação atingível) | dimensionamento e valor (energia, balanço, VPL) |

**Três razões, em ordem de peso:**

1. **Nenhum objetivo de aprendizagem atravessa o corte.** `oa01` e `oa02` caem inteiros na parcial 1; `oa03` e `oa04`, inteiros na parcial 2. Isso é estritamente mais limpo que o Módulo 08, onde `oa01` e `oa03` atravessavam a fronteira e as questões de integração tiveram de ser empurradas para o final. Aqui o final cumulativo fica livre para fazer o que deve: integrar de verdade, não remendar.
2. **O corte é a fronteira profissional real da disciplina** — caracterização (o que o depósito entrega) contra processamento e modelagem (o que se faz com isso). É a mesma divisão que separa o mineralogista de processo do engenheiro de processo, e a a01 já a antecipa ao distinguir variável primária de proxy.
3. **Ponto de verificação antes da a04**, que é a aula mais dura do módulo e depende diretamente do P80 da a03. Somando-se à a05, que é a mais larga (achado `DID-M09-A05-AMPLITUDE-002`), a segunda metade do módulo concentra as duas aulas mais pesadas em sequência. Um checkpoint antes delas vale mais aqui do que valeria num módulo de dificuldade plana.

**Razão que NÃO se aplica aqui, e que vale registrar** para que a decisão não seja lida como automática: no Módulo 08, um dos argumentos para parciais foi que quatro aulas estavam acima do teto de palavras, o que tornaria um questionário único uma prova de resistência. **No Módulo 09 isso não vale** — as seis aulas estão dentro do teto e as contagens declaradas são honestas. A decisão aqui se sustenta na estrutura de objetivos, não no volume.

**Atenção ao gerador de questionários:**

- A a06 é **explicitamente cumulativa** — reúne as cinco anteriores por desenho. Ela é a matéria natural do **final cumulativo**, e questões da a06 na parcial 2 devem se restringir ao que a a06 tem de próprio (definição de domínio, não aditividade, modelo de blocos), deixando as amarrações para o final.
- O **final cumulativo** deve trazer pelo menos: (i) uma questão que componha o **teto por partição (a02) com o teto por liberação (a03)**, cobrando que se multiplicam e que o menor manda — é a ideia mais importante da primeira metade; (ii) uma questão que converta **energia por tonelada em toneladas por ano** e vice-versa, cobrindo o achado 🟠 da auditoria e a reciprocidade que a a04 e a a06 agora tratam de forma consistente; (iii) uma questão de **não aditividade**, que é o conteúdo mais importante do módulo.
- Ver os dois encaminhamentos dos achados `DID-M09-A05-AMPLITUDE-002` (não distribuir questões uniformemente pelas cinco famílias da a05) e `DID-M09-A03-COLISAO-004` (ancorar o viés estereológico na medida por seção polida).
- Ver ainda as cinco advertências no fim da auditoria científica, que listam os números que mudaram nas correções.

## Encaminhamentos abertos

Nenhum bloqueia a geração da avaliação.

| # | Encaminhamento | Destino |
|---|---|---|
| 1 | Candidata a quebra futura: a05, entre "Separação magnética" e "Flotação" | revisão futura, se o usuário relatar fadiga |
| 2 | Não distribuir questões uniformemente pelas cinco famílias da a05 | gerador de questionários |
| 3 | Ancorar o viés estereológico na medida por seção polida; nunca no mesmo item que a fratura não preferencial | gerador de questionários e de flashcards |
| 4 | Final cumulativo deve trazer a composição dos dois tetos, a reciprocidade energia/capacidade e a não aditividade | gerador de questionários |

## Recomendação

**Aprovar o módulo para avaliação e memorização.** O achado 🟠 e os dois 🟡 corrigíveis foram aplicados ao texto, aos recaps e aos blocos de metadados. O 🟡 restante é ressalva justificada com ponto de quebra nomeado. Nenhum achado didático permanece em aberto.
