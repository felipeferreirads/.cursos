# Auditoria científica: Módulo 09 — Cristaloquímica II: substituição iônica, solução sólida e fórmula estrutural

**Auditado em:** 2026-10-06
**Material:** `curso-mineralogia/09-substituicao-e-formula/` — as 6 aulas (`-aula-01` a `-aula-06`) e a figura 1; cruzamento com o módulo 01 (aulas 02, 03 e 06), o módulo 03 (aula 01) e o módulo 08 (aulas 01 a 06)
**Modo:** audit-and-fix
**Profundidade:** full, com recálculo de todas as diferenças de raio, potenciais iônicos, frações de membros finais, da planilha da olivina de San Carlos (bases de 4 O e de 3 cátions), da granada construída pela equação de Droop e da magnetita (Python)
**Escopo:** as 46 alegações dos rodapés e as afirmações de risco do corpo: regras de Goldschmidt e de Ringwood e seus exemplos; mecanismos de substituição e vetores de troca (plagioclásio, Tschermak, berilo, pirrotita, edenita, celsiana, rubi); séries completas e limitadas, temperatura e exsolução, isomorfismo; receita de cálculo de fórmula e bases de normalização; distribuição por sítios; equação de Droop e suas hipóteses; classificação de Goldschmidt, coeficientes de partição, LILE e HFSE. Questionário e baralho ainda não existiam.
**Veredito:** Requer correção → **correções aplicadas; estado final: Aprovado com ressalva** (um 🔵 adiado, não bloqueante; nenhum 🔴/🟠 aberto)

## Resumo

🔴 0 erros · 🟠 1 imprecisão · 🟡 2 imprecisões menores · 🔵 1 sem fonte completa (adiado) · ⚪ 0 controversos
Verificadas e corretas: 42 alegações dos rodapés (46 no total; ver o manifesto `.json`) e todas as contas.

O núcleo quantitativo passou sem erro: diferenças de raio e z/r (raios de Shannon conferidos nas mesmas compilações do módulo 08), a planilha da olivina, a equação de Droop e a sua forma de balanço de cargas, a granada construída (o método recupera a fórmula de partida), a magnetita e todas as conferências de carga dos vetores.

**Contas conferidas (Python, 2026-10-06):**

| O quê | Resultado | Onde |
|---|---|---|
| Diferenças de raio sobre o menor (Fe/Mg 8,3; Ni/Mg 4,3; Hf/Zr 1,2; Rb/K 6,6; Sr/Ca 12,5; Cr/Al 15,0; K/Na 28,0; Ca/Mg 38,9; Ba/K 6,3; Al/Si 50,0; Na/K VI 35,3%) | conferidas | a01, a03, figura 1 |
| z/r: Mg 2,78; Fe²⁺ 2,56; Ni 2,90; Rb 0,62; Cs 0,57; Sr 1,59; Ba 1,41; Zr 4,76 | conferidos | a01, a06 |
| Vetores: cargas de FeMg₋₁, CaAlNa₋₁Si₋₁, Tschermak, BaAlK₋₁Si₋₁, LiNa□₋₁Be₋₁, Fe³⁺₂□Fe²⁺₋₃, NaAl□₋₁Si₋₁ | todas zero | a02 |
| Ca-Tschermak (carga 12) e Fe₇S₈ (carga 16) | conferidos | a02 |
| Fo₈₂, An₄₅ (Al 1,45; Si 2,55) | conferidos | a03 |
| San Carlos, 4 O: fator 1,4682; Si 0,997, Fe 0,195, Mn 0,003, Mg 1,800, Ni 0,007; Σ 3,003; carga 8,00; Fo 90,2; base de 3 cátions: O 3,996 | conferidos | a04 |
| Granada construída: wt% a partir da fórmula; Σ O 2,52977; fator 4,7435; S 8,050; F 0,149; Fe²⁺ 1,801; carga 24,00; X 60/25/15%; total 99,73 (FeOt) e 100,00 (FeO + Fe₂O₃) | recupera a fórmula | a05 |
| Magnetita: 93,09 wt% FeOt; S 4; F 2 | Fe²⁺Fe³⁺₂O₄ | a05 |
| San Carlos por Droop: F = 8(1 − 3/3,003) | 0,007 (ruído) | a05 |
| D do Ni: 2800/280; D total 0,3 × 10 + 0,7 × 0,05 | 10; 3,04 | a06 |

> [!note] Limite da verificação nesta sessão
> Como no módulo 08, o acesso direto às fontes estava bloqueado pelo proxy; tudo foi conferido por busca. Confirmados por busca: as regras de Goldschmidt e de Ringwood (com Ringwood, 1955, *GCA* 7, 189–202), Thompson (1982), Droop (1987), Grew et al. (2013), Mitscherlich (1819), o mecanismo do berilo, os feldspatos (alcalinos e plagioclásio), uraninita–torianita, a classificação de Goldschmidt (1923), LILE/HFSE com z/r > 2 (White) e a faixa do D do Ni na olivina (Hart & Davis, 1978, e estudos experimentais). **Não conferido na fonte primária:** quatro dos cinco óxidos da olivina de San Carlos (achado 🔵 4).

