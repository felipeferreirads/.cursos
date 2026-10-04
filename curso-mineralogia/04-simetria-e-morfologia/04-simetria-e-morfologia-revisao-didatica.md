# Revisão didática: Módulo 04 — Simetria e morfologia cristalina

**Revisado em:** 2026-10-04  ·  **Modo:** review-and-fix
**Material:** `curso-mineralogia/04-simetria-e-morfologia/` — aulas 01 a 07, depois da auditoria científica
**Veredito:** Bem ensinado com ressalvas → **ressalvas 🟠 e 🟡 corrigidas**

## Resumo

🔴 0 bloqueiam · 🟠 1 prejudica · 🟡 5 atrito · 🔵 3 sugestões

**Carga estimada por aula** (contagem de `gerador-de-aula`; palavras de corpo entre parênteses, depois das correções):

| Aula | Conceitos novos | Pré-requisitos reativados | Exemplos | Visuais | Duração |
|---|---|---|---|---|---|
| 01 | 4 (cristal × agregado × amorfo; Steno; ângulo entre normais; Haüy) + nota sobre quasicristais | 2 | 1 (3 amostras) | 1 tabela + 1 figura | ~27 min (1.443) |
| 02 | 4 (operação × elemento; rotação e restrição; espelho e quiralidade; centro) | 1 | 1 (tijolo e caixa) | 1 tabela + 1 figura | ~29 min (1.404) |
| 03 | 4 (rotoinversão; equivalências; próprio × impróprio; regras de combinação), conteúdo contraintuitivo | 2 | 1 | 1 tabela + 1 figura | ~30-32 min (1.458) |
| 04 | 3 (32 grupos em famílias; posições de Hermann-Mauguin; completo × curto) + centrossimétricos | 2 | 1 (3 casos) | 2 tabelas + 1 figura | ~30 min (1.429) |
| 05 | 3 (procedimento; armadilhas; testes físicos) + tabela de consulta | 2 | 1 | 1 tabela grande + 1 figura | ~30 min (1.599) |
| 06 | 3 (simetria característica; pseudossimetria; famílias e sistemas reticulares) + holoedria | 2 | 1 (4 casos) | 1 tabela | ~27 min (1.356) |
| 07 | 4 (forma; geral × especial; aberta × fechada; hábito) | 2 | 1 | 3 tabelas | ~30 min (1.415) |

Todas no teto de ~1.600 palavras do contrato LC-02. A divisão em 7 aulas, com os 32 grupos em duas partes, funcionou: cada aula tem um objetivo central, e a Parte 1 (dedução e notação) fecha sem depender da Parte 2.

## Achados

### 🟠 1. Figuras obrigatórias do módulo ausentes nas aulas de grupos pontuais

**Tipo:** visual ausente onde o `_contexto.md` o exige
**Onde:** aulas 04 e 05
**Problema:** o `_contexto.md` marca "operações de simetria e grupos pontuais (04)" como tema em que a ilustração é essencial e deve ser pedida explicitamente. As aulas 01, 02 e 03 pediam figuras; as aulas 04 e 05, justamente as dos grupos pontuais, não.
**Correção aplicada:** aula 04: figura de quatro sólidos (4mm, 4/mmm, 4̄2m, mmm) com elementos e símbolo, legenda "O que observar"; aula 05: figura dos cubos liso (halita) e estriado (pirita) com os eixos 4 e 2 pela face da frente.
**Escopo:** correção local.

### 🟡 2. Aula 03 no limite de carga

**Onde:** aula 03 (rotoinversão + regras de combinação)
**Problema:** a rotoinversão é o ponto de travamento clássico do módulo (hub, "Pontos de dificuldade") e conta em dobro na estimativa; a aula fica em ~30-32 min.
**Correção aplicada:** callout "Ponto de pausa" antes das regras de combinação, que só dependem do que já foi visto; duração declarada ajustada para "~30-32 min (com ponto de pausa)". Não se dividiu a aula: as regras são curtas e a aula 04 depende delas.

