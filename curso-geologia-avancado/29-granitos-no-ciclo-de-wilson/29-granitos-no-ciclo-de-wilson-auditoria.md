# Auditoria científica — Módulo 29: Granitos no ciclo de Wilson

**Curso:** geologia-avancado
**Módulo:** 29 — `29-granitos-no-ciclo-de-wilson` (6 aulas)
**Modo:** `audit-and-fix` · **Profundidade:** `full`
**Passagens:** 1 (2026-09-23). Backup do estado antes da auditoria: `course-state.yaml.bak-20260923-pre-m29-audit`.
**Veredito:** **Aprovado após correções**. Foram levantados 2 vermelhos, 10 laranjas, 2 azuis e 2 brancos, e todos foram tratados nas aulas. Nada ficou em aberto. Não houve achado amarelo.

---

## Resumo por severidade

| Severidade | Levantados | Corrigidos / tratados | Em aberto |
|---|---|---|---|
| 🔴 Erro | 2 | 2 | **0** |
| 🟠 Impreciso | 10 | 10 | **0** |
| 🟡 Desatualizado | 0 | — | 0 |
| 🔵 Sem fonte | 2 | 2 (1 confirmado com fonte nova; 1 atribuição retirada) | 0 |
| ⚪ Controverso | 2 | 2 (reescritos com as duas posições) | 0 |
| **Total** | **16** | **16** | **0** |

Gate de qualidade: **liberado** para o questionário e os flashcards (0 vermelhos e 0 laranjas em aberto), com as restrições listadas no fim. O módulo **não** foi fechado nesta etapa.

---

## Nota de método

A redação declarou **26 alegações auditáveis** (a01 4, a02 4, a03 4, a04 4, a05 5, a06 5) e pediu prioridade para seis pontos. O resultado de cada um:

| Ponto pedido | Resultado |
|---|---|
| Limiares de Chappell & White (ASI 1,1; Sr inicial 0,708; Na₂O 3,2%) | ASI 1,1 e Na₂O 3,2% (a ~5% de K₂O) **conferem**. O **Sr não confere como escrito**: o trabalho de 1974 dá **0,704-0,706 para o tipo I** e **> 0,708 para o tipo S**. Não existe um corte único em 0,708 (🟠 9). |
| Limiares de Whalen (10.000 Ga/Al > 2,6; Zr+Nb+Ce+Y > 350 ppm) | **Conferem**, porque são os limites de campo usados na literatura que aplica Whalen et al. (1987). O que estava errado era o **escopo**: Whalen et al. não trabalharam "no sudeste da Austrália", e sim com 131 amostras novas e conclusão de alcance mundial. O texto também omitia a ressalva dos próprios autores sobre granitos I e S muito fracionados (🟠 10). |
| Temperaturas de fusão por desidratação | **Conferem** como ordens de grandeza: muscovita ~650-750 °C, biotita ~760-900 °C, anfibólio ~850-950 °C a partir do solidus (Patiño Douce & Beard 1995; Rapp & Watson 1995; Brown 2013). O erro achado foi de **atribuição**: Vielzeuf & Holloway (1988) e Patiño Douce & Johnston (1991) são ambos do sistema **pelítico**, e o texto dizia que eles cobriam também metagrauvacas (🟠 12). Achou-se ainda uma **controvérsia não declarada** sobre a fusão com água livre (⚪ 15). |
| Datas de Iapetus, Rheic e Newer Granites | O **Rheic confere**: abriu no Ordoviciano Inicial e fechou do Devoniano ao Mississippiano (Nance et al. 2010, 2012). O **Iapetus não conferia**: abriu no Ediacarano entre Laurentia e Báltica/oeste de Gondwana, com Avalônia na margem gondwânica, e fechou no **Siluriano** (🟠 7). Os **Newer Granites** vão de **~430 a ~390 Ma** (o texto dava 430-400), em parte **contemporâneos** da colisão final, e não "muito depois" dela (🟠 8). |
| Faixas de ⁸⁷Sr/⁸⁶Sr dos Andes | **Conferem** como ordem de grandeza: Zona Vulcânica Sul 0,7036-0,7043; Zona Vulcânica Central ≥ 0,7055, até ~0,711 nos andesitos do pico do flare-up. O erro do parágrafo estava no **par Sm/Yb-Dy/Yb com granada-anfibólio** (🟠 4). |
| Geometria tabular dos plútons ("a confirmar") | **Confirmada**. Cruden (1998) mostra que muitos plútons são tabulares, com espessura média de ~3 km. McCaffrey & Petford (1997) acham uma lei de potência que favorece lâminas tabulares. A marca "a confirmar" saiu (🔵 14). |
| Referências "de memória" | **Todas as 57 conferidas** (Crossref para 54 artigos; J-STAGE, catálogo da editora e literatura secundária convergente para Ishihara 1977, Pitcher 1983 e Loiselle & Wones 1979). **Nenhuma paginação, volume ou autoria estava errada.** O único ajuste é o ano de Pitcher (o livro é de 1982 e costuma ser citado como 1983; ver 🟠 3). As marcas "de memória" foram trocadas por "CONFERIDO na auditoria". |

Os **dois vermelhos** são pontos que a redação **não** tinha marcado como risco, e seguem o padrão já visto nos módulos 27 e 28. Um é uma frase de física básica (Vs depende do módulo de incompressibilidade). O outro é um critério diagnóstico errado dentro de exemplos "hipotéticos" (a "alta razão Ba/Sr" como marca de manto). Dos laranjas, **três são de atribuição**, com a fonte citada dizendo outra coisa ou o contrário: Chappell 1999, Whalen 1987 e Vielzeuf/Patiño Douce. **Dois são de consistência entre módulos**: a constante do ⁸⁷Rb e as latitudes dos flat slabs, que o módulo 18 já tinha corrigido.

