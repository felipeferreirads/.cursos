# Auditoria científica: Módulo 04 — Pérolas e gemas orgânicas

**Auditado em:** 2026-08-25 (rodada 1, 5 aulas) · 2026-08-28 (rodada 2, seção "Casco de tartaruga" da aula 05)
**Material:** `04-perolas/` — 5 aulas e o hub do módulo. Todas são texto de primeira redação; nenhuma foi migrada de outro curso.
**Escopo desta partição:** a auditoria original de 2026-08-25 cobriu o módulo único `03-gemas-coradas-perolas`, de 21 aulas. Em 2026-08-26 aquele módulo foi dividido em `03-gemas-coradas` (aulas 01–16) e `04-perolas` (ex-aulas 17–21, renumeradas 01–05). Este relatório ficou com os itens das aulas biológicas; os das aulas minerais estão em [[03-gemas-coradas-auditoria|auditoria do módulo 03]]. Nada foi reauditado, criado ou descartado na divisão.
**Modo:** audit-and-fix
**Profundidade:** full
**Escopo:** biologia e estrutura do nácar; formação da pérola natural e da cultivada; tipos comerciais de pérola cultivada e técnicas de nucleação; os sete fatores de valor do GIA para pérolas; ensaios de identificação e tratamentos de pérola; âmbar, copal, azeviche, coral, marfim e madrepérola; regime CITES aplicável a coral e a marfim; **consistência numérica interna entre as 5 aulas** e entre elas e os módulos 01 e 03.
**Veredito final:** **Aprovado** (rodadas 1 e 2). Aula 05 inteiramente auditada, incluindo a seção "Casco de tartaruga".

> [!info] Ordem de execução
> Esta auditoria rodou **antes** da geração do questionário e do baralho, conforme a ordem adotada no curso: auditar → corrigir → só então avaliar e cardificar. Nenhum material derivado precisou de propagação, porque nenhum existia quando as correções foram aplicadas.

## Resumo

**Rodada 1 (2026-08-25, 51 alegações das 5 aulas):** 🔴 0 · 🟠 1 · 🟡 0 · 🔵 0 · ⚪ 3. 50 corretas; o único 🟠 corrigido na mesma rodada.

**Rodada 2 (2026-08-28, 4 alegações `TRT-*` da seção casco de tartaruga):** 🔴 0 · 🟠 0 · 🟡 0 · 🔵 0 · ⚪ 0. **Todas corretas — nenhum achado.** Detalhe na seção "Rodada 2" abaixo.

**Nenhum achado permanece aberto.** As três controvérsias da rodada 1 foram tratadas na redação sob a regra LC-08 e **não** são pendências. Com a rodada 2, a aula 05 está inteiramente auditada.

O padrão do módulo é próprio, e vale registrá-lo: aqui **não há propriedade física a conferir contra tabela** — não há índice de refração útil nem birrefringência —, e o risco factual migra para outro lugar. Ele está nas **idades geológicas** (âmbar), nos **critérios estatísticos** (ângulos de Schreger), no **regime legal** (CITES) e na **nomenclatura reservada** (pérola, cultivada, imitação). Foi exatamente numa idade geológica que o único achado apareceu; os três demais eixos passaram.

## Achados

### 🟠 1. A idade do âmbar báltico estava estreita demais e omitia a controvérsia

