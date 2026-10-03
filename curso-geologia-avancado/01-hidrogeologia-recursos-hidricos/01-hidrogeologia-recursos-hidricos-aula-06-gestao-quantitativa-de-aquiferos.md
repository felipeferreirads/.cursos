# Aula 06: Gestão quantitativa — recarga, balanço hídrico, intrusão salina, vazão sustentável e outorga

**ID:** geologia-avancado-m01-a06
**Módulo:** [[01-hidrogeologia-recursos-hidricos-modulo|Módulo 01 — Hidrogeologia e recursos hídricos]]
**Duração estimada:** ~29 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** montar o balanço hídrico de um aquífero, distinguir vazão segura de vazão sustentável, quantificar a intrusão salina pela relação de Ghyben-Herzberg e situar a outorga de uso da água no arcabouço legal brasileiro.

## Antes de começar, você precisa saber

- Recarga, descarga, relação rio-aquífero efluente/influente/desconectado — Aula 03 deste módulo.
- Interferência entre poços e vazão ótima de um poço individual — Aula 05 deste módulo.
- Densidade da água doce e da água salgada (noção qualitativa de que água salgada é mais densa).

## Conteúdo

### O balanço hídrico de um aquífero

O **balanço hídrico** (water budget) de um aquífero, para qualquer intervalo de tempo, é a contabilidade de massa da água:

Entradas − Saídas = Δ Armazenamento

Entradas típicas: recarga direta por infiltração de precipitação, infiltração de rio influente, recarga lateral de aquíferos vizinhos, retorno de irrigação. Saídas típicas: descarga para rios efluentes e nascentes, evapotranspiração da franja capilar em áreas de nível freático raso, fluxo lateral de saída, e **extração por bombeamento**. Quando entradas igualam saídas, o armazenamento é estável (regime de equilíbrio ou *steady state*); quando bombeamento excede a capacidade do sistema de compensar com aumento de recarga induzida ou redução de descarga natural, o armazenamento diminui — é o rebaixamento regional persistente que caracteriza a superexplotação.

> [!important] Bombear não cria água nova — redistribui o balanço
> Todo volume extra bombeado de um aquífero em equilíbrio tem que vir de algum lugar: ou de uma redução da descarga natural (o rio que recebia menos baseflow, a nascente que seca), ou de um aumento da recarga induzida (um rio antes efluente se torna influente perto do poço), ou da redução do armazenamento (rebaixamento contínuo). O chamado "princípio da captura" (Theis, 1940; Bredehoeft, 2002) formaliza essa ideia: bombeamento sustentável no longo prazo depende de a "captura" (a soma de descarga reduzida mais recarga induzida) equilibrar a extração — não de o aquífero "ter água suficiente" em termos de reserva estática.

### Reserva versus recurso: dois números que não devem ser confundidos

A **reserva permanente** (ou reserva estática) é o volume total de água armazenada no aquífero num dado momento — um estoque, calculável (aproximadamente) como volume saturado × porosidade efetiva (livre) ou × coeficiente de armazenamento (confinado). O **recurso renovável** é a taxa de recarga do aquífero — um fluxo, não um estoque, medido em volume por tempo. A confusão entre os dois é a origem do erro gerencial mais grave em recursos hídricos subterrâneos: tratar a reserva estática (acumulada ao longo de milhares a milhões de anos, em muitos casos) como se fosse disponível para exploração continuada — o que equivale a tratar um depósito bancário fixo como se fosse renda mensal recorrente.

### Vazão segura, vazão sustentável e o problema do conceito de "segurança" isolado

O conceito histórico de **vazão segura** (safe yield), popular no início do século XX, definia-a como a taxa máxima de extração que não excede a taxa média de recarga natural. Esse conceito, hoje considerado insuficiente isoladamente (Sophocleous, 2000), ignora dois fatos centrais: primeiro, que a extração pode induzir aumento de recarga (rio que se torna influente) ou redução de descarga (baseflow reduzido), de modo que "recarga natural" não é uma constante independente do próprio bombeamento; segundo, que mesmo um bombeamento formalmente "dentro da recarga" pode causar impactos inaceitáveis em ecossistemas dependentes de água subterrânea (banhados, nascentes, vazão ecológica de rios) muito antes de esgotar o balanço de massa.

