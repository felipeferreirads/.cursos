# Auditoria científica — Módulo 30: Petrologia de kimberlitos e carbonatitos e mineralizações associadas

**Curso:** geologia-avancado
**Módulo:** 30 — `30-kimberlitos-carbonatitos` (6 aulas)
**Modo:** `audit-and-fix` · **Profundidade:** `full`
**Passagens:** 1 (2026-09-23). Backup do estado antes da auditoria: `course-state.yaml.bak-20260923-pre-m30-audit` (idêntico byte a byte ao estado no início desta passagem).
**Veredito:** **Aprovado após correções**. Foram levantados 4 vermelhos, 7 laranjas, 1 amarelo e 2 azuis, e todos foram tratados nas aulas. Nada ficou em aberto. Não houve achado branco (controverso): os pontos genuinamente em disputa (contínuo carbonatito-kimberlito, rotas de geração de carbonatito, transição magma-brine, origem de Bayan Obo e do carbonado, captura de diamante em Argyle) já estavam apresentados como debate.

---

## Resumo por severidade

| Severidade | Levantados | Corrigidos / tratados | Em aberto |
|---|---|---|---|
| 🔴 Erro | 4 | 4 | **0** |
| 🟠 Impreciso | 7 | 7 | **0** |
| 🟡 Desatualizado | 1 | 1 | **0** |
| 🔵 Sem fonte | 2 | 2 (ambos confirmados com fonte e reescritos com o valor verificado) | 0 |
| ⚪ Controverso | 0 | — | 0 |
| **Total** | **14** | **14** | **0** |

Gate de qualidade: **liberado** para o questionário e os flashcards (0 vermelhos e 0 laranjas em aberto), com as restrições listadas no fim. O módulo **não** foi fechado nesta etapa.

### Inversões de sentido

Dois vermelhos são **inversões**, do tipo que já apareceu em módulos anteriores e que iria direto para uma questão de verdadeiro/falso ou para o verso de um flashcard:

- **🔴 4 (Aula 04):** "carbonatitos são muito mais numerosos" que kimberlitos. É o contrário: kimberlitos somam alguns milhares de corpos; carbonatitos, cerca de 600 ocorrências.
- **🔴 2 (Aula 03):** "nas descrições modernas é o corpo que se chama tuffisítico". É o contrário: "brecha kimberlítica tuffisítica" é o nome **antigo**; o moderno (Scott Smith et al., 2013) é "kimberlito piroclástico do tipo Kimberley".

O **🔴 1** (fronteira grafite-diamante) não é uma inversão, mas é o mais perigoso para a avaliação. A equação estava errada, e o exemplo trabalhado colocava a entrada do diamante a **95 km**, profundidade irreal para o manto cratônico, onde ela fica perto de **150 km**. Uma questão de cálculo feita sobre a aula cobraria esse número.

---

## Nota de método

A redação declarou **26 alegações auditáveis** (a01 4, a02 4, a03 5, a04 4, a05 4, a06 5). A auditoria criou mais 8: sete nos metadados das aulas (a01 +1, a03 +3, a04 +2, a06 +1) e uma de módulo (`KIMB-M30-MOD-BIBLIO-001`). O total rastreado é **34**, e **33** estão declaradas nos arquivos, contadas por script sem `claim_id` duplicado. A redação e marcou como "de memória" ou "não conferido" boa parte da bibliografia e das datas.

| Ponto marcado pela redação | Resultado |
|---|---|
| Limiares IUGS do carbonatito (>50 % carbonato, <20 % SiO₂; corte 0,8; MgO contra FeO + Fe₂O₃ + MnO) | **Conferem** (Le Maitre, 2002; Woolley e Kempe, 1989, reproduzidos em Simandl e Paradis, 2018, que também dão o silicocarbonatito acima de 20 % de SiO₂ e a base em % peso). A aritmética do exemplo A-D confere (0,85 e 0,59). |
| Datas históricas (Lewis 1887; Brøgger 1921; Niggli 1923; Argyle; Dawson 1962) | Lewis 1887, Brøgger 1921, Niggli 1923 e Dawson 1962 **conferem**. Argyle foi descoberto em 1979, e a **idade** dada no texto (~1,2 Ga) está **desatualizada** (🟡 12). |
| Grupos I e II, orangeíto | O esquema geral confere, mas as **atribuições** estão trocadas: quem nomeou os Grupos I e II foi Smith (1983), e o termo "orangeíto" é de Wagner (1928), retomado por Mitchell (🟠 6). |
| Fronteira grafite-diamante de Kennedy e Kennedy (1976) | **Não confere.** A reta de Kennedy e Kennedy é P (kbar) = 19,4 + T(°C)/40. A reta do texto, 7,1 + 0,027 T, é a extrapolação de Berman e Simon (1955), com T em **kelvin** (🔴 1). |
| Quilha cratônica (150-250 km, Fo 92-93, ~40 mW/m²) | **Confere** como ordem de grandeza (Pollack e Chapman, 1977; Jordan, 1978; Pearson et al., 2014). |
| MARID, PIC, modelo de veios, contínuo carbonatito-kimberlito | **Conferem** (Dawson e Smith, 1977; Foley, 1992; Wyllie e Huang, 1975; Dalton e Presnall, 1998). |
| Fácies de pipe e minerais indicadores | O modelo de três fácies **confere para os pipes do tipo Kimberley**, mas foi apresentado como universal e atribuído a Scott Smith et al. (2013), que dizem outra coisa (🟠 7). O nome "tuffisítico" estava **invertido** (🔴 2). A textura em **atol** estava definida errado (🔴 3). O limiar G10 era "ilustrativo" e foi **conferido** no artigo original (🔵 13). |
| Faixas isotópicas Grupo I e orangeíto | Grupo I confere em Sr. O **limite inferior do Sr do orangeíto** (0,705) está baixo demais, e a faixa de εNd do Grupo I estava deslocada para negativo, o que tornava ambígua a amostra 1 do exemplo (🟠 5). |
| Ascensão de kimberlito (m/s; Russell et al., 2012) | **Confere**: Sparks et al. (2006) estimam de mais de 4 a 20 m/s; Russell et al. (2012) conferem (Nature 481, 352-356). |
| Sequência calcita → dolomita → ferrocarbonato; transição magma-brine | **Confere** como tendência geral e como debate. A fonte "PubMed 37467324" foi identificada: Yuan et al. (2023), *Science Advances* 9, eadh0458 (🟠 11). |
| APIP, complexos, Braúna, Juína | **Conferem**: ~85 Ma e >15.000 km³ (Gibson et al., 1995); área de ~25.000 km² e os seis complexos (literatura da USP); Braúna 642 ± 6 Ma (Donatti-Filho et al., 2013) e primeira mina de diamante em kimberlito da América do Sul; Juína (Kaminsky et al., 2001). |
| Dados de mina (Argyle 2020, Ekati 1998, Orapa 1967, Nb do Brasil) | Argyle fechou em novembro de 2020, Ekati abriu em 14/10/1998 e Orapa foi descoberto em 01/03/1967: **conferem**. "Grandes pipes de **baixo teor**" para Orapa **não confere** (🟠 10). O Nb brasileiro é **~93 %** da produção mineira mundial (USGS, MCS 2026) (🔵 14). |
| Referências "de memória" | **Todas as 47 referências distintas foram conferidas** (Crossref para os artigos; catálogo da editora e literatura secundária para livros e anais). Havia **quatro problemas bibliográficos**, agrupados em 🟠 11: o ano de Janse (1994, e não 1992), a lista de autores incompleta de Scott Smith et al. (2013), e duas fontes sem autoria identificada (Sarkar et al., 2023; Yuan et al., 2023). Nenhuma paginação ou volume estava errado. |

