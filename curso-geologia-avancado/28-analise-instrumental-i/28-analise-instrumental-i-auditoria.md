# Auditoria científica — Módulo 28: Análise instrumental I

> [!warning] Numeração das aulas mudou depois desta auditoria
> A revisão didática de 2026-09-23 dividiu a antiga Aula 05 (arquivo `...-aula-05-fluorescencia-de-raios-x-estatistica-erros.md`) em **Aula 05** (XRF, arquivo `...-aula-05-fluorescencia-de-raios-x.md`: achados 10 e 11) e **Aula 06** (estatística e LOD/LOQ, arquivo novo `...-aula-06-estatistica-de-contagens-limites-de-deteccao.md`: achados 12 e 13). Este relatório mantém a numeração da auditoria; os `claim_id` não mudaram. O manifesto `.json` teve os caminhos atualizados.

**Curso:** geologia-avancado
**Módulo:** 28 — `28-analise-instrumental-i` (5 aulas)
**Modo:** `audit-and-fix` · **Profundidade:** `full`
**Passagens:** 1 (2026-09-23). Backup do estado antes da auditoria: `course-state.yaml.bak-20260923-pre-m28-audit`.
**Veredito:** **Aprovado após correções** — 1 vermelho, 11 laranjas e 1 amarelo levantados; todos corrigidos. Nenhum azul nem branco. Nada em aberto.

---

## Resumo por severidade

| Severidade | Levantados | Corrigidos | Em aberto |
|---|---|---|---|
| 🔴 Erro | 1 | 1 | **0** |
| 🟠 Impreciso | 11 | 11 | **0** |
| 🟡 Desatualizado / metadado | 1 | 1 | **0** |
| 🔵 Sem fonte | 0 | — | 0 |
| ⚪ Controverso | 0 | — | 0 |
| **Total** | **13** | **13** | **0** |

Gate de qualidade: **liberado** para questionário e flashcards (0 vermelhos e 0 laranjas em aberto). O módulo **não** foi fechado nesta etapa.

---

## Nota de método

A redação declarou **29 alegações auditáveis** (a01 5, a02 6, a03 5, a04 7, a05 6) e marcou como incertos a paginação de Moseley e de Walsh, a página inicial de Long & Winefordner e o fator de melhoria de sensibilidade do forno de grafite. Resultado da conferência:

- **Paginações: todas resolvidas, nenhuma errada.** Walsh (1955) *Spectrochim. Acta* 7, 108-117; Moseley (1913) *Phil. Mag.* 26(156), 1024-1034 e (1914) 27(160), 703-713; Long & Winefordner (1983) *Anal. Chem.* 55(7), **712A**-724A (registro da editora; "713A" é variante de listas secundárias). As marcas de incerteza foram retiradas e as citações completadas.
- **O fator do forno de grafite era mesmo o ponto fraco**, mas pelo motivo oposto ao sinalizado: o valor "100 a 1000 vezes" existe na literatura; o erro estava em dizer que as fontes "convergem" nele. Elas não convergem (🟠 5).
- **O único vermelho está num exemplo classificado como "hipotético"** (🔴 7), exatamente o padrão já visto no módulo 27: a narrativa era plausível, mas o mecanismo atribuído (ionização do Ca em chama ar-acetileno) não é o que domina nas condições descritas.
- **Seis dos laranjas são de atribuição ou generalização**, não de número: regra d³ creditada a Visman, "certificada pelo USGS", "fontes convergem", "a primeira técnica espectrométrica", "elemento ausente na amostra", três grandezas IUPAC que não são as três de Currie. O texto soava seguro em todos.

Ferramentas: metadados de 10 artigos conferidos na **API do Crossref** (Walsh 1955; Greenfield et al. 1964; Wendt & Fassel 1965; Houk et al. 1980; Currie 1995; Long & Winefordner 1983; Moseley 1913 e 1914; Currie 1968; Merkle et al. 2004; Yokoyama et al. 1999 localizado mas não usado); livros no **Open Library** e em páginas de editora (Pitard 1993, Potts 1987, Jeffery & Hutchison 1981, Jarvis et al. 1992, Jenkins 1999, Thompson & Walsh 1983/1989, Rollinson 1993); fontes primárias lidas por extração de texto do PDF: **Agilent, *Flame Atomic Absorption Spectrometry — Analytical Methods*, 13ª ed.** (entrada do Ca, linhas espectrais) e **USGS, BHVO-2 Reference Material Information Sheet, rev. junho 2022**.

