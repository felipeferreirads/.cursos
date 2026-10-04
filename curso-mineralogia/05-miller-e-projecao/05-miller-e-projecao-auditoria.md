# Auditoria científica: Módulo 05 — Eixos cristalográficos, índices de Miller e projeção estereográfica

**Auditado em:** 2026-10-04
**Material:** `curso-mineralogia/05-miller-e-projecao/` — as 6 aulas planejadas (`05-miller-e-projecao-aula-01` a `-aula-06`) e as figuras 1 a 8; na segunda passagem, a aula 07 criada pela revisão didática e a figura 9
**Modo:** audit-and-fix
**Profundidade:** full, com conferência numérica de todos os índices, eixos de zona, ângulos e distâncias estereográficas (Python, frações exatas e trigonometria), e conferência dos parâmetros de cela no *Handbook of Mineralogy*
**Escopo:** as alegações dos rodapés `alegacoes_auditaveis` e as afirmações de risco do corpo: convenções de eixos e ângulos (α, β, γ), relações de parâmetros por sistema, parâmetros de cela de seis minerais, receita de Miller e exemplos, multiplicidade das formas cúbicas e tetragonais, regra i = −(h + k), conversão de direções [uvtw] ↔ [UVW], indexação da clivagem da calcita, lei das zonas e regra da cruz, construção estereográfica r = R·tan(ρ/2), convenção φ/ρ, datas (Miller 1839; Wulff 1902), ângulos do cubo e do quartzo. Questionário e baralho ainda não existiam.
**Veredito:** Requer correção → **correções aplicadas; estado final: Aprovado** (nenhum achado aberto)

## Resumo

🔴 0 erros · 🟠 2 imprecisões (uma achada na terceira passagem) · 🟡 3 imprecisões menores · 🔵 1 sem fonte · ⚪ 0 controversos
Verificadas e corretas: 43 alegações dos rodapés (47 no total, incluídas as 6 da aula 07 na segunda passagem; ver o manifesto `.json`), todas as contas dos exemplos trabalhados e a geometria das nove figuras.

O núcleo formal passou sem erro: as receitas (interceptos → inversos → inteiros; i = −(h + k); lei das zonas hu + kv + lw = 0; regra da cruz), todos os exemplos numéricos e as figuras, que foram **geradas por cálculo** (vetores normais projetados por r = R·tan(ρ/2)) e não desenhadas à mão. Os achados estão onde a regra geral encontra um caso particular (a classe 4̄3m na tabela de eixos) e em generalizações sem fonte.

**Contas conferidas (Python, 2026-10-04):**

| O quê | Resultado | Onde aparece |
|---|---|---|
| Interceptos → índices: 1a:2b:∞c; 2a:3b:6c; 1a:−1b:½c; 2a:∞b:−1c; ½a:1b:∞c | (210); (321); (11̄2); (102̄); (210) | aula 02 |
| (231) → interceptos | 3a : 2b : 6c | aula 02 |
| Cúbico: (100)∧(111), (100)∧(110), (111)∧(11̄1), (110)∧(011) | 54,74°; 45,00°; 70,53°; 60,00° | aulas 05, 06 |
| Zircão (a = 6,607, c = 5,982 Å): ρ(101); (101)∧(011) | 42,16°; 56,67° | conferência de c/a, aula 01 |
| Quartzo (a = 4,9133, c = 5,4053 Å): c/a; ρ(r); m∧r; r∧z; r∧r′ | 1,1001; 51,79°; 38,21°; 46,27°; 85,76° | aula 06, figura 8 |
| Calcita (a = 4,9896, c = 17,0610 Å): c/a; c/(4a); ângulo da clivagem {101̄4} | 3,419; 0,855; 74,94° (105,06° interno) | aula 03 (equivalência {101̄4} ↔ {101̄1}) |
| Eixos de zona: (100)×(111); (101)×(011) [quartzo r, z]; face comum a [01̄1] e [001] | [01̄1]; [1̄1̄1]; (1̄00) | aula 04 |
| Pertença: (011) e (110) em [01̄1]; (11̄0) e (100) em [1̄1̄1] | 0 e −1; 0 e −1 | aula 04 |
| Direções: [21̄1̄0] → [UVW] | [300] = [100] (a₁); apagar t daria [21̄0] ≠ a₁ | aula 03 |
| r/R = tan(ρ/2) para 0°, 30°, 45°, 54,7°, 60°, 90° | 0; 0,268; 0,414; 0,518; 0,577; 1 | aula 05 |
| Formas gerais (fechamento do grupo): 2/m, mm2, 4/m, 4mm, 422, 4/mmm, 4̄, 6̄ | 4; 4; 8; 8; 8; 16; 4; 6 polos, com a distribuição cheio/aberto citada | aula 07, figura 9 |

