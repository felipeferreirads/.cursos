# Auditoria científica — Módulo 37: Petrografia de minério

**Curso:** geologia-avancado
**Módulo:** 37 — `37-petrografia-de-minerio` (7 aulas; a06/a07 da divisão da antiga a06)
**Modo:** `audit-and-fix` · **Profundidade:** `full`
**Auditado em:** 2026-09-30 · **Passagens:** 1
**Backup do estado antes da auditoria:** `course-state.yaml.bak-20260930-pre-m37-audit` (idêntico byte a byte ao `course-state.yaml.bak-20260930-post-m37-redacao`; os hashes das 7 aulas no estado foram conferidos contra o disco antes de qualquer edição).
**Escopo:** as 7 aulas, o hub do módulo e os `claim_id` declarados na redação. **Contagem em disco: 72 claims** (a01 9, a02 10, a03 9, a04 12, a05 12, a06 12, a07 8; sem duplicata), e não 61 como dizia o encaminhamento. A auditoria criou 2 claims novos (`PET-M37-A01-BIBLIO-010`, `PET-M37-A02-EXSOLUCAO-011`), e o total passou a 74. Não existem questionário, baralho nem glossário do módulo.
**Fontes principais de verificação:** Craig & Vaughan (1994), *Ore Microscopy and Ore Petrography*, 2ª ed., caps. 7–10 e Apêndice 1, na edição de acesso aberto da MSA (minsocam.org, consultada 2026-09-30), lidos no texto integral; Einaudi, Hedenquist & Inan (2003), texto integral da versão de 17/02/2003 (pyrite.utah.edu); John et al. (2010), USGS SIR 2010-5070-B, texto integral; resumos e registros bibliográficos dos demais artigos (links na tabela de verificação).
**Veredito:** **Aprovado após correções.** Foram levantados 5 vermelhos, 13 laranjas, 0 amarelos, 4 azuis e 0 brancos. Todos foram tratados nas aulas; nada ficou em aberto.

---

## Resumo por severidade

| Severidade | Levantados | Corrigidos / tratados | Em aberto |
|---|---|---|---|
| 🔴 Erro | 5 | 5 | **0** |
| 🟠 Impreciso | 13 | 13 | **0** |
| 🟡 Desatualizado | 0 | — | **0** |
| 🔵 Sem fonte | 4 | 4 (2 com fonte nova, 1 generalizado, 1 removido) | 0 |
| ⚪ Controverso | 0 | — | 0 |
| **Total** | **22** | **22** | **0** |

Gate de qualidade: **liberado** para o questionário e os flashcards (0 vermelhos e 0 laranjas em aberto), com as restrições do fim deste relatório.

### Inversões de sentido procuradas

Checadas uma a uma as prioridades do encaminhamento:

- **Tampão pirita-pirrotita: SEM inversão.** FeS₂ ⇌ FeS + ½ S₂; a T fixa, fS₂ alta dá pirita; a fS₂ fixa, aquecer dá pirrotita (a curva sobe com T). Confere com Einaudi et al. (2003, eq. 2) e Barton & Skinner (1979).
- **Tampão MH e ordem QFM < NNO < MH: SEM inversão.**
- **Estado de sulfetação × rótulos epitermais: ERRO (🔴 1).** A aula dizia que os rótulos "alta" e "baixa sulfetação" usam "exatamente" a escala de estado de sulfetação. A própria fonte citada adverte o contrário: os termos "não são estritamente paralelos". Também faltava a intermediária sulfetação, que o Módulo 34 (Aula 05) já ensina.
- **Geobarômetro da esfalerita: IMPRECISO (🟠 3).** O teor de FeS da esfalerita com pirita e pirrotita quase não varia com T entre ~300 e ~550 °C e depende da pressão; a aula dizia "função de T e de P", e o exemplo dizia que ele poderia informar "T ou P".
- **Ordem de resistência à deformação: SEM inversão.** Galena < calcopirita ≈ pirrotita < esfalerita < pirita, arsenopirita, magnetita confere com Craig & Vaughan (§7.6: o limiar de resposta é função sobretudo da dureza; §10.10.1).
- **Pirita → pirrotita com o grau: SEM inversão.** Craig & Vaughan §10.10.1–2: nos graus moderados a altos, a pirita perde S e vira pirrotita; na retrogressão, a pirita volta a crescer como euédrica.
- **Zonamento supergênico: INVERSÃO NO PERFIL (🔴 6).** O sentido das frentes estava certo (de fora para dentro do grão; de cima para baixo no perfil), mas a tabela punha a zona "oxidada (chapéu-de-ferro)" com malaquita **acima** da zona "lixiviada". A capa lixiviada (o chapéu-de-ferro) é a de cima; a zona de minério oxidado fica abaixo dela, sobre o enriquecimento.
- **Escada de teor de Cu: INVERSÃO (🔴 17).** A covelita (CuS, ~66% Cu) estava no topo da escada da Aula 05, acima de calcocita (~80%) e digenita (~78%), o que também contradizia a Aula 02.
- **Veio de espaço aberto: EXCEÇÃO TROCADA (🔴 5).** O veio **sintaxial** cresce das paredes para o centro e **segue** a regra; a exceção é o **antitaxial**.
- **Martita (magnetita → hematita): SEM inversão de sentido**, mas "oxidação em baixa temperatura" generalizava demais (🟠 8).
- **Pentlandita em chamas × pirrotita: SEM inversão.** Craig & Vaughan (§9.3.2): a pentlandita exsolve da mss, e as chamas são as últimas (abaixo de ~100–200 °C) e ficam presas no hospedeiro; a calcopirita vem da iss (Naldrett, 2004). "Mais nova que o hospedeiro no sentido de formação" confere.
- **Dissolução-reprecipitação:** confere (Putnis, 2009; Craig & Vaughan §7.4 lista a dissolução e a reprecipitação entre os processos).
- **Ouro invisível: ERRO (🔴 22).** O MEV aparecia como técnica de detecção; pela definição de Cook & Chryssoulis (1990), o ouro invisível é justamente o que não se detecta nem ao microscópio óptico nem ao MEV.

### Consistência com os Módulos 34, 35 e 36

- **Módulo 36 (auditado):** três durezas + resistência à deformação como quarta propriedade (a03) — consistente; oxi-exsolução da ilmenita em magnetita com "a textura sozinha não prova" (a04, a01) — consistente; doença da calcopirita controversa (a05, a07) — consistente; relevo não é evidência de reação (a04, passo 4) — consistente; galena deformada por fileiras encurvadas, não por geminação (a03) — consistente. **Inconsistência corrigida:** a Aula 02 chamava a exsolução de textura "primária", e o Módulo 36 a trata como família própria (🟠 7). **Limite óptico:** a frase "o microscópio óptico só vê grãos maiores que poucos micrômetros" (a06) foi alinhada à restrição 15 do Módulo 36 (resolução de décimos de µm; identificação segura a partir de alguns µm).
- **Módulos 34 e 35 (HS/IS/LS):** a Aula 01 passou a nomear os três tipos e a remeter ao Módulo 34, Aula 05, que já define os tipos por fluido e alteração, com o nome derivado do estado de sulfetação.

### Padrão dominante

Três tipos de achado: (a) **inversões de ordem ou de posição** em tabelas e listas — perfil supergênico, escada de Cu, exceção do veio, SEM como detector de ouro invisível; (b) **fonte citada que não diz o que a aula atribui a ela** — "exatamente" contra a ressalva de Einaudi et al.; título errado do próprio Einaudi et al.; itabiritos do Quadrilátero atribuídos a Craig & Vaughan; série cristaloblástica atribuída a Stanton sem conferência possível; (c) **generalizações que a fonte restringe** — reequilíbrio de "sulfetos" (a pirita, a arsenopirita, a cromita e a esfalerita são refratárias), ângulo de 120° estendido a agregados de fases diferentes, saída de Cr da cromita, martita só de baixa temperatura, violarita como indicador de perfil oxidado próximo. Os exemplos brasileiros conferem em essência; dois foram precisados (Carajás, Rio das Velhas) e todos ganharam fonte.