**Padrão dominante.** É o mesmo dos módulos 27-29. Os erros graves **não estavam na lista de risco da redação**: a definição de atol, o nome tuffisítico e o número de ocorrências foram escritos como fatos seguros. A exceção é a equação grafite-diamante, que a redação marcou como "de memória". As faixas e datas que a redação marcou como incertas, em geral, conferiram.

**Ferramentas:** metadados na **API do Crossref** (47 referências). Resumos na **API do OpenAlex**: Gibson et al. 1995, Simandl e Paradis 2018, Sarkar et al. 2023, Yuan et al. 2023, Olierook et al. 2023, Humphreys-Williams e Zahirovic 2021, Liu et al. 2023, Giuliani e Pearson 2019. **Texto integral lido**: Scott Smith et al. (2013), PDF da UBC; Grütter et al. (2004), PDF da SRK; Simandl e Paradis (2018), PDF do INGEMMET. Buscas na web para Kennedy e Kennedy (1976), Berman e Simon (1955), a textura em atol, a contagem de kimberlitos e carbonatitos, Smith (1983), Wagner (1928), Skinner (1989), Janse (1994), jacupiranguito, Orapa, USGS Nb, APIP, Argyle, Ekati e Lewis (1887).

---

## Achados

### 🔴 1. Fronteira grafite-diamante: equação de Berman e Simon (T em K) atribuída a Kennedy e Kennedy com T em °C

**claim_id:** `KIMB-M30-A02-GRAFITE-DIAMANTE-002` (também cobre `KIMB-M30-A02-EXEMPLO-GEOTERMAS-004`)
**Tipo:** erro factual
**Onde:** Aula 02 · "Geotermas e o campo de estabilidade do diamante" e "Exemplo trabalhado"
**Está escrito:** "P (kbar) ≈ 7,1 + 0,027 · T (°C) (Kennedy e Kennedy, 1976)" e, no exemplo, "**z ≈ 95 km**. A essa profundidade, T = [...] 875 °C" e "**z ≈ 153 km**".
**Problema:** A reta de Kennedy e Kennedy (1976), medida entre 1100 e 1625 °C, é **P (kbar) = 19,4 + T(°C)/40** (= 19,4 + 0,025 T). A reta 7,1 + 0,027 T é a extrapolação de **Berman e Simon (1955)**, com T em **kelvin**. Usada com T em °C, ela põe a fronteira cerca de 10 kbar abaixo, ou uns 30 km mais rasa. Com ela, o exemplo dava diamante estável a 95 km e 875 °C num cráton, o que é irreal: a entrada da janela do diamante em geotermas cratônicas fica perto de 140-150 km. A geoterma "quente" do exemplo (T = 800 + 5z) também não serve com a reta correta, porque chegaria à fronteira só perto de 200 km e 1800 °C, acima da temperatura do manto convectivo. A frase "Acima da curva (pressões mais baixas...)" só vale num gráfico com a profundidade crescendo para baixo, e foi reescrita sem "acima" e "abaixo".
**Correção proposta:** Reta de Kennedy e Kennedy correta, com uma nota sobre a de Berman e Simon (T em K). Recalcular o exemplo: na geoterma cratônica, **z ≈ 149 km, T ≈ 1145 °C, P ≈ 4,8 GPa**. A geoterma quente passa a ser T = 1100 + 5(z − 100), 200 °C mais quente em qualquer profundidade, e dá **z ≈ 174 km, T ≈ 1470 °C**, já na ordem da temperatura do manto convectivo (janela estreita ou nula). A diferença passa de "58 km" para "~25 km", mais a temperatura. O "O que fixar" também foi ajustado.
**Fonte:** Kennedy e Kennedy (1976), *JGR* 81, 2467-2470, doi:10.1029/JB081i014p02467 (resumo: "P = 19.4 + T/40 kbar", 1100-1625 °C). Berman e Simon (1955), *Z. Elektrochem.* 59, 333-338, doi:10.1002/bbpc.19550590503 ("P(kbar) = 7,1 + 0,027 T(K)", acima de 1200 K). · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** só na Aula 02 (texto, exemplo, recap indireto e alegação 002/004). Não há outro módulo com a equação.

### 🔴 2. "Nas descrições modernas é o corpo que se chama tuffisítico" (inversão antigo/moderno)

