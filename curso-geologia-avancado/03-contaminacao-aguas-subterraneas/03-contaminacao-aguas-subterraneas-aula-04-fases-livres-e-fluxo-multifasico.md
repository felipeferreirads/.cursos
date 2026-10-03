# Aula 04: Fases livres e fluxo multifásico: LNAPL, DNAPL e a interface água doce-água salgada

**ID:** geologia-avancado-m03-a04
**Módulo:** [[03-contaminacao-aguas-subterraneas-modulo|Módulo 03 — Contaminação dos recursos hídricos subterrâneos]]
**Duração estimada:** ~29 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** prever o comportamento em subsuperfície de líquidos não aquosos leves (LNAPL) e densos (DNAPL) e calcular a posição da interface água doce-água salgada num aquífero costeiro.
**Pré-requisito:** transporte advectivo-dispersivo (Aula 02) e retardação/atenuação (Aula 03).

## Antes de começar, você precisa saber

- Zona não saturada e zona saturada, capilaridade básica (Módulo 01).
- Sorção e transporte de soluto dissolvido (Aulas 02–03) — esta aula trata do que acontece **antes** de o contaminante se dissolver, quando ele ainda existe como líquido separado.

## Conteúdo

### NAPL: líquidos que não se misturam com a água

Até aqui, o módulo tratou o contaminante como um **soluto dissolvido** na água. Mas muitos contaminantes comuns — hidrocarbonetos de petróleo, solventes clorados industriais — são pouco solúveis em água e, quando derramados em volume, formam uma fase líquida separada, imiscível: um **NAPL** (*non-aqueous phase liquid*, líquido de fase não aquosa). A parcela do NAPL que efetivamente se dissolve na água que passa por ele segue o transporte de soluto das Aulas 02–03; mas a massa principal do NAPL, enquanto existe como fase separada, se comporta de forma completamente diferente — governada por densidade, viscosidade e tensão interfacial, não pelas leis de transporte de soluto.

A propriedade física que mais determina o comportamento de um NAPL em subsuperfície é sua **densidade relativa à água**, o que leva à classificação central desta aula:

- **LNAPL (*light NAPL*):** densidade menor que a água (< 1,0 g/cm³) — a maioria dos hidrocarbonetos de petróleo (gasolina, diesel, óleo cru).
- **DNAPL (*dense NAPL*):** densidade maior que a água (> 1,0 g/cm³) — solventes clorados (tricloroetileno/TCE, percloroetileno/PCE), muitos bifenilos policlorados (PCBs), alcatrão de hulha (creosoto).

### Comportamento do LNAPL: flutua sobre o lençol freático

Um LNAPL derramado na superfície infiltra pela zona não saturada, sob a ação da gravidade, até encontrar o topo da zona saturada. Como é menos denso que a água, ele **não afunda através do lençol freático** — em vez disso, se espalha lateralmente sobre a franja capilar e o topo da zona saturada, formando uma camada de fase livre que "flutua" aproximadamente sobre o nível d'água, análoga (com ressalvas importantes) a uma mancha de óleo sobre um lago.

Três zonas de contaminação se desenvolvem a partir de um derramamento de LNAPL:

- **Fase livre (*free-phase* ou *mobile* LNAPL):** o volume de LNAPL que ainda pode se mover como líquido separado, geralmente concentrado próximo ao ponto de liberação e sobre o topo do lençol freático.
- **Fase residual (*residual* LNAPL):** LNAPL retido por tensão superficial nos poros do solo e da rocha ao longo de todo o trajeto de infiltração — não flui mais como líquido livre, mas permanece como fonte de longo prazo, continuamente dissolvendo componentes solúveis (como BTEX) na água que passa por ele.
- **Pluma dissolvida:** a parte do LNAPL (fase livre e residual) que se dissolve na água subterrânea que entra em contato com ele, formando a pluma de soluto que de fato se transporta pelas Aulas 02–03 — tipicamente muito menor em extensão que a área ocupada pela fase livre/residual, porque a solubilidade de hidrocarbonetos de petróleo é baixa (benzeno, o componente mais solúvel do BTEX, tem solubilidade de ordem de 1.750 mg/L puro, mas a concentração efetiva dissolvida a partir de uma mistura como a gasolina é bem menor, regida pela lei de Raoult).

