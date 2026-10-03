# Auditoria científica — Módulo 26: Geologia isotópica aplicada

**Curso:** geologia-avancado
**Módulo:** 26 — `26-geologia-isotopica-aplicada` (6 aulas)
**Modo:** `audit-and-fix` · **Profundidade:** `full`
**Passagens:** 1 (2026-09-21)
**Veredito:** **Aprovado com uma pendência azul** — 0 achados vermelhos, laranjas ou amarelos em aberto; 1 achado azul registrado como pendência que não bloqueia as etapas seguintes

---

## Resumo por severidade

| Severidade | Levantados | Corrigidos | Em aberto |
|---|---|---|---|
| 🔴 Erro | 1 | 1 | **0** |
| 🟠 Impreciso | 6 | 6 | **0** |
| 🟡 Desatualizado | 2 | 2 | **0** |
| 🔵 Sem fonte | 1 | — | **1** |
| ⚪ Controverso | 0 | — | 0 |
| **Total** | **10** | **9** | **1** |

Nenhum achado vermelho, laranja ou amarelo permanece aberto: o gate de qualidade do plugin está liberado para o questionário e para os flashcards deste módulo. A pendência azul é a ausência de uma citação primária única para duas aplicações de pesquisa ativa (δ98Mo e Δ199Hg); ela não sustenta nenhuma alegação factual do módulo e o próprio texto já declara a incerteza, por isso não bloqueia.

---

## Nota de método: este módulo veio com o risco pré-mapeado

A redação (geo-redator, 2026-09-21) entregou as 6 aulas com **47 alegações auditáveis** já declaradas nos blocos de metadados, e **marcou explicitamente 10 pontos com `INCERTEZA DECLARADA`** — paginação, listas de autores e detalhes bibliográficos citados de memória, mais dois valores numéricos. Essa lista foi o ponto de partida, não o ponto de chegada.

O resultado é instrutivo e vale registrar, porque contraria a intuição:

- **Das 10 incertezas declaradas, 8 eram falsos alarmes.** A referência estava certa como citada; o redator só não tinha conferido. Um caso (o tempo de residência do Sr no oceano) era incerteza sobre um número que a aula teve o cuidado de **não publicar**.
- **Apenas 2 das incertezas declaradas continham erro real** (o ano de York e a edição de Hoefs), e ambos são amarelos — erro de metadado bibliográfico, não de conteúdo.
- **Os 3 achados mais graves do módulo — o único vermelho e dois dos seis laranjas — estavam em trechos que a redação NÃO sinalizou como risco.** O 🔴 é uma comparação aritmética ("quase sete vezes"), o 🟠 2 é a inclinação de uma reta de regressão publicada sem ter sido regredida, e o 🟠 9 é uma frase que faz o ²³²Th parecer isótopo de urânio.

A lição de auditoria é a de sempre: o autor sinaliza o que sabe que não conferiu, e o erro se esconde exatamente no que ele achou que sabia. Auditar só a lista de incertezas declaradas deste módulo teria pego 2 achados amarelos e deixado passar o vermelho.

---

## O que foi verificado

**23 itens bibliográficos e normativos** conferidos em fonte primária ou base de indexação (ADS, ScienceDirect, DOI, Wiley, Springer, OSTI, Journal of Geology, GeoScienceWorld):

| Situação | Quantidade | Itens |
|---|---|---|
| Corretos exatamente como citados | 12 | Steiger & Jäger 1977 · Kuiper et al. 2008 · Villa et al. 2015 · DePaolo & Wasserburg 1976 · DePaolo 1981 · Bouvier et al. 2008 · Jaffey et al. 1971 · Wetherill 1956 · Hiess et al. 2012 · Albarède 2004 · Valley et al. 2005 · Dauphas & Rouxel 2006 |
| Incompletos, agora completados | 8 | Renne et al. 2010 · Renne et al. 2011 · Min et al. 2000 · Villa et al. 2020 (volume/paginação) · Ludwig/Isoplot (versão) · Fike et al. 2006 · Grotzinger et al. 2011 · McArthur et al. 2001 |
| **Factualmente errados** | **2** | **York (ano) · Hoefs (edição)** |
| Fonte normativa consultada | 1 | ICS, *International Chronostratigraphic Chart* (limite Jurássico-Cretáceo) |

**8 constantes de decaimento e razões de referência** conferidas contra a fonte primária — **todas corretas como publicadas**:

| Grandeza | Valor na aula | Fonte · situação |
|---|---|---|
| λ total ⁴⁰K | 5,543 × 10⁻¹⁰ a⁻¹ | Steiger & Jäger 1977 · ✅ |
| λβ ⁴⁰K | 4,962 × 10⁻¹⁰ a⁻¹ | Steiger & Jäger 1977 (±0,009) · ✅ |
| λε ⁴⁰K | 0,581 × 10⁻¹⁰ a⁻¹ | Steiger & Jäger 1977 (±0,004) · ✅ |
| λ total ⁴⁰K (alternativo) | 5,463 × 10⁻¹⁰ a⁻¹ | Min et al. 2000 (±0,054) · ✅ |
| λ ⁸⁷Rb | 1,3972 × 10⁻¹¹ a⁻¹ | Villa et al. 2015, IUPAC-IUGS (±0,0045) · ✅ |
| λ ¹⁴⁷Sm | 6,524 × 10⁻¹² a⁻¹ | Villa et al. 2020, IUPAC-IUGS (±0,024) · ✅ |
| λ ²³⁸U | 1,55125 × 10⁻¹⁰ a⁻¹ | Jaffey et al. 1971 · ✅ (derivado de T½ = 4,4683 Ga) |
| λ ²³⁵U | 9,8485 × 10⁻¹⁰ a⁻¹ | Jaffey et al. 1971 · ✅ (derivado de T½ = 7,0381 × 10⁸ a) |
| ²³⁸U/²³⁵U | 137,818 ± 0,045 | Hiess et al. 2012 · ✅ |

