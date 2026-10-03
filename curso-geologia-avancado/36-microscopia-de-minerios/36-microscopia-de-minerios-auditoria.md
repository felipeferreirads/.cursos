# Auditoria científica — Módulo 36: Microscopia de minérios

**Curso:** geologia-avancado
**Módulo:** 36 — `36-microscopia-de-minerios` (4 aulas, como no currículo)
**Modo:** `audit-and-fix` · **Profundidade:** `full`
**Auditado em:** 2026-09-29 · **Passagens:** 1
**Backup do estado antes da auditoria:** `course-state.yaml.bak-20260929-pre-m36-audit` (idêntico byte a byte ao `course-state.yaml.bak-20260929-post-m36-redacao` e ao estado no início desta passagem; hashes das 4 aulas no estado conferidos contra o disco antes de qualquer edição).
**Escopo:** as 4 aulas, o hub do módulo e os 33 `claim_id` declarados na redação (a01 8, a02 9, a03 7, a04 9; sem duplicata). Não existem questionário, baralho nem glossário do módulo.
**Fonte principal de verificação:** Craig & Vaughan (1994), *Ore Microscopy and Ore Petrography*, 2ª ed., capítulos 1–8 e Apêndice 1, na edição de acesso aberto da Mineralogical Society of America (minsocam.org / msaweb.org, consultada 2026-09-29), lidos no texto integral; Barton & Bethke (1987), *Am. Mineral.* 72:451-467, texto integral (minsocam.org, consultado 2026-09-29); relatório da IMA-COM (2007).
**Veredito:** **Aprovado após correções.** Foram levantados 0 vermelhos, 15 laranjas, 1 amarelo, 1 azul e 0 brancos. Todos foram tratados nas aulas; nada ficou em aberto.

---

## Resumo por severidade

| Severidade | Levantados | Corrigidos / tratados | Em aberto |
|---|---|---|---|
| 🔴 Erro | 0 | — | **0** |
| 🟠 Impreciso | 15 | 15 | **0** |
| 🟡 Desatualizado | 1 | 1 (nome antigo mantido como referência) | **0** |
| 🔵 Sem fonte | 1 | 1 (generalizado para o que as compilações têm em comum) | 0 |
| ⚪ Controverso | 0 | — | 0 |
| **Total** | **17** | **17** | **0** |

Gate de qualidade: **liberado** para o questionário e os flashcards (0 vermelhos e 0 laranjas em aberto), com as restrições do fim deste relatório.

### Inversões de sentido procuradas

Checadas uma a uma as prioridades do encaminhamento:

- **Pseudo-linha de Becke (linha de Kalb): SEM inversão.** Craig & Vaughan (1994, §3.3.1) dão o procedimento literal: focalizar o contato, **baixar a platina (ou subir o tubo), aumentando a distância entre amostra e objetiva**, e a linha de luz se move **para o mineral mais mole**; a desfocalização no sentido oposto põe a linha no mais duro. É exatamente o que a Aula 02 diz, e o exemplo trabalhado (linha indo para a calcopirita ao baixar a platina) é coerente. Só o registro de fonte dos metadados, que dizia "derivado da geometria", foi trocado pela citação.
- **Dureza de polimento: inversão parcial dependente da fonte (🟠 6).** A aula punha **ouro < galena**; o Apêndice 1 de Craig & Vaughan dá para o ouro "PH > galena", embora a microdureza Vickers do ouro (53–58) seja um pouco menor que a da galena (59–65). Também **calcopirita ≈ esfalerita** foi precisado para calcopirita < esfalerita (Apêndice 1: esfalerita "PH > chalcopyrite"). Nenhuma inversão grosseira (pirita, hematita, magnetita e ilmenita estão no lugar certo).
- **Refletância: sem inversão de ordem,** mas a tabela era internamente inconsistente (🟠 4): a esfalerita (~17%) estava numa classe "muito baixa" separada, com número dentro da faixa da classe "baixa" (~15–30%), e a ilmenita (16,4–19,2% a 546 nm) se sobrepõe à esfalerita (16,6%).
- **Birreflectância × anisotropia × reflexões internas:** conceitos corretos e bem separados; uma intensidade trocada (hematita tem birreflectância **moderada**, não fraca; 🟠 9) e um exemplo que contradizia a própria aula (🟠 12: hematita descrita como cinza-amarronzada e de refletância igual à da magnetita).
- **Seção basal uniaxial:** correta (Craig & Vaughan §3.2.4 e §4.3.1).
- **Anisotropia anômala da pirita:** o fenômeno é real, mas as causas foram dadas como estabelecidas; Craig & Vaughan dizem que ocorrem "por razões que continuam obscuras" (🟠 11).
- **Doença da calcopirita:** o debate estava mal enquadrado (🟠 16). A exsolução não é mais uma alternativa viva para a maioria dos casos (a esfalerita só dissolve Cu apreciável acima de ~500 °C); o debate é substituição × crescimento conjunto.
- **Exsolução × oxi-exsolução:** o "exemplo clássico de exsolução" da Aula 04 (ilmenita em magnetita) é justamente o caso atribuído sobretudo à **oxi-exsolução** (🟠 14).
- **Caminho óptico:** ordem correta; a vantagem do vidro plano estava errada (🟠 1: é o prisma e o vidro plano que perturbam a polarização, não o contrário).
- **Escala de Talmage:** confundida com a dureza de polimento (🟠 7). Talmage (1925) é **dureza ao risco**.

### Padrão dominante