**claim_id:** `KIMB-M30-A03-TUFFISITICO-006` (criado pela auditoria)
**Tipo:** erro factual (nomenclatura invertida)
**Onde:** Aula 03 · "Kimberlitos: a forma do corpo e as três fácies", item 2
**Está escrito:** "Nas descrições modernas é o corpo que se chama tuffisítico."
**Problema:** É o contrário. "Brecha kimberlítica tuffisítica" (TKB) é o nome **tradicional** do preenchimento do diatrema. Scott Smith et al. (2013) o substituíram por **kimberlito piroclástico do tipo Kimberley (KPK)**, "formerly tuffisitic kimberlite". Um flashcard sobre a aula ensinaria o nome antigo como moderno.
**Correção proposta:** "Na terminologia tradicional essa rocha se chamava brecha kimberlítica tuffisítica (TKB); na de Scott Smith et al. (2013), passou a se chamar kimberlito piroclástico do tipo Kimberley (KPK), e 'tuffisítico' ficou como nome antigo."
**Fonte:** Scott Smith et al. (2013), *Proc. 10th IKC* vol. 2, 1-17, doi:10.1007/978-81-322-1173-0_1, resumo e texto integral. · **Nível:** normativa (terminologia de referência da comunidade)
**Confiança:** confirmado
**Também aparece em:** recap da Aula 03 (reescrito para dizer o nome moderno e o antigo).

### 🔴 3. Textura em atol definida como "espinélio circundando um grão de olivina ou de perovskita"

**claim_id:** `KIMB-M30-A03-ATOL-007` (criado pela auditoria)
**Tipo:** erro factual (definição)
**Onde:** Aula 03 · "Kimberlitos: mineralogia e a distinção macrocristal versus matriz", item Fenocristais e matriz
**Está escrito:** "Textura típica: **atol** (espinélio circundando um grão de olivina ou de perovskita)."
**Problema:** No espinélio em atol, o **núcleo** é o espinélio (magnesiochromita zonada ou espinélio magnesiano titanífero, MUM). Uma zona de silicato ou carbonato (serpentina, calcita) o separa de uma **borda fina de magnetita**, como a lagoa entre a ilha e o recife. Não é espinélio em volta de olivina ou perovskita.
**Correção proposta:** "Textura típica: **espinélio em atol**: um núcleo de espinélio (magnesiochromita ou espinélio titanífero magnesiano), separado por uma zona de serpentina ou calcita de uma borda fina de magnetita, como o anel de um atol em volta da lagoa."
**Fonte:** Roeder e Schulze (2008), "Crystallization of groundmass spinel in kimberlite", *J. Petrol.* 49, 1473-1495, doi:10.1093/petrology/egn034. Descrições convergentes em trabalhos sobre Benfontein e outros kimberlitos ("euhedral cores of zoned magnesiochromite surrounded by concentric zones of silicate material, in turn surrounded by magnetite"). · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** a Aula 05 cita "as texturas de atol mostram cristalização precoce e reação", o que é **compatível** com a definição correta (núcleo precoce, reabsorção, borda tardia). Não precisou de alteração.

### 🔴 4. "Carbonatitos são muito mais numerosos" que kimberlitos (inversão)

**claim_id:** `KIMB-M30-A04-NUMERO-OCORRENCIAS-005` (criado pela auditoria)
**Tipo:** erro factual (inversão de sentido)
**Onde:** Aula 04 · "Kimberlito e carbonatito: contínuo ou linhagens separadas?", segundo parágrafo
**Está escrito:** "carbonatitos são muito mais numerosos (várias centenas de ocorrências conhecidas; o número exato depende do catálogo e é de memória), aparecem em riftes e plumas, enquanto kimberlitos tendem a se concentrar em crátons."
**Problema:** A relação é a **inversa**. As compilações globais têm alguns **milhares** de kimberlitos: ~3.500 em Giuliani e Pearson (2019), mais de 5.000 em bases mais amplas, e 5.652 na base usada por Liu et al. (2023). Carbonatitos são **~600**: 527 em Woolley e Kjarsgaard (2008), 594 em Liu et al. (2023) e 609 em Humphreys-Williams e Zahirovic (2021). A segunda metade da frase também simplifica demais. Carbonatitos são sobretudo **continentais** (88 % em contexto cratônico no sentido amplo, segundo Simandl e Paradis, 2018), e **75 % ficam a menos de 600 km da borda de um cráton** (Humphreys-Williams e Zahirovic, 2021). Não são exclusivos de riftes e plumas.
**Correção proposta:** "kimberlitos são muito mais numerosos (alguns milhares de corpos conhecidos, em geral agrupados em campos) que carbonatitos (cerca de 600 ocorrências; 609 na compilação de Humphreys-Williams e Zahirovic, 2021), e os dois se distribuem de forma diferente: os kimberlitos diamantíferos concentram-se no interior de crátons antigos, enquanto os carbonatitos aparecem sobretudo em contextos continentais extensionais, riftes e grandes províncias ígneas, e três quartos deles ficam a menos de 600 km da borda de um cráton."
**Fonte:** Humphreys-Williams, E. R. & Zahirovic, S. (2021), *Elements* 17, 339-344, doi:10.2138/gselements.17.5.339 (609 ocorrências; 75 % a menos de 600 km de borda cratônica). Liu et al. (2023), *Geology* 51, 101-105, doi:10.1130/G50775.1. Giuliani e Pearson (2019), *Elements* 15, 377-380. Simandl e Paradis (2018). · **Nível:** revisada por pares
**Confiança:** confirmado (o sentido da relação); provável (os números exatos de kimberlitos, que variam com o critério de contagem)
**Também aparece em:** só na Aula 04. A tabela da Aula 01 ("Carbonatito: complexos alcalinos; rifteamento e plumas") dá o contexto **usual** e não compara números; foi mantida.
**Nota:** a base de kimberlitos mais citada para a contagem de 5.652 (Tappe et al., 2018, *EPSL* 484) teve **aviso de remoção** publicado em 2026 (doi:10.1016/j.epsl.2026.119830). Por isso **não** foi usada como fonte.

### 🟠 5. Faixas isotópicas: Sr do orangeíto começando em 0,705 e εNd do Grupo I deslocado para negativo