> [!important] A espessura do LNAPL medida num poço superestima o volume real no aquífero
> Um poço de monitoramento que intercepta a franja de LNAPL costuma mostrar uma espessura de fase livre aparente maior do que a espessura real presente na formação, porque o próprio poço, ao criar um espaço aberto sem tensão capilar, permite que o LNAPL escoe e se acumule ali mais do que ocorreria no meio poroso intacto ao redor — um efeito bem documentado (Hampton & Miller, 1988) que costuma levar a superestimar reservas de LNAPL recuperável se não corrigido.

### Comportamento do DNAPL: afunda e pode atingir a base do aquífero

Um DNAPL, por ser mais denso que a água, comporta-se de forma qualitativamente diferente: ao atingir o lençol freático, **continua afundando através da zona saturada**, sob o efeito combinado da gravidade e de sua própria pressão de entrada (a pressão capilar necessária para deslocar a água dos poros), até encontrar uma camada de baixa permeabilidade (uma lente de argila, o topo de uma rocha pouco fraturada) que o detenha, ou até esgotar o volume derramado.

Esse comportamento produz uma geometria de contaminação muito mais difícil de caracterizar e remediar que a de um LNAPL:

- O DNAPL pode acumular-se em depressões da superfície de uma camada confinante em subsuperfície ("poças" de DNAPL em pontos baixos de uma interface impermeável), muitas vezes a profundidades e em geometrias imprevisíveis a partir apenas da posição do ponto de liberação na superfície.
- Fraturas em rocha e heterogeneidades sedimentares finas (lentes de silte, contatos entre camadas) podem desviar sua trajetória vertical de forma abrupta e não intuitiva, inclusive lateralmente, seguindo o mergulho de uma camada confinante.
- Assim como o LNAPL, o DNAPL deixa fase residual retida ao longo de todo o trajeto de infiltração, atuando como fonte de longo prazo para a pluma dissolvida — mas, no caso do DNAPL, essa fonte residual pode estar distribuída em profundidade ao longo de toda a coluna, não concentrada perto do lençol freático.

> [!warning] DNAPL contraria a intuição de "contaminante segue o fluxo da água"
> Enquanto a pluma dissolvida de qualquer contaminante (LNAPL, DNAPL ou soluto puro) sempre migra na direção do fluxo de água subterrânea (Aulas 02–03), a fase livre de DNAPL, antes de se dissolver, migra sob controle gravitacional e estrutural (mergulho de camadas confinantes), podendo se mover numa direção **diferente** — inclusive oposta — à direção do fluxo regional de água. Uma investigação que busca a fonte de DNAPL seguindo apenas a direção de fluxo hidráulico corre o risco de nunca encontrar a fase livre, que pode estar fora do eixo da pluma dissolvida.

Por essas razões, sítios contaminados por DNAPL (sobretudo solventes clorados em antigas áreas industriais) estão entre os mais difíceis e caros de remediar, e a detecção direta da fase livre em subsuperfície costuma exigir métodos geofísicos e de perfilagem especializados, além de investigação estratigráfica detalhada da(s) camada(s) confinante(s) que controlam sua migração.

### A interface água doce-água salgada em aquíferos costeiros

Um caso particular, porém importante, de contato entre dois fluidos de densidades diferentes em subsuperfície — mecanicamente análogo em princípio ao LNAPL flutuando sobre a água, mas com a água doce (menos densa) sobre a água salgada (mais densa) — é a **cunha salina** em aquíferos costeiros, introduzida no Módulo 01 no contexto de gestão quantitativa e retomada aqui pelo ângulo da física da interface.

A relação clássica e mais simples que descreve a profundidade dessa interface é a **relação de Ghyben-Herzberg**, deduzida do equilíbrio hidrostático entre as duas colunas de fluido de densidade diferente:

**z = (ρ_f / (ρ_s − ρ_f)) × h**

onde z é a profundidade da interface água doce-água salgada abaixo do nível do mar, h é a altura do nível d'água doce acima do nível do mar, ρ_f é a densidade da água doce (≈1,000 g/cm³) e ρ_s é a densidade da água salgada (≈1,025 g/cm³, água do mar típica). Substituindo esses valores:

z ≈ (1.000 / (1.025 − 1.000)) × h = 40 × h

