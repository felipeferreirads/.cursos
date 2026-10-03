# Revisão didática: Módulo 15 — Introdução à petrofísica

**Revisado em:** 2026-09-08 · **Modo:** `review-and-fix`
**Material:** `15-petrofisica/` — 4 aulas (`geologia-avancado-m15-a01` a `a04`)
**Rodou depois da auditoria científica** (`15-petrofisica-auditoria.md`, veredito aprovado, `open_findings: []`), como manda a ordem.
**Veredito:** **Bem ensinado com ressalvas**

## Resumo

🔴 0 bloqueiam · 🟠 4 prejudicam · 🟡 2 atrito · 🔵 2 sugestões

**Carga por aula** (medida após auditoria e revisão; blocos de diagrama não entram na contagem):

| Aula | Palavras | Conceitos novos | Exemplos | Duração declarada |
|---|---|---|---|---|
| a01 | 2.503 | 4 (porosidade total/efetiva, primária/secundária, permeabilidade, garganta de poro) | 1 + 1 diagrama | ~30 min |
| a02 | 2.406 | 4 (três densidades, quatro módulos elásticos, Vp/Vs, impedância acústica) | 1 | ~30 min |
| a03 | 2.798 | 5 (três comportamentos magnéticos, minerais ferrimagnéticos, ⁴⁰K vs. séries U/Th, espectrometria, razão Th/U) | 1 | ~30 min |
| a04 | 2.367 | 4 (condução eletrolítica, condutividade de superfície, lei de Archie, integração) | 1 + 1 tabela | ~30 min |

**Total do módulo: 10.074 palavras. Dispersão entre a aula mais leve (a04) e a mais pesada (a03) = 18,2%** — a **menor dispersão registrada no curso até aqui**, abaixo dos 23% dos Módulos 12 e 13 e muito abaixo dos 62% do Módulo 14. Nenhuma aula precisou de ajuste de duração declarada: as quatro cabem em 30 minutos. Registro honesto: cerca de 1.000 palavras do total foram acrescentadas pela auditoria e por esta revisão, não pelo redator — as aulas saíram do redator com 2.145, 2.210, 2.075 e 2.085 palavras, uma dispersão de 6,5%, ainda mais uniforme.

---

## Achados

### 🟠 1. A a01 declarava um objetivo que nenhuma seção cumpre

**Tipo:** objetivo não coberto
**Onde:** a01 · cabeçalho, linha de Objetivo
**Estava escrito:** "distinguir seus tipos (total, efetiva, **absoluta, relativa**)"
**Problema:** permeabilidade **absoluta** e **relativa** aparecem exatamente uma vez em toda a aula — nessa linha de objetivo — e nunca são definidas nem mencionadas no corpo. O leitor autodidata que estuda pelo objetivo declarado (que é como se estuda material autodidata) termina a aula procurando dois conceitos que não existem ali, e não tem como saber se perdeu uma seção, se o termo apareceu com outro nome, ou se a promessa era vazia. É o defeito clássico de objetivo declarado que nenhuma seção ensina.
**Correção aplicada:** objetivo aparado para o que a aula de fato entrega — "distinguir porosidade total de porosidade efetiva". **Deliberadamente NÃO ensinei os dois conceitos ausentes**: seria introduzir conteúdo factual novo depois de a auditoria ter rodado, o que esta skill não faz.
**Escopo:** correção local aplicada. **ENCAMINHADO AO ORQUESTRADOR:** permeabilidade absoluta, efetiva e relativa é assunto legítimo e provavelmente desejável, mas **não está no oa01** do módulo ("Definir e medir porosidade e permeabilidade e explicar seus controles geológicos"), então a lacuna não é do objetivo — era só do cabeçalho. Se o curso quiser cobrir permeabilidade relativa (que é pré-requisito real para engenharia de reservatório), o lugar é uma seção nova na a01 ou uma revisão do oa01, não um remendo desta revisão.

---

### 🟠 2. A armadilha central declarada do módulo era ensinada só em prosa

