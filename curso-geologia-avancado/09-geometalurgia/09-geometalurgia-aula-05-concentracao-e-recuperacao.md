# Aula 05: Concentração: gravítica, magnética, flotação e lixiviação; recuperação metalúrgica

**ID:** geologia-avancado-m09-a05
**Módulo:** [[09-geometalurgia-modulo|Módulo 09 — Geometalurgia]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** descrever as rotas de concentração — gravítica (critério de concentração), magnética (baixa e alta intensidade), flotação (coletor, espumante, modificadores, hidrofobicidade, contato trifásico, cinética, curva teor-recuperação) e lixiviação (pilha, tanque, pressão, cianetação, biolixiviação) — e fechar o balanço metalúrgico pela fórmula de dois produtos, calculando recuperação, razão de enriquecimento e razão de concentração a partir dos teores.

**Pré-requisito:** nenhum módulo deste curso. Da Aula 02: partição do metal, minerais de ganga problemáticos, propriedades físicas relevantes. Da Aula 03: liberação, curva teor-recuperação.

## Antes de começar, você precisa saber

- Que a partição do metal fixa o teto de recuperação de cada rota: só se recupera o metal que está num mineral que a rota consegue separar ou dissolver (Aula 02).
- Que a **curva teor-recuperação** relaciona inversamente o teor do concentrado e a recuperação, para um dado minério e uma dada moagem (Aula 03).
- Balanço de massa: em regime permanente, a massa (e a massa de cada elemento) que entra numa unidade é igual à que sai.

## Conteúdo

### O princípio comum

Toda concentração explora uma propriedade em que o mineral-minério difere da ganga: **densidade** (gravítica), **susceptibilidade magnética** (magnética), condutividade elétrica, cor ou resposta a sensores, ou **química de superfície** (flotação). A **lixiviação** foge à lógica de separação física: dissolve quimicamente o metal e deixa o sólido para trás.

### Separação gravítica

Baseia-se na diferença de densidade e no comportamento diferencial das partículas num fluido em movimento. A viabilidade se estima pelo **critério de concentração**:

`CC = (ρ_pesado − ρ_fluido) / (ρ_leve − ρ_fluido)`

A regra prática consagrada (Taggart, reproduzida em Wills & Finch) associa a cada faixa de `CC` o **tamanho mínimo de partícula** em que a separação ainda funciona — e é esse par, e não o `CC` sozinho, que decide a viabilidade:

| `CC` | Separação viável até | Leitura |
|---|---|---|
| `> 2,5` | ~75 µm | fácil, inclusive em granulometria fina |
| `1,75 – 2,50` | ~150 µm | viável, mas já exige controle de finos |
| `1,50 – 1,75` | ~1,7 mm | difícil, só material grosso |
| `1,25 – 1,50` | ~6,35 mm | só em fragmentos, tipicamente pré-concentração |
| `< 1,25` | — | comercialmente inviável em qualquer tamanho |

O padrão é claro: **quanto menor o `CC`, mais grossa precisa ser a partícula** para que a diferença de densidade vença o arraste do fluido.

Equipamentos: jigues, calhas e espirais, mesas vibratórias, concentradores centrífugos (Knelson, Falcon), separação em meio denso. Aplicações típicas: ouro livre, cassiterita, cromita, minério de tungstênio, minério de ferro, carvão e pré-concentração.

### Separação magnética

- **Baixa intensidade (LIMS)** — tambores de ~0,1–0,4 T na superfície; separa os minerais **fortemente magnéticos**, sobretudo magnetita e pirrotita monoclínica, e recupera o meio denso. A literatura de processamento chama esse grupo de "ferromagnético" em sentido amplo; a rigor, magnetita e pirrotita monoclínica são **ferrimagnéticas** (subredes magnéticas antiparalelas e desiguais, momento líquido não nulo) — distinção que importa quando a mesma propriedade for lida ao microscópio de minérios ou em magnetismo de rochas.
- **Alta intensidade e alto gradiente (WHIMS, HGMS)** — campos de 1–2 T ou mais; separa minerais **paramagnéticos** fracos (hematita, ilmenita, wolframita, monazita, granada) ou remove ganga paramagnética de um concentrado (limpeza de concentrados de minerais industriais e de terras raras).

### Flotação

É a rota mais versátil e a mais usada para sulfetos e para muitos minerais industriais. Explora a **hidrofobicidade** da superfície: numa polpa aerada, partículas hidrofóbicas aderem a bolhas de ar e sobem à espuma, enquanto as hidrofílicas permanecem na polpa.

Reagentes:

- **Coletor** — molécula anfifílica (xantatos, ditiofosfatos para sulfetos; ácidos graxos, aminas para não sulfetos) que adsorve seletivamente na superfície do mineral-alvo, deixando a cauda apolar exposta e tornando-a hidrofóbica.
- **Espumante** — tensoativo (MIBC, glicóis) que estabiliza as bolhas e a espuma, sem alterar a hidrofobicidade das partículas. Coletor e espumante têm funções distintas.
- **Modificadores** — **depressor** torna um mineral hidrofílico (cal deprime pirita; cianeto deprime esfalerita e pirita; carboximetilcelulose e quebracho deprimem talco e silicatos); **ativador** prepara a superfície (sulfato de cobre ativa a esfalerita para o xantato); **regulador de pH** (cal, ácido) controla a seletividade.

Física: o **contato trifásico** sólido–líquido–gás forma-se quando o filme de água entre a bolha e a partícula se rompe; a firmeza da adesão cresce com o **ângulo de contato**, que o coletor aumenta. Há uma janela de tamanho útil: partículas grossas (acima de ~150–300 µm) descolam da bolha por peso; ultrafinas (abaixo de ~10 µm) colidem pouco com as bolhas — as duas pontas flotam mal.

**Cinética:** a recuperação em função do tempo de flotação segue aproximadamente uma lei de primeira ordem:

`R(t) = R_∞ · (1 − e^(−k·t))`

com `R_∞` a recuperação máxima (limitada por liberação e mineralogia) e `k` a constante de taxa (depende de reagente, granulometria e hidrodinâmica). Minerais liberados têm `k` alto; partículas mistas, `k` baixo.

**Circuito:** *rougher* (desbaste, recupera o grosso da massa), *scavenger* (recupera o que escapou do rougher) e *cleaner* (limpa o concentrado rougher, elevando o teor). Usam-se células mecânicas e colunas.

**Curva teor-recuperação:** a Aula 03 já mostrou a curva e a diferença entre andar sobre ela e trocar de curva. O que a flotação acrescenta é **quem move o ponto de operação na prática**: mais tempo, mais estágios de recuperação e menos limpeza empurram para mais recuperação e menor teor; mais limpeza, para o lado oposto. E acrescenta o **critério de escolha**, que é econômico, não técnico: penalidades por baixo teor e por contaminantes de um lado, valor do metal perdido no rejeito do outro. É por isso que duas plantas com o mesmo minério podem operar deliberadamente em pontos diferentes da mesma curva.

### Lixiviação

Dissolução química seletiva do metal:

- **Em pilha (*heap*)** — minério britado empilhado, solução aplicada por gotejamento; barata, para baixo teor: cobre oxidado e sulfetos secundários com ácido sulfúrico (seguidos de extração por solventes e eletrólise), ouro com solução cianetada diluída.
- **Agitada em tanque** — minério moído, em reatores; teores maiores e cinética mais rápida: cianetação de ouro (CIL, CIP), zinco, urânio.
- **Sob pressão (autoclave, POX)** — temperatura e pressão de oxigênio elevadas para oxidar sulfetos: níquel laterítico (HPAL), ouro refratário, concentrados de cobre.
- **Cianetação do ouro** (equação de Elsner): `4 Au + 8 NaCN + O₂ + 2 H₂O → 4 Na[Au(CN)₂] + 4 NaOH`.
- **Biolixiviação** — micro-organismos acidófilos (do gênero *Acidithiobacillus* e afins) aceleram a oxidação de sulfetos: pilhas de calcosita, pré-tratamento de concentrados de ouro refratário.

**Ouro refratário** é ouro submicroscópico encapsulado em pirita ou arsenopirita, inacessível ao cianeto sem oxidação prévia, ou minério *preg-robbing*, em que carbono natural readsorve o ouro já dissolvido. É um diagnóstico de mineralogia de processo (Aula 02) com forte impacto no fluxograma.

### O balanço metalúrgico e a fórmula de dois produtos

Considere uma unidade que separa a alimentação em **concentrado** e **rejeito**. Sejam `F, C, T` as massas e `f, c, t` os teores do metal em cada corrente. Em regime permanente:

`F = C + T`  (balanço de massa)
`F·f = C·c + T·t`  (balanço do metal)

Resolvendo para a **recuperação** `R = C·c / (F·f)` sem medir as massas — só com os três teores:

`R = [c · (f − t)] / [f · (c − t)] × 100 %`  ← fórmula de dois produtos

Grandezas associadas:

- **Razão de enriquecimento** = `c / f` (quantas vezes o concentrado é mais rico que a alimentação).
- **Razão de concentração** `K = F / C = (c − t) / (f − t)` (toneladas de minério por tonelada de concentrado).

A força da fórmula: numa planta em operação, amostrar o teor das correntes é fácil e contínuo; pesar todas as correntes de polpa é difícil. Os três teores bastam para fechar o balanço e acompanhar a recuperação em tempo real.

## Exemplo trabalhado

**Situação:** uma usina de flotação de cobre amostra as três correntes: alimentação `f = 0,85 % Cu`, concentrado `c = 27,5 % Cu`, rejeito `t = 0,072 % Cu`.

**Recuperação (fórmula de dois produtos):**
`R = [27,5 × (0,85 − 0,072)] / [0,85 × (27,5 − 0,072)]`
`R = (27,5 × 0,778) / (0,85 × 27,428)`
`R = 21,395 / 23,314 = 0,9177 → 91,8 %`

**Razão de concentração:**
`K = (27,5 − 0,072) / (0,85 − 0,072) = 27,428 / 0,778 = 35,3`
→ processam-se 35,3 t de minério por tonelada de concentrado.

**Razão de enriquecimento:**
`27,5 / 0,85 = 32,4`

**Verificação por balanço** (base 1 000 t de alimentação):
`Cu na alimentação = 1 000 × 0,0085 = 8,50 t`
`Massa de concentrado = 1 000 / 35,3 = 28,3 t → Cu = 28,3 × 0,275 = 7,79 t`
`Massa de rejeito = 971,7 t → Cu = 971,7 × 0,00072 = 0,70 t`
`Soma: 7,79 + 0,70 = 8,49 t ≈ 8,50 t` (fecha, a menos do arredondamento das massas)

**Interpretação:** com o rejeito a 0,072 % Cu, 8,2 % do cobre alimentado sai pela barragem de rejeitos. Se um ajuste de reagente ou de moagem baixasse o rejeito para 0,050 % Cu, a recuperação subiria para ~94,3 % — 2,5 pontos, ou ~0,21 t de Cu por 1 000 t de minério, que a US$ 8 500/t valem cerca de US$ 1 800 por 1 000 t. Numa planta de 30 000 t/dia, são da ordem de US$ 54 mil por dia. É esse cálculo, repetido, que orienta a operação sobre a curva teor-recuperação.

## Erros comuns

- **Usar a fórmula de dois produtos quando há mais de dois produtos com o metal** (circuito Cu-Pb-Zn) — aí é a fórmula de três produtos, com dois metais medidos.
- **Confundir razão de enriquecimento (`c/f`) com razão de concentração (`F/C`).**
- **Reportar recuperação sem dizer de que metal e em que ponto da curva teor-recuperação.**
- **Achar que a separação gravítica serve para qualquer minério** — o critério de concentração manda, e ele nunca se lê sozinho: vem sempre com um tamanho mínimo de partícula. `CC < 1,5` é caso perdido para finos, e `CC < 1,25` é caso perdido em qualquer tamanho.
- **Trocar as funções de coletor e espumante** — o espumante não coleta, o coletor não faz espuma.
- **Tratar ouro refratário como problema de reagente** — é encapsulamento mineralógico e exige oxidação (POX, biolixiviação, ustulação).
- **Assumir que elevar o teor do concentrado é de graça** — anda-se para trás na curva, perdendo recuperação.

## O que não concluir

- **Que recuperação de 100 % é a meta** — a curva teor-recuperação e as penalidades comerciais definem um ótimo econômico abaixo disso.
- **Que a fórmula de dois produtos precisa das vazões** — precisa só dos três teores; essa é a razão de usá-la.
- **Que lixiviação é sempre mais barata que flotação** — depende de teor, de mineralogia (óxido × sulfeto, refratariedade) e do consumo de ácido ou de cianeto da ganga.
- **Que a mesma rota serve para todo o depósito** — a zona oxidada pode pedir lixiviação e a primária, flotação, no mesmo corpo (Aula 06).

## Recap relâmpago

- Toda **concentração** explora uma propriedade diferencial: densidade (gravítica; **critério de concentração** `CC = (ρ_p − ρ_f)/(ρ_l − ρ_f)` — cada faixa de `CC` vem com o tamanho mínimo de partícula: > 2,5 até ~75 µm, 1,75–2,5 até ~150 µm, 1,5–1,75 até ~1,7 mm, 1,25–1,5 até ~6,35 mm, < 1,25 inviável), susceptibilidade magnética (LIMS para magnetita e pirrotita monoclínica — fortemente magnéticas, a rigor ferrimagnéticas; WHIMS/HGMS para paramagnéticos) ou química de superfície (flotação).
- **Flotação:** o **coletor** torna o mineral-alvo hidrofóbico, o **espumante** estabiliza as bolhas, **depressores e ativadores** dão seletividade; a adesão bolha–partícula é o **contato trifásico**, e a recuperação no tempo segue `R(t) = R_∞ (1 − e^(−kt))`.
- A **curva teor-recuperação** é inversa: mais recuperação custa menor teor; o ponto de operação é escolhido pelo valor.
- **Lixiviação** dissolve o metal: pilha (baixo teor), tanque agitado, pressão (autoclave); **cianetação** para ouro, **biolixiviação** para sulfetos; **ouro refratário** é encapsulamento mineralógico, não falha de reagente.
- O **balanço metalúrgico** fecha pela **fórmula de dois produtos** `R = c(f − t) / [f(c − t)]`, mais a **razão de enriquecimento** `c/f` e a **razão de concentração** `(c − t)/(f − t)` — tudo a partir dos três teores, sem pesar as correntes.
- No exemplo (f 0,85 %, c 27,5 %, t 0,072 % Cu): R ≈ 91,8 %, K ≈ 35, enriquecimento ≈ 32.

## Próxima aula

[[09-geometalurgia-aula-06-dominios-e-modelagem-da-variabilidade|Aula 06 — Domínios geometalúrgicos e modelagem da variabilidade: variáveis proxy e valor do projeto]]

## Anterior

[[09-geometalurgia-aula-04-cominuicao-e-moabilidade|Aula 04 — Cominuição: britagem, moagem e índices de moabilidade]]

## Fontes

- Wills, B. A. & Finch, J. A. (2016), *Wills' Mineral Processing Technology*, 8ª ed., Butterworth-Heinemann, cap. 10 (gravítica), 12 (flotação), 13 (magnética e elétrica), 15 (hidrometalurgia).
- Bulatovic, S. M. (2007), *Handbook of Flotation Reagents: Chemistry, Theory and Practice*, vol. 1, Elsevier, cap. 1–5.
- Marsden, J. O. & House, C. I. (2006), *The Chemistry of Gold Extraction*, 2ª ed., SME, cap. 5 e 10.
- Gupta, C. K. (2003), *Chemical Metallurgy: Principles and Practice*, Wiley-VCH, cap. 6.
- Napier-Munn, T. J., Morrell, S., Morrison, R. D. & Kojovic, T. (1996), *Mineral Comminution Circuits: Their Operation and Optimisation*, JKMRC, cap. 4 (balanço de massa e reconciliação).

<!--
nivel: avancado
palavras_corpo: ~1810
mapa_objetivo_secao:
  geologia-avancado-m09-oa03: "O princípio comum" + "Separação gravítica" + "Separação magnética" + "Flotação" + "Lixiviação" + "O balanço metalúrgico e a fórmula de dois produtos" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOMET-M09-A05-CC-001
    claim: "A separação gravítica explora a diferença de densidade; sua viabilidade estima-se pelo critério de concentração CC = (ρ_pesado − ρ_fluido)/(ρ_leve − ρ_fluido), lido sempre em par com o tamanho mínimo de partícula: CC > 2,5 viável até ~75 µm; 1,75–2,50 até ~150 µm; 1,50–1,75 até ~1,7 mm; 1,25–1,50 até ~6,35 mm; CC < 1,25 comercialmente inviável em qualquer tamanho."
    risk: fato
    source: "Taggart, Handbook of Mineral Dressing, reproduzido em Wills & Finch 2016, cap. 10 (concentration criterion)"
  - claim_id: GEOMET-M09-A05-MAGNETICA-002
    claim: "A separação magnética de baixa intensidade (LIMS, ~0,1–0,4 T na superfície do tambor) separa os minerais fortemente magnéticos, sobretudo magnetita e pirrotita monoclínica — que a literatura de processamento chama de ferromagnéticos em sentido amplo, mas que a rigor são ferrimagnéticos; a de alta intensidade e alto gradiente (WHIMS/HGMS, 1–2 T ou mais) separa minerais paramagnéticos fracos como hematita, ilmenita, wolframita, monazita e granada, ou remove ganga paramagnética de concentrados."
    risk: fato
    source: "Wills & Finch 2016, cap. 13; literatura de magnetismo mineral quanto à distinção ferro/ferrimagnetismo da magnetita"
  - claim_id: GEOMET-M09-A05-FLOTACAO-REAGENTES-003
    claim: "Na flotação, o coletor é uma molécula anfifílica que adsorve seletivamente no mineral-alvo tornando-o hidrofóbico; o espumante estabiliza as bolhas sem afetar a hidrofobicidade; depressores tornam um mineral hidrofílico (cal deprime pirita, cianeto deprime esfalerita e pirita, CMC e quebracho deprimem talco), ativadores preparam a superfície (CuSO4 ativa esfalerita) e reguladores de pH controlam a seletividade."
    risk: fato
    source: "Wills & Finch 2016, cap. 12; Bulatovic 2007, cap. 1–5"
  - claim_id: GEOMET-M09-A05-FLOTACAO-FISICA-004
    claim: "A flotação depende do contato trifásico sólido-líquido-gás, cuja adesão cresce com o ângulo de contato; há uma janela de tamanho útil (partículas grossas acima de ~150–300 µm descolam por peso, ultrafinas abaixo de ~10 µm colidem pouco com as bolhas); a recuperação em função do tempo segue aproximadamente primeira ordem, R(t) = R_∞ (1 − e^(−kt))."
    risk: fato
    source: "Wills & Finch 2016, cap. 12"
  - claim_id: GEOMET-M09-A05-LIXIVIACAO-005
    claim: "A lixiviação dissolve o metal seletivamente: em pilha (baixo teor: Cu oxidado e secundário com H2SO4, Au com cianeto diluído), agitada em tanque (teores maiores, Au por CIL/CIP, Zn, U), ou sob pressão (autoclave/POX para sulfetos, Ni laterítico por HPAL); a cianetação do ouro segue a equação de Elsner 4 Au + 8 NaCN + O2 + 2 H2O → 4 Na[Au(CN)2] + 4 NaOH; a biolixiviação usa micro-organismos acidófilos para oxidar sulfetos; ouro refratário é encapsulamento em pirita/arsenopirita ou preg-robbing por carbono."
    risk: fato
    source: "Wills & Finch 2016, cap. 15; Marsden & House 2006, cap. 5 e 10; Gupta 2003, cap. 6"
  - claim_id: GEOMET-M09-A05-DOIS-PRODUTOS-006
    claim: "Do balanço de massa (F = C + T) e de metal (F·f = C·c + T·t), a recuperação obtém-se apenas dos três teores pela fórmula de dois produtos R = [c(f − t)]/[f(c − t)]; a razão de enriquecimento é c/f e a razão de concentração é K = F/C = (c − t)/(f − t)."
    risk: fato
    source: "Wills & Finch 2016, cap. 3; Napier-Munn et al. 1996, cap. 4"
  - claim_id: GEOMET-M09-A05-EXEMPLO-007
    claim: "Para f = 0,85 % Cu, c = 27,5 % Cu, t = 0,072 % Cu: R = [27,5 × 0,778]/[0,85 × 27,428] = 91,8 %; razão de concentração K = 27,428/0,778 = 35,3; razão de enriquecimento = 27,5/0,85 = 32,4. Baixar o rejeito para 0,050 % Cu elevaria R para ~94,3 %."
    risk: calculo
    source: "Fórmula de dois produtos; aritmética de balanço metalúrgico"
-->