> [!note] Limite da verificação nesta sessão
> O acesso direto a sites (handbookofmineralogy.org, mindat.org, rruff, Wikipedia, IUCr) estava bloqueado pelo proxy de rede. Os parâmetros de cela foram conferidos por **busca na web**, cujos resultados citam as fichas em PDF do *Handbook of Mineralogy* (halita a = 5,6404; quartzo a = 4,9133, c = 5,4053; calcita a = 4,9896, c = 17,0610; zircão a = 6,607, c = 5,982; forsterita a = 4,7540, b = 10,1971, c = 5,9806; cianita a = 7,1262, b = 7,8520, c = 5,5724, α = 89,99°, β = 101,11°, γ = 106,03°; rutilo a = 4,5937, c = 2,9587). A razão axial morfológica clássica da calcita (c/a = 0,8543) e o fator 4 entre as celas morfológica e estrutural foram confirmados por busca. A convenção φ a partir de (010) no sentido horário e ρ a partir de c foi confirmada no material de S. A. Nelson (Tulane, EENS 211); a data da rede de Wulff (1902), no *IUCr Newsletter* 30(2); Miller (1839), em biografias (Britannica, Oxford Reference). Não houve acesso ao texto integral de Klein & Dutrow nem das *International Tables*; as convenções gerais (eixos por sistema, símbolos gráficos, multiplicidades) foram conferidas por consistência interna e pelo conhecimento consolidado. Os valores clássicos dos ângulos do quartzo em graus e minutos (38°13′, 46°16′, 85°46′) **não** foram achados na fonte; por isso a aula 06 usa só os valores calculados a partir da cela.

## Achados

### 🟠 1. Eixos do cúbico "ao longo dos três eixos 4", esquecendo o 4̄

**claim_id:** `CRI-EIX-POSICAO-001`
**Tipo:** omissão que gera erro
**Onde:** aula 01 · tabela "A tabela que esta aula entrega", linha Cúbico
**Está escrito:** "ao longo dos três eixos 4 (ou dos três eixos 2, nas classes 23 e m3̄, que não têm eixo 4)"
**Problema:** a classe 4̄3m (esfalerita, tetraedrita, do módulo 04) não tem eixo 4 de rotação, e sim três eixos 4̄; os eixos cristalográficos ficam ao longo deles. Como estava, um aluno com esfalerita na mão não acharia "eixo 4" nem estaria nas exceções listadas.
**Correção aplicada:** "ao longo dos três eixos 4 ou 4̄ (ou dos três eixos 2, nas classes 23 e m3̄, que não têm nem 4 nem 4̄)"
**Fonte:** *International Tables for Crystallography*, vol. A (direções de simetria do sistema cúbico)  ·  **Nível:** normativa
**Confiança:** confirmado
**Também aparece em:** só na aula 01.

### 🟡 2. "Ângulos entre faces equivalentes" de halita, fluorita e galena

