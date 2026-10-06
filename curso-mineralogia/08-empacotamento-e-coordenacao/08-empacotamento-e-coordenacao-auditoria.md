# Auditoria científica: Módulo 08 — Cristaloquímica I: raios iônicos, coordenação e regras de Pauling

**Auditado em:** 2026-10-06
**Material:** `curso-mineralogia/08-empacotamento-e-coordenacao/` — as 6 aulas (`-aula-01` a `-aula-06`) e as figuras 1 a 6; cruzamento com o módulo 01 (aulas 02 a 06) e o módulo 06 (aulas 02 a 04, figura 6)
**Modo:** audit-and-fix
**Profundidade:** full, com recálculo de todas as razões, distâncias, frações de empacotamento, somas de valência eletrostática e do fator de tolerância (Python) e conferência de cada raio de Shannon citado
**Escopo:** as 44 alegações dos rodapés `alegacoes_auditaveis` e as afirmações de risco do corpo: raios iônicos efetivos (âncora, dependência com NC, carga e spin), distâncias previstas e medidas, valores-limite da razão de raios e seus acertos e falhas, empacotamentos compactos e contagem de interstícios, descrição de minerais como pilhas de ânions, enunciado das cinco regras de Pauling, forças de ligação, isodésmico/anisodésmico/mesodésmico, geometria do compartilhamento, polimorfos de TiO₂, estruturas-tipo com grupos espaciais e minerais isoestruturais, fator de tolerância, bridgmanita. Questionário e baralho ainda não existiam.
**Veredito:** Requer correção → **correções aplicadas; estado final: Aprovado** (nenhum achado aberto)

## Resumo

🔴 0 erros · 🟠 3 imprecisões · 🟡 3 imprecisões menores · 🔵 1 sem fonte (frase removida) · ⚪ 0 controversos
Verificadas e corretas: 37 alegações dos rodapés (44 no total; ver o manifesto `.json`) e todas as contas.

O núcleo quantitativo passou sem erro: todos os raios de Shannon (conferidos um a um em duas compilações digitais independentes), os limites 0,155/0,225/0,414/0,732, as somas da segunda regra (todas exatas), as distâncias relativas do compartilhamento, as frações de empacotamento e os grupos espaciais. Os achados são de escopo e de formulação; um deles é uma analogia que ensinava o sentido errado da dependência raio × NC.

**Contas conferidas (Python, 2026-10-06; raios de Shannon 1976):**

| O quê | Resultado | Referência | Onde |
|---|---|---|---|
| Halita Na–Cl: 1,02 + 1,81; a/2 | 2,83; 2,820 Å | HoM: a = 5,6404 Å | a01 |
| Periclásio Mg–O: 0,72 + 1,40; a/2 | 2,12; 2,102–2,106 Å | HoM: a = 4,203–4,212 Å | a01 |
| Quartzo Si–O: Si IV 0,26 + O II 1,35 | 1,61 Å | m01 a06: ~1,62 Å | a01 |
| Esfalerita Zn–S: 0,60 + 1,84; a·√3/4 | 2,44; 2,341 Å (4,2%) | HoM: a = 5,4060 Å | a01 |
| Galena Pb–S: 1,19 + 1,84; a/2 | 3,03; 2,968 Å (2,1%) | HoM: a = 5,936 Å | a01 |
| Limites: 2/√3 − 1; √(3/2) − 1; √2 − 1; √3 − 1 | 0,1547; 0,2247; 0,4142; 0,7321 | Pauling (1929) | a02 |
| Razões com O 1,40 (Si, Al, Ti, Mg, Fe²⁺, Ca, Na, K em VI) | 0,286; 0,382; 0,432; 0,514; 0,557; 0,714; 0,729; 0,986 | — | a02 |
| Halita 0,564; fluorita 1,12/1,31; esfalerita 0,74/1,84; zircão 0,72/1,40 | 0,564; 0,855; 0,402; 0,514 | — | a02 |
| Frações: π/(3√2); π√3/8; π/6 | 0,7405; 0,6802; 0,5236 | — | a03 |
| Cl–Cl na halita: a/√2 | 3,988 Å (contra 3,62) | — | a03 |
| Somas da regra 2 (halita, rutilo, corindo, forsterita, quartzo, calcita, espinélio, magnetita inversa, perovskita ideal, esfalerita, periclásio) | todas 1 ou 2, exatas | frações em Python | a04, a06 |
| Compartilhamento: √2/2; 1/√3; 1/3 | 0,707; 0,577; 0,333 | — | a05 |
| Si–Si: aresta 2·1,61/√3; face 2·1,61/3; vértice com 144° | 1,859; 1,073; 3,062 Å | Si–O–Si do α-quartzo 143,6° | a05 |
| Rutilo: Ti–O = 0,605 + 1,36; ×√2; Ti–Ti pela aresta = c | 1,965; 2,779; 2,9587 Å | HoM: c = 2,9587 Å | a05 |
| Fator de tolerância CaTiO₃: (1,34 + 1,40)/[√2(0,605 + 1,40)] | 0,966 | busca: t = 0,966, Pbnm | a06 |