Nenhum erro grave e **nenhuma inversão no ponto de maior risco** (linha de Kalb). O que apareceu foi de três tipos: (a) **fusão de conceitos vizinhos** — Talmage (risco) com dureza de polimento; exsolução com oxi-exsolução; debate da doença da calcopirita reduzido a "exsolução × substituição"; (b) **valores de tabela e exemplos que não conversam** com o resto da aula — tabela de refletância, exemplo magnetita/hematita, exemplo pirrotita/calcopirita, galena com "linhas ortogonais"; (c) **certezas onde a fonte registra incerteza ou variação** — causas da anisotropia anômala, resolução óptica, intensidades de birreflectância, tintas de rotação da ilmenita. Toda a bibliografia citada confere (edições, editoras, anos; Barton & Bethke com título, volume e páginas corretos).

---

## Achados

### 🟠 1. Vidro plano dado como "melhor para polarização"

**claim_id:** `MIC-M36-A01-CAMINHO-002`
**Tipo:** imprecisão (vantagem trocada)
**Onde:** Aula 01 · "O caminho óptico", tabela, linha do iluminador vertical; e passo 5 de "Ajuste da iluminação"
**Está escrito:** "pode ser **vidro plano** (iluminação mais uniforme e melhor para polarização) ou **prisma** (imagem mais brilhante, mas usa só parte da abertura)"
**Problema:** Craig & Vaughan (§1.2.5) descrevem três refletores. O vidro plano a 45° é o único com incidência de fato vertical e abertura total, e é o "adequado ou superior para a rotina"; mas **perde luz** (~19% chega à ocular) e **gira levemente a polarização**, de modo que um isotrópico entre nicóis cruzados não fica perfeitamente negro. É o **refletor de Smith** que reduz essa rotação. O prisma dá até ~50% da luz, mas ilumina por metade da abertura, com incidência oblíqua. "Melhor para polarização" não se sustenta; e o passo 5 ("escura de forma estável") precisa da ressalva de que um resíduo uniforme é normal.
**Correção proposta:** vidro plano = incidência vertical, abertura total, preferido na rotina, com perda de luz e leve rotação da polarização; refletor de Smith = menos rotação; prisma = mais brilho, metade da abertura, incidência oblíqua. No passo 5: resíduo de luz uniforme é normal; o critério é não mudar ao girar.
**Fonte:** Craig & Vaughan 1994, §1.2.5 e §4.3.1 (MSA acesso aberto, consultado 2026-09-29)  ·  **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** —

### 🟠 2. Seção delgada polida descrita como "polida dos dois lados"

**claim_id:** `MIC-M36-A01-PREPARACAO-005`
**Tipo:** imprecisão (definição)
**Onde:** Aula 01 · "Preparação da seção polida", passo 2
**Está escrito:** "Uma **seção polida delgada** é uma lâmina polida dos dois lados que permite luz transmitida e refletida sobre a mesma área."
**Problema:** a seção delgada polida comum é uma lâmina delgada sem lamínula cuja **face superior** é polida. A seção **duplamente polida** (*doubly polished*) é outro tipo, usado para ver o interior de minerais translúcidos (esfalerita, cassiterita, cinábrio) sem o espalhamento da face inferior rugosa.
**Correção proposta:** "Uma **seção delgada polida** é uma lâmina delgada sem lamínula, com a face superior polida, que permite luz transmitida e refletida sobre a mesma área; a versão **polida dos dois lados** serve para ver o interior de minerais translúcidos, como a esfalerita."
**Fonte:** Craig & Vaughan 1994, §2.5 (consultado 2026-09-29)  ·  **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** —

### 🟡 3. "Comissão de Microscopia de Minérios" — nome antigo da IMA-COM

**claim_id:** `MIC-M36-A02-COM-002`
**Tipo:** desatualização (nomenclatura de instituição)
**Onde:** Aula 02 · "Refletância: o que é e do que depende", terceiro parágrafo
**Está escrito:** "a Comissão de Microscopia de Minérios (COM) da IMA padronizou quatro (470, 546, 589 e 650 nm) e uma escala de padrões para medição em microespectrofotômetro."
**Problema:** os quatro comprimentos de onda **conferem**, assim como a recomendação de 546 nm quando se mede um só. A comissão, criada em 1962, chama-se hoje **Commission on Ore Mineralogy** (COM); "Commission on Ore Microscopy" é o nome antigo (ainda no *Quantitative Data File* de Criddle & Stanley, 1986). Os padrões adotados pela COM são de refletância conhecida: vidro negro (~4,5%), SiC (~20%) e WTiC (~50%) a 546 nm; "escala de padrões" era vago.
**Correção proposta:** "a Comissão de Mineralogia de Minérios da IMA (COM, antes Comissão de Microscopia de Minérios) recomenda medir em quatro (470, 546, 589 e 650 nm; se for um só, 546 nm) e adotou padrões de refletância conhecida (vidro negro, carbeto de silício e carbeto de tungstênio-titânio) para a medição com microfotômetro."
**Fonte:** Craig & Vaughan 1994, §5.2.3; IMA-COM, relatório 2007 (mineralogy-ima.org, consultado 2026-09-29)  ·  **Nível:** normativa
**Confiança:** confirmado
**Também aparece em:** —

### 🟠 4. Tabela de refletância internamente inconsistente (esfalerita × ilmenita)