Vale destacar o caso do U-Pb: as meias-vidas **medidas** por Jaffey et al. (1971) — (4,4683 ± 0,0024) × 10⁹ e (7,0381 ± 0,0048) × 10⁸ anos — reproduzem, por ln2/T½, exatamente os dois λ publicados na Aula 05, até o último algarismo. A afirmação da aula de que este é o par de constantes mais estável do arsenal geocronológico se sustenta.

**7 exemplos numéricos trabalhados** integralmente recalculados por execução em Python (não conferidos de cabeça):

| Aula | Exemplo | Resultado |
|---|---|---|
| 01 | idade de mineral hipotético | ✅ reproduz (446,3 Ma; T½ 1,386 Ga) |
| 02 | idade K-Ar convencional | ⚠️ resultado certo (84,1 Ma), dois intermediários mal arredondados → 🟠 7 |
| 02 | fator J e idade ⁴⁰Ar/³⁹Ar | ⚠️ resultado certo (64,1 Ma), um logaritmo mal arredondado → 🟠 7 |
| 03 | isócrona Rb-Sr | ❌ inclinação e idade erradas → 🟠 2 |
| 04 | isócrona Sm-Nd e εNd(t) | ✅ reproduz (110,3 Ma; CHUR_t 0,512496; εNd −13,59) |
| 05 | idade concordante | ✅ reproduz (2613,8 Ma; ²⁰⁷Pb*/²³⁵U 12,12) |
| 05 | idade Pb-Pb por iteração | ✅ reproduz; raiz por bisseção = 2652,12 Ma |

---

## Achados

### 🔴 1. Meia-vida do ¹⁴⁷Sm declarada como "quase sete vezes" a do ⁸⁷Rb — o fator real é 2,1

**claim_id:** `ISOGEO-M26-A04-SM147-RB87-HALFLIFE-RATIO-012`
**Tipo:** erro factual (comparação aritmética)
**Onde:** Aula 04 · seção "A isócrona Sm-Nd"
**Está escrito:** "correspondendo a uma meia-vida de (106,25 ± 0,38) bilhões de anos — **quase sete vezes mais longa que a do ⁸⁷Rb**, o que faz do Sm-Nd um sistema especialmente adequado para datar eventos muito antigos"
**Problema:** o próprio módulo publica as duas meias-vidas. A do ¹⁴⁷Sm é 106,25 Ga (Aula 04); a do ⁸⁷Rb é 49,61 Ga (Aula 03, recomendação IUPAC-IUGS 2015). A razão é 106,25 / 49,61 = **2,14** — pouco mais que o dobro, não "quase sete vezes". Mesmo contra o valor clássico de Steiger & Jäger para o ⁸⁷Rb (48,81 Ga), a razão é 2,18. O erro é autocontraditório dentro do próprio módulo: um aluno que voltasse uma aula e dividisse os dois números encontraria a discrepância, e um aluno que não voltasse sairia com uma noção errada da ordem de grandeza relativa dos dois relógios. Como a frase serve de justificativa para "especialmente adequado para datar eventos muito antigos", o argumento inteiro é apresentado com um apoio quantitativo sete vezes exagerado.
**Correção aplicada:** "correspondendo a uma meia-vida de (106,25 ± 0,38) bilhões de anos — **cerca de duas vezes mais longa que a do ⁸⁷Rb (49,61 Ga, Aula 03)**, o que faz do Sm-Nd um sistema especialmente adequado..." — com o valor do ⁸⁷Rb explicitado entre parênteses, para que a comparação fique verificável no próprio parágrafo.
**Fonte:** Villa, I. M., Holden, N. E., Possolo, A., Hibbert, D. B., Ickert, R. B. & Renne, P. R. (2020), "IUPAC-IUGS recommendation on the half-lives of ¹⁴⁷Sm and ¹⁴⁶Sm", *Geochimica et Cosmochimica Acta* **285**, 70-77 (doi 10.1016/j.gca.2020.06.022); Villa, I. M., De Bièvre, P., Holden, N. E. & Renne, P. R. (2015), "IUPAC-IUGS recommendation on the half life of ⁸⁷Rb", *GCA* **164**, 382-385 (doi 10.1016/j.gca.2015.05.025). · **Nível:** normativa (força-tarefa conjunta IUPAC-IUGS) · **Versão:** recomendações de 2015 e 2020, ambas vigentes
**Confiança:** confirmado
**Também aparece em:** somente na Aula 04. O recap da Aula 04 menciona λ = 6,524 × 10⁻¹² a⁻¹ sem fazer a comparação, e não precisou de alteração.
**Desfecho:** **corrigido**

---

### 🟠 2. A inclinação da isócrona Rb-Sr publicada não é a da reta ajustada, e a idade resultante está 2,1 Ma errada — com mudança de período geológico