A **vazão sustentável** substitui esse critério puramente quantitativo por um critério de **impacto tolerável**: a taxa de extração que pode ser mantida indefinidamente sem produzir efeitos considerados inaceitáveis — rebaixamento excessivo, redução de vazão de base abaixo de um limiar ecológico, intrusão salina, subsidência do terreno, ou custo de bombeamento economicamente proibitivo. É, deliberadamente, um conceito que envolve escolha social e não só cálculo hidráulico: "inaceitável" é definido pelo gestor e pela sociedade, não deduzido só da equação de balanço.

### A relação de Ghyben-Herzberg: quantificando a interface água doce-água salgada

Em aquíferos costeiros, água doce (menos densa) flutua sobre água salgada (mais densa) que se infiltra do mar, formando uma interface aproximadamente definida pelo equilíbrio hidrostático entre as duas colunas de fluido de densidades diferentes (Badon Ghyben, 1888; Herzberg, 1901). Considerando densidade da água doce ρf ≈ 1,000 g/cm³ e da água salgada ρs ≈ 1,025 g/cm³, o equilíbrio de pressão numa coluna vertical implica que a profundidade da interface abaixo do nível do mar (z) se relaciona com a altura do nível freático acima do nível do mar (h) por:

z = h · [ρf / (ρs − ρf)] ≈ 40 · h

Ou seja: **para cada metro de carga de água doce acima do nível do mar, a interface salgada está aproximadamente 40 metros abaixo do nível do mar.** A relação é uma aproximação hidrostática (ignora o fluxo dinâmico e assume interface abrupta sem zona de mistura, quando na realidade existe uma zona de transição por dispersão), mas captura a ordem de grandeza corretamente e explica por que aquíferos costeiros são desproporcionalmente sensíveis: um rebaixamento de apenas 1 m no nível freático perto da costa pode elevar a interface salgada em ~40 m, potencialmente atingindo o fundo de um poço que antes captava só água doce.

> [!warning] Por que a intrusão salina costuma ser irreversível na prática
> Uma vez que água salgada avança e satura os poros de um trecho de aquífero, revertê-la exige não apenas restabelecer o gradiente de carga original (parar de bombear, ou até sobrecarregar com recarga artificial), mas também lavar fisicamente o sal residual retido na matriz porosa — processo lento, de anos a décadas, mesmo depois de cessada a causa. Prevenção (limitar rebaixamento em faixa costeira, afastar poços da linha de costa, monitorar cloreto) é ordens de grandeza mais barata que remediação.

### Da vazão do poço ao balanço da bacia: a escala da decisão de gestão

A gestão quantitativa de um aquífero opera em duas escalas que precisam ser conciliadas: a escala do **poço individual** (vazão ótima, Aula 05) e a escala do **sistema aquífero regional** (balanço hídrico, vazão sustentável). Um campo de poços onde cada poço individualmente respeita sua vazão ótima local pode, ainda assim, exceder coletivamente a vazão sustentável da bacia — a interferência somada de dezenas de poços "bem dimensionados" isoladamente é exatamente o mecanismo de superexplotação regional mais comum na prática (retomado com profundidade no Módulo 04, dimensionamento de campos de poços). Índices simples de estresse hídrico — razão entre extração total e recarga estimada da bacia — são usados como primeira triagem, mas escondem a distribuição espacial: uma bacia com razão média de 0,3 (aparentemente confortável) pode ter uma sub-bacia local com razão de 1,5 por concentração de poços, já em superexplotação localizada.

### Outorga de direito de uso: o instrumento legal brasileiro

No Brasil, a Lei das Águas (Lei Federal 9.433/1997) institui a **outorga de direito de uso de recursos hídricos** — incluindo água subterrânea — como um dos instrumentos da Política Nacional de Recursos Hídricos, ao lado do enquadramento dos corpos d'água, da cobrança pelo uso e do Sistema de Informações sobre Recursos Hídricos. A outorga é o ato administrativo pelo qual o poder público (a Agência Nacional de Águas e Saneamento Básico — ANA — para corpos hídricos de domínio da União, ou o órgão gestor estadual competente para os de domínio estadual) autoriza, por prazo determinado, a extração de uma vazão específica de um poço, condicionada a critérios técnicos (compatibilidade com a disponibilidade hídrica local, distância mínima de outras captações, monitoramento). Águas subterrâneas são, pela Constituição Federal, sempre de domínio dos Estados — diferente das águas superficiais, que podem ser de domínio da União ou dos Estados conforme o corpo hídrico — o que faz da outorga de água subterrânea, na prática brasileira, quase sempre uma competência estadual, exercida pelos órgãos gestores de recursos hídricos de cada Estado.