**claim_id:** `KIMB-M30-A04-ISOTOPOS-002` (também cobre `KIMB-M30-A04-EXEMPLO-ENDT-004`)
**Tipo:** impreciso
**Onde:** Aula 04 · "Isótopos: a impressão digital das fontes"; "Exemplo trabalhado"; recap
**Está escrito:** "Grupo I [...] εNd inicial em torno de zero, de levemente negativo a positivo" e "Orangeíto [...] ⁸⁷Sr/⁸⁶Sr inicial mais alto (da ordem de 0,705 a 0,710)". No exemplo, a amostra 1 (εNd ≈ −2,4) "cai na faixa de kimberlito do Grupo I".
**Problema:** Nos dados sul-africanos, o Sr inicial dos orangeítos começa perto de **0,707** (0,7072-0,7105 em Swartruggens e Star; ~0,708 como valor típico em Smith, 1983). Com 0,705 como limite, a faixa encosta na do Grupo I e o critério perde o poder de separar. O εNd do Grupo I vai de **próximo de zero a positivo (até ~+4)**. Um valor de −2,4 fica fora da faixa típica, e o exemplo classificava como Grupo I, sem ressalva, uma amostra ambígua.
**Correção proposta:** Grupo I: "εNd inicial próximo de zero a positivo (da ordem de 0 a +4)". Orangeíto: "⁸⁷Sr/⁸⁶Sr inicial da ordem de 0,707 a 0,712". Exemplo: a amostra 1 passa a ter ¹⁴³Nd/¹⁴⁴Nd = **0,512600**, o que dá **εNd ≈ +1,5**. A amostra 2 continua com −7,3.
**Fonte:** Smith (1983), *Nature* 304, 51-54, doi:10.1038/304051a0. Becker e le Roex (2006), *J. Petrol.* 47, 673-703. Coe, N., le Roex, A., Gurney, J., Pearson, D. G. & Nowell, G. (2008), *Contrib. Mineral. Petrol.* 156, 627-652, sobre Swartruggens e Star (0,70718-0,71050; εNd −7,8 a −12,0). · **Nível:** revisada por pares
**Confiança:** confirmado (sentido e ordem de grandeza); as faixas exatas variam com a compilação, e o texto já dizia isso
**Também aparece em:** recap da Aula 04.

### 🟠 6. Atribuições históricas: quem nomeou os Grupos I e II e quem criou "orangeíto"

**claim_id:** `KIMB-M30-A01-GRUPOS-I-II-002`
**Tipo:** impreciso (atribuição)
**Onde:** Aula 01 · "Um percurso histórico curto", item Grupos I e II; recap
**Está escrito:** "Skinner (1989) consolidou os rótulos **Grupo I** e **Grupo II**, e Mitchell (1995) propôs, para o Grupo II, o nome **orangeíto**"
**Problema:** Os rótulos Grupo I e Grupo II são de **Smith (1983)**, que mostrou a separação isotópica. Skinner (1989) sistematizou o **contraste petrográfico** entre os grupos. O termo **orangeíto** é de **Wagner (1928)**, para os kimberlitos micáceos do Estado Livre de Orange. Mitchell o **retomou** a partir de 1989 e o consolidou no livro de 1995. A distinção petrográfica entre kimberlito "basáltico" e "micáceo" já existia em Wagner (1914).
**Correção proposta:** Reescrever o item e a linha do recap com essas atribuições.
**Fonte:** Smith (1983); Skinner (1989), GSA Spec. Publ. 14, 528-544; Mitchell (1995), *Kimberlites, Orangeites, and Related Rocks*, Plenum. Literatura secundária convergente: Mitchell (1989, 1991, 1994) e Mitchell e Bergman (1991) "proposed the revival of the original term 'orangeite'"; Smith et al. (1985). · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** recap da Aula 01.

### 🟠 7. Scott Smith et al. (2013) descritos de forma imprecisa: "três fácies" universais, ordem dos estágios, tamanho do macrocristal

**claim_id:** `KIMB-M30-A03-FACIES-001`
**Tipo:** confusão de escopo e atribuição
**Onde:** Aula 03 · primeiro parágrafo das fácies, texto do macrocristal e recap. Aula 01 · item "A mudança de 2013"
**Está escrito:** (a03) "Scott Smith e colaboradores (2013) organizam a descrição em três **fácies** (esquema que vem de Clement e Skinner, adaptado por Field e Scott Smith, 1999, de memória)". (a03) "macrocristais (acima de 0,5 mm [...])". (a01) "terminologia por estágios [...] baseada primeiro em critérios de campo e textura (fácies), depois em mineralogia e geoquímica".
**Problema:**
- O modelo de **três zonas** (cratera, diatrema, hipabissal) é o clássico da escola sul-africana e vale para os pipes do **tipo Kimberley**. Field e Scott Smith (1999) mostraram que há **três classes de pipe**, e as do Canadá (Fort à la Corne, Lac de Gras) têm outra forma e outro preenchimento. Scott Smith et al. (2013, Fig. 1) ilustram justamente os três tipos de pipe, e não "três fácies" universais.
- O esquema de 2013 tem **cinco estágios**: descrição não genética; tipo de magma e mineralogia; classificação textural-genética (coerente ou vulcaniclástica); forma do corpo; interpretação genética. "Fácies" é interpretação genética, que o esquema deixa para depois de propósito.
- O corte de 0,5 mm para macrocristal é de **Clement et al. (1984)**. Scott Smith et al. (2013) o elevaram para **1 mm**.
**Correção proposta:** Apresentar o modelo de três zonas como o clássico dos pipes do tipo Kimberley, com as outras classes de Field e Scott Smith (1999). Descrever os estágios de 2013 na ordem certa. Dar os dois cortes do macrocristal.
**Fonte:** Scott Smith et al. (2013), texto integral (resumo; Fig. 1; seção sobre cristais: "Macrocryst [...] as proposed by Clement et al. (1984) with a lower size cut-off of 0.5 mm. Here the cut-off is adjusted to 1 mm"). Field e Scott Smith (1999), *Proc. 7th IKC* vol. 1, 214-237. Clement, Skinner e Scott Smith (1984), *J. Geol.* 92, 223-228. · **Nível:** normativa
**Confiança:** confirmado
**Também aparece em:** Aula 01 (item 2013) e recap da Aula 03. A Aula 05 (tabela de sítios finais) cita as fácies da Aula 03 de forma genérica e foi mantida.

