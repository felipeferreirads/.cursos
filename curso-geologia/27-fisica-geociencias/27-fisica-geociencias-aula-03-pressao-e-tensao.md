# Aula 03: Pressão e tensão — força espalhada em área, da coluna de rocha ao cisalhamento

**ID:** geologia-m27-a03
**Módulo:** [[27-fisica-geociencias-modulo|Módulo 27 — Física para geociências: grandezas, forças e energia]]
**Duração estimada:** ~30 min
**Nível:** ensino médio completo, sem geologia prévia (contrato `ensino-medio-sem-geologia-v1`)
**Objetivo:** calcular pressão a partir de força e área e distinguir pressão litostática, pressão hidrostática e tensão cisalhante.

> [!info] Esta aula cobre uma lacuna do curso O [[17-geologia-estrutural-modulo|Módulo 17]] declara o objetivo de "reativar força, pressão e tensão em nível funcional" (`geologia-m17-oa01`), mas nenhuma aula escrita do curso cobria pressão e tensão de forma explícita antes desta — lacuna registrada em `_contexto.md` (2026-08-19). Esta aula entrega esse conteúdo.

## Antes de começar, você precisa saber

- Força, massa e as leis de Newton — [[27-fisica-geociencias-aula-02-forca-massa-leis-de-newton|aula 02 deste módulo]] (exigido).

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **Pressão** | Uma força espalhada por uma área, medida em pascal (Pa = N/m²); quanto menor a área para a mesma força, maior a pressão. |
| **Pressão litostática** | A pressão exercida pelo peso da coluna de rocha acima de um ponto no subsolo, igual em todas as direções. |
| **Pressão hidrostática** | A pressão exercida pelo peso de uma coluna de fluido (água, magma) acima de um ponto. |
| **Tensão (stress)** | De forma geral, a força interna por unidade de área que atua sobre um corpo, podendo variar com a direção — mais ampla que pressão, que é sempre igual em todas as direções. |
| **Tensão normal** | A componente da tensão perpendicular a uma superfície, que comprime ou estica. |
| **Tensão cisalhante (shear)** | A componente da tensão paralela a uma superfície, que tende a fazer as partes deslizarem uma sobre a outra. |
| **Isotrópico** | Que tem o mesmo valor em todas as direções — a pressão é isotrópica; a tensão, em geral, não é. |

## Conteúdo

### Pressão: a mesma força, espalhada de jeitos diferentes

Pise na neve com uma bota comum e você afunda; calce um esqui, com a mesma força do seu peso, e você flutua na superfície. A força é a mesma — o que muda é a **área** sobre a qual ela se espalha. É essa relação que define **pressão**: força dividida por área (P = F/A), medida em **pascal (Pa)**, que equivale a um newton por metro quadrado. Quanto menor a área para a mesma força, maior a pressão resultante — e é por isso que uma lâmina fina corta e uma superfície larga sustenta.

### Pressão litostática: o peso da rocha acima de você

No subsolo, a pressão em qualquer ponto vem do peso de toda a coluna de rocha empilhada acima dele — assim como a pressão no fundo de uma piscina vem do peso da água acima. Essa pressão, chamada **pressão litostática**, cresce com a profundidade: quanto mais rocha por cima, maior o peso acumulado, maior a área efetiva de sustentação não muda a lógica — a pressão continua sendo o peso da coluna dividido pela área da base dessa coluna.

A característica central da pressão litostática é ser **isotrópica**: em um ponto qualquer do subsolo, ela empurra igualmente em todas as direções — para cima, para baixo, para os lados — exatamente como a pressão da água num ponto qualquer de uma piscina não "escolhe" uma direção preferencial. É essa mesma lógica que rege a **pressão hidrostática**, o equivalente para uma coluna de fluido (água subterrânea, ou magma dentro de uma câmara magmática) em vez de rocha sólida.

### Tensão: quando a força depende da direção

A pressão isotrópica é um caso especial de um conceito mais amplo, a **tensão** (em inglês, *stress*): a força interna por unidade de área que atua sobre um corpo. A diferença crucial é que a tensão, em geral, **não** precisa ser igual em todas as direções — uma rocha em profundidade pode estar sendo comprimida com mais força numa direção do que em outra, por exemplo, por causa do empurrão de placas tectônicas convergindo.