**claim_id:** `CRI-EIX-RAZAO-001`  ·  **Tipo:** imprecisão  ·  **Onde:** aula 01 · Razão axial e lei de Steno
**Problema:** "faces equivalentes" (da mesma forma, no mesmo cristal) não é o que se queria dizer; o ponto é que o ângulo entre faces de **mesmos índices**, como (100) e (111), é o mesmo em todo mineral cúbico.
**Correção aplicada:** "o ângulo entre duas faces de mesmos índices, como (100) e (111), é exatamente o mesmo na halita, na fluorita e na galena".  ·  **Confiança:** confirmado (cálculo).

### 🟡 3. Sinônimo "Bravais-Miller" não registrado

**claim_id:** `CRI-MB-INDICE-001`  ·  **Tipo:** inconsistência interna (entre módulos)  ·  **Onde:** aula 03 · Vocabulário
**Problema:** a auditoria do módulo 04 (achado 🟠 3) reservou o nome "Bravais-Miller" para os índices hkil e prometeu que o módulo 05 os ensinaria; o módulo 05 usava só "Miller-Bravais". Os dois nomes circulam na literatura; sem registrar os dois, o aluno acharia que são coisas diferentes.
**Correção aplicada:** "(também chamados de Bravais-Miller)" no verbete.  ·  **Confiança:** confirmado.

### 🟡 4. "Redes impressas têm linhas a cada 2°"

**claim_id:** `CRI-WUL-REDE-001`  ·  **Tipo:** certeza indevida  ·  **Onde:** aula 06 · Como a rede funciona
**Problema:** 2° é o espaçamento usual, não uma regra; há redes de 1° e de 10°.
**Correção aplicada:** "costumam ter linhas a cada 2°".  ·  **Confiança:** confirmado.

### 🔵 5. β "sempre entre 90° e 130°" em feldspatos, piroxênios e micas

**claim_id:** `CRI-EIX-BETA-001`
**Tipo:** evidência insuficiente
**Onde:** aula 01 · observação "No monoclínico, b é o eixo especial"
**Está escrito:** "Por isso os parâmetros de feldspatos, piroxênios e micas aparecem sempre com um β entre 90° e 130°."
**Problema:** a generalização ("sempre", três grupos inteiros) não foi conferida espécie a espécie nesta sessão; só o ortoclásio (116,07°) foi.
**Correção aplicada:** a frase foi substituída pelo exemplo conferido: "como os 116,1° do ortoclásio na tabela abaixo". Não há perda de conteúdo para o objetivo da aula.
**Confiança:** não verificado (removido).

## Verificado e correto (seleção das alegações de maior risco)

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `CRI-EIX-ANGULOS-001` | α = b∧c, β = a∧c, γ = a∧b | *Int. Tables* A | confirmado |
| `CRI-EIX-TABELA-001` | relações de parâmetros e nº de parâmetros independentes (1, 2, 3, 2, 4, 6) | *Int. Tables* A | confirmado |
| `CRI-EIX-PARAM-001` | parâmetros de halita, zircão, quartzo, forsterita, cianita (o ortoclásio foi trocado pelo diopsídio na terceira passagem, achado 6) | *Handbook of Mineralogy* (busca) | confirmado |
| `CRI-MIL-HIST-001` | Weiss (início do séc. XIX); Miller, 1839 | biografias por busca | confirmado |
| `CRI-MIL-EXEMPLOS-001` | índices dos exemplos da aula 02 | cálculo | confirmado |
| `CRI-MIL-FORMAS-001` / `-PIRITOEDRO-001` | {100} 6, {111} 8, {110} 12, geral 48; {210} 12 em m3̄ e 24 em m3̄m | *Int. Tables* A | confirmado |
| `CRI-DIR-NORMAL-001` | [hkl] ⟂ (hkl) só no cúbico; contraexemplos tetragonal e monoclínico | geometria | confirmado |
| `CRI-MB-DIRECAO-001` | [uvtw] → [UVW]; a₁ = [21̄1̄0] = [100] | cálculo | confirmado |
| `CRI-MB-CALCITA-001` | clivagem {101̄4} (estrutural) = {101̄1} (morfológica) | HoM; razão 0,8543 × 4 = 3,419 | confirmado |
| `CRI-ZON-WEISS-001` | lei das zonas e dedução pelo plano hx + ky + lz = 0 | Klein & Dutrow | confirmado |
| `CRI-ZON-QUARTZO-001` | zona r–z = [1̄1̄1], contém m(11̄00) e m(1̄100) | cálculo + figura 8 | confirmado |
| `CRI-EST-CONSTR-001` | r = R·tan(ρ/2); projeção pelo polo oposto | Whittaker (IUCr) | confirmado |
| `CRI-EST-CONV-001` | c no centro, (010) à direita, φ horário a partir de (010) | Nelson (Tulane) | confirmado |
| `CRI-EST-WULFF-001` | rede de Wulff, 1902; Schmidt de igual área | *IUCr Newsletter* 30(2) | confirmado |
| `CRI-WUL-CUBICO-001` | ângulos do cubo | cálculo | confirmado |
| `CRI-WUL-QUARTZO-001` | m∧r 38,2°, r∧z 46,3°, ρ(r) 51,8° | cálculo a partir do HoM | confirmado (valores em minutos: provável, fora do texto) |