---

## Achados

### 🟠 1. Regra da massa ∝ d³ atribuída a Visman

**claim_id:** `ANINST-M28-A01-MASSA-CUBO-DIAMETRO-002`
**Tipo:** imprecisão (atribuição)
**Onde:** Aula 01 · "Heterogeneidade de constituição e massa mínima de amostra"
**Está escrito:** "uma regra prática amplamente citada e conhecida por vários nomes (regra de Visman, "regra de amostragem" ou, em mineração, "curva de segurança de amostragem")"
**Problema:** a dependência da massa mínima com o cubo do diâmetro vem do termo d³ da fórmula do erro fundamental de **Gy**. A teoria de **Visman** (1969) é outra formulação, que decompõe a variância em um termo de heterogeneidade aleatória (A/w) e outro de segregação (B/n) e não é "a regra do cubo". A "curva de segurança" corresponde à linha de segurança dos nomogramas de amostragem de Gy.
**Correção proposta:** retirar "regra de Visman" e descrever a regra como consequência do termo d³ da fórmula de Gy, representada em mineração pela "linha de segurança" dos nomogramas.
**Fonte:** Visman, J. (1969), "A General Sampling Theory", *Materials Research & Standards* 9(11) — resumo em TRID (trid.trb.org/View/97190) e 911Metallurgist ("Visman' General Sampling Theory"); forma σ²_FSE ∝ d³/M em Zenodo 22672003 e na literatura de Gy, consultados 2026-09-23 · **Nível:** revisada por pares (Visman) / geral (resumos)
**Confiança:** confirmado

### 🟠 2. "Erros de amostragem tendem a introduzir viés sistemático, não dispersão"

**claim_id:** `ANINST-M28-A01-VIES-VS-FSE-006` (novo)
**Tipo:** imprecisão (generalização que contradiz a teoria citada)
**Onde:** Aula 01 · parágrafo de Rollinson (1993) e 4º item do Recap
**Está escrito:** "erros de amostragem — ao contrário de erros analíticos aleatórios, que aparecem como dispersão — tendem a introduzir **viés sistemático**" / "Erros de amostragem tendem a introduzir viés sistemático, não dispersão aleatória"
**Problema:** na teoria de Gy que a própria aula apresenta, o **erro fundamental de amostragem é o único componente aleatório**, com média praticamente nula: aparece como dispersão entre amostras replicadas (a aula mesmo diz, no exemplo do Au, que ele pode "tanto superestimar quanto subestimar"). O **viés** vem dos erros de amostragem *incorreta* — segregação, delimitação e extração malfeitas, como a "colherada de cima". O ponto pedagógico que vale é outro: **nenhum dos dois aparece na réplica instrumental**; só réplicas da própria etapa de amostragem os revelam. A frase também atribuía a generalização a Rollinson sem conferência.
**Correção proposta:** distinguir as duas coisas — FSE aleatório (dispersão entre duplicatas de amostragem; em elementos de grão raro, distribuição assimétrica em que a maioria das amostras pequenas subestima) e viés de amostragem incorreta — e manter a conclusão de que a réplica instrumental não revela nenhum deles.
**Fonte:** Minnitt, R. C. A., Rice, P. M. & Spangenberg, C. (2007), "Part 1: Understanding the components of the fundamental sampling error: a key to good sampling practice", *J. Southern African Inst. Min. Metall.* 107(8), 505-511 (texto lido: decomposição de Gy 1982 e Pitard 1989 do erro total em erros **aleatórios** — o erro fundamental entre eles — e erros de **viés** de delimitação, extração, pesagem e preparação, "the source of major biases" quando a amostragem correta não é praticada; o mesmo artigo registra o trabalho de Gy sobre massa mínima desde 1951), consultado 2026-09-23 · **Nível:** revisada por pares
**Confiança:** confirmado

### 🟠 3. Fusão com borato de lítio "dissolve completamente" a cromita