---

## Achados

### 🔴 1. Rótulos epitermais dados como "exatamente" a escala de estado de sulfetação

**claim_id:** `PET-M37-A01-SULFETACAO-003`
**Tipo:** erro factual (contradiz a fonte citada)
**Onde:** Aula 01 · "O tampão pirita-pirrotita e o estado de sulfetação", tabela e parágrafo seguinte
**Está escrito:** "Os rótulos "alta" e "baixa sulfetação" dos depósitos epitermais usam exatamente essa escala, aplicada ao fluido (Einaudi et al., 2003)." / tabela: "Baixo | … calcopirita"; "Alto | pirita com enargita, covelita, bornita e digenita"
**Problema:** Einaudi et al. (2003) advertem, com essas palavras, que o termo estado de sulfetação "is not strictly parallel" aos termos HS e LS da classificação dos epitermais, embora as assembleias dominantes costumem concordar com eles; o estado de sulfetação varia dentro de um depósito e até numa amostra. O texto omitia a intermediária sulfetação (IS), que o Módulo 34 ensina. Na tabela, a calcopirita sozinha não indica estado baixo (é estável do baixo ao intermediário; o baixo é calcopirita **com pirrotita**), e a escala formal tem cinco níveis: o limite intermediário/alto é a reação calcopirita + S₂ → bornita + pirita, e covelita e digenita com pirita marcam o "muito alto".
**Correção proposta:** tabela com "calcopirita com pirrotita" no baixo, tetraedrita-tennantita no intermediário e "alto a muito alto" (pirita com bornita ou enargita; covelita e digenita no extremo), com a menção aos cinco níveis; parágrafo reescrito: os nomes HS, IS e LS vêm dessa escala e costumam concordar com as assembleias dominantes, mas os tipos também se definem por fluido e alteração, e os termos não são estritamente paralelos ao estado de sulfetação.
**Fonte:** Einaudi, Hedenquist & Inan 2003, SEG Spec. Publ. 10:285-313, texto integral (pyrite.utah.edu, consultado 2026-09-30), p. 5–6 (cinco níveis, reações 2–5, ressalva sobre HS/LS) e seção de epitermais (HS/IS/LS)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Módulo 34, Aula 05 (compatível; nada alterado).

### 🟠 2. Título errado da referência de Einaudi et al. (2003)

**claim_id:** `PET-M37-A01-BIBLIO-010` (criado pela auditoria)
**Tipo:** imprecisão bibliográfica
**Onde:** Fontes das Aulas 01, 05 e 07
**Está escrito:** "Einaudi, M. T., Hedenquist, J. W. & Inan, E. E. (2003), "Sulfidation state of hydrothermal fluids: the porphyry-epithermal transition and beyond", *Society of Economic Geologists Special Publication* 10, 285-313."
**Problema:** autores, ano, série e páginas conferem, mas o título do capítulo é outro: "Sulfidation state of fluids in active and extinct hydrothermal systems: transitions from porphyry to epithermal environments", no volume organizado por Simmons & Graham.
**Correção proposta:** título e volume corretos nas três listas de Fontes.
**Fonte:** Einaudi et al. 2003, folha de rosto do texto (pyrite.utah.edu); registro Semantic Scholar e SCIRP (consultados 2026-09-30)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aulas 05 e 07 (corrigidas).

### 🟠 3. Geobarômetro da esfalerita descrito como função de T e de P

**claim_id:** `PET-M37-A01-GEOTERMOMETROS-006`
**Tipo:** imprecisão
**Onde:** Aula 01 · "Geotermômetros e geobarômetros de assembleia", linha da esfalerita; Exemplo trabalhado, passo 4; recap
**Está escrito:** "teor de FeS da esfalerita, função de T e de P; usado como geobarômetro em minérios metamorfisados" / "seu teor de FeS poderia informar T ou P"
**Problema:** com a atividade de FeS tamponada por pirita e pirrotita hexagonal, o teor de FeS da esfalerita é **praticamente independente da temperatura entre ~300 e ~550 °C** e depende da pressão; é por isso um geobarômetro, não um geotermômetro. Craig & Vaughan recomendam ainda usar esfalerita inclusa em pirita e evitar a que toca pirrotita ou calcopirita, que perde FeS no resfriamento.
**Correção proposta:** "depende sobretudo da pressão e quase não varia com T entre ~300 e ~550 °C: é geobarômetro"; na coluna da petrografia, "de preferência esfalerita inclusa em pirita, longe de pirrotita e calcopirita"; passo 4: "poderia informar a pressão (não a temperatura)"; recap ajustado.
**Fonte:** Craig & Vaughan 1994, §8.4 (p. 192–193) e §10.10.1 (p. 307–308), MSA acesso aberto; Scott & Barnes 1971, *Econ. Geol.* 66:653-669 (registro e resumo consultados 2026-09-30)  ·  **Nível:** base de referência / revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 05 ("instrumento geobarométrico", correto, não alterado).

### 🟠 4. Reequilíbrio rápido atribuído a "sulfetos e óxidos" em geral

**claim_id:** `PET-M37-A01-REEQUILIBRIO-007`
**Tipo:** omissão que gera erro (generalização)
**Onde:** Aula 01 · "Equilíbrio e reequilíbrio", primeira frase; recap
**Está escrito:** "Sulfetos e óxidos de Fe-Ti **reequilibram-se com rapidez** durante o resfriamento"
**Problema:** Craig & Vaughan (§7.5) separam as fases refratárias, que costumam guardar composição e textura originais no resfriamento (magnetita, cromita, pirita, esfalerita, alguns arsenetos), das que se reequilibram (muitos sulfetos, sulfossais, metais nativos). A frase, como escrita, apaga essa diferença, e é justamente ela que faz a arsenopirita e a esfalerita inclusa em pirita servirem de instrumento (linhas seguintes da mesma aula).
**Correção proposta:** "Muitos sulfetos (pirrotita, sulfetos de Cu-Fe, sulfossais) e os pares de óxidos de Fe-Ti reequilibram-se com rapidez … As fases refratárias (pirita, arsenopirita, cromita e, em boa parte, a esfalerita) tendem a guardar composição e zonamento, e por isso são as preferidas para geotermômetros e geobarômetros." Recap ajustado.
**Fonte:** Craig & Vaughan 1994, §7.5 (p. 138) e §10.10.1 (p. 306), MSA acesso aberto (consultado 2026-09-30)  ·  **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** —

### 🔴 5. Veio sintaxial dado como exceção à regra parede-velha / centro-novo

**claim_id:** `PET-M37-A02-HIDROTERMAL-002`
**Tipo:** erro factual (inversão)
**Onde:** Aula 02 · "Texturas primárias", parágrafo "Hidrotermal"
**Está escrito:** "A regra tem exceção: veios de crescimento por abertura repetida (*crack-seal*) e de crescimento sintaxial mostram outra geometria."
**Problema:** no veio **sintaxial** os cristais crescem das paredes para o centro, e o material mais novo fica no centro: é exatamente a regra da aula. A exceção é o veio **antitaxial**, que cresce a partir de uma zona mediana em direção às paredes, com o material mais novo junto à encaixante. No *crack-seal*, a nova fratura pode abrir em vários pontos, e a ordem parede-centro não é garantida.
**Correção proposta:** "A regra vale para o crescimento das paredes para o centro (veio **sintaxial**) e tem exceções: no veio **antitaxial**, o material novo se acrescenta junto às paredes, e o mais velho fica no centro; em veios de abertura repetida (*crack-seal*), a nova fratura pode abrir em vários pontos, e as bandas não seguem a ordem simples parede-centro (Bons et al., 2012)." Acrescentar Bons et al. (2012) às Fontes.
**Fonte:** Bons, Elburg & Gomez-Rivas 2012, *J. Struct. Geol.* 43:33-62 (resumo e registro ADS/ScienceDirect, consultados 2026-09-30); Craig & Vaughan 1994, §7.3, Fig. 7.6 (crostificação das paredes para dentro)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** nenhum outro módulo menciona veios sintaxiais ou antitaxiais.

