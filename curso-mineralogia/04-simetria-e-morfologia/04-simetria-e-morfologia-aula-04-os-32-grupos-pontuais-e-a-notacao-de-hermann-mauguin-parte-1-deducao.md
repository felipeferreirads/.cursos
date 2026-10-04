# Aula 04: Os 32 grupos pontuais e a notação de Hermann-Mauguin — Parte 1: dedução

**ID:** mineralogia-m04-a04
**Módulo:** [[04-simetria-e-morfologia-modulo|Módulo 04 — Simetria e morfologia cristalina: operações, classes e sistemas]]
**Duração estimada:** ~30 min
**Nível:** ensino médio, sem geologia prévia (contrato `ensino-medio-sem-geologia-v1`)
**Objetivo:** explicar por que existem exatamente 32 combinações de elementos de simetria compatíveis com um cristal, e escrever o grupo pontual de um conjunto de elementos no símbolo de Hermann-Mauguin, curto e completo. *(A Parte 2 aplica isso a cristais reais.)*
**Pré-requisito:** [[04-simetria-e-morfologia-aula-03-operacoes-de-simetria-ii-rotoinversao-e-combinacao-de-elementos|Aula 03]] (rotoinversão e regras de combinação).

## Vocabulário desta aula

| Termo | O que quer dizer |
|---|---|
| **grupo pontual (classe cristalina)** | o conjunto completo de operações de simetria de um cristal que deixam pelo menos um ponto fixo (o centro do cristal). Os dois nomes são sinônimos em mineralogia. |
| **ordem do grupo** | o número de operações do grupo, contando a identidade. |
| **notação de Hermann-Mauguin (internacional)** | o modo padrão de escrever um grupo pontual com até três "posições", cada uma descrevendo uma direção do cristal. |
| **símbolo completo / curto** | o completo escreve tudo o que há em cada direção (4/m 2/m 2/m); o curto omite o que pode ser deduzido (4/mmm). |
| **centrossimétrico** | grupo que contém o centro de inversão. |

## Antes de começar, você precisa saber

- Os elementos 1, 2, 3, 4, 6, m, 1̄, 3̄, 4̄, 6̄ e as equivalências 2̄ = m e 6̄ = 3/m: [[04-simetria-e-morfologia-aula-03-operacoes-de-simetria-ii-rotoinversao-e-combinacao-de-elementos|aula 03]].
- As quatro regras de combinação (eixo par + espelho perpendicular ⇒ centro; dois espelhos ⇒ eixo; eixo n multiplica espelhos e eixos 2): mesma aula.

## Ao final você vai conseguir

- `mineralogia-m04-oa03` — Deduzir o grupo pontual (classe cristalina) de um cristal a partir dos seus elementos de simetria e escrevê-lo em notação de Hermann-Mauguin. *(Parte 1: dedução e escrita do símbolo a partir de uma lista de elementos.)*

## Conteúdo

### Por que 32

A aula 03 mostrou que os elementos de simetria se geram uns aos outros até fechar um conjunto. Quantos conjuntos fechados são possíveis com os eixos permitidos (ordens 1, 2, 3, 4 e 6)? A resposta foi obtida por Johann Hessel, em 1830, e redescoberta de forma mais clara por Axel Gadolin, em 1867: **32**. Cada um é um **grupo pontual**, ou **classe cristalina**. Todo cristal pertence a exatamente uma delas.

Dá para reconstruir a contagem em oito famílias, partindo do mais simples:

| Família | Receita | Classes | Quantas |
|---|---|---|---|
| Só rotação | um eixo de ordem n | 1, 2, 3, 4, 6 | 5 |
| Só rotoinversão | um eixo n̄ | 1̄, m (= 2̄), 3̄, 4̄, 6̄ | 5 |
| Eixo par + espelho perpendicular | n/m | 2/m, 4/m, 6/m | 3 |
| Eixo + eixos 2 perpendiculares | n2(2) | 222, 32, 422, 622 | 4 |
| Eixo + espelhos que o contêm | nm(m) | mm2, 3m, 4mm, 6mm | 4 |
| Eixo de rotoinversão + eixos 2 e espelhos | n̄2m | 4̄2m, 6̄m2, 3̄m | 3 |
| Tudo junto | n/m m m | mmm, 4/mmm, 6/mmm | 3 |
| Quatro eixos 3 em diagonal (cúbicas) | 23 e derivados | 23, m3̄, 432, 4̄3m, m3̄m | 5 |
| | | **Total** | **32** |