**claim_id:** `AMB-ORIG-001`
**Tipo:** impreciso (faixa numérica estreita demais; controvérsia não declarada) · **Natureza:** `erro_factual` em grau leve, com componente de `omissao_de_controversia`
**Onde:** aula 04 (então aula 20 do módulo único) · "Âmbar: resina que virou fóssil", tabela de fontes e idades
**Estava escrito:** "**Báltico** (succinita) | ~34–38 milhões de anos | o mais abundante e o mais estudado"
**Problema:** a literatura não converge para esse intervalo. As estimativas para o âmbar báltico cobrem aproximadamente **34 a 48 milhões de anos**, e a dispersão não é ruído de medida: é uma **disputa real** sobre se o material é autóctone nas camadas do Eoceno superior — o que o colocaria em torno de 34 a 38 Ma, na atribuição priaboniana clássica — ou se foi **retrabalhado e redepositado**, tendo se formado no Eoceno médio, perto de 44 Ma. Apresentar a faixa estreita como fato fechado violava, além disso, a regra LC-08 do curso, que exige declarar controvérsia em uma frase.
**Correção aplicada:** a tabela passou a registrar "~**34–48** milhões de anos (Eoceno) … a idade exata é **debatida**", e foi acrescentado um parágrafo explicando as duas hipóteses. Foi criada a alegação nova `AMB-ORIG-002` para a controvérsia, e uma linha correspondente em "O que não concluir". O recap foi atualizado.
**Fonte:** revisão crítica da idade do âmbar báltico da península de Samland (*Earth and Environmental Science Transactions of the Royal Society of Edinburgh*); literatura de datação por bioestratigrafia e por K-Ar de glauconita das camadas · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** nenhum outro arquivo do curso.
**Desfecho:** ✅ **Corrigido.**

## Controvérsias declaradas (⚪ — verificadas, não são pendências)

Três passagens do módulo declaram explicitamente um debate aberto em vez de arbitrá-lo, conforme a regra LC-08. As três foram verificadas como controvérsias reais e **corretamente representadas**. As outras duas controvérsias da auditoria original são das aulas minerais e estão em [[03-gemas-coradas-auditoria|auditoria do módulo 03]].

| claim_id | Aula | Do que se trata | Situação na literatura |
|---|---|---|---|
| `PER-TRAT-004` | 03 | O **maeshori** deve ser divulgado como tratamento? | Divergência real de prática no setor; a aula declara a divergência e não a resolve |
| `AMB-COP-001` | 04 | Onde termina o **copal** e começa o **âmbar** | Não há idade-limite consensual; a distinção é de grau de maturação num contínuo. A aula diz exatamente isso |
| `AMB-ORIG-002` | 04 | **Idade do âmbar báltico** — autóctone no Eoceno superior ou redepositado do Eoceno médio | Controvérsia ativa. Alegação **criada nesta auditoria**, a partir do achado 🟠 1 |

## Verificações que passaram, e que valeram o esforço

Registro do que foi checado e **não** virou achado, para que uma auditoria futura não refaça o trabalho:

- **Ângulos de Schreger.** Confirmado o critério de Espinoza & Mann: ângulos externos tipicamente **>115°** no elefante e **<90°** no mamute, **com zona de sobreposição entre 90° e 115°** que exige múltiplas medições. A aula 05 já declarava o critério como estatístico e sujeito a sobreposição — formulação correta.
- **Situação CITES do coral precioso.** Confirmado que as propostas de inclusão de *Corallium* no Apêndice II foram apresentadas e **rejeitadas** na CoP14 (2007) e na CoP15 (2010), e que os corais negros (Antipatharia) e outros grupos **estão** no Apêndice II. Confirmado também que a ausência de listagem não implica ausência de regulação. A aula 05 apresenta a distinção corretamente — e ela é o oposto do que a maioria das fontes de varejo afirma.
- **Idade do âmbar dominicano.** Confirmados os 15 a 20 milhões de anos de Iturralde-Vinent & MacPhee, *Science* 273 (1996).
- **Composição do nácar.** Confirmados os valores gemológicos de referência: ~82–86 % de aragonita, ~10–14 % de conquiolina e ~2 % de água. Ver a nota deferida abaixo. Os mesmos valores aparecem de forma idêntica nas aulas 01 e 05.
- **Nomenclatura reservada.** Confirmado contra CIBJO *Pearl Blue Book* e FTC *Jewelry Guides*: "pérola" sem qualificativo designa pérola natural; "cultivada" é reservado à pérola e não se aplica a gema mineral; não existe "pérola sintética", apenas imitação de pérola. A simetria com a regra de "sintético" da aula 16 do módulo 03 está correta nos dois lados.
- **História da pérola cultivada.** Confirmadas as datas de Mikimoto, Mise e Nishikawa, a patente de 1907 do método de enxerto e a de 1916 para esféricas.