Ou seja, sob a aproximação de Ghyben-Herzberg, **cada metro de água doce acima do nível do mar corresponde a aproximadamente 40 metros de água doce abaixo do nível do mar antes de encontrar a interface salina** — um multiplicador que explica por que rebaixamentos aparentemente pequenos do nível d'água doce por bombeamento excessivo podem elevar substancialmente a interface salina e, em casos extremos, levar à intrusão de água salgada nos próprios poços de captação (o mecanismo de superexplotação costeira detalhado no Módulo 01, e retomado no planejamento de campos de poços do Módulo 04).

> [!note] Ghyben-Herzberg é uma aproximação hidrostática, não a interface real completa
> A relação assume equilíbrio hidrostático estático e uma interface abrupta, sem considerar o fluxo de água doce em direção ao mar (que na realidade desloca a posição de equilíbrio) nem a zona de mistura por dispersão (Aula 02) que sempre existe entre as duas águas, em vez de um contato perfeitamente nítido. Modelos mais completos (Glover, 1959, considerando fluxo em regime permanente) corrigem essa simplificação, mas a relação de Ghyben-Herzberg permanece o ponto de partida conceitual e a estimativa de ordem de grandeza mais usada em avaliações preliminares.

## Exemplo trabalhado

**Situação:** um aquífero costeiro livre tem nível d'água doce 1,5 m acima do nível do mar num ponto de referência. Usando a relação de Ghyben-Herzberg, estime a profundidade da interface água doce-água salgada abaixo do nível do mar nesse ponto. Se o bombeamento excessivo rebaixar o nível d'água doce para 0,9 m acima do nível do mar, qual o novo valor de z, e quanto a interface sobe?

**Cálculo:**

Situação inicial: z₁ = 40 × h₁ = 40 × 1,5 m = 60 m abaixo do nível do mar.

Após rebaixamento: z₂ = 40 × h₂ = 40 × 0,9 m = 36 m abaixo do nível do mar.

Elevação da interface: Δz = 60 − 36 = 24 m.

**Interpretação:** um rebaixamento de apenas 0,6 m no nível d'água doce (uma fração modesta, facilmente causada por um período de bombeamento intenso ou de estiagem) eleva a interface salina em 24 m — quarenta vezes mais que o rebaixamento na superfície, exatamente pelo multiplicador de Ghyben-Herzberg. Esse resultado ilustra por que aquíferos costeiros são especialmente sensíveis à superexplotação e por que a gestão de poços próximos à costa (Módulo 04) trata a manutenção do nível d'água doce como uma restrição operacional crítica, não apenas uma questão de vazão disponível.

## Erros comuns

- **Tratar LNAPL e DNAPL com o mesmo modelo conceitual de migração**, esperando que ambos se acumulem "sobre" o lençol freático — só o LNAPL faz isso; o DNAPL continua migrando através da zona saturada.
- **Buscar a fonte de uma pluma dissolvida de DNAPL apenas ao longo do eixo de fluxo hidráulico**, sem investigar a geometria de camadas confinantes em profundidade, que pode ter desviado a fase livre para fora desse eixo.
- **Usar a espessura de LNAPL observada num poço de monitoramento como medida direta da espessura real no aquífero**, sem corrigir pelo efeito do próprio poço (Hampton & Miller, 1988).
- **Aplicar a relação de Ghyben-Herzberg como se fosse exata**, ignorando que é uma aproximação hidrostática que não representa a zona de mistura por dispersão nem o efeito do fluxo em regime permanente.

## O que não concluir

- **Que a ausência de fase livre detectada num poço de monitoramento significa ausência de NAPL na área.** Fase residual, sobretudo de DNAPL em profundidade e fora do eixo de poços existentes, pode permanecer não detectada por anos, mesmo funcionando como fonte contínua da pluma dissolvida.
- **Que a relação de 40:1 de Ghyben-Herzberg vale para qualquer aquífero costeiro sem ajuste.** O multiplicador depende das densidades reais da água doce e salgada locais (que variam com temperatura e salinidade) — 40 é o valor de referência para água do mar padrão, não uma constante universal exata.

## Recap relâmpago

