# Aula 02: Mol, massa molar e estequiometria — quanto reage com quanto

**ID:** geologia-m26-a02
**Módulo:** [[26-quimica-geociencias-modulo|Módulo 26 — Química para geociências: reações, soluções e equilíbrio]]
**Duração estimada:** ~30 min
**Nível:** ensino médio completo, sem geologia prévia (contrato `ensino-medio-sem-geologia-v1`)
**Objetivo:** calcular quantidades de reagentes e produtos usando mol, massa molar e proporção estequiométrica.

## Antes de começar, você precisa saber

- Como escrever e balancear uma equação química, e o que é reagente/produto — [[26-quimica-geociencias-aula-01-reacao-quimica-conservacao-da-massa|aula 01 deste módulo]] (exigido).
- Como ler a tabela periódica e o que é massa atômica — recomendado (não exigido): [[04-cristalografia-quimica-minerais-aula-01-ponte-atomo-eletrons-tabela-periodica|M04, aula 01]].

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **Mol** | A unidade que conta uma quantidade fixa de partículas (átomos, íons ou moléculas) — assim como "dúzia" conta 12 unidades, "mol" conta 6,02 × 10²³. |
| **Número de Avogadro** | O número de partículas em um mol: aproximadamente 6,02 × 10²³. |
| **Massa atômica** | A massa média de um átomo de um elemento, em unidades de massa atômica (u), lida direto na tabela periódica. |
| **Massa molar** | A massa de um mol de uma substância, em gramas por mol (g/mol) — numericamente igual à soma das massas atômicas da fórmula. |
| **Proporção estequiométrica** | A relação de quantas unidades (em mol) de cada substância participam de uma reação, dada pelos coeficientes da equação balanceada. |
| **Reagente limitante** | O reagente que se esgota primeiro numa reação, limitando quanto produto pode se formar. |

## Conteúdo

### Por que precisamos do mol

Átomos são pequenos demais para contar um a um ou pesar um a um — um único grama de ferro tem mais de 10 quintilhões de átomos. Para lidar com números assim, a química usa uma unidade de contagem em massa, do mesmo jeito que o comércio usa "dúzia" para não contar ovo por ovo: o **mol**.

> [!tip] A analogia da dúzia Uma dúzia sempre tem 12 unidades — de ovos, de laranjas ou de parafusos — mas o **peso** de uma dúzia muda completamente conforme o que você está contando. Uma dúzia de ovos pesa bem menos que uma dúzia de melancias. O **mol** funciona igual: sempre conta a mesma quantidade de partículas (6,02 × 10²³, o **número de Avogadro**), mas a massa de um mol muda de substância para substância, porque átomos diferentes têm massas diferentes.

A massa de um mol de uma substância tem nome — **massa molar** — e você a calcula somando as **massas atômicas** dos elementos da fórmula, exatamente como aparecem na tabela periódica. Por exemplo, a massa molar da água (H₂O): 2 átomos de hidrogênio (≈1 g/mol cada) mais 1 átomo de oxigênio (≈16 g/mol) resulta em ≈18 g/mol — ou seja, 18 gramas de água contêm 6,02 × 10²³ moléculas de H₂O.

### Da equação balanceada aos gramas reais

A equação balanceada da aula 01 diz **quantos mols** de cada substância reagem entre si — não quantos gramas. Os coeficientes são uma **proporção estequiométrica**: dizem, por exemplo, que 4 mols de pirita reagem com 15 mols de gás oxigênio. Para transformar isso numa pergunta prática — "quantos quilos de ácido sulfúrico saem de uma tonelada de pirita exposta ao ar?" — é preciso passar por três etapas:

1. **Gramas → mols** do reagente que você conhece, dividindo a massa pela massa molar.
2. **Mols → mols** do produto de interesse, usando a proporção dos coeficientes da equação balanceada.
3. **Mols → gramas** do produto, multiplicando pela massa molar dele.

Esse caminho de três passos é o coração da **estequiometria**: a parte da química que calcula quanto reage com quanto.

### O reagente limitante: quem manda na conta

