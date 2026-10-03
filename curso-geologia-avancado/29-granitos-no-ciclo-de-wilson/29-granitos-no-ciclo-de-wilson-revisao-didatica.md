# Revisão didática: Módulo 29 — Granitos no ciclo de Wilson

**Revisado em:** 2026-09-23  ·  **Modo:** review-and-fix
**Material:** `29-granitos-no-ciclo-de-wilson/` (hub + 6 aulas; nenhuma aula dividida)
**Veredito:** Bem ensinado com ressalvas (todas corrigidas nesta passagem)

A revisão rodou depois da auditoria científica do mesmo dia, que levantou 2 vermelhos, 10 laranjas, 2 azuis e 2 brancos, todos tratados (ver [[29-granitos-no-ciclo-de-wilson-auditoria|relatório de auditoria]]). A auditoria encaminhou três observações de escopo: a carga das Aulas 01 e 05, o crescimento da Aula 06 e a clareza do rótulo sin/pós-colisional na Aula 04. Todas foram examinadas aqui (ver "Carga e divisão").

## Resumo

🔴 0 bloqueiam · 🟠 2 prejudicam · 🟡 8 atrito · 🔵 3 sugestões

**Carga estimada** (palavras do corpo, de `## Conteúdo` a `## Fontes`, a ~84 palavras/min, contadas por script depois da última edição):

| Aula | Palavras | Duração | Conceitos novos centrais | Exemplos |
|---|---|---|---|---|
| 01 | 1998 | ~24 min | 4 (descontinuidades, tomografia, litosfera/LAB, envelope de resistência) | 2 (refração; transição frágil-dúctil) |
| 02 | 1610 | ~19 min | 3 (ciclo de Wilson, regime → granito, geração × colocação) | 1 (três corpos) |
| 03 | 1515 | ~18 min | 3 (geometria da placa, Sm/Yb-Dy/Yb, contribuição crustal isotópica) | 1 (razão inicial de Sr) |
| 04 | 1452 | ~17 min | 3 (Iapetus/Rheic, tipo caledoniano, tipo varisco e suas exceções) | 1 (intervalos) |
| 05 | 1960 | ~23 min | 4 (critérios I/S, critérios A, Frost, ASI) | 2 (três análises; Sr de granito S) |
| 06 | 1904 | ~23 min | 4 (fusão, ascensão, colocação, gravimetria) + metalogênese | 1 (gravimetria em dois modelos) |
| **Total** | **10439** | **~124 min** | | |

---

## Carga e divisão

**Nenhuma aula foi dividida.** Todas ficam abaixo de 25 min e de 2000 palavras. No Módulo 28, a divisão foi decidida para uma aula de ~31 min com seis blocos independentes. As três candidatas aqui ficam bem abaixo disso:

- **Aula 01 (~24 min):** tem quatro blocos, mas eles formam um arco único (do modelo em camadas à reologia), exigido inteiro pelo OA-01, e há dois exemplos numéricos que dão pausa. Dividir produziria uma "aula de sismologia" sem granito, que se sustentaria mal sozinha num módulo de granitos.
- **Aula 05 (~23 min):** é a aula mais densa do módulo, mas os critérios I, S e A são uma comparação e rendem mais lado a lado. A auditoria acrescentou ressalvas (Whalen, Chappell 1999) e esta revisão acrescentou a linha do MALI, somando cerca de 180 palavras. **Nenhuma passagem futura deve acrescentar texto a esta aula sem cortar o equivalente.**
- **Aula 06 (~23 min):** a auditoria acrescentou as duas posições sobre fusão com água e as fontes da geometria tabular (~140 palavras). A metalogênese é um quinto bloco curto, de leitura, que prepara o Módulo 34. Continua dentro do limite.

---

## Achados

### 🟠 1. Rótulos I, S, A e o ASI usados três aulas antes de definidos

**ID:** `DID-M29-ROTULOS-ANTES-DE-DEFINIDOS-001`