**Ferramentas:** metadados na **API do Crossref**. Resumos na **API do OpenAlex** e da **Semantic Scholar**: Rapp & Watson 1995; Patiño Douce & Beard 1995; Cawood et al. 2001; Soper et al. 1992; Matte 2001; Cocks & Torsvik 2002; Mamani et al. 2010; Gutscher et al. 2000; Eby 1992; Frost et al. 2001; Whalen et al. 1987; Brown 2013; Cruden 1998; McCaffrey & Petford 1997; Améglio & Vigneresse 1999; Davidson et al. 2007; Fowler et al. 2001; Nance et al. 2012; Willis-Richards & Jackson 1989; Dyck et al. 2019. **Texto lido**: resumo de Chappell (1999) no portal da Macquarie University e texto integral de Milne et al. (2023, *JGS* 180, eprints Glasgow). Buscas na web para Chappell & White (1974), Whalen et al. (1987), Neilson et al. (2009), Weinberg & Hasalová (2015), Pitcher (1983) e as faixas de Sr dos Andes (Frontiers in Earth Science 2022; Nature Communications 2018).

---

## Achados

### 🔴 1. "A velocidade de ambas [P e S] depende do módulo de incompressibilidade"

**claim_id:** `GRANIT-M29-A01-VELOCIDADE-ONDAS-005` (criado pela auditoria)
**Tipo:** erro factual
**Onde:** Aula 01 · "Ondas sísmicas e o modelo em camadas"
**Está escrito:** "A velocidade de ambas depende do módulo de rigidez, do módulo de incompressibilidade e da densidade do meio."
**Problema:** a velocidade da onda S é Vs = √(μ/ρ) e depende **só** do módulo de rigidez e da densidade. Quem depende também do módulo de incompressibilidade é a onda P, com Vp = √((K + 4μ/3)/ρ). A frase afirma o contrário para a S, e é exatamente o que explica por que Vs cai a zero num líquido (μ = 0), ponto que a própria aula usa logo abaixo.
**Correção aplicada:** "A velocidade da onda P depende do módulo de incompressibilidade, do módulo de rigidez e da densidade; a da onda S, só do módulo de rigidez e da densidade (por isso Vs cai a zero num líquido, que tem rigidez nula)."
**Fonte:** Kearey, Klepeis & Vine (2009), *Global Tectonics*, 3ª ed., cap. 2 (expressões de Vp e Vs; física-padrão de meios elásticos isotrópicos) · **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** só na Aula 01.

### 🔴 2. "Alta razão Ba/Sr" como marca de participação mantélica

**claim_id:** `GRANIT-M29-A02-ALTO-BA-SR-005` (criado pela auditoria; cobre também o exemplo da Aula 04, claim `GRANIT-M29-A04-EXEMPLO-INTERVALOS-004`)
**Tipo:** erro factual (critério diagnóstico)
**Onde:** Aula 02 · Exemplo trabalhado (Corpo 3, situação e resolução 3). Aula 04 · Exemplo trabalhado (pluton de 403 Ma, situação e passo 3).
**Está escrito:** "alta razão Ba/Sr" (Aula 02); "alto K, alto Ba/Sr, enclaves máficos indicando participação de magma mantélico" (Aula 02); "enclaves microgranulares máficos e alto Ba/Sr" e "O pluton com enclaves máficos e alto Ba/Sr (403 Ma) aponta para participação mantélica" (Aula 04).
**Problema:** a assinatura dos granitoides caledonianos tardios de fonte mantélica enriquecida é a dos **granitos "alto Ba-Sr"**, com **teores altos de Ba e de Sr**, e não uma **razão** Ba/Sr alta. Uma razão Ba/Sr alta costuma indicar o contrário, um líquido muito fracionado que perdeu Sr para o plagioclásio. O corpo das duas aulas já dizia certo ("ricos em K, Ba e Sr"; "alto Ba e Sr"), mas os exemplos ensinavam a regra errada e iriam direto para uma questão de diagnóstico.
**Correção aplicada:** "Ba e Sr altos" nos quatro lugares, com a nota "(granitos 'alto Ba-Sr')" na primeira ocorrência de cada exemplo.
**Fonte:** Fowler et al. (2001), "Petrogenesis of high Ba-Sr granites: the Rogart pluton, Sutherland", *J. Geol. Soc.* 158, 521-534, doi:10.1144/jgs.158.3.521 (resumo lido); Fowler et al. (2008), *Lithos* 105, 129-148; Tarney & Jones (1994), *J. Geol. Soc.* 151, 855-868. Milne et al. (2023) também descrevem a natureza "high Ba–Sr" desses corpos · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 02 (2 lugares), Aula 04 (2 lugares).

### 🟠 3. Pitcher: "quatro grupos"

**claim_id:** `GRANIT-M29-A02-PITCHER-BARBARIN-002`
**Tipo:** imprecisão (omissão)
**Onde:** Aula 02 · "As classificações por ambiente: Pitcher e Barbarin"
**Está escrito:** "distinguindo quatro grupos: cordilheiranos [...], caledonianos [...], hercinianos [...] e anorogênicos"
**Problema:** o esquema de Pitcher tem **cinco** tipos: **M** (arcos de ilha oceânicos), **I cordilheirano**, **I caledoniano**, **S herciniano** e **A** (anorogênico). O tipo M ficou de fora, e a Aula 05 o menciona sem dizer que ele faz parte do esquema. O livro de Hsü (*Mountain Building Processes*) é de **1982**, e o capítulo é citado ora como 1982, ora como 1983.
**Correção aplicada:** "cinco tipos: M (arcos de ilha oceânicos, fonte mantélica), I cordilheirano [...], I caledoniano [...], S herciniano [...] e A (anorogênico)". Nas Fontes foi anotado "(livro de 1982; citado frequentemente como 1983)".
**Fonte:** síntese de Pitcher em literatura secundária (IntechOpen 2021, cap. 75063: "M-type, I- (Cordilleran or Caledonian) type, S-type and A-type"); registro bibliográfico de Pitcher (1982) em Springer, *Int. J. Earth Sci.*, doi:10.1007/BF01820573 (lista de referências) · **Nível:** revisada por pares / base de referência
**Confiança:** confirmado
**Também aparece em:** só na Aula 02.

