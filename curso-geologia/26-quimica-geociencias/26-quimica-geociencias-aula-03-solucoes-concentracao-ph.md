# Aula 03: Soluções, concentração e pH — a água como reagente geológico

**ID:** geologia-m26-a03
**Módulo:** [[26-quimica-geociencias-modulo|Módulo 26 — Química para geociências: reações, soluções e equilíbrio]]
**Duração estimada:** ~30 min
**Nível:** ensino médio completo, sem geologia prévia (contrato `ensino-medio-sem-geologia-v1`)
**Objetivo:** expressar e converter concentrações de soluções (molaridade, ppm, ppb) e interpretar a escala de pH.

## Antes de começar, você precisa saber

- O que é mol e massa molar — [[26-quimica-geociencias-aula-02-mol-massa-molar-estequiometria|aula 02 deste módulo]] (exigido).
- Que a água pode se comportar como reagente numa reação (visto na aula 01, com o feldspato) — recomendado.

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **Solução** | Uma mistura homogênea (uniforme, sem partes visíveis diferentes) de uma substância dissolvida (o soluto) em outra (o solvente). |
| **Soluto** | A substância presente em menor quantidade numa solução, que se dissolve. |
| **Solvente** | A substância presente em maior quantidade, que dissolve o soluto — na maioria das águas naturais, a própria água. |
| **Concentração** | A quantidade de soluto presente numa certa quantidade de solução. |
| **Molaridade (mol/L)** | Uma forma de concentração: quantos mols de soluto existem em 1 litro de solução. |
| **ppm / ppb** | "Partes por milhão" e "partes por bilhão": quantas unidades de massa de soluto existem em um milhão (ou bilhão) de unidades de massa de solução — usadas para concentrações muito baixas, como as de águas naturais. |
| **pH** | Uma escala de 0 a 14 que mede o quão ácida ou básica é uma solução, a partir da concentração de íons hidrogênio (H⁺). |
| **Ácido / base** | Substância que, em água, libera H⁺ em excesso (ácido) ou reduz a concentração de H⁺ em favor de OH⁻ (base). |

## Conteúdo

### A água quase nunca está sozinha

Quando você bebe "água pura", está na verdade bebendo uma **solução**: água (o **solvente**) com pequenas quantidades de sais, gases e outras substâncias dissolvidas (os **solutos**). Na natureza, isso é ainda mais verdadeiro — a água da chuva dissolve gás carbônico do ar; a água subterrânea dissolve íons dos minerais que atravessa; a água do mar carrega sódio, cloro, magnésio e dezenas de outros elementos. Entender **quanto** de cada soluto está dissolvido — a **concentração** — é o que permite prever se aquela água vai dissolver mais rocha, precipitar mineral novo, ou estar apta para consumo.

### Três formas de medir concentração

A concentração pode ser expressa de formas diferentes, dependendo da escala do que está sendo medido:

- **Molaridade (mol/L):** quantos mols de soluto há em 1 litro de solução. É a forma mais direta de ligar concentração à estequiometria da aula 02, porque entra em cálculo de reação já em mols.
- **ppm (partes por milhão):** quantas unidades de massa de soluto existem em um milhão de unidades de massa de solução — equivalente, na prática, a miligramas de soluto por litro de água (mg/L), para soluções diluídas em água. Usada para águas naturais, porque as concentrações reais costumam ser baixas.
- **ppb (partes por bilhão):** mil vezes mais diluído que ppm — usada para traços ainda menores, como certos metais pesados em água potável.

> [!tip] Uma analogia Pense em concentração como "quantas gotas de suco de limão você pôs num copo de água": molaridade conta em "colheres de soluto por litro"; ppm conta em algo como "uma gota de limão em uma piscina inteira" — a mesma ideia de proporção, só em escalas bem diferentes.

Converter entre elas usa a massa molar, exatamente como na aula 02. Por exemplo, uma água com 40 ppm de cálcio (Ca²⁺, massa molar ≈ 40 g/mol) tem 40 mg de Ca²⁺ por litro de água — o que equivale a 0,040 g/L, ou

$$\frac{0{,}040\ \text{g/L}}{40\ \text{g/mol}} = 0{,}001\ \text{mol/L} = 1\ \text{mmol/L de Ca}^{2+}$$