**Tipo:** abstração sem apoio visual, em passagem irredutivelmente geométrica
**Onde:** a01 · "Permeabilidade: o que ela mede e por que não é a mesma coisa que porosidade"
**Problema:** o hub do módulo declara, em "Pontos de dificuldade", que "porosidade alta não implica permeabilidade alta" é **a** dificuldade do módulo e que ela "contraria a intuição e derruba estimativas de fluxo". O oa01 a cobra. A própria a01 fecha dizendo que confundir as duas é "o erro mais comum de quem está começando em petrofísica". E então a distinção era explicada inteiramente em prosa corrida, exigindo que o leitor mantivesse simultaneamente na cabeça quatro litologias, dois atributos geométricos (corpo de poro × garganta de poro) e a relação não monotônica entre eles. Prosa é o pior meio possível para geometria comparativa — foi exatamente o achado `DID-M14-A06-VISUAL-002` do Módulo 14, e o precedente vale aqui com mais força, porque lá o visual apoiava um objetivo entre quatro e aqui apoia a dificuldade que o módulo se declara existir para vencer.
**Correção aplicada:** inserido diagrama esquemático com os quatro casos lado a lado — arenito limpo, arenito cimentado, folhelho e basalto vesicular —, cada um com sua φ e sua k na coluna da direita. A legenda de fechamento entrega as duas leituras que só o desenho torna óbvias: de (A) para (B) a porosidade cai 2 pontos e a permeabilidade cai por milhares; de (A) para (C) a porosidade quase dobra e a permeabilidade despenca oito ordens de grandeza. **Nenhum fato novo** — é destilação do que o texto já afirmava, com valores dentro das faixas por litologia que a própria aula publica, e declarados como ilustrativos.

---

### 🟠 3. Colisão de símbolos K/k atravessando três disciplinas, sem aviso

**Tipo:** notação acumulada sem consolidação
**Onde:** a02 · "Módulos elásticos" (e, por herança, a01 e o Módulo 01)
**Problema:** a letra K carrega três significados no percurso do aluno, e nenhum deles é errado — são convenções estabelecidas em disciplinas diferentes. No **Módulo 01** (hidrogeologia), K é **condutividade hidráulica**. Na **a01 deste módulo**, k minúsculo é **permeabilidade intrínseca**. Na **a02**, K maiúsculo é **módulo de compressibilidade**. O agravante é a proximidade: a a01 discute a lei de Darcy — exatamente o contexto em que o K do Módulo 01 vive na memória do leitor — e duas páginas depois a a02 introduz um K que não tem nada a ver com fluxo de fluido, sem uma palavra de aviso. O leitor que fez o Módulo 01 vai ler "K" e ativar o modelo mental errado.
**Correção aplicada:** nota destacada inserida na primeira ocorrência do K como módulo de compressibilidade, nomeando os três usos, dizendo de qual disciplina vem cada um e fechando com a regra prática ("identifique primeiro de qual disciplina o texto está falando"). Quatro linhas, resolve o atrito para o resto do módulo.

---

### 🟠 4. A a04 declarava um pré-requisito e dependia de três

**Tipo:** pré-requisito subdeclarado
**Onde:** a04 · cabeçalho
**Estava escrito:** "**Pré-requisito:** Aula 01 — porosidade e permeabilidade reaparecem aqui como os controles centrais da condutividade elétrica"
**Problema:** verdadeiro para a **primeira metade** da aula. Mas a segunda metade é a seção de integração do módulo, cuja tabela cruza densidade e velocidade sísmica (a02) com magnetismo e radioatividade (a03) — e cujo parágrafo de fechamento discute a cegueira relativa de cinco métodos geofísicos. Um leitor que confiasse no cabeçalho e pulasse a02 e a03 chegaria à tabela de fechamento sem nada com que lê-la, na exata seção que existe para amarrar o módulo. Cabeçalho subdeclarado é pior que cabeçalho ausente, porque autoriza ativamente o salto.
**Correção aplicada:** pré-requisito reescrito distinguindo as duas metades da aula, declarando a dependência real das a02 e a03 por inteiro na segunda, e advertindo explicitamente que esta é a única aula do módulo que reativa todas as anteriores.

---

