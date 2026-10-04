# Revisão didática: Módulo 05 — Eixos cristalográficos, índices de Miller e projeção estereográfica

**Revisado em:** 2026-10-04  ·  **Modo:** review-and-fix
**Material:** `curso-mineralogia/05-miller-e-projecao/` — aulas 01 a 06 e figuras 1 a 8, depois da auditoria científica
**Veredito:** Requer revisão → **aula 05 dividida (nova aula 07), ressalvas 🟠 e 🟡 corrigidas**

## Resumo

🔴 0 bloqueiam · 🟠 2 prejudicam · 🟡 4 atrito · 🔵 3 sugestões

**Carga estimada por aula** (contagem de `gerador-de-aula`; palavras de corpo depois das correções):

| Aula | Conceitos novos | Pré-requisitos reativados | Exemplos | Visuais | Duração |
|---|---|---|---|---|---|
| 01 | 3 (eixos pela simetria; nomes dos ângulos; parâmetros e razão axial) + tabela por sistema | 2 | 1 (4 casos) | 1 figura + 2 tabelas | ~28-30 min (1.595) |
| 02 | 3 (interceptos/Weiss; receita de Miller; forma {hkl}) | 2 (+ inverso e mmc) | 1 (5 itens) | 1 figura + 1 tabela | ~28 min (1.275) |
| 03 | 3 (direções [uvw]; quatro índices hkil; conversões) + nota de consulta | 2 | 1 | 1 figura + 2 tabelas | ~30 min (1.274) |
| 04 | 3 (zona; lei de Weiss; regra da cruz) + regra da adição | 1 | 1 (5 passos) | 1 figura | ~28 min (1.253) |
| 05 | 4 (construção; r = R·tan(ρ/2) e hemisférios; φ e ρ; grandes círculos), contraintuitiva | 2 | 1 | 2 figuras + 1 tabela | ~28 min (1.267) |
| 06 | 3 (rede e regra de ouro; cinco procedimentos; conferência por cálculo) | 2 | 1 | 2 figuras | ~30 min, com prática (1.213) |
| 07 (nova) | 3 (símbolos; receita da forma geral; leitura inversa) | 2 | 1 (+ 3 casos guiados) | 1 figura + releitura da figura 6 | ~28 min (1.191) |

Todas dentro do teto de ~1.600 palavras do contrato LC-02 (a aula 01 no limite).

## Achados

### 🟠 1. Aula 05 sobrecarregada: cinco ideias novas e duas construções

**Tipo:** sobrecarga
**Onde:** aula 05 (versão auditada)
**Problema:** a aula levava a construção da projeção, a fórmula e os hemisférios, as coordenadas φ e ρ, os grandes círculos e, ainda, os símbolos dos elementos de simetria e a forma geral das classes, com um exemplo de duas partes (polo de (111) e forma geral de 2/m). Pela contagem de carga, ~45 min, num conteúdo que o hub do módulo marca como o ponto de dificuldade ("a passagem 3D → 2D exige figura e exercício, não texto"). A parte de simetria é uma ideia independente, com fronteira conceitual clara.
**Correção aplicada:** **divisão**. A aula 05 ficou com a projeção das faces (exemplo novo: os polos de seis faces do cubo e uma zona); a simetria no estereograma virou a **aula 07, "Simetria no estereograma: elementos e forma geral das classes"**, depois da aula de medição, com a figura 9 (formas gerais calculadas de 2/m, mm2 e 4/mmm), a leitura inversa (do estereograma à classe) e a releitura da figura 6 como estereograma de m3̄m. A aula 07 cobre o mesmo objetivo `mineralogia-m05-oa04` (não houve objetivo novo); recebeu o ID `mineralogia-m05-a07`, o próximo livre, sem renumerar as demais.
**Escopo:** exigiu nova aula no módulo (decisão do orquestrador); o módulo passa a 7 aulas e, por isso, a avaliação passa a parciais + final.

### 🟠 2. Aula 03 acima de 30 minutos