### A escala de pH: medindo o quanto uma água "ataca" rocha

Nem toda molécula de água se comporta igual: uma pequena fração dela se rompe espontaneamente, liberando um íon hidrogênio (H⁺) e um íon hidroxila (OH⁻). Quanto mais H⁺ livre numa solução, mais **ácida** ela é; quanto menos H⁺ livre (e mais OH⁻), mais **básica**. O **pH** é a escala que resume isso num único número, de 0 (muito ácido) a 14 (muito básico), com 7 sendo neutro — a água pura.

A escala de pH é **logarítmica**: cada unidade de pH representa uma mudança de 10 vezes na concentração de H⁺. Uma água de pH 4 tem 10 vezes mais H⁺ que uma de pH 5, e 100 vezes mais que uma de pH 6. É por isso que uma pequena queda no pH de uma água de mina — de 5 para 3, por exemplo — representa um aumento de **cem vezes** na acidez real, não apenas "um pouco mais ácida".

A água da chuva, mesmo longe de qualquer poluição, já nasce levemente ácida (pH próximo de 5,6), porque dissolve CO₂ do ar e forma ácido carbônico — o mesmo processo que fornece o H⁺ que ataca o feldspato na reação da aula 01, e que você vai reencontrar, com o foco no equilíbrio, na aula 04. Já a drenagem ácida de mina gerada pela oxidação da pirita (aulas 01 e 02) pode chegar a pH abaixo de 3 — água ácida o bastante para dissolver metais de rochas ao redor e ser tóxica para a vida aquática.

## Exemplo trabalhado

**Situação:** uma amostra de água subterrânea tem concentração de íons H⁺ igual a 1 × 10⁻⁶ mol/L. Qual o pH dessa água, e ela é ácida, neutra ou básica?

**Passo 1 — a definição de pH.** O pH é o **logaritmo negativo** da concentração de H⁺ em mol/L:

$$\text{pH} = -\log_{10}[\text{H}^+]$$

**Passo 2 — aplicar o valor dado.**

$$\text{pH} = -\log_{10}(1 \times 10^{-6}) = -(-6) = 6$$

**Passo 3 — interpretar.** pH 6 está abaixo de 7 (neutro), então essa água é **levemente ácida** — consistente com uma água que dissolveu um pouco de CO₂ do solo, um caso comum e não motivo de alarme.

**Comparando com um segundo cenário:** uma água de drenagem de mina tem concentração de H⁺ igual a 1 × 10⁻³ mol/L. O pH dessa água é:

$$\text{pH} = -\log_{10}(1 \times 10^{-3}) = 3$$

**A lição:** a diferença entre pH 6 e pH 3 parece pequena em números (só 3 unidades), mas representa uma concentração de H⁺ **mil vezes maior** (10³, porque 3 unidades de pH = 3 potências de 10) — é essa natureza logarítmica que faz da drenagem ácida de mina uma água quimicamente muito mais agressiva do que a diferença de "3 pontos" sugere à primeira vista.

## Erros comuns

- **Achar que pH mede "quanto ácido tem dissolvido" em termos absolutos.** pH mede a concentração de H⁺ **livre**, não a quantidade total de substância ácida — um ácido fraco em alta concentração pode ter pH parecido com um ácido forte em baixa concentração.
- **Tratar a escala de pH como linear.** Uma diferença de 1 unidade de pH é uma diferença de **10 vezes** na concentração de H⁺, não de "10%" nem de "1 unidade de acidez".
- **Confundir ppm com porcentagem.** 1% equivale a 10.000 ppm — são escalas diferentes por um fator de dez mil; usar ppm onde a conta pede porcentagem (ou vice-versa) erra por ordens de grandeza.
- **Achar que água da chuva "pura" (sem poluição) deveria ter pH exatamente 7.** Ela já nasce naturalmente ácida (pH ≈ 5,6) por dissolver CO₂ atmosférico — isso é esperado, e é a chuva ácida por **poluição** (pH bem mais baixo que 5,6, geralmente por óxidos de enxofre e nitrogênio) que é o problema ambiental.

## O que não concluir

