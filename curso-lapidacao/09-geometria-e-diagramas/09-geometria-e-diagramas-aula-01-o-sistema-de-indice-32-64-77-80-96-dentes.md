# Aula 01: O sistema de índice — 32, 64, 77, 80, 96 dentes e o que a escolha determina

**ID:** lapidacao-m09-a01
**Módulo:** [[09-geometria-e-diagramas-modulo|Módulo 09]] — Geometria da máquina e leitura de diagramas de lapidação
**Duração estimada:** ~22 min
**Objetivo:** explicar o que o número de dentes do índice determina na simetria possível de um talhe.
**Pré-requisito:** [[03-maquinas-da-bancada-aula-04-a-facetadora-por-dentro|Aula 04 do módulo 03]] deste curso (o sistema de índice como roda dentada mais pino, que trava a pedra em posições angulares repetíveis) e [[03-maquinas-da-bancada-aula-05-anatomia-do-ajuste-batente-de-angulo-altura-do-mastro-e-o-cheater|Aula 05 do módulo 03]] (o índice como ajuste grosso da rotação, distinto do batente de ângulo e da altura do mastro). Nenhum pré-requisito específico do curso de Gemologia.

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **índice (index gear)** | neste módulo, sempre a roda dentada da facetadora — nunca o índice de refração da gema, que é outra grandeza com o mesmo nome curto. |
| **dente** | cada uma das posições angulares fixas gravadas na roda de índice; travar num dente é travar a pedra naquele ponto da volta. |
| **jogo de índice** | uma roda de índice específica, identificada pelo número total de dentes que ela tem — por exemplo, "o jogo de 96". |
| **simetria N-fold** | um talhe tem simetria N-fold quando N cópias idênticas de um mesmo grupo de facetas, giradas em ângulos iguais, completam a volta ao redor da pedra. |
| **divisor** | um número inteiro que cabe um número inteiro de vezes dentro de outro, sem sobra — por exemplo, 8 é divisor de 96 porque 96 ÷ 8 = 12, exato. |

## Antes de começar, você precisa saber

- Da [[03-maquinas-da-bancada-aula-04-a-facetadora-por-dentro|Aula 04 do módulo 03]]: o **sistema de índice** é uma roda dentada fixa ao cabeçote, mais um pino que cai entre dois dentes e trava a pedra numa posição angular repetível ao redor do próprio eixo dela.
- Da [[03-maquinas-da-bancada-aula-05-anatomia-do-ajuste-batente-de-angulo-altura-do-mastro-e-o-cheater|Aula 05 do módulo 03]]: o índice controla a **posição da faceta na volta** (simetria radial), nunca o ângulo — isso é do batente e da altura do mastro, outra família de ajuste inteiramente.
- Não é preciso saber ainda as três coordenadas completas de uma faceta (ângulo, índice, altura juntos) — é a aula 02 — nem ler um diagrama de lapidação — é a aula 03.

## Ao final você vai conseguir

- `lapidacao-m09-oa01` — Explicar o que o número de dentes do índice — 32, 64, 77, 80, 96 — determina na simetria possível de um talhe.

## Conteúdo

### Um nome, duas grandezas

Antes de qualquer coisa, uma advertência de vocabulário que este curso já cruzou de raspão no módulo 08: "índice" designa **duas grandezas completamente diferentes** na literatura de facetamento. Uma é o **índice de refração**, propriedade óptica da gema, do curso de Gemologia. A outra é o **índice** desta aula — a roda dentada da facetadora, também chamada *index gear*. As duas nada têm em comum além do nome curto. Sempre que a palavra aparecer sozinha neste módulo, é a roda dentada; quando for a grandeza óptica, este curso escreve "índice de refração" por extenso.

### O que a roda de índice já faz, em uma frase

A Aula 04 do módulo 03 apresentou o sistema de índice: uma roda dentada trava a pedra em posições angulares fixas ao redor do próprio eixo dela, dando **repetibilidade rotacional**. Esta aula pergunta o que muda quando a roda tem 32 dentes em vez de 96.