**claim_id:** `ISOGEO-M26-A03-EXEMPLO-ISOCRONA-CALCULO-006` (claim pré-existente, reaproveitado por tratar do mesmo alvo)
**Tipo:** inconsistência interna (valor publicado como resultado de um cálculo que não foi feito)
**Onde:** Aula 03 · "Exemplo trabalhado: construindo e resolvendo uma isócrona Rb-Sr"
**Está escrito:** "Uma **regressão linear completa** (...) para este conjunto de dados **devolve** uma inclinação de aproximadamente **0,00201** e um intercepto de aproximadamente **0,70760**." E, adiante: "$t = 0{,}002008 / 1{,}42\times10^{-11} \approx 141{,}4$ milhões de anos", com a interpretação "cristalizou há aproximadamente 141 milhões de anos (**Cretáceo Inferior**, próximo ao limite Jurássico-Cretáceo)".
**Problema:** a inclinação publicada não é a da reta de melhor ajuste dos quatro pontos dados — o bloco de metadados da própria aula admitia que os valores foram "estimados por inspeção". Regressão por mínimos quadrados sobre os pontos (0,20; 0,70800), (0,80; 0,70920), (1,50; 0,71070) e (3,00; 0,71370), recalculada nesta auditoria: Sxx = 4,3675, Sxy = 0,008910, **inclinação = 0,0020395**, **intercepto = 0,7075957**. O intercepto publicado (0,70760) está **correto**; a inclinação está errada em **1,5%**. A causa provável do erro é visível no texto: as três inclinações parciais calculadas na etapa anterior (0,00200, 0,00214, 0,00200) têm média ≈ 0,00205, e a média dos dois valores repetidos é 0,00200 — mas a inclinação de uma reta ajustada **não é** a média das inclinações parciais, porque a regressão pondera cada ponto pela distância ao centro do conjunto e os pontos extremos em x puxam a reta mais que os intermediários. Consequência propagada: com a inclinação correta, ln(1,0020395) = 0,00203742 e **t = 143,5 Ma**, não 141,4 Ma. E 143,5 Ma **não cai no Cretáceo Inferior**: o limite Jurássico-Cretáceo (base do Berriasiano) está em 143,1 ± 0,6 Ma na carta da ICS, de modo que a idade corrigida fica no Titoniano, no Jurássico Superior terminal — do outro lado da fronteira que a interpretação original citava.
**Correção aplicada:** inclinação → **0,002040**; intercepto → **0,70759**; ln(1,002040) ≈ 0,002038; **t ≈ 143,5 Ma**. A interpretação foi reescrita para "Jurássico Superior terminal (Titoniano), imediatamente acima do limite Jurássico-Cretáceo, hoje posicionado pela ICS em 143,1 ± 0,6 Ma". Foram acrescentadas duas frases: uma alertando que a inclinação ajustada não é a média das inclinações parciais (que é justamente a armadilha em que o texto original caiu, e vale ensinar), e outra observando que a incerteza analítica típica de uma isócrona real (1–2%, aqui ±1,5 a 3 Ma) é da mesma ordem da distância deste resultado ao limite cronoestratigráfico — uma idade isotópica próxima de uma fronteira raramente decide, por si só, de que lado dela o evento caiu.
**Fonte:** regressão por mínimos quadrados sobre os dados publicados na própria aula (execução em Python nesta auditoria; resíduos da reta ajustada: −2,9 × 10⁻⁶, −2,7 × 10⁻⁵, +4,5 × 10⁻⁵, −1,5 × 10⁻⁵, confirmando a colinearidade que o texto afirma). Limite Jurássico-Cretáceo: International Commission on Stratigraphy, *International Chronostratigraphic Chart* — base do Berriasiano em 143,1 ± 0,6 Ma; Titoniano 149,2–143,1 Ma (consultada 2026-09-21; não há GSSP definido para a base do Berriasiano). Método de regressão: York, D. (1968), *EPSL* **5**, 320-324. · **Nível:** normativa (ICS) + cálculo direto sobre dado publicado
**Confiança:** confirmado
**Também aparece em:** o recap da Aula 03 não cita a idade do exemplo, e não precisou de alteração. O intercepto 0,70760 aparece também na frase de interpretação petrogenética ("razão inicial de 0,70760 é intermediária"), ajustada para 0,70759 na mesma edição.
**Desfecho:** **corrigido**

---

### 🟠 3. Divergência entre as calibrações do Fish Canyon sanidine informada como 0,4–0,7%; o valor real é 0,33%

**claim_id:** `ISOGEO-M26-A02-DIVERGENCIA-PERCENTUAL-011`
**Tipo:** impreciso (magnitude exagerada em ~2×)
**Onde:** Aula 02 · seção "Onde ainda mora a incerteza: a própria calibração do relógio", e recap
**Está escrito:** "a idade de referência exata do Fish Canyon Tuff (Kuiper et al., 2008: 28,201 Ma; Renne et al., 2010–2011, com valor ligeiramente mais velho, **divergem por cerca de 0,4–0,7%**). Essa divergência afeta **toda** a escala de tempo ⁴⁰Ar/³⁹Ar sistematicamente, com diferenças de **milhares a dezenas de milhares de anos** em eventos do Cenozoico."
**Problema:** os valores concorrentes são 28,201 ± 0,046 Ma (Kuiper et al. 2008), 28,305 Ma (Renne et al. 2010) e 28,294 ± 0,036 Ma (Renne et al. 2011, revisando o próprio valor anterior em resposta a um comentário publicado). As divergências relativas a Kuiper são **0,330%** e **0,369%** — a faixa correta é 0,3–0,4%, e o limite superior publicado (0,7%) é mais que o dobro do real. A origem provável da confusão é identificável: a dispersão de ~3% que a literatura reporta (idades de 27,54 a 28,39 Ma) é a de **todas** as idades K-Ar e ⁴⁰Ar/³⁹Ar já publicadas para o Fish Canyon Tuff ao longo de décadas, não a divergência entre as duas calibrações modernas concorrentes que o texto compara. Segunda imprecisão, propagada da primeira: 0,33% de 66 Ma são ~218 mil anos, de modo que "milhares a dezenas de milhares de anos" subestima o efeito no extremo antigo do Cenozoico.
**Correção aplicada:** os três valores numéricos foram explicitados no lugar da faixa percentual solta — "Kuiper et al., 2008: 28,201 Ma; Renne et al., 2010: 28,305 Ma; Renne et al., 2011, revisando o próprio valor anterior: 28,294 ± 0,036 Ma — uma divergência de cerca de **0,3 a 0,4%** em relação a Kuiper". A frase sobre a propagação virou "diferenças de poucos milhares de anos no Quaternário, dezenas de milhares no Neogeno e até cerca de 200 mil anos perto do limite Cretáceo-Paleogeno", que é escala e não só ordem de grandeza. O recap recebeu os quatro valores (λ e idade do padrão, nas duas convenções) em vez da expressão vaga "diferenças de fração de percentual".
**Fonte:** Kuiper, K. F. et al. (2008), "Synchronizing rock clocks of Earth history", *Science* **320**(5875), 500-504; Renne, P. R., Mundil, R., Balco, G., Min, K. & Ludwig, K. R. (2010), "Joint determination of ⁴⁰K decay constants and ⁴⁰Ar*/⁴⁰K for the Fish Canyon sanidine standard, and improved accuracy for ⁴⁰Ar/³⁹Ar geochronology", *GCA* **74**(18), 5349-5367; Renne, P. R., Balco, G., Ludwig, K. R., Mundil, R. & Min, K. (2011), "Response to the comment by W. H. Schwarz et al. ...", *GCA* **75**(17), 5097-5100 (κFCs = (1,6418 ± 0,0045) × 10⁻³, λε = (0,5755 ± 0,0016) × 10⁻¹⁰ a⁻¹, λβ = (4,9737 ± 0,0093) × 10⁻¹⁰ a⁻¹, idade FCs = 28,294 ± 0,036 Ma). · **Nível:** revisada por pares · **Versão:** valores de 2008/2010/2011, ainda as duas calibrações concorrentes em uso
**Confiança:** confirmado
**Também aparece em:** recap da Aula 02 (corrigido na mesma edição). A Aula 01 menciona o processo de recomendação IUPAC/IUGS sem citar percentuais, e não precisou de alteração.
**Desfecho:** **corrigido**