### 🔴 6. Perfil supergênico: zona oxidada posta acima da capa lixiviada

**claim_id:** `PET-M37-A02-SUPERGENICO-008`
**Tipo:** erro factual (inversão de posição no perfil)
**Onde:** Aula 02 · "Zonamento supergênico", tabela; Exemplo trabalhado, passo 1
**Está escrito:** "Oxidada (chapéu-de-ferro) | goethita e hematita, carbonatos e sulfatos de metais (malaquita, cerussita, anglesita)" na primeira linha e "Lixiviada | metais removidos; resíduo pobre" na segunda / "(a) é a zona oxidada"
**Problema:** o chapéu-de-ferro (*gossan*, capa lixiviada) é o topo do perfil: resíduo poroso de óxidos e hidróxidos de Fe (goethita, hematita, jarosita), de onde o cobre foi removido. A zona de minério oxidado (malaquita, azurita, crisocola, cuprita; cerussita e anglesita nos minérios de Pb) fica **abaixo** dela, acima do nível freático e sobre o enriquecimento. A tabela fundia o chapéu-de-ferro com o minério oxidado e punha a zona lixiviada embaixo. O sentido das frentes (de fora para dentro do grão; de cima para baixo no perfil) e o mecanismo estão corretos.
**Correção proposta:** linhas "Lixiviada (chapéu-de-ferro)" com óxidos e hidróxidos de Fe e metais removidos, e depois "Oxidada (minério oxidado)" com carbonatos, silicatos, óxidos e sulfatos de metais, acima do nível freático; exemplo: "(a) é a capa lixiviada (chapéu-de-ferro)". Acrescentar John et al. (2010) às Fontes.
**Fonte:** John et al. 2010, USGS SIR 2010-5070-B, "Supergene Ore Characteristics" (texto integral, consultado 2026-09-30): "the overlying porous rock from which hypogene copper minerals … were removed … is called leached capping", com o minério oxidado e o manto de calcocita subjacentes; Sillitoe 2005 citado ali  ·  **Nível:** base de referência (normativa de modelos de depósito)
**Confiança:** confirmado
**Também aparece em:** `PET-M37-A02-EXEMPLO-010` (passo 1, corrigido); hub e recap (sentido das frentes, corretos, não alterados).

### 🟠 7. Exsolução chamada de textura "primária"

**claim_id:** `PET-M37-A02-EXSOLUCAO-011` (criado pela auditoria)
**Tipo:** inconsistência interna / com o Módulo 36
**Onde:** Aula 02 · fim de "Texturas primárias"
**Está escrito:** "Uma quarta textura, a **exsolução**, é primária no sentido de formar-se no resfriamento"
**Problema:** Craig & Vaughan classificam a exsolução entre as texturas **secundárias de resfriamento** (§7.5), e o Módulo 36 (Aula 04, auditado) a trata como família própria, ao lado de crescimento, substituição e deformação. Chamar de "primária" a textura que se forma dentro de uma fase já cristalizada ensina o contrário.
**Correção proposta:** "A **exsolução** não entra nesta tabela: forma-se no resfriamento de uma fase já cristalizada e é uma família à parte (textura secundária de resfriamento em Craig & Vaughan, 1994); sua leitura está no Módulo 36 (Aula 04)."
**Fonte:** Craig & Vaughan 1994, §7.5 (título e texto); Módulo 36, Aula 04 (auditado 2026-09-29)  ·  **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** —

### 🟠 8. Martita restrita à "oxidação em baixa temperatura"

**claim_id:** `PET-M37-A02-EXEMPLOS-006`
**Tipo:** confusão de escopo
**Onde:** Aula 02 · "Substituição: como e onde", item Martita
**Está escrito:** "é oxidação em baixa temperatura (Ramdohr, 1980)"
**Problema:** a martitização é comum no intemperismo (Craig & Vaughan §7.8), mas também ocorre por oxidação hidrotermal e metamórfica: nos itabiritos do Quadrilátero Ferrífero, que a Aula 04 usa como exemplo, a martita é a primeira geração de hematita de uma sequência metamórfico-hidrotermal. A frase, como escrita, contradiz o exemplo da Aula 04. O sentido (magnetita → hematita, ao longo de {111}) está certo.
**Correção proposta:** "é oxidação posterior à magnetita, comum no intemperismo, mas também hidrotermal ou metamórfica, como nos itabiritos (Aula 04) (Ramdohr, 1980; Craig & Vaughan, 1994)".
**Fonte:** Craig & Vaughan 1994, §7.4.2 (hematita ao longo de (111)) e §7.8, Fig. 7.34; Rosière et al. 2008, *Rev. Econ. Geol.* 15:223-254 (registro e resumos consultados 2026-09-30)  ·  **Nível:** base de referência / revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 01 ("oxidação tardia", compatível); Aula 04 (ver 🔵 14).

### 🟠 9. Junções de ~120° estendidas a agregados de fases diferentes

**claim_id:** `PET-M37-A03-RECRISTALIZACAO-003`
**Tipo:** confusão de escopo
**Onde:** Aula 03 · "Recristalização"; Exemplo trabalhado (situação e passo 1); recap
**Está escrito:** "grãos poligonais, com **contatos retos** e **junções tríplices de ângulo próximo de 120°**" / exemplo: "agregado de pirrotita, calcopirita e esfalerita com contatos retos e junções de ~120°"
**Problema:** os ângulos tendem a 120° nas junções de agregados **monominerálicos**; nos poliminerálicos, o ângulo de equilíbrio depende do par (galena-esfalerita 103° e 134°; calcopirita-esfalerita 106–108°; pirrotita-esfalerita 107–108°, dados de Stanton citados por Craig & Vaughan), e o ângulo verdadeiro só sai da moda de muitas medidas, porque a seção corta os grãos ao acaso. O exemplo lê "~120°" justamente num agregado de três fases.
**Correção proposta:** "~120° em agregados de uma só fase; entre fases diferentes o ângulo depende do par (perto de 106–108° entre calcopirita e esfalerita), e só a moda de muitas medidas estima o ângulo verdadeiro (Stanton, 1972; Craig & Vaughan, 1994)"; no exemplo e no passo 1, "junções tríplices regulares"; recap "(~120° entre grãos da mesma fase)".
**Fonte:** Craig & Vaughan 1994, §7.2 e §7.7.1 (p. 153–154), MSA acesso aberto (consultado 2026-09-30)  ·  **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** `PET-M37-A03-EXEMPLO-009` (corrigido); Aula 07, tabela de força da evidência ("junção de 120°", genérico, não alterado).

### 🔵 10. "Série cristaloblástica" atribuída a Stanton (1972)

**claim_id:** `PET-M37-A03-IDIOMORFISMO-004`
**Tipo:** evidência insuficiente (atribuição)
**Onde:** Aula 03 · "A armadilha do idiomorfismo cristaloblástico"
**Está escrito:** "(a chamada série cristaloblástica; Stanton, 1972)"
**Problema:** o conteúdo confere com Craig & Vaughan: pirita, arsenopirita, magnetita e hematita crescem como porfiroblastos euédricos no metamorfismo, e calcopirita, pirrotita e esfalerita tendem a grãos anédricos equidimensionais; não há meio inequívoco de separar porfiroblasto de cristal euédrico precoce (§7.7.2, §10.10.1). Não foi possível conferir, em fonte acessível, a série e a ordem atribuídas a Stanton (1972). A hematita faltava na lista.
**Correção proposta:** trocar a citação por Craig & Vaughan (1994), acrescentar a hematita e manter Stanton nas Fontes (citado na mesma aula para os ângulos interfaciais, que Craig & Vaughan confirmam).
**Fonte:** Craig & Vaughan 1994, §7.7.2 (p. 154–155) e §10.10.1 (p. 305), MSA acesso aberto (consultado 2026-09-30)  ·  **Nível:** base de referência
**Confiança:** não verificado (atribuição a Stanton); confirmado (conteúdo)
**Também aparece em:** Aula 06 (arsenopirita euédrica, compatível); Aula 07 (força da evidência, compatível).