**Tipo:** termo técnico usado antes de definido (ordem interna do módulo)
**Onde:** Aula 02 (regimes e exemplo: "tipo A", "tipo S", "metaluminosos", "peraluminosos", "ASI ≈ 0,95 / 1,25 / 1,0"); Aula 03 ("ASI abaixo de aproximadamente 1,0 a 1,1"); Aula 04 (exemplo, "ASI ≈ 1,2")
**Problema:** a definição dos tipos I, S e A e do ASI só chega na Aula 05, mas o exemplo trabalhado da Aula 02 **pede ao aluno** que classifique corpos pelo ASI. Quem não traz a classificação da graduação resolve o exemplo por palpite. As remissões "o tipo A da Aula 05" avisam onde está a definição, mas não a dão.
**Correção aplicada:** um parágrafo de ponte no início de "Os regimes e os granitos esperados" (Aula 02) define em uma linha cada rótulo (I: fonte ígnea ou metaígnea; S: metassedimentar; A: alcalino, pobre em água, típico de extensão) e o ASI (razão molar Al₂O₃/(CaO + Na₂O + K₂O); < 1 metaluminoso, > 1 peraluminoso), remetendo o cálculo completo à Aula 05. Na Aula 05, a primeira menção ao ASI passou a remeter à Aula 02, e o hub registra a ordem. **Nenhum fato novo:** todas as definições já estavam auditadas na Aula 05.
**Escopo:** correção local. A alternativa, mover a Aula 05 para a posição 02, exigiria renumerar quatro arquivos e romperia o arco "regimes → exemplos → classificação que resume as fontes", que a própria Aula 04 anuncia.

### 🟠 2. Objetivo "usar o esquema de Frost" sem prática correspondente

**ID:** `DID-M29-A05-OBJETIVO-FROST-NAO-PRATICADO-002`

**Tipo:** objetivo não coberto por exemplo
**Onde:** Aula 05 · cabeçalho ("usar o esquema ferroso-magnesiano/álcali-cálcico/ASI de Frost et al. (2001)") e Exemplo 1 (amostra Z)
**Problema:** o exemplo praticava só o número de Fe. O MALI, que é o eixo "álcali-cálcico" prometido, nunca era calculado. Além disso, a aula não dá as fronteiras do diagrama de Frost contra a sílica, sem as quais não se classifica pelo MALI, e prometia um uso que o aluno não consegue fazer.
**Correção aplicada:** objetivo reformulado para "calcular os três índices do esquema de Frost et al. (2001) (número de Fe, MALI e ASI) e dizer o que cada um separa". No exemplo Z entrou o MALI = 4,1 + 4,6 − 0,5 = 8,2, com a observação de que a classe (alcalino, álcali-cálcico, cálcio-alcalino ou cálcico) sai do diagrama de Frost contra o SiO₂, e com a lembrança de que o terceiro eixo, o ASI, já foi calculado (0,99). A mudança é só aritmética sobre números do enunciado. As fronteiras do diagrama **não** foram acrescentadas porque não foram verificadas (ver 🔵 12).
**Escopo:** correção local.

### 🟡 3. Ringwoodita aparece sem ter sido apresentada

**ID:** `DID-M29-A01-POLIMORFOS-OLIVINA-003`

**Tipo:** termo técnico usado antes de definido
**Onde:** Aula 01 · tabela das descontinuidades (410 km: "olivina para wadsleyita"; 660 km: "ringwoodita para bridgmanita + ferropericlásio")
**Problema:** a linha de 410 km termina em wadsleyita e a de 660 km começa em ringwoodita. Sem saber que as duas são polimorfos da olivina, o aluno não liga uma linha à outra.
**Correção aplicada:** uma frase na legenda: "Wadsleyita e ringwoodita são polimorfos de alta pressão da olivina, com a mesma composição e estrutura mais compacta; a ringwoodita da linha de 660 km é o polimorfo que sucede a wadsleyita com a profundidade." É uma frase definicional e não entra profundidade nova.
**Escopo:** correção local.

### 🟡 4. "Assinatura adakítica" sem definição

**ID:** `DID-M29-A06-ADAKITICA-004`