---

### 🟠 6. Modo de decaimento do ³⁹Ar registrado como captura eletrônica; o ³⁹Ar decai por β⁻

**claim_id:** `ISOGEO-M26-A02-AR39-MODO-DECAIMENTO-010`
**Tipo:** erro factual (física nuclear)
**Onde:** Aula 02 · **bloco de metadados** `alegacoes_auditaveis`, claim `ISOGEO-M26-A02-METODO-AR-AR-FATOR-J-004`, campo `source`
**Está escrito:** "Meia-vida do 39Ar (aproximadamente 269 anos, **por captura eletronica**) e valor tabelado de fisica nuclear"
**Problema:** o ³⁹Ar decai por **emissão beta negativa** para ³⁹K, com energia de transição (*endpoint*) de 565 keV, classificada como decaimento β⁻ único de primeira proibição. Captura eletrônica é o modo do ramo ⁴⁰K → ⁴⁰Ar que a **mesma aula** descreve corretamente algumas seções antes; o erro parece ser contaminação por proximidade. A meia-vida está correta: 269 ± 3 anos.
**Correção aplicada:** "por emissão beta negativa", com a energia de *endpoint* e a incerteza da meia-vida acrescentadas ao registro.
**Fonte:** Stoenner, R. W., Schaeffer, O. A. & Katcoff, S. (1965), "Half-lives of Argon-37, Argon-39, and Argon-42", *Science* **148**(3675), 1325-1328; dados nucleares replicados na literatura de detectores de argônio líquido (β⁻, *endpoint* 565 keV, T½ = 269 ± 3 a, ~1 Bq/kg no argônio atmosférico). · **Nível:** revisada por pares / base de dados nucleares
**Confiança:** confirmado
**Nota de escopo — importante:** o erro estava **apenas no bloco de metadados de auditoria**, não no texto que o aluno lê. O corpo da Aula 02 diz somente "o ³⁹Ar é, ele mesmo, radioativo, mas com meia-vida de centenas de anos", o que está correto e não afirma modo de decaimento nenhum. **Nenhuma correção foi necessária no conteúdo didático.** O achado foi registrado de todo modo porque o manifesto de alegações é o que uma auditoria futura vai reler como verdade já verificada, e um erro ali envenena a verificação seguinte.
**Desfecho:** **corrigido (somente no registro; conteúdo didático não tinha o erro)**

---

### 🟠 7. Intermediários mal arredondados nos dois exemplos trabalhados da Aula 02

**claim_id:** `ISOGEO-M26-A02-ARREDONDAMENTOS-EXEMPLOS-012`
**Tipo:** inconsistência interna (aritmética de exemplo trabalhado)
**Onde:** Aula 02 · "Exemplo trabalhado 1: idade K-Ar convencional" e "Exemplo trabalhado 2: fator J e idade ⁴⁰Ar/³⁹Ar"
**Está escrito:** "λ/λε = 5,543×10⁻¹⁰ / 0,581×10⁻¹⁰ ≈ **9,541**"; "ln(1,04771) ≈ **0,04661**"; e, no exemplo 2, "ln(1,036150) ≈ **0,035506**"
**Problema:** 5,543/0,581 = 9,54045, que arredonda para **9,540**, não 9,541. ln(1,047702) = 0,046599, não 0,04661. ln(1,036150) = 0,0355119, não 0,035506 — um desvio de 1,7 × 10⁻⁴ em termos relativos. **As idades finais não mudam** com três algarismos significativos (84,1 Ma e 64,1 Ma; os valores exatos são 84,07 e 64,06 Ma), de modo que nenhuma conclusão do módulo depende disso.
**Por que foi corrigido ainda assim, e classificado como laranja e não amarelo:** um exemplo trabalhado é precisamente o material que o aluno reproduz passo a passo, com calculadora na mão. Um intermediário que não fecha na terceira casa não gera um erro de resultado — gera desconfiança no próprio cálculo, que é pior, porque o aluno não tem como saber se errou ele ou o texto. Em material autodidata, sem professor para consultar, isso custa mais que o desvio numérico.
**Correção aplicada:** 9,541 → **9,540**; ln(1,04771) ≈ 0,04661 → ln(1,04770) ≈ **0,046600**; ln(1,036150) ≈ 0,035506 → **0,035512**. As idades finais e todo o raciocínio permanecem intactos.
**Fonte:** aritmética direta sobre as equações e os dados publicados na própria aula, recalculada por execução em Python nesta auditoria. · **Nível:** cálculo verificável
**Confiança:** confirmado
**Também aparece em:** somente na Aula 02. O fator J (0,30125) e todos os outros intermediários dos dois exemplos foram reconferidos e **reproduzem corretamente** (λ·t_padrão = 0,0156318; e^x − 1 = 0,0157546; J = 0,3012358).
**Desfecho:** **corrigido**