**claim_id:** `MIC-M36-A02-ORDEM-003`
**Tipo:** inconsistência interna (valores)
**Onde:** Aula 02 · tabela de ordens de grandeza, frase "Guarde a ordem" e recap
**Está escrito:** "| **Baixa** | hematita, ilmenita, magnetita | ~15% a ~30% |" / "| **Muito baixa** | esfalerita | cerca de 17% a 18% |" / "magnetita ≈ ilmenita > esfalerita"
**Problema:** a esfalerita (~17%) cai dentro da faixa da classe "baixa" e é posta numa classe "muito baixa" separada. Pelo Apêndice 1 de Craig & Vaughan (546 nm, ar): hematita 26,4–30,0; magnetita 19,9; **ilmenita 16,4–19,2**; **esfalerita 16,6**. Ilmenita e esfalerita se sobrepõem; só a magnetita fica claramente acima. A ordem geral (ouro > pirita > calcopirita ≈ galena > pirrotita > hematita > magnetita) confere (ouro 77,0; pirita 51,7; calcopirita 44,6–45,0; galena 42,9; pirrotita ~34–40).
**Correção proposta:** classe "baixa" com os números por mineral (hematita ~26–30, magnetita ~20, ilmenita ~16–19) e esfalerita "~16–17%, na faixa da ilmenita"; ordem "magnetita ≥ ilmenita ≈ esfalerita", com a nota de que as separa a anisotropia e as reflexões internas.
**Fonte:** Craig & Vaughan 1994, Apêndice 1 e §3.4.3 (magnetita ~20, galena ~43, pirita ~55) (consultado 2026-09-29)  ·  **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** recap da Aula 02 (corrigido).

### 🟠 5. Clivagem da galena "em duas direções ortogonais" como regra

**claim_id:** `MIC-M36-A02-HABITO-005`
**Tipo:** omissão que gera erro
**Onde:** Aula 02 · "Hábito e clivagem", item da galena; exemplo trabalhado (situação e passo 3)
**Está escrito:** "com **clivagem cúbica perfeita** que, na seção, aparece como linhas em duas direções ortogonais e como cavidades triangulares de arrancamento" / "C é branco, com linhas ortogonais de clivagem e cavidades triangulares"
**Problema:** os traços de clivagem só são ortogonais num corte paralelo a uma face do cubo. As cavidades triangulares, diagnósticas, aparecem em fileiras onde o corte intercepta as três clivagens, e dependem da orientação e do polimento. Um mesmo grão com "linhas ortogonais **e** cavidades triangulares" é um caso particular, não o padrão.
**Correção proposta:** "aparece sobretudo como fileiras de cavidades triangulares de arrancamento, onde o corte intercepta as três clivagens (traços ortogonais só num corte paralelo a uma face do cubo)"; no exemplo, "fileiras de cavidades triangulares".
**Fonte:** Craig & Vaughan 1994, §3.4.2 e Fig. 3.5a (consultado 2026-09-29)  ·  **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** exemplo da Aula 02 (corrigido). Aula 01 ("cavidades triangulares, pela clivagem cúbica") compatível, não alterada.

### 🟠 6. Ordem de dureza de polimento: ouro × galena e calcopirita × esfalerita

**claim_id:** `MIC-M36-A02-DUREZA-006`
**Tipo:** imprecisão (inversão parcial dependente da fonte)
**Onde:** Aula 02 · "Relevo, borda e dureza de polimento", segundo parágrafo
**Está escrito:** "**ouro < galena < calcopirita ≈ esfalerita < pirrotita < ilmenita ≈ magnetita < hematita < pirita**"
**Problema:** Apêndice 1 de Craig & Vaughan: ouro "PH > galena, PH < tetraedrita, pirita, calcopirita" (VHN 53–58, contra 59–65 da galena); calcopirita "PH > galena, PH < esfalerita"; magnetita "PH > pirrotita, PH < ilmenita, hematita, pirita"; ilmenita "PH > magnetita, PH < hematita". Ouro e galena ficam praticamente juntos, com posição trocada conforme o critério (polimento ou Vickers); a esfalerita fica acima da calcopirita. A ordem ensinada não pode dar "ouro < galena" como fato.
**Correção proposta:** "**galena ≈ ouro < calcopirita < esfalerita ≲ pirrotita < magnetita ≲ ilmenita < hematita < pirita**", com a nota de que entre minerais de dureza próxima a posição muda com o método (o ouro tem Vickers um pouco menor que a galena, mas Craig & Vaughan o põem ligeiramente acima em polimento).
**Fonte:** Craig & Vaughan 1994, Apêndice 1 (PH e VHN) e cap. 6 (consultado 2026-09-29)  ·  **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** —

### 🟠 7. Escala de Talmage descrita como escala de dureza de polimento

**claim_id:** `MIC-M36-A02-TALMAGE-008`
**Tipo:** confusão de escopo
**Onde:** Aula 02 · "Relevo, borda e dureza de polimento", terceiro parágrafo; recap
**Está escrito:** "A **escala de Talmage** é o esquema clássico para registrar a dureza de polimento como classes ordinais, usando minerais de referência e a comparação de grãos vizinhos pelo relevo, pela pseudo-linha de Becke e pelo comportamento a riscos."
**Problema:** Craig & Vaughan distinguem três durezas em minério: de polimento, **ao risco** e de microindentação, "não inteiramente equivalentes". Talmage (1925) é o método de **dureza ao risco**: arrastar uma ponta sobre a superfície sob carga conhecida. Relevo e linha de Kalb medem a dureza de **polimento**, não Talmage. Ambos os métodos foram superados pela microdureza Vickers. Nenhuma das classes de Talmage está na aula, o que está certo, pois não foi possível conferir a lista de minerais de referência em fonte acessível.
**Correção proposta:** reescrever: Talmage = dureza ao risco, com ponta sob carga, em classes ordinais com minerais de referência; distinta da dureza de polimento lida pelo relevo e pela pseudo-linha; ambas superadas pela Vickers; na rotina, a comparação ao risco se faz pela profundidade de um mesmo risco que atravessa dois grãos, com a cautela de riscos antigos no mineral duro. Acrescentar Talmage (1925) às Fontes.
**Fonte:** Craig & Vaughan 1994, §3.3 e §6.1; Talmage, S. B. (1925), *Econ. Geol.* 20:535-553 (referência conferida em Craig & Vaughan) (consultado 2026-09-29)  ·  **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** recap da Aula 02 (corrigido); objetivo oa02 do hub e do estado cita "escala de Talmage" como tema, sem definição — compatível, não alterado.

