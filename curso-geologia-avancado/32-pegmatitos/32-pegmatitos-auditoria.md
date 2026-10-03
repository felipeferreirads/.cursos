# Auditoria científica — Módulo 32 (Pegmatitos) — RELATÓRIO CONSOLIDADO (Aulas 01–26)

**Data da consolidação:** 2026-09-28
**Modo:** audit-and-fix · **Profundidade:** full
**Lotes:** A = Aulas 01–09 (2026-09-24) · B = Aulas 10–17 (Aulas 10–15 corrigidas em 2026-09-24; relatório, reverificação e Aulas 16–17 em 2026-09-28) · C = Aulas 18–26 (2026-09-28)
**Detalhe por achado:** `32-pegmatitos-auditoria-lote-A.md`, `-lote-B.md`, `-lote-C.md` · **Manifesto:** `32-pegmatitos-auditoria.json` (165 achados, um registro por achado)
**Material derivado:** o módulo não tinha questionário, flashcards nem glossário quando a auditoria rodou; nenhuma propagação externa e nenhum card no Anki a corrigir. Busca no curso inteiro por Borrachudos, Volyn, Jegdalek, Panebianco, Princesa Brasileira e schorlita: fora do módulo 32 só aparece o título da Aula 24 em `00-progresso-do-aluno.md`, sem erro.

## Veredito

**Aprovado após correções.** Nenhum achado 🔴, 🟠 ou 🟡 em aberto. Os 🔵 e ⚪ foram confirmados, retirados ou reescritos com a incerteza explícita no texto. **O gate para `gerador-de-questionarios` e `gerador-de-flashcards` está liberado**, com as restrições obrigatórias listadas no fim deste relatório.

## Totais

| Severidade | Lote A | Lote B | Lote C | Consolidação | **Total** | Em aberto |
|---|---|---|---|---|---|---|
| 🔴 Erro | 10 | 7 | 8 | 0 | **25** | 0 |
| 🟠 Impreciso | 38 | 36 | 27 | 1 | **102** | 0 |
| 🟡 Desatualizado | 2 | 3 | 6 | 0 | **11** | 0 |
| 🔵 Sem fonte | 7 | 6 | 5 | 0 | **18** | 0 |
| ⚪ Controverso | 4 | 2 | 3 | 0 | **9** | 0 |
| **Total** | **61** | **54** | **49** | **1** | **165** | **0** |

Desfechos (manifesto): 136 corrigidos, 8 corrigidos com ressalva, 8 reescritos mostrando as posições, 7 removidos, 5 resolvidos por verificação, 1 tratado com ressalva nas Fontes (A07-7).

**Achado da consolidação (CONS-1, 🟠 bibliográfico):** o lote A deixara para a consolidação o recheque das citações feitas de memória. No Crossref: Atencio et al. (2010) estava como *Mineralogical Magazine* 74:1041-1060; o correto é ***The Canadian Mineralogist* 48:673-698** — corrigido na Aula 04 (claim `PEG-M32-A04-BIB-ATENCIO-015`). Confirmadas sem alteração: London (2005), *Lithos* 80:281-303; London et al. (1993), *CMP* 113:450-465; London (2013), *Rocks & Minerals* 88:527-538; Van Lichtervelde et al. (2007), *Econ. Geol.* 102:257-276; Che et al. (2015), *Ore Geol. Rev.* 65:979-989; Webber et al. (1997), *J. Petrol.* 38:1777-1791; Martin & De Vito (2005), *Can. Mineral.* 43:2027-2048. Não indexadas pelo Crossref na consulta, mantidas por consistência com a literatura secundária: London (1986, *Am. Mineral.* 71:376-395), London (1992, *Can. Mineral.* 30:499-540), Fenn (1977), Swanson (1977).

**Pendências herdadas do lote A:** A01-5 (parental de Greenbushes e Pilgangoora) e o controle estrutural adiado da Aula 08 foram **resolvidos** no lote B (B13-1, B13-3), com a Aula 01 e a Aula 13 coerentes. A07-7 (associação de campos sveconoruegueses a metamorfismo de alta P e alta T, não conferida no texto integral de Rosing-Schow et al. 2023) permanece como estava: tratada com ressalva nas Fontes da Aula 07, baixo impacto, não bloqueia.

## Inversões de sentido perigosas — lista única do módulo

São os pontos em que um aluno que leu uma versão antiga, ou que raciocina por intuição, erraria. O questionário e o baralho devem cobri-los.

**Lote A (Aulas 01–09)**
1. A monazita **não** fica metamítica (A09-3).
2. Trebilcock e 44069 são padrões de **monazita**, não de columbita-tantalita nem de cassiterita (A09-1, A09-2).
3. Pet = Spd + 2 Qtz e Spd = Ecr + Qtz (A04-1).
4. **Classe** = profundidade/fácies; o que varia dentro de um campo é o **tipo** (A05-7).
5. "Espodumênio secundário" = espodumênio **formado** por substituição (A02-2).
6. O paradoxo dos cristais gigantes **não** está resolvido (A06-2).