---

### 🟠 8. Faixa de εNd atribuída a manto empobrecido não contaminado começa baixo demais

**claim_id:** `ISOGEO-M26-A04-EPSILON-DM-BAND-013`
**Tipo:** impreciso (limite de faixa numérica)
**Onde:** Aula 04 · "Exemplo trabalhado: de isócrona a εNd(t)", parágrafo de interpretação
**Está escrito:** "incompatível com uma fonte de manto empobrecido não contaminado (que, num basalto dessa idade, tipicamente mostraria εNd positivo, **entre +5 e +10**)"
**Problema:** o limite inferior é baixo demais para uma fonte **estritamente** empobrecida, que é o que a frase qualifica. A média de N-MORB atual fica em torno de εNd = +9 a +10, e valores próximos de +5 já indicam fonte levemente enriquecida (tipo E-MORB) ou algum grau de contaminação — exatamente o que a frase pretende excluir. Como o exemplo usa essa faixa para argumentar que εNd(t) = −13,6 é incompatível com manto empobrecido, um limite inferior frouxo enfraquece o próprio argumento que o parágrafo quer fazer.
**Correção aplicada:** "entre cerca de **+7 e +10** — a média de basaltos de dorsal meso-oceânica atuais fica próxima de +9 a +10", com o valor de referência explicitado para que o aluno tenha uma âncora, não só uma faixa.
**Fonte:** compilações de composição do manto empobrecido (DMM): Workman, R. K. & Hart, S. R. (2005), "Major and trace element composition of the depleted MORB mantle (DMM)", *EPSL* **231**, 53-72; Salters, V. J. M. & Stracke, A. (2004), "Composition of the depleted mantle", *Geochemistry, Geophysics, Geosystems* **5**, Q05B07; εNd médio de N-MORB próximo de +9,5, manto empobrecido de referência ≈ +10. · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** o recap da Aula 04 descreve εNd positivo como indicador de manto empobrecido sem publicar faixa numérica, e não precisou de alteração.
**Desfecho:** **corrigido**

---

### 🟠 9. Frase faz o ²³²Th parecer um isótopo de urânio

**claim_id:** `ISOGEO-M26-A05-TH232-NAO-E-URANIO-009`
**Tipo:** omissão que gera erro (referência ambígua que afirma algo falso)
**Onde:** Aula 05 · seção "Dois relógios no mesmo mineral"
**Está escrito:** "**O urânio natural tem dois isótopos radioativos** de meia-vida longa relevantes para geocronologia — ²³⁸U e ²³⁵U — e cada um decai (...). **Um terceiro isótopo, ²³²Th**, decai para ²⁰⁸Pb e constitui um sistema adicional (Th-Pb)..."
**Problema:** lido em sequência — e é assim que se lê —, "um terceiro isótopo" retoma "o urânio natural tem dois isótopos radioativos", e o texto afirma implicitamente que o ²³²Th é um terceiro isótopo de urânio. É falso: o tório é o elemento 90 e o urânio o 92, elementos químicos distintos, e a distinção importa justamente aqui, porque toda a Aula 05 se organiza em torno de "dois relógios **no mesmo elemento**, no mesmo mineral, que devem concordar". Um aluno que internalize o ²³²Th como isótopo de urânio perde o que torna o par ²³⁸U/²³⁵U especial. Este achado não estava entre as incertezas declaradas pela redação.
**Correção aplicada:** "**Um terceiro radionuclídeo de vida longa produz chumbo do mesmo modo, mas ele não é um isótopo de urânio: o ²³²Th, isótopo de tório**, decai para ²⁰⁸Pb e constitui um sistema adicional (Th-Pb)..." — a negação foi posta explicitamente porque a confusão é comum e vale desfazê-la, não só evitá-la.
**Fonte:** tabela periódica e dados nucleares básicos (Th, Z = 90; U, Z = 92); Dickin, A. P. (2005), *Radiogenic Isotope Geology*, 2ª ed., Cambridge University Press, cap. 6. · **Nível:** normativa
**Confiança:** confirmado
**Nota:** a qualificação original "dois isótopos radioativos **de meia-vida longa relevantes para geocronologia**" está **correta** e foi preservada — o urânio natural tem também o ²³⁴U, radioativo, mas de meia-vida curta (~245 ka) e membro da própria cadeia do ²³⁸U. A auditoria verificou esse ponto e não abriu achado sobre ele.
**Desfecho:** **corrigido**

---

### 🟡 4. Edição de Hoefs, *Stable Isotope Geochemistry*, citada como 8ª; a de 2021 é a 9ª

**claim_id:** `ISOGEO-M26-A06-HOEFS-EDICAO-012`
**Tipo:** desatualização (metadado bibliográfico)
**Onde:** Aula 06 · lista de fontes
**Está escrito:** "Hoefs, J. (2021), *Stable Isotope Geochemistry*, **8ª ed.**, Springer"
**Problema:** o par ano/edição não existe. A edição publicada em 2021 é a **nona** (Springer Textbooks in Earth Sciences, Geography and Environment, ISBN 978-3-030-77691-6, que declara discutir 47 elementos com variação isotópica natural resolvível); a 8ª edição é de **2018** (ISBN 978-3-319-78526-4). Este ponto estava entre as incertezas que a redação declarou.
**Correção aplicada:** "9ª ed.", mantendo o ano 2021, com a coleção e o ISBN acrescentados para desambiguar de vez.
**Fonte:** registro editorial Springer (doi do livro 10.1007/978-3-030-77692-3; ISBN 978-3-030-77691-6, 2021, 9ª edição). · **Nível:** normativa (editor)
**Confiança:** confirmado
**Desfecho:** **corrigido**