- **NAPL** é um líquido imiscível com a água; classifica-se por densidade relativa em **LNAPL** (< água, flutua sobre o lençol freático) e **DNAPL** (> água, afunda através da zona saturada até uma camada confinante).
- LNAPL forma fase livre (móvel), fase residual (retida, fonte de longo prazo) e pluma dissolvida (a fração que efetivamente se transporta como soluto); a espessura de LNAPL num poço superestima a espessura real na formação.
- DNAPL pode migrar em direção diferente do fluxo hidráulico regional, controlado por gravidade e pela geometria de camadas confinantes — por isso é mais difícil de localizar e remediar que o LNAPL.
- **Ghyben-Herzberg: z ≈ 40 × h** (para água do mar típica) relaciona a profundidade da interface água doce-água salgada à altura do nível d'água doce acima do mar — pequenos rebaixamentos elevam muito a interface.

## Próxima aula

[[03-contaminacao-aguas-subterraneas-aula-05-caracterizacao-e-protecao-de-aquiferos|Aula 05 — Caracterização de áreas contaminadas e proteção de aquíferos: vulnerabilidade e perímetros de proteção]]

## Anterior

[[03-contaminacao-aguas-subterraneas-aula-03-retardacao-e-atenuacao|Aula 03 — Retardação e atenuação: sorção, biodegradação e atenuação natural monitorada]]

## Fontes

- Classificação e comportamento de LNAPL/DNAPL: Fetter, C. W. (1999), *Contaminant Hydrogeology*, 2ª ed., Prentice Hall, cap. 7.
- Efeito do poço de monitoramento na espessura aparente de LNAPL: Hampton, D. R. & Miller, P. D. (1988), "Laboratory investigation of the relationship between actual and apparent product thickness in sands", *Proceedings of the NWWA/API Conference on Petroleum Hydrocarbons*.
- Migração de DNAPL controlada por estrutura: Pankow, J. F. & Cherry, J. A. (1996), *Dense Chlorinated Solvents and other DNAPLs in Groundwater*, Waterloo Press.
- Relação de Ghyben-Herzberg: Freeze, R. A. & Cherry, J. A. (1979), *Groundwater*, Prentice-Hall, cap. 9; Custodio, E. & Llamas, M. R. (1983), *Hidrología Subterránea*, Omega, cap. 17.

<!--
nivel: avancado
palavras_corpo: ~1950

mapa_objetivo_secao:
  geologia-avancado-m03-oa03: "NAPL: líquidos que não se misturam com a água" + "Comportamento do LNAPL: flutua sobre o lençol freático" + "Comportamento do DNAPL: afunda e pode atingir a base do aquífero" + "A interface água doce-água salgada em aquíferos costeiros" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: CONTAM-M03-A04-NAPL-001
    claim: "NAPL classifica-se por densidade relativa a agua em LNAPL (densidade menor que 1,0 g/cm3, ex. hidrocarbonetos de petroleo) e DNAPL (densidade maior que 1,0 g/cm3, ex. solventes clorados como TCE e PCE, creosoto)."
    risk: fato
    source: "Fetter 1999, cap. 7"
  - claim_id: CONTAM-M03-A04-DNAPL-002
    claim: "DNAPL, por ser mais denso que a agua, continua migrando atraves da zona saturada sob gravidade ate encontrar uma camada de baixa permeabilidade, podendo migrar em direcao diferente do fluxo hidraulico regional, controlado pela geometria de camadas confinantes."
    risk: fato
    source: "Pankow & Cherry 1996"
  - claim_id: CONTAM-M03-A04-POCO-003
    claim: "A espessura de LNAPL medida em um poco de monitoramento tende a superestimar a espessura real de fase livre presente na formacao, efeito documentado por Hampton & Miller (1988)."
    risk: fato
    source: "Hampton & Miller 1988"
  - claim_id: CONTAM-M03-A04-GHYBENHERZBERG-004
    claim: "A relacao de Ghyben-Herzberg e z = (rho_f/(rho_s - rho_f)) x h; para agua doce (rho=1,000 g/cm3) e agua do mar tipica (rho=1,025 g/cm3), o multiplicador resultante e aproximadamente 40 (cada metro de agua doce acima do nivel do mar corresponde a cerca de 40 m de agua doce abaixo do nivel do mar ate a interface)."
    risk: fato
    source: "Freeze & Cherry 1979, cap. 9; Custodio & Llamas 1983, cap. 17"
-->
