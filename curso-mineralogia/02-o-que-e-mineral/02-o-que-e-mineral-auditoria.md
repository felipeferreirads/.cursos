# Auditoria científica: Módulo 02 — O que é um mineral

**Auditado em:** 2026-10-03
**Material:** `curso-mineralogia/02-o-que-e-mineral/` — as 5 aulas (`02-o-que-e-mineral-aula-01` a `-aula-05`)
**Modo:** audit-and-fix
**Profundidade:** full (com checagem de consistência com curso-geologia, módulo 04, aulas 03 e 06, sem alterar aquele curso)
**Escopo:** as 41 alegações listadas nos rodapés `alegacoes_auditaveis`, mais as afirmações de risco do corpo (definição literal, datas de decisões da IMA, códigos de classificação, números de abundância). Não há questionário nem baralho do módulo, então não houve material derivado a propagar.
**Veredito:** Requer correção → **correções aplicadas; estado final: Aprovado** (nenhum achado aberto)

## Resumo

🔴 0 erros · 🟠 3 imprecisões · 🟡 0 desatualizados · 🔵 1 sem fonte · ⚪ 0 controversos
Verificadas e corretas: 39 alegações (36 confirmadas, 3 prováveis), incluindo 2 alegações acrescentadas pela revisão didática e conferidas no mesmo dia.

Os pontos de maior risco passaram: o texto literal da definição de Nickel (1995) e a exclusão de biogênicos e antropogênicos com os exemplos do próprio artigo; o status "grandfathered" do mercúrio e da opala; a decisão de 1982 (titanita × esfeno); biotita como nome de série (Rieder et al., 1998); as abundâncias de Mason & Moore e de Ronov & Yaroshevsky; os códigos de Strunz e Dana do quartzo, da halita e da forsterita. Os problemas foram de atribuição (o cargo de Nickel), de hierarquia de nomenclatura incompleta e de escopo (manto).

> [!note] Limite da verificação nesta sessão
> O proxy da sessão bloqueou o acesso direto às páginas (Mindat, RRUFF, CNMNC, Cambridge, Wikipedia, MSA). A verificação foi feita por busca na web, cruzando resumos de mais de uma fonte com as referências bibliográficas completas (autor, ano, revista, volume, páginas). Onde só havia uma fonte secundária, a confiança ficou em "provável". Recomenda-se, numa sessão com acesso, conferir o PDF de Nickel (1995) e a página de Mills et al. (2009) no site da CNMNC.

## Achados

### 🟠 1. Ernest Nickel chamado de "presidente da comissão" em 1995

**claim_id:** `MIN-DEF-COMISSAO-001`
**Tipo:** certeza indevida (atribuição)
**Onde:** aula 01 · Uma palavra comum, um termo técnico
**Está escrito:** "redigida por Ernest Nickel, então presidente da comissão"
**Problema:** o obituário de Nickel e o histórico da comissão o registram como **vice-presidente** da CNMMN, ao lado do presidente J. A. Mandarino (1983–1994). Nenhuma fonte encontrada o coloca como presidente em 1995. Faltava também o nome atual da comissão: a CNMMN e a Commission on Classification of Minerals se fundiram em 2006 na CNMNC.
**Correção aplicada:** "Desde 1959, uma comissão da IMA (chamada CNMNC desde 2006) aprova cada mineral novo [...] redigida por Ernest Nickel, mineralogista que foi vice-presidente da comissão por mais de uma década".
**Fonte:** Obituário "Ernest Henry Nickel 1925–2009", *Mineralogical Magazine* 73(5), 891; relatório da CNMNC de 2009 (fusão de 2006)  ·  **Nível:** revisada por pares / normativa
**Confiança:** provável
**Também aparece em:** só na aula 01.

### 🟠 2. Hierarquia de grupos da IMA incompleta; "série" tratada como não oficial