### 🟠 4. Sm/Yb e Dy/Yb "elevados com granada e anfibólio", ambos ligados à crosta espessa

**claim_id:** `GRANIT-M29-A03-ESPESSURA-ISOTOPOS-003`
**Tipo:** imprecisão
**Onde:** Aula 03 · "Espessura crustal e o que os magmas registram"; Exemplo trabalhado, passo 2
**Está escrito:** "o Sm/Yb e o Dy/Yb ficam elevados quando o magma se equilibrou com um resíduo contendo granada e anfibólio, que é estável a pressões que só ocorrem em crosta espessa"; "Sm/Yb alto (granada e anfibólio na fonte ou no resíduo)"
**Problema:** Mamani et al. (2010) usam o **Sm/Yb para rastrear a granada** e o **Dy/Yb para rastrear o anfibólio**. As duas razões não sobem juntas por causa dos dois minerais. O anfibólio retém mais os ETR médios (Dy) do que os pesados (Yb), e o fracionamento de anfibólio **baixa** o Dy/Yb do líquido (o "anfibólio esponja" de Davidson et al. 2007). Só a granada exige pressões de crosta espessa. O anfibólio é estável em boa parte da crosta média e inferior.
**Correção aplicada:** o Sm/Yb sobe com granada residual, estável só em crosta espessa (base com mais de ~40 km). O Dy/Yb responde também ao anfibólio, que tende a baixá-lo, e Mamani et al. usam o Dy/Yb para o anfibólio e o Sm/Yb para a granada. No exemplo, "(granada no resíduo; o anfibólio eleva o Sm/Yb só moderadamente)".
**Fonte:** Mamani, Wörner & Sempere (2010), *GSA Bull.* 122, 162-182, doi:10.1130/B26538.1 (resumo lido: "Dy/Yb and Sm/Yb ratios, which track [...] amphibole and garnet, respectively"); Davidson et al. (2007), *Geology* 35, 787-790, doi:10.1130/G23637A.1 · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** só na Aula 03 (o recap fala só de Sm/Yb e La/Yb com granada e já estava correto).

### 🟠 5. Latitudes dos flat slabs divergem do Módulo 18 auditado

**claim_id:** `GRANIT-M29-A03-FLAT-SLAB-001`
**Tipo:** inconsistência interna (entre módulos)
**Onde:** Aula 03 · "Geometria da subducção"
**Está escrito:** "o do Peru (aproximadamente 2° a 15°S) e o Pampeano [...] (aproximadamente 28° a 33°S)"
**Problema:** a auditoria do Módulo 18 (achado `AUD-M18-A01-PERUFLATSLAB-016`) corrigiu o flat slab peruano para **~5-15°S**, com base em Ramos & Folguera (2009) e Ramos et al. (2002), e confirmou o pampeano em **~27-33°S** (27°00'-33°30'S). Com o texto como estava, o aluno receberia valores diferentes em dois módulos. Gutscher et al. (2000) descrevem um segmento peruano de ~1500 km, compatível com 5-15°S.
**Correção aplicada:** "(aproximadamente 5° a 15°S)" e "(aproximadamente 27° a 33°S)". A convergência (~7 cm/a) e o mergulho (~30°) conferem e não mudaram.
**Fonte:** auditoria do Módulo 18 (2026-09-12, Ramos & Folguera 2009, *GSL Spec. Publ.* 327, 31-54); Gutscher et al. (2000), *Tectonics* 19, 814-833 (resumo lido) · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** só no corpo da Aula 03 (o recap não dá latitudes).

### 🟠 6. Constante do ⁸⁷Rb 1,393 × 10⁻¹¹ a⁻¹ "consulte o Módulo 26", mas o Módulo 26 não usa esse valor

**claim_id:** `GRANIT-M29-A03-EXEMPLO-SR-004` e `GRANIT-M29-A05-EXEMPLOS-NUM-005`
**Tipo:** inconsistência interna (entre módulos)
**Onde:** Aula 03 · Exemplo trabalhado, passo 1. Aula 05 · Exemplo trabalhado 2.
**Está escrito:** "λ(⁸⁷Rb) = 1,393 × 10⁻¹¹ a⁻¹ (valor adotado por convenção nesta aula; consulte o Módulo 26 para a discussão sobre constantes de decaimento)"
**Problema:** o Módulo 26 (auditado) ensina **dois** valores, o convencional de Steiger & Jäger (1977), 1,42 × 10⁻¹¹ a⁻¹, e o recomendado pela IUPAC-IUGS (Villa et al. 2015), **1,3972 × 10⁻¹¹ a⁻¹**. O 1,393 × 10⁻¹¹ é de Nebel et al. (2011) e não aparece no Módulo 26. A remissão manda o aluno a um lugar onde o número não está.
**Correção aplicada:** λ = 1,3972 × 10⁻¹¹ a⁻¹ (IUPAC-IUGS 2015, como no Módulo 26), com as contas refeitas por script. Aula 03: λt = 8,38 × 10⁻⁴, e^(λt) − 1 ≈ 8,39 × 10⁻⁴; A: correção ≈ 0,00034, razão inicial ≈ **0,70446**; B: correção ≈ 0,00042, razão inicial ≈ **0,70570**. Aula 05: e^(λt) − 1 = 0,00420, correção 0,0420, razão inicial ≈ **0,718** (não muda). As conclusões dos dois exemplos ficam iguais.
**Fonte:** Módulo 26, Aula 03 e auditoria (Villa et al. 2015, IUPAC-IUGS; Steiger & Jäger 1977) · **Nível:** normativa
**Confiança:** confirmado
**Também aparece em:** Aulas 03 e 05.