### 🟠 11. Bordas de ferritchromit: "Cr, Al e Mg saem"

**claim_id:** `PET-M37-A04-FERRICROMITA-007`
**Tipo:** imprecisão (mecanismo)
**Onde:** Aula 04 · "Sistema Cr-Fe-O", terceiro parágrafo
**Está escrito:** "o Cr, o Al e o Mg saem das bordas dos grãos e o Fe³⁺ entra: formam-se bordas de **ferritchromit** e, depois, de magnetita cromífera"
**Problema:** a alteração metamórfica da cromita troca **Mg por Fe²⁺** e remove **Al**, com entrada de Fe³⁺; o Cr fica relativamente retido, e a razão Cr/(Cr+Al) da borda sobe. Barnes (2000) registra que as proporções de Cr³⁺, Al³⁺ e Fe³⁺ mudam pouco até a fácies anfibolito inferior e que a substituição extensa por magnetita é da fácies anfibolito. "Ferritchromit" é termo de uso corrente, não uma espécie aprovada pela IMA.
**Correção proposta:** "as bordas perdem Mg (trocado por Fe²⁺) e Al e ganham Fe³⁺; o Cr fica relativamente retido, e a razão Cr/(Cr+Al) da borda sobe. Formam-se bordas de ferritchromit (termo de uso corrente, não uma espécie aprovada; também descrita como cromita férrica) e, nos graus mais altos, de magnetita cromífera".
**Fonte:** Barnes 2000, *J. Petrol.* 41:387-409 (resumo, Oxford Academic, consultado 2026-09-30); Evans & Frost 1975, *Geochim. Cosmochim. Acta* 39:959-972; Mindat, verbetes Ferritchromit e Ferrian Chromite (consultados 2026-09-30)  ·  **Nível:** revisada por pares / base de referência
**Confiança:** confirmado
**Também aparece em:** `PET-M37-A04-EXEMPLO-012` (fala só em "ferritchromit ou magnetita cromífera", compatível, não alterado).

### 🟠 12. Scheelita e wolframita incluídas sem ressalva no "grupo dos óxidos"

**claim_id:** `PET-M37-A04-WOLFRAMITA-009`
**Tipo:** imprecisão de classificação
**Onde:** Aula 04 · "Sistema Sn-W-O" e tabela "Resumo dos óxidos desta aula"
**Está escrito:** "Resumo dos óxidos desta aula:" (tabela com wolframita e scheelita)
**Problema:** a scheelita é um **tungstato** (Nickel-Strunz 7.GA.05). A wolframita é tungstato na classificação de Dana, mas fica entre os óxidos na de Nickel-Strunz (4.DB.30), porque o W está em octaedros de arestas compartilhadas e não em grupos tetraédricos WO₄. Só a cassiterita é óxido sem ambiguidade. O título da aula e o objetivo oa03 seguem o currículo ("sistema Sn-W-O") e não foram alterados.
**Correção proposta:** nota de classificação no fim do bloco de ocorrência e "Resumo das fases desta aula" no lugar de "Resumo dos óxidos desta aula".
**Fonte:** Mindat, scheelita (7.GA.05) e fórum "Tungstate vs tungsten oxide mineral classification"; ferberita, Strunz 4.DB.30 (Wikipedia, infobox) (consultados 2026-09-30)  ·  **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** hub e estado (objetivo oa03: "grupos dos óxidos (Fe-Ti-O, Cr-Fe-O, Sn-W-O)"; texto curricular, não alterado; ver restrições).

### 🟠 13. Anisotropia da cassiterita dada como fraca; ocorrências sem fonte

**claim_id:** `PET-M37-A04-CASSITERITA-008`
**Tipo:** imprecisão
**Onde:** Aula 04 · "Sistema Sn-W-O", item Cassiterita e frase das ocorrências brasileiras
**Está escrito:** "anisotropia fraca, com frequência mascarada pelas reflexões internas" / "cassiterita em granitos e aluviões de Rondônia e em Pitinga (AM)"
**Problema:** o Apêndice 1 de Craig & Vaughan dá anisotropia **nítida** (*distinct*), cinza, mascarada em óleo pelas reflexões internas, e birreflectância nítida. As ocorrências brasileiras conferem (Província Estanífera de Rondônia, com produção sobretudo aluvionar; Pitinga, maior produtora de Sn do país, com cassiterita disseminada no albita-granito do plúton Madeira e em greisens do Água Boa), mas estavam sem fonte.
**Correção proposta:** "anisotropia nítida, cinza, com frequência mascarada pelas reflexões internas, sobretudo em óleo"; ocorrências precisadas, com Bettencourt et al. (2016) nas Fontes.
**Fonte:** Craig & Vaughan 1994, Apêndice 1 (MSA, consultado 2026-09-30); Bettencourt et al. 2016, *J. South Am. Earth Sci.* 68:22-49 (registro e resumo consultados 2026-09-30)  ·  **Nível:** base de referência / revisada por pares
**Confiança:** confirmado
**Também aparece em:** tabela-resumo da aula (sem anisotropia; não alterada).

### 🔵 14. Itabiritos do Quadrilátero atribuídos a Craig & Vaughan

**claim_id:** `PET-M37-A04-HEMATITA-MARTITA-004`
**Tipo:** evidência insuficiente (fonte citada não trata do caso)
**Onde:** Aula 04 · item Martita
**Está escrito:** "Em minérios de ferro metamórficos, como os itabiritos do Quadrilátero Ferrífero, especularita e martita são texturas esperadas (Craig & Vaughan, 1994)."
**Problema:** Craig & Vaughan não tratam do Quadrilátero. O conteúdo confere na literatura regional: nos itabiritos e minérios de alto teor do Quadrilátero, a hematita aparece como martita, hematita granoblástica e especularita, e a sequência descrita vai de magnetita a martita, depois hematita granoblástica e por fim hematita tabular e especular.
**Correção proposta:** "martita, hematita granoblástica e especularita são texturas esperadas, e a martita é a geração mais antiga de hematita (Rosière et al., 2008)", com a referência nas Fontes.
**Fonte:** Rosière, Spier, Rios & Suckau 2008, *Rev. Econ. Geol.* 15:223-254 (registro GeoScienceWorld e resumos consultados 2026-09-30)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** —

### 🔵 15. Leucoxênio "de refletância mais alta que a da ilmenita fresca"

**claim_id:** `PET-M37-A04-MAGNETITA-ILMENITA-003`
**Tipo:** evidência insuficiente
**Onde:** Aula 04 · item Ilmenita
**Está escrito:** "Alterada, dá **leucoxênio**, agregado microcristalino de fases de TiO₂ (rutilo, anatásio) de refletância mais alta que a da ilmenita fresca."
**Problema:** a composição geral do leucoxênio confere; a comparação de refletância não foi encontrada em fonte acessível (é um agregado poroso e fino, de leitura dominada por reflexões internas).
**Correção proposta:** remover a comparação: "agregado microcristalino de fases de TiO₂ (rutilo, anatásio)".
**Fonte:** Craig & Vaughan 1994, §7.8 (leucoxênio como produto de alteração; sem valor de refletância)  ·  **Nível:** base de referência
**Confiança:** não verificado
**Também aparece em:** —

### 🔵 16. Scheelita no Seridó sem fonte

**claim_id:** `PET-M37-A04-SCHEELITA-010`
**Tipo:** evidência insuficiente (ocorrência sem fonte)
**Onde:** Aula 04 · frase das ocorrências brasileiras
**Está escrito:** "scheelita em skarns do Seridó (RN)"
**Problema:** confere (Faixa Seridó, Província Borborema; Brejuí é o principal depósito de scheelita da província e a maior reserva brasileira de W), mas estava sem fonte. As propriedades ópticas conferem com o Apêndice 1 (cinza-branca, refletância ~10%, semelhante à ganga em ar, reflexões internas brancas comuns; fluorescência azul em UV de onda curta).
**Correção proposta:** "scheelita em skarns do Seridó (RN), como Brejuí (Souza Neto et al., 2008)", com a referência nas Fontes.
**Fonte:** Souza Neto et al. 2008, *Miner. Deposita* 43:185-205 (registro e resumo consultados 2026-09-30); Craig & Vaughan 1994, Apêndice 1  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** —