### A regra central: simetria só existe se o número de dentes for divisível por ela

Um talhe com simetria **N-fold** repete um mesmo grupo de facetas N vezes ao redor da pedra, cada cópia girada do mesmo ângulo exato em relação à anterior. Um talhe de 8 facetas iguais e igualmente espaçadas — simetria 8-fold — precisa que cada corte avance exatamente 1/8 da volta completa. Numa roda de N dentes, uma volta inteira corresponde a N dentes; avançar 1/8 de volta significa avançar N/8 dentes. Isso só dá um número inteiro de dentes — a única coisa que a roda consegue travar — se N/8 for exato, ou seja, **se 8 for divisor de N**.

A regra vale para qualquer simetria: um jogo de índice com N dentes só consegue cortar simetria M-fold se M for divisor de N. Não é uma convenção do ofício, é aritmética: a roda só trava em dentes inteiros, então só posições que sejam frações M/N inteiras da volta são alcançáveis.

### Os jogos correntes e o que cada um libera

A literatura de facetamento amador trabalha com um pequeno número de jogos de índice padronizados, cada um vendido como roda avulsa e trocável na máquina. O catálogo corrente de um fabricante de referência lista oito — 32, 64, 72, 77, 80, 84, 96 e 120 dentes. Esta aula trabalha com **cinco** deles — **32, 64, 77, 80 e 96** —, escolhidos por exporem os fatores primos que decidem a simetria. A tabela mostra os divisores de cada um — e, por eles, as simetrias que cada roda consegue cortar sozinha.

| Jogo (dentes) | Divisores (>1) | Simetrias que o jogo cobre |
|---|---|---|
| 32 | 2, 4, 8, 16, 32 | 2, 4, 8, 16 e 32-fold |
| 64 | 2, 4, 8, 16, 32, 64 | 2, 4, 8, 16, 32 e 64-fold |
| 77 | 7, 11, 77 | **só** 7 e 11-fold |
| 80 | 2, 4, 5, 8, 10, 16, 20, 40, 80 | inclui **5 e 10-fold**, além das potências de 2 |
| 96 | 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 96 | a cobertura mais ampla — inclui múltiplos de 3 |

O padrão salta à vista: 32 e 64 são potências de 2 puras, e só entregam simetrias que também são potências de 2. O 96 acrescenta o fator 3 (96 = 2⁵ × 3), o que abre 3, 6, 12, 24 e 48-fold — talhes com contorno hexagonal ou facetas em grupos de seis, muito comuns, exigem esse fator e nenhuma roda só-potência-de-2 os alcança. O 80 acrescenta o fator 5 (80 = 2⁴ × 5), a única forma de chegar a 5 e 10-fold — pentágonos e talhes de dez facetas por fileira. E o 77 é o caso mais extremo: como 77 = 7 × 11, ele **só** serve para simetria 7 ou 11-fold, e não serve para nada que uma roda de potência de 2 já resolvesse — nem 2-fold ele tem, porque 2 não é divisor de 77 (77 é ímpar). É a roda especializada por excelência: existe só para destravar o fator 7, que nenhuma das outras quatro tem.

### Por que cinco rodas, e não uma só

Se um único jogo cobrisse toda simetria útil, não haveria por que trocar de roda. O 96 é o mais versátil **dos cinco** — cobre onze simetrias diferentes. Mas essa cobertura não é recorde: fora da lista, o 72 e o 84 empatam com ele, e o 120 supera. A razão de fundo da adoção do 96 como jogo padrão é outra: **a grande maioria dos diagramas publicados é escrita em notação de 96**, o que faz dele a língua franca do ofício. E nenhuma roda cobre todos os fatores primos ao mesmo tempo: entre os cinco desta aula, só o 77 alcança 7-fold, porque nenhuma combinação de 2, 3 ou 5 chega a 7 — fora dela, o 84 (2² × 3 × 7) também alcança. A escolha do jogo de índice, então, não é sobre qual é "melhor" — é sobre **qual fator primo o design exige**, e a resposta está sempre no próprio diagrama de lapidação (aula 03), que declara a simetria do talhe antes de qualquer corte.