### 🟠 8. Exemplo da Aula 02 sugere que a anisotropia separa pirrotita de calcopirita "isotrópica"

**claim_id:** `MIC-M36-A02-EXEMPLO-009`
**Tipo:** omissão que gera erro
**Onde:** Aula 02 · exemplo trabalhado, passo 5
**Está escrito:** "Por exemplo, pirrotita também poderia ser B: ela tem tinta rosada e é anisotrópica, o que a Aula 03 resolve."
**Problema:** a calcopirita também é anisotrópica (fracamente; Apêndice 1: "Weak, but distinct"). Como está, o aluno lê "anisotrópica = pirrotita, isotrópica = calcopirita". A diferença é a **intensidade** (pirrotita muito forte, calcopirita fraca), além da cor e da refletância um pouco menor da pirrotita.
**Correção proposta:** "ela tem tinta rosada, refletância um pouco menor e é **fortemente** anisotrópica, enquanto a calcopirita é só **fracamente** anisotrópica; a Aula 03 mostra como ver essa diferença."
**Fonte:** Craig & Vaughan 1994, Apêndice 1 (calcopirita e pirrotita) (consultado 2026-09-29)  ·  **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** —

### 🟠 9. Birreflectância da hematita dada como fraca

**claim_id:** `MIC-M36-A03-BIRREFLECTANCIA-002`
**Tipo:** imprecisão (intensidade)
**Onde:** Aula 03 · "Birreflectância e pleocroísmo de refletância", segundo item
**Está escrito:** "moderada em pirrotita e fraca em hematita, ilmenita e arsenopirita (Craig & Vaughan, 1994)"
**Problema:** a própria fonte citada (§3.2.3) põe a hematita entre as de birreflectância **moderada** (com marcassita, nicolita, cubanita, pirrotita) e ilmenita, enargita e arsenopirita entre as fracas. O Apêndice 1 dá a ilmenita como "distinta", o que mostra que as intensidades variam entre compilações.
**Correção proposta:** "moderada em pirrotita e hematita, e fraca em ilmenita e arsenopirita (Craig & Vaughan, 1994; as intensidades variam entre compilações)".
**Fonte:** Craig & Vaughan 1994, §3.2.3 e Tabela 3.2 (consultado 2026-09-29)  ·  **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** —

### 🔵 10. Tintas de rotação da ilmenita ("marrom a azul-acinzentado")

**claim_id:** `MIC-M36-A03-ROTACAO-003`
**Tipo:** evidência insuficiente (divergência entre compilações)
**Onde:** Aula 03 · "Anisotropia (analisador cruzado)", terceiro parágrafo; exemplo trabalhado, passo 1
**Está escrito:** "ilmenita, marrom a azul-acinzentado" / "mostra tintas marrom-azuladas"
**Problema:** o Apêndice 1 de Craig & Vaughan dá para a ilmenita anisotropia forte em "cinza-esverdeado a cinza-amarronzado". Não foi possível conferir, em fonte acessível, a tinta "azul-acinzentada". As demais tintas (pirrotita, hematita, covelita) e as intensidades (calcopirita fraca; arsenopirita, pirrotita e grafita fortes) conferem.
**Correção proposta:** generalizar para "ilmenita, tons de cinza, de esverdeado a amarronzado (as tintas descritas variam entre compilações)"; no exemplo, "tintas acinzentadas, entre esverdeado e amarronzado".
**Fonte:** Craig & Vaughan 1994, Apêndice 1 (ilmenita) e §3.2.4 (as cores de anisotropia dependem do cruzamento exato e do microscópio) (consultado 2026-09-29)  ·  **Nível:** base de referência
**Confiança:** não verificado (a tinta azulada); generalizado
**Também aparece em:** exemplo da Aula 03 (ajustado junto com o achado 12).

### 🟠 11. Causas da anisotropia anômala da pirita dadas como estabelecidas

**claim_id:** `MIC-M36-A03-CAUTELAS-004`
**Tipo:** certeza indevida
**Onde:** Aula 03 · "Três cuidados que evitam erro", item 2
**Está escrito:** "Alguns minerais cúbicos, como a pirita, podem exibir anisotropia fraca por deformação, zonamento químico ou substituições"
**Problema:** o fenômeno confere (Apêndice 1: pirita "Often weakly anisotropic, blue-green to orange-red"; magnetita "slight anomalous anisotropism"), mas Craig & Vaughan (§3.2.4, nota 2) dizem que ocorre "por razões que continuam obscuras". A aula dava as causas como fato. Os mesmos autores alertam que riscos finos de polimento imitam anisotropia.
**Correção proposta:** "exibem com frequência anisotropia fraca, por causas não bem esclarecidas (deformação, zonamento químico e efeitos da superfície polida foram propostos); riscos finos de polimento também imitam anisotropia."
**Fonte:** Craig & Vaughan 1994, §3.2.4 e nota 2; Apêndice 1 (pirita, magnetita) (consultado 2026-09-29)  ·  **Nível:** base de referência
**Confiança:** confirmado (quanto à incerteza das causas)
**Também aparece em:** recap da Aula 03 ("pirita pode ter anisotropia anômala") — compatível, não alterado.

