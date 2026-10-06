# Auditoria científica: Módulo 10 — Polimorfismo, politipismo, ordem-desordem e não cristalinidade

**Auditado em:** 2026-10-06
**Material:** `curso-mineralogia/10-polimorfismo/` — as 5 aulas (`-aula-01` a `-aula-05`) e as figuras 1 a 3; cruzamento com o módulo 01 (aulas 04 e 05), o módulo 02 (aulas 01 a 03), o módulo 03 (aulas 01 e 03), o módulo 04 (aula 01), o módulo 06 (aulas 03 e 04), o módulo 08 (aulas 02, 03, 05 e 06) e o módulo 09 (aulas 01 a 03); e, por nome, com o curso-geologia-avancado, módulo 40, aulas 02 e 06
**Modo:** audit-and-fix
**Profundidade:** full, com recálculo em Python das densidades relativas e volumes molares dos polimorfos, das somas de ocupação do exemplo de feldspato, das sequências de empilhamento (camadas vizinhas diferentes; equivalência ABAC = ABCB) e da perda de densidade do zircão
**Escopo:** as 41 alegações dos rodapés e as afirmações de risco do corpo: tabela de polimorfos (C, CaCO₃, SiO₂, Al₂SiO₅, TiO₂, FeS₂) com NC e densidades; classificação de Buerger; quartzo α ↔ β; paramorfos; reconstrutivas com e sem mudança de NC; ordem-desordem (dolomita, feldspatos potássicos, ortopiroxênio; convergente × não convergente); politipos (Ramsdell, ZnS, SiC, grafite, micas, regra da IMA, lonsdaleíta); amorfos, vidros, opala, vidro diaplético, metamictização (dano alfa e de recuo, zircão, definição da IMA); metaestabilidade, histerese, neomorfismo da aragonita, devitrificação, regra de Ostwald. Questionário e baralho ainda não existiam.
**Veredito:** Requer correção → **correções aplicadas; estado final: Aprovado** (nenhum achado aberto)

## Resumo

🔴 0 erros · 🟠 3 imprecisões · 🟡 6 imprecisões menores (5 nas aulas; 1 achado na checagem do questionário, ver a terceira passagem) · 🔵 1 sem fonte (detalhe removido) · ⚪ 0 controversos
Verificadas e corretas: 32 alegações dos rodapés (41 no total; ver o manifesto `.json`) e todas as contas.

O núcleo factual passou: a classificação de Buerger, os 573 °C e os ângulos do quartzo, as coordenações de Al₂SiO₅, a série sanidina–ortoclásio–microclínio, a notação de Ramsdell, os números do dano por decaimento alfa e a regra da IMA para metamícticos. Os achados são de generalização (duas regras ditas sem exceção) e de uma inconsistência interna de classificação.

**Contas conferidas (Python, 2026-10-06):**

| O quê | Resultado | Onde |
|---|---|---|
| Aragonita/calcita 2,93/2,71 | +8,1% | a01 |
| Diamante/grafite 3,51/(2,09–2,23) | +57 a +68% | a01 |
| Coesita/quartzo (2,92–3,01)/2,65 | +10 a +14% | a01 |
| Estishovita/quartzo 4,29/2,65 | +62% | a01 |
| Cianita/andaluzita 3,56/3,13; sillimanita/andaluzita 3,24/3,13 | +13,7%; +3,5% | a01 (achado 1) |
| Volumes molares (calcita 36,93; aragonita 34,16; quartzo 22,67; coesita 20,58; estishovita 14,01 cm³/mol) | coerentes com a ordem de densidade | a01 |
| Exemplo de feldspato: somas A, B, C | 1,00; 1,00; 1,00 | a02 |
| Sanidina: Al por sítio T | 0,25 | a02 |
| Sequências 2H, 3C, 4H, 6H: camadas vizinhas sempre diferentes; ABAC ≡ ABCB por troca de origem e de letras | conferido | a03, figura 2 |
| Zircão 4,65 × (1 − 0,17) | ~3,86 g/cm³ | a04 (não citado no texto) |