> [!note] Limite da verificação nesta sessão
> O acesso direto aos sites de referência (base de raios do Imperial College, *Handbook of Mineralogy*, Wikipedia, IUCr, editoras) estava bloqueado pelo proxy. Os **raios de Shannon (1976)** foram conferidos em duas compilações digitais independentes da tabela original, baixadas do PyPI: o `periodic_table.json` do *pymatgen-core* e a tabela `ionicradii` do *mendeleev*; as duas concordam em todos os valores citados. Parâmetros de cela, grupos espaciais e fatos estruturais foram conferidos por busca (resultados que citam as fichas do *Handbook of Mineralogy*, o Mindat, notas de cursos de mineralogia e os artigos citados). Não conferido na fonte: a página final (1026) do artigo de Pauling (1929) — a inicial, 1010, e o volume 51 foram confirmados.

## Achados

### 🟠 1. Spin baixo: "todos" os elétrons nos orbitais entre os vizinhos

**claim_id:** `CRQ-RAIO-SPIN-001`  ·  **Tipo:** confusão de escopo  ·  **Onde:** aula 01 · O spin também muda o raio
**Está escrito:** "no **spin baixo**, todos se recolhem nos orbitais que apontam entre eles"
**Problema:** a frase vem logo depois de "íons com 4 a 7 elétrons d". Para d⁴–d⁶ é verdade (t₂g⁴ a t₂g⁶), mas um d⁷ de spin baixo (t₂g⁶ e_g¹) mantém um elétron nos orbitais que apontam para os vizinhos.
**Correção aplicada:** "no **spin baixo**, os elétrons se concentram nos orbitais que apontam entre eles (no Fe²⁺, todos os seis), e o íon fica menor."
**Fonte:** teoria do campo cristalino (configurações de spin baixo d⁴–d⁷)  ·  **Confiança:** confirmado

### 🟠 2. Analogia da espuma no sentido errado

**claim_id:** `CRQ-RAIO-ANALOGIA-001`  ·  **Tipo:** omissão que gera erro (modelo mental)  ·  **Onde:** aula 01 · Um íon não tem borda
**Está escrito:** "Elas se deixam apertar um pouco conforme o número de vizinhas que as comprimem, e o tamanho 'de contato' depende da vizinhança."
**Problema:** a imagem de bolas comprimidas por mais vizinhas sugere raio **menor** com mais vizinhos. Os dados de Shannon, que a própria aula mostra a seguir, dizem o contrário (Na⁺: 0,99 Å em IV, 1,39 Å em XII). A analogia é memorável, e o erro gruda.
**Correção aplicada:** a analogia fica, com o aviso explícito: "Atenção ao sentido da mudança, que é o contrário do que a espuma sugere: como se verá abaixo, o raio **cresce** quando há mais vizinhos, porque cada um é atraído com menos força."
**Fonte:** Shannon (1976)  ·  **Confiança:** confirmado

### 🟠 3. "Si em NC VI só em alta pressão"

**claim_id:** `CRQ-RR-TABELA-001`  ·  **Tipo:** omissão que gera erro  ·  **Onde:** aula 02 · tabela "Aplicando aos cátions das rochas"
**Está escrito:** "IV (VI só em alta pressão)"
**Problema:** a **taumasita**, Ca₃Si(OH)₆(CO₃)(SO₄)·12H₂O, tem Si octaédrico (coordenado por OH) estável em condições ambiente. É rara, mas o "só" torna a frase falsa.
**Correção aplicada:** "IV (VI em alta pressão; na superfície, só na rara taumasita)", com a fonte acrescentada.
**Fonte:** Mindat (taumasita); estudos de expansão térmica do Si hexacoordenado da taumasita, *Physics and Chemistry of Minerals* (busca em 2026-10-06)  ·  **Confiança:** confirmado

