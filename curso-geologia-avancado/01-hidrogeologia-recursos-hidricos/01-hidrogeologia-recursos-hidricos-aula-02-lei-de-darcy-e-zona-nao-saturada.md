# Aula 02: Lei de Darcy e o movimento da água subterrânea; água na zona não saturada

**ID:** geologia-avancado-m01-a02
**Módulo:** [[01-hidrogeologia-recursos-hidricos-modulo|Módulo 01 — Hidrogeologia e recursos hídricos]]
**Duração estimada:** ~27 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** aplicar a lei de Darcy para calcular a vazão e a velocidade do fluxo subterrâneo, reconhecer os limites de validade da lei, e descrever como a água se comporta na zona não saturada entre a superfície e o nível freático.

## Antes de começar, você precisa saber

- Aquífero livre, confinado e semiconfinado; condutividade hidráulica K, transmissividade T e porosidade efetiva ne — Aula 01 deste módulo.
- Conceito de gradiente como variação de uma grandeza por unidade de distância.
- Número de Reynolds como critério de regime de escoamento (laminar × turbulento) — noção de mecânica dos fluidos.

## Conteúdo

### A carga hidráulica: a grandeza que realmente comanda o fluxo

Antes da lei em si, uma peça conceitual indispensável: água subterrânea não flui de "onde há mais água" para "onde há menos água", nem necessariamente de cima para baixo. Ela flui de **maior carga hidráulica** para **menor carga hidráulica**. A carga hidráulica total (h), pelo princípio de Bernoulli aplicado a escoamentos lentos em meio poroso (onde o termo de velocidade é desprezível), é:

h = z + ψ