**claim_id:** `ANINST-M28-A02-FUSAO-FUNDENTE-LI-002`
**Tipo:** omissão que gera erro
**Onde:** Aula 02 · "Fusão com fundente"; 2º item do Recap
**Está escrito:** "ela **dissolve completamente até os minerais mais refratários** — zircão, cromita, minerais resistatos [...]" / "dissolve completamente até minerais refratários (zircão, cromita)"
**Problema:** vale para o zircão nas condições de rotina, mas a **cromita** é o caso clássico de dissolução **lenta e incongruente** em fundente de borato de lítio; material rico em cromita exige diluição muito maior, temperatura mais alta ou aditivos oxidantes. Como escrito, o aluno conclui que a fusão de rotina resolve qualquer resistato.
**Correção proposta:** manter o zircão como exemplo de sucesso e acrescentar a ressalva da cromita.
**Fonte:** Merkle, R. K. W., Loubser, M. & Gräser, P. P. H. (2004), "Incongruent dissolution of chromite in lithium tetraborate flux", *X-Ray Spectrometry* 33, 222-224, doi:10.1002/xrs.759 (Crossref, 2026-09-23); Loubser, M., dissertação *Chemical and physical aspects of lithium borate fusion*, Univ. Pretoria ("chromite-rich samples are notoriously difficult") · **Nível:** revisada por pares
**Confiança:** confirmado

### 🟠 4. BCR-2 "um basalto colunar" e materiais do USGS "certificados"

**claim_id:** `ANINST-M28-A02-MRC-EXEMPLOS-005`
**Tipo:** imprecisão (nomenclatura e estatuto metrológico)
**Onde:** Aula 02 · "Controle de qualidade", item Material de referência certificado
**Está escrito:** "certificada por um órgão como o USGS (nos EUA, materiais como BHVO-2, um basalto havaiano, ou **BCR-2, um basalto colunar**)"
**Problema:** (a) BCR = **Basalt, Columbia River**: basalto do Grupo Basalto do Rio Columbia, coletado em 1996 na pedreira Bridal Veil Flow (Oregon). "Colunar" é leitura errada da sigla. (b) A folha de informação do próprio USGS diz que o órgão **não publicou caracterização metrologicamente rastreável** do BHVO-2; os valores vêm de compilações multilaboratoriais. São materiais de referência com valores recomendados, não MRC "certificados pelo USGS" no sentido estrito.
**Correção proposta:** "BCR-2, um basalto do rio Columbia" e uma frase curta sobre o estatuto dos materiais do USGS, sem mexer no argumento (a comparação com o valor de referência continua sendo o teste de exatidão).
**Fonte:** USGS, *BHVO-2 Reference Material Information Sheet*, rev. junho 2022 (texto lido); USGS, *BCR-2 Information Sheet* 2022 (Bridal Veil Flow Quarry, 1996), consultados 2026-09-23 · **Nível:** normativa (emissor do material)
**Confiança:** confirmado

### 🟠 5. Forno de grafite: "fontes técnicas convergem" em 100 a 1000 vezes

**claim_id:** `ANINST-M28-A03-FORNO-GRAFITE-SENSIBILIDADE-003`
**Tipo:** certeza indevida (incerteza declarada pela redação)
**Onde:** Aula 03 · item Forno de grafite; nota nas Fontes
**Está escrito:** "fontes técnicas convergem numa melhoria típica da ordem de 100 a 1000 vezes no limite de detecção"
**Problema:** as fontes **não convergem**: Harvey (*Analytical Chemistry 2.1*) dá concentração no vapor "até 1000×" maior e um exemplo de Zn com ~420×; Sperling (*Encyclopedia of Analytical Chemistry*) dá limites de detecção **20 a 200 vezes** menores que os da chama; outras fontes dão 10-1000×. O que é robusto é a ordem de grandeza — **uma a três ordens**, variando com o elemento — que é justamente o que o Recap da própria aula já dizia. O corpo e o Recap estavam em desacordo.
**Correção proposta:** "melhora os limites de detecção em uma a três ordens de grandeza, conforme o elemento (as fontes dão de ~20× a ~1000×)"; nota das Fontes reescrita com as fontes nomeadas.
**Fonte:** Harvey, D., *Analytical Chemistry 2.1*, §10.4 (LibreTexts), consultado 2026-09-23; Sperling, M., "Flame and Graphite Furnace Atomic Absorption Spectrometry in Environmental Analysis", *Encyclopedia of Analytical Chemistry*, Wiley, doi:10.1002/9780470027318.a0805 · **Nível:** base de referência
**Confiança:** confirmado (a faixa; nenhum valor único)