> [!note] Limite da verificação nesta sessão
> Como nos módulos 08 e 09, o acesso direto às fontes (*Handbook of Mineralogy*, Mindat, RRUFF, Wikipedia) estava bloqueado pelo proxy; tudo foi conferido por busca, em resultados que citam as fichas e os artigos. **Não conferido na fonte primária:** as densidades medidas de cada polimorfo (usadas como faixas, ver achado 3); a página exata dos artigos de Brøgger (1893) e Hamberg (1914), citados a partir de Ewing (1994); a autoria dos trabalhos sobre diagênese da aragonita e da sílica, citados pelo título.

## Achados

### 🟠 1. "O polimorfo de NC maior é o mais denso", sem exceção

**claim_id:** `CRQ-POL-NCDENS-001`  ·  **Tipo:** confusão de escopo  ·  **Onde:** aula 01 · Mesma fórmula, outro arranjo; Recap
**Está escrito:** "Primeira: **o polimorfo de NC maior é o mais denso** (diamante, aragonita, estishovita, cianita)."
**Problema:** a própria tabela da aula desmente a regra como absoluta: a andaluzita, com metade do Al em NC 5 (~3,13–3,16 g/cm³), é menos densa que a sillimanita, com metade do Al em NC 4 (~3,23–3,27). O aluno levaria uma regra falsa para o módulo 22.
**Correção aplicada:** "**em geral**, o polimorfo de NC maior é o mais denso [...] É uma tendência, não uma regra sem exceção: a sillimanita, com metade do Al em NC 4, é um pouco mais densa que a andaluzita, com metade do Al em NC 5, porque a densidade depende do empacotamento da estrutura inteira." O recap ganhou a mesma ressalva.
**Fonte:** notas do MIT 12.108 (coordenação do Al); densidades de Al₂SiO₅ (busca)  ·  **Confiança:** confirmado

### 🟠 2. Andaluzita → sillimanita no grupo errado

**claim_id:** `CRQ-POL-RECON-001`  ·  **Tipo:** inconsistência interna  ·  **Onde:** aula 01 · Reconstrutiva: romper e refazer, item 2
**Está escrito:** no item "O NC fica, a rede de ligações muda": "Andaluzita → sillimanita: o Al de NC 5 vai a NC 4"
**Problema:** o exemplo muda o NC e foi listado entre os que não mudam; o exemplo trabalhado (c) da mesma aula o classifica corretamente pela mudança de NC.
**Correção aplicada:** andaluzita → sillimanita passou para o item 1 ("Muda o NC"); o item 2 recebeu anatásio → rutilo (Ti sempre em octaedro, rede de octaedros refeita), coerente com o módulo 08, aula 05.
**Fonte:** MIT 12.108 (busca)  ·  **Confiança:** confirmado

### 🟡 3. Densidades da coesita e da estishovita como valor único

**claim_id:** `CRQ-POL-TABELA-001` (propagado a `CRQ-POL-CALC-001`)  ·  **Onde:** aula 01 · tabela, exemplo (d), Fontes
**Problema:** a aula usava a densidade **calculada** da coesita (2,92), enquanto a medida é ~3,0, e o curso-geologia-avancado, módulo 40, aula 02, usa ~3,00 e ~4,35. Sem a faixa, os dois cursos pareceriam se contradizer.
**Correção aplicada:** coesita ~2,9–3,0; estishovita ~4,3; "10 a 14% mais densa que o quartzo"; nas Fontes, remissão por nome ao módulo 40 do curso irmão.  ·  **Confiança:** confirmado

### 🟡 4. "Costuma deixar maclas de Dauphiné"

**claim_id:** `CRQ-POL-PARAMORFO-001`  ·  **Onde:** aula 01 · Deslocativa
**Problema:** as maclas de Dauphiné podem ser de crescimento, de transformação ou mecânicas; a frequência implicada por "costuma" não tem fonte.
**Correção aplicada:** "pode deixar".  ·  **Confiança:** confirmado