### O que a escolha do índice não determina

O número de dentes não diz nada sobre o **ângulo** de uma faceta nem sobre sua **altura** — essas duas coordenadas vêm de outros ajustes inteiramente, como a Aula 05 do módulo 03 já separou. Um jogo de 96 dentes trava posições rotacionais; ele não torna uma faceta mais rasa ou mais funda, nem é "mais preciso" em ângulo que um de 32.

## Exemplo trabalhado

**Um projetista tem em mãos os cinco jogos — 32, 64, 77, 80 e 96 — e precisa decidir qual roda serve para um talhe de simetria 8-fold, e qual serve para um talhe de simetria 7-fold.**

**Simetria 8-fold.** A pergunta é: 8 é divisor de qual desses cinco números? 32 ÷ 8 = 4 (exato); 64 ÷ 8 = 8 (exato); 77 ÷ 8 = 9,625 (não exato); 80 ÷ 8 = 10 (exato); 96 ÷ 8 = 12 (exato). Quatro dos cinco jogos servem — 32, 64, 80 e 96 —, e só o 77 fica de fora, porque 77 não tem o fator 2 em nenhuma potência.

**Simetria 7-fold.** Repetindo a pergunta com 7: 32 ÷ 7, 64 ÷ 7, 80 ÷ 7 e 96 ÷ 7 não são exatos — nenhum dos quatro tem o fator 7. Só 77 ÷ 7 = 11 é exato. **Um único jogo, entre os cinco, cobre essa simetria: o 77.**

**A lição do exemplo.** A simetria mais comum (8-fold, ligada às potências de 2) tem várias rodas candidatas; a simetria mais rara (7-fold) tem exatamente uma. É por isso que o 77 existe como jogo dedicado: ele não compete com o 96 em versatilidade, ele preenche um dos dois buracos que o 96 deixa entre os cinco — o fator 7. O outro, o fator 5, é o que o 80 preenche.

## Erros comuns

- **Confundir "índice" com índice de refração.** São duas grandezas com o mesmo nome curto e nada em comum; este módulo usa "índice" só para a roda dentada.
- **Achar que qualquer roda serve para qualquer simetria.** Simetria N-fold só é alcançável se N for divisor do número de dentes — é aritmética, não preferência.
- **Achar que mais dentes significa "mais preciso" em ângulo.** O número de dentes não toca no ângulo da faceta; ele só define quantas posições rotacionais existem numa volta.
- **Tratar o jogo de 96 como suficiente para tudo.** Ele é o mais versátil dos cinco, mas não tem nem o fator 5 nem o fator 7; 5 e 10-fold pedem o 80, e 7-fold pede uma roda dedicada — o 77 entre os cinco, o 84 fora deles.

## O que não concluir

- Não concluir como se troca fisicamente a roda de índice na máquina — competência de bancada, fora do escopo teórico deste curso.
- Não concluir a fórmula ou a lógica de ângulo e altura como coordenadas da faceta — é a aula 02 deste módulo.
- Não concluir como ler a simetria declarada num diagrama de lapidação real — é a aula 03.
- Não concluir nada sobre o cheater ou o ajuste fino de índice — já coberto na Aula 05 do módulo 03 e retomado na aula 05 deste módulo sob outro ângulo (o diagnóstico de erro).

## Recap relâmpago

- "Índice" tem dois sentidos: a roda dentada da facetadora (este módulo) e o índice de refração da gema (Gemologia). São grandezas diferentes.
- Simetria **N-fold** só é alcançável com um jogo de índice de N₀ dentes se N for **divisor** de N₀ — a roda só trava em posições de dente inteiro.
- Os cinco jogos correntes e o que cada um libera: **32** e **64** (potências de 2 puras — 2, 4, 8, 16... fold), **96** (a cobertura mais ampla, com o fator 3 — inclui 3, 6, 12, 24, 48-fold), **80** (o fator 5 — inclui 5 e 10-fold), **77** (7 × 11 — só 7 e 11-fold, nenhuma outra).
- Nenhum jogo cobre todos os fatores primos ao mesmo tempo; a escolha do jogo depende do fator que o design exige, declarado no diagrama de lapidação.
- O número de dentes não determina ângulo nem altura da faceta — só a posição rotacional.