### 🟠 6. AAS como "a primeira técnica espectrométrica de rotina", adotada "a partir do final da década de 1960"

**claim_id:** `ANINST-M28-A03-ADOCAO-AAS-HISTORICO-006` (novo)
**Tipo:** imprecisão (data e prioridade)
**Onde:** Aula 03 · "Onde AAS se encaixa no panorama deste módulo"
**Está escrito:** "A absorção atômica foi, historicamente, a primeira técnica espectrométrica de rotina amplamente adotada em laboratórios de geoquímica a partir do final da década de 1960"
**Problema:** o primeiro instrumento comercial (Perkin-Elmer 303) saiu em 1963 e as vendas cresceram exponencialmente em **1963-67**; a adoção começou em meados da década, não no fim. E a espectrografia de emissão óptica em arco (semiquantitativa) já era técnica espectrométrica de rotina em geoquímica, inclusive nos programas de exploração do USGS, de modo que "a primeira" é falso como escrito.
**Correção proposta:** "uma das primeiras técnicas instrumentais quantitativas de rotina [...] a partir de meados da década de 1960 (antes dela, a espectrografia de emissão em arco já era usada, mas de forma semiquantitativa)".
**Fonte:** CSIROpedia, "Atomic absorption spectroscopy" (Perkin-Elmer 303 em 1963; vendas 1963-67); Grimes, D. J. & Marranzino, A. P. (1968), USGS Circular 591 (espectrografia semiquantitativa em arco), consultados 2026-09-23 · **Nível:** base de referência / normativa (USGS)
**Confiança:** confirmado

### 🔴 7. Exemplo do Ca em basalto: ionização em chama ar-acetileno como causa do valor baixo

**claim_id:** `ANINST-M28-A03-INTERFERENCIA-IONIZACAO-CA-004` (cobre também `ANINST-M28-A03-EXEMPLO-CA-BASALTO-005`)
**Tipo:** erro factual (mecanismo)
**Onde:** Aula 03 · Exemplo trabalhado (Situação, Diagnóstico, Correção)
**Está escrito:** "O Ca é um elemento alcalino-terroso relativamente fácil de ionizar na temperatura de uma **chama ar-acetileno**. [...] O analista repete a medição após adicionar um excesso de cloreto de potássio ou de césio [...] O resultado corrigido concorda [...] com o valor obtido por ICP-OES."
**Problema:** numa solução de basalto em chama **ar-acetileno**, a depressão do sinal do Ca é dominada por **interferência química** de Al, Si e P (compostos refratários; Harvey mostra 100 ppm de Al derrubando a absorbância de 0,50 para 0,14). A ionização do Ca nessa chama é efeito de **5-10%**. Só adicionar K ou Cs **não** recuperaria o valor, e a conclusão do exemplo (concordância com ICP-OES) é falsa nas condições descritas. É na chama **óxido nitroso-acetileno** — a recomendada para Ca justamente porque elimina a interferência química — que "a principal interferência é a ionização do próprio cálcio", corrigida com 2000-5000 µg/mL de K. O exemplo ensinava a lição certa (viés sistemático de ionização) com a chama errada, e iria direto para uma questão de diagnóstico.
**Correção proposta:** manter o exemplo e sua lição e trocar a chama para óxido nitroso-acetileno, dizendo por quê (escolhida para evitar a interferência química de Al/Si/P que dominaria na ar-acetileno). Menor edição possível: o comprimento de onda de 422,7 nm, o supressor e a conclusão ficam.
**Fonte:** Agilent Technologies, *Flame Atomic Absorption Spectrometry — Analytical Methods*, 13ª ed., entrada "Ca (Calcium)" (texto lido: "Chemical interferences in the air-acetylene flame are pronounced [...] excess sodium or potassium causes 5–10% signal enhancement [...] In the nitrous oxide-acetylene flame the main interference is caused by ionization of calcium itself"); Harvey, *Analytical Chemistry 2.1*, §10.4, consultados 2026-09-23 · **Nível:** base de referência (manual do fabricante) + livro-texto
**Confiança:** confirmado

### 🟠 8. Padrão interno de ICP-MS "ausente na amostra natural"