**Tipo:** termo técnico usado antes de definido
**Onde:** Aula 06 · "Geração", item do anfibólio
**Correção aplicada:** aposto "(líquidos com Sr/Y e La/Yb altos, marca de equilíbrio com granada residual)", que retoma a lógica da granada da Aula 03.
**Escopo:** correção local.

### 🟡 5. "Largura à meia altura" definida como meia-largura

**ID:** `DID-M29-A06-MEIA-LARGURA-005`

**Tipo:** risco de aplicação errada no exemplo trabalhado
**Onde:** Aula 06 · Exemplo trabalhado, situação e passo 2
**Problema:** "largura à meia altura" costuma designar a largura **total** entre os dois pontos de meia amplitude. A aula a definia como distância do centro, que é a correta para x½ = 0,766 z. Um aluno que mede a largura total num perfil real erra z por um fator 2.
**Correção aplicada:** o termo virou "meia-largura x½", com o aviso explícito de que não é a largura total. Os números não mudaram.
**Escopo:** correção local.

### 🟡 6. Título da Aula 06 no hub prometia "modelagem tectônica"

**ID:** `DID-M29-A06-TITULO-MODELAGEM-TECTONICA-006`

**Tipo:** título que não corresponde
**Onde:** hub (lista de aulas) e `course-state.yaml` (título do item m29-a06)
**Problema:** o H1 da aula não fala de modelagem tectônica e nenhuma seção a ensina. O OA-04 também não a pede. O título herdado do planejamento prometia um conteúdo inexistente.
**Correção aplicada:** o título no hub e no estado foi alinhado ao H1 ("...gravimetria de plutons e metalogênese associada"). **Registro de lacuna:** se a ementa de origem exigir modelagem tectônica, o lugar natural é o Módulo 23 (modelagem numérica em geodinâmica). Aqui ela não foi fabricada. O `00-progresso-do-aluno.md` ainda mostra o título antigo, porque é um débito do fechamento do módulo (ver abaixo).
**Escopo:** correção local (metadado).

### 🟡 7. Concordância: "as durbachitos", "à fracionamento"

**ID:** `DID-M29-CONCORDANCIA-007`

**Tipo:** atrito de leitura
**Onde:** Aula 04 · variscos; Aula 06 · metalogênese (Blevin & Chappell)
**Correção aplicada:** "os durbachitos"; "ao fracionamento".
**Escopo:** correção local.

### 🟡 8. Autorreferência "(Aula 05, seção final)" dentro da própria Aula 05

**ID:** `DID-M29-A05-AUTORREFERENCIA-008`

**Tipo:** atrito de leitura
**Correção aplicada:** "(seção final desta aula)".
**Escopo:** correção local.

### 🟡 9. Hub listava só o Módulo 26, mas as aulas se apoiam em 18, 27 e 28

**ID:** `DID-M29-HUB-CONEXOES-009`

**Tipo:** pré-requisito não declarado
**Onde:** hub; Aula 03 (flat slabs, alinhados ao Módulo 18 pela auditoria), Aula 04 (pré-requisito "Módulo 27, idades U-Pb"), Aula 05 (remissão ao Módulo 28)
**Correção aplicada:** linha "Conexões usadas nas aulas" no hub, com os Módulos 18, 27 e 28, e uma frase sobre os rótulos I, S, A e o ASI adiantados na Aula 02. O pré-requisito formal continua sendo o Módulo 26, como no estado.
**Escopo:** correção local.

### 🟡 10. Durações declaradas desatualizadas

**ID:** `DID-M29-DURACOES-DECLARADAS-010`

**Tipo:** metadado divergente do texto
**Problema:** a redação declarava a01 23, a02 18, a03 17, a04 16, a05 21 e a06 21 min (1942/1500/1457/1317/1778/1760 palavras). Depois da auditoria e desta revisão, o texto tem 1998/1610/1515/1452/1960/1904 palavras.
**Correção aplicada:** cabeçalhos "Duração estimada" e metadados `palavras_corpo`/`duracao_estimada_min` recontados por script: **24, 19, 18, 17, 23 e 23 min**, total de ~124 min.
**Escopo:** correção local.

### 🔵 11. Escala de referência para Sm/Yb (não aplicada)