Por que 3/m não aparece entre os n/m? Porque 3/m é o mesmo que 6̄, já contado. Por que não existe "5mm" ou "8/m"? Porque ordens 5 e 8 não são permitidas (aula 02). A tabela não precisa ser decorada: ela mostra que o número 32 é consequência, não convenção.

### A notação de Hermann-Mauguin: um símbolo, até três direções

A lista "3A₄ 4A₃ 6A₂ 9P C" da aula 02 é longa e redundante: as regras de combinação já dizem que boa parte dela decorre do resto. Carl Hermann (1928) e Charles-Victor Mauguin (1931) propuseram um símbolo compacto, adotado nas *International Tables* a partir de 1935. As regras:

1. O símbolo tem **até três posições**. Cada posição descreve **uma direção** do cristal (ou um conjunto de direções equivalentes).
2. Em cada posição, escreve-se o **eixo** que há naquela direção (2, 3, 4, 6, ou 3̄, 4̄, 6̄) e, se houver um **espelho perpendicular** a essa direção, acrescenta-se "/m". Se há só espelho perpendicular, sem eixo, escreve-se "m".
3. **Quais** direções ocupam cada posição depende do sistema cristalino (aula 06). Por enquanto, basta esta tabela:

| Tipo de cristal (sistema) | 1ª posição | 2ª posição | 3ª posição |
|---|---|---|---|
| eixo 4 ou 4̄ único (tetragonal) | o eixo 4 | as 2 direções perpendiculares a ele, paralelas às arestas da base | as 2 direções diagonais da base |
| eixo 3, 3̄, 6 ou 6̄ único (trigonal, hexagonal) | o eixo principal | as direções perpendiculares a ele, a 120° | (hexagonal) as direções intermediárias, a 30° das anteriores |
| três direções perpendiculares, não equivalentes (ortorrômbico) | x | y | z |
| quatro eixos 3 diagonais (cúbico) | as 3 arestas do cubo | as 4 diagonais | as 6 diagonais de face |

### Do completo ao curto

*Figura sugerida: quatro sólidos lado a lado, cada um com seus elementos desenhados e o símbolo embaixo: pirâmide de base quadrada (4mm), bipirâmide de base quadrada (4/mmm), disfenoide (4̄2m) e tijolo (mmm). O que observar: em cada posição do símbolo, o eixo e o espelho perpendicular àquela direção.*

O cubo da aula 02 fica assim, posição por posição:

- **Arestas do cubo** (3 direções): eixo 4 com espelho perpendicular → **4/m**.
- **Diagonais do cubo** (4 direções): eixo 3 que, combinado com o centro, é 3̄ → **3̄**.
- **Diagonais de face** (6 direções): eixo 2 com espelho perpendicular → **2/m**.

Símbolo **completo: 4/m 3̄ 2/m**. Ele reconstrói tudo: 3 eixos 4 + 3 espelhos; 4 eixos 3̄ (que trazem o centro); 6 eixos 2 + 6 espelhos. Total: 3 + 6 = 9 espelhos, como na lista antiga.

O símbolo **curto** omite o que as regras de combinação já garantem: os eixos 2 que dois espelhos perpendiculares geram, e o centro, que vem de eixo par + espelho perpendicular. O cubo fica **m3̄m**. O tijolo da aula 02 (3 eixos 2, 3 espelhos, centro) fica, completo, **2/m 2/m 2/m** e, curto, **mmm**. A caixa de base quadrada, **4/m 2/m 2/m**, curto **4/mmm**.

Três detalhes de leitura, que causam a maioria dos erros:

- No sistema cúbico, a **segunda posição é sempre 3 ou 3̄**. Um "3" na segunda posição é a assinatura do cúbico; em 32 ou 3m, o "3" está na primeira posição e o cristal é trigonal.
- **"m" numa posição significa espelho perpendicular àquela direção**, não um espelho que contém a direção. Em 4mm, os espelhos são perpendiculares às direções da 2ª e da 3ª posição, e por isso **contêm** o eixo 4.
- "1" e "1̄" só aparecem sozinhos (as duas classes de menor simetria). Uma posição sem nada de especial simplesmente não é escrita.

> [!question] Pare e explique
> O símbolo curto mmm não mostra nenhum eixo de rotação. Como você sabe que ele tem três eixos 2?

