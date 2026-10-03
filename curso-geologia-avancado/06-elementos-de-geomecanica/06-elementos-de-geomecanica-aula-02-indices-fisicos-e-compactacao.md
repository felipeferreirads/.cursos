# Aula 02: Índices físicos de solos e rochas e compactação

**ID:** geologia-avancado-m06-a02
**Módulo:** [[06-elementos-de-geomecanica-modulo|Módulo 06 — Elementos de geomecânica]]
**Duração estimada:** ~27 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** calcular os índices físicos de um solo (índice de vazios, porosidade, teor de umidade, grau de saturação, pesos específicos) a partir de dados de massa e volume, relacioná-los aos índices físicos de rochas já vistos no Módulo 05, e determinar a umidade ótima e a densidade seca máxima de um solo por ensaio de compactação.
**Pré-requisito:** Aula 01 deste módulo (classificação de solos); porosidade e densidade de rochas, tratadas no Módulo 05, Aula 02.

## Antes de começar, você precisa saber

- Que um solo (ou uma rocha porosa) é um sistema de três fases: sólidos minerais, água e ar, ocupando volumes distintos dentro do volume total da amostra.
- Manipulação algébrica básica de razões e proporções.

## Conteúdo

### O modelo de três fases e as relações-massa-volume

Qualquer amostra de solo (e, em menor escala, uma rocha porosa) pode ser representada por um **diagrama de fases**: um volume total V, dividido em volume de sólidos (Vs), volume de água (Vw) e volume de ar (Va), com Vv = Vw + Va sendo o **volume de vazios**. Em massa, o sólido tem massa Ms e a água massa Mw (a massa do ar é desprezada). Todos os índices físicos usados em mecânica dos solos são razões entre esses volumes e massas — não constantes tabeladas, mas grandezas calculadas a partir de dados medidos em laboratório (massa total, massa seca, volume da amostra).

Os índices de **volume** mais usados:

- **Índice de vazios:** e = Vv/Vs (razão entre o volume de vazios e o volume de sólidos — não em relação ao volume total).
- **Porosidade:** n = Vv/V (razão entre o volume de vazios e o volume total da amostra, geralmente expressa em %).
- **Grau de saturação:** Sr = Vw/Vv (fração dos vazios ocupada por água; Sr=0 para solo seco, Sr=1 ou 100% para solo saturado).

Índice de vazios e porosidade descrevem a mesma coisa (a proporção de vazios) em relação a bases diferentes (sólidos vs. total), e por isso se convertem um no outro sem precisar de mais nenhum dado:

n = e/(1+e)  e  e = n/(1−n)

> [!important] Por que dois índices para a mesma ideia
> A porosidade (n) é mais intuitiva para descrever "quanto vazio tem uma amostra" e é o índice preferido para rochas. O índice de vazios (e) é preferido em mecânica dos solos porque aparece de forma mais direta nas equações de adensamento e recalque (Aula 05): à medida que o solo se comprime, é o volume de sólidos — não o volume total, que muda — que permanece constante, tornando e a base de referência mais estável para acompanhar a evolução do volume ao longo do carregamento.

### Teor de umidade e pesos específicos

O **teor de umidade** (w) é a razão entre a massa de água e a massa de sólidos secos (não a massa total!):

w = Mw/Ms

expresso em % (um solo saturado de argila mole pode facilmente ter w > 50%, ou seja, mais massa de água que de sólidos).

O **peso específico** (ou unidade de peso) relaciona o peso da amostra ao seu volume total, em diferentes condições de referência:

- **Peso específico natural (ou úmido):** γ = W/V, o peso total (sólidos + água presente) sobre o volume total — a condição real de campo.
- **Peso específico seco:** γd = Ws/V, o peso apenas dos sólidos sobre o mesmo volume total — usado como referência de compactação (Ws não muda ao secar a amostra, então γd é o índice mais estável para comparar o "empacotamento" de solos com umidades diferentes).
- **Peso específico saturado:** γsat, o peso específico que a amostra teria se todos os vazios estivessem preenchidos por água — usado para calcular tensões totais abaixo do nível d'água (Aula 03).
- **Peso específico submerso (ou efetivo):** γsub = γsat − γw, o peso específico "aparente" de um solo totalmente submerso, descontado o empuxo da água — central na Aula 03 para o cálculo de tensões efetivas.