**claim_id:** `ANINST-M28-A04-PADRAO-INTERNO-006`
**Tipo:** imprecisão (generalização falsa como escrita)
**Onde:** Aula 04 · "Interferências em ICP-MS", item Efeitos de matriz
**Está escrito:** "tipicamente um elemento ausente na amostra natural, como In, Rh ou Bi"
**Problema:** In e Bi **não são ausentes** em rochas: o próprio BHVO-2 tem In ≈ 0,117 mg/kg e Bi ≈ 0,015 mg/kg. O critério real é concentração natural **desprezível diante da quantidade adicionada** (e diferente entre amostras em proporção irrelevante). Rh, sim, é praticamente ausente.
**Correção proposta:** "tipicamente um elemento ausente ou em concentração natural desprezível diante da quantidade adicionada, como In, Rh ou Bi".
**Fonte:** USGS, *BHVO-2 Reference Material Information Sheet*, rev. junho 2022, Tabela 2 (texto lido), consultado 2026-09-23 · **Nível:** normativa (emissor)
**Confiança:** confirmado

### 🟡 9. Thompson & Walsh citado como "(1989/2003), Blackie/Springer"

**claim_id:** `ANINST-M28-A04-THOMPSON-WALSH-BIBLIO-008` (novo)
**Tipo:** erro de metadado bibliográfico
**Onde:** Aula 04 · Fontes
**Está escrito:** "Thompson, M. & Walsh, J. N. (1989/2003), *Handbook of Inductively Coupled Plasma Spectrometry*, Blackie/Springer — referência padrão de instrumentação ICP-OES e ICP-MS"
**Problema:** 1ª ed. Blackie 1983; 2ª ed. Blackie (EUA: Chapman & Hall) 1989, reimpressa pela Springer. Nenhuma edição de 2003 localizada (a reimpressão Viridian de 2003 é do *Handbook of ICP-MS* de Jarvis et al., não deste livro). O livro é centrado em ICP-AES; o capítulo de ICP-MS da 2ª ed. é de G. E. M. Hall.
**Correção proposta:** "(1989), 2ª ed., Blackie (1ª ed. 1983) — [...] ICP-OES, com um capítulo sobre ICP-MS (G. E. M. Hall) na 2ª edição".
**Fonte:** Open Library (edições 1983 e 1989); Springer Link, doi:10.1007/978-1-4613-0697-9 (2ª ed.); resenha da 1ª ed. em *Mineralogical Magazine* (Blackie, 1983, xii+268 pp.), consultados 2026-09-23 · **Nível:** base de indexação
**Confiança:** confirmado

### 🟠 10. Transições de valência em "luz visível e ultravioleta próxima"

**claim_id:** `ANINST-M28-A05-FAIXA-ESPECTRAL-VALENCIA-007` (novo)
**Tipo:** imprecisão (faixa numérica)
**Onde:** Aula 05 · "Uma física diferente"
**Está escrito:** "que respondem a energias relativamente baixas (luz visível e ultravioleta próxima)"
**Problema:** muitas linhas analíticas de AAS e ICP-OES estão no **ultravioleta médio e distante**, bem abaixo do UV próximo (300-400 nm): As 193,7 nm, Se 196,0 nm, Zn 213,9 nm, Cd 228,8 nm. Outras estão no visível e no infravermelho próximo (K 766,5 nm, Cs 852,1 nm).
**Correção proposta:** "(ultravioleta e visível, de ~190 a ~850 nm)".
**Fonte:** Agilent, *Flame AAS — Analytical Methods*, 13ª ed., tabelas de condições de trabalho por elemento (texto lido), consultado 2026-09-23 · **Nível:** base de referência
**Confiança:** confirmado

### 🟠 11. Efeito de absorção em XRF atribuído a "elementos de número atômico mais alto"