### 🟡 5. A a03 são duas metades sem mecanismo comum, e a troca não era sinalizada onde acontece

**Tipo:** troca de assunto não sinalizada
**Onde:** a03 · início da seção "Radioatividade natural: de onde ela vem"
**Problema:** magnetismo e radioatividade não partilham mecanismo físico, instrumento nem raciocínio interpretativo — partilham apenas a lógica de "identificar o mineral responsável pelo contraste". A aula **anuncia isso muito bem no início** (a seção de abertura "Mudando de mecanismo físico" é das melhores transições do módulo), mas não repete o aviso **no ponto onde a troca de fato ocorre**, quinze parágrafos depois. É também a aula mais longa do módulo (2.798 palavras) e a que mais recebeu acréscimos da auditoria, o que aumenta a chance de o leitor pausar exatamente ali. Forma reduzida do achado `DID-M14-A07-DUASAULAS-001` — reduzida porque aqui as duas metades **servem ao mesmo objetivo declarado** (oa03) e a aula é 300 palavras mais curta que a a07 do Módulo 14 era.
**Correção aplicada:** **mitigado, não resolvido.** Nota destacada inserida no início da seção de radioatividade, marcando a troca de assunto, afirmando que nada na segunda metade depende da primeira, indicando o ponto como corte natural de pausa, e dizendo qual pré-requisito reativar ao voltar (a ideia geral da aula, não o conteúdo magnético). **Não recomendo dividir a a03**: ela está dentro dos 30 minutos, a divisão quebraria o mapeamento 1:1 entre aula e objetivo que é a maior força estrutural deste módulo, e o oa03 é declaradamente sobre as duas propriedades.

---

### 🟡 6. "Molhabilidade" entrou no módulo pela auditoria, sem definição

**Tipo:** termo técnico usado antes de definido
**Onde:** a04 · "A lei de Archie"
**Problema:** achado **introduzido pela própria auditoria desta rodada**, e registrado com honestidade. A correção do expoente de saturação n (achado laranja `PETROFIS-M15-A04-ARCHIEN-007`) trouxe *water-wet*, *oil-wet* e "molhabilidade neutra" para dentro da aula como termos centrais de um argumento quantitativo — e o conceito de **molhabilidade** nunca aparecera antes no módulo nem, pelo que a busca mostra, em nenhum módulo anterior do curso. Os termos estavam parcialmente auto-explicativos ("molhável por água"), mas o mecanismo que os torna importantes não estava dito.
**Correção aplicada:** glosa de duas linhas inserida na primeira ocorrência, definindo molhabilidade como a preferência da superfície mineral por um dos fluidos, com o contraste concreto (na water-wet a água adere à parede e o óleo fica no meio do poro; na oil-wet, o inverso) e a razão de importar aqui. Definição, não fato novo.

---

### 🔵 7. Nenhum exemplo trabalhado atravessa o módulo — e este módulo é o melhor candidato do curso

**Tipo:** oportunidade de integração
**Onde:** módulo inteiro
**Observação:** os quatro exemplos trabalhados são bons e independentes, mas nenhum reaproveita resultado de outro. É o mesmo achado `DID-M14-INTEGRACAO-009` do Módulo 14 — só que aqui a lacuna dói mais, porque a **tese declarada do módulo** é que as propriedades físicas se determinam mutuamente, e o aluno nunca é obrigado a percorrer essa cadeia com números.
**Não corrigido — encaminhado ao gerador de questionários,** com a mesma resolução adotada no Módulo 14 (fazer a integração no questionário, não reescrevendo a aula mais pesada). **O material já existe e a cadeia fecha sem inventar nada:** partir de um arenito com φ da a01 → densidade bulk pela equação da a02 → Vp e Vp/Vs pelos módulos elásticos → assinatura gama e magnética esperada pela a03 (arenito limpo = "frio" e fracamente magnético) → Sw por Archie na a04. É uma questão de síntese que percorre as quatro aulas sobre uma única rocha, e o módulo entrega todas as fórmulas necessárias.

---

### 🔵 8. oa03 é o objetivo mais amplo e tem uma aula só