Numa reação real, os reagentes raramente estão presentes na proporção exata da equação balanceada. Se você tem pirita em excesso mas pouco oxigênio disponível (situação comum em rejeitos de mina cobertos, com acesso limitado de ar), o **oxigênio** é quem determina quanto produto pode se formar — ele é o **reagente limitante**, mesmo havendo pirita sobrando. É por isso que cobrir rejeitos de mina com água ou solo, cortando o acesso ao O₂, é uma estratégia real de controle de drenagem ácida: ela transforma o oxigênio em reagente limitante e trava a reação.

## Exemplo trabalhado

**Situação:** um depósito de rejeito de mineração expõe 100 kg de pirita (FeS₂) ao ar e à água. Usando a equação balanceada da aula 01,

$$4\,\text{FeS}_2 + 15\,\text{O}_2 + 8\,\text{H}_2\text{O} \rightarrow 2\,\text{Fe}_2\text{O}_3 + 8\,\text{H}_2\text{SO}_4$$

quantos quilogramas de ácido sulfúrico (H₂SO₄) essa massa de pirita pode gerar, se o oxigênio e a água estiverem disponíveis em excesso (ou seja, a pirita é o reagente limitante)?

**Passo 1 — massa molar da pirita (FeS₂).** Fe ≈ 56 g/mol; S ≈ 32 g/mol cada, e há 2 enxofres: 56 + (2 × 32) = 56 + 64 = **120 g/mol**.

**Passo 2 — gramas para mols de pirita.** 100 kg = 100.000 g.

$$\frac{100.000\ \text{g}}{120\ \text{g/mol}} \approx 833\ \text{mol de FeS}_2$$

**Passo 3 — proporção estequiométrica.** A equação diz que 4 mol de FeS₂ produzem 8 mol de H₂SO₄ — uma proporção de 1 para 2. Logo:

$$833\ \text{mol de FeS}_2 \times \frac{8\ \text{mol H}_2\text{SO}_4}{4\ \text{mol FeS}_2} = 1.666\ \text{mol de H}_2\text{SO}_4$$

**Passo 4 — massa molar do ácido sulfúrico (H₂SO₄).** H: 2 × 1 = 2; S: 32; O: 4 × 16 = 64. Total: 2 + 32 + 64 = **98 g/mol**.

**Passo 5 — mols para gramas.**

$$1.666\ \text{mol} \times 98\ \text{g/mol} \approx 163.000\ \text{g} \approx 163\ \text{kg de H}_2\text{SO}_4$$

**A lição:** 100 kg de pirita oxidada, em condições favoráveis, podem gerar da ordem de 160 kg de ácido sulfúrico — mais massa de ácido do que a massa original de pirita, porque o oxigênio e a água do ambiente entram na conta como reagentes. É exatamente esse tipo de cálculo que orienta o dimensionamento de sistemas de neutralização em minas com potencial de drenagem ácida.

## Erros comuns

- **Usar a massa da substância diretamente na proporção da equação balanceada.** Os coeficientes da equação são uma razão de **mols**, não de gramas — é obrigatório converter para mol antes de aplicar a proporção, e converter de volta para grama só no final.
- **Esquecer de multiplicar a massa atômica pelo número de átomos do elemento na fórmula.** Na pirita, o enxofre aparece 2 vezes (FeS₂) — usar só 32 g/mol de enxofre, em vez de 64, é o erro mais comum nesse tipo de conta.
- **Assumir que o reagente que sobra em maior massa (ou volume) é sempre o reagente em excesso.** O que decide é a proporção estequiométrica, não a quantidade absoluta — um reagente pode estar presente em grande massa e ainda assim ser o limitante, dependendo do quanto a reação exige dele.
- **Confundir "mol" com "molécula".** Um mol **é uma quantidade** de moléculas (ou átomos, ou íons) — 6,02 × 10²³ delas —, não uma molécula específica.

## O que não concluir

- **Que todo o oxigênio e toda a água de um ambiente real estão sempre "disponíveis em excesso".** O exemplo trabalhado assumiu essa condição para isolar o cálculo estequiométrico; em campo, o próprio oxigênio costuma ser o fator limitante, como discutido na seção sobre reagente limitante.
- **Que o cálculo estequiométrico prevê a velocidade da reação.** Ele diz **quanto** produto se forma se a reação for completa, não **em quanto tempo** isso acontece — pirita exposta pode levar anos para oxidar por completo.

