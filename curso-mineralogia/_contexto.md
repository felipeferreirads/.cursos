# Contexto — Curso de Mineralogia

Preferências e decisões duradouras sobre **como** este curso é ensinado. Não é estado de progresso — isso vive em `course-state.yaml`. Este arquivo **só cresce**: qualquer skill pode acrescentar uma seção ou uma linha, nenhuma pode reescrevê-lo por inteiro.

Criado em **2026-09-29** pelo `planejador-curricular`, no ato de planejamento do currículo. Nenhuma aula existia quando ele foi escrito.

## O que este curso é

Um curso de **mineralogia geocientífica geral, completo e autossuficiente**, do ensino médio ao nível avançado: cristalografia geométrica e de difração, cristaloquímica, termodinâmica e diagramas de fase, crescimento cristalino e texturas, maclas e defeitos, mineralogia óptica, métodos analíticos, sistemática por classes (IMA, Nickel-Strunz, Dana), gênese e paragênese por ambiente, evolução mineral e biomineralização. Tem aprofundamentos em espécies minerais e em mineralogia gemológica, e fecha o núcleo com um gancho de catalogação de espécimes de coleção.

São **50 módulos em 13 áreas temáticas**, **262 aulas planejadas** (199 no núcleo, 63 nos aprofundamentos), **244 objetivos de aprendizagem**, estimativa de **~109-131 h** de estudo (núcleo ~83-100 h).

## Perfil e nível

- **Partida:** ensino médio completo, **sem geologia prévia**.
- **Chegada:** avançado — nível de graduação plena em mineralogia e cristalografia (referência: GMG0106 + GMG0220 do IGc-USP, 150 h de aula), com incursões de pós-graduação nos módulos de aprofundamento.
- **Aplicação prática declarada:** formação geocientífica ampla e descrição rigorosa de espécimes de coleção (o usuário mantém coleção e já usa o plugin para catalogá-la).

## Decisão estrutural: curso autossuficiente

> [!warning] Regra dura — vale para toda skill a jusante
> Este curso **não tem pré-requisito cruzado**. Toda a base — química (módulo 01), contexto geológico (módulo 03), óptica ondulatória (módulo 14), matemática reativada antes do uso — é reescrita **dentro** dele. Outros cursos aparecem **só como remissão**, citados **por nome** ("curso-geologia, módulo 04, aula 05"), **nunca por wikilink**: um wikilink para fora do curso quebra no Obsidian e é reportado como link morto pelo `validador-estrutural-do-curso`. Mesma regra já em vigor no curso-gemologia e no curso-lapidacao.

Consequência aceita: há sobreposição deliberada com o curso-geologia (módulos 04 e 05) e com o curso-gemologia. Ela é o preço da autossuficiência. A regra para conviver com ela é **não contradizer** (ver o mapa de sobreposição abaixo) e **ir além** do que o curso irmão faz, nunca repetir no mesmo nível.

## Viés e fronteiras com os cursos irmãos

- **Viés geocientífico geral.** O centro é cristalografia, cristaloquímica, termodinâmica, gênese e paragênese.
- **Gemologia fica com o curso-gemologia.** Aqui só entram os módulos 48-49 (mineralogia gemológica), que explicam **mecanismo estrutural** (por que a cor, por que o tratamento funciona, por que a síntese deixa aquela feição) e **não** ensinam identificação por instrumento, graduação, valor, mercado, procedência, laudo nem regra de divulgação.
- **Lapidação fica com o curso-lapidacao.** Nenhum módulo trata de talhe; a óptica do talhe é citada por nome.
- **Catalogação é um gancho, não um curso.** Um módulo de 3 aulas (50) que aplica o curso inteiro à ficha de um espécime, usando os campos do usuário e a escada de inferência.

## Trilha dupla: núcleo e aprofundamento

Decisão do usuário: cada módulo é marcado como **núcleo** ou **aprofundamento**. O usuário estuda o núcleo primeiro, na ordem numérica, pulando os aprofundamentos, e volta a eles depois.