### 🟠 12. Exemplo da Aula 03 conclui hematita a partir de uma fase igual à magnetita

**claim_id:** `MIC-M36-A03-EXEMPLO-007`
**Tipo:** inconsistência interna
**Onde:** Aula 03 · exemplo trabalhado (situação, passos 3 e 5)
**Está escrito:** "Duas fases cinza-amarronzadas lado a lado, de refletância baixa e parecida." ... "**Hipótese.** X é magnetita e Y é hematita"
**Problema:** a Aula 02 ensina que a hematita é **branca-acinzentada com tinta azulada** e de refletância claramente maior que a da magnetita (26–30% contra ~20%). Uma fase cinza-amarronzada de refletância igual à da magnetita não pode terminar como hematita sem contradizer a aula anterior; o que o enunciado descreve é o par magnetita–ilmenita.
**Correção proposta:** manter o enunciado; no passo 3, usar a hematita como hipótese a **excluir** (seria visivelmente mais clara, azulada, com reflexões internas vermelho-sangue possíveis; Y não mostra nada disso); hipótese final: X magnetita, Y ilmenita, compatível e não confirmada.
**Fonte:** Craig & Vaughan 1994, Apêndice 1 (hematita, magnetita, ilmenita) (consultado 2026-09-29)  ·  **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** —

### 🟠 13. "Paragênese": uso duplo do termo não registrado

**claim_id:** `MIC-M36-A04-PARAGENESE-001`
**Tipo:** omissão que gera erro (terminologia)
**Onde:** Aula 04 · "Assembleia, paragênese e sequência"
**Está escrito:** "**Paragênese**: subconjunto da assembleia de minerais que se formaram no mesmo evento ou processo." ... "(Craig & Vaughan, 1994)"
**Problema:** a definição corresponde ao uso europeu. A fonte citada usa "paragenesis" **só** no sentido de **ordem de formação** e registra que o uso europeu é o de associação característica (cap. 8, nota 1). Sem a ressalva, o aluno que ler Craig & Vaughan, a referência central do módulo, vai encontrar "paragenesis" com outro sentido.
**Correção proposta:** acrescentar: "Atenção ao termo: esta é a acepção corrente na literatura europeia. Na literatura norte-americana de minério, inclusive em Craig & Vaughan (1994), *paragenesis* significa a própria sequência de formação."
**Fonte:** Craig & Vaughan 1994, §8.1 e nota 1 (consultado 2026-09-29)  ·  **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** —

### 🟠 14. Ilmenita em magnetita como "exemplo clássico" de exsolução

**claim_id:** `MIC-M36-A04-EXSOLUCAO-003`
**Tipo:** confusão de escopo
**Onde:** Aula 04 · "Quatro famílias de textura", item 2; "Exsolução ou substituição?", segundo parágrafo; Aula 02 · "Hábito e clivagem", item da ilmenita
**Está escrito:** "O exemplo clássico são as **lamelas de ilmenita em magnetita**" / "lamelas de ilmenita em magnetita podem vir de exsolução ou de **oxidação** de titanomagnetita (oxi-exsolução)" / Aula 02: "comum como lamelas de exsolução em magnetita"
**Problema:** Craig & Vaughan (§7.5.4) registram que as lamelas de ilmenita em magnetita costumam ocorrer **em volume maior que o limite de solubilidade** e as explicam por **oxidação** do componente ulvoespinélio no resfriamento (oxi-exsolução; Lindsley, 1976; Buddington & Lindsley, 1964). Os exemplos de exsolução verdadeira do mesmo livro são ulvoespinélio em magnetita, hematita–ilmenita, pentlandita em pirrotita, calcopirita–bornita. A aula escolheu como "exemplo clássico" de exsolução justamente o caso atribuído sobretudo a outro processo, e a Aula 02 repetiu o rótulo.
**Correção proposta:** trocar o exemplo clássico por pentlandita em pirrotita, hematita–ilmenita, calcopirita–bornita e ulvoespinélio em magnetita; reescrever o parágrafo da ilmenita em magnetita dizendo que é atribuída sobretudo à oxi-exsolução e que a geometria não prova o processo; na Aula 02, "lamelas em magnetita, em geral por oxi-exsolução (Aula 04)". Acrescentar Buddington & Lindsley (1964) e Lindsley (1976) às Fontes da Aula 04.
**Fonte:** Craig & Vaughan 1994, §7.5.1 e §7.5.4, Fig. 7.17d; Lindsley 1976, MSA Short Course Notes 3:L61-L88; Buddington & Lindsley 1964, *J. Petrol.* 5:310-357 (consultado 2026-09-29)  ·  **Nível:** base de referência / revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 02 (corrigido).

### 🟠 15. Galena com "geminações de deformação"