### 🟡 5. Sítios T dos feldspatos e ocorrência do ortoclásio e do microclínio

**claim_id:** `CRQ-OD-KFS-001`  ·  **Onde:** aula 02 · vocabulário; tabela da série
**Problema:** "nos feldspatos há quatro tipos" de sítio T vale para os triclínicos; nos monoclínicos há dois (T1 e T2). E a coluna de ocorrência ("ortoclásio em rochas plutônicas resfriadas a velocidade intermediária") divergia do curso-geologia-avancado, módulo 40, aula 06 (ortoclásio subvulcânico e epizonal, e metamórfico de grau moderado a alto; microclínio em pegmatitos e granitos de embasamento, e metamórfico de grau baixo a médio).
**Correção aplicada:** vocabulário com os dois casos; coluna de ocorrência alinhada ao curso irmão, sem mudar a nomenclatura de estado estrutural.  ·  **Confiança:** confirmado

### 🟡 6. "Mesma composição de qualquer outra muscovita"

**claim_id:** `CRQ-PTP-MICA-001`  ·  **Onde:** aula 03 · Exemplo trabalhado (c)
**Problema:** a muscovita é solução sólida e varia em composição; o sufixo de politipo diz que a **espécie** é a mesma.
**Correção aplicada:** "É muscovita, a mesma espécie de uma muscovita-2M₁, com 3 lâminas na repetição [...]".  ·  **Confiança:** confirmado

### 🟡 7. "Ao longo de centenas de milhões de anos"

**claim_id:** `CRQ-MET-ZIRCAO-001`  ·  **Onde:** aula 04 · Metamictização
**Problema:** o tempo para a metamictização depende do teor de U e Th e da história térmica; um número único é certeza indevida.
**Correção aplicada:** "Ao longo do tempo geológico (tanto mais depressa quanto mais U e Th o cristal tiver)".  ·  **Confiança:** confirmado (Ewing et al., 2003)

### 🔵 8. Vidro diaplético com "maclas reliquiares"

**claim_id:** `CRQ-AMO-DIAPLETICO-001`  ·  **Onde:** aula 04 · Exemplo trabalhado (d) e método geral
**Problema:** as fontes consultadas confirmam a preservação da forma e da textura do grão, não especificamente de maclas.
**Desfecho:** detalhe removido ("grão isotrópico com a forma de um cristal de plagioclásio"; "forma externa de cristal" no método). O debate sobre a natureza da maskelynita continua apresentado como pergunta aberta.

### 🟠 9. "A maior parte dos invertebrados marinhos [...] produz aragonita"

**claim_id:** `CRQ-MEST-ARAG-001`  ·  **Tipo:** confusão de escopo  ·  **Onde:** aula 05 · Quatro histórias de persistência
**Problema:** braquiópodes, equinodermos e muitos foraminíferos fazem calcita; a frase ensinaria que a aragonita é a regra dos esqueletos. A frase vinha de um resumo de artigo sobre moluscos e foi generalizada.
**Correção aplicada:** "Muitos organismos marinhos, como os corais atuais e muitos moluscos, fazem esqueleto de aragonita, que é metaestável (outros, como os equinodermos, usam calcita)."
**Fonte:** *Biogeosciences* 14, 1461 (2017); literatura de biomineralização (retomada no módulo 45)  ·  **Confiança:** confirmado

