# Revisão didática: Módulo 09 — Cristaloquímica II: substituição iônica, solução sólida e fórmula estrutural

**Revisado em:** 2026-10-06  ·  **Modo:** review-and-fix
**Material:** `curso-mineralogia/09-substituicao-e-formula/` — aulas 01 a 06 e figura 1, depois da auditoria científica
**Veredito:** Bem ensinado com ressalvas → **ressalvas 🟠 e 🟡 corrigidas**

## Resumo

🔴 0 bloqueiam · 🟠 1 prejudica · 🟡 2 atrito · 🔵 3 sugestões

**Carga estimada por aula** (contagem de `gerador-de-aula`; palavras de corpo depois das correções):

| Aula | Conceitos novos | Pré-requisitos reativados | Exemplos | Visuais | Duração |
|---|---|---|---|---|---|
| 01 | 3 (regras de tamanho, carga e preferência; Ringwood como refinamento) | 3 | 1 (4 casos) | 1 figura + 1 tabela | ~28 min (1.280) |
| 02 | 3 (quatro mecanismos agrupados em: simples × compensações; vacância; vetor de troca) | 3 | 1 (3 itens) | 1 tabela | ~27 min (1.079) |
| 03 | 3 (série completa × limitada; temperatura e solvus; isoestrutura × miscibilidade) | 2 | 1 (4 itens) | — | ~27 min (1.079) |
| 04 | 2 (receita da planilha; bases de normalização) | 3 | 1 (planilha completa) | 2 tabelas | ~30 min com a planilha (1.047) |
| 05 | 3 (distribuição por sítios; Fe³⁺ escondido; balanço de cargas/Droop) + limites | 2 | 1 (granada) + 2 conferências curtas | 1 tabela | ~30 min com a planilha (1.312) |
| 06 | 3 (classificação de Goldschmidt; D e D total; LILE × HFSE) | 2 | 1 (4 itens) | 1 tabela | ~28 min (1.156) |

Todas abaixo do teto de ~1.600 palavras; a carga das aulas 04 e 05 está na planilha, não no texto.

## Achados

### 🟠 1. Sítios M1 e M2 do piroxênio usados sem definição

**Tipo:** termo técnico antes de definido
**Onde:** aula 05 · tabela "Distribuir pelos sítios"
**Problema:** a tabela manda pôr Al, Fe³⁺, Cr e Ti em "M1" e Ca e Na em "M2", mas os piroxênios só são estudados no módulo 34, e nenhuma aula anterior definiu esses sítios. O aluno decora a regra sem saber o que é M1.
**Correção aplicada:** linha nova no vocabulário: "sítios T, M1, M2 — os sítios de cátion dos piroxênios (como o diopsídio): T é o tetraedro; M1, um octaedro menor; M2, um sítio maior e mais irregular, onde cabem Ca e Na (módulo 34)". O fato novo foi conferido na segunda passagem da auditoria.
**Escopo:** correção local.

### 🟡 2. "Componente de Tschermak dos piroxênios" sem situar o piroxênio

**Onde:** aula 02 · Substituição acoplada
**Correção aplicada:** aposto "(silicatos de cadeias de tetraedros, como o diopsídio do módulo 06, estudados no módulo 34)".

### 🟡 3. "Terras raras" sem definição

**Onde:** aula 06 · vocabulário e tabela de Goldschmidt
**Correção aplicada:** linha de vocabulário "terras raras (ETR): os 15 lantanídeos (do La ao Lu), aos quais se juntam Y e Sc", a mesma definição IUPAC do módulo 01, aula 01.

### 🔵 4. Planilha-modelo

**Sugestão:** um arquivo de planilha (CSV ou planilha eletrônica) com as colunas das aulas 04 e 05 já montadas, para o aluno digitar só os wt%. Reduz o erro mecânico (esquecer o 2 do Al₂O₃) e libera atenção para a interpretação.
**Desfecho:** aberto, não bloqueante (fica para a skill `gerador-de-praticas`, se o usuário pedir).

### 🔵 5. Diagrama de solvus

**Sugestão:** a aula 03 descreve o solvus dos feldspatos alcalinos só em palavras; o diagrama T × composição é do módulo 23, mas um esboço qualitativo ajudaria o aluno visual.
**Desfecho:** registrado para o módulo 23, que tem o diagrama como objetivo.

### 🔵 6. Aula 05 densa no fim

**Observação:** a aula 05 junta a distribuição por sítios, o balanço de cargas, as hipóteses e um exemplo com cinco itens. Está no limite de 30 min com a planilha; não se dividiu porque o exemplo da granada é a aplicação direta da equação e separá-lo deixaria a Parte 2 sem prática. Se o aluno sentir peso, pode deixar a seção "Quando o método vale" para uma segunda leitura.
**Desfecho:** aberto, não bloqueante.

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo | Avaliado em |
|---|---|---|---|
| `mineralogia-m09-oa01` — regras de Goldschmidt e Ringwood | a01 | sim (Ni, Ba, Ca, z/r) | (questionário a gerar) |
| `mineralogia-m09-oa02` — mecanismos e vetores de troca | a02 | sim (Tschermak, pirrotita, rubi) | (questionário a gerar) |
| `mineralogia-m09-oa03` — solução sólida, miscibilidade, isomorfismo | a03 | sim (Fo, An, halita–silvita) | (questionário a gerar) |
| `mineralogia-m09-oa04` — fórmula estrutural | a04, a05 | sim (olivina de San Carlos; granada construída; magnetita) | (questionário a gerar) |
| `mineralogia-m09-oa05` — Goldschmidt geoquímico; compatíveis × incompatíveis | a06 | sim (D, D total, z/r) | (questionário a gerar) |

Nenhum objetivo descoberto; nenhuma seção órfã.

## O que está bem feito (manter)

- As regras de Goldschmidt são ensinadas com **as exceções** (Zr⁴⁺ × Mg²⁺, Al³⁺ × Si⁴⁺) e com a dependência da convenção de cálculo, o que evita ler 15% e 30% como fronteiras naturais.
- O vetor de troca aparece como ferramenta de **conferência** (carga zero) e de **composição** (albita + vetor = anortita), não como notação decorativa.
- A planilha da aula 04 usa um **padrão real**, e a aula 05 usa uma **análise construída** declarada como tal: o aluno vê o método recuperar uma resposta conhecida antes de confiar nele.
- A aula 05 ensina a **desconfiar** do resultado (F = 0,007 na olivina é ruído), e a aula 01 do módulo 03 e a aula 03 do módulo 01 são retomadas sem repetir.
- As pontes prometidas pelos módulos 01 (neutralidade, óxidos, Fe total) e 08 (raios; isoestrutural ≠ miscível) são fechadas explicitamente.

## Correções aplicadas

| # | Severidade | Desfecho | Arquivos |
|---|---|---|---|
| 1 | 🟠 | Corrigido | aula-05 |
| 2 | 🟡 | Corrigido | aula-02 |
| 3 | 🟡 | Corrigido | aula-06 |
| 4-6 | 🔵 | 4 e 6 abertos; 5 registrado para o módulo 23 | — |

As mudanças da revisão foram conferidas pelo `auditor-cientifico` (seção "Segunda passagem" da auditoria do módulo).