## Próxima aula

Na [[09-geometria-e-diagramas-aula-02-angulo-indice-e-altura-as-tres-coordenadas-da-faceta|Aula 02 — Ângulo, índice e altura]], o índice desta aula se junta ao batente de ângulo e à altura do mastro — já localizados no módulo 03 — para formar as três coordenadas que definem qualquer faceta, e cada uma ganha o nome que os diagramas de lapidação usam para ela.

## Fontes consultadas

- United States Faceters Guild, *dicionário de facetamento* — definição de índice (index) como a roda dentada usada para fixar o ângulo de circunferência. Consultada em 2026-09-06.
- International Faceting Academy, *Which Index Gear?* (facetingacademy.com) — a relação entre número de dentes e quantidade de simetrias cobertas ("the 96 gear allows 11 symmetries"; "the 120 gear allows the most possible symmetries — 14 of them"; o 72 e o 84 "offer as many different symmetries as the 96") e a nota de que "only the 84 will let you do 7-fold or 14-fold symmetry". Consultada em 2026-09-06. **Essa página não menciona o jogo de 77** — a caracterização do 77 vem das fontes abaixo.
- ULTRA TEC Faceting, catálogo de *Index Gears* (ultratec-facet.com) — a lista corrente de jogos de índice: 32, 64, 72, 77, 80, 84, 96 e 120. Consultada em 2026-09-06.
- Sky Jems, *96 Index: The Standard Indexing Gear in Faceting* — os divisores do 96 e a razão de fundo de sua adoção como padrão: "the overwhelming majority of published facet diagrams are written to 96-index notation". Consultada em 2026-09-06.
- GemologyOnline.com, tópico *Index Gears* — o 77 como jogo de 7 e 11 apenas, e a observação de que designs 7-fold com o 77 são raros. Consultado em 2026-09-06.
- Vargas & Vargas, *Faceting for Amateurs* — os jogos de índice correntes na bancada amadora.
- Cálculo direto dos divisores de 32, 64, 77, 80 e 96 — a tabela de simetrias desta aula é derivada por aritmética, não copiada de fonte.
- [[03-maquinas-da-bancada-aula-04-a-facetadora-por-dentro|módulo 03, aula 04]] e [[03-maquinas-da-bancada-aula-05-anatomia-do-ajuste-batente-de-angulo-altura-do-mastro-e-o-cheater|aula 05]] deste curso — a definição física do sistema de índice, reativada nesta aula.

<!--
nivel: ensino-medio-com-gemologia-v1
palavras_corpo: 1588
cobertura:
  lapidacao-m09-oa01: [Conteúdo, "Exemplo trabalhado", "Erros comuns", "Recap relâmpago"]