**Tipo:** sobrecarga
**Onde:** aula 03 · Converter entre três e quatro índices
**Problema:** direções, famílias, perpendicularidade, quatro índices de face, tabela de formas, conversões de face **e** de direção, e o caso da calcita: ~35 min. As direções de quatro índices [uvtw] são o item menos usado no resto do curso e o mais propenso a erro.
**Correção aplicada:** as direções [uvtw] foram para uma nota "Para consulta (não precisa decorar)"; o corpo recomenda [UVW] com três índices, que o curso usa daqui em diante. O erro comum correspondente remete à nota.
**Escopo:** correção local.

### 🟡 3. Remissão de módulo trocada na aula 02

**Onde:** aula 02 · A face unitária define a régua
**Correção aplicada:** "a cela unitária (módulo 06), medida por difração (módulo 18)" no lugar de "medida por difração (módulo 06)".

### 🟡 4. Tabela de minerais reais sem instrução de uso (aula 01)

**Problema:** seis linhas de parâmetros com três decimais convidam a decorar, como a tabela de 32 representantes do módulo 04.
**Correção aplicada:** "A tabela é de consulta: o que importa é o padrão de igualdades, não os decimais." Para manter a aula no teto, saiu uma frase redundante sobre a razão c/a = 1,2. O baralho segue a mesma regra: nenhum card pede parâmetro com decimais.

### 🟡 5. Dedução da lei das zonas abstrata para o nível

**Onde:** aula 04 · A lei das zonas
**Correção aplicada:** "Se a dedução pesar, guarde a regra: é ela que se usa." A dedução fica para quem quiser o porquê.

### 🟡 6. Remissões internas desatualizadas pela divisão

**Correção aplicada:** "Próxima aula" da aula 06 aponta para a aula 07; a aula 07 fecha o módulo e aponta para o módulo 06; a aula 01 remete à aula 06 (e não "05 e 06") para a medição dos ângulos; a aula 05 remete os elementos de simetria à aula 07.

### 🔵 7. Rede de Wulff para imprimir

**Sugestão:** a aula 06 pede prática com papel vegetal. Uma rede de 2° em tamanho real (20 cm) gerada pelo mesmo script da figura 7 e anexada ao módulo permitiria a prática sem procurar rede na internet.
**Desfecho:** aberto, não bloqueante.

### 🔵 8. Goniômetro de papel

**Sugestão:** um goniômetro de contato de papel (transferidor com régua articulada) tornaria concreta a lei de Steno do módulo 04 e o ângulo interno da aula 06.
**Desfecho:** aberto, não bloqueante.

### 🔵 9. Estereogramas das 32 classes

**Observação:** a revisão do módulo 04 pediu uma remissão de volta à tabela das oito famílias com os estereogramas das 32 classes. A aula 07 faz a remissão, ensina o método e mostra cinco classes calculadas (2/m, mm2, 4/mmm no desenho; 4/m, 4mm, 422, 4̄ e 6̄ no texto). Um quadro com as 32 seria material de consulta útil, mas excede a aula.
**Desfecho:** registrado; candidato a anexo do módulo se o usuário quiser.

## Pontos fortes (manter)

- Toda figura foi **calculada**, não desenhada: os ângulos escritos nas figuras 8 e 9 são os mesmos que o texto ensina a obter, o que permite ao aluno conferir a régua.
- O quartzo atravessa o módulo (índices na aula 03, zona na aula 04, medida na aula 06), e a calcita mostra que o índice depende da cela.
- Cada exemplo trabalhado termina em "método geral" e em conferência (a soma h + k + i, a pertença à zona, a contagem pela ordem do grupo).
- Os erros comuns atacam as confusões clássicas do tema: inverter ou não inverter, (hkl) × {hkl} × [uvw], distância ∝ ρ, Wulff × Schmidt.

## Correções aplicadas

| # | Severidade | Desfecho | Arquivos |
|---|---|---|---|
| 1 | 🟠 | Corrigido (aula dividida; aula 07 criada) | aula-05, aula-06, aula-07 (nova), figura 9 (nova) |
| 2 | 🟠 | Corrigido | aula-03 |
| 3-6 | 🟡 | Corrigidos | aula-01, aula-02, aula-04, aula-05, aula-06 |
| 7-9 | 🔵 | 7 e 8 abertos; 9 registrado | — |

As alegações novas (aula 07 e exemplo novo da aula 05) foram conferidas pelo `auditor-cientifico` antes de fechar a revisão (seção "Segunda passagem" da auditoria do módulo).