## Verificado e correto (seleção)

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `CRQ-POL-BUERGER-001` | Buerger (1951): reconstrutiva, deslocativa, ordem-desordem | IUCr, *Online Dictionary of Crystallography* | confirmado |
| `CRQ-POL-QTZAB-001` | quartzo α → β a 573 °C (1 atm); Si–O–Si ~144° → ~153°; P3₁21/P3₂21 → P6₄22/P6₂22; não temperável | The Quartz Page; IAS 1979; busca | confirmado |
| `CRQ-POL-ANDSIL-001` | metade do Al em octaedro nos três Al₂SiO₅; o resto IV (sillimanita), V (andaluzita), VI (cianita) | MIT 12.108 | confirmado |
| `CRQ-OD-DOLOMITA-001` | dolomita R3̄, camadas alternadas de Ca e Mg; calcita R3̄c | *Minerals* 2023 | confirmado |
| `CRQ-OD-OPX-001` | Fe²⁺ prefere M2; fechamento a ~300–400 °C para 1–10⁴ °C/Ma | Stimpfl, Ganguly & Molin (2005) | confirmado |
| `CRQ-PTP-RAMSDELL-001` | Ramsdell: nº de camadas + sistema; 2H, 3C, 4H, 6H, 15R | Guinier et al. (1984) | confirmado |
| `CRQ-PTP-IMA-001` | politipo não é espécie; sufixo; esfalerita e wurtzita mantidas | Nickel & Grice (1998); Hatert et al. (2023) | confirmado |
| `CRQ-MET-DANO-001` | alfa: 10–20 µm, ~100 deslocamentos; recuo ~70 keV, 30–40 nm, ~1000 | Ewing et al. (2003) | confirmado |
| `CRQ-MET-IMA-001` | metamíctico é mineral se era cristalino e de mesma composição | Nickel (1995) | confirmado |
| `CRQ-MEST-VIDRO-001` | nenhuma obsidiana inalterada mais antiga que o Cretáceo | Britannica; Oregon State | confirmado |

## Consistência interna e com o resto do curso

- **Módulo 02:** polimorfos como espécies distintas (aula 03); opala como mineraloide com nome na lista da IMA, opala-A amorfa e opala-CT parcialmente ordenada (aula 02); "normalmente cristalino" (aula 01) — a aula 04 daqui acrescenta o caso metamíctico sem contradizer.
- **Módulo 03:** coesita de Dora Maira (aula 03) e bridgmanita que amorfiza na descompressão (aula 01) — reaproveitadas nas aulas 04 e 05.
- **Módulo 04, aula 01:** cristal × agregado × amorfo; obsidiana e opala-A amorfas — mesma leitura.
- **Módulo 06:** quartzo 2,65 e calcita 2,71 g/cm³ (aula 04); aragonita Pmcn e calcita R3̄c (aula 03).
- **Módulo 08:** rutilo, brookita e anatásio com 2, 3 e 4 arestas compartilhadas (aula 05); estishovita com estrutura de rutilo (aula 06); empilhamentos ABAB e ABCABC e esfalerita/wurtzita (aulas 03 e 06) — base da aula 03 daqui.
- **Módulo 09:** dolomita ordenada (aula 03), sítios M1 e M2 do piroxênio (aula 05) — retomados na aula 02.
- **curso-geologia-avancado, módulo 40** (por nome): 573 °C a 1 atm; deslocativa × reconstrutiva; sanidina, ortoclásio e microclínio pela distribuição do Al e pela simetria; macla em grade como consequência da inversão. Depois dos achados 3 e 5, nenhuma divergência.
- **Internamente:** a classificação da aula 01 é usada sem contradição nas aulas 02 e 05; o objetivo novo `mineralogia-m10-oa05` (aula 05) recebeu o próximo ID livre.

## Correções aplicadas

**Aplicadas em:** 2026-10-06

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `CRQ-POL-NCDENS-001` | 🟠 | Corrigido | aula-01 |
| `CRQ-POL-RECON-001` | 🟠 | Corrigido | aula-01 |
| `CRQ-POL-TABELA-001` | 🟡 | Corrigido (propagado ao exemplo e às Fontes) | aula-01 |
| `CRQ-POL-PARAMORFO-001` | 🟡 | Corrigido | aula-01 |
| `CRQ-OD-KFS-001` | 🟡 | Corrigido | aula-02 |
| `CRQ-PTP-MICA-001` | 🟡 | Corrigido | aula-03 |
| `CRQ-MET-ZIRCAO-001` | 🟡 | Corrigido | aula-04 |
| `CRQ-AMO-DIAPLETICO-001` | 🔵 | Corrigido (detalhe removido) | aula-04 |
| `CRQ-MEST-ARAG-001` | 🟠 | Corrigido | aula-05 |
| `CRQ-POL-AL2SUP-001` | 🟡 | Corrigido na terceira passagem (afirmação evitada) | questionario-final, aula-01 |