**claim_id:** `MIC-M36-A04-DEFORMACAO-005`
**Tipo:** imprecisão
**Onde:** Aula 04 · "Quatro famílias de textura", item 4
**Está escrito:** "A galena e a calcopirita mostram **geminações de deformação** e, em minérios metamorfisados, recristalização com contatos em junções poligonais."
**Problema:** Craig & Vaughan (§7.6.1–7.6.2) citam geminação de deformação em pirrotita, ilmenita, calcopirita e hematita; na galena, a deformação se registra caracteristicamente no **encurvamento das fileiras de cavidades triangulares** de clivagem. O resto do item (pirita frágil e fraturada; calcopirita, galena e pirrotita fluindo para as fraturas) confere.
**Correção proposta:** "A calcopirita, a pirrotita e a ilmenita desenvolvem **geminações de deformação**; a galena registra a deformação sobretudo no **encurvamento das fileiras de cavidades triangulares**. Em minérios metamorfisados, os sulfetos moles recristalizam com contatos em junções poligonais."
**Fonte:** Craig & Vaughan 1994, §7.6.1, §7.6.2, Figs. 7.20 e 7.22 (consultado 2026-09-29)  ·  **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** —

### 🟠 16. Doença da calcopirita: debate enquadrado como "exsolução × substituição"

**claim_id:** `MIC-M36-A04-DOENCA-006`
**Tipo:** omissão que gera erro (controvérsia mal enquadrada)
**Onde:** Aula 04 · "Exsolução ou substituição?", segundo parágrafo; recap
**Está escrito:** "foram por muito tempo lidos como exsolução; Barton & Bethke (1987) propuseram que resultam da **substituição** da esfalerita por fluido, e o tema segue **debatido**."
**Problema:** a citação confere (título, volume, páginas). Mas, como escrito, o aluno entende que a exsolução continua sendo uma das posições em debate. Não é: experimentos mostram que a esfalerita só dissolve calcopirita em quantidade apreciável acima de ~500 °C, e a textura ocorre em minérios formados a 100–300 °C (Craig & Vaughan §7.5.2). Barton & Bethke atribuem as três texturas comuns ("watermelon", "dusting", "bimodal") à substituição, registram um **paradoxo não resolvido** (a substituição exigiria difusão extensa em estado sólido) e admitem exsolução só em casos especiais (as "bead chains" de Creede). Craig & Vaughan leem o trabalho como "crescimento epitaxial durante a formação da esfalerita **ou** substituição". O debate vivo é substituição × crescimento conjunto, não exsolução × substituição.
**Correção proposta:** reescrever com as três peças: exsolução explica poucos casos (limite de ~500 °C); substituição por fluido cuprífero para as texturas comuns (Barton & Bethke), com o paradoxo da difusão; crescimento conjunto (epitaxial) como alternativa em parte dos casos; mecanismo por depósito ainda debatido. Ajustar o recap.
**Fonte:** Barton & Bethke 1987, *Am. Mineral.* 72:451-467, resumo e texto (minsocam.org, consultado 2026-09-29); Craig & Vaughan 1994, §7.5.2  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** recap da Aula 04 (corrigido); recap do módulo ("exsolução versus substituição em algumas texturas fica em debate") compatível, não alterado.

### 🟠 17. "Fases menores que cerca de 1 µm estão abaixo da resolução óptica"

**claim_id:** `MIC-M36-A04-APLICABILIDADE-007`
**Tipo:** imprecisão (valor)
**Onde:** Aula 04 · "O que a microscopia de opacos faz e o que não faz", Restrições, segundo item
**Está escrito:** "Fases menores que cerca de 1 µm estão abaixo da resolução óptica."
**Problema:** o limite de resolução de Abbe (≈ 0,61 λ/AN) fica em alguns décimos de micrômetro com objetivas de imersão (~0,25 µm para AN 1,3 a 546 nm). Um grão de 1 µm é resolvido; o que ele não permite é a leitura segura de cor, anisotropia e dureza. O ponto didático (grãos muito finos não se identificam) está certo; o número atribuído à resolução não.
**Correção proposta:** "Fases de poucos micrômetros ou menos são difíceis de identificar: a resolução óptica fica em alguns décimos de micrômetro, mas cor, anisotropia e dureza só se leem com segurança em grãos bem maiores."
**Fonte:** critério de resolução de Abbe, d ≈ 0,61 λ/AN (óptica de microscópio, manual padrão); não há número de resolução em Craig & Vaughan para conferir, e a aula não cita um  ·  **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** —

---