### 🟠 8. Jacupiranguito "com magnetita e titanita"

**claim_id:** `KIMB-M30-A03-JACUPIRANGUITO-009` (criado pela auditoria)
**Tipo:** impreciso (definição)
**Onde:** Aula 03 · "Foscoritos e rochas ultramáficas alcalinas"
**Está escrito:** "**jacupiranguito** (clinopiroxenito alcalino com magnetita e titanita, nome dado por sua localidade-tipo em Jacupiranga, São Paulo)"
**Problema:** Pela definição clássica (Derby, 1891; glossário IUGS de Le Maitre, 2002), o jacupiranguito é um **clinopiroxenito com nefelina**, formado essencialmente de **titanoaugita e magnetita**, com pouca nefelina. A titanita não é mineral definidor.
**Correção proposta:** "(clinopiroxenito com nefelina, formado essencialmente de titanoaugita e magnetita, com pouca nefelina; nome dado por Derby, em 1891, a partir da localidade-tipo em Jacupiranga, São Paulo)".
**Fonte:** Le Maitre (2002), glossário; Mindat, glossário "jacupirangite" (Derby 1891; "titanaugite and magnetite, with a smaller amount of nepheline"). · **Nível:** normativa (glossário IUGS) e base de referência
**Confiança:** confirmado
**Também aparece em:** só na Aula 03. A Aula 06 cita Jacupiranga como "localidade-tipo do jacupiranguito" e está correta.

### 🟠 9. "Kimberlitos transicionais" atribuídos a um artigo que os reclassifica

**claim_id:** `KIMB-M30-A04-TRANSICIONAIS-006` (criado pela auditoria)
**Tipo:** impreciso (atribuição e uso de termo)
**Onde:** Aula 04 · "Exemplo trabalhado", Passo 3, ressalva (i); Fontes
**Está escrito:** "amostras com εNd intermediário são comuns em 'kimberlitos transicionais' (Journal of Petrology, 2023, sobre lamproítos e kimberlitos de fonte comum, título parcial de memória)"
**Problema:** O artigo é Sarkar et al. (2023). Ele diz que "kimberlito transicional" é um termo **usado antes** para rochas do sudoeste do Kaapvaal e, por petrografia e química mineral, as **reclassifica** como kimberlitos típicos (Leicester, Frank Smith) ou olivina-lamproítos (Wimbledon, Melton Wold, Droogfontein, Silvery Home). Os autores argumentam que petrografia e química mineral classificam melhor que isótopos. Citar o artigo para apoiar "kimberlitos transicionais" como categoria inverte o que ele conclui.
**Correção proposta:** "há rochas com valores intermediários; no sudoeste do Cráton do Kaapvaal elas eram chamadas de 'kimberlitos transicionais', mas Sarkar et al. (2023) mostraram, por petrografia e química mineral, que são kimberlitos típicos ou olivina-lamproítos, o que reforça que os isótopos sozinhos não classificam a rocha".
**Fonte:** Sarkar, S., Giuliani, A., Dalton, H., Phillips, D., Ghosh, S., Misev, S. & Maas, R. (2023), *J. Petrol.* 64(7), egad043, doi:10.1093/petrology/egad043 (resumo lido no OpenAlex). · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Fontes da Aula 04.

### 🟠 10. Orapa como "grandes pipes de baixo teor"

**claim_id:** `KIMB-M30-A06-ORAPA-006` (criado pela auditoria)
**Tipo:** impreciso
**Onde:** Aula 06 · "Da anomalia ao teor: o ciclo de exploração"
**Está escrito:** "Em outro extremo, minas como **Orapa** (Botsuana, descoberta em 1967, de memória) exploram grandes pipes de baixo teor."
**Problema:** O pipe AK1 de Orapa é um dos maiores conhecidos (~117 ha), mas o teor **não é baixo**: as reservas de 2012 davam ~59 cpht, mais que o dobro dos 25 cpht do exemplo trabalhado da própria aula. O traço distintivo é a **tonelagem**, não o teor baixo. A data de descoberta (1º de março de 1967) confere.
**Correção proposta:** "Em outro extremo de escala, **Orapa** (Botsuana, descoberta em 1967) lavra um dos maiores pipes conhecidos (AK1, cerca de 117 ha), com teor de reserva da ordem de 60 cpht (dado de 2012): ali, o que pesa é a tonelagem."
**Fonte:** Mining Technology, "Orapa Diamond Mine" (reservas de dezembro de 2012: 85,7 Mct a 58,69 cpht; AK1 de 117 ha); Debswana/De Beers (descoberta em 01/03/1967). · **Nível:** geral (dados de empresa)
**Confiança:** provável (dado de mina datado)
**Também aparece em:** só na Aula 06.

### 🟠 11. Problemas bibliográficos (ano, autoria incompleta, fontes sem autor identificado)

**claim_id:** `KIMB-M30-MOD-BIBLIO-001` (criado pela auditoria)
**Tipo:** impreciso (bibliografia)
**Onde:** Fontes das Aulas 01, 03, 04, 05 e 06; texto da Aula 06
**Está escrito / problema:**
- **Janse (1992)** no texto e nas Fontes da Aula 06. O trabalho saiu nos anais da 5ª IKC (Araxá, 1991), vol. 2, CPRM, **1994**, pp. 215-235, e é nele que aparece o conceito de *archon*.
- **Scott Smith et al. (2013)** nas Aulas 01 e 03, com sete autores. São **nove**: faltavam M. Harder e E. M. W. Skinner.
- Aula 04: artigo do *J. Petrol.* 2023 "autoria e título completos NÃO conferidos". É Sarkar et al. (2023) (ver 🟠 9).
- Aula 05: discussão magma × brine citada como "PubMed 37467324; autoria e periódico NÃO conferidos". É **Yuan, X., Zhong, R., Xiong, X., Gao, J. & Ma, Y. (2023)**, *Science Advances* 9(29), eadh0458. O artigo sustenta transição **contínua** em carbonatitos profundos e partição diferente em sistemas rasos, o que confere com os "dois cenários" do texto.
**Correção proposta:** Corrigir o ano de Janse no texto e nas Fontes; completar os autores de Scott Smith et al.; identificar Sarkar et al. e Yuan et al.
**Fonte:** Crossref (doi:10.1093/petrology/egad043; doi:10.1126/sciadv.adh0458); texto integral de Scott Smith et al. (2013); IKC Extended Abstracts e bibliografias que citam Janse (1994). · **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** somente nas Fontes e no parágrafo da regra de Clifford (Aula 06).