**claim_id:** `ANINST-M28-A05-EFEITOS-MATRIZ-003`
**Tipo:** imprecisão (modelo mental errado)
**Onde:** Aula 05 · "Efeitos de matriz em XRF", item Absorção
**Está escrito:** "elementos de número atômico mais alto na matriz podem absorver parte da radiação de fluorescência de um elemento de interesse"
**Problema:** a absorção forte ocorre quando a **borda de absorção** do elemento da matriz fica **logo abaixo** da energia da linha do analito — e, para linhas K, esse elemento costuma ter **Z menor** que o do analito. Exemplo canônico: o Cr (Z = 24; borda K 5,99 keV) absorve o Fe Kα (6,40 keV). O Ni (Z = 28) não absorve o Fe Kα: **reforça-o**. Como escrito, o texto põe o mesmo par de elementos (o mais pesado) como causador de absorção e de reforço, o contrário do que a física diz. Fica só a ressalva geral de que matrizes pesadas atenuam mais.
**Correção proposta:** reescrever o item Absorção com o critério da borda e o exemplo Cr/Fe/Ni.
**Fonte:** LUMS Physlab, "Quantitative XRF: matrix effects, corrections/influence coefficients" (texto lido: "E Cr < E Fe → absorption in Fe; E Fe < E Ni → enhancement in Fe"), a partir de Jenkins (1999), cap. de análise quantitativa, consultado 2026-09-23 · **Nível:** geral (material didático universitário) + física de bordas de absorção consolidada
**Confiança:** confirmado

### 🟠 12. LOD/LOQ: as "três grandezas" IUPAC e a cronologia Long & Winefordner → Currie

**claim_id:** `ANINST-M28-A05-LOD-LOQ-FORMULAS-005`
**Tipo:** imprecisão (atribuição normativa e cronologia)
**Onde:** Aula 05 · "Limite de detecção e limite de quantificação" (introdução, itens LOD e LOQ)
**Está escrito:** "(Currie, 1995 [...]), que definem três grandezas [...]: Branco de procedimento; LOD; LOQ" / "A convenção IUPAC mais citada define LOD como três vezes o desvio-padrão do branco" / "A **formulação original** de Long & Winefordner (1983) [...] e **mais tarde formalizada** nas recomendações Currie (1995)"
**Problema:** (a) As três grandezas de Currie (1995) são o **nível crítico L_C**, o **limite de detecção L_D** e o **limite de quantificação L_Q**. O branco é a base do cálculo, não uma das três. (b) O fator **3** é a convenção IUPAC de 1976/78 que Long & Winefordner (1983) discutiram. Em Currie (1995), com α = β = 0,05 e σ conhecido, **L_D ≈ 3,29 σ₀** e **L_Q = 10 σ_Q**. (c) Long & Winefordner não são a "formulação original": o **L_Q = 10σ** e o trio L_C/L_D/L_Q vêm de Currie (**1968**), quinze anos antes, que a recomendação de 1995 consolidou.
**Correção proposta:** manter as fórmulas didáticas (3σ e 10σ, as mais usadas em laboratório) e acertar as atribuições; branco rebaixado de "grandeza IUPAC" para "base do cálculo"; Currie 1968 nas Fontes.
**Fonte:** Crossref: Currie (1968), *Anal. Chem.* 40(3), 586-593, doi:10.1021/ac60259a007; Currie (1995), *Pure Appl. Chem.* 67(10), 1699-1723; Long & Winefordner (1983), *Anal. Chem.* 55(7), 712A-724A; Currie (1999), "Detection and quantification limits: origins and historical overview", *Anal. Chim. Acta* 391, 127-134 (L_D = 2L_C = 3,29σ_B), consultados 2026-09-23 · **Nível:** normativa (IUPAC) + revisada por pares
**Confiança:** confirmado

### 🟠 13. Exemplo do Nb: "elemento-traço leve" e saída única por ICP-MS

**claim_id:** `ANINST-M28-A05-EXEMPLO-NB-BASALTO-006`
**Tipo:** imprecisão + omissão que gera erro
**Onde:** Aula 05 · Exemplo trabalhado, "Consequência para a interpretação"
**Está escrito:** "buscar um método com LOD/LOQ mais baixos para Nb, tipicamente ICP-MS (Aula 04), que na faixa de poucos ppm costuma ter desempenho superior ao de XRF para **elementos-traço leves** incompatíveis como Nb"
**Problema:** (a) o Nb (Z = 41) não é "leve" em nenhum sentido usado em geoquímica: está entre os traços pesados que o XRF mede bem pelas linhas K, junto com Rb, Sr, Y e Zr. (b) O LOD alto do exemplo vem da **pérola fundida**, que dilui a amostra. A rotina clássica de traços por XRF usa **pastilha de pó prensado**, com LOD típico de 1-5 ppm, e isso é aplicação direta do que o módulo ensina (Aula 02: diluição do fundente piora LOD). Como escrito, o aluno conclui que XRF não serve para Nb baixo.
**Correção proposta:** retirar "leves"; apresentar duas saídas — XRF sobre pastilha prensada (sem a diluição do fundente) ou ICP-MS.
**Fonte:** Actlabs, "Pressed Pellet XRF" (LOD 1-5 ppm); Malvern Panalytical e literatura comparativa pérola × pastilha (pérola para maiores, pastilha para traços); Potts (1987), consultados 2026-09-23 · **Nível:** base de referência (laboratórios) + manual
**Confiança:** confirmado