## Verificado e correto

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `MIC-M36-A01-OPACOS-001` | Opacos só por luz refletida; esfalerita, hematita fina, cassiterita e cuprita translúcidas | Craig & Vaughan 1994, §2.5 (esfalerita, cassiterita, cinábrio... transmitem luz) e Tabela 3.3 | confirmado |
| `MIC-M36-A01-ILUMINACAO-003` | Köhler com o diafragma de campo; abertura = contraste × resolução; mesmas condições para comparar; cor depende da lâmpada | Óptica de Köhler padrão (diafragma de campo = área iluminada; de abertura = ângulo do cone); Craig & Vaughan 1994, §1.2.4 (temperatura de cor da lâmpada muda as cores). Nota: o §1.2.4 de Craig & Vaughan descreve os papéis dos dois diafragmas de forma diferente da terminologia de Köhler; a aula segue a terminologia padrão e não foi alterada | confirmado |
| `MIC-M36-A01-IMERSAO-004` | Óleo nD ~1,515; objetivas de luz refletida sem lamínula; óleo reduz R, reduz espalhamento e realça cor e anisotropia fraca; ar e óleo registrados à parte | Craig & Vaughan 1994, §1.2.3 (óleo ~1,515; objetivas de luz transmitida corrigidas para lamínula de 0,17 mm) e §5.2.3 (óleo Cargille DF aceito pela COM) | confirmado |
| `MIC-M36-A01-ARTEFATOS-006` | Riscos, relevo, arrancamento (cavidades triangulares da galena), contaminação, embaçamento da bornita | Craig & Vaughan 1994, §2 e §3.3.2 (riscos imitam anisotropia) | confirmado |
| `MIC-M36-A01-PRECAUCOES-007` | Não tocar, focar afastando, nivelar, óleo mínimo; poeira tóxica | Craig & Vaughan 1994, §5.2.4 (erros de nivelamento); boas práticas | confirmado |
| `MIC-M36-A01-EXEMPLO-008` | Exemplo hipotético de avaliação de seção | — (lógica conferida: pirita VHN ≫ galena e calcopirita) | confirmado |
| `MIC-M36-A02-REFLETANCIA-001` | Fórmula de Fresnel com k; R cai em óleo | Craig & Vaughan 1994, cap. 4 | confirmado |
| `MIC-M36-A02-COR-004` | Cores em ar dos nove minerais; contraste simultâneo | Craig & Vaughan 1994, Apêndice 1 | confirmado |
| `MIC-M36-A02-BECKE-007` | Linha de Kalb vai para o **mais mole** ao **afastar** a objetiva (baixar a platina); calibrar em par conhecido | Craig & Vaughan 1994, §3.3.1 (texto literal do procedimento, Fig. 3.3); Oxford Dictionary of Earth Sciences (encyclopedia.com) | confirmado — **sem inversão** |
| `MIC-M36-A03-ISOANISO-001` | Cúbico isotrópico; anisotrópico com 4 extinções a 90° e brilho máximo a ~45° | Craig & Vaughan 1994, §3.2.4 | confirmado |
| `MIC-M36-A03-INTERNAS-005` | Reflexões internas em minerais de baixa absorção; cores de hematita, cuprita, esfalerita, cassiterita; ausentes em pirita, galena, magnetita, calcopirita, ouro | Craig & Vaughan 1994, §3.2.5, Tabela 3.3, Tabela A1.1 | confirmado |
| `MIC-M36-A03-FIGURAS-006` | Figuras no plano focal posterior; cruz estacionária em isotrópico; em anisotrópico a cruz se abre em isogiras ao girar | Craig & Vaughan 1994, §4.3.3, Fig. 4.11 | confirmado |
| `MIC-M36-A04-CRESCIMENTO-002` | Euédricos, zonamento, coloforme de crescimento rápido, framboides | Craig & Vaughan 1994, §7.2 e §7.9 (Roedder 1968: coloforme de cristais fibrosos em fluido supersaturado) | confirmado |
| `MIC-M36-A04-SUBSTITUICAO-004` | Relictos, contatos embaiados, avanço por fraturas; covelita e calcocita supergênicas | Craig & Vaughan 1994, §7.4 | confirmado |
| `MIC-M36-A04-RELATORIO-008` | Estrutura do relatório com grau de confiança | Craig & Vaughan 1994, cap. 8; estrutura do curso | confirmado |
| `MIC-M36-A04-EXEMPLO-009` | Exemplo hipotético pirita → calcopirita → covelita | — | confirmado |

**Nota sobre as referências.** Craig & Vaughan (1994, 2ª ed., Wiley), Ramdohr (1980, 2ª ed., Pergamon), Uytenbogaardt & Burke (1971, 2ª ed., Elsevier), Pracejus (2015, 2ª ed., Elsevier) e Marshall, Anglin & Mumin (2004, GAC) conferem em autor, ano, edição e editora. Barton & Bethke (1987) confere em título, periódico, volume e páginas. Ramdohr, Uytenbogaardt & Burke e Pracejus não foram relidos no texto (não há edição aberta); nenhuma afirmação corrigida depende só deles.

## Observações não factuais

- Os objetivos do currículo (hub e estado) citam "escala de Talmage" como tema. Depois da correção, a Aula 02 ensina Talmage como dureza ao risco (histórica) e não lista as classes. A avaliação não deve cobrar letras de classe nem minerais de referência.
- A Aula 02 ficou mais densa (tabela de refletância com números por mineral e o parágrafo de Talmage). A extensão fica para a revisão didática.

---

## Correções aplicadas

**Aplicadas em:** 2026-09-29

| # | claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|---|
| 1 | `MIC-M36-A01-CAMINHO-002` | 🟠 | Corrigido | aula-01 |
| 2 | `MIC-M36-A01-PREPARACAO-005` | 🟠 | Corrigido | aula-01 |
| 3 | `MIC-M36-A02-COM-002` | 🟡 | Corrigido (nome antigo mantido como referência) | aula-02 |
| 4 | `MIC-M36-A02-ORDEM-003` | 🟠 | Corrigido | aula-02 |
| 5 | `MIC-M36-A02-HABITO-005` | 🟠 | Corrigido | aula-02 |
| 6 | `MIC-M36-A02-DUREZA-006` | 🟠 | Corrigido | aula-02 |
| 7 | `MIC-M36-A02-TALMAGE-008` | 🟠 | Corrigido | aula-02 |
| 8 | `MIC-M36-A02-EXEMPLO-009` | 🟠 | Corrigido | aula-02 |
| 9 | `MIC-M36-A03-BIRREFLECTANCIA-002` | 🟠 | Corrigido | aula-03 |
| 10 | `MIC-M36-A03-ROTACAO-003` | 🔵 | Corrigido com ressalva (generalizado) | aula-03 |
| 11 | `MIC-M36-A03-CAUTELAS-004` | 🟠 | Corrigido | aula-03 |
| 12 | `MIC-M36-A03-EXEMPLO-007` | 🟠 | Corrigido | aula-03 |
| 13 | `MIC-M36-A04-PARAGENESE-001` | 🟠 | Corrigido | aula-04 |
| 14 | `MIC-M36-A04-EXSOLUCAO-003` | 🟠 | Corrigido | aula-04, aula-02 |
| 15 | `MIC-M36-A04-DEFORMACAO-005` | 🟠 | Corrigido | aula-04 |
| 16 | `MIC-M36-A04-DOENCA-006` | 🟠 | Corrigido (posições expostas, sem vencedor por depósito) | aula-04 |
| 17 | `MIC-M36-A04-APLICABILIDADE-007` | 🟠 | Corrigido | aula-04 |