## Consistência interna e com o resto do curso

- **Módulo 04, aula 01:** ângulo interfacial entre normais e ângulo interno somando 180° — a aula 06 usa a mesma convenção (m∧r = 38,2°, interno 141,8°); o prisma hexagonal a 60° entre normais confere com m∧m = 60°.
- **Módulo 04, aula 06:** pontas do quartzo como dois romboedros alternados — aulas 03 e 06 dão os índices (r {101̄1}, z {011̄1}) e a figura 8 mostra a alternância a 60°.
- **Módulo 04, aula 07:** forma geral de m3̄m com 48 faces e de 4/mmm com 16; {100} como forma especial — aulas 02 e 07 coerentes.
- **Módulo 04, auditoria (achado 3):** "Bravais-Miller" = hkil — coerente agora (achado 3 acima).
- **Figuras:** as nove figuras foram geradas por script a partir dos vetores; cada número escrito numa figura (51,8°; 38,2°; 46,3°; contagens de polos) sai do mesmo cálculo que o texto usa.

## Correções aplicadas

**Aplicadas em:** 2026-10-04

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `CRI-EIX-POSICAO-001` | 🟠 | Corrigido | aula-01 |
| `CRI-EIX-RAZAO-001` | 🟡 | Corrigido | aula-01 |
| `CRI-MB-INDICE-001` | 🟡 | Corrigido | aula-03 |
| `CRI-WUL-REDE-001` | 🟡 | Corrigido | aula-06 |
| `CRI-EIX-BETA-001` | 🔵 | Corrigido (afirmação substituída por exemplo conferido) | aula-01 |

Também foram atualizados: os rodapés `alegacoes_auditaveis` das aulas (campo `audit:`), o hub do módulo e o `course-state.yaml` (bloco `audit`).

## Segunda passagem (depois da revisão didática)