> [!tip] Uma analogia Pense em apertar uma esponja entre as duas mãos. Se você aperta igualmente de todos os lados (como debaixo d'água), a esponja só encolhe de tamanho, sem mudar de forma — isso é pressão isotrópica. Mas se você aperta mais forte de um lado do que do outro, a esponja não só encolhe: ela também **muda de forma**, alongando-se na direção onde a pressão é menor. Essa assimetria de força por área é o que a tensão captura, e a pressão não.

Quando a força atua **perpendicular** a uma superfície dentro da rocha, ela é chamada de **tensão normal** — ela comprime ou estica o material ao longo dessa direção. Quando a força atua **paralela** à superfície, tentando fazer duas partes do material deslizarem uma sobre a outra, ela é chamada de **tensão cisalhante**. As duas componentes normalmente coexistem: em quase qualquer plano dentro de uma rocha sob tensão, há alguma componente normal e alguma componente cisalhante ao mesmo tempo, e é a combinação das duas que determina se — e como — a rocha vai se deformar.

### Por que essa distinção importa para entender a deformação da rocha

A pressão litostática sozinha, por ser isotrópica, tende a comprimir a rocha uniformemente, reduzindo espaços vazios e aumentando a densidade — é importante para entender compactação e metamorfismo, mas não explica, por si só, por que uma rocha se dobra numa direção específica ou se rompe ao longo de um plano específico. É a existência de **diferenças de tensão entre direções** — o que o Módulo 17 (Geologia estrutural) chama de tensão diferencial — que produz deformação orientada: dobras que se alinham numa direção preferencial, falhas que se rompem ao longo de planos específicos, minerais que crescem alongados numa direção sob metamorfismo. A tensão cisalhante, em particular, é a componente diretamente responsável por fazer blocos de rocha deslizarem uns em relação aos outros ao longo de uma falha — tema que o Módulo 17 desenvolve em profundidade.

## Exemplo trabalhado

**Situação:** um ponto está a 3 km de profundidade, sob uma coluna de rocha com densidade média de 2.700 kg/m³.

**Pergunta 1: qual é, aproximadamente, a pressão litostática nesse ponto?**

A pressão litostática é o peso da coluna de rocha dividido pela área da base, o que equivale a P = ρ × g × h, onde ρ é a densidade da rocha, g é a aceleração da gravidade (≈ 9,8 m/s²) e h é a profundidade. Substituindo: P ≈ 2.700 kg/m³ × 9,8 m/s² × 3.000 m ≈ 79.000.000 Pa ≈ 79 MPa (megapascal). Esse valor empurra igualmente em todas as direções nesse ponto — é isotrópico.

**Pergunta 2: se, além dessa pressão litostática, a convergência de duas placas tectônicas adicionar uma tensão extra de 40 MPa numa direção horizontal específica, o que muda?**

A tensão deixa de ser isotrópica: numa direção horizontal a tensão total é maior (79 + 40 = 119 MPa) do que nas outras direções (que continuam em torno de 79 MPa). Essa diferença entre direções é a tensão diferencial, e é ela — não a pressão litostática de fundo — que vai orientar a deformação da rocha: dobras e falhas tendem a se organizar em relação a essa direção preferencial de tensão máxima, não aleatoriamente.

**A lição:** a mesma rocha, na mesma profundidade, pode estar sob a mesma pressão litostática de fundo e, ainda assim, se deformar de forma orientada — porque é a tensão diferencial, não a pressão isotrópica, que "escolhe" a direção da deformação.

## Erros comuns

- **Usar "pressão" e "tensão" como sinônimos perfeitos.** Pressão é sempre isotrópica (igual em todas as direções); tensão é o conceito mais geral, que pode variar com a direção — toda pressão é um caso particular de tensão, mas nem toda tensão é uma pressão.
- **Achar que pressão litostática sozinha explica dobras e falhas.** Ela comprime uniformemente, mas é a tensão diferencial (a diferença de tensão entre direções) que produz deformação orientada.
- **Confundir tensão normal com tensão cisalhante.** A primeira age perpendicular a uma superfície (compressão ou estiramento); a segunda age paralela a ela (tendência a deslizamento) — na maioria das situações reais, as duas coexistem no mesmo plano.
- **Esquecer que pressão hidrostática e litostática têm a mesma lógica com fluidos diferentes.** Água subterrânea e magma produzem pressão pelo mesmo princípio — peso da coluna de fluido — que a rocha sólida produz pressão litostática.

## O que não concluir

- **Que esta aula ensina o tensor de tensões completo (com suas nove componentes) ou a construção do círculo de Mohr.** Essa formalização matemática mais avançada é tratada, quando necessária, dentro do [[17-geologia-estrutural-modulo|Módulo 17]]; esta aula entrega apenas o vocabulário funcional de pressão, tensão normal e cisalhante.
- **Que a pressão de poro (a pressão exercida por fluidos dentro dos espaços vazios de uma rocha, que reduz a tensão efetiva sobre o esqueleto sólido) já foi coberta aqui.** É um refinamento importante, tratado em módulos aplicados de geologia de engenharia e hidrogeologia.

## Recap relâmpago

- **Pressão** é força dividida por área (P = F/A, em pascal); é sempre **isotrópica** — igual em todas as direções.
- A **pressão litostática** vem do peso da coluna de rocha acima de um ponto; a **pressão hidrostática**, do peso de uma coluna de fluido.
- **Tensão** é o conceito mais geral de força interna por área, que pode variar com a direção; toda pressão é uma tensão isotrópica, mas nem toda tensão é isotrópica.
- **Tensão normal** age perpendicular a uma superfície (comprime ou estica); **tensão cisalhante** age paralela a ela (tende a deslizamento).
- É a **tensão diferencial** — a diferença de tensão entre direções — que produz deformação orientada da rocha (dobras, falhas), não a pressão litostática isotrópica de fundo.

## Próxima aula

[[27-fisica-geociencias-aula-04-trabalho-energia-potencia|Aula 04 — Trabalho, energia e potência]]

## Anterior

[[27-fisica-geociencias-aula-02-forca-massa-leis-de-newton|Aula 02 — Força, massa e as leis de Newton]]

## Fontes

- Pressão, força e área: física geral básica (ex.: Halliday, Resnick & Walker, *Fundamentals of Physics*).
- Pressão litostática, pressão hidrostática, tensão (stress), tensão normal e cisalhante, e tensão diferencial como motor da deformação orientada: Twiss & Moores, *Structural Geology*; Fossen, *Structural Geology*; Davis, Reynolds & Kluth, *Structural Geology of Rocks and Regions*.

<!--
nivel: ensino-medio-sem-geologia-v1
palavras_corpo: ~1520
bridge_lesson: true

mapa_objetivo_secao:
  OA-03: "Pressão: a mesma força, espalhada de jeitos diferentes" + "Pressão litostática: o peso da rocha acima de você" + "Tensão: quando a força depende da direção" + "Por que essa distinção importa para entender a deformação da rocha" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEO-M27-A03-PRESSAO-DEFINICAO-001
    claim: "Pressão é definida como força dividida por área (P=F/A), medida em pascal (Pa=N/m²), e é uma grandeza isotrópica — igual em todas as direções em um ponto de um fluido em equilíbrio."
    risk: fato
    source: "física geral básica; mecânica dos fluidos"
  - claim_id: GEO-M27-A03-PRESSAO-LITOSTATICA-002
    claim: "A pressão litostática em um ponto no subsolo é aproximada por P = ρ·g·h, onde ρ é a densidade média da coluna de rocha sobrejacente, g é a aceleração da gravidade e h é a profundidade; é isotrópica em condições de equilíbrio hidrostático de rocha."
    risk: fato
    source: "Twiss & Moores, Structural Geology; Fossen, Structural Geology"
  - claim_id: GEO-M27-A03-TENSAO-VS-PRESSAO-003
    claim: "Tensão (stress) é o conceito geral de força interna por unidade de área atuando sobre um corpo, podendo variar com a direção do plano considerado; pressão é o caso particular de tensão isotrópica (igual em todas as direções)."
    risk: fato
    source: "Twiss & Moores, Structural Geology; Davis, Reynolds & Kluth, Structural Geology of Rocks and Regions"
  - claim_id: GEO-M27-A03-NORMAL-CISALHANTE-004
    claim: "Em qualquer plano dentro de um corpo sob tensão, a tensão pode ser decomposta em uma componente normal (perpendicular ao plano, que comprime ou estica) e uma componente cisalhante (paralela ao plano, que tende a produzir deslizamento)."
    risk: fato
    source: "Twiss & Moores, Structural Geology; mecânica dos meios contínuos básica"
  - claim_id: GEO-M27-A03-TENSAO-DIFERENCIAL-005
    claim: "É a tensão diferencial (a diferença de magnitude de tensão entre direções distintas), e não a pressão litostática isotrópica de fundo, que controla a orientação da deformação da rocha, incluindo a formação orientada de dobras e falhas."
    risk: interpretacao
    source: "Twiss & Moores, Structural Geology; Fossen, Structural Geology — princípio consolidado de geologia estrutural"

nota_trilha_apoio: >-
  Aula 3 de 6 do módulo 27 (trilha de apoio, opcional, não bloqueante), criada em
  2026-08-19. Aula-ponte que preenche diretamente a lacuna do objetivo
  geologia-m17-oa01 do Módulo 17 (Geologia estrutural), que pressupõe
  reativação funcional de força, pressão e tensão sem que nenhuma aula escrita a
  entregasse até esta rodada — ver decisão registrada em _contexto.md (2026-08-19).
-->