> [!note] Onde a trilha fica registrada (limite do schema)
> O `schemas/course-state.schema.json` do plugin **não tem campo** para a trilha, e o objeto `module` tem `additionalProperties: false` — acrescentar um campo quebraria a validação. Por isso a trilha está registrada, sem tocar no schema, em quatro lugares: **(1)** esta tabela, que é o registro canônico; **(2)** uma entrada em `decisions` do `course-state.yaml`; **(3)** um comentário `# trilha: ...` acima de cada módulo no YAML (atenção: comentários se perdem se um script regravar o YAML com PyYAML — nesse caso, esta tabela e a decisão continuam valendo); **(4)** a seção "Trilha" do hub de cada módulo. Se o plugin um dia ganhar um campo `track`, migrar a partir desta tabela.

**Regra de fechamento, verificada no planejamento:** nenhum módulo do núcleo tem como pré-requisito um módulo de aprofundamento. O núcleo sozinho é um curso coerente.

| Área | Núcleo | Aprofundamento |
|---|---|---|
| I. Fundamentos: da matéria ao mineral | 01, 02, 03 | — |
| II. Cristalografia geométrica e reticular | 04, 05, 06 | 07 |
| III. Cristaloquímica | 08, 09, 10, 11, 12 | — |
| IV. Propriedades físicas e identificação macroscópica | 13 | — |
| V. Mineralogia óptica | 14, 15, 16 | 17 |
| VI. Difração e métodos analíticos | 18, 19 | 20, 21 |
| VII. Termodinâmica, diagramas de fase e cinética | 22, 23 | 24 |
| VIII. Crescimento cristalino, texturas e inclusões | 25, 26, 27 | 28 |
| IX. Mineralogia sistemática | 29, 30, 31, 32, 33, 34, 35, 36 | — |
| X. Gênese e paragênese | 37, 38, 39, 40, 41 | 42, 43 |
| XI. Mineralogia no tempo e na vida | — | 44, 45 |
| XII. Espécies minerais e mineralogia gemológica | — | 46, 47, 48, 49 |
| XIII. Catalogação de espécimes | 50 | — |

Totais: **36 módulos de núcleo (199 aulas)**, **14 de aprofundamento (63 aulas)**.

## Ajuste de escopo de 2026-09-29: espécies minerais e mineralogia gemológica

Pedido do usuário, repassado pelo orquestrador durante o planejamento: incluir, quando justificado, módulos de espécies minerais e de mineralogia gemológica, como aprofundamento por padrão.

**Incluídos:**

- **46 — Espécies minerais I** (quartzo, granada, turmalina, berilo, zircão) e **47 — Espécies minerais II** (coríndon, espinélio, calcita-aragonita, fluorita, pirita, apatita). Justificativa: a sistemática (área IX) descreve por grupo; o estudo de caso por espécie **integra** cristalografia, cristaloquímica, polimorfismo, crescimento, zoneamento, gênese e identificação em torno de um objeto só — é a forma de consolidação que falta a um curso organizado por disciplina. Critério de escolha: importância geológica **e** presença em coleção, com pelo menos um fenômeno ensinado no curso bem representado em cada espécie (maclas no quartzo, zoneamento na granada e na turmalina, canais no berilo, metamictização no zircão, polimorfismo na calcita, centros de cor na fluorita, hábito e pseudomorfose na pirita).
- **48 — Mineralogia gemológica I** (campo cristalino, transferência de carga, centros de cor, bandas, cor estrutural, fenômenos por exsolução, da indicatriz aos instrumentos gemológicos) e **49 — Mineralogia gemológica II** (tratamento térmico como química de defeitos e difusão, irradiação e HPHT, rotas de síntese como crescimento cristalino, inclusões diagnósticas). Justificativa: Klein & Dutrow dedicam um capítulo a gem minerals; a USP oferece GMG0425; e o curso-gemologia trata esses temas no nível do **que se observa e como se identifica**, não do mecanismo estrutural.

**Não incluídos (e por quê):**