O peso específico natural e o seco relacionam-se diretamente pelo teor de umidade:

γd = γ/(1+w)

— uma relação puramente geométrica (o peso específico natural inclui a água; dividir por (1+w) "remove" essa água da base de peso, mantendo o mesmo volume total de referência), válida independentemente da textura ou mineralogia do solo.

### Densidade relativa dos grãos e densidade relativa (compacidade)

A **densidade relativa dos grãos** (Gs, adimensional, também chamada de peso específico relativo dos sólidos) é a razão entre a densidade dos sólidos minerais e a densidade da água a 4°C — tipicamente 2,65–2,70 para solos com predomínio de quartzo e feldspato, podendo passar de 2,75 em solos ricos em minerais pesados ou ferruginosos. Gs é uma propriedade da mineralogia dos grãos, não do estado de compactação — dois corpos de prova do mesmo solo, um fofo e um denso, têm o mesmo Gs, mas índices de vazios diferentes.

Não confundir Gs com a **densidade relativa (ou compacidade relativa)**, Dr, que descreve o estado de compacidade de um solo **granular** (areias e pedregulhos, onde não se aplicam limites de Atterberg) comparando seu índice de vazios atual aos índices de vazios extremos possíveis para aquele material:

Dr = (emáx − e)/(emáx − emín) × 100%

onde emáx é o índice de vazios no estado mais fofo possível (deposição solta) e emín no estado mais denso possível (compactação máxima em laboratório). Dr próximo de 0% indica areia muito fofa (potencialmente suscetível a liquefação sob carregamento cíclico); Dr próximo de 100% indica areia muito densa (alta resistência ao cisalhamento, baixa compressibilidade).

### Índices físicos de rochas: continuidade com o Módulo 05

O Módulo 05 (Aula 02) já introduziu porosidade e densidade de rocha intacta como parâmetros de caracterização física, no mesmo sentido usado aqui para solos — a diferença central é de grandeza e de mecanismo: a porosidade de uma rocha sã costuma ser de 0,1% a poucos % (vazios intergranulares residuais, microfissuras), enquanto solos podem exceder 50% de porosidade (argilas moles, solos residuais jovens); e a variação de porosidade num solo é dominada por rearranjo mecânico das partículas (compactação, adensamento), enquanto numa rocha ela é dominada por processos diagenéticos e de fissuramento, muito mais lentos e menos reversíveis por carregamento mecânico direto. O vocabulário e as fórmulas (n=Vv/V, γsat, γsub) são idênticos nos dois materiais — o que muda é a ordem de grandeza típica e o processo físico que controla sua evolução.

### Compactação: o ensaio de Proctor

**Compactação** é a densificação mecânica de um solo por aplicação de energia (impacto, amassamento, vibração), reduzindo o índice de vazios sem alteração significativa do teor de umidade durante o processo de aplicação da energia — distinta do **adensamento** (Aula 05), que é a redução de volume ao longo do tempo por expulsão de água sob carga sustentada num solo saturado. O **ensaio de Proctor** (normal ou modificado, diferindo na energia de compactação aplicada) compacta, com energia padronizada, o mesmo solo em vários teores de umidade, medindo o peso específico seco resultante em cada um. O resultado é a **curva de compactação**: γd cresce com w até um pico — a **umidade ótima** (wót) — e decresce depois dele.

O formato em sino da curva reflete dois efeitos que competem: em umidades baixas, pouca água lubrifica o rearranjo dos grãos, e o mesmo impacto compacta pouco (partículas ainda "travadas" por atrito e sucção); à medida que w aumenta até wót, a água lubrifica o deslizamento entre partículas, permitindo maior densificação com a mesma energia; além de wót, o excesso de água passa a ocupar espaço que, de outro modo, seria preenchido por sólidos adicionais — a água incompressível "empurra" os grãos para fora, reduzindo γd apesar da energia constante.

O limite teórico da curva de compactação é a **curva de saturação (zero de vazios de ar)**, o lugar geométrico onde Sr=100% para cada w — nenhum ponto experimental da curva de compactação ultrapassa essa curva, porque nenhuma compactação mecânica, por mais energia aplicada, consegue expulsar todo o ar de uma amostra sem que ela sature completamente:

γd,zav = Gs·γw / (1 + w·Gs)

> [!warning] A curva de compactação depende da energia aplicada
> Comparar diretamente uma umidade ótima obtida com energia normal a outra obtida com energia modificada (maior) é um erro comum: energia maior desloca a curva para uma wót menor e um γd,máx maior — os dois ensaios (Proctor normal e modificado, ASTM D698 e D1557 respectivamente, com energias de compactação diferentes por unidade de volume) descrevem a mesma amostra de solo, mas produzem curvas diferentes, não intercambiáveis sem qualificar qual energia foi usada.

## Exemplo trabalhado

**Situação:** um corpo de prova de solo tem massa total 185 g, massa seca 160 g e volume total 100 cm³. A densidade relativa dos grãos é Gs = 2,68. Calcule o teor de umidade, o índice de vazios, a porosidade e o grau de saturação. (Considere γw = 1 g/cm³ = 9,81 kN/m³ apenas para efeito de conversão de unidades quando necessário; nos cálculos de massa/volume em g e cm³, a densidade da água é numericamente 1.)

**Resolução:**

Massa de água: Mw = 185 − 160 = 25 g. Teor de umidade: w = Mw/Ms = 25/160 = 0,15625 ≈ 15,6%.

Volume de sólidos: Vs = Ms/(Gs·ρw) = 160/(2,68×1) ≈ 59,7 cm³.

Volume de vazios: Vv = V − Vs = 100 − 59,7 = 40,3 cm³.

Índice de vazios: e = Vv/Vs = 40,3/59,7 ≈ 0,675.

Porosidade: n = Vv/V = 40,3/100 = 40,3% (conferência: n = e/(1+e) = 0,675/1,675 ≈ 0,403 → 40,3%. Confere.)

Volume de água: Vw = Mw/ρw = 25/1 = 25 cm³.

Grau de saturação: Sr = Vw/Vv = 25/40,3 ≈ 0,620 → 62,0%.

**Interpretação:** o corpo de prova está com quase 2/3 de seus vazios preenchidos por água (Sr≈62%) — nem seco, nem saturado. Se esse mesmo solo fosse compactado até saturação total (Sr=100%) sem mudar w, o índice de vazios teria que cair; a relação entre w, e e Sr (Sr·e = w·Gs, uma consequência direta de combinar as definições acima) é a ferramenta para prever esse tipo de cenário sem refazer o diagrama de fases do zero.

## Erros comuns

- **Calcular o teor de umidade em relação à massa total (Mw/Mtotal) em vez da massa seca (Mw/Ms)** — a convenção geotécnica universal usa a massa seca como base, o que permite que w ultrapasse 100% em solos muito moles.
- **Confundir índice de vazios (e, base Vs) com porosidade (n, base V)** ao substituir um pelo outro numa fórmula sem converter — são numericamente diferentes exceto no caso trivial e=n=0.
- **Tratar Gs (densidade dos grãos, propriedade mineralógica) como se fosse Dr (densidade relativa, estado de compacidade)** — são grandezas com nomes parecidos em português e significados completamente distintos.
- **Comparar γd,máx e wót de ensaios de Proctor normal e modificado como se fossem a mesma curva**, sem notar que a energia de compactação aplicada é diferente entre os dois ensaios padronizados.

## O que não concluir

- **Que a curva de compactação em sino significa que "mais água sempre piora a compactação".** Só piora *depois* do ótimo; antes dele, mais água ajuda a compactar mais denso com a mesma energia — o objetivo prático em obra é chegar perto de wót, não minimizar a umidade.
- **Que porosidade alta sempre implica baixa resistência.** A relação entre porosidade e resistência depende também da cimentação, da mineralogia e do histórico de tensões — um solo residual poroso mas bem cimentado pode ter resistência comparável à de um solo mais denso mas sem cimentação, tema retomado na Aula 06.

## Recap relâmpago