### 🟡 3. Tabela de 32 representantes sem instrução de uso

**Onde:** aula 05 · Um representante por classe
**Problema:** sem instrução, o aluno tende a tentar decorar 32 linhas.
**Correção aplicada:** "A tabela abaixo é de consulta, não de memorização [...] Vale guardar só os casos que esta aula discutiu (pirita, turmalina, apatita, quartzo, calcita) e alguns comuns de cada sistema." O baralho segue a mesma regra.

### 🟡 4. "Clivagem" sem glossa

**Onde:** aula 01 · Exemplo trabalhado
**Correção aplicada:** "(planos de quebra fácil, que seguem planos de átomos do cristal)". Conferida pelo auditor (`CRI-REV-GLOSSAS-001`).

### 🟡 5. "Retículo" e "macla" usados antes dos módulos 06 e 12

**Onde:** aula 06 · vocabulário (holoedria) e leucita
**Correção aplicada:** "retículo, a grade de pontos que se repete por translação, módulo 06"; "lamelas de macla (faixas do cristal com orientações diferentes, unidas de modo regular; módulo 12)". Conferidas pelo auditor (`CRI-REV-GLOSSAS-002`).

### 🟡 6. Aula 05 acima do teto de palavras depois das inserções

**Correção aplicada:** enxugadas a armadilha 1, a seção "Quando a morfologia não basta" e um erro comum redundante; a aula voltou a 1.599 palavras.

### 🔵 7. Modelos físicos

**Sugestão:** a simetria se aprende com as mãos. Uma nota no hub sugerindo montar, em papel, cubo, octaedro, disfenoide e romboedro (moldes de planificação) ajudaria as aulas 02-03.
**Desfecho:** aberto, não bloqueante.

### 🔵 8. Ordem das posições antes dos sistemas

**Onde:** aula 04
**Observação:** a tabela de posições de Hermann-Mauguin aparece antes da aula 06 (sistemas). A aula contorna isso descrevendo cada linha pela simetria ("eixo 4 único", "quatro eixos 3") e só pondo o nome do sistema entre parênteses. Funciona; uma alternativa seria inverter as aulas 04-05 e 06, mas a definição dos sistemas pela simetria característica depende de conhecer as classes.
**Desfecho:** mantido como está.

### 🔵 9. Projeção estereográfica

**Observação:** a forma usual de mostrar um grupo pontual é o estereograma, que só chega no módulo 05. Quando o módulo 05 for escrito, vale uma remissão de volta à tabela de famílias da aula 04 com os estereogramas das 32 classes.
**Desfecho:** registro para o módulo 05.

## Pontos fortes (manter)

- O módulo diferencia sistematicamente **forma aparente × simetria**: cristal distorcido (aula 01), pirita estriada e apatita (aula 05), quartzo, leucita e anidrita (aula 06), forma × hábito (aula 07). Isso ataca de frente o ponto de dificuldade previsto no hub (cubo de pirita × piritoedro; forma × hábito).
- A contagem de 32 é **deduzida**, não apresentada como dogma, e a mesma soma reaparece por sistema (2 + 3 + 3 + 7 + 5 + 7 + 5).
- A convenção dos **sete sistemas** fica compatível com o curso-geologia (citado por nome) e com os livros que usam seis, sem chamar nenhum de errado.
- Cada exemplo trabalhado termina em "método geral", reaproveitável no questionário.

## Correções aplicadas

| # | Severidade | Desfecho | Arquivos |
|---|---|---|---|
| 1 | 🟠 | Corrigido | aula-04, aula-05 |
| 2-6 | 🟡 | Corrigidos | aula-01, aula-03, aula-05, aula-06 |
| 7-9 | 🔵 | 7 aberto, 8 mantido, 9 registrado para o módulo 05 | — |

As glossas novas foram conferidas pelo `auditor-cientifico` antes de fechar a revisão (seção "Segunda passagem" da auditoria do módulo).