## Achados deferidos (não bloqueantes)

Um ponto deste módulo foi examinado, considerado **defensável como está** e registrado para revisão futura, sem correção nesta rodada. A outra nota deferida da auditoria original é da aula de topázio e peridoto e ficou no módulo 03.

| id | Aula | Questão | Por que fica assim |
|---|---|---|---|
| `GEM-PER-NACRE-PCT-001` | 01 | Os percentuais 82–86 / 10–14 / 2 são os de referência **gemológica** para o nácar de pérola; parte da literatura de ciência dos materiais cita ~95 % de aragonita para o nácar em geral | A divergência decorre do material medido (pérola × madrepérola de concha) e do método. A aula usa a fonte adequada ao domínio, e a alteração exigiria uma discussão metodológica desproporcional ao nível da aula |

## Método

- **Alegações auditáveis** extraídas dos blocos `alegacoes_auditaveis` em comentário HTML no rodapé das aulas. A rodada de 2026-08-25 registrou **204** alegações nas 21 aulas do módulo então único; **51** delas são das 5 aulas que formam este módulo — hoje **8 + 12 + 11 + 12 + 8** (era 8 + 10 + 11 + 12 + 10 até a realocação de 2026-08-28 registrada abaixo).
- **Priorização por risco declarado:** alegações marcadas `numero` e `nomenclatura` foram verificadas uma a uma contra fonte; as marcadas `mecanismo` foram verificadas quanto à direção causal; as marcadas `interpretacao` e `controverso` foram verificadas quanto à **calibragem** — se a afirmação é tão forte quanto a evidência sustenta, e não mais.
- **Fontes de referência, por ordem de precedência:** literatura revisada por pares (*Science*, *Earth and Environmental Science Transactions of the Royal Society of Edinburgh*) → normas e convenções (CITES, CIBJO *Pearl Blue Book* e *Coral Blue Book*, FTC, Reino Unido *Ivory Act 2018*) → referências de área (GIA *Pearl Description*, *Pearl Quality Factors* e *Gems & Gemology*, Strack, Grimaldi, Muller, Espinoza & Mann) → bases de dados minerais (Mindat, IMA-CNMNC), quando aplicáveis.
- **Verificação cruzada entre módulos** executada sobre a composição do nácar (aulas 01 e 05) e sobre a simetria de nomenclatura com a aula 16 do módulo 03.
- **Divergência conhecida e herdada:** o formato de `claim_id` deste curso usa três segmentos (`AMB-ORIG-001`), enquanto o `audit.schema.json` do plugin exige quatro. É a mesma divergência já registrada em `_contexto.md` para os módulos 01 e 02. A exceção é o id deferido acima, que nasceu nesta auditoria e já segue o formato de quatro segmentos.
- **Reconstrução do registro em JSON.** Na divisão de 2026-08-26, as 51 alegações auditáveis deste módulo foram relidas dos blocos `alegacoes_auditaveis` no rodapé das cinco aulas — a mesma fonte usada pela auditoria original — e as controvérsias e a nota deferida foram recompostas a partir deste relatório. O conteúdo é idêntico ao registrado em 2026-08-25; **nenhuma verificação nova foi feita na divisão**, e o registro traz a nota em `split_from.reconstruction_note`.

## Realocação de alegações (2026-08-28)

Em **2026-08-27** a seção **Madrepérola** saiu da aula 05 — que passou a se chamar "Gemas orgânicas II: coral e marfim" — e foi para o fim da aula 02, resolvendo o achado 🟠 1 da [[04-perolas-revisao-didatica|revisão didática]]. Em **2026-08-28** o registro desta auditoria foi propagado.

| claim_id | Antes | Agora | O que mudou |
|---|---|---|---|
| `MPE-EST-001` | aula 05 | **aula 02** | apenas o arquivo de origem |
| `MPE-USO-001` | aula 05 | **aula 02** | apenas o arquivo de origem |