onde **z** é a carga de elevação (cota do ponto, relativa a um datum) e **ψ** é a carga de pressão (pressão da água no ponto, expressa em altura de coluna d'água). Num piezômetro, h é simplesmente a cota até onde a água sobe no tubo. A carga hidráulica é o que se mede com **potenciômetros/piezômetros** e o que se contorna em **mapas potenciométricos** (Aula 03).

> [!important] O erro conceitual mais caro da hidrogeologia introdutória
> Nível d'água raso não implica carga hidráulica alta, e profundidade do nível d'água **não é** a mesma coisa que carga hidráulica. Dois poços vizinhos, um raso e um profundo, podem ter cargas hidráulicas h idênticas (se ambos estiverem no mesmo aquífero) ou completamente diferentes (se estiverem em aquíferos empilhados com fluxo vertical entre eles) — depende de z e de ψ juntos, nunca de um só.

### A lei de Darcy

Henry Darcy (1856), estudando a filtração de água através de colunas de areia para o abastecimento de Dijon, estabeleceu experimentalmente que a vazão Q através de um meio poroso é proporcional à área da seção A e ao gradiente hidráulico, e inversamente... na verdade diretamente proporcional a uma constante do meio — a condutividade hidráulica K:

Q = -K · A · (dh/dl)

O sinal negativo expressa que o fluxo ocorre no sentido de carga decrescente (dh/dl é negativo no sentido do fluxo; Q é definido positivo nesse sentido). Dividindo pela área, obtém-se a **velocidade de Darcy** ou **descarga específica**:

q = Q/A = -K · (dh/dl)

Um ponto que confunde sistematicamente quem chega da mecânica dos fluidos: **q não é a velocidade real da água**. q é uma velocidade fictícia, calculada como se a água atravessasse toda a seção A — inclusive a parte ocupada pelos grãos sólidos. A velocidade real, média, com que a água efetivamente se move através dos poros interconectados é a **velocidade linear média** (ou velocidade de percolação), vx:

vx = q / ne

onde ne é a porosidade efetiva (Aula 01). Como ne é sempre menor que 1, vx é sempre maior que q — tipicamente de 2 a 10 vezes maior em sedimentos comuns. Essa distinção não é acadêmica: é vx, não q, que se usa para estimar o **tempo de trânsito** de um contaminante ou de um traçador (tema central do Módulo 03, sobre contaminação de águas subterrâneas).

### Limites de validade: quando Darcy deixa de funcionar

A lei de Darcy é empírica e vale numa faixa de condições — não é uma lei universal como a conservação de massa. O critério físico é o regime de escoamento: Darcy é válida para **escoamento laminar**, o que corresponde a número de Reynolds (Re) baixo, tipicamente Re < 1 a 10 em meios porosos (o limite exato depende da definição usada para o comprimento característico).

Dois desvios práticos importam para o geólogo de campo:

- **Limite superior de velocidade**: perto de poços bombeados a alta vazão, em condutos cársticos e em fraturas muito abertas, a velocidade real pode ser alta o bastante para gerar turbulência, e a relação entre q e o gradiente deixa de ser linear (passa a depender do quadrado da velocidade, regime descrito por leis do tipo Forchheimer). Isso é a razão física por trás da **perda de carga não-Darciana** observada em testes de bombeamento com vazão elevada (well loss, tratado na Aula 05).
- **Limite inferior de velocidade**: em argilas muito compactas, com poros extremamente finos, forças eletroquímicas de superfície podem exigir um **gradiente hidráulico limiar** antes que o fluxo comece — abaixo dele, não há fluxo detectável mesmo com gradiente diferente de zero. É um desvio menos citado, mas relevante para justificar por que aquicludos "seguram" água por tempo geológico.

> [!note] Fora desses extremos, a lei é notavelmente robusta
> Para a imensa maioria dos problemas de hidrogeologia regional — fluxo em aquíferos porosos granulares, mesmo em rochas fraturadas quando tratadas como meio poroso equivalente em escala suficientemente grande — Darcy descreve o comportamento com precisão adequada à engenharia. A ressalva do carste e das fraturas isoladas é a exceção que confirma a regra de aplicabilidade.

### Meio poroso equivalente e a hipótese que sustenta todo o formalismo

Um pressuposto silencioso acompanha o uso de K, T e S: tratamos um meio geologicamente heterogêneo (grãos, poros, fraturas discretas) como se fosse um **contínuo homogêneo equivalente**, com propriedades médias representativas de um **volume elementar representativo** (VER) — grande o bastante para que a média não dependa mais do ponto exato de amostragem, mas pequeno o bastante para captar a escala do problema. Em areia bem selecionada, o VER tem escala de centímetros a decímetros. Em rocha fraturada com poucas famílias de fraturas dominantes, o VER pode não existir em escala prática — e aí o meio poroso equivalente é uma aproximação de conveniência, não uma descrição fiel, o que explica a alta incerteza característica de aquíferos cristalinos e cársticos.

### A zona não saturada: entre a superfície e o nível freático

Acima do nível freático, no perfil vertical do solo, a água ocupa apenas parte dos poros — o restante contém ar. Essa é a **zona não saturada** (zona vadosa), e ela se subdivide, de cima para baixo:

1. **Zona de água do solo**: próxima à superfície, sujeita à evapotranspiração e à absorção radicular; o teor de umidade oscila fortemente com o clima e a estação.
2. **Zona intermediária (vadosa propriamente dita)**: onde a umidade se aproxima da **capacidade de campo** — o teor máximo de água que o solo retém contra a gravidade depois da drenagem livre cessar.
3. **Franja capilar**: uma faixa logo acima do nível freático onde a água sobe por capilaridade e satura (ou quase satura) os poros, apesar de estar sob pressão menor que a atmosférica. A espessura da franja capilar é inversamente proporcional ao tamanho dos poros — pode ser de poucos centímetros em areia grossa e mais de um metro em silte.

O movimento de água na zona não saturada é governado pela mesma ideia de Darcy, generalizada: a condutividade hidráulica não saturada K(ψ) **não é constante** — cai drasticamente conforme o teor de umidade diminui, porque os poros maiores (que conduzem a maior parte do fluxo quando saturados) esvaziam primeiro, deixando só os poros finos e tortuosos conduzindo água. A equação que governa esse fluxo transiente e não linear é a **equação de Richards**, cuja solução analítica geral não existe para a maioria dos casos reais — modelos numéricos são a ferramenta padrão.

> [!important] Por que isso importa para a recarga
> A recarga que efetivamente chega ao nível freático não é a chuva total, nem sequer toda a água infiltrada: parte é retida na zona do solo e devolvida à atmosfera por evapotranspiração antes de atingir a franja capilar. A defasagem entre um evento de chuva e o pico de recarga observado no nível freático (dias a décadas, dependendo da espessura da zona não saturada e de K(ψ)) é uma das razões pelas quais aquíferos profundos respondem à precipitação com atraso de meses a anos — tema retomado na Aula 06.

## Exemplo trabalhado

**Situação:** dois piezômetros, A e B, distam 500 m entre si num aquífero confinado de areia (K = 2 × 10⁻⁴ m/s, ne = 0,30, espessura 15 m). A carga hidráulica em A é 42 m e em B, 39,5 m (B está a jusante do fluxo). Calcule a descarga específica, a velocidade linear média e a vazão total por metro de largura da seção.

**Raciocínio.** O gradiente hidráulico é dh/dl = (39,5 − 42) / 500 = −0,005 (adimensional; o sinal negativo confirma que o fluxo vai de A para B, no sentido de carga decrescente). A descarga específica é q = −K · (dh/dl) = −(2 × 10⁻⁴) × (−0,005) = 1 × 10⁻⁶ m/s (no sentido de A para B). A velocidade linear média é vx = q/ne = (1 × 10⁻⁶)/0,30 ≈ 3,3 × 10⁻⁶ m/s, o que equivale a cerca de 0,29 m/dia ou ~105 m/ano — uma velocidade de percolação típica de aquífero arenoso regional, nem instantânea nem geologicamente lenta. A vazão por metro de largura de seção (perpendicular ao fluxo) é q' = q × b = (1 × 10⁻⁶) × 15 = 1,5 × 10⁻⁵ m³/s por metro (ou, usando T = K·b = 3 × 10⁻³ m²/s diretamente: q' = T × |dh/dl| = 3 × 10⁻³ × 0,005 = 1,5 × 10⁻⁵ m²/s — mesmo resultado, confirmando a consistência).