**claim_id:** `MIN-NOM-GRUPO-001`
**Tipo:** omissão que gera erro
**Onde:** aula 03 · Série de solução sólida; Grupo; Tabela de decisão
**Está escrito:** "uma hierarquia [...] supergrupo, grupo, subgrupo e espécie (Mills et al., 2009)"; na tabela, série com status "descreve composição".
**Problema:** Mills et al. (2009) definem classe, subclasse, família, supergrupo, grupo, **subgrupo ou série** e espécie. Série é um nível formal, alternativo a subgrupo. A tabela, como escrita, dizia que a série não tem lugar na nomenclatura da IMA, o que contradiz a norma citada.
**Correção aplicada:** hierarquia completa no texto; a série "agrupa espécies, mas não é uma espécie; na hierarquia da IMA, 'série' aparece no mesmo nível que 'subgrupo'"; tabela e recap ajustados.
**Fonte:** Mills, S. J., Hatert, F., Nickel, E. H. & Ferraris, G. (2009), *European Journal of Mineralogy* 21, 1073–1080  ·  **Nível:** normativa
**Confiança:** confirmado
**Também aparece em:** só na aula 03.

### 🟠 3. "No manto, olivina e piroxênios dominam"

**claim_id:** `MIN-ABU-MANTO-001`
**Tipo:** confusão de escopo
**Onde:** aula 04 · O que não concluir
**Está escrito:** "O manto tem mais Mg e Fe [...] e por isso outra mineralogia (olivina e piroxênios dominam)".
**Problema:** vale para o manto superior. Na zona de transição e no manto inferior, a pressão transforma essas fases em outras (wadsleyíta, ringwoodita, bridgmanita), que são tema do módulo 43.
**Correção aplicada:** "(no manto superior, olivina e piroxênios dominam; mais fundo, a pressão produz outras fases, módulo 43)".
**Fonte:** Klein & Dutrow, *Manual of Mineral Science*, 23ª ed. (mineralogia do manto)  ·  **Nível:** livro-texto de referência
**Confiança:** confirmado
**Também aparece em:** só na aula 04.

### 🔵 4. Ano de aprovação da edscottita

**claim_id:** `MIN-DEF-EXTRATERR-001`
**Tipo:** evidência insuficiente
**Onde:** aula 01 · Parte 3 (e recap)
**Está escrito:** "aprovada pela comissão em 2019"
**Problema:** o número da proposta é IMA 2018-086a e a descrição foi publicada em 2019. O ano exato da aprovação não foi confirmado.
**Correção aplicada:** reescrito com o que está confirmado: "descrita em 2019 (proposta IMA 2018-086a)".
**Fonte:** Ma, C. & Rubin, A. E. (2019), *American Mineralogist* 104(9), 1351–1355, doi:10.2138/am-2019-7102  ·  **Nível:** revisada por pares
**Confiança:** confirmado (para a nova redação)
**Também aparece em:** recap da aula 01 (corrigido junto).