### 🟠 7. Abertura e fechamento do Iapetus

**claim_id:** `GRANIT-M29-A04-IAPETUS-RHEIC-001`
**Tipo:** imprecisão
**Onde:** Aula 04 · "Dois oceanos, dois orógenos"; Recap item 1
**Está escrito:** "[Iapetus] Abriu-se entre Laurentia (o núcleo da América do Norte, com a Groenlândia e a Escócia setentrional) e Báltica e Avalônia, na passagem do Neoproterozoico ao Cambriano, e foi consumido por subducção no Ordoviciano"; no recap, "Iapetus (entre Laurentia e Báltica/Avalônia) fechou no Ordoviciano-Devoniano".
**Problema:** (a) o Iapetus abriu com a separação da Laurentia em relação ao **oeste de Gondwana** (Amazônia-Rio de la Plata) a partir de **~570 Ma**. O oceano já era largo por ~550 Ma, e a transição rifte-deriva na margem da Terra Nova foi por volta de 540-535 Ma. Avalônia estava na **margem de Gondwana**, e não era uma placa independente na abertura. (b) O **fechamento foi no Siluriano**: Avalônia e Báltica acoplaram-se à Laurentia no Siluriano, e a deformação acadiana devoniana teve outra causa. "Consumido no Ordoviciano" e "fechou no Ordoviciano-Devoniano" encurtam e alargam a história de forma errada. (c) A Escócia **inteira**, e não só a setentrional, ficava do lado laurenciano da sutura do Iapetus. O Rheic, por sua vez, **confere**.
**Correção aplicada:** "Abriu-se no fim do Neoproterozoico (Ediacarano: separação a partir de ~570 Ma, oceano já largo por ~550 Ma; Cawood et al., 2001) entre Laurentia (com a Groenlândia e a Escócia) e, do outro lado, Báltica e o oeste de Gondwana, em cuja margem estava Avalônia; foi consumido por subducção do Cambriano tardio ao Siluriano e fechou no Siluriano". O recap foi ajustado e Cawood et al. (2001) entrou nas Fontes.
**Fonte:** Cawood, McCausland & Dunning (2001), *GSA Bull.* 113, 443-453 (resumo lido); Soper et al. (1992), *J. Geol. Soc.* 149, 871-880 (resumo lido); Nance et al. (2012), *Geosci. Frontiers* 3, 125-135, doi:10.1016/j.gsf.2011.11.008 (resumo lido: "the ocean reached its greatest width with the closure of Iapetus [...] in the Silurian") · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 04 (corpo e recap). A Aula 02 só fala do Iapetus como oceano ancestral e está correta.

### 🟠 8. Newer Granites: "muito depois", "430 a 400 Ma"

**claim_id:** `GRANIT-M29-A04-NEWER-GRANITES-002`
**Tipo:** imprecisão
**Onde:** Aula 04 · "Granitos caledonianos: o tipo pós-colisional"; Recap item 2
**Está escrito:** "Os granitos que ali se alojaram muito depois, entre aproximadamente 430 e 400 Ma"; no recap, "(~430-400 Ma)".
**Problema:** (a) a faixa publicada é de **c. 426-390 Ma** (Milne et al. 2023), com o magmatismo cálcio-alcalino do Terreno Grampiano começando **c. 430 Ma** (Neilson et al. 2009). O limite de 400 Ma corta a parte mais jovem. (b) Esses corpos são posteriores ao pico **grampiano** (~470 Ma), mas **se sobrepõem** à subducção final do Iapetus e às deformações escandiana e acadiana (Milne et al. 2023). "Muito depois" da colisão final, que o próprio parágrafo situa no Siluriano, está errado. (c) Milne et al. (2023) observam que o termo é antigo e reúne corpos de idades e contextos diferentes.
**Correção aplicada:** "depois do pico grampiano e em parte ainda durante a colisão final, entre aproximadamente 430 e 390 Ma — os 'Newer Granites' (termo antigo, que reúne corpos de idades e contextos diferentes)". Recap "(~430-390 Ma)". Neilson et al. (2009) e Milne et al. (2023) entraram nas Fontes.
**Fonte:** Neilson, Kokelaar & Crowley (2009), *J. Geol. Soc.* 166, 545-561, doi:10.1144/0016-76492008-069; Milne et al. (2023), *J. Geol. Soc.* 180, doi:10.1144/jgs2022-076 (texto lido) · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 04 (corpo e recap).

### 🟠 9. Sr inicial do tipo I "em geral abaixo de ~0,708" e um corte único em 0,708

**claim_id:** `GRANIT-M29-A05-CRITERIOS-IS-001`
**Tipo:** imprecisão
**Onde:** Aula 05 · "Critérios do tipo I"; "Cuidado"; Recap item 2
**Está escrito:** "⁸⁷Sr/⁸⁶Sr inicial em geral abaixo de ~0,708"; "os valores de corte (ASI 1,1; Sr inicial 0,708; Na₂O 3,2%)"; no recap, "Os cortes (ASI 1,1; Sr 0,708)".
**Problema:** Chappell & White (1974) deram **0,704-0,706 para o tipo I** e **> 0,708 para o tipo S**. O 0,708 é o limite inferior do tipo S, e não um divisor simétrico. Entre 0,706 e 0,708 fica uma faixa que o critério original não atribui. ASI 1,1 e Na₂O ~3,2% (a ~5% de K₂O, caindo para ~2,2% a ~2% de K₂O) conferem.
**Correção aplicada:** tipo I "0,704-0,706 no caso original"; "Cuidado" com "(ASI 1,1; Sr inicial 0,704-0,706 para I e > 0,708 para S; Na₂O 3,2%)"; recap com "Sr ≤ 0,706 no I e > 0,708 no S".
**Fonte:** Chappell & White (1974), *Pacific Geology* 8, 173-174, via Chappell & White (2001), *AJES* 48, 489-499 (reimpressão; resumo lido), e literatura que reproduz os critérios (Wikipedia "I-type granite", com as citações; resultados de busca convergentes para 0,704-0,706 / > 0,708) · **Nível:** revisada por pares / geral convergente
**Confiança:** confirmado (texto de 1974 não lido na íntegra; valores convergentes em várias fontes independentes)
**Também aparece em:** Aula 05 (3 lugares). O exemplo 2 (Sr inicial 0,718 "acima de 0,708") continua certo.