- **Feldspatos e diamante como monografia.** Os feldspatos já têm tratamento de graduação no módulo 36 e de aprofundamento no curso-geologia-avancado, módulo 40 (14 aulas); uma monografia seria a terceira versão do mesmo conteúdo. O diamante como mineral e sua origem estão no curso-gemologia, módulo 02 (aulas 01-04), e no módulo 43 deste curso (manto e inclusões).
- **Monografias de minérios metálicos** (calcopirita, galena, esfalerita, cassiterita, wolframita). Ficam na sistemática (30-32) e nos módulos 36-37 do curso-geologia-avancado.

**Regra para os módulos 46-49:** citar o curso-gemologia por nome onde ele trata a mesma espécie ou o mesmo fenômeno, **não repetir** propriedades gemológicas, fatores de valor, procedências nem regra de divulgação, e **não contradizer** (ver mapa abaixo).

## Espinha didática: a escada de inferência

Vinda do insumo do usuário e adotada como método de todo o bloco de texturas (módulos 25-27), da paragênese (37) e da catalogação (50):

**observação → descrição interpretativa → interpretação genética → hipótese de processo.**

Toda aula desses módulos deve deixar visível em que degrau está cada afirmação. Erro típico a combater: pular da observação ("bandas de cor paralelas às faces") direto para o processo ("mudança de temperatura do fluido"). Isto conversa com a regra do plugin de separar fato de interpretação.

## Insumos do usuário e o que foi verificado

Os dois insumos do usuário são **material de partida, não fonte**. Nenhum dos dois estava gravado em arquivo no momento do planejamento; o planejador trabalhou com a descrição feita pelo orquestrador. Quando o gerador de aulas os receber, toda afirmação vinda deles entra em `alegacoes_auditaveis` e passa pelo `auditor-cientifico`.

### 1. Resumo de IA sobre crescimento, zoneamento, sobrecrescimento, epitaxia, sintaxia, exsolução, macla, inclusões e dissolução

- **A espinha** (a escada de inferência) foi adotada — ver seção acima.
- **Cobertura:** crescimento → módulo 25; zoneamento → 26; sobrecrescimento, epitaxia × sintaxia, intercrescimento, dissolução, pseudomorfose e inclusões proto/sin/epigenéticas → 27; exsolução → 23 (núcleo) e 24 (aprofundamento); macla → 12.
- **Citação "(Nature)" de 2024 — verificada na fonte durante o planejamento.** O estudo de 2024 sobre epitaxia e singenesia em inclusões de diamante é **Bruno, M., Ghignone, S., Aquilano, D. & Nestola, F. (2024). A critique of using epitaxial criterion to discriminate between protogenetic and syngenetic mineral inclusions in diamond. _Scientific Reports_ 14, doi:10.1038/s41598-024-59432-6.** Dois ajustes em relação ao insumo:
  1. A revista é a **Scientific Reports** (portfólio Nature), **não a _Nature_**. Citar como "Nature" é erro de atribuição.
  2. O artigo **contesta** o uso da relação epitaxial (e da morfologia imposta pelo diamante) como prova de singenesia e propõe que a maioria das inclusões em diamante seja **protogenética**. Se o resumo de IA apresentar a epitaxia como evidência de singenesia, isso está **invertido** em relação ao estudo.
  - Contexto correlato, a confirmar na auditoria antes de citar: Nestola et al. (2017), "Mineral inclusions in diamonds may be synchronous but not syngenetic", _Nature Communications_; e o trabalho de orientação cristalográfica de inclusões de olivina em diamante (Lithos, 2016). Não foi encontrado, no planejamento, um artigo de 2024 na revista _Nature_ propriamente dita sobre o tema. Se o insumo citar "estudos" no plural, o auditor deve localizar cada um.