- **Que toda água ácida é necessariamente poluída ou perigosa.** A acidez natural da chuva e de muitas águas subterrâneas é parte normal do ciclo geoquímico — o que importa é o **valor** de pH e a **origem** da acidez, não a simples presença de H⁺.
- **Que ppm e molaridade são sempre diretamente intercambiáveis sem conversão.** A equivalência "ppm ≈ mg/L" usada nesta aula vale para soluções aquosas diluídas, onde a densidade da solução é próxima de 1 g/mL; em soluções muito concentradas essa aproximação deixa de ser precisa.

## Recap relâmpago

- Uma **solução** é uma mistura homogênea de soluto em solvente; **concentração** mede quanto soluto há numa dada quantidade de solução.
- **Molaridade** (mol/L) liga a concentração à estequiometria; **ppm/ppb** são usados para as concentrações baixas típicas de águas naturais.
- **pH** mede a concentração de H⁺ numa escala **logarítmica** de 0 a 14: cada unidade representa uma mudança de 10 vezes na acidez real.
- A água da chuva já nasce levemente ácida (pH ≈ 5,6) por dissolver CO₂; a drenagem ácida de mina, pela oxidação da pirita, pode chegar a pH abaixo de 3.
- Essas ferramentas — solução, concentração, pH — são a base direta para a hidrogeoquímica e a contaminação de águas subterrâneas, tratadas no curso avançado irmão (`../curso-geologia-avancado/`, módulos 02 e 03).

## Próxima aula

[[26-quimica-geociencias-aula-04-equilibrio-quimico-solubilidade|Aula 04 — Equilíbrio químico e solubilidade: o sistema carbonato]]

## Anterior

[[26-quimica-geociencias-aula-02-mol-massa-molar-estequiometria|Aula 02 — Mol, massa molar e estequiometria]]

## Fontes

- Conceitos de solução, concentração, molaridade e ppm/ppb: química geral básica.
- Escala de pH, natureza logarítmica e pH natural da água de chuva (≈5,6 por dissolução de CO₂ atmosférico): química ambiental básica.
- pH de drenagem ácida de mina e sua origem na oxidação de sulfetos: geoquímica ambiental (literatura consolidada de AMD/DAM).

<!--
nivel: ensino-medio-sem-geologia-v1
palavras_corpo: ~1400
bridge_lesson: false

mapa_objetivo_secao:
  OA-03: "A água quase nunca está sozinha" + "Três formas de medir concentração" + "A escala de pH: medindo o quanto uma água 'ataca' rocha" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEO-M26-A03-PH-DEFINICAO-001
    claim: "pH é definido como o logaritmo negativo (base 10) da concentração molar de íons H+ em solução: pH = -log10[H+]."
    risk: fato
    source: "química geral básica (definição de Sørensen)"
  - claim_id: GEO-M26-A03-PH-LOGARITMICO-002
    claim: "A escala de pH é logarítmica: cada unidade de diferença de pH corresponde a uma mudança de 10 vezes na concentração de H+."
    risk: fato
    source: "química geral básica"
  - claim_id: GEO-M26-A03-CHUVA-PH-NATURAL-003
    claim: "A água da chuva não poluída tem pH naturalmente ácido, próximo de 5,6, por dissolver CO2 atmosférico e formar ácido carbônico."
    risk: fato
    source: "química ambiental / ciência atmosférica consolidada (valor de referência amplamente citado, ~5,6)"
  - claim_id: GEO-M26-A03-DAM-PH-004
    claim: "A drenagem ácida de mina, associada à oxidação de sulfetos como a pirita, pode atingir valores de pH abaixo de 3."
    risk: fato
    source: "literatura consolidada de geoquímica ambiental de drenagem ácida de mina (AMD/DAM)"
  - claim_id: GEO-M26-A03-PPM-PORCENTAGEM-005
    claim: "1% em massa equivale a 10.000 ppm."
    risk: fato
    source: "definição matemática direta de ppm (partes por milhão)"

nota_trilha_apoio: >-
  Aula 3 de 5 do módulo 26 (trilha de apoio, opcional, não bloqueante), criada em
  2026-08-19. É a aula deste módulo com maior valor de preparo para a
  hidrogeoquímica e a contaminação de águas subterrâneas, hoje no curso avançado
  irmão, conforme registrado na tabela "Quando estudar" de _contexto.md.
-->