### Centrossimétricos e não centrossimétricos

Das 32 classes, **11 têm centro**: 1̄, 2/m, mmm, 4/m, 4/mmm, 3̄, 3̄m, 6/m, 6/mmm, m3̄, m3̄m. As 21 restantes não têm. A diferença não é só de contagem: só cristais **sem centro** podem ter propriedades que distinguem um sentido do outro numa direção, como a piezoeletricidade (gerar tensão elétrica sob pressão) do quartzo, que é da classe 32. Essa conexão aparece na aula 05.

## Exemplo trabalhado

**Problema.** Escreva o símbolo de Hermann-Mauguin, completo e curto, de três cristais:
(A) um eixo 6 vertical, um espelho horizontal, seis eixos 2 horizontais, sete espelhos no total e centro;
(B) três eixos 2 perpendiculares entre si, sem espelho e sem centro;
(C) um eixo 3 vertical, três espelhos verticais e nada mais.

**Passo 1. (A), 1ª posição.** Eixo 6 vertical com espelho perpendicular (o horizontal): **6/m**.

**Passo 2. (A), 2ª e 3ª posições.** Seis eixos 2 horizontais formam dois conjuntos de três (a 30° entre si). Os seis espelhos verticais restantes (7 − 1) são perpendiculares a eles. Cada posição: **2/m**. Completo: **6/m 2/m 2/m**; curto: **6/mmm**. Ordem do grupo: 24.

**Passo 3. (B).** Três direções perpendiculares, não equivalentes (ortorrômbico), cada uma com eixo 2 e nada mais: **222** (completo e curto são iguais).

**Passo 4. (C).** Eixo 3 na 1ª posição. Os três espelhos verticais são perpendiculares às três direções horizontais a 120°: **3m**. Sem eixo 2 horizontal e sem centro.

**Passo 5. Verificação pela tabela de famílias.** 6/mmm está em "tudo junto"; 222, em "eixo + eixos 2 perpendiculares"; 3m, em "eixo + espelhos que o contêm". Os três estão entre os 32.

**Método geral:** identifique o eixo principal (ou os quatro eixos 3), atribua as direções às posições pela tabela do sistema, escreva eixo e "/m" em cada posição, e só depois abrevie.

## Erros comuns

- **Ler o "m" como espelho que contém a direção.** É natural, porque o "m" fica "junto" do eixo. Na convenção, ele é perpendicular à direção da posição.
- **Achar que m3̄m e 3̄m são parentes por causa das letras.** O primeiro é cúbico (3̄ na 2ª posição); o segundo é trigonal (3̄ na 1ª).
- **Escrever o mesmo elemento duas vezes**, por exemplo "6/m m" para o espelho horizontal e de novo para os verticais. Cada posição corresponde a uma direção.
- **Inventar classes como 3/m ou 5m.** 3/m existe como 6̄; ordem 5 não existe em cristais.

## O que não concluir

- Que os 32 grupos pontuais descrevam a estrutura atômica completa. Somando as operações com translação, chega-se aos 230 grupos espaciais (módulo 07).
- Que o símbolo curto "perca" informação. Ele perde redundância, não simetria: o completo sempre pode ser reconstruído.
- Que todas as 32 classes sejam comuns entre os minerais. Algumas têm pouquíssimos representantes naturais (aula 05).

## Recap relâmpago

- 32 grupos pontuais (classes cristalinas), deduzidos por Hessel (1830) e Gadolin (1867).
- Oito famílias: n; n̄; n/m; n22; nmm; n̄2m; n/mmm; cúbicas (23, m3̄, 432, 4̄3m, m3̄m).
- Hermann-Mauguin: até três posições, cada uma uma direção; eixo + "/m" se houver espelho perpendicular.
- Cubo: 4/m 3̄ 2/m (completo) = m3̄m (curto); tijolo: 2/m 2/m 2/m = mmm.
- No cúbico, a 2ª posição é sempre 3 ou 3̄.
- 11 classes centrossimétricas; 21 sem centro.

## Próxima aula

Em [[04-simetria-e-morfologia-aula-05-os-32-grupos-pontuais-parte-2-reconhecer-a-classe-num-cristal-real|Aula 05 — Os 32 grupos pontuais, Parte 2]], você vai aplicar o método a cristais reais, com faces distorcidas, estrias e hemimorfismo, e conhecer um mineral representante de cada classe.