### 🟠 10. Whalen et al. (1987) "caracterizaram-nos no sudeste da Austrália", e ressalva omitida

**claim_id:** `GRANIT-M29-A05-TIPO-A-002`
**Tipo:** imprecisão (atribuição) + omissão que gera erro
**Onde:** Aula 05 · "Critérios do tipo A"
**Está escrito:** "Collins et al. (1982) e Whalen et al. (1987) caracterizaram-nos no sudeste da Austrália e chegaram a critérios geoquímicos mais objetivos."
**Problema:** Collins et al. (1982) trabalharam no sudeste da Austrália. Whalen et al. (1987) usaram **novas análises de 131 amostras** e concluíram que os granitos A ocorrem **no mundo todo e em vários ambientes**, e "não indicam necessariamente ambiente anorogênico ou de rifte". Os próprios autores advertem que granitos I e S félsicos **muito fracionados** podem ter Ga/Al e outros valores sobrepostos aos do tipo A, ressalva que pesa sobre uma amostra como a Z (74,8% de SiO₂). Os limiares (10.000 Ga/Al > 2,6; Zr+Nb+Ce+Y > 350 ppm) **conferem**.
**Correção aplicada:** atribuição separada ("Collins et al. (1982) caracterizaram-nos no sudeste da Austrália; Whalen et al. (1987), com 131 análises novas, generalizaram critérios geoquímicos mais objetivos") e acrescentada a ressalva de Whalen et al. sobre granitos I e S muito fracionados.
**Fonte:** Whalen, Currie & Chappell (1987), *CMP* 95, 407-419, doi:10.1007/BF00402202 (resumo lido via Semantic Scholar); uso dos limites 2,6 e 350 ppm na literatura (resultados de busca convergentes) · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** só na Aula 05.

### 🟠 11. Chappell (1999) citado para uma tese que o artigo contradiz

**claim_id:** `GRANIT-M29-A05-FRACIONAMENTO-CHAPPELL-006` (criado pela auditoria)
**Tipo:** imprecisão (atribuição) + omissão que gera erro
**Onde:** Aula 05 · "Onde a classificação falha", item 1
**Está escrito:** "Os últimos líquidos de um magma tipo I podem tornar-se peraluminosos [...] e passar a ter aparência de tipo S sem que a fonte tenha sido sedimentar. Chappell (1999) discute esse ponto."
**Problema:** Chappell (1999) mostra que os magmas I fracionados **tendem à saturação em Al**, e por isso podem ficar fracamente peraluminosos. Mas com fracionamento extenso desenvolve-se uma separação **quase completa** de saturação em Al entre I e S, e os granitos I e S fortemente fracionados "podem ser facilmente distinguidos" pelo P, Y, ETR e Th. A aula citava o artigo como apoio à confusão I→S, que é o contrário do que ele conclui.
**Correção aplicada:** "podem tornar-se fracamente peraluminosos (ASI perto de 1) [...] e, olhando só o ASI, parecer tipo S. Chappell (1999) mostra, porém, que o fósforo (e Y, ETR e Th) continua a separá-los: a apatita é solúvel no líquido peraluminoso, e o P sobe no S e cai no I".
**Fonte:** Chappell (1999), *Lithos* 46, 535-551, doi:10.1016/S0024-4937(98)00086-3 (resumo lido no portal da Macquarie University) · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** só na Aula 05. O hub (pontos de dificuldade) fala de "granitos muito fracionados ou contaminados" de modo geral e continua correto.

### 🟠 12. Vielzeuf & Holloway (1988) e Patiño Douce & Johnston (1991) "de metapelitos e de metagrauvacas"

**claim_id:** `GRANIT-M29-A06-FUSAO-DESIDRATACAO-001`
**Tipo:** imprecisão (atribuição)
**Onde:** Aula 06 · "Geração: fusão parcial da crosta"
**Está escrito:** "Vielzeuf & Holloway (1988) e Patiño Douce & Johnston (1991) mapearam experimentalmente a fusão de metapelitos e de metagrauvacas."
**Problema:** os dois trabalhos são do **sistema pelítico**, como dizem os títulos ("in the pelitic system"). Os experimentos em metagrauvacas e gnaisses de biotita são de outros autores (por exemplo, Patiño Douce & Beard 1995). As **temperaturas** da seção **conferem** como ordens de grandeza.
**Correção aplicada:** "mapearam experimentalmente a fusão de metapelitos; Patiño Douce & Beard (1995) fizeram o mesmo para gnaisse de biotita e anfibolito com quartzo", com a referência nas Fontes.
**Fonte:** Crossref (títulos); Patiño Douce & Beard (1995), *J. Petrol.* 36, 707-738 (resumo lido: fusão de desidratação de gnaisse de biotita e anfibolito com quartzo a partir de ~850 °C a 3 kbar e ~930 °C a 15 kbar); Rapp & Watson (1995), *J. Petrol.* 36, 891-931 (resumo lido); Brown (2013), *GSA Bull.* 125, 1079-1113 (resumo lido) · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** só na Aula 06.

### 🔵 13. "Frost et al. (2001) usam [...] 1,1 como referência de 'fortemente peraluminoso'"