### 🔴 17. Escada de "teor crescente de Cu" com a covelita no topo

**claim_id:** `PET-M37-A05-ESCADA-CU-001`
**Tipo:** erro factual (inversão de ordem) e inconsistência com a Aula 02
**Onde:** Aula 05 · "Sulfetos de cobre", tabela; recap, primeiro item
**Está escrito:** tabela na ordem calcopirita, bornita, calcocita, digenita, **covelita**, apresentada como "escada por teor crescente de Cu"; recap: "calcopirita amarela, bornita rosa-acastanhada, calcocita e digenita cinza-azuladas, covelita azul"
**Problema:** em massa, Cu ≈ 35% (calcopirita), 63% (bornita), 66% (covelita), 78% (digenita) e 80% (calcocita). A covelita (CuS) é a mais pobre em Cu entre os sulfetos simples de Cu, e o topo da escada é a calcocita. A Aula 02 dá a ordem certa (pirita e calcopirita, depois covelita, depois calcocita ou digenita), e as duas aulas se contradiziam.
**Correção proposta:** tabela reordenada (calcopirita, bornita, covelita, digenita, calcocita) com os teores aproximados na frase de abertura; recap: "calcopirita amarela, bornita rosa-acastanhada, covelita azul, digenita e calcocita cinza-azuladas".
**Fonte:** estequiometria das fórmulas da própria aula, que conferem com o Apêndice 1 de Craig & Vaughan 1994 (CuFeS₂, Cu₅FeS₄, CuS, Cu₉S₅, Cu₂S); cores e anisotropias da tabela conferem com o mesmo Apêndice  ·  **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** Aula 02 (ordem correta, não alterada).

### 🟠 18. IOCG de Carajás: "calcopirita e bornita com magnetita abundante" para Salobo e Sossego

**claim_id:** `PET-M37-A05-IOCG-CARAJAS-005`
**Tipo:** imprecisão (exemplo brasileiro)
**Onde:** Aula 05 · fim de "Sulfetos de cobre"
**Está escrito:** "Nos depósitos IOCG de Carajás (Salobo, Sossego), calcopirita e bornita associam-se a magnetita abundante."
**Problema:** o minério de Salobo é dominado por **bornita e calcocita** (com digenita), com calcopirita subordinada, em rochas ricas em magnetita; em Sossego predomina a **calcopirita**, com magnetita abundante em partes do depósito (corpos Sequeirinho-Pista-Baiano). A frase atribuía aos dois a mesma assembleia.
**Correção proposta:** "o minério de Salobo é dominado por bornita e calcocita, com digenita e calcopirita subordinada, em rochas ricas em magnetita (Melo et al., 2017), e o de Sossego, por calcopirita, com magnetita abundante em partes do depósito (Monteiro et al., 2008)", com as duas referências nas Fontes.
**Fonte:** Melo et al. 2017, *Miner. Deposita* 52:709-732; Monteiro et al. 2008, *Miner. Deposita* 43:129-159 (registros e resumos consultados 2026-09-30)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 07 ("calcopirita e bornita com magnetita é compatível com pórfiro ou IOCG", genérico, compatível, não alterado).

### 🟠 19. Fraturas da pentlandita atribuídas só à partição octaédrica

**claim_id:** `PET-M37-A06-PENTLANDITA-001`
**Tipo:** imprecisão (mecanismo)
**Onde:** Aula 06 · "Sulfetos de níquel", primeiro parágrafo
**Está escrito:** "com **fraturas poligonais** características, que marcam sua partição octaédrica"
**Problema:** Craig & Vaughan atribuem o fraturamento intenso da pentlandita à contração térmica, 2 a 10 vezes maior que a da pirrotita e da pirita que a envolvem. A partição octaédrica existe, mas não é a causa dada pela fonte da aula. Cor (creme-clara, mais clara que a pirrotita), isotropia e ausência de reflexões internas conferem.
**Correção proposta:** "com **fraturas** características, atribuídas à contração no resfriamento, bem maior que a da pirrotita, e guiadas em parte pela partição octaédrica (Craig & Vaughan, 1994)".
**Fonte:** Craig & Vaughan 1994, §7.5.5 (p. 145), §9.3.1 (p. 215) e Apêndice 1, MSA acesso aberto (consultado 2026-09-30)  ·  **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** recap e exemplo da Aula 06 ("fraturas poligonais" como descrição, compatível, não alterado).

### 🟠 20. Violarita "rosa-violácea" e "perfil oxidado próximo"

**claim_id:** `PET-M37-A06-VIOLARITA-003`
**Tipo:** imprecisão
**Onde:** Aula 06 · "Sulfetos de níquel" (parágrafo da violarita); Exemplo trabalhado (situação, passo 1); recap
**Está escrito:** "**Violarita** (FeNi₂S₄) é **rosa-violácea** e **isotrópica**, e é produto **supergênico** … Onde há violarita, o perfil oxidado deve estar próximo."
**Problema:** Craig & Vaughan descrevem a violarita como cinza-amarronzada com tinta violeta, mais escura que a pentlandita, isotrópica, e a secundária como porosa. A violarita é em geral supergênica, mas se forma abaixo da zona oxidada, na zona de transição, e há violarita hipogênica; "o perfil oxidado deve estar próximo" é mais do que a textura sustenta.
**Correção proposta:** cor corrigida no texto, no exemplo e no recap; "na maioria dos casos" supergênica; "sua presença sugere que a amostra passou pela alteração supergênica, sem dizer a que distância está o perfil oxidado".
**Fonte:** Craig & Vaughan 1994, §9.3.3 (p. 219–220), Fig. 9.8 e Apêndice 1, MSA acesso aberto (consultado 2026-09-30)  ·  **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** `PET-M37-A06-EXEMPLO-012` (corrigido).

### 🟠 21. "Quadrilátero Ferrífero e greenstone belt Rio das Velhas" como lugares distintos

**claim_id:** `PET-M37-A06-QF-AU-006`
**Tipo:** imprecisão (exemplo brasileiro)
**Onde:** Aula 06 · "Arsênio: arsenopirita e arsenetos", segundo parágrafo
**Está escrito:** "Minérios auríferos com arsenopirita e pirrotita em rochas metamorfisadas ocorrem no Quadrilátero Ferrífero e no *greenstone belt* Rio das Velhas."
**Problema:** o *greenstone belt* Rio das Velhas está **dentro** do Quadrilátero Ferrífero; o "e" sugere duas regiões. A mineralogia confere: pirita, arsenopirita e pirrotita são os principais sulfetos dos depósitos orogênicos do cinturão (Morro Velho, Cuiabá, Lamego, São Bento).
**Correção proposta:** "Minérios auríferos com pirita, arsenopirita e pirrotita em rochas metamorfisadas ocorrem no *greenstone belt* Rio das Velhas, no Quadrilátero Ferrífero, como em Morro Velho e Cuiabá (Lobato et al., 2001)", com a referência nas Fontes.
**Fonte:** Lobato, Ribeiro-Rodrigues & Vieira 2001, *Miner. Deposita* 36:249-277 (registro e resumo consultados 2026-09-30)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** —

### 🔴 22. MEV listado como técnica que detecta o ouro invisível