- **Terminologia a travar na auditoria:** sintaxia = sobrecrescimento orientado da **mesma** fase (ex.: quartzo autigênico sobre grão detrítico de quartzo); epitaxia = sobrecrescimento orientado de **fase diferente**; topotaxia = transformação no estado sólido com relação de orientação. Os termos proto-, sin- e epigenético para inclusões vêm da tradição gemológica (Gübelin) e têm critérios contestados — o módulo 27 apresenta o debate, não uma regra.

### 2. Lista de campos de catalogação de espécimes

Grupos declarados pelo usuário: **cristalográficos/morfológicos; texturais/de crescimento; superfície/alteração; associação mineralógica; visuais; propriedades físicas variáveis.** Mapeamento: módulo 50, aulas 01 (cristalográficos, morfológicos, texturais) e 02 (superfície, alteração, associação, visuais, propriedades variáveis); a aula 03 aplica a escada de inferência à redação da ficha.

> [!note] Lacuna de schema observada, sem ação
> O `schemas/specimen.schema.json` do plugin (usado pelo `catalogador-de-colecao`) tem só `habit_or_form`, `matrix`, `condition` e `damage` como campos descritivos físicos — não tem campos para macla, zoneamento, inclusões, superfície/alteração nem paragênese. O módulo 50 ensina a descrição completa; os campos extras vão em `notes` do registro até que o plugin decida ampliar o schema. Não alterar o schema a partir deste curso.

## Mapa de sobreposição e remissões

Levantado lendo os hubs, os objetivos e os títulos de aula dos cursos existentes. **Nenhum outro curso foi alterado.**

### curso-geologia (introdutório; pré-requisito declarado do curso-gemologia)

| Curso irmão | O que cobre | Aqui | Cuidado para não contradizer |
|---|---|---|---|
| m04 a01-a02 (pontes de átomo e ligação) | elétrons, tabela, ligação, nível funcional | 01 (vai além: orbitais d, oxidação, estequiometria) | eletronegatividade decide ligação; raio decide substituição — mesma distinção |
| m04 a03 (definição de mineral) | "cinco critérios": sólido, natural, **inorgânico**, composição definida, estrutura ordenada | 02 | **Ponto sensível.** A definição da IMA (Nickel, 1995) não exige "inorgânico" literalmente e há minerais orgânicos aprovados. O módulo 02 apresenta a definição da IMA e trata os "cinco critérios" como simplificação didática corrente, **sem dizer que o curso-geologia está errado**. Recomenda-se rodar o `auditor-cientifico` em modo `cross-course` sobre m04 a03 do curso-geologia quando o módulo 02 daqui for escrito. |
| m04 a04-a05 (simetria, sete sistemas) | qualitativo, sem notação | 04 | manter "sete sistemas cristalinos" (convenção IUCr) e apresentar famílias e sistemas reticulares como refinamento |
| m04 a06 (Strunz/Dana) | classes pelo ânion | 02, 29 | mesmo critério |
| m04 a07 (silicatos) | tetraedro e polimerização | 11 | — |
| m05 a01-a03 (propriedades, grupos, chave macroscópica) | nível introdutório | 13 | Mohs ordinal (1812), mesma leitura |
| m05 a04-a07 (luz, óptica 1-2, microscópio) | funcional, sem Snell nem indicatriz | 14-16 | lâmina ~0,03 mm; geminação polissintética do plagioclásio |
| m06, m08 (ígneas, metamórficas) | Bowen, fácies | 38, 40 | — |
| m09 (geoquímica: Goldschmidt, fases, geotermobarometria) | introdutório | 09, 22, 42 | — |
| m16 a04, a05b (biomineralização, biogenicidade) | introdutório | 45 | — |
| m21 (depósitos supergênicos) | introdutório | 41 | — |

### curso-gemologia