**claim_id:** `GRANIT-M29-A05-FROST-003`
**Tipo:** evidência insuficiente
**Onde:** Aula 05 · "O cálculo do ASI"
**Está escrito:** "Frost et al. (2001) usam 1,0 como fronteira formal entre metaluminoso e peraluminoso e 1,1 como referência de 'fortemente peraluminoso' em discussões de tipo S."
**Problema:** o resumo de Frost et al. (2001) confirma o ASI [Al/(Ca − 1,67P + Na + K)] e a fronteira 1,0. Não foi possível confirmar que eles adotem 1,1 como "fortemente peraluminoso", porque o texto integral tem acesso restrito. O 1,1 é o divisor de Chappell & White.
**Tratamento:** a parte não verificada foi **retirada**. O texto ficou "Frost et al. (2001) usam 1,0 como fronteira formal entre metaluminoso e peraluminoso". Não era central para a aula, então não houve decisão a pedir.
**Fonte:** Frost et al. (2001), *J. Petrol.* 42, 2033-2048, doi:10.1093/petrology/42.11.2033 (resumo lido) · **Nível:** revisada por pares
**Confiança:** não verificado → afirmação removida
**Também aparece em:** só na Aula 05.

### 🔵 14. Plútons tabulares "(a ser confirmado na literatura primária para cada caso)"

**claim_id:** `GRANIT-M29-A06-GRAVIMETRIA-003`
**Tipo:** evidência insuficiente (declarada pela redação), agora resolvida
**Onde:** Aula 06 · "Gravimetria: a forma do pluton em profundidade"
**Está escrito:** "muitos plutons têm geometria tabular ou em cunha, com espessuras da ordem de poucos quilômetros e muito mais largos que espessos (a ser confirmado na literatura primária para cada caso)"
**Problema:** a afirmação geral **está confirmada**. Cruden (1998) conclui, a partir de dados gravimétricos e estruturais, que muitos plútons de 3 a 100 km de largura são tabulares, com espessura média de ~3 km. McCaffrey & Petford (1997) acham uma relação de potência comprimento-espessura que reflete "preferência por geometrias tabulares". Brown (2013) situa a colocação de lacólitos e plútons em cunha em torno da transição dúctil-frágil. A marca de incerteza ficou desnecessária.
**Correção aplicada:** a marca foi retirada e o trecho passou a citar Cruden (1998) e McCaffrey & Petford (1997), incluídos nas Fontes. A ressalva de que cada caso exige seu próprio modelo continua no texto, por meio da não unicidade.
**Fonte:** Cruden (1998), *J. Geol. Soc.* 155, 853-862, doi:10.1144/gsjgs.155.5.0853 (resumo lido); McCaffrey & Petford (1997), *J. Geol. Soc.* 154, 1-4, doi:10.1144/gsjgs.154.1.0001 (resumo lido) · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 06 (o recap já dizia "muitos plutons são tabulares" sem ressalva).

### ⚪ 15. Newer Granites "pós-colisionais" contra o "sin-colisional tardio" de Atherton & Ghani

**claim_id:** `GRANIT-M29-A04-SLAB-BREAKOFF-SIN-POS-005` (criado pela auditoria; cobre a Aula 02)
**Tipo:** controvérsia (certeza indevida)
**Onde:** Aula 02 · "Pós-colisão"; Aula 04 · parágrafo de Atherton & Ghani
**Está escrito:** na Aula 02, sob "Pós-colisão": "Atherton & Ghani (2002) propuseram o *slab break-off* para os 'Newer Granites'"; na Aula 04, "Granitos caledonianos: o tipo pós-colisional", com Atherton & Ghani como proponentes.
**Problema:** o próprio título de Atherton & Ghani (2002) classifica esse magmatismo como **"Late Granite syn-collisional"**. Neilson et al. (2009) tratam o mesmo episódio como **pós-colisional**, e Milne et al. (2023) lembram que parte dos corpos é pré-break-off e ligada à subducção. O rótulo depende de qual colisão se toma como referência: a grampiana (~470 Ma) ou o fechamento final do Iapetus no Siluriano. A aula apresentava um lado como consenso e atribuía a Atherton & Ghani um enquadramento que não é o deles.
**Tratamento:** as duas posições foram expostas na Aula 04, no parágrafo de Atherton & Ghani. A Aula 02 ganhou a observação "(que eles classificam como sin-colisionais tardios; outros autores, como pós-colisionais — Aula 04)". O objetivo "Ao final você vai conseguir" da Aula 04 ganhou a mesma ressalva, aplicada durante a revisão didática. A lição central da aula ficou como estava: a assinatura de arco vem da fonte, e o regime de colocação é outro.
**Fonte:** Atherton & Ghani (2002), *Lithos* 62, 65-85 (título; Crossref); Neilson et al. (2009); Milne et al. (2023), texto lido · **Nível:** revisada por pares
**Confiança:** em disputa (terminológica)
**Também aparece em:** Aulas 02 e 04.

### ⚪ 16. Fusão com água livre "produz volumes pequenos" e a desidratação é "o principal mecanismo"

**claim_id:** `GRANIT-M29-A06-FUSAO-FLUIDO-PRESENTE-006` (criado pela auditoria)
**Tipo:** controvérsia (certeza indevida)
**Onde:** Aula 06 · "Geração: fusão parcial da crosta"
**Está escrito:** "Produz volumes pequenos de líquido, e o fluido é limitado; é mecanismo relevante em zonas de cisalhamento e localmente." e "[desidratação] É o principal mecanismo de fusão crustal em larga escala"
**Problema:** essa é a posição clássica (Clemens & Vielzeuf 1987; Clemens & Stevens 2015). Weinberg & Hasalová (2015) sustentam, numa revisão ampla, que a fusão com influxo de água é **comum e subestimada**, e que pode gerar volumes relevantes. O debate teve comentário e réplica no mesmo volume da *Lithos*. Brown (2013) admite as duas vias, conforme a temperatura.
**Tratamento:** o texto foi reescrito para apresentar a posição clássica **e** a revisão de Weinberg & Hasalová (2015), com o debate marcado como aberto. As referências entraram nas Fontes.
**Fonte:** Weinberg & Hasalová (2015), *Lithos* 212-215, 158-188, doi:10.1016/j.lithos.2014.08.021; Clemens & Stevens (2015), comentário, *Lithos* 234-235, 100-101; Brown (2013), resumo lido · **Nível:** revisada por pares
**Confiança:** em disputa
**Também aparece em:** só na Aula 06 (o recap fala só da desidratação "em larga escala", mantida com a palavra "clássica").