**ID:** `DID-M29-A03-ESCALA-SMYB-011`

A Aula 03 chama o Sm/Yb de "baixo" (2,5) e "alto" (6,0) sem dar uma escala. Kay & Mpodozis (2002) usam faixas de Sm/Yb associadas a resíduos de piroxênio, anfibólio e granada, que dariam ao aluno uma régua. **Não aplicado** porque os limites exatos não foram verificados nesta passagem. Fica para uma próxima auditoria.

### 🔵 12. Fronteiras do diagrama de Frost (não aplicada)

**ID:** `DID-M29-A05-FRONTEIRAS-FROST-012`

Para que o objetivo de Frost vá além do cálculo dos índices, a aula precisaria dar as equações das fronteiras ferroso/magnesiano e das classes do MALI em função do SiO₂. **Não aplicado**, porque o texto integral de Frost et al. (2001) tem acesso restrito e as equações não foram conferidas.

### 🔵 13. Visuais

**ID:** `DID-M29-VISUAIS-013`

Três figuras ajudariam: o envelope de resistência (frágil sobre dúctil, com o "sanduíche" e a "crème brûlée"), na Aula 01; um mapa esquemático de Laurentia, Báltica, Avalônia e Gondwana com Iapetus e Rheic, na Aula 04; e o diagrama 10.000 Ga/Al × Zr+Nb+Ce+Y com as linhas 2,6 e 350 e as amostras X, Y e Z, na Aula 05.

---

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo | Avaliado em |
|---|---|---|---|
| OA-01 (estrutura interna, tomografia, reologia) | Aula 01 inteira; Aula 02 (regimes) | sim (refração; frágil-dúctil) | — (sem questionário ainda) |
| OA-02 (cordilheiranos, caledonianos, hercinianos) | Aulas 02, 03, 04 | sim (três corpos; Sr inicial; intervalos) | — |
| OA-03 (I, S, A e esquemas correlatos) | Aula 05 (+ ponte na Aula 02) | sim (X, Y, Z com ASI, Whalen, Fe#, MALI; Sr de granito S) | — |
| OA-04 (geração, ascensão, colocação, gravimetria) | Aula 06 | sim (gravimetria em dois modelos) | — |

Os quatro objetivos são cobertos por texto e por exemplo. O objetivo específico da Aula 05 sobre Frost foi reformulado (🟠 2). A metalogênese da Aula 06 não pertence a nenhum OA do módulo: é conteúdo de ligação com o Módulo 34 e deve ser cobrada no máximo em uma questão.

**Alinhamento com avaliação:** não há questionário nem baralho. O plano de avaliação está em `course-state.yaml` → `assessment.plan`.

---

## O que está bem feito

Fica registrado para que as próximas revisões **não estraguem**:

1. **O ponto de dificuldade atravessa o módulo.** Geração × colocação aparece declarado no hub, é ensinado na Aula 02, tem armadilha no exemplo da Aula 02 (diagrama de Pearce), volta na Aula 03 (batólito como resultado) e é praticado na Aula 04 (intervalo evento-colocação).
2. **Todo exemplo termina com uma ressalva de honestidade científica** ("duas amostras não estabelecem tendência", "o intervalo é indício, não prova", "a gravimetria dá massa deficiente, não a forma").
3. **As classificações são tratadas como hipóteses** (I/S/A, Pitcher, Barbarin, Pearce) e **testadas contra isótopos, idade e estrutura**, o que é exatamente o OA-03.
4. **O exemplo gravimétrico resolve o mesmo mínimo com dois modelos** e mostra a não unicidade em números, e não só em palavras.
5. **As controvérsias estão marcadas como tais** (jelly sandwich × crème brûlée; sin- × pós-colisional; fusão com água × desidratação), sem que a aula finja consenso.

**Não tocado:** `00-dashboard.md` (0/6 aulas) e `00-progresso-do-aluno.md` (aulas "pendentes de geração", título antigo da Aula 06) estão desatualizados desde a redação. É um débito pré-existente, que se resolve no fechamento do módulo (mesma conduta dos módulos 27 e 28), e não foi normalizado aqui.