**claim_id:** `PET-M37-A06-OURO-INVISIVEL-009`
**Tipo:** erro factual (contradiz a definição da fonte citada)
**Onde:** Aula 06 · "Ouro visível e ouro invisível"; recap
**Está escrito:** "O microscópio óptico só vê grãos maiores que poucos micrômetros. O ouro pode estar também em solução sólida ou em nanopartículas dentro da pirita e da arsenopirita, o chamado **ouro invisível** (refratário), que não aparece na seção e é detectado por técnicas como SIMS, LA-ICP-MS e MEV (Cook & Chryssoulis, 1990)."
**Problema:** Cook & Chryssoulis (1990) definem o ouro invisível como o ouro na estrutura dos sulfetos e em inclusões menores que ~1000 Å (0,1 µm), **não detectáveis por microscopia óptica nem eletrônica de varredura**; eles o medem por SIMS. O MEV é, por definição, um dos métodos que **não** o veem; nanopartículas se veem ao microscópio eletrônico de transmissão. A primeira frase também destoava do Módulo 36 (restrição 15: a resolução óptica é de décimos de µm; o limite prático de identificação é maior).
**Correção proposta:** "O microscópio óptico só identifica com segurança grãos de alguns micrômetros ou mais (Módulo 36, Aula 04). O ouro pode estar também na estrutura da pirita e da arsenopirita ou em inclusões menores que ~0,1 µm, o chamado **ouro invisível**, que por definição não aparece nem ao microscópio óptico nem ao MEV; mede-se por microanálise de traços, como SIMS e LA-ICP-MS, e as nanopartículas se veem ao microscópio eletrônico de transmissão (Cook & Chryssoulis, 1990)." Recap: "…não aparece nem ao microscópio óptico nem ao MEV".
**Fonte:** Cook & Chryssoulis 1990, *Can. Mineral.* 28:1-16 (resumo e definição, SciSpace/Semantic Scholar, consultados 2026-09-30); Módulo 36, restrição 15 (auditado 2026-09-29)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** —

---

## Verificado e correto

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `PET-M37-A01-FUGACIDADE-001` | T, fO₂ e fS₂; fugacidade; assembleia restringe e não mede | Einaudi et al. 2003 (reações-tampão e índice relativo); Barton & Skinner 1979 | confirmado |
| `PET-M37-A01-PIRITA-PIRROTITA-002` | FeS₂ ⇌ FeS + ½S₂; fS₂ alta → pirita; aquecer → pirrotita; tampão | Einaudi et al. 2003, eq. 2 e Fig. 1 | confirmado — **sem inversão** |
| `PET-M37-A01-MH-004` | 4Fe₃O₄ + O₂ ⇌ 6Fe₂O₃; QFM < NNO < MH; martita tardia não registra fO₂ primária | Craig & Vaughan 1994, §7.5.4 (curvas tampão Ni-NiO, FMQ), §7.4.2; Buddington & Lindsley 1964 | confirmado |
| `PET-M37-A01-LEITURA-ASSEMBLEIA-005` | Leitura qualitativa po+mt / py+mt / py+hm | Barton & Skinner 1979; Craig & Vaughan 1994, cap. 8 | confirmado |
| `PET-M37-A01-RECONHECIMENTO-008` | Pares críticos pirita/pirrotita, magnetita/hematita, magnetita/ilmenita | Módulo 36 (auditado); Craig & Vaughan 1994, Apêndice 1 | confirmado |
| `PET-M37-A01-EXEMPLO-009` | Exemplo hipotético (passo 4 corrigido com 🟠 3) | lógica conferida | confirmado |
| `PET-M37-A02-MAGMATICA-001` | Euédrico cumulus, intersticial tardio, gotas de sulfeto imiscível | Craig & Vaughan 1994, §7.2 (líquidos Fe-S cristalizam depois dos silicatos; gotas redondas) e §9.3.2; Naldrett 2004; Barnes & Lightfoot 2005 | confirmado |
| `PET-M37-A02-SEDIMENTAR-003` | Framboides, nódulos, pseudomorfos de matéria orgânica; concordância não prova | Craig & Vaughan 1994, §7.4 (pseudomorfos de madeira e conchas), §7.9 | confirmado |
| `PET-M37-A02-MECANISMO-004` | Dissolução-reprecipitação acoplada; de fora para dentro | Putnis 2009, *Rev. Mineral. Geochem.* 70:87-124; Craig & Vaughan 1994, §7.4 e §7.4.1 | confirmado |
| `PET-M37-A02-GEOMETRIAS-005` | Coroa, fraturas, pseudomorfo, relictos em continuidade óptica, seletiva (atol) | Craig & Vaughan 1994, §7.4.1 e §7.4.3, Fig. 7.15 | confirmado |
| `PET-M37-A02-REGRAS-007` | Regras de idade relativa e inversão pela substituição | Craig & Vaughan 1994, §7.4.1 (substituição × preenchimento de fratura) | confirmado |
| `PET-M37-A02-ENRIQUECIMENTO-009` | Cu:S crescente (py/cp → cv → cc/dg); covelita e calcocita também hipogênicas | Craig & Vaughan 1994, §7.4.3, Fig. 7.14; Einaudi et al. 2003 (covelita hipogênica em HS e "muito alto") | confirmado |
| `PET-M37-A02-EXEMPLO-010` | Exemplo hipotético do furo (passo 1 corrigido com 🔴 6) | lógica conferida | confirmado |
| `PET-M37-A03-RESISTENCIA-001` | Ordem de ductilidade e quarta propriedade | Craig & Vaughan 1994, §7.6, §7.6.4 (pirita "rolada" de Sulitjelma), §10.10.1–2 (resistência ao cisalhamento cai com T) | confirmado — **sem inversão** |
| `PET-M37-A03-DEFORMACAO-002` | Cataclase, geminações em calcopirita, pirrotita e ilmenita; fileiras encurvadas na galena | Craig & Vaughan 1994, §7.6.1–7.6.4, §10.10.1; Módulo 36 | confirmado |
| `PET-M37-A03-SOMBRAS-005` | Sombra de pressão exige grão rígido preexistente | Craig & Vaughan 1994, §10.10.1 (fases dúcteis forçadas para áreas de baixa pressão) | confirmado |
| `PET-M37-A03-REMOBILIZACAO-006` | Remobilização mecânica ou por fluido; sinais heurísticos | Marshall & Gilligan 1987, *Ore Geol. Rev.* 2:87-131 (processos químico, mecânico e misto); Craig & Vaughan 1994, §7.4.1 (preenchimento × substituição de fratura) | confirmado |
| `PET-M37-A03-GRAU-007` | Pirita → pirrotita com o grau; retrogressão devolve pirita ou marcassita | Craig & Vaughan 1994, §10.10.1–2 (pirita volta a crescer euédrica), §7.5.3 (marcassita de baixa T ao longo de fraturas da pirrotita) | confirmado — **sem inversão** |
| `PET-M37-A03-FOLIACAO-008` | Relação com a foliação; concordância não prova anterioridade | Marshall & Gilligan 1987; Craig & Vaughan 1994, §10.10.2 | confirmado |
| `PET-M37-A03-EXEMPLO-009` | Exemplo hipotético (situação e passo 1 corrigidos com 🟠 9) | lógica conferida | confirmado |
| `PET-M37-A04-FETIO-SERIES-001` | Duas séries; oxi-exsolução da titanomagnetita | Craig & Vaughan 1994, §7.5.4, Fig. 7.17d; Buddington & Lindsley 1964 | confirmado |
| `PET-M37-A04-TITANOMAGNETITA-002` | Titanomagnetita vanadífera em acamadados | Módulo 33, Aula 08 (auditado) | confirmado |
| `PET-M37-A04-CROMITA-005` | Cromita cúbica, isotrópica, menos refletora que a magnetita; reflexões internas marrom-avermelhadas, ausentes nas ricas em Fe | Craig & Vaughan 1994, Apêndice 1 | confirmado |
| `PET-M37-A04-CROMITITO-006` | Estratiformes e podiformes; Ipueira-Medrado como maior depósito brasileiro | Módulo 33, Aula 08 (auditado) | confirmado |
| `PET-M37-A04-PAR-CASSITERITA-ESFALERITA-011` | Cassiterita × esfalerita | Craig & Vaughan 1994, Apêndice 1 (esfalerita isotrópica, VHN 138–160; cassiterita dura) | confirmado |
| `PET-M37-A04-EXEMPLO-012` | Exemplo hipotético da rocha ultramáfica | lógica conferida; Barnes 2000 | confirmado |
| `PET-M37-A05-CALCOPIRITA-002` | Principal sulfeto primário de Cu; geminações | Craig & Vaughan 1994, §7.6.1, Apêndice 1 | confirmado |
| `PET-M37-A05-BORNITA-TARNISH-003` | Bornita escurece ao ar; lamelas de calcopirita | Craig & Vaughan 1994, Apêndice 1, Fig. 7.17a | confirmado |
| `PET-M37-A05-FS2-004` | Bornita, digenita e covelita mais sulfetadas que cp+po; hipogênicas ou supergênicas | Einaudi et al. 2003 (cp+S₂→bn+py como limite intermediário/alto; py+dg+cv no "muito alto") | confirmado |
| `PET-M37-A05-SULFOSSAIS-006` | Sulfossais de Cu mal distinguíveis só por óptica | Craig & Vaughan 1994, Apêndice 1 | confirmado |
| `PET-M37-A05-GALENA-007` | Galena branca, isotrópica, cavidades triangulares, dúctil, oxida a anglesita e cerussita | Craig & Vaughan 1994, Fig. 7.11c, §10.10.1; Módulo 36 | confirmado |
| `PET-M37-A05-ESFALERITA-008` | Esfalerita e teor de Fe; coloforme de crescimento rápido | Craig & Vaughan 1994, §7.3 (Roedder 1968; cor escura só indica Fe de modo inconsistente abaixo de 5%) | confirmado |
| `PET-M37-A05-DOENCA-009` | Doença da calcopirita controversa | Barton & Bethke 1987; Craig & Vaughan 1994, §7.5.2; Módulo 36 | confirmado (⚪ declarado na redação, nenhum lado escolhido) |
| `PET-M37-A05-FES-BAROMETRO-010` | FeS da esfalerita como geobarômetro | Craig & Vaughan 1994, §8.4, §10.10.1 | confirmado |
| `PET-M37-A05-ZONAMENTO-011` | Tendência Cu, Zn, Pb como hipótese | Craig & Vaughan 1994, §9.10 (zonamento de Cu, Zn, As e S comum em veios) | provável |
| `PET-M37-A05-EXEMPLO-012` | Exemplo hipotético do veio | lógica conferida | confirmado |
| `PET-M37-A06-EXSOLUCAO-MSS-002` | Pentlandita exsolvida da mss; calcopirita da iss; chamas mais novas que o hospedeiro | Craig & Vaughan 1994, §9.3.2 (chamas abaixo de ~100–200 °C, presas na mss); Naldrett 2004; Barnes & Lightfoot 2005 | confirmado — **sem inversão** |
| `PET-M37-A06-NI-BRASIL-004` | Ni sulfetado em komatiítos e intrusões; laterita majoritária | Módulo 33, Aula 08 (auditado) | confirmado |
| `PET-M37-A06-ARSENOPIRITA-005` | Arsenopirita branca, forte anisotropia, losango; hospedeiro de Au; geotermômetro | Craig & Vaughan 1994, Apêndice 1, §8.4, Fig. 8.19; Kretschmar & Scott 1976, *Can. Mineral.* 14:364-386 | confirmado |
| `PET-M37-A06-ARSENETOS-007` | Löllingita, niquelina, cobaltita, skutterudita | Craig & Vaughan 1994, Apêndice 1 | confirmado |
| `PET-M37-A06-OURO-008` | Ouro nativo e posição textural | Craig & Vaughan 1994, Apêndice 1; Módulo 36 | confirmado |
| `PET-M37-A06-ELECTRUM-PRATA-010` | Electrum mais pálido com Ag; rubis de prata | Craig & Vaughan 1994, §7.8 (electrum > 20% Ag) e Apêndice 1 | confirmado |
| `PET-M37-A06-PGM-011` | PGM pequenos, em sulfetos magmáticos e cromititos; espécie por MEV-EDS | Craig & Vaughan 1994, §9.3.1 (grãos pequenos, raros na seção) | confirmado |
| `PET-M37-A06-EXEMPLO-012` | Exemplo hipotético (cor da violarita corrigida com 🟠 20) | lógica conferida | confirmado |
| `PET-M37-A07-COLECAO-001` | Paragênese composta de coleção representativa | Craig & Vaughan 1994, cap. 8 | confirmado |
| `PET-M37-A07-GERACOES-002` | Ordens opostas = gerações ou remobilização | Craig & Vaughan 1994, §7.3 (duas gerações de esfalerita, Fig. 7.3b); Marshall & Gilligan 1987 | confirmado |
| `PET-M37-A07-HIERARQUIA-003` | Força da evidência (heurística declarada) | síntese didática coerente com Craig & Vaughan 1994, §7.4 e §7.7.2 | confirmado |
| `PET-M37-A07-DIAGRAMA-004` | Convenção do diagrama paragenético | Craig & Vaughan 1994, cap. 8 (diagramas em barras) | confirmado |
| `PET-M37-A07-CONDICOES-ESTAGIO-005` | Tampão só no mesmo estágio | Einaudi et al. 2003; Barton & Skinner 1979 | confirmado |
| `PET-M37-A07-TIPO-DEPOSITO-006` | Paragênese restringe e não classifica | Módulos 34 e 35 (auditados) | confirmado |
| `PET-M37-A07-EXEMPLO-007` | Exemplo hipotético das três seções | lógica conferida | confirmado |
| `PET-M37-A07-RECAP-MODULO-008` | Pendências em aberto (doença da calcopirita, origem das exsoluções) | Barton & Bethke 1987; Módulo 36 | confirmado (⚪ declarado, nenhum lado escolhido) |