O instrumento de outorga só funciona, tecnicamente, se apoiado num **cadastro de poços** e numa estimativa confiável de disponibilidade hídrica subterrânea da bacia — sem os quais o órgão gestor autoriza extrações sem visibilidade do estresse acumulado, o cenário mais comum em bacias sedimentares brasileiras historicamente subcadastradas. A fiscalização da outorga (poços clandestinos, extração acima do outorgado) é, nesse sentido, tão determinante para a gestão quantitativa efetiva quanto o cálculo técnico da vazão sustentável em si.

## Exemplo trabalhado

**Situação:** um poço costeiro capta de um aquífero livre arenoso onde o nível freático natural está 1,5 m acima do nível do mar. O bombeamento contínuo rebaixa o nível freático local para 0,4 m acima do nível do mar. O poço tem 45 m de profundidade abaixo do nível do mar. Avalie o risco de intrusão salina.

**Raciocínio.** Pela relação de Ghyben-Herzberg, a profundidade da interface salgada antes do bombeamento era aproximadamente z₁ = 40 × 1,5 = 60 m abaixo do nível do mar — o poço (45 m) estava 15 m acima da interface, com margem de segurança. Após o rebaixamento para 0,4 m, a nova profundidade estimada da interface é z₂ = 40 × 0,4 = 16 m abaixo do nível do mar — a interface subiu de 60 m para 16 m, ultrapassando os 45 m de profundidade do poço por 29 m. O poço está agora abaixo da interface salgada estimada e deve apresentar (ou apresentar em breve, dada a zona de transição real e o tempo de resposta do sistema) salinização progressiva.

**A lição:** a relação de Ghyben-Herzberg amplifica por um fator de ~40 qualquer rebaixamento em faixa costeira — um rebaixamento de pouco mais de 1 m, que pareceria trivial num aquífero interior, é suficiente para inverter completamente a viabilidade de um poço costeiro relativamente profundo. Isso justifica por que a gestão de aquíferos costeiros trata limites de rebaixamento com muito mais rigor que aquíferos do interior.

## Erros comuns

- **Confundir reserva permanente (estoque) com recurso renovável (fluxo de recarga)** ao avaliar quanto se pode extrair de um aquífero — o erro que leva à "mineração" inadvertida de água subterrânea antiga.
- **Aplicar o conceito de vazão segura (safe yield) como se fosse suficiente**, sem considerar os impactos induzidos (redução de baseflow, secamento de nascentes) que podem ser inaceitáveis muito antes do limite de balanço de massa ser atingido.
- **Tratar a relação de Ghyben-Herzberg como uma medição exata da posição da interface**, ignorando que é uma aproximação hidrostática que despreza a zona real de mistura por dispersão e o comportamento dinâmico do fluxo.
- **Avaliar estresse hídrico só pela razão extração/recarga média da bacia inteira**, mascarando superexplotação localizada por concentração espacial de poços.
- **Assumir que águas subterrâneas seguem o mesmo regime dominial das águas superficiais no Brasil** — são sempre de domínio estadual, independentemente do domínio do corpo de água superficial sobrejacente.

## O que não concluir

- **Que um aquífero em "equilíbrio de balanço" nunca deve ser explotado.** O objetivo da gestão não é zerar a extração, e sim dimensioná-la para um novo equilíbrio com impacto tolerável — captura compensando extração de forma sustentada, dentro de limites aceitos.
- **Que intrusão salina só ocorre em aquíferos litorâneos rasos.** Pode ocorrer também em aquíferos confinados profundos com conexão hidráulica ao mar, ou por avanço lateral em vez de ascensão vertical, dependendo da geometria do aquífero.
- **Que a existência de outorga garante, por si, sustentabilidade.** A outorga é um instrumento de controle formal; sua eficácia depende de a disponibilidade hídrica ter sido corretamente estimada e de haver fiscalização — outorgar acima da capacidade real do aquífero é uma falha de gestão, não uma impossibilidade legal.

## Recap relâmpago

- **Balanço hídrico**: entradas − saídas = Δ armazenamento; bombeamento sustentável depende do princípio da captura (recarga induzida + descarga reduzida), não apenas da reserva estática existente.
- **Reserva (estoque) ≠ recurso (fluxo de recarga)** — confundir os dois é o erro gerencial mais grave em água subterrânea.
- **Vazão segura** (balanço de massa) foi substituída por **vazão sustentável** (impacto tolerável) como critério de gestão moderno.
- **Ghyben-Herzberg**: z ≈ 40h — cada metro de rebaixamento no litoral eleva a interface salgada em ~40 m; intrusão é lenta e cara de reverter.
- **Outorga no Brasil** (Lei 9.433/1997): água subterrânea é sempre de domínio estadual; a outorga só funciona apoiada em cadastro de poços e estimativa confiável de disponibilidade hídrica.