| Curso irmão | O que cobre | Aqui | Cuidado |
|---|---|---|---|
| m01 a01 (gema, espécie, variedade, nome comercial) | visão gemológica, CIBJO | 02, 29 | espécie IMA × nome comercial CIBJO: mesma distinção |
| m01 a02 (origem da cor, **cinco mecanismos**: campo cristalino, transferência de carga, centros de cor, bandas, cor estrutural) | nível do que se observa | 48 | manter a divisão em cinco mecanismos; a teoria do campo cristalino entra como detalhamento, não como classificação concorrente |
| m01 a03-a06, a08-a11 (propriedades, refratômetro, polariscópio, dicroscópio, espectroscópio, lupa e microscópio, densidade, fluorescência, espectroscopia de laboratório) | instrumentos gemológicos | 13, 14-16, 20, 48 a06 | 48 a06 liga instrumento à indicatriz; não ensina operar o instrumento |
| m01 a14-a15 (gemas fenomenais) | observação | 48 a04-a05 | — |
| m01 a20-a21 (ambientes formadores, províncias brasileiras) | panorama | 38-41 | — |
| m02 a01-a04 (diamante como mineral, origem, superprofundos, tipos Ia/Ib/IIa/IIb) | — | 43, 49 | mesma leitura do diagrama P-T do carbono; mesma classificação por tipo |
| m02 a12-a15 (HPHT, CVD, triagem, tratamentos) | crescimento e detecção | 49 | aqui só o mecanismo |
| m03 a04-a13 e a18-a19 (coríndon, berilo, turmalina, granadas, espinélio, crisoberilo, topázio, peridoto, quartzo, calcedônia, zircão, tanzanita, espodumênio, iolita, gemas de colecionador) | espécies como gemas | 33, 36, 46-47 | citar por nome; não repetir propriedades gemológicas nem valor |
| m03 a15-a17 (tratamentos, rotas de síntese, imitações, divulgação) | mapa gemológico | 49 | terminologia de sintéticos igual à do curso-gemologia |
| m04 (pérolas e gemas orgânicas) | — | 45 | — |

### curso-geologia-avancado (nível de pós-graduação; é o aprofundamento natural de vários módulos daqui)

| Curso irmão | Aqui | Cuidado |
|---|---|---|
| m40 — Mineralogia dos tectossilicatos (14 aulas, base Vlach/IGc-USP) | 36 (graduação), 10, 12, 23 | **não contradizer** leis de geminação, nomenclatura de estado estrutural (sanidina, ortoclásio, microclínio), campos P-T da sílica, pertitas; divergências já registradas na auditoria do m40 valem como referência |
| m36-m37 — Microscopia de minérios; petrografia de minério | 17, 30, 37 | 17 é só a porta de entrada |
| m32 — Pegmatitos (26 aulas) | 38, 46 | classificação Černý & Ercit (2005) e Wise, Müller & Simmons (2022) |
| m34 — Sistemas hidrotermais e metalogênese | 39 | nomes dos estilos de alteração |
| m27 — Petrocronologia (zoneamento de acessórios e granada, técnicas, average P-T) | 26, 40, 42, 46 | — |
| m39 — Análise textural (BSE, EBSD, CSD, nucleação) | 21, 24, 25 | — |
| m28 — Análise instrumental I (FRX, ICP de amostra total) | 18-20 | difração não é tratada lá |
| m26 — Geologia isotópica | 46 (zircão) | datação não é ensinada aqui |
| m30 — Kimberlitos e carbonatitos | 43 | — |
| m15 — Petrofísica (magnetismo e radioatividade das rochas) | 13, 31 | — |
| m09 — Geometalurgia (mineralogia de processo) | fora do escopo | — |

### curso-lapidacao

Declara mineralogia e cristalografia **fora** do seu escopo. Tocam este curso: m05 (leitura do bruto: inclusões, pleocroísmo, eixo óptico) → 16, 27; m08 (ângulo crítico, óptica do talhe) → 14, 48; m13 (tratamentos da oficina) → 49. Só remissão.

## Fora do escopo (e por quê)