---

## Verificado e correto

| Alegação | Resultado | Fonte |
|---|---|---|
| Descontinuidades (Moho, 410, 660, 2890, 5150 km; 660 km = ringwoodita → bridgmanita + ferropericlásio; Vs = 0 no núcleo externo) | ✅ | PREM (Dziewonski & Anderson 1981); Kearey et al. 2009 |
| Altiplano com Moho até ~70 km; média continental ~40 km | ✅ | Frontiers 2022; Nature Comm. 2018 (60-70 km sob a CVZ) |
| Transição frágil-dúctil: quartzo ~300 °C, feldspato ~450 °C, olivina ~600-700 °C | ✅ (ordens de grandeza) | síntese da literatura experimental (busca); Kohlstedt et al. 1995 |
| Debate "jelly sandwich" × "crème brûlée" em aberto | ✅ | Jackson 2002; Burov & Watts 2006 |
| Refração: h = (x_c/2)√[(V2−V1)/(V2+V1)] = 34,5 km; z = 290/g = 11,6 e 7,25 km (37,5% menor) | ✅ (recalculado) | fórmula-padrão |
| Wilson 1966, estágios do ciclo, Iapetus como nome posterior | ✅ | Wilson et al. 2019; Harland & Gayer 1972 (nome) |
| Barbarin 1999: grupos por mineralogia e ênfase em mistura | ✅ | Crossref; resumo não disponível, conteúdo consistente com a literatura |
| Nazca ~7 cm/a; mergulho normal ~30°; placa plana a ~100 km; ausência de vulcanismo | ✅ | Gutscher et al. 2000 |
| Kay & Mpodozis 2002: fases ~27-20, ~20-16, ~8-4 Ma | ✅ | verificado na redação; Crossref |
| Mamani et al. 2010: >1500 análises, 13-18°S, 190-0 Ma | ✅ | resumo lido (650 Sr, 610 Nd, 570 Pb) |
| Faixas de ⁸⁷Sr/⁸⁶Sr: ~0,704 (ZVS) a 0,706-0,708 ou mais (ZVC) | ✅ | ZVS 0,7036-0,7043; ZVC > 0,7050, até 0,708-0,711 |
| Hildreth & Moorbath 1988: MASH, aumento isotópico com espessamento | ✅ | Crossref; literatura derivada |
| Rheic: abertura no Ordoviciano Inicial, fechamento do Devoniano ao Carbonífero | ✅ | Nance et al. 2010 e 2012 |
| Newer Granites ricos em K, alto Ba-Sr, enclaves máficos | ✅ | Fowler et al. 2001; Milne et al. 2023 |
| Variscos peraluminosos ~340-300 Ma; durbachitos K-Mg da Boêmia | ✅ | Parat et al. 2009; Janoušek & Holub 2007 (Crossref) |
| Cornualha ~295-275 Ma, tipo S, série ilmenita, duas micas, Sn-W, alta produção de calor | ✅ | Willis-Richards & Jackson 1989 (resumo lido: 270-295 Ma) |
| ASI: fórmula com CaO′ = CaO − 3,33 P₂O₅ (Ca:P = 5:3; P₂O₅ tem 2 P) | ✅ | estequiometria; Frost et al. 2001 (forma catiônica 1,67 P) |
| Exemplos X, Y, Z: ASI 0,96 / 1,30 / 0,99; 10.000 Ga/Al 3,96; soma 725 ppm; Fe# 0,95 | ✅ (recalculado) | aritmética |
| Eby 1992: A₁ (OIB, rifte/intraplaca) × A₂ (crosta que passou por colisão ou arco) | ✅ | resumo lido |
| Frost 2001: Fe#, MALI, ASI; independente do ambiente | ✅ | resumo lido |
| Loiselle & Wones 1979; Bonin 2007; Collins et al. 1982 | ✅ | Crossref / citação-padrão convergente |
| Temperaturas de fusão por desidratação (muscovita, biotita, anfibólio); solidus com água ~650 °C | ✅ | Patiño Douce & Beard 1995; Brown 2013; Dyck et al. 2019 |
| Rapp & Watson 1995: 8-32 kbar, líquidos trondhjemítico-tonalíticos, granada acima de ~12 kbar | ✅ | resumo lido |
| Watson & Harrison 1983; Miller et al. 2003 (granitos quentes e frios) | ✅ | Crossref |
| Ascensão por diques favorecida sobre diápiro; construção por pulsos | ✅ | Petford et al. 2000; Brown 2013 (resumo lido) |
| Densidades (granito 2,62-2,67; encaixante 2,70-2,80 g/cm³) | ✅ (valores típicos) | Kearey et al. 2009 |
| Exemplo gravimétrico: 0,04193 mGal/(g·cm⁻³·m); t ≈ 2385 m; x½ = 0,766 z; z ≈ 6,0 km; R ≈ 5,05 km; V ≈ 539 km³ | ✅ (recalculado) | fórmulas-padrão |
| Ishihara 1977; Blevin & Chappell 1992; Sillitoe 2010 | ✅ | J-STAGE; Crossref |
| Bibliografia: 57 referências, paginação e autoria | ✅ (nenhuma errada) | Crossref, J-STAGE |

---

## Correções aplicadas

**Aplicadas em:** 2026-09-23

| # | claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|---|
| 1 | `GRANIT-M29-A01-VELOCIDADE-ONDAS-005` | 🔴 | Corrigido | aula-01 |
| 2 | `GRANIT-M29-A02-ALTO-BA-SR-005` | 🔴 | Corrigido | aula-02, aula-04 |
| 3 | `GRANIT-M29-A02-PITCHER-BARBARIN-002` | 🟠 | Corrigido | aula-02 |
| 4 | `GRANIT-M29-A03-ESPESSURA-ISOTOPOS-003` | 🟠 | Corrigido | aula-03 |
| 5 | `GRANIT-M29-A03-FLAT-SLAB-001` | 🟠 | Corrigido | aula-03 |
| 6 | `GRANIT-M29-A03-EXEMPLO-SR-004` / `GRANIT-M29-A05-EXEMPLOS-NUM-005` | 🟠 | Corrigido | aula-03, aula-05 |
| 7 | `GRANIT-M29-A04-IAPETUS-RHEIC-001` | 🟠 | Corrigido | aula-04 |
| 8 | `GRANIT-M29-A04-NEWER-GRANITES-002` | 🟠 | Corrigido | aula-04 |
| 9 | `GRANIT-M29-A05-CRITERIOS-IS-001` | 🟠 | Corrigido | aula-05 |
| 10 | `GRANIT-M29-A05-TIPO-A-002` | 🟠 | Corrigido | aula-05 |
| 11 | `GRANIT-M29-A05-FRACIONAMENTO-CHAPPELL-006` | 🟠 | Corrigido | aula-05 |
| 12 | `GRANIT-M29-A06-FUSAO-DESIDRATACAO-001` | 🟠 | Corrigido | aula-06 |
| 13 | `GRANIT-M29-A05-FROST-003` | 🔵 | Corrigido com ressalva (afirmação não verificada removida) | aula-05 |
| 14 | `GRANIT-M29-A06-GRAVIMETRIA-003` | 🔵 | Corrigido (confirmado; marca de incerteza trocada por fonte) | aula-06 |
| 15 | `GRANIT-M29-A04-SLAB-BREAKOFF-SIN-POS-005` | ⚪ | Corrigido com ressalva (as duas posições expostas) | aula-02, aula-04 |
| 16 | `GRANIT-M29-A06-FUSAO-FLUIDO-PRESENTE-006` | ⚪ | Corrigido com ressalva (as duas posições expostas) | aula-06 |

As Fontes das seis aulas também foram alteradas: as marcas "de memória / não reverificada" viraram "CONFERIDO na auditoria (2026-09-23)", porque as 57 referências conferem. Cada aula ganhou um bloco `auditoria` no fim dos metadados, e as alegações criadas pela auditoria entraram em `alegacoes_auditaveis`. O hub do módulo teve a linha "Auditoria científica" atualizada.

**Propagação:** o módulo **não tem** questionário, baralho nem glossário, porque a auditoria correu antes deles. Não há card no Anki a corrigir. Nenhum outro módulo repete os fatos corrigidos (busca por 0,708, tipo S, Whalen, Newer Granites e Iapetus em todo o curso). As latitudes dos flat slabs e a constante do Rb foram **alinhadas** aos Módulos 18 e 26, que não mudaram.

**Pendências:** nenhuma.

---

## Restrições obrigatórias para quem gerar a avaliação (questionário e flashcards)

1. **Vs depende só de μ e ρ.** Não cobrar que a onda S dependa do módulo de incompressibilidade.
2. **Granitos "alto Ba-Sr"** significa teores altos de Ba **e** de Sr. Não cobrar "razão Ba/Sr alta" como marca de manto.
3. **Pitcher tem cinco tipos** (M, I cordilheirano, I caledoniano, S herciniano, A). Não cobrar "quatro".
4. **Sm/Yb acompanha a granada e Dy/Yb acompanha o anfibólio** (Mamani et al. 2010). O anfibólio tende a **baixar** o Dy/Yb. Não cobrar os dois minerais como elevando as duas razões.
5. **Flat slabs:** Peru ~5-15°S e Pampeano ~27-33°S, como no Módulo 18.
6. **λ(⁸⁷Rb) = 1,3972 × 10⁻¹¹ a⁻¹** (IUPAC-IUGS 2015) ou 1,42 × 10⁻¹¹ (Steiger & Jäger 1977), como no Módulo 26. Não usar 1,393.
7. **Iapetus:** abriu no Ediacarano (~570-550 Ma) entre Laurentia e Báltica/oeste de Gondwana, com Avalônia na margem gondwânica, e **fechou no Siluriano**. O Rheic abriu no Ordoviciano Inicial e fechou do Devoniano ao Carbonífero.
8. **Newer Granites ~430-390 Ma**, em parte contemporâneos da colisão final. Não cobrar "sin-" ou "pós-colisional" como resposta única: Atherton & Ghani dizem sin-colisional tardio, e Neilson et al. dizem pós-colisional.
9. **Sr inicial de Chappell & White:** 0,704-0,706 (I) e > 0,708 (S). Não cobrar 0,708 como divisor simétrico.
10. **Whalen et al. (1987):** 131 amostras, alcance mundial. Não atribuir os critérios ao sudeste da Austrália. Lembrar que granitos I e S muito fracionados podem ter Ga/Al sobreposto.
11. **Chappell (1999):** granitos I e S fortemente fracionados são distinguíveis pelo P (e Y, ETR, Th). Não citar esse trabalho como prova de que o I fracionado vira "tipo S".
12. **Vielzeuf & Holloway / Patiño Douce & Johnston = sistema pelítico.** Não cobrar metagrauvaca nesses dois.
13. **Fusão com água livre × desidratação:** debate aberto (Weinberg & Hasalová 2015 × Clemens & Stevens 2015). Não cobrar "volumes pequenos" como fato fechado.
14. **Frost et al. (2001):** cobrar só a fronteira ASI = 1,0 e os três eixos. Não atribuir o 1,1 a Frost.
15. Não cobrar paginação de referências nem os valores dos exemplos hipotéticos como constantes.