**Lote B (Aulas 10–17)**
7. Borrachudos (~1,7 Ga) é **paleoproterozoica** (estateriana), não mesoproterozoica (B17-1).
8. Kings Mountain é **mississippiano**, não arqueano (B14-4).
9. Spruce Pine: 377–404 Ma, orogenia **acadiana**; a colisão África–América do Norte é posterior (B14-7).
10. Manono está no **Cinturão Kibara**, não no cráton do Congo (B15-3).
11. Bikita está **em operação**, não exaurida (B12-8); Tanco é quase **cego**, não aflorante (B12-1).
12. Spruce Pine **não** é fonte de berílio (B11-6).
13. Tanco e Bikita são ambos **subtipo petalita**; diferem na fase de Li explotada (B12-6).

**Lote C (Aulas 18–26)**
14. LCT = lítio-césio-tântalo; a elbaíta **não** deu nome à família (C23-1).
15. Elbaíta: nome de **Vernadsky** (1913); Rosina = localidade do **neótipo** (C23-2).
16. Volyn é **NYF**, não LCT (C24-1).
17. Shigar/Dassu na placa **asiática** (Caracórum); só Haramosh/Stak no maciço Nanga Parbat-Haramosh (C21-1).
18. Idade de um pegmatito **não** é duração da cristalização (C21-3).
19. Xuxa e Barreiro são **reservas**; Colina e o total de Grota do Cirilo são **recursos** (C19-1).
20. Complexo e albita-espodumênio são **tipos**; o tipo albita-espodumênio **não** é o gemífero (C18-1).

## Padrão dominante

O mesmo dos módulos 27–31: os erros graves estavam em frases de ligação, síntese e comparação que soavam seguras e **não** constavam da lista de alegações de risco do redator (a etimologia de LCT, o autor da elbaíta, a família de Volyn, a placa de Shigar, a idade "mesoproterozoica" de 1,7 Ga, a categoria de Xuxa). Nos estudos de caso gemológicos (Aulas 18, 21–24) o redator se apoiou em fontes de divulgação e de localidade, e foi ali que se concentraram as falhas de atribuição. Nos estudos de caso de metais raros (Aulas 12–16) o padrão foi número desatualizado (recursos, status de minas).

## Arquivos alterados

- Aulas 01–26 (todas), `32-pegmatitos-modulo.md` (status e registro do módulo).
- Relatórios: `32-pegmatitos-auditoria-lote-A.md` (existente), `-lote-B.md` e `-lote-C.md` (novos), este consolidado e o manifesto `.json`.
- `course-state.yaml`: bloco `audit` do módulo 32 e `content_hash` das 26 aulas.

## Alegações rastreadas

166 `claim_id` nos rodapés das 26 aulas, sem duplicata (contados por script em 2026-09-28). Criados pela auditoria nos lotes B e C: A18-007, A18-008, A18-009, A20-006, A21-006, A21-007, A22-007, A24-005, A26-007; na consolidação: A04-015. Nenhum `claim_id` foi renumerado; o ID atípico `PEG-M32-A18-SAPUCAIA-0025`, do redator, foi mantido.

## Restrições obrigatórias para o questionário e os flashcards

1. Usar nomes IMA: columbita-(Fe), columbita-(Mn), tantalita-(Fe), tantalita-(Mn), com o antigo entre parênteses na primeira ocorrência; microlita como grupo; schorl (não "schorlita"); polucita ·2H₂O; UST (não USST).
2. Cobrar a distinção **classe × tipo × família** (Černý & Ercit 2005); LCT/NYF são de Černý (1991a); família mista de Černý & Ercit (2005).
3. Nunca apresentar como fato fechado: o paradoxo dos cristais gigantes, as taxas de cristalização (Aula 10), a idade de Greenbushes, a idade dos pegmatitos de Murzinka, a origem de Koktokay nº 3 (evolução longa × eventos sucessivos).
4. Diferenças entre geocronômetros (U-Pb × Ar-Ar) medem **resfriamento**, não duração; Ar-Ar em muscovita é idade mínima.
5. Números de recurso, reserva e produção sempre com **categoria e data**; nunca comparar reserva com recurso.
6. Não perguntar a causa geológica da pureza do quartzo de Spruce Pine (não está estabelecida); não aceitar "ambiente seco".
7. Rubi de Hunza, Nangimali e Jegdalek: metamórfico em mármore, sem fundido pegmatítico (Garnier et al. 2008) — sem afirmar que "a literatura é explícita" nem que são "dolomíticos".
8. "Paraíba" é nome de variedade (LMHC), não certificado de procedência.
9. Volyn é NYF; Alto Ligonha é LCT com algumas afinidades NYF; Anjanabonoina é família mista.
10. Borrachudos e Santa Maria de Itabira: paleoproterozoicos (estaterianos).
11. G1 630–585, G2 585–560, G3 ~540–500, G4 ~535–500, G5 ~520–490 Ma; a idade de 467 Ma do Ipê é de um corpo só.
12. Não cobrar os dados marcados como hipotéticos nos exemplos trabalhados (Aulas 05, 09, 10, 11) como se fossem reais.