| Fora | Por quê | Onde está |
|---|---|---|
| Identificação gemológica por instrumento, graduação, valor, mercado, procedência, laudo e divulgação | fronteira decidida pelo usuário | curso-gemologia |
| Lapidação | idem | curso-lapidacao |
| Petrologia sistemática (classificação IUGS de rochas, petrogênese de magmas) | o curso trata o mineral, não a rocha; o módulo 03 dá só o mínimo | curso-geologia 06-08 |
| Modelos de depósitos minerais, exploração, recursos | geologia econômica, não mineralogia | curso-geologia 21; curso-geologia-avancado 34, 42 |
| Mineralogia aplicada e industrial (cerâmica, cimento, vidro, agregados, rochas ornamentais) | escopo da GMG0203, fora do viés pedido | candidato a módulo futuro, se o usuário pedir |
| Geocronologia isotópica (métodos de datação) | geoquímica isotópica | curso-geologia-avancado 26-27 |
| Microscopia de minérios aprofundada | já existe em nível avançado | curso-geologia-avancado 36-37 |
| Teoria de grupos formal, mecânica quântica, teoria de bandas quantitativa, DFT | acima do nível de chegada | — |
| Mineralogia planetária além de meteoritos e minerais de impacto | cabe numa aula do módulo 43 | curso-geologia 24 |
| Competência de laboratório (operar microscópio, difratômetro, microssonda) | curso escrito: avalia leitura e interpretação de imagens, dados e espectros, nunca "saber operar" | — |

## Contrato de nível (proposto: `ensino-medio-sem-geologia-v1`, herdado dos cursos irmãos)

Proposto pelo planejador por coerência com o curso-geologia e o curso-gemologia; o usuário pode alterá-lo antes do módulo 01.

1. **LC-01 — Nenhum termo sem definição** na primeira aparição, em linguagem comum.
2. **LC-02 — Teto de ~1.600 palavras** de corpo por aula (régua de `palavras_corpo` do curso-lapidacao: de `## Conteúdo` ao fim do `## Recap relâmpago`). O que não cabe vira Parte 1 / Parte 2 — nunca é comprimido.
3. **LC-03 — Abertura padronizada:** "Vocabulário desta aula" (5 a 10 termos) e "Antes de começar, você precisa saber", com wikilink para aulas **deste** curso e menção **por nome** para outros cursos.
4. **LC-04 — Analogia antes do termo** — com cuidado: analogia que ensina modelo mental errado (ex.: átomos como bolas rígidas sem ressalva) é defeito.
5. **LC-05 — Ordem de grandeza, não precisão de laboratório.** Exceção: constantes e valores de referência tabelados (raios de Shannon, parâmetros de cela, índices de refração, ângulos de clivagem, temperaturas de transição) são objeto de estudo e vão com valor, faixa e fonte.
6. **LC-06 — Matemática reativada antes do uso.** Pontos críticos já mapeados: trigonometria (05, 14, 18), logaritmo e exponencial (22, 24, 28, 42), vetores (12, 18), regra da alavanca (23).
7. **LC-07 — "Erros comuns", "O que não concluir" e "Recap relâmpago" obrigatórios.**
8. **LC-08 — Controvérsia em uma frase**, declarada como pergunta aberta. Controvérsias já mapeadas: modelos de zoneamento oscilatório (26); critério epitaxial e singenesia em inclusões de diamante (27, 43); gênese de pegmatitos (38); estágios da evolução mineral (44); precursores amorfos na biomineralização (45).
9. **LC-09 — Degrau de inferência explícito** nos módulos 25-27, 37 e 50 (ver "Espinha didática").

Convenções estruturais herdadas: bloco **"Ao final você vai conseguir"** com o **ID completo** do objetivo (`mineralogia-m09-oa04`), nunca `OA-04`; rodapé em comentário HTML com `nivel`, `palavras_corpo`, `cobertura` e `alegacoes_auditaveis` em YAML; aulas de ≤30 min; módulos de 3 a 8 aulas.

## IDs e `claim_id`

```text
mineralogia-m<NN>-oa<NN>    objetivo de aprendizagem
mineralogia-m<NN>-a<NN>     aula
mineralogia-m<NN>-q<NN>     questão
mineralogia-m<NN>-fb<NNN>   flashcard Basic
mineralogia-m<NN>-fc<NNN>   flashcard Cloze
```