---

### 🟡 5. Regressão de York datada de 1969; o artigo é de 1968

**claim_id:** `ISOGEO-M26-A03-YORK-ANO-007` (claim novo, criado pela auditoria)
**Tipo:** desatualização (metadado bibliográfico)
**Onde:** Aula 03 · seção "Exemplo trabalhado" (menção no corpo) e lista de fontes
**Está escrito:** "o mais usado na literatura é o de **York, 1969**" e "York, D. (**1969**), 'Least squares fitting of a straight line with correlated errors', *Earth and Planetary Science Letters*, 5, 320-324"
**Problema:** a **paginação estava correta** (EPSL vol. 5, p. 320-324) — era exatamente isso que a redação pedira para conferir. O que estava errado era o **ano**: o artigo saiu no fascículo de dezembro de **1968**. NASA ADS indexa o trabalho como `1968E&PSL...5..320Y` e o identificador ScienceDirect é `S0012821X68800597`, ambos apontando 1968. Boa parte da literatura de geocronologia cita, ainda assim, "York, 1969".
**Correção aplicada:** "York, 1968" no corpo e na lista de fontes, **preservando a menção à forma "York, 1969"** na entrada bibliográfica — o aluno vai encontrar essa citação em artigos e manuais, e precisa saber que se trata do mesmo trabalho, não de um segundo artigo. Não existe um York (1969) homônimo.
**Fonte:** NASA ADS, `1968E&PSL...5..320Y`; ScienceDirect, `S0012821X68800597`; *Earth and Planetary Science Letters* vol. 5, fascículo de dezembro de 1968. · **Nível:** base de referência (indexação bibliográfica)
**Confiança:** confirmado
**Desfecho:** **corrigido**

---

### 🔵 10. Sem citação primária única para δ98Mo como proxy de oxigenação e para Δ199Hg como traçador vulcânico

**claim_id:** `ISOGEO-M26-A06-MO-HG-CITACOES-PRIMARIAS-013` (cobre também o claim `ISOGEO-M26-A06-HG-MIF-VULCANISMO-009`)
**Tipo:** evidência insuficiente
**Onde:** Aula 06 · seção "Isótopos não tradicionais: Fe, Mo e Hg como traçadores de paleorredox e de vulcanismo", e lista de fontes
**Situação:** os **mecanismos** descritos foram reconfirmados nesta auditoria — adsorção seletiva de Mo isotopicamente leve em óxidos de manganês, com δ98Mo da água do mar moderna em torno de +2,3‰; fracionamento independente de massa do Hg nos isótopos ímpares (¹⁹⁹Hg, ²⁰¹Hg) por via fotoquímica; picos de Hg sedimentar associados a províncias ígneas gigantes. O que **não** foi possível é eleger uma citação primária única e definitiva para nenhuma das duas aplicações. São campos de pesquisa ativa com artigos concorrentes: no caso do Hg no limite Permiano-Triássico, há literatura sustentando que as excursões negativas de Δ199Hg não se explicam apenas por vulcanismo ou erosão terrestre, exigindo fracionamento adicional por fotorredução marinha sob euxinia de zona fótica — ou seja, o mecanismo em si segue em disputa.
**Conduta adotada:** conforme a política de achado azul, **nenhuma citação foi inventada** e **nenhuma afirmação foi removida**. A incerteza foi tornada explícita na lista de fontes da aula, marcada como achado azul em aberto. O corpo da aula já declarava as duas aplicações como "área de pesquisa ativa, com mecanismos ainda debatidos", de modo que nenhuma certeza indevida está sendo ensinada — o que falta é a âncora bibliográfica, não a ressalva epistêmica.
**Por que não bloqueia as etapas seguintes:** nenhuma alegação factual do módulo depende desta pendência, e o gate do plugin trava em achados vermelhos e laranjas. Um questionário ou flashcard sobre este trecho pode cobrar o mecanismo (confirmado) sem cobrar atribuição bibliográfica.
**Encaminhamento:** registrado em `open_findings` no `course-state.yaml`; deve ser revisitado na revisão final do curso ou quando o Módulo 27 (petrocronologia) tocar literatura adjacente.
**Confiança:** não verificado (quanto à citação; o mecanismo está confirmado)
**Desfecho:** **não corrigido (aguarda decisão)**

---

## Verificado e correto

Auditoria que não mostra o que olhou não vale o arquivo que ocupa. Os pontos abaixo foram verificados e **passaram sem alteração**:

**Física e matemática do decaimento (Aula 01).** Dedução de dN/dt = −λN para N = N₀e^(−λt); t½ = ln2/λ; equação geral da idade t = (1/λ)ln(1 + D*/P). Conversão do λ do ⁴⁰K em meia-vida reconferida: 0,6931/5,543 × 10⁻¹⁰ = 1,2504 × 10⁹ anos, consistente com o 1,25 Ga tabelado. As quatro premissas (sistema fechado, filho inicial determinável, λ bem calibrada, razão medida com exatidão) estão corretamente enunciadas e nenhuma é apresentada como garantida pela física.

**Espectrometria de massa (Aula 01).** Separação por m/z com raio de curvatura proporcional a √(m/z) — correto para setor magnético após aceleração por tensão fixa. Ionização térmica sobre filamento de Ta ou Re; plasma de argônio a ~6.000–10.000 K; copos de Faraday para corrente e multiplicadores de elétrons para feixes fracos; vantagem da multicoleção no cancelamento de instabilidade temporal do feixe. Diferenças de massa relativa reconferidas: ⁸⁷Sr–⁸⁶Sr = 1/86 = 1,16% ("cerca de 1,2%", correto); ⁵⁶Fe–⁵⁴Fe = 2/55 = 3,64% ("cerca de 3,6%", correto).