**Em:** 2026-10-04. A revisão didática dividiu a aula 05 (a simetria no estereograma virou a **aula 07**, nova), pôs as direções de quatro índices da aula 03 numa nota de consulta, corrigiu duas remissões de módulo e acrescentou frases de orientação ("tabela de consulta", "se a dedução pesar, guarde a regra"). O exemplo trabalhado da aula 05 foi refeito (polos de (001), (010), (100), (011), (101), (111) do cubo). Alegações novas ou movidas, conferidas:

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `CRI-EST-111-001` | (111) ρ 54,7°, φ 45°, r 0,518 R; (011) e (101) a ρ 45°, r 0,414 R; (001), (011), (010) na zona [100] | cálculo | confirmado |
| `CRI-ESS-SIMBOLOS-001` | espelho = grande círculo cheio; primitivo cheio se há espelho horizontal; elipse 2, triângulo 3, quadrado 4, hexágono 6 | *Int. Tables* A | confirmado |
| `CRI-ESS-HEMISF-001` | operações que trocam o hemisfério | geometria das operações | confirmado |
| `CRI-ESS-FORMAS-001` | polos da forma geral de 2/m, mm2, 4/m, 4mm, 422, 4/mmm, 4̄, 6̄ | fechamento de grupo em Python | confirmado |
| `CRI-ESS-POLAR-001` | mm2 polar; hemimorfita Imm2 | auditoria do módulo 04 | confirmado |
| `CRI-ESS-CUBO-001` | m3̄m: 9 espelhos; eixos 4, 3, 2 nos polos de {100}, {111}, {110} | *Int. Tables* A; figura 6 | confirmado |

**Pendências:** nenhuma.

**Aviso de baralho já importado:** não se aplica; questionário e flashcards ainda não existiam.

## Terceira passagem (durante a escrita do módulo 06)

**Em:** 2026-10-04. Ao preparar o exemplo de densidade do módulo 06 (aula 04), o ortoclásio da tabela da aula 01 deu densidade calculada de 2,540 g/cm³, contra 2,563 calculada pelo próprio *Handbook of Mineralogy*; a discrepância levou a reabrir o parâmetro c.

### 🟠 6. Parâmetro c do ortoclásio suspeito

**claim_id:** `CRI-EIX-PARAM-001`
**Tipo:** evidência insuficiente que gera erro (valor numérico de referência não confirmado)
**Onde:** aula 01 · tabela "Minerais reais, números reais" e exemplo trabalhado (B); questionário final, Q26
**Está escrito:** "ortoclásio: a = 8,563 Å; b = 12,963 Å; c = 7,299 Å; β = 116,1°"
**Problema:** a busca devolveu c = 7,299(11) Å como sendo do *Handbook of Mineralogy*, mas esse valor não fecha: com ele, o volume é ~728 Å³, o que dá densidade de 2,540, enquanto o HoM declara D(calc.) = 2,563; o volume listado junto (724,57 Å³) também não fecha com β = 116,07°; e outras determinações de ortoclásio dão c ≈ 7,20 Å (por exemplo a = 8,525, b = 13,028, c = 7,200 Å, β = 116,06°). Sem acesso ao PDF, não foi possível decidir qual é o valor do HoM. Um parâmetro de referência que não se consegue confirmar não fica na aula.
**Correção aplicada:** o ortoclásio saiu da tabela, do exemplo (B) e da observação sobre β obtuso; entrou o **diopsídio**, de parâmetros conferidos por busca e coerentes entre si (a = 9,746 Å, b = 8,899 Å, c = 5,251 Å, β = 105,63°, C2/c, Z = 4; volume 438,6 Å³ e densidade calculada 3,28 g/cm³). A Q26 do questionário final foi refeita com o diopsídio (o gabarito não muda). Nenhum card do baralho usava o ortoclásio.
**Fonte:** *Handbook of Mineralogy*, fichas de diopsídio e ortoclásio (D(calc.) = 2,563), por busca em 2026-10-04  ·  **Nível:** base de referência
**Confiança:** confirmado (para o diopsídio); não verificado (para o c do ortoclásio, que saiu do texto)
**Também aparece em:** `_contexto.md` não cita parâmetros; o módulo 36 (feldspatos) deve conferir o c do ortoclásio na fonte primária antes de usá-lo.

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `CRI-EIX-PARAM-001` | 🟠 | Corrigido (mineral trocado) | aula-01, questionario-final |

O achado 🔵 5, mais acima, cita "os 116,1° do ortoclásio" como a correção então aplicada; depois desta passagem, a frase da aula passou a citar "os 105,6° do diopsídio".

**Pendências:** nenhuma.