### 🟡 12. Idade de Argyle "cerca de 1,2 Ga"

**claim_id:** `KIMB-M30-A01-ARGYLE-005` (criado pela auditoria)
**Tipo:** desatualizado
**Onde:** Aula 01 · "Rochas insaturadas em sílica associadas", item Lamproítos; e o item histórico sobre Argyle
**Está escrito:** "Argyle (Austrália, cerca de 1,2 Ga, diamantífero)" e "se descobriu, no fim da década de 1970, que o depósito de Argyle [...] era um lamproíto".
**Problema:** A idade clássica era 1178 ± 47 Ma. Olierook et al. (2023) situaram a colocação do lamproíto de Argyle **entre 1311 ± 9 e 1257 ± 15 Ma**, ou seja, **~1,3 Ga**, "older than previously known". O pipe foi descoberto em 1979, e sua natureza lamproítica foi reconhecida na virada das décadas de 1970 e 1980.
**Correção proposta:** Dar a idade revista (~1,3 Ga) e manter a antiga como referência ("antes estimada em ~1,18 Ga"), porque o aluno vai encontrar o valor antigo na literatura. Situar a descoberta em 1979 e o reconhecimento como lamproíto na virada das décadas.
**Fonte:** Olierook, H. K. H. et al. (2023), "Emplacement of the Argyle diamond deposit into an ancient rift zone triggered by supercontinent breakup", *Nature Communications* 14, 5274, doi:10.1038/s41467-023-40904-8. · **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** a Aula 06 cita Argyle sem idade (cinturão proterozoico; fechamento em 2020, que confere) e não precisou de alteração de idade.

### 🔵 13. Limiar G10 declarado como "ilustrativo e não o do artigo"

**claim_id:** `KIMB-M30-A03-EXEMPLO-GRANADA-005` (também cobre a parte G10 de `KIMB-M30-A03-MINERAIS-INDICADORES-002`)
**Tipo:** evidência insuficiente (resolvido com fonte)
**Onde:** Aula 03 · "Exemplo trabalhado", Passo 2; Fontes (Grütter et al.)
**Está escrito:** "situa-se, em diagramas Ca-Cr como os de Grütter et al. (2004), no campo de granadas subcálcicas de harzburgito (G10), conforme a discriminação usual de exploração (limite depende do diagrama; ver Fontes)" e, nas Fontes, "os limiares de Cr₂O₃ e CaO do exemplo são ilustrativos e não os do artigo".
**Problema:** O critério não estava conferido. No artigo, a divisória G10/G9 é **CaO = 3,375 + 0,25 · Cr₂O₃** (% peso), a "linha de 85 %" de Gurney (1984). Para Cr₂O₃ = 9 %, o limite é CaO = 5,6 %, e a granada do exemplo (CaO = 2,5 %) é **G10**. Ela também cumpre o critério **G10D** (fácies diamante): Cr₂O₃ ≥ 5,0 + 0,94 · CaO = 7,4 %. A classificação do exemplo estava certa, mas por acaso.
**Correção proposta:** Escrever a divisória e o critério G10D no Passo 2 e trocar a nota das Fontes.
**Fonte:** Grütter, H. S., Gurney, J. J., Menzies, A. H. & Winter, F. (2004), *Lithos* 77, 841-857, doi:10.1016/j.lithos.2004.04.012 (texto integral, seção 4.1 e Fig. 3). · **Nível:** normativa para exploração
**Confiança:** confirmado
**Também aparece em:** só na Aula 03.

### 🔵 14. Participação do Brasil no Nb "mais de 85 %, de memória" e percentuais de Simandl e Paradis

**claim_id:** `KIMB-M30-A06-CARBONATITOS-MINERIO-003`
**Tipo:** evidência insuficiente (resolvido com fonte)
**Onde:** Aula 06 · "Carbonatitos: os grandes fornecedores de Nb e ETR"
**Está escrito:** "cerca de 10 % das ocorrências de carbonatito hospedam ou hospedaram mina, e outros 10 % são recursos definidos" e "(a literatura brasileira cita mais de 85 %, de memória)".
**Problema:** O dado de Nb estava marcado como de memória. O USGS (Mineral Commodity Summaries 2026) dá ao Brasil **~93 %** da produção mineira mundial de Nb em 2025. Os percentuais de Simandl e Paradis conferem como aproximação: 9 % com minas ativas ou históricas (6 % + 3 %) e 11 % com recurso mineral estabelecido, sobre as 527 ocorrências de Woolley e Kjarsgaard (2008).
**Correção proposta:** Substituir os dois trechos pelos valores com fonte.
**Fonte:** USGS, *Mineral Commodity Summaries 2026*, Niobium (pubs.usgs.gov/periodicals/mcs2026/mcs2026-niobium.pdf). Simandl e Paradis (2018), *Applied Earth Science* 127(4), 123-152, texto integral. · **Nível:** normativa (USGS) e revisada por pares
**Confiança:** confirmado
**Também aparece em:** recap da Aula 06 (não repete o número; mantido).

---