`claim_id` com **4 segmentos desde a primeira aula** (`^[A-Z]{2,4}-[A-Z0-9]+-[A-Z0-9]+-[0-9]{3}$`), como no curso-lapidacao, para não repetir a divergência herdada do curso-gemologia. Exemplos: `MIN-QTZ-MACLA-001`, `CRI-MILLER-ZONA-001`, `OPT-BECKE-REL-001`.

IDs **nunca são reciclados**. Os objetivos foram numerados no planejamento (244); se uma aula for dividida, o objetivo novo recebe o próximo ID livre do módulo.

## Pipeline de qualidade

Padrão do plugin, por módulo: **aulas → auditoria científica (audit-and-fix) → correção → revisão didática → questionário(s) → flashcards.**

**Gate:** nenhum questionário nem baralho de um módulo com achado 🔴 ou 🟠 em aberto na auditoria. Flashcards incluídos por padrão; o usuário dispensou flashcards no curso-lapidacao a partir do módulo 06, mas essa decisão **não** foi estendida a este curso — perguntar se quiser mudar.

Lição dos cursos irmãos (memória do usuário): subagentes de validação já fabricaram relatórios; a validação estrutural deve ser rodada diretamente pelos scripts do plugin e o resultado conferido.

## Preferências de ensino

- `.md` local é canônico (vault Obsidian). Publicar no Notion é passo à parte, pelo `publicador-notion`, quando o usuário pedir.
- Ilustração é essencial e deve ser pedida explicitamente pela aula em: operações de simetria e grupos pontuais (04), índices de Miller e projeção estereográfica (05), retículos de Bravais (06), poliedros e empacotamento (08), polimerização dos silicatos (11), maclas (12), carta de Michel-Lévy (15), indicatriz e figuras de interferência (16), lei de Bragg e esfera de Ewald (18), diagramas de fase (22-23), mecanismos de crescimento e zoneamento (25-26), estruturas das camadas dos filossilicatos (35).
- Números tabelados sempre com fonte e faixa.
- Nomes de espécie sempre como a lista IMA vigente; variedade e nome comercial marcados como tais.

## Base do currículo

- **Ementas do IGc-USP** (pasta `GradeCurricular/Geologia-USP`): GMG0106 Cristalografia Fundamental (estado cristalino, Steno e Haüy, simetria, grupos pontuais, projeção estereográfica, Weiss-Miller, Bravais, grupos espaciais, cristaloquímica, Pauling, defeitos, geminações, soluções sólidas, isomorfismo, polimorfismo, DRX); GMG0220 Mineralogia (sistemática por classes, métodos de caracterização incl. DRX, MEV e microssonda, mineralogia óptica com indicatriz uniaxial e biaxial; bibliografia Deer-Howie-Zussman, Klein & Dutrow, Nesse); optativas GMG0203 Mineralogia Aplicada e GMG0425 Técnicas Gemológicas.
- **Klein & Dutrow, _Manual of Mineral Science_, 23ª ed.** — 22 capítulos (sumário conferido no site da Wiley): propriedades, cristaloquímica, estruturas, composição, simetria externa, ordem interna, projeções, grupos pontuais e espaciais, **crescimento e defeitos, maclas, cor e magnetismo**, **estabilidade e diagramas de fase**, **processos pós-cristalização**, microscopia óptica, métodos analíticos e de imagem, sistemática por classe, **minerais-gema**, assembleias.
- **Nesse, _Introduction to Mineralogy_** — cristalografia, cristaloquímica, estrutura, **crescimento mineral**, propriedades, óptica, DRX, análise química, estratégias de estudo, silicatos por classe estrutural, não silicatos.
- **Putnis, _An Introduction to Mineral Sciences_** — periodicidade e simetria, anisotropia, difração e imagem, espectroscopia, estruturas, defeitos, energética, soluções sólidas, exsolução e ordem, cinética, transformações (espinha dos módulos 22-24).
- **Perkins, _Mineralogy_, 3ª ed.** — minerais por ambiente (ígneo, sedimentar, metamórfico, minério) antes da cristalografia formal; inspirou a área X, mas a ordem escolhida é a de Klein & Dutrow e Nesse (ver decisões).
- **Wenk & Bulakh, _Minerals: Their Constitution and Origin_, 2ª ed.** — minerais no contexto dos ambientes de formação.
- **Dyar & Gunter, _Mineralogy and Optical Mineralogy_** (MSA).
- **Deer, Howie & Zussman**, minerais formadores de rocha; **Nesse, _Introduction to Optical Mineralogy_**.
- **Normativo:** IMA-CNMNC (definição de mineral — Nickel, 1995; lista de minerais versionada; hierarquia de grupos; regras do constituinte e da valência dominantes — Hatert & Burke, 2008; nomenclaturas de supergrupos: granada, Grew et al., 2013; turmalina, Henry et al., 2011; anfibólio, Hawthorne et al., 2012; piroxênio, Morimoto, 1988). Classificação Nickel-Strunz e Dana; Mindat, RRUFF e Handbook of Mineralogy como referência de dados.
- **Insumo verificado:** Bruno et al. (2024), _Scientific Reports_ 14 (ver seção de insumos).