## Achados

### 🟠 1. "Cu, Zn e Pb entram pouco nos silicatos"

**claim_id:** `CRQ-GOLD-RINGWOOD-001`  ·  **Tipo:** confusão de escopo  ·  **Onde:** aula 01 · O refinamento de Ringwood
**Está escrito:** "O critério pesa mais para elementos de eletronegatividade alta, como Cu, Zn e Pb, que formam ligações mais covalentes: eles entram pouco nos silicatos e se concentram nos sulfetos (aula 06)."
**Problema:** o critério de Ringwood fala de **preferência** entre dois íons que disputam um sítio, não de exclusão. E o exemplo do Pb é mal escolhido: o Pb²⁺ é traço importante do sítio do K nos feldspatos potássicos.
**Correção aplicada:** "O critério ajuda a entender por que elementos de eletronegatividade mais alta, como Cu e Zn, que formam ligações mais covalentes, tendem a se concentrar em sulfetos quando há enxofre disponível (aula 06). É uma tendência, não uma exclusão: o Pb, por exemplo, também entra no sítio do K dos feldspatos potássicos."
**Fonte:** Ringwood (1955), *GCA* 7, 189–202; White, *Geochemistry*, cap. 7  ·  **Confiança:** confirmado

### 🟡 2. Calcita–magnesita sem a ressalva de temperatura

**claim_id:** `CRQ-GOLD-OBS-001` (propagado a `CRQ-SS-SERIES-001`)  ·  **Onde:** aula 01, tabela da primeira regra; aula 03, "Completa ou limitada"
**Problema:** "quase não se misturam" / "cada uma aceita pouco do outro cátion" vale em equilíbrio e a baixa temperatura; a quente a calcita aceita bem mais Mg (e há calcitas magnesianas metaestáveis, biogênicas).
**Correção aplicada:** "em equilíbrio e a baixa temperatura, calcita e magnesita quase não se misturam" (aula 01); "Em equilíbrio e a baixa temperatura, cada uma aceita pouco do outro cátion (a quente, a calcita aceita mais Mg)" (aula 03).  ·  **Confiança:** provável (Klein & Dutrow, sistema CaCO₃–MgCO₃)

### 🟡 3. Vetor do berilo sem a vacância do canal

**claim_id:** `CRQ-SUB-BERILO-001`  ·  **Onde:** aula 02 · tabela de vetores
**Problema:** a tabela escreve a vacância na edenita (NaAl□₋₁Si₋₁), mas não no berilo, onde o Na também ocupa um vazio do canal: inconsistência de notação.
**Correção aplicada:** **LiNa□₋₁Be₋₁** (o Na ocupa um vazio do canal), também no recap.  ·  **Confiança:** confirmado

### 🔵 4. Análise da olivina de San Carlos conferida só em parte

**claim_id:** `CRQ-FORM-SANCARLOS-001`  ·  **Onde:** aula 04 · Exemplo trabalhado
**Está escrito:** "SiO₂ 40,81; FeO 9,55; MnO 0,14; MgO 49,42; NiO 0,37 (total 100,29 wt%)"
**Problema:** a busca confirmou SiO₂ = 40,81 wt% e Fo₉₀,₁ para o padrão USNM 111312/444 (Jarosewich et al., 1980), mas a tabela original não pôde ser aberta para conferir FeO, MnO, MgO e NiO. A coerência interna é boa (Fo calculado 90,2; soma de cátions 3,003), o que torna improvável um erro grande.
**Desfecho:** **aguarda decisão / adiado, não bloqueante.** A aula já declara, nas Fontes, quais valores foram confirmados e quais são "os usualmente citados". O exemplo serve ao método em qualquer caso. Sugestão: conferir na tabela de Jarosewich et al. (1980) quando houver acesso e, se diferir, atualizar a aula 04, a aula 05 (S = 3,003) e o questionário.

## Verificado e correto (seleção)

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `CRQ-GOLD-TAMANHO-001` / `-CARGA-001` / `-PREF-001` | as três regras de Goldschmidt | White cap. 7; notas de curso | confirmado |
| `CRQ-GOLD-ZRMG-001` | Zr⁴⁺ e Mg²⁺, 0,72 Å, não se substituem | busca | confirmado |
| `CRQ-SUB-VETOR-001` | vetores de troca (Thompson, 1982) | *Rev. Mineral.* 10, 1–31 | confirmado |
| `CRQ-SS-MITSCH-001` | Mitscherlich, 1819, fosfatos e arseniatos | busca | confirmado |
| `CRQ-SS-TEMP-001` / `-PLAGLOW-001` | feldspatos alcalinos e plagioclásio | busca | confirmado |
| `CRQ-FE3-DROOP-001` | F = 2X(1 − T/S) e hipóteses | Droop (1987) | confirmado |
| `CRQ-FE3-GRANADA-001` | a granada construída é recuperada | cálculo | confirmado |
| `CRQ-GEO-GOLD-001` | classificação de 1923 pelas fases dos meteoritos | busca | confirmado |
| `CRQ-GEO-LILEHFSE-001` | LILE e HFSE, z/r > 2 | White cap. 7 | confirmado |
| `CRQ-GEO-NI-001` | D do Ni na olivina ~4 a > 30 | Hart & Davis (1978); busca | confirmado |