## Verificado e correto

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `MIN-DEF-NICKEL-001` | Texto literal da definição de 1995 | Nickel (1995), *Can. Mineral.* 33, 689–690 | confirmado |
| `MIN-DEF-MERCURIO-001` | Mercúrio líquido, sólido abaixo de ~−39 °C, espécie "grandfathered" | Nickel (1995); status na lista IMA | confirmado |
| `MIN-DEF-GELO-001` | Gelo é mineral; água líquida não | Nickel (1995) | confirmado |
| `MIN-DEF-AMORFO-001` | Georgeíta e outros poucos amorfos aceitos; "mineraloide" para os demais | Nickel (1995) | confirmado |
| `MIN-DEF-SINTETICO-001` | Sintéticos não são minerais | Nickel (1995) | confirmado |
| `MIN-DEF-ORGANICO-001` | Minerais orgânicos aprovados (whewellita, abelsonita); classe 10 de Strunz | Strunz & Nickel (2001); *Am. Mineral.* 63 (1978) | confirmado |
| `MIN-DEF-CINCOCRIT-001` | "Inorgânico" não consta do texto da IMA | comparação direta com Nickel (1995) | confirmado |
| `MIN-DEF-BIOGEN-001` | Exemplos de Nickel: cálculos urinários, oxalato em plantas, conchas; aceitação com componente geológico (folhelho negro, guano, calcários, fosforitos) | Nickel (1995) | confirmado |
| `MIN-DEF-ANTROPO-001` | Decisão de 1995 sobre produtos de processos naturais em material humano (Laurion); espécies antigas mantidas | Nickel (1995); Nickel & Grice (1998) | confirmado |
| `MIN-DEF-HAZEN208-001` | 208 espécies de ocorrência principal ou exclusivamente humana | Hazen et al. (2017), *Am. Mineral.* 102, 595–611 | provável (número confirmado; lista de contextos provável) |
| `MIN-DEF-OPALA-001` | Opala-A amorfa, opala-CT parcial; "opala" na lista como espécie herdada | lista IMA; Mindat | confirmado |
| `MIN-DEF-WHEWELL-001` | Whewellita em cálculos renais (biogênica) e em carvão e concreções (mineral) | Handbook of Mineralogy; Mindat | confirmado |
| `MIN-DEF-AMBAR-001` | Âmbar mineraloide orgânico; obsidiana rocha vítrea; pérola biogênica | Klein & Dutrow | confirmado |
| `MIN-NOM-DOMINANTE-001` | Regra do constituinte dominante; 50% em binária simples | Hatert & Burke (2008), *Can. Mineral.* 46, 717–728 | confirmado |
| `MIN-NOM-OLIVINA-001` | Olivina é grupo; forsterita e faialita são espécies | lista IMA | confirmado |
| `MIN-NOM-PLAGIO-001` | Albita e anortita são as espécies do plagioclásio; labradorita etc. não | lista IMA | confirmado |
| `MIN-NOM-BIOTITA-001` | Biotita é nome de série (flogopita–anita–siderofilita–eastonita) | Rieder et al. (1998), *Can. Mineral.* 36, 905–912 | confirmado |
| `MIN-NOM-VARIEDADE-001` | Ametista, citrino, esmeralda (Cr e/ou V), rubi, safira | Klein & Dutrow; GIA | confirmado |
| `MIN-NOM-COMERCIAL-001` | "Diamante Herkimer" é quartzo; "jade" = jadeíta ou nefrita | GIA; Klein & Dutrow | confirmado |
| `MIN-NOM-ESFENO-001` | 1982: titanita adotada, esfeno desacreditado | histórico da CNMMN; Mindat | confirmado |
| `MIN-NOM-POLIMORFO-001` | Calcita e aragonita: polimorfos, espécies distintas | lista IMA | confirmado |
| `MIN-ABU-NESPECIES-001` | 6.161 espécies (jul. 2025); ~100 novas por ano | *The New IMA List of Minerals*, jul. 2025 | provável (taxa anual de fonte secundária) |
| `MIN-ABU-ELEMENTOS-001` | O 46,6; Si 27,7; Al 8,1; Fe 5,0; Ca 3,6; Na 2,8; K 2,6; Mg 2,1 (~98,5%) | Mason & Moore (1982) | confirmado |
| `MIN-ABU-OXIGENIO-001` | O: ~62,6% dos átomos, 91,7% do volume | Mason & Moore (1982) | confirmado |
| `MIN-ABU-RONOV-001` | Tabela de volume da crosta (plagioclásio 39 ... não silicatos 8) | Ronov & Yaroshevsky (1969) | confirmado |
| `MIN-ABU-CROSTA-001` | Crosta oceânica ~5–10 km; continental ~30–70 km | USGS; geofísica consolidada | confirmado |
| `MIN-ABU-RBBA-001` | Rb e Ba substituem K em feldspatos e micas | Klein & Dutrow | provável |
| `MIN-ABU-HAZEN2015-001` | 4.933 espécies; 22% de uma localidade; mais da metade de ≤5 | Hazen et al. (2015), *Can. Mineral.* 53, 295–324 | confirmado |
| `MIN-CLS-STRUNZ-001` | 10 classes de Nickel-Strunz; Strunz 1941; 9ª ed. 2001 | Strunz & Nickel (2001) | confirmado |
| `MIN-CLS-CODIGOS-001` | Halita 3.AA.20; forsterita 9.AC.05; pirita 2.EB.05a; quartzo 4.DA.05 | Strunz & Nickel (2001) | confirmado |
| `MIN-CLS-DANA-001` | 78 classes; 1, 9, 14, 28, 38; silicatos 51–78; quartzo 75.1.3.1 | Gaines et al. (1997) | confirmado |
| `MIN-CLS-BERZELIUS-001` | Classificação pelo ânion remonta a Berzelius (1814, 1824) | Strunz & Nickel (2001) | confirmado |
| `MIN-CLS-TITANITA-001` | Titanita é silicato (classe 9) | Strunz & Nickel (2001) | confirmado |
| `MIN-FON-HANDBOOK-001` | Handbook: 5 volumes, 1990–2003; PDFs da MSA | handbookofmineralogy.org | confirmado |
| `MIN-FON-RRUFF-001` | RRUFF: Univ. do Arizona; Raman, DRX, química; base IMA | rruff.info | confirmado |
| `MIN-FON-MINDAT-001` | Mindat: 1993 (J. Ralph), aberto em 2000; Hudson Institute | Mindat; *Am. Mineral.* 110 (2025) | confirmado |
| `MIN-FON-LISTAIMA-001` | Lista oficial mantida pela CNMNC, atualizada periodicamente | CNMNC | confirmado |
| `MIN-DEF-ABELSON-001` | Abelsonita: Ni-porfirina derivada de clorofila (texto da revisão didática) | *Am. Mineral.* 63 (1978); OSTI | confirmado |
| `MIN-ABU-GLOSSAS-001` | Glossas de granito, basalto, arenito e argilominerais (texto da revisão didática) | Klein & Dutrow | confirmado |