> As referências normativas de nomenclatura (Nickel 1995, Hatert & Burke 2008, Grew 2013, Henry 2011, Hawthorne 2012, Morimoto 1988, Shannon 1976, Droop 1987, Hazen 2008) foram citadas pelo planejador de memória de domínio como ponteiros de pesquisa; **cada uma precisa ser conferida na fonte pela aula que a usar**, e entra em `alegacoes_auditaveis`.

## Decisões (registro por data)

- **[2026-09-29]** Curso **completo e autossuficiente**; partida ensino médio sem geologia; chegada avançado; remissões só por nome.
- **[2026-09-29]** **Viés geocientífico geral**; gemologia no curso-gemologia; catalogação como gancho (módulo 50).
- **[2026-09-29]** **Trilha dupla** registrada fora do schema (tabela acima); regra de fechamento do núcleo verificada.
- **[2026-09-29]** **Espécies minerais (46-47) e mineralogia gemológica (48-49)** incluídas como aprofundamento, por ajuste de escopo do usuário; feldspatos e diamante sem monografia própria (ver justificativa).
- **[2026-09-29]** **Ordem de base: cristalografia → cristaloquímica → propriedades → óptica → difração e métodos → termodinâmica → crescimento e texturas → sistemática → gênese.** Segue Klein & Dutrow, Nesse e a sequência GMG0106 → GMG0220 da USP. Alternativa rejeitada: a ordem de Perkins (minerais por ambiente antes da cristalografia), que chega antes a algo "usável", mas obrigaria a reensinar estrutura e diagramas de fase dentro de cada ambiente. Compensação: o módulo 13 (identificação macroscópica) vem logo após a cristaloquímica, como primeiro ponto de uso prático.
- **[2026-09-29]** **Nomenclatura IMA (29) no núcleo e antes da sistemática**, não no fim como previa o escopo inicial: nomear granadas, turmalinas, anfibólios e piroxênios exige as regras do constituinte e da valência dominantes.
- **[2026-09-29]** **Termodinâmica (22-23) antes de crescimento e texturas (25-27)**: supersaturação, solvus e cristalização fracionada são pré-requisito de hábito, zoneamento e exsolução. A cinética formal (24) é aprofundamento; a nucleação qualitativa é ensinada no núcleo (25) para o núcleo não depender do 24.
- **[2026-09-29]** **Geotermobarometria (42) na área de gênese, não na de termodinâmica**, porque depende de granada, biotita e plagioclásio (sistemática) e do metamorfismo (40).
- **[2026-09-29]** **Polimorfismo em dois tempos:** estrutura no 10 (cristaloquímica), estabilidade P-T no 22 (termodinâmica).
- **[2026-09-29]** `claim_id` de 4 segmentos desde a primeira aula.