## Verificado e correto

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `KIMB-M30-A01-CARBONATITO-IUGS-001` | >50 % vol. de carbonato primário e <20 % em peso de SiO₂; silicocarbonatito acima de 20 %; corte 0,8; MgO contra FeO + Fe₂O₃ + MnO; % peso | Le Maitre 2002; Woolley e Kempe 1989; Simandl e Paradis 2018 (texto integral) | confirmado |
| `KIMB-M30-A01-HISTORICO-003` | Kimberley no início dos anos 1870; Lewis 1887; Brøgger 1921 (Fen; também "fenitização"); Niggli 1923; Dawson 1962 (*Nature* 195, 1075-1076) | Crossref; biografia de H. C. Lewis; literatura sobre Fen e lamproítos | confirmado (Argyle: ver 🟡 12) |
| `KIMB-M30-A01-EXEMPLO-CLASSIFICACAO-004` | A = 0,85, calciocarbonatito; D = 0,59, magnesiocarbonatito (12 > 8,5); B não é carbonatito; C é silicocarbonatito | aritmética refeita | confirmado |
| `KIMB-M30-A02-QUILHA-CRATONICA-001` | 150-250 km; Fo 92-93 contra 89-90; flutuabilidade composicional (Jordan 1978); ~40 mW/m² | Jordan 1978 (*Nature* 274, 544-548); Pollack e Chapman 1977; Pearson et al. 2014 | confirmado (ordem de grandeza) |
| `KIMB-M30-A02-METASSOMATISMO-003` | Modal × críptico; MARID (Dawson e Smith 1977); PIC; veios de Foley 1992; contínuo em peridotito carbonatado | Crossref para todos; Foley 1992 (*Lithos* 28, 187-204) | confirmado |
| `KIMB-M30-A03-MINERAIS-INDICADORES-002` | KIMs; piropo G10 e cromita rica em Cr e pobre em Ti como indicadores | Grütter et al. 2004 (texto integral) | confirmado |
| `KIMB-M30-A03-LAMPROITO-KAMAFUGITO-003` | Assembleias de lamproíto, kamafugito e UML | Mitchell e Bergman 1991; Tappe et al. 2005 | confirmado |
| `KIMB-M30-A03-FENITIZACAO-004` | Feldspato alcalino, aegirina, anfibólio sódico, perda de quartzo; Le Bas 2008 | Le Bas 2008 (*Can. Mineral.* 46, 915-932) | confirmado |
| `KIMB-M30-A04-GEOQUIMICA-001` | Faixas típicas de SiO₂ e MgO do kimberlito; carbonatito com La/Yb alto e anomalias negativas de Zr, Hf e Ti | Giuliani e Pearson 2019; Becker e le Roex 2006; Gibson et al. 1995 (La/Yb = 50-230 na APIP) | provável (faixas típicas) |
| `KIMB-M30-A04-TRES-ROTAS-003` | Três rotas não exclusivas; contínuo experimental não consensual | Yaxley et al. 2022 (*Annu. Rev.* 50, 261-293); Brooker e Kjarsgaard 2011; Kjarsgaard e Hamilton 1988 | confirmado |
| `KIMB-M30-A05-ASCENSAO-001` | Ascensão em diques a m/s; assimilação de opx reduz a solubilidade do CO₂ | Sparks et al. 2006 (>4 a 20 m/s); Russell et al. 2012 (*Nature* 481, 352-356) | confirmado |
| `KIMB-M30-A05-SEQUENCIA-CARBONATITO-002` | Calcita → dolomita → ferrocarbonato, com Fe, Mn, Ba, Sr, ETR e F tardios | Chakhmouradian e Zaitsev 2012; Yaxley et al. 2022 | confirmado (tendência geral) |
| `KIMB-M30-A05-MAGMA-BRINE-003` | Exsolução × diluição contínua, em debate | Yuan et al. 2023 (*Sci. Adv.* 9, eadh0458) | confirmado |
| `KIMB-M30-A05-EXEMPLO-RAYLEIGH-004` | 0,30^(−0,95) = 3,14, ou 1569 ppm; D = 1,5 dá ~274 ppm (texto: 275, arredondamento de 0,55); 0,30/0,30 = 1,0 % | aritmética refeita | confirmado |
| `KIMB-M30-A06-DIAMANTE-TRANSPORTADOR-001` | Diamante de 1 a >3 Ga; populações P, E e W | Gurney et al. 2010 (*Econ. Geol.* 105, 689-712); Stachel e Harris 2008 | confirmado |
| `KIMB-M30-A06-CLIFFORD-002` | Regra de Clifford (1966, *EPSL* 1, 421-434); archon (Janse 1994; ano corrigido em 🟠 11); Argyle num orógeno proterozoico ao lado do Cráton Kimberley; fechamento em nov./2020 | Crossref; Olierook et al. 2023; Rio Tinto (2020) | confirmado |
| `KIMB-M30-A06-APIP-004` | APIP ~85 Ma (Cretáceo Superior), >15.000 km³, ~25.000 km², pluma de Trindade; seis complexos; Braúna 642 Ma e primeira mina de diamante em kimberlito da América do Sul; Juína | Gibson et al. 1995 (resumo); literatura USP/APIP; Donatti-Filho et al. 2013; Kaminsky et al. 2001 | confirmado |
| `KIMB-M30-A06-EXEMPLO-ESTOQUE-005` | 11,7 Mt; 2,93 Mct; US$ 176 M; 300 kt de Nb₂O₅; fração 0,699; 210 kt de Nb | aritmética refeita | confirmado |

**Consistência entre módulos.** As constantes do CHUR e o λ do ¹⁴⁷Sm da Aula 04 (0,512638; 0,1967; 6,524 × 10⁻¹² a⁻¹) são **as mesmas** do Módulo 26, Aula 04, já auditado. A atribuição do CHUR a DePaolo e Wasserburg (1976) segue a convenção do Módulo 26 e não foi reaberta aqui. A rota "Módulo 26, Aula 04 (Sm-Nd, εNd)" confere. As remissões aos Módulos 9, 15, 16, 19 e 20-22 conferem com os títulos desses módulos.

---

## Correções aplicadas

**Aplicadas em:** 2026-09-23

| # | claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|---|
| 1 | `KIMB-M30-A02-GRAFITE-DIAMANTE-002` | 🔴 | Corrigido | aula-02 |
| 2 | `KIMB-M30-A03-TUFFISITICO-006` | 🔴 | Corrigido | aula-03 |
| 3 | `KIMB-M30-A03-ATOL-007` | 🔴 | Corrigido | aula-03 |
| 4 | `KIMB-M30-A04-NUMERO-OCORRENCIAS-005` | 🔴 | Corrigido | aula-04 |
| 5 | `KIMB-M30-A04-ISOTOPOS-002` | 🟠 | Corrigido | aula-04 |
| 6 | `KIMB-M30-A01-GRUPOS-I-II-002` | 🟠 | Corrigido | aula-01 |
| 7 | `KIMB-M30-A03-FACIES-001` | 🟠 | Corrigido | aula-03, aula-01 |
| 8 | `KIMB-M30-A03-JACUPIRANGUITO-009` | 🟠 | Corrigido | aula-03 |
| 9 | `KIMB-M30-A04-TRANSICIONAIS-006` | 🟠 | Corrigido | aula-04 |
| 10 | `KIMB-M30-A06-ORAPA-006` | 🟠 | Corrigido | aula-06 |
| 11 | `KIMB-M30-MOD-BIBLIO-001` | 🟠 | Corrigido | aula-01, aula-03, aula-04, aula-05, aula-06 |
| 12 | `KIMB-M30-A01-ARGYLE-005` | 🟡 | Corrigido (valor antigo mantido como referência) | aula-01 |
| 13 | `KIMB-M30-A03-EXEMPLO-GRANADA-005` | 🔵 | Confirmado com fonte e reescrito | aula-03 |
| 14 | `KIMB-M30-A06-CARBONATITOS-MINERIO-003` | 🔵 | Confirmado com fonte e reescrito | aula-06 |

Também foram alterados: as marcas "DE MEMÓRIA / não conferido" das Fontes das seis aulas, trocadas por "CONFERIDO na auditoria (2026-09-23)"; o bloco `alegacoes_auditaveis` das aulas 01, 03, 04 e 06, com os claims criados pela auditoria; o bloco `auditoria` nos metadados de cada aula; e o hub do módulo (registro).

**Propagação.** O módulo **não tem questionário, baralho nem glossário**: a auditoria correu antes deles, e nenhum card no Anki precisa ser corrigido. Busquei no curso inteiro tuffisítico, atol, orangeíto, Clifford, Argyle, Orapa, jacupiranguito, a reta grafite-diamante e a comparação de números: **nenhum outro módulo repete os fatos corrigidos**. O Módulo 40 cita kimberlitos só como portadores de xenólitos, e o 22 só como geometria de pipe.

**Pendências:** nenhuma.

---

## Restrições obrigatórias para quem gerar a avaliação (questionário e flashcards)

1. **Grafite-diamante:** usar só P (kbar) = 19,4 + 0,025 · T(°C) (Kennedy e Kennedy, 1976). **Nunca** 7,1 + 0,027 T com T em °C. Se Berman e Simon aparecer, T é em kelvin. A janela do diamante numa geoterma cratônica começa perto de **~150 km**, e não a ~95 km.
2. Em cálculo de janela, o enunciado deve dar a geoterma, a conversão km/GPa e a reta. Não cobrar a "temperatura do manto convectivo" como número exato (~1400 °C é ordem de grandeza).
3. **Tuffisítico = nome antigo**; o moderno é **kimberlito piroclástico do tipo Kimberley (KPK)** (Scott Smith et al., 2013).
4. **Atol:** núcleo de espinélio, zona de serpentina ou calcita, borda de magnetita. Nunca "espinélio em volta de olivina ou perovskita".
5. **Kimberlitos são muito mais numerosos que carbonatitos** (milhares × ~600). Não cobrar número exato de kimberlitos, que varia com o critério de contagem.
6. Carbonatitos não são "exclusivos de riftes e plumas": são sobretudo continentais, e 75 % ficam a menos de 600 km de uma borda cratônica.
7. **Isótopos:** Grupo I com Sr inicial ~0,703-0,705 e εNd de ~0 a +4; orangeíto com Sr ~0,707-0,712 e εNd de ~−6 a −12. As faixas são referências e **não fronteiras rígidas**. Não cobrar os limites como valores exatos.
8. **Atribuições:** Grupos I e II = Smith (1983); contraste petrográfico = Skinner (1989); orangeíto = Wagner (1928), retomado por Mitchell (consolidado em 1995). Não cobrar atribuição bibliográfica como resposta única, a não ser nesses termos.
9. O modelo de **três fácies** vale para os pipes do **tipo Kimberley**. Não cobrá-lo como universal. Field e Scott Smith (1999) reconhecem três classes de pipe.
10. **Macrocristal:** > 0,5 mm (Clement et al., 1984) ou > 1 mm (Scott Smith et al., 2013). Aceitar os dois, com a convenção citada.
11. **Jacupiranguito:** titanoaugita + magnetita + pouca nefelina. Não cobrar titanita como mineral definidor.
12. **G10:** divisória CaO = 3,375 + 0,25 · Cr₂O₃ (% peso); G10D: Cr₂O₃ ≥ 5,0 + 0,94 · CaO. Um piropo G10 indica manto compatível com diamante, **não** teor de diamante.
13. **"Kimberlito transicional"** não deve ser cobrado como categoria válida; Sarkar et al. (2023) reclassificaram essas rochas.
14. **Argyle:** ~1,3 Ga (Olierook et al., 2023; antes ~1,18 Ga), lamproíto, descoberto em 1979, fechado em 2020. **Orapa:** grande pipe (~117 ha), **não** "de baixo teor".
15. **Nb:** o Brasil tem ~90 % ou mais da produção mineira mundial (USGS: ~93 % em 2025). Não cobrar o percentual exato.
16. **Janse = 1994** (archon). Sem paginação nem valores de exemplos hipotéticos cobrados como constantes.
17. Continuam **em debate** e não podem ser cobrados como consenso: o contínuo carbonatito-kimberlito, a rota dominante de geração do carbonatito, a transição magma-brine, a origem de Bayan Obo e do carbonado, e o mecanismo de captura do diamante em Argyle.