**Decaimento ramificado do ⁴⁰K (Aula 02).** Os três valores de Steiger & Jäger conferidos individualmente contra a fonte primária: λβ = (4,962 ± 0,009) × 10⁻¹⁰, λε = (0,581 ± 0,004) × 10⁻¹⁰, λ total = (5,543 ± 0,010) × 10⁻¹⁰ a⁻¹, soma exata. Razão de ramificação λε/λ = 10,48%, coerente com o "cerca de 10,5%" e "cerca de 89,5%" da aula. Abundâncias isotópicas do potássio (³⁹K 93,26%, ⁴¹K 6,73%, ⁴⁰K 0,0117%) somam 100,0017% por arredondamento dos valores tabelados (93,2581 / 6,7302 / 0,0117), sem erro. Reação de irradiação ³⁹K(n,p)³⁹Ar, fator J, critérios de platô (≥50% do ³⁹Ar liberado, concordância em 2σ, sinalizados como convenção e não regra universal) e a assinatura em U/escada ascendente de perda parcial de argônio: todos corretos.

**Uma armadilha de convenção que a aula evitou (Aula 02).** Parte da literatura reporta, para Steiger & Jäger, uma "razão de ramificação" de 0,1171 — que é λε/λ**β** (0,581/4,962), não λε/λ**total**. As duas definições circulam com o mesmo nome e trocá-las erra o resultado em 12%. A aula usa, corretamente e de forma explícita, a fração do decaimento total ("de cada 100 átomos de ⁴⁰K que decaem, cerca de 10 ou 11 produzem ⁴⁰Ar").

**Isócrona Rb-Sr (Aula 03).** Equação, papel do ⁸⁶Sr como normalizador não radiogênico, condição de cogeneticidade, significado geométrico de inclinação e intercepto. Meias-vidas reconferidas: ln2/1,3972 × 10⁻¹¹ = 49,610 Ga e ln2/1,42 × 10⁻¹¹ = 48,813 Ga; diferença percentual entre as duas constantes = 1,632% ("cerca de 1,6%", correto). Faixas de razão inicial (manto 0,702–0,706; crosta antiga >0,710, podendo exceder 0,720) e as duas armadilhas — isócrona de mistura e re-homogeneização metamórfica com preservação da isócrona de rocha total — corretas.

**CHUR, εNd e idade-modelo (Aula 04).** (¹⁴³Nd/¹⁴⁴Nd)_CHUR,0 = 0,512638 e (¹⁴⁷Sm/¹⁴⁴Nd)_CHUR = 0,1967 (DePaolo & Wasserburg 1976), com o refinamento de 0,1960 corretamente atribuído a condritos não equilibrados (Bouvier et al. 2008, que também dá 143/144 = 0,512630 ± 11). Fórmula do εNd, sinal da interpretação (Nd mais incompatível que Sm, logo extração de magma eleva Sm/Nd do manto residual), distinção entre idade-modelo e idade isocrônica, e a ressalva de que a curva de DePaolo (1981) não é linear e que a aula usa simplificação didática declarada: tudo correto. Meia-vida do ¹⁴⁷Sm reconferida: ln2/6,524 × 10⁻¹² = 106,246 Ga.

**U-Pb, concórdia e Pb-Pb (Aula 05).** Cadeia de decaimentos intermediários em equilíbrio secular tratada como passo único; atribuição do diagrama a Wetherill (1956); curva não retilínea por causa da diferença entre λ238 e λ235; interceptos superior e inferior da discórdia; propriedades do zircão (incorpora U e exclui Pb por incompatibilidade de raio iônico e valência no sítio do Zr, resistência a intemperismo e metamorfismo de grau baixo a médio, zonamento visível por catodoluminescência datável por SIMS/LA-ICP-MS); caráter transcendental da equação Pb-Pb; modelo de Holmes-Houtermans. Os dois exemplos trabalhados reproduzem exatamente, inclusive a raiz iterativa (2652,12 Ma por bisseção contra 2,652 Ga publicado).

**Isótopos estáveis (Aula 06).** Notação δ em partes por mil; padrões VSMOW, VPDB, VCDT e AIR, com as origens históricas corretas (VPDB de belemnite fóssil da Formação Pee Dee; VCDT da troilita, FeS, do meteorito de ferro Canyon Diablo); distinção equilíbrio (dependente de T, base da geotermometria) versus cinético (irreversível, maior, dependente da taxa); discriminação fotossintética contra ¹³C. Enxofre tem quatro isótopos estáveis (correto); faixas de δ34S magmático (0 ± 2‰) e de redução bacteriana de sulfato (−10 a −40‰ ou mais negativo) consistentes com a literatura. δ18O mantélico de zircão 5,3 ± 0,3‰ VSMOW (Valley et al. 2005) confirmado. Uniformidade global do ⁸⁷Sr/⁸⁶Sr oceânico por residência ≫ tempo de mistura: correto, e a aula teve o cuidado de **não** publicar um valor numérico para a residência, de modo que a incerteza que a redação declarou sobre esse número não corresponde a nenhuma alegação publicada. Excursão de Shuram-Wonoka como maior e mais prolongada anomalia negativa de δ13C conhecida, com δ13Ccarb até ~−12‰ VPDB e mecanismo em debate: confirmado, e a citação primária que faltava foi identificada (Fike et al. 2006; revisão em Grotzinger et al. 2011). Mercúrio tem sete isótopos estáveis (correto). δ98Mo da água do mar moderna ~+2,3‰ confirmado.