> [!warning] Os IDs são `MPE-*`, não `PER-MAD-*`
> O `course-state.yaml` e as notas de trabalho de 2026-08-27 se referiam a estas duas alegações como "as alegações `PER-MAD-*`". **Esse prefixo nunca existiu** neste módulo: as alegações de madrepérola sempre foram `MPE-EST-001` e `MPE-USO-001`. Fica o registro para que ninguém procure um par de IDs que não existe.

**Nenhuma alegação foi criada, alterada ou descartada, e nenhuma foi reauditada.** O total continua **51**; só a distribuição por aula mudou, de 8 + 10 + 11 + 12 + 10 para **8 + 12 + 11 + 12 + 8**. O veredito, o saldo de achados e as controvérsias permanecem como estavam. No manifesto JSON, cada uma das duas alegações traz `moved_from`, `moved_at` e `move_note`, e a operação está registrada em `claims_migrated`.

## Rodada 2 — 2026-08-28 (seção "Casco de tartaruga", aula 05)

A seção de casco de tartaruga foi acrescentada à aula 05 em 2026-08-28 para fechar a lacuna aprovada. Esta rodada auditou as **4 alegações `TRT-*`** contra Webster (*Gems*), O'Donoghue (*Gems*, 6ª ed.), GIA *Gems & Gemology* e a base oficial da CITES.

**Resultado: 4 corretas · 🔴 0 · 🟠 0 · 🟡 0 · 🔵 0 · ⚪ 0. Nenhum achado.**

- **`TRT-EST-001`** — placas córneas da carapaça dorsal da tartaruga-de-pente *Eretmochelys imbricata*, β-queratina; IR ~1,55, DR ~1,29, dureza Mohs ~2,5, cheiro de cabelo queimado no ponto quente. Valores conferidos com Webster e O'Donoghue.
- **`TRT-USO-001`** — termoplástico, solda em si mesmo sob calor e pressão ("casco prensado" / *bekko*), junção visível à lupa como linha reta. Confirmado.
- **`TRT-IMI-001`** — grânulos de pigmento arredondados no genuíno vs. faixas/redemoinhos sem grânulos no celuloide/caseína/baquelite; padrão repetido de molde; **a densidade confirma mas não separa** (faixas dos plásticos vizinhas de ~1,29); cheiros distintos no ponto quente (cabelo queimado / cânfora / leite queimado). Confirmado — a ressalva sobre a densidade é correta e vai deliberadamente contra a simplificação de varejo.
- **`TRT-CITES-001`** — *Eretmochelys imbricata* no **Apêndice I da CITES desde 04/02/1977**; comércio internacional comercial proibido; o Japão manteve reserva à listagem e encerrou a importação de *bekko* no início da década de 1990 (redação hedgeada, correta). Confirmado contra cites.org.

## Correções aplicadas

### Rodada 1 — 2026-08-25

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `AMB-ORIG-001` | 🟠 | Corrigido | 04-perolas-aula-04-gemas-organicas-1-ambar-copal-e-azeviche.md |

Como o questionário e o baralho deste módulo foram gerados **depois** desta rodada, não houve propagação para material derivado. A divisão do módulo em 2026-08-26 não alterou nenhum texto de aula.

### Rodada 2 — 2026-08-28 (casco de tartaruga)

Nenhuma correção: as 4 alegações `TRT-*` passaram limpas. Única edição de arquivo foi a flag `pendencias.auditoria_cientifica` do rodapé da aula 05 (`parcial → false`).

**Pendências:** a seção de casco de tartaruga segue sem revisão didática, sem questão e sem flashcard — e o objetivo `gemologia-m04-oa05`, embora coberto por questão desde 2026-08-25, só tem questão sobre coral e marfim (cobertura parcial, registrada em `assessment.partial_coverage_note`).

## Navegação

- Módulo: [[04-perolas-modulo|Módulo 04 — Pérolas e gemas orgânicas]]
- Auditoria do módulo irmão: [[03-gemas-coradas-auditoria|Módulo 03 — Gemas coradas]]
- Revisão didática: [[04-perolas-revisao-didatica|relatório]]
- Contexto do curso: [[_contexto|decisões duradouras]]