## Consistência com curso-geologia, módulo 04 (aulas 03 e 06)

Lido sem alterar. O módulo 02 apresenta a definição da IMA e trata os "cinco critérios" como simplificação didática, sem dizer que o curso-geologia está errado, como pede o `_contexto.md`. Dois pontos daquele curso merecem a auditoria `cross-course` recomendada no `_contexto.md`:

- **aula 03:** diz que o mercúrio é a "única" exceção ao critério de sólido cristalino mantida por tradição. A lista IMA também mantém a opala como espécie herdada, e a comissão aceitou alguns amorfos (georgeíta). Não é contradição com este módulo sobre o mercúrio, mas a palavra "única" fica imprecisa.
- **aula 03:** afirma que a obsidiana não seria "uma rocha no sentido estrito". Este curso a trata como rocha vítrea (o vidro é o mineraloide). Vale conferir na auditoria transversal.
- **aula 06:** mesmo critério de classe pelo ânion; sem divergência encontrada.

## Observações não factuais

- A aula 05 cobre dois objetivos (classes e fontes) e fica no limite de ~30 min; é tema para a revisão didática.

## Correções aplicadas

**Aplicadas em:** 2026-10-03

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `MIN-DEF-COMISSAO-001` | 🟠 | Corrigido | aula-01 |
| `MIN-NOM-GRUPO-001` | 🟠 | Corrigido | aula-03 |
| `MIN-ABU-MANTO-001` | 🟠 | Corrigido | aula-04 |
| `MIN-DEF-EXTRATERR-001` | 🔵 | Corrigido (reescrito com o que está confirmado) | aula-01 |

Também foram atualizados: os rodapés `alegacoes_auditaveis` das 5 aulas (campo `audit:` com data e desfecho em cada uma das 43 alegações, 41 originais e 2 da revisão didática); o hub `02-o-que-e-mineral-modulo.md` (registro); `course-state.yaml` (bloco `audit` do módulo 02).

**Pendências:** nenhuma pendência factual no módulo. Limite de acesso a fontes registrado acima.

**Aviso de baralho já importado:** não se aplica; questionário e flashcards ainda não existiam na auditoria.