### 🟡 4. Tabelas antigas de raios: "pelo mesmo motivo: outra âncora"

**claim_id:** `CRQ-RAIO-ANCORA-001`  ·  **Onde:** aula 01 · aviso "Duas tabelas"
**Problema:** as tabelas de Goldschmidt, Pauling e Ahrens diferem também pelo método de derivação, não só pela âncora.
**Correção aplicada:** "porque usaram outra âncora e outros métodos."  ·  **Confiança:** provável (histórico resumido na introdução de Shannon, 1976)

### 🟡 5. "s = 1 é a maior força de ligação"

**claim_id:** `CRQ-PAU-SIFORCA-001`  ·  **Onde:** aula 04 · Erros comuns
**Problema:** o B³⁺ em triângulo, presente em borossilicatos (turmalina), também tem s = 3/3 = 1.
**Correção aplicada:** "s = 1 está entre as maiores forças de ligação dos cátions comuns dos silicatos".  ·  **Confiança:** confirmado (cálculo)

### 🔵 6. Detalhe atribuído a George et al. (2020) sem confirmação

**claim_id:** `CRQ-PAU-ESTAT2-001`  ·  **Onde:** aula 04 · Quão bem a regra funciona
**Está escrito:** "…às vezes bastante, sobretudo quando há cátions de raio e carga muito diferentes."
**Problema:** a busca confirmou os números globais do estudo (~5000 óxidos; 66% para a regra 1; 13% para as regras 2 a 5 juntas), não esse detalhe.
**Desfecho:** frase removida; fica só a constatação geral.

### 🟡 7. Hábito "do rutilo e da cassiterita"

**claim_id:** `CRQ-EST-RUTILO-001`  ·  **Onde:** aula 06 · Rutilo: cadeias de octaedros
**Problema:** a cassiterita é com frequência curta-prismática a dipiramidal; atribuir a ela o hábito alongado em c, como regra, não se sustenta.
**Correção aplicada:** "Essas cadeias ajudam a explicar o hábito prismático, alongado em c, comum no rutilo."  ·  **Confiança:** confirmado

## Verificado e correto (seleção)

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `CRQ-RAIO-NC-001` / `-CARGA-001` / `-FE-001` | todos os raios citados (Na, Ca, K, O, F, Cl, S, Mg, Al, Si, Fe²⁺/³⁺ alto e baixo spin, Mn²⁺/³⁺/⁴⁺) | Shannon (1976) em *pymatgen* e *mendeleev* | confirmado |
| `CRQ-RAIO-DIST-001` | distâncias previstas × medidas | HoM (busca); cálculo | confirmado |
| `CRQ-RR-ESTAT-001` | ~5000 óxidos; ~66% concordam com a regra 1 | George et al. (2020) | confirmado |
| `CRQ-RR-FALHAS-001` | C⁴⁺ III = −0,08 Å; Zr VIII no zircão; Mg IV no espinélio; Si VI na estishovita | Shannon; HoM; Klein & Dutrow | confirmado |
| `CRQ-EMP-MINERAIS-001` | frações ocupadas em halita, esfalerita, wurtzita, corindo, olivina, espinélio; fluorita | Birle et al. (1968); busca | confirmado |
| `CRQ-PAU-DESMICO-001` | iso-, aniso- e mesodésmico; C 4/3, S 3/2, Si 1 | Perkins/LibreTexts; Klein & Dutrow | confirmado |
| `CRQ-PAU-TIO2-001` | rutilo 2, brookita 3, anatásio 4 arestas | Pauling (1929), por busca | confirmado |
| `CRQ-PAU-R5-001` | granada: X, Y, Z e um único sítio de O (96h) | busca (estrutura Ia3̄d) | confirmado |
| `CRQ-EST-QUADRO-001` | grupos espaciais das oito estruturas | HoM; auditoria m04 | confirmado |
| `CRQ-EST-BRIDG-001` | bridgmanita, IMA 2014-017, Tenham | Tschauner et al. (2014) | confirmado |

## Consistência interna e com o resto do curso