## Próxima aula

[[01-hidrogeologia-recursos-hidricos-aula-07-aguas-subterraneas-e-mudancas-climaticas|Aula 07 — Águas subterrâneas e mudanças climáticas: crises hídricas, aquíferos fósseis, manejo da recarga e governança]]

## Anterior

[[01-hidrogeologia-recursos-hidricos-aula-05-testes-de-bombeamento-e-de-aquifero|Aula 05 — Testes de bombeamento e de aquífero: rebaixamento, interferência e vazão ótima]]

## Fontes

- Balanço hídrico e princípio da captura: Theis, C. V. (1940), "The source of water derived from wells: essential factors controlling the response of an aquifer to development", *Civil Engineering*, 10(5), 277–280; Bredehoeft, J. D. (2002), "The water budget myth revisited: why hydrogeologists model", *Ground Water*, 40(4), 340–345.
- Crítica ao conceito de vazão segura e proposta de vazão sustentável: Sophocleous, M. (2000), "From safe yield to sustainable development of water resources — the Kansas experience", *Journal of Hydrology*, 235(1–2), 27–43.
- Relação de Ghyben-Herzberg e intrusão salina em aquíferos costeiros: Fetter, C. W. (2001), *Applied Hydrogeology*, 4ª ed., Prentice-Hall, cap. 11; Badon Ghyben, W. (1888); Herzberg, A. (1901), conforme citados em Fetter (2001).
- Outorga de direito de uso de recursos hídricos e domínio das águas subterrâneas no Brasil: Lei Federal 9.433/1997 (Política Nacional de Recursos Hídricos); Constituição Federal de 1988, art. 26, I; Agência Nacional de Águas e Saneamento Básico (ANA), Manual de Procedimentos Técnicos e Administrativos de Outorga.

<!--
nivel: avancado
palavras_corpo: ~1900

mapa_objetivo_secao:
  geologia-avancado-m01-oa04: "O balanço hídrico de um aquífero" + "Reserva versus recurso: dois números que não devem ser confundidos" + "Vazão segura, vazão sustentável e o problema do conceito de segurança isolado" + "A relação de Ghyben-Herzberg: quantificando a interface água doce-água salgada" + "Da vazão do poço ao balanço da bacia: a escala da decisão de gestão" + "Outorga de direito de uso: o instrumento legal brasileiro" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: HIDRO-M01-A06-CAPTURA-001
    claim: "O princípio da captura (Theis 1940; Bredehoeft 2002) estabelece que bombeamento sustentável de longo prazo depende de a soma de descarga natural reduzida mais recarga induzida equilibrar a extração, e não apenas da existência de reserva estática no aquífero."
    risk: fato
    source: "Theis 1940, Civil Engineering 10(5); Bredehoeft 2002, Ground Water 40(4)"
  - claim_id: HIDRO-M01-A06-SAFEYIELD-002
    claim: "O conceito de vazão segura (safe yield), que limita a extração à taxa média de recarga natural, é considerado insuficiente isoladamente pela literatura moderna (Sophocleous 2000) e foi substituído pelo conceito de vazão sustentável, baseado em impacto tolerável."
    risk: fato
    source: "Sophocleous 2000, Journal of Hydrology 235(1-2)"
  - claim_id: HIDRO-M01-A06-GHYBEN-003
    claim: "A relação de Ghyben-Herzberg estima a profundidade da interface água doce-água salgada abaixo do nível do mar como z = h*[rho_f/(rho_s-rho_f)], aproximadamente z = 40h para densidades típicas de água doce (1,000 g/cm3) e água do mar (1,025 g/cm3), sendo uma aproximação hidrostática que ignora a zona real de mistura por dispersão."
    risk: fato
    source: "Badon Ghyben 1888; Herzberg 1901, apud Fetter 2001, cap. 11"
  - claim_id: HIDRO-M01-A06-OUTORGA-004
    claim: "No Brasil, a Lei Federal 9.433/1997 institui a outorga de direito de uso de recursos hídricos, incluindo água subterrânea, como instrumento da Política Nacional de Recursos Hídricos; pela Constituição Federal de 1988 (art. 26, I), as águas subterrâneas são sempre de domínio dos Estados, tornando a outorga de água subterrânea majoritariamente uma competência estadual."
    risk: fato
    source: "Lei 9.433/1997; Constituição Federal 1988, art. 26, I"
-->