**A lição:** a mesma pergunta pode ser respondida por dois caminhos equivalentes (K·b·gradiente ou T·gradiente); usar T diretamente é mais rápido quando ele já foi estimado por um teste de bombeamento, sem precisar decompor de volta em K e b.

## Erros comuns

- **Confundir a velocidade de Darcy (q) com a velocidade real da água (vx).** q subestima sistematicamente vx por um fator 1/ne — usar q para estimar tempo de trânsito de contaminante gera erro de várias vezes.
- **Tratar "nível d'água raso" como sinônimo de "carga hidráulica alta".** A carga soma cota e pressão; só a posição do nível num piezômetro específico (não a profundidade absoluta) informa a carga naquele ponto.
- **Aplicar Darcy sem verificar o regime de escoamento** em ambientes cársticos, em fraturas abertas ou muito perto de um poço bombeado a vazão elevada, onde o desvio não-linear já é relevante.
- **Achar que a zona não saturada é só "terra seca".** Ela retém e transmite água ativamente; a defasagem de recarga que ela impõe é frequentemente maior que toda a variação sazonal de precipitação.

## O que não concluir

- **Que a lei de Darcy prova que o fluxo é sempre horizontal ou sempre vertical.** A direção do fluxo é dada pelo gradiente de carga hidráulica em três dimensões — pode ter componente vertical relevante mesmo em bacias sedimentares aparentemente tabulares.
- **Que uma condutividade hidráulica não saturada K(ψ) baixa significa solo seco "parado".** Pode significar apenas que os macroporos já drenaram e o fluxo continua, mais lento, pelos poros finos — processo ainda ativo, só mais devagar.
- **Que meio poroso equivalente é uma simplificação sempre segura.** Em rocha fraturada com poucas fraturas dominantes, tratar o meio como contínuo pode mascarar caminhos preferenciais reais de fluxo e de transporte de contaminante — ressalva central do Módulo 03.

## Recap relâmpago