**Tipo:** desequilíbrio de cobertura (não é lacuna)
**Onde:** mapeamento objetivo → aula
**Observação:** o módulo tem mapeamento **1:1 perfeito** entre objetivo e aula — oa01/a01, oa02/a02, oa03/a03, oa04/a04 —, o que é sua maior força estrutural e torna a decisão de questionário trivial. Mas os quatro objetivos não têm a mesma amplitude: oa01, oa02 e oa04 cobrem **um** domínio físico cada, enquanto **oa03 cobre dois** (magnetismo *e* radioatividade), que não partilham mecanismo. Não há buraco — a a03 ensina os dois por inteiro e o exemplo trabalhado exercita o segundo. Mas a superfície examinável do oa03 é maior que a dos outros três, e o questionário precisa extrair proporcionalmente mais questões da a03, ou o oa03 sai sub-avaliado numa de suas duas metades — provavelmente a magnética, já que o único exemplo trabalhado da aula é gamaespectrométrico.
**Não corrigido — encaminhado ao gerador de questionários.**

---

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo trabalhado | Verbo verificável | Avaliado em |
|---|---|---|---|---|
| `oa01` — porosidade e permeabilidade e seus controles | a01 inteira | sim (φ total × efetiva) + diagrama | definir, medir, explicar ✓ | pendente |
| `oa02` — densidade, módulos elásticos, Vp/Vs | a02 inteira | sim (Vp, Vs, Vp/Vs de calcário) | relacionar ✓ | pendente |
| `oa03` — magnetismo e radioatividade e seus minerais | a03 inteira | sim (Th/U de duas áreas) — só a metade radiométrica | explicar, identificar ✓ | pendente |
| `oa04` — lei de Archie e integração | a04 inteira | sim (F, R₀, Sw, Sh) + tabela de integração | aplicar, integrar ✓ | pendente |

**Nenhum objetivo sem seção que o ensine, nenhuma seção órfã, nenhum verbo não verificável** (nada de "entender" ou "conhecer" — os quatro usam definir, medir, explicar, relacionar, identificar, aplicar, integrar).

**Cadeia de pré-requisitos, após as correções:** a01 (nenhum interno) → a02 (a01, genuína: φ entra na equação de densidade bulk) → a03 (a02 declarada como posição, não dependência — e a aula **diz isso ao leitor**, que é o padrão correto fixado nos Módulos 13 e 14) → a04 (a01 para a primeira metade, a02 e a03 para a segunda, agora declarado). **NENHUM SALTO DE PRÉ-REQUISITO.**

**Os quatro exemplos trabalhados foram percorridos passo a passo e nenhum tem salto lógico.** Cada passo decorre do anterior sem inferência oculta, e os quatro terminam em interpretação, não em número.

**Alinhamento com a avaliação:** não avaliável nesta rodada — o módulo ainda não tem questionário nem baralho. As recomendações dos achados 7 e 8 foram encaminhadas ao gerador.

---

## Decisão sobre a estrutura do questionário

**QUESTIONÁRIO ÚNICO CUMULATIVO.** Sem parciais.

1. **Tamanho.** Quatro aulas, abaixo do limiar de ~5-6 que aciona parciais. Segue exatamente o critério já aplicado nos Módulos 02, 03, 04, 07, 10 e 12 (4-5 aulas → questionário único) e não o dos Módulos 06, 08, 09, 11, 13 e 14 (6-7 aulas → parciais + final).
2. **Volume de texto.** 10.074 palavras, o **menor de qualquer módulo recente** — pouco mais da metade das 18.566 do Módulo 14, que precisou de três parciais. Não há intervalo de verificação a proteger: quatro aulas curtas e uniformes cabem num único ponto de aferição.
3. **Não há corte conceitual que justifique parciais.** Este é o argumento decisivo, e ele é específico deste módulo. As quatro aulas são quatro **propriedades físicas paralelas**, não uma progressão em dois blocos: qualquer corte (a01-a02 / a03-a04, ou a01 / a02-a04) separaria propriedades que a aula final existe justamente para reunir. Comparar com o Módulo 14, onde o corte a05/a06 era de **mecanismo físico** e a própria aula o anunciava ao leitor — aqui, o "corte de mecanismo" acontece **quatro vezes**, uma por aula, e por isso não seleciona nenhum ponto de divisão privilegiado.
4. **O mapeamento 1:1 favorece o questionário único.** Com cada objetivo em exatamente uma aula, um questionário único com blocos por objetivo já entrega a granularidade que as parciais dariam, sem fragmentar a avaliação em quatro arquivos de 4 questões.
5. **A integração exige cumulativo.** O achado 7 recomenda que o questionário supra a ausência de um exemplo que atravesse o módulo. Isso só é possível num instrumento que cubra as quatro aulas de uma vez.