**Propagação:** nenhuma externa. O módulo não tem questionário, baralho nem glossário (a auditoria correu antes deles), e não há card no Anki a corrigir. Busca em todas as aulas do curso fora do Módulo 36 por Talmage, linha de Kalb/pseudo-linha de Becke, doença da calcopirita, *chalcopyrite disease*, oxi-exsolução, lamelas de ilmenita/ilmenita em magnetita, exsolução ligada a ilmenita ou magnetita e nome da COM: **nenhuma ocorrência** (a única ocorrência de "exsolução" perto de "magnetita", no Módulo 34, Aula 03, é exsolução de fluido magmático, sem relação). Nada alterado fora do Módulo 36. O Módulo 37 (petrografia de minério) ainda não tem aulas; quando for escrito, deve herdar as restrições abaixo.

**Pendências:** nenhuma.

## Restrições para o questionário e os flashcards

1. **Pseudo-linha de Becke (linha de Kalb):** ao **afastar** a objetiva (baixar a platina), a linha vai para o mineral **mais mole**; ao aproximar, para o mais duro. Só aparece com relevo apreciável. Não inverter.
2. **Três durezas distintas:** de **polimento** (relevo, linha de Kalb), **ao risco** (Talmage, 1925: ponta arrastada sob carga) e de **microindentação** (Vickers, a única numérica em uso). Não cobrar Talmage como dureza de polimento, nem letras/minerais de referência das classes de Talmage.
3. **Ordem de dureza de polimento:** galena ≈ ouro < calcopirita < esfalerita ≲ pirrotita < magnetita ≲ ilmenita < hematita < pirita. Não cobrar a posição relativa de ouro × galena nem de pares marcados com ≈/≲; cobrar o que é robusto (pirita e hematita duras; galena, ouro e calcopirita moles).
4. **Refletância (546 nm, ar):** ouro > pirita > calcopirita ≈ galena > pirrotita > hematita > magnetita ≥ ilmenita ≈ esfalerita. Ilmenita e esfalerita **se sobrepõem**; separam-se por anisotropia e reflexões internas. Números só como ordem de grandeza; R cai em óleo.
5. **COM da IMA:** Comissão de **Mineralogia** de Minérios (antes Microscopia); comprimentos de onda 470, 546, 589 e 650 nm (546 se for um só).
6. **Galena:** diagnóstico = fileiras de cavidades triangulares; traços ortogonais só em corte paralelo a face do cubo. Deformação na galena = fileiras encurvadas, não geminação.
7. **Calcopirita é anisotrópica** (fracamente); pirrotita fortemente. Não cobrar "calcopirita isotrópica".
8. **Isotrópico = escuro estável; anisotrópico = 4 extinções a 90°.** Seção basal de uniaxial parece isotrópica. Anisotropia anômala da pirita existe, com **causa não esclarecida** — não cobrar uma causa.
9. **Birreflectância:** forte em grafita, molibdenita, covelita; moderada em pirrotita e hematita; fraca em ilmenita e arsenopirita (intensidades variam entre compilações — não cobrar grau fino). Não cobrar tintas de rotação da ilmenita.
10. **Refletores:** vidro plano = incidência vertical e abertura total (preferido na rotina), perde luz e gira levemente a polarização; prisma = mais brilho, metade da abertura. Não cobrar "vidro plano é melhor para polarização".
11. **Seção delgada polida** = face superior polida, sem lamínula; "duplamente polida" é outro tipo.
12. **Paragênese:** no curso, associação formada no mesmo evento; em Craig & Vaughan e na literatura norte-americana, *paragenesis* = sequência de formação. Não cobrar uma acepção como a única correta.
13. **Exsolução × oxi-exsolução:** ilmenita em magnetita é atribuída **sobretudo à oxi-exsolução**; exemplos de exsolução: pentlandita em pirrotita, hematita–ilmenita, calcopirita–bornita, ulvoespinélio em magnetita. Não cobrar ilmenita em magnetita como "exemplo clássico de exsolução".
14. **Doença da calcopirita:** exsolução explica poucos casos (Cu só se dissolve de forma apreciável na esfalerita acima de ~500 °C); debate vivo = substituição (Barton & Bethke 1987, com paradoxo da difusão) × crescimento conjunto. Não cobrar "exsolução" nem "substituição" como resposta fechada para todos os casos.
15. **Resolução:** limite óptico de alguns décimos de µm; o limite prático de identificação é maior. Não cobrar "1 µm = limite de resolução".
16. **Reflexões internas:** hematita vermelho-sangue, cuprita vermelha, esfalerita amarela a marrom (ausentes se muito rica em Fe), cassiterita amarela a marrom; ausentes em pirita, galena, magnetita, calcopirita e ouro.
17. Não cobrar números dos exemplos hipotéticos.