## Fontes consultadas

- *International Tables for Crystallography*, vol. A (2016), IUCr (os 32 grupos pontuais; símbolos completo e curto; direções de simetria por sistema).
- Klein, C. & Dutrow, B., *Manual of Mineral Science*, 23ª ed., Wiley (dedução dos 32 grupos; notação de Hermann-Mauguin).
- Burke, J. G. (1966), *Origins of the Science of Crystals* (Hessel, 1830; Gadolin, 1867).
- Hermann, C. (1928), *Zeitschrift für Kristallographie* 68, 257–287; Mauguin, C. (1931), *Zeitschrift für Kristallographie* 76, 542–558 (origem da notação); *Internationale Tabellen zur Bestimmung von Kristallstrukturen* (1935).

<!--
nivel: ensino-medio-sem-geologia-v1
palavras_corpo: 1429
cobertura:
  mineralogia-m04-oa03: [Conteúdo, Exemplo trabalhado]
alegacoes_auditaveis:
  - claim_id: CRI-GP-32-001
    claim: "Existem exatamente 32 grupos pontuais cristalograficos; deduzidos por Hessel (1830) e por Gadolin (1867)."
    risk: data
    source: "Burke (1966); International Tables vol. A"
    audit: "verificado em 2026-10-04"
  - claim_id: CRI-GP-FAMILIAS-001
    claim: "Familias: 1,2,3,4,6; 1-barra, m, 3-barra, 4-barra, 6-barra; 2/m, 4/m, 6/m; 222, 32, 422, 622; mm2, 3m, 4mm, 6mm; 4-barra 2m, 6-barra m2, 3-barra m; mmm, 4/mmm, 6/mmm; 23, m3-barra, 432, 4-barra 3m, m3-barra m. Total 32."
    risk: numero
    source: "International Tables vol. A"
    audit: "verificado em 2026-10-04"
  - claim_id: CRI-HM-HIST-001
    claim: "A notacao de Hermann-Mauguin foi proposta por Carl Hermann (1928) e Charles-Victor Mauguin (1931) e adotada nas International Tables a partir de 1935."
    risk: data
    source: "Hermann (1928); Mauguin (1931); Internationale Tabellen (1935)"
    audit: "corrigido em 2026-10-04 (🟡: datas precisas, Hermann 1928 e Mauguin 1931)"
  - claim_id: CRI-HM-DIRECOES-001
    claim: "Direcoes das posicoes: tetragonal [001], <100>, <110>; trigonal/hexagonal [001], <100>, <1-10> (hexagonal); ortorrombico x, y, z; cubico <100>, <111>, <110>."
    risk: conceito
    source: "International Tables vol. A"
    audit: "verificado em 2026-10-04"
  - claim_id: CRI-HM-CUBO-001
    claim: "Simbolo completo do cubo: 4/m 3-barra 2/m; curto m3-barra m; reconstroi 3 eixos 4, 4 eixos 3-barra, 6 eixos 2, 9 espelhos e centro."
    risk: conceito
    source: "International Tables vol. A"
    audit: "verificado em 2026-10-04"
  - claim_id: CRI-HM-CURTOS-001
    claim: "mmm = 2/m 2/m 2/m; 4/mmm = 4/m 2/m 2/m; 6/mmm = 6/m 2/m 2/m; no cubico a segunda posicao e sempre 3 ou 3-barra; m indica espelho perpendicular a direcao."
    risk: conceito
    source: "International Tables vol. A"
    audit: "verificado em 2026-10-04"
  - claim_id: CRI-GP-CENTRO-001
    claim: "11 classes centrossimetricas: 1-barra, 2/m, mmm, 4/m, 4/mmm, 3-barra, 3-barra m, 6/m, 6/mmm, m3-barra, m3-barra m; 21 sem centro."
    risk: numero
    source: "International Tables vol. A"
    audit: "verificado em 2026-10-04"
  - claim_id: CRI-GP-PIEZO-001
    claim: "Piezoeletricidade exige ausencia de centro; o quartzo (classe 32) e piezoeletrico."
    risk: conceito
    source: "Klein & Dutrow; Nye"
    audit: "verificado em 2026-10-04"
  - claim_id: CRI-GP-ORDEM6MMM-001
    claim: "A ordem do grupo 6/mmm e 24."
    risk: numero
    source: "International Tables vol. A"
    audit: "verificado em 2026-10-04"
-->