**Nota sobre as referências.** Conferem em autor, ano, periódico, volume e páginas: Barton & Skinner (1979, cap. em Barnes ed., 2ª ed., Wiley); Buddington & Lindsley (1964, *J. Petrol.* 5:310-357); Lindsley & Spencer (1982, *Eos* 63:471, resumo); Scott & Barnes (1971, *Econ. Geol.* 66:653-669); Kretschmar & Scott (1976, *Can. Mineral.* 14:364-386; Craig & Vaughan a citam com o ano de 1978 na lista, mas 1976 na legenda da Fig. 8.19; o volume 14 é de 1976); Putnis (2009, *RiMG* 70:87-124); Naldrett (2004, Springer); Barnes & Lightfoot (2005, *Econ. Geol. 100th Anniv. Vol.*, 179-213); Evans & Frost (1975, *GCA* 39:959-972); Barnes (2000, *J. Petrol.* 41:387-409); Marshall & Gilligan (1987, *Ore Geol. Rev.* 2:87-131); Cook & Chryssoulis (1990, *Can. Mineral.* 28:1-16); Barton & Bethke (1987); Stanton (1972, McGraw-Hill). Einaudi et al. (2003) tinha o título errado (🟠 2). Ramdohr (1980), Uytenbogaardt & Burke (1971), Pracejus (2015) e Marshall, Anglin & Mumin (2004) não foram relidos no texto; nenhuma correção depende só deles. **Novas nas Fontes:** Bons et al. 2012 e John et al. 2010 (a02); Rosière et al. 2008, Bettencourt et al. 2016 e Souza Neto et al. 2008 (a04); Melo et al. 2017 e Monteiro et al. 2008 (a05); Lobato et al. 2001 (a06).

## Observações não factuais

- O título da Aula 04, o objetivo oa03 (hub e estado) e o nome do sistema "Sn-W-O" seguem o currículo e não foram alterados; a aula agora avisa que scheelita e wolframita não são óxidos na classificação de Dana.
- A Aula 01 ficou um pouco mais densa (tabela de sulfetação e parágrafo sobre as fases refratárias). A extensão fica para a revisão didática.

---

## Correções aplicadas

**Aplicadas em:** 2026-09-30

| # | claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|---|
| 1 | `PET-M37-A01-SULFETACAO-003` | 🔴 | Corrigido | aula-01 |
| 2 | `PET-M37-A01-BIBLIO-010` | 🟠 | Corrigido | aula-01, aula-05, aula-07 |
| 3 | `PET-M37-A01-GEOTERMOMETROS-006` | 🟠 | Corrigido | aula-01 |
| 4 | `PET-M37-A01-REEQUILIBRIO-007` | 🟠 | Corrigido | aula-01 |
| 5 | `PET-M37-A02-HIDROTERMAL-002` | 🔴 | Corrigido | aula-02 |
| 6 | `PET-M37-A02-SUPERGENICO-008` | 🔴 | Corrigido | aula-02 |
| 7 | `PET-M37-A02-EXSOLUCAO-011` | 🟠 | Corrigido | aula-02 |
| 8 | `PET-M37-A02-EXEMPLOS-006` | 🟠 | Corrigido | aula-02 |
| 9 | `PET-M37-A03-RECRISTALIZACAO-003` | 🟠 | Corrigido | aula-03 |
| 10 | `PET-M37-A03-IDIOMORFISMO-004` | 🔵 | Corrigido com ressalva (citação trocada por fonte conferida) | aula-03 |
| 11 | `PET-M37-A04-FERRICROMITA-007` | 🟠 | Corrigido | aula-04 |
| 12 | `PET-M37-A04-WOLFRAMITA-009` | 🟠 | Corrigido | aula-04 |
| 13 | `PET-M37-A04-CASSITERITA-008` | 🟠 | Corrigido | aula-04 |
| 14 | `PET-M37-A04-HEMATITA-MARTITA-004` | 🔵 | Corrigido (fonte nova) | aula-04 |
| 15 | `PET-M37-A04-MAGNETITA-ILMENITA-003` | 🔵 | Corrigido com ressalva (comparação removida) | aula-04 |
| 16 | `PET-M37-A04-SCHEELITA-010` | 🔵 | Corrigido (fonte nova) | aula-04 |
| 17 | `PET-M37-A05-ESCADA-CU-001` | 🔴 | Corrigido | aula-05 |
| 18 | `PET-M37-A05-IOCG-CARAJAS-005` | 🟠 | Corrigido | aula-05 |
| 19 | `PET-M37-A06-PENTLANDITA-001` | 🟠 | Corrigido | aula-06 |
| 20 | `PET-M37-A06-VIOLARITA-003` | 🟠 | Corrigido | aula-06 |
| 21 | `PET-M37-A06-QF-AU-006` | 🟠 | Corrigido | aula-06 |
| 22 | `PET-M37-A06-OURO-INVISIVEL-009` | 🔴 | Corrigido | aula-06 |

**Propagação:** nenhuma externa. O módulo não tem questionário, baralho nem glossário (a auditoria correu antes deles), e não há card no Anki a corrigir. Busca em todas as aulas do curso fora do Módulo 37 por veio sintaxial/antitaxial/*crack-seal*, chapéu-de-ferro/*gossan*/capa lixiviada, escada de Cu, ouro invisível, ferritchromit e estado de sulfetação: a única ocorrência relacionada é o Módulo 34, Aula 05 (HS/IS/LS definidos por fluido e alteração, com o nome derivado do estado de sulfetação), compatível com a correção 🔴 1. Nada alterado fora do Módulo 37.

**Pendências:** nenhuma.

## Restrições para o questionário e os flashcards

1. **Estado de sulfetação:** escala da assembleia e do fluido, com cinco níveis formais (muito baixo a muito alto). Baixo = pirrotita, arsenopirita, esfalerita rica em Fe, calcopirita **com pirrotita**; intermediário = pirita com calcopirita, tetraedrita-tennantita; alto = pirita com bornita ou enargita; muito alto = covelita e digenita com pirita. **Não cobrar** "HS/LS usam exatamente essa escala"; os tipos epitermais HS, IS e LS têm nome derivado dela, mas não são estritamente paralelos a ela. Não cobrar calcopirita sozinha como indicador de estado baixo.
2. **Tampões:** fS₂ alta → pirita, aquecer → pirrotita (não inverter); QFM < NNO < MH na mesma T; hematita em película ou martita não registra a fO₂ primária.
3. **Esfalerita com pirita e pirrotita = geobarômetro** (FeS depende da pressão; quase independente de T entre ~300 e ~550 °C). **Não cobrar como geotermômetro.** Magnetita-ilmenita = T e fO₂; arsenopirita = T com fS₂ tamponada.
4. **Reequilíbrio:** muitos sulfetos e os pares de Fe-Ti reequilibram rápido; pirita, arsenopirita, cromita e, em boa parte, a esfalerita são refratárias. Não cobrar "todos os sulfetos reequilibram".
5. **Veios:** sintaxial = das paredes para o centro (mais novo no centro, segue a regra); **antitaxial** = mais novo junto às paredes (exceção); *crack-seal* não garante a ordem. **Não inverter.**
6. **Perfil supergênico, de cima para baixo:** capa lixiviada (chapéu-de-ferro: óxidos e hidróxidos de Fe, metais removidos) → zona oxidada (malaquita, azurita, crisocola, cuprita; cerussita, anglesita) → nível freático → enriquecimento (calcocita, covelita, digenita) → primária. Frente de fora para dentro no grão e de cima para baixo no perfil. **Não pôr a zona oxidada acima da lixiviada.**
7. **Exsolução** não é textura primária: é família própria (secundária de resfriamento em Craig & Vaughan).
8. **Martita:** hematita nova sobre magnetita, ao longo de {111}; sentido magnetita → hematita; comum no intemperismo, mas também hidrotermal e metamórfica (itabiritos). Não cobrar "martita = sempre baixa temperatura".
9. **Junções de ~120°:** em agregados de uma só fase; entre fases diferentes o ângulo depende do par. Indicam equilíbrio textural, não ordem. Não cobrar valores de ângulo entre pares.
10. **Idiomorfismo cristaloblástico:** pirita, arsenopirita, magnetita e hematita euédricas em minério metamorfisado não são necessariamente precoces. Não cobrar a "série de Stanton" nem uma ordem fina da série.
11. **Ordem de ductilidade:** galena > calcopirita ≈ pirrotita > esfalerita > pirita, arsenopirita, magnetita (sem ordem entre estas três). Não cobrar a ordem entre calcopirita e pirrotita.
12. **Cromita:** borda mais clara = alteração (perda de Mg e Al, ganho de Fe³⁺, Cr relativamente retido), não zonamento magmático. Não cobrar "o Cr sai da borda"; não cobrar ferritchromit como espécie IMA.
13. **Classificação:** cassiterita é óxido; scheelita é tungstato; wolframita é óxido na Nickel-Strunz e tungstato na Dana. Não cobrar scheelita como "óxido".
14. **Cassiterita:** anisotropia nítida mascarada pelas reflexões internas; relevo forte; geminação em joelho. Não cobrar "anisotropia fraca".
15. **Escada de Cu (% Cu em massa):** calcopirita ~35 < bornita ~63 < covelita ~66 < digenita ~78 < calcocita ~80. **Não pôr a covelita no topo.** Números só como ordem de grandeza.
16. **Carajás:** Salobo = bornita e calcocita (com digenita) em rochas ricas em magnetita; Sossego = calcopirita dominante. Não cobrar "calcopirita e bornita com magnetita" para os dois.
17. **Pentlandita:** creme-clara, isotrópica, fraturada (contração térmica); chamas na pirrotita são exsolução e **mais novas** que o hospedeiro; a regra de inclusão não se aplica.
18. **Violarita:** cinza-amarronzada com tinta violeta, mais escura que a pentlandita, isotrópica; em geral supergênica. Não cobrar "rosa-violácea" nem "perfil oxidado próximo".
19. **Quadrilátero Ferrífero:** o *greenstone belt* Rio das Velhas está dentro dele; ouro com pirita, arsenopirita e pirrotita.
20. **Ouro invisível:** na estrutura do sulfeto ou em inclusões < ~0,1 µm; não aparece nem ao óptico nem ao **MEV**; SIMS e LA-ICP-MS medem, MET vê nanopartículas. **Não cobrar o MEV como detector.** O limite prático de identificação óptica é de alguns µm (resolução de décimos de µm; Módulo 36, restrição 15).
21. **Doença da calcopirita** e origem de exsoluções e oxi-exsoluções: só pelas frases-síntese, sem escolher lado (herdado do Módulo 36).
22. Não cobrar números dos exemplos hipotéticos nem dados de produção ou reserva dos exemplos brasileiros.