alegacoes_auditaveis:
  - claim_id: IDX-DUPLO-SENT-001
    claim: "A palavra indice designa duas grandezas distintas na literatura de facetamento: o indice de refracao (propriedade optica da gema) e o indice/index gear (a roda dentada da facetadora que trava posicoes angulares de rotacao). As duas nao tem relacao alguma alem do nome curto compartilhado."
    risk: consistencia interna
    source: "United States Faceters Guild, dicionario de facetamento (index); curso de lapidacao, modulo 08 aula 06 (uso do termo indice para a posicao no disco dentado, distinto do indice de refracao)"
  - claim_id: IDX-REGRA-DIVISOR-001
    claim: "Um jogo de indice com N0 dentes so consegue cortar simetria N-fold se N for divisor de N0, porque uma volta completa corresponde a N0 dentes e avancar 1/N da volta exige avancar N0/N dentes — um numero que so e inteiro (a unica coisa que a roda consegue travar) quando N divide N0 exatamente."
    risk: mecanismo
    source: "International Faceting Academy, Which Index Gear? (facetingacademy.com) — relacao entre divisores do numero de dentes e simetrias cobertas; derivacao aritmetica direta"
  - claim_id: IDX-JOGO-CORRENTE-001
    claim: "O catalogo corrente de um fabricante de referencia (Ultra Tec) lista oito jogos de indice: 32, 64, 72, 77, 80, 84, 96 e 120 dentes, vendidos como rodas avulsas trocaveis na maquina. Esta aula trabalha com cinco deles (32, 64, 77, 80, 96), escolhidos por exporem os fatores primos que decidem a simetria. O jogo de 96 e o mais versatil DESSES CINCO (11 simetrias), mas nao detem o recorde de cobertura no mercado: o 72 e o 84 tambem cobrem 11 e o 120 cobre mais. A razao de fundo da adocao do 96 como padrao nao e a amplitude de cobertura e sim a notacao: a grande maioria dos diagramas publicados e escrita em notacao de 96."
    risk: fato tecnico
    source: "ULTRA TEC Faceting, catalogo de Index Gears (lista dos oito jogos); International Faceting Academy, Which Index Gear? ('the 96 gear allows 11 symmetries'; '120 ... 14 of them'; 72 e 84 'offer as many different symmetries as the 96'); Sky Jems, 96 Index: The Standard Indexing Gear in Faceting ('the overwhelming majority of published facet diagrams are written to 96-index notation'); Vargas & Vargas, Faceting for Amateurs. Verificado em 2026-09-06."
  - claim_id: IDX-DIVISOR-TAB-001
    claim: "Os divisores maiores que 1 de cada jogo sao: 32 = {2,4,8,16,32}; 64 = {2,4,8,16,32,64}; 77 = {7,11,77}; 80 = {2,4,5,8,10,16,20,40,80}; 96 = {2,3,4,6,8,12,16,24,32,48,96}. Por consequencia, 32 e 64 cobrem so simetrias potencia de 2; 96 acrescenta o fator 3 (96 = 2^5 x 3); 80 acrescenta o fator 5 (80 = 2^4 x 5), unica fonte de 5 e 10-fold entre os cinco; 77 = 7 x 11 cobre exclusivamente 7 e 11-fold, sem nenhuma simetria em comum com as outras quatro rodas, incluindo a ausencia de 2-fold (77 e impar). RESSALVA DE ESCOPO: o 77 e a unica fonte de 7-fold ENTRE ESSES CINCO, nao no mercado — o jogo de 84 (= 2^2 x 3 x 7) tambem carrega o fator 7 e ainda alcanca 14-fold, que o 77 nao alcanca. E o 96 deixa DOIS buracos entre os cinco, nao um: o fator 5 (preenchido pelo 80) e o fator 7 (preenchido pelo 77)."
    risk: dado numerico
    source: "Calculo direto de divisores (aritmetica, verificado); International Faceting Academy, Which Index Gear? ('only the 84 will let you do 7-fold or 14-fold symmetry'; 'the 96 gear allows 11 symmetries') — ESSA PAGINA NAO MENCIONA O JOGO DE 77; a caracterizacao 'the 77 is 7 and 11 only' vem de GemologyOnline.com, topico Index Gears, que tambem registra que designs 7-fold com o 77 sao raros. Verificado em 2026-09-06."
  - claim_id: IDX-NAO-ANGULO-001
    claim: "O numero de dentes do indice nao determina angulo nem altura de faceta — essas duas coordenadas vem do batente de angulo e da altura do mastro, ja separados como outra familia de ajuste na Aula 05 do modulo 03 deste curso. Uma roda com mais dentes oferece mais posicoes rotacionais possiveis numa volta, nao maior precisao de angulo."
    risk: consistencia interna
    source: "curso de lapidacao, modulo 03 aula 05 (as duas familias de ajuste: plano radial vs. posicao na volta)"
-->