## Recap relâmpago

- O **mol** é uma unidade de contagem (6,02 × 10²³ partículas, o número de Avogadro), do mesmo jeito que "dúzia" conta 12 — mas a massa de um mol muda conforme a substância.
- A **massa molar** (g/mol) é a soma das massas atômicas da fórmula, e converte entre massa (gramas, o que se mede) e quantidade de partículas (mols, o que a equação balanceada usa).
- O caminho de cálculo em estequiometria é sempre: **gramas → mols → (proporção da equação) → mols → gramas**.
- O **reagente limitante** é quem determina quanto produto se forma, mesmo que outro reagente esteja presente em grande quantidade — controlar o acesso ao reagente limitante (como o O₂ em rejeitos de mina) é uma estratégia real de controle de reação em geologia aplicada.

## Próxima aula

[[26-quimica-geociencias-aula-03-solucoes-concentracao-ph|Aula 03 — Soluções, concentração e pH: a água como reagente geológico]]

## Anterior

[[26-quimica-geociencias-aula-01-reacao-quimica-conservacao-da-massa|Aula 01 — Reação química e conservação da massa]]

## Fontes

- Conceito de mol, número de Avogadro e massa molar: química geral básica.
- Estequiometria da oxidação da pirita e reagente limitante em drenagem ácida de mina: geoquímica ambiental de minas sulfetadas (literatura consolidada de AMD/DAM); controle por exclusão de oxigênio como estratégia de mitigação.

<!--
nivel: ensino-medio-sem-geologia-v1
palavras_corpo: ~1350
bridge_lesson: false

mapa_objetivo_secao:
  OA-02: "Por que precisamos do mol" + "Da equação balanceada aos gramas reais" + "O reagente limitante: quem manda na conta" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEO-M26-A02-MOL-AVOGADRO-001
    claim: "Um mol corresponde a aproximadamente 6,02 x 10^23 partículas (número de Avogadro)."
    risk: fato
    source: "química geral básica (constante de Avogadro, CODATA)"
  - claim_id: GEO-M26-A02-MASSA-MOLAR-PIRITA-002
    claim: "A massa molar da pirita (FeS2) é aproximadamente 120 g/mol (Fe ~56 + 2 x S ~32)."
    risk: fato
    source: "massas atômicas da tabela periódica (IUPAC)"
  - claim_id: GEO-M26-A02-MASSA-MOLAR-H2SO4-003
    claim: "A massa molar do ácido sulfúrico (H2SO4) é aproximadamente 98 g/mol."
    risk: fato
    source: "massas atômicas da tabela periódica (IUPAC)"
  - claim_id: GEO-M26-A02-REAGENTE-LIMITANTE-DAM-004
    claim: "Cobrir rejeitos de mineração sulfetada com água ou solo, restringindo o acesso ao oxigênio, é uma estratégia real de mitigação de drenagem ácida de mina, tornando o oxigênio o reagente limitante da oxidação da pirita."
    risk: interpretacao
    source: "literatura de geoquímica ambiental e engenharia de minas sobre controle de drenagem ácida (AMD/DAM)"
  - claim_id: GEO-M26-A02-CALCULO-ESTEQUIOMETRICO-005
    claim: "A partir da equação balanceada 4 FeS2 + 15 O2 + 8 H2O -> 2 Fe2O3 + 8 H2SO4, 100 kg de pirita produzem, em condições de reagentes O2/H2O em excesso, da ordem de 160 kg de H2SO4."
    risk: fato
    source: "cálculo estequiométrico direto a partir da equação balanceada e das massas molares"

nota_trilha_apoio: >-
  Aula 2 de 5 do módulo 26 (trilha de apoio, opcional, não bloqueante), criada em
  2026-08-19. Depende diretamente da aula 01 deste módulo (equação balanceada da
  pirita), reutilizada aqui para dar contexto quantitativo.
-->