Também foram atualizados: os rodapés `alegacoes_auditaveis` das aulas (campo `audit:`), o hub do módulo e o `course-state.yaml` (bloco `audit` do 10).

**Pendências:** nenhuma. Não há questionário nem baralho a propagar (ainda não existiam).

## Segunda passagem (depois da revisão didática)

**Em:** 2026-10-06. A revisão didática acrescentou quatro trechos, conferidos aqui:

- **aula 01, erros comuns:** "quem decide é a estrutura (pela difração, módulo 18), não a análise química" — correto: polimorfos têm a mesma composição; não há fato numérico novo.
- **aula 01, tabela:** "arcabouço: rede de ligações nas três direções" — definição, coerente com o diamante como C em NC 4 nas três direções (módulo 01, aula 04).
- **aula 04:** "1 MeV = 1000 keV" — conversão de unidade, correta.
- **aula 04:** "fratura conchoidal (em superfícies curvas, como a de um vidro quebrado)" — definição corrente (Klein & Dutrow), retomada no módulo 13.

**Pendências:** nenhuma.

## Terceira passagem: checagem científica do questionário e do baralho

**Em:** 2026-10-06, antes de marcar o módulo como concluído (lição dos módulos anteriores: questionário e baralho precisam de checagem própria).

**Questionário final (15 questões, 37 pontos).** Cada gabarito foi refeito contra as aulas corrigidas e as contas foram recalculadas em Python: cianita/andaluzita +13,7%; sillimanita/andaluzita +3,5%; ocupações da Q3 (soma 1,00; T1 = 0,62; T1o = T1m); equivalência ABAC = ABCB por script. Nenhum distrator é defensável como correto (na Q6, aragonita, diamante e sanidina persistem na superfície; só o quartzo-β não). A matriz foi recontada: 7 + 6 + 7 + 7 + 10 = 37 (a primeira versão trazia 8 e 9 nas linhas de `oa01` e `oa05`, corrigido antes de fechar).

**Achado da checagem, corrigido (🟡, `CRQ-POL-AL2SUP-001`):** a primeira versão da Q13 (d) dizia que a cianita é metaestável num afloramento e que a andaluzita é a forma estável "a baixa pressão e temperatura moderada". Qual polimorfo de Al₂SiO₅ é estável a 25 °C e 1 atm depende da extrapolação da curva cianita–andaluzita abaixo da faixa calibrada (Holdaway, 1971; Pattison, 1992), e as buscas não deram resposta confiável. Para não ensinar um ponto não verificado, a questão passou a usar a **sillimanita**, cujo campo é de alta temperatura (módulo 03, aula 03), e a pergunta "Pare e explique" da aula 01 foi ajustada pelo mesmo motivo ("sillimanita, formada em alta temperatura, numa rocha que hoje está fria"). Nenhum card afirma a estabilidade de Al₂SiO₅ na superfície.

**Baralho (70 Basic + 8 Cloze).** Cada card foi rastreado até a frase da aula de origem; as nove correções da auditoria aparecem só na versão corrigida; nenhum número fora das aulas (densidades, 573 °C, 144°/153°, 0,25 Al por sítio T, 300–400 °C, 6H, 2M₁, ~30 Å, ~100 e ~1000 deslocamentos, 17%, 1893, Cretáceo). Resultado: 0 🔴, 0 🟠. `validate_flashcards.py`: 0 erros, 0 avisos depois de uma quase-duplicata reformulada.

**Pendências:** nenhuma.