- **Carga hidráulica h = z + ψ** comanda o fluxo, não a profundidade do nível d'água isoladamente.
- **Lei de Darcy: Q = −K·A·(dh/dl)**; a descarga específica q = Q/A não é a velocidade real da água — a velocidade linear média vx = q/ne é sempre maior.
- **Válida para Re baixo** (escoamento laminar); desvia-se em fluxo turbulento (carste, fraturas abertas, perto de poços a alta vazão) e pode exigir gradiente limiar em argilas muito finas.
- **Meio poroso equivalente** trata a heterogeneidade real como contínuo — funciona bem em granulares, é aproximação arriscada em fraturados sem VER definido.
- **Zona não saturada**: solo → intermediária → franja capilar; K(ψ) cai com a umidade (equação de Richards), gerando defasagem entre chuva e recarga efetiva.

## Próxima aula

[[01-hidrogeologia-recursos-hidricos-aula-03-cartografia-hidrogeologica-sistemas-de-fluxo|Aula 03 — Cartografia hidrogeológica: sistemas de fluxo, recarga, descarga e relação rio-aquífero]]

## Anterior

[[01-hidrogeologia-recursos-hidricos-aula-01-aquiferos-e-propriedades-hidraulicas|Aula 01 — Aquíferos e propriedades hidráulicas de solos, sedimentos e rochas]]

## Fontes

- Carga hidráulica, dedução da lei de Darcy e velocidade linear média: Freeze, R. A. & Cherry, J. A. (1979), *Groundwater*, Prentice-Hall, cap. 2.
- Limites de validade da lei de Darcy e número de Reynolds em meios porosos: Fetter, C. W. (2001), *Applied Hydrogeology*, 4ª ed., Prentice-Hall, cap. 4; Bear, J. (1972), *Dynamics of Fluids in Porous Media*, Elsevier.
- Zona não saturada, capacidade de campo, franja capilar e equação de Richards: Fetter (2001), cap. 6; Freeze & Cherry (1979), cap. 6.
- Experimento original de Darcy (1856): Darcy, H., *Les Fontaines Publiques de la Ville de Dijon*, Dalmont, Paris, conforme citado em Freeze & Cherry (1979).

<!--
nivel: avancado
palavras_corpo: ~1700

mapa_objetivo_secao:
  geologia-avancado-m01-oa02: "A carga hidráulica: a grandeza que realmente comanda o fluxo" + "A lei de Darcy" + "Limites de validade: quando Darcy deixa de funcionar" + "Meio poroso equivalente e a hipótese que sustenta todo o formalismo" + "A zona não saturada: entre a superfície e o nível freático" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: HIDRO-M01-A02-CARGA-001
    claim: "A carga hidráulica total h é a soma da carga de elevação z e da carga de pressão psi (h = z + psi), medida diretamente por piezômetros como a cota até onde a água sobe no tubo."
    risk: fato
    source: "Freeze & Cherry 1979, cap. 2"
  - claim_id: HIDRO-M01-A02-DARCY-002
    claim: "A lei de Darcy estabelece Q = -K*A*(dh/dl); a descarga específica q = Q/A não corresponde à velocidade real da água, que é dada pela velocidade linear média vx = q/ne, sendo ne a porosidade efetiva; como ne é menor que 1, vx é sempre maior que q."
    risk: fato
    source: "Freeze & Cherry 1979, cap. 2; Fetter 2001, cap. 4"
  - claim_id: HIDRO-M01-A02-LIMITES-003
    claim: "A lei de Darcy é válida para escoamento laminar, correspondente a número de Reynolds tipicamente abaixo de 1 a 10 em meios porosos; desvia-se em condutos cársticos, fraturas abertas e próximo a poços bombeados a alta vazão, onde a relação entre fluxo e gradiente deixa de ser linear."
    risk: fato
    source: "Fetter 2001, cap. 4; Bear 1972"
  - claim_id: HIDRO-M01-A02-ZNS-004
    claim: "A zona não saturada subdivide-se em zona de água do solo, zona intermediária e franja capilar; a condutividade hidráulica não saturada K(psi) diminui com a redução do teor de umidade porque os poros maiores esvaziam primeiro; o fluxo transiente na zona não saturada é descrito pela equação de Richards."
    risk: fato
    source: "Fetter 2001, cap. 6; Freeze & Cherry 1979, cap. 6"
-->
