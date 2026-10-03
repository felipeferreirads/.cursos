# Aula 05: Testes de bombeamento e de aquífero — rebaixamento, interferência e vazão ótima

**ID:** geologia-avancado-m01-a05
**Módulo:** [[01-hidrogeologia-recursos-hidricos-modulo|Módulo 01 — Hidrogeologia e recursos hídricos]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** interpretar um teste de bombeamento para estimar transmissividade e coeficiente de armazenamento pelo método de Theis/Cooper-Jacob, reconhecer o papel dos testes de interferência e de step-drawdown, e determinar a vazão ótima de um poço.

## Antes de começar, você precisa saber

- Transmissividade T = K·b e coeficiente de armazenamento S (confinado) / produção específica Sy (livre) — Aula 01 deste módulo.
- Superfície potenciométrica e mapa potenciométrico — Aula 03 deste módulo.
- Logaritmo (natural e decimal) e leitura de gráficos em escala log-log e semilog.

## Conteúdo

### O que um teste de bombeamento realmente mede

Um **teste de aquífero** (aquifer test, teste de bombeamento) bombeia um poço a vazão constante e monitora o **rebaixamento** (drawdown, s — a queda da carga hidráulica em relação ao nível estático anterior ao bombeamento) no próprio poço e, idealmente, em um ou mais poços de observação a distâncias conhecidas. É, até hoje, o método mais confiável para estimar T e S/Sy **em escala de campo** — muito mais representativo que testes de laboratório em amostra pequena, porque integra a resposta de um volume de aquífero da ordem de centenas de metros a quilômetros ao redor do poço, incluindo heterogeneidades reais que uma amostra de testemunho nunca capturaria.

### A solução de Theis: a base teórica

Charles Theis (1935) resolveu analiticamente o rebaixamento transiente s, a uma distância r do poço bombeado, num aquífero confinado idealizado (homogêneo, isotrópico, de extensão infinita, espessura constante, poço totalmente penetrante e de diâmetro infinitesimal, vazão constante Q, sem outras fontes/sumidouros):

s(r,t) = (Q / 4πT) · W(u), onde u = r²S / (4Tt)

**W(u)** é a **função de poço** (well function), uma integral exponencial sem solução elementar, tabelada e disponibilizada como a **curva de Theis** — a curva-padrão para o método de ajuste gráfico que dá nome ao método. Na prática, o analista plota o rebaixamento observado versus tempo (ou versus t/r² para múltiplos poços) em papel log-log, sobrepõe à curva de Theis padrão e desliza os dois gráficos até encontrar o melhor ajuste; um **ponto de ajuste** arbitrário (qualquer ponto comum às duas curvas superpostas) fornece os quatro valores (s, t, W(u), u) necessários para isolar T e S das duas equações.

> [!important] Toda estimativa de T e S carrega o peso das hipóteses de Theis
> Nenhum aquífero real é homogêneo, isotrópico e infinito. A solução de Theis é uma idealização deliberada — o valor de T e S obtido é uma média efetiva representativa do volume de aquífero "sentido" pelo teste, não uma medição pontual e exata. Desvios da curva teórica (achatamentos, degraus, subidas abruptas) não são "erro de medição": são a assinatura de que uma das hipóteses de Theis foi violada — e diagnosticá-los é tão importante quanto ajustar a curva.

### A aproximação de Cooper-Jacob: o método de campo mais usado

Para tempos suficientemente longos (u pequeno, tipicamente u < 0,01–0,05), a função de poço W(u) pode ser aproximada por uma expressão logarítmica simples (Cooper & Jacob, 1946):

s ≈ (2,3Q / 4πT) · log₁₀(2,25Tt / r²S)

Essa aproximação torna o gráfico de s versus log(t) (em papel semilog) uma **linha reta**, cuja inclinação (Δs por ciclo logarítmico de tempo) fornece T diretamente:

T = 2,3Q / (4π·Δs)

e cujo intercepto no eixo do tempo (t₀, onde a reta extrapolada cruza s = 0) fornece S:

S = 2,25T·t₀ / r²

O método de Cooper-Jacob é, na prática de campo, muito mais usado que o ajuste gráfico completo de Theis, precisamente porque não exige sobrepor curvas — basta plotar os dados e medir a inclinação de uma reta. A contrapartida é a restrição de validade a u pequeno, o que geralmente exclui os primeiros minutos do teste (quando u ainda não é pequeno o bastante) da análise.

### Lendo os desvios da linha reta: diagnóstico de campo

Um gráfico de Cooper-Jacob raramente é uma reta perfeita do início ao fim — e é justamente nos desvios que está a informação mais valiosa sobre a estrutura real do aquífero:

- **Achatamento da inclinação** (Δs por ciclo menor depois de um tempo): sugere uma **fonte adicional de água** entrando no sistema — recarga por um rio conectado hidraulicamente, ou um aquífero adjacente mais transmissivo alimentando o bombeado por drenança.
- **Aumento da inclinação** (Δs por ciclo maior depois de um tempo): sugere um **limite impermeável** (barreira de fluxo) — o aquífero se estreitando, uma falha selante, ou o limite físico da bacia sendo "sentido" pelo cone de rebaixamento.
- **Degrau abrupto na curva**: frequentemente indica mudança de regime de armazenamento — por exemplo, um aquífero originalmente confinado cujo rebaixamento cruza o topo da unidade durante o teste, passando a se comportar como livre no ponto de observação (a transição de S elástico para Sy de drenagem gravitacional, discutida na Aula 01, produz exatamente esse tipo de inflexão).

> [!note] Um limite hidráulico pode ser tratado como um "poço imagem"
> O método dos poços imagem (Ferris et al., 1962) modela o efeito de um limite de recarga (rio conectado) ou de um limite impermeável (barreira) somando ao rebaixamento real o rebaixamento (ou o efeito espelhado, com sinal invertido no caso de recarga) que seria produzido por um poço fictício, colocado do outro lado do limite, à mesma distância que o poço real está do limite. É a técnica padrão para incorporar contornos físicos reais numa solução originalmente pensada para meio infinito.

### Teste de degraus de vazão (step-drawdown) e a eficiência do poço

O **teste de degraus de vazão** bombeia o mesmo poço em uma sequência de vazões crescentes (degraus), cada uma mantida por um intervalo curto e fixo, medindo o rebaixamento no próprio poço bombeado (não em poço de observação). O rebaixamento total observado no poço de produção tem dois componentes:

s_total = B·Q (perda de carga *no aquífero*, linear com Q) + C·Q² (perda de carga *no poço* — através do filtro, do pré-filtro e da tubulação de produção, devido a turbulência local, não-linear com Q)

O coeficiente **B** reflete propriedades do aquífero (T, S, distância — a mesma física de Theis/Cooper-Jacob); o coeficiente **C** reflete a qualidade construtiva do poço (perda de carga no filtro, no pré-filtro, colmatação — Aula 04). A **eficiência do poço** é definida como a razão entre a perda de carga teórica no aquífero (B·Q) e o rebaixamento total observado; um poço bem construído e desenvolvido tem eficiência alta (>70 %); eficiência baixa aponta para colmatação, sub-desenvolvimento ou projeto construtivo inadequado — diagnóstico direto para as causas de deterioração vistas na Aula 04.

### Interferência entre poços e a vazão ótima

Quando dois ou mais poços bombeiam do mesmo aquífero, seus cones de rebaixamento se superpõem: pelo **princípio da superposição** (válido porque a equação de fluxo transiente em meio confinado é linear), o rebaixamento total num ponto qualquer é a soma dos rebaixamentos que cada poço produziria isoladamente. Essa **interferência** reduz a carga disponível para cada poço individual em relação ao que ele teria bombeando sozinho — e é a razão física por trás da queda de vazão observada quando um campo de poços é operado com espaçamento insuficiente (tema desenvolvido em profundidade no Módulo 04, sobre dimensionamento de campos de poços).

A **vazão ótima** de um poço não é simplesmente "a vazão máxima que a bomba consegue extrair". É a vazão que maximiza a extração útil sujeita a restrições: o rebaixamento não deve expor o topo do filtro (perda de eficiência e possível entrada de ar), não deve aproximar-se do nível crítico que dispara a perda não-Darciana excessiva (C·Q² dominando o rebaixamento — desperdício energético sem ganho proporcional de vazão), e — em operação de campo, com múltiplos poços — deve manter a interferência entre poços dentro de um rebaixamento total tolerável no longo prazo. Na prática, a vazão ótima costuma ser identificada no próprio teste de degraus: o ponto a partir do qual o rebaixamento por unidade de vazão adicional (a inclinação da curva vazão-rebaixamento, dominada pelo termo C·Q² em vazões altas) cresce desproporcionalmente, indicando entrada em regime ineficiente.

## Exemplo trabalhado

**Situação:** um teste de bombeamento com Q = 1.500 m³/dia, observado num piezômetro a r = 60 m, produz um gráfico de Cooper-Jacob (s vs. log t) com inclinação Δs = 0,35 m por ciclo logarítmico e reta extrapolada cruzando s = 0 em t₀ = 0,8 min (= 0,8/1440 dia). Estime T e S.

**Raciocínio.** T = 2,3Q / (4π·Δs) = (2,3 × 1.500) / (4π × 0,35) = 3.450 / 4,40 ≈ 784 m²/dia. Para S, converte-se t₀ para dias: 0,8 min = 0,8/1440 ≈ 5,56 × 10⁻⁴ dia. S = 2,25·T·t₀ / r² = (2,25 × 784 × 5,56 × 10⁻⁴) / 60² = 0,980 / 3.600 ≈ 2,7 × 10⁻⁴. O valor de S, da ordem de 10⁻⁴, é compatível com um aquífero **confinado** (armazenamento elástico) — se o valor obtido fosse da ordem de 10⁻¹, isso denunciaria que a hipótese de confinamento provavelmente não se sustenta e que o piezômetro está, na verdade, respondendo como aquífero livre (drenagem gravitacional), exigindo reinterpretação do teste sob outro modelo (por exemplo, a solução de Neuman para livre com drenagem retardada).

**A lição:** o valor numérico de S obtido do ajuste não é só um resultado — é também um teste de consistência da hipótese de regime (confinado × livre) assumida antes de escolher o método de interpretação; um S "impossível" para o regime assumido é sinal de que o modelo conceitual do teste está errado, não de erro aritmético.

## Erros comuns

- **Aplicar Cooper-Jacob aos primeiros minutos do teste**, quando u ainda não é pequeno o suficiente para a aproximação logarítmica ser válida — produz T e S sistematicamente errados.
- **Ignorar um achatamento ou aumento de inclinação na curva**, tratando-o como "ruído de medição" em vez de investigar recarga adicional ou limite de fluxo.
- **Confundir a perda de carga no poço (C·Q², dependente do estado construtivo) com a perda de carga no aquífero (B·Q, propriedade do meio)** ao interpretar um teste de degraus — atribuir baixa eficiência a "aquífero pobre" quando na verdade é colmatação do próprio poço.
- **Somar diretamente as vazões de poços vizinhos sem considerar a superposição dos rebaixamentos** ao estimar o rebaixamento conjunto de um campo de poços.
- **Definir vazão ótima só pela capacidade máxima da bomba**, sem verificar se o rebaixamento correspondente expõe o filtro ou entra em regime dominado por perda de carga não-Darciana no poço.

## O que não concluir

- **Que a solução de Theis é "a resposta certa" e Cooper-Jacob é uma aproximação inferior.** Cooper-Jacob é matematicamente equivalente a Theis no regime de validade (u pequeno); a escolha é de conveniência operacional, não de precisão.
- **Que um teste de bombeamento de poucas horas caracteriza definitivamente um aquífero regional.** Testes curtos "sentem" apenas o volume de aquífero próximo ao poço; efeitos de limites distantes (um rio a 2 km, uma borda de bacia) só aparecem em testes suficientemente longos para que o cone de rebaixamento os alcance.
- **Que eficiência de poço baixa significa sempre poço malfeito.** Pode refletir deterioração ao longo da vida operacional (Aula 04) em um poço originalmente bem construído — a comparação com o teste de aceitação inicial (logo após a construção) é o que discrimina as duas situações.

## Recap relâmpago

- **Solução de Theis**: s = (Q/4πT)·W(u), idealização de aquífero confinado homogêneo e infinito; **Cooper-Jacob** aproxima W(u) por log(t) para u pequeno, dando T pela inclinação e S pelo intercepto de uma reta em papel semilog.
- **Desvios da reta de Cooper-Jacob são diagnóstico**: achatamento → fonte adicional/recarga; aumento de inclinação → limite impermeável; degrau → mudança de regime de armazenamento.
- **Teste de degraus**: s_total = B·Q + C·Q² separa perda de carga no aquífero (B) de perda de carga no poço (C); a razão define a **eficiência do poço**.
- **Interferência**: rebaixamentos se somam por superposição (meio linear); a **vazão ótima** equilibra extração útil contra exposição do filtro e regime não-Darciano no próprio poço.

## Próxima aula

[[01-hidrogeologia-recursos-hidricos-aula-06-gestao-quantitativa-de-aquiferos|Aula 06 — Gestão quantitativa: recarga, balanço hídrico, intrusão salina, vazão sustentável e outorga]]

## Anterior

[[01-hidrogeologia-recursos-hidricos-aula-04-pocos-tubulares-e-de-monitoramento|Aula 04 — Poços tubulares e de monitoramento: projeto, perfuração, construção e manutenção]]

## Fontes

- Solução de Theis para rebaixamento transiente em aquífero confinado: Theis, C. V. (1935), "The relation between the lowering of the piezometric surface and the rate and duration of discharge of a well using ground-water storage", *Eos, Transactions AGU*, 16(2), 519–524.
- Aproximação logarítmica de Cooper-Jacob: Cooper, H. H. & Jacob, C. E. (1946), "A generalized graphical method for evaluating formation constants and summarizing well-field history", *Eos, Transactions AGU*, 27(4), 526–534.
- Método dos poços imagem para limites de fluxo: Ferris, J. G., Knowles, D. B., Brown, R. H. & Stallman, R. W. (1962), *Theory of Aquifer Tests*, USGS Water-Supply Paper 1536-E.
- Teste de degraus, perda de carga no poço (well loss) e eficiência do poço: Driscoll, F. G. (1986), *Groundwater and Wells*, 2ª ed., Johnson Screens, cap. 16; Jacob, C. E. (1947), "Drawdown test to determine effective radius of artesian well", *Trans. ASCE*, 112, 1047–1064.
- Princípio da superposição e interferência entre poços: Fetter, C. W. (2001), *Applied Hydrogeology*, 4ª ed., Prentice-Hall, cap. 5.

<!--
nivel: avancado
palavras_corpo: ~1950

mapa_objetivo_secao:
  geologia-avancado-m01-oa03: "O que um teste de bombeamento realmente mede" + "A solução de Theis: a base teórica" + "A aproximação de Cooper-Jacob: o método de campo mais usado" + "Lendo os desvios da linha reta: diagnóstico de campo" + "Teste de degraus de vazão (step-drawdown) e a eficiência do poço" + "Interferência entre poços e a vazão ótima" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: HIDRO-M01-A05-THEIS-001
    claim: "A solução de Theis (1935) para rebaixamento transiente em aquífero confinado idealizado é s(r,t) = (Q/4*pi*T)*W(u), com u = r^2*S/(4*T*t), onde W(u) é a função de poço tabelada; pressupõe aquífero homogêneo, isotrópico, de extensão infinita e poço totalmente penetrante."
    risk: fato
    source: "Theis 1935, Eos Trans. AGU 16(2)"
  - claim_id: HIDRO-M01-A05-COOPERJACOB-002
    claim: "A aproximação de Cooper-Jacob (1946) é válida para u pequeno (tipicamente u < 0,01-0,05) e permite estimar T pela inclinação de s versus log(t) em papel semilog (T = 2,3Q/(4*pi*Delta_s)) e S pelo intercepto t0 onde a reta extrapolada cruza s=0 (S = 2,25*T*t0/r^2)."
    risk: fato
    source: "Cooper & Jacob 1946, Eos Trans. AGU 27(4)"
  - claim_id: HIDRO-M01-A05-LIMITES-003
    claim: "Desvios da reta de Cooper-Jacob indicam violação das hipóteses de Theis: achatamento da inclinação sugere fonte adicional de recarga (limite de recarga), aumento de inclinação sugere limite impermeável (barreira de fluxo); o método dos poços imagem de Ferris et al. (1962) modela esses limites com um poço fictício espelhado."
    risk: fato
    source: "Ferris et al. 1962, USGS Water-Supply Paper 1536-E"
  - claim_id: HIDRO-M01-A05-STEPTEST-004
    claim: "No teste de degraus de vazão, o rebaixamento total no poço bombeado se decompõe em perda de carga linear no aquífero (B*Q) e perda de carga não linear no poço (C*Q^2, well loss, associada a turbulência no filtro/pré-filtro/tubulação); a eficiência do poço é a razão entre a perda teórica no aquífero e o rebaixamento total observado."
    risk: fato
    source: "Jacob 1947, Trans. ASCE 112; Driscoll 1986, cap. 16"
  - claim_id: HIDRO-M01-A05-SUPERPOSICAO-005
    claim: "Pelo princípio da superposição, válido para a equação de fluxo transiente linear em aquífero confinado, o rebaixamento total num ponto devido a múltiplos poços bombeados é a soma dos rebaixamentos que cada poço produziria isoladamente, o que explica a interferência entre poços vizinhos."
    risk: fato
    source: "Fetter 2001, cap. 5"
-->