---

## Verificado e correto

| Área | O que foi conferido |
|---|---|
| Bibliografia (Crossref) | Walsh 1955, *Spectrochim. Acta* 7, 108-117 · Greenfield, Jones & Berry 1964, *Analyst* 89(1064), 713(-720) · Wendt & Fassel 1965, *Anal. Chem.* 37(7), 920-922 · Houk, Fassel, Flesch, Svec, Gray & Taylor 1980, *Anal. Chem.* 52(14), 2283-2289 · Currie 1995, *Pure Appl. Chem.* 67(10), 1699-1723 · Long & Winefordner 1983, *Anal. Chem.* 55(7), 712A-724A · Moseley 1913, *Phil. Mag.* 26(156), 1024-1034; 1914, 27(160), 703-713 |
| Bibliografia (livros) | Pitard 1993, 2ª ed., CRC (1ª 1989) · Potts 1987, Blackie · Jeffery & Hutchison 1981, 3ª ed., Pergamon · Jarvis, Gray & Houk 1992, Blackie · Jenkins 1999, 2ª ed., Wiley, *Chemical Analysis* v. 152 · Rollinson 1993, Longman |
| Aula 01 | FSE de Gy e termo d³ (dobrar d → ×8 a massa, com os demais fatores fixos); efeito pepita; contaminação por aço (Fe, Cr, Co, Ni, Mn) e por carboneto de tungstênio (W, e também Co do ligante); segregação granulométrica ao "colherar" |
| Aula 02 | Moagem a ~85% < 75 µm (200 mesh); fundente Li₂B₄O₇/LiBO₂ ~50:50, razão 5:1-10:1, ~1000-1100 °C; HF volatiliza Si como SiF₄; LOI 900-1000 °C e ganho de massa pela oxidação de Fe²⁺; BHVO-2 = pahoehoe de 1919 do Halemaumau, Kilauea |
| Aula 03 | Walsh na CSIRO (Divisão de Química Industrial, seção de física química), patente 1954, artigo 1955; lâmpada de cátodo oco; ar-acetileno × óxido nitroso-acetileno para refratários; Ca 422,7 nm; forno de grafite 2000-3000 °C; correção de fundo por D₂ e Zeeman; La/Sr como liberadores |
| Aula 04 | Tocha de três tubos, 27/40 MHz, 6000-10000 K; histórico Greenfield 1964 / Wendt & Fassel 1965 / Houk et al. 1980 (Ames + Gray, Surrey); ⁴⁰Ar¹⁶O⁺ sobre ⁵⁶Fe⁺ (55,9349 × 55,9573 u); correção ⁸⁷Rb via ⁸⁵Rb; "diagrama TAS" para granitoides com análise química é compatível com a política de terminologia do plugin (TAS quando há química disponível) |
| Aula 05 | Lei de Moseley (√ν ∝ Z − σ; "aproximadamente proporcional" é a formulação usual); WDXRF/Bragg × EDXRF/SDD; Poisson √N e o exemplo 10 000 → 40 000 contagens (100 → 400 s); propagação em quadratura; LOD 3σ/m e LOQ 10σ/m como convenções de laboratório; Lachance-Traill e de Jongh como modelos de coeficientes de influência |

---

## Propagação

**Nenhuma propagação externa.** O módulo não tem questionário, baralho nem glossário (a auditoria correu antes deles). Nenhum card no Anki a corrigir à mão. Nenhum outro módulo do curso menciona BCR-2, Visman, Currie, Long & Winefordner ou chama ar-acetileno (busca em todo o curso). O ponto de dificuldade do hub ("LOD, LOQ e branco de procedimento são grandezas distintas") continua correto como está: afirma a distinção, não a atribui à IUPAC.

