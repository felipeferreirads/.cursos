# Revisão didática: Módulo 06 — Retículo cristalino, cela unitária e redes de Bravais

**Revisado em:** 2026-10-04  ·  **Modo:** review-and-fix
**Material:** `curso-mineralogia/06-reticulo-e-cela/` — aulas 01 a 04 e figuras 1 a 5, depois da auditoria científica
**Veredito:** Bem ensinado com ressalvas → **ressalvas 🟠 e 🟡 corrigidas**

## Resumo

🔴 0 bloqueiam · 🟠 2 prejudicam · 🟡 2 atrito · 🔵 3 sugestões

**Carga estimada por aula** (contagem de `gerador-de-aula`; palavras de corpo depois das correções):

| Aula | Conceitos novos | Pré-requisitos reativados | Exemplos | Visuais | Duração |
|---|---|---|---|---|---|
| 01 | 3 (motivo × retículo × estrutura; teste da vizinhança; translação como operação) | 3 | 1 (+ grafita) | 1 figura | ~27 min (1.160) |
| 02 | 3 (cela e escolha; contagem por pesos; primitiva × convencional e centragens) + coordenadas fracionárias | 2 | 1 | 2 figuras + 2 tabelas | ~28 min (1.241) |
| 03 | 3 (símbolo e lista; duas razões das ausências, contraintuitivas; hP × hR) | 2 | 1 (5 casos) | 2 figuras + 1 tabela | ~30 min (1.189) |
| 04 | 3 (Z; volume por sistema; densidade e Z inverso) + cela romboédrica × hexagonal (seção adiável) | 3 | 1 (+ 3 contas curtas) | 1 figura + 1 tabela | ~30 min com as contas (1.217) |

Todas bem abaixo do teto de ~1.600 palavras; a carga está nas contas e nas ideias contraintuitivas, não no texto.

## Achados

### 🟠 1. Exemplo de contagem da halita sem figura

**Tipo:** visual ausente onde o `_contexto.md` o exige ("retículos de Bravais (06)")
**Onde:** aula 02 · Exemplo trabalhado
**Problema:** o exemplo pede para contar 4 Na e 4 Cl com pesos 1/8, 1/4, 1/2 e 1 só a partir de coordenadas. É o primeiro contato do aluno com uma cela 3D cheia de átomos; sem ver onde cada íon cai (vértice, face, aresta, centro), a contagem vira fórmula decorada.
**Correção aplicada:** **figura 6** nova, gerada pelas mesmas coordenadas do exemplo (Na nos vértices e centros de face, Cl nos meios das arestas e no centro), com legenda "O que observar" e o balanço 4 + 4 ao lado.
**Escopo:** correção local.

### 🟠 2. Aula 04 carregada de contas

**Tipo:** sobrecarga
**Onde:** aula 04
**Problema:** Z, seis fórmulas de volume, densidade, Z inverso, calculada × medida e, ainda, a cela romboédrica × hexagonal, com quatro contas no corpo além do exemplo: ~35 min pela contagem de carga.
**Correção aplicada:** o exemplo do quartzo virou uma linha (mesmos números); a seção romboédrica × hexagonal ganhou a indicação de que pode ser lida numa segunda sessão, porque o exemplo trabalhado não depende dela. Não se dividiu a aula: a seção é curta e é a resposta ao "por que Z = 6 e Z = 2" que o aluno encontra nas fichas.
**Escopo:** correção local.

### 🟡 3. Módulo 07 citado como se fosse caminho obrigatório

**Onde:** aula 01 · Do papel de parede ao cristal
**Correção aplicada:** "este módulo e o 07 (de aprofundamento) tratam do retículo e da simetria". A aula 04 já remete ao 08 como próximo do núcleo.

### 🟡 4. Justificativa do ortorrômbico (aula 03) apoiada numa só razão

**Onde:** aula 03 · Por que não 7 × 5
**Observação:** coincidiu com o achado 🟡 3 da auditoria, que corrigiu o texto; do ponto de vista didático, a correção também fecha o raciocínio da seção, que apresentava duas razões e aplicava só uma.

### 🔵 5. Modelo físico da cela

**Sugestão:** montar a cela da halita com bolinhas de massa de modelar de dois tamanhos e palitos, cortando as bolinhas dos vértices em oitavos, deixa a regra dos pesos física.
**Desfecho:** aberto, não bloqueante.

### 🔵 6. Figura 3D dos 14 retículos

**Observação:** a figura 3 usa perspectiva oblíqua simples; as celas monoclínica, triclínica e romboédrica ficam legíveis, mas um modelo 3D girável (ou um applet) seria melhor para o aluno visual.
**Desfecho:** aberto, não bloqueante.

### 🔵 7. Coordenadas fracionárias como ponte para o módulo 08

**Sugestão:** o módulo 08 (coordenação) pode reutilizar a figura 6 para mostrar que cada Na tem 6 Cl vizinhos.
**Desfecho:** registrado para o módulo 08.

## Pontos fortes (manter)

- O teste da **vizinhança idêntica** é aplicado a dois contraexemplos (tabuleiro de dois átomos, colmeia de grafita), o que evita o erro mais comum do tema (átomo = ponto do retículo).
- As duas razões das combinações ausentes são mostradas, uma com figura (tC = tP).
- A distinção **trigonal × romboédrico** e **cela × romboedro de clivagem** fecha pontas deixadas pelos módulos 04 e 05.
- Todas as densidades do módulo foram recalculadas e comparadas com o valor medido do *Handbook of Mineralogy*.

## Correções aplicadas

| # | Severidade | Desfecho | Arquivos |
|---|---|---|---|
| 1 | 🟠 | Corrigido | aula-02, figura 6 (nova) |
| 2 | 🟠 | Corrigido | aula-04 |
| 3-4 | 🟡 | Corrigidos | aula-01, aula-03 |
| 5-7 | 🔵 | 5 e 6 abertos; 7 registrado para o módulo 08 | — |

As mudanças da revisão foram conferidas pelo `auditor-cientifico` (seção "Segunda passagem" da auditoria do módulo).