**Coerência entre aulas.** Nenhuma contradição encontrada entre as seis aulas após as correções. A cadeia conceitual — equação geral da idade (A01) → ramificação (A02) → isócrona (A03) → isócrona + notação ε + idade-modelo (A04) → dois relógios simultâneos (A05) → fracionamento em vez de decaimento (A06) — é consistente, e as referências cruzadas entre aulas apontam para conteúdo que existe. O λ do ⁴⁰K citado na Aula 01 é o mesmo da Aula 02; a meia-vida do ⁸⁷Rb da Aula 03 é a usada na comparação corrigida da Aula 04.

---

## Observação fora do escopo desta auditoria

Um item didático, registrado aqui em uma linha e **não** contado como achado factual, para a revisão didática tratar: a Aula 03 tem a grafia "uma mesma **suíce** ígnea" onde se lê "suíte". Erro de digitação, sem efeito sobre a correção científica.

---

## Correções aplicadas

**Aplicadas em:** 2026-09-21 (mesma sessão da auditoria; modo `audit-and-fix`)

| claim_id | Sev. | Desfecho | Arquivos alterados |
|---|---|---|---|
| `ISOGEO-M26-A04-SM147-RB87-HALFLIFE-RATIO-012` | 🔴 | Corrigido | aula-04 (corpo + metadados) |
| `ISOGEO-M26-A03-EXEMPLO-ISOCRONA-CALCULO-006` | 🟠 | Corrigido | aula-03 (corpo, fontes + metadados) |
| `ISOGEO-M26-A02-DIVERGENCIA-PERCENTUAL-011` | 🟠 | Corrigido | aula-02 (corpo, recap, fontes + metadados) |
| `ISOGEO-M26-A02-AR39-MODO-DECAIMENTO-010` | 🟠 | Corrigido (só no registro) | aula-02 (metadados) |
| `ISOGEO-M26-A02-ARREDONDAMENTOS-EXEMPLOS-012` | 🟠 | Corrigido | aula-02 (dois exemplos + metadados) |
| `ISOGEO-M26-A04-EPSILON-DM-BAND-013` | 🟠 | Corrigido | aula-04 (corpo + metadados) |
| `ISOGEO-M26-A05-TH232-NAO-E-URANIO-009` | 🟠 | Corrigido | aula-05 (corpo + metadados) |
| `ISOGEO-M26-A06-HOEFS-EDICAO-012` | 🟡 | Corrigido | aula-06 (fontes + metadados) |
| `ISOGEO-M26-A03-YORK-ANO-007` | 🟡 | Corrigido | aula-03 (corpo, fontes + metadados, claim novo) |
| `ISOGEO-M26-A06-MO-HG-CITACOES-PRIMARIAS-013` | 🔵 | **Aguarda decisão** | aula-06 (fontes: incerteza explicitada) |

**Além das correções, 10 incertezas declaradas pela redação foram investigadas e resolvidas**, com 8 referências bibliográficas completadas ou identificadas pela primeira vez (Renne et al. 2010 e 2011, Min et al. 2000, Villa et al. 2020, Ludwig/Isoplot 3.75, Fike et al. 2006, Grotzinger et al. 2011, McArthur et al. 2001) e 12 confirmadas exatamente como estavam. Os blocos `alegacoes_auditaveis` das seis aulas registram, alegação por alegação, o que foi verificado, com que fonte e com que resultado.

**Material derivado:** nenhum. O módulo 26 **não tem** questionário nem baralho de flashcards gerados — é justamente por isso que a auditoria roda antes deles. Nenhuma propagação para material de avaliação foi necessária, e os erros corrigidos (em especial o 🔴 da Aula 04 e a idade da isócrona da Aula 03) **não chegaram a virar gabarito nem verso de card**. Nada foi importado no Anki, portanto não há aviso de reimportação a dar.

**Pendências:** uma, o achado azul 10 (citação primária para δ98Mo e Δ199Hg). Não bloqueia questionário nem flashcards.

---

## Rastreabilidade

- **Manifesto estruturado:** `26-geologia-isotopica-aplicada-auditoria.json`, ao lado deste arquivo.
- **Registro por alegação:** blocos `alegacoes_auditaveis` em comentário HTML no fim de cada uma das 6 aulas, com **55 alegações rastreadas** (47 declaradas na redação + **8 criadas pela auditoria**): a01 5, a02 12, a03 7, a04 9, a05 9, a06 13. *Correção de contabilidade, 2026-09-22:* esta linha dizia "48 alegações (47 + 1)". A contagem em disco desmente esse número — o relatório rotulou explicitamente como "claim novo" apenas o `ISOGEO-M26-A03-YORK-ANO-007`, mas a mesma passagem criou outros sete (`A02-AR39-MODO-DECAIMENTO-010`, `A02-DIVERGENCIA-PERCENTUAL-011`, `A02-ARREDONDAMENTOS-EXEMPLOS-012`, `A04-SM147-RB87-HALFLIFE-RATIO-012`, `A04-EPSILON-DM-BAND-013`, `A06-HOEFS-EDICAO-012`, `A06-MO-HG-CITACOES-PRIMARIAS-013`) sem rotulá-los como tais. Os claims `A03-EXEMPLO-ISOCRONA-CALCULO-006` e `A05-TH232-NAO-E-URANIO-009` eram pré-existentes e foram reaproveitados. Nenhum achado, severidade ou correção muda por causa disso: é erro de contabilidade de manifesto, não de conteúdo auditado.
- **Estado do curso:** bloco `audit` do módulo 26 em `course-state.yaml`.
- **Ambiente de cálculo:** Python 3.13.2 (`math` da biblioteca padrão; regressão por mínimos quadrados e bisseção implementadas diretamente, sem dependências externas).
- **Data da consulta às fontes normativas:** 2026-09-21. Recomendações IUPAC-IUGS vigentes: ⁸⁷Rb (2015) e ¹⁴⁷Sm/¹⁴⁶Sm (2020). Carta ICS consultada para o limite Jurássico-Cretáceo em 143,1 ± 0,6 Ma.