---

## Correções aplicadas

**Aplicadas em:** 2026-09-23

| # | claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|---|
| 1 | `ANINST-M28-A01-MASSA-CUBO-DIAMETRO-002` | 🟠 | Corrigido | aula-01 |
| 2 | `ANINST-M28-A01-VIES-VS-FSE-006` | 🟠 | Corrigido | aula-01 |
| 3 | `ANINST-M28-A02-FUSAO-FUNDENTE-LI-002` | 🟠 | Corrigido | aula-02 |
| 4 | `ANINST-M28-A02-MRC-EXEMPLOS-005` | 🟠 | Corrigido | aula-02 |
| 5 | `ANINST-M28-A03-FORNO-GRAFITE-SENSIBILIDADE-003` | 🟠 | Corrigido | aula-03 |
| 6 | `ANINST-M28-A03-ADOCAO-AAS-HISTORICO-006` | 🟠 | Corrigido | aula-03 |
| 7 | `ANINST-M28-A03-INTERFERENCIA-IONIZACAO-CA-004` | 🔴 | Corrigido | aula-03 |
| 8 | `ANINST-M28-A04-PADRAO-INTERNO-006` | 🟠 | Corrigido | aula-04 |
| 9 | `ANINST-M28-A04-THOMPSON-WALSH-BIBLIO-008` | 🟡 | Corrigido | aula-04 |
| 10 | `ANINST-M28-A05-FAIXA-ESPECTRAL-VALENCIA-007` | 🟠 | Corrigido | aula-05 |
| 11 | `ANINST-M28-A05-EFEITOS-MATRIZ-003` | 🟠 | Corrigido | aula-05 |
| 12 | `ANINST-M28-A05-LOD-LOQ-FORMULAS-005` | 🟠 | Corrigido | aula-05 |
| 13 | `ANINST-M28-A05-EXEMPLO-NB-BASALTO-006` | 🟠 | Corrigido | aula-05 |

Também feito, sem achado (resolução de incertezas declaradas): citações completas de Walsh (1955), Moseley (1913, 1914) e Long & Winefordner (1983, 712A) nas Fontes, com as marcas "não conferida" retiradas; Currie (1968) acrescentado às Fontes da Aula 05. Cada aula ganhou um bloco `auditoria` no fim dos metadados. Hub: registro de etapas atualizado.

**Pendências:** nenhuma.

---

## Restrições para quem gerar a avaliação (obrigatórias)

1. O exemplo do Ca por AAS usa chama **óxido nitroso-acetileno**. Na ar-acetileno, a interferência dominante sobre o Ca é **química** (Al, Si, P → corrige com La/Sr), não de ionização. Não cobrar "ionização do Ca em ar-acetileno" como causa principal.
2. Absorção em XRF: o absorvedor forte é o elemento cuja **borda** fica logo abaixo da linha do analito (Cr absorve Fe Kα; Ni reforça Fe). Não cobrar "Z mais alto absorve".
3. As três grandezas de Currie (1995) são **L_C, L_D e L_Q**. O fator 3σ é convenção IUPAC 1976/78; L_Q = 10σ vem de Currie (1968). Não cobrar Long & Winefordner como "origem" nem o branco como "grandeza IUPAC".
4. O FSE de Gy é **aleatório** (dispersão); viés vem de amostragem incorreta. A réplica instrumental não revela nenhum dos dois.
5. Fator do forno de grafite: cobrar só "uma a três ordens de grandeza", nunca um valor único.
6. BCR-2 = basalto do **rio Columbia**. Não cobrar "certificado pelo USGS".
7. Não cobrar paginação de referências nem a regra d³ como "regra de Visman".

---

## Observações fora do escopo (para a revisão didática)

- Aula 05 com ~27 min declarados e seis blocos (física de XRF, WD/ED, matriz, Poisson, propagação, LOD/LOQ) é a candidata natural a divisão; ficou mais longa com as correções 11-13.
- Aula 04: o título promete "métodos qualitativos e quantitativos", mas o corpo não trata de calibração/quantificação em ICP de forma explícita.
- O hub declara "Nenhum [pré-requisito] dentro deste curso", mas a Aula 05 remete aos Módulos 26 e 27.