- **Módulo 01, aula 03:** Fe²⁺ VI spin alto 0,78 Å e Fe³⁺ 0,645 Å (lá "~0,65"); spin baixo do Fe²⁺ da pirita — a aula 01 deste módulo reaproveita os mesmos números e a mesma definição restrita a 4–7 elétrons d (agora sem o "todos").
- **Módulo 01, aulas 04 e 05:** Si–O com ~45% de caráter iônico; ligação mais covalente nos sulfetos — usado na aula 01 para explicar o desvio maior na esfalerita e na galena; sem conflito.
- **Módulo 01, aula 06:** Si–O ≈ 1,62 Å e "diâmetro do Si⁴⁺ IV de ~0,5 Å" — coerente com 0,26 Å de raio e 1,61 Å previstos.
- **Módulo 06, aulas 02 a 04:** halita Fm3̄m, a = 5,6404 Å, cela cF com 4 pontos, fluorita a = 5,4626 Å, rutilo a e c — reaproveitados; a figura 6 do módulo 06 é usada para a coordenação 6:6 (sugestão 🔵 7 da revisão didática do 06, agora atendida).
- **Internamente:** as frações de interstícios (aula 03) e as somas da regra 2 (aulas 04 e 06) foram cruzadas e contam a mesma história para corindo, espinélio e olivina.

## Correções aplicadas

**Aplicadas em:** 2026-10-06

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `CRQ-RAIO-SPIN-001` | 🟠 | Corrigido | aula-01 |
| `CRQ-RAIO-ANALOGIA-001` | 🟠 | Corrigido | aula-01 |
| `CRQ-RR-TABELA-001` | 🟠 | Corrigido | aula-02 |
| `CRQ-RAIO-ANCORA-001` | 🟡 | Corrigido | aula-01 |
| `CRQ-PAU-SIFORCA-001` | 🟡 | Corrigido | aula-04 |
| `CRQ-PAU-ESTAT2-001` | 🔵 | Corrigido (frase removida) | aula-04 |
| `CRQ-EST-RUTILO-001` | 🟡 | Corrigido | aula-06 |

Também foram atualizados: os rodapés `alegacoes_auditaveis` das aulas (campo `audit:`), o hub do módulo e o `course-state.yaml` (bloco `audit` do 08).

**Pendências:** nenhuma. Não há questionário nem baralho a propagar (ainda não existiam).

## Segunda passagem (depois da revisão didática)

**Em:** 2026-10-06. A revisão didática condensou dois trechos da aula 01 (mesmos fatos), acrescentou uma frase de orientação de leitura na aula 06 e explicitou a simetria no exemplo geométrico da aula 05. Conferido: nenhuma das mudanças introduz fato, número ou fonte novos; as contas do exemplo da aula 05 continuam as mesmas (R·√2; 2R/√3).

**Pendências:** nenhuma.

## Terceira passagem: checagem científica do questionário e do baralho

**Em:** 2026-10-06, antes de marcar o módulo como concluído (lição dos módulos 01 e 06: questionário e baralho precisam de checagem própria).

**Questionários (parciais 1 e 2 + final, 28 questões).** Cada gabarito foi refeito contra as aulas corrigidas e todas as contas foram recalculadas em Python: MnO suposto (0,593; 2,23; 2,045 Å); forças de ligação (3/4, 3/2, 1/2); corindo (4 Al por O; Σ = 2; 2/3); fluorita (0,855; 2,43 contra 2,365 Å, 2,7%; Σ = 1); espinélio e magnetita (1/8, 1/2; Σ = 2 nas duas distribuições); fator de tolerância (CaTiO₃ 0,966; SrTiO₃ 1,002); olivina (16/4 = 4; Σ = 2; 0,557); rutilo (0,432; 1,965; 2,779 contra c = 2,9587 Å); estishovita 0,286; O hipotético 7/3. Nenhum distrator é defensável como correto. Único dado fora das aulas: o raio do Sr²⁺ XII (1,44 Å), conferido em Shannon (1976) nas mesmas compilações, usado só como cálculo comparativo; o gabarito não afirma a simetria real do SrTiO₃. Resultado: 0 🔴, 0 🟠.

**Baralho (75 Basic + 10 Cloze).** Cada card foi rastreado até a frase da aula de origem; os quatro pontos corrigidos na auditoria (spin baixo, analogia, taumasita, hábito) aparecem nos cards só na versão corrigida. Resultado: 0 🔴, 0 🟠; ajustes de redação e de duplicação registrados no histórico do `flashcards.md`.

**Pendências:** nenhuma.