- O modelo de três fases (sólidos, água, ar) sustenta todos os índices físicos: e=Vv/Vs, n=Vv/V=e/(1+e), Sr=Vw/Vv, w=Mw/Ms (base seca, não total).
- γd=γ/(1+w) converte peso específico natural em seco; γsat e γsub=γsat−γw serão a base do cálculo de tensões totais e efetivas na Aula 03.
- Gs (densidade relativa dos grãos, propriedade mineralógica) e Dr (densidade relativa/compacidade, estado de compactação de solos granulares, Dr=(emáx−e)/(emáx−emín)) são grandezas distintas apesar do nome parecido.
- Solo e rocha usam as mesmas fórmulas de índices físicos, mas em ordens de grandeza e mecanismos de controle diferentes (rearranjo mecânico no solo; diagênese e fissuramento na rocha).
- A curva de compactação de Proctor tem um pico (umidade ótima, γd máximo), limitado pela curva teórica de saturação total, e depende da energia de compactação aplicada — normal e modificado não são comparáveis diretamente.

## Próxima aula

[[06-elementos-de-geomecanica-aula-03-tensoes-totais-efetivas-neutras-k0|Aula 03 — Tensões totais, efetivas e neutras; pressões geostáticas e o coeficiente K0]]

## Anterior

[[06-elementos-de-geomecanica-aula-01-classificacao-de-solos-granulometria-atterberg-sucs-aashto|Aula 01 — Caracterização e classificação dos solos]]

## Fontes

- Modelo de três fases, índices físicos e relações fundamentais: Das, B. M. (2019), *Fundamentos de Engenharia Geotécnica*, 9ª ed., Cengage, cap. 2.
- Densidade relativa (compacidade) de solos granulares: ASTM D4253/D4254 (*Standard Test Methods for Maximum/Minimum Index Density and Unit Weight of Soils*).
- Ensaio de compactação, curva de Proctor e curva de saturação: ASTM D698 (Proctor normal) e ASTM D1557 (Proctor modificado); Das (2019), cap. 6.
- Porosidade e densidade de rocha intacta como referência comparativa: Jaeger, J. C., Cook, N. G. W. & Zimmerman, R. W. (2007), *Fundamentals of Rock Mechanics*, 4ª ed., Blackwell, cap. 1 (retomando o Módulo 05, Aula 02).

<!--
nivel: avancado
palavras_corpo: ~1650

mapa_objetivo_secao:
  geologia-avancado-m06-oa02: "O modelo de três fases e as relações-massa-volume" + "Teor de umidade e pesos específicos" + "Densidade relativa dos grãos e densidade relativa (compacidade)" + "Índices físicos de rochas: continuidade com o Módulo 05" + "Compactação: o ensaio de Proctor" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOMEC-M06-A02-INDICES-001
    claim: "Índice de vazios e=Vv/Vs, porosidade n=Vv/V, e a relação n=e/(1+e) (equivalente e=n/(1-n))."
    risk: fato
    source: "Das 2019, cap. 2"
  - claim_id: GEOMEC-M06-A02-UMIDADE-002
    claim: "O teor de umidade w=Mw/Ms usa a massa seca (não a massa total) como base, permitindo w>100% em solos muito moles."
    risk: fato
    source: "Das 2019, cap. 2; convenção geotécnica padrão (ASTM D2216)"
  - claim_id: GEOMEC-M06-A02-GAMAD-003
    claim: "A relação entre peso específico natural e seco é γd=γ/(1+w)."
    risk: fato
    source: "Das 2019, cap. 2"
  - claim_id: GEOMEC-M06-A02-DR-004
    claim: "A densidade relativa (compacidade) de um solo granular é Dr=(emáx−e)/(emáx−emín)×100%, distinta de Gs (densidade relativa dos grãos, propriedade mineralógica)."
    risk: fato
    source: "ASTM D4253/D4254; Das 2019, cap. 2"
  - claim_id: GEOMEC-M06-A02-COMPACTACAO-005
    claim: "A curva de compactação de Proctor tem um pico de γd na umidade ótima, é limitada pela curva teórica de saturação γd,zav=Gs·γw/(1+w·Gs), e depende da energia de compactação (normal vs. modificado não são comparáveis diretamente)."
    risk: fato
    source: "ASTM D698; ASTM D1557; Das 2019, cap. 6"
-->
