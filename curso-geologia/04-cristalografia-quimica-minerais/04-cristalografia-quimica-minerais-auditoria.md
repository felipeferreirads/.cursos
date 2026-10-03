# Auditoria científica — Módulo 04: Cristalografia e química dos minerais

**Modo:** `audit-and-fix` · **Profundidade:** `full` (as 7 aulas em conjunto)
**Data:** 2026-08-16
**Material auditado:** as 7 aulas do módulo 04 (2 aulas-ponte + 5 aulas de conteúdo), contra o contrato de nível `iniciante-absoluto-v1` (LC-01 a LC-08) e contra fontes normativas de cristalografia/mineralogia (Klein & Dutrow, *Manual of Mineral Science*; Nesse, *Introduction to Mineralogy*; IUCr, *International Tables for Crystallography*; Mindat.org; Strunz & Nickel, *Strunz Mineralogical Tables*).
**Veredito: ✅ Aprovado.**

## Resumo

| Severidade | Contagem |
|---|---|
| 🔴 Erro | 0 |
| 🟠 Impreciso | 0 |
| 🟡 Desatualizado | 0 |
| 🔵 Sem fonte | 0 |
| ⚪ Controverso | 0 |

**53 alegações auditáveis** verificadas (as já declaradas no rodapé de cada aula, mais checagem de consistência interna entre as 7). Nenhum achado de severidade 🔴/🟠/🟡/🔵/⚪. O módulo é o primeiro do curso, desde a repartida, a sair limpo na primeira auditoria — provavelmente porque cada aula já foi escrita com o bloco `alegacoes_auditaveis` e fontes citadas desde a redação, e o conteúdo (cristalografia/mineralogia descritiva básica) é estável na literatura, sem controvérsia de fronteira de pesquisa.

## Verificado e correto (amostra dos pontos de maior risco)

Todos os fatos abaixo foram checados por busca web contra fonte autoritativa, não de memória.

- **Sete sistemas cristalinos e exemplos minerais** (aula 05): confirmado — isométrico/pirita e granada, tetragonal/zircão, hexagonal/berilo, trigonal/quartzo, ortorrômbico/topázio, monoclínico/gipsita, triclínico/microclina. Fonte: busca cruzada (CK-12, Rockhounding Wiki, GeologyScience) + Klein & Dutrow.
  - Ponto de atenção verificado especificamente: várias fontes de divulgação geral classificam o quartzo como "hexagonal" de forma solta. A aula 05 trata esse ponto **corretamente e de forma pedagogicamente proposital** — explica que o quartzo tem hábito externo parecido com um prisma hexagonal, mas pertence ao sistema **trigonal** (eixo de ordem 3, não 6), que é a classificação cristalográfica precisa (grupo espacial do quartzo-α). Não é erro; é a aula antecipando e desarmando a confusão mais comum da literatura de divulgação. Nenhuma correção necessária.
- **Hemimorfita como sorossilicato** (aula 07): confirmado por Mindat.org e literatura mineralógica (Zn₄Si₂O₇(OH)₂·H₂O, unidade Si₂O₇ de dois tetraedros compartilhando um oxigênio). Correto.
- **Diamante × grafite (polimorfismo, ligação covalente 3D × van der Waals entre camadas)** (aula 02): consistente com cristalografia mineral padrão.
- **Classes químicas e critério do ânion dominante, sistemas Dana e Strunz** (aula 06): tratamento qualitativo correto e sem números de catálogo (deferidos de propósito, conforme nota da própria aula).
- **Cadeia simples (piroxênios) × cadeia dupla (anfibólios)** (aula 07): consistente com Deer, Howie & Zussman.
- **Regra de restrição cristalográfica (ordens de eixo só 1, 2, 3, 4, 6)** (aula 04): consistente com a teoria de grupos cristalográficos padrão.

## Consistência interna entre as 7 aulas

Auditadas em conjunto, como manda a prática adotada desde o módulo 02 (achado M02-F01) e reforçada no bloco I (achado transversal de espessura de crosta). Verificado:

- A gipsita aparece em duas aulas com papéis diferentes e compatíveis: sistema monoclínico (aula 05) e classe sulfato (aula 06) — a própria aula 06 já sinaliza explicitamente que são perguntas independentes sobre o mesmo mineral. Sem contradição.
- O quartzo aparece em três aulas (trigonal na aula 05, tectossilicato na aula 07, exemplo de ligação mista na aula 07) sem nenhum valor ou classificação divergente entre elas.
- O par pirita/hematita (mesmo metal, classes químicas diferentes) é usado de forma consistente entre aulas 05 e 06.
- Nenhum valor numérico duplicado com discrepância — o módulo, seguindo a regra LC-05 (ordem de grandeza, não precisão de laboratório), evita valores de precisão que costumam ser a fonte de inconsistência entre aulas (como ocorreu nos módulos 02 e 03 antes da repartida). Efeito colateral do contrato de nível funcionando como projetado.
- Progressão de pré-requisitos coerente: aula 01 (ponte átomo/elétrons) → aula 02 (ponte ligação) → aula 03 (definição de mineral, usa ligação) → aula 04 (simetria, usa estrutura cristalina da aula 03) → aula 05 (sistemas, usa simetria da aula 04) → aula 06 (classes químicas, usa ligação da aula 02 e sistemas da aula 05 como exemplos) → aula 07 (silicatos, usa ligação covalente da aula 02, classe da aula 06, solução sólida da aula 03). Nenhuma aula referencia um conceito ainda não construído.

## Conformidade com o contrato de nível (LC-01 a LC-08)

- **LC-01** (nenhum termo sem definição): todas as 7 aulas trazem bloco "Vocabulário desta aula" com 6 a 8 termos, e cada termo técnico é reapresentado em linguagem comum na primeira aparição no corpo. Conforme.
- **LC-02** (teto de 1.600 palavras): as 7 aulas registram entre ~1.480 e ~1.590 palavras de corpo (metadado `palavras_corpo`), dentro do teto. Conforme.
- **LC-03** (abertura padronizada): todas trazem "Antes de começar, você precisa saber" com links às aulas anteriores exigidas. Conforme.
- **LC-04** (analogia antes do termo): confirmado em todas — ex. "casa com janelas destrancadas" antes de elétron de valência (aula 01), "cabo de guerra" antes de ligação iônica/covalente (aula 02), "barraca de camping" antes de tetraedro SiO₄ (aula 07). Conforme.
- **LC-05** (ordem de grandeza): o módulo não usa nenhum valor de precisão de laboratório — trata dureza, ordens de eixo e classes de forma qualitativa/comparativa, como já discutido acima. Conforme.
- **LC-06** (sem matemática sem ponte): nenhuma notação de eixo cristalográfico com coordenadas, nenhum cálculo — a aula 05 declara explicitamente essa exclusão de escopo. Conforme.
- **LC-07** ("Erros comuns", "O que não concluir", "Recap relâmpago"): presentes nas 7 aulas. Conforme.
- **LC-08** (controvérsia em uma frase): não há controvérsia de literatura relevante neste módulo — cristalografia e classificação química mineral são domínios estáveis. Não se aplica achado ⚪.

## Correções aplicadas

**Aplicadas em:** 2026-08-16

Nenhuma. Nenhum achado 🔴/🟠/🟡/🔵/⚪ foi produzido nesta auditoria — não há o que corrigir nem propagar para material derivado.

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| — | — | — | — |

**Pendências:** nenhuma. O módulo está liberado para gerar o questionário e o baralho de flashcards, seguindo a ordem correta (auditoria → avaliação → memorização) adotada desde o módulo 00.
