# Revisão didática: Módulo 03 — A Terra como fábrica de minerais

**Revisado em:** 2026-10-04  ·  **Modo:** review-and-fix
**Material:** `curso-mineralogia/03-terra-fabrica-de-minerais/` — aulas 01 a 04, depois da auditoria científica
**Veredito:** Bem ensinado com ressalvas → **ressalvas 🟠 e 🟡 corrigidas**

## Resumo

🔴 0 bloqueiam · 🟠 1 prejudica · 🟡 7 atrito · 🔵 2 sugestões

**Carga estimada por aula** (contagem de `gerador-de-aula`; palavras de corpo entre parênteses, depois das correções):

| Aula | Conceitos novos | Pré-requisitos reativados | Exemplos | Visuais | Duração |
|---|---|---|---|---|---|
| 01 | 6 (evidências do interior, camadas, duas crostas, peridotito e fase aluminosa, transições 410/660, núcleo) | 2 (silicatos da crosta, polimorfo) | 1 | 1 tabela + 1 figura descrita | ~30 min (1.558) |
| 02 | 4 (três famílias, textura ígnea, intemperismo e diagênese, foliação) | 1 (minerais da crosta) | 1 (3 amostras) | 1 diagrama + 1 tabela | ~28 min (1.391) |
| 03 | 5 (pressão litostática, gradiente/geoterma, diagrama P-T, litosfera/astenosfera, ambientes tectônicos) | 2 (GPa/kbar, polimorfo) | 1 (duas contas) | 1 tabela grande + 1 figura descrita | ~30 min (~1.560) |
| 04 | 4 (solubilidade e seus controles, fontes de água, cinco mecanismos de supersaturação, minerais hidratados) | 2 (ligação iônica, ambientes) | 1 | 1 tabela | ~29 min (1.385) |

Todas abaixo do teto de 1.600 palavras do contrato LC-02. O módulo cumpre o papel declarado no hub: dar o mínimo de contexto geológico, sem virar curso de petrologia. A escada de inferência aparece de forma explícita no exemplo da aula 02 (observação → processo) e no "O que não concluir" da aula 04.

## Achados

### 🟠 1. Aula 01 acima de 30 minutos de carga

**Tipo:** sobrecarga
**Onde:** aula 01 · seção "Duas maneiras de fatiar a Terra"
**Problema:** a aula somava sete conceitos novos (~28 min só de conceitos, mais exemplo, tabela e figura: ~38 min estimados). O sétimo, litosfera × astenosfera, é mecânico e não serve ao objetivo `mineralogia-m03-oa01` (composição das camadas); serve à tectônica.
**Correção aplicada:** a seção foi **movida para a aula 03**, como "Antes das placas: litosfera e astenosfera", imediatamente antes da tabela de ambientes, com o termo no vocabulário, o erro comum ("igualar crosta e litosfera") e uma linha no recap. A alegação `TER-LIT-ESPESS-001` foi junto. A aula 01 ficou com seis conceitos e ~30 min; a aula 03, que estava curta, absorveu o conteúdo sem passar do teto.
**Escopo:** reorganização entre aulas do módulo.

### 🟡 2. Nomes de minerais e rochas sem glossa (aula 01)

**Onde:** aula 01 · evidências, manto, crosta
**Correção aplicada:** "condritos (meteoritos rochosos primitivos)", "pirolito, o modelo de composição do manto", "ortopiroxênio e clinopiroxênio (dois tipos de piroxênio, módulo 34)", "espinélio (um óxido de Mg e Al)", "zircão (silicato de zircônio, muito resistente)". Conferidas pelo auditor (`TER-REV-GLOSSAS-001`).

### 🟡 3. Minerais de alta pressão sem glossa (aula 03)

**Onde:** aula 03 · tabela de ambientes
**Correção aplicada:** glaucofânio (anfibólio azul de Na), lawsonita (silicato hidratado de Ca e Al), onfacita (piroxênio de Na e Ca), cordierita (silicato de Mg e Al); xisto azul e eclogito como "rochas metamórficas de alta pressão". Conferidas pelo auditor (`TER-REV-GLOSSAS-002`).

### 🟡 4. Leitura da geoterma com imagem ambígua

**Onde:** aula 03 · Ler uma geoterma num diagrama P-T
**Problema:** "quanto mais inclinada para a temperatura" não diz ao aluno de ensino médio o que olhar na figura.
**Correção aplicada:** "se ela se deita para o lado da temperatura (muitos graus em poucos quilômetros), o lugar é quente; se ela desce quase reta pelo eixo da pressão (muitos quilômetros para poucos graus), o lugar é frio".

### 🟡 5. "Estaurolita" sem glossa

**Onde:** aula 02 · Metamórficas
**Correção aplicada:** "(silicato de Fe e Al típico dessas rochas)".

### 🟡 6. "Pegmatitos", "esfalerita" e "autoclaves" sem glossa

**Onde:** aula 04 · tabela de origens; mecanismo 3; quartzo sintético
**Correção aplicada:** "(rochas ígneas de cristais muito grandes)"; "o sulfeto de zinco"; "(recipientes fechados de alta pressão)". Conferidas pelo auditor (`TER-REV-GLOSSAS-003`).

### 🟡 7. Duração declarada da aula 01 subestimada

**Onde:** cabeçalho da aula 01
**Correção aplicada:** de ~28 para ~30 min, coerente com a carga depois da mudança do achado 1.

### 🟡 8. Duplicação do erro "crosta = litosfera"

**Onde:** aula 03, depois da mudança
**Correção aplicada:** a frase ficou só em "Erros comuns", sem repetir no corpo.

### 🔵 9. Figuras descritas, não desenhadas

**Onde:** aula 01 (corte da Terra) e aula 03 (diagrama P-T com geotermas e ponto triplo do Al₂SiO₅)
**Sugestão:** produzir as duas figuras (SVG) quando o curso tiver um passo de ilustração; as legendas "O que observar" já estão escritas. O diagrama P-T é o mais importante: o módulo 22 vai reutilizá-lo.
**Desfecho:** aberto, não bloqueante.

### 🔵 10. Um exercício de conversão na aula 01

**Sugestão:** um "Pare e explique" que peça a pressão a 410 km pela regra de bolso e mostre por que ela falha no manto (densidade maior, g quase constante) reforçaria o elo com a aula 03.
**Desfecho:** aberto, não bloqueante.

## Pontos fortes (manter)

- Cada aula fecha com um exemplo que obriga a **usar** a ideia em vez de lembrá-la (peridotito com granada × espinélio; três amostras pela textura; duas contas de P e T; três minerais de uma mesma chaminé).
- Os "Erros comuns" atacam o modelo mental errado dominante do aluno sem geologia: manto líquido, metamorfismo que funde, fusão só por calor, "tudo dissolve mais no quente".
- O módulo planta, sem ensinar ainda, os ganchos do curso: polimorfos de alta pressão (10, 22, 43), ponto triplo do Al₂SiO₅ (22, 40), espaço aberto e faces livres (04, 25).

## Correções aplicadas

| # | Severidade | Desfecho | Arquivos |
|---|---|---|---|
| 1 | 🟠 | Corrigido (reorganização) | aula-01, aula-03 |
| 2-8 | 🟡 | Corrigidos | aula-01, aula-02, aula-03, aula-04 |
| 9-10 | 🔵 | Abertos, não bloqueantes | — |

As glossas novas foram conferidas pelo `auditor-cientifico` antes de fechar a revisão (ver a seção "Segunda passagem" da auditoria do módulo).