## Consistência interna e com o resto do curso

- **Módulo 08:** todos os raios e o Zr⁴⁺ = Mg²⁺ em VI vêm da mesma tabela da aula 01 de lá; a pergunta "Fe²⁺ × Fe³⁺ no lugar do Mg²⁺" (m08 a01) e "isoestrutural não implica miscível" (m08 a06) são respondidas nas aulas 01 e 03 daqui, sem contradição.
- **Módulo 01, aula 06:** massas molares dos óxidos idênticas (SiO₂ 60,083; FeO 71,844; MgO 40,304); o cálculo de % em óxidos é feito aqui no sentido inverso.
- **Módulo 01, aula 03:** "microssonda mede só ferro total; Fe²⁺/Fe³⁺ por método direto ou balanço de cargas (módulo 09)" — cumprido na aula 05, com Droop (1987), a mesma referência citada lá.
- **Módulo 01, aula 02:** eletronegatividades de Pauling (Mg 1,31; Fe²⁺ 1,83) usadas no critério de Ringwood.
- **Internamente:** a granada construída da aula 05 usa a mesma planilha da aula 04; as bases de normalização das duas aulas coincidem.

## Correções aplicadas

**Aplicadas em:** 2026-10-06

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `CRQ-GOLD-RINGWOOD-001` | 🟠 | Corrigido | aula-01 |
| `CRQ-GOLD-OBS-001` | 🟡 | Corrigido (propagado) | aula-01, aula-03 |
| `CRQ-SUB-BERILO-001` | 🟡 | Corrigido | aula-02 |
| `CRQ-FORM-SANCARLOS-001` | 🔵 | Aguarda decisão (adiado, não bloqueante) | — |

Também foram atualizados: os rodapés `alegacoes_auditaveis` das aulas (campo `audit:`), o hub do módulo e o `course-state.yaml` (bloco `audit` do 09, com o 🔵 em `deferred_findings`).

**Pendências:** o 🔵 4, não bloqueante.

## Segunda passagem (depois da revisão didática)

**Em:** 2026-10-06. A revisão didática acrescentou três trechos com conteúdo factual, conferidos aqui:

- **aula 05, vocabulário:** "T é o tetraedro; M1, um octaedro menor; M2, um sítio maior e mais irregular, onde cabem Ca e Na" (`CRQ-FE3-PXSITIOS-001`) — coerente com a nomenclatura de piroxênios (Morimoto, 1988) e com Klein & Dutrow. Verificado.
- **aula 06, vocabulário:** "terras raras: os 15 lantanídeos (La a Lu), mais Y e Sc" (`CRQ-GEO-ETR-001`) — definição IUPAC (Red Book, 2005), a mesma já auditada no módulo 01, aula 01. Verificado.
- **aula 02:** aposto que situa o piroxênio como silicato de cadeias (diopsídio, módulo 06) — sem fato novo além do já ensinado.

**Pendências:** o 🔵 4 (adiado, não bloqueante).

## Terceira passagem: checagem científica do questionário e do baralho

**Em:** 2026-10-06, antes de marcar o módulo como concluído.

**Questionários (parciais 1 e 2 + final, 28 questões).** Cada gabarito foi refeito contra as aulas corrigidas e todas as contas foram recalculadas em Python: Ba/K 6,3%; z/r Mg 2,78 e Fe²⁺ 2,56; K₀,₈Ba₀,₂Al₁,₂Si₂,₈O₈ (carga 16); Al₂O₃ 10,20 wt% → 0,200 mol Al; olivina construída Fo₇₀ (ΣO 2,50597; fator 1,5962; Σ 3,000); espinélio construído (ΣO 2,10993; S 3,2433; F 0,600; carga 8,00); clinopiroxênio (Σ 4,00; carga 12,00; Tschermak 0,10); D totais 6,8 e 0,0046; F 0,0075 e 0,0319; K/Na 28,0% e Na/Ca 5,4%; plagioclásio An₃₀. Nenhum distrator é defensável como correto. Dados fora das aulas, todos declarados nos enunciados e no registro de geração: análises **construídas** (olivina Fo₇₀, espinélio, piroxênio) e D hipotéticos da Q26. O 🔵 adiado (óxidos da olivina de San Carlos) só aparece na Q27 pelo valor S = 3,003, que se mantém mesmo se os óxidos não conferidos tiverem pequenas diferenças (a leitura pedida — "ruído" — não depende do terceiro decimal). Resultado: 0 🔴, 0 🟠.

**Baralho (69 Basic + 10 Cloze).** Cada card foi rastreado até a frase da aula de origem; as três correções da auditoria aparecem só na versão corrigida; o único card sobre o padrão de San Carlos usa o Fo₉₀, confirmado. Resultado: 0 🔴, 0 🟠.

**Pendências:** o 🔵 4 (adiado, não bloqueante).