**Volume sugerido: 16 questões**, alinhado aos Módulos 03, 04, 10 e 12 (16 questões para módulos de 4-5 aulas), com IDs `geologia-avancado-m15-q01` a `q16`. Distribuição sugerida, respeitando o achado 8 (oa03 tem o dobro de amplitude): **oa01 4 questões · oa02 4 · oa03 5** (garantindo que a metade magnética não fique sub-avaliada, já que o único exemplo da aula é radiométrico) **· oa04 3, das quais a última é a questão de síntese** que percorre as quatro aulas sobre uma única rocha. Tipos: múltipla escolha, V/F com justificativa, dissertativa curta e aplicação/cálculo, os quatro presentes.

---

## O que está bem feito

- **A menor dispersão de carga do curso (18,2%).** Quatro aulas de tamanho quase igual, cada uma cobrindo exatamente um objetivo, cada uma com exatamente um exemplo trabalhado. Depois da dispersão de 62% do Módulo 14, este módulo é o exemplo do que a arquitetura modular deveria produzir — e o mérito é do planejamento, não da revisão: as aulas saíram do redator com 6,5% de dispersão.
- **O mapeamento 1:1 objetivo–aula.** Nenhum objetivo atravessa aulas, nenhuma aula serve a dois objetivos. Torna a cobertura trivialmente verificável e a decisão de questionário quase automática.
- **Toda aula abre dizendo por que aquela propriedade importa antes de formalizá-la.** A a01 abre explicando por que a petrofísica precede a geofísica; a a03 abre nomeando a troca de mecanismo físico; a a04 abre com o paradoxo produtivo "por que uma rocha conduz eletricidade, se seus minerais não conduzem". Motivação antes de formalização, feita com consistência nas quatro.
- **Os títulos de seção fazem trabalho pedagógico, não só rotulam.** "Porosidade: definição e o que ela **não** diz sozinha", "Três densidades que **não são a mesma coisa**", "A relação (**frágil**) entre porosidade e permeabilidade", "Por que uma rocha conduz eletricidade, **se seus minerais não conduzem**". Cada um já anuncia a armadilha que a seção vai desarmar — o leitor sabe onde prestar atenção antes de começar a ler.
- **Os quatro exemplos trabalhados terminam em interpretação, não em número.** O melhor é o da a03, o único de duas etapas: calcula duas razões e então mostra que **nenhum canal isolado** resolveria a distinção, fechando com o argumento de por que a espectrometria reporta três canais separados em vez de uma contagem total. É o exemplo mais bem construído do módulo.
- **A aula final integra de verdade.** A tabela propriedade → método não é um resumo: é o argumento que justifica a existência do Módulo 16, e o parágrafo que a segue transforma a limitação de cada método em razão para a integração multimétodo. Poucos módulos do curso fecham tão bem.
- **Disciplina de definir por aposto na primeira ocorrência**, com as duas exceções corrigidas nesta revisão (K e molhabilidade): porosidade, permeabilidade, darcy, garganta de poro, tortuosidade, impedância acústica, magnetização remanente, dupla camada elétrica, fator de formação — todos glosados onde aparecem.
- **As transições entre aulas nomeiam o que muda.** A da a02 para a a03 é a melhor: "muda o campo físico explorado: em vez de ondas elásticas, a próxima aula trata de como minerais específicos tornam uma rocha magnética ou radioativa" — exatamente onde o leitor mais precisa ser avisado.
